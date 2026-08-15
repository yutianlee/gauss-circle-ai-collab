# Conductor audit: global boundary, section, and power assembly

Campaign: `m9-m1-beta-global-nonsaddle-signed-section`  
Round: 47  
Allocation: 100% analytical/algebraic

## Decision

The repaired packet and the statement-only derivation give the correct
global inner/outer nonsaddle theorem.  The finite section is

\[
 I_{U,V}(L)=[-V,V]\cap[L-U,L+U],
\]

so at symmetric exhaustion its only moving face is
\(\nu=L-T\) for \(0<L<2T\), with the reflected face for negative
\(L\).  There is no missing velocity: it is one in \(L\), zero in
\(x\), while \(\nu=\pm T\) are fixed.

## Complete section bounds

Let \(R=1+|\alpha|\).  Differentiated two-sided Stirling gives

\[
 R_\alpha(\alpha)e^{i\omega_LL}
 =R^\kappa e^{i\Psi(L)}G_R(L),\qquad
 |\partial_L^mG_R|\ll P_XR^{-m},\quad m\le2.
\]

The Round-41 four-region calculation is scale-local in \(R\), not in the
stationary scale \(\lambda\): its three height centers are
\(0,L,-L-2\beta\), separated by \(\asymp R\).  Repeating it before
any stationary normalization yields

\[
 |\mathcal P_\Delta|+R|\partial_L\mathcal P_\Delta|
 \ll P_XR^{\kappa-2}.
\]

For the phase-conjugated radial derivative, the exact numerator identity

\[
 \frac{\eta p(\nu)-\alpha p(L)}{L-\nu}
 =\alpha\frac{p(\nu)-p(L)}{L-\nu}-\frac12p(\nu)
\]

must be formed first.  It gives

\[
 |\mathcal Q_\Delta|+R|\partial_L\mathcal Q_\Delta|
 \ll P_XR^{\kappa-1}.
\]

Every smooth share is smaller.  The signed diagonal is first evaluated by

\[
 C_{U,V}[H]=\frac{H(L,L)}{A(L)}
 \{\Log D(L,q)-\Log D(L,p)\},
\]

and tends to \(i\pi H(L,L)/A(L)\).  Cubic decay of \(p(L)\) makes
this \(O(P_XR^{\kappa-4})\), hence strictly smaller than the displayed
targets.  This preserves the signed-before-absolute rule.

On the moving symmetric faces, direct substitution gives integrated
capacities \(O(P_XT^{\kappa-2})\) for the value and
\(O(P_XT^{\kappa-1})\) for the conjugated radial derivative.  Both vanish
because \(\kappa<1\); smooth traces vanish faster.  Affine switches agree
and collapsed sections are zero.

## Nonsaddle and coefficient assembly

On the accepted inner/outer supports, \(|\Psi'|\ge\log(4/3)\).
The value shells cost \(P_XR^{\kappa-1}\).  One \(L\)-integration by
parts gives the same cost for the radial derivative, including
\(\Psi''=1/\alpha\) and ratio-cutoff derivatives.  The dyadic shell sum
converges because \(\kappa<1\), uniformly since the actual
\(\lambda\ge\pi\).

The untouched sums are harmless: \(r,p>1\), one logarithmic derivative
is still summable, the scale factors are bounded, and there are only
\(O(\log X)\) scales.  The resulting normalized amplitude has

\[
 \sup_x|\mathcal A_{\rm ns}(x)|+
 \int_1^{N_X}|\mathcal A_{\rm ns}'(x)|\,dx\ll\log^C(2X).
\]

The accepted radial-BV implication then gives a polylogarithmic internal
bound, after which the external \(X^{1/4}\) factor is restored once.
Floors, stars, \(\chi_4\), collisions, and endpoint coefficients never
leave their one-count ledger.

## Remaining seam

The global nonsaddle theorem is proved.  The separate middle interface is
not supplied by this calculation: it requires cutoff invariance of the
accepted fixed-ratio saddle theorem, or literal identification of its
historical cutoffs.  That seam is audited separately.

