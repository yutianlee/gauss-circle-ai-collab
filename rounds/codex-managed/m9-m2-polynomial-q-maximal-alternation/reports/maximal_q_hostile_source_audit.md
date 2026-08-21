# Round 105 hostile/source audit: maximal polynomial-\(q\) alternation

Campaign: m9-m2-polynomial-q-maximal-alternation

Task: maximal_q_hostile_source_audit

Role: hostile mathematical and source auditor

Status: candidate evidence only; no shared proof state is edited.

## 1. Result

**The maximal actual theorem is neither proved nor refuted.  The proposed
adjacent-\(q\) transport identity does not control the complete mode, and
the nonzero two-variable Hessian gives a carrier self-return rather than an
automatic gain.**  No literal actual-symbol lower obstruction was found.

Let

\[
 \mathcal M_a(D)=\sup_{I\subset[D,2D)}
 \left|\sum_{q\in I}(-1)^qF_a(q)\right|,
 \qquad M_0=X^\varepsilon {L^2\over A}.
\]

If \(\mathcal M_a(D)\ll M_0\), then for \(H\asymp D\) there are
\(O(D)\) zero-extended windows for each of \(O(A)\) bases, and hence

\[
 \mathcal G_H^{\rm act}\ll AD M_0^2
 \ll_\varepsilon X^\varepsilon {DL^4\over A}
 \asymp X^\varepsilon {H^2L^4\over AD}.             \tag{105.H1}
\]

Thus the frozen maximal theorem has exactly the advertised Gram
consequence.  By contrast, even a square-root-in-\(q\) maximal estimate

\[
 \mathcal M_a(D)\ll_\varepsilon \sqrt D\,M_0
\]

would give only

\[
 \mathcal G_H^{\rm act}\ll_\varepsilon
 {D^2L^4\over A},                                   \tag{105.H2}
\]

which is still above (105.H1) by a factor \(D\).  The fixed-row plus
Cauchy route is above (105.H1) by \(D^2\).  A standard square-root
correlation theorem is therefore not enough: the frozen sufficient
theorem needs bounded partial sums, up to \(X^\varepsilon\).

For one complete metric mode put

\[
 c=\nu-{g\over2},\qquad n=|2\nu-g|=2|c|\ge1,
 \qquad \Psi(q,k)={q\over2}+c{\Lambda_q\over k}.
\]

The determinant calculation is exact.  With

\[
 t=\sqrt{a+2q\over a},\qquad
 \Lambda_q={Xa\over2}(t-1)^2,
\]

one has

\[
 \det \nabla^2_{q,k}\Psi
 =-{c^2X^2(t-1)^3\over t^3k^4}
 \asymp -{n^2A\over D}.                              \tag{105.H3}
\]

This full rank is real, including the density mode \(\nu=0\), but it is
not by itself a lattice-sum estimate.  In the orientation
\(c=-n/2\), a \(k\)-B process followed by a \(q\)-B process sends the
carrier exactly to

\[
 -\left(J\sqrt{n\ell\over s}-{\sqrt{as}\over2}\right)^2
 =-{Xn\ell\over s}+\sqrt{X(as)(n\ell)}-{as\over4},   \tag{105.H4}
\]

where \(\ell>0\) and the relevant stationary branch has the positive odd
integer \(s=1-2r\).  Since \(a,s\) are odd,
\(e(-as/4)=-i\chi_4(as)\).  Thus the dual carrier is again the
square-root-product/reciprocal two-character architecture, not a new
separated oscillatory direction.  The transformed stationary-mode count
and Hessian weight have no automatic capacity saving.  Applying the
adjoint transforms returns the original sum.

This is an exact **carrier-level no-go for a black-box Hessian argument**.
It is not yet a complete owner-preserving transform theorem: the dual
amplitude still contains the moving actual integral, primitive and prior
owner decompositions, lift entry/exit, metric weights, collars, floors,
stars, and the maximal cutoff.  Consequently (105.H4) neither proves nor
disproves (105.H1).

The Möbius progressions do not break this return.  On the term \(q=du\),
\(d\mid a\), the odd dual variable is \(s=d-2r\), and the same two scalar
B processes give

\[
 -{dXn\ell\over s}-{as\over4d}+J\sqrt{an\ell}
 =-\left(J\sqrt{dn\ell\over s}
          -{1\over2}\sqrt{as\over d}\right)^2.       \tag{105.H4d}
\]

Moreover \(e(-as/(4d))=-i\chi_4(a/d)\chi_4(s)\).  Thus exact primitive
decomposition preserves, rather than removes, the odd two-character
return.

Two literal seams do improve the interface.  First, primitivity has the
exact decomposition

\[
 \mathbf1_{(a,q)=1}=\sum_{d\mid a,\,d\mid q}\mu(d),
 \qquad q=dr,\qquad (-1)^{dr}=(-1)^r,                \tag{105.H5}
\]

because every divisor of the odd integer \(a\) is odd.  Primitivity
therefore preserves alternation at a divisor cost \(X^\varepsilon\).
Second, both reciprocal endpoints are increasing in \(q\), so for each
fixed integer \(k\) the geometric reciprocal support is one interval in
\(q\), with at most one entry and one exit.  Neither seam supplies the
missing cancellation in the interior.

## 2. Exact statement and hypotheses

Work on one literal residual hard-top cell with

\[
 b=a+2q,\qquad a,b\ \mathrm{odd},\qquad a<b<4a,\qquad
 a\asymp b\asymp A,\qquad q\asymp D,
\]

\[
 J=\sqrt X,\qquad K\asymp {JD\over A},\qquad
 G\asymp {L\over A},\qquad 1\le L\le J^{1/2}.
\]

The complete zero-extended row is the one in the accepted fixed-\(q\)
interface:

\[
\begin{aligned}
 F_a(q)=\mathbf1_{\rm actual\ owners}(a,q)
 \sum_{k\in I_{a,q}\cap\mathbb Z}
 W_R(\Lambda_q/k)
 \sum_{g\in\mathcal G_{a,q}}
 \Omega_{a,q,g}(k)
 e\!\left(-{g\Lambda_q\over2k}\right)
 \mathfrak B^\circ_{a,q,k}(g),                       \tag{105.H6}
\end{aligned}
\]

where

\[
 I_{a,q}=\left({J\delta_q\over2\sqrt a},
                {J\delta_q\over\sqrt{a+2q}}\right),
 \quad \delta_q=\sqrt{a+2q}-\sqrt a,
 \quad \Lambda_q={X\delta_q^2\over2}.              \tag{105.H7}
\]

All assertions in this report retain the following literal data:

- the primitive condition \((a,q)=1\) and every prior one-count owner;
- the open moving reciprocal interval and exact integer samples;
- the finite odd-lift set \(\mathcal G_{a,q}\);
- the accepted profiles, floors, stars, orientations, physical collars,
  saddle entry/exit, and zero extension;
- the whole punctured metric window, including its density coefficient
  and every discrepancy mode.

Opening the last item gives

\[
 W_R(\Lambda_q/k)
 =\sum_{\nu\in\mathbb Z}\widehat W_R(\nu)
 e(\nu\Lambda_q/k).
\]

Together with the centred carrier in (105.H6), one orientation has phase
\(\Psi(q,k)=q/2+c\Lambda_q/k\), where
\(c=\nu-g/2\).  Since every actual lift \(g\) is odd,

\[
 n=|2\nu-g|\quad\hbox{is a positive odd integer}.    \tag{105.H8}
\]

The conjugate orientation replaces \(\nu-g/2\) by \(\nu+g/2\) and has
the same conclusions.  In particular the density mode \(\nu=0\) has
\(n=g\), not zero.

The no-go proved here is deliberately scoped.  It says that neither the
centred transport identity alone nor the determinant (105.H3), followed
by an absolute or coefficient-blind transform estimate, proves the
bounded maximal theorem.  It does not say that cancellation in the
complete actual dual sum is impossible.

## 3. Proof or derivation

The scalar implication to the Gram is immediate but exact.  A
zero-extended row supported on \(q\asymp D\) has \(O(D+H)=O(D)\)
length-\(H\) windows when \(H\asymp D\).  Squaring the maximal bound and
summing over \(O(A)\) bases proves (105.H1).  Replacing \(M_0\) by
\(\sqrt D\,M_0\) proves (105.H2).  This also shows why a generic
square-root theorem cannot close the frozen Gram.

For the transport seam, write the centred physical phase as

\[
 r_{q,k}={J\delta_q\over2k},\qquad
 gk(y-r_{q,k})^2.
\]

Although

\[
 \partial_q e(gk(y-r_{q,k})^2)
 =-r'_{q,k}\,\partial_y e(gk(y-r_{q,k})^2)            \tag{105.H9}
\]

is exact, it acts only on the centred factor.  Recoupling it with one
complete metric mode gives the exact identity

\[
 c{\Lambda_q\over k}+gk(y-r_{q,k})^2
 =\nu{\Lambda_q\over k}+gky^2-gJ\delta_qy.           \tag{105.H10}
\]

Here \(gkr_{q,k}^2=g\Lambda_q/(2k)\).  At the saddle \(y=r_{q,k}\),
the derivative of the whole phase is

\[
 {1\over2}+c{\Lambda_q'\over k},\qquad
 {\Lambda_q'\over k}\asymp J.                       \tag{105.H11}
\]

Thus (105.H9) leaves a residual complete-mode derivative of size
\(nJ\).  Integrating the centred derivative by parts in \(y\) does not
turn (105.H11) into a \(D^{-1}\)-sized variation.  Any proof of total
transported variation must recover cancellation jointly in \((q,k)\),
after every moving symbol is included.  This is the first phase-level
failure of the proposed total-variation shortcut.

The endpoint algebra makes the derivative-gap failure literal.  In the
coordinate \(t=\sqrt{(a+2q)/a}\),

\[
 k_-(q)={J(t-1)\over2},\qquad
 k_+(q)={J(t-1)\over t}=J(1-t^{-1}),                 \tag{105.H12}
\]

and

\[
 k_-'(q)={J\over2at}>0,\qquad
 k_+'(q)={J\over at^3}>0.                            \tag{105.H13}
\]

This proves the two-jump statement for fixed \(k\).  It also gives

\[
 {\Lambda_q'\over k_+(q)}=J,\qquad
 {\Lambda_q'\over k_-(q)}={2J\over t}.              \tag{105.H14}
\]

For the orientation \(c=-n/2\), the \(q\)-derivative at the upper
corner is \((1-nJ)/2\).  If \(X=T^4\) with odd \(T\), then \(J=T^2\)
and odd \(n\) make this an integer.  Hence there is no uniform
first-derivative gap.  The exact point is at an open reciprocal endpoint
and at a flat, collarized physical saddle corner.  It is therefore not an
actual contributing lower-bound point.  The smooth collar removes the
exact corner from the residual core, while nearby resonances and the
separately owned collar terms still forbid a derivative-gap shortcut.

For the Hessian, use

\[
 \Lambda_q'=X(1-t^{-1}),\qquad
 \Lambda_q''={X\over at^3}.
\]

Direct differentiation yields

\[
 \Psi_{qq}={cX\over at^3k},\qquad
 \Psi_{qk}=-{cX(t-1)\over tk^2},\qquad
 \Psi_{kk}={cXa(t-1)^2\over k^3},
\]

whose determinant is (105.H3).  Since \(t-1\asymp D/A\) and
\(k\asymp JD/A\), its magnitude is \(\asymp n^2A/D\).

The corresponding gradient image has area, at scale,

\[
 |\det\nabla^2\Psi|\,DK\asymp n^2JD.                 \tag{105.H15}
\]

Each two-dimensional stationary term has Hessian factor

\[
 |\det\nabla^2\Psi|^{-1/2}\asymp {1\over n}\sqrt{D\over A}.
\]

Absolute summation of the dual stationary terms therefore has capacity

\[
 nJD\sqrt{D\over A},                                 \tag{105.H16}
\]

before the actual symbol is inserted.  This is not a determinant saving;
it requires a new cancellation theorem in the dual variables.

The exact carrier form of that dual problem is visible without a model
coefficient.  Choose the orientation

\[
 \Psi(q,k)={q\over2}-{n\Lambda_q\over2k}.
\]

In the \(k\)-B process, the dual integer \(\ell>0\) has stationary point
\(k_*^2=n\Lambda_q/(2\ell)\), and the stationary phase is

\[
 {q\over2}-J\delta_q\sqrt{n\ell}.                   \tag{105.H17}
\]

In the subsequent \(q\)-B process, subtract \(rq\) and put
\(s=1-2r\).  The relevant stationary branch has \(s>0\), an odd integer.
The stationary equation and value are

\[
 b_*=a+2q_*={4Xn\ell\over s^2},                      \tag{105.H18}
\]

\[
 {sq_*\over2}-J(\sqrt{b_*}-\sqrt a)\sqrt{n\ell}
 =-\left(J\sqrt{n\ell\over s}-{\sqrt{as}\over2}\right)^2. \tag{105.H19}
\]

Putting \(h=as\) and \(m=n\ell\) gives (105.H4).  The odd dual lattice
is exactly the alternation; it removes a literal zero \(s\)-mode but not
the large family of stationary modes.  The returned product phase and
reciprocal phase are the accepted transposed two-character architecture.
The complete zero-extended transforms are invertible, so another adjoint
step returns to the original capacity.  What is not established is an
identity between every prior-owner piece of the original amplitude and a
single prior-owner piece of the dual amplitude.  That missing seam is why
the conclusion is a determinant-only no-go, not a complete actual-symbol
self-return theorem.

For completeness, retain the Möbius divisor instead of shifting its
integer contribution out of \(du/2\).  On \(q=du\), subtracting the dual
integer \(ru\) gives \(s=d-2r\), again odd.  The stationary equations now
give

\[
 b_*={4d^2Xn\ell\over s^2},
\]

and the stationary value is exactly (105.H4d).  Since \(d\mid a\), the
last linear term supplies \(-i\chi_4(a/d)\chi_4(s)\).  This is not the
accepted terminal M1 divisor sum: its amplitude remains jointly dependent
on \((a,d,n,\ell,s)\), contains the transformed physical integral and all
owners, and is accompanied by the square-root term \(J\sqrt{an\ell}\).
The terminal M1 theorem assumes a one-dimensional reciprocal phase with a
separable fixed-shell BV weight.  No literal specialization is available.

Finally, (105.H5) follows from ordinary Möbius inversion.  The divisor
\(d\mid a\) is odd, so the parity character on the rescaled progression
is unchanged.  This removes primitivity as a source of alternation loss,
although it does not smooth the remaining owner masks.

## 4. First doubtful or unproved step

The first unproved step is **not** the scalar Abel inequality and is
**not** primitivity.  It is the passage from the centred identity
(105.H9) to a bound for the complete transported difference

\[
 \sum_{q\asymp D}|F_a(q+1)-F_a(q)|.                 \tag{105.H20}
\]

At the first complete Fourier mode, (105.H10)--(105.H11) leave the
oscillatory derivative \(c\Lambda_q'/k\asymp nJ\).  The accepted
fixed-\(q\) theorem supplies variation in sampled \(k\), not variation
in \(q\), and taking the absolute value in (105.H20) prevents one from
using the oscillation without a new joint theorem.

The actual amplitude introduces further seams that cannot be replaced by
an arbitrary bounded coefficient:

- Möbius decomposition handles \((a,q)=1\) exactly and preserves the
  character, but the prior square-ray deletion is a sparse arithmetic
  mask in \(q\).  At fixed \((a,q)\) it removes a whole row, whereas at
  fixed \(a\) it is not a smooth multiplier.  The accepted square-ray
  theorem controls its own complete signed contribution; it is not a
  per-base maximal-BV theorem for the complement.
- The geometric \(k\)-support has only two jumps per fixed \(k\), and
  the simple dyadic odd-lift support has only bounded entry/exit for fixed
  \(g\), because \(a+2q\) is monotone.  This is useful, but summing the
  absolute sizes of all entering and exiting samples restores the large
  \(k\)-capacity.  The phases at those crossings must remain coupled.
- Moving physical collars are flat at the exact endpoints, so no boundary
  term is created by formal integration by parts there.  Their transition
  symbols still move with \(q\), and the fixed-\(q\) sampled-variation
  theorem does not supply the required \(q\)-seminorm.
- Expanding the complete metric factor is mandatory.  It gives all odd
  \(n=|2\nu-g|\), including \(n=g\) for density.  Keeping the metric
  factor unexpanded merely hides a rapidly moving \(q\)-amplitude.
- A maximal prefix cutoff becomes another moving boundary after the two B
  processes.  A whole-shell transform estimate is not automatically
  uniform over all subintervals.

The first unproved step on the Hessian route is the conversion of the
carrier return (105.H4) into an estimate for the **complete transformed
actual amplitude**.  Full rank does not furnish such an estimate.  No
literal source theorem audited below accepts that amplitude and proves
bounded maximal partial sums.

No actual-symbol counterexample is certified.  Square rays, Pell and
near-square rays, and fourth-power choices create exact or near derivative
and metric recurrences.  However the exact metric centre is killed by the
punctured factor, square rays have their accepted signed \(k\)-owner, and
the endpoint resonance is open and collarized.  These are hostile method
controls, not lower bounds for \(F_a(q)\) or \(\mathcal M_a(D)\).

## 5. Required controls, outcomes, and primary-source hypothesis map

| Required control | Hostile test and outcome |
|---|---|
| maximal-to-Gram implication | Counting \(O(AD)\) windows at \(H\asymp D\) gives (105.H1) exactly. **Pass.** |
| total variation versus maximal alternation | Scalar Abel is valid, but (105.H10)--(105.H11) leave a residual derivative \(\asymp nJ\). **The sufficient TV route remains unproved and may be strictly stronger than the maximal theorem.** |
| square-root correlation consequence | A \(\sqrt D\) maximal gain leaves the exact factor-\(D\) Gram deficit (105.H2). **Insufficient.** |
| primitivity | Möbius inversion gives (105.H5); every divisor of odd \(a\) preserves \((-1)^q\). **Pass.** |
| moving \(k\)-interval | Both endpoints have positive derivatives (105.H13); fixed \(k\) has one support interval and at most two jumps. **Pass, but absolute entry/exit summation is too large.** |
| finite odd lifts | For fixed \(a,g\), the basic dyadic condition on \(g(a+2q)\) has bounded entry/exit. The full owner-weighted \(q\)-symbol has no accepted BV theorem. **Geometric pass; analytic seam open.** |
| complete centred integral | Exact recoupling (105.H10) shows what (105.H9) does and does not transport. **Pass algebraically; no TV estimate follows.** |
| physical collars | Flat collars remove the exact open endpoint resonance from the residual core and suppress integration-by-parts boundary terms. Moving transition seminorms in \(q\) remain unproved. **No lower obstruction; no transport theorem.** |
| collapsing cone edge | As \(t\to2^-\), \(k_-\) and \(k_+\) meet while (105.H3) stays nonzero. Empty/singleton fibres survive, so a rectangular two-dimensional theorem has no literal uniform support map. **Fixed-row control passes; Hessian import fails.** |
| density and discrepancy | Every mode has odd \(n\ge1\); \(\nu=0\) gives \(n=g\). The B-process must sum all modes and both orientations. **Pass only when kept jointly.** |
| exact q-boundary resonance | \(\Lambda'/k_+=J\); for odd fourth-power \(J\) and odd \(n\), the discrete derivative is integral. The point is open and collarized. **Derivative-gap shortcut rejected; no actual lower bound.** |
| Hessian determinant | Equation (105.H3) is exact and full rank. Its dual mode count and stationary weight give (105.H15)--(105.H16), not a gain. **Pass algebraically; determinant-only estimate rejected.** |
| two-step transform | Equations (105.H17)--(105.H19) return the reciprocal square-root-product carrier with the odd character. **Carrier self-return; complete owner-preserving theorem open.** |
| Möbius-progression transform | Formula (105.H4d) returns the character \(\chi_4(a/d)\chi_4(s)\) and a coupled reciprocal/product phase. **Primitivity does not create a new separated dual sum.** |
| Pell and near-square rows | They can approach metric and derivative resonances and rule out uniform Diophantine gaps. Accepted actual coefficient cancellation is not reversed. **Method control only.** |
| primitive square rays | For odd squares \(a=u^2,b=v^2\), \(q=(v^2-u^2)/2\) is even, so there is no character alternation on that subfamily. It is a prior-owned family with an accepted complete signed \(k\)-bound. **Not a residual counterexample.** |
| fourth powers | Taking \(X=T^4\) can make \(J\) integral and align endpoint or reciprocal phases. Smooth collars, the puncture, and the square-ray owner prevent a certified lower bound. **False-gap control passes.** |
| exact and near metric centres | Exact centres are zeros of the punctured metric factor; near centres remain at ordinary density and are included in every mode. **Exact removed; near problem open.** |
| coherent arbitrary coefficients | Phase-conjugated coefficients can force large partial sums but violate the actual Fresnel/profile transport. **False analogue rejected; not used.** |
| dyadic polynomial endpoints | The argument uses no reverse interval-length bound, but maximal prefix boundaries and the cone cusp remain in the transformed amplitude. **No endpoint theorem obtained.** |
| downstream scope | Even (105.H1) would close only the polynomial fixed-\(a\) Gram input to the canonical hard top. Other M2 packets, M9-M2, M9, endpoint uniformity, and the quarter target do not follow directly. **Pass.** |

The initial literal-hypothesis gate excludes every natural external
theorem recorded in the assigned context.  Therefore no external theorem
is imported and no new source card is proposed.

| Primary source/theorem already audited in the assigned context | Literal mismatch with the maximal actual row |
|---|---|
| Montgomery--Vaughan, *Hilbert's Inequality*, Theorem 1 | It requires a fixed separated frequency set and a compatible common coefficient family.  Here frequencies, support, lifts and actual coefficients move with \(q\); collisions and maximal prefixes remain.  Its Hilbert-space gain would in any event be an energy/square-root mechanism, not the bounded partial sum required by (105.H1). |
| Bombieri--Iwaniec, *On the order of \(\zeta(1/2+it)\)*, Lemma 2.4 | The double large sieve retains close-pair quadratic forms for factorized point sets.  After (105.H4), the complete physical coefficient is nonfactorized and the required close-pair form is the open actual kernel itself.  It gives no bounded maximal theorem for this amplitude. |
| Robert--Sargos, *Three-dimensional exponential sums with monomials*, Theorem 2 | This is an unweighted positive spacing count on fixed dyadic integer boxes.  It deletes the \(k,g\), metric, owner, collar and sign data and cannot cancel the Gram diagonal or control maximal prefixes. |
| Li--Yang, Proposition 3.1 and Theorem 4.2 | The audited forms use rectangular/separable bounded coefficients and fixed smooth phase hypotheses in explicit parameter ranges.  Neither the moving actual symbol nor the owner-weighted maximal cutoff maps to those hypotheses. |
| Bourgain's audited reciprocal exponent-pair interface | It treats one unweighted reciprocal progression, with a BV weight inserted afterwards and proper-subinterval uniformity.  The Round-105 object is a coupled \((q,k)\) sum whose actual coefficient has no accepted \(q\)-BV bound. |
| Accepted terminal M1 frequency-first divisor theorem | Its literal input is a separable \(u(h)w(d)e(hX/d)\) sum on fixed shells, with BV in the one-dimensional frequency weight.  Formula (105.H4d) has a coupled \((a,d,n,\ell,s)\) actual amplitude and the additional square-root product phase, so the internal theorem has no implication here. |
| Weyl, Satz 9 | Qualitative equidistribution for a fixed polynomial and fixed interval supplies neither shrinking-window uniformity nor bounded coefficient-weighted partial sums at fixed \(X\). |

In particular, none of these primary results supplies bounded partial
sums rather than a square-root/energy gain for the literal coefficient.
Because the coefficient map already fails, reopening other secondary
formulations would not satisfy the campaign's primary-source rule.

## 6. Dependencies and exact artifacts used

This report used exactly the assigned Round-105 brief and selected
context:

- `protocol.md`;
- `state/proof_obligations.yml`, especially the three target nodes and
  their accepted determinant, self-return, fixed-\(q\), square-ray and
  owner dependencies;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/reports/fixed_q_hostile_source_audit.md`;
- `rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/synthesis.md`;
- `rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/synthesis.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/synthesis.md`;
- `strategy/conductor_0817_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/briefs/maximal_q_hostile_source_audit.md`.

No sibling Round-105 report, proof draft, validation matrix, shared
synthesis, legacy response, or unlisted repository artifact was read.
The primary-source applicability check used the literal hypotheses already
recorded in the assigned fixed-\(q\) hostile audit and authoritative graph.
No source passed the coefficient gate, so no external theorem was imported
and no web source was needed.  No numerical experiment was performed.
Apart from this assigned report, no campaign artifact or shared state was
edited.

## 7. Recommended state effect

**Recommended effect: retain the polynomial maximal theorem and the full
fixed-\(a\) Gram as open; record only the exact algebraic interfaces and a
scoped determinant-only route obstruction.**

The following statements are suitable for conductor seam review as exact
internal reductions:

1. the maximal-to-Gram implication (105.H1), including the factor-\(D\)
   deficit left by a mere square-root maximal estimate;
2. Möbius primitivity with alternation preserved, (105.H5);
3. monotonicity of both reciprocal endpoints and the resulting two-jump
   fixed-\(k\) support, (105.H12)--(105.H13);
4. the complete-mode recoupling and residual derivative,
   (105.H10)--(105.H11);
5. the exact full-rank Hessian (105.H3) and the two-step carrier return
   (105.H17)--(105.H19).

Record the last item only as a no-go for **determinant-only or black-box
smooth-amplitude reasoning**.  Do not call it a complete owner-preserving
self-return until the transformed primitive decomposition, prior owners,
lift fibres, profiles, collars, density/discrepancy modes, and maximal
cutoff are matched one by one.

Do not reject (105.H1): the fourth-power endpoint recurrence is outside the
open collarized core, exact metric centres are punctured, square rays are
prior-owned, and no lower bound for the complete actual coefficient was
proved.  Also do not promote the total-variation estimate (105.H20), a
polynomial hard subrange, the canonical density--discrepancy energy,
M9-M2, M9, endpoint uniformity, or any new Gauss-circle exponent.

The strict surviving problem is a bounded **maximal** estimate for the
complete mode-resolved \((q,k)\) sum, or an averaged fixed-\(a\) theorem
with the same exact Gram consequence, using cancellation in the returned
actual dual carrier before absolute values.  It must treat the collar-owned
endpoint pieces and sparse prior-owner masks separately and must deliver a
full \(D\)-gain, not only square-root cancellation.
