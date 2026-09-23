# Candidate: tangent-character Fejer-commutator self-return obstruction

- Campaign: `m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate`
- Round: 173
- Starting graph: `70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f`
- Candidate status: not accepted until final seam review and State Patch validation

## 1. Result

The exact tangent chart and alternating identity split every stopped parity-
Fejer link into a target-safe bandpass commutator and one actual-symbol
difference remainder. Exact adjoint reindexing sends that difference back to
the original character mode with an adjacent **sum** of bandpass weights:

\[
 \mathcal R_{R,T}
 =\Re\sum(-1)^s\{\beta_{R,T}(r_s)+
                        \beta_{R,T}(r_{s+1})\}G(s).
\]

Consequently the whole-chain remainder target is equivalent, modulo the
target-safe commutator and the one accepted short correction, to K26 itself.
The displayed operator has not produced a smaller theorem. This is a
route-scoped self-return obstruction, not a physical lower bound and not a
disproof of K26.

## 2. Exact statement and hypotheses

Let $J=\sqrt X$, $1\ll L\ll H\le J^{1/2}$,
$R_0=\lceil L\rceil$, and $M=M_L\asymp L^2$. Retain the complete literal
residual opening

\[
 c_N^{\mathrm{rem}}=
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)\lambda_N(d),
 \qquad
 D_L=\sum_N|c_N^{\mathrm{rem}}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\]

On every nonzero incidence, $N=dm\asymp L^2$, $d,m\asymp L$,
$|\lambda_N(d)|\ll X^\eta$, and the active divisor multiplicity is
$X^{O(\eta)}$. The weight retains every canonical selector/no-pair value,
squarefree and coprimality mask, two-adic branch, profile, floor, star,
crossing, endpoint, point value, and zero extension.

For $R<T\le2R$, including the strict final non-doubling link, put

\[
 \beta_{R,T}(r)=
 \begin{cases}
 r(T-R)/(RT),&0<r<R,\\
 1-r/T,&R\le r<T,\\
 0,&r\le0\text{ or }r\ge T.
 \end{cases}
\]

For every opened ordered pair define uniquely

\[
 N=dm,\qquad d'=d+2s,\qquad m'=m+v,
 \qquad r_s=dv+2s(m+v).
\]

Both $s,v\in\mathbb Z$; an even physical gap is equivalent to
$v\in2\mathbb Z$. Define, before evaluating any square root,

\[
 G_{d,m,v}(s)=
 \lambda_{(d+2s)(m+v)}(d+2s)\overline{\lambda_{dm}(d)}
 e\!\left(J\{\sqrt{(d+2s)(m+v)}-\sqrt{dm}\}\right)
\]

when both opened atoms are positive literal incidences, and define it as zero
otherwise. The character is excluded from $G$, because it is extracted as

\[
 \chi_4(d+2s)\chi_4(d)=(-1)^s.
\]

The complete even-gap link is therefore

\[
 \boxed{
 \Delta_{R,T}=2\Re
 \sum_{\substack{d>0\ \mathrm{odd},\ m\ge1\\
                  v\in2\mathbb Z,\ s\in\mathbb Z}}(-1)^s
 \beta_{R,T}(r_s)G_{d,m,v}(s).}
\]

## 3. Proof

The inverse chart is $s=(d'-d)/2$, $v=m'-m$, so multiplicity is one at
the opened-incidence level, including negative $s,v$. Modulo two,
$d'm'-dm\equiv v\pmod2$. The odd--odd branch has $v$ even; in the
squarefree even--even branch $4\mid v$ and $4\mid r_s$. There is no mixed
branch at even gap. The character law follows from
$\chi_4(d+2)=-\chi_4(d)$.

The bandpass is continuous at $0,R,T$ and globally $1/T$-Lipschitz, hence
also $1/R$-Lipschitz. Since

\[
 r_{s+1}-r_s=2m'\asymp L,
\]

the adjacent weight difference is $O(L/R)$. If it is nonzero, the signed
physical gap lies in an interval $-O(L)<r_s<T$ of length $O(R)$. The
complete absolute double opening over the resulting $O(RL^2)$ ordered
physical pairs has weight
$O_\varepsilon(RL^2X^{C_0\eta})$ for a fixed $C_0$. Hence

\[
 |\mathcal C_{R,T}|\ll_\varepsilon L^3X^\varepsilon,
 \qquad
 \sum_j|\mathcal C_{R_j,R_{j+1}}|
 \ll_\varepsilon L^3X^\varepsilon,
\]

after choosing $\eta$ sufficiently small in terms of the requested
$\varepsilon$ and absorbing the $O(\log L)$ links.

For a finitely supported sequence $H$, full-line zero extension gives

\[
 2\sum_s(-1)^sH(s)=\sum_s(-1)^s\{H(s)-H(s+1)\}.
\]

With $H(s)=\beta(r_s)G(s)$, this is exactly

\[
 \Delta_{R,T}=\mathcal C_{R,T}+\mathcal R_{R,T},
\]

where

\[
 \begin{aligned}
 \mathcal C_{R,T}
 &=\Re\sum(-1)^s\{\beta(r_s)-\beta(r_{s+1})\}G(s),\\
 \mathcal R_{R,T}
 &=\Re\sum(-1)^s\beta(r_{s+1})\{G(s)-G(s+1)\}.
 \end{aligned}
\]

Reindexing only the $G(s+1)$ term proves

\[
 \boxed{
 \mathcal R_{R,T}
 =\Re\sum(-1)^s\{\beta(r_s)+\beta(r_{s+1})\}G(s).}
\]

Thus $D_s^*\{(-1)^s\beta(r_{s+1})\}$ is an adjacent sum, and
$\mathcal R_{R,T}=\Delta_{R,T}-\mathcal C_{R,T}$ exactly.

Let $R_{j+1}=\min(2R_j,M_L)$, with repetitions removed. Using the accepted
stopped-chain identity,

\[
 \sum_j\mathcal R_{R_j,R_{j+1}}
 =2(T_{26}+B_{\mathrm{short}})
  -\sum_j\mathcal C_{R_j,R_{j+1}},
 \qquad
 |B_{\mathrm{short}}|\ll_\varepsilon L^3X^\varepsilon.
\]

The Round-173 remainder estimate and K26 are therefore equivalent one-sided
up to target-safe terms, preserving one outer real part and every possible
cross-link cancellation.

## 4. First open step

The first open step is again the complete literal K26 shifted-convolution
estimate. Expanding $G(s)-G(s+1)$ exposes order-one selector, arithmetic-
mask, profile, endpoint, and zero-extension jumps together with the phase
increment

\[
 J\{\sqrt{N_s'+2m'}-\sqrt{N_s'}\}.
\]

Its large real size is not uniform distance from an integer. The
coefficient-uniform positive/absolute closure has available upper scale
$RL^2X^\varepsilon$, reaching $L^4X^\varepsilon$ at a maximal link.
The phase-adapted test attaining the erased-structure scale is nonliteral and
proves no physical lower bound. Moving the difference back to the weight
returns the displayed adjacent-sum identity.

A future proof needs a genuinely new collective actual-symbol shifted-
convolution theorem. The no-go covers only the displayed tangent-character
first-difference placement, its adjoint or tautological second-Abel transfer,
and positivity before an actual-symbol gain. It does not exclude cross-link
cancellation, a nonlocal signed theorem, a coefficient-sensitive positive
theorem after a literal-symbol gain, another tangent mechanism, or K26 itself.

## 5. Controls

Singleton and finite-interval tests reproduce all birth/death terms and the
factor $2$. A phase-adapted abstract $G(s)=(-1)^sg(s)$ makes the remainder
positive with the full adjacent-average carrier, so coefficient-uniform
variation cannot save $L$. This array is nonliteral.

On the retained all-$1\pmod4$ no-pair class, every active
$d,d'\equiv1\pmod4$, hence $s$ is even and missing odd sites make the two
difference jumps add. This is an allowed-support operator control, not a
density estimate, a physical lower bound, or an owner-complete sector.

The arbitrary-divisor examples in the initial statement-only report violate
the repaired literal hypotheses $d,m\asymp L$ or bounded opened weights. They
remain useful erased-structure controls but are not literal counterexamples.
The exact self-return identity does not depend on them.

## 6. Dependencies

Mathematical dependencies are exactly:

- `M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction`;
- `M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction`; and
- `M9-M2-hard-top-t1-residual-maximal-fejer-dyadic-positive-transform-obstruction`.

Candidate evidence consists of the three Round-173 reports, the repaired
statement-only packet and verification, conductor controls, and all final
seam reviews.

## 7. Recommended state effect

Create one `proved_internal` obstruction node named
`M9-M2-hard-top-t1-residual-tangent-fejer-commutator-self-return-obstruction`.
Give it no implication edge and no blocker. Add it only as inconclusive route
evidence and dependency to these two already-open interfaces, without changing
their statuses:

- `M9-M2-top-endpoint-density-discrepancy-energy`; and
- `M9-M2-top-endpoint-signed-cone`.

Do not create a standalone target-safe commutator sector: its complement is
exactly the open remainder. Do not change K26, the complete residual scalar,
any other hard-TOP channel, hard TOP, BAL, UNBAL, M9--M2, either M1 route,
endpoint assembly, M9, either bridge, the quarter theorem, or either exponent
ledger.
