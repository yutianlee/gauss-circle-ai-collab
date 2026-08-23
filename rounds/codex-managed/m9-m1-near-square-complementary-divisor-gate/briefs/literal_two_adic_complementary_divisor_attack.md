# Task Brief: literal_two_adic_complementary_divisor_attack

- Campaign: `m9-m1-near-square-complementary-divisor-gate`
- Research round: `122` (`m9_m1_near_square_complementary_divisor_gate`)
- Role: `discovery`
- Access mode: `selected_context`
- Graph SHA-256: `3e85caebbaf6c69d0019009bee3ce8f720f34f579bfb0cfa2035b92be0fb2c13`
- Generated: `2026-08-21T18:22:34.735884+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 99%.
- Numerical/experimental effort: at most 1%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

After a target-safe localization of the exact Round-121 discrepancy wavelet, does the near-square complementary-divisor involution give a noninvertible signed gain, a strict target-safe branch, or a rigorous self-return?

## Reference formula and distinctions

B_flat^(N)=sum_(k in Z)D_N(k)W_(R,y)(k), where D_N(k)=sum_(d<=y)chi_4(d)(floor((N+k)/d)-floor(N/d)-k/d), W_(R,y)(k)=hat J(k)-hat J(k+1), J(t)=eta(yt)V_low(4R^2t^2)/t, and the target is B_flat^(N)<<R X^epsilon.

- X large real, R=X^(1/4), y=floor(sqrt X), N=floor X
- all k in Z before a proved target-safe tail deletion
- K_(R,y)(t)=J_(R,y)(t)(1-e(-t)) and its uniform Fourier envelope
- m=N+k positive on the localized window
- m=2^a m_0 with m_0 odd and every a>=0
- fixed cutoff d<=y versus complementary threshold m_0/y
- m_0 mod 4 character sign, square ties, central divisor band, and hard d=y sample
- signed k-wavelet retained across every parity and complement branch
- full r_2/4 coefficient plus exact complementary tail, never one without the other
- all Round-121 normalization, real-X amplitudes, and downstream owner restrictions

## Assigned targe

Derive the literal Fourier localization and all 2-adic complementary-divisor branches, then seek a noninvertible signed inequality on the complete near-square wavelet.

## Permitted contex

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/conductor_0821_full_proof_strategy.md`
- `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/synthesis.md`
- `rounds/codex-managed/m9-m1-product-wavelet-local-discrepancy/synthesis.md`
- `rounds/codex-managed/m9-m1-unmatched-crossing-fourier-modes/synthesis.md`
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md`
- `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/derivation_packet.md`

## Required controls

- `exact_Round121_discrepancy`
- `uniform_wavelet_envelope`
- `far_k_tail_budget`
- `positive_near_square_window`
- `two_adic_divisor_involution`
- `character_residue_branches`
- `square_and_central_boundaries`
- `full_divisor_and_complement_one_count`
- `signed_k_aggregation`
- `circle_problem_noncircularity`
- `old_return_map_nonduplication`
- `false_unsigned_control`
- `one_count_downstream_scope`

## Required deliverables

- A seven-section analytic report.
- Exact Fourier-envelope and 2-adic complement formulas with capacity table.
- A target estimate, strict signed gain, inverse theorem, or smallest exact return.
- A precise state recommendation.

## Report contrac

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
