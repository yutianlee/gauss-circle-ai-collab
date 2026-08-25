# Round 140 conductor candidate: smoothed far-alias reduction

## 1. Result

Fix two constants

\[
 0<\rho_1<\rho_2<1/8.
\tag{140.C1}
\]

The literal Round-139 tail at \(\rho_1\) is target-equivalent to one
clean signed far-alias scalar.  Put

\[
 L_{i,h}=\left\lfloor{\rho_i y\over\sqrt h}\right\rfloor,
 \qquad D_{i,h}=y-L_{i,h}-1,
\tag{140.C2}
\]

and, for every nonempty active row, let \(r_{2,h}\) be the least positive
odd integer satisfying

\[
 r_{2,h}\ge {4Nh\over D_{2,h}^2}.
\tag{140.C3}
\]

Every summand in what follows is defined to be zero when the
corresponding row is empty or its profile sample vanishes; in
particular, no undefined \(r_{2,h}\) is used in (140.C4).

Define

\[
 \begin{split}
 \mathcal P_{\rho_2}^{+}
 =e(-1/8)N^{1/4}
 \sum_{h\ge1}
 \sum_{\substack{r\ge r_{2,h}+2\\r\ {\rm odd}}}
 \chi_4(r)(hr)^{-3/4}
 V_{\rm low}\!\left({R^2hr\over N}\right)
 e\!\left(\sqrt{Nhr}\right),
 \qquad
 \mathcal P_{\rho_2}^{-}=\overline{\mathcal P_{\rho_2}^{+}}.
 \end{split}
\tag{140.C4}
\]

There is a fixed \(C\) such that

\[
 \boxed{
 \mathcal S_{N,\rho_1}^{\pm}
 =\mathcal P_{\rho_2}^{\pm}
 +O_{\rho_1,\rho_2,V}(R\log^C(2X)).}
\tag{140.C5}
\]

Every discarded term in (140.C5) is estimated as part of its literal
owner.  Thus the target is equivalent to

\[
 \boxed{|\mathcal P_{\rho_2}^{\pm}|
 \ll_\varepsilon RX^\varepsilon.}
\tag{140.C6}
\]

Equation (140.C6) is not proved.  The survivor has
\(R^{3/2+o(1)}\) coefficient-blind absolute capacity.  Its Hessian is
rank one, and product grouping gives an incomplete signed divisor
coefficient.  The round should close under
\(\mathsf{strict\_height\_alias\_reduction}\), with the sharp-endpoint,
rank-one, product-fibre, and self-return barriers recorded separately.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad0\le q\le2y.
\tag{140.C7}
\]

The fixed real profile \(V_{\rm low}\) is the accepted smooth compactly
supported lower profile, with its literal endpoint samples and zero
extension.  A nonzero sample forces \(h\ll d/R\), hence \(h\ll R\).
Bounded \(X\), empty rows, and zero profile samples are absorbed before
any denominator is formed.

The sharp positive tail is

\[
 \mathcal S_{N,\rho_1}^{+}
 =\sum_{h\ge1}{1\over h}
  \sum_{1\le d\le D_{1,h}}\chi_4(d)
  V_{\rm low}\!\left({4R^2h^2\over d^2}\right)e(Nh/d),
\tag{140.C8}
\]

and the negative tail is its conjugate.  For a fixed sharp row put

\[
 A_h(x)={1\over h}V_{\rm low}\!\left({4R^2h^2\over x^2}\right),
 \qquad
 I_{h,r}^{\sharp}=\int_0^{D_{1,h}}A_h(x)
 e\!\left({Nh\over x}+{rx\over4}\right)dx.
\tag{140.C9}
\]

All sums in (140.C10)--(140.C12) range only over rows with
\(D_{1,h}\ge1\), with omitted rows understood as zero.  Branchwise
symmetric Poisson summation gives the exact identity

\[
 \begin{split}
 \mathcal S_{N,\rho_1}^{+}
 ={}&{1\over2}\sum_h\chi_4(D_{1,h})A_h(D_{1,h})e(Nh/D_{1,h})\\
 &+{1\over2i}\sum_{\tau=\pm1}\tau\sum_h
 \lim_{K\to\infty}\sum_{|k|\le K}I_{h,\tau-4k}^{\sharp}.
 \end{split}
\tag{140.C10}
\]

The endpoint term is \(O(\log(2X))\).  The pair
\((\tau,k)\) parameterizes all odd \(r=\tau-4k\), and for positive
\(r\), \(\tau=\chi_4(r)\).

The exact stationary point and its entry condition are

\[
 x_*=2\sqrt{Nh/r},\qquad
 \phi(x_*)=\sqrt{Nhr},\qquad
 r\ge {4Nh\over D_{1,h}^2}.
\tag{140.C11}
\]

Writing \(a_{1,h}=L_{1,h}+1\), \(D_{1,h}=y-a_{1,h}\), and
\(r=4h+s\), the last inequality is exactly

\[
 s\ge T_{1,h}:={4h(2ya_{1,h}-a_{1,h}^2+q)
                       \over(y-a_{1,h})^2}.
\tag{140.C12}
\]

Uniformly on active rows,

\[
 4\rho_1\sqrt h<T_{1,h}
 \ll_{\rho_1}\sqrt h+h/y,
\tag{140.C13}
\]

and changing \(q=0\) to \(q=2y\) changes the threshold by exactly
\(8hy/D_{1,h}^2=O_{\rho_1}(h/y)\).  Equality in (140.C12) is an
endpoint stationary point, not a full Gaussian term.

## 3. Proof of the owner-complete reduction

The sharp formula cannot first be separated by modulus.  If an active
endpoint sample is nonzero, integration by parts gives

\[
 I_{h,r}^{\sharp}
 ={A_h(D_{1,h})
 e(Nh/D_{1,h}+rD_{1,h}/4)
  \over2\pi i\{r/4-Nh/D_{1,h}^2\}}
 +O_h(r^{-2}).
\tag{140.C14}
\]

Hence \(\sum_{r\ {\rm odd}}|I_{h,r}^{\sharp}|=\infty\).  The
half-endpoint and the prescribed symmetric ordering in (140.C10) own
this principal-value boundary series.  Removing only the closest alias
does not repair it.

To remove the jump lawfully, put

\[
 \Delta_h=D_{1,h}-D_{2,h}+1
 =L_{2,h}-L_{1,h}+1\asymp {y\over\sqrt h}
\tag{140.C15}
\]

and choose a fixed smooth flat step \(\eta\), zero on
\(( -\infty,0]\) and one on \([1,\infty)\).  Define

\[
 W_h(x)=\eta\!\left({D_{1,h}+1-x\over\Delta_h}\right).
\tag{140.C16}
\]

It equals one for \(x\le D_{2,h}\), vanishes for
\(x\ge D_{1,h}+1\), and
\(\|W_h^{(j)}\|_\infty\ll_j\Delta_h^{-j}\).  Replacing the sharp
indicator in (140.C8) by \(W_h\) changes only

\[
 L_{1,h}<v=y-d\le L_{2,h}.
\tag{140.C17}
\]

The exact Round-139 curvature calculation applies to this sampled BV
amplitude and gives

\[
 \mathcal S_{N,\rho_1}^{+}
 =\widetilde{\mathcal S}_N^{+}+O(R\log(2X)).
\tag{140.C18}
\]

This is the sole noninvertible step and is made before transforming.

With \(\widetilde A_h=A_hW_h\), whole-line character Poisson is now
exact with no boundary harmonic.  The derivative ledger is

\[
 \|\widetilde A_h\|_\infty+
 \|\widetilde A_h'\|_1\ll h^{-1},
 \qquad
 \|\widetilde A_h''\|_1
 \ll {1\over h}\left({1\over Rh}+{1\over\Delta_h}\right).
\tag{140.C19}
\]

Here is the rowwise smooth \(B\)-process ledger used below.  Put
\(x_{h,r}=2\sqrt{Nh/r}\) and

\[
 \widetilde I_{h,r}
 =\int_0^\infty\widetilde A_h(x)
   e(Nh/x+rx/4)\,dx .
\tag{140.C19a}
\]

Then

\[
 \begin{split}
 {1\over2i}\sum_{r\ {\rm odd}}\chi_4(r)\widetilde I_{h,r}
 ={}&e(-1/8)N^{1/4}
 \sum_{\substack{r>0\\r\ {\rm odd}}}
 \chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)W_h(x_{h,r})e(\sqrt{Nhr})\\
 &+O_{\rho_1,\rho_2,V}\!\left({\log^2(2X)\over h}\right).
 \end{split}
\tag{140.C19b}
\]

For completeness, partition the true support
\(c_VRh\ll x\ll y\) into blocks \(x\asymp Z\).  On one block put

\[
 P={Nh\over Z^2},\qquad
 w=\left({Z^3\over Nh}\right)^{1/2},\qquad
 \epsilon_3={Nh\over Z^4}w^3=\sqrt{Z\over Nh}.
\tag{140.C19c}
\]

There are \(O(1+P)\) stationary aliases and \(w\) is one Gaussian
width.  Including the actual \(h^{-1}\) amplitude, the counted cubic
and fixed-profile variation errors are

\[
 {P w\epsilon_3\over h}\ll {1\over h},
 \qquad
 {P w^2\over hZ}\ll {1\over h}.
\tag{140.C19d}
\]

The derivative of \(W_h\) is supported only on the smoothing ramp.
There \(Z\asymp y\), only \(O(1+\sqrt h)\) aliases occur,
\(w^2\asymp y/h\), and \(\Delta_h\asymp y/\sqrt h\); hence its counted
variation is

\[
 \sqrt h\,{w^2\over h\Delta_h}\ll {1\over h}.
\tag{140.C19e}
\]

Second-amplitude-derivative terms are smaller by (140.C19).  Off the
stationary neighborhoods, monotonicity of the derivative gives
\(O((hj)^{-1})\) at odd-alias distance \(j\), producing one logarithm.
The infinite negative and profile-exterior tails are integrated twice;
flatness at both physical endpoints removes every boundary term, and
(140.C19) makes their alias sum \(O(h^{-1})\).  The nearest
derivative-image endpoint alias stays in the transition owner below.
Summing the \(O(\log(2X))\) physical blocks proves (140.C19b), and then

\[
 \sum_{h\ll R}{\log^2(2X)\over h}\ll\log^3(2X).
\tag{140.C19f}
\]

Stationary points in the smoothing ramp have odd aliases in

\[
 {4Nh\over(D_{1,h}+1)^2}
 \le r\le {4Nh\over D_{2,h}^2}.
\tag{140.C20}
\]

There are \(O(1+\sqrt h)\) such aliases.  Since
\(\phi''(x)\gg h/y\) there, the weighted integral bound and the
corresponding principal-term bound are both \(O(Rh^{-3/2})\).  The
complete ramp, together with the separately discarded alias
\(r_{2,h}\) when it lies just beyond the real interval, therefore costs

\[
 \sum_{h\ll R}Rh^{-3/2}(1+\sqrt h)
 \ll R\log(2X).
\tag{140.C21}
\]

For \(r\ge r_{2,h}+2\), one has
\(\phi'(D_{2,h})\ge1/2\), whereas
\(\sqrt{\phi''(D_{2,h})}\asymp\sqrt{h/y}\).  Thus the saddle is
\(\gg\sqrt{y/h}\) Gaussian widths inside the region \(W_h=1\).
The local calculation in (140.C19b) gives

\[
 \int_0^\infty\widetilde A_h(x)e(\phi_{h,r}(x))dx
 =2e(1/8)N^{1/4}(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr})+\mathcal E_{h,r}.
\tag{140.C22}
\]

The local Taylor part of \(\mathcal E_{h,r}\) is
\(O(N^{-1/4}(hr)^{-5/4})\), and it sums absolutely by

\[
 N^{-1/4}\sum_m\tau(m)m^{-5/4}\ll R^{-1}X^\varepsilon.
\tag{140.C23}
\]

The plateau-to-ramp off-saddle part is
\(O(\{h(1+r-4Nh/D_{2,h}^2)\}^{-1})\), and the remaining fixed-profile
off-saddle part is \(O((hr)^{-1})\).  Their complete far-owner sum is
\(O(R\log(2X))\).  Equations (140.C19b)--(140.C19f) own every smooth
nonstationary mode, profile crossing, closest endpoint alias, and
stationary remainder; (140.C20)--(140.C21) remove the full ramp and
\(r_{2,h}\).  Hence there is no remaining half-endpoint or transition
owner.  The branch factor and Gaussian constant satisfy
\(e(1/8)/i=e(-1/8)\), so (140.C18)--(140.C23) prove
(140.C4)--(140.C5).

## 4. Exact product geometry and first open estimate

Grouping (140.C4) by \(m=hr\) gives

\[
 \mathcal P_{\rho_2}^{+}
 =e(-1/8)N^{1/4}
 \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)
 A_{\rho_2}(m)e(\sqrt{Nm}),
\tag{140.C24}
\]

where

\[
 A_{\rho_2}(m)=
 \sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\
                  r\ge r_{2,h}+2}}\chi_4(r).
\tag{140.C25}
\]

This is an exact incomplete divisor coefficient.  The first unproved
step is either (140.C6) or, equivalently,

\[
 \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)
 A_{\rho_2}(m)e(\sqrt{Nm})
 \ll_\varepsilon X^\varepsilon.
\tag{140.C26}
\]

The divisor bound gives only

\[
 |\mathcal P_{\rho_2}^{+}|
 \ll_\varepsilon R^{3/2}X^\varepsilon.
\tag{140.C27}
\]

This is also the genuine coefficient-blind absolute capacity.  On the
\(h=1\) row the far condition removes only
\(O_{\rho_2}(1)\) initial odd aliases.  Since the fixed lower profile is
one near zero, a fixed interval

\[
 C_{\rho_2}\le r\le c{N\over R^2}\asymp cR^2
\tag{140.C27a}
\]

lies on its plateau for sufficiently small fixed \(c>0\), and the sum
of the moduli of the corresponding terms is

\[
 N^{1/4}\sum_{\substack{C_{\rho_2}\le r\le cN/R^2\\
                         r\ {\rm odd}}}r^{-3/4}
 \asymp R^{3/2}.
\tag{140.C27b}
\]

Thus modulus genuinely has an extra factor \(R^{1/2}\) beyond the
target; (140.C27b) is not a lower bound for the signed scalar.

This excess cannot be removed by a generic two-dimensional curvature
theorem.  For \(F(h,r)=\sqrt{Nhr}\),

\[
 \nabla^2F={\sqrt N\over4\sqrt{hr}}
 \begin{pmatrix}-r/h&1\\1&-h/r\end{pmatrix},
 \qquad\det\nabla^2F=0,
 \qquad\nabla^2F\binom h r=0.
\tag{140.C28}
\]

The invertible linear change \(r=4h+s\) preserves the zero determinant.  Along a
rational ray the phase is linear in the scale.  At odd fourth powers,
the literal subray \((h,r)=(\ell,9\ell)\),
\(\ell\equiv1\pmod4\), has unit phase and character on a profile
plateau; its mass is only target-scale, so it is a control rather than a
lower bound.

Without the cone mask, the product fibre is
\(\sum_{r\mid m}\chi_4(r)=r_2(m)/4\).  The mask does not create
uniform character cancellation.  For sufficiently large odd
fourth-power centres and \(m=p^{2a}\), \(p\equiv1\pmod4\), in a fixed
nonzero profile range, write \(r=p^j\), \(h=p^{2a-j}\).  The lower
divisors \(j\le a\) fail the far inequality, while all \(a\) upper
divisors \(a+1\le j\le2a\) satisfy \(r\ge r_{2,h}+2\) and have
\(\chi_4(r)=1\).  Hence

\[
 \boxed{A_{\rho_2}(p^{2a})=a.}
\tag{140.C28a}
\]

This remains an internal fibre statement, not a lower bound for the
full scalar.

If \(N=Du^2\), \(D\) squarefree, exact phase one occurs only for
\(m=Dt^2\), whose entire far-family absolute mass is

\[
 \ll_\varepsilon RD^{-3/4}X^\varepsilon.
\tag{140.C29}
\]

Thus exact radicals are target-safe.  Near radicals, nonsquares, and
the aggregate of incomplete fibres remain open.  A second Legendre
transform sends \(\sqrt{Nm}-mz/4\) back to \(N/z\), and completing the
full fibre returns the sum-of-two-squares interface.  Both are
self-returns, not gains.

## 5. First doubtful or unproved step

The first open analytic statement is (140.C26).  It requires actual
signed cancellation among near-radical and nonsquare incomplete product
fibres.  Rank-one geometry supplies no nondegenerate Hessian, exact
radicals account for only a target-safe subfamily, product-fibre modulus
gives (140.C27), and a second transform returns the reciprocal scalar.

Before smoothing, the first false step is even earlier: treating the
sharp dual integrals in (140.C10) as absolutely separate owners.
Equation (140.C14) proves that the boundary tail is harmonic.  The
two-collar step (140.C15)--(140.C18), not a closest-alias deletion,
repairs that seam.  The transition contains \(O(\sqrt h)\) aliases and
must be priced as the complete band (140.C21).

No estimate of \(|\mathcal S_N|^2\) follows from (140.C5).  The
collar--tail cross term and the lift-splitting issue in reduced Farey
coordinates remain open, so the Round-138 residual changes only by
logical target equivalence.

## 6. Required controls, dependencies, and outcomes

The exact tail floor, empty rows, both scalar signs, mod-four branches,
half-endpoint, zero extension, equality stationary point, \(q=0\),
\(q=2y\), and real-centre uniformity are retained in
(140.C7)--(140.C13).  The sharp principal-value failure is proved in
(140.C14), rather than hidden by rearrangement.

The smooth repair uses only the already proved exact curvature collar.
Its physical band, derivative norms, \(O(\sqrt h)\) transition-alias
count, closest clean alias, profile crossings, nonstationary tails, and
stationary remainders are priced in (140.C15)--(140.C23).  No rowwise
or aliaswise modulus is applied to the surviving bulk.

The rank-one Hessian, character-correct rational rays, exact product
coefficient, divisor-sized fibre control, \(R^{3/2}\) capacity, exact
radical channel, near-radical gap, and Legendre self-return are retained
in (140.C24)--(140.C29).  No arbitrary array, positive energy, centre
average, numerical experiment, external theorem, or desired circle
estimate is used.  The allocation is 100 percent analytical.

Exact dependencies and evidence are:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- the Round-138 hostile Poisson report and synthesis;
- the Round-139 conductor candidate, adjudication, and synthesis;
- the three primary Round-140 reports and the Round-140 blind statement.

The candidate changes only the scalar interface.  Lower GAR, both direct
M1 parents, M9-M1, every M2 parent, endpoint uniformity, M9, the bridge,
the quarter theorem, and both recorded global exponents remain unchanged.

## 7. Recommended state effect

After independent post-unmask verification, create one proved reduction
recording (140.C1)--(140.C6): the literal sharp tail is target-equivalent
to the clean far-alias principal scalar, with all sharp endpoint,
smoothing, transition, nonstationary, profile, and stationary-remainder
owners target-safe.

Create one proved obstruction recording (140.C14) and
(140.C24)--(140.C29): sharp Poisson is not absolutely separable; the far
phase has rank-one Hessian and exact product fibres; coefficient-blind
capacity is \(R^{3/2+o(1)}\); exact radicals are target-safe; near
radicals and the incomplete signed coefficient remain open; and a second
transform self-returns.

Update the Round-139 collar reduction and the open lower-radial signed
owner with the new exact interface.  Reject a sharp closest-alias-only
repair, principal-only use before smoothing, nondegenerate Hessian gain,
independent height cancellation, complete-fibre replacement, near-radical
inference, product-fibre modulus, tail-square identity, and second-transform
gain.  Do not promote lower GAR, a direct M1 parent, M9-M1, any M2 parent,
endpoint uniformity, M9, the bridge, the quarter target, or an exponent.
