# Round-195 literal Gram/no-go and owner-scope seam review

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Review verdict: REPAIR
- Candidate reviewed: SHA-256 6dfa01ba15e9a64039bcce6a7b8bab788676d55c567b4b9c1c3e5dbb214d9fde
- Conductor reconciliation reviewed: SHA-256 0ed89615d9eb5480aa540eeb362727c2fa65a05bbc12956599a5b6040195f4ec
- Shared-state mutation: none

## 1. Result

The strict positive sector \(P_{2,\ge D}\) and its exact physical
complement \(P_{2,<D}\) survive this review.  The two defect signs, the
same-site event recombination, the \(O(1)\) length of a fixed-row far
fibre, the necessity of the four orientation Gram blocks, the
capacity-versus-mass disclaimer, and the owner/exponent quarantine all
pass.

Two statements in the candidate/reconciliation require repair.

First, the claimed constant plus anchor-character ratio
\(-e(a/q)\) is not the ratio of a fixed retained Round-191 anchor mode.
For the legal plus step it is

\[
 (-1)^{c_+(h;v)}e(a/q),\qquad c_+(h;v)\in\{0,1\},
\tag{195.R1}
\]

where \(c_+\) is the canonical-anchor wrap.  The value
\(-e(a/q)\) occurs only on a wrap; without a wrap the ratio is
\(+e(a/q)\).  The pre-Fourier physical parity has constant ratio \(-1\),
but that identity is recovered only after the complete anchor-mode sum
and cannot be multiplied by the phase of one retained mode.  The minus
ratio is exactly \(1\).

Second, on \(P_{2,<D}\) the fixed-height and all-height positive counts
combine with the accepted terminal/Fejer cost to give the sharper
envelope

\[
 \left|\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)\right|
 \ll
 u\{\kappa+\min(Y,D_L)\}X^\varepsilon.
\tag{195.R2}
\]

Thus the unresolved positive-capacity multiplier beyond the safe
\(\kappa u\) term is at most

\[
 \frac{\min(Y,D_L)}{H_B\mathfrak m\kappa},
\tag{195.R3}
\]

not uniformly \(Y/(H_B\mathfrak m\kappa)\).  In particular, the part
\(\min(Y,D_L)\ll H_B\mathfrak m\kappa\) is already target-safe by an
absolute count.  The no-go applies only to the remaining parameter range
and only to coefficient-blind or within-row determinant/anchor
mechanisms.  These repairs do not invalidate the promoted strict
large-\(\kappa\) lemma.

## 2. Exact statement and hypotheses

Fix the literal Round-192 hard-\(M_1\), original-\(t=1\),
\(\rho\)-large core with

\[
 Q=H_B,\qquad D_L=\lceil\sqrt L\rceil,\qquad
 U=\mathfrak m q,\qquad U\mid u,
\]

and retain every physical endpoint, arithmetic mask, selector, profile,
Fejer factor, square-root phase, carry, birth/death term, orientation,
frequency sign, affine site, conjugation, zero extension, and the single
outer real part.  The physical first-failure mask is

\[
 P_2=\mathbf 1_{\{|d-gm|\le D_L\}}
     \mathbf 1_{\{|d'-gm'|>D_L\}},
\]

with the disjoint split

\[
 P_{2,\ge D}=P_2\mathbf 1_{\{\kappa\ge D_L\}},\qquad
 P_{2,<D}=P_2\mathbf 1_{\{1\le\kappa<D_L\}}.
\]

The review asserts the following.

1. The plus and minus charts give the signed defects and height equations
   in Section 3 below, with a positive far defect in both charts.
2. On one primitive row, the parity step in the positive far defect has
   \(O(1)\) legal samples in a live height block.
3. At one transported common site, the literal source channels must be
   recombined before a Gram estimate; doing so returns the original
   masked non-Fejer jump.
4. The full \(TT^*\) form has \(++,+-,-+,--\) orientation blocks and
   retains the actual coefficient vectors.
5. Equations (195.R2)--(195.R3) are positive upper capacities only.  They
   imply neither a literal lower mass nor failure of the complete
   \(P_2\) estimate.
6. Only the strict \(P_{2,\ge D}\) subordinate lemma may be promoted.
   The complete \(P_2\) claim, its owner, all parents, bridges, theorem
   endpoints, and exponent records remain unchanged.

## 3. Proof or derivation

### 3.1 Defect signs and determinant fibres

In the plus chart,

\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,\quad h=Sv-Uw>0.
\]

Consequently

\[
 \delta_+=\kappa(U-v)-2w,\qquad
 \eta_+=\kappa(U-v)+2S,
\]

\[
 g\delta_+=d-gm,\qquad
 g\eta_+=d'-gm',\qquad
 \eta_+-\delta_+=2(S+w),
\]

and direct expansion gives

\[
 2h=v\eta_++U\delta_+-\kappa(U^2-v^2).
\tag{195.R4}
\]

Lower closeness gives \(|g\delta_+|\le D_L\).  Since
\(\eta_+>\delta_+\), the upper-far alternative cannot have
\(g\eta_+<-D_L\); hence \(g\eta_+>D_L\).

In the minus chart,

\[
 d'=\kappa gU,\quad d=g(\kappa U+2S),\quad
 m=\kappa v,\quad m'=\kappa v+2w,\quad h=Uw-vS>0,
\]

so

\[
 \delta_-=\kappa(U-v)+2S,\qquad
 \eta_-=\kappa(v-U)+2w,
\]

\[
 g\delta_-=d-gm,\qquad
 -g\eta_-=d'-gm',\qquad
 \delta_-+\eta_-=2(S+w),
\]

and

\[
 2h=U\eta_--v\delta_-+\kappa(U^2-v^2).
\tag{195.R5}
\]

Here \(|g\delta_-|\le D_L\).  Positivity of
\(\delta_-+\eta_-\) rules out \(\eta_-<-D_L/g\), so upper failure forces
\(g\eta_->D_L\), while the raw upper defect \(d'-gm'=-g\eta_-\) is
negative.  Thus the signs in the candidate and reconciliation are exact.

### 3.2 Fixed-row fibre length

At fixed \((\kappa,g,U,v,\delta)\), increasing the positive far defect
\(\eta\) by \(2\) changes \(h\) by \(v\) in (195.R4) and by \(U\) in
(195.R5).  Since

\[
 U,v\asymp L/\kappa,\qquad Y\ll L/\kappa,
\]

one live height block contains respectively

\[
 O(1+Y/v)=O(1),\qquad O(1+Y/U)=O(1)
\]

legal far samples.  This establishes the asserted within-row
multiplicity bound, but supplies no cross-row cancellation.

### 3.3 Anchor-character ratios

For a fixed retained Round-191 mode the plus summand has the factor

\[
 (-1)^t z_{+,v}^{\,h},\qquad
 z_{+,v}=e(a\overline v_q/q).
\]

The plus parity step is \(S\mapsto S+1\), \(h\mapsto h+v\).  If
\(S=S_{0,+}(h)+Ut\) with \(0\le S_{0,+}<U\), then exactly

\[
 S_{0,+}(h+v)=S_{0,+}(h)+1-Uc_+(h;v),\qquad
 t(h+v)=t(h)+c_+(h;v),
\]

where \(c_+(h;v)\in\{0,1\}\).  Because
\(v\overline v_q\equiv1\pmod q\),

\[
 \frac{(-1)^{t(h+v)}z_{+,v}^{h+v}}
      {(-1)^{t(h)}z_{+,v}^{h}}
 =(-1)^{c_+(h;v)}e(a/q).
\tag{195.R6}
\]

This is (195.R1), not a constant \(-e(a/q)\).  Before Fourier splitting,
\((-1)^S\) does flip by \(-1\), but the constant physical identity is
restored only after summing all anchor modes.  Combining that full-mode
identity with \(e(a/q)\) from one retained mode mixes two incompatible
levels of the expansion.

In the minus chart the step is \(w\mapsto w+1\), \(S\) and \(t\) are
unchanged, and \(h\mapsto h+U\).  Hence

\[
 z_{-,v}^{\,U}
 =e(-a\overline v_qU/q)
 =e(-a\overline v_q\mathfrak m)=1.
\tag{195.R7}
\]

The minus ratio in both source documents is therefore exact.  The repair
to the plus ratio does not create a long within-row averaging variable:
Section 3.2 already bounds the row length by \(O(1)\).

### 3.4 Exact same-site event recombination

Write \(B=F\Lambda\Psi\), let \(P_h\) and \(P_-^{\rm tr}\) be the current
and transported-previous physical masks, and put
\(\chi=(-1)^\nu\).  At a common affine site,

\[
\begin{aligned}
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
={}&P_h(1-\chi)F_-\Lambda_-^{\rm tr}\Psi_-^{\rm tr}\\
 &+P_h(F_h-F_-)\Lambda_h\Psi_h\\
 &+P_hF_-(\Lambda_h-\Lambda_-^{\rm tr})\Psi_h\\
 &+P_hF_-\Lambda_-^{\rm tr}
       (\Psi_h-\Psi_-^{\rm tr})\\
 &+\chi(P_h-P_-^{\rm tr})
       F_-\Lambda_-^{\rm tr}\Psi_-^{\rm tr}.
\end{aligned}
\tag{195.R8}
\]

The Fejer-change line is the already safe projection.  Among the
remaining lines, the two current-phase contributions recombine as

\[
 P_hF_-(\Lambda_h-\Lambda_-^{\rm tr})\Psi_h
 +P_hF_-\Lambda_-^{\rm tr}\Psi_h
 =P_hF_-\Lambda_h\Psi_h,
\]

while the three transported-previous-phase contributions recombine as

\[
\begin{aligned}
 &P_h(1-\chi)F_-\Lambda_-^{\rm tr}\Psi_-^{\rm tr}
 -P_hF_-\Lambda_-^{\rm tr}\Psi_-^{\rm tr}\\
 &\qquad+\chi(P_h-P_-^{\rm tr})
 F_-\Lambda_-^{\rm tr}\Psi_-^{\rm tr}\\
 &=-\chi P_-^{\rm tr}F_-\Lambda_-^{\rm tr}\Psi_-^{\rm tr}.
\end{aligned}
\]

Thus exact recombination returns

\[
 P_hF_-\Lambda_h\Psi_h
 -\chi P_-^{\rm tr}F_-\Lambda_-^{\rm tr}\Psi_-^{\rm tr},
\tag{195.R9}
\]

the original masked non-Fejer jump.  The phrases all-ones
\(2\times2\) and \(3\times3\) Gram blocks are correct only for the equal
effective phase labels; the actual endpoint coefficients remain inside
the vectors and need not equal one.  Treating source labels as orthogonal
merely postpones the same summation cost.

### 3.5 Four orientation blocks

Let \(V_{\mathbf r}^{\omega}(h)\) be the literal recombined event vector
for orientation \(\omega\in\{+,-\}\) and primitive row \(\mathbf r\).
The exact Gram entries are

\[
 \Gamma_{\mathbf r,\mathbf r'}^{\omega,\omega'}(E)
 =\sum_h V_{\mathbf r}^{\omega}(h)
 \overline{V_{\mathbf r'}^{\omega'}(h)}
 \mathbf1_{\{\text{far bin }E\}}.
\tag{195.R10}
\]

They form the \(++,+-,-+,--\) blocks.  The \(-+\) block is the adjoint of
\(+-\), not a disposable positive term.  The endpoint coefficients,
radical phases, Fejer factors, masks, carries, births/deaths, and
cross-event terms therefore must remain in one joint quadratic form
before taking the single outer real part.  Neither document claims a
proved estimate for that form on the full small-\(\kappa\) complement.

### 3.6 Capacity normalization and exact no-go scope

For \(\kappa<D_L\), the close congruence has
\(O(1+\kappa D_L/L)=O(1)\) sites per height on each row.  There are
\(O(uJ/q)\) rows and the exact anchor/Abel return costs \(q/J\).
Consequently the new positive contribution is \(O(YuX^\varepsilon)\).
Independently, the all-height determinant count gives
\(O(D_LuX^\varepsilon)\).  Combining these two bounds and restoring the
accepted terminal/Fejer contribution \(O(\kappa uX^\varepsilon)\) proves
(195.R2).

The target is \(H_B\mathfrak m\kappa uX^\varepsilon\).  The
\(\kappa u\) term is automatically safe, while the new term has ratio
(195.R3).  The candidate's displayed \(Y/(H_B\mathfrak m\kappa)\) is a
valid upper deficit but is not the precise worst deficit when
\(D_L<Y\).  The reconciliation's coarser
\[
 \min\{Y/(H_B\mathfrak m),D_L/(H_B\mathfrak m\kappa)\}
\]
is compatible but likewise does not use the fixed-height \(Yu\) bound in
its first branch.

Nothing here is a lower bound.  The literal coefficients may vanish or
cancel.  The rigorous no-go says only that multiplicity, support,
same-site source-label orthogonalization, or a long within-row
determinant/anchor variable cannot by itself supply the missing factor.
It does not exclude a coefficient-sensitive cross-row estimate for the
actual four-block Gram and does not disprove complete \(P_2\).

The newly inserted squarefree-support observation is consistent with this
scope.  On nonzero support, squarefreeness of \(\kappa gU\) makes \(U\)
squarefree and \((\kappa,U)=1\), so the fixed
\((\kappa,U,h,\delta)\) quadratic congruence has at most
\(2^{\omega(U)}\ll_\varepsilon U^\varepsilon\) residue roots.  This
controls an algebraic multiplicity only; it does not remove the
anchor/Abel return or bound the actual cross-row coefficient Gram.

## 4. First doubtful or unproved step

The first false statement in the reviewed mechanism-boundary argument is
the constant plus ratio \(-e(a/q)\) following (195.C21), repeated in
Section 3 of the conductor reconciliation.  Equation (195.R6) is the
exact fixed-mode replacement.

After that repair, the first genuinely unproved step is a
coefficient-sensitive joint estimate for the actual \(++,+-,-+,--\)
Gram on

\[
 P_{2,<D}\,
 \mathbf1_{\{\min(Y,D_L)\gg H_B\mathfrak m\kappa\}}.
\tag{195.R11}
\]

The complementary small-\(\kappa\) parameter range is already safe by
(195.R2).  No available determinant identity controls the off-diagonal
endpoint-vector inner products and square-root phase at the target scale.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| plus/minus defect signs | PASS.  Equations (195.R4)--(195.R5) recover the positive far defects and the negative raw upper defect in the minus chart. |
| fixed-row fibre length | PASS.  The legal far step changes height by \(v\) or \(U\), so one live block has \(O(1)\) samples. |
| plus anchor-character ratio | REPAIR.  Replace constant \(-e(a/q)\) by the carry-dependent fixed-mode ratio (195.R6), or state only the full-mode physical parity ratio \(-1\). |
| minus anchor-character ratio | PASS.  Equation (195.R7) is exactly \(1\). |
| same-site event Gram | PASS with wording qualification.  Equal-phase channels give the all-ones phase blocks, and exact signed recombination gives (195.R9); actual coefficients are not all ones. |
| four orientation blocks | PASS.  The \(++,+-,-+,--\) blocks remain joint before positive norms. |
| small-\(\kappa\) capacity | REPAIR.  Use (195.R2)--(195.R3) and exclude the already-safe subrange from the open no-go seam. |
| squarefree quadratic-root insertion | PASS.  The \(U^\varepsilon\) root count is valid on nonzero support and is correctly denied any missing-power consequence. |
| no capacity-to-mass inference | PASS.  Both documents explicitly deny literal lower mass; this review makes the upper-only status explicit. |
| no complete \(P_2\) claim | PASS.  Only \(P_{2,\ge D}\) is proved; \(P_{2,<D}\) is its exact complement. |
| owner quarantine | PASS.  The hard-\(M_1\) original-\(t=1\) owner and every parent, bridge, and theorem endpoint remain open/unchanged. |
| exponent quarantine | PASS.  The internal \(1/3\), accepted external \(0.3144831759740614\ldots\), and target \(1/4\) records are not altered. |

## 6. Dependencies and exact artifacts used

1. protocol.md, SHA-256
   f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
2. state/proof_obligations.yml, SHA-256
   815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89.
3. state/active_campaign.yml, SHA-256
   7a6762a4030410bce88305638367821bc9280dc2f88f1b201e3403594e41e00d.
4. candidates/formalized_hard_m1_t1_p2_large_kappa_sector.md, SHA-256
   6dfa01ba15e9a64039bcce6a7b8bab788676d55c567b4b9c1c3e5dbb214d9fde.
5. reviews/conductor_round195_report_reconciliation.md, SHA-256
   0ed89615d9eb5480aa540eeb362727c2fa65a05bbc12956599a5b6040195f4ec.
6. reports/literal_p2_determinant_fibre_vector_attack.md, SHA-256
   c617c18c959792622e3df9fe3eb06f47ba61c6948be77f8617c83bda96302879.
7. reports/p2_gram_diagonal_collision_hostile_audit.md, SHA-256
   52de40ade4e243cca9e0c50edfee5f913c8120a488407b4f39fe951f22d9b8fb.
8. reports/blind_p2_determinant_fibre_rederivation.md, SHA-256
   f19700d13fc1c5e6f911a7860385fa8a6d9991d74f1791c5ddfa06bb63b00adf.
9. proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md,
   SHA-256
   7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2.
10. proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md,
    SHA-256
    4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160.

No computation or diagnostic artifact was used, and no shared proof state,
candidate, kernel, synthesis, or sibling report was edited.

## 7. Recommended state effect

REVISE before promotion.

1. Keep the strict \(P_{2,\ge D}\) positive lemma and exact complement.
2. Replace the fixed-mode plus ratio by (195.R6); retain (195.R7) for the
   minus chart.  State the full physical parity flip only at the
   pre-Fourier or fully recombined level.
3. Replace the small-\(\kappa\) capacity ledger and open parameter range by
   (195.R2)--(195.R3) and (195.R11).
4. Retain the same-site recombination and four-block Gram as a scoped
   method no-go only.  Do not promote a literal lower bound or a complete
   \(P_2\) failure.
5. Promote at most the subordinate strict-sector node after these text
   repairs and the remaining required seam reviews.  Leave the hard-\(M_1\)
   owner, every parent and bridge, the Gauss-circle target, and all
   exponent records unchanged.
