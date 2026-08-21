# Round 113 statement-only packet

You must not read the proof graph, strategy files, the Round-113 derivation
packet or candidate, earlier balanced-packet derivations, or sibling
Round-113 reports.

## Frozen definitions

Let \(e(t)=e^{2\pi it}\), \(X\ge4096\), \(R=\sqrt X\), and
\(y=\lfloor R\rfloor\). Define
\[
 \rho(t)=0\ (t\le0),\quad \rho(t)=e^{-1/t}\ (t>0),
 \quad q(t)={\rho(1-t)\over\rho(t)+\rho(1-t)},
\]
\[
 \eta(t)=q(2(t-1)),\qquad W(t)=\eta(t)-\eta(2t).
\]

Set \(J_y=\lceil\log _2y\rceil\), \(D_j=2^{-j}y\), and
\[
 w_j(d)=W(d/D_j){\bf1}_{1\le d\le y}\quad(0\le j<J_y),
 \qquad
 w_{\rm bot}(d)=\eta(d/D_{J_y}){\bf1}_{1\le d\le y}.
\]
For active \(D=D_j\ge X^{1/4}\), put
\[
 H=\lfloor DX^{-1/4}\rfloor,\quad
 J_H=\lceil\log _2H\rceil,\quad L_r=2^{-r}H,
\]
\[
 v_r(h)=W(h/L_r){\bf1}_{1\le h\le H}\quad(0\le r<J_H),
 \qquad
 v_{\rm bot,H}(h)=\eta(h/L_{J_H}){\bf1}_{1\le h\le H}.
\]

Let
\[
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\quad
 \alpha_{h,H}=-{\Phi(h/(H+1))\over2\pi i h},
\]
and extend \(\chi _4\) by zero on even integers. For \(j,r\ge1\), define
\[
 {\cal B}_{j,r}^{+}
 =-{1\over\pi}\sum_{h\ge1}{\chi _4(h)v_r(h)
 \Phi(h/(H+1))\over h}
 \sum_{d\in\mathbb Z}W(d/D)e(hX/(4d)).
\]
The proposed literal two-sided physical block is
\[
 B_{2,j,r}=8\operatorname {Re}{\cal B}_{j,r}^{+}.
\]

Put \(L=L_r\), \(K=XL/D^2\), \(M=LK\), and
\[
 A_{j,r}(h,k)=v_r(h)\Phi(h/(H+1))
  (M/(hk))^{3/4}
  W\!\left(\sqrt{hX/(4kD^2)}\right).
\]
The proposed accepted transform is
\[
 {\cal B}_{j,r}^{+}
 =-{e(1/8)\over2\pi}X^{1/4}M^{-3/4}
  \sum_{h,k\ge1}\chi _4(h)A_{j,r}(h,k)e(R\sqrt{hk})
  +O(1).
\]

A balanced smooth residual label has \(j,r\ge1\),
\(D\ge X^{1/4}\), and
\[
 1\le K/L\le16.
\]
Prior analytic owners are whole-block tags; they never become arithmetic
masks inside \(A_{j,r}\).

## Proposed gcd dictionary

Set \(G_0=\sqrt L/2\),
\[
 S=\max(0,\lceil\log _2G_0\rceil),\qquad G_s=2^{-s}G_0.
\]
For \(0\le s<S\), let \(\psi_s(g)=W(g/G_s)\). Put
\[
 c_L=\eta(1/G_S),\qquad\psi_{\rm bot}(g)=c_LW(g),
\]
\[
 \psi_{\rm hi}(g)=1-\sum_{s<S}\psi_s(g)-\psi_{\rm bot}(g)
 \quad(g\in\mathbb N).
\]
For a low shell \(\sigma\), use
\[
 (G_\sigma,\vartheta_\sigma)
 =(G_s,W)\quad\hbox{or}\quad(1,c_LW),
\]
and, for coprime \(u,v\),
\[
 F_{\sigma,u,v}(t)
 =\vartheta_\sigma(t)
 A_{j,r}(G_\sigma tu,G_\sigma tv).
\]

With \(\widehat F(\xi)=\int F(t)e(-t\xi)\,dt\), define
\[
\begin{aligned}
 Q_\sigma(R)=
 \sum_{\substack{(u,v)=1\\u\ {\rm odd}}}\chi _4(u)\sum_n\Big[
 &\widehat F_{\sigma,u,v}
  (G_\sigma(n-R\sqrt{uv}-1/4))\\
 -&\widehat F_{\sigma,u,v}
  (G_\sigma(n-R\sqrt{uv}-3/4))
 \Big].
\end{aligned}
\]
The proposed exact low-gcd identity is
\[
 {\cal T}^{\rm low}_{j,r}
 ={1\over2i}\sum_\sigma G_\sigma Q_\sigma(R).
\]
Inside the low part, assign exact squares first and then nonsquares with
\(\operatorname {dist}(\sqrt{hk},\mathbb Z)\le R^{-1}\). If their literal
signed subtotals are \({\cal S}^{\rm sq}\) and
\({\cal S}^{\rm near}\), the proposed residual identity is
\[
 {\cal T}^{\rm res}_{j,r}
 ={1\over2i}\sum_\sigma G_\sigma Q_\sigma(R)
 -{\cal S}^{\rm sq}-{\cal S}^{\rm near}.
\]

## Assigned question

Independently prove or refute:

1. both finite telescoping partitions, including \(H=1,2\);
2. the factor \(8\), the \(e(1/8)/(2\pi)\) transform constant, and
   positive/negative recombination;
3. the exact balanced boundary \(K/L=4^jX/y^2\);
4. the integer gcd partition, including its bottom atom and high support;
5. the \(1/4\)-minus-\(3/4\) packet and the one-count correction;
6. uniform real compact support and scale-normalized seminorms;
7. whether any datum remains undefined before the signed estimate.

The desired packet estimate is not part of this task. A rigorous
counterexample or repaired dictionary is a successful result.
