# Round 128 hostile audit: the birth count does not by itself control local transverse \(V^2\)

Campaign: `gc-w7-16-local-transverse-lift-variation-gate`
Task: `local_variation_hostile_audit`
Role: seam reviewer
Starting graph SHA-256: `1a5c8c8b4b6c6c0dcf3d0e05a1607b3d29dfe22f66748d401405d1c0f7b474d6`
Status: candidate evidence only; no shared proof state is changed.

## 1. Result: a sharp \(J_B\)-only no-go and a conditional BV lemma

The displayed birth count

\[
 J_B=1+\frac{DQ_B}{B^2}
\]

correctly bounds the number of crossings of any fixed finite collection of
faces whose lift endpoint is a floor of a constant multiple of \(D/b'\)
while \(b'\) moves through an interval of length \(Q_B\).  It does **not**
by itself bound the stated \(V^2\) norm.  The two endpoint values, continuous
motion of every weight already in the lift interval, parity and reduced
characters, profile or hard-face jumps, and cross-shell zero extensions are
separate sources of variation.  Each needs a literal estimate.

The selected context never defines the functions
\(I_{i,\rho}(v)\), the star, or
\(\omega_i(g,a',\rho v)\): it only says that these symbols “contain” all
floors, tapers, profiles, signs, hard samples, and support faces.  It also
does not say, in the definition of \(U_{i,\rho}\), whether the M1 factor
\(\chi_4(b')\), the odd-denominator mask, or a half-open shell mask remains
in the amplitude or has been transferred to the carrier.  Consequently no
literal M1 or M2 package can be checked term by term, and the proposed bound

\[
 \|U_{i,\rho}\|_{V^2(I)}
 \ll_\varepsilon \frac{J_B^{1/2}}{L}Y^\varepsilon
 \tag{1.1}
\]

cannot be certified from the permitted artifacts.

There is also a reproducible sharp no-go for any argument that tries to
deduce (1.1) from the birth count, pointwise size, and the presence of
\(\chi_4(g)\) alone.  On an interval of \(N\) points, a fixed one-lift
family with no births can have

\[
 U(v)=L^{-1}(-1)^v,
 \qquad
 \|U\|_{V^2}^2=\frac{4N-2}{L^2}.
 \tag{1.2}
\]

At the critical longest-lift shell \(B=D/L=Y^{1/3}\), \(\rho=1\),
\(N\asymp Q_B=Y^{11/48}\), and
\(J_B\asymp Y^{1/16}=Y^{3/48}\).  Thus (1.2) exceeds (1.1) by
\(Y^{1/12}\).  Relative to \(J_B\), its effective loss is
\(J_B^{11/6}/L\), far beyond the admissible threshold \(2/3\).

This oscillating example is an abstract transverse countermodel, not a
lower bound for the physical coefficient.  It becomes a literal package
control for M1 if \(\chi_4(b')\), or the equivalent odd-support zero
extension, is left inside \(U\): on writing
\(b'=\rho(2t+1)\),

\[
 \chi_4(b')=\chi_4(\rho)(-1)^t.
\]

Hence a slowly varying nonzero core acquires a jump at every transverse
step, not at the \(J_B\) lift births.  The only eligible formulation must
extract this factor exactly, either by the two branches

\[
 \chi_4(b')=\frac{e(b'/4)-e(-b'/4)}{2i}
 \tag{1.3}
\]

or by using an odd progression and placing \((-1)^t=e(t/2)\) in the
oscillatory carrier.  The selected context indicates that a quarter shift
is intended, but the literal definition does not enact the split.

What can be proved independently is the following conditional lemma.  For
a finite zero-extended sequence \(f(g)\), put

\[
 \|f\|_{BV_g}^{\#}
 :=\sup_g|f(g)|+\sum_g|f(g+1)-f(g)|.
\]

If \(U(v)=\sum_g\chi_4(g)\omega_v(g)\), then

\[
 \|U\|_{V^2(I)}^2
 \ll
 \|\omega_{v_-}\|_{BV_g}^{\#\,2}
 +\|\omega_{v_+}\|_{BV_g}^{\#\,2}
 +\sum_{v,v+1\in I}
   \|\omega_{v+1}-\omega_v\|_{BV_g}^{\#\,2}.
 \tag{1.4}
\]

Thus (1.1) would follow packagewise from the literal bound

\[
 \|\omega_{v_-}\|_{BV_g}^{\#\,2}
 +\|\omega_{v_+}\|_{BV_g}^{\#\,2}
 +\sum_v\|\Delta_v\omega_v\|_{BV_g}^{\#\,2}
 \ll_\varepsilon \frac{J_B}{L^2}Y^\varepsilon.
 \tag{1.5}
\]

Pure endpoint births satisfy (1.5).  No selected artifact proves (1.5)
for either complete literal M1 or M2 weight.  The result of this audit is
therefore a **revision/no-certification**, not a disproof of the physical
coefficient estimate.

## 2. Exact statement and hypotheses

Work at

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},
 \qquad D/L\le B\le D,
\]

and let

\[
 Q_B=\min\!\left(B,\frac{BD}{WL}\right),\qquad
 G=\frac DB,\qquad
 J_B=1+\frac{DQ_B}{B^2}.
\]

Fix the outer ray and all labels other than \(b'\), fix a divisor
\(\rho\mid a'\), and write \(b'=\rho v\).  The curvature interval has

\[
 N_\rho\ll 1+\frac{Q_B}{\rho}
 \tag{2.1}
\]

values.  In the selected context the only stated coefficient formula is

\[
 U_{i,\rho}(v)
 =\sum_{g\in I_{i,\rho}(v)}^{*}
   \chi_4(g)\omega_i(g,a',\rho v).
 \tag{2.2}
\]

The accepted reduced coefficients one level above (2.2) are

\[
 A_1(a',b')=\frac{2\chi_4(b')}{\pi i a'}T_1(a',b'),
 \qquad
 A_2(a',b')=-\frac{4\chi_4(|a'|)}{\pi|a'|}T_2(a',b'),
 \tag{2.3}
\]

where

\[
 T_i(a',b')=\sum_{g\ge1}\frac{\chi_4(g)}g
 U_{i,a',b'}(g)
\]

is real.  Formula (2.3) identifies the reduced character placement and
the common lift character, but it does not identify the long-lift
\(\omega_i\) in (2.2), its normalization, either endpoint of
\(I_{i,\rho}(v)\), the hard and star values, or the zero-extension owner.
In particular, the pointwise bound for the completed primitive coefficient
\(A_i(a',b')\) does not automatically bound each separate Möbius term
\(U_{i,\rho}(v)\).

The exact sufficient hypotheses for (1.1) are the following.

1. The M1 denominator character and odd mask are removed from the
   amplitude exactly as in (1.3), or the progression is reparameterized
   so that their alternation lies in the phase.  The M2 numerator
   character is constant in \(v\) and may remain outside.
2. Each endpoint sequence has
   \(\|\omega_{v_\pm}\|_{BV_g}^{\#}\ll L^{-1}Y^\varepsilon\).
3. The common-support smooth part satisfies
   \[
   \sum_v\|\Delta_v\omega^{\rm sm}_v\|_{BV_g}^{\#\,2}
   \ll \frac{J_B}{L^2}Y^\varepsilon.
   \tag{2.4}
   \]
4. All discrete floor, hard, star, profile, support, and half-open-shell
   changes, after common values have been subtracted, satisfy the same
   square ledger.  It is enough that there are
   \(O(J_BY^\varepsilon)\) events and each event has
   \(BV_g^{\#}\)-size \(O(L^{-1}Y^\varepsilon)\).
5. These estimates hold uniformly for every divisor progression before
   the divisor sum.  Summing \(\rho\mid a'\) may then cost
   \(\tau(a')Y^\varepsilon\), but no power of \(B,D,G,Q_B\), or
   \(N_\rho\).
6. Every cross-shell term has exactly one half-open owner, and the
   interval used in (2.4) is the same interval of \(b'\)-length
   \(Q_B\) used by the reciprocal curvature estimate.

These hypotheses are not claimed to be necessary.  They are a literal,
checkable replacement for the unsupported inference “there are \(J_B\)
births, therefore the whole \(V^2\) norm is \(J_B^{1/2}/L\).”

## 3. Proof and derivation

### 3.1 Character Abel proves the conditional lemma

The partial sums of \(\chi_4\) are uniformly bounded on every integer
interval.  Discrete summation by parts therefore gives, for every finite
zero-extended \(f\),

\[
 \left|\sum_g\chi_4(g)f(g)\right|
 \ll \|f\|_{BV_g}^{\#}.
 \tag{3.1}
\]

Apply (3.1) first to \(f=\omega_{v_-}\) and
\(f=\omega_{v_+}\).  On a common zero-extended ambient lift lattice,

\[
 U(v+1)-U(v)
 =\sum_g\chi_4(g)\{\omega_{v+1}(g)-\omega_v(g)\},
\]

so a second application of (3.1), followed by squaring and summing in
\(v\), proves (1.4).  This keeps \(\chi_4(g)\) inside the complete lift
sum until its bounded partial sums have been used.

For a pure birth or exit of one lift with coefficient \(O(L^{-1})\), the
zero-extended difference is one point mass and has
\(BV_g^{\#}\)-size \(O(L^{-1})\).  A fixed finite number of moving faces
whose endpoints are \(\lfloor cD/b'\rfloor\) cross at most

\[
 O\!\left(1+\left|\frac{cD}{b'_1}-
                         \frac{cD}{b'_0}\right|\right)
 \ll 1+\frac{DQ_B}{B^2}\ll J_B
 \tag{3.2}
\]

integer values.  Their square contribution is therefore
\(O(J_B/L^2)\).  A strict versus weak face or a star changes only the
constant in the point-mass size, not (3.2).

This proves (1.1) for the strict subset consisting solely of a fixed
finite set of such endpoint births, provided the two endpoint values have
the stated \(BV_g\) bound.  It does not prove the continuous or literal
hard/profile pieces.

### 3.2 Continuous weights are potentially safe, but not counted by births

For a standard smooth scale \(w(gb'/D)\) with coefficient size \(L^{-1}\),
one expects, after taking the \(g\)-variation as well as the supremum,

\[
 \|\Delta_v\omega_v^{\rm sm}\|_{BV_g}^{\#}
 \ll_\varepsilon \frac{\rho}{BL}Y^\varepsilon.
 \tag{3.3}
\]

If (3.3) is proved for the exact product of tapers and profiles, then
(2.1) yields

\[
 \sum_v\|\Delta_v\omega_v^{\rm sm}\|_{BV_g}^{\#\,2}
 \ll_\varepsilon
 \left(1+\frac{Q_B}{\rho}\right)
 \frac{\rho^2}{B^2L^2}Y^\varepsilon
 \ll_\varepsilon \frac{J_B}{L^2}Y^\varepsilon.
 \tag{3.4}
\]

Here \(\rho\le |a'|\asymp LB/D\le D\), so
\(Q_B\rho/B^2\le DQ_B/B^2\); the unit term is harmless on the permitted
range.  Thus continuous motion need not destroy the desired capacity.
But (3.3), not the birth count, is what controls it.  Since no literal
\(\omega_i\) is supplied, (3.3) cannot be checked for the Vaaler taper,
frequency profile, triangular factor, hard sample, or either M1/M2
normalization.

### 3.3 Möbius progressions do not repair missing transverse regularity

The zero extension used in the bounded-lift proof expands

\[
 {\bf1}_{(a',b')=1}
 =\sum_{\rho\mid a',\ \rho\mid b'}\mu(\rho),
 \qquad b'=\rho v.
 \tag{3.5}
\]

For nonzero M1 and M2 coefficients the effective divisors are odd.  Fixed
\(\rho\) changes the number of transverse samples to \(N_\rho\), but the
total \(b'\)-motion remains \(Q_B\), so the endpoint count (3.2) is still
\(J_B\).  Absolute divisor summation costs only \(Y^\varepsilon\) after
(1.5) is known uniformly.  It supplies no estimate for (1.5), and a
pointwise bound after recombining (3.5) cannot be pushed backward to each
Möbius piece.

### 3.4 The two reproducible countermodels and their capacities

For (1.2), take \(I=\{0,\ldots,N-1\}\), a fixed lift set \(\{1\}\), and

\[
 \omega_v(1)=L^{-1}(-1)^v,\qquad \omega_v(g)=0\ (g\ne1).
\]

There are no births, \(|U(v)|=L^{-1}\), and direct substitution in the
definition of \(V^2\) gives (1.2).  This proves that endpoint size plus a
birth count does not control transverse differences.  If the M1 factor
\(\chi_4(b')\) is left in the amplitude, the same construction is the
constant-core character control described after (1.3).

The adversarial-lift control is independent and tests the use of the
common lift character.  On a fixed set of \(G\) odd lifts, put

\[
 \omega_v(g)=L^{-1}\chi_4(g),
\]

independently of \(v\).  Then

\[
 U(v)=L^{-1}\sum_{g\le G,\ g\ {\rm odd}}\chi_4(g)^2
 \asymp \frac GL,
 \qquad
 \|U\|_{V^2}\asymp\frac GL,
 \tag{3.6}
\]

solely from the two endpoint terms.  At \(B=D/L\), \(G=L=Y^{1/6}\)
and \(J_B=Y^{1/16}\), so (3.6) exceeds the desired endpoint allowance by
\(Y^{13/96}\).  In the \(J_B^\theta/L\) ledger it has
\(G=J_B^{8/3}\), hence \(\theta=8/3\).

This second model is deliberately phase-conjugated in the lift variable
and is not a physical lower bound.  It proves that \(\chi_4(g)\) may be
used before modulus only together with an actual \(g\)-BV statement for
the literal weight.  The accepted top-shell finite-lift BV statement does
not furnish that long-lift statement.

### 3.5 Capacity and the finite stop rule

At the worst shell the conditional connector turns a coefficient cost
\(J_B^\theta/L\) into correlation exponent

\[
 \beta(\theta)=\frac{35}{48}+\frac{\theta}{16}.
 \tag{3.7}
\]

Thus \(\theta=1/2\) gives \(73/96\), while
\(\theta=2/3\) gives exactly \(37/48\), the already proved complete
envelope.  A dense \(N_\rho^{1/2}\) variation at \(\rho=1\) has
\(\theta=11/6\) and capacity \(27/32\).  Full-shell square variation
\(G^{1/2}/L\) has \(\theta=4/3\) and capacity \(13/16\).  The coherent
endpoint control (3.6) has \(\theta=8/3\) and capacity \(43/48\).

Every one of these losses is at or above the stopping threshold.  The
route may continue only after the exact literal dictionary verifies
(1.5), with the M1 character/parity moved to the carrier and every
discrete owner charged once.

## 4. First doubtful or unproved step

The earliest fatal seam is definitional, before any exponent estimate:
there is no literal M1/M2 dictionary for \(I_{i,\rho}(v)\), the star, or
\(\omega_i\).  In particular, the selected artifacts do not determine

- the two exact lift endpoints and their strict, weak, floor, and star
  values;
- the normalization of every smooth Vaaler, dyadic, frequency, and
  triangular factor;
- which hard-top samples are point masses and which remain in a smooth
  profile;
- whether \(\chi_4(b')\), odd-denominator support, or a half-open shell
  mask is in \(U\) or in the oscillatory carrier;
- whether the accepted pointwise reduced-ray bound holds before or only
  after the Möbius pieces are recombined; and
- the unique owner of unequal-shell and shell-boundary terms.

Without these definitions, neither endpoint bound in \(V^2\) nor the
continuous difference estimate (3.3) is a mathematical statement about
the physical coefficient.  The first potential literal counterterm is
the M1 denominator character/parity package: if it is kept inside
\(U\), its variation is \(N_\rho^{1/2}/L\), not
\(J_B^{1/2}/L\).  If it is extracted exactly, the next unproved step is
the packagewise bound (1.5) for the actual long-lift weight.

Accordingly this review cannot certify (1.1), cannot assert that a
physical package violates it, and does not reach the subsequent
\(V^2\)-weighted curvature inequality.

## 5. Control tests and outcomes

| Required seam/control | Exact hostile test | Outcome |
|---|---|---|
| `literal_complete_lift_dictionary` | Locate exact formulas for both endpoints, every weight, the star, character placement, zero extension, and M1/M2 normalization. | **Fail at the first seam.** Only the placeholder (2.2) is present. The higher-level coefficients (2.3) do not determine its packages. |
| `local_window_and_birth_count` | Vary a face \(\lfloor cD/b'\rfloor\) over the same \(b'\)-interval of length \(Q_B\). | **Pass for pure endpoint faces only.** Equation (3.2) gives \(O(J_B)\) crossings. It says nothing about continuous weights or dense parity. |
| `V2_endpoint_terms` | Bound \(U(v_-)\) and \(U(v_+)\) before inspecting increments; apply the conjugated-lift control (3.6). | **Fail for certification.** Character Abel would pass under endpoint \(g\)-BV \(O(L^{-1})\), but this is unstated for each Möbius package. An adversarial lift has endpoint capacity \(G/L\). |
| `continuous_weight_variation` | Derive the exact analogue of (3.3) for the product of all literal weights. | **Open/undefined.** The scale \(\rho/(BL)\) would be safe by (3.4), but no literal derivative-plus-\(g\)-BV formula is available. |
| `character_partial_sum_before_modulus` | Prove (3.1) and apply it to endpoint and difference sequences before taking modulus in \(g\). | **Conditional pass.** The algebra is valid. Its hypotheses fail to be verified for the actual \(\omega_i\); (3.6) shows why they are necessary. |
| `mobius_divisor_progressions` | Expand (3.5), keep fixed \(\rho\), and compare the primitive recombination with the termwise endpoint and variation bounds. | **Counting pass, norm fail.** Divisor multiplicity is only \(Y^\varepsilon\), but the selected context has no uniform termwise \(V^2\) bound and no backward implication from the recombined ray coefficient. |
| `floors_stars_hard_faces_and_support` | Charge each discrete face by its event count and its zero-extended \(BV_g\) jump. | **Pass only for an abstract finite endpoint list; fail literally.** Floors of \(cD/b'\), strict/weak faces, and half-stars fit (3.2), but the actual list and hard values are not defined. |
| M1 denominator character and parity | Leave \(\chi_4(b')\) or the odd-support mask inside \(U\) and take a constant core. | **Fail with a reproducible package control.** It gives (1.2), of size \(N_\rho^{1/2}/L\). It must be transferred exactly to quarter-linear carrier branches or an odd-step phase. |
| M2 numerator character | Hold \(a'\) fixed while \(b'\) varies. | **Pass algebraically.** \(\chi_4(|a'|)\) is constant in \(v\). This does not control the remaining M2 weight. |
| `cross_shell_owner_and_no_duplication` | Intersect the curvature window with half-open \(b'\)-shells and identify the owner of unequal-shell pairs and the boundary jump. | **Fail for certification.** The context asserts a complete cross-shell count but gives no coefficient-level owner or zero-extension formula. A shell boundary is at least one additional event, harmless only after ownership is explicit. |
| `actual_vs_adversarial_lift_coefficients` | Compare actual \(g\)-smooth weights with \(\omega=\chi_4/L\) and compare slow transverse weights with (1.2). | **Control behaves correctly.** Both adversaries violate (1.1); neither is asserted physical. Any proof must use exact actual \(g\)-BV and transverse structure unavailable to these controls. |
| `theta_two_thirds_capacity_threshold` | Insert each effective coefficient loss into (3.7). | **Pass.** \(\theta=1/2\) is useful; \(2/3\) merely recovers \(37/48\); dense-window, full-shell, and coherent endpoint controls all have \(\theta>2/3\). |
| `finite_stop_rule` | Ask whether every literal package has passed (1.5) before testing the oscillatory inequality. | **Stop.** The dictionary, endpoints, continuous weights, M1 parity placement, and cross-shell owner are not all closed. |
| `no_exponent_or_M9_promotion` | Compare the coefficient gate with the later curvature theorem and downstream obligations. | **Pass.** No curvature inequality, \(Y^{73/96}\) bound, global exponent, M9 parent, M9, endpoint uniformity, or quarter theorem is proved. |

All tests are analytic.  No numerical experiment or external theorem was
used.

## 6. Dependencies and exact artifacts used

This report used only the assigned context:

1. `protocol.md`;
2. `state/proof_obligations.yml`, mechanically parsed as the authoritative
   graph, with the exact W7-16, determinant, bounded-lift, connector, and
   relevant rejected-claim entries extracted;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reports/blind_determinant_fibre_rederivation.md`;
5. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reports/determinant_fibre_hostile_source_audit.md`;
6. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_involution_product_and_source.md`;
7. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_actual_savings.md`;
8. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/synthesis.md`;
9. `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/graded_determinant_long_lift_feasibility.md`;
10. `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reviews/conductor_round127_frontier_selection_adjudication.md`; and
11. `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/briefs/local_variation_hostile_audit.md`.

No Round-128 sibling report, unlisted derivation packet, strategy file,
web source, or computation was used.  The effort allocation was 100%
analytical/algebraic.

## 7. Recommended state effect

**Recommendation: no promotion; revise the coefficient gate and retain
the conditional connector only as conditional.**

Retain as candidate evidence the exact character-Abel inequality
(1.4), the strict pure-endpoint subset proved by (3.2), and the scoped
no-go that \(J_B\) plus pointwise size and a common lift character do not
imply (1.1).  Record the M1 placement requirement: its reduced denominator
character and odd mask must be transferred to exact quarter-linear carrier
branches, or to an odd-step phase, before the amplitude \(V^2\) norm is
taken.

Do not promote the literal \(J_B^{1/2}/L\) coefficient norm.  Before the
route can proceed, a literal dictionary must define every M1/M2
\(\omega_i\), endpoint, star, hard value, Möbius term, parity branch, and
cross-shell owner, and then verify (1.5) package by package.  If any package
retains dense parity, costs \(G^{1/2}/L\), costs
\(N_\rho^{1/2}/L\), or has effective \(J_B^\theta/L\) with
\(\theta\ge2/3\), apply the finite stop rule and stop the graded route.

No change is licensed for
`GC-W7-16-actual-reduced-determinant-correlation`, either M9 component,
endpoint uniformity, M9, the global exponent, the conditional quarter
bridge, or `GC-target`.
