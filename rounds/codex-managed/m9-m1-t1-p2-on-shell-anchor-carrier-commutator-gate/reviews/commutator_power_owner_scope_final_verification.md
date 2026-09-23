# Round 196 commutator, power, owner, and scope final verification

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Candidate verified:
  `candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md`
- Candidate SHA-256:
  `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`
- Starting graph SHA-256:
  `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Numerical theorem evidence: none

## 1. Result

**Verdict: PASS.** The final candidate implements the canonical
\((\rho,\beta,\gamma)\) repair and the K189 fast-predicate repair
exactly, and every previously accepted operator, commutator, power, owner,
and scope repair remains intact.

The decisive checks are:

1. the signed inverse is uniquely normalized by

   \[
   \rho v_0-\beta U=1,\qquad
   -\frac{U-1}{2}\le\rho\le\frac{U-1}{2};
   \tag{196.F1}
   \]

2. the R192 Farey selector uses canonical \(\beta\):

   \[
   |c\beta-d\rho|>T;
   \tag{196.F2}
   \]

3. literal K191 transport uses \(\gamma\), with

   \[
   v=v_0+nU,\qquad
   \rho v-\gamma U=1,\qquad
   \gamma=\beta+n\rho;
   \tag{196.F3}
   \]

4. the fast packet explicitly retains

   \[
   j_q(a,v)>T_Q(\mathfrak m,q;Y)
   \tag{196.F4}
   \]

   together with its dyadic \(J\)-band; and
5. the \(T=0\) unit-inverse exception, directional event law, physical
   and artificial event ledgers, endpoint and Fejer vectors, no-submask
   controls, fixed-to-outer ledger, owner boundary, and exponent
   quarantine are unchanged and correct.

This is a PASS only for the candidate's stated route-scoped
normalization/support no-go. It proves no fixed target, strict sector,
literal lower bound, parent theorem, or exponent.

## 2. Exact statement and hypotheses

The candidate fixes \(X\ge2\), one nonempty literal middle or lower
hard-M1 shell \(L\ge2\), a sign
\(\sigma\in\{\pm1\}\), and

\[
 Q=H_B,\qquad R_0=\lceil L\rceil,\qquad
 D_L=\lceil\sqrt L\rceil,\qquad M=\min(Y,D_L).
\tag{196.F5}
\]

It places

\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}}
\tag{196.F6}
\]

on the physical source before Fourier expansion and height differencing,
and restricts to the exact open Round-195 region

\[
 \kappa<D_L,\qquad M>Q\mathfrak m\kappa.
\tag{196.F7}
\]

The displayed exact-conductor fast packet now contains

\[
 U=\mathfrak m q>4Q,\quad k=\mathfrak m a,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,
\tag{196.F8}
\]

\[
 U\mid u,\quad g=u/U,\quad (u,v)=1,\quad(U,h)=1,
\quad J\le j_q(a,v)<2J,
\tag{196.F9}
\]

with inherited oddness and

\[
 j_q(a,v)=|a\bar v_q|_q>
 \min\left\{\frac{q-1}{2},
 \left\lfloor\frac{Q\mathfrak m q}{Y}\right\rfloor\right\}.
\tag{196.F10}
\]

The candidate then separates the canonical and literal inverse data:

\[
 v_0=[v]_U\in\{1,\ldots,U-1\},\qquad v=v_0+nU,
\tag{196.F11}
\]

\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},
\tag{196.F12}
\]

\[
 \rho v-\gamma U=1,\qquad \gamma=\beta+n\rho.
\tag{196.F13}
\]

With

\[
 T=\min\left\{\frac{U-1}{2},
 \left\lfloor\frac{Q\mathfrak m U}{Y}\right\rfloor\right\},
\tag{196.F14}
\]

the \(T=0\) branch keeps the complete inherited \(|\rho|>0\)
remainder, while at \(T\ge1\) every retained row satisfies

\[
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A),\qquad
 |\rho|\ge(A+1)(T+1).
\tag{196.F15}
\]

Thus \(\beta\) appears in the Farey covector and \(\gamma\) appears
only in literal transport, exactly as R192 requires. Both orientations,
frequency signs, the full anchor aggregate, endpoint labels,
conjugations, and all four cross-row blocks remain in one complex
aggregate before the final real part. No branch or proper shadow is
silently promoted.

## 3. Proof and verification

### 3.1 Canonical quotient, transport, and displacement

Equations (196.F11)--(196.F13) imply

\[
 \rho(v_0+nU)-(\beta+n\rho)U=1,
\tag{196.F16}
\]

so the candidate's literal transport quotient is exactly compatible with
the canonical signed inverse. The previous error
\(|c\gamma-d\rho|>T\) is absent: candidate (196.K4d) uses
\(|c\beta-d\rho|>T\).

K191 transports the height-\(h\) fibre to height \(h-1\) by

\[
 (S,w)\longmapsto
 (S-\epsilon_\omega\rho,
  w-\epsilon_\omega\gamma).
\tag{196.F17}
\]

For \(x=\kappa U+2S\), the candidate correctly records

\[
 x_{h-1}^{\rm tr}=x_h-2\epsilon_\omega\rho,\qquad
 x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\rho.
\tag{196.F18}
\]

At \(T\ge1\), (196.F15) forces \(|\rho|>1\). At \(T=0\),
\(\rho=\pm1\) is not excluded, and the candidate now says only that
the unit-inverse selector cannot replace the complete branch unless its
literal complement is proved empty or estimated. This is the exact
no-submask conclusion; it asserts no lower mass for the complement.

The plus/minus roles remain correct: \(x=d'/g\) is plus-far,
\(x=d/g\) is minus-close, and the literal minus far step
\(w\mapsto w+1\) leaves \(x\) fixed. Hence no common inherited
\(\Delta_2\) exists on the complete two-orientation core.

### 3.2 Literal carrier and genuine event ledger

The literal exact-conductor atom remains

\[
 \mathfrak m^{-1}c_q(a)(-1)^t
 e(\epsilon_\omega a\bar v_qh/q)B_\omega(h,t),
\tag{196.F19}
\]

not the parity-restored \((-1)^S\) shadow. Restoring
\(E_U(S_{0,\omega})\) mixes the complete \(U\)-mode family, while
full recombination removes the distinguished coefficient. The literal
live nonwrap ratio is \(e(a/q)\); the only formal cancelling wrap lands
at \(S_0=0\) and survives only as a live/dead zero-extension boundary
atom.

The candidate also preserves the exact product rule

\[
 \Delta_2(E_UB)
 =E_U\Delta_2B+(E_U-E_U^-)B^-.
\tag{196.F20}
\]

The commutator coefficient has modulus \(2\) on live-to-live nonwrap
edges. Boundary edges are not discarded.

For a genuine persistent K191 event, candidate (196.K19b) retains

\[
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
  +\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\tag{196.F21}
\]

It correctly distinguishes the already removed outer terminal and
unit-height Fejer projections from the surviving coprimality flips,
transported affine births/deaths, carry, ordered endpoint arithmetic,
cell/crossing, square-root phase, and outer and endpoint zero extensions.

### 3.3 Artificial adjacent-\(S\) ledger

For

\[
 \tau:(S,w)\longmapsto(S-1,w),\qquad
 A_0=\kappa gU,\qquad C_v=\kappa v,
\tag{196.F22}
\]

candidate (196.K19d) retains the exact endpoint pairs

\[
\begin{array}{c|cc}
 &(N_{0,\omega},d_{0,\omega})&(N_{1,\omega},d_{1,\omega})\\ \hline
 +&(A_0(C_v+2w),A_0)&((A_0+2gS)C_v,A_0+2gS)\\
 -&((A_0+2gS)C_v,A_0+2gS)&(A_0(C_v+2w),A_0).
\end{array}
\tag{196.F23}
\]

The derived vectors are

\[
 (\Delta N,\Delta d)=(2gC_v,2g),\qquad
 h_+-h_+\circ\tau=v,\qquad h_--h_-\circ\tau=-v.
\tag{196.F24}
\]

They act on the plus upper endpoint and conjugated minus lower endpoint.
The candidate therefore correctly retains possible changes of the
plus-far/minus-close physical mask, divisor and arithmetic masks, carry,
affine support, endpoint product, phase, cells, crossings, and both
zero-extension families.

Its Fejer vector is also exact:

\[
 |F(h)-F(h\circ\tau)|=\frac{2\kappa gv}{R_0},
\tag{196.F25}
\]

not the removed unit-height difference \(2\kappa g/R_0\). Support
nonoverlap is routed to an outer birth/death.

### 3.4 Controls, powers, and proof-state boundary

The candidate rejects consecutive support, cumulative primitives,
unsigned and character-erased shadows, mask or \(T\)-deletions,
wrap-only restrictions, arbitrary or phase-conjugated arrays, and
separate orientation norms as claimant evidence. Capacity attainment is
explicitly method-only, not literal lower mass.

The fixed estimate remains

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+M\}X^\varepsilon,
\tag{196.F26}
\]

with exact open multiplier

\[
 \frac{M}{Q\mathfrak m\kappa}>1.
\tag{196.F27}
\]

The candidate restores the exact lift, coefficient \(\ell^1\) mass,
projective bands, and divisor ledger. It applies the
\(\mathfrak m^{-1}\) cancellation only after a fixed
\(Q\mathfrak m\kappa u\) target is proved and hides no positive power
in \(X^\varepsilon\).

Finally, it assigns only inconclusive evidence to the existing open
hard-M1 small-\(t\) owner. It creates no target-safe node and changes no
parent, bridge, theorem, or exponent.

## 4. First doubtful or unproved step

No invalid or doubtful step remains in the candidate's stated
normalization/support no-go. In particular, the former first defect is
repaired: the Farey selector uses canonical \(\beta\), literal transport
uses \(\gamma\), and \(\rho\) is the uniquely normalized signed inverse.

The first genuinely unproved analytic step lies outside the candidate's
claim: a jointly signed, coefficient-sensitive estimate for the complete
literal \(P_2\) remainder, retaining the actual anchor factor and every
event in (196.F21)--(196.F25) before positive norms and gaining
\(M/(Q\mathfrak m\kappa)\). The candidate explicitly leaves this theorem
open and therefore does not overclaim.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `candidate_hash` | **PASS.** SHA-256 is `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`. |
| `canonical_signed_inverse` | **PASS.** (196.K4a)--(196.K4b) define \(v_0\) and uniquely normalize \(\rho\). |
| `Farey_uses_beta` | **PASS.** (196.K4d) uses \(|c\beta-d\rho|>T\). |
| `transport_uses_gamma` | **PASS.** (196.K4b) and (196.K19) use \(\gamma=\beta+n\rho\) for literal transport. |
| `K189_fast_predicate` | **PASS.** (196.K3a) states the exact fast lower bound beside the \(J\)-band. |
| `T0_unit_inverse_exception` | **PASS.** \(\rho=\pm1\) is permitted and no complement is silently discarded. |
| `directional_displacement` | **PASS.** (196.K19a) has the exact sign and direction. |
| `physical_mask_order` | **PASS.** \(P_2\) precedes Fourier expansion and height differencing. |
| `one_outer_real_part` | **PASS.** All orientations, signs, labels, conjugations, and cross-row blocks remain joint. |
| `genuine_vs_artificial_events` | **PASS.** (196.K19b) is separated from (196.K19c)--(196.K19f). |
| `endpoint_vectors` | **PASS.** The ordered pairs and displacement (196.K19d)--(196.K19e) are exact. |
| `mask_arithmetic_carry_birth_death` | **PASS.** All possible commutators remain literal. |
| `Fejer_displacement` | **PASS.** The raw \(v\)-height vector and nonoverlap event are correct. |
| `phase_and_zero_extensions` | **PASS.** No phase regularity is invented and both zero extensions remain. |
| `no_submask_and_false_controls` | **PASS.** No shadow is promoted without its exact complement. |
| `capacity_not_lower_mass` | **PASS.** The method boundary is explicit. |
| `fixed_to_outer_powers` | **PASS.** All \(Q,\mathfrak m,\kappa,u,M,L,X\) powers and sums are restored. |
| `no_power_in_epsilon` | **PASS.** The multiplier (196.F27) remains explicit. |
| `owner_scope` | **PASS.** Only the existing open small-\(t\) owner receives inconclusive evidence. |
| `exponent_quarantine` | **PASS.** No downstream claim or exponent changes. |
| `diagnostic_only` | **PASS.** No computation was used. |

## 6. Dependencies and exact artifacts used

Only the final candidate, the two prior seam reviews, the current
Round-196 reconciliation, and the named accepted interfaces were used:

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
9. `reviews/commutator_power_owner_scope_postrepair_verification.md` —
   `51b04cb8cf2fba130e37696659e055b071aecb18baa8b18cc06f7ef5d8de786a`;
10. `reviews/conductor_round196_report_reconciliation.md` —
    `208b69cb7905b41e08d4dc004034c1a50434ef8d64175656dad060640ef772d3`;
11. `candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md` —
    `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`.

Items 8--11 are relative to the Round-196 campaign directory. No web
source, external result, unlisted sibling report, or computation was used.

## 7. Recommended state effect

**PASS the formal candidate for conductor synthesis as a route-scoped
normalization/support no-go.** The candidate may support only the
following state effect after the conductor's independent graph validation:

1. record the exact parity-restoration, live-wrap, commutator, and
   no-common-\(\Delta_2\) obstruction to the proposed
   carrier-denominator mechanism;
2. retain the complete \(P_2\) remainder open;
3. attach only inconclusive evidence to the already open hard-M1
   small-\(t\) owner; and
4. leave \(P_1\), complete original \(t=1\), every other original
   \(t\) incidence, either M1 parent, GAR, every M2 parent, endpoint
   uniformity, M9, both bridges, the quarter theorem, and every exponent
   unchanged.

No shared-state edit is made by this verification.
