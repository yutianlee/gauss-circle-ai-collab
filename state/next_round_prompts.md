# Next Round Prompts

Generated after round 5 in run `obligation-main`.

Source judge synthesis: `rounds/obligation-main/round_005/judge/judge-005.md`.

## For A1

Target obligations: `H4-source-audit`, `H4`, `R5-Full-reconciliation`, `M9-M2-beta-algebra`, `M9-M2-fourth-moment-average-to-pointwise`, `M9-M2-local-fourth-moment-LFM`, and proof-draft maintenance.

Objectives:

1. Complete or draft `sources/vaaler_1985.md` physically. Include the earlier required data plus the new Round 5 item: a source-card check for the regularity of

$$
\Phi(u)=\pi u(1-u)\cot(\pi u)+u
$$

sufficient to justify freezing $H_D$ across windows of length $\delta=X^{1/2}/D$.

2. Insert into `state/best_proof_draft.md`:
   - H1-H3 statement;
   - H4 statement, still source-audit-dependent;
   - R5 positive-Fejer product-count proof;
   - official M1/M2 definitions;
   - M2 raw two-sided, complex-weight cosine, and real-weight paired formulas;
   - fourth-moment numerator $N$;
   - AP lemma;
   - local fourth-moment hypothesis `(LFM)`;
   - list of open endpoint and unpaired near-collision blockers.

3. Write a short proof-draft note explaining why AP is not a proof of `M9-M2`: it needs `(LFM)` on every interval of length $\delta=X^{1/2}/D$, the local expansion controls $|N|\ll D^5X^{-1/2}$, and the endpoint $D=X^{1/2}$ degenerates.

4. Reconcile terminology:
   - denominator-pattern semi-diagonal;
   - pair-swapped;
   - fraction-matching/fraction-collision;
   - mixed;
   - unclassified.

5. Do not promote `M9`, `M9-M1`, `M9-M2`, `M9-near-collision-taxonomy`, `M9-near-collision-estimate`, or `GC-target`.

Exploratory allocation: compare the absolute unpaired-exact route, the local fourth-moment `(LFM)` route, and the direct signed/SPD route. State for each the exact needed theorem and a one-line falsification test.

## For A2

Target obligations: `M9-near-collision-taxonomy`, `M9-M2-N0-diagonal-core-bound`, `M9-M2-fraction-matching-weighted-bound`, and unpaired exact $N=0$ mass.

Objectives:

1. Do not re-prove denominator-paired exact resonance or pair-swapped exact resonance.

2. Reconcile terminology. If the official semi-diagonal family is

$$
d_1=d_3,\qquad d_2=d_4,\qquad d_2(h_1+h_3)=d_1(h_2+h_4),
$$

then either prove this exact denominator-pattern family or state explicitly that Round 5's fraction-matching proof is a different subfamily.

3. Write one proof-draft-ready lemma for an unpaired exact $N=0$ family. Choose one:
   - an upper bound $\ll D^2X^\epsilon$ for a well-defined unpaired class; or
   - a lower-bound construction showing a larger scale; or
   - a normal-form reduction that leaves a smaller explicit subproblem.

4. Repair or discard the continuous $L^4$ route. If repaired, use an integer frequency based on the cleared numerator $N$ and state the exact kernel. Do not use rational-frequency orthogonality over $[0,1]$.

5. Keep `M9`, `M9-M2`, and `M9-near-collision-taxonomy` open.

Exploratory allocation: propose one sign-preserving analytic inequality that would exploit $\chi_4(h)$ without Cauchy erasing the sign.

## For A3

Target obligations: `M9-regression-raw-vs-paired`, `M9-fourth-moment-enumeration`, `M9-M2-local-fourth-moment-LFM`, and signed-vs-unsigned/SPD diagnostics.

Objectives:

1. Materialize and execute the diagnostic bundle. Required outputs:
   - script path and full script contents;
   - exact command lines;
   - Python version and package versions;
   - `python -m py_compile` result;
   - precision log;
   - CSV schema;
   - generated tables;
   - report.md;
   - pass/fail assertions.

2. Use exact integer arithmetic for $N$ and for all exact $N=0$ classification.

3. Implement and separately test:
   - raw two-sided M2;
   - complex-weight cosine pairing;
   - real-weight paired formula;
   - deliberate failure of $\operatorname{Re}B_h$ for complex weights.

4. Replace placeholder $\Phi$ with the audited Vaaler $\Phi$ once H4 is available. Until then, separate classification results from coefficient-magnitude results.

5. Taxonomy tests:
   - pair-equality;
   - denominator-paired;
   - pair-swapped;
   - official denominator-pattern semi-diagonal;
   - fraction-matching/fraction-collision;
   - mixed;
   - unclassified.

6. Test whether A4's fraction-collision family accounts for the previously unclassified exact mass.

7. Local fourth-moment diagnostics:
   - use $\delta=X^{1/2}/D$;
   - sample many windows;
   - report local fourth moment, global fourth moment, exceptional-window concentration, and the ratio to the AP-derived bound;
   - include endpoint $D=X^{1/2}$.

8. Near-collision diagnostics:
   - compare thin band $|N|\ll D^4/X$ and local fat band $|N|\ll D^5X^{-1/2}$;
   - split denominator-paired and unpaired-denominator cases.

9. Signed-vs-unsigned/SPD diagnostics:
   - true $\beta_h$;
   - unsigned $|\beta_h|$;
   - random signs;
   - adversarial signs;
   - reciprocal spacing statistic $P(D,H;X)$ if feasible.

All outputs remain `diagnostic_only`.

## For A4

Target obligations: `M9-M2-DP-near-collision-bound`, `M9-M2-local-fourth-moment-LFM`, `M9-M2-coprime-rigidity-normal-form`, and unpaired near-collision search.

Objectives:

1. Write validator-ready proofs for:
   - DP parity emptiness with exact dyadic constants;
   - thin DP near-collision mass bound;
   - full DP-total mass bound;
   - dependence on H4/beta odd support.

2. Write the coprime-rigidity normal form in a compact lemma format suitable for `state/lemma_bank.md`.

3. Develop the `(LFM)` obstruction:
   - prove exactly how the local window creates the band $|N|\ll D^5X^{-1/2}$;
   - isolate whether an exceptional-window argument can convert a global fourth moment into `(LFM)` outside a small exceptional set;
   - state why the endpoint $D=X^{1/2}$ still requires separate control.

4. Attack one unpaired near-collision or exact-resonance subproblem using the coprime-rigidity normal form. Provide either a proof, a counterexample family, or a sharply reduced equation.

5. Keep the SPD/sign-preserving route exploratory. State the needed first-spacing statistic and the exact falsification test for A3.

Do not claim `M9-M2`, `M9`, or `GC-target`.

## Round Assessment

| Agent | Idea quality | State evidence | Calibration | Assessment |
|---|---:|---:|---:|---|
| A1 | 8.0 | 7.5 | 8.5 | Strong infrastructure consolidation: H4/R5/M2 definitions, formulas, and average-to-pointwise obstruction. No endpoint overclaim. Needs physical source-card/proof-draft commits. |
| A2 | 7.2 | 5.6 | 6.2 | Pair-swapped and fraction-matching material is useful under H4. Calibration weaker because "semi-diagonal" terminology is unsafe and the continuous $L^4$ orthogonality route is false as stated. |
| A3 | 7.6 | 3.8 | 7.2 | Good diagnostic design and correct `diagnostic_only` framing, but no positive state evidence until scripts are materialized and executed; placeholder $\Phi$ must be replaced after H4. |
| A4 | 8.8 | 7.8 | 8.4 | Strongest analytic progress: AP lemma, local-fourth-moment obstruction, DP near-collision scoping, coprime-rigidity, and fraction-collision calibration. Some M2 applications remain H4-dependent and require dyadic proof-draft verification. |

Overall Round 5 assessment: moderate but real proof-graph progress. The main gain is not an M2 estimate; it is a sharper map of what any M2 fourth-moment proof must still supply.
