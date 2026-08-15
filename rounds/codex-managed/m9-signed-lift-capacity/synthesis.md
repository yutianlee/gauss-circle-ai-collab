# Round 3 synthesis: signed-lift capacity

## Closing decision

**SPLIT ACCEPTANCE.** The reduced-fraction lift estimate B1 is proved after replacing the vague phrase “bounded smooth weight” by an explicit uniform twisted-discrepancy or bounded-variation hypothesis. The proposed implication from B1 to signed fat-band cancellation is rejected.

No numerical experiment was used.

## Validated B1 lemma

Let

\[
A_\chi(p/q)=
\sum_{\substack{gq\in[D,2D)\\1\le |gp|\le H}}
\beta_{gp,H}w_D(gq),
\qquad
\beta_{h,H}=-\frac{\Phi(|h|/(H+1))\chi_4(|h|)}{\pi|h|}
\mathbf 1_{2\nmid h}.
\]

If (p) is even, then (A_\chi(p/q)=0). If (p) is odd and the sampled odd-lift sequence has uniformly bounded twisted discrepancy

\[
\sup_{I}\left|\sum_{g\in I\atop g\ {m odd}}
\chi_4(g)w_D(gq)\right|\le C_w,
\]

then Abel summation and the monotonicity of (\Phi(u)/g) give

\[
\boxed{
|A_\chi(p/q)|
\le \frac{C_w}{\pi|p|}\min\!\left(1,\frac qD\right)
\le \frac{C_wq}{\pi D|p|}.}
\]

A fixed profile (w_D(d)=W(d/D)) with

\[
\|W\|_\infty+\operatorname{Var}_{[1,2]}W=O(1)
\]

is sufficient, as are sharp dyadic cutoffs and uniformly discrete-BV weights. Boundedness alone, and smoothness without a scale-normalized variation bound, are insufficient: one may choose (w_D(gq)=\chi_4(g)) on an active lift progression and destroy the character cancellation.

## Exact global normalization

Collect the actual lift coefficients in

\[
S_D(t)=\sum_x A_\chi(x)e(tx/4),
\qquad
R_\chi(r)=\sum_{x+y=r}A_\chi(x)A_\chi(y).
\]

For a fixed real nonnegative (V\in C_c^\infty((1/2,3))), put

\[
K(\xi)=\int_{\mathbb R}V(u)e(\xi u)\,du.
\]

Then the frozen smoothed fourth moment is exactly

\[
\frac1X\int_{\mathbb R}V(t/X)|S_D(t)|^4\,dt
=\sum_{r,s}R_\chi(r)\overline{R_\chi(s)}
K\!\left(\frac{X(r-s)}4\right).
\]

The normalized off-diagonal constant is therefore

\[
c_\chi^V(D;X)=D^{-2}\operatorname{Re}
\sum_{r\ne s}R_\chi(r)\overline{R_\chi(s)}
K\!\left(\frac{X(r-s)}4\right).
\]

This is a global frozen-coefficient object, not a pointwise M2 estimate.

## Sharp B1-only capacity

The exact support and B1 imply

\[
\|A_\chi\|_1\ll D\log(2H),
\qquad
\|A_\chi\|_2^2\ll D.
\]

Using the rational pair-representation identity

\[
(\mu q_1-Qp_1)(\mu q_3-Qp_3)=Q^2p_1p_3
\]

and the elementary divisor bound gives the sharper character-blind diagonal estimate

\[
\boxed{\sum_r|R_\chi(r)|^2\ll_\varepsilon D^2X^\varepsilon.}
\]

Distinct pair sums have spacing at least (1/(16D^4)). Hence B1 plus rational spacing yields only

\[
\frac1X\int V(t/X)|S_D(t)|^4\,dt,
\quad D^2|c_\chi^V(D;X)|
\ll_{\varepsilon,V}
D^2X^\varepsilon\left(1+\frac{D^4}{X}\right).
\]

The factor (1+D^4/X) is an unresolved off-diagonal capacity, not a diagonal-counting defect.

## No-go result

An even, odd-numerator, exact-support envelope model supported on (x=\pm1/q), (q\asymp D), satisfies B1 but has critical signed fat-band size

\[
c_{*,\le\kappa}^V(D;X)
\ge c\frac{D^3}{X}-O_\varepsilon(X^\varepsilon).
\]

Thus for every fixed (\delta>0), B1 alone cannot imply (c_\chi\ll_\varepsilon X^\varepsilon) uniformly when (D\ge X^{1/3+\delta}). This is a theorem about the information content of B1; it is not a counterexample to the actual Vaaler/(\chi_4) coefficient system.

The missing theorem must use correlations absent from the envelope, for example

\[
\left|
\sum_{0<|r-s|\le\kappa/X}
R_\chi(r)\overline{R_\chi(s)}
K\!\left(\frac{X(r-s)}4\right)
\right|
\ll_{\varepsilon,V,\kappa}D^2X^\varepsilon,
\]

or the corresponding full graded off-diagonal bound. The generic band (q\asymp D) has only one lift, so B1 gives no gain there; cancellation must occur across numerator or denominator classes in the actual coefficient system.

## Literature decision

The two M2 shifts map exactly to the Li--Yang phase with

\[
\mathsf H=L,\qquad \mathsf M=D,\qquad \mathsf T=X/4,
\qquad F_\rho(u)=u^{-1}+\rho D/X,\quad \rho\in\{1,3\}.
\]

The derivative nondegeneracy conditions pass. However, Li--Yang Case A misses the largest block (L\asymp DX^{-1/4}) by the fixed power (X^{2/41}), and its displayed Case B height conditions never include that block anywhere in the active range. The method remains structurally relevant for smaller frequency blocks, but no literature theorem is imported as a proof dependency.

## Scope boundary and next target

Accepted:

- B1 under explicit uniform twisted-discrepancy/BV hypotheses;
- the exact global fourth-moment normalization;
- the B1-only pair-energy bound and capacity obstruction.

Rejected:

- B1 for arbitrary bounded or unnormalized smooth weights;
- B1 alone implying signed fat-band cancellation;
- a global fourth moment alone implying the pointwise M2 endpoint bound.

Round 4 should isolate the actual generic single-lift band (q\asymp D), derive its numerator-residue structure before taking absolute values, and determine whether the two-shift reciprocal phase permits a genuine signed autocorrelation estimate. The smaller-height Li--Yang-covered portion and the top-height gap must be recorded separately.

## Evidence ledger

- Blind proof: `reports/blind_b1_rederivation.md`
- Capacity/no-go theorem: `reports/signed_energy_capacity.md`
- Hostile audit: `reports/adversarial_b1_review.md`
- Conductor derivation: `reviews/conductor_independent_analysis.md`
- Primary-literature audit: `reviews/conductor_literature_method_audit.md`

