# Round215 synthesis: complete weighted-wave costs and their limits

Campaign:gc-complete-localized-wave-moment. Date:2026-09-28.
Conductor decision takes effect after the final-hash closure validation.
Graph SHA256:4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

## 1. Result

The complete actual localized-wave target remains open. The round gives
a legal weighted transfer of an amplitude-dependent cone theorem, a
complete angular reduction with a valid insufficient upper bound, and
actual-coefficient lower bounds for two explicitly defined positive
Fourier certificates. No improved moment or pointwise exponent follows.

This is a reviewed diagnosis of the selected methods, not an advance
of the accepted arithmetic frontier. The angular change of variables
retains the original difficult zeroth mode. Its completeness is useful
for checking methods, but an unestimated equivalent or stronger input
does not count as an arithmetic gain.

## 2. Frozen target and complete scope

For every real T>=2 and T^(166/325)<N<T^(242/325), use

    c_m=|m|^(-3/2)Psi(|m|/sqrt(T))v(|m|^2/N),
    F_N(x,R)=sum_(m!=0)c_m e(x.m+R|m|),
    R_j=T/sqrt(2)+j sqrt(N),
    J=ceil((sqrt(3)-1/sqrt(2))T/sqrt(N)), 0<=j<=J,
    f_j(y,u)=phi(y/N)eta(u/N)F_N(y/sqrt(N),R_j+u/sqrt(N)),
    C(T,N)=sum_j integral W(y)|f_j(y,u)|^10 dydu.

Here v is the fixed nonzero nonnegative smooth mask supported in[1,4],
Psi the real mollifier transform with Psi(0)=1, and
W=C_A(1+|y|^2)^(-100). The fixed bandlimited Schwartz cutoffs are
normalized as recorded in the frozen strategy and its clarification.
The target C<<T^(83/65+epsilon) retains all directions, norm
multiplicities, common center phases, windows, endpoints and tails.

Fixed spatial bandwidth and du=sqrt(N)dR prove the sufficient trace
bound integral_I |F_N(0,R)|^10dR<=C N^(-1/2) C(T,N). The complete
tenth gate would supply the102/325 milestone only. It is still unproved.

## 3. Reviewed mathematical findings

### A. Legal amplitude-dependent transfer and its full cost

The source is Guth--Maldague, arXiv:2206.01093v2, Theorem2 and its
exact envelope definitions. Its superlevel measure is unweighted; it
does not directly permit the physical weightW. Both the independent
reviewer and conductor checked the primary statement and definitions.
The external proof is not claimed independently reproved.

For dyadic spatial radii r_k, a bandlimited Schwartz localizer gives
W(y) comparable to sum_k lambda_k |b(y/r_k)|^10, with
lambda_k=(1+r_k^2)^(-100). After the fixed cone dilation, the added
Fourier thickness requires source scale S_k comparable to min(N,r_k).
In particular the bounded spatial radii have bounded source scale.
Keeping N after that multiplication would violate the source hypothesis.

The source threshold and tenth-power layer cake give the complete
positive certificate E_sigma in report equation(E215.7), preserving
the minimum of the amplitude ceiling and the source's good-envelope
threshold. Its sufficient target estimate(E215.8) is unproved.
The exact second moment has only a bounded number of adjacent norm
indices, because eta has compact Fourier support. With every window
and tail included, that second moment and the full amplitude bound give

    C(T,N)<<T N^(2+epsilon).

The report separately proves this same upper cost for the whole source
certificate, including its infinite envelope and spatial-radius sums.
Its target deficit is T^(-18/65)N^2. These calculations identify the
failure of this crude estimate, not impossibility of every weighted
cone argument or of improving the actual source certificate.

### B. Actual angular reduction and a stronger insufficient upper bound

Recombine the windows exactly, with
Q(R)=sum_j |eta((R-R_j)/sqrt(N))|^10 and
rho(R)=(1+dist(R,[R_0,R_J])/sqrt(N))^(-2). Then Q<=C rho and

    C=sqrt(N) integral Q(R) integral W(y)|phi(y/N)|^10
                                   |F_N(y/sqrt(N),R)|^10 dy dR.

For A_ell(n)=sum_(|m|^2=n) exp(-i ell arg(m)) and
G_ell(R)=sum_n n^(-3/4)Psi(sqrt(n/T))v(n/N)A_ell(n)e(Rsqrt(n)),
the complete, proved sufficient reduction is

    C<<sqrt(N) sum_(ell in4Z)(1+|ell|)^(-8)
                              integral rho(R)|G_ell(R)|^10 dR.

Eight angular integrations and three frequency derivatives give a
multiplier kernel bounded by
(1+|ell|)^(-8)(1+|y|)^11(1+|s|)^(-3). Its weighted temporal
translations cost(1+|s|/N)^(1/5); its spatial tenth power is integrable
againstW. Thus every mode, frequency-kernel tail, spatial tail and
radius tail is paid, without a new power of T or N.

The finite coefficient duality of the accepted204 kernel is reproduced
for these complex angular vectors. Their grouped energy is at most
N^(-1/2+epsilon) uniformly inell. Its actual consequence is

    integral rho |G_ell|^10<<T^epsilon(T+N^2),
    C<<T^epsilon(Tsqrt(N)+N^(5/2))<<T^epsilon N^(5/2).

The last comparison uses N^2>T on the entire critical band. This
bound misses the target on every fixed interior power scale. The
zeroth mode is exactly A_0=r2 and G_0=F_N(0,R); angular symmetry
does not estimate it. The stronger sufficient angular inequality(A3)
remains unproved, with no claim that it is equivalent to C215.

A single global rephasing of the coefficients creates weighted mass
of order N^(5/2) near one physical center. This proves only a limitation
of the enlarged coefficient-uniform method. The rephased array is not
the actual arithmetic array, so it is not an actual lower obstruction.

### C. Actual positive Fourier certificates cannot supply the target

For five-tuples M,Q, let b_M=product c_m, v_M=sum m, s_M=sum |m|,
Delta v=v_M-v_Q and Delta s=s_M-s_Q. With plus-exponent Fourier
transforms A_N of W|phi(y/N)|^10 and B of |eta|^10, the exact identity is

    C=N sum_(M,Q)b_M b_Q A_N(Delta v/sqrt(N))
                      B(sqrt(N)Delta s) sum_j e(R_j Delta s).

The actual coefficients are eventually nonnegative with total mass
comparable to N^(1/4), uniformly in the band. This follows from Psi
near1 and an elementary lattice subannulus count, and has received an
independent actual-binding review. The transform ofW is strictly
positive by a Gaussian mixture; uniform Fourier convergence gives
|A_N(z)|>=c on the entire relevant compact disk |z|<=20 for largeN.
This is not a general all-finite-N positivity assertion.

Taking every two-tuple kernel in modulus separately in each window
defines P_sep. Summing all center phases first and then taking the
modulus defines P_joint. Exactly C<=P_joint<=P_sep. Weighted binning
at radial widths N^(-1/2) and T^(-1), respectively, proves

    P_sep>=c T N^2,                P_joint>=c N^(5/2).

At N=T^alpha, their target gaps are2alpha-18/65 and
(5/2)alpha-83/65. The latter is strictly positive on each fixed
interior scale, but tends to zero at the lower endpoint. These are
lower bounds on upper certificates only. Discarded signed terms can
cancel; neither result lower-bounds C or the Gauss error. The independent
statement-only report obtained the same generic conclusions before
its separate NONBLIND seam assignment.

## 4. First unproved step and strategy consequence

The actual signed weighted moment C215 remains the first open estimate.
The complete angular and source-envelope inequalities are sufficient
inputs with explicit costs; neither is now an arithmetic theorem.
Do not spend another round reproducing either positive Fourier
certificate, the crude coefficient norm, or the angular identity alone.

As a candidate for post-closure216 design, retain the already costed
whole-series actual high-value alternative from checkpoint214:

    integral_(|B_T|>T^(13/125)) w(R/T)|B_T(R)|^12 dR
                                  <<T^(29/25+epsilon),
    B_T(R)=sum_n r2(n)n^(-3/4)Psi(sqrt(n/T))
                                  cos(2pi R sqrt(n)-3pi/4).

This is the original real physical series, with every effective block
and the complete smoothing tail. Accepted204 pays its complementary
low values by T^(26/25+epsilon)+T^(29/25+epsilon); the high-value bound
is still unproved. It is a candidate change of focus away from stronger
spatial and angular sufficient envelopes, not a result or a frozen216
task. A fresh216 design must inspect the previous high-value barriers,
select one actual coefficient mechanism, and demand a complete gain.
No next-round research has begun. Broad strategy/source review is due217.

Even a success of either fixed-order gate gives only102/325. The full
quarter route needs a complete moment family E(p)=1+o(p) along unbounded
fixedp, or a different complete proof. Constants need not be uniform
for p growing withT. The current family still tends to the qualified
Li--Yang benchmark, not toquarter.

## 5. Controls, interventions and review

Three reports and three independent final-hash seams are complete,
including a statement-only kernel derivation and its conductor review.
The blind analyst received only an explicit central-cube normalization;
the frozen plan and briefs were not rewritten. That clarification is
archived separately. The conductor ledger's reviewer required a
self-contained actual coefficient formula and smooth mask assumptions;
these were inserted and the changed final hash was independently
rechecked GREEN. This repair did not change the frozen target.

Every source scale, coefficient norm, modulus location, central phase,
window, tail, real endpoint and fixed-interior limitation is preserved.
No numerical experiment was run. All effort was analytical, algebraic
or source audit. No vote or computation substitutes for a proof.

## 6. Evidence and state validation

The reports are weighted_envelope_transfer.md, actual_lattice_envelopes.md,
and blind_spatial_kernel.md. The conductor's independent calculation is
controls/conductor_actual_kernel_ledger.md. The three independent seams,
conductor blind review and conductor_round215_reconciliation.md record
the reviewed scope and exact hashes. The closing archive pins final
reports, reviews, clarification, this synthesis and the frozen strategy.

Closure verifies all348 archived entries from rounds200--214, frozen215
scope, graph/campaign schemas, the identity State Patch and its inverse
replay, graph/draft bytes, the older ledger prefix and both immutable
legacy directories. These state checks do not prove the open estimate.

## 7. State effect and preserved full-goal frontier

Identity State Patch: all399 graph nodes and proof-draft bytes unchanged.
The goal-turn classification is no mathematical gain with reviewed
method diagnosis, not a solved or blocked goal. No actual moment,
pointwise exponent, parent or endpoint is promoted.

M1 HARD still requires all smallt and its complete signed L^(3/2)
bound; SMOOTH is independent. M2 TOP retains its single outer real
part and complete unequal-product complement; BAL requires
|sum_G G P_G|<<L^(3/2); UNBAL retains its actual joint symbol with
target(LK)^(3/4), K=XL/D^2 and K/L>16. RealX, D endpoints, stars,
floors, short blocks and transitions remain. GAR proves totalM1 only
and still requiresM2. Whole-series moments would bypass that
decomposition for the final theorem, not prove its separate parents.
Round216 remains pending design; the next mandatory broad review is217.
