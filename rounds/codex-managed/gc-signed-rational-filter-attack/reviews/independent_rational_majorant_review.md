# Round 207: independent review of the grouped rational sixth majorant

Campaign: `gc-signed-rational-filter-attack`. Role: independent post-report
seam reviewer, not statement-only blind. Date: 2026-09-27.
Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Reviewed artifact:
`rounds/codex-managed/gc-signed-rational-filter-attack/reports/signed_rational_moment_attack.md`.
Final reviewed SHA-256:
`f34a4a56d076bf9aa369181feac45a60bf387a38976ac7470f74244785e3cf19`.
Effort: 100 percent analytical; no mathematical numerical experiment.

## 1. Result

**GREEN within the exact stated scope.** The complete two-arm formula,
the mod-four Fourier sign, both reduced-denominator classes, duplicate
sums, target-safe threshold error, and the actual-coefficient lower
bound

\[
 \mathfrak M_6\gg X^3H
\]

are correct. In particular the lower bound survives the *integrated*
absolute-value placement: the report proves a fixed coefficient sign
and a common positive rotated phase throughout the whole displaced
interval, rather than integrating a pointwise positive majorant.

The primitive-frequency count is valid in the shrinking interval of
width comparable to 1/H. Its elementary error is smaller than its main
term uniformly throughout the complete middle range. The actual
variable h(x) is retained, and the selected interior window is used
only to obtain a uniform positive amplitude lower bound.

The majorant includes exact and near triple relations. No conclusion
after exact-relation deletion is proved or claimed. The lower bound is
for the sum of absolute values of separate sextuple integrals, not for
the signed sixth moment and not for a majorant formed only after
cancelling all sextuples at a common total frequency. The report
consistently preserves these distinctions.

The resulting certificate exceeds the sufficient sixth threshold by
at least `T^(517/250)` before epsilon losses. It gives no new complete
moment bound; the accepted complete twelfth exponent remains `10 beta`.
No mathematical correction was needed. Six raw carriage-return TeX
rendering defects were reported before review closure, repaired by the
claimant without changing the mathematics, and the finalized version
above was rechecked.

## 2. Exact hypotheses and reviewed scope

Use real T, X=T^2, J=[X/2,3X], and every dyadic
`T^(52/125)<N<T^(99/125)`. Set H=T/sqrt(N),
`h(x)=2sqrt(x)/sqrt(N)`, and retain the fixed actual mollifier and
nonnegative partition from Round205. All lower bounds are for
sufficiently large T uniformly over this band, as the claimant states.

The spatial kernel is

\[
 F(u)=-\int_1^2a_{N,T}(t)\sin(2\pi tu)\,dt,
 \qquad a_{N,T}(t)=t^{-1}\Psi(\sqrt{N/T}\,t)v(t^2),
\]

and E_N is the centered actual-r2 filter with argument `(m-x)/h(x)`.
The Fourier convention is `Fhat(xi)=integral F(u)e(-xi u)du` and the
rational expansion uses `e(-lambda x)`. The frozen cutoffs are
`M=ceil(6X)`, `D=floor(sqrt(M))`, `L=floor(M/(D+1))`.

The reviewed rational sum Q_N includes both arms, every harmonic, all
exact duplicate fractions and the strict quotient mask `D ell<x`.
The finite frequency set is the union of all labels that occur for
some x in J, with their coefficient functions allowed to be zero on
part of J. The majorant is exactly

\[
 \mathfrak M_6=
 \sum_{\lambda_1,\ldots,\lambda_6}
 \left|\int_J\prod_{j=1}^6c_{\lambda_j}(x)
                      e(-x\sum_j\lambda_j)\,dx\right|.
\]

All absolute values occur separately after the individual sextuple
integrations. Because Q_N is real, this is the termwise majorant of
its actual sixth-power expansion. It is not the integral of the sixth
power of the coefficient l1 norm.

The sufficient comparison threshold is
`T^(129/25-6 omega(alpha)+epsilon)`, where N=T^alpha,
`omega=min(alpha/4,beta,(1-alpha)/2)` and
`1/8<beta<27/208`. Its sufficiency is the inherited certificate, not a
necessary condition on the actual twelfth moment.

## 3. Independent derivation of the audited seams

### Orientation, periodicity and both character arms

The sine transform gives
`Fhat(xi)=(i/2)a(xi)` for positive xi in [1,2] and its negative for
negative xi, with zero elsewhere. For a progression r modulo q,
ordinary Schwartz Poisson summation gives

\[
 \sum_{m\equiv r\ (q)}F((m-x)/h)
 =\frac hq\sum_k\widehat F(hk/q)e(k(r-x)/q).
\]

Consequently the quotient difference of residues ell and 3ell modulo
4ell has Gauss factor

\[
 e(k/4)-e(3k/4)=2i\chi_4(k).
\]

For k=1 it equals 2i; for k=3 it equals -2i; for even k it vanishes.
This verifies the sign in the claimant's (12)--(15), with the stated
orientation. The coefficient four from r2/4 converts the quotient
Poisson prefactor to `2ih/ell`; it is not missing.

The small arm is restricted automatically to odd d. In a reduced
positive frequency k/d=a/q, q is therefore odd and
`d=jq`, `k=ja`. Complete grouping gives

\[
 c^A_{a/q}(x)=\frac{4h\chi_4(q)}q\widehat F(ha/q)
                  \sum_{j\le D/q}\frac{\chi_4(j)}j.
\]

For the quotient arm surviving k is odd. The reduced denominator is
therefore divisible by four. Writing the frequency uniquely as
`a/(4b)` with a odd and (a,b)=1, all original labels are
`ell=jb`, `k=ja`. The exact grouped coefficient is

\[
 c^B_{a/(4b)}(x)=\frac{2ih\chi_4(a)}b\widehat F(ha/(4b))
       \sum_{\substack{j\le L/b\\j<x/(Db)}}\frac{\chi_4(j)}j.
\]

The strict mask correctly includes no j satisfying equality. All
nonempty partial sums here lie between 2/3 and 1: their nonzero terms
are the alternating decreasing odd reciprocal series starting at one.
Thus the grouped coefficients are physical coefficients, not an
artificial array with the same envelope.

Odd reduced denominators cannot equal reduced denominators divisible
by four. This proves exact single-frequency disjointness, while saying
nothing about exact or near equality of sums of three frequencies.
Negative-frequency coefficients are conjugates: the first arm is
purely imaginary with odd conjugate symmetry, and the second is real
with even symmetry. Hence Q_N is real, which licenses the sixth-power
expansion used by the claimant.

The zero harmonic vanishes. Every complete progression with q<h/2
vanishes because its nonzero Fourier samples have modulus greater
than two. This is applied only after completing the progressions;
the moving threshold remainder is separately retained. No fundamental-
harmonic restriction or deletion of the quotient arm occurs.

### Completion tails, moving masks and real endpoints

The exact divisor split for positive m<=M is exhaustive: d<=D in the
first arm; d>D implies `ell=m/d<=M/(D+1)` in the second, and the
converse is `ell|m` and `m>D ell`. Thus each actual divisor is counted
once. The central constant density is annihilated by complete
Schwartz Poisson summation for h>2.

The smooth cutoff equals one a distance comparable to X on either
side of every x in J. Removing it from O(T) explicit progression sums
costs only a rapidly small tail, since X/H tends to infinity by a
fixed power. This does not require extending the hyperbola identity
itself to the introduced remote integers. The claimant explicitly
makes that distinction.

For a threshold t_ell=D ell, a crossing lattice term obeys
`|m-x|>=|x-t_ell|`. A one-sided lattice tail, bounded by its nearest
term and its tail integral, gives

\[
 |\mathcal R_N(x)|\ll_A\sum_{\ell\le L}
  (1+H/\ell)(1+|x-D\ell|/H)^{-A}.
\]

For ell<cT the threshold is at most X/4 if c is small, making the
entire contribution rapidly small for x in J. For ell>=cT the factor
`1+H/ell` is uniformly bounded. The remaining bumps have spacing
D comparable to T, greater than H by a fixed power, so their sum is
uniformly bounded. If u_ell denotes such a bump, then
`(sum u_ell)^p <= (sup sum u_ell)^(p-1) sum u_ell` for p=2 or 6.
Each bump has integral O(H), and there are O(T) labels. This proves
both the sixth and second error bounds O(TH), including bumps outside
J and partially intersecting its real endpoints.

This proof uses only h(x) comparable to H in an error bound; it does
not replace h in the exact formula. Strict threshold equality and
integer centers are valid: the crossing-distance inequality still
holds, and F(0)=0 if the central lattice point occurs.

### Actual physical sign and primitive fractions in a short interval

The use of actual nonnegative Fourier amplitude is justified.
Uniformly over the whole band, `N/T<=T^(-26/125)` tends to zero.
The fixed radial-mollifier transform is real, continuous and equals
one at zero. It is therefore positive on every sampled argument
`sqrt(N/T)t`, 1<=t<=2, for sufficiently large T. Since v>=0, a is
nonnegative on its full support. Since v is a smooth nonzero
nonnegative function, it is positive on some fixed compact interval
inside (1,2), and a is bounded below there uniformly.

Choose a positive-amplitude interval [u,v], narrower fixed inner
endpoints u'<v', and h0=2H. For a sufficiently small fixed delta>0,
the exact relation `h(x)/h0=sqrt(x/X)` ensures

\[
 h(x)\lambda\in[u,v]
 \quad\hbox{if }x\in[(1-\delta)X,(1+\delta)X],\quad
                  \lambda\in[u'/h0,v'/h0].
\]

There is no fixed-width replacement in this statement. The selected
frequency labels remain fixed while their actual coefficients vary
with x.

For each odd q in [D/2,D], Möbius inversion counts primitive positive
numerators in the interval `[u'q/h0,v'q/h0]` as

\[
 \frac{v'-u'}{h0}\varphi(q)+O(\tau(q)).
\]

The O(1) lattice-endpoint error for each divisor of q proves this
uniformly; the interval is allowed to shrink relative to q. There is
no appeal to equidistribution of reduced residues on short intervals.
Summing the main term over odd q is justified by

\[
 \sum_{q\le Y,\ q\ {\mathrm{odd}}}\varphi(q)
 =\frac{Y^2}{4}\sum_{d\ {\mathrm{odd}}}\frac{\mu(d)}{d^2}
                          +O(Y\log(2Y)).
\]

Indeed write q=dm with d,m odd and use
`sum_(m<=Z, m odd) m=Z^2/4+O(Z)`. The truncated main series has
tail O(1/Y), and its limit is the positive Euler product over odd
primes. Differencing at D and D/2 gives a positive constant times
D^2. Also `sum_(q<=D)tau(q)<<D log(2D)` by divisor-pair counting.
Thus the total primitive count is

\[
 |\mathcal C|\asymp D^2/H,
\]

because `D/H` is comparable to sqrt(N), at least a fixed multiple of
`T^(26/125)`, and dominates the logarithmic counting error uniformly.
This verifies the quantitative seam of claimant (20)--(22).

For this denominator interval the duplicate sum is exactly one:
`1<=D/q<=2`, and chi4(2)=0. Hence

\[
 c_\lambda(x)=i\chi_4(q)b_\lambda(x),\qquad
 b_\lambda(x)=2h(x)a(h(x)\lambda)/q\ge0\quad(x\in J),
\]

and `b_lambda(x)>=cH/D` on the fixed inner interval J0. The sign is
fixed on all of J, even where the amplitude vanishes. Applying this
same count separately with each h(x) also proves the claimed lower
coefficient norms `||c(x)||1>>D` and `||c(x)||2^2>>H` uniformly.
The upper coefficient norms follow from support, counting at most
`O(1+q/h)` numerators per denominator, and the bounded duplicate
prefixes. The quotient mask only removes a prefix; it introduces no
unbounded coefficient factor. Thus claimant (17) is correct.

### Triple bins, integration over the whole displaced window and X^3 H

Assign each lambda in C the weight `w_lambda=cH/D`, with c small
enough that `b_lambda>=w_lambda` on J0. Then
`sum_C w_lambda` is comparable to D. All ordered triple sums lie in
an interval of length O(1/H). Partition it into bins of width zeta/X,
with zeta a fixed sufficiently small positive number. There are
O(X/H) bins, including any partial end bin. If m_j is the total
product weight of triples in bin j, then

\[
 \sum_jm_j=\left(\sum_{\lambda\in\mathcal C}w_\lambda\right)^3
                  \asymp D^3,
 \qquad
 \sum_jm_j^2\gg D^6H/X.
\]

This is Cauchy--Schwarz for nonnegative triple weights. It counts
ordered pairs of triples, allows repeated labels, and includes the
exact equality cases. Each pair maps to a unique ordered sextuple
`(lambda1,lambda2,lambda3,-mu1,-mu2,-mu3)` in the complete majorant.
It has `|Delta|<=zeta/X`.

For this sextuple, its coefficient product is the real fixed sign
`product chi4(q)` times `product b_lambda(x)`: the complex constants
give `i^3(-i)^3=1`. Remove that sign and multiply the integral by
the unit factor e(X Delta). The real part becomes

\[
 \int_J\prod b_\lambda(x)
                     \cos(2\pi(x-X)\Delta)\,dx.
\]

On J, `|x-X|<=2X`. Taking, for example, any fixed zeta<1/12 makes
the cosine at least 1/2 throughout J. Since every b is nonnegative
throughout that *entire* window, the complement of J0 cannot cancel
the positive contribution from J0. The absolute value of the original
integral is therefore at least

\[
 cX\prod w_\lambda.
\]

Summing over all within-bin ordered triple pairs proves
`mathfrak M6 >> X*(D^6H/X)=D^6H`, and D comparable to sqrt(X)
gives `mathfrak M6 >> X^3H`. This argument directly verifies the
placement of the absolute value after integration. A subinterval
lower bound without the fixed global sign and phase rotation would
not suffice; both necessary ingredients are present here.

The chosen first-arm sextuples form a positive subsum of the
majorant because each of its terms is an absolute value. They do not
form a positive subsum of the signed sixth integral. All second-arm
and mixed sextuples remain in the complete majorant and in Q_N.
No independence or orthogonality assumption is used.

### Restored powers and complete-range comparison

The lower scale is `X^3H=T^(7-alpha/2)`. Dividing by the sufficient
threshold `T^(129/25-6 omega)` gives excess exponent

\[
 d(\alpha)=46/25-\alpha/2+6\omega(\alpha).
\]

The accepted beta bounds put `4 beta` and `1-2 beta` inside the
middle interval, in that order. The three pieces of d are

\[
 46/25+\alpha,\qquad
 46/25-\alpha/2+6\beta,\qquad
 121/25-7\alpha/2.
\]

The first has lower endpoint value 282/125. The middle has minimum
`67/50+7 beta>443/200`. The last has minimum at the upper boundary,
equal to 517/250. Hence the claimed complete-range lower excess is
correct, with uniform fixed constants before small epsilon losses.

The actual shell bridge supplies amplitude R^(-1/2), and
`dR=dx/(2sqrt(x))`; their sixth conversion is exactly T^(-4).
Multiplication by the available block supremum to the sixth power
therefore gives the certificate `T^(-4+6 omega)K6`. The freezing error
contributes at most
`T^(-4+6 omega)TH=T^(-2-alpha/2+6 omega)<=T^(-2+alpha)`,
which is negligible uniformly. The curvature error and the rapid
tails have the powers stated by the claimant and the independently
reviewed predecessor bridge.

The actual variance for E_N transfers to Q_N because the freezing
error has second moment O(TH), smaller than XH. Combining this
variance with `sup |Q_N|<<T` proves the lawful but weak signed bound
`integral |Q_N|^6<<T^4 XH T^epsilon=X^3H T^epsilon`.
The stronger inherited sixth estimate and complete p12 bound remain
stronger. The report correctly does not promote this interpolation
as a new gain.

Finally, no comparison above turns a sufficient arithmetic input into
a necessary condition for the twelfth moment. The majorant's excess
refutes only the specified way of certifying that input. Summing all
middle blocks by the physical norm inequality retains cross-block
terms and costs logarithmic factors only; no subrange is omitted.

## 4. First doubtful or unproved step

No mathematical gap was found in the finalized report under the
stated inherited dependencies. The complete actual signed sixth
estimate sufficient for the milestone remains unproved.

The first invalid extension would be to infer a signed-moment lower
bound from `mathfrak M6>>X^3H`, or to claim that the same lower bound
survives removing every exact rational triple relation. The binning
proof retains those exact relations. The accepted square-root exact-
resonance result is a different object and supplies no automatic
subtraction estimate here.

Likewise, the report does not obstruct cancellation among sextuples
after grouping them by their complete total frequency. That is a
different absolute-value placement. The distinction is explicit in
both the result and first-gap sections of the claimant.

## 5. Controls and outcomes

| Seam | Outcome |
|---|---|
| Fourier orientation and Gauss phase | GREEN: Fhat positive branch is i a/2; e(-lambda x) gives quotient factor +2i chi4(k). |
| Both arms and duplicate sums | GREEN: odd and four-divisible reduced denominators; exact character prefixes and strict quotient upper bound. |
| Primitive numerator count | GREEN: interval-wise Möbius inversion, positive odd totient mean, error O(D log D) dominated uniformly by D^2/H. |
| Actual physical sign/core | GREEN: actual Psi is positive on sampled arguments for large T; nonzero v gives a fixed positive core; coefficient signs are fixed throughout J. |
| Variable width/full displaced window | GREEN: exact square-root width on J0; amplitudes nonnegative on all J; rotated phase positive over all J. |
| Triple bins and multiplicity | GREEN: ordered triples, all repeated labels, O(X/H) bins, injective selection of the balanced ordered sextuples. |
| X^3 H lower bound | GREEN: product of the integrated cX factor with weighted collision mass D^6H/X, then D^6 comparable to X^3. |
| Thresholds, endpoints and tails | GREEN: complete O(TH) second/sixth error, strict equality retained, all real-window and remote-lattice tails paid. |
| Restored powers and all middle scales | GREEN: T^(-4), W0^6, negligible freezing contribution, and uniform excess 517/250 verified. |
| Exact+near versus exact-deleted | GREEN for the stated exact+near majorant only; no exact-deleted lower bound is asserted. |
| Absolute majorant versus signed moment | GREEN: positive subsum is used only inside the sum of absolute sextuple integrals. |
| Source and full-proof scope | GREEN: inherited qualified inputs only; no new source import, p12 improvement, M1/M2 conclusion or quarter theorem. |

All checks were analytical. Hash verification and formatting inspection
are provenance checks, not mathematical numerical evidence.

## 6. Exact dependencies and finalized artifact

The finalized reviewed report has SHA-256
`f34a4a56d076bf9aa369181feac45a60bf387a38976ac7470f74244785e3cf19`.
The initial version read had hash
`65e64971bb01a34e0fbe6af6186f4f90ec282cccda0203cd4b46432acb90db54`.
The sole intervening change repaired six raw carriage returns inside
intended TeX `\rm` tokens. The repaired lines and final hash were
rechecked before freezing this review. No mathematical revision was
requested or required.

Exact local interfaces used, already read in this reviewer's bounded
Round207 assignment and rechecked as needed:

- `protocol.md`.
- `rounds/codex-managed/gc-signed-rational-filter-attack/reports/signed_rational_moment_attack.md`, finalized hash above.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reports/actual_divisor_shell_attack.md`: centered additive filter, complete tails and exact hyperbola convention.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/controls/conductor_sixth_moment_power_ledger.md`, SHA-256 `0a60519b209389501b62a82225e5ca9506cf01c0e739acab8d7836b05d275f5a`: variance, suprema, sufficient threshold and stronger inherited sixth estimate.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reviews/independent_divisor_obstruction_review.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reviews/independent_bridge_power_review.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md`, SHA-256 `f297dadc44d0113097d6549650228992b6e969740b75e25451eab3a514cebffb`: fixed physical filters, complete middle bands and outside-band scope.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, SHA-256 `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`: inherited complete distribution/moment comparison.

The review is explicitly post-report and does not claim blind isolation.
The reviewer had already derived the periodic interface in a separate
bounded discovery assignment; that discovery report remained frozen
and was not used as substitute evidence for the majorant proof here.
No other Round207 report or new source theorem was read for this review.

## 7. Recommended state effect

**Retain the accepted mathematical state unchanged.** Mark the reviewed
artifact GREEN as a scoped actual-coefficient obstruction to the
specified integrated rational sixth majorant. It supports a no-gain
closure with the exact+near, norm-placement and sufficient-certificate
qualifications preserved.

The complete signed arithmetic moment, full twelfth target, all M1/M2
parents and quarter theorem remain open. No proof-graph promotion is
implied by this compatible auxiliary calculation.

Only this assigned review was written. No discovery report, shared
state, proof draft, validation matrix, synthesis, source card, legacy
artifact or successor file was edited. This review stops here.
