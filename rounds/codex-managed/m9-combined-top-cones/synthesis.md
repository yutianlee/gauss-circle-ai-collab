# Round 9 synthesis: the top cones reinforce rather than cancel

Campaign: `m9-combined-top-cones`  
Round type: combined-kernel discovery  
Graph SHA-256 before patch: `d155bdcc1ef62728419694f98c40a1cd4fe9664d6cc7e74528b282f8dc69fa2b`

## Conductor decision

Promote the exact top-block M1 transform and the exact piecewise formula for
the combined M1/M2 stationary contribution. Reject the proposed algebraic
cancellation mechanism: three isolated derivations agree that the leading
constants have the same sign, while the actual Vaaler factors lie on
different variables and M1 has an unmatched outer wing. No top-cone estimate
is promoted.

## Exact M1 endpoint transform

Let

\[
y=\lfloor\sqrt X\rfloor,\qquad q=X/y^2,\qquad
1\le h\le H=\lfloor yX^{-1/4}\rfloor,
\]

and put

\[
B_h=\sum_{d\le y}\chi_4(d)W(d/y)e(hX/d).
\]

Using

\[
\chi_4(d)=\frac{e(d/4)-e(3d/4)}{2i}
\]

and one-sided Poisson summation with the included endpoint gives

\[
\begin{aligned}
B_h={}&E_h^\chi(X)\\
&+\frac{e(1/8)(hX)^{1/4}}{i}
\sum_{\substack{4h<n<16h\\n\ \mathrm{odd}}}
\frac{\chi_4(n)W(\sqrt{4qh/n})}{n^{3/4}}
e(\sqrt{Xhn})+O_W(\log(2+h)),
\end{aligned}
\]

where

\[
E_h^\chi(X)=\frac1{2i}
\left\{
\frac{e(hX/y+y/4)}{1-e(hq-1/4)}-
\frac{e(hX/y+3y/4)}{1-e(hq-3/4)}
\right\}.
\]

Both denominators are uniformly separated from zero. The positive-frequency
boundary is \(O(1)\) on a dyadic frequency block and \(O(\log H)\) over the
whole height; the actual two-sided real-even boundary is \(O(1)\). The
Vaaler-weighted transform error is \(O_W(\log^2 H)\).

After multiplication by the exact M1 factor \(-4\alpha_{h,H}\), the positive
stationary contribution is

\[
-\frac{2e(1/8)}{\pi}X^{1/4}
\sum_{h\le H}\frac{\Phi(h/(H+1))}{h^{3/4}}
\sum_{\substack{4h<n<16h\\n\ \mathrm{odd}}}
\frac{\chi_4(n)W(\sqrt{4qh/n})}{n^{3/4}}
e(\sqrt{Xhn}).
\]

Thus the top M1 estimate reduces to a signed product-phase cone estimate at
the \(L^{3/2}X^\varepsilon\) normalized scale; that estimate is open.

## Exact combined cone

In common coordinates \((r,m)=(n,h)\), M1 occupies

\[
r\ \mathrm{odd},\qquad
\lceil r/16\rceil\le m\le\min(H,\lfloor r/4\rfloor),
\]

while M2 occupies

\[
r\ \mathrm{odd},\qquad r\le H,qquad
\lceil r/4\rceil\le m\le r.
\]

For odd \(r\le H\), these integer intervals are adjacent with neither gap
nor overlap. Restoring the actual H3 prefactors, both stationary pieces have
the same leading constant

\[
-\frac{2e(1/8)}{\pi}X^{1/4}.
\]

The combined positive stationary kernel is therefore

\[
\sum_{\substack{r\ \mathrm{odd}\\m\ge1}}
\frac{\chi_4(r)}{(rm)^{3/4}}\mathcal A_H(r,m;q)
e(\sqrt{Xrm}),
\]

with the exact piecewise symbol

\[
\begin{aligned}
\mathcal A_H(r,m;q)={}&
\mathbf1_{m\le H,\,4m<r<16m}
\Phi(m/(H+1))W(\sqrt{4qm/r})\\
&+\mathbf1_{r\le H,\,\lceil r/4\rceil\le m\le r}
\Phi(r/(H+1))W(\sqrt{qr/(4m)}).
\end{aligned}
\]

The full two-sided contribution is twice its real part, together with the
explicit M1 and M2 boundary terms and target-sized transform errors.

## Why complementarity does not close the block

The cones concatenate, but four exact obstructions prevent the proposed
folding or cancellation.

1. Their stationary constants reinforce rather than cancel.
2. M1 uses \(\Phi(m/(H+1))\), whereas M2 uses \(\Phi(r/(H+1))\). Near
   \(r\asymp H\) the first can be order one while the second is order
   \(H^{-2}\).
3. The continuum reflection \((r,m)\mapsto(4m,r/4)\) is not a lattice
   involution when \(r\) is odd.
4. M1 has an unmatched outer wing \(H<r<16H\). For \(X=H^4\), the term
   \((r,m)=(4H+1,H)\) is nonzero and has no M2 term with the same phase.

Consequently neither an exact actual-weight cancellation nor a symmetric
divisor pairing exists. A bound for the combined kernel would also not, by
itself, prove the separately stated M1 and M2 obligations.

## Status and next kernel

Round 9 closes an exact transform seam and a false architectural branch. It
does not prove M1, M2, endpoint uniformity, M9, or the Gauss-circle target.
The useful next move is to bound M1 directly before transformation wherever
the bounded partial sums of \(\chi_4(d)\) are effective, and then map the
remaining \((D,L)\) corridor. This avoids treating the combined cone as an
artificially easier object.

No numerical experiment or external theorem was used. The round therefore
stayed entirely within its analytical allocation.
