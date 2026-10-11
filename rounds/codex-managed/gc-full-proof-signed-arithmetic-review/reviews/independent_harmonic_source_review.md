# Round 208 independent harmonic-source and selection review

Campaign: `gc-full-proof-signed-arithmetic-review`. Reviewer:
`arithmetic_full_frontier`, in the separate same-round review role.
Date: 2026-09-27. Review mode: independent line/source audit, not blind.
Graph SHA256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Effort: 100 percent analytical/algebraic/source inspection. No mathematical
experiment. Only this assigned review is written.

## 1. Result

**GREEN for the scoped source/application-cost and strategy-selection
review at the final hashes in Section 2.** Guth--Maldague Theorems 4 and 5
are correctly identified as parabola statements in the inspected v2.
The p=12 cap estimate, exact lift, paid line trace and amplitude-envelope
trace in H7 and H9--H12 have the stated powers. They establish no new
complete arithmetic saving. The new conductor gate B8 is an unproved
complete tenth-moment condition, derived without importing a saving from
either Guth--Maldague theorem.

One mathematical wording defect was reported and repaired during review:
the general H8 formula initially omitted the reconstruction-error floor
when its putative radius exponent E_p is less than one. It now uses
`E_p^*=max(1,E_p)`. The repair changes none of the E_p>=1 applications
or the sufficient unbounded-fixed-order conclusion. The conductor's
last source-scope reference was also corrected from B5 to the selected B8.
Both changes were reread and their final hashes verified.

GREEN does not mean that B8, H4 or H12 is proved, that an external paper's
entire proof was independently checked, or that M1, M2, the pointwise
benchmark or the quarter theorem has improved.

## 2. Exact statements, hypotheses and reviewed hashes

The reviewed final files are:

| Artifact in this campaign | SHA256 |
|---|---|
| `reports/harmonic_current_sources.md` | `8af1b4e373c27706f50f3b59ac077d8327cb01c4f2b3767cbdbbb2c9eb0c773e` |
| `controls/conductor_bandlimited_strategy.md` | `6aa17dd35e2d930cedadfb489adf8e042b6aed61ed5882ae8e2eb0cd36fbd552` |

The originally read hashes, before the two reported corrections, were
`f7ba9d89e0c6bf772d7d3c52768c8101452c99ea1064381d7c015b4d524e8734`
and
`962bba63cb9865fddcb6bbf838b8e2ac50a95ddf9a1f70cbebf6b5cd0006b658`,
respectively. The conductor's intermediate repaired hash was
`e07ef450628814c77f5341c6ccfb2081bb2bfdd0044497329d9a00cb06bb6c7d`.
One final paragraph clarified the direction of implication between
the old sixth-moment certificate and B8. The whole conductor file was
reread and that paragraph checked before rebinding this review to
the final hash in the table. The verdict attaches to the final hashes only.

The primary statement text was independently read at
[Guth--Maldague 2206.01093v2](https://arxiv.org/html/2206.01093v2),
introduction, Theorems 4--5 and their preceding definitions. The
[current official record](https://arxiv.org/abs/2206.01093) confirms v2,
13 August 2022, as the latest listed version on the date checked.

Theorem 5 concerns Fourier support in the R^-1 neighborhood of the
truncated parabola, caps of dimensions R^-b by R^-1, `1/2<=b<=1`,
and `3/p+1/q<=1`. With p=12,q=2 its factor is precisely
`R^epsilon(2+R^(5b-1))` times the sixth power of the sum of squared
global L12 cap norms. The left side is local to a ball.

Theorem 4 is the two-dimensional amplitude-dependent level estimate.
Its envelopes have dimensions W by R, `sqrt R<=W<=R`, and its
threshold uses the average localized square function divided by the
square of the number of occupied coarse caps. The report preserves
that occupation count and the source's epsilon-dependent threshold.
Neither statement concerns a bare one-dimensional radius trace.

All algebra below concerns the literal coefficients
`a_n=r2(n)n^(-3/4)Psi(sqrt(n/T))zeta_N(n)`, their finite dyadic support,
and the retained bounds `A_N=sum|a_n|`, `E_N=sum|a_n|^2` from H6.
For the conductor gate, the inherited variance, block suprema, complete
shell identity and complementary-tail estimates are its explicit
inputs. This review checks their use and scope, not their full older
proof chains.

## 3. Independent derivation and application audit

### H7, H9 and H10: small caps and the line trace

Substitution p=12,q=2 in the source's three factors gives exponents
0,0 and `5b-1`. The admissibility sum is `3/12+1/2=3/4<=1`.
Thus H7 has neither an omitted source power nor a wrong endpoint.

In H9, after interchanging the two ambient coordinates, the frequency
is exactly `(xi_n,xi_n^2)` with `xi_n=sqrt(n/(2N))`. Its spacing is
comparable to 1/N. Evaluating x=0 and using `t=sqrt(2N)R` gives
the original complex square-root sum exactly, and
`dR=(2N)^(-1/2)dt`. No Taylor error enters this lift.

Write `L~T sqrt N` and `Rcal~min(L,N^2)`. For `2<=N<=T^(3/2)`
one has `N<=Rcal<=N^2`, up to fixed constants. Hence a cap of width
comparable to 1/N is within the permitted small-cap range. There are
O(1) frequencies per cap, also after broadening each frequency by a
sufficiently small Fourier bump of radius Rcal^-1. Fixed overlaps
or a bounded refinement only change absolute constants. For the
localized function,

\[
 \left(\sum_\gamma\|f_\gamma\|_{12}^2\right)^6
       \ll \mathcal R^2 E_N^6.
\]

The Rcal^2 is the full ambient area. Since `Rcal^b~N` and
`Rcal<=N^2`, the source factor is `O(N^5/Rcal)`. Thus the ambient
price on one interval is
`Rcal N^5 E_N^6<<Rcal N^(2+epsilon)`.

The trace is legal because the x-frequency is in a fixed compact
interval. A Schwartz reproducing kernel rho in x gives, by Holder,

\[
 |F_N(0,t)|^{12}\ll
       \int_{\mathbb R}|F_N(x,t)|^{12}|\rho(x)|\,dx.
\]

On the central rectangle, the chosen localization is bounded below;
the rectangle fits in a fixed enlargement of the source ball. Outside
it, the coefficient bound A_N and the Schwartz decay of rho pay an
arbitrarily high inverse power of Rcal. Such a localization can have
compact Fourier support and be bounded below on the chosen finite
rectangle without having compact physical support. The report does
not assume both kinds of compact support.

There are `O(1+L/Rcal)` t-intervals. Restoring that count and dR gives

\[
 N^{-1/2}(1+L/\mathcal R)\mathcal R N^2
             \ll TN^2,
\]

which verifies H10 in both regimes separated by `N~T^(2/3)`.
The tail of the reproducing weight is harmless after choosing a fixed
large decay order. Bounded N contributes O(T). With the actual
Schwartz decay for N>T, summing the L12 norms yields `M12<<T^(3+epsilon)`;
the infinite residual tail remains rapidly small. Multiplying by T^7
in sharp reconstruction yields `Y^(5+epsilon)`, with the smaller
sharp-error moment retained. This is an inferior upper certificate,
not a lower bound for actual arithmetic moments.

### H11 and H12: the amplitude-dependent trace

The derivative in the transverse x-variable obeys
`|partial_x F_N|<=C A_N` because `n/(2N)` is bounded. At each radius
where `|S_N(R)|>V`, `0<V<=A_N`, an interval in x of length
`cV/A_N` retains amplitude at least cV. The cutoff at scale
`L~T sqrt N` is bounded below there and on the entire displaced
t-window. Fubini and `dt=sqrt(2N)dR` therefore give ambient
level-set measure at least

\[
 c\sqrt N\,{V\over A_N}D_N(V).
\]

Apply the source's fourth-power level inequality at amplitude cV.
The resulting radius inequality is exactly

\[
 D_N(V)\ll T^\epsilon {A_N\over\sqrt N}
                     V^{-5}\mathcal E_{f_N}(cV).
\]

The extra V^-1 and A_N are necessary costs of this transverse
argument. Layer cake multiplies by V^11, leaving the V^6 integral
in H12. All occupied caps, envelope scales and selected envelopes
remain in E. The source does not bound this actual envelope integral
by the p=12 milestone. The report labels that final inequality
unproved, so it has not imported an arithmetic gain or discarded
aligned peaks.

### H8 repair and the separate conductor gate B8

Sharp reconstruction gives, for any stated radius exponent E_p,

\[
 \int |P(x)|^pdx\ll
 T^{1+p/2+E_p+\epsilon}+T^{2+p/2+\epsilon}.
\]

Consequently E_p must be replaced by `max(1,E_p)` in the general
pointwise certificate. The repaired H8 now does this. For every
application in the harmonic report E_p>=1 already; its conclusions
are unchanged. The condition `E_p=o(p)` along unbounded fixed p
remains sufficient after taking the maximum with one.

B8 has a different route. The actual finite H_N has Fourier support
in `[-2sqrt N,2sqrt N]`. A one-dimensional reproducing kernel on the
larger radius interval I, using its positive margin around each
target point, gives

\[
 |H_N(R_0)|\ll N^{1/20}
        \left(\int_I|H_N|^{10}\right)^{1/10}
        +O_A(T^{-A}).
\]

The off-I tail is paid by the **global** finite coefficient bound,
not by extending a local supremum. With the stated actual shell
identity, Jacobian and error,

\[
 \int_I|H_N|^{10}\ll T^{-6}K_{10}(N)
                     +T^{-4+\epsilon}N^{-10}+O_A(T^{-A}).
\]

Set `b=83/650`. The candidate

\[
 K_{10}(N)\ll T^{473/65+\epsilon}N^{-1/2}
\]

gives `M10(H_N)<<T^(83/65+epsilon)N^-1/2`, and hence
`|H_N(R0)|<<T^(83/650+epsilon)`. The N^(1/20) and
N^(-1/20) cancel. The propagated shell error is harmless. This is
elementary reproduction and algebra; neither Guth--Maldague estimate
enters this implication.

The full required band is
`T^(166/325)<N<T^(242/325)`. Its two endpoints are assigned to
the known pointwise complement bounds `N^(1/4)` and `(T/N)^(1/2)`.
The band is contained in the older reviewed shell band. The singleton,
all dyadic blocks, both cosine phases and the infinite high tail are
retained. Uniformity is for real radii, with the final sharp count's
jumps covered by reconstruction. Thus B8 is a complete sufficient
gate for `1/4+b/2=102/325`, conditional on its unproved arithmetic
bound and the stated inherited inputs.

For the order-selection ledger, intersecting variance Chebyshev with
the known distribution and splitting at `V0=N^(13/220)` gives, for
`2<p<136/13`,

\[
 M_p(H_N)\ll T^\epsilon
 \left[TN^{-(136/13-p)/(2(136/13-2))}
                +T^{(p-2)\omega}\right].
\]

At p=10 this restores
`K10<<T^7N^(-3/110)+T^(6+8omega)`; both terms are present.
Subtracting B8 gives exactly
`d_A=1-10b+(26/55)alpha` and
`d_B=8omega-10b+alpha/2`.
Their difference is `8omega-1+3alpha/110`. It is positive at both
band endpoints and is affine, increasing on the first two omega
branches and decreasing on the last. Therefore d_B is the active
deficit. Its maximum is `7beta-101/130` at `alpha=1-2beta`.
This is a smaller deficit of the displayed certificates; it does
not prove that the actual ten-factor problem is easier.

The conductor's final comparison paragraph is also correct. The
old206 certificate gives `M6<<T^(29/25-6omega)`; multiplication
by the actual supremum to the fourth power yields
`M10<=W^4 M6<<T^(29/25-2omega)`, with the displayed shell errors
negligible. The available slack against the new target is
`10b-29/25-alpha/2+2omega`. It equals 38/325 on the first omega
branch, decreases on the later branches, and vanishes at the upper
endpoint, which is already assigned to a safe complement. Thus
old206 implies B8. Merely comparing the deficits of the new sixth
and tenth gates would not establish an implication between them,
and the final text makes no such claim.

The B8 arithmetic remains the complete signed shell with all m>=1,
the fixed r2 coefficient, actual odd filter, variable width and moving
hyperbola prefix. Its proposed fifth rational convolution must retain
both arms and all mixed, near and exact total-frequency relations.
An exact convolution identity alone gives no saving. The document
explicitly rejects treating such an identity, recovered variance or
deletion of the `T^(8omega)` radius term as success.

## 4. First doubtful or unproved step

There is no remaining source-statement or displayed normalization
error in the reviewed scope after the H8 repair. The outstanding
analytic estimates are H4/H12 and, in the changed strategy, B8 itself.
The latter is not a consequence of H7--H12. The report's broader
literature screen is not an exhaustive search theorem, and this
review does not independently certify every metadata entry in it.

The local reproduction argument proves a conditional implication.
The inherited exact shell bridge and complement estimates are still
inputs; their older proof files were not opened in this review.
For b approaching zero, the needed band expands. The conductor
correctly labels extensions of the bridge/complements as hypotheses
until separately verified. One fixed moment and the present fixed
band do not establish the full quarter theorem.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Primary theorem identification | GREEN: Theorem 4 is the parabola envelope result and Theorem 5 its small-cap estimate; cone dimensions are not substituted. |
| Source admissibility | GREEN: p=12,q=2 and b in [1/2,1] are legal; frequency broadening, Schwartz localization and occupied-cap thresholds are retained. |
| Trace normalization | GREEN: H10 pays ambient area, interval count and N^-1/2; H11 pays A_N V^-1 and N^-1/2. |
| Sharp reconstruction | GREEN after repair: H8 includes the E=1 floor. The repaired formula preserves the stated milestone and full-proof conclusions. |
| B8 source independence | GREEN: no external harmonic gain enters B8; its arithmetic inequality remains unproved. |
| Complete arithmetic scope | GREEN as a scope audit: both arms, all coefficients, variable width/prefix, full band, real endpoints and all complementary series pieces remain required. |
| Signed versus positive | GREEN: weak upper certificates and aligned-coefficient controls are not lower bounds on the actual r2 family. |
| Full-quarter scope | GREEN: B8 yields only the fixed 102/325 milestone; the all-k route and independent M1/M2 parents remain open. |

An aligned finite exponential polynomial confirms analytically that
the reproduction bandwidth factor cannot generically be deleted.
The harmonic report's complex absolute-value bound is explicitly a
stronger sufficient route than the signed cosine target. No numerical
experiment, guessed Gaussian pairing or deletion of an exceptional
set was used in this review.

## 6. Dependencies and artifacts used

This review used only the two same-round artifacts and exact hashes
listed in Section 2, the primary Guth--Maldague theorem text/current
record linked there, and the governing protocol/active-round context
already read under the original assignment. The review was explicitly
authorized to read the sibling report. The original arithmetic report
was not reread, reviewed or used as an independent authority here.
No blind report, other sibling review, shared synthesis, proof draft,
state patch or successor plan was inspected or edited for this review.

The initial H8 defect and stale conductor reference were sent to the
conductor promptly. The amended lines and both final file hashes were
then read directly from disk. The final old206-to-B8 interpolation
paragraph was separately reread and verified before the verdict was
bound to the last conductor hash.

## 7. Recommended state effect

Record this as **GREEN, scoped source/selection review** for the two
final hashes. Retain the corrected harmonic cost ledger and the
complete B8 candidate as strategy evidence. Do not promote an
arithmetic moment theorem, source gain, pointwise improvement, M1/M2
parent or quarter theorem. No shared proof-state change is recommended.

This review stops here and designs no successor.
