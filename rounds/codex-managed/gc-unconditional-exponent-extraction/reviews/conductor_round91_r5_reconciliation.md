# Conductor review: pointwise Fejer residual reconciliation

## Verdict

The positive product-count proof closes R5-Full pointwise after H4, and
the current graph dependency cycle is documentary rather than
mathematical.

For \(H_D\asymp DX^{-1/4}\) put
\(\Delta=D/H_D\asymp X^{1/4}\). Vaaler's residual and the Fejer bound give

\[
 {1\over H_D}K_{H_D}(t)
 \ll \min\left(1,{1\over H_D^2\|t\|^2}\right).
\]

For the unshifted leg, a nearest integer \(m\) gives
\(d(X/d-m)=X-dm\). Grouping by \(n=dm\), with at most
\(\tau(n)\) divisors, reduces the residual to

\[
 X^\varepsilon\sum_{n\asymp X}
 \min\left(1,{\Delta^2\over|X-n|^2}\right)
 \ll_\varepsilon X^{1/4+\varepsilon}.
\]

The shifted legs use the exact products \(n=d(4m-\rho)\),
\(\rho=1,3\). Their congruence restrictions only reduce multiplicity.
Exact products take the summand value one. This matches the
floor-compatible equality
\(\psi_F(n)=-1/2\), \(K_H(0)/(2H+2)=1/2\). Half-open shells and
\(d\leq\lfloor\sqrt X\rfloor\) only restrict a positive majorant, while
the far tail is \(DH_D^{-2}\asymp X^{1/2}/D\leq X^{1/4}\).

The proof is uniform for real \(X\) and uses no \(X\)-average. It depends
directly on H4, H4-source-audit, the dyadic profile certificate, and the
elementary divisor bound. It does not depend on R5-Full itself.

Required graph repair:

1. remove R5-Full from the dependencies of R5-Full-reconciliation;
2. set both nodes to proved_internal;
3. retain H4 and the profile/divisor inputs as direct dependencies;
4. attach the Round-91 reports and conductor reviews as positive evidence.
