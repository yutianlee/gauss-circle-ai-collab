# Round 62 statement-only packet: subcritical small-angle collapse

This is the complete packet for the statement-only task.

Let
\[
 R=X^{1/4},\qquad Y=\sqrt X,\qquad y=\lfloor\sqrt X\rfloor,
\]
and use the accepted exact denominator partition
\[
 \mathbf1_{1\le d\le y}
 =w_0(d)+\sum_{j=1}^{J}w_j(d)+w_{\rm bot}(d),
\]
where \(D_j=2^{-j}y\), \(H_j=\lfloor D_j/R\rfloor\), every active
profile is nonnegative, and the bottom remainder is supported on
\(d<4R/3\).  The top and interior weights telescope from
\[
 W(t)=\eta(t)-\eta(2t).
\]

For \(n=hq\), \(q\) positive and odd, put
\[
 d_{n,h}=2h\sqrt{\frac Xn}.
\]
The accepted angular coefficient is
\[
 \mathcal C_X^*(n)=
 \sum_{\substack{h\mid n\\q=n/h\ {\rm odd}}}
 \chi_4(q)\Omega_X^*(n,h),
\]
\[
 \Omega_X^*(n,h)=
 \sum_j\mathbf1_{h\le H_j}
 \Phi\!\left(\frac h{H_j+1}\right)[w_j(d_{n,h})]^*.
\tag{62.1}
\]
The inactive bottom range is not in (62.1) and is already target-safe
before Fourier expansion.

The Vaaler profile is
\[
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u,\qquad 0<u<1,
\tag{62.2}
\]
with \(\Phi(0)=1\).  Direct Taylor expansion suggests
\[
 \Phi(u)=1-\frac{\pi^2}{3}u^2+O(u^3)
\quad(u\to0).
\tag{62.3}
\]

Fix \(0<\nu<1/2\) and a smooth radial block \(n\asymp N=X^\nu\).
For an active profile containing \(d_{n,h}\),
\[
 \frac{h}{H_j+1}\asymp \sqrt{\frac nY}
 =X^{(\nu-1/2)/2}\to0.
\tag{62.4}
\]
The desired exact reduction is therefore
\[
 \Omega_X^*(n,h)
 =
 \mathbf1_{d_{n,h}\le y}^{*}
 +O\!\left(\frac nY\right),
\tag{62.5}
\]
with the exact meaning of the star and all floor, top, support, and
bottom qualifications proved rather than assumed.

Since \(d_{n,h}\le y\) is equivalent up to the exact
\(y/\sqrt X\) factor to
\[
 h\le\frac{y}{2\sqrt X}\sqrt n,
\tag{62.6}
\]
the candidate limiting coefficient is
\[
 \mathcal D_X^*(n)=
 \sum_{\substack{h\mid n,\ q=n/h\ {\rm odd}\\
 2h\sqrt{X/n}\le y}}^{*}\chi_4(q).
\tag{62.7}
\]
For a fixed smooth \(n\asymp N\) block, the triangle estimate for the
coefficient error suggested by (62.5) is
\[
 \sum_{n\asymp N}n^{-3/4}\tau(n)\frac nY
 \ll_\varepsilon \frac{N^{5/4+\varepsilon}}Y.
\tag{62.8}
\]
Thus it would be normalized target-safe for \(N\le
X^{2/5-\epsilon_0}\), if (62.5) is exact enough and no omitted owner
changes the ledger.

Tasks:

1. Prove or refute (62.5), including the exact floor factor
   \(H_j+1\), active cutoff, partition stars, \(d=y\), and bottom
   remainder.
2. Derive the sharp uniform bound for \(\Phi(u)-1\) in the actual
   supported range.
3. Prove the total radial error and identify the exact power threshold;
   distinguish fixed \(\nu<2/5\), \(\nu=2/5\), and logarithmic losses.
4. Determine the exact arithmetic form of \(\mathcal D_X^*(n)\) and
   whether elementary character/divisor identities simplify it.
5. Attempt a signed estimate for
\[
 \sum_n V(n/N)\mathcal D_X^*(n)n^{-3/4}e(\sqrt{Xn}).
\tag{62.9}
\]
   A precise return-map or capacity no-go is acceptable.

Do not promote full GAR, M9-M1, M9, or an exponent without a new signed
estimate.  No numerical experiment is requested.

