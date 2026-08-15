# Task brief: hostile endpoint scope review

Campaign: `m9-endpoint-kernel-validation`  
Task: `hostile_endpoint_scope_review`  
Role: hostile seam reviewer  
Graph SHA-256: `90f44e99047eff10b620228e8480a88984f9dbbca4445bb8921667d9d3575031`

You are not the Round-6 claimant. Read and line-audit:

- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/endpoint_sine_kernel_attack.md`;
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/endpoint_dual_signed_attack.md`;
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reviews/conductor_source_and_seam_audit.md`.

Do not edit shared state or synthesis files. Write only
`rounds/codex-managed/m9-endpoint-kernel-validation/reports/hostile_endpoint_scope_review.md`.

## Objective

Try to refute or sharply rescope:

1. the claim that a fixed smooth profile has \(D/L\) average and occasional
   one-sided, one-class first-annulus subtotal;
2. the exact-square/near-square local transition and its claimed uniform
   \(L\)-range;
3. the statement that none of these subtotals lower-bounds the full signed
   block;
4. the endpoint dual reductions, especially the smooth-symbol hypothesis,
   the treatment of even products, the large-gcd cutoff, and whether the
   proposed packet lemma is genuinely weaker than the character-erasing
   mean square.

Check actual Vaaler amplitudes, both frequency signs, nearest-odd cells,
endpoint support, fixed versus adversarial profiles, special square versus
uniform real \(X\), and any assertion that could prove a false arbitrary
coefficient analogue.

## Required report contract

Give the first false or doubtful line if one exists; otherwise give a scoped
validation proof. Include the exact surviving statement, controls, artifacts
used, and recommended state effect. No numerical work is expected.
