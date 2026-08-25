# Round 140 conductor controls

Campaign: m9-m1-lower-post-collar-height-alias-gate

Starting graph SHA-256:
a9f766ddfc55c1aa9dd0561d8a406996627ac8701313af063c90e2422cf54eaa

## Mathematical seam matrix

| Control | Exact test | Outcome |
|---|---|---|
| exact \(N,y,q\) and tail dictionary | Retain \(N=y^2+q\), \(0\le q\le2y\), \(L_{i,h}\), \(D_{i,h}\), floors, empty rows, and both signs. | Green. Empty and profile-zero rows are defined before any \(D_{i,h}\) or \(r_{2,h}\) denominator is used. |
| mod-four Poisson branches | Apply finite Poisson separately to \(e(\pm d/4)\) with symmetric dual limits. | Green. \(r=\tau-4k\) covers every odd integer and \(\tau=\chi_4(r)\) for positive \(r\). |
| hard endpoint | Keep the inclusive half-endpoint and test absolute summability of the raw integrals. | Green obstruction. The endpoint is \(O(\log X)\), but each nonzero sharp row has a \(1/r\) boundary tail. |
| exact stationary entry | Derive \(x_*=2\sqrt{Nh/r}\) and retain the full floor and \(q\) threshold. | Green. The offset is exactly \(4h(2ya-a^2+q)/(y-a)^2\asymp_{\rho_1}\sqrt h\); equality is not a full Gaussian. |
| two-collar support | Check the off-by-one relation for \(W_h\) at every integer. | Green. Sharp minus smooth is supported exactly on \(L_{1,h}<v\le L_{2,h}\), with no new physical sample. |
| signed smoothing price | Apply the accepted exact-curvature estimate before Poisson. | Green. The complete band is \(O(R\log X)\) and changes only the unsquared scalar. |
| derivative ledger | Rescale the lower profile and integrate the upper cutoff derivatives. | Green. The norms are \(h^{-1}\), \(1/(Rh^2)\), and \(1/(h\Delta_h)\), with flat endpoints. |
| smooth \(B\)-process local errors | On \(x\asymp Z\), count \(P=Nh/Z^2\) aliases of width \(w=(Z^3/(Nh))^{1/2}\). | Green after explicit repair. Both \(Pw\epsilon_3/h\) and \(Pw^2/(hZ)\) are \(O(1/h)\). |
| cutoff-derivative localization | Count \(W_h'\) only where it is supported. | Green. The ramp has \(O(1+\sqrt h)\) aliases and \(\sqrt h\,w^2/(h\Delta_h)\ll1/h\). |
| remote aliases | Separate finite derivative-image distances from infinite tails. | Green. One integration gives the finite harmonic logarithm; two integrations plus flat endpoints make the negative and remote positive tails absolute. |
| rowwise and height error | Sum all smooth local and nonstationary errors. | Green. One row is \(O(h^{-1}\log^2 X)\), and all heights total \(O(\log^3 X)\). |
| ramp image and clean start | Compute the derivative image of \(D_{2,h}\le x\le D_{1,h}+1\). | Green. It has \(O(1+\sqrt h)\) odd aliases; including \(r_{2,h}\) costs \(O(R\log X)\), and the retained bulk starts at \(r_{2,h}+2\). |
| Gaussian normalization | Recompute the saddle factor and mod-four branch constant. | Green. The integral factor is \(2e(1/8)N^{1/4}(hr)^{-3/4}\), and \((2i)^{-1}\) gives \(e(-1/8)\chi_4(r)\). |
| stationary remainder | Sum the local Taylor and off-saddle pieces with the true profile range. | Green. Local errors are \(O(N^{-1/4}(hr)^{-5/4})\); the complete remainder is target-safe. |
| exact product regrouping | Group the finite far family by \(m=hr\). | Green. The coefficient is exactly \(A_{\rho_2}(m)\), with no missing height factor. |
| complete versus incomplete fibre | Remove the mask only as a comparison. | Green. The complete fibre is \(r_2(m)/4\), but it may not replace the incomplete coefficient. |
| coefficient-blind capacity | Prove both an upper bound and a matching term-modulus control. | Green. The divisor upper bound is \(R^{3/2+o(1)}\), and the \(h=1\) plateau has the same absolute capacity. |
| rank after \(r=4h+s\) | Transform the Hessian by the exact invertible linear map. | Green obstruction. It has rank one and determinant zero in both coordinate systems. |
| coherent-ray character | Test phase and \(\chi_4\) on an actual far ray. | Green scope. \((h,r)=(\ell,9\ell)\), \(\ell\equiv1\pmod4\), is coherent but has only target-scale mass. |
| prime-square fibre | Audit the far inequality for every divisor of \(p^{2a}\). | Green scope. In a sufficiently large fourth-power profile range, \(A_{\rho_2}(p^{2a})=a\); this is not a scalar lower bound. |
| exact and near radicals | Write \(N=Du^2\) and separate square from near-square phases. | Green only for exact radicals. Their mass is \(O(RD^{-3/4}X^\varepsilon)\); near radicals remain open. |
| second transform | Compute the Legendre critical value of \(\sqrt{Nm}-mz/4\). | Green obstruction. It is \(N/z\), so the phase returns to the reciprocal interface. |
| scalar directionality | Compare the new scalar with Round 138 without squaring the support split. | Green only as target equivalence. The cross term and lift-dependent cutoff remain open. |
| downstream scope | Audit lower GAR, M1, M2, endpoint, M9, bridge, target, and exponents. | Green. Every downstream owner and both recorded exponents are unchanged. |

## Independent seam reviews

| Review | Assigned seam | Outcome |
|---|---|---|
| blind post-unmask smoothed-connector rederivation | Two-collar support, derivative scales, ramp localization, rowwise \(B\)-process, and scalar direction | Final green after the literal multiplication in (140.C19e) was repaired. |
| hostile post-unmask owner-complete audit | Sharp principal value, floors, smoothing owners, nonstationary and remainder ledger, and downstream scope | Final green after the explicit (140.C19a)--(140.C19f) ledger and empty-row conventions were inserted. |
| discovery post-unmask rank-product audit | Hessian, coherent rays, product coefficient, capacity, prime fibres, radicals, self-return, and direction | Final green after the \(h=1\) capacity control and exact qualified prime-square fibre were inserted. |

No reviewer certifies its own principal discovery.  All requested repairs
are present in the final conductor candidate and adjudication.

## Exit-gate decision

- target_bound: not met;
- strict_height_alias_reduction: met;
- sharp_endpoint_absolute_split: rejected;
- rank_one_product_fibre_no_go: proved as a scoped obstruction, not as
  the terminal label.

The first open estimate is

\[
 \sum_{m\ll y}m^{-3/4}V_{\rm low}(R^2m/N)
 A_{\rho_2}(m)e(\sqrt{Nm})
 \ll_\varepsilon X^\varepsilon.
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
  numbered sections and a final green verdict.
- Candidate and conductor adjudication: present with exactly seven
  numbered sections.
- Artifact hygiene: green for all 16 campaign files; no standalone
  carriage returns, forbidden control bytes, replacement characters,
  trailing whitespace, conflict markers, or delimiter defects remain.
- Repository validation: green for campaign validation, raw JSON
  parsing, State Patch dry validation and application, six unit tests,
  compileall, and diff checking, with line-ending notices only.

## Downstream status

The exact post-collar tail is now reduced to one clean signed
height-alias/product-fibre scalar, but that scalar retains
\(R^{3/2+o(1)}\) coefficient-blind capacity and its near-radical
nonsquare cancellation is open.  Lower GAR, both direct blockwise M1
parents, M9-M1, hard TOP, BAL, every required UNBAL M2 owner, M9-M2,
endpoint uniformity, M9, the conditional bridge, and the quarter target
remain open.

The strongest internally proved exponent remains \(1/3\).  The
separately audited external Li--Yang exponent remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots .
\]
