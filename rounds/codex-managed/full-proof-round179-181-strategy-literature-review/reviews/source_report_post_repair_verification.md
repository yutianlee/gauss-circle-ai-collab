# Round 182 source-report post-repair verification

- Campaign: `full-proof-round179-181-strategy-literature-review`
- Round: `182`
- Role: independent post-repair source verifier
- Starting graph:
  `fec130bc66641cbdad18c832de10077a7825f1caaf5d10170a67ef65c0b27196`
- Claimant report SHA-256:
  `4f58245e8d047af6073820f41a3b47de6403798e0b4e916c0f326b5980b3685f`

## 1. Result

**Verdict: REPAIR.**

The substantive repairs are present and correct.  The Shao--Shparlinski--
Wijaya comparison now uses \(N=p\) and \(p\asymp L^2\), the
Tao--Trudgian--Yang version/date and pair provenance are repaired, and the
Xiao section now contains the exact formal map, failed fourth-moment range,
and non-saving second-moment consequence.  The citation ledger is also
repaired.  The dated named-corpus no-import conclusion, every owner status,
and all three exponent scopes are unchanged.  A byte/character scan found no
malformed control character.

The report is not GREEN because two residual Xiao sentences retain the
categorical claim that the positive moment cannot select or single out
\(t=1\).  The repaired derivation itself correctly proves the opposite:
positivity can isolate that frequency, but only with a non-saving bound far
above the target.  The residual wording occurs in Section 3.4 and again in
the closing recommendation, so bounded repair items 4 and 5 are not yet
fully satisfied.  This is an exposition/source-interface defect only; it
does not change the no-import conclusion.

## 2. Exact statement and hypotheses

The bounded repair audit is:

| Required repair | Repaired claimant text | Outcome |
|---|---|---|
| Shao--Shparlinski--Wijaya scale | Every project comparison uses \(N=p\) and \(p\asymp L^2\); no exact \(p=N=L^2\) remains.  The diagnostic is \(L^{3/2-1/116+o(1)}\). | **PASS** |
| Tao--Trudgian--Yang currency | Official arXiv v1 is recorded as submitted 2025-01-28.  The displayed 2026-08-24 experimental-HTML date is identified as render-time expansion of `\date\today`, not a later author snapshot or arXiv version. | **PASS** |
| Tao--Trudgian--Yang pair provenance | The pair \((195/796,235/398)\) is attributed to Table 1 and Lemmas 13--15, with an explicit statement that it is not one of the four pairs in Theorem 20. | **PASS** |
| Xiao parameter map | The report gives \(n_{\rm Xiao}\asymp L^2/t^2\), \(h=t\sqrt X\), and \(H\asymp t\sqrt X\), while retaining the integer-frequency obstruction for general real \(X\). | **PASS** |
| Xiao fourth-moment range | On \(X=J^2\), \(L\asymp X^{1/6}\), \(t=1\), the report checks that \(H\asymp X^{1/2}\) cannot satisfy \(H\le n_{\rm Xiao}^{2/3}\asymp X^{2/9}\). | **PASS** |
| Xiao second-moment restoration | Positivity is used to obtain \(\lvert S(tJ,n_{\rm Xiao})\rvert\ll X^{1/4}Lt^{-1/2}X^\varepsilon\), hence \(X^{5/12+\varepsilon}\) on the critical \(t=1\) shell, above both raw capacity \(X^{1/3}\) and target \(X^{1/4}\). | **PASS** |
| Xiao pointwise wording | The opening summary correctly says “no target-sized coefficient-literal pointwise bound,” but Section 3.4 says “Xiao's moment cannot single out \((t=1)\).” | **REPAIR** |
| Citation ledger and closing recommendation | The ledger carries the repaired TTY metadata and provenance.  The closing Shao scale is repaired, but its Xiao recommendation says that the moment “cannot select \((t=1)\).” | **REPAIR** |

The relevant primary hypotheses remain:

- Shao--Shparlinski--Wijaya Theorem 1.1 assumes a prime \(p\), an integer
  \(s\ge2\), an even positive integer \(\ell\), and
  \(p^{1/2+2/\ell}\le N\le p\).  At \(N=p,\ell=8\), it gives
  \(p^{3/4-1/232+o(1)}\).
- Xiao Theorem 1.1 is the positive second moment over integer
  \(h\sim H\), uniformly for \(H\ge n^{1/2+\delta}\).  Theorem 1.2 is the
  fourth moment for fixed \(0<\delta<1/6\) and
  \(n^{1/2+\delta}\le H\le n^{2/3}\).
- The official Tao--Trudgian--Yang record contains only arXiv v1, submitted
  2025-01-28.  Its v1 TeX contains `\date\today`.  Table 1 records
  \[
    D\!\left(\frac{13}{84},\frac{55}{84}\right)
      =\left(\frac{18}{199},\frac{593}{796}\right),
  \]
  and Lemmas 13--15 authorize the displayed \(D\)- and \(B\)-processes.

## 3. Proof or derivation

For Shao--Shparlinski--Wijaya, Theorem 1.1 at \(N=p,\ell=8\) gives

\[
 p^{3/4-1/232+o(1)}.
\]

The source requires \(p\) to be prime, so the lawful fictional project map is
\(p\asymp L^2\), not the exact identity \(p=L^2\).  Restoring the scale gives

\[
 p^{3/4-1/232+o(1)}
   \asymp L^{\,2(3/4-1/232)+o(1)}
   =L^{3/2-1/116+o(1)}.
\]

All four claimant occurrences of the fictional comparison use the lawful
\(N=p,\ p\asymp L^2\) formulation.

For Xiao, on the diagnostic square subfamily \(X=J^2\), the project phase
has the formal map

\[
 n_{\rm Xiao}\asymp\frac{L^2}{t^2},\qquad
 h=tJ=t\sqrt X,\qquad
 H\asymp t\sqrt X.
\]

At \(t=1\) and \(L\asymp X^{1/6}\),

\[
 n_{\rm Xiao}\asymp X^{1/3},\qquad H\asymp X^{1/2}.
\]

Xiao's fourth-moment upper hypothesis would require

\[
 X^{1/2}\asymp H
   \le n_{\rm Xiao}^{2/3}
   \asymp X^{2/9},
\]

which fails.  The second moment is available, and positivity does isolate
one integer frequency:

\[
 |S(tJ,n_{\rm Xiao})|^2
 \le \sum_{h\sim H}|S(h,n_{\rm Xiao})|^2
 \ll Hn_{\rm Xiao}^{1+\varepsilon}.
\]

Therefore

\[
 |S(tJ,n_{\rm Xiao})|
 \ll X^{1/4}Lt^{-1/2}X^\varepsilon.
\]

At the critical \(t=1\) shell this is \(X^{5/12+\varepsilon}\), whereas
the raw coefficient-one capacity is \(L^2=X^{1/3}\) and the desired budget
is \(L^{3/2}=X^{1/4}\).  Thus “cannot select/single out” is false literally;
“supplies no target-sized coefficient-literal pointwise estimate” is the
exact conclusion.  The joint coefficient, hard zero extension, and sparse
frequency section remain further literal failures.

For Tao--Trudgian--Yang, the claimant now correctly applies the \(B\)-process
to the Table-1 \(D\)-pair:

\[
 B\!\left(\frac{18}{199},\frac{593}{796}\right)
   =\left(\frac{195}{796},\frac{235}{398}\right).
\]

With \(N_t\asymp L^2/t^2\) and \(T\asymp\sqrt X\,L\),

\[
 (T/N_t)^{195/796}N_t^{235/398}
   =X^{195/1592}L^{745/796}t^{-550/796}.
\]

Comparison with \(L^{3/2}t^{-3/2}\) is exactly

\[
 (\sqrt X)^{195}t^{644}\le L^{449}.
\]

This remains only a coefficient-one/normalized-BV diagnostic, so it does
not import a project owner.

Finally, the repaired report retains

\[
 \theta_{\rm internal}=\frac13,\qquad
 \theta_{\rm audited,external}
 =\frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots,\qquad
 \theta_{\rm target}=\frac14.
\]

No R179 residual, R180 residual, R181 residual, parent, endpoint, bridge,
\(M9\), quarter theorem, or exponent status changes.

## 4. First doubtful or unproved step

The first remaining report defect is the first sentence of Section 3.4:
“Xiao's moment cannot single out \((t=1)\).”  This contradicts the repaired
calculation earlier in the same report, where positivity explicitly
isolates a single frequency and gives a non-saving bound.  The same defect
recurs in recommendation 4 as “cannot select \((t=1)\).”

The exact bounded repair is sentence-level:

1. replace the Section-3.4 sentence by “Xiao's second moment isolates
   \(t=1\) only at the non-saving scale derived in Section 2.3 and supplies
   no target-sized coefficient-literal estimate”; and
2. replace the recommendation phrase by “a dense positive frequency moment
   gives only the non-saving single-frequency bound at \(t=1\).”

No primary-source, arithmetic, restored-power, owner-status, or exponent
defect remains in the bounded repair set.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| No residual exact \(p=N=L^2\) identification | **PASS** |
| Shao restored diagnostic \(L^{3/2-1/116+o(1)}\) | **PASS** |
| TTY official-v1 date and `\date\today` explanation | **PASS** |
| TTY Table-1/Lemmas-13--15 provenance | **PASS** |
| Xiao exact formal map | **PASS** |
| Xiao failed fourth-moment upper range | **PASS** |
| Xiao non-saving second-moment single-frequency bound | **PASS** |
| Only target-sized pointwise nonimport language | **REPAIR**; two categorical residual sentences remain |
| Citation ledger | **PASS** |
| Closing recommendations | **REPAIR**; recommendation 4 repeats the Xiao wording defect |
| Dated named-corpus no-import scope | **PASS** |
| Owner statuses | **PASS**; all remain unchanged |
| Internal/external/target exponent scopes | **PASS**; \(1/3\), \(0.3144831759740614\ldots\), and \(1/4\) are retained |
| Malformed control-character scan | **PASS**; zero C0 controls other than line endings, zero DEL, zero U+FFFD/U+2028/U+2029, and zero NUL bytes |

Overall outcome: **REPAIR**.

## 6. Dependencies and exact artifacts used

- `protocol.md`;
- `rounds/codex-managed/full-proof-round179-181-strategy-literature-review/briefs/source_report_post_repair_verification.md`;
- `rounds/codex-managed/full-proof-round179-181-strategy-literature-review/reviews/source_hypotheses_currency_interface_review.md`;
- `rounds/codex-managed/full-proof-round179-181-strategy-literature-review/reports/current_primary_literature_reassessment.md`, SHA-256
  `4f58245e8d047af6073820f41a3b47de6403798e0b4e916c0f326b5980b3685f`;
- Shao--Shparlinski--Wijaya
  [official arXiv v1 record](https://arxiv.org/abs/2411.12113) and
  [v1 theorem text](https://arxiv.org/html/2411.12113v1);
- Xiao [official arXiv v1 record](https://arxiv.org/abs/2606.28986) and
  [v1 theorem text](https://arxiv.org/html/2606.28986v1); and
- Tao--Trudgian--Yang
  [official arXiv v1 record](https://arxiv.org/abs/2501.16779),
  [official v1 TeX archive](https://arxiv.org/src/2501.16779v1), and
  [experimental v1 HTML](https://arxiv.org/html/2501.16779v1).

Only the assigned post-repair review file was written.

## 7. Recommended state effect

Do not mark the claimant source report GREEN until the two Xiao sentences
identified in Section 4 are repaired and this bounded seam is rerun.  Retain
`strategy_source_update_only`; make no analytic graph or exponent change.
Every R179--R181 residual and every parent, endpoint, bridge, \(M9\), quarter
theorem, and exponent must retain its current status.

**Final verdict: REPAIR.  Recommended state effect:
`strategy_source_update_only`; no analytic promotion.**
