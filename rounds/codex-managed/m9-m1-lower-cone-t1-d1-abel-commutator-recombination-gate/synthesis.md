# Round 159 synthesis

- Campaign: `m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate`
- Starting graph: `8a0f917fb8117e9dbaf287d9f773046ff201729d2d8d8c3df1a51bca7815574b`
- Terminal label: `paired_interior_abel_commutator_no_go`
- Graph mutation: applied
- Resulting graph: `4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`

## Outcome

Round 159 proves that the six sign-adapted Abel lines are a telescoping
presentation of the original positive and negative rows.  The positive
right outer endpoint, positive moving atom, positive profile difference,
negative left outer endpoint, negative moving atom, and negative profile
difference reconstruct the two original rows separately for every odd
divisor and every frequency.  Both moving atoms have positive sign.  No
individual Abel term is estimated by this identity.

Recombining first and then applying complete half-period inversion gives

\[
 \mathcal T_{\mathrm{int},U}(V)
 =\mathcal S_U(V)-\mathcal Z_U(V)-\mathcal F_U(V),
\tag{159.Y1}
\]

where the two special terms are the whole zero and Nyquist rows, subtracted
exactly once, and

\[
 |\mathcal Z_U(V)|+|\mathcal F_U(V)|
 \ll_\varepsilon M^{-1/4}X^\varepsilon.
\tag{159.Y2}
\]

The special pieces of the isolated Round-158 trace are not additional
subtractions.

## Exact common-profile return

The physical cells

\[
 x^2-x+1\le N\ell\le x^2+x
\tag{159.Y3}
\]

partition the positive integers.  Fixed-dilation support and the inherited
compatible nonwrapping lift contain the unique supported root hull.  With

\[
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell,
\tag{159.Y4}
\]

the completed physical row is exactly

\[
 \boxed{
 \mathcal S_U(V)=
 \sum_{\ell\ge1}\chi_4(\ell)w_U(\ell)e(\sqrt{N\ell})
 \mathbf1_{V<|r(\ell)|\le2V}.}
\tag{159.Y5}
\]

This is the accepted Round-154 hard dyadic common-profile root-defect block,
not a new analytic wave.  The isolated Round-158 moving trace continues to
have two distinct boundary-frozen profiles.  Those profiles are not
identified; the quotient profile is restored only after all six lines are
added.

## Target and method frontier

Writing (w_U=M^{-3/4}\widetilde w_U), the first open theorem is

\[
 \left|
 \sum_{\ell\asymp M}\chi_4(\ell)\widetilde w_U(\ell)
 e(\sqrt{N\ell})\mathbf1_{V<|r(\ell)|\le2V}
 \right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{159.Y6}
\]

This is equivalent to the normalized scalar (O_\varepsilon(X^\varepsilon))
target.  The mask satisfies

\[
 r=-\delta(2\kappa+\delta),
 \qquad \delta=\sqrt{N\ell}-\kappa(\ell),
\tag{159.Y7}
\]

and has four moving endpoints, strict inner and closed outer dyadic edges,
and centered-cell clipping.  Its shifted (h=-1) Fourier coefficient is
raw (O_\varepsilon(X^\varepsilon)) because (chi_4) remains, but every
other moving mode and the hard-boundary remainder stay open.

The complete ordinary discrepancy capacity is

\[
 \frac M Q+\sqrt{KQ}+\frac M{\sqrt K}+1,
\tag{159.Y8}
\]

which requires (M\ge N^{2/3}).  Literal Vaaler--Fejér/root incidence gives

\[
 E_J\ll_\varepsilon
 \left(\frac KJ+\sqrt V+\sqrt M+1\right)X^\varepsilon.
\tag{159.Y9}
\]

At (J=KM^{-3/4}), the transformed pair ((195/796,235/398)) has raw
capacity

\[
 N^{195/796}M^{1295/3184+\varepsilon},
\tag{159.Y10}
\]

and needs (M^{1093}\ge N^{780}).  The older (M^{703}\ge N^{390})
threshold belongs only to the easier fixed-boundary (M/J) model.  The
(B)-process returns the accepted reciprocal carrier, and favorable
incomplete quadratic completion again needs (M\ge N^{2/3}).  These are
upper capacities of named routes, not lower bounds or universal no-go
theorems.

No audited source through 25 August 2026 proves the joint signed variable-
mask estimate.  For the named Fourier route, the first missing input is
signed boundary-incidence control when (V>M^{3/2}), or a joint estimate
for all nonzero moving modes when (V\le M^{3/2}).

## Proof status

The exact full-row algebra improves the proof architecture: the isolated
trace, both outer endpoints, and both profile-difference terms no longer
need five separate target estimates.  They telescope back to one already
known common-profile wave.  Analytically, however, the round self-returns to
the existing Round-154 frontier.  The fixed-polylogarithmic collar remains
the last proved complete (D=1) range, and the open side
(M^{449}\ll R^{780}), (R=X^{1/4}), is unchanged.

Every (D>1), (L>1), generic (t=1), original (t\ge2), cross, remaining
M1, and M2 owner remains separate.  Endpoint uniformity, M9, the bridge, and
the quarter theorem remain open.  The internal global exponent remains
(1/3); the separately audited external Li--Yang exponent remains
(0.3144831759740614\ldots).

## Reviews and state effect

The independent lift/normalization review, independent terminal line review,
hostile power/source review, and terminal State Patch scope review are GREEN
for this narrow package.  The blind report independently verifies the Abel
algebra and exposes the need for a lift indicator under stripped hypotheses;
its countermodel does not apply to the actual compatible project lift.  The
source audit's periodic-wrap seam was repaired with exact shifted-square-root
circle identities.

The validated State Patch creates one proved-internal obstruction, updates
nine obligations, rejects twenty-two overbroad inferences, and records eight
principal downstream obligations unchanged.  The resulting graph is
`4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`.
