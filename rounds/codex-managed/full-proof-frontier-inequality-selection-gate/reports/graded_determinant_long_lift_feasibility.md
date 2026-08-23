# Round 127 report: a transverse local-square-variation inequality can save \(Y^{1/96}\)

Campaign: `full-proof-frontier-inequality-selection-gate`

Task: `graded_determinant_long_lift_feasibility`

Role: discovery

Graph SHA-256: `fd8831d74d53795182b9f8c234753b33df27e096b9d9f52a6cf43403c87c4a43`
Status: candidate evidence only; no shared proof state is changed.

## 1. Result: a theorem-shaped strict-saving candidate and one scalar no-go

At the critical block

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},
\tag{1.1}
\]

the prescribed-centre scalar continuation does not improve the certified
complete \(Y^{37/48+\varepsilon}\) envelope, but a genuinely joint
transverse local-square-variation inequality has just enough capacity to
improve it.

First, even if the certified Round-118 prescribed-centre scalar-wave
envelope is granted, with no interface loss, for every literal determinant
cell, it gives cell amplitude \(Y^{1/3+\varepsilon}\) at (1.1).  There are
\(Y^{5/48+o(1)}\) cells.  Its square-function consequence is therefore
exactly \(Y^{37/48+\varepsilon}\), with no strict saving.

Second, let \(B\) be a reduced-denominator shell, \(G=D/B\) its full lift
length, and \(Q_B\) the actual reciprocal \(q\)-window.  Across one such
window the moving lift endpoint traverses only

\[
 J_B=1+{DQ_B\over B^2}=1+{GQ_B\over B}
\tag{1.2}
\]

integer births, not all \(G\) births of the complete \(B\)-shell.
Replacing the lost transverse total variation \(J_B/L\) by its optimal
local square variation \(J_B^{1/2}/L\), while keeping the complete lift
transform jointly inside the reciprocal \(q\)-sum, requires the new
\(V^2\)-weighted curvature inequality stated in Section 2.3.  If that
inequality holds for the actual starred lift family, the complete-shell
bound is

\[
 |\mathfrak O_{i,B}|
 \ll_\varepsilon
 D J_B^{1/2}
 \min\!\left(Q_B,Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\right)
 Y^\varepsilon,
\tag{1.3}
\]

where

\[
 Q_B=\min\!\left(B,{BD\over WL}\right),\qquad
 \lambda_B={YL\over DB^2}.
\tag{1.4}
\]

At (1.1), the curvature factor in (1.3) is
\(Y^{11/48+o(1)}\), uniformly for the allowed
\(D/L\ll B\ll D\).  Hence (1.3) is

\[
 |\mathfrak O_{i,B}|
 \ll_\varepsilon Y^{35/48+\varepsilon}J_B^{1/2}.
\tag{1.5}
\]

At the longest permitted lift, \(B\asymp D/L\), one has
\(J_B\asymp D/W=Y^{1/16}\), not \(G=L=Y^{1/6}\).  Thus (1.5) has worst
capacity

\[
 Y^{35/48}Y^{1/32}=Y^{73/96},
\tag{1.6}
\]

a strict \(Y^{1/96}\) improvement over \(Y^{37/48}=Y^{74/96}\).
The saving is small and gives no pointwise-exponent improvement, but it is
a bankable complete fixed-block saving if the new inequality is proved.

The scalar conclusion is a rigorous capacity no-go.  The square-variation
conclusion is a theorem-shaped feasibility result, not a proof: its first
unproved seam is the actual-family \(V^2\)-weighted curvature inequality.

## 2. Exact statement and hypotheses

### 2.1 Literal graded target

Fix one literal M1 or M2 dyadic block, one fixed moving-symbol stratum, and
\(c\asymp Y\).  Aggregate all equal-frequency lifts
\((h,d)=(ga,gb)\) before any absolute value.  With
\(\kappa_1=1\), \(\kappa_2=4\), and

\[
 n=ab'-a'b,
\]

the one-sided open correlation is

\[
 \mathfrak O_i^+(c)=
 \sum_{\substack{(a,b)=(a',b')=1\\
                  0<n<\kappa_i bb'/W}}^{\mathrm{literal}}
 A_i(a,b)\overline{A_i(a',b')}
 e\!\left({cn\over\kappa_i bb'}\right)
 \left(1-{Wn\over\kappa_i bb'}\right).
\tag{2.1}
\]

The superscript `literal` in (2.1) retains, rather than suppresses, the
actual Vaaler taper; \(\chi_4\) on the M1 denominator or M2 numerator;
the common lift character \(\chi_4(g)\); both frequency signs; the fixed
sign of the M2 product sector; exact reduced supports; moving profiles and
symbols; floors; strict and weak faces; hard-top samples; endpoint stars;
and all support births and exits.  The target is

\[
 \boxed{\mathfrak O_i^+(c)\ll_\varepsilon Y^{1/2+\varepsilon}}
\tag{2.2}
\]

uniformly in all of those data.  The equal-frequency diagonal is already
\(O_\varepsilon(D/L)\).

The accepted complete and bounded-lift estimates are

\[
 \mathcal C_i(c),\ |\mathfrak O_i(c)|
 \ll_\varepsilon
 \left({D^2\over L^2}+{WD\over L}\right)Y^\varepsilon,
\tag{2.3}
\]

and, only when \(b,b'\asymp D\),

\[
 |\mathfrak O_{i,B\asymp D}|
 \ll_\varepsilon
 D\min\!\left(Q_*,Q_*\sqrt\lambda+\lambda^{-1/2}\right)Y^\varepsilon,
\quad
 Q_*=\min\!\left(D,{D^2\over WL}\right),\quad
 \lambda={YL\over D^3}.
\tag{2.4}
\]

At (1.1), (2.3) is \(Y^{37/48+\varepsilon}\) and (2.4) is
\(Y^{35/48+\varepsilon}\).  Relative to (2.2), their deficits are
respectively \(Y^{13/48}\) and \(Y^{11/48}\).

### 2.2 The three literal frontiers and their capacities

| Frontier | Exact live quantity | Present capacity | Required capacity | Missing power | Downstream scope |
|---|---|---:|---:|---:|---|
| hard TOP | \(E_{\rm ns}=\|A_L^{\rm ns}\chi_4\|_2^2\), with the \(hm=\square\) entry sector removed only through the norm triangle | support/Bessel capacity \(L^3X^\varepsilon\) | \(L^2X^\varepsilon\) | \(L\) | closes only hard TOP; BAL and UNBAL still remain for M9-M2 |
| lower GAR | the exact Round-122 medium-index, low-two-adic cumulative wavelet \(\sum_{R<|k|\le K_\delta}W(k)I_kV_\delta\), with the certified central packages removed | \(R^2X^\varepsilon\) absolute capacity | \(RX^\varepsilon\) | \(R\) | would close the alternative total-M1 parent, not blockwise M9-M1 or M9-M2 |
| graded determinant | (2.1) at \(W=Y^{7/16}\) | complete \(Y^{37/48}\); bounded-lift top shell \(Y^{35/48}\) | \(Y^{1/2}\) | \(Y^{13/48}\); top shell \(Y^{11/48}\) | full target gives the internal \(5/16\) exponent, but proves neither M9 component nor the quarter theorem |

The scales in the table are deliberately not mixed: hard TOP is an energy,
lower GAR is a linear wavelet, and (2.1) is the triangular correlation
energy.

### 2.3 Exact transverse square-variation inequality that would be needed

On a shell \(b'\asymp B\), put \(G=D/B\) and
\(|a'|\asymp LB/D\).  After the same zero extension and Möbius expansion
used in (2.4), write the complete, unseparated lift amplitude on a divisor
progression \(b'=\rho v\) as

\[
 U_{i,\rho}(v)
 =\sum_{g\in I_{i,\rho}(v)}^{\!*}
 \chi_4(g)\,\omega_i(g,a',\rho v).
\tag{2.5}
\]

Here \(I_{i,\rho}(v)\), the star, and \(\omega_i\) contain the exact
floor endpoints, hard sample, triangular taper, profiles, signs, and
entry/exit symbols.  In particular, (2.5) is not a clean complete divisor
coefficient.  Define

\[
 \|U\|_{V^2(I)}^2
 =|U(v_-)|^2+
   \sum_{v,v+1\in I}|U(v+1)-U(v)|^2+|U(v_+)|^2.
\tag{2.6}
\]

The proposed continuation requires the genuinely joint estimate

\[
 \left|\sum_{v\in I}^{\!*}U_{i,\rho}(v)
 e\!\left(-{ca'\over\kappa_i\rho v}+\vartheta_i\rho v\right)\right|
 \ll_\varepsilon
 \|U_{i,\rho}\|_{V^2(I)}
 \min\!\left(N_\rho,
 N_\rho\sqrt{\lambda_B\rho^2}
 +(\lambda_B\rho^2)^{-1/2}\right)Y^\varepsilon,
\tag{SV}
\]

where \(N_\rho\asymp Q_B/\rho\) and \(\vartheta_i\) is the literal
zero or quarter-linear shift.  Although the full shell has \(G=D/B\)
possible lift endpoints, the interval in (SV) has \(b'\)-length at most
\(Q_B\).  Since the endpoint is a floor of a quantity comparable to
\(D/b'\), it changes only

\[
 J_B=1+O\!\left({DQ_B\over B^2}\right)
\tag{2.7}
\]

times on this interval.  The required local coefficient norm is therefore

\[
 \|U_{i,\rho}\|_{V^2(I)}
 \ll_\varepsilon {J_B^{1/2}\over L}Y^\varepsilon.
\tag{2.8}
\]

Standard partial summation plus Cauchy does **not** prove (SV): it inserts
an additional \(N_\rho^{1/2}\).  Thus (SV), if true for (2.5), would be a
new noninvertible actual-family inequality, not a change of variables or a
separated norm.  The capacity calculation below grants both (SV) and
(2.8).  Replacing \(J_B\) by the full \(G\) before combining with the
\(q\)-sum would erase the saving and is precisely the separated-modulus
step that the candidate forbids.

## 3. Proof and exponent derivation

### 3.1 Prescribed-centre scalar wave: exact critical equality

Write \(D=Y^\delta\), \(L=Y^\ell\),
\(\alpha=7/16\), and \(a=\delta-\ell\).  A random cell has the
accepted product-window amplitude \(D/L=Y^a\), and the signed band meets

\[
 1+{WL\over D}=1+Y^{\alpha-a}
\tag{3.1}
\]

cells.  Optimistically grant to every literal cell the Round-118 scalar
envelope

\[
 Y^\varepsilon\min\!\left({D\over L},
 \sqrt{YL/D}+\sqrt{Y/(LD)}\right).
\tag{3.2}
\]

Its leading exponent is

\[
 \gamma(a)=\min\!\left(a,{1-a\over2}\right).
\]

Squaring before the random-shift integral, as the exact triangular kernel
requires, gives energy exponent

\[
 \beta_{\rm scalar}(a)
 =2\gamma(a)+\max(0,\alpha-a).
\tag{3.3}
\]

At the literal minimax point \(a=1/3\), the two branches of (3.2) meet:

\[
 \gamma(1/3)=1/3,
 \qquad
 \beta_{\rm scalar}(1/3)
 ={2\over3}+\left({7\over16}-{1\over3}\right)
 ={37\over48}.
\tag{3.4}
\]

The scalar mechanism saves only for \(a>1/3\).  Because the complete
literal family contains the equality block (1.1), no uniform strict power
can be obtained from (3.2), even if every coefficient, endpoint, floor,
star, and moving symbol were transferred without loss.  This is the first
fatal seam for the prescribed-centre scalar proposal: capacity, before
source or interface applicability.

### 3.2 Why \(J_B^{1/2}\) is the sharp local square variation

The endpoint model fixes both the gain and its lawful locality.  For

\[
 S_M^*=\sum_{1\le g\le M}^{\!*}\chi_4(g),
\]

successive floor births obey
\(S_M^*-S_{M-1}^*=\chi_4(M)\), apart from one harmless half-weight at a
starred face.  Therefore, on any interval containing \(J\) consecutive
endpoint births,

\[
 \sum_{M\in\mathcal J}|S_M^*-S_{M-1}^*|^2\asymp J,
 \qquad
 \sum_{M\in\mathcal J}|S_M^*-S_{M-1}^*|\asymp J.
\tag{3.5}
\]

After the literal \(L^{-1}\) coefficient scale, (3.5) is respectively
\(J^{1/2}/L\) and \(J/L\).  Across a whole \(B\)-shell one may have
\(J\asymp G\), which is the previously recorded total-variation loss.
Across the actual \(q\)-window in (SV), however, elementary floor geometry
gives only \(J=J_B\) from (2.7).  This localization is lost if the lift
transform or the \(b'\)-sum is first put in modulus.

Choosing an interval endpoint in a suitable class modulo four leaves
\(|S_M^*|\gg1\), so no factor \(G^{-\sigma}\) is available from the lift
character alone.  Strict versus weak endpoints and a star change only the
absolute constant.  This is an adversarial BV control, not a claim that
the physical coefficient saturates (3.5); it shows that \(J_B^{1/2}\) is
the optimal square-variation size available from endpoint orthogonality
alone.  Proving (2.8) for the physical smooth, hard, floor, and star pieces
remains an actual-coefficient task.

### 3.3 Capacity of the granted joint \(V^2\)-curvature estimate

For fixed outer labels, (SV), (2.8), and the divisor sums give the inner
cost

\[
 {J_B^{1/2}\over L}
 \min\!\left(Q_B,Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\right)Y^\varepsilon.
\]

The complete cross-shell count retained in the certified top-shell proof
has \(O(LD)\) outer rays, \(O(L)\) numerator increments, and outer
coefficient \(O(L^{-1})\).  Multiplication gives exactly (1.3).  A
same-\(B\) pair count can be smaller, but it does not cover the complete
cross-shell target (2.1), so it cannot replace (1.3) in a complete bound.

At (1.1), reduced numerator support gives
\(D/L\ll B\ll D\).  Writing \(B=Y^b\),
\(1/3\le b\le1/2\), one has

\[
 Q_B={BD\over WL}=Y^{b-5/48},
 \qquad
 \lambda_B={Y^{2/3}\over B^2}=Y^{2/3-2b},
\tag{3.6}
\]

and hence

\[
 Q_B\sqrt{\lambda_B}=Y^{11/48},
 \qquad
 \lambda_B^{-1/2}=Y^{b-1/3}\le Y^{8/48}.
\tag{3.7}
\]

Moreover,

\[
 J_B=1+{DQ_B\over B^2}
 =1+Y^{19/48-b}.
\tag{3.8}
\]

Thus the minimum in (1.3) is \(Y^{11/48+o(1)}\), and the candidate gives

\[
 |\mathfrak O_{i,B}|
 \ll_\varepsilon
 Y^{35/48+\frac12\max(0,19/48-b)+\varepsilon}.
\tag{3.9}
\]

The right side increases as \(b\) decreases.  Its worst permitted value is
at \(b=1/3=16/48\), where \(J_B=Y^{3/48}=Y^{1/16}\) and (3.9) is
\(Y^{73/96+\varepsilon}\).  For \(b\ge19/48\), only \(O(1)\) endpoint
births occur in one curvature window and the candidate returns the
bounded-lift \(Y^{35/48}\) scale.  Thus the complete dyadic shell sum is
\(Y^{73/96+\varepsilon}\), logarithms absorbed.

More generally, if the local coefficient norm costs \(J_B^\theta/L\), a
strict improvement at the maximal local endpoint range requires

\[
 {35\over48}+{\theta\over16}<{37\over48},
 \qquad\text{i.e.}\qquad \theta<{2\over3}.
\]

Natural local square variation has \(\theta=1/2\), so it passes this
capacity gate with the \(Y^{1/96}\) margin in (1.6).  Full-shell square
variation \(G^{1/2}/L\) would fail; the gain comes exactly from retaining
the lift transform inside its moving \(q\)-window.

### 3.4 Exact downstream exponent propagation

Let a complete graded correlation bound be \(Y^{\beta+\varepsilon}\).
The length-\(W\) local square integral then has exponent
\(q=\alpha+\beta\) for \(\beta\ge1/2\).  The accepted persistence bridge
delivers

\[
 \Theta(\beta)
 =\max\!\left({\alpha+\beta\over3},{\beta\over2}\right),
 \qquad \alpha={7\over16},
\tag{3.10}
\]

to be compared with the already proved \(1/3\) fallback.

| Complete correlation exponent \(\beta\) | Persistence exponent from (3.10) | Actual theorem effect |
|---:|---:|---|
| \(37/48\) (present) | \(29/72\) | none; \(1/3\) is stronger |
| \(73/96\) (if (SV) and (2.8) are proved) | \(115/288\) | banked block saving \(Y^{1/96}\), but no pointwise change |
| \(35/48\) (best certified top-shell envelope, even if it became complete) | \(7/18\) | none; \(1/3\) is stronger |
| \(27/48=9/16\) | \(1/3\) | threshold only; no strict improvement |
| \(24/48=1/2\) | \(5/16\) | the stated graded payoff; still not M9 |

Thus a partial graded saving changes the internal pointwise exponent only
after the complete \(\beta\) crosses below \(9/16\).  To beat the audited
external exponent \(\theta_{\rm LY}=0.3144831759740614\ldots\), one needs

\[
 \beta<3\theta_{\rm LY}-{7\over16}
 =0.505949527922184\ldots .
\tag{3.11}
\]

For a theorem stated in the transparent two-gain form

\[
 \mathcal C_i(c)
 \ll_\varepsilon
 \left({D^2\over L^2}Y^{-\eta_0}
       +{WD\over L}Y^{-\eta_1}\right)Y^\varepsilon,
\tag{3.12}
\]

the critical exponent is
\(\max(32/48-\eta_0,37/48-\eta_1)\).  A strict block-envelope saving only
needs \(\eta_1>0\); an internal exponent below \(1/3\) needs
\(\eta_0>5/48\) and \(\eta_1>10/48\); and the full \(5/16\) payoff needs
\(\eta_0\ge8/48\) and \(\eta_1\ge13/48\).  This distinguishes a banked
fixed-block saving from an actual pointwise-exponent improvement.
The proposed local-square-variation theorem corresponds at the critical
maximum to only \(\eta_1=1/96\), far below the \(10/48\) pointwise
threshold.

## 4. First doubtful or unproved step

The first doubtful seam is (2.8): the endpoint count proves the
\(J_B^{1/2}\) scale for pure lift births, but it has not been proved that
the complete actual smooth profile, hard face, floor perturbation, star,
and triangular weight have no additional \(G^{1/2}\), \(Q_B^{1/2}\), or
total-variation contribution.  This is a finite, coefficient-level norm
question and should be tested before the oscillatory theorem.

If (2.8) passes, the first unproved analytic inequality is (SV).  A generic
\(V^2\) amplitude estimate does not imply it: partial summation and Cauchy
cost \(N_\rho^{1/2}\), while arbitrary coefficients can conjugate the
reciprocal phase.  It must be proved for the complete actual family (2.5),
jointly in the lift endpoint, \(b'\), the divisor progression, and the
literal quarter shift.

There is an earlier interface doubt for the scalar proposal: Round 118
controls an analogous flat prescribed-centre wave, not every determinant
cell with its two different truncated M1/M2 product coefficients.  The
capacity no-go in (3.4) deliberately grants that missing transfer, so this
doubt cannot rescue the scalar mechanism.

The endpoint model (3.5) does not disprove a stronger physical theorem.
It only shows that such a theorem cannot follow from support, sampled BV,
\(\chi_4\), or a lift Fourier transform alone.  The still-unproved option is
an actual-symbol correlation making the endpoint births cancel against
product/cell motion before any outside norm.

## 5. Control tests and outcomes

- `literal_three_frontier_statements`: **pass**.  Section 2.2 records the
  nonsquare hard-TOP energy, the exact Round-122 cumulative wavelet, and
  the literal one-sided determinant correlation separately.
- `capacity_and_missing_power_table`: **pass**.  The table uses energy or
  linear scale consistently and records \(L\), \(R\), \(Y^{13/48}\), and
  \(Y^{11/48}\) deficits.  Equations (3.8)--(3.12) audit every proposed
  gain.
- `noninvertible_mechanism_test`: **conditional pass for (SV), fail for the
  scalar proposal**.  The local \(V^2\)-curvature inequality is genuinely
  joint in the lift endpoint and reciprocal \(q\)-sum and has positive
  \(Y^{1/96}\) capacity.  A lift Fourier transform, separated Cauchy, full
  \(G^{1/2}\) norm, or scalar cell norm is not an eligible substitute.
- `prior_no_go_bypass`: **conditional pass for (SV)**.  It bypasses the
  Round-117 moving-endpoint seam by measuring only the births inside the
  same moving curvature window, before a modulus, and does not invoke the
  half-shift transform or clean product completion.  The scalar proposal
  still fails at the Round-118 \(a=1/3\) contact.
- `actual_vs_adversarial_coefficients`: **pass with restricted conclusion**.
  The scalar capacity failure holds even after granting an actual literal
  transfer.  The partial-sum construction (3.5) is explicitly an
  adversarial BV control and is not asserted as a physical lower bound.
- `endpoint_floor_star_and_support_scope`: **pass**.  Equations (2.5)--(2.8)
  keep moving floors, support births, strict/weak endpoints, stars, hard
  samples, profiles, and signs inside the lift transform.  Equation (3.5)
  shows why they cannot be discarded as negligible variation.
- `dependency_and_payoff_scope`: **pass**.  Section 3.4 uses only the
  accepted persistence bridge.  No conclusion is drawn for M9-M1,
  M9-M2, M9, endpoint uniformity, or the quarter theorem.
- `finite_stop_rule`: **pass**.  First prove or refute the local actual
  coefficient norm (2.8), including every hard face and star.  Only if it
  passes, test (SV).  Stop if any step enlarges \(J_B^{1/2}\) to the full
  \(G^{1/2}\), inserts \(N_\rho^{1/2}\), separates a cross-shell owner, or
  gives effective local loss \(J_B^\theta\) with \(\theta\ge2/3\).  Success
  means the literal complete \(Y^{73/96+\varepsilon}\) bound, not an
  exponent theorem.
- `no_proof_status_from_strategy_only`: **pass**.  Strategy statements are
  used only for route/payoff context.  No selected inequality, exponent,
  M9 parent, or target is declared proved.

## 6. Dependencies and exact artifacts used

Accepted graph dependencies used in the derivation are:

- `M9-short-window-triangular-cluster-kernel` for the cell square function;
- `GC-W7-16-reduced-Farey-cluster-reduction` for (2.1), lift aggregation,
  the determinant, and literal coefficient placement;
- `GC-W7-16-original-numerator-product-window-bound` for (2.3);
- `GC-W7-16-bounded-lift-top-shell-curvature-saving` for (2.4) and the
  reciprocal-curvature normalization;
- `GC-W7-16-determinant-half-shift-transform-obstruction` for the parked
  transform/product mechanisms;
- `GC-one-sided-persistence-local-bridge` for (3.10);
- `M9-M1-lower-near-square-wavelet-reduction`,
  `M9-M1-global-lower-radial-signed-estimate`, and
  `M9-M2-top-endpoint-density-discrepancy-energy` only to state the other
  two literal frontiers and their implication scope.

The exact permitted artifacts read were:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0821_full_proof_strategy.md`;
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/synthesis.md`;
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_actual_savings.md`;
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_involution_product_and_source.md`;
- `rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/synthesis.md`.

No numerical experiment, web source, unlisted report, or external theorem
was used.  The effort allocation was 100% analytical/algebraic.

## 7. Recommended state effect

**Recommendation: retain the graded determinant target as open; reject the
scalar-per-cell continuation; retain the local transverse-square-variation
inequality (2.8)+(SV) as an eligible, tightly bounded candidate; make no
proof-state change from this report alone.**

The conductor may, after independent seam review, record the scoped scalar
no-go: at \(D/L=Y^{1/3}\), the certified prescribed-centre scalar envelope
returns the exact \(Y^{37/48}\) complete capacity.  In contrast, the
proposed local square variation counts only
\(J_B=1+DQ_B/B^2\) births in the same curvature window and has the exact
conditional payoff \(Y^{73/96}\).

If the conductor selects this route, the next round should freeze exactly
two gates and no transform work: (i) prove (2.8) coefficientwise for every
literal smooth/hard/floor/star package; (ii) only then prove (SV) without
the generic \(N_\rho^{1/2}\) loss.  Either failure activates the finite
stop rule in Section 5.  Even success banks only \(Y^{1/96}\) on the
complete graded block and leaves the internal pointwise exponent at
\(1/3\); the \(Y^{1/2}\) correlation target, both M9 components, endpoint
uniformity, M9, and the quarter theorem remain open.
