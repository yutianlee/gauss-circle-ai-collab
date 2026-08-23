# Round 128 report: literal lift coefficient and its local square variation

Campaign: `gc-w7-16-local-transverse-lift-variation-gate`
Task: `literal_lift_coefficient_variation_attack`
Role: discovery
Starting graph SHA-256:
`1a5c8c8b4b6c6c0dcf3d0e05a1607b3d29dfe22f66748d401405d1c0f7b474d6`

## 1. Result

There are two different coefficient statements hidden in the proposed
notation.  They have different answers.

After the reduced M1 denominator character is split into its two exact
quarter-linear phases, every remaining literal M1 and M2 complete-lift
amplitude satisfies the desired local estimate

\[
 \boxed{
 \|U_{i,\rho,\eta}\|_{V^2(I)}
 \ll_\varepsilon {J_B^{1/2}\over L}Y^\varepsilon,
 \qquad
 J_B=1+{DQ_B\over B^2}.}
 \tag{128.1}
\]

Here \(\eta=\pm\) for the two M1 quarter-shift packages and there is one
\(\eta=0\) package for M2.  The proof is exact for the accepted sampled
profiles: discrete Stieltjes decomposition writes every denominator
profile, including the hard top and its starred sample, as a bounded-mass
superposition of moving hard faces.  For each face the common lift
character is summed before a modulus.  Its bounded partial sums control
both values at the two \(V^2\) endpoints, while the floor geometry charges
only \(O(J_B)\) births.  Fixed frequency faces, the Vaaler taper, signs,
Möbius weights, the one-sided triangular factor, strict and weak faces,
and cross-shell cuts introduce no larger term.

The same assertion is false if “literal coefficient” means that the
reduced M1 character \(\chi _4(b')\) must remain inside \(U\).  On the
one-lift shell \(B\asymp D\), \(\rho=1\), the actual coefficient contains

\[
 \widetilde U_1(v)=\chi _4(v)R_1(v),
 \qquad |R_1(v)|\asymp L^{-1}
 \tag{128.2}
\]

on an interior reciprocal subwindow of length \(\asymp Q_B\).  Hence

\[
 \|\widetilde U_1\|_{V^2(I)}^2
 \gg {Q_B\over L^2},
 \tag{128.3}
\]

whereas \(J_B=1+Q_B/D\asymp1\).  This is a literal counterterm, not an
adversarial shadow.  It is removed exactly, and only, by the already used
identity

\[
 \chi _4(b')={e(b'/4)-e(-b'/4)\over2i},
 \tag{128.4}
\]

which transfers the rapid reduced character to the oscillatory phase.
Thus (128.1) is a complete packagewise coefficient theorem for the
character-split formulation required by the proposed curvature sum.  The
unsplit wording must be rejected or revised.  No reciprocal-curvature
inequality, fixed-block correlation saving, pointwise exponent, M9 parent,
or quarter theorem is proved here.

## 2. Exact statement and hypotheses

Fix

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},
 \qquad D/L\le B\le D,
 \tag{128.5}
\]

one literal M1 or M2 denominator-frequency block, one frequency sign,
one fixed moving-symbol stratum, one original denominator profile, and
one reduced-denominator shell.  Put

\[
 G={D\over B},\qquad
 Q_B=\min\left(B,{BD\over WL}\right)={BD\over WL},\qquad
 J_B=1+{DQ_B\over B^2}.
 \tag{128.6}
\]

For the inner ray, \(b'=\rho v\asymp B\) and

\[
 |a'|\asymp {LB\over D}={L\over G},
 \qquad \rho\mid a',
 \qquad |I|\ll1+{Q_B\over\rho}.
 \tag{128.7}
\]

The progression is obtained only after extending the literal finite-sum
formula to every integer pair \((a',b')\), and then inserting

\[
 {\bf1}_{(a',b')=1}
 =\sum_{\rho\mid a',\ \rho\mid b'}\mu(\rho).
 \tag{128.8}
\]

This is the same nonprimitive extension required by the accepted
bounded-lift argument; it is a formula extension, not a second physical
owner.

Let \(H\) be the exact Vaaler height of the fixed symbol stratum, let
\(v_L^{*}(|h|)\) be its exact frequency sample (the sign is retained by
the signed variable \(h\)), and let
\(\omega_{i,D,\mathfrak s}^{*}(d;c)\) be the exact zero-extended denominator
sample.  Thus an interior profile is the accepted fixed smooth rescaling,
while the unique hard profile also contains
\({\bf1}_{d\le\lfloor\sqrt c\rfloor}^{*}\).  Set

\[
 \Phi_H(h)=\Phi\!\left({|h|\over H+1}\right),
 \qquad
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u,
 \tag{128.9}
\]

with the accepted endpoint values.  Before any variation estimate, the
literal original coefficients are

\[
 \begin{aligned}
 q_1(h,d)
 &=-4\alpha_{h,H}\chi_4(d)
   \omega_{1,D,\mathfrak s}^{*}(d;c)v_L^{*}(|h|),\\
 q_2(h,d)
 &=4\alpha_{h,H}\bigl(e(h/4)-e(3h/4)\bigr)
   \omega_{2,D,\mathfrak s}^{*}(d;c)v_L^{*}(|h|),\\
 \alpha_{h,H}
 &=-{\Phi_H(h)\over2\pi i h}.
 \end{aligned}
 \tag{128.9a}
\]

Reducing \(h/d=a/b\) and summing exactly
\(A_i(a,b)=\sum_{g\ge1}q_i(ga,gb)\) gives

\[
 \begin{aligned}
 A_1(a,b)
 &=\chi _4(b)\,R_1(a,b),\\
 R_1(a,b)
 &={2\over\pi i a}
   \sum_{g\ge1}^{*}{\chi _4(g)\over g}
   \Phi_H(ga)v_L^{*}(g|a|)
   \omega_{1,D,\mathfrak s}^{*}(gb;c),                               \\[1mm]
 A_2(a,b)
 &=R_2(a,b),\\
 R_2(a,b)
 &=-{4\chi _4(|a|)\over\pi |a|}
   \sum_{g\ge1}^{*}{\chi _4(g)\over g}
   \Phi_H(ga)v_L^{*}(g|a|)
   \omega_{2,D,\mathfrak s}^{*}(gb;c).
 \end{aligned}
 \tag{128.10}
\]

The factors \(\chi _4(g)\chi _4(b)=\chi _4(gb)\) in M1 and
\(\chi _4(g)\chi _4(|a|)=\chi _4(|ga|)\) in M2 give zero automatically
on the forbidden even samples.  The factor four in M2, the signed
\(1/a\) in M1, both frequency signs, and the fixed M2 product-sector sign
are therefore not suppressed.  Formula (128.10) is the complete lift
dictionary; in particular no liftwise modulus has been taken.

There is no remaining literal support coupled in \((ga,gb)\):
\(\Phi_H(ga)v_L^*(g|a|)\) is frequency-only and
\(\omega_{i,D,\mathfrak s}^*(gb;c)\) is denominator-only, with every
profile, prefix, hard face, support indicator, and star already included.
The determinant/cell restriction introduced after ray aggregation is the
single reduced-variable multiplier \(T_i(v)\) below.  Thus no unidentified
mixed \((g,v)\) support package remains outside the Stieltjes argument.

For fixed outer \((a,b)\), fixed \(a'\), and
\(\kappa _1=1,\ \kappa _2=4\), write

\[
 n(v)=a\rho v-a'b
 \tag{128.11}
\]

and let \(T_{i}(v)\) be the exact zero-extended product of

\[
 {\bf1}^{\rm literal}_{0<n(v)<\kappa_i b\rho v/W},
 \qquad
 1-{Wn(v)\over\kappa_i b\rho v},
 \qquad
 {\bf1}^{\rm owner}_{\rho v\asymp B},
 \tag{128.12}
\]

together with the fixed cell, sign-sector, and support faces.  “Literal”
in (128.12) means the prescribed strict/weak and starred values, rather
than a smoothed replacement.  On every clipped interval
\(\|T_i\|_\infty+\operatorname {Var}T_i\ll1\).

The exact character-split coefficient packages in the reciprocal sums
are

\[
 \begin{aligned}
 U_{1,\rho,+}(v)
 &= {\mu(\rho)\over2i}\,T_1(v)\,
    \overline{R_1(a',\rho v)},
 &\vartheta_{1,+}&={1\over4},\\
 U_{1,\rho,-}(v)
 &=-{\mu(\rho)\over2i}\,T_1(v)\,
    \overline{R_1(a',\rho v)},
 &\vartheta_{1,-}&=-{1\over4},\\
 U_{2,\rho,0}(v)
 &=\mu(\rho)\epsilon_{\rm sgn}\,T_2(v)\,
    \overline{R_2(a',\rho v)},
 &\vartheta_{2,0}&=0.
 \end{aligned}
 \tag{128.13}
\]

Indeed the corresponding phases are exactly

\[
 e\!\left(-{ca'\over\kappa_i\rho v}
             +\vartheta_{i,\eta}\rho v\right).
 \tag{128.14}
\]

The theorem proved in this report is (128.1) for every package in
(128.13), uniformly in all the displayed data.  The unsplit alternative
\(T_1(v)\chi _4(\rho v)\overline{R_1(a',\rho v)}\) is explicitly not
part of that theorem and obeys the no-go (128.3).

## 3. Proof or derivation

**Fixed lift weight.**  Remove only the denominator sample from one of
the sums in (128.10), and call the resulting fixed sequence
\(\gamma_i(g;a')\).  On (128.7), every nonzero term has
\(g\asymp G\) and \(g|a'|\asymp L\).  The accepted \(C^1\) bound for
\(\Phi\), the sampled-BV frequency profile, \(1/g\), and every fixed
frequency floor or star give

\[
 \|\gamma_i\|_{\mathrm{BV}(\mathbb Z)}
 :=\sup_g|\gamma_i(g)|+
   \sum_g|\gamma_i(g+1)-\gamma_i(g)|
 \ll_\varepsilon {Y^\varepsilon\over |a'|G}
 \ll_\varepsilon {Y^\varepsilon\over L}.
 \tag{128.15}
\]

This calculation includes the constants \(2/(\pi ia')\) and
\(-4\chi _4(|a'|)/(\pi|a'|)\).  The Vaaler height and all moving
symbols are fixed on the chosen stratum; hence they have no hidden
\(v\)-dependence.

**Character partial sums and both \(V^2\) endpoint values.**  Put

\[
 P_i(M)=\sum_{g\le M}^{*}\chi _4(g)\gamma_i(g;a').
 \tag{128.16}
\]

The periodic character satisfies
\(\sup_x|\sum_{g\le x}\chi _4(g)|\le1\).  Discrete Abel summation,
performed before any modulus over the lifts, and (128.15) imply

\[
 \sup_M|P_i(M)|\ll_\varepsilon {Y^\varepsilon\over L}.
 \tag{128.17}
\]

This proves, rather than assumes, the required bounds for
\(U(v_-)\) and \(U(v_+)\).  A star at \(M\) changes (128.16) by at most
half of one term and is covered by the same estimate.

**Exact denominator-profile decomposition.**  Zero-extend the actual
sample \(w(d)=\omega_{i,D,\mathfrak s}^{*}(d;c)\), and set

\[
 c_k=w(k)-w(k+1).
 \tag{128.18}
\]

Then, at every integer sample and with its actual hard/star value,

\[
 w(d)=\sum_{k\ge d}c_k,
 \qquad
 \sum_k|c_k|\ll1.
 \tag{128.19}
\]

The second assertion is exactly the accepted discrete-BV profile bound.
It includes the smooth taper, the lower and upper support exits, the hard
sample at \(\lfloor\sqrt c\rfloor\), and a prescribed half weight.  Thus
there is no unpriced “continuous profile” remainder: (128.19) is an exact
discrete Stieltjes decomposition of it into moving faces.

For \(b'=\rho v\), (128.16)--(128.19) give the identity

\[
 R_i(a',\rho v)
 =\sum_k c_k
   P_i\!\left(\left\lfloor{k\over\rho v}\right\rfloor\right).
 \tag{128.20}
\]

All fixed frequency support restrictions are already inside
\(\gamma_i\), so (128.20) does not complete or enlarge a literal lift
range.

**Local birth count.**  For \(k\asymp D\), set

\[
 M_k(v)=\left\lfloor{k\over\rho v}\right\rfloor.
 \tag{128.21}
\]

Across the same physical \(b'\)-window of length at most \(Q_B\) used by
the reciprocal curvature estimate,

\[
 \sum_{v,v+1\in I}|M_k(v+1)-M_k(v)|
 \ll1+{DQ_B\over B^2}=J_B.
 \tag{128.22}
\]

No completed shell is used in (128.22).  Moreover one progression step
cannot hide many simultaneous births.  Since \(\rho\mid a'\),

\[
 {D\rho\over B^2}
 \le {D|a'|\over B^2}
 \ll {L\over B}
 \le {L^2\over D}=Y^{-1/6},
 \tag{128.23}
\]

up to fixed dyadic constants.  Consequently
\(\max_v|M_k(v+1)-M_k(v)|\ll1\).  From (128.15), (128.22), and
(128.23),

\[
 \sum_{v,v+1\in I}
 \left|
 P_i(M_k(v+1))-P_i(M_k(v))
 \right|^2
 \ll_\varepsilon {J_B\over L^2}Y^\varepsilon.
 \tag{128.24}
\]

Together with the two endpoint estimates (128.17), this says

\[
 \left\|P_i(M_k(\cdot))\right\|_{V^2(I)}
 \ll_\varepsilon {J_B^{1/2}\over L}Y^\varepsilon.
 \tag{128.25}
\]

The \(V^2\) norm is the Euclidean norm of the vector consisting of its
left value, successive increments, and right value.  Minkowski's
inequality applied to the exact identity (128.20), followed by
(128.19), proves

\[
 \|R_i(a',\rho\,\cdot)\|_{V^2(I)}
 \ll_\varepsilon {J_B^{1/2}\over L}Y^\varepsilon,
 \qquad
 \sup_{v\in I}|R_i(a',\rho v)|
 \ll_\varepsilon L^{-1}Y^\varepsilon.
 \tag{128.26}
\]

This simultaneously charges all lower/upper support births, smooth
profile motion, floors, stars, and the hard face.  A direct difference
calculation gives the smaller smooth contribution
\(\sum|\Delta R|^2\ll Q_B\rho/(B^2L^2)\), but it is not needed for
(128.26).

**Triangular taper, cells, hard faces, and shell ownership.**  On each
clipped determinant interval,

\[
 {n(v)\over\rho v}=a-{a'b\over\rho v}
 \tag{128.27}
\]

is monotone.  Hence the positive one-sided triangular factor in
(128.12), zero-extended with its literal face values, has total variation
\(O(1)\).  A frequency-cell face, sign-sector face, or half-open
\(B\)-shell owner adds only \(O(1)\) jumps.  If \(T\) denotes their
product, then

\[
 \begin{split}
 |\Delta(TR)|
 &\le |T|\,|\Delta R|+|R(v+1)|\,|\Delta T|,\\
 \sum_v|\Delta T(v)|^2
 &\le \operatorname {Var}(T)^2\ll1.
 \end{split}
 \tag{128.28}
\]

Equations (128.26)--(128.28), including the two product endpoint values,
give (128.1).  A \(Q_B\le B\) window meets only \(O(1)\) adjacent
half-open shells; splitting at those faces assigns every term to exactly
one inner-shell owner.  The original \(D\)-profile owner stays inside
(128.20), and the outer ray is not re-counted.

**Möbius and reduced characters.**  The factors \(\mu(\rho)\) and the
fixed M2 sign have modulus at most one.  The proof is uniform in every
\(\rho\mid a'\); summing all progressions later costs only
\(\tau(a')\ll_\varepsilon Y^\varepsilon\).  In M1, leaving
\(\chi _4(\rho v)\) in the amplitude would introduce a jump at essentially
every \(v\).  Identity (128.4) instead produces exactly the two packages
in (128.13), with the character owned by the phases
\(e(\pm\rho v/4)\).  In M2 the reduced character \(\chi _4(|a'|)\) is
constant in \(v\) and is already included in (128.10).  The common lift
character \(\chi _4(g)\), by contrast, remains inside (128.16) until its
partial-sum cancellation has been used.

**Literal unsplit M1 counterterm.**  Take the top reduced shell
\(B\asymp D\), \(\rho=1\), and an interior literal profile subpacket on
which the unique nonzero lift is \(g=1\).  Choose \(a'\asymp L\) away
from its frequency and Vaaler faces, and take a middle fixed fraction of
a generic determinant window, so the denominator profile and triangular
factor are bounded away from zero.  Since \(Q_B=o(D)\), such a subwindow
has length \(\asymp Q_B\), and (128.10) gives
\(|R_1(a',v)|\asymp L^{-1}\) there with only scale-\(D\) drift.  The
sequence \(\chi _4(v)\) is \(1,0,-1,0,\ldots\).  Every odd-to-even or
even-to-odd step therefore contributes \(\gg L^{-2}\) to the squared
increment sum.  This proves (128.3).  At this shell

\[
 Q_B={D^2\over WL}=Y^{19/48},
 \qquad
 J_B=1+{Q_B\over D}\asymp1,
 \tag{128.29}
\]

so the unsplit version contradicts (128.1) by the power
\(Q_B^{1/2}\).  The counterterm is exactly the quarter-linear character
already exposed in (128.4); no floor, star, or boundary convention can
absorb it.

**Adversarial lift control.**  If the common lift factors are replaced by
phase-conjugating coefficients, then at an interior endpoint

\[
 \sum_{g\asymp G}{1\over |a'|g}
 \asymp {1\over|a'|}={G\over L},
 \tag{128.30}
\]

rather than \(O(L^{-1})\).  At the longest shell \(G=L\), this already
violates the desired endpoint term.  Thus (128.1) genuinely uses the
actual common \(\chi _4(g)\); it does not prove the false arbitrary- or
phase-adapted-coefficient analogue.

## 4. First doubtful or unproved step

There is no remaining coefficient-level estimate after the exact
character ownership is fixed as in (128.13).  The first presentation seam
is that the phrase “literal complete-lift coefficient” is ambiguous: if it
includes \(\chi _4(b')\) inside M1's \(V^2\) amplitude, (128.3) is the
first exact counterterm and the route stops.  The minimal repair is to
state Gate 1 for the two exact M1 additive-character branches and the one
M2 branch, with \(\vartheta_{1,\pm}=\pm1/4\) and
\(\vartheta_{2,0}=0\).  This is not a relaxation; it is the exact algebra
of the literal coefficient.

Under that repaired statement, the first genuinely unproved analytic
step is the joint inequality

\[
 \left|\sum_{v\in I}^{*}U_{i,\rho,\eta}(v)
 e\!\left(-{ca'\over\kappa_i\rho v}
          +\vartheta_{i,\eta}\rho v\right)\right|
 \ll_\varepsilon
 \|U_{i,\rho,\eta}\|_{V^2(I)}
 \min\!\left(
 N_\rho,
 N_\rho\sqrt{\lambda_B\rho^2}
 +(\lambda_B\rho^2)^{-1/2}
 \right)Y^\varepsilon,
 \tag{128.31}
\]

where

\[
 N_\rho\asymp {Q_B\over\rho},
 \qquad
 \lambda_B={YL\over DB^2}.
 \tag{128.32}
\]

Nothing in this report proves (128.31).  Generic partial summation and
Cauchy insert the forbidden factor \(N_\rho^{1/2}\), and arbitrary
coefficients may conjugate the reciprocal phase.  Consequently a proof
of (128.1) licenses only a later test of (128.31), not the conditional
\(Y^{73/96+\varepsilon}\) shell assembly.

## 5. Control tests and outcomes

| Required control | Exact audit | Outcome |
|---|---|---|
| `literal_complete_lift_dictionary` | Equations (128.9)--(128.14) reconstruct M1 and M2 before a norm, including constants, Vaaler taper, reduced and common characters, signs, profiles, lifts, Möbius branches, triangular weight, and phase shifts. | **Pass after an explicit M1 character split.** The unsplit dictionary fails by (128.3). |
| `local_window_and_birth_count` | Use the same physical \(b'\)-window of length \(Q_B\); (128.22) gives exactly \(1+DQ_B/B^2\), while (128.23) forbids batched births. | **Pass.** No full-shell \(G\) count is substituted. |
| `V2_endpoint_terms` | Abel summation gives (128.17) at every sampled endpoint; (128.19) and Minkowski preserve it for the full profile. | **Pass** for every split package. Endpoint control is not inferred from increments. |
| `continuous_weight_variation` | The exact discrete Stieltjes identity (128.19) contains all sampled smooth motion; the triangular/profile-side common multiplier has \(O(1)\) BV by (128.27)--(128.28). | **Pass.** There is no derivative residual. |
| `character_partial_sum_before_modulus` | Keep \(\chi _4(g)\) in (128.16), use its partial sums, and only then take the modulus in (128.17). | **Pass.** The adversarial replacement fails by (128.30), as required. |
| `mobius_divisor_progressions` | Extend the formula before (128.8), prove the estimate uniformly for \(b'=\rho v\), use \(\rho\le|a'|\) in (128.23), and charge \(\tau(a')\) only after the progression estimate. | **Pass.** No density heuristic or missing \(\rho^{1/2}\) occurs. |
| `floors_stars_hard_faces_and_support` | Exact sampled values enter (128.18); every denominator floor/hard/star face becomes a term in (128.20), while fixed frequency faces stay in \(\gamma_i\). | **Pass.** Each moving face has \(O(J_B)\) births and each fixed face costs \(O(1)\). |
| `cross_shell_owner_and_no_duplication` | Use half-open \(B\)-shells, split a \(Q_B\le B\) window at its \(O(1)\) shell faces, and retain the original \(D\)-profile in the lift sum. | **Pass.** Inner terms have one shell owner; outer rays are not duplicated. |
| `actual_vs_adversarial_lift_coefficients` | Actual \(\chi _4(g)\) gives (128.17); phase-conjugated lift weights give the endpoint (128.30). | **Pass with required false-control failure.** |
| Reduced M1 character | Keep \(\chi _4(\rho v)\) inside \(U\), then test the one-lift shell. | **Literal fail:** (128.3). **Exact repair:** the two phase packages (128.13). |
| `theta_two_thirds_capacity_threshold` | A local loss \(J_B^\theta/L\) produces worst shell exponent \(35/48+\theta/16\), which is below \(37/48\) exactly when \(\theta<2/3\). | **Pass** for the split packages, where \(\theta=1/2\). The unsplit \(Q_B^{1/2}\) loss triggers the stop rule. |
| `finite_stop_rule` | Do not attempt (128.31) unless the branchwise definition is adopted; stop immediately if the unsplit norm is required or if a later proof adds \(N_\rho^{1/2}\), full \(G^{1/2}\), or loses an owner. | **Pass.** |
| `no_exponent_or_M9_promotion` | Compare (128.1) only with the conditional connector; (128.31) remains open. | **Pass.** No fixed-block saving, global exponent, M9 component, M9, endpoint-uniformity theorem, or quarter theorem follows. |

All controls are analytical/algebraic.  No numerical experiment and no
external source were used.

## 6. Dependencies and exact artifacts used

This report read and used every context artifact permitted by the brief,
plus the exact factorization artifact supplied by the conductor:

1. `protocol.md`, for graph authority, the signed/unsigned distinction,
   the no-vote promotion rule, controls, and report contract;
2. `state/proof_obligations.yml`, in particular the accepted H4 and
   \(\Phi\) normalization, M2 beta algebra, dyadic-profile BV and hard-top
   ownership, signed lift cancellation, exact reduced-Farey reduction,
   original-variable product-window bound, bounded-lift curvature lemma,
   conditional local transverse connector, and their current scopes;
3. `state/active_campaign.yml`, for the frozen \(W,D,L,B,Q_B,J_B\)
   normalization, the \(V^2\) endpoint convention, completion tests, and
   finite stop rule;
4. `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/synthesis.md`,
   for lift-first aggregation, M1/M2 reduced-character placement, the
   accepted \(L^{-1}\) coefficient scale, literal owners, and the exact
   determinant correlation;
5. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reports/actual_character_determinant_attack.md`,
   for (117.7), the nonprimitive Möbius extension, the M1 quarter shifts,
   the M2 fixed reduced character, clipped reciprocal windows, and the
   long-lift variation seam;
6. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/hostile_round117_discovery_addendum.md`,
   for the exact top-shell BV, hard/star accounting, divisor progressions,
   and the warning that a finite-lift proof alone does not cover \(B<D\);
7. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_actual_savings.md`,
   for the accepted character orientation, curvature normalization, and
   downstream nonimplications;
8. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/synthesis.md`,
   for the certified \(Y^{37/48}\) and top-shell \(Y^{35/48}\) capacities,
   transform obstruction, and exact long-lift frontier;
9. `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/graded_determinant_long_lift_feasibility.md`,
   for the proposed \(V^2\) norm, the same-window birth count, the
   conditional curvature inequality, and the \(\theta<2/3\) arithmetic;
   and
10. `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reviews/conductor_round127_frontier_selection_adjudication.md`,
    for the exact sequential gate, capacity threshold, and stop rule.

11. rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reports/actual_rational_cluster_attack.md,
    especially (2.1)--(2.4) and (3.4)--(3.7), for the exact original
    coefficients, complete ray sum, frequency-only
    \(\Phi v_L\)/denominator-only \(\omega_{i,D}\) factorization, and the
    statement that all literal supports and stars are contained in that
    factorization.

The derivation adds only discrete Abel summation, the exact discrete
Stieltjes identity (128.18)--(128.20), monotone floor geometry, and
Minkowski in the finite \(V^2\) vector.  It does not use a sibling
Round-128 report, computation, or web literature.

## 7. Recommended state effect

**Revise, then promote after independent seam review,** the coefficient
half of `GC-W7-16-local-transverse-square-variation-connector` as the
branchwise lemma (128.1) with the exact dictionary (128.10)--(128.14).
The statement must say that M1's reduced \(\chi _4(b')\) is owned by the
two quarter-linear phases before the \(V^2\) norm is taken.  Record the
discrete-Stieltjes/character-partial-sum proof as closing smooth, hard,
floor, star, support-motion, endpoint-value, Möbius, and cross-shell seams
for those packages.

**Reject** the stronger unsplit claim
\(\|\chi _4(\rho\,\cdot)R_1\|_{V^2}\ll J_B^{1/2}/L\).  Equation (128.3)
is its first literal counterterm and should be retained as a normalization
obstruction.  Also retain the phase-conjugated common-lift endpoint
(128.30) as the required false control, not as a physical lower bound.

**Retain open** the joint \(V^2\)-weighted reciprocal-curvature theorem
(128.31).  Until it is proved with no \(N_\rho^{1/2}\), full-lift, or owner
loss, do not promote the conditional \(Y^{73/96+\varepsilon}\) complete
block.  Make no change to the actual \(Y^{1/2}\) determinant target, the
global pointwise exponent, M9-M1, M9-M2, endpoint uniformity, M9, the
conditional quarter bridge, or the Gauss-circle target.
