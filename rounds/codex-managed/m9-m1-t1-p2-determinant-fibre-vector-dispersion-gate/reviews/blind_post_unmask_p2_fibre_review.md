# Round 195 blind post-unmask \(P_2\) fibre review

- Campaign: `m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate`
- Role: blind post-unmask normalization, fibre, and scope review
- Blind report SHA-256:
  `f19700d13fc1c5e6f911a7860385fa8a6d9991d74f1791c5ddfa06bb63b00adf`
- Status: review evidence only; no candidate, kernel, graph, synthesis, or
  frozen-report edit

## 1. Result

**Verdict: REVISE the use of the blind evidence.**

The blind report's two signed defect identities, divisor/quadratic fibre
forms, and fixed-packet collision equations are algebraically correct. They
are useful independent checks on the corresponding formulas in the
candidate and the two nonblind reports. Its insistence on a joint literal
Gram, common zero extension, the physical-mask commutator, both
orientations, and one outer real part is also directionally correct.

The proposed \(\gg\sqrt U\) minus fibre and its subsequent quantitative
counterexample are not live-packet evidence. The isolated packet omitted
the inherited relations

\[
 U\mid u,\qquad u=gU,\qquad u\asymp v\asymp L/\kappa,\qquad
 Y<h\le2Y,\qquad 0<2\kappa gh<R_0,\qquad L\ll X^{1/4},       \tag{1.1}
\]

as well as the literal squarefree endpoint support and hard endpoint cone.
The blind specialization \(g=\kappa=\mathfrak m=u=1\), \(U=q=p^2\),
\(L=p^2\), \(X=p^4\), \(Y=2QU\) violates several of (1.1) simultaneously.
Moreover \(U=p^2\) makes the fixed divisor \(\kappa gU\) nonsquarefree, so
the literal endpoint coefficient is zero. The claimed \(\gg\sqrt U\)
family is therefore only an algebraic family in the isolated enlarged
chart; it is not a family of nonzero atoms in the accepted core.

Even if one repairs only \(u=gU\), the target contains the factor
\(u\asymp U\). A coherent subfamily of size \(O(\sqrt U)\) is then far below
\(Q\mathfrak m\kappa u\), rather than a quantitative obstruction to it.
The blind report's asserted asymptotic violation and rank-one block at the
target scale must be rejected.

The arbitrary bounded-coefficient construction survives only as a
**mechanism control**: a theorem uniform over arbitrary arrays, or based
only on support, coefficient moduli, determinant phases, or separate
orientation norms, can be adversarially phase-aligned to capacity. This is
not literal lower mass. The actual live method boundary is supplied by the
nonblind reports' exact same-site all-ones event blocks and by the absence
of a coefficient-sensitive cross-row four-block Gram estimate on
\(P_{2,<D_L}\). The blind report supports that boundary qualitatively but
does not independently supply its quantitative normalization.

The three reported TeX locations—line 139, lines 284--285, and line 378—are
pure transport-only missing-backslash errors before `qquad`. They alter no
symbol, inequality, hypothesis, or argument. A later bounded textual repair
is mathematically safe; this review makes no such edit.

## 2. Exact statement and hypotheses after unmasking

Use \(\mathfrak m\) for the spectral lift gcd. The live packet has

\[
 U=\mathfrak m q>4Q,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,\quad
 U\mid u,\quad g=u/U,                                      \tag{2.1}
\]

\[
 (u,v)=1,\quad (U,h)=1,\quad
 u\asymp v\asymp L/\kappa,\quad
 Y<h\le2Y,\quad0<2\kappa gh<R_0,\quad L\ll X^{1/4}.         \tag{2.2}
\]

On \(P_2\), lower closeness gives \(g=O(1)\). Thus
\(U=u/g\asymp L/(\kappa g)\) and \(v\asymp L/\kappa\), while
\(Y\ll L/(\kappa g)\). The literal endpoint coefficient is nonzero only
when each endpoint product is squarefree and allocation-coprime. In the
plus chart \(d=\kappa gU\), and in the minus chart
\(d'=\kappa gU\). Hence on nonzero literal support

\[
 \kappa gU\ \hbox{is squarefree},\qquad (\kappa,U)=1,\qquad
 U\ \hbox{is odd and squarefree}.                           \tag{2.3}
\]

The exact signed charts are as follows. In the plus orientation, put

\[
 \delta=\kappa(U-v)-2w,\qquad F=\kappa(U-v)+2S>0.
\]

Then

\[
 2h=vF+U\delta-\kappa(U^2-v^2),\qquad
 v(\kappa v+F)=2h-U\delta+\kappa U^2.                       \tag{2.4+}
\]

In the minus orientation, put

\[
 \delta=\kappa(U-v)+2S,\qquad
 F=\kappa(v-U)+2w=-\frac{d'-gm'}g>0.
\]

Then

\[
 2h=UF-v\delta+\kappa(U^2-v^2),                            \tag{2.4-}
\]

\[
 \kappa v^2+\delta v+2h\equiv0\pmod U,\qquad
 F=\frac{2h+\delta v+\kappa v^2}{U}-\kappa U.               \tag{2.5-}
\]

These are exactly the blind formulas, with the minus far defect interpreted
as the positive magnitude of the negative signed upper defect. For fixed
\((\kappa,g,U,v,\delta,h,\omega)\), the far defect is unique. The blind
divisor/quadratic counts fix less data and range over different \(v\)-rows;
they are cross-row algebraic fibre counts, not extra multiplicity inside
one primitive row.

The selected candidate makes the exact physical split

\[
 P_2=P_{2,\ge D}+P_{2,<D},\qquad
 P_{2,\ge D}=P_2\mathbf1_{\{\kappa\ge D_L\}},\quad
 P_{2,<D}=P_2\mathbf1_{\{1\le\kappa<D_L\}}.                 \tag{2.6}
\]

The blind report supplies no proof of the positive large-\(\kappa\) sector.
That proof comes from the two nonblind reports and the candidate's absolute
count. The blind formulas are consistent with it and do not obstruct it.

## 3. Proof and derivation of the post-unmask decisions

### 3.1 Fibre-formula audit

In the plus chart, substituting

\[
 2S=F-\kappa(U-v),\qquad2w=\kappa(U-v)-\delta
\]

in \(2h=2Sv-2Uw\) gives (2.4+). Thus the blind quantity

\[
 C_+=2h-U\delta+\kappa U^2=v(\kappa v+F)>0                 \tag{3.1}
\]

is correct. Fixing \((U,\kappa,h,\delta)\), every permitted \(v\mid C_+\)
determines at most one \(F,S,w\). The displayed divisor count is therefore
a valid algebraic upper count.

In the minus chart, substitution of

\[
 2S=\delta-\kappa(U-v),\qquad2w=F+\kappa(U-v)
\]

in \(2h=2Uw-2Sv\) gives (2.4-) and (2.5-). The discriminant identity

\[
 (2\kappa v+\delta)^2\equiv\delta^2-8\kappa h\pmod U       \tag{3.2}
\]

is also correct; its converse uses \((\kappa,U)=1\), now available from
(2.3). The same-orientation exact collision equations in the blind report
are obtained by subtracting (2.4+) or (2.4-), and its cross-orientation
equation follows by equating their right sides. They are correct for one
fixed packet, where \(U,\kappa,g\) are fixed. They do not control the
square-root phase or literal endpoint-vector inner products.

The live squarefree normalization repairs the apparent large quadratic
multiplicity. For every prime \(p\mid U\), the polynomial
\(\kappa v^2+\delta v+2h\) is a genuine quadratic modulo \(p\), because
\((\kappa,U)=1\). It has at most two roots modulo \(p\). Since \(U\) is
squarefree, the Chinese remainder theorem gives

\[
 \#\{v\bmod U:\kappa v^2+\delta v+2h\equiv0\pmod U\}
 \le2^{\omega(U)}\ll_\varepsilon U^\varepsilon.             \tag{3.3}
\]

The literal \(v\)-support has total length \(O(u)=O(gU)\), and \(g=O(1)\),
so each residue class occurs only \(O(1)\) times. Thus the live cross-row
minus fibre has at most \(U^\varepsilon\) algebraic candidates before the
remaining literal masks. The plus divisor count is likewise harmless after
the usual divisor ledger. Neither fibre count is the missing power.

### 3.2 Why the blind large family is not live

The blind construction set \(g=\kappa=1\), \(U=L=p^2\),
\(\delta=p-1\), \(h=(p-1)^2/8\), and varied \(v\) through
\(\gg p\) roots. Its algebraic endpoint equations and determinant equality
are correct. Its live interpretation fails independently at the following
seams.

1. The blind quantitative shadow also set \(u=1\), whereas (2.1) forces
   \(u=gU=p^2\). Thus \(U\mid u\), the row length, and the target
   normalization were all lost.
2. It set \(Y=2QU\) to force \(T=0\), while its atoms have
   \(h=(p-1)^2/8<U\). This violates the live block condition \(Y<h\).
3. It set \(X=p^4\) and \(L=p^2\), so \(L=X^{1/2}\), contrary to the live
   hard-shell connector \(L\ll X^{1/4}\).
4. The fixed character divisor is \(\kappa gU=p^2\), not squarefree.
   Therefore the literal endpoint coefficient is zero. This is exactly the
   squareful-modulus source of the \(\sqrt U\) quadratic-root multiplicity;
   (3.3) excludes it on nonzero support.
5. With \(g=1\), the constructed lower divisor and cofactor are nearly
   equal, contrary to the literal hard endpoint cone. No residual,
   endpoint, core, Farey, carry, birth/death, or zero-extension survival was
   shown either.

Even ignoring items 2--5 and repairing only item 1, the coherent count is
\(n\asymp\sqrt U\), whereas

\[
 Q\mathfrak m\kappa uX^\varepsilon
 =Q\mathfrak m\kappa gU X^\varepsilon.                     \tag{3.4}
\]

Thus \(n\ll Q\mathfrak m\kappa uX^\varepsilon\), and
\(n^2\ll(Q\mathfrak m\kappa uX^\varepsilon)^2\). The blind family does not
obstruct the fixed-packet target quantitatively.

### 3.3 What remains valid from the arbitrary-coefficient control

For an arbitrary bounded-array theorem class, after exact source
recombination one may choose \(b_x=e(-\Theta_x)\) and set all other entries
to zero. This aligns the chosen support and shows that support-only,
coefficient-modulus-only, phase-only, positive-completion, or separately
normed orientation estimates cannot manufacture cancellation for every
bounded array. That statement is valid as a falsifier of a proposed
mechanism.

It says nothing about the actual Vaaler/profile endpoint products. In the
literal Gram the diagonal can vanish, and no capacity-to-lower-mass
comparison is known. The live exact self-return is instead the one proved
in the hostile report: same-site current channels form an all-ones
\(2\times2\) block, previous channels form an all-ones \(3\times3\) block,
and signed recombination returns the original masked jump. Across rows the
\(++,+-,-+,--\) Gram still contains the actual endpoints, radical phases,
Fejer factors, carries, births/deaths, mask commutator, and zero extensions.

The blind capacity ratio

\[
 \frac{Y\kappa u}{Q\mathfrak m\kappa u}
 =\frac{Y}{Q\mathfrak m}                                  \tag{3.5}
\]

is a correct coarse whole-packet envelope from the isolated statement, but
it is not the sharp post-\(P_2\) obstruction. Lower closeness gives the
small-\(\kappa\) positive capacity \(YuX^\varepsilon\), hence the candidate
ratio \(Y/(Q\mathfrak m\kappa)\); the hostile report records the compatible
worst-band upper ratio

\[
 \min\left\{\frac{Y}{Q\mathfrak m},
             \frac{D_L}{Q\mathfrak m\kappa}\right\}.       \tag{3.6}
\]

All of (3.5)--(3.6) are capacity ratios, never literal lower bounds.

### 3.4 TeX transport audit

The frozen report has `D_L,qquad` at line 139,
`X^\varepsilon,qquad` at lines 284--285, and
`p^2,qquad` at line 378. In every case the intended separator is
`\qquad`; surrounding formulas, tags, and prose make this unique. These are
purely typographical missing-backslash errors and have no mathematical
effect.

## 4. First doubtful or unproved step

After the blind claims are repaired, the first unproved theorem is still

\[
 \left|\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)\right|
 \stackrel{?}{\ll}_{B,C_0,\varepsilon}
 Q\mathfrak m\kappa uX^\varepsilon.                        \tag{4.1}
\]

Neither (3.1), (3.3), multiplicity one at fixed row, nor the anchor aliases
controls the literal off-diagonal Gram. A proof must first recombine the
same-site event channels with their actual signs and then estimate the full
cross-row four-orientation block using the moving endpoint coefficients,
square-root phases, Fejer factors, unequal translations, carries,
births/deaths, physical-mask commutator, and zero extensions. No reviewed
artifact proves that estimate.

The candidate's absolute \(P_{2,\ge D_L}\) theorem is logically separate
and is not challenged by the blind report. The blind report also supplies
no fixed-to-outer proof; the positive strict-sector power ledger comes from
the nonblind count and accepted lift/divisor restoration.

## 5. Exact controls and outcomes

| Control | Outcome |
|---|---|
| `exact_round193_P2_physical_mask` | **PASS.** The blind defect formulas use the exact lower-close/upper-far mask. The large family is not promoted from a dyadic subblock to full \(P_2\). |
| `mask_before_Fourier_and_height_difference` | **PASS in formulation.** The blind report imposed \(P_2\) physically; no post-expansion scalar mask was used. |
| `exact_round192_core_and_T_zero_scope` | **REPAIR.** The abstract scope was retained, but the proposed \(T=0\) example is not live because \(Y=2QU>h\). |
| `strict_T_positive_Farey_covectors` | **INCONCLUSIVE for the family.** No constructed atom was shown to survive the simultaneous strict core inequalities. They remain mandatory in (4.1). |
| `spectral_lift_gcd_vs_physical_cofactor_notation` | **PASS.** The blind formulas kept \(\mathfrak m\) and \(\kappa\) distinct. |
| `both_orientation_primitive_charts` | **PASS.** Equations (2.4+)--(2.5-) agree with the candidate and both nonblind reports. |
| `Delta_minus_Delta_plus_identity` | **PASS.** The plus and signed-minus defect identities and signs are correct. |
| `lower_close_uniform_g_bound` | **PASS.** The blind derivation \(g=O(1)\) is valid and agrees with the live kernel. |
| `upper_failure_positive_far_defect` | **PASS.** Plus has \(+gF>D_L\), while minus has signed upper defect \(-gF<-D_L\). |
| `dyadic_far_defect_partition` | **PASS algebraically.** The partition is exact; it does not make the blind large fibre literal. |
| `determinant_fibre_multiplicity` | **PASS after repair.** The blind cross-row divisor/quadratic equations are correct, fixed-row multiplicity is one, and live squarefreeness gives (3.3). Reject the claimed live \(\sqrt U\) multiplicity. |
| `complete_anchor_Fourier_aggregate` | **INCONCLUSIVE in the blind report.** It was retained abstractly but not reconstructed. The nonblind reports supply the exact anchor identities. |
| `actual_endpoint_coefficient_vectors` | **INCONCLUSIVE in the blind report.** Its common vector notation states the right requirement but gives no literal formula or estimate. |
| `squarefree_coprimality_and_residual_selectors` | **FAIL for the large family.** \(U=p^2\) makes the fixed divisor nonsquarefree; all further selectors were also unaudited. |
| `unequal_endpoint_translations_and_carries` | **INCONCLUSIVE in the blind report.** They were named but not derived. They remain in the live Gram. |
| `birth_death_zero_extension_vectors` | **PASS as a requirement, no estimate.** Common zero extension was correctly demanded; the family did not show literal survival. |
| `physical_mask_commutator` | **PASS as a requirement, no estimate.** It was retained abstractly and cannot be dropped. |
| `Fejer_square_root_phase_cells_crossings` | **INCONCLUSIVE in the blind report.** These fields can destroy determinant-phase collisions and were not evaluated on the family. |
| `one_outer_real_part` | **PASS.** The blind vector inequality kept both orientations and signs before one real part. |
| `TTstar_Gram_before_positive_norms` | **PASS conceptually.** The literal Gram must precede positive norms; the blind abstract Gram is not the exact live event Gram. |
| `Gram_diagonal_and_phase_collisions` | **REVISE.** The arbitrary rank-one block is a false-shadow block, not a literal block. The authoritative live collision blocks are the nonblind same-site \(2\times2\) and \(3\times3\) blocks. |
| `off_diagonal_determinant_fibres` | **PASS algebraically / OPEN analytically.** The blind collision equations are correct at fixed packet; endpoint/radical correlations remain unbounded. |
| `Y_over_HBmfrak_deficit` | **REPAIR.** \(Y/(Q\mathfrak m)\) is the coarse envelope. The small-\(\kappa\) one-close ratios are (3.6) and \(Y/(Q\mathfrak m\kappa)\). |
| `fixed_packet_to_outer_power_ledger` | **NO BLIND SUPPORT.** The blind report correctly left it unproved. The candidate relies on the nonblind strict-sector ledger. |
| `unsigned_character_erased_adversarial_controls` | **PASS only as mechanism falsifiers.** They prove no literal nonvanishing or lower mass. |
| `no_arbitrary_bounded_coefficient_closure` | **PASS after scope repair.** Arbitrary arrays reject a theorem class; they are not substituted for actual coefficients. |
| `no_separate_orientation_norm` | **PASS.** No separate-orientation estimate is licensed for (4.1). |
| `no_width_Farey_or_proper_submask_escape` | **PASS.** \(D_L\) is unchanged. The candidate's strict sector has the exact complement \(P_{2,<D}\); the blind dyadic subfamily proves no full-mask theorem. |
| `diagnostic_only_computation` | **PASS.** No computation was used. |
| `original_t1_only_downstream_scope` | **PASS.** No other original-\(t\) incidence is affected. |
| `no_in_round_owner_pivot` | **PASS.** The review remains on the Round-195 \(P_2\) seam. |
| `exponent_quarantine` | **PASS after rejection.** The blind asymptotic counterexample is discarded; no accepted exponent changes. |
| `inherited_U_divides_u_and_u_equals_gU` | **FAIL in the blind counterexample; repaired here.** Live normalization is \(U\mid u\) and \(u=gU\), not \(u=1\) with \(U=p^2\). |
| `live_height_carrier_shell_normalization` | **FAIL in the blind counterexample.** Its \(Y\), \(h\), \(L\), and \(X\) choices do not lie in one live hard packet. |
| `literal_squarefree_nonzero_support` | **FAIL in the blind large fibre.** Its squareful \(U\) forces zero endpoint weight. |
| `capacity_vs_literal_lower_mass` | **PASS after repair.** Every quantitative ratio is explicitly only an upper-capacity ratio. |
| `transport_only_tex_backslash_hygiene` | **PASS, bounded repair recommended.** The three locations are uniquely determined missing `\` characters before `qquad`; no mathematics changes. |

## 6. Dependencies and exact artifacts used

The review used the following exact artifacts:

1. `protocol.md` —
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
2. `state/proof_obligations.yml` —
   `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`;
3. `state/active_campaign.yml` —
   `7a6762a4030410bce88305638367821bc9280dc2f88f1b201e3403594e41e00d`;
4. the live physical and packet kernels
   `m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`,
   `m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md`,
   `m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`,
   `m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md`, and
   `m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`, with hashes
   respectively
   `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160`,
   `31092b28826b9f36ecaedfb5efc5d7625f4caa4da2cf4c37bd48389c6ac6ee58`,
   `7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2`,
   `301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325`,
   and `470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`;
5. the frozen blind report —
   `f19700d13fc1c5e6f911a7860385fa8a6d9991d74f1791c5ddfa06bb63b00adf`;
6. `reports/literal_p2_determinant_fibre_vector_attack.md` —
   `c617c18c959792622e3df9fe3eb06f47ba61c6948be77f8617c83bda96302879`;
7. `reports/p2_gram_diagonal_collision_hostile_audit.md` —
   `52de40ade4e243cca9e0c50edfee5f913c8120a488407b4f39fe951f22d9b8fb`;
8. `reviews/conductor_round195_report_reconciliation.md` —
   `59c123c7300dddf4a0dbecb3f346318f966702f87dd4e3d198121c6b22a6e538`;
9. `candidates/formalized_hard_m1_t1_p2_large_kappa_sector.md` —
   `c2cb78666e5396260a6a1951aa77f37356190bad44b423d4f4779b7c744e3819`.

No web source or computation was used. No candidate, kernel, frozen report,
state file, synthesis, validation matrix, or other shared artifact was
edited.

## 7. Recommended state effect

**Revise the blind evidence classification; otherwise no change.**

1. Retain the blind plus/minus defect identities, divisor/quadratic fibre
   forms, fixed-packet collision equations, and joint-vector requirement as
   independent algebraic cross-checks after adjoining the live hypotheses
   (2.1)--(2.3).
2. Reject the \(p^2\) large-minus-fibre family, its \(\sqrt U\) live
   multiplicity, its \(T=0\) realization, and its claimed quantitative
   violation as evidence about the literal operator.
3. Retain the arbitrary bounded-array construction only as a false-control
   theorem-class falsifier. Do not treat it as actual endpoint
   nonvanishing, diagonal lower mass, or a disproof of (4.1).
4. Let the candidate's \(P_{2,\ge D_L}\) strict-sector theorem stand or fall
   on its nonblind count/operator/power reviews; the blind report neither
   proves nor contradicts it.
5. Retain \(P_{2,<D_L}\) as the exact open complement and the
   coefficient-sensitive joint cross-row Gram as the first missing theorem.
6. Permit only the later requested bounded `\qquad` hygiene repair to the
   frozen blind report; it changes no mathematical status.

No complete \(P_2\), owner, parent, endpoint theorem, bridge, Gauss-circle
target, or exponent promotion is supported by this review.
