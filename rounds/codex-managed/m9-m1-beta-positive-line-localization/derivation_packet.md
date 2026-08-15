# Round 45 frozen derivation packet

This packet states the exact mathematical inputs and target. It contains no
claimant proof. A statement-only rederivation may use only this packet and
its generated task brief. System-supplied repository operating instructions
are not mathematical evidence and do not count as contamination; reading
any excluded mathematical state or claimant artifact does.

## 1. Lines, coordinates, and selectors

Let

\[
b=\frac1{\log(2X)},\qquad 0<a\le b,qquad
c'=\frac54,
\]

for sufficiently large \(X\), and put

\[
r=\frac54-\frac{a+b}{2}>1,\qquad
p=\frac54+\frac{a+b}{2}>1.
\]

Use

\[
u=a+i\mu,\qquad v=b+i\nu,\qquad
s=\frac54+it,
\]

\[
\beta=t-\frac{\mu+\nu}{2},\qquad
\alpha=t+\frac{\mu+\nu}{2}.
\]

Let \(\psi\in C_c^\infty(\mathbb R)\) be the fixed beta mask and let
\(\chi_0\in C_c^\infty(\mathbb R)\), \(0\le\chi_0\le1\), be one on a
fixed neighborhood of zero. The active scales are

\[
D_j=2^{-j}\lfloor\sqrt X\rfloor,\qquad
H_j=\lfloor D_jX^{-1/4}\rfloor\ge1.
\]

The exact spatial decomposition has only

\[
\widehat W_0(u)=\frac1u+\widehat W_{0,r}(u),
\qquad \widehat W_j(u)\quad(j\ge1).                \tag{45.1}
\]

The \(u^{-1}\) share uses the signed top functional; the \(j=0\)
regular and \(j\ge1\) interior shares retain ordinary \(\mu\)-integration.
The normalized smooth profiles and finitely many derivatives are rapidly
decreasing. The actual height transform satisfies, with polynomial
\(b^{-1}\) loss,

\[
|\partial_\nu^k\widehat\phi(b+i\nu)|
\ll_{b,k}(1+|\nu|)^{-3-k}\quad(k\le2).             \tag{45.2}
\]

Every floor, equality convention, star, \(\chi_4(q)\), and profile stays
attached to its original scale.

## 2. Recombine before localizing

At fixed finite \(U,V,S\), the complete sixteen-cell product
Cauchy--Green representation of the endpoint-free beta vector is an exact
finite Stokes identity

\[
\sum_{k=1}^{16}\mathcal C_k[\psi Q_{\rm ef}]
=R_uR_v[\psi(\beta)Q_{\rm ef}],                    \tag{45.3}
\]

including the positive mixed cell

\[
\mathcal C_{16}=\frac14A_uA_v[\psi''(\beta)Q_{\rm ef}].
\]

No individual \(\mathcal C_k\) has a physical limit. The right side of
(45.3) is the original positive-line representative. Only there use

\[
1=\chi_0(\alpha)+(1-\chi_0(\alpha)).               \tag{45.4}
\]

This gives exact finite central and complementary terminal functionals.
If either share is transferred again, its full cutoff-derivative connector
ledger must be restored.

After aggregate endpoint/arithmetic subtraction and radial-side removal,
the endpoint-free beta vector is

\[
\mathfrak V_{\rm ef}=\mathfrak T[R_1]+\mathfrak P_\rho[R_1], \tag{45.5}
\]

with the artificial coefficient oriented as below. Axial/corner/collision
restrictions retain the accepted single combined coefficient and are not
inserted into the terminal a second time.

## 3. Exact positive-line compact terminal

In beta-slab coordinates put \(L=\mu+\nu\), so
\(\alpha=L+\beta\), and define

\[
A(L)=-1-\frac b2-i(L+\beta),\qquad
D(L,\nu)=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right). \tag{45.6}
\]

For one scale and coefficient set

\[
\gamma_j(x)=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x},
\qquad
p_{j,x}(\nu)=e^{i\gamma_j(x)\nu}\widehat\phi(b+i\nu). \tag{45.7}
\]

Let \(\mathcal G(\alpha,\beta)\) be the exact bounded double-gamma quotient
on compact \((\alpha,\beta)\), including its unit phase, and put

\[
g_{j,h,q,x}(L,\beta)=
\psi(\beta)\chi_0(L+\beta)\mathcal G(L+\beta,\beta)
e^{iL\log(D_j/(2q\sqrt{Xx}))-i\beta\log(hqx)}.    \tag{45.8}
\]

The hard singular functional is

\[
\mathsf P_j=
\frac{g_{j,h,q,x}(L,\beta)p_{j,x}(L)}{A(L)}
-\frac{i g_{j,h,q,x}(L,\beta)}{2\pi}
\int_{\mathbb R}
\frac{p_{j,x}(\nu)-p_{j,x}(L)}{(L-\nu)D(L,\nu)}\,d\nu. \tag{45.9}
\]

For a smooth normalized spatial profile \(\mathscr W\), put

\[
\mathsf S_j[\mathscr W]=
\frac{g_{j,h,q,x}(L,\beta)}{2\pi}
\int_{\mathbb R}
\frac{p_{j,x}(\nu)\mathscr W(L-\nu)}{D(L,\nu)}\,d\nu. \tag{45.10}
\]

The exact compact terminal amplitude before the radial factor is

\[
\begin{aligned}
\mathcal A_{\rm db}(x)={}&-\pi i
\sum_{j,h,q}\chi_4(q)h^{-r}q^{-p}
\left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b\\
&\times\int_{\mathbb R^2}\frac{dL\,d\beta}{(2\pi)^2}
\bigl\{
\mathbf1_{j=0}\mathsf P_j
+\mathbf1_{j=0}\mathsf S_j[\widehat W_{0,r}]\\
&\hspace{45mm}+\mathbf1_{j\ge1}\mathsf S_j[\widehat W_j]
\bigr\}.
\end{aligned}                                               \tag{45.11}
\]

The sum retains its actual finite product/equality restrictions; dropping
them is allowed only for an upper bound. The target compact estimate is

\[
\boxed{
\sup_{1\le x\le N_X}
\{|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\}
\ll\log^C(2X).}                                           \tag{45.12}
\]

The exact combined phase gives

\[
x\partial_x\Theta=-\left(\frac{L+\nu}{2}+\beta\right),
\qquad
\left|\frac{(L+\nu)/2+\beta}{D(L,\nu)}\right|\le1.       \tag{45.13}
\]

One radial integration by parts then gives a normalized
\(O(\log^C X)\) contribution with full continuous endpoint coefficients.
The external physical factor is restored once afterward.

## 4. Oriented artificial coefficient

At the artificial pole

\[
\rho=\frac14-s-\frac v2=0,
\]

one has

\[
s=\frac14-\frac v2,\qquad
\alpha_\rho=\frac\mu2,qquad
\beta_\rho=-\frac\mu2-\nu.                         \tag{45.14}
\]

The radial factor is

\[
R_{1,v}(1-s)=-\frac{\pi i\sqrt X}{\rho}I_1(\rho),
\qquad
I_1(\rho)=\int_1^{N_X}x^{\rho-1/2}e(\sqrt{Xx})\,dx. \tag{45.15}
\]

Because \(d\rho/ds=-1\), the oriented \(s\)-residue is

\[
\operatorname{Res}_sR_{1,v}(1-s)=\pi i\sqrt X I_1(0). \tag{45.16}
\]

The remaining arithmetic product must stay recombined:

\[
F_{u+v}\!\left(\frac34+\frac v2\right)
=\zeta\!\left(\frac34+\frac u2+v\right)
L\!\left(\frac34-\frac u2,\chi_4\right).           \tag{45.17}
\]

It is not replaced by a termwise \(h,q\) series on this residue.
Accordingly, for \(c\in\{\chi_0,1-\chi_0\}\), the artificial share is
the \((u,v)\) Mellin functional with multiplier

\[
c(\mu/2)\psi(-\mu/2-\nu)
\sum_j\widehat W_j(a+i\mu)\widehat\phi(b+i\nu)
\left(\frac{D_j}{2\sqrt X}\right)^{a+i\mu}
(H_j+1)^{b+i\nu},                                  \tag{45.18}
\]

times (45.16)--(45.17), the accepted residue sign, and normalized
\(d\mu\,d\nu/(2\pi)^2\). Use the top split (45.1): its singular share
is evaluated by Plemelj as \(a\downarrow0\); smooth shares are ordinary.

The target is

\[
|\mathfrak P_\rho[\chi_0]|+
|\mathfrak P_\rho[1-\chi_0]|\ll\log^C(2X).         \tag{45.19}
\]

The following elementary period-four estimate may be proved by Abel
summation from bounded partial sums of \(\chi_4\): uniformly on a fixed
compact real interval containing \(3/4-a/2\),

\[
L(\sigma+i\tau,\chi_4)\ll 1+|\tau|.                \tag{45.20}
\]

## 5. Large-alpha interface

The accepted large-alpha analytic theorem applies to the same direct
positive-line endpoint-free terminal after global module and
artificial/axial ownership, on a finite one-count signed partition
\(\{\eta_\tau\}\) satisfying

\[
\sum_\tau\eta_\tau(\alpha)=1-\chi_0(\alpha).       \tag{45.21}
\]

Its cells include both saddle signs, entry and exit collars, and their
nonstationary completion, with the same \(\psi(\beta)\), three selectors,
floors, stars, character, contour constants, radial integration, and
external factor. The theorem gives

\[
\sum_\tau\mathfrak T[\psi\eta_\tau Q_{\rm ef}]
=O_\varepsilon(X^{1/4+\varepsilon}).               \tag{45.22}
\]

The required seam check is that the left side is exactly the terminal
complement obtained from (45.3)--(45.4), with no transferred connector,
axis, artificial coefficient, or external factor inserted again.

## 6. Promotion target and controls

Prove or refute all of the following as one theorem:

1. (45.3)--(45.4) is the lawful one-count localization order.
2. (45.11) is exactly its central terminal and obeys (45.12).
3. The artificial coefficient obeys (45.19), with correct orientation,
   Plemelj treatment, arithmetic chamber, selectors, and scale sum.
4. Equations (45.21)--(45.22) identify the direct positive-line terminal
   complement exactly.
5. After the full endpoint-free beta vector is assembled, the external
   operator
   \(-4X^{1/4}\Re\{e(1/8)(\cdot)\}/\pi\) is applied once.

No numerical experiment or external theorem is authorized or needed.
