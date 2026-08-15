# Round 63 synthesis: exact Appell completion and reciprocal return

## Accepted result

The one-sided divisor coefficient has the exact generating function

\[
 \sum_{n\ge1}\mathcal D(n)z^n
 =\sum_{h\ge1}\frac{z^{4h^2+h}}{1+z^{2h}},
\]

and this is exactly half of a moving level-four Appell section, after
subtracting its zero term:

\[
 \mathscr F(z)=\frac12
 K_4\!\left(\tau,\frac{\tau}{8},
 \frac12-\frac{\tau}{8}\right)-\frac14.
\]

The completed section has four indispensable theta--Mordell terms and
is stable under \(\Gamma(2)\) only modulo elliptic shifts.  Its
holomorphic part is not an ordinary modular theta.

An independent statement-only derivation also proves an exact
one-sided character-Poisson formula.  For the square-root radial weight,
its interior stationary main is the reciprocal sum

\[
 2X^{-1/4}e(-1/8)
 \sum_{h,j>0}\frac{\chi_4(j)}h
 V\!\left(\frac{4Xh^2}{j^2N}\right)e(Xh/j),
\]

with exact half-boundary and subtraction terms.  The square boundary is
target-safe; the reciprocal bulk is not estimated.

## What did not close

The Appell transformation does not by itself control its convolution
with the square-root radial kernel.  Elementary Cauchy--Parseval and
deperiodized absolute-transfer routes retain polynomial capacity.  The
exact periodized signed pairing may still cancel, so this is a scoped
method no-go rather than a counterexample.

Likewise, termwise absolute summation of the reciprocal stationary cone
has \(X^{1/4}\) capacity.  A new character/hyperbola correlation theorem
is required, together with uniform stationary entry/exit control.

## State effect

Promote the exact Appell/source interface and the exact Poisson-return
reduction.  Do not promote the signed radial bound, a radial interval,
M9-M1, M9, or any discrepancy exponent.

