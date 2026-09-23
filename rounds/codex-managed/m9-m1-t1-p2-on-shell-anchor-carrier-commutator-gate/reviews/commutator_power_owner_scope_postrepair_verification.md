# Round 196 commutator, power, owner, and scope post-repair verification

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Candidate verified:
  `candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md`
- Candidate SHA-256:
  `d996d60d09ed8b6b58cf9cc3e7462215843780f00938840ed425247ec92e9bf9`
- Starting graph SHA-256:
  `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Numerical theorem evidence: none

## 1. Result

**Verdict: REPAIR.** The repaired candidate correctly implements every
operator, displacement, commutator, power, no-submask, owner, and exponent
repair from the first seam review except the exact R192 Farey-coordinate
interface. The remaining defect is localized but mathematically real:
(196.K4b) uses

\[
 |c\gamma-d\rho|>T
\tag{196.V1}
\]

where the accepted R192 core uses

\[
 |c\beta-d\rho|>T.
\tag{196.V2}
\]

Here \(\beta\) is the canonical quotient attached to
\(v_0=[v]_U\), whereas \(\gamma\) is the literal transport quotient.
They differ by \(n\rho\) when \(v=v_0+nU\). Thus (196.V1) is not a
renaming of (196.V2); it defines a different row selector. The candidate
also omits the signed normalization that makes \(\rho\) unique and does
not display the K189 fast inequality
\(j_q(a,v)>T_Q(\mathfrak m,q;Y)\), although the opening inheritance
sentence imports it.

All other demanded repairs pass. In particular, the candidate now:

- allows \(\rho=\pm1\) on \(T=0\) and does not infer a uniform nonunit
  displacement there;
- states the directional law
  \(x_{h-1}^{\rm tr}=x_h-2\epsilon_\omega\rho\);
- places \(P_2\) before Fourier expansion and differencing and keeps the
  orientations, frequency signs, literal labels, conjugations, and four
  cross-row blocks under one outer real part;
- separates the genuine K191 event from the artificial adjacent-\(S\)
  control, with correct endpoint and Fejer displacement vectors;
- retains all mask, arithmetic, carry, affine birth/death, phase, and
  zero-extension commutators and rejects all proper-shadow escapes;
- preserves the exact fixed-to-outer deficit and capacity-only language;
  and
- leaves every owner, parent, bridge, theorem, and exponent unchanged.

After the canonical \((\rho,\beta,\gamma)\) repair and the explicit fast
predicate stated in Section 7, the candidate can pass this seam as a
route-scoped no-go. No graph promotion is justified before that repair.

## 2. Exact statement and hypotheses checked

The candidate correctly confines itself to \(X\ge2\), one nonempty
literal middle or lower hard-M1 shell \(L\ge2\), a sign
\(\sigma\in\{\pm1\}\), and

\[
 Q=H_B,\qquad R_0=\lceil L\rceil,\qquad
 D_L=\lceil\sqrt L\rceil,\qquad M=\min(Y,D_L),
\tag{196.V3}
\]

with the physical mask

\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}}
\tag{196.V4}
\]

inserted before Fourier expansion and height differencing. The frozen
open region is exactly

\[
 \kappa<D_L,\qquad M>Q\mathfrak m\kappa.
\tag{196.V5}
\]

The candidate displays the exact-conductor packet conditions

\[
 U=\mathfrak m q>4Q,\quad k=\mathfrak m a,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,\quad
 U\mid u,\quad g=u/U,\quad (u,v)=1,\quad(U,h)=1,
\tag{196.V6}
\]

the projective band \(J\le j_q(a,v)<2J\), and inherited oddness. For a
fully explicit K189 interface, it must additionally display

\[
 j_q(a,v)=|a\bar v_q|_q>
 T_Q(\mathfrak m,q;Y):=
 \min\left\{\frac{q-1}{2},
 \left\lfloor\frac{Q\mathfrak m q}{Y}\right\rfloor\right\}.
\tag{196.V7}
\]

The opening phrase “retain the exact accepted Round-192 core” imports
(196.V7), so its omission does not silently enlarge the intended object;
nevertheless, the repaired packet display is not self-contained until
(196.V7) is added.

The exact R192 quotient interface is

\[
 v_0=[v]_U\in\{1,\ldots,U-1\},\qquad v=v_0+nU,
\tag{196.V8}
\]

\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},
\tag{196.V9}
\]

and, for literal transport,

\[
 \rho v-\gamma U=1,\qquad \gamma=\beta+n\rho.
\tag{196.V10}
\]

The Farey selector uses \(\beta\), while K191 transport uses
\(\gamma\). The threshold is

\[
 T=\min\left\{\frac{U-1}{2},
 \left\lfloor\frac{Q\mathfrak m U}{Y}\right\rfloor\right\}.
\tag{196.V11}
\]

At \(T=0\), the Farey projector is zero and the complete inherited
\(|\rho|>0\) remainder stays. At \(T\ge1\), every core row must satisfy
simultaneously

\[
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A),\qquad
 |\rho|\ge(A+1)(T+1).
\tag{196.V12}
\]

Candidate (196.K4b) fails only at the \(\beta\)-versus-\(\gamma\)
entry of (196.V12), plus the omitted signed normalization (196.V9).
Its \(T=0\) convention and lower bound on \(|\rho|\) at \(T\ge1\)
are otherwise correct.

## 3. Verification derivation

### 3.1 Directional event law and \(T\)-branch control

The genuine K191 transport is

\[
 (S,w)\longmapsto
 (S-\epsilon_\omega\rho,
  w-\epsilon_\omega\gamma),
\tag{196.V13}
\]

so, for \(x=\kappa U+2S\),

\[
 x_{h-1}^{\rm tr}=x_h-2\epsilon_\omega\rho,\qquad
 x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\rho.
\tag{196.V14}
\]

Candidate (196.K19a) matches (196.V14) exactly. At \(T\ge1\),
(196.V12) forces \(|\rho|>1\), so the event cannot be a step-two
event. At \(T=0\), \(\rho=\pm1\) is not excluded and displacement of
magnitude \(2\) may occur. Candidate (196.K19a) and item 5 of Section 1
now state this correctly.

The phrase “proper submask” should be read through the candidate's explicit
no-submask rule: unit-inverse rows cannot replace the complete
\(T=0\) branch unless their literal complement is proved empty or is
estimated. No accepted lower-support theorem supplies that fact. This is
the rigorous content needed here; no lower mass of the complement is
asserted.

The plus/minus geometry also passes. The candidate has
\(x=d'/g\) as the plus far coordinate and \(x=d/g\) as the minus
close coordinate. The literal minus far step \(w\mapsto w+1\) leaves
\(x\) fixed. Hence exceptional unit-inverse rows do not create a common
literal \(\Delta_2\) on the complete two-orientation aggregate.

### 3.2 Genuine versus artificial event ledgers

Candidate (196.K19b) correctly retains the genuine physical-mask product
rule

\[
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
 +\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\tag{196.V15}
\]

It also correctly records that the K191 outer terminal and isolated
unit-height Fejer projections were already removed, while the two
coprimality flips, transported affine births/deaths, carry, ordered
endpoint arithmetic, cell/crossing, square-root phase, and both outer and
endpoint zero extensions remain. It does not identify this height-one
event with an adjacent-\(S\) operation.

For the artificial predecessor

\[
 \tau:(S,w)\longmapsto(S-1,w),\qquad
 A_0=\kappa gU,\qquad C_v=\kappa v,
\tag{196.V16}
\]

candidate (196.K19d) gives the correct ordered endpoint table

\[
\begin{array}{c|cc}
 &(N_{0,\omega},d_{0,\omega})&(N_{1,\omega},d_{1,\omega})\\ \hline
 +&(A_0(C_v+2w),A_0)&((A_0+2gS)C_v,A_0+2gS)\\
 -&((A_0+2gS)C_v,A_0+2gS)&(A_0(C_v+2w),A_0).
\end{array}
\tag{196.V17}
\]

The derived vectors

\[
 (\Delta N,\Delta d)=(2gC_v,2g),\qquad
 h_+-h_+\circ\tau=v,\qquad
 h_--h_-\circ\tau=-v
\tag{196.V18}
\]

are correct. They act on the plus upper endpoint factor and the
conjugated minus lower endpoint factor. Therefore the candidate correctly
uses “can change” for the plus-far/minus-close physical mask, divisor and
arithmetic masks, carry, affine range, endpoint product, phase, cells,
crossings, and zero extensions.

The repaired Fejer audit also passes:

\[
 |F(h)-F(h\circ\tau)|=\frac{2\kappa gv}{R_0},
\tag{196.V19}
\]

which is not the removed K191 unit-height difference
\(2\kappa g/R_0\). Candidate (196.K19f) correctly sends support
nonoverlap to an outer birth/death rather than treating it as a
common-site Fejer commutator.

### 3.3 Live carrier, no-submask controls, and lower-mass boundary

The literal exact-conductor atom, restored \(E_U(S_0)\) factor, live
multiplier, and product rule (196.K18)--(196.K18a) remain correct. The
candidate now distinguishes live-to-live nonwrap edges, where
\(|E_U-E_U^-|=2\), from live/dead wrap transitions, which survive as
zero-extension boundary atoms with the original coefficient.

The false-control paragraph passes. Consecutive support, a cumulative
primitive, unsigned or character-erased shadows, mask or
\(T\)-deletions, wrap-only restriction, arbitrary or phase-conjugated
arrays, and separate orientation norms are not claimant operators.
Candidate Section 1 also prohibits promotion of unit-inverse, wrap,
parity, mask, orientation, or \(T\)-branch submasks without their exact
complements. Capacity attainment is explicitly classified as a method
control, not literal lower mass.

### 3.4 Power, owner, and exponent ledger

The repaired fixed-to-outer ledger passes. K195 supplies only

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+M\}X^\varepsilon.
\tag{196.V20}
\]

On (196.V5), the unresolved term has exact ratio

\[
 \frac{Mu}{Q\mathfrak m\kappa u}
 =\frac{M}{Q\mathfrak m\kappa}>1.
\tag{196.V21}
\]

The candidate correctly restores
\(c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a)\),
\(\sum|c_q(a)|\ll\log(2q)\), and
\(\sum_{\mathfrak m q\mid u}1\le\tau_3(u)\). The spectral
\(\mathfrak m^{-1}\) cancels \(\mathfrak m\) only after a fixed
\(Q\mathfrak m\kappa u\) target is proved; it cannot erase (196.V21).
No positive power is hidden in \(X^\varepsilon\).

The proof-state recommendation also passes. It attaches only inconclusive
route-scoped evidence to the already open hard-M1 small-\(t\) owner,
creates no target-safe obligation, and does not promote complete
\(P_2\), \(P_1\), original \(t=1\), any other original-\(t\)
incidence, an M1 or M2 parent, GAR, endpoint uniformity, M9, a bridge, the
quarter theorem, or an exponent.

## 4. First doubtful or unproved step

The first invalid statement in the repaired candidate is (196.K4b).
From (196.V8)--(196.V10),

\[
 c\gamma-d\rho
 =c\beta-(d-cn)\rho,
\tag{196.V22}
\]

and \((c,d-cn)\) generally is not in the fixed Farey family
\(\mathcal F_A\), whose second coordinate satisfies \(0\le d\le c\).
Thus replacing \(\beta\) by \(\gamma\) changes the selector and can
change which rows are called core. This is not repaired by the true
transport identity \(\gamma=\beta+n\rho\).

The first unproved analytic step remains unchanged: a jointly signed,
coefficient-sensitive estimate for the complete literal \(P_2\)
remainder, with the actual anchor factor and all events in
(196.V15)--(196.V19) retained before positive norms, gaining the full
factor \(M/(Q\mathfrak m\kappa)\). Neither the candidate nor any reviewed
dependency proves or refutes that theorem.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `candidate_hash_and_scope` | **PASS.** Candidate hash is `d996d60d09ed8b6b58cf9cc3e7462215843780f00938840ed425247ec92e9bf9` and it stays on the exact Round-195 open \(P_2\) region. |
| `T0_unit_inverse_exception` | **PASS.** \(\rho=\pm1\) is allowed at \(T=0\); no uniform nonunit displacement is claimed there. |
| `directional_event_displacement` | **PASS.** (196.K19a) equals (196.V14). |
| `canonical_Farey_coordinate` | **FAIL/REPAIR.** (196.K4b) uses literal \(\gamma\), not canonical \(\beta\), and omits the signed normalization of \(\rho\). |
| `full_fast_packet` | **PASS BY INHERITANCE/REPAIR FOR SELF-CONTAINMENT.** The Round-192 core imports (196.V7), but the displayed packet should state it. |
| `physical_mask_before_spectral_operations` | **PASS.** Section 1 fixes the order explicitly. |
| `one_outer_real_part` | **PASS.** Both orientations, frequency signs, labels, conjugations, and cross-row blocks remain joint. |
| `genuine_vs_artificial_event` | **PASS.** (196.K19b) is separated from (196.K19c)--(196.K19f). |
| `endpoint_vectors_and_conjugation` | **PASS.** The table and vector (196.K19d)--(196.K19e) are exact. |
| `physical_and_arithmetic_masks` | **PASS.** The candidate retains possible flips and their product-rule commutators. |
| `carry_and_affine_birth_death` | **PASS.** Genuine and artificial event roles are distinguished. |
| `Fejer_displacement` | **PASS.** The \(v\)-height difference and support nonoverlap are handled correctly. |
| `square_root_phase` | **PASS.** No unproved phase regularity is asserted. |
| `outer_and_endpoint_zero_extension` | **PASS.** Both survive and are kept distinct. |
| `no_submask_escape` | **PASS.** No unit-inverse, wrap, parity, mask, \(T\)-branch, or orientation submask is promoted without its complement. |
| `false_controls_and_lower_mass` | **PASS.** Every shadow is method-only; capacity is not literal lower mass. |
| `fixed_to_outer_power_ledger` | **PASS.** All \(Q,\mathfrak m,\kappa,u,M,L,X\) powers and coefficient/divisor sums are restored. |
| `no_power_in_epsilon` | **PASS.** The positive multiplier (196.V21) is not absorbed. |
| `owner_boundary` | **PASS.** Only inconclusive evidence is assigned to the existing open owner. |
| `exponent_quarantine` | **PASS.** Every exponent and downstream theorem remains unchanged. |
| `diagnostic_only` | **PASS.** No computation was used. |

## 6. Dependencies and exact artifacts used

Only the repaired candidate, the prior seam, the current Round-196
reconciliation, and the named accepted interfaces were used:

1. `protocol.md` —
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
2. `state/proof_obligations.yml` —
   `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`;
3. `state/active_campaign.yml` —
   `8aa8f0dea94adc77f6e3e4dbc8a2b43c3a6749aefe7f95c37be0c3867e85dfab`;
4. `proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md` —
   `31092b28826b9f36ecaedfb5efc5d7625f4caa4da2cf4c37bd48389c6ac6ee58`;
5. `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md` —
   `7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2`;
6. `proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md` —
   `301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325`;
7. `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md` —
   `4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009`;
8. `reviews/commutator_power_owner_scope_seam_review.md` —
   `acd413701ce21c002a6ca0b3c8bf3d905bd262b1a4283a1ab20721096daed785`;
9. `reviews/conductor_round196_report_reconciliation.md` —
   `208b69cb7905b41e08d4dc004034c1a50434ef8d64175656dad060640ef772d3`;
10. `candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md` —
    `d996d60d09ed8b6b58cf9cc3e7462215843780f00938840ed425247ec92e9bf9`.

Items 8--10 are relative to the Round-196 campaign directory. No web
source, external result, unlisted sibling report, or computation was used.

## 7. Recommended state effect and exact repair

**Return the candidate for one canonical-coordinate repair; do not edit
the claim graph or any shared state.**

Replace the paragraph beginning “Write \(\rho v-\gamma U=1\)” and
(196.K4b) by:

\[
 v_0=[v]_U\in\{1,\ldots,U-1\},\qquad v=v_0+nU,
\tag{196.V23}
\]

\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},\qquad
 \rho v-\gamma U=1,\qquad \gamma=\beta+n\rho,
\tag{196.V24}
\]

and, for \(T\ge1\),

\[
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A),\qquad
 |\rho|\ge(A+1)(T+1).
\tag{196.V25}
\]

Use \(\beta\) only in the Farey selector and \(\gamma\) only in literal
K191 transport. Add the fast predicate (196.V7) beside the displayed
\(J\)-band. Retain the correct \(T=0\) statement and the directional
law (196.K19a). For maximal logical precision, replace “unit-inverse rows
form a proper submask” by “the unit-inverse selector cannot replace the
complete branch unless its literal complement is proved empty or
estimated.”

No other repair is required. After these changes, the formal candidate
may be retained only as an exact route-scoped normalization/support no-go
and inconclusive evidence for the already open hard-M1 small-\(t\) owner.
It still creates no target-safe node and promotes no \(P_2\), \(P_1\),
original-\(t\), parent, GAR, endpoint, M9, bridge, theorem, or exponent
claim.
