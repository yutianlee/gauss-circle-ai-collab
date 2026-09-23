# Round 165 statement-only packet

Let \(J=\sqrt X\), \(1\ll L\ll H\leq J^{1/2}\), and
\(R=\lceil L\rceil\).  Let \(c_N\) be the exact real residual coefficient
supported on a fixed-relative squarefree shell \(N\asymp L^2\), zero
outside that shell.  It is a bounded normalized sum over odd divisors
\(\sqrt N\leq d\leq2\sqrt N\), with sign \(\chi_4(d)\), a selector
\(\rho_N(d)\in\{0,1\}\), both parity branches, fixed smooth profiles,
finitely many hard point values, and zero extension.  Assume only

\[
 \sum_N|c_N|^2\ll_\varepsilon L^2X^\varepsilon.
\]

Define

\[
 \mathfrak C_{R,J,L}
 =\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r}c_N
 e\!\left(\frac{Jr}{\sqrt{N+r}+\sqrt N}\right).
\]

The frozen target is the one-sided actual-direction theorem

\[
 \Re\mathfrak C_{R,J,L}
 \leq C_\varepsilon L^2X^\varepsilon.
\]

Opening the two coefficients gives exactly

\[
 N=dm,\qquad N+r=d'm',\qquad
 d'm'-dm=r,\qquad1\leq r<R,
\]

where \(d,d'\) are odd and any factor \(2\) remains in \(m,m'\).
Both products are supported squarefree rows; every coefficient is zero off
its literal domain.

Starting only from this statement, independently test exact additive
near-product parameterizations, character-preserving summation,
square-root-phase summation, and any direct real-part completion.  Do not
take absolute values around individual shifts or tuples.  Derive a proof,
an owner-complete sector, or the first exact missing theorem and a rigorous
route no-go.  State every multiplicity, gcd, parity, endpoint, and
\(L,H,J,X\) power.

