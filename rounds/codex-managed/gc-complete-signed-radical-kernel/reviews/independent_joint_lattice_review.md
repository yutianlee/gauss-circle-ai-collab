# Round218 independent joint-lattice application seam

## 1. Result

Campaign: `gc-complete-signed-radical-kernel`; round 218.
Reviewer: temporary `joint_divisor_kernel` subagent, NONBLIND exact-hash
cross-review, 2026-09-28. Verdict: **GREEN for the stated certificate
no-go and complete fallback; no required mathematical repair identified.**

Reviewed claimant artifact:
`rounds/codex-managed/gc-complete-signed-radical-kernel/reports/joint_lattice_kernel.md`
at SHA256
`c3193b053d594b3a1599cdf707161b438f3387703f9e0f2010cf1d3b0101d41c`.
Its hash was checked before the review.

The global positive certificate takes its modulus AFTER the full radius
integral and AFTER each factor has combined every original radial scale
and both cosine signs. The proof supports its bounds

    c T^7 <= P_T <<_epsilon T^(7+epsilon).

The annular certificate likewise supports

    c T^7 L^(-12) <= P_(T,L) <<_epsilon T^(7+epsilon)L^(-12)

for the stated fixed positive annular profile and 1<=L<=c sqrt(T).
The complete elementary signed-moment fallback is T^(7/3+epsilon),
weaker than the inherited complete T^(10 beta+epsilon) estimate.
No actual target or exponent improvement is proved.

This review independently verifies the claimant's after-integration
positivity argument. It does not deduce it from the reviewer's own
inside-integral divisor-packet certificate. Those are different objects,
and an inside-integral certificate lower bound would not imply this one.

## 2. Exact statement and hypotheses checked

The mollifier rho, its real radial Schwartz transform Psi, and the
nonnegative displaced window w are exactly those of the accepted216
reduction. In particular w=1 on [1/sqrt(2),sqrt(3)]. T is real and at
least 2; lower bounds are asserted for sufficiently large T. The fixed
extension chi is smooth, zero on [0,1/2], and one on [1,infinity).

The actual full wave has the exact lattice realization

    f_(T,R)(x)=chi(|x|)|x|^(-3/2)Psi(|x|/sqrt(T))
                                  cos(2 pi R|x|-3 pi/4),
    B_T(R)=sum_(m in Z^2) f_(T,R)(m).

Every nonzero integer vector has norm at least 1, so chi=1 at all those
points; its zero extension eliminates the origin. Thus the arbitrary
smooth interpolation on radii between 1/2 and 1 changes no actual
coefficient. It is nevertheless part of the specified Poisson
certificate and cannot be varied silently when quoting the no-go.

For its real radial Fourier transform F_T(R,kappa), the certificate is

    K_T(k_1,...,k_12)=integral w(R/T) product_j F_T(R,|k_j|)dR,
    P_T=sum_(ordered k_1,...,k_12 in Z^2) |K_T(k_1,...,k_12)|.

This is the full B_T certificate, with no distinct-class mask inserted.
The transfer to the original I12 target uses only the accepted216
equivalence and its already paid head T^(15/13+epsilon) and repeated-
class error T^(8 beta-1/5+epsilon). The report does not assert an additive
approximation of M12(B_T) by I12 with just those errors.

The annular version samples the actual coefficients against a fixed
nonnegative nonzero v in C_c^infinity((1,2)) on |x|/L. Its lower bound
assumes L<=c sqrt(T), with c small enough to ensure Psi>=1/2 throughout
that annulus. Its positive certificate can be large even when an
individual sampled original annulus is sparse; no original-wave lower
bound is inferred from that fact.

## 3. Independent proof and seam checks

### 3.1 Exact identity, convergence, and odd leading constant

For fixed T, f_(T,R) is smooth at zero because it vanishes in a
neighborhood of zero, and it is Schwartz at infinity. Its Schwartz
seminorms are uniformly bounded for R in the fixed compact T-dependent
window. Smooth Poisson therefore gives

    B_T(R)=sum_(k in Z^2) F_T(R,|k|)

with absolute and uniform convergence on that window. The corresponding
finite products and their radius integrals can be interchanged. In
particular M12(B_T)=sum K_T and M12(B_T)<=P_T are exact. The fact that
P_T has its moduli after integration is respected in this identity.

Angular integration supplies 2 pi J0(2 pi kappa r). The leading J0
coefficient is 1/(pi sqrt(kappa r)), so the remaining product of cosines
has prefactor 2 kappa^(-1/2)/r. The product identity is

    2 cos(2 pi Rr-3 pi/4) cos(2 pi kappa r-pi/4)
       =sin(2 pi(R-kappa)r)-cos(2 pi(R+kappa)r).

Consequently the report's exact leading constant and signs are correct:

    kappa^(-1/2)[H_T(R-kappa)-C_T(R+kappa)].

There is no missing pi, factor 2, or factor i. The leading near-shell
profile is real and odd; it vanishes at R=kappa. This is the actual
cosine pairing, not an unsigned substitute.

### 3.2 Localized transform error and every distant dual term

For central kappa~T, the first angular-symbol remainder is of order
kappa^(-3/2) times a radial amplitude with leading size chi(r)r^(-2)
Psi(r/sqrt(T)). Every fixed number of radial derivatives has uniformly
bounded L1 norm. After splitting the two oscillatory branches, integration
by parts therefore gives the claimed mismatch decay

    O_A(T^(-3/2)(1+|R-kappa|)^(-A)).

The counterrotating phase R+kappa is comparable to T, and positive-order
derivatives of chi(r)Psi(r/sqrt(T))/r have uniform L1 norms. Its entire
contribution is consequently O_A(T^-A). The report explicitly chooses
this exponent sufficiently large before subsequent sums or products.

In particular, on the full physical window, the localized error has
L12 norm O(T^(-3/2)); the leading factor has L12 norm O(T^(-1/2)).
In a product of twelve factors, a term containing one localized error
has integrated magnitude at most

    O(T^(-3/2) (T^(-1/2))^11)=O(T^-7).

Higher error products are smaller. A uniform O(T^-A) term has L12
norm O(T^(1/12-A)) and can be made smaller as claimed. Thus the report
correctly avoids integrating a bare pointwise error over a length-T
interval, which would give an inadequate justification for the local
coefficient lower bound.

For 1<=kappa outside [T/4,4T], both radial frequencies R+-kappa have
magnitude comparable to T+kappa. The same symbol integration gives
summable decay in kappa as well as an arbitrary power of T. Actual
integer vector counts grow only quadratically, so sufficiently many
fixed integrations pay their full sum. For kappa=0 the original radial
integral with J0(0)=1 has phase Rr; its smooth amplitude has uniformly
integrable derivatives after differentiation. This term is also
arbitrarily small in T. The infinite original Schwartz tail is retained
in this argument rather than dropped before Poisson.

### 3.3 H_T convergence, translation, and positivity after integration

The uniform estimate for H_T needs care near u=0 because its limiting
function has a jump there. The report handles this correctly.

For M>=1, differentiating Psi(r/sqrt(T))/r gives

    integral_M^infinity |d[Psi(r/sqrt(T))/r]| <= C/M.

Indeed the term with Psi' is bounded by
M^(-1) integral_(M/sqrt(T))^infinity |Psi'(s)|ds, and the r^(-2)
term is O(M^-1). Splitting at r=1/|u| and integrating the tail once
therefore bounds H_T uniformly for 0<|u|<1. For |u|>=1, all
positive-order amplitude derivatives have uniformly bounded L1 norm,
so repeated integration gives arbitrary decay in |u|.

For each fixed u!=0, the same tail bound allows passage to the improper
limit H_infinity(u). Its uniform decaying majorant belongs to L12.
Dominated convergence thus proves H_T->H_infinity in L12; uniform
pointwise convergence across u=0 is neither true nor used. The value at
the single point u=0 has no effect on this assertion.

The damped sine integral is arctan(b/a). Passing a down to zero using
the tail bound gives, for u>0,

    H_infinity(u)=pi/2-
        integral_0^1 (1-chi(r))sin(2 pi ur)dr/r=pi/2+O(u).

Hence A0=integral H_infinity^12 is finite and strictly positive.
For |h_j|<=delta, the difference of the product of twelve translated
H_T factors from H_infinity^12 is bounded in L1 by the telescoping
sum of twelve L12 differences multiplied by eleven bounded L12 norms.
Translation continuity of the fixed L12 limit, together with H_T
convergence, makes this estimate uniform in all the shifts. This proves
the report's integrated positivity statement

    integral product_j H_T(u-h_j)du >= A0/2.

This is the crucial valid step that is absent from a mere lower bound
for an inside-integral sum of moduli. It allows each complete real
profile to change sign and retains that sign inside the R integral.

If all kappa_j belong to a bin of width delta in [T,3T/2], translate
R by a member kappa0. On any fixed bounded translated interval the
actual w is exactly 1 for all sufficiently large T, uniformly in the
bin's position, because that interval lies strictly inside the flat
part of w. Uniform decay pays the remaining translated tails. Multiplying
the twelve positive factors kappa_j^(-1/2), and using the localized
error estimate above, proves for the exact, already integrated kernel

    K_T(k_1,...,k_12) >= c T^-6.

All original signs and radial scales have been combined before this
positivity assertion. The error is smaller by a power T^-1.

### 3.4 Exact integer multiplicity and complete global certificate

Let b_l count the actual vectors in each half-open bin of fixed width
at most delta in [T,3T/2]. There are O(T) bins. The elementary disk
comparison has O(T) boundary error and gives sum b_l comparable to T^2
for real T. Finite Holder then yields

    sum_l b_l^12 >= (sum_l b_l)^12/(number of bins)^11
                  >> T^13.

The tuples are ordered and repetitions are allowed, exactly as in the
full B_T expansion. Each vector is counted with its actual multiplicity;
there is no replacement of r2(q) by 1 and no thin-annulus asymptotic.
The previous exact kernel lower bound therefore proves P_T>>T^7.

For the upper bound, squared integer norms in a radius band of width
a+1 near T occupy O(T(a+1)+(a+1)^2+1) integer values, each with divisor
size multiplicity. Summing the decaying H_T and error envelopes over
distance bands gives sum_k |F_T(R,|k|)|<<T^(1/2+epsilon). The already
paid far tails do not change this. Tonelli gives

    P_T <=integral w(R/T)(sum_k |F_T(R,|k|)|)^12 dR
         <<T^(7+epsilon).

This inequality is an upper comparison used in the proof; it does not
redefine P_T as the larger inside-integral certificate. The independent
lower proof concerned P_T itself, so the two-sided statement is valid.

### 3.5 Annular and unequal-scale seams

Putting r=Lt in the leading radial integral leaves no extra power of L:
its dr/r becomes dt/t. Thus the claimed annular profile and prefactor are

    kappa^(-1/2) H_(T,L)(L(R-kappa)).

The first symbol remainder is O(T^(-3/2)L^-1) with mismatch width L^-1,
which agrees with the stated T^(-1/2)(TL)^(-1). The profiles have
uniform Schwartz bounds in their argument. For L/sqrt(T)<=c, positivity
of Psi and v makes their derivative at zero uniformly positive; bounded
higher derivatives then give a fixed interval on which the profile has
uniform positive size. This proves a uniform positive L12 lower bound.
Their uniform derivative bounds also prove the required uniform
translation continuity.

The same-bin positivity proof now gives c T^-6 L^-1 per exact joint
coefficient. There are O(TL) bins of width delta/L, and still comparable
to T^2 total vectors. Thus the exact ordered tuple count is at least
T^13 L^-11, proving the annular lower T^7 L^-12. The local error products
are smaller by (TL)^-1; the physical window remains flat across the
relevant translated region.

For unequal scales, the radial integrations by parts give the product
mismatch envelope in the report's (18). To obtain (19), choose an index
i with L_i maximal and use

    1+L_j|kappa_j-kappa_i|
      <= C(1+L_j|R-kappa_j|)(1+L_i|R-kappa_i|).

Assign enough of the original decay power to each of the eleven
distance factors, and leave an integrable power of the i-th factor.
The resulting integral has size L_i^-1. For L_j<=T^(3/4), the integer
shell count is T^(1+epsilon)/L_j, including its +1 because T/L_j>=T^(1/4).
There are O(T^2) reference vectors. Hence the complete restoration is

    T^-6 L_i^-1 T^2 product_(j!=i)(T/L_j)
       =T^7/product_j L_j,

as claimed. Rescaled smooth nonproduct amplitudes have the same
integration-by-parts bound with finitely many seminorms; an arithmetic
mask would not have those seminorms and is not used.

### 3.6 Stationary rank and the complete fallback

For phase R sum epsilon_j |x_j|-sum k_j.x_j, the stationary directions
are x_j/r_j=epsilon_j k_j/|k_j| and all |k_j|=R. Each angular Hessian
entry is epsilon_j R r_j, so fixed-R rank is p. The additional common-R
equation is sum epsilon_j r_j=0. The radial/common-R Hessian has rank 2;
therefore full rank is p+2 and nullity p-1. At p=12 these are 14 and 11.
All-equal signs have no stationary set; comparable balanced signs do.
No full-rank gain follows. The stated scale T^-6 L^-1 agrees with the
annular coefficient calculation above.

The complete fallback preserves the original signed second moment.
On n~L^2 the coefficient square sum is O(L^-1 T^epsilon), the distinct
root spacing is at least c/L, and the smooth Gram row sum is O(T) for
L<=T^(3/4). Thus M2<<T^(1+epsilon)/L. Its multiplication by ten powers
of the valid pointwise envelope min(L^(1/2),T^(1/2)/L) gives

    M12<<T^epsilon min(T L^4,T^6 L^-11).

The terms meet at L=T^(1/3) with exponent 7/3. The L12 triangle inequality
pays every mixed dyadic block by logarithmic losses. Bounded initial
blocks, including n=1, have O(T) moments directly. The actual coefficient
Schwartz tail past n=T^(3/2) is arbitrarily small in supremum, while the
full coefficient L1 sum is O(T^(1/4+epsilon)); taking its decay order
large enough pays even an additive twelfth-power comparison over the
length-T window. This verifies a complete fallback without an unestimated
endpoint or tail complement. The stronger inherited T^(10 beta+epsilon)
bound remains the best supported result.

## 4. First doubtful or unproved step

No unproved step was found in the precise global or annular certificate
claims at the reviewed hash. No required repair is identified.

The first unproved step toward the research target remains cancellation
between different exact K_T tuples in their signed sum. The positivity
of a large selected family proves a lower bound for P_T; it gives no
lower bound for M12(B_T), because other K_T may be negative. The report
states this distinction correctly.

The reviewed certificate depends on the fixed chi interpolation and on
working with full B_T through the paid216 equivalence. The proof makes
no universal assertion about every interpolation, subtraction of the
paid head, or every signed joint-Poisson method. These scope restrictions
must remain attached to any conductor summary or retained evidence.

## 5. Controls and outcomes

* Actual lattice identity and original coefficients: GREEN. Integer
  samples agree exactly, the origin is removed, and every multiplicity
  is retained.
* Odd leading constant and all real signs: GREEN. The leading expression
  is exactly kappa^(-1/2)[H_T(R-kappa)-C_T(R+kappa)].
* Localized L12 error: GREEN. It gives O(T^-7) product error, with
  arbitrarily small uniform remainder and all distant dual vectors paid.
* H_T limit and translation: GREEN. L12 convergence is used correctly
  despite the limit's jump at zero; product positivity is uniform in
  small translations.
* Bin coherence and exact multiplicity: GREEN. Global and annular
  bin counts are respectively O(T) and O(TL), and finite Holder applies
  to the actual vector counts with ordered repetitions.
* Modulus-after-integration scope: GREEN. The lower proof concerns the
  exact K_T, not the larger inside-integral certificate from the
  reviewer's divisor report.
* Rank, unequal blocks, and nonproduct amplitudes: GREEN within the
  stated smooth amplitude class; arithmetic masks remain excluded.
* Real endpoints, harmonic coverage, and all tails: GREEN. Real T,
  literal half-open assignment, original Schwartz tails, zero dual
  vector, noncentral vectors, and bounded initial blocks are paid.
* Complete fallback and actual target: GREEN bookkeeping; target OPEN.
  The method gives T^(7/3), inherited best is T^(10 beta), and neither
  reaches T^(29/25).
* Full-goal scope: GREEN. Even success at this fixed moment would give
  only 102/325. No unbounded-fixed-order family, M1/M2/GAR parent, or
  quarter theorem is supplied.

This is a nonblind application review, not the separately assigned blind
geometry validation. All checks were analytical; no experiment, theorem
search, additional current report, or successor work was used.

## 6. Exact dependencies and artifacts used

Newly read and hash-verified claimant:

    rounds/codex-managed/gc-complete-signed-radical-kernel/reports/joint_lattice_kernel.md
    c3193b053d594b3a1599cdf707161b438f3387703f9e0f2010cf1d3b0101d41c

Reviewer's original frozen report, used only to distinguish certificate
scope, and not edited or reread in this seam:

    rounds/codex-managed/gc-complete-signed-radical-kernel/reports/joint_divisor_kernel.md
    81a983cbf4f3de82e0c88911d1569c26b3920c7b6cb4adaf7ebb71918cdcba87

Previously read allowed context retained from the original task:

* `protocol.md` — `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
* `state/proof_obligations.yml` — `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
* `state/active_campaign.yml` — `86bd9c5a8d329935b4c4cb944840b369149004ae706ae9c5b8f5d4ff41e07732`.
* `strategy/round218_complete_signed_radical_kernel.md` — `40185e8fbd2961087f93ce6141fe7801b36d57c0d1e9ee67e6f42ac2925800d4`.
* `strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md` — `39054e4123c11b85e55d9146794cfdd7453915ebefd8a1286763e08b4ecabcd2`.
* `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` — `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.
* `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` — `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee`.
* `proofs/kernels/gc_distinct_radical_absolute_certificate_obstruction.md` — `603aa69cb4b757707d6eb89bb8290b05190b6b6d5cae83be52ddc19658ef68bb`.
* `rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md` — `6ea983ef7066a7dc1a7833bbf4a99889e79c75eef9c42190421a4248c104aa5a`.
* `rounds/codex-managed/gc-signed-near-frequency-cancellation/synthesis.md` — `b0f7d6e95b868c02fbc19d7bff0d7d0833867e9e527f1d349a44f5074c0cb86c`.

The original task brief was previously read. No context newly cited by
the lattice claimant outside this reviewer's allowed context was opened.
In particular the localized-wave synthesis and isolated geometry packet
were not read. No new external theorem is required for the checked
elementary transform, integration, and counting arguments. The qualified
Li--Yang input enters only through the inherited comparison and the
already accepted216 transfer; this review does not independently reaudit it.

## 7. Recommended state effect

Retain the exact-hash joint-lattice report as GREEN method evidence for
the precisely defined certificate obstruction and full classical fallback.
No repair cycle is requested on this seam. Keep the separate blind
geometry and conductor reconciliation gates independent.

No accepted analytic target, complete moment exponent, source qualification,
M1/M2/GAR parent, or quarter-goal status changes on the strength of this
review. In particular do not summarize the result as impossibility of
the actual signed target. The conductor owns any State Patch and closure.
This review is the only file written during the follow-up, and the
subagent stops after returning its hash.
