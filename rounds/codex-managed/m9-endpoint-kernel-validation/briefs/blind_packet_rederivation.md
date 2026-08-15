# Task brief: statement-only signed packet rederivation

Campaign: `m9-endpoint-kernel-validation`  
Task: `blind_packet_rederivation`  
Role: statement-only blind rederiver  
Graph SHA-256: `90f44e99047eff10b620228e8480a88984f9dbbca4445bb8921667d9d3575031`

Do not read the Round-6 dual endpoint report before completing your
derivation. Do not edit shared state or synthesis files. Write only
`rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_packet_rederivation.md`.

## Statement to rederive or refute

For a fixed smooth symbol \(a(h,k)=A(h/L,k/L)\), consider

\[
\mathcal T(R)=\sum_{h,k\asymp L}\chi_4(h)a(h,k)e(R\sqrt{hk}),
\qquad 1\le L\le R^{1/2}.
\]

Independently derive:

1. \(\sum_m r_L(m)^2\ll L^2\log(2L)\);
2. exact square products and products with
   \(\operatorname{dist}(\sqrt{hk},\mathbb Z)\le R^{-1}\) contribute
   \(O_\varepsilon(L^{1+\varepsilon})\) absolutely;
3. the sector \((h,k)\ge L^{1/2}\) contributes \(O(L^{3/2})\) absolutely;
4. on a dyadic shell \(g=(h,k)\asymp G<L^{1/2}\), with
   \(h=ga,k=gb,(a,b)=1\), Poisson summation in \(g\) converts the exact
   \(\chi_4(g)\) factor into the signed difference of quarter-integer
   packets centered at \(1/4\) and \(3/4\);
5. state the weakest packet estimate which, after summing fixed dyadic
   \(G\), would imply \(\mathcal T(R)\ll L^{3/2}X^\varepsilon\).

Check every factor \(G\), sign, parity restriction, Fourier-transform
normalization, and the distinction between \(\sum_G|\mathcal T_G|\) and
\(|\sum_G\mathcal T_G|\). Determine whether a sharp cutoff in gcd can be
used or whether a fixed smooth partition is required.

## Required report contract

Give the result, exact statement and hypotheses, independent derivation,
first doubtful step, signed/unsigned, square, parity, and proves-too-much
controls, dependencies, and recommended state effect. No external theorem is
needed for the finite reductions; if one is invoked, audit the primary
source exactly.

Allowed context: `protocol.md`, `state/proof_obligations.yml`, and
`rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md`.
