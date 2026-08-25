# Round 138 conductor controls

Campaign: m9-m1-lower-gar-signed-farey-scalar-gate

Starting graph SHA-256:
56de446648dfb7a492fbb4b46c38d840fb14ac306df61bf61d466d26abfbe797

## Mathematical seam matrix

| Control | Exact test | Outcome |
|---|---|---|
| integerized flat cone | Distinguish the \(e(hN/d)\) scalar from the original \(e(hX/d)\) cone and retain the accepted \(O(R)\) phase seam. | Green. The Farey scalar is termwise \(\mathcal B_{\rm flat}^{(N)}\), while \(\mathcal B_{\rm flat}^{+}=\mathcal B_{\rm flat}^{(N)}+O(R)\). |
| certified small arc | Reproduce the literal profile support, \(1\le h<d\le y\), and \(\eta(yh/d)=1\). | Green. The exact support certificate, not an asymptotic \(C/R\) statement alone, owns \(h<d\). |
| reduced lift and centre | Set \(h=ag,d=bg\), retain odd \(b,g\), primitive \(a\), all lifts, and the zero class. | Green. The coefficient is \(\chi_4(b)L_\chi(y/b)/a\), and \(J(0)=0\) kills \(b=1\). |
| literal coefficient ledger | Check \(|c_{a,b}|\ll1/a\), \(a\ll b/R\), total \(\ell^1\), and equality \(\ell^2\). | Green. The totals are \(O(y\log X)\) and \(O(y)\), respectively. |
| full same-denominator owner | Keep all unequal numerators in the actual row polynomial before taking a modulus. | Green. The complete row square is \(O(y\log^2X)\); no residual row is separated. |
| ordinary phase fibres | Reduce \(Na/b\) with \(g=(N,b)\), including \(q=1\), parity, primitive restrictions, and divisor denominators. | Green. One fibre has mass \(O(\tau(N)\log X)\); total mass is \(O(y\log X)\). |
| physical carrier fibres | Absorb \(\chi_4(b)=e((b-1)/4)\) and classify both congruence branches. | Green. One physical fibre is a union of at most two ordinary fibres. |
| microscopic packing | Use exact denominator bounds and circular spacing for both carriers. | Green. Each \(\delta\)-collar costs \(O(y\tau(N)\log^2X(1+\delta y^2))\), target-safe at \(\delta=y^{-2}\). |
| exact survivor | Partition the ordered scalar square into rows, the union of both collars, and their complement. | Green. The complement is real and gives \(|\mathcal F_N|^2=\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon)\). |
| determinant chart | Retain odd \(G,r,s\), primitive holes, the coherent solution direction, and endpoint/aspect terms. | Green as a dictionary; red as a gain. The phase and character are constant in \(\ell\), and an aspect-free \(1/|\delta_0|\) bound is false. |
| determinant parity falsifier | Replace the stale even-\(s\) example by odd \(S\to\infty\) with \(r=1,s=S,a=a'=1\). | Green. With \(G\asymp R^{3/2}\), \(S\asymp R^{1/2}\), the reciprocal kernel is \(1\) while \(\log X/(S-1)\to0\). |
| fourth-power packet | Test \(a=1,b=y-4u\) at odd fourth powers with the literal profile plateau. | Green as target-scale residual capacity only. Exterior terms may cancel; no physical lower bound follows. |
| adjacent-character tubes | Reconcile the accepted half-integer tube construction with the Farey survivor. | Green as a post-pairing modulus obstruction. Its \(R^{3/2}\) capacity is not a signed scalar lower bound. |
| complete character Poisson | Retain the hard half-endpoint, both branches, nonstationary modes, crossings, remainders, and floors. | Green. The exact formula is the integral ledger; the clean square-root sum is only an interior principal family. |
| stationary normalization | Recompute the saddle, Hessian, branch factor, profile, and Gaussian constant. | Green. The principal factor is \(e(-1/8)N^{1/4}\chi_4(r)(hr)^{-3/4}V_{\rm low}(R^2hr/N)e(\sqrt{Nhr})\). |
| principal capacity | Sum all possible stationary modes without discarding an owner. | No-go as a modulus. The ledger is \(O(R^{3/2}\log X)\), a factor \(R^{1/2}\) above target. |
| squarefree radical channel | Write \(N=Ds^2\) and classify exact variable phase one. | Green only inside a bounded principal/transition family. The unique channel \(hr=Dt^2\) has mass \(O_\varepsilon(RD^{-3/4}X^\varepsilon)\); near radicals remain open. |
| transform directionality | Apply a second Legendre step and exact periodic completion. | Self-return. They recover the reciprocal phase and flat discrepancy; no contraction is proved. |
| real centre and signs | Retain \(N,y\), both frequency signs, the hard endpoint, and the \(O(R)\) integerization seam. | Green. All statements are uniform for real \(X\ge2\). |
| downstream scope | Test every GAR, blockwise M1, M2, endpoint, M9, quarter, and exponent owner. | No downstream closure. Only the strict lower scalar-square reduction changes. |

## Review record

- Discovery report: strict_signed_farey_reduction; proves the full row,
  both carrier collars, determinant chart, physical tube capacity, and
  interior-principal radical control.
- Statement-only report: strict_signed_farey_reduction; independently
  proves the exact lift, row, exact phase fibres, and Poisson self-return.
- Hostile report: strict_signed_farey_reduction; supplies the exact
  hard-endpoint Poisson formula, endpoint/aspect correction, fourth-power
  packet, and complete owner ledger.
- Discovery post-unmask review: green after the integerized-cone, odd
  determinant, Poisson, radical, and scope repairs.
- Blind post-unmask review: green after independently recomputing the
  rows, both collars, odd fibre converse, complete endpoint, and residual.
- Hostile post-unmask review: green after reconciling all other artifacts,
  the variable odd-\(S\) control, physical packets, and downstream scope.

The parity-invalid \(s=100\) examples in working drafts were mechanically
replaced by the variable odd-\(S\) family before closure. All promoted
seams were independently recomputed. No numerical or symbolic experiment,
centre average, arbitrary coefficient replacement, or external theorem
was used.

## Closure

Terminal label: strict_signed_farey_reduction.

Promote only the exact scalar/Farey dictionary, complete row bound, both
carrier-fibre packing bounds, strict residual identity, and the scoped
determinant/Poisson/radical/self-return obstruction. The first open input
is a prescribed-centre signed estimate

\[
 |\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon
\]

that keeps the literal coefficient, primitive numerator, determinant,
ordinary carrier, physical carrier, and boundary owners joint.

Validation and the resulting graph hash are appended after the State
Patch passes all mechanical checks.

## Applied validation record

Resulting graph SHA-256:
`5e82825804e5bb2de43779e7121e76bcfaa4b89d7ac0977ca2ceb84a33be8552`.

The State Patch applied two creates, three updates, twenty rejects, and
eight no-change decisions. The patched graph and completed campaign
validate. Six of six unit tests pass; bytecode compilation succeeds; all
JSON-backed state and campaign files parse; and `git diff --check` passes
apart from line-ending notices. All sixteen Round-138 artifacts are strict
UTF-8 and pass the control-character, replacement-character,
trailing-space, conflict-marker, and delimiter hygiene checks.
