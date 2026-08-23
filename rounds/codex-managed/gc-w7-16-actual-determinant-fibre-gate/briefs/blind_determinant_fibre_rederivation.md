# Task Brief: blind_determinant_fibre_rederivation

- Campaign: `gc-w7-16-actual-determinant-fibre-gate`
- Research round: `117` (`gc_w7_16_actual_determinant_fibre_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `a27a89fd4e688cae719a28fec8f48dd74190bafb64d0345c590f1caadc2805d9`
- Generated: `2026-08-21T15:13:57.801175+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 98%.
- Numerical/experimental effort: at most 2%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the literal one-sided reduced-determinant correlation at W=Y^(7/16) exploit its M1 denominator or M2 numerator character high-pass, centre phase, and lift transforms to prove O(Y^(1/2+epsilon)), a target-safe strict block subrange, or a quantified saving; or does the exact determinant-fibre transform self-return with its smallest signed survivor named?

## Reference formula and distinctions

O_i=2 Re sum_{0<n=ab'-a'b<kappa_i bb'/W} A_i(a,b) conjugate(A_i(a',b')) e(cn/(kappa_i bb')) (1-Wn/(kappa_i bb')), with kappa_1=1, kappa_2=4, W=Y^(7/16), c asymp Y, and A_i the complete literal reduced-ray coefficient. In increments p=a'-a, q=b'-b, n=aq-bp. M1 has b,b' odd, q=2r and chi_4(b)chi_4(b')=(-1)^r; M2 has a,a' odd, p=2s and chi_4(a)chi_4(a')=(-1)^s.

- Y large real, c in a fixed comparable interval, W=Y^(7/16)
- one fixed moving-symbol stratum and one hard block D=Y^delta, L=Y^ell in H_95
- 1/4<=delta<=1/2, 0<=ell<=delta-1/4, and 3delta-ell>15/16
- literal frequencies a/(kappa_i b), both signs, kappa_1=1 and kappa_2=4
- complete lift coefficients A_1=(constant chi_4(b)/a) sum_g chi_4(g)U_1(g)/g and A_2=(constant chi_4(|a|)/|a|) sum_g chi_4(g)U_2(g)/g
- equal-lift diagonal already O_epsilon(D/L Y^epsilon)
- capacity_before (D/L)(1+min(DL,D^2/W)); minimax Y^(43/48+epsilon)
- target Y^(1/2+epsilon); minimax coefficient-blind deficit Y^(19/48)
- full target implies internal exponent 5/16=0.3125 after accepted assembly, but not M9 or the quarter theorem
- no determinantwise, character-sector, liftwise, raywise, or blockwise absolute value may hide the required signed cancellation

## Assigned target

Independently rederive the literal determinant-increment and character-high-pass chart from the supplied fixed-block statement, price both strip orientations and capacities, and either state a lawful signed target or prove the first exact obstruction.

## Permitted context

- `problems/gauss_circle.md`
- `state/control_models.md`
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-94 and Round-95 reports and reviews`
- `the Round-117 derivation packet and conductor candidate`
- `all Round-117 sibling reports`

## Required controls

- `literal_reduced_ray_and_equal_lift_diagonal`
- `m1_m2_character_placement_and_factor_four`
- `increment_determinant_and_one_sided_orientation`
- `character_high_pass_progressions`
- `determinant_strip_widths_and_boundary`
- `centre_phase_and_stationary_or_geometric_norm`
- `gcd_congruence_and_multiplicity`
- `capacity_before_after_each_norm`
- `actual_symbol_vs_phase_conjugated_coefficients`
- `real_Y_and_endpoint_uniformity`
- `linear_cluster_vs_local_mass_vs_pointwise_exponent`
- `downstream_scope`

## Required deliverables

- A seven-section statement-only report.
- The exact increment, parity-character, phase, and strip charts.
- A candidate signed inequality with every norm and capacity charged, or a precisely scoped no-go.
- A promote, retain, revise, reject, or no-change recommendation.

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
