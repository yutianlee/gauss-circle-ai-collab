# Task brief: literal primitive-conductor parity attack

- Round: 179
- Role: discovery
- Access: selected context
- Starting graph:
  e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27
- Write only:
  rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/reports/literal_primitive_conductor_parity_attack.md

## Context files

Read exactly:

1. protocol.md;
2. state/proof_obligations.yml;
3. state/active_campaign.yml;
4. strategy/round179_m2_hard_top_t1_residual_k17a_primitive_conductor_orientation_defect_strategy.md;
5. proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md;
6. proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md;
7. rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reviews/conductor_round178_adjudication.md; and
8. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/synthesis.md.

## Objective

Attack only the exact aggregate high-conductor estimate (177.K34) through
the primitive-conductor parity projection. Rederive every factor in
(179.S4)--(179.S7), prove or reject the target-safe trace component, then
work on the complete literal orientation defect with all selectors,
squarefree/coprimality fields, physical lifts, determinant ranges, phases,
hard endpoints, and zero extensions retained.

Seek, in order: a proof of (177.K34); a complete nontrivial literal sector
where the defect vanishes or contracts at target scale; or the first exact
selector/multiplicity/capacity self-return. Do not pivot to (177.K35), K26,
another parent, a bridge, or exponent work.

## Mandatory controls

- odd modulus and unit residue;
- exact-conductor Möbius projection and the \(d=1\) term;
- \(q/u_0\) normalization;
- \(q\mid u_0\) and \(u_0\mid u\) divisor summation;
- literal two-orientation bucket definitions;
- no double counting of the proved low-\(q\) packet;
- endpoint, parity, selector, lift, and zero-extension retention;
- arbitrary-bucket false control;
- restored \(L\sqrt q\), \(Lq\), \(Lu_0\), and \(Lu\) stop tests;
- no aliaswise pivot; and
- downstream and exponent quarantine.

## Output contract

Write a seven-section report:

1. Result: exact lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect.

Do not edit shared state, the proof draft, validation matrix, strategy,
synthesis, or any sibling artifact.
