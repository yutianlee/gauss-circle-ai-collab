# Round231 prelaunch admission: split-prime cancellation

Role: arithmetic mechanism scout. Task: `split_prime_cancellation`.
Generated: 2026-10-11T02:29:01Z. Status: selection evidence only; analytic Round231 is unlaunched.
Frozen graph SHA256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

## 1. Result: exact prime relations and a scoped amplifier no-go

The actual coefficients admit exact complete prime-divisibility and prime-power dilation identities, derived below with the mollifier, radial window, every valuation, primitive complement and squarefree cutoff retained. They do not, by themselves, give a new signed estimate.

The proposed scalar Hecke amplifier has a rigorous obstruction: every completed split-prime row is exactly twice the original complete real wave. Its covariance matrix, including the twelfth-moment weighted covariance, has rank one. Signed amplifier weights either rescale that same wave or annihilate the signal. Polynomial/nonbacktracking combinations have the same problem on this actual coefficient vector. This is a no-go for completed scalar rows followed by covariance/norm bounds, not for all arithmetic amplification.

An unfinished alternative using prime-coprime rows has a precise complete gate. With primes of size P, its discarded divisible part has complete twelfth moment at most T^(4+epsilon) P^(-12). Consequently P >= T^(71/300) pays that part at the preferred T^(29/25+epsilon) milestone. The remaining required signed covariance estimate must save a factor T^Delta over the inherited complete bound, where

    Delta = 10 beta - 29/25 = 0.12966351948... .

No such input is proved here. The primitive rows still contain the common original wave; their apparent arithmetic centering is not a demonstrated decorrelation. This report therefore does not meet the new-signed-input admission gate. Retain Round231 as pending design, with no graph change and no improvement to a complete bound.

## 2. Exact statement and hypotheses

Use exactly the packet's fixed nonnegative radial smooth unit-mass mollifier rho, its real even Schwartz transform Psi, and fixed nonnegative smooth window w. For every real T >= 2,

    B_T(R) = sum_(n>=1) r2(n) n^(-3/4) Psi(sqrt(n/T))
                         cos(2 pi R sqrt(n) - 3 pi/4),
    M12(B_T) = integral w(R/T) |B_T(R)|^12 dR.

The window has support [1/2,2] and equals one on [1/sqrt(2),sqrt(3)]. All identities below hold for every real R, not only window points. For algebra, B_U is defined by the same convergent formula for every U > 0; a definition outside the accepted U >= 2 range is not an extension of an accepted estimate.

Write f(n)=r2(n)/4=(1*chi4)(n). For a prime p set e_p=chi4(p), lambda_p=1+e_p, and

    S_a(p)=sum_(j=0)^a e_p^j,  S_(-1)(p)=0.

Here e_p is 1 for split primes, -1 for inert primes, and 0 for p=2. Thus S_a is respectively a+1, the indicator that a is even, and 1. The zeroth power in S_0 is 1 also at p=2.

Define operators on the full two-parameter wave family by

    A_p^a B_T(R)=p^(-3a/4) B_(T/p^a)(p^(a/2) R),
    D_(p^a) B_T(R)=sum_(p^a|n) a_n(T) cos(2 pi R sqrt(n)-3 pi/4),
    C_p B_T=(I-D_p)B_T,
    E_(p,k) B_T=(D_(p^k)-D_(p^(k+1)))B_T.

A_p^0 and D_1 are the identity. The result is the exact pair of formulas, valid for a,k >= 0,

    D_(p^a) B = S_a A_p^a B - e_p S_(a-1) A_p^(a+1) B,          (2.1)
    E_(p,k) B = S_k A_p^k C_p B,
    C_p B = (I-lambda_p A_p+e_p A_p^2)B.                      (2.2)

Composition in (2.2) acts on the family C_p B, not on a single fixed-parameter function. These identities include all complementary residue classes p does not divide n, not merely the p-divisible piece.

For the amplifier define the completed real row

    H_p(T,R)=p^(3/4) D_p B_(pT)(R/sqrt(p)) + e_p A_p B_T(R).
                                                                    (2.3)

Then H_p=lambda_p B_T exactly. For any finite set of split primes and any complex weights alpha_p, writing S=sum alpha_p gives

    sum alpha_p H_p = 2 S B_T,
    integral w |sum alpha_p H_p|^12 = 2^12 |S|^12 M12(B_T).    (2.4)

In particular, for the real weighted covariance

    K_pq=integral w(R/T)|B_T(R)|^10 H_p(T,R) H_q(T,R) dR,

one has K_pq=4 M12(B_T) for every pair of split primes p,q. The same identity with weight 1 is 4 M2(B_T). No cross-prime independence is available for these completed rows.

The accepted input used in costing is only M12(B_T) << T^(10 beta+epsilon), with beta as in the packet, and the accepted order-twelve radical reduction. No all-order consequence of that reduction is assumed.

## 3. Proof, complete restoration and attempted analytic input

### 3.1 Coefficient recurrence, including valuation exceptions

For n=p^k m with p not dividing m, multiplicativity of f gives

    f(n)=S_k(p) f(m).

For a,k >= 0 the finite geometric sums satisfy

    S_(a+k)=S_a S_k-e_p S_(a-1) S_(k-1).                     (3.1)

For e_p=1 this is (a+k+1)=(a+1)(k+1)-ak. For e_p=-1 it follows by the two parities; for e_p=0 both sides equal 1, with the second term zero. Thus no division by f(n), which can vanish, is used. Restoring r2 yields

    r2(p^a n)=S_a r2(n)-e_p S_(a-1) 1_(p|n) r2(n/p).        (3.2)

The frequently tempting split-prime formula r2(pn)=2r2(n) is valid only when p does not divide n. Its missing term is r2(n/p). At an inert prime, r2(pn)=1_(p|n)r2(n/p), so there is no eigenvalue-2 amplification; at p=2, r2(2n)=r2(n).

Set n=p^a m in the p^a-divisible part of B. The first term of (3.2) gives S_a A_p^a B. In the correction set m=p l; this changes both the radial argument and the mollifier parameter once more, and gives -e_p S_(a-1) A_p^(a+1)B. This proves (2.1). Subtracting adjacent a values and using (3.1), or directly decomposing n=p^k m with p not dividing m, proves (2.2).

In particular,

    split:   D_p=2A_p-A_p^2,       E_(p,k)=(k+1) A_p^k (I-A_p)^2 B;
    inert:   D_p=A_p^2,           E_(p,2j)=A_p^(2j)(I-A_p^2)B,
                                      E_(p,2j+1)=0;
    p=2:     D_2=A_2,             E_(2,k)=A_2^k(I-A_2)B.

Every identity is for the complete real wave with its fixed phase -3 pi/4. Replacing cosine by one complex exponential is unnecessary and no complex-wave bound is imported.

Summing exact valuations gives the convergent reconstruction

    B=sum_(k>=0) S_k A_p^k C_p B.                            (3.3)

Formally its Euler factor is [(I-A_p)(I-e_p A_p)]^(-1), but (3.3) is justified by the actual disjoint coefficient decomposition and absolute convergence, not by an unproved operator contraction. Products over finitely many distinct primes retain every coprime-to-the-product complement. The coefficient operators commute across distinct primes and hence the multivariate valuation expansion is exact. No positive-density assumption on any complementary residue class is used.

### 3.2 Squarefree classes, harmonics and the actual cutoff

Let sf(n) denote the squarefree kernel in n=d s^2. Define the involution

    tau_p(d)=p d if p does not divide d, and d/p if p divides d,

and eta_(p,a)=identity for even a, tau_p for odd a. Then

    sf(p^a n)=eta_(p,a)(sf(n)).                              (3.4)

For a=2h the harmonic changes from s to p^h s. For a=2h+1 it changes to p^h s when p does not divide d, and to p^(h+1)s when p divides d. This formula includes every valuation of p in s.

For any squarefree-class set A, let B^A restrict the n sum to sf(n) in A. The correctly masked form of (2.1) is

    D_(p^a) B^A
      =S_a A_p^a B^(eta_(p,a)^(-1)(A))
       -e_p S_(a-1) A_p^(a+1) B^(eta_(p,a+1)^(-1)(A)).       (3.5)

Here A and its original cutoff are held fixed when A_p changes T. In particular for A={d>Q}, Q=floor(T^(2/5)), an odd dilation uses precisely

    {squarefree d: p does not divide d and d>Q/p}
       union {squarefree d: p divides d and d>p Q}.          (3.6)

An even dilation uses d>Q. These are strict inequalities with the original integer Q; they are not d>floor((T/p^a)^(2/5)). Any replacement by the latter introduces a real collar which must be estimated. The complementary low classes are obtained by the exact complementary inequalities.

For inert p, any d divisible by p has r2(d s^2)=0. Nonzero inert-prime divisibility therefore shifts harmonics by even valuations within the same radical; it does not generate a new signed family of nonzero radicals. For split p both branches of (3.6) can contribute. The ramified prime has no missing extra character sign.

If the same tau_p is applied to every class in a tuple, distinctness is preserved because tau_p is a bijection. In a mixed prime or mixed parity expansion, the correct indicator is instead

    1_(eta_(p_i,a_i)(d_i) are pairwise distinct).

It cannot be replaced by the untransported distinctness indicator. For example tau_5(13)=tau_13(5)=65. Thus coordinatewise amplification of the accepted E12 creates collision terms. The accepted repeated-class estimate is for the original common-parameter decomposition; applying it to a transported mixed family without returning all masks and parameters is not licensed. Applying completed Hecke identities to the entire original B avoids such omitted terms but then returns (2.4).

### 3.3 Moving radial windows, all tails and absolute costs

The a-fold dilation moves the mollifier parameter to U=T/p^a and the radial window center to S_rad=p^(a/2)T. Therefore S_rad/U=p^(3a/2). The accepted bound for a fixed window r/U in [1/2,2] does not apply uniformly as p grows. Explicitly,

    integral w(R/T)|A_p^a B_T(R)|^12 dR
      =p^(-19a/2) integral w(r/(p^(a/2)T))
                            |B_(T/p^a)(r)|^12 dr.           (3.7)

The factor contains p^(-9a) from twelve amplitudes and p^(-a/2) from the Jacobian. It is incorrect to retain the first while omitting the second, or to declare the last integral a natural moment at T/p^a. Describing it as a natural wave at S_rad instead replaces Psi(t) by Psi(p^(3a/4)t), whose parameter-dependent seminorms also require payment. Equation (2.3) has an analogous off-center first term, with wave parameter pT and radial center T/sqrt(p).

For full unconditional costing, the elementary divisor majorant and Schwartz decay give, for any fixed small eta>0,

    sum_(n>=1) r2(n)n^(-3/4)|Psi(sqrt(n/U))|
       << U^(1/4+eta)                     (U>=1),
       <<_(J) U^(J/2)                    (0<U<=1, J>1/2+2 eta).

The second assertion follows by taking |Psi(x)| << x^(-J) for x>=1 and summing n^(-3/4-J/2+eta). Thus the large-a part of every displayed prime-power expansion converges absolutely; no Schwartz tail or prime power is dropped. For p^a<=T,

    |A_p^a B_T| << T^(1/4+eta) p^(-a),
    M12(A_p^a B_T) << T^(4+12 eta) p^(-12a).                (3.8)

These are pointwise/absolute estimates, so their validity does not depend on the moved window. For p^a>T the second estimate for U gives a summable stronger tail after increasing J. Coefficients S_a grow at most a+1 and are harmless for that convergence. The untouched singleton n=1 is included throughout.

For split p in [P,2P] with 2<=P<=T/2, (2.1) and the same absolute estimates give

    |D_p B_T(R)| << T^(1/4+eta)/P,
    M12(D_p B_T) << T^(4+12 eta) P^(-12).                   (3.9)

This remains valid when p^2>T: use the U<1 bound for A_p^2 instead of pretending it is a natural-parameter wave. For p>T the estimate can be made still smaller using Schwartz decay. Conversely, a small divisible part leaves the coprime part equal to the original wave up to this small part. It is not a bound for B itself.

All dyadic blocks, unequal block interactions, signs of Psi, harmonics, real endpoint parameters, prime 2 and finite/infinite cutoffs are included in these convergent identities and estimates. No individual favorable product scale is selected as representative of the full sum.

### 3.4 Completed amplification and nonbacktracking self-return

Changing n=p m in the first term of (2.3) yields exactly

    sum_(m>=1) r2(p m) m^(-3/4) Psi(sqrt(m/T))
                              cos(2 pi R sqrt(m)-3 pi/4).

The second term is the wave with coefficient e_p 1_(p|m)r2(m/p). Equation (3.2) for a=1 proves H_p=lambda_p B. This proves (2.4) and the rank-one covariance statements. Inert completed rows are identically zero; the p=2 row is B. They do not supply independent amplification signals either.

For completeness, on arithmetic sequences define

    (U_p c)(n)=c(pn),      (V_p c)(n)=1_(p|n)c(n/p),
    mathcal H_p=U_p+e_p V_p.

The actual r2 sequence satisfies mathcal H_p r2=lambda_p r2. Hence any finite polynomial in the commuting distinct-prime operators sends r2 to the scalar obtained by evaluating at the lambda_p. A polynomial whose scalar vanishes kills the target; a polynomial with nonzero scalar returns it. In particular, the local polynomials N_0=I, N_1=mathcal H_p,

    N_(a+1)=mathcal H_p N_a-e_p N_(a-1)

satisfy N_a r2=S_a r2. At split primes the eigenvalue is a+1, corresponding to a double characteristic root 1; at inert primes it alternates between 1 and 0, corresponding to roots 1 and -1. This recurrence provides no decay on the actual coefficient vector.

One must not replace U_p,V_p by two-sided inverses to delete boundaries: U_p V_p=I but V_p U_p is the projection onto p-divisible n. Their difference is the full prime-coprime projection. Such a deletion would discard exactly the complementary owner in (2.2). The polynomial assertion includes these projections; it is not a free-tree heuristic.

For k split primes with all alpha_p=1, the complete twelfth-moment numerator is exactly (2k)^12 M12(B). The inherited estimate therefore has price k^12 T^(10 beta+epsilon); dividing by the amplifier restores T^(10 beta+epsilon). A supposed k^6 twelfth-moment diagonal price contradicts the exact rank-one algebra unless it is proved using an additional bound for the original B. With arbitrary signs the identical conclusion uses |sum alpha_p|, not sum |alpha_p| or sqrt(sum |alpha_p|^2).

This reaches the same self-return obstruction as the completed GAR rows in Round224, now for actual r2 rather than angular symbols. There is no Round224 profile commutator to estimate here because the full r2 identity is exact; there is also no remaining spectral gain. Deleting the valuation correction would create a false gain. The algebra does not provide the signed Mobius/character input absent from Round225, and no better full coefficient-uniform bilinear price is established.

### 3.5 A quantified candidate covariance gate and its full cost

The following formulation isolates the first possible new analytic input without assuming it. Let P be in [2,T/2], let Pcal be a finite set of k>=1 split primes in [P,2P], and set

    C_p=(I-D_p)B_T,
    Csum=sum_(p in Pcal) C_p,
    E=(1/k)sum_(p in Pcal)D_p B_T.

The exact reconstruction is B_T=Csum/k+E. By (3.9) and convexity,

    M12(E) << T^(4+epsilon) P^(-12).                        (3.10)

Define the actual, not phase-insensitive, weighted signed covariance sum

    mathcal C(T,P)=sum_(p,q in Pcal)
          integral w(R/T)|B_T(R)|^10 C_p(R) C_q(R) dR
       = integral w(R/T)|B_T(R)|^10 Csum(R)^2 dR.           (3.11)

Only the total in (3.11) is nonnegative; individual cross terms retain their signs. The reconstruction, |x+y|^2<=2|x|^2+2|y|^2, Holder and Young imply

    M12(B_T) << mathcal C(T,P)/k^2 + M12(E).                (3.12)

Indeed, the error is at most 2 M12(B_T)^(5/6) M12(E)^(1/6), which is absorbed by Young. This proves the sufficiency claim without assuming a bound for the unknown moment in the error term.

For any b in the intended range b>1, a complete new input

    mathcal C(T,P) << k^2 T^(b+epsilon),                    (3.13)

together with P>=T^((4-b)/12), yields M12(B_T)<<T^(b+epsilon). At b=29/25 the exact error threshold is P>=T^(71/300). Epsilon factors can be allocated by starting every coefficient estimate with a smaller epsilon. No estimate for mixed transported windows or radical collisions is required for (3.12), since it reconstructs the original full B.

The inherited information gives only mathcal C << k^2 T^(10 beta+epsilon) when (3.10) is no larger than that bound, using Holder and the triangle inequality. The preferred gate (3.13) therefore requires the power saving T^Delta, Delta=10 beta-29/25. Strict moment improvement merely requires some b<10 beta. Strict pointwise improvement needs b<13 beta-1/2, so it needs a saving larger than

    10 beta-(13 beta-1/2)=1/2-3 beta=0.11310094415... .

The preferred finite milestone then has the packet's pointwise consequence 102/325, not the quarter theorem. These are complete restored powers, not local block gains.

For example, a genuinely proved square-root-prime covariance bound

    mathcal C(T,P) << k T^(10 beta+epsilon)                 (3.14)

would suffice when k>=T^Delta and P>=T^(71/300), with room for epsilon losses. This is a conditional sufficient inequality, not a source result or an asserted count of available primes. Its diagonal terms have the inherited T^(10 beta) size when (3.10) is paid; the missing assertion is the aggregate signed treatment of all off-diagonal pairs. Merely counting k primes does not prove it.

There is a decisive reason not to advertise (3.13) or (3.14) as a newly independent arithmetic theorem supplied by the recurrence: Csum=k(B_T-E). When E is as small as (3.10), (3.13) is quantitatively another expression of the original complete target. The common n coprime to every amplifier prime remains unchanged in every C_p. For signed weights with sum zero,

    sum alpha_p C_p=-sum alpha_p D_p B_T,

so apparent centering deletes the original signal. For nonzero sum the original signal remains. Proving a favorable covariance for a suitably different, genuinely arithmetic row system would be meaningful, but its signed input is absent from the exact prime relations established here.

## 4. First doubtful or unproved step

All finite coefficient identities and complete reindexings above are proved. The first missing step is a signed analytic inequality for the noncompleted rows, such as (3.13), with all p,q and the actual |B_T|^10 weight retained. It must save T^Delta at the preferred gate after paying (3.10); an estimate for only diagonal pairs, only high divisibility, only one radical region, or only a moved natural window is insufficient.

For the completed rows this is even more explicit: their weighted covariance is exactly 4 M12(B_T), so claiming decorrelation would merely assume the desired bound. For nonbacktracking polynomials the same scalar-eigenvector self-return remains. No new independently checkable signed analytic input, source theorem or bound overcoming that return was located or proved in this bounded task. The local identities are therefore not sufficient to launch an analytic campaign.

This is a scoped no-go. It does not rule out a row system using additional angular information, nontrivial signed correlations between different actual spectral pieces, a new complete source estimate, or another arithmetic mechanism. Nor does it show that the conjectured signed integral is large.

## 5. Required controls and outcomes

All mathematical controls here are exact algebraic checks, not numerical evidence for an asymptotic theorem.

1. **Split valuation correction: pass.** For p=5, r2(1)=4, r2(5)=8 and r2(25)=12. The n=5 recurrence is 12=2*8-4. Deleting the p-divisible correction gives the false value 16. More generally at n=p^k the recurrence is 4(k+2)=8(k+1)-4k.
2. **Inert and ramified branches: pass.** At p=3, r2(3)=0, r2(9)=4 and r2(27)=0; the odd valuations vanish but even ones survive. At p=2 every r2(2^k)=4. These falsify deleting all inert powers or imposing the split recurrence at p=2.
3. **Complement/boundary operator control: pass.** U_p V_p=I whereas V_p U_p=1_(p|n) as operators. The discrepancy at n=1 is exactly the missing coprime sector. The singleton survives in every C_p and is carried by every completed H_p.
4. **Actual completed covariance falsifier: pass.** On the actual r2 sequence H_p=2B for every split p. Thus K_pq=4M12(B) even for p not equal q. This directly falsifies any claim that these completed rows become orthogonal just because the primes differ. It does not lower-bound M12(B) beyond what the identity says.
5. **Radical mask and collision control: pass.** At p=5,Q=20, d=13 is below Q but tau_5(d)=65 is above Q; d=65 is above Q but maps to 13 below Q. Both classes have actual nonzero r2 coefficients. Also tau_5(13)=tau_13(5), so mixed-prime dilation need not preserve distinctness. These falsify omitting the collars/collisions.
6. **Window and Jacobian control: pass.** For a=1 the new wave parameter is T/p and its radial center is sqrt(p)T, with ratio p^(3/2), and the twelfth-moment prefactor is p^(-19/2). The original window is therefore not a fixed natural window at T/p. This falsifies applying the inherited moment with uniform constants by a bare substitution.
7. **Full-prime-power/tail and false-analogue scope: pass.** The coefficient sum proof above controls all a, including p^a>T, and all n; signs of Psi were never assumed nonnegative. The no-go uses the exact actual r2 eigenrelation, not a generic arbitrary-sign coefficient statement. The absolute divisor estimates alone would work for adversarial coefficients, and are used only to price errors, never to assert the desired signed cancellation.
8. **Cost restoration: pass as a sufficient implication.** Substitution in (3.10) gives 4-12*(71/300)=29/25 exactly. Equation (3.12) retains the unknown moment in its Holder step and absorbs it correctly; it does not silently bound |B|^10 by a conjectural supremum.

The only decimal arithmetic was evaluation of the already exact beta and these gate differences; it was not a mathematical experiment and no asymptotic conclusion rests on decimals. Analytical/algebraic effort exceeded 95 percent. No external primary source was needed or invoked.

## 6. Dependencies and exact artifacts used

Read only the assigned brief and its permitted contexts. The graph was parsed selectively after an oversized raw read to identify the authoritative target and accepted order-twelve nodes; no sibling report or historical report was consulted. The two supplied synthesis paths already identify Rounds224 and225, so no extra plan metadata or source was needed.

- `protocol.md`, SHA256 `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
- `state/active_campaign.yml`, SHA256 `fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa`; records closed Round230, not a launched Round231.
- `state/proof_obligations.yml`, SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`; used `GC-target`, `M9`, `M9-M1`, `M9-M2`, `GC-complete-square-root-large-values-moment-bound`, and `GC-complete-distinct-radical-twelfth-reduction`.
- `strategy/round231_admission/briefs/split_prime_cancellation.md`, SHA256 `0685714b68334c98d82a8f6045afa1f9fb3e813fc3f169118bf5abcc738bf853`.
- `strategy/round231_admission/briefs/complete_target.md`, SHA256 `6a26238ec9bdf5b7e92cb2278234b316d1bba26ef87b9b75fc5f0a8b5561853c`.
- `rounds/codex-managed/m9-m1-complete-gar-prime-amplification/synthesis.md`, SHA256 `d5a94b25e876714c8e17602a497812afef3b42724a75dd4cc1501583d12fe98f`.
- `rounds/codex-managed/gc-complete-logarithmic-convolution/synthesis.md`, SHA256 `c4324e2b8c75b8cb972ccf6a9e4f762ed9d8d648299acf7df77aff2b9b1546c7`.

The r2 formula comes from the frozen target; (3.1)--(3.14) are derived here. The existing complete moment benchmark and preferred moment-to-pointwise comparison are accepted/context inputs, not new claims. The report has not received independent seam review and is selection evidence only. Its final byte hash is reported to the conductor after writing, rather than inserted self-referentially into the file.

## 7. Recommended state effect

**No change.** Retain the exact identities as unpromoted admission evidence and reject the assertion that this particular completed scalar prime amplifier or its polynomial/nonbacktracking variants yield a new bound merely from their arithmetic eigenrelations. Do not reject the possibility of another signed prime mechanism.

No new complete moment estimate, pointwise exponent, M1/M2/GAR parent, endpoint result, all-order moment family or quarter theorem is proved. No existing graph node is closed or weakened. The task stops with this report; Round231 remains unlaunched. No shared-state, synthesis, validation-matrix, proof-draft or legacy artifact is modified, and no successor is designed.
