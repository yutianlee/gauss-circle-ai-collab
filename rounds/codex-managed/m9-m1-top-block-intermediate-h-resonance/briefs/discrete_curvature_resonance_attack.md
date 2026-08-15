# Task Brief: discrete_curvature_resonance_attack

- Campaign: `m9-m1-top-block-intermediate-h-resonance`
- Research round: `56` (`intermediate_h_discrete_curvature_resonance`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `7d2604d4c686e45d0348b1087741c812bb8943ee141db1d05aab22f84cb1dd11`
- Generated: `2026-08-13T18:19:43.129664+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the discrete quadratic curvature resonances of the remaining intermediate-h, large-q top-block window be averaged over h to give the missing square-root aggregate bound, or is there a sharp actual-profile resonance obstruction?

## Reference formula and distinctions

W_J^core=sum_(hq in J,q odd,h>L) chi_4(q) Omega_X^*(hq,h)(hq)^(-3/4)e(sqrt(Xhq)), where Y asymp sqrt(X), |J|<=R asymp sqrt(Y), L=(log(2X))^B, q>=2sqrt(hq), h<=sqrt(hq)/2.

- odd-q discrete first and second differences
- large-h regime sqrt(R)<h<=sqrt(Y)/2
- resonance parameter modulo one
- averaged resonance count over h
- actual angular sampled amplitude
- short hyperbola-strip geometry
- perfect-fourth-power rational resonance
- target unweighted window size sqrt(R)
- full H/R exponent ledger

## Assigned target

Derive and attack the averaged modulo-one curvature resonance sum over the exact intermediate-h, large-q core; prove a target window theorem or isolate a sharp resonance survivor.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-top-block-intermediate-h-resonance/derivation_packet.md`
- `rounds/codex-managed/m9-m1-top-block-low-leg-curvature/synthesis.md`
- `rounds/codex-managed/m9-m1-global-angular-shifted-correlation/synthesis.md`
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`

## Required controls

- `odd_q_discrete_phase`
- `large_curvature_mod_one`
- `resonance_spacing_average`
- `actual_profile_amplitude`
- `hyperbola_window_edges`
- `perfect_fourth_power`
- `target_exponent_ledger`
- `low_leg_overlap`
- `alpha_scope`
- `downstream_scope`

## Required deliverables

- seven-section report
- exact averaged resonance theorem or no-go
- residual-core exponent ledger

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
