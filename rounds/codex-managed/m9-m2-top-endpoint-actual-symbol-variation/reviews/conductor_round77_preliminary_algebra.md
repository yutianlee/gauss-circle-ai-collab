# Round 77 conductor preliminary algebra

Campaign: `m9-m2-top-endpoint-actual-symbol-variation`  
Graph SHA-256:
`e14373a05ee7d55258b53f07e18afa33682806add90bee49789208f464e46166`  
Status: conductor working note, not accepted mathematics.

## Exact lift factorization

For fixed primitive odd \(a<b<4a\), fixed stationary mode \(k\), and
odd lift \(g\), write

\[
\phi(u)=-J(\sqrt b-\sqrt a)\sqrt u+ku+
\frac{X(\sqrt b-\sqrt a)^2}{4k}.
\]

Its unique critical point is

\[
u_0=\frac{X(\sqrt b-\sqrt a)^2}{4k^2},
\qquad \phi(u_0)=0.
\]

The actual product symbol factors exactly as

\[
A_{ga,gb}(gu)=g^{-3}E_{a,b}(g)P_{a,b}(u),
\]

where

\[
\begin{aligned}
E_{a,b}(g)
={}&\eta_L(ga)\eta_L(gb)
\Phi\!\left(\frac{ga}{H+1}\right)
\Phi\!\left(\frac{gb}{H+1}\right),\\
P_{a,b}(u)
={}&L^3(ab)^{-3/4}u^{-3/2}
W\!\left(\sqrt{\frac{q_Xa}{4u}}\right)
W\!\left(\sqrt{\frac{q_Xb}{4u}}\right).
\end{aligned}
\]

Thus \(W\), \(q_X\), and the ratio powers are independent of \(g\).
Only the smooth dyadic/Vaaler factors and the additive collars move.
With

\[
R_g(u)=
\rho\!\left(\frac{g(u-b/4)}M\right)
\rho\!\left(\frac{g(a-u)}M\right),
\]

the complete centred integral is

\[
\mathfrak B^\circ(g)
=g^{-2}E_{a,b}(g)
\int P_{a,b}(u)R_g(u)e(g\phi(u))\,du.                \tag{C77.1}
\]

On every nonempty lift interval, \(g\asymp G\asymp L/b\).
The normalized symbol hypotheses should give

\[
|g\partial_g E|\ll |E|_{\rm env},\qquad
\|g\partial_g R_g\|_{\mathrm{BV}}\ll1.               \tag{C77.2}
\]

The second estimate is supported in the two fixed physical collars.

## Variation without a phase-derivative loss

The phase is strictly convex on \([b/4,a]\). Since \(a<b<4a\), its
second derivative is uniformly comparable to its value at \(u_0\) when
\(u_0\) is in the full saddle interval:

\[
\phi''(u_0)=\frac{2k^3}{J^2(\sqrt b-\sqrt a)^2}.      \tag{C77.3}
\]

Use the exact one-dimensional Morse coordinate \(v\), chosen with
\(\phi(u)=v^2\) and \(v(u_0)=0\). The complete integral becomes
\[
I(g)=\int Q_g(v)e(gv^2)\,dv.
\]

The potentially dangerous derivative of the phase is removed by the
exact identity

\[
g\partial_g e(gv^2)=\frac v2\,\partial_v e(gv^2).
\]

After integration by parts,

\[
gI'(g)=
\int\left(g\partial_gQ_g-\frac12\partial_v(vQ_g)\right)
e(gv^2)\,dv,                                         \tag{C77.4}
\]

with no boundary term because the collared amplitude is compactly
supported. Hence the same Fresnel/BV estimate controls \(I\) and \(gI'\).
At the expected normalized scale,

\[
|\mathfrak B^\circ(g)|+g|\partial_g\mathfrak B^\circ(g)|
\ll_\varepsilon X^\varepsilon
\frac{J(\sqrt b-\sqrt a)\sqrt g}{k^{3/2}}.           \tag{C77.5}
\]

Summing the derivative over a step-two interval of length \(O(G)\) then
gives the candidate variation bound. Formula (C77.4) remains the key
check at saddle entry and exit: the moving collar must give a uniformly
bounded \(Q_g\), \(g\partial_gQ_g\), and first \(v\)-variation after the
Morse change.

## Aggregate Poisson error

The original full endpoint rows and the difference between the original
symbol and the fixed-collar symbol use \(O_M(1)\) samples for each of
\(O(L^2)\) ordered pairs. Their absolute contribution is
\(O_M(L^2X^\varepsilon)\).

For the collared symbol, use whole-line Poisson. The curvature is

\[
\left|(-C_{h,s}\sqrt x)''\right|
\asymp\frac{Jr}{L^2}\ge1
\quad (L\le J^{1/2},\ r\ge1).                        \tag{C77.6}
\]

The zero and positive modes are therefore uniformly nonstationary or
one-sign curved. A negative mode whose critical point lies in the full
interval is retained as a complete integral, including a saddle inside a
collar. For every remaining negative mode, the fixed collar creates a
derivative gap at least a constant multiple of
\(M Jr/L^2\). Two integrations by parts in the mode tails, together with
one-dimensional curvature for the finitely many nearby modes, should
give \(O_\varepsilon(X^\varepsilon)\) per ordered pair. Summation gives
\(O_\varepsilon(L^2X^\varepsilon)\).

The required final proof must write these mode ranges and derivative
norms explicitly; pointwise stationary phase is unnecessary because all
stationary modes are retained as complete integrals.

## Preliminary verdict

The candidate interface is algebraically plausible. The decisive proof
seams are:

1. uniform BV after the exact Morse coordinate at both collar entries;
2. the two-integration-by-parts tail with the actual \(x\)-symbol;
3. exact finite support and full endpoint ownership;
4. whether the packet's seminorm assumptions on \(\eta_L,\Phi,W\) are
   sufficient without adding an unaccepted hypothesis.

No resonance-union or energy estimate follows from this note.
