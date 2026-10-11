# Round 206: independent divisor and absolute-placement review

Campaign: `gc-complete-signed-shell-arithmetic`. Role: independent
post-report mathematical reviewer; line/seam audit, not statement-only
blind. Date: 2026-09-26. Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Reviewed report:
`rounds/codex-managed/gc-complete-signed-shell-arithmetic/reports/actual_divisor_shell_attack.md`.
Exact reviewed SHA-256:
`999f9c77ff468a39fb87eb4c593bede24d9bd6542d5ee16a2ade7ae60e0743b5`.
This is a same-round review. No new round, source import, numerical
experiment, or authoritative-state mutation is involved.

## 1. Result

**Scoped GREEN.** The actual centered-coefficient absolute-sixth
obstruction, its uniform kernel nonvanishing and variable-width
Riemann-sum argument, the exact moving-threshold hyperbola/CRT
expansion, the repeated-shift separation, and both sixth-moment
thresholds are correct within the stated inherited interfaces.

In particular, the termwise absolute expansion has a genuine lower
bound of order XH^6, even after removal of every at-most-three-distinct
shift pattern. It exceeds the relaxed sufficient sixth threshold by
at least a fixed multiple of T^(136/125), before epsilon losses.
This obstruction applies to the absolute expansion only. It is neither
a lower bound for the signed sixth moment nor a refutation of the
twelfth-moment objective.

The separate X^(3+epsilon)H^6 CRT remainder figure is a valid upper
certificate obtained by summing individual variation bounds. It is
not a proved lower bound for the signed remainder. The report keeps
these two logically different conclusions separate. No mathematical
correction is required, and no new moment exponent is established.

## 2. Exact hypotheses and reviewed scope

The report uses real T>=2, X=T^2,
J=[X/2,3X], I=[T/sqrt(2),sqrt(3)T], and every dyadic N strictly between
T^(52/125) and T^(99/125). With the fixed reviewed mollifier and
partition it defines a real odd Schwartz filter F=F_(N,T),

\[
 E_N(x)=\sum_{m\ge1}(r_2(m)-\pi)
       F((m-x)/h(x)),\qquad h(x)=2\sqrt{x}/\sqrt N,
\]

and H=2sqrt(3X)/sqrt(N). Consequently H/sqrt(6)<=h(x)<=H on J.
The physical shell S_N is connected to E_N by the report's formula
(A6), with its uniform curvature error and all remote tails included.

The relevant available supremum, up to T^epsilon, is

\[
 W_0=\min(N^{1/4},T^\beta,T^{1/2}N^{-1/2}),
 \qquad 1/8<\beta<27/208.
\]

The two candidate sixth bounds are the variance scale XH^3 and the
relaxed scale Lambda XH^3, where

\[
 \Lambda=T^{4/25}N^{3/2}W_0^{-6}\ge T^{4/25}.       \tag{R1}
\]

Both are sufficient hypotheses, with the latter the less restrictive
one for the displayed interpolation. Neither is claimed necessary
for the actual twelfth moment. All asymptotic lower bounds below are
for sufficiently large T, uniformly over the entire middle band;
constants depend only on the fixed filters and windows.

## 3. Independent derivation of the audited seams

### Actual coefficients and a uniform absolute lower bound

Every representation orbit of a positive integer under quarter-turn
rotation has four distinct members. Thus r2(m) is a nonnegative
multiple of four, and the closest such multiple to pi is four:

\[
 |r_2(m)-\pi|\ge4-\pi>0.                           \tag{R2}
\]

This assertion uses actual representation multiplicities. It would
not be interchangeable with a representability indicator or an
arbitrary centered arithmetic sequence.

The fixed amplitude v(t^2)/t is nonzero. The corresponding limiting
sine transform F_0 is nonzero by Fourier uniqueness. Alternatively,
the derivative at zero is a nonzero constant times the positive
integral of v(t^2). On the whole middle band N/T<=T^(-26/125), so the
compactly supported amplitudes defining F converge, with all fixed
orders of derivatives, to the amplitude defining F_0. Integration by
parts therefore gives convergence in every fixed Schwartz seminorm.
It follows uniformly that

\[
 \|F\|_1\ge c>0,\qquad \|F\|_1+\|F'\|_1\le C.      \tag{R3}
\]

For a fixed real x in J, keep its actual width h=h(x), and set
g_x(t)=eta(t/X)|F((t-x)/h)|, with the report's eta. Its variation in
the summation variable t obeys

\[
 \operatorname{Var}(g_x)
 \le \|eta\|_\infty\|F'\|_1+
       (h/X)\|eta'\|_\infty\|F\|_1\ll1.             \tag{R4}
\]

The comparison between a lattice sum and the integral of a compactly
supported BV function has error at most its total variation. The
region on which eta equals one contains an interval of radius cX
around every x in J. The omitted integral tail therefore has size
O_A(h(X/h)^(-A)). Equations (R3)--(R4), h tending to infinity uniformly,
and X/h tending to infinity uniformly imply

\[
 \sum_{m\ge1}eta(m/X)|F((m-x)/h(x))|\ge c_1h(x).       \tag{R5}
\]

No fixed-width substitution is present: for each x the Riemann-sum
comparison uses h(x), and its constants are uniform in x. It applies
at integer centers and across the real endpoints of J.

The report's termwise absolute six-shift sum is exactly the integral
of the sixth power of the positive sum in (R5), with the extra factors
|r2(m)-pi|. By (R2) and h(x) comparable to H, its size is at least
cXH^6. This establishes the actual obstruction, rather than merely
showing that an upper bound is inconveniently large.

### Repeated shifts and the exact residual interface

Writing x=b+u, with 0<=u<1, is an exact change of variables. The
window indicator in W_(k,u)(b) preserves the partially occupied first
and last unit cells. After the fixed smooth localization every sum
in m is finite; before localization Schwartz decay also gives the
needed absolute convergence. Since all values are real, |E|^6=E^6.

An equality pattern with q distinct shifts has only q independent
shift sums. For each such sum the uniform Schwartz bound contributes
O(H); the anchor sum contributes O(X); the product of six actual
coefficients is O_epsilon(X^epsilon), including repetitions. Its
absolute contribution is therefore O_epsilon(X^(1+epsilon)H^q).
There are finitely many equality patterns for six coordinates.

Thus every q<=3 pattern is safe at the variance scale. This includes
all patterns without singletons, while correctly leaving the q=4
and q=5 repeated-coordinate patterns in the unresolved aggregate.
Subtracting the q<=3 positive contribution from cXH^6 preserves a
lower bound of that order after choosing epsilon small enough.

For the signed expression, bounding the absolute value of the *joint*
q>=4 aggregate is equivalent to the variance sixth-moment bound,
up to constants and the paid localization error. Indeed the complete
sixth moment is that aggregate plus a complementary sum bounded in
absolute value by X^(1+epsilon)H^3. The same equivalence holds with
the relaxed right side because Lambda>=1. It does not assert that
each remaining stratum, main term, or remainder must separately
satisfy that bound.

### Exact moving-mask hyperbola and CRT accounting

With M=ceil(6X), D=floor(sqrt(M)), and
L=floor(M/(D+1)), every divisor of an integer n<=M belongs either to
d<=D or to d>D. In the second case ell=n/d<=L, and conversely the
condition ell|n and n>D ell means exactly d=n/ell>D. Thus (A12) counts
each divisor once, including the boundary cases d=D and n=D ell.

The quotient character equals the difference of the two residue
indicators n=ell mod 4ell and n=3ell mod 4ell. The even quotient
values vanish automatically. Subtracting the small-divisor means
leaves exactly delta_D=4 sum_(d<=D) chi4(d)/d-pi=O(D^(-1)). The
report includes this constant atom rather than deleting it in an
individual correlation.

There are O(sqrt(X)) atom labels per coefficient. Each atom has at
most two congruence branches, with coefficients bounded by an
absolute constant. For a six-atom choice the conditions on the
anchor are b=r_i-k_i mod q_i. Pairwise compatibility modulo each
gcd is necessary and sufficient for a common residue class modulo
the lcm. Hence (A15) is the exact density, including noncoprime
moduli, zero/unit modulus branches, and repeated shifts.

All masks b+k_i>D ell_i must remain inside the weight, as the report
does. At most six such jumps and two real-window jumps occur. In
the smooth part, differentiating h(b+u) costs its relative derivative
1/(2(b+u))=O(1/X); cutoff differentiation costs O(1/X); the factors
(k_i-u)/h produced by differentiation are absorbed by arbitrary
Schwartz decay. The supremum, integrated derivative, and every jump
are bounded by

\[
 C_A\prod_{i=1}^6(1+|k_i|/H)^{-A}.                  \tag{R6}
\]

The discrepancy of a single arithmetic progression from its density
has a bounded primitive, uniformly in its modulus. Partial summation
therefore proves (A16) with exactly this variation cost. Incompatible
branches give zero, while compatible branches give their actual
density times the thresholded integral, plus the bounded remainder.
Large lcm values require no separate deletion or additional claim.

Summing the six-atom remainder bounds costs O(X^3) label tuples,
a fixed branch factor, H^6 from all shifts, and a unit u-integral.
This recovers O_epsilon(X^(3+epsilon)H^6). Opening all divisors instead
costs O(X^6) tuples. Both are valid upper-bound ledgers; neither
implies that the corresponding actual signed error is that large.
The common-modulus example in the report is also correct: the sixth
power of a centered residue indicator has positive average, and the
sixth power of chi4(d) is one for odd d. This refutes individual
independence/zero-mean substitutions, without giving positivity after
the signed kernel and divisor sums are restored.

### Sixth thresholds and complete power accounting

The amplitude in S_N(R)=R^(-1/2)E_N(R^2)+error and the Jacobian
dR=dx/(2sqrt(x)) together give

\[
 \int_I|S_N|^6dR\ll T^{-4}\int_J|E_N|^6dx+
                 \hbox{the stated negligible error}.          \tag{R7}
\]

If the variance sixth bound holds, the right side is
O(T^(1+epsilon)N^(-3/2)). The elementary original coefficient
supremum N^(1/4+epsilon) then supplies W^6=N^(3/2+epsilon), proving
the stronger conditional twelfth bound O(T^(1+epsilon)). Thus the
report's earlier calculation using only T^beta is sufficient but
not the sharpest implication, and its subsequent (A8a) correctly
records the stronger one.

Using the minimum of the three available suprema yields

\[
 \int_I|S_N|^{12}dR
 \ll T^{-4+\epsilon}W_0^6\int_J|E_N|^6dx
       +O(T^{-2+\epsilon}).                           \tag{R8}
\]

The sixth power of the curved-shell error contributes
O(T^(-2+epsilon)N^(-6)) before multiplication by W_0^6, and
W_0^6<=N^(3/2), confirming the smaller N^(-9/2) cost stated in
the report. Solving (R8) for a sufficient T^(29/25) output gives
T^(129/25+epsilon)W_0^(-6), exactly (A4'). Dividing by XH^3 gives
(R1), up to fixed window constants. For N=T^nu, the three pieces
of log_T Lambda in (A8c) follow directly, with breakpoints 4beta
and 1-2beta; both lie in the present middle interval.

The absolute obstruction compared with this relaxed threshold is

\[
 H^3/\Lambda\asymp
 \min\{T^{71/25}N^{-3/2},
        T^{71/25+6\beta}N^{-3},
        T^{146/25}N^{-6}\}.                            \tag{R9}
\]

Each entry decreases as N increases. At the upper edge N=T^(99/125)
their powers are respectively 413/250, 58/125+6beta, and 136/125.
Since beta>1/8, the second is greater than 136/125, as is the first.
This proves the uniform lower factor T^(136/125) for (R9). The
uniform epsilon loss can be chosen below this fixed margin. The
CRT upper-cost comparison has the additional X^2 factor, but remains
only an upper-cost comparison.

Finally, the existing second moment XH combined with the available
suprema gives the report's (A10), not a variance sixth moment.
Relative to the relaxed threshold the resulting exponents are
2nu-4/25, 10beta-nu/2-4/25, and 121/25-11nu/2 in their respective
ranges. Their claimed positive lower margins check out. This is a
failure of that interpolation certificate, without a lower bound
for the true sixth moment. The better accepted distribution estimate
continues to provide the complete T^(10beta+epsilon) twelfth bound.
Minkowski over all O(log T) blocks retains all cross-block terms in
the physical norm inequality.

## 4. First doubtful or unproved step

No doubtful step was found in the scoped obstruction or the algebraic
and analytic ledgers reviewed above. The first unproved estimate is
the joint signed q>=4 correlation bound in (A17), with either the
variance or relaxed right side. The local-density main terms and
weighted endpoint remainders remain coupled; cancellation of their
complete signed aggregate is not proved.

The relaxed sufficient threshold is not necessary for the frozen
twelfth moment. Consequently, even a proof that an attempted method
cannot establish that threshold would not disprove the target. The
report correctly makes no such converse inference.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Actual r2 absolute-sixth obstruction | GREEN: coefficient separation from pi and uniform filter mass give a genuine XH^6 lower bound for the absolute expansion. |
| Uniform nonvanishing | GREEN: N/T tends to zero uniformly, compact amplitudes converge smoothly, and the limiting filter is nonzero. |
| Variable width and real endpoints | GREEN: the BV argument uses each actual h(x), and its O(1) error is uniform at integer centers and both real window endpoints. |
| Complete divisor identity | GREEN: the strict hyperbola threshold partitions every divisor once; both quotient residues and the constant mean remainder remain. |
| Moving masks and CRT | GREEN: all threshold/window jumps enter variation; compatibility and lcm density are exact; no modulus or shift is removed. |
| Repeated-shift strata | GREEN: q<=3 is bounded absolutely; q=4,5 repetitions remain with q=6 in the joint unresolved interface. |
| Infinite tails | GREEN within the explicitly stated Schwartz bounds and inherited reviewed transform; localization occurs only after its error is paid. |
| Relaxed versus variance sixth scale | GREEN: (A4') is weaker by Lambda>=T^(4/25), and the absolute-placement obstruction still exceeds it uniformly. |
| Full moment ledger | GREEN: amplitude, Jacobian, supremum powers, transform errors and all middle scales are restored. No improved bound is inferred. |
| No-go scope | GREEN: absolute-expansion lower bound, CRT upper-cost certificate, and missing signed cancellation are explicitly distinguished. |
| Source and proof scope | GREEN within inherited source qualifications; no new primary theorem or pointwise exponent is imported or promoted. |

No numerical experiment was performed. File hashes and section checks
are mechanical provenance checks only.

## 6. Exact dependencies and artifacts used

- `protocol.md`, previously read and retained for this same round.
- The reviewed report at the exact SHA-256 printed above.
- The report's previously read exact inherited interfaces:
  `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md`,
  `rounds/codex-managed/gc-full-frontier-moment-strategy-review/reviews/independent_middle_band_review.md`,
  and `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.

No further local context or external literature was needed for this
review. The reviewer had separately authored the source-application
report in this campaign, but that report is not a dependency of this
audit; the present conclusions were checked directly against the
divisor report and its inherited interfaces. This is an independent
post-report audit, not a blind rederivation.

## 7. Recommended state effect

**Retain as scoped GREEN review evidence; no authoritative-state
change is recommended by this review.** The conductor may close the
arithmetic attempt as a fully priced no-gain result. The absolute
placement is rigorously obstructed, whereas the complete signed
correlation estimate and the frozen twelfth-moment objective remain
open. All accepted exponents, external qualifications, and M1/M2
obligations remain unchanged.

Only this assigned review was written during the review task. The
separately authorized correction to the reviewer's source report was
completed and its final hash communicated before this review. No
claimant report, shared synthesis, state, proof draft, validation
matrix, source card, or successor artifact was edited. The review
task stops here.
