# Round 24 synthesis: the recombined R1 residue returns to a character-Abel integral

Campaign: `m9-m1-r1-arithmetic-residue`  
Round type: arithmetic-residue physical return  
Graph SHA-256 before patch: `4778c43f94bec97ea6887fb62456f16ee6fe0981d395d2d7685cb1fc026f22ef`

## Conductor decision

Promote the exact physical return of the recombined \(R_1\) arithmetic
residue, the fixed-\(y\) sampled-BV lemma, and the normalized \(O_W(1)\)
bound. Three independent derivations agree on the admissible Mellin lines,
conditional character series, \(x,r\mapsto x,y\) Jacobian, lower-minus-upper
phase, character placement, support, sampled variation, small-\(y\) seam,
scale sum, top star, floors, and external \(X^{1/4}\) normalization.

Promotion begins only after the accepted symmetric physical-profile limits.
It does not extend automatically to an arbitrary finite top Mellin height.
The two diagonal transition traces, GAR, M9-M1, M9-M2, M9, and the final
target remain open. No numerical experiment or external theorem was used;
the round was 100 percent analytical/algebraic.

## Exact residue and admissible lines

Choose \(u=a+i\mu\), \(v=b+i\nu\) with

\[
 a>0,\qquad b>0,\qquad \frac a2+b<\frac14.
\]

Then \(\Re\delta>0\) for

\[
 \delta=\frac14-\frac u2-v,
\]

and \(a+b<1\), so the nonprincipal character series for
\(L(1-u-v,\chi_4)\) converges locally uniformly on finite-height boxes by
Dirichlet's test. The recombined residue is

\[
 \mathfrak R^{\rm ar}[R_1]
 =\sum_j\frac1{(2\pi i)^2}\iint
 \mathcal A_j(u,v)
 \left\{-\frac{\pi i\sqrt X}{\delta}
 \int_1^N x^{\delta-1/2}e(\sqrt{Xx})\,dx\right\}
 L(1-u-v,\chi_4)\,dv\,du,
 \tag{24.1}
\]

where \(N=N_X\) and

\[
 \mathcal A_j(u,v)=\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v.
\]

## Physical return

First truncate the character series and both contours. Insert

\[
 \frac1\delta=\int_0^1r^{\delta-1}\,dr
\]

and set \(y=xr\). The domain becomes
\(0<y<N\), \(\max(1,y)\le x\le N\), while

\[
 x^{\delta-1/2}r^{\delta-1}\,dr
 =x^{-1/2}y^{\delta-1}\,dy.
\]

The \(u\)- and \(v\)-inversions produce, respectively,

\[
 V_j^*\!\left(\frac{2\sqrt{Xy}}{D_jq}\right),
 \qquad
 \phi\!\left(\frac{y}{(H_j+1)q}\right).
\]

Since

\[
 \frac d{dx}e(\sqrt{Xx})
 =\pi i\sqrt X\,x^{-1/2}e(\sqrt{Xx}),
\]

the exact phase is lower minus upper. After the licensed physical profile
limits and removal of the character truncation,

\[
 \boxed{\begin{aligned}
 \mathfrak R^{\rm ar}[R_1]
 ={}&\sum_j\sum_{q\ge1}\frac{\chi_4(q)}q
 \int_0^N y^{-3/4}
 \{e(\sqrt{X\max(1,y)})-e(\sqrt{XN})\}\\
 &\qquad\times
 V_j^*\!\left(\frac{2\sqrt{Xy}}{D_jq}\right)
 \phi\!\left(\frac{y}{(H_j+1)q}\right)\,dy.
 \end{aligned}}
 \tag{24.2}
\]

Here \(V_j=W\) for interior scales and \(V_0\) is the actual one-sided
top profile with its symmetric half-star. The height profile vanishes at
its equality endpoint and has no half-star.

## Fixed-y character cancellation

Fix \((j,y)\) and put

\[
 Q_j(y)=\frac{\sqrt{Xy}}{D_j},\qquad
 a_{j,y}(q)=\frac1qV_j^*(2Q_j(y)/q)
 \phi\!\left(\frac{y}{(H_j+1)q}\right).
\]

The interior spatial support is

\[
 \frac32Q_j(y)\le q\le4Q_j(y),
\]

and the top hard cutoff changes the lower edge to \(2Q_0(y)\). On this
fixed-ratio interval, \(q^{-1}=Q_j(y)^{-1}s^{-1}\); both profile factors
are fixed BV functions composed with monotone maps. The hard top adds only
one jump and the equality half-value adds only one sample. Hence

\[
 \boxed{
 \|a_{j,y}\|_\infty+
 \sum_{q\ge1}|a_{j,y}(q+1)-a_{j,y}(q)|
 \ll_W Q_j(y)^{-1}.}
 \tag{24.3}
\]

Using \(\sup_T|\sum_{q\le T}\chi_4(q)|\le1\), Abel summation gives

\[
 \boxed{
 \sum_q\chi_4(q)a_{j,y}(q)
 \ll_W\frac{D_j}{\sqrt{Xy}}.}
 \tag{24.4}
\]

Nonempty support forces \(D_j\le4\sqrt{Xy}\). Thus geometric scale
summation yields

\[
 \left|\sum_j\sum_q\chi_4(q)a_{j,y}(q)\right|
 \ll_W\min(1,y^{-1/2}).
 \tag{24.5}
\]

Since the phase bracket in (24.2) has modulus at most two,

\[
 |\mathfrak R^{\rm ar}[R_1]|
 \ll_W\int_0^1y^{-3/4}\,dy+
 \int_1^Ny^{-5/4}\,dy
 \ll_W1.
 \tag{24.6}
\]

Equivalently, summing scale by scale uses the threshold
\(y>D_j^2/(16X)\) and gives
\(X^{-1/4}\sum_jD_j^{1/2}\ll1\).
Restoring the active-M1 normalization,

\[
 -\frac4\pi X^{1/4}\operatorname{Re}
 \{e(1/8)\mathfrak R^{\rm ar}[R_1]\}
 =O_W(X^{1/4}).
 \tag{24.7}
\]

## Scope and controls

At \(y=1\), the phase is continuous; at \(y=N\), it vanishes; as
\(y\downarrow0\), (24.5) makes the integral convergent. Smooth spatial
edges have zero profile value. A hard-top equality has exactly the accepted
half-star, while a height equality is zero. Exact floors and the smallest
height \(H_j=1\) are harmless.

If \(\chi_4\) is replaced by unsigned coefficients, a \(q\asymp Q\) block
has \(Q\) terms of size \(Q^{-1}\), so the inverse-support-length gain in
(24.4) disappears and one recovers the obstructive normalized
\(N^{1/4}\)-type capacity. At finite top Mellin height, the inverse top
profile has noncompact logarithmic tails and no compact-support sampled-BV
bound; (24.3) cannot be inserted before the physical limit.

## State effect

- promote the exact physical return (24.2);
- promote the sampled-BV and fixed-\(y\) character-Abel estimates
  (24.3)--(24.5);
- promote the normalized \(O_W(1)\), physical \(O_W(X^{1/4})\) residue
  bound;
- reject automatic finite-top-Mellin and unsigned extensions;
- record the endpoint/residue package as target-safe;
- retain the two diagonal transition traces and the full post-FE vector
  operator, GAR, M9-M1, M9-M2, M9, and the target as open.
- isolate one-factor functional-equation reduction of those two traces as
  the next candidate obligation.
