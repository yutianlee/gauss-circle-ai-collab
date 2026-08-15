## 1. Result

The arithmetic (R_1)-residue has the exact physical form
\[
 \mathfrak R^{\rm ar}[R_1]
 =\int_0^{N_X}y^{-3/4}
 \{e(\sqrt{X\max(1,y)})-e(\sqrt{XN_X})\}\,\mathcal S_X(y)\,dy,                 \tag{1}
\]
where
\[
 \mathcal S_X(y)=\sum_j\sum_{q\ge1}{\chi _4(q)\over q}
 W_j^\star\!\left({2\sqrt{Xy}\over D_jq}\right)
 \phi\!\left({y\over(H_j+1)q}\right).                                      \tag{2}
\]
Here (W_j=W) on the interior scales and (W_0=W_+) on the top scale; the star in (2) is solely the accepted symmetric half-value at the top spatial endpoint. In the normalization of the accepted (M_1) recombination,
\[
 \mathfrak R^{\rm ar}[R_1]=O_W(1),
 \qquad
 -{4\over\pi}X^{1/4}\Re\{e(1/8)\mathfrak R^{\rm ar}[R_1]\}
 =O_W(X^{1/4}).                                                               \tag{3}
\]

## 2. Exact statement and hypotheses

Take the accepted finite dyadic profile system, with its exact integer floors (D_j,H_j), (D_0=\lfloor\sqrt X\rfloor\), and no replacement of (H_j+1). Assume the accepted smooth profiles: (W) is supported in ([1/2,4/3]), (W_+) in ([1/2,1]), and
\(phi(t)=\Phi(t){\bf1}_{0<t<1}\) with (phi(1)=0). Put (N=N_X) and (e(t)=e^{2\pi it}).

Choose
\[
 \Re u=a={1\over16},\qquad \Re v=b={1\over16}.
\]
Then (delta=1/4-u/2-v) has real part (5/32>0), while
(Re(1-u-v)=7/8>0). Formulae (1)--(3) hold with the (u)-integral at the top interpreted by the already accepted symmetric-profile inversion. No deletion of a finite contour side and no infinite-height estimate is being asserted here.

## 3. Proof or derivation

Begin with the assigned identity
\[
 \sum_j{1\over(2\pi i)^2}\iint \mathcal A_j(u,v)
 R_{1,v}\!\left(1-{u+v\over2}\right)L(1-u-v,\chi _4)\,dv,du,
\]
where
\[
 \mathcal A_j=\widehat W_j(u)\widehat\phi(v)
 \left({D_j\over2\sqrt X}\right)^u(H_j+1)^v,
\quad
 R_{1,v}=-{\pi i\sqrt X\over\delta}
 \int_1^N x^{\delta-1/2}e(\sqrt{Xx})\,dx.
\]
On the chosen lines,
\[
 {1\over\delta}=\int_0^1r^{\delta-1}dr,
 \qquad
 L(1-u-v,\chi _4)=\sum_{q\ge1}{\chi _4(q)\over q^{,1-u-v}}.
\]
The latter converges locally uniformly on finite height rectangles by bounded partial sums of (chi _4). Set (y=xr). Then
\[
 r^{\delta-1}x^{\delta-1/2}dr,dx=y^{\delta-1}x^{-1/2}dy,dx,
\]
and the region is (0<y<N), (max(1,y)\le x\le N). Since
(y^{\delta-1}=y^{-3/4-u/2-v}), the (u)- and (v)-powers become respectively
\[
 \left({D_jq\over2\sqrt{Xy}}\right)^u,
 \qquad
 \left({(H_j+1)q\over y}\right)^v.
\]
Mellin inversion therefore gives exactly (2), including the top star and the unstarred, vanishing height endpoint. Finally,
\[
 \int_{\max(1,y)}^N x^{-1/2}e(\sqrt{Xx})dx
 ={e(\sqrt{XN})-e(\sqrt{X\max(1,y)})\over\pi i\sqrt X}.
\]
Multiplication by (-\pi i\sqrt X) proves (1), in particular its sign.

For the bound fix (j,y), set (P_j=\sqrt{Xy}/D_j), (R_j=y/(H_j+1)), and
\[
 f_{j,y}(q)={1\over q}W_j^\star(2P_j/q)\phi(R_j/q).
\]
Its spatial support is (3P_j/2\le q\le4P_j) on an interior scale and (2P_j\le q\le4P_j) on the top scale. On every smooth piece,
(lvert f'_{j,y}(q)\rvert\ll q^{-2}); the possible top jump contributes (O(P_j^{-1})). Hence
\[
 \|f_{j,y}\|_\infty+\operatorname{Var}(f_{j,y})\ll P_j^{-1}.
\]
Since (left|\sum_{q\le Q}\chi _4(q)\right|\le1), discrete Abel summation yields
\[
 \sum_q\chi _4(q)f_{j,y}(q)\ll {D_j\over\sqrt{Xy}}.
\]
Nonempty support forces (D_j\le4\sqrt{Xy}), and the exact active-scale set only shortens the dyadic sum. Thus
\[
 |\mathcal S_X(y)|\ll {1\over\sqrt{Xy}}
 \sum_{D_j\le\min(\sqrt X,4\sqrt{Xy})}D_j
 \ll\min(1,y^{-1/2}).                                                        \tag{4}
\]
As the phase difference in (1) is at most (2), (4) gives
\[
 |\mathfrak R^{\rm ar}[R_1]|
 \ll\int_0^1y^{-3/4}dy+\int_1^Ny^{-5/4}dy\ll1.
\]
The even (q)'s vanish through (chi _4(q)=0); no coprimality or omitted-star convention is used.

## 4. First doubtful or unproved step

There is no additional doubtful step in this isolated lemma once the accepted symmetric physical inversion for the one-sided top profile is admitted. The argument does not prove a stronger estimate uniform in an arbitrary finite top truncation, and it does not justify discarding any contour side.

## 5. Required control test and outcome

The sign/endpoints control passes: the elementary (x)-integral reverses sign against the leading minus in (R_{1,v}); the bracket in (1) vanishes at (y=N), is continuous at (y=1), and (y^{-3/4}\mathcal S_X(y)) is integrable at (0). The (x=1,N) endpoints carry full Lebesgue weight. The only half-weight is (2\sqrt{Xy}=D_0q) in the top spatial profile; (y=(H_j+1)q) contributes zero because (phi(1)=0). The unsigned control fails at the Abel step: replacing (chi _4) by (1) loses the factor (P_j^{-1}), so (4) is genuinely character cancellation rather than profile cancellation.

## 6. Dependencies and exact artifacts used

Used only: `protocol.md`; the relevant entries of `state/proof_obligations.yml`; `state/active_campaign.yml`; the Round 21, Round 22, and Round 23 synthesis files named in the brief; and `rounds/codex-managed/m9-m1-r1-arithmetic-residue/briefs/blind_r1_residue_return.md`. The proof also uses the accepted profile hypotheses and symmetric top inversion explicitly imported by those artifacts.

## 7. Recommended state effect

**Promote** the arithmetic (R_1)-residue return, with exact formula (1) and normalized bound (O_W(1)). Record its physical contribution as (O_W(X^{1/4})), with all other downstream obligations unchanged.
