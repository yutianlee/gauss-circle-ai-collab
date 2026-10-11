# Round227 complete actual signed interface

Graph SHA256 a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
All definitions are fixed for the round; no mathematical gain is granted.
For real T>=2, every real cT<=R<=CT, let P be the smallest dyadic
integer >=T^(3/2). Fix real smooth phi=1 on x<=1, phi=0 on x>=2,
w(x)=phi(x)-phi(2x), and the accepted real even Schwartz Psi from rho.
For every dyadic2<=N<=P put
\[
g_N(t)=(t/N)^{-3/4}\Psi(\sqrt{t/T})w(t/N),\quad
A_J=(1+N/T)^{-J},\quad z_n=r_2(n)g_N(n)e(R\sqrt n).
\]
Smooth zero extension gives support N/2<t<2N and all fixed scaled
derivatives O(A_J), after reserving sufficient fixed Schwartz order.
Positive integers are literal. Define
\[
C_h=\sum_n z_{n+h}\overline{z_n},\quad
\rho_h=\frac8h\sum_{d\mid h}(-1)^{h+d}d,
\quad W_h(x)=g_N(x+h)g_N(x)e(R(\sqrt{x+h}-\sqrt x)),
\]
\[
{\cal R}_h=C_h-\rho_h\int_0^\infty W_h(x)\,dx.
\]
The COMPLETE selected sufficient bound, with H=2N, is
\[
2\Re\sum_{h=1}^{2N-1}(1-h/(2N)){\cal R}_h
\le C_{\epsilon,J} A_J^2 N^{3/2}T^\epsilon.                 \tag{F}
\]
One outer real part, all h, no individually absolute remainders. A
discrete-empty overlap need not have zero continuous density; its
compensating remainder stays. The ambient integer length L=3N/2-1.
Exact Fejer factor is (L+H-1)/H; normalized shell is N^-3/4 sum z_n.
Diagonal is O(A_J^2N^(1+eta)); density integral is O(A_J^2N^(3/2)/(Th)).
After normalized squaring those give A_J^2[N^-1/2+eta+T^-1N^eta logN].
The partition telescopes to phi(n/P) for every n>=2; residual n>P is
arbitrarily small at fixed Schwartz order. Singleton is O(1).
Thus (F) gives the full complex wave T^epsilon, hence real B_T and
P(R^2)=sqrt(R)B_T(R)/pi+O(T^(1/2+epsilon)), the quarter theorem.
This is a stronger sufficient complex route; beta is only complete REAL.

## Exact available spectral starting point

Closed226 report actual_shifted_spectral_sources, equations20--22, binds
HKLDW1705.04771v3. With q_h(y)=W_h(Ny-h),
qhat_h(s)=integral_0^infty q_h(y)y^(s-1)dy,
\[
{\cal R}_h=\frac1{2\pi i}\int_{(\sigma)}N^s\widehat q_h(s)
\left[D_2(s;h)-r_2(h)h^{-s}
             -\frac{\rho_hh^{1-s}}{s-1}\right]ds.          \tag{M}
\]
Initially sigma>1 sufficiently large. D2 includes n=0 and uses(n+h)^-s;
the atom's transform is zero but it is explicitly subtracted. The density
term is the Mellin transform on[h,infinity), so it is exactly centered.
All discrete and three-cusp continuous terms and further residues must
be retained. It is not an assertion that unproved contour shifts converge.

The actual scaled phase in q_h is 2pi R sqrt(N)[sqrt(y)-sqrt(y-h/N)],
with y and y-h/N both in(1/2,2). Its dimensionless variation is
Lambda_h~Rh/sqrt(N). The Mellin transform has polynomially growing norms,
and the gamma quotient does not exponentially suppress spectral heights
|t|<=|Im s|. Source226's absolute transfer already loses; joint phases
and actual spectral coefficients must enter before taking norms.

AH2607.13518v1 supplies a fixed-level, fixed-Heegner-point fourth moment
and its actual-r2 application. It does not automatically identify the
HKLDW coefficient <V,mu_j> with a Heegner value. Audit that exact seam.
The source's printed mean-square4/2 is literal; do not substitute4/3.
No representation identity, formal kernel, local range or positive
certificate alone is a new complete estimate. All other full-proof
frontiers and unbounded FIXED even-order moments remain as checkpoint226.
