# Literal pre-Möbius Mellin attack

## 1. Result

The intact squarefree/coprime coefficient series has the exact two-variable
factorization
\[
 D(s_1,s_2)=L(s_1,\chi _4)\zeta(s_2)G(s_1,s_2),
\]
with all odd-prime factors \(1+\chi _4(p)p^{-s_1}+p^{-s_2}\), the separate
factor \(1+2^{-s_2}\) at \(2\), and an Euler product \(G\) absolutely
convergent for \(\Re s_1,\Re s_2>1/2\).  A further exact factorization gives
the larger meromorphic continuation region and identifies every possible
singularity; in particular, a contour shift from \(\Re s_j>1\) to
\(\Re s_j=1/2+\eta\) crosses only the pole of \(\zeta(s_2)\) at \(s_2=1\).

There is a lawful, literal-value-preserving Mellin representation for the
full \(t=1\) scalar: interpolate the already evaluated lattice profile by
disjoint smooth cardinal cells.  This preserves every floor, half-open
endpoint, star value, and arbitrary real centre.  It is exact, but its
\(O(L^2)\) cell complexity gives no saving by itself.

The \(\zeta\)-pole has two materially different exact realizations.  In the
cardinal-cell realization it is target-safe by nonstationary oscillation in
the second physical variable.  In contrast, the exact half-integer
Perron/Stieltjes realization makes the same residue telescope to
\(\sum_{n,m}\rho(n)W(n,m)\).  It has no continuous variable in which to
integrate by parts and is not automatically target-safe.  Thus harmlessness
of the pole is representation-dependent, not a consequence of the formal
residue alone.

On \(\Re s_j=1/2+\eta\), put
\[
 t_+=t_1+t_2,\qquad t_-=t_1-t_2.
\]
For the favorable recombined smooth/BV capacity model, not for an
individual unit cardinal cell, the radial stationary set is
\[
 t_+=-2\pi Jr\asymp-JL,
\]
has length \(\asymp JL\), and the pointwise transform scale is
\[
 L^{1+2\eta}(JL)^{-1/2}
   =\sqrt{L/J}\,L^{2\eta}.
\]
Even if Lindelöf-strength pointwise estimates, or an optimistic fixed
\(t_-\) mean square, are granted for the arithmetic factors, absolute
integration restores
\[
 \sqrt{L/J}\,(JL)=\sqrt J\,L^{3/2},
\]
which is a factor \(\sqrt J\) above the required \(L^{3/2}\) scale.
Hard faces in such a BV model only add angular tails and cannot improve
this optimistic ledger.  The first missing mechanism is therefore a signed two-height
correlation between the stationary Mellin transform and
\(L(s_1,\chi _4)\zeta(s_2)G(s_1,s_2)\), saving \(\sqrt J\) over absolute
control.

No coefficient-, gamma-, endpoint-, and error-complete argument here shows
that applying the two separate functional equations or approximate
functional equations returns to Round 162.  The lawful comparison is
conditional and separate: if one deliberately reopens the original
squarefree/coprime projector exactly as in the accepted Round-162 kernel
and then invokes its positive Poisson calculation, its accepted collar has
capacity \(\sqrt{JL}\).  With
\[
 y=\lfloor J\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor=\sqrt J+O(1),
\]
the ratio to the target is
\[
 \frac{\sqrt J}{L}=\frac HL+O(L^{-1}).
\]
The new scoped no-go concerns unweighted pointwise absolute control and
the stated fixed-angular mean square followed by Cauchy in the favorable
smooth/BV Mellin model.  The already accepted reopened-projector positive
collar is only an additional route comparison.  Neither statement is a
universal no-go for a new signed two-height theorem.

The full target is therefore not proved for the polynomial intermediate
range.  The complete literal scalar is, however, owner-complete in the
already elementary polylogarithmic range: from the \(O(L^2X^{\epsilon/2})\)
absolute bound, \(L\le(\log X)^B\) gives
\[
 L^2X^{\epsilon/2}
 \ll_{B,\epsilon}L^{3/2}X^\epsilon.
\]
This uses an explicit relabelling of \(\epsilon\), includes all endpoints,
and does not promote the general K17a target.

## 2. Exact statement and hypotheses

Let
\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=\frac{X}{y^2},\qquad
 H=\left\lfloor yX^{-1/4}\right\rfloor
   =\sqrt J+O(1),
\]
and
\[
 1\ll L\ll H.
\]
Let \(a_{n,m}=\mathcal A_{L,X}(n,m)\) denote the literal \(t=1\) lattice
profile after its normalization, \(q_X\)-ratio profile,
\((H+1)\)-profile, all real-centre floors, half-open interval conventions,
star values, and zero cases have been evaluated.  Put
\[
 W(n,m)=a_{n,m}e(J\sqrt{nm}).
\]
Its support has
\(n,m\asymp L\), and its pointwise divisor-type losses are absorbed in
\(X^\epsilon\).  The full scalar is
\[
 \mathcal S_{L,1}
 =
 \sum_{\substack{n,m\ge1\\ n\ {\rm odd}\\ nm\ {\rm squarefree}}}
 \chi _4(n)a_{n,m}e(J\sqrt{nm}).
\]
Since \(nm\) is squarefree exactly when \(n,m\) are squarefree and
\((n,m)=1\), its arithmetic Dirichlet series is
\[
 D(s_1,s_2)
 =
 \sum_{\substack{n,m\ge1\\ n,m\ {\rm squarefree}\\ (n,m)=1\\ n\ {\rm odd}}}
 \frac{\chi _4(n)}{n^{s_1}m^{s_2}},
 \qquad \Re s_1,\Re s_2>1.
\]

The claims proved below are:

1. the exact local factors and the stated convergence and continuation of
   \(D\);
2. an exact endpoint-safe Mellin identity for \(\mathcal S_{L,1}\);
3. target-safety of the \(s_2=1\) residue for the cardinal-cell
   realization, but not automatically for the exact discrete
   Perron/Stieltjes realization;
4. the stationary scale and the \(\sqrt J\) deficit of unweighted
   pointwise absolute control or the stated fixed-angular mean square plus
   Cauchy, in the favorable recombined smooth/BV capacity model;
5. the conditional comparison obtained only by deliberately reopening the
   accepted Round-162 projector and then invoking its positive Poisson
   collar;
6. the elementary full-scalar bound in the fixed polylogarithmic \(L\)
   sector.

The resulting no-go has the label
\[
 \mathsf{t1\_mellin\_euler\_interface\_no\_go}.
\]
Its new Mellin scope is only the two absolute treatments in item 4.
Item 5 imports a separate accepted obstruction and is not a
functional-equation equivalence.  The no-go does not rule out a genuinely
signed joint transform estimate and asserts no result for any other
hard-TOP channel.

## 3. Proof or derivation

### 3.1 Exact Euler factors, including \(p=2\)

For an odd prime put
\[
 u_p=\chi _4(p)p^{-s_1},\qquad v_p=p^{-s_2}.
\]
Squarefreeness and coprimality allow the three choices: \(p\) divides
neither leg, only the first leg, or only the second leg.  Hence
\[
 D_p(s_1,s_2)=1+u_p+v_p\qquad(p\ {\rm odd}).
\]
The first leg is odd, so at \(p=2\) only the choices \(2\nmid m\) and
\(2\mid m\) occur:
\[
 D_2(s_1,s_2)=1+2^{-s_2}.
\]
Factoring \(L(s_1,\chi _4)\zeta(s_2)\) gives
\[
 G_2(s_1,s_2)=1-2^{-2s_2}
\]
and, at every odd prime,
\[
\begin{aligned}
 G_p(s_1,s_2)
  &=(1+u_p+v_p)(1-u_p)(1-v_p)\\
  &=1-u_p^2-v_p^2-u_pv_p+u_p^2v_p+u_pv_p^2.
\end{aligned}
\]
Thus
\[
 D(s_1,s_2)=L(s_1,\chi _4)\zeta(s_2)G(s_1,s_2)
\]
with
\[
 G=(1-2^{-2s_2})
 \prod_{p\ {\rm odd}}
 \left(1-u_p^2-v_p^2-u_pv_p+u_p^2v_p+u_pv_p^2\right).
\]
The nonconstant terms in \(G_p\) are bounded by a fixed multiple of
\[
 p^{-2\sigma _1}+p^{-2\sigma _2}
   +p^{-\sigma _1-\sigma _2}
\]
on compact subsets.  Therefore this product converges absolutely and
locally uniformly, and is holomorphic, for
\(\sigma _1,\sigma _2>1/2\).  Zeros of this product are possible; no
nonvanishing assertion is needed.

There is also a useful exact continuation.  Define
\[
 P_p=(1-u_p^2)(1-v_p^2)(1-u_pv_p),\qquad
 \mathcal H_p=G_p/P_p.
\]
Direct multiplication gives
\[
 G_p-P_p
 =
 u_p^2v_p+u_pv_p^2-u_p^3v_p-u_pv_p^3
 -u_p^2v_p^2+u_p^3v_p^3.
\]
Consequently \(\prod_{p\ {\rm odd}}\mathcal H_p\) converges absolutely in
\[
 \Omega=
 \left\{
 \sigma _1>0,\ \sigma _2>0,\
 2\sigma _1+\sigma _2>1,\
 \sigma _1+2\sigma _2>1
 \right\}.
\]
Including the prime \(2\) exactly, one obtains
\[
 G(s_1,s_2)=
 \frac{\mathcal H(s_1,s_2)}
 {(1-2^{-2s_1})\zeta(2s_1)\zeta(2s_2)
 L(s_1+s_2,\chi _4)}.
\]
This formula is meromorphic, not automatically holomorphic, throughout
\(\Omega\): zeros of the three denominator \(L\)-functions can create
poles.  The poles of \(\zeta(2s_j)\) instead give zeros of \(G\).
On a shift confined to \(\sigma_j\ge1/2+\eta\), all denominator arguments
remain in their zero-free absolute-convergence half-planes, and the direct
Euler product for \(G\) is already holomorphic.  Hence the only crossed
singularity of \(D\) is the simple pole of \(\zeta(s_2)\) at \(s_2=1\).

### 3.2 Literal endpoint-safe Mellin inversion

Choose once and for all
\(\psi\in C_c^\infty((-1/3,1/3))\) with \(\psi(0)=1\), and set
\[
 \mathcal B(x,z)
 =
 e(J\sqrt{xz})
 \sum_{n,m}a_{n,m}\psi(x-n)\psi(z-m).
\]
The sum is finite and the cell supports are disjoint.  At every positive
integer pair,
\[
 \mathcal B(n,m)=a_{n,m}e(J\sqrt{nm})=W(n,m).
\]
This identity uses the literal array itself; it neither rounds a real
centre nor replaces half-open or star conventions by continuous
surrogates.

Use the sign convention
\[
 \widehat{\mathcal B}(s_1,s_2)
 =
 \int_0^\infty\int_0^\infty
 \mathcal B(x,z)x^{s_1-1}z^{s_2-1}\,dx\,dz.
\]
Then
\[
 \mathcal B(x,z)
 =
 \frac1{(2\pi i)^2}
 \int_{(c_1)}\int_{(c_2)}
 \widehat{\mathcal B}(s_1,s_2)
 x^{-s_1}z^{-s_2}\,ds_2\,ds_1.
\]
For \(c_1,c_2>1\), absolute convergence and the finite support permit
summation under the integrals, giving the exact identity
\[
 \mathcal S_{L,1}
 =
 \frac1{(2\pi i)^2}
 \int_{(c_1)}\int_{(c_2)}
 \widehat{\mathcal B}(s_1,s_2)
 D(s_1,s_2)\,ds_2\,ds_1.
\]
The cardinal construction is an identity device, not a free smoothing
gain: it has \(O(L^2)\) unit cells, and taking their absolute values simply
returns the physical \(L^2X^\epsilon\) bound.

An exact half-integer Perron/Stieltjes construction gives a different
endpoint realization.  Initially for \(\Re s>1\), write
\[
 \sum_{n\ge1}\rho(n)n^{-s}=L(s,\chi _4)G(s,1).
\]
The local factors give the explicit coefficient
\[
 \rho(n)=
 \frac1{\zeta(2)}
 \mathbf 1_{\substack{n\ {\rm odd}\\n\ {\rm squarefree}}}
 \chi _4(n)\prod_{p\mid n}(1+p^{-1})^{-1}.
\]
For the exact mixed-difference convention of the half-integer formula,
telescoping at \(s_2=1\) gives, because \(m\asymp L\) and \(1\ll L\),
\[
 R_\zeta^{\rm St}
 =
 \sum_{\substack{n,m\ge1\\m\asymp L}}\rho(n)W(n,m).
\]
There is no lower \(m=1\) half-threshold correction in this range.  This
is an exact discrete weighted \(m\)-sum, not a continuous oscillatory
\(z\)-integral.  It supplies no integration by parts and has
\(L^2X^\epsilon\) absolute capacity.  No target-safe claim is made for
this residue without an additional discrete cancellation theorem.

### 3.3 Contour shift and the \(\zeta\)-residue

Fix \(\alpha=\beta=1/2+\eta\).  Shifting the two contours within the
holomorphic region of \(G\) gives
\[
\begin{aligned}
 \mathcal S_{L,1}
  =R_\zeta
  +\frac1{(2\pi)^2}\int_{\mathbb R^2}
  &\widehat{\mathcal B}(\alpha+it_1,\beta+it_2)\\
  &\times L(\alpha+it_1,\chi _4)
  \zeta(\beta+it_2)G(\alpha+it_1,\beta+it_2)
  \,dt_1dt_2,
\end{aligned}
\]
where
\[
 R_\zeta
 =
 \frac1{2\pi i}\int_{(\alpha)}
 \widehat{\mathcal B}(s_1,1)
 L(s_1,\chi _4)G(s_1,1)\,ds_1.
\]
There is no \(s_1\)-residue because \(L(s_1,\chi _4)\) is entire.
Equivalently, expanding on the initial absolute-convergence line and then
using Mellin inversion gives the exact cardinal residue
\[
 R_\zeta
 =
 \sum_{n\ge1}\rho(n)\int_0^\infty\mathcal B(n,z)\,dz,
\]
with \(\rho(n)\) as in Section 3.2.  No character identity forces this
expression to vanish.

For the cardinal-cell realization, \(R_\zeta\) is target-safe.  On every
cardinal cell the derivative of the physical phase in \(z\) is
\[
 \frac{\partial}{\partial z}\bigl(2\pi J\sqrt{xz}\bigr)
 =\pi J\sqrt{x/z}\asymp J.
\]
Repeated integration by parts in \(z\), followed by sufficiently many
integrations in \(x\) to control the polynomial vertical growth of
\(L(s_1,\chi _4)\), gives for each \(N\)
\[
 R_\zeta\ll_N L^{C_N}J^{-N}.
\]
The \(O(L^2)\) cells are included in \(C_N\), and since \(L\le J^{1/2}\),
\(N\) can be chosen so that this is \(O(L^{3/2}X^\epsilon)\).

The frequency explanation is consistent with this calculation but is not
a substitute for the endpoint audit.  At \(t_2=0\),
\[
 t_+=t_-=t_1.
\]
Radial stationarity would require \(t_1\asymp-JL\).  A favorable
recombined BV bulk would then be at large angular frequency as well.  A
unit cardinal cell has angular bandwidth \(O(L)\), not \(O(1)\), but
\(JL\) is still outside that bandwidth and the direct \(z\)-integration
above is the rigorous cardinal argument.  Delta masses in a Stieltjes
model have full angular frequency support, which is exactly why that
model does not inherit the same conclusion.

### 3.4 Radial and angular frequency ledger

This subsection is an optimistic capacity test for a favorable
recombined smooth profile, or for a parameter-uniform BV profile after
its jumps have been kept explicitly.  It is not the transform law of one
unit cardinal cell, and no unconstructed continuous interpolation of the
literal array is asserted.  The exact cardinal representation has
\(O(L^2)\) cells and different radial/angular bandwidths.

Put
\[
 x=rw,\qquad z=r/w.
\]
Since \(dx\,dz=2r\,dr\,dw/w\), the Mellin transform becomes
\[
 \widehat{\mathcal B}_{\rm sm}(s_1,s_2)
 =
 2\iint
 \widetilde{\mathcal A}_{\rm sm}(r,w)e(Jr)
 r^{s_1+s_2}w^{s_1-s_2}
 \,d\log r\,d\log w,
\]
where \(\widetilde{\mathcal A}_{\rm sm}\) denotes the favorable
recombined model profile.  On \(s_j=\sigma_j+it_j\), the oscillatory
phase in \(\log r\) is
\[
 2\pi Jr+t_+\log r.
\]
Its stationary equation and second derivative are
\[
 2\pi Jr+t_+=0,\qquad
 \frac{d^2}{d(\log r)^2}(2\pi Jr+t_+\log r)
 =2\pi Jr\asymp JL.
\]
As \(r\) traverses a dyadic interval \(r\asymp L\), the stationary
\(t_+\)-interval has length \(\asymp JL\).  On
\(\sigma_1=\sigma_2=1/2+\eta\), one-dimensional stationary phase for
this recombined model yields the capacity scale
\[
 \left|\widehat{\mathcal B}_{\rm sm}\right|
 \ \text{at stationary }t_+
 \asymp_{\rm scale}
 L^{\sigma_1+\sigma_2}(JL)^{-1/2}
 =
 \sqrt{L/J}\,L^{2\eta},
\]
up to the profile seminorm and the angular Fourier weight.  This is not
a lower bound and does not suppress those profile-dependent factors.  The
stationary phase itself is
\[
 \Phi(t_+)
 =
 t_+\left(\log\frac{-t_+}{2\pi J}-1\right).
\]

Grant, only for the purpose of testing capacity, the stronger-than-known
uniform estimate
\[
 \left|
 L(\alpha+it_1,\chi _4)\zeta(\beta+it_2)
 G(\alpha+it_1,\beta+it_2)
 \right|
 \ll X^\epsilon.
\]
Even with an \(O(1)\) angular range, absolute integration over the
stationary radial interval gives
\[
 \sqrt{L/J}\cdot JL\cdot X^\epsilon
 =
 \sqrt J\,L^{3/2}X^\epsilon.
\]
Likewise, grant an optimistic fixed-\(t_-\) arithmetic mean square of size
\[
 \int_{T}^{2T}
 \left|L\zeta G\right|^2\,dt_+
 \ll TX^\epsilon,\qquad T=JL,
\]
and use the radial Plancherel scale
\(\|\widehat{\mathcal B}_{\rm sm}\|_2\asymp_{\rm scale}L\).
Cauchy--Schwarz then gives
\[
 L\sqrt{JL}\,X^\epsilon
 =\sqrt J\,L^{3/2}X^\epsilon.
\]
This is not an invocation of Lindelöf or of an unproved hybrid moment:
it tests their capacity even if granted.  It does not rule out a
parameter-dependent weighted hybrid estimate that retains the sign of
\(\widehat{\mathcal B}_{\rm sm}\).  A BV jump gives a reciprocal
\(t_-\)-tail, so the optimistic bounded-angular calculation is already
the favorable case.

To reach \(L^{3/2}X^\epsilon\), the stationary asymptotic would require a
signed estimate of the schematic exact strength
\[
\begin{aligned}
 \int_{|t_+|\asymp JL}
 e^{i\Phi(t_+)}
 \mathscr A(t_+/J,t_-)
 &L\left(\alpha+i\frac{t_++t_-}{2},\chi _4\right)\\
 {}\times&
 \zeta\left(\beta+i\frac{t_+-t_-}{2}\right)
 G\left(\alpha+i\frac{t_++t_-}{2},
        \beta+i\frac{t_+-t_-}{2}\right)\,dt_+
 \ll \sqrt J\,L\,X^\epsilon,
\end{aligned}
\]
uniformly either for the exact cardinal-cell sum or for an independently
constructed endpoint-lawful profile with summable angular tails.  The
absolute capacity of the favorable model integral is \(JLX^\epsilon\),
so this is precisely a saving of \(\sqrt J\).  No such selector-,
endpoint-, and \(G\)-preserving theorem occurs in the supplied packet or
the independent source audit.

### 3.5 Conditional comparison with the accepted Round-162 collar

The one-variable character transform
\[
 \sum_m\chi _4(m)g(m)
 =
 \frac i2\sum_{\substack{s\in\mathbb Z\\s\ {\rm odd}}}
 \chi _4(s)\widehat g(s/4).
\]
is exact and has the accepted normalization.  This identity alone does
not show that separate functional equations or approximate functional
equations applied to
\(L(s_1,\chi _4)\zeta(s_2)G(s_1,s_2)\) return to the Round-162 kernel.
No coefficient bridge for \(G\), two-adic branch, gamma and main terms,
AFE lengths and remainders, or returned literal \(q_X\), \(H+1\), floor,
star, and endpoint profiles is derived here.  An exact
functional-equation/AFE self-return is therefore not established.

There is a narrower lawful comparison.  If one deliberately leaves the
intact Mellin route and reopens the original projector by the accepted
identity
\[
 \mu^2(d_1)\mu^2(d_2)\mathbf1_{(d_1,d_2)=1}
 =
 \sum_{a^2\mid d_1}\mu(a)
 \sum_{b^2\mid d_2}\mu(b)
 \sum_{c\mid(d_1,d_2)}\mu(c),
\]
with \(Q=[a^2,c]\), \(R=[b^2,c]\), then the already accepted physical
character/ordinary Poisson calculation supplies the dual phase
\[
 J\sqrt{QRmn}-\frac{s m}{4}-\ell n
\]
and the conditions
\[
 s\ell=XQR,\qquad Q\ell\le Rs\le4Q\ell,\qquad
 |s\ell-XQR|\ll QRJ/L.
\]
In that accepted opened calculation, one dual coefficient has scale
\[
 \frac{L^{3/2}}{QR\sqrt J},
\]
and positive counting has capacity
\[
 \frac{L^{3/2}}{QR\sqrt J}
 \left(\frac{QRJ}{L}+1\right)X^\epsilon
 \asymp\sqrt{JL}\,X^\epsilon
\]
in the adverse range.  Since the literal parameter satisfies
\[
 \frac{\sqrt{JL}}{L^{3/2}}
 =\frac{\sqrt J}{L}
 =\frac HL+O(L^{-1}),
\]
this is target-adverse for polynomial intermediate \(L<H\).  It is a
capacity calculation, not a lower bound for physical mass and not a full
upper bound.  It is an imported obstruction for the deliberately reopened
positive-Poisson route, not an equivalence between the intact Mellin
functional equations and the Round-162 kernel.

### 3.6 Full scalar, residual connector, and the polylogarithmic sector

The accepted exact decomposition is
\[
 \mathcal S_{L,1}
 =
 \mathcal S^{\rm cp}_{L,1}
 +
 \mathcal S^{\rm rem}_{L,1},
\qquad
 \mathcal S^{\rm cp}_{L,1}\ll_\kappa L^{3/2}.
\]
Thus a full-scalar target would imply, only by exact subtraction,
\[
 |\mathcal S^{\rm rem}_{L,1}|
 \le
 |\mathcal S_{L,1}|+|\mathcal S^{\rm cp}_{L,1}|
 \ll L^{3/2}X^\epsilon.
\]
The converse requires the same exact addition.  No other parent follows.

For completeness, the literal array has \(O(L^2)\) entries of
divisor-type size, whence
\[
 \mathcal S_{L,1}\ll L^2X^{\epsilon/2}.
\]
If \(L\le(\log X)^B\), then
\[
 L^{1/2}\le(\log X)^{B/2}\ll_{B,\epsilon}X^{\epsilon/2},
\]
so
\[
 \mathcal S_{L,1}\ll_{B,\epsilon}L^{3/2}X^\epsilon.
\]
This is an explicit \(\epsilon/2\mapsto\epsilon\) relabelling, not a
uniform polynomial-range improvement.

## 4. First doubtful or unproved step

The first genuinely unproved step is the signed stationary two-height
estimate displayed in Section 3.4, with all of the following retained
simultaneously:

- the exact literal transform rather than a majorant;
- the factor \(G(s_1,s_2)\) rather than a termwise Möbius expansion;
- the stationary phase \(e^{i\Phi(t_+)}\);
- the full cardinal-cell sum, or a separately proved endpoint-lawful
  profile with quantified BV/angular tails;
- uniformity in arbitrary real centres, their floors, and star values.

Call this missing interface
\(\mathsf{SMEH}_{L,J}\).  It must save \(\sqrt J\) relative to the
absolute \(t_+\)-length \(JL\).  Pointwise Lindelöf, a fixed-angular
mean square plus Cauchy--Schwarz, and the separately accepted positive
product-collar count do not imply it.

Accordingly the no-go is terminal only for:

1. the favorable recombined smooth/BV Mellin capacity model followed by
   unweighted pointwise absolute control; and
2. that same model followed by the stated fixed-angular mean square and
   Cauchy--Schwarz.

Separately, deliberately reopening the accepted projector and then using
positive Poisson invokes the already accepted Round-162 collar
obstruction.  This is not part of the newly proved Mellin no-go, and
factorwise functional equations or AFEs are not asserted to return to it.

It is not terminal for a future theorem proving
\(\mathsf{SMEH}_{L,J}\), and it is not a claim that the physical sum itself
has size \(\sqrt{JL}\) or \(\sqrt J\,L^{3/2}\).

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| literal_full_t1_scalar_and_xor_connector | PASS.  The analyzed object is the full literal scalar, and the only residual consequence is the exact XOR subtraction in Section 3.6. |
| exact_Euler_local_factors_including_p2 | PASS.  Odd factors are \(1+\chi _4(p)p^{-s_1}+p^{-s_2}\); the factor at \(2\) is \(1+2^{-s_2}\), producing \(G_2=1-2^{-2s_2}\). |
| G_absolute_convergence_and_singularities | PASS.  Direct absolute convergence for \(\sigma_j>1/2\), the exact continuation through \(\mathcal H\), and all possible denominator-zero poles are distinguished. |
| Mellin_sign_normalization_and_exact_inversion | PASS.  The forward powers are \(x^{s_1-1}z^{s_2-1}\), the inverse powers are \(x^{-s_1}z^{-s_2}\), and the resulting \(D(s_1,s_2)\) has the correct signs. |
| hard_half_open_profile_BV_endpoints | PASS FOR THE EXACT CARDINAL MODEL.  Cardinal cells preserve every literal value.  No unconstructed natural-continuous-plus-atoms claim remains. |
| zeta_pole_and_residue | PASS WITH REPRESENTATION QUALIFICATION.  The cardinal residue is target-safe; the exact Stieltjes residue is \(\sum_{n,m}\rho(n)W(n,m)\) and is not declared small. |
| radial_angular_frequency_support | PASS AS A CAPACITY MODEL.  For the favorable recombined smooth/BV model, \(t_+=-2\pi Jr\asymp-JL\) and \(t_-=t_1-t_2\); this scale is not assigned to a unit cardinal cell. |
| full_transform_length_and_tail | PASS WITH MODEL SCOPE.  The favorable radial stationary interval has length \(JL\); a BV jump has a reciprocal angular tail, while the exact cardinal transform retains all \(O(L^2)\) cells. |
| no_absolute_hybrid_moment_inflation | PASS WITH NARROW SCOPE.  Optimistic unweighted pointwise control and the stated fixed-angular mean square plus Cauchy each restore \(\sqrt J\,L^{3/2}\); no weighted signed hybrid estimate is ruled out. |
| functional_equation_AFE_self_return | NOT ESTABLISHED / NARROWED.  Separate FEs or AFEs are not identified with Round 162; gamma, coefficient, main-term, error, two-adic, and literal-profile bridges remain missing. |
| round162_product_collar_comparison | PASS CONDITIONALLY.  Deliberately reopening the accepted projector and then invoking its accepted positive Poisson calculation gives the imported coefficient, pair-count, and \(\sqrt{JL}\) capacity. |
| arbitrary_real_centre_floors_and_stars | PASS.  These are evaluated before cardinal interpolation and are not replaced by symmetric or integer-centred surrogates. |
| target_L_three_halves_power_ledger | PASS.  The target, the favorable absolute Mellin loss \(\sqrt J\), the exact collar ratio \(\sqrt J/L=H/L+O(L^{-1})\), and the fixed-\(B\) polylogarithmic epsilon relabelling are explicit. |
| downstream_scope_and_no_exponent_promotion | PASS.  Only the full-to-residual XOR connector is stated; no parent or exponent is promoted. |
| no_in_round_pivot | PASS.  The report remains on the frozen pre-Möbius Mellin/Euler interface. |
| maximal_K26_quarantine | PASS.  No maximal-\(t\), K26, or shifted-supremum input is used or inferred. |

## 6. Dependencies and exact artifacts used

Only the files authorized by the generated brief were used:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md;
- proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md;
- strategy/round168_m2_hard_top_t1_pre_mobius_mellin_euler_strategy.md;
- rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/barrier_packet.md;
- rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/briefs/literal_pre_mobius_mellin_attack.md;
- rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reviews/claimant_math_endpoint_power_review.md;
- rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reports/hybrid_zeta_l_source_hostile_audit.md.

No new external search, numerical experiment, or shared-state edit was
made in this repair.  The independent source audit was used only for its
audited interface conclusions.  The Euler identities, continuation,
Mellin normalization, cardinal residue, stationary powers, and conditional
collar comparison are stated at their proved scopes.

## 7. Recommended state effect

**RETAIN / NO GENERAL PROMOTION.**

Retain as proved interface facts:

1. the exact local Euler factors, including \(p=2\);
2. the direct half-plane of absolute convergence and the factored
   meromorphic continuation of \(G\);
3. the endpoint-exact cardinal Mellin identity;
4. the representation-dependent residue audit, including target-safety
   for the cardinal realization and the absence of such a conclusion for
   the exact Stieltjes sum;
5. the favorable recombined smooth/BV capacity scale
   \(\sqrt{L/J}\) over length \(JL\), explicitly not a unit-cardinal-cell
   transform law;
6. the scoped no-go
   \(\mathsf{t1\_mellin\_euler\_interface\_no\_go}\);
7. the owner-complete fixed-polylogarithmic-\(L\) sector with explicit
   epsilon relabelling.

Do not promote K17a, its residual child, either direct \(M_1\) parent, any
hard-TOP/BAL/UNBAL/GAR/endpoint parent, or any exponent claim.  A future
round could return to this route only with a precisely stated
\(\mathsf{SMEH}_{L,J}\)-type signed correlation theorem and an
endpoint-lawful transform with quantified parameter dependence.  The
separate factorwise FE/AFE route remains unproved; deliberately reopening
the accepted projector merely invokes the already accepted positive
collar obstruction.
