from __future__ import annotations

import unittest

from math_collab.proof_obligations import apply_state_patch, validate_patch_against_graph


class ProofObligationPatchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = {
            "proof_obligations": [],
            "rejected_claims": [
                {"id": "old-claim", "reason": "old reason", "evidence": ["old.md"]}
            ],
        }

    def test_correct_rejected_updates_existing_claim(self) -> None:
        patch = {
            "proof_obligations": {
                "correct_rejected": [
                    {
                        "id": "old-claim",
                        "reason": "corrected scope",
                        "evidence_added": ["new.md"],
                    }
                ]
            }
        }
        self.assertEqual(validate_patch_against_graph(self.graph, patch), [])
        graph, result = apply_state_patch(self.graph, patch, round_index=27)
        claim = graph["rejected_claims"][0]
        self.assertEqual(claim["reason"], "corrected scope")
        self.assertEqual(claim["evidence"], ["old.md", "new.md"])
        self.assertEqual(claim["last_updated_round"], 27)
        self.assertEqual(result.corrected_rejected, ["old-claim"])

    def test_correct_rejected_requires_existing_claim(self) -> None:
        patch = {
            "proof_obligations": {
                "correct_rejected": [{"id": "missing", "reason": "correction"}]
            }
        }
        issues = validate_patch_against_graph(self.graph, patch)
        self.assertTrue(any("unknown claim" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
