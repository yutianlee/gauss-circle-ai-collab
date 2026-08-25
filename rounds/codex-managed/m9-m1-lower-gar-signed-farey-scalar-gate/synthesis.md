# Round 138 synthesis: the actual lower scalar has a strict cross-denominator residual

Campaign: m9-m1-lower-gar-signed-farey-scalar-gate

Starting graph SHA-256:
56de446648dfb7a492fbb4b46c38d840fb14ac306df61bf61d466d26abfbe797

## Decision

Close under strict_signed_farey_reduction. Put

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor.
\]

The frozen scalar is termwise the integerized Round-121 flat cone:

\[
 \mathcal F_N=
 \sum_{\substack{2\le b\le y\\b\ {\rm odd}}}
 \frac{\chi_4(b)}bL_\chi(y/b)
 \sum_{\substack{1\le a<b\\(a,b)=1}}
 e(aN/b)J_{R,y}(a/b).
\tag{138.S1}
\]

The original \(X\)-phase cone differs from this scalar by the accepted
\(O(R)\) integerization seam. The certified small positive arc has
\(h<d\); all odd lifts are aggregated before any norm, and \(J(0)=0\)
kills the \(b=1\) class.

## Positive structural progress

At every rational sample,

\[
 \lambda_bJ_{R,y}(a/b)=\chi_4(b)c_{a,b},\qquad
 c_{a,b}=\frac{L_\chi(y/b)}a
 V_{\rm low}(4R^2a^2/b^2),
\]

\[
 |c_{a,b}|\ll\frac1a,\qquad a\ll\frac bR.
\tag{138.S2}
\]

Absorb the denominator character into

\[
 \theta_{a,b}=\frac{Na}{b},\qquad
 \phi_{a,b}=\frac{Na}{b}+\frac{b-1}{4}\pmod1.
\]

The complete same-denominator block is target-square-safe:

\[
 \sum_b\left|\sum_ac_{a,b}e(\phi_{a,b})\right|^2
 \ll y\log^2(2X).
\tag{138.S3}
\]

For a fixed reduced ordinary phase \(u/q\), every denominator is
\(b=qg\), with

\[
 g\mid N,\qquad q,g\ {\rm odd},\qquad
 (N/g,q)=1,
\]

and the numerator lies in one residue class modulo \(q\). Thus one
ordinary phase fibre has mass \(O(\tau(N)\log X)\). A physical
\(\phi\)-fibre is a union of at most two ordinary fibres. Since distinct
ordinary carriers have spacing at least \(y^{-2}\), and distinct physical
carriers have spacing at least \((4y^2)^{-1}\), either collision collar
satisfies

\[
 \sum_{\|z-z'\|\le\delta}M(z)M(z')
 \ll y\tau(N)\log^2(2X)(1+\delta y^2).
\tag{138.S4}
\]

Define

\[
 \mathcal R_\delta=
 \sum_{\substack{(a,b),(a',b')\\b\ne b'\\
 \|\theta_{a,b}-\theta_{a',b'}\|>\delta\\
 \|\phi_{a,b}-\phi_{a',b'}\|>\delta}}
 c_{a,b}\overline{c_{a',b'}}
 e(\phi_{a,b}-\phi_{a',b'}).
\tag{138.S5}
\]

Equations (138.S3)--(138.S4) prove the exact strict reduction

\[
 \boxed{
 |\mathcal F_N|^2
 =\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon).}
\tag{138.S6}
\]

Hence the scalar target is equivalent, after renaming epsilon, to

\[
 \boxed{
 |\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon.}
\tag{138.S7}
\]

Equation (138.S7) is not proved. The residual still has
\(y^{2+o(1)}\) absolute capacity against target \(y^{1+o(1)}\).

## Exact obstruction map

For \(b=Gr,b'=Gs,(r,s)=1\), the determinant chart is

\[
 \Delta=G\delta_0,\qquad
 \delta_0=as-a'r,\qquad
 a=a_0+r\ell,\quad a'=a'_0+s\ell.
\tag{138.S8}
\]

The phase and denominator character are constant in \(\ell\). The
partial fraction

\[
 \frac1{aa'}=\frac1{\delta_0}
 \left(\frac{s}{a'}-\frac r a\right)
\]

retains endpoint/aspect terms. Taking \(r=1,s=S\) with odd
\(S\asymp R^{1/2}\), \(a=a'=1\), and odd
\(G\asymp R^{3/2}\) gives a reciprocal-kernel contribution \(1\) while
\(\log X/(S-1)\to0\). Thus determinant fibres do not supply an
aspect-free contraction, and a fibrewise modulus returns full capacity.

At odd fourth powers, the actual packet

\[
 a=1,\qquad b=y-4u,\qquad1\le u\le cR
\]

lies beyond both \(y^{-2}\) collars and has target-square internal
capacity. It is not a lower bound because exterior terms may cancel.
The accepted half-integer tube calculation separately shows
\(R^{3/2}\) capacity after a forbidden tube-wise modulus.

## Poisson normalization, radical control, and self-return

The complete hard-interval character-Poisson identity contains the
explicit half-endpoint and every dual integral. Its clean interior
stationary principal factor is

\[
 e(-1/8)N^{1/4}\chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),
\tag{138.S9}
\]

with absolute ledger

\[
 \ll R^{3/2}\log(2X),
\tag{138.S10}
\]

above target \(R\). Formula (138.S9) is not a full transform of the
finite scalar: the hard endpoint and transition, nonstationary modes,
profile and stationary crossings, remainders, small heights, both
branches, floors, lift reassembly, and the conjugate sign keep separate
owners.

If \(N=Ds^2\), \(D\) squarefree, the variable principal phase is exactly
one only on

\[
 hr=Dt^2.
\]

This unique radical channel has absolute mass

\[
 \ll_\varepsilon RD^{-3/4}X^\varepsilon,
\tag{138.S11}
\]

inside a bounded principal/transition family. Near radicals, nonsquare
modes, and all nonprincipal owners remain open. A second Legendre step
returns the reciprocal phase, while exact Fourier completion returns the
flat discrepancy. These are scoped self-returns, not gains.

## Proof and exponent status

The smallest unresolved object is now the literal cross-denominator
residual (138.S5) with both carrier distances exceeding \(y^{-2}\). It
requires a full factor \(y\) of joint cancellation in the square. The
diagonal, complete rows, exact fibres, microscopic collars, determinant
modulus, uniform character pairing, principal-only Poisson replacement,
radical-only control, positive separated energy, and repeated transform
are all insufficient.

The lower-radial signed estimate and lower GAR remain open. Both direct
blockwise M1 parents remain open, so M9-M1 remains open. Hard TOP, BAL,
and every required UNBAL owner remain open, so M9-M2 remains open.
Endpoint uniformity, M9, the conditional quarter bridge, and the
Gauss-circle target remain open.

The strongest internally proved exponent remains

\[
 \frac13.
\]

The separately audited external Li--Yang benchmark remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
\]

Round 138 proves no exponent improvement.

Resulting graph SHA-256:
5e82825804e5bb2de43779e7121e76bcfaa4b89d7ac0977ca2ceb84a33be8552
