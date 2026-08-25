# Round 139 conductor adjudication: exact curvature collar and displacement tail

## 1. Result and decision

Close Round 139 under
\(\mathsf{strict\_displacement\_quadratic\_reduction}\).  For

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad0\leq q\leq2y,
\]

fix \(0<\rho<1/8\) and put

\[
 L_h=\left\lfloor{\rho y\over\sqrt h}\right\rfloor.
\tag{139.J1}
\]

The literal integerized lower scalar splits exactly as

\[
 \boxed{\mathcal F_N^\pm
 =\mathcal C_N^\pm+\mathcal S_N^\pm
 =\mathcal S_N^\pm+O(R\log(2X)),}
\tag{139.J2}
\]

where \(\mathcal C_N^\pm\) contains \(0\leq v\leq L_h\) and
\(\mathcal S_N^\pm\) contains \(L_h<v<y\), with every profile endpoint,
zero sample, parity restriction, floor, and sign retained.  Therefore

\[
 |\mathcal S_N^\pm|\ll_\varepsilon RX^\varepsilon
 \quad\Longleftrightarrow\quad
 |\mathcal F_N^\pm|\ll_\varepsilon RX^\varepsilon.
\tag{139.J3}
\]

The tail estimate in (139.J3) is not proved and its absolute capacity
remains \(y^{1+o(1)}\).

This decision is not a vote.  The discovery report found the exact-phase
curvature collar.  The statement-only and hostile reports independently
proved the narrower Taylor/Gauss window and diagnosed the full-completion
self-return.  After unmasking, two reviewers independently rederived the
collar and its directionality, while the third recomputed the quadratic
modulus, gcd, correction, and Fourier seams.  Their requested floor,
fixed-\(\rho\), and Fourier-normalization repairs are incorporated below.

## 2. Exact scalar and displacement dictionary

For \(\sigma\in\{+1,-1\}\), set

\[
 \mathcal F_N^\sigma
 =\sum_{h\geq1}{1\over h}\sum_{0\leq v<y}
 \chi_4(y-v)
 V_{\rm low}\!\left({4R^2h^2\over(y-v)^2}\right)
 e\!\left(\sigma h{q+v^2\over y-v}\right).
\tag{139.J4}
\]

This follows termwise from \(d=y-v\) and

\[
 {N\over y-v}=y+v+{q+v^2\over y-v};
\tag{139.J5}
\]

the omitted \(\sigma h(y+v)\) is integral.  The map is a bijection from
\(1\leq d\leq y\) to \(0\leq v<y\).  Even \(d\) vanish.  If
\(p_y\equiv y-1\pmod2\), \(p_y\in\{0,1\}\), then every surviving sample is
\(v=p_y+2n\), and

\[
 \chi_4(y-v)=e\!\left({y-v-1\over4}\right).
\tag{139.J6}
\]

Thus the complete parity-lattice phase is

\[
 \Psi_{\sigma,h}(v)
 =\sigma h{q+v^2\over y-v}+{y-v-1\over4}.
\tag{139.J7}
\]

The fixed profile has bounded supremum and total variation, and its
literal support gives

\[
 h\leq C_V{y-v\over R}\leq C_VR .
\tag{139.J8}
\]

Define \(\mathcal C_N^\sigma\) and \(\mathcal S_N^\sigma\) by the two
disjoint integer ranges in (139.J2).  The floor endpoint belongs to the
collar if it has the surviving parity; otherwise the last parity point
lies below it.  Empty short rows, the hard \(v=0\) sample, terminal
displacements, and profile-zero samples are all assigned exactly once.
The negative scalar and both pieces are conjugates of their positive
counterparts.

## 3. Proof of the target-safe exact curvature collar

Put

\[
 g(v)={q+v^2\over y-v}={N\over y-v}-y-v .
\]

Then

\[
 g''(v)={2N\over(y-v)^3}.
\tag{139.J9}
\]

For \(v=p_y+2n\), the carrier in (139.J7) is linear and the exact
second derivative is

\[
 {d^2\over dn^2}\Psi_{\sigma,h}(p_y+2n)
 =\sigma{8hN\over(y-p_y-2n)^3}.
\tag{139.J10}
\]

On \(0\leq v\leq L_h\), one has
\((1-\rho)y\leq y-v\leq y\).  Since
\(y^2\leq N\leq y^2+2y\), the curvature has constant sign and

\[
 \left|\Psi_{\sigma,h}''\right|\asymp_{\rho}{h\over y}
\tag{139.J11}
\]

with a bounded ratio, uniformly in \(q\), \(p_y\), and \(\sigma\).

The elementary second-derivative estimate, uniformly on every
subinterval, is

\[
 \left|\sum_{n\in I}e(f(n))\right|
 \ll_A M\sqrt\lambda+\lambda^{-1/2}
\tag{139.J12}
\]

when \(I\) has \(M\) integer points,
\(\lambda\leq|f''|\leq A\lambda\), and \(f''\) has constant sign.
The monotone derivative-alias proof includes every stationary alias.
Abel summation gives the same bound times the amplitude supremum plus
sampled variation.

For fixed \(h\), the profile argument is monotone in \(n\); hence the
sampled profile variation, including its zero extension and both hard
cutoff jumps, is \(O_{V_{\rm low}}(1)\).  The number \(M_h\) of allowed
parity points satisfies

\[
 M_h\leq1+{L_h\over2}\ll1+{y\over\sqrt h}.
\tag{139.J13}
\]

Applying (139.J12) with \(\lambda\asymp h/y\) gives

\[
 \left|\sum_{\substack{0\leq v\leq L_h\\y-v\ {\rm odd}}}
 V_{\rm low}\!\left({4R^2h^2\over(y-v)^2}\right)
 e(\Psi_{\sigma,h}(v))\right|
 \ll \sqrt y+\sqrt{y/h}.
\tag{139.J14}
\]

The harmless term \(\sqrt{h/y}\) coming from the \(1\) in (139.J13) is
absorbed because active \(h\ll R\ll y\), with bounded \(X\) handled
directly.  Restoring \(h^{-1}\) and summing (139.J14) over \(h\ll R\)
proves

\[
 |\mathcal C_N^\sigma|
 \ll\sum_{h\ll R}{1\over h}
 \left(\sqrt y+\sqrt{y/h}\right)
 \ll R\log(2X).
\tag{139.J15}
\]

On \(h\asymp H\), the collar's weighted absolute capacity is
\(yH^{-1/2}\), whereas its signed curvature cost is
\(R+RH^{-1/2}\).  More generally, the same proof for the fixed-top
collar \(L_{\alpha,H}=\rho yH^{-\alpha}\) costs

\[
 RH^{1/2-\alpha}+RH^{-1/2}.
\tag{139.J16}
\]

Thus \(\alpha=1/2\) is the last power scale certified at \(R\) by this
specific rowwise curvature ledger.  This is not an optimality theorem or
a signed lower bound.  A full top row at \(H=R\) costs \(R^{3/2}\).

## 4. Quadratic completion: legal window and exact obstruction

The prescribed-centre quadratic decomposition is

\[
 {q+v^2\over y-v}
 ={q\over y}+{v^2\over y}
 +{v(q+v^2)\over y(y-v)},
\qquad
 E_{h,q,y}(v)=h{v(q+v^2)\over y(y-v)}.
\tag{139.J17}
\]

For \(v\leq y/2\),

\[
 0\leq E_{h,q,y}(v)
 \ll {hv\over y}+{hv^3\over y^2}.
\tag{139.J18}
\]

Consequently the window

\[
 v\ll\left({y^2\over h}\right)^{1/3}
\tag{139.J19}
\]

has bounded correction variation, uniformly in \(q\), because
\(h\ll\sqrt y\).  On \(v=p_y+2n\), the core is

\[
 C_h+{8hn^2+(8hp_y-y)n\over2y}.
\tag{139.J20}
\]

Exact completion modulo \(2y\), with all boundary frequencies, has

\[
 |G_{2y}(8h,B)|
 \leq\{2y(16h,2y)\}^{1/2}
 \ll\sqrt{y(h,y)}.
\tag{139.J21}
\]

The actual height weight closes every gcd case:

\[
 \sum_{h\ll R}{(h,y)^{1/2}\over h}
 \ll\log(2y)\sum_{g\mid y}g^{-1/2}
 \ll_\varepsilon X^\varepsilon.
\tag{139.J22}
\]

Thus the Taylor window is also target-safe, but it is polynomially
smaller than the exact curvature collar.

The correction cannot be treated as a bounded-variation coefficient on
the full range.  At odd fourth-power centres \(X=N=M^4\), with
\(R=M\), \(y=M^2\), \(q=0\), and \(h=1\),

\[
 E(v)={v^3\over y(y-v)}=y\,{t^3\over1-t},\qquad t={v\over y}.
\tag{139.J23}
\]

On a fixed compact \(t\)-interval, every allowed parity increment can be
chosen between \(1/10\) and \(1/6\).  There are \(\asymp y\) such
increments on the literal profile plateau, so

\[
 \operatorname{Var}_{v\equiv p_y(2)}e(E(v))\gg y.
\tag{139.J24}
\]

With

\[
 \begin{aligned}
 w_h(n)&={\bf1}_{p_y+2n\in I_h}
 V_{\rm low}\!\left({4R^2h^2\over(y-p_y-2n)^2}\right)
 e(E_{h,q,y}(p_y+2n)),\\
 \widehat w_h(k)&=\sum_{n\bmod2y}w_h(n)e(-kn/(2y)),\\
 C_h&={hq\over y}+{hp_y^2\over y}-{p_y\over4}+{y-1\over4},
 \end{aligned}
\]

the exact positive-sign completion is

\[
 e(C_h)\sum_{n\bmod2y}w_h(n)
 e\!\left({8hn^2+(8hp_y-y)n\over2y}\right)
 ={e(C_h)\over2y}\sum_{k\bmod2y}\widehat w_h(k)
 G_{2y}(8h,8hp_y-y+k).
\tag{139.J25}
\]

The negative sign is the conjugate identity.  Coefficient-blind \(L^2\)
gives \(O(y)\) on a full active interval; the raw Fourier-\(\ell^1\)
bound can be worse and must be minimized with the trivial bound.  There
is no gain over \(y^{1+o(1)}\).  Keeping the correction in the phase
recombines exactly to the original reciprocal scalar.  The complete sum
is ordinary additive Gauss, not Salié: the varying reciprocal
denominator, \(q\), profile, and hard boundary remain in \(w_h\).

Exact character-Poisson keeps all half-integer aliases and has the
accepted principal absolute ledger \(R^{3/2}\log(2X)\).  A second
Legendre step returns the reciprocal phase.  These facts obstruct the
full quadratic-completion route but do not weaken the exact collar bound.

## 5. Round-138 directionality and first open step

Round 138 proves

\[
 |\mathcal F_N|^2
 =\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon).
\tag{139.J26}
\]

Equations (139.J2) and (139.J26) yield only the logical chain

\[
 |\mathcal S_N|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal F_N|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon.
\tag{139.J27}
\]

They do not yield
\(|\mathcal S_N|^2=\mathcal R_{y^{-2}}+O(yX^\varepsilon)\).
Indeed,

\[
 |\mathcal F_N|^2
 =|\mathcal C_N|^2+|\mathcal S_N|^2
 +2\Re(\mathcal C_N\overline{\mathcal S_N}),
\tag{139.J28}
\]

and the cross term is open.  In reduced variables \(h=ag,d=bg\), the
condition

\[
 y-bg\leq\left\lfloor{\rho y\over\sqrt{ag}}\right\rfloor
\tag{139.J29}
\]

depends on the lift \(g\) and splits the exact
\(L_\chi(y/b)\) coefficient.  No residual sub-square has been deleted.

The first unproved estimate is precisely

\[
 \boxed{|\mathcal S_N^\pm|\ll_\varepsilon RX^\varepsilon.}
\tag{139.J30}
\]

The tail contains every sector in which the independent rowwise
curvature ledger exceeds \(R\), all terminal profile crossings, and the
remaining half-integer aliases.  A continuation needs a joint signed
height--alias estimate or a direct bound for the complete Round-138
residual.

## 6. Controls, dependencies, and scope

The following seams are green after the displayed repairs: exact
\(N=y^2+q\) and two-way displacement; literal support and zero extension;
both \(y\)-parities and scalar signs; parity-lattice curvature; floor and
empty-row ownership; profile sampled variation; weighted height summation;
\(q=0\), \(q=2y\), fourth powers, and every real floor interval; exact
Taylor correction; quadratic modulus, gcd, and boundary frequencies;
ordinary-Gauss rather than Salié structure; stationary aliases; and
scalar directionality.

The red inferences are: dropping the Taylor correction outside
(139.J19); applying a rowwise or aliaswise modulus beyond (139.J16);
using the raw Fourier-\(\ell^1\) bound as a gain; replacing the exact
completion by one principal term; calling the collar a filtered
Round-138 residual owner; deleting the collar--tail cross term; or
promoting a downstream theorem.

The evidence consists of the three primary reports, the conductor
candidate, the three post-unmask reviews, the Round-138 synthesis and
adjudication, and the Round-121 flat-cone synthesis.  No numerical or
symbolic experiment, centre average, external theorem, arbitrary
coefficient array, or desired circle estimate is used.  The round is
100 percent analytical.

No complete lower-radial signed estimate, lower GAR, direct blockwise M1
parent, M9-M1, M2 parent, endpoint-uniformity theorem, M9, quarter theorem,
or exponent follows.

## 7. Recommended State Patch

Create one proved reduction recording (139.J1)--(139.J3) and
(139.J9)--(139.J16): the complete exact-phase collar
\(v\leq\rho y/\sqrt h\) is target-safe, leaving the literal displacement
tail (139.J30).

Create one proved obstruction recording (139.J17)--(139.J25): the
prescribed-centre Taylor/Gauss window is target-safe, but the full
correction has \(\gg y\) variation on a literal fourth-power family;
complete quadratic Fourier summation is an invertible ordinary-Gauss
correlation, and coefficient-blind or aliaswise moduli retain \(y\) or
\(R^{3/2}\) capacity.

Update the open lower-radial signed owner and the Round-138 reduction and
transform-obstruction nodes with this evidence and with the scalar-only
directionality rule (139.J27)--(139.J29).  Reject every red inference in
Section 6.

Retain unchanged M9-M1, M9-M2, endpoint uniformity, M9, the conditional
bridge, the quarter target, the internally proved exponent \(1/3\), and
the separately audited external Li--Yang exponent
\((3292+25\sqrt{1717})/13762\).
