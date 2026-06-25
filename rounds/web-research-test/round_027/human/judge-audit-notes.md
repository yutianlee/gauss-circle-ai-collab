# Judge Audit Notes

Use these notes when judging Round 27. They summarize local polish/audit findings and should be treated as human steering plus audit cautions, not as agent outputs.

## Process notes

- A1/A2/A3 Stage A responses are archived and normalized.
- A1/A2/A3 Stage B reviews are archived and normalized.
- `strategy-revised.md` is archived under this round's `human/` directory.
- A2 Stage A and A2 Stage B both failed their configured local word-count self-checks. Treat them as useful mathematical content, not as fully compliant with the standing A2 depth standard.

## Mathematical cautions

- Keep the bridge conditional:

$$
\text{H1--H3}+\text{H4}+\text{R5-Full}+\text{M9}
\Longrightarrow
P(X)\ll_\epsilon X^{1/4+\epsilon}.
$$

M9 remains open.

- A1 is the strongest proof-infrastructure artifact: H4 external theorem status, R5-Full conditional residual control, fixed-coefficient M9 target, real-weight caveat for paired formulas, and Hardy-collapse demotion are all useful.

- A2's two-sided `M_2` convention, resonance integer `N`, and CRI statistic are useful, but the fourth-moment formulas need a real-weight or conjugated-weight hypothesis. For complex weights, use

$$
w_D(d_1)\overline{w_D(d_2)}w_D(d_3)\overline{w_D(d_4)}.
$$

- A2's denominator-paired singular family and full `N=0` compatibility claims should not be promoted as proved without more parameter and boundary bookkeeping.

- A3's Stage A R5 pseudocode has a normalization bug: it returns a per-denominator average divided by `D X^{1/4}`. Future scripts should report the raw block quantity

$$
\frac1{H_D}\sum_{d\asymp D}|w_D(d)|K_{H_D}(t_d)
$$

and its ratio to `X^{1/4}`.

- Li--Yang Case A typo correction is strongly supported by TeX/final-argument audit, but rendered-PDF verification is still pending. The endpoint non-import guardrail remains stable.

- Treat `strategy-revised.md` as a human-supplied conjectural Hardy-collapse proposal to falsify. Do not record it as a proof or replacement main route unless uniform B-process error bounds, local divisor-window coefficient control, and an applicable shifted-convolution theorem are supplied.

