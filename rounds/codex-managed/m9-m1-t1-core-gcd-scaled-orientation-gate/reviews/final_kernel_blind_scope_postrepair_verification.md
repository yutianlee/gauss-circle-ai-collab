# Final kernel blind/scope post-repair verification

## Verdict: PASS

The repaired durable kernel preserves the previously verified mathematics,
blind finite seam, operator convention, complement, proof-state scope, and
exponent quarantine.

- Kernel:
  `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`
- Repaired kernel SHA-256:
  `470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`
- Final candidate SHA-256:
  `274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd`
- Starting graph SHA-256 recorded by both artifacts:
  `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`

The repaired kernel hash was independently recomputed and exactly matches
the supplied hash.

## Exact repair check

Relative to the final candidate, the only new Section-1--6 difference is
the declared provenance repair:

1. `controls/gcd_scaled_orientation_involution_diagnostic.wl` becomes
   `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/controls/gcd_scaled_orientation_involution_diagnostic.wl`;
2. `controls/gcd_scaled_orientation_involution_diagnostic_output.md`
   becomes
   `rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/controls/gcd_scaled_orientation_involution_diagnostic_output.md`.

The accompanying grammar changes only from “and its [second path] are” to
“and its output [second path] are.”  Both controls remain explicitly
`diagnostic only` and are still excluded from theorem evidence.

After normalizing precisely that two-path block back to the candidate's
relative spelling, Sections 1 through 6 are byte-identical to the final
candidate.  The remaining full-file differences are exactly the already
approved durable title/metadata and Section-7 wording.

## Blind and mathematical consistency

No finite identity changed.  The tuple order, gcd/parity/involution
identities, character-sign condition, plus-to-minus primitive map, close
floors and small-\(U\) handling, determinant restriction, and the
distinction between the no-\(k\)/no-\(r\) absolute count and the narrower
signed involution are unchanged.

No analytic statement changed.  The physical mask is still applied before
the linear Fourier/Abel operators, the exact mask commutator is retained,
and the first-failure masks remain a disjoint complement.  Only the
double-close term is target-safe.

The kernel still proves no complete rho-large estimate, complete \(t=1\),
\(t\ge2\) range, M1 or M2 parent, GAR, endpoint theorem, M9 statement,
bridge, or Gauss-circle theorem.  Internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), and target \(1/4\) remain unchanged.  The
repair introduces no new mathematical claim or dependency.

## Qualified provenance

The blind evidence remains qualified rather than pristine.  The blind
reviewer had high-level Round-192 proof-status context before Round 193,
but no Round-193 claimant material before completing the statement-only
derivation.  Candidate and kernel review occurred only after unmasking.
Expanding the two diagnostic paths does not alter that disclosure or the
independence boundary.

## Recommendation

**PASS** the repaired final-kernel blind/scope consistency seam at exact
SHA-256
`470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`.
Any State Patch must retain the subordinate strict-sector scope and leave
all parents, bridges, theorem nodes, and exponent records unchanged.
