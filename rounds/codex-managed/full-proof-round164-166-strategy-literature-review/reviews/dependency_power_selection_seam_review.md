# Round 166 dependency, power, and selection seam review

- Campaign: full-proof-round164-166-strategy-literature-review
- Review role: dependency / power / selection seam
- Starting authoritative graph: 87d58660e7e11a23eb3d8759917e02376479ba38acaf727b0a2dc15d5920f5e0
- Date: 2026-08-26
- Reviewed reports: statement-only blind rederivation and full-graph frontier audit
- Verdict: **GREEN WITH MANDATORY TEXTUAL/DERIVATIONAL REPAIRS**

## 1. Result

The substantive Round-166 decision is sound. The blind report and the full-graph report independently select the same unique Round-167 inequality:

\[
 \boxed{
 \Re\mathfrak C_{R_0,2,\mathrm{opp},\,g<\gamma L}^{\mathrm{rem}}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon,
 \qquad R_0=\lceil L\rceil .}
 \tag{167.F}
\]

The authoritative standard and GAR trees support that selection. The standard route still needs both direct M1 parents, TOP, BAL, UNBAL, and endpoint-uniform assembly. The GAR route replaces the two direct M1 parents only at the total-active-M1 bridge and still needs all of M2. Estimate (167.F) lies strictly inside the residual child of TOP. It can close only the residual scalar and cannot by itself close the full \(t=1\) face, TOP, BAL, UNBAL, either M1 route, endpoint uniformity, \(M9\), either bridge, or an exponent theorem.

The full-graph ordering is retained:

1. minimal residual Fejer, (165.K17a)/(167.F);
2. maximal residual Fejer, (165.K26);
3. direct residual scalar;
4. a direct complete hard-TOP parent shortcut;
5. GAR;
6. direct hard M1;
7. direct smooth M1;
8. BAL;
9. UNBAL;
10. the separate \(W=Y^{7/16}\) graded determinant lane; and
11. endpoint uniformity, which is an assembly seam rather than a stand-alone analytic inequality.

The blind report orders BAL, UNBAL, the two direct M1 parents, and GAR differently below rank 4. That is not a logical conflict: the blind report expressly lacked the graph's exact capacities and mechanisms and disclaimed a strong confidence ordering there. It agrees on the only selection-relevant facts: unique rank 1 is (167.F), rank 2 is (165.K26), rank 3 is the direct residual scalar, and all three have residual-only leverage.

Nine repairs are required before synthesis quotes the reports:

1. do not transfer fixed-shift Cauchy for the unpartitioned coefficient correlation directly to the post-opening \( \mathrm{opp},g<\gamma L\) sector;
2. repair the malformed odd-divisor condition in the full-graph report;
3. replace “quarter-strength local target” for \(\beta=1/2\);
4. define \(R=X^{1/4}\) and \(y=\lfloor\sqrt X\rfloor\) in the GAR capacity row;
5. freeze the Round-167 mechanism as the Grimmelt--Merikoski source-to-literal-interface/no-go gate, without an in-round fallback to a different “bespoke” route after source failure; and
6. narrow two overbroad equivalence/uniqueness phrases concerning BAL capacity and the internal sub-\(1/3\) connector;
7. strengthen “bounded multiplicity” to an exact multiplicity-preserving determinant dictionary and describe the source as matching the determinant skeleton, not the literal weighted theorem;
8. scope the arbitrary-coefficient control to the unfiltered or filter-erased level unless an explicit incidence-level adversarial family is constructed; and
9. distinguish the complete hard-TOP shortcut ranked fourth from the narrower task of proving only the remaining nonresidual channels, and qualify “smallest exact theorem” as a claim about a mechanistically specified aggregate frontier.

None of these repairs changes the K17a selection, its one-power deficit, its promotion gate, its source-failure stop rule, or any graph status or exponent.

## 2. Exact statement and hypotheses

### 2.1 Reviewed residual theorem

Let \(J=\sqrt X\). Retain the complete literal Round-164 coefficient

\[
 c_N^{\mathrm{rem}}
 =\sum_{\substack{d\mid N\\ d\ \mathrm{odd}}}
   \chi_4(d)\lambda_N(d)
\]

with the neither/both residual selector, squarefree and coprime conditions, both parity branches, Vaaler taper, profiles, floors, stars, hard point value, support crossings, endpoint conventions, and zero extension. The accepted scales are

\[
 N\asymp L^2,\qquad M_L\asymp L^2,\qquad
 D_L:=\sum_N|c_N^{\mathrm{rem}}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\]

For \(R_0=\lceil L\rceil\), (167.F) retains:

- one outer real part;
- exactly the even shifts \(1\le r<R_0\);
- the opened determinant equation \(d'm'-dm=r\);
- the opposing-displacement condition \((d'-d)(m'-m)<0\);
- the opened-incidence condition \(g=(d,d')<\gamma L\); and
- every literal residual weight and boundary convention.

The proved Fejer connector, parity split, monotone-sector estimate, and high-\(g\) estimate then imply only

\[
 |\mathcal S_{L,1}^{\mathrm{rem}}|
 \ll_{\gamma,\varepsilon}L^{3/2}X^\varepsilon.
\]

The \(g\)-split is owner-complete for opened divisor incidences, not a unique partition of product rows. No deletion or modulus inside this signed sector is licensed merely because it decreases an unsigned atom set.

### 2.2 Complete standard tree

The exact standard logic is

\[
\begin{array}{c}
\mathrm{H1\!-\!H3}+\mathrm{H4}+\mathrm{R5\!-\!Full}+\mathrm{M9}\\
\Downarrow\quad\mathrm{Conditional\!-\!bridge}\\
\mathrm{GC\!-\!target}.
\end{array}
\]

Conditional-bridge is derived under assumptions; H1-H3 and R5-Full are proved internally; H4 is a proved external dependency; and M9 is open. The open analytic part of M9 is

\[
\begin{array}{c}
\mathrm{M9\!-\!M1}\\[-2mm]
\swarrow\qquad\searrow\\[-2mm]
\mathrm{M1\ top\ endpoint\ signed\ cone}\qquad
\mathrm{M1\ direct\ smooth\ residual}
\end{array}
\]

together with

\[
\begin{array}{c}
\mathrm{M9\!-\!M2}\\[-2mm]
\swarrow\qquad\downarrow\qquad\searrow\\[-2mm]
\mathrm{TOP}\qquad\mathrm{BAL}\qquad\mathrm{UNBAL}.
\end{array}
\]

The two physical one-count assemblies are already proved conditional assemblies. M9-endpoint-uniformity is an open blocker/assembly seam over the five analytic parents; it is not a sixth cancellation theorem and is not listed as a formal dependency of M9.

Inside TOP only, the relevant residual branch is

\[
\mathrm{TOP}
\supset
\mathrm{complete\ hard\!-\!TOP\ channel\ assembly}
\supset
\text{residual at }t=1
\Leftarrow
\begin{cases}
\text{(165.K17a), or}\\
\text{(165.K26).}
\end{cases}
\]

This OR is local to the residual child. The remaining \(L\ll D\ll L^2\), \(t\ll\sqrt L\) channels and their near-collision collars remain open after either residual theorem.

### 2.3 Complete GAR tree

The alternative logic is

\[
\begin{array}{c}
\mathrm{H1\!-\!H3}+\mathrm{H4}+\mathrm{R5\!-\!Full}
+\mathrm{GAR\!-\!total\ active\ equivalence}
+\mathrm{M9\!-\!M2}\\
\Downarrow\quad\mathrm{GC\!-\!global\!-\!M1\ alternative\ bridge}\\
\mathrm{GC\!-\!target}.
\end{array}
\]

M9-M1-GAR-total-active-equivalence is proved internally but depends on the open GAR node M9-M1-global-angular-radial-estimate. The GAR node's sole open assembly blocker is the global lower-radial signed estimate; its compact, nonlower, and interface owners are proved. GAR controls the total active M1 contribution only. It neither proves either direct blockwise M1 parent nor implies M9-M1, blockwise M9, or endpoint-uniform blockwise M1.

The \(W=Y^{7/16}\) determinant lane is a separate graded route. It is not a third quarter-proof tree and does not imply an M9 parent.

### 2.4 Promotion gate and stop rule

Promotion of (167.F) requires, conjunctively:

1. an exact multiplicity-preserving equality from the opened residual family to matrices with \(d'm'-dm=r\), with every multiplicity either one or carried by an explicit restoring weight and every selector, parity, squarefree/coprime mask, profile, star, and endpoint owned once;
2. preservation of one aggregate real part, with every intermediate modulus priced at \(O(L^2X^\varepsilon)\);
3. a literal Grimmelt--Merikoski Theorem 10.1 interface audit: the coefficient class, \(C^7_\delta\) seminorm, factorization and gcd hypotheses, two-adic strata, \(\mathcal K_+\), main term, \(\mathcal R_0,\mathcal R_1,\mathcal R_2\), completion, boundary, Möbius, and modulus costs must all restore to \(O(L^2X^\varepsilon)\);
4. failure on the phase-aligned arbitrary-coefficient control, with an explicit explanation of which actual residual structure creates the saving;
5. uniformity in the real centre, hard crossings, two-adic strata, fixed \(\gamma\), and inherited physical labels; and
6. independent normalization/sign, source, endpoint/power, and graph-scope reviews.

Round 167 must stop with a scoped no-go at the first literal source-hypothesis failure or fixed positive restored-power loss. It must not pivot in the same round to (165.K26), direct residual, another TOP channel, GAR, BAL, UNBAL, or a parent theorem. A “bespoke theorem” may only be the exact literal determinant-kernel formulation developed inside this frozen source-to-interface gate; it is not authority to abandon a failed source map and begin a second mechanism.

## 3. Proof or derivation

### 3.1 Dependency verification

The tree statements above were checked directly against dependencies, blockers, and implies in the authoritative graph.

- GC-target is open. Its standard dependency is Conditional-bridge, whose only open dependency is M9.
- M9 formally depends on M9-M1 and M9-M2 in addition to the already accepted infrastructure. Its blocker list is exactly the two direct M1 parents, TOP, BAL, UNBAL, and endpoint uniformity.
- M9-M1 and M9-M2 are connected through proved physical one-count assemblies; those assemblies do not prove their open analytic parents.
- GC-global-M1-alternative-bridge depends on the proved GAR-to-total-active equivalence and on M9-M2. It has no implication to M9.
- M9-M1-global-angular-radial-estimate remains open on M9-M1-global-lower-radial-signed-estimate; the nonlower completion is proved.
- M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction is proved as a reduction. The boxed estimates (165.K17a) and (165.K26) are hypotheses inside that reduction, not proved graph nodes.

Thus the two reports' common residual-only scope and no-promotion conclusion are correct.

### 3.2 Target and capacity audit

Every numerical target or capacity used in the full-graph ranking checks as follows. “Capacity” means an accepted upper/adversarial ledger, never a lower bound for the literal signed scalar.

| Rank | Frontier | Exact target | Present capacity and missing power | Scope/exponent check |
|---:|---|---|---|---|
| 1 | Minimal residual Fejer (165.K17a) | \(\Re\mathfrak C_{R_0,2,\mathrm{opp},g<\gamma L}^{\mathrm{rem}}\ll L^2X^\varepsilon\), \(R_0\asymp L\) | The direct opened-incidence absolute ledger is \(L^3X^\varepsilon\); the missing factor is \(L\). The monotone and \(g\ge\gamma L\) sectors are already \(L^2X^\varepsilon\)-safe. | Closes only the residual scalar; no exponent follows. |
| 2 | Maximal residual Fejer (165.K26) | Even \(R_0\le r<M_L\) aggregate \(\ll L^3X^\varepsilon\) | Fixed-shift Cauchy gives \(D_L\) for each of \(O(M_L)=O(L^2)\) shifts, hence \(L^4X^\varepsilon\); missing \(L\). The paid \(r<R_0\) range already costs \(R_0D_L\ll L^3X^\varepsilon\). | Same residual owner as rank 1; no exponent follows. |
| 3 | Direct residual scalar | \(|\mathcal S_{L,1}^{\mathrm{rem}}|\ll L^{3/2}X^\varepsilon\) | Support/energy Cauchy gives \((M_LD_L)^{1/2}\ll L^2X^\varepsilon\); missing \(L^{1/2}\). | Same residual owner, with no equally literal new theorem interface. |
| 4 | Direct complete hard-TOP shortcut | \(\Re C_{(L,\mathrm{tag})}^{\mathrm{comp}}\ll L^2X^\varepsilon\), with owner normalizations \(E_L^{\mathrm{top}}\ll L^2X^\varepsilon\) and \(T_{\mathrm{end},L}\ll L^{3/2}X^\varepsilon\) | Coefficient-blind energy \(L^3\) or scalar \(L^2\); missing \(L\) in energy or \(L^{1/2}\) in the scalar. Fixed \(t\ge\tau\sqrt L\) is closed; the residual, small-\(t\) intermediate-\(D\) channels, and collars remain. | Would close TOP only; BAL and UNBAL still block M9-M2. Proving only the remaining nonresidual channels is a narrower, different frontier and would leave K17a/K26 open. |
| 5 | GAR | \(G_X\ll X^\varepsilon\) in the exact displayed real-part normalization | With \(R=X^{1/4}\), \(y=\lfloor\sqrt X\rfloor\), the lower scalar/wavelet has \(R^2=y\) absolute capacity against \(RX^\varepsilon\). The separated centered-square route at \(K\asymp y\) asks for \(y^2X^\varepsilon\) against coefficient-blind \(y^3\). | GAR plus all M2 gives the alternative quarter bridge; GAR alone gives no exponent and no blockwise M1 result. |
| 6 | Direct hard M1 | Normalized cone \(\ll L^{3/2}X^\varepsilon\), equivalently its physical block \(\ll X^{1/4+\varepsilon}\) | Normalized \(L^2\), or physical \(X^{1/4}L^{1/2}\); missing \(L^{1/2}=X^{1/12}\) at \(L=X^{1/6}\). | Closes one direct M1 parent only. |
| 7 | Direct smooth M1 | Every literal \(B_1(D,L;X)\ll X^{1/4+\varepsilon}\) | First critical smooth profile has \(X^{1/3+o(1)}\) menu capacity; missing \(X^{1/12}\). | Closes the second direct M1 parent only. |
| 8 | BAL | \(\left|\sum_GG\mathscr P_G\right|\ll L^{3/2}X^\varepsilon\) on each literal balanced block | The current scalar envelope loses at most \(X^{1/12}=L^{1/2}\). In the corresponding double-far squared-energy ledger, the target is \(L^3\) and coefficient-uniform capacity is \(L^4\). | Closes BAL only. The \(L^4/L^3\) statement is a route-specific energy comparison, not a literal lower bound or algebraic equivalent of every scalar formulation. |
| 9 | UNBAL | \(\mathcal T_{L,K}\ll (LK)^{3/4}X^\varepsilon\), \(K/L>16\) | For \(a=\delta-\ell\), the missing factor is \(X^{\mu(a)}\), with \(\mu(a)=a-1/4\) for \(1/4<a\le1/3\) and \(\mu(a)=(1-2a)/4\) for \(1/3\le a<1/2\). The audited scalar projective and long-row costs exceed this margin. | Closes UNBAL only. |
| 10 | \(W=Y^{7/16}\) graded determinant | Complete actual correlation \(\ll Y^{\beta+\varepsilon}\); frozen determinant target \(\beta=1/2\) | Best complete bound is \(\beta=35/48\). Crossing below the persistence threshold requires \(\beta<9/16\), hence a saving \(>1/6\); reaching \(1/2\) needs \(11/48\). | \(\Theta(\beta)=\max\{(7/16+\beta)/3,\beta/2\}\). Thus \(\beta=1/2\) yields \(5/16\), not \(1/4\); the lane closes no M9 parent. |
| 11 | Endpoint uniformity | Uniformity of the selected parent bounds over all real-\(X\) active labels | No independent positive capacity. Its blockers are the five analytic parents on the standard route. | Necessary assembly seam, not a selectable cancellation theorem. |

The arithmetic in the graded connector is exact:

\[
\Theta(9/16)=1/3,\qquad
\Theta(1/2)=\max\{5/16,1/4\}=5/16.
\]

Hence the internal certified exponent stays \(1/3\); the separately audited Li--Yang exponent stays

\[
\theta_{\mathrm{LY}}
=\frac{3292+25\sqrt{1717}}{13762}
=0.3144831759740614\ldots;
\]

and the target \(1/4\) stays open.

For the K17a capacity, the lawful direct count is independent of the unpartitioned coefficient Cauchy bound. After exact divisor opening, choose \(d,m,d'\asymp L\). The condition \(0<d'm'-dm<R_0\asymp L\) confines \(m'\) to an interval of length \(O(R_0/d')=O(1)\). Thus there are \(O(L^3)\) raw incidences before divisor-size losses, and all literal sector, squarefree, coprime, and gcd restrictions only delete incidences. This proves the stated \(L^{3+o(1)}\) absolute ledger without treating a signed sector deletion as monotone at the coefficient level.

### 3.3 Selection proof

Ranks 1 and 2 require the same one-power cancellation and close the same residual owner. Rank 1 is the smaller theorem: it has \(O(L)\) shifts, already proved strict-sector removals, and no maximal-window short/medium-long splice. Rank 2 has \(O(L^2)\) shifts and consumes its complete \(L^3\) short-shift connector budget before the open medium/long theorem is used.

The direct residual target has a smaller formal deficit \(L^{1/2}\), but the accepted direct routes erase or return the necessary sign and no comparably literal new theorem interface is available. The remaining candidates are broader parent or global theorems with more independent owners, or a separate graded lane with no M9 implication. The determinant equation

\[
d'm'-dm=r
\]

is exactly the determinant skeleton underlying (165.K17a), while Grimmelt--Merikoski Theorem 10.1 offers a concrete joint-determinant spectral model without yet satisfying the literal coefficient and power hypotheses. This makes an exact source-to-interface/no-go audit of (167.F) the unique bounded Round-167 objective.

### 3.4 Precise issues and repairs

| ID | Severity | Issue | Required repair |
|---|---|---|---|
| S1 | Material derivational seam; selection unaffected | Blind equations (3.1)--(3.2) apply to the unpartitioned \(S_r=\sum_Nc_{N+r}^{\mathrm{rem}}\overline{c_N^{\mathrm{rem}}}e(\cdots)\). The post-opening \(\mathrm{opp},g<\gamma L\) subaggregate is not obtained by deleting coefficient terms before that Cauchy bound in an order-preserving way; discarded sectors may cancel the retained one. | State the \(L^3\) K17a capacity using the direct opened-incidence absolute ledger. Keep fixed-shift Cauchy for K26 and for the unpartitioned short range only. Do not claim a Cauchy proof of a restricted-sector upper bound. |
| S2 | Textual but exact-statement critical | The full-graph report's definition of \(c_N^{\mathrm{rem}}\) contains a bare carriage-return corruption in the odd-divisor condition. | Replace that condition by \(d\ \mathrm{odd}\). |
| S3 | Exponent terminology | The phrase “quarter-strength local target” for \(\beta=1/2\) suggests a quarter connector, while the exact connector gives \(5/16\). | Replace it by “frozen determinant-correlation target” or “full \(Y^{1/2}\) determinant target.” |
| S4 | Scale ambiguity | The GAR row uses \(R\) and \(y\) without defining them locally, while \(R\) elsewhere denotes a Fejer window. | Insert \(R=X^{1/4}\) and \(y=\lfloor\sqrt X\rfloor=R^2+O(1)\) in the GAR row. |
| S5 | Round-discipline ambiguity | “Grimmelt--Merikoski ... or a bespoke theorem” can be read as two mechanisms inside one frozen round. | Freeze Round 167 as the exact Grimmelt--Merikoski source-to-literal-interface/no-go map for (167.F). A bespoke determinant-kernel statement is permitted only as the literal theorem extracted within that map. On the first source-class or restored-power failure, stop; do not pivot. |
| S6 | Overbroad wording | “Equivalently” in the BAL row conflates the scalar envelope with one stronger squared-energy ledger, and “the only independent sub-one-third connector” is globally too absolute in the presence of the separate accepted external Li--Yang theorem. | Say “in the corresponding double-far squared-energy ledger” for BAL, and “the only explicitly quantified open internal sub-\(1/3\) connector compared in this ranking” for \(\Theta(\beta)\). |
| S7 | Exact-interface defect | “Bounded multiplicity” alone does not identify the literal weighted K17a aggregate, and saying the source geometry “lands literally” on K17a conflates an exact determinant equation with an unproved coefficient map. | Require exact equality: multiplicity one or an explicit multiplicity weight, with every sign and owner restored. Say that the source matches the determinant skeleton only. |
| S8 | False-control scope | An arbitrary product-site array \(c_N\) has no canonical \(d,d',m,m'\), hence no literal \(\mathrm{opp}\) or \(g<\gamma L\) sector. The usual phase-aligned control falsifies energy-only reasoning for the unfiltered Fejer form but is not automatically a counterexample to K17a. | Scope the control to proof steps that have erased the incidence filters, or construct a literal lifted incidence array with all selectors and energy accounted for. Do not demand that an actual K17a proof fail a control that is not defined on its domain. |
| S9 | Frontier-scope terminology | The blind rank-4 item is work on remaining nonresidual hard-TOP channels; the graph report's row 4 is a complete all-channel TOP theorem that also owns the residual. “Smallest exact surviving theorem” also overlooks that the direct residual scalar is a smaller owner-level target, though less mechanistically specified. | Relabel row 4 as a direct complete hard-TOP parent shortcut and keep a narrower remaining-channel task distinct. Describe K17a as the smallest exact mechanistically specified aggregate frontier, not unqualifiedly the smallest theorem. |

## 4. First doubtful or unproved step

The first mathematical gap remains the source/interface lemma, not a hidden graph connector:

> Partition the literal K17a residual determinant family into finitely many target-safe pieces and represent each piece in the exact coefficient and \(C^7_\delta\) class required by Grimmelt--Merikoski Theorem 10.1, while preserving one aggregate real part and proving that the main term, \(\mathcal K_+\), every \(\mathcal R_j\), two-adic/gcd split, Möbius/modulus sum, completion, and boundary contribution total \(O_{\gamma,\varepsilon}(L^2X^\varepsilon)\).

This is unproved. The first likely failure is either:

- the neither/both residual selector does not enter the source coefficient class without a fixed-power projective/orbit-correlation cost; or
- the square-root phase and hard support force a \(C^7_\delta\), cell, or boundary cost that consumes the required factor \(L\).

The first review-specific doubtful step is S1: the blind report's fixed-shift Cauchy calculation cannot certify the opened restricted K17a sector. The corrected opened-incidence absolute ledger still leaves exactly the same factor \(L\), so this seam does not weaken the selection argument.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Complete standard dependency tree | **GREEN.** Both direct M1 parents, TOP, BAL, UNBAL, and endpoint uniformity remain exactly the blockers recorded above. |
| Complete GAR dependency tree | **GREEN.** GAR replaces total active M1 only in the alternative bridge and still requires all of M9-M2. |
| K17a versus K26 target and capacity | **GREEN WITH REPAIR S1.** Targets \(L^2\) and \(L^3\), capacities \(L^3\) and \(L^4\), and one-power deficits are correct; the K17a capacity must not be attributed to a non-lawful Cauchy transfer. |
| Residual-only scope | **GREEN.** Either Fejer theorem can update only the residual scalar after seam review. |
| Direct residual, hard TOP, GAR, direct M1, BAL, UNBAL capacities | **GREEN WITH WORDING REPAIRS S4/S6.** All powers check; no hostile capacity is treated as a physical lower bound. |
| Graded sub-\(1/3\) connector | **GREEN WITH TERMINOLOGY REPAIR S3/S6.** The threshold \(9/16\), current \(35/48\), target \(1/2\), and \(\Theta(\beta)\) arithmetic are exact. |
| Unique Round-167 objective | **GREEN WITH REPAIR S5.** The only inequality is (167.F); the source audit is its frozen mechanism gate, not a second theorem or fallback task. |
| Promotion gate | **GREEN WITH REPAIRS S7/S8.** It covers literal coefficient, sign, source, power, endpoint, hostile-array, and graph-scope validation; exact equality and the domain of the hostile-array control must be stated precisely. |
| Source-failure stop rule | **GREEN.** Stop on the first failed literal hypothesis or fixed positive restored-power loss and record a scoped no-go. No pivot is licensed. |
| Exponent/status guard | **GREEN.** Internal \(1/3\), external \(\theta_{\mathrm{LY}}\), and target \(1/4\) remain distinct; K17a alone has no exponent connector. |
| File-integrity control | **REPAIR REQUIRED.** Remove the bare carriage return identified in S2 before reusing the displayed coefficient. |

The Round-167 hostile controls must additionally reject any proof step that, after erasing the literal incidence filters, survives replacement by phase-aligned arbitrary coefficients; takes a modulus per shift/orbit/gcd row; invokes alternating character on an even cofactor row; converts a large real derivative into unproved modulo-one separation; deletes high-\(g\) incidences twice; or omits any \(\delta^{-O(1)}\), \(\mathcal K_+\), \(\mathcal R_j\), main-term, modulus, Möbius, endpoint, or completion cost. A stronger filtered adversarial control is valid only after its incidence-level coefficient family is explicitly constructed.

No numerical experiment was used. The review is entirely algebraic, logical, and power-ledger based.

## 6. Dependencies and exact artifacts used

This review used:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
- rounds/codex-managed/full-proof-round164-166-strategy-literature-review/reports/blind_frontier_priority_rederivation.md;
- rounds/codex-managed/full-proof-round164-166-strategy-literature-review/reports/full_graph_frontier_strategy_audit.md;
- the authoritative W-lane nodes GC-W7-16-actual-reduced-determinant-correlation, GC-W7-16-complete-all-shell-curvature-saving, and GC-W7-16-residue-mode-interlacing-cross-ray-obstruction inside the graph; and
- the authoritative GAR, direct-M1, BAL, UNBAL, hard-TOP, and bridge nodes cited by ID in Sections 2 and 3.

The Grimmelt--Merikoski paper was not independently source-audited in this seam review. Its theorem remains only a candidate mechanism subject to the dedicated source report and the promotion gate above.

## 7. Recommended state effect

**Recommended state effect: retain / no graph change, after report-level repairs.**

- Accept (167.F)/(165.K17a) as the unique Round-167 inequality.
- Preserve the full-graph ranking in Section 1.
- Preserve the conjunctive promotion gate.
- Freeze the Grimmelt--Merikoski source-to-literal-interface/no-go map as the Round-167 mechanism.
- Preserve the first-failure stop rule: on a source-class mismatch or any fixed positive restored-power loss, close with a scoped no-go and do not pivot within Round 167.
- Apply repairs S1--S9 in synthesis wording before quoting the reports.
- Do not promote K17a, the residual scalar, TOP, BAL, UNBAL, either M1 route, endpoint uniformity, M9, a bridge, a source dependency, or any exponent.
- Close Round 166 under strategy_frontier_retained only after the conductor confirms the sibling source review is compatible with this gate.

This review writes no State Patch and licenses no shared-state edit or Round-167 start.
