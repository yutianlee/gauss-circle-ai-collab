# Round 102 discovery report: determinant-weighted actual Gram

## 1. Result

The literal fixed-\(a\) Gram has an exact carrier normal form, but the
off-shift determinant mechanism does not by itself prove the required
\(\rho^{-1/2}\) linear gain.  The result is a sharp scoped no-go with
two exact reductions.

First, if \(b_q=a+2q\), then completing the physical square without a
stationary-phase approximation gives the off-shift carrier phase

\[
 \Phi_s(q;g,k,g',k')
 =\frac{g'}{2k'}\Lambda_{q+s}
  -\frac g{2k}\Lambda_q,\qquad
 \Lambda_q=\frac X2(\sqrt{b_q}-\sqrt a)^2,
\]

and

\[
 \Phi_s''(q)=\frac{X\sqrt a}{2}\Delta_0,\qquad
 \Delta_0=\frac{g'}{k'b_{q+s}^{3/2}}
              -\frac g{kb_q^{3/2}}.
\]

This is the exact physical-carrier determinant stated in the campaign.
However, after the mandatory joint metric expansion, the total phase has
\(\nu=g-2\ell\) and \(\nu'=g'-2\ell'\), and its determinant is

\[
 \Delta_{\ell,\ell'}
 =\frac{\nu'}{k'b_{q+s}^{3/2}}
  -\frac{\nu}{kb_q^{3/2}}.
\]

Thus a split using only \(\Delta_0\) is a split of the density-density
carrier, or else a split in which the rapidly moving complete metric
factor remains inside the amplitude.  It is not a complete phase split
for the coupled density-discrepancy symbol.

Second, the bottom dyadic primitive block \(q=1\),
\(D_{\rm ray}=1\), has only \(H=1\).  Hence its Gram is exactly its
actual diagonal and has no off-shift determinant locus at all.  The hard
ratio may nevertheless tend to infinity on the accepted primitive
near-square/Pell rows.  Consequently any uniform determinant proof must
first prove the separate complete-symbol diagonal estimate

\[
 \boxed{
 \mathcal D_1^{\rm act}:=\sum_a|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon\frac{E_0}{\rho}
 \asymp_{X^\varepsilon}
 X^\varepsilon\frac{L^4}{A}. }
\]

This is the smallest strict survivor.  It retains the entire actual
symbol inside \(F_a(1)\); it is not an arbitrary-coefficient claim.  No
full Gram bound, target-safe hard subrange, downstream M2 statement, or
exponent is proved here.

## 2. Exact statement and hypotheses

Fix one residual hard top-M2 block and put \(J=\sqrt X\),
\(b_q=a+2q\), \(\delta_q=\sqrt{b_q}-\sqrt a\), and
\(\Lambda_q=X\delta_q^2/2\).  The reciprocal support is kept
literally as

\[
 I_{a,q}=\left(\frac{J\delta_q}{2\sqrt a},
                    \frac{J\delta_q}{\sqrt{b_q}}\right).
\]

Let \(\alpha_{a,q,g,k}\) denote, without alteration, the residual
mask, primitive mask, every prior-owner complement, both orientations,
profiles, floors, stars, signs, finite odd-lift restriction, and zero
extension.  The complete physical entry/exit integral is

\[
 \mathfrak C^\circ_{a,b_q,k}(g)
 =g\int_{b_q/4}^{a} A^\circ_{ga,gb_q}(gu)
 e\bigl(g[ku-J\delta_q\sqrt u]\bigr)\,du.
\]

With the exact moving interval and coupled metric factor, define

\[
 F_a(q)=\sum_{\substack{g\ {\rm odd}\\ k\in I_{a,q}}}
 \alpha_{a,q,g,k}
 W_R\left(\frac{\Lambda_q}{k}\right)
 \mathfrak C^\circ_{a,b_q,k}(g),
\]

and extend it by zero outside the literal block.  No smoothness in
\(q\) is assumed for \(\alpha\) or for the complete integral.  For
\(1\le H\le D_{\rm ray}\), set

\[
 \mathcal G_H^{\rm act}
 =\sum_{a,n}\left|\sum_{0\le r<H}(-1)^rF_a(n+r)\right|^2.
\]

The exact conclusions proved below are:

- the Fejer-Gram expansion and the carrier and mode-resolved
  determinants above;
- for a nonzero shift \(s\), exact determinant zero can occur only when
  \(b_q\) and \(b_{q+s}\) have the same squarefree kernel, and the
  possible base pairs for fixed \(s\) are divisor-sparse;
- away from exact zero there is an explicit algebraic spacing bound,
  but its worst-scale curvature is too small to imply oscillation;
- the \(q=1\) actual diagonal is logically untouched by every off-shift
  determinant estimate.

The scale ledger retained throughout is

\[
 E_0\asymp_{X^\varepsilon}LJD_{\rm ray}^2,\qquad
 \rho=\frac{AJD_{\rm ray}^3}{L^3}>1,\qquad
 \frac{H^2E_0}{\rho}
 \asymp_{X^\varepsilon}\frac{H^2L^4}{AD_{\rm ray}}.
\]

## 3. Proof or derivation

Expanding the square first and only then changing variables gives the
exact identity

\[
 \mathcal G_H^{\rm act}
 =H\sum_{a,q}|F_a(q)|^2
 +2\Re\sum_{1\le s<H}(-1)^s(H-s)
   \sum_{a,q}F_a(q)\overline{F_a(q+s)}.
 \tag{3.1}
\]

The factor \((-1)^s\) is constant in \(q\).  Every support entry
and exit is already exact in (3.1), because a missing term is zero rather
than a boundary error.

The physical phase has the exact square identity

\[
 ku-J\delta_q\sqrt u
 =k\left(\sqrt u-\frac{J\delta_q}{2k}\right)^2
  -\frac{\Lambda_q}{2k}.
\]

Therefore

\[
 \mathfrak C^\circ_{a,b_q,k}(g)
 =e\left(-\frac{g\Lambda_q}{2k}\right)
 \mathfrak B^\circ_{a,q,k}(g),
\]

where \(\mathfrak B^\circ\) is the same complete integral with
the centred square phase.  This is an identity through saddle entry and
exit, not an asymptotic replacement.  A term in the \(s\)-correlation
then carries \(e(\Phi_s)\), where \(\Phi_s\) is the phase in
Section 1.  Since

\[
 \Lambda_q=X\bigl(a+q-\sqrt{a(a+2q)}\bigr),\quad
 \Lambda_q'=X\left(1-\sqrt{\frac a{b_q}}\right),\quad
 \Lambda_q''=\frac{X\sqrt a}{b_q^{3/2}},\quad
 \Lambda_q'''=-\frac{3X\sqrt a}{b_q^{5/2}},
\]

differentiation proves the stated \(\Delta_0\) formula exactly.

Now expand the same retained metric window, rather than deleting its
mean or its discrepancies:

\[
 W_R(t)=\sum_{\ell\in\mathbb Z}\widehat W_R(\ell)e(\ell t).
\]

The product of the two metric factors changes the carrier phase to

\[
 \Phi_{s,\ell,\ell'}(q)
 =\frac{g'-2\ell'}{2k'}\Lambda_{q+s}
  -\frac{g-2\ell}{2k}\Lambda_q.
 \tag{3.2}
\]

Because \(g,g'\) are odd, \(\nu=g-2\ell\) and
\(\nu'=g'-2\ell'\) are nonzero odd integers.  Twice
differentiating (3.2) proves the total determinant
\(\Delta_{\ell,\ell'}\).  In particular, the density-density
piece is \(\ell=\ell'=0\), but the complete coefficient contains all
four density/discrepancy pairings.  Keeping \(W_R\) unexpanded is
algebraically legitimate, but then it and the centred integrals remain
part of a moving \(q\)-amplitude; no accepted bounded-variation theorem
applies to that amplitude.

The exact-zero incidence is elementary.  Put \(b=b_q\) and
\(b'=b_{q+s}\).  A mode-resolved determinant can vanish only for
\(\nu\) and \(\nu'\) of the same sign, and then

\[
 \nu' k b^{3/2}=\nu k'b'^{3/2}.
 \tag{3.3}
\]

Squaring (3.3) and comparing every prime valuation modulo two shows that
\(b\) and \(b'\) have the same squarefree kernel.  Thus
\(b=cu^2\), \(b'=cv^2\) with \(c\) squarefree, and (3.3) is
equivalent to

\[
 \nu'ku^3=\nu k'v^3,\qquad
 c(v-u)(v+u)=b'-b=2s.
 \tag{3.4}
\]

For fixed \(s\), the second equation in (3.4) gives at most
\(d_3(2s)\) possible triples \(c,v-u,v+u\), before parity,
primitive, owner, interval, and symbol restrictions.  Hence those masks
can only reduce the exact-zero base incidence.

If the two signs agree but (3.3) fails, then

\[
 N=(\nu'k)^2b^3-(\nu k')^2b'^3
 \in\mathbb Z\setminus\{0\}.
\]

Factoring this difference of squares gives the rigorous spacing bound

\[
 |\Delta_{\ell,\ell'}|\ge
 \frac{1}{kk'b^{3/2}b'^{3/2}
 (|\nu'|kb^{3/2}+|\nu|k'b'^{3/2})}.
 \tag{3.5}
\]

On \(b,b'\asymp A\), \(k,k'\asymp K\), and
\(|\nu|,|\nu'|\le V\), this is only
\(\gg(VK^3A^{9/2})^{-1}\).  For the density modes
\(V\asymp G=L/A\) and \(K\asymp JD_{\rm ray}/A\), the
guaranteed carrier curvature from (3.5) is merely

\[
 |\Phi_s''|\gg
 \frac{J^2}{GK^3A^4}
 \asymp\frac1{LJD_{\rm ray}^3},\qquad
 D_{\rm ray}^2|\Phi_s''|\gg
 \frac1{LJD_{\rm ray}}.
 \tag{3.6}
\]

Thus mere algebraic nonvanishing does not force even one oscillation
across the \(q\)-interval.  On the density-density locus a complementary
raw near-incidence bound is also exact: for fixed \(q,s,g,k,k'\),
\(|\Delta_0|\le\tau\) confines \(g'\) to an interval of
length \(\ll\tau KA^{3/2}\).  Consequently

\[
 \#\{(g,k,g',k'):|\Delta_0|\le\tau\\}
 \ll GK^2\min\bigl(G,1+\tau KA^{3/2}\bigr)
 \tag{3.7}
\]

per \((q,s)\).  Formula (3.7) is a raw count, not a bound for the
complete coefficient-weighted correlation.  After (3.2), a single
\(\nu'\) has many \((g',\ell')\) representations carrying
\(\widehat W_R(\ell')\), so the required object is a weighted
incidence, not (3.7).

Finally take the exact bottom block \(q=1\).  Since \(a\) is odd,
\((a,a+2)=1\), and
\(a(a+2)=(a+1)^2-1\), so this is the primitive nonsquare
near-square control.  The accepted hard cone contains such rows,
including Pell subfamilies, with \(D_{\rm ray}=1\) and unbounded
\(\rho\).  The only lawful choice is \(H=1\), and (3.1) becomes

\[
 \mathcal G_1^{\rm act}=\sum_a|F_a(1)|^2=\mathcal D_1^{\rm act}.
\]

Here \(E_0\asymp_{X^\varepsilon}LJ\) and
\(\rho=AJ/L^3\), so the frozen target is exactly the boxed
\(L^4/A\) diagonal survivor.  There is no separated locus, no near
off-shift locus, and no character autocorrelation on which the proposed
determinant mechanism could act.

## 4. First doubtful or unproved step

The first unproved step is not the elementary determinant algebra.  It
is a \(q\)-variation or coefficient-weighted oscillatory estimate for
the literal product of the two centred entry/exit integrals, primitive
and prior-owner masks, moving \(k,g\) supports, and coupled metric
coefficients.  Round 77 supplies step-two variation in the lift
variable \(g\), not bounded variation in \(q\).  The primitive mask
alone can jump on every unit shift, the reciprocal interval has literal
entry and exit crossings, and

\[
 \frac d{dq}W_R(\Lambda_q/k)
 =W_R'(\Lambda_q/k)\frac{\Lambda_q'}k
\]

retains the rapid metric motion.  Treating these factors as a harmless
smooth amplitude in a second-derivative test is therefore unjustified.
Expanding them avoids that false step but replaces \(\Delta_0\) by
the mode-resolved determinant (3.2).

After the \(q=1\) diagonal is separately owned, the next exact survivor
on \(D_{\rm ray}\ge2\) is the signed, mode-resolved near tube

\[
 \begin{aligned}
 \mathcal N_{H,\tau}^{\rm act}
 =2\Re\sum_{1\le s<H}(-1)^s(H-s)
 \sum_{\substack{a,q,g,k,g',k',\ell,\ell'\\
 |\Delta_{\ell,\ell'}|\le\tau}}
 &\widehat W_R(\ell)
 \overline{\widehat W_R(\ell')}
 \mathcal A^\circ_{a,q,s;g,k,g',k'}\\
 &\times e\bigl(\Phi_{s,\ell,\ell'}(q)\bigr),
 \end{aligned}
\]

where \(\mathcal A^\circ\) is the full centred actual-symbol
product with every mask and entry/exit factor.  Neither the sparse exact
zero classification nor the raw bound (3.7) controls this weighted
quantity.  A valid successor must prove the short-ray diagonal estimate
and then control this tube jointly with its separated complement; it
must not take absolute values across the \(s,\ell,\ell'\)
interactions without an explicit power ledger.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Literal fixed-\(a\) row and complete actual symbol | Passed.  All primitive and prior-owner masks, profiles, floors, stars, orientations, signs, collars, finite odd lifts, and physical entry/exit integrals remain in \(\alpha\mathfrak C^\circ\) or \(\mathcal A^\circ\). |
| Moving \(k,g\) fibres and support crossings | Passed.  The exact open interval \(I_{a,q}\) is used on both rows; zero extension makes every entry and exit exact.  No overlap of two moving intervals is assumed. |
| Metric density-discrepancy jointness | Passed.  The density determinant \(\Delta_0\) and the full determinants \(\Delta_{\ell,\ell'}\) are distinguished.  The mean and all nonzero modes remain in the same correlation. |
| Exact Gram and diagonal | Passed.  Identity (3.1) fixes the sign, Fejer multiplicity, diagonal, and both conjugate orientations before any absolute value. |
| Separated determinant locus | Passed as an algebraic split, not as an estimate.  Equations (3.5)-(3.6) show that nonzero algebraic spacing alone is below the oscillatory scale, and the missing actual \(q\)-variation is stated explicitly. |
| Near determinant and exact resonance | Passed.  Equations (3.3)-(3.4) classify exact zero; (3.7) gives the elementary density-mode raw incidence.  The coefficient-weighted mode tube is retained as open. |
| \(D_{\rm ray}=1\), \(q=1\), Pell, and near-square | Failed for the proposed mechanism in the precise route sense: the nonzero-shift set is empty while \(\rho\) may be unbounded.  No lower bound for the actual coefficient is inferred. |
| Fourth-power recurrence | Passed as a method control only.  Coherent square/fourth-power examples can defeat variation-as-cancellation, while square rays are prior-owned where the literal mask says so; they supply no residual lower bound here. |
| Arbitrary-coefficient and unsigned false shadows | Passed.  A phase-aligned or nonnegative row supported only at \(q=1\) has \(\mathcal G_1=E_0\), contradicting a uniform \(E_0/\rho\) conclusion as \(\rho\to\infty\).  This rejects coefficient-blind reasoning but is not asserted to be the actual symbol. |
| Transform self-return | Passed.  The metric-mode expansion exposes the same half-frequency carrier and does not create a deleted zero mode or a new unitary saving.  No parity-aware Poisson or reciprocal completion is reused as a gain. |
| \(\rho\)-power ledger | Passed.  The energy target is \(H^2L^4/(AD_{\rm ray})\); at \(D_{\rm ray}=H=1\) it is \(L^4/A=E_0/\rho\), exactly the missing \(\rho^{-1/2}\) linear gain. |
| Downstream and exponent scope | Passed.  No density-discrepancy energy, signed cone, smooth packet, all-denominator endpoint, M9-M2, M9-M1, M9, or exponent is inferred. |

## 6. Dependencies and exact artifacts used

The mathematical dependencies used are the accepted exact top-M2 row
and entry/exit normal form, the complete-symbol carrier cancellation and
density/discrepancy recoupling, the primitive fixed-\(a\) Gram
normalization and short-ray obstruction, and the canonical
\(E_0,\rho\) ledger.  The exact artifacts read and used were:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/synthesis.md`;
- `rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/reviews/conductor_round96_adjudication.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/synthesis.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/synthesis.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md`;
- `rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/briefs/determinant_weighted_gram_attack.md`.

No external theorem, web source, unlisted historical derivation, or
numerical computation is used.  The exact-zero classification, spacing
bound, raw incidence estimate, and short-ray reduction are proved in
this report.

## 7. Recommended state effect

**Revise**, without promoting the open Gram target.  Record the exact
carrier and mode-resolved determinants, the divisor-sparse exact-zero
classification, and the scoped no-go: off-shift determinant separation
cannot be a uniform mechanism until the disjoint \(q=1\) actual diagonal
is proved independently.  Replace the single next action by the ordered
pair of strict survivors

\[
 \mathcal D_1^{\rm act}\ll_\varepsilon
 X^\varepsilon E_0/\rho
 \quad\text{and then}\quad
 \mathcal N_{H,\tau}^{\rm act}
 \text{ jointly with its separated complement on }D_{\rm ray}\ge2.
\]

Retain `M9-M2-primitive-ray-fixed-a-actual-Gram` and every downstream
obligation as open.  Reject any claim that \(\Delta_0\) alone is the
complete density-discrepancy determinant, that algebraic nonvanishing
supplies useful curvature, or that the determinant split covers the
short-ray block.

### Conductor-authorized seam audit

The claimant-side cubic identity is exact.  Fix \(s>0\), write
\(b=b_q\), \(b_s=b_{q+s}=b+2s\), and suppose a density-carrier zero
occurs:

\[
 \Delta_0=0,\qquad
 c:=\frac{g}{kb^{3/2}}
   =\frac{g'}{k'b_s^{3/2}}>0.
\]

From the exact third derivative in Section 3,

\[
 \begin{aligned}
 \Phi_s'''(q)
 &=\frac{3X\sqrt a}{2}
 \left(\frac{g}{kb^{5/2}}
       -\frac{g'}{k'b_s^{5/2}}\right)\\
 &=\frac{3X\sqrt a}{2}c
   \left(\frac1b-\frac1{b_s}\right).
 \end{aligned}
 \tag{7.1}
\]

In particular, the absolute-value identity requested at the seam holds
(and the displayed quantity is positive because \(s>0\)).  The scale
comparison

\[
 |\Phi_s'''(q)|
 \asymp \frac{JL s}{D_{\rm ray}A^3}
 \tag{7.2}
\]

requires all of the following hypotheses: \(a\asymp b\asymp
b_s\asymp A\); both shifted rows remain in the same fixed block;
\(g,g'\asymp G\) and \(k,k'\asymp K\) with positive variables;
\(G\asymp L/A\), \(K\asymp JD_{\rm ray}/A\); and
\(1\le s<H\le D_{\rm ray}\ll A\).  Indeed,

\[
 c\asymp\frac{G}{KA^{3/2}}
 \asymp\frac{L}{JD_{\rm ray}A^{3/2}},\qquad
 \frac1b-\frac1{b_s}
 =\frac{2s}{bb_s}\asymp\frac{s}{A^2},
\]

and \(X\sqrt a\asymp J^2A^{1/2}\), proving (7.2).  On a
\(q\)-interval of length \(D_{\rm ray}\), its dimensionless cubic scale
is

\[
 D_{\rm ray}^3|\Phi_s'''|
 \asymp \frac{JL sD_{\rm ray}^2}{A^3}
 =\rho\left(\frac LA\right)^4\frac{s}{D_{\rm ray}}
 \asymp \rho G^4\frac{s}{D_{\rm ray}}.
 \tag{7.3}
\]

Equation (7.3) is not a lawful gain for the complete Gram.  Equality
\(\Delta_0=0\) occurs only at the divisor-sparse base points classified
in (3.4), whereas a third-derivative estimate needs a controlled phase
and amplitude on an interval around such a point.  More decisively, the
complete multiplier changes the determinant at this density zero to

\[
 \Delta_{\ell,\ell'}
 =2\left(\frac{\ell}{kb^{3/2}}
         -\frac{\ell'}{k'b_s^{3/2}}\right),
 \tag{7.4}
\]

which is not generally zero.  The centred entry/exit symbols, primitive
and owner masks, and moving supports still have no accepted
\(q\)-variation bound.  Thus (7.1)-(7.3) may diagnose the isolated
density-density cubic transition, but they neither estimate the joint
mode-resolved multiplier nor bypass the \(q=1\) diagonal survivor.

There is, however, a sharper raw density near-count than (3.7).  Under
the same dyadic comparabilities, put

\[
 \alpha=\left(\frac{b_s}{b}\right)^{3/2},\qquad
 \left|\frac{g'}{k'}-\alpha\frac gk\right|
 \le \eta\frac GK.
 \tag{7.5}
\]

Equivalently, a determinant window \(|\Delta_0|\le\tau\) has this
normalization with

\[
 \eta\asymp \frac{\tau A^{3/2}K}{G}.
\]

Let \(u=g'k\) and \(v=gk'\).  Condition (7.5) implies
\(|u-\alpha v|\ll\eta GK\).  There are \(O(GK)\) possible integers
\(v\), at most \(O(1+\eta GK)\) possible integers \(u\) for each
\(v\), and each product has at most \(d(u),d(v)\ll_\varepsilon
X^\varepsilon\) representations in the prescribed dyadic rectangles.
After renaming \(\varepsilon\),

\[
 \#\{(g,k,g',k'):\text{(7.5) holds}\}
 \ll_\varepsilon X^\varepsilon
 \left(\eta(GK)^2+GK\right).
 \tag{7.6}
\]

Oddness, exact moving intervals, primitive masks, and prior-owner masks
only decrease this raw count.  Estimate (7.6) supersedes the baseline
term in (3.7), but it still counts density variables without the actual
weights.  For the complete mode-resolved multiplier, the effective
integers are \(g-2\ell\) and \(g'-2\ell'\), with Fourier-weighted
multiple representations; (7.6) therefore supplies no complete-symbol
\(\rho^{-1/2}\) gain or target-safe subrange by itself.  The recommended
state effect remains **revise**, with all downstream obligations open.
