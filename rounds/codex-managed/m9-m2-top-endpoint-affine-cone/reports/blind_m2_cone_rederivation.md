## 1. Result

I do not obtain (74.2) in the full intermediate range.  I obtain three
rigorous packet-level conclusions.

First, for every fixed \(A>0\), the target holds in the strict unbounded
subrange
\[
 1\leq L\leq \min\{H,(\log(2+X))^A\}:
 \qquad
 \mathcal T_L^{\rm end}\ll_{A,\varepsilon}L^{3/2}X^\varepsilon.
 \tag{R74.1}
\]
This is an epsilon-trivial extension of the bounded-\(L\) slice, not a
polynomial-range advance.

Second, after exact row Cauchy, every diagonal term, every fixed-width
near-diagonal, and every correlation touching either moving endpoint is
already target-safe by absolute values.  Thus, for any fixed integer
\(K_0\geq1\), (74.2) follows from the strictly smaller, actual-symbol,
one-sided core estimate displayed in (R74.12) below.

Third, four tempting coefficient-blind routes do not close the remaining
range: swap-cancellation after the shear is destroyed by the actual domain
and symbol; product grouping followed only by a divisor bound has a false
arbitrary-coefficient analogue; absolute estimation of the row
off-diagonal is one power of \(L\) too large; and a one-variable stationary
transform returns exactly to the reciprocal-denominator phase, with an
absolute alias sum worse than the original trivial row bound.  Large real
curvature by itself is also defeated by exact perfect-fourth-power/square
resonances.  These are route-specific no-go results, not a disproof of
(74.2).

## 2. Exact statement and hypotheses

Let \(X\) be sufficiently large and retain exactly
\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor.
\]
Let \(L\) be dyadic, \(1\leq L\leq H\), and use precisely the fixed
cutoffs and symbol (74.1).  The only quantitative cutoff fact used in
(R74.1) and in the safe-piece estimates is the uniform boundedness that
comes with the fixed normalized smooth cutoffs:
\[
 \sup_L\|\eta_L\|_\infty+\|\Phi\|_\infty+\|W\|_\infty<\infty.
 \tag{R74.2}
\]
No derivative-gap, symmetry, multiplicativity, or replacement \(q_X=1\)
is assumed.

For a fixed \(A>0\), (R74.1) holds uniformly for all such dyadic \(L\)
with \(L\leq(\log(2+X))^A\).  Its implicit constant may depend on
\(A,\varepsilon\) and the three fixed cutoffs, but not on \(X,H,L\).
The terminal slice \(L\asymp H\) is the inherited closed slice stated in
the packet; it is not reproved here.  The unresolved range after this
report is, in particular, polynomially growing intermediate \(L\) away
from that terminal slice.

## 3. Proof or derivation

Write
\[
 \mathcal H_L=\{h\geq1:h\ \text{odd and }\eta_L(h)\ne0\},
 \qquad b_h=\lceil h/4\rceil,
 \qquad I_h=\{b_h,b_h+1,\ldots,h\}.
\]
On this support, \(h\asymp L\), \(m\asymp L\), and hence (R74.2) and
(74.1) give
\[
 |a_{L,H,X}(h,m)|\ll1.                                      \tag{R74.3}
\]

The exact shear is \(r=4m-h\).  It is a bijection from \(m\in I_h\) to
the odd integers satisfying
\[
 1\leq r\leq3h,\qquad r\equiv-h\pmod4,
 \qquad m=(h+r)/4.
\]
At the first lattice point, \(r=3\) if \(h\equiv1\pmod4\) and \(r=1\)
if \(h\equiv3\pmod4\); thus the ceiling has not been replaced by a
continuous edge.  Define the exact sheared symbol
\[
 \widetilde a(h,r)=
 \eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 \left(\frac{4L^2}{h(h+r)}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xh}{h+r}}\right).                  \tag{R74.4}
\]
For odd \(h,r\),
\[
 \mathbf1_{r\equiv-h(4)}=\frac{1-\chi_4(h)\chi_4(r)}2,
 \qquad
 \chi_4(h)\mathbf1_{r\equiv-h(4)}
   =\frac{\chi_4(h)-\chi_4(r)}2.
\]
Consequently the exact shear identity is
\[
 \mathcal T_L^{\rm end}
 =\frac12\sum_{h\in\mathcal H_L}
   \sum_{\substack{1\leq r\leq3h\\r\ \mathrm{odd}}}
  \{\chi_4(h)-\chi_4(r)\}\widetilde a(h,r)
  e\!\left(\frac{\sqrt X}{2}\sqrt{h(h+r)}\right).         \tag{R74.5}
\]
Both character terms are present.  The phase is symmetric under swapping
\(h,r\), but the summation set, \(\eta_L(h)\), \(\Phi(h/(H+1))\), and
\(W(\sqrt{q_Xh/(h+r)})\) are not.  Hence (R74.5) has no exact
antisymmetric pair cancellation.  For fixed \(r\), direct differentiation
gives
\[
 F_r''(h)=-\frac{\sqrt X\,r^2}
 {8\{h(h+r)\}^{3/2}}.                                     \tag{R74.6}
\]
In particular the curvature scale is nonuniform from \(r=O(1)\) to
\(r\asymp h\).

The exact product ledger follows by setting \(n=hm\):
\[
 \mathcal T_L^{\rm end}=\sum_{n\asymp L^2}A_L(n)e(\sqrt{Xn}),              \tag{R74.7}
\]
where
\[
 A_L(n)=\sum_{\substack{h\mid n,\ h\asymp L,\ h\ \mathrm{odd}\\
                         b_h\leq n/h\leq h}}
 \chi_4(h)a_{L,H,X}(h,n/h).                               \tag{R74.8}
\]
Every admissible pair occurs once, through its divisor \(h\).  Conversely,
only divisors satisfying the moving near-square window occur.  Thus the
multiplicity is truncated-divisor multiplicity; (R74.8) is neither the
full \(r_2(n)/4\) coefficient nor a multiplicative coefficient.

For the exact diagonal ledger, put
\(z_{h,m}=a_{L,H,X}(h,m)e(\sqrt{Xhm})\).  Cauchy only in the original
\(h\)-variable gives
\[
 |\mathcal T_L^{\rm end}|^2
 \leq |\mathcal H_L|\sum_{h\in\mathcal H_L}
       \left|\sum_{m\in I_h}z_{h,m}\right|^2
 =O(L)\{D+\mathcal C_{\ne}\},                             \tag{R74.9}
\]
with the exact real quantities
\[
 D=\sum_{h\in\mathcal H_L}\sum_{m\in I_h}|a(h,m)|^2\ll L^2,
\]
and
\[
 \mathcal C_{\ne}
 =2\Re\sum_{h\in\mathcal H_L}
       \sum_{k=1}^{h-b_h}\sum_{m=b_h}^{h-k}
 a(h,m)\overline{a(h,m+k)}
 e\!\left(\sqrt{Xh}\{\sqrt m-\sqrt{m+k}\}\right).       \tag{R74.10}
\]
Thus only the one-sided upper estimate
\(\mathcal C_{\ne}\leq C_\varepsilon L^2X^\varepsilon\) is
sufficient; an absolute-value estimate for \(\mathcal C_{\ne}\) is
stronger than needed, and this sufficient condition is not necessary for
a different proof retaining \(\chi_4(h)\).

Here is the promised smaller correlation.  Fix \(K_0\geq1\).  In
(R74.10), all \(k\leq K_0\) contribute \(O_{K_0}(L^2)\) absolutely.
For \(k>K_0\), all terms with \(m=b_h\) or \(m+k=h\) together contribute
\(O(L^2)\) absolutely.  Therefore
\[
 \mathcal C_{\ne}=\mathcal C_{\rm core}+O_{K_0}(L^2),       \tag{R74.11}
\]
where, with empty inner ranges understood,
\[
 \mathcal C_{\rm core}:=
 2\Re\sum_{h\in\mathcal H_L}
 \sum_{k=K_0+1}^{h-b_h}
 \sum_{m=b_h+1}^{h-k-1}
 a(h,m)\overline{a(h,m+k)}
 e\!\left(\sqrt{Xh}\{\sqrt m-\sqrt{m+k}\}\right).       \tag{R74.12}
\]
Hence the weakest sufficient estimate furnished by this particular
Cauchy ledger is the signed, one-sided bound
\[
 \mathcal C_{\rm core}\leq C_\varepsilon L^2X^\varepsilon.\tag{R74.13}
\]
The diagonal, a fixed-width near-diagonal, the full hard endpoint, the
flat upper endpoint, and their moving-boundary correlations have all been
removed without smoothing or changing the actual symbol.

The logarithmic subrange now follows directly, without (R74.13).  There
are \(O(L^2)\) admissible pairs and (R74.3) holds, so
\[
 |\mathcal T_L^{\rm end}|\ll L^2
 =L^{3/2}L^{1/2}
 \leq L^{3/2}(\log(2+X))^{A/2}
 \ll_{A,\varepsilon}L^{3/2}X^\varepsilon.
\]

Finally, the exact one-variable stationary self-return can be seen without
using it as an estimate.  For fixed \(h\), let
\(f_h(m)=\sqrt{Xhm}\).  A Poisson alias \(k\) is stationary at
\[
 f_h'(m)=k,\qquad m_k=\frac{Xh}{4k^2},\qquad
 f_h(m_k)-km_k=\frac{Xh}{4k}.                              \tag{R74.14}
\]
As \(h/4\leq m\leq h\), the aliases satisfy
\(\sqrt X/2\leq k\leq\sqrt X\), and the actual profile returns as
\[
 W\!\left(\sqrt{\frac{q_Xh}{4m_k}}\right)=W(k/y).          \tag{R74.15}
\]
Thus the stationary phase is exactly the reciprocal-denominator phase in
(74.3), not a new phase.  Moreover
\[
 |f_h''(m_k)|^{-1/2}=\left(\frac{Xh}{2k^3}\right)^{1/2}
 \asymp \frac{L^{1/2}}{X^{1/4}}.
\]
There are \(\asymp\sqrt X\) aliases, so their absolute sum is
\(\asymp X^{1/4}L^{1/2}\) per row, worse than the trivial \(O(L)\) row
bound throughout \(L\leq X^{1/4}\).  A stationary transform plus absolute
alias summation therefore cannot close (74.2); an additional signed alias
estimate would be needed.

## 4. First doubtful or unproved step

There is no doubtful step in the logarithmic-range estimate or in the
exact identities (R74.5), (R74.7), (R74.10), and (R74.14).  The first
unproved step toward the full intermediate range is (R74.13), or some
different signed estimate that retains \(\chi_4(h)\).  The packet supplies
no derivative gap modulo one, no symmetry of the actual sheared symbol,
and no arithmetic estimate for the moving truncated coefficient
\(A_L(n)\).  Consequently none of the displayed reductions by itself
provides the required factor \(L^{1/2}\) saving over the \(O(L^2)\)
direct bound when \(L\) grows like a fixed power of \(X\).

In particular, (R74.13) must not be silently strengthened to an
arbitrary-coefficient or absolute correlation estimate, and it must not
be called necessary: the original character has already disappeared in
(R74.9).

## 5. Required control test and outcome

1. **External normalization and conjugate.**  The positive block is
   exactly
   \[
   B_L^+=-\frac{2e(1/8)}\pi X^{1/4}L^{-3/2}\mathcal T_L^{\rm end}.
   \]
   The negative block is \(\overline{B_L^+}\), so the full block is
   \(2\Re B_L^+\) and
   \(|B_L^++\overline{B_L^+}|\leq(4/\pi)X^{1/4}L^{-3/2}|\mathcal T_L^{\rm end}|\).
   The factor in (74.4) is used once; conjugation contributes only the
   displayed factor two.

2. **Parity and character.**  Every formula restricts \(h\) to odd
   integers and keeps \(\chi_4(h)\).  Extending to all \(h\) would add
   zero at even frequencies, not new terms.  Cauchy deliberately loses
   the character and is identified only as a sufficient route.

3. **Hard lower edge.**  The lower point is always
   \(b_h=\lceil h/4\rceil\).  Its sheared value is \(r=3\) for
   \(h\equiv1(4)\) and \(r=1\) for \(h\equiv3(4)\).  Its coefficient is
   the full value from (R74.4), including
   \(W(\sqrt{q_Xh/(h+r)})\); it is never deleted or replaced by a
   full-line Poisson endpoint.

4. **Flat upper edge and actual \(q_X\).**  At \(m=h\), one has
   \(r=3h\) and the exact profile is \(W(\sqrt{q_X}/2)\).  I never set
   \(q_X=1\).  If \(X=K^4\), then \(q_X=1\) and this particular edge
   vanishes because \(W(1/2)=0\); for general \(X\), its actual value is
   retained.  The endpoint correlations are safe by their count, not by
   assuming this value vanishes.

5. **All \(L\)-slices.**  (R74.1) covers a genuinely unbounded but
   subpolynomial slice and includes bounded \(L\).  The packet supplies
   the independent inherited result for \(L\asymp H\).  No claim is made
   for the remaining polynomial intermediate range.

6. **Product multiplicity.**  Equations (R74.7)--(R74.8) retain exactly
   one contribution for each admissible divisor \(h\), with the moving
   inequalities \(b_h\leq n/h\leq h\).  No replacement by a full divisor
   function, \(r_2/4\), or a multiplicative coefficient is made.

7. **Shear projector and ownership.**  Equation (R74.5) keeps both
   \(\chi_4(h)\) and \(-\chi_4(r)\), the triangular condition
   \(r\leq3h\), and all cutoffs on their original \(h\)-variable.  A
   swap would move those cutoffs and change the \(W\)-argument, so the
   antisymmetric numerator alone gives no cancellation.

8. **Square and perfect-fourth-power resonance.**  Take \(X=K^4\).
   If \(hm=s^2\), then
   \(e(\sqrt{Xhm})=e(K^2s)=1\).  Equivalently,
   \(h(h+r)=4s^2\) and the phase in (R74.5) is also one.  More explicitly,
   \(h=da^2,m=db^2\) gives such points throughout the cone when the ratio
   condition holds.  The character and actual weights remain, so this is
   not a lower bound for the whole sum; it is a conclusive test that
   nonzero or large real curvature alone is not cancellation modulo one.
   The logarithmic proof is insensitive to these resonances.

9. **Diagonal, near-diagonal, hard-edge, and moving boundaries.**  The
   diagonal is \(D\ll L^2\).  Each fixed \(k\) in (R74.10) is
   \(O(L^2)\) absolutely.  All pairs touching \(b_h\) or \(h\), even
   with all remaining \(k\), total \(O(L^2)\).  Formula (R74.12) keeps
   the exact moving integer boundary in the residual core; no rectangular
   extension is made.

10. **Aliases, errors, and self-return.**  Equations (R74.14)--(R74.15)
    expose every stationary alias and the exact self-return phase.  Their
    absolute power count does not save.  No transform is used in the
    proof of (R74.1), so no new transform error or endpoint term is
    introduced.  The errors already declared target-safe with (74.3) are
    neither reused as main terms nor counted twice.

11. **False coefficient-blind analogue.**  Product grouping plus only
    \(|A(n)|\ll d(n)\) cannot suffice: on an interval \(n\asymp L^2\),
    the admissible artificial coefficients
    \(A^*(n)=e(-\sqrt{Xn})\) give a sum \(\asymp L^2\).  Likewise,
    artificial row coefficients \(a^*(h,m)=\chi_4(h)e(-\sqrt{Xhm})\)
    make every term of the original character-weighted sum positive.
    For \(L=X^\delta\) and \(0<\varepsilon<\delta/2\), this exceeds
    \(L^{3/2}X^\varepsilon\).  Hence an unsigned/arbitrary-coefficient
    theorem of the required polynomial-range strength is false.  The
    actual symbol and its signed structure are indispensable.

12. **Separation.**  Every estimate here concerns only
    \(\mathcal T_L^{\rm end}\).  No cancellation with (M1), no
    smooth-interior packet, no (M9) input, and no global-exponent claim is
    used.

## 6. Dependencies and exact artifacts used, including an isolation ledger

The derivation used exactly the two permitted artifacts:

| Artifact | Use |
|---|---|
| `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/briefs/blind_m2_cone_rederivation.md` | Task scope, output contract, and mandatory controls. |
| `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/derivation_packet.md` | Definitions (74.1)--(74.13), inherited slice, and stopping rule. |

Isolation ledger: I did not read the proof graph, proof draft, prior or
sibling reports, source cards, synthesis files, web literature, or any
other repository file.  I used no web source and no numerical or symbolic
computation.  The algebra, power counts, resonance test, and self-return
calculation in this report were derived directly from the packet.

## 7. Recommended state effect

**Retain.**  Retain (R74.1) as an epsilon-trivial strict unbounded
subrange, retain (R74.11)--(R74.13) as an exact smaller actual-symbol
correlation reduction, and retain the shear/product/curvature/self-return
no-go conclusions as route exclusions.  Do not promote
`M9-M2-top-endpoint-signed-cone`: the polynomial intermediate range still
requires a new signed estimate.
