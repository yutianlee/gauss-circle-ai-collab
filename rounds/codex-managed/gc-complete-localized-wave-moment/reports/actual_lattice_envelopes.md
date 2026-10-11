# Round 215: actual lattice angular envelopes with complete costs

Campaign: `gc-complete-localized-wave-moment`.
Task: `actual_lattice_envelopes`; discovery, selected context, NONBLIND.
Generated: 2026-09-28 01:31 +08:00.
Frozen graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Status: candidate evidence only. Allocation: 100 percent analysis/algebra;
zero experiments and zero new primary-source imports. Only this report is
written. No sibling or statement-only packet/report was read.

## 1. Result: a complete actual angular reduction, without a new power gain

The fixed common modulation can be retained exactly while all radius
windows are recombined. An elementary angular Fourier decomposition then
gives the following complete sufficient envelope, with no additional power
of either parameter:

\[
 \boxed{\quad
 C(T,N)\ll \sqrt N\sum_{\ell\in4\mathbb Z}(1+|\ell|)^{-8}
       \int_{\mathbb R}\rho_{T,N}(R)|G_\ell(R)|^{10}\,dR.
 \quad}                                                     \tag{A1}
\]

Here all coefficients of every `G_ell` are the explicit actual angular
lattice sums in Section 2, and `rho` is a complete polynomial radius
majorant. The proof pays the full infinite angular expansion, all spatial
tails, all radius tails, and every original cutoff. In particular, (A1)
does not discard narrow or rational directions. Its zeroth angular
coefficient is exactly `r2(n)`, so fourfold symmetry does not itself
improve the actual radial problem.

Reproducing the needed finite-block consequence of the accepted
square-root correlation argument gives, uniformly for every angular mode,

\[
 \int\rho_{T,N}|G_\ell|^{10}\ll_\epsilon
       T^\epsilon(T+N^2),\qquad
 C(T,N)\ll_\epsilon T^\epsilon(T\sqrt N+N^{5/2}).           \tag{A2}
\]

These are valid estimates on the actual family, but not the frozen gain.
The angular reduction is a complete reformulation, not an improved
arithmetic estimate. Throughout the whole critical band `N^2>T`, so
the bound in (A2) is dominated by `T^epsilon N^(5/2)`.
The second displayed term has the target power only at
`N=T^(166/325)` and exceeds it for every strictly larger power scale.
An enlarged-coefficient control proves that its `N^(5/2)` scale cannot
be removed using only the uniform coefficient data used in (A2).
That control changes the coefficients and is expressly **not** a lower
bound on the frozen actual moment. No actual obstruction to (C215) is
proved.

The positive missing arithmetic input is the bound

\[
 \sum_{\ell\in4\mathbb Z}(1+|\ell|)^{-8}
       \int\rho_{T,N}(R)|G_\ell(R)|^{10}dR
       \ll_\epsilon T^{83/65+\epsilon}N^{-1/2}.              \tag{A3}
\]

This is a complete sufficient input, not a theorem established here and
not claimed equivalent to (C215). Already its `ell=0` summand contains
the original difficult actual complex radial block. A theorem only for
the nonzero angular modes does not close (A3). No transformed remainder
or coefficient cancellation is silently credited.

## 2. Exact statement and hypotheses

Write `e(t)=exp(2 pi i t)`. Let `T>=2` be real and

\[
 T^{166/325}<N<T^{242/325},\qquad
 a=1/\sqrt2,\quad d=\sqrt3-a,\quad
 J=\lceil dT/\sqrt N\rceil,\quad R_j=aT+j\sqrt N.
\]

Use the fixed nonnegative nonzero smooth mask `v`, supported in `[1,4]`,
and the exact fixed radial mollifier transform `Psi`, with `Psi(0)=1`.
All definitions are those of the frozen strategy:

\[
 b_n=n^{-3/4}\Psi(\sqrt{n/T})v(n/N),\quad
 c_m=b_{|m|^2},\quad
 F_N(x,R)=\sum_{m\ne0}c_m e(x\cdot m+R|m|).
                                                               \tag{A4}
\]

The sums are finite because of `v`; no infinite radial tail is hidden
inside a block. The surrounding full-circle problem still has all dyadic
scales and its accepted Schwartz remainder. Let `phi` and `eta` be the
frozen real Schwartz cutoffs of small compact Fourier support. Their
fixed initial dilation makes their moduli bounded below on
`[-1,1]^2` and `[-1,1]`, respectively, as clarified by the conductor.
Let `W(y)=C_A(1+|y|^2)^(-100)` and define

\[
 f_j(y,u)=\phi(y/N)\eta(u/N)
       F_N(y/\sqrt N,R_j+u/\sqrt N),\qquad
 C(T,N)=\sum_{j=0}^J\int W(y)|f_j(y,u)|^{10}\,dy\,du.
\]

Set `K=[R_0,R_J]`, which contains the entire required comparison interval
`I=[T/sqrt2,sqrt3 T]`, and put

\[
 Q(R)=\sum_{j=0}^J
         |\eta((R-R_j)/\sqrt N)|^{10},\qquad
 \rho_{T,N}(R)=\left(1+\frac{\operatorname{dist}(R,K)}{\sqrt N}\right)^{-2}.
                                                               \tag{A5}
\]

For each integer `ell`, use the exact finite sums

\[
 A_\ell(n)=\sum_{m\in\mathbb Z^2:\,|m|^2=n}
                    \exp(-i\ell\arg m),\qquad
 G_\ell(R)=\sum_{n\ge1}b_n A_\ell(n)e(R\sqrt n).
                                                               \tag{A6}
\]

The argument is well-defined modulo `2 pi` for integer `ell`. Rotation
of the whole integer lattice by `pi/2` proves
`A_ell=0` unless `4` divides `ell`. Reflection gives
`A_-ell=A_ell` real, although the proof only needs

\[
 A_0(n)=r_2(n),\qquad |A_\ell(n)|\le r_2(n).                 \tag{A7}
\]

Every signed representation is included. No angular equidistribution,
automorphic estimate, independent random phase, or cap occupancy
assumption is made.

Constants in (A1)--(A2) depend only on the fixed cutoffs and, where
indicated, epsilon. The coefficient-normalization control below is stated
in a larger family and explicitly does not alter (A4) in the positive
claims.

## 3. Proof and complete cost derivation

### 3.1 Actual coefficient masses and exact window recombination

Throughout the frozen band, `N/T<=T^(-83/325)`. Continuity and
`Psi(0)=1` therefore give `Psi(|m|/sqrt T)>1/2` on the support for all
sufficiently large `T`. The constants absorb the bounded remainder of
the parameter range. Since `v` is positive on some fixed interior
subinterval, the elementary lattice-annulus count gives

\[
 \sum_m c_m\asymp N^{1/4},\quad
 \sum_m c_m^2\asymp N^{-1/2},\quad
 \sum_m |c_m|^p\asymp_p N^{1-3p/4}\quad(p>0),              \tag{A8}
\]

for sufficiently large `T`. Upper bounds hold without the positivity
restriction. Indeed the number of lattice points in a fixed dilated
annulus is `asymp N`; covering its boundary with unit squares gives an
`O(sqrt N)` error in the area count. All radii in the annulus are
comparable to `sqrt N`. The grouped norm needed later obeys

\[
 \sum_n |b_nA_\ell(n)|^2
 \le\sum_{N\le n\le4N}r_2(n)^2|b_n|^2
 \ll_\epsilon N^{-1/2+\epsilon},                         \tag{A9}
\]

uniformly in `ell`, by `r2(n)<=4d(n)` and the elementary divisor bound.
This is a grouped coefficient norm, distinct from the lattice norm in
(A8). Also `sum_n |b_n A_ell(n)|<<N^(1/4)`, uniformly in `ell`, by the
actual ungrouped mass upper bound.

The substitution `u=sqrt N(R-R_j)` is exact, with
`du=sqrt N dR` and `u/N=(R-R_j)/sqrt N`. Tonelli gives

\[
 C(T,N)=\sqrt N\int_{\mathbb R}Q(R)
          \int_{\mathbb R^2}W(y)|\phi(y/N)|^{10}
                    |F_N(y/\sqrt N,R)|^{10}\,dy\,dR.       \tag{A10}
\]

This uses the original same `F_N` at every center. In particular the
modulations remain exactly `c_m e(R_j|m|)` before the substitution;
they have not been chosen separately. Since the centers are one unit
apart after scaling by `sqrt N`, summing the Schwartz bound
`|eta(t)|^10<<_L(1+|t|)^(-L)` shows

\[
 Q(R)\ll \rho_{T,N}(R)\quad(R\in\mathbb R),\qquad
 Q(R)\gg1\quad(R\in K).                                  \tag{A11}
\]

For the first statement use `L>=3` and the convergent discrete tail;
for the second take a nearest center at distance at most `sqrt N/2`.
The ceiling and both real endpoint windows remain present. Replacing
`|phi(y/N)|` by its fixed supremum is an upper bound on its entire
Schwartz tail, not a truncation.

### 3.2 Exact angular Fourier expansion

Define the elementary angular Fourier coefficient

\[
 h_\ell(t)=\frac1{2\pi}\int_0^{2\pi}
              e(t\cos\alpha)\exp(-i\ell\alpha)\,d\alpha.
                                                               \tag{A12}
\]

This definition fixes every `2 pi` factor and needs no Bessel identity
from an external source. For `y=r(cos theta,sin theta)`, Fourier
expansion of the smooth periodic function in (A12), followed by the
finite lattice summation, gives exactly

\[
 F_N(y/\sqrt N,R)=
   \sum_{\ell\in4\mathbb Z}\exp(i\ell\theta)
   \sum_n b_n A_\ell(n)
          h_\ell(r\sqrt{n/N})e(R\sqrt n).                   \tag{A13}
\]

At `r=0` only `ell=0` survives and `h_0(0)=1`, so this recovers
`F_N(0,R)=G_0(R)` and the exact `r2` lift. Away from zero (A13) retains
all angular harmonics, not just the circular average.

Choose a fixed smooth function `chi` supported in `(1/2,3)` and equal
to one on `[1,2]`. For `r>=0` set

\[
 a_{\ell,r}(\lambda)=\chi(\lambda)h_\ell(r\lambda),\qquad
 k_{\ell,r}(s)=\int_{\mathbb R}a_{\ell,r}(\lambda)e(s\lambda)d\lambda.
\]

Fourier inversion uses `a(lambda)=int k(s)e(-s lambda)ds`, so the
inner sum in (A13) is precisely

\[
 \int_{\mathbb R}k_{\ell,r}(s)
                   G_\ell(R-s/\sqrt N)\,ds.               \tag{A14}
\]

There is no missing `sqrt N` in (A14): `s` is the dimensionless Fourier
dual of `lambda=sqrt(n/N)`. Written in the physical time difference
variable, the convolution kernel would be `sqrt N k(sqrt N t)`.

Eight integrations by parts in `alpha` in (A12), with the trivial
bound used for `ell=0`, and up to three derivatives in `lambda` give

\[
 \max_{0\le q\le3}\|\partial_\lambda^q a_{\ell,r}\|_\infty
       \ll (1+|\ell|)^{-8}(1+r)^{11}.
\]

For example the `q` derivatives introduce at most `r^q`; each of the
eight angular derivatives costs at most another fixed factor `1+r`.
All frequency supports are fixed. Three integrations by parts in the
frequency transform, together with its trivial bound at `s=0`, yield

\[
 |k_{\ell,r}(s)|\ll
 (1+|\ell|)^{-8}(1+r)^{11}(1+|s|)^{-3}.                    \tag{A15}
\]

### 3.3 Weighted radius translation and the full spatial tail

Distance to `K` is one-Lipschitz. Consequently

\[
 \rho(Z+t)\le\rho(Z)(1+|t|/\sqrt N)^2,
\]

where `rho=rho_(T,N)`. Weighted Minkowski applied to (A14) gives

\[
 \left\|\int k_{\ell,r}(s)G_\ell(\,\cdot-s/\sqrt N)ds
            \right\|_{L^{10}(\rho)}
 \le\int |k_{\ell,r}(s)|(1+|s|/N)^{1/5}ds
                      \|G_\ell\|_{L^{10}(\rho)}
 \ll (1+|\ell|)^{-8}(1+r)^{11}
                      \|G_\ell\|_{L^{10}(\rho)}.           \tag{A16}
\]

The integral converges because `3-1/5>1`; the factor is uniform for
`N>=1`. Every radius translation and the entire `s` tail is included.
Now combine (A10)--(A16), Minkowski for the angular series and the
spatial norm, and

\[
 \int_{\mathbb R^2}W(y)(1+|y|)^{110}dy<\infty.
\]

The last integrand has radial tail of order `r^(-89) dr` or smaller.
Thus

\[
 C(T,N)^{1/10}\ll N^{1/20}
       \sum_{\ell\in4\mathbb Z}(1+|\ell|)^{-8}
                         \|G_\ell\|_{L^{10}(\rho)}.
\]

Finally weighted Holder, with the finite sum
`sum_ell(1+|ell|)^(-8)`, proves (A1). The argument uses all radii
`r>=0` and all angular modes. It does not replace a slowly decaying
spatial tail by a logarithmic truncation or an unestimated remainder.

### 3.4 Reproduced finite-block duality bound and its exact range

The accepted Round-204 **statement** is not a theorem for arbitrary
angular modes. The following uses and reproduces its finite coefficient
argument, whose unweighted correlation input is separately explicit in
that accepted proof.

Let `H>=T`, let `L` be a dyadic ambient length comparable to `N`, and
let `S(R)=sum_(L<n<=2L) d_n e(R sqrt n)`, with zeros at any inactive
integers. Suppose

\[
 \sum|d_n|^2\le A L^{-1/2},\qquad
 |K_L(t)|\le A\sqrt L(|t|^\kappa+|t|^{-1}),\qquad
 \kappa=13/55,                                             \tag{A17}
\]

for `0<|t|<=C H`, where `K_L(t)=sum_(L<n<=2L)e(t sqrt n)` and
`A>=1`. The accepted kernel proves its correlation estimate for
`L<=H^(3/2)` and arbitrary real `t` in this range. Here `L~N<T`
makes that hypothesis valid, after fixed constants and bounded
parameters are absorbed. It invokes only the already accepted
Bourgain exponent-pair interface, not a new weighted exponential-sum
theorem. Negative differences are handled by conjugation.

On an interval of length at most `C H`, localize further to intervals
of length at most
`h=(v^2/(C_0 A^2))^(1/kappa)`. In each, choose a maximal
`delta=L^(-1/2)` separated subset of `{|S|>v}`, of cardinality `M`.
The coefficient Cauchy inequality and the exact Gram expansion give,
after dividing by `M` when `M>0`,

\[
 Mv^2\le C A\sqrt L+C A^2 M h^\kappa
                  +C A^2\sqrt L\log(2+H\sqrt L).          \tag{A18}
\]

The first term is the full diagonal `K_L(0)`. The final term follows
by ordering the separated points and summing `1/|R_i-R_j|`.
Choose `C_0` large to absorb the middle term. Maximality covers
the local level set by `M` intervals of radius `delta`, so its measure
is `O(A^2 log(2+H sqrt L) v^(-2))`. There are at most
`C(1+H/h)` local intervals, including one when `h>H`. Hence

\[
 |\{|S|>v\}|\ll A^2\log(2+H\sqrt L)
       \{v^{-2}+H A^{2/\kappa}v^{-136/13}\}.              \tag{A19}
\]

This argument is uniform in the location of the interval: its Gram
matrix depends only on radius differences. A common translation of
coefficients, when used to express that fact, is not a choice of
independent phases at different original windows.

The support `[N,4N]` is zero-extended into at most three standard
dyadic intervals. Formula (A9) supplies their energy condition with
`A=H^delta` for a sufficiently small fixed positive `delta`; the
correlation bound admits the same subpower normalization. Since every
power of `A` in (A19) is fixed, choosing `delta` according to the output
epsilon gives

\[
 |\{R\in E:|G_\ell(R)|>v\}|
 \ll_\epsilon H^\epsilon(v^{-2}+Hv^{-136/13})             \tag{A20}
\]

for any interval `E` of length `O(H)`, uniformly in `ell`. Use the
trivial measure bound below `v=1` and the actual norm upper bound
`|G_ell|<<N^(1/4)`. Because `10<136/13`, layer cake yields

\[
 \int_E|G_\ell(R)|^{10}dR
 \ll_\epsilon H^\epsilon(H+N^2).                          \tag{A21}
\]

The `N^2` comes from `int_1^(C N^(1/4)) v^7 dv`, while the
`H v^(-136/13)` term has a convergent tenth-moment integral. This
explicitly checks the complex coefficient extension instead of
misquoting the accepted full cosine-series moment statement.

To restore the entire `rho` tail, cover `dist(R,K)<=T` by a fixed
number of intervals of length `O(T)`. On the successive exterior
dyadic regions of distance `asymp H_k=2^k T`,

\[
 \rho(R)\ll N/H_k^2.
\]

Equation (A21) applies on each of their two intervals with parameter
`H_k`. Therefore the exterior contribution is at most

\[
 \sum_{k\ge0}\frac{N}{H_k^2}H_k^\epsilon(H_k+N^2)
 \ll_\epsilon T^\epsilon(N/T+N^3/T^2)
 \ll_\epsilon T^\epsilon(T+N^2),                           \tag{A22}
\]

initially for `0<epsilon<1`, which suffices after renaming epsilon.
All real, negative, and arbitrarily distant radii in the cutoffs are
paid. Equations (A21)--(A22) prove the first assertion of (A2); (A1)
then proves the second.

### 3.5 Complete power comparison and the scope of the control

The ratios of the two costs in (A2) to the frozen right side are

\[
 T^{-18/65}\sqrt N,\qquad T^{-83/65}N^{5/2}.              \tag{A23}
\]

Throughout the frozen band, `N^2>T^(332/325)>T`, so the second cost
also dominates the first. The first ratio exceeds one above
`N=T^(36/65)`; the second already exceeds
one above `N=T^(166/325)`. For `N=T^(166/325+delta)` the latter ratio
is `T^(5 delta/2)`, a fixed power when `delta>0` is fixed. Thus this
complete bound cannot certify the target throughout its open band.
For parameters approaching the boundary subpolynomially the comparison
is correspondingly only subpolynomial; no uniform fixed gap is asserted.

For a diagnostic control of the **larger coefficient class**, choose
one real `R_*` in the interior of `I` and replace (A4) by
`tilde c_m=c_m e(-R_*|m|)`. This is one global rephasing, not a
separate choice in each window. It preserves every coefficient modulus
and the norms used above. For small fixed `|y|` and
`|R-R_*|<=c/sqrt N`, all phases

\[
 y\cdot m/\sqrt N+(R-R_*)|m|
\]

lie in a fixed small arc. Positivity and (A8) give
`|tilde F_N(y/sqrt N,R)|>>N^(1/4)`. One center has
`|R_*-R_j|<=sqrt N/2`, so its eta cutoff is bounded below on this
radius interval; phi is also bounded below for these bounded `y`.
The interval has `u` length bounded below by a fixed positive constant.
Integrating over it and a fixed spatial disk gives

\[
 \widetilde C(T,N)\gg N^{5/2}.                              \tag{A24}
\]

This checks the complete weighted normalization and explains the
unremovable high-value cost for that coefficient-uniform input. It
**does not** assert (A24) for the actual positive `c_m` in (A4): their
phases at a physical center are prescribed. Even the common rephasing
in this control is forbidden as a substitution into (C215). In
particular neither (A23) nor (A24) is a signed actual lower obstruction.

## 4. First doubtful or unproved step

No unestimated transform error occurs in (A1); its cost is explicit.
The first unproved positive step in this reduction is (A3), or a
different actual bound on (A10) that avoids its triangle inequalities.
The primitive actual information proved here is (A7)--(A9). These
uniform norms only give (A2). To improve the power one must use more
than those norms, such as actual signed relations among the coefficients
or their radius phases. No such relation is estimated here.

The exact spatial angular average in (A13) is the `ell=0` filtered
block. Its multiplier satisfies `h_0(0)=1`, and its coefficients are
exactly `r2`; the fourfold cancellation merely removes modes not
divisible by four. Thus a proposed angular argument that retains only
nonzero modes omits a required component. Calling the nonzero modes
Gaussian Hecke coefficients would not itself supply any moment
estimate, and no such theorem is imported.

Independently of (A1), the frozen fixed-spatial-bandwidth reproducing
inequality gives

\[
 \sqrt N\int_I|G_0(R)|^{10}dR\ll C(T,N).                  \tag{A25}
\]

Indeed apply it to each `f_j(.,u)`, use `phi(0)=1`, the lower bound
for eta on the central windows, their complete coverage of `I`, and
`du=sqrt N dR`. This necessary consequence confirms that the original
radial arithmetic is not bypassed by changing angular notation.
(A3) is stronger because of its extra modes and full polynomial radius
majorant. Neither direction supplies the missing bound.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `exact_r2_lift` | Exact: (A6)--(A7), (A13) at `r=0`, and (A25) keep all representations. |
| `actual_common_modulation` | Exact: (A10) recombines the original common wave. Only the separately labeled enlarged-class control changes coefficients. |
| `weighted_fourier_normalization` | Checked: (A12) fixes `2 pi`; (A14) uses dimensionless `s`; (A16) keeps the translation weight; (A10) restores `sqrt N`. |
| `all_windows_tails` | Complete: all `J+1` windows, the full `Q`, all angular modes, `r>=0`, Fourier-kernel tails, and (A22)'s infinite radius tails are included. |
| `narrow_aligned_directions` | Included in every `A_ell(n)`. No angular density or transversal-only assertion is used. The aligned enlarged-class control is explicitly separate. |
| `complete_coefficient_norms` | (A8) and (A9) distinguish lattice and grouped norms; the latter and the full `ell` weight are both paid. |
| `source_hypotheses` | No new import. The exact finite-block range `L<=H^(3/2)`, difference range, Gram diagonal and localization ceiling of the accepted kernel are reproduced in (A17)--(A21). |
| `all_restored_powers` | All powers appear in (A10), (A15)--(A16), (A21)--(A23); spatial `r^110` is integrable against `W`. |
| `actual_arbitrary_distinction` | (A1)--(A2) apply to actual coefficients. (A24) changes them and only controls the larger norm-based method. |
| `certificate_signed_distinction` | The cost comparison in (A23) is not a lower bound on `C`; no actual signed lower obstruction is claimed. |
| `real_endpoints` | `T,N,R_j` remain real; `J` keeps its ceiling; zero-extension covers noninteger norm endpoints; all of `I` is included. |
| `full_quarter_scope` | No moment/exponent improvement. Even (C215), if proved, is the `102/325` milestone only; the full sufficient moment family remains necessary for that route. |
| `statement_only_control` | This report is nonblind. Its elementary kernels are suitable for independent review, but it supplies no verdict for the isolated task and reads none of its files. |

All controls are analytic. There was no numerical or symbolic experiment.
The independent conductor suggestion to inspect angular symmetry was
received during the task; the derivation and weighted cost proof above
are provided in full and do not claim statement-only independence.

## 6. Dependencies and exact artifacts used

Only the assigned brief and its permitted internal context were read:

1. `protocol.md` and
   `rounds/codex-managed/gc-complete-localized-wave-moment/briefs/actual_lattice_envelopes.md`.
2. `state/proof_obligations.yml`, frozen hash in the header; relevant
   target, M1/M2, endpoint, GAR, qualified Li--Yang, and accepted
   square-root moment statements were extracted from the large graph.
3. `state/active_campaign.yml`, inspected hash
   `5f12ab05333d3814468b66fa0597e1276ecbb61fc7f0f3deb463928644c46cca`.
4. `strategy/round215_complete_localized_wave_attack.md`, hash
   `7b447077f999d022c4e9073cf2aa166c86c87f570cfc378f8826895da3ed6cf9`.
5. `strategy/gauss_circle_strategy_checkpoint_round214_2026-09-28.md`, hash
   `e8ad087a36bcb9bf098056a0498242b7b5882ac34dc071b0b5007f7818647877`.
6. `rounds/codex-managed/gc-full-goal-radius-source-review/reports/full_goal_harmonic_sources.md`,
   hash `50228227fa0f77a6ce944ea8e2fbfd8f1fe75ddad60662bf041a487dcb0cf4b3`.
7. `rounds/codex-managed/gc-full-goal-radius-source-review/reviews/independent_harmonic_sources_review.md`,
   hash `959b82e190b0e8528284c3c15460147468ef1d41079e6eb72f7faa31774ca2c2`.
8. `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`,
   hash `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.

The accepted kernel's correlation lemma and finite duality proof are used
as specified in Section 3.4. Its external source dependency is inherited;
no new source card or theorem extension is claimed. The angular Fourier
and multiplier estimates are proved directly. The prior harmonic report
and its independent seam supply only the frozen trace/whole-goal context.
No path appearing solely as their historical provenance was opened.

Conductor messages supplied the already intended fixed central cutoff
cubes and suggested the fourfold symmetry check. No sibling derivation,
blind packet, shared synthesis, validation matrix, or successor artifact
was consulted or edited.

## 7. Recommended state effect

**Retain** (A1) as a complete candidate actual-coefficient interface,
subject to independent multiplier, tail and arithmetic-scope review.
**Retain** (A2) as a valid but insufficient bound, with the finite-block
extension proved here rather than attributed to a stronger printed
accepted theorem. **Retain** (A24) only as an enlarged-class control.

**No change** to the accepted graph, proof draft, exponents, M1/M2,
GAR or endpoint obligations. The frozen estimate (C215) and the
complete sufficient arithmetic input (A3) remain open. A future proof
of this fixed tenth gate would still not prove quarter: that route
needs a sufficient complete family with physical moment exponent
`E(p)=1+o(p)` along unbounded fixed `p`, every effective scale and the
paid full-series tails. The independent M1 HARD/SMOOTH and M2
TOP/BAL/UNBAL parents, and GAR's total-M1-only scope, are not altered.

This bounded task stops after its assigned report and does not select
or begin a successor round.
