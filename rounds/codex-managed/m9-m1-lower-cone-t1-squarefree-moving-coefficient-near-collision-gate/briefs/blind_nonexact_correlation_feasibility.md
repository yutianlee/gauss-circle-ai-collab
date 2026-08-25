# Task Brief: blind_nonexact_correlation_feasibility

- Campaign: `m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate`
- Research round: `150` (`m9_m1_lower_cone_t1_squarefree_moving_coefficient_near_collision_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `b6c5ee5b0d51d347876b389c05c78596c069b190af715d297bd937701ea893b6`
- Generated: `2026-08-24T12:54:59.086981+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the complete nonzero near-collision collar in the exact Round-149 moving-row energy contribute O_epsilon(R^2 D X^epsilon), after an exact two-row expansion of both gcd-lift coefficients, prefixes, and profiles; if not, what is the first exact rank, cutoff, shifted-factor, source-hypothesis, D=1, or all-scale obstruction?

## Reference formula and distinctions

Let A_d(L,q)=chi_4(Lq)B_(d,U)(L)W_(d,U)(L/q)/L with (L,q)=1 and q asymp LQ. For q_i=h r_i, (r_1,r_2)=1, delta=L_1r_2-L_2r_1, choose k so rho=Ndelta-khr_1r_2 and |rho|<=hr_1r_2/2. Exact rho=0 is already owned. The Round-150 target is the absolute value of the full signed contribution of 0<|rho|<=hr_1r_2/D to sum_(d asymp D)mu^2(d)|G_U(d)|^2, bounded by R^2D X^epsilon, with the literal A_d coefficients.

- For L=ts^2, a=(t,d_o), c=t/a, retain exactly the accepted closed formula B_(d,U)(ts^2)=mu(a)mu(c)mu(s)/c times the u|d_o/a and coprime v squarefree sums with kappa_(d,U)(au(csv)^2); B vanishes when (s,d_o)>1.
- Expand the product B_(d,U)(L_1)conj(B_(d,U)(L_2)) through exact divisibility and coprimality masks before calling the coefficient arbitrary, low rank, separable, or of bounded variation.
- Determine the exact d-dependence of both prefix indicators and sampled profiles from the accepted transform. Boundedness alone does not imply variation, and no continuous cutoff may replace the prefix.
- Check the exact identity (NL_1-khr_1)(NL_2+khr_2)=N^2L_1L_2+kh rho, including signs, integrality, support, k=0, and possible zero or exceptional factors.
- A divisor bound for fixed L_i,h,k,rho is incomplete until every shift and all coefficient weights are summed with a full power ledger.
- Separate raw collar tuples, coefficient-weighted absolute mass, and the true signed mass carrying chi_4(L_1L_2r_1r_2).
- Audit D=1 and L_1=L_2=1, where no d-average exists and the centered collar covers the full frequency range, as well as balanced and extreme aspects.
- Retain even squarefree d, odd primes dividing d_o, q_i|N, common factors, imprimitive fractions, small reduced denominators, every clipped prefix, and all M<=R^2.
- Classical fixed-vector large sieve, early Cauchy, an arbitrary-matrix counterexample, a conditional variation diagnostic, and a termwise L-to-powerful-H map are forbidden shortcuts.
- The generic complement, every t>=2 layer, and the independent Round-138 cross owner remain separate unless the same proof explicitly controls them.

## Assigned target

Independently analyze the literal moving-coefficient nonzero collar from the statement only. Prove its R^2D bound, a strict owner-complete range, or the first exact coefficient, counting, D=1, prefix, or all-scale obstruction, while separating raw, absolute-weighted, and signed quantities.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-138 through Round-150 nonblind artifacts`
- `all Round-150 sibling reports`

## Required controls

- `literal_nonzero_collar_expansion`
- `two_row_divisor_incidence_linearization`
- `prefix_profile_d_dependence`
- `k_zero_and_exceptional_factor`
- `full_shift_and_weight_summation`
- `tuple_absolute_signed_separation`
- `mod_four_character_retention`
- `all_M_D_E_Q_L_h_k_rho_power_ledger`
- `D1_L1_full_frequency_test`
- `prime_parity_prefix_imprimitive_controls`
- `exact_and_small_denominator_exclusion`
- `generic_tge2_cross_and_downstream_scope`

## Required deliverables

- A seven-section statement-only analytic report.
- An independent collar theorem, strict range, or rigorous no-go with exact first doubtful step.
- A complete D=1 and all-aspect falsifier ledger.
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
