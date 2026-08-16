# Round 85 analytic report: hybrid large-difference attack

Campaign: `m9-m1-large-dual-difference-joint-dispersion`
Task: `hybrid_large_difference_attack`
Role: analytic discovery
Starting graph SHA-256:
`942453c8d45068875932507e8ca84ed87bcb2187ee141029a27eb0c0642bf60f`

## 1. Result

No whole-offset \(B^{-1/2}\), or any fixed \(B^{-\delta}\), is proved.
There is nevertheless a rigorous joint physical/dual reduction and a
new target-safe deletion at the *outer difference edge*.

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B=C/T,
\]

and fix a local class and orientation as in the Round-85 packet. After
removing the literal \(d=0\) term and the already accepted range
\(0<|d|\leq D_0=\lfloor J^{17/30}\rfloor\), write the active-sign
stationary interval as

\[
 \mathscr N_b=[N_b^-,N_b^+]\cap\mathbb Z,
 \qquad \Delta_b=N_b^+-N_b^-\asymp Q^2.                 \tag{1.1}
\]

The endpoints in (1.1) are the outer endpoints furnished by the exact
support of the smooth principal \(c\)-symbol under
\(m=A_{\kappa,b}gM/c^2\). For every fixed
\(0<\delta<4/5\), set

\[
 E_\delta=\lfloor Q^2J^{-\delta}\rfloor.                \tag{1.2}
\]

Then, with constants allowed to depend on \(\delta\), the complete
large-difference contribution with

\[
 |d|\geq \Delta_b-E_\delta                              \tag{1.3}
\]

is \(O_{\varepsilon,\delta}(X^\varepsilon J^2/T)\), uniformly for
\(J^{13/18}<C\leq J^{3/4}\). This includes both outer collars, every
\(|d|>\Delta_b\), all terms containing an entry/exit, stationary
remainder, or nonstationary Fourier tail, and both signs of \(d\).

Consequently the exact new survivor is

\[
 \boxed{
 \mathfrak Y_{\mathrm{int},\delta}^{(\kappa,k)}
 ={1\over M^2}\sum_{b\asymp B}
 \sum_{D_0<|d|<\Delta_b-E_\delta}\sum_{n\in\mathbb Z}
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)},}                \tag{1.4}
\]

where \(M=M_{\kappa,b}\) inside the \(b\)-sum. More precisely,

\[
 \mathfrak Y_{>D_0}^{(\kappa,k)}
 =\mathfrak Y_{\mathrm{int},\delta}^{(\kappa,k)}
 +O_{\varepsilon,\delta}\!\left(X^\varepsilon{J^2\over T}\right).
                                                                  \tag{1.5}
\]

There is a useful derivative-free benchmark. Taking

\[
 E=J^{13/20}=Q^2J^{-3/20}                               \tag{1.6}
\]

already proves (1.3)--(1.5) using only the stationary supremum bound;
the arbitrary fixed \(\delta>0\) version uses the flatness to every
fixed order of the actual compactly supported \(C^\infty\) principal
symbol. The pointwise-small raw Farey transition is not used.

The inherited physical-row saving is not exchanged for this deletion.
The exact joint time-frequency identity below retains
\(TQ^{-5/24}\) per physical row, hence \(Q^{-5/12}\) in the energy.
In particular the new survivor still has the baseline

\[
 |\mathfrak Y_{\mathrm{int},\delta}^{(\kappa,k)}|
 \ll_\varepsilon X^\varepsilon
 \left({C^3\over TQ^{5/12}}+{J^2\over T}\right).        \tag{1.7}
\]

The support-edge deletion is therefore a strict reduction preserving
both earlier gains, not a new conductor range.

## 2. Exact statement and hypotheses

Assume

\[
 J^{13/18}<C\leq J^{3/4},\qquad B=C/T,
\]

and fix one transition-flattened smooth nonaxial principal component,
one compatible nonzero pair \(k=\rho\sigma>0\), one alias, and one
endpoint orientation. For

\[
 (g,M,K)\in
 \{(1,4b,k),(2,2b,2[k\bar4]_b),(4,b,[k\bar4]_b)\},      \tag{2.1}
\]

one has \(gM=4b\), \(M\asymp B\), and \((K,M)=O_k(1)\). Put

\[
 A_{M,K,d}(n)=S(n+d,K;M)\overline{S(n,K;M)}-c_M(d).     \tag{2.2}
\]

The exact normalization and arithmetic facts used are

\[
 {1\over M^2}\sum_{r\bmod M}|A_{M,K,d}(r)|\leq2,
 \qquad \sum_{r\bmod M}A_{M,K,d}(r)=0,                  \tag{2.3}
\]

for every integer \(d\), together with the elementary pointwise bound

\[
 |A_{M,K,d}(n)|\leq M^2+M\leq2M^2.                     \tag{2.4}
\]

No pointwise square-root bound for a prime-power Fourier mode is used.

For orientation \(\eta\in\{1,-1\}\), write \(m=\eta n>0\). The
accepted stationary phase is

\[
 -\eta\lambda_b\sqrt m,
 \qquad \lambda_b=\sqrt X+{\sqrt{\kappa k}\over b},     \tag{2.5}
\]

and the stationary size and large parameter are

\[
 H={C\sqrt T\over J}={C\over\sqrt{JQ}},
 \qquad \Lambda\asymp JQ.                              \tag{2.6}
\]

For the large-\(d\) argument it is convenient to put the full-Gaussian
leading term in \(P_{b,\eta}\) and everything else in \(E_{b,\eta}\):

\[
 I_{b,\eta}(n)=P_{b,\eta}(n)+E_{b,\eta}(n).             \tag{2.7}
\]

Thus, on the active sign,

\[
 P_{b,\eta}(\eta m)
 =e(-\eta\lambda_b\sqrt m)e(-\eta/8)
 \Delta_{b,m}V_b(c_{b,m}),
 \quad c_{b,m}=\sqrt{A_{\kappa,b}gM/m},                 \tag{2.8}
\]

and \(P=0\) when the saddle is outside the exact support of \(V_b\).
The complete incomplete-Gaussian entry and exit collars, the Morse
remainder, and all wrong-sign and exterior terms belong to \(E\).
The accepted smooth extension and the same saddle-overlap count as in
Round 84 give the global, all-frequency bounds

\[
 \|P_{b,\eta}\|_{\ell^1(\mathbb Z)}
 \ll_\varepsilon X^\varepsilon H Q^2,
 \qquad
 \|E_{b,\eta}\|_{\ell^1(\mathbb Z)}
 \ll_\varepsilon X^\varepsilon {HQ^2\over\sqrt\Lambda}
 \asymp X^\varepsilon M.                               \tag{2.9}
\]

The last equivalence is the exact scale identity

\[
 {HQ^2\over\sqrt\Lambda}
 \asymp {CQ^2\over JQ}={C\over T}=B\asymp M.            \tag{2.10}
\]

Finally, compact \(C^\infty\) support with the accepted normalized
derivatives implies, for each fixed integer \(N\geq0\),

\[
 |P_{b,\eta}(\eta m)|
 \ll_{N,\varepsilon}X^\varepsilon H
 \left({\operatorname {dist}(m,\{N_b^-,N_b^+\})+1
              \over Q^2}\right)^N                      \tag{2.11}
\]

whenever \(m\) is in a fixed outer collar of either endpoint. This is
flatness of the actual smooth principal symbol under the monotone saddle
map. It is not asserted for the separately owned raw Farey transition.

## 3. Proof or derivation

### 3.1 Exact joint physical/dual identity and the row factor

In the \(x=c/g\) coordinate let

\[
 I_b(n)=\int_{\mathbb R}F_b(t)e(-nt/M)\,dt
\]

and, for \(x\bmod M\) with \((x,M)=1\), define the continuously shifted
physical row

\[
 \mathcal R_{b,x}(\theta)
 =\sum_{\ell\in\mathbb Z}F_b(x+M(\ell+\theta)),
 \qquad 0\leq\theta<1.                                  \tag{3.1}
\]

Poisson summation gives

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_{n\in\mathbb Z}I_b(n)e_M(nx)e(n\theta).
                                                                  \tag{3.2}
\]

With \(u_b(x)=e_M(K\bar x)\), put

\[
 \mathcal S_b(\theta)=\sum_{x\bmod M}^{*}
 u_b(x)\mathcal R_{b,x}(\theta)
\]

and

\[
 \mathcal G_b(\theta)=|\mathcal S_b(\theta)|^2
 -\sum_{x\bmod M}^{*}|\mathcal R_{b,x}(\theta)|^2.      \tag{3.3}
\]

Opening (3.2) and using finite orthogonality yields the exact identity

\[
 \boxed{
 \mathcal G_b(\theta)
 ={1\over M^2}\sum_{d\in\mathbb Z}\sum_{n\in\mathbb Z}
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}e(d\theta).}      \tag{3.4}
\]

The subtraction in (3.3) is exactly \(c_M(d)\); it is not an
approximate diagonal. Formula (3.4) is valid in all three rows of
(2.1). The reflected endpoint is its conjugate reflection.

The reciprocal-row estimate is uniform under the real translation in
(3.1), because it is the same proper-subinterval reciprocal phase with
the same BV symbol. Hence

\[
 |\mathcal R_{b,x}(\theta)|
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.              \tag{3.5}
\]

For a finite difference multiplier \(w(d)\), let

\[
 K_w(\theta)=\sum_dw(d)e(-d\theta).
\]

Then (3.4) gives

\[
 \sum_dw(d){1\over M^2}\sum_n
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}
 =\int_0^1\mathcal G_b(\theta)K_w(\theta)\,d\theta.      \tag{3.6}
\]

Using (3.5), \(\varphi(M)\leq M\), \(M\asymp B\), and then summing
\(b\asymp B\), (3.6) gives

\[
 \ll_\varepsilon X^\varepsilon\|K_w\|_1
 B^3T^2Q^{-5/12}
 =X^\varepsilon\|K_w\|_1{C^3\over TQ^{5/12}}.           \tag{3.7}
\]

Thus the physical reciprocal-row gain survives exactly. However
\(\|K_w\|_1\geq|w(d_*)|\) for every coefficient \(d_*\), so a sharp or
smooth projection with a unit plateau cannot obtain \(B^{-\delta}\)
from (3.5) and Fourier projection alone. A sharp interval costs at
most the familiar logarithm, which is absorbed by \(X^\varepsilon\),
but gives no power. This is a route-specific no-go: it does not rule
out cancellation in the actual joint \((b,x,\theta)\) expression.

### 3.2 Global all-\(d\) stationary-error ledger

The Round-84 overlap count, summed over all residue progressions, gives
the bulk Morse and Gaussian-collar part of (2.9). Moving the complete
entry/exit collars into \(E\) costs

\[
 H\,{Q^2\over\sqrt\Lambda}\asymp M.                     \tag{3.8}
\]

Repeated integration by parts for the actual compact smooth principal
symbol gives the same \(O_\varepsilon(X^\varepsilon M)\) bound for the
wrong-sign and exterior tails. This use of smoothness is legitimate
only for the principal row; a single first-derivative \(M/(Q^2+|n|)\)
bound would not by itself be summable over every \(d\).

By (2.4) and the convolution identity

\[
 \sum_{d,n}|P(n+d)E(n)|=\|P\|_1\|E\|_1,
\]

all terms in the complete \(d\)-sum containing at least one \(E\)
contribute

\[
 \begin{aligned}
 &\ll_\varepsilon X^\varepsilon
 \sum_{b\asymp B}\bigl(HQ^2M+M^2\bigr)\\
 &\ll_\varepsilon X^\varepsilon
 \bigl(B^2HQ^2+B^3\bigr).                               \tag{3.9}
 \end{aligned}
\]

At \(C=J^{3/4}\), the two terms in (3.9) are respectively
\(J^{23/20}\) and \(J^{9/20}\), both strictly below
\(J^{7/5}=J^2/T\); they decrease with \(C\). Equation (3.9) is global
in \(d\), so it owns support entry/exit, opposite signs, and
\(|d|>\Delta_b\), rather than reusing the Round-84 small-\(d\) error
bound outside its range.

### 3.3 The smooth outer-edge deletion

It remains to treat \(P(n+d)\overline{P(n)}\). If
\(|d|>\Delta_b\), this product is identically zero. If

\[
 j=\Delta_b-|d|\geq0,
\]

then the overlap of the two stationary supports has length
\(O(j+1)\). On each progression \(n=r+M\ell\), it contains at most

\[
 O\!\left(1+{j+1\over M}\right)                         \tag{3.10}
\]

indices. When \(0\leq j\leq E_\delta\), the two stationary points
lie at opposite outer support edges. Flatness (2.11) therefore gives

\[
 |P(n+d)P(n)|
 \ll_{N,\varepsilon}X^\varepsilon H^2
 \left({j+1\over Q^2}\right)^{2N}.                     \tag{3.11}
\]

Using the exact normalized residue mass (2.3), (3.10), and (3.11),
then summing both signs of \(d\), all \(b\asymp B\), and
\(0\leq j\leq E_\delta\), gives

\[
 \begin{aligned}
 \mathfrak Y_{\mathrm{edge},\delta}^{PP}
 &\ll_{N,\varepsilon}X^\varepsilon H^2
 \left(
 {B E_\delta^{2N+1}\over Q^{4N}}
 +{E_\delta^{2N+2}\over Q^{4N}}
 \right)\\
 &\ll_{N,\varepsilon}X^\varepsilon H^2
 \left({E_\delta\over Q^2}\right)^{2N}
 (BE_\delta+E_\delta^2).                               \tag{3.12}
 \end{aligned}
\]

At the largest conductor,

\[
 H^2\leq J^{1/10},\qquad B\leq J^{3/20},\qquad
 E_\delta\leq J^{4/5-\delta}.
\]

The two exponents in (3.12) are at most

\[
 {21\over20}-(2N+1)\delta,
 \qquad
 {17\over10}-(2N+2)\delta.                              \tag{3.13}
\]

Choose a fixed integer \(N\geq0\) with

\[
 2(N+1)\delta\geq {3\over10}.                           \tag{3.14}
\]

Then both terms in (3.12) are \(O(X^\varepsilon J^{7/5})\).
Combining (3.9) and (3.12) proves (1.5). If \(N=0\), (3.12) is simply

\[
 \mathfrak Y_{\mathrm{edge}}^{PP}
 \ll_\varepsilon X^\varepsilon H^2(E^2+BE),             \tag{3.15}
\]

and \(E=J^{13/20}\) reaches the target exactly at the upper conductor.
This supplies the derivative-free check (1.6).

No differencing, completion, or coefficientwise trace estimate occurs
in (3.8)--(3.15). The saving is the actual support overlap, strengthened
by the actual smooth symbol's flatness.

## 4. First doubtful or unproved step

The first unproved step is a signed estimate for the exact interior
survivor (1.4). Its differences still have length comparable with
\(Q^2\), and neither (3.7) nor (3.12) supplies a whole-offset power.

In particular, (3.4)--(3.7) show precisely why the most immediate
time-frequency/uncertainty argument stops: after preserving the physical
factor \(Q^{-5/12}\), projection onto a large-\(d\) set introduces
\(\|K_w\|_1\geq1\), not \(B^{-1/2}\). Completing the \(\theta\)-Fourier
series is exactly the original physical off-residue energy, so it is a
self-return. An actual advance must exploit cancellation of
\(\mathcal G_b(\theta)\) jointly across \(b\), residues, and \(\theta\),
or a gcd-sensitive signed property of (2.2); the row supremum and
stationary support alone do not provide it.

This is not an actual-symbol impossibility theorem. It is a rigorous
no-go only for the inequality consisting of the shifted-row supremum,
Fourier projection, and triangle inequality. No claim is made that
the remaining actual coefficients saturate that bound.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| External normalization | **Pass.** The factor \(M^{-2}\) is present in (1.4), (3.4), and every estimate. The worst edge exponent is \(J^{7/5}=J^2/T\). |
| All three local classes | **Pass.** The exact triples are listed in (2.1); the proof uses only \(gM=4b\), exact finite orthogonality, and \(M\asymp B\). |
| Both endpoint orientations | **Pass.** The second orientation is the conjugate reflection; support diameter, flatness, error norms, and all absolute estimates are unchanged. |
| Physical \(Q^{-5/24}\) row factor | **Pass.** Equations (3.1)--(3.7) retain it before any difference projection, giving \(Q^{-5/12}\) in the energy and (1.7). |
| Difference ownership | **Pass.** Literal \(d=0\) and \(0<\lvert d\rvert\leq D_0\) remain removed exactly once. The new deletion is only \(\lvert d\rvert\geq\Delta_b-E_\delta\), which is disjoint from the small-\(d\) range for large \(J\). |
| Negative differences | **Pass.** Both outer collars are summed in (3.12); reflection changes only which endpoint is entered first. |
| Support edges and \(\lvert d\rvert\asymp Q^2\) | **Pass.** The exact overlap count is (3.10); the outer support complement is zero for \(PP\), and every tail is in the global bound (3.9). |
| Nonzero \(d\equiv0\pmod M\) | **Pass without exceptional deletion.** Such differences are retained in (1.4) unless they lie in the new geometric edge, in which case (2.3) treats them exactly. |
| Ramanujan subtraction | **Pass.** The \(-c_M(d)\) term remains in \(A_{M,K,d}\). It is exactly the same-residue subtraction in (3.3)--(3.4). |
| Prime powers and gcd modes | **Pass.** The main edge uses exact \(L^1\) mass (2.3); global errors use only the trivial exact bound (2.4). No false coefficientwise square-root bound is invoked. |
| Actual stationary symbol | **Pass.** The full-Gaussian leading symbol is the actual \(V_b(c_{b,m})\). Its compact smooth flatness yields (2.11). The raw Farey transition is excluded and keeps its separate owner. |
| Entry/exit and aggregate errors | **Pass.** They are moved into \(E\), whose global all-frequency \(\ell^1\) norm is (2.9); (3.9) sums them over every integer \(d\). |
| Differencing prefactor and diagonal | **Pass by non-use.** No van der Corput or Cauchy differencing is used, so there is no hidden \(Q^2/D\) prefactor or new differencing diagonal. The only multiplier cost is the explicit \(\|K_w\|_1\) in (3.7). |
| Integer derivatives and perfect powers | **Pass.** The edge estimate is absolute and depends only on support and flatness, so integral first derivatives, square phases, and fourth-power specializations create no exception. |
| Complete-transform self-return | **Pass.** Equation (3.4) identifies the return exactly, and (3.7) assigns it no power gain. |
| Transition and axes | **Pass by scope.** Only the transition-flattened smooth nonaxial principal row is treated. Transition errors and axes remain with their existing owners. |
| Downstream scope | **Pass.** No claim is made for \(C>J^{3/4}\), cone edges, another radial sector, full `M9-M1`, `M9`, endpoint uniformity, or the Gauss-circle exponent. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

The permitted context used was:

- `protocol.md`;
- the relevant Round-85/M1 entries of `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0816_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/synthesis.md`;
- `rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/reviews/conductor_round84_stationary_normalization.md`;
- `rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/reports/stationary_dual_difference_attack.md`;
- `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reviews/conductor_round82_residue_normalization.md`;
- `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/reviews/conductor_round83_dual_normalization.md`.

The conductor narrowed the task during execution to verification of the
support-edge deletion, the global all-\(d\) stationary-error count, and
the exact interior survivor. No sibling Round-85 report, new shared
review, web source, source card, or numerical computation was read.

## 7. Recommended state effect

**Promote after independent seam review** the scoped outer-edge
reduction (1.5): for every fixed \(0<\delta<4/5\), all differences

\[
 |d|\geq\Delta_b-Q^2J^{-\delta}
\]

are target-safe for the exact smooth principal row, with the integer
rounding in (1.2). The derivative-free version
\(E=J^{13/20}\) is an immediate conservative specialization. Also
promote the global all-\(d\) error estimate (3.9), which is what makes
the deletion exact rather than a leading-symbol truncation.

**Retain as a route-specific no-go** that the exact shifted-row
time-frequency identity plus the inherited row supremum and Fourier
multiplier triangle inequality cannot produce \(B^{-1/2}\): it returns
(85.15), up to \(X^\varepsilon\), while preserving its
\(Q^{-5/12}\) factor.

**Revise the candidate survivor, but do not close an obligation**, to
the exact interior correlation (1.4). Retain as open every fixed
\(B\)-power, any new conductor interval, the interior large-difference
estimate, \(C>J^{3/4}\), full `M9-M1`, `M9`, endpoint
uniformity, and the global exponent.
