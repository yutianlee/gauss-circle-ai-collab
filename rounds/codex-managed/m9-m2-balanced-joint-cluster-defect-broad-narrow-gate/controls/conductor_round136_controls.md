# Round 136 conductor controls

Campaign: `m9-m2-balanced-joint-cluster-defect-broad-narrow-gate`

Starting graph SHA-256:
`c43058006cec6849cd17a49e6a7a5298f5a3c124b34d2333b3279adcb54da1d1`

## Mathematical seam matrix

| Control | Exact test | Outcome |
|---|---|---|
| literal bulk kernel and owner ledger | Retain \((h,k,k',d,J,\mu)\), \(b_B\), \(\gamma_d\), \(\mathcal A_{d,J}\), both strict gates, and the fixed physical block. | Green. Only the interior stationary bulk is reopened; every boundary, transition, crossing, nonstationary, remainder, and phase-free owner is used zero additional times. |
| combined character carrier | Derive the phase from \(h+2s_d=d\ell_d\) and \(\mu=1/2-m\), keeping both original \(\chi_4\) factors. | Green. The exact identity is \(-i(-1)^m\chi_4(d)\chi_4(h)\). Residue alone is not the complete carrier. |
| equal-rational lift chart | Reduce \(2\lambda=a/b\) and enumerate every odd lift. | Green. All lifts are \((d,\mu)=(bc,ac/2)\), and \((-1)^m\chi_4(d)=\chi_4(ab)\). Their amplitudes and progressions remain distinct. |
| gate invariance across lifts | Compare \(x_*=Xk'/\lambda^2\), \(\rho\), and \(\Delta\) for fixed reduced \(\lambda\). | Green. The gates are common across the lift multiplier, although support and \(J\)-admissibility need not be. |
| determinant type | Compare the blind gradient-vector determinant, discovery gradient-surface normal determinant, and hostile one-body Hessian. | Green after reconciliation. They are three inequivalent objects; no inference between them is made. |
| exact gauge | Move the combined carrier into the coefficient and compare \(\Sigma_0=(r-z,r^{-1},-z^{-1})\) with \(\Sigma_1=(r,r^{-1},-z^{-1})\). | Green. The gauged surface normals are coplanar. This empties only the chosen gauged surface-normal broad class, not every possible broad decomposition. |
| modulation-invariant broadness | Ask whether raw surface-normal curvature is a sufficient coefficient-uniform certificate after the exact unit modulation. | No-go. Coefficient magnitudes and the scalar are unchanged while the normal geometry changes. A gauge-sensitive actual-symbol theorem remains possible but is absent. |
| raw gradient transversality | Retain the exact \(L^7\) three-gradient determinant on broad slope triples and seek a scalar return inequality. | No-go. No spatial/parameter norm or fixed-scalar exponential-sum theorem prices the determinant. |
| fixed-\(Q\) ruling | Fix \(Q=\mu^2h/(d^2k)=Xc^2\) and test both gauges. | Green. Both gradient families obey \(G_2+cG_3=0\), so the three-gradient determinant vanishes on the ruling. |
| coupled far gates | Substitute fixed \(c\) and \(A=k'/k\). | Green. \(\rho=hk'(c^2-1)/c^2\), \(\Delta=hk(A^2-c^2)/c^2\); the gates remove collars, not the ruling. |
| same-denominator cluster | Pigeonhole same-parity reciprocal frequencies at the natural fixed-slice resolution after both collars. | Green only for cardinality \(\gg d^2L^2\). No second-normal condition, common \(v\)-run, actual weighted mass, or lower bound is inferred. |
| capacity direction | Compare alias \(\ell^1\), positive square mass, and the signed scalar. | Green as an obstruction. \(L^5\) and \(L^4\) are upper/adversarial capacities, not physical lower bounds or substitutes for the \(L^3\) scalar. |
| leading divisor positivity | Audit \(\sum_{d\mid n}\gamma_d/d\). | Green only for the exact divisor identity and a separately verified leading common-profile/common-admissibility model. Full literal amplitude positivity is unproved. |
| phase-adapted coefficients | Align arbitrary bounded amplitudes with the phase. | Green as a coefficient-uniform falsifier only. The array need not be the actual stationary amplitude and is not a physical lower bound. |
| second B-process | Recompute the stationary action and arithmetic lattice. | Canonical phase self-return only. Full profile, gate, \(J\), transition, and remainder return needs a new owner ledger; no saving is claimed. |
| scalar versus positive energy | Compare the one fixed signed scalar with cap and row square functions. | Green. Positive energy is a stronger object and cannot be declared equivalent to the target. |
| downstream scope | Trace the graph from the balanced bulk target. | Green. BAL, hard TOP, UNBAL, M9-M2, M9-M1, endpoint uniformity, M9, and both global exponents remain unchanged. |

## Post-unmask corrections

1. The blind determinant uses three gradient vectors; the discovery
   determinant uses three surface normals; the hostile Hessian is a
   one-body Jacobian.
2. The gauged broad part is empty only under the discovery report's chosen
   surface-normal definition. Intrinsic empty-broad language was removed.
3. The residue-only half-integral multiplier was replaced by the full
   character-restored carrier.
4. Equal-rational lifts are carrier- and gate-coherent but retain distinct
   amplitudes and owners.
5. Fixed-slice cluster counts were separated from unproved common-run and
   actual-mass claims.
6. The positive divisor identity was restricted to its leading
   common-profile scope.
7. The second-B statement was restricted to canonical phase self-return.
8. Adversarial capacities were not treated as physical lower bounds.

## Validation record

- State Patch: validated and applied cleanly, with 2 creates, 4 updates,
  16 rejections, and 8 explicit no-change records.
- Resulting graph SHA-256:
  `3c5003b1478d78b8469d4220ad305bb06ee0f869b9c4a741e7211642eeb52cc7`.
- Patched graph: green under structural, dependency, and evidence-path
  validation.
- Campaign manifest: green before closure; the durable plan contains all
  completed task statuses and the closing assessment.
- Unit tests: six of six passed under explicit test discovery.
- Source compilation: `math_collab` and tests green.
- JSON parsing: campaign manifest, next-round plan, round ledger, validation
  matrix, campaign plan, and State Patch green.
- Artifact hygiene: all 16 Round-136 files are strict UTF-8 with no embedded
  control bytes, replacement characters, trailing whitespace, conflict
  markers, or unbalanced inline/display delimiters.
- Diff check: green.

No numerical experiment or external theorem was used; the round was 100%
algebraic and analytic.
