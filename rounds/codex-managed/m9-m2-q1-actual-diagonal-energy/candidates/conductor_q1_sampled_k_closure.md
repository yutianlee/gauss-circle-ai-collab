# Conductor candidate: sampled-\(k\) closure of the singleton \(q=1\) diagonal

Campaign: `m9-m2-q1-actual-diagonal-energy`

Starting graph SHA-256:
`902eb43bc0fc72b1c3e080dac5cd89757d17e2eaa1f72d606b89afbecff92935`

## 1. Exact claim

On every residual hard-top M2 half-open block whose fixed-\(a\) row
contains only \(q=1\), the literal actual coefficient satisfies

\[
 \boxed{
 \sum_{a\asymp A}|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon {L^4\over A}.}
 \tag{103.C1}
\]

This closes only the disjoint singleton input to the fixed-\(a\) Gram.
It does not estimate a nonzero \(q\)-shift or a longer row.

Put

\[
 b=a+2,\qquad \delta_a=\sqrt{a+2}-\sqrt a,
 \qquad \Lambda_a={X\delta_a^2\over2},
\]

\[
 I_a=\left({J\delta_a\over2\sqrt a},
            {J\delta_a\over\sqrt{a+2}}\right),
 \qquad K\asymp {J\over A},\qquad G\asymp {L\over A}.
 \tag{103.C2}
\]

The interval in (103.C2) is open. Empty and singleton reciprocal or
lift fibres are retained by zero extension.

## 2. Complete centered integral and literal owners

The exact physical integral is

\[
 \mathfrak C^\circ_{a,k}(g)
 =g\int_{(a+2)/4}^{a}A^\circ_{ga,g(a+2)}(gu)
 e\!\left(g[ku-J\delta_a\sqrt u]\right)\,du.
\]

Completing the square gives the exact carrier identity

\[
 \mathfrak C^\circ_{a,k}(g)
 =e\!\left(-{g\Lambda_a\over2k}\right)
  \mathfrak B^\circ_{a,k}(g),
 \tag{103.C3}
\]

where \(\mathfrak B^\circ\) is the complete centered integral. It
contains both fixed physical collars, every incomplete-Fresnel entry and
exit, the actual \(\Phi,q_X,W\) profiles, floors, stars, and the finite
odd-lift support.

The accepted Round-80 normal form makes the remaining \(k\)-multiplier
literal. It consists only of fixed smooth dyadic cutoffs of bounded
variation and the two jumps of the open reciprocal interval. On \(q=1\):

- primitivity is automatic;
- \(a(a+2)\) is not a square;
- the \(\rho\)-safe owner is constant on the frozen residual block;
- exact centers are killed by \(W_R(0)=0\);
- the Round-77 collar error is already disjoint;
- the two orientations are finitely many conjugate copies.

Thus there is no hidden jagged \(k\)-mask.

## 3. Complete-Fresnel sampled \(k\)-variation

Set \(u=y^2\),

\[
 r_k={J\delta_a\over2k},\qquad \lambda=gk,qquad
 q_{a,g}(y)=2gyA^\circ_{ga,g(a+2)}(gy^2).
\]

Then

\[
 \mathfrak B^\circ_{a,k}(g)
 =\int_{\sqrt{a+2}/2}^{\sqrt a}
 q_{a,g}(y)e\!\left(\lambda(y-r_k)^2\right)\,dy.
 \tag{103.C4}
\]

The profile \(q_{a,g}\) is independent of \(k\). Its height and total
variation are \(O_\varepsilon(X^\varepsilon g\sqrt A)\). A fixed
physical collar has \(y\)-width \(w_g\asymp(g\sqrt A)^{-1}\), and

\[
 \lambda w_g^2\asymp {K\over gA}\asymp {J\over AL}\ge1
 \tag{103.C5}
\]

on every nonempty block, because \(A\le L\le J^{1/2}\). Moreover,
as \(k\) crosses its exact open interval, \(r_k\) traverses the full
centered support monotonically once.

The exact Morse-coordinate argument, with the two collars retained,
therefore gives

\[
 \sup_k|B_{a,g}(k)|+\operatorname {Var}_k B_{a,g}(k)
 \ll_\varepsilon X^\varepsilon V,
 \qquad V=\sqrt{AL\over J},
 \tag{103.C6}
\]

where \(B_{a,g}\) includes the literal bounded-variation \(k\)-cutoff.
No leading stationary term or stationary remainder is introduced.

## 4. Metric Fourier modes and reciprocal curvature

For one punctured metric member,

\[
 W_R(t)=\sum_{\nu\in\mathbb Z}\widehat W_R(\nu)e(\nu t),
 \qquad
 |\widehat W_R(\nu)|\ll_N R^{-1}(1+|\nu|/R)^{-N},
 \qquad 1\le R\le G.
\]

Combining this series with (103.C3), the total phase is

\[
 f_{\nu,g}(k)=\left(\nu-{g\over2}\right){\Lambda_a\over k}.
\]

Since every lift \(g\) is odd,

\[
 n:=|2\nu-g|\ge1,
 \qquad |f_{\nu,g}''(k)|\asymp {nA^2\over J}.
\]

The second-derivative estimate and partial summation with (103.C6) give

\[
 \left|\sum_{k\in I_a\cap\mathbb Z}
 B_{a,g}(k)e(f_{\nu,g}(k))\right|
 \ll_\varepsilon X^\varepsilon
 \left(\sqrt{ALn}+\sqrt{L/A}\,n^{-1/2}\right).
 \tag{103.C7}
\]

The complete Fourier moments are

\[
 \sum_\nu|\widehat W_R(\nu)|\,|2\nu-g|^{1/2}\ll\sqrt G,
 \qquad
 \sum_\nu|\widehat W_R(\nu)|\,|2\nu-g|^{-1/2}
 \ll G^{-1/2}.
 \tag{103.C8}
\]

They include the density mode \(\nu=0\), the indices nearest \(g/2\),
and the remote Fourier tail.

## 5. Row and energy bounds

Equations (103.C7)--(103.C8) cost \(O_\varepsilon(X^\varepsilon(L+1))\)
for each fixed odd lift. Since there are \(O(G)=O(L/A)\) actual lifts,

\[
 |F_a(1)|\ll_\varepsilon X^\varepsilon {L^2\over A}.
 \tag{103.C9}
\]

There are \(O(A)\) active bases, so (103.C9) proves (103.C1).
Logarithmically many metric members and finitely many orientations are
absorbed into \(X^\varepsilon\).

The result is compatible with Round 80. Round 80 rejected a formal
half-frequency inference based only on lift variation. Here the new
input is the complete actual sampled-\(k\) variation (103.C6). The
metric mean is not deleted: \(\nu=0\) has \(n=g\) and is estimated by
the same reciprocal-curvature argument.

## 6. Controls and scope

- The Pell ray \((25,27)\), fourth-power recurrence, and strict metric
  annuli obey the same uniform upper bound.
- An arbitrary phase-conjugated \(k\)-coefficient can destroy
  (103.C6); the theorem is actual-symbol only.
- Taking absolute values before the reciprocal phase loses (103.C7),
  so no unsigned analogue is proved.
- Exact centers, endpoints, stars, empty fibres, singleton fibres, and
  both orientations are retained exactly once.
- No actual lower obstruction is asserted.
- The longer fixed-\(a\) Gram and the complete mode-resolved determinant
  tube remain open.

## 7. Proposed state effect

Promote `M9-M2-primitive-ray-q1-actual-diagonal-energy` to
`proved_internal`, with (103.C1) as its statement. Remove it as an open
dependency of the longer fixed-\(a\) Gram and canonical
density-discrepancy energy, while retaining those parent obligations as
open. Record the complete sampled-\(k\) mechanism and its arbitrary-
coefficient false shadow. Do not change M9-M2, M9-M1, M9, endpoint
uniformity, the quarter target, or any exponent.
