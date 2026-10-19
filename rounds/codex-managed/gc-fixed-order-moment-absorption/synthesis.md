# Round233: complete fixed-order absorption reduction

Campaign `gc-fixed-order-moment-absorption`; conductor synthesis2026-10-12 Asia/Shanghai. Terminal decision `fixed_order_absorption_reduction_reviewed`. Accept only the narrow reduction described below through its reviewed State Patch. No complete moment or pointwise exponent improves.

## 1. Result

The repeated-squarefree-class terms can be absorbed into the unknown moment at every fixed even order. This removes the earlier dependence on the baseline pointwise exponent for paying those terms and supplies the all-fixed-order bridge that the strategy review had left unproved.

For a real summable class family, write Z=sum f_d, V=sum f_d^2 and E_p for the ordered sum over pairwise distinct p-tuples. For each fixed even p>=2 and 0<delta<1,

    |Z^p-E_p|<=delta|Z|^p+C_(p,delta)V^(p/2),
    C_(p,delta)=(p!-1)max(1,((p!-1)/delta)^((p-2)/2)).

For the actual complete circle-wave classes above cutoff Q,

    J_(p,Q):=int w V_Q^(p/2)<<T Q^(-p/4+epsilon),
    (1-delta)M_p(Z_Q)<=I_(p,Q)+C_(p,delta)J_(p,Q).

The signed integral I_(p,Q)=int w E_(p,Q) need not be positive. Its negative part is paid by the same J budget; no positivity shortcut is used.

At Q=1, the full small-class head and J both cost O_p(T). Consequently, for every fixed even p and b>=1, the complete bound M_p(B_T)<<T^(b+epsilon) is equivalent to a one-sided upper bound on the actual signed I_(p,1) at that power. An unbounded sequence of fixed orders with signed exponents b_p=o(p) would therefore suffice for the quarter theorem. **Those signed bounds remain unproved.**

## 2. Proof mechanism and exact application

The finite cycle-partition identity expresses E_p in power sums P_h. The identity permutation supplies Z^p; every other permutation has at most p-2 fixed points. Bounding |P_h| by V^(h/2), h>=2, leaves a polynomial in t=|Z|/sqrt(V) of degree at most p-2, with total absolute coefficient p!-1. Above t=sqrt((p!-1)/delta) it is paid by delta t^p; below that threshold it is paid by the explicit constant. This proof is uniform in the number of classes. It requires no arithmetic cancellation.

The actual wave is the full smoothed real cosine series

    B_T(R)=sum_n r2(n)n^(-3/4)Psi(sqrt(n/T))
                         cos(2pi R sqrt(n)-3pi/4),
    f_d(R)=sum_(s>=1)a_(d s^2)(T)
                         cos(2pi R s sqrt(d)-3pi/4).

The fixed mollifier/window and all exact definitions are in the reviewed kernel. Every harmonic is retained, including all squares in d=1. The amplitude bound A_d<<r2(d)d^(-3/4) gives the uniform square-sum tail sum_(d>Q)A_d^2<<Q^(-1/2+epsilon), while the elementary positive r2 mass bound gives ||L_Q||infinity<<Q^(1/4). Separate fixed-T Schwartz l1 convergence justifies the infinite identities and integration. It is not used as an asymptotic power estimate.

The norm inequalities for B=L+Z and Z=B-L pay all head/tail mixed terms. This is a relative reduction and target equivalence; it does not replace Round216's stronger additive twelfth-order error statement. The old theorem and all its qualifications remain unchanged.

## 3. Cutoff and sharp-restoration budgets

| Cutoff | Complete head | Absorption budget J | Sufficient common exponent floor |
|---|---|---|---|
| Q=1 | O_p(T) | O_p(T) | 1 |
| Q=floor(T^(1/p)), elementary estimate | O_p(T^(5/4)) | O_(p,epsilon)(T^(3/4+epsilon)) | 5/4 |
| Same growing cutoff, accepted distribution refinement | O_(p,epsilon)(T^(h_p+epsilon)) | Same | h_p=1+(p-136/13)_+/(4p) |

The refined head calculation is explicitly restricted to1<=Q<=T, which includes both intended cutoffs. At p12, h_p=161/156. The core relative bound and elementary head/square-sum bounds remain uniform for all real Q>=1. All floors and bounded-T cases are retained.

For a complete normalized exponent b>=1, restoring sqrt(R)/pi, dx=2R dR and the full smoothing error gives the sharp moment exponent

    a_p=max(1+p/4,(1+p/2+b)/2).

One-sided persistence of the inclusive counting function gives pointwise exponent

    a_p/(p+1)=1/4+(1+2b)/(4(p+1)).

Both signs and real endpoints are covered. The conditional quarter implication selects a sufficiently large fixed p after the desired final epsilon, then lets T vary. It does not use p=p(T) or constants uniform in p. For the growing cutoff, taking the maximum with its paid head floor preserves the condition b_p=o(p).

## 4. First remaining arithmetic gap and controls

The signed distinct-class integral still contains all cross-class, harmonic and cosine-sign correlations at physical frequency resolution1/T. Distinct radicals exclude exact zero frequencies but do not provide a useful quantitative separation estimate. The algebraic absorption supplies no upper bound on this aggregate.

The previously accepted `GC-distinct-radical-absolute-certificate-obstruction` also applies to the proposed cutoffs for each fixed even p>=4: its termwise absolute Fourier certificate has a positive subcollection of size at least c_p T^(p/4-1/2). This inherited statement is not a lower bound for signed I or a physical moment. It requires keeping signed aggregate cancellation in any successor; the new reduction does not invalidate that barrier.

Finite controls include fewer than p classes, vanishing entries, positive aligned families, opposite signs and growing |Z|/sqrt(V). For p6 with three1 entries and three-1 entries, E6=-720, disproving universal positivity. Families of p-1 equal entries force constants to grow with p, so a growing-order inference is unsupported. Positive families show that I cannot be bounded by J alone from the finite hypotheses.

Wolfram checked exact Newton/derangement coefficients at even orders2 through16. An independent local integer/rational implementation reproduced the coefficients, monomial counts, negative control and rational exponent, and passed64 finite-family cases. These are diagnostic checks, not the proof for arbitrary p or an asymptotic theorem. Code, returned output, parameters and limits are in `controls/control_manifest.md` and its linked local artifacts.

## 5. Independent reviews and localized repair

Three initial reports were frozen before the nonauthor review cycle. The statement-only task had no access to the actual application, graph, history or conductor derivation. Its initial isolation is preserved separately from the explicitly expanded review assignment.

- `reports/blind_partition_absorption.md`: independent finite/summable proof, reviewed by the conductor.
- `reviews/independent_finite_absorption_review.md` and `reviews/finite_absorption_final_hash_supplement.md`: nonauthor finite/integral and fixed-order verification binding the repaired candidate.
- `reviews/independent_actual_kernel_review.md`: actual coefficients, square sum, harmonics, head, floors, complete-wave and sharp-restoration review; pass.
- `reviews/independent_scope_restoration_review.md`: independent hostile line audit of the candidate and actual report, including signs, dependencies and complete scope; pass.

Two arithmetic reviewers independently requested the same literal restriction before optional formula(A13). The p2 logarithm is directly absorbed into T^epsilon on1<=Q<=T; that range is now explicit. No core statement or intended cutoff conclusion changed. The original candidate is archived; the repaired hash is `b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0`. Final reviews bind this hash, and the finite supplement verifies that its certified sections are unchanged. The line-ending conversion is separately disclosed in the repair record.

No new external theorem was imported. The elementary core does not use the baseline beta ceiling; the optional distribution and sharp reconstruction retain the accepted204/216 dependencies and their existing source qualifications. Wolfram's semantic suggestions are not proof dependencies.

## 6. State Patch and validation

Create only `GC-complete-fixed-even-moment-distinct-absorption`, with status `proved_internal` for the reduction and conditional implication. Its accepted kernel is the exact reviewed candidate copied to `proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md`. All401 preexisting nodes remain unchanged; the resulting graph has402 nodes. Append the new reduction to the proof draft only after the graph patch passes and is applied.

The patch does not mark any actual signed estimate as proved, change complete moment or pointwise powers, close M1/M2/GAR/endpoints, or prove the quarter theorem. It preserves the historical twelfth-order additive reduction. Validation includes the accepted dependency cone, final-hash review bindings, frozen initial reports, inverse/replay, prior ledger/matrix preservation and protected-file hashes. The mechanical outcome is recorded in `controls/closure_validation.json`; the State Patch and final artifact manifest are part of this campaign.

## 7. Strategy decision and round boundary

The all-fixed-order reduction is now available as a distinct complete proof interface. This is a structural result; the next advance still needs an actual signed arithmetic estimate. A successor must choose a concrete aggregate cancellation mechanism with a quantified complete implication and test it against the retained absolute-certificate controls. It should not repeat the partition identity, transfer calculation or local product-cutoff mechanism as a new estimate.

The two earlier upper-tail attempts remain completed and their reassessment remains in force. This round does not reset their count. Target A and all stronger milestones remain open. Round233 closes after this single bounded derivation/review cycle. Round234 is pending design, has no tasks and is not automatically launched.
