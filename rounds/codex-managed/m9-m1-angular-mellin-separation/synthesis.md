# Round 15 synthesis: Mellin modes reflect the angular sector

Campaign: `m9-m1-angular-mellin-separation`  
Round type: Mellin twisted-divisor attack  
Graph SHA-256 before patch: `aa33b1c414e135f96f912b34ec17acda79c3cf5cb68a73c4fb706bd393993251`

## Conductor decision

Promote the exact double-Mellin separation, its twisted-divisor Dirichlet
series, the centered functional equation, and the scoped angular return-map
obstruction. Retain GAR and its top Perron maximal component as open. No new
point of the residual M1 corridor is closed.

The statement-only derivation fixes all Mellin powers, floors, parity,
product cutoffs, and endpoint stars. The analytic derivation and independent
primary-source audit agree on the completion, conductor, root number, and
coefficient reflection. The source audit also confirms that existing
fixed-parameter Voronoi formulas do not provide the required uniform
complex-order or hard-endpoint estimate. No numerical experiment was used.

## Exact double-Mellin formula

Put

\[
 \tau_{\chi_4,z}(n)=
 \sum_{hq=n}\chi_4(q)h^{-z},
 \qquad N_X=\lfloor16\sqrt X\rfloor.
\]

For spatial Mellin variable (u) and height variable (v), set (z=u+v)
and

\[
 \mathcal R_X(u,v)=
 \sum_{n\le N_X}\tau_{\chi_4,u+v}(n)
 n^{-3/4+u/2}e(\sqrt{Xn}).
\]

For every interior scale (j\ge1), the exact contribution is

\[
 \mathcal I_j(X)=\frac1{(2\pi i)^2}
 \int_{(a)}\int_{(b)}
 \widehat W(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u
 (H_j+1)^v\mathcal R_X(u,v)\,dv\,du,
\]

where (H_j=\lfloor D_jX^{-1/4}\rfloor) and
(phi(t)=\Phi(t)\mathbf1_{0<t<1}). The top scale has the same formula as a
symmetric Perron limit with

\[
 \widehat W_+(u)=\frac1u-rac1u\int_0^1W'(t)t^u\,dt.
\]

The (1/u) term is exactly the hard spatial jump and yields the stationary
endpoint half weight. The second term is rapidly decreasing. Thus

\[
 \sum_{n\le N_X}\mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn})
 =\mathcal I_0^*(X)+\sum_{j\ge1}\mathcal I_j(X).
\]

All interior contours are absolutely integrable. The top (1/u) contour
is not: absolute truncation at height (T) costs
(O(\log(2+T/a))), so a maximal Perron/Hilbert estimate is genuinely
needed.

## Twisted divisor series and centering

In the joint absolute-convergence region

\[
 \Re s>1,qquad \Re(s+z)>1,
\]

one has

\[
 \boxed{
 \sum_{n\ge1}\tau_{\chi_4,z}(n)n^{-s}
 =\zeta(s+z)L(s,\chi_4).}
\]

Define the centered coefficient

\[
 a_z(n)=n^{z/2}\tau_{\chi_4,z}(n)
 =\sum_{hq=n}\chi_4(q)(q/h)^{z/2}.
\]

Then

\[
 F_z(s)=\sum_na_z(n)n^{-s}
 =\zeta(s+z/2)L(s-z/2,\chi_4),
\]

and, because (z=u+v),

\[
 \boxed{
 \mathcal R_X(u,v)=
 \sum_{n\le N_X}a_z(n)n^{-3/4-v/2}e(\sqrt{Xn}).}
\]

This is a genuine simplification: the spatial variable (u) disappears
from the radial power and survives only in the angular shift and outside
scale factors.

## Exact functional equation

For the primitive odd character (chi_4), define

\[
 \Lambda_z(s)=
 \pi^{-(s+z/2)/2}\Gamma\!\left(\frac{s+z/2}{2}\right)
 \left(\frac4\pi\right)^{(s-z/2+1)/2}
 \Gamma\!\left(\frac{s-z/2+1}{2}\right)F_z(s).
\]

Since both component root numbers are (+1),

\[
 \boxed{\Lambda_z(s)=\Lambda_{-z}(1-s).}
\]

The arithmetic conductor is (4), and the two archimedean heights are
(t\pm\Im z/2). Hence functional-equation/Voronoi duality sends

\[
 \boxed{a_z\longmapsto a_{-z}.}
\]

It reflects the divisor ratio (q/h\leftrightarrow h/q); it does not erase
the angular multiplier or produce (r_2/4). At (z=0),
(a_0(n)=r_2(n)/4), exactly the previously audited Hardy–Voronoi return.

For bounded shifts and a smooth radial shell (n\asymp N), stationary
analysis of the degree-two Hankel kernel returns to a dual product window
near (m=X). Full uniform localization for large (|\Im z|) is not
promoted, because that transition range has not received an independent
Stirling seam proof.

## Literature verdict

Banerjee–Khurana exactly matches the coefficient via
(	au_{\chi_4,z}=\overline\sigma_{-z,\chi_4}) and supplies fixed-order
odd-character Voronoi identities. Its hypotheses require analytic
finite-interval weights and (0<\Re\nu<1/2), and it supplies no uniform
large-imaginary-order estimate. Kiral–Zhou provides the general
double-Dirichlet-series architecture, but its degree-two, ramified,
noncuspidal, polar specialization is not a direct theorem import. Neither
source controls the top (1/u) Perron limit.

Source cards:
`sources/banerjee_khurana_2023.md` and `sources/kiral_zhou_2016.md`.

## Remaining exact kernel

The functional equation is useful because it identifies the missing seam,
but it is not a bound. The smallest remaining mode-space requirement is the
outside-integral signed correlation between the actual (z) sector and its
reflected (-z) sector, together with a maximal theorem for the top Perron
mode. Pointwise fixed-(z) estimates cannot simply be integrated: the
analytic conductor grows with (t\pm\Im z/2), (widehat\phi(v)) has a
(1/v) pole near zero, and the top symbol has the (1/u) tail.

GAR, RCS, blockwise M9-M1, M9-M2, M9, and the Gauss target remain open.

