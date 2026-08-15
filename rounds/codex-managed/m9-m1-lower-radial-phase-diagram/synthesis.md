# Round 61 synthesis: exact lower-radial phase diagram

Campaign: m9-m1-lower-radial-phase-diagram

## Conductor decision

Promote the exact phase-diagram reduction, but no new analytic estimate.
For a smooth radial block \(n\asymp X^\nu\), stationary support maps
\[
 \ell=\delta+\frac{\nu-1}{2},\qquad
 \frac{1-\nu}{2}\leq\delta\leq\frac12.
\]
The TTY wedge is
\[
 1816\delta+89\nu\leq552,
\]
and first touches the active interval at
\[
 (\nu,\delta,\ell)=
 \left(\frac{356}{819},\frac{463}{1638},0\right).
\]
This point begins partial low-\(D\) coverage; it is not a radial closure
threshold.

## Coverage

The terminal theorem maps exactly to \(\nu=1/2\).  V2 maps exactly to
the degenerate sector \((\nu,\delta)=(0,1/2)\).  For
\(356/819\leq\nu<1/2\), TTY closes only
\[
 \frac{1-\nu}{2}\leq\delta\leq
 \frac{552-89\nu}{1816}.
\]
For \(0<\nu<356/819\), it closes no active scale.  Every
\(0<\nu<1/2\) retains the hard-top block
\[
 (\delta,\ell)=\left(\frac12,\frac{\nu}{2}\right).
\]
Thus the accepted direct menu fully closes only \(\nu=0\) and
\(\nu=1/2\); the exact uncovered radial band is \(0<\nu<1/2\).

## Missing power

On a residual block, the excess above the target for the best accepted
menu is
\[
 \sigma_*=
 \min\left\{
 \frac{1-2\nu}{4},\
 \frac{1816\delta+89\nu-552}{2564},\
 \delta-\frac14,\
 \frac{\nu}{4}
 \right\}.
\]
At the unavoidable top scale it is
\[
 \min\left\{\frac{\nu}{4},\frac{1-2\nu}{4}\right\},
\]
with crossover \(\nu=1/3\).

## Scope and next step

The smooth Mellin multiplier, \(O(\log X)\) scale count, floors, hard
top, profiles, stars, and transform errors preserve this diagram.  They
do not create cancellation.  No GAR, M9-M1, M9, or exponent promotion
follows.

The next target is the exact small-angle collapse of the angular
coefficient for \(n=o(\sqrt X)\), using
\(\Phi(u)=1+O(u^2)\) and the exact denominator partition.  The goal is
to isolate a simpler one-sided character-divisor radial sum and prove a
target-sized error range.

