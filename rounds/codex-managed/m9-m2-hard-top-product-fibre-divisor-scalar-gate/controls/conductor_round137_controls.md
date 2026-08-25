# Round 137 conductor controls

Campaign: m9-m2-hard-top-product-fibre-divisor-scalar-gate

Starting graph SHA-256:
3c5003b1478d78b8469d4220ad305bb06ee0f869b9c4a741e7211642eeb52cc7

## Mathematical seam matrix

| Control | Exact test | Outcome |
|---|---|---|
| literal hard cone and square projection | Reproduce \(a_{\rm end}\), \(\lceil h/4\rceil\le m\le h\), zero extension, and remove \(hm=\square\) only by the proved norm triangle. | Green. No equality moved and no orthogonal energy split used. |
| exact product-fibre bijection | Check \(n=hm\) in both directions, including the ceiling. | Green. The fibre is exactly \(h\mid n,\sqrt n\le h\le2\sqrt n,m=n/h\). |
| truncated \(\chi_4\)-divisor coefficient | Retain every profile and test primes, prime powers, singleton semiprimes, and same-sign many-divisor fibres. | Green as a dictionary; no automatic character cancellation. |
| actual coefficient energy | Expand \(\sum|C_L(n)|^2\) and parameterize all equal products. | Green. The upper envelope is \(O(L^2\log L)\); Cauchy still has \(L^{2+o(1)}\) capacity. |
| squarefree-radical channels | Parameterize \(hm=Dt^2\), include \(\sqrt D\ll A\ll L\), all \((+1)\)-terms, factorizations, and parity. | Green. One channel has absolute mass \(\ll(1+L/\sqrt D)L^\varepsilon\). |
| exact versus near resonance | Classify \(e(J\sqrt{Dt^2})=1\) and compare different squarefree kernels. | Green. Exact points at one centre lie in at most one channel and are target-safe; near resonances remain open. |
| real centre and dual modes | Compute stationary integers and test \(X=4r^2n_0\). | Green as a control. A uniform first-derivative gap is false. |
| one-dimensional scalar capacity | Price \(J/L\) formal modes of size \(L^{3/2}/\sqrt J\). | No-go. The coefficient-free absolute capacity is \(\sqrt{JL}=L^{3/2}(H/L)\), not actual mass or a legal rough-coefficient estimate. |
| lawful divisibility completion | Insert \(h^{-1}\sum_{a\bmod h}e(an/h)\), prove \((a,k)\mapsto kh-a\) bijective, and recompute the saddle. | Green. The \(1/h\), \(2e(-1/8)L^{3/2}J^{-1/2}\), positive starred range, and all profiles survive. |
| completion and B-process self-return | Compare the completed \(n\)-process with the direct \(m\)-process and retain all correction owners. | Green at the stationary-principal level. Both return \(W(r/y)e(Xh/(4r))\); no full finite identity or saving follows. |
| complementary-divisor switch | Switch \(h\) to \(n_{\rm o}/h\) with even valuation retained. | Green as an involution; the transformed height profile remains literal and truncated. |
| full-divisor continuation | Split \(C_L=r_2/4-R_L\) with identical cutoffs. | No-go. \(R_L\) is uncontrolled; importing the desired circle estimate is circular, while an independent radial theorem would still leave the complement. |
| directionality | Test fibrewise modulus, positive energy, centre averaging, and phase-adapted arrays. | Rejected as substitutes. Arbitrary alignment is only a method control, never a physical lower bound. |
| uniformity and boundaries | Retain \(y,H,q_X\), half-open supports, hard face, endpoint stars, crossings, nonstationary modes, remainders, and square restoration. | Green as scope. No unowned error is absorbed into the principal family. |
| downstream scope | Test whether one polynomial nonsquare hard-TOP block closes any parent. | No. Hard TOP, BAL, UNBAL, M9-M2, M9-M1, endpoint uniformity, M9, and all exponent claims remain open. |

## Review record

- Discovery report: product_fibre_no_go; independently proves the
  \(L^2\log L\) energy envelope and direct reciprocal return.
- Statement-only report: product_fibre_no_go; independently locates the
  rough-coefficient seam, exact resonances, and canonical self-return.
- Hostile report: product_fibre_no_go; derives the lawful
  divisibility-completion map and full capacity/circularity ledger.
- Blind post-unmask review: green after the radical-shell, exact-resonance,
  principal-family, and route-circularity repairs.
- Discovery post-unmask review: green after recomputing both energy counts,
  radical channels, and the \(n\)- versus \(m\)-B-process factors.
- Hostile post-unmask review: green after verifying the residue bijection,
  Jacobian, exact profile, owner ledger, and full-divisor scope.

All promoted seams were independently recomputed. No numerical or symbolic
experiment and no external theorem import was used.

## Closure

Terminal label: product_fibre_no_go.

Promote only the two scoped structural nodes named in the conductor
adjudication. The first open input is a fixed-centre additive-twist or
equivalent actual-direction theorem for the literal \(C_L(n)\), saving
\(L^{1/2-o(1)}\) without a positive or averaged substitute, reciprocal
self-return, or imported Gauss-circle conclusion.

Validation and resulting graph hashes are appended after the State Patch
passes all mechanical checks.

## Applied validation record

Resulting graph SHA-256:
`56de446648dfb7a492fbb4b46c38d840fb14ac306df61bf61d466d26abfbe797`.

The State Patch applied two creates, three updates, sixteen rejects, and
eight no-change decisions. The patched graph and completed campaign
validate. Six of six unit tests pass; bytecode compilation succeeds; all
JSON-backed state and campaign files parse; and `git diff --check` passes
apart from line-ending notices. All sixteen Round-137 artifacts are strict
UTF-8 and pass the control-character, replacement-character, trailing-space,
conflict-marker, and delimiter hygiene checks.
