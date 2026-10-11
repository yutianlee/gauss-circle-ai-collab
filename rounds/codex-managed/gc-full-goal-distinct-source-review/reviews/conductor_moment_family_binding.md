# Round217 actual binding of the isolated moment-family derivation

## 1. Result

Conductor NONBLIND review, 2026-09-28, campaign
gc-full-goal-distinct-source-review, starting graph
f7c8b74e9acaa3bf5234c3678f20e2aaf8dbb9ba6179f73d839fa2f0537a14d7.
GREEN for conditional transfer, not for any signed-integral grant.
Claimant:reports/blind_moment_family.md, SHA256
fe681f61a48faac2825138c8b7e0884e4f73c05b6cca789cb0f72b9f33e49e35.
Its Young absorption is stronger than its restricted nonabsorbing
certificate and gives a precise sufficient full-quarter family.

## 2. Exact hypotheses and actual identification

Use exactly the actual B_T, f_d, L_Q, Z_Q, mollifier and window of
the accepted216 kernel, now at a fixed even p>=4 and fixed cutoff
exponent 0<=alpha<=4beta. The complete harmonics converge absolutely
for each T. The primewise divisor inequality and elementary disk count
give |L_Q|<=C Q^(1/4) and sum_(d>Q) A_d^h<=C_(h,eta)Q^(1-3h/4+eta).
The arbitrary-coefficient proof of accepted204 applies to each masked
series; the physical B_T ceiling plus the head bound gives the ceiling
for Z_Q. This is the same actual binding checked in the216 ledger.
No random independence is an input. All orders and cutoffs are fixed
before T tends to infinity; constants may depend on them.

## 3. Independent derivation and restored powers

For the ordered distinct sum E_p, the exponential generating function
product_d(1+t f_d) gives the exact partition formula. A nontrivial
partition has r singleton factors and n=p-r>=2 other positions.
Its non-singleton product is bounded by C Q^(-n/4+eta n), since
each power sum of order h>=2 is bounded by Q^(-h/4+eta h).
Writing u=Q^(-1/4+eta), each error is C u^(p-r)|Z|^r.
The finitely many Young inequalities with total coefficient1/2 yield

    |Z^p-E_p| <= |Z|^p/2 + C_(p,eta) Q^(-p/4+eta p),
    M_p(Z) <= 2 I_p + C_(p,eta) T Q^(-p/4+eta p).

Terms with r=0 cost the constant term directly. The moment is finite
before absorption, so there is no integrability bootstrap. The one-sided
I_p is retained; E_p is allowed to be negative. This derivation uses
no inherited lower moment after the actual amplitude binding.

In particular, along any unbounded sequence of fixed even p, set
Q_p=floor(T^(1/p)). If the additional estimate

    I_p(T,Q_p) <= C_(p,epsilon) T^(5/4+epsilon)

holds for every such chosen p, then M_p(Z)<=T^(5/4+epsilon).
The actual head trivially satisfies M_p(L)<=C_p T Q_p^(p/4)
<=C_p T^(5/4). Thus M_p(B)<=T^(5/4+epsilon), and the accepted
physical restoration gives

    Theta(p)=1/4+7/[8(p+1)] -> 1/4.

Choose a fixed p large enough for each desired final loss, then choose
the moment epsilon small enough. No constants uniform in p and no
growing p(T) are needed. Intermediate-order grants are unnecessary.
The source report's every-even-order induction is valid but stronger
in its assumed availability than this same-order proof requires.

At the current p=12, alpha=2/5, the head is paid by accepted216 at
15/13 and the target remains I12<=T^(29/25+epsilon), not T^(5/4).
That single bound would give102/325. It supplies neither the displayed
family nor an extrapolation to another p or cutoff.

For completeness, the isolated report's restricted insertion gives
C_p=max(1,beta(p-4))-alpha/2. Its head has all three costs
max(1,alpha(p-2)/4,1+alpha(p-q)/4). The one-pair partition dominates
the other inherited correction exponents. Its optimization is expressly
confined to this nonabsorbing procedure; the p16 optimum and limiting
Li--Yang power do not impose a barrier on the stronger absorption.

## 4. First doubtful or unproved step

The first unproved step is a signed I_p upper bound at any useful new
pair, including the complete I12 target. The family above is a rigorously
sufficient set of new hypotheses, not an accepted asymptotic estimate.
Nothing here proves a complete M1/M2/GAR parent or changes a pointwise
exponent. The present binding may be retained as reviewed strategy
evidence; no separate graph promotion is requested in this round.

## 5. Controls and outcomes

GREEN for ordered multiplicities, all repeated-class partitions, odd
singleton powers, finite versus infinite identity, signs, floors including
Q=1, finite prior integrability, all harmonic tails, real window endpoints,
and fixed-order constants. The actual head cost remains explicit. The
positive certificate obstruction concerns a sum of Fourier moduli and
does not contradict this signed conditional transfer. No experiment.

## 6. Dependencies and artifacts

protocol.md; the frozen isolated packet and report; accepted
proofs/kernels/gc_complete_distinct_radical_moment_reduction.md,
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md;
closed216 actual binding/ledger; reports/full_frontier_sources.md at
3fcd969a5fb4b53edb6cbbd337b19ae18c363fb44bc1cdc0042a80f05c1fd338.
The isolated author had no access to this arithmetic origin during the
original derivation. This later conductor application is explicitly NONBLIND.

## 7. Recommended state effect

Retain the conditional family and revise strategy away from treating the
nonabsorbing p16 optimum as a universal limitation. Keep the actual
signed grants and quarter theorem open. Accept only the separately
reviewed distinct-class absolute-certificate obstruction in the round's
graph patch if all of its remaining gates pass.
