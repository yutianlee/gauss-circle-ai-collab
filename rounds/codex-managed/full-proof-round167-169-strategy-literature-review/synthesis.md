# Round 170 synthesis: full-proof strategy and current literature

Round 170 closes under **`strategy_frontier_reselected`**. The State Patch
changes no accepted estimate, theorem, bridge, or exponent. It repairs one
balanced-parent quantifier seam, creates one explicit open remaining-label
owner, and selects one scoped Round-171 identity-or-no-go experiment. The
resulting graph is
`4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`.

## Full-proof architecture

The standard quarter route still requires both direct M1 parents, all three
complete M2 parents (hard TOP, BAL, and UNBAL), endpoint-uniform one-count
assembly, M9, and the accepted conditional bridge. The alternative route
replaces the direct M1 branch by the complete GAR theorem, but still needs all
of M9--M2. GAR proves neither direct M1 parent nor standard M9.

Round 169 proves an exact coefficientwise double-Poisson self-return to the
Round-162 moving product collar, not its signed nonzero-frequency estimate.
K17a and K26 remain open residual alternatives. Any one of these three routes
would close only a residual or one \(t=1\) face below hard TOP; the other hard-
TOP channels and collars would remain.

## Material BAL scope correction

The dependency review found that the existing double-far remainder and energy
nodes quantify only over persistent critical \(j=1\) blocks with
\(L\asymp X^{1/6}\), while the full BAL parent quantifies over every literal
balanced label \(1\le K/L\le16\). In particular,

\[
 {K\over L}=4^j{X\over\lfloor\sqrt X\rfloor^2}
\]

leaves the exact-square \(j=2\), \(K/L=16\) boundary, noncritical \(j=1\)
scales, and other uncovered labels outside the critical child.

The graph now contains the separate open node
`M9-M2-balanced-remaining-label-owner-quantifier-completion`, and full BAL
depends on it in addition to the critical double-far energy. This prevents a
future proof of the critical child from silently promoting the universally
quantified parent.

## Selected Round-171 frontier

For a persistent critical \(j=1\) literal balanced block \(B\), define

\[
 \mathcal R_B^{\rm osc}
 =\sum_{\substack{|h'k'-hk|>L\\|hk'-h'k|>L}}
 a_B^<(h,k)\overline{a_B^<(h',k')}
 \left[e\!\left(\sqrt X(\sqrt{hk}-\sqrt{h'k'})\right)-1\right].
\]

The sole next inequality is

\[
 \boxed{|\mathcal R_B^{\rm osc}|\ll_\varepsilon L^3X^\varepsilon.}
 \tag{171.BAL-j1}
\]

Its positive capacity is \(L^4X^\varepsilon\), so one factor \(L\) is
missing. Round 171 first tests an exact two-defect commutator identity, using

\[
 \Delta+\rho=q(2h+p),\qquad
 \Delta-\rho=p(2k+q),\qquad h'=h+p,\quad k'=k+q.
\]

These factorizations are coordinates, not a proved commutator. A valid attack
must preserve multiplicity, the fixed-\(p\) character constancy, the
\(p=0\) and \(q=0\) axial sectors, fixed-\(Q\) rulings, both gcd weights,
both slanted symbols, sharp gates, all boundaries, and the real centre. It
must save the factor \(L\) before a positive norm. The round stops at the
first failed identity, complement, restoration, capacity, or owner-scope
gate and does not pivot.

The choice over K26 is a strategic tie-break, not evidence for the estimate.
Both have a factor-\(L\) deficit. The critical BAL child is chosen because
its diagonal, two width-\(L\) corridors, and phase-free mode are already paid,
so the proposed identity has a sharp falsifiable first gate.

## Current-primary-literature result

The source audit is current through 2026-08-26. It found no later indexed
unrestricted pointwise exponent improvement beyond the accepted repaired
Li--Yang dependency. Gao's 2026 theorem is restricted to friable integers.
The current Blomer--Pascadi and Pascadi fixed-modulus Kloosterman advances do
not match the moving product collar, the varying-modulus signed UNBAL vector,
or any other literal project interface after all coefficient, gcd, support,
spectral, endpoint, and restored-power hypotheses are reinstated.

This is a dated scoped no-match, not a universal literature nonexistence
claim. No source promotes the Round-169 collar, K17a, K26, BAL, UNBAL, either
M1 parent, GAR, endpoint assembly, or a global theorem.

## State effect and controls

The State Patch made:

- one open obligation creation;
- three open-obligation scope, dependency, blocker, next-action, and evidence
  updates;
- eighteen rejected-overclaim records; and
- eighteen explicit no-change decisions.

Dry validation, independent scope review, application, authoritative-graph
validation, and post-application reverse audit pass. The new node is open,
the three updated nodes remain open, the BAL parent receives the new
dependency and blocker exactly once, and no new dependency cycle or proof
promotion is introduced.

## Exponent and remaining work

There is no exponent improvement:

- internally proved: \(1/3\);
- accepted external Li--Yang dependency:
  \[
  {3292+25\sqrt{1717}\over13762}
  =0.3144831759740614\ldots;
  \]
- target: \(1/4\).

Even a proof of (171.BAL-j1) would leave the remaining BAL labels, hard TOP,
UNBAL, both direct M1 parents or GAR, endpoint assembly, M9, a bridge, and the
quarter theorem. The full Gauss circle conjecture is therefore not proved.
