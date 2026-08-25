# M9--M2 hard-TOP (t=1) character-Poisson product-collar obstruction

## Statement

Let (J=\sqrt X), (y=\lfloor J\rfloor),
(q_X=X/y^2), (H=\lfloor yX^{-1/4}\rfloor), and
(1\ll L\ll H\).  Consider the literal (t=1) close-factor scalar

\[
\begin{aligned}
\mathcal S_{L,1}=\sum_{\substack{d_1d_2\asymp L^2\\
d_1,d_2\ \mathrm{squarefree},\ (d_1,d_2)=1\\
d_1\ \mathrm{odd},\ d_2\le d_1\le4d_2}}
&\chi_4(d_1)\left(\frac{L^2}{d_1d_2}\right)^{3/4}
\eta_L(d_1)\Phi\!\left(\frac{d_1}{H+1}\right)\\
&\times W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right)
e(J\sqrt{d_1d_2}),
\end{aligned}
\tag{K162.1}
\]

with every inherited half-open support, floor, profile value, cone edge,
star, endpoint transition, and zero-extension convention retained.

The following route-scoped obstruction holds.

1. The squarefree/coprime projector has an exact Möbius opening.  On each
   fixed opening (Q=[a^2,c]), (R=[b^2,c]), character Poisson transfers
   (\chi_4) from (d_1) to an odd dual variable (s); it does not
   remove the character.
2. The exact character transform is involutive.  Repeating it gives no
   contraction.
3. The product phase has rank-one Hessian.  For every compact smooth
   interior cell of one fixed opening, two-variable Poisson has resonant
   product

   \[
    s\ell=XQR,
   \]

   broadened by the radial support to

   \[
    |s\ell-XQR|\ll QRJ/L.
   \]

   One dual coefficient has scale
   (L^{3/2}/(QR\sqrt J)), while the collar contains at most
   ((QRJ/L+1)(XQR)^\varepsilon) factor pairs.  Termwise positive
   control therefore has capacity (\sqrt{JL},X^\varepsilon); the
   (QR)-decay is repaid by the rescaled collar width.
4. Grouping by (N=s\ell) yields a moving near-square
   (\chi_4)-divisor window, not a completed (r_2)-coefficient.
   Standard positive differencing makes the character correlation
   constant.
5. The Bombieri--Iwaniec, Kowalski--Robert--Wu, Robert--Sargos,
   Duke--Friedlander--Iwaniec, Bettin--Chandee, and
   Dong--Robles--Zeindler interfaces audited in Round 162 do not prove
   the literal target.  The separated real-monomial routes fail after
   restoring powers.  The fixed-modulus or fixed-integral Kloosterman
   cards have no uniform literal placement for the arbitrary-real
   ordinary reciprocal produced here; Bettin--Chandee has a formal
   degenerate placement on an integral subcase, but its printed
   parameter factor is already adverse.

Consequently, exact Möbius opening followed by termwise positive
one- or two-variable Poisson control, a second bare character transform,
standard positive differencing, and those named source placements do not
prove

\[
 |\mathcal S_{L,1}|\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{K162.2}
\]

This is not a physical lower bound and not a universal literature
impossibility theorem.  Literal hard-boundary families are not declared
target-safe; they remain inside the first open signed aggregate.

## Proof

### 1. Exact arithmetic and character opening

The indicator in (K162.1) is

\[
\begin{aligned}
&\mu^2(d_1)\mu^2(d_2)\mathbf1_{(d_1,d_2)=1}\\
&\quad=\sum_{a^2\mid d_1}\mu(a)
       \sum_{b^2\mid d_2}\mu(b)
       \sum_{c\mid(d_1,d_2)}\mu(c).
\end{aligned}
\tag{K162.3}
\]

Put

\[
 Q=[a^2,c],\qquad R=[b^2,c],\qquad d_1=Qm,\qquad d_2=Rn.
\tag{K162.4}
\]

The character forces (a,c,Q,m) odd, while (b,R,n) may be even.
Thus the even-(d_2) branch is retained, and

\[
 \chi_4(Qm)=\chi_4(Q)\chi_4(m).
\tag{K162.5}
\]

Every opening retains the rescaled shell, cone, profiles, endpoints, and
the sign (\mu(a)\mu(b)\mu(c)\chi_4(Q)).

With

\[
 \widehat g(\xi)=\int_{\mathbb R}g(x)e(-\xi x)\,dx,
\]

the identity

\[
 \chi_4(m)=\frac{e(m/4)-e(-m/4)}{2i}
\]

and ordinary Poisson give

\[
 \boxed{
 \sum_{m\in\mathbb Z}\chi_4(m)g(m)
 =\frac i2\sum_{\substack{s\in\mathbb Z\\s\ \mathrm{odd}}}
 \chi_4(s)\widehat g(s/4).}
\tag{K162.6}
\]

Indeed, for the quarter-shift sign (\sigma\), set (s=4k-\sigma).
Then (\sigma=-\chi_4(s)), so
(\sigma/(2i)=i\chi_4(s)/2).

### 2. One-variable stationary data and involution

For fixed physical (d_2), the opened (m)-phase is

\[
 F_s(m)=J\sqrt{Qd_2m}-sm/4.
\tag{K162.7}
\]

Its positive saddle is

\[
 m_s=\frac{4XQd_2}{s^2},\qquad
 d_1^*=\frac{4XQ^2d_2}{s^2},\qquad
 F_s(m_s)=\frac{XQd_2}{s}.
\tag{K162.8}
\]

The cone is equivalent to (JQ\le s\le2JQ), and the exact profile
argument is

\[
 W\!\left(\sqrt{\frac{q_Xd_1^*}{4d_2}}\right)
 =W\!\left(\frac{XQ}{ys}\right).
\tag{K162.9}
\]

Since

\[
 F_s''(m_s)=-\frac{s^3}{32XQd_2},
\]

the normalization and stationary factor satisfy

\[
 \left(\frac{L^2}{d_1^*d_2}\right)^{3/4}
 |F_s''(m_s)|^{-1/2}
 =\frac{2L^{3/2}J^{-1/2}}{Qd_2}.
\tag{K162.10}
\]

Together with (i/2) and the negative Gaussian unit (e(-1/8)), the
leading signed unit is (e(1/8)\chi_4(Q)\chi_4(s)).

For exact involution let (h(s)=\widehat g(s/4)).  Then

\[
 \widehat h(\xi)=4g(-4\xi).
\]

Two applications of (K162.6) give

\[
 \left(\frac i2\right)^2 4
 \sum_{u\ \mathrm{odd}}\chi_4(u)g(-u)
 =\sum_{u\ \mathrm{odd}}\chi_4(u)g(u),
\tag{K162.11}
\]

because (\chi_4(-u)=-\chi_4(u)).  Thus a second bare transform returns
the original character sum.

### 3. Rank-one dual geometry

For (f(x,z)=J\sqrt{xz}),

\[
 \operatorname{Hess}f=\frac J4
 \begin{pmatrix}
 -z^{1/2}x^{-3/2}&(xz)^{-1/2}\\
 (xz)^{-1/2}&-x^{1/2}z^{-3/2}
 \end{pmatrix},
\tag{K162.12}
\]

whose determinant is zero and whose radial null vector is ((x,z)).
After Poisson in both opened variables the phase is

\[
 J\sqrt{QRmn}-sm/4-\ell n.
\tag{K162.13}
\]

Set physical (u=Qm=tw), (v=Rn=t/w).  The phase becomes

\[
 t\left(J-\frac{s}{4Q}w-\frac{\ell}{Rw}\right).
\tag{K162.14}
\]

The angular saddle satisfies

\[
 w_0^2=\frac{4Q\ell}{Rs},\qquad
 J-\sqrt{\frac{s\ell}{QR}}=0,
\]

so

\[
 \boxed{s\ell=XQR},\qquad
 \boxed{Q\ell\le Rs\le4Q\ell}.
\tag{K162.15}
\]

The second box is the exact image of (1\le u/v\le4).

For a compact smooth radial cell of physical length comparable to (L),
the residual frequency

\[
 \delta_{Q,R}(s,\ell)=J-\sqrt{\frac{s\ell}{QR}}
\]

is central only for (|\delta_{Q,R}|\ll L^{-1}).  Rationalizing the
square roots on the dual support yields

\[
 \boxed{|s\ell-XQR|\ll QRJ/L.}
\tag{K162.16}
\]

The number of possible integer products is (O(QRJ/L+1)), and each has
at most (O_\varepsilon((XQR)^\varepsilon)) admissible factorizations.
Thus

\[
 \#\{(s,\ell)\}_{\mathrm{collar}}
 \ll_\varepsilon
 \left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon.
\tag{K162.17}
\]

The Jacobian (dm\,dn=du\,dv/(QR)), the physical amplitude, angular
stationary phase, and radial length give one smooth-interior dual
coefficient the scale

\[
 \frac{L^{3/2}}{QR\sqrt J}.
\tag{K162.18}
\]

Multiplying (K162.17) and (K162.18) gives

\[
 \sqrt{JL}\,(XQR)^\varepsilon
 =L^{3/2}\left(\frac HL+O(L^{-1})\right)(XQR)^\varepsilon.
\tag{K162.19}
\]

The rescaling has supplied no positive (Q,R)-gain.  On the favorable
single-opening model, combining this with triviality leaves the
coefficient-insensitive comparison

\[
 \min\{L^2,\sqrt{JL}\}
 =L^{3/2}\min\{L^{1/2},H/L\}\,(1+o(1)).
\tag{K162.20}
\]

This is a route capacity, not a bound for the complete physical Möbius
sum.  It is above target by a fixed power on polynomial intermediate
blocks and only target-scale at (L\asymp H).

### 4. Local divisor window and differencing

Put (N=s\ell).  The dual cone in (K162.15) is equivalent to

\[
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}.
\]

The smooth central transform therefore groups as

\[
 \sum_{\substack{s\mid N,\ s\ \mathrm{odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi_4(s)\mathcal K_{Q,R}(N;s),
\tag{K162.21}
\]

with the actual saddle profiles and radial Fourier weight retained in
(\mathcal K_{Q,R}).  For (Q=R=1), completion to all divisors would
use

\[
 \sum_{s\mid N}\chi_4(s)=r_2(N)/4,
\tag{K162.22}
\]

but it adds an uncontrolled complementary divisor window.  It does not
estimate (K162.21).

For odd (d),

\[
 \chi_4(d+2h)\chi_4(d)=(-1)^h.
\tag{K162.23}
\]

Thus ordinary differencing followed by absolute values makes the
character constant in each correlation.  It gives no character-sensitive
saving, while the radial null direction persists.

### 5. Source and boundary scope

The primary-source audit gives separate route failures.  First, the
Bombieri--Iwaniec and direct real-monomial interfaces require separated
coefficients, whereas the physical projector, ratio cutoff, shell, and
cone are joint.  Even granting cost-one separation, the
Kowalski--Robert--Wu and Robert--Sargos bounds restore, respectively,

\[
 J^{1/8}L^{13/8}+L^{3/2}+L^{7/4}+J^{-1/2}L^{3/2},
\tag{K162.24}
\]

and

\[
 J^{1/4}L^{3/2}+L^{7/4}+L^{3/2}+J^{-1/2}L^{3/2}.
\tag{K162.25}
\]

Neither reaches the target in the assigned range.  For the
Duke--Friedlander--Iwaniec fixed-modulus/fixed-numerator cards and the
Dong--Robles--Zeindler card, the ordinary reciprocal
(e(XQd_2/s)) has no uniform literal placement for arbitrary real
(X) and its moving physical coefficient.  On the admissible integral
subcase, Bettin--Chandee has the formal one-point-inverse placement

\[
 M=1,\qquad N\asymp JQ,\qquad A\asymp L,\qquad
 \vartheta=XQ,
\]

but its printed factor satisfies

\[
 \left(1+\frac{|\vartheta|A}{MN}\right)^{1/2}
 \asymp(JL)^{1/2},
\tag{K162.26}
\]

before the remaining positive powers and physical stationary
normalization.  Thus the formal embedding is not target-strength.

These conclusions park only the named placements.  A bespoke signed
theorem remains possible.

The smooth calculations above do not discard literal hard supports.
A nonzero endpoint can have only reciprocal-frequency Fourier decay, and
a saddle meeting a hard edge is a boundary transition.  Individual
Möbius-opened terms also need not inherit cancellations visible only
after the physical projector is recombined.  Hence hard edges, stars,
profile transitions, collar tails, and endpoint values remain in the
first open signed statement.

## First open statement

A continuation must estimate the complete signed, Möbius-coupled family
whose smooth principal part has the schematic form

\[
\begin{aligned}
 \frac{L^{3/2}}{\sqrt J}
 \sum_{a,b,c}\frac{\mu(a)\mu(b)\mu(c)\chi_4(Q)}{QR}
 \sum_{N\approx XQR}
 \sum_{\substack{s\mid N,\ s\ \mathrm{odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi_4(s)\mathcal K_{Q,R}(N;s),
\end{aligned}
\tag{K162.27}
\]

while retaining the even-(d_2) branch, arbitrary-real centre, all
profiles, hard edges, floors, stars, endpoint transitions, nonstationary
pieces, and collar tails before every positive norm.  It must recover the
factor (\min\{L^{1/2},H/L\}) missed by the favorable positive ledger.

Even a proof of this (t=1) face would leave the compatible
(L\ll D\ll L^2), (t\ll\sqrt L) few-point channels and their
near-collision collars open.  Therefore no full hard-TOP, M9--M2, M9,
bridge, quarter-theorem, or global-exponent conclusion follows from this
kernel.
