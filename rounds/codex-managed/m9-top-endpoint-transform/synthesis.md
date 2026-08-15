# Round 8 synthesis: one-sided top-endpoint transform

Campaign: `m9-top-endpoint-transform`  
Round type: endpoint transform attack  
Graph SHA-256 before patch: `7b5a7c93190fa88305d91bb1f2e64788921fe2f4cbbd02eddb8e60e654d64d58`

## Conductor decision

Promote the exact one-sided endpoint transform after the hostile boundary
audit. Do not promote the top-block estimate: the transformed signed cone
remains unproved. The tail/symmetry task was terminated after repeated scope
interventions because it did not deliver a report; no result from it is
carried forward.

## Endpoint arithmetic and Poisson normalization

Let

\[
y=\lfloor\sqrt X\rfloor,
\quad q=X/y^2,
\quad \nu_h=hX/(4y^2),
\quad 1\le h\le H_y=\lfloor yX^{-1/4}\rfloor,
\]

with \(h\) odd. Uniformly for sufficiently large \(X\),

\[
\operatorname{dist}(\nu_h,\mathbb Z)\ge1/8.
\]

The exact minimum is

\[
\frac14-\frac{h_*(X-y^2)}{4y^2},
\]

where \(h_*\) is the largest surviving \(3\pmod4\) frequency. Thus an
exact \(1/4\) lower bound is false, but the fixed \(1/8\) separation is
valid. The closest stationary point is \(\gg y^{1/4}\) natural stationary
widths from the endpoint, so no half-Fresnel transition occurs.

For

\[
S_h=\sum_{d\le y}W(d/y)e(hX/(4d)),
\]

finite one-sided Poisson summation must give the included endpoint its
missing half weight and sum the Fourier endpoint tails in symmetric
principal value. The resulting boundary term is

\[
E_h(X)=
\frac{e(hX/(4y))}{1-e(hX/(4y^2))}.
\]

Omitting this term or using the smooth full-line formula is false even for
\(h=1,X=y^2\).

## Exact transformed cone

The accepted candidate transform is

\[
\begin{aligned}
S_h={}&E_h(X)\\
&+\frac{e(1/8)(hX)^{1/4}}2
\sum_{m=\lceil h/4\rceil}^{h}
\frac{W(\sqrt{qh/(4m)})}{m^{3/4}}
e(\sqrt{Xhm})+R_h,
\end{aligned}
\]

with \(R_h\ll_W\log(2+h)\). The cone limits are exact and independent of
\(X\) throughout the square interval. After the actual Vaaler weights are
inserted, transform errors contribute \(O_W(\log^2 H)\). The positive
whole-height boundary is sharply \(O(\log H)\), while each positive dyadic
block is \(O(1)\) and the actual two-sided real-even boundary is \(O(1)\).

On a dyadic frequency block, the remaining normalized signed sum is

\[
\mathcal T^{\rm end}_L=
\sum_{\substack{h\asymp L\\h\ {m odd}}}
\sum_{\lceil h/4\rceil\le m\le h}
\chi_4(h)a^{\rm end}(h,m)e(\sqrt{Xhm}),
\]

and the target is

\[
\mathcal T^{\rm end}_L\ll_\varepsilon L^{3/2}X^\varepsilon.
\]

The symbol is smoothly normalized in the cone interior and at its upper
support transition, but has a hard affine lower edge where \(W(1)=1\). The
smooth interior packet theorem does not automatically apply to this edge.

## Status and next kernel

The hard endpoint transform seam is closed, but the analytic top-block
estimate is not. The exact successor is the signed cone estimate above.
The smooth interior residual corridor independently retains the
outside-absolute small-gcd quarter-packet estimate from Round 7.

Round 8 used no numerical evidence and stayed within its 90/10 analytical
budget. `M9-M2`, endpoint uniformity, `M9`, and the Gauss-circle target
remain open.
