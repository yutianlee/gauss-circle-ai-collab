# Complete actual twelfth moment reduced to distinct radical classes

Round216 candidate,2026-09-28. Campaign:gc-actual-radical-high-values.
Conductor formalization of the discovery task's collective-class
identity and the independently derived complete cutoff estimates.
Authoritative acceptance requires the claim graph and validated patch.
Starting graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

## 1. Exact statement and scope

Fix a nonnegative real radial rho in C_c^infinity(R^2), supported in
the unit disk and of integral1. Use e(t)=exp(2pi i t) and
Psi(s)=rho-hat(s e1) with the minus-sign Fourier convention. Fix
w>=0 smooth, supported in[1/2,2] and equal1 on[1/sqrt(2),sqrt(3)].
For realT>=2 set

    a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    B_T(R)=sum_(n>=1)a_n(T)cos(2pi R sqrt(n)-3pi/4),
    Q=floor(T^(2/5)), V0=T^(13/125),
    f_d(R)=sum_(s>=1)a_(d s^2)(T)cos(2pi R s sqrt(d)-3pi/4),
    L_Q=sum_(d squarefree,d<=Q)f_d,
    Z_Q=sum_(d squarefree,d>Q)f_d=B_T-L_Q,
    E12(R)=sum_(d_1,...,d_12>Q squarefree and pairwise distinct)
                                           product_j f_(d_j)(R),
    I12(T)=integral_R w(R/T)E12(R)dR,
    M_p(F)=integral_R w(R/T)|F(R)|^p dR.

Every tuple inE12 is ordered. Every s, cosine sign, dyadic block,
mixed block and smoothing tail remains. All sums converge absolutely
for each fixedT. Let beta=2theta_LY-1/2, with the existing qualified
accepted Li--Yang application. Then

    M12(L_Q)<<_epsilon T^(15/13+epsilon),                 (D1)
    integral w(R/T)|Z_Q(R)^12-E12(R)|dR
                 <<_epsilon T^(8beta-1/5+epsilon).       (D2)

In particular

    |M12(Z_Q)-I12(T)|<<_epsilon T^(8beta-1/5+epsilon).     (D3)

Since1/8<beta<13/100, the error exponent in(D2) is less than21/25,
well below29/25. Also29/25-15/13=2/325>0.

The following assertions are equivalent, in the convention that each
bound holds for everyepsilon>0 with its own fixed constant:

    integral_(|B_T|>V0)w(R/T)|B_T|^12dR<<T^(29/25+epsilon);
    M12(B_T)<<T^(29/25+epsilon);
    M12(Z_Q)<<T^(29/25+epsilon);
    |I12(T)|<<T^(29/25+epsilon).                          (D4)

A one-sided upper bound I12(T)<=C_epsilon T^(29/25+epsilon) also
suffices, because(D3) bounds its possible negative part by the error.
No assertion in(D4) is proved here. The new result pays every
repeated-class configuration collectively, including its nonzero
frequencies; the remaining distinct-class integral is still unestimated.
This does not give a new pointwise exponent or the quarter theorem.

## 2. Coefficients, head and infinite convergence

The mollifier gives real even SchwartzPsi, |Psi|<=1 andPsi(0)=1.
Let A_d(T)=sum_s |a_(d s^2)(T)| for squarefreed. The prime-factor
formula fromr2=4(1*chi4) gives

    r2(d s^2)<=r2(d)tau(s^2),
    A_d(T)<=zeta(3/2)^3 r2(d)d^(-3/4).                    (D5)

For a prime3 modulo4 occurring ind, the representation counts vanish
on both sides. For a prime1 modulo4 ind, the factor2e+2 is at
most2(2e+1); the other prime factors obey the same inequality, and
powers of2 do not increase ther2 factor. The divisor inequality
tau(s^2)<=tau_3(s) completes(D5), includingd=1 and every s.

The elementary disk area/unit-square comparison gives
sum_(n<=x)r2(n)<=Cx forx>=1. Partial summation of(D5) yields

    sup_(R inR)|L_Q(R)|<=sum_(d<=Q)A_d(T)<<Q^(1/4).       (D6)

For every fixedh=2,...,12 andeta>0, the elementary divisor bound
and dyadic summation give

    sum_(d>Q)A_d(T)^h<<_eta Q^(1-3h/4+eta).              (D7)

Choose the input divisor exponent smaller thaneta/h. The exponent of
d in the summation is strictly less than-1, so the estimate is uniform
inT and allQ>=1. SincePsi decays rapidly, sum_n|a_n(T)| is finite
for fixedT, hence sum_d A_d(T)<infinity. This supplies absolute and
uniform-inR convergence ofZ, each power sum below, andE12. It also
justifies all finite-to-infinite limits against the finite measure
w(R/T)dR. All constants may depend on the fixed functions.

## 3. Masked distribution and complete moment inputs

ForF=L_Q orZ_Q andV>=1, the finite mechanism of the accepted204
kernel gives

    D_F(V):=integral w(R/T)1_(|F|>V)dR
          <<_epsilon T^epsilon[V^-2+T V^(-136/13)].       (D8)

Here is the required coefficient extension. Truncate only at
T^(3/2); the omitted Schwartz/divisor L1 tail isO_A(T^-A), uniformly
in either mask. Split the rest into its singleton andO(logT) ambient
dyadic blocks, setting inactive coefficients to zero. The block
coefficient energy remains at mostT^eta N^(-1/2), and the accepted
unweighted square-root correlation kernel is unchanged. Its finite
Gram and maximal-separated-cover proof applies to these vectors for
every positive block level, retaining its full diagonal and1+T/h
localization ceiling. The real cosine is the real part of its complex
wave times e(-3/8). A union of the block level sets atV/(C logT),
with the uniformly tiny tail included, proves(D8). Choose the input
eta according to the outputepsilon and absorb the finite logarithmic
powers. This uses the accepted finite proof, not an unproved extension
of its final statement for lower cutoffsU. The masks depend onT but
are independent ofR, as needed by that proof.

Layer cake below amplitude1 costsO(T). ForL_Q, its ceiling(D6)
and(D8), withq=136/13, give

    M12(L_Q)<<T^epsilon[T+Q^(5/2)+T Q^(5/13)]
                 <<T^(15/13+epsilon),                    (D9)

because12-q=20/13 andQ is comparable toT^(2/5). This proves(D1)
with all tails and levels, not merely a pointwise small head.

The accepted actual reconstruction and qualified Li--Yang bound give
sup_(R in[T/2,2T])|B_T(R)|<<T^(beta+epsilon). By(D6),
sup|Z_Q|<<T^(beta+epsilon), since1/10<beta. Using(D8) and layer
cake therefore gives, for each integer2<=r<=10,

    M_r(Z_Q)<<_epsilon T^epsilon[T+T^((r-2)beta)].         (D10)

Indeedr<q makes the second large-value integral bounded, and the
first contributes the ceiling to powerr-2, with a logarithm atr=2.
Forr=0 the measure isO(T); forr=1 Cauchy--Schwarz andr=2 give
O(T^(1+epsilon)). These observations prove every lower moment used
in the next section. They assert no supremum bound for arbitrary
coefficient masks: the supremum here specifically usesB_T-L_Q.

## 4. Finite collective-class identity and full partition cost

First take finitely many real functionsf_d. Putp_h=sum_d f_d^h,
so p_1=Z. For a set partitionpi of[12], put
mu(pi)=product_(C inpi)(-1)^(|C|-1)(|C|-1)!. Then

    E12=sum_(pi partition[12])mu(pi) product_(C inpi)p_(|C|).
                                                               (D11)

To prove this, expand the right side into ordered index tuples.
For a given equality class of sizem, the coefficient contributed by
its subordinate partitions is the sum of the signs of all permutations
ofm labels: the factor(|C|-1)! counts cycles on that block. This is1
form=1 and0 form>=2, by the sign-reversing transposition bijection
on permutations. Thus only tuples with all labels distinct survive,
with coefficient1. The all-singleton partition in(D11) isZ^12.

Consequently Z^12-E12 is a finite signed combination of expressions

    Z^r product_(i=1)^b p_(h_i),
    h_i>=2, r+sum_i h_i=12,
    r in{0,...,10}, 1<=b<=floor((12-r)/2).                (D12)

The value r=11 is impossible, andr=12 is the canceled singleton
partition. The expression is a collective signed regrouping, not the
termwise absolute repeated-label expansion. By(D7), |p_h|<=sum_d A_d^h.
Using(D10), each term in(D12) therefore has integrated absolute value
at most

    T^epsilon [T+T^(max(r-2,0)beta)]
                           Q^(b-3(12-r)/4).             (D13)

There are finitely many partitions. Maximizeb atfloor((12-r)/2),
sinceQ>=1. WithQ comparable toT^(2/5), the possible exponents are

    max(1,max(r-2,0)beta)-(12-r)/10       for evenr,
    max(1,max(r-2,0)beta)-(12-r)/10-1/5   for oddr.        (D14)

Forr<=9, (r-2)beta<1 becausebeta<13/100, and the largest exponent
among them is3/5, attained atr=8. Forr=10, beta>1/8 gives the
exponent8beta-1/5>4/5. It is the maximum. This proves(D2).

All identities pass to the infinite class family by the absolute
convergence established in Section2; the bounds(D7),(D10) apply to
the infinite sums after the identity is obtained, so no unproved
pointwise bound for an arbitrary finite subfamily is needed. The
absolute error integral in(D2) proves(D3) immediately.

As elementary controls, fewer than twelve indices giveE12=0 by(D11),
while its right side still cancels correctly. Vanishingfunctions give
zero, and equal valuesf_d=x with exactlym indices give
E12=m(m-1)...(m-11)x^12, including the zero case. No pointwise
positivity ofE12 is asserted for unequal real values.

## 5. Complete equivalence and remaining nonzero correlation

The accepted distribution forB_T pays the entire low-value contribution:

    integral_(|B_T|<=V0)w(R/T)|B_T|^12dR
       <<T^epsilon[T+V0^10+T V0^(20/13)]
       <<T^(29/25+epsilon).                              (D15)

The two larger terms areT^(26/25) andT^(29/25). Thus the first two
conditions in(D4) are equivalent. The scalar inequalities
|B_T|^12<=2^11(|L_Q|^12+|Z_Q|^12) and its version withB_T andZ_Q
exchanged, together with(D1), prove equivalence with the third.
They pay every mixed term without assuming its separate cancellation.
Finally(D3) proves equivalence with the fourth. SinceM12(Z_Q)>=0,
it also gives I12>=-O(T^(8beta-1/5+epsilon)), proving the stated
one-sided upper-bound alternative. BoundedT is harmless by the fixed
Schwartz L1 bound andQ>=1.

There is a direct high-event check: (D6)/V0<<T^(-1/250), so eventually
|L_Q|<=V0/2. On |B_T|>V0, one then has |Z_Q|>|B_T|/2>V0/2;
the full integrand is at most2^12 times the tail integrand. The
constant threshold shift is explicit and its complementary low levels
are paid by(D8), not discarded.

The remaining signed integral has the exact expansion

    I12=T 2^-12 sum_(epsilon in{+1,-1}^12)
      sum_(d_j>Q squarefree pairwise distinct;s_j>=1)
      [product_j a_(d_j s_j^2)(T)] e(-3 sum_j epsilon_j/8)
                w-hat(-T sum_j epsilon_j s_j sqrt(d_j)). (D16)

Distinct squarefree radicals are linearly independent overQ, including
sqrt(1); the accepted exact-resonance kernel proves that algebraic
fact. Every frequency difference in(D16) is therefore nonzero. No
quantitative separation large enough for this physical window is
asserted. Every term remains signed and the Fourier kernel retains
the displacement. Taking all terms in modulus has no justification
as a target-sized estimate. Equation(D16) is unestimated, even though
the exact and collectively repeated classes have been completely paid.

## 6. Dependencies, controls and validation boundary

Accepted dependencies are the elementary r2 divisor identity and
divisor bound, the finite mechanism in
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md,
its qualified Li--Yang pointwise input, and the algebraic independence
in proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md.
No new external theorem is imported. All new algebra and transfers
are proved above. The source theorem's existing repairs remain intact.

The discovery report actual_radical_tail.md supplies the collective
identity proposal; controls/conductor_radical_ledger.md independently
supplies the stronger actual head bound and complete head moment.
The original isolated radical-cutoff report checks all-sign exact
coefficients and high-event scope. The separately isolated collective
identity packet is being independently rederived before acceptance.
Final line reviews must bind this candidate's exact hash. Until then
it is evidence only. No numerical experiment is used as proof.

## 7. State effect and full-goal limitation

Candidate promotion is limited to(D1)--(D3) and the proved equivalence
(D4), with the explicit remaining signed integral(D16). It would add
a complete arithmetic reduction, not a new estimate of the full moment.
The target bound onI12 is open. Even proving it at this order would
give only the102/325 milestone after the already paid sharp-circle
restoration. It does not prove any M1/M2/GAR parent or endpoint.

There is no inference to unbounded moment order. For orderp the
one-pair repeated-class term can cost
T^epsilon Q^(-1/2)[T+T^((p-4)beta)], retaining a term linear inp.
The full quarter goal still requires a sufficient complete family
E(p)=1+o(p) or a complete different route. The proof graph and draft
must remain unchanged until a validated State Patch explicitly accepts
the narrow reduction and independent final-hash seams are complete.
