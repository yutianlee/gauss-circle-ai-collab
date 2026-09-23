# M9--M2 hard-TOP residual tangent-Fejer commutator self-return obstruction

- Campaign: `m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate`
- Round: 173
- Starting graph: `70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f`
- Scope: one route-specific internal obstruction; K26 remains open

## 1. Exact setting

Let $J=\sqrt X$, $1\ll L\ll H\le J^{1/2}$,
$R_0=\lceil L\rceil$, and let $M=M_L\asymp L^2$ be the exact containing-
interval length in the accepted residual Fejer reduction. Retain

\[
 c_N^{\mathrm{rem}}
 =\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
  \chi_4(d)\lambda_N(d),
 \qquad
 D_L=\sum_N|c_N^{\mathrm{rem}}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{173.K1}
\]

On every nonzero opened incidence, $N=dm\asymp L^2$, $d,m\asymp L$,
$|\lambda_N(d)|\ll X^\eta$, and the divisor-opening multiplicity is
$X^{O(\eta)}$. The literal weight includes every selected/no-pair value,
squarefree and coprimality mask, two-adic branch, profile, floor, star,
crossing, endpoint, point value, and zero-extension value.

For $R<T\le2R$, define the exact one-sided Fejer link weight

\[
 \beta_{R,T}(r)=
 \begin{cases}
 r(T-R)/(RT),&0<r<R,\\
 1-r/T,&R\le r<T,\\
 0,&r\le0\text{ or }r\ge T.
 \end{cases}
\tag{173.K2}
\]

This definition also governs the strict final non-doubling link.

## 2. Tangent chart and exact physical link

For an ordered pair of opened incidences put

\[
 N=dm,\qquad d'=d+2s,\qquad m'=m+v,
 \qquad N_s'=(d+2s)(m+v),
 \qquad r_s=N_s'-N=dv+2s(m+v).
\tag{173.K3}
\]

The inverse is $s=(d'-d)/2$, $v=m'-m$, so this is a multiplicity-one chart
at the opened-incidence level. Negative $s,v$ are retained; literal support
requires $d+2s>0$, $m+v>0$, and both atoms to lie in their exact positive
domains. Since $d,d'$ are odd,

\[
 r_s=d'm'-dm\equiv v\pmod2,
 \qquad
 \chi_4(d+2s)\chi_4(d)=(-1)^s.
\tag{173.K4}
\]

Thus even physical gaps are equivalent to $v\in2\mathbb Z$. The odd--odd
branch has $v$ even; the squarefree even--even branch has
$4\mid v$ and $4\mid r_s$; there is no mixed branch at even gap.

Define, before evaluating a square root,

\[
 G_{d,m,v}(s)=
 \lambda_{(d+2s)(m+v)}(d+2s)\overline{\lambda_{dm}(d)}
 e\!\left(J\{\sqrt{(d+2s)(m+v)}-\sqrt{dm}\}\right)
\tag{173.K5}
\]

when both atoms are positive literal incidences, and zero otherwise. The
character is excluded from $G$. The complete even-gap link is exactly

\[
 \Delta_{R,T}=2\Re
 \sum_{\substack{d>0\ \mathrm{odd},\ m\ge1\\
                  v\in2\mathbb Z,\ s\in\mathbb Z}}
 (-1)^s\beta_{R,T}(r_s)G_{d,m,v}(s).
\tag{173.K6}
\]

## 3. Target-safe bandpass commutator

The weight in (173.K2) is continuous at $0,R,T$. Its two nonzero slopes are

\[
 \frac{T-R}{RT}=\frac1R-\frac1T,
 \qquad -\frac1T,
\]

so it is globally $1/T$-Lipschitz, hence $1/R$-Lipschitz. Along a tangent
line,

\[
 r_{s+1}-r_s=2m'\asymp L
 \qquad\text{whenever }G_{d,m,v}(s)\ne0.
\tag{173.K7}
\]

Therefore

\[
 |\beta_{R,T}(r_s)-\beta_{R,T}(r_{s+1})|
 \ll L/R.
\tag{173.K8}
\]

If this difference is nonzero and $G_{d,m,v}(s)\ne0$, then
$-O(L)<r_s<T$, an interval of length $O(R)$ because
$R\ge R_0\asymp L$. There are $O(L^2)$ base product sites,
so the complete weighted double opening over the relevant atoms is
$O(RL^2X^{C_0\eta})$ for a fixed $C_0$. Hence the complete commutator

\[
\mathcal C_{R,T}
:=\Re\sum(-1)^s
 \{\beta_{R,T}(r_s)-\beta_{R,T}(r_{s+1})\}G(s)
\tag{173.K9}
\]

Here and in (173.K11)--(173.K14), every unqualified sum uses exactly the
complete domain in (173.K6), with the same positive-literal zero extension.

satisfies

\[
 |\mathcal C_{R,T}|\ll_\varepsilon L^3X^\varepsilon,
 \qquad
 \sum_j|\mathcal C_{R_j,R_{j+1}}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{173.K10}
\]

Here $\eta$ is chosen sufficiently small in terms of the requested
$\varepsilon$, and the $O(\log L)$ links are absorbed into
$X^\varepsilon$.

## 4. Alternating split and adjoint self-return

For every finitely supported sequence $H$ on the full zero-extended integer
line,

\[
 2\sum_s(-1)^sH(s)=\sum_s(-1)^s\{H(s)-H(s+1)\}.
\tag{173.K11}
\]

Taking $H(s)=\beta(r_s)G(s)$ gives

\[
 \Delta_{R,T}=\mathcal C_{R,T}+\mathcal R_{R,T},
\tag{173.K12}
\]

where

\[
 \mathcal R_{R,T}
 :=\Re\sum(-1)^s\beta(r_{s+1})\{G(s)-G(s+1)\}.
\tag{173.K13}
\]

Reindexing only the $G(s+1)$ term, with every support birth and death retained,
gives

\[
 \boxed{
 \mathcal R_{R,T}
 =\Re\sum(-1)^s\{\beta(r_s)+\beta(r_{s+1})\}G(s).}
\tag{173.K14}
\]

Thus the adjoint of the forward difference at character frequency $\pi$
produces an adjacent sum, not a small difference, and

\[
 \mathcal R_{R,T}=\Delta_{R,T}-\mathcal C_{R,T}.
\tag{173.K15}
\]

Let $R_{j+1}=\min(2R_j,M_L)$, with repetitions removed. The accepted stopped-
chain identity is

\[
 T_{26}=\frac12\sum_j\Delta_{R_j,R_{j+1}}-B_{\mathrm{short}},
 \qquad
 |B_{\mathrm{short}}|\ll_\varepsilon L^3X^\varepsilon.
\tag{173.K16}
\]

Consequently

\[
 \boxed{
 \sum_j\mathcal R_{R_j,R_{j+1}}
 =2(T_{26}+B_{\mathrm{short}})
  -\sum_j\mathcal C_{R_j,R_{j+1}}.}
\tag{173.K17}
\]

Since the last two terms are target-safe in absolute value, the one-sided
whole-chain remainder bound and the one-sided K26 bound are equivalent at
target strength. Cross-link cancellation remains available in both directions,
and the short correction is paid exactly once.

## 5. Restored power and false controls

The adjacent sum in (173.K14) has no $L/R$ multiplier. Its coefficient-
uniform positive or absolute closure has available upper scale

\[
 RL^2X^\varepsilon,
\tag{173.K18}
\]

which reaches $L^4X^\varepsilon$ at a maximal link. A phase-adapted abstract
array $G(s)=(-1)^sg(s)$, $g(s)\ge0$, makes (173.K14) a positive adjacent-
average sum. This is a nonliteral erased-structure falsifier and proves no
physical lower bound.

There is also an exact literal-support warning. If both products are no-pair
rows whose odd prime factors are all $1\pmod4$, then every active
$d,d'\equiv1\pmod4$, so $s$ is even. Missing odd sites make the two births
and deaths in $G(s)-G(s+1)$ add, and (173.K14) retains the full adjacent-
average carrier. This is not a density theorem, a physical lower bound, or an
owner-complete strict sector.

Expanding the difference exposes order-one selector, squarefree/coprimality,
profile, endpoint, point-value, and zero-extension jumps. Its phase ratio
contains

\[
 J\{\sqrt{N_s'+2m'}-\sqrt{N_s'}\},
\tag{173.K19}
\]

whose large real size gives no uniform distance from an integer. A second Abel
transfer moves the difference back to (173.K14) and is an exact shift
tautology.

The arbitrary single-divisor and cancelling-opening examples from the initial
blind report violate the repaired literal hypotheses $d,m\asymp L$ or bounded
opened weights. They remain useful false controls but are not literal
counterexamples.

## 6. Obstruction scope and first open step

The first open step is again the complete literal K26 signed stopped-chain
shifted-convolution theorem. The tangent first-difference notation has not
created a smaller analytic object.

The no-go covers only:

1. the displayed tangent-character first-difference placement;
2. its adjoint or a second Abel step that merely transfers the same difference
   back to the bandpass; and
3. coefficient-uniform positivity or absolute variation before an actual-
   symbol gain.

It does not exclude cross-link cancellation, a nonlocal signed theorem, a
coefficient-sensitive positive theorem after a literal-symbol gain, another
tangent mechanism, or K26 itself.

## 7. Proof-state boundary

The durable result is one proved-internal obstruction:

`M9-M2-hard-top-t1-residual-tangent-fejer-commutator-self-return-obstruction`.

Its mathematical dependencies are exactly the accepted Round-164 residual
transport reduction, Round-165 parity/gcd/scale reduction, and Round-172
maximal-Fejer positive-transform obstruction. It has no implication edge and
no blocker.

The target-safe commutator is not a standalone owner: its complement is the
open remainder, exactly equivalent to K26 up to target-safe terms. Add this
obstruction only as inconclusive route evidence to
`M9-M2-top-endpoint-density-discrepancy-energy` and
`M9-M2-top-endpoint-signed-cone`, with no status change.

K26, the complete residual scalar, all other hard-TOP channels, hard TOP, BAL,
UNBAL, M9--M2, both M1 routes, endpoint assembly, M9, both bridges, the quarter
theorem, and both exponent ledgers remain unchanged.
