# Round 162 statement-only blind rederivation: the close-factor scalar

## 1. Result

**Result: exact scoped no-go result, not a proof of (162.BL2) and not a
physical lower bound.**  Character-preserving Poisson summation can be
carried out without losing the sign of \(\chi _4\).  It sends the
\(d_1\)-character back to a \(\chi _4\)-character on an odd dual variable,
with the following orientation:

\[
 \chi _4(d_1)e(J\sqrt{d_1d_2})
 \quad\leadsto\quad
 e(1/8)\chi _4(m)e(Xd_2/m),\qquad m>0\text{ odd}.
\]

For a smooth component of the literal amplitude, the saddle is

\[
 d_{1,m}=\frac{4Xd_2}{m^2},\qquad J\le m\le 2J,
\]

and the factor \((L^2/(d_1d_2))^{3/4}\) cancels the \(m^{\pm3/2}\)
powers in the stationary-phase Jacobian.  The exact leading transformed
coefficient is

\[
 e(1/8)\chi _4(m)\frac{L^{3/2}X^{-1/4}}{d_2}
\]

times the literal profiles evaluated at the saddle.  In particular,

\[
 W\!\left(\sqrt{\frac{q_Xd_{1,m}}{4d_2}}\right)
 =W\!\left(\frac{X}{ym}\right),
\]

so neither \(q_X\) nor its floor dependence is discarded.

The two-variable phase is not genuinely curved.  Its Hessian has rank
one and radial null vector \((d_1,d_2)\).  After the character shift, the
stationary equations are

\[
 r=k-\frac{\sigma}{4},\qquad
 r=\frac J2\sqrt{\frac{d_2}{d_1}},\qquad
 \ell=\frac J2\sqrt{\frac{d_1}{d_2}},\qquad
 r\ell=\frac X4.
\]

Writing \(m=4r=4k-\sigma\), they become

\[
 m\ell=X,\qquad J\le m\le2J,qquad J/2\le\ell\le J.
\]

The finite radial support broadens this hyperbola to

\[
 |m\ell-X|\ \lesssim\ \frac JL.
\]

There are at most \((J/L+1)X^{\varepsilon}\) coefficient slots in this
central collar.  A single dual slot has stationary integral capacity
\(L^{3/2}J^{-1/2}\).  Thus taking a positive norm at this collar gives

\[
 B_{\mathrm{collar}}\ \lesssim_\varepsilon\
 \sqrt{JL}\,X^\varepsilon
 =X^{1/4}L^{1/2}X^\varepsilon.
\]

Since \(H=X^{1/4}+O(1)\), this exceeds the requested
\(L^{3/2}X^\varepsilon\) by the factor \(H/L\) away from the top scale.
Combining it with the original positive capacity \(L^2X^\varepsilon\)
leaves the exact coefficient-insensitive ledger

\[
 \min\{L^2,\sqrt{JL}\}
 =L^{3/2}\min\{L^{1/2},H/L\}\,(1+O(H^{-1})).
\]

The crossover is \(L\asymp J^{1/3}\asymp H^{2/3}\).  Hence the original
positive norm misses the target by \(L^{1/2}\), while Poisson followed by
a positive dual norm misses it by \(H/L\) in the range where that is the
better of the two bounds.  At \(L\asymp H\) the smooth unprojected collar
ledger is of target size, but this does not by itself handle the actual
squarefree/coprime projector or the literal hard pieces.

Opening squarefreeness and coprimality does not repair the power.  Each
rescaled Mobius term has a collar of width \(JAB/L\), a per-slot factor
\(L^{3/2}/(AB\sqrt J)\), and therefore the same positive capacity
\(\sqrt{JL}\); the \(AB\) factors cancel.  Summing the opening parameters
absolutely consequently introduces an additional unsummable
multiplicity.  Differencing is also coefficient-blind: every nonzero
\(d_1\)-correlation has even shift \(h\) and
\(\chi _4(d_1+h)\chi _4(d_1)=(-1)^{h/2}\), a constant in \(d_1\).

Thus character-preserving Poisson correctly isolates, but does not prove,
the needed estimate.  Closure requires a new literal coefficient-sensitive
bound for the signed dual collar, retaining \(\chi _4\), all Mobius signs,
and all profile and endpoint factors before any positive norm.  No such
bound follows from the statement-only packet.  The calculation is a
method obstruction: it does not assert that the physical sum is as large
as \(\sqrt{JL}\).

## 2. Exact statement and hypotheses

Let \(X\) be a sufficiently large positive real number and retain exactly

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=\frac X{y^2},\qquad
 H=\left\lfloor yX^{-1/4}\right\rfloor.
\]

Then

\[
 q_X=1+O(J^{-1}),\qquad H=\sqrt J+O(1)=X^{1/4}+O(1),
\]

but all formulas below use the exact \(q_X,y,H\), not these
approximations.  Let \(1\ll L\ll H\), and let the original summation set,
half-open convention, cone, profiles, endpoint values, and zero extensions
be exactly those in (162.BL1).  No lower bound for \(\eta_L,\Phi\), or
\(W\) is assumed.

There are two levels to the no-go statement.

1. The coefficient grouping, parity identities, character algebra,
   Hessian, stationary equations, saddle values, dual hyperbola, and
   rescaling formulas below are exact consequences of (162.BL1).
2. The stationary-phase size and rapid decay assertions apply to one
   compact smooth component whose derivatives at order \((i,j)\) are on
   their literal support scales.  A finite-piece bounded-variation
   component gives the same central-collar power after its nonzero hard
   endpoints are peeled off and handled in the primal variables.  The
   statement-only packet does not specify derivative norms, the number of
   profile entry/exit pieces, or endpoint values, so these analytic
   hypotheses cannot be certified for the named profiles from the packet
   alone.

The scoped no-go proposition is the following.  Suppose a proof applies
one- or two-variable Poisson summation to such components and then bounds
every coefficient in a dual product collar by its magnitude, using only
support length, stationary phase, and the divisor bound.  Then its central
two-variable contribution is bounded at the power
\(\sqrt{JL}X^\varepsilon\), not at
\(L^{3/2}X^\varepsilon\), unless \(L\) is comparable to \(H\).  The same
power survives every fixed Mobius rescaling, and an absolute sum over the
opening parameters is worse.  This proposition says that this proof
architecture does not establish (162.BL2); it does not rule out a signed
collar theorem, a different coefficient-sensitive argument, or additional
cancellation in the physical scalar.

## 3. Proof or derivation

**(a) Literal coefficient, orientation, and parity.**  For positive
integers \(d_1,d_2\),

\[
 d_1,d_2\text{ squarefree and }(d_1,d_2)=1
 \quad\Longleftrightarrow\quad
 \mu^2(d_1d_2)=1.
\]

Consequently, with \(n=d_1d_2\), (162.BL1) has the exact product grouping

\[
 \mathcal S_{L,1}
 =\sum_{n\asymp L^2}\mu^2(n)
 \left(\frac{L^2}{n}\right)^{3/4}e(J\sqrt n)\,b_L(n),
\]

where

\[
 \begin{aligned}
 b_L(n)=\sum_{\substack{d\mid n,\ d\ {
m odd}\\
                         \sqrt n\le d\le2\sqrt n}}
 &\chi _4(d)\eta_L(d)\Phi\!\left(\frac d{H+1}\right)\\
 &\times W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt n}\right).
 \end{aligned}
\]

Here \(d=d_1\) and \(n/d=d_2\).  This verifies the direction of both cone
inequalities and puts \(\chi _4\) on \(d_1\), not on \(d_2\).  The factor
\((L^2/n)^{3/4}\) is positive and of order one on the displayed block.
Thus the coefficient-uniform capacity is \(L^{2+o(1)}\), and the target
requires an arithmetic signed saving of \(L^{1/2-o(1)}\).

The condition that \(d_1\) is odd does not imply that \(d_2\) is odd.  If
\(n\) is even, squarefreeness forces the single factor 2 into \(d_2\),
because \(d_1=d\) is odd.  Equivalently the even sector is
\(d_2=2d_2'\), with \(d_2'\) odd and squarefree and
\((d_1,d_2')=1\).  It remains present in every formula below; imposing an
odd condition on the second variable would delete a genuine branch.

The literal cone endpoints cause no physical lattice row at this scale.
The equality \(d_1=d_2\), together with coprimality, forces
\(d_1=d_2=1\), outside \(L\gg1\).  The equality \(d_1=4d_2\) contradicts
the oddness and squarefreeness of \(d_1\).  This does not remove the need
to retain cone endpoint terms after a Mobius opening, because individual
opened terms no longer have these projector cancellations.

For comparison only, if the close-factor and profile restrictions are
removed, then for squarefree \(n\)

\[
 \sum_{\substack{d\mid n\\d\ {
m odd}}}\chi _4(d)
 =\prod_{\substack{p\mid n\\p\ {
m odd}}}(1+\chi _4(p)).
\]

This is zero when an odd prime \(p\equiv3\pmod4\) divides \(n\), and is
\(2^{\omega(n_{
m odd})}\) otherwise.  In particular it is nonnegative,
not a generic random-sign divisor coefficient.  The identity is used only
as a diagnostic against an unjustified mean-zero heuristic; the actual
close-factor/profile coefficient is incomplete and is not replaced by
this full divisor sum.

**(b) Exact additive character decomposition and one-variable
self-return.**  Let \(a(x,z)\) denote a compact component of the literal
amplitude, zero extended away from positive \(x,z\).  With the convention
\(e(t)=e^{2\pi it}\),

\[
 \chi _4(n)=\frac{e(n/4)-e(-n/4)}{2i}
 =\frac1{2i}\sum_{\sigma=\pm1}\sigma e(\sigma n/4).
\]

Poisson summation in \(n\) gives

\[
 \begin{aligned}
 &\sum_{n\in\mathbb Z}\chi _4(n)a(n,z)e(J\sqrt{nz})\\
 &\quad=\frac1{2i}\sum_{\sigma=\pm1}\sigma
       \sum_{k\in\mathbb Z}
       \int_0^\infty a(x,z)
       e\!\left(J\sqrt{xz}-\left(k-\frac\sigma4\right)x\right)dx.
 \end{aligned}
\]

Put

\[
 r=k-\frac\sigma4,\qquad m=4r=4k-\sigma.
\]

For \(\sigma=1\), \(m\equiv3\pmod4\), whereas for \(\sigma=-1\),
\(m\equiv1\pmod4\).  In both cases \(\sigma=-\chi _4(m)\).  The two
shifted lattices therefore combine exactly to

\[
 \boxed{
 \sum_n\chi _4(n)a(n,z)e(J\sqrt{nz})
 =-\frac1{2i}\sum_{\substack{m\in\mathbb Z\\m\ {
m odd}}}
 \chi _4(m)\int_0^\infty a(x,z)
 e\!\left(J\sqrt{xz}-\frac m4x\right)dx.}
\]

Thus the character is preserved before any positive norm.  Modes
\(m\le0\) have no interior saddle.  For \(m>0\), the stationary equation
and saddle phase are

\[
 x_m=\frac{4Xz}{m^2}=\frac{Xz}{4r^2},\qquad
 J\sqrt{x_mz}-\frac m4x_m=\frac{Xz}{m}=\frac{Xz}{4r}.
\]

Moreover

\[
 \frac{\partial^2}{\partial x^2}J\sqrt{xz}\bigg|_{x=x_m}
 =-\frac{m^3}{32Xz},
\qquad
 |f_{xx}(x_m,z)|^{-1/2}
 =\left(\frac{32Xz}{m^3}\right)^{1/2}.
\]

The negative quadratic direction contributes the stationary signature
\(e(-1/8)\).  Write the original smooth amplitude as

\[
 a(x,z)=\left(\frac{L^2}{xz}\right)^{3/4}p(x,z),
\]

where \(p\) includes the literal cone and profiles on the component.  At
the saddle there is the exact cancellation

\[
 \left(\frac{L^2}{x_mz}\right)^{3/4}
 \left(\frac{32Xz}{m^3}\right)^{1/2}
 =\frac{2L^{3/2}X^{-1/4}}{z}.
\]

Combining this factor, \(-1/(2i)\), and \(e(-1/8)\), the leading
one-variable transform is

\[
 \boxed{
 e(1/8)L^{3/2}X^{-1/4}
 \sum_{\substack{m>0\\m\ {
m odd}}}\chi _4(m)
 \frac{p(4Xz/m^2,z)}{z}\,e(Xz/m).}
\]

The sign and phase are both positive as displayed.  At the saddle, the
ratio profile is exactly

\[
 W\!\left(\sqrt{\frac{q_Xx_m}{4z}}\right)
 =W\!\left(\frac{\sqrt{q_XX}}m\right)
 =W\!\left(\frac X{ym}\right).
\]

On the literal cone \(1\le x_m/z\le4\), this saddle exists only for

\[
 J\le m\le2J,
\]

up to further trimming by the literal profiles.  Equivalently
\(J/4\le r\le J/2\).  No replacement of the profile endpoints
\(W(\sqrt{q_X}/2)\) and \(W(\sqrt{q_X})\) by interior values is justified.

**(c) Rank-one geometry and the two-variable dual hyperbola.**  For

\[
 f(x,z)=J\sqrt{xz},
\]

one has

\[
 \nabla^2 f=\frac J4
 \begin{pmatrix}
 -z^{1/2}x^{-3/2}&(xz)^{-1/2}\\
 (xz)^{-1/2}&-x^{1/2}z^{-3/2}
 \end{pmatrix},
\qquad \det\nabla^2f=0.
\]

Euler homogeneity gives

\[
 (\nabla^2f)(x,z)^T=0.
\]

Thus the radial direction is exactly null; the other eigenvalue is
negative.  Adding the linear character and Poisson frequencies does not
change the Hessian.  Direct two-variable Poisson gives oscillatory
integrals with phase

\[
 \Psi_{m,\ell}(x,z)=J\sqrt{xz}-\frac m4x-\ell z.
\]

Its stationary equations are

\[
 \frac m4=\frac J2\sqrt{\frac zx},\qquad
 \ell=\frac J2\sqrt{\frac xz},
\]

and therefore

\[
 \boxed{m\ell=X.}
\]

In the original \((k,\sigma)\) notation this is
\((k-\sigma/4)\ell=X/4\).  On the cone the dual ranges are

\[
 J\le m\le2J,qquad J/2\le\ell\le J.
\]

When \(m\ell=X\), every point on the admissible radial ray is critical,
and Euler's identity gives \(\Psi_{m,\ell}=0\) on that ray.  When
\(m\ell\ne X\), there is no two-dimensional critical point.  This is a
clean one-dimensional critical manifold, not an isolated two-dimensional
saddle.

Sequentially, after the nondegenerate transverse \(x\)-saddle the
remaining phase is

\[
 \left(\frac Xm-\ell\right)z.
\]

If a literal radial component has length \(R\le C L\), its central Fourier
collar is

\[
 \left|\frac Xm-\ell\right|\lesssim\frac1R,
 \qquad\text{equivalently}\qquad
 |m\ell-X|\lesssim\frac JR.
\]

For the full-length component \(R\asymp L\), this is the claimed dual
product collar of width \(J/L\).  Shrinking a profile support cannot be
counted as a free gain: it reduces a single radial integral by \(R/L\)
but broadens the collar from \(J/L\) to \(J/R\).

For a dyadic collar \(R|X/m-\ell|\asymp T\), the integer
\(p=m\ell\) lies in an interval of length \(O(JT/R)\) around the real
number \(X\).  Each positive integer \(p\asymp X\) has at most
\(\tau(p)\ll_\varepsilon X^\varepsilon\) admissible factorizations.
Hence

\[
 N(T)\ll_\varepsilon (JT/R+1)X^\varepsilon.
\]

A smooth radial Fourier integral is at most
\(R\sqrt{L/J}(1+T)^{-A}\): the factor \(\sqrt{L/J}\) is the transverse
stationary scale.  Taking \(A>2\) and summing dyadic collars yields

\[
 \sum_{m,\ell}|\text{dual coefficient}|
 \ll_\varepsilon \sqrt{JL}\,X^\varepsilon.
\]

For \(R=L\), the central calculation is especially transparent:

\[
 \#\{(m,\ell)\}_{\rm collar}\ll_\varepsilon\frac JL X^\varepsilon,
 \qquad
 |\text{one slot}|\ll\frac{L^{3/2}}{\sqrt J},
\]

whose product is \(\sqrt{JL}X^\varepsilon\).

**(d) Restored power ledger.**  The exact scale relations are

\[
 J=X^{1/2},\qquad \sqrt J=X^{1/4}=H+O(1),\qquad L\le C H.
\]

Thus

\[
 \sqrt{JL}=X^{1/4}L^{1/2}
 =L^{3/2}\frac{X^{1/4}}L
 =L^{3/2}\left(\frac HL+O(L^{-1})\right).
\]

The original positive capacity and the Poisson-collar capacity therefore
give, respectively,

\[
 \frac{L^2}{L^{3/2}}=L^{1/2},
 \qquad
 \frac{\sqrt{JL}}{L^{3/2}}=\frac{\sqrt J}{L}\asymp\frac HL.
\]

The better coefficient-insensitive ledger misses the target by
\(\min(L^{1/2},H/L)\).  This is a genuine power for blocks below the top;
it cannot be put into \(X^\varepsilon\) uniformly in \(L\).  At
\(L\asymp H\), the smooth collar mass is of target order, but this fact
does not supply the arithmetic-projector or hard-endpoint analysis needed
for the physical scalar.

To close the unscaled collar one would need, after normalizing the
per-slot stationary factor, an estimate of the schematic literal form

\[
 \boxed{
 \sum_{\substack{m\asymp J,\ \ell\asymp J\\m\ {
m odd}\\
                   |m\ell-X|\lesssim J/L}}
 \chi _4(m)\,\mathcal C_{m,\ell}(X,L)
 \ll_\varepsilon \sqrt J\,X^\varepsilon,}
 \tag{*}
\]

where \(\mathcal C_{m,\ell}\) must retain the actual saddle profiles,
radial Fourier phases, endpoint transitions, and arithmetic projector.
The positive mass on the left is \(J/L\); hence (*) must save the factor
\(\sqrt J/L\asymp H/L\).  Arbitrary bounded coefficients cannot satisfy
(*): choosing them to cancel \(\chi _4(m)\) gives the positive mass.
Therefore a theorem capable of closing the gap must be literal and
coefficient-sensitive.

**(e) Squarefree/coprime opening and rescaled supports.**  The exact
projector identity is

\[
 \begin{aligned}
 &\mu^2(d_1)\mu^2(d_2)1_{(d_1,d_2)=1}\\
 &\quad=\sum_{a^2\mid d_1}\mu(a)
          \sum_{b^2\mid d_2}\mu(b)
          \sum_{c\mid(d_1,d_2)}\mu(c).
 \end{aligned}
\]

For a nonzero term put

\[
 A=[a^2,c]=\frac{a^2c}{(a,c)},\qquad
 B=[b^2,c]=\frac{b^2c}{(b,c)},\qquad
 d_1=Au,quad d_2=Bv.
\]

Because \(d_1\) is odd, \(a,c,A,u\) are odd.  There is no corresponding
odd restriction on \(b,B,v\); in particular the even \(d_2\) branch is
not deleted.  Complete multiplicativity on odd integers gives
\(\chi _4(Au)=\chi _4(A)\chi _4(u)\).  The rescaled support has

\[
 u\asymp L/A,\qquad v\asymp L/B,qquad
 Bv\le Au\le4Bv.
\]

Poisson summation in \(u\) has saddle

\[
 u_m=\frac{4XABv}{m^2},\qquad
 \text{phase}=\frac{XABv}{m},
\]

and the exact leading coefficient, including character orientation, is

\[
 \begin{aligned}
 e(1/8)\mu(a)\mu(b)\mu(c)\chi _4(A)\chi _4(m)
 \frac{L^{3/2}X^{-1/4}}{ABv}\quad\quad\\
 \times\eta_L\!\left(\frac{4XA^2Bv}{m^2}\right)
 \Phi\!\left(\frac{4XA^2Bv}{m^2(H+1)}\right)
 W\!\left(\frac{AX}{ym}\right)
 e\!\left(\frac{XABv}{m}\right).
 \end{aligned}
\]

The cone gives

\[
 JA\le m\le2JA,qquad JB/2\le\ell\le JB,
\]

and second Poisson gives the rescaled hyperbola and collar

\[
 m\ell=XAB,qquad
 |m\ell-XAB|\lesssim\frac{JAB}{L}.
\]

One full radial dual slot has size

\[
 \frac{L^{3/2}}{AB\sqrt J},
\]

whereas its product collar has at most

\[
 \frac{JAB}{L}(XAB)^\varepsilon
\]

factor slots.  Their product is again

\[
 \sqrt{JL}\,(XAB)^\varepsilon.
\]

Thus the support shrinkage and the stationary coefficient do not make the
Mobius parameters absolutely summable: the factor \(AB\) in the collar
width exactly repays the factor \((AB)^{-1}\) in a single transformed
coefficient.  Summing different \((a,b,c)\) after positive norms loses
their multiplicity.  A useful theorem must instead retain the
\(\mu(a)\mu(b)\mu(c)\chi _4(A)\chi _4(m)\) signs jointly.

The usual positive tail estimates do not create a hidden saving.  For
example, before oscillation,

\[
 \sum_{a>D}\#\{d_1\asymp L:a^2\mid d_1\}\,L
 \ll \frac{L^2}{D}+L^{3/2},
\]

and similarly for \(b\), while

\[
 \sum_{c>D}\#\{d_1\asymp L:c\mid d_1\}
                \#\{d_2\asymp L:c\mid d_2\}
 \ll \frac{L^2}{D}+L\log L+L.
\]

Taking \(D\asymp\sqrt L\) makes these tails no larger than the target,
but the remaining opened core has no decaying \(A,B\) factor after its
dual collar is counted.  This is an opening obstruction, not a proof that
the projector itself is harmful.

If the even physical sector is isolated first by \(d_2=2d_2'\), then its
rescaling has \(B=2\), phase \(J\sqrt{2d_1d_2'}\), and dual product
\(m\ell=2X\).  Its collar and power ledger are the same up to constants;
it cannot be omitted.

**(f) Differencing and the absent bilinear input.**  If both \(d_1\) and
\(d_1+h\) are odd, then \(h\) is even and

\[
 \chi _4(d_1+h)\chi _4(d_1)=(-1)^{h/2},
\]

independent of \(d_1\).  If \(h\) is odd, the two odd supports do not
overlap.  Hence Cauchy--Schwarz followed by ordinary differencing in the
character variable removes the only periodic signed coefficient instead
of amplifying it.  Simultaneous differencing also encounters the exact
radial null direction of the Hessian: increments proportional to
\((d_1,d_2)\) have zero quadratic form.  A generic two-dimensional
second-derivative theorem with a nonzero determinant is therefore
inapplicable.

No literal coefficient-sensitive bilinear theorem is supplied in the
statement-only packet.  A coefficient-uniform theorem cannot replace
(*), because the adversarial choice of bounded coefficients makes the
collar positive.  A valid imported theorem would have to state its
dependence on the quarter-shifted odd lattice, the close-factor ranges,
the squarefree/coprime projector or its joint Mobius opening, the hard
profiles, and arbitrary real \(X\); no such hypothesis audit can be made
here.

**(g) Hard supports, endpoints, nonstationary modes, and zero
extension.**  The exact floor dependence is confined to amplitudes, but
must remain there:

\[
 \Phi\!\left(\frac{4Xz}{m^2(H+1)}\right),
 \qquad W\!\left(\frac X{ym}\right)
\]

in the unscaled transform, and the rescaled versions displayed above.
Replacing \(q_X\) by 1 or \(H+1\) by \(X^{1/4}\) can change a literal
endpoint value and is not part of this derivation.  An upper support bound
does not imply a nonzero interval on which a profile is bounded below.

For a smooth interior piece, negative modes and modes separated from the
gradient image are nonstationary and are treated by integration by parts.
A saddle reaching a hard edge lies in a boundary stationary/Fresnel
transition and is not a rapidly decaying mode.  If zero extension leaves
a nonzero endpoint, its dual Fourier tail is only of order
\(|X/m-\ell|^{-1}\) and is not absolutely summable over all \(\ell\).
It is therefore invalid to discard every nonstationary dual mode by an
unqualified positive norm.

For a fixed finite family of Lipschitz hard boundaries, one may peel a
unit lattice collar in the primal variables: it contains \(O(L)\) points
per boundary curve and its positive contribution is within
\(L^{3/2}\).  Corners contribute \(O(1)\).  The remaining smooth piece can
use the collar calculation above.  Alternatively one must retain the
conditional cancellation of the endpoint Fourier series.  The
statement-only packet does not give enough definitions to verify the
number, variation, derivative norms, or literal endpoint values of the
named profile pieces, so this endpoint prescription is a required ledger,
not a completed proof for (162.BL1).  After a Mobius opening, boundary
pieces must be combined before using the physical cone cancellations
noted in part (a).

## 4. First doubtful or unproved step

The first indispensable unproved step is the signed dual-collar estimate
(*) with the **actual** coefficient.  In an opening-based proof it must be
a joint version of (*) that retains

\[
 \mu(a)\mu(b)\mu(c)\chi _4(A)\chi _4(m),
\]

the rescaled profiles, the even \(d_2\) sector, radial Fourier phases, and
endpoint transitions before any positive norm.  A per-Mobius-term bound
is insufficient because every fixed term has the same
\(\sqrt{JL}\) positive collar capacity.

Quantitatively, the missing assertion must reduce a collar of positive
mass \(J/L\) to signed mass at most \(\sqrt JX^\varepsilon\), saving
\(\sqrt J/L\asymp H/L\).  Periodicity of \(\chi _4\) alone does not prove
this: its differenced correlation is constant, and its complete divisor
convolution can be nonnegative.  Rank-one stationary phase and the
divisor bound give the collar and its capacity, but no cancellation within
it.

There is also a prior implementation gap if one insists on a theorem for
the exact named profiles: their explicit formulas, derivative/variation
bounds, number of hard entries and exits, and endpoint values are absent
from the statement-only packet.  Even granting standard finite-piece
smoothness does not remove the signed-collar gap above.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_t1_coefficient_and_orientation` | **PASS.** The product grouping keeps \(\chi _4\) on \(d_1\), the positive factor is \((L^2/(d_1d_2))^{3/4}\), the original phase is \(+J\sqrt{d_1d_2}\), and the leading dual orientation is \(+e(1/8)\chi _4(m)e(Xd_2/m)\). |
| `squarefree_coprime_even_d2_branch` | **PASS.** The projector is \(\mu^2(d_1d_2)\); an even squarefree product forces 2 into \(d_2\), and the isolated even sector has \(d_2=2d_2'\) and dual product \(m\ell=2X\). |
| `chi4_preserved_before_positive_norms` | **PASS algebraically.** The two quarter-shifted frequency lattices combine to \(-\chi _4(m)/(2i)\) on all odd \(m\).  No positive norm was used before deriving this identity.  Taking a norm afterward is explicitly labeled diagnostic and loses the needed arithmetic information. |
| `product_phase_rank_one_hessian` | **PASS.** The determinant is identically zero, \((x,z)\) is the radial null vector, and there is exactly one negative transverse direction. |
| `one_variable_character_poisson_self_return` | **PASS.** The equations \(r=k-\sigma/4\), \(x_0=Xz/(4r^2)\), and transformed phase \(Xz/(4r)\) were derived, including the stationary signature, coefficient cancellation, dual character, and exact \(W(X/(ym))\) profile. |
| `two_variable_dual_hyperbola` | **PASS.** The stationary equations give \((k-\sigma/4)\ell=X/4\), equivalently \(m\ell=X\), with a radial critical manifold and zero Legendre phase on exact resonance. |
| `dual_product_collar_width_and_mass` | **PASS.** A radial interval of length \(R\) gives width \(J/R\), at most \((J/R+1)X^\varepsilon\) factor slots, and total positive mass \(\sqrt{JL}X^\varepsilon\); for \(R=L\) the width is \(J/L\). |
| `mobius_opening_and_rescaled_support_cost` | **PASS as an obstruction.** The exact \((a,b,c)\) opening, \(A=[a^2,c]\), \(B=[b^2,c]\), rescaled supports, dual ranges, hyperbola \(m\ell=XAB\), and cancellation of the \(AB\) power in the positive ledger were derived. |
| `hard_cone_profiles_floors_endpoints` | **OBSTRUCTION RECORDED; not green for a proof.** The physical cone endpoint rows vanish for arithmetic reasons, but opened terms and the literal profile endpoints remain.  Exact \(q_X,y,H+1\), zero extension, boundary stationary transitions, and non-absolutely-summable hard Fourier tails were retained.  The packet does not provide the profile regularity data needed to finish their analytic estimates. |
| `missing_L_half_power` | **PASS.** The original capacity misses by \(L^{1/2}\); after Poisson the better ledger misses by \(H/L\), so the best coefficient-insensitive gap is \(\min(L^{1/2},H/L)\). |
| `physical_coefficient_vs_diagnostic` | **PASS.** The positive collar calculation and the nonnegative full divisor convolution are explicitly diagnostic.  No lower bound for the profiles, no coherent phase alignment, and no lower bound for \(\mathcal S_{L,1}\) is claimed. |
| `remaining_few_point_and_downstream_scope` | **PASS.** This report concerns only the displayed \(t=1\) close-factor scalar.  It makes no claim for other few-point channels, the hard-TOP parent, M9-M2, M9, the bridge, or a global exponent. |

No numerical experiment was performed; the allocation was 100% analytic
and algebraic.

## 6. Dependencies and exact artifacts used

This was a statement-only blind derivation.  The only files read were:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/blind_statement.md`;
3. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/briefs/blind_t1_close_factor_rederivation.md`.

No proof graph, active campaign, strategy file, conductor seed, barrier
packet, prior-round artifact, sibling report, or other Round-162 artifact
was inspected.  No web source, external bilinear theorem, source card,
code, or numerical computation was used.  The derivation uses only exact
character algebra, elementary Mobius identities, Poisson summation on a
compact smooth/BV component, one-dimensional stationary phase, and the
standard elementary divisor estimate \(\tau(n)\ll_\varepsilon
n^\varepsilon\).

## 7. Recommended state effect

**Retain** this report as an exact scoped obstruction and coefficient/
geometry interface; make **no change** that promotes (162.BL2).  The
target remains unproved.  A future candidate can change that status only
by proving a literal signed collar estimate of type (*) (or an equally
strong alternative) while preserving the squarefree/coprime projector,
the even \(d_2\) branch, all profile and endpoint pieces, and uniformity in
the arbitrary real centre.  The positive collar capacity in this report
must not be recorded as a physical lower bound.
