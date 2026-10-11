# Round 204 conductor derivation and scope control

Date: 2026-09-26. Campaign: `gc-complete-large-values-duality`.
Starting graph SHA256:
`abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`.
Conductor analysis; not an independent blind report and not acceptance by itself.
The previous goal turn made progress by completing the three assigned reports
and saving the unaccepted candidate before the goal was paused. On resume,
the authoritative goal is active, the saved graph/draft/report hashes match,
and the original frozen objective is unchanged.

## 1. Result

The complete weaker distribution is sufficient for an improved recorded
moment comparison, but insufficient for the frozen distribution target.
The candidate kernel retains the full series, its arithmetic coefficients,
every dyadic block and infinite tail, and the singleton n=1 after review repair.
No pointwise exponent or parent estimate follows beyond the inherited input.

## 2. Exact statement and hypotheses

Use precisely the kernel's fixed real even Schwartz function Psi, bounded
nonnegative displaced window w, real T>=2, arbitrary real U>=0, and V>=1.
Only the moment consequence specializes Psi to the transform of a fixed
nonnegative radial smooth unit-mass mollifier. Write

\[
\kappa=13/55,\quad q=136/13,\quad
\theta=(3292+25\sqrt{1717})/13762,\quad\beta=2\theta-1/2.
\]

The bound to accept is D(V)<<T^epsilon(V^-2+TV^-q). The stronger frozen
target is D(V)<<T^(29/25+epsilon)V^-12 over its stated height range.
These are different statements. The former is proved using the actual
coefficients but is uniform over a wider coefficient-norm class.

## 3. Independent derivation and exact power accounting

The accepted pair gives |K_N(u)|<<T^epsilon |u|^(13/84)N^(97/168)
only in its legal phase/length range. The elementary second-derivative
bound gives |u|^(1/2)N^(1/4) there. Weights 42/55 and13/55 respectively
give the exact exponents13/55 and1/2. The monotone first derivative
handles small u without crossing an integer; a fixed comparable
u~sqrt(N) interval handles the change of source normalization. The
kernel at u=0 remains the full number of indices.

For coefficient energy A N^(-1/2), delta=N^(-1/2) separated local
samples and a window length h, finite Cauchy and the harmonic row sum
give Jv^2<<A sqrt(N)+A^2(Jh^kappa+sqrt(N)log(2+J)). Absorb the first
off-diagonal term with h a fixed multiple of(v^2/A^2)^(1/kappa).
Covering costs delta J, with no assertion that values stay large on
the covering intervals. The number of windows is O(1+T/h). Its1 is
exactly the V^-2 term. Removing it would fail for one aligned peak.

Schwartz decay above Z=T^(3/2) gives a uniform l1 error bounded by
T^(3/8+3eta/2-L/4). A fixed sufficiently large L makes it smaller
than every required fixed negative power. The threshold is halved
before taking the union of O(log T) block level sets. Zero extension
keeps the kernel unweighted even on partially cut blocks. The
singleton n=1 obeys the same finite estimate directly. All constants
and logarithms fit an arbitrarily small final epsilon loss.

The sharp/smooth identity is
P(R^2)=sqrt(R)H_T(R)/pi+O(T^(1/2+epsilon)), with the same smoothing
width T^(-1/2) throughout the window. The closed annulus includes
the sharp counting jumps. The Bessel remainder is summable because
sum r2(n)n^(-5/4) converges. Hence the inherited pointwise theorem
supplies sup|H_T|<<T^(beta+epsilon), including at real jump radii.

Layer cake gives, for fixed p>2,

\[
M_p\ll T^{1+\epsilon}+T^{(p-2)\beta+\epsilon}
 +T^{1+\epsilon}\int_1^{T^{\beta+\epsilon}}V^{p-1-q}\,dV.
\]

Here the final integral is bounded for p<q, logarithmic at p=q,
and is dominated by the displayed high-value term for p>q because
beta(q-2)>1. At p=2 the V^-2 contribution adds only a logarithm.
Restoring the leading amplitude T^(p/2) and Jacobian T gives

\[
\int_{Y/2}^{3Y}|P(x)|^pdx
\ll Y^{1+p/4+\epsilon}+Y^{1+(p-2)\theta+\epsilon}.
\]

For p=12 the radius-moment exponent is10beta, the sixth-power
norm exponent is5beta=10theta-5/2, and the sharp moment exponent
is1+10theta. The moment range of conjectural order extends to
q_star=2+1/beta. Since beta<27/208, q_star>262/27. No inaccessible
Ivic proof is used to replace a parameter in a printed theorem.

For V=T^v, dividing the two distribution terms by the target gives
the powers10v-29/25 and(20/13)v-4/25. Both are nonpositive exactly
through v<=13/125. The high end v=beta is not covered. Thus even
the complete weaker bound leaves a radius-moment deficit
10beta-29/25 and a norm deficit5beta-29/50.

The persistence exponent is(1+10theta)/13, exceeding theta by
(1-3theta)/13>0. More generally, the high-p term tends to the
inherited theta under this bridge, not to one quarter. This is
moment progress only and cannot close the full goal.

## 4. First unproved step

The remaining task is a complete estimate exploiting the actual arithmetic
coefficients at heights T^(13/125)<V<=T^(beta+epsilon). The norm-only
argument cannot make that estimate for arbitrary coefficient vectors.
The discovery report's weighted-Gram attempt retains the exact derivative
of e(u sqrt(x)) in Stieltjes integration. Its remainder contains
u integral P(x)x^(-1/2)e(u sqrt(x))dx. Bounding P pointwise pays
|u|N^theta after normalization and fails to improve the distribution.
This is a bounded unsuccessful attempt, not a universal arithmetic no-go.

## 5. Controls and outcomes

The aligned vector a_n=N^(-3/4)e(-R0 sqrt(n)) has energy N^(-1/2),
supremum N^(1/4), and a peak of width cN^(-1/2). Its twelfth moment
is at least cN^(5/2). Choosing N~T^(4beta) yields T^(10beta).
The coefficient-uniform source and norm data admit that example;
the actual r2 coefficients are a different fixed family. No arithmetic
counterexample or false lower bound for its signed moment is claimed.

All relevant controls are analytic: u tending to zero; u~sqrt(N);
the full diagonal; one or zero selected samples; h larger than T;
delta larger than h; n=1; U=0; U beyond Z; partial final blocks;
inclusive integer-radius jumps; p=2 and p=q; bounded T. No mathematical
numerical experiment was used. Mechanical file/hash/graph checks have
no status as proofs of an analytic theorem.

## 6. Dependencies and artifacts

- `protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`.
- `strategy/round204_complete_large_values_attack.md` and its frozen plan.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
- The three Round204 reports, read after their completed independent tasks.
- Round203 synthesis and the Round202/203 closure procedures, used only
  for exact scope and state-validation procedure.
- Accepted dependencies: H1-H3, Divisor-bound-elementary,
  Bourgain-2017-reciprocal-exponent-pair-source-audit, and
  GC-external-Li-Yang-theta-star. Their unchanged historical scopes apply.

This analysis does not re-audit every historical graph node. The separately
assigned source, Gram/tail, and reconstruction reviews must pass against
the final candidate hash before a State Patch is applied.

## 7. Recommended state effect

Promote only the complete weaker distribution and its proved moment
consequences after all required exact-hash reviews and validation gates.
Keep all existing nodes unchanged. Close Round204 with the frozen target
explicitly open, then perform the scheduled broad strategy/current-literature
review in Round205. No successor is frozen by this analysis.
