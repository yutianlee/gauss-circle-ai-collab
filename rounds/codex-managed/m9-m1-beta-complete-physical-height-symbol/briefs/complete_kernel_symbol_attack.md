# Task Brief: complete_kernel_symbol_attack

- Campaign: `m9-m1-beta-complete-physical-height-symbol`
- Research round: `32` (`beta_complete_physical_height_symbol`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `e53cc040c84e084cfa37f22c4a745080909deac6c510b61953eced488362f0b5`
- Generated: `2026-08-13T00:09:18.061403+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can one form the exact common physical-height regular kernel for omega G+(1-omega)R1-omega E1 and prove its lambda^(-2)/lambda^(-3) weighted symbol bounds through rho=0, the v=0 axial split, finite radial sides, and joint U,V,S exhaustion?

## Reference formula and distinctions

After identical-mask recombination and one combined delta/log subtraction, prove |K_complete(L,nu)| <= X^epsilon lambda^(-2) w_b(nu) and |partial_L K_complete(L,nu)| <= X^epsilon lambda^(-3) w_b(nu), with integrable w_b, compatible translated endpoint traces, polylogarithmic b loss after extracting v=0, and summable radial/height sides.

- exact common K_complete(L,nu)
- rho=0 Taylor coefficients of G/E1/R1
- combined diagonal/log ownership
- ordinary L derivative at fixed physical nu
- v=0 axial residue and b downarrow zero
- radial hard-endpoint and horizontal-side terms
- joint U,V,S exhaustion
- full h,D_j,x,q and external normalization ledger

## Assigned target

Construct K_complete(L,nu), expand the rho-regular Taylor package, extract the axial residue, and prove the lambda^(-2)/lambda^(-3) weighted bounds with radial-side and joint-height exhaustion. If full closure fails, isolate the smallest exact radial or axial operator and quantify its capacity.

## Permitted context

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-radial-endpoint-renormalization/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/reports/blind_hierarchical_recombined_identity.md`
- `rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/reviews/conductor_rho_taylor_ledger.md`

## Required controls

- `common-kernel-ownership`
- `rho-Taylor-and-residue`
- `physical-height-derivative`
- `axial-b-limit`
- `radial-side-exhaustion`
- `normalization-and-q-power`

## Required deliverables

- Complete weighted-symbol proof or smallest explicit survivor
- Axial, radial-side, tail, and normalization ledger
- Seven-section report at the assigned path

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
