from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from math_collab.campaigns import prepare_campaign, validate_campaign


class CampaignTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "problems").mkdir()
        (self.root / "state").mkdir()
        (self.root / "problems/gauss_circle.md").write_text("problem\n", encoding="utf-8")
        (self.root / "state/control_models.md").write_text("controls\n", encoding="utf-8")
        self.graph_path = self.root / "state/proof_obligations.yml"
        self.graph_path.write_text("{}\n", encoding="utf-8")
        self.graph = {"proof_obligations": [{"id": "target"}], "rejected_claims": []}
        self.manifest = {
            "round_index": 1,
            "round_type": "test",
            "campaign_id": "test-campaign",
            "status": "ready",
            "max_concurrency": 1,
            "target_obligations": ["target"],
            "frozen_target": {"question": "Q?", "reference_formula": "F", "quantities": []},
            "completion_criteria": ["done"],
            "controls": ["control"],
            "tasks": [
                {
                    "id": "blind_task",
                    "role": "blind_rederiver",
                    "access_mode": "statement_only",
                    "target": "derive",
                    "context_files": ["problems/gauss_circle.md", "state/control_models.md"],
                    "excluded_context": ["claimant"],
                    "required_controls": ["control"],
                    "required_output": ["proof"],
                }
            ],
            "review_seams": [{"id": "normalization", "requirement": "check"}],
        }

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_valid_statement_only_campaign(self) -> None:
        self.assertEqual(validate_campaign(self.manifest, self.graph, root=self.root), [])

    def test_statement_only_context_leak_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["tasks"][0]["context_files"].append("state/proof_obligations.yml")
        issues = validate_campaign(manifest, self.graph, root=self.root)
        self.assertTrue(any("leaks claimant context" in issue for issue in issues))

    def test_concurrency_is_bounded(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["max_concurrency"] = 4
        issues = validate_campaign(manifest, self.graph, root=self.root)
        self.assertTrue(any("max_concurrency" in issue for issue in issues))

    def test_prepare_writes_minimal_brief_and_provenance(self) -> None:
        paths = prepare_campaign(
            self.manifest, self.graph, root=self.root, graph_path=self.graph_path
        )
        brief = self.root / "rounds/codex-managed/test-campaign/briefs/blind_task.md"
        plan = self.root / "rounds/codex-managed/test-campaign/plan.json"
        self.assertIn(brief, paths)
        self.assertTrue(plan.exists())
        text = brief.read_text(encoding="utf-8")
        self.assertIn("First doubtful or unproved step", text)
        self.assertNotIn("state/proof_obligations.yml", text)


if __name__ == "__main__":
    unittest.main()
