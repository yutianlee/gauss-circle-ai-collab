# Round 78 conductor adjudication

Campaign: m9-m2-top-endpoint-square-resonance-mass  \
Round: 78  \
Starting graph SHA-256:
5afbe1bb7b5c5d943be9438ba02bd9ede1ab6735344174b33b4a99c7de7f9123

## Decision

Promote the complete actual-symbol primitive-square contribution as
target-sized.  Also promote the route no-go that its raywise absolute
Abel majorant is not target-sized.  These conclusions are compatible:
the proof of the signed theorem retains reciprocal-mode cancellation,
whereas the majorant removes it before summation.

The clean statement-only rederivation, analytic derivation, hostile
audit, and conductor calculation agree on the exact square
parametrisation, the complete-integral sampled \(k\)-variation, the
weighted second-derivative estimate, and the aggregate lift count.  The
hostile review correctly rejects a stronger pointwise
\(k\partial_k\)-bound at a smooth collar.

The generic nonsquare resonance union, full transposed energy, signed
top cone, \(M9\!-\!M2\), \(M9\), endpoint uniformity, and the global
exponent remain open.

## Exact promoted interface

Let \(J=\sqrt X\), \(1\leq L\leq H\leq J^{1/2}\), and use the accepted
Round-77 complete collar-extracted coefficient.  The primitive rays for
which \(ab\) is a square are exactly

\[
 a=s^2,\qquad b=t^2,\qquad t=s+2u,\qquad
 (s,u)=1,\qquad 1\leq u<s/2,
\]

with odd \(s,t\).  Their reciprocal-mode interval and exact combined
phase are

\[
 I_{s,u}=\left(\frac{Ju}{s},\frac{2Ju}{t}\right),
 \qquad
 e(-Xu^2/k)e(-2nXu^2/k)=e(-gXu^2/k),
 \quad g=2n+1.                                      \tag{78.A}
\]

For every actual odd lift \(g\), put

\[
 K=\frac{Ju}{s},\qquad
 B_g(k)=\mathfrak B^\circ_{s^2,t^2,k}(g).
\]

The complete smooth-collar integral satisfies

\[
 \sup_{k\in I_{s,u}}|B_g(k)|
 +\operatorname{Var}_{k\in I_{s,u}\cap\mathbb Z}B_g(k)
 \ll_\varepsilon
 X^\varepsilon\sqrt{\frac{gt^2}{K}}.                \tag{78.B}
\]

Consequently

\[
 \left|\sum_{k\in I_{s,u}\cap\mathbb Z}
 B_g(k)e(-gXu^2/k)\right|
 \ll_\varepsilon (L+1)X^\varepsilon.                \tag{78.C}
\]

Since

\[
 \sum_{s,u}\#\mathcal G_{s^2,(s+2u)^2}
 \ll L\log(2+L),
\]

the exact signed square-family sub-sum obeys

\[
 \boxed{
 |\mathcal S_L^\square(X)|
 \ll_\varepsilon L^2X^\varepsilon .
 }                                                    \tag{78.D}
\]

This includes every exact and metric reciprocal resonance and requires
no cancellation between distinct lifts or rays.

By contrast, for the standard fixed dyadic support with a positive
interior terminal box,

\[
 \boxed{
 \mathcal M_L^\square(X)
 \asymp_{X^\varepsilon}\sqrt J\,L^{3/2}.
 }                                                    \tag{78.E}
\]

Already a fixed populated \((s,t)=(9,11)\) ray along fourth powers gives
\(\mathcal M_{L_0}^\square(T^4)\gg_{L_0}T=X^{1/4}\).
The lower bound uses only
\(\min(N,(2\|\theta\|)^{-1})\geq1\), not an abundance of exact
resonances.

## Proof adjudication

For a fixed square ray and lift, set \(A=Ju\), \(\lambda=gk\), and
\(r=A/k\).  After the exact square-root radial substitution, the
Round-77 coefficient is

\[
 B_g(k)=g^{-2}E(g)\int q_g(\tau)
 e\!\left(\lambda(\tau-r)^2\right)d\tau,             \tag{78.F}
\]

where \(E(g)\) is \(k\)-independent and uniformly bounded, while
\(q_g\) is \(k\)-independent and contains the literal \(W\)-profiles,
\(q_X\), powers, and both fixed physical collars.  If
\(Q_0\asymp g^3s\) and \(w\asymp(gs)^{-1}\), then

\[
 \|q_g'\|_1\ll Q_0,\qquad
 \|q_g^{(m)}\|_1\ll_m Q_0w^{1-m}.
\]

The quadratic kernel resolves the narrowest collar because

\[
 \lambda w^2\asymp\frac{K}{gs^2}
 \asymp\frac{K}{L}\gg1.                              \tag{78.G}
\]

The exact Gaussian multiplier formula, expanded to fixed order, has a
Schwartz remainder after each collar is rescaled by \(w\).  Its value,
total variation in the normalized collar coordinate, and logarithmic
\(\lambda\)-derivative are bounded by a geometric power of
\((\lambda w^2)^{-1}\).  Since \(r=A/k\) traverses the physical
interval only once and \(k\) stays in one fixed-ratio interval, the
leading terms and remainder give (78.B).

This argument proves total variation, not the false pointwise bound
\(k|B_g'(k)|\ll\sqrt{gt^2/K}\).  At a collar crossing the pointwise
derivative may be larger by \(L\), but the crossing lasts
\(\asymp K/L\) modes and contributes one endpoint-sized variation
packet.

For \(f(k)=-gXu^2/k\),

\[
 |f''(k)|\asymp\lambda_0:=\frac{gs^3}{Ju}
 \asymp\frac{gt^2}{K}\ll1.
\]

The one-dimensional second-derivative bound on every partial interval,
followed by discrete Abel with (78.B), gives

\[
 \sqrt{\lambda_0}
 \left(M\sqrt{\lambda_0}+\lambda_0^{-1/2}\right)
 \ll M\lambda_0+1\ll L+1,
\]

where \(M=Ju(2s-t)/(st)\) is the real interval length.  This proves
(78.C).  The lift count then proves (78.D).

For (78.E), use
\(\min(N,(2\|\theta\|)^{-1})\leq N\ll G\),
\(G\ll L/t^2\), and

\[
 \sum_{K<k<K'}k^{-3/2}
 \ll (K'-K+1)K^{-3/2}.
\]

The interval-length term sums to
\(\ll\sqrt J\,L^{3/2}\log(2L)\); the singleton term is smaller.
Conversely, a fixed-ratio terminal box with \(g=1\),
\(s\asymp u\asymp\sqrt L\), and \(s-2u\asymp s\) contains
\(\gg L\) coprime odd pairs.  Each pair has \(G\asymp N\asymp1\),
\(k\asymp J\), and a \(k\)-interval of length \(\asymp J\), so its
positive contribution is \(\gg\sqrt{JL}\).  This proves the matching
lower bound up to \(X^\varepsilon\).

## Hostile controls and rejected analogues

For \(X=T^4\), odd \(13\mid T\), \((s,t,u)=(9,11,1)\), and
\(k=2T^2/13\), the mode is strictly interior, the lift phase is fully
coherent, the saddle is \(169/4\), and both actual \(W\)-arguments
\(9/13\) and \(11/13\) lie on the unit plateau.  Its single-mode mass is
target-safe; coherence does not refute (78.D).

The following shortcuts are false:

1. the absolute Abel majorant is target-sized;
2. \(k|B_g'(k)|\) has the total-variation scale pointwise through a
   physical collar;
3. all collar-transition modes may be removed absolutely;
4. exact-divisor counting captures the metric resonance window;
5. an arbitrary bounded or phase-conjugated \(k\)-coefficient satisfies
   (78.B);
6. reciprocal inversion supplies a second independent saving.

## Downstream scope

The theorem removes the exact square/common-squarefree-kernel family
from the unresolved primitive-ray energy.  The next M2 obligation is the
generic nonsquare reciprocal-resonance inverse theorem, followed by the
signed primitive-ray energy.  Round 78 does not close the full
transposed energy or the top cone.

The residual upper-conductor part of \(M9\!-\!M1\) is untouched.  No
status changes for \(M9\!-\!M1\), \(M9\!-\!M2\), \(M9\), endpoint
uniformity, \(R5\)-Full, or the Gauss-circle exponent are authorized.
