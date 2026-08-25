# Round 139 synthesis: an exact curvature collar is target-safe

Campaign: m9-m1-lower-denominator-displacement-quadratic-gate

Starting graph SHA-256:
5e82825804e5bb2de43779e7121e76bcfaa4b89d7ac0977ca2ceb84a33be8552

## Decision

Close under
\(\mathsf{strict\_displacement\_quadratic\_reduction}\).  Let

\[
 R=X^{1/4},\quad y=\lfloor\sqrt X\rfloor,\quad
 N=\lfloor X\rfloor=y^2+q,\quad0\leq q\leq2y,
\]

and fix \(0<\rho<1/8\).  With

\[
 L_h=\left\lfloor{\rho y\over\sqrt h}\right\rfloor,
\]

the exact integerized lower scalar has the owner-complete split

\[
 \boxed{\mathcal F_N^\pm
 =\mathcal S_N^\pm+O(R\log(2X)),}
\tag{139.S1}
\]

where \(\mathcal S_N^\pm\) is the literal complement
\(L_h<v<y\).  Thus the original scalar target is equivalent to

\[
 \boxed{|\mathcal S_N^\pm|
 \ll_\varepsilon RX^\varepsilon.}
\tag{139.S2}
\]

Equation (139.S2) is not proved.  The survivor retains
\(y^{1+o(1)}\) absolute scalar capacity.

## Exact curvature gain

On the surviving parity lattice \(v=p_y+2n\), the physical phase is

\[
 \Psi_{\sigma,h}(v)
 =\sigma h{q+v^2\over y-v}+{y-v-1\over4},
\]

and its exact curvature is

\[
 {d^2\over dn^2}\Psi_{\sigma,h}(p_y+2n)
 =\sigma{8hN\over(y-p_y-2n)^3}.
\tag{139.S3}
\]

On \(v\leq L_h\), the denominator is comparable to \(y\), so the
curvature has constant sign and size \(h/y\), uniformly in \(q\), both
parities, both signs, and every real floor interval.  The number of
parity points is at most \(1+L_h/2\), and the sampled profile has fixed
total variation.  The weighted second-derivative estimate gives

\[
 \left|\sum_{\substack{0\leq v\leq L_h\\y-v\ {\rm odd}}}
 V_{\rm low}(\cdots)e(\Psi_{\sigma,h}(v))\right|
 \ll\sqrt y+\sqrt{y/h}.
\tag{139.S4}
\]

Since the literal support has \(h\ll R\),

\[
 \sum_{h\ll R}{1\over h}
 \left(\sqrt y+\sqrt{y/h}\right)
 \ll R\log(2X),
\]

which proves (139.S1).  On \(h\asymp H\), the deleted collar has weighted
absolute capacity \(yH^{-1/2}\), but its signed curvature cost is
\(R+RH^{-1/2}\).  More generally, within a fixed top fraction,
\(L_{\alpha,H}=\rho yH^{-\alpha}\) costs
\(RH^{1/2-\alpha}+RH^{-1/2}\).  The value \(\alpha=1/2\) is the last
scale certified at \(R\) by this rowwise method; it is not a universal
optimality statement.

## Why the full quadratic completion still fails

The exact prescribed-centre core and correction are

\[
 {q+v^2\over y-v}
 ={q\over y}+{v^2\over y}
 +{v(q+v^2)\over y(y-v)},
\qquad
 E_{h,q,y}(v)=h{v(q+v^2)\over y(y-v)}.
\tag{139.S5}
\]

The window \(v\ll(y^2/h)^{1/3}\) has bounded correction variation.
There the parity-reduced core completes modulo \(2y\), with

\[
 |G_{2y}(8h,B)|
 \leq\{2y(16h,2y)\}^{1/2}
 \ll\sqrt{y(h,y)},
\]

and the actual \(h^{-1}\) weight makes the gcd ledger target-safe.  This
Taylor window is polynomially smaller than the exact curvature collar.

On the full range, the correction cannot be treated as a bounded-
variation coefficient.  At odd fourth powers with \(q=0,h=1\), a fixed
literal plateau interval has

\[
 \operatorname{Var}_{v\equiv p_y(2)}e(E_{1,0,y}(v))\gg y.
\tag{139.S6}
\]

The exact Fourier formula is an ordinary quadratic-Gauss correlation,
not a Salié sum.  Coefficient-blind \(L^2\) gives no improvement over
\(y\); retaining the full correlation and inverting reconstructs the
reciprocal scalar.  Exact character-Poisson retains all half-integer
aliases and its principal absolute ledger remains
\(R^{3/2}\log(2X)\).  A second Legendre step self-returns.

Thus the new progress comes from estimating the complete exact phase on
one collar, not from extending the Taylor core or discarding its
correction.

## Relation to the Round-138 residual

Round 138 gives

\[
 |\mathcal F_N|^2
 =\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon).
\tag{139.S7}
\]

Together with (139.S1), this yields the logical target equivalence

\[
 |\mathcal S_N|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal F_N|\ll_\varepsilon RX^\varepsilon
 \Longleftrightarrow
 |\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon.
\tag{139.S8}
\]

It does not yield a tail-square identity.  The collar--tail cross term is
open, and in reduced coordinates the cutoff depends on the lift and
splits the exact \(L_\chi(y/b)\) coefficient.  No part of the
Round-138 residual is separately deleted.

## Proof and exponent status

Round 139 proves a strict scalar support reduction and a scoped
full-completion obstruction.  It does not prove the tail bound, the
complete lower-radial signed estimate, lower GAR, either direct blockwise
M1 parent, or M9-M1.

Hard TOP, BAL, and every required UNBAL M2 owner remain open, so M9-M2
remains open.  Endpoint uniformity, M9, the conditional quarter bridge,
and the Gauss-circle target remain open.

The strongest internally proved exponent remains

\[
 {1\over3}.
\]

The separately audited external Li--Yang benchmark remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots .
\]

Round 139 proves no exponent improvement.

Resulting graph SHA-256:
a9f766ddfc55c1aa9dd0561d8a406996627ac8701313af063c90e2422cf54eaa
