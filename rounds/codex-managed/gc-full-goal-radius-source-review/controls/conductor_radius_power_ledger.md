# Round214 conductor ledger: optimized complete radius certificate

## 1. Result

Campaign: gc-full-goal-radius-source-review. Date: 2026-09-28.
Role: conductor derivation, NONBLIND. Graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

Under the isolated packet's hypothetical arithmetic input, the fully paid
radius certificate has optimal uniform block exponent 1/8, even with free
differencing lengths and both elementary complementary caps. The physical
discrepancy consequence would be X^(5/16+epsilon), not the quarter theorem.
This is an exact limit of the displayed certificate and caps, not an actual
lower bound for the arithmetic sum. The radius input itself is still open.

For the specified target-power lengths, a formal input with first term
sqrt(N)q^(-sigma), 0<=sigma<=1, instead requires
b >= (1-sigma)/(8-6sigma). Approaching the quarter target in this family
therefore requires sigma approaching 1. No such arithmetic bound is proved
or assumed applicable beyond the lengths stated in its hypothetical input.

The conductor derived these powers independently from the packet before
receiving the blind analyst's matching interim conclusions. This artifact
is nevertheless NONBLIND, and requires an independent final-hash review.

## 2. Exact statement and hypotheses

Use exactly the round214 isolated packet, with 1<=N<=T, T>=2,
2<=L<=K<=cN, U=N^(3/2)/T and D=LK/U. Constants are independent of
T,N and lengths in their stated input range. Harmless fixed constants,
logarithms, roundings and arbitrary epsilon losses are suppressed below.
For D>1, the resulting positive fourth-power certificate is

    E(N,L,K) = N/L^2 + N/K + N/D + sqrt(ND).                 (1)

The corresponding available block bound is the minimum of E^(1/4),
N^(1/4) and (T/N)^(1/2); for D<=1 only the caps are used. The assertion
of an optimum concerns this explicit expression. It is not a converse
to an upper bound, nor a lower bound forced on any actual F.

Conditional on the radius input throughout the middle range of lengths
used below, that minimum is <=T^(1/8+epsilon) uniformly in N. At
N comparable to T^(3/4), every admissible positive certificate (1) is
>= a constant times T^(1/2), and both caps are >= a constant times
T^(1/8). Thus no exponent smaller than 1/8 is supplied uniformly by
this expression and these caps alone.

## 3. Derivation

### A. Sum all shells and tails

The paid radius term in the packet gives sqrt(N)sqrt(q)+N/q on shell q.
The fractions satisfy delta_q <= min(1,Cq log(2L)/D) and sum delta_q<=1.
Consequently sum delta_q sqrt(q)<=sqrt(D), while
sum delta_q/q <=C log(2L)log(2D)/D. For fixed B>1, the tail
sum delta_q Nq^(-B)<=C_B N log(2L)/D. Adding safe shifts and the
model term gives (1), with only the allowed epsilon factors. All shell
counts and the paid bandwidth sqrt(q) are essential parts of this sum.

### B. Uniform attainment and rounding

Use the first cap for N<=T^(1/2) and the second for N>=T^(3/4).
In between, choose

    L=max(2,ceil(sqrt(N)T^(-1/4))),
    K=max(2,ceil(NT^(-1/2))).

These are comparable to the displayed real lengths and obey L<=K,
and K<=cN for all sufficiently large T. Small T and bounded N are
absorbed in constants. Then D is comparable to T^(1/4), both diagonal
terms are O(T^(1/2)), N/D<=T^(1/2), and sqrt(ND)<=T^(1/2).
The shell estimate therefore proves the asserted conditional bound.
In particular, applying a result known only at b=83/650 would not
justify this step at b=1/8: the broader arithmetic hypothesis is explicit.

### C. A certificate lower bound at the exact limiting scale

If E is the sum in (1), its first two summands imply
L>=sqrt(N/E), K>=N/E. Hence

    D=TLK/N^(3/2) >= T E^(-3/2).

The last summand implies E>=sqrt(ND), whence
E^(7/4)>=sqrt(NT), or

    E >= (NT)^(2/7).                                      (2)

At N=T^(3/4), interpreted up to integer rounding, this is T^(1/2).
The first cap there is T^(3/16), the second is T^(1/8).
If D<=1 and no radius certificate is invoked, their minimum remains
T^(1/8). This proves precisely the expression-level obstruction.

For a further algebraic check let S=LK and balance K=L^2. The diagonal
terms become N/S^(2/3), the radius term is T^(1/2)N^(-1/4)S^(1/2),
and the smooth contribution is N^(5/2)/(TS). Balancing the first two
gives S=N^(15/14)T^(-3/7), E=(NT)^(2/7). The smooth contribution
is N^(10/7)T^(-4/7), no larger precisely for N<=T^(3/4).
These lengths grow once N>T^(2/5). With caps and integer adjustments,
the supplied power envelope for N=T^alpha is

    alpha/4                 for 0<=alpha<=2/5,
    (alpha+1)/14            for 2/5<=alpha<=3/4,
    (1-alpha)/2             for 3/4<=alpha<=1.

Inequality (2), and comparison with both caps, also proves that the
displayed envelope cannot be reduced using (1) at fixed alpha. The
middle expression is attained by the lengths just computed; the caps
attain the other intervals. Fixed endpoints follow by constants and
epsilon losses rather than an assumption of strict power separation.

### D. Formal frequency decay at the target-power lengths

For fixed 0<b<1/6, take L comparable to sqrt(N)T^(-2b) and K comparable
to NT^(-4b), with max(2,ceil(...)), on T^(4b)<N<T^(1-2b).
Then D is comparable to T^(1-6b), including near the lower endpoint.
Put r=1/2-sigma. Since -1/2<=r<=1/2, geometric dyadic summation gives

    sum delta_q q^r <= C log(2L) D^r.                     (3)

For negative r this follows from delta_q<=Cq log(2L)/D and r+1>=1/2;
using only sum delta_q<=1 would wrongly discard the frequency gain.
The complete new first radius cost is therefore sqrt(N)D^(1/2-sigma).
At the upper edge of the band its exponent is

    1-sigma-4b+6b sigma.

All remaining costs are <=T^(4b+epsilon): the two diagonals by design,
and N/D at N<=T^(1-2b). Thus the precise power test for this displayed
upper certificate to be <=T^(4b+epsilon) uniformly is

    1-sigma <= b(8-6sigma).                              (4)

If the strict opposite holds, choose a fixed alpha sufficiently near
1-2b inside the band: the displayed first term has a positive power
deficit. Again this is a failure of this certificate, not an actual
lower bound, nor a claim that all admissible shell families saturate (3).
For sigma=0,1/2,1, (4) gives b>=1/8,1/10,0 respectively. The last is
only a formal limiting requirement; feasibility of its arithmetic input
and validity as b varies are separate unsolved mathematical questions.

### E. Reconstruction and full-goal meaning

If the complete physical reconstruction supplies T^(1/2) times
logarithmically many blocks, plus target-safe complementary errors,
block exponent b yields squared-radius exponent 1/4+b/2 because X=T^2.
Thus b=1/8 gives 5/16. Neither a proof of the current radius gate nor
an optimized fixed-b milestone alone closes the full quarter goal.
The original whole-discrepancy high-moment family and complete M1/M2
parents remain alternatives; no identity between their missing estimates
and the unproved stronger frequency input is asserted.

## 4. First doubtful or unproved step

The arithmetic radius estimate is unproved, already for sigma=0 at the
original b=83/650. Optimization and transfer are conditional algebra.
Extending that input to b=1/8 or to sigma>0 needs a new proof with its
actual r2 coefficients and specified growing shifts. This ledger supplies
no new upper estimate on actual signed radius energy, moment or discrepancy.

## 5. Required controls and outcomes

- Complete shell fractions and tails: paid in A; no omitted overlap cost.
- Exact limiting scale: N=T^(3/4) yields the lower bound (2) for E only.
- Rounding and complementary ranges: B covers the full 1<=N<=T range.
- Negative shell exponent: (3) uses density and avoids the wrong sigma cap.
- Normalization: physical T^(1/2), X=T^2 gives 5/16, not 1/8 or 1/4.
- Input scope: b and sigma generalizations are explicitly hypothetical.
- Actual signed versus positive certificate: no converse claim anywhere.
- Zero mathematical numerical experiments; all comparisons are algebraic.

## 6. Dependencies and exact artifacts

- protocol.md, state/proof_obligations.yml and active round214 manifest.
- strategy/round214_full_goal_source_review.md and the pinned September23 memo.
- rounds/codex-managed/gc-full-goal-radius-source-review/briefs/blind_radius_optimization_statement.md.
- Closed213 reports/centered_shell_dispersion.md for the original conditional
  bandwidth transfer and arithmetic gate; no broader arithmetic theorem.
- Closed211 controls/conductor_two_stage_strategy.md and closed208 complete
  reconstruction as context only for the physical interpretation.

No external theorem is newly imported. The important optimization was
also assigned independently to a statement-only analyst; this ledger is
not that analyst's isolated report.

## 7. Recommended state effect

Retain accepted graph and draft unchanged. Record the reviewed certificate
limit in strategy evidence. The next research objective must identify a
complete estimate with quantitatively greater reach; another centering or
positive-kernel reformulation does not address the missing cancellation.
