# Round 98 conductor review: partition and route scope

## Direct physical partition

Let

\[
 \Omega=\{(\delta,\ell):1/4\leq\delta\leq1/2,
 0\leq\ell\leq\delta-1/4\}.
\]

Give the accepted main owners priority in the order terminal, isolated full
second derivative, then TTY. Equivalently put

\[
\begin{aligned}
 \mathcal T&=\{\ell=\delta-1/4\},\\
 \mathcal P&=\{(1/2,0)\},\\
 \mathcal W&=\{\ell<\delta-1/4,
                 \ 178\ell+1638\delta\leq463\},\\
 \mathcal U_1&=\{\ell<\delta-1/4,
                 \ 178\ell+1638\delta>463\}\setminus\mathcal P.
\end{aligned}
\]

Then

\[
 \Omega=\mathcal T\mathbin{\dot\cup}\mathcal P
 \mathbin{\dot\cup}\mathcal W\mathbin{\dot\cup}\mathcal U_1.
\]

The bottom and `R5-Full` residuals remain outside this main-term partition.
Lift \(\mathcal U_1\) to literal dyadic labels, and split only there by the
actual physical profile: the unique profile containing
\(d=\lfloor\sqrt X\rfloor\) is hard; every other profile is smooth. Fixed
smooth bands below the top have exponent \(1/2+o(1)\), so no exponent-only
hard/smooth test is valid.

The exact conditional direct theorem is

\[
 \boxed{
 \mathrm{TOP}_{\rm residual}+\mathrm{SMOOTH}_{\rm residual}
 \Longrightarrow\mathrm{M9\!-!M1},}
\]

relative to the accepted bottom, R5, terminal, second-derivative, TTY, and
hard-transform owners. `TOP` contains only the middle/lower residual shells
of the unique hard profile; its terminal shell is already owned.
`SMOOTH` is the literal uniform block estimate on every smooth profile in
\(\mathcal U_1\). A whole-\(\mathcal U_1\) theorem such as the exact
odd-kernel target or RCS is an alternative sufficient route, not an
additional simultaneous owner.

## Canonical scope

The canonical Gram is downstream of global angular recombination, the
one-sided-divisor/product-wavelet reduction, and a Farey conductor
decomposition. It owns one transition-flattened smooth nonaxial principal
component in

\[
 J^{13/18}<C_{\rm cond}\leq J^{3/4}.
\]

That route has already summed away the physical \(L\)-partition and has no
accepted inverse localization to one literal \((D,L)\) block. Thus assuming
the Gram theorem does not remove either direct physical child above. This is
a formal scope obstruction, not a failure of the Gram estimate.

Inside its own global route the theorem also leaves
\(J^{3/4}<C_{\rm cond}\leq J\), raw transitions, axes, cone edges, other
radial sectors, and top/radial interfaces. Lower conductors through
\(J^{13/18}\) are already owned on the fixed smooth threshold child.

## Coarse global radial partition

Before applying Mellin, alpha, product-wavelet, or conductor transforms,
fix a smooth dyadic partition of the exact finite \(n\)-sum. It has:

1. critical pieces \(n\asymp\sqrt X\) compactly inside
   \((0,16\sqrt X)\), already closed by terminal transfer;
2. lower-radial dyadic pieces tending to \(n/\sqrt X=0\), open as one exact
   signed aggregate;
3. the sharp upper endpoint and the finitely many support/interface pieces
   excluded by the compact critical theorem, open as one interface
   aggregate.

The exact coefficient \(\mathcal C_X^*(n)\), floors, stars, signs, and
endpoint convention stay inside each summand. This produces the proved
conditional radial assembly

\[
 \boxed{
 \mathrm{LOWER}_{\rm radial}+\mathrm{INTERFACE}_{\rm radial}
 \Longrightarrow\mathrm{GAR},}
\]

with the critical child already owned. Through \(\nu=2/5\), the lower child
may use the target-safe one-sided-divisor replacement, but its signed sum is
still open. Above \(2/5\), it retains both the exact correction and the
signed limiting cone.

The alpha transition and the product-wavelet/conductor program are
alternative refinements of unresolved transformed material. They are not
additional physical summands in this coarse radial partition and must not be
conjoined with it without a new successive-complement identity.

## Blockwise versus total conclusion

The accepted recombination gives

\[
 \mathcal M_{1,\rm active}^{\rm stat}(X)
 =-{4\over\pi}X^{1/4}\mathcal G_X+O(\log^2X).
\]

Hence GAR is exactly sufficient for the total active M1 contribution. It
does not imply bounds for individual dyadic blocks: the summation map has a
large kernel. The lawful downstream alternative is therefore

\[
 H1\!-!H3+H4+R5\text{-Full}+\mathrm{GAR}+\mathrm{M9\!-!M2}
 \Longrightarrow\mathrm{GC\ target},
\]

not `GAR -> blockwise M9-M1` and not `GAR -> M9`.

No analytic estimate or exponent is promoted by this review.
