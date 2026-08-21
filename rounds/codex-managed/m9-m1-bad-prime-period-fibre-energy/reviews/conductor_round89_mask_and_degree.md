# Round 89 conductor review: mask and degree

## Verdict

The small-prime table, transverse lift theorem, and cellwise two-sided
degree bound pass.

## Checks

- The complete mask, rather than a numerator surrogate, is used.
- Exhaustion gives (1,15,25,13) successful raw reductions at
  (p=2,3,5,7), and the normalized rays agree across the constructive,
  blind-supplemental, hostile-supplemental, and conductor checks.
- Nonzero second derivatives on the transverse (p=3,5) discs rule out
  every deeper lift, giving exact depth one.
- Source and target counts are performed separately.  A zero projective
  coordinate pays the necessary (p-1) scaling factor.
- CRT multiplication gives (M^2/\mathfrak b_sigma); deleting earlier
  owners cannot increase either degree.
- Complete reduction cells retain the entire base-point sum and hence do
  not corrupt the (p^{2j}) completed-trace descent.

The union estimate is only the sum of cellwise degrees.  It is not an
orthogonality or cancellation statement.

