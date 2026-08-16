# Round 86 analytic report: twisted ambiguity attack

Campaign: `m9-m1-interior-four-kloosterman-ambiguity`  
Task: `twisted_ambiguity_attack`  
Role: analytic discovery  
Starting graph SHA-256:
`910950f389c49a17cc188c8e0ad9b18e4d83d4a7f580fa0baacca97d39195fe6`

## 1. Result

There is a rigorous new deletion inside the Round-86 middle interval. It
does not use a four-Kloosterman estimate. Instead it keeps the exact
centered Kloosterman product periodic in \(n\pmod M\) and applies the
third-derivative estimate to the complete stationary square-root
difference on each progression.

Put

\[
 D_1:=\left\lfloor J^{87/140}\right\rfloor .             \tag{1.1}
\]

Then, uniformly for

\[
 J^{13/18}<C\leq J^{3/4},
\]

all terms of (86.1) with

\[
 D_0<|d|\leq D_1,
 \qquad D_0=\lfloor J^{17/30}\rfloor,                   \tag{1.2}
\]

are \(O_\varepsilon(X^\varepsilon J^2/T)\). Thus the exact new
smooth-principal survivor is

\[
 \boxed{
 \mathfrak Y_{\rm deep}={1\over M^2}\sum_{b\asymp B}
 \sum_{D_1<|d|<\Delta_b-E_*}\sum_n
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)} .}               \tag{1.3}
\]

More precisely,

\[
 \mathfrak Y_{\rm int}=\mathfrak Y_{\rm deep}
 +O_\varepsilon\!\left(X^\varepsilon {J^2\over T}\right).
                                                                    \tag{1.4}
\]

The continuously twisted physical-row identity is not spent in proving
(1.4). It therefore still supplies, for (1.3),

\[
 |\mathfrak Y_{\rm deep}|
 \ll_\varepsilon X^\varepsilon
 \left({C^3\over TQ^{5/12}}+{J^2\over T}\right),        \tag{1.5}
\]

so the physical \(Q^{-5/12}\) energy factor is retained exactly.

No whole-middle \(B^{-\delta}\), conductor extension, or endpoint
closure is proved. The exact four-Kloosterman transform does give a
useful no-go: separating a supposedly generic rational trace sum from
the \(h_1=h_2\) locus is not sufficient. That locus contains exact
self-return and prime-power modes of size \(M^{2-o(1)}\), even at
nonzero shifts below \(M\).

## 2. Exact statement and hypotheses

Assume

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B={C\over T},\qquad J^{13/18}<C\leq J^{3/4}.           \tag{2.1}
\]

Fix one compatible transition-flattened smooth nonaxial principal row,
one alias, one sign, and one endpoint orientation. In the three local
classes

\[
 (g,M,K)\in
 \{(1,4b,k),(2,2b,2[k\bar4]_b),(4,b,[k\bar4]_b)\},
 \qquad gM=4b,                                          \tag{2.2}
\]

one has \(b\asymp B\) and \(M\asymp B\). Define

\[
 A_{M,K,d}(n)=S(n+d,K;M)\overline{S(n,K;M)}-c_M(d).
                                                                    \tag{2.3}
\]

The proof uses the following exact or accepted interfaces from the
Round-86 packet.

1. \(A_{M,K,d}(n)\) is periodic in \(n\pmod M\), and for every integer
   \(d\),
   \[
     {1\over M^2}\sum_{r\bmod M}|A_{M,K,d}(r)|\leq2.     \tag{2.4}
   \]
2. On the active sign, \(m=|n|\asymp Q^2\), the complete principal
   stationary term has phase
   \[
     -\eta\lambda_b\sqrt m,\qquad
     \lambda_b=\sqrt X+{\sqrt{\kappa k}\over b}\asymp J,             \tag{2.5}
   \]
   and size \(H=C\sqrt T/J=BJ^{-1/10}\).
3. The complete phase-removed principal symbol, including its actual
   stationary amplitude and compact support, has sampled supremum plus
   variation \(O_\varepsilon(X^\varepsilon H)\) on every residue
   progression. Consequently the product of two translates has sampled
   supremum plus variation \(O_\varepsilon(X^\varepsilon H^2)\).
4. Entry/exit corrections, stationary errors, wrong signs, and exterior
   tails have already been routed out of (86.1) by the global Round-85
   error ledger. Raw Farey transitions and axes are separately owned.

Let \(\mathfrak Y_{(D_0,D_1]}\) denote (86.1) restricted to (1.2), with
both signs of \(d\). The claimed lemma is

\[
 \boxed{
 \mathfrak Y_{(D_0,D_1]}
 \ll_\varepsilon X^\varepsilon J^{7/5}
 =X^\varepsilon {J^2\over T}.}                         \tag{2.6}
\]

This statement is uniform in (2.2), both signs, and reflected
orientations. It retains every nonzero \(d\equiv0\pmod M\), every
prime-power gcd mode, and the full Ramanujan subtraction.

## 3. Proof or derivation

### 3.1 Progressionwise cubic curvature

Fix \(b,d\), and a residue \(r\pmod M\). On the intersection of the two
active stationary supports, write \(n=r+M\ell\). Interchanging the two
factors when necessary reduces both signs and both orientations to a
phase of the form

\[
 \Phi_{b,d,r}(\ell)
 =\pm\lambda_b\bigl(\sqrt{m+|d|}-\sqrt m\bigr),
 \qquad m\asymp Q^2.                                  \tag{3.1}
\]

The interval of admissible \(\ell\)'s has length

\[
 L\ll N:={Q^2\over M}.                                 \tag{3.2}
\]

Since

\[
 {d^3\over dx^3}\bigl(\sqrt{x+s}-\sqrt x\bigr)
 ={3\over8}\bigl((x+s)^{-5/2}-x^{-5/2}\bigr),          \tag{3.3}
\]

the mean-value theorem, \(m,m+|d|\asymp Q^2\), and
\(\lambda_b\asymp J\) give the uniform one-signed estimate

\[
 |\Phi'''_{b,d,r}(\ell)|
 \asymp {JM^3|d|\over Q^7}
 =:\rho_d.                                             \tag{3.4}
\]

The ratio of the upper and lower constants in (3.4) is absolute on the
fixed stationary support. This remains true at integer first
derivatives and on square or fourth-power specializations.

Let \(a_{b,d,r}(\ell)\) be the complete phase-removed product. The
accepted smooth hierarchy and the elementary product-variation
inequality give

\[
 \|a_{b,d,r}\|_\infty+
 \operatorname {Var}_\ell a_{b,d,r}
 \ll_\varepsilon X^\varepsilon H^2.                   \tag{3.5}
\]

The weighted third-derivative estimate applied to (3.1)--(3.5) yields

\[
 \left|\sum_\ell a_{b,d,r}(\ell)e(\Phi_{b,d,r}(\ell))\right|
 \ll_\varepsilon X^\varepsilon H^2
 \left(N\rho_d^{1/6}+N^{1/2}\rho_d^{-1/6}+1\right).
                                                                    \tag{3.6}
\]

Substituting \(Q=J^{2/5}\) into (3.6) gives

\[
 N\rho_d^{1/6}
 =J^{1/2}M^{-1/2}|d|^{1/6},\qquad
 N^{1/2}\rho_d^{-1/6}
 =J^{7/10}M^{-1}|d|^{-1/6}.                            \tag{3.7}
\]

### 3.2 Exact arithmetic normalization and summation

Because \(A_{M,K,d}(r+M\ell)=A_{M,K,d}(r)\), (2.4) and
(3.6)--(3.7) imply, for each \(b,d\),

\[
 \begin{aligned}
 {1\over M^2}\left|\sum_n A_{M,K,d}(n)
 I_b(n+d)\overline{I_b(n)}\right|
 \ll_\varepsilon X^\varepsilon H^2\bigl(&J^{1/2}M^{-1/2}|d|^{1/6}\\
 &+J^{7/10}M^{-1}|d|^{-1/6}+1\bigr).
 \end{aligned}                                        \tag{3.8}
\]

No Kloosterman coefficient is estimated pointwise in (3.8). In
particular, (2.4) keeps the prime-power and modulus-multiple modes.
Summing (3.8) over \(b\asymp B\), both signs, and
\(D_0<|d|\leq D\), using \(M\asymp B\) and
\(H^2=B^2J^{-1/5}\), gives

\[
 \mathfrak Y_{(D_0,D]}
 \ll_\varepsilon X^\varepsilon\left(
 B^{5/2}J^{3/10}D^{7/6}
 +B^2J^{1/2}D^{5/6}
 +B^3J^{-1/5}D\right).                                \tag{3.9}
\]

At the largest conductor, \(B\leq J^{3/20}\). With
\(D=D_1=J^{87/140}\), the three powers of \(J\) on the right of
(3.9) are at most

\[
 J^{7/5},\qquad J^{369/280},\qquad J^{61/70},          \tag{3.10}
\]

respectively. The first is exactly the target and the other two are
strictly smaller. All terms in (3.9) increase with \(B\), so (3.10)
is uniform throughout (2.1). The logarithmic number of dyadic
\(d\)-shells is absorbed by \(X^\varepsilon\). This proves (2.6), and
(1.4) follows from the already accepted small-\(d\) and outer-edge
deletions.

### 3.3 Preservation of the physical-row saving

Apply (86.3) to the new deep multiplier

\[
 w_b(d)=\mathbf 1_{\{D_1<|d|<\Delta_b-E_*\}}.
\]

Its Fourier kernel has \(L^1\)-norm \(O(\log J)\). The exact shifted
physical-row estimate remains

\[
 |\mathcal R_{b,x}(\theta)|
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.
\]

Thus Fourier projection gives
\(X^\varepsilon C^3/(TQ^{5/12})\) for (1.3), while subtracting the
newly safe shell costs only (2.6). This proves (1.5). In particular,
the cubic deletion and the physical \(Q^{-5/12}\) factor are cumulative,
not alternative normalizations.

### 3.4 Exact four-Kloosterman transform and its diagonal obstruction

For completeness, write the nonzero arithmetic Fourier coefficient as

\[
 \mathcal C_{M,K}(a,h)=
 \sum_{\substack{x\bmod M\\(x(x-h),M)=1}}
 e_M\!\left(ax+K[x^{-1}-(x-h)^{-1}]\right).            \tag{3.11}
\]

Opening two copies, summing \(a\pmod M\), and setting the second
physical variable equal to \(x-v\) gives the exact identity

\[
 \begin{aligned}
 &\sum_{a\bmod M}\mathcal C(a+u,h_1)
 \overline{\mathcal C(a,h_2)}e_M(-va)\\
 &\quad=M\!\sum_{\substack{x\bmod M\\
 x,x-h_1,x-v,x-v-h_2\ {\rm units}}}
 e_M\!\left(u x+K\left[x^{-1}-(x-h_1)^{-1}
 -(x-v)^{-1}+(x-v-h_2)^{-1}\right]\right).
 \end{aligned}                                        \tag{3.12}
\]

At \(v=0\) and \(h_1=h_2=h\), the rational phase cancels identically:

\[
 (3.12)=M\sum_{\substack{x\bmod M\\(x(x-h),M)=1}}e_M(ux).
                                                                    \tag{3.13}
\]

For \(u\equiv0\pmod M\), (3.13) is the exact self-return
\(MN_M(h)\). More strongly, let \(M=p^\nu\), \(\nu\geq2\), take
\(h=p\), and take the nonzero shift \(u=p^{\nu-1}<M\). Then the two
unit conditions in (3.13) are both simply \(p\nmid x\), and

\[
 |(3.13)|=M\,|c_{p^\nu}(p^{\nu-1})|
 =M p^{\nu-1}={M^2\over p}.                            \tag{3.14}
\]

Hence the equal-\(h\) piece is not coefficientwise square-root even
below the first exact \(u=M\) return. At a good odd prime
\(p\nmid K\), complete pole cancellation in the rational part of
(3.12) occurs only when \(v=0,h_1=h_2\); full constant degeneracy also
requires \(u=0\). Thus a generic prime-field square-root trace estimate
is available away from that locus. It still does not control the actual
aggregate: if \(p\mid K\), the rational part can disappear modulo \(p\);
if \(p\mid u\) as well, a full constant mode returns. At prime powers,
collisions \(h_1\equiv h_2\pmod {p^j}\), pole collisions, and stationary
gcd modes persist, with (3.14) an explicit example. A good-prime
coefficientwise bound therefore cannot be multiplied over arbitrary
\(M\) and summed after declaring (3.13) harmless. The complete actual
weighted equal-\(h\) aggregate would itself need a new estimate.

This also explains the \(A\)-process threshold. With shift height
\(U\leq M\asymp B\), the diagonal can yield at most the formal
\(B^{-1/2}\) gain, reaching \(C\leq J^{56/75}\). Taking the larger
height needed for \(B^{-5/9}\) necessarily crosses \(u=M\), where
(3.13) returns. The Fejer prefactor, diagonal, two Ramanujan cross
terms, and Ramanujan-square term therefore cannot be suppressed.

### 3.5 The residual \(b\)-phase is quantitatively sufficient only
conditionally

The \(b\)-dependent part of the stationary difference phase is

\[
 {\sqrt{\kappa k}\over b}
 \bigl(\sqrt{n+d}-\sqrt n\bigr).
\]

For \(n\asymp Q^2\), \(d\ll Q^2\), its total variation across
\(b\asymp B\) is

\[
 \asymp {d\over QB}.                                   \tag{3.15}
\]

At \(C=J^{3/4}\), \(B=J^{3/20}\), and the old boundary
\(d=D_0=J^{17/30}\), (3.15) is

\[
 J^{1/60}=B^{1/9}.                                     \tag{3.16}
\]

An ideal square-root use of (3.16) would give \(B^{-1/18}\); combined
with the formal \(B^{-1/2}\) residue gain, this is exactly
\(B^{-5/9}\). This exponent match is real, but it is not a proof.
The modulus \(M\), the inverse unit \(K\), the Kloosterman products,
the residue set, and the stationary symbol all vary with \(b\). No
sampled-\(b\) BV estimate or composite-modulus large sieve for that
actual vector is available in the permitted input. Taking absolute
values before using (3.15) destroys the oscillation, while treating the
arithmetic vector as an arbitrary coefficient is falsified by the
self-return (3.13)--(3.14). Thus the proposed \(B^{-1/18}\) supplement
remains a precise conditional target, not a promoted gain.

## 4. First doubtful or unproved step

The cubic shell deletion (2.6) has no unproved analytic step beyond the
accepted complete-symbol sampled-variation interface. Translation and
multiplication preserve that interface by

\[
 \operatorname {Var}(fg)
 \leq\|f\|_\infty\operatorname {Var}(g)
 +\|g\|_\infty\operatorname {Var}(f),
\]

and the exact support intersection is one interval on each progression.

The first unproved step after (1.4) is a signed estimate for
\(D_1<|d|<\Delta_b-E_*\). In the literal \(d\)-\(A\)-process, it is the
complete actual-symbol weighted off-diagonal after (3.12), including the
equal-\(h\) prime-power pieces (3.13)--(3.14). Equivalently, a hybrid
route must prove that the \(b\)-oscillation (3.15) acts on the actual
varying-modulus arithmetic vector without losing the inherited
\(Q^{-5/12}\). Neither assertion follows from the shifted-row supremum,
generic trace bounds, Parseval, or the present derivative estimate.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| External normalization | **Pass.** The factor \(M^{-2}\) is retained in (1.3), (2.6), and (3.8). The largest term in (3.10) is exactly \(J^{7/5}=J^2/T\). |
| All-class local units | **Pass.** The proof uses the exact triples (2.2), \(gM=4b\), \(M\asymp B\), and the class-independent identities (2.4) and (3.12). It does not infer the even units from the odd one. |
| Physical-row energy factor | **Pass.** Section 3.3 retains \(TQ^{-5/24}\) per physical row and \(Q^{-5/12}\) in (1.5). |
| Middle-difference ownership | **Pass.** Only \(D_0<|d|\leq D_1\) is newly removed. The old small range and outer collar are not counted again; (1.3) is the strict remaining middle. |
| Negative and modulus-multiple differences | **Pass.** Negative \(d\) follows by factor interchange. Every nonzero \(d\equiv0\pmod M\) in (1.2) is included in (3.8), not relabeled as the zero mode. |
| Ramanujan cross and square terms | **Pass.** The positive proof keeps \(A_{M,K,d}\) intact. Section 3.4 explicitly records that opening the \(A\)-process creates both cross terms and the square term and licenses no deletion. |
| Prime-power gcd modes | **Pass.** Equation (2.4) is exact for arbitrary \(M\). Equation (3.14) is an explicit hostile prime-power control showing why a generic square-root trace substitute is false. |
| Fejer prefactor and diagonal | **Pass by non-use for (2.6), and retained in the audit.** The cubic proof does not apply an \(A\)-process. The discussion following (3.14) keeps its compulsory prefactor, diagonal, and \(U\leq M\) limitation. |
| Four-Kloosterman off-diagonal | **Pass.** It is derived exactly in (3.12), not replaced by a two-product model. No bound for its full actual weighted sum is claimed. |
| Actual stationary symbol | **Pass.** Equations (3.5)--(3.6) use the complete phase-removed smooth symbol and its sampled variation, not a frozen saddle value or arbitrary BV antecedent. |
| Entry/exit and error ownership | **Pass.** The proof acts only on (86.1). Entry/exit, Morse error, wrong sign, and exterior tails remain in the already accepted global Round-85 ledger; raw transitions and axes remain separately owned. |
| Integer and perfect-power resonance | **Pass.** The third derivative (3.4) is nonzero and one-signed independently of the first derivative modulo one. Squares and fourth powers require no exception. |
| Complete transform and \(u=M\) self-return | **Pass.** Section 3.4 exhibits the exact return \(MN_M(h)\), and (1.5) assigns complete physical projection no extra power. |
| Downstream scope | **Pass.** No claim is made for a whole-middle \(B\)-power, a conductor extension, \(C>J^{3/4}\), raw transitions, axes, cone edges, another radial sector, full `M9-M1`, `M9-M2`, `M9`, endpoint uniformity, `R5-Full`, or the Gauss-circle exponent. |

No numerical experiment or external theorem was used in the positive
shell proof. The good-prime comment after (3.14) is a route audit only
and is not a dependency of (2.6).

## 6. Dependencies and exact artifacts used

The permitted context used was:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0816_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/synthesis.md`;
- `rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reviews/conductor_round85_support_edge_normalization.md`;
- `rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reports/hybrid_large_difference_attack.md`;
- `rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/reviews/conductor_round84_stationary_normalization.md`.

The conductor supplied the finite identity checked independently in
(3.11)--(3.12), together with the good-prime pole-degeneracy check
audited after (3.14). No sibling Round-86 report, source card, web
source, or numerical computation was read or used.

## 7. Recommended state effect

**Promote after independent seam review** a scoped reduction, suggested
ID `M9-M1-centred-dual-difference-cubic-shell-bound`, asserting (2.6)
with

\[
 D_1=\lfloor J^{87/140}\rfloor.
\]

Revise the exact smooth-principal survivor from
\(D_0<|d|<\Delta_b-E_*\) to (1.3), and retain the physical baseline
(1.5). This is a strict proof-state improvement but not a conductor
extension.

**Retain as a route-specific no-go** that a generic rational-function
square-root estimate after the four-Kloosterman transform can close the
off-diagonal once \(h_1=h_2\) is called a harmless diagonal. Equations
(3.13)--(3.14) show exact self-return and \(M^2/p\) prime-power modes.

**Retain as an unproved conditional milestone** the exponent match

\[
 B^{-1/2}\cdot B^{-1/18}=B^{-5/9}
\]

from residue dispersion plus the residual \(b\)-phase. A valid theorem
must act on the actual varying-modulus symbol and preserve
\(Q^{-5/12}\); the phase-variation count alone is not evidence.

Keep open the remaining deep correlation, every whole-middle
\(B\)-power, any conductor extension, \(C>J^{3/4}\), transitions, axes,
cone edges, other sectors, full `M9-M1`, `M9-M2`, `M9`, endpoint
uniformity, and the global exponent.
