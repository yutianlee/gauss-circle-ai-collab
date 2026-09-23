# Final kernel normalization and formalization review

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Round: 196
- Kernel:
  `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md`
- Kernel SHA-256:
  `dd1da266a32701f3e6f727feeec8868247a9aac6f56e36e613f3e721fc8b5ee8`
- Formal candidate SHA-256:
  `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`
- Verdict: **PASS**
- Numerical theorem evidence: none

## 1. Result

**PASS.** The current durable kernel is an exact formalization of the
verified Round-196 candidate at its stated scope. It preserves:

1. the K185 canonical least-residue anchor and affine parity;
2. the K187 exact-conductor normalization
   \(\mathfrak m^{-1}c_q(a)(-1)^t\);
3. both determinant orientation signs and the primitive modulus-\(4q\)
   shadow algebra;
4. the canonical \(\beta\)/literal \(\gamma\) interface;
5. the distinction between absence of a live-to-live wrap and survival of
   the live/dead zero-extension boundary atom;
6. both parity and physical-mask product-rule signs; and
7. the candidate's route-scoped no-go, capacity-only status, owner boundary,
   and exponent quarantine.

The current K196.10 includes
\(0\le S_{0,\omega}(h)<U\), so the affine index and wrap indicator are
unique. The statement also says precisely that the only formal wrap carrying
\(z_{q,a}\) is a live/dead event supplying no paired denominator
cancellation. No normalization or provenance defect remains.

## 2. Exact statement and hypotheses

The kernel fixes the accepted Round-192 core, imposes

\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}}
\tag{R196.1}
\]

on the physical source before Fourier expansion and height differencing,
and restricts to

\[
 \kappa<D_L,\qquad
 M:=\min(Y,D_L)>Q\mathfrak m\kappa,\qquad Q=H_B.
\tag{R196.2}
\]

The exact-conductor fast packet is

\[
\begin{gathered}
 U=\mathfrak m q>4Q,\qquad k=\mathfrak m a,\qquad
 q>Q,\qquad \mathfrak m|a|_q>Q,\qquad Q\mathfrak m<Y,\\
 (a,q)=1,\qquad U\mid u,\qquad g=u/U,\qquad
 (u,v)=1,\qquad (U,h)=1,\qquad \kappa,g,U\ {\rm odd},
\end{gathered}
\tag{R196.3}
\]

together with

\[
 j_q(a,v)=|a\bar v_q|_q>
 \min\!\left\{\frac{q-1}{2},
 \left\lfloor\frac{Q\mathfrak m q}{Y}\right\rfloor\right\},
\qquad J\le j_q(a,v)<2J.
\tag{R196.4}
\]

Thus \((U,v)=1\), \(q\) is odd, and all displayed inverses exist. The
canonical and literal inverse data are separated by

\[
 v_0=[v]_U,\qquad v=v_0+nU,
\tag{R196.5}
\]

\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},\qquad
 \rho v-\gamma U=1,\qquad \gamma=\beta+n\rho.
\tag{R196.6}
\]

The Round-192 Farey selector uses

\[
 |c\beta-d\rho|>T,\qquad
 |\rho|\ge(A+1)(T+1)
\tag{R196.7}
\]

when \(T\ge1\), whereas \(\gamma\) is reserved for literal K191
transport. At \(T=0\), the complete inherited \(|\rho|>0\) remainder is
retained.

Finally, for \(\epsilon_+=1,\epsilon_-=-1\),

\[
 S=S_{0,\omega}(h)+Ut,\qquad
 0\le S_{0,\omega}(h)<U,\qquad
 S_{0,\omega}(h)\equiv
 \epsilon_\omega\bar v_Uh\pmod U.
\tag{R196.8}
\]

The literal atom is exactly

\[
 \boxed{\mathfrak m^{-1}c_q(a)(-1)^t
 e(\epsilon_\omega a\bar v_qh/q)B_{\omega,\sigma}(h,t),}
\qquad
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\tag{R196.9}
\]

## 3. Proof and derivation

### K185/K187 normalization

K185.27 gives \((gU,v)=1\), \((U,h)=1\), and odd
\(\kappa,g,U\). K185.30--K185.31 give the two least-residue anchors

\[
 S_{0,+}\equiv\bar v_Uh,\qquad
 S_{0,-}\equiv-\bar v_Uh\pmod U,\qquad
 S=S_{0,\omega}+Ut.
\tag{R196.10}
\]

K185.36 has
\((-1)^{S_{0,\omega}}\sum_t(-1)^tB_{\omega,\sigma}(t)\).
K187 Fourier-expands the first factor:

\[
 E_U(S_0)=(-1)^{S_0}
 =\sum_{r\bmod U}c_U(r)e(rS_0/U).
\tag{R196.11}
\]

For \(k=(U/q)a=\mathfrak m a\), K187.15--K187.16 give

\[
 c_U(k)=\frac qU c_q(a)=\mathfrak m^{-1}c_q(a),
\qquad
 e(\epsilon_\omega k\bar v_Uh/U)
 =e(\epsilon_\omega a\bar v_qh/q).
\tag{R196.12}
\]

Hence kernel (K196.11) is the literal atom. It correctly leaves
\((-1)^t\) in the affine sum and does not replace it by \((-1)^S\).

### Determinant signs and primitive \(4q\) shadow

The kernel retains

\[
\begin{array}{ll}
 2h=v\eta_+ +U\delta_+-\kappa(U^2-v^2),
 &x=\kappa v+\eta_+=d'/g,\\
 2h=U\eta_- -v\delta_-+\kappa(U^2-v^2),
 &x=\kappa v+\delta_-=d/g.
\end{array}
\tag{R196.13}
\]

Modulo \(q\mid U\), the plus row gives
\(2h\equiv vx\pmod q\), and the minus row gives
\(2h\equiv-vx\pmod q\). Therefore

\[
 \epsilon_\omega\bar v_qh\equiv\bar2_qx\pmod q
\tag{R196.14}
\]

in both orientations. Since \(x=\kappa U+2S\) and \(\kappa U,x\) are
odd,

\[
 (-1)^S=\chi_4(\kappa U)\chi_4(x).
\tag{R196.15}
\]

This proves the parity-restored shadow, not the literal atom. With

\[
 b_{q,a}\equiv q+4a\bar2_q\pmod{4q},
\tag{R196.16}
\]

\(b_{q,a}\) is odd and
\(b_{q,a}\equiv2a\not\equiv0\pmod p\) for every \(p\mid q\).
Thus \((b_{q,a},4q)=1\). Its step-two ratio and scalar identity are

\[
 z_{q,a}=-e(a/q),\qquad
 (1-z_{q,a})c_q(a)=\frac{2e(a/q)}q.
\tag{R196.17}
\]

All orientation and carrier signs agree with the candidate and the exact
determinant charts.

### Literal parity, convolution, and wrap

Oddness of \(U\) gives

\[
 (-1)^S=E_U(S_{0,\omega})(-1)^t,\qquad
 (-1)^t=E_U(S_{0,\omega})(-1)^S.
\tag{R196.18}
\]

The literal on-shell factor therefore contains the extra
\(E_U(S_{0,\omega})\). Keeping the outside fixed-mode coefficient gives

\[
\mathfrak m^{-1}c_q(a)E_U(S_0)e(kS_0/U)
=\mathfrak m^{-1}c_q(a)
\sum_{r\bmod U}c_U(r)e((r+k)S_0/U).
\tag{R196.19}
\]

The right-side weights are products
\(\mathfrak m^{-1}c_q(a)c_U(r)\), not original shifted packet weights.
Consequently the multiplication mixes exact conductors and packet
partitions; full recombination restores physical parity and removes the
distinguished coefficient.

Under \(S\mapsto S+1\), canonical reduction gives

\[
 (-1)^{\mathbf1_{\{S_0=U-1\}}}e(a/q).
\tag{R196.20}
\]

Live support makes \(S_0\) a unit modulo \(U\). Every live-to-live edge
is therefore nonwrap and has ratio \(e(a/q)\). The formal wrap carrying
\(-e(a/q)\) lands at \(S_0=0\), hence at a height divisible by \(U\);
it is live/dead, not live-to-live. Zero extension retains this boundary
atom with the original coefficient and supplies no paired denominator
cancellation. The kernel's statement and K196.4 use this exact wording.

For \(a=(q-1)/2\),

\[
 |(1-e(a/q))c_q(a)|
 =\frac2q\cot\!\left(\frac{\pi}{2q}\right)\asymp1,
\tag{R196.21}
\]

which is correctly labelled a coefficient-level method falsifier rather
than literal lower mass.

### Product-rule signs and genuine event

With
\(\Delta_2B=B(x)-B(x-2)\), \(B^-=B(x-2)\), and
\(E_U^-=E_U(S_0(x-2))\), direct expansion gives

\[
 \Delta_2(E_UB)
 =E_U\Delta_2B+(E_U-E_U^-)B^-,
\tag{R196.22}
\]

and hence

\[
 E_U\Delta_2B
 =\Delta_2(E_UB)-(E_U-E_U^-)B^-.
\tag{R196.23}
\]

The solved commutator has the required minus sign. On live-to-live
nonwrap edges its coefficient has modulus \(2\); at the wrap the
live/dead boundary replaces the paired edge.

The physical-mask product rule is also exact:

\[
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
  +\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\tag{R196.24}
\]

The genuine transport uses \(\gamma\):

\[
 (S,w)\mapsto
 (S-\epsilon_\omega\rho,w-\epsilon_\omega\gamma),
\qquad
 x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\rho.
\tag{R196.25}
\]

For \(T\ge1\), \(|\rho|>1\); for \(T=0\), unit-inverse rows are not
silently promoted without their complement. The endpoint tables,
\((2gC_v,2g)\) displacement, opposite \(\pm v\) height shifts, and raw
Fejer displacement \(2\kappa gv/R_0\) all agree with the verified
candidate. Thus no accepted common literal \(\Delta_2\) is asserted.

### Provenance and scope

The kernel metadata names the verified candidate hash
`5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`.
Its equations K196.1--K196.38 preserve the candidate's physical mask,
fast predicate, \(\beta/\gamma\) repair, literal carrier, primitive-shadow
quarantine, live/dead boundary, event ledger, fixed deficit, conditional
outer assembly, and no-lower-mass qualifier.

The review-provenance paragraph is consistent with the Round-196
artifacts: normalization/live-wrap verification, commutator/power/owner
verification, blind derivation with post-unmask review, and conductor
reconciliation all exist. The kernel claims only
`on_shell_carrier_denominator_self_return_no_go` and does not convert
method controls into claimant evidence.

## 4. First doubtful or unproved step

No doubtful normalization, sign, support, or provenance step remains in
the current kernel. The first genuinely unproved analytic step lies outside
its no-go claim: a coefficient-sensitive joint
\((++,+-,-+,--)\) cross-row estimate for the complete literal region

\[
 \kappa<D_L,\qquad M>Q\mathfrak m\kappa,
\tag{R196.26}
\]

retaining every endpoint, phase, mask, carry, birth/death, coprimality,
and zero-extension term before positive norms and gaining
\(M/(Q\mathfrak m\kappa)\).

## 5. Required controls and outcomes

1. **Kernel hash and text integrity — PASS.** SHA-256 is
   `dd1da266a32701f3e6f727feeec8868247a9aac6f56e36e613f3e721fc8b5ee8`;
   no non-line ASCII control characters occur.
2. **K185 canonical anchor — PASS.** K196.10 has the least-residue range,
   both orientation signs, and the unique affine decomposition.
3. **K187 exact-conductor normalization — PASS.** K196.11 and
   K196.20--K196.23 keep \(\mathfrak m^{-1}c_q(a)(-1)^t\), the outside
   coefficient, and the non-packet convolution weights.
4. **Determinant and \(4q\) algebra — PASS.** K196.13--K196.19 have the
   exact plus/minus signs, primitive numerator, multiplier, and scalar
   identity.
5. **\(\beta/\gamma\) interface — PASS.** The Farey selector uses
   canonical \(\beta\); K191 transport uses \(\gamma=\beta+n\rho\).
6. **Live/dead wrap wording — PASS.** The kernel denies only a
   live-to-live cancelling pair and retains the unpaired zero-extension
   boundary atom.
7. **Product-rule signs — PASS.** Both the parity identity K196.26--K196.27
   and physical-mask identity K196.30 expand exactly.
8. **Candidate provenance — PASS.** The embedded candidate hash, equation
   content, route-scoped status, power deficit, owner boundary, and exponent
   quarantine match the final verified candidate.
9. **Claim scope — PASS.** No target-safe sector, literal lower bound,
   parent theorem, bridge, or exponent is promoted.

## 6. Dependencies and exact artifacts used

- `protocol.md` —
  `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
- `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md` —
  `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160`.
- `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md` —
  `a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2`.
- `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md` —
  `7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2`.
- `proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md` —
  `301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325`.
- `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md` —
  `4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009`.
- `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md` —
  `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`.
- `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/on_shell_normalization_live_wrap_postrepair_verification.md` —
  `281782967401cb142f95d4a0d8892b846520689851e31d18104a6a40bea02641`.
- `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/commutator_power_owner_scope_final_verification.md` —
  `273afb36679a4b1f24f2dbc7708660079ef474c19130618a6fd5f3d892054cfa`.
- `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/conductor_round196_report_reconciliation.md` —
  `208b69cb7905b41e08d4dc004034c1a50434ef8d64175656dad060640ef772d3`.
- `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md` —
  `dd1da266a32701f3e6f727feeec8868247a9aac6f56e36e613f3e721fc8b5ee8`.

No web source, numerical experiment, or computation is used as theorem
evidence.

## 7. Recommended state effect

**PASS the durable kernel as an exact route-scoped
normalization/support no-go.** It may record only that the proposed bare
on-shell carrier-denominator mechanism fails at the literal
exact-conductor normalization and returns through conductor mixing,
live/dead boundary support, and parity/physical commutators.

Retain the complete \(P_2\) remainder open and attach only inconclusive
no-go evidence to the existing hard-M1 small-\(t\) owner. Do not promote
\(P_1\), complete original \(t=1\), another original-\(t\) incidence,
either M1 parent, GAR, any M2 parent, endpoint uniformity, M9, either
bridge, the quarter theorem, or any exponent. This review makes no
shared-state edit.
