# Final kernel formalization, provenance, and hygiene review

- Round: 193
- Kernel:
  proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md
- Expected SHA-256:
  4f053d1e0396876877efb1c9631e010f4f17fdd11fba478ca8b5ec95ba5ff5f8
- Observed SHA-256:
  4f053d1e0396876877efb1c9631e010f4f17fdd11fba478ca8b5ec95ba5ff5f8
- Hash check: **PASS**
- Overall verdict: **FAIL**
- Boundary: candidate-to-kernel formalization, metadata, provenance,
  dependency and owner typing, TeX/byte/path hygiene, and exponent
  quarantine.  The incidence proof was not reopened, and claimant agreement
  was not used as proof.

## 1. Candidate-to-kernel consistency

**PASS.**  The kernel metadata records formal-candidate SHA-256
274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd,
which matches the terminally reviewed candidate.  A direct file comparison
has exactly two hunks:

1. the title and metadata replace candidate status with durable-kernel status
   and record the formal-candidate hash; and
2. section 7 changes “Proposed state effect” to “Dependencies and proof-state
   boundary,” makes the effect conditional on the completed review
   lifecycle, and changes “proposed terminal label” to “Round-193 terminal
   label.”

Sections 1--6, including every numbered formula (193.C1)--(193.C31), are
otherwise identical to the terminal candidate.  No mathematical hypothesis,
operator identity, estimate, complement, or scope statement changed during
promotion to the durable artifact.

The title, campaign, round, starting-graph hash, formal-candidate hash, kernel
status, and diagnostic-evidence metadata are correctly typed.  The starting
graph hash also matches the current proof-obligation graph.

## 2. TeX and byte hygiene

**PASS.**  Exact checks give:

- \(40\) display opens and \(40\) display closes;
- \(89\) inline opens and \(89\) inline closes;
- \(40\) equation tags;
- zero unescaped qquad or quad tokens;
- strict valid UTF-8 with no byte-order mark;
- no NUL bytes and no tab bytes;
- LF-only line endings and a final LF; and
- no trailing-whitespace error.

The durable filename is lowercase snake case and is located in the designated
proofs/kernels directory.

## 3. Provenance and dependency typing

The mathematical dependency typing itself is **PASS**.  The kernel separates:

- the Round-192 exact-core node as direct logical graph prerequisite;
- the Round-185 physical coordinate interface as accepted transitive
  provenance reopened by the new argument;
- the Round-187, Round-188, Round-189, Round-191, and Round-192 proofs as
  connector artifacts reopened only for deletion stability; and
- the Round-184 selector truth table and elementary divisor bound as
  subsidiary or inherited provenance.

The two Round-193 claimant reports are correctly separated from the accepted
Round-192 parent kernel.  They are provenance/evidence records only.  This
review does not infer correctness from their agreement.

## 4. Exact path-hygiene failure

**FAIL.**  The two finite-control references in lines 540--541 are written as

- controls/gcd_scaled_orientation_involution_diagnostic.wl
- controls/gcd_scaled_orientation_involution_diagnostic_output.md

Neither path exists relative to the repository root, and neither resolves
relative to the durable kernel directory.  Those abbreviations were
unambiguous only while the candidate lived in the Round-193 campaign
directory; they are not durable artifact paths after the file was copied to
proofs/kernels.

Replace them by the exact repository-relative paths:

- rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/controls/gcd_scaled_orientation_involution_diagnostic.wl
- rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/controls/gcd_scaled_orientation_involution_diagnostic_output.md

Both corrected targets exist.  The two claimant-report paths and the accepted
parent-kernel path already resolve exactly and need no change.

## 5. Owner scope and exponent quarantine

**PASS.**  The kernel supports only one subordinate strict double-close
sector attached as evidence to the open hard-M1 small-\(t\) residual owner.
It does not claim either first-failure complement, the full rho-large core,
complete original \(t=1\), any original \(t\ge2\) range, the near-resonant
complement, the remaining small-\(t\) owner, either M1 parent, GAR, any M2
parent, endpoint uniformity, M9, either bridge, or the Gauss-circle target.

The internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), and target \(1/4\) exponent records remain
unchanged.  The durable-kernel status does not itself assert graph acceptance;
section 7 correctly leaves acceptance to the Round-193 State Patch.

## 6. Decision

**FAIL pending one exact path repair.**  Candidate consistency, title,
metadata, section-7 conversion, dependency typing, owner scope, exponent
quarantine, TeX hygiene, and byte hygiene all pass.  Correct the two
finite-control paths, recompute the kernel SHA-256, and rerun only the
candidate-diff, hash, and path-resolution checks.  No mathematical-body,
dependency, owner, or exponent change is required.
