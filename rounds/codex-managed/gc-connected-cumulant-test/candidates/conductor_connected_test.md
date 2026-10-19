# Actual connected-cumulant test at order twelve

Round234, conductor candidate, 2026-10-12 Asia/Shanghai. Campaign `gc-connected-cumulant-test`. Starting graph SHA256 `dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306`. This report requires nonauthor review. It proposes reviewed evidence and an identity State Patch, not promotion of another unestimated complete target.

## 1. Result

For the literal actual full squarefree-class waves and cutoff below, all disconnected lower correlations together have the SIGNED bound

    |I12-K12| <<_epsilon T^(1+epsilon).                         (C1)

Thus a one-sided upper bound K12<=C_epsilon T^(29/25+epsilon) would give the complete preferred twelfth-moment target. No such upper bound is obtained in this attempt.

The proposed stronger method of taking absolute values of the fully pooled connected correlations fails:

    C_conn=TW sum_d^* |kappa12(d)| >= c T^(5/2).               (C2)

The lower bound includes every harmonic and cosine sign before the modulus. It follows by comparing with the independently reviewed actual full-harmonic certificate and proving that the entire cumulant correction has absolute mass O(T^(9/4+epsilon)). It does not lower-bound K12, I12, or any complete physical moment. Signed cancellation between different label tuples remains essential.

## 2. Exact quantities and hypotheses

Use the fixed real nonnegative radial smooth unit-mass mollifier rho, supported in the unit disk; Psi(s)=rho-hat(s e1), real even Schwartz, |Psi|<=1. Use the fixed nonnegative smooth w supported[1/2,2] and equal1 on[1/sqrt(2),sqrt(3)]. Put W=integral w>0. For every real T>=2 let

    a_n=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    f_d(R)=sum_(s>=1)a_(ds^2) cos(2pi R s sqrt(d)-3pi/4),
    Q=floor(T^(2/5)), Z=sum_(squarefree d>Q) f_d,
    dnu_T(R)=w(R/T)dR/(TW).

The star means ordered, pairwise distinct squarefree d_1,...,d_12>Q. For S a nonempty set of positions define

    m_S(d)=E_nu product_(j in S) f_(d_j),
    kappa12(d)=sum_(pi partition[12]) c(pi) product_(C in pi)m_C(d),
    c(pi)=(-1)^(|pi|-1)(|pi|-1)!,
    I12=TW sum_d^* m_[12](d), K12=TW sum_d^* kappa12(d).

These are joint cumulants defined by their finite partition formula; no probability independence hypothesis is made. The distinct-label inclusion-exclusion coefficients later in this proof are DIFFERENT: mu(sigma)=product_(A in sigma)(-1)^(|A|-1)(|A|-1)!. All statements fix order12 before T. Epsilon bounds mean for every positive epsilon, with constants depending on it and the fixed functions. All infinite series converge absolutely for each fixed T, uniformly in R.

## 3. Derivation

### A. Absolute coefficient tails and smooth low correlations

Let S_T=sum_n |a_n|. The elementary divisor bound and Schwartz decay give S_T<<_epsilon T^(1/4+epsilon). For P=T^(3/2), any fixed A and fixed product order q, the coefficient sum over n>P is O_A(T^(-A)); choose the Schwartz decay exponent as large as needed. Removing products with any n>P consequently changes any sum of absolute normalized correlations of order q by O_A(T^(-A)), after the other q-1 coefficient sums are paid. The norm cutoff is only a proof device; the targets retain their full tails.

Write

    A_q=sum_(ordered distinct squarefree d_1,...,d_q>Q)
                 |E_nu product_j f_(d_j)|.

Smoothness gives |E_nu e(lambda R)|<=C_L(1+T|lambda|)^(-L). For q=1 every norm frequency has magnitude>=1. For q=2, different squarefree labels force different norm integers n!=m in every harmonic pair. For n,m<=P,

    |sqrt(n)-sqrt(m)| >= 1/(2sqrt(P));

the plus frequency is larger. Thus T|lambda|>=T^(1/4)/2 in every retained cross-class pair. Arbitrarily many integrations by parts, the finite coefficient mass, and the already paid tail prove

    A_1+A_2 <<_A T^(-A) for every fixed A.                    (C3)

No diagonal n=m is discarded from a quantity that contains it: it is absent precisely because the two squarefree labels are distinct. This is small cross-correlation under smooth radius averaging, not independence of the full family.

### B. Absolute block bounds

For every fixed q>=3,

    A_q <<_(q,epsilon) T^(max(q/4-1,0)+epsilon).               (C4)

Expand each harmonic and sign, then apply the triangle inequality only for this upper bound. Dropping class restrictions enlarges the positive sum. Split n_j into dyadic intervals n_j~N_j, choose N=N_j maximal, and freeze the other q-1 norm variables. Along the remaining integer variable, successive values of T(sqrt(n)+alpha), with either sign, are separated by at least cT/sqrt(N). A separated sequence satisfies

    sum_(n~N)(1+T|sqrt(n)+alpha|)^(-L)
                     <=C_L(1+sqrt(N)/T), L>1,

uniformly in alpha. Coefficients on this block obey

    |a_n|<=C_(eta,J) n^(-3/4+eta)(1+n/T)^(-J).

Therefore the block contributes at most

    C [product_j N_j^(1/4+eta)] N^(-1)
                  (1+N/T)^(-J)(1+sqrt(N)/T).                (C5)

For N<=T, use product N_j<=N^q. The bound is N^(q/4-1+q eta) times a bounded spacing factor. For N>T the displayed Schwartz factor makes the dyadic sum no larger than the same estimate at scale T, after choosing J>q/4+q eta+2. Summing the smaller blocks and the maximal scale costs only finite logarithmic factors, absorbed by choosing eta sufficiently small. For q=3 the exponent q/4-1 is negative, so the small scales contribute O(T^epsilon); for q=4 the scale sum is logarithmic. This proves (C4) with every dyadic norm and the infinite tail. There is no assumed near-resonance density law.

### C. Signed mixed-radius collision bound

Fix a proper partition pi whose block sizes q_b all lie between3 and9. Introduce one independent radius R_b with law nu_T for each block. Its signed distinct-label sum is

    S_pi=E_(nu^k) sum_d^* product_(positions j) f_(d_j)(R_(b(j))).

For a finite label family, inclusion-exclusion on equality partitions sigma gives

    S_pi=E_(nu^k) sum_sigma mu(sigma)
             product_(A in sigma) U_A,
    U_A=sum_d product_(j in A) f_d(R_(b(j))).                 (C6)

The identity follows by grouping assignments by their equality classes: the sum of permutation signs on any class of size>=2 vanishes, while a singleton contributes1. If |A|=1 then U_A=Z(R_b). If |A|=h>=2 and m_b positions of A belong to block b, generalized Holder over d gives

    |U_A| <= product_b (sum_d |f_d(R_b)|^h)^(m_b/h)
           <= product_b V(R_b)^(m_b/2),
    V(R)=sum_(d>Q) f_d(R)^2.                                (C7)

The full actual amplitude bound from accepted216/233 gives V<=sum_d A_d(T)^2<=H^2 with a T-independent H; indeed it gives the sharper Q^(-1/2+eta). Let s_b(sigma) count singleton positions of sigma in block b. Taking absolute values AFTER (C6), each term is bounded by

    |mu(sigma)| H^(12-sum_b s_b)
                         product_b E_nu |Z|^(s_b).           (C8)

Here s_b<=q_b<=9. Accepted216 Section3 equation(D10), including r=0,1, shows E_nu |Z|^r<<_epsilon T^epsilon for every integer0<=r<=9: (r-2)beta<1 in this range. The normalization TW is essential. Since the number of position partitions is fixed, (C8) proves |S_pi|<<T^epsilon after allocating a sufficiently small epsilon to each input. Uniform absolute coefficient convergence for each fixed T justifies all countable limits; the moments of finite partial Z converge to the actual moments by domination. The bound is independent of the number of labels. It is not a bound for the sum of the absolute values of individual tuple contributions.

### D. Pay the signed disconnected sum and compare certificates

In I12-K12 only proper partitions occur. If a partition has a singleton or a pair, (C3) pays its entire sum absolutely at every negative power, even using the crude polynomial bound S_T for all other factors. Every other proper partition of12 has all blocks between3 and9, and its signed sum is paid by (C8). Multiplication by TW proves(C1).

For the absolute correction use(C4) instead. After the same rapid singleton/pair removal, the only possible proper block shapes and outer exponents are

| Block sizes | 1+sum max(q_b/4-1,0) |
|---|---|
|9,3|9/4|
|8,4; 7,5; 6,6|2|
|6,3,3|3/2|
|5,4,3|5/4|
|4,4,4; 3,3,3,3|1|

The coefficients c(pi) are fixed. Dropping the cross-block distinctness constraint only when bounding a NONNEGATIVE sum permits factorization into product A_(q_b). Thus

    TW sum_d^* |m_[12](d)-kappa12(d)| <<T^(9/4+epsilon).       (C9)

The actual full-harmonic lower certificate previously proved and independently reviewed is

    C_harm=TW sum_d^* |m_[12](d)| >=c_0 T^(5/2).              (C10)

It is reviewed admission evidence, not an accepted graph node. The exact proof used here is the independent Gram proof in `strategy/round231_harmonic_admission/reports/blind_harmonic_pooling.md`, together with the squarefree shell mass proof in Section3A of that packet's `conductor_harmonic_obstruction.md`. Their relevant seams are re-audited in this round.

For clarity, the main ingredients of(C10) are these. On each of six disjoint fixed intervals d~T, elementary square-divisor removal gives sum_(squarefree d)r2(d)>=cT. The explicit union fraction is at most1/4+3(1/9+1/8)=23/24, with O(sqrt(T)log T) error. Normalize h_d=f_d/(r2(d)d^(-3/4)); its full harmonic l1 norm is bounded by sum_s tau(s^2)s^(-3/2). Choose a fixed harmonic cutoff preserving a positive norm and choose six small frequency boxes avoiding all finitely many nonzero relations with coefficients up to twice that cutoff. Sixfold products g_q of these full h_d retain cT projected squared norm in a subspace of dimension O(T^(3/2)). This subspace is supplied by ordinary Fourier approximation on the scaled radius interval; the fixed harmonic tail is paid per vector before forming the Gram matrix.

With weights a_q=product_j r2(d_j)d_j^(-3/4), sum_q a_q>=cT^(3/2). The positive semidefinite Gram inequality tr G^2>=tr G_P^2>=(tr G_P)^2/dim(P), together with |<g_q,g_q'>|<=CT, yields sum_(q,q')a_qa_q'|<g_q,g_q'>|>=cT^(5/2). Repeated labels across the two six-tuples cost O(T^(2+epsilon)): at most eleven free label variables, one-variable square-root spacing, all twelve coefficient factors T^(-3/4+eta), and all harmonics summed by the convergent majorant. If every combined frequency coefficient vanishes, only six free labels remain and the cost is smaller. Removing these tuples retains(C10). This proof works for all sufficiently large real T, sign-changing higher Psi coefficients and all infinite harmonics. It does not subtract a fixed per-tuple tail after summing all pairs.

The triangle inequality |kappa|>=|m|-|kappa-m|, summed and multiplied by TW, combines(C9),(C10) to prove(C2), choosing epsilon<1/4. This transfer is valid for the actual cumulants; merely reusing an unmodified coefficient-norm barrier would not suffice.

### E. Complete conditional restoration

By(C1), one-sided K12 at29/25 is equivalent to one-sided I12 at29/25. Accepted216 then restores the actual tail moment, complete B_T and all sharp-circle errors: the head costs T^(15/13+epsilon), and the repeated-class error costs T^(8beta-1/5+epsilon). Both are below29/25. The sharp moment and inclusive-count persistence yield pointwise exponent(7+29/25)/26=102/325. This remains CONDITIONAL because the signed K12 estimate is absent. The fixed twelfth moment would not prove quarter. Accepted233's sufficient unbounded-fixed-order signed family remains a separate open target.

## 4. First unproved step

The missing estimate is precisely the one-sided bound for the actual sum K12 over all distinct class tuples at T^(29/25+epsilon). Subtracting disconnected correlations does not prove cancellation between those tuples. Smooth pair decorrelation and the independent-radius collision argument pay only D12. The absolute connected-cluster route is refuted by(C2), while a genuinely signed connected argument is not refuted. No improvement on the accepted complete exponent10beta or qualified pointwise benchmark is obtained.

## 5. Controls

- All means and cumulants use probability nu_T; the unique outer factor TW is restored in every target and exponent table.
- The rapid pair statement excludes equal squarefree classes; self-pairs and their harmonics are retained in collision factors V, never asserted small.
- The two partition coefficient systems c(pi) and mu(sigma) are distinct; the former depends on number of blocks, the latter on their sizes.
- Countable limits are justified by full absolute coefficient convergence for fixed T; no T-uniform l1 bound is assumed.
- A balanced constant family x_d=+/-1/sqrt(N), with N/2 of each sign, has V=1 and Z=0. For any fixed block partition, its signed distinct12 sum is12! binom(N/2,6)/N^6=O(1), while its tuple-absolute sum is(N)_12/N^6, growing as N^6. This diagnoses the invalid signed-to-absolute swap. These artificial variables are not actual circle coefficients. Their joint cumulant is zero, so this control alone would NOT establish(C2).
- Exact Wolfram checks at orders2..12 compare partition multiplicities with built-in cumulants; all eight proper block shapes and coefficients are checked. Independent local rational/polynomial recurrence reproduces them, plus two six-position mixed-radius identities and balanced constant controls. All pass; they are diagnostic only.

## 6. Dependencies and provenance

The active manifest and frozen interface; accepted204 complete distribution/moments; accepted216 definitions, actual cutoff lower moments(D10) and complete restoration; accepted233 variance, full convergence and fixed-order distinction; the re-audited prior full-harmonic Gram proof and its elementary squarefree shell input. No new external theorem is imported. Wolfram's documentation was used only to select a symbolic check; its computed finite identities are independently reproduced locally. Initial reports are independently frozen before cross-review. Exact hashes are recorded in the round manifests and reviews.

## 7. Recommended state effect

Retain(C1),(C4),(C9),(C2) as reviewed evidence after all seams pass. Close this bounded connected-correlation test without complete gain. Use an identity State Patch; keep all402 accepted graph nodes and the proof draft byte-for-byte unchanged. Future use of cumulants must retain cross-tuple signed cancellation and provide an actual new estimate; another finite partition identity or a claim of approximate independence is insufficient. Do not launch a successor within this report.
