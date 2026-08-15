# Round 29 synthesis: side cancellation is false, but the signed finite-box limit survives

Campaign: `m9-m1-beta-outside-v-side-reconciliation`  
Round type: beta outside-v-side reconciliation  
Graph SHA-256 before patch: `2a5a8ac3d40fc39cef58d677ee339ec474c3eb88ca1f4ab5755fec6b73c67a0c`

## Conductor decision

Round 29 closes the proposed outside-side interface with a correction rather
than a cancellation theorem.

With both horizontal sides parametrized left-to-right, a finite \(v\)-shift
has the exact sign pattern

\[
 {\cal V}_b={\cal V}_\ell+{\cal S}_+-{\cal S}_-
 +2\pi i\sum\operatorname {Res}.                       \tag{29.1}
\]

At the upper collision, the logarithmic coefficients of \({\cal V}_b\)
and \({\cal S}_+\) agree; at the lower collision, those of
\({\cal V}_b\) and \(-{\cal S}_-\) agree. The sides reproduce or transfer
the edge required by (29.1). They are not the missing tails
\(|\nu|>V\), and the physical top limit \(a=\Re u\downarrow0\) does not
move the \(v\)-line or generate these sides. Axial, top, corner, and
artificial-pole residue terms have no independent fixed-\(V\) logarithmic
coefficient available to reverse this conclusion.

The edge is nevertheless not a divergence of the complete signed operator.
Retaining the exact finite polytope and taking the symmetric top limit in
its original variable \(\mu=\Im u\) gives a uniform finite-box Plemelj
limit. The fixed-\(L\) logarithm is locally integrable in
\(L=\alpha-\beta=\mu+\nu\). Thus Round 28 is a no-go for pointwise scaled
\(C^2\) patching, not a no-go for the beta transition or Gauss target.

The next interface is a distribution-first, polytope-aware two-saddle
estimate with logarithmic amplitude. The ordinary \(C^2\) Fresnel lemma
remains valid away from moving faces, but is the wrong tool on them.

Round 29 used no numerical experiment or external theorem.

## Exact finite-box top lemma

In the accepted diagonal coordinates,

\[
 \mu=\alpha-\beta-\nu,\qquad |\mu|\le U,\qquad |\nu|\le V.
\]

Equivalently, with \(L=\alpha-\beta=\mu+\nu\), the exact section is

\[
 I_{U,V}(L)=[-V,V]\cap[L-U,L+U],                     \tag{29.2}
\]

and \(L\in[-U-V,U+V]\). Let \(F\in C^1([-U,U]\times[-V,V])\). Then

\[
 T_{a;U,V}(F)=\int_{-V}^{V}\int_{-U}^{U}
 \frac{F(\mu,\nu)}{a+i\mu}\,d\mu\,d\nu             \tag{29.3}
\]

has the signed limit

\[
 \boxed{
 \begin{aligned}
 \lim_{a\downarrow0}T_{a;U,V}(F)
 ={}&\pi\int_{-V}^{V}F(0,\nu)\,d\nu\\
 &-i\int_{-V}^{V}\operatorname {PV}\!\int_{-U}^{U}
       \frac{F(\mu,\nu)}{\mu}\,d\mu\,d\nu .
 \end{aligned}}                                      \tag{29.4}
\]

Indeed, write

\[
 F(\mu,\nu)=F(0,\nu)+\mu G(\mu,\nu).
\]

Then

\[
 \int_{-U}^{U}\frac{d\mu}{a+i\mu}=2\arctan(U/a)\to\pi,
 \qquad
 \frac{\mu}{a+i\mu}\to-i,quad
 \left|\frac{\mu}{a+i\mu}\right|\le1.
\]

Dominated convergence proves (29.4), including its sign. Taking absolute
values first costs \(\log(1/a)\), so the lemma is genuinely signed. It does
not use \(\chi_4\) and is analytic infrastructure, not the final arithmetic
saving.

In section coordinates, (29.4) becomes almost everywhere

\[
 \boxed{
 \begin{aligned}
 C_{0;U,V}(L)={}&
 \pi\mathbf1_{|L|<V}H(L,L)\\
 &-i\operatorname {PV}\!\int_{I_{U,V}(L)}
       \frac{H(L,\nu)}{L-\nu}\,d\nu .
 \end{aligned}}                                      \tag{29.5}
\]

The equality convention at \(|L|=V\) belongs to symmetric distributional
inversion; changing one point value does not alter the operator.

## Exact edge scope

At \(L=V\), assuming the numerator is nonzero and separated from all other
poles,

\[
 C_{a;U,V}(V)=-iH(V,V)\log(1/a)+O(1),                \tag{29.6}
\]

and the lower edge has the opposite orientation. The condition
\(|L-\nu|\le U\) changes the finite length but does not remove (29.6).

After the physical limit, the singularity is
\(O(1+|\log|L\mp V||)\) and belongs to every finite local \(L^p\) space.
The elementary bound is

\[
 \sup_{0<a\le1}\int_{-c}^{c}
 |\Log(a+iy)|^p\,dy<\infty,qquad 1\le p<\infty.       \tag{29.7}
\]

Split \(|y|\le a\) from \(a<|y|\le c\). The first part is
\(O(a(1+|\log a|)^p)\); the second is dominated by
\(O((1+|\log|y||)^p)\). Thus the signed top limit exists in an integrated
norm.

Pointwise derivatives fail. At an edge, the first two \(L\)-derivatives
have capacities \(a^{-1}\) and \(a^{-2}\), and after the limit have the
expected inverse-power face singularities. The scaled \(C^2\) hypothesis of
Round 28 cannot be asserted across moving faces.

## Side and residue ledger

For upward verticals and left-to-right horizontals, positive orientation
proves (29.1). If \(v=0\) is crossed, it enters with the full positive
residue. If both \(u\) and \(v\) are shifted, apply the two one-variable
identities sequentially: the \(u=0\) residue is evaluated on every surviving
\(v\)-piece, the \(v=0\) residue on every surviving \(u\)-piece, and the
joint corner appears exactly once.

On a fixed diagonal slice the moving pole \(v=z\), equivalently \(u=0\),
has residue

\[
 \operatorname {Res}_{v=z}\frac{{\cal M}(z-v,v)}{(z-v)v}
 =-\frac{{\cal M}(0,z)}z,                             \tag{29.8}
\]

where the minus sign is \(du=-dv\). It must not be counted twice as an
independent top residue.

The artificial-pole-safe radial expression remains

\[
 R_1=\omega G+(1-\omega)R_1-\omega E_1.              \tag{29.9}
\]

Because \(\omega\) is nonholomorphic in contour heights, every
Cauchy--Green area term must remain until the three terms in (29.9) are
recombined. No isolated \(\rho=0\) residue or
\(\bar\partial\omega\) term is available to cancel (29.6).

## Replacement kernel

The smallest exact survivor is

\[
 \begin{aligned}
 {\cal J}_{U,V}=\int e^{i\Psi(L)}\Bigg[
 &\pi\mathbf1_{|L|<V}H(L,L)\\
 &-i\operatorname {PV}\!\int_{I_{U,V}(L)}
       \frac{H(L,\nu)}{L-\nu}\,d\nu
 \Bigg]dL,                                           \tag{29.10}
 \end{aligned}
\]

with both signed saddles, beta mask, exact \((U,V,S)\) polytope,
\(\chi_4(q)\), all \(q,h,D_j,x\) factors, floors, stars, radial
integration, and (29.9) restored.

The conductor derived a candidate logarithmic-amplitude stationary bound:
after an exact Morse change, a compact nondegenerate oscillatory integral
with moving factor \(\Log(a+i(x-x_0))\) should cost at most the ordinary
Fresnel size times \(\log(2+\lambda)\), uniformly as \(x_0\) crosses the
saddle or endpoint. This would preserve the local \(q^{-2}\) power and add
only an \(X^\varepsilon\)-absorbable logarithm. It is not promoted here:
its exact statement, endpoint seams, and actual-profile scaled variation
need a new blind proof and hostile audit.

## Evidence assessment

- The blind report proves the side orientation, edge coefficients,
  two-axis residue ledger, moving-pole sign, and distinction between
  retained-side and closed-boundary combinations.
- The discovery report restores the exact \(|\mu|\le U\) constraint and
  proves the finite-box Plemelj limit and local integrability.
- The hostile audit independently proves the same orientation and limit,
  falsifies pointwise scaled \(C^2\), and confirms that top inversion does
  not generate \(v\)-horizontal sides.
- The conductor review gives the explicit section formula, local \(L^p\)
  control, and candidate logarithmic-Fresnel next step.

The exact finite algebra and elementary signed limit are promoted. The
candidate oscillatory estimate remains open.

## State effect

- promote the exact side orientation and no-cancellation verdict;
- promote the finite-box Plemelj limit and polytope support;
- revise the finite-height obstruction to a pointwise-\(C^2\) obstruction,
  not an obstruction to the complete signed operator;
- reject treating outside-\(v\) sides as height tails or universal
  cancellation terms;
- create the distribution-first logarithmic two-saddle kernel as open;
- retain the complete beta trace, height exhaustion, full sums,
  double-bounded share, alpha transition, M9-M1, M9-M2, M9, and the Gauss
  target as open.
