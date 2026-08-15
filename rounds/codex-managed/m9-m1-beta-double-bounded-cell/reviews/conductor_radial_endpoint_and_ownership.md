# Conductor review: radial endpoints and ownership

Campaign: m9-m1-beta-double-bounded-cell

Assume

\[
\sup_{1\le x\le N}|\mathcal A(x)|
+\int_1^N|\mathcal A'(x)|\,dx\ll_\varepsilon X^\varepsilon.
\]

Since

\[
\frac d{dx}e(\sqrt{Xx})
=\pi i\sqrt X\,x^{-1/2}e(\sqrt{Xx}),
\]

exact integration by parts gives

\[
\begin{aligned}
&\sqrt X\int_1^N x^{-3/2-b/2}e(\sqrt{Xx})\mathcal A(x)\,dx\\
&=\frac1{\pi i}
\left[x^{-1-b/2}e(\sqrt{Xx})\mathcal A(x)\right]_1^N\\
&\quad-\frac1{\pi i}\int_1^N e(\sqrt{Xx})
\frac d{dx}\{x^{-1-b/2}\mathcal A(x)\}\,dx.
\end{aligned}
\]

Thus the radial integral is \(O_\varepsilon(X^\varepsilon)\). The two
continuous radial endpoints have full coefficients. A half-value can
occur only inside a pre-existing profile, product-equality, or
inverse-Mellin star.

The bracket is a beta-masked local trace and cannot be discarded by
citing the unmasked three-mask endpoint theorem. It can instead be
controlled by proving the displayed value bound directly. Equivalently,
on the fixed terminal line use

\[
R_1(\rho)=G(\rho)-E_1(\rho)
\]

with the same mask and without another contour shift. For

\[
G(\rho)=\int_1^N x^{\rho-1}e(\sqrt{Xx})\,dx,\qquad
\Re\rho=-1-\frac b2,
\]

one has

\[
|G|+|\partial_{\Im\rho}G|\ll1.
\]

Also

\[
E_1(\rho)=\frac{N^\rho e(\sqrt{XN})-e(\sqrt X)}{\rho}
\]

satisfies

\[
|E_1|+|\partial_{\Im\rho}E_1|
\ll\frac{1+N^{-1-b/2}\log N}{1+|\Im\rho|}.
\]

This is a direct local estimate, not an identification of the local
\(E_1\) with the globally routed endpoint module. The discovery and
hostile proofs use this route. The statement-only packet did not display
the full amplitude needed to test it, so the full-cell promotion is
deferred while this conditional radial reduction is accepted.

