# Round 103 synthesis: singleton \(q=1\) actual diagonal

Campaign: `m9-m2-q1-actual-diagonal-energy`

Starting graph SHA-256:
`902eb43bc0fc72b1c3e080dac5cd89757d17e2eaa1f72d606b89afbecff92935`

Resulting graph SHA-256 after the validated State Patch:
`d2502a33224fbcb1fe3b8ffe0ea1227b953112fa0c98216597e8b0ccfa887372`

## Frozen objective

The round asked whether the complete residual singleton row satisfies

\[
 \sum_{a\asymp A}|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon {L^4\over A},
\]

with every primitive and prior-owner mask, moving reciprocal endpoint,
finite odd lift, actual profile, floor, star, collar, orientation, metric
density and discrepancy mode retained.

## Exact singleton geometry

For \(b=a+2\), put

\[
 \delta_a=\sqrt{a+2}-\sqrt a,
 \qquad \Lambda_a={X\delta_a^2\over2},
\]

\[
 I_a=\left({J\delta_a\over2\sqrt a},
            {J\delta_a\over\sqrt{a+2}}\right),
 \qquad K\asymp {J\over A},\qquad G\asymp {L\over A}.
\]

The interval is open. Its two endpoints are exactly saddle exit and
entry. Empty and singleton reciprocal fibres are handled by zero
extension. The exact carrier identity is

\[
 \mathfrak C^\circ_{a,k}(g)
 =e\!\left(-{g\Lambda_a\over2k}\right)
  \mathfrak B^\circ_{a,k}(g).
\]

## Complete sampled-\(k\) variation

After \(u=y^2\), the centered coefficient is the complete quadratic
integral

\[
 \mathfrak B^\circ_{a,k}(g)
 =\int q_{a,g}(y)
   e\!\left(gk\left(y-{J\delta_a\over2k}\right)^2\right)dy.
\]

The actual profile \(q_{a,g}\) is independent of \(k\). Both fixed
physical collars are retained, and their resolution parameter is

\[
 {J\over AL}\ge1.
\]

The uniform complete-Fresnel argument therefore gives, for the literal
actual multiplier,

\[
 \sup_k|B_{a,g}(k)|+\operatorname {Var}_k B_{a,g}(k)
 \ll_\varepsilon X^\varepsilon\sqrt{AL\over J}.
\]

This is the new actual-symbol input. It is not valid for arbitrary
phase-conjugated coefficients.

## Fourier and curvature closure

Expanding the complete punctured metric window produces the total phase

\[
 f_{\nu,g}(k)=\left(\nu-{g\over2}\right){\Lambda_a\over k}.
\]

Every lift \(g\) is odd, so \(n=|2\nu-g|\ge1\), including the density
mode \(\nu=0\). Moreover,

\[
 |f_{\nu,g}''(k)|\asymp {nA^2\over J}.
\]

Weighted van der Corput and the two exact Fourier moments give

\[
 \sum_k B_{a,g}(k)e(f_{\nu,g}(k))
 \ll_\varepsilon X^\varepsilon
 \left(\sqrt{ALn}+\sqrt{L/A}\,n^{-1/2}\right),
\]

\[
 \sum_\nu|\widehat W_R(\nu)|\,|2\nu-g|^{1/2}\ll\sqrt G,
 \qquad
 \sum_\nu|\widehat W_R(\nu)|\,|2\nu-g|^{-1/2}
 \ll G^{-1/2}.
\]

Thus one odd lift costs \(O_\varepsilon(X^\varepsilon(L+1))\), one
row satisfies

\[
 |F_a(1)|\ll_\varepsilon X^\varepsilon {L^2\over A},
\]

and summing the \(O(A)\) bases proves

\[
 \boxed{\sum_{a\asymp A}|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon {L^4\over A}.}
\]

## Owner and hostile controls

The accepted owner formula puts the actual profiles, floors, stars,
finite lift support, both physical collars and all saddle transitions
inside the complete integral. The remaining external multiplier has
fixed dyadic bounded variation. For \(q=1\), primitivity is automatic,
the square-ray exclusion is empty, the \(\rho\)-safe owner is blockwise
constant, exact centers vanish because the window is punctured, and the
orientation ledger has finitely many conjugate copies.

Pell \((25,27)\), general near-square, perfect-fourth, strict-metric,
empty-fibre, singleton-fibre, endpoint, density, arbitrary-coefficient
and unsigned controls all pass. Round 80 is not contradicted: its no-go
concerned a formal half-frequency inference from lift variation alone,
whereas this round proves complete actual sampled-\(k\) variation and
then estimates the retained density mode.

## Conductor decision

Promote `M9-M2-primitive-ray-q1-actual-diagonal-energy` to
`proved_internal`. The singleton is now a discharged dependency of the
longer fixed-\(a\) Gram and canonical density-discrepancy energy.

Retain open:

- the complete longer-row mode-resolved fixed-\(a\) Gram;
- the canonical M2 density-discrepancy energy and hard signed cone;
- the two smooth M2 packets and endpoint assembly;
- M9-M2, M9-M1, M9, endpoint uniformity and the quarter target.

The result makes no change to the best global exponent. The strongest
certified external exponent remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots,
\]

and the strongest internal uniform exponent remains \(1/3\).

## Evidence and next interface

The decision uses the statement-only rederivation, constructive proof,
hostile/source audit, conductor normalization review, owner/control
review and State Patch dry-run. The next non-core deliverable is to test
whether the same complete sampled-\(k\) lemma is uniform for fixed or
subpolynomial \(q\), and to identify the first genuinely polynomial
signed \(q\)-correlation that survives.
