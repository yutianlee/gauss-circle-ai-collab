# Complete fixed-even-order distinct-class reduction by relative absorption

Round233; campaign `gc-fixed-order-moment-absorption`; conductor candidate2026-10-12 Asia/Shanghai. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Requires nonauthor final-hash reviews before acceptance. This is an all-fixed-order reduction, not a bound for its remaining signed integral.

## 1. Exact theorem and scope

Fix the real nonnegative radial smooth unit-mass mollifier rho supported in the unit disk, Psi(s)=rho-hat(s e1), and nonnegative smooth w supported[1/2,2], equal1 on[1/sqrt(2),sqrt(3)]. For real T>=2, squarefree positive d, and real Q>=1 set

    a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    f_d(R)=sum_(s>=1)a_(d s^2)(T)cos(2pi R s sqrt(d)-3pi/4),
    B_T=sum_d f_d, L_Q=sum_(d<=Q)f_d, Z_Q=sum_(d>Q)f_d,
    V_Q(R)=sum_(d>Q)f_d(R)^2,
    E_(p,Q)(R)=sum_(ordered pairwise distinct d_1,...,d_p>Q) product_j f_(d_j)(R),
    I_(p,Q)=int w(R/T)E_(p,Q)(R)dR,
    M_p(F)=int w(R/T)|F(R)|^p dR,
    J_(p,Q)=int w(R/T)V_Q(R)^(p/2)dR.

For every FIXED even integer p>=2 and every delta in(0,1), the following hold, uniformly in real T>=2 and Q>=1:

    int w |Z_Q^p-E_(p,Q)| <= delta M_p(Z_Q)+C_(p,delta)J_(p,Q),       (A1)
    (1-delta)M_p(Z_Q) <= I_(p,Q)+C_(p,delta)J_(p,Q),                (A2)
    I_(p,Q)>=-C_(p,delta)J_(p,Q),
    |I_(p,Q)| <=(1+delta)M_p(Z_Q)+C_(p,delta)J_(p,Q).               (A3)

For every sufficiently small eta>0, depending on fixed p as needed,

    J_(p,Q)<<_(p,eta) T Q^(-p/4+eta),
    M_p(L_Q)<<_p T Q^(p/4).                                       (A4)

Thus, whenever a chosen nonnegative budget A(T) pays J_(p,Q) and M_p(L_Q), the assertions M_p(B_T)=O(A(T)), M_p(Z_Q)=O(A(T)), |I_(p,Q)|=O(A(T)), and the one-sided upper bound I_(p,Q)<=C A(T) are equivalent, with constants depending on p and the stated bounds. In particular:

1. For Q=1 and any fixed b>=1, each bound at T^(b+epsilon), for every epsilon>0, is equivalent to the others. The head and J are O_p(T), without a pointwise beta input.
2. For Q=floor(T^(1/p)), the same equivalence holds for any fixed b>=5/4: the head is O_p(T^(5/4)) and J<<T^(3/4+epsilon).

A sharper optional head estimate from the accepted coefficient-mask distribution replaces5/4 in(2) by

    h_p=1+max(p-136/13,0)/(4p).                                   (A5)

In particular h_12=161/156. This refinement requires the distribution input audited below; the core Q=1 and crude growing-cutoff statements do not require it.

An unbounded sequence of fixed even orders p, with one-sided signed bounds I_(p,1)<<_(p,epsilon)T^(b_p+epsilon), b_p=o(p), would imply the quarter bound by the complete bridge and sharp restoration. The analogous assertion for Q=floor(T^(1/p)) also suffices, after replacing b_p by max(b_p,5/4), or by max(b_p,h_p) if(A5) is used. None of these signed bounds is proved here. Constants may grow with p; p never grows with T in a claimed estimate.

## 2. Finite absorption proved independently of arithmetic

Take a finite real family x_i, Z=sum x_i, V=sum x_i^2, and power sums P_h=sum x_i^h. Let E_p be the ordered distinct polynomial. For every set partition pi of[p], let mu(pi)=product_(C in pi)(-1)^(|C|-1)(|C|-1)!. Then

    E_p=sum_(pi partition[p])mu(pi) product_(C in pi)P_(|C|).       (A6)

Indeed, after expansion a tuple's equality block of size m contributes the sum of permutation signs on m labels: cycle blocks contribute exactly the displayed factorial and sign. For m>=2 composing with a transposition pairs positive and negative signs, so this sum vanishes; for m=1 it is1. Thus exactly the distinct tuples survive.

The all-singleton term is Z^p. For h>=2, |P_h|<=V^(h/2): if V>0, divide by sqrt(V), so each normalized |x_i|<=1 and sum normalized squares is1. Every other partition has r<=p-2 singleton blocks and contributes in absolute value at most |Z|^r V^((p-r)/2) times |mu|. The sum of |mu| over all partitions is p!, since these weights count permutations by their cycle partitions. Let A=p!-1. For t=|Z|/sqrt(V),

    |Z^p-E_p|/V^(p/2) <= H_p(t)
      =sum_(j=2)^p binom(p,j) D_j t^(p-j)
      <=A max(1,t^(p-2)),                                      (A7)

where D_j counts permutations of j labels with no fixed points. The coefficient formula follows by choosing the nonsingletons and then a derangement on them; it is not needed to assume any closed formula for D_j.

Set R0=max(1,sqrt(A/delta)). If t>=R0, the last bound is at most delta t^p. If t<R0, it is at most A R0^(p-2). Therefore

    |Z^p-E_p|<=delta |Z|^p+C_(p,delta)V^(p/2),
    C_(p,delta)=(p!-1)max(1,((p!-1)/delta)^((p-2)/2)).             (A8)

For V=0 all x_i vanish and the conclusion is immediate. For p=2, E_2=Z^2-V and the stated C is1. No family-size dependence occurs. The finite identity and inequality extend to absolutely summable real families: finite sums converge in l1 and l2, and the distinct p-fold sum converges absolutely, dominated by (sum|x_i|)^p. No cancellation or positivity of E_p is assumed. Evenness is used in identifying Z^p with the nonnegative |Z|^p for integral absorption.

For a measurable family, whenever the indicated finite integrals exist, integrate(A8) to obtain(A1)-(A3). Pointwise E_p>=(1-delta)|Z|^p-C V^(p/2) also bounds its negative part by C V^(p/2). Hence a finite one-sided signed-integral upper bound is meaningful once J is finite, and forces moment finiteness even if that finiteness was not assumed in advance. In the actual application all integrals are already finite for each T by the uniform absolute convergence below.

## 3. Actual amplitudes, infinite harmonics and head

The divisor identity gives, for squarefree d,

    r2(d s^2)<=r2(d)tau(s^2),
    A_d(T):=sum_s |a_(d s^2)(T)|<=C r2(d)d^(-3/4).                (A9)

For a prime3 modulo4 dividing d, both representation counts vanish. For a prime1 modulo4 the factors satisfy2e+2<=2(2e+1); powers of2 do not increase the representation count. Since |Psi|<=1 and tau(s^2)<=tau_3(s), the harmonic sum is bounded by zeta(3/2)^3. This proves(A9) with all s retained.

The elementary count sum_(n<=x)r2(n)<=C x follows by covering the lattice disk with unit squares. Partial summation gives sum_(d squarefree<=Q)A_d<<Q^(1/4), including Q near1. Thus the actual complete head has the uniform pointwise bound ||L_Q||infinity<<Q^(1/4), and its p moment is O_p(TQ^(p/4)). This uses actual positive coefficient mass; no arbitrary-mask ceiling is invoked.

For any small xi>0, the elementary divisor bound and summation give

    V_Q(R)<=sum_(d>Q)A_d(T)^2<<_xi Q^(-1/2+xi).                 (A10)

Raise this bound to fixed p/2, choose xi=2eta/p, and use integral w=O(T), proving(A4). For Q=1 a single fixed summable bound gives J=O_p(T) with no T^epsilon. Only the square-sum estimate is needed; no all-order version of a graph statement restricted to h<=12 is presumed.

For fixed T, rapid decay of Psi and the divisor bound give sum_n |a_n(T)|<infinity. This majorizes sum_d A_d and is independent of R. Consequently every harmonic expansion, class sum, p-fold product and distinct tuple series converges absolutely and uniformly on the radius window. Integration and finite-to-infinite limits are legitimate for every fixed p,T; no uniform l1 bound as T increases is claimed or needed. Real Q and its integer boundaries merely select a subset. With Q=floor(T^(1/p)), one has T^(1/p)/2<=Q<=T^(1/p), so(A4) gives the claimed powers with constants depending on p. Large but fixed p does not invalidate that floor comparison.

## 4. Complete moment comparison and optional head refinement

Take delta=1/2. Equations(A2)-(A3) give

    M_p(Z_Q)<=2I_(p,Q)+2C_(p,1/2)J_(p,Q),
    |I_(p,Q)|<=3M_p(Z_Q)/2+C_(p,1/2)J_(p,Q).                   (A11)

The first right side is nonnegative by(A2); it must not be replaced by a misleading bound proportional to I alone. Equivalently one may use I_+=max(I,0), together with the paid negative-part floor. The scalar inequalities

    M_p(B_T)<=2^(p-1)(M_p(Z_Q)+M_p(L_Q)),
    M_p(Z_Q)<=2^(p-1)(M_p(B_T)+M_p(L_Q))                        (A12)

pay every mixed head/tail contribution without a separate cancellation assumption. Equations(A4),(A11),(A12) prove all budget equivalences in Section1. These are multiplicative target equivalences; they do not assert the stronger small additive approximation recorded for p12 and Q=T^(2/5) in216.

For(A5), use the accepted204 finite Gram/covering argument with zero coefficients outside squarefree classes d<=Q, as explicitly audited in216 Section3. The mask is fixed in R; dyadic coefficient energies are no larger, the correlation kernel is unchanged, and the full Schwartz tail is retained. This gives D_(L_Q)(v)<<T^epsilon(v^-2+T v^(-q0)), q0=136/13, for v>=1. For the optional head refinement only, restrict to1<=Q<=T, which includes both proposed cutoffs. With ||L_Q||infinity<<Q^(1/4), layer cake, including levels below1, gives

    M_p(L_Q)<<_(p,epsilon)T^epsilon
       [T+Q^((p-2)/4)+T Q^(max(p-q0,0)/4)].                  (A13)

At p=2 the first large-value integral is logarithmic; at p=q0 the second would be logarithmic, though no even integer equals q0. Such logarithms are included in epsilon. For Q=floor(T^(1/p)), the middle exponent(p-2)/(4p)<1, so(A13) gives(A5). This optional improvement imports only the already accepted coefficient mechanism, not any new external theorem or arbitrary-mask pointwise bound. The crude complete statement remains valid independently of(A13).

## 5. Sharp-circle restoration and fixed-order quantifiers

The accepted complete reconstruction with smoothing width T^(-1/2) is

    P(R^2)=sqrt(R)B_T(R)/pi+O_epsilon(T^(1/2+epsilon))

for every real radius R comparable to T, including integer jumps. This restores the entire Bessel and smoothing errors. Therefore for X=T^2,

    int_(X/2)^(3X)|P(x)|^p dx
      <<T^(1+p/2)M_p(B_T)+T^(2+p/2+epsilon).                 (A14)

A complete normalized moment exponent b gives sharp moment exponent

    a_p=max(1+p/4, (1+p/2+b)/2).

The persistence proof is elementary and includes both signs. If P(x)=V>0, monotonicity of the inclusive count gives P(x+h)>=V-pi h for h>=0. If P(x)=-V<0, it gives P(x-h)<=-V+pi h. Thus |P|>=V/2 on a one-sided interval of length V/(2pi), lying in the enlarged dyadic range for large X by an elementary sublinear circle bound. Integrating yields V^(p+1)<<X^(a_p+epsilon). Small X is absorbed by constants. For b>=1 this gives

    theta_p=(p+2+2b)/(4(p+1))
            =1/4+(1+2b)/(4(p+1)).                           (A15)

For arbitrary b replace it by max(b,1); for the crude growing cutoff use max(b,5/4). If a sequence of fixed even p tends to infinity with b_p=o(p), these paid exponents divided by p tend to zero. For any desired circle epsilon, first choose one sufficiently large p, then choose the moment-input epsilon and keep p fixed as T tends to infinity. The p-dependent constants in(A8),(A12) can be arbitrarily large without changing this implication. There is no permitted substitution p=p(T), no claim of uniform constants in p, and no inference that the required signed estimates have been obtained.

Distinct squarefree radicals have no nontrivial rational linear relation; thus the fully expanded distinct-class Fourier integral has no exact zero frequency. This inherited algebraic fact supplies no sufficiently strong near-frequency separation. Every sign, harmonic and cross-class cancellation remains in I. A tuplewise absolute estimate would be an additional, generally much stronger certificate; none is made here.

## 6. Controls, dependencies and first remaining gap

For fewer than p indices E_p=0. For n equal values x, E_p=n(n-1)...(n-p+1)x^p; the repeated correction is of relative order1/n for large n, consistent with absorption. With three values1 and three values-1 and p6, Z=0, V=6 and E_6=-720, so signed distinct polynomials and their integrals need not be positive. Scaling shows V^(p/2) cannot be omitted. A single nonzero x shows the defect cannot in general be bounded by delta|Z|^p alone when delta<1.

Wolfram verifies Newton/derangement coefficients at even orders2 through16; independent local exact-integer/rational reproduction checks every coefficient, the one-pair coefficient binom(p,2), total absolute coefficient p!-1,64 signed finite-family cases and the negative control. The proofs in Sections2-5, not those computations, establish the unrestricted statements. Exact code/output are in controls/ and are diagnostic only. The semantic Wolfram context query was used for tool orientation; no theorem was imported from its generated suggestions.

Dependencies: `protocol.md`; accepted `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` for the actual coefficient argument and audited mask use; `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` for the accepted finite distribution and complete sharp reconstruction; the graph-accepted elementary divisor and exact-radical-independence inputs. The finite absorption proof is reproduced here, with a statement-only independent derivation required separately. Existing external source qualifications are preserved. No new source theorem is needed.

The first remaining arithmetic gap is a one-sided upper bound for the actual signed I_(p,Q) at a complete improved budget. At unbounded fixed orders, the required b_p=o(p) family is entirely unproved here. The new absorption removes the baseline repeated-class expenditure; it does not estimate the remaining oscillatory aggregate. Existing high-moment and pointwise exponents do not improve from this reduction alone.

## 7. Recommended state effect

After the required reviews and graph validation, promote only this all-fixed-even-order relative-absorption and complete-reduction lemma, with the conditional sharp implication and explicit open signed targets. Preserve216's stronger additive p12 statement and all existing nodes verbatim. Do not promote a complete moment bound, a pointwise improvement, any M1/M2/endpoints or the quarter theorem. The proof draft may mention the new accepted reduction only after the State Patch adds that narrow node.
