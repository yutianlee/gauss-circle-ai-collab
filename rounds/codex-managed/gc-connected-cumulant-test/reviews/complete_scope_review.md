# Round234 — complete-scope nonauthor review

- Campaign: gc-connected-cumulant-test
- Task/role: complete_scope_review / nonauthor actual-binding and restoration reviewer
- Generated: 2026-10-12T00:42:01.0990447Z
- Reviewed candidate SHA-256: 3a443b5e63e826511f99e9428438018e5fc41f358a014fc15d9b8bb75233ae97
- Starting/current graph SHA-256: dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306
- The earlier statement-only report remains frozen. Expanded context was used only for this separate review.
- No candidate, initial report, proof kernel, or shared state was edited.

## 1. Result and verdict

PASS for the assigned complete-scope seam: the actual family binding, probability normalization, signed disconnected remainder, finite/countable passage, accepted216/233 scope, and conditional complete restoration are valid. The candidate correctly states that no new complete moment or pointwise exponent has been obtained.

The transfer from the full-harmonic absolute certificate C10 to the connected absolute obstruction C2 is logically valid given C10. The original Gram-proof files underlying C10 were outside this review's permitted context. Their proof certification belongs to the separate actual-certificate seam; this report does not silently promote that reviewed admission evidence to an accepted graph theorem.

## 2. Exact statement and hypotheses audited

The literal real family is
\[
 f_d(R)=\sum_{s\ge1}r_2(ds^2)(ds^2)^{-3/4}
          \Psi(s\sqrt{d/T})\cos(2\pi Rs\sqrt d-3\pi/4),
\]
with squarefree d>Q=floor(T^{2/5}), Z=sum_d f_d, and the fixed mollifier and window in accepted216. The probability measure is
\[
 d\nu_T=w(R/T)dR/(TW),\qquad W=\int w>0.
\]
All radii T>=2 are real. All harmonics, cosine signs and infinite tails are retained. Order12 is fixed before T varies.

For ordered pairwise-distinct labels, m_C is the normalized product moment and kappa12 is the finite joint-cumulant partition formula with coefficient
c(pi)=(-1)^{|pi|-1}(|pi|-1)!.
The physical sums are I12=TW sum* m_[12] and K12=TW sum* kappa12.

The proved assertion is |I12-K12|<<T^{1+epsilon}. The unproved target is the one-sided upper bound K12<=C_epsilon T^{29/25+epsilon}. The separate certificate conclusion concerns TW sum*|kappa12|, not either signed sum.

## 3. Derivation and seam audit

### Actual binding and normalization

The f_d, Q, Z and I12 definitions match accepted216 exactly. Indeed TW E_nu E12=integral w E12, so the candidate's I12 is the accepted unnormalized distinct-class integral.

Each block expectation is genuinely a probability expectation. Thus a product of k block moments has k normalization factors internally; using k independent radius variables represents that product exactly. The single outer TW belongs to I12 and K12 and is restored once, after the partition sum. No extra T is introduced for each block. In particular normalized Fourier averaging is
\[
 E_\nu e(\lambda R)=\widehat w(-T\lambda)/W,
\]
with no factor T. The candidate's C3 and C4 use this normalization correctly.

The joint-cumulant coefficients c(pi), depending on the number of blocks, are distinguished correctly from the distinct-label collision coefficients
mu(sigma)=product_A(-1)^{|A|-1}(|A|-1)!.
Interchanging those coefficient systems would invalidate the argument; the candidate does not do so.

### Why the lower-moment input suffices for C1

Accepted216 D10 gives
\[
 M_r(Z)\ll T^\eta(T+T^{(r-2)\beta}),\quad 2\le r\le10.
\]
Dividing by TW, and using (r-2)beta<1 for every r<=9, gives
E_nu|Z|^r<<T^\eta. For r=0 the moment is exactly1; r=1 follows from Cauchy--Schwarz and the r=2 bound. This uses the actual tail Z=B_T-L_Q, not an arbitrary subfamily supremum.

Accepted216 D7, or accepted233 A10, gives
\[
 V(R)=\sum_{d>Q}f_d(R)^2\le\sum_{d>Q}A_d(T)^2
       \ll_\xi Q^{-1/2+\xi}.
\]
Fixing any sufficiently small xi supplies a T-independent square-mass bound H^2. The sharper Q decay is not needed for C1.

For a proper cumulant partition with no singleton or pair, every block has size3 through9. Independent-radius collision inclusion-exclusion produces factors
\[
 U_A=\sum_d\prod_b f_d(R_b)^{|A\cap C_b|}.
\]
For |A|>=2, Holder gives |U_A|<=H^{|A|}; singleton factors are actual Z(R_b). Therefore each equality-partition term is bounded after integration by a constant times product_b E_nu|Z|^{s_b}, with s_b<=9. This is O(T^epsilon) after dividing the requested epsilon among finitely many inputs. Absolute values occur after the equality-partition identity, not inside the original label-tuple sum.

If a cumulant partition has a singleton or pair, its whole tuple sum can instead be bounded absolutely. Truncate the norms only for this proof at P=T^{3/2}; full Schwartz tails have arbitrarily negative-power coefficient mass. Distinct squarefree labels force n!=m in a two-class harmonic product, hence
T|sqrt(n)-sqrt(m)|>=T^{1/4}/2 for retained norms. Smooth averaging then pays A1+A2 at every negative power, while the other blocks cost at most a fixed power of the full coefficient mass. Diagonal self-correlations are not declared small; they remain in V.

Consequently all proper partitions are paid, and the one outer TW yields C1.

### Finite and countable scope

For each fixed T, S_T=sum_n|a_n(T)| is finite and bounds sum_d|f_d(R)| uniformly in R. Thus on the k-fold radius space every finite twelve-position expansion is dominated by the fixed finite number S_T^{12}. This supplies all Fubini, product-expectation and finite-exhaustion passages needed here.

The bound need not be uniform in T for dominated convergence at fixed T. Uniform asymptotic constants are obtained only after passing to the actual full family and applying its square-mass and moment bounds. This avoids the invalid inference that every arbitrary finite truncation has the same normalized lower-moment bounds as Z. Negative block moments and signed cumulants cause no problem.

### Absolute correction and obstruction scope

The dyadic proof of C4 is a legitimate absolute upper bound. Freezing q-1 norm variables and summing the maximal norm N uses spacing of size T/sqrt(N), with the bound 1+sqrt(N)/T. Multiplying its coefficient maximum by the other q-1 coefficient sums gives the displayed product N_j^{1/4+eta}/N. The maximal norm's Schwartz factor pays all N>T, while q=3 and q=4 give respectively bounded and logarithmic low-scale sums. This justifies A_q<<T^{max(q/4-1,0)+epsilon} for each fixed q.

Dropping cross-block distinctness is permitted only in this nonnegative correction majorant. The proper shapes with every block at least3 are exactly
(9,3), (8,4), (7,5), (6,6), (6,3,3), (5,4,3), (4,4,4), (3,3,3,3).
The largest physical correction exponent is 1+(9/4-1)=9/4. Hence C9 is valid.

Given the separately certified C10, triangle inequality gives
\[
 TW\sum^*|\kappa_{12}|
 \ge c_0T^{5/2}-O(T^{9/4+\epsilon})
 \ge cT^{5/2}
\]
for sufficiently small epsilon and sufficiently large real T. This is a bound on a certificate with the modulus outside each fully pooled tuple correlation. It is neither a signed lower bound nor a physical-moment lower bound. The candidate correctly distinguishes this stronger full-harmonic premise from the accepted217 Fourier-termwise obstruction; the latter alone would not imply C10.

### Complete restoration and accepted233 boundary

C1 makes one-sided K12 and I12 bounds at b=29/25 equivalent, since1<b. Accepted216 then gives
\[
 |M_{12}(Z)-I12|\ll T^{8\beta-1/5+\epsilon},
 \qquad M_{12}(L_Q)\ll T^{15/13+\epsilon}.
\]
Here 8beta-1/5<21/25<29/25 and 29/25-15/13=2/325. The first inequality controls the negative part of I12; no positivity of I12 or K12 is assumed. The scalar head/tail inequality restores the full B_T moment, including mixed terms. This is not a small additive approximation of M12(B_T) by I12.

Accepted233's sharp reconstruction gives at p=12
\[
 \int_{X/2}^{3X}|P(x)|^{12}\,dx
 \ll T^7M_{12}(B_T)+T^{8+\epsilon},\qquad X=T^2.
\]
Conditionally on b=29/25, the larger exponent is T^{204/25}, namely X^{102/25}. Inclusive-count persistence divides this sharp moment exponent by13 and yields 102/325. This verifies the candidate's (7+29/25)/26 calculation and pays the entire smoothing/Bessel error.

Accepted233 remains a fixed-even-order reduction. A sufficient unbounded sequence requires separate actual signed estimates with b_p=o(p), with p chosen before T. The candidate supplies no such estimates and makes no substitution p=p(T). Accepted216's stronger additive order12 result is preserved.

## 4. First doubtful or unproved step

The first missing arithmetic step is exactly
\[
 K12(T)\le C_\epsilon T^{29/25+\epsilon}
\]
for the complete actual signed tuple sum. C1 controls its difference from I12 but supplies no such upper bound. No improved complete exponent follows from C1 alone.

The underlying full-harmonic C10 Gram certificate is an explicitly declared dependency outside this review's permitted source set. This is a review boundary, not a newly identified defect; final round closure must also obtain the designated certificate-seam verdict.

No defect was found in the assigned binding, normalization, countable-limit, or complete-restoration seams.

## 5. Controls and outcomes

- probability_normalization: PASS analytically. Each moment uses nu_T and there is exactly one outer TW.
- actual_full_harmonics / rapid_single_pair: PASS analytically. The tail is restored after proof-device truncation; cross-class pairs alone have the separation used.
- signed_collision_sum: PASS analytically. Mixed-radius Holder and inclusion-exclusion handle all repeated labels, and no tuple-absolute replacement is made.
- complete_budget: PASS. The head gap is2/325; the repeated error is below21/25; the conditional pointwise value is102/325.
- no_signed_lower_bound: PASS. C2 concerns an absolute certificate only; the signed target and the quarter problem remain open.
- exact controls: the permitted current JSON records all order2..12 coefficient comparisons and constant-cumulant checks as passing; the maximal proper-partition exponent is9/4. Its two isolated mixed-radius checks are-560 and-23120, and the added discovery control records direct=expanded=-68112 over5040 assignments. These are reported diagnostic checks, not substitute proofs. I did not read or rerun excluded source scripts.
- constant-family control: its signed distinct sum12! binom(N/2,6)/N^6 stays bounded while its absolute tuple sum grows. Its higher joint cumulant is zero, so it cannot prove the actual connected obstruction; the candidate says this explicitly.
- history and scope: the reviewed graph has both216 and233 nodes proved_internal with their explicit no-complete-gain limitations. No shared mathematical state was mutated by this review.

No new experiment or source lookup was needed.

## 6. Dependencies and exact reviewed hashes

Only the current brief and its listed files were read in this expanded review. The initial blind context remains separately recorded in the frozen initial report.

- protocol.md:
  f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a
- state/proof_obligations.yml (selected accepted nodes and relevant matches):
  dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306
- state/active_campaign.yml:
  7736f3050adba099c4ecbbb9eb78639f4a32b8ae9361ce7c05f5cc04f023a13b
- rounds/codex-managed/gc-connected-cumulant-test/briefs/complete_scope_review.md:
  4433732a85021c6e3fe58ec6d5f6c63dd4fd3ea4f48004717e219669bd8c4d67
- rounds/codex-managed/gc-connected-cumulant-test/candidates/conductor_connected_test.md:
  3a443b5e63e826511f99e9428438018e5fc41f358a014fc15d9b8bb75233ae97
- proofs/kernels/gc_complete_distinct_radical_moment_reduction.md:
  d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee
- proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md:
  b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0
- rounds/codex-managed/gc-connected-cumulant-test/controls/control_manifest.md (current expanded version):
  637fff1ca0f85b632f2e5a3cb93772639b19c5833dd19e9ff8e1b316fbad803d
- rounds/codex-managed/gc-connected-cumulant-test/controls/exact_local_controls.json (including -68112 control):
  89e888dfaf9c7e933ebeded4b165ae0598880aebcc29b1d30f3e18d46b780cd1

The earlier manifest version was also read before the conductor's notified control update; its hash was9254a1fcc8b0667539e4c150740e41c4d4c93e01777bf569958a268abde4240d. The current version above was then read. Candidate hash stayed unchanged.

The reviewed graph nodes are GC-complete-distinct-radical-twelfth-reduction, GC-complete-fixed-even-moment-distinct-absorption, and the adjacent GC-distinct-radical-absolute-certificate-obstruction scope distinction. Accepted inputs are used only within their stated interfaces.

## 7. Recommended state effect

Retain the candidate as reviewed evidence for this seam. Close the bounded test without a complete gain once the independent certificate and finite-algebra seams also pass. The identity State Patch and unchanged accepted graph/proof draft are appropriate.

Do not promote a signed K12 bound, a complete moment exponent, a pointwise improvement, an unbounded-order estimate, or the quarter theorem. This assigned review is complete and frozen.
