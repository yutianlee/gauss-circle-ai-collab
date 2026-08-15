# Candidate beta double-bounded cell kernel

Status: candidate only. Acceptance is controlled by
state/proof_obligations.yml.

Fix

\[
\sigma=\frac54,\quad b=\frac1{\log(2X)},\quad
r=\frac54-\frac{a+b}{2},\quad p=\frac54+\frac{a+b}{2},
\]

and

\[
\Theta_{\rm db}(L,\beta)=\psi(\beta)\chi_0(L+\beta).
\]

Let

\[
\mathcal G=C_{\sigma,a+b}
e^{i\{\alpha\log(4/\pi)-\beta\log\pi\}}
R_\alpha(\alpha)R_\beta(\beta),
\]

\[
g=\Theta_{\rm db}\mathcal G
e^{iL\log(D_j/(2q\sqrt{Xx}))}e^{-i\beta\log(hqx)},
\]

\[
p_x(\nu)=
e^{i\nu\log(2\sqrt X(H_j+1)/(D_j\sqrt x))}
\widehat\phi(b+i\nu),
\]

\[
A=-1-\frac b2-i(L+\beta),\qquad
D=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right).
\]

The singular top functional is

\[
\mathsf P=\frac{gp_x(L)}A-\frac{ig}{2\pi}\int_{\mathbb R}
\frac{p_x(\nu)-p_x(L)}{(L-\nu)D}\,d\nu.
\]

For a smooth normalized spatial profile \(\mathscr W\), put

\[
\mathsf S=\frac g{2\pi}\int_{\mathbb R}
\frac{p_x(\nu)\mathscr W(L-\nu)}D\,d\nu.
\]

The finite post-routing family replaces compact multipliers and profiles
by their exact finite connector derivatives under identical ownership.
Its aggregate amplitude is

\[
\begin{aligned}
\mathcal A(x)={}&-\pi i\sum_j\sum_{h,q\ge1}
\chi_4(q)h^{-r}q^{-p}
\left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b\\
&\times\int_{\mathbb R^2}\frac{dL\,d\beta}{(2\pi)^2}
\{\mathbf1_{j=0}\mathsf P+\mathsf S\},
\end{aligned}
\]

with the finite connector-family sum understood.

The candidate estimate is

\[
\sup_{1\le x\le N_X}
\{|\mathcal A(x)|+x|\mathcal A'(x)|\}\ll\log^C(2X).
\]

Its key derivative is

\[
x\partial_x(gp_x)
=-i\left(\frac{L+\nu}{2}+\beta\right)gp_x.
\]

The signed top is formed before absolute values. The \(h,q\) series are
absolute, and the actual dyadic sum is polylogarithmic.

Then

\[
\begin{aligned}
&\sqrt X\int_1^{N_X}x^{-3/2-b/2}e(\sqrt{Xx})\mathcal A(x)\,dx\\
&=\frac1{\pi i}
\left[x^{-1-b/2}e(\sqrt{Xx})\mathcal A(x)\right]_1^{N_X}\\
&\quad-\frac1{\pi i}\int_1^{N_X}e(\sqrt{Xx})
\frac d{dx}\{x^{-1-b/2}\mathcal A(x)\}\,dx
\ll\log^C(2X).
\end{aligned}
\]

The endpoints have full coefficients and are estimated locally, not by
the global unmasked endpoint theorem. Restoring the external factor gives
the candidate \(O_\varepsilon(X^{1/4+\varepsilon})\) bound.

An isolated verifier must still receive the explicit finite post-routing
family and establish that every connector/profile derivative satisfies
the same estimate, all actual endpoint blocks and floors are included,
and artificial, axial, collision, corner, endpoint, and arithmetic
modules are excluded exactly once. Until then this is not accepted.

