# Round 127 conductor adjudication: select the local transverse lift variation gate

Campaign: `full-proof-frontier-inequality-selection-gate`

Starting graph SHA-256:
`fd8831d74d53795182b9f8c234753b33df27e096b9d9f52a6cf43403c87c4a43`

## 1. Decision

The August 21 strategy files correctly identify three qualitatively different
frontiers, but only one report supplies a new inequality that passes the
round's frozen novelty gate.  Round 128 will therefore test the graded
determinant's **local transverse lift square variation**, beginning with the
finite coefficient-level estimate

\[
 \|U_{i,\rho}\|_{V^2(I)}
 \ll_\varepsilon L^{-1}J_B^{1/2}Y^\varepsilon,
 \qquad
 J_B=1+\frac{DQ_B}{B^2}.
 \tag{127.J1}
\]

Only if (127.J1) survives every literal smooth, hard, floor, star, and moving
support piece may the subsequent joint reciprocal-curvature inequality be
tested.  Neither inequality is proved in Round 127.

The selection is based on interface and capacity, not a vote.  Hard TOP has
no actual-coefficient hypothesis at the permitted interface; lower GAR's
available proposal is an explicitly excluded separated positive norm after
an ambient Fourier canonicalization; the graded proposal alone keeps the
moving lift endpoint inside the same reciprocal curvature window and has a
strict, audited payoff.

## 2. Three-frontier adjudication

| Frontier | Literal live target | Present capacity | Proposed mechanism | Decision |
|---|---|---:|---|---|
| hard TOP nonsquare actual direction | \(\|A_L^{\rm ns}\chi_4\|_2^2\ll L^2X^\varepsilon\) | \(L^3X^\varepsilon\) coherent versus \(L^2X^\varepsilon\) diagonal | product-fibre averaging or another noninvertible actual-vector map | ineligible at the current interface: support, phase, and pointwise magnitude allow exact alignment, while product-fibre means retain the coherent direction |
| lower GAR wavelet | exact Round-122 survivor \(\ll RX^\varepsilon\) | \(R^2X^\varepsilon\) linearly; at \(K=y=R^2\), \(y^3\) energy versus \(y^2\) requested | centered \(k\)-square function and reduced-Farey determinant expansion | rejected for this selection: it is a stronger separated \(k\)-norm reached through ambient additive Fourier expansion and asks for the entire missing factor rather than producing one |
| graded determinant at \(W=Y^{7/16}\) | complete signed correlation \(\ll Y^{1/2+\varepsilon}\) | complete \(Y^{37/48+\varepsilon}\); bounded-lift top shell \(Y^{35/48+\varepsilon}\) | local \(V^2\) lift variation kept inside the moving reciprocal window | selected for one finite gate: conditionally gives \(Y^{73/96+\varepsilon}\), a strict \(Y^{1/96}\) complete-block saving |

The graph payoff is deliberately separated from the mathematical fit.  A
proved lower-GAR bound would close the alternative total-M1 analytic parent,
whereas the conditional graded saving closes no M9 parent.  That larger
payoff cannot override the frozen exclusion of separated norms and ambient
spectra.  Hard TOP would close only one of the three M2 parents even after a
full success; its actual endpoint coefficient structure is not present in
the statement-only interface used by the proposed inequality.

## 3. Hard-TOP method obstruction

For finite row supports \(S_m\), unit-modulus \(c_h\), and arbitrary phases
\(\phi_{m,h}\), put

\[
 (T_ac)(m)=\sum_{h\in S_m}a_{m,h}e(\phi_{m,h})c_h,
 \qquad |a_{m,h}|\le1.
\]

Then exactly

\[
 \sup_{|a_{m,h}|\le1}\|T_ac\|_2^2
 =\sum_m|S_m|^2,
 \tag{127.J2}
\]

because the upper bound is rowwise triangle inequality and equality follows
from \(a_{m,h}=\overline{c_h}e(-\phi_{m,h})\).  On a macroscopic hard-cone
rectangle, deleting all \(hm=\square\) entries removes only
\(O(L^{1/2})\) heights per row, so an admissible support-and-magnitude
countermodel still has Hilbert--Schmidt energy \(\asymp L^2\) and selected
energy \(\asymp L^3\).

This is not a lower bound for the literal \(a_{\rm end}\).  It proves that
any successful theorem must use a concrete structural property of that
actual coefficient that fails under the phase twist in (127.J2).

The most natural noninvertible product-shear average also has an exact bad
space.  After absorbing the phase and character, every function
\(F(m,h)=f(mh)\) is fixed by averaging along product fibres; in particular,
the coherent constant direction is fixed and has full row-sum energy.  A
high-pass kills that fibre and must restore it as a remainder of the same
capacity.  Thus product-fibre averaging is a genuine contraction on part of
the input but not on the component carrying the coefficient-blind
obstruction.  This extends the Round-126 filter obstruction without
claiming that the physical nonsquare energy is large.

## 4. Lower-GAR square-function and Farey audit

Let \(S(k)=\mathcal I_k\mathscr V_\delta\) and
\(c_y=\sum_{d\le y}\chi_4(d)/d\).  The actual survivor contains the drift
\(kc_y\).  On a positive block \(K\asymp y\), the exact Round-122 overlap
identity and \(c_y\ge2/3\) give

\[
 \sum_{K<k\le2K}|S(k)|^2\gg y^3.
 \tag{127.J3}
\]

Consequently the uncentered energy estimate is false for the actual
coefficient.  The only valid centering is
\(S^\circ(k)=S(k)-kc_y\).  It is target-equivalent in the scalar wavelet
because the exact full first moment of \(W\) vanishes, with the central and
far truncation errors already target-safe.

The stronger sufficient estimate

\[
 \sum_{k\in\mathcal K(K)}|S^\circ(k)|^2
 \ll_{\varepsilon,\delta}K(R^2+K)X^\varepsilon
 \tag{127.J4}
\]

would close the Round-122 wavelet after Cauchy and the wavelet envelope.
But at \(K=y=R^2\), the coefficient-blind capacity is \(y^3\) and
(127.J4) asks for \(y^2\): it is exactly the full missing factor \(y\),
not an already obtained gain.

The broader centered discrepancy has the exact reduced-Farey expansion

\[
 D_N(k)=
 \sum_{\substack{2\le b\le y\\b\ {m odd}}}
 \frac{\chi_4(b)}{b}
 \left(\sum_{g\le y/b}\frac{\chi_4(g)}g\right)
 \sum_{a\bmod b}^{*}e(aN/b)G_k(a/b).
 \tag{127.J5}
\]

The \(b=1\) term is exactly the removed centre.  Squaring (127.J5)
produces the prescribed-centre determinant phase
\(e(N(ab'-a'b)/(bb'))\); determinant zero is equality of reduced
fractions, and its complete contribution is
\(O(K(y+K)X^\varepsilon)\).  The nonzero determinant estimate remains
entirely open.  Because reaching it uses both an ambient Fourier
canonicalization and a separated positive \(k\)-norm, it is not eligible
under the frozen Round-127 rule.  The exact identity and safe diagonal are
recorded as a scoped self-return, not as progress on the scalar target.

## 5. Graded strict-saving candidate

At

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},
\]

the most optimistic scalar prescribed-centre cell estimate has exponent

\[
 2\min\!\left(a,\frac{1-a}{2}\right)
 +\max\!\left(0,\frac7{16}-a\right)
 =\frac{37}{48}
 \quad\text{at }a=\log_Y(D/L)=\frac13.
 \tag{127.J6}
\]

Thus the scalar-per-cell continuation cannot give a uniform strict saving,
even if its literal transfer is granted for free.

For a reduced-denominator shell \(B=Y^b\), \(1/3\le b\le1/2\), set

\[
 Q_B=\frac{BD}{WL}=Y^{b-5/48},\qquad
 \lambda_B=\frac{YL}{DB^2}=Y^{2/3-2b}.
\]

The curvature factor is uniformly

\[
 \min(Q_B,Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2})
 =Y^{11/48+o(1)}.
\]

Only

\[
 J_B=1+\frac{DQ_B}{B^2}=1+Y^{19/48-b}
 \tag{127.J7}
\]

lift endpoints are born inside that same reciprocal window.  If the
literal coefficient has local variation (127.J1), and if the joint
\(V^2\)-weighted reciprocal-curvature inequality controls the unseparated
sum without an additional \((Q_B/\rho)^{1/2}\), then the complete shell is

\[
 \ll_\varepsilon
 Y^{35/48+\frac12\max(0,19/48-b)+\varepsilon}.
 \tag{127.J8}
\]

The worst shell is \(b=1/3\), where (127.J8) is
\(Y^{73/96+\varepsilon}\), one power \(Y^{1/96}\) below the present
\(Y^{74/96+\varepsilon}\) bound.  The arithmetic is exact, but both
hypotheses are unproved.  Full-shell square variation would replace
\(J_B^{1/2}\) by \((D/B)^{1/2}\) and erase the gain; standard partial
summation plus Cauchy inserts the forbidden reciprocal-window square-root
loss.

## 6. Exact payoff and stop rule

A complete graded correlation exponent \(\beta\) gives persistence

\[
 \Theta(\beta)=
 \max\!\left(\frac{7/16+\beta}{3},\frac\beta2\right).
\]

The conditional \(\beta=73/96\) gives \(115/288>1/3\), so the already
proved \(1/3\) theorem remains stronger.  A pointwise improvement begins
only after \(\beta<9/16\), far beyond the candidate's \(1/96\) saving.
Accordingly Round 128 is not an exponent campaign: it is a finite test of
whether a new actual-family inequality exists.

The stop rule is sequential:

1. audit and prove (127.J1) for each literal coefficient package, with the
   exact moving window, stars, floors, hard faces, support births, and
   cross-shell owner;
2. stop the route if any package costs the full \((D/B)^{1/2}\), a
   \(J_B^\theta\) loss with \(\theta\ge2/3\), or an unpriced variation;
3. only after Gate 1 passes, test the joint reciprocal-curvature inequality;
4. stop if its proof inserts \((Q_B/\rho)^{1/2}\), separates the lift
   transform before the reciprocal sum, or loses a literal owner.

Success at both gates would bank only the complete-block
\(Y^{73/96+\varepsilon}\) estimate.  It would not prove the
\(Y^{1/2}\) graded target, improve the global exponent, close M9-M1 or
M9-M2, prove endpoint uniformity, prove M9, or prove the Gauss circle
conjecture.

## 7. State decision

Promote the two exact method obstructions, the lower centered
square-function/Farey self-return, and the conditional graded connector.
Do not promote either new inequality.  Select only the coefficient-level
local-variation gate for Round 128.  Every analytic parent and every
global exponent remains unchanged.
