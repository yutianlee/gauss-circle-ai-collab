# Round 191 final-kernel power, literal, and owner-scope post-hygiene verification

- Campaign: m9-m1-t1-fast-height-jump-coboundary-gate
- Reviewed kernel:
  proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md
- Current kernel SHA-256:
  7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2
- Comparison evidence:
  reviews/final_kernel_power_literal_owner_scope_review.md
- Review role: focused hygiene-only power and owner-scope replay
- Status: review evidence only; no kernel or shared-state edit

## 1. Result and verdict

**Verdict: PASS.** The current kernel preserves every mathematical
statement, hypothesis, estimate, dependency, type boundary, and scope
quarantine certified by the prior final-kernel PASS. The refresh is
nonmathematical:

1. the formal-candidate provenance hash is now
   76c1a3adb14fc00063a2fcab06f73458ae8f5c9b0e7d19e41c5d8c78f103b978;
2. the narrative definition of the transported superscript now uses
   valid TeX, \({\rm tr}\), rather than the former Markdown-like marker.

Neither change enters an equation, predicate, summation range,
inequality, dependency, or proposed state effect. The promoted content
remains only the strict signed-inverse sector, the terminal and Fejer
safe projections, their \(L^2X^\varepsilon\) outer bound, and the exact
decomposition (191.C11). Estimate (191.C12) remains open with exact
deficit

\[
 \boxed{Y/(Qm)>1.}
\tag{191.H1}
\]

## 2. Exact statement and hypotheses preserved

The refreshed kernel still fixes the Round-189 fast packet under

\[
 U=mq>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y,\quad
 j_q(a,v)>T_Q,
\tag{191.H2}
\]

with \(U\mid u\), \(g=u/U\), odd \(\kappa,g,U\), \((u,v)=1\),
\((U,h)=1\), \(0<2\kappa gh<R_0\), and

\[
 u\asymp v\asymp L/\kappa,\qquad
 \operatorname{length}(\mathcal V_{\rm lit})\ll u,\qquad
 L\ll X^{1/4}.
\tag{191.H3}
\]

The signed inverse and strict safe cutoff are unchanged:

\[
 \varrho_U(v)v-\gamma_U(v)U=1,\qquad
 -\frac{U-1}{2}\leq\varrho_U(v)\leq\frac{U-1}{2},
\]

\[
 0<|\varrho_U(v)|\leq
 \min\left\{\frac{U-1}{2},
 \left\lfloor\frac{QmU}{Y}\right\rfloor\right\}.
\tag{191.H4}
\]

The fixed estimates remain

\[
 |\mathscr J_{{\rm inv},{\rm fix}}|
 \ll Qm\kappa uX^\varepsilon,\qquad
 |\mathscr J_{{\rm terminal},{\rm fix}}|
 +|\mathscr J_{{\rm Fejer},{\rm fix}}|
 \ll \kappa uX^\varepsilon,
\tag{191.H5}
\]

and the full safe estimate remains

\[
 |\mathscr J_{Y,Q}^{{\rm safe},\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{191.H6}
\]

Floor-zero and saturated cutoffs retain their prior meanings. Both
orientations, every literal field, and all zero-extension deaths remain
inside the same complex aggregate.

## 3. Proof and focused comparison

### 3.1 Theorem and ledger

The signed-inverse class count is still

\[
 \#\{v:0<|\varrho_U(v)|\leq T_\varrho\}
 \ll \frac{uT_\varrho}{U}
 \ll \frac{Qmu}{Y}.
\]

Multiplication by \(O(Y)\) heights and \(O(\kappa)\) sites gives the
first estimate in (191.H5) without a \(q/J\) loss. The terminal
calculation is still

\[
 (q/J)(uJ/q)\kappa X^\varepsilon
 \ll\kappa uX^\varepsilon,
\]

and the Fejer calculation is still

\[
 (q/J)(uJ/q)Y\kappa
 \frac{2\kappa g}{R_0}X^\varepsilon
 \ll\kappa uX^\varepsilon,
\qquad \frac{2\kappa gY}{R_0}<1.
\]

The outer ledger is unchanged:

\[
 c_{mq}(ma)=m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),\qquad
 \sum_{mq\mid u}1\leq\tau_3(u).
\]

Thus \(m^{-1}\) still cancels before the positive outer sum, the
power-of-two bands and coefficient mass cost only fixed logarithms, and

\[
 QX^\eta\sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\]

No positive power of \(Y\) has appeared or been absorbed. The theorem
and power ledger certified by the prior PASS are unchanged.

### 3.2 Fixed/full typing and one outer operation

The fixed packet remains (191.C13a). Its inverse, terminal, and Fejer
pieces remain exact complex projections, and
\(\mathscr R_{\rm fix}\) remains their complex subtraction in
(191.C28d). The full safe packet and remainder remain the separate
images of those fixed objects under the one linear outer assembly in
(191.C32a)--(191.C32b). Hence

\[
 \mathscr F_{Y,Q}^{\sigma}
 =\mathscr J_{Y,Q}^{{\rm safe},\sigma}
  +\mathscr R_{Y,Q}^{\sigma}
\]

still holds before the final real part.

No orientation-wise norm, inner real part, or inner modulus has been
introduced. Absolute values occur only after joint complex safe
projections are defined. The formatting repair to the notation
\({\rm tr}\) changes only how the already-defined transported
evaluation is rendered; every occurrence in (191.C24)--(191.C25)
retains the same algebraic meaning.

### 3.3 Literal, bounded-array, dependency, and scope boundaries

The exact gated partition (191.C22d), affine common/birth/death split
(191.C23), carry/Fejer/endpoint/phase telescoping (191.C24), two-endpoint
product identity (191.C24a), arithmetic-mask split (191.C25), and
ordered first-changed-field list (191.C25a) are all still present.
Outer terminal zero and endpoint zero extension remain distinct, and
the actual common-cell coefficient difference remains in the residual
case. No literal jump source was added, deleted, merged, or assigned a
regularity estimate.

The bounded-array identity (191.C38) is unchanged, including its lawful
zero-extended extremizer
\(W_r(h)=\overline z_r^{\,h}\mathbf1_{H_r}(h)\). It remains expressly
quarantined as an operator-class capacity statement, not literal
realizability, a literal lower bound, or a disproof of (191.C12).

The direct dependencies remain exactly

- M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction;
- Divisor-bound-elementary.

The owner list and exponent sentence are unchanged: every original
\(t\geq2\) small-\(G\) incidence, the large-\(G\) near-resonant
complement, the rest of the small-\(t\) owner, hard and smooth M1, GAR,
every M2 parent, endpoint uniformity, M9, both bridges, and the quarter
target remain open or conditional. The internal \(1/3\), external
\(0.3144831759740614\ldots\), and target \(1/4\) exponents remain
unchanged.

## 4. First doubtful or unproved step

The first unproved step remains exactly

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{191.H7}
\]

Positive control still gives only \(Y\kappa uX^\varepsilon\) at fixed
outer labels and band, against the target
\(Qm\kappa uX^\varepsilon\). The carry, displaced literal endpoint
coefficients, actual square-root phase, and changing masks still require
a genuinely signed theorem. The hygiene and candidate-hash refresh
neither supplies nor claims that theorem.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Current kernel hash | PASS: exact match to 7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2. |
| Candidate-hash refresh | PASS: metadata only; no theorem or dependency uses the hash as a mathematical input. |
| Transport-superscript formatting | PASS: the legacy marker is absent and the narrative now uses valid \({\rm tr}\) TeX consistently with (191.C24)--(191.C25). |
| Strict-sector power | PASS: \(O(Qmu/Y)\) rows and \(O(Y\kappa)\) row mass still give \(O(Qm\kappa uX^\varepsilon)\). |
| Terminal/Fejer power | PASS: both remain \(O(\kappa uX^\varepsilon)\) at fixed packet. |
| Outer ledger | PASS: \(m^{-1}\), coefficient logarithm, \(\tau_3\), band logarithm, and shell sum still give \(L^2X^\varepsilon\). |
| Fixed/full typing | PASS: exact definitions at both levels remain separate. |
| One outer operation | PASS: both orientations remain joint; no inner modulus or real part was added to the remainder. |
| Literal jump coverage | PASS: the exact-once source partition is unchanged. |
| Bounded-\(W\) quarantine | PASS: operator capacity is unchanged and no literal realization is asserted. |
| Direct dependencies | PASS: the same two accepted dependencies remain listed. |
| Open C12 | PASS: explicitly open with deficit \(Y/(Qm)\). |
| Owner scope | PASS: the complete prior owner quarantine is unchanged. |
| Exponent scope | PASS: \(1/3\), \(0.3144831759740614\ldots\), and \(1/4\) are unchanged. |
| Text hygiene | PASS: UTF-8 without BOM; no NUL byte, conflict marker, trailing-whitespace line, mixed newline style, or legacy transported-superscript marker. |

## 6. Dependencies and exact artifacts used

Only the two assigned artifacts were used:

1. proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md
   — SHA-256
   7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2.
2. reviews/final_kernel_power_literal_owner_scope_review.md
   — SHA-256
   6ab7a48387bb40f42a36a53f706044c77e61a61102737f3b92f445625f2d62f0.

No candidate, earlier kernel, proof-state file, sibling review, external
source, web result, or numerical computation was read or used.

## 7. Recommended state effect

**Retain the prior PASS and accept the refreshed final kernel as the
same durable proved_internal subordinate reduction, subject to the
conductor's normal graph patch and validation.** Promote only
(191.C5)--(191.C11) at their stated strict-sector, safe-projection, and
exact-reduction scopes.

Keep (191.C12) open with exact deficit \(Y/(Qm)\). Make no owner or
exponent change, and do not promote the bounded-array or archived finite
controls beyond their stated diagnostic/no-go roles. No mathematical
repair is required after the hygiene-only refresh.
