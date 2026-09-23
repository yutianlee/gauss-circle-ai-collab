# Round 182 source-hypotheses, currency, and interface review

- Campaign: `full-proof-round179-181-strategy-literature-review`
- Round: `182`
- Role: independent primary-source hypotheses, currency, and interface reviewer
- Starting graph: `fec130bc66641cbdad18c832de10077a7825f1caaf5d10170a67ef65c0b27196`
- Audit cutoff: **2026-08-27 (Asia/Shanghai)**
- Status: review evidence only; no source-card or shared-state edit is authorized

## 1. Result

**Verdict: REPAIR.**

The Round-182 report's substantive source conclusion survives independent
checking.  No audited primary theorem has both the literal coefficient/
absolute-value interface and the restored power needed for a live quarter
owner.  In particular:

1. the Shao--Shparlinski--Wijaya squarefree-Kloosterman estimate has the
   reported scale (L^{3/2-1/116+o(1)}) in a deliberately nonliteral
   comparison, but its prime finite-field trace is not the Round-181
   Archimedean hard-M1 coefficient;
2. Xiao's moment estimates do not give a target-sized fixed-(t) literal
   estimate, and the fourth-moment frequency window misses the critical
   hard-M1 shell;
3. the Tao--Trudgian--Yang derived pair gives exactly
   ((\sqrt X)^{195}t^{644}\le L^{449}) as the coefficient-one sufficient
   range, before the unproved bounded-variation transfer for the actual
   coefficient;
4. Blomer--Pascadi gives only a (c^{-1/32}) critical saving for a
   fixed-modulus separable Kloosterman form, which optimistically leaves
   (Lc^{31/32+o(1)}) from project capacity (Lc), not (L); and
5. Li--Yang Theorem 1.2 remains a separately repaired, narrow global
   benchmark with exponent (0.3144831759740614\ldots>1/4), not an
   internal owner.  Bourgain--Watt remains withdrawn.

The report is not GREEN because three exact-source seams need bounded repair.
First, the notation (p=N=L^2) is incompatible with the source hypothesis
that (p) is prime when (L>1) is integral; the intended scale comparison is
(N=p) and (p\asymp L^2).  Second, the Tao--Trudgian--Yang record is
misdescribed as an official arXiv v1 plus a later “current author source dated
2026-08-24.”  The official record has only v1, submitted 2025-01-28; its v1
TeX archive contains `\date\today`, so the date displayed by a later HTML
render is not evidence of a new author snapshot or a new arXiv version.
Third, the Xiao discussion should replace “supplies no pointwise literal
bound” by the exact statement that positivity gives only a non-saving
single-frequency bound, while the fourth moment is outside its source range
on the critical shell.  These defects do not create an import and do not
alter the no-match or exponent conclusion.

## 2. Exact statement and hypotheses

### 2.1 Shao--Shparlinski--Wijaya

The official primary record is Xuancheng Shao, Igor E. Shparlinski, and
Laurence P. Wijaya, *Sums of Kloosterman sums over square-free and smooth
integers*, [arXiv:2411.12113v1](https://arxiv.org/abs/2411.12113), submitted
2024-11-18.  For a prime (p) and integer (s\ge2), the source uses the
normalized finite-field trace

\[
 {\cal K}_{s,p}(n)=p^{-(s-1)/2}
 \sum_{x_1\cdots x_s\equiv n\pmod p}e_p(x_1+\cdots+x_s)
\]

and (Q_{s,p}(N)=\sum_{n\le N}|\mu(n)|{\cal K}_{s,p}(n)).  Theorem 1.1
assumes an even positive integer (\ell) and
(p^{1/2+2/\ell}\le N\le p), and states

\[
 |Q_{s,p}(N)|\le N^{1/2}p^{1/4}
 \left(\frac{p^{1/2+2/\ell}}{N}\right)^{1/[2(4\ell-3)]}p^{o(1)}.
\]

At (N=p), (\ell=8), this is the printed
(p^{3/4-1/232+o(1)}).  The lawful fictional scale comparison is therefore

\[
 N=p,\qquad p\asymp L^2,\qquad
 p^{3/4-1/232}=L^{3/2-1/116+o(1)}.
\]

The equality (p=L^2) should not be used.  Even after this repair, the first
project failure is the kernel/modulus: the source has one prime finite-field
hyper-Kloosterman trace, whereas the project has

\[
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})
\]

with a joint divisor-incidence coefficient, Archimedean phase, physical
endpoints, and no prime modulus.  Theorem 1.3 likewise concerns friable
integers (P(n)\le y), not the project's physically smooth M1 parent.  The
report's nonimport conclusion is correct.

### 2.2 Xiao

The official primary record is Yixiu Xiao, *Moment Estimates and Discrepancy
for Sums of Square Roots Modulo One*,
[arXiv:2606.28986v1](https://arxiv.org/abs/2606.28986), submitted 2026-06-27.
For

\[
 S(h,n)=\sum_{n/2\le a\le n}e(h\sqrt a),
\]

Theorem 1.1 assumes an **integer** frequency family (H/2\le h\le H) and
(H\ge n^{1/2+\delta}), and gives

\[
 \sum_{H/2\le h\le H}|S(h,n)|^2
 \ll_{\varepsilon,\delta}Hn^{1+\varepsilon}.
\]

Theorem 1.2 additionally requires (0<\delta<1/6) and

\[
 n^{1/2+\delta}\le H\le n^{2/3},
 \qquad
 \sum_{H/2\le h\le H}|S(h,n)|^4
 \ll_{\varepsilon,\delta}Hn^{2+\varepsilon}.
\]

For a fixed project multiplier (t), the formal map is

\[
 n_{\rm Xiao}\asymp \frac{L^2}{t^2},\qquad
 h=t\sqrt X,\qquad H\asymp t\sqrt X.
\]

For general real (X), (h) is not an integer, so there is no literal
source map.  Even on the diagnostic square subfamily (X=J^2), the critical
hard-M1 shell has (L\asymp X^{1/6}).  At (t=1), Theorem 1.2 would require

\[
 \sqrt X\le (L^2)^{2/3}=L^{4/3}\asymp X^{2/9},
\]

which is false.  Theorem 1.1 is in range, but positivity gives only

\[
 |S(tJ,n_{\rm Xiao})|
 \le (Hn_{\rm Xiao}^{1+\varepsilon})^{1/2}
 \ll X^{1/4}L\,t^{-1/2}X^\varepsilon.
\]

At (t=1), (L\asymp X^{1/6}), this is (X^{5/12+\varepsilon}), worse
even than the raw (L^2=X^{1/3}) capacity and far above the
(L^{3/2}=X^{1/4}) target.  Thus a positive moment can formally isolate one
frequency, but not at a useful power.  In all cases the source coefficient is
one, not the joint (C_{L,X}^{\sigma}(st^2)\mu^2(s)) with hard zero
extension.  The report should record these exact range and power failures.

### 2.3 Tao--Trudgian--Yang

The official [arXiv record](https://arxiv.org/abs/2501.16779) contains only
v1, submitted 2025-01-28.  The official v1 source archive is
[arXiv:2501.16779v1 source](https://arxiv.org/src/2501.16779v1).  Its TeX
contains `\date\today`; consequently the date “August 24, 2026” visible in
the experimental v1 HTML is a render-time date, not a revision timestamp.
No separate author-hosted snapshot URL or hash is supplied by the report.
The version ledger must therefore cite the official v1 date and must not
describe the render date as a later author version.

The needed mathematical content is already present in official v1.  Table 1
and Lemmas 13--15 give

\[
 D\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{18}{199},\frac{593}{796}\right),
\]

and the (B)-process gives

\[
 B D\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{195}{796},\frac{235}{398}\right).
\]

This pair is not one of the four pairs stated in Theorem 20; its exact
provenance is Table 1 plus Lemmas 13--15.  For the coefficient-one fixed-(t)
fiction, put

\[
 N_t\asymp \frac{L^2}{t^2},\qquad T\asymp\sqrt X\,L.
\]

Then the exponent-pair bound is

\[
 (T/N_t)^{195/796}N_t^{235/398}
 =X^{195/1592}L^{745/796}t^{-550/796+o(1)}.
\]

Comparing with the sufficient fixed-(t) budget
((L^2/t^2)^{3/4}=L^{3/2}t^{-3/2}) is exactly equivalent to

\[
 X^{195}t^{1288}\le L^{898},
 \qquad\text{or}\qquad
 (\sqrt X)^{195}t^{644}\le L^{449}.
\]

At (t=1) this needs (L\ge X^{195/898}), so it misses the critical
(L\asymp X^{1/6}) shell.  The source theorem is an unweighted interval
estimate.  Partial summation transfers it only to a uniformly normalized
bounded-variation weight; no such representation has been proved for the
literal squarefree divisor coefficient and moving endpoints.  The report's
power calculation and nonimport conclusion are correct after the metadata
and provenance repair.

### 2.4 Blomer--Pascadi

The official primary record is Valentin Blomer and Alexandru Pascadi,
*Bilinear forms with Kloosterman sums via quadratic characters*,
[arXiv:2607.24311v1](https://arxiv.org/abs/2607.24311), submitted
2026-07-27.  Theorem 1.1 assumes (c\ge1), (1\le N\le c), intervals
(\mathcal I,\mathcal J) of length at most (N), separable complex
sequences (\alpha_m,\beta_n), and a unit (a\bmod c).  It sums the
unnormalized (S(am,n;c)), with ((m,n,c)=1) except for the stated full
initial-interval case, and gives

\[
 \|\alpha\|_2\|\beta\|_2c^{1+o(1)}
 \left(N^{1/8}c^{-3/32}+N^{5/16}c^{-3/16}
       +N^{2/3}c^{-7/18}\right).
\]

At (N=\sqrt c), the first two terms give the printed
(c^{-1/32}) critical saving.  Even granting an optimistic transfer of
only this saving to the project's exact-(q) capacity (Lq\log(2q)) leaves

\[
 Lq^{31/32+o(1)},
\]

not (LX^\varepsilon).  The literal application fails earlier: the R179
centered orientation defect is a joint lifted symbol with two orientations,
selector, moving phase, physical endpoints, and outer alias recombination,
not a separable fixed-modulus bilinear form.  The report's scope and restored
power are source-faithful.

### 2.5 Li--Yang, Huxley, and withdrawals

The official Li--Yang record is
[arXiv:2308.14859v2](https://arxiv.org/abs/2308.14859), revised 2023-09-14.
Equation (1.1) defines the area-variable discrepancy

\[
 R(X)=\sum_{m^2+n^2\le X}1-\pi X,
\]

and Theorem 1.2 states a pointwise bound with
(\theta^*=0.314483\ldots).  Substituting (x=-\theta) in Definition 1.1
and eliminating the square root gives

\[
 27524\theta^2-13168\theta+1419=0.
\]

The root in the source interval is

\[
 \theta_{\rm LY}
 =\frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\]

Thus no radius-to-area conversion is missing.  The project may use only its
separately repaired final Theorem 1.2 application; the general Proposition
3.1 and Theorem 4.2 remain quarantined and do not prove an R179--R181 owner.

The official
[Bourgain--Watt record](https://arxiv.org/abs/1709.04340) is v2,
withdrawn 2023-07-16, and states that Theorems 1--3 lose theorem status.
Huxley's official journal abstract gives (131/208) in the radius-of-
curvature variable, hence (131/416) in the project's area variable.  Both
controls agree with the report.  No exponent changes.

### 2.6 Currency and dated corpus scope

The official [math.NT new listing](https://arxiv.org/list/math.NT/new) is
headed Thursday, 27 August 2026 and contains 35 entries.  The report correctly
limits its negative conclusion to its named, versioned corpus and that dated
listing.  The checked new-entry descriptions of Chen--Lin and
Mirzoabdughafurov, and the checked withdrawal records, do not match a literal
project owner.  This is a reproducible corpus statement, not a universal
nonexistence theorem.

## 3. Proof or derivation

The independent audit used the following order for each plausible import:
official version and theorem status; theorem number and exact parameter
range; pointwise versus family/moment quantifier; coefficient and modulus
class; position of absolute values; literal project variable map; restoration
of normalizations and outer accumulation; and downstream owner scope.

The decisive power calculations are exact:

1. **Shao--Shparlinski--Wijaya.**  At (N=p), (\ell=8), the factor in
   Theorem 1.1 is
   ((p^{3/4}/p)^{1/58}=p^{-1/232}), so the total exponent is
   (p^{3/4-1/232}).  With (p\asymp L^2), this is
   (L^{3/2-1/116+o(1)}).  The power is sufficient only in the declared
   kernel-free fiction.
2. **Xiao.**  On the critical (t=1) map,
   ((n,H)\asymp(X^{1/3},X^{1/2})).  The fourth-moment upper range is
   (H\le n^{2/3}=X^{2/9}), which fails.  The second moment gives at best
   (H^{1/2}n^{1/2}=X^{5/12}), and the raw (n=X^{1/3}) count is smaller;
   neither reaches (X^{1/4}).
3. **Tao--Trudgian--Yang.**  Since
   (235/398-195/796=275/796), one obtains
   (T^{195/796}N_t^{275/796}), hence the displayed
   (X,L,t) exponents.  Moving the fixed-(t) budget to the right and
   clearing denominator (1592) gives
   (X^{195}t^{1288}\le L^{898}), exactly the square of the report's
   condition.
4. **Blomer--Pascadi.**  At (N=c^{1/2}), the first two theorem terms are
   both (c^{-1/32}), while the third is (c^{-1/18}).  The dominant saving
   is therefore (c^{-1/32}); applying it to (Lq) leaves
   (Lq^{31/32}), not (L).
5. **Li--Yang.**  Exact elimination from Definition 1.1 gives the quadratic
   above and selects the reported radical root in the printed interval.
   This checks the number but does not certify the quarantined general
   arguments.

All five controls fail to create a source import before any live parent.
The R179 centered self-return, R180 unequal-product deletion, and R181
small-(t) squarefree-radical residual are therefore mapped to the correct
post-round objects rather than to already-paid sectors.

## 4. First doubtful or unproved step

The earliest precision defect in report order is the exact equality
(p=N=L^2).  Because the report labels it fictional, it does not assert a
legal application, but exact hypothesis bookkeeping should replace it by
(N=p\asymp L^2); otherwise the prime hypothesis is visibly impossible.

The first material source-record defect is the Tao--Trudgian--Yang date.
The official v1 archive itself contains `\date\today`.  A later HTML render
therefore cannot be cited as an independently versioned author snapshot.
If a genuinely later author manuscript was inspected, the report must give
its exact author-hosted URL, retrieval date, and immutable commit/hash and
must distinguish every theorem used from official arXiv v1.  Without that
evidence, all technical citations should be assigned to official v1, where
the needed Table-1 and Lemma-13--15 material already appears.

The next imprecision is Xiao: a positive moment does imply a weak bound for
an individual term, so “no pointwise literal bound” is too absolute.  The
correct conclusion is that the bound is non-saving after restoration, the
fourth-moment range is unavailable on the critical shell, and the actual
coefficient/real-frequency map fails.  No conclusion-relevant error was
found in the TTY algebra, Blomer--Pascadi restoration, Li--Yang exponent
quarantine, withdrawal handling, or dated corpus limitation.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| `primary_source_currency` | **PASS with one metadata repair**: official records and the 2026-08-27 listing support the stated versions/statuses, but TTY has only official v1; the HTML's 2026 date comes from `\date\today` |
| `theorem_hypothesis_and_version_audit` | **REPAIR**: distinguish official TTY v1 from any genuinely later author snapshot and cite Table 1 plus Lemmas 13--15 for the derived pair |
| Shao fictional specialization | **REPAIR notation; PASS power**: use (N=p\asymp L^2), not (p=N=L^2); (L^{3/2-1/116+o(1)}) is exact |
| Xiao frequency/range interface | **REPAIR exposition; PASS nonimport**: record the failed fourth-moment upper range and the non-saving second-moment restoration; change the categorical pointwise sentence |
| TTY restored project power | **PASS**: the coefficient-one condition is exactly ((\sqrt X)^{195}t^{644}\le L^{449}), and the literal BV seam remains open |
| Blomer--Pascadi scope and power | **PASS**: arbitrary modulus but separable fixed-modulus data; critical (c^{-1/32}) saving leaves (Lq^{31/32+o(1)}) in the optimistic project ledger |
| Li--Yang exponent quarantine | **PASS**: v2, area variable, pointwise Theorem 1.2 number correct; general Proposition 3.1/Theorem 4.2 remain quarantined |
| Withdrawal status | **PASS**: Bourgain--Watt and Dong--Robles--Zeindler cannot be theorem dependencies |
| `literal_coefficient_and_absolute_value_interface` | **PASS**: joint versus separable weights, positive moments, outer signs, endpoints, and fixed versus varying moduli are not conflated into an owner |
| `dated_no_match_scope` | **PASS**: the conclusion is expressly corpus- and cutoff-scoped |
| `strategy_only_no_analytic_promotion` / `exponent_quarantine` | **PASS**: no lemma, parent, bridge, theorem, or exponent is promoted |

Overall control outcome: **REPAIR**, with the analytic no-import conclusion
retained.

No numerical theorem experiment was used.  Machine assistance was limited to
retrieving primary records and exact symbolic/rational consistency checks.

## 6. Dependencies and exact artifacts used

Local artifacts read as the assigned context:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round182_full_proof_strategy_current_literature_review.md`;
- `rounds/codex-managed/full-proof-round179-181-strategy-literature-review/briefs/source_hypotheses_currency_interface_review.md`;
- `rounds/codex-managed/full-proof-round179-181-strategy-literature-review/reports/current_primary_literature_reassessment.md`;
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reports/current_primary_literature_reassessment.md`;
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reviews/source_hypotheses_currency_interface_review.md`;
- the Round-179, Round-180, and Round-181 synthesis files named by the brief;
- `proofs/kernels/m9_m1_hard_top_squarefree_radical_reduction_and_self_return.md`; and
- the cited local source cards for Li--Yang, Bourgain--Watt, Huxley,
  Banerjee--Khurana, Kiral--Zhou, both Popov interfaces, Xiao, and
  Tao--Trudgian--Yang.

Primary records independently checked:

- Shao--Shparlinski--Wijaya
  [abstract/version record](https://arxiv.org/abs/2411.12113) and
  [v1 theorem text](https://arxiv.org/html/2411.12113v1);
- Xiao [abstract/version record](https://arxiv.org/abs/2606.28986) and
  [v1 theorem text](https://arxiv.org/html/2606.28986v1);
- Tao--Trudgian--Yang
  [official v1 record](https://arxiv.org/abs/2501.16779),
  [official v1 source archive](https://arxiv.org/src/2501.16779v1), and
  [experimental v1 HTML](https://arxiv.org/html/2501.16779v1);
- Blomer--Pascadi
  [official v1 record](https://arxiv.org/abs/2607.24311) and
  [v1 theorem text](https://arxiv.org/html/2607.24311v1);
- Li--Yang [official v2 record](https://arxiv.org/abs/2308.14859) and
  [v2 theorem text](https://arxiv.org/html/2308.14859v2);
- Bourgain--Watt
  [official withdrawal record](https://arxiv.org/abs/1709.04340);
- Huxley
  [official journal page](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024611503014485); and
- the official [math.NT new listing](https://arxiv.org/list/math.NT/new) for
  2026-08-27.

No graph, shared state, source card, sibling report, synthesis, or validation
artifact was edited.

## 7. Recommended state effect

**Retain `strategy_source_update_only`; make no analytic graph or exponent
change.**

Before the Round-182 source report is accepted as exact-source evidence:

1. replace every exact fictional (p=N=L^2) identification by
   (N=p\asymp L^2), while retaining the correct
   (L^{3/2-1/116+o(1)}) diagnostic;
2. replace “official v1; current author source dated 2026-08-24” by the
   exact official-v1 provenance, explain `\date\today`, and provide a URL
   and immutable identifier if a genuinely later author manuscript is to be
   cited;
3. attribute the derived TTY pair specifically to Table 1 and Lemmas 13--15;
4. add the exact Xiao map and restored powers, including the failed
   fourth-moment upper range and the non-saving termwise consequence of the
   second moment; and
5. change “supplies no pointwise literal bound” to “supplies no
   target-sized coefficient-literal pointwise bound.”

After those bounded repairs, rerun this source seam.  Every R179--R181
residual, parent, endpoint, bridge, (M9), and global exponent must retain
its present status.

**Final verdict: REPAIR.  Recommended state effect:
`strategy_source_update_only`; no analytic theorem, parent, bridge, or
exponent promotion.**
