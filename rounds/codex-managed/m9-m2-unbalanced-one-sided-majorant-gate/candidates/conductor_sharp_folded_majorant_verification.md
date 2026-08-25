# Conductor verification: the sharp folded Fejer majorant

Campaign: `m9-m2-unbalanced-one-sided-majorant-gate`

## 1. Extremal statement

Let

$$
F_H(\alpha)=|D_H(\alpha)|^2,
\qquad D_H(\alpha)=\sum_{a=0}^{H-1}e(a\alpha).
$$

Fix \(1\le q\le H\), write \(H=mq+r\), \(0\le r<q\), and let
\(\mathcal T_q\) be the real trigonometric polynomials of degree at most
\(q-1\) satisfying \(T\ge F_H\) pointwise. Then

$$
\boxed{
\inf_{T\in\mathcal T_q}\widehat T(0)
=\mu(H,q):=(q-r)m^2+r(m+1)^2
=\frac{H^2}{q}+r\left(1-\frac rq\right).}
\tag{134.V1}
$$

The infimum is attained by

$$
\boxed{T^*_{H,q}(\alpha)=|mD_q(\alpha)+D_r(\alpha)|^2,}
\tag{134.V2}
$$

with \(D_0=0\).

## 2. Sharp lower bound by exact quadrature

For \(T(\alpha)=\sum_{|s|<q}t_se(s\alpha)\), root-of-unity
orthogonality gives

$$
t_0=\frac1q\sum_{j=0}^{q-1}T(j/q).
\tag{134.V3}
$$

The residues of \(0,\ldots,H-1\) modulo \(q\) occur with multiplicities

$$
n_a=\begin{cases}m+1,&0\le a<r,\\m,&r\le a<q.\end{cases}
$$

Hence discrete Parseval gives

$$
\frac1q\sum_{j=0}^{q-1}F_H(j/q)
=\sum_{a=0}^{q-1}n_a^2=\mu(H,q).
\tag{134.V4}
$$

Pointwise domination and (134.V3)--(134.V4) prove
\(t_0\ge\mu(H,q)\).

## 3. Independent verification of the extremizer

Put \(z=e(\alpha)\), \(w=z^q\), \(v=z^r\),

$$
A=1-w,\qquad B=1-v,\qquad
G=\sum_{a=0}^{m-1}w^a.
$$

For \(z\ne1\),

$$
(1-z)(mD_q+D_r)=mA+B,
$$

$$
(1-z)D_H=1-w^mv=AG+w^mB.
$$

Let

$$
S_m(\bar w)=\sum_{j=1}^m\sum_{a=0}^{j-1}\bar w^a
=\sum_{a=0}^{m-1}(m-a)\bar w^a.
$$

Since

$$
m-G\bar w^m=(1-\bar w)S_m(\bar w)=\bar A S_m(\bar w)
$$

and

$$
m^2-|G|^2+2\Re S_m(\bar w)=m(m+1),
$$

direct expansion yields

$$
\begin{aligned}
|mA+B|^2-|AG+w^mB|^2
=|A|^2\left(m(m+1)-2\Re\{\bar vS_m(\bar w)\}\right).
\end{aligned}
\tag{134.V5}
$$

The sum of the nonnegative multiplicities in \(S_m\) is
\(m(m+1)/2\). Therefore

$$
2\Re\{\bar vS_m(\bar w)\}
\le 2|S_m(\bar w)|_{\rm triangle}\le m(m+1),
$$

so (134.V5) is nonnegative. At \(z=1\), both polynomials have value
\(H\), and continuity completes the proof of (134.V2). Its constant
coefficient is \(\sum_an_a^2=\mu(H,q)\), so the lower bound is attained.

## 4. Exact physical inequality and excess

For every finitely supported complex \(A\), Parseval gives

$$
\sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
\le
\sum_n\left|\sum_{a=0}^{q-1}n_aA(n+a)\right|^2.
\tag{134.V6}
$$

This is endpoint-complete under zero extension. It has only \(q\) shift
locations, total weight \(H\), and squared weight mass \(\mu(H,q)\).
Because \(T-F_H\ge0\), its exact minimal \(L^1\) excess is

$$
\mu(H,q)-H=qm(m-1)+2mr.
\tag{134.V7}
$$

The endpoints are consistent: \(q=1\) gives the constant majorant
\(H^2\), while \(q=H\) gives \(T^*=F_H\).

## 5. Capacity consequence

Relative to the accepted diagonal normalization

$$
\mathcal D_0=C_HH\sum_{p,k}|b_{p,k}|^2,
$$

the folded zeroth coefficient carries factor

$$
\rho(H,q)=\frac{\mu(H,q)}H\ge\frac Hq.
\tag{134.V8}
$$

If a lag-count argument chooses

$$
q\le \frac{H}{\Gamma_{\rm before}},
\qquad \Gamma_{\rm before}=\min(H,Q),
$$

then

$$
\Gamma_{\rm claimed}=1,
\qquad
\Gamma_{\rm zeroth\ survivor}=\rho(H,q)
\ge\Gamma_{\rm before}.
\tag{134.V9}
$$

More generally, \(q\le HX^{-\eta}\) forces
\(\rho(H,q)\ge X^\eta\). Thus the exact contraction is not target-safe
by bandwidth and zeroth-mass bookkeeping alone.

This is not a lower bound for the literal majorized form: its signed
nonzero shifts and cross-\(p\) terms could cancel the enlarged zeroth
piece. Proving that cancellation is precisely a new actual-family
\(\chi_4\)-sensitive correlation theorem.

## 6. Order and character seams

Universal quadratic-form domination is equivalent to pointwise
multiplier domination. The converse follows by testing with translated
normalized Dirichlet kernels, whose squared moduli approximate a point
mass. Coefficientwise domination of an internal window does not suffice:
for \(u=(1,1)\), \(v=(1,2)\), and \(c=(2,-1)\), one has
\(|u\cdot c|=1\) and \(|v\cdot c|=0\).

The lawful comparison must be applied after forming

$$
A(k)=\sum_{p\ {m odd}}\chi_4(p)b_{p,k}.
$$

Rowwise positivity is a different and stronger object: two identical
rows in opposite \(\chi_4\)-classes cancel in \(A\) but not in the
separate row energy. The folded majorant preserves the character because
it acts on the combined \(A\); it does not itself exploit that character.

## 7. Conductor disposition before seam reviews

Equations (134.V1)--(134.V7) are a genuine new exact finite lemma and
should be considered for promotion after the independent post-unmask
reviews. Equations (134.V8)--(134.V9) prove a scoped no-go for extracting
a fixed-power endpoint gain from one-sided bandwidth contraction plus
positive-diagonal or lag-count bookkeeping alone.

The literal target \(\mathcal E_\chi\ll X^{1/2+\varepsilon}\) remains
open. No complete UNBAL, M9-M2, M9, bridge, quarter, or exponent change
follows.
