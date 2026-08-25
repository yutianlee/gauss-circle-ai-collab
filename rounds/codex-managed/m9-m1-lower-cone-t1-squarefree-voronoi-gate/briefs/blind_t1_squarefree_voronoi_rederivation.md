# Task Brief: blind_t1_squarefree_voronoi_rederivation

- Campaign: `m9-m1-lower-cone-t1-squarefree-voronoi-gate`
- Research round: `147` (`m9_m1_lower_cone_t1_squarefree_voronoi_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `1dc79cf41e0dea8888341e944c5d0bf025d87f22cfaa282da34fcd10eecd04f5`
- Generated: `2026-08-24T09:11:11.193216+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the mandatory exact t=1 squarefree-cone prefix be bounded at M^(3/4) by a ratio-Mellin factorization zeta(w+z)L(w-z,chi_4)H(w,z), a level-four complex-order generalized-divisor Voronoi transform, and signed aggregation over the powerful H-convolution; if not, what is the first exact uniform-order, test-function, polar, boundary, self-return, convolution, or all-scale power obstruction?

## Reference formula and distinctions

Let R=X^(1/4), N=floor X, I_M=N intersect [M,B_M), B_M<=2M. The mandatory t=1 face is U_N^(1)=sum_M sum_(s in I_M, mu^2(s)=1) s^(-3/4)V_low(R^2s/N)C(s)e(+sqrt(Ns)), with C(s)=sum_(de=s, e odd, e>4d)chi_4(e). Uniformly for every clipped prefix M<=U<=B_M, it is enough to prove |sum_(M<=s<U, mu^2(s)=1)V_low(R^2s/N)C(s)e(+sqrt(Ns))| <<_(epsilon,V) M^(3/4)X^epsilon. Before imposing the cone, Z(w,z)=sum_(d,e>=1, e odd, mu^2(de)=1) chi_4(e)d^(-w-z)e^(-w+z)=zeta(w+z)L(w-z,chi_4)H(w,z), where H_2=1-2^(-2w-2z) and, for odd p with x=p^(-w-z), y=chi_4(p)p^(-w+z), H_p=(1+x+y)(1-x)(1-y)=1-x^2-y^2-xy+x^2y+xy^2.

- Write s=2^nu n with nu in {0,1} and n odd squarefree. Then C(2^nu n)=sum_(e|n, e>2^(1+nu/2)sqrt(n))chi_4(e). Divisor pairing leaves both a complete positive-character sector and a mandatory antisymmetric negative-character tail; neither may be discarded.
- The exact Euler correction H is absolutely convergent when Re(w+z)>1/2 and Re(w-z)>1/2. Its coefficients h_z(k) are supported on powerful integers, but this half-plane convergence is not an unweighted physical l1 bound.
- A hard ratio Perron cutoff must distinguish e=4d+1 and requires height comparable to D. A target-safe collar |e-4d|<=sqrt(D) costs O(X^epsilon) after the physical weight and permits a smooth ratio bandwidth |Im z|<=D^(1/2)X^epsilon, uniformly for clipped radial prefixes.
- For a level-q kernel with Bessel phase e(plus or minus 2sqrt(mx/q)), the conductor-four resonance against e(+sqrt(Nx)) is m=N. After the H convolution the k-family resonates at m=kN+O(k sqrt(N/M)); freeze conductor and cusp normalization before using either centre.
- For the bare complete zeta-L factor, the favorable normalized transfer price is R/sqrt(M), while the trivial t=1 price is M^(1/4). Their minimum peaks at M=R^(4/3) with R^(1/3), so a top-block formula alone cannot improve the all-scale barrier.
- On M comparable to R^2 the complete-factor transform is only target-borderline. Termwise modulus over powerful k loses a positive power; the required new input is joint signed aggregation across moving resonant bands, not absolute convergence of H or a triangle inequality.
- The five-variable gamma-d-a-b-e expansion has scaled Hessian determinant 3/4 but is an exact multiplicity-one over-resolution of the original h-r wave. It creates no new owner and is parked for this round.
- Round 141 already established target-safe cone smoothing, the sharp-versus-smooth ratio bandwidth distinction, and complete-coefficient transform self-return. This round must address the exact squarefree H correction and its signed resonant aggregation rather than repackage the bare zeta-L model.
- Retain squarefreeness, coprimality, parity, chi_4, strict cone or proved collar replacement, profile, half-open prefixes, fixed N=floor X, individual positive direction, exact radicals, D=1, prime and even controls, polar terms, and all Bessel branches.
- The independent Round-138 collar-tail cross owner and every t>=2 layer remain outside this face. No result here alone proves lower GAR, either direct M1 parent, M9-M1, any M2 owner, endpoint uniformity, M9, the bridge, the quarter target, or a better global exponent.

## Assigned target

Independently reconstruct the exact t=1 squarefree-cone coefficient, its Euler factorization and cone-Mellin interface, and determine whether a complex-order generalized-divisor transform with the full powerful Euler correction can meet the uniform prefix target. Give a target proof, strict owner-complete reduction, or exact no-go, with every short face and all-scale power checked.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-138 through Round-147 nonblind artifacts`
- `all Round-147 sibling reports`

## Required controls

- `t1_exact_extraction_and_prefix_target`
- `squarefree_coprime_even_odd_character_and_cone`
- `divisor_pairing_chi4_sector_ledger`
- `ratio_Mellin_Euler_product_p2_and_H`
- `target_safe_cone_collar_and_ratio_bandwidth`
- `level_four_generalized_divisor_Voronoi_kernel`
- `uniform_complex_order_and_Bessel_asymptotics`
- `H_powerful_coefficients_tail_and_signed_aggregation`
- `dual_resonance_centre_width_amplitude_and_off_resonance`
- `all_M_D_E_capacity_and_R4over3_barrier`
- `clipped_prefix_profile_terminal_endpoint`
- `t1_D1_prime_even_and_slow_family_controls`
- `individual_positive_direction_and_fixed_centre`
- `Round138_cross_and_downstream_scope`

## Required deliverables

- A seven-section statement-only analytic report.
- A self-contained coefficient, Euler-product, cone-bandwidth, transform-resonance, and all-scale power derivation.
- A target estimate, strict owner-complete survivor, or first exact no-go.
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
