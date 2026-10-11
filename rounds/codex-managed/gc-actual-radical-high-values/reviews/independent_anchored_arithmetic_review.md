# Independent anchored-arithmetic seam review

Campaign: gc-actual-radical-high-values. Round: 216.
Reviewer: actual_radical_tail, new bounded NONBLIND review assignment.
Generated: 2026-09-28. Effort: 100 percent analysis/source checking;
zero numerical experiments.
Starting graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
Claimant: reports/anchored_divisor_high_values.md.
Final claimant SHA256 independently checked:
7fb1a536ef78d6e2af007bf179fa8c3ce74cda69c96948a81043b3a4cf9213d8.

## 1. Result and verdict

**GREEN** for the exact divisor decomposition, anchored real energy,
conditional implication from claimant (12), restored high-value powers,
source specialization, and the limited failure of the stated absolute
closure. No correction to the frozen claimant is required.

This verdict does not prove claimant (12), H216, a better complete
moment, or a pointwise exponent. The report correctly labels (12) as
an unproved sufficient input, its modulus calculation as an insufficient
upper bound, and \(102/325\) as only a conditional fixed-order milestone.
The original actual-radical report remains frozen and was not edited.

## 2. Exact reviewed statement and hypotheses

The claimant uses the full frozen real series and mollifier, real
\(T\ge2\), radius interval \([T/2,2T]\), \(V_0=T^{13/125}\), and
upper index cutoff \(Z=T^{3/2}\). Its dyadic scales satisfy
\(N,D\in\{1,2,4,\ldots\}\), \(D\le N\), and \(K=N/D\ge1\).
Ordinary divisors \(d\), rather than squarefree classes, range over
\([D,2D)\). No squarefree restriction is imposed on this independent
route.

For a rectangle, let \(J\) denote a maximal \(N^{-1/2}\)-separated
set of actual real high values at level \(v\), with aligned real signs
\(\sigma_j\). Let \(\mathfrak Q,\mathfrak D,\mathfrak O\) be exactly
claimant (8)--(10), including every plus-kernel sine term in
\(\mathfrak O=\mathfrak Q-\mathfrak D\).

The conditional hypothesis is the one-sided bound

\[
 \mathfrak O\le
 \frac{J^2v^2N^{3/2}}{64K}+C_\eta T^{\rho+\eta}JN
 \quad(v\ge V_0/(2L)),                                    \tag{R1}
\]

where \(L\ll(1+\log T)^2\) is the full rectangle count.
The checked implication is

\[
 {\rm (R1)}\Longrightarrow
 H_{12}(T)\ll_\epsilon
 T^{113/125+42\rho/13+\epsilon}.
                                                               \tag{R2}
\]

At \(\rho=208/2625\), its exponent equals \(29/25\).
Only actual aligned configurations are assumed; neither arbitrary
rephasings nor all independently selected coefficient vectors are part
of (R1). All conclusions are uniform over the prescribed real endpoints
and partial top block.

## 3. Independent derivation of the reviewed seams

### A. Exact rectangles, endpoints and symbol variation

Every \(n\le Z\) belongs to precisely one half-open dyadic block
\([N,2N)\), including an exact dyadic boundary in its new block.
Every divisor \(d\mid n\) belongs to one interval \([D,2D)\) with
\(D\le N\), since \(d\le n<2N\).
For \(k=n/d\),

\[
 K/2<k<2K,\qquad K=N/D.
\]

Thus the claimant's ambient \([K/2,2K)\cap\mathbb Z_{\ge1}\)
contains every actual cofactor. Its extraneous endpoints are killed by
the product mask. Each divisor pair occurs once, and the factor
\(4N^{-3/4}(N/n)^{3/4}\) restores precisely \(4n^{-3/4}\).
The real top condition \(n\le Z\), including equality when \(Z\) is
integer, remains explicit.

For fixed \(d\), the nonzero support of \(h_{N,T}(dk)\) is an interval,
with at most two boundary jumps. On its smooth part, \(dk\asymp N\).
Differentiation with respect to \(k\) gives total variation bounded by
a fixed multiple of
\(\sup|\Psi|+\sup|s\Psi'(s)|\): the derivative is \(O(1/k)\)
over a bounded ratio of endpoints. The factor \((N/(dk))^{3/4}\)
is bounded there. For two divisors the product support is the
intersection of two intervals, and the product variation is bounded
by the individual variations and suprema. It too has at most two
outer jumps. This checks both scalar and correlation Abel summations.

For the scalar sum the phase parameter is
\(\mathcal T=R\sqrt d\sqrt K\asymp T\sqrt N\), and its normalized
phase is the exact square-root monomial on a fixed positive interval.
The accepted exponent pair gives
\(\mathcal T^{13/84+\eta}K^{1/2}\). The source length condition
holds since \(K/\mathcal T\ll\sqrt N/T\le T^{-1/4}\).
Proper intervals and the symbol variation introduce only allowed
subpower factors. Restoring \(4N^{-3/4}\) and summing \(O(D)\)
divisors gives

\[
 |H_{N,D}|\ll_\eta
 T^{13/84+\eta}N^{-29/168}D^{1/2}.
\]

The pair count is \(O(N)\), giving independently
\(|H_{N,D}|\ll N^{1/4}\). Consequently a nonempty level set satisfies

\[
 N\gg v^4,\qquad
 D\gg_\eta T^{-13/42-2\eta}v^2N^{29/84}.                   \tag{R3}
\]

Substitution of the first restriction into the second gives
\(D\gtrsim T^{-13/42}V^{71/21}\), apart from stated logarithms and
small powers. At \(V=T^{13/125}\) the exponent is
\(-13/42+(13/125)(71/21)=221/5250>0\), as claimed.

### B. Real cosine identity, diagonal and absolute anchor

There are at most \(2K\) ambient integer cofactors. Cauchy after
aligning actual real values therefore gives exactly the permissible
constant

\[
 J^2v^2<32KN^{-3/2}\mathfrak Q.
\]

Writing the two phases as \(A-3\pi/4\) and \(B-3\pi/4\), their product
is
\[
 \tfrac12\{\cos(A-B)+\cos(A+B-3\pi/2)\}
 =\tfrac12\{\cos(A-B)-\sin(A+B)\}.
\]

Thus the sign in claimant (9) is correct. The kernels involve
\(R_j\sqrt d-R_l\sqrt e\) and \(R_j\sqrt d+R_l\sqrt e\);
the absolute radius has not disappeared.

Only the minus terms with \((j,d)=(l,e)\) form
\(\mathfrak D=\tfrac12J\sum_{d,k}c_{d,k}^2\).
All other exact-zero minus arguments and every sine term correctly
remain in the signed \(\mathfrak O\). The upper bound
\(\mathfrak D\ll JN\) follows from the same pair count.
For a full block with \(N\le cT\), \(\Psi\) is bounded below if fixed
\(c\) is small. There are \(\asymp N\) admissible pairs with odd
\(d\), including \(D=N,K=1\) and \(D=1\). This verifies the limited
claim \(\mathfrak D\asymp JN\), without lower-bounding
\(\mathfrak Q\).

A common radius translation changes the two kernels by respectively
\(R_*(\sqrt d-\sqrt e)\) and \(R_*(\sqrt d+\sqrt e)\).
The characterization of this interface as anchored is therefore exact.

### C. Conditional power ledger and complete event implication

Substituting (R1) into Cauchy contributes at most half the left side
from its first term. Absorbing it and using the diagonal yields

\[
 Jv^2\ll_\eta T^{\rho+\eta}\frac{\sqrt N}{D}.
\]

The maximal separated set covers its full level set by intervals of
radius \(N^{-1/2}\), giving measure
\(O(T^{\rho+\eta}D^{-1}v^{-2})\).
For a nonempty set, the integer inequality \(J\ge1\) also gives
\(D\ll T^{\rho+\eta}\sqrt N\,v^{-2}\). Combining this with (R3),

\[
 v^4\ll T^{\rho+13/42+O(\eta)}N^{13/84},
\]

and hence

\[
 N\gg T^{-2-84\rho/13-O(\eta)}v^{336/13},\qquad
 D\gg T^{-1-29\rho/13-O(\eta)}v^{142/13}.
\]

The covered measure is therefore
\[
 O_\eta(T^{1+42\rho/13+O(\eta)}v^{-168/13}).
\]

Every exponent in claimant (13)--(15) is correct. A lower bound below
one is harmless; if it exceeds the actual finite range, the high set
is empty. No fractional sample count is substituted for \(J\).

The entire \(n>Z\) series has uniform error \(O_A(T^{-A})\), by the
actual divisor bound and Schwartz decay. For large \(T\) it is at most
\(V_0/2\). At each \(V\ge V_0\), an actual high value forces one of
the \(L\) rectangles above \(V/(2L)\). Union over all rectangles,
absorption of their logarithms, and multiplication by the bounded
window give
\[
 D_B(V)\ll_\epsilon
 T^{1+42\rho/13+\epsilon}V^{-168/13}.
\]

This applies at every integration level, so it pays all mixed scales
through the actual event. The boundary term and integral are
\[
 H_{12}=V_0^{12}D_B(V_0)
       +12\int_{V_0}^{\infty}V^{11}D_B(V)\,dV
 \ll T^{1+42\rho/13+\epsilon}V_0^{-12/13}.
\]

Since \(168/13=12+12/13\), the integral converges. Exactly
\((13/125)(12/13)=12/125\) and
\(42(208/2625)/13=32/125\). This proves (R2), with target
\(113/125+32/125=29/25\). Uniform absolute convergence handles
bounded \(T\). This is a valid implication from (R1), not its proof.

### D. Available kernel and limited absolute-closure failure

For a nonzero argument the accepted square-root kernel, followed by
the checked product-symbol Abel summation, gives
\[
 |\mathcal K_{d,e}(u)|\ll_\eta T^\eta
 \min\{K,\sqrt K(|u|^{13/55}+|u|^{-1})\}.
\]

The auxiliary scale \(T'=CT\sqrt D\) satisfies
\(|u|\le T'\) and \(K\le (T')^{3/2}\).
Its epsilon losses are still powers of \(T^\eta\), since
\(D\le T^{3/2}\). The zero argument is correctly treated by \(K\).
Splitting \([K/2,2K)\) into boundedly many comparable intervals
matches the accepted ambient block convention.

For fixed \(j,d,e\), the minus arguments indexed by \(l\) have spacing
\(\gg K^{-1/2}\). Their few closest terms cost \(O(K)\); summing the
inverse-argument part over the remaining separated terms costs
\(O(K\log(2+J))\). For the plus arguments,
\[
 \sum_l\frac{\sqrt K}{u^+_{jl,de}}
 \ll\frac{J\sqrt K}{T\sqrt D}\ll K,
\]
using \(J\ll1+T\sqrt N\). This independently verifies the report's
brief assertion about that part. The growing kernel term costs
\(J\sqrt K(T\sqrt D)^{13/55}\) per \(j,d,e\).
Summation gives exactly
\[
 |\mathfrak O|\ll_\eta T^\eta
 \{JD^2K+J^2D^2\sqrt K(T\sqrt D)^{13/55}\}.
\]

Multiplying by \(KN^{-3/2}\), the two expressions become
\(J\sqrt N\) and \(J^2T^{13/55}D^{34/55}\).
Thus the claimed restoration is correct. At the lowest original level,
\(v^2\) has power \(26/125<13/55\), so the latter certificate
cannot be absorbed even for \(D=1\); larger \(D\) increases it.
This is failure of this stated upper-bound certificate, not a lower
bound on the signed energy or an impossibility theorem for other
anchored arguments.

The unconditional upper powers are also correct:
\(10\beta\) and \(1+20\beta/13\) both exceed \(29/25\);
the former dominates because \(\beta>13/110\).
Their lower-boundary costs are \(26/25\) and \(29/25\).
The conditional reconstruction computes
\([3+(1+29/25)/2]/13=102/325\), not quarter.

## 4. First unproved step and review limitations

The first unproved step is exactly claimant (12), reproduced as (R1).
Nothing in the scalar rectangle restriction, the nonnegative
\(\mathfrak Q\), the constant diagonal, or the accepted unweighted
kernel proves this signed estimate. The report preserves that gap
explicitly. The present review has found no earlier invalid step.

This is a NONBLIND seam audit of the final claimant hash, not a
statement-only rederivation and not an independent proof of the external
exponent-pair theorem. Only the already accepted source interface was
checked. The full target and its other analytic parents remain open.

## 5. Controls and outcomes

- Exact actual divisor coefficients and their unique rectangle
  occurrence: PASS, including singleton and partial top block.
- Cofactor endpoints and product-symbol variation: PASS for all
  \(K\ge1\), real \(Z\), and empty intersections.
- Real cosine signs, minus sine, constant-only diagonal split:
  PASS. Other zero arguments remain in the signed off-diagonal.
- Absolute-radius information and no difference-only replacement:
  PASS. No free translation or modulation is used.
- Conditional exponents, integer \(J\ge1\), cover width, and
  \(\rho=208/2625\): PASS with derivation in Section 3C.
- Full high-event union, boundary layer-cake term, all higher levels,
  all dyadic rectangles and Schwartz tail: PASS.
- Exact versus nonzero relations, squares, nonpairing and character
  controls: PASS as algebraic controls only. They are not asserted
  to be actual high-value configurations.
- Limited modulus-closure conclusion: PASS. The claimant does not
  confuse failure of its certificate with a lower bound or universal
  no-go result.
- Source hypotheses, real endpoints, restored sharp powers and
  fixed-order/full-quarter distinction: PASS.
- Numerical controls: none required or performed; all checks here
  are exact algebra, inequalities, endpoint checks, and source matching.

## 6. Dependencies and exact artifacts used

The reviewed final claimant is
rounds/codex-managed/gc-actual-radical-high-values/reports/anchored_divisor_high_values.md,
SHA256
7fb1a536ef78d6e2af007bf179fa8c3ce74cda69c96948a81043b3a4cf9213d8.

Only it and the original allowed common context were used: protocol.md;
state/proof_obligations.yml; state/active_campaign.yml;
strategy/round216_actual_radical_high_values.md;
strategy/gauss_circle_strategy_checkpoint_round214_2026-09-28.md;
rounds/codex-managed/gc-complete-localized-wave-moment/synthesis.md;
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md;
rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md;
rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_arithmetic_source_gate.md;
and the previously read exact-resonance kernel. No other round216
report or candidate was read.

The sole source interface was directly checked again at
[Bourgain, arXiv:1408.5794v2, Section 5, Theorem 6 and its following discussion](https://arxiv.org/html/1408.5794v2#S6),
on 2026-09-28. It gives the accepted exponent pair and explicitly
addresses lengths exceeding the square root of the phase parameter
and proper subintervals with logarithmic loss. Here the derivative is
an exact positive multiple of \(k^{-1/2}\), so the monomial class
matches; the length is below the phase parameter. No weighted divisor
theorem is imported from it. The interpolated \(13/55\) correlation
bound is the already accepted local kernel, with the auxiliary scale
checked in Section 3D.

## 7. Recommended state effect

Retain the claimant as **GREEN, final-hash verified, scoped conditional
method evidence**. No change to H216, the complete moment or pointwise
frontier, M1/M2/GAR, endpoints, or the full-quarter target is justified.
The one-sided signed input (12) remains unproved.

Only this assigned review file was written. Originals and shared
state were not changed. Stop this bounded review here.
