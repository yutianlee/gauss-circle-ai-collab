# Conductor controls for Round 176

- Campaign: `m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate`
- Starting graph: `9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`
- Allocation: 100% analytical/algebraic; 0% numerical
- Selected terminal label: `k17a_cross_gcd_alternating_fibre_capacity_or_self_return_no_go`

## Mathematical controls

- Exact plus/minus incidence maps and conjugations: GREEN.
- Multiplicity and coordinate compatibility: GREEN.
- Displacement positivity is explicit rather than delegated to zero
  extension: GREEN.
- Original divisor gcd on nonzero squarefree atoms: GREEN,
  \((d,d')=(u,n)\).
- Odd and even-even parity branches: GREEN.
- Canonical-anchor DFT, primitive modulus, and normalized norms: GREEN.
- Robust hyperbola count and fixed-proportion owner theorem: GREEN.
- Rowwise and two-variable positive-transform scopes: GREEN and
  quarantined from physical lower mass.
- Constant-anchor, arbitrary-support, selector-erased, and dechirped
  controls: quarantined.
- Sufficient joint estimate: explicitly OPEN.
- K17a and every downstream owner: unchanged and OPEN.

## Review controls

The candidate received an initial AMBER review, incorporated every
mandatory repair, and then received two independent GREEN post-repair
verifications.  The final proof kernel received a separate GREEN
mathematical review.  Independent power/owner and State Patch
scope/cycle/reversibility reviews are GREEN.

## Applied State Patch

- Exact effect: `1 create / 3 update / 0 correct-rejected / 16 reject / 18 no-change`.
- Applied graph SHA-256:
  `e3927f0ace0f3d74e9e9f5116a319159e3508838c7f7bd14b086fa851cad82b8`.
- Repository graph validator: PASS with zero schema or reference issues.
- Evidence-path audit: PASS; all 15 unique new-node evidence paths exist.
- Canonical inversion using the patch's explicit preimage metadata recovers
  `9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`
  exactly.
- Patch-local dependency cycle effect: zero.  The stricter independent
  audit records three inherited dependency SCCs and one additional
  inherited SCC after normalizing implication direction; all before/after
  component sets are identical.  These are pre-existing graph debt, not a
  Round 176 mutation.
- Independent post-application verification: GREEN.  The actual graph has
  the certified hash and exact operation effect; canonical inversion recovers
  the starting hash, timestamp-controlled reapplication is object-exact, and
  patch-local dependency-SCC and hidden-implication deltas are zero.
