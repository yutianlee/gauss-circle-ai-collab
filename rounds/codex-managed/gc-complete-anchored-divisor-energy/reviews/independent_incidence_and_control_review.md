# Round219 independent incidence and conductor-control review

## 1. Result

Campaign: `gc-complete-anchored-divisor-energy`; round 219.
Reviewer: temporary `joint_cofactor_dispersion` subagent, NONBLIND
exact-hash cross-review, 2026-09-28. Verdict: **GREEN for the stated
packing, inverse-certificate absorption, and complete failure ledger.
No required mathematical repair identified.**

Reviewed and hash-verified artifacts:

* `reports/actual_anchor_incidence.md` —
  `5f1c44affd95367bff61ebc1a8333fba840abece9c5775e88e4a2210f549a64b`.
* `controls/conductor_anchor_packing.md` —
  `b5ccf3e2c362203568885fcc60c39836e5f455a2f6197e8d4dc673b8eb1831bf`.

Both paths are under
`rounds/codex-managed/gc-complete-anchored-divisor-energy/`.

The sharpened inverse-frequency certificate is bounded by

    JN sqrt(J)+J^2 D sqrt(N) log(2T)/T.

For the actual nonempty high rectangles, it fits any fixed small
absorption coefficient plus T^(169/3500+epsilon) JN. The loss is below
the frozen rho=208/2625 by exactly 13/420. This is a valid improvement
of the named component cost, subject to the conductor's overall gates.

The full signed target remains unproved. The complete capped residual
has Cauchy-restored coefficient

    J^2 min(sqrt(N),T^(13/55)D^(34/55)),

which the present conditions do not absorb uniformly. The examples in
the reviewed files test that cost ledger only and are not asserted
actual high-point configurations. Neither the moment nor a pointwise
exponent improves.

## 2. Exact hypotheses and scope checked

Use the original216 literal rectangles with real T>=2,
N<=T^(3/2), 1<=D<=N, K=N/D>=1, d,e in[D,2D), and the actual
cofactor and norm cutoffs contained in h. Anchors R_j lie in[T/2,2T]
and are N^(-1/2)-separated. The target concerns a maximal separated
subset of the actual high set |H(R)|>v, with its actual real signs
sigma_j=sign H(R_j), and v>=T^(13/125)/(2L).

The incidence proof itself needs only separation. Its application to
the target additionally needs the actual high-rectangle restrictions,
the full Schwartz coefficient, and nonemptiness. The reviewed files
make this distinction correctly. Empty sets have J=0 and need no
estimate; no fractional sample count is used.

For fixed j, the claimant defines C_j(A) by

    |R_j sqrt(d)-R_l sqrt(e)|<=A/sqrt(K).

Its bound is asserted for A>=0. The conductor uses A>=1 for the
dyadic inverse-kernel summation; these are compatible formulations.
The signed energy keeps the actual minus cosine and plus sine, and
removes only the constant minus terms (j,d)=(l,e). All other exact
zeros and all plus terms remain.

The positive inverse envelope is explicitly a certificate used after
an upper bound on the oscillatory kernel. It is not asserted to be
an exact signed decomposition of Q or O. All constants may depend
on the fixed mollifier, window, and requested small exponents.

## 3. Independent derivation and verification

### 3.1 Exact radical classes and character signs

Only odd d,e can contribute because chi4 vanishes on even divisors.
An active exact equality implies (R_j/R_l)^2=e/d, whose reduced
numerator and denominator are odd. This defines an equivalence
relation on the anchors. In a finite component, choosing a common
odd denominator represents the anchors as R_j=r sqrt(b_j), with
positive odd integers b_j. No bounded-height claim about those
integers is needed.

Exact labels then satisfy b_j d=b_l e=q, and q is odd. Since
chi4(b_j)^2=1,

    chi4(q/b_j)=chi4(q)chi4(b_j).

Grouping the exact constant minus terms by q and factoring the common
chi4(q) gives precisely the square formula in the incidence report's
(9). The actual h(qk/b_j) and sigma_j remain inside each square.
The individual-position squares give exactly the original Dcal;
cross terms can be negative, so E0-Dcal need not be positive. The
complete Q also contains every other minus and plus term, and E0
is not promoted to a lower bound for Q.

For a fixed reduced ratio d/e=a/b, write d=at,e=bt. There are
O(D/max(a,b)) admissible t in the literal dyadic box. The harmless
additive 1 is absorbed because an admissible pair has max(a,b)<=2D.
If a,b are odd, active t are odd and

    chi4(d)chi4(e)=chi4(ab)

throughout the family. If either is even, there is no active pair.
This establishes the claimed limitation on automatic character
cancellation without introducing any artificial high-value signs.

### 3.2 Uniform rational-anchor packing

Put X=T sqrt(N) and x_l=(R_l/R_j)^2. The derivative of R_l^2/R_j^2
with respect to R_l is comparable to 1/T on the prescribed radius
range. Thus distinct anchors give

    |x_l-x_(l')|>=c/X.

Squaring the near-incidence expression exactly gives

    |d/e-x_l|
      =|R_j sqrt(d)-R_l sqrt(e)|
        (R_j sqrt(d)+R_l sqrt(e))/(R_j^2 e)
      <=C A/X.

There is no omitted D or K power: the original width A/sqrt(K)
is divided by T sqrt(D), and sqrt(KD)=sqrt(N).

Reduce d/e=a/b and group by dyadic height H<=max(a,b)<2H.
Ratios d/e lie in a fixed compact positive interval. Distinct reduced
fractions in that group have distance at least c/H^2, and there are
O(H^2) of them. Each has O(D/H) original common multiples, exactly
the multiplicity needed when returning to d,e.

For fixed j, a given fraction belongs to at most C(A+1) anchor
intervals by anchor separation. Conversely, each anchor interval
contains at most C(1+A H^2/X) fractions by rational separation.
Hence the number M_H of pairs (l,a/b) obeys both bounds and therefore

    M_H<=C min((A+1)H^2,J(1+A H^2/X)).

Using min(u,v+z)<=min(u,v)+z, multiplying by D/H, and summing
dyadic H<=2D gives

    C_j(A)
      <=C D sum_H H^-1 min((A+1)H^2,J)
                          +C J A D/X sum_H H
      <=C D sqrt(J(A+1))+C J A D^2/X.

The first sum is geometric on each side of
H=sqrt(J/(A+1)); if the split lies outside the available range,
the same upper bound follows by using just the appropriate side.
The second dyadic sum is O(D), with no unnecessary logarithm.
At A=0 this proves C_j(0)<=C D sqrt(J), including the literal
constant diagonal. Thus both the claimant's all-A statement and the
conductor's A>=1 specialization are correct.

No thin-rational-density theorem, generic-position assumption, or
character cancellation is used. Deleting even or unsupported pairs
can only decrease this positive count.

### 3.3 Entire inverse kernel, including zeros and plus terms

The inherited weighted kernel follows by Abel summation because
h(dk)h(ek) has uniformly bounded smooth variation and finitely many
bounded jumps on its actual interval support. At u=0 its bound is K;
at u!=0 the inverse envelope is

    W(u)=min(K,sqrt(K)/|u|).

The full range satisfies sqrt(K)|u^-|<=C X. In the initial band
sqrt(K)|u^-|<=1, the packing bound with A=1 covers every zero and
near zero. In the dyadic band of size A>=1, W<=C K/A. Summing
over j and all dyadic bands therefore gives

    sum W(u^-)
      <=C KJ sum_A A^-1
         [D sqrt(J(A+1))+J A D^2/X]
      <=C JN sqrt(J)+C J^2 D sqrt(N) log(2T)/T.

The first dyadic sum converges as A^-1/2. The second contains O(log T)
terms because N<=T^(3/2), and its restored factor is
K D^2/X=D sqrt(N)/T.

For plus arguments, u^+ is comparable to T sqrt(D). Each inverse
term is O(sqrt(K)/(T sqrt(D)))=O(sqrt(N)/(TD)). There are
O(J^2D^2) positions, so the total plus contribution is
O(J^2D sqrt(N)/T). This checks that the inverse part of every plus
term, including its diagonal positions, is paid explicitly. No plus
sine is dropped because its absolute frequency is large.

The split of the original scalar estimate is valid because
min(K,a+b)<=min(K,a)+min(K,b). It is an upper-envelope split only;
the reviewed files correctly avoid claiming a corresponding exact
signed split of the oscillatory energy.

### 3.4 Schwartz restriction and loss allocation

The original rectangle has O(N) divisor/cofactor incidences and
coefficient size O(N^-3/4) times the actual Schwartz multiplier.
Thus for every fixed M,

    |H(R)|<=C_M N^(1/4)(1+N/T)^(-M),

after renaming the decay order if one starts with decay in sqrt(N/T).
For any fixed zeta>0, this is below the retained high level when
N>=T^(1+zeta) and M is sufficiently large. One may either use
monotonicity of N^(1/4)(N/T)^(-M), as in the claimant, or the
coarser N<=T^(3/2) bound, as in the conductor control. Both prove
the asserted restriction for nonempty high rectangles, with constants
depending on zeta. Neither imposes a false exact cutoff at N=T.

The required pre-Cauchy scalar restriction is

    D>=c_eta T^(-13/42-O(eta))v^2 N^(29/84).

Its exponents match the permitted cofactor estimate: multiplying
(T sqrt(N))^(13/84)K^(1/2) by D N^-3/4 gives
T^(13/84)N^(-29/168)D^(1/2). The original absolute count also gives
N>>v^4. These are actual necessary conditions, not existence claims.

For fixed small delta>0, Young's inequality with
a=v^2 D/sqrt(N) gives

    C JN sqrt(J)
       <=delta J^2v^2D sqrt(N)
                          +C_delta JN sqrt(N)/(Dv^2).

The residual ratio satisfies

    sqrt(N)/(Dv^2)
       <<T^(13/42+O(eta))N^(13/84)v^-4
       <<T^(13/28-52/125+epsilon)
        =T^(169/3500+epsilon).

Here N<=C_zeta T^(1+zeta) contributes 13/84 plus a freely small
13zeta/84, while v>=T^(13/125)/(2L) contributes -52/125 and only
logarithmic factors. Any source loss multiplying the initial inverse
certificate is squared by Young's residual coefficient; it is still
an arbitrarily small exponent, so choosing input losses smaller than
the requested final epsilon pays it. The files' loss-allocation
statements are sufficient for this finite number of operations.

The other inverse term divided by J^2v^2D sqrt(N) is
O(T^eta log T/(T v^2)), uniformly tending to zero by a fixed power.
It fits any prescribed remaining absorption coefficient. Bounded T
is harmless: the separated sample count and all original indices are
then bounded, so the JN coefficient can be enlarged.

Finally,

    208/2625-169/3500=13/420.

Thus the claimed inverse component fits the target loss budget with
a genuine fixed exponent margin. The original constant diagonal
Dcal=O(JN) also fits it. This does not bound the other component.

### 3.5 Complete capped leftover and the compatible scale control

For both minus and plus kernels, the positive-power envelope is
bounded by its maximum anchored frequency O(T sqrt(D)). Counting
all positions, without omitting any exact or near family, gives

    C_eta T^eta J^2 D^2
             min(K,sqrt(K)(T sqrt(D))^(13/55)).

Multiplication by the original Cauchy factor K N^-3/2 restores
respectively

    K^2 D^2 N^-3/2=sqrt(N),
    K^(3/2) D^2 N^-3/2 T^(13/55)D^(13/110)
                               =T^(13/55)D^(34/55).

The complete inequality therefore retains both a linear sample term
T^(169/3500+epsilon)J sqrt(N)/D and a quadratic term
T^epsilon J^2 min(sqrt(N),T^(13/55)D^(34/55)). This correctly
accounts for the whole attempted closure; the improved inverse part
has not been substituted for the missing signed bulk.

At N~T^(2/3), D~T^(2/15), and v~T^(13/125), the available scalar
ceiling exponent is

    13/84-(29/168)(2/3)+(1/2)(2/15)=67/630,

which exceeds 13/125 by 37/15750. The trivial N^(1/4) ceiling
and effective-support restriction also permit these scales. Thus the
necessary conditions in the two files do not exclude them.

The restored quadratic coefficient is

    min(T^(1/3),T^(13/55+(34/55)(2/15)))
       =T^(263/825).

Its excess over v^2 is 263/825-26/125=457/4125; its exponent is
below the cap's exponent by 1/3-263/825=4/275. These calculations
verify the stated fixed deficit with the cap retained. They establish
that this available upper certificate does not imply uniform
absorption. They do not establish high-point existence or a lower
bound for any actual signed quantity at those scales.

### 3.6 Complete moment and full-goal restoration

Without a new signed bound, the accepted distribution and actual full
ceiling yield the high-tail costs

    W^10+T W^(20/13)+V0^10+T V0^(20/13),
    W<<T^(beta+epsilon), V0=T^(13/125).

Both upper terms and both lower-boundary terms are retained. The
largest exponent is still 10 beta. The original n>Z Schwartz tail
is uniformly arbitrarily small, and the finite exact rectangle
decomposition has O(log^2 T) pieces. The event implication at every
level V, with rectangle level V/(2L), pays every mixed contribution
without requiring every block to be high.

If the full target were eventually proved, the inherited complete
restoration would produce the high moment exponent
113/125+42rho/13=29/25 at rho=208/2625, and then the fixed
102/325 discrepancy milestone. The reviewed files preserve the missing
premise and do not infer this conclusion from a single paid component.
No sufficient unbounded-order family or quarter theorem follows.

## 4. First doubtful or unproved step

No doubtful mathematical step was found in the two named claims at
their reviewed hashes. No required repair is requested.

The first missing step remains a signed estimate of the complete
oscillatory remainder strong enough to remove the quadratic coefficient
in Section 3.5. Exact class squares absorb chi4 into anchor signs;
they do not show that those signs balance. Near rational packing
counts incidences but supplies no cancellation for the nonzero
positive-power kernel or the plus sine aggregate.

The inverse-envelope split is not an identity expressing the original
energy as two separately signed quantities. Consequently any future
use must retain the complete exact original energy as authoritative,
as both reviewed files presently do.

## 5. Controls and outcomes

* Rational packing, reduced fractions, and common-multiple factors:
  GREEN. Both anchor spacing and fraction spacing are used with their
  correct scales; all dyadic heights are summed.
* Exact classes and chi4: GREEN. Odd rational-square components and
  the exact weighted square formula are correct. No artificial
  high-wave signs are substituted.
* Full inverse kernel: GREEN. Exact zeros, nearest nonzeros, every
  inverse-distance band, and all plus inverse terms are included.
* Schwartz cutoff: GREEN. The N<=T^(1+zeta) restriction is derived
  only for actual nonempty high rectangles; the original sum retains
  its literal truncation and full Schwartz tail.
* Source losses and absorption constants: GREEN. Young squares only
  freely chosen subpowers, and the fixed exponent is 169/3500 with
  margin 13/420. The second inverse term is uniformly absorbable.
* Complete capped leftover: GREEN bookkeeping; target OPEN. Both
  branches of the cap and every kernel family remain in the ledger.
* Actual versus enlarged scope: GREEN. Incidence upper bounds may
  hold for arbitrary signs, but no such enlarged assertion is used
  to manufacture a counterexample to the actual target. The scale
  example checks necessary-condition compatibility only.
* All rectangles, real endpoints, and tails: GREEN. Empty, singleton,
  partial top, K=1, literal half-open assignment, real anchors, and
  all original high-event levels are paid.
* Statement-only and full-goal scope: This is NONBLIND verification,
  not the isolated anchor-class derivation. No complete moment,
  M1/M2/GAR parent, or quarter theorem is promoted.

All verification was analytical/algebraic. No experiment, sample
configuration search, or new external theorem audit was used.

## 6. Exact dependencies and artifacts used

Newly read and hash-verified in this review:

    rounds/codex-managed/gc-complete-anchored-divisor-energy/reports/actual_anchor_incidence.md
    5f1c44affd95367bff61ebc1a8333fba840abece9c5775e88e4a2210f549a64b

    rounds/codex-managed/gc-complete-anchored-divisor-energy/controls/conductor_anchor_packing.md
    b5ccf3e2c362203568885fcc60c39836e5f455a2f6197e8d4dc673b8eb1831bf

Previously read permitted original task context: protocol; authoritative
graph at `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`;
frozen219 manifest and strategy; closed217 checkpoint; accepted complete
large-values and distinct-radical kernels; the original216 anchored
report at `7fb1a536ef78d6e2af007bf179fa8c3ce74cda69c96948a81043b3a4cf9213d8`;
the closed218 synthesis; and this agent's own disclosed218 report.

The reviewer's219 discovery report was frozen before this review at
`cbb7e8de456bb37c871eafaf21ffb4ecedeb36e7aac50b1719275d13cb1fef81`
and was not edited. Its reciprocal-anchor transform is not a dependency
of any packing or absorption claim verified here.

No isolated219 packet, additional sibling artifact, historical source,
or successor artifact was read. The conductor's earlier packing lead
and the claimants' shared nonblind provenance are disclosed in their
files. This review independently checks the argument rather than
counting agreement as evidence. Existing source qualifications remain
attached to the inherited scalar kernel.

## 7. Recommended state effect

Retain the two exact-hash artifacts as GREEN method evidence. No repair
cycle is requested on this seam. The conductor should keep its isolated
class-algebra review and complete closure gates separate.

The validated improvement pays an inverse-frequency component only.
No accepted complete moment, pointwise benchmark, full anchored target,
or quarter-goal status changes from this review. Do not create a new
unestimated residual node merely because its complete cost is written
explicitly. The conductor owns any State Patch and closing decision.
This review is the only file written during this follow-up, and the
subagent stops after returning its hash.
