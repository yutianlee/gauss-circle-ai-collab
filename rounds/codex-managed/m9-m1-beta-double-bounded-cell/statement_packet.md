# Round 42 statement packet: double-bounded beta cell

This packet is the frozen statement for independent rederivation. It is
not a proof and does not authorize reading another Round-42 report.

Fix

\[
c'=\frac54,\qquad b=\frac1{\log(2X)},\qquad
r=\frac54-\frac{a+b}{2},\qquad
p=\frac54+\frac{a+b}{2},
\]

with the accepted small positive contour parameters. In beta-slab
coordinates

\[
u=a+i(L-\nu),\qquad v=b+i\nu,\qquad
s=\frac54+i\left(\frac L2+\beta\right),
\qquad \alpha=L+\beta.
\]

Use the hierarchical beta mask \(\psi(\beta)\) and a fixed smooth central
cutoff \(\chi_0(\alpha)\) supported where both \(|\beta|\) and
\(|\alpha|\) are bounded. This is the double-bounded box owned by the
beta branch. The two large-alpha complements were closed in Round 41.

Before the radial, height, and compact archimedean integrations, one exact
terminal share has coefficient

\[
\mathfrak a_{j,h,q,x}=(-\pi i\sqrt X)e(\sqrt{Xx})
h^{-r}q^{-p}\left(\frac{D_j}{2\sqrt X}\right)^a
(H_j+1)^b x^{-3/2-b/2},
\]

and exact unit phase

\[
\begin{aligned}
 &(L-\nu)\log\frac{D_j}{2\sqrt X}
 +\nu\log(H_j+1)-L\log q-\beta\log(hq)
 -\frac12(L+\nu+2\beta)\log x\\
 &=L\log\frac{D_j}{2q\sqrt{Xx}}
 +\nu\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}
 -\beta\log(hqx).
\end{aligned}
\]

The exact gamma quotient is

\[
C_{\sigma,\zeta}
e^{i\{\alpha\log(4/\pi)-\beta\log\pi\}}
R_\alpha(\alpha)R_\beta(\beta),
\]

with

\[
R_\alpha=
\frac{\Gamma((1+\sigma+\zeta/2)/2+i\alpha/2)}
{\Gamma((2-\sigma-\zeta/2)/2-i\alpha/2)},
\qquad
R_\beta=
\frac{\Gamma((\sigma-\zeta/2)/2+i\beta/2)}
{\Gamma((1-\sigma+\zeta/2)/2-i\beta/2)}.
\]

No Stirling or Morse approximation is permitted in the central box. Set

\[
p_x(\nu)=
\exp\!\left(i\nu\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}\right)
\widehat\phi(b+i\nu),
\]

and

\[
D(L,\nu;\beta)=-1-\frac b2
-i\left(\frac{L+\nu}{2}+\beta\right).
\]

The singular hard-top share must retain the exact signed Plemelj
distribution in \(\mu=L-\nu\); its diagonal Cauchy section is formed
before absolute values. Smooth top and interior shares use their ordinary
\(\mu\)-integration and normalized fixed spatial Mellin profiles.

The candidate direct theorem is:

\[
\boxed{
\sup_{1\le x\le N_X}|\mathcal A(x)|
+\int_1^{N_X}|\partial_x\mathcal A(x)|\,dx
\ll_\varepsilon X^\varepsilon,}
\]

where \(\mathcal A(x)\) is the complete compact \((\alpha,\beta)\),
height, profile, and absolutely convergent \((h,q,j)\) amplitude after
the common post-routing ownership operations, but before
\(\sqrt Xx^{-3/2-b/2}e(\sqrt{Xx})\) is integrated. An equivalent
weighted form with \(x|\mathcal A'(x)|\) is acceptable if stated exactly.
The required radial consequence is

\[
\sqrt X\int_1^{N_X}x^{-3/2-b/2}e(\sqrt{Xx})
\mathcal A(x)\,dx\ll_\varepsilon X^\varepsilon,
\]

by one exact radial integration by parts, including its full endpoint
coefficients and every pre-existing profile or product-equality star at
its already assigned value.  The continuous radial integration by parts
does not itself create a half-weight.
Restoring the already fixed external factor would give
\(O_\varepsilon(X^{1/4+\varepsilon})\) for the full double-bounded beta
cell.

The displayed amplitude theorem is a candidate, not an accepted input.
In particular, a verifier must check whether the post-routing terminal
remainder really admits a standalone radial integration by parts. If the
resulting endpoint functional is only a beta-masked share of the globally
accepted unmasked endpoint module, then the proposed route does not close;
that masked endpoint functional is the exact survivor to record unless an
additional aggregate identity controls it.

Every proof must audit: the signed diagonal and off-diagonal top terms;
one \(x\)-derivative of the modulated height profile; the exact compact
gamma ratios; absolute \(h,q\) convergence; the actual dyadic scale sum;
hard-top and smooth profiles; endpoint stars; and the global post-routing
ownership of endpoint, arithmetic, axial, connector-axis, collision,
corner, and artificial-pole modules. It must not infer a separate masked
boundary-module limit that the graph does not provide.
