# Conductor candidate: a BV-threshold lemma for local lift variation

Campaign: `gc-w7-16-local-transverse-lift-variation-gate`

Starting graph SHA-256:
`1a5c8c8b4b6c6c0dcf3d0e05a1607b3d29dfe22f66748d401405d1c0f7b474d6`

## 1. Result

A general discrete BV-threshold lemma proves the desired local
\(J_B^{1/2}/L\) square variation for every coefficient that has the exact
separable lift form accepted in Round 95:

\[
 \frac{1}{a}
 \sum_g\frac{\chi_4(g)}g P_a(g)\,w_D(gb),
 \tag{128.C1}
\]

with uniformly sampled-BV frequency factor \(P_a\) and denominator
profile \(w_D\).  The proof uses the common lift character before any
modulus and represents an arbitrary discrete-BV denominator profile as a
superposition of moving threshold indicators.

The remaining conductor seam is literal rather than analytic: verify that
every M1/M2 floor, prefix, hard, star, support, and moving-symbol package in
the selected determinant cell is contained in the Round-95 separable
formula, or is a bounded-BV multiplier in the same \(b'\)-window.  If so,
the coefficient gate passes.  A genuinely coupled support not represented
by those forms is the first possible residual.

## 2. Exact abstract statement

Let \(\chi=\chi_4\).  Suppose:

1. \(P:\mathbb N\to\mathbb C\) is supported on \(g\asymp G\) and,
   after zero extension,
   \[
   \|P\|_\infty+\operatorname {Var}_{g}P\le C_P;
   \tag{128.C2}
   \]
2. \(w:\mathbb N\to\mathbb C\) is supported on \(d\asymp D\) and
   \[
   \|w\|_\infty+\operatorname {Var}_{d}w\le C_w;
   \tag{128.C3}
   \]
3. \(aG\asymp L\), \(b=\rho v\asymp B\), and \(v\) ranges over one
   integer interval whose corresponding \(b\)-range has length at most
   \(Q\).

Define

\[
 A(v)=\frac1a\sum_g\frac{\chi(g)}gP(g)w(g\rho v)
 \tag{128.C4}
\]

and include the two endpoint values in \(V^2\).  Then

\[
 \boxed{
 \|A\|_{V^2(I)}
 \ll C_PC_w\frac1L
 \left(1+\frac{DQ}{B^2}\right)^{1/2}.}
 \tag{128.C5}
\]

The same conclusion holds after multiplying \(A\) by a scalar
\(b\)-weight \(\tau\) with
\(\|\tau\|_\infty+\operatorname {Var}\tau=O(1)\), after restriction to
\(O(1)\) clipped intervals, and after a divisor sum over
\(\rho\mid a\), with the divisor loss absorbed in \(Y^\varepsilon\).

## 3. Proof

Every partial sum of \(\chi_4\) is bounded.  Abel summation and (128.C2)
therefore give, uniformly for every subinterval \(J\subset[g\asymp G]\),

\[
 \left|\sum_{g\in J}\frac{\chi(g)}gP(g)\right|
 \ll \frac{C_P}{G}.
 \tag{128.C6}
\]

Zero-extend \(w\) and put \(\Delta w(t)=w(t)-w(t+1)\).  The exact
discrete Stieltjes identity is

\[
 w(d)=\sum_{t\ge d}\Delta w(t),
 \qquad
 \sum_t|\Delta w(t)|=\operatorname {Var}w.
 \tag{128.C7}
\]

Thus (128.C4) is the absolutely finite superposition

\[
 A(v)=\sum_t\Delta w(t)A_t(v),
 \qquad
 A_t(v)=\frac1a
 \sum_{g\le t/(\rho v)}\frac{\chi(g)}gP(g).
 \tag{128.C8}
\]

For fixed \(t\asymp D\), (128.C6) and \(aG\asymp L\) give

\[
 |A_t(v)|\ll \frac{C_P}{L}.
 \tag{128.C9}
\]

The endpoint
\(M_t(v)=\lfloor t/(\rho v)\rfloor=\lfloor t/b\rfloor\) is monotone.
Across a \(b\)-window of length \(Q\),

\[
 |M_t(v_-)-M_t(v_+)|
 \ll 1+\frac{tQ}{B^2}
 \ll 1+\frac{DQ}{B^2}=:J.
 \tag{128.C10}

Hence there are at most \(O(J)\) consecutive \(v\)-steps on which
\(A_t\) changes.  On each such step the difference is a sum over one
integer interval in \(g\), so (128.C6) again bounds it by \(O(C_P/L)\),
even if the floor endpoint skips several integers.  Including the two
endpoint values,

\[
 \|A_t\|_{V^2(I)}^2\ll \frac{C_P^2J}{L^2}.
 \tag{128.C11}
\]

The vector consisting of the left endpoint, all consecutive differences,
and the right endpoint has its ordinary Euclidean norm equal to
\(V^2\).  Minkowski applied to (128.C8), followed by (128.C7), gives

\[
 \|A\|_{V^2(I)}
 \le\sum_t|\Delta w(t)|\|A_t\|_{V^2(I)}
 \ll C_PC_w\frac{J^{1/2}}L,
\]

which proves (128.C5).

For a bounded-BV multiplier \(\tau\), write

\[
 \Delta(\tau A)(v)=\tau(v+1)\Delta A(v)+A(v)\Delta\tau(v).
\]

The first term is controlled by (128.C5); the second has \(\ell^2\) norm
at most \(\|A\|_\infty\operatorname {Var}\tau\ll L^{-1}\), and the
endpoint values are safe.  Zero-extension to a clipped interval adds only
two jumps of size \(O(L^{-1})\).  Finally, summing over divisors
\(\rho\mid a\) costs \(\tau(a)\ll_\varepsilon Y^\varepsilon\).

## 4. Application to the accepted literal coefficient

Round 95 gives exactly

\[
 \begin{aligned}
 A_1(a,b)&=\frac{2\chi_4(b)}{\pi ia}
 \sum_g\frac{\chi_4(g)}gF_{1,a,b}(g),\\
 A_2(a,b)&=-\frac{4\chi_4(|a|)}{\pi|a|}
 \sum_g\frac{\chi_4(g)}gF_{2,a,b}(g),
 \end{aligned}
 \tag{128.C12}
\]

where

\[
 F_{i,a,b}(g)=
 \Phi(g|a|/(H+1))v_L(g|a|)\omega_{i,D}(gb),
 \tag{128.C13}
\]

with all literal support indicators and the star included.  On a fixed
moving-symbol stratum, \(H\), prefix, and floor data are fixed; the
frequency factor in (128.C13) is sampled BV in \(g\), and the smooth or
hard denominator profile is sampled BV in \(d=gb\).  Also
\(g\asymp G=D/B\) and \(|a|G\asymp L\).  Thus (128.C5), with
\(Q=Q_B\), gives

\[
 \|A_i(a',\rho\,\cdot)\|_{V^2(I)}
 \ll_\varepsilon \frac{J_B^{1/2}}L Y^\varepsilon,
 \qquad
 J_B=1+\frac{DQ_B}{B^2},
 \tag{128.C14}
\]

provided every support indicator in (128.C13) is either frequency-only,
denominator-only, or contributes only \(O(1)\) clipped interval entries
and exits on the same window.

The M1 reduced character \(\chi_4(b')\) must not be included in the
amplitude in (128.C14): after Möbius inversion it is resolved into the
literal quarter-linear phase already denoted by \(\vartheta_i\rho v\).
Otherwise it creates artificial every-step variation.  The M2 reduced
numerator character is constant because \(a'\) is fixed.  The common lift
character remains inside (128.C12) and is exactly what proves (128.C6).

The determinant triangular taper is bounded BV on each clipped
\(Q_B\)-interval, so the multiplier extension of the lemma applies.
Dyadic shell cutoffs, strict versus weak faces, stars, and hard endpoint
samples are discrete-BV profiles or \(O(1)\) zero-extension jumps.

## 5. Controls

- **V2 endpoints:** included explicitly through (128.C9)--(128.C11).
- **Multiple births in one step:** harmless; their difference is one
  character sum and (128.C6) is interval-uniform.
- **Continuous smooth variation:** represented exactly by the discrete
  threshold superposition (128.C7), so it is not silently counted as an
  endpoint birth.
- **Hard profile and star:** zero extension and a half-weight change only
  the discrete BV mass.
- **Adversarial lift phases:** fail (128.C6).  A phase-conjugating weight
  can make an interval sum have length \(G\), showing why the actual
  common character and sampled-BV factorization are essential.
- **Progressions:** \(b=\rho v\) changes the number of \(v\)-steps but not
  the total floor movement (128.C10).
- **Capacity:** at the longest shell \(J_B=Y^{1/16+o(1)}\), so the proved
  exponent is \(\theta=1/2<2/3\).
- **Scope:** (128.C14) is only the coefficient gate.  It gives no bound
  for the reciprocal oscillatory sum without the separate open curvature
  inequality.

## 6. First doubtful step

The proof of the abstract lemma is complete.  The first literal seam is
the clause attached to (128.C14): the accepted compact formula says that
every literal support indicator is included in \(F_{i,a,b}\), but does not
list each indicator's dependence on \((ga,gb)\) in the Round-95 report.
The conductor must audit the underlying coefficient dictionary and verify
that no indicator couples \(g a'\) and \(g b'\) in a way that has more than
\(O(J_B)\) entries or exits on the same \(Q_B\)-window.  The next possible
seam is a moving-symbol boundary that was fixed only cellwise rather than
on the entire reciprocal window.

If every literal package has the separable or clipped-BV form stated in
Round 95, (128.C14) is proved.  If one coupled support remains, it must be
written explicitly and its \(V^2\) contribution tested rather than hidden
inside the notation \(F_{i,a,b}\).

## 7. Recommended state effect

Retain this as candidate conductor evidence until the two nonblind reports
independently reconstruct the literal coefficient dictionary.  Promote the
coefficient norm only if that dictionary closes the coupled-support seam.
Do not promote the subsequent oscillatory inequality, the conditional
\(Y^{73/96}\) block bound, any global exponent, or any M9 obligation from
this lemma alone.
