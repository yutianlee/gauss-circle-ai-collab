# Independent review of the finite absorption and integral seam

- Campaign: `gc-fixed-order-moment-absorption`; round 233.
- Role: nonauthor reviewer, following a frozen statement-only independent derivation.
- Review start UTC: `2026-10-12T00:13:38.5098978Z`.
- Exact claimant artifact: `rounds/codex-managed/gc-fixed-order-moment-absorption/candidates/conductor_fixed_order_kernel.md`.
- Exact claimant SHA-256 verified before review: `6e2be69a41d2bee8b8391e154a01e2f7468291314668c4363a93cc4b126b2caf`.
- Prior blind report remains frozen at SHA-256 `71e5827c677fb0975eb763f667cf1472ac4e28d71ded17293578cd0eb8b75f23` and was not modified.
- Graph hash supplied as provenance, not inspected: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
- Scope: Sections 1-2, finite/integral logic, limiting hypotheses, and fixed-order quantifiers. Application-specific estimates elsewhere in the claimant are treated only as hypotheses. No historical kernel, sibling, graph, or shared state was read.
- Verdict: PASS for the finite/summable relative absorption and signed integral seam; conditional PASS for the stated budget equivalences and fixed-order quantifier logic. This is not an independent certification of the actual arithmetic, distribution, or reconstruction inputs.

## 1. Result: verified lemma and conditional implications

The claimant's partition identity (A6), remainder bound (A7), and constructive constant (A8) are correct. They agree with the earlier isolated derivation, which preceded access to this claimant artifact. In particular, with A = p!-1,

    C_(p,delta) = A max(1,(A/delta)^((p-2)/2))

is valid independently of the family size and values. The p = 2 and V = 0 cases are correctly covered.

For fixed even p and 0 < delta < 1, the integral conclusions (A1)-(A3) follow under the claimant's absolute summability, measurability and integrability conditions. The negative part is controlled pointwise; therefore finite moment existence is a conclusion, rather than a circular prerequisite, when a finite one-sided upper bound on the signed integral and a finite J are supplied.

The equivalence between paid-budget bounds for B_T, Z_Q, |I_(p,Q)| and the one-sided upper bound for I_(p,Q) is valid assuming the stated head and J estimates. The unbounded sequence of fixed orders is logically different from substituting p = p(T); the candidate explicitly uses the correct quantifiers.

## 2. Exact reviewed statement and hypotheses

The independently certified finite kernel is this: for every integer p >= 2, every delta > 0, and every finite or absolutely summable real family (x_i), with Z, V and the ordered distinct polynomial E_p as in the claimant,

    |Z^p-E_p| <= delta |Z|^p + C_(p,delta) V^(p/2).

For the integral seam, p is even. A fixed finite/countable measurable family is absolutely summable almost everywhere. With respect to a nonnegative measure, set

    M = integral |Z|^p,  J = integral V^(p/2),  I = integral E_p.

Assume J is finite. Then E_p^- is integrable, I has a well-defined extended value in R union {+infinity}, and

    (1-delta)M <= I+C_(p,delta)J,
    I <= (1+delta)M+C_(p,delta)J

for every 0 < delta < 1. If I is finite above, M is finite and (A1)-(A3) follow as finite-valued inequalities. In (A3), the absolute value belongs outside the signed integral; the stronger pointwise negative-part control also holds.

In the claimant's application, the measure is w(R/T)dR. The assumed nonnegativity and compact support of w make this a finite nonnegative measure for each T. The supplied fixed-T majorization

    sum_d |f_d(R)| <= sum_d A_d(T) < infinity

uniformly in R is a sufficient domination hypothesis, and all f_d are assumed to be real measurable functions. This review verifies the implications of those inputs, not their arithmetic derivation.

For the budget statements, A(T) is nonnegative and J_(p,Q), M_p(L_Q) are each bounded by a fixed constant times A(T). Constants may depend on p, the fixed weight/coefficient data, and the stated input bounds. For sharp-circle conclusions, the complete reconstruction and persistence hypotheses in Section 5 must additionally be valid; their algebraic consequences are checked here only conditionally.

## 3. Proof and seam audit

### 3.1 Ordered normalization and partition coefficients

In the permutation formulation of (A6), each cycle of length h contributes P_h. After expansion, a fixed index tuple has coefficient equal to the product of the permutation-sign sums on its equality blocks. A block of size at least two has sign sum zero by composition with a transposition; a singleton has sum one. Thus precisely the ordered distinct tuples have coefficient one. Grouping cycles by their underlying sets yields the factor (|C|-1)! and its sign in (A6). No factor p! is missing or duplicated.

For h >= 2, |P_h| <= V^(h/2). Each nonidentity permutation has at most p-2 fixed points. The number having exactly p-j fixed points is binom(p,j)D_j. Therefore the nonidentity absolute coefficients sum to p!-1, and (A7) follows. All coefficient signs have been discarded only for bounding the remainder, not for claiming an estimate on the signed distinct integral.

### 3.2 Constructive absorption constant

For V > 0 put t = |Z|/sqrt(V). The bound is

    |Z^p-E_p|/V^(p/2) <= A max(1,t^(p-2)).

For R0 = max(1,sqrt(A/delta)), t >= R0 gives A t^(p-2) <= delta t^p. For t < R0 the expression is at most A R0^(p-2), which equals the constant displayed in (A8). Both inequalities remain valid for p = 2, when the exponent p-2 is zero. For V = 0 the separate zero-family branch is correct. No value of T, Q, or the number of classes enters this constant.

### 3.3 Signed integral and negative part

Because p is even, the pointwise lower inequality is

    E_p >= (1-delta)|Z|^p-C_(p,delta)V^(p/2).

Consequently E_p^- <= C_(p,delta)V^(p/2). If J is finite, I cannot be minus infinity and is a legitimate extended signed integral. Also E_p+C_(p,delta)V^(p/2) is nonnegative. Integrating this nonnegative function gives

    (1-delta)M <= I+C_(p,delta)J

without first assuming M finite. A finite upper bound on I forces M finite. The absolute remainder then integrates, and

    |M-I| <= delta M+C_(p,delta)J

implies (A2), the signed lower bound in (A3), and

    |I| <= (1+delta)M+C_(p,delta)J.

The claimant correctly retains the signed I in the upper moment bound. The possibility I < 0 does not invalidate that bound: its right side is nonnegative by the pointwise lower inequality. No hidden assumption I >= 0 is used.

### 3.4 Finite-to-infinite and integration

For an absolutely summable family, S = sum_i |x_i| is finite. The full ordered p-fold absolute sum is at most S^p, so the distinct subseries is absolutely convergent. Finite truncations give Z_N -> Z, V_N -> V, and E_(p,N) -> E_p; the family-size-independent inequality passes to their pointwise limit. For example, its tuple-series tail is at most

    p S^(p-1) sum_{i>N}|x_i|.

For the actual family, the assumed fixed-T uniform bound S(R) <= K_T < infinity implies an integrable common dominator K_T^p on the finite weighted window. Thus pointwise and integral limiting operations for every fixed p,T are justified. The absence of a T-uniform l1 majorizer is immaterial to this passage: uniform asymptotic estimates come from (A8) and the separately supplied head/J bounds. No integral-limit conclusion is asserted for merely conditionally summable families or from pointwise convergence alone.

### 3.5 Budget equivalences and cutoff bookkeeping

Taking delta = 1/2 gives

    M_p(Z_Q) <= 2I_(p,Q)+2C_(p,1/2)J_(p,Q),
    |I_(p,Q)| <= (3/2)M_p(Z_Q)+C_(p,1/2)J_(p,Q).

The negative-part floor bounds the negative side of I when J is paid. Hence a one-sided upper bound I <= constant A is equivalent to |I| = O(A), and both are equivalent to M_p(Z_Q) = O(A). The inequalities |a+b|^p <= 2^(p-1)(|a|^p+|b|^p), applied in both directions with B_T = L_Q+Z_Q, add M_p(B_T) to the equivalence once the head is paid. The constants are allowed to depend on fixed p.

Treating (A4) as an input, Q = 1 gives the claimed O_p(T) budgets. For Q = floor(T^(1/p)), the valid inequalities T^(1/p)/2 <= Q <= T^(1/p) give

    T Q^(p/4) <= T^(5/4),
    T Q^(-p/4+eta) <<_(p,eta) T^(3/4+eta/p)

when eta is sufficiently small that the exponent of Q is negative. Thus the crude epsilon-budget equivalences for b >= 5/4 are correct. No exceptional small-T floor case occurs because T^(1/p) >= 1.

The optional improved threshold (A5) is a conditional assertion: its distribution input was not inspected. Given the stated layer-cake bound, the exponent h_p is algebraically consistent, and h_12 = 1+5/156 = 161/156. This review does not certify the applicability of the coefficient-mask distribution theorem.

### 3.6 Fixed-order quantifiers

The constants in (A8) and in the head/tail triangle inequality grow with p. The candidate does not require them to be uniform in p. Conditional on the stated restoration/persistence inequalities, the normalized moment budget b gives

    theta_p = 1/4 + (1+2b)/(4(p+1))

when b >= 1, with b replaced by the appropriate paid maximum otherwise. If b_p = o(p) along an unbounded sequence of even orders, these correction exponents tend to zero. For any prescribed final positive epsilon, one first chooses a sufficiently large single p, then an input epsilon, and only then lets T grow. This is a valid order of quantifiers. No step permits taking p = p(T).

## 4. First doubtful or unproved step

No blocking defect was found in Sections 1-2 at the finite/summable absorption and integral seam.

The first missing mathematical input for an improved actual moment bound is still an independent upper bound for the actual signed I_(p,Q) at the desired budget. The finite kernel supplies no such estimate. For an unbounded sequence of fixed orders, the b_p = o(p) signed estimates remain additional unproved hypotheses, as the claimant states.

For independent certification of the entire application, the amplitude square-sum/head estimates, optional mask distribution, and sharp reconstruction must be audited against their actual dependencies. They are outside this review's permitted context and have not been certified here. This is a scope limitation, not a discovered contradiction in those inputs.

The generic measurable-family paragraph is understood to retain the preceding absolute-summability hypothesis. Under that reading it is correct; dropping summability or measurability would exceed the reviewed statement.

## 5. Controls and outcomes

All controls are exact analytical calculations, with no numerical experiment.

- `finite_partition_identity`: PASS. At p = 2, E_2 = Z^2-V. At p = 4, E_4 = Z^4-6Z^2V+3V^2+8ZP_3-6P_4. The absolute nonidentity coefficients are 6+3+8+6 = 23 = 4!-1; the derangement grouping is 6t^2+8t+9.
- `relative_absorption`: PASS. The zero family is exact. With fewer than p nonzero indices E_p = 0; the required square-sum expenditure is present. Equal positive values give E_p = (N)_p a^p and relative error asymptotic to binom(p,2)/N at fixed p, consistent with the large-t estimate A/t^2. The control (a,-a) has E_2 = -V and verifies that signs do not defeat the inequality.
- `signed_integral_negative_part`: PASS. The claimant's p = 6 family (1,1,1,-1,-1,-1) has Z = 0, V = 6 and E_6 = -720. On a one-point measure space its signed integral is negative. The negative-part bound permits this, and the moment implication never assumes a nonnegative I.
- `finite_to_infinite`: PASS under the stated absolute-summability and domination hypotheses. Absolute ordered-product mass is bounded by S^p; fixed-T uniform S gives an integrable dominator on the weighted window. A claim for conditional summability was neither needed nor accepted.
- `fixed_order_quantifiers`: PASS. With p-1 unit entries and delta < 1, E_p = 0 forces any constant C_(p,delta) to be at least (1-delta)(p-1)^(p/2). Thus uniformity in growing p would be false; the claimant correctly makes only fixed-order claims.
- `remaining_signed_target`: PASS as an explicit limitation. With N unit values on a one-point space, I/J = (N)_p/N^(p/2) tends to infinity at fixed p. Hence the finite hypotheses alone cannot bound the signed integral by the square-sum budget.
- `review_isolation`: PASS. The permitted context expansion was limited to the exact claimant file. No sibling report, historical actual kernel, graph, or state was inspected. The initial blind report was preserved. Only this assigned review artifact was written.

## 6. Dependencies and exact artifacts used

Exact files read in the combined blind-derivation/review context:

| Artifact | SHA-256 |
| --- | --- |
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/blind_partition_absorption.md` | `c34aaeeaf7f25d8ee5fe1cf83fe149ed98e6226c30b3a1fe3fac11ce4b82ec63` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/isolated_absorption.md` | `bcc451ae8c29d9a8c5623b90a6d8fb84c99eb98543189de8c2fdebe93c851422` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/candidates/conductor_fixed_order_kernel.md` | `6e2be69a41d2bee8b8391e154a01e2f7468291314668c4363a93cc4b126b2caf` |

The prior independently authored report at `reports/blind_partition_absorption.md`, SHA-256 `71e5827c677fb0975eb763f667cf1472ac4e28d71ded17293578cd0eb8b75f23`, was already available in the reviewer's own session history; it was not modified or newly used to import any additional context.

No external source, computer algebra result, or numerical certificate was relied on. No claim is made to have reproduced the conductor's separately described controls. This review supplies independent analytical controls only.

Output: `rounds/codex-managed/gc-fixed-order-moment-absorption/reviews/independent_finite_absorption_review.md`, explicitly UTF-8 without BOM. Its final hash is returned separately.

## 7. Recommended state effect

Recommend accepting this review as a PASS for the final-hash claimant's finite/summable absorption and signed integral seam, and as a conditional PASS for the head/tail budget equivalences and fixed-p quantifier logic. No correction to the reviewed finite kernel is required.

Promotion of the complete application remains contingent on the conductor's other required source/application checks and mechanical state validation. Do not use this isolated review to certify uninspected arithmetic inputs, to assert a signed integral bound, to improve a pointwise exponent, or to close any parent target. No graph, proof draft, validation matrix, synthesis, or initial frozen report was edited. This bounded review ends upon freeze and hash return; no successor is initiated.