# Statement-only packet: maximal residual parity-Fejer dyadic gate

Let \(J=\sqrt X\), \(1\ll L\ll H\le J^{1/2}\),
\(R_0=\lceil L\rceil\), and \(M\asymp L^2\).  A consecutive interval of
\(M\) sites contains the support of a finite coefficient \(c_N\), which is
zero-extended.  Put

\[
 z_N=c_Ne(J\sqrt N),\qquad
 D=\sum_N|c_N|^2\ll_\varepsilon L^2X^\varepsilon.
\]

The coefficient is the complete literal hard-TOP residual coefficient: all
selectors, no-pair rows, squarefree masks, \(\chi_4\) factors, complementary
parity branches, profiles, floors, stars, crossings, endpoints, point values,
and zero-extension jumps are part of it.

The target is

\[
 \Re\!\sum_{\substack{R_0\le r<M\\2\mid r}}
 \left(1-\frac rM\right)
 \sum_N z_{N+r}\overline{z_N}
 \ll_\varepsilon L^3X^\varepsilon.
\tag{B1}
\]

There is one outer real part and no shiftwise or rowwise modulus.

Define

\[
 F_R(\theta)=R^{-1}\left|\sum_{0\le j<R}e(j\theta)\right|^2,
\quad
 K_R^{(2)}(\theta)=\tfrac12\{F_R(\theta)+F_R(\theta+1/2)\},
\quad
 Z(\theta)=\sum_Nz_Ne(N\theta).
\]

Starting from this data alone:

1. derive the exact parity-projected Fejer identity for all integer \(R\);
2. choose \(R_{j+1}=\min(2R_j,M)\) and derive the exact telescoping formula,
   including the short-shift correction and final non-doubling link;
3. for exact doublings, derive both the triangular-tent correlation identity
   and the adjacent-block Haar-detail identity;
4. determine whether every dyadic increment is
   \(O_\varepsilon(L^3X^\varepsilon)\), or isolate the first exact missing
   actual-coefficient theorem;
5. audit the coherent dechirped array, the one-site array, global Parseval,
   both parity peaks, endpoints, and the full factor-\(L\) ledger; and
6. state precisely what a finite character-Poisson transform on the common
   Fejer frequency would have to prove before any positive dual-mode sum.

A rigorous route-specific no-go is a successful result.  Do not infer any
other hard-TOP channel, BAL, UNBAL, M9--M2, M1, GAR, endpoint, bridge,
quarter-theorem, or exponent conclusion.
