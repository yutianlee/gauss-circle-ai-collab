# Next Round Prompts

Generated after round 6 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_006/judge/judge-006.md`.

## For A1

Target obligations: `H4-source-audit`, `H4-Phi-regularity`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-local-fourth-moment-kernel`, `M9-M2-subcoherence-window-multiplier`, `M9-M2-LFM-pointwise-equivalence`, proof-draft maintenance.

Objectives:

1. Physically draft or commit `sources/vaaler_1985.md`. Include:
   - bibliographic data and DOI;
   - local PDF path;
   - Theorem 6 equation (2.28);
   - Section 7 equations (7.1)--(7.3);
   - Theorem 18 equations (7.13)--(7.17);
   - coefficient sign;
   - Fejer normalization;
   - residual constant;
   - floor-compatible endpoint convention;
   - $\Phi$ regularity;
   - the M2 single-parity support check from the $\rho=1,3$ difference.

2. Insert into `state/best_proof_draft.md`:
   - H1--H3;
   - H4 as source-audit-dependent;
   - R5 positive-Fejer product-count proof;
   - M1/M2 definitions;
   - beta algebra;
   - raw two-sided, complex-weight cosine, and real-weight paired M2 formulas;
   - fourth-moment numerator $N$;
   - local kernel;
   - endpoint degeneracy;
   - subcoherence-window multiplier and LFM-pointwise equivalence;
   - DP-0 through DP-3;
   - NF-1/NF-2;
   - reduced-paired bound;
   - URES residual target.

3. Write a proof-draft note explaining that `(LFM)` is no longer the primary relaxed route: coherence windows provide no power-saving multiplier, and endpoint control must come from signed pointwise or global-moment/large-value propagation.

4. Keep `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, `GC-target`, and `H4` unpromoted.

Exploratory allocation: compare three route maps in one page:
- URES exact-resonance route;
- graded global near-collision/moment route;
- SPD or sign-preserving Poisson endpoint route.

For each, state the exact theorem needed and one falsification test.

## For A2

Target obligations: `M9-M2-unpaired-residual-URES`, `M9-near-collision-taxonomy`, `M9-M2-sign-preserving-poisson-voronoi-route`.

Objectives:

1. Attack URES only. Do not re-prove denominator-paired, pair-swapped, or fraction-matching subfamilies.

2. Use NF-2 explicitly. For each reduced value $r=\mu/Q$, bound the possible reduced fractions $x_1=p_1/q_1$ with $x_3=r-x_1$ and $q_3\le2D$ using

$$
q_3\ge \frac{Qq_1}{\gcd(Q,q_1)^2}.
$$

3. Produce one of:
   - a proof of $\sum_{r\ne0}R(r)^2\ll D^2X^\epsilon$;
   - a lower-bound family exceeding the budget;
   - a rigorous reduction to a smaller divisor-sum problem with all lifts and beta weights stated.

4. If using the Poisson/B-process route, supply the exact transformed object:
   - sign of the dual variable;
   - stationary point;
   - amplitude;
   - boundary terms;
   - $k=0$ terms;
   - dual range $m\asymp hX/D^2$;
   - the first signed theorem that would imply `M9-M2`.

5. Do not label any unpaired mass bound `derived_under_assumptions` unless all lifts, signs, reduced denominators, overlaps, and dyadic endpoints are handled.

Exploratory allocation: write one sign-preserving endpoint lemma for the top block $D\asymp X^{1/2}$ using the expansion $d=\lfloor X^{1/2}\rfloor+m$, but keep it `proposed` unless fully proved.

## For A3

Target obligations: `M9-fourth-moment-enumeration`, `M9-regression-raw-vs-paired`, `M9-M2-local-fourth-moment-LFM` diagnostics, `M9-M2-reciprocal-SPD-route`.

Objectives:

1. Execute, not plan. Required deliverables:
   - script path and full script contents;
   - exact command lines;
   - Python version and package versions;
   - `python -m py_compile` result;
   - precision log;
   - CSV schema;
   - generated tables;
   - report.md;
   - pass/fail assertions.

2. Use exact integer arithmetic for $N$ and exact rational reduction for $h_i/d_i=p_i/q_i$.

3. First required tables:
   - DP parity/no-small-nonzero-$N$ check;
   - DP thin mass compared to $C_0D\log^2(2H)$;
   - URES residual enumeration including $(6,10,15,5)k$;
   - $R(r)^2$ concentration;
   - reduced-paired versus residual exact mass.

4. Formula regression:
   - raw two-sided M2;
   - complex-weight cosine pairing;
   - real-weight $\operatorname{Re}B_h$ pairing;
   - deliberate failure of $\operatorname{Re}B_h$ for complex weights.

5. Local-window diagnostics:
   - compute $\max \delta|\lambda|$;
   - compare $\delta^{-1}\int_I |S_2|^4$ to local sup;
   - include $D=X^{1/4},X^{3/8},X^{1/2}$.

6. Before running any diagnostic, fix the $d=7$ imaginary-part sign, the complex-weight relation $B_{-1}=(1+i)\overline{\Sigma}$, and the envelope $\sup_I |S_2'|\ll H_D$.

7. SPD diagnostics:
   - compute $P(D,H;X)$;
   - compare true beta signs, unsigned signs, random signs, and adversarial signs.

All outputs remain `diagnostic_only`.

## For A4

Target obligations: `M9-M2-DP-near-collision-bound`, `M9-M2-coprime-rigidity-normal-form`, `M9-M2-NF-participation-rigidity`, `M9-M2-unpaired-reduced-paired-bound`, `M9-M2-unpaired-residual-URES`, `M9-M2-reciprocal-SPD-route`.

Objectives:

1. Write validator-ready statements and proofs for:
   - DP-0 parity;
   - DP-1 thin-band emptiness;
   - DP-2 thin DP mass;
   - DP-3 full DP total mass;
   - exact H4 dependency split.

2. Insert NF-1 and NF-2 in lemma-bank form. NF-2 must include all definitions:

$$
g=\gcd(Q,q_1),\quad
\widehat Q=Q/g,\quad
\widehat q_1=q_1/g,\quad
M=\mu\widehat q_1-p_1\widehat Q.
$$

3. Verify overlap bookkeeping for U-2, SS, anti-paired, and fraction-matching coverage of all exact $N=0$ tuples with reduced-denominator multiset $\{q,q,q',q'\}$.

4. Attack URES jointly with A2:
   - attempt a proof of $\sum_{r\ne0}R(r)^2\ll D^2X^\epsilon$;
   - or produce a counterexample/lower-bound family;
   - or reduce it to a named divisor-sum inequality.

5. Develop SPD only as backup. State the exact theorem required for reciprocal points $\theta_d=X/(4d)$ and give A3 a falsification threshold.

Exploratory allocation: formulate a global-moment/large-value propagation map for sub-endpoint ranges $D\le X^{1/2-\eta}$, with all assumptions marked as proposed or diagnostic unless proved.

## Round Assessment

Round 6 produced real proof-graph progress, but not endpoint proof.

Agent scores:

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.5 | 7.0 | 9.0 | Strong source-card draft, $\Phi$ regularity, M2 formulas, local kernel, and endpoint degeneracy. Correctly avoided endpoint overclaim. A4's subcoherence result supersedes the endpoint-only framing. |
| A2 | 7.2 | 3.8 | 5.8 | Good terminology separation and useful exploratory Poisson/B-process idea. The unpaired mass bound is not proved, and the nonseparability obstruction is over-scoped if treated as route-closing. |
| A3 | 7.0 | 2.5 | 7.5 | Useful diagnostic architecture and correct diagnostic-only attitude, but no executed artifact. Formula and classifier issues must be fixed before evidence is positive. |
| A4 | 9.0 | 8.0 | 8.5 | Strongest analytic contribution: DP suite, NF-2, subcoherence-window equivalence, reduced-paired exact-resonance bounds, and URES residual definition. Some overlap bookkeeping still needs proof-draft verification. |

Split round scores:

- idea quality: 8/10;
- state evidence: 6/10;
- calibration: 8/10;
- mathematical progress: 5/10.

The proof graph gains narrower lemmas and a better obstruction map. It does not gain `M9-M2`, `M9`, or the final theorem.
