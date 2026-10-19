# Round235 conductor candidate: signed sixth-order dispersion

Campaign gc-signed-sixth-dispersion;12 October2026. Starting graph SHA256 dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306. Candidate evidence only; conductor-owned. The frozen objective is an actual signed estimate, not an arbitrary-coefficient or tuple-absolute surrogate.

## 1. Result and proposed scope

The bounded attempt pays the full-band variance reduction, the odd Hankel packet with its complete errors, the small-divisor and square sectors, exact arithmetic grouping, the paired sixth-order contribution, and exact-zero tuples sharing one denominator. It also obstructs the tuplewise absolute grouped-fraction certificate for an actual interior block. It does not prove the required nonpaired signed dispersion estimate. Retain these components as reviewed evidence if the final nonauthor seams pass. Proposed State Patch: identity, with no new complete bound or proof-draft change.

The concrete first gap is a one-sided upper bound for the nonpaired rational-frequency sextuple sum defined in Section3D. It includes nonpaired exact relations as well as near relations. Formal centering, a tuplewise modulus, or replacing the common center by independent centers does not pay that sum.

## 2. Exact actual hypotheses and target

Use the accepted actual real rho,Psi,w,B_T and fixed smoothing convention, with R in the fixed positive radius window R comparable to T. The source-qualified actual ceiling is T^(beta+epsilon), beta=(50sqrt(1717)-297)/13762. Let gamma=13/125, X=T^(52/125), Y=T^(99/125), and eta fixed smooth, zero at and below1, one at and above2, and valued in[0,1]. For large T the transition strips are disjoint; bounded T is absorbed in constants. Put phi(n)=eta(n/X)-eta(n/Y) and

    F(R)=sum_(n>=1) phi(n)r2(n)n^(-3/4)Psi(sqrt(n/T))
                         cos(2pi R sqrt(n)-3pi/4).

This is the complete smooth norm band X<n<2Y. The exact identity B_T=L+F+H uses low coefficient1-eta(n/X) and high coefficient eta(n/Y). The latter includes the whole infinite Schwartz tail. These are the actual coefficients, not arbitrary masks to which the B_T supremum has been transferred.

The sufficient band target is M6(F)<=T^(193/500+epsilon), where M_p uses w(R/T)dR. We do not assert it. Choose a fixed smooth dyadic partition chi(n/N); there are O(log T) active blocks cX<=N<=CY. Write A=sqrt(N) and

    q_N(s)=s^(-1)Psi(sqrt(N/T)s)phi(Ns^2)chi(s^2),
    K_N(u)=integral q_N(s)sin(2pi u s)ds,
    H_N(x)=2sqrt(x)/sqrt(N),
    S_N(x)=sum_(m>=1)r2(m)K_N((x-m)/H_N(x)).

The q_N have common compact support[a,b] in(0,infinity), with uniform derivatives. Every K_N is real, odd, uniformly Schwartz, with Fourier support in[-b,-a] union[a,b]. The stronger blockwise sufficient hypothesis is

    (S6) integral w(sqrt(x)/T)|S_N(x)|^6 dx
             <=T^(2+1/100+epsilon)(T/sqrt(N))^3,

uniformly for all required blocks, real T and transition/endpoints. Set H0=T/sqrt(N); H_N(x) is comparable to H0 and ranges from scale T^(151/250) to T^(99/125). This moving width is retained exactly.

S6 is sufficient for the full-band target. No reverse implication from the full-band M6 bound to every blockwise S6 bound is claimed. At the full-band level only, M6(F) is equivalent to the distinct-six upper bound in Section3A. This narrows the potentially ambiguous phrase 'or equivalently' in Section4 of the frozen bridge report; the report is preserved as written.

## 3. Proof and paid components

### A. All classes, all band harmonics, and complete restoration

Group n=ds^2 by every squarefree d and call the resulting real band functions g_d. The coefficient majorants obey

    |g_d|<=T^epsilon X^(-1/4)d^(-1/2) for d<=X,
    |g_d|<=T^epsilon d^(-3/4) for d>X.

The first line retains the high harmonics of low squarefree classes. Squaring and summing gives V=sum_d g_d^2<=T^epsilon X^(-1/2), including the logarithmic low-d sum. Thus J6=integral w V^3<=T^(47/125+epsilon). Accepted233's finite real-family absorption applies directly to this finite band family. If E6 is the ordered distinct-six product sum and I6 its integral, then for fixed0<delta<1,

    integral w|F^6-E6|<=delta M6(F)+C_delta J6,
    (1-delta)M6(F)<=I6+C_delta J6,
    I6>=-C_delta J6.

Hence the one-sided I6 target at193/500 is equivalent to the M6(F) target. No additive approximation at a smaller absolute error is asserted.

The inherited reviewed high-norm Hankel bound and low-norm coefficient bound give sup|L|,sup|H|<=T^(gamma+epsilon). Applying the accepted coefficient-uniform distribution estimate only after those actual ceilings are established pays each complementary M12 by

    T^epsilon[T+T^(10gamma)+T^(1+20gamma/13)]<=T^(29/25+epsilon).

The exact B_T decomposition then gives sup|F|<=T^(beta+epsilon). Conditional on the band M6 target,

    M12(F)<=sup|F|^6 M6(F)<=T^(6beta+193/500+epsilon).

The strict margin below29/25 is387/500-6beta=0.000201888311263119... . An exact proof is beta<129/1000: both sides of25000sqrt(1717)<1036149 are positive and1036149^2-1717*25000^2=479750201>0. Internal epsilons may be chosen arbitrarily small after the output epsilon and this fixed margin are set. Physical norm inequalities pay every mixed term. Complete M12(B_T) at29/25 and then sharp102/325 would follow, with the accepted source qualifications. Neither conclusion is obtained here. Fixed p12 implies no quarter theorem.

### B. The complete Hankel representation and error budget

The full derivation is in reports/actual_sixth_bridge.md, Sections3.2–3.4. Radial Poisson applied to the actual lattice norm weight has a dual zero mode and all positive dual norms. Retain the two positive-real Bessel terms

    J0(2pi vu)=cos(2pi vu-pi/4)/(pi sqrt(vu))
       +sin(2pi vu-pi/4)/(16pi^2(vu)^(3/2))+O((vu)^(-5/2)).

The two phase products give a positive difference sine in the leading term and a difference cosine in the second. The error is absolutely summable over all nonzero dual lattice vectors only after the second term has been retained. With u comparable to A it costs O(A^(-2)) times the convergent sum of |z|^(-5/2). The dual zero mode costs R^(-2)A^(-3/2). Smooth sum phases and all remote dual tails are arbitrarily small powers after integration by parts.

For the leading term let t=A(R-sqrt(m)) and v=A(R^2-m)/(2R). Then v=t-t^2/(2AR). On sqrt(m) comparable to R, t and v have the same sign and comparable magnitude; the mean-value theorem and uniform Schwartz bounds pay the replacement by the exact moving-width packet. The entire remote tail of both expressions is also bounded. The result is

    F_N(R)=R^(-1/2)S_N(R^2)+E_N(R),
    |E_N|<=T^epsilon[N^(-1)+T^(-3/2)N^(-1/2)
                           +T^(-1/2)N^(-1)+T^(-2)N^(-3/4)].

Thus M6(E_N)<=T^(1+epsilon)N^(-6), whose worst band exponent is−187/125. All norm transitions have uniform derivative bounds; no hard dual cutoff or constant-width approximation is hidden.

The exact Jacobian is

    integral w(R/T)|R^(-1/2)S_N(R^2)|^6dR
       =(1/2)integral w(sqrt(x)/T)x^(-2)|S_N(x)|^6dx.

Consequently S6 gives M6(F_N)<=T^(1+1/100+epsilon)N^(-3/2). The dyadic norm inequality and the already paid errors give M6(F)<=T^(47/125+1/100+epsilon)=T^(193/500+epsilon).

### C. Exact arithmetic grouping, including the cutoff error

For fixed x write R=sqrt(x), H=H_N(x), K=K_N. The independently rederived full progressions are

    P_d=sum_(j in Z)K((x-dj)/H)
       =(H/d)sum_l Khat(lH/d)e(lx/d),
    Q_d=sum_(j in Z)chi4(j)K((x-dj)/H)
       =(H/(2id))sum_k chi4(k)Khat(kH/(4d))e(kx/(4d)).

P_d vanishes for d/H<=1/b; Q_d for d/H<=1/(4b). Equality is allowed because the smooth Fourier profile vanishes at its support endpoints. Restoring j>=1 costs at most C_L[(1+x/H)^(-L)+(H/d)(1+x/H)^(1-L)]; it is not silently zero.

The actual divisor identity is

    r2(m)=4 sum_(d|m,d^2<=m)[chi4(d)+chi4(m/d)]
                   -4 chi4(sqrt(m))1_(m square).

Freeze the divisor range at d<=R while retaining both character branches. The nonsquare discrepancy consists of pairs with both factors<=R or both>R. Their products are at distance at least a constant times R from x; Schwartz decay, H/R<<1 and divisor counting pay their entire contribution arbitrarily rapidly. The square discrepancy is retained explicitly with its sign:

    Qsq(x)=4 sum_d sigma(d,R)chi4(d)K((x-d^2)/H),
    sigma(d,R)=-1 for d<=R, +1 for d>R.

At equality K(0)=0. Pointwise |Qsq|<=C(1+H/R)<=C, uniformly at every square; this alone pays its sixth center integral by O(T^2), smaller than the S6 budget. The sharper bound, where established in the arithmetic report, is not needed for the implication. Positive-index restoration is rapidly small after summing d<=R. Therefore

    S_N(x)=A_N(x)+Qsq(x)+O_B(T^(-B)),
    A_N(x)=4 sum_(d<=R)[chi4(d)P_d(x,H)+Q_d(x,H)].

Let Lchi(U)=sum_(1<=j<=U)chi4(j)/j, whose absolute value is at most1 by alternating odd terms. Group identical nonzero rational frequencies lambda=a/q in lowest terms, q>0, BEFORE any norm. Then A_N=sum_lambda c_lambda(x)e(lambda x), with

    q odd: c_(a/q)=4H chi4(q) Lchi(R/q) Khat(Ha/q)/q;
    4|q:   c_(a/q)=8H chi4(a) Lchi(4R/q) Khat(Ha/q)/(i q);
    q=2 mod4: c_(a/q)=0.

The first family has q<=R; the second q<=4R. Negative a are included, and c_-lambda is the complex conjugate of c_lambda. The coefficients retain the exact sharp x-dependent divisor cutoff and the actual varying H. They are bounded by C H/q on Fourier support aH/q in the fixed two bands. This exact grouping performs real character cancellation among different representations of a fraction; it does not yet estimate the sixth moment across different grouped tuples.

### D. Paid paired sextuples and the exact remaining signed sum

On the Fourier support q>=cH, the number of numerators for a given q is O(q/H); hence

    sum_lambda |c_lambda(x)|^2<=C H sum_(cH<=q<=CT)1/q
                                     <=C H log(2T).

This estimate is pointwise and remains valid despite moving divisor endpoints. Let P6(x) be the contribution of ordered sextuples admitting an opposite-frequency pairing, counted once each. Every such product is nonnegative because c_-lambda=conjugate(c_lambda). The union of the15 possible pairings gives

    0<=P6(x)<=15(sum_lambda |c_lambda(x)|^2)^3,
    integral w(sqrt(x)/T)P6(x)dx<=C T^2 H0^3 log^3(2T).

Define Rnp_N to be the integral of the remaining sextuples, with every original complex coefficient and common phase e(x sum_j lambda_j) retained. Conjugate pairing makes this a real signed number. Then

    integral w(sqrt(x)/T)|A_N(x)|^6dx
                   = integral w(sqrt(x)/T)P6(x)dx+Rnp_N.

For exact-zero sextuples all sharing one reduced denominator q, choosing five numerators fixes the sixth. Their absolute mass is at most C(q/H0)^5(H0/q)^6=C H0/q. Summing q and integrating pays this sector by C T^2 H0 log(2T), including its nonpaired members. It can be removed from Rnp_N with overlap handled explicitly; it is not a bound for mixed-denominator rational relations.

In particular Rnp_N is bounded below by minus the paid paired budget. Its one-sided upper target

    Rnp_N<=T^(2+1/100+epsilon)H0^3

would pay S6, using the square and tail errors. This statement, uniformly over every required actual block, is UNPROVED. It includes exact nonpaired frequency relations; 'off-diagonal' must not be read as 'nonzero frequency'. The natural common-center resolution is T^(-2). Taking absolute values, assuming independent centers, or replacing a congruence by its full-period mean when the modulus exceeds the available interval introduces new unpaid assertions.

The arithmetic report also pays one integration by parts including every moving cutoff. For fixed q, the total jumps of Lchi(R/q) or Lchi(4R/q) over R in[cT,CT] sum in absolute value to O(1): their indices occupy a fixed-ratio interval, or an O(1) initial segment. Thus ||c_lambda||_infinity+Var(c_lambda)<=C H0/q. Smooth factors vary on the T^2 scale. Stieltjes integration by parts yields the valid tuple bound product_j(H0/q_j) min(T^2,1/|sum_j lambda_j|). This is only first-order decay; arbitrary repeated integration by parts would require additional control of the jumps.

### E. Actual obstruction to the grouped tuplewise absolute certificate

Select a genuine interior norm block with phi=1 on the block support and a fixed nonnegative smooth partition cutoff. Such blocks exist between the separated powers X and Y for all sufficiently large T. Since N/T tends to zero, Psi tends uniformly to1 there, so q_N is nonnegative everywhere and uniformly positive on one fixed interval. Choose a small fixed subwindow J of positive w-mass and a positive fraction interval of size comparable to1/H0 whose H(x)-scaled values stay in that positive interval for every x in J. Select odd denominators q in[kappa T,2kappa T] with2kappa<c. These fractions remain active throughout the full radius window, and2/3<=Lchi(R/q)<=1.

There are at least cT^2/H0 reduced fractions in this region. To check this without a distribution theorem, count integer pairs in the resulting trapezoid with q odd and remove common odd prime factors. Their main-area fractions sum to at most sum_(n>=3)1/(n(n-1))=1/2; summed boundary errors O(T log T+(T/H0)log T) are smaller than T^2/H0 since T/H0 grows as a fixed positive power. This establishes the positive lower density.

Let M denote the number selected. Pigeonhole their ordered triple sums in cells of width delta/T^2. There are O(T^2/H0) cells, so at least cM^6/(T^2/H0)>=cT^10/H0^5 ordered pairs of triples differ by at most delta/T^2. For each resulting three-positive/three-negative sextuple, the product of actual coefficients is real with one fixed character sign, or zero, throughout the full radius window. On J its magnitude is at least c(H0/T)^6. Taking delta small enough makes the cosine of the common phase at least1/2 throughout the full window. Hence the modulus of its complete integrated tuple is at least cT^2(H0/T)^6, with no unaccounted negative tail outside J.

The sum of these individual moduli is therefore at least cT^6 H0. Removing paired tuples, whose contribution on this denominator subrange is O(T^2 H0^3), leaves the same order lower bound. This is a lower bound on the tuplewise absolute certificate for the actual grouped coefficients of a full interior block. It is not a lower bound on the signed Rnp_N, on |A_N|^6, on the physical sixth moment, or on a denominator-restricted physical moment. The character signs across different tuples remain available for cancellation.

Its ratio to the desired T^(2+1/100)H0^3 grows at least as a positive constant times T^(4-1/100)/H0^2 throughout the frozen band. Thus taking moduli even after the exact fraction grouping cannot prove S6 at this budget. A uniform S6 theorem would have to treat these actual interior blocks as well as all transitions.

## 4. Independent controls and first gap

The isolated report proves exact signs, different character cutoffs, and uniform positive-index tails. It also proves, for any fixed nonzero kernel in that packet and a constant width, that the sum of absolute six-tuple product integrals over an interval of length L>=C_K H has order LH^6. The signed constant-coefficient packet is nevertheless exactly zero for sufficiently large H. The lower proof controls whole-line correlations and both endpoint tails, including every negative contribution; it also works with six distinct nearby indices. This is an artificial-coefficient certificate obstruction, not an r2 lower bound or a refutation of S6.

The frozen bridge report's two instances of a damaged TeX roman-font escape in the squarefree summation labels are rendering defects only; the index is all squarefree d as defined in its prose and as written here. No claim depends on that font command. Reports are not rewritten after freeze.

The actual unresolved estimate is Rnp_N at the stated signed budget. The paired bound, exact character filter, oddness, and constant mean-zero control do not prove it. A new hypothesis equivalent to or stronger than the desired moment is not recorded as an unconditional gain.

## 5. Shared computations and source check

controls/control_manifest.md records all Wolfram inputs/outputs, independent local exact reproduction, parameters, pass rules and limitations. Exact exponent, hyperbola, phase, coefficient-grouping and finite absorption controls pass. The first Wolfram query's unrelated27/83 expression is explicitly corrected to the actual sharp formula102/325; the grouping call's nonfatal pre-evaluation warning and the failed context request are retained. No numerical asymptotic experiment is evidence.

controls/source_check.md freshly checks the fixed-order positive-real Bessel specialization against [DLMF10.17](https://dlmf.nist.gov/10.17) and its real-axis remainder hypotheses. The actual high-norm bound itself remains inherited reviewed evidence; it is not newly promoted by this attempt. All accepted external pointwise qualifications remain intact.

## 6. Dependencies and review boundary

Proof details are the frozen reports actual_sixth_bridge.md, signed_fraction_dispersion.md and blind_packet_control.md. Exact report hashes are bound in controls/frozen_initial_reports.json before any expanded-context review. Accepted204 and233 provide only their stated distribution/actual-ceiling and finite algebraic mechanisms. The reviewed norm-band ledger supplies the previously proved low/high complementary ceilings. Round234's actual tuple-absolute connected obstruction and the earlier two-attempt upper-tail reassessment remain in force.

Required nonauthor seams: actual bridge/errors/restoration/source; arithmetic grouping/paired sector/remaining gap; blind-control applicability and overall conditional scope. Reviews must bind this candidate's final hash. No graph claim is promoted from mutually supporting reports without these checks.

## 7. Recommended state effect and stop

Retain the new paid sectors and explicit signed owner as reviewed campaign evidence, subject to final review. Close Round235 without complete moment, pointwise or quarter gain. Use an identity State Patch, preserving all402 graph nodes and proof-draft bytes. Do not add another accepted unestimated reduction merely because a new representation has been derived.

A successor, if designed after closure, must attack the signed nonpaired rational sextuples with the exact arithmetic coefficients and moving cutoffs, or supply a different fully costed complete mechanism. Repeating the filter, paying the paired sector again, or estimating tuplewise moduli is insufficient. No successor is launched by this report or by a subagent.
