# 1. Result

**GREEN for the stated, limited claims.** This NONAUTHOR, NONBLIND
Round227 review checks
`reports/heegner_joint_norm_audit.md` at exact SHA256
`cc921c6d04fb7015e68915000badffa82ff284734460e0be57b2260197443909`,
in campaign `gc-complete-joint-spectral-remainder`.

The whole-functional Heegner representation, two-adic restoration,
constant-density normalization, uniform scalar transform estimates,
applicable norm upper prices, and complete reconstruction are
consistent. In particular, the arbitrary complex smooth test is
justified by the explicit orbit identity and smooth radial pretrace
argument; it is not borrowed for free from Chamizo's printed smoothed
disk transform. No repair to the reviewed report is required.

GREEN does not assert its unproved complete signed estimate, its
stronger positive norm closure, the hypothetical twisted large sieve,
an individual theta-pairing/point-value equality, a new exponent, or
the quarter theorem. The result remains
`complete_joint_spectral_remainder_no_new_bound`.

# 2. Exact statement, hypotheses, and review scope

The target remains the whole actual expression

\[
 2\Re\sum_{1\le h<2N}(1-h/(2N))
 \left\{\sum_{n\ge1}r_2(n)r_2(n+h)W_h(n)
       -\rho_h\int_0^\infty W_h(x)dx\right\}
 \ll A_J(N)^2N^{3/2}T^\epsilon,
\]

with the frozen signed mollifier, smooth weights, all real R comparable
to T, every dyadic 2<=N<=P, and P the smallest dyadic at least T^(3/2).
All densities and all h, including discrete-empty overlaps, remain.

The reviewed unconditional conclusions are an exact representation of
this expression by the level-one point i and the level-two point
(-1+i)/2, together with the upper certificate A_J^2 T^(1+epsilon)N^2.
The elementary A_J^2N^(2+epsilon) cap is stronger. These conclusions use
the stated external AH fourth moment at fixed q=1,2 and discriminant
-4, and its separately stated Hecke second moment. They do not depend
on repairing AH's malformed collective-sieve display.

Primary bindings checked directly:

* [HKLDW1705.04771v3](https://arxiv.org/html/1705.04771v3),
  Remark4.4/equation(4.2), and the previously authorized exact
  Sections3/7 spectral context.
* [AH2607.13518v1](https://arxiv.org/html/2607.13518v1), Theorem1.2,
  equation(8), Section2.1, Section2.4, and the Gaussian pretrace
  calculation in Section4.1; [exact PDF](https://arxiv.org/pdf/2607.13518v1)
  for the already inspected printed limitations.
* [Chamizo, published DOI10.1007/s00009-021-01959-3](https://link.springer.com/article/10.1007/s00009-021-01959-3),
  Lemma2.1, Proposition2.2, equations(2.2)--(2.3), the stated constant
  eigenfunction values, and Lemma2.4 as corroboration of the Hecke
  second moment. This is the published article, not an invented
  arXiv revision.

# 3. Independent derivation and checks

## 3.1 Arbitrary-test orbit/pretrace interface

For determinant m>0 matrices acting on i,

\[
 u(Mi,i)={\|M\|_F^2-2m\over4m}.
\]

For h=4m the reviewed map is integral precisely under the parity
match a=c and b=d modulo2. Its inverse is
a=M11+M22, c=M11-M22, b=M12-M21, d=M12+M21. It gives
det(M)=h/4 and norm-squared 2m+c^2+d^2. Thus it is a bijection onto
all integral determinant-m matrices, and u=(c^2+d^2)/h.

For h odd the undivided map has inverse half of these expressions.
It is invertible over the integers exactly for the matrices whose
mod2 reduction is I or S=(0,1;1,0). Indeed their diagonal entries
agree, their off-diagonal entries agree, and determinant1 modulo2
forces exactly one of those two pairs to be odd. Conjugation by
gamma0=(0,-1;1,1) sends S to (1,1;0,1) modulo2. It therefore sends
this determinant-h semigroup to the level-two determinant-h
semigroup; gamma0(i)=(-1+i)/2. Because h is odd, these are precisely
the prime-to-level Hecke matrices used in the source.

Both maps count M and -M separately. Passing to PSL identifies these
two and gives exactly the factor2 in the report. Stabilizers of the
elliptic point are still counted inside the orbit sum; there is no
further division by their order. As an algebraic normalization check,
the h=1,n=0 count is r2(1)=4: the level-two stabilizer in PSL has
order2 and the matrix sign gives the other factor2. The h=4,n=0
parity-restricted count is likewise4 at i. These controls concern
the orbit identity; the actual test vanishes at zero.

For a compact smooth complex k, the automorphic kernel

\[
 K_k(z,w)=\sum_{\gamma\in\Gamma/\{\pm I\}}
                  k(u(\gamma z,w))
\]

has spherical multiplier

\[
 H(t)=4\pi\int_0^\infty k(u)P_{-1/2+it}(1+2u)du.
\]

This normalization follows from hyperbolic polar area
2pi sinh(r)dr=4pi du. Smooth compact k gives rapid spectral decay
at fixed parameters, so the spectral resolution, point evaluation,
and the finite Hecke coset operation are legitimate. Complex-valued k
is allowed by linearity. Applying the normalized T_m introduces
1/sqrt(m), so the unnormalized orbit is sqrt(m) times its spectral
expansion; the matrix sign then yields the report's 2sqrt(m).
The cusp contribution has measure dt/(4pi), as in Chamizo
Proposition2.2. This independently explains all factors in the
report's equation(8) for the actual test k_h(u)=W_h(hu).

Chamizo's printed proposition includes Delta-dependent smoothed disk
transforms. The review does not identify those transforms with H_h.
The exact matrix identity plus the smooth kernel argument above
supplies the required arbitrary-test extension instead.

## 3.2 Parity descendants and constant density

If h=2 modulo4, an odd n cannot have both n and n+h represented as
two squares: their odd residues would be1 and3 modulo4. The remaining
even n reduce using r2(2n)=r2(n). If4 divides h, even n give matching
coordinate parities automatically. For odd n, swapping the
coordinates of one represented integer exchanges matching and
nonmatching parity, with no fixed point. Consequently the two
measure identities in the report's equation(6) hold for every
complex test F, including their stated zero-atom convention.

Iterating gives exactly

\[
 L_{1,h}=4\sum_{a=0}^{k-2}(-1)^a\sqrt{h/2^{a+2}}
                  \lambda^{(1)}(h/2^{a+2}),\qquad
 L_{2,h}=2\epsilon_k\sqrt{h_0}\lambda^{(2)}(h_0).
\]

The weighted A-descendant has argument 2^a(4mu)=hu and the final odd
descendant has argument 2^k h0 u=hu. Thus the common H_h is exact;
there is no loss of a changing test under the recurrence.

At t=i/2, P_-1=1, so H_h(i/2)=4pi I_h/h. With area-normalized
eigenfunctions, the constant coefficients are respectively
3sigma(m)/(pi sqrt(m)) and sigma(m)/(pi sqrt(m)). They agree with
the explicit source values. For k>=2 the remaining two-adic algebra
is the identity

\[
 6\sum_{a=0}^{k-2}(-1)^a\sigma(2^{k-a-2})+(-1)^{k-1}
                 =2^{k+1}-3.
\]

It follows by induction from sigma(2^r)=2^(r+1)-1. For k=0,1 the
separate formula gives factor1, so all cases yield the report's
rho_h. In particular h=1,2,4,8 give rho_h=8,4,10,13. These are
exact algebraic controls, not numerical experiments.

AH uses probability Haar measure. If phi has norm1 there, its area
norm squared is v_q; hence u=phi/sqrt(v_q), and its fourth moment
changes by v_q^-2. The report uses v1=pi/3 and v2=pi correctly. Its
continuous spectrum is supplied directly by the area-normalized
pretrace identity, so no unconverted probability normalization is
inserted into that part.

There is one cusp at level1 and two at level2. All occur with their
own Eisenstein point value in the reviewed formula. At the used
Hecke indices, their eigenvalue is the common
eta_t(m)=sum_(ab=m)(a/b)^(it); level-two indices are always odd.
This checks the entire constant subtraction and the complete
nonconstant formula(10).

## 3.3 Phase, uniform endpoints, and tails

I independently verified the phase and transform scaling in my
earlier frozen report; this history is disclosed, so this review is
not a statement-only derivation. Here they are checked against the
new pretrace normalization H_h=(4pi/h)J_h.

Set x=h sinh^2(r/2). The physical difference is exactly
sqrt(h)e^(-r/2), and dr/dx=1/sqrt(x(x+h)). On nonempty overlap,
r>log3, sinh(r) is comparable to N/h, and the r-support has bounded
length. All fixed r-derivatives of the signed amplitude remain
O(A^2); a shrinking support does not produce a reciprocal width
because the original smooth weights are differentiated directly.

After the factor (t sinh r)^(-1/2) is extracted from the spherical
function, the two phases are Phi_h(r)+tr and Phi_h(r)-tr. The minus
phase is nonstationary, whereas the plus phase has
t=pi R sqrt(h)e^(-r/2) and positive second derivative t/2. This
gives the exact phase in report(14), and

\[
 |H_h(t)|\ll A^2\sqrt{N/h}/\Lambda_h
       \quad (t\asymp\Lambda_h),\qquad
 \Lambda_h=Rh/\sqrt N.
\]

No h-dependent connection phase cancels h^(it). The spectral
coefficient and the common spectral phase cannot be removed when
applying a signed estimate. For the declared upper certificates,
discarding them is permissible and loses information as stated.

The tail claim is also consistent. Outside an enlarged stationary
band the symbol form gives, for any fixed B, a bound of the shape
A^2 sqrt(N/h)t^(-1/2)(t+Lambda_h)^(-B) for t>=1. Low t can instead
be bounded by A^2 times a fixed polynomial in N/h times
Lambda_h^(-B). Since N/h<<T^(3/2) and Lambda_h>>T^(1/4), B can be
chosen once to defeat any required fixed polynomial. The point
spectral density and Hecke factors have polynomial growth; the high
t dyadic sum converges once B is sufficiently large. There are only
O(N log N) shift/descendant pairs, a further fixed polynomial. Thus
the summed low/high tails can be O(A^2T^-D) for any fixed D.

Smooth zero extension is essential and is present. The exact kernel
also covers the small-h gamma transition; no expansion at tau-t
large is required. Empty continuous support gives zero H_h; empty
integer support alone does not.

## 3.4 Applicable norms, continuous spectrum, and optimistic test

For h comparable to M, t comparable to U, significant interaction
has U comparable to TM/sqrt(N). Each descendant m satisfies m<=h,
and its weighted transform size is

\[
 \sqrt m|H_h(t)|\ll A^2\sqrt N\,U^{-1}\sqrt{m/h}.
\]

The sum of sqrt(m/h) over all descendants is bounded. For the actual
vector, AH's fourth moment gives

\[
 |\sum |u_j(z_q)|^2V(j)|\ll U^{1+\epsilon}\|V\|_2.
\]

Its independently stated equation(8) gives
sum|lambda_j(m)|^2<<(mU)^epsilon(U^2+sqrt(m)). Throughout the required
range U^2>>sqrt(m), because T^2M^2/N divided by sqrt(M) is at least
a fixed multiple of T^(1/2). Minkowski therefore yields
||V||2<<A^2 M sqrt(N)T^epsilon. Multiplication by U gives exactly
A^2 T^(1+epsilon)M^2. This is a lawful use of the whole h-vector
before the explicitly declared norm relaxation.

For the continuous spectrum the local Weyl upper bound used in the
report retains all cusps. It can be verified from the same Gaussian
pretrace method appearing in AH Section4.1: its inverse spherical
kernel is O(U^2) at distance0 and is bounded by a fixed polynomial
factor times exp(-cU^2r^2-r/2) away from0. A fixed-point orbit has a
finite stabilizer, a positive gap away from that stabilizer, and
O(e^r) points out to distance r by disjoint hyperbolic balls.
Consequently the Gaussian kernel sum is O(U^2). On |t|<=2U the
positive spectral multiplier is bounded below by a positive constant,
so both the discrete and continuous contributions are bounded above
by the same O(U^2) majorant. The heat/spherical bound itself follows
from AH's displayed Gaussian inverse-transform integral by extracting
exp(-cU^2r^2) and integrating its endpoint square-root singularity.
This establishes the stated continuous majorant without assuming an
Eisenstein fourth moment.

Since |eta_t(m)|<=tau(m), the supremum of the continuous vector is
O(A^2M sqrt(N)/U) up to epsilon powers; its full band contribution is
O(A^2T M^2). Summing every shift dyad and the already paid tails gives
the reviewed complete A^2 T N^2 certificate. No complementary large
shift sector was omitted.

The fixed-coefficient sieve comparison is explicitly hypothetical.
Even after granting a correct fixed-sieve-sized bound for the true
t-dependent vector, its claimed norm would be A^2sqrt(NM), and the
point fourth moment would cost U times that norm, namely
A^2T M^(3/2). Summing gives A^2T N^(3/2), a factor T too large. The
descendant reorganization causes no extra power: at a fixed 2-adic
depth b, coefficient energy costs sqrt(M)2^-b, and this is summable.
This verifies the optimistic comparison while granting no such sieve.

## 3.5 Missing saving and full reconstruction

At M comparable to N, U comparable to T sqrt(N), the sufficient norm
needed by this Cauchy mechanism is A^2N/T. The available norm is
A^2N^(3/2), giving ratio T sqrt(N); at N comparable to T this is
T^(3/2). The hypothetical sieve norm A^2N still misses by T.
These are sufficient mechanism comparisons, not necessary lower
sizes of the actual vector. A signed spectral estimate can bypass
these positive certificates.

The elementary cap is A^2N^2, whose deficit from A^2N^(3/2) is
sqrt(N). After Fejer's exact bounded multiplier, the diagonal, and
N^(-3/2) normalization, this gives shell wave modulus A N^(1/4).
The dyadic sum with the Schwartz factor gives complete complex
T^(1/4+epsilon), with the singleton and full n>P tail paid. The
uncapped spectral and hypothetical certificates give gamma=3/4 and
gamma=1/2 at N comparable to T. The restored physical exponents are
respectively3/8,5/8,1/2 as stated. They do not improve theta_LY.

The report correctly keeps inherited beta only for the complete real
wave and does not use it blockwise. Its factor T^(2gamma) allowance
for a desired complete wave exponent gamma and the resulting saving
requirements are correct. The whole one-sided signed estimate, with
every discrete/continuous piece in report(10), remains the first
unproved arithmetic claim.

# 4. First doubtful or unproved step

No additional mathematical gap was found in the scoped conclusions
reviewed above. The first unproved target is the complete signed
formula(10) bounded by A^2N^(3/2)T^epsilon. Report(23) is a stronger
positive sufficient closure, also unproved. Report(20) is an
optimistic hypothetical comparison and is not certified as a theorem.

The underlying external theorems remain external premises. This
review verifies their literal statements and application interfaces;
it does not independently reproduce the full proofs of AH's fourth
moment or its cited precursors. The printed defects in AH Lemma2.1
remain fenced off. The whole-functional bridge avoids the unsupported
coefficientwise identification with the level-four theta pairing.

# 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact target hash | Matched cc921c6d04fb7015e68915000badffa82ff284734460e0be57b2260197443909 before review. |
| Matrix and group | Both bijections, mod2 conjugacy, Hecke index and factor2 checked. |
| Arbitrary complex test | Derived by smooth radial pretrace; no free Delta-smoothed prefix transfer. |
| Parity/common kernel | Recurrence verified as measure identity; every descendant retains W_h(hu). |
| Constant and measure | Area/probability conversion and rho_h checked, including h=1,2,4,8. |
| All continuous spectrum | One plus two cusps retained; local Weyl includes their positive mass. |
| Phase/endpoints/tails | Uniform r geometry and full scalar spectral tails checked. |
| AH hypotheses | Correct q=1,2,D=-4; level4 square-prime obstruction correctly stated. |
| Literal source limitations | No repaired Lemma2.1, no N^(4/3) replacing printed N^(4/2), no point/pairing equality. |
| Actual coupled vector | h^(it) dependence remains; fixed-coefficient sieve not applied to it. |
| Full powers | All shift dyads, descendants, normalization, singleton and original tail retained. |
| Actual versus certificate | No vector/scalar lower bound inferred from a norm cost. |
| Full goal | No fixed moment or local sector substituted for quarter. |

Zero mathematical experiments were performed. All controls above are
exact algebra, integral bounds, source checks, or exponent bookkeeping.

# 6. Dependencies and provenance

Role: temporary NONAUTHOR reviewer `joint_shift_spectral_attack`,
reviewing the distinct `heegner_joint_norm_audit` report. Starting
graph SHA256 is
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

I had already read the protocol, graph's named targets, active manifest,
the assigned strategy/checkpoint/interface files, the closed226
source report/review/synthesis, and the accepted complete large-values
kernel in my original assignment. I used that authorized history
rather than rereading unrelated files. My own discovery report is
frozen at SHA256
`9df8afa574a54a6d9c7ca587030aeaec00a7daa345594d224116a93e823d3560`.
It supplied prior knowledge of the scalar Legendre phase and source
printing issues; this review therefore makes no statement-only or
history-free independence claim. Its orbit/parity and norm checks
were rederived against the newly assigned target.

The newly read local artifact was only the named Heegner report at
the exact hash above. No current blind packet/report, sibling review,
conductor control, synthesis, or authoritative state was edited or
used as review evidence. Direct primary bindings are listed in
Section2. The source citations support the claimed interfaces, not
an assertion that their entire proofs have been independently audited.

# 7. Recommended state effect and stopping rule

Retain this GREEN review for the exact whole-functional bridge,
complete norm-cost assessment and no-new-bound conclusion at the
bound target hash. No repair is requested. No accepted proof graph,
draft, moment bound, pointwise exponent, M1/M2/GAR endpoint, or quarter
claim is promoted by this review.

The conductor decides closure and any successor. This review is frozen
at its externally recorded SHA256; the reviewer stops after reporting
that hash and changes no other file.
