# Task brief: statement-only profile rederivation

Campaign: `m9-endpoint-kernel-validation`  
Task: `blind_profile_rederivation`  
Role: statement-only blind rederiver  
Graph SHA-256: `90f44e99047eff10b620228e8480a88984f9dbbca4445bb8921667d9d3575031`

Do not read the Round-6 profile report before completing your derivation.
Do not edit shared state or synthesis files. Write only
`rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`.

## Statement to rederive or refute

Let \(y=\lfloor\sqrt X\rfloor\). Construct one explicit, fixed,
nonnegative smooth step \(\eta\) and band \(W(t)=\eta(t)-\eta(2t)\), with a
unit plateau. For \(D_j=2^{-j}y\), prove an exact partition of unity on the
integers \(1\le d\le y\), including a bottom remainder, such that:

1. every block has
   \(\|w\|_\infty+\sum_d|w(d+1)-w(d)|\le4\);
2. every active \(D_j\ge X^{1/4}\) has
   \(\sum_d|w_j(d)|\ge D_j/8\) for all sufficiently large \(X\);
3. \(H_D=\lfloor DX^{-1/4}\rfloor\) satisfies
   \(\tfrac12DX^{-1/4}\le H_D\le DX^{-1/4}\);
4. every interior active block is a full fixed \(C_c^\infty\) rescaling,
   while exactly one top block carries the finite endpoint jump;
5. the union of inactive blocks contributes \(O(X^{1/4})\) before Fourier
   expansion.

Determine exactly which accepted BV, B1, W-1, TTY, Fejer, and smooth-Poisson
hypotheses follow. Do not assume that discrete BV implies continuum
smoothness at the endpoint.

## Required report contract

Give the result, exact statement and hypotheses, independent proof, first
doubtful step, endpoint/partition/BV/mass controls, dependencies used, and a
recommended state effect. If any constant or transfer is false, give the
smallest correction.

Allowed context: `protocol.md`, `state/proof_obligations.yml`,
`rounds/codex-managed/m9-unit-frequency-w1-validation/reports/h4_weight_normalization_review.md`,
and `rounds/codex-managed/m9-frequency-phase-diagram/synthesis.md`.
