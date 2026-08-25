# Round 146 barrier packet

The authoritative starting graph is
7d56a2cf6725cbcbd1746e41c300e01bd2028b9a855cbd057e02546df8a4d18d.
Round 145 proved, but did not estimate, the exact reduction

\[
\mathfrak T_N=
\sum_M\sum_{1\le t<M^{1/4}}
\sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M\\
|k_{s,t}^2-Nst^2|>M^{3/4}}}
(st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
C(st^2)e(t\sqrt{Ns})
+O_{\varepsilon,V}(X^\varepsilon).
\]

Here \(R=X^{1/4}\), \(N=\lfloor X\rfloor\),
\(\mathcal I_M=\mathbb N\cap[M,B_M)\), \(B_M\le2M\), and
\(k_{s,t}=\lfloor t\sqrt{Ns}+1/2\rfloor\). The retained support has
\(s>M^{1/2}\). Every \(t\ge\lceil M^{1/4}\rceil\) fibre has already
been discharged and must not be recounted.

The accepted coefficient formula

\[
C(st^2)=
\sum_{\substack{\gamma\mid t\\\gamma\ {\rm squarefree}\\
(\gamma,s)=1\\\gamma\ {\rm odd}}}\chi_4(\gamma)
\sum_{\substack{de=s\\e\ {\rm odd}}}\chi_4(e)
\sum_{\substack{ab=t/\gamma\\b\ {\rm odd}\\eb^2>4da^2}}1
\]

is multiplicity one. Equivalently,

\[
C(st^2)=
\sum_{de=s}^{\rm ord}
\sum_{\substack{Gab=t\\(da,eb)=1\\Geb\ {\rm odd}\\
eb^2>4da^2}}\chi_4(Ge).
\]

The common factors in these two formulas are different objects; do not
merge their coprimality conditions.

On a dyadic \(t,d,e\) box,

\[
t\asymp T,\qquad d\asymp D,\qquad e\asymp E,\qquad
DE\asymp M/T^2,
\]

the phase is

\[
f(t,d,e)=\sqrt N\,t\sqrt{de}.
\]

Ordered as \(t,d,e\), its dimensionless scaled Hessian is

\[
f^{-1}\operatorname{diag}(t,d,e)\nabla^2f\operatorname{diag}(t,d,e)
=
\begin{pmatrix}
0&1/2&1/2\\
1/2&-1/4&1/4\\
1/2&1/4&-1/4
\end{pmatrix},
\qquad \det=1/4.
\]

This determinant is a candidate interface only. The literal amplitude
contains the factor count, parity, character, cone, squarefree and
coprimality restrictions, profile, and the discontinuous mask. A
coefficient-blind \(t\)-shell has weighted price

\[
\ll X^\varepsilon M^{1/4}/T.
\]

The \(t=1\), \(D=1\), \(E=1\), cone-boundary, and terminal-block faces
must be checked separately. In particular,
\(C(p)=\chi_4(p)\ne0\) for odd primes \(p>4\), and the accepted family
\(N=sL^2+1\) has \(j=-st^2\) with slowly rotating
\(e(t\sqrt{Ns})\). Neither is a lower bound, but both prohibit a
large-\(t\)-only or uniform-frequency argument.

The target is an \(O_{\varepsilon,V}(X^\varepsilon)\) estimate for the
displayed survivor, or a strict smaller survivor whose entire complement
is proved target-safe. Preserve the individual positive complex
direction and the fixed centre. The independent Round-138 cross owner
and all M2, endpoint, M9, bridge, and exponent claims remain outside this
round.
