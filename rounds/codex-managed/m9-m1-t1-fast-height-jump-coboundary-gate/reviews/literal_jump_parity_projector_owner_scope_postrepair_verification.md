# Round 191 literal-jump, parity-projector, and owner-scope post-repair verification

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Reviewed candidate: `candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md`
- Frozen candidate SHA-256: `263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`
- Compared review: `reviews/literal_jump_parity_projector_owner_scope_seam_review.md`
- Review role: hostile literal-source, parity-projector, one-outer-operation,
  and owner-scope seam replay
- Status: review evidence only; no candidate or shared-state edit

## 1. Result and verdict

**Verdict: PASS for the stated reduction, with the rho-large remainder
and every downstream owner still quarantined.**  The current candidate
repairs all five defects labelled (191.R1), (191.R6), (191.R7),
(191.R8), and (191.R9) in the prior review.  It also supplies the
previously implicit support hypotheses, separates fixed-fibre from full
outer packets, and gives an exact complex complement before the sole
final real part.

The promoted content, if the conductor accepts it, is only the strict
signed-inverse sector together with the exact terminal/Fejer
projections and the decomposition (191.C11).  It does not include the
open estimate (191.C12).  At fixed outer labels and fast band, the
remaining positive bound is

\[
 Y\kappa uX^\varepsilon
 \quad\hbox{versus}\quad
 Qm\kappa uX^\varepsilon,
\]

so the first unresolved deficit is still exactly

\[
 D_{\rm rem}=\frac{Y}{Qm}>1.
\tag{191.P1}
\]

Equivalently, before the factor \(q/J\), the positive jump mass and
required variation mass are respectively
\(Y\kappa uJ/q\) and \(Qm\kappa uJ/q\), with the same deficit.

## 2. Exact verified statement and hypotheses

The replay verifies the candidate only under its displayed literal
hypotheses

\[
 Q=\lfloor(\log(2X))^B\rfloor,\qquad
 U=mq>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y,
\]

\[
 U\mid u,\quad g=u/U,\quad \kappa,g,U\ {\rm odd},\quad
 (u,v)=1,\quad(U,h)=1,\quad0<2\kappa gh<R_0,
\tag{191.P2}
\]

together with the repaired support connectors

\[
 u\asymp v\asymp L/\kappa,\qquad
 \operatorname{length}(\mathcal V_{\rm lit})\ll u,
 \qquad L\ll X^{1/4}.
\tag{191.P3}
\]

The fast predicate \(j_q(a,v)>T_Q\), its disjoint power-of-two bands,
all original literal fields, both orientations, and the final
zero-extension deaths remain in the packet.  For the signed least
inverse

\[
 \varrho v-\gamma U=1,\qquad
 -(U-1)/2\leq\varrho\leq(U-1)/2,
\]

the safe inverse predicate is exactly

\[
 0<|\varrho|\leq
 T_\varrho:=\min\left\{(U-1)/2,
 \left\lfloor QmU/Y\right\rfloor\right\}.
\tag{191.P4}
\]

Its fixed packet is (191.C13a) restricted by (191.P4).  The terminal
and Fejer packets are the exact fixed complex projections
(191.C28b)--(191.C28c), and the fixed remainder is the complex
subtraction (191.C28d).  The full safe packet and full remainder are
then, separately and without a change of meaning, the images of those
fixed packets under the inherited linear outer assembly in
(191.C32b).  Thus the complement is exact both before and after outer
assembly.  Floor-zero makes the inverse sector empty; saturation makes
its row complement empty.  Neither case requires an exception to the
decomposition.

## 3. Proof and hostile seam replay

### 3.1 R1: full parity versus a retained fast mode

From (191.C18),

\[
 S_{0,\omega}(h)-S_{0,\omega}(h-1)
 =\epsilon_\omega\varrho+\nu_\omega(h)U.
\]

Consequently the current/transported-previous affine and accepted-mode
ratio is exactly

\[
 (-1)^{\nu_\omega(h)}
 e(\epsilon_\omega k\varrho/U)
 =(-1)^{\nu_\omega(h)}
 e(\epsilon_\omega a\varrho/q),
\tag{191.P5}
\]

for the inherited accepted frequency \(k=ma\) and \(U=mq\).  This is
displayed in (191.C20a), with the correct orientation sign.  In the
plus fibre transport subtracts \((\varrho,\gamma)\); in the minus fibre
it adds them.  In either orientation the pre-Fourier bare site parity
changes by \((-1)^\varrho\) because \(U\) is odd.

The candidate now draws the required projector boundary exactly:
\((-1)^\varrho\) is a complete-anchor identity, while (191.P5) is the
identity for one retained mode.  The carry sequence is not constant in
height and multiplication by it mixes Fourier modes.  Summing all
modes reconstructs the complete-anchor parity but returns to the
pre-Round-187 packet.  No occurrence of \((-1)^\varrho\) is used to
simplify the retained fast remainder.  The former false parity route is
therefore closed rather than promoted as cancellation.

### 3.2 R6 and R7: exact outer gating and endpoint coverage

Equation (191.C22d) is an exhaustive disjoint truth-table identity for
the two binary masks \(K\) and \(G\):

- if \(K\) is born or dies, the complete live-side \(GA\) is taken;
- if \(K_h=K_-=1\) and \(G\) flips, the complete live-side \(A\) is
  taken; and
- only if both masks persist is \(A_h-A_-\) sent to affine transport.

This remains exact when \(K\) and \(G\) change simultaneously, because
the first branch already contains the live-side value of \(G\).  No
outer event is omitted or duplicated.

On the persistent branch, (191.C23) partitions the affine index sets
into transported common sites, current births, and previous deaths.
On a common site, (191.C24) assigns the four remaining differences to
carry, Fejer, endpoint product, and actual square-root phase.  The
endpoint product is then opened by the exact two-factor identity

\[
 \Lambda_h-\Lambda_-^{\rm tr}
 = (\lambda_{1,h}-\lambda_{1,-}^{\rm tr})
   \overline{\lambda_{0,h}}
 +\lambda_{1,-}^{\rm tr}
  (\overline{\lambda_{0,h}}
   -\overline{\lambda_{0,-}^{\rm tr}}),
\tag{191.P6}
\]

using the orientation-specific divisor pairs (191.C22a)--(191.C22b).
Equation (191.C25) is applied separately to both endpoints and is
conjugated for endpoint zero.  Arithmetic-mask changes and literal
amplitude changes are thereby separated algebraically before the
first-changed-field partition.

The resulting exact-once source ledger is:

| Source | Unique location |
|---|---|
| outer dyadic/carrier birth or death | first line of (191.C22d) |
| outer \((U,h)=1\) flip | persistent-\(K\) part of (191.C22d) |
| affine positivity birth or death | (191.C23) |
| canonical-anchor carry | first term of (191.C24) |
| Fejer change | second term of (191.C24) |
| two endpoint arithmetic masks and values | (191.C24a), then (191.C25) for \(i=0,1\) |
| shell/cone/selector/profile/floor/star/half-weight/hard-sample/crossing/trace labels | ordered first-change list (191.C25a) |
| actual common-cell endpoint value | the no-label-change residue after (191.C25a) |
| actual square-root phase | last term of (191.C24) |

The endpoint's own zero extension is explicitly distinguished from the
outer \(K\)-terminal zero.  Simultaneous endpoint label changes go to
the first differing entry, while the actual numerical profile is not
replaced by its cell label.  Thus no literal source named in the
candidate is missing, and no regularity is silently assigned to one.

### 3.3 R8: lawful safe projections and one outer operation

The three safe objects at fixed
\((\kappa,u,m,q,a,J,\sigma)\) are exact linear complex packets:

\[
 \mathscr J_{{\rm inv},{\rm fix}},\qquad
 \mathscr J_{{\rm terminal},{\rm fix}},\qquad
 \mathscr J_{{\rm Fejer},{\rm fix}}.
\]

Each completes both orientations and all its surviving literal labels
before a modulus.  The terminal projection contains the full live-side
outer atom \(D_K\); the Fejer projection is restricted to persistent
\(K,G\) and transported common sites.  Their sum and complement are
defined in (191.C28d) before triangle inequality.  Hence (191.C28),
(191.C30), and (191.C32) are bounds for already-defined projections,
not inner positive completions of the unsolved packet.

Equations (191.C32a)--(191.C32b) then apply one inherited linear outer
assembly to the fixed packets.  In particular:

- there is no separate plus/minus norm;
- no real part or modulus is inserted into \(\mathscr R_{\rm fix}\) or
  \(\mathscr R_{Y,Q}^\sigma\);
- triangle inequality is used only among completed safe projections
  and subsequently in their positive outer estimate; and
- the exact \(m^{-1}c_q(a)\) lift cancels the \(m\) in the fixed safe
  bound before the outer divisor sum.

This satisfies the one-outer-operation rule.  The fixed/full
distinction is mechanical, not merely verbal, and (191.C11) follows by
linearity.

### 3.4 R9: bounded-array capacity and its quarantine

For zero-extended arrays supported on finite sets \(H_r\), Abel gives

\[
 \frac1{1-z_r}\sum_h\Delta^-W_r(h)z_r^h
 =\sum_{h\in H_r}W_r(h)z_r^h.
\]

Therefore the upper bound in (191.C38) is \(\sum_r|H_r|\), and the
lawful choice

\[
 W_r(h)=\overline{z_r}^{\,h}\mathbf1_{H_r}(h)
\]

attains equality, including every zero-extension birth, death, and
hole.  The arrays are coboundaries; no jump atom is selected
independently.  Independent row choices can align both orientations
inside the single final complex sum, so support, pointwise size,
separate variation, and other separable positive norms have full
operator capacity.

The candidate correctly quarantines this as an operator-class no-go.
It neither asserts that the extremizing arrays occur in the fixed
literal endpoint family nor gives a literal lower bound or a disproof
of (191.C12).  Its exact content is only that a proof using those
bounded-array data alone cannot manufacture the missing factor
\(Y/(Qm)\).

### 3.5 Owner and exponent quarantine

The candidate lists, both in its statement and proposed state effect,
every remaining owner: all original \(t\ge2\) small-\(G\) incidences,
the large-\(G\) near-resonant complement, the rest of the small-\(t\)
owner, hard and smooth M1, GAR, every M2 parent, endpoint uniformity,
M9, both bridges, and the Gauss-circle quarter target.  None is claimed
proved by this reduction.  The internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), and target \(1/4\) exponents are stated
unchanged.  No downstream or exponent leak remains.

## 4. First doubtful or unproved step

There is no remaining formal seam defect in (191.C3a),
(191.C14)--(191.C35), or (191.C38) among the issues assigned to this
replay.  The first genuinely unproved step is precisely the advertised
rho-large estimate (191.C12).  Already at transported common sites it
would require signed control of the interaction among the carry,
displaced literal endpoint coefficients, and actual square-root
phases, while endpoint masks may change and the displacement is
\((\varrho,\gamma)\), not a unit shift.  Neither transport nor Abel
alone supplies the deficit (191.P1).

The candidate's final finite-control counts were not independently
replayed in this two-file review.  They are explicitly labelled
diagnostic and excluded from numerical theorem evidence, so this does
not affect the PASS.  If those counts are later used as promoted
control evidence, their exact artifact paths, commands, parameters,
outputs, and hashes must be attached separately.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Repaired support connectors (R3) | PASS: \(u,v\asymp L/\kappa\), total literal \(v\)-length \(O(u)\), and \(L\ll X^{1/4}\) are explicit. |
| R1 retained-mode parity | PASS: (191.C20a) has the exact carry, orientation, and \(k=ma\), \(U=mq\) phase; full parity is projector-quarantined. |
| R6 simultaneous outer masks | PASS: (191.C22d) is a disjoint exhaustive gated identity. |
| R7 two endpoint factors | PASS: (191.C24a) includes both factors, conjugation, and the actual orientation-specific divisor arguments. |
| Endpoint/jump-source coverage | PASS: outer terminal, coprimality, affine, carry, Fejer, both endpoints, common-cell value, and phase each occur exactly once. |
| R8 exact terminal projection | PASS: the complete \(D_K\) atom is summed jointly before modulus. |
| R8 exact Fejer projection | PASS: it is restricted to persistent masks and transported common sites and is summed jointly before modulus. |
| One outer operation | PASS: no orientation-wise norm or inner modulus is inserted; the outer assembly is linear. |
| Fixed versus full complement | PASS: (191.C28d) and (191.C32b) give separate exact definitions and complex subtraction at both levels. |
| Lift and divisor ledger | PASS: \(m^{-1}\) cancels before positivity; only \(\tau_3(u)\), coefficient logarithms, and band logarithms remain. |
| R9 bounded-array scope | PASS: the supremum is over lawful zero-extended \(W\), equality is attained, and literal realizability is not claimed. |
| No-go deficit | PASS: both forms give exactly \(Y/(Qm)\); no positive power of \(Y\) is hidden in \(X^\varepsilon\). |
| Downstream owner quarantine | PASS: every owner requested by the prior review is named and left open or conditional. |
| Exponent quarantine | PASS: \(1/3\), \(0.3144831759740614\ldots\), and \(1/4\) are unchanged. |
| Frozen-file hygiene | PASS: current candidate hash matches the conductor's updated hash; UTF-8 text has no BOM, NUL byte, conflict marker, trailing-whitespace line, or mixed newline style. |
| Finite diagnostic provenance | QUARANTINED: not used for the theorem or this PASS; exact archives would be required before citing it as control evidence. |

## 6. Dependencies and exact artifacts used

Only the two artifacts authorized for this replay were re-read:

1. `candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md`  
   SHA-256 `263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`.
2. `reviews/literal_jump_parity_projector_owner_scope_seam_review.md`  
   SHA-256 `4e25cea4858de4d4f950699d883e374e7dffa63ed74fa4eec2918eb0f800cef4`.

The originally dispatched candidate hash
`5b4df7a0ab8172ec749a466ab9d8769cdb267d85ffd3b83f8a66d5821fcdfd65`
was superseded by the conductor's metadata-only status-line update; the
PASS is against the current frozen hash above.  No state file, blind
statement, sibling report, external source, web result, or numerical
computation was used in this post-repair replay.

## 7. Recommended state effect

**Promote only the subordinate reduction (191.C5)--(191.C11), subject
to the conductor's normal graph patch and validation.**  It may be
recorded as a `proved_internal` reduction and as inconclusive evidence
for the still-open small-\(t\) owner.  Keep (191.C12) open with exact
deficit \(Y/(Qm)\), and make no state change to any downstream owner or
to any exponent.

Do not promote the bounded-array capacity control as a literal lower
bound, and do not promote the unreferenced finite diagnostic counts as
theorem evidence.  No further repair is required for the parity,
gating, endpoint, projection, complement, bounded-array, owner-scope,
or exponent seams reviewed here.
