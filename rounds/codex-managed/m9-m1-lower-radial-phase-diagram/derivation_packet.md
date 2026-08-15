# Round 61 derivation packet: lower-radial phase diagram

This is the complete statement-only packet. No other report is needed.

Put

\[
 R=X^{1/4},\qquad Y=\sqrt X,
\]

and let a smooth radial block have \(n\asymp N=X^\nu\), with
\(0\le\nu\le1/2\). On a denominator block \(d\asymp D=X^\delta\),
\(1/4\le\delta\le1/2\), the exact stationary relation is

\[
 n={4Xh^2\over d^2}.
\]

Therefore its primal frequency scale is expected to be

\[
 h\asymp L={D\sqrt N\over2\sqrt X},\qquad
 \ell=\log_XL=\delta+{\nu-1\over2}.
\tag{61.1}
\]

The active Vaaler height is \(H_D=\lfloor D/R\rfloor\), so the formal
frequency triangle is

\[
 {1\over4}\le\delta\le{1\over2},\qquad
 0\le\ell\le\delta-{1\over4}.
\tag{61.2}
\]

Audit floors and bounded-height exceptions rather than using exponents
where \(L=O(1)\).

Accepted inputs:

1. Terminal theorem:
\[
 B_1(D,L;X)\ll_\varepsilon X^\varepsilon(1+D/L),
\]
which reaches the physical \(X^{1/4}\) target on
\(L\asymp H_D\), i.e. \(\ell=\delta-1/4\).

2. TTY theorem:
\[
 B_1(D,L;X)
 \ll_\varepsilon
 X^{[89(1+\ell)+819\delta]/1282+\varepsilon},
\]
which reaches the target when

\[
 178\ell+1638\delta\le463.
\tag{61.3}
\]

3. The accepted second-derivative endpoint is

\[
 (\delta,\ell)=\left({1\over2},0\right).
\tag{61.4}
\]

4. The exact residual corridor is

\[
 \mathcal U_1=
 \{(\delta,\ell):1/4\le\delta\le1/2,
 0\le\ell<\delta-1/4,
 178\ell+1638\delta>463\}
 \setminus\{(1/2,0)\}.
\tag{61.5}
\]

5. Round 60 proves, separately and more strongly, every fixed smooth
critical sector \(\nu=1/2\) compactly inside the radial product range.

Tasks:

- Substitute (61.1) into (61.2)--(61.5) exactly.
- For each fixed radial exponent \(\nu\), determine which spatial scales
  \(\delta\) occur and which are closed. Full radial-sector closure
  requires every actual contributing scale, not merely one choice of
  \(\delta\), unless exact profile support proves otherwise.
- Optimize the TTY inequality and identify exact boundary rationals.
- Include the \(L=O(1)\), \(H_D=O(1)\), hard-top, floor, star, and smooth
  radial multiplier ledgers.
- State the first uncovered radial sector and the exact remaining
  blockwise theorem or saving it needs.

No numerical experiment is requested. No claim may be made for full GAR,
M9-M1, M9, or the Gauss-circle exponent without a new estimate.
