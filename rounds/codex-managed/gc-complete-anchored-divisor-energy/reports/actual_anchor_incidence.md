# Round219 actual anchor incidences: paid inverse kernel, unpaid complete bulk

Campaign: `gc-complete-anchored-divisor-energy`.
Task: `actual_anchor_incidence`; role: barrier/no-go, selected context.
NONBLIND discovery report, 2026-09-28. Prior round218 work in this agent
is disclosed; no round219 sibling report or isolated packet was read.
Starting graph SHA256:
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
All mathematical work is analytical/algebraic; zero experiments.

## 1. Result

The complete actual anchored-energy inequality(12) at
rho=208/2625 remains unproved. There is, however, a sharper exact/near
incidence calculation than the old separate-count cost JD^2K.

For the actual separated anchors of one rectangle, let C_j(A) count
all triples(l,d,e) with d,e in[D,2D) and

    |R_j sqrt(d)-R_l sqrt(e)| <= A/sqrt(K),   K=N/D.

For every A>=0,

    C_j(A) << D sqrt(J(A+1)) + J A D^2/(T sqrt(N)).       (1)

At A=0 this gives C_j(0)<<D sqrt(J). The estimate is uniform in real
anchors and endpoints; no character cancellation or arbitrary choice
of signs is assumed. Dyadic summation of(1) pays the ENTIRE inverse
frequency certificate, including every zero and near minus incidence
and the plus-kernel inverse term, at

    JN sqrt(J) + J^2 D sqrt(N) log(2T)/T.                (2)

For actual nonempty high rectangles at the frozen level, Young's
inequality and the actual necessary size restrictions turn(2), including
arbitrarily small source losses, into

    delta J^2 v^2 D sqrt(N)
          + C_(delta,eta) T^(169/3500+eta) JN            (3)

for every fixed delta>0. The residual exponent169/3500 is below
208/2625 by exactly13/420. Thus this incidence part fits the required
budget. The packing and exponent lead in(1)--(3) was supplied by the
conductor during the task; it is independently derived below and is
not presented as an independent discovery.

The complete remaining modulus cost is still

    T^eta J^2 D^2 min(K, sqrt(K)(T sqrt(D))^(13/55)).     (4)

It contains both minus and plus terms. After the original Cauchy factor,
its coefficient is

    T^eta J^2 min(sqrt(N), T^(13/55)D^(34/55)).           (5)

Neither(1) nor actual alignment estimates the signed cancellation
needed to remove this cost. A necessary-condition-compatible scale
specified below leaves a fixed power deficit even with the cap in(5).
That is a limitation of this complete upper certificate, not a claim
that actual high points exist at that example scale or a refutation of
the actual signed target. The certified full moment remains
T^(10 beta+epsilon).

The exact radical-class algebra also shows why an automatic chi4
cancellation claim is false: within every exact anchor class the
character can be absorbed into a fixed sign on each anchor. Within a
reduced-ratio near-incidence family, its product is constant on all
active common multiples. Actual high-point signs are retained throughout;
no arbitrary rephasing is substituted for them.

## 2. Exact hypotheses and quantities

Use the full setup of the permitted216 anchored report. T>=2 is real,
Psi is the transform of the fixed nonnegative radial unit-mass mollifier,
and w is the original displaced nonnegative smooth radius window.
Put Z=T^(3/2), V0=T^(13/125), and let L be the total number of exact
dyadic rectangles, so L<<log^2(2T). For one rectangle,

    N<=Z,  D<=N,  K=N/D>=1,
    h(n)=(N/n)^(3/4)Psi(sqrt(n/T))
                          1_(N<=n<2N, n<=Z),
    H(R)=4N^(-3/4) sum_(D<=d<2D) chi4(d)
       sum_(k in[K/2,2K), k positive integer)
                h(dk)cos(2pi R sqrt(dk)-3pi/4).

Take a maximal N^(-1/2)-separated subset R_1,...,R_J of the ACTUAL
level set |H(R)|>v in[T/2,2T], where v>=V0/(2L), and set
sigma_j=sign H(R_j). Empty high sets have J=0 and need no argument.
The incidence estimates require only separation; the high-point
conditions are used later for the size restrictions and absorption.

Write c_(d,k)=chi4(d)h(dk) and

    Q=sum_k (sum_(j,d) sigma_j c_(d,k)
                    cos(2pi R_j sqrt(dk)-3pi/4))^2,
    Dcal=(J/2)sum_(d,k)c_(d,k)^2,      O=Q-Dcal.

The exact identity is

    Q=(1/2)sum_(j,l,d,e) sigma_j sigma_l sum_k c_(d,k)c_(e,k)
       [cos(2pi u^- sqrt(k))-sin(2pi u^+ sqrt(k))],
    u^-=R_j sqrt(d)-R_l sqrt(e),
    u^+=R_j sqrt(d)+R_l sqrt(e).                         (6)

In particular all plus sine terms, including their diagonal positions,
belong to O. The only removed terms are the constant minus terms
(j,d)=(l,e). Cauchy in k gives the actual aligned lower requirement

    J^2v^2 < 32 K N^(-3/2) Q.                           (7)

For reference define B0=J^2 v^2 D sqrt(N). The frozen target is

    O <= B0/64 + C_eta T^(208/2625+eta) JN.              (8)

No positivity of Psi away from zero is assumed. Exact formulas keep
its signs; absolute upper estimates use its boundedness and variation.

## 3. Proof, arithmetic interfaces and complete cost restoration

### A. Exact classes and what happens to chi4

Only odd d,e contribute. Thus an equality
R_j sqrt(d)=R_l sqrt(e) can occur only when (R_j/R_l)^2 is a positive
rational number whose numerator and denominator, in reduced form, are
both odd. This condition on pairs of anchors is an equivalence relation.
In each of its finite components choose a common r>0 and positive odd
integers b_j such that R_j=r sqrt(b_j). To construct them, express all
squared ratios to one anchor as odd rationals and multiply by their
common odd denominator. No bound on the height of b_j is presumed.

Within that component, equality of labels is exactly

    R_j sqrt(d)=R_l sqrt(e) iff b_j d=b_l e=q.

All active q are odd, and multiplicativity gives

    chi4(d)=chi4(q/b_j)=chi4(q)chi4(b_j).

Consequently the entire constant minus-frequency contribution is

    E0=(1/2)sum_(components) sum_k sum_(q odd)
       (sum_(j: b_j divides q, D<=q/b_j<2D)
           sigma_j chi4(b_j) h(qk/b_j))^2.               (9)

The actual top cutoff and cofactor support are already in h and the
outer k sum. Equation(9) is exact even when h changes sign. Terms
from different components cannot share an active exact label.
The usual Dcal is precisely the single-position square contribution
inside(9); E0-Dcal can have either sign.

Thus chi4(q) disappears from each class square. The residual anchor
sign is tau_j=sigma_j chi4(b_j), with sigma_j still the ACTUAL high-wave
sign. There is no oscillating character in a free common multiple left
to average within an exact class. This algebra is not a lower bound
for Q, since the other minus terms and every plus term remain.

For a fixed pair of anchors, write its reduced exact ratio as

    (R_l/R_j)^2=a/b,    (a,b)=1.

The corresponding exact divisor pairs are d=a t, e=b t. Their number
in the literal dyadic box is O(D/max(a,b)). If either a or b is even,
there are no active odd pairs. Otherwise t must be odd and

    chi4(d)chi4(e)=chi4(ab)                              (10)

on every active pair. The same identity holds for a near-incidence
family with this fixed reduced ratio d/e=a/b; nearness changes its
phase, not its character product. On a sufficiently small normalized
minus-frequency band the cosines themselves are positive, but their
remaining signs still include sigma_j sigma_l chi4(ab) and the actual
mollifier factors. No cancellation or coherent alignment of these
signs is inferred without proof.

### B. Exact and near multiplicative packing

Fix j and put X=T sqrt(N) and x_l=(R_l/R_j)^2. Since all radii lie
in[T/2,2T] and are N^(-1/2)-separated,

    |x_l-x_(l')| >= c/X for l!=l'.                       (11)

The near condition in(1) implies, using d,e~D,

    |d/e-x_l|
      =|u^-|(R_j sqrt(d)+R_l sqrt(e))/(R_j^2 e)
      <= C A/X.                                        (12)

Reduce d/e=a/b and group the fractions by dyadic height
H<=max(a,b)<2H, with H<=2D. They lie in a fixed bounded positive
ratio interval. Distinct fractions in that group are separated by
at least c/H^2, because their cross determinant is a nonzero integer.
Each has at most CD/H admissible multiples(d,e) in the box. Deleting
even or unsupported pairs only decreases the upper count.

Let M_H count pairs(l,a/b) satisfying(12) at this height. There are
O(H^2) such reduced fractions in total. By(11), each fraction can
belong to at most C(A+1) anchor intervals. Conversely, fraction
spacing implies at most C(1+A H^2/X) fractions for each anchor.
Therefore

    M_H <= C min((A+1)H^2, J(1+A H^2/X)).                (13)

Use min(u,v+z)<=min(u,v)+z, multiply by CD/H, and sum dyadic H:

    C_j(A) <= C D sum_H H^(-1)min((A+1)H^2,J)
                    + C J A D/X sum_H H
             <= C D sqrt(J(A+1)) + C J A D^2/X.

The first sum is split at H=sqrt(J/(A+1)); if that point lies outside
the available heights, the same upper bound remains valid. The second
sum is a geometric dyadic sum O(D), not O(D log D). This proves(1).
At A=0 it also proves C_j(0)<<D sqrt(J), including the literal
constant diagonal. All bounds hold for arbitrary real anchors with
the specified separation, so they certainly hold for actual high points.

In particular, |h|<=1 and at most2K cofactors give

    E0 <= C K sum_j C_j(0) <= C JN sqrt(J).              (14)

This estimate uses no sign or character cancellation and is valid for
the exact square form(9). It improves the old JD^2K count whenever
sqrt(J) is smaller than D. There is no assertion that(14) is saturated
by the actual aligned configuration.

### C. Entire inverse kernel, including plus terms

The accepted216 kernel calculation applies by Abel summation to the
actual joint weight h(dk)h(ek). Its support is an interval, possibly
empty; its smooth variation and endpoint jumps are uniformly bounded.
For nonzero u, with kappa=13/55, it gives

    |sum_k h(dk)h(ek)e(u sqrt(k))|
        <<_eta T^eta min(K, sqrt(K)(|u|^kappa+|u|^(-1))).
                                                               (15)

At u=0 use K. This is the already permitted square-root kernel with
the auxiliary radius bound C T sqrt(D); no character-weighted source
theorem is newly assumed. By min(K,a+b)<=min(K,a)+min(K,b), define
the inverse envelope

    W(u)=K min(1,1/(sqrt(K)|u|)),     W(0)=K.

Every minus argument has sqrt(K)|u^-|<=C X. Apply(1) to dyadic
bands A=1,2,4,...,O(X), with weights O(1/A). The sum over all j,l,d,e
of W(u^-) is at most

    C KJ sum_A A^(-1)
          [D sqrt(J(A+1))+J A D^2/X]
      <= C [JN sqrt(J)+J^2 D sqrt(N) log(2T)/T].         (16)

The first geometric series converges. The second has O(log T)
terms because N<=T^(3/2). Exact zeros and all arguments below
K^(-1/2) are included in its first band, never inserted into a
nonzero-frequency formula.

For plus arguments u^+~T sqrt(D), all are positive and large. Their
individual inverse envelope is O(sqrt(N)/(TD)). There are O(J^2D^2)
positions, so

    sum_(j,l,d,e) W(u^+) << J^2 D sqrt(N)/T.             (17)

The plus terms are thus paid for their inverse envelope; they are
not declared nonstationary or omitted. Combining(16)--(17) proves(2).

As a separate interpretation, the actual restriction |u^-|<=c/sqrt(K)
has kernel bounded by K and is already covered by(16), while the
remaining inverse-frequency envelope is also covered. The envelope
split is an upper-bound device, not an assertion that the exact
oscillatory kernel splits into two independently signed functions.

### D. Actual high-point conditions pay the incidence budget

The original count of O(N) divisor pairs and Schwartz decay give

    |H(R)| <= C_A N^(1/4)(1+N/T)^(-A).                   (18)

Since v>=T^(13/125)/(2L), nonempty actual high rectangles satisfy
N<=C_zeta T^(1+zeta) for every fixed zeta>0, after choosing a fixed
Schwartz order A depending on zeta. Indeed for N>=T^(1+zeta), the
right side of(18) is bounded by a constant times
T^((1+zeta)/4-A zeta), which falls below the high level for large A.
The bounded-T cases are covered by an enlarged constant. This step
uses the actual high condition and all its tails; it is not an
unproved effective-support truncation at exactly N=T.

The permitted one-variable estimate before Cauchy gives

    |H(R)| <<_eta T^(13/84+eta)N^(-29/168)D^(1/2).

For clarity, the cofactor exponent-pair cost is
(T sqrt(N))^(13/84)K^(1/2); multiplying by D N^(-3/4) gives precisely
this formula. Along with the trivial N^(1/4) ceiling it implies

    N >> v^4,
    D >>_eta T^(-13/42-eta)v^2N^(29/84).                (19)

Now Young's scalar inequality, with a=v^2D/sqrt(N), gives for any
fixed delta>0

    C JN sqrt(J)
       <=delta J^2v^2D sqrt(N)
                       +C_delta JN sqrt(N)/(Dv^2).      (20)

Using(19), (18), and v>=V0/(2L),

    sqrt(N)/(Dv^2)
       << T^(13/42+eta) N^(13/84) v^(-4)
       <<_eta T^(13/28-52/125+eta)
        = T^(169/3500+eta).                             (21)

Here zeta, the input exponent-pair loss, and logarithmic losses are
chosen small relative to the requested final eta. The second term
of(2), including its source losses, divided by B0 is
O(T^eta log(2T)/(T v^2)); this tends to zero by a fixed power on the
entire high-level range. It can be absorbed into any remaining fixed
delta fraction of B0. For bounded T the coefficient constant absorbs
it instead. Equations(20)--(21) prove(3) for the entire inverse
certificate, with the small losses in(15) accounted for.

Finally

    208/2625-169/3500=13/420>0.

The original diagonal Dcal<<JN is also within this error allowance.
Thus no exact-zero or inverse-frequency estimate at the old JD^2K
price is needed. This improvement does not pay the rest of(15).

### E. Every remaining term and the full failed closure

The positive-power part of(15), for either sign of u^-, and for all
u^+, has maximum argument O(T sqrt(D)). Counting every position
retains the cap and gives(4). Therefore a COMPLETE valid upper bound
from this mechanism is

    O <= delta B0 + C_(delta,eta) T^(169/3500+eta) JN
       + C_eta T^eta J^2D^2
                       min(K,sqrt(K)(T sqrt(D))^(13/55)). (22)

All original h signs, sigma signs, and character products were retained
in the exact identity before the indicated upper bounds. Equation(22)
includes every minus and plus term; it does not substitute a small
sector for the objective. With delta sufficiently small, (7) absorbs
its first term and gives

    J^2 v^2 <<_eta T^(169/3500+eta) J sqrt(N)/D
          + T^eta J^2 min(sqrt(N),T^(13/55)D^(34/55)).    (23)

This prices the whole attempted closure. The second term remains,
and it cannot be removed merely by the exact-class algebra(9), the
near-incidence packing(1), or the high-wave sign definition.

Here is a quantitative control of the AVAILABLE inequality, not a
construction of actual high points. Take dyadic N~T^(2/3), D~T^(2/15),
and v~T^(13/125), allowing the prescribed logarithmic shift if desired.
These choices obey N<=T^(1+o(1)), N>>v^4, and the necessary rectangle
bound in(19): its scalar ceiling has exponent67/630, exceeding13/125
by37/15750. Thus the restrictions proved here do not exclude them.
At these scales the second coefficient in(23) is

    min(T^(1/3),T^(263/825))=T^(263/825).

Relative to v^2 it is larger by

    T^(263/825-26/125)=T^(457/4125).

The cap is larger by T^(4/275), so retaining it does not repair this
example of the cost ledger. Absorption of this upper certificate
therefore does not follow uniformly from the present high-point
restrictions. Proving that the actual level set is empty there, or
that its signed remainder is smaller, would require a new estimate.
No existence or lower bound for that actual level set is asserted.

Without such an estimate, keep the accepted complete distribution
D_B(V)<<T^epsilon(V^(-2)+T V^(-136/13)) and the actual full ceiling
W<<T^(beta+epsilon). Exact layer cake gives the entire high tail

    H12(T) << T^epsilon
       [W^10+T W^(20/13)+V0^10+T V0^(20/13)]
            << T^(10 beta+epsilon).                    (24)

Both upper terms are retained; neither improves the29/25 target.
The complete low complement is already paid by accepted216. The
original n>Z Schwartz tail is O_A(T^(-A)), uniformly in R, and the
finite rectangle count is O(log^2 T); event inclusion at every level
therefore restores every rectangle and every mixed contribution as in
the permitted216 argument. No new unconditional full moment follows.

If the complete(8) were eventually proved, its known implication would
give full distribution T^(1+42rho/13+epsilon)V^(-168/13), and then
high twelfth exponent113/125+42rho/13. At rho=208/2625 this is29/25
and the restored discrepancy milestone is102/325. Those implications
are conditional; the present improvement to only the incidence part
does not establish their premise.

## 4. First doubtful or unproved step

The first missing estimate is the signed cancellation in the COMPLETE
remaining minus/plus aggregate beyond the paid inverse certificate.
Equation(22) is a complete upper bound, but its last term is too large
for the intended absorption. It is not promoted as a new open-sector
lemma, and it is not a lower bound on O or Q.

The character does not automatically oscillate along a common exact
label: (9) absorbs it into tau_j. Nor does it oscillate along the
active common multiples of a fixed reduced near ratio: (10) is
constant. Actual alignment gives sigma_j H(R_j)=|H(R_j)| and hence
(7); it does not by itself say that the tau_j balance inside any
particular label or near cluster. No stronger consequence of alignment
is proved here. In particular, choosing artificial tau_j all equal
would not refute the actual target, and no such counterexample is used.

The packet-counting and Young calculations are elementary claimed
lemmas requiring independent seam review before any accepted use.
Their correctness would still leave the stated complete arithmetic
input unproved.

## 5. Controls and outcomes

1. `actual_coefficients`: PASS locally. The exact chi4 product and real
   h coefficients appear in(6), (9), and(10). Upper bounds use the
   actual bounded variation and Schwartz decay, including sign changes.
2. `actual_aligned_high_points`: PASS. The signs are exactly sign H.
   Separation and nonemptiness are used where specified. Actual high
   size restrictions enter(18)--(21). No independently modulated array
   replaces a physical high-point configuration.
3. `exact_anchor_incidence`: PASS analytically, pending review. Odd
   rational-square components, their integer representatives, exact
   class squares, reduced-ratio multiplicities and C_j(0) are explicit.
4. `near_anchor_incidence`: PASS analytically, pending review. The
   physical width A/sqrt(K) becomes A/(T sqrt(N)) in squared ratios.
   Both anchor spacing and fraction spacing are retained in(13).
   Each common-multiple factor D/H and every dyadic height are priced.
5. `all_plus_minus_terms`: PASS for the complete ledger; TARGET OPEN.
   Equations(16)--(17) pay all inverse terms. Equations(22)--(23)
   retain the complete positive-power cost for both families, including
   the trivial cap. No plus sine term is dropped as a diagonal.
6. `every_rectangle_and_tail`: PASS. Literal half-open supports,
   bounded initial rectangles, partial top block, K>=1, integer
   endpoints and full Schwartz tails remain. N<=T^(1+zeta) is derived
   only for nonempty high rectangles, not imposed on the original sum.
7. `full_exponent_restoration`: PASS as diagnosis. The paid residual
   exponent is169/3500 with margin13/420 to the frozen budget. The
   unpaid full coefficient is(5); the certified moment remains(24).
   The conditional29/25 and102/325 claims retain their missing premise.
8. `arbitrary_sign_scope`: PASS. The incidence upper bounds actually
   hold for arbitrary signs, but no arbitrary-sign lower example is
   used to refute the actual high-point target. The scale control in
   Section3.E concerns compatibility of necessary conditions only.
9. `statement_only_control`: PENDING conductor's independent exact-class
   and application seams. This analyst read no isolated219 statement or
   sibling report. The conductor-supplied packing lead is disclosed and
   independently verified; it is not mislabeled as a blind discovery.
10. `unbounded_order_goal_scope`: PASS. No unbounded-fixed-order family,
    M1/M2/GAR parent, endpoint theorem or quarter bound is proved.
    Even the still-open fixed target supplies only102/325.

There were no numerical tests. The exact diagonal is a part of Q, not
a lower bound for it after the signed complements. No certificate lower
bound, random sign model, or artificial high set enters the argument.

## 6. Dependencies and exact artifacts used

The new task brief and its permitted context are:

- `protocol.md`.
- `state/proof_obligations.yml`, at the starting graph hash above.
- `state/active_campaign.yml`, frozen219 manifest.
- `strategy/round219_complete_anchored_energy_attack.md`.
- `strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
- `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md`.
- `rounds/codex-managed/gc-actual-radical-high-values/reports/anchored_divisor_high_values.md`.
- `rounds/codex-managed/gc-complete-signed-radical-kernel/synthesis.md`.
- This task's own219 generated brief.

Previously read protocol, graph and accepted kernels were retained from
the disclosed218 history; the graph hash is unchanged. No historical
reference named inside an allowed file was followed. No new external
theorem or web source was imported. The unweighted exponent-pair and
correlation interfaces are the already accepted ones in the supplied
kernel, with the same216 square-root specialization.

During the task, the conductor sent the candidate exact/near packing
and169/3500 exponent calculation. Sections3.B--D independently supply
its fraction-spacing proof, weight summation, plus-term completion,
actual high-support proof, and absorption constants. The exact character
class formula and the complete capped residual ledger are derived here.
That message is disclosed provenance, not unseen sibling evidence.

Only this assigned report was written. No state, proof draft, validation
matrix, synthesis, legacy file, sibling artifact or successor plan was
edited. No further delegation or mathematical experiment was performed.

## 7. Recommended state effect

Retain as bounded, reviewable method evidence; **no change** to accepted
moment, pointwise exponent or open full-proof parents. The exact and
near incidence envelope is better than the old separate counting bound
and fits its part of the available loss budget, but the complete signed
inequality(8) remains open because(4) is unpaid at the target size.

Do not promote a new residual sector merely for the reformulation in
(22), and do not interpret the constant character within a ratio family
as a counterexample to actual high-value cancellation. Preserve the full
anchored target and quarter objective. This task stops after this report
and designs no successor round.
