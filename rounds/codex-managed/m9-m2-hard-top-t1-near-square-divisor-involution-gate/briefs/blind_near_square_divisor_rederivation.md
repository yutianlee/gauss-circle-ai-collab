# Task Brief: blind_near_square_divisor_rederivation

- Campaign: `m9-m2-hard-top-t1-near-square-divisor-involution-gate`
- Research round: `163` (`m9_m2_hard_top_t1_near_square_divisor_involution_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358`
- Generated: `2026-08-25T14:41:57.532348+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the actual squarefree t=1 product coefficient be bounded at target strength before Mobius separation by an exact p congruent 3 modulo 4 prime toggle, multi-prime exchange, complementary-divisor pairing, or signed boundary decomposition; or does the moving near-square window, parity, profile asymmetry, unmatched-set capacity, arbitrary-real centre, or hard-edge leakage repay the full L^(1/2-o(1)) gain?

## Reference formula and distinctions

S_(L,1)=sum_(N asymp L^2) mu^2(N)(L^2/N)^(3/4)e(J sqrt(N)) b_(L,X)(N), where b_(L,X)(N)=sum_(d|N,d odd,sqrt(N)<=d<=2sqrt(N)) chi4(d)eta_L(d)Phi(d/(H+1))W(sqrt(q_X)d/(2sqrt(N))), with the exact half-open shell, cone, even-N branch, profiles, floors, stars, endpoints, and zero extension retained. The target is |S_(L,1)| <<_epsilon L^(3/2)X^epsilon.

- J=sqrt(X), y=floor(J), q_X=X/y^2, H=floor(y X^(-1/4)), and 1<<L<<H<=J^(1/2).
- The product N is squarefree because the t=1 factors d1,d2 are squarefree and coprime. The physical divisor d=d1 is odd; N may be even through d2.
- The upper near-square divisor window has multiplicative width two. A single odd prime p congruent 3 modulo 4 reverses chi4 but has p>=3.
- Complementation sends the upper window to an excluded lower window. For odd N it changes the character by chi4(N). For even N=2M, the physical complement N/d is even while the odd-part character complement M/d=N/(2d) lies in [sqrt(N)/4,sqrt(N)/2].
- A two-prime exchange may have ratio close to one and is not ruled out by the single-toggle control. Its global matching, character sign, profile difference, multiplicity, and unmatched set must be proved.
- The positive physical capacity is L^(2+o(1)); the target requires a signed L^(1/2-o(1)) gain at every allowed endpoint scale.
- No t=1 result transfers automatically to the remaining few-point channels, full hard TOP, smooth M2 packets, M9-M2, M9, the bridge, or a global exponent.

## Assigned target

Starting only from the frozen statement, independently derive the product coefficient and test all prime-toggle, multi-prime, and complementary-divisor involutions. Decide whether a self-contained target theorem, complete sector, or exact leakage obstruction is available, with all profiles, endpoints, and powers restored.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `state/active_campaign.yml`
- `all strategy files`
- `all Round-163 nonblind artifacts`
- `all Round-163 sibling reports`
- `the Round-163 conductor seed`
- `all Round-162, Round-161, and Round-137 reports, candidates, reviews, kernels, and syntheses`

## Required controls

- `literal_squarefree_product_grouping`
- `odd_divisor_and_even_N_branch`
- `full_divisor_vs_truncated_window`
- `single_prime_toggle_domain`
- `two_prime_exchange_matching`
- `complementary_divisor_orientation`
- `character_sign_and_parity`
- `profile_window_and_endpoint_leakage`
- `representable_sector_density_power`
- `arbitrary_real_centre_phase`
- `missing_L_half_power`
- `physical_coefficient_vs_diagnostic`
- `remaining_few_point_and_downstream_scope`

## Required deliverables

- A seven-section statement-only analytic report satisfying the repository report contract.
- An independent exact matching, leakage, parity, profile, and target-power derivation.
- A target theorem, complete nontrivial sector, or first rigorous scoped obstruction.
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
