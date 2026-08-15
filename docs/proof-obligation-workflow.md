# Proof-Obligation and Campaign Workflow

The proof obligation, not the transcript or agent, is the unit of progress.

## State model

- `state/proof_obligations.yml`: authoritative accepted graph.
- `state/active_campaign.yml`: frozen current target and task briefs.
- `state/current_round.md`: generated summary of the active numbered round.
- `state/round_ledger.yml`: durable round status, exit gates, closing assessments, and next-round decisions.
- `state/failure_ledger.md`: generated anti-memory from rejected claims.
- `state/control_models.md`: false analogues and boundary tests.
- `state/validation_matrix.yml`: independent acceptance gates for a candidate kernel.
- `state/best_proof_draft.md`: proof text assembled only from accepted graph state.
- `manifests/reading_packet.md`: compact derived project state.

Historical fixed-agent rounds remain evidence. Their owner fields are historical stewards, not active assignments.

## Campaign flow

1. The conductor designs a numbered round and freezes one exact obligation, definitions, range, dependencies, forbidden shortcuts, and completion rule.
2. Extract relevant rejected claims into a barrier packet.
3. Prepare minimal, context-isolated briefs.
4. Run up to three orthogonal subagents, such as discovery, no-go, blind derivation, source audit, or numerical falsification.
5. Select the smallest candidate kernel that could change the graph.
6. Review different failure seams independently; route at least one important derivation around the claimant.
7. Reproduce diagnostic computations and attack with adversarial controls.
8. Fill the validation matrix.
9. The conductor closes the round, records its assessment, and writes any State Patch.
10. Only then update the graph and proof draft and design the next numbered round.

Reports must include an exact lemma or no-go result, proof, first doubtful step, control outcome, dependencies, and recommended state effect.

## Commands

```powershell
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
python -m math_collab.campaigns validate
python -m math_collab.campaigns prepare
python -m math_collab.campaigns status
python -m unittest discover -s tests -v
```

`prepare` writes a plan snapshot, task briefs, `state/current_round.md`, the compatibility `state/next_campaign.md`, and the generated failure ledger. It does not launch Codex subagents, edit the proof graph, or certify mathematics.

## State Patch rules

The existing JSON-compatible YAML patch format remains supported. Candidate reports do not patch the graph directly. Only the conductor proposes a patch, and promotion remains subject to graph invariants:

- computation can add only diagnostic evidence;
- external dependencies require source cards;
- downstream obligations cannot outrun blockers;
- M9 cannot be promoted without M9-M1 and M9-M2 plus endpoint uniformity;
- signed/unsigned and raw/weighted quantities require explicit connecting lemmas;
- a failed campaign may record a new obstruction or rejected claim without promoting its target.

## Active pilot

The first campaign adjudicates raw near-collision counts versus genuine $\beta$-weighted mass. The $X^{3/8}$ split is unchanged until the normalization, counting, coefficient-summation, endpoint, blind-rederivation, hostile-audit, and local-computation gates have been evaluated.
