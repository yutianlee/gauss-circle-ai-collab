# Strategy checkpoint after Rounds205--207

Review round:208. Campaign:gc-full-proof-signed-arithmetic-review.
Date:2026-09-27. This is a strategy decision, not an accepted graph theorem.
The original23September memo and full target remain unchanged.

## 1. Decision and its mathematical reason

Target the actual signed **tenth moment of each complete frequency block**,
using local Fourier reproduction to control its peak. This replaces the
previous sixth-to-twelfth sufficient certificate as the immediate attempt.
It does not claim the earlier complete twelfth-moment milestone.

Let T>=2, X=T^2, beta=2theta_LY-1/2, b=83/650, and retain the exact
physical block H_N, signed filter Z_N, variable h(x)=2sqrt(x)/sqrt(N),
window J=[X/2,3X] and fixed mollifier of205--207. The selected bound is

\[
 \boxed{\int_J|Z_N(x)|^{10}dx
 \ll_\epsilon T^{473/65+\epsilon}N^{-1/2}
 \quad\text{for every dyadic }T^{166/325}<N<T^{242/325}.}
 \tag{S208}
\]

Equivalently at these powers, one may prove directly
integral_I |H_N|^10 << T^(83/65+epsilon)N^-1/2,
I=[T/sqrt(2),sqrt(3)T]. The explicit shell errors are negligible.
No unknown block or tail is delegated to a future unestimated complement:
N<=T^(166/325) is already bounded pointwise by N^1/4, and
N>=T^(242/325) by(T/N)^1/2 up to the reviewed tail cutoff.
The singleton and infinite Schwartz tail are paid.

The new ingredient in the strategy is the complete local reproduction
inequality, not a claimed new arithmetic cancellation. Since H_N has
frequency support in[-2sqrt(N),2sqrt(N)], a Schwartz reproducing kernel
and Holder yield, for R0 in[T,sqrt(2)T],

\[
 |H_N(R_0)|\ll N^{1/20}
 \left(\int_I|H_N|^{10}\right)^{1/10}+O_A(T^{-A}).
\]

The off-window integral uses the GLOBAL coefficient bound and the
positive margin between R0 and the boundary of I. This factor N^1/20
is retained. Substituting(S208) and dx=2R dR gives |H_N|<<T^b.
Complete recombination and sharp reconstruction would therefore yield
P(x)<<x^(102/325+epsilon). All real endpoints are included.

The conductor proof and independent reviews are in the208 campaign's
controls/conductor_bandlimited_strategy.md and reviews/. This is a
conditional bridge; (S208) itself is open. It changes the next attack
because the old sufficient band was the larger
(T^(52/125),T^(99/125)), and local peak control admits looser inputs.

## 2. Price the missing estimate before attacking it

The reviewed variance and complete distribution, intersected at
V0=N^(13/220), give

\[
 \int_I|H_N|^{10}\ll T^\epsilon
 (T N^{-3/110}+T^{8\omega(\alpha)}),\quad
 \omega(\alpha)=\min(\alpha/4,\beta,(1-\alpha)/2),\ N=T^\alpha.
\]

The T^(8omega) term cannot be discarded. After shell conversion the
baseline is T^7 N^-3/110 + T^(6+8omega). Relative to(S208) the two
deficits are1-10b+26alpha/55 and8omega-10b+alpha/2. The second dominates
throughout the required band. Its exact maximum is7beta-101/130 at
alpha=1-2beta. The sixth-order version of the new peak gate has worst
deficit7326/17875; the eighth-order version is also more demanding in
this comparison. This selects order ten by a quantified cost, while
acknowledging that ten-factor correlations may be harder analytically.

These are deficits of existing upper certificates, not lower bounds on
the actual moment. The full arithmetic task must retain both rational
arms, all characters, every prefix label, actual varying width and near
frequencies. A fifth-convolution identity alone is exactly a rewritten
tenth moment. A successful attempt must estimate it at(S208), or obtain
a different complete pointwise improvement with every cost restored.

Round207's lower bound X^3H concerns termwise absolute sextuple integrals
after single-frequency grouping. It does not reject signed aggregation,
but also supplies no positive evidence for its smallness. Zero-th
frequency-bin sums are insufficient: within-bin phases must survive.
Repeated variance proofs, generic norm prices and another unestimated
partition are parked rather than counted as new endpoint progress.

## 3. Current primary literature and application decisions

The source review was bounded, current as of27September2026, and used
two fully priced interfaces per source task. It is not an exhaustive
literature claim. Exact definitions and versions are preserved in the
two source reports and their independent/conductor reviews.

| Source | Current check and decision |
|---|---|
| [Li--Yang2308.14859v2](https://arxiv.org/abs/2308.14859v2) | Record unchanged; preserve the graph's repaired narrow application, not an unrestricted intermediate theorem. |
| [Guth--Maldague2206.01093v2](https://arxiv.org/html/2206.01093v2), Theorems4--5 | Exact parabola lift and trace paid. Ordinary p12 decoupling gives block T N^2 and complete T^3, weaker than the accepted estimate. Amplitude-dependent envelopes leave an explicit arithmetic integral unproved. No saving imported. |
| [Blomer--Pascadi2607.24311v1](https://arxiv.org/html/2607.24311v1), Theorem1.1 | Actual internal M1 matrix and outer sums cost L^(119/32), against L^2, even on the legal primitive/unit part; exceptions stay explicit. A rational convolution is not automatically this kernel. |
| [Xiao--Li2609.24248v1](https://arxiv.org/html/2609.24248v1), Theorem1.1 | Fresh21September result concerns two shifted logarithmic cutoff profiles at the same integer, with Mobius/squarefree sieve weights. It is not additive six-point r2 correlation. Coefficients, cutoff, order and fixed-smoothing conditions fail; its logarithmic error would also be insufficient under the explicitly hypothetical transfer. |
| [Kim2509.24152v4](https://arxiv.org/abs/2509.24152v4) | Withdrawn10September2026; exclude as a source of a shifted-correlation gain. |
| [Bourgain--Watt1709.04340v2](https://arxiv.org/abs/1709.04340v2), [Dong--Robles--Zeindler2601.00292v2](https://arxiv.org/abs/2601.00292v2) | Both remain withdrawn; no import. |
| [Yamaguchi et al.2609.04725v1](https://arxiv.org/abs/2609.04725v1) | New September numerical evidence, not an asymptotic proof. No experiments run here. |

Additional current screens covered Guth--Maynard, Kim--Ko, Xiao,
Lamzouri, Gao, Edwin--Lin, Pascadi, Milicevic--Qin--Wu,
Fouvry--Kowalski--Michel--Sawin, Milicevic--Robinson--Shupe,
Robles, Baier and sparse-moduli large-sieve work. Their precise screening
levels and limits are in the reports. Conditional, almost-all, random,
indicator-weight or prime-power results were not silently promoted to
the fixed actual-coefficient uniform problem.

## 4. Preserve the full proof objective

The full target is still P(x)<<x^(1/4+epsilon). A success at(S208) would
improve the benchmark only to102/325. The all-order conditional peak
gate for fixed k>=2 and b>0 is

\[
 K_{2k}(N)\ll T^{k+1+2kb+\epsilon}N^{-1/2},
 \qquad T^{4b}<N<T^{1-2b}.
\]

For general b, the shell bridge and complements must hold on that entire
required band; extensions outside the reviewed205--206 range are explicit
hypotheses, not accepted by extrapolation. A Gaussian hierarchy
K_(2k)<<X(T/sqrt(N))^k would suffice when b>=1/(4k-2), hence as fixed
k grows it would imply quarter. One fixed order does not prove this
hierarchy. The isolated report independently establishes the alternative
full-discrepancy criterion delta_p/p→0 along unbounded fixed orders,
with all Jacobians, errors and persistence intervals paid.

The independent direct M1 HARD and SMOOTH parents, M2 TOP/BAL/UNBAL,
endpoint uniformity, and GAR's separate total-M1 quantifier remain open.
No examined internal import has a better paid path than the selected
whole-discrepancy peak gate. They remain available routes, not disproved
by this selection. Full formulas are retained in the arithmetic report.

## 5. Closure and next-round discipline

Close208 with an identity State Patch after final-hash reviews pass.
Preserve all399 nodes and the proof draft byte-for-byte. Record the new
conditional bridge, source exclusions and complete next target as strategy
evidence. No complete moment or pointwise exponent is improved this round.

Only after closure, design209 around(S208), allowing a direct signed
shell, arithmetic high-value, or fully paid rational-convolution attack.
Its exit must be a complete quantitative inequality or an exact bounded
failed application; a transform or generic no-go alone does not justify
another identical successor. Next mandatory broad review:211, after
208--210. Effort:100 percent analysis/algebra/source inspection; no
mathematical numerical experiments.
