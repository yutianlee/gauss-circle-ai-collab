# Task Brief: blind_cell_trace_rederivation

- Campaign: `m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate`
- Research round: `158` (`m9_m1_lower_cone_t1_d1_paired_interior_cell_trace_gate`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f`
- Generated: `2026-08-25T07:27:12.325066+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Can the exact moving-mask Abel trace inside the paired interior D=d=L=1 nonzero theta matrix be proved target-sized after sign-adapted prefix or suffix summation, safe zero and Nyquist trace removal, and exact selected-coordinate rewriting; if not, what is the first strict-prefix, arithmetic, sign, coefficient, endpoint, source, or restored-power obstruction?

## Reference formula and distinctions

Fix q=4N, c=q/d, H=c/2, and V<|j|<=2V. With B_j(x)=1_(x>=lambda_sigma(j))F_j(x), lambda_+(j)=j+1, lambda_-(j)=-j, define P^+_(d,v)(j)=sum_(s=a_+)^j K(-v^2,-s;c) and P^-_(d,v)(j)=sum_(s=j)^(b_-) K(-v^2,-s;c). The paired trace is -i(1+i)/(2Nq) sum_(d|N,d odd)chi_4(d)d sqrt(c) times [sum_(j in J_+)F_j(j+1)sum_(v mod H,v!=0,H/2)e_c(-2v(j+1))P^+_(d,v)(j)+sum_(j in J_-)F_j(-j)sum_(v mod H,v!=0,H/2)e_c(2vj)P^-_(d,v)(j)], with exact strict endpoints. Its full-v physical form is sum_j F_j(j+1)sum_(s<=j)G_N((j+1)^2-s)+sum_j F_j(-j)sum_(s>=j)G_N(j^2-s).

- Retain arbitrary N, every odd d|N, c=4N/d, H=c/2, both complementary interior representatives, and the edge case c=4.
- Retain both signed blocks, prefix orientation on the positive side, suffix orientation on the negative side, every Abel outer endpoint, and the exact sign of each moving atom.
- Retain the actual complex residual phase, zero-extended profile, transitions, asymmetric cell, half-open choices, hard endpoints, and external B_(1,U)(1) seam.
- Prove the full-frequency delta-mass inversion and separately bound the v=0 and v=H/2 trace pieces; do not transfer their total-row theorems to an Abel piece.
- Compute complete p-adic root tables for j^2+j+1 and j^2-j, including p=2 and p=3.
- Distinguish the endpoint s=j from every strict prefix s<j or suffix s>j term.
- Rewrite the strict trace in selected coordinates with its literal boundary-frozen coefficient and chi_4 quotient.
- Treat min(M,V) as support cardinality only; a signed square-root theorem remains a separate input.
- Restore every N-M-V-d-c factor before assigning a gain.
- No trace result transfers to the profile bulk, full paired matrix, D>1, L>1, generic t=1, t>=2, cross, M2, endpoint uniformity, M9, bridge, target, or exponent owners.

## Assigned target

Independently derive the moving-cell trace from the literal paired interior matrix. Audit prefix versus suffix signs, outer endpoints, full-frequency inversion, removed-row trace pieces, endpoint polynomials, and any strict selected survivor. Prove the target, a strict range or subrow, or the first exact missing theorem.

## Permitted context

- `protocol.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/blind_statement.md`

## Excluded context

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `all strategy files`
- `all Round-158 nonblind artifacts`
- `all Round-158 sibling reports`

## Required controls

- `literal_paired_interior_trace`
- `positive_prefix_negative_suffix_signs`
- `all_Abel_outer_endpoints`
- `full_frequency_delta_inversion`
- `zero_trace_piece`
- `Nyquist_trace_piece`
- `endpoint_polynomial_p_adic_roots`
- `strict_prefix_suffix_survivor`
- `selected_coordinate_boundary_weight`
- `positive_negative_profiles_and_endpoints`
- `N_M_V_d_c_power_ledger`
- `upper_capacity_vs_signed_sum`
- `profile_bulk_and_downstream_scope`

## Required deliverables

- A seven-section statement-only analytic report.
- An independent exact trace normalization and feasibility derivation.
- A target theorem, strict range or subrow, or first rigorous obstruction.
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
