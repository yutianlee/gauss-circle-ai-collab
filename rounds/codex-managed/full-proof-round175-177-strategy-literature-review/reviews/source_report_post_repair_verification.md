# Round 178 source-report post-repair verification

## 1. Result

**Verdict: GREEN.**

Every bounded repair required by the independent source-hypotheses review is
present in the Round-178 source report.  The repaired text agrees with the
official primary records, contains no stray control character, and leaves the
source-interface and exponent conclusions unchanged.  No analytic claim,
owner, bridge, or exponent is promoted by this verification.

## 2. Exact statement and hypotheses

The repaired items are:

| Required repair | Repaired report text | Verification |
|---|---|---|
| Shen Theorem 1 | odd prime \(q\), \(1\le N\le q-1\), \(0<\delta<1/4\), and the printed lower bound on \(N\) | **PASS** |
| Shen Theorem 3 unit multiplier | \((k,q)=1\) now appears alongside the prime and range hypotheses; the section has already declared integer \(s\ge1\) | **PASS** |
| Shen Theorem 4 | \(\sum_{\substack{q\sim Q\\q\ {\rm odd}}}|\Delta(\alpha,N;q)|^2\ll_\varepsilon\|\alpha\|_2^2N^{11/12}Q^{1+\varepsilon}\) | **PASS** |
| Dong metadata | Anji Dong; *Bilinear forms with Kloosterman fractions and applications*; v2 withdrawn 2026-01-05 | **PASS** |
| Guo title nuance | official abstract-record title distinguished from the rendered v3 internal title | **PASS** |
| Citation ledger | Dong title/name/status and \(L^2\) notice recorded; Shen, Guo, Chen--Lin, Mirzoabdughafurov, and Li--Yang versions/statuses retained | **PASS** |

The official Shen v1 text, Dong withdrawal record, Guo v3 abstract/HTML
records, and Li--Yang v2 record support these transcriptions.

## 3. Proof or derivation

The repaired Shen hypotheses do not alter the power calculation.  In the most
favorable fictional specialization \(R,N\asymp q\), \(s=1\), Theorem 3 has
bracket

\[
\frac{q^2\log q}{RN^2}+\frac1N
\asymp \frac{\log q}{q},
\]

and hence supplies only \(q^{-1/2+o(1)}\).  Restoring the project scale still
gives \(L\sqrt q\,q^{o(1)}\), not the required \(L X^\varepsilon\).  The
literal application continues to fail earlier at prime modulus and
coefficient/support class.

Theorem 4 remains a positive modulus-average second moment.  At
\(Q\asymp N\), division by the number of moduli and square root gives only
RMS size \(\|\alpha\|_2N^{11/24+\varepsilon}\); it neither selects the fixed
supported packet nor preserves its outer signs.

Dong--Robles--Zeindler remains nonimportable because v2 is withdrawn and its
notice changes \(L^5\) to \(L^7\).  No post-withdrawal power restoration is
legal.

Li--Yang remains a pointwise theorem in the area variable
\(R(X)=\sum_{m^2+n^2\le X}1-\pi X\), with

\[
\theta_{\rm LY}
=\frac{3292+25\sqrt{1717}}{13762}
=0.3144831759740614\ldots .
\]

Thus the repaired report still supports internal exponent \(1/3\), external
audited benchmark \(\theta_{\rm LY}\), and target \(1/4\), with no new global
exponent.

## 4. First doubtful or unproved step

No doubtful step remains in the bounded repair set.  The first unresolved
matter is external to this verification: no theorem in the dated named corpus
has been mapped hypothesis-validly and power-sufficiently to a live project
interface.  The report states this only as a corpus-scoped search result, not
as universal nonexistence.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Exact Shen hypotheses | **PASS** |
| Theorem 4 formula and byte/control-character audit | **PASS**; no embedded or non-line-ending carriage return remains |
| Dong author/title/version/withdrawal notice | **PASS** |
| Guo abstract-record versus internal-title distinction | **PASS** |
| Primary-source citation ledger | **PASS** |
| Shen and Dong restored-power handling | **PASS** |
| Li--Yang pointwise area-variable exponent scope | **PASS** |
| Dated corpus-scoped no-match language | **PASS** |
| No analytic promotion | **PASS** |

Overall outcome: **GREEN**.

## 6. Dependencies and exact artifacts used

- `protocol.md`;
- `strategy/round178_full_proof_strategy_current_literature_review.md`;
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reports/current_primary_literature_reassessment.md`;
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reviews/source_hypotheses_currency_interface_review.md`;
- Shen [arXiv:2607.06575v1](https://arxiv.org/abs/2607.06575) and
  [v1 HTML](https://arxiv.org/html/2607.06575v1);
- Dong--Robles--Zeindler
  [arXiv:2601.00292v2](https://arxiv.org/abs/2601.00292);
- Guo [arXiv:2608.23500v3](https://arxiv.org/abs/2608.23500) and
  [v3 HTML](https://arxiv.org/html/2608.23500v3); and
- Li--Yang [arXiv:2308.14859v2](https://arxiv.org/abs/2308.14859) and
  [v2 HTML](https://arxiv.org/html/2308.14859v2).

Only the assigned post-repair review file was written.

## 7. Recommended state effect

Accept the repaired source report as **GREEN source evidence**.  Retain all
analytic graph statuses and retain
\[
\theta_{\rm internal}=\frac13,\qquad
\theta_{\rm audited,external}=0.3144831759740614\ldots,\qquad
\theta_{\rm target}=\frac14.
\]
Any State Patch supported by this source audit remains provenance/evidence
only, under `strategy_source_update_only`; it must not promote a proof node,
bridge, quarter theorem, or exponent.
