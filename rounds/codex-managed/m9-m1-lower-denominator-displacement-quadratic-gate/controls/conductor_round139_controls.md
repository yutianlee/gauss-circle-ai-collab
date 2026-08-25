# Round 139 conductor controls

Campaign: m9-m1-lower-denominator-displacement-quadratic-gate

Starting graph SHA-256:
5e82825804e5bb2de43779e7121e76bcfaa4b89d7ac0977ca2ceb84a33be8552

## Mathematical seam matrix

| Control | Exact test | Outcome |
|---|---|---|
| exact \(N,y,q\) dictionary | Derive \(N=y^2+q\), \(0\leq q\leq2y\), and both directions of \(d=y-v\). | Green. No \(d=0\) or \(v=y\) row is created. |
| literal support | Retain the exact profile, endpoint samples, zero extension, and \(h\ll(y-v)/R\). | Green. Active heights satisfy \(h\ll R\); no rounded support row is inserted. |
| mod-four carrier | Parameterize every surviving denominator for both parities of \(y\). | Green. \(v=p_y+2n\), \(\chi_4(y-v)=e((y-v-1)/4)\), and even terms remain zero. |
| both scalar signs | Recompute the phase and curvature for \(\sigma=\pm1\). | Green. Curvature changes sign but not magnitude; the two scalars and both pieces are conjugate. |
| exact curvature | Differentiate the complete displacement phase on the parity lattice. | Green. \(\Psi_{\sigma,h}''(n)=8\sigma hN/(y-p_y-2n)^3\). |
| collar range | Check \(L_h=\lfloor\rho y/\sqrt h\rfloor\), denominator comparability, floors, and empty rows. | Green after repair. \(M_h\leq1+L_h/2\), and \(y-v\asymp_\rho y\). |
| profile sampled variation | Bound every smooth and hard boundary contribution before Abel summation. | Green. Monotone composition has fixed variation; the hard start, artificial end, and zero-extension jumps cost \(O(1)\). |
| weighted height ledger | Retain \(h^{-1}\) and sum every active height. | Green. One row costs \(O(\sqrt y+\sqrt{y/h})\), and the complete collar is \(O(R\log X)\). |
| maximal rowwise power scale | Generalize only within a fixed top fraction and price every dyadic height. | Green after repair. \(L_{\alpha,H}=\rho yH^{-\alpha}\) costs \(RH^{1/2-\alpha}+RH^{-1/2}\); \(\alpha=1/2\) is method-specific, not universal. |
| exact Taylor correction | Keep \(E_{h,q,y}(v)=hv(q+v^2)/(y(y-v))\) and audit \(q=0,2y\). | Green. The bounded-variation window is \(v\ll(y^2/h)^{1/3}\); the larger exact-phase collar is nonperturbative. |
| quadratic completion | State parity modulus, gcd, boundary modes, Fourier convention, and unit. | Green after repair. The modulus is \(2y\), the bound is \(\{2y(16h,2y)\}^{1/2}\), and the exact unit \(e(C_h)\) is retained. |
| Gauss versus Salié | Identify the complete finite sum after resolving the character. | Green. It is an ordinary additive quadratic Gauss sum; the reciprocal correction remains in the coefficient. |
| fourth-power variation | Test the full correction on a literal plateau at \(q=0,h=1\). | Green. Allowed parity increments give \(\operatorname{Var}(e(E))\gg y\), so global bounded-variation completion is false. |
| stationary aliases | Count all aliases on the collar and compare the full-row ledger. | Green. The collar collectively costs \(R\); a full \(h\asymp R\) row costs \(R^{3/2}\). |
| \(q\) and real-centre uniformity | Test \(q=0\), \(q=2y\), fourth powers, and every floor interval. | Green. Only \(y^2\leq N\leq y^2+2y\) enters the curvature comparison. |
| scalar directionality | Map the collar split to the Round-138 residual without inventing a positive sub-square. | Green only as logical target equivalence. The lift-dependent cutoff splits \(L_\chi(y/b)\), and the collar--tail square cross term stays open. |
| exact residual scope | Test whether the collar deletes a term from \(\mathcal R_{y^{-2}}\). | Red as a deletion. It proves no identity for \(|\mathcal S_N|^2\); only the three target statements are equivalent. |
| full completion direction | Compare exact DFT, coefficient-blind modulus, Poisson, and second Legendre steps. | Green as a no-go. Inversion returns the reciprocal scalar; moduli retain \(y\) or \(R^{3/2}\) capacity. |
| downstream scope | Audit lower GAR, direct M1, M9-M1, M2, endpoint, M9, bridge, target, and exponents. | Green. Every downstream owner and both recorded exponents are unchanged. |

## Independent seam reviews

| Review | Assigned seam | Outcome |
|---|---|---|
| blind post-unmask curvature rederivation | Exact collar, parity curvature, floors, height ledger, and residual direction | Green after replacing \(M_h\ll L_h\) by \(M_h\leq1+L_h/2\); red for any residual sub-square deletion. |
| hostile post-unmask curvature and directionality audit | Exact curvature, profile BV, maximal scale, aliases, and scope | Green after retaining the fixed \(\rho\) in generalized collars; full completion obstruction remains intact. |
| discovery post-unmask quadratic completion audit | Core algebra, modulus, gcd, Fourier unit, fourth-power variation, and scalar direction | Green after defining \(w_h,\widehat w_h,C_h\) in the exact completion and correcting the capacity wording. |

All three repairs are incorporated in the conductor candidate and
adjudication.  No reviewer certifies its own principal claim.

## Exit-gate decision

- target_bound: not met;
- strict_displacement_quadratic_reduction: met;
- displacement_quadratic_no_go: retained only for the attempted full
  fixed-modulus completion, not as the round's terminal label.

The first open estimate is

\[
 |\mathcal S_N^\pm|\ll_\varepsilon RX^\varepsilon.
\]

## Resource and artifact controls

- Analytical/algebraic work: 100 percent.
- Numerical or symbolic experiments: none.
- External theorem imports: none.
- Centre averaging, arbitrary arrays, positive separated energies, and
  desired circle estimates: none.
- Primary reports: three of three present, each with exactly seven
  numbered sections.
- Post-unmask reviews: three of three present, each with exactly seven
  numbered sections.
- Candidate and conductor adjudication: present with exactly seven
  numbered sections.
- Artifact hygiene: green for all 16 campaign files; no forbidden control,
  zero-width, replacement, trailing-whitespace, conflict, or delimiter
  defects remain.
- Repository validation: green for campaign validation, raw JSON parsing,
  State Patch dry validation, six of six unit tests, compileall, and diff
  checking (line-ending notices only).

## Downstream status

The exact scalar collar is proved target-safe, but the literal tail and
the Round-138 cross-denominator residual remain open at full-order
capacity.  Lower GAR, both direct blockwise M1 parents, M9-M1, hard TOP,
BAL, every required UNBAL M2 owner, M9-M2, endpoint uniformity, M9, the
conditional bridge, and the Gauss-circle quarter target remain open.

The strongest internally proved exponent remains \(1/3\).  The separately
audited external Li--Yang exponent remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots .
\]
