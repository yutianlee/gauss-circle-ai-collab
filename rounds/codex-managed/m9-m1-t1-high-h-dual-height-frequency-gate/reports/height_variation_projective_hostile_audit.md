# Round 189 hostile projective-power and literal height-variation audit

- Campaign: m9-m1-t1-high-h-dual-height-frequency-gate
- Task: height_variation_projective_hostile_audit
- Starting graph SHA-256:
  338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c
- Regenerated brief SHA-256:
  fedbbf940f1f443dd51f8982867da23c1c78b7b0a43dead02d1ab9a3dc43d96b
- Status: candidate evidence only; no shared-state edit

## 1. Result and verdict

The corrected baseline is valid:

\[
 j_q(a,v):=|a\bar v_q|_q
 \leq \left\lfloor {mq\over Y}\right\rfloor
 =\left\lfloor {U\over Y}\right\rfloor .
\tag{189.H1}
\]

For fixed \(a,m,q\), it gives \(O(U/Y)\) projective unit classes
and, because \(q\mid U\mid u\), exactly

\[
 O\!\left({u\over q}{U\over Y}\right)
 =O(um/Y)
\tag{189.H2}
\]

literal \(v\)-values. The factor \(m\) in (189.H2) cancels the exact
lift coefficient \(c_U(ma)=m^{-1}c_q(a)\) before divisor summation.
After the \(O(Y)\) heights and \(O(\kappa)\) affine sites are restored,
the \(Y\) also cancels algebraically. The baseline sector is therefore
\(O_{B,\varepsilon}(L^2X^\varepsilon)\).

The adjective “maximal” requires correction. Put

\[
 T_P(q):=\min\!\left\{{q-1\over2},
          \left\lfloor {PU\over Y}\right\rfloor\right\}.
\tag{189.H3}
\]

For \(P=Q\), the legitimate enlarged cutoff is exactly

\[
 T_Q(q)=\min\!\left\{{q-1\over2},
          \left\lfloor {QU\over Y}\right\rfloor\right\},
\tag{189.H4}
\]

and the sector \(j_q(a,v)\leq T_Q(q)\) is still target-safe. More
generally, the same is true for every predeclared fixed power
\(P=(\log(2X))^A\). Hence \(U/Y\) is the power-neutral baseline, not
a unique maximal cutoff under an \(X^\varepsilon\) convention.

The exact fast complement remains under one outer real part with both
orientations and every literal field. A mask-free constant-height
coefficient would gain \(q/j\), but the actual zero-extended endpoint
coefficient has no proved height variation or discrepancy bound. The
first exact Abel remainder retains the complete factor \(Y\). Thus the
strict projective sector is GREEN, while completion of the Round-188
complement is a rigorous NO-GO from the presently permitted inputs.

The centered exact-conductor identities and the prime bad-slope
survivor are valid. They falsify a uniform polylogarithmic kernel-prefix
claim, but prove no literal lower mass. The complete high-height owner
and every downstream owner remain open.

## 2. Exact claim and hypotheses

Fix \(X\geq2\), one nonempty literal middle or lower hard-M1 residual
shell \(L\geq2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\), and

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor,\qquad Y>Q,\qquad
 L\ll X^{1/4}.
\tag{189.H5}
\]

Retain exactly the carrier (K185.27) and amplitudes
(K185.30)--(K185.35):

\[
 \kappa,g,h,U,v>0,\quad
 \kappa,g,U\ {\rm odd},\quad
 (gU,v)=1,\quad(U,h)=1,\quad0<2\kappa gh<R_0,
\tag{189.H6}
\]

\[
 A_{\mathfrak f,\omega}^{\sigma}
 =\sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t),
 \qquad \omega\in\{+,-\}.
\tag{189.H7}
\]

Every selector, squarefree and allocation-coprimality deletion,
profile, floor, star, hard sample, crossing, endpoint, conjugation,
Fejer weight, square-root phase, sign, positivity condition,
orientation, and zero extension remains inside (189.H7).

Work only on the exact Round-188 complement

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y,
\tag{189.H8}
\]

where \(k=ma\), \((a,q)=1\), and \(u=gU\). Since the inherited
carrier has \(U\) odd and \(m\mid U,\ q=U/m\), the three integers
\(U,m,q\) are all odd. Moreover,

\[
 q\mid U\mid u,\qquad (u,v)=1,\qquad
 u,v\asymp L/\kappa,
\tag{189.H9}
\]

\[
 c_U(ma)={1\over m}c_q(a),\qquad
 e\!\left({\epsilon_\omega ma\bar v_Uh\over U}\right)
 =e\!\left({\epsilon_\omega a\bar v_qh\over q}\right).
\tag{189.H10}
\]

For \(P=1,Q\), or \(P=(\log(2X))^A\), let
\(\mathscr S_{Y,Q;P}^{\sigma}\) add
\(j_q(a,v)\leq T_P(q)\) to (189.H8), and let
\(\mathscr F_{Y,Q;P}^{\sigma}\) add the exact complementary predicate
\(j_q(a,v)>T_P(q)\). Before any modulus,

\[
 \mathscr C_{Y,Q}^{\sigma}
 =\mathscr S_{Y,Q;P}^{\sigma}
 +\mathscr F_{Y,Q;P}^{\sigma}.
\tag{189.H11}
\]

The proved claim is

\[
 |\mathscr S_{Y,Q;P}^{\sigma}|
 \ll_{A,B,\varepsilon}L^2X^\varepsilon .
\tag{189.H12}
\]

For \(P=1\), the fast condition is exactly
\(j_q(a,v)>\lfloor U/Y\rfloor\), equivalently \(j_q(a,v)>U/Y\).
For \(P=Q\), replace it only by \(j_q(a,v)>T_Q(q)\).
Both complements retain (189.H6)--(189.H10), both orientations, and
one real part outside every \(h,v,t,a,m,q,U\) and literal field.

## 3. Checks and proof

### Projective multiplicity and the cap

Because \(q\mid u\) and \((u,v)=1\), every admissible \(v\) is a unit
modulo \(q\). For fixed unit \(a\), the map
\(v\mapsto a\bar v_q\) is a bijection of
\((\mathbb Z/q\mathbb Z)^\times\). Since \(q\) is odd, the number of
unit slopes with \(1\leq j_q(a,v)\leq T_P(q)\) is exactly

\[
 2\sum_{\substack{1\leq r\leq T_P(q)\\(r,q)=1}}1
 \leq 2T_P(q).
\tag{189.H13}
\]

The two sides \(r\) and \(-r\) are distinct. If \(T_P=0\), the sector
is empty. If \(T_P=(q-1)/2\), (189.H13) equals \(\varphi(q)\), so
the cap contains every unit slope without overlap.

The literal \(v\)-range has total length \(O(u)\). Each residue class
modulo \(q\) occurs \(O(u/q+1)=O(u/q)\) times because \(q\mid u\).
The condition \((u,v)=1\) only deletes values. Therefore

\[
 \#\{v:j_q(a,v)\leq T_P(q)\}
 \ll {uT_P(q)\over q}
 \ll u\min\!\left(1,{Pm\over Y}\right).
\tag{189.H14}
\]

At \(P=1\), this is the required \(O(um/Y)\), including interval
endpoints and the floor-zero case.

### Exact \(1/m\), \(Y\), and divisor ledger

At fixed \((\kappa,u,U=mq,a)\), multiply:

- \(O(uT_P/q)\) admissible \(v\)'s;
- \(O(Y)\) heights;
- \(O(1+\kappa)=O(\kappa)\) affine sites per oriented row;
- two orientations, an absolute constant;
- \(O_\eta(X^\eta)\) per literal endpoint atom; and
- the exact coefficient \(|c_q(a)|/m\).

The result is

\[
 \kappa u|c_q(a)|X^\eta\,{YT_P(q)\over U}.
\tag{189.H15}
\]

Since \(T_P(q)\leq PU/Y\),

\[
 {YT_P(q)\over U}\leq P.
\tag{189.H16}
\]

For \(P=1\), (189.H15) displays both exact cancellations: the
\(m\) from \(um/Y\) cancels \(1/m\), and the height factor \(Y\)
cancels \(1/Y\). No \(Y^\delta\) is absorbed later.

The unit-frequency mass satisfies

\[
 \sum_{a\in\mathbb U(q)}|c_q(a)|\ll\log(2q),
\tag{189.H17}
\]

and the lift/conductor labels satisfy exactly

\[
 \sum_{U\mid u}\sum_{q\mid U}1
 =\sum_{mq\mid u}1=\tau_3(u).
\tag{189.H18}
\]

There is no fourth free divisor. Hence

\[
 |\mathscr S_{Y,Q;P}^{\sigma}|
 \ll_\eta P X^\eta
 \sum_{\kappa}\sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log(2u)
 \ll P L^2\log^{O(1)}(2L)X^\eta.
\tag{189.H19}
\]

For \(P=Q\) or a fixed logarithmic power, (189.H19), (189.H5), and a
fresh \(\eta<\varepsilon\) prove (189.H12).

If \(Pm\geq Y\), then \(PU/Y=Pmq/Y\geq q\), so the cutoff is
saturated at \((q-1)/2\) and all unit slopes are paid. Directly, all
\(O(u)\) values of \(v\), followed by \(Y\) heights and \(1/m\),
cost \(Y/m\leq P\). The cap may occur earlier, at
\(PU/Y\geq(q-1)/2\); (189.H16) still applies. For \(P=Q\), the
actual condition \(Qm<Y\) excludes \(Qm\geq Y\), but permits this
earlier cap. If capped, the \(Q\)-fast complement is empty for that
lift.

This proves the \(Q\)-enlarged sector and refutes unique maximality.
Any fixed logarithmic \(P\) is absorbable; a fixed positive power
\(P=X^\delta\) is not uniformly absorbable for arbitrary epsilon.

### Exact complement and literal height variation

For fixed \(a,v,q,\omega\), put
\(b=\epsilon_\omega a\bar v_q\) and \(j=|b|_q\). A genuinely
constant coefficient on an unmasked interval obeys

\[
 \left|\sum_{H<h\leq H+Y}e(bh/q)\right|
 \ll \min\{Y,q/j\}.
\tag{189.H20}
\]

On a dyadic band \(J<j\leq2J\), there are \(O(uJ/q)\) relevant
\(v\)'s and (189.H20) contributes \(O(q/J)\); their product is
\(O(u)\). This is only a normalization check. Even the literal
condition \((U,h)=1\) is a moving mask. Möbius-opening it creates
divisor progressions, including resonant ones; it does not prove
bounded variation. All other literal fields create further changes.

Define the complete zero-extended row sequence

\[
 F_{\kappa,u,m,q,v,\omega}^{\sigma}(h)
 :=\mathbf1_{Y<h\leq2Y}\,
   \mathbf1_{\rm all\ literal\ carrier\ and\ endpoint\ predicates}
   A_{(\kappa,u/(mq),h,mq,v),\omega}^{\sigma}
\tag{189.H21}
\]

and

\[
 V_Y(F):=\sum_{h\in\mathbb Z}|F(h+1)-F(h)|.
\tag{189.H22}
\]

Exact Abel summation gives

\[
 \left|\sum_hF(h)e(bh/q)\right|
 \ll {q\over j}V_Y(F).
\tag{189.H23}
\]

A sufficient fast-band input would be

\[
 \sum_{\omega}\sum_{\substack{v\ {\rm literal}\\
                    J<j_q(a,v)\leq2J}}
 V_Y(F_{\kappa,u,m,q,v,\omega}^{\sigma})
 \ll_\eta \kappa X^\eta {uJ\over q}.
\tag{189.H24}
\]

No permitted result proves (189.H24). The available estimate is only

\[
 |F(h)|\ll_\eta\kappa X^\eta,\qquad
 V_Y(F)\leq2\sum_h|F(h)|
 \ll_\eta Y\kappa X^\eta.
\tag{189.H25}
\]

Thus (189.H23) returns \(O(YL^2X^\varepsilon)\), the full positive
capacity. The quantitative deficit is exactly the complete factor
\(Y\).

The first literal jump is also exact. If
\(\widetilde B_h(t)=\mathbf1_{I_h}(t)B_h(t)\), including every zero
extension, then

\[
 F(h+1)-F(h)
 =\sum_t(-1)^t\{\widetilde B_{h+1}(t)-\widetilde B_h(t)\}.
\tag{189.H26}
\]

Splitting into \(I_h\cap I_{h+1}\), births
\(I_{h+1}\setminus I_h\), and deaths \(I_h\setminus I_{h+1}\)
is exact. Changing \(h\) changes \((U,h)=1\),
\(r=2\kappa gh\), the Fejer weight, anchors, affine ranges,
endpoints \(N,N+r\), squarefree/coprime masks, residual selector,
profiles, floors, stars, crossings, conjugation, square-root phase,
and terminal zero extension. The inherited deletion controls prohibit
assuming translation invariance, but prove no lower mass. Neither the
common term nor the birth/death terms has a proved improvement over
(189.H25).

### Centered conductor and prime bad slope

For a unit \(b\bmod q\), define

\[
 K_q(b)=\sum_{a\in\mathbb U(q)}c_q(a)e(ab/q),\qquad
 K_q^\circ(b)=K_q(b)-{\mu(q)\over q}.
\tag{189.H27}
\]

Exact-conductor inversion and Möbius inversion give

\[
 E_U(b)=\sum_{q\mid U}{q\over U}K_q(b),\qquad
 K_q(b)={1\over q}\sum_{d\mid q}\mu(q/d)dE_d(b).
\tag{189.H28}
\]

For odd \(d>1\) and unit \(b\), \(E_d(-b)=-E_d(b)\). The sole
\(d=1\) trace yields

\[
 K_q(b)+K_q(-b)={2\mu(q)\over q},\qquad
 K_q^\circ(-b)=-K_q^\circ(b).
\tag{189.H29}
\]

For prime \(p\),

\[
 K_p(b)=E_p(b)-{1\over p},\qquad K_p^\circ(b)=E_p(b).
\tag{189.H30}
\]

At the projective slope \(b=-2\), for
\(1\leq h\leq(p-1)/2\),
\([-2h]_p=p-2h\) is odd. Every such \(h\) is a unit, so

\[
 \sum_{h=1}^{(p-1)/2}K_p^\circ(-2h)
 =-{p-1\over2}.
\tag{189.H31}
\]

This is the exact bad-slope survivor. It falsifies a uniform
polylogarithmic prefix theorem for the full centered kernel. It does
not lower-bound the literal aggregate: it sums the full
exact-conductor \(a\)-set, while the open packet retains the ordinary
edge deletion, slow/fast split, dyadic endpoint coefficient, both
orientations, and all masks.

## 4. First doubtful or unproved step

There is no doubtful step in the oddness of \(U,m,q\), projective
bijection, capped two-sided count, \(O(um/Y)\) baseline, \(1/m\)
cancellation, \(Q\)-enlarged cutoff, \(\tau_3\) ledger, exact
complement, centered trace, or prime bad-slope parity.

The first unproved relation is (189.H24), or an equally strong jointly
signed discrepancy estimate inserted before separating \(a,v,h,t\)
or the two orientations. The exact first difference is (189.H26);
the only established bound is (189.H25), too large by \(Y\).

This is a mechanism no-go, not a disproof. Abstract bounded amplitudes
can dephase the height, affine parity, and square-root phases and attain
positive capacity, but are not the actual Vaaler/\(\chi_4\) endpoint
coefficient. Conversely, (189.H31) is a full-kernel falsifier, not
literal lower mass.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| exact_round188_Qm_lt_Y_complement | PASS: all four predicates in (189.H8) remain. |
| literal_K185_27_30_35_carrier | PASS: (189.H6)--(189.H7), (189.H21), and (189.H26) retain every field. |
| single_outer_real_part_and_both_orientations | PASS: (189.H11) is split before modulus; the fast term stays joint. |
| dual_frequency_j_abs_a_v_inverse_mod_q | PASS: (189.H1) and (189.H10) use the corrected reduced inverse. |
| projective_residue_bijection_and_two_sided_count | PASS: (189.H13) handles both sides, zero, and saturation. |
| q_divides_U_divides_u_v_interval_multiplicity | PASS: (189.H14) includes interval endpoints. |
| per_v_O_kappa_affine_sites | PASS: the \(O(1+\kappa)\) term is retained. |
| exact_cU_m_inverse_cq_normalization | PASS: (189.H10) retains \(1/m\). |
| slow_j_le_floor_U_over_Y_sector_and_exact_complement | PASS, with “maximal” repaired. |
| Q_enlarged_cutoff_cap_and_saturation | PASS: (189.H4), (189.H16), and the saturated ledger are exact. |
| full_factor_Y_before_positive_recombination | PASS for the strict family; FAIL for the fast complement by (189.H25). |
| kappa_u_m_q_divisor_power_ledger | PASS: (189.H18)--(189.H19) give exactly \(\tau_3\). |
| centered_exact_conductor_identity | PASS: (189.H27)--(189.H30) retain the trace. |
| prime_bad_slope_height_prefix_survivor | PASS with no-lower-mass quarantine. |
| selector_squarefree_coprime_deletions | PASS as scope/barrier; no invariance inferred. |
| profile_endpoint_phase_zero_extension | PASS as scope/barrier in (189.H21), (189.H26). |
| no_invented_height_BV_or_periodicity | PASS as a no-go: only (189.H25) is known. |
| no_positive_large_sieve_Poisson_alias_energy | PASS as a no-go: positive norms return capacity. |
| false_unsigned_and_adversarial_controls | PASS with explicit diagnostic-only scope. |
| original_t1_only_downstream_scope | PASS: even fast success affects only the exact original-\(t=1\) chain. |
| exponent_quarantine | PASS: no downstream status or exponent changes. |

## 6. Dependencies and exact artifacts used

Only the regenerated brief and its permitted context were used:

1. briefs/height_variation_projective_hostile_audit.md —
   fedbbf940f1f443dd51f8982867da23c1c78b7b0a43dead02d1ab9a3dc43d96b.
2. protocol.md —
   f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
3. state/proof_obligations.yml —
   338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c.
4. state/active_campaign.yml —
   966a17240b3a8c62900a54af6c4c5df1b86065025387c7eefcad9863fb342c70.
5. strategy/round189_m1_t1_high_h_dual_height_frequency_strategy.md —
   9daac6924dda273bc49ffd674122d7960af30460720c76705cf07c7e9d7212ad.
6. proofs/kernels/m9_m1_hard_top_t1_high_h_imprimitive_lift_gcd_reduction.md —
   ca313d2ed11884bdb3ff237c51380de7aadd713a5dc01b565935fbdb8fe9744a.
7. proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md —
   a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2.
8. proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md —
   4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160.
9. reports/lift_power_completion_hostile_audit.md —
   1f27281d91fd7290f548e3c1dfa696f2a6a9b82e184f8bc878747a29f1a3dce1.
10. reports/deletion_resonance_capacity_audit.md —
    5a09310baf8574bf1f2c841cd179a66d22aa5834cc50be555a11ad969569db1a.

No external theorem or web source was used. No new computation was used
as theorem evidence; inherited finite controls remain diagnostic only.

## 7. Recommended state effect

Revise, then retain as candidate evidence pending independent seams.

1. Promote only the exact projective count and strict-family bound
   (189.H12). The baseline \(P=1\) is valid, and the wider
   \(P=Q\) cutoff is exactly (189.H4).
2. Remove any claim that \(\lfloor U/Y\rfloor\) is uniquely maximal.
   Any fixed logarithmic \(P\) is target-safe; call \(U/Y\) the
   power-neutral baseline.
3. Keep \(\Re\mathscr F_{Y,Q;P}^{\sigma}\) open, with (189.H24) or
   an equally strong coupled discrepancy estimate as the first missing
   input and the factor-\(Y\) deficit (189.H25) explicit.
4. Record (189.H29)--(189.H31) only as exact mechanism controls.
   Reject assumed BV, uniform kernel-prefix, positive completion, large
   sieve, Poisson, alias-energy, and arbitrary-bounded-weight closures;
   assert no literal lower mass.
5. Keep every original \(t\geq2\) small-\(G\) incidence, the
   large-\(G\) near-resonant complement, both M1 parents, every M2
   owner, endpoint uniformity, M9, both bridges, the quarter theorem,
   and every exponent unchanged and open.

Recommended unique Round-189 exit label:

dual_height_actual_coefficient_discrepancy_no_go.
