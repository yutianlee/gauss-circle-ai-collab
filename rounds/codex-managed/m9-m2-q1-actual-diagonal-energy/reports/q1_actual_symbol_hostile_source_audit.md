# Round 103 hostile/source audit: complete sampled-\(k\) variation closes the singleton actual diagonal

Campaign: `m9-m2-q1-actual-diagonal-energy`
Task: `q1_actual_symbol_hostile_source_audit`
Role: hostile mathematical and primary-source auditor
Status: candidate evidence only; no shared proof state is edited.

## 1. Result

**Complete actual-symbol upper theorem and target-safe reciprocal
diagonal.**  The proposed centred-integral
sampled-\(k\) argument has the correct normalization and, unlike the
Round-80 formal half-frequency argument, contains a genuinely new
actual-symbol input.  It is not invalidated by carrier self-return.

Put \(b=a+2\),

\[
 \theta_{a,k}={\Lambda_a\over k},\qquad
 V:=\sqrt{AL/J},\qquad K\asymp {J\over A},\qquad
 G\asymp {L\over A}.
\]

For fixed \(a,g\), the complete centred physical integral itself obeys
the sampled reciprocal variation estimate

\[
 \sup_{k\in I_a\cap\mathbb Z}|\mathfrak B^\circ_{a,k}(g)|
 +\sum_{k,k+1\in I_a}
  |\mathfrak B^\circ_{a,k+1}(g)
   -\mathfrak B^\circ_{a,k}(g)|
 \ll X^\varepsilon V.                                  \tag{103.H1}
\]

The bound is uniform through saddle entry and exit.  Its proof uses the
literal Round-77 factorisation, not a leading stationary value.  The
complete remaining multiplier \(\Omega_{a,g}(k)\), containing every
owner, profile and orientation not already inside
\(\mathfrak B^\circ\), satisfies the equally literal product bound

\[
 \sup_k|\Omega_{a,g}(k)\mathfrak B^\circ_{a,k}(g)|
 +\sum_k|\Delta_k(\Omega_{a,g}\mathfrak B^\circ_{a,\cdot}(g))|
 \ll X^\varepsilon V,                                  \tag{103.H2}
\]

and hence the full singleton row satisfies

\[
 |F_a(1)|\ll_\varepsilon X^\varepsilon {L^2\over A},
 \qquad
 \boxed{\sum_{a\asymp A}|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon {L^4\over A}.}          \tag{103.H3}
\]

Thus the complete proposed upper proof passes.  The density
mode is retained and estimated; the Gaussian carrier is used once; and no
second transform is counted as a gain.

The authorized exact owner formula closes the only initially opaque seam.
It puts the exact \(\Phi,q_X,W\) profiles, floors, stars, both fixed
collars, finite odd-lift support and every saddle transition inside
\(A^\circ\).  Outside the integral, \(\omega(k)\) consists only of fixed
smooth dyadic cutoffs of bounded variation and the residual exclusions.
For \(q=1\), primitivity is automatic, the square-ray exclusion is empty,
the \(\rho\)-safe exclusion is blockwise constant, exact centres are
killed by \(W_R(0)=0\), the collar error is already disjoint, reciprocal
zero extension has two jumps, and the orientations are finitely many
conjugates.  Product variation therefore proves (103.H2) with the full
actual symbol.  Equation (103.H3) is an unconditional internal theorem on
the frozen singleton block.

There is an unconditional fallback reduction that uses only boundedness.
Writing the exact row as \(F_a(1)=\sum_k Z_{a,k}\), its reciprocal
diagonal obeys

\[
 \sum_{a,k}|Z_{a,k}|^2
 \ll_\varepsilon X^\varepsilon {L^3\over A}
 \le X^\varepsilon {L^4\over A}.                       \tag{103.H4}
\]

Hence empty and singleton \(k\)-fibres are target-safe independently of
the stronger theorem.  The signed \(k\ne k'\) correlation is controlled
by the sampled-\(k\) argument, so no singleton survivor and no literal
actual lower obstruction remain.

## 2. Exact statement and hypotheses

Let \(e(t)=e^{2\pi i t}\), \(J=\sqrt X\), and work on one residual
singleton \(q=1\) block.  Thus \(a\asymp A\) is odd,
\(b=a+2\), and

\[
 \delta_a=\sqrt{a+2}-\sqrt a={2\over\sqrt a+\sqrt{a+2}},
\]

\[
 \lambda_a={\delta_a^2\over2}
 =a+1-\sqrt{a(a+2)}
 ={1\over a+1+\sqrt{a(a+2)}},\qquad
 \Lambda_a=X\lambda_a.                                \tag{103.H5}
\]

The literal open reciprocal interval is

\[
 I_a=\left({J\over\sqrt a(\sqrt a+\sqrt{a+2})},
 {2J\over\sqrt{a+2}(\sqrt a+\sqrt{a+2})}\right),       \tag{103.H6}
\]

so \(k\asymp K\asymp J/A\).  On it,

\[
 {J\sqrt{a+2}\over\sqrt a+\sqrt{a+2}}
 <\theta_{a,k}<
 {2J\sqrt a\over\sqrt a+\sqrt{a+2}},                 \tag{103.H7}
\]

and the centred saddle

\[
 r_k={J\delta_a\over2k},\qquad
 u_k=r_k^2={\Lambda_a\over2k^2}                        \tag{103.H8}
\]

runs monotonically from \(u=a\) to \(u=b/4\).  Therefore the two open
endpoints in (103.H6) are exactly saddle exit and entry, not arbitrary
cutoffs.

The complete uncentred and centred integrals are

\[
 \mathfrak C^\circ_{a,k}(g)
 =g\int_{b/4}^{a}A^\circ_{ga,gb}(gu)
   e\!\left(g[ku-J\delta_a\sqrt u]\right)\,du,
\]

\[
 \mathfrak C^\circ_{a,k}(g)
 =e(-g\theta_{a,k}/2)\mathfrak B^\circ_{a,k}(g). \tag{103.H9}
\]

All fixed physical collars and incomplete-Fresnel transitions remain in
these exact integrals.  Let \(\mathcal G_a\) be the literal finite odd-lift
support, of size \(O(G)\), and write the row, after only an algebraic
regrouping, as

\[
 F_a(1)=\mathbf1_{\rm residual}
 \sum_{k\in I_a\cap\mathbb Z}W_R(\theta_{a,k})
 \sum_{g\in\mathcal G_a}
 \Omega_{a,g}(k)e(-g\theta_{a,k}/2)
 \mathfrak B^\circ_{a,k}(g).                     \tag{103.H10}
\]

Here \(\Omega\) is not an arbitrary coefficient: it is exactly the
product of the accepted primitive and prior-owner masks, normalized
profiles not already in \(A^\circ\), floors, stars, signs, conjugate
orientation, block cutoff and zero extension.  The proof uses precisely
(103.H2), rather than merely \(|\Omega|\le1\).  The
authorized owner formula verifies this hypothesis: all \(k\)-dependent
factors outside \(\mathfrak B^\circ\) are fixed smooth dyadic cutoffs or
the two zero-extension jumps, while every other residual owner is
constant or redundant on this \(q=1\) strict-metric block.

The strict metric window is kept complete and has

\[
 W_R(t)=\sum_{\nu\in\mathbb Z}\widehat W_R(\nu)e(\nu t),
 \qquad
 |\widehat W_R(\nu)|\ll_N {1\over R}
       (1+|\nu|/R)^{-N},\qquad 1\le R\le G.             \tag{103.H11}
\]

Its \(\nu=0\) density coefficient is included.  Fixed translates and the
two sides of the annulus only change fixed constants.

The active scale hypotheses are

\[
 A\ll L\le J^{1/2},\qquad
 K\asymp J/A,\qquad G\asymp L/A,\qquad
 \rho={AJ\over L^3}>1.                                \tag{103.H12}
\]

The first inequality follows on every nonempty physical row from
\(ga\asymp L\) and \(g\ge1\).  The exact energy ledger is

\[
 E_{0,\rm short}\asymp LJ,\qquad
 {E_{0,\rm short}\over\rho}={L^4\over A},\qquad
 P_{\rm abs}\asymp\sqrt{AJL}=L^2\sqrt\rho.             \tag{103.H13}
\]

No assertion in this report covers a longer \(q\)-row.

## 3. Proof or derivation

The identities (103.H5)--(103.H8) follow by rationalising
\(\sqrt{a+2}-\sqrt a\).  They verify the factor \(1/2\), orientation and
moving-fibre normalization.  Also

\[
 ku-J\delta_a\sqrt u
 =k(\sqrt u-r_k)^2-\theta_{a,k}/2,                     \tag{103.H14}
\]

which proves (103.H9) with no stationary approximation.

For the sampled-\(k\) estimate, the exact Round-77 factorisation and the
change \(y=\sqrt u\) give, for fixed \(a,g\),

\[
 \mathfrak B^\circ_{a,k}(g)
 =L^3g^{-2}P_a(g)
   \int q_{a,g}(y)e\!\left(gk(y-r_k)^2\right)\,dy.      \tag{103.H15}
\]

The complete actual profile \(q_{a,g}\) is independent of \(k\).  It
contains both real-affine physical collars and satisfies

\[
 \|q_{a,g}\|_\infty+\operatorname{Var}(q_{a,g})
 \ll A^{-5/2}.                                        \tag{103.H16}
\]

The collar width in the \(y\)-variable and the stationary width are

\[
 w_c\asymp{1\over g\sqrt A},\qquad
 w=(gk)^{-1/2},\qquad
 {w_c^2\over w^2}={k\over gA}\asymp {J\over AL}\ge1. \tag{103.H17}
\]

Thus no collar is narrower than one stationary width.  A uniform
complete-Fresnel variation lemma gives

\[
 \sup_{k\in I_a}|T_{gk}q_{a,g}(r_k)|
 +\int_{I_a}\left|{d\over dk}T_{gk}q_{a,g}(r_k)\right|dk
 \ll A^{-5/2}(gK)^{-1/2}.                              \tag{103.H18}
\]

For clarity, this is not a leading-term assertion.  To prove it, split at
\(|y-r_k|\le2(gk)^{-1/2}\), use the exact Fresnel integral on the central
piece, and integrate twice by parts on the dyadic outer annuli.  When
\(r_k\) crosses a collar, (103.H17) keeps every differentiated collar
factor at the central scale.  Along the path \(k\mapsto(gk,r_k)\), the
parameter \(gk\) changes only dyadically and \(r_k\) traverses the support
once monotonically.  The identity used to differentiate the quadratic
kernel is the same complete-Fresnel identity as in the accepted
Round-77 \(g\)-variation proof; flat collars kill its boundary term.
Consequently the central value, both transitions and the nonstationary
tails each have total variation bounded by the right side of
(103.H18).  Sampling the integral variation and adding the two
zero-extension endpoint jumps proves (103.H1), because

\[
 L^3g^{-2}A^{-5/2}(gK)^{-1/2}
 \asymp \sqrt{AL/J}=V.                                \tag{103.H19}
\]

Now expand (103.H11) in (103.H10).  For one \(\nu,g\), the reciprocal
phase is

\[
 f_{\nu,g}(k)=(\nu-g/2){\Lambda_a\over k},\qquad
 n:=|2\nu-g|\ge1,                                     \tag{103.H20}
\]

because every actual lift \(g\) is odd.  On the whole fixed-ratio interval
(103.H6),

\[
 |f_{\nu,g}''(k)|\asymp {n\Lambda_a\over K^3}
 \asymp {nA^2\over J}.                                \tag{103.H21}
\]

The elementary second-derivative estimate, uniformly on every
subinterval, is therefore

\[
 \max_{U\subset I_a}
 \left|\sum_{k\in U\cap\mathbb Z}e(f_{\nu,g}(k))\right|
 \ll \sqrt{nJ}+{\sqrt J\over A\sqrt n}.               \tag{103.H22}
\]

It follows directly from the usual differencing/first-derivative proof
of the second-derivative lemma; no external estimate is imported.
Partial summation with (103.H2) multiplies (103.H22) by
\(X^\varepsilon V\).

The Fourier moments needed to sum \(\nu\) are exactly

\[
 \sum_\nu|\widehat W_R(\nu)|\,|2\nu-g|^{1/2}
 \ll\sqrt G,\qquad
 \sum_\nu|\widehat W_R(\nu)|\,|2\nu-g|^{-1/2}
 \ll G^{-1/2}.                                        \tag{103.H23}
\]

For the first, use \(\sqrt{|2\nu-g|}\ll\sqrt G+\sqrt{|\nu|}\)
and (103.H11).  For the second, if \(R\ll G\) the main Fourier mass has
\(|2\nu-g|\asymp G\); if \(R\asymp G\), summing the odd distances from
\(g/2\) gives \(R^{-1}\sum_{m\ll R}(2m+1)^{-1/2}\ll
G^{-1/2}\).  The tails follow from the rapid decay.  This argument also
covers \(G\asymp1\).

Combining (103.H19), (103.H22) and (103.H23), the complete \(k,\nu\)
sum for one fixed \(g\) is

\[
 \ll X^\varepsilon V\sqrt J
 \left(\sqrt G+{1\over A\sqrt G}\right)
 \ll X^\varepsilon(L+1).                              \tag{103.H24}
\]

There are \(O(G)=O(L/A)\) actual odd lifts.  Taking absolute values only
at this final finite \(g\)-sum gives the pointwise row bound in
(103.H3), and summing its square over \(O(A)\) values of \(a\) gives the
energy target.

This does not delete the Round-80 density term.  If
\(\theta=\ell+\eta\), then for odd \(g\)

\[
 (-1)^{1+\ell}\mathfrak B^\circ(g)e(-g\eta/2)
 =-\mathfrak C^\circ(g).                         \tag{103.H25}
\]

Thus quotient parity is still not an independent sign.  In the centred
representation the density mode is \(\nu=0\), hence \(n=g\), and it is
estimated in (103.H22)--(103.H24).  Rewriting the same calculation with
\(\mathfrak C^\circ\) returns to the uncentred physical integral;
it does not erase the cancellation.  Round 80 ruled out a conclusion from
formal half-frequency support plus \(g\)-variation alone.  Here (103.H1)
is a new sampled-\(k\) property of the complete actual integral, so there
is no logical conflict and no duplicated transform gain.

Finally, without (103.H2), put

\[
 Z_{a,k}:=W_R(\theta_{a,k})
 \sum_{g\in\mathcal G_a}\Omega_{a,g}(k)
 \mathfrak C^\circ_{a,k}(g).
\]

The accepted pointwise complete-Fresnel bound gives
\(|Z_{a,k}|\ll X^\varepsilon GV\).  Since there are
\(O(AK)=O(J)\) pairs \((a,k)\),

\[
 \sum_{a,k}|Z_{a,k}|^2
 \ll X^\varepsilon JG^2V^2
 \asymp X^\varepsilon {L^3\over A},
\]

which proves (103.H4).  Before applying the stronger sampled-\(k\) lemma,
the exact off-diagonal part is

\[
 2\Re\sum_a\sum_{k<k'}Z_{a,k}\overline{Z_{a,k'}},       \tag{103.H26}
\]

with every owner and actual integral retained.

## 4. First doubtful or unproved step

The initially doubtful seam was not the Gaussian phase, the van der
Corput power, or the Fourier summation.  It was the replacement of the
packet's semantic multiplier \(\omega_{a,g,k}\) by a factor
\(\Omega_{a,g}(k)\) satisfying (103.H2).  The authorized exact formula
closes that seam.  Its line audit is as follows.

- For \(b=a+2\) with odd \(a\), \((a,b)=1\) automatically and
  \(ab=(a+1)^2-1\) is never a square.  The primitive and square-ray masks
  are therefore constant on the \(k\)-row.
- A strict metric window vanishes at every exact centre, so the exact-
  centre owner causes no additional deletion on its support.
- The reciprocal support (103.H6) is one interval.  A smooth dyadic
  \(k\)-profile or sharp zero extension has bounded variation, with only
  two endpoint jumps.
- The actual \(\eta_L,\Phi,W,q_X\) profiles and the floor/star data in
  the Round-77 bulk, the finite odd-lift support, every saddle transition
  and both real-affine collars are already inside \(q_{a,g}\) in
  (103.H15), so they are not external jagged masks.
- The \(\rho\)-safe owner is blockwise constant, and the disjoint
  Round-77 collar error is not reinserted into the residual row.
- Conjugation and the two fixed orientations preserve (103.H1).

This list exhausts \(\omega\); product variation proves (103.H2).  The
arbitrary-jagged-mask warning remains a false-shadow control, not a gap in
the literal proof.  No doubtful step remains inside the frozen singleton
upper theorem.  The first unproved analytic step after it is the
longer-row fixed-\(a\) actual Gram: there \(q\)-shifts move two independent
\(k,g\) fibres and owner products, and the present one-row pointwise
argument supplies no signed nonzero-shift correlation estimate.

The first missing step for a literal lower obstruction is much earlier.
A stationary plateau would have to prove a nonzero, common-sign value of
the full \(\Omega\mathfrak B^\circ\), coherence across enough active
\(k\)'s, compatibility with both orientations, and domination of every
complementary \(k,g\) contribution inside \(F_a(1)\).  The Gaussian unit
\(e(1/8)\), positive capacity and one recurrent Pell mode do not provide
that lower bound.

## 5. Required controls, outcomes, and primary-source map

| Required control | Hostile test and outcome |
|---|---|
| `literal_q1_coefficient` | Equation (103.H10) retains the exact complete integral. The authorized exact owner formula expands the remaining multiplier and proves (103.H2). **Pass.** |
| `singleton_Gram_normalization` | The half-open row has \(H=1\), so its Gram is exactly \(\sum_a|F_a(1)|^2\). The target is (103.H13). **Pass.** |
| `exact_k_interval` | Rationalisation gives (103.H6), with the correct factor \(1/2\), orientation and open endpoints. **Pass.** |
| `finite_odd_g_support` | Only the actual finite odd set \(\mathcal G_a\) is used; \(\#\mathcal G_a\ll G\). **Pass.** |
| `complete_metric_density_discrepancy` | The whole Fourier series (103.H11), including \(\nu=0\), is summed before any estimate. **Pass.** |
| `quotient_carrier_cancellation` | Equation (103.H25) confirms the Round-80 cancellation. No quotient sign is claimed as independent. **Pass.** |
| `centred_integral_and_Gaussian_unit` | The proof uses the exact quadratic integral (103.H15) and complete-Fresnel variation, not only its \(e(1/8)\) leading value. **Pass for the core integral.** |
| `profiles_floors_stars_orientations` | The exact profiles, floors, stars, finite lift support, collars and transitions are in (103.H15); fixed conjugate orientations preserve BV. **Pass.** |
| `prior_owner_complements` | Primitivity is automatic, the square owner is empty, the \(\rho\) owner is blockwise constant, exact centres are killed by \(W_R(0)=0\), the collar error is disjoint, and the remaining dyadic cutoff has fixed BV. **Pass.** |
| `empty_and_singleton_fibres` | Zero extension is exact. Empty rows vanish; a singleton \(k\)-row has no (103.H26) term and is bounded by the target-safe diagonal (103.H4). **Pass.** |
| `Pell_25_27_and_near_square` | For \((a,b)=(25,27)\), \(\lambda=26-15\sqrt3\). With \(X=T^4\), \(k=T^2/32\), \(\theta=32(26-15\sqrt3)T^2\) and \(u_*=512(26-15\sqrt3)\in(27/4,25)\). This is primitive, nonsquare and strictly stationary. **Pass as a control, not a lower bound.** |
| `fourth_power_strict_metric_recurrence` | Weyl recurrence gives fixed-width strict annuli and either nearest-integer parity along a suitable arithmetic progression of \(T\). It is not uniform for a shrinking \(R(T)^{-1}\) window and does not align the full \(k\)-row. **No obstruction to (103.H3).** |
| `saddle_entry_exit_and_collars` | The saddle maps the exact endpoints of (103.H6) to \(a\) and \(b/4\); (103.H17) shows every fixed physical collar is at least one stationary width. **Pass for (103.H1).** |
| `actual_lower_bound_gate` | No selected input proves actual nonvanishing, common sign, complement domination or a lower bound for the full \(F_a(1)\). **No counterexample certified.** |
| `arbitrary_coefficient_false_shadow` | On \(R\asymp G\), a false coefficient \(\widetilde B_{a,k}(g)=c_{a,k}(-1)^\ell V\phi(g/G)e(g\eta/2)\) has the Round-77 pointwise and \(g\)-variation scale and makes \(e(-g\theta/2)\widetilde B\) coherent. Choosing \(c_{a,k}\) aligns \(k\). It violates the actual sampled-\(k\) BV (103.H2). **The new mechanism distinguishes the false shadow.** |
| `unsigned_false_shadow` | Since \(q=1\), \((-1)^q=-1\) is constant and supplies no row cancellation. The proof instead uses actual reciprocal curvature plus (103.H2). **Pass.** |
| `energy_and_rho_ledger` | Equations (103.H13) and (103.H24) give the exact \(L,A,J,G,K,\rho\) powers. Squaring \(L^2/A\) over \(A\) rows gives \(L^4/A\). **Pass.** |
| `route_vs_canonical_scope` | Even a proof of (103.H3) closes only the disjoint singleton input. It is not a counterexample to, or proof of, the longer-row canonical Gram. **Pass.** |
| `downstream_and_exponent_scope` | No longer-row Gram, other M2 packet, M9-M2, M9-M1, M9, endpoint uniformity or exponent is inferred. **Pass.** |

No external estimate is required for the proof: the
second-derivative bound in (103.H22) and the complete-Fresnel lemma are
derived internally.  The primary results already identified in the
selected source-audit context were nevertheless checked against the
literal remaining seam:

| Primary source | Literal hypotheses | Verdict for (103.H2)--(103.H3) |
|---|---|---|
| H. Weyl, *Über die Gleichverteilung von Zahlen mod. Eins*, Satz 9 ([primary scan](https://zenodo.org/records/2425535/files/article.pdf)) | A polynomial with an irrational nonconstant coefficient; fixed test interval as the averaging length grows. | Applies only to the fixed-width Pell/fourth-power recurrence control. It gives neither sampled \(k\)-BV nor a fixed-\(X\) actual-symbol energy. |
| H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, Theorem 1 ([primary paper](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)) | Distinct frequencies modulo one with an explicit minimum separation and one common coefficient sequence. | The actual coefficient depends on \((a,k,g)\), and reciprocal points may cluster. It is not the theorem used here. |
| E. Bombieri and H. Iwaniec, *On the order of \(\zeta(1/2+it)\)*, Lemma 2.4 ([primary paper](https://www.numdam.org/article/ASNSP_1986_4_13_3_449_0.pdf)) | Factorised coefficients on two finite point sets, a dot-product phase, coordinate boxes and explicitly paid close-pair energies. | Opening the literal symbol leaves moving fibres, owners and complete physical integrals. The internal sampled-\(k\) proof avoids this mismatch rather than importing the theorem. |
| O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials*, Theorem 2 ([primary paper](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf)) | An unweighted positive four-monomial spacing count in one dyadic interval. | It discards the reciprocal \(k\)-amplitude, metric modes and owners. It neither proves (103.H2) nor supplies the signed row bound. |
| X. Li and X. Yang, *An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem*, Proposition 3.1 and Theorem 4.2 ([primary version](https://arxiv.org/html/2308.14859v2)) | A specific rectangular cone extension or a separably weighted double sum with fixed \(C^3\) phase and displayed derivative/parameter inequalities. | No literal substitution retains the moving owner multiplier and complete entry/exit symbol. Structural analogy is not applicability. |

No theorem from these sources is imported.

## 6. Dependencies and exact artifacts used

The report used exactly the selected Round-103 context and its assigned
brief:

- `protocol.md`;
- `state/proof_obligations.yml`, restricted to the Round-103 targets,
  their direct accepted dependencies, and recorded route obstructions;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/reports/determinant_gram_hostile_source_audit.md`;
- `rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/reviews/conductor_round102_owners_controls_and_sources.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reports/actual_symbol_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reports/strict_metric_energy_hostile_source_audit.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/reports/nonsquare_resonance_hostile_source_audit.md`;
- `strategy/conductor_0817_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/briefs/q1_actual_symbol_hostile_source_audit.md`;
- the conductor's in-task request to audit the sampled-\(k\) closure with
  the complete centred integral, followed by its authorized literal
  Round-80 owner-factor formula for the \(q=1\) row.

No sibling Round-103 report, proof draft, validation matrix, synthesis,
legacy report or unlisted repository artifact was read.  No numerical
experiment was used.  The primary-source map in Section 5 uses only the
literal theorem hypotheses already preserved in the selected source-audit
artifacts; no external theorem was imported.  No shared state was edited.

## 7. Recommended state effect

**Recommended effect: promote the singleton actual-diagonal node after
the conductor's ordinary independent seam check.**

Equations (103.H15)--(103.H24), together with the exhaustive owner audit
in Section 4, prove
`M9-M2-primitive-ray-q1-actual-diagonal-energy` at exactly
\(X^\varepsilon L^4/A\).  The result is an internal actual-symbol theorem,
not a source import, parity trick or repeated transform.  Record (103.H4)
as a separately target-safe reciprocal-diagonal control and (103.H2) as
the property distinguishing the actual symbol from the arbitrary
coefficient shadow.

Record also that Round-80 carrier cancellation is **not** a no-go for
this mechanism: it forbids a formal spectral-gap inference without
actual amplitude control, whereas (103.H1)--(103.H2) provide precisely
the missing complete-integral sampled-\(k\) control.  Conversely, record
no literal lower obstruction from Pell recurrence, a Gaussian plateau,
positive capacity, arbitrary coefficients or the unsigned shadow.

Even after promotion of the singleton node, the longer-row
fixed-\(a\) Gram, the canonical density--discrepancy energy, the two
smooth M2 packets, M9-M2, M9-M1, M9, endpoint uniformity and every
Gauss-circle exponent implication remain open.
