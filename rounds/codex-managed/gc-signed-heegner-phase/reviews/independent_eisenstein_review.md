# 1. Result

**GREEN for the complete continuous-component estimate and its stated
limited scope**, at the verified corrected final target SHA256
`cf92b16e42ad85d900a532a66f1df33cb8aa2be175c7f0f4d8013501a4112d1f`.
This is a NONAUTHOR, NONBLIND Round228 review in campaign
`gc-signed-heegner-phase`, role `signed_hecke_functional_attack` reviewing
the distinct report `reports/complete_eisenstein_pairing.md`.

The initial supplied and verified target SHA256 was
`105b2fb292d1e32fff401d92292a20590f5a1185a55a58815d0a77bb15f645c6`.
Two unintended standalone carriage-return bytes in roman-type labels
required a formatting repair. No mathematical repair is requested.
The corrected final target binding is recorded in Section6 before freeze.

The report proves its full continuous contribution is
O(A_J(N)^2 N^(3/2) T^epsilon), including both level-two cusps, all shifts,
two-adic descendants, both spectral signs, and all tails. Its degree-two
mean square is established with a paid moving-weight argument; it is not
an unproved extra L-function premise. Its sole new external estimate is
matched to its exact critical-line arguments.

This establishes a complete component, not a complete wave improvement.
The ENTIRE signed cusp term remains unproved at target size. No whole
parent, moment, pointwise exponent or quarter theorem is certified here.

# 2. Exact statement, hypotheses and review scope

For every real T>=2 and R comparable to T, all dyadic 2<=N<=P<2T^(3/2),
actual signed Schwartz Psi, and the frozen smooth weights, let A denote
(1+N/T)^(-J). Use the exact H_h, alpha_h, and full continuous Hecke
polynomials L_(q,h) from the target. I reviewed the stronger assertion

\[
 {1\over4\pi}\sum_{h<2N}\alpha_h\sum_{q=1,2}
 \int_{\mathbb R}B_q(t)|L_{q,h}(t)H_h(t)|\,dt
       \ll_{\epsilon,J} A^2N^{3/2}T^\epsilon,             \tag{R1}
\]

where B_q(t) sums the squared point values over every cusp of level q.
It implies the modulus bound for the entire complex continuous pairing.
Hyperbolic area, width-one incoming terms and measure dt/(4pi) are the
same conventions as the already reviewed arbitrary-test pretrace identity.

The source checked directly is Nicol Leong,
[arXiv2405.04869v5, Section2.3, Corollary4](https://arxiv.org/html/2405.04869v5#S2.SS3),
dated 30 January2026. Its final assertion is the reciprocal-zeta bound
29.388 log v on sigma=1 for v>=2. Substitution v=2|t| is legal for
|t|>=1; negative t follows by conjugation. This statement is unconditional.
The neighboring estimates have other ranges and are not substituted.
The inspected exact-version HTML supports the claimed statement. I did
not independently audit the source's entire proof or claim a fresh PDF
render inspection. No additional primary work was introduced by review.

The old closed227 whole-functional identity and scalar kernel/tail
estimates are inherited reviewed premises. I checked their application
again below. The new continuous proof does not need a cusp fourth moment
or the defective printed collective sieve from AH.

# 3. Independent derivation and seam checks

## 3.1 CM normalization and the two level-two cusps

Starting in Re s>1,

\[
 E(z,s)=\tfrac12\sum_{(c,d)=1}y^s|cz+d|^{-2s}
\]

gives E(i,s)=2 zeta(s)L(s,chi_4)/zeta(2s). The factor2 follows from
r_2(n)=4 sum_(d|n)chi_4(d) and the factor1/2 identifying opposite
primitive rows. No stabilizer factor is divided out a second time.

For E(2z,s), primitive rows with odd d correspond to all even lower-left
rows after replacing c by 2c, and contribute 2^s E_infinity^(2)(z,s).
If d is even, c is odd; extracting the factor2 leaves the odd lower-left
rows and contribution 2^(-s)(E(z,s)-E_infinity^(2)(z,s)). Solving gives
the target's first equation(8). Applying the determinant-one W_2 scaling
matrix gives its second equation(8), because level-one modularity sends
E(-1/z,s) to E(z,s).

Both z_2=-1/(i+1) and 2z_2=i-1 are level-one translates of i modulo
SL_2(Z). Thus both level-two cusp values are E(i,s)/(1+2^s). On the
critical line the denominator has modulus at least sqrt(2)-1. The two
equal values remain two distinct cusp channels with the same dt/(4pi)
measure. In particular

\[
 B_1(t)={4|F(1/2+it)|^2\over|\zeta(1+2it)|^2},\qquad
 B_2(t)={2B_1(t)\over|1+2^{1/2+it}|^2},
 \quad F(s)=\zeta(s)L(s,\chi_4).                         \tag{R2}
\]

I also checked the full local factors. At p=2, F has factor
(1-2^(-s))^(-1), and dividing by zeta(2s) leaves 1+2^(-s).
At an inert odd prime F has factor (1-p^(-2s))^(-1), which cancels.
At a split prime the remaining factor is (1+p^(-s))/(1-p^(-s)).
Dividing the resulting product by 1+2^s gives exactly 2^(1-s) times the
split-prime product at either level-two cusp. These are identities in
the convergent half-plane, not convergent critical-line products.
Residues 3/pi at level one and 1/pi at each level-two cusp match the
inverse areas and independently check the normalization.

## 3.2 Theta functional equation and both polar corrections

Let theta(y)=sum_(n in Z)exp(-pi n^2 y). The theta transformation gives

\[
 \pi^{-s}\Gamma(s)F(s)=\tfrac14\left[
 {1\over s-1}-{1\over s}
 +\int_1^\infty(\theta(y)^2-1)(y^{s-1}+y^{-s})\,dy\right].
                                                               \tag{R3}
\]

I obtain this by subtracting 1 before integrating on (0,1), inserting
theta(y)^2=y^(-1)theta(1/y)^2, and changing variables there. This
independently checks the factor1/4, residues +1/4 at1 and -1/4 at0,
and root number +1. The gamma factor is pi^(-s)Gamma(s); its analytic
conductor is comparable to U^2 and its balanced coefficient length to U.

With G(w)=exp(w^2), shift the contour of Lambda(s+w)G(w)/w from2 to-2.
The residues are Lambda(s) at w=0,
G(1-s)/(4(1-s)) at w=1-s, and G(s)/(4s) at w=-s. The last sign is
positive because both the residue of Lambda at0 and the denominator
w=-s contribute a minus. After w maps to-w, the remaining contour is
the negative dual integral. Solving for F(s) gives precisely the two
sums minus P(s) in target(14), with both polar terms shown there.
No trivial-zero gamma poles are added: the contour being shifted is
the completed Lambda, whose only poles are0 and1 by (R3).

On Re s=1/2, the factor X(s) has modulus1. Also
|G(s)|=|G(1-s)|=exp(1/4-t^2), while the reciprocal gamma factor costs
only exp(pi|t|/2) times fixed powers. Thus the displayed P(s) is smaller
than every fixed inverse power at large |t|. The two sums nevertheless
retain this term in their exact identity, as required.

## 3.3 Gamma transition, moving weights and mean square

For w=b+iv, b>0 fixed, the target's uniform estimate

\[
 \left|{\Gamma(1/2+it+b+iv)\over\Gamma(1/2+it)}\right|
 \ll_b U^b(1+|v|)^b e^{\pi|v|/2},\qquad U\le|t|\le2U,
                                                               \tag{R4}
\]

follows from the gamma modulus estimate with 1+|t+v| in place of a large
argument. The numerator is bounded when t+v is bounded because its real
part is positive. Triangle inequality in the exponential and
1+|t+v|<=O(U(1+|v|)) prove (R4) across that transition. Thus the AFE
weight is never estimated by invalid interior Stirling at t+v=0.

Moving the weight contour to a fixed B>0 yields
V_s(n)<<_B(U/n)^B. With a(n)<=d(n)<<n^eta, the tail after
L=ceil(U^(1+delta)) is
O(U^B L^(1/2+eta-B)). Taking B sufficiently large for each fixed delta
and requested tail accuracy pays both infinite coefficient tails.
No parameter order grows with T.

For a finite polynomial Q(t)=sum_(n<=L)b_n n^(-it), direct integration
and 1/|log(m/n)|<=L/|m-n| give

\[
 \int_a^{a+U}|Q(t)|^2dt
 \ll(U+L\log(2L))\sum_{n\le L}|b_n|^2                 \tag{R5}
\]

uniformly for every real starting point a. The harmonic sum arises after
2|b_m b_n|<=|b_m|^2+|b_n|^2. This verifies target(16) without an imported
mean-value theorem.

For the first finite AFE sum, insert the b-line weight integral. Its
inner polynomial has fixed coefficients a(n)n^(-1/2-b) and argument
t+v. For each v, bound the gamma multiplier pointwise by (R4), then
apply (R5) on [U+v,2U+v]. Minkowski is legal since
exp(b^2-v^2)(1+|v|)^b exp(pi|v|/2)/|b+iv| is integrable. It gives
exactly target(17). In the dual sum, use [-2U+v,-U+v]; multiplication
by X(s) preserves the L2 norm. Thus no t-dependent coefficient was
treated as a fixed coefficient without a price.

The divisor estimate pays the coefficient square sum by
O(L^(2eta)log(2L)). Choose fixed delta,b,eta>0 sufficiently small in
terms of the desired epsilon, and then absorb logarithms. Both finite
sums, both tails and P(s) give

\[
 \int_U^{2U}|F(1/2+it)|^2dt\ll_\epsilon U^{1+\epsilon}.
                                                               \tag{R6}
\]

This proves the mean square needed in (R2); it is not a conjectural
Lindelof-type input. All small exponents can be renamed before final
assembly. Source specialization and the bounded denominator in (R2)
therefore yield integral_(U<=|t|<=2U)B_q(t)dt<<U^(1+epsilon).

## 3.4 Low heights and absence of unpriced singularities

The target's elementary trigonometric-polynomial argument excludes
zeros of zeta on Re s=1 away from its pole. Specifically a zero of order
r>=1 at1+iv, v nonzero, would make
zeta(sigma)^3|zeta(sigma+iv)|^4|zeta(sigma+2iv)| tend to0 as sigma
decreases to1, contradicting its Euler-product lower bound1. The last
factor is bounded since2v is nonzero. At t=0 the reciprocal
1/zeta(1+2it) vanishes and F(1/2+it) is regular. Consequently B_q(t)
is bounded on compact t intervals. This closes the range not covered
by the explicit reciprocal-zeta theorem.

## 3.5 All shifts, descendants and spectral tails

The reviewed exact radial geometry gives Lambda_h=Rh/sqrt(N), and
in its enlarged stationary range
|H_h(t)|<<A^2 sqrt(N/h)/Lambda_h. Every coefficient in the exact
L_(q,h) polynomials has its displayed sqrt(m), and the total
sum_descendants sqrt(m/h) is a bounded geometric sum. The elementary
|eta_t(m)|<=d(m) therefore gives

\[
 |L_{1,h}(t)|+|L_{2,h}(t)|\ll h^{1/2+eta}.               \tag{R7}
\]

Combining (R7) with the new mass O(Lambda_h^(1+eta)) makes the entire
stationary integral for this one shift

\[
 \ll A^2\sqrt N\,h^\eta\Lambda_h^\eta.                 \tag{R8}
\]

Thus all h<2N cost A^2N^(3/2)T^epsilon. At no step is a large-shift
sector discarded. The bounds h<<T^(3/2) and Lambda_h<<T^(7/4) make
the small-exponent absorption uniform on every frozen scale.

For completeness I recomputed the tail powers. A low dyadic band
1<=U<=c Lambda_h contributes
O(A^2 sqrt(N)h^eta Lambda_h^(-K) U^(1/2+eta)); its dyadic sum is at
most O(A^2 sqrt(N)h^eta Lambda_h^(1/2+eta-K)). A high band
U>=C Lambda_h contributes O(A^2 sqrt(N)h^eta U^(1/2+eta-K)), with
the same summed bound. The compact |t|<=1 range contributes
O(A^2 sqrt(N)h^eta log(2N)Lambda_h^(-K)). These agree with the target.
Since Lambda_h is at least a constant times T^(1/4), one fixed large
K makes all tails, summed over h, O(A^2T^(-D)) for any prescribed D.

The exact smooth zero extension removes all boundary terms, including
a disappearing continuous overlap. Discrete-empty overlap is not
confused with continuously empty support. The Legendre parameter
symmetry makes H_h even in t even for complex W_h; eta_t and B_q are
also even. Both signs are therefore included, with the proper factor2.
These checks establish (R1) with every spectral channel and endpoint.

## 3.6 Residual scope and reconstruction

The underlying determinant and parity identities are complex-linear,
so target(6) is valid before taking its real part. Its full arithmetic
right side is O(A^2N^(2+epsilon)). Since the ENTIRE continuous partner
is now target-sized, subtraction bounds the ENTIRE complex sum of
both cusp levels by O(A^2N^(2+epsilon)). This does not grant that cap
for each cusp level, band, or individual mode.

In Fejer, dividing by N^(3/2) makes the new continuous term O(A^2),
but leaves the cusp cap O(A^2N^(1/2+epsilon)). The full fallback
therefore remains complex exponent1/4 and physical3/8 after the
singleton, all scales and original Schwartz tail are restored.
The inherited beta remains a whole real-wave bound only.

The pair-count identity in target(26) is exact: a pair separated by h
occurs in H-|h| translated intervals. It therefore reconstructs the
original Fejer quadratic after the full pretrace return. It does not
supply a new signed estimate for the remaining cusp term.

# 4. First doubtful or unproved step

No unresolved mathematical error was found in the scoped component
conclusion. The target proof's new mean-square, source application,
CM normalization, uniform shifts and tails are sufficient for (R1).
The inherited full pretrace/scalar-transform premises remain declared
dependencies; this review does not silently promote those premises.

The first unproved FULL arithmetic inequality is still
2 Re D<<A^2N^(3/2)T^epsilon for target(5), with its entire signed
cuspidal spectrum, all shifts and exact H_h. Paying C makes this an
equivalent remaining one-sided objective up to a target-sized error.
No estimate for that signed cusp cancellation follows from the present
component proof or its geometric return.

The two initial formatting defects were repaired without mathematical
change. The corrected-hash binding and zero standalone-CR check are
recorded in Section6.

# 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Actual whole quantity | Original complex continuous pairing, actual signed g and r_2; all remaining cusp ownership stated. |
| Cusps and normalization | One plus two cusp channels; correct factor2, scaling W_2, residues and dt/(4pi). |
| Local arithmetic factors | Prime2, inert and split factors rederived without claiming critical-line Euler-product convergence. |
| Functional equation | Theta-derived gamma factor, conductor, root+, poles and both AFE residue signs checked. |
| Moving-weight mean square | Gamma multiplier bounded before a uniform translated polynomial mean square; both coefficient tails paid. |
| Source hypotheses | Exact Leong v5 Corollary4 final assertion used at v=2|t|>=2; no RH or off-line substitution. |
| Gamma and low heights | Transition t+v=0 covered by modulus bound; compact critical-line density bounded separately. |
| All shifts and parity | Every descendant included before bounded geometric mass; every h<2N and every frozen N restored. |
| Both signs and full tails | Evenness includes both spectral signs; low, compact and high tails have arbitrary fixed-order decay. |
| Endpoint conventions | Smooth zero extension and literal empty-overlap distinction retained. |
| Real/complex restoration | New component modulus bound; whole real beta never assigned to a complex block. |
| Certificate versus value | No upper-cost deficit converted to an arithmetic lower bound. |
| Blindness and fixed-order scope | NONBLIND history disclosed; no current isolated gamma packet read; no moment or quarter promotion. |

Zero experiments. All controls are algebraic, integral estimates,
source inspection or exact exponent bookkeeping.

# 6. Dependencies, target binding and provenance

Corrected final target SHA256:
`cf92b16e42ad85d900a532a66f1df33cb8aa2be175c7f0f4d8013501a4112d1f`.

The initial target hash was verified before reading. The author repaired
exactly two standalone carriage-return bytes in roman-type labels and
added a provenance disclosure. I verified the corrected hash above,
inspected the repair disclosure and checked that zero standalone CR
bytes remain. The conductor confirmed this as the final byte-only
repair. No mathematical content change was requested by this review.

Reviewer authored the separate discrete attack frozen at SHA256
`f0d2507ef603e8ce1dac149994e52feb660ec9ccf27cf070a1ee83079b6d55dd`.
Its exact primitive/CM and transform history was retained, so this is
a NONAUTHOR review of a different report, not a statement-only or
history-free review. That own report was not edited during review.

Prior authorized context comprises protocol, the graph and manifest,
Round228 strategy and frozen complete interface, September23 strategy,
checkpoint226, the specified closed227 reports/reviews/synthesis and
the accepted complete-wave/moment kernel. The only new local read was
the assigned Eisenstein target. The only new primary read was exact
Leong2405.04869v5 at the citation in Section2. No current blind packet,
blind report, conductor control or sibling review was inspected.

The conductor confirmed that the completed target change is a
byte-only formatting repair. That steering supplied no mathematical
review or independent evidence. Only this assigned review file was
written; shared proof state, synthesis and legacy material were untouched.

# 7. Recommended state effect and stopping rule

Retain the target as GREEN evidence for the COMPLETE continuous-component
lemma at the corrected exact hash bound above. No mathematical
repair is requested. The conductor decides whether any narrowly scoped
component graph change is appropriate after all required gates.

No change follows here to the full signed target, whole exponents,
moments, M1/M2/GAR/endpoints or quarter theorem. The ENTIRE cusp partner
remains open. Freeze this review at its externally recorded SHA256 and
stop. Only the conductor closes Round228.
