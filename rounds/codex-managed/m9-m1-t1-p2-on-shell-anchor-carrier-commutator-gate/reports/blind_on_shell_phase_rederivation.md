# Blind on-shell phase rederivation (Round 196)

## 1. Result

**Conditional exact carrier lemma, followed by a route-scoped self-return.**
Put \(A=\kappa U\), let \(s\in\{+1,-1\}\) denote the frequency sign, and
let \(\overline 2_q\) be the inverse of \(2\pmod q\).  On either
orientation's shell,
\[
 \epsilon_\omega\overline v_qh\equiv \overline2_qx\pmod q,
\]
and hence
\[
 (-1)^S e\!\left(\frac{s\epsilon_\omega a\overline v_qh}{q}\right)
 =e(-A/4)e\!\left[\left(\frac14+\frac{sa\overline2_q}{q}\right)x\right].
 \tag{1}
\]
If \(A\) and \(x\) are odd, (1) is precisely
\[
 \chi _4(A)\chi _4(x)e(sa\overline2_qx/q).                 \tag{2}
\]
If \((a,q)=1\), the phase in (1) has primitive additive modulus \(4q\), and
its \(x\mapsto x+2\) multiplier is
\[
 z_s=-e(sa/q).
 \tag{3}
\]
With \(c_q(sa)=2/[q\{1+e(-sa/q)\}]\),
\[
 (1-z_s)c_q(sa)=\frac{2e(sa/q)}q.                          \tag{4}
\]

Equation (4) removes the near-singular denominator only when the
**literal, fully recombined, zero-extended coefficient event sequence** is
an actual step-two difference.  With
\(\tau_2B(x)=B(x-2)\) and \(\Delta_2=1-\tau_2\), the required identity is
\[
 \mathcal A_{s,a}(x)=\Delta_2\mathcal B_{s,a}(x)
 \quad\text{or}\quad
 \mathcal A_{s,a}=\Delta_2\mathcal B_{s,a}+\mathcal E_{s,a}
 \text{ with an exactly priced complement}.               \tag{5}
\]
It must hold before any positive norm, while orientations and signs remain
under the single outer real part.  Then, and only then,
\[
\begin{aligned}
 c_q(sa)\sum_xF_{s,a}(x)\mathcal A_{s,a}(x)
 &=\frac{2e(sa/q)}q\sum_xF_{s,a}(x)\mathcal B_{s,a}(x)\\
 &\quad+c_q(sa)\sum_xF_{s,a}(x)\mathcal E_{s,a}(x),
\end{aligned}                                               \tag{6}
\]
where \(F_{s,a}\) is the carrier in (1).

The isolated data do not define \(\mathcal A_{s,a}\), its endpoint event
vectors, its changing fibres, or
\(\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)\).  They therefore do not
supply (5), the required zero-mass/bounded-primitive control, or estimates
for any commutator in Section 3.  The known positive capacity is
\(u\{\kappa+\min(Y,D_L)\}X^\varepsilon\), while
\(\min(Y,D_L)/(Q\mathfrak m\kappa)>1\).  Thus neither the full target nor a
target-safe strict sector with a priced complement follows.  The exact
outcome is a self-return at the genuine-\(\Delta_2\) gate: manufacturing a
cumulative primitive can lose one full carrier length and exactly return
the gain \(1/q\) in (4).

## 2. Exact statement and hypotheses

Let \(e(t)=\exp(2\pi i t)\).  Assume exactly the packet hypotheses in the
isolated statement:
\[
 U=\mathfrak m q\ \text{is odd},\quad q>Q,\quad U>4Q,
 \quad (v,U)=1,\quad \kappa<D_L,
 \quad M:=\min(Y,D_L)>Q\mathfrak m\kappa,
\]
with all displayed shell variables integral.  Since \(q\mid U\), \(q\) is
odd; hence both \(\overline v_q\) and \(\overline2_q\) exist.
The frozen brief also stipulates the physical-coordinate identifications
\[
 x=\kappa v+\eta=\kappa U+2S=d'/g\quad\text{in the plus chart},
 \qquad
 x=\kappa v+\delta=\kappa U+2S=d/g\quad\text{in the minus chart}. \tag{H}
\]
They are retained exactly; the equalities to \(d'/g\) and \(d/g\) cannot
be rederived from the displayed shell equations because those physical
variables are not otherwise defined in the isolated packet.

For the word **primitive**, one additionally needs the exact-conductor
hypothesis \((a,q)=1\).  It is suggested by the phrase
“exact-conductor coefficient” but is not explicitly stated in the
permitted packet statement.  Without it, the carrier can factor through a
proper divisor of \(4q\).

For the literal \(\chi _4(A)\chi _4(x)\) form (2), one additionally needs
\(A=\kappa U\) and \(x\) odd, equivalently \(\kappa\) odd because \(U\) is
odd and \(x=A+2S\).  This oddness is also not explicit in the permitted
statement.  Formula (1) is valid with no extra parity hypothesis.  Under
the standard Dirichlet-character convention, when \(A,x\) are even the
right side of (2) is zero and cannot equal the unit-modulus left side.  The
exact even-lattice replacement is
\[
 (-1)^S=\chi _4(A+1)\chi _4(x+1).                          \tag{7}
\]

For (6), \(\mathcal A_{s,a}\), \(\mathcal B_{s,a}\), and
\(\mathcal E_{s,a}\) must be finitely supported on the complete parity
lattice \(x\equiv A\pmod2\), after zero extension across every legal-domain
boundary.  The sums in (5)--(6) must include the full \(T=0\) branch and
all strict \(T\ge1\) Farey-core branches, both orientations, both frequency
signs, every physical mask and arithmetic selector, and all endpoint
events.

## 3. Proof or derivation

In the plus chart, \(\eta=x-\kappa v\).  Substitution gives
\[
\begin{aligned}
 2h
 &=v(x-\kappa v)+U\delta-\kappa(U^2-v^2)\\
 &=vx+U\delta-\kappa U^2,
\end{aligned}
\]
so \(2h\equiv vx\pmod q\), and therefore
\[
 \overline v_qh\equiv\overline2_qx\pmod q.                 \tag{8}
\]
In the minus chart, \(\delta=x-\kappa v\), so
\[
\begin{aligned}
 2h
 &=U\eta-v(x-\kappa v)+\kappa(U^2-v^2)\\
 &=U\eta-vx+\kappa U^2.
\end{aligned}
\]
Thus \(\overline v_qh\equiv-\overline2_qx\pmod q\);
multiplying by \(\epsilon_-=-1\) gives exactly (8).  This proves the same
anchor phase in both orientations.  Replacing \(a\) by \(sa\)
simultaneously handles the two frequency signs without separating their
norms.

Since \(x=A+2S\),
\[
 (-1)^S=e(S/2)=e((x-A)/4)=e(-A/4)e(x/4),                  \tag{9}
\]
which proves (1).  If \(A,x\) are odd, the definition
\(\chi _4(n)=(-1)^{(n-1)/2}\) gives
\[
 \chi _4(A)\chi _4(x)
 =(-1)^{(A+x-2)/2}=(-1)^{(x-A)/2}=(-1)^S,
\]
because the difference of the first two exponents is \(A-1\), an even
integer.  This proves (2), and the same calculation with \(A+1,x+1\)
proves (7) on the even lattice.

Choose any integer representative of \(\overline2_q\) and set
\[
 r_s=q+4sa\overline2_q.
\]
Apart from the constant \(e(-A/4)\), (1) is \(e(r_sx/(4q))\).  If
\((a,q)=1\), then \(r_s\) is odd and
\[
 (r_s,q)=(4sa\overline2_q,q)=1,
\]
so \((r_s,4q)=1\).  The modulus is therefore primitive.  Equivalently, on
the parity lattice,
\[
 \frac{F_{s,a}(x+2)}{F_{s,a}(x)}
 =e(1/2)e(2sa\overline2_q/q)=-e(sa/q)=z_s.                \tag{10}
\]
The numerator \(q+2sa\) of \(z_s=e((q+2sa)/(2q))\) is coprime to \(2q\),
so \(z_s\) has order \(2q\), corresponding to the \(x\)-period \(4q\).

Writing \(w_s=e(sa/q)\), one has \(z_s=-w_s\) and
\[
 (1-z_s)c_q(sa)
 =(1+w_s)\frac{2}{q(1+w_s^{-1})}
 =\frac{2w_s}{q},
\]
which proves (4).  The denominator never vanishes for integral \(a\) and
odd \(q\): \(e(-sa/q)=-1\) would equate an even integer with an odd
integer modulo \(2q\).

For a fully zero-extended finite sequence \(B\), a change of variable gives
\[
\begin{aligned}
 \sum_xF_{s,a}(x)\Delta_2B(x)
 &=\sum_xF_{s,a}(x)B(x)
   -\sum_xF_{s,a}(x)B(x-2)\\
 &=(1-z_s)\sum_xF_{s,a}(x)B(x).                            \tag{11}
\end{aligned}
\]
Combining (11) with (4) proves (6).  If one sums only over a truncated
index interval \(l\le n\le r\), where \(x=x_0+2n\), then instead
\[
 \sum_{n=l}^rF_n(B_n-B_{n-1})
 =(1-z_s)\sum_{n=l}^rF_nB_n
   +z_sF_rB_r-z_sF_{l-1}B_{l-1}.                          \tag{12}
\]
Thus endpoints cannot be discarded; full zero extension merely records
them as birth/death terms one step outside the old support.

Here is the literal commutator ledger forced when the proposed difference
is opened.  For \(\Delta_2=1-\tau_2\),
\[
 \Delta_2(fg)=(\Delta_2f)g+(\tau_2f)(\Delta_2g),
 \qquad [\Delta_2,M_f]=M_{\Delta_2f}\tau_2,                \tag{13}
\]
and, for an ordered product,
\[
 \Delta_2\!\left(\prod_{j=1}^Jf_j\right)
 =\sum_{j=1}^J
   \left(\prod_{i<j}\tau_2f_i\right)(\Delta_2f_j)
   \left(\prod_{i>j}f_i\right).                            \tag{14}
\]
The literal event product has, at minimum, the following factors (some may
be vector-valued): zero-extension/legal-domain support \(Z\); diagonal
selector \(D\); collision/multiplicity selector \(C\); actual endpoint
product \(E_{\rm end}\); physical mask \(P_2\); the direct sum of the
\(T=0\) and strict \(T\ge1\) Farey-core selectors \(F_T\); residual and
divisibility selectors \(R\); squarefree/coprimality masks \(G\);
carry/cell/crossing/unequal-translation event maps \(K\); Fejer weight
\(V\); amplitude \(W_0\); and square-root phase \(e(\Phi)\).  Formula (14)
produces, with no permitted deletion:

1. \((\Delta_2Z)\)-terms: outer endpoints, zero-extension faces, and all
   affine births and deaths;
2. \((\Delta_2D)\)- and \((\Delta_2C)\)-terms: diagonal entry/exit,
   collisions, multiplicity changes, and non-bijective reindexing;
3. \((\Delta_2E_{\rm end})\)-terms: every shifted endpoint product and
   endpoint crossing, including unequal translations;
4. \((\Delta_2P_2)\)-terms: the physical-mask commutator;
5. \((\Delta_2F_T)\)-terms: both the \(T=0\) boundary events and crossings
   of every simultaneous strict \(T\ge1\) Farey condition;
6. \((\Delta_2R)\)- and \((\Delta_2G)\)-terms: residual/divisibility
   changes and squarefree or gcd flips;
7. \((\Delta_2K)\)-terms: carries, cell crossings, changed affine fibres,
   conjugation/reorientation changes, and further births/deaths;
8. \((\Delta_2V)\)-terms: Fejer variation and its endpoint support;
9. \((\Delta_2W_0)\)- and \(\Delta_2e(\Phi)\)-terms: amplitude variation
   and the exact square-root-phase increment
   \[
    \Delta_2e(\Phi)(x)
    =e(\Phi(x-2))\{e(\Phi(x)-\Phi(x-2))-1\};               \tag{15}
   \]
10. if \(\mathcal R_x\) is the orientation/sign/carry reindexing map, its
    unavoidable recombination commutator
    \[
      \Delta_2(\mathcal R_xE_x)
      =\mathcal R_x\Delta_2E_x
       +(\mathcal R_x-\mathcal R_{x-2})E_{x-2}.             \tag{16}
    \]

For the stated physical mask, write
\[
 N(x)=\mathbf1_{\{|d-gm|\le D_L\}},\qquad
 H(x)=\mathbf1_{\{|d'-gm'|>D_L\}}.
\]
Because the mask is imposed before differencing, (13) gives the exact term
\[
 \Delta_2P_2=(\Delta_2N)H+(\tau_2N)(\Delta_2H).             \tag{17}
\]
It is supported on literal threshold changes under the actual event
translation; it is not zero merely because \(x\) changes by two.  If a raw
difference is first found behind the mask, then
\[
 P_2\Delta_2B=\Delta_2(P_2B)-(\Delta_2P_2)\tau_2B,         \tag{18}
\]
so the first term receives (4), while the mask commutator retains the
original \(c_q(sa)\).

Likewise, if the event fibre at \(x\) is \(\mathcal J_x\), use one global
label set and zero extension.  Then exactly
\[
\begin{aligned}
 \Delta_2\sum_{\lambda\in\mathcal J_x}b_{x,\lambda}
 &=\sum_{\lambda\in\mathcal J_x\cap\mathcal J_{x-2}}
       (b_{x,\lambda}-b_{x-2,\lambda})\\
 &\quad+\sum_{\lambda\in\mathcal J_x\setminus\mathcal J_{x-2}}
       b_{x,\lambda}
 -\sum_{\lambda\in\mathcal J_{x-2}\setminus\mathcal J_x}
       b_{x-2,\lambda}.                                    \tag{19}
\end{aligned}
\]
The last two sums are the literal birth and death vectors.  Carries and
collisions determine whether the assumed global labeling is bijective; if
it is not, the multiplicity terms in (16) survive.

Equations (13)--(19) show why a difference of only a smooth core factor is
not enough.  Unless the **entire** physical, arithmetic, endpoint, phase,
and fibre event vector is already the difference in (5), every displayed
commutator is an uncancelled complement carrying \(c_q(sa)\).  Conversely,
defining a formal cumulative primitive is not a saving.  A finitely
supported sequence \(\mathcal A=\Delta_2B\) must satisfy
\(\sum_x\mathcal A(x)=0\).  Even when that necessary condition holds, the
primitive can have full diameter:
two opposite endpoint atoms have an interval-valued primitive, so
\(\|B\|_1\) is of order the support length while
\(\|\mathcal A\|_1=2\).  On a
carrier-length block this loss is of order \(q\), cancelling the \(1/q\)
gain in (4).  This is the precise norm-level self-return; a local,
event-theoretic primitive estimate is indispensable.

The complete available power ledger is therefore
\[
 \underbrace{u\{\kappa+M\}X^\varepsilon}_{\text{inherited positive capacity}}
 \quad\text{versus}\quad
 \underbrace{Q\mathfrak m\kappa uX^\varepsilon}_{\text{target}},
 \qquad \frac{M}{Q\mathfrak m\kappa}>1.                   \tag{20}
\]
For the literal-difference main term one would still have to prove the
aggregate bound after the coefficient \(2/q\) in (6).  Separately, every
term (12)--(19) not already inside that literal difference must be bounded
with \(c_q(sa)\).  The permitted statement supplies neither event counts
nor variation estimates for this ledger, so (20) cannot be improved from
the carrier algebra alone.

## 4. First doubtful or unproved step

Strictly from the written isolated hypotheses, the first gap is the use of
the odd \(\chi _4\) identity and the word “primitive”: \(\kappa\) odd and
\((a,q)=1\) are not stated.  Formula (1) repairs the parity issue, and
primitivity is valid once the intended exact-conductor unit condition is
added.

Granting those two intended hypotheses, the first substantive unproved
step is (5): there is no supplied literal recombined event sequence from
which to prove
\(\mathcal A_{s,a}=\Delta_2\mathcal B_{s,a}\), no proof that its total mass
vanishes, and no local-capacity bound for \(\mathcal B_{s,a}\).  The actual
endpoint vectors and fibre translations are absent.  Consequently none of
the commutators (12)--(19) can be shown to vanish or to fit the target
budget.  This is exactly where the route returns to the unresolved factor
\(M/(Q\mathfrak m\kappa)>1\).

## 5. Required controls and outcomes

- **exact_round195_open_P2_packet_region — PASS (scope):** retained
  \(\kappa<D_L\) and \(M>Q\mathfrak m\kappa\); the latter exposes the exact
  positive-capacity gap.
- **physical_mask_before_spectral_operations — PASS (formal order):**
  \(P_2\) is inside the event product before \(\Delta_2\); (17)--(18)
  retain its commutator.  Quantitative pricing is unavailable.
- **both_T_branches — RETAINED / NOT PRICEABLE:** \(T=0\) and every strict
  \(T\ge1\) branch occur in \(F_T\); none is deleted.
- **both_orientations_and_frequency_signs — PASS:** (8) is derived in both
  charts, and \(s=\pm1\) is kept inside one aggregate.
- **on_shell_x_coordinate_identity — PASS:** the two displayed definitions
  of \(x\), including the stipulated \(d'/g\) and \(d/g\) identifications
  in (H), are used exactly; no off-shell substitution is made.
- **determinant_anchor_congruence — PASS:** (8) and its minus analogue are
  direct congruence calculations.
- **parity_character_identity — CONDITIONAL PASS / AS-STATED GAP:** (9) is
  unconditional; (2) needs odd \(A,x\), not stated.  Equation (7) gives the
  exact even-lattice form.
- **primitive_4q_carrier — CONDITIONAL PASS:** proved when \((a,q)=1\);
  false as a general assertion without the unit condition.
- **exact_conductor_coefficient_normalization — PASS:** (4) follows from
  the displayed \(c_q\), with no vanishing denominator for odd \(q\).
- **step_two_multiplier_denominator_cancellation — PASS ALGEBRAICALLY:**
  (3)--(4) are exact for each sign.
- **genuine_Delta2_before_identity — FAIL / UNPROVED:** (11) identifies the
  necessary gate, but the permitted data contain no literal
  \(\mathcal A\) or \(\mathcal B\) proving it.
- **actual_endpoint_event_vectors — NOT EVALUABLE:** no vectors are given;
  (12), (14), and (19) show the endpoint terms that must survive.
- **physical_mask_commutator — FORMAL PASS, ESTIMATE OPEN:** (17)--(18) are
  exact; no threshold-crossing count is supplied.
- **squarefree_coprimality_flips — RETAINED, ESTIMATE OPEN:** the
  \(\Delta_2G\) term in (14) cannot be smoothed or omitted.
- **carry_birth_death_zero_extension — FORMAL PASS, ESTIMATE OPEN:**
  (12), (16), and (19) list all such terms; no bijection or bound is given.
- **Fejer_square_root_phase — RETAINED, ESTIMATE OPEN:** both
  \(\Delta_2V\) and the exact phase increment (15) survive.
- **one_outer_real_part — PASS:** all identities are coefficient-level
  identities to be inserted before the one outer real part; no orientation
  or sign is separately normed.
- **complete_packet_power_ledger — FAIL TO CLOSE:** (20) is the complete
  ledger available from the statement, and the ratio is strictly \(>1\).
  No event data price the additional commutators.
- **unsigned_character_erased_phase_conjugated_controls — PASS AS
  OBSTRUCTIONS:** taking a positive norm erases the factor \(1-z_s\);
  erasing \(\chi _4\) changes the step multiplier to \(e(sa/q)\), which
  does not cancel \(1+e(-sa/q)\); a coefficient aligned with
  \(\overline{F_{s,a}}\) has no carrier cancellation.  These are adversarial
  diagnostics of the proposed inference, not replacements for the actual
  packet sequence.
- **no_consecutive_or_arbitrary_array_replacement — PASS:** no such array
  is used to prove the target.  The two-endpoint example is only a sharp
  control showing why a manufactured primitive gives no theorem.
- **no_separate_orientation_norm — PASS:** neither chart is bounded
  separately.
- **no_T_branch_or_submask_escape — PASS (scope):** no branch, Farey
  condition, or proper submask is claimed as the target.
- **diagnostic_only — PASS:** no computation was used.
- **original_t1_only_downstream_scope — PASS:** the report asserts nothing
  beyond the fixed original-\(t=1\), physical-\(P_2\) packet.
- **exponent_quarantine — PASS:** no downstream exponent, bridge, M9, or
  quarter-theorem conclusion is inferred.

## 6. Dependencies and exact artifacts used

This is a statement-only blind derivation.  The only artifacts read were:

1. protocol.md;
2. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/blind_statement.md;
3. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/briefs/blind_on_shell_phase_rederivation.md.

No graph, campaign state, proof draft, strategy file, source card,
prior-round artifact, kernel, sibling report/review/control, or conductor
analysis was read.  No external theorem or computation was used.

## 7. Recommended state effect

**Revise; do not promote the fixed-packet target.**  Retain (1), (3), (4),
(11), and the commutator ledger as candidate exact algebra.  Before even a
narrow phase lemma is accepted, verify or add the missing odd-parity and
exact-conductor unit hypotheses.  Promotion of the target must wait for a
literal definition of the complete recombined event sequence, an exact
identity of the form (5), and target-sized estimates for every term in
(12)--(19).  Absent those items, record the genuine-\(\Delta_2\)
full-carrier-length self-return and leave the proof state unchanged.
