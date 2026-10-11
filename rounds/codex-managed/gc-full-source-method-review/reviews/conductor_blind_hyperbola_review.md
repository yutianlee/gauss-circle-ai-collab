# Round211 conductor review of the isolated hyperbola transfer

Campaign: gc-full-source-method-review. Date: 2026-09-28.
Role: conductor line and implication review, not a second blind derivation.
Graph SHA256: 4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

## 1. Result

GREEN for the conditional transfer and its scope. The original report was
completed with only protocol and the isolated packet, before its author
received any nonblind two-stage review assignment. Its source input,
complements and reconstruction remain explicit hypotheses in that report.
Nothing here establishes a new admissible pair or a better exponent.

## 2. Exact statement and hypotheses

For real T>=2, 1<=N<=T and R in a fixed positive compact multiple of T,
the packet's partial-interval square-root bound with pair (kappa,lambda)
implies F_N<<T^(kappa+epsilon)N^(lambda/2-1/4). The source must permit the
two residue-four restrictions and fixed phase rescalings. With the separate
supplied caps and full reconstruction, the wave exponent is

    delta=min(1/6,(4kappa+2lambda-1)/(4lambda+2)),

and the squared-radius exponent is 1/4+delta/2. For 0<b<1/6, delta<b
is equivalent to 4kappa+2(1-2b)lambda<1+2b.

## 3. Proof and independent checks

Partition all positive divisor pairs by d<=D or d>=D+1. The second arm
then has m<=floor(4N/(D+1)), exactly; the real support endpoints give the
displayed ceilings and floors without overlap. With s=lambda-kappa,
A=R sqrt(N) and K=N/u, partial summation costs N^-3/4 times a uniformly
bounded variation. Smoothness of Psi at zero supplies that uniformity.
Splitting the second inner character into d=4j+1 and 4j+3 changes K to K/4
and uses precisely the stipulated fixed shift, not an arbitrary weight.
K<4 is bounded length. For sufficiently large T, A>=N>=K; bounded T is
paid before this source call. Thus both outer sums give the full expression

    N^-3/4 [A^kappa N^s(H_s(D)+H_s(M_D))
                      +(N/A)(H_1(D)+H_1(M_D))].

At q=floor(2sqrt(N)), floor(4N/(q+1)) is q-1 or q, since
q^2<=4N<(q+1)^2. The leading power is
N^-3/4 R^kappa N^(kappa/2+s+(1-s)/2)
=R^kappa N^(lambda/2-1/4). The other term is
R^-1 N^-1/4 log(2N). Bounded inner lengths total at most N^-1/4.
For s=1 only a logarithm replaces the power. These costs are absorbed in
the main expression because kappa>=0 and lambda>=1/2.

For any D, one of D or M_D is at least a fixed multiple of sqrt(N), so
balancing is optimal at the level of this positive cost. This says nothing
about a lower bound on the signed F_N. The scalar envelope
min(alpha/4,(1-alpha)/2,kappa+alpha(lambda/2-1/4)) has the displayed
maximum delta: either its original apex alpha=2/3 remains, or the
nondecreasing third line meets the descending second line to its right.
Restoring sqrt(R), the singleton and complete tail gives the claimed
squared-radius exponent. A family tending to (0,1/2) gives quarter with
epsilon by fixing its member after epsilon is specified; constants need
not be uniform across that family. A fixed nonendpoint pair does not.

The actual real-block-to-complex comparison needed outside the isolated
packet is supplied separately by the smooth positive-frequency projection
in the conductor two-stage ledger. It is not presumed proved by this
blind report. The packet correctly labels the entire reconstruction as
an input, including its complete tail.

## 4. First doubtful or unproved step

The first arithmetic assertion remains the uniform exponential-sum input
for an improving pair. This review proves no pair approaching (0,1/2).
The source reports separately price the available pairs and bilinear
theorems. The source and complementary hypotheses cannot be promoted just
because their implication passes this review.

## 5. Required controls and outcomes

Both divisor arms, actual character, real endpoints, bounded scales,
amplitude derivatives, source range, residual term, logarithmic endpoint,
cutoff optimization and complete exponent conversion pass. The argument
also permits an unsigned divisor analogue under the same scalar input;
it makes no character-cancellation claim. The adversarial coefficient
which removes the phase is correctly excluded from the scalar input.
No numerical experiment was needed or run for this review.

## 6. Dependencies and exact artifacts

Reviewed claimant:
rounds/codex-managed/gc-full-source-method-review/reports/blind_hyperbola_transfer.md
SHA256 2e004517f358e5eebf0e1c9da5cea6fdeb18c787c12a7d70b94facfb8a73674a.
Other dependencies: protocol.md; the same campaign's
briefs/blind_hyperbola_statement.md; its frozen plan and strategy; and
controls/conductor_two_stage_strategy.md only for the separate actual
complex-block seam, not as evidence the blind author saw it. No external
theorem is imported in this conductor review.

## 7. Recommended state effect

Retain as reviewed statement-only conditional strategy evidence. No graph
mutation, new exponent, parent closure or quarter claim. The original
blind report remains unchanged after the author's separate nonblind work.
