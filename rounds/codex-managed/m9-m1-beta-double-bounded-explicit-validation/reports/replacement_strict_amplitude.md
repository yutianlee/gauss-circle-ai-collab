## 1. Result

Isolation status: `contaminated_independent_not_counted_as_strict_gate`.

The frozen theorem is **not established from the displayed hypotheses as written**.  The packet gives only
\(a+b<1/2\) and \(a/2+b<1/4\).  These upper inequalities do not imply either the absolute \(q\)-summability required by the brief or a target-safe absolute sum over the active \(j\)-scales.  In particular, for all sufficiently large \(X\), the permitted choice
\[
 a=-1,
 \qquad b=\frac1{\log(2X)}
\]
has
\[
 p=\frac34+\frac b2<1,
\]
so \(\sum_q |\chi _4(q)|q^{-p}\) diverges.  Thus the requested absolute \(h,q\) derivation cannot even be formed on the stated contour.

There is, however, a short complete repair at the local-amplitude level.  If one adds
\[
 \sigma:=a+b\ge 0
\tag{H\(_\sigma\)}
\]
and reads the stated logarithmic-monomial description literally, so that \(x\partial_xM_\tau\) obeys the same kind of polylogarithmic bound and \(W_\tau\) has no unlisted \(x\)-dependence, then
\[
 \sup_{1\le x\le N_X}
 \bigl(|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\bigr)
 \ll \log^C(2X).
\]
The displayed radial-BV implication then gives the displayed polylogarithmic radial integral.  The final \(O_\varepsilon(X^{1/4+\varepsilon})\) restoration cannot be independently checked because the packet does not display the external factor.

## 2. Exact statement and hypotheses

The unconditional no-go statement is:

> The two displayed contour inequalities and the frozen-family seminorms do not imply the requested proof by absolute \(h,q,j\) summation.  Indeed, they allow \(p\le1\), and they also allow negative \(a+b\), for which the bottom active scale has polynomially large displayed scale weight.

The repaired amplitude statement proved below uses exactly the packet definitions, together with:

1. \(X\) is sufficiently large, \(b=1/\log(2X)\), \(\sigma=a+b\ge0\), \(\sigma<1/2\), and \(a/2+b<1/4\).
2. The only \(x\)-dependence of \(M_\tau\) not explicitly shown in \(g_\tau\) is its stated fixed-degree monomial in the listed logarithms.  Consequently, on the compact \((L,\beta)\)-support,
   \[
   |M_\tau|+|x\partial_xM_\tau|\ll_\tau\log^{C_\tau}(2Xhq).
   \]
3. A normalized \(W_\tau(L-\nu)\) has the stated fixed Schwartz seminorms and no additional uncontrolled \(x\)-dependence.
4. \(|\mathfrak T|=O(1)\), singular types occur only at \(j=0\), and all support and profile bounds are exactly those displayed in the packet.

No assertion is made here that the actual routed operator equals this finite family.  That identification is expressly outside this task.

## 3. Proof or derivation

Write
\[
 P_X:=\|p\|_1+\|p'\|_\infty+|(1+|\nu|)p\|_1
      +\sup_\nu(1+|\nu|)^3|p(\nu)|,
\]
so \(P_X\ll\log^C(2X)\), uniformly in active \(j\) and \(x\).  On the fixed support of \(M_\tau\),
\[
 |A|\ge1,
 \qquad
 |D|\gg_{C_0}1+|\nu|.
\tag{3.1}
\]

For the signed top, set
\[
 Q_p(L,\beta):=
 \int_{\mathbb R}\frac{p(\nu)-p(L)}{(L-\nu)D}\,d\nu.
\]
On \(|\nu-L|\le1\), the numerator is bounded by
\(\|p'\|_\infty|\nu-L|\).  On \(|\nu-L|>1\), the \(p(\nu)\) part is controlled by \(\|p\|_1\), while the constant \(p(L)\) part is controlled by the uniformly finite integral
\[
 \int_{|\nu-L|>1}\frac{d\nu}{|L-\nu|\,|D|}.
\]
Using (3.1) and the pointwise bound on \(p\),
\[
 |Q_p(L,\beta)|\ll P_X.
\tag{3.2}
\]
It is essential here that the difference \(p(\nu)-p(L)\) is retained before absolute values.  Equations (3.1)--(3.2) give
\[
 |\mathsf P_\tau|\ll |g_\tau|P_X.
\tag{3.3}
\]

The exact modulation gives
\[
 x\partial_xp_{j,x}(\nu)=-\frac{i\nu}{2}p_{j,x}(\nu).
\tag{3.4}
\]
For \(q_p(\nu):=\nu p(\nu)\), the same near/far split works: near \(L\),
\[
 |q_p(\nu)-q_p(L)|
 \le |\nu-L|\sup_{|t-L|\le1}|p(t)+tp'(t)|\ll P_X|\nu-L|,
\]
and away from \(L\), (3.1) and \(\|(1+|\nu|)p\|_1\) give
\[
 \int_{|\nu-L|>1}
 \frac{|\nu p(\nu)-Lp(L)|}{|L-\nu|\,|D|}\,d\nu
 \ll P_X.
\tag{3.5}
\]
Moreover, the literal logarithmic-monomial hypothesis and compactness of \(L,\beta\) imply
\[
 |g_\tau|+|x\partial_xg_\tau|
 \ll_\tau\log^{C_\tau}(2Xhq),
\tag{3.6}
\]
because the two displayed \(x\)-phases contribute exactly \(-iL/2\) and \(-i\beta\).  Differentiating the signed functional as one recombined object and applying (3.2), (3.4)--(3.6) proves
\[
 |\mathsf P_\tau|+|x\partial_x\mathsf P_\tau|
 \ll \log^C(2Xhq).
\tag{3.7}
\]

For a smooth type, (3.1), the fixed Schwartz seminorm, and \(\|p\|_1\) give
\[
 \left|\int_{\mathbb R}\frac{p(\nu)W_\tau(L-\nu)}D\,d\nu\right|
 \ll P_X\log^C(2X).
\]
After one \(x\)-derivative, (3.4) is controlled by
\(\||\nu|p\|_1\), and (3.6) controls the derivative of \(g\).  Hence
\[
 |\mathsf S_\tau|+|x\partial_x\mathsf S_\tau|
 \ll \log^C(2Xhq).
\tag{3.8}
\]
The \((L,\beta)\)-integration has fixed volume because \(M_\tau\) is compactly supported.  The factors \(-\pi i\), \((2\pi)^{-2}\), and the internal \((2\pi)^{-1}\) are fixed constants and occur exactly as displayed; they cause no residual contour loss.

It remains to sum the arithmetic and scale weights.  Put
\[
 \delta_h=r-1=\frac14-\frac{a+b}{2},
 \qquad
 \delta_q=p-1=\frac14+\frac{a+b}{2}.
\]
The second contour inequality gives
\[
 \delta_h
 =\left(\frac14-\frac a2-b\right)+\frac b2
 >\frac b2,
\tag{3.9}
\]
while (H\(_\sigma\)) gives \(\delta_q\ge1/4\).  Therefore, for every fixed \(K\), integral comparison (or differentiating the elementary zeta majorant) gives
\[
 \sum_{h,q\ge1}h^{-r}q^{-p}\log^K(2Xhq)
 \ll_K \log^{C_K}(2X),
\tag{3.10}
\]
since \(b^{-1}=\log(2X)\).  This is absolute, so \(|\chi_4(q)|\le1\) suffices and no character cancellation is being used.

For the floors, let \(n=\lfloor\sqrt X\rfloor\) and
\(y_j=D_jX^{-1/4}=2^{-j}nX^{-1/4}\).  On every active scale \(y_j\ge1\), hence
\[
 H_j+1=\lfloor y_j\rfloor+1\le2y_j.
\]
With \(\sigma=a+b\ge0\),
\[
 \begin{aligned}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 &\le
 2^{b-a}2^{-j\sigma}n^\sigma X^{-a/2-b/4}\\
 &\le C\,X^{b/4}2^{-j\sigma}
 \le C,
 \end{aligned}
\tag{3.11}
\]
where \(n^\sigma\le X^{\sigma/2}\), \(-b\le a<1/2-b\), and
\(X^{b/4}\le e^{1/4}\).  Thus the exact active set, including its bottom endpoint and all floors, satisfies
\[
 \sum_{j=0}^{J_X}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 \ll J_X+1\ll\log(2X).
\tag{3.12}
\]
Combining (3.7)--(3.12), the bounded cardinality of \(\mathfrak T\), and the fact that a singular type has the displayed \(\mathbf1_{j=0}\), proves the repaired boxed estimate, uniformly for \(1\le x\le N_X\).

The packet then supplies, as an already accepted implication,
\[
 \sqrt X\int_1^{N_X}x^{-3/2-b/2}e(\sqrt{Xx})
 \mathcal A_{\rm db}(x)\,dx\ll\log^C(2X),
\]
with full radial endpoint coefficients.  No half-weight is introduced anywhere in the argument above.  There is no displayed formula for the external factor, however, so its normalization and its occurrence exactly once cannot be derived or checked from this packet.

## 4. First doubtful or unproved step

The first failed step in an unconditional proof is the requested absolute \(q\)-sum.  It would require
\[
 p>1\quad\Longleftrightarrow\quad a+b>-\frac12,
\]
but neither displayed contour inequality implies this.  The concrete permitted choice \(a=-1\) above gives \(p<1\) and
\[
 \sum_{q\ge1}|\chi_4(q)|q^{-p}=\infty.
\]

Even adding merely \(p>1\) does not close the advertised absolute scale ledger.  For example, take \(a=-1/4\) and large \(X\), so \(p>1\) but \(a+b<0\).  At the last active index, \(1\le y_{J_X}<2\), hence \(H_{J_X}=1\) and
\[
 \left(\frac{D_{J_X}}{2\sqrt X}\right)^{-1/4}(H_{J_X}+1)^b
 \asymp X^{1/16}.
\]
The supplied seminorms contain no compensating scale decay.  Condition (H\(_\sigma\)) is therefore a natural sufficient repair for the absolute proof.

After that repair, the remaining unproved seams are not local analytic estimates: (i) the packet withholds the term-by-term identification of the actual routed operator with \(\mathfrak T\), and (ii) it withholds the exact external factor.  Neither can be certified from the allowed statement-only data.

## 5. Required control test and outcome

1. **Signed top constant/PV control — pass conditionally.**  The proof keeps
   \((p(\nu)-p(L))/(L-\nu)\) intact.  Its local limit is controlled by \(p'\); splitting the two terms before absolute values would destroy this control.
2. **Full \(x\)-phase derivative — pass conditionally.**  The displayed phases contribute \(-iL/2\), \(-i\beta\), and \(-i\nu/2\).  The last contribution is controlled by the weighted \(L^1\)-norm of \(p\), while the near-diagonal difference is controlled by \(p+\nu p'\) on a fixed interval.
3. **Absolute \(h,q\) series — fail as stated; pass under (H\(_\sigma\)).**  The stated contour permits \(p<1\).  Under (H\(_\sigma\)), (3.9)--(3.10) are absolute and cost only powers of \(\log(2X)\).
4. **Exact active \(j\)-block and floors — fail as stated; pass under (H\(_\sigma\)).**  Equation (3.11) uses \(H_j+1\le2D_jX^{-1/4}\) on the exact active set and retains the final scale.  Negative \(a+b\) produces the polynomial bottom-scale obstruction exhibited above.
5. **Finite family and residual measures — pass for the displayed model.**  The fixed support, \(|\mathfrak T|=O(1)\), all three displayed \(2\pi\)-normalizations, and the outer \(-\pi i\) cost only a constant.
6. **Connector/axis/collision/corner and same-mask one-count control — not testable here.**  The packet explicitly assigns the actual-family mapping to a separate audit.
7. **Radial endpoint and external normalization — partial.**  Composition with the stated radial-BV implication preserves full endpoint coefficients and gives the displayed polylogarithmic integral.  The external-factor-once test is indeterminate because that factor is asserted but not displayed.

No numerical or web control was used.

## 6. Dependencies and exact artifacts used

The derivation from the replacement point used only:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `rounds/codex-managed/m9-m1-beta-double-bounded-explicit-validation/briefs/blind_explicit_amplitude_proof.md`;
4. `rounds/codex-managed/m9-m1-beta-double-bounded-explicit-validation/explicit_amplitude_packet.md`.

The local bounds depend only on the displayed compact support, the stated height-profile seminorms, the smooth-profile seminorms, the exact formulas for \(A,D,g,\mathsf P,\mathsf S\), and the repaired contour condition (H\(_\sigma\)).  The radial conclusion is quoted only in the conditional form stated in the packet.  This report is deliberately marked `contaminated_independent_not_counted_as_strict_gate` and must not be used as the campaign's strict blind-validation artifact.

## 7. Recommended state effect

**Revise; do not promote.**  Add an explicit lower contour condition sufficient for the intended absolute proof, preferably \(a+b\ge0\), and explicitly state the \(x\partial_xM_\tau\) bound (or the exact logarithmic-only \(x\)-dependence).  Supply the external factor with its normalization and one-count placement.  After those corrections, an uncontaminated statement-only rerun can promote the finite-family amplitude estimate, provided the separate line audit also proves that the actual routed operator equals the displayed family.
