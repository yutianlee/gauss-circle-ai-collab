# Round 6 brief: endpoint sine-kernel attack

You are the direct endpoint attacker. Work at

\[
D\asymp X^{1/2},\qquad 1<L<X^{1/4},
\]

with one fixed nonzero smooth profile \(W(d/D)\). The exact two-sided kernel
is

\[
B_L=
4\sum_{d\asymp D}W(d/D)\chi_4(r_d)
\sum_{\substack{h>0\\h\ {\rm odd}}}
\frac{v_L(h)\Phi(h/(H+1))}{2\pi h}
\sin\!\left(\frac{\pi h(X-dr_d)}{2d}\right),
\]

where \(r_d\) is a nearest odd integer to \(X/d\).

Try to prove \(B_L\ll X^{1/4+\varepsilon}\) on a nontrivial \(L\)-range by
using the fixed-profile smoothness, the nearest-odd map, the product annuli,
or the exact quadratic endpoint identity. If the estimate is false or a
proposed mechanism is false, construct a counterexample using the fixed
profile, not an adversarial sparse weight. Audit the resonant model
\(X=4N^2\), but do not infer uniform real-\(X\) behavior from it.

Retain both frequency signs and the actual \(\Phi/h\) amplitude. Computation,
if any, is limited to falsifying a precise statement and must be followed by
an analytic proof or obstruction.

Deliver
rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/endpoint_sine_kernel_attack.md.
Do not edit shared state.
