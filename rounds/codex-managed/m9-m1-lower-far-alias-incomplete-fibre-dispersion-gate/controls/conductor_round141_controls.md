# Round 141 conductor controls

Campaign: m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate

Starting graph SHA-256:
072e08848e9d368d65b89fbf03c36423a8e3662e7ae61c48052d4c352d1d71b0

## Mathematical seam matrix

| Control | Exact test | Outcome |
|---|---|---|
| exact incomplete mask | Retain \(L_h,D_h,r_h\), the least-positive-odd convention, empty rows, profile zeros, \(0\le q\le2y\), and every real centre. | Green. For odd \(r\), \(r\ge r_h+2\) iff \((r-2)D_h^2\ge4Nh\). |
| floor-to-cone sign | Partition the odd cone \(r>4h\) at \(r_h\). | Green. The exact coefficient is \(A_\rho=C-E_N\), where \(E_N\) has \(4h<r\le r_h\). |
| floor correction price | Count \(O(1+\sqrt h+h/y)\) correction aliases and restore \((hr)^{-3/4}\). | Green. The complete unscaled correction is \(O_{\rho,V}(\log X)\). |
| dyadic support and small \(m\) | Use disjoint powers-of-two blocks through \(M_*=C_VN/R^2\), including \(M=1\) and the terminal truncation. | Green. No growing small block is dropped. |
| nearest-integer endpoints | Exclude half-integer ties and define the cell with the lower boundary included. | Green. \(4Nm\) cannot be an odd square. |
| cell width and multiplicity | Compute \([(k-1/2)^2/N,(k+1/2)^2/N)\). | Green. Its length is \(2k/N\ll R^{-1}<1\), so it contains at most one integer \(m\). |
| quadratic-congruence roots | Audit odd primes, \(p=2\), odd valuations, zero roots, and CRT. | Green. \(\rho_N(j)\ll_\varepsilon N^\varepsilon|j|^{1/2}\). |
| \(k<N\) injection | For fixed \(j\), recover \(m=(k^2-j)/N\) and keep the effective \(k\)-range. | Green. The map injects into roots modulo \(N\). |
| microscopic near radicals | Count \(0<|j_m|\le\sqrt M\) and restore \(m^{-3/4}\tau(m)\). | Green. Each block is \(O_\varepsilon(X^\varepsilon)\), and all blocks remain target-safe after epsilon renaming. |
| exact radicals | Write \(N=Du^2\), \(D\) squarefree, and solve \(Nm=\square\). | Green. Exactly \(m=Dt^2\), with total unscaled mass \(O_\varepsilon(D^{-3/4}X^\varepsilon)\). |
| wider-cell extrapolation | Replace \(\sqrt M\) by \(J\) in the root count. | Green obstruction. The ledger is \(M^{-3/4}J^{3/2}X^\varepsilon\), so this method reaches target scale only at \(J=\sqrt M\). |
| \(2\)-adic divisor pairing | Write \(m=2^\nu n\), \(n\) odd, and swap the odd factors \(d,r\). | Green. The two exact far masks are disjoint and the swapped sector equals \(\chi_4(n)A_\nu(n)\). |
| complete-fibre comparison | Add the first far, swapped far, and neither-far sectors. | Green obstruction. \(\sigma_{\chi_4}=(1+\chi_4(n))A_\nu+B_\nu\); negative-character fibres are invisible, while positive-character fibres return \(r_2/4\) plus a central band. |
| prime and prime-square controls | Test \(p\equiv3\pmod4\) and the accepted \(p^{2a}\), \(p\equiv1\pmod4\), fibres. | Green. \(A_0(p)=-1\) with complete and central terms zero; \(A_0(p^{2a})=a\), \(\sigma=2a+1\), \(B=1\). |
| raw capacity direction | Price complete radial mass, a central rectangle, and the \(h=1\), \(r\equiv3\pmod4\) far incidences. | Green only as raw \(\ell^1\) capacity \(R^{1/2+o(1)}\). A grouped or signed lower-bound inference is rejected. |
| cone quarter mode | Separate even and odd \(h\) in \(\sum_{m\le M}C(m)e(m/4)\). | Green. Odd rows give \(i\chi_4(h)\), hence \(i\pi M/8+O(M^{1/2})\). |
| exact-mask quarter mode | Count the unweighted floor correction for \(M\le c_0y\). | Green. The correction is \(O(M^{3/4})\), so the exact coefficient retains the same linear main term. |
| weighted quarter mode | Abel-sum the exact partial sum against \(m^{-3/4}\). | Green. The main coefficient is \(i\pi/2\), with \(O(\log M)\) error. |
| coefficient variation | Sum by parts against the bounded partial sums of \(e(m/4)\). | Green after repair. Linear variation holds only for \(M_0(\rho,c_0)\le M\le c_0y\), not for every small \(M\). |
| plateau and scalar direction | Choose \(c_0\) inside \(V_{\rm low}=1\) and compare \(e(m/4)\) with \(e(\sqrt{Nm})\). | Green obstruction only. The bad Fourier mode is literal but is not a fixed-centre scalar lower bound. |
| smooth ratio transition | Smooth \(r/(4h)=1\) over relative width \(H^{-1/2}\). | Green. \(H\) heights, \(O(\sqrt H)\) aliases each, and weight \(H^{-3/2}\) cost \(O(1)\) per block. |
| sharp Perron tail | Resolve the nearest odd ratio \(1+O(H^{-1})\). | Green obstruction. A sharp truncation needs \(T\gg H\); only smoothing licenses bandwidth \(H^{1/2}X^\varepsilon\). |
| double-Mellin signs | Derive the factor before and after \(t\mapsto-t\). | Green. It is \(4^t\zeta(s-t)L(s+t,\chi_4)\), equivalently \(4^{-t}\zeta(s+t)L(s-t,\chi_4)\). |
| Robert--Sargos source | Distinguish separated smoothing from a direct exact joint mask. | Green after source repair. The respective unscaled bounds are \(R^{1/2+\varepsilon}\) and \(R^{3/4+\varepsilon}\). |
| Sargos--Wu source | Distinguish genuine Theorem 9 from the adjacent general-domain lemma. | Green after source repair. The separated theorem admits the phase but gives \(R^{2/5+\varepsilon}\); the joint-domain lemma excludes \(\alpha+\beta-1=0\). |
| rowwise exponent pair | Apply the TTY pair \((89/1282,997/1282)\) with the actual row length and weight. | Green but insufficient: \(R^{267/641+\varepsilon}\). |
| complete radial source | Audit coefficient, phase combination, truncation, and outer factor in Popov/Li--Yang. | Green obstruction. The radial cosine gives only \(R^{4\theta_*-1+\varepsilon}\); it does not control the incomplete coefficient or an individual complex branch. |
| shifted-\(L\) moments | Track product height \(U\asymp R^3\), ratio shifts \(U^{1/6}\), kernel \(L^2\)-mass, and absolute-value placement. | Green obstruction. Even an ideal shifted mean square through Cauchy gives \(R^{1+\varepsilon}\), not \(R^\varepsilon\). |
| canonical self-return | Transform \(\sqrt{Nm}-mz/4\). | Green obstruction. The critical point is \(4N/z^2\) and the critical value \(N/z\); a second transform returns the original phase. |
| nonresonant complement | Prove the survivor with \(|k_m^2-Nm|>\sqrt M\) at \(X^\varepsilon\). | Open. Modulus retains the \(R^{1/2+o(1)}\) excess; no accepted theorem closes it. |
| unsquared direction | Restore the Round-140 factor \(N^{1/4}\asymp R\). | Green. Removed families cost \(O(RX^\varepsilon)\); no square identity, cross-term bound, or residual deletion follows. |
| downstream scope | Audit lower GAR, direct M1, M9-M1, M2, endpoint, M9, bridge, target, and exponents. | Green. Every downstream owner and both exponent records remain unchanged. |

## Independent seam reviews

| Review | Assigned seam | Final outcome |
|---|---|---|
| discovery post-unmask cone/quarter audit | Least-odd floors, correction sign and price, quarter-mode constants, variation range, plateau, scalar direction | Green after restricting the variation statement to sufficiently large \(M\) and repairing review hygiene. |
| source post-unmask phase/pairing audit | Cell endpoints and roots, dyadic weights, exact radicals, \(2\)-adic pairing, raw capacity, target direction | Green. The candidate explicitly retains raw-incidence wording and rejects a grouped/signed lower bound. |
| blind post-unmask source/Mellin audit | Ratio smoothing, Mellin signs, primary-source hypotheses, \(R\)-powers, cosine direction | Green after correcting the Robert--Sargos placement and the Sargos--Wu theorem attribution. |

No reviewer certifies its own principal discovery.  Every requested
candidate repair is present in the final candidate and conductor
adjudication.

## Exit-gate decision

- target_bound: not met;
- strict_near_resonance_reduction: not used as the terminal label,
  because the proved target-safe set is the microscopic resonant set
  and the owner-sized nonresonant complement remains;
- incomplete_fibre_dispersion_no_go: met.

The first open estimate is

\[
\sum_M\sum_{\substack{m\in\mathcal I_M\\|k_m^2-Nm|>\sqrt M}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
\ll_\varepsilon X^\varepsilon.
\]

## Resource and artifact controls

- Analytical/algebraic/source work: 100 percent.
- Numerical or symbolic experiments: none.
- Centre averages, positive separated energies, arbitrary arrays, and
  desired circle estimates: none.
- Primary reports: three of three present, each with exactly seven
  numbered sections.
- Post-unmask reviews: three of three present, each with exactly seven
  numbered sections and a final green verdict.
- Candidate and conductor adjudication: present with exactly seven
  numbered sections.
- Artifact hygiene: all 16 campaign files have zero standalone carriage
  returns, forbidden controls, replacement characters, trailing
  whitespace, conflict markers, or delimiter imbalances.
- State Patch: dry-validated before application; 2 creates, 4 updates,
  20 rejects, and 8 no-change decisions applied; resulting graph
  validates.
- Repository validation: campaign and all JSON-backed state parse;
  six of six unit tests pass; bytecode compilation succeeds; diff
  checking has line-ending notices only.

## Downstream status

The Round-140 far scalar is now floor-free and has its exact plus
microscopic nearest-square cells removed at target cost.  The remaining
fixed-centre nonresonant cone scalar is still open.  Lower GAR, both
direct blockwise M1 parents, M9-M1, hard TOP, BAL, all required UNBAL
owners, M9-M2, endpoint uniformity, M9, the conditional bridge, and the
quarter target remain open.

The strongest internally proved exponent remains \(1/3\).  The
separately audited external Li--Yang exponent remains

\[
{3292+25\sqrt{1717}\over13762}
=0.3144831759740614\ldots.
\]

The applied State Patch produces graph SHA-256
de02111a1831d30da33c9f4b2d4a549efa1942dcdc32b5d829e671f6ad5e0e76.
