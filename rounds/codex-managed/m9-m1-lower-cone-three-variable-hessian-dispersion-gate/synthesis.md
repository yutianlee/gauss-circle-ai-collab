# Round 146 synthesis

Round 146 closes under

\[
\boxed{\mathsf{three\_variable\_dispersion\_no\_go}.}
\]

The round proves one exact simplification. If
\(\mathfrak S_N^{<,>}\) is the masked Round-145 small-\(t\) scalar and
\(\mathfrak U_N^{<}\) is the same scalar without the nearest-square
mask, then

\[
\mathfrak S_N^{<,>}
=\mathfrak U_N^{<}+O_{\varepsilon,V}(X^\varepsilon).
\]

Together with the already proved unmasked large-\(t\) tail,

\[
\mathfrak T_N
=\mathfrak U_N^{<}+O_{\varepsilon,V}(X^\varepsilon).
\]

The two error owners are disjoint in the exact partition

\[
\{t<M^{1/4},|j|>M^{3/4}\}
\dot\cup
\{t<M^{1/4},|j|\leq M^{3/4}\}
\dot\cup
\{t\geq\lceil M^{1/4}\rceil\}.
\]

Thus the first open scalar is now

\[
\mathfrak U_N^{<}=
\sum_M\sum_{1\leq t<M^{1/4}}
\sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M}}
(st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
C(st^2)e(t\sqrt{Ns}),
\]

with the exact multiplicity-one Round-145 coefficient, cone, profile,
endpoints, fixed center, and positive complex direction retained.

The advertised three-variable Hessian is genuinely nondegenerate:

\[
f^{-1}\operatorname{diag}(t,d,e)\nabla^2f
\operatorname{diag}(t,d,e)=
\begin{pmatrix}
0&1/2&1/2\\
1/2&-1/4&1/4\\
1/2&1/4&-1/4
\end{pmatrix},
\qquad\det=\frac14.
\]

It does not prove cancellation. The exact coefficient is not a smooth
or separated tensor; \(t=1\) remains a rank-one face with
owner-sized capacity; a \(t\)-difference returns rank-one phases and
an unproved coefficient correlation; and the full smooth transform
returns the same monomial at the phase level after orthant reversal.

The strongest favorable primary-source test is Cao--Zhai Theorem 6.
Its only legal placement uses exponents \((1/2,1,1/2)\) in
\((d,t,e)\), but its coefficient class is \(a(d)b(t,e)\). Even after
granting this missing separation, its balanced top-box first term is

\[
R^{3/8-5\tau/8+\varepsilon},
\]

leaving \(R^{1/16+\varepsilon}\) at the formal
\(\tau=1/2\) endpoint. Robert--Sargos and Sargos--Wu leave
\(R^{1/4+\varepsilon}\) there. These are limitations of the displayed
upper bounds, not lower bounds for the signed scalar.

The round therefore creates an exact small-\(t\) unmasking reduction
and a scoped three-variable dispersion obstruction. It proves no
strict fixed-power \(t\)-corridor, no lower-radial target, and no
downstream theorem.

The independent Round-138 cross owner, direct M1 parents, all M2
owners, endpoint uniformity, M9, and the bridge remain open. The
internally proved exponent remains \(1/3\); the separately audited
external exponent remains

\[
\frac{3292+25\sqrt{1717}}{13762}
=0.3144831759740614\ldots;
\]

the target \(1/4\) remains open.
