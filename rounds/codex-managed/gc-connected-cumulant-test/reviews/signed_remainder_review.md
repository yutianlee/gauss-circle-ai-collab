# Round234 nonauthor signed-remainder review

Campaign: `gc-connected-cumulant-test`. Task: `signed_remainder_review`.
Role: independent nonauthor collision/moment/application seam reviewer.
Generated: 2026-10-12 UTC. Starting graph SHA256: `dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306`.
Exact reviewed conductor candidate SHA256: `3a443b5e63e826511f99e9428438018e5fc41f358a014fc15d9b8bb75233ae97`.

## 1. Result: PASS

**PASS, with no mathematical repair required**, for conductor candidate Sections3A,3C, the proof of(C1) in3D, and3E. The actual signed disconnected remainder satisfies

    |D12|=|I12-K12| <<_epsilon T^(1+epsilon).

The normalized lower moments needed by the mixed-radius argument are available for every integer order0 through9. The exact label-collision identity preserves the requisite signed cancellation, and the full countable class family satisfies the needed domination. A one-sided K12 upper bound at29/25 would therefore imply the already specified complete twelfth-moment milestone and conditional pointwise exponent102/325. That K12 estimate is still unproved.

The review also passes the signed discovery report's stronger comparison

    S_pi=product_b E_nu Z^(q_b)+O_epsilon(Q^(-1/2)T^epsilon)

for proper partitions with all q_b>=3. This stronger statement is not necessary for(C1), but its actual-amplitude proof is valid.

I authored the earlier absolute-certificate audit, not these collision/moment claims. This review audits those nonauthored seams. It does not count as a second independent review of my own certificate derivation or as a new review of the inherited harmonic lower bound. The latter retains its status as reviewed admission evidence, not a graph-promoted theorem.

## 2. Exact statement and hypotheses reviewed

The candidate uses the accepted216 actual f_d with every harmonic and cosine sign, the same fixed rho/Psi/w, Q=floor(T^(2/5)), Z=sum_(squarefree d>Q)f_d, W=integral w>0, and probability measure dnu=w(R/T)dR/(TW). Labels in each twelve-tuple are ordered and pairwise distinct.

For a partition pi of the twelve positions, define

    S_pi=sum_d^* product_(C in pi) E_nu product_(j in C)f_(d_j),
    c(pi)=(-1)^(|pi|-1)(|pi|-1)!.

The one-block coefficient is1. Therefore the exact sign convention is

    D12=-TW sum_(pi proper) c(pi)S_pi.                         (R1)

No assumption of independence of the f_d on the original radius space is made. Independent radius copies represent a product of moments exactly. All constants depend only on fixed functions, the fixed order12 and requested epsilon. Full-family lower moments are invoked only after the infinite identity is established.

## 3. Proof and derivation of the audit

### A. Smooth singleton/pair removal: PASS

The full coefficient norm S_T=sum_n|a_n(T)| is finite for every fixed T and grows at most polynomially. Schwartz decay gives sum_(n>T^(3/2))|a_n(T)|<<_A T^(-A), for arbitrary fixed A, including after multiplication by any fixed power of S_T. Thus all omitted mixed tails in the temporary norm cutoff can be paid to arbitrary order.

The probability Fourier kernel is w-hat(-T lambda)/W. For a singleton |lambda|>=1. For different squarefree classes, n=ds^2 and m=et^2 cannot be equal because their squarefree cores differ. Below the temporary cutoff,

    |sqrt(n)-sqrt(m)|>=1/(2T^(3/4)),

so T|lambda|>=T^(1/4)/2 for the difference; the sum frequency is larger. Smooth Fourier decay pays all such terms, including their polynomial coefficient mass. This proves rapid A1 and A2 for the full waves. It does not discard a diagonal contained in the original quantity: equal classes are excluded from A2 by definition. Equal-class collisions later in the proof remain in U_A and V.

If a proper moment partition has a singleton or pair, summing its moment moduli and dropping only cross-block distinctness constraints is bounded by that rapid A1 or A2 times S_T to the number of remaining positions. Thus even partitions(11,1) and(10,2) are paid without needing global moments of orders10 or11. This is why the subsequent moment argument needs at most order9.

### B. Mixed-radius finite identity and its coefficients: PASS

Fix a proper pi with block sizes3<=q_b<=9 and use independent radii R_b, one for each block. For a label-equality partition sigma set

    mu(sigma)=product_(A in sigma)(-1)^(|A|-1)(|A|-1)!,
    U_A=sum_d product_(j in A) f_d(R_(b(j))).

Then the pointwise identity is

    sum_d^* product_j f_(d_j)(R_(b(j)))
          =sum_sigma mu(sigma) product_(A in sigma)U_A.        (R2)

To check its coefficients independently, fix a tuple with actual equality partition tau. Its coefficient on the right is sum_(sigma refining tau)mu(sigma), which factors over equality classes. On a class of size h the factor is the sum of signs of all permutations of h letters, since each cycle support of size a carries(a-1)! choices and sign(-1)^(a-1). This sum is1 for h=1 and0 for h>=2 by a transposition bijection. Thus exactly distinct tuples survive. This proof does not depend on the different radius values.

The coefficients mu(sigma) differ from the cumulant coefficients c(pi). For example a single equality block of size12 has mu=-11!, whereas a one-block cumulant term has c=1. The candidate uses the two systems consistently. The minus sign in(R1) is also correct.

### C. Bounding mixed collisions by square mass: PASS

For |A|=h>=2 let m_b count its positions in original block b. With V(R)=sum_d f_d(R)^2, Holder on the label index and the elementary l^2-to-l^h inequality give

    |U_A|<=product_(b:m_b>0)(sum_d|f_d(R_b)|^h)^(m_b/h)
           <=product_b V(R_b)^(m_b/2).

The full amplitude estimate A_d=sum_s|a_(ds^2)|<<r_2(d)d^(-3/4) gives

    V(R)<=sum_(d>Q)A_d^2<<_eta Q^(-1/2+eta)<=H^2

with H independent of T after fixing any eta<1/2 and using Q>=1. This follows from accepted216(D5),(D7), and is independently explicit in accepted233(A9),(A10). It is uniform in R and includes all harmonics. Thus each nonsingleton collision factor is bounded by H^h, while every singleton is exactly the signed Z(R_b).

If s_b is the number of singleton positions at radius b, taking the modulus only after(R2) bounds each integrated term by

    |mu(sigma)| H^(12-sum_b s_b) product_b E_nu |Z|^(s_b).

Here s_b<=q_b<=9. The modulus is on each collectively summed Z, not on each label f_d. This distinction is the source of the number-of-labels-independent bound. Summing |mu(sigma)| gives12!, so the finite partition sum has an absolute constant depending on order12 only.

### D. Actual moment and infinite-family application: PASS

Accepted216 Section3(D10) gives, for2<=r<=10,

    integral w|Z|^r <<_epsilon T^epsilon[T+T^((r-2)beta)].

For2<=r<=9, (r-2)beta<=7beta<91/100<1, because the inherited qualified input has beta<13/100. Dividing by TW yields E_nu|Z|^r<<T^epsilon. Order0 is exactly1; order1 follows by Cauchy-Schwarz from normalized order2. In particular the candidate does not incorrectly treat the tenth moment as normalized O(T^epsilon): its possible8beta loss is not needed.

This input applies to the exact actual Z=B_T-L_Q at Q=floor(T^(2/5)). Accepted216(D8)-(D10) audits the coefficient mask and derives its supremum by this specific subtraction. No arbitrary-mask or finite-subset supremum is imported. The cutoff is comparable to T^(2/5) uniformly for real T>=2, so floors do not change the estimates.

The countable-interchange requirement in the blind report is satisfied especially strongly here. At fixed T and every R,

    sum_d|f_d(R)|<=S_T<infinity.

For k independent radii the unrestricted twelvefold absolute product sum is bounded by S_T^12, a finite constant. Tonelli, Fubini and dominated convergence therefore identify the integrated full distinct-label sum with its external sum of products of moments. They also permit the limit in(R2) and in every finite partition product. This fixed-T domination is enough even though S_T grows with T.

One must not infer uniform low-moment bounds for arbitrary finite partial Z from those for full Z. Neither candidate nor signed report does so: pass to the full identity using S_T^12, then apply the actual full-Z moment bounds. The sentence about convergence of finite-partial moments is valid by the same fixed-T domination and does not require a uniform asymptotic bound for those partial moments.

Allocate epsilon among at most four independent radius factors; the finite partition sum then gives |S_pi|<<T^epsilon. Combining this with rapid singleton/pair shapes and restoring exactly one TW proves(C1).

The signed discovery report's stronger comparison uses the all-singleton sigma term separately. For a nonsingleton block of size h it applies the valid uniform estimate |U_A|<=sum_d A_d^h<<Q^(1-3h/4+eta). If there are c nonsingleton blocks with total H0 positions, c<=H0/2 and H0>=2. Their power is at most Q^(c-3H0/4+c eta)<=Q^(-1/2+c eta). The remaining full-Z singleton moments cost T^epsilon. Since Q<=T^(2/5), the small c eta factor is absorbed by the allocated epsilon. This proves its claimed error Q^(-1/2)T^epsilon without using the stronger comparison in the conductor's(C1) proof.

### E. Complete conditional restoration: PASS

From |D12|<<T^(1+epsilon), one-sided K12 and one-sided I12 bounds at29/25 are equivalent, with every epsilon quantified separately. Accepted216 then restores M12(Z), the complete B_T moment and sharp errors. The head exponent15/13 is smaller than29/25 by2/325. The repeated-class exponent8beta-1/5 is below21/25. The signed error exponent1 is also below29/25.

For a target-sized full B_T moment, accepted233's sharp reconstruction formula gives

    integral_(X/2)^(3X)|P(x)|^12 dx
       << T^7 M12(B_T)+T^(8+epsilon), X=T^2.

The leading target exponent is7+29/25=204/25>8, hence the sharp moment exponent is102/25 in X. Inclusive-count persistence divides this exponent by13, giving102/325. This is a conditional implication from a complete moment, not a claimed converse from a pointwise estimate.

The signed report's K12=M12(Z)+O(T^(1+epsilon)) also follows by adding accepted216's smaller repeated-class error. Its negative floor and inherited upper estimate T^(1+epsilon)+T^(10beta+epsilon) are valid; since10beta>5/4>29/25, they furnish no preferred complete gain. No all-order inference is licensed.

## 4. First doubtful or unproved step

No doubtful step remains in the reviewed signed-remainder or conditional-restoration statements under the inherited accepted inputs. The independent isolated collision lemma has precisely the required domination hypothesis, and the actual waves satisfy it.

The first unproved step for a complete improvement is the one-sided signed K12 bound at29/25. The remainder estimate only shows that this is equivalent to the existing full moment target at that budget. Neither the low correlations nor the label-collision identity supplies it. The harmonic absolute certificate is outside this review's nonauthor seam and supplies no signed lower bound.

## 5. Controls and outcomes

- **Probability and outer factor: PASS.** All products use probability expectations at independent radii; exactly one TW is restored in D12. There is no extra T per block.
- **Distinct pair and full tail: PASS.** Unique squarefree cores remove the pair diagonal; Schwartz tails pay every omitted product. Equal-class collisions are retained in square masses.
- **Finite equality coefficients: PASS analytically.** The permutation-cycle proof verifies the identity at every finite label count, including fewer than12 labels. Cumulant and collision coefficients are distinguished.
- **Negative moments and signed sums: PASS.** Original block moments may be negative. Moduli are inserted after exact regrouping, and the proof never estimates the tuple-absolute sum by the signed bound.
- **Countable limit and finite-mask trap: PASS.** Fixed-T bound S_T^12 proves the needed interchange. Full-Z moments are used after the limit, not for arbitrary partial masks.
- **Actual lower moment range: PASS.** Orders0 through9 are paid. The order10 ceiling is never presumed free. All accepted source qualifications remain inherited.
- **Signed/absolute countercontrols: PASS.** The blind report's balanced family has signed value12! binom(N/2,6)/N^6=O(1), while its tuple-absolute sum(N)_12/N^6 grows like N^6. Its zero deterministic higher cumulants do not establish an actual connected lower bound. Its centered Walsh family also checks analytically: orthogonality gives V=1 and diagonal covariance, the complete character sum gives |Z|<=sqrt(3), and each of the78 excluded zero/equal-label conditions removes q^(11-k) out of q^(12-k) assignments. Thus its unsigned counterexample is valid, but is not an actual circle family.
- **Archived exact controls: PASS as diagnostic evidence.** The manifest and current JSON record all orders2..12, all eight proper block patterns, two independent mixed-radius values-560 and-23120, and the separately reproduced discovery value-68112 over5040 assignments. The code recorded inside the signed report is consistent with its equality-partition formula. No additional numerical experiment was needed or run in this review. These finite results are not used as proof of(C1).
- **Complete budget: PASS conditionally.** The exact restoration is102/325, with K12 still open. No improved complete theorem, M1/M2/GAR claim, endpoint, or quarter theorem is inferred.
- **Isolation and preservation: PASS.** This is nonauthor selected-context review after all initial reports froze. Only this assigned review is written. No candidate, report, shared graph, validation matrix, proof draft, synthesis, or historical artifact is changed.

## 6. Dependencies and exact reviewed artifacts

Previously read permitted protocol/accepted kernels were retained in context; the exact accepted graph nodes were rechecked, and accepted216's moment and amplitude passages were reread. The current active manifest records review status and the frozen initial reports. No fresh external source, unlisted filesystem context, or source-search output was read for this review.

| Artifact | SHA256 |
| --- | --- |
| protocol.md | F26FB038496B5AE171B3352E7D02BA1A4B7DD808EF31BF8620E6D4930CEA9D5A |
| state/proof_obligations.yml | DD743DB27ED8EAAC685D23DD2F92DA743DD2D1742C2F150DDECF802DBBCA5306 |
| state/active_campaign.yml | 7736F3050ADBA099C4ECBBB9EB78639F4A32B8AE9361CE7C05F5CC04F023A13B |
| rounds/codex-managed/gc-connected-cumulant-test/briefs/signed_remainder_review.md | 7F81714394123FE5A67BD48D22A5F99D352523A4AD7E369F3D0533583FB2F1E2 |
| rounds/codex-managed/gc-connected-cumulant-test/candidates/conductor_connected_test.md | 3A443B5E63E826511F99E9428438018E5FC41F358A014FC15D9B8BB75233AE97 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | D7A5945F834C565C11CDC26BC3480DE12D173E35DE28C734381392F5FEECB1EE |
| proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md | B1097AA498D0430D5BBE81FB0B8927CC4FFDF278CE838B3EF38F555BC75C31D0 |
| rounds/codex-managed/gc-connected-cumulant-test/controls/control_manifest.md | 9254A1FCC8B0667539E4C150740E41C4D4C93E01777BF569958A268ABDE4240D |
| rounds/codex-managed/gc-connected-cumulant-test/controls/exact_local_controls.json | 89E888DFAF9C7E933EBEDED4B165AE0598880AEBCC29B1D30F3E18D46B780CD1 |
| rounds/codex-managed/gc-connected-cumulant-test/reports/signed_connected_attack.md | 09EE3A7EE1031C015CBC34B463B887524D7150966D774FEC477D2A9DCAD45FA4 |
| rounds/codex-managed/gc-connected-cumulant-test/reports/blind_collision_bound.md | 035FEBF79ED5F6ACC569AD2109F1091B9D014E382A1305B65671743108E9BC7C |

The control JSON was first read at SHA256 `807FE2B0BC1A15B8F035A6636725D8E2BADD54C49F7ADEE0A7BBB22C2F75E72C`; the conductor then added its reproduction of the discovery -68112 control. I reread the full current JSON and bind the table above to that updated artifact. The mathematical candidate and frozen initial reports were unchanged. This disclosed control addition does not change the proof verdict.

## 7. Recommended state effect

PASS the assigned signed-remainder and complete conditional-restoration seams. Retain the exact candidate as reviewed evidence and follow its proposed identity State Patch; this review does not request promotion of an unestimated complete target. Keep the signed K12 estimate and all complete-improvement obligations open. The prior harmonic lower certificate remains reviewed admission evidence unless a separate valid graph action promotes it.

No mathematical repair, candidate rewrite, further experiment, or successor-round design is requested by this review. Freeze this UTF-8 report and return its hash.
