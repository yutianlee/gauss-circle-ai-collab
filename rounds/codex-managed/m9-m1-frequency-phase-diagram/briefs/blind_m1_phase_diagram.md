# Task brief: blind M1 phase diagram

Campaign: `m9-m1-frequency-phase-diagram`  
Round: 10  
Role: statement-only parameter deriver

Read only:

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `state/best_proof_draft.md`
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`

Do not read another Round-10 report. Do not edit shared state.

## Assigned target

For the actual positive-frequency M1 block

\[
B_1(D,L;X)=
\sum_{h\asymp L}\frac{\Phi(h/(H_D+1))}{h}
\sum_{d\asymp D}\chi_4(d)w_D(d)e(hX/d),
\]

with \(H_D\asymp DX^{-1/4}\), derive from scratch every justified direct
bound available from summation by parts, frequency-first geometric/Dirichlet
kernels, van der Corput/exponent pairs, and the actual fixed-BV dyadic
profile. Translate them into exact regions for

\[
D=X^\delta,\qquad L=X^\ell,qquad
1/4\le\delta\le1/2,quad0\le\ell\le\delta-1/4.
\]

Determine whether any combination proves the whole M1 range. If not, state
the exact smallest uncovered region and the first missing estimate. Treat the
hard top profile separately from smooth blocks. Preserve the spatial
\(\chi_4(d)\) and actual Vaaler factor; no arbitrary-coefficient surrogate.

Required controls: both frequency signs, \(L=1\), \(L\asymp H_D\),
\(D=X^{1/4}\), \(D=X^{1/2}\), exact-square \(X\), and all normalization
powers. No numerical experiment is needed.

## Report contract

Write only
`rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/blind_m1_phase_diagram.md`.
Include: Result; exact statement/hypotheses; proof; first doubtful or unproved
step; controls and outcomes; exact dependencies; recommended state effect.
A rigorous no-go or empty-region calculation is a successful result.
