# Round 215 independent actual-wave seam review

Campaign: `gc-complete-localized-wave-moment`.
Reviewer task: `weighted_envelope_transfer`, reassigned to independent
same-round seam review after its original report was frozen.
Role: NONBLIND reviewer. Date: 2026-09-28, Asia/Shanghai.
Allocation: entirely analytical; zero experiments and no new source import.

Reviewed report:
`rounds/codex-managed/gc-complete-localized-wave-moment/reports/actual_lattice_envelopes.md`.
Verified SHA-256:
`4e7c9088141687087ceb8582028cbdffd3b66926fffca983c6086002ed7e6de6`.
Every verdict below binds this exact hash. The reviewed report and this
reviewer's original report remain unchanged.

## 1. Result

**GREEN for the assigned seam. No mathematical correction required.**

The exact angular decomposition, its multiplier bounds and all weight
transfers reproduce the sufficient envelope (A1). The finite duality
argument applies to the complex angular coefficient vectors after their
coefficient energy is checked; it does not rely on extending the final
statement for the full cosine series. Recombining all radius tails gives

\[
 C(T,N)\ll_\epsilon T^\epsilon
                   (T\sqrt N+N^{5/2}),
\]

with no missing window, angular, translation or spatial-tail factor.
This complete bound is insufficient for the frozen target on its open
band. The actual arithmetic input (A3) remains unproved.

The enlarged-array lower control has the asserted `N^(5/2)` size and
is correctly restricted to changed coefficients. It is not a lower bound
for the actual signed moment. The result licenses neither a new circle
exponent nor any M1/M2/GAR or quarter-theorem promotion.

## 2. Exact statement and hypotheses reviewed

The review uses the frozen actual `c_m`, `F_N`, product cutoffs, weight
`W(y)=C_A(1+|y|^2)^(-100)`, all centers `R_j`, the ceiling in `J`, and
every real parameter in
`T>=2`, `T^(166/325)<N<T^(242/325)`.
The cutoff clarification makes the central lower bounds valid on
`[-1,1]^2` and `[-1,1]`, with the dilation fixed initially.

The intermediate radius majorant is exactly

\[
 K=[R_0,R_J],\quad
 \rho(R)=\left(1+\frac{\operatorname{dist}(R,K)}{\sqrt N}\right)^{-2}.
\]

The exact angular coefficients and radial waves are

\[
 A_\ell(n)=\sum_{|m|^2=n}\exp(-i\ell\arg m),\qquad
 G_\ell(R)=\sum_n n^{-3/4}\Psi(\sqrt{n/T})v(n/N)
                    A_\ell(n)e(R\sqrt n).
\]

The accepted kernel inspected for the finite coefficient mechanism is
`proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`,
SHA-256
`942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.
Its Sections 3--4 give the unweighted square-root correlation bound and
finite duality with arbitrary coefficient vectors and real endpoints.
The report uses those proved mechanisms, not the stronger interpretation
that its final full-series cosine statement automatically covers every
angular mode. The external exponent-pair source remains an inherited
accepted dependency; this review adds no external source assertion.

## 3. Independent derivation and seam checks

### 3.1 Actual norm multiplicities and window recombination

All vectors with `|m|^2=n` have the same actual radial coefficient.
Grouping them gives exactly `A_0(n)=r_2(n)`. Rotation by `pi/2` multiplies
each angular term by `exp(-i ell pi/2)`, so `A_ell` vanishes unless
`ell` is divisible by four. Reflection conjugates the summands and
permutes the complete norm class, proving that `A_ell` is real and
`A_-ell=A_ell`. In particular `|A_ell|<=r_2` uniformly; rational rays
and repeated norms were not deleted.

An active fixed subannulus has `asymp N` lattice points. In the frozen
band the arguments of `Psi` tend uniformly to zero, so its positivity
there gives the large-parameter mass comparisons (A8). Upper bounds
hold without this positivity argument. The grouped energy is

\[
 \sum_n|b_nA_\ell(n)|^2
       \ll_\epsilon N^{-1/2+\epsilon},\qquad
 \sum_n|b_nA_\ell(n)|\ll N^{1/4},
\]

uniformly in every integer `ell`. These retain the distinction between
the lattice norm and the grouped norm with `r_2(n)^2`.

The substitution `u=sqrt(N)(R-R_j)` restores exactly one factor
`sqrt(N)`. Summing before estimating gives the identity (A10) with
`Q(R)=sum_j|eta((R-R_j)/sqrt(N))|^10`. Inside `K`, a nearest center is
at most `sqrt(N)/2` away, so `Q` is bounded below. Everywhere, the
Schwartz decay with exponent at least three, summed over the spaced
centers, gives `Q lesssim rho`. For example an exterior distance
`t sqrt(N)` gives a bound by `sum_(k>=0)(1+t+k)^(-3)`, of order
`(1+t)^(-2)`. This proves both parts of (A11) without losing a factor
`J`, while retaining the two real endpoints and all tails.

### 3.2 Angular Fourier signs, derivatives and translations

Expanding `e(t cos(alpha))` with coefficient
`(2pi)^(-1) integral e(t cos(alpha))exp(-i ell alpha)dalpha`, and using
`alpha=theta-arg(m)`, gives the sign and every `2pi` in (A13).
The smooth angular series converges absolutely at each fixed `r`, and
the lattice sum is finite. At zero radius only `ell=0` survives.

The frequency variable in the multiplier is
`lambda=sqrt(n/N)`. Fourier inversion of
`a_ell,r(lambda)=chi(lambda)h_ell(r lambda)` therefore produces the
translation `R-s/sqrt(N)` in (A14); it produces no extra scalar
`sqrt(N)` in the dimensionless `s` integral.

For `0<=q<=3`, differentiating in `lambda` introduces at most `r^q`.
Eight angular integrations by parts introduce at most eight further
factors of `1+r` and a factor `|ell|^(-8)` when `ell` is nonzero.
The trivial estimate covers zero. With fixed compact frequency support,

\[
 \max_{q\le3}\|\partial_\lambda^q a_{\ell,r}\|_\infty
 \lesssim(1+|\ell|)^{-8}(1+r)^{11}.
\]

Three frequency integrations by parts, plus the trivial estimate near
`s=0`, prove precisely
`|k_ell,r(s)| lesssim (1+|ell|)^(-8)(1+r)^11(1+|s|)^(-3)`.
All boundary terms vanish because the frequency cutoff is smooth and
compactly supported. No unestimated Bessel asymptotic is used.

The distance function is one-Lipschitz, giving
`rho(Z+t)<=rho(Z)(1+|t|/sqrt(N))^2`. After the tenth root and the
translation `t=s/sqrt(N)`, this becomes the factor
`(1+|s|/N)^(1/5)` in (A16). It is bounded by
`(1+|s|)^(1/5)` since `N>=1`; multiplying by the kernel's cubic decay
is integrable. This proves the claimed weighted translation estimate
uniformly in `N`, including every translation.

After Minkowski, the tenth power of the spatial cost is `(1+r)^110`.
The two-dimensional weighted integral has large-radius integrand of
order `r^(1+110-200)=r^(-89)`, hence converges. The angular weight
`(1+|ell|)^(-8)` is summable, and weighted Holder gives

\[
 \left(\sum_\ell w_\ell x_\ell\right)^{10}
 \le\left(\sum_\ell w_\ell\right)^9
                       \sum_\ell w_\ell x_\ell^{10}.
\]

These computations independently reproduce (A1), with its single
factor `sqrt(N)`. The infinite series cause no circular integrability
assumption: initially `|G_ell| lesssim N^(1/4)` uniformly and
`integral rho<infinity`, so the displayed majorants already justify
the limits and Minkowski applications.

### 3.3 Finite duality and the complete tenth-moment bound

For an ambient block `(L,2L]` and coefficients of squared norm at
most `A L^(-1/2)`, the accepted kernel gives
`|K_L(t)|<=A sqrt(L)(|t|^kappa+|t|^(-1))`, `kappa=13/55`.
For intervals of length `O(H)`, `H>=T`, the range
`L asymp N<T` is inside `L<=H^(3/2)` after fixed constants and bounded
parameters are handled. Difference arguments satisfy `|t|<=C H`,
including negative differences by conjugation. The interval's absolute
location is irrelevant to the Gram matrix.

For a maximal `L^(-1/2)` separated local set of `M` large values,
the exact Gram diagonal contributes `C A sqrt(L)` after division by
`M`. The two off-diagonal parts contribute respectively
`C A^2 M h^kappa` and `C A^2 sqrt(L)log(2+H sqrt(L))`.
This is (A18). Choosing
`h=(v^2/(C_0 A^2))^(1/kappa)` absorbs the first part.
Covering by the separated points gives the local measure cost
`A^2 log(2+H sqrt(L))v^(-2)`. The full number of subintervals is
`O(1+H/h)`, including one when `h>H`, yielding (A19).
This also treats a singleton large value and subintervals shorter than
the separation scale; there is no deleted Gram diagonal.

The support `[N,4N]` fits into at most three ambient dyadic blocks,
using zero coefficients at inactive integers. The checked grouped
energy supplies the coefficient hypothesis for each angular mode.
Every power of `A` is fixed, so using a sufficiently small input
subpower yields (A20), with constants independent of `ell`.

For the tenth moment, the first distribution term gives
`integral_1^(C N^(1/4)) v^7 dv=O(N^2)`. The second gives
`H integral_1^infinity v^(9-136/13)dv=O(H)`, because
`9-136/13=-19/13<-1`. The region below amplitude one costs `O(H)`.
Thus (A21) is correctly `H^epsilon(H+N^2)`.

For exterior distances of order `H_k=2^k T`, the majorant is at most
`N/H_k^2`. Summing both exterior intervals gives

\[
 \sum_{k\ge0}N H_k^{-2+\epsilon}(H_k+N^2)
 \lesssim_\epsilon T^\epsilon(N/T+N^3/T^2),
\]

for `0<epsilon<1`. The central region has length `O(T)`, since
`|K|=J sqrt(N)=dT+O(sqrt(N))`. Combining these regions proves
`integral rho |G_ell|^10 lesssim T^epsilon(T+N^2)` uniformly in `ell`.
This includes negative and arbitrarily distant radii. Summing the
angular weights and restoring `sqrt(N)` proves (A2).

### 3.4 Power and enlarged-family controls

The ratio of `N^(5/2)` to the frozen target is
`T^(-83/65)N^(5/2)`. Its lower endpoint is exactly
`N=T^(166/325)`. Also `N^2/T>1` throughout the band, so this term
dominates `T sqrt(N)`. The report correctly distinguishes a fixed
power distance above the endpoint from a subpolynomial approach.

The single global rephasing `c_m e(-R_*|m|)` creates amplitude
`gtrsim N^(1/4)` on a fixed small spatial disk and a radius interval
of length `asymp N^(-1/2)`. Its `u` length is of constant order.
A nearest original window has its cutoff bounded below there, so
the tenth weighted mass is `gtrsim N^(5/2)`. All coefficient moduli
and the finite-duality data survive this rephasing, which verifies
the claimed limitation of those coefficient-uniform inputs.
The rephased array is outside the frozen actual family.

Finally the fixed spatial bandwidth and the central cutoff lower
bounds reproduce (A25), including its factor `sqrt(N)`. Thus the
zeroth angular mode retains the original radial arithmetic problem.

## 4. First doubtful or unproved step

No unresolved step requiring correction was found in (A1), (A2) or the
stated enlarged-family control at the reviewed hash. The first missing
positive arithmetic estimate remains (A3), or a different complete
actual bound on (A10). The unweighted correlation estimate and grouped
coefficient energy do not remove the high-value `N^2` term.

The report makes no unsupported assertion that nonzero angular modes
alone imply the target, that a coefficient-uniform adversary is an
actual counterexample, or that a fixed tenth-moment milestone proves
quarter. These limitations are essential to the GREEN verdict.

## 5. Control tests and outcomes

| Control | Verdict |
|---|---|
| Exact lattice lift and norm multiplicity | GREEN: all signed representations and `A_0=r_2` retained. |
| Common radius modulation | GREEN: (A10) recombines the same wave; rephasing appears only in the labeled control. |
| Angular signs and Fourier normalization | GREEN: exact `2pi`, angular sign and dimensionless convolution variable checked. |
| Eight angular / three frequency derivatives | GREEN: powers `ell^(-8)`, `(1+r)^11`, `s^(-3)` reproduce. |
| Weighted translations and spatial tails | GREEN: translation exponent `1/5`; integrable radial power `-89`. |
| All windows and radius tails | GREEN: `Q lesssim rho`, central coverage, all exterior intervals and their convergent sum checked. |
| Finite coefficient duality | GREEN: full diagonal, harmonic row sum, localization ceiling and arbitrary interval center preserved. |
| Complete coefficient norms and narrow directions | GREEN: no angular occupancy assumption; all `A_ell` use full norm classes. |
| Source and real-scale hypotheses | GREEN: only the accepted kernel's proved finite mechanism is used, in its legal range; arbitrary real endpoints retained. |
| Restored power | GREEN: `T sqrt(N)+N^(5/2)` and its target comparison checked. |
| Actual versus enlarged coefficients | GREEN: the lower control is not applied to actual `c_m`. |
| Certificate versus signed lower bound | GREEN: no actual lower obstruction inferred. |
| Full-quarter and statement-only scope | GREEN: no quarter claim; this review is explicitly NONBLIND, not a replacement for the isolated control. |

No computation or experiment was used.

## 6. Dependencies and artifacts used

1. `protocol.md` and already permitted frozen graph/strategy context.
2. The reviewed report at the exact hash in the header.
3. The accepted Round-204 kernel at the exact hash in Section 2.
4. `rounds/codex-managed/gc-complete-localized-wave-moment/controls/cutoff_normalization_clarification.md`,
   SHA-256
   `579fb5d584a605fe7912fddbb718d5f5a6464c1336749e07ad7572d9a114de82`.

The conductor's reassignment expressly authorized the reviewed report
and the two added context files. No current sibling report, blind
packet/report, conductor kernel ledger, shared synthesis, validation
matrix or successor artifact was read. No new literature was consulted.
The review writes only its assigned review file; it does not change
the author's report or this reviewer's original report.

## 7. Recommended state effect

**GREEN: retain the reviewed report at the bound hash as independently
checked analytical evidence. No correction required.** Retain (A1) as
a complete sufficient envelope and (A2) as a valid insufficient upper
bound. Retain (A24) only with its enlarged-array scope.

No change to the accepted graph, proof draft, pointwise exponents,
M1/M2/GAR, endpoint obligations or the quarter target. The actual
estimate (C215) and its sufficient input (A3) remain open. This review
stops at the current same-round seam and designs no successor work.
