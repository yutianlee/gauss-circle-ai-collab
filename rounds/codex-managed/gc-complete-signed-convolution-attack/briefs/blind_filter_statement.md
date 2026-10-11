# Isolated statement: displaced filter and smoothing scale

Round 203. Role: statement-only independent rederivation. Read only
this packet and protocol.md; do not read graph, manifest, strategy,
prior reports, claimant derivations or sibling reports.

Fix real nonnegative chi in C_c^infinity((c,C)), 0<c<C, nonzero.
Fourier transform uses exp(-2 pi i x xi).
K_T(xi)=T chi-hat(T xi). Let nu be any finite complex measure,
f=inverse Fourier transform of nu, so ||K_T*nu||_2=||chi(./T)f||_2.
For a fixed even Schwartz approximate identity phi with integral1,
write phi_h(xi)=h^-1 phi(xi/h), g_h=phi_h*nu, e_h=nu-g_h.
Derive independently the exact filtered formulas for g_h and e_h,
uniformly for all nu, and optimize any claimed gain by selecting h.
Test the assertion that all vanishing moments of K_T and smoothness
of g_h alone imply ||K_T*nu||_2=O(T^0.58) with a negligible remainder.
Give a rigorous scale dichotomy or a counterexample if appropriate.
Include the borderline hT~1 and possible zeros of phi-hat; distinguish
a uniform statement from a statement for particular coefficients.

The intended arithmetic example, for interpretation only, is
nu=mu^{*6}, where mu=1/2 sum_(n>floor(T^(1/2047)))
r_2(n)n^(-3/4)Psi(sqrt(n/T))
[e(-3/8)delta_sqrt(n)+e(3/8)delta_-sqrt(n)],
Psi fixed real even Schwartz, Psi(0)=1. Do not assert that a generic
counterexample is a counterexample for these particular coefficients.
If smoothing nu directly differs from smoothing mu before convolution,
give the exact multipliers and control all sixfold error terms.

Output a seven-section report: result, hypotheses, proof, first
unproved step, controls, dependencies, recommended state effect.
Write only rounds/codex-managed/gc-complete-signed-convolution-attack/reports/blind_filter_scale_audit.md.
No experiments, no shared edits, no next-round work; stop on report.
