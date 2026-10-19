# Round233 Wolfram and independent local controls

Date2026-10-12 Asia/Shanghai. User explicitly selected the Wolfram plugin. Evidence level `diagnostic_only`; planned analytical/algebraic allocation at least90 percent, bounded computation at most10 percent. All infinite-family and asymptotic arguments are proved and reviewed analytically.

The plugin's semantic context call returned general Newton-identity information and unrelated suggestions. No theorem or source hypothesis was imported from those generated suggestions. The substantive computation used the Wolfram Language evaluator, with a45-second bound and a fresh stateless kernel. Exact submitted code is `wolfram_checks.wl`; the complete returned structured text is `wolfram_result.json`. No formatted-result URL was returned.

The code constructs the ordered distinct polynomial by the Newton recurrence, then checks every coefficient of its repeated-index remainder against the derangement grouping at fixed even orders2,4,6,8,10,12,14,16. It verifies total absolute coefficient p!-1, leading repeated-pair coefficient binom(p,2), the signed sequence(-3,-1,0,2,5), the order6 negative control-720, and the rational head exponent161/156. Every returned check was true. Polynomial monomial counts were1,4,10,21,41,76,134,230 respectively.

Independent local reproduction uses standard-library integer polynomial dictionaries and a separate elementary-symmetric dynamic program, with exact rational values where needed. Run from the repository root:

    python rounds/codex-managed/gc-fixed-order-moment-absorption/controls/exact_local_controls.py

The run passed; output is `exact_local_controls.json`. It matches all Wolfram coefficients and counts, and additionally checks64 finite-family identity/absorption cases, including empty/zero, small cardinality, positive, mixed-sign and rational families. The negative signed control and161/156 match exactly. There is no floating-point tolerance or fitted exponent. All scripts and outputs are frozen in the closure artifact manifest.

Pass/fail rule: all finite polynomial identities and rational inequalities must hold exactly. Scope: these controls can reveal normalization, sign or coefficient mistakes, but finitely many orders cannot certify the all-fixed-order theorem. They do not estimate the actual arithmetic signed integral, justify p growing with T, or imply a new Gauss-circle exponent. The independent statement-only report supplies exact analytical adversarial controls beyond the finite run.

Launch validation initially rejected an unsupported task-role label before any shared-state mutation. The label was corrected to the schema's `barrier_no_go`, and launch validation then passed. No mathematical hypothesis or frozen objective was changed by that administrative repair.
