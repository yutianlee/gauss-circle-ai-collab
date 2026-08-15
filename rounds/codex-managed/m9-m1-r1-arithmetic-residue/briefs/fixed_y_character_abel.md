# Round 24 brief: fixed-y character-Abel proof

## Role and context

Read `protocol.md`, the proof graph, `state/active_campaign.yml`, Round-21,
Round-22, and Round-23 syntheses, and this brief. Do not read another
Round-24 report. Write only
`rounds/codex-managed/m9-m1-r1-arithmetic-residue/reports/fixed_y_character_abel.md`.

## Candidate kernel

Independently verify the exact return, whose proposed physical form is

\[
\sum_j\sum_{q\ge1}\frac{\chi_4(q)}q
\int_0^{N_X}y^{-3/4}
\{e(\sqrt{X\max(1,y)})-e(\sqrt{XN_X})\}
V_j\!\left(\frac{2\sqrt{Xy}}{D_jq}\right)
\phi\!\left(\frac{y}{(H_j+1)q}\right)dy.
\]

Here \(V_j=W\) for interior scales and the actual one-sided starred top
profile for \(j=0\). Check the sign and every power rather than assuming
this display.

For fixed \((j,y)\), set \(Q=\sqrt{Xy}/D_j\) and prove or refute

\[
\left\|q^{-1}V_j(2Q/q)
\phi\!\left(\frac{y}{(H_j+1)q}\right)\right\|_\infty
+\operatorname{Var}_{q\in\mathbb N}(\cdots)\ll_W Q^{-1}.
\]

Use period-four Abel summation, identify the exact automatic lower threshold
in \(y\), integrate it, and sum the actual dyadic \(D_j\). Retain all
floors, the top jump, equality conventions, and physical normalization.
Explain why the mechanism does not prove an unsigned analogue. Do not use
numerics or import a theorem.

Your report must contain the protocol's seven required sections and stop
after the residue verdict.
