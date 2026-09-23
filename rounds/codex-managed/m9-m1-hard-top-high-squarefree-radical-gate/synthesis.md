# Round 181 synthesis

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Round: 181
- Generated: `2026-08-27T08:44:04.7412815Z`
- Starting graph: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Closing label: `strict_hard_m1_radical_sector`
- Role: conductor synthesis; State Patch evidence, not self-authorizing state
- Context: complete Round-181 campaign packet and accepted graph dependencies
- Numerical work: none; 100% analytic/algebraic

## Outcome

Round 181 proves an exact squarefree-radical reduction for every literal
residual hard-M1 shell. Grouping by (r=hn=st^2), with (s) squarefree,
preserves all incidences and all literal coefficient fields. If
(G=(h,n)), then uniquely

\[
 h=Gda^2,\qquad n=Geb^2,\qquad s=de,\qquad t=Gab,
\]

so (G\mid t) and (st^2\asymp L^2).

Two disjoint sectors are now paid absolutely:

\[
 \sum_{s\leq L}\sum_t|C(st^2)|
 +\sum_{\substack{s>L\\t\geq\lceil\sqrt L\rceil}}|C(st^2)|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

The exact remaining hard owner is

\[
 \left|\sum_{\substack{s>L,\ \mu^2(s)=1\\1\leq t<\lceil\sqrt L\rceil}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

It remains open, including (t=1), where the full coprime-squarefree
literal cone survives and the universal capacity remains (L^2).

## Mechanism result

Complete squarefree Möbius linearization gives, for every (L),

\[
 \mathcal H_{L,\sigma}=\mathcal T_{L,\sigma}^{M1}+E_{L,\sigma},
\]

with

\[
 E_{L,\sigma}=
 \sum_{b\leq L,u}K_L(b,u)F_\sigma(bu^2)-\sum_{r\leq L}F_\sigma(r)
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

Thus complete Möbius inversion returns to the original cone modulo an
already-safe term. Joint-(t) lifting is only a permutation of product
indices. The full-orientation Mellin Euler factor has useful cancellation
at its central mode, but the literal truncated divisor cone requires all
noncentral modes and endpoints. These conclusions park only the exact
automatic mechanisms tested. Adversarial/dechirped capacity is not literal
lower mass.

## Proof status

The strict sectors and exact self-return are subordinate progress. They do
not prove `M9-M1-top-endpoint-signed-cone`. Even that hard child would leave
the independent smooth direct-M1 child open. GAR, M9-M1, hard TOP, BAL,
UNBAL, M9-M2, endpoint uniformity, M9, both bridges, and the Gauss circle
quarter theorem remain open.

There is no global exponent improvement: the strongest internally proved
exponent remains (1/3); the accepted external benchmark remains
(0.3144831759740614\ldots); the target remains (1/4).

## State decision

The reviewed patch creates a proved reduction, an explicit open small-(t)
residual, and one mechanism-scoped obstruction; updates only four M1
owner/strategy records; rejects thirteen overclaims; and makes no existing
status or theorem-statement change. Round 182 is mandatory after mechanical
closure and will reconstruct the full proof strategy and reassess current
primary literature before selecting another analytic frontier.

