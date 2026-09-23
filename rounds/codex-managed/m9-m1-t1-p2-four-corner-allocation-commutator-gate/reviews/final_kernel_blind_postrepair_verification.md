# Round 197 final durable-kernel provenance post-repair verification

## 1. Result

**Verdict: GREEN.**

The provenance-repaired durable kernel has the requested SHA-256

\[
\texttt{6CAF8DC3A027A4548C7059546F117868B45CE51C23F05A5148B78AA995415467}.
\]

Its mathematical body remains identical to the final candidate at

\[
\texttt{285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0}
\]

and therefore remains covered by the prior GREEN candidate-to-kernel
review.  The repairs are provenance-only: they add the exact candidate
path and hash, replace candidate-specific nouns by kernel-specific nouns,
expand campaign-relative evidence paths to unambiguous full
workspace-relative paths, list all diagnostic-control paths, and rename
the last section as a proof-state boundary.  No definition, equation,
hypothesis, estimate, proof step, no-go, complement, or mathematical
scope changed.

## 2. Exact statement and provenance verified

The repaired header now records the exact source candidate as

\[
\begin{gathered}
\texttt{rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/}\\
\texttt{candidates/formalized\_hard\_m1\_t1\_p2\_common\_cell\_allocation\_commutator\_sector.md}
\end{gathered}
\]

and records its correct SHA-256
\(\texttt{285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0}\).
The referenced file exists and its freshly computed hash matches.

The kernel retains verbatim the final candidate's:

1. parameter range and constants;
2. exact selector \(K_{\rm sel},p_N,q_N,\rho_N\);
3. total zero-extended coefficient \(\lambda_{N,\sigma}\);
4. physical source, gcd normalization, and \(P_2,P_0,P_{\rm cc}\);
5. arithmetic/live/dead sharp code;
6. fixed-packet, Farey, outer, cap, and open operator definitions;
7. two \(O(L^2X^\varepsilon)\) strict-sector estimates;
8. exact complement and sharp-face no-go; and
9. complete scope exclusions and proof-state restrictions.

The final section's new title, “Dependencies and proof-state boundary,”
accurately describes its unchanged state proposal and does not alter its
mathematical effect.

## 3. Proof or derivation

### 3.1 Direct body identity

Extracting each file from the line

\[
\texttt{\#\# 1. Statement}
\]

through the line immediately before

\[
\texttt{\#\# 6. Dependencies and scope}
\]

gives the same SHA-256 for kernel and candidate:

\[
\boxed{\texttt{14028E00E7E0350BB19241A7D903D148D4BEDE53B4E0080414AA2D7021DBE08D}.}
\]

Thus Sections 1--5, including every numbered formula
(197.C1)--(197.C37), are byte-identical.  This is stronger than a
semantic spot check: the complete theorem statement, orbit algebra,
coefficient ledger, operator passage, complement, false controls, and
no-go are unchanged.

### 3.2 Provenance diff

A full line-level comparison against the final candidate has changes
only in the following locations:

1. the title and status metadata;
2. the new exact-candidate path and hash in the header;
3. “prerequisites of this candidate” changed to “prerequisites of this
   kernel”;
4. the four claimant/reconciliation evidence paths expanded from
   campaign-relative to full workspace-relative paths;
5. the three bounded finite-orbit control paths added explicitly, with
   their \(\texttt{diagnostic\_only}\) status retained;
6. “This candidate proves only” changed to “This kernel proves only”;
   and
7. the Section 7 heading changed from “Proposed state effect” to
   “Dependencies and proof-state boundary.”

The body of the dependency list and every item under the final
proof-state boundary remain unchanged.

### 3.3 Header and full-path validation

Every newly explicit workspace-relative path resolves to an existing
file:

1. the exact final candidate;
2. the literal, hostile, blind, and reconciliation reports/review;
3. the finite-orbit diagnostic program, output, and report; and
4. all four accepted prerequisite kernels named in Section 6.

The claimant and reconciliation paths all lie under the same Round-197
campaign directory stated in the header.  The control files all lie
under that campaign's controls directory.  The prerequisite paths all
lie under proofs/kernels.  No path points to a legacy A1--A4 artifact,
an unrelated campaign, or a shared-state file.

The three finite-orbit controls are still expressly labeled
\(\texttt{diagnostic\_only}\) and “not theorem evidence.”  Making their
paths explicit does not promote computation into proof evidence.

### 3.4 Algebra, sharp code, selector, and complement

Because the mathematical body is identical, the earlier GREEN checks
remain valid without qualification:

\[
 (gm,g\beta)=g(m,\beta)=g
\]

on \(P_0\), the character reverses by
\(\chi_4(\alpha m)=-1\), and the actual lower orbit is the endpoint
difference (197.C17).

The sharp code still uses the exact arithmetic gate, literal gate, and
dead value \(\dagger\); code equality is symmetric under input exchange.
The selector still has the exact \((1,0,0,1)\) formula, and the actual
coefficient still has the exact smooth/BV/selector decomposition
(197.C22d).  The finite-\(g\), BV, logarithmic-gap, and bounded-shell
arguments are unchanged.

The Boolean partition remains

\[
 P_2=P_{\rm cc}\ \dot\cup\ P_{\partial\mathrm{lit}}
       \ \dot\cup\ P_{s\mathrm f}\ \dot\cup\ P_{g\mathrm f},
\]

with no target claim on the last three terms.  The aligned sharp-face
identity and the whole-sector capacity no-go remain verbatim.

### 3.5 Scope and graph safety

The kernel still proves only \(P_{\rm cc}\) and its exact open-packet
intersection.  It still excludes the full lower-swap sector, full
\(P_2\), \(P_1\), the full four-corner rectangle, all parents,
endpoint uniformity, M9, bridges, the target, and exponent changes.

The proof-state boundary still leaves all accepted Round-184/185/193/195
nodes unchanged and records the refined remainder only in the new
subordinate node and open owner's next action.  Hence the provenance
repairs create no reverse dependency or graph cycle.

## 4. First doubtful or unproved step

No new doubtful mathematical or provenance step was introduced.  The
new full paths were checked for existence, the header candidate hash was
recomputed, and the complete Sections 1--5 body hash matches the final
candidate.

As before, this review does not re-prove the four accepted prerequisite
kernels or reinterpret the diagnostic controls as theorem evidence.
Those are explicit dependency boundaries, not inconsistencies in the
durable artifact.

## 5. Required control test and outcome

1. **Kernel hash — PASS.**  The current file hashes to
   \(\texttt{6CAF8DC3A027A4548C7059546F117868B45CE51C23F05A5148B78AA995415467}\).
2. **Candidate hash — PASS.**  The header hash equals the freshly
   computed final-candidate hash.
3. **Mathematical-body hash — PASS.**  Sections 1--5 have identical
   SHA-256 values in kernel and candidate.
4. **Full textual diff — PASS.**  Every difference is header,
   provenance, artifact-role wording, or section-title wording.
5. **Evidence-path existence — PASS.**  All four claimant/reconciliation
   paths resolve.
6. **Control-path existence — PASS.**  Program, output, and report all
   resolve and remain diagnostic-only.
7. **Prerequisite-path existence — PASS.**  All four accepted kernel
   paths resolve.
8. **Algebra and coefficient correspondence — PASS.**  Every numbered
   formula is unchanged.
9. **Complement and no-go correspondence — PASS.**  The exact partition
   and sharp-face obstruction are unchanged.
10. **Scope and graph-cycle control — PASS.**  No prerequisite, parent,
    bridge, theorem, or exponent is altered.

## 6. Dependencies and exact artifacts used

This verification used:

1. protocol.md as the governing proof-state protocol;
2. proofs/kernels/m9_m1_hard_top_t1_p2_common_cell_allocation_commutator_sector.md at SHA-256
   6CAF8DC3A027A4548C7059546F117868B45CE51C23F05A5148B78AA995415467;
3. rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md at SHA-256
   285EA0975EB3D48691FFB27B5A83E251D33A68062EB4D14DD54972F6AF6296C0;
4. rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/final_kernel_blind_candidate_consistency_review.md as the prior GREEN comparison in this reviewer's active context; and
5. read-only existence checks for the full evidence, control, and
   prerequisite paths printed in the repaired kernel.

No evidence report, control output, prerequisite kernel, graph file, or
shared-state file was opened.  Their paths were checked only for
existence.  The durable kernel and shared state were not edited.

## 7. Recommended state effect

**GREEN for the provenance-repaired durable kernel.**  The prior
candidate-to-kernel GREEN verdict remains valid at the new kernel hash.
The corrected header and full paths improve auditability without changing
the proved statement or its dependencies.

Subject to the remaining required reviews and a mechanically valid State
Patch, this file may serve as the durable proof artifact for the same
subordinate \(P_{\rm cc}\) node.  Do not promote the complement, alter a
prerequisite, close a parent, or change any bridge, endpoint theorem,
global theorem, or exponent.
