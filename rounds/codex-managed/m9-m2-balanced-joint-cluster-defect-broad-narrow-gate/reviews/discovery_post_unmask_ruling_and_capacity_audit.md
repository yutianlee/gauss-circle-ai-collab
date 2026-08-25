# Discovery post-unmask audit: ruling algebra, cluster capacity, and gradient-chart reconciliation

## 1. Result and exact verdict

**Verdict: certify the hostile obstruction after two explicit scope
repairs; do not certify a target estimate or a literal lower bound.**  At
the frozen graph SHA-256
`c43058006cec6849cd17a49e6a7a5298f5a3c124b34d2333b3279adcb54da1d1`,
the following parts of the hostile report are exact.

1. Equations (136.H1), (136.H3), and (136.H15) correctly restore the
   complete combined linear/residue character, rather than inspecting
   the residue phase alone.
2. The reduced equal-rational-
   \(\lambda\) parametrization
   \((d,\mu)=(bc,ac/2)\), \(c\) odd, is complete, and (136.H16)
   correctly retains every \(c\)-dependent \(\gamma_{bc}\), progression,
   \(J\)-condition, and amplitude.
3. For fixed \((h,k,k',\lambda)\), \(x_*\), \(\rho\), and \(\Delta\)
   are independent of the lift multiplier \(c\).  The gates therefore
   do not separate equal-rational lifts, although their progression
   intervals and amplitudes still may.
4. The same-\(d\), same-parity pigeonhole count (136.H17) is correct as a
   **one-frequency cluster count on one fixed admissible \(v=k'/d\)
   slice**.  It is not by itself a two-normal narrow class under
   (136.H8), and it proves no weighted lower bound.
5. The Hessians (136.H10)--(136.H11) are exact one-body canonical
   Jacobians.  Their nonvanishing is not pairwise or multilinear
   transversality and persists on arithmetically coherent lift families.

Two repairs are mandatory.  First, (136.H18)--(136.H19) do not prove that
the cluster found at one fixed \(v\)-slice survives on a nontrivial common
\(v\)-run with the same literal \(J\)'s, gates, and amplitudes.  They prove
phase proximity at the fixed slice; a common-run intersection lemma is
absent.  Second, (136.H20) and the last line of the capacity table must be
read as **envelope/adversarial capacities**.  From
\(|\mathcal A_{d,J}|\ll(dL)^{-1}\) one obtains only upper capacities, not
the asserted \(\asymp dL\) and \(\asymp1\) actual weighted masses.

With those repairs, the hostile conclusion is sound: local curvature,
liftwise character cancellation, one-frequency spacing, and positive
row norms do not prove the \(L^3\) scalar target.  Nothing in any of the
three reports proves that the literal scalar is large.

## 2. Exact audited statement and hypotheses

The audit keeps the frozen bulk atom

\[
 b_B(h,k)\gamma_d\mathcal A_{d,J}(h,k,k';\mu)
 e(\Theta_{d,\mu}),
\]

with

\[
 h+2s_d=d\ell_d,\qquad \mu=\tfrac12-m,\qquad
 \lambda={\mu\over d},\qquad d\mid k',\quad d\text{ odd},
 \tag{136.R1}
\]

\[
 \Theta_{d,\mu}=R\sqrt{hk}-{Xk'\over2\lambda}
 -{\lambda h\over2}+s_d(\tfrac12-\lambda),\qquad
 x_*={Xk'\over\lambda^2},
 \tag{136.R2}
\]

and both strict gates

\[
 \rho=hk'-x_*k,\qquad \Delta=x_*k'-hk,\qquad
 |\rho|>L,\quad |\Delta|>L.
 \tag{136.R3}
\]

Only the interior bulk is in scope.  The available size information is

\[
 \mu\asymp dL^3,\qquad
 \#\{\mu:t_*\in J\}\asymp dL^3,\qquad
 |\mathcal A_{d,J}|\ll(dL)^{-1},\qquad
 \sum_{d\mid k'}|\gamma_d|\ll_\varepsilon X^\varepsilon.
 \tag{136.R4}
\]

In particular, (136.R4) contains no lower bound, common argument, or
nonvanishing assertion for the actual amplitudes.

Reduce

\[
 2\lambda={a\over b},\qquad (a,b)=1,\qquad a,b\text{ odd}.
\]

Because \(2\mu\) and \(d\) are odd, every and only every lift of this
rational has

\[
 d=bc,\qquad 2\mu=ac,\qquad c\text{ a positive odd integer},
 \qquad bc\mid k'.
 \tag{136.R5}
\]

The exact owner-complete equal-rational packet is therefore the hostile
expression (136.H16), not its later schematic abbreviation (136.H24):

\[
 \begin{aligned}
 &-i\chi_4(h)\chi_4(ab)
 e\!\left(R\sqrt{hk}-{Xbk'\over a}\right)\\
 &\quad\times
 \sum_{\substack{c\text{ odd}\\bc\mid k'}}\gamma_{bc}
 \sum_{J:\,t_*(bc)\in J}^{\rm bulk}
 \mathcal A_{bc,J}(h,k,k';ac/2).
 \end{aligned}
 \tag{136.R6}
\]

Equation (136.R6) may be grouped for an algebraic sign audit, but its
distinct lift summands may not be identified or replaced by one common
amplitude.

## 3. Proof and seam audit

**Character algebra.**  Since \(\ell_d\) is odd,

\[
 -{\lambda h\over2}+s_d(\tfrac12-\lambda)
 ={s_d\over2}-{\mu\ell_d\over2},
\]

and hence

\[
 \begin{aligned}
 e(s_d/2-\mu\ell_d/2)
 &=(-1)^{s_d+m}e(-\ell_d/4)\\
 &=-i(-1)^{s_d+m}\chi_4(\ell_d).
 \end{aligned}
\]

Also \(dh\equiv\ell_d-2s_d\pmod4\), so

\[
 (-1)^{s_d}\chi_4(\ell_d)=\chi_4(d)\chi_4(h).
\]

This proves (136.H1) exactly.  For (136.R5),

\[
 m={1-ac\over2},\qquad
 (-1)^m=\chi_4(ac),\qquad
 (-1)^m\chi_4(bc)=\chi_4(ab),
 \tag{136.R7}
\]

which proves (136.H15), and substitution in (136.R2) proves (136.H3).
Thus equal-rational lifts have the same complete unit phase and character.
This says only that cancellation cannot be attributed to that carrier;
\(\gamma_{bc}\mathcal A_{bc,J}\) can still cancel.

**Lift and gate seam.**  For fixed \(h,k,k'\) and reduced
\(\lambda=a/(2b)\),

\[
 x_*={4Xb^2k'\over a^2}
\]

contains no \(c\).  Therefore (136.R3), including the coupling
\(\Delta+\rho=(k'-k)(h+x_*)\), is identical for all lifts in
(136.R5).  This certifies the hostile gate-invariance statement.  It
does **not** imply that \(t_*(bc)\), the integer progression, \(J\), or
\(\mathcal A_{bc,J}\) is independent of \(c\); (136.R6) correctly keeps
all of them.

**Same-\(d\) cluster count.**  Put

\[
 N_d\asymp dL^3,\qquad Q_d\asymp L/d,\qquad
 \omega_{d,\mu}={Xd^2\over2\mu}.
\]

After the two gate collars remove \(O(dL^2)\) aliases each, there are
still \(\asymp N_d\) aliases on a fixed admissible outer slice.  Split
them into two parities of \(m\), \(O_B(1)\) labels \(J\), and
\(O_c(Q_d)\) arcs of length \(c/Q_d\) on \(\mathbb R/\mathbb Z\).
Pigeonhole gives

\[
 |\mathcal C_d|\gg_c {N_d\over Q_d}\asymp d^2L^2.
 \tag{136.R8}
\]

The parity factor \((-1)^m\) is constant on \(\mathcal C_d\), and at
the fixed value \(v_0=k'/d\asymp Q_d\),

\[
 \| (\omega_{d,\mu}-\omega_{d,\mu_0})v_0\|
 \ll c.
 \tag{136.R9}
\]

This certifies (136.H17) and the fixed-slice phase-cluster control.  It
does not certify the second normal condition in (136.H8), because the
\(t_*\)'s may be separated.  Nor does it certify a common interval of
new \(v\)-values: changing \(v\) changes \(k'\), the gates, \(t_*\),
\(J\), and the amplitude.  The formula corresponding to (136.H18) is a
valid phase identity wherever all terms coexist, but coexistence on a
run of positive length was not proved.

The cluster cardinality is a genuine lower count.  Its weighted claims
are only envelope statements.  After trimming a large cluster to
\(\asymp d^2L^2\) elements if desired, (136.R4) gives

\[
 \sum_{\mu\in\mathcal C_d}|\mathcal A_{d,J}(\mu)|
 \ll dL,\qquad
 \sum_{\mu\in\mathcal C_d}|\mathcal A_{d,J}(\mu)|^2
 \ll1.
 \tag{136.R10}
\]

Neither inequality reverses.  Thus the hostile \(dL/1\) ledger is the
largest allowed coefficient envelope, or an adversarial capacity after
choosing saturating coefficients; it is not an actual-symbol mass.
Likewise, the global \(L^5\) alias triangle and \(L^4\) positive
diagonal are method capacities, not scalar lower bounds.

**One-body Hessian.**  With the hostile variable \(v=k'/d\) and
\(\mu=1/2-m\),

\[
 \Phi_d(v,m)=-{Xd^2v\over2\mu}-{\ell_d\mu\over2}+{s_d\over2},
\]

so

\[
 \det D^2_{v,m}\Phi_d=-{X^2d^4\over4\mu^4}\asymp-1.
 \tag{136.R11}
\]

The formal \((q,\lambda)\) calculation gives the same unit-scale
one-body Jacobian.  These determinants say that the transform on one
sheet is locally invertible.  They compare neither two divisor lattices
nor two complete character-gauged atoms.  Equal-rational lifts provide
the exact hostile countercheck: (136.R11) is nonzero on every sheet even
though their complete unit phases agree by (136.H3).

**Reconciliation of the three gradient geometries.**  Set
\(r=\sqrt{k/h}\), \(z=\lambda/R\).  On a fixed residue sheet, the
unfactored normalized outer gradient is

\[
 G_0(r,z)=(r-z,r^{-1},-z^{-1}).
 \tag{136.R12}
\]

The blind report's determinant of three vectors \(G_0(r_i,z_i)\) and its
area formula are exact.  The normal to the two-parameter surface
\(G_0(r,z)\) is proportional to \((1,r^2,z^2)\).  After the exact lattice
identity (136.H1) moves the linear/residue carrier into the arithmetic
coefficient, the remaining smooth phase has outer gradient

\[
 G_{\rm g}(r,z)=(r,r^{-1},-z^{-1}),
 \tag{136.R13}
\]

whose surface normal is proportional to \((1,r^2,0)\).  Hence every
triple of **surface normals** in the discovery report is coplanar.  This
does not say that every triple of the raw vectors \(G_{\rm g}(r_i,z_i)\)
has zero determinant; gradient-vector and surface-normal determinants
are different objects.

There is no contradiction.  Equations (136.R12) and (136.R13) are two
continuous extensions of the same discrete lattice exponential, related
by an exact arithmetic modulation.  The hostile Hessian (136.R11) is a
third object: the Jacobian from one index sheet to its discrete normal.
The gauge changes the first derivative by the half-character carrier but
does not change this Hessian.  Therefore:

- the blind raw-gradient determinant is exact but gauge-dependent and has
  no supplied norm interface to the fixed scalar;
- the discovery cylindrical-normal collapse is exact for a standard
  coefficient-modulation-invariant surface-normal interface, but is not
  a universal vanishing statement for every possible determinant; and
- the hostile unit Hessian certifies only one-body invertibility, not
  pairwise broadness.

The common conclusion, and the only one licensed for synthesis, is that
no stated determinant has been connected to an owner-preserving
\(L^3\) scalar inequality.

## 4. First failed or unproved seam

The first failed seam in the hostile derivation occurs immediately after
the valid count (136.H17): the passage from a cluster selected on one
fixed \(v=k'/d\) slice to the phrase "a common \(v\)-subrun" in the
discussion of (136.H18)--(136.H19).  Phase proximity on a hypothetical
common run is elementary, but the intersection of the literal support,
both gates, the same \(J\)-owner, and nonvanishing amplitudes over such a
run is not proved.  The lawful conclusion is the fixed-slice statement
(136.R9).

The next scope failure is not algebraic but directional: (136.H20) writes
\(\asymp dL\) and "square mass of order one" although only the amplitude
upper bound (136.R4) is available.  These must be replaced by (136.R10)
or explicitly labeled phase-adapted envelope capacities.  The same
qualification applies to the \(L^5\) and \(L^4\) global ledgers.

Neither repair changes the no-go.  A single admissible sample already
forces the coefficient-uniform large-sieve diagonal, and the accepted
one-frequency calculation already stops at \(L^4\) capacity.  But neither
fact is a lower bound for \(\mathcal K_B^{\rm bulk}\).  The first
remaining analytic step is still a genuinely signed inequality across
the exact packet (136.R6) and the outer \(h,k,k'\) variables, before any
lift, cluster, cap, or row modulus.

## 5. Control tests and outcomes

| Seam or required control | Verdict |
|---|---|
| H1 combined character algebra | **Certified.** The parity and mod-four derivation gives exactly \(-i(-1)^m\chi_4(d)\chi_4(h)\). |
| H3/H15 equal-rational carrier | **Certified.** For \((d,\mu)=(bc,ac/2)\), \((-1)^m\chi_4(d)=\chi_4(ab)\), independently of \(c\). |
| Equal-rational lift parametrization | **Certified with explicit conditions.** \(a,b,c\) are positive odd integers, \((a,b)=1\), and \(bc\mid k'\). |
| Distinct amplitudes and progressions | **Certified in H16, not in schematic H24.** Use (136.R6); keep \(\gamma_{bc}\), \(t_*(bc)\), \(J\), progression, and \(\mathcal A_{bc,J}\) distinct. |
| \(\rho/\Delta\) gate invariance | **Certified for fixed \((h,k,k',\lambda)\).** The gates are common across \(c\); support and progression membership need not be. |
| H17 same-\(d\) cardinality | **Certified at one fixed admissible \(v\)-slice.** Parity, \(J\), and \(O(Q_d)\) frequency arcs leave a class of size \(\gg d^2L^2\). |
| H17 as a full H8 narrow class | **Not certified.** No simultaneous \(N_d^{-1}\)-clustering of \(t_*\) is proved. |
| H18 common \(v\)-run | **Unproved.** The phase relation is valid conditionally, but a common literal run preserving gates, \(J\), and amplitudes is absent. |
| H20 cluster mass | **Scope correction required.** Replace actual \(\asymp dL\) and \(\asymp1\) by the upper/envelope bounds (136.R10). |
| One-body Hessians H10/H11 | **Certified and correctly diagnosed.** They are unit-scale invertible-transform Jacobians, not cross-lift or pairwise transversality. |
| Gauged versus unfactored geometry | **Reconciled.** Raw gradient vectors, frequency-surface normals, and one-body Hessians are three different determinants; none currently has a scalar norm interface. |
| Diagonal and same-denominator controls | **Pass.** The true diagonal fails both far gates; away from it, \(k'=k\) gives \(\Delta=-\rho\), and the retained same-denominator packet remains a narrow/method-capacity control. |
| Opposite-character control | **Pass only as a no-automatic-cancellation test.** H1 exposes the half-shifted carrier; it supplies no pairing of the literal amplitudes or gates. |
| Coherence versus literal lower bound | **No overreach after repair.** H3 is unit-phase coherence only. H17 is cardinality only. No actual weighted lower bound follows. |
| Scalar versus positive energy | **Pass as an obstruction, fail as a substitution.** The \(L^4\) diagonal blocks a coefficient-uniform positive-norm gain but cannot be compared as if it were the signed \(L^3\) scalar. |
| Boundary, transition, and owner scope | **Pass.** No collar, equality case, incomplete stationary mode, or previously owned error is reintroduced. |
| Downstream scope | **Pass.** No BAL, M9-M2, endpoint, M9, quarter, or exponent claim is proved. |

## 6. Dependencies and artifacts used

This post-unmask seam review used exactly the frozen Round-136 packet:

- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/briefs/joint_cluster_defect_broad_narrow_attack.md`;
- `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reports/joint_cluster_defect_broad_narrow_attack.md`;
- `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reports/blind_signed_cluster_kernel_feasibility.md`;
- `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reports/aligned_rational_ruling_hostile_audit.md`.

The audit used the manifest's accepted Round-116 scale and owner facts
only as reproduced in these frozen artifacts.  It used no sibling review,
web source, computation, numerical experiment, shared proof-draft edit, or
graph mutation.  All verdicts are algebraic or capacity-direction audits.

## 7. Recommended state effect

Recommend **retain the three target obligations as open** and close Round
136 under `broad_narrow_no_go`, subject to conductor synthesis.  After
independent seam review, the following are suitable candidate facts for a
scoped obstruction node:

- the exact combined carrier (136.H1);
- the complete equal-rational lift parametrization and coherence identity
  (136.H2)--(136.H3), equivalently (136.H15)--(136.H16), with all lift
  amplitudes and owners distinct;
- invariance of \(x_*\), \(\rho\), and \(\Delta\) across those lifts;
- the statement that (136.H10)--(136.H11) are one-body self-return
  Jacobians, not pairwise broadness certificates; and
- the fixed-slice cluster cardinality (136.H17), only as a
  one-frequency/positive-capacity obstruction.

Do **not** promote a common-\(v\)-run theorem, an actual cluster mass of
size \(dL\), an \(L^4\) lower bound for the physical scalar, or a universal
claim that every conceivable gradient determinant vanishes.  Record the
geometry reconciliation narrowly: the unfactored raw-gradient
determinant, the gauged cylindrical surface-normal rank, and the one-body
Hessian are all exact but inequivalent, and none has the missing fixed-
block scalar norm interface.

No status change is licensed for
`M9-M2-balanced-double-far-oscillatory-remainder`,
`M9-M2-balanced-double-far-actual-energy`, or
`M9-M2-smooth-balanced-quarter-packet-estimate`, and no downstream BAL,
M9-M2, endpoint, M9, or global-exponent promotion is permitted.  Any
continuation must prove a noninvertible signed estimate for the complete
packet (136.R6) jointly with the outer variables and both gates, before
any liftwise or clusterwise modulus.
