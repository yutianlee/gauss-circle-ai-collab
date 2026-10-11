# Round222 independent review of the product-phase certificate

## 1. Result

**GREEN for the scoped finite identities, complete BV-symbol certificate estimate, and actual buffered failed-certificate control. No complete UNBAL or pointwise gain is certified.**

The final reviewed claimant is reports/actual_product_phase_attack.md in rounds/codex-managed/m9-m2-complete-unbalanced-vector/, SHA256:

    86d5dfa556ed71e925cb02331f8c59f9f4167f4c8eba0ad3c84743544fa0ec97

The initially reviewed version had SHA256:

    87cf5fbd265786d8b21a3fef8e49105b821568e61e83fbff390fc9494ae52baa

Its matrix mathematics and restored powers were correct, but its blanket statement that the conservative fallback paid "any companion" was broader than the exhibited proof. The proof establishes \(O(D)\) for the displayed original finite expression (9), verified bounded-weight cuts of that expression, and the listed physical endpoint terms. It does not automatically estimate an unidentified correction.

I inspected the repaired report's Sections 2 and 3.7, owner-control row and repair provenance. They now explicitly impose this restriction and leave other corrections with their inherited estimates and owners. **The repair cures the issue.** No additional repair is required for the scoped conclusions certified here.

The actual buffered family has the stated physical certificate exponent \(11/32\), strictly for the rectangle certificate capped by the coefficient triangle. This is not an actual signed lower bound or a floor for all previously available fallback estimates.

## 2. Exact statement and hypotheses reviewed

The target remains the actual complete smooth UNBAL inequality

\[
 T=\sum_{h\asymp L,k\asymp K}\chi_4(h)a(h,k)e(\sqrt{Xhk})
 \ll_\epsilon (LK)^{3/4}X^\epsilon,\qquad
 K=XL/D^2,\quad K/L>16.
 \tag{R1}
\]

The tested sufficient certificate uses \(A_{h,k}=a(h,k)e(\sqrt{Xhk})\) on odd positive rows, with zero extension outside the literal support and an enclosing column interval of length \(O(K)\). The actual symbol is

\[
 a(h,k)=\eta(h/L)\Phi(h/(H_D+1))(LK/(hk))^{3/4}
 W\!\left(\sqrt{hX/(4kD^2)}\right),\qquad
 H_D=\lfloor DX^{-1/4}\rfloor .
 \tag{R2}
\]

The upper bound assumes uniformly bounded column supremum and total variation, preserved by a fixed number of column interval cuts and stars. It requires no derivative across row cuts. The lower control additionally requires fixed nonzero interior profiles, a full buffered frequency piece, \(L,K\to\infty\), and \(L/H_D\to0\). It is not a lower statement for arbitrary vanishing or clipped symbols.

Writing \(R=X/D\), \(M=LK\), and \(E_4=\operatorname{tr}((AA^*)^2)\), the checked claims are

\[
 |T|\le(n_hn_k)^{1/2}E_4^{1/4},\qquad
 E_4\ll LK^2+RL^3+(LK^2/R)\log(2L),
 \tag{R3}
\]

and, after the coefficient-triangle cap and the inherited smooth transformation,

\[
 |\mathcal B^+|\ll_\epsilon X^{1/4+\epsilon}
 \min\{M^{1/4},(K+DL+L/D)^{1/4}\}+O_W(1).
 \tag{R4}
\]

The inherited transformation has factor \(-e(1/8)X^{1/4}M^{-3/4}/(2\pi)\). Its error and smooth-denominator hypothesis remain in force. No hard-denominator transformation or unidentified correction estimate is an implicit hypothesis of this review.

## 3. Independent mathematical checks

**Signed increments and integer aliases.** Extend \(b_{h,k}=\chi_4(h)a(h,k)e(\sqrt{Xhk})\) by zero. Summing all two-coordinate autocorrelations gives exactly \(|T|^2\). Phases need only be evaluated where both entries lie in the positive support. Odd row increments contribute zero. For odd \(h=2s+1\),

\[
 \chi_4(h+2r)\chi_4(h)=(-1)^{s+r}(-1)^s=(-1)^r.
 \tag{R5}
\]

The claimant's amplitude, sign and conjugations in (13)--(15) are correct. Negative increments are conjugates of the positive increments after translating the row, giving the stated \(2\Re\) multiplicity. The identity \(\chi_4(h)=(e(h/4)-e(3h/4))/(2i)\) retains both quarter shifts and their cross terms.

For the same-column increment, adding the alternating phase \(r/2\) gives derivative

\[
 \frac{\sqrt{Xk}}{\sqrt{h+2r}}+\frac12\asymp
 \sqrt{XK/L}=R.
\]

Equality to an integer \(m\) requires \(m-1/2>0\) and \(h+2r=4Xk/(2m-1)^2\). Thus the half shift does not permit a distance-from-zero derivative estimate. The report correctly uses this as a diagnostic, not a new transformation or a claim that these aliases are negligible.

**Vector factors and four corners.** On odd rows \(u_h=\chi_4(h)\) is real, so \(T=u^*Av\), where \(v_k=1\). The two vector norms are \(\sqrt{n_h}\) and \(\sqrt{n_k}\); no further averaging factor is available. The operator norm is at most the fourth Schatten norm \(E_4^{1/4}\). Expanding \(\sum_{h,h'}|(AA^*)_{h,h'}|^2\) gives phase

\[
 \sqrt X(\sqrt{h_1}-\sqrt{h_2})
                  (\sqrt{k_1}-\sqrt{k_2})
 \tag{R6}
\]

and amplitude \(a_{11}\overline{a_{21}}\overline{a_{12}}a_{22}\), exactly as claimed. Multiplication of odd rows by \(\chi_4(h)\) is unitary and preserves \(E_4\). The first norm inequality in (19) therefore loses the prescribed fixed-vector signs. The report identifies that loss accurately.

**Derivative, trace and physical costs.** For \(r=|h-h'|\ge1\),

\[
 f''(k)=-\frac{\sqrt X(\sqrt h-\sqrt{h'})}{4k^{3/2}},
 \qquad |f''(k)|\asymp
 \frac{\sqrt Xr}{\sqrt L K^{3/2}}=\frac{Rr}{K^2}.
 \tag{R7}
\]

The product of the two actual column profiles has bounded supremum plus variation. The inherited second-derivative estimate and Abel summation therefore give \(\sqrt{Rr}+K/\sqrt{Rr}\), with a separate trivial cap \(K\). This estimate treats the whole integer interval and all integer aliases. It does not use complete-period orthogonality on a short window.

Equal rows cost \(LK^2\). There are \(O(L)\) pairs at each increment. Squaring and summing the two off-diagonal terms gives \(RL^3\), \((LK^2/R)\log(2L)\), and cross term \(L^2K\). Since \(K>L\), the cross term is absorbed in \(LK^2\). Odd-row parity restricts increments to even values and changes only constants. Short or empty rows cause no difficulty, and the trivial cap remains available when the curvature exceeds one.

The restored norm product is

\[
 X^{1/4}M^{-3/4}\sqrt M\,E_4^{1/4}
     =X^{1/4}(E_4/M)^{1/4}.
\]

Dividing the trace terms by \(M\) gives \(K\), \(RL^2/K=DL\), and \(K/R=L/D\). The logarithm in the last term is absorbed only after this restoration. The coefficient triangle gives \(X^{1/4}M^{1/4}\). This proves the claimant's displayed physical upper certificate and its complete finite output cost.

**Actual lower buffer and dyadic control.** Nonzero interior values of \(\eta\) and \(W\) supply \(x_0,u_0>0\). Setting \(y_0=x_0/(4u_0^2)\) gives a fixed small product rectangle inside the actual slanted support on which both profile moduli are bounded below. Since \(L/H_D\to0\), continuity and \(\Phi(0)=1\) make the Vaaler factor uniformly bounded below there. The normalized power \((xy)^{-3/4}\) is also bounded below. Consequently the rectangle contains \(\gg L\) odd rows and \(\gg K\) integer columns with coefficient modulus \(\gg1\).

An independent direct check of the trace lower bound is available: every buffered row has diagonal Gram entry \(\sum_k|a(h,k)|^2\gg K\). The squares of these diagonal entries alone give \(E_4\gg LK^2\). This agrees with the claimant's trace/rank Cauchy argument without transferring an abstract unweighted rank obstruction to actual coefficients. Also \(\sum|a(h,k)|\asymp LK\). Since \(L^{3/4}K\le LK\), the dual coefficient-triangle cap does not remove the lower certificate scale \(L^{3/4}K\).

For \(X=2^{24j}\), the labels are exactly \(D=2^{8j}\), \(L=2^j\), \(K=2^{9j}\), and \(H_D=2^{2j}\). Thus \(L/H_D\to0\), \(K/L>16\) eventually, and \(178/24+1638/3>463\). The family is a strict legal residual family. Here \(K=DL\), both main trace costs have exponent \(19/24\), and the rectangle certificate has dual exponent \(13/32\). The physical factor has exponent \(-1/16\), yielding \(11/32\), with gap \(3/32\) from quarter.

This floor concerns the specified rectangle certificate capped only by the dual coefficient triangle. If one additionally uses the old original-side \(O(D)\) estimate, this family has the smaller available upper price \(X^{1/3+\epsilon}\). Hence \(11/32\) is not a floor for every available method or fallback. The claimant's precise certificate statement and explicit elementary comparison respect this distinction.

**Exponent and elementary comparisons.** With \(a=\delta-\ell\), the three restored exponents are

\[
 b_1=\frac12-\frac\delta4-\frac a4,\quad
 b_2=\frac14+\frac\delta2-\frac a4,\quad
 b_3=\frac14-\frac a4.
\]

The larger of the first two switches at \(\delta=1/3\), and \(b_3\) is smaller. The triangle exponent is \(b_0=(1-a)/2\). The claimant's three region checks correctly prove \(\min(b_0,\max(b_1,b_2))\ge\min(a,b_0)\) on the legal flat region. No flat-envelope gain follows, and no flat result is transferred to a different owner.

The comparison with the elementary actual smooth bound is also correct. If \(D\le X^{1/3}\), then \(X^{1/4}K^{1/4}\ge D\), using \(L\ge1\). If \(D\ge X^{1/3}\) and \(M<DL\), the triangle cap is selected. Otherwise \(M\ge DL\) implies \(L\ge D^3/X\), and \(X^{1/4}(DL)^{1/4}\ge D\). The rectangle certificate therefore does not improve \(\min(D+1,X^{1/4}M^{1/4}+1)\).

## 4. First gap and verified repair

No mathematical repair is needed in the signed finite algebra, the trace estimate, its restoration, or the buffered lower control under their written hypotheses. The first missing positive estimate remains a signed bound before the all-vector inequality (19). Better evaluation of this same positive certificate cannot prove quarter on the buffered family, because its actual diagonal mass already forces the stated floor.

The pre-repair scope defect was precise: absence of a BV dual representation was followed by an unqualified assertion that any further companion could still be paid on the original side. The report had not exhibited that side for an unspecified correction.

For the actual sum (9), the mass bounds \(\sum_{h\asymp L}|q_L(h)|/h=O(1)\) and \(\sum_d|W(d/D)|=O(D)\) do prove \(O(D)\). Fixing one \(h\asymp L\) gives \(O(D/L)\); fixing one \(d\) gives \(O(1)\). Verified bounded-weight cuts, fixed endpoint weights and bounded-variation cutoff differences of this expression preserve these conservative prices. They do not prove the same result for an unidentified transform correction.

The final repair is explicit at every relevant seam:

- Section2 says neither its sharper certificate nor its \(O(D)\) fallback automatically applies to a correction lacking an original-side representation and coefficient-mass bound.
- Section3.7 states the two mass estimates, restricts its cuts and endpoint claims to that expression, and leaves other corrections with their inherited estimates and owners.
- It also states that the dyadic label count supplies no estimate for an untreated correction.
- The owner-control row repeats the restriction, and the repair provenance records this review issue.

These local changes cure the issue. The final report does not claim an unidentified additional package is paid. Hard denominator endpoints retain their separate owner, and this review does not supply a missing sharp-endpoint transformation.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Even increment and both quarter shifts | GREEN: exact sign \((-1)^r\), conjugations and mixed terms verified. |
| Integer aliases | GREEN: half-shift derivative and odd-label equation verified; no aliases deleted. |
| Four corners and vector factors | GREEN: amplitude, mixed phase, both vector norms and fourth root are correct. |
| BV symbol, large curvature and short rows | GREEN: the inherited derivative estimate applies with the trivial cap available in every regime. |
| Full trace and restoration | GREEN: diagonal, increment sum, harmonic term, cross term, logarithm and smooth error are paid. |
| Actual buffer | GREEN only for the selected nonzero interior family; no unbuffered weighted-rank transfer. |
| Exact dyadic/floor control | GREEN: the stated sequence realizes all labels and the exact height floor. |
| Certificate versus signed lower bound | GREEN: \(11/32\) is the named rectangle/dual-triangle certificate floor only. |
| Real signs and endpoints | GREEN for the actual real pairing and explicitly smooth transform; sharp denominator endpoints stay separate. |
| Companion-scope repair | GREEN: final Sections2/3.7 and owner control restrict \(O(D)\) to represented original sums and verified cuts/endpoints. |
| Full frontier | No new complete UNBAL, M2, M1, endpoint, moment-family or pointwise exponent conclusion. |

All checks are analytical. Zero experiments, source searches or new theorem imports.

## 6. Exact dependencies and provenance

This is an independent **nonblind**, claimant-avoiding review. I authored the current222 joint cross-modulus report and retain disclosed218--221 role history. I did not author the reviewed product report. Its proof was read expressly for this assignment; no other current sibling was read during this review.

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| Current222 reports/actual_product_phase_attack.md, final repaired claimant | 86d5dfa556ed71e925cb02331f8c59f9f4167f4c8eba0ad3c84743544fa0ec97 |
| Same claimant, inspected pre-repair version | 87cf5fbd265786d8b21a3fef8e49105b821568e61e83fbff390fc9494ae52baa |
| Current222 briefs/conductor_actual_unbal_interface.md | 7cb7bfd2a69a6cf57e2bdbb0bc90f0f65f09696edbb2a1cf05e09502500045c3 |
| rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md | a97702a1a4608e106d4171a4fd713eca5a2c9693b61ee89ca1eb0eb51621b3c3 |
| Previously read permitted proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md | 584745fb9af72993a4b33eb95dad3421e8924ae5fb64c5b314511b08d4254baf |

The packet quotes starting graph SHA256 a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b; the graph was not reread for this review. Accepted160 is used only to distinguish its unweighted scalarization obstruction from the proved actual buffer, not as a premise granting a matrix gain. The smooth-transform report supplies the accepted normalization, error scope and elementary derivative input. No external theorem has been re-audited or enlarged.

The conductor requested one narrow same-round claimant repair after my first mathematical check. I verified the corrected local statements and final claimant hash, retaining the first hash above as provenance. This was not a second mechanism or source audit.

## 7. Recommended state effect

Retain the final-hash product-report identities and priced certificate failure as **GREEN evidence**. The only requested repair, the companion-scope restriction, is explicitly verified and cured. Make no change to the complete target or accepted exponents.

Any future complete-companion bound still needs its original-side identification or another valid estimate. The certificate floor remains distinct from an actual signed lower bound.

Only this assigned review file was written. No claimant edit, shared-state change, source work, experiment or successor work was performed. The task stops with the final review hash.
