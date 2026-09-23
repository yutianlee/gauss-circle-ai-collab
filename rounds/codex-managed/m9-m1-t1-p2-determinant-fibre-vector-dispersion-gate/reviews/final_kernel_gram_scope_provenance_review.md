# Final Round-195 kernel Gram/scope/provenance review

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Verdict: PASS
- Durable kernel SHA-256: 4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009
- Final candidate SHA-256: 81198f76dfbad6d81fc4ed88d7582ff70ce200f755b82228b6eb4650c4996d72
- Repaired reconciliation SHA-256: 3ff78bbb5f491ec4dfb30ae05123dfcecf8a93e38e17d7fee1c124c5c45b9436
- Shared-state mutation: none

## 1. Result

PASS.  The durable kernel
proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md is
mathematically identical to the final candidate on Sections 1--6 and on
every formula in Section 7.  The only candidate-to-kernel changes are:

1. the title and artifact-status metadata;
2. insertion of the exact final-candidate hash in the kernel header; and
3. renaming the last section from Proposed state effect to Dependencies
   and proof-state boundary, with a provenance-specific introductory
   clause.

No sign, mask, packet predicate, bound, Gram statement, exponent, or
dependency formula changed in transport.

The plus and minus defect signs pass; the fixed retained plus-mode ratio is
the repaired carry-dependent
\((-1)^{c_+(h;v)}e(a/q)\); the minus ratio is exactly one; the squarefree
quadratic-root statement is valid; and the exact open region is

\[
 P_{2,<D}\cap\mathcal P_{\rm rem}
 =
 P_2\mathbf1_{\{1\le\kappa<D_L\}}
 \mathbf1_{\{\min(Y,D_L)>H_B\mathfrak m\kappa\}}.
\tag{195.KV1}
\]

The event-Gram paragraph is scoped correctly: equal effective phase labels
must be recombined, the \(++,+-,-+,--\) blocks remain joint, and no
positive capacity is asserted to be literal lower mass.  Complete
\(P_2\), the hard-\(M_1\) owner, all parents and bridges, the target
theorem, and all exponent records remain quarantined.

## 2. Exact statement and hypotheses

The verified kernel fixes one literal accepted Round-192 hard-\(M_1\),
original-\(t=1\), \(\rho\)-large core shell \(L\ge2\), with

\[
 Q=H_B,\qquad D_L=\lceil\sqrt L\rceil,\qquad
 U=\mathfrak m q,\qquad U\mid u,
\]

and retains both orientations and frequency signs, both \(T\)-branches,
the complete anchor sum, every endpoint/event field, all zero extensions,
the physical-mask commutator, and one final real part.  Its physical mask
and cross-gcd split are

\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}},
\]

\[
 P_{2,\ge D}=P_2\mathbf1_{\{\kappa\ge D_L\}},\qquad
 P_{2,<D}=P_2\mathbf1_{\{1\le\kappa<D_L\}}.
\tag{195.KV2}
\]

The fixed packet includes the height scale:

\[
 p=(\kappa,u,\mathfrak m,q,a,J,Y,\sigma).
\tag{195.KV3}
\]

Thus the packet sectors are well typed:

\[
 \mathcal P_{\rm cap}
 =\{p:\kappa<D_L,\ 
       \min(Y,D_L)\le H_B\mathfrak m\kappa\},
\]

\[
 \mathcal P_{\rm rem}
 =\{p:\kappa<D_L,\ 
       \min(Y,D_L)>H_B\mathfrak m\kappa\}.
\tag{195.KV4}
\]

The kernel proves only the fixed and outer target bounds on
\(P_{2,\ge D}\) and \(\mathcal P_{\rm cap}\), together with the exact
open complement (195.KV1) and a method no-go for coefficient-blind or
within-row determinant/anchor dispersion there.

## 3. Proof or derivation

### 3.1 Candidate-to-kernel mathematical consistency

A byte diff between the final candidate and durable kernel has exactly
three metadata/proof-state hunks: the title/header, the Section 7 heading,
and the first sentence under that heading.  From the beginning of
Section 1 through the end of Section 6 the mathematical bytes are
identical.  The numbered state-effect list and terminal label in Section 7
are also identical.  The kernel header records the actual final candidate
hash

\[
 81198f76dfbad6d81fc4ed88d7582ff70ce200f755b82228b6eb4650c4996d72,
\]

and the actual starting-graph hash

\[
 815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89.
\]

### 3.2 Defect signs

In the plus chart,

\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,\quad h=Sv-Uw,
\]

\[
 \delta_+=\kappa(U-v)-2w,\qquad
 \eta_+=\kappa(U-v)+2S.
\]

Therefore

\[
 g\delta_+=d-gm,\qquad g\eta_+=d'-gm',
\]

\[
 2h=v\eta_++U\delta_+-\kappa(U^2-v^2).
\tag{195.KV5}
\]

Since \(\eta_+-\delta_+=2(S+w)>0\), lower closeness and upper failure
force \(g\eta_+>D_L\).

In the minus chart,

\[
 d'=\kappa gU,\quad d=g(\kappa U+2S),\quad
 m=\kappa v,\quad m'=\kappa v+2w,\quad h=Uw-vS,
\]

\[
 \delta_-=\kappa(U-v)+2S,\qquad
 \eta_-=\kappa(v-U)+2w.
\]

Hence

\[
 g\delta_-=d-gm,\qquad -g\eta_-=d'-gm',
\]

\[
 2h=U\eta_--v\delta_-+\kappa(U^2-v^2).
\tag{195.KV6}
\]

Because \(\delta_-+\eta_-=2(S+w)>0\), lower closeness rules out a
negative far \(\eta_-\); upper failure gives \(g\eta_->D_L\), while the
raw upper defect is negative.  The kernel signs exactly match the final
candidate and reconciliation.

### 3.3 Anchor-character ratios

For the retained plus mode, the factor is
\((-1)^tz_{+,v}^{h}\) with
\(z_{+,v}=e(a\overline v_q/q)\).  The legal far step sends
\(S\mapsto S+1\), \(h\mapsto h+v\).  If
\(c_+(h;v)\in\{0,1\}\) is the canonical-anchor wrap, then \(t\) changes
by \(c_+\) and

\[
 \frac{(-1)^{t+c_+}z_{+,v}^{h+v}}
      {(-1)^tz_{+,v}^{h}}
 =(-1)^{c_+(h;v)}e(a/q).
\tag{195.KV7}
\]

The kernel correctly reserves the constant physical parity flip \(-1\)
for the completely recombined anchor sum.  It does not mix that identity
with a retained mode.

In the minus chart the legal step keeps \(S,t\) fixed and sends
\(h\mapsto h+U\).  Since \(U=\mathfrak m q\),

\[
 z_{-,v}^{U}
 =e(-a\overline v_qU/q)
 =e(-a\overline v_q\mathfrak m)=1.
\tag{195.KV8}
\]

Thus both repaired ratios are exact.

### 3.4 Squarefree root control

On nonzero literal support, the endpoint divisor
\(\kappa gU\) is squarefree.  Therefore \(U\) is squarefree and
\((\kappa,U)=1\).  Modulo each prime \(p\mid U\), the minus congruence

\[
 \kappa v^2+\delta v+2h\equiv0\pmod p
\]

has at most two roots because \(\kappa\not\equiv0\pmod p\).  The Chinese
remainder theorem gives

\[
 \#\{v\bmod U:
 \kappa v^2+\delta v+2h\equiv0\pmod U\}
 \le2^{\omega(U)}
 \ll_\varepsilon U^\varepsilon.
\tag{195.KV9}
\]

The plus fibre retains its divisor-bound multiplicity.  The kernel
correctly treats (195.KV9) only as algebraic multiplicity control and not
as a missing-power estimate.

### 3.5 Exact packet complement and capacity boundary

For \(\kappa<D_L\), the close congruence has
\(O(1+\kappa D_L/L)=O(1)\) sites per row and height.  The fixed-height
count gives \(YuX^\varepsilon\), the independent all-height determinant
count gives \(D_LuX^\varepsilon\), and the accepted terminal/Fejer pieces
give \(O(\kappa uX^\varepsilon)\).  Hence

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon.
\tag{195.KV10}
\]

When \(\min(Y,D_L)\le H_B\mathfrak m\kappa\), (195.KV10) is bounded by
the fixed target \(H_B\mathfrak m\kappa uX^\varepsilon\).  Equality is
safe, so the strict reverse inequality in (195.KV1) is the exact open
packet complement.

The outer lift
\(c_{\mathfrak m q}(\mathfrak m a)=\mathfrak m^{-1}c_q(a)\) cancels
\(\mathfrak m\), while the \(a\)-mass, divisor choices, and \(J\)-bands
cost only logarithms.  Restricting the positive accepted outer ledger to
\(\mathcal P_{\rm cap}\) deletes terms.  Therefore

\[
 H_BX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll L^2X^\varepsilon.
\tag{195.KV11}
\]

This is an upper capacity bound.  No step asserts a nonzero coefficient,
a lower Gram diagonal, or literal lower mass.

### 3.6 Same-site and four-orientation Gram

At a transported common site, with \(B=F\Lambda\Psi\) and
\(\chi=(-1)^\nu\), the physical mask obeys

\[
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
  +\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\tag{195.KV12}
\]

After removing the already safe Fejer-change line, the two current
equal-phase channels recombine to
\(P_hF_-\Lambda_h\Psi_h\).  The carry, previous-phase part of the phase
difference, and mask-commutator channels recombine to
\(-\chi P_-^{\rm tr}F_-\Lambda_-^{\rm tr}\Psi_-^{\rm tr}\).  Thus exact
same-site recombination returns the original masked non-Fejer jump.

The all-ones \(2\times2\) and \(3\times3\) descriptions concern equal
effective phase labels, not equal endpoint coefficients.  The actual
cross-row form retains \(++,+-,-+,--\), with the \(-+\) block adjoint to
\(+-\), and keeps endpoint products, radical phases, Fejer factors,
masks, carries, births/deaths, and cross-event terms before positive
norms.  The kernel claims no estimate for this full Gram on (195.KV1).

### 3.7 Scope, exponent, and provenance boundary

The kernel supports only the large-\(\kappa\) sector, the packet-level
absolute-capacity sector, their exact complement, and the scoped method
no-go.  It explicitly excludes complete \(P_2\), \(P_1\), complete
original \(t=1\), every original \(t\ge2\) range, the remaining
hard-\(M_1\) owner, both \(M_1\) parents, GAR, all \(M_2\) parents,
endpoint uniformity, M9, both final bridges, and the Gauss-circle target.
The internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), and target \(1/4\) exponent records are
unchanged.

The direct prerequisite named in the kernel is the accepted Round-193
gcd-scaled close-sector kernel.  Its named dependencies are the accepted
Round-192 Farey-covector kernel and the physical primitive chart in the
residual Fejer tangent-gcd kernel.  The three frozen Round-195 claimant
reports exist at their reconciled hashes.  The blind report is restricted
to algebra/method-boundary evidence and is explicitly denied positive or
literal-lower-mass force.

## 4. First doubtful or unproved step

No audited kernel seam fails.  The first unproved mathematical step is
exactly the coefficient-sensitive joint four-block Gram estimate on
(195.KV1), after same-site source recombination and before separate
orientation norms.

The positive-capacity multiplier

\[
 \frac{\min(Y,D_L)}{H_B\mathfrak m\kappa}>1
\]

on \(\mathcal P_{\rm rem}\) is not a lower bound.  The kernel correctly
does not infer that the literal vectors attain it, and it makes no
complete-\(P_2\) or downstream conclusion.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| candidate mathematical-body identity | PASS.  The diff contains metadata/proof-state wording only; no formula changed. |
| plus defect sign | PASS.  Equation (195.KV5) has positive far defect \(g\eta_+>D_L\). |
| minus defect sign | PASS.  Equation (195.KV6) has positive \(\eta_-\) and negative raw upper defect. |
| plus fixed-mode carry ratio | PASS.  Equation (195.KV7) is carry-dependent and level-correct. |
| minus fixed-mode ratio | PASS.  Equation (195.KV8) is exactly one. |
| squarefree quadratic-root bound | PASS.  Equation (195.KV9) follows prime by prime and by CRT. |
| packet tuple and \(\mathcal P_{\rm rem}\) | PASS.  \(Y\) is included in \(p\); equality is safe and the strict reverse is the exact open region. |
| fixed and outer capacity | PASS.  Equations (195.KV10)--(195.KV11) have no hidden \(Y,q,J,U,\mathfrak m\), or lift power. |
| same-site event Gram | PASS.  Equal-phase channels recombine to the original masked jump; source labels are not falsely orthogonalized. |
| four orientation blocks | PASS.  \(++,+-,-+,--\) remain joint before positive norms. |
| capacity versus literal mass | PASS.  Every capacity statement is upper-only; no literal lower mass is asserted. |
| complete-\(P_2\) and owner quarantine | PASS.  The open owner and every downstream node remain unchanged. |
| exponent quarantine | PASS.  The \(1/3\), \(0.3144831759740614\ldots\), and \(1/4\) records are unchanged. |
| provenance metadata | PASS.  Campaign, round, starting graph, final candidate hash, prerequisites, evidence role, and State-Patch boundary agree. |

## 6. Dependencies and exact artifacts used

1. proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md,
   SHA-256
   4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009.
2. candidates/formalized_hard_m1_t1_p2_large_kappa_sector.md,
   SHA-256
   81198f76dfbad6d81fc4ed88d7582ff70ce200f755b82228b6eb4650c4996d72.
3. reviews/conductor_round195_report_reconciliation.md,
   SHA-256
   3ff78bbb5f491ec4dfb30ae05123dfcecf8a93e38e17d7fee1c124c5c45b9436.
4. reports/literal_p2_determinant_fibre_vector_attack.md,
   SHA-256
   c617c18c959792622e3df9fe3eb06f47ba61c6948be77f8617c83bda96302879.
5. reports/p2_gram_diagonal_collision_hostile_audit.md,
   SHA-256
   52de40ade4e243cca9e0c50edfee5f913c8120a488407b4f39fe951f22d9b8fb.
6. reports/blind_p2_determinant_fibre_rederivation.md,
   SHA-256
   29ae2a518cf61fe5f7f43369d4d51a52b71a535dae63717801874bf7ffc935df.
7. reviews/literal_gram_nogo_owner_scope_seam_review.md,
   SHA-256
   5b37315c66bd637c127cc8f3fddbb7f94ed14f9f94955c685f90a5960120c197.
8. reviews/literal_gram_capacity_postrepair_verification.md,
   SHA-256
   515dbe0e8b48ebb727a156cfe666e63dc4bdad395dd769bcc9aa0d9df8ba946a.
9. proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md,
   SHA-256
   470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83.
10. proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md,
    SHA-256
    301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325.
11. proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md,
    SHA-256
    7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2.
12. proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md,
    SHA-256
    4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160.
13. state/proof_obligations.yml, SHA-256
    815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89.
14. state/active_campaign.yml, SHA-256
    7a6762a4030410bce88305638367821bc9280dc2f88f1b201e3403594e41e00d.
15. protocol.md, SHA-256
    f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.

No diagnostic artifact was created.  No kernel, candidate, reconciliation,
state, synthesis, or sibling artifact was edited.

## 7. Recommended state effect

PROMOTE the durable kernel as evidence for exactly one subordinate
proved-internal node, subject to the remaining campaign controls and a
mechanically valid Round-195 State Patch:

1. retain \(P_{2,\ge D_L}\) and \(\mathcal P_{\rm cap}\) as target-safe;
2. record (195.KV1), the unresolved multiplier, and the within-row
   self-return as the exact remaining seam;
3. retain the squarefree root bound and event-Gram no-go only at their
   stated algebraic/method scope;
4. do not infer literal lower mass or complete \(P_2\); and
5. leave the hard-\(M_1\) owner, every parent and bridge, the target
   theorem, and all exponent records unchanged.
