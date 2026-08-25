# Round 149 conductor controls

- Campaign: \`m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate\`
- Round: 149
- Starting graph SHA-256: \`8f1912eeda4843718379213478a839b30fb2694d6b169ac8decbab5ca3561176\`
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| exact_progression_coefficient_collapse | GREEN.  The odd-prime local table gives \(C_d(n)=\mu(u)\mu(v)\) exactly on \(n=uv^2\), \(u\mid d_{\mathrm o}\), \(\mu^2(uv)=1\), \((v,d)=1\), and zero otherwise. |
| p_divides_d_square_local_cancellation | GREEN.  At odd \(p\mid d_{\mathrm o}\), the two exponent-two cells have signs \(-1,+1\) and cancel.  The prime \(2\) is absent even when \(d\) is even. |
| finite_nonempty_progression_prefix_indicator | GREEN.  The literal \(0\)-\(1\) indicator \(\kappa_{d,U}(n)\) remains inside every lcm and lift sum; no smoothing or monotonicity is used in the norm. |
| gcd_lift_character_phase_profile_recombination | GREEN.  The finite bijection \(\ell=gL,\ q=gq_0,\ (L,q_0)=1\) cancels \(\chi_4(g)^2\), leaves phase \(NdL/q_0\), and retains \(C_d(gL)\kappa_{d,U}(gL)/g\) exactly. |
| truncated_lift_square_norm | GREEN.  The cube-free parameterization gives \(\sum_L|B_{d,U}(L)|^2/L+\sum_L|B_{d,U}(L)|/L\ll X^\varepsilon\) for every exact prefix. |
| joint_d_energy_target_normalization | GREEN as a reduction, OPEN as an estimate.  Cauchy only in \(d\) sends \(\sum_d|G_U(d)|^2\ll R^2DX^\varepsilon\) to \(|\mathcal T|\ll RDX^\varepsilon\). |
| literal_equal_cell_diagonal | GREEN.  It costs \(DQX^\varepsilon\), hence is target-safe because \(Q\ll R^2\). |
| offdiagonal_determinant_and_near_collision | GREEN as an exact classification, OPEN as a bound.  The determinant, centered integer \(k\), nonzero collar, and generic complement remain literal. |
| N_dependent_exact_alignments | GREEN.  Common-denominator divisor classification and an independent reduced-phase grouping both prove that all exact phase classes, including distinct cells, are target-safe. |
| common_divisor_and_imprimitive_denominator | GREEN.  Writing \(q_i=Hr_i\) removes only one factor \(H\); no squarefreeness or primitive-denominator shortcut is used. |
| d_dependent_arithmetic_coefficient | GREEN as the first obstruction.  The closed \(B_{d,U}\) formula, exact prefix, and profile show genuine joint \(d\)-cell dependence. |
| source_theorem_energy_match | GREEN as a no-match audit.  Montgomery--Vaughan requires one common coefficient vector; the progression, inverse-square, Kloosterman-fraction, and partially fixed-modulus sources have different coefficients, phases, averages, diagonals, or ranges. |
| all_M_D_E_Q_power_ledger | GREEN.  Diagonal, exact alignment, small reduced denominator, positive triangle, optimistic unwrapped spacing, and fully wrapped spacing are separated for every \(M\leq R^2\). |
| D1_L1_qdividesN_prime_and_prefix_controls | GREEN/OPEN split.  \(q_0\mid N\) is divisor-safe.  \(D=1,L=1\) remains a compulsory signed reciprocal-sum test; the second-derivative powers are used only as a conditional bounded-variation diagnostic. |
| H_interface_and_transform_self_return | GREEN as a mismatch.  The cube-free \(L\) is not termwise the powerful \(H\)-index, and a second transform supplies no saving without a new signed estimate. |
| Round138_cross_tge2_and_downstream_scope | GREEN.  The independent cross owner, every \(t\geq2\) layer, lower GAR, M9--M1, M9--M2, endpoint, M9, bridge, quarter target, and exponents remain separate. |

## 2. Exact compression and norm controls

For squarefree \(d\), let \(d_{\mathrm o}=d/(d,2)\).  The accepted
local table is

| prime case | exponent \(0\) | exponent \(1\) | exponent \(2\) |
|---|---:|---:|---:|
| odd \(p\nmid d_{\mathrm o}\) | \(1\) | \(0\) | \(-1\) |
| odd \(p\mid d_{\mathrm o}\) | \(1\) | \(-1\) | \(-1+1=0\) |

Thus

$$
 C_d(n)=
 \begin{cases}
  \mu(u)\mu(v),&
  n=uv^2,\ u\mid d_{\mathrm o},\
  \mu^2(uv)=1,\ (v,d)=1,\ u,v\ {\rm odd},\\
 0,&\text{otherwise}.
 \end{cases}
$$

The exact compressed coefficient and row are

$$
 B_{d,U}(L)=\sum_g\frac{C_d(gL)\kappa_{d,U}(gL)}g,
$$

$$
 G_U(d)=
 \sum_{\substack{L,q_0\ {\rm odd}\\(L,q_0)=1\\q_0\asymp LQ}}
 \chi_4(Lq_0)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q_0)e(NdL/q_0).
$$

If \(L=ts^2\), \(a=(t,d_{\mathrm o})\), and \(r=t/a\), then
\(B_{d,U}(L)=0\) when \((s,d_{\mathrm o})>1\); otherwise

$$
\begin{aligned}
 B_{d,U}(ts^2)
 ={}&\frac{\mu(a)\mu(r)\mu(s)}r
 \sum_{u'\mid d_{\mathrm o}/a}\frac{\mu(u')}{u'}\\
 &\times
 \sum_{\substack{v'\ {\rm odd\ squarefree}\\
                  (v',d_{\mathrm o}rs)=1}}
 \frac{\mu(v')}{(v')^2}
 \kappa_{d,U}\!\left(au'(rsv')^2\right).
\end{aligned}
$$

The bound \(|B_{d,U}(ts^2)|\ll X^\varepsilon/r\) proves

$$
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 +\sum_L\frac{|B_{d,U}(L)|}{L}
 \ll X^\varepsilon,
 \qquad
 \sum_L|B_{d,U}(L)|
 +\sum_L|B_{d,U}(L)|^2
 \ll\sqrt E\,X^\varepsilon.
$$

Every bound is uniform in an arbitrary finite \(0\)-\(1\) prefix.

## 3. Diagonal, alignment, and near-collision controls

The literal diagonal is

$$
 \mathscr E_{\rm diag}
 \ll Q\sum_{d\asymp D}\sum_L
 \frac{|B_{d,U}(L)|^2}{L}
 \ll DQX^\varepsilon
 \leq R^2DX^\varepsilon.
$$

For two reduced cells, put

$$
 \Delta=L_1q_2-L_2q_1,\qquad
 q_1=HA,\quad q_2=HB,\quad (A,B)=1,\qquad
 \delta=L_1B-L_2A.
$$

Then \(\Delta=H\delta\),
\((\delta,A)=(\delta,B)=1\), and a distinct exact alignment obeys

$$
 HAB\mid N\delta,\qquad
 AB\mid N,\qquad
 H\mid (N/AB)\delta.
$$

For fixed \(L_1,L_2\), this has divisor multiplicity
\(O_\varepsilon(X^\varepsilon)\); the weighted \(\ell^1\) norm gives
a target-safe exact off-diagonal.  Independently, grouping cells by
the reduced phase \(NL/q_0\bmod1\) gives the robust bound
\(O_\varepsilon(QX^\varepsilon)\) per row and
\(O_\varepsilon(DQX^\varepsilon)\) in the energy.

For the nonexact part, write

$$
 q_i=hr_i,\qquad (r_1,r_2)=1,\qquad
 \delta=L_1r_2-L_2r_1,
$$

and choose \(k\) so that

$$
 \rho=N\delta-khr_1r_2,\qquad
 |\rho|\leq \frac{hr_1r_2}{2}.
$$

The first open collar is

$$
 0<|\rho|\leq\frac{hr_1r_2}{D}.
$$

The exact \(d\)-kernel contains both \(B_{d,U}\)'s and both moving
profiles.  It is not replaced by a geometric kernel or by an
arbitrary coefficient matrix.

## 4. Source and false-analogue controls

1. Montgomery--Vaughan, *The large sieve* (1973), Theorem 1 and
   Lemma 1, were checked in the primary source.  Both primal and dual
   forms retain one common coefficient vector.  They do not authorize
   a vector \(A_d(L,q_0)\) that changes with the outside row \(d\).

2. The pointwise squarefree-progression and fixed-modulus variance
   ranges lie within the already target-safe reduced-denominator
   stratum \(q_*\leq R\), and their coefficient is the pure
   \(\mu^2(d)\), not the literal moving coefficient.

3. Bettin--Chandee and Wright require independent coefficient
   sequences and an inverse Kloosterman-fraction or fixed-residue
   convolution structure.  The formal inverse dictionary determines
   one variable jointly from \((L,q_0)\), so separability fails before
   their numerical bounds can be applied.

4. Raw rational spacing and optimistic determinant spacing were
   recorded only as illegal fixed-vector diagnostics.  Their adverse
   capacities are not lower bounds for the actual signed energy.

5. The initial \(D=1\) second-derivative statement was rejected because
   boundedness alone does not imply the required profile variation.
   The repaired candidate states the variation as an additional
   diagnostic hypothesis and draws no unconditional estimate from it.

## 5. Review gate

The initial blind conductor review returned RED solely because the
\(D=1\) weighted second-derivative diagnostic had not stated the
required variation hypothesis.  The candidate was repaired to make
that hypothesis explicit, conditional, and unused in the promoted
mathematics.  The terminal blind repair review is:

- \`blind_conductor_round149_math_review_v2.md\`: GREEN.

The other terminal reviews are:

- \`source_conductor_round149_final.md\`: GREEN;
- \`discovery_source_conductor_round149_review.md\`: GREEN.

They authorize only the exact compression, coefficient norms,
target-safe literal diagonal and exact alignments, and the scoped
fixed-vector/source no-go.  They do not authorize the joint energy, a
strict range, the scalar target, or any downstream theorem.

## 6. Validation and state mutation

Before graph mutation:

- campaign manifest validation: PASS;
- State Patch validation against starting graph
  \`8f1912eeda4843718379213478a839b30fb2694d6b169ac8decbab5ca3561176\`:
  PASS;
- graph, active campaign, round plan, ledger, and State Patch parsing:
  PASS;
- conductor candidate equation check: 32 distinct tags, no duplicate
  tag, and 32 balanced display pairs;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- complete 18-file Round-149 byte scan: strict UTF-8, LF only, no
  forbidden C0 bytes, no U+200E or replacement characters, no BOM,
  and every file ending in LF;
- Round-149 whitespace diff check: PASS.

The validated State Patch applied:

- 2 obligations created;
- 5 obligations updated;
- 12 false inferences rejected;
- 8 global obligations recorded unchanged.

Resulting graph SHA-256:
\`b6c5ee5b0d51d347876b389c05c78596c069b190af715d297bd937701ea893b6\`.

Post-application graph and completed-campaign validation,
structured-state parsing, Python compilation, all 6 unit tests,
equation checking, Round-149 whitespace checking, and the complete
18-file byte scan all pass.  The analytical allocation was 100
percent.
