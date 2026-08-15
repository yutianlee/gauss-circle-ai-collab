# Task Brief: isolated_nonsaddle_rederivation

- Campaign: `m9-m1-beta-large-alpha-complement-completion`
- Research round: `46` (`beta_large_alpha_complement_completion`)
- Role: `blind_rederiver`
- Access mode: `statement_only`
- Graph SHA-256: `295fbe40d51001a263c0740930b476599f04c35afbc7ca159fb9fa819d204739`
- Generated: `2026-08-13T12:14:46.620711+00:00`
- Status: candidate evidence only; do not edit shared proof state.

## Research allocation and tools

- Analytical/algebraic effort: at least 100%.
- Numerical/experimental effort: at most 0%.
- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.
- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.
- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.

## Frozen question

Does the exact direct positive-line complement admit a finite one-count saddle/nonsaddle partition whose nonsaddle cells are target-safe?

## Reference formula and distinctions

Use the Round-46 derivation packet. The compact terminal and artificial residue are closed; estimate only the same-antecedent 1-chi_0 complement.

- same-antecedent alpha partition
- signed saddle and entry/exit cells
- inner and outer nonsaddle sectors
- singular signed Cauchy section
- smooth top and interior profiles
- moving traces and cutoff collars
- coefficient and radial sums
- external normalization once

## Assigned target

Independently prove or refute the Round-46 packet theorem, including partition exactness and nonsaddle integration by parts, without reading the graph or other reports.

## Permitted context

- `rounds/codex-managed/m9-m1-beta-large-alpha-complement-completion/derivation_packet.md`

## Excluded context

- `proof graph`
- `proof draft`
- `prior reports and syntheses`
- `other Round-46 reports`

## Required controls

- `same_positive_line_antecedent`
- `finite_partition_exactness`
- `round41_literal_cell_match`
- `inner_nonsaddle_sector`
- `outer_nonsaddle_sector`
- `signed_cauchy_before_absolute`
- `moving_trace_and_cutoff_derivatives`
- `coefficient_scale_radial_sum`
- `collision_and_external_once`

## Required deliverables

- seven-section statement-only report
- independent proof or counterexample
- first doubtful step and state recommendation

## Report contract

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.
