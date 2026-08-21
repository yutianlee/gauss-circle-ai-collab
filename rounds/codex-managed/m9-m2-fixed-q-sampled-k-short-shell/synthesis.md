# Round 104 synthesis: uniform fixed-\(q\) rows and short shells

Campaign: m9-m2-fixed-q-sampled-k-short-shell

Starting graph SHA-256:
d2502a33224fbcb1fe3b8ffe0ea1227b953112fa0c98216597e8b0ccfa887372

Resulting graph SHA-256 after the validated State Patch:
f8f20833d2f24fa0b323488e247887ba943b8dffdd3eacb58e5bae773eb5831b

## Frozen objective

The round asked whether the proved singleton sampled-\(k\) mechanism is
uniform on literal rows

\[
 b=a+2q,\qquad a\asymp b\asymp A,\qquad q\asymp D,
\]

and, if so, exactly how much of the complete fixed-\(a\) Gram follows
without a signed correlation between distinct \(q\)-rows.

## Uniform actual row theorem

Put

\[
 \delta_q=\sqrt{a+2q}-\sqrt a,\qquad
 \Lambda_q={X\delta_q^2\over2}.
\]

The exact open reciprocal interval is

\[
 I_{a,q}=\left({J\delta_q\over2\sqrt a},
               {J\delta_q\over\sqrt{a+2q}}\right),
\]

with

\[
 K\asymp {JD\over A},\qquad G\asymp {L\over A}.
\]

After \(u=y^2\), the literal complete centered integral is

\[
 \mathfrak B^\circ_{a,q,k}(g)
 =\int Q_{a,q,g}(y)
 e\!\left(gk\left(y-{J\delta_q\over2k}\right)^2\right)dy.
\]

The exact identity

\[
 k\partial_k e\!\left(gk(y-r_k)^2\right)
 ={y+r_k\over2}\partial_y e\!\left(gk(y-r_k)^2\right)
\]

converts saddle motion into a physical derivative. With the actual
homogeneous profile, both fixed physical collars, and the literal
bounded-variation owners retained, it gives

\[
 \sup_k|B_{a,q,g}(k)|+\operatorname{Var}_kB_{a,q,g}(k)
 \ll_\varepsilon X^\varepsilon\sqrt{AL\over JD}.
\]

Writing \(s=\sqrt{b/a}\), the reciprocal interval length is

\[
 {J(s-1)(2-s)\over2s}.
\]

It may collapse as \(s\to2\), but the saddle path collapses with it.
The proof uses no lower bound for the interval length and no inverse
power of \(2-s\). Empty and singleton fibres are handled by zero
extension and the supremum estimate.

## Metric modes and row closure

Opening the complete punctured metric window gives

\[
 f_{\nu,g}(k)=\left(\nu-{g\over2}\right){\Lambda_q\over k},
 \qquad n=|2\nu-g|\ge1,
\]

and the conjugate orientation gives \(n=|2\nu+g|\ge1\). The density
mode \(\nu=0\) is retained. Exact differentiation yields

\[
 |f_{\nu,g}''(k)|\asymp {nA^2\over JD}.
\]

Weighted second-derivative estimation therefore gives

\[
 \sum_kB_{a,q,g}(k)e(f_{\nu,g}(k))
 \ll_\varepsilon X^\varepsilon
 \left(\sqrt{ALn}+\sqrt{L/A}\,n^{-1/2}\right).
\]

The two complete Fourier half-moments are \(O(\sqrt G)\) and
\(O(G^{-1/2})\). Thus one lift costs \(O(L+1)\), and summing the
literal \(O(G)\) odd lifts proves

\[
 \boxed{|F_a(q)|\ll_\varepsilon X^\varepsilon {L^2\over A}}.
\]

The theorem is specific to the actual coefficient. Arbitrary
phase-conjugated or unsigned multipliers are excluded.

## Owner and carrier controls

Primitivity, square-ray ownership, the positive-safe owner, and dyadic
ownership are rowwise constant. Exact metric centers are already zeros
of the punctured window. The metric annulus is opened as its complete
Fourier series. Profiles, floors, stars, orientations, finite lifts,
physical collars, entry/exit, and zero extension remain literal. No
jagged exterior \(k\)-mask survives.

The blind carrier-cancellation identity is also exact: expanding the
centered integral back into an uncentered physical Fourier coefficient
moves the reciprocal carrier inside that coefficient. It does not
invalidate the proof, because the new actual sampled-\(k\) variation is
precisely the dephasing theorem needed before applying reciprocal
curvature. Direct periodized Parseval is a valid but weaker estimate.

## Exact Gram ceiling

Summing the \(O(AD)\) rows gives

\[
 \sum_{a\asymp A}\sum_{q\asymp D}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon {DL^4\over A}.
\]

For \(1\le H\le D\), rowwise Cauchy and zero extension give

\[
 \mathcal G_H^{\rm act}
 \ll_\varepsilon X^\varepsilon {H^2DL^4\over A}.
\]

The canonical target is

\[
 X^\varepsilon{H^2E_0\over\rho}
 \asymp X^\varepsilon{H^2L^4\over AD}.
\]

The exact route deficit is \(D^2\). Consequently the target is proved
for every prescribed fixed polylogarithmic range
\(D\le(\log(2+X))^C\), after epsilon splitting, but no fixed
positive-power shell follows.

This is a ceiling of the pointwise-row plus Cauchy route, not an actual
lower obstruction. The polynomial shell can still close through signed
cross-\(q\) cancellation.

## Conductor decision

Promote a narrow internal lemma for the uniform actual fixed-\(q\) row
and its prescribed polylogarithmic shell consequence.

Retain open:

- the complete polynomial-shell signed \(q\)-correlation;
- the full fixed-\(a\) actual Gram;
- the canonical hard density-discrepancy energy and signed cone;
- the two smooth M2 packets;
- M9-M2, M9-M1, endpoint uniformity, M9, and the quarter target.

No primary-source dependency is imported. No global exponent changes.
The certified external exponent remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots,
\]

and the strongest internal uniform exponent remains \(1/3\).

## Next interface

The strict survivor is the complete polynomial-shell correlation

\[
 \sum_{1\le s<H}(H-s)(-1)^s
 \sum_{a,q}F_a(q+s)\overline{F_a(q)}.
\]

A successful next core must keep both moving reciprocal fibres, both
lift sets, primitive and owner masks, the density and every discrepancy
mode, and all entry/exit transitions coupled. Rowwise absolute values,
coefficient-blind determinant counts, and another Cauchy step cannot
recover the missing \(D^2\).
