# Conductor derivation: a uniform moving-logarithm Fresnel bound

Campaign: `m9-m1-beta-log-amplitude-two-saddle`  
Role: conductor's independent analytic derivation  
Allocation: 100% analytical/algebraic; no numerical experiment or external theorem

## 1. Frozen abstract lemma

Let \(J=[p,q]\) be a fixed compact interval and let \(J^*\) be a fixed
compact enlargement. Assume
\(\varphi\in C^3(J)\) has at most one stationary point \(x_s\), with

\[
 c_0|x-x_s|\le |\varphi'(x)|\le C_0|x-x_s|,
 \qquad |\varphi''(x_s)|\ge c_0,                       \tag{30.C1}
\]

on the component containing it; a component with no stationary point is
easier. Let \(g\) be absolutely continuous, supported in \(J\), and let
\(x_0\in J^*\), \(0<a\le1\), \(\Lambda\ge2\). Then

\[
 \boxed{
 \left|\int_J g(x)\Log(a+i(x-x_0))e^{i\Lambda\varphi(x)}dx\right|
 \ll_{J,c_0,C_0,\|\varphi'''\|_\infty}
 \Lambda^{-1/2}\log(2\Lambda)
 \bigl(\|g\|_\infty+\|g'\|_1\bigr).}                \tag{30.C2}
\]

The branch is the principal logarithm. The estimate is uniform as \(x_0\)
crosses \(x_s\), either endpoint of \(J\), or the stationary entry/exit
point of a truncated component. The logarithm is sharp when
\(x_0=x_s\): after \(x=x_s+y/\sqrt\Lambda\), its constant piece is
\(-\tfrac12\log\Lambda\) times the ordinary Fresnel integral.

The same estimate holds for finite linear combinations of such logarithms,
step functions with finitely many jumps, and a BV remainder, with the
right side multiplied by the total coefficient/BV norm. This is the form
needed after explicit evaluation of a finite-section Hilbert kernel.

## 2. Uniform local logarithm mass

For every interval \(I\subset J\) of length \(r\le1\),

\[
 \sup_{0<a\le1}\sup_{x_0\in J^*}
 \int_I|\Log(a+i(x-x_0))|dx
 \ll r\log(2/r).                                      \tag{30.C3}
\]

If \(\operatorname {dist}(x_0,I)>2r\), the left side is
\(O(r(1+|\log\operatorname {dist}(x_0,I)|))\); because \(J^*\) is fixed,
this is at most the displayed bound. Otherwise translate and
enlarge \(I\) to \([-3r,3r]\). Split \(|y|\le a\) and
\(a<|y|\le3r\). The first part is
\(O(a(1+|\log a|))\), bounded by \(O(r\log(2/r))\); the second integrates
\(1+|\log|y||\) directly. This proves (30.C3), including endpoint
coalescence.

## 3. Stationary neighborhood

Set \(r=\Lambda^{-1/2}\) and
\(I_0=J\cap[x_s-4r,x_s+4r]\). Taking absolute values only here and using
(30.C3) gives

\[
 \left|\int_{I_0}g(x)\Log(a+i(x-x_0))e^{i\Lambda\varphi(x)}dx\right|
 \ll r\log(2/r)\|g\|_\infty.                         \tag{30.C4}
\]

This is \(O(\Lambda^{-1/2}\log(2\Lambda))\). It is uniform if the saddle
lies at an endpoint or if the moving logarithm meets it.

## 4. Dyadic nonstationary shells

For \(k\ge2\), let

\[
 I_k=J\cap\{2^kr<|x-x_s|\le2^{k+1}r\},
\]

stopping when the shell reaches the endpoint. On each connected component,
\(|\varphi'|\asymp2^kr\). Split once at \(x_0\) if it lies in the
component. On either resulting interval the logarithm is absolutely
continuous away from its endpoint, and integration by parts in the
Stieltjes/BV form gives

\[
 \left|\int_I A(x)e^{i\Lambda\varphi(x)}dx\right|
 \ll \frac{\|A\|_\infty+\operatorname {Var}_I(A)}
 {\Lambda 2^kr}
 +\frac{\|A\|_\infty |I|\|\varphi''\|_\infty}
 {\Lambda(2^kr)^2}.                                   \tag{30.C5}
\]

For \(A=g\Log(a+i(x-x_0))\), a direct absolute BV norm is not uniform as
\(a\downarrow0\) when \(x_0\in I\). Avoid this false step by separating
the logarithmic interval

\[
 K=I\cap[x_0-r_k,x_0+r_k],\qquad
 r_k=(\Lambda 2^kr)^{-1}.                             \tag{30.C6}
\]

On \(K\), take absolute values and apply (30.C3): the cost is
\(r_k\log(2/r_k)\). On each component of \(I\setminus K\), the logarithm
has variation

\[
 \int_{r_k}^{O(2^kr)}\frac{dy}{\sqrt{a^2+y^2}}
 \ll \log\!\frac{2^kr}{r_k}\ll\log(2\Lambda).       \tag{30.C7}
\]

Using (30.C5) there yields

\[
 \left|\int_{I_k}g(x)\Log(a+i(x-x_0))e^{i\Lambda\varphi(x)}dx\right|
 \ll \frac{\log(2\Lambda)}{\Lambda2^kr}
 \left(\|g\|_\infty+\int_{I_k}|g'|\right).           \tag{30.C8}
\]

Since \(\Lambda r=\sqrt\Lambda\), summing \(2^{-k}\) proves (30.C2).
The terminal partial shell and endpoint cases obey the same estimate.

## 5. Finite-section Hilbert form

For smooth \(H(L,\nu)\), subtract \(H(L,L)\):

\[
 \operatorname {PV}\int_{A(L)}^{B(L)}
 \frac{H(L,\nu)}{L-\nu}d\nu
 =H(L,L)\log\left|\frac{L-A(L)}{B(L)-L}\right|+R(L), \tag{30.C9}
\]

with signs interpreted componentwise and with the delta/Plemelj jump kept
separately. More invariantly, use the complex logarithm formula from Round
29 and take its boundary value. The remainder is

\[
 R(L)=\int_{A(L)}^{B(L)}
 \frac{H(L,\nu)-H(L,L)}{L-\nu}d\nu,                  \tag{30.C10}
\]

which is bounded by interval length times \(\|\partial_\nu H\|_\infty\).
On each cell where \(A,B\) are affine, its BV norm is controlled by first
and mixed derivatives of \(H\), plus endpoint traces. The finitely many
changes of affine formula add only jumps. Thus the complete delta-plus-PV
amplitude is a finite linear combination of moving logarithms, steps, and a
BV remainder. Equation (30.C2) applies provided those scaled norms are
uniform for the complete recombined beta numerator.

This reduces the actual Round-30 problem to a concrete seam: establish the
required scaled first/mixed derivative and endpoint-trace bounds for the
full \(H\), with the \(q,h,D_j,x,\beta,\rho\)-split and masks retained.
The abstract singular stationary estimate itself loses only one logarithm
and no power of the saddle height.

## 6. Normalization implication and caveat

In the original \(\alpha\) variable, the saddle width is
\(\sqrt\lambda\), because the normalized coordinate is
\(y=\alpha/\lambda\) and the large parameter is \(\lambda\). Hence
(30.C2) contributes the ordinary \(\sqrt\lambda\) stationary size times
\(\log(2\lambda)\). It does not change the algebraic \(q\)-power.
Conditionally on the Round-27 complete numerator retaining its separated
\(D_j/(q\lambda)\) factor in the BV/endpoint norms, the moving face keeps
\(q^{-2}\) up to a logarithm.

That conditional is material. Differentiating the full numerator can hit
the artificial \(\rho\)-cutoff, beta connector, radial phase, moving
polytope endpoint, or a scale profile. The abstract lemma cannot certify
that these derivatives preserve \(q^{-2}\). Nor does it control the
\(U,V,S\) tails or execute the \(h,D_j,x\) sums. No beta-transition or
theorem-level claim follows yet.

## 7. Recommended state effect

Promote (after independent blind and hostile agreement) only the abstract
moving-logarithm Fresnel bound (30.C2), its sharp logarithmic loss, and the
finite-section decomposition (30.C9)--(30.C10) under explicit scaled BV
hypotheses. Retain the actual-profile norm insertion, q-power preservation,
height tails, full sums, beta transition, M9-M1, M9, and target as open.
