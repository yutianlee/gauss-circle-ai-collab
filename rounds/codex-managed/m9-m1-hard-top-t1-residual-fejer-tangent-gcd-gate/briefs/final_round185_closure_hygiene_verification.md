# Task brief: final Round-185 closure hygiene verification

- Campaign: m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate
- Round: 185
- Role: independent final closure verifier
- Access mode: selected current-workspace context
- Write only:
  rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reviews/final_round185_closure_hygiene_verification.md

## Objective

Independently audit the complete current Round-185 closure after lifecycle
bookkeeping and the final TeX/control-byte repairs. Return GREEN only if the
graph, campaign, lifecycle, patch reverse/replay evidence, hashes, paths,
artifact hygiene, tests, owner scope, and exponent quarantine agree
exactly.

## Required context

Read protocol.md; state/proof_obligations.yml; state/active_campaign.yml;
state/best_proof_draft.md; state/current_round.md; state/current_state.md;
state/last_validation.md; state/last_validation_report.md;
state/next_campaign.md; state/next_round_plan.yml; state/project_summary.md;
state/round_ledger.yml; state/validation_matrix.yml;
human/current_directives.md; manifests/reading_packet.md; the Round-185
plan.json, state_patch.json, synthesis.md, candidate, adjudication, all four
pre/postapplication audits, and
controls/conductor_round185_closure_controls.md;
controls/conductor_round185_postclosure_tex_repair_control.md; and the
durable kernel
proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md.

You may inspect the remaining Round-185 campaign artifacts as needed to
verify cited hashes, paths, report-contract compliance, and provenance.

## Required controls

1. Verify the graph hash
   f43248060d7876a96d4554cd13372dbf267387bcbe44a832b87cd5f571801575,
   graph validation, unique IDs, and protected statuses.
2. Verify campaign validation, active-campaign versus plan deep identity,
   complete status, three completed tasks, terminal label, and Round-185
   ledger closure with Round 186 pending design.
3. Verify the exact 1/1/0/20/31 State Patch inventory and independently
   check, or rigorously audit the existing independent checks of, the exact
   inverse to f16b7a43... and frozen-time byte-identical replay.
4. Verify every untouched frozen hash recorded in the postapplication
   audit and all 15 distinct patch evidence paths. For the three
   postclosure TeX-repaired artifacts, verify the exact current hashes and
   exact byte-reversal to the historical hashes recorded in the repair
   control; do not require the historical hash to equal the repaired
   current byte string.
5. Verify that the validation matrix top-level metadata is current and all
   required Round-185 gates are GREEN.
6. Scan the assigned closure corpus for strict UTF-8, replacement
   characters, isolated control bytes, trailing whitespace, missing final
   line feeds, malformed recent TeX, and unbalanced math delimiters.
   CRLF and LF are both acceptable. Eight frozen evidence files may retain
   one extra terminal blank line solely to preserve reviewed hashes.
7. Run structured-data parsing, git diff whitespace checking, repository
   compilation if available, and all repository unit tests.
8. Confirm the proof draft states only the accepted parity/tangent-gcd
   reduction, monotone and bounded-height sector, exact high-height
   complement, and first open full-factor-Y relation.
9. Confirm the complete t=1 residual, all t>=2 and near-resonant pieces,
   both M1 parents, every M2 parent, endpoint uniformity, M9, both bridges,
   GC-target, and every exponent remain unpromoted.

## Output contract

Write a seven-section report containing:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect.

Do not edit the graph, proof draft, validation matrix, lifecycle files,
campaign plan, patch, synthesis, candidate, kernel, reports, controls, or
other shared state. If any check fails, report the first exact failure and
recommend no closure until repaired.
