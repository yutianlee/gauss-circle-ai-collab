# Round 233 independent actual-kernel review

Campaign: `gc-fixed-order-moment-absorption`.
Reviewer role: selected-context nonauthor review of the conductor kernel, covering actual binding and sharp scope; not the separate statement-only finite certificate.
Task: bounded review following `actual_fixed_order_bridge`.
Verdict: **PASS at the final claimant hash below; no remaining repair in the assigned seams.**
Reviewed claimant: `rounds/codex-managed/gc-fixed-order-moment-absorption/candidates/conductor_fixed_order_kernel.md`.
Final claimant SHA-256: `b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0`.
Starting graph SHA-256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
Generated UTC: 2026-10-12T00:18:00Z.
No sibling report, external source, numerical experiment or shared-state edit was used.

## 1. Result: reviewed reduction passes, with the signed target still open

The conductor candidate correctly proves the relative absorption and its binding to the complete actual squarefree-class family for every fixed even p>=2, real T>=2 and real Q>=1. The square-sum control pays the defect with T Q^(-p/4+eta) and does not introduce the baseline pointwise exponent. Both proposed cutoffs have complete paid head and defect budgets.

The full-wave comparison, one-sided signed target equivalence, exact sharp-circle amplitude and Jacobian, smoothing contribution, p+1 persistence denominator, and conditional unbounded sequence of fixed-order implication are correct. Promotion can cover only this reduction and conditional implication. It cannot cover the unestimated signed integral, a new full moment bound, a pointwise improvement, or any target parent.

One narrow literal scope issue in the initial claimant was repaired during this bounded review. The optional head proof (A13) now explicitly assumes 1<=Q<=T, which contains Q=1 and Q=floor(T^(1/p)). This makes its absorption of the p=2 logarithm into T^epsilon immediate. The all-real-Q claims (A1)-(A4) remain unchanged and valid. No further repair is required.

## 2. Exact statement, hypotheses and reviewed boundary

The reviewed hypotheses are exactly those in claimant Section 1: a fixed nonnegative real radial smooth unit-mass mollifier supported in the unit disk; real even Schwartz Psi from its Fourier transform; nonnegative smooth w supported in [1/2,2] and equal to 1 on [1/sqrt(2),sqrt(3)]; real T>=2; real Q>=1; fixed even p>=2; and 0<delta<1. Every harmonic s>=1 and every squarefree class selected by literal d>Q is retained.

The audit confirms:

- (A1)-(A3), including the nonnegative numerator in the one-sided absorption, for the complete infinite actual family.
- (A4) uniformly for real Q>=1, with eta chosen sufficiently small after fixing p.
- The complete target equivalences above the paid budgets: b>=1 for Q=1, b>=5/4 for Q=floor(T^(1/p)), or b>=h_p under the optional refinement.
- (A5) and (A13) under the repaired refinement range 1<=Q<=T, with h_p=1+max(p-136/13,0)/(4p).
- (A14)-(A15) and the conditional quarter implication along an unbounded sequence of orders, each fixed independently of T.

The fixed-p constants may grow without control in p. No claim permits p=p(T). Nonnegativity is imposed on w, not on E_(p,Q) or I_(p,Q). The Fourier transform Psi need not be nonnegative away from zero.

This review checks the main finite absorption logic for compatibility with the actual application but does not replace the separately required statement-only finite derivation or conductor-owned computational controls.

## 3. Proof audit and independent seam calculations

### 3.1 Actual coefficients and the square-sum defect

For squarefree d, the prime-factor formula for r2 gives r2(d s^2)<=r2(d)tau(s^2). When a prime congruent to 3 modulo 4 divides d, both representation counts vanish. Otherwise the only enlarged representation factors requiring attention are 2e+2<=2(2e+1) at primes congruent to 1 modulo 4 that divide d; factors at the prime 2 do not increase r2. The factor 4 in r2 is consistent on both sides, including d=1.

Using |Psi|<=1 and tau(s^2)<=tau_3(s),

    A_d(T)=sum_s |a_(d s^2)(T)|
         <=zeta(3/2)^3 r2(d)d^(-3/4).

This is the actual all-harmonic amplitude; d=1 contains all squares, not only n=1. With r2(d)<<_xi d^(xi/2), squared amplitudes obey A_d(T)^2<<_xi d^(-3/2+xi). For 0<xi<1/2,

    sum_(d>Q) A_d(T)^2 <<_xi Q^(-1/2+xi).

Enlarging the squarefree tail to all integers is an upper bound. Since |f_d|<=A_d, V_Q<=sum_(d>Q)A_d^2 pointwise. Raising to p/2 and integrating against a measure of mass T integral w gives

    J_(p,Q)<<_(p,xi)T Q^(-p/4+p xi/2).

Choosing xi=2eta/p proves (A4). This argument needs no h>2 amplitude theorem and no baseline pointwise estimate. At Q=1, fix one xi in (0,1/2) and obtain J=O_p(T), without a T^epsilon loss. The exact defect coefficient C_(p,delta) is absorbed into fixed-p constants, as allowed.

### 3.2 Head, real cutoffs and infinite completion

The elementary disk count gives sum_(n<=x)r2(n)<<x. Partial summation then yields

    sum_(d<=Q)A_d(T)<<Q^(1/4),
    M_p(L_Q)<<_p T Q^(p/4).

This proof uses the actual positive amplitude majorant and retains all the selected harmonics. It is not an unsupported cancellation bound for arbitrary coefficient masks. It is uniform near Q=1 and across squarefree endpoints, because d<=Q is literal.

For Q=floor(T^(1/p)), since T^(1/p)>=1,

    T^(1/p)/2<=Q<=T^(1/p).

Consequently the head is O_p(T^(5/4)); after renaming the arbitrarily small eta, J<<_(p,epsilon)T^(3/4+epsilon). The floor does not depend on R, and the estimates cover the interval where Q=1 and all larger floor transitions. At Q=1 the entire head is O_p(T).

For fixed T, Schwartz decay and the divisor bound imply sum_n|a_n(T)|<infinity. Since the decomposition n=d s^2 is unique, this is exactly sum_d A_d(T). All harmonic series, class sums and products therefore converge absolutely, uniformly in R. The ordered distinct p-fold sum is bounded in absolute value by (sum_d A_d)^p. These bounds justify limits, rearrangement and integration against the finite window. Uniformity of this l1 majorant as T grows is not needed and is not claimed.

The finite relative inequality has constants independent of family size, so it passes to these infinite sums. Its power-sum bound is valid for real values of either sign. Evenness supplies Z_Q^p=|Z_Q|^p, which is the exact place needed for absorption of the unknown moment.

### 3.3 Optional distribution head and repaired (A13)

The optional coefficient mask 1_(sf(n)<=Q) is fixed in R. Truncating n>T^(3/2) leaves a uniformly tiny absolute Schwartz tail even after the mask. In the remaining singleton and ambient dyadic blocks the masked coefficient energy can only decrease, while the accepted unweighted square-root correlation kernel is unchanged. Thus accepted204's finite Gram and covering mechanism applies with its full diagonal, full localization ceiling, and every positive block threshold. Zero extension handles partial blocks. Summing O(log T) block events at a threshold proportional to v/log T proves the stated distribution bound, with input epsilon decreased before logarithmic losses are absorbed. The accepted216 argument already audits precisely this mask mechanism, not merely a lower integer cutoff.

For q0=136/13 and a ceiling W<<Q^(1/4), layer cake pays the O(T) contribution below amplitude 1 and gives

    T^epsilon integral_1^max(1,W) v^(p-3)dv
      +T^(1+epsilon) integral_1^max(1,W) v^(p-1-q0)dv.

At p=2 the first integral is O(log(2+Q)). The initial text did not state a polynomial upper restriction on Q next to (A13). The final claimant now explicitly restricts this optional calculation to 1<=Q<=T, making log(2+Q)=O(log T). No even integer equals q0, so the second integral has no even-order endpoint logarithm. For fixed p>2 it gives exactly the displayed powers in (A13).

With Q=floor(T^(1/p)), the first power Q^((p-2)/4) contributes an exponent (p-2)/(4p)<1. The second gives exponent 1 when p<=q0 and 1+(p-q0)/(4p) otherwise. This proves the claimed h_p. At p=12,

    h_12=1+(12-136/13)/48=161/156.

This verifies the optional refinement at every fixed even p. The repair narrows only the displayed refinement proof; the general real-Q absorption and elementary head statements remain fully uniform. No additional saturation estimate or new theorem is needed.

### 3.4 Whole-wave transfer and signed interpretation

For delta=1/2, the absorption gives M_p(Z_Q)<=2I+2CJ, with I+CJ>=0. Its negative-part floor is I>=-CJ; the reverse estimate is |I|<=3M_p(Z_Q)/2+CJ. These facts suffice to equate a one-sided upper bound on I with a full moment bound once J is paid. Positivity of I is unnecessary and would be false in general.

The two inequalities for B=L+Z and Z=B-L in (A12) retain every mixed contribution through the physical norm inequality. If a nonnegative budget pays J and M_p(L), these inequalities give all four stated target equivalences. Nothing in this passage asserts a small additive approximation for M_p(B), or replaces accepted216's order-12 statement.

The remaining distinct-class expression is the complete signed Fourier integral, with all s, all cosine signs, all coefficient factors and the original window. Distinct radicals imply only that its individual frequencies are nonzero; the proof never uses that fact as quantitative separation or a bound for their signed sum. Thus it introduces no hidden arithmetic gain.

### 3.5 Full sharp restoration and fixed-order sequence

The inherited reconstruction is correctly normalized:

    P(R^2)=sqrt(R) B_T(R)/pi+O_epsilon(T^(1/2+epsilon)).

The leading disk transform R J_1(2pi R sqrt(n))/sqrt(n) has cosine amplitude sqrt(R)/pi times n^(-3/4). Its remainder sums absolutely as O(R^(-1/2)sum r2(n)n^(-5/4)). The smoothing annulus contains O(T^(1/2)+1) possible squared radii, with endpoint multiplicities paid by the divisor bound, producing the stated complete error at smoothing width T^(-1/2). No harmonic has been dropped.

For x=R^2, dx=2R dR supplies a factor T, while the leading amplitude to the pth power supplies T^(p/2). Integrating the smoothing error over x-length O(T^2) supplies T^(2+p/2+epsilon). Therefore (A14) and

    a_p=max(1+p/4,(1+p/2+b)/2)

are exact. The fixed window equals 1 on all radii corresponding to [X/2,3X].

For a positive discrepancy V at x, inclusive-count monotonicity preserves discrepancy at least V/2 on the following interval of length V/(2pi). For a negative discrepancy -V it preserves discrepancy at most -V/2 on the preceding interval of that length. The elementary O(sqrt(x)+1) discrepancy ensures both intervals lie inside the enlarged range for large x. Thus V^(p+1) is bounded by a constant times the pth moment. This proves the denominator p+1 and includes both signs and sharp jumps.

For b>=1 the larger sharp moment exponent is (1+p/2+b)/2, yielding

    theta_p=(p+2+2b)/(4(p+1)).

For smaller proposed b the paid O(T) floor requires replacement by max(b,1); the growing cutoff similarly pays max(b,5/4), or max(b,h_p). If signed exponents are o(p) along an unbounded sequence of fixed even orders, these paid exponents remain o(p). For a desired final epsilon, choose one sufficiently large order first and then sufficiently small input loss. All constants can depend on this chosen order. This is a valid conditional quarter implication and never exchanges p and T limits.

## 4. First doubtful or unproved step

There is no remaining repair in the assigned actual-binding, head, full-wave, sharp-restoration or quantifier seams at the final claimant hash. The A13 scope issue was explicitly repaired and rechecked.

The first unproved arithmetic assertion remains the one-sided target estimate for the actual complete signed I_(p,Q), especially a family whose exponents are o(p) at an unbounded sequence of fixed even orders. The relative inequality is universal for real families and therefore contains no mechanism proving that signed arithmetic target. This review does not certify any such estimate.

The claimant's descriptions of Wolfram and local controls were not independently inspected in this review, because the authorized context excludes their files. Those controls and the isolated finite certificate remain separate conductor gates. They are not substituted for the analytical proof audited here.

## 5. Required controls and outcomes

- **Actual coefficients and harmonics: pass.** The r2 factor inequality covers zero representation classes, d=1, the prime 2 and all s. No positivity of Psi beyond its absolute bound is assumed.
- **Variance square sum: pass.** The exponent is -1/2+xi before raising to p/2; the resulting defect is T Q^(-p/4+eta), with no omitted factor of Q or T.
- **Infinite convergence: pass.** A fixed-T uniform absolute majorant controls all class sums, products, ordered tuples and integration. It retains every tail.
- **Real Q and floors: pass.** Literal class membership and the two-sided floor comparison prove both proposed regimes, including Q=1 and all real-T endpoints.
- **Optional all-p head: pass after narrow repair.** A13 now explicitly has 1<=Q<=T. The p=2 logarithm and the even-order nonendpoint at q0 are both accounted for. The exact p=12 head exponent is 161/156.
- **Signed negative part and complete transfer: pass.** The right side I+CJ is nonnegative by the proved inequality, not by an assumption on I. A12 pays all mixed terms.
- **Sharp restoration and persistence: pass.** Leading factor, Jacobian, smoothing moment, both signs, sharp jumps and p+1 denominator are all retained.
- **Fixed-order quantifiers: pass.** The final epsilon selects p before T varies. No growing-order constants or asymptotic interchange is asserted.
- **Reduction-only scope: pass.** The arithmetic signed target stays explicitly open; no complete moment improvement is inferred from the reduction.
- **Computational gate: not assessed here.** No experiment or control-file inspection was authorized or performed. The separate conductor gate remains necessary.
- **Final claimant integrity: pass.** The archived initial file has its original SHA-256, and the final file has the supplied new SHA-256. After normalizing line endings, the only textual change is the sentence restricting the optional refinement to 1<=Q<=T. The final save also normalizes its line endings from LF to CRLF; this has no mathematical effect.
- **Isolation and state ownership: pass.** No sibling reports were read; only this review is written. The frozen formalizer report and all shared state remain untouched.

## 6. Dependencies and exact artifacts used

The original permitted context was retained without expansion, except for the conductor's explicit authorization to inspect the candidate and its archived initial version to verify the sole repair. No new source theorem was imported. The qualified accepted204 finite distribution and sharp reconstruction, accepted216's actual amplitude/mask argument, and graph-accepted elementary divisor and radical-independence inputs retain their original scope.

| Artifact | SHA-256 |
|---|---|
| Final reviewed `candidates/conductor_fixed_order_kernel.md` | `b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0` |
| Archived initial `candidates/conductor_fixed_order_kernel_v1.md` | `6e2be69a41d2bee8b8391e154a01e2f7468291314668c4363a93cc4b126b2caf` |
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `state/active_campaign.yml` | `58f07ad6959a485751d27e4df55fddc72d6cba7a474ce824c1426a390ab21b15` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/actual_fixed_order_bridge.md` | `cba3784e168c97c8f74167bc86b201cd77664ec82c6bd50f6245b71cf5e394a2` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/actual_interface.md` | `f7ca86a3d0565aff3234286b0f0949a02920ccd91af0521f51aa3bb3baa338a4` |
| `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` | `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee` |
| `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` | `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212` |

Candidate paths in the first two rows are relative to `rounds/codex-managed/gc-fixed-order-moment-absorption/`. This review is a selected-context nonauthor review of the conductor candidate; it makes no claim to statement-only isolation.

## 7. Recommended state effect

**Promote the narrow reduction after the remaining independent gates and graph validation, with no further repair required in these reviewed seams.** Acceptance must bind the final claimant SHA-256 `b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0`, including the explicit optional range 1<=Q<=T.

Preserve accepted216's stronger additive order-12 statement, all historical evidence, all actual signed estimates and all target parents. The new node may record all-fixed-even-order relative absorption, complete actual target equivalences above the paid budgets, and the conditional fixed-order-sequence sharp implication. It may not assert an actual improved moment family, a new pointwise exponent, or the quarter theorem. No State Patch or proof-draft edit is performed by this reviewer. Freeze this report and stop.
