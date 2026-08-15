# Conductor calculation: global nonsaddle section calculus

Campaign: `m9-m1-beta-global-nonsaddle-signed-section`  
Round: 47  
Allocation: 100% analytical/algebraic

## Exact x derivative

From (47.1), the complete x-dependent unit phase of one numerator is

\[
 \Theta=L\log\frac{D_j}{2q\sqrt{Xx}}
 +\nu\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}
 -\beta\log(hqx).
\]

Consequently

\[
 x\partial_x\Theta=-\left(\frac{L+\nu}{2}+\beta\right)
 =-\eta.                                                   \tag{47.C1}
\]

At the diagonal \(\nu=L\), this becomes \(-\alpha\). Hence the
phase-conjugated x derivative of the singular divided difference has the
exact numerator

\[
 -i\{\eta p(\nu)-\alpha p(L)\}.                            \tag{47.C2}
\]

It must not be split into two tails. Since

\[
 \eta=\alpha-\frac{L-\nu}{2},
\]

we have the cancellation-preserving identity

\[
 \frac{\eta p(\nu)-\alpha p(L)}{L-\nu}
 =\alpha\frac{p(\nu)-p(L)}{L-\nu}-\frac12p(\nu).           \tag{47.C3}
\]

Together with \(|\eta/D|\le1\) and \(|\alpha/A|\le1\), this is the
correct source of the one allowed height power in the x derivative.

## Global alpha normalization

Let

\[
 R=1+|\alpha|.
\]

Two-sided differentiated Stirling on the exact ratio gives

\[
 R_\alpha(\alpha)e^{i\omega_LL}
 =R^\kappa e^{i\Psi(L)}G_R(L),
 \qquad |\partial_L^mG_R(L)|\ll_m R^{-m},\quad m\le2,       \tag{47.C4}
\]

on each signed dyadic alpha shell, after putting every lower Stirling
correction in \(G_R\). The fixed-ratio Round-41 proof uses
\(R\asymp\lambda\); its four-region physical-height calculation is
otherwise scale-local. Replacing \(\lambda\) by \(R\) predicts

\[
 |\mathcal P_R|+R|\partial_L\mathcal P_R|
 \ll P_XR^{\kappa-2},                              \tag{47.C5}
\]

and, after (47.C3),

\[
 |\mathcal Q_R|+R|\partial_L\mathcal Q_R|
 \ll P_XR^{\kappa-1}.                              \tag{47.C6}
\]

The signed diagonal is not put under an absolute height norm. Its exact
finite-section logarithmic primitive must be formed first; the same
dyadic normalization predicts a smaller \(R^{\kappa-3}\log(2+R)\)
coefficient for the value and one extra R power after (47.C1).

Equations (47.C5)--(47.C6) are conductor candidates, not accepted
lemmas. Their missing seam is a complete global four-region calculation
with the actual moving faces, especially when \(R\ll\lambda\) on the
inner nonsaddle sector and when the physical center, radial ridge, or a
finite face crosses a dyadic shell.

## Nonsaddle summability if the candidate holds

On a dyadic shell of length \(O(R)\), absolute integration of (47.C5)
costs

\[
 O(P_XR^{\kappa-1}).                                  \tag{47.C7}
\]

For the x derivative, one L integration by parts using
\(|\Psi'|\ge\log(4/3)\), (47.C6), and \(\Psi''=1/\alpha\) has the same
capacity \(O(P_XR^{\kappa-1})\). Because \(\kappa<1\), the outer dyadic
sum converges. The compact inner endpoint adjoining the already closed
central box costs \(O(P_X)\), while ratio-cutoff L and x derivatives are
order one after integration over their fixed-ratio collars.

Thus the mathematical bottleneck is not an exponent gap. It is the
uniform global section theorem (47.C5)--(47.C6), including moving traces
and exact diagonal ownership, plus its actual one-count middle-cutoff
interface.

