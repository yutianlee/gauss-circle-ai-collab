# Round 214: sources for the complete signed radius energy

Campaign: `gc-full-goal-radius-source-review`. Task: `signed_radius_sources`.
Role: source auditor, selected context, NONBLIND.
Generated: 2026-09-28 Asia/Shanghai; primary-source checks completed on
2026-09-27 UTC. Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Candidate evidence only. All mathematical work was analytical or source
inspection; zero numerical experiments. Two theorem interfaces were
audited, with each proposed import stopped at its first exact failure.

## 1. Result: two scoped import failures, with the full arithmetic gate retained

No inspected theorem proves the complete signed radius estimate. This is
a bounded source review, not an assertion that every possible source has
been excluded.

The first audited interface, Chamizo's uniform shifted correlation of
two sum-of-two-squares coefficients, really does allow all the growing
original shifts required here. The first failure is the extra arithmetic
coefficient, not lack of shift uniformity. Grouping two of the four
factors does not turn their product into an admissible coefficient of
that theorem. A prefix error cannot be transferred through the remaining
two factors at subpower cost. Even hypothetical four-factor analogues
with that theorem's error exponent would be quantitatively insufficient
under the usual absolute Abel transfer.

The second interface is the September 2026 Wessel--zur Verth theorem on
quadratic forms with restricted coordinate weights. The exact
four-norm parallelogram is an eight-variable quadratic form of signature
`(4,4)`. The source requires an off-block rank at least five, impossible
in eight variables. The actual radius energy instead encodes four
quadratic equations in sixteen variables, whereas the source treats one
equation. Neither variable regrouping nor extra dummy variables repairs
these hypotheses while retaining the original count.

Both conclusions preserve the full signed eight-factor kernel. They do
not rerun the fixed-shift Matthiesen failure or the positive-certificate
obstructions from 212--213. In particular, the radius interface remains
a potentially useful milestone, but its displayed diagonal-scale
certificate cannot itself approach the full quarter exponent. Section
3.6 gives a necessary `5/16` limit for that certificate, without claiming
a lower bound for the arithmetic energy or the discrepancy.

## 2. Exact statement and hypotheses of the interface being tested

Write `e(x)=exp(2 pi i x)`. Keep

\[
b=83/650,\quad T\ge2,\quad T^{166/325}<N<T^{242/325},
\]
\[
L=\max(2,\lceil\sqrt N T^{-2b}\rceil),\qquad
K=\max(2,\lceil NT^{-4b}\rceil).
\]

The fixed real smooth masks are

\[
g(t)=(t/N)^{-3/4}\Psi(\sqrt{t/T})v(t/N),\qquad
W_{h,k}(t)=g(t)g(t+h)g(t+k)g(t+h+k).
\]

They are zero extended with their actual overlap and internal zeros;
`W^(r)=O_r(N^(-r))`. The arithmetic and phase are exactly

\[
a_{h,k}(n)=r_2(n)r_2(n+h)r_2(n+k)r_2(n+h+k),
\]
\[
\psi_{h,k}(t)=\sqrt{t+h+k}-\sqrt{t+k}-\sqrt{t+h}+\sqrt t,
\quad D_{h,k}(R)=\sum_n a_{h,k}(n)W_{h,k}(n)e(R\psi_{h,k}(n)).
\tag{2.1}
\]

Here `r2(n)` counts all ordered signed integer representations. In its
divisor expansion it is `4 sum_(d|n) chi4(d)`, so a four-factor expansion
has `4^4`, and a double-discrete energy expansion has `4^8`. The harmless
fixed constants can enter upper bounds, but none of the character sums
or translated factors can be replaced by independent copies.

Let `rho_(h,k)=rho^loc_(h,k)` be the candidate nonnegative local product
from 212, used only with its proved bound `rho<<T^epsilon`, not as an
established integer mean. Set

\[
I_{h,k}(R)=\int W_{h,k}(t)e(R\psi_{h,k}(t))\,dt,
\qquad E_{h,k}=D_{h,k}-\rho_{h,k}I_{h,k}.
\]

For `q=2^j>=1`, use the complete nonempty shell

\[
\Omega_j=\{1\le h<L,\ 1\le k<K:\ h\ne k,
\ q<Thk/N^{3/2}\le2q\},\quad m_j=|\Omega_j|,
\]
\[
Q_j(E)^2=\frac1{Tm_j}\int_{T/2}^{2T}
                         \sum_{\Omega_j}|E_{h,k}(R)|^2\,dR.
\tag{2.2}
\]

The desired input is the uniform inequality

\[
Q_j(E)\ll_\epsilon T^\epsilon(\sqrt N+Nq^{-3/2}).
\tag{R214}
\]

All original real endpoints, overlaps, and ordered pairs occur in this
definition. Repeated shifts and products `Thk/N^(3/2)<=1` are separately
paid by the inherited complete estimates; they are not assigned a
distinct-root density. No selected dense subfamily can replace a
complete shell in (R214).

The anisotropic dimensions are substantial. At the limiting upper
power scale, `N=T^(242/325)`, the shift lengths have powers `38/325`
and `76/325`, their product has power `114/325`, and the largest
product frequency has power `76/325`. These endpoint powers are
comparison limits, not claims that the open endpoint is included.

## 3. Derivations, source cards, and complete costs

### 3.1 The signed radius kernel and the arithmetic which a source must estimate

Put

\[
\mathcal K(y)=\int_{1/2}^{2}e(vy)\,dv
 =e(5y/4)\frac{\sin(3\pi y/2)}{\pi y},\qquad \mathcal K(0)=3/2.
\]

For one fixed pair, suppress its subscripts and define

\[
X=\sum_{n,m}a(n)a(m)W(n)W(m)
                  \mathcal K(T[\psi(n)-\psi(m)]),
\]
\[
Y=\sum_n a(n)W(n)\int W(t)
                  \mathcal K(T[\psi(n)-\psi(t)])\,dt,
\quad
Z=\iint W(t)W(u)\mathcal K(T[\psi(t)-\psi(u)])\,dt\,du.
\]

Then exactly

\[
Q_j(E)^2=\frac1{m_j}\sum_{\Omega_j}
                 (X-2\rho\Re Y+\rho^2Z).
\tag{3.1}
\]

`X` contains eight actual `r2` factors. Its diagonal is
`(3/2) sum_n a(n)^2 W(n)^2 << N T^epsilon`; this does not upper-bound
`X`. The kernel is complex and satisfies `K(-y)=conjugate(K(y))`, so
pairing makes (3.1) real. Replacing it by its modulus changes the
arithmetic assertion and returns to an already rejected certificate.

Equivalently, a sufficient one-sided signed assertion is

\[
\sum_{\Omega_j}(X^{\rm off}-2\rho\Re Y+\rho^2Z)
 \ll_\epsilon m_j T^\epsilon(N+N^2q^{-3}).
\tag{3.2}
\]

The factor `m_j` is essential. An estimate averaged over a much larger
shift region does not automatically give (3.2), and an estimate for
`sum D` has the wrong norm.

### 3.2 Source card A: the valid pair-correlation theorem and its first failure

**Primary version.** Fernando Chamizo, *The additive problem for the
number of representations as a sum of two squares*,
[arXiv:2009.01667v1, 3 September 2020](https://arxiv.org/html/2009.01667v1),
Theorem 1.1; [published version, 26 January 2022](https://link.springer.com/article/10.1007/s00009-021-01959-3),
Mediterranean Journal of Mathematics 19, article 44. Both versions were
checked; arXiv currently lists only v1. No withdrawal is displayed.

The audited specialization is the following. For positive integer `d`,
let `2^nu||d`,

\[
c_d=8|2^{\nu+1}-3|\,\sigma(d/2^\nu)/d.
\]

With `r=r2` counting all representations, the theorem and the permissible
Hecke exponent `7/64` give

\[
\sum_{n\le x}r_2(n)r_2(n+d)=c_dx+O_\epsilon(d^\epsilon x^{2/3})
 \quad\text{when }d^{117/64}\le x.
\tag{3.3}
\]

The unrestricted theorem has other shift regimes; none is needed for
the original shifts in the proposed pair grouping. Its weight is the
prefix indicator, not an arbitrary arithmetic sequence. The two-adic
normalization is included in `c_d`. This card audits that exact
specialization, not a new theorem for products of theta coefficients.

Here is the independent application check. Write `N=T^alpha` on fixed
interior scales. Since `K asymp NT^(-4b)` and `L<<K`, all
`d in {h,k,h+k}` obey

\[
d\ll NT^{-4b},\qquad
\frac{d^{117/64}}N\ll
T^{(53\alpha-468b)/64}=o(1)
\]

uniformly up to `alpha=242/325`; the numerator there is
`53(242/325)-468(83/650)<0`. Bounded cutoffs and bounded `T` are paid
by constants. Thus the growing-shift hypothesis is genuinely satisfied
on real prefixes `x asymp N`. Differences of two such prefixes cost
`O(T^epsilon N^(2/3))`, not `O(length^(2/3))`.

The proposed direct use would write

\[
D_{h,k}(R)=\sum_n r_2(n)r_2(n+h)\,B_{h,k,R}(n),
\quad
B_{h,k,R}(n)=r_2(n+k)r_2(n+h+k)W(n)e(R\psi(n)).
\tag{3.4}
\]

**First failed hypothesis:** the remaining arithmetic factor in `B` is
not among the permitted weights in (3.3). It has no proved subpower
variation or spectral expansion with a paid norm. For completeness,
the elementary available variation bound is

\[
\|B\|_\infty+\sum_n|B(n+1)-B(n)|
 \ll_\epsilon T^\epsilon(N+q).
\]

Indeed the arithmetic factor is bounded by `T^epsilon`, so its `O(N)`
successive differences cost `O(N T^epsilon)`; the smooth oscillatory
factor has total variation `O(1+q)`. In this band `q<<N`. Abel transfer
of (3.3) consequently gives an error at best from this certificate of
size `N^(5/3)T^epsilon`, worse than the original trivial `NT^epsilon`.
This is a failed upper-bound route, not a lower bound on its true error.

Iterating pair main terms would also introduce `c_h^2`, which is not
the actual four-point local product. Neither independent translates
nor independence of the two pair errors is justified. In the radius
square the two additional copies only increase this unresolved
coefficient problem. The shift `n-m` there also ranges up to `O(N)`;
the small-original-shift calculation above is not asserted for it.

A separate quantitative control makes the scope transparent. Even if,
contrary to what the source proves, an unweighted four-factor prefix
error `N^(2/3)` were granted, its smooth Abel transfer would cost

\[
N^{2/3}(1+q).
\]

At the upper-band comparison limit and `q asymp Lambda_*`, this has
power `712/975`, exceeding `4b=498/975` by `214/975`. Even the stronger
fictional *local* error `ell^(2/3)`, where `ell=N/(1+q)`, would cost
`N^(2/3)(1+q)^(1/3)`, with power `560/975`, still exceeding the target
by `62/975`. No fictional estimate is credited to Chamizo. These are
cost controls on two proposed transfers, not additional theorem audits.

### 3.3 Source card B: the recent restricted-quadratic theorem

**Primary version.** Mieke Wessel and Svenja zur Verth,
[*Solving quadratic forms in restricted variables with the circle
method*](https://link.springer.com/article/10.1007/s00605-026-02189-z),
Monatshefte fuer Mathematik, version of record 9 September 2026,
DOI 10.1007/s00605-026-02189-z, Theorem 1.8 and Condition L1.
The publisher's complete statement and its defined conditions were
inspected; no correction or withdrawal is displayed.

For a nonsingular integral quadratic form in `s` variables the source
uses identical nonnegative product coordinate weights. It assumes
conditions C, D, K, L1, L2 and smooth approximability of their cumulative
weight. L1 requires, after a permutation, an off-block matrix rank at
least 5. The conclusion has error
`A(B)^s B^(-2)(log B)^(-A)` for every fixed `A>0`. With unit coordinate
weights, the distribution and weight conditions hold, and this becomes
`O(B^(s-2)(log B)^(-A))`. It remains a theorem for one equation and the
stated region, with the rank hypothesis intact.

Here is the exact geometric application test, independently derived.
For `z_i=(x_i,y_i) in Z^2`, put `Q_i=|z_i|^2`. Summing the actual
four coefficients over `n,h,k` counts, with multiplicity exactly one
per ordered representation tuple, the solutions of

\[
Q_0+Q_3-Q_1-Q_2=0,
\quad n=Q_0,\quad h=Q_1-Q_0,\quad k=Q_2-Q_0,
\tag{3.5}
\]

with `1<=h<L`, `1<=k<K`, all original norm supports and the selected
product shell. The form in (3.5) is nonsingular of rank 8 and signature
`(4,4)`. Its displayed matrix is diagonal, so all off-block ranks under
permutation are zero. Even an arbitrary invertible coordinate change
in eight variables cannot create an off-block rank exceeding 4.
**First failure: Condition L1.** This terminates the direct import.

The norm-coordinate domain is also a thin coupled region, not a
coordinate product: normalized widths in the two differences are
`L/N` and `K/N`. A partition or coordinate change would require its own
uniform constants, congruence treatment and coefficient norms. None is
claimed free. In particular the modulus outside each arithmetic fiber
is equivalent to allowing separate unit complex multipliers for the
shift pairs; these are not the source's nonnegative product weights.

For the actual energy introduce another four norms `P_i=|w_i|^2`.
Its exact equations are

\[
\begin{split}
Q_0+Q_3-Q_1-Q_2&=0,\quad
P_0+P_3-P_1-P_2=0,\\
(Q_1-Q_0)-(P_1-P_0)&=0,\\
(Q_2-Q_0)-(P_2-P_0)&=0.
\end{split}
\tag{3.6}
\]

These are four independent quadratic equations in sixteen coordinates,
with `n=Q0`, `m=P0` and shared `h,k`. The discrete kernel is precisely
`K(T[psi_(h,k)(n)-psi_(h,k)(m)])` from (3.1), including its sign and
complex phase. A single arbitrary linear combination of (3.6) admits
extra solutions; it is not equivalent to (3.6). Squaring and adding
the four equations would make a quartic equation. The theorem therefore
does not treat this energy even though sixteen exceeds ten.

Adding free dummy coordinates to (3.5) makes its quadratic form
singular. Adding new nonzero quadratic terms changes its solution set.
Restricting such new coordinates to zero is not the source's unit
coordinate-weight specialization. Thus dimensional padding is not an
admissible repair. This no-go concerns this source interface, not the
circle method on the structured system (3.6).

### 3.4 Thin volumes cannot be silently replaced by full-size errors

The exact norm parameters of (3.5) are `(n,h,k)`, with scale volume
`NLK`; those of (3.6) are `(n,m,h,k)`, with scale volume `N^2LK`.
These are dimension and normalization statements, not unproved
asymptotics for integer points. A full-size four-norm box has parameter
scale `N^3`; the eight-norm system has parameter scale `N^4`.

Consequently, even an *optimistically granted* error
`N^4(log N)^(-A)` for (3.6), uniform over the actual shell and kernel,
would normalize to

\[
\frac{N^4}{m_j}(\log N)^{-A}.
\tag{3.7}
\]

Taking a complete shell with `q asymp Lambda_*` and `m_j asymp LK`
is possible on fixed interior scales by choosing a dyadic product
shell bounded away from the maximal product. At the upper comparison
limit, (3.7) has power `(968-114)/325=854/325`. The allowed energy
scale `N+N^2q^(-3)` there has largest power `256/325`. The deficit is
`598/325` before any norm or weight losses. A fixed logarithmic saving
cannot pay it. This calculation is deliberately generous: source B
does not assert the hypothetical system theorem or its uniformity.

An effective theorem must operate at the actual anisotropic volume
with quantitative signed cancellation, not merely assert a full-box
local-density asymptotic. Local solvability and the bounded candidate
product do not fill this gap.

### 3.5 Every restoration in the radius route

Let `Lambda_*=TLK/N^(3/2) asymp T^(76/325)` and
`delta_j=m_j/(LK)`. The inherited complete count gives

\[
\delta_j\ll\min(1,q\log(2L)/\Lambda_*),\qquad
\sum_j\delta_j\le1.
\]

The exact identity
`psi(t)=-(1/4) integral_0^h integral_0^k(t+u+v)^(-3/2)dvdu`
places the radius frequencies in an interval of width `O(q/T)`.
The previously reviewed enlarged-window transfer therefore costs

\[
\sup_{R\in[T/\sqrt2,\sqrt3T]}\operatorname{RMS}_{\Omega_j}|E(R)|
 \ll\sqrt q\,Q_j(E)+C_B NT^\epsilon q^{-B}.
\tag{3.8}
\]

The `sqrt(q)` factor and the global-envelope Schwartz tail are part of
the target, not artifacts that a new source may omit. Using every
complete shell, (R214) and (3.8) give

\[
\sup_R\frac1{LK}\sum_{\Omega}|E_{h,k}(R)|
 \ll_\epsilon T^\epsilon\left(\sqrt{N\Lambda_*}+\frac N{\Lambda_*}\right).
\tag{3.9}
\]

The powers at the upper limit are `159/325` and `166/325`. Choosing
fixed `B>1` pays the tail by `NT^epsilon/Lambda_*`. Smooth integration
by parts on the entire positive radius interval pays
`rho I=O_A(NT^epsilon q^(-A))`; consequently `Q_j(D)` and `Q_j(E)`
differ by at most that amount. This is a norm equivalence using only
the size of the candidate density, not an integer-mean theorem.

Repeated shifts cost at most `T^epsilon N/K`; small products cost at
most `T^epsilon N/Lambda_*` after logarithms. The model has the same
complete averaged price. The two-stage finite transfer then gives

\[
|F_N|^4\ll T^\epsilon
 (N/L^2+N/K+T^{4b}),\qquad |F_N|\ll T^{b+\epsilon}.
\]

The inherited complementary scales, singleton, infinite tail,
smoothing and real-endpoint reconstruction yield only
`P(X)<<X^(1/4+b/2+epsilon)=X^(102/325+epsilon)`.
No source above proves this conditional input, so this report records
no actual exponent gain.

### 3.6 Full-goal check on the displayed certificate

Independently of the source failures, consider the displayed restored
envelope in (3.9) with a free positive product frequency `Lambda`.
Its two terms satisfy

\[
\sqrt{N\Lambda}+N/\Lambda\gg N^{2/3}:
\]

if `Lambda>=N^(1/3)` the first term is at least `N^(2/3)`; otherwise
the second is larger. Thus at `N=T^(3/4)` this particular fourth-power
certificate cannot be smaller than `T^(1/2)`, regardless of how
integer differencing lengths are chosen. The two elementary
complementary caps have powers `N^(1/4)=T^(3/16)` and
`(T/N)^(1/2)=T^(1/8)` at that scale. The displayed certificate and
these caps cannot certify `b<1/8`, hence cannot certify a squared-radius
exponent below `5/16` by this restoration alone.

This is a necessary limitation of the formula being optimized, not a
complete optimization theorem, and not a claim that the true `Q_j` is
at least `sqrt(N)`. A one-sided upper bound containing a diagonal-size
term can be sharpened by further signed arithmetic; no positivity of
its off-diagonal has been assumed here. The blind task, which was not
read, is responsible for the independently isolated full optimization.

For the quarter goal one needs a stronger complete estimate, a different
pointwise transfer, a higher-order family that avoids this fixed
certificate limit, or the independent full M1/M2 route. Proving (R214)
would be meaningful but would not remove that strategic requirement.

## 4. First doubtful or unproved step

The first arithmetic gap remains (3.2), equivalently (R214), with the
actual eight-factor coefficient, complete shifts, real radius kernel
and full shell normalization. No source theorem closes it.

For source A the first unjustified operation is inserting the other
two translated representation functions as a cheap weight in the
two-factor theorem. Its shift condition is satisfied; claiming instead
that it fails for growing shifts would misdiagnose the interface.

For source B the first failed hypothesis on the four-norm geometry is
off-block rank at least 5. On the radius-energy geometry the first scope
failure is four simultaneous equations instead of one. These imports
are stopped there. The subsequent thin-volume calculations are explicit
optimistic controls, not applications of either failed theorem.

There is no assumption that the candidate density is the true mean,
that pairwise theta correlations imply fourfold independence, that
unweighted prefix errors localize at unchanged cost, or that radius
averaging gives a fixed-radius bound freely. Those are exactly the
operations a successful replacement source would have to justify.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `actual_four_point_coefficients` | PASS in every interface and obstruction. Four actual factors remain in D; eight remain in X; the exact representation-count normalization is retained. Neither audited theorem is credited with a larger coefficient class. |
| `complete_shifts_overlap` | PASS. Exact rounded L, K, ordered complete shells, full overlaps and paid repeated/small-product sectors are recorded. No theorem on a selected shift subfamily is substituted. |
| `local_global_discrepancy` | PASS as a distinction. Pair prefix errors remain at N scale on short intervals. The hypothetical local transfer is separately labeled and fully priced. |
| `density_hypotheses` | PASS as a distinction. Only the bounded local candidate is used in norm equivalence; no integer mean or independent pair-density factorization is claimed. |
| `real_endpoints` | PASS. All sums are zero extended; source prefixes permit real x; the enlarged real radius window and recovery margins are preserved. |
| `all_restored_powers` | PASS. Shift dimensions, arithmetic variation, model/tail prices, shell fractions, bandwidth loss and final reconstruction are explicit. Failed source imports receive no saving. |
| `signed_absolute_distinction` | PASS. The phase ofK, DD off-diagonal, mixed and continuous terms remain. Formula (3.7) is an optimistic error certificate, never a lower bound on the signed energy. |
| `full_quarter_scope` | PASS. The fixed input gives at most the 102/325 milestone; the displayed general certificate has a necessary 5/16 limitation. Neither statement proves a full-goal obstruction. |
| `statement_only_control` | NOT CLAIMED here. No sibling, blind packet/report, or conductor calculation was opened. The elementary check in 3.6 is selected-context work only. |
| `source_versions_hypotheses` | PASS for the two cards. Exact arXiv/publisher versions and theorem identifiers are given; the first failure is explicit. Other papers were metadata/abstract screens only. |
| `complete_frontier` | RETAIN. M1 HARD includes every small t; M1 SMOOTH is independent. M2 TOP/BAL/UNBAL and endpoints remain open. GAR only supplies total M1 and still needs M2. The original tenth gate and full high-moment family remain independent alternatives. |

Two further exact controls: the actual modulo 4 zero sector from 212
annuls both a and its candidate density and therefore all terms in (3.1).
Repeated shifts are not silently included in a convergent distinct-root
density. The source B dimensional argument survives every invertible
eight-variable coordinate change, so it is not a superficial objection
to writing the form diagonally. No numerical controls were necessary.

## 6. Dependencies, primary checks, and exact artifacts

Only the assigned brief, its permitted context and primary web sources
were read. The authoritative graph was inspected at its preamble and
the relevant GC-target, M9-M1, M9-M2 and complete-large-values nodes;
cited child paths were not opened. No sibling or conductor artifact
was read. The conductor suggested the norm geometry in a message;
equations (3.5)--(3.6) and their rank/volume checks were then derived here.

| Permitted artifact | SHA-256 at inspection |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71` |
| `state/active_campaign.yml` | `c3d19ffa14feae76e1dc0cb5775a346c2e7e08bfc761e492c97caeba24f0aaed` |
| `strategy/round214_full_goal_source_review.md` | `fb0126e2c5adf47b6cf7df92fb642b30b2751ee564f45d214c1ee4c980dfcc09` |
| `strategy/gauss_circle_strategy_review_2026-09-23.md` | `0729f1d9c596867e7a06bdcd096847b32e6747653235706b01275a153bd617c6` |
| `strategy/gauss_circle_strategy_checkpoint_round211_2026-09-28.md` | `09806113079e70cd5863c315a9595524eac4270de6afa1f0c2b97e02c7f674f8` |
| `rounds/codex-managed/gc-complete-centered-arithmetic/synthesis.md` | `4d79d586ff57652212573a01bcb456346833b6d9ecfc0c199e296810befa30b5` |
| `rounds/codex-managed/gc-complete-centered-arithmetic/reports/centered_shell_dispersion.md` | `f7165a8d41b9541ff54b53442f238f3d295a8dc944b1ee421a95bc6e3b51af28` |
| `rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_local_arithmetic.md` | `6ab0a4f40d1304a846a166f3e9cf76659107a94457f32cdd1b1d95a6e3a4605e` |
| `rounds/codex-managed/gc-full-goal-radius-source-review/briefs/signed_radius_sources.md` | `e89b6adb7b27a9a21ef0d4baf09ec6ba709e02965656294fd07197d90ac53bf0` |

The radius identities, sector prices and reconstruction in 3.1/3.5 are
inherited from the permitted 213 report and 211 checkpoint, with their
scope rechecked. The pair-weight calculation and exact source B geometry
are this report's analytical application checks. Neither source becomes
an accepted external dependency through this report.

The additional bounded screens were:

- [Chamizo 1999, *Correlated sums of r(n)*](https://www.jstage.jst.go.jp/article/jmath1948/51/1/51_1_237/_article/-char/en): publisher abstract only, then follow-up to the newer exact pair theorem above; no separate theorem audit.
- [Sun, arXiv:1705.00839](https://arxiv.org/abs/1705.00839): abstract screen of a cusp-form coefficient paired with r2, not the fourfold coefficient; no theorem imported.
- [Rydin Myerson 2018](https://discovery.ucl.ac.uk/id/eprint/10044411/): primary repository metadata/abstract screen of general quadratic systems under smoothness and many-variable hypotheses; no theorem imported or claimed applicable.
- [Lott--Magyar--Ponagandla, arXiv:2609.13126v3](https://arxiv.org/abs/2609.13126v3), 18 September 2026: current metadata/abstract screen. Its high-dimensional simplex-density problem is not the literal planar signed radius energy; no theorem audit or quantitative import was made.

The searches also returned unrelated and secondary results; none is
evidence for a mathematical claim here. Bounded screens do not establish
an exhaustive literature result. The current review date does not
require a relevant theorem to have a recent publication date; it
requires checking the actual available versions and their hypotheses.

## 7. Recommended state effect

**Retain** the complete signed gate and the two exact source-interface
failures as strategy evidence. **Reject** a direct pair-correlation
import through an unpriced extra arithmetic weight, and reject the
specified restricted-quadratic import through dimensional padding or
replacement of four equations by one. These rejections are narrow.

**No change** to the authoritative graph, accepted exponents, moment
estimates, M1/M2/GAR obligations, endpoint claims or proof draft.

For the strategy decision, retain (R214) only as a bounded milestone
with the explicit signed arithmetic requirement (3.2). Its proof must
produce an actual complete estimate before finer spectral, local or
geometric subdivisions receive credit. The source checks give no reason
to replace it by pairwise independence, full-size lattice asymptotics
or another absolute certificate. For the full quarter goal, require
either a quantified improvement beyond the certificate limitation in 3.6
or an independent complete high-moment/M1--M2 direction. Designing that
successor belongs to the conductor after 214 closes.

Only this assigned report was written. The task stops here.
