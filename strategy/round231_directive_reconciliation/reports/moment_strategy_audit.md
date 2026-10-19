# Moment normalization, restoration, and strategy reconciliation

Round231 prelaunch strategy reconciliation; task `moment_strategy_audit`; role: restoration and scope reviewer. Generated 2026-10-11. This is selected-context independent algebraic review, not statement-only isolation, an analytic campaign, or a State Patch. Starting and inspected graph SHA256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

## 1. Result: restoration lemma and scoped strategy decision

The memo's sharp-variable moment loss and the present complete radial-wave exponent are consistent. If the complete unnormalized radial moment has exponent \(b_p\geq1\), its sharp-variable loss is

\[
\lambda_p=(b_p-1)/2,
\qquad
\theta_p=\frac{1+p/4+\lambda_p}{p+1}
=\frac14+\frac{b_p+1/2}{2(p+1)}.
\]

The exponent must be restored for the **complete** real wave before applying this formula. For a residual with exponent \(b_{\rm res}\) and complementary terms paid at \(c_p\), the currently certified exponent is \(b_{\rm full}=\max(c_p,b_{\rm res})\). This maximum is an upper-bound accounting floor, not a lower bound for the physical moment.

For order twelve, strict complete moment improvement and strict pointwise benchmark improvement are different gates:

\[
b_{12}<10\beta=1.289663519481\ldots,
\qquad
b_{12}<13\beta-\tfrac12=1.176562575325\ldots,
\]

where \(\theta=(3292+25\sqrt{1717})/13762\) and \(\beta=2\theta-1/2\). The memo's threshold \(\lambda<13\theta-4\) is exactly the second gate. It does not replace the first gate or the complete-owner accounting.

The memo does not justify resetting present priority to its selected M1 attachment. Its global-moment program is substantially implemented in accepted Rounds204 and216, and the current central-owner interfaces are more specific than its suggested preliminary inventory. Retain the complete actual twelfth-moment priority and the independent direct complete-wave fixed-order family. A different M1 or geometric route can supersede that priority only after a complete, quantitatively stronger admission case. No such case is proved in the supplied memo, and this report does not audit its proposed external transfer.

## 2. Exact statement and hypotheses

Let \(P(x)=\#\{(m,n)\in\mathbb Z^2:m^2+n^2\leq x\}-\pi x\), with the inclusive count for every real \(x\geq2\). Fix the mollifier and window of the accepted kernels: a nonnegative real radial smooth unit-mass function supported in the unit disk, its real even Schwartz transform \(\Psi\), and a fixed nonnegative bounded radial weight \(w(R/T)\) that is at least one on the radii needed to cover \(x\in[Y/2,3Y]\), where \(T=\sqrt Y\). A fixed enlargement or finitely many comparable windows is allowed. All constants may depend on these fixed functions and on a fixed \(p>0\).

Use the actual real wave

\[
B_T(R)=\sum_{n\geq1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
\cos(2\pi R\sqrt n-3\pi/4),\qquad
M_p(B_T)=\int w(R/T)|B_T(R)|^p\,dR.
\]

The accepted reconstruction, uniform over the fixed radial window, is

\[
P(R^2)=\frac{\sqrt R}{\pi}B_T(R)+O_\eta(T^{1/2+\eta})
\quad\text{for every }\eta>0. \tag{1}
\]

It retains the full infinite series and inclusive jumps. Assume, conditionally, that \(M_p(B_T)\ll_{p,\eta}T^{b_p+\eta}\) for every \(\eta>0\). The direct integrated consequence is

\[
\int_{Y/2}^{3Y}|P(x)|^p\,dx
\ll_{p,\epsilon}Y^{1+p/4+\lambda_p+\epsilon},
\qquad
\lambda_p=\max(0,(b_p-1)/2). \tag{2}
\]

For \(b_p\geq1\), (2) and one-sided persistence give the formula in Section1. For general \(b_p\), thresholding the smoothing error before using the radial moment gives the stronger conditional pointwise formula

\[
|P(X)|\ll_{p,\epsilon}
X^{\max(1/4,\;1/4+(b_p+1/2)/(2(p+1)))+\epsilon}. \tag{3}
\]

The simple two-way parameter translation \(b_p=1+2\lambda_p\) applies to the present \(b_p\geq1,\lambda_p\geq0\) regime; it must not be extrapolated through the smoothing floor without qualification. For sharp moments known uniformly over enlarged comparable windows, the inverse of (1) gives radial exponent at most \(1+2\lambda_p\) for \(\lambda_p\geq0\). This is a translation of available bounds, not an equality between optimal unknown exponents.

For the reviewed central-owner interface only, retain its exact \(C_\gamma\), original radius-independent patch starts, literal cutoff equalities, actual \(\chi_4\) weights, real cosine, and infinite smoothing tails. Its permitted range is \(13/125\leq\gamma<\beta\), and its reviewed complementary bound is

\[
M_{12}(B_T-C_\gamma)\ll T^{m(\gamma)+\epsilon},
\qquad m(\gamma)=\max(1,10\gamma,1+20\gamma/13). \tag{4}
\]

Equation (4) is used at its reviewed-evidence status. This report does not convert that packet into an accepted graph theorem or independently reprove its analytic decomposition.

## 3. Proof and quantitative derivation

**Jacobian and smoothing.** The scalar inequality \(|u+v|^p\leq C_p(|u|^p+|v|^p)\), valid for every fixed \(p>0\), and \(dx=2R\,dR\) give from (1)

\[
\int_{Y/2}^{3Y}|P(x)|^p\,dx
\ll T^{1+p/2}M_p(B_T)+T^{2+p/2+\epsilon}. \tag{5}
\]

The first factor \(T\) is the Jacobian, \(T^{p/2}\) is the wave amplitude, and the last term is the smoothing error integrated over an \(x\)-interval of length \(O(T^2)\). Substituting the assumed moment and writing \(Y=T^2\) gives (2). Conversely, solve (1) for \(B_T\), integrate in \(R\), and use \(dR\asymp dx/T\): a uniform sharp moment with loss \(\lambda_p\geq0\) yields \(M_p(B_T)\ll T^{1+2\lambda_p+\epsilon}+T^{1+\epsilon}\). Finite window enlargement changes constants only.

**Persistence, sign, and jumps.** Fix \(x\in[Y,2Y]\) and set \(V=|P(x)|\). If \(P(x)=V>0\), monotonicity of the inclusive count implies \(P(x+h)\geq V-\pi h\). If \(P(x)=-V<0\), it implies \(P(x-h)\leq -V+\pi h\). Therefore \(|P|\geq V/2\) on the relevant one-sided interval of length \(V/(2\pi)\). This uses no continuity assumption and holds across all integer jumps. An elementary sublinear bound ensures that interval lies in \([Y/2,3Y]\) for sufficiently large \(Y\). Integrating gives

\[
V^{p+1}\ll_p\int_{Y/2}^{3Y}|P(t)|^p\,dt. \tag{6}
\]

Equations (2) and (6) yield the memo's formula and, when \(b_p\geq1\), the current radial formula. To obtain (3), separate \(V\ll T^{1/2+\eta}\), already paid at the smoothing scale. Otherwise choose the comparison constant so that (1)'s error is at most \(V/4\) throughout the persistence interval. Then \(|B_T|\gg VT^{-1/2}\) there; its radial length is comparable to \(V/T\). Thus

\[
M_p(B_T)\gg V^{p+1}T^{-1-p/2},
\qquad V\ll T^{(b_p+1+p/2)/(p+1)+\epsilon}.
\]

Restoring \(X\asymp T^2\) proves (3). Input epsilon choices depend on the fixed \(p\) and desired output epsilon; no order grows with \(T\).

**The complete twelve-moment scale.** The graph-accepted Round204 exponent is \(b_{12}=10\beta\), hence \(\lambda_{12}=5\beta-1/2=10\theta-3\). The following conversions are exact; decimals only aid comparison.

| Complete radial exponent | Sharp loss \(\lambda_{12}\) | Sharp moment exponent | Pointwise exponent supplied by this moment |
|---|---|---|---|
| Accepted \(10\beta=1.289663519481\ldots\) | \(10\theta-3=0.144831759740\ldots\) | \(1+10\theta\) | \((1+10\theta)/13=0.318833212287\ldots\) |
| Modest proposed \(32/25\) | \(7/50=0.14\) | \(207/50\) | \(207/650=0.318461538461\ldots\) |
| Benchmark threshold \(13\beta-1/2\) | \(13\theta-4=0.088281287662\ldots\) | \(13\theta\) | \(\theta\), with strict inequality needed for improvement |
| Preferred proposed \(29/25\) | \(2/25=0.08\) | \(102/25\) | \(102/325=0.313846153846\ldots\) |
| Optimal fixed twelve-moment \(1\) | \(0\) | \(4\) | \(4/13\) |

The modest \(32/25\) bound would be a strict improvement of the complete moment, but the previously accepted external pointwise bound would still be stronger. The preferred \(29/25\) bound would improve the benchmark by \(0.000637022127\ldots\). Neither proposed bound is proved here. The memo's optimal absolute eleventh-moment comparison is also arithmetically correct: \((1+11/4)/12=5/16\).

**Complementary-owner restoration.** Write \(B_T=C+E\). The scalar norm inequality in both directions shows that if \(M_{12}(E)\ll T^{c+\epsilon}\), then a residual bound at \(b\geq c\) is equivalent, at epsilon-loss level, to the same complete bound. A smaller residual bound gives only the restored exponent \(\max(c,b)\) from these data. For the previously stated \(W_{\rm low}\), \(c=29/25\); therefore

\[
b_{\rm full}=\max(29/25,b_{\rm low}),\quad
\lambda_{12}=\max(2/25,(b_{\rm low}-1)/2),\quad
E_{\rm sharp}=\max(102/25,(7+b_{\rm low})/2). \tag{7}
\]

This independently recovers the seam repair. In particular, an arbitrarily strong isolated \(W_{\rm low}\) estimate cannot improve the pointwise consequence beyond \(102/325\) using that unchanged complementary budget alone.

For (4), a proposed central exponent \(b_C\) restores to \(\max(m(\gamma),b_C)\). At \(\gamma=16/125\), \(m=32/25\), so this fixed decomposition cannot cross the benchmark gate through a better central estimate alone. At \(\gamma=13/125\), \(m=29/25\), which permits the preferred benchmark-improving target if the missing central bound is supplied.

There is a useful explicit screening threshold. Put \(b_*=13\beta-1/2\). Requiring \(m(\gamma)<b_*\) gives both

\[
\gamma<b_*/10,
\qquad \gamma<\frac{13}{20}(b_*-1).
\]

Since \(b_*<13/11\), the second condition is stricter. Thus this reviewed family can support a strict benchmark gain under its present complementary bounds only if

\[
\gamma<\frac{13}{20}(13\beta-3/2)
=0.114765673961\ldots. \tag{8}
\]

This is a restriction on the displayed restoration certificate. It does not rule out a better complementary estimate, joint cancellation, or a different representation.

**All-order scope.** For an unbounded sequence of fixed even orders, a direct complete-wave family \(b_p=o(p)\) gives the quarter bound by (3): choose an order for the requested epsilon, then keep it fixed as \(T\to\infty\). In the \(b_p\geq1\) regime the equivalent sharp target is \(\lambda_p=o(p)\). The stronger optimal family \(\lambda_p=0\) is sufficient, as the memo says, but not necessary for this implication. The accepted curve \(b_p=\max(1,(p-2)\beta)\) gives a pointwise exponent at least \(\theta+(1-3\theta)/(p+1)>\theta\) at every finite order, approaching \(\theta\) only in the limit.

Accepted216 is specifically a twelfth-order equivalence, not an all-order bridge. Its repeated-class calculation at general order can retain \(Q^{-1/2}[T+T^{(p-4)\beta}]\). Holding its cutoff construction fixed therefore leaves a term linear in \(p\). The direct complete-wave family and an extension of the distinct-class reduction must remain separate obligations.

## 4. First doubtful or unproved step

The first unresolved analytic step is a bound for the actual signed complete quantity at a new power. Within accepted216 it is the distinct-class integral \(I_{12}\); within the reviewed current central interface it is \(M_{12}(C_\gamma)\) after (4) is restored. Neither a new name for this owner nor a correct change of variable supplies that bound.

The accepted exact expansion retains all real cosine signs, all harmonics \(n=ds^2\), all ordered distinct squarefree labels, and \(\widehat w(-T\sum_j\epsilon_js_j\sqrt{d_j})\). Its physical near-resonance scale is \(1/T=Y^{-1/2}\). Exact nonvanishing of these frequencies does not bound their closeness at that scale. Taking absolute values per tuple or per reciprocal fibre may remove precisely the cancellation needed; the reviewed exact-real-resonance zero does not by itself control physically detuned frequencies or their aggregate.

No external theorem is newly imported in this report. The accepted qualified Li--Yang application is inherited as a dependency; the memo's transfer and decoupling source claims require their own algebraic and source audits. A proposed M1 transfer must still pay independent complete owners before it can supersede the current full-wave priority. Its unproved identity or cost cannot be substituted for the moment gap.

## 5. Required controls and outcomes

1. **Normalization control: passed analytically.** A radial wave of constant size has unnormalized moment \(O(T)\); its amplitude \(T^{1/2}\), Jacobian \(T\), and radial length \(T\) produce sharp moment \(T^{2+p/2}=Y^{1+p/4}\). Hence the correct baseline is \(b_p=1,\lambda_p=0\), not \(b_p=0\).
2. **Sign and endpoint control: passed analytically.** Positive discrepancies persist to the right and negative discrepancies to the left. Monotonicity proves (6) with inclusive jumps; no two-sided continuity or differentiability is used.
3. **Smoothing control: passed analytically.** Formula (2) includes the smoothing floor; the separate high-value argument proves (3) without incorrectly claiming that (2) improves when \(b_p<1\).
4. **Complementary-owner control: passed analytically.** Substituting \(b_{\rm low}=1\) into (7) leaves \(b_{\rm full}=29/25\), not (1). Substituting \(\gamma=16/125\) into (4) leaves \(32/25\), even if its central residual were smaller. These are upper-bound limitations, not lower-mass assertions.
5. **Progress classification control: passed.** \(32/25<10\beta\) but \(207/650>\theta\). \(29/25<13\beta-1/2\) and \(102/325<\theta\). The two notions of progress are therefore distinguished explicitly.
6. **All-order and coefficient control: passed at the conditional-statement level.** The real \(r_2\) cosine series is preserved. No arbitrary complex-wave bound, independent-sign model, or twelfth-order class identity is promoted to an unbounded-order family. No new family is claimed.
7. **Bounded numerical diagnostic: passed.** Direct floating-point evaluation of the exact radical expression and rational identities reproduces the displayed thresholds and decimals, including (8). It is a check on arithmetic only. All asymptotic implications above have analytic derivations; numerical work was below five percent of this task.

## 6. Dependencies and exact artifacts used

All paths below are relative to `D:/BaiduSyncdisk/Codex/gauss circle/`. Only named task context was used; no sibling report or unassigned historical file was read. The graph was subsequently parsed selectively for `GC-target`, `M9`, `M9-M1`, `M9-M2`, `GC-complete-square-root-large-values-moment-bound`, and `GC-complete-distinct-radical-twelfth-reduction`. The last two are `proved_internal`; the four parents remain open.

- `protocol.md`.
- `strategy/round231_directive_reconciliation/briefs/moment_strategy_audit.md`.
- `strategy/round231_directive_reconciliation/plan.json`.
- `strategy/next_campaign_gauss_circle_20261011.md`, SHA256 `aff0b81cb3ed71126776a680733fc4e831cf7e198cee8407f13c0354fd908e35`.
- `strategy/gauss_circle_strategy_checkpoint_round230_2026-10-11.md`, SHA256 `d8dadae0d42e0b84a31fda14a132556e3fd2fdccfdf6b37c782564c4721fc34b`.
- `strategy/round231_balanced_cancellation/conductor_decision.md`, SHA256 `54c99e2a8e376bbde73a2697f0f3379f2489a7a054cf3bd3c3382a684b7f23e1`.
- `strategy/round231_balanced_cancellation/conductor_seam_repairs.md`, SHA256 `e4dc22c726eb241e24a4e7c485202ea6b6b567ecc4e16a3708d435ddc82eab14`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, SHA256 `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`; exact dependencies for (1), complete moments, actual mollifier, full tails, and source qualifications.
- `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md`, SHA256 `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee`; accepted twelfth-only reduction and precise signed unresolved integral.
- `state/next_round_plan.yml`, inspected SHA256 `f45951df71e98570b229f5211cf5a49a6388f53ba6ea59cc28072b0220fcbd50`; admission and historical status are used as recorded metadata, not independently re-audited analytic results.
- `state/active_campaign.yml`, inspected SHA256 `fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa`; closed Round230, no analytic Round231 launched.
- `state/proof_obligations.yml`, inspected SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`; authoritative mathematical scope.

## 7. Recommended state effect and useful adopted practice

**Retain** the complete actual twelfth moment as the finite priority, the preferred \(29/25\) target, the separate direct complete-wave fixed-order quarter route, and all current completeness and endpoint requirements. The memo's emphasis on original-discrepancy moments, actual signs, full tails, and full restored exponents is sound; it reinforces existing practice rather than establishing a new estimate.

**Revise strategy presentation only** by adding the explicit translation \(\lambda=(b_{\rm full}-1)/2\) and the two distinct numerical gain thresholds. For each prospective residual estimate, freeze the pair consisting of its exponent and its complementary exponent, and report the resulting complete moment and pointwise consequence. In the parameterized central family, (8) immediately distinguishes decompositions capable of benchmark improvement from those capable only of a modest moment improvement. This is a useful screening refinement, not a new cancellation mechanism or a reason to launch another analytic round.

**Do not adopt** a reset to the memo's Round199 research frontier, a repeated high-moment inventory without changed evidence, or three automatic concurrent research tracks. A selected source attachment remains a candidate until its full identity and restored gain pass the present admission gate. The memo's upper bound of three tracks does not supersede the protocol's one frozen objective per numbered round.

**No mathematical state change.** Do not promote any parent, alter the graph, extend accepted216 to all orders, or call \(32/25\) a pointwise improvement. No new attack or successor is designed. The only task output is this report; its frozen hash is returned separately.
