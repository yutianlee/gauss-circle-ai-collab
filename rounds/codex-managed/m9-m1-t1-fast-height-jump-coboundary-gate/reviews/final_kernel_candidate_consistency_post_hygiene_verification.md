# Final kernel/candidate consistency post-hygiene verification

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Round: 191
- Candidate SHA-256:
  `76c1a3adb14fc00063a2fcab06f73458ae8f5c9b0e7d19e41c5d8c78f103b978`
- Kernel SHA-256:
  `7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2`
- Review role: focused post-hygiene body, delimiter, EOF, equation, and
  scope replay
- Verdict: **PASS**

## 1. Result

**PASS.** The candidate and durable kernel now have exactly the same
mathematical body, including the same final newline.  The kernel header
contains the current candidate hash, and the remaining header
differences are the intended candidate-versus-kernel status metadata.

The hygiene repair made no mathematical change.  It replaced the
unpaired prose backtick/apostrophe around the transported superscript by
the paired inline-math form \({\rm tr}\), and it normalized the kernel
to one EOF newline.  Every equation, tag, projection, estimate,
dependency, caveat, and owner-scope statement is unchanged.  In
particular, (191.C12) remains open.

## 2. Exact statement and hypotheses

Beginning at `## Candidate statement`, the current candidate and kernel
are raw character-for-character matches.  Hence the kernel retains the
full repaired statement: all positivity and unit quantifiers, the
literal \(v\)-support and \(L\ll X^{1/4}\) connector, the empty and
saturated cases, the disjoint power-of-two \(J\)-partition, the
fixed/global packet distinction, all inherited literal fields, both
orientations, and one final real part.

The exact conclusion is also unchanged.  The strict signed-inverse
sector and the terminal/Fejer projections are target-safe at fixed
packet scale; their lifted global aggregate satisfies the stated
\(L^2X^\varepsilon\) bound; and C32a--C32b give the exact global
safe/remainder decomposition C11.  No assertion closes the remaining
large-inverse packet.

## 3. Proof and derivation

The equal raw bodies each contain 21,315 characters and have SHA-256

`f29eb55c0620bfdfbafb3974fa23bc6cd01594de04668b857d96f2c61d9834d4`.

There is exactly one repaired transported-superscript phrase and no
copy of the former malformed phrase.  Replacing only
\({\rm tr}\) in that prose sentence by the former backtick/apostrophe
spelling reconstructs the previously reviewed normalized body digest

`b3d077ed9e398ab9d5a81959fa46eac39bcd2b7e5e43d08c7841d90bc83b482b`.

This checksum replay proves that the prose-delimiter repair is the only
body-content change from the preceding accepted comparison.  The
previous kernel's extra terminal newlines disappear under that earlier
normalization and are now absent on disk.

Independently, all 53 display-math blocks in the candidate and kernel
match exactly, and their 53-tag sequences match exactly.  This includes
the signed transport C17--C20a, source partition C22d, conjugated
endpoint telescope C24a, literal first-change list C25a, exact
projections C28a--C28d, outer operator C32a--C32b, power ledger
C33--C35, and bounded-array identity C38.  Thus no sign, gate,
orientation, modulus placement, lift, or power was altered.

## 4. First doubtful or unproved step

The first unproved step is still exactly

\[
 \boxed{\Re\mathscr R_{Y,Q}^{\sigma}
       \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{191.C12}
\]

Each artifact has exactly one C12 tag, followed by the words “remains
open,” and neither contains an affirmative C12-proof statement.  The
later C38 paragraph still says that separable positive control cannot
prove C12 and that C38 is not a disproof.  The first missing input
remains a signed theorem for the complete remainder.

Accordingly, the strict-sector reduction does not close the rest of the
\(t=1\) owner, any \(t\ge2\) or large-\(G\) complement, either M1
parent, M9, either bridge, or the quarter theorem.  Every exponent
remains unchanged.

## 5. Required control test and outcome

All requested hygiene and consistency controls pass:

- the on-disk hashes equal the dispatched candidate and kernel hashes;
- the kernel's `Formal candidate SHA-256` field equals the current
  candidate hash;
- both files end in exactly one LF byte, preceded by the final period,
  with no EOF blank line;
- the candidate has 10 backticks and the kernel 12, all paired on their
  respective lines; neither has an odd-backtick line or a fence run;
- each has 123 paired inline-math delimiters, 53 paired display-math
  delimiters, and five paired `aligned` environments;
- both have 53 unique equation tags in the same order, with no missing
  projection tag;
- strict UTF-8 decoding passes with zero forbidden control bytes and
  zero replacement characters; and
- there is no trailing whitespace or whitespace-diff error.

Outcome: no Markdown, EOF, TeX, equation, tag, projection, C12, or
scope regression remains.

## 6. Dependencies and exact artifacts used

This focused replay inspected only:

1. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md`, at SHA-256 `76c1a3adb14fc00063a2fcab06f73458ae8f5c9b0e7d19e41c5d8c78f103b978`;
2. `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`, at SHA-256 `7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2`.

The immediately preceding accepted body digest was used only as a
checksum target for the one-phrase hygiene reconstruction.  No control,
state, synthesis, validation, plan, sibling artifact, or unrelated
kernel was opened, and no numerical or symbolic experiment was run.

## 7. Recommended state effect

**Promote/retain.** Accept the hygiene-repaired kernel as the durable
subordinate `proved_internal` reduction for (191.C5)--(191.C11).
Retain (191.C12), all larger owners, and every exponent unchanged.  No
further candidate or kernel repair is required, and this review makes
no state mutation.
