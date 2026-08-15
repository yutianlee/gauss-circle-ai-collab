# Conductor adjudication: exact Fejer interface, no one-step power saving

## Outcome

The three Round-54 reports independently certify the same exact finite
interface.  If

\[
 c_n=\tau_X(n)A_X(n)n^{-3/4}e(\sqrt{Xn})
\]

is restricted to a consecutive interval \(I\) of length \(L\), extended by
zero, and \(1\le R\le L\), then

\[
 \left|\sum_{n\in I}c_n\right|^2
 \le {L+R-1\over R}\,\mathfrak F_{I,R},
\]

where

\[
 \mathfrak F_{I,R}=Q_I+2\Re\sum_{1\le r<R}
 \left(1-{r\over R}\right)\mathcal C_{I,r}
 ={1\over R}\sum_k\left|\sum_{s=0}^{R-1}c_{I,k+s}\right|^2\ge0.
\]

The diagonal radial top has weight \(1/4\), while a shifted upper endpoint
has weight \(1/2\).  Each angular star remains attached to its own divisor
leg.  Expanding the two exact coefficients gives

\[
 h_1q_1-h_2q_2=r,
\]

with \(q_1,q_2\) odd, the two characters, two scale sums, two Vaaler-height
floors, and the square-root difference phase all retained.

## Exponent ledger

On a dyadic radial block \(n\asymp Y\), one has

\[
 Q_I\ll_\varepsilon X^\varepsilon Y^{-1/2}.
\]

The weakest sufficient theorem is

\[
 \mathfrak F_{I,R}\ll_\varepsilon X^\varepsilon {R\over Y}.
\]

For \(R\ge Y^{1/2}\), the convenient stronger signed assertion

\[
 \left|\sum_{r<R}\left(1-{r\over R}\right)
 \mathcal C_{I,r}\right|
 \ll_\varepsilon X^\varepsilon {R\over Y}
\]

is genuinely sufficient without a negative off-diagonal main term: the
diagonal is already at most \(R/Y\).  At the minimal length
\(R=Y^{1/2}\), this asks for a quadratic gain \(Y^{-1/2}\); its square root
is the missing \(X^{-1/8}\) on the largest block \(Y\asymp\sqrt X\).

The global unsplit formulation obscures this useful localization: there the
diagonal is order one and a target-capable one-sided theorem without
diagonal cancellation requires \(R\asymp N\).  The dyadic theorem is the
sharper canonical interface.

## Sharp no-go and phase audit

Termwise absolute values give

\[
 |\mathcal C_{I,r}|\ll_\varepsilon X^\varepsilon Y^{-1/2},
\qquad
 \left|\sum_{n\in I}c_n\right|\ll_\varepsilon
 X^\varepsilon Y^{1/4},
\]

for every allowed \(R\).  Globally they give
\(N^{1/4+\varepsilon}=X^{1/8+\varepsilon}\).  A bounded adversarial
coefficient cancels the radial phase and saturates this coefficient-blind
ledger.  More importantly, the actual Round-53 star-free \(h_1=h_2=1\)
shell realizes the expanded absolute Fejer mass, so the obstruction is not
an artifact of endpoint conventions.  This remains an absolute-capacity
statement, not a signed lower bound for the actual coefficient.

For a smooth artificial amplitude, radial curvature balances at
\(R=Y^{3/2}/\sqrt X\), meeting the diagonal requirement only on the top
radial blocks.  The actual product coefficient has no usable bounded-
variation theorem.  Elementary Abel summation loses the same \(Y^{1/2}\),
and a B-process returns dual modes coupled to the original additive-product
constraint.  Phase-only differencing therefore returns the same signed
arithmetic survivor.

## Source and scope decision

The source audit checked Blomer--Harcos, Cowan, Petrow,
Banerjee--Khurana, and Kiral--Zhou.  None supplies the required uniform
theorem for an \(X\)-dependent divisor-angle coefficient with floors,
stars, growing shifts, and the nonlinear radial phase.  They remain method
analogies rather than imported dependencies.

The Hermitian Fejer form proves a stronger complex-modulus estimate.  A
lossless real-part polarization also creates a nonconjugated sum-phase
correlation and is not represented by the difference-phase kernel alone.
No physical estimate is transferred automatically to the connector-
completed alpha trace.

## Decision

Promote the exact Fejer reduction, dyadic target theorem, endpoint and
incidence ledger, and the sharp absolute/source no-go.  Retain the signed
actual-symbol correlation, GAR, alpha transition, M9-M1, M9, and the target
open.  The next campaign should analyze the minimal top-block regime
\(Y\asymp\sqrt X\), \(R\asymp Y^{1/2}=X^{1/4}\), using the exact
\(h_1q_1-h_2q_2=r\) incidence rather than another coefficient-blind phase
estimate.

All Round-54 work was analytical.  No numerical experiment was used.
