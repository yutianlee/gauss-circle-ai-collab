# Adjacent-\(q\) transport attack and dual-square self-return

Campaign: `m9-m2-polynomial-q-maximal-alternation`
Round: 105
Task: `adjacent_q_transport_attack`
Role: discovery
Starting graph SHA-256: `f8f20833d2f24fa0b323488e247887ba943b8dffdd3eacb58e5bae773eb5831b`

## 1. Result

**No full maximal theorem and no fixed positive-power \(q\)-subrange is
proved.**  Exact adjacent-\(q\) transport does control the motion of the
centered physical saddle, and the primitive mask is benign after an exact
Möbius decomposition.  It does not control the exterior complete metric
phase.  For one orientation, with

\[
 c=\nu-\frac g2,\qquad n=|2\nu-g|,
\]

the product of the centered phase and the metric mode satisfies the exact
carrier identity

\[
 e\!\left(gk(y-r_q)^2+c\frac{\Lambda_q}{k}\right)
 =e\!\left(gky^2-gJ\delta_qy+\nu\frac{\Lambda_q}{k}\right).       \tag{105.A1}
\]

Thus the mandatory density mode \(\nu=0\) is exactly the original
uncentered physical phase.  Its apparent nonzero \((q,k)\)-Hessian after
centering is not an independent oscillation.

More precisely, for \(c=-n/2<0\), the successive formal stationary
transforms in \(k\) and in \(q\) are an exact phase self-return.  Without
the primitive decomposition the dual phase is

\[
 -\frac{Xn\ell}{s}-\frac{sa}{4}+J\sqrt{an\ell}
 =-\left(J\sqrt{\frac{n\ell}{s}}-\frac{\sqrt{as}}2\right)^2,
 \qquad s\ \hbox{positive odd}.                                  \tag{105.A2}
\]

After the literal decomposition
\(\mathbf 1_{(a,q)=1}=\sum_{d\mid(a,q)}\mu(d)\), write \(q=dm\).
Every \(d\mid a\) is odd, so \((-1)^{dm}=(-1)^m\), and the exact dual
phase, with \(s=d-2h\) for the \(m\)-dual integer \(h\), becomes

\[
 \boxed{
 -\frac{dXn\ell}{s}-\frac{as}{4d}+J\sqrt{an\ell}
 =-\left(J\sqrt{\frac{dn\ell}{s}}
          -\frac12\sqrt{\frac{as}{d}}\right)^2 .}                 \tag{105.A3}
\]

Here \(a/d\) and \(s\) are odd, and the residual rational term carries
the exact character

\[
 e\!\left(-\frac{as}{4d}\right)
 =-i\,\chi_4(a/d)\chi_4(s).                                      \tag{105.A3c}
\]

Thus the survivor is an M1-like reciprocal dual row with a literal odd
dual character, not an unweighted two-dimensional Hessian sum.

This is the smallest mode-resolved survivor found: an actual-vector
estimate for the dual square (105.A3), with all transformed owners, lift
fibres, metric modes, collars, and boundary remainders.  It is an
equal-capacity reformulation, not a proved saving.  On a noncollapsing
interior mode box the dual packet has
\(\asymp n^2JD\) points and stationary Jacobian
\(\asymp \sqrt{D/A}/n\).  Multiplying the accepted centered coefficient
scale \(V_D=\sqrt{AL/(JD)}\) gives dual point scale
\(\asymp \sqrt{L/J}/n\); hence its natural \(\ell^2\) capacity is
\(\asymp\sqrt{LD}\), exactly \(\sqrt D\) times the one-row
\(\sqrt L\) capacity.  A new actual-vector projection saving is still
required.

The only unconditional fallback remains

\[
 \mathcal M_a(D)\ll_\varepsilon
 X^\varepsilon D\frac{L^2}{A},                                    \tag{105.A4}
\]

from the accepted fixed-row theorem.  It misses the desired maximal
bound by \(D\) linearly and, after the exact maximal-to-Gram count, misses
the fixed-\(a\) Gram by \(D^2\).  This reproduces rather than improves
the Round-104 ceiling.  The dual self-return is a route obstruction only;
it is not an actual-symbol lower bound.

## 2. Exact statement and hypotheses

Let \(J=\sqrt X\), and work on one literal residual hard-top half-open
block with

\[
 a,b\ \hbox{odd},\qquad b=a+2q,\qquad
 a\asymp b\asymp A,\qquad q\asymp D,\qquad a<b<4a,
\]

\[
 K\asymp\frac{JD}{A},\qquad G\asymp\frac LA,
 \qquad \rho=\frac{AJD^3}{L^3}>1.
\]

Put

\[
 t=\sqrt{\frac{a+2q}{a}},\qquad
 \delta_q=\sqrt{a+2q}-\sqrt a=\sqrt a(t-1),
\]

\[
 \Lambda_q=\frac{X\delta_q^2}{2}
 =\frac{Xa(t-1)^2}{2},qquad
 r_{q,k}=\frac{J\delta_q}{2k}.                                    \tag{105.A5}
\]

The literal reciprocal interval is

\[
 I_{a,q}=(\kappa_-(q),\kappa_+(q))
 =\left(\frac{J\delta_q}{2\sqrt a},
         \frac{J\delta_q}{\sqrt{a+2q}}\right).                   \tag{105.A6}
\]

For a fixed actual odd lift \(g\) and one physical profile piece, write

\[
 \mathfrak B_{a,q,k,g}
 =\int_{\sqrt{a+2q}/2}^{\sqrt a}
 Q_{a,q,g}(y)e\!\left(gk(y-r_{q,k})^2\right)\,dy.                 \tag{105.A7}
\]

The actual row is the zero-extended finite sum over the literal
\(k\)-samples, odd lifts, both orientations, and the complete punctured
metric Fourier series.  In the displayed orientation it contains

\[
 \widehat W_R(\nu)\,
 \mathfrak B_{a,q,k,g}
 e\!\left(\left(\nu-\frac g2\right)\frac{\Lambda_q}{k}\right),   \tag{105.A8}
\]

including \(\nu=0\).  All primitive, square-ray, exact-centre,
positive-safe, residual, dyadic, original-mode, boundary, floor, star,
and finite-support owners remain literal.  The algebraic identities below
are uniform in real \(X\), in Pell and near-square rows, and at exact or
near metric centres.  No assertion of a smooth interpolation of the full
owner product is made.

The maximal target is

\[
 \mathcal M_a(D)=\sup_{I\subset[D,2D)}
 \left|\sum_{q\in I}(-1)^qF_a(q)\right|
 \ll_\varepsilon X^\varepsilon\frac{L^2}{A}.                     \tag{105.A9}
\]

For \(H\asymp D\), (105.A9) would imply the Gram target exactly:
there are \(O(A)\) bases and \(O(D)\) nonempty zero-extended windows,
so

\[
 \mathcal G_H^{\rm act}
 \ll AD\left(X^\varepsilon\frac{L^2}{A}\right)^2
 \ll_\varepsilon X^\varepsilon\frac{DL^4}{A}
 \asymp X^\varepsilon\frac{H^2L^4}{AD}.                          \tag{105.A10}
\]

## 3. Proof or derivation

First, the centered saddle has a clean exact transport.  If
\(E_q(y)=e(gk(y-r_{q,k})^2)\), then

\[
 r'_{q,k}=\frac{J}{2k\sqrt{a+2q}},\qquad
 \partial_qE_q=-r'_{q,k}\partial_yE_q.                           \tag{105.A11}
\]

Let \(\lambda(q)=\sqrt{a+2q}/2\) and \(u=\sqrt a\).  Direct
differentiation of (105.A7), with no discarded endpoint, gives

\[
\begin{aligned}
 \partial_q\mathfrak B_{a,q,k,g}
 &=\int_{\lambda(q)}^u
   (\partial_qQ_{a,q,g}+r'_{q,k}\partial_yQ_{a,q,g})E_q\,dy\\
 &\quad-r'_{q,k}Q_{a,q,g}(u)E_q(u)
 +(r'_{q,k}-\lambda'(q))Q_{a,q,g}(\lambda(q))E_q(\lambda(q)),
\end{aligned}                                                     \tag{105.A12}
\]

where \(\lambda'(q)=1/(2\sqrt{a+2q})\).  The last line vanishes for
a retained profile that vanishes at both collarized endpoints; otherwise
it is the exact boundary term that must be owned.  Equation (105.A12) is
the rigorous adjacent-\(q\) transport identity.  It reduces centered
transport to the material derivative
\(\partial_q+r'_{q,k}\partial_y\), but the accepted context supplies no
uniform material-derivative ledger for every moving owner.

The integer entry/exit geometry itself is exact.  From (105.A6),

\[
 \kappa_-(q)=\frac J2(t-1),\qquad
 \kappa_+(q)=J\left(1-\frac1t\right),
\]

\[
 \kappa_-'(q)=\frac{J}{2at}>0,
 \qquad \kappa_+'(q)=\frac{J}{at^3}>0.                            \tag{105.A13}
\]

Therefore, for every fixed integer \(k\), the set
\(\{q:k\in I_{a,q}\}\) is an interval: that sample has at most one
entry and one exit.  This resolves multiplicity, but not size.  Across
one unit change in \(q\), each endpoint can move by \(\asymp J/A\), so
many integer samples can enter or leave simultaneously; a collar or
actual-symbol estimate is still needed before summing those events.

Primitivity also has an exact favorable decomposition.  Since \(a\) is
odd,

\[
 (a,a+2q)=1\iff(a,q)=1,
 \qquad \mathbf1_{(a,q)=1}=\sum_{d\mid a,\ d\mid q}\mu(d).        \tag{105.A14}
\]

For every integer interval \(I\),

\[
 \left|\sum_{q\in I}(-1)^q\mathbf1_{(a,q)=1}\right|
 \le\sum_{d\mid a}|\mu(d)|
 \le\tau(a)\ll_\varepsilon A^\varepsilon,                       \tag{105.A15}
\]

because every \(d\mid a\) is odd and the inner sum over \(q=dm\) is
an alternating interval sum.  Hence Abel summation would preserve the
target if the remaining complete coefficient had one-row-sized total
\(q\)-variation.  This mask-only fact does **not** survive multiplication
by the moving metric symbol without such a variation theorem.  Nor does
it automatically include the square-ray owner: if \(a=ds_0^2\) and
\(a+2q=dt_0^2\) with \(d,s_0,t_0\) odd, then
\(q=d(t_0^2-s_0^2)/2\) is even, so the deleted square locations have
constant sign and can have \(\asymp\sqrt{A/d}\) members in a long fixed-
\(a\) interval.

The obstruction appears when the complete metric mode is restored.
Multiplying the phases in (105.A7)--(105.A8) proves (105.A1), since

\[
 gk(y-r_{q,k})^2
 =gky^2-gJ\delta_qy+\frac{g\Lambda_q}{2k}.           \tag{105.A16}
\]

Equivalently, differentiating the exterior factor creates
\(c\Lambda_q'/k\), where

\[
 \Lambda_q'=X\left(1-\frac1t\right),\qquad
 \Lambda_q''=\frac{X}{at^3},qquad
 \frac{|c|\Lambda_q'}{k}\asymp nJ.                              \tag{105.A17}
\]

Thus (105.A11) does not turn the complete mode into a small-total-
variation amplitude.  In the density mode the same carrier instead
cancels exactly as in (105.A1), returning to the physical phase.  This is
why neither an absolute derivative estimate nor deletion of density is
valid.

For completeness, the apparent centered Hessian is genuinely nonzero.
For

\[
 \Psi(q,k)=\frac q2+c\frac{\Lambda_q}{k},
\]

one has

\[
 \det D^2_{q,k}\Psi
 =\frac{c^2}{k^4}\bigl(2\Lambda_q\Lambda_q''-(\Lambda_q')^2\bigr)
 =-\frac{c^2X^2(t-1)^3}{t^3k^4}
 \asymp-\frac{n^2A}{D}.                                           \tag{105.A18}
\]

Nonvanishing does not yield a discrete saving.  To see the exact return,
take \(c=-n/2\).  A \(k\)-stationary dual integer \(\ell\) satisfies

\[
 \ell=\frac{n\Lambda_q}{2k^2},\qquad
 k_* =\sqrt{\frac{n\Lambda_q}{2\ell}},\qquad
 \frac{nb}{4}<\ell<na,                                           \tag{105.A19}
\]

and the transformed phase is

\[
 \frac q2-J\delta_q\sqrt{n\ell}.                                \tag{105.A20}
\]

Apply the primitive decomposition first and put \(q=dm\).  Keep the
literal linear phase \(dm/2\), and let \(h\in\mathbb Z\) be the
\(m\)-dual integer.  Set \(s=d-2h\), which is odd because \(d\) is
odd.  (Replacing \(dm/2\) by \(m/2\) only relabels
\(h\) by the integer \((d-1)/2\).)  The \(m\)-stationary equation is

\[
 \frac d2-\frac{dJ\sqrt{n\ell}}{\sqrt b}=h,
 \qquad s>0\ \hbox{odd},qquad
 b_* =\frac{4d^2Xn\ell}{s^2}.                                    \tag{105.A21}
\]

Substitution, with \(m_*=(b_*-a)/(2d)\), gives exactly

\[
\begin{aligned}
 &\left(\frac d2-h\right)m_*
   -J(\sqrt{b_*}-\sqrt a)\sqrt{n\ell}\\
 &\qquad=-\frac{dXn\ell}{s}-\frac{as}{4d}+J\sqrt{an\ell}
 =-\left(J\sqrt{\frac{dn\ell}{s}}
          -\frac12\sqrt{\frac{as}{d}}\right)^2,
\end{aligned}                                                     \tag{105.A22}
\]

Since \(a/d\) and \(s\) are odd, the non-square part of (105.A22)
has the exact factor

\[
 e\!\left(-\frac{as}{4d}\right)
 =-i\chi_4(a/d)\chi_4(s).                                        \tag{105.A22c}
\]

The dual survivor therefore has the original Möbius coefficient and a
literal \(\chi_4\)-weighted reciprocal row in \((\ell,s)\).  Treating
it as a coefficient-blind Hessian sum discards the only new arithmetic
structure exposed by the transform.  This proves (105.A3).  The opposite
sign of \(c\) and the conjugate orientation give the corresponding
reflected dual lattice; no zero-frequency deletion results.

On an interior box, (105.A19) has \(\asymp nA\) values and (105.A21)
has \(\asymp nJD/A\) odd values of \(s\) per \(\ell\), hence
\(\asymp n^2JD\) dual points.  From (105.A18), the stationary Jacobian
is \(\asymp\sqrt{D/A}/n\).  The scale calculation in Section 1 follows.
At the cone edge both the primal \(k\)-interval and the \(\ell\)-interval
collapse, so this count decreases; a uniform stationary expansion through
that transition is nevertheless not supplied by the accepted fixed-row
theorem.

Finally, (105.A4) follows simply from
\(|F_a(q)|\ll X^\varepsilon L^2/A\).  Inserting it into (105.A10)
multiplies the right side by \(D^2\).  No fixed \(D=X^\theta\),
\(\theta>0\), can be absorbed into \(X^\varepsilon\) for every
\(\varepsilon>0\).

## 4. First doubtful or unproved step

The first missing literal input is **not** the phase algebra.  Equations
(105.A11)--(105.A15) and (105.A18)--(105.A22) are exact.  The first
unproved step is a one-row-sized \(q\)-transport theorem for the whole
actual amplitude after zero extension:

\[
 \sup_q|\mathcal A(q)|+\operatorname{Var}_q\mathcal A(q)
 \stackrel{?}{\ll}_\varepsilon X^\varepsilon\,(\hbox{one-row scale}),
                                                                    \tag{105.A23}
\]

where \(\mathcal A\) must include the material derivative in (105.A12),
all integer entry/exit samples, the changing finite odd-lift fibre, the
square and prior owners, floors, stars, both physical collars, and the
complete metric Fourier sum.  The accepted Round-104 theorem gives
sampled variation in \(k\) at fixed \(q\); it does not give (105.A23).
Round 77 gives variation in \(g\), not in \(q\).

Even a proof of centered material variation alone would not suffice:
the exact exterior term in (105.A17) remains, while moving it inside
returns the density mode to the original physical/transposed character
row by (105.A1).  Applying two B-processes would additionally require a
literal smooth interpolation, uniform stationary remainders at all
integer and collar transitions, and exact transport of every owner to the
dual \((\ell,s)\)-lattice.  None of those amplitude and remainder claims
is established here.  Consequently (105.A22) is an exact phase reduction
and equal-capacity obstruction, not a completed Poisson estimate.

The first possible new theorem is therefore the actual-vector dual-square
estimate

\[
 \sum_{d\mid a}\mu(d)
 \sum_{g,\nu,\ell,s}
 \widetilde{\mathcal A}_{a,d,g,\nu,I}(\ell,s)
 e\!\left(-\left(J\sqrt{\frac{dn\ell}{s}}
       -\frac12\sqrt{\frac{as}{d}}\right)^2\right)
 \ll_\varepsilon X^\varepsilon\frac{L^2}{A},                     \tag{105.A24}
\]

with the complete Fourier series, both orientations, every owner, and all
transform remainders retained.  It needs a \(D^{-1/2}\) gain beyond the
natural dual \(\ell^2\) packet capacity at the mode level.  No such
fixed-vector projection or signed correlation is proved.

## 5. Required control tests and outcomes

- **`maximal_to_Gram_implication` -- passed.**  Equation (105.A10) uses
  exactly \(O(AD)\) nonempty windows for \(H\asymp D\) and reaches
  \(H^2L^4/(AD)\) if (105.A9) holds.
- **`adjacent_q_transport_identity` -- passed algebraically.**
  Equations (105.A11)--(105.A12) include both moving-boundary terms.
  No endpoint is silently dropped.
- **`total_q_variation_vs_maximal_alternation` -- reduction passed,
  estimate open.**  Scalar Abel gives maximal alternation from supremum
  plus total variation, but (105.A17) prevents deriving that variation
  from centered transport alone.
- **`primitive_Mobius_or_residue_decomposition` -- passed.**
  Equations (105.A14)--(105.A15) give the exact decomposition and the
  \(O(\tau(a))\) mask-only interval bound.  Equation (105.A22) retains
  the divisor \(d\) in the dual phase.
- **`moving_k_interval_and_integer_entry_exit` -- passed for
  multiplicity, estimate open.**  Both endpoints are monotone by
  (105.A13), hence each integer \(k\) enters and exits at most once.
  Simultaneous \(\asymp J/A\) endpoint motion and collar size still need
  an actual amplitude estimate.
- **`finite_odd_lift_transport` -- open.**  Zero extension is exact, but
  no supplied formula proves one-row total variation of all moving lift
  endpoints, floors, and lift owners in \(q\).
- **`complete_metric_density_discrepancy` -- passed as an obstruction.**
  Identity (105.A1) retains every \(\nu\).  For \(\nu=0\) it returns
  exactly to the physical density row; density cannot be deleted or
  estimated independently of discrepancy at an exact centre.
- **`physical_collars_and_cone_edge` -- phase geometry passed,
  transform theorem open.**  The reciprocal and dual intervals collapse
  together as \(b/a\to4^-\).  No denominator in the exact identities
  blows up, but no new uniform two-variable stationary remainder through
  overlapping collars is claimed.
- **`Pell_near_square_square_fourth_power` -- passed as method
  controls.**  All identities are algebraic and use no irrationality or
  Diophantine gap.  Square rays remain with their prior owner; Pell,
  near-square, and fourth-power coherent specializations are not excluded.
  They provide no lower bound for the complete actual maximal sum.
- **`exact_and_near_metric_centers` -- passed.**  At an exact centre the
  punctured window vanishes only after all Fourier modes are recombined.
  The density term in (105.A1) remains present modewise, and the dual
  square can be integral or near-integral without contradiction.
- **`coherent_alternating_coefficient_false_shadow` -- rejected, as
  required.**  Taking a phase-conjugated coefficient with
  \(F(q)=(-1)^qL^2/A\) makes the maximal sum \(D L^2/A\).  Such a
  sequence violates the actual material-derivative, collar, and owner
  structure; it disproves only a coefficient-uniform theorem.
- **`actual_symbol_lower_obstruction_gate` -- passed.**  No lower bound
  for the literal actual sum is asserted.  The dual-square return is
  equal-capacity and identifies a missing projection estimate only.
- **`dyadic_polynomial_endpoints` -- failed for a polynomial theorem.**
  The fallback loses \(D\) linearly and \(D^2\) in the Gram.  Prescribed
  polylogarithmic/\(X^{o(1)}\) shells remain those already owned by Round
  104; no fixed \(D\le X^\theta\) range is new.
- **`transform_self_return` -- passed.**  The Hessian determinant
  (105.A18) is nonzero, but the two stationary transforms give the exact
  centered square (105.A22), with the alternation recorded by odd \(s\).
- **`primary_source_hypothesis_map` -- passed by nonuse.**  No external
  theorem or web source is invoked; in particular no generic
  two-dimensional Hessian theorem is misapplied to the jagged moving
  actual symbol.
- **`downstream_and_exponent_scope` -- passed.**  Nothing here proves the
  polynomial fixed-\(a\) Gram, canonical density-discrepancy energy, hard
  signed cone, another M2 packet, M9-M2, M9-M1, endpoint uniformity, M9,
  the quarter target, or a new exponent.

No numerical experiment and no external source were used.

## 6. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/derivation_packet.md`
- `rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/briefs/adjacent_q_transport_attack.md`
- `rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/synthesis.md`
- `rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/reports/fixed_q_sampled_k_attack.md`
- `rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/synthesis.md`
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/synthesis.md`
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/synthesis.md`
- Live Round-105 conductor messages supplying the candidate Hessian and
  successive stationary-transform formulas, independently checked in
  (105.A18)--(105.A22).

No sibling Round-105 report, proof draft, validation matrix, shared
synthesis, computational artifact, or external source was read or used.

## 7. Recommended state effect

**Retain the polynomial maximal theorem and
`M9-M2-primitive-ray-fixed-a-actual-Gram` as open.**  Do not promote a
fixed positive-power \(q\)-subrange.  The prescribed polylogarithmic
survivor is already owned by Round 104 and is not a new result of this
round.

**Promote only after seam review** the scoped algebraic transport packet:

1. the exact material-derivative identity (105.A12), including boundary
   terms;
2. monotone reciprocal endpoints and at-most-one integer entry/exit;
3. the exact primitive alternating interval bound (105.A15); and
4. the Möbius-resolved dual-square self-return (105.A22), recorded as a
   route obstruction rather than an estimate.

Retain (105.A24) as the strictly smaller, mode-resolved actual-vector
survivor.  Its proof must keep the whole metric Fourier series and both
orientations coupled, transport every owner and lift fibre, give uniform
collar and integer-transition remainders, and obtain a genuine
\(D^{-1/2}\) projection saving beyond equal-capacity transform/Plancherel.
The available absolute fallback has exact deficits \(D\) in the maximal
sum and \(D^2\) in the Gram.  Do not infer the canonical M2 energy,
M9-M2, M9, endpoint uniformity, the quarter target, or any exponent.
