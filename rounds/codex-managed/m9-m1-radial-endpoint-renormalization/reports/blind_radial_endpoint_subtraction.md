# Blind radial endpoint subtraction

## 1. Result

For every integer \(M\ge1\), the exact radial transform
\[
G_v(w)=\int_1^{N_X}x^{w-7/4-v/2}e(\sqrt{Xx})\,dx
\]
splits as
\[
\boxed{G_v(w)=B_{M,v}(w)+G^{\rm ren}_{M,v}(w)}
\tag{1}
\]
into \(M\) explicit signed endpoint terms and a remainder gaining \(M\)
powers of the true radial height
\(\rho=w-\tfrac34-\tfrac v2\). Substitution into the finite Round-19
rectangle gives an exact endpoint boundary operator and radial sides with
arbitrary algebraic decay. It gives no cancellation with arithmetic or
axial residues by itself.

## 2. Exact statement and hypotheses

Put \(N=N_X=\lfloor16\sqrt X\rfloor\),
\[
E_X(x)=e(\sqrt{Xx}),\qquad \mathscr D=x\frac d{dx},\qquad
E_r(x)=\mathscr D^rE_X(x),\qquad \rho=w-\frac34-\frac v2.
\]
Then
\[
\boxed{
B_{M,v}(w)=\sum_{r=0}^{M-1}\frac{(-1)^r}{\rho^{r+1}}
\{N^\rho E_r(N)-E_r(1)\},}
\tag{2}
\]
\[
\boxed{
G^{\rm ren}_{M,v}(w)=
\frac{(-1)^M}{\rho^M}\int_1^N x^{\rho-1}E_M(x)\,dx .}
\tag{3}
\]
Equations (1)–(3) extend through \(\rho=0\) by cancellation; poles of the
two separated terms there are artificial and are not new Mellin residues.

More explicitly, with \(\theta_x=2\pi i\sqrt{Xx}\),
\[
E_r(x)=E_X(x)P_r(\theta_x),\quad P_0=1,\quad
P_{r+1}(T)=\frac T2\{P_r(T)+P'_r(T)\}.
\tag{4}
\]
Thus every endpoint coefficient is finite and explicit.

## 3. Derivation and exact subtraction identity

Set \(y=\log x\), \(L=\log N\). Then
\[
G_v(w)=\int_0^Le^{\rho y}E_X(e^y)\,dy.
\]
Repeated integration by parts, always differentiating \(E_X(e^y)\),
gives (2)–(3). The upper endpoint has sign \(+\), the lower endpoint
sign \(-\), and the successive orders alternate by \((-1)^r\).

In the terminal Round-19 kernel put
\[
\rho_*(s,v)=\frac14-s-\frac v2
\]
and replace \(G_v(1-s)\) exactly by
\[
B_{M,v}(1-s)+G^{\rm ren}_{M,v}(1-s).
\tag{5}
\]
Both terms retain without modification the complete multiplier
\[
\mathbf1_{hq=m}\chi_4(q)\sum_j
\widehat W_j(u)\widehat\phi(v)
\left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v
\left(\frac hq\right)^{(u+v)/2}
K_{u+v}(1-s)m^{-s}.
\tag{6}
\]
Hence all actual floors and profiles remain present, including
\(\widehat W_0(u)=1/u+\widehat W_{+,r}(u)\).

Let \(\mathfrak T(B_M)\) and \(\mathfrak T(G_M^{\rm ren})\) denote the
upward terminal \(s\)-integrals with (6). On the original radial
horizontal sides retain the Round-19 orientations
\[
\lambda+iS\to c+iS,\qquad c-iS\to\lambda-iS,
\]
and write the corresponding integrals as
\[
\mathfrak S(Y)=\sum_j\frac1{(2\pi i)^3}\iint\mathcal A_j(u,v)
\left\{\int_{\lambda+iS}^{c+iS}+\int_{c-iS}^{\lambda-iS}\right\}
Y_v(w)F_{u+v}(w)\,dw\,dv\,du .
\]
The exact finite
identity is therefore
\[
\boxed{\mathfrak I^c
=\mathfrak R^{\rm ar}[G]
+\mathfrak T(G_M^{\rm ren})
+\mathfrak S(G_M^{\rm ren})
+\underbrace{\mathfrak T(B_M)+\mathfrak S(B_M)}
_{\mathfrak E_M\ {\rm(endpoint\ boundary\ operator)}}.}
\tag{7}
\]
This grouping subtracts endpoints only *after* the accepted finite
rectangle identity, so the arithmetic residue remains exactly
\[
\mathfrak R^{\rm ar}[G]
=\sum_j\iint\mathcal A_j(u,v)
G_v(1-(u+v)/2)L(1-u-v,\chi_4)\,dv\,du.
\tag{8}
\]
Height \(v=0\), hard-Perron \(u=0\), joint-corner, and any auxiliary
radial-Perron residues remain separate exactly as in Round 19. If one
instead shifts \(B_M\) alone, its artificial \(\rho=0\) poles must be
paired with those of (3); counting them separately is invalid.

The star on \(\mathbf1_{[1,N]}^*\) fixes symmetric inverse Mellin values
\(1/2\) at \(x=1,N\). It does not halve the full endpoint coefficients
in (2), which arise from the fundamental theorem of calculus. Any
auxiliary Perron boundary residue still carries its own \(1/2\) and stays
outside \(\mathfrak E_M\).

## 4. Renormalized side decay and first unproved step

Since
\[
|E_M(x)|\le C_M(1+\sqrt{Xx})^M,
\]
on either radial side \(w=\sigma\pm iS\), \(\lambda\le\sigma\le c\),
\(|\Im v|\le V\), and \(S>V/2+1\),
\[
|G^{\rm ren}_{M,v}(w)|
\ll_M
\frac{(1+\sqrt{XN})^M\log(2N)\,
\max(1,N^{\sigma-3/4-\Re v/2})}
(S-V/2)^M}.
\tag{9}
\]
Thus against the Round-20 left-edge capacity \(S^{1-2\lambda}\), the
renormalized radial factor has capacity
\(S^{1-2\lambda-M}\) for fixed outside boxes and endpoint data. Choosing
\(M>1-2\lambda\) removes the previous \(S^{-1}\) *absolute-capacity*
obstruction. The first unproved step is uniform nested exhaustion when
\(X,U,V\) also grow, plus a target-sized estimate for the explicit
boundary operator \(\mathfrak E_M\) and the diagonal transition traces.
No side is deleted here.

## 5. Required controls and outcomes

For \(M=1\), (1) reads
\[
G_v(w)=\frac{N^\rho E_X(N)-E_X(1)}{\rho}
-\frac1\rho\int_1^Nx^{\rho-1}\mathscr D E_X(x)\,dx,
\]
verifying signs and orientations directly. Recombining (2) and (3)
removes every apparent pole at \(\rho=0\). The full profile (6), endpoint
stars, and existing residue ledger are unchanged. All controls pass
algebraically; no numerics were used.

## 6. Dependencies and exact artifacts used

Only the authorized protocol, proof graph, active campaign, Round-19 blind
finite-vector identity, Round-20 synthesis and blind transition report, and
Round-21 brief were used.

## 7. Recommended state effect

Promote (1)–(9) as exact finite endpoint-renormalization infrastructure and
record that arbitrary subtraction defeats the prior fixed-order side-decay
capacity obstruction. Retain endpoint-boundary cancellation, nested-limit
uniformity, diagonal vector-Hilbert control, GAR, and M9-M1 as open.
