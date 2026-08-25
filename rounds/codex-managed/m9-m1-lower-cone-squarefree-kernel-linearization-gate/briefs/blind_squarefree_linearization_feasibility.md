# Task Brief: blind_squarefree_linearization_feasibility

- Campaign: `m9-m1-lower-cone-squarefree-kernel-linearization-gate`
- Research round: `145` (`m9_m1_lower_cone_squarefree_kernel_linearization_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `cc5e1b2597d6d233702d566f49884dc0530d0fa62395ce03684d2f55ae19e756`
- Generated: `2026-08-23T22:11:12.107392+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the unique squarefree-kernel decomposition m=s t^2 convert the Round-144 strict large-displacement cone survivor into a target-safe large-square tail plus a source-legal fixed-centre linear-twist problem that can be proved, or into a strictly smaller owner-complete survivor; if not, what is the first exact coefficient, parity, Diophantine, exceptional-fibre, source-hypothesis, or capacity obstruction?

## Reference formula and distinctions

Let R=X^(1/4), N=floor X, C(m)=sum_(hr=m,r odd,r>4h)chi_4(r), k_m=floor(sqrt(Nm)+1/2), and j_m=k_m^2-Nm. The exact open Round-144 scalar is T_N=sum_M sum_(m in I_M, |j_m|>M^(3/4)) m^(-3/4)V_low(R^2m/N)C(m)e(sqrt(Nm)). Write every m uniquely as m=s t^2 with s squarefree, so e(sqrt(Nm))=e(t sqrt(Ns)). The target is T_N<<_epsilon X^epsilon uniformly for every real X.

- The m=s t^2 decomposition is a bijection, but no cancellation follows until C(s t^2), the odd-r condition, the strict cone, and the large-displacement mask are parameterized exactly.
- A candidate absolute lemma is that the aggregate part t>=M^(1/4) is target-safe, since a fixed t supports O(M/t^2) squarefree kernels on a block and the m^(-3/4) divisor envelope gives a tail of order M^(1/4)sum_(t>=M^(1/4))t^(-2). This must be proved with half-open blocks, profiles, exact radicals, and all endpoints.
- On the remaining t<M^(1/4), one has s comparable to M/t^2 and hence s>M^(1/2) up to block constants. This support fact is not a signed estimate.
- The identity |j_m|=|k_m-t sqrt(Ns)|(k_m+t sqrt(Ns)) translates the Round-144 mask into a nearest-integer condition on t sqrt(Ns). Exact resonance occurs only in the separately owned squarefree kernel of N; quadratic-irrational and Pell-near-resonant fibres remain possible.
- The t=1 layer and every small-t layer must be retained. A bound that gains only from large t, assumes bounded continued-fraction quotients uniformly in Ns, or treats squarefree support as random is invalid.
- The individual complex direction e(+t sqrt(Ns)) must be estimated. A cosine, conjugate-pair, mean-square-in-N, or average-over-s theorem is not a fixed-centre substitute.
- Round 144 already parks Appell completion, rational-mode truncation, derivative-arc inference, and reciprocal stationary self-return. This round must exploit the new squarefree-kernel interface rather than relabel an invertible transform.
- The Round-138 collar-tail cross owner remains independent. No result here alone proves lower GAR, either direct M1 parent, M9-M1, any M2 owner, endpoint uniformity, M9, the bridge, or a global exponent.

## Assigned target

Independently rederive the squarefree-kernel decomposition of the strict cone survivor and decide whether its linearized phase yields a target bound or strict reduction. Retain all parity, cone, mask, exact/near resonance, t=1, endpoint, and capacity owners; otherwise prove the first exact no-go.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-138 through Round-145 nonblind artifacts`
- `all Round-145 sibling reports`

## Required controls

- `unique_squarefree_kernel_decomposition_and_block_endpoints`
- `exact_C_st2_cone_parity_character_parameterization`
- `large_square_part_t_tail_absolute_ledger`
- `small_t_large_s_survivor_and_multiplicity`
- `j_mask_nearest_integer_sign_tie_and_exact_radical`
- `quadratic_irrational_Pell_and_continued_fraction_exceptions`
- `t_equals_one_and_bounded_t_capacity`
- `individual_complex_direction_and_fixed_centre`
- `full_R_M_s_t_power_and_dyadic_assembly`
- `downstream_M1_M2_endpoint_M9_and_exponent_scope`

## Required deliverables

- A seven-section statement-only analytic report.
- A self-contained fibre parameterization, tail estimate, and small-t feasibility analysis.
- A target estimate, strict signed survivor, or first rigorous no-go.
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
