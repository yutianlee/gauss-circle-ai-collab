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

    def test_created_positive_judge_evidence_is_not_duplicated_as_inconclusive(self) -> None:
        judge_ref = "rounds/test/judge.md"
        patch = {
            "proof_obligations": {
                "create": [
                    {
                        "id": "new-claim",
                        "status": "proved_internal",
                        "evidence": {
                            "positive": [judge_ref],
                            "negative": [],
                            "inconclusive": [],
                        },
                    }
                ]
            }
        }
        graph, _ = apply_state_patch(self.graph, patch, judge_ref=judge_ref)
        evidence = graph["proof_obligations"][0]["evidence"]
        self.assertEqual(evidence["positive"], [judge_ref])
        self.assertEqual(evidence["inconclusive"], [])

    def test_evidence_removed_is_bucket_specific(self) -> None:
        judge_ref = "rounds/test/judge.md"
        graph = {
            "proof_obligations": [
                {
                    "id": "claim",
                    "status": "proved_internal",
                    "evidence": {
                        "positive": [judge_ref],
                        "negative": [],
                        "inconclusive": [judge_ref, "rounds/test/diagnostic.md"],
                    },
                }
            ],
            "rejected_claims": [],
        }
        patch = {
            "proof_obligations": {
                "update": [
                    {
                        "id": "claim",
                        "evidence_removed": {"inconclusive": [judge_ref]},
                    }
                ]
            }
        }
        updated, _ = apply_state_patch(graph, patch)
        evidence = updated["proof_obligations"][0]["evidence"]
        self.assertEqual(evidence["positive"], [judge_ref])
        self.assertEqual(evidence["inconclusive"], ["rounds/test/diagnostic.md"])


if __name__ == "__main__":
    unittest.main()
