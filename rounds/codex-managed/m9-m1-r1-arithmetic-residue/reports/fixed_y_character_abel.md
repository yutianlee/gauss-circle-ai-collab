# Fixed-\(y\) character-Abel proof

## 1. Result

The proposed return has the correct sign and every displayed power.  In
the accepted physical symmetric-profile limit the recombined \(R_1\)
arithmetic residue is \(O_W(1)\) on the normalized M1 scale. Therefore its
physical contribution, after restoring the external \(X^{1/4}\), is
\(O_W(X^{1/4})\).

For fixed scale \(D_j\) and radial variable \(y>0\), put
\(Q=\sqrt{Xy}/D_j\). The exact sampled amplitude satisfies
\[
 \left\|q^{-1}V_j(2Q/q)
 \phi\!\left(\frac{y}{(H_j+1)q}\right)\right\|_\infty
 {}+\operatorname{Var}_{q\in\mathbb N}(\cdots)
 \ll_W Q^{-1}. \tag{1}
\]
Period-four cancellation is essential; the unsigned analogue retains the
Round-22 \(X^{1/8}\)-type normalized capacity.

## 2. Exact statement and hypotheses

Let \(Y=\lfloor\sqrt X\rfloor\), \(D_j=2^{-j}Y\),
\(H_j=\lfloor D_jX^{-1/4}\rfloor\), and
\(N=N_X=\lfloor16\sqrt X\rfloor\). Choose positive Mellin abscissae
\(a,b\) with
\[
 a+b<1,\qquad \delta_0=\frac14-\frac a2-b>0. \tag{2}
\]
Write \(E(x)=e(\sqrt{Xx})\), \(C=\pi i\sqrt X\). The residue to be
estimated is
\[
 \mathfrak R_{R_1}=\sum_j\frac1{(2\pi i)^2}\iint
 \mathcal A_j(u,v)\left\{-\frac C\delta
 \int_1^N x^{\delta-1/2}E(x)\,dx\right\}
 L(1-u-v,\chi_4)\,dv\,du, \tag{3}
\]
where \(\delta=1/4-u/2-v\). Here \(V_j=W\) for \(j\ge1\), while
\(V_0(t)=W(t)\mathbf1_{t\le1}^{*}\); \(\phi\) is the exact bounded-BV
height profile with its zero value at equality.

## 3. Derivation, sampled BV, and full sum

By (2),
\[
 \frac1\delta=\int_0^1r^{\delta-1}\,dr,\qquad
 L(1-u-v,\chi_4)=\sum_{q\ge1}\frac{\chi_4(q)}q q^{u+v}. \tag{4}
\]
The latter converges by bounded partial sums of \(\chi_4\). Rigorously,
truncate it and the outside lines first; (4) is locally uniform on every
finite box. After Mellin inversion set \(y=xr\). Since
\[
 x^{\delta-1/2}r^{\delta-1}dr
 =x^{-1/2}y^{-3/4}\,dy,
\]
the \(u,v\) inversions give respectively
\[
 V_j\!\left(\frac{2\sqrt{Xy}}{D_jq}\right),\qquad
 \phi\!\left(\frac{y}{(H_j+1)q}\right).
\]
Moreover \(E'(x)=Cx^{-1/2}E(x)\). Thus the initial factor \(-C\)
and the integral over \(\max(1,y)\le x\le N\) give
\[
 -C\int_{\max(1,y)}^Nx^{-1/2}E(x)\,dx
 =E(\max(1,y))-E(N).
\]
Consequently
\[
 \boxed{\begin{aligned}
 \mathfrak R_{R_1}={}&
 \sum_j\sum_{q\ge1}\frac{\chi_4(q)}q
 \int_0^Ny^{-3/4}\{E(\max(1,y))-E(N)\}\\
 &\qquad\times
 V_j\!\left(\frac{2\sqrt{Xy}}{D_jq}\right)
 \phi\!\left(\frac{y}{(H_j+1)q}\right)\,dy .
 \end{aligned}} \tag{5}
\]
For a truncated \(L\)-series this is ordinary finite algebra. After the
physical top symmetric inversion, fixed \(y\) has finite \(q\)-support,
so the truncation may be removed. No absolute integration of the hard
top Mellin kernel is used.

To prove (1), the support of \(V_j(2Q/q)\) lies in
\[
 \frac32Q\le q\le4Q, \tag{6}
\]
and for the top scale the lower edge improves to \(2Q\), with half weight
at equality. On (6), the zero-extended sequence \(q^{-1}\) has
supremum plus variation \(O(Q^{-1})\). Composition with the monotone map
\(q\mapsto2Q/q\) cannot increase the fixed BV norm of \(W\); the top
one-jump projector adds one jump. Likewise
\(q\mapsto y/((H_j+1)q)\) is monotone, so the exact floor-dependent
height factor has uniformly bounded sampled variation. The product
variation inequality proves (1), including every equality convention.

Since \(\sup_T|\sum_{q\le T}\chi_4(q)|\le1\), discrete Abel summation and
(1) give
\[
 \sum_q\frac{\chi_4(q)}qV_j(2Q/q)
 \phi\!\left(\frac{y}{(H_j+1)q}\right)
 \ll_W \frac{D_j}{\sqrt{Xy}}. \tag{7}
\]
There is an indispensable automatic lower threshold. A nonzero term has
\(q<4Q\) (at \(q=4Q\), \(W(1/2)=0\)); since \(q\ge1\),
\[
 y>\frac{D_j^2}{16X}. \tag{8}
\]
Using \(|E(\max(1,y))-E(N)|\le2\), (7)--(8) yield
\[
 |\mathfrak R_{R_1}|
 \ll\sum_j\frac{D_j}{\sqrt X}
 \int_{D_j^2/(16X)}^Ny^{-5/4}\,dy
 \ll X^{-1/4}\sum_jD_j^{1/2}\ll1. \tag{9}
\]
The last sum is the exact active geometric sequence
\(\sum_{j=0}^JD_j^{1/2}\le
Y^{1/2}\sum_{j\ge0}2^{-j/2}\ll X^{1/4}\).
No \(H_j\) was replaced by an asymptotic.
Restoring the accepted physical normalization gives explicitly
\[
 -\frac4\pi X^{1/4}\Re\{e(1/8)\mathfrak R_{R_1}\}
 =O_W(X^{1/4}). \tag{10}
\]

## 4. First doubtful or unproved step

There is no doubtful step for the accepted physical residue. The result
does not assert a sampled-BV bound for an arbitrary finite top Mellin
truncation, whose inverse has noncompact Perron tails. The remaining
unproved objects are the two diagonal post-functional-equation transition
traces, not this arithmetic residue.

## 5. Required control test and outcome

The sign control passes because \(-C\int x^{-1/2}E(x)dx\) is lower
endpoint minus upper endpoint. The powers \(q^{-1}\) and \(y^{-3/4}\)
follow exactly from (4) and \(y=xr\). At \(y=1\) the two phase branches
agree; at \(y=N\) the bracket vanishes. Top equality has its half star,
while the integration-by-parts endpoint coefficients remain full.

If \(\chi_4\) is replaced by \(|\chi_4|\), (7) becomes only \(O(1)\);
integrating gives normalized capacity \(O(N^{1/4}\log X)\), not (9).
Thus the proof does not establish an unsigned or adversarial analogue.
No numerical test was used.

## 6. Dependencies and exact artifacts used

Used only the protocol, proof graph, active campaign, Round-21, Round-22,
and Round-23 syntheses, and the assigned Round-24 brief. No other
Round-24 report, external theorem, web source, or numerical artifact was
used.

## 7. Recommended state effect

Promote the exact return (5), fixed-\(y\) BV lemma (1), automatic threshold
(8), and normalized bound (9). Mark the physical
\(M9\text{-}M1\text{-}R1\) arithmetic residue target-sized and remove it
as a blocker from the endpoint-boundary package. Retain arbitrary finite
top truncations, both diagonal transition traces, the post-FE vector
estimate, GAR, M9-M1, M9-M2, M9, and the target as open.
