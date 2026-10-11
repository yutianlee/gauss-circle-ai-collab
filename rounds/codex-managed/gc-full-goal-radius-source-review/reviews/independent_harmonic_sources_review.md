# Round 214 independent harmonic-source seam

Campaign: `gc-full-goal-radius-source-review`.
Role: independent source/normalization reviewer, NONBLIND.
Reviewer task: `signed_radius_sources`, reassigned after its original
report was frozen. Date: 2026-09-28 local time.
Allocation: entirely analytical/source review; zero experiments.

Reviewed artifact:
`rounds/codex-managed/gc-full-goal-radius-source-review/reports/full_goal_harmonic_sources.md`.
Verified final SHA-256:
`50228227fa0f77a6ce944ea8e2fbfd8f1fe75ddad60662bf041a487dcb0cf4b3`.
All verdicts below bind that exact hash. This review changes no report.

## 1. Result

**GREEN for the assigned seam. No required mathematical correction.**

The exact lattice lift, legitimate cone parameters, bounded cap
occupancy, localization and all reconstruction powers reproduce
(214.H1). Its comparison with the tenth gate is quantitatively
insufficient as stated. The Guth--Maynard import correctly stops at
its logarithmic frequency hypothesis. The complete-moment normalization
in (H14), the threshold computation in (H15), and the sufficient
weighted-tube implication (H17)--(H19) check.

The verdict accepts the source applications and conditional strategy
statements as reviewed evidence. It does not prove (H3), (H15), (H18),
the proposed high-moment family, a new circle exponent or an M1/M2 parent.
The new weighted gate is explicitly unproved in the artifact, which is
essential to this verdict.

## 2. Exact scope and hypotheses reviewed

Use the report's fixed real even Schwartz `Psi`, its smooth dyadic mask
`v` supported on `[1,4]`, real `T>=2`, physical block `1<=N<=T`, full
positive radius window of length `asymp T`, and every finite fixed
`p>=2`. Define `S_N`, `H_N`, `F_N`, `c_m` exactly as (H2)/(H6).

The main source is Guth--Maldague,
[arXiv:2206.01093v2](https://arxiv.org/html/2206.01093v2), 13 August 2022,
Theorem 3, together with the preceding definitions of the truncated
cone and its small caps. The displayed three powers and the legal
parameter rectangle match (H4). In particular the choice
`beta_1=beta_2=1/2` lies inside that rectangle.

The second source is Guth--Maynard,
[arXiv:2405.20552v2](https://arxiv.org/html/2405.20552v2), Theorem 1.1.
Its coefficients have modulus at most one and its sample points are
one-separated in a time interval of length `mathcal T`; its polynomial
uses `n^(it)`. The statement and all three large-value terms agree with
(H5). No new theorem or source family was added to the review.

Moment reconstruction uses the accepted Round-204 kernel at
`proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`,
specifically its complete series, real window, pointwise normalization,
distribution bound and sharp smoothing formula. Its inspected SHA-256 is
`942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.

## 3. Independent derivation and seam checks

### 3.1 Arithmetic lift, cone support and cap norms

At `x=0`, grouping lattice vectors by `n=|m|^2` gives

\[
\sum_m |m|^{-3/2}\Psi(|m|/\sqrt T)v(|m|^2/N)e(R|m|)
 =\sum_n r_2(n)n^{-3/4}\Psi(\sqrt{n/T})v(n/N)e(R\sqrt n).
\]

Thus every ordered signed representation contributes exactly once.
The annulus contains `O(N)` lattice vectors and each coefficient has
size `O(N^(-3/4))`; rational directions and repeated norms are not
deleted. The multiplicity is restored automatically at the spatial line.

For a radius window of length `sqrt N`, rescale
`y=sqrt N x`, `u=sqrt N(R-R_j)`. Take a Schwartz function
`eta(y/N,u/N)` with Fourier support in a sufficiently small ball of
radius `O(N^(-1))` and modulus bounded below on the required central
cube. Such a function exists by taking the inverse Fourier transform
of a small smooth bump, positive at the origin, and shrinking its
Fourier support by a fixed factor. Its rescaling constants are fixed.
Multiplying the finite wave by it produces a Schwartz function.

The centers `(m/sqrt N,|m|/sqrt N)` lie exactly on the cone with radial
coordinate in `[1,2]`. A fixed dilation sends that interval to `[1/2,1]`;
the thickening remains `O(N^(-1))`. Bounded partitions or harmless fixed
enlargements at the radial ends only change constants.

With both tangential cap lengths `N^(-1/2)`, the projection of a cap
onto the first two frequency coordinates has diameter `O(N^(-1/2))`.
After multiplication by `sqrt N`, it meets a bounded-radius disk in
the integer lattice, hence contains `O(1)` lattice centers uniformly.
The frequency balls from the physical cutoff have smaller radius
`O(N^(-1))`, so they do not alter that count. No angular equidistribution
claim is used.

For clarity about the projection convention, smooth cutoffs adapted
to the affine cap frames have uniformly bounded convolution `L1` norms:
linear dilation preserves the `L1` norm of their inverse Fourier
transforms. Bounded-overlap neighboring caps cost only a fixed factor.
The standard smooth support formulation of the small-cap inequality
therefore has the same powers as the source's projection notation.
One must not assign an `L1` kernel bound to a sharp characteristic
projection; the report explicitly chooses smooth cutoffs instead.
For finite `p>1`, the corresponding rectangular sharp projection can
also be handled by its scale-invariant `Lp` multiplier bound, without
changing any displayed power. This convention causes no hidden power
loss in the application.

There are `O(N)` active caps. Each contains `O(1)` cutoff plane waves,
whose `p`th norm is `O_p(N^(-3p/4)N^3)`. Hence

\[
\sum_\gamma\|f_\gamma\|_p^p\ll_p N^{4-3p/4},
\]

reproducing (H9).

### 3.2 Trace, cells, Jacobian and all windows

The spatial torus reproducing kernel has bounded `L1` norm and size
`O(N)`. Weighted Holder gives the trace factor in (H7).

On the central cutoff region the original `x` variables occupy a square
of side `asymp sqrt N`, containing `asymp N` full torus cells. The
change `(x,R)->(y,u)` has determinant `N^(3/2)`. Thus

\[
\|f\|_p^p\gg N^{5/2}
 \int_J\int_{[0,1]^2}|F_N(x,R)|^p\,dx\,dR.
\]

Combining with the trace factor `N` gives
`integral_J |S_N|^p << N^(-3/2)||f||_p^p`, exactly (H10).
This directly checks the sometimes-confused cancellation between the
number of torus cells and the trace factor.

Theorem 3 at the chosen cap parameters gives the two distinct powers
`N^(p/2-1)` and `N^(p-3)`. Combining them with (H9) and (H10) yields

\[
\int_J|S_N|^p\ll N^\epsilon
  (N^{3/2-p/4}+N^{p/4-1/2}).
\]

There are `O(T/sqrt N)` windows, including partial end windows. Since
`N<=T` and bounded parameters are absorbed into constants, no missing
additive one changes this count. The result is

\[
\int_I|H_N|^p\ll T^\epsilon
  (TN^{1-p/4}+TN^{p/4-1}),
\]

which is (H1). At `p=10`, dividing `TN^(3/2)` by
`T^(83/65)N^(-1/2)` gives `T^(-18/65)N^2`; its lower-band limiting
power is `242/325`. The claimed failure throughout the open band checks.
The aligned coefficient example has peak `N^(1/4)` for radius length
`asymp N^(-1/2)`, so its local `p`th moment is
`asymp N^(p/4-1/2)`. It is correctly labeled as an enlarged-coefficient
control rather than an actual `r2` counterexample.

### 3.3 The frequency mismatch remains exact

Rescaling the actual divisor-size coefficients to modulus at most one
is permitted, but it does not change their frequencies. The strict
convexity of `exp(t/2)` shows that three distinct points of
`(log n,sqrt n)` are not collinear. Thus an exact common
reparameterization and fixed coefficient phases cannot turn the full
square-root family into the logarithmic family.

Expanding at `N` gives

\[
\sqrt{N+j}-\sqrt N-\frac{\sqrt N}{2}\log(1+j/N)
 =\frac{j^2}{8N^{3/2}}+O(j^3/N^{5/2}).
\]

The reported `T J^2/N^(3/2)` phase cost follows. Subintervals with
zero extension retain ambient logarithmic length `N`; replacing it
by `J` is not justified. The review assigns no numerical large-value
consequence to this failed dictionary.

### 3.4 Moment normalization and the twelfth gate

The accepted sharp relation is
`P(R^2)=(sqrt R/pi)B_T(R)+O(T^(1/2+epsilon))`. A complete radius
moment `T^(E(p)+epsilon)` therefore gives a sharp moment with the larger
of the powers `T^(1+p/2+E(p))` and `T^(2+p/2)`. Passing to `Y=T^2`
and applying persistence divides its exponent by `p+1`. This is
precisely (H14).

For the low part of the twelfth moment, put `V0=T^(13/125)`. Layer cake
and `D_T(V)<<T^epsilon(V^(-2)+TV^(-136/13))` give, besides `O(T)`,

\[
V_0^{10}=T^{26/25},\qquad
T V_0^{12-136/13}=T^{29/25}.
\]

Thus (H15) would give the complete moment `T^(29/25+epsilon)`.
Multiplication by `T^7` for the amplitude and Jacobian yields
`T^(204/25)=Y^(102/25)`; persistence gives `102/325`. The existing
moment term is `T^(10 beta)`, so the stated missing saving is exactly
`10 beta-29/25`. The hierarchy condition `E(p)=1+o(p)` along unbounded
fixed `p` is sufficient for quarter through (H14), with constants allowed
to depend on `p`. No growing moment order in `T` is needed.

### 3.5 The new weighted-tube gate is sufficient and explicitly open

For each fixed `u`, the spatial Fourier support of `f_j` stays in a
fixed disk. Let `k` be a fixed Schwartz reproducing kernel for this
disk. Holder gives

\[
|f_j(0,u)|^p
 \le \|k\|_1^{p-1}\int |k(y)|\,|f_j(-y,u)|^p\,dy
 \ll_p\int W(y)|f_j(y,u)|^p\,dy,
\]

after choosing the fixed polynomially decaying `W` to dominate the
kernel. This proves (H17). The cutoff at `y=0` is bounded below on the
assigned central interval, and `dR=N^(-1/2)du`. Summing every window
therefore proves that (H18) implies (H3) with the exact factor
`N^(-1/2)`. The full weighted integrals include all cutoff tails, which
makes the asserted sufficient hypothesis stronger; no tail is discarded.

Tonelli applied to the nonnegative weighted measure proves the layer
cake identity (H19). It does not estimate that integral. The report
correctly leaves the actual weighted envelope bound unproved and does
not convert the source's unweighted superlevel estimate into a weighted
one for free.

The stated full-goal family includes every effective dyadic scale,
with the accepted Schwartz tail paid. Its factor `sqrt N` cancels
`dR=N^(-1/2)du`; finitely many `O(log T)` blocks cost only `T^epsilon`
at each fixed `p`. This reproduces its conditional implication to
`E(p)=1+o(p)`.

## 4. First doubtful or unproved step

There is no unresolved step in the assigned normalization/source seam
requiring revision of the frozen artifact. The first positive arithmetic
claim still missing is (H18), or the alternative complete high-value
gate (H15), or directly (H3). Proving their stronger full-goal family is
also open. The generic cone theorem and its projections do not supply
the actual envelope information near the spatial line.

The source-frequency failure for Guth--Maynard is a scope failure, not
a theorem that no adaptation can work. The radius certificate limit is
a limit of the specified restored envelope, not a lower bound for the
signed arithmetic energy. These distinctions are maintained.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Exact `r2` lift and multiplicity | GREEN; grouping all lattice vectors recovers (H2) identically. |
| Cone support and source parameters | GREEN; fixed radial dilation, `O(N^(-1))` thickening, lawful half/half caps. |
| Cap occupancy and projection norms | GREEN; spatial lattice spacing gives `O(1)` centers and adapted smooth kernels have uniform `L1` norms. |
| Trace, Jacobian, cells and windows | GREEN; factors are respectively `N`, `N^(3/2)`, `N`, and `T/sqrt N`, producing exactly (H1). |
| Aligned local control | GREEN; sharpness control is kept separate from physical coefficients. |
| Guth--Maynard frequency class | GREEN scoped failure; no logarithmic theorem is credited to square-root phases. |
| H14 and H15 powers | GREEN; both independently recomputed from the accepted kernel. |
| H17--H19 scope | GREEN conditional implication; actual weighted-tube estimate remains explicitly open. |
| Real windows, partial endpoints, tails | GREEN; no omitted radius window or unpaid tail is used in the sufficient implications. |
| Full parents and quarter scope | GREEN; all M1 HARD small `t`, independent M1 SMOOTH, M2 TOP/BAL/UNBAL, endpoints, and GAR's total-M1 limitation are retained. |

No experiment was run. The low-order control `p=4` in (H1) gives
`O(T^(1+epsilon))`, agreeing with the report. Fixed local aligned peaks
reproduce its expensive term without saying anything about a false
arithmetic lower bound.

## 6. Dependencies and exact artifacts used

This reassigned NONBLIND review used only:

1. `protocol.md`.
2. The frozen harmonic report at the hash in the header.
3. The accepted Round-204 kernel at the hash in Section 2.
4. The two exact versioned primary theorem texts linked in Section 2.
5. Already-read permitted Round-214 strategy/graph context for the
   unchanged frontier and the scope of candidate evidence.

The new reassignment explicitly authorized reading the harmonic report;
it does not retroactively change the isolation status of this agent's
earlier source report. That original report remains unchanged. No blind
packet/report, conductor calculation, shared synthesis, validation matrix
or successor artifact was opened or edited. The broader metadata corpus
was not independently re-audited in this bounded seam; its source-status
screens remain the author's documented checks rather than new imports.

## 7. Recommended state effect

**GREEN: retain the harmonic report at its reviewed final hash as
independently checked method/strategy evidence.** No required correction.
Retain (H1) as a valid but insufficient source consequence; retain
(H17)--(H19) only as a complete conditional gate with its estimate open.

**No change** to accepted exponents, proof parents or the proof draft.
This review writes only its assigned review file and stops. It does not
design a successor round or authorize promotion of an unproved input.
