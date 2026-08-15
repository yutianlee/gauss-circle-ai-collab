# Round 19 synthesis: exact finite vector kernel and swept transition barrier

Campaign: `m9-m1-vector-hankel-kernel`  
Round type: finite vector Hankel kernel derivation  
Graph SHA-256 before patch: `c29c2fde51f316b7d7837d60c9abfc4210e2e5950586c36d62dec2b550635804`

## Conductor decision

Promote the exact finite reflected vector-kernel identity, its residue and
horizontal-side ledger, and the archimedean conductor transition diagram.
Retain every infinite-height/operator estimate as open. The bounded-shift
Hankel phase returns to the already known near-product window; it gives no
new bound. For unbounded angular shift, the two transition strips
(\Im s\approx\pm\Im(u+v)/2) sweep the full hard-Perron height, and the
finite radial horizontal sides cannot yet be removed uniformly.

The hostile source audit confirms the completion, root number, quotient
orientation, expansion chamber, and dual-index necessity. Existing audited
fixed-order Voronoi sources do not control these swept transition strips or
finite sides. No numerical experiment or new theorem import was used.

## Exact finite vector kernel

Put (z=u+v),

\[
 F_z(w)=\zeta(w+z/2)L(w-z/2,\chi_4),
\]

and

\[
 \mathcal A_j(u,v)=\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v.
\]

For

\[
 g_v(x)=x^{-3/4-v/2}e(\sqrt{Xx})\mathbf1_{[1,N_X]}^*(x),
 \qquad
 G_v(w)=\int_1^{N_X}x^{w-7/4-v/2}e(\sqrt{Xx})\,dx,
\]

take finite vertical segments (u\in\Gamma_{a,U}),
(v\in\Gamma_{b,V}), and (w\in\Gamma_{c,S}), where (a,b>0).
Choose (c'>1+(a+b)/2), put (\lambda=1-c'), and take
(S>(U+V)/2), so the moving zeta pole remains strictly inside the
radial rectangle.

The exact gamma quotient is

\[
 K_z(1-s)=2^{2s+z-1}\pi^{1-2s}
 \frac{\Gamma((s-z/2)/2)\Gamma((1+s+z/2)/2)}
 {\Gamma((1-s+z/2)/2)\Gamma((2-s-z/2)/2)}.
\]

After shifting the finite radial segment, retaining both horizontal sides,
and expanding (F_{-z}(s)) absolutely on (Re s=c'), the terminal vector
kernel is

\[
 \begin{aligned}
 \mathcal K_{U,V,S,X}(h,q;m)
 ={}&\mathbf1_{hq=m}\frac{\chi_4(q)}{(2\pi i)^3}
 \sum_j\int_{\Gamma_{a,U}}\int_{\Gamma_{b,V}}
 \int_{\Gamma_{c',S}}\mathcal A_j(u,v)
 \left(\frac hq\right)^{(u+v)/2}\\
 &\quad\times G_v(1-s)K_{u+v}(1-s)m^{-s}\,ds\,dv\,du.
 \end{aligned}
\]

The crossed arithmetic residue is

\[
 \sum_j\frac1{(2\pi i)^2}\int_{\Gamma_{a,U}}
 \int_{\Gamma_{b,V}}\mathcal A_j(u,v)
 G_v(1-z/2)L(1-z,\chi_4)\,dv\,du.
\]

The two radial horizontal segments joining (c\pm iS) to
(\lambda\pm iS) remain explicit. Since the outside (u,v) lines are not
moved in this identity, their (0)-axis residues are not crossed. If those
lines are later shifted, the height, top Perron, and joint corner residues,
together with their own finite horizontal segments, must be added to both
the terminal and arithmetic-residue pieces. Gamma poles paired with trivial
zeros are not counted again.

This is an exact finite-rectangle identity. It licenses neither deletion of
horizontal sides nor any limit (U,V,S\to\infty).

## Bounded-shift return and conductor diagram

For (s=\sigma+it) and (z=\zeta+i\eta), the archimedean conductor is

\[
 \boxed{\mathcal C(t,\eta)
 =4(1+|t+\eta/2|)(1+|t-\eta/2|).}
\]

For bounded (|\eta|), inversion of the complete degree-two gamma kernel
has the two standard phases (e(\pm\sqrt{mx})). Only the opposite phase can
interact stationarily with (e(\sqrt{Xx})); on a smooth shell
(x\asymp N) it returns to

\[
 |m-X|\ll\sqrt{X/N}.
\]

This is the accepted near-product return and is equivalent-hard, not a new
sector estimate.

For large (|\eta|), the exact conductor has three regimes:

1. outer: both (|t\pm\eta/2|\gg1), so two-factor Stirling applies but
   the saddle and amplitude vary with (eta);
2. single transition: one of (|t\pm\eta/2|\lesssim1), so one gamma
   argument is bounded and ordinary two-factor Stirling is invalid;
3. double bounded: possible only for bounded (|\eta|), already covered by
   fixed-order analysis.

Because (eta=\Im u+\Im v) and the top (u)-integral is maximal, the two
single-transition strips sweep every large outside height. On the radial
horizontal sides, decay is uniform only when (S) stays separated from and
dominates both transition planes. No accepted exhaustion relates (S) to
(U+V) strongly enough while preserving the maximal (u)-limit.

## Literature scope

Banerjee--Khurana supplies fixed-order odd-character Voronoi identities for
analytic finite-interval weights under real-part restrictions. It supplies
neither a hard spatial jump nor estimates uniform in large imaginary order.
Kiral--Zhou supplies structural Voronoi architecture, but not this ramified,
polar degree-two specialization with three contour heights and finite
horizontal sides. Neither source closes the swept transition operator.

## Smallest survivor

The remaining exact analytic object is the sum of:

- the vector kernel restricted to
  (|\Im s\mp\Im(u+v)/2|\lesssim1);
- the radial horizontal sides under a nested finite-height exhaustion;
- the already listed arithmetic and axial residues.

A bounded-shift theorem cannot be extrapolated across this object. The next
round should change to diagonal archimedean coordinates

\[
 \alpha=t+\eta/2,\qquad \beta=t-\eta/2,
\]

and test whether a nested choice (S\gg U+V) removes the horizontal sides
while reducing each single-transition strip to a degree-one kernel.

## State effect

- promote the finite vector-kernel identity and exact gamma normalization;
- promote the bounded-shift near-product return and the scoped
  outer/transition/double-bounded conductor diagram;
- reject deletion of horizontal sides, fixed-order extrapolation, and
  black-box source imports;
- retain the swept transition/horizontal operator, high-(2)-adic reflected
  tail, GAR, M9-M1, M9-M2, M9, and the target as open.

