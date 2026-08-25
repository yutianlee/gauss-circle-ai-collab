# Task Brief: blind_full_abel_rederivation

- Campaign: `m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate`
- Research round: `159` (`m9_m1_lower_cone_t1_d1_abel_commutator_recombination_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `8a0f917fb8117e9dbaf287d9f773046ff201729d2d8d8c3df1a51bca7815574b`
- Generated: `2026-08-25T08:58:21.166182+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does exact recombination of the moving trace, both profile-difference remainders, and both outer endpoints restore a single common-profile selected residual-mask sum for the full paired-interior D=d=L=1 matrix, and can that exact combined scalar be proved target-sized or on a strict owner-complete range; if not, what is the first non-telescoping, variable-mask, coefficient, Fourier, truncation, source, or restored-power obstruction?

## Reference formula and distinctions

Retain B_j(x)=1_(x>=1)1_(-x<=j<=x-1)w_U((x^2-j)/N)e(sqrt(x^2-j)-x), every odd d|N, every interior v mod H, both signed j blocks, and all six sign-adapted Abel lines. Recombine before estimation. Complete-frequency inversion gives S_U(V)=sum_(V<|j|<=2V)sum_x B_j(x)G_N(x^2-j). The candidate selected compression is sum_(ell>=1)chi_4(ell)w_U(ell)e(sqrt(N ell))1_(V<|kappa(ell)^2-N ell|<=2V), with kappa(ell)=floor(sqrt(N ell)+1/2). The scalar target is X^epsilon, equivalently raw M^(3/4)X^epsilon.

- Retain the positive right and negative left Abel outer endpoints, both moving atoms, both profile-difference remainders, every component transition, zero extension, half-open choice, and hard dyadic endpoint.
- Prove the finite reconstruction separately on each sign block and for every d and v before complete-frequency inversion.
- Retain arbitrary N, every odd d|N, c=4N/d, H=c/2, both complementary representatives, and c=4.
- Subtract the already closed zero and Nyquist whole rows exactly once; do not transfer their theorems to Abel pieces.
- Audit the physical-lift multiplicity and the nearest-cell partition before replacing x and j by kappa(ell) and r(ell).
- Distinguish the full quotient profile w_U(ell) from both isolated-trace boundary profiles; no isolated-trace statement is retroactively altered.
- Use e(sqrt(N ell)-kappa(ell))=e(sqrt(N ell)) only because kappa(ell) is integral.
- Treat the exact defect mask as the variable band r=-delta(2kappa+delta); no fixed endpoint may replace it without a proved error.
- Treat min(M,V) as support cardinality only and restore the M^(-3/4) atom scale before claiming the scalar target.
- No result transfers to D>1, L>1, generic t=1, t>=2, cross, another M1 or M2 owner, endpoint uniformity, M9, bridge, target, or exponent owners.

## Assigned target

From the literal statement alone, independently reconstruct both Abel blocks, derive the full physical and selected scalar with exact endpoints and normalization, and determine whether the combined object is target-sized, has a strict range, or meets a first rigorous algebraic or analytic obstruction.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-159 nonblind artifacts`
- `all Round-159 sibling reports`
- `the Round-159 conductor seed`

## Required controls

- `literal_full_Abel_six_line_package`
- `positive_negative_signs_and_outer_endpoints`
- `profile_difference_and_transition_reconstruction`
- `all_d_all_v_complete_frequency_normalization`
- `zero_and_Nyquist_whole_row_subtraction`
- `physical_lift_and_nearest_cell_uniqueness`
- `quotient_profile_not_boundary_profile`
- `integral_phase_shift`
- `variable_residual_band`
- `chi4_shifted_zero_mode`
- `Fourier_truncation_and_boundary_errors`
- `N_M_V_power_and_scalar_target`
- `upper_capacity_vs_signed_bound`
- `external_scalar_and_downstream_scope`

## Required deliverables

- A seven-section statement-only analytic report.
- An independent exact reconstruction and target calibration.
- A target theorem, strict range, or first rigorous obstruction.
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
