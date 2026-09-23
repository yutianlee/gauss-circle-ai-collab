# Final kernel formalization and provenance post-repair verification

- Round: 193
- Kernel:
  proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md
- Expected SHA-256:
  470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83
- Observed SHA-256:
  470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83
- Hash check: **PASS**
- Overall verdict: **PASS**
- Boundary: exact post-repair candidate consistency, provenance and dependency
  typing, TeX/byte/path hygiene, owner scope, and exponent quarantine.  The
  incidence proof was not reopened, and claimant consensus was not used as
  proof.

## Candidate consistency and repaired paths

**PASS.**  The kernel records the exact terminal candidate hash
274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd.
Direct comparison with that candidate shows only:

1. the approved title and durable-kernel metadata changes;
2. the approved section-7 proof-state-boundary wording; and
3. the two nonmathematical durable-path expansions required by the preceding
   hygiene review.

Every numbered formula and mathematical sentence remains unchanged.

The repaired control references are now the exact repository-relative paths:

- rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/controls/gcd_scaled_orientation_involution_diagnostic.wl
- rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/controls/gcd_scaled_orientation_involution_diagnostic_output.md

Both paths resolve.  The two Round-193 claimant-report paths and the accepted
Round-192 parent-kernel path also resolve.  No stale campaign-relative or
kernel-relative artifact path remains.

## TeX and byte hygiene

**PASS.**  Exact checks give:

- \(40\) display opens and \(40\) display closes;
- \(89\) inline opens and \(89\) inline closes;
- \(40\) equation tags;
- zero unescaped qquad or quad tokens;
- strict valid UTF-8 with no byte-order mark;
- no NUL bytes, tabs, or carriage returns;
- LF-only line endings and a final LF; and
- no trailing-whitespace error.

The durable filename and proofs/kernels location are correct.

## Provenance and dependency typing

**PASS.**  The kernel keeps the exact Round-192 core as the direct logical
prerequisite, names the Round-185 physical chart as transitive interface
provenance, identifies the accepted Round-187--Round-192 connector proofs as
reopened only for deletion stability, and types the Round-184 selector and
elementary divisor bound as subsidiary or inherited.

The Round-193 claimant reports remain candidate evidence, separate from the
accepted Round-192 parent kernel.  The repaired finite-control paths remain
diagnostic-only.  No report agreement or finite computation is represented
as proof of the asymptotic estimate.

## Owner scope and exponent quarantine

**PASS.**  The durable artifact supports only one subordinate strict
double-close sector under the already-open hard-M1 small-\(t\) residual
owner.  It leaves both first-failure complements, the full rho-large core,
complete original \(t=1\), every original \(t\ge2\) range, the near-resonant
complement, the remaining small-\(t\) owner, both M1 parents, GAR, M2,
endpoint uniformity, M9, both bridges, and the Gauss-circle target open.

The internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), and target \(1/4\) records remain unchanged.
Kernel durability is not conflated with graph acceptance; section 7 leaves
that action to the Round-193 State Patch.

## Decision

**PASS.**  The two durable control paths are repaired, all referenced
artifacts resolve, and no candidate-consistency, provenance, dependency,
TeX, byte, path, owner, downstream, or exponent defect remains at the
verified kernel hash.
