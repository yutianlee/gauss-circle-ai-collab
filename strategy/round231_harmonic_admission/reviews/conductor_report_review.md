# Conductor review of the harmonic-pooling reports

Date: 2026-10-11. Admission selection only. Graph SHA256 a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. No graph promotion is made by this review.

## 1. Result

The discovery proof and the statement-only Gram proof both establish the new full harmonic-pooled certificate obstruction from actual inputs. The independent arithmetic report supplies the only substantial input granted in the blind harmonic statement: positive r2-weighted squarefree mass in every fixed shell. All three mathematical reports pass this conductor review. Their conclusions are about the certificate C_harm, not the signed I12 or the complete moment.

## 2. Exact statements and reviewed bytes

- reports/harmonic_pooling_discovery.md, SHA256 d5c56d66442579162bb1440e1b13379439a0583a7afb5b854822c85a3239539e.
- reports/blind_harmonic_pooling.md, SHA256 16af77813be06098cc10ff77c1b176657953024c37ef52873d81f648a6f871f8.
- reports/blind_squarefree_mass.md, SHA256 12aaf0a9fbb03786abd862b3cc2da11cdf25415eafa02851f6f3e7f3087c0267.

The literal functions, ordered distinct squarefree labels, floor cutoff and original real window are in briefs/complete_target.md. Every harmonic and cosine sign precedes each modulus. The conclusion is C_harm(T)>=cT^(5/2) for every sufficiently large real T, with constants depending on fixed data. The isolated harmonic report uses a supplied macroscopic squarefree-mass hypothesis, which the arithmetic report and the conductor's direct union proof discharge. It does not import an unverified density assertion.

## 3. Proof-seam checks

### Arithmetic shell seam

The isolated report correctly uses r2(4m)=r2(m) and r2(p^2m)<=3r2(m) for odd primes, including zero factors. Its interval endpoint formula uses S(b)-S(ceil(a)-1); hence the O(sqrt(b)+1) error is valid even for subunit rescaled intervals. Summing all errors through sqrt(vT) costs O(sqrt(T)log T). The rational prime-square price is at most23/24, leaving a positive constant times T for any fixed width v-u>0. Its explicit threshold is conservative and valid.

The discovery report independently proves a stronger shell asymptotic by convolution. The local h-polynomials are correct: at prime2 and inert primes,1-z^2; at split primes,1-3z^2+2z^3=(1-z)^2(1+2z). Multiplying the local r2/4 series gives its squarefree restriction. Absolute convergence of sum|h(m)|m^(-sigma) for sigma>1/2 follows by comparison with the convergent integer sum of exponent2sigma. For1/2<sigma<1, all three displayed error terms are at most C_sigma x^sigma. The positive Euler product converges absolutely. This stronger asymptotic is valid but unnecessary for the selected minimal proof; no source theorem is being imported.

### Direct harmonic proof seam

The exact factor g_d(s) is bounded by g(s)=product_(p=1 mod4)(2v_p(s)+1). The absence of spurious factors at2 and inert primes matters. The elementary g(h)<=h^(3/4), with g(2)=g(3)=g(4)=1, proves the displayed rational upper bound for sum_(h>=2)g(h)^12 h^(-18). The conductor independently checks it below1/200000. Signs of the higher Psi factors are bounded in absolute value; only the fundamental positive shell is used for normalization.

For H=floor(T^(1/100)), the rank-two inverse gives root uncertainty O((H delta+T^(1/4))/T)=O(T^(-3/4)); there is no missing factor H multiplying T^(1/4), because the first row has entries plus/minus1. The determinant is a nonzero integer. A fixed harmonic vector therefore removes at most M^10 b_max^2. Counting at most(2H)^12 vectors gives T^(28/25+2eta), smaller than T^(3/2) for a sufficiently small fixed eta. Common multiples are exactly plus/minus h epsilon0 and are retained at all h, not discarded.

The entire common-multiple packet is controlled by its arithmetic coefficient tail and |w_hat|<=W, leaving the fundamental near pair positive. For the other bounded vectors, Fourier decay order8 gives T^(-2). For harmonics above H, the uniform Schwartz estimate on d/T>=c supplies |Psi(s sqrt(d/T))|<=C s^(-200)<=C H^(-200); the remaining summable coefficient series Z then gives T^(-2). This last bound does not require an incorrectly stronger estimate for the bare divisor tail. Both are uniform relative to the per-tuple fundamental coefficient product. All omitted terms of each full J_d are therefore paid. The conductor's fixed-H proof reaches the same conclusion with a simpler fixed-tail budget, using this independently discovered arithmetic bound.

### Independent Gram proof seam

The blind report uses a genuinely different mechanism and no discovery context. Its fixed harmonic cutoff H is chosen before selecting six disjoint positive boxes. The finite excluded hyperplanes are proper, so six small boxes away from them exist. On those boxes, the zero formal Fourier coefficient of the squared sixfold product is exactly the product of half the sums of coefficient squares. It is positive independently of all higher-harmonic signs. Every nonzero frequency is separated by gamma sqrt(T), where gamma is fixed after the boxes are chosen. Thus the finite products have a uniform lower L2 norm.

The explicit smooth Fourier approximation on the rescaled interval has dimension O(T^(3/2)). The uniform integration-by-parts estimate is valid for all real frequencies; the Fourier cutoff exceeds twice the maximum frequency, so the remaining Fourier series is uniformly small. The full infinite products are close enough in L2 to retain positive projection energy. This is a per-vector approximation, not an uncontrolled fixed-tail subtraction across every matrix entry.

For the weighted Gram matrix G=G_P+G_perp, both pieces are positive semidefinite and tr(G_P G_perp)>=0. Therefore tr(G^2)>=tr(G_P^2)>=tr(G_P)^2/rank(G_P). The use of |I|^2<=B^12WT|I| converts this Frobenius lower bound into the required absolute-entry sum. This is the indispensable absolute-value step: it does not yield a lower bound on the signed sum. The six positive box masses each contribute at least T^(1/4); together with dimension T^(3/2) and the time factor T, the resulting exponent is5/2.

Overlap subtraction is fully paid. The boxes ensure labels can overlap only in matching coordinates, hence an exact overlap pattern has at most11 distinct variables. For any nonzero integer frequency coefficient, summing the smooth Fourier kernel over that variable is bounded uniformly: consecutive arguments are separated by at least c sqrt(T), even for arbitrarily large harmonic coefficients. Freezing the other variables and retaining the outer T gives T^m. The twelve amplitudes cost T^(-9+12eta); the convergent twelvefold divisor-harmonic series supplies the remaining constant. If every coefficient is zero, all six coordinates overlap and only six variables remain. Thus total overlap is O(T^(2+12eta)+T^(-2+12eta)); eta=1/48 gives O(T^(9/4)), below the main T^(5/2). Restricting to squarefree, noncolliding labels only reduces these upper bounds. The resulting disjoint pairs inject into the requested ordered twelve-tuples.

### Complete target seam

The accepted graph and216 kernel are explicitly twelfth-order. They pay the head15/13 and repeated-class error8beta-1/5, so a new bound |I12|<=T^(b+epsilon) would restore exponent max(b,15/13,8beta-1/5). At b=29/25 this gives the intended finite milestone102/325. No reviewed report proves that upper bound. C_harm>=cT^(5/2) instead rules out using this absolute certificate at any exponent below5/2. It is fully compatible with the accepted complete10beta bound and with a possible stronger signed I12 estimate.

## 4. First unproved step

The remaining issue is signed cancellation across different squarefree-label tuples, or a different representation that retains equivalent cancellation. None of the reports supplies such an estimate. The no-go result cannot be converted into a signed lower bound, a rejection of the conjecture, or a new moment upper bound. A further exact regrouping alone does not satisfy the analytic launch criterion.

## 5. Controls and outcomes

The statement-only Gram derivation discharges the crucial full-pooling interface independently; its supplied shell input is independently proved and checked. The direct proof also has a separately requested nonauthor review. Wolfram's exact rational margins are reproduced locally using integers/fractions; these diagnose algebra and normalization only. No numerical asymptotic claim, new external source, shrinking-shell density assumption, or omitted harmonic is used. All analytical scope checks pass; graph and archive preservation are checked separately at closure.

## 6. Dependencies and independence

The conductor read the exact reports above, protocol, the selectively parsed accepted graph, active230 manifest, next-round plan, accepted216 kernel, earlier norm-tuple admission boundary, and the frozen new briefs. The blind harmonic author received only its statement and protocol, and obtained a different Gram proof. The squarefree author received only its separate arithmetic statement and protocol; it then performs a disclosed nonauthor review of the conductor's full proof. The discovery author received a conductor suggestion after independently reporting its arithmetic-dominance route, but did not use the suggested alternative. No result is decided by agreement or vote; the proofs are checked by distinct mathematical seams.

## 7. Recommended state effect

Retain the full harmonic-pooling obstruction as reviewed admission evidence. Do not launch an analytic Round231 on this positive-certificate premise; do not promote a moment or pointwise gain. Preserve the graph, proof draft, matrix, active closed230 manifest, previous admission packet and all historical rounds. Any future formal promotion of a narrow obstruction is a separate conductor-controlled patch decision. The present user request is fulfilled by testing and adjudicating this exact pooling mechanism, not by manufacturing a successor estimate.
