# Conductor Round 117 prechecks

Campaign: gc-w7-16-actual-determinant-fibre-gate

Evidence status: exact algebra and exponent diagnostics only. No estimate
for the determinant correlation is asserted.

## Exact identities

Direct expansion verifies

\[
 ab'-a'b=a(b+q)-(a+p)b=aq-bp
\]

and the phase identity (117.C1). Character multiplication modulo four
gives (117.C2)--(117.C3), including negative same-sign M2 numerators after
the absolute values are taken.

Differentiation gives

\[
 \phi_{pp}=0,\quad
 \phi_{pq}={c\over\kappa_i(b+q)^2},\quad
 \phi_{qq}=-{2c(a+p)\over\kappa_i(b+q)^3},
\]

hence (117.C6).

## Shell and exponent ledger

For (b\asymp B), (a\asymp LB/D), the determinant threshold is
(B^2/W). Division by the coefficients of (q) and (p) gives the
widths (BD/(WL)) and (B/W). At
(B=D=Y^{1/2}), (L=Y^{1/6}), (W=Y^{7/16}), their exponents are
(19/48) and (1/16), and the row degree is (9/16).

The (B)-shell ray count is (O(LB^2/D)). Multiplication by the
(L^{-2}) coefficient square gives energy (B^2/(DL)), and multiplying
by row degree (B^2/W) gives (B^4/(DLW)). At (B=D), this is
(D^3/(LW)=Y^{43/48}).

## Scope guardrail

The actual lift coefficient has not been proved smooth along (p) or
(q). The one-sided triangle boundary, primitivity, both signs, and all
moving-symbol endpoints remain. No one-variable or Hessian calculation is
treated as a block estimate, and no block estimate is treated as a global
local moment before all-block assembly.
