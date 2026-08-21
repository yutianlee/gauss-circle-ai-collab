# Round 111 conductor controls

Campaign: m9-m2-adjacent-ray-transport-commutator

Starting graph SHA-256:
c93f14d6790341b792b54bbaa7ccb96c211741d666729f08addc80fb91d1b759

| Gate | Result | Evidence |
|---|---|---|
| Exact parity high-pass | Green. \(2C=\sum(-1)^q(I-S)f(q)\) for finite zero-extended rows. | blind report; high-pass review |
| One orientation and endpoint | Green. One forward difference and one outer \(2\Re\); truncated sums retain \(f(Q+1)\). | blind report; high-pass review |
| Signed target versus stronger norms | Green separation. Variation, maximal, row energy, modulus, and Gram require bridges. | blind report |
| Phase-preserving transport | Green. \(T_q(x,k)=(\lambda_qx,k/\lambda_q)\) preserves phase, \(kx\), and \(\Lambda/k\). | discovery and hostile reports |
| Jacobian | Green. The two-dimensional determinant is exactly one. | both transport reports |
| Discrete sampler | Green after repair. The exact pullback is \(\lambda\sum\delta_{\lambda n}\). | hostile report; transport review |
| Rational/irrational comb | Green route no-go. Total variation on a \(K\)-interval is \(\asymp K\) for every \(\lambda\ne1\). | hostile report |
| Common-band carrier | Green route no-go. Its displacement is \(\asymp JL/A\); no modular gap is inferred. | discovery report |
| Endpoint and physical slabs | Green ownership, open estimate. Widths are \(J/A\) and \(L/D\). | both reports |
| Ceiling | Green. The raw jump is \((g-\chi_4(gb))/2\). | both reports |
| Jump one-count | Green algebraically through the first-failure partition. | discovery report |
| Coprimality and Möbius | Green algebraically; no saving. Odd divisor progressions preserve parity but jump internally. | both reports |
| Floors, stars, terminal and metric centre | Green in the inherited tagged partition; none is deleted. | both reports |
| Empty, singleton, \(q=1\), cone edge | Green controls. They remain birth/death atoms. | all reports |
| Polylogarithmic rows | Green as prior scope only; no polynomial range. | discovery report |
| Square, Pell, fourth powers and near centres | Green method controls; no lower bound. | both reports |
| False coefficients | Green as coefficient-blind falsifiers only. | all reports |
| Endpoint absolute capacity | Red as a proof route: \(L^2\sqrt\kappa\), \(\kappa\ge D\). | discovery report |
| Full actual signed commutator | Open. No bound, subrange, or actual lower obstruction. | synthesis |
| Primary-source dependency | Green. No external theorem invoked. | hostile report |
| Downstream scope | Green. Gram, hard cone, smooth packets, M9 components, endpoint, exponent open. | synthesis |
| Artifact hygiene | Green. Three reports have seven sections, UTF-8/LF, balanced TeX, no controls or trailing whitespace. | conductor validation |

Decision rule: promote only the exact high-pass, one-count, transport,
sampler, slab, and coefficient-blind equal-capacity obstruction. Do not
promote the signed estimate, an actual-symbol lower bound, a polynomial
subrange, or a downstream theorem.

