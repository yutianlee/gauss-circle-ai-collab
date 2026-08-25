# Task Brief: blind_joint_matrix_spectral_feasibility

- Campaign: `m9-m2-unbalanced-level-four-kuznetsov-matrix-gate`
- Research round: `143` (`m9_m2_unbalanced_level_four_kuznetsov_matrix_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789`
- Generated: `2026-08-23T20:05:58.767482+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the fully gcd-restored inverse-selector completion of the literal flat-smooth strict-UNBAL M2 wave admit a fixed-level-four generalized-Kloosterman and Kuznetsov/spectral-large-sieve estimate that preserves chi_4 across moduli and beats the accepted envelope uniformly at the prescribed real centre; if not, what is the first exact cusp, modulus, coefficient-matrix, Bessel-transform, spectral, self-return, or capacity obstruction?

## Reference formula and distinctions

Let X=N_0+xi with N_0=floor X and 0<=xi<1, D=X^delta, L=X^ell, R=X/D, K=XL/D^2, Delta=D/L=R/K, and 1/4<delta-ell<1/2. The flat packet is R_(D,L)(X)=sum_(r asymp R, r odd)chi_4(r)W(X/(rD))sum_(k asymp K)q_L(4Xk/r^2)k^(-1)e(Xk/r). With r=gn, k=gj, (j,n)=1, b_(g,n)(j)=q_L(4Xj/(gn^2))(gj)^(-1)e(xi j/n), gamma_(g,n)(m)=b_(g,n)(inverse_n(m)) on units, and normalized Fourier transform gammahat_(g,n)(h), the exact inverse-first row is sum_(h mod n)gammahat_(g,n)(h)S(N_0,h;n). The full owner retains sum_(g,n odd, gn asymp R)chi_4(g)chi_4(n)W(X/(gnD)) and every gcd stratum. The target is O_epsilon(X^(1/4+epsilon)), or a strictly smaller owner-complete survivor below the accepted envelope min(Delta,sqrt(XL/D)+sqrt(X/(LD))).

- The modulus sign chi_4(n) must remain inside the complete n-sum; replacing it by its modulus or an arbitrary coefficient theorem is not a signed gain.
- An identity with standard or generalized Kloosterman sums is useful only after the exact level, cusps, allowed moduli, residue normalization, and all root-of-unity factors are proved.
- Kuznetsov normally accepts a common Kloosterman argument and a controlled modulus test. Here gammahat_(g,n)(h) is a joint rough function of n and h created by the inverse selector; its separation cost is part of the theorem, not a free preprocessing step.
- All holomorphic, Maass, Eisenstein, exceptional, oldform, continuous-spectrum, and Bessel-transform terms must be included before a spectral estimate is called owner-complete.
- The real-centre repair e(xi j/n) is legal inside b_(g,n); no proof may silently set xi=0 or discard moving profiles, entries, exits, or gcd strata.
- Smooth-weight-first completion is the exact Ramanujan/additive return of size Delta X^epsilon. A proposed spectral gain must not merely transform back to that identity or to the original reciprocal wave.
- This round concerns one flat-smooth strict-UNBAL owner only. It cannot promote sharp, clipped, starred, transition, hard-TOP, BAL, complete M9-M2, endpoint, M9, or the global theorem.

## Assigned target

Independently decide from the frozen flat-wave and inverse-first identities whether a fixed-level trace formula or spectral large sieve can exploit the odd-modulus chi_4 sign with the literal joint gammahat_(g,n)(h) coefficient. Derive all normalizations and capacity from scratch, or prove the first exact no-go.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-118 through Round-143 nonblind artifacts`
- `all Round-143 sibling reports`

## Required controls

- `exact_gcd_restored_inverse_first_identity`
- `chi4_modulus_sign_and_level_four_embedding`
- `cusp_modulus_progression_and_root_of_unity`
- `joint_gammahat_n_h_coefficient_geometry`
- `real_centre_profile_and_endpoint_ownership`
- `Kuznetsov_test_Bessel_transform_hypotheses`
- `holomorphic_Maass_Eisenstein_exceptional_ledger`
- `spectral_large_sieve_common_sequence_and_norms`
- `full_polytope_D_L_R_K_Delta_capacity`
- `Ramanujan_original_wave_and_spectral_self_return`
- `actual_character_vs_unsigned_adversary`
- `downstream_owner_and_exponent_scope`

## Required deliverables

- A seven-section statement-only analytic report.
- A self-contained fixed-level Kloosterman/Kuznetsov normalization and joint-coefficient feasibility derivation.
- A target estimate, strict signed spectral survivor, or first rigorous obstruction.
- Write only the assigned report and make no graph or shared-state edit.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
