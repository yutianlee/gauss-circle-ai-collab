# Round 205 conductor: complete middle-band arithmetic interface

Campaign: gc-full-frontier-moment-strategy-review. Date: 2026-09-26.
Role: conductor analytical strategy derivation, candidate pending independent
review; not an accepted graph addition. Starting graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

## 1. Result

The complete twelfth-moment milestone reduces, with all other frequencies
estimated, to the actual smooth middle band

\[
 T^{52/125}<N<T^{99/125},\qquad N=2^j.
\]

This is a strategy reduction, not a gain on the remaining band. The first
unproved estimate is its complete moment of order T^(29/25+epsilon).
A signed arithmetic shell formulation gives a concrete prospective attack
using short-interval correlations of r2, with its coefficients and curvature
retained. Repeating the Poisson transform or estimating the shell absolutely
does not supply that estimate.

## 2. Exact statement and hypotheses

Use the actual Psi from the fixed radial mollifier and the complete series
H=B_(T,0) of the accepted Round204 kernel. Let R belong to a fixed interval
I=[cT,CT], 0<c<C, and use Lebesgue measure there. All assertions also hold
with a fixed bounded nonnegative window w(R/T). Fix a smooth nonincreasing
phi on the positive real axis, equal to1 for x<=1 and0 for x>=2, and set

\[
 v(x)=\phi(x/2)-\phi(x),\quad
 H_N(R)=\sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})v(n/N)
          \cos(2\pi R\sqrt n-3\pi/4).
\]

Here0<=v<=1, its support is [1,4], and N=2^j, j>=0.
Set Z=T^(3/2), J=floor(log_2 Z), and N_max=2^J. Split these finitely
many blocks into low N<=T^(52/125), middle T^(52/125)<N<T^(99/125),
and high N>=T^(99/125). Write H_mid for the sum of all middle blocks.
Equality at either dividing point belongs to the estimated outer part.

The asserted reduction is

\[
 \int_I|H-H_{\rm mid}|^{12}dR\ll_\epsilon T^{29/25+\epsilon}. \tag{M1}
\]

Consequently the complete milestone for H holds if and only if the same
upper bound holds for H_mid, at the epsilon-loss level. The equivalence is
by the triangle inequality, and does not mean the moments are equal.

## 3. Derivation and all powers

For every integer n>=2,

\[
 \sum_{j=0}^Jv(n/2^j)=\phi(n/(2N_{\max}))-\phi(n)
                    =\phi(n/(2N_{\max})).
\]

Thus H is exactly the singleton n=1 plus these blocks plus a residual
supported on n>2N_max>=Z. The singleton has bounded size. The residual
has l1 norm O_K(T^(-K)) by the actual Schwartz bound in Round204 (L9).
Neither lower endpoint nor the infinite upper tail is discarded.

The coefficient energy of each block is O_eta(N^(-1/2+2eta)). Split
the support [N,4N] into at most two ambient dyadic intervals and use
Round204 (L6)--(L10), with zero extension and the actual coefficients.
For V>=1 this proves

\[
 |\{R\in I:|H_N(R)|>V\}|\ll_\epsilon
 T^\epsilon(V^{-2}+TV^{-136/13}).                         \tag{M2}
\]

The cosine is bounded by the modulus of its complex sum. This argument
uses coefficient energy, not an invalid weighted exponent pair.

The divisor bound gives |H_N|<<N^(1/4+eta). The complete radial Poisson
calculation from Round203 gives the additional bound

\[
 |H_N(R)|\ll_\epsilon T^{1/2+\epsilon}N^{-1/2}
                  +O_\epsilon(T^{-1/2+\epsilon}).         \tag{M3}
\]

Its proof extends from support [1,2] to [1,4] by the identical rescaling
on a fixed compact positive interval; alternatively partition v into
two fixed smooth pieces supported on slightly enlarged dyadic intervals.
All constants remain fixed. N<=T^(3/2) satisfies that proof's condition
N<=T^(1+alpha) with alpha=1/2. Its lattice-shell count keeps the +1 term
until using N<T^2. All R are real, including lattice radii.

Let W>=1 be any upper bound for |H_N|, after harmless constants and
small epsilon losses. Layer cake applied to (M2), with trivial measure
O(T) below V=1, gives

\[
 \int_I|H_N|^{12}\ll_\epsilon
 T^{1+\epsilon}+T^\epsilon W^{10}
                    +T^{1+\epsilon}W^{20/13}.            \tag{M4}
\]

For low N use W=max(1,C N^(1/4+eta)). The two possible powers are
N^(5/2) and T N^(5/13). With N<=T^(52/125), they are bounded by
T^(26/25) and T^(29/25), respectively. The separate limits supplied
by those terms are N<=T^(58/125) and N<=T^(52/125).

For high N use W=max(1,C T^(1/2+eta)N^(-1/2)). The two possible powers
are T^5 N^(-5) and T^(23/13)N^(-10/13). For N>=T^(99/125), they are
bounded by T^(26/25) and T^(29/25), respectively. The separate lower
limits are N>=T^(96/125) and N>=T^(99/125). Where W=1, the bound is
O(T^(1+epsilon)), so no issue occurs beyond N=T.

Minkowski's inequality over O(log T) blocks, followed by raising to
the twelfth power, costs at most a fixed logarithmic power. Choose all
input eta small enough for the requested final epsilon. Add the singleton
moment O(T) and rapidly small tail. This proves (M1).

This argument crucially uses the distribution estimate. The mere outer
supremum T^(13/125) would give the much larger bound T^(281/125)
and does not prove (M1).

For a concrete arithmetic formulation let

\[
 L_{N,T}(z)=\int_0^\infty r^{-1}\Psi(r/\sqrt T)v(r^2/N)
                       \sin(2\pi zr)\,dr,
\qquad S_N(R)=\sum_{m\ge1}r_2(m)m^{-1/4}L_{N,T}(R-\sqrt m).
\]

The same complete Round203 formula gives

\[
 H_N=S_N+O_\epsilon(T^{-1/2+\epsilon}N^{-1})+O_K(T^{-K}). \tag{M5}
\]

The kernel is odd, L(0)=0, and |L(z)|<<_A(1+sqrt(N)|z|)^(-A).
Both far dual tails and the zero dual vector have already been paid in
the cited derivation. Summing its errors over the middle band is harmless
in L12. Hence the new, complete arithmetic objective can be written

\[
 \boxed{\int_I\left|\sum_{T^{52/125}<2^j<T^{99/125}}
                 S_{2^j}(R)\right|^{12}dR
              \ll_\epsilon T^{29/25+\epsilon}.}          \tag{M6}
\]

A uniform bound of the same order for each S_N in the full middle range
is sufficient by Minkowski; it is stronger than (M6) and is not assumed.
The exact center m is R^2~T^2 and its effective width is h=T/sqrt(N).
Over the middle range, T^(151/250)<h<T^(99/125), or in X=T^2 notation
X^(151/500)<h<X^(99/250). The argument R-sqrt(m) and factor m^(-1/4)
are exact; no unpriced linearization of the odd filter is used.

Using Round204's complete M12 and (M1) gives the existing baseline for
the entire middle sum, T^(10beta+epsilon), beta=2theta-1/2. Thus (M6)
requires a net moment power saving 10beta-29/25, approximately0.1296635.
It would imply the sharp moment Y^(102/25+epsilon), and monotonicity
would give pointwise exponent102/325, below theta but above1/4.
For that implication choose I=[T/sqrt(2),sqrt(3)T], or a window bounded
below by1 there, to cover x in [Y/2,3Y]. The points x in [Y,2Y] then
have their required one-sided persistence interval inside the moment
domain for large Y. A merely nonnegative window with gaps cannot by
itself justify this pointwise inference.

## 4. First unproved step

(M6) is open. A prospective method must estimate the actual signed
short-shell correlations of r2, retaining the odd weights and all
cross terms, or prove the stated uniform single-block alternative.
The absolute shell count only gives (M3) and is insufficient on the
middle band. A quantitative higher correlation theorem must apply to
these thin ranges, repeated shifts, and weights, with an error smaller
than the required normalized power. Merely naming a nilsequence,
spectral, random-model, or divisor-correlation theorem does not do so.

## 5. Required controls and outcome

Analytical controls: singleton and all infinite tails retained; exact
partition telescopes; division endpoints assigned; both terms in (M2)
integrated; all logarithmic and epsilon costs paid; real radii allowed;
L(0)=0; physical r2 coefficients and curved phase retained. PASS at
conductor level, pending independent review. No numerical experiment.

A generic aligned coefficient peak can saturate the old high-moment
power; it is not the actual r2 shell. Removing its diagonal without
arithmetic input remains invalid. Positive near-resonance mass is not
a lower bound for the signed moment. The reduction does not claim that
the middle band is small or that any M1/M2 parent is closed.

## 6. Exact dependencies and artifacts

- protocol.md; state/proof_obligations.yml; state/active_campaign.yml;
  strategy/round205_full_frontier_strategy_review.md.
- proofs/kernels/gc_complete_square_root_large_values_moment_bound.md,
  especially Sections3--6. Accepted graph dependency for (M2) and baseline.
- rounds/codex-managed/gc-complete-signed-convolution-attack/controls/
  conductor_radial_poisson_analysis.md, (P1)--(P5), and its exact-hash
  reviews/independent_radial_poisson_review.md in that campaign.
  This prior calculation is reviewed evidence, not a newly promoted node.
- strategy/gauss_circle_strategy_review_2026-09-23.md, moment-persistence
  bridge, independently rederived in the present isolated task.

## 7. Recommended state effect

No graph or proof-draft change. Review and archive this as the costed
strategy interface for a possible successor, chosen only at Round205
closure. Every accepted theorem, open parent and external qualification
stays unchanged. If the next arithmetic attempt produces only (M5) or
absolute shell bounds again, close it as no gain rather than replacing
(M6) with smaller unestimated sectors.
