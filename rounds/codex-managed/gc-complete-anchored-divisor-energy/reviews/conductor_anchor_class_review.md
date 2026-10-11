# Round219 conductor review of the isolated exact-anchor report

## 1. Result

GREEN for exact identities and their limited application. Reviewed file:
reports/blind_anchor_classes.md, SHA256
83e2f43ad76fe404379d79d308ce3da2b5653151218fdffad458630297150512.
No promotion of the actual energy target follows.

## 2. Exact hypotheses

Use positive real anchors, finitely many integer labels, and arbitrary
real coefficients, exactly as in the isolated packet. Anchor classes
use rational squared ratios. Do not identify this exact-frequency
energy with the finite cofactor energy Q in the application.

## 3. Independent algebra and actual binding

Squaring an equality R_j sqrt(d)=R_l sqrt(e) proves the rational
squared-ratio condition. Clearing all denominators in one class gives
integer q_j; dividing their joint gcd gives the unique primitive
representation. A second primitive representation differs by a positive
rational scalar whose denominator divides all q_j and whose numerator
divides the new joint gcd, so the scalar is one.

Labels ell=q_j d classify every collision once. The equation q_j d=q_l e
has d=(q_l/g)t,e=(q_j/g)t with g=gcd(q_j,q_l). The character product
is chi4((q_j/g)(q_l/g)) times the odd-t indicator. This verifies ordered
cross-term multiplicity and the exact diagonal. For q_j=2^v_j u_j,
nonzero coefficients at ell=2^v m require v=v_j. Within this stratum,
chi4(m/u_j)=chi4(m)chi4(u_j); the common factor disappears on squaring.

For the actual rectangle, apply the identity for each fixed cofactor k
with b_j=sigma_j and h_(j,d)=h(N,T;dk). The constant minus-frequency
contribution is one half the sum over k of the report's E. Its original
diagonal is one half J sum_(d,k) c(d,k)^2. The remaining minus terms
and every plus sine term can have either sign. Therefore the exact
energy gives neither a lower bound for Q nor a counterexample to(12).
The abstract control uses freely selected sparse h and b, which the
physical rectangle/high-value alignment does not supply. It only
disproves automatic character cancellation in that enlarged class.

## 4. First unproved step

The full actual signed energy estimate at rho208/2625 remains open.
No balance of sigma_j chi4(q_j) inside the common labels is known from
the condition sigma_j=sign H(R_j). The report correctly requests such
an additional weighted hypothesis instead of assuming it.

## 5. Controls and outcomes

The positive odd-square construction has one common frequency and
coefficient sum J, hence energy J^2 and diagonal J. The irrational
squared-ratio example has no cross frequency. The q=(1,2,10) example
correctly retains the two even-anchor contributions with odd quotients;
using chi4(q_j) directly there would incorrectly kill them. The q=(1,3)
balanced example has energy zero, disproving any general diagonal
lower bound. All controls are finite algebra, with no experiments.

## 6. Dependencies and provenance

The frozen report above and its isolated statement
briefs/blind_anchor_statement.md, SHA256
2182389e0e5d8a8a3630b3ef0b88d016061c68aaa9e7fc7f7e999a32c0de1187;
the exact real expansion in the closed216 anchored report, equations8--10.
The conductor is the application reviewer. The isolated agent's prior
history is explicitly disclosed; it is not a fresh history-free agent.

## 7. Recommended state effect

Retain as checked evidence with no graph change. The algebra is sound;
it does not close any actual analytic parent or improve the exponent.
