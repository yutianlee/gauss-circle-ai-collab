# Final kernel/candidate consistency review

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Round: 191
- Candidate SHA-256:
  `263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`
- Kernel SHA-256:
  `18b169b96ce9521ad91be748c3562e8974f4f5fcb3d067f76102ae6f54b4df05`
- Review role: final mathematical-body, projection, tag, and open-scope
  consistency seam
- Verdict: **PASS**

## 1. Result

**PASS.** The durable kernel is mathematically identical to the
post-repair candidate.  Beginning at `## Candidate statement`, the two
artifacts have the same statement, hypotheses, prose derivation,
equations, equation tags, exact projections, bounds, method boundary,
dependencies, and proposed narrow state effect.  The only body-level
byte difference is two additional terminal newline characters in the
kernel; it has no mathematical or rendering effect.

The header changes are the intended promotion metadata: the title is
changed from a formalized candidate title to the kernel title, the
candidate's pending-replay status is replaced by the exact formal
candidate hash and durable-evidence status, and the common campaign,
round, starting graph hash, and declaration of no numerical theorem
evidence are retained.  No mathematical claim was strengthened during
the copy.  In particular, (191.C12) remains explicitly open.

## 2. Exact statement and hypotheses

The copied kernel retains every quantified hypothesis certified by the
post-repair PASS:

- \(X\ge2\), a nonempty inherited middle or lower residual hard-M1
  shell \(L\ge2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\), and
  \(Q=\lfloor(\log(2X))^B\rfloor\);
- positive integral arithmetic labels, \(1\le a<q\), \((a,q)=1\), the
  full conditions (191.C2)--(191.C3), the literal support length
  \(O(u)\), and \(L\ll X^{1/4}\);
- the empty saturated projective case, the exact disjoint half-open
  power-of-two \(J\)-partition, and both empty/saturated signed-inverse
  cases;
- preservation of every inherited literal field, both orientations,
  the fixed complex packet type, the global complex aggregate type, and
  one final real part.

The conclusion is unchanged: (191.C8)--(191.C10) prove the fixed
strict-inverse and safe-projection bounds and their lifted global
\(L^2X^\varepsilon\) bound; (191.C11) is the exact complex
safe/remainder decomposition; (191.C12) is only the required open
remainder estimate.  All larger owners and all exponents remain at
their prior open or conditional scopes.

## 3. Proof and derivation

The comparison was performed at the exact mathematical-body interface.
After normalizing line endings and ignoring terminal newline padding,
each body has 21,306 characters and the same SHA-256

`b3d077ed9e398ab9d5a81959fa46eac39bcd2b7e5e43d08c7841d90bc83b482b`.

Thus the equality is character-for-character, not merely semantic.
As explicit seam checks:

1. all 53 display-math blocks agree in order and content;
2. all 53 tags agree in order and content, from (191.C1) through
   (191.C38), including C3a, C13a, C20a, C22a--C22d, C24a, C25a,
   C28a--C28d, and C32a--C32b;
3. the signed-inverse/carry transport (191.C17)--(191.C20a) is
   unchanged;
4. the exact \(K,G\) source partition C22d, transported affine
   partition C23, two-endpoint conjugated product rule C24a, and
   ordered literal first-change partition C25a are unchanged;
5. the strict-sector inverse-class count and exact inverse-Abel return
   (191.C26)--(191.C28) are unchanged;
6. the terminal atom and the fully gated joint complex terminal and
   Fejer projections C28a--C28c, their safe sum and exact complement
   C28d, and the estimates C30--C32 are unchanged;
7. the inherited linear outer operator C32a--C32b, exact
   \(m^{-1}c_q(a)\) lift, divisor/power ledger C33--C35, and fresh
   \(0<\eta<\varepsilon\) rebudget are unchanged; and
8. the bounded-zero-extended-array capacity identity C38 and all its
   no-go qualifications are unchanged.

Consequently no target-safe term has been detached, no orientation has
been separately normed, no literal gate has been dropped, no power of
\(Y\) has been hidden, and no fixed/global packet type has regressed.
The post-repair proof accepted in the prior PASS is exactly the proof
present in the durable kernel.

## 4. First doubtful or unproved step

The first unproved step remains exactly

\[
 \boxed{\Re\mathscr R_{Y,Q}^{\sigma}
       \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{191.C12}
\]

Both artifacts state immediately after this display that it “remains
open.”  Each has exactly one C12 tag, no affirmative sentence claiming
that C12 is proved, and the same later statements that separable
positive control cannot prove it, that C38 is not a disproof, and that
the missing input is a signed theorem for the complete remainder.

This is the correct protocol boundary.  The kernel proves the strict
sector and exact reduction only; it does not close the complete fast
packet, the remaining \(t=1\) owner, any \(t\ge2\) or large-\(G\)
complement, M9, either bridge, or the quarter theorem.

## 5. Required control test and outcome

The required control was an exact candidate-to-kernel body comparison,
supplemented by structural integrity checks.  It passed:

- the on-disk candidate and kernel hashes equal the two dispatched
  hashes;
- the normalized bodies and every display block and tag sequence are
  exact matches;
- the raw body lengths differ only by two terminal newline characters;
- both files decode as strict UTF-8, with zero forbidden C0/DEL bytes
  and zero replacement characters;
- each has 53 matched display delimiters, 122 matched inline-math
  delimiters, five matched `aligned` environments, 333 opening and 333
  closing unescaped braces, 53 unique tags, and every required
  projection tag;
- each has exactly one C12 tag followed by “remains open,” and neither
  has an affirmative C12-proof statement; and
- the whitespace diff check is clean.

Outcome: no mathematical, TeX, encoding, projection, tag, or
open-scope regression was found.

## 6. Dependencies and exact artifacts used

This consistency replay used only the four authorized artifacts:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md`, at candidate SHA-256 `263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`;
3. `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`, at kernel SHA-256 `18b169b96ce9521ad91be748c3562e8974f4f5fcb3d067f76102ae6f54b4df05`;
4. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/reviews/signed_inverse_normalization_transport_power_postrepair_verification.md`.

No control, shared state, synthesis, validation, plan, campaign, sibling
review, or unrelated kernel was opened.  No numerical or symbolic
experiment was used; the machine work was limited to exact hashes,
text equality, tag/delimiter inventories, and encoding diagnostics.

## 7. Recommended state effect

**Promote/retain.** Accept the kernel as the durable subordinate
`proved_internal` reduction for (191.C5)--(191.C11), consistent with
the post-repair PASS and the protocol's narrow-kernel rule.  Retain
(191.C12), all larger owners, and every exponent unchanged.  No kernel
repair is required, and this review makes no state mutation.
