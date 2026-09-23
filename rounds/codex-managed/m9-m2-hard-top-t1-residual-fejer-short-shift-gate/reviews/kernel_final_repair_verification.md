# Round 165 final kernel repair verification

## 1. Result

**GREEN.** All four repairs requested by the focused audit are present in
the current terminal kernel, and no mathematical or proof-status wording
was damaged.

The repaired kernel now:

1. defines parity by the absolute site \(s+j\);
2. states (165.K7a) only for \(R=2S+1\ge3\), uses
   \(j=0,\ldots,T-1\), and treats \(R=1\) separately;
3. excludes open (165.K17a) from the ranges declared proved internally;
   and
4. prints the maximal-scale epsilon bookkeeping with
   \(\eta=2\varepsilon\) before taking the square root.

The current \(g=(d,d')\), \(s=(m,m')\), and \(G_0\) notation remains
unambiguous. Equations (165.K17a) and (165.K26) remain explicitly open,
their sufficiency implications remain proved, and the terminal label and
downstream quarantine are unchanged.

## 2. Exact statement and hypotheses

The repaired parity definition is

\[
 Y_s^{(\epsilon)}
 =\sum_{\substack{0\le j<R\\s+j\equiv\epsilon\pmod2}}z_{s+j},
 \qquad \epsilon\in\{0,1\}.
\tag{165.F1}
\]

For odd \(R=2S+1\ge3\), the kernel defines

\[
 \mathcal E_T(w)=T^{-1}\sum_k
 \left|\sum_{j=0}^{T-1}w_{k+j}\right|^2
\tag{165.F2}
\]

and prints the exact convex parity decomposition (165.K7a). At \(R=1\),
it separately states

\[
 \mathfrak E_1=\mathfrak E_1^{(2)}=D_L.
\tag{165.F3}
\]

The repaired status sentence declares only

\[
 (165.K4)\text{--}(165.K12),\qquad
 (165.K14)\text{--}(165.K17),\qquad
 (165.K18)\text{--}(165.K25)
\tag{165.F4}
\]

proved internally, together with the implications from the boxed open
estimates. It then separately identifies (165.K17a) and (165.K26) as
unproved.

## 3. Proof or derivation

The absolute-site condition in (165.F1) is the condition needed for a
pair to survive in one parity component exactly when its gap is even.
Thus (165.K7)--(165.K9) retain the exact weight \(1-r/R\), including
weight \(1/R\) for the terminal even gap when \(R\) is odd.

The restriction \(R\ge3\) in (165.K7a) removes the previously undefined
\(\mathcal E_0\). Equation (165.F3) closes the omitted \(R=1\) case
directly, so the all-\(R\) parity connector remains valid.

The proof-status range (165.F4) no longer syntactically includes
(165.K17a). The surrounding text is consistent:

- (165.K12) and (165.K17) are proved target-safe sectors;
- (165.K13) is an open broader sufficient theorem;
- (165.K17a) is the sharpest open minimal-scale theorem; and
- (165.K26) is the open maximal-scale alternative.

At \(R=M_L\), the repaired final proof paragraph still uses the exact
chain

\[
 \mathfrak E_{M_L}^{(2)}\ll_\eta L^3X^\eta,\qquad
 \mathfrak E_{M_L}\le2\mathfrak E_{M_L}^{(2)},\qquad
 {2M_L-1\over M_L}<2.
\tag{165.F5}
\]

It now explicitly invokes (165.K3), (165.K25), and the hypothesis
(165.K26) with \(\eta=2\varepsilon\), and therefore obtains

\[
 |\mathcal S_{L,1}^{\rm rem}|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{165.F6}
\]

The added positive-domain convention in (165.K5) is also safe: it is
equivalent to zero extension while avoiding evaluation of a square root
off the positive literal pair domain. No correlation term is deleted.

## 4. First doubtful or unproved step

No repair remains doubtful. The first unproved estimates are still
(165.K17a) and (165.K26). The kernel proves only that either estimate is
sufficient on its stated scale.

Nothing in the repairs supplies cancellation for either open aggregate,
and nothing changes the status of the complete residual or any downstream
obligation.

## 5. Control tests and outcomes

| Repair control | Outcome |
|---|---|
| absolute-site parity | **GREEN.** Printed explicitly before (165.K7). |
| odd-\(R\) normalization | **GREEN.** (165.K7a) is restricted to \(R\ge3\). |
| inner window range | **GREEN.** The definition uses \(j=0,\ldots,T-1\). |
| \(R=1\) endpoint | **GREEN.** Treated separately by \(\mathfrak E_1=\mathfrak E_1^{(2)}=D_L\). |
| gcd notation | **GREEN.** \(g\), \(s\), and \(G_0\) retain distinct roles. |
| incidence ownership | **GREEN.** The high-gcd sector is scoped to opened divisor incidences. |
| combined frontier | **GREEN status.** (165.K17a) remains open and sufficient. |
| proved-equation range | **GREEN.** Open (165.K17a) is excluded. |
| maximal-scale implication | **GREEN.** Parity, short payment, and (165.K26) recombine exactly. |
| epsilon bookkeeping | **GREEN.** \(\eta=2\varepsilon\) is explicit. |
| positive square-root domain | **GREEN.** Equivalent to zero extension. |
| terminal status and scope | **GREEN.** Label and downstream quarantine are unchanged. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

This verification used:

1. proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md; and
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reviews/kernel_parity_scale_repair_review.md.

No shared proof state, external source, web lookup, or computation was
used.

## 7. Recommended state effect

**Accept the four repairs as complete.** The terminal kernel requires no
further mathematical or textual change from this seam.

Retain the proved parity, tangent, dual-gcd, high-gcd, and variable-scale
reductions and the terminal label strict_residual_short_shift_sector,
subject to the conductor's remaining graph validation.

Keep (165.K17a), (165.K26), the complete residual, full \(t=1\) face,
all other few-point channels, both hard-TOP parents, BAL, UNBAL, smooth
M2, M9--M2, M9--M1, endpoint uniformity, M9, the bridge, the quarter
theorem, and both global exponents open.
