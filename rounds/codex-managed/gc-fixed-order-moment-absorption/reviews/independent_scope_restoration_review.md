# Round233 independent scope and sharp-restoration review

Campaign: `gc-fixed-order-moment-absorption`.
Reviewer task: `hostile_bridge_audit`; role: nonauthor scope/restoration reviewer.
Date: 2026-10-12 Asia/Shanghai.
Starting graph SHA-256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
Final reviewed candidate: `candidates/conductor_fixed_order_kernel.md`, SHA-256 `b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0`.
Status: PASS for this review seam, after one precise optional-head scope repair. This is evidence for the conductor's decision, not a State Patch or a declaration that all other campaign gates passed.

## 1. Result: narrow reduction passes; signed estimate stays open

The repaired candidate correctly proves a complete actual reduction at every fixed even order. Its relative repeated-class bound, signed integral comparisons, full harmonics, head costs, floor handling, and conditional sharp reconstruction are mathematically consistent at the stated scope.

One issue was found in the first candidate, SHA-256 `6e2be69a41d2bee8b8391e154a01e2f7468291314668c4363a93cc4b126b2caf`: the optional layer-cake formula (A13) had no explicit restriction on Q, although its stated proof absorbs the p=2 logarithm log(2+Q) into T^epsilon. The actual claimant already restricted its corresponding formula to 1<=Q<=T. The conductor inserted exactly that restriction before (A13). Both proposed cutoffs obey it, so no theorem, exponent, or conclusion changed. I reread the repaired candidate and bind this PASS to its final hash above. The initial hostile report remains frozen and unchanged.

Promotion is justified only for the narrow relative-absorption and complete-reduction lemma, including its conditional sharp implication. There is still no new bound for the actual signed integral, no new complete moment exponent, and no new pointwise circle exponent.

## 2. Exact statement and hypotheses reviewed

I reviewed the same real radial nonnegative unit-mass smooth mollifier, actual coefficients a_n(T), complete squarefree-class functions f_d(R), nonnegative radius window w(R/T), real T>=2 and Q>=1, and fixed even p>=2 as the frozen interface and candidate. All harmonic indices s>=1 remain. Every distinct tuple is ordered.

The core statement holds for every fixed delta in (0,1):

    integral w |Z_Q^p-E_(p,Q)|
       <= delta M_p(Z_Q)+C_(p,delta)J_(p,Q),
    (1-delta)M_p(Z_Q) <= I_(p,Q)+C_(p,delta)J_(p,Q),
    |I_(p,Q)| <= (1+delta)M_p(Z_Q)+C_(p,delta)J_(p,Q),
    J_(p,Q) <<_(p,eta) T Q^(-p/4+eta),
    M_p(L_Q) <<_p T Q^(p/4).

The full-moment/signed-integral equivalences require a nonnegative budget which pays both J and M_p(L_Q). At Q=1 that budget has exponent at least 1. At Q=floor(T^(1/p)) the elementary sufficient exponent is 5/4; the optional refined threshold is

    h_p=1+(p-136/13)_+/(4p).

The refined layer-cake proof is now explicitly restricted to 1<=Q<=T. The core estimates remain uniform for all Q>=1. No p=p(T), no uniform constants in p, and no claimed signed-integral estimate form part of the theorem.

## 3. Proof and derivation audit

### Relative inequality and all signs

The candidate's partition identity has the correct signed cycle coefficient. Summing over partitions subordinate to an equality block gives the sign sum over all permutations of that block; a transposition pairs opposite signs unless the block is a singleton. Thus precisely the ordered distinct tuples survive.

The absolute coefficient sum over all partitions is p!, and after removing the singleton partition it is p!-1. Each remaining term with r singleton blocks has r<=p-2 and is bounded by |Z|^r V^((p-r)/2). This follows from |P_h|<=V^(h/2) for h>=2, with no positivity assumption on the original entries. The candidate's derangement polynomial records these same absolute coefficients by the number of nonsingletons; it is consistent with the partition proof and not an extra arithmetic assertion.

Splitting t=|Z|/sqrt(V) at max(1,sqrt((p!-1)/delta)) proves the displayed constant in (A8). V=0 and p=2 are explicitly correct. The constant grows with p but has no family-size dependence.

For even p, integration gives a nonnegative M_p(Z_Q). Pointwise,

    E_(p,Q) >= (1-delta)|Z_Q|^p-C_(p,delta)V_Q^(p/2),

so integral (E_(p,Q))_- <= C_(p,delta)J_(p,Q). Thus the signed integral is well-defined whenever its positive part is finite, and a finite one-sided upper bound plus finite J forces moment finiteness. The candidate explicitly preserves the nonnegative numerator I+CJ. Neither I nor E is declared nonnegative. The reverse bound for |I| and both head/tail norm comparisons have the correct constants and directions.

### Actual family, convergence, and constants

The amplitude bound A_d<=C r2(d)d^(-3/4) sums every harmonic via tau(s^2)s^(-3/2). The prime-factor comparison is valid, including classes containing a prime 3 modulo 4 and powers of 2. No sign condition on Psi beyond its realness is needed; |Psi|<=1 supplies the envelope.

The head ceiling follows by partial summation from the positive r2 mass bound. The square-sum estimate is summable uniformly in T; raising it to the fixed power p/2 and choosing the input divisor loss after fixing p gives the correct Q exponent. At Q=1 the resulting constants are independent of T, yielding O_p(T) without a baseline beta input.

For each fixed T, Schwartz decay supplies the separate l1 bound sum_n |a_n(T)|<infinity. This implies uniform absolute convergence in R of the class sums and ordered distinct p-fold sum, so the finite identity passes through integration. The candidate does not confuse this fixed-T l1 convergence with uniform summability of d^(-3/4). No T-dependent l1 bound is used as an asymptotic cost.

The floor comparisons T^(1/p)/2<=Q<=T^(1/p) are valid even when the floor is 1. Raising them to p-dependent powers costs constants depending on p, which the quantifiers allow. They give J<<T^(3/4+epsilon) and the complete crude head O_p(T^(5/4)).

### Optional head and its repair

The optional mask depends on n and T but not R. Zeroing coefficients preserves the block energy bound while keeping the accepted unweighted square-root Gram kernel, diagonal, and full localization ceiling. The actual claimant explicitly restores singleton n=1, ambient partial blocks, O(log T) recombination, the real cosine, and the entire Schwartz tail. This is a valid application of the accepted finite mechanism, not an unproved appeal to a theorem about arbitrary coefficient masks.

For the repaired range 1<=Q<=T, layer cake up to C Q^(1/4) gives the displayed (A13). The p=2 logarithm is now bounded by O(log(2+T)); the other possible logarithmic order q=136/13 is not even. At Q=floor(T^(1/p)), the middle term has exponent (p-2)/(4p)<1 and the final term has exponent h_p. In particular h_12=1+20/624=161/156, as claimed. This refinement remains optional and does not affect the independence of the elementary core from the finite distribution input.

### Sharp restoration and fixed-order family implication

The leading amplitude is sqrt(R)/pi, and dx=2R dR contributes the additional T factor. Raising the full sharp smoothing error to the pth power and integrating gives T^(2+p/2+epsilon), which is retained. Therefore a normalized exponent b gives

    a_p=max(1+p/4,(1+p/2+b)/2)

in the sharp X=T^2 moment. Both the candidate and actual claimant use the correct enlarged interval and the part of w which equals 1.

Monotonicity of the inclusive count gives forward persistence for positive discrepancy and backward persistence for negative discrepancy. Both intervals have length V/(2pi) at height at least V/2. The elementary O(sqrt(X)+1) circle bound places them inside the enlarged dyadic interval for large X. Integrating proves the p+1 denominator. For b>=1,

    a_p/(p+1) = 1/4+(1+2b)/(4(p+1)).

Replacing b by the paid head floor handles smaller purported exponents. An unbounded sequence of fixed even p with b_p=o(p) would suffice, because for each requested final epsilon one first selects one p and then holds it fixed while T increases. The candidate does not substitute p(T), require hidden uniform p constants, or discard the smoothing term. No high-value threshold is used in the complete argument, so no unpaid low-value contribution enters this implication.

## 4. First doubtful or unproved step

After the literal (A13) range repair, this review identifies no remaining unproved step in the narrow reduction relative to its stated accepted dependencies.

The first arithmetic gap is still a one-sided upper bound for the literal complete signed I_(p,Q) at a useful budget. The unbounded fixed-order family with b_p=o(p) is not supplied. Distinct squarefree radicals remove exact zero frequencies but do not give sufficient quantitative near-frequency separation, and the finite absorption lemma supplies no aggregate arithmetic cancellation.

The original candidate's omission was a scope gap in its optional displayed derivation, not a counterexample to its intended cutoff theorem. The repaired final hash closes that gap without claiming the missing signed estimate. The existing actual termwise-absolute obstruction remains unaffected.

## 5. Control tests and outcomes

- Finite signs and multiplicities: PASS analytically. The cycle-partition proof gives coefficient one for ordered distinct tuples and zero for repeated tuples; the absolute coefficient sum is p!.
- Negative signed integral: PASS. At p=2, (1,-1) gives E_2=-2; at p=6, three 1 values and three -1 values give E_6=-720. The offset CJ and its negative-part bound are necessary and present.
- Infinite limits and all harmonics: PASS. Fixed-T l1 convergence supplies identities and integration; uniform square-sum estimates supply asymptotic costs. These roles are kept separate.
- Q floors and fixed-order constants: PASS. Both cutoff regimes include floors equal to 1 and permit constants depending on the fixed p. No p(T) inference occurs.
- Optional head: PASS after repair. Formula (A13) is now explicitly on 1<=Q<=T, so p=2 logarithms are absorbed legitimately. h_12=161/156 was checked exactly by algebra.
- Sharp reconstruction: PASS. The amplitude, Jacobian, smoothing term, both signs, inclusive count, and p+1 denominator are retained.
- Dependency and status scope: PASS. The relative reduction does not use Li--Yang to pay repeated classes, and the optional finite mechanism retains its inherited qualifications. Round216's stronger additive twelfth-order statement is not overwritten.
- Numerical/source controls: OUTSIDE THIS REVIEW. No additional computation or source import was performed. I did not inspect the conductor's Wolfram/local control artifacts and do not certify their completion. The candidate correctly describes computations as diagnostic only; their separate campaign gate remains conductor-owned.
- State ownership: PASS. Only this assigned review was written. No authoritative graph, proof draft, validation matrix, synthesis, legacy artifact, or initial report was changed by this task.

## 6. Dependencies and exact artifact hashes

The newly reviewed artifacts are:

| Artifact or version | SHA-256 |
|---|---|
| Final `candidates/conductor_fixed_order_kernel.md` | `b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0` |
| Initial conductor candidate, before the single scope repair | `6e2be69a41d2bee8b8391e154a01e2f7468291314668c4363a93cc4b126b2caf` |
| `reports/actual_fixed_order_bridge.md` | `a1b2839cf640a2a11d66e6685ca1db8b8f572163412d3d67c00861fd5d2d1221` |
| Preserved `reports/hostile_bridge_audit.md` | `53bf482159c87669b83bed5ec3e9896bc743b0851eb2d519e083b01a79b6cfe2` |

All paths in the preceding table are under `rounds/codex-managed/gc-fixed-order-moment-absorption/`. The original authorized context, inherited from the initial audit, is:

| Artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `state/active_campaign.yml` | `58f07ad6959a485751d27e4df55fddc72d6cba7a474ce824c1426a390ab21b15` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/hostile_bridge_audit.md` | `d1235dbc32d40221b1db5c31bd5c50964db8dce3e9853467f0af7725423050d6` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/actual_interface.md` | `f7ca86a3d0565aff3234286b0f0949a02920ccd91af0521f51aa3bb3baa338a4` |
| `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` | `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee` |
| `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` | `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212` |
| `rounds/codex-managed/gc-upper-tail-separated-products/candidates/strategy_reassessment.md` | `286415c548b027b986f939d17ef9654d51a4d5083253d2df09117d656a20c476` |

The graph and active manifest hashes were rechecked during this review and remained the starting hashes. No other sibling, isolated report, external source, or control artifact was read. Analytical/algebraic effort was 100%; numerical experimentation was 0%.

## 7. Recommended state effect

PASS the repaired final candidate for signs, integral comparisons, convergence, actual binding scope, optional head, fixed-order quantifiers, and sharp restoration. This seam supports promotion of a new narrow all-fixed-even-order relative reduction once the conductor has completed the other required independent and mechanical gates.

Keep the actual signed estimates and quarter target open. Preserve the accepted Round216 additive twelfth-order lemma and all historical nodes. Any State Patch must add only the new reduction and its conditional implication; it must not mark a complete moment improvement or arithmetic cancellation as proved. No further repair, experiment, source import, or successor is requested by this reviewer.
