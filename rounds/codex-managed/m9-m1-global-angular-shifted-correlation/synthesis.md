# Round 54 synthesis: shifted correlation exposes, but does not supply, the missing square-root gain

## 1. Conductor decision

Round 54 closes with an exact coefficient-preserving Fejer reduction and a
sharp one-step no-go.  The reduction isolates a concrete signed
shifted-product theorem with the right target capacity, but no such theorem
is proved.  Absolute values retain the full normalized \(X^{1/8}\) loss.

## 2. Exact finite reduction

For a consecutive radial interval \(I\) of length \(L\), put

\[
 c_n=\mathbf1_I(n)\tau_X(n)A_X(n)n^{-3/4}e(\sqrt{Xn}).
\]

For every \(1\le R\le L\),

\[
 \left|\sum_n c_n\right|^2
 \le {L+R-1\over R}\left\{Q_I+2\Re\sum_{1\le r<R}
 \left(1-{r\over R}\right)\mathcal C_{I,r}\right\},
\tag{54.1}
\]

and the braced Fejer form is nonnegative.  The correlation expands with the
exact incidence

\[
 h_1q_1-h_2q_2=r,
\tag{54.2}
\]

while retaining both \(\chi_4\) factors, scale sums, height floors, angular
profiles, and the phase

\[
 e\!\left(\sqrt X(\sqrt{h_1q_1}-\sqrt{h_2q_2})\right).
\]

The shifted radial endpoint has weight \(1/2\); the diagonal endpoint has
weight \(1/4\); angular stars remain independent.

## 3. Exact target capacity

On a dyadic block \(n\asymp Y\), the weakest sufficient condition is

\[
 \mathfrak F_{Y,R}\ll_\varepsilon X^\varepsilon {R\over Y}.
\tag{54.3}
\]

Since \(Q_Y\ll_\varepsilon X^\varepsilon Y^{-1/2}\), for any
\(Y^{1/2}\le R\le Y\) it suffices to prove

\[
 \left|\sum_{r<R}\left(1-{r\over R}\right)\mathcal C_{Y,r}\right|
 \ll_\varepsilon X^\varepsilon {R\over Y}.
\tag{54.4}
\]

At \(R=Y^{1/2}\), (54.4) requires a \(Y^{-1/2}\) gain over the quadratic
absolute capacity.  On the largest block \(Y\asymp\sqrt X\), its square
root is exactly the missing normalized \(X^{-1/8}\).

## 4. Sharp obstruction

Termwise absolute values and ordinary divisor bounds give only

\[
 \left|\sum_{n\asymp Y}c_n\right|
 \ll_\varepsilon X^\varepsilon Y^{1/4},
\]

and globally \(X^{1/8+\varepsilon}\).  A phase-cancelling bounded
coefficient saturates the coefficient-blind inequality.  An actual
star-free \(h_1=h_2=1\) shell also realizes the expanded absolute Fejer
mass, so endpoints and stars do not explain the loss.

Smooth radial curvature has formal capacity only on the top block.  With
the actual divisor-angle coefficient, its variation cost loses the same
square root, and a B-process reconstructs the shifted-product kernel.
Thus Fejer differencing and phase curvature do not themselves prove a new
range.

## 5. Literature and real-part scope

No audited primary theorem among the relevant spectral, shifted-divisor,
averaged-shift, or Voronoi sources accepts the moving \(X\)-dependent
angular coefficient with all floors, stars, growing shifts, and nonlinear
phase.  No black-box theorem is imported.

Equation (54.1) controls the stronger complex modulus.  Direct differencing
of the required real part additionally creates a nonconjugated sum-phase
correlation.  The physical radial reduction also does not by itself close
the finite connector-completed alpha operator.

## 6. State effect

Promote a scoped exact Fejer shifted-correlation reduction and a scoped
absolute/source no-go.  Retain the signed theorem (54.4), GAR, the alpha
transition, M9-M1, M9, and the Gauss-circle target open.  No new exponent is
proved.

## 7. Next strategy

The next round should freeze the minimal top-block kernel
\(Y\asymp\sqrt X\), \(R\asymp X^{1/4}\), expand the short additive
incidence (54.2), and test a character-sensitive completion in the shift
variable.  The objective is to determine whether the period-four
character and square-root phase yield a genuine two-variable cancellation
after summing \(r\), or whether the Fejer average returns a positive/local
energy obstruction.  The alpha transfer remains a separate later seam.
