# Round 147 conductor controls

- Campaign: m9-m1-lower-cone-t1-squarefree-voronoi-gate
- Round: 147
- Starting graph SHA-256: 1dc79cf41e0dea8888341e944c5d0bf025d87f22cfaa282da34fcd10eecd04f5
- Allocation: 100% analytic, algebraic, and source verification; 0% numerical

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| t1_exact_extraction_and_prefix_target | GREEN as an interface. The literal weighted face and sufficient \(M^{3/4}\) raw prefix target are retained; the target estimate is not claimed. |
| squarefree_coprime_even_odd_character_and_cone | GREEN. The exact \(2^\nu n\) coefficient, squarefree support, parity, strict cone, and prime/even-prime checks pass. |
| divisor_pairing_chi4_sector_ledger | GREEN. The positive-total-character complete sector and negative-total-character antisymmetric tail both remain. |
| ratio_Mellin_Euler_product_p2_and_H | GREEN. The local partition constants, radial twist, unitary order, original Euler domain, \(H_2\), odd factors, prime-power coefficients, and powerful support pass. |
| target_safe_cone_collar_and_ratio_bandwidth | GREEN as a target-sized reduction. The \(\sqrt D\) collar costs \(D^{3/2}=M^{3/4}\) raw, the smooth bandwidth is \(D^{1/2}X^\varepsilon\), and hard Perron still needs height comparable with \(D\). |
| shifted_zeta_L_functional_equations_and_poles | GREEN at fixed order. The coefficient is \(\zeta(w+z)L(w-z,\chi_4)\), with one pole at \(w=1-z\). |
| level_four_generalized_divisor_Voronoi_kernel | GREEN at fixed order. The scalar is \(\pi4^z\), the argument is \(2\pi\sqrt{mx}\), and every \(J/Y/K\) branch is retained. |
| uniform_complex_order_and_Bessel_asymptotics | OPEN and excluded. No source or derivation supplies the needed growing-order derivative, transition, off-resonant, and moving-prefix bounds. |
| H_powerful_coefficients_tail_and_signed_aggregation | Coefficient and physical-support ledger GREEN; signed saving OPEN. The finite \(k\le K_F\) convolution is exact, and every \(k>K_F\) zero pair cancels per \(k\). |
| dual_resonance_centre_width_amplitude_and_off_resonance | Fixed-order centre, width, and amplitude GREEN: \(m=kN+O(k\sqrt{N/M})\), raw one-term size \(M^{3/4}/(kR)\). Uniform complementary ranges remain open. |
| all_M_D_E_capacity_and_R4over3_barrier | GREEN as a scoped adverse capacity. Absolute \(H\)-aggregation loses \(R^{1/3}\) at \(M=R^{4/3}\) and \(R^{1/4}\) at \(M=R^2\); no lower bound is inferred. |
| clipped_prefix_profile_terminal_endpoint | GREEN as a reduction. Short prefixes and peeled \(\sqrt M\) endpoint collars cost \(O(M^{1/2+\varepsilon})\) raw; transformed seminorms remain in the open uniform seam. |
| t1_D1_prime_even_and_slow_family_controls | GREEN. \(D=1\), primes, even squarefree inputs, \(N=sL^2\), \(N=sL^2+1\), and \(m=kN+j\) are retained only as exact or slow-phase controls. |
| individual_positive_direction_and_fixed_centre | GREEN. The individual \(+\) physical phase and \(N=\lfloor X\rfloor\) remain fixed; only the negative Bessel branch resonates. |
| Round141_142_144_self_return_and_zero_mode | No bypass. The hard zero residue and smooth zero Fourier mode remain, and no second termwise transform is counted as a saving. |
| Round138_cross_and_downstream_scope | GREEN. The independent cross owner, \(t\ge2\), lower GAR, M1, M2, endpoint, M9, bridge, target, and exponents remain separate. |

## 2. New exact algebra and reciprocal controls

1. The corrected identity

   \[
   \mathscr K_p
   =\frac{1+a+b}{(1+a)(1+b)(1-ab)}
   =1+\frac{a^2b+ab^2+a^2b^2}
   {(1+a)(1+b)(1-ab)}
   \]

   proves the stated \(\mathscr K\) convergence domain. The coarse
   fourth-order remainder is not used.

2. The bare reciprocal lemma is proved only for \(Q\le N/4\). The
   project has \(Q\le R^2\ll N\), so its divisor-count proof is legal.

3. Expanding \(\mu^2(d)\) and taking triangle gives
   \(QD^{1/2}+D\). This is recorded as the output of that proof
   placement, not as a lower bound for the signed sum.

4. The \(R^{4/3}\) crossover comes from
   \(\min(M^{1/4},R/\sqrt M)\), not from the reciprocal lemma alone.

## 3. Review gate

The first source, arithmetic, and hostile power reviews all returned
REVISE with exact local corrections. The corrected candidate then
received:

- source_conductor_round147_final_green.md: GREEN;
- blind_conductor_round147_final_green.md: GREEN;
- discovery_conductor_round147_final_green_v2.md: GREEN.

The terminal reviews authorize only the exact fixed-order reduction
and the scoped method no-go. They do not authorize the growing-order
estimate, signed correlation, separate \(t=1\) target, strict top
range, downstream theorem, or exponent change.

## 4. Pre-mutation validation

The following checks completed successfully before graph mutation:

- campaign manifest validation: PASS;
- State Patch validation against the starting graph: PASS;
- active campaign, round plan, ledger, graph, plan, and State Patch
  JSON parsing: PASS;
- Python compile check for math_collab: PASS;
- unit tests: 6/6 PASS;
- complete Round-147 byte scan after LF normalization:
  0 carriage-return bytes, 0 forbidden control bytes, and
  0 U+200E format characters;
- git diff whitespace check for the Round-147 directory: PASS.

## 5. State-mutation result

The validated State Patch was applied with:

- 2 obligations created;
- 5 obligations updated;
- 9 false inferences rejected;
- 8 global obligations recorded unchanged.

Resulting graph SHA-256:
`bb43abb1e0fbd719b18ebf91f4c7e477bf18e46e7b5225faaa88a7fb38d31352`.

Post-application graph validation, Python compilation, all 6 unit
tests, structured-state parsing, Round-147 whitespace checking, and
the complete 21-file byte scan all passed. The byte scan found 0
carriage-return bytes, 0 forbidden control bytes, and 0 U+200E format
characters.
