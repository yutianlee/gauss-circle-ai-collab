# Blind diagonal single-transition kernel

## 1. Result

Write
\[
u=a+i\mu,\quad v=b+i\nu,\quad z=\zeta+i\eta,\quad
s=\sigma+it,\qquad \zeta=a+b,\quad\eta=\mu+\nu,
\]
and
\[
\alpha=t+\eta/2,\qquad\beta=t-\eta/2.
\]
The exact Round-19 gamma quotient factors into one \(\alpha\)-factor and one \(\beta\)-factor. If \(\beta\) is bounded and \(|\alpha|\) is large, only the \(\alpha\)-factor admits Stirling reduction; the bounded \(\beta\)-factor remains an exact meromorphic multiplier. The opposite transition is obtained by interchanging \(\alpha,\beta\). This is a degree-one transition normal form, not an operator estimate. All finite sides and residues remain outside it.

## 2. Exact statement and hypotheses

On the terminal line \(\sigma=c'>1+\zeta/2\), define
\[
\begin{aligned}
R_\alpha&=
\frac{\Gamma((1+\sigma+\zeta/2)/2+i\alpha/2)}
{\Gamma((2-\sigma-\zeta/2)/2-i\alpha/2)},\\
R_\beta&=
\frac{\Gamma((\sigma-\zeta/2)/2+i\beta/2)}
{\Gamma((1-\sigma+\zeta/2)/2-i\beta/2)}.
\end{aligned}
\]
Then exactly
\[
\boxed{K_z(1-s)=C_{\sigma,\zeta}
e^{\,i\{\alpha\log(4/\pi)-\beta\log\pi\}}R_\alpha R_\beta,}
\qquad
C_{\sigma,\zeta}=2^{2\sigma+\zeta-1}\pi^{1-2\sigma}.
\tag{1}
\]
For fixed \(B\), uniformly on \(|\beta|\le B\),
\[
R_\alpha=
\left|\frac{\alpha}{2}\right|^{\sigma+\zeta/2-1/2}
e^{i\varphi_\alpha}\{1+O_B(|\alpha|^{-1})\},
\quad
\varphi_\alpha=\operatorname {sgn}(\alpha)
\left(|\alpha|\log\frac{|\alpha|}{2}-|\alpha|+\frac\pi4\right).
\tag{2}
\]
Uniformly on \(|\alpha|\le B\),
\[
R_\beta=
\left|\frac{\beta}{2}\right|^{\sigma-\zeta/2-1/2}
e^{i\varphi_\beta}\{1+O_B(|\beta|^{-1})\},
\quad
\varphi_\beta=\operatorname {sgn}(\beta)
\left(|\beta|\log\frac{|\beta|}{2}-|\beta|-\frac\pi4\right).
\tag{3}
\]
The exact bounded factor \(R_\beta\), respectively \(R_\alpha\), is not replaced by Stirling.

## 3. Derivation and transition kernel

The four gamma arguments in Round 19 have imaginary parts
\[
\beta/2,\quad\alpha/2,\quad-\beta/2,\quad-\alpha/2,
\]
which proves (1). The standard signed Stirling identity
\[
\frac{\Gamma(A+iy)}{\Gamma(B-iy)}
=|y|^{A-B}e^{i\,\operatorname {sgn}(y)
\{2|y|\log|y|-2|y|+\pi(A+B-1)/2\}}
\{1+O(|y|^{-1})\}
\]
gives (2), since \(A_\alpha+B_\alpha=3/2\), and (3), since
\(A_\beta+B_\beta=1/2\).

Use \((\alpha,\beta,\nu)\) as coordinates:
\[
t=(\alpha+\beta)/2,\quad\eta=\alpha-\beta,\quad
\mu=\alpha-\beta-\nu.
\tag{4}
\]
The Lebesgue Jacobian has modulus one (orientation is inherited), and the finite box becomes
\[
|\nu|\le V,\quad|\alpha-\beta-\nu|\le U,\quad
|\alpha+\beta|\le2S.
\tag{5}
\]
For a dual incidence \(hq=m\), retain the exact profile amplitude
\[
\begin{aligned}
\mathcal B_j^{(\alpha)}={}&
C_{\sigma,\zeta}R_\beta
\left|\frac{\alpha}{2}\right|^{\sigma+\zeta/2-1/2}
\widehat W_j(a+i(\alpha-\beta-\nu))\widehat\phi(b+i\nu)\\
&\times\left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
\left(\frac hq\right)^{\zeta/2}m^{-\sigma},
\end{aligned}
\tag{6}
\]
where \(D_j=2^{-j}\lfloor\sqrt X\rfloor\),
\(H_j=\lfloor D_jX^{-1/4}\rfloor\), and
\(\widehat W_0=1/u+\widehat W_{+,r}\) is unchanged. Substituting the exact
\[
G_v(1-s)=\int_1^{N_X}x^{-\sigma-3/4-b/2}
e^{\,i\{2\pi\sqrt{Xx}-(\alpha+\beta+\nu)\log x/2\}}\,dx
\]
shows that the \(\beta\)-bounded transition has the one-large phase
\[
\begin{aligned}
\Psi_\alpha(x)={}&2\pi\sqrt{Xx}
-\frac{\alpha+\beta+\nu}{2}\log x
-\frac{\alpha+\beta}{2}\log m\\
&+(\alpha-\beta-\nu)\log\frac{D_j}{2\sqrt X}
+\nu\log(H_j+1)
+\frac{\alpha-\beta}{2}\log\frac hq\\
&+\alpha\log(4/\pi)-\beta\log\pi+\varphi_\alpha .
\end{aligned}
\tag{7}
\]
Thus the finite transition contribution is exactly the Round-19 measure
\(\mathbf1_{hq=m}\chi_4(q)(2\pi)^{-3}d\alpha\,d\beta\,d\nu\,dx\),
over (5), times (6), \(e^{i\Psi_\alpha(x)}\), and the Stirling remainder.
For the \(\alpha\)-bounded transition replace (6)'s \(R_\beta\) and
\(\alpha\)-power by \(R_\alpha|\beta/2|^{\sigma-\zeta/2-1/2}\), and
replace \(\varphi_\alpha\) in (7) by \(\varphi_\beta\).

The arithmetic residue, height residue, top \(u=0\) Perron residue, joint
corner, and radial endpoint stars remain exactly those of Round 19. The
coordinate change crosses no contour and creates no residue.

The radial horizontal sides are also retained. On the upper/lower original
\(w\)-sides, after \(s=1-w\), \(t=\mp S\), hence
\[
(\alpha,\beta)=(\mp S+\eta/2,\ \mp S-\eta/2).
\tag{8}
\]
No decay or deletion of these side integrals is inferred from (2)–(3).

## 4. First doubtful or unproved step

The first unproved step is a uniform signed estimate for (7) after summing
scales and dual incidences, or any nested exhaustion that removes the sides
(8) while preserving the symmetric top Perron limit.

## 5. Required controls and outcomes

The conductor becomes exactly \(4(1+|\alpha|)(1+|\beta|)\). The constants
\(+\pi/4\) and \(-\pi/4\) follow from the gamma-pair sums \(3/2\) and
\(1/2\). The unit Jacobian, finite polytope (5), floors, top \(1/u\), and
endpoint star all remain visible. Controls pass algebraically; no numerical
experiment was used.

## 6. Dependencies and exact artifacts used

Only the authorized protocol, graph, active campaign, Round-19 synthesis
and blind finite-vector report, Round-15 completion formulas, and Round-20
brief were used.

## 7. Recommended state effect

Promote the exact diagonal factorization (1), transition normal forms
(2)–(3), and phase (7) as finite algebraic infrastructure. Retain the swept
transition operator, every horizontal-side limit, maximal Perron problem,
GAR, and M9-M1 as open.
