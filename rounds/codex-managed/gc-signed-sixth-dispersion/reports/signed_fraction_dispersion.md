# 1. Result: paid square and paired sectors; signed sextuple dispersion remains open

Campaign `gc-signed-sixth-dispersion`; Round235; task `signed_fraction_dispersion`; role discovery; selected-context, nonblind claimant. Generated 2026-10-12, Asia/Shanghai. Starting graph SHA256 `dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306`. This is candidate evidence, not accepted graph mathematics. Effort was analytical/algebraic apart from file/hash operations; the conductor owns the shared exact diagnostics.

The actual odd packet admits an exact, quantitatively paid divisor-to-fraction reduction. BOTH character branches survive, on disjoint reduced denominator classes: odd denominators and denominators divisible by4. The signed square correction has sixth integral O(T H0), where H0=T/sqrt(N). All other hyperbola-freezing errors are arbitrarily small powers of T. The grouped coefficient square-sum is O(H0 log T), so every completely paired rational sextuple is paid at O(T^2 H0^3 log^3 T). All exact-zero sextuples with a single reduced denominator are also paid, at O(T^2 H0 log T).

These statements do not prove S6. The remaining term is the signed, nonpaired six-fraction integral, including its exact rational resonances. Its coefficients, radius dependence, true resolution T^(-2), and a valid bounded-variation integration estimate are displayed below. Replacing it by its tuplewise absolute certificate fails badly: for an actual interior block with a nonnegative partition cutoff, a balanced-six absolute certificate is at least c T^6 H0. This is a scoped obstruction to taking moduli after grouping, not a lower bound for the signed physical moment and not a refutation of S6.

# 2. Exact statement and hypotheses

Use the actual rho,Psi,w,eta and norm band in `actual_interface.md`. Write R=sqrt(x), x in [c^2 T^2,C^2 T^2], with fixed 0<c<C, and

    N between fixed multiples of T^(52/125) and T^(99/125),
    H(x)=2sqrt(x)/sqrt(N), H0=T/sqrt(N).

Thus H is comparable to H0 and H0/T=1/sqrt(N) is a negative power of T. Choose a fixed smooth nonnegative dyadic partition chi on positive norm arguments. For a particular block put

    q_N(s)=s^(-1) Psi(sqrt(N/T)s) phi(Ns^2) chi(s^2),
    K(u)=integral_0^infinity q_N(s) sin(2pi u s) ds.

There are fixed 0<a<b such that supp(q_N) is contained in [a,b], with every derivative uniformly bounded over the required real parameters and transition blocks. The kernel is real odd Schwartz, with the exact Fourier convention

    Khat(xi)=q_N(xi)/(2i) for xi>0,
    Khat(xi)=-q_N(-xi)/(2i) for xi<0,
    Khat(0)=0.

In particular Khat is supported where a<=|xi|<=b. No positivity of K is assumed. Define the actual arithmetic packet

    S(x)=sum_(m>=1) r2(m) K((x-m)/H(x)).                    (2.1)

All identities in this report first hold at each fixed x,T,N as absolutely convergent sums. Constants can depend on fixed supports and seminorms. For every A>0, uniformly in the real center x,

    S(x)=P(x)+Q(x)+O_A(T^(-A)),                            (2.2)
    Q(x)=4 sum_(d>=1) sigma_R(d) chi4(d) K((x-d^2)/H(x)),
    sigma_R(d)=-1 if d<=R, +1 if d>R.

At an equality d=R the convention is immaterial because K(0)=0. The full-progression term is

    P(x)=4 sum_(1<=d<=R) sum_(k in Z)
                 [chi4(d)+chi4(k)] K((x-dk)/H(x)).         (2.3)

Let Lchi(U)=sum_(1<=l<=U)chi4(l)/l, with the empty sum zero. For reduced nonzero fractions lambda=a0/q, q>0, define

    c_lambda(x)=4H(x) chi4(q)/q Lchi(R/q) Khat(H(x)lambda),
                            if q is odd;                 (2.4a)
    c_lambda(x)=8H(x) chi4(a0)/(i q) Lchi(4R/q)
                            Khat(H(x)lambda), if 4|q;     (2.4b)
    c_lambda(x)=0,           if q=2 mod4.

Then

    P(x)=sum_lambda c_lambda(x)e(lambda x),
    c_(-lambda)=conjugate(c_lambda).                       (2.5)

Only q<=R in (2.4a), q<=4R in (2.4b), and a/H(x)<=|lambda|<=b/H(x) contribute. Consequently q>=H(x)/b and all contributing fractions belong to one fixed finite set with q<=4CT and |a0|<=C1 q/H0. No zero fraction contributes.

The proved budgets are

    integral w(sqrt(x)/T)|Q(x)|^6 dx << T H0,               (2.6)
    sum_lambda |c_lambda(x)|^2 << H0 log(2T),              (2.7)
    absolute paired-six contribution << T^2 H0^3 log^3(2T), (2.8)
    absolute same-denominator exact-zero contribution
                                      << T^2 H0 log(2T).  (2.9)

The remaining signed integral D_np is defined by expanding P^6 and retaining the ordered tuples that cannot be partitioned into three opposite-frequency pairs. Equations (2.6)--(2.9) leave its desired one-sided upper bound

    D_np <= C_epsilon T^(2+1/100+epsilon) H0^3             (2.10)

unproved. A bound of this size for D_np, together with the paid terms, implies S6; none of (2.2)--(2.9) alone implies it.

# 3. Proof and derivation

## 3.1. Exact two-branch hyperbola and all freezing errors

For every positive integer m,

    r2(m)/4=sum_(d|m,d<=sqrt(m))[chi4(d)+chi4(m/d)]
                                      -1_(m square)chi4(sqrt(m)). (3.1)

This follows by pairing complementary divisors, subtracting the duplicate central divisor at a square. Therefore

    S(x)/4=sum_(d>=1)sum_(k>=d)[chi4(d)+chi4(k)]K((x-dk)/H)
                                  -sum_d chi4(d)K((x-d^2)/H).

Compare the nonsquare terms with (2.3). When d<=R and 1<=k<d, one has dk<=d(d-1)<=R^2-R. When d>R and k>d, one has dk>=d(d+1)>R^2+R. Thus EVERY wrongly included or omitted nonsquare positive-product term is at distance at least R from x. Its multiplicity is bounded by a constant times tau(m), not by an unproved estimate for the number of relevant d. The square terms give exactly Q.

For m comparable to x, the omitted nonsquare absolute tail is at most

    C_(B,epsilon) T^epsilon H (H/T)^(B-1),                (3.2)

by the divisor bound and summation of (1+|m-x|/H)^(-B). The ranges m<x/2 and m>2x are bounded in the same way with |m-x| comparable to x+m; their complete infinite sums converge when B is sufficiently large. Because H/T<<T^(-26/125), choosing B in terms of any requested A makes all these terms O_A(T^(-A)).

The extension to k<=0 in the full progression is also paid. For each d<=R,

    sum_(k<=0) |K((x-dk)/H)|
       << (1+x/H)^(-B)+(H/d)(1+x/H)^(-B+1).

Summing d gives at most O(T(1+x/H)^(-B)+H log(2T)(1+x/H)^(-B+1)), again arbitrarily small. Here chi4(k) is its usual periodic extension to all integers, including chi4(0)=0; the chi4(d) part at k=0 has been retained in this estimate. These arguments prove (2.2) with all tails, all real endpoints, and the exact floor convention d<=R.

For Q, the squares in d comparable to T have separation comparable to T, while H<<T. The Schwartz grid bound gives

    sum_d |K((x-d^2)/H)|<<1,
    integral_(c^2 T^2)^(C^2 T^2)
              sum_d |K((x-d^2)/H(x))| dx << T H0.         (3.3)

For the second assertion, replace H(x) by a comparable constant H0 in a Schwartz majorant, integrate each central d over x at cost O(H0), and note that O(T) central squares occur. The complete far-d tails are arbitrarily small by the same Schwartz summation. Since the first majorant is bounded, its sixth power is bounded by a constant times itself. This proves (2.6), including centers arbitrarily close to, and exactly at, squares. No square term was declared zero except its exact leading value at its own center.

## 3.2. Compact-frequency filtering and the character phases

Poisson summation in k, for each fixed real x and its actual width H(x), gives

    sum_(k in Z)K((x-dk)/H)
       =(H/d)sum_(h in Z)Khat(Hh/d)e(hx/d),              (3.4)

and the exact identity chi4(k)=[e(k/4)-e(-k/4)]/(2i) gives

    sum_k chi4(k)K((x-dk)/H)
       =H/(2i d) sum_(h in Z) [
          Khat(H(h+1/4)/d)e((h+1/4)x/d)
         -Khat(H(h-1/4)/d)e((h-1/4)x/d)].              (3.5)

These formulae are valid with H changing with x; no integration or differentiation in x was used. The first progression vanishes identically if d<H/b, and the character progression vanishes if d<H/(4b). The zero Fourier mode in (3.4) vanishes because Khat(0)=0. The second progression has no zero mode in the first place. Endpoints where Hh/d meets the support boundary are handled by the actual smooth Khat, not by an approximate count.

For (3.4), write h=la0,d=lq. Complete multiplicativity of chi4 gives (2.4a). Even q vanish. For (3.5), write 4h+delta=g a0 and 4d=gq, delta in {1,-1}. The reduction gcd implies g is odd and 4|q, with d=gq/4. The original sign is delta=chi4(g a0)=chi4(g)chi4(a0), yielding the factor 8H/(i q) in (2.4b). Thus q=2 mod4 does not occur, and the two character branches do not merge into one unsigned divisor coefficient.

The series Lchi consists of the alternating odd harmonic series. For U>=1,

    2/3<=Lchi(U)<=1,                                      (3.6)

and it is zero for U<1. In particular the multiplicity grouping is bounded with no logarithmic loss. For lambda>0 the two coefficients are, explicitly,

    c_lambda=-2i H chi4(q) q_N(Hlambda)Lchi(R/q)/q       (q odd),
    c_lambda=-4H chi4(a0) q_N(Hlambda)Lchi(4R/q)/q       (4|q). (3.7)

The first branch is imaginary and odd in lambda; the second is real and even. This checks the signs, reality, and the character information that remains available for a genuine signed argument.

## 3.3. Paid paired sector and a rational main sector

There are O(q/H0+1)=O(q/H0) possible contributing numerators for each q, since q>=c1 H0. Equations (2.4) and (3.6) give |c_lambda|<<H0/q. Therefore

    sum_lambda |c_lambda|^2
      <<sum_(c1 H0<=q<=4CT)(q/H0)(H0/q)^2
      <<H0 log(2T),

proving (2.7). For each of the15 pair partitions of six positions, the absolute sum of products with lambda_i=-lambda_j in each pair is at most (sum|c_lambda|^2)^3. The union of paired configurations is bounded by their sum, with harmless overcounting. Integrating over length O(T^2) proves (2.8), with the actual moving coefficients retained.

If all six reduced denominators equal q and their frequencies sum exactly to zero, fixing five numerators fixes the sixth. Their number is O((q/H0)^5). The absolute coefficient mass is consequently

    O((q/H0)^5(H0/q)^6)=O(H0/q).

Summation over q and integration prove (2.9). This includes nonpairing rational zero relations within one denominator. It is not a bound for all rational zero relations across different denominators. One can use the union of this sector and the paired sector and subtract the overlap, or simply retain the displayed upper bounds; no signed positivity inference is needed.

## 3.4. Moving coefficients, true resolution, and the exact unproved owner

Extend (2.4) by zero to a fixed finite fraction set containing every active fraction on the whole x window. Each coefficient is a piecewise smooth bounded-variation function of x. For a fixed denominator q, Lchi(R/q) jumps by chi4(l)/l only when R=lq. Over cT<=R<=CT, the total absolute jump size is O(1): if many jumps occur, their indices lie in a fixed-ratio interval and sum 1/l=O(1); if the lower endpoint is below1, q is comparable to T and only O(1) jumps occur. The same argument applies to Lchi(4R/q).

The smooth factors H and Khat(Hlambda) have total variation O(H0/q) after the coefficient normalization, because H'=H/(2x), |Hlambda| is uniformly bounded where relevant, and x ranges over a fixed multiple of T^2. Hence

    ||c_lambda||infinity+Var(c_lambda)<<H0/q.             (3.8)

Multiplying six such factors and the smooth window, and applying Stieltjes integration by parts, proves for Lambda=sum_j lambda_j,

    |integral w(sqrt(x)/T) product_j c_(lambda_j)(x)
                       e(Lambda x) dx|
       << product_j(H0/q_j) min(T^2,1/|Lambda|),          (3.9)

with min(T^2,infinity)=T^2 at Lambda=0. This is a valid, PAID oscillatory bound including every cutoff jump. It does not give arbitrary powers of (1+T^2|Lambda|)^(-1); such powers would require additional treatment of the moving jumps. The true frequency resolution is T^(-2), not H0^(-1) or T^(-1).

The exact remaining owner is

    D_np=sum_(ordered nonpaired lambda_1,...,lambda_6)
           integral w(sqrt(x)/T) product_j c_(lambda_j)(x)
                             e(x sum_j lambda_j) dx.    (3.10)

Every exact nonpairing rational zero relation remains in (3.10), except those one elects to remove using (2.9). The sum is real after conjugate tuples are combined. A signed upper bound (2.10) is sufficient because P is real and P^6>=0. There is no derivation of (2.10) here. In particular, (3.9) followed by termwise moduli is not a substitute.

## 3.5. Scoped failure of the absolute fraction certificate

Here is a quantitative control on that last temptation. Choose a genuine interior norm block, with phi=1 on its support, and a nonnegative smooth partition function nonzero on an interval. Since N/T tends to zero, Psi(sqrt(N/T)s) tends uniformly to1 on its fixed support. Thus q_N is nonnegative and bounded below by a positive constant on a fixed subinterval, uniformly for large T. Choose a small fixed subwindow J of positive w-mass, of length comparable to T^2, and an interval of positive fractions lambda in [a1/H0,b1/H0] such that q_N(H(x)lambda)>=c2 for x in J. Choose odd q in [kappa T,2kappa T] with 2kappa<c, so the q-odd branch is active over the entire radius window.

There are M>>T^2/H0 distinct reduced fractions in this region. An elementary proof counts all integer pairs (a0,q) in the indicated trapezoid with q odd, then excludes common odd prime factors. For a common odd factor p the main area is 1/p^2 of the original count; the sum over odd primes is at most sum_(n>=3)1/(n(n-1))=1/2. The summed boundary errors are O(T log T+(T/H0)log T), since p<=C T/H0. They are o(T^2/H0), as T/H0 is a fixed positive power of T. This yields the claimed lower count without an imported distribution theorem.

Partition the range of the ordered triple sums lambda_1+lambda_2+lambda_3 into intervals of length delta/T^2, where delta>0 is a sufficiently small fixed constant. There are O(T^2/H0) cells. Cauchy--Schwarz on their occupancy gives at least

    c M^6/(T^2/H0) >> T^10/H0^5                          (3.11)

ordered balanced sextuples with

    |lambda_1+lambda_2+lambda_3-lambda_4-lambda_5-lambda_6|
                                                        <=delta/T^2.

For each such tuple use three positive and three negative fractions in (2.5). By (3.6)--(3.7), the product of their coefficients has a fixed real sign determined by the six chi4(q)'s, and its absolute size on J is at least c(H0/T)^6. It has that same sign or is zero elsewhere because q_N>=0 and Lchi>=0. Choose delta so small that cos(2pi x Lambda)>=1/2 throughout the full x window. Therefore the modulus of the actual integrated tuple is at least cT^2(H0/T)^6. Summing gives

    sum_(balanced tuples) |integrated actual tuple|
                                      >> T^6 H0.         (3.12)

The completely paired tuples number only O(M^3) in this selected set and have total upper bound O(T^2 H0^3); removing them leaves (3.12). The result applies to the explicitly stated absolute tuple certificate, including a large nonpaired portion. It is not a positive lower bound for D_np, P^6, S6, or a moment of an artificially restricted denominator family. Other tuple contributions can have either sign, and taking the modulus separately erases exactly that cancellation.

The ratio of this absolute certificate to the desired T^(2+1/100)H0^3 is at least a constant times T^(4-1/100)/H0^2, a positive power throughout the frozen band. Thus this particular certificate cannot establish S6. The paid diagonal is useful but exceptionally small compared with the absolute nonpaired mass.

## 3.6. CRT does not provide the missing common-center average

For fixed residue conditions t=a_j mod d_j, compatibility gives one residue class modulo L=lcm(d_1,...,d_6), and exact interval counting gives length/L+O(1). The O(1) is indispensable unless an additional averaged discrepancy theorem is proved. For six active d_j of size comparable to T, L can be of order T^6, whereas the center interval has length only O(T^2). Including chi4 changes the period to a divisor of lcm(4d_1,...,4d_6), not to a small modulus.

At the level of an unweighted divisor expansion there are O(T^6) sextuples before any short-shift choices, so summing even one O(1) discrepancy per sextuple already costs O(T^6), above T^(2+1/100)H0^3 for every required H0. Additional shift sums or partial periods must be paid, not suppressed. This count is a price of that certificate, not a claim that every actual discrepancy attains1. A complete-period average has an error of order its full period times the integrand bound, also unusable at period T^6 on an interval T^2. Compact Fourier filtering removes individual small progressions, but it does not turn six shared-center averages into six independent averages. The rational expression (3.10) is the exact replacement; no CRT density approximation has been used in its proof.

## 3.7. Actual Hankel seam and complete exponent accounting

The permitted independent Hankel report supplies the normalized two-term Bessel identity. Applying its derivation to the compact dyadic amplitude, with u=sqrt(N)s, gives the exact leading difference term

    sum_(m>=1)r2(m)m^(-1/4)K(sqrt(N)(R-sqrt(m))).         (3.13)

The leading sum phase has arbitrarily small total size after integration by parts. The first correction has the cosine difference phase and size O(T^(-1/2+epsilon)N^(-1)); it is not declared zero at resonance. The full two-term Bessel remainder has absolute lattice sum O(N^(-1)), because sum_(v in Z^2\{0})|v|^(-5/2) converges. The dual zero mode is O(T^(-2)N^(-3/4)). A first-term-only expansion would leave a non-summable |v|^(-3/2) error and is not used.

For z=(x-m)/H(x), the near-phase argument equals

    sqrt(N)(R-sqrt(m))=z*2R/(R+sqrt(m))
                       =z+O(z^2/(T sqrt(N))).

Likewise m^(-1/4)=R^(-1/2)(1+O(|z|/(T sqrt(N)))). Schwartz derivative bounds, summation on the shifted integer m-grid, and the divisor bound give total linearization error O(T^(-1/2+epsilon)N^(-1)); outside m comparable to x the complete tail is arbitrarily small. Therefore

    F_N(R)=R^(-1/2) S_N(R^2)+E_N(R),
    E_N(R)<<N^(-1)+T^(-1/2+epsilon)N^(-1),
    M6(E_N)<<T^(1+epsilon)N^(-6).                        (3.14)

This error is paid throughout the band, including transition blocks. Since dR=dx/(2sqrt(x)), the conjectured S6 would give

    M6(F_N)<<T^(1+1/100+epsilon)N^(-3/2)
                       +T^(1+epsilon)N^(-6).

At N>=cT^(52/125), the first exponent is 1+1/100-78/125=193/500. The finite logarithmic smooth partition is paid by Holder and epsilon. This implication does not prove S6.

For a separate all-harmonic control, if g_d is the actual squarefree-class band sum, its absolute amplitude is at most T^epsilon d^(-1/2)X^(-1/4) for d<=X and T^epsilon d^(-3/4) for d>X, with X=T^(52/125). The first estimate sums s^(-3/2) from s comparable to sqrt(X/d), so it retains the high harmonics of the low classes. Summing the squares gives

    sum_d|g_d|^2<<T^epsilon X^(-1/2),
    integral w (sum_d|g_d|^2)^3 <<T^(47/125+epsilon).     (3.15)

The accepted fixed-even absorption inequality at p6 consequently pays repeats at this budget; it leaves the one-sided distinct-six integral unproved. This is consistent with, and does not replace, the signed fraction owner.

The complete norm-band ledger pays L and H at M12<=T^(29/25+epsilon), with H including the infinite norm tail. Their proved ceilings are T^(13/125+epsilon); the accepted actual B ceiling then gives the actual F ceiling T^(beta+epsilon) by B=L+F+H. This does not import a pointwise ceiling for an arbitrary mask. If M6(F)<=T^(193/500+epsilon), interpolation gives exponent 6beta+193/500. Its exact margin is positive because

    29/25-193/500=387/500,
    beta<129/1000,
    (2072298)^2-1717*(50000)^2=1919000804>0.

The last positive integer proves the middle inequality after multiplying by positive denominators and squaring. The margin is 6(129/1000-beta), approximately0.0002018883, so input epsilons must be chosen after this fixed margin. Complete29/25 would imply sharp102/325 by the accepted p12 reconstruction/persistence formula; it would not imply one-quarter. The actual signed input remains missing, so neither consequence is claimed.

# 4. First doubtful or unproved step

The first unproved step is (2.10), the one-sided signed upper bound on the actual nonpaired rational sextuple integral (3.10), with its exact coefficients (2.4), moving H and cutoff, nonpairing exact rational resonances, and near resonances at T^(-2). It is not an estimate for one fraction, one denominator, or six independent centers.

The grouping identity, the compact-frequency zeros, and the paid paired sector do not establish it. The bounded-variation certificate (3.9) is valid but insufficient after moduli, as (3.12) demonstrates. A CRT product-density replacement omits an unpaid short-interval discrepancy. No claim that S6 is false is made. No separate proof of arithmetic cancellation between the two denominator classes, or among the chi4(q) and chi4(a0) signs within them, has been found in this bounded attempt.

# 5. Control tests and outcomes

1. `actual_band_and_complements`: pass at inherited scope. The actual phi, real radius, fixed mollifier, transition blocks, and full high-norm Schwartz tail are retained. The complete-band ledger is reviewed evidence from Round231; its repetition is not a new gain. The graph-accepted generic moment theorem is used only within its stated scope.
2. `sixth_variance_and_repeats`: pass analytically in (3.15), including low d with high harmonics. Relative absorption pays repeats; it does not grant the distinct-six signed estimate.
3. `hankel_phase_and_two_term_error`: pass relative to the cited permitted two-term Hankel derivation, with its normalization reproduced in (3.13)--(3.14). The near leading phase is odd sine; its correction is not zero at exact resonance. No first-term divergent error sum is used.
4. `moving_width_and_endpoints`: pass. H(x) is never replaced inside an identity by a constant. The floor d<=sqrt(x), signed square packet, full nonsquare tails, and coefficient jump variation are all priced. Only comparable constant H0 is used in upper bounds.
5. `two_character_branches`: pass by (3.1), (3.5), and (3.7). For m=3 the true divisor sum is0; keeping only the small-divisor chi4(d) branch would give4 and fail immediately. The conductor reports independent Wolfram/local hyperbola checks for m=1,...,256; this report does not treat a message about diagnostics as a proof or inspect siblings.
6. `signed_fraction_resolution`: pass as a reduction, unresolved as a gain. The center interval is of length T^2, giving T^(-2) resolution. Odd q and 4|q have different actual coefficients. The nonpaired signed estimate is explicitly open.
7. `constant_mean_and_absolute_control`: pass. For a constant sequence on all integers, sum_m K((x-m)/H)=H sum_h Khat(Hh)e(hx) vanishes exactly once H>b; on positive integers the omitted negative tail is arbitrarily small for x comparable to T^2. The continuum mean also vanishes because integral K=0. This does not center away arithmetic fluctuations. An even compact-frequency kernel ALSO has zero mean and small-progression annihilation when its Fourier support avoids0; parity alone is not a new dispersion theorem. The actual Hankel phase selects the odd kernel, whose square-center leading contribution is0. Replacing K by |K| destroys this cancellation. The actual absolute grouped-six control (3.12) blocks the tuplewise-modulus route.
8. `complete_exponent_margin`: pass by the exact positive integer in Section3.7. The small margin, paid errors, Jacobian, full complements and fixed-p12 consequence are all explicit.
9. `wolfram_local_exact`: conductor-owned, pending its archived shared-control record. No tool-generated numerical or asymptotic certification is claimed here. The report's finite formulas and positive integer can be checked directly and were not inferred from numerical sampling.
10. `blind_isolation`: not a blind claim. Only the assigned selected context and conductor messages were used; no sibling report or brief was read. The separate statement-only review remains the conductor's gate.
11. `history_preservation`: pass by work scope. Only the assigned report was written; no graph, proof draft, synthesis, validation matrix, historical evidence, or successor artifact was edited.

# 6. Dependencies and exact artifacts used

The graph was parsed for the accepted complete large-value, distinct-twelfth, and fixed-even-absorption nodes and the open target. Its relevant status is acceptance of reductions and baseline estimates, not of the present improved signed bound. No new literature theorem or outside source was imported. The Bessel references are used only through the permitted report's already written derivation and qualifications. The actual band ledger and historical obstruction synthesis are evidence at their recorded scope.

| Context artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306 |
| state/active_campaign.yml | 8e1e7cdf33fea4338bc8fcc154536ba8df576a3ea359054f6c3a32617788db92 |
| rounds/codex-managed/gc-signed-sixth-dispersion/briefs/signed_fraction_dispersion.md | f7cdde107fe24855c0aa0a01f8048c86352fa0da3978f5a8f76ed082083760f5 |
| rounds/codex-managed/gc-signed-sixth-dispersion/briefs/actual_interface.md | e665ea9cd651c7c6346279d90e89ca7b476bc9f39f757becc9f788abc1a4ecfa |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md | b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0 |
| strategy/round231_balanced_cancellation/conductor_combined_owner.md | 9f5d9a31c0624e7ee97a21bcdfa2e638154fa313cc45cbab198856222366d76b |
| strategy/round231_balanced_cancellation/reports/blind_hankel_tail.md | 03b30638eb6da7242343731ac03b425e2f09e16749f73685adc343a357cd01d5 |
| rounds/codex-managed/gc-connected-cumulant-test/synthesis.md | fc90f9a04a4d851f7dcaa05f90771ab8762f3987b97bc23a6add445006e55213 |
| strategy/round231_cross_label_admission/conductor_decision.md | 89315791f42355233d04b69ed2dba19121bbf0741594880305e74c038c1432a0 |

The initial attempted combined text read of the large graph was tool-truncated; the relevant nodes were then explicitly parsed and read. No inference relies on unseen truncated material. Exact file hashes bind all selected context. Own task brief is included in the manifest for provenance.

# 7. Recommended state effect

Retain this report as candidate evidence for the exact two-branch fraction reduction, paid square/paired/single-denominator sectors, and the scoped failure of the absolute grouped-fraction certificate. Obtain nonauthor review of constants, the hyperbola freeze, the rational-count control, and moving-coefficient variation before considering any narrow graph addition. A statement-only progression/filter check is especially appropriate.

Do not promote S6, M6(F) at193/500, complete29/25, sharp102/325, any M1/M2/GAR endpoint, or the quarter theorem. The report neither improves the accepted complete exponent nor proves a global no-go for signed dispersion. Recommend no target-state change. Freeze this assigned report and stop; no successor round is designed.
