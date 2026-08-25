# Blind statement: prescribed-centre Kloosterman-fraction dispersion gate

Round: 135

This is statement-only input. Do not consult any proof graph, strategy memo,
prior nonblind round, sibling report, or conductor derivation.

Let \(e(t)=e^{2\pi i t}\). Let \(X\ge 2\) be real and set

\[
D=X^\delta,\qquad L=X^\ell,\qquad R=X/D,\qquad
K=XL/D^2,\qquad \Delta=D/L,
\]

where

\[
\frac14\le\delta<\frac12,\qquad
0\le\ell<\delta-\frac14,\qquad
178\ell+1638\delta>463.
\]

Thus \(K/R=L/D=\Delta^{-1}\). Let \(W\) and \(q_L\) be the fixed
uniformly smooth compactly supported profiles of one flat-smooth interior
packet, with \(r\asymp R\) and \(k\asymp K\). Define

\[
\mathscr R_{D,L}(X)=
\sum_{\substack{r\ge1\\r\ \mathrm{odd}}}\chi_4(r)
W\!\left(\frac{X}{rD}\right)
\sum_{k\ge1}\frac{q_L(4Xk/r^2)}{k}e(Xk/r).
\tag{135.B1}
\]

Equivalently, with

\[
\mathcal Q_L(y)=\int_0^\infty \frac{q_L(h)}h e(hy)\,dh,
\]

the same principal packet is

\[
\mathscr R_{D,L}(X)=
\sum_s\sum_{\substack{r\mid s\\r\ \mathrm{odd}}}
\chi_4(r)W\!\left(\frac{X}{rD}\right)
\mathcal Q_L\!\left(\frac{r(X-s)}{4X}\right).
\tag{135.B2}
\]

The effective physical window is \(|s-X|\ll\Delta X^\varepsilon\).
Absolute divisor bounds give

\[
|\mathscr R_{D,L}(X)|\ll_\varepsilon \Delta X^\varepsilon,
\tag{135.B3}
\]

while the required estimate is

\[
\boxed{|\mathscr R_{D,L}(X)|\ll_\varepsilon X^{1/4+\varepsilon}.}
\tag{135.B4}
\]

The candidate source interfaces are these.

**Bettin--Chandee form.** For independent coefficient sequences supported
on dyadic \(a\asymp A\), \(m\asymp M\), \(n\asymp N\), their Theorem 1
estimates

\[
\mathcal B(M,N,A)=
\sum_{\substack{a,m,n\\(m,n)=1}}
\alpha_m\beta_n\nu_a
e\!\left(\vartheta\frac{a\overline m}{n}\right)
\tag{135.B5}
\]

by

\[
\|\alpha\|_2\|\beta\|_2\|\nu\|_2
\left(1+\frac{|\vartheta|A}{MN}\right)^{1/2}
\left((AMN)^{7/20+\varepsilon}(M+N)^{1/4}
+(AMN)^{3/8+\varepsilon}(AN+AM)^{1/8}\right).
\tag{135.B6}
\]

Here \(\overline m\) is the multiplicative inverse modulo \(n\).

**Wright fixed-factor form.** For

\[
\mathcal B(M,N,A;R_0)=
\sum_{\substack{a,m,n\\(m,nR_0)=1}}
\alpha_m\beta_n\nu_a
e\!\left(\vartheta\frac{a\overline m}{nR_0}\right),
\tag{135.B7}
\]

Wright's arXiv:2604.25177v2, Theorem 2.1, assumes \(M\ll N^2\) and
\(R_0\ll M^C\) for a fixed large \(C\), and gives

\[
\begin{aligned}
\mathcal B(M,N,A;R_0)\ll{}&M^\varepsilon
\|\alpha\|_2\|\beta\|_2\|\nu\|_2(AMN)^{1/2}R_0^{1/4}
\left(1+\frac{|\vartheta|A}{MN}\right)^{1/4}\\
&\times\left(
N^{-1/8}+\frac{R_0^{1/8}N^{1/8}}{M^{1/4}}
+\frac{M^{1/10}}{R_0^{3/20}A^{1/20}N^{3/20}}
+\frac{N^{3/20}}{A^{3/20}M^{1/5}}
+\frac{N^{3/8}}{M^{1/2}}
\right).
\end{aligned}
\tag{135.B8}
\]

Treat (135.B5)--(135.B8) only as the supplied source statements; any
application must match their hypotheses literally.

Independently decide whether either theorem can control (135.B1) or
(135.B2) at (135.B4). At minimum audit all of the following:

1. the difference between the ordinary fraction \(k/r\) and the modular
   inverse \(\overline m/n\);
2. the direct specialization \(m=1,n=r,a=k,\vartheta=X\), including its
   loss of an averaging variable and the source's admissibility/uniformity;
3. reindexing a short interval \(k\asymp K\) by modular inversion modulo
   \(r\), including the \(r\)-dependent support and coefficient sequence;
4. completion modulo \(r\), with every Fourier mass or density cost;
5. the coupled profile \(q_L(4Xk/r^2)\), including any Mellin or Fourier
   separation cost;
6. real \(X\) versus an integral additive frequency;
7. in (135.B2), the fact that the candidate modulus \(r\) also divides the
   product variable \(s\), and the difference between a pointwise short
   interval and an average over independent moduli or fixed coprime
   residue classes;
8. retention of \(\chi_4(r)\) before every modulus or positive norm; and
9. the complete exponent after substituting \(D=X^\delta,L=X^\ell\)
   throughout the full stated polytope.

Prove (135.B4), reduce it to a strictly smaller owner-complete survivor, or
give the smallest exact source-interface no-go. A missing dictionary is not
a lower-bound obstruction. Keep all conclusions inside the flat-smooth
principal packet; no endpoint, transition, complete-UNBAL, M9, or global
exponent conclusion is licensed by this statement.
