# Round 62 synthesis: subcritical small-angle collapse

Campaign: `m9-m1-lower-radial-small-angle-collapse`

## Conductor decision

The exact angular symbol collapses, on every fixed subcritical radial
block, to a one-sided character-divisor cone with a target-safe
replacement error through the inclusive exponent \(\nu=2/5\).

With \(Y=\sqrt X\), \(y=\lfloor\sqrt X\rfloor\), and
\(d_{n,h}=2h\sqrt{X/n}\),

\[
 \Omega_X^*(n,h)=\mathbf1_{d_{n,h}\leq y}^{*}
 +O\!\left(\min\{1,n/Y\}\right).
\]

For fixed \(0<\nu<1/2\) and \(n\asymp X^\nu\), this produces exactly

\[
 \mathcal D(n)=
 \sum_{\substack{hq=n\\q\ {m odd}\\q>4h}}\chi_4(q).
\]

The floor perturbation and equality star vanish in this formula by
parity.  The active height floors, bottom owner, hard top, and all
profile stars have been audited explicitly.

## Replacement range

For fixed smooth \(V\) on \(n\asymp N\),

\[
 \sum_n |V(n/N)|n^{-3/4}
 |\mathcal C_X^*(n)-\mathcal D(n)|
 \ll_V \frac{N^{5/4}\log(2N)}{Y}.
\]

Thus the replacement is power-saving below \(\nu=2/5\), costs only a
logarithm at \(\nu=2/5\), and is not target-safe by absolute summation
above that point.

## Open signed kernel

The remaining normalized target is

\[
 \sum_{\substack{h,q\geq1\\q\ {m odd}\\q>4h}}
 \chi_4(q)(hq)^{-3/4}V(hq/N)e(\sqrt{Xhq})
 \ll_{\varepsilon,V}X^\varepsilon.
\]

The coefficient is nonmultiplicative and is not \(r_2/4\).  Prime
incidences give \(N^{1/4}/\log N\) absolute capacity, while the full
incidence cone has \(N^{1/4}\log N\) capacity.  Hence the proof must use
the character and radial phase jointly.  No current primary-source
theorem, including the complete \(r_2\) Voronoi formula, estimates this
truncated cone.

## Next direction

The exact generating identity

\[
 \sum_{n\geq1}\mathcal D(n)z^n
 =\sum_{h\geq1}\frac{z^{4h^2+h}}{1+z^{2h}}
\]

suggests a partial-theta or Appell--Lerch transformation problem.  The
next round will derive this interface exactly, audit the relevant
primary literature, and test whether it supplies a signed radial
transform rather than merely another return to the original M1 sum.

No full lower-radial estimate, M9-M1 theorem, M9 theorem, or exponent
improvement is claimed.

