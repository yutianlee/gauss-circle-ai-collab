# Round 105 conductor controls

Campaign: m9-m2-polynomial-q-maximal-alternation

Starting graph SHA-256:
f8f20833d2f24fa0b323488e247887ba943b8dffdd3eacb58e5bae773eb5831b

## Logical and capacity controls

- `maximal_to_Gram_one_count`: passed conditionally.  For
  \(H\asymp D\), zero extension leaves \(O(D)\) nonzero sliding
  windows per base, so a maximal row bound \(L^2/A\) gives exactly
  \(DL^4/A=H^2L^4/(AD)\).
- `pointwise_route_deficit`: passed.  The proved fixed-row estimate gives
  maximal capacity \(DL^2/A\) and direct-Cauchy Gram capacity
  \(H^2DL^4/A\), an exact \(D^2\) deficit against the target.
- `maximal_vs_Gram`: passed.  The maximal theorem is sufficient but not
  necessary; the exact weighted shift aggregate can close the Gram
  without bounding every rowwise partial sum.
- `variation_vs_maximal`: passed.  Total adjacent variation is sufficient
  but not necessary.  Even the primitive mask can have variation
  \(\asymp D\) while its alternating interval sums are bounded.

## Actual phase controls

- `complete_carrier_recoupling`: passed.  The exact identity is
  \[
   (\nu-g/2)\Lambda/k+gk(y-r)^2
   =\nu\Lambda/k+gky^2-gJ\delta y.
  \]
  The density mode is retained as the original physical phase.
- `material_derivative_residual`: passed as a no-go.  Adjacent transport
  of the centered integral leaves
  \((\nu-g/2)\Lambda'/k\asymp nJ\).  Absolute differentiation therefore
  does not prove the claimed total variation.
- `joint_Hessian`: passed algebraically.  With
  \(t=\sqrt{(a+2q)/a}\),
  \[
   \det\nabla^2_{q,k}\Psi
   =-c^2X^2(t-1)^3/(t^3k^4)\asymp-n^2A/D.
  \]
- `two_step_stationary_return`: passed at the scalar stationary-phase
  level.  A \(k\)-process followed by a \(q\)-process has odd dual
  \(s=1-2r\) and phase
  \[
   -Xn\ell/s-sa/4+J\sqrt{an\ell}
   =-\left(J\sqrt{n\ell/s}-\sqrt{as}/2\right)^2.
  \]
  This is a centered dual-square return.  It does not license another
  determinant gain and does not itself bound the complete actual dual
  vector.
- `endpoint_derivative_gap`: rejected.  At
  \(k_+=J\delta/\sqrt{a+2q}\), one has \(\Lambda'/k_+=J\).  The exact
  corner is open and flat-collarized, so it is a shortcut falsifier, not
  an actual lower bound.

## Arithmetic and support controls

- `primitive_mask`: passed.  Exact Mobius inversion and oddness of every
  \(d\mid a\) give
  \((-1)^{dr}=(-1)^r\) and mask-only interval sums
  \(O(\tau(a))\).  Multiplication by the moving metric coefficient remains
  the open step.
- `moving_reciprocal_interval`: passed geometrically.  Both reciprocal
  endpoints are monotone in \(q\); every fixed integer \(k\) has at most
  one entry and one exit.  This controls support combinatorics but not the
  metric phase.
- `finite_lifts_profiles_floors_stars`: retained.  No theorem is promoted
  by suppressing these actual factors; a complete analytic bound for their
  dual image is absent.
- `collapsing_cone_edge`: passed as a route control.  The fixed-row BV
  theorem remains uniform, but no polynomial cross-row estimate follows.
- `density_discrepancy_one_count`: passed by retention.  No density mode,
  discrepancy mode, orientation, exact center, or zero-extension boundary
  is separately deleted.

## Hostile models and scope

- `coherent_coefficient_shadow`: passed as a falsifier of coefficient-
  uniform claims.  \(F_a(q)=(-1)^qL^2/A\) violates the maximal theorem by
  \(D\), but is not an actual-symbol counterexample.
- `Pell_square_fourth_power`: no actual lower bound is inferred.  The
  endpoint resonance and dual square show why derivative-gap and generic
  Hessian claims must retain these families; prior square owners remain
  one-count.
- `primary_sources`: no audited black-box theorem supplies bounded partial
  sums for the moving complete actual symbol.  Generic square-root
  cancellation would in any event be insufficient for the frozen Gram.
- `exponent_scope`: passed.  No positive-power \(D\)-range, full hard
  cone, M9-M2, M9, quarter theorem, or global exponent is obtained.

## Conductor verdict

The conditional maximal-to-Gram implication and the exact phase/transport
identities are certified.  The maximal theorem, total variation, direct
polynomial Gram, and every downstream conclusion remain open.  The next
interface is the actual-vector weighted shift aggregate, equivalently its
complete dual centered-square row, after owners and stationary errors are
transported once.
