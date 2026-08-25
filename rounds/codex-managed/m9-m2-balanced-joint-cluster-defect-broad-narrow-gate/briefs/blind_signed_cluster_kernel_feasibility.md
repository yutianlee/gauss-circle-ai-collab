# Task Brief: blind_signed_cluster_kernel_feasibility

- Campaign: `m9-m2-balanced-joint-cluster-defect-broad-narrow-gate`
- Research round: `136` (`m9_m2_balanced_joint_cluster_defect_broad_narrow_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `c43058006cec6849cd17a49e6a7a5298f5a3c124b34d2333b3279adcb54da1d1`
- Generated: `2026-08-23T14:28:53.294575+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the complete signed divisor-progressive bulk kernel K_B^bulk be split into a genuinely transverse broad part and arithmetic aligned-ruling narrow parts, with the broad and every narrow contribution together bounded by L^(3+epsilon), while retaining both chi_4 factors, both low-gcd weights, literal slanted profiles, distinct divisor lifts, both far gates, real-centre phases, crossings, and the fixed-block owner; if not, what is the first exact transversality, cluster, arithmetic-sign, or capacity obstruction?

## Reference formula and distinctions

K_B=sum_(h odd,k,k') b_B(h,k) sum_(d|k', d odd) gamma_d sum_J sum_(mu in Z+1/2, mu>0, t_* in J) A_(d,J)(h,k,k';mu)e(Theta_(d,mu)), where lambda=mu/d, x_*=Xk'/lambda^2, Theta=R sqrt(hk)-Xk'/(2lambda)-lambda h/2+s_d(1/2-lambda), and the target is |K_B^bulk|<<_epsilon L^3 X^epsilon for L asymp X^(1/6).

- h'=h+2s=d(ell_d+2t), s=s_d+dt, h+2s_d=d ell_d, d odd, mu=1/2-m, lambda=mu/d
- mu asymp dL^3 with spacing one, lambda spacing 1/d, stationary amplitude O((dL)^(-1)), and O(L^3) outer triples
- rho=hk'-x_*k=[hk'/lambda^2](lambda^2-lambda_0^2) and Delta=x_*k'-hk=[hk/lambda^2](lambda_r^2-lambda^2), with both strict far gates |rho|>L and |Delta|>L retained
- the residue phase s_d(1/2-lambda), divisor coefficient gamma_d, and lift label (d,mu) are literal; equal rational lambda from distinct lifts may not be merged
- all finite-Poisson boundary, transition, support-crossing, nonstationary, and stationary-remainder packages are already target-safe at O_epsilon(L^3X^epsilon); the frozen question concerns only the interior bulk
- the phase-free mode is already target-safe only after full signed assembly
- aliaswise l1, one-frequency reciprocal counting, coefficient-uniform spacing large sieves followed by outer norms, a second one-variable B-process, and positive row energy as an equivalent scalar target are parked controls

## Assigned target

Independently derive whether the stated literal signed cluster kernel admits an L^3 broad--narrow estimate; identify the first unproved determinant, norm, or arithmetic-sign step if not.

## Permitted context

- `problems/gauss_circle.md`
- `state/control_models.md`
- `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-112 through Round-136 nonblind artifacts`
- `all Round-136 sibling reports`

## Required controls

- `literal_bulk_kernel_and_owner_ledger`
- `divisor_progression_and_distinct_lifts`
- `joint_broad_partition_resolution`
- `broad_transversality_determinant`
- `broad_capacity_to_L3`
- `narrow_rational_ruling_classification`
- `actual_chi4_and_residue_phase`
- `coupled_rho_Delta_far_gates`
- `coherent_and_opposite_character_packets`
- `boundary_and_transition_scope`
- `scalar_vs_positive_energy`
- `full_BAL_owner_and_downstream_scope`

## Required deliverables

- A seven-section statement-only report.
- A self-contained derivation with an explicit scale partition and adversarial controls.
- A target estimate, strict smaller survivor, or first exact no-go step.
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
