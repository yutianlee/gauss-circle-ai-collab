# Final-kernel formalization/provenance post-hygiene verification

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Role: post-repair final formalization/provenance/hygiene replay
- Candidate SHA-256:
  `76c1a3adb14fc00063a2fcab06f73458ae8f5c9b0e7d19e41c5d8c78f103b978`
- Kernel SHA-256:
  `7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2`
- Date: 2026-08-29

## 1. Result

**Verdict: PASS. REPAIR required: none.**

The requested coordinated hygiene repair is complete and exact:

1. The malformed `` `tr' `` fragment has been replaced in both files
   by the valid TeX expression \(\mathrm{tr}\).
2. Candidate and kernel now each end in exactly one LF, with no terminal
   blank line.
3. Beginning at `## Candidate statement`, their bodies are raw-identical,
   including the final newline.
4. The kernel header records the refreshed candidate hash exactly once
   and contains no stale candidate hash.
5. Strict UTF-8, control-character, whitespace, Markdown-delimiter,
   TeX-delimiter, brace, tag, reference, and link checks all pass.
6. The only candidate/kernel diff is the intended durable-kernel header.
7. The mathematics, two direct dependencies, open-remainder boundary,
   diagnostic-only wording, owner scope, and all exponent statements are
   unchanged.

The kernel is therefore ready for the conductor's normal graph and
validation-matrix promotion checks at its already reviewed subordinate
scope.

## 2. Exact statement and hypotheses

The replay checks these exact artifacts:

\[
 \operatorname{SHA256}(\text{candidate})=
 \texttt{76c1a3adb14fc00063a2fcab06f73458ae8f5c9b0e7d19e41c5d8c78f103b978},
\]

\[
 \operatorname{SHA256}(\text{kernel})=
 \texttt{7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2}.
\]

The intended header delta consists only of:

- changing the candidate title to the durable-kernel title;
- replacing candidate-status metadata by `Formal candidate SHA-256` and
  durable evidence-status metadata;
- retaining `Numerical theorem evidence: none`.

Everything from `## Candidate statement` through the end of file must
be identical. The kernel must continue to prove only (191.C5)--(191.C11),
leave (191.C12) open with deficit \(Y/(Qm)\), depend exactly on the
accepted Round-189 projective reduction and elementary divisor bound,
and leave every parent and exponent unchanged.

## 3. Proof or derivation

### 3.1 Hash, provenance, and body identity

Read-only SHA-256 computation reproduces both supplied hashes exactly.
The kernel's `Formal candidate SHA-256` field contains

`76c1a3adb14fc00063a2fcab06f73458ae8f5c9b0e7d19e41c5d8c78f103b978`

exactly once. The superseded candidate hash

`263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`

occurs zero times.

A complete candidate-versus-kernel diff contains only the intended
initial header hunk. There is no end-of-file hunk and no mathematical
body hunk. Direct substring comparison beginning at
`## Candidate statement` gives

\[
 \texttt{BODY\_RAW\_EXACT=True},qquad
 \texttt{BODY\_LENGTHS}=21315/21315.
\]

Both final bytes are LF (`0x0A`), and each file has exactly one
consecutive terminal LF. Thus body identity now holds byte-for-byte
modulo the intended header; no whitespace normalization or `TrimEnd`
exception is needed.

### 3.2 Markdown, UTF-8, TeX, tag, and link hygiene

Both files decode under strict UTF-8. For the kernel, the mechanical
audit gives:

- zero forbidden control characters;
- zero Unicode replacement characters;
- zero tabs and zero trailing-whitespace lines;
- 346 opening and 346 closing braces;
- 123 opening and 123 closing inline-math delimiters;
- 53 opening and 53 closing display-math delimiters;
- 53 equation tags and 53 unique equation tags;
- no unresolved `191.C...` tag reference;
- twelve backticks, paired on their respective lines into six valid
  inline-code spans;
- zero fenced-code delimiters, Markdown links, or unsafe URI schemes.

The repaired sentence is now

`write a superscript \({\rm tr}\) for evaluation at`,

which is a properly paired inline-TeX expression and opens no Markdown
code span. The new counts differ from the pre-repair audit exactly as
expected from this one formatting substitution: one malformed backtick
is removed, and one TeX pair plus one brace pair is added.

### 3.3 Mathematics, dependencies, and scope

Raw body identity proves that the kernel has no mathematical change
relative to the refreshed candidate. The only direct dependencies remain

- `M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction`;
- `Divisor-bound-elementary`.

The strict signed-inverse sector, exact terminal projection, isolated
Fejer projection, outer ledger, and exact safe/remainder decomposition
remain the only proved content. The kernel still states that

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon
\]

is open and that the missing pointwise gain is exactly \(Y/(Qm)\). It
continues to leave the rest of the original-\(t=1\) owner, every
\(t\ge2\) incidence, all parents, GAR, M2, endpoint uniformity, M9,
both bridges, the quarter target, and every exponent unchanged.

The header says `Numerical theorem evidence: none`. The finite-control
paragraph still says the checks are diagnostic only and supply no
asymptotic theorem, literal density, lift, divisor ledger, or remainder
cancellation. The bounded-array capacity paragraph remains explicitly
an operator-class insufficiency control, not a literal realizability
claim, lower bound, or disproof of the open remainder estimate.

## 4. First doubtful or unproved step

There is no remaining formalization, provenance, or hygiene defect in
the repaired pair. The first unproved mathematical step remains exactly
the openly stated estimate for \(\Re\mathscr R_{Y,Q}^{\sigma}\), which
requires the \(Y/(Qm)\) gain for the complete transported remainder.
This open seam is outside the promoted strict reduction and is not
obscured by the kernel wording.

## 5. Required control test and outcome

The post-repair controls give:

1. **Supplied hashes:** candidate and kernel hashes match. PASS.
2. **Refreshed provenance:** new candidate hash occurs once; stale hash
   occurs zero times. PASS.
3. **Complete diff:** only the intended header differs. PASS.
4. **Raw body equality:** exact, equal length, no normalization needed.
   PASS.
5. **EOF:** exactly one terminal LF in each file. PASS.
6. **Markdown delimiters:** all backticks pair locally; no fence is
   open. PASS.
7. **UTF-8/control/whitespace:** strict decoding and all character checks
   pass. PASS.
8. **TeX/tags/references:** delimiters and braces balance; all 53 tags
   are unique; no referenced `191.C...` tag is missing. PASS.
9. **Links:** no malformed or unsafe link exists. PASS.
10. **Dependencies/scope/diagnostic wording:** unchanged and properly
    narrow. PASS.

These are formal text/provenance checks only and are not used as new
mathematical theorem evidence.

## 6. Dependencies and exact artifacts used

The replay used only:

1. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md`,
   SHA-256
   `76c1a3adb14fc00063a2fcab06f73458ae8f5c9b0e7d19e41c5d8c78f103b978`.
2. `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`,
   SHA-256
   `7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2`.
3. The immediately preceding final formalization/provenance/hygiene
   review, solely to compare the requested defects and invariant scope.
4. The repository protocol already governing this campaign.

No proof graph, state file, campaign file, strategy, control program,
other report, sibling review, candidate, or kernel was read. No web or
numerical experiment was used.

## 7. Recommended state effect

**PASS the repaired final kernel at SHA-256
`7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2`;
no further repair is requested.** Subject to the conductor's ordinary
graph validation, promote only the subordinate proved-internal reduction
for (191.C5)--(191.C11) as inconclusive evidence for the still-open
small-\(t\) owner.

Do not promote the complete fast packet or any downstream owner,
parent, bridge, theorem, or exponent. The remainder estimate and its
exact \(Y/(Qm)\) deficit remain open.
