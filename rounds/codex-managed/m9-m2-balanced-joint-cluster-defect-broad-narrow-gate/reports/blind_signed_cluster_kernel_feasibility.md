# 1. Result

**No-go result for the proposed proof mechanism, not a disproof of the literal target.**  The data in the statement-only packet do not imply

\[
 |\mathcal K_B^{\rm bulk}|\ll_\varepsilon L^3X^\varepsilon.
\]

There is an exact algebraic parametrisation of the **unfactored outer-gradient vectors** and an explicit routing partition at the gate resolution \(\delta=L^{-1}\).  In that chosen representative, a triple labelled broad has determinant

\[
 |\det(\nabla\Theta_1,\nabla\Theta_2,\nabla\Theta_3)|
 \gg R^3\delta^2\asymp L^7.
\]

This determinant is not a gauge-invariant physical transversality certificate: an exact lattice character gauge can move the \(-\lambda h/2+s_d(1/2-\lambda)\) phase into the coefficient.  In any case it yields no saving for the scalar kernel, because there is no spatial integral, averaged block variable, or restriction norm to which it can be applied.  Point evaluation has the full \(\ell^1\) coefficient norm.  A phase-adapted array is used below strictly as a coefficient-uniform method control; it is not the literal amplitude and gives no physical lower bound.

The narrow side also has an exact surviving ruling.  With

\[
 u=\lambda/R,\qquad v=\sqrt{h/k},\qquad c=uv,
\]

all terms with fixed

\[
 Q=\frac{\mu^2h}{d^2k}=Xc^2
\]

have zero three-gradient-vector determinant in the unfactored representative.  The arithmetic ruling itself is exact, and both far gates allow it even at distance \(\asymp L^{-1}\) from their boundaries.  Moreover, when \(\lambda=N+\tfrac12\), the **residue-only multiplier** is exactly

\[
 e\!\left(s_d(\tfrac12-\lambda)\right)=1
\]

for every odd lift.  The post-unmask connector sharpens this: if \(2\lambda=P/D\) is reduced and \((d,\mu)=(Dr,Pr/2)\), then the complete linear/residue/character carrier is

\[
 -i\chi_4(h)\chi_4(PD),
\]

independent of the odd lift \(r\); for \(D=1\) it is
\(-i\chi_4(h)\chi_4(P)\).  Thus neither the gates nor the actual character carrier automatically cancels an equal-rational-\(\lambda\) class.  The first exact obstruction remains the missing scalar norm interface; independently, the first narrow obstruction is a missing signed estimate for the fixed-\(Q\), equal-rational-\(\lambda\) lift sums.  The literal estimate might still be true, but it requires information about \(b_B\), \(\mathcal A_{d,J}\), and their signed interaction that is not present in the packet.

# 2. Exact statement and hypotheses

Write a literal term of (136.B1) as

\[
 C_\iota e(\Theta_\iota),\qquad
 C_\iota=b_B(h,k)\gamma_d\mathcal A_{d,J}(h,k,k';\mu),
\]

where

\[
 \iota=(h,k,k',d,J,\mu),\quad d\mid k',\quad d\text{ odd},
 \quad \mu\in\mathbb Z+\tfrac12,
\]

and the two strict gates and the literal condition \(t_*\in J\) are retained.  No two indices are identified, including two indices having the same rational \(\lambda=\mu/d\).  The derivation below uses only:

* \(R=\sqrt X\asymp L^3\), balanced dyadic support \(h,k,k'\asymp L\), and \(O(L^3)\) outer triples;
* \(\mu\asymp dL^3\), unit spacing in \(\mu\), and \(|\mathcal A_{d,J}|\ll(dL)^{-1}\);
* \(\sum_{d\mid k'}|\gamma_d|\ll_\varepsilon X^\varepsilon\);
* the exact phase, divisor progression, and gates in (136.B2)--(136.B6).

In particular, the packet gives no pointwise or \(\ell^p\) bound for \(b_B\), no derivative or phase formula for \(\mathcal A_{d,J}\), and no cancellation identity for \(\gamma_d\).  Conclusions below therefore distinguish exact geometry of the literal phase from coefficient-adversary controls that test what can follow from the stated hypotheses.

The precise no-go proposition is the following.

> On every fixed \((d,s_d,J)\)-sheet, the chosen unfactored interpolation has the outer-gradient-vector determinant identity (3.1) below.  At resolution \(\delta=L^{-1}\), triples labelled broad in that representative satisfy the displayed lower bound, while its narrow collections lie in the pullback of a \(O(\delta)\)-tube about a line in a two-dimensional slope plane.  This routing is not gauge-invariant physical transversality, and no scalar determinant gain follows uniformly from the displayed hypotheses.  The pullback contains the exact rational rulings \(\mu^2h/(d^2k)=Q\), on which both far gates and a completely coherent combined character carrier can coexist.

# 3. Proof or derivation

**Unfactored outer-gradient coordinates and determinant.**  Freeze \(d\), its residue representative \(s_d\), and \(J\), and choose the continuous representative in which the entire exponent (136.B4) remains in the phase.  The residue term is then independent of the continuous outer variables, and the outer gradient in this representative is

\[
 \nabla_{h,k,k'}\Theta
 =\frac R2\left(\sqrt{k/h}-u,\ \sqrt{h/k},\ -\frac1u\right),
 \qquad u=\frac\lambda R.
\]

Put \(v=\sqrt{h/k}\), \(c=uv\), and introduce the two joint slope coordinates

\[
 a=\frac{1-c}{v^2},\qquad b=-\frac1c.
\]

Then the normalized gradient is

\[
 G:=\frac2R\nabla\Theta
 =\left(\frac1v-u,v,-\frac1u\right)
 =v(a,1,b).
\]

Consequently, for any three literal terms (on their respective fixed residue sheets), the determinant of their three unfactored outer-gradient vectors is

\[
 \begin{aligned}
 \det(\nabla\Theta_1,\nabla\Theta_2,\nabla\Theta_3)
 &=\frac{R^3}{8}v_1v_2v_3\,\mathfrak A(1,2,3),\\
 \mathfrak A(1,2,3)
 &:=(a_3-a_1)(b_2-b_1)-(a_2-a_1)(b_3-b_1).
 \tag{3.1}
 \end{aligned}
\]

Thus (3.1) is exactly twice the signed area of the triangle formed by the three \((a,b)\)-points, up to the harmless dyadic factors.  It is an algebraic identity for this chosen representative, not a gauge-invariant physical transversality certificate and not a determinant of normals to the gradient-image surface.  The exact post-unmask gauge

\[
 e\!\left(-{\lambda h\over2}+s_d(\tfrac12-\lambda)\right)
 =-i(-1)^m\chi_4(d)\chi_4(h)
\]

moves the term responsible for the first-coordinate \(-u\) into the coefficient.  Any use of (3.1) must therefore specify the representative and a normed operator; neither is supplied by the scalar kernel.

**Explicit scale partition.**  Tile the compact \((a,b)\)-range by half-open squares of side

\[
 \delta=L^{-1}.
\]

Each literal index, including its \(d,J,\mu\) lift label, is assigned to exactly one square.  Split triples in the cubic expansion of \(\mathcal K_B^{\rm bulk}\) as follows:

\[
 \begin{cases}
 \text{broad},&|\mathfrak A(1,2,3)|\ge 100\delta^2,\\
 \text{narrow},&|\mathfrak A(1,2,3)|<100\delta^2.
\end{cases}
\]

More explicitly, if \(T_\iota=C_\iota e(\Theta_\iota)\), define

\[
 \mathcal B_\delta=\sum_{|\mathfrak A(\iota_1,\iota_2,\iota_3)|\ge100\delta^2}
 T_{\iota_1}T_{\iota_2}T_{\iota_3},
 \qquad
 \mathcal N_\delta=\sum_{|\mathfrak A(\iota_1,\iota_2,\iota_3)|<100\delta^2}
 T_{\iota_1}T_{\iota_2}T_{\iota_3}.
\]

Then this is an exhaustive, literal-label-preserving partition

\[
 (\mathcal K_B^{\rm bulk})^3=\mathcal B_\delta+\mathcal N_\delta,
 \qquad
 |\mathcal K_B^{\rm bulk}|^3\le |\mathcal B_\delta|+|\mathcal N_\delta|.
\]

It is used because broadness is a relation among at least three directions; a canonical linear broad/narrow split of a single scalar sum does not exist.

The choice \(\delta=L^{-1}\) is the intrinsic gate resolution: the formulas below show that, on balanced support, a gate can change status when \(c^2\) changes by \(\asymp L^{-1}\).  By (3.1), every triple labelled broad in this routing has

\[
 |\det(\nabla\Theta_1,\nabla\Theta_2,\nabla\Theta_3)|
 \gg R^3\delta^2\asymp L^7.
 \tag{3.2}
\]

For a narrow collection, either all its slope points have diameter \(O(\delta)\), or choose two points separated by at least \(\delta\).  The triangle-area condition then puts every other point in an \(O(\delta)\)-tube about the line through those two points.  A line

\[
 \alpha a+\beta b+\gamma=0
\]

pulls back to the exact joint ruling equation

\[
 \alpha c(1-c)-\beta v^2+\gamma cv^2=0,
 \qquad c=\frac{\mu}{dR}\sqrt{\frac hk},\quad v^2=\frac hk,
 \tag{3.3}
\]

with an \(O(\delta)\) error for a line tube.  Therefore the narrow locus is not, in general, a single divisor progression; it is a family of algebraic line pullbacks.  The horizontal lines \(b=-1/c_0\) give the especially simple exact rational ruling

\[
 c=c_0
 \quad\Longleftrightarrow\quad
 \frac{\mu^2h}{d^2k}=Q:=Xc_0^2.
 \tag{3.4}
\]

For fixed \(c\),

\[
 G=\left(\frac{1-c}{v},v,-\frac v c\right),
\]

so all such unfactored gradient vectors lie in the plane \(G_2+cG_3=0\); every determinant of three of them is exactly zero.  The fixed-\(Q\) relation is an exact arithmetic ruling and the gate calculation below is representation-independent; only the interpretation of this zero determinant as physical transversality is gauge-dependent.

**The gates do not remove the ruling.**  Put \(A=k'/k\).  Substitution of \(\lambda=cR/v\) into (136.B6) gives the exact identities

\[
 \rho=hk'\frac{c^2-1}{c^2},
 \qquad
 \Delta=hk\frac{A^2-c^2}{c^2}.
 \tag{3.5}
\]

Thus the gates exclude only \(c^2=1+O(L^{-1})\) and \(c^2=A^2+O(L^{-1})\); they do not imply transversality along a fixed-\(c\) ruling.  In particular, when \(k'=k\),

\[
 \Delta=-\rho,
\]

and any fixed \(c\) with \(|c^2-1|>C/L\), for a sufficiently large support-dependent constant \(C\), obeys both strict gates.  Taking \(c^2=1+C/L\) gives a gate-safe packet whose unfactored gradient-vector determinant is zero, immediately inside the retained bulk and just beyond both gate boundaries.

There is also an exact lattice realisation of this geometry.  Take \(L=N\), \(X=N^6\), \(R=N^3\), \(d=1\),

\[
 \mu=N^3+MN^2+\tfrac12,
 \qquad h=k=k'\in[N,2N]\cap(2\mathbb Z+1),
\]

with fixed sufficiently large \(M\).  Then all terms have the same
\(c=1+M/N+1/(2N^3)\), and

\[
 \rho=-\Delta=h^2\frac{c^2-1}{c^2}>N
\]

for all sufficiently large \(N\).  Thus every member that satisfies the literal interior \(J\)-support condition is a same-lift, equal-\(\lambda\), gate-safe term on which the chosen-representative gradient-vector determinant vanishes; no boundary or transition term has been invoked.

**Divisor lifts, the residue-only multiplier, and the complete carrier.**  Write \(2\mu=p\), with \(p\) odd.  If

\[
 \lambda=\frac p{2d}=\frac P{2D}
\]

is reduced, then \(P,D\) are odd and all equal-rational-\(\lambda\) lifts have

\[
 d=Dr,qquad \mu=\frac{Pr}{2},qquad r\text{ odd},qquad Dr\mid k'.
 \tag{3.6}
\]

The smooth phase \(R\sqrt{hk}-Xk'/(2\lambda)\) is identical for these lifts.  For the particularly transparent class \(D=1\), write \(P=2N+1\).  Then the residue term by itself satisfies

\[
 \lambda=N+\tfrac12,qquad
 \underbrace{e\!\left(s_{r}(\tfrac12-\lambda)\right)}
 _{\text{residue-only multiplier}}
 =e(-Ns_{r})=1
 \tag{3.7}
\]

for every lift.

Equation (3.7) is **not** the full combined character carrier.  The exact post-unmask connector is

\[
 e\!\left(-{\lambda h\over2}
       +s_{Dr}(\tfrac12-\lambda)\right)
 =-i(-1)^m\chi_4(Dr)\chi_4(h).
\]

Since \(m=(1-Pr)/2\) and \(r\) is odd,

\[
 (-1)^m\chi_4(Dr)
 =\chi_4(Pr)\chi_4(Dr)=\chi_4(PD).
\]

Therefore every reduced equal-rational-\(\lambda\) family obeys

\[
 \boxed{
 e\!\left(-{\lambda h\over2}
       +s_{Dr}(\tfrac12-\lambda)\right)
 =-i\chi_4(h)\chi_4(PD),}
 \tag{3.7a}
\]

and, including the common smooth phase,

\[
 \boxed{
 e(\Theta_{Dr,Pr/2})
 =-i\chi_4(h)\chi_4(PD)
   e\!\left(R\sqrt{hk}-{XDk'\over P}\right).}
 \tag{3.7b}
\]

Both formulas are independent of the odd lift \(r\).  For \(D=1\),
the complete carrier in (3.7a) is
\(-i\chi_4(h)\chi_4(P)\), as distinct from the residue-only identity
(3.7).  The lift label still changes \(\gamma_{Dr}\), its progression,
\(J\)-admissibility, and the literal amplitude, so no lifts are merged.

This correction is consistent with retaining both original \(\chi_4\) factors.  For odd \(h\) and \(h'=h+2s\),

\[
 \chi_4(h)\chi_4(h')=(-1)^s.
\]

Writing \(s=s_d+dt\) with odd \(d\) gives \((-1)^{s_d}(-1)^t\).  The \((-1)^t\) is precisely the half-integral dual-frequency shift.  Equations (3.7a)--(3.7b), rather than the residue-only (3.7), are the exact statement that the complete carrier is coherent.  Cancellation among the distinct lifts would have to come from a new identity involving \(\gamma_{Dr}\mathcal A_{Dr,J}\), and only an \(\ell^1\) bound for \(\gamma\) is stated.

**Capacity at the chosen resolution.**  For fixed \((h,k,d)\),

\[
 \frac{dc}{d\mu}=\frac{v}{dR}.
\]

A horizontal narrow tube of width \(\delta=L^{-1}\) therefore contains at most \(O(dR\delta+1)=O(dL^2)\) consecutive \(\mu\)'s per interior \(J\), and its absolute stationary-amplitude capacity is \(O(L)\).  By contrast, the whole \(\mu\)-range has capacity \(O(L^2)\).  Hence, writing

\[
 B_1:=\sum_{\substack{(h,k,k')\\ \mathrm{in\ the\ fixed\ block}}}|b_B(h,k)|,
\]

the information in the packet gives only the formal capacities

\[
 \text{one horizontal narrow tube: }O_\varepsilon(LB_1X^\varepsilon),
 \qquad
 \text{all frequencies: }O_\varepsilon(L^2B_1X^\varepsilon),
 \tag{3.8}
\]

per bounded-overlap family of \(J\)'s.  Even the first expression reaches the target by absolute values only if \(B_1\ll L^2\).  The packet gives no such weighted outer estimate; the raw support cardinality alone cannot replace it.

**Why the chosen gradient-vector determinant has no scalar price.**  Formula (3.2) could only become useful after a normed operator theorem in a specified gauge.  The kernel in (136.B1), however, is one complex number.  To test any coefficient-uniform scalar claim, take a finite routed subcollection on which \(b_B\gamma_d\ne0\) and define the phase-adapted **method-control array**

\[
 \mathcal A_{d,J}
 =\frac1{dL}e(-\Theta_{d,\mu})
   \frac{\overline{b_B(h,k)\gamma_d}}
        {|b_B(h,k)\gamma_d|}.
 \tag{3.9}
\]

It satisfies the displayed magnitude bound and makes every selected summand equal \(|b_B\gamma_d|/(dL)\), independently of the determinant.  Equation (3.9) is not the hidden literal stationary amplitude, is not a lawful replacement for it in the physical kernel, and supplies no physical lower bound.  Its sole implication is methodological: no coefficient-uniform scalar lemma follows from (3.2) and the displayed size hypotheses.  To use the literal amplitude one must state and prove an additional actual-symbol oscillatory identity that is not coefficient-uniform in the sense tested by (3.9).

# 4. First doubtful or unproved step

The first unproved step is the conversion

\[
 |\det(\nabla\Theta_1,\nabla\Theta_2,\nabla\Theta_3)|\gg L^7
 \quad\Longrightarrow\quad
 \text{a saving in }|\mathcal K_B^{\rm bulk}|.
\]

There is no valid implication of this form for a scalar exponential sum, and the antecedent itself is representative-dependent.  A determinant can measure separation only inside a specified operator as an external variable moves; (136.B1) supplies no such variable and no norm over it.  Expanding \(\mathcal K^3\), taking a positive row Gram, or applying Cauchy--Schwarz merely replaces the signed scalar by a positive sum and incurs the corresponding row/cap capacity.  It does not manufacture the absent averaging operation.  Equation (3.9) is strictly a coefficient-uniform method control witnessing this failure, not a literal lower-bound packet.

Even if a suitable broad norm were introduced, the first independent narrow step would still be unproved.  On a fixed rational ruling, the required estimate contains sums of the form

\[
 \mathscr L_{P,D}(h,k,k')
 :=
 \sum_{\substack{r\ \mathrm{odd}\\ Dr\mid k'}}
 \gamma_{Dr}
 \sum_{J:\,t_*(Dr)\in J}^{\mathrm{bulk}}
 \mathcal A_{Dr,J}(h,k,k';Pr/2),
 \tag{4.1}
\]

multiplied by the common carrier (3.7b) and coupled to the outer variables, both gates, and the slanted profile.  No cancellation estimate for (4.1), no usable \(B_1\) bound, and no formula pairing its literal amplitudes across opposite character classes is among the statement-only hypotheses.  This is the first exact arithmetic-sign/capacity obstruction on the narrow side.

# 5. Control tests and outcomes

| Control | Exact analytical test | Outcome and implication |
|---|---|---|
| `literal_bulk_kernel_and_owner_ledger` | Keep \(\iota=(h,k,k',d,J,\mu)\), \(b_B\), \(\gamma_d\), \(\mathcal A_{d,J}\), \(s_d\), and both strict gates attached to every cap. | Passed as bookkeeping.  The partition changes no owner and takes no absolute value until a stated capacity/adversary test. |
| `divisor_progression_and_distinct_lifts` | Reduce \(\lambda=p/(2d)=P/(2D)\) and use (3.6). | Distinct lifts remain distinct.  Equations (3.7a)--(3.7b) show that every reduced equal-\(\lambda\) family has a lift-independent combined carrier, while \(\gamma_{Dr}\), \(J\), progression, and amplitude remain literal. |
| `joint_broad_partition_resolution` | Tile the exact joint slope plane \((a,b)\) at \(\delta=L^{-1}\), the scale detected by (3.5). | Exhaustive, with half-open boundary ownership.  A horizontal tube contains \(O(dL^2)\) frequencies per fixed row and lift. |
| `broad_transversality_determinant` | Apply (3.1) to triples with slope-triangle area at least \(100\delta^2\). | Algebraically \(\gg L^7\) for the three unfactored gradient vectors in that representative.  It is neither a normal determinant nor a gauge-invariant physical certificate. |
| `broad_capacity_to_L3` | Test a coefficient-uniform scalar claim against the method-control array (3.9). | Failed.  The control can align routed terms at full \(\ell^1\) mass, but gives no literal lower bound.  A spatial/parameter norm and a theorem returning to the fixed block are missing. |
| `narrow_rational_ruling_classification` | Pull back a line by (3.3); inspect horizontal lines separately. | General narrow tubes are algebraic line pullbacks, not automatically divisor classes.  The exact horizontal subclass is the rational invariant \(\mu^2h/(d^2k)=Q\), and its determinant vanishes identically. |
| `actual_chi4_and_residue_phase` | Separate the residue-only identity (3.7) from the exact connector (3.7a)--(3.7b). | Both characters are retained.  At \(D=1\), (3.7) equals one but the complete carrier is \(-i\chi_4(h)\chi_4(P)\); in general it is \(-i\chi_4(h)\chi_4(PD)\), independent of the odd lift. |
| `coupled_rho_Delta_far_gates` | Substitute fixed \(c\) and \(A=k'/k\) to obtain (3.5), including \(k'=k\). | Failed as a source of separation.  For \(k'=k\), both gates hold just beyond \(|c^2-1|\asymp L^{-1}\), while the fixed-\(Q\) ruling is exact and its chosen-representative gradient determinant is zero. |
| `coherent_and_opposite_character_packets` | Coherent packet: a reduced equal-\(\lambda\) family with (3.7b).  Opposite packet: switch one \(\chi_4\) class while retaining literal weights; use (3.9) only as a coefficient-uniform control. | The complete carrier is lift-independent, not merely residue-coherent at \(D=1\).  No measure- and profile-preserving opposite-character pairing is given.  Phase adaptation tests a method and is never asserted as the physical amplitude. |
| same-lift / same-denominator | Fix \(d\) (in particular \(d=1\)) and use a \(c\)-tube of width \(L^{-1}\). | Divisor or lift cancellation disappears, yet the tube retains capacity \(O(L)\) per outer row.  This isolates the needed outer signed estimate. |
| equal-rational-\(\lambda\) | Use all lifts (3.6), without merging them. | The full combined carrier is coherent for every reduced \(P/D\) by (3.7b).  Only a new bound for the distinct-amplitude sum (4.1) can help. |
| phase-adapted | Use (3.9) on either routed broad triples or a narrow tube. | It preserves the displayed magnitudes and cancels the real-centre phase only in a coefficient-uniform adversary model.  It is not the literal amplitude and proves no physical lower bound. |
| gate-boundary | Set \(k'=k\) and \(c^2=1+C/L\) with \(C\) large enough for strictness. | Both gates survive and \(\Delta=-\rho\); the fixed-\(c\) class has zero unfactored gradient-vector determinant in the chosen representative.  No transition term is imported. |
| `boundary_and_transition_scope` | Assign only indices already marked bulk; do not move a crossing or incomplete stationary mode into a cap. | Passed.  Previously controlled boundary, crossing, transition, nonstationary, and remainder packages play no role in the no-go result. |
| `scalar_vs_positive_energy` | Write row sums \(S_{h,k,k'}\) and compare \(|\sum b_BS|^2\) with \((\sum|b_B|^2)(\sum|S|^2)\). | A positive energy is only a sufficient upper-bound route after paying the outer norm; it is not equivalent to the signed scalar target.  The packet supplies no energy estimate of the strength required after that payment. |
| raw-vs-weighted / signed-vs-unsigned | Compare (3.8) with the raw \(O(L^3)\) row count, and compare the literal signs with (3.9). | The raw count gives no bound for \(B_1\).  The signed result cannot be inferred from absolute, random, or adversarial coefficients; an exact literal cancellation lemma is required. |
| `full_BAL_owner_and_downstream_scope` | Keep the fixed balanced block and address only (136.B1); accept the listed error packages only as the packet states them. | Passed as scope.  The determinant and no-go statements neither alter downstream packages nor claim an estimate for the full Gauss-circle expression. |

# 6. Dependencies and exact artifacts used

This report used, completely and exclusively, the following permitted artifacts:

1. `problems/gauss_circle.md`;
2. `state/control_models.md`;
3. `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/blind_statement.md`;
4. the task brief `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/briefs/blind_signed_cluster_kernel_feasibility.md`.

No claim graph, proof draft, strategy file, Round-112--136 nonblind artifact, sibling report, web source, or numerical/symbolic experiment was read or used in the original blind derivation.  The work was entirely analytical.  Equations (3.1), (3.3)--(3.7), and the capacity calculation (3.8) were derived directly from (136.B2)--(136.B6).  The later conductor-requested artifact repair labels (3.7) correctly as residue-only and records the exact post-unmask connector (3.7a)--(3.7b); it does not alter this statement-only provenance.

# 7. Recommended state effect

**Reject promotion of the claimed broad--narrow closure; retain the exact arithmetic and representative-specific identities with corrected scope; otherwise make no proof-state change.**  In particular:

* retain (3.1) only as the exact determinant of three unfactored outer-gradient vectors in a chosen representative, not as gauge-invariant physical transversality, and retain (3.3)--(3.4) as the corresponding line pullback and exact fixed-\(Q\) ruling;
* retain (3.5) as the proof that both far gates allow exact fixed-\(Q\) rulings, including the gate-boundary packet, while their unfactored gradient-vector determinant vanishes in the chosen representative;
* retain (3.6), the residue-only (3.7), and the corrected complete-carrier identities (3.7a)--(3.7b) as the equal-rational-lift control;
* require, before reconsidering promotion, a genuine normed broad estimate together with a justified passage back to the single fixed-block scalar, an explicit weighted bound for \(b_B\), and a literal signed estimate for (4.1) that handles \(D=1\), same lift, opposite character, and phase-adapted controls.

Until those inputs exist, (136.B7) remains unproved and the broad--narrow mechanism has an exact norm/arithmetic-sign obstruction rather than a closed \(L^3\) estimate.
