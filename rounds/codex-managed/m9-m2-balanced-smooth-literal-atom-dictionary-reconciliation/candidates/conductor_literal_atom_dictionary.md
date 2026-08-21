# Conductor candidate: literal balanced smooth atom dictionary

Campaign: m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation

Starting graph SHA-256:
9d560539df2db7d69e72dd6e7e6af7247f00237ee795ac13b053b3f34eae8efa

This is candidate evidence. Its purpose is to eliminate abstract phrases
such as “the actual profile”; it asserts no signed packet estimate.

## 1. Two explicit finite partitions

Put
\[
 \rho(t)=\begin{cases}0,&t\le0,\\ e^{-1/t},&t>0,\end{cases}
 \qquad
 q(t)={\rho(1-t)\over \rho(t)+\rho(1-t)},
\]
\[
 \eta(t)=q(2(t-1)),\qquad W(t)=\eta(t)-\eta(2t).
\tag{113.C1}
\]
Then \(\eta=1\) on \((-\infty,1]\), \(\eta=0\) on
\([3/2,\infty)\), and \(W\in C_c^\infty((0,\infty))\), with
\(\operatorname {supp}W\subset[1/2,3/2]\).

For \(R=\sqrt X\), \(y=\lfloor R\rfloor\),
\[
 J_y=\lceil\log _2y\rceil,\qquad D_j=2^{-j}y,
\]
define
\[
 w_j(d)=W(d/D_j){\bf1}_{1\le d\le y}\quad(0\le j<J_y),
\qquad
 w_{\rm bot}(d)=\eta(d/D_{J_y}){\bf1}_{1\le d\le y}.
\tag{113.C2}
\]
For every \(1\le d\le y\),
\[
 \sum_{j=0}^{J_y-1}w_j(d)+w_{\rm bot}(d)=1.
\tag{113.C3}
\]
Only \(j=0\) is clipped. For every \(j\ge1\),
\(w_j(d)=W(d/D_j)\) on all integers.

For an active \(D=D_j\ge X^{1/4}\), put
\[
 H=H_D=\lfloor DX^{-1/4}\rfloor,\qquad
 J_H=\lceil\log _2H\rceil,\qquad L_r=2^{-r}H.
\tag{113.C4}
\]
For \(0\le r<J_H\), set
\[
 v_r(h)=W(h/L_r){\bf1}_{1\le h\le H},
\qquad
 v_{\rm bot,H}(h)=\eta(h/L_{J_H}){\bf1}_{1\le h\le H}.
\tag{113.C5}
\]
Then, for every \(1\le h\le H\),
\[
 \sum_{r=0}^{J_H-1}v_r(h)+v_{\rm bot,H}(h)=1.
\tag{113.C6}
\]
Only \(r=0\) is clipped. For \(r\ge1\), \(v_r(h)=W(h/L_r)\)
on all integers. If \(H=1\), the sum over \(r\) is empty and the bottom
piece is the whole frequency partition.

## 2. Literal physical and normalized blocks

For \(0<u<1\), define the audited Vaaler taper
\[
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\tag{113.C7}
\]
with its continuous endpoint values. For \(h>0\),
\[
 \alpha_{h,H}=-{\Phi(h/(H+1))\over2\pi i h},\qquad
 C_h=e(h/4)-e(3h/4)=2i\chi _4(h),
\tag{113.C8}
\]
where \(\chi _4(h)=0\) for even \(h\). Hence
\[
 \alpha_{h,H}C_h=-{\Phi(h/(H+1))\chi _4(h)\over\pi h}.
\tag{113.C9}
\]

For one smooth denominator block \(j\ge1\) and one full smooth frequency
block \(r\ge1\), define
\[
 {\cal B}_{j,r}^{+}(X)
 =-{1\over\pi}\sum_{h\ge1}{\chi _4(h)v_r(h)
 \Phi(h/(H+1))\over h}
 \sum_{d\in\mathbb Z}W(d/D)e(hX/(4d)).
\tag{113.C10}
\]
The support omits \(d=0\). The literal two-sided physical M2 block,
including the outer factor four in the H1--H3 reduction, is
\[
 B_{2,j,r}(X)=8\operatorname {Re}{\cal B}_{j,r}^{+}(X).
\tag{113.C11}
\]

Put
\[
 L=L_r,\qquad K={XL\over D^2},\qquad M=LK
\tag{113.C12}
\]
and define, for positive integers \(h,k\),
\[
 A_{j,r}(h,k)
 =v_r(h)\Phi(h/(H+1))
  \left({M\over hk}\right)^{3/4}
  W\!\left(\sqrt{hX\over4kD^2}\right).
\tag{113.C13}
\]
Then the accepted smooth Poisson/stationary formula is
\[
 {\cal B}_{j,r}^{+}(X)
 =-{e(1/8)\over2\pi}X^{1/4}M^{-3/4}{\cal T}_{j,r}(X)
  +E_{j,r}(X),
\tag{113.C14}
\]
\[
 {\cal T}_{j,r}(X)
 =\sum_{h,k\ge1}\chi _4(h)A_{j,r}(h,k)e(R\sqrt{hk}),
\qquad |E_{j,r}(X)|\ll1.
\tag{113.C15}
\]
The \(k\)-sum is finite because the last \(W\)-factor is compactly
supported. Smooth entry and exit are part of that factor; there is no
separate hard crossing atom.

## 3. Literal residual block labels

Let \({\cal R}_{\rm bal}(X)\) consist of pairs \((j,r)\) satisfying:

1. \(j\ge1\), \(D_j\ge X^{1/4}\), \(H_{D_j}\ge1\);
2. \(r\ge1\) and \(r<J_{H_{D_j}}\), so neither clipped terminal
   frequency nor the unit bottom is present;
3. \(1\le K/L\le16\), with equality assigned to the balanced side;
4. the accepted terminal, full second-derivative, and TTY tests have
   declined the block.

One literal conservative choice for item 4 is to retain the block whenever
all three recorded envelopes exceed \(X^{1/4}\):
\[
 1+D/L>X^{1/4},
\tag{113.C16}
\]
\[
 1+(LX/D)^{1/2}+D^{3/2}(LX)^{-1/2}>X^{1/4},
\tag{113.C17}
\]
\[
 X^{89/1282}L^{89/1282}D^{819/1282}>X^{1/4}.
\tag{113.C18}
\]
Moving an equality or a fixed-constant collar to the residual side only
enlarges the open target and is harmless under \(X^\varepsilon\).

Because \(D_j=2^{-j}y\),
\[
 {K\over L}=4^j{X\over y^2}.
\tag{113.C19}
\]
Thus the exact ratio test is finite and transparent: \(j=1\) is balanced
for all sufficiently large \(X\); \(j=2\) lies on the balanced boundary
only when \(X=y^2\); \(j\ge3\) is unbalanced. The hard \(j=0\) profile
never enters.

For each \((j,r)\in{\cal R}_{\rm bal}(X)\), take the internal subdivision
set \(\Omega_{j,r}\) to be the singleton. Any later bounded smooth
subdivision must be a prescribed partition of unity inside this same
block and may not combine distinct \(j\) or \(r\).

## 4. An explicit smooth gcd partition

For the fixed block, set \(G_0=\sqrt L/2\) and
\[
 S=\max(0,\lceil\log _2G_0\rceil),\qquad G_s=2^{-s}G_0.
\tag{113.C20}
\]
For \(0\le s<S\), put
\[
 \psi_s(g)=W(g/G_s).
\]
The last integer atom is
\[
 c_L=\eta(1/G_S),\qquad \psi_{\rm bot}(g)=c_LW(g).
\tag{113.C21}
\]
Finally define
\[
 \psi_{\rm hi}(g)=1-\sum_{s=0}^{S-1}\psi_s(g)-\psi_{\rm bot}(g)
\quad(g\in\mathbb N).
\tag{113.C22}
\]
Telescoping gives, on every positive integer \(g\),
\[
 1=\psi_{\rm hi}(g)+\sum_{s=0}^{S-1}\psi_s(g)+\psi_{\rm bot}(g).
\tag{113.C23}
\]
Moreover \(\psi_{\rm hi}(g)=0\) for \(g\le\sqrt L/2\), and it is
supported on \(g\ge\sqrt L/2\). Thus its absolute contribution is
\(O(L^{3/2})\). Every low atom is the restriction of a fixed real compact
smooth profile at scale \(G_s\), with the last scale equal to one.

For a low atom \(\sigma\), write \(G_\sigma=G_s\) and
\(\vartheta_\sigma=W\), or \(G_\sigma=1\) and
\(\vartheta_\sigma=c_LW\) for the bottom. With
\(h=gu,k=gv,(u,v)=1\), define
\[
 F_{\sigma,u,v}(t)
 =\vartheta_\sigma(t)
 A_{j,r}(G_\sigma tu,G_\sigma tv).
\tag{113.C24}
\]
This is a literal real \(C_c^\infty\) function. At \(t=g/G_\sigma\)
it is exactly the low-gcd summand.

## 5. Quarter packets and one-count correction

With
\[
 \widehat F(\xi)=\int_{\mathbb R}F(t)e(-t\xi)\,dt,
\]
define
\[
\begin{aligned}
 Q_\sigma^{\rm full}(R)
 =\sum_{\substack{(u,v)=1\\u\ {\rm odd}}}\chi _4(u)
 \sum_{n\in\mathbb Z}\Big[
 &\widehat F_{\sigma,u,v}
  (G_\sigma(n-R\sqrt{uv}-1/4))\\
 -&\widehat F_{\sigma,u,v}
  (G_\sigma(n-R\sqrt{uv}-3/4))
 \Big].
\end{aligned}
\tag{113.C25}
\]
Poisson gives the exact low-gcd identity
\[
 {\cal T}_{j,r}^{\rm low}
 ={1\over2i}\sum_\sigma G_\sigma Q_\sigma^{\rm full}(R).
\tag{113.C26}
\]

Give priority first to the high-gcd part, then inside the low part to
\[
 hk\ \hbox{a square},
\qquad
 hk\notin\square,\quad
 \operatorname {dist}(\sqrt{hk},\mathbb Z)\le R^{-1}.
\tag{113.C27}
\]
Let \({\cal S}_{j,r}^{\rm sq}\) and
\({\cal S}_{j,r}^{\rm near}\) denote those two literal restrictions of
\({\cal T}_{j,r}^{\rm low}\). Then
\[
 {\cal T}_{j,r}^{\rm res}
 ={1\over2i}\sum_\sigma G_\sigma Q_\sigma^{\rm full}(R)
 -{\cal S}_{j,r}^{\rm sq}-{\cal S}_{j,r}^{\rm near}.
\tag{113.C28}
\]
This is the one-count residual equation. No square or near-square
indicator is inserted into \(F_{\sigma,u,v}\).

The high-gcd term, the two corrections in (113.C28), and the transform
error in (113.C14) are target-safe. Therefore the first analytic gap after
this dictionary is
\[
 \left|\sum_\sigma G_\sigma Q_\sigma^{\rm full}(R)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon
\tag{113.C29}
\]
for each fixed \((j,r)\in{\cal R}_{\rm bal}(X)\).

## 6. Uniformity obligations

The proposed certificate must prove, uniformly over
\((j,r)\in{\cal R}_{\rm bal}(X)\):

- \(A_{j,r}\) is real and has fixed compact support after the
  \(h/L,k/K\) rescaling;
- every logarithmic \(h,k\) derivative is \(O_{a,b}(1)\);
- every \(F_{\sigma,u,v}\) has scale-normalized seminorms uniform in
  \(X,D,L,H\), the floors, and the shell label;
- the truncated profiles \(j=0\) and \(r=0\) are absent;
- both frequency signs recombine exactly as (113.C11);
- all sums are finite or absolutely convergent before rearrangement.

The identity changes no capacity. The current envelope still loses
\[
 \min(L^{1/2},R^{1/2}/L),
\]
with worst deficit \(X^{1/12}\).

## 7. Required adjudication

The round must certify or correct (113.C1)--(113.C28) coefficientwise.
In particular it must not silently accept the finite-\(X\) residual tests,
the bottom gcd atom, the physical factor in (113.C11), or the uniform
seminorm claim. If one of these is false, the report must give the first
exact repair. If they pass, the state effect is only a literal dictionary
connector; (113.C29) and every downstream theorem remain open.
