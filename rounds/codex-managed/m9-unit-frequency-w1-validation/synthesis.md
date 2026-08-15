# Round 2 synthesis: unit-frequency W-1 validation

## Closing decision

**ACCEPT WITH EXPLICIT HYPOTHESES.**  The unit-frequency W-1 mechanism is correct for the sharp block and for an actual absolute weighted block satisfying a uniform discrete \(\ell^1\)-nondegeneracy condition.  The conclusion remains conditional on the matching exact-\(N=0\) mass closure.  It has no signed consequence.

The three independent seams agree:

- the statement-only rederivation proves the Cauchy window lower bound and the \(X^{1/3}\) crossover;
- the hostile review finds no counting or denominator-clearing flaw, but requires explicit coefficient, support, exact-subtraction, and dyadic-weight hypotheses;
- the primary-source audit verifies Vaaler's coefficient normalization and gives the uniform bound \(|\beta_{1,H}|\ge1/(2\pi)\) for every integer \(H\ge1\).

The conductor's independent weighted proof improves the sufficient weight hypothesis from a pointwise plateau to the sampled scalar condition

\[
\sum_{d\asymp D}|w_D(d)|\ge\lambda D.
\]

Under the already assumed uniform boundedness of \(w_D\), this is quantitatively equivalent to the existence of a positive-density lower-level set, up to changing fixed constants.

## Validated conditional lemma

Let the denominator support be contained in a fixed shell \([aD,bD]\), let \(H_D\ge1\), and suppose

\[
\sum_d|w_D(d)|\ge\lambda D,
\qquad
|\beta_{1,H_D}|\ge b_0>0.
\]

For the project's cleared integer

\[
N=h_1d_2d_3d_4-h_2d_1d_3d_4+h_3d_1d_2d_4-h_4d_1d_2d_3,
\]

assume the same absolute weighted quantity satisfies

\[
\Sigma_{\rm abs}(N=0)\le C_\epsilon D^2X^\epsilon.
\]

Then for every \(M>0\),

\[
\boxed{
\Sigma_{\rm abs}(0<|N|\le M)
\ge c(a,b,\lambda,b_0)\min(D^4,MD)
-C_\epsilon D^2X^\epsilon.}
\]

The sharp-block statement is the special case \(w_D\equiv1\).  The proof restricts to \(h_1=h_2=h_3=h_4=1\), bins the weighted pair sums \(1/d_1+1/d_3\) into intervals of length \(\asymp M/D^4\), applies weighted Cauchy--Schwarz, clears denominators, and finally subtracts the entire exact-resonance mass.

## Vaaler source decision

The source audit is complete against Jeffrey D. Vaaler's 1985 paper, [DOI 10.1090/S0273-0979-1985-15349-2](https://doi.org/10.1090/S0273-0979-1985-15349-2).  The completed source card is `sources/vaaler_1985.md`, with the audited local PDF at `sources/papers/vaaler_1985.pdf`.

Theorem 6, equation (2.28), supplies

\[
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\]

and its monotonicity on \([0,1]\).  Theorem 18, equation (7.14), supplies the normalized Fejer residual.  Vaaler uses the midpoint value \(\psi(n)=0\); the project's floor-compatible value \(-1/2\) at integers is a valid endpoint corollary because the Fourier polynomial is zero and the residual bound equals \(1/2\) there.  The M2 factor gives

\[
\beta_{h,H}
=-\frac{\Phi(|h|/(H+1))\chi_4(|h|)}{\pi|h|}\mathbf1_{2\nmid h},
\qquad
|\beta_{1,H}|\ge\frac1{2\pi}.
\]

## Endpoint and quantifier decision

For \(M=D^4/X\) and \(X^{1/4}\le D\le X^{1/2}\), the linear branch gives

\[
\Sigma_{\rm abs}(0<|N|\le D^4/X)
\ge cD^5/X-C_\epsilon D^2X^\epsilon.
\]

For every fixed \(\delta>0\), choosing \(0<\epsilon<3\delta\) yields a power contradiction to \(\Sigma_{\rm abs}\ll_\epsilon D^2X^\epsilon\) uniformly when \(D\ge X^{1/3+\delta}\).  At \(D=X^{1/3}\) there is only equality of polynomial scales, so the round records a crossover, not a contradiction at the exact boundary.  The previous \(X^{3/8}\) threshold was a nonoptimal bulk-frequency specialization.

## Scope boundary

Accepted scope:

- sharp weight-blind tuple count, after the corresponding exact subtraction;
- absolute beta-weighted mass under sampled \(\ell^1\)-nondegeneracy;
- a genuinely nonnegative character-removed unsigned mass.

Excluded scope:

- the full true signed mass;
- the signed fat-band constant;
- pointwise M2, M9-M2, M9, or the Gauss-circle target.

A positive \(h=1\) subtotal can be cancelled by complementary frequencies in the true signed sum.  This round therefore strengthens the reason to preserve the \(\chi_4(h)\) signs: character-blind absolute methods already fail by a power above \(D=X^{1/3}\).

## Remaining seam

The proof draft currently says only “bounded smooth dyadic partition.”  That wording does not guarantee \(\sum_d|w_D(d)|\gg D\), especially for truncated endpoint blocks.  A fixed nonzero profile \(w_D(d)=W(d/D)\) supplies the condition away from degenerate truncations, but the actual partition and the rounding rule ensuring \(H_D\ge1\) must be written down.  This is recorded as a new normalization obligation rather than hidden inside the obstruction lemma.

## Evidence ledger

- Blind proof: `reports/blind_w1_rederivation.md`
- Primary-source and weight audit: `reports/h4_weight_normalization_review.md`
- Hostile seam review: `reports/adversarial_endpoint_review.md`
- Conductor proof: `reviews/conductor_weight_transfer_analysis.md`

No numerical experiment was used in Round 2.

## Next-round strategy

Round 3 should leave the absolute route and attack the earliest genuinely open signed interface.  The primary target is a precise signed pair/lift energy statement for the M2 fat band, with \(\chi_4(h)\) retained.  It should compare two routes without conflating them:

1. reduced-fraction signed lift weights \(A_\chi(p/q)\) and the proposed signed fat-band constant;
2. a sign-preserving Poisson/stationary-phase transform only if all boundary, zero-mode, and support-edge terms are stated.

The round should first determine whether the existing B1 pointwise lift envelope can possibly imply the needed signed energy.  A capacity obstruction or counterexample is a successful outcome.
