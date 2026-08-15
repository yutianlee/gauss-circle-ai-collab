# Conductor review: compact gamma quotient and signed top

Campaign: m9-m1-beta-double-bounded-cell

Verdict: exact local algebra verified; full-cell promotion deferred to an
explicit-amplitude validation round.

The mask

\[
\Theta_{\rm db}(L,\beta)=\psi(\beta)\chi_0(L+\beta)
\]

makes \(\beta\), \(\alpha=L+\beta\), and \(L=\alpha-\beta\) compact.
The full diagonal quotient is

\[
C_{\sigma,\zeta}e^{i\{\alpha\log(4/\pi)-\beta\log\pi\}}
R_\alpha(\alpha)R_\beta(\beta).
\]

The exponential is an exact \(x\)-independent unit phase. At
\(\sigma=5/4\), the gamma arguments have real parts

\[
\frac98+\frac\zeta4,\quad \frac38-\frac\zeta4,\quad
\frac58-\frac\zeta4,\quad -\frac18+\frac\zeta4.
\]

No numerator pole occurs for \(0<\zeta<1/2\); approach of the last
denominator to the pole of \(\Gamma\) at zero makes its reciprocal tend
to zero. The exact quotient and fixed connector derivatives are therefore
bounded on the compact cell. Stirling is not needed.

Put

\[
A=-1-\frac b2-i(L+\beta),\qquad
D=A+\frac i2(L-\nu).
\]

The physical top is

\[
\frac1{2\pi}\frac1{0^++i(L-\nu)}
=\frac12\delta_L(\nu)-\frac{i}{2\pi}
\operatorname{PV}\frac1{L-\nu}.
\]

For \(H(L,\nu)=g(L,\beta)p(\nu)\), use

\[
\operatorname{PV}\int_{\mathbb R}\frac{dy}{y(A+iy/2)}
=\frac{i\pi}{A}.
\]

The exact cancellation-preserving functional is

\[
\boxed{\frac{gp(L)}A-\frac{ig}{2\pi}\int_{\mathbb R}
\frac{p(\nu)-p(L)}{(L-\nu)D}\,d\nu.}
\]

Only the divided difference may be put under an absolute value. Taking
absolute values before delta/PV recombination retains a false divergent
diagonal tail.

The raw phase gives

\[
x\partial_x\{g(L,\beta)p(\nu)\}
=-i\eta gp,\qquad \eta=\frac{L+\nu}{2}+\beta.
\]

On the diagonal \(\eta=\alpha=L+\beta\), so the differentiated numerator
\(\eta p(\nu)-\alpha p(L)\) vanishes to first order at \(\nu=L\).
The genuine cubic height tail and first moment control the value and one
\(x\)-derivative. Smooth spatial shares are easier because
\(|\eta/D|\ll1\).

This verifies the gamma phase, Plemelj sign, diagonal constant, and
derivative algebra. It does not certify the finite post-routing one-count
assembly.

