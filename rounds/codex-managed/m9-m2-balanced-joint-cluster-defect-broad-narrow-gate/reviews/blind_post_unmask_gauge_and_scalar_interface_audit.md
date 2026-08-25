# 1. Result

**Seam verdict: retain the Round-136 no-go, but narrow the discovery report's geometric claims before promotion.**  The exact character gauge (136.A1)/(136.H1), the equal-rational-\(\lambda\) carrier coherence (136.A4)/(136.H3), and the absence of a scalar norm interface are certified.  They jointly rule out a coefficient-blind curvature/positive-norm closure with the ingredients presently stated.

The apparent conflict between the discovery report and the blind report is not a contradiction.  In the discovery notation \(r=\sqrt{k/h}\), \(z=\lambda/R\), the blind vector in its equation (3.1) is

\[
 G=\Sigma_0(r,z)=(r-z,r^{-1},-z^{-1}).
\]

The blind determinant is the determinant of three **gradient vectors** \(\Sigma_0(r_i,z_i)\).  The discovery determinant in (136.A12), (136.A16), and lines 283--300 is instead the determinant of three **normals to the image surface**.  These are different objects.  After the exact arithmetic gauge, the chosen smooth representative becomes the cylinder

\[
 \Sigma(r,z)=(r,r^{-1},-z^{-1}),
 \qquad N(r,z)\parallel(1,r^2,0),
\]

so its three-normal determinant is zero.  The determinant of three vectors \(\Sigma(r_i,z_i)\) is still generally nonzero.  Thus the discovery report does not literally turn the blind determinant into zero; it changes gauge and changes the geometric object.

Accordingly:

* (136.A17), \(\mathcal K_{B,\mathrm{br}}=0\), is exact **only for the normal-based partition defined in (136.A11)--(136.A13) after the gauge**.  It is not an intrinsic or gauge-independent statement that every possible broad component of the signed kernel is empty.
* The gauge-invariant correction is more precise: the unfactored \(z\)-curvature is not, by itself, an intrinsic transversality certificate, because the exact gauge transfers it into \((-1)^m\chi_4(d)\chi_4(h)\) without changing coefficient magnitudes.  A proof may still use that curvature in a chosen gauge, but it must prove the full operator inequality and track the modulated coefficient class; the determinant alone is insufficient.
* An actual-symbol theorem is allowed to be gauge-sensitive and exploit that arithmetic factor.  No such theorem is supplied, so the scalar target remains open.
* (136.A18) is a correct positivity identity for the complete \(1/d\)-weighted divisor coefficient and therefore for a **leading common-profile** lift packet when all lifts share that profile and admissibility.  It is not positivity of the full literal \(\mathcal A_{d,J}\)-weighted lift sum.
* The second-B calculation certifies a stationary-phase/canonical self-return.  It does not, from the equations in these reports alone, certify an exact full-operator return of every literal profile, \(J\)-piece, boundary owner, and remainder.

The first failed seam is the unqualified move at discovery lines 53--56 and 272--281 from “the gauged smooth normal surface has rank two” to “the whole literal kernel is narrow,” later called “gauge-invariant” at lines 515--516.  The first analytic gap after the corrected statement is still the blind report's scalar interface: no normed operator turns any surviving transversality into an \(L\)-saving for the one fixed-block complex number.

# 2. Exact statement and hypotheses

Let an atom be written in an arbitrary phase-amplitude gauge as

\[
 T_\alpha=C_\alpha e(\Phi_\alpha),
 \qquad \alpha=(h,k,k',d,\mu,J).
\]

For any unit complex \(\varepsilon_\alpha\), the replacement

\[
 C_\alpha\mapsto C_\alpha\varepsilon_\alpha,
 \qquad
 e(\Phi_\alpha)\mapsto \overline{\varepsilon_\alpha}e(\Phi_\alpha)
 \tag{2.1}
\]

leaves the literal atom, index set, support, gates, and scalar sum unchanged.  It also preserves every coefficient \(\ell^p\) magnitude.  It need not preserve smoothness or arithmetic form of the coefficient, so an actual-symbol theorem may distinguish gauges, whereas a coefficient-uniform square-function or restriction theorem may not.

For the present kernel, (136.A1) gives the exact gauge

\[
 \varepsilon_\alpha=-i(-1)^m\chi_4(d)\chi_4(h),
 \qquad
 \Psi=R\sqrt{hk}-{Xk'\over2\lambda},
 \tag{2.2}
\]

because

\[
 e(\Theta_{d,\mu})
 =\varepsilon_\alpha e(\Psi).
\]

The audit uses the following distinction throughout.

* A statement is **atom-gauge-invariant** if it concerns the complete \(T_\alpha\), exact ratios of complete carriers, the literal scalar, the index/lift labels, coefficient magnitudes, or the two gates.
* A statement is **representative-dependent** if it concerns a continuous derivative, Hessian, surface normal, cap, or broad label formed after choosing which unit phase sits in \(C_\alpha\) and which sits in \(e(\Phi_\alpha)\).

The exact hypotheses retained are those of the frozen plan: distinct lifts, the full \(d,J,\mu\) owner, both strict gates, the fixed block and slanted profile, amplitude size \(O((dL)^{-1})\), and no reuse of boundary/transition/remainder owners.  No assertion below treats a phase-adapted array, a leading stationary profile, or a positive diagonal as the full physical scalar.

# 3. Derivation and reconciliation

**The connector is exact.**  Since \(h+2s_d=d\ell_d\),

\[
 -{\lambda h\over2}+s_d(\tfrac12-\lambda)
 ={s_d\over2}-{\mu\ell_d\over2}.
\]

With \(\mu=1/2-m\) and \(\ell_d\) odd,

\[
 e(s_d/2-\mu\ell_d/2)
 =-i(-1)^{s_d+m}\chi_4(\ell_d).
\]

The congruence \(d\ell_d=h+2s_d\pmod4\) gives

\[
 (-1)^{s_d}\chi_4(\ell_d)=\chi_4(d)\chi_4(h),
\]

which proves (136.A1)/(136.H1).  Discovery lines 15--42 and hostile-audit lines 142--165 are therefore certified.

**The two geometric objects.**  Before applying (2.2), differentiation in \((h,k,k')\), on a fixed residue sheet, gives

\[
 {2\over R}\nabla\Theta=\Sigma_0(r,z)
 =(r-z,r^{-1},-z^{-1}).
 \tag{3.1}
\]

This is exactly the blind report's \(G\) after substituting \(r=1/v\), \(z=u\).  Its equation (3.1) computes

\[
 D_{\rm pos,0}=\det\bigl(\Sigma_0(r_1,z_1),
                          \Sigma_0(r_2,z_2),
                          \Sigma_0(r_3,z_3)\bigr).
 \tag{3.2}
\]

By contrast, the normal to the image of \(\Sigma_0\) is

\[
 N_0=\partial_r\Sigma_0\times\partial_z\Sigma_0
 \parallel(1,r^2,z^2),
 \tag{3.3}
\]

and the discovery expression at lines 291--296 is \(\det(N_{0,1},N_{0,2},N_{0,3})\), not (3.2).

After (2.2),

\[
 {2\over R}\nabla\Psi=\Sigma(r,z)
 =(r,r^{-1},-z^{-1})=\Sigma_0(r,z)+(z,0,0),
 \tag{3.4}
\]

and

\[
 N=\partial_r\Sigma\times\partial_z\Sigma
 \parallel(1,r^2,0).
 \tag{3.5}
\]

Therefore \(\det(N_1,N_2,N_3)=0\), proving (136.A16) in this gauge.  On the other hand,

\[
 \det\bigl(\Sigma(r_1,z_1),\Sigma(r_2,z_2),\Sigma(r_3,z_3)\bigr)
\]

is not identically zero.  Discovery control line 472 is correct if “the nonzero determinant” means its own normal determinant (3.3); it is false if read as saying that the blind position-vector determinant (3.2) becomes zero.  Neither determinant has scalar force without an operator norm.

**Gauge-invariant content of the broad no-go.**  The modulation (2.2) has modulus one.  A coefficient-uniform estimate in the unfactored gauge is norm-equivalent, by the bijection \(C_\alpha\leftrightarrow C_\alpha\varepsilon_\alpha\), to the same estimate for the gauged atoms.  Therefore \(\det N_0\ne0\) cannot be promoted as a sufficient, representation-independent certificate: in the equivalent representative the corresponding normal determinant is zero.  This does not logically prohibit using \(N_0\) as a proof device in one chosen gauge; it requires the missing full operator inequality and a justified scalar return.  It also does not exclude a theorem that keeps \((-1)^m\chi_4(d)\chi_4(h)\) as actual arithmetic data and proves cancellation jointly with \((h,k,k',d,\mu,J)\).

**Equal-rational lifts are genuinely coherent in their full carrier.**  If \(2\lambda=a/b\) is reduced, every lift is \((d,\mu)=(bc,ac/2)\), with \(c\) odd.  Since

\[
 (-1)^m\chi_4(d)=\chi_4(ac)\chi_4(bc)=\chi_4(ab),
\]

the entire phase-character carrier is (136.H3), independent of \(c\).  Also \(x_*=Xk'/\lambda^2\), \(\rho\), and \(\Delta\) are common.  This is atom-gauge-invariant and strengthens the blind report's residue-only observation at reduced denominator \(b=1\): coherence holds for every reduced \(a/b\).  What remains noncommon is precisely the literal sum

\[
 \sum_{\substack{c\ \mathrm{odd}\\ bc\mid k'}}\gamma_{bc}
 \sum_{J:t_*(bc)\in J}\mathcal A_{bc,J}(h,k,k';ac/2).
 \tag{3.6}
\]

Thus (136.A4), (136.H3), and (136.H16) are certified, while merging the lifts or assigning a sign to (3.6) is not.

**The second B-process returns only at the phase/canonical level on the displayed evidence.**  With \(k'=dv\) and \((-1)^m=e(1/4-\mu/2)\), the smooth phase is

\[
 g(\mu)=-{Xd^2v\over2\mu}-{\mu\over2}.
\]

The stationary equation \(g'(\mu)=n\) gives

\[
 x_*=d(2n+1),\qquad h'=d(2n+1),\qquad k'=dv,
\]

and the critical action is

\[
 g(\mu)-n\mu=-R\sqrt{h'k'}.
 \tag{3.7}
\]

Discovery lines 358--380 are therefore correct.  This proves that the leading canonical phase is involutive and explains why a second one-variable B-process supplies no automatically independent oscillation.  Lines 382--386, and the analogous hostile statement at lines 253--268, go further when they say that the complete reciprocal Jacobian, profiles, gates, and character owner return.  That full operator claim requires a separate finite-Poisson, support, \(J\), transition, and remainder ledger; it is not proved by (3.7) alone and cannot be used as a new owner here.

**The \(b=1\) positivity has a strict scope.**  From (136.A6), for the odd part \(n\) of \(k'\),

\[
 \sum_{d\mid n}{\gamma_d\over d}
 =\sum_{r\mid n}{\eta(r/G_0)\over r}
   {\varphi(n/r)\over n/r}>0,
 \tag{3.8}
\]

assuming the stated nonnegative cutoff.  This algebra is exact.  If, on a reduced-denominator-\(b=1\) packet, the leading stationary amplitudes have the common factorisation

\[
 \mathcal A^{\rm lead}_{d,J}=d^{-1}W(h,k,k';\lambda)
 \tag{3.9}
\]

with common admissibility and common Fresnel/profile factor \(W\), then (3.8) makes that leading lift coefficient positive after removing \(W\).  It does **not** imply

\[
 \sum_{d\mid n}\gamma_d\mathcal A_{d,J}>0
\]

for the full literal amplitudes.  A partial set of admissible lifts, \(d\)-dependent \(J\)-ownership, a noncommon profile, or any literal correction destroys the reduction to (3.8).  Discovery lines 337--356 do not display the decomposition (3.9) or prove common admissibility.  Accordingly, (136.A18) is certified as a divisor identity and leading-common-profile control, not as positivity of (3.6) or as a physical lower bound.

# 4. First doubtful or unproved step

The first false **wording** seam is discovery lines 53--56: “the whole literal kernel is narrow.”  What was proved is that the normals of the selected gauged smooth representative lie in one plane, so the report's own three-normal broad class is empty.  The same overstatement reappears at lines 515--516 as “the gauge-invariant cylindrical normal-rank obstruction.”  Normal rank is representative-dependent; the invariant fact is only that the same atom family has a rank-deficient representative, so nonzero normal determinant cannot stand alone as the proof certificate.

The first unproved **analytic** seam is earlier and common to all three reports: neither (3.2), (3.3), nor (3.5) is connected to an averaging domain or operator norm whose bound returns to the fixed scalar.  The blind phase-adapted control remains decisive for coefficient-uniform claims.  Declaring the gauged broad part empty avoids rather than solves this scalar interface, since its narrow part is exactly the original kernel.

There are then two independent literal-symbol gaps:

1. no signed estimate gains the missing factor \(L\) in (3.6) or in the same-denominator clusters (136.H17)--(136.H20), with the outer profile and both gates retained;
2. no displayed identity upgrades the leading coefficient positivity (3.8)--(3.9) to the full \(\mathcal A_{d,J}\)-weighted lift family.

The phase self-return (3.7) does not fill either gap.  At most it shows that iterating the same one-variable transform does not create a new phase direction; a full second-B operator statement would itself require an owner-preserving proof.

# 5. Controls and line/equation-specific verdicts

| Seam or control | Location | Verdict |
|---|---|---|
| Exact character gauge | Discovery lines 15--42, (136.A1)--(136.A2); hostile lines 142--165, (136.H1) | **Certify.** The congruence and quarter-phase calculation are exact, retain both \(\chi_4\) factors, and preserve every atom. |
| Blind unfactored determinant | Blind lines 69--103, equation (3.1) | **Retain only as algebra.** It is \(\det(\Sigma_{0,1},\Sigma_{0,2},\Sigma_{0,3})\), not a surface-normal determinant and not gauge-invariant.  Calling it a physical transversality certificate was an overreach; the blind scalar-interface objection remains valid. |
| Collapsed smooth normal surface | Discovery lines 243--281, (136.A16)--(136.A17) | **Certify in the chosen gauge and definition.** The normal determinant is zero and hence that defined broad part is empty.  **Reject** the stronger claim that all gauge-sensitive or arithmetic broad mechanisms are empty. |
| “Removed nonzero determinant” | Discovery lines 283--304 and control line 472 | **Scope correction.** The gauge removes the \(z^2\) coordinate from \(N_0\); it does not make the determinant of three gauged gradient vectors identically zero.  A coefficient-blind theorem cannot charge the removed normal curvature, but an actual-sign theorem remains possible. |
| Joint broad partition | Discovery lines 165--211, (136.A11)--(136.A14) | **Valid routing, no estimate.** Half-open ownership is exact.  Because (136.A17) makes every atom narrow, (136.A14) is a unique parametrisation of all atoms, not a nontrivial exhaustive classification of intrinsic transversality failures. |
| Gauge invariance | Equations (2.1)--(3.5) of this review | **Pass with distinction.** Atoms, gates, carrier ratios, lift labels, and coefficient magnitudes are invariant; continuous phase gradients, Hessians, normals, caps, and broad labels are not. |
| Equal-rational-\(\lambda\) lifts | Discovery (136.A4); hostile (136.H3), (136.H15)--(136.H16) | **Certify.** The complete linear/residue/character carrier and both gates are independent of the lift multiplier \(c\).  The amplitudes, \(\gamma_{bc}\), progression, and \(J\) remain distinct and may neither be merged nor declared positive. |
| Blind \(b=1\) residue packet | Blind lines 212--242, (3.6)--(3.7) | **Correct but strictly weaker.** The residue alone is one when \(\lambda=N+1/2\); post-unmask, the exact combined carrier is coherent for all reduced \(a/b\), not only \(b=1\). |
| Leading \(b=1\) positivity | Discovery lines 337--356, (136.A18) | **Certify (136.A18) only for \(\sum\gamma_d/d\)** and for a proved common leading factor (3.9).  **Do not certify** positivity of the full literal lift sum (3.6), a partial lift family, or the full physical kernel. |
| Same-denominator clusters | Hostile lines 219--251, (136.H17)--(136.H20) | **Certify as a capacity/coherence control.** Pigeonholing gives a same-parity reciprocal cluster and no forced character cancellation.  It does not prove the literal amplitudes have a common phase or give a scalar lower bound. |
| One-body Hessians | Hostile lines 108--138, (136.H10)--(136.H12) | **Certify algebra, reject transversality inference.** Their nonzero determinants are transform Jacobians and persist on coherent lift rulings; they do not classify pairwise broadness. |
| Second-B return | Discovery lines 358--386; hostile lines 253--268 | **Certify phase/canonical self-return (3.7).** The claim that every full profile, gate component, character factor, transition, and remainder returns is not internally established and cannot be charged as a second owner.  No new \(L\)-saving follows. |
| Broad and positive capacities | Discovery (136.A19)--(136.A20); hostile power ledger lines 281--298 | **Capacity only.** \(L^3\) per cap, \(L^4\) square mass, and \(L^5\) aliaswise \(\ell^1\) are coefficient-blind scales.  Without lower envelopes for \(b_B\) and the full literal amplitude they are not actual lower bounds; they validly obstruct coefficient-uniform positive-norm closure. |
| Coupled gates and boundary | Discovery (136.A9), control lines 476 and 484; hostile lines 300--306 | **Certify.** Equal-\(\lambda\) lifts have common \(x_*,\rho,\Delta\); the two gates do not separate them, and collars may not be reused. |
| Scalar versus positive energy | Blind lines 268--302; discovery lines 416--431; hostile lines 298--323 | **No-go certified.** A positive diagonal or phase-adapted array tests capacity but is not the signed scalar.  No report supplies the owner-preserving non-positive inequality needed for \(L^3\). |
| Full owner/downstream scope | All three section-7 recommendations; frozen plan completion criteria | **No closure.** The complete bulk remains the smallest certified open scalar.  No BAL, M9-M2, endpoint, quarter, M9, or exponent promotion is licensed. |

# 6. Dependencies and artifacts used

This post-unmask audit used exactly the frozen Round-136 manifest/brief and the three fixed reports requested by the conductor:

1. `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/plan.json`;
2. `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/briefs/blind_signed_cluster_kernel_feasibility.md`;
3. `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reports/joint_cluster_defect_broad_narrow_attack.md`;
4. `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reports/blind_signed_cluster_kernel_feasibility.md`;
5. `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reports/aligned_rational_ruling_hostile_audit.md`.

The graph hash is the frozen `c43058006cec6849cd17a49e6a7a5298f5a3c124b34d2333b3279adcb54da1d1`.  No report or shared-state file was edited.  No web source, numerical experiment, symbolic computation, strategy file, claim graph, proof draft, or earlier-round artifact was read for this review.

# 7. Recommended state effect

Recommend the following scoped disposition.

* **Promote after wording correction:** the exact connector (136.A1)/(136.H1); equal-rational-lift carrier and gate coherence (136.A4)/(136.H3)/(136.H16); and the statement that the unfactored three-normal determinant is not a representation-independent sufficient certificate under the exact unit-modulus gauge.
* **Promote only as a leading-model identity:** (136.A18), explicitly stated as positivity of \(\sum_{d\mid n}\gamma_d/d\), or of a lift packet after an independently verified common factorisation \(\mathcal A^{\rm lead}_{d,J}=W/d\) with common admissibility.  Do not attach positivity to the full literal amplitude sum.
* **Retain as diagnostic, not as a theorem:** the canonical phase self-return displayed at discovery lines 363--380, the \(L^4\) positive capacity, the same-parity cluster, and the blind fixed-\(Q\) ruling.  Each falsifies a proposed automatic gain but gives no physical lower bound.
* **Revise/reject:** “gauge-invariant cylindrical normal rank,” “the whole literal kernel is intrinsically narrow,” any reading of discovery control line 472 that identifies the blind gradient-vector determinant with the normal determinant, full-literal positivity inferred from (136.A18), and a full exact second-B return without a fresh owner ledger.
* **Leave open with no downstream change:** the complete signed divisor-progressive bulk estimate and all three target obligations.  A continuation must prove one gauge-explicit, owner-preserving scalar inequality jointly in \((h,k,k',d,\mu,J)\), retaining (3.6), the common gates, the slanted profile, and opposite character classes without rulingwise modulus.

Thus the Round-136 conductor decision should remain `broad_narrow_no_go`, but its promotable geometric content is the modulation-invariant method obstruction, not an intrinsic empty-broad decomposition of the literal signed kernel.
