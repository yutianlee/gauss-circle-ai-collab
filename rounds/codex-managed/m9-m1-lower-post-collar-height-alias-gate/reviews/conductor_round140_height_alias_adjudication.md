# Round 140 conductor adjudication: smoothed far-height aliases

## 1. Result and decision

Close Round 140 under
\(\mathsf{strict\_height\_alias\_reduction}\).  Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad0\le q\le2y,
\tag{140.J1}
\]

and fix

\[
 0<\rho_1<\rho_2<1/8.
\tag{140.J2}
\]

Put

\[
 L_{i,h}=\left\lfloor{\rho_i y\over\sqrt h}\right\rfloor,\qquad
 D_{i,h}=y-L_{i,h}-1.
\tag{140.J3}
\]

For every nonempty active row, let \(r_{2,h}\) be the least positive
odd integer with

\[
 r_{2,h}\ge {4Nh\over D_{2,h}^2}.
\tag{140.J4}
\]

Empty rows and profile-zero terms are defined to contribute zero.  The
literal Round-139 sharp tail at \(\rho_1\) is target-equivalent to

\[
 \begin{split}
 \mathcal P_{\rho_2}^{+}
 ={}&e(-1/8)N^{1/4}
 \sum_h\sum_{\substack{r\ge r_{2,h}+2\\r\ {\rm odd}}}
 \chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),\\
 \mathcal P_{\rho_2}^{-}
 ={}&\overline{\mathcal P_{\rho_2}^{+}}.
 \end{split}
\tag{140.J5}
\]

More precisely, for a fixed \(C\),

\[
 \boxed{\mathcal S_{N,\rho_1}^{\pm}
 =\mathcal P_{\rho_2}^{\pm}
 +O_{\rho_1,\rho_2,V}(R\log^C(2X)).}
\tag{140.J6}
\]

Consequently the first open scalar estimate is

\[
 \boxed{|\mathcal P_{\rho_2}^{\pm}|
 \ll_\varepsilon RX^\varepsilon.}
\tag{140.J7}
\]

Equation (140.J7) is not proved.  The decision is not a vote.  One
primary report found a smooth character-Poisson connector, the hostile
report detected the sharp principal-value failure and supplied the
two-collar repair, and the statement-only report independently found
the endpoint, rank-one, product-fibre, radical, and self-return
obstructions.  The three post-unmask reviews then independently checked
the smoothing and \(B\)-process owners, the arithmetic geometry, and
the scalar direction.

## 2. Exact sharp formula, floor threshold, and endpoint obstruction

The positive sharp tail is

\[
 \mathcal S_{N,\rho_1}^{+}
 =\sum_{h\ge1}{1\over h}\sum_{1\le d\le D_{1,h}}
 \chi_4(d)V_{\rm low}\!\left({4R^2h^2\over d^2}\right)e(Nh/d),
\tag{140.J8}
\]

and the negative tail is its conjugate.  For a nonempty row define

\[
 A_h(x)={1\over h}V_{\rm low}\!\left({4R^2h^2\over x^2}\right),
\qquad
 I_{h,r}^{\sharp}
 =\int_0^{D_{1,h}}A_h(x)e(Nh/x+rx/4)\,dx.
\tag{140.J9}
\]

Finite Poisson summation in the two mod-four branches, with the dual
integer symmetrized separately in each branch, gives

\[
 \begin{split}
 \mathcal S_{N,\rho_1}^{+}
 ={}&{1\over2}\sum_h\chi_4(D_{1,h})A_h(D_{1,h})
       e(Nh/D_{1,h})\\
 &+{1\over2i}\sum_{\tau=\pm1}\tau\sum_h
   \lim_{K\to\infty}\sum_{|k|\le K}
   I_{h,\tau-4k}^{\sharp}.
 \end{split}
\tag{140.J10}
\]

The explicit half-endpoint is \(O(\log(2X))\).  The map
\((\tau,k)\mapsto r=\tau-4k\) covers every odd integer, and
\(\tau=\chi_4(r)\) for positive \(r\).

For \(r>0\), the phase has

\[
 x_{h,r}=2\sqrt{Nh/r},\qquad
 \phi_{h,r}(x_{h,r})=\sqrt{Nhr},\qquad
 \phi_{h,r}''(x_{h,r})={r^{3/2}\over4(Nh)^{1/2}}.
\tag{140.J11}
\]

Writing \(a_{1,h}=L_{1,h}+1\) and \(r=4h+s\), the closed sharp-entry
condition is exactly

\[
 s\ge T_{1,h}
 ={4h(2ya_{1,h}-a_{1,h}^2+q)\over(y-a_{1,h})^2}
 \asymp_{\rho_1}\sqrt h.
\tag{140.J12}
\]

Every floor and equality case remains in the exact fraction.  Changing
\(q=0\) to \(q=2y\) adds exactly
\(8hy/D_{1,h}^2=O_{\rho_1}(h/y)\).  Equality is an endpoint saddle,
not a full Gaussian term.

The sharp dual family is not absolutely separable.  If the endpoint
sample is nonzero, integration by parts gives

\[
 I_{h,r}^{\sharp}
 ={A_h(D_{1,h})e(Nh/D_{1,h}+rD_{1,h}/4)
   \over2\pi i(r/4-Nh/D_{1,h}^2)}
 +O_h(r^{-2}).
\tag{140.J13}
\]

For the \(h=1\) plateau row the numerator is nonzero for all sufficiently
large \(X\), and therefore

\[
 \sum_{r\ {\rm odd}}|I_{h,r}^{\sharp}|=\infty.
\tag{140.J14}
\]

The half-endpoint and branchwise principal-value order in (140.J10)
carry this boundary cancellation.  A closest-alias deletion or a
principal-only sharp formula is false.

## 3. Two-collar smoothing and owner-complete \(B\)-process

Set

\[
 \Delta_h=D_{1,h}-D_{2,h}+1
 =L_{2,h}-L_{1,h}+1
 \asymp_{\rho_1,\rho_2}{y\over\sqrt h},
\tag{140.J15}
\]

choose a fixed smooth flat step \(\eta\), zero on
\((-\infty,0]\) and one on \([1,\infty)\), and define

\[
 W_h(x)=\eta\!\left({D_{1,h}+1-x\over\Delta_h}\right),\qquad
 \widetilde A_h(x)=A_h(x)W_h(x).
\tag{140.J16}
\]

At integer samples, sharp minus smooth is supported exactly on

\[
 D_{2,h}<d\le D_{1,h}
 \quad\Longleftrightarrow\quad
 L_{1,h}<v=y-d\le L_{2,h}.
\tag{140.J17}
\]

The complete phase on this band has constant-sign curvature
\(\asymp h/y\), and the sampled amplitude has fixed variation.  The
accepted Round-139 curvature lemma therefore gives, before any
transform,

\[
 \mathcal S_{N,\rho_1}^{+}
 =\widetilde{\mathcal S}_N^{+}+O(R\log(2X)).
\tag{140.J18}
\]

This is the only noninvertible step.  The smooth amplitude is flat at
both physical ends and satisfies

\[
 \|\widetilde A_h\|_\infty+\|\widetilde A_h'\|_1\ll h^{-1},
\qquad
 \|\widetilde A_h''\|_1
 \ll {1\over h}\left({1\over Rh}+{1\over\Delta_h}\right).
\tag{140.J19}
\]

Whole-line character Poisson now has no boundary harmonic.  The
rowwise smooth \(B\)-process is

\[
 \begin{split}
 {1\over2i}\sum_{r\ {\rm odd}}\chi_4(r)\widetilde I_{h,r}
 ={}&e(-1/8)N^{1/4}
 \sum_{\substack{r>0\\r\ {\rm odd}}}
 \chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)W_h(x_{h,r})e(\sqrt{Nhr})\\
 &+O_{\rho_1,\rho_2,V}\!\left({\log^2(2X)\over h}\right).
 \end{split}
\tag{140.J20}
\]

Here every negative alias, positive nonstationary alias, profile
crossing, and stationary remainder belongs to the displayed error.
For the error proof, split the true support \(c_VRh\ll x\ll y\) into
blocks \(x\asymp Z\) and put

\[
 P={Nh\over Z^2},\qquad
 w=\left({Z^3\over Nh}\right)^{1/2},\qquad
 \epsilon_3=\sqrt{Z\over Nh}.
\tag{140.J21}
\]

There are \(O(P)\) stationary aliases on the block and \(P\ge1\).
Including the \(h^{-1}\) amplitude, the total cubic and fixed-profile
variation errors are

\[
 {Pw\epsilon_3\over h}\ll h^{-1},
\qquad
 {Pw^2\over hZ}\ll h^{-1}.
\tag{140.J22}
\]

The derivative of \(W_h\) occurs only in its upper ramp.  That ramp has
\(O(1+\sqrt h)\) aliases, and with \(Z\asymp y\),
\(w^2\asymp y/h\), and \(\Delta_h\asymp y/\sqrt h\), its counted
variation is

\[
 \sqrt h\,{w^2\over h\Delta_h}\ll h^{-1}.
\tag{140.J23}
\]

Second-amplitude-derivative terms are smaller by (140.J19).  Away from
the local neighborhoods, derivative-image distance \(j\) gives
\(O((hj)^{-1})\).  The infinite negative and remote positive tails are
integrated twice; flatness kills their boundary terms and (140.J19)
makes the alias sums absolute.  One logarithm comes from distance and
one from the physical blocks, proving (140.J20).  Hence

\[
 \sum_{h\ll R}{\log^2(2X)\over h}\ll\log^3(2X).
\tag{140.J24}
\]

The smoothing-ramp aliases lie in

\[
 {4Nh\over(D_{1,h}+1)^2}
 \le r\le {4Nh\over D_{2,h}^2},
\tag{140.J25}
\]

an interval containing \(O(1+\sqrt h)\) odd integers.  Each principal
or exact transition integral is \(O(Rh^{-3/2})\).  Including the
separately discarded \(r_{2,h}\), their full cost is

\[
 \sum_{h\ll R}Rh^{-3/2}(1+\sqrt h)
 \ll R\log(2X).
\tag{140.J26}
\]

For \(r\ge r_{2,h}+2\),
\(\phi'(D_{2,h})\ge1/2\), while
\(\sqrt{\phi''(D_{2,h})}\asymp\sqrt{h/y}\).  Thus the saddle lies
\(\gg\sqrt{y/h}\) Gaussian widths inside \(W_h=1\).  Its Gaussian term
is

\[
 2e(1/8)N^{1/4}(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),
\tag{140.J27}
\]

with local error
\(O(N^{-1/4}(hr)^{-5/4})\).  Those local errors total
\(O(R^{-1}X^\varepsilon)\); the remaining plateau and profile
off-saddle pieces total \(O(R\log(2X))\).  Finally
\((2i)^{-1}\cdot2e(1/8)=e(-1/8)\).  Equations
(140.J18)--(140.J27) prove (140.J6) with every owner assigned.

## 4. Product geometry, capacity, radicals, and self-return

Finite regrouping of (140.J5) by \(m=hr\) gives

\[
 \mathcal P_{\rho_2}^{+}
 =e(-1/8)N^{1/4}
 \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)
 A_{\rho_2}(m)e(\sqrt{Nm}),
\tag{140.J28}
\]

where

\[
 A_{\rho_2}(m)
 =\sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\
                   r\ge r_{2,h}+2}}\chi_4(r).
\tag{140.J29}
\]

There is no missing height weight: the stationary coefficient is
\((hr)^{-3/4}=m^{-3/4}\).  Removing the far mask gives

\[
 \sum_{r\mid m}\chi_4(r)={r_2(m)\over4}.
\tag{140.J30}
\]

The divisor bound proves only

\[
 |\mathcal P_{\rho_2}^{+}|
 \ll_\varepsilon R^{3/2}X^\varepsilon.
\tag{140.J31}
\]

This is the actual coefficient-blind absolute capacity.  On the \(h=1\)
row the far mask removes only \(O_{\rho_2}(1)\) aliases.  On a fixed
profile plateau,

\[
 N^{1/4}\sum_{\substack{C_{\rho_2}\le r\le cN/R^2\\
                         r\ {\rm odd}}}r^{-3/4}
 \asymp R^{3/2}.
\tag{140.J32}
\]

Equation (140.J32) is a term-modulus control, not a lower bound for the
signed scalar.

For \(F(h,r)=\sqrt{Nhr}\),

\[
 \nabla^2F={\sqrt N\over4\sqrt{hr}}
 \begin{pmatrix}-r/h&1\\1&-h/r\end{pmatrix},
\qquad
 \det\nabla^2F=0,\qquad
 \nabla^2F\binom h r=0.
\tag{140.J33}
\]

The invertible linear change \(r=4h+s\) preserves determinant zero and
rank one.  At odd fourth-power centres, the ray
\((h,r)=(\ell,9\ell)\), \(\ell\equiv1\pmod4\), has unit phase and
character after a fixed initial segment, but its absolute mass is only
\(O(R)\).  It is a target-scale control, not a physical lower bound.

The mask also does not force fibrewise character cancellation.  Let
\(p\equiv1\pmod4\) and \(m=p^{2a}\) lie in a fixed nonzero profile
range at a sufficiently large odd fourth-power centre.  Write
\(r=p^j\), \(h=p^{2a-j}\).  Since \(D_{2,h}\ge3y/4\),

\[
 4h<{4Nh\over D_{2,h}^2}<8h.
\tag{140.J34}
\]

For \(j\le a\), \(r\le h\), so the divisor is excluded.  For
\(j\ge a+1\), \(r/h=p^{2(j-a)}\ge25\), hence
\(r-2>8h\) and \(r\ge r_{2,h}+2\).  All \(a\) upper divisors have
character one, and therefore

\[
 \boxed{A_{\rho_2}(p^{2a})=a.}
\tag{140.J35}
\]

This is an internal fibre statement only.

Write \(N=Du^2\) with \(D\) squarefree.  The phase is exactly one if
and only if \(m=Dt^2\).  Its complete far-family absolute mass is

\[
 N^{1/4}\sum_{\substack{m\ll y\\Nm=\square}}
 m^{-3/4}|A_{\rho_2}(m)|
 \ll_\varepsilon RD^{-3/4}X^\varepsilon.
\tag{140.J36}
\]

Thus exact radicals are target-safe.  Near radicals and nonsquare
incomplete fibres remain open.  Finally,

\[
 \Psi(m)=\sqrt{Nm}-{mz\over4},\qquad
 m_*={4N\over z^2},\qquad
 \Psi(m_*)={N\over z}.
\tag{140.J37}
\]

A second Legendre step returns the reciprocal phase, and completion of
the product fibre returns the sum-of-two-squares coefficient.  Neither
operation supplies an independent gain.

## 5. First open step and scalar direction

The first genuinely unproved estimate is the grouped form of
(140.J7):

\[
 \boxed{
 \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)
 A_{\rho_2}(m)e(\sqrt{Nm})
 \ll_\varepsilon X^\varepsilon.}
\tag{140.J38}
\]

It requires signed cancellation among near-radical and nonsquare
incomplete product fibres.  Rank-one geometry supplies no
nondegenerate two-variable theorem; fibrewise modulus loses
\(R^{1/2}\); exact radicals account for only a target-safe subfamily;
and a second transform self-returns.

Equation (140.J6) changes only an unsquared scalar by a target-safe
signed error.  It does not imply
\(|\mathcal P_{\rho_2}|^2=\mathcal R_{y^{-2}}+O(yX^\varepsilon)\),
nor does it delete a positive residual sub-square.  The
collar--tail cross term and the lift-dependent cutoff in reduced Farey
coordinates remain open.  The valid direction is only

\[
 |\mathcal P_{\rho_2}|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal S_{N,\rho_1}|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal F_N|\ll_\varepsilon RX^\varepsilon,
\tag{140.J39}
\]

after the usual epsilon renaming.

## 6. Controls, dependencies, and scope

The following seams are green after repair: exact \(N,y,q\); every
floor and empty row; both scalar signs; mod-four Poisson branches;
sharp half-endpoint and principal-value order; exact stationary entry
and equality; the two-collar off-by-one support; sampled variation;
profile and cutoff derivative norms; the \(O(\sqrt h)\) ramp image;
the \(r_{2,h}+2\) clean start; Gaussian constant; local, off-saddle,
nonstationary, transition, profile-crossing, and remainder ledgers;
the exact product coefficient; rank after \(r=4h+s\); character-correct
fourth-power controls; coefficient-blind capacity; prime-square fibres;
exact radicals; self-return; and scalar direction.

The rejected inferences are: absolute separation of the sharp dual
series; closest-alias-only endpoint repair; starting the clean bulk at
the \(\rho_1\) threshold; counting only \(O(1)\) ramp aliases; one
integration for remote smooth aliases; nondegenerate joint Hessian
gain; replacement of the incomplete fibre by \(r_2(m)/4\); automatic
height-character cancellation; a signed lower bound from a coherent
ray or modulus capacity; a near-radical estimate from the exact radical
bound; a second-transform gain; a tail-square identity; or any
downstream theorem or exponent promotion.

The evidence consists of the three primary reports, the conductor
candidate, the three final post-unmask reviews, and the accepted
Round-138 and Round-139 artifacts named in those reports.  No numerical
or symbolic experiment, web theorem, centre average, arbitrary array,
positive separated energy, or desired circle estimate is used.  The
round is 100 percent analytical.

No complete lower-radial signed estimate, lower GAR, either direct
blockwise M1 parent, M9-M1, M2 parent, M9-M2, endpoint-uniformity
theorem, M9, conditional quarter bridge, or Gauss-circle quarter theorem
follows.  The strongest internally proved exponent remains \(1/3\).
The separately audited external Li--Yang exponent remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots .
\tag{140.J40}
\]

## 7. Recommended State Patch

Create one proved reduction recording (140.J2)--(140.J7) and
(140.J15)--(140.J27): the literal post-collar sharp scalar is
target-equivalent to the clean far stationary alias scalar, with every
endpoint, smoothing, transition, nonstationary, profile, and remainder
owner target-safe.

Create one proved obstruction recording (140.J13)--(140.J14) and
(140.J28)--(140.J37): sharp Poisson is not absolutely separable; the
far scalar has rank-one phase, an exact incomplete product coefficient,
\(R^{3/2+o(1)}\) coefficient-blind capacity, same-sign prime-square
fibres, a target-safe exact-radical channel, an open near-radical
channel, and a transform self-return.

Update the open lower-radial signed owner, the Round-139 collar
reduction, and the existing transform-radical obstruction with this
new interface.  Reject every red inference in Section 6.

Retain unchanged M9-M1, M9-M2, endpoint uniformity, M9, the conditional
bridge, the quarter target, the internally proved exponent \(1/3\),
and the separately audited external Li--Yang exponent.
