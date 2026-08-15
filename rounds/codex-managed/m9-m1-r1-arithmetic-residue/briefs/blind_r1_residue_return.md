# Round 24 brief: blind exact R1 residue return

## Role and isolation

You are the statement-only residue-return deriver. Read only:

- `protocol.md`;
- `state/proof_obligations.yml` entries named below;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-radial-endpoint-renormalization/synthesis.md`;
- `rounds/codex-managed/m9-m1-endpoint-boundary-cauchy/synthesis.md`;
- `rounds/codex-managed/m9-m1-upper-endpoint-character-abel/synthesis.md`;
- this brief.

Do not read any other Round-24 report. Write only
`rounds/codex-managed/m9-m1-r1-arithmetic-residue/reports/blind_r1_residue_return.md`.

## Exact task

Starting from

\[
\mathfrak R^{\rm ar}[R_1]
=\sum_j\frac1{(2\pi i)^2}\iint\mathcal A_j(u,v)
R_{1,v}(1-(u+v)/2)L(1-u-v,\chi_4)\,dv\,du,
\]

\[
\mathcal A_j=\widehat W_j(u)\widehat\phi(v)
\left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v,
\quad
R_{1,v}=-\frac{\pi i\sqrt X}{\delta}
\int_1^{N_X}x^{\delta-1/2}e(\sqrt{Xx})\,dx,
\]

\[
\delta=\frac14-\frac u2-v,
\]

choose explicit positive lines satisfying every convergence inequality and
derive the physical symmetric-profile expression from scratch. You may use
the beta integral for \(1/\delta\), conditional Dirichlet convergence of
\(L(s,\chi_4)\) for \(\Re s>0\), and elementary integration. Decide
whether the resulting expression is normalized \(O(1)\), with a complete
proof if so.

Audit the finite truncation order, the top one-sided inversion, every sign
and power, \(y=0,1,N_X\), height floors, endpoint stars, and the external
physical \(X^{1/4}\) factor. Do not address transition traces or GAR.

Your report must contain exactly the seven protocol sections: result;
exact statement/hypotheses; proof; first doubtful/unproved step; required
control and outcome; dependencies/artifacts; recommended state effect.
No numerics.
