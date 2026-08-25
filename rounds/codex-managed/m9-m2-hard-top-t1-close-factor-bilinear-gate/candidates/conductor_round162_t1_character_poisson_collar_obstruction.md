# Round 162 conductor candidate: literal character Poisson and the scaled product collar

- Campaign: `m9-m2-hard-top-t1-close-factor-bilinear-gate`
- Round: 162
- Status: selected candidate; not accepted until seam and graph review
- Starting graph SHA-256:
  `8d39b06bd12357e337159473da3d4d6ec0c71d0ab3217588e4c6b5b34973b422`

## 1. Selected result and scope

The three independent reports agree on a narrow terminal result:

> Exact character-preserving Poisson, exact Möbius opening followed by
> termwise positive dual control, a second bare character transform,
> standard positive differencing, and the named source interfaces audited
> in Round 162 do not prove the literal (t=1) estimate
>
> \[
>  |\mathcal S_{L,1}|\ll_\varepsilon L^{3/2}X^\varepsilon
> \tag{162.CA1}
> \]
>
> uniformly for (1\ll L\ll H\asymp J^{1/2}), (J=\sqrt X).

This is a method obstruction, not a lower bound for the physical scalar.
It leaves open a signed theorem acting jointly on the literal character,
Möbius weights, profiles, and boundary pieces before every positive norm.

The selected kernel deliberately does **not** promote the discovery
report's stronger claim that all transformed hard-edge families are
already target-safe.  The blind report could not certify the required
literal profile regularity and endpoint ledger, and the accepted Round-75
history warns that a leading moving-saddle formula need not be an
all-orders identity.  Boundary terms are retained as part of the open
signed aggregate.  This does not weaken the route no-go: the favorable
smooth interior already leaves the required power unpaid, while rougher
pieces add obligations rather than a proved saving.

## 2. Literal coefficient and exact arithmetic opening

The frozen scalar is

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
\tag{162.CA2}
\]

with the literal half-open shell, cone, profiles, endpoint values, stars,
floors, and zero extension.  Here

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor.
\tag{162.CA3}
\]

The squarefree and coprime projector has the exact identity

\[
\begin{aligned}
&\mu^2(d_1)\mu^2(d_2)\mathbf 1_{(d_1,d_2)=1}\\
&\quad=\sum_{a^2\mid d_1}\mu(a)
       \sum_{b^2\mid d_2}\mu(b)
       \sum_{c\mid(d_1,d_2)}\mu(c).
\end{aligned}
\tag{162.CA4}
\]

For one opening put

\[
 Q=[a^2,c],\qquad R=[b^2,c],\qquad d_1=Qm,\quad d_2=Rn.
\tag{162.CA5}
\]

Because the character kills even (d_1), only odd (a,c,Q,m) survive,
whereas (b,R,n), and hence the physical (d_2)-branch, may be even.
Complete multiplicativity gives

\[
 \chi_4(Qm)=\chi_4(Q)\chi_4(m).
\tag{162.CA6}
\]

The opening is exact but is not cost-free: every rescaled hard support
and every sign (\mu(a)\mu(b)\mu(c)\chi_4(Q)) must remain coupled until
an estimate is applied.

## 3. Exact character transform and one-variable saddle

With (e(t)=e^{2\pi i t}) and

\[
 \widehat g(\xi)=\int_{\mathbb R}g(x)e(-\xi x)\,dx,
\]

the primitive character satisfies the exact Poisson identity

\[
 \boxed{
 \sum_{m\in\mathbb Z}\chi_4(m)g(m)
 =\frac{i}{2}\sum_{\substack{s\in\mathbb Z\\s\ \mathrm{odd}}}
 \chi_4(s)\widehat g(s/4).}
\tag{162.CA7}
\]

Indeed, writing

\[
 \chi_4(m)=\frac{e(m/4)-e(-m/4)}{2i}
\]

and setting (s=4k-\sigma) transfers the two quarter shifts to the two
odd residue classes; since (\sigma=-\chi_4(s)), their coefficient is
(-\chi_4(s)/(2i)=i\chi_4(s)/2).  Thus the character is preserved before
any positive norm.

For fixed physical (d_2), the opened phase in the (m)-integral is

\[
 F_s(m)=J\sqrt{Qd_2m}-\frac{s}{4}m.
\tag{162.CA8}
\]

Its positive saddle and phase are

\[
 m_s=\frac{4XQd_2}{s^2},\qquad
 d_1^*=Qm_s=\frac{4XQ^2d_2}{s^2},\qquad
 F_s(m_s)=\frac{XQd_2}{s},
\tag{162.CA9}
\]

and the literal cone gives

\[
 JQ\le s\le2JQ.
\tag{162.CA10}
\]

The exact profile substitution is

\[
 W\!\left(\sqrt{\frac{q_Xd_1^*}{4d_2}}\right)
 =W\!\left(\frac{XQ}{ys}\right).
\tag{162.CA11}
\]

Moreover

\[
 |F_s''(m_s)|^{-1/2}
 =\left(\frac{32XQd_2}{s^3}\right)^{1/2},
\]

and multiplication by the normalization in (162.CA2) gives

\[
 \left(\frac{L^2}{d_1^*d_2}\right)^{3/4}
 |F_s''(m_s)|^{-1/2}
 =\frac{2L^{3/2}J^{-1/2}}{Qd_2}.
\tag{162.CA12}
\]

The factor (i/2) in (162.CA7) and the negative Gaussian signature
(e(-1/8)) yield the leading unit (e(1/8)).  These equations identify
the literal reciprocal phase and all powers; they do not turn the
stationary principal family into a complete formula for rough endpoints.

The transform is exactly involutive on a suitable zero-extended test
function.  If (h(s)=\widehat g(s/4)), then

\[
 \widehat h(\xi)=4g(-4\xi),
\]

so two applications of (162.CA7) give

\[
 \left(\frac{i}{2}\right)^2 4
 \sum_{u\ \mathrm{odd}}\chi_4(u)g(-u)
 =\sum_{u\ \mathrm{odd}}\chi_4(u)g(u).
\tag{162.CA13}
\]

The Fourier reflection is cancelled by
(\chi_4(-u)=-\chi_4(u)).  A second bare character transform is
therefore an identity, not a contraction.

## 4. Rank-one product geometry and the scaled collar

For (f(x,z)=J\sqrt{xz}),

\[
 \operatorname{Hess}f=\frac J4
 \begin{pmatrix}
 -z^{1/2}x^{-3/2}&(xz)^{-1/2}\\
 (xz)^{-1/2}&-x^{1/2}z^{-3/2}
 \end{pmatrix},
 \qquad \det\operatorname{Hess}f=0,
\tag{162.CA14}
\]

and ((x,z)) is a null vector.  Hence the transform has one transverse
curvature direction and one radial Fourier direction.

After character Poisson in (m) and ordinary Poisson in (n), the
fixed-opening integral has phase

\[
 J\sqrt{QRmn}-\frac{s}{4}m-\ell n.
\tag{162.CA15}
\]

In physical variables

\[
 u=Qm=tw,\qquad v=Rn=t/w,
\]

the phase is

\[
 t\left(J-\frac{s}{4Q}w-\frac{\ell}{Rw}\right).
\tag{162.CA16}
\]

The angular stationary equations and the exact resonant product are

\[
 \frac{s}{4Q}=\frac J2\sqrt{\frac vu},\qquad
 \frac{\ell}{R}=\frac J2\sqrt{\frac uv},\qquad
 \boxed{s\ell=XQR}.
\tag{162.CA17}
\]

The cone becomes

\[
 Q\ell\le Rs\le4Q\ell.
\tag{162.CA18}
\]

For one compact smooth radial cell of physical length (R_0\asymp L),
the residual radial frequency is

\[
 \delta_{Q,R}(s,\ell)=J-\sqrt{\frac{s\ell}{QR}}.
\tag{162.CA19}
\]

The non-negligible central window
(|\delta_{Q,R}|\ll L^{-1}) is equivalent to

\[
 \boxed{|s\ell-XQR|\ll QRJ/L.}
\tag{162.CA20}
\]

There are

\[
 \ll_\varepsilon
 \left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon
\tag{162.CA21}
\]

dual factor pairs in this collar.  Transverse stationary phase gives
one smooth-interior coefficient the scale

\[
 \frac{L^{3/2}}{QR\sqrt J}.
\tag{162.CA22}
\]

Consequently, termwise positive summation on every fixed opening has the
same central capacity

\[
 \sqrt{JL}\,(XQR)^\varepsilon
 =L^{3/2}\frac{H+O(1)}{L}(XQR)^\varepsilon.
\tag{162.CA23}
\]

The (QR)-decay of one coefficient is exactly repaid by the width of its
rescaled product collar.  Positive summation over the opening triples is
therefore not licensed by a hidden (Q,R)-gain.

Grouping the smooth interior by (N=s\ell) gives the local divisor
window

\[
 \sum_{\substack{s\mid N,\ s\ \mathrm{odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi_4(s)\,\mathcal K_{Q,R}(N;s),
\tag{162.CA24}
\]

where (\mathcal K_{Q,R}) retains the actual saddle profiles and radial
Fourier weight.  For (Q=R=1), completing the divisor interval would
invoke

\[
 \sum_{s\mid N}\chi_4(s)=r_2(N)/4,
\tag{162.CA25}
\]

but (162.CA24) is only a moving near-square truncation.  Completion adds
the complementary window and returns to the already parked full-divisor
interface; it is not a bound for the literal local window.

The favorable unprojected/single-opening comparison is

\[
 \min\{L^2,\sqrt{JL}\}
 =L^{3/2}\min\{L^{1/2},H/L\}\,(1+o(1)).
\tag{162.CA26}
\]

This is a method-capacity comparison, not an upper or lower bound for the
complete physical Möbius sum.  It misses the target by a fixed power on
polynomial intermediate blocks and becomes merely target-scale at
(L\asymp H).  The exact physical scalar still has only the inherited
(L^{2+o(1)}) positive capacity.

## 5. Differencing and named-source seams

If both character arguments are odd, their separation is even and

\[
 \chi_4(d_1+2h)\chi_4(d_1)=(-1)^h,
\tag{162.CA27}
\]

which is constant in (d_1).  Standard Cauchy--van der Corput followed
by absolute values therefore removes the character rather than extracting
a new character saving.  The rank-one Hessian leaves the radial null
direction under two-variable differencing as well.  This parks only
standard positive differencing, not a new signed correlation theorem.

The source audit supplies the following route-specific conclusions.

1. Bombieri--Iwaniec's double large sieve requires separated coefficient
   vectors and charges absolute near-collision forms; the physical
   projector, ratio profile, shell, and hard cone are joint.
2. Even after granting fictitious cost-one coefficient separation,
   Kowalski--Robert--Wu Proposition 5 restores

   \[
    J^{1/8}L^{13/8}+L^{3/2}+L^{7/4}
    +J^{-1/2}L^{3/2},
   \tag{162.CA28}
   \]

   and Robert--Sargos Theorem 1 restores

   \[
    J^{1/4}L^{3/2}+L^{7/4}+L^{3/2}
    +J^{-1/2}L^{3/2}.
   \tag{162.CA29}
   \]

   Neither reaches (162.CA1) in the assigned range.
3. The audited Duke--Friedlander--Iwaniec, Bettin--Chandee, and
   Dong--Robles--Zeindler theorems concern modular-inverse phases with
   integral arithmetic parameters and separated coefficients.  The
   literal transform has the ordinary real reciprocal
   (e(XQd_2/s)), with arbitrary real (X) and a joint moving
   coefficient.  There is no literal target-strength substitution.

These are named-source no-matches only.  They do not exclude an
unexamined, future, or bespoke coefficient-sensitive theorem.

## 6. First open step and controls

The first affirmative step not proved in Round 162 is a bound of target
strength for the complete signed aggregate

\[
\begin{aligned}
 \frac{L^{3/2}}{\sqrt J}
 \sum_{a,b,c}
 \frac{\mu(a)\mu(b)\mu(c)\chi_4(Q)}{QR}
 \sum_{N\approx XQR}
 \sum_{\substack{s\mid N,\ s\ \mathrm{odd}\\
 \sqrt{QN/R}\le s\le2\sqrt{QN/R}}}
 \chi_4(s)\mathcal K_{Q,R}(N;s),
\end{aligned}
\tag{162.CA30}
\]

with the exact (Q=[a^2,c]), (R=[b^2,c]), arbitrary-real centre,
profiles, even-(d_2) branch, collar tails, hard boundaries, stars,
floors, and endpoint transitions retained before every positive norm.
Equivalently, a new theorem must recover the factor

\[
 \min\{L^{1/2},H/L\}
\tag{162.CA31}
\]

missed by the favorable coefficient-insensitive ledger.  The schematic
display (162.CA30) describes the smooth principal interface; it is not a
replacement for the omitted literal boundary owners.

The conductor independently reproduced:

- the sign in (162.CA7);
- the saddle, phase, (W)-argument, and normalization in
  (162.CA9)--(162.CA12);
- the Hessian determinant and radial null vector in (162.CA14);
- the rescaled product, cone, and collar in
  (162.CA17)--(162.CA20);
- the cancellation of the (QR)-powers in (162.CA21)--(162.CA23);
- the even-shift identity (162.CA27).

No numerical experiment is used as proof.

## 7. Proposed state effect

Subject to independent reviews, create one obstruction node:

`M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`.

It should depend on the accepted Round-137 product-fibre transform
self-return and the two Round-161 radical nodes.  Add it only as a
dependency and inconclusive evidence to the two open hard-TOP parents.
Do not add a reverse dependency into an accepted node.

Reject only the following stronger readings:

- the (t=1) target is proved;
- the positive collar capacity is physical mass or a lower bound;
- Möbius opening or divisor completion is free;
- a second character transform or standard differencing supplies a gain;
- every literal hard-edge family is already target-safe;
- the named source audit excludes all possible theorems;
- a (t=1) no-go closes any remaining few-point channel, hard TOP,
  M9--M2, M9, a bridge, or a global exponent.

The proposed terminal label is
`hard_top_t1_close_factor_bilinear_no_go`.
