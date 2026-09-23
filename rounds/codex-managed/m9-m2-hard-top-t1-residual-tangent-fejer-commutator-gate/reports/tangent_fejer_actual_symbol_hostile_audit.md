# Hostile audit: tangent-character Fejer commutator

- Campaign: m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate
- Round: 173
- Task: tangent_fejer_actual_symbol_hostile_audit
- Role: barrier/no-go
- Starting graph:
  70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f
- Allocation: 100% analytic/algebraic; 0% numerical

## 1. Result

The tangent-character/Fejer commutator is exact and its bandpass
commutator is target-safe, but its purported actual-symbol difference
remainder **self-returns coefficientwise to the original link**.

More precisely, for every literal stopped-chain link \(R<T\le2R\), put
\(\beta_s=\beta_{R,T}(r_s)\). The proposed split is

\[
 \Delta_{R,T}=\mathcal C_{R,T}+\mathcal R_{R,T},
\tag{173.H1}
\]

with

\[
 \mathcal C_{R,T}
 =\Re\sum(-1)^s(\beta_s-\beta_{s+1})G_s
\tag{173.H2}
\]

and

\[
 \mathcal R_{R,T}
 =\Re\sum(-1)^s\beta_{s+1}(G_s-G_{s+1}).
\tag{173.H3}
\]

Finite reindexing of the second term in (173.H3), with the full literal
zero extension retained, gives the exact identity

\[
 \boxed{
 \mathcal R_{R,T}
 =\Re\sum_s(-1)^s(\beta_s+\beta_{s+1})G_s.}
\tag{173.H4}
\]

Thus the difference has not made the actual symbol smaller. It has merely
replaced the original weight \(2\beta_s\) by the adjacent average
\(\beta_s+\beta_{s+1}\); their difference is exactly the target-safe
commutator (173.H2). In particular,

\[
 \mathcal R_{R,T}=\Delta_{R,T}-\mathcal C_{R,T}.
\tag{173.H5}
\]

On the full stopped chain,

\[
 \boxed{
 \sum_j\mathcal R_{R_j,R_{j+1}}
 =2(T_{26}+B_{\rm short})
  -\sum_j\mathcal C_{R_j,R_{j+1}}.}
\tag{173.H6}
\]

Since \(B_{\rm short}\) and the complete commutator are
\(O_\varepsilon(L^3X^\varepsilon)\), the frozen Round-173 remainder
estimate is equivalent, modulo target-safe terms, to K26 itself. It is not
a smaller analytic gate.

This proves the route-scoped terminal result

\[
 \boxed{\texttt{tangent\_fejer\_actual\_symbol\_commutator\_no\_go}.}
\]

The no-go covers the displayed alternating tangent difference, its positive
variation closure, and any second summation by parts which merely transfers
the same difference back to its weight. It is not a lower bound for the
literal residual scalar and does not disprove K26 or a future genuinely
signed shifted-convolution theorem.

## 2. Exact statement and hypotheses

Let

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad M\asymp L^2,
\]

and retain the complete literal residual coefficient

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {\rm odd}}}
   \chi_4(d)\lambda_N(d).
\tag{173.H7}
\]

The coefficient \(\lambda_N(d)\) includes every selected/no-pair value,
squarefree and coprimality deletion, both two-adic branches, normalization,
profile, floor, star, crossing, hard endpoint, point value, and
zero-extension value. On a nonzero literal atom,

\[
 N=dm\asymp L^2,\qquad d,m\asymp L,\qquad
 |\lambda_N(d)|\ll X^\eta,
\tag{173.H8}
\]

for arbitrarily small fixed \(\eta>0\).

For an ordered opened pair put

\[
 d'=d+2s,\qquad m'=m+v,\qquad
 N=dm,\qquad N_s'=(d+2s)(m+v),
\tag{173.H9}
\]

and

\[
 r_s=N_s'-N=dv+2s(m+v).
\tag{173.H10}
\]

Both \(s\) and \(v\) range over all integers subject only to literal
support. If the physical gap is even, then \(v\) is even, because \(d,d'\)
are odd and

\[
 r_s=d'm'-dm\equiv m'-m=v\pmod2.
\tag{173.H11}
\]

Conversely, \(v\) even makes every \(r_s\) even. The inverse chart is

\[
 s=\frac{d'-d}{2},\qquad v=m'-m,
\tag{173.H12}
\]

so the chart is multiplicity one, including negative \(s,v\). Moreover,

\[
 \chi_4(d')\chi_4(d)
 =\chi_4(d+2s)\chi_4(d)=(-1)^s.
\tag{173.H13}
\]

Define \(G_{d,m,v}(s)\) to be

\[
 \lambda_{N_s'}(d+2s)\overline{\lambda_{dm}(d)}
 e\!\left(J(\sqrt{N_s'}-\sqrt{dm})\right)
\tag{173.H14}
\]

when both opened atoms are on positive literal support, and zero otherwise.
This piecewise definition never evaluates a square root off positive
support.

For \(R<T\le2R\), including the strict final non-doubling link, define

\[
 \beta_{R,T}(r)=
 \begin{cases}
  r(T-R)/(RT),&0<r<R,\\
  1-r/T,&R\le r<T,\\
  0,&r\le0\text{ or }r\ge T.
 \end{cases}
\tag{173.H15}
\]

The exact opened link is

\[
 \Delta_{R,T}
 =2\Re\sum_{\substack{d\ {\rm odd},\,m\ge1\\
                       v\in2\mathbb Z,\,s\in\mathbb Z}}
 (-1)^s\beta_{R,T}(r_s)G_{d,m,v}(s).
\tag{173.H16}
\]

All sums below use this full domain. The shorthand \(G_s,\beta_s\) never
licenses a fixed-shift, fixed-row, selector-class, parity-class, or
endpoint modulus.

The stopped chain is

\[
 R_{j+1}=\min(2R_j,M),
\]

with repetitions removed and final value \(M\). The accepted identity is

\[
 T_{26}
 =\frac12\sum_j\Delta_{R_j,R_{j+1}}-B_{\rm short},
\qquad
 |B_{\rm short}|\ll_\varepsilon L^3X^\varepsilon.
\tag{173.H17}
\]

## 3. Proof or derivation

### 3.1 Chart, parity, and atom reconstruction

Given a literal opened atom \((N,d;N',d')\), the cofactors are uniquely
\(m=N/d\) and \(m'=N'/d'\). Since both character-bearing divisors are odd,
\(d'-d=2s\) for one integer \(s\), and \(v=m'-m\) is unique. Direct
expansion proves (173.H10), while reduction modulo two proves (173.H11).
Equations (173.H12) recover the original tuple, so no atom is duplicated or
lost. Literal zero extension handles negative \(s,v\), support births and
deaths, and nonpositive candidate products without an extra boundary term.

Even gaps force the two products to have the same parity. In the odd--odd
branch, \(m,m'\) are odd and \(v\) is even. In the squarefree even--even
branch, write \(m=2u\), \(m'=2u'\) with \(u,u'\) odd. Then
\(v=2(u'-u)\) and in fact \(4\mid v\) and \(4\mid r_s\). The character
law (173.H13) is unchanged because the character remains on the odd
divisors \(d,d'\). There is no mixed-parity branch at an even gap.

### 3.2 Bandpass cusps and the commutator bound

The two slopes of (173.H15) are

\[
 \frac{T-R}{RT}\quad\text{and}\quad-\frac1T.
\]

Their magnitudes are at most \(1/R\). At the interior cusp,

\[
 \frac{R(T-R)}{RT}=\frac{T-R}{T}=1-\frac RT,
\]

so the two pieces agree at \(r=R\). The function also agrees with its zero
extension at \(r=0,T\). Therefore

\[
 |\beta_{R,T}(x)-\beta_{R,T}(y)|
 \le \frac{|x-y|}{R}
\tag{173.H18}
\]

for all real \(x,y\), including every cusp and the terminal non-doubling
link.

For a nonzero \(G_s\), \(m'=m+v\asymp L\), and

\[
 r_{s+1}-r_s=2m'\asymp L.
\tag{173.H19}
\]

Hence

\[
 |\beta_s-\beta_{s+1}|\ll\frac LR.
\tag{173.H20}
\]

If this difference is nonzero, at least one of \(r_s,r_{s+1}\) lies in
\((0,T)\); by (173.H19), the other lies within \(O(L)\) of that interval.
Since \(R\ge R_0\asymp L\), only \(O(R)\) possible product gaps occur.
For each gap there are \(O(L^2)\) product sites and
\(X^{O(\eta)}\) pairs of divisor incidences. Thus

\[
 \sum_{\beta_s\ne\beta_{s+1}}|G_s|
 \ll_\varepsilon RL^2X^\varepsilon.
\tag{173.H21}
\]

Combining (173.H20)--(173.H21) proves

\[
 |\mathcal C_{R,T}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{173.H22}
\]

The \(O(\log L)\) links are absorbed by rebudgeting epsilon:

\[
 \sum_j|\mathcal C_{R_j,R_{j+1}}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{173.H23}
\]

This count includes negative starting gaps, \(r=0,R,T\), both slopes,
support jumps, and the strict final link. It uses no cancellation and no
positive norm over an omitted owner.

### 3.3 Exact alternating split

For every finitely supported sequence \(H_s\), zero extension and the shift
\(t=s+1\) give

\[
 \sum_s(-1)^sH_{s+1}
 =-\sum_t(-1)^tH_t.
\]

Therefore

\[
 2\sum_s(-1)^sH_s
 =\sum_s(-1)^s(H_s-H_{s+1}).
\tag{173.H24}
\]

Taking \(H_s=\beta_sG_s\), expanding the difference, and taking the real
part proves (173.H1)--(173.H3), with exactly the constants displayed in the
campaign.

### 3.4 Adjoint reindexing and exact self-return

Now reindex the second half of the proposed remainder itself:

\[
\begin{aligned}
 \mathcal R_{R,T}
 &=\Re\left\{
 \sum_s(-1)^s\beta_{s+1}G_s
 -\sum_s(-1)^s\beta_{s+1}G_{s+1}\right\}\\
 &=\Re\left\{
 \sum_s(-1)^s\beta_{s+1}G_s
 +\sum_s(-1)^s\beta_sG_s\right\}.
\end{aligned}
\tag{173.H25}
\]

This is (173.H4). It is an identity for the complete complex literal atom;
the selector, squarefree masks, profiles, endpoints, and phase can jump
arbitrarily without affecting it. In operator language, the adjoint of the
forward difference sends the alternating shifted weight to

\[
 D_s^*\{(-1)^s\beta_{s+1}\}
 =(-1)^s(\beta_s+\beta_{s+1}),
\tag{173.H26}
\]

an adjacent **sum**, not a small adjacent difference. Thus moving the
difference off the actual symbol restores the full carrier.

Equations (173.H2), (173.H4), and (173.H16) give

\[
 \mathcal C_{R,T}+\mathcal R_{R,T}
 =\Re\sum_s(-1)^s(2\beta_s)G_s
 =\Delta_{R,T}.
\tag{173.H27}
\]

The average kernel in (173.H4) is nonnegative before the character sign and
has the same scale as \(2\beta_s\). By (173.H20),

\[
 \beta_s+\beta_{s+1}
 =2\beta_s+O(L/R),
\tag{173.H28}
\]

and the total \(O(L/R)\) contribution is precisely the target-safe
commutator. Positive treatment of (173.H4) therefore has the original
\(RL^2X^\varepsilon\) capacity, reaching \(L^4X^\varepsilon\) at
\(R\asymp L^2\).

### 3.5 Stopped-chain equivalence

Sum (173.H5) over the complete stopped chain and insert (173.H17):

\[
\begin{aligned}
 \sum_j\mathcal R_{R_j,R_{j+1}}
 &=\sum_j\Delta_{R_j,R_{j+1}}
   -\sum_j\mathcal C_{R_j,R_{j+1}}\\
 &=2(T_{26}+B_{\rm short})
   -\sum_j\mathcal C_{R_j,R_{j+1}}.
\end{aligned}
\tag{173.H29}
\]

This is (173.H6). Conversely,

\[
 T_{26}
 =\frac12\sum_j\mathcal R_{R_j,R_{j+1}}
  +\frac12\sum_j\mathcal C_{R_j,R_{j+1}}
  -B_{\rm short}.
\tag{173.H30}
\]

Because the last two terms are target-safe in absolute value, a one-sided
target bound for the Round-173 remainder is equivalent to a one-sided
target bound for K26. Cross-link cancellation is preserved in both
directions, and the short correction is paid exactly once. The selected
operator has exposed no smaller theorem.

### 3.6 Actual no-pair parity concentration

The abstract self-return has a literal warning. Suppose both products are
no-pair rows whose odd prime factors are all \(1\pmod4\). Then every active
odd divisor satisfies \(d\equiv d'\equiv1\pmod4\), so

\[
 s=\frac{d'-d}{2}\equiv0\pmod2.
\tag{173.H31}
\]

On this subfamily \(G_s=0\) for odd \(s\), and the apparent tangent
character is identically \(+1\) on literal sites. For any even-supported
sequence,

\[
 \mathcal R_{R,T}
 =\Re\sum_{\substack{s\in\mathbb Z\\2\mid s}}
 \{\beta_s+\beta_{s+1}\}G_s,
\tag{173.H32}
\]

while

\[
 \mathcal C_{R,T}
 =\Re\sum_{2\mid s}(\beta_s-\beta_{s+1})G_s.
\tag{173.H33}
\]

Thus the remainder retains the full positive adjacent-average weight, and
only the small bandpass difference enters the commutator. Equivalently,
\(D_sG\) creates one order-one jump on each side of every occupied
even site; it does not create cancellation.

This is an exact allowed-support control, not a lower bound or density
theorem for the physical scalar. It rules out deriving the missing factor
from tangent alternation, row sign mass, parity support, or positive
variation alone.

### 3.7 Phase and support jumps

Inside \(D_sG\), the second product changes by

\[
 N_{s+1}'-N_s'=2m'\asymp L,
\]

and the phase ratio contains

\[
 J\{\sqrt{N_s'+2m'}-\sqrt{N_s'}\}.
\tag{173.H34}
\]

Its real size supplies no uniform distance from an integer. Selector,
squarefree/coprimality, profile, and endpoint values can also jump by order
one. Taking their absolute variations gives the \(L^4\) capacity.

More importantly, (173.H25) shows that no separate estimate of these jumps
is created by the commutator: summation by parts moves every jump back to
the original \(G_s\) with the full average kernel. A second Abel step is
therefore already an exact shift tautology. No forced ramp need be invoked;
the route self-returns before a new uncharactered primitive appears.

## 4. First doubtful or unproved step

After the exact self-return, the first unproved statement is again the
complete K26 scalar, equivalently either side of (173.H29)--(173.H30).
Nothing in the tangent difference controls it.

A future proof may still estimate the complete signed family by a genuinely
new theorem which couples

\[
 (d,m,d',m'),\quad d'm'-dm,\quad
 \chi_4(d)\chi_4(d'),\quad
 \lambda_{d'm'}(d')\overline{\lambda_{dm}(d)},
\quad e(J(\sqrt{d'm'}-\sqrt{dm}))
\]

before every modulus. Such a theorem must fail for phase-adapted abstract
arrays and must retain selected/no-pair rows, both parity branches, all
holes and endpoints, and the full stopped chain. But calling that theorem a
bound for (173.H3) does not make it narrower than K26, because (173.H29) is
an exact equivalence.

The first doubtful step in any continuation of the displayed operator is
therefore not a cusp, endpoint, or normalization issue. It is the original
actual-symbol shifted-convolution estimate. The tangent commutator supplies
no independent hypothesis with which to prove it.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Literal residual domain | **PASS.** \(G_s\) is defined only when both atoms are positive and literal; all other values are zero. |
| Multiplicity-one tangent chart | **PASS.** Equations (173.H9)--(173.H12) give an exact inverse, including negative \(s,v\). |
| Even-gap parity and character | **PASS.** \(v\) is even and \(\chi_4(d')\chi_4(d)=(-1)^s\). |
| Odd--odd branch | **PASS.** \(m,m'\) are odd and the chart is unchanged. |
| Squarefree even--even branch | **PASS.** \(4\mid v,r\); the same character law holds and supplies no extra sign. |
| Finite alternating identity | **PASS.** Zero extension makes (173.H24) exact on intervals, singletons, and endpoint data. |
| Bandpass slopes and cusp \(r=R\) | **PASS.** Both slopes are at most \(1/R\), and the two values agree at the cusp. |
| Zero and terminal endpoints | **PASS.** The bandpass meets zero continuously at \(0,T\), including a strict final link. |
| Complete commutator power | **PASS.** Equations (173.H20)--(173.H23) give \(L^3X^\varepsilon\). |
| Constant \(G\) on a finite interval | **PASS with endpoint correction.** \(D_sG\) vanishes in the interior but retains the two zero-extension boundary jumps; (173.H4) gives the same endpoint result. |
| Phase-adapted \(G_s=(-1)^sA\) | **FAILS as required for a generic theorem.** In the interior, \((-1)^sD_sG=2A\), so the remainder is a positive average-kernel sum of full capacity. |
| Positive no-pair one-parity support | **FAILS as a saving.** Equations (173.H31)--(173.H33) show exact parity concentration and adjacent-average self-return. |
| Selected rows and large toggles | **RETAINED.** The tangent identity neither repairs nor deletes the accepted fixed-product leakage; all selector jumps remain in \(G_s\). |
| Squarefree/coprimality holes | **RETAINED.** They are deletion masks; their jumps self-return through (173.H25). |
| Profile, point-value, and endpoint jumps | **RETAINED.** No smoothing or boundary omission occurs. |
| Large real phase increment | **NO SAVING.** Equation (173.H34) gives no modulo-one separation, and reindexing restores the phase exactly. |
| Whole stopped chain | **PASS algebraically.** Equation (173.H29) retains one outer real part and cross-link cancellation. |
| Short correction | **PASS.** It appears exactly once in (173.H29)--(173.H30). |
| Factor \(L\) before positivity | **FAILS for the remainder.** Only the commutator difference has \(L/R\); the remainder has the adjacent sum and \(L^4\) positive capacity. |
| Tautology / second Abel | **FAILS terminally.** The adjoint reindexing (173.H25) returns the original carrier before any new ramp is useful. |
| One-site normalization | **PASS.** The complete physical Fejer increment still vanishes after all compensating terms recombine; no isolated positive diagonal is inferred. |
| Owner scope | **PASS.** Only K26 and its residual connector are touched; no parent or exponent is promoted. |

The \(L^4\) statements above are available positive or adversarial
capacities, not literal physical lower bounds. No numerical experiment or
external theorem is used.

## 6. Dependencies and exact artifacts used

Accepted mathematical dependencies:

1. M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction;
2. M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction;
3. M9-M2-hard-top-t1-residual-maximal-fejer-dyadic-positive-transform-obstruction;
4. M9-M2-hard-top-t1-character-poisson-product-collar-obstruction, only
   through the inherited positive-route barrier; and
5. M9-M2-balanced-two-defect-commutator-ramp-obstruction, only as a
   nontransfer and tautology control.

Exact artifacts used:

- protocol.md;
- state/proof_obligations.yml at the stated graph hash;
- state/active_campaign.yml;
- strategy/round173_m2_hard_top_t1_residual_tangent_fejer_commutator_strategy.md;
- strategy/round173_selection/k26_actual_symbol_mechanism_audit.md;
- strategy/round173_selection/hostile_round173_selection_audit.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate/barrier_packet.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md; and
- proofs/kernels/m9_m2_balanced_two_defect_commutator_ramp_obstruction.md.

The report uses no sibling Round-173 report, web source, or computation.
The only new deductions are the full chart audit, cusp/incidence audit,
adjoint identity (173.H25), stopped-chain equivalence (173.H29), and
one-parity self-return (173.H31)--(173.H33).

## 7. Recommended state effect

Recommend promotion of one proved-internal, route-scoped obstruction:

**M9-M2-hard-top-t1-residual-tangent-fejer-commutator-self-return-obstruction.**

Its exact content should be:

1. the tangent chart, parity law, finite alternating identity, and
   bandpass commutator are valid;
2. the full commutator is
   \(O_\varepsilon(L^3X^\varepsilon)\);
3. the actual-symbol difference remainder equals the original link minus
   that commutator, and its stopped-chain target is equivalent to K26 modulo
   the one short correction;
4. on all-\(1\pmod4\) no-pair parity support, the remainder visibly retains
   the full adjacent-average carrier; and
5. positive variation, multiplier normalization, and a second Abel transfer
   do not supply the missing factor \(L\).

Retain K26, the complete residual \(t=1\) scalar, every other \(t=1\) and
few-point hard-TOP channel, hard TOP, critical and remaining-label BAL,
UNBAL, M9--M2, both direct M1 parents or GAR, endpoint uniformity, M9, both
bridges, and the Gauss-circle quarter target as open. Do not create a
standalone commutator-sector owner: its complement is exactly the open
remainder. Do not change either exponent ledger.

The recommended Round-173 terminal label is

\[
 \boxed{\texttt{tangent\_fejer\_actual\_symbol\_commutator\_no\_go}.}
\]
