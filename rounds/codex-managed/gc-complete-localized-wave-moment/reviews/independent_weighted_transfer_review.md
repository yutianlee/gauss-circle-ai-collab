# Round 215 independent weighted-transfer seam

Campaign: `gc-complete-localized-wave-moment`.
Reviewer: `actual_lattice_envelopes`, reassigned after freezing its own
report. Role: independent source/normalization reviewer, NONBLIND.
Date: 2026-09-28, Asia/Shanghai. Allocation: entirely analytical/source
work; zero experiments.

Reviewed report:
`rounds/codex-managed/gc-complete-localized-wave-moment/reports/weighted_envelope_transfer.md`.
Verified final SHA-256:
`a157a86f1ce23665e22c2c513fa3be3f4b410c01fbd7f313ee033e07b234887a`.
Every verdict below binds this exact hash. No original report was edited.

## 1. Result

**GREEN for the assigned seam. No required correction.**

The spatial localizer expansion is a legal transfer of the frozen
weighted moment to a convergent sum of unweighted source applications.
Its frequency support requires the stated parameter
`S_k asymp min(N,r_k)`. The theorem's amplitude cutoff is preserved
correctly in (E215.6)--(E215.7), including the factor `5/3`.

The actual grouped second moment and the independent upper estimate
of the entire positive source certificate both give
`T N^(2+epsilon)`, with all real windows, spatial tails, temporal tails,
source scales and envelope translates paid. Neither estimate proves
the frozen target. The report correctly leaves (E215.8) open and does
not turn this insufficient upper cost into a lower bound or a broad
impossibility assertion.

## 2. Exact scope and source hypotheses reviewed

Use the frozen real parameters, exact `c_m`, all `0<=j<=J`, product
cutoffs, and `W` as defined in the reviewed report and strategy215.
The permitted cutoff clarification supplies fixed lower bounds on
`[-1,1]^2` for phi and `[-1,1]` for eta. This is used for coverage and
the separate aligned control, not to discard any tail.

The only primary source consulted is Guth--Maldague,
[arXiv:2206.01093v2](https://arxiv.org/html/2206.01093v2), Theorem 2
and its definitions: the introduction's cone/projection conventions,
Section 5 equations (29)--(30), and the envelope-weight definition
there referring to (13). The amplitude condition, global nonzero-cap
count, weighted square-function average, and unweighted superlevel
measure agree with (E215.2). The weights are associated with envelope
translates; they are not the problem's spatial `W`. The angular
partitions are nested, and the source permits a power-of-four scale.
The report's fixed truncation/dilation and positive endpoint additions
do not change the theorem's power. No source theorem with an arbitrary
spatial measure is credited.

The external proof is not being independently reproved. The following
application calculations were checked directly rather than inferred
from the prior round's different small-cap calculation.

## 3. Independent derivation and seam checks

### 3.1 The whole spatial weight and uniform Fourier support

Put `r_k=r_0 2^k` and `lambda_k=(1+r_k^2)^(-100)`. Since `b` is
bounded below on the unit disk, choosing the first `r_k>=|y|` gives
the lower side of (E215.5). For its upper side, if `|y|>=r_0`, split
the sum at that first index. Larger radii contribute a geometric
tail of order `|y|^(-200)`. For smaller radii use, for any fixed
`L>200`,

\[
 |b(y/r_k)|^{10}\ll_L (|y|/r_k)^{-L}.
\]

Then their sum is bounded by
`|y|^(-L) sum_(r_k<|y|) r_k^(L-200)`, also of order
`|y|^(-200)`. The region `|y|<r_0` is bounded with constants allowed
to depend on the fixed `r_0`. Thus the comparison is uniform in
`T,N,j` and retains all spatial radii. Large constants at the fixed
origin scale are harmless and do not depend on `T`.

The finite plane-wave centers for `g_jk=b(y/r_k)f_j` are
`(m/sqrt N,|m|/sqrt N)`, on cone radii `[1,2]`. Multiplication by
the cutoffs convolves them with a compact Fourier set of width at
most `C(N^(-1)+r_k^(-1))`. For `h_jk(z)=g_jk(z/2)`, frequencies
are halved and the centers lie on radii `[1/2,1]`. Its norm obeys
`||h_jk||_p^p=8||g_jk||_p^p`, with no dependence on `p` in this
Jacobian. Frequency blobs at the radial endpoints remain within the
same stated neighborhood of the truncated cone.

Choose a fixed sufficiently small `c>0`, and let `S_k` be the largest
power of four no greater than `c min(N,r_k)`. Then

\[
 \frac{c}{4}\min(N,r_k)<S_k\le c\min(N,r_k),\qquad
 C(N^{-1}+r_k^{-1})\le S_k^{-1},
\]

after making `c` small enough. This verifies the source support
hypothesis quantitatively. There are three cases:

- For the finitely sized spatial radii, including `r_k=r_0`, the
  source scale is a sufficiently large fixed constant. Choosing
  `r_0` and the lower large-`T` threshold according to the fixed
  source parameter ensures that this case is lawful.
- For `r_0<=r_k<=N`, the controlling thickness is `O(1/r_k)` and
  `S_k asymp r_k`.
- For every `r_k>N`, including the infinite tail, the thickness is
  `O(1/N)` and `S_k asymp N` uniformly in `k`.

For bounded remaining `T`, `N` and the number of active frequencies
are bounded in the frozen band, so the direct norm estimate absorbs
the parameter range without applying a large-scale source theorem
there. Every `h_jk` is Schwartz. None of these operations changes
the original coefficient modulation `c_m e(R_j|m|)`.

### 3.2 Layer cake and the retained amplitude cutoff

The complete coefficient mass is `sum_m|c_m|<<N^(1/4)`, so the
fixed cutoff suprema give a common ceiling `M=C N^(1/4)` for all
`h_jk`. Write `A=A_jk,U`, `n=n_jk(s)` and `S=S_k` for one
source summand. Multiplying its superlevel inequality by `10 alpha^5`
and integrating over `0<alpha<M` gives the exact scalar integral

\[
 10\int_0^M\alpha^5
       \mathbf1_{\{\alpha^2\le K_\sigma S^\sigma n^2A\}}
       d\alpha
 =\frac53\min\{M^6,(K_\sigma S^\sigma n^2A)^3\}.
\]

This reproduces (E215.6). In particular the cap count is squared
before the cubic power and remains tied to the actual function and
source scale. The outer source factor `K_sigma S^sigma` is also
retained. Tonelli is legitimate because the summands are nonnegative.
Adding the weight comparison and the fixed factor eight proves
(E215.7), with `K_sigma` absorbed only in its allowed fixed constant.
The infinite envelope sum has not been truncated in this step.

### 3.3 Exact grouped second moment

Let `a_n` and `B_n(y)` have the definitions in Section 3.3 of the
report. The `u` integral of a pair of terms, with the convention
`hat q(t)=int q(u)e(-ut)du`, is

\[
 N\widehat{|\eta|^2}\bigl(\sqrt N(\sqrt{n'}-\sqrt n)\bigr).
\]

The sign, factor `N`, and argument agree with (E215.9). Compact
Fourier support of eta implies compact Fourier support of its square;
if that support lies in `[-L_eta,L_eta]`, then for `n,n'` in `[N,4N]`
any surviving pair satisfies

\[
 |n-n'|\le \frac{L_\eta}{\sqrt N}(\sqrt n+\sqrt{n'})
              \le4L_\eta.
\]

This gives a bounded-degree adjacency relation, regardless of the
nonintegral values of `T,N`. It does not require exact diagonal
orthogonality. The actual `e(R_j(sqrt n-sqrt n'))` factor is present
before the stated absolute upper bound. Bounding `|B_n|` by `r2(n)`,
using `2ab<=a^2+b^2`, and then the divisor bound gives

\[
 \int|\eta(u/N)F_N(y/\sqrt N,R_j+u/\sqrt N)|^2du
 \ll N\sum_n |a_n|^2r_2(n)^2\ll_\epsilon N^{1/2+\epsilon}.
\]

The integration is over the entire real line, so this one calculation
includes both endpoint tails and negative radii. Since
`J+1<<T/sqrt N`, integration against `W|phi|^2` gives
`T N^epsilon`. Integration instead against `|b(y/r_k)phi(y/N)|^2`
costs at most `C r_k^2`, giving `T r_k^2 N^epsilon` after the fixed
dilation. These are precisely both inequalities of (E215.11).
The scalar inequality `|f_j|^10<=M^8|f_j|^2`, with `M^8<<N^2`,
therefore proves the complete `T N^(2+epsilon)` bound directly.

### 3.4 The certificate's own finite upper cost

The Fourier `L1` norm of a dilated cutoff is unchanged by its scale.
Convolution for the product of `b`, phi and eta, followed by summing
the plane-wave coefficients, consequently gives
`||hat h_jk||_1<<N^(1/4)` uniformly in `j,k`. A sharp frequency
restriction decreases this norm, so every canonical projection has
supremum at most `C N^(1/4)`. This reasoning does not use a false
integrable convolution kernel for sharp projections.

There are `O(S_k^(1/2))` canonical angular sectors. Integrating their
squared supremum bounds against an envelope weight of mass `O(|U|)`
gives

\[
 A_{jk,U}\ll S_k^{1/2}N^{1/2}.
\]

For each fixed source scale the envelope-weight translates have a
uniformly bounded sum. Nested disjoint angular partitions and
Plancherel hence give

\[
 \sum_{\tau,U}|U|A_{jk,U}\ll\|h_{jk}\|_2^2.
\]

Use `A^2<=C S_k^(1/2)N^(1/2) A` and the `M^6` branch of the
minimum. The result for that `j,k` is at most
`C N^2 S_k^(1/2+sigma) log(2S_k)||h_jk||_2^2`.
After summing `j`, (E215.11) reduces the remaining tail to

\[
 T N^{2+\epsilon}
 \sum_{k\ge0}\lambda_k r_k^{5/2+\sigma}\log(2r_k).
\]

This geometric sum converges uniformly when, for example,
`0<sigma<1`. The inequality `S_k<<r_k` handles both `r_k<=N` and
the full `r_k>N` tail without a new factor of `N`. Thus the entire
certificate, including every envelope translate, has the stated
`T N^(2+epsilon)` upper cost. Removing the amplitude cutoff occurs
only at this explicitly identified last upper-bound step; it is not
part of the source-transfer identity.

### 3.5 Powers and mathematical scope

Dividing the cost `T N^2` by the target `T^(83/65)` gives
`T^(-18/65)N^2`. At the two limiting critical exponents the losses
are `242/325` and `394/325`, respectively. Both calculations match
the report. The spatial trace and `du=sqrt N dR` then give the
displayed physical cost `T N^(3/2+epsilon)`.

The aligned modified coefficients supply the separate weighted peak
control with mass `N^(5/2)`: amplitude `N^(1/4)` on a fixed spatial
disk and fixed `u` interval yields exactly that tenth power. Choosing
one global rephasing keeps the modification consistent across all
windows, but still changes the frozen arithmetic family. The report
states this distinction correctly. Actual rational/axis rays are not
discarded, and their subset control is not mislabeled as a lower bound
for the complete actual wave.

## 4. First doubtful or unproved step

There is no unresolved step requiring correction in the assigned seam.
The first positive arithmetic estimate still missing is (E215.8),
which would bound the actual complete source certificate more sharply
than the available norm calculation. The threshold-preserving transfer
does not prove that estimate by itself.

The two rejected shortcuts have precisely limited scope: compact
spatial localization at radius much smaller than `N` changes the
available cone neighborhood, and an unweighted source theorem does
not directly replace Lebesgue measure by `W(y)dydu`. These observations
do not exclude another weighted argument or a coefficient-sensitive
estimate. The report keeps this distinction throughout.

## 5. Controls and outcomes

| Control | Review outcome |
|---|---|
| Actual `r2` lift and grouped norms | GREEN: all representations remain, including the necessary `r2(n)^2` second-moment factor. |
| Common center modulation | GREEN: localizers preserve the one original wave; modulus is used only in the explicitly crude second-moment bound. |
| Spatial weight and Fourier normalization | GREEN: dyadic localizers cover the full weight, dilation costs eight, and the temporal transform has the correct sign and factor. |
| Source scale in all radius regimes | GREEN: power-of-four `S_k asymp min(N,r_k)` satisfies support uniformly; bounded source scales are chosen above the fixed theorem threshold. |
| Amplitude thresholds and cap counts | GREEN: exact layer-cake factor `5/3`, actual cap count, and the entire minimum are retained. |
| All windows and tails | GREEN: every `j`, every `k`, every envelope translate and the entire temporal line are paid. |
| Narrow and aligned directions | GREEN: no `O(1)` occupancy claim is made for canonical sectors; no favorable angular deletion occurs. |
| Restored powers | GREEN: both complete upper costs are `T N^(2+epsilon)` and the stated deficits check. |
| Actual versus modified arrays | GREEN: the aligned control is outside the actual coefficient family and does not refute (C215). |
| Positive certificate versus signed quantity | GREEN: (E215.8) stays open, and insufficient cost is not an actual lower bound. |
| Real endpoints | GREEN: the ceiling, partial endpoints and noninteger norm cutoffs are retained. |
| Full-quarter scope | GREEN: a fixed tenth-moment success would be a milestone only; no parent or quarter promotion is licensed. |
| Statement-only independence | NOT CLAIMED: this reassigned review is NONBLIND and binds the exact report hash. |

No numerical experiment was used. The source's proof internals and any
theorem beyond the assigned interface were not re-audited.

## 6. Dependencies and artifacts used

This same-round reassignment used only:

1. The already-read protocol and permitted strategy/context from the
   original task, without reopening their historical provenance files.
2. The reviewed report at the exact SHA-256 in the header.
3. `rounds/codex-managed/gc-complete-localized-wave-moment/controls/cutoff_normalization_clarification.md`.
4. The exact versioned primary source and definitions specified in
   Section 2, consulted directly for this seam.

The reassignment explicitly authorized this one sibling report. No
other sibling, statement-only packet/report, ledger, synthesis,
validation matrix, shared state, or successor file was read or edited.
The reviewer's original discovery report remains frozen at
`4e7c9088141687087ceb8582028cbdffd3b66926fffca983c6086002ed7e6de6`.
Only this assigned review file is written.

## 7. Recommended state effect

**GREEN: retain the reviewed source transfer and complete insufficient
cost at the exact final hash above. No required mathematical correction.**
Retain (E215.8) as an open sufficient estimate. No change is justified
to accepted arithmetic bounds, exponents, M1/M2, GAR, endpoints or the
proof draft. This review stops here and does not select a successor
round or promote an unestimated certificate.
