# Exact residue margins do not exclude a coherent root-wave peak

Round231 prelaunch continuation, 11 October 2026. Conductor derivation, written independently before reading the statement-only report. Frozen graph: a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. Candidate evidence only.

## 1. Result

Even on the actual represented-integer support, preserving the exact coefficient total in each of a sublinear number of prescribed cells does not imply the complete twelfth-moment target. There are bounded nonnegative perturbations of r2, preserving those totals exactly, whose complete real wave has twelfth moment at least a constant times T^(5/2). A smaller-shell version additionally respects the inherited actual pointwise ceiling and attains the retained complete moment exponent 10beta. The coefficients of the actual circle problem are not perturbed by this work: this is a control for the information contained in cell totals, not a counterexample for r2 or the circle conjecture.

## 2. Exact statement

Fix 0<a<b so small that Psi(s)>=p0>0 throughout 0<=s<=sqrt(b). This is possible by continuity and Psi(0)=1. Put I={n integer:aT<=n<=bT}, c_n=r2(n), and v(x)=x^(-3/4)Psi(sqrt(x)). Write C=max v and c=min v>0 on this compact interval. Choose a fixed nondegenerate compact interval J inside (1/sqrt(2),sqrt(3)). Let delta>0 and partition the represented n in I into K<=T^(1-delta) nonempty cells, independently of R.

For all sufficiently large real T there are fixed real numbers d_n, zero outside I, with |d_n|<=r2(n)/2 and sum_(n in cell)d_n=0 for every cell, and a sign sigma in {+1,-1}, such that the complete wave with coefficients r2(n)+sigma d_n satisfies

    integral w(R/T)|B_T^sigma(R)|^12 dR >= c_0 T^(5/2).

The coefficient vector may depend on T and the cell partition; it is held fixed as R varies. Its support is exactly that of r2, and each nonzero coefficient lies between one-half and three-halves of r2(n). All original coefficients outside I, including the entire infinite smoothing tail, are unchanged. This statement does not preserve multiplicativity, integer-valued coefficients, every prefix sum, or arbitrary simultaneous moduli of total partition complexity exceeding the bound on K.

The same construction works for any nonnegative c_n on I with A=sum c_n comparable to T and c_*=max c_n<<_eta T^eta for every fixed eta>0, with any fixed positive bounded v. Only the original full-wave application uses its smooth tail.

## 3. Proof

### Averaged finite-dimensional residual

For R in TJ define z_n(R)=v(n/T)cos(2pi R sqrt(n)-3pi/4). For each nonempty cell C write W_C=sum_C c_n>0 and m_C(R)=W_C^(-1)sum_C c_n z_n(R). The weighted residual energy is

    E(R)=sum_n c_n z_n(R)^2 - sum_C W_C m_C(R)^2
        =sum_C sum_(n in C)c_n(z_n(R)-m_C(R))^2 >=0.

Average in R over TJ, dividing by its length. Elementary integration of exponentials gives, for n!=m in I,

    |Avg cos(phi_n)cos(phi_m)|
      <= C_J [1/(T|sqrt(n)-sqrt(m)|)+1/(T(sqrt(n)+sqrt(m)))]
      <= C_(a,b,J)/(sqrt(T)|n-m|).

For n=m, Avg cos(phi_n)^2=1/2+O(T^(-3/2)). Hence

    Avg sum c_n z_n^2 >= (c^2/2+o(1)) A.

For each cell, the diagonal of Avg (sum_C c_n z_n)^2 is bounded by a fixed multiple of sum_C c_n^2. For its off-diagonal use 2c_n c_m<=c_n^2+c_m^2 and sum_(m!=n, m in I)1/|m-n|<=C log(2T). Therefore, uniformly in the partition,

    Avg (sum_C c_n z_n)^2 <= C_1[1+T^(-1/2)log(2T)] sum_C c_n^2.

After dividing by W_C and summing, Avg sum_C W_C m_C^2<=C_2 K c_*. Fix eta<delta; then K c_* = O(T^(1-delta+eta))=o(A). Thus Avg E>=c^2 A/4 for large T. There exists R0 in TJ with E(R0)>=c^2 A/4.

### Perturbation and its fixed physical width

Define d_n=(4C)^(-1)c_n[z_n(R0)-m_C(R0)] for n in C, and zero elsewhere. This is a single fixed vector. Since |z_n|,|m_C|<=C, it obeys |d_n|<=c_n/2 and each cell sum is exactly zero. Its wave D(R)=T^(-3/4)sum d_n z_n(R) satisfies

    D(R0)=(4C)^(-1)T^(-3/4)E(R0) >=c_3 T^(1/4).

The derivative in R has the bound

    sup_R |D'(R)| <=C_4 T^(-3/4)sqrt(T)sum |d_n| <=C_5 T^(3/4).

Consequently D remains at least c_3 T^(1/4)/2 on a physical interval |R-R0|<=c_6 T^(-1/2). This interval stays in the region w=1 for all sufficiently large T, because J lies strictly inside it. The perturbation alone has twelfth moment at least c_7 T^3 T^(-1/2)=c_7 T^(5/2).

### Actual coefficients and the entire baseline

The elementary disk-area count gives sum_(n in I)r2(n)=pi(b-a)T+O(sqrt(T)+1); inclusive endpoints can change this by at most the same harmless size. The divisor bound gives max_I r2(n)<<_eta T^eta. These verify the finite construction for the actual support.

For the entire original smoothed wave, differentiate its absolutely convergent series:

    sup_R |B_T'(R)| <=2pi sum_(n>=1)r2(n)n^(-1/4)|Psi(sqrt(n/T))| << T^(3/4).

For n<=T, dyadic summation of the area bound proves the estimate. For n>T, the Schwartz bound gives a convergent geometric tail after taking any fixed decay order greater than 3/2. The same argument justifies termwise differentiation. No part of the baseline or its tail is discarded.

At R0 at least one of |B_T(R0)+D(R0)| and |B_T(R0)-D(R0)| is at least |D(R0)|. Select that sign once. Its derivative has the same O(T^(3/4)) bound. A possibly smaller interval of width c T^(-1/2) therefore gives the asserted complete moment lower bound. No pointwise estimate for the actual B is needed.

### Smaller shell: the same obstruction at the inherited ceiling

There is a useful strengthening with a genuinely different scale. Let N=N(T) tend to infinity with N<=T and use integers aN<=n<=bN, choosing fixed a,b as above. Replace v by

    v_(N,T)(x)=x^(-3/4)Psi(sqrt(Nx/T)).

These profiles have uniform positive lower and upper bounds on [a,b]. The proof does not differentiate v in R, so it works uniformly for this family. Assume K<=N^(1-delta). The averaged off-diagonal bound is now C sqrt(N)/(T|n-m|), and the projection loss is at most C K c_*[1+sqrt(N)log(2N)/T]. Since c_*<<_eta N^eta, it is o(N). The same construction gives

    sup |D| <= C N^(1/4),  D(R0)>=c N^(1/4),
    sup |D'|<=C N^(3/4),  M12(D)>=c N^(5/2).

The peak width is N^(-1/2), and R0 remains of order T. Appending the baseline need not preserve that local width: use instead the pointwise convexity identity

    |B+D|^12+|B-D|^12 >= 2|D|^12.

After integrating, one fixed sign has M12(B+sigma D)>=M12(D). Both signs have sup_(R in [T/2,2T])|B+sigma D|<=sup_(R in [T/2,2T])|B|+C N^(1/4).

Now choose N=T^(4beta), where beta is the accepted actual-wave exponent and 0<4beta<1. The retained actual bound sup_(R in [T/2,2T])|B_T(R)|<<_epsilon T^(beta+epsilon) gives, for BOTH perturbed waves,

    sup_(R in [T/2,2T]) |B_T^sigma| <<_epsilon T^(beta+epsilon),

while ONE sign satisfies

    M12(B_T^sigma) >= c T^(10beta).

Thus exact totals in K<=T^(4beta(1-delta)) cells on this shell, the actual represented support, bounded nonnegative coefficient comparison, the untouched complete complement, and the inherited pointwise ceiling together still cannot force a power improvement below 10beta for this coefficient class. Taking epsilon smaller than 10beta-b contradicts any proposed uniform M12<=T^(b+epsilon) for b<10beta. This is not a lower bound for exact r2. It also does not assert preservation of any other arithmetic or distribution hypothesis without checking it.

## 4. First unproved step and scope

The construction is an information-content obstruction. It proves no lower bound for the unperturbed actual moment. In particular the two perturbed coefficient vectors need not satisfy the exact divisor-character identity, Hecke recurrences, or any other unlisted multiplicative constraints. An argument that essentially uses those constraints is not covered. Likewise exact margins for a finite cell partition are not all local-prefix estimates. The smaller-shell consequence imports only the already accepted actual-wave ceiling, with its existing source qualifications; it does not establish a new external theorem. The missing actual arithmetic inequality remains open.

## 5. Controls

Singleton cells force d_n=0. They cannot meet K<=T^(1-delta) along this coefficient class for large T: A<=K c_* would contradict A comparable to T when eta<delta. Empty-support cells are omitted; zero c_n cause no division and remain zero. Boundaries are assigned to one cell, with no double ownership. Nonnegative perturbed coefficients and unchanged zero support follow from |d_n|<=c_n/2. Peak width is in R, not R/T; using width one would give a false power.

As an exact residue application, partition by n mod L, optionally intersecting with H disjoint norm intervals. There are at most LH nonempty cells. If LH<=T^(1-delta), all residue totals in each interval are preserved. Every divisor modulus q|L is also preserved by summing cells. For several moduli use L=lcm(q_1,...,q_k) and pay LH explicitly. This does not assert uniform preservation for all polynomially many moduli at no cost.

All controls are analytical; no numerical experiment certifies this theorem.

## 6. Dependencies and provenance

Protocol, this packet's frozen complete target and isolated finite-cell statement, the prior cross-label complete-target definitions, elementary integration, weighted projection, the disk-area count and divisor bound. The smaller-shell specialization also uses the inherited actual-wave pointwise ceiling recorded in the accepted204/216 kernels and graph; all its source qualifications are retained. The conductor wrote this derivation, including the smaller-shell extension, before reading any current subagent report. The isolated brief covers the first T-sized shell lemma; it does not claim a statement-only proof of the later extension. A statement-only independent proof and nonauthor review are required before retaining this evidence. The previously present local_global_bridge report is separate inherited evidence; none of its formulas is used in this proof.

## 7. Recommended state effect

Retain only after independent and seam review, at reviewed prelaunch evidence level. No graph promotion, complete actual moment improvement, successor round, or conclusion that all local arithmetic methods fail is licensed. The explicit limitation is that sublinear cell totals and bounded perturbation stability alone cannot certify the desired complete estimate.
