# Final-kernel formalization, provenance, and hygiene review

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Role: final kernel formalization/provenance/hygiene reviewer
- Kernel:
  `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`
- Verified kernel SHA-256:
  `18b169b96ce9521ad91be748c3562e8974f4f5fcb3d067f76102ae6f54b4df05`
- Candidate:
  `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md`
- Verified candidate SHA-256:
  `263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`
- Date: 2026-08-29

## 1. Result

**Verdict: REPAIR, formatting/provenance hygiene only. Mathematical,
dependency, and owner-scope review: PASS.**

The kernel faithfully carries the repaired candidate's mathematics and
does not strengthen its theorem. Its header records the exact current
candidate hash, the starting graph hash is unchanged, the two direct
dependencies are exact, the large fast remainder remains open, every
parent and exponent remains unchanged, and all finite computation is
described as diagnostic only.

Two strictly textual defects prevent a final formalization PASS:

1. The candidate at line 375 and the kernel at line 379 both contain
   the malformed Markdown fragment `` `tr' `` in the sentence
   “write a superscript … for evaluation at”. It opens an inline-code
   span with a backtick and attempts to close it with an apostrophe.
   The next backtick is hundreds of lines later, so a Markdown renderer
   may treat a large part of the kernel as one code span. Replace it in
   both artifacts by `` `tr` `` (or by one identical TeX spelling in
   both).
2. After the last non-newline byte, the candidate has one terminal LF
   while the kernel has three. Thus the mathematical body is identical
   after trimming terminal whitespace, but it is not byte-identical
   modulo the header. Remove the two surplus kernel terminal blank
   lines.

Because the first repair changes the candidate body, the candidate hash
must be recomputed and the kernel's `Formal candidate SHA-256` metadata
must be updated to that new value. The repaired kernel will also have a
new hash and needs a final hash/body/hygiene replay. No equation, proof,
dependency, scope sentence, or state claim needs alteration.

## 2. Exact statement and hypotheses

This review tests the final kernel only against the following permitted
sources and invariants:

1. The mathematical body must reproduce the candidate body exactly,
   modulo the durable-kernel header.
2. The kernel header must identify candidate SHA-256
   `263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`
   and preserve starting graph SHA-256
   `306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa`.
3. The only direct dependencies must be
   `M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction` and
   `Divisor-bound-elementary`.
4. The proved scope is confined to (191.C5)--(191.C11): the strict
   signed-inverse sector, exact terminal and Fejer projections, their
   outer ledger, and the exact safe/remainder decomposition.
5. The required bound (191.C12) for the transported remainder must stay
   open with the exact \(Y/(Qm)\) deficit.
6. No original \(t\ge2\) incidence, remaining original-\(t=1\) packet,
   parent, M9 component, bridge, quarter theorem, or exponent may be
   promoted.
7. Finite controls and bounded-array constructions may be cited only as
   diagnostic or operator-class evidence, never as an asymptotic
   theorem or literal lower bound.
8. The Markdown/UTF-8/TeX body must be mechanically well formed and
   free of hidden control characters, broken delimiters, duplicate
   equation tags, malformed links, and unmatched inline-code marks.

The kernel satisfies items 2--7. Item 1 fails only by two terminal blank
lines, and item 8 fails only by the shared malformed inline-code mark.

## 3. Proof or derivation

### 3.1 File identity and header provenance

Read-only SHA-256 computation gives exactly

\[
 \operatorname{SHA256}(\text{kernel})=
 \texttt{18b169b96ce9521ad91be748c3562e8974f4f5fcb3d067f76102ae6f54b4df05},
\]

\[
 \operatorname{SHA256}(\text{candidate})=
 \texttt{263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925}.
\]

The kernel header contains the latter hash exactly once under
`Formal candidate SHA-256`. It also repeats the candidate's starting
graph hash exactly. Its durable evidence-status text adds provenance but
does not assert numerical theorem evidence; the next metadata line is
`Numerical theorem evidence: none`.

The complete textual diff has only two regions:

- the initial title/status metadata are replaced by the durable-kernel
  title, formal-candidate hash, and evidence-status lines;
- two blank lines are added after the final period at end of file.

There is no mathematical-body edit. Taking the substring beginning at
`## Candidate statement`, normalizing line endings, and applying
`TrimEnd()` gives identical bodies with common SHA-256

`b3d077ed9e398ab9d5a81959fa46eac39bcd2b7e5e43d08c7841d90bc83b482b`.

Without trimming the end, the body hashes differ. Byte inspection finds
one terminal LF in the candidate and three in the kernel. Therefore
body identity holds semantically and after canonical terminal-whitespace
normalization, but not strictly byte-for-byte modulo the header.

### 3.2 Dependency and theorem-scope identity

The kernel's `Direct dependencies` section contains exactly

- `M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction`;
- `Divisor-bound-elementary`.

This is identical to the candidate and to the dependency scope approved
by the blind-post-unmask PASS. No additional source, theorem, or
unreviewed bridge is imported.

The accepted content remains narrow:

- (191.C8) bounds only the strict small-signed-inverse fixed sector;
- (191.C9) adds only the exact outer-terminal and isolated Fejer
  projections;
- (191.C10) applies the already displayed lift, coefficient mass,
  dyadic-band loss, divisor ledger, and shell connectors to that safe
  packet;
- (191.C11) is an exact complex decomposition into safe packet and
  remainder;
- (191.C12), the estimate of the remainder, is explicitly labeled
  open.

The method-boundary section retains the pointwise scale
\(Y\kappa uX^\varepsilon\), target scale
\(Qm\kappa uX^\varepsilon\), and exact deficit \(Y/(Qm)\). The closing
scope paragraph explicitly leaves the rest of the original-\(t=1\)
owner, every \(t\ge2\) incidence, hard and smooth M1 parents, GAR, all
M2 parents, endpoint uniformity, M9, both bridges, and the quarter
target open or conditional. It also says the internal exponent \(1/3\),
accepted benchmark, and target \(1/4\) are unchanged. There is no hidden
full-fast or exponent claim.

### 3.3 Diagnostic-only and adversarial scope

The kernel says `Numerical theorem evidence: none`. Its finite-control
paragraph calls the controls `diagnostic only` and expressly says they
supply no asymptotic theorem, literal density, lift, divisor ledger, or
remainder cancellation.

Likewise, (191.C38) is introduced as capacity for bounded
zero-extended height arrays. The following sentence says it is an
operator-class insufficiency control, not a realizability claim, not a
lower bound for the fixed literal coefficient, and not a disproof of
(191.C12). This wording is exact and prevents the false adversarial or
unsigned strengthening.

### 3.4 UTF-8, control-character, TeX, tag, and link audit

Strict UTF-8 decoding passes for both files. The kernel has no BOM, no
Unicode replacement character, no disallowed C0/C1 control character,
no tab, and no line ending in spaces or tabs.

The TeX audit gives:

- 345 opening and 345 closing braces;
- 122 opening and 122 closing inline-math delimiters;
- 53 opening and 53 closing display-math delimiters;
- 53 equation tags, all unique;
- no unresolved reference to a `191.C...` tag.

Heading levels are coherent. There are no fenced-code blocks, Markdown
links, HTTP URLs, or unsafe URI schemes, so link hygiene passes.

The one failing Markdown check is the backtick count. There are thirteen
single backticks. Every intended inline-code span is paired except

`write a superscript `tr' for evaluation at`

at candidate line 375/kernel line 379, where the closing character is
an apostrophe. This is a real rendering defect, not merely a stylistic
preference.

## 4. First doubtful or unproved step

There is no newly doubtful mathematical step in the kernel. The first
unproved theorem remains exactly (191.C12), the signed estimate for the
complete transported remainder with required gain \(Y/(Qm)\). The
kernel states that gap rather than concealing it.

The first formalization defect is earlier and purely textual: the
unmatched backtick at kernel line 379. The first strict provenance-copy
defect is the pair of surplus terminal blank lines. These defects do not
change mathematical meaning, but they fail the requested final hygiene
and raw body-identity gates.

## 5. Required control test and outcome

The following read-only controls were run on the two authorized files.

1. **Hash control:** kernel and candidate hashes equal the two hashes in
   the review brief. Outcome: PASS.
2. **Diff control:** apart from the initial durable header, only two
   terminal blank lines differ. Outcome: mathematical body PASS;
   byte-exact body REPAIR.
3. **Normalized-body hash control:** after LF normalization and terminal
   trimming, both bodies hash to
   `b3d077ed9e398ab9d5a81959fa46eac39bcd2b7e5e43d08c7841d90bc83b482b`.
   Outcome: PASS.
4. **Provenance control:** the exact current candidate hash occurs once
   in the kernel header. Outcome: PASS.
5. **Dependency/scope control:** exactly two dependencies occur; (191.C12)
   remains open; all downstream owners and exponents remain unchanged.
   Outcome: PASS.
6. **UTF-8/control/TeX/tag/link control:** strict UTF-8, control
   characters, whitespace, braces, math delimiters, tags, references,
   headings, and links all pass. Inline-code delimiter pairing fails at
   the single `` `tr' `` fragment. Outcome: REPAIR.
7. **Diagnostic wording control:** `Numerical theorem evidence: none`,
   `diagnostic only`, and the non-realizability/non-lower-bound caveats
   are all present. Outcome: PASS.

No computation was used as theorem evidence; these are formal text and
provenance controls only.

## 6. Dependencies and exact artifacts used

Only the four artifacts authorized by the final-review brief were read:

1. `protocol.md`.
2. `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`,
   SHA-256
   `18b169b96ce9521ad91be748c3562e8974f4f5fcb3d067f76102ae6f54b4df05`.
3. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md`,
   SHA-256
   `263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`.
4. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/reviews/blind_post_unmask_signed_inverse_sector_postrepair_verification.md`.

No proof graph, state file, campaign file, strategy, control note or
program, sibling review, other candidate, or earlier kernel was read.
No web access or numerical experiment was used.

## 7. Recommended state effect

**REPAIR before final kernel promotion; do not edit state yet.** Make
only this coordinated textual repair:

1. In both candidate and kernel, replace `` `tr' `` by `` `tr` `` (or
   the same valid TeX spelling in both files).
2. Remove the two surplus terminal blank lines from the kernel so its
   post-header body has the candidate's single terminal LF.
3. Recompute the candidate SHA-256, update the kernel's formal-candidate
   provenance hash, and recompute the kernel SHA-256.
4. Replay the hash, raw body-identity, backtick, and UTF-8/TeX/tag/link
   checks on the new hashes.

No mathematical rederivation is requested unless the repair changes
anything beyond those characters. After a green replay, the kernel's
narrow proposed state effect is supported: promote only the subordinate
proved-internal reduction for (191.C5)--(191.C11) as inconclusive
evidence for the still-open owner. Keep the complete fast remainder,
all parents and bridges, the quarter theorem, and every exponent
unchanged.
