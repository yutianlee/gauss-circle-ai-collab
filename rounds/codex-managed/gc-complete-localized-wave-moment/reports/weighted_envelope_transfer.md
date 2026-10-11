# Round 215: legal weighted amplitude-envelope transfer

Campaign: `gc-complete-localized-wave-moment`.
Task: `weighted_envelope_transfer`; role: discovery, selected-context NONBLIND.
Date: 2026-09-28, Asia/Shanghai.
Frozen graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Status: candidate evidence only. Allocation: 100% analysis/source audit;
zero numerical experiments. Only this assigned report is written.

## 1. Result: a complete transfer, with its estimate still open

The amplitude-dependent theorem has a legal application which retains the
spatial weight through a convergent family of bandlimited spatial
localizers. Its exact consequence is the certificate (E215.7) below,
including every amplitude threshold, cap, envelope, radius window and
Schwartz tail. The localization changes the permissible cone parameter
from `N` to `min(N,r)`, where `r` is the spatial localization radius.
The fixed-width part of the weight therefore uses a bounded cone
parameter. The source theorem does not itself estimate the resulting
actual certificate at the required power.

The complete upper bound proved here is

\[
 \mathcal C(T,N)\lesssim_\epsilon T N^{2+\epsilon}.       \tag{E215.1}
\]

The same bound holds for the particular positive source certificate
constructed below. This is insufficient throughout the frozen band;
its power deficit is `T^(-18/65)N^2`, at least the limiting power
`T^(242/325)`. This derivation uses weighted second moments and the
complete coefficient amplitude, not the previously priced Theorem 3.

The result is a scoped source/transfer limitation, not a no-go theorem
for all weighted wave-envelope arguments or for the actual moment.
The quantitative first open step is (E215.8). No envelope can be
discarded merely because its direction is rational or aligned.

## 2. Exact statement, frozen hypotheses and source interface

Use `e(t)=exp(2 pi i t)` and the definitions of strategy215 literally:
real `T>=2`, `T^(166/325)<N<T^(242/325)`,
`a=1/sqrt(2)`, `d=sqrt(3)-a`, `J=ceil(dT/sqrt(N))`,
`R_j=aT+j sqrt(N)` for every `0<=j<=J`, and

\[
 c_m=|m|^{-3/2}\Psi(|m|/\sqrt T)v(|m|^2/N),\quad
 F_N(x,R)=\sum_{m\ne0}c_m e(x\cdot m+R|m|),
\]
\[
 f_j(y,u)=\phi(y/N)\eta(u/N)
 F_N(y/\sqrt N,R_j+u/\sqrt N),\qquad
 W(y)=C_A(1+|y|^2)^{-100}.
\]

Here `v` is the nonnegative, nonzero fixed smooth mask supported in
`[1,4]`; `Psi` is the fixed real radial mollifier transform with
`Psi(0)=1`. The fixed real Schwartz cutoffs have small compact Fourier
support and are bounded below on the requisite central cubes. The
conductor clarified that these include `[-1,1]^2` for `phi` and
`[-1,1]` for `eta`, using the permitted fixed dilation before freezing.
No cutoff is subsequently adjusted with the window index.

The sole external source interface audited is Guth--Maldague,
[*Amplitude dependent wave envelope estimates for the cone in R^3*,
arXiv:2206.01093v2](https://arxiv.org/html/2206.01093v2),
Theorem 2, equation (2), and Section 5, equations (29)--(30), with the
envelope weight specified there by reference to equation (13).
The theorem's mathematical data, written in the notation used here, are

\[
 \alpha^4|\{|h|>\alpha\}|
 \le K_\sigma S^\sigma\sum_s\sum_{\tau\in\mathbf S_s}
       \sum_{U\parallel U_{\tau,S}}
 |U|A_U^2\,
 \mathbf1_{\{\alpha^2\le K_\sigma S^\sigma n_h(s)^2A_U\}},
                                                        \tag{E215.2}
\]
\[
 A_U=|U|^{-1}\int\sum_{\theta\subset\tau}|h_\theta(z)|^2W_U(z)\,dz,
 \qquad n_h(s)=\#\{\tau\in\mathbf S_s:h_\tau\not\equiv0\}.
\]

The hypothesis is that `h` is Schwartz and its Fourier support lies in
the `S^(-1)` neighborhood of the truncated cone. Canonical `theta` have
dimensions `1 x S^(-1/2) x S^(-1)`; dyadic `s` runs from the canonical
scale to a fixed top scale. Fixed endpoint enlargements have no power
cost. The projections are the source's exact frequency restrictions.
For direction `omega`, put

\[
 \mathbf c=(\cos\omega,\sin\omega,1),\quad
 \mathbf n=(\cos\omega,\sin\omega,-1),\quad
 \mathbf t=(-\sin\omega,\cos\omega,0).
\]
\[
 U_{\tau,S}=\{z:|\mathbf c\cdot z|\le Ss^2,
                    |\mathbf n\cdot z|\le S,
                    |\mathbf t\cdot z|\le Ss\},
 \qquad |U_{\tau,S}|\asymp S^3s^3.                 \tag{E215.3}
\]

`W_U` is an L-infinity normalized polynomial weight in this affine
frame, with exponent 100 in each normalized coordinate, translated to
the center of `U`; Section 5 specifies the three-dimensional analogue
of (13). Its fixed normalization is harmless. In particular
`integral W_U asymp |U|` and `sum_(U parallel U_tau,S) W_U lesssim 1`.
It is not the frozen spatial weight `W(y)`.

No theorem for the measure `W(y)dydu`, no weighting of the right side
by `average_U W`, and no unrestricted deletion of low-density envelopes
is stated in the source. The theorem and definitions have been checked;
the external proof is not being independently reproved.

## 3. Derivation and all restored powers

### 3.1 Exact coefficients and a legal representation of the weight

Grouping every lattice vector by its norm gives exactly

\[
 F_N(0,R)=\sum_{n\ge1}r_2(n)n^{-3/4}
                \Psi(\sqrt{n/T})v(n/N)e(R\sqrt n).
\]

There are `O(N)` vectors and

\[
 \sum_m|c_m|\lesssim N^{1/4},\qquad
 \sum_m|c_m|^2\lesssim N^{-1/2}.                    \tag{E215.4}
\]

For large `T`, positivity of `Psi` on the shrinking argument range
and a subannulus where `v` is bounded below give the corresponding
lower orders. These lower bounds are used only for the enlarged-family
control below. Bounded parameters are absorbed into constants.

Choose a fixed real Schwartz function `b` on `R^2`, with small compact
Fourier support and `|b|>=c>0` on the unit disk. Let `r_k=r_0 2^k`,
`lambda_k=(1+r_k^2)^(-100)`, `k>=0`; `r_0` is a sufficiently large
fixed constant, allowed to depend on the fixed source parameter `sigma`
but never on `T,N,j,k`. Then, with constants depending only on these choices,

\[
 W(y)\asymp\sum_{k\ge0}\lambda_k|b(y/r_k)|^{10}.       \tag{E215.5}
\]

For the lower inequality choose the first `r_k>=|y|`. For the upper
inequality split the sum at that index, and use Schwartz decay of
`|b|^10` of order greater than 200 on the smaller radii; both geometric
sums are `O((1+|y|)^(-200))`. Thus (E215.5) includes the whole spatial
tail, rather than truncating it.

Put `g_jk(y,u)=b(y/r_k)f_j(y,u)` and `h_jk(z)=g_jk(z/2)`.
The last fixed dilation puts cone radii `[1,2]` into `[1/2,1]`, and
`||h_jk||_10^10=8||g_jk||_10^10`. The frequency thickening is
`O(N^(-1)+r_k^(-1))`. A power-of-four parameter

\[
 S_k\asymp\min(N,r_k)
\]

with a sufficiently small fixed comparison factor therefore satisfies
the source support hypothesis. For `r_k<=N` the width is `O(1/r_k)`
and `S_k asymp r_k`, including the fixed radius `r_0`. For `r_k>N`
the width is `O(1/N)` and `S_k asymp N`, uniformly for the infinitely
many such `k`. Choose `r_0` large enough for the source's lower scale
threshold. The source certificate is asserted for all sufficiently
large `T` (depending on `sigma`), so also `N` exceeds that threshold.
The remaining bounded `T` range is paid separately by constants in
(E215.1) and in the target, not by an unauthorized small-scale theorem.
Each `h_jk` is Schwartz. Its coefficients still contain exactly the
common modulation `c_m e(R_j|m|)`; the localizers do not choose or
replace these phases. Projections include all Fourier blobs and their
overlaps.

Multiplication by a fixed-width spatial cutoff does not preserve cone
thickness `N^(-1)`. The required change to `S_k` is a genuine hypothesis
cost. Direct multiplication by `W^(1/10)` provides no compact thin-cone
support at all. This identifies the defect in the tempting direct
weighted application, without claiming that every other transfer must
suffer the same cost.

### 3.2 The complete threshold-preserving certificate

Let `M=C N^(1/4)` be a common amplitude ceiling for all `h_jk`, using
(E215.4) and the fixed cutoff suprema. For each `j,k,s,tau,U`, define
`A_jk,U` and `n_jk(s)` by the exact source definitions in Section 2.
Layer cake, (E215.2), and Tonelli give

\[
 \begin{aligned}
 \|h_{jk}\|_{10}^{10}
 &=10\int_0^M\alpha^9|\{|h_{jk}|>\alpha\}|\,d\alpha\\
 &\le \tfrac53K_\sigma S_k^\sigma
 \sum_{s,\tau,U}|U|A_{jk,U}^{2}
 \min\{M^6,(K_\sigma S_k^\sigma
                    n_{jk}(s)^2 A_{jk,U})^3\}.
                                                        \tag{E215.6}
 \end{aligned}
\]

Indeed the inner integral is `integral_0^L alpha^5 d alpha=L^6/6`,
where `L=min(M,sqrt(K_sigma S_k^sigma n_jk(s)^2 A_jk,U))`.
There is no replacement of this threshold by a mean energy threshold.
All infinitely many envelope translates remain in the nonnegative sum.

Define the following actual, complete positive certificate:

\[
 \mathfrak E_\sigma(T,N)=
 \sum_{j=0}^J\sum_{k\ge0}\lambda_k S_k^\sigma
 \sum_{s,\tau,U}|U|A_{jk,U}^{2}
 \min\{M^6,(K_\sigma S_k^\sigma
                  n_{jk}(s)^2 A_{jk,U})^3\}.
\]
\[
 \boxed{\quad\mathcal C(T,N)\lesssim_\sigma
                 \mathfrak E_\sigma(T,N).\quad}          \tag{E215.7}
\]

One concrete sufficient estimate for the frozen target is therefore

\[
 \mathfrak E_\sigma(T,N)
       \lesssim_\epsilon T^{83/65+\epsilon},             \tag{E215.8}
\]

with a suitably chosen fixed positive source parameter `sigma` for
each requested epsilon. Equation (E215.8) is open. It is stronger than
the target and is not presented as an equivalent arithmetic statement.
The certificate remains sensitive to the actual intra-cap phases; it
has not replaced them by coefficient norms at this stage.

### 3.3 Complete second moment, including every window and tail

Write `a_n=n^(-3/4)Psi(sqrt(n/T))v(n/N)` and
`B_n(y)=sum_(|m|^2=n)e(y.m/sqrt(N))`. For the Fourier convention
`hat q(t)=integral q(u)e(-ut)du`, integration of the `u` factor in the
second moment gives exactly

\[
 \int |\eta(u/N)|^2
 e(u(\sqrt n-\sqrt{n'})/\sqrt N)\,du
 =N\widehat{|\eta|^2}
       (\sqrt N(\sqrt{n'}-\sqrt n)).                    \tag{E215.9}
\]

The Fourier transform on the right has fixed compact support, say in
`[-L_eta,L_eta]`. Since `n,n'` belong to `[N,4N]`, nonzero terms satisfy
`|n-n'|<=4L_eta`. This is a bounded number of adjacent norm indices;
it is not necessary to assume exact diagonality or enlarge the cutoffs.
Keep the exact factor `e(R_j(sqrt n-sqrt n'))` until making the explicit
upper bound by its modulus. From `|B_n(y)|<=r_2(n)`, bounded degree,
`2ab<=a^2+b^2`, and the elementary divisor bound,

\[
 \int_{\mathbb R}|\eta(u/N)F_N(y/\sqrt N,
                         R_j+u/\sqrt N)|^2du
 \lesssim N\sum_{N\le n\le4N}|a_n|^2r_2(n)^2
 \lesssim_\epsilon N^{1/2+\epsilon}.                 \tag{E215.10}
\]

This is uniform in `y` and every actual `R_j`. In particular

\[
 \sum_{j=0}^J\int W(y)|f_j(y,u)|^2dydu
       \lesssim_\epsilon T N^\epsilon,
 \qquad
 \sum_{j=0}^J\|h_{jk}\|_2^2
       \lesssim_\epsilon T r_k^2N^\epsilon.            \tag{E215.11}
\]

Here `J+1 lesssim T/sqrt(N)`, `integral W|phi(y/N)|^2 lesssim 1`,
and `integral |b(y/r_k)phi(y/N)|^2dy lesssim r_k^2`.
The dilation factor eight is constant. The radius integrals in
(E215.9)--(E215.11) are over the entire real line. Neither the negative
radius tail nor the tails beyond the two endpoints are removed.

Combining (E215.11) with `||f_j||_infinity<=M` proves (E215.1):
`M^8 lesssim N^2`. This calculation binds the complete coefficient
norm to the actual repeated norms, rather than replacing `r_2(n)` by
one representative.

### 3.4 A fully finite upper cost for the source certificate itself

It is also possible to estimate (E215.7) completely, albeit too weakly.
Scale-invariance of the Fourier L1 norms of the three cutoffs gives

\[
 \|\widehat h_{jk}\|_1\lesssim\sum_m|c_m|
     \lesssim N^{1/4},\qquad
 \|(h_{jk})_\theta\|_\infty\lesssim N^{1/4}.
\]

This uses the source's sharp restrictions harmlessly in Fourier L1;
it assigns no false L1 convolution-kernel bound to a sharp projection.
There are `O(S_k^(1/2))` canonical sectors, so
`A_jk,U lesssim S_k^(1/2)N^(1/2)`. Also, at every scale,

\[
 \sum_{\tau,U}|U|A_{jk,U}\lesssim\|h_{jk}\|_2^2,
\]

by the bounded sum of `W_U`, nested angular partitions and Plancherel.
Using the `M^6` branch of the minimum only at this final upper-bound
step, and summing the `O(log(2S_k))` scales, yields

\[
 \mathfrak E_\sigma(T,N)
 \lesssim N^2\sum_k\lambda_k S_k^{1/2+\sigma}
                 \log(2S_k)\sum_j\|h_{jk}\|_2^2
 \lesssim_\epsilon TN^{2+\epsilon}.                 \tag{E215.12}
\]

Choose, for example, any fixed `0<sigma<1`. The last sum converges
uniformly because `S_k lesssim r_k` and
`sum_k lambda_k r_k^(5/2+sigma)log(2r_k)<infinity`.
Thus no hidden sum of tails or envelope translates remains unpaid in
the reported upper cost. The loss of the amplitude threshold in this
last estimate is explicitly visible. A successful use of (E215.7)
would have to improve this step using actual information.

At `N=T^nu`, the ratio of (E215.1) to the target is
`T^(2nu-18/65+epsilon)`. The lower and upper limiting deficits are
`242/325` and `394/325`. The trace consequence pays `du=sqrt(N)dR`:

\[
 \int_I|F_N(0,R)|^{10}dR
 \lesssim N^{-1/2}\mathcal C(T,N)
 \lesssim_\epsilon TN^{3/2+\epsilon}.
\]

There is no favorable spatial-volume factor missing from these powers.

## 4. First doubtful or unproved step

The first new estimate not proved is (E215.8). The source supplies
(E215.7), not a bound on the actual `A_jk,U` and their good-envelope
distribution sufficient for (E215.8). This distinction is especially
visible at `r_k=O(1)`: the source scale is bounded, all angular
decompositions have bounded complexity, and the unknown high moments
of local averages remain in the right side.

There are two unsupported shortcuts to reject:

1. Keeping source parameter `N` after multiplying by a cutoff at
   spatial radius `r<<N`; its frequency thickening is `O(1/r)`.
2. Applying the unweighted superlevel conclusion directly with the
   measure `W(y)dydu`, or inserting `average_U W` on its right side,
   without a separately proved transfer theorem.

Neither objection rules out a more refined weighted proof using the
original scale `N`, or an actual arithmetic bound on the certificate.
No positive-certificate lower bound is promoted to a lower bound for
the signed moment. The conductor's communicated independent
ten-tuple absolute-kernel observation was not used in this derivation.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `exact_r2_lift` | PASS: the identity in Section 3.1 sums every ordered signed lattice representation once. |
| `actual_common_modulation` | PASS: every localized function retains `c_m e(R_j|m|)` from the same global wave; only the explicitly crude L2 upper bound takes phase moduli. |
| `weighted_fourier_normalization` | PASS: (E215.5), the fixed factor eight, the source scale, and the sign and factor `N` in (E215.9) are explicit. `W_U` and `W` remain different weights. |
| `all_windows_tails` | PASS: all `0<=j<=J`, all spatial localization radii, all envelope translates and the complete `u` integral occur; convergent sums are proved. |
| `narrow_aligned_directions` | PASS as a safeguard: canonical sectors have radial length one and can contain `O(sqrt(N))` lattice vectors at scale `N`, not `O(1)`. The axis ray `m=(k,0)` in a fixed active subannulus has coefficient sum of order `N^(-1/4)` and can align at integer radii. Nothing removes it. This is a subset control, not a lower bound for the whole wave. |
| `complete_coefficient_norms` | PASS: (E215.4), the `r_2(n)^2` second moment and every localization norm are fully costed. |
| `source_hypotheses` | PASS for (E215.7): Schwartz class, support, sharp projections, cap-count threshold, geometric volumes and envelope weights are audited. A weighted theorem at unchanged scale is not imported. |
| `all_restored_powers` | PASS: (E215.11)--(E215.12) and the displayed deficit pay windows, Jacobian, cutoffs, scales and tails. |
| `actual_arbitrary_distinction` | PASS: the adversarial control below is explicitly outside the actual coefficient family. |
| `certificate_signed_distinction` | PASS: (E215.7) is an upper certificate; its improvement is open. No signed lower bound is inferred from a positive quantity. |
| `real_endpoints` | PASS: no integral-index assumption for `T,N,R_j`; the ceiling and endpoint coverage are retained. |
| `full_quarter_scope` | PASS: success at (E215.8) would prove the tenth milestone only; the unbounded fixed-order complete moment family remains required. |
| `statement_only_control` | NOT CLAIMED BY AUTHOR: this task is NONBLIND. Independent review must bind the final report hash; no sibling or blind artifact was read. |

Here is an analytical adversarial control on any coefficient-uniform
claim of the desired strength. Fix one of the prescribed centers `R_*`
and use the single global array `d_m=c_m e(-R_*|m|)` in place of the
actual array. This is one fixed modification for all windows, not an
independent phase choice per window. At that window center, and on a
fixed small neighborhood of `(y,u)=(0,0)`, all phases lie in a common
small arc. Positivity on an active subannulus gives amplitude
`gtrsim N^(1/4)`, hence weighted tenth mass `gtrsim N^(5/2)` in that
one window. For any fixed `nu>166/325`, this exceeds
`T^(83/65+epsilon)` at `N=T^nu` for sufficiently small epsilon.
Thus the actual coefficient phases are indispensable to any positive
conclusion. This does not falsify (C215): the modified array is not the
actual one. For the actual array the fully aligned radius zero is far
outside the central comparison interval; the frozen Schwartz radius
cutoffs suppress it, and it cannot be used as the same lower bound.

No numerical experiment was run. All controls above are identities,
finite norm estimates or analytical examples.

## 6. Dependencies and exact artifacts used

The local context was exactly the assigned brief and its permitted
files. The proof graph was read by its top-level metadata and relevant
obligation entries; no historical evidence file outside the permitted
list was opened. Hashes read during this task are:

| Artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71` |
| `state/active_campaign.yml` | `5f12ab05333d3814468b66fa0597e1276ecbb61fc7f0f3deb463928644c46cca` |
| `strategy/round215_complete_localized_wave_attack.md` | `7b447077f999d022c4e9073cf2aa166c86c87f570cfc378f8826895da3ed6cf9` |
| `strategy/gauss_circle_strategy_checkpoint_round214_2026-09-28.md` | `e8ad087a36bcb9bf098056a0498242b7b5882ac34dc071b0b5007f7818647877` |
| `rounds/codex-managed/gc-full-goal-radius-source-review/reports/full_goal_harmonic_sources.md` | `50228227fa0f77a6ce944ea8e2fbfd8f1fe75ddad60662bf041a487dcb0cf4b3` |
| `rounds/codex-managed/gc-full-goal-radius-source-review/reviews/independent_harmonic_sources_review.md` | `959b82e190b0e8528284c3c15460147468ef1d41079e6eb72f7faa31774ca2c2` |

External mathematics used: only the versioned Guth--Maldague source
interface identified in Section 2. Exact theorem hypotheses were
checked in the primary text on 2026-09-28 local time. The source's
Theorem 3 was not reapplied. The elementary divisor bound, Fourier
inversion/Plancherel, Tonelli and geometric sums supply all remaining
steps. No numerical output is offered as theorem evidence.

The conductor supplied the central-cube clarification recorded above.
No current sibling report, blind packet/report, shared synthesis,
validation matrix or successor file was opened or modified.

## 7. Recommended state effect

**Retain** (E215.7) as a complete, threshold-preserving source-transfer
candidate with (E215.8) explicitly open, and retain (E215.1)/(E215.12)
as its fully priced insufficient norm bound, subject to independent
seam review. **Reject** the free weighted application at unchanged
cone scale. **No change** to accepted exponents, the physical moment
parent, M1/M2, GAR, the proof draft or the quarter target.

This report stops after its assigned Round-215 task. It neither selects
a successor objective nor begins another round.
