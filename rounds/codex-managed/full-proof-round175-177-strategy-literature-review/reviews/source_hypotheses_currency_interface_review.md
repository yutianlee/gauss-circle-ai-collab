# Round 178 source-hypotheses, currency, and interface review

## 1. Result

**Verdict: REPAIR.**

The report's analytic source conclusion survives independent checking: the
audited sources do not furnish a literal import for the live project owners,
Shen restores only one square root of conductor, the Dong--Robles--Zeindler
record is withdrawn before any power comparison is legal, and Li--Yang remains
a pointwise area-variable benchmark with exponent

\[
\theta_{\rm LY}
=\frac{3292+25\sqrt{1717}}{13762}
=0.3144831759740614\ldots .
\]

The dated no-match is also properly limited to the named corpus and the
official math.NT listing through 27 August 2026.  Thus there is no source-side
reason to change any proof owner or exponent.

The report is not GREEN because its exact-hypothesis transcription has several
local defects.  The first is an incomplete statement of Shen's Theorem 1;
later, Shen's Theorem 3 omits the unit-multiplier hypothesis, the displayed
Theorem 4 congruence condition contains an embedded carriage return, and the
Dong citation gives the wrong first initial and omits the current title.  These
are repairable source-record defects, not grounds for RED and not changes to
the mathematical no-import conclusion.

## 2. Exact statement and hypotheses

### 2.1 Shen

The current official record is Qixiang Shen, *A problem of D. H. Lehmer in
short intervals. II*, [arXiv:2607.06575v1](https://arxiv.org/abs/2607.06575),
submitted 2 July 2026.  The [v1 theorem text](https://arxiv.org/html/2607.06575v1)
states:

- Theorem 1: \(q\) is an odd prime, \(1\le N\le q-1\), and
  \(0<\delta<1/4\), in addition to
  \(N\ge q^{1/2}\exp(- (\log q)^{1/2-2\delta})\).
- Theorem 2: \(q\) is prime, \((k,q)=1\), \(1<R<q/2\), \(R<N<q\), and
  \(s\in\mathbb Z_{>0}\), for the separable sum
  \(\Sigma_k(\boldsymbol\alpha;R,N,q)\).
- Theorem 3: \(q\) is prime, **\((k,q)=1\)**,
  \(1<R<q/2\), \(1<N<q\), and \(s\in\mathbb Z_{>0}\).
- Theorem 4: \(1<N<Q\), with arbitrary coefficients, and

  \[
  \sum_{\substack{q\sim Q\\q\ {\rm odd}}}
  |\Delta(\boldsymbol\alpha,N;q)|^2
  \ll_\varepsilon
  \|\boldsymbol\alpha\|_2^2N^{11/12}Q^{1+\varepsilon}.
  \]

Lemma 1 places an absolute value around each inverse-mode row before the
outer mode sum.  The report's coefficient-class and absolute-value objections
are therefore source-faithful.

### 2.2 Dong--Robles--Zeindler

The current record is **Anji Dong**, Nicolas Robles, and Dirk Zeindler,
*Bilinear forms with Kloosterman fractions and applications*,
[arXiv:2601.00292v2](https://arxiv.org/abs/2601.00292), last revised and
withdrawn 5 January 2026.  The official notice says that a missed factor
\(L^2\) in equation (2.53) changes \(L^5\) to \(L^7\), so the claimed improved
bound no longer follows.  The report's use of withdrawal as the first failed
condition is exact.  Its citation “Y. Dong” is not current metadata and must be
changed to “A. Dong” or “Anji Dong”; the title should be recorded explicitly.

### 2.3 Li--Yang and the exponent scope

The current record is Xiaochun Li and Xuerui Yang, *An improvement on Gauss's
Circle Problem and Dirichlet's Divisor Problem*,
[arXiv:2308.14859v2](https://arxiv.org/abs/2308.14859), revised 14 September
2023, with no journal reference on the audited arXiv record.  In the
[v2 theorem text](https://arxiv.org/html/2308.14859v2), equation (1.1) defines

\[
R(X)=\sum_{m^2+n^2\le X}1-\pi X,
\]

so \(X\) is the area/squared-radius variable.  Theorem 1.2 is pointwise, not
averaged or almost-all, and states for every ε that

\[
R(X),\ \Delta(X)=O_\varepsilon(X^{\theta^*+\varepsilon}),
\qquad \theta^*=0.314483\ldots .
\]

Definition 1.1 specifies \(-\theta^*\) as the unique root in
\([-0.35,-0.3]\) of its printed equation.  Direct substitution shows that the
radical displayed by the report gives exactly that root.  Extending the
asymptotic statement over the finite interval down to every real \(X\ge2\)
only enlarges the implicit constant.  The report also correctly confines use
to the already repaired final Theorem 1.2 application and does not promote the
general Proposition 3.1 or Theorem 4.2.

### 2.4 Current titles, arrivals, and cutoff

The arXiv abstract records confirm the report's three stated title repairs:

- Alexandru Pascadi, *Non-abelian amplification and bilinear forms with
  Kloosterman sums*, [arXiv:2511.08445v2](https://arxiv.org/abs/2511.08445),
  revised 21 June 2026;
- Chung-Hang Kwan, *Spectral Moment Formulae for GL(3) x GL(2) L-functions
  II: The Eisenstein Case*,
  [arXiv:2310.09419v3](https://arxiv.org/abs/2310.09419), revised 16 March
  2026 and recorded as JIMJ 25(4) (2026), 2265--2312; and
- Liyang Yang, *Spectral Reciprocity: A Fourier--Analytic Approach*,
  [arXiv:2512.03305v1](https://arxiv.org/abs/2512.03305), submitted
  2 December 2025.

The official [math.NT new listing](https://arxiv.org/list/math.NT/new) is
headed “Thursday, 27 August 2026” and contains the relevant new/replacement
records.  It confirms Chen--Lin
[2608.25812v1](https://arxiv.org/abs/2608.25812) as Selberg-conditional and
averaged over primitive even characters with factorized moduli; it confirms
Mirzoabdughafurov [2608.25787v1](https://arxiv.org/abs/2608.25787) as a
coefficient-one polynomial Weyl-sum theorem of degree at least three; and it
confirms Guo [2608.23500v3](https://arxiv.org/abs/2608.23500) as a
logarithmically weighted shift-average/almost-all result.  One metadata nuance
should be preserved: Guo's arXiv abstract-record title is *Logarithmic Chowla
Correlations Uniformly over Fixed Polylogarithmic Shift Ranges*, whereas the
rendered v3 manuscript internally titles itself *Quantitative Logarithmic
Chowla Correlations over Growing Shift Ranges*.  The report uses the official
abstract-record title; adding the internal-title discrepancy would make the
version audit unambiguous.

## 3. Proof or derivation

For Shen Theorem 3, take the report's deliberately favorable fictional
specialization \(R,N\asymp q\).  With \(s=1\), the bracket is

\[
\frac{q^2\log q}{RN^2}+\frac1N
\asymp \frac{\log q}{q}.
\]

Thus the theorem gains only \(q^{-1/2+o(1)}\) relative to the raw separable
row.  Larger \(s\) is weaker here because the \(s/N\) term, after the
\(1/(2s)\) power, gives only \(q^{-1/(2s)}\).  Applying one square root to the
already restored project capacity gives

\[
Lq\log(2q)\,q^{-1/2+o(1)}
=L\sqrt q\,q^{o(1)},
\]

not the \(L X^\varepsilon\) target.  The literal use fails still earlier:
Theorems 2--3 require a prime modulus and a separable outer coefficient with
an initial inverse row, whereas the project conductor may be composite and
the coefficient retains its joint symbol, orientations, lifts, and hard
support.

For Shen Theorem 4, averaging its right-hand side over \(\asymp Q\) odd
moduli and taking a square root gives RMS size

\[
\|\boldsymbol\alpha\|_2N^{11/24+\varepsilon}
\]

when \(Q\asymp N\).  This is a positive modulus average and cannot select the
one fixed supported signed packet.  The report's Shen restoration and
interface rejection are therefore correct.

For Dong--Robles--Zeindler, theorem status fails before normalization.  The
withdrawal notice itself supplies the complete control: the corrected
\(L^7\) bookkeeping removes the advertised improvement, and v2 provides no
paper theorem to restore to project scale.  It is correct not to infer even a
weaker project estimate from the withdrawn v1 claim.

For Li--Yang, substituting
\(\theta=(3292+25\sqrt{1717})/13762\) into the Definition 1.1 equation with
\(x=-\theta\) gives equality and places \(x\) in the printed uniqueness
interval.  The source definition of \(R(X)\) verifies that no factor-of-two
radius conversion is missing.  Therefore the external benchmark is exactly
the area exponent printed by the report, not \(2\theta\) or \(\theta/2\).

Finally, the report's negative literature conclusion is a reproducible
search statement, not an impossibility theorem: the cutoff, official listing,
named corpus, and excluded future/unindexed sources are all explicit.  That is
the strongest lawful scope of the no-match.

## 4. First doubtful or unproved step

The **exact first failure in document order** is in report Section 2.2's
summary of Shen Theorem 1: it omits the source hypotheses
\(1\le N\le q-1\) and \(0<\delta<1/4\) (and should say “odd prime”).  This
violates the round's exact-hypothesis recording standard even though Theorem 1
is not used for the conductor power restoration.

The next exact-hypothesis failure is the omission of \((k,q)=1\) from the
report's Theorem 3 sentence.  The next literal transcription failure is the
Theorem 4 display, where `\rm` has become an embedded carriage return, rendering
the condition as `q\ {` followed by `m odd}`.  The Dong author initial/title
defect follows in Section 2.3.  None of these defects reverses a source
hypothesis or creates an application; they only prevent a GREEN exact-source
certificate until repaired.

No conclusion-relevant unproved source step was found in the Shen power
restoration, Dong withdrawal handling, Li--Yang variable/exponent scope, or
the dated corpus limitation.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Current version/date/title | **REPAIR**: principal versions and three advertised title corrections are right; correct Anji Dong's initial, add the Dong title, and note the Guo abstract-record/internal-title discrepancy |
| Shen theorem hypotheses | **REPAIR**: add the omitted Theorem 1 range/δ hypotheses and Theorem 3 condition \((k,q)=1\) |
| Shen restored project power | **PASS**: the best favorable specialization yields one square root, \(L\sqrt q\,q^{o(1)}\), not \(L\) |
| Shen fixed-versus-averaged/sign interface | **PASS**: Theorem 4 is a positive modulus-average square and Lemma 1 has inner absolute values |
| Dong withdrawal and power handling | **PASS**: v2 is withdrawn; the notice changes \(L^5\) to \(L^7\); no post-failure theorem restoration is legal |
| Li--Yang exponent and variable | **PASS**: v2 Theorem 1.2 is pointwise in the area variable and has the stated exponent; general statements remain quarantined |
| Dated no-match scope | **PASS**: the report says named corpus/cutoff, not universal nonexistence; the official 27 August listing matches the cutoff |
| Literal source-formula integrity | **REPAIR**: replace the embedded carriage return by `q\ {\rm odd}` in Shen Theorem 4 |

Overall control outcome: **REPAIR**, with the analytic source conclusion
retained.

## 6. Dependencies and exact artifacts used

Local artifacts read completely or as the assigned exact context:

- `protocol.md`;
- `strategy/round178_full_proof_strategy_current_literature_review.md`; and
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reports/current_primary_literature_reassessment.md`.

Official primary records checked:

- Shen [abstract record](https://arxiv.org/abs/2607.06575) and
  [v1 HTML](https://arxiv.org/html/2607.06575v1);
- Dong--Robles--Zeindler [withdrawal record](https://arxiv.org/abs/2601.00292);
- Li--Yang [abstract record](https://arxiv.org/abs/2308.14859) and
  [v2 HTML](https://arxiv.org/html/2308.14859v2);
- Pascadi [v2 record](https://arxiv.org/abs/2511.08445);
- Kwan [v3 record](https://arxiv.org/abs/2310.09419) and
  [v3 HTML](https://arxiv.org/html/2310.09419v3);
- Liyang Yang [v1 record](https://arxiv.org/abs/2512.03305);
- Chen--Lin [v1 record](https://arxiv.org/abs/2608.25812) and
  [v1 HTML](https://arxiv.org/html/2608.25812v1);
- Mirzoabdughafurov [v1 record](https://arxiv.org/abs/2608.25787) and
  [v1 HTML](https://arxiv.org/html/2608.25787v1);
- Guo [v3 record](https://arxiv.org/abs/2608.23500) and
  [v3 HTML](https://arxiv.org/html/2608.23500v3); and
- the official [math.NT new listing for 27 August
  2026](https://arxiv.org/list/math.NT/new).

No state file, source report, strategy file, synthesis, or validation artifact
was edited by this review.

## 7. Recommended state effect

**Retain every analytic status and exponent; repair source evidence only.**

Before the source report is accepted as exact-source evidence:

1. add Shen Theorem 1's complete range and δ hypotheses;
2. add \((k,q)=1\) to the Shen Theorem 3 statement;
3. repair the Theorem 4 odd-modulus LaTeX/control character;
4. replace “Y. Dong” by “Anji Dong” or “A. Dong” and add the title
   *Bilinear forms with Kloosterman fractions and applications*; and
5. optionally record the Guo abstract-record/internal-manuscript title
   discrepancy so that the chosen current title is explicit.

After those bounded repairs, rerun the exact-source transcription control.
Absent a new discrepancy, the report should become GREEN.  This review gives
no authority to promote a proof node, bridge, quarter theorem, or exponent;
its state-side label remains `strategy_source_update_only`.
