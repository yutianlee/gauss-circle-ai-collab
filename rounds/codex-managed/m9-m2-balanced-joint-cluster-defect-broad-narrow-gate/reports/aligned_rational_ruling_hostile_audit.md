# Hostile audit of aligned rational rulings in the balanced bulk kernel

## 1. Result

**Verdict: broad_narrow_no_go.**  The proposed broad--narrow mechanism does not presently certify

\[
 |\mathcal K_B^{\mathrm{bulk}}|
 \ll_\varepsilon L^3X^\varepsilon .
\]

The exact arithmetic obstruction is the complete combined linear/residue carrier

\[
 \boxed{
 e\!\left(-{\lambda h\over2}+s_d(\tfrac12-\lambda)\right)
 =-i(-1)^m\chi_4(d)\chi_4(h).}
 \tag{136.H1}
\]

If \(2\lambda=a/b\) is reduced with \(a,b\) odd, every lift of the same rational is

\[
 (d,\mu)=(bc,ac/2),\qquad c\text{ odd},
 \tag{136.H2}
\]

and the full exponential is independent of the lift multiplier:

\[
 e(\Theta_{bc,ac/2})
 =-i\chi_4(h)\chi_4(ab)
   e\!\left(R\sqrt{hk}-{Xbk'\over a}\right).
 \tag{136.H3}
\]

The quantities \(x_*=Xk'/\lambda^2\), \(\rho\), and \(\Delta\) are also independent of \(c\).  Thus equal-rational lifts have a common phase, character, and gate decision.  Their \(\gamma_{bc}\), divisor progressions, \(J\)-conditions, and amplitudes remain distinct, so coherence does not authorize merging them and does not prove a lower bound.

The post-unmask geometry has three inequivalent determinants: the blind report's determinant of three unfactored gradient vectors, the discovery report's determinant of three surface normals after the exact character gauge, and the one-body Hessians (136.H10)--(136.H11).  The first is exact but gauge-dependent, the second vanishes identically for the gauged cylindrical surface, and the third is a unit-scale canonical Jacobian.  None has a supplied spatial, averaging, or scalar exponential-sum interface that yields a power saving for the fixed number \(\mathcal K_B^{\mathrm{bulk}}\).

The same-\(d\) argument below retains one exact positive fact: on one fixed admissible slice \(v_0=k'/d\), a same-parity, same-\(J\), one-frequency cluster has cardinality \(\asymp d^2L^2\) after trimming.  It need not satisfy the \(t_*\)-proximity condition in (136.H8), it is not proved to persist on a common \(v\)-run, and its weighted \(\ell^1\) and square masses have only upper-envelope bounds.  Consequently the cluster is a coefficient-uniform capacity control, not a physical lower bound.

This is a scoped method obstruction, not a disproof of BAL.  The complete signed divisor-progressive bulk kernel remains the smallest lawful open object.

## 2. Exact statement and hypotheses

Assume exactly (136.B1)--(136.B6).  Thus \(X\ge2\), \(R=\sqrt X\), \(L\asymp X^{1/6}\), there are \(O(L^3)\) balanced outer triples, \(d\mid k'\) is odd, \(\mu=1/2-m>0\), \(\lambda=\mu/d\), and

\[
 |\mathcal A_{d,J}(h,k,k';\mu)|\ll(dL)^{-1}.
\]

Every label \((h,k,k',d,J,\mu)\), coefficient \(b_B(h,k)\gamma_d\), condition \(t_*\in J\), and strict gate \(|\rho|,|\Delta|>L\) remains literal.  Boundary, transition, support-crossing, nonstationary, stationary-remainder, and phase-free owners are not reintroduced.

For \(k'=dv\), put

\[
 \Phi_d(v,m):=\Theta_{d,\mu}-R\sqrt{hk}
 =-{Xd^2v\over2\mu}-{\ell_d\mu\over2}+{s_d\over2},
 \qquad \mu={1\over2}-m,
 \tag{136.H4}
\]

\[
 t_*={1\over2}\left({x_*\over d}-\ell_d\right),
 \qquad
 \omega_{d,\mu}:={Xd^2\over2\mu}.
 \tag{136.H5}
\]

Then

\[
 \nabla_{v,m}\Phi_d=(-\omega_{d,\mu},-t_*).
 \tag{136.H6}
\]

The natural side lengths are

\[
 Q_d\asymp {L\over d},\qquad N_d\asymp dL^3.
 \tag{136.H7}
\]

For two atoms on the same \(d\)-lattice, the conservative two-normal narrow relation is

\[
 Q_d\|\omega_{d,\mu}-\omega_{d,\mu'}\|_{\mathbb R/\mathbb Z}
 \le C_0,\qquad
 N_d\|t_*-t_*'\|_{\mathbb R/\mathbb Z}\le C_0.
 \tag{136.H8}
\]

For \(d\ne d'\), let \(\ell=[d,d']\), \(Q_\ell\asymp L/\ell\), and \(\alpha_\lambda=X/(2\lambda)\).  Equal \(\lambda\), \(\ell>L\), or

\[
 Q_\ell\|\ell(\alpha_\lambda-\alpha_{\lambda'})\|_{\mathbb R/\mathbb Z}
 \le C_0
 \tag{136.H9}
\]

is an arithmetic narrow alternative on the common \(k'=\ell u\) progression.  These relations define a routing partition only; they do not estimate either side.

The one-body Hessians are

\[
 \det D^2_{v,m}\Phi_d
 =-{X^2d^4\over4\mu^4}\asymp-1,
 \tag{136.H10}
\]

and, in the formal \((q,\lambda)\)-chart,

\[
 D^2_{q,\lambda}\Theta
 =\begin{pmatrix}
 0&X/(2\lambda^2)\\
 X/(2\lambda^2)&-Xk'/\lambda^3
 \end{pmatrix},
 \qquad
 \det D^2_{q,\lambda}\Theta=-{X^2\over4\lambda^4}\asymp-1.
 \tag{136.H11}
\]

Also

\[
 \partial_\lambda\Theta
 =-{h\over2}+{Xk'\over2\lambda^2}-s_d
 ={x_*-h-2s_d\over2}=dt_*.
 \tag{136.H12}
\]

To separate the three geometric objects, set \(r=\sqrt{k/h}\) and \(z=\lambda/R\).  Before extracting (136.H1), the normalized outer-gradient surface is

\[
 G_0(r,z)=(r-z,r^{-1},-z^{-1}).
 \tag{136.H12a}
\]

The blind determinant of three vectors \(G_0(r_i,z_i)\) is exact.  After extracting (136.H1), the remaining smooth phase has gradient surface

\[
 G_{\mathrm g}(r,z)=(r,r^{-1},-z^{-1}),\qquad
 N_{\mathrm g}(r,z)\parallel(1,r^2,0),
 \tag{136.H12b}
\]

so every determinant of three gauged surface normals is zero.  This does not make every determinant of three vectors \(G_{\mathrm g}(r_i,z_i)\) zero.  Equations (136.H10)--(136.H11) are a third object: one-sheet canonical Jacobians.  No stated theorem connects any of these determinants to the required fixed-block scalar saving.

## 3. Proof and hostile derivation

**Combined character connector.**  Since \(h+2s_d=d\ell_d\), with \(h,d,\ell_d\) odd,

\[
 -{\lambda h\over2}+s_d(\tfrac12-\lambda)
 ={s_d\over2}-{\mu\ell_d\over2}.
\]

Using \(\mu=1/2-m\),

\[
 \begin{aligned}
 e\!\left({s_d\over2}-{\mu\ell_d\over2}\right)
 &=(-1)^{s_d+m}e(-\ell_d/4)\\
 &=-i(-1)^{s_d+m}\chi_4(\ell_d).
 \end{aligned}
\]

The congruence \(d\ell_d=h+2s_d\pmod4\) gives

\[
 (-1)^{s_d}\chi_4(\ell_d)=\chi_4(d)\chi_4(h),
\]

which proves (136.H1).  The combined term is essential; the residue phase alone is not the carrier.

**Same exact lift.**  For fixed \((d,\mu)\), the \(k'=dv\) packet has carrier

\[
 -i(-1)^m\chi_4(d)\chi_4(h)e(R\sqrt{hk})
 \sum_{v\in I_{d,J}}
 \mathcal A_{d,J}(h,k,dv;\mu)e(-\omega_{d,\mu}v).
 \tag{136.H13}
\]

If

\[
 \|\omega_{d,\mu}\|_{\mathbb R/\mathbb Z}\le \kappa/Q_d,
 \tag{136.H14}
\]

then the reciprocal phase varies by \(O(\kappa)\) on any admissible \(v\)-run of length \(O(Q_d)\).  This is a conditional phase calculation, not a sign or nonvanishing assertion for the actual amplitudes.

**Equal rational \(\lambda\), distinct lifts.**  Let \(2\lambda=a/b\) in lowest terms, with \(a,b\) odd.  The lifts are exactly (136.H2), and

\[
 m={1-ac\over2},\qquad (-1)^m=\chi_4(ac).
\]

Consequently

\[
 (-1)^m\chi_4(d)
 =\chi_4(ac)\chi_4(bc)
 =\chi_4(ab),
 \tag{136.H15}
\]

which proves (136.H3).  The exact aligned lift packet is

\[
 \begin{aligned}
 &-i\chi_4(h)\chi_4(ab)
 e\!\left(R\sqrt{hk}-{Xbk'\over a}\right)\\
 &\quad\times
 \sum_{\substack{c\text{ odd}\\bc\mid k'}}
 \gamma_{bc}
 \sum_{J:\,t_*(bc)\in J}^{\mathrm{bulk}}
 \mathcal A_{bc,J}(h,k,k';ac/2).
 \end{aligned}
 \tag{136.H16}
\]

No character or residue oscillation remains in \(c\), but no identity forces the second line to be positive or nonzero.  Because \(\lambda=a/(2b)\) is common, \(x_*\), \(\rho\), and \(\Delta\) are common; the gates accept or reject all admissible lifts together.  Progression, \(J\), and amplitude admissibility can still differ and are retained in (136.H16).

**Same denominator: fixed-slice one-frequency control.**  Fix \(h,k,d\) and one admissible \(v_0=k'/d\asymp Q_d\).  The two gate collars remove only \(O(dL^2)\) of the \(N_d\asymp dL^3\) aliases, leaving \(\asymp N_d\) bulk aliases at this slice.  Split them by parity of \(m\), by the \(O_B(1)\) literal \(J\)-labels, and into \(O_\kappa(Q_d)\) arcs of length \(\kappa/Q_d\) for \(\omega_{d,\mu}\pmod1\).  Pigeonhole, followed by trimming if necessary, gives a class \(\mathcal C_{d,v_0}\) with fixed parity and a fixed label \(J_0\) such that

\[
 |\mathcal C_{d,v_0}|
 \asymp_\kappa {N_d\over Q_d}
 \asymp d^2L^2.
 \tag{136.H17}
\]

For any \(\mu_0\in\mathcal C_{d,v_0}\),

\[
 \left\|
 (\omega_{d,\mu}-\omega_{d,\mu_0})v_0
 \right\|_{\mathbb R/\mathbb Z}
 \ll\kappa
 \qquad(\mu\in\mathcal C_{d,v_0}).
 \tag{136.H18}
\]

The corresponding selected fixed-slice control is

\[
 \begin{aligned}
 \mathsf S_{d,v_0}(\mathcal C_{d,v_0})
 &:=-i\chi_4(d)\chi_4(h)(-1)^{m_0}e(R\sqrt{hk})\\
 &\quad\times
 \sum_{\mu\in\mathcal C_{d,v_0}}
 \mathcal A_{d,J_0}(h,k,dv_0;\mu)
 e(-\omega_{d,\mu}v_0).
 \end{aligned}
 \tag{136.H19}
\]

The parity carrier is constant and the reciprocal phases are close at \(v_0\).  However, (136.H17)--(136.H19) do not imply the second condition in (136.H8): the values \(t_*(\mu)\) can be separated even though their \(J\)-label is common.  They also do not produce a common nontrivial \(v\)-run.  Changing \(v\) changes \(k'\), the gates, \(t_*\), \(J\)-membership, and the amplitude.  Thus (136.H19) is a one-frequency fixed-slice control, not a certified two-normal narrow packet or a literal lower bound.

The only weighted consequences of the amplitude hypothesis are the upper envelopes

\[
 \sum_{\mu\in\mathcal C_{d,v_0}}
 |\mathcal A_{d,J_0}(h,k,dv_0;\mu)|
 \ll dL,
 \qquad
 \sum_{\mu\in\mathcal C_{d,v_0}}
 |\mathcal A_{d,J_0}(h,k,dv_0;\mu)|^2
 \ll1.
 \tag{136.H20}
\]

Neither inequality reverses.  Arbitrary phase-adapted coefficients saturating the allowed magnitude can realize these as adversarial capacities, so a theorem uniform over that coefficient class cannot infer an extra gain from one-frequency spacing alone.  The actual stationary coefficients may be smaller or cancel; no physical mass estimate follows.

**Character half-shift and canonical self-return.**  Before Poisson summation, the progression character is

\[
 (-1)^{s_d}(-1)^t e(F(t))
 =(-1)^{s_d}e(F(t)+t/2),
 \tag{136.H21}
\]

and the half-lattice frequency \(m\) has stationary equation

\[
 F'(t_*)+{1\over2}-m=0.
 \tag{136.H22}
\]

Thus the primal character creates the half-shifted dual lattice; it is not an independent second source of alias cancellation.  At the canonical phase level, applying the inverse stationary transform returns the primal square-root phase and primal character.  This is a phase self-return check only.  Without a complete second-transform ledger for profiles, endpoints, gates, \(J\)-owners, remainders, and outer coefficients, it is not a full operator identity and cannot itself prove either a gain or a no-gain theorem for the entire bulk owner.

**Near cross-lift rational alternatives.**  On a common \(k'=\ell u\) progression, the reciprocal phase ratio is

\[
 e\!\left(-\ell(\alpha_\lambda-\alpha_{\lambda'})u\right).
 \tag{136.H23}
\]

Under (136.H9) it varies by \(O(1)\) across the available common progression; for \(\lambda=\lambda'\) it is identically one and (136.H16) supplies the full common carrier.  If \(\ell>L\), the progression has at most \(O(1)\) samples.  These are arithmetic routing alternatives, not estimates.

**Power and owner ledger.**  With \(X^\varepsilon\) divisor losses suppressed, every weighted entry below is an upper or adversarial capacity unless explicitly marked as a cardinality:

| item | exact scale or capacity |
|---|---:|
| outer triples \((h,k,k')\) | \(O(L^3)\) |
| aliases per fixed \((h,k,k',d)\) | \(N_d\asymp dL^3\) |
| one stationary amplitude | \(\ll(dL)^{-1}\) |
| alias \(\ell^1\) envelope per row and \(d\) | \(\ll L^2\) |
| alias square envelope per row and \(d\) | \(\ll L/d\) |
| nominal global aliaswise \(\ell^1\) capacity | \(\ll L^5X^\varepsilon\) |
| \(d=1\) positive coefficient-square capacity | \(\ll L^4X^\varepsilon\) |
| accepted one-frequency returned capacity | \(L^4X^\varepsilon\) |
| target | \(L^3X^\varepsilon\) |
| \(v\)-samples | \(Q_d\asymp L/d\) |
| trimmed fixed-slice cluster cardinality | \(\asymp d^2L^2\) |
| cluster \(\ell^1\) / square envelopes | \(\ll dL\) / \(\ll1\) |

At \(d=1\), a coefficient-blind sampling operator already has norm at least \(N_1^{1/2}=L^{3/2}\) on one admissible row, while an \(O(L)\) norm would be needed to convert the global \(L^4\) square capacity to the \(L^3\) target by that route.  This is a coefficient-uniform method obstruction, not a lower bound for the physical scalar.

Finally, the gates cannot be used twice.  Their collars and incomplete stationary terms already have a boundary owner.  In the bulk each collar removes only \(O(dL^2)\) aliases, and, with \(q=k'-k\),

\[
 \Delta+\rho=q(h+x_*).
\]

Thus the gates are coupled rather than independent averaging variables.

## 4. First doubtful or unproved step

The first unproved analytic step is the conversion of any of the exact geometric quantities into a saving for the fixed scalar:

\[
 \text{unfactored gradient determinant, gauged normal rank, or one-body Hessian}
 \quad\centernot\Longrightarrow\quad
 |\mathcal K_B^{\mathrm{bulk}}|\ll L^3X^\varepsilon .
\]

The unfactored gradient-vector determinant is gauge-dependent and lacks a spatial/averaging norm.  The gauged surface-normal determinant is identically zero.  The Hessians (136.H10)--(136.H11) certify only local invertibility on one sheet.  No report supplies an owner-preserving theorem that prices any of them and returns to the one fixed complex number.

The fixed-slice correction prevents a second false seam: (136.H17) is only a cardinality theorem, (136.H18) holds only at \(v_0\), and (136.H20) consists only of upper envelopes.  The class need not obey the \(t_*\)-condition in (136.H8), persist on a common \(v\)-run, carry nonzero physical weight, or force any lower bound.

The first narrow signed problem remains the exact lift sum

\[
 \sum_{\substack{c\text{ odd}\\bc\mid k'}}
 \gamma_{bc}
 \sum_{J:\,t_*(bc)\in J}^{\mathrm{bulk}}
 \mathcal A_{bc,J}(h,k,k';ac/2),
 \tag{136.H24}
\]

jointly with \(b_B(h,k)\), \(\chi_4(h)\), the outer variables, profiles, and both gates.  The hypotheses give divisor \(\ell^1\) control, not cancellation.  The second B-process supplies only the canonical phase self-return described above unless a full owner ledger is added.

## 5. Control tests and outcomes

| required control | outcome |
|---|---|
| literal bulk kernel and owner ledger | Pass.  Every literal label, amplitude, coefficient, profile, gate, and owner remains attached; no previously owned error is reclaimed. |
| divisor progression and distinct lifts | Pass.  Equations (136.H2), (136.H15), and (136.H16) keep every \(\gamma_{bc}\), progression, \(J\)-condition, and amplitude distinct. |
| actual \(\chi_4\) and residue phase | Exact hostile outcome.  The complete carrier is (136.H1), not the residue phase alone; equal-rational lifts have the common sign (136.H15). |
| equal-lift gate coherence | Pass.  Fixed \((h,k,k',\lambda)\) gives common \(x_*,\rho,\Delta\), while progression and amplitude admissibility can differ. |
| joint broad partition | Pass as routing, fail as proof.  Equations (136.H8)--(136.H9) are exhaustive controls but have no scalar estimate attached. |
| fixed-slice H17 cardinality | Pass.  At one admissible \(v_0\), parity, \(J\), and one-frequency pigeonholing yield a trimmed class of cardinality \(\asymp d^2L^2\). |
| H17 as full H8 narrowness | Not proved.  No \(N_d^{-1}\)-clustering of \(t_*\) follows. |
| H18 common \(v\)-run | Rejected.  Equation (136.H18) is asserted only at \(v_0\); no common run preserving gates, \(J\), and amplitudes is claimed. |
| H20 weighted mass | Corrected.  The \(\ell^1\) and square quantities are upper/adversarial capacities \(\ll dL\) and \(\ll1\), never actual \(\asymp\)-masses. |
| unfactored gradient-vector determinant | Exact but gauge-dependent.  It has no supplied scalar norm interface. |
| gauged surface-normal determinant | Exact cylindrical rank collapse.  It does not assert that all gradient-vector determinants vanish and has no scalar closure by itself. |
| one-body Hessians H10/H11 | Exact unit-scale canonical Jacobians, not pairwise or multilinear transversality certificates; no scalar interface is supplied. |
| broad capacity to \(L^3\) | Fail.  The coefficient-uniform positive and one-frequency routes stop at \(L^4\) capacity, one factor \(L\) above target. |
| coherent and opposite-character packets | Equal-rational carriers are coherent.  No weight-, profile-, and gate-preserving opposite-character pairing is supplied; phase adaptation tests only coefficient-uniform claims. |
| second B-process | Scoped to canonical phase/character self-return.  No full owner-preserving transform theorem is claimed without endpoint, gate, profile, \(J\), and remainder ledgers. |
| scalar versus positive energy | The \(L^4\) positive diagonal is a capacity obstruction to that stronger route, not an equivalent scalar target or a physical lower bound. |
| boundary and transition scope | Pass.  No collar, equality case, incomplete stationary term, crossing, nonstationary term, or remainder is put back into the bulk. |
| full BAL owner and downstream scope | No closure.  BAL, full M2, M9, endpoint uniformity, and all exponent claims remain open. |

No numerical or experimental control was used.

## 6. Dependencies and exact artifacts used

This repaired report uses the originally permitted Round-136 context:

- protocol.md;
- state/proof_obligations.yml, at graph SHA-256 c43058006cec6849cd17a49e6a7a5298f5a3c124b34d2333b3279adcb54da1d1;
- state/active_campaign.yml;
- strategy/conductor_0823_full_proof_strategy.md;
- rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/synthesis.md;
- rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md;
- rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/reviews/conductor_round116_literal_alias_and_errors.md;
- rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/reviews/conductor_round116_norm_involution_and_scope.md;
- rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/blind_statement.md;
- rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/briefs/aligned_rational_ruling_hostile_audit.md.

The artifact-repair pass also used the two authorized post-unmask verdicts:

- rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reviews/discovery_post_unmask_ruling_and_capacity_audit.md;
- rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reviews/hostile_post_unmask_determinant_and_character_audit.md.

No web source, numerical computation, symbolic computation, candidate, synthesis edit, proof-draft edit, or shared-state mutation was used.

## 7. Recommended state effect

Close Round 136 under **broad_narrow_no_go**, subject to conductor synthesis.  Recommend retaining as scoped exact evidence:

- the combined carrier (136.H1);
- the complete equal-rational parametrization and coherence identities (136.H2)--(136.H3) and (136.H15)--(136.H16), with all lift amplitudes and owners distinct;
- invariance of \(x_*,\rho,\Delta\) across equal-rational lifts;
- the distinction among the gauge-dependent unfactored gradient-vector determinant, the gauged cylindrical surface-normal rank, and the one-body Hessians, together with the fact that none has the missing scalar interface; and
- the fixed-slice cluster cardinality (136.H17), only as a one-frequency coefficient-uniform capacity obstruction.

Do not promote a full (136.H8) narrow class from (136.H17), a common \(v\)-run, actual cluster mass of size \(dL\), a literal \(L^4\) lower bound, automatic opposite-character cancellation, or a full second-B operator self-return without its owner ledger.

Retain open with no downstream status change M9-M2-balanced-double-far-oscillatory-remainder, M9-M2-balanced-double-far-actual-energy, and M9-M2-smooth-balanced-quarter-packet-estimate.  Any continuation must prove a noninvertible, owner-preserving signed estimate for the complete packet (136.H16)/(136.H24), jointly with the outer variables, literal profiles, and both gates, before any liftwise, clusterwise, capwise, or rowwise modulus.
