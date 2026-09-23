# Blind Round-171 frontier selection

**Role:** statement-only blind frontier selector
**Isolation:** This report used only `protocol.md` and `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/blind_statement.md`. It did not inspect the proof graph, campaign state, strategy or source files, web results, sibling reports, conductor artifacts, or earlier-round artifacts.
**Status:** strategic recommendation only; no mathematical claim or proof status is promoted here.

## 1. Result: selection lemma and bounded no-go

### Selection lemma

On exactly the information in the blind statement, the uniquely best *Round-171-sized* frontier is the signed maximal-window correlation over the already-isolated even medium and long shifts:

\[
\boxed{
  \left|K_{26}^{\mathrm{signed},\,\mathrm{even},\,
  \mathrm{medium+long}}\right|
  \ll_{\varepsilon} L^3X^{\varepsilon}.
}
\tag{R171-K26}
\]

This is a choice of the next falsifiable analytic inequality, not a claim that the inequality is true. Its advantage is local and comparative: among the three exposed hard-TOP \(t=1\) kernels, it has no *stated* positive-capacity deficit in a power of \(L\), its short-shift diagonal part has already been separated and paid, and it retains the signed coefficient aggregate on precisely the unresolved medium/long range. It still closes at most one residual face and therefore cannot by itself close hard TOP.

### Bounded no-go

None of the other listed programs is a better single-round objective on the supplied information. K17a has a certified factor-\(L\) gap between target and positive capacity; (B170.1) has an explicit dualization loop back to the moving product collar and no estimate at its only positive saddle; and every parent-level or exponent-level alternative lacks an exposed atomic inequality together with a visible new cancellation mechanism. Thus Round 171 should not be broadened to a full parent or to a vague “improve the exponent” program.

## 2. Exact statement and hypotheses

The literal Round-171 objective is (R171-K26), with the following hypotheses and conventions fixed at the interface level supplied by the blind statement.

1. \(K_{26}^{\mathrm{signed},\mathrm{even},\mathrm{medium+long}}\) means the inherited K26 signed aggregate, with exactly its inherited normalization and admissible parameter ranges, restricted to even medium and long shifts.
2. Short shifts are excluded from the left side. They remain charged exactly once to the already-paid diagonal energy budget and may not be re-imported as a source of cancellation or absorbed into the right side a second time.
3. The estimate is uniform over every block, endpoint, dyadic, and auxiliary parameter occurring in the inherited K26 definition. The implicit constant may depend on \(\varepsilon\), but not on those parameters.
4. The actual inherited coefficient signs must remain in the aggregate. Absolute values may not be inserted before the medium/long shift summation.
5. No external source theorem is a dependency of (R171-K26). In particular, the stated external exponent \(0.3144831759740614\ldots\) is only a benchmark in this report.
6. The conclusion is only the K26 inequality. A separate exact seam is required before it can affect its residual owner; no hard-TOP parent, M2 parent, M9 node, endpoint, or final target follows merely from writing (R171-K26).

Because the blind packet deliberately does not reproduce the summand-level definition of K26, the Round-171 brief must quote that inherited definition verbatim before work begins. That is a normalization requirement, not permission to alter the displayed target, shift range, or signs.

### Promotion gate

(R171-K26) is promotion-eligible only if all of the following are green:

- a complete uniform analytic proof of (R171-K26), with the exact K26 normalization and no hidden power or logarithmic loss beyond \(X^\varepsilon\);
- an exact accounting showing that short shifts are excluded and paid exactly once by the diagonal energy budget;
- a line that identifies the concrete Vaaler/character coefficient identity responsible for cancellation, rather than using only coefficient boundedness, generic mean-zero language, or positive-operator capacity;
- negative unsigned and adversarial-sign controls, as specified below;
- a normalization/multiplicity seam showing exactly how (R171-K26) discharges its immediate residual owner and showing that it does not silently claim the rest of hard TOP; and
- independent hostile and seam review under the protocol. Computation, if used, remains diagnostic only.

## 3. Proof/derivation of the ranking

The ranking criterion is: first minimize the certified missing saving and hidden connector for an atomic inequality; then use owner leverage; finally discount any route for which no genuinely new cancellation mechanism is visible. High downstream leverage cannot compensate for an undefined or round-sized-unbounded objective.

| Rank | Frontier | Target versus stated capacity | Exact owner leverage | Hidden connector and mechanism diagnosis |
|---:|---|---|---|---|
| 1 | **K26 signed even medium/long aggregate** | Target \(L^3X^\varepsilon\). No positive capacity is stated, so no capacity equality is assumed; importantly, the packet advertises no extra power-of-\(L\) deficit. | At most one residual face; hard TOP and all other parents remain. | Must convert the inherited signs into cancellation across even medium/long shifts. Short shifts are already removed, so there is no unresolved diagonal connector. This is the narrowest place where genuine coefficient cancellation could still act. |
| 2 | **K17a minimal-window residual** | Target \(L^2X^\varepsilon\), positive-operator capacity \(L^3X^\varepsilon\): an explicit full factor \(L\) is missing. | At most one residual face; it does not close hard TOP. | The determinant quadratic-form model is exact and fixed polylogarithmic shift sectors are proved, but a new global connector must sum the remaining sectors while recovering \(L\). Sectorwise proofs and positivity alone cannot do this. |
| 3 | **Full \(t=1\) signed aggregate (B170.1)** | Main target \(L^{3/2}X^\varepsilon\); even the displayed error \(L^2/J\) must be compatible with it (formally requiring \(J\gtrsim L^{1/2}X^{-\varepsilon}\) at that comparison). No main-term estimate is supplied. | At most the complete \(t=1\) face; other hard-TOP faces and all other parents remain. This is more face-level leverage than a residual, but not enough to offset the analytic gap. | The \(\chi_4(k)\) sign and full selector-free scalar are visible, but bare dualization is already known to return to the moving product collar. The positive saddle \(k\ell=XQR\), \(Q\ell\le Rk\le4Q\ell\), therefore needs a genuinely new treatment, not another transform of the same type. |
| 4 | **Remaining hard-TOP few-point channels and collars** | No single target/capacity pair is supplied; several unresolved pieces remain. | Completing the whole bundle would close one of the three route-independent M2 parents, leaving BAL, UNBAL, and the chosen M1 side. | It is not an atomic Round-171 objective. Combining several collars would conceal which connector supplies a saving and would violate the one-frozen-objective discipline. |
| 5= | **BAL** | No exposed inequality, capacity, coefficient formula, or required saving is supplied. | One of three M2 parents, required on both accepted routes; hard TOP and UNBAL plus the M1 side remain. | Route-independent leverage is high, but there is no visible proof kernel or new mechanism from which to design a bounded round. |
| 5= | **UNBAL** | No exposed inequality, capacity, coefficient formula, or required saving is supplied. | One of three M2 parents, required on both accepted routes; hard TOP and BAL plus the M1 side remain. | Same information-level diagnosis as BAL. The blind packet gives no lawful basis for breaking the tie. |
| 7 | **Global angular-radial theorem (GAR)** | No target/capacity pair or finite kernel is supplied. | One theorem would satisfy the alternative route's M1 requirement, but would leave all three M2 parents and would not prove either blockwise M1 node. | Its owner leverage is larger than one direct M1 parent, but the scope is global and no new angular-radial cancellation mechanism is exposed. It is not yet a round-sized inequality. |
| 8= | **First direct M1 parent** | No target/capacity pair or candidate mechanism is supplied. | Only one of two independent M1 parents on the standard route; the other M1 parent and all three M2 parents remain. | No atomic frontier is visible in the packet. |
| 8= | **Second direct M1 parent** | No target/capacity pair or candidate mechanism is supplied. | Symmetrically, only one of two independent M1 parents on the standard route; the other M1 parent and all three M2 parents remain. | The blind packet gives no basis for distinguishing the two direct parents. |
| 10 | **Endpoint uniformity, blockwise assembly, and final bridge** | These are implication/uniformity seams, not a supplied cancellation inequality with a capacity comparison. | They can close the final route only after the required M1 and M2 parents exist; at present they close no missing parent. | Starting here would necessarily assume open parents or prove only a conditional shell. The hidden connector is precisely uniform passage from all blocks/parents to the pointwise endpoint. |
| 11 | **Lawful exponent route** | Internal benchmark \(1/3\) misses \(1/4\) by \(1/12\). The stated external benchmark misses it by \(0.0644831759740614\ldots\). Merely becoming sub-one-third is therefore insufficient. | A genuine \(1/4\) theorem could have maximal leverage, but no such theorem or exact reduction is supplied and the external theorem may not be assumed here. | No mechanism is visible that produces the full remaining exponent gain or connects a generic sub-one-third estimate to the target. “Improve the exponent” is not a literal analytic inequality and would be an unbounded round. |

The decisive comparison among the top three is not that K26 is already within capacity—the packet does not state its capacity. It is that K17a is known to be outside positive capacity by \(L\), while (B170.1) is known to loop under the most immediate transform, whereas K26 has a clean residual range, the desired signed aggregate, and no advertised power deficit. Hence K26 has the smallest *certified* obstruction. Its low owner leverage is shared by the other two candidate kernels, so owner leverage does not reverse the ordering.

Every alternative ranks below K26 for a distinct reason:

- **K17a:** quantified factor-\(L\) missing saving and an unproved local-to-global shift connector.
- **(B170.1):** stronger scalar target, a live moving-product collar, and an explicit no-progress result for bare dualization.
- **remaining hard TOP:** multiple unresolved channels rather than one frozen inequality.
- **BAL/UNBAL:** indispensable parent leverage but no exposed kernel, capacity, or mechanism; they are tied on the available evidence.
- **either direct M1 parent:** route-specific and only half of the standard M1 requirement, with no candidate inequality supplied.
- **GAR:** better M1 owner leverage, but it is a new complete global theorem, leaves all M2 parents, and supplies no blockwise M1 result.
- **endpoint/assembly/bridge:** downstream-only while the parent hypotheses are absent.
- **exponent routes:** the known benchmarks remain strictly above \(1/4\), and “sub-one-third” is not enough.

## 4. First doubtful or unproved step

The first unproved step is the existence of an exact identity or orthogonality principle for the *actual inherited K26 coefficients* that gives cancellation after summing the even medium and long shifts at the full maximal window.

The word “signed” is not itself a saving. Before applying Cauchy--Schwarz, a large sieve, a determinant estimate, or a shift decomposition, Round 171 must display the coefficient pairing and show why it survives the whole medium/long range. If the first reduction replaces the coefficients by their magnitudes, bounds only a positive operator, or treats shifts independently and then sums their bounds, it has already lost the only potential mechanism and cannot meet the promotion gate.

No such identity appears in the blind statement, so (R171-K26) remains genuinely unproved.

## 5. Required control tests and outcomes

### False controls required in Round 171

1. **Unsigned control.** Replace every inherited signed coefficient in K26 by its absolute value. The proof of (R171-K26) must have a specific line that becomes unavailable. A proof that survives this replacement is rejected, because it would establish the forbidden unsigned analogue.
2. **Adversarial-sign control.** Permit arbitrary phases/signs chosen to align the medium/long-shift summands. Again, the claimed cancellation line must fail. Generic boundedness or a sign-blind operator norm does not pass.
3. **Coefficient-structure control.** Remove or scramble the relevant Vaaler/\(\chi_4\) coefficient relation while preserving coefficient magnitudes. The proof must identify the exact algebraic relation it loses. Merely citing “oscillation” is not an outcome.
4. **Short-shift leakage control.** Restore the excluded short shifts without their diagonal payment. Any argument that still claims the same budget without a new estimate is rejected; conversely, the valid proof must show where the medium/long restriction is used.
5. **Multiplicity and endpoint control.** Test the extremal admissible endpoints and the largest allowed multiplicity in the inherited K26 normalization. The same \(L^3X^\varepsilon\) constant must be uniform, with no concealed block-count factor.

### Present outcome

At the statement-only selection stage, these controls are **not green**, because no K26 derivation was supplied or attempted. The logical erasure test already rules out an entire proof class: any chain using only absolute values, positive capacity, or coefficient magnitudes would be unchanged in the unsigned/adversarial models and is therefore inadmissible. This is a successful negative control on method selection, not evidence for (R171-K26). The inequality must remain unpromoted until all five controls have concrete outcomes against an actual proof.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read or used:

1. `protocol.md` — authority, round discipline, promotion rules, false-control requirements, and the seven-part report contract.
2. `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/blind_statement.md` — all mathematical targets, capacities, route counts, exponent benchmarks, and the three candidate frontiers used in the ranking.

No proof-state file, graph, active campaign, source card, source theorem, web result, strategy report, sibling report, conductor artifact, or historical round is a dependency. No computation was used. The external exponent was treated only as a stated benchmark and not as an assumed theorem.

## 7. Recommended state effect, Round-171 stop rule, and disposition

### Recommended state effect now

**No change.** This report recommends a next-round objective but proves no mathematical inequality and authorizes no proof-state mutation.

### Exactly one Round-171 objective

Freeze only (R171-K26): prove the inherited signed K26 aggregate over even medium and long shifts is \(\ll_\varepsilon L^3X^\varepsilon\), uniformly and with the actual coefficient algebra retained. K17a, (B170.1), all other hard-TOP channels, BAL, UNBAL, M1, GAR, endpoint assembly, and exponent improvement are expressly out of scope for that round.

### Stop rule

Stop Round 171 and return a rigorous no-go report—without switching to another frontier—at the first of the following events:

1. after the exact K26 coefficient expansion and one full cancellation attempt, no identity distinguishes the actual signs from the unsigned or adversarial-sign controls;
2. the argument reaches only a positive-capacity/absolute-value bound, treats shifts independently and loses an uncancelled power of \(L\), or requires an unproved estimate whose strength is equivalent to (R171-K26);
3. the argument must borrow the already-paid short-shift diagonal budget, creates an untracked multiplicity or endpoint loss, or loops into K17a or the moving product collar without a strictly stronger invariant; or
4. either false analogue would follow from the proposed proof.

If the promotion gate is met, recommend promotion of **only** the normalized K26 inequality and its exact immediate-owner seam. If it is not met, retain the resulting obstruction/no-go as evidence and make no proof-status change. The conductor must close and assess Round 171 before choosing any successor objective.
