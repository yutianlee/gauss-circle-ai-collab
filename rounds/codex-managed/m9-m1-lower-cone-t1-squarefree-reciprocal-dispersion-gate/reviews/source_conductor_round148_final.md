# Final source re-review of the repaired Round 148 conductor candidate

## 1. Result

**Result: GREEN on the source, power-ledger, interface, and scope seams.**
The repaired candidate now states the exact finite progression support,
uses the correct reduced denominator, separates the five distinct power
placements, qualifies the Schlage--Puchta calculation as an
exact-denominator specialization, records both the exact-multiple
improvement and the unclassified larger-denominator approximants, and
narrows the literature conclusion to the theorem interfaces actually
audited.  It also gives the missing Round-147 bandwidth comparison and
retains every owner and downstream exclusion.

This verdict does not independently recertify the detailed uniform
remainder proof in (148.C14a)--(148.C14c), which belongs to the blind
transform/remainder review.  The limited sanity check required here found
no normalization, scale, finite-support, or source-interface conflict in
that repaired statement.

## 2. Exact statement and hypotheses checked

The leading transformed form is now literally finite.  The set

$$
 \mathcal P(d)=\{(\alpha,b):\alpha,b\text{ odd},\
 \mu(\alpha)\mu(b)\ne0,\ b\mid d,\ \alpha^2\le e_+,
 \ \mathscr A(d,[\alpha^2,b]n)\ne0\text{ for some }n\ge1\}
$$

retains the divisibility support inherited from \(\alpha^2\mid e\).
Consequently (148.C4) is a finite sum over the literal cells
\((\alpha,b)\), with
\(\ell=[\alpha^2,b]\), coefficient \(\chi_4(\ell)/\ell\),
phase \(e(Nd\ell/q)\), coupled weight
\(\mathscr A(d,4Nd\ell^2/q^2)\), and
\(q\asymp\ell Q\), where
\(Q=2\sqrt{ND/E}\asymp D\sqrt{N/M}\).  The candidate explicitly says
that the continuous saddle weight alone does not impose this finite
support.

If \(g=(\ell,q)\), \(L=\ell/g\), and \(q_0=q/g\), then the candidate
uses

$$
 e(Nd\ell/q)=e(NLd/q_0),\qquad (L,q_0)=1,
$$

and correctly relates the source denominator to this coordinate by

$$
 q_*={q\over(q,\ell N)}={q_0\over(q_0,N)}.
\tag{F148.1}
$$

Its nearest-integer coordinate is therefore formed with \(q_0\), not
with the unreduced original \(q\).  The bare formula \(j=N-Aq\) is
confined to the unexpanded \(\ell=1\) cell.

The source statements used in the conclusion are also separated
correctly: the three pointwise progression results have prime,
squarefree, or squarefree-smooth moduli and the stated subunit powers;
Nunes's variance Theorems 1.1--1.2 instead concern a fixed-modulus
average of residue-class errors with a genuine diagonal main term; and
Schlage--Puchta Theorem 3 is a pointwise additive result without a special
modulus family.  The candidate does not restate or use Nunes Theorems
1.2--1.3 or the least-squarefree Lemma 1.3.  Its cited exact source report
now records, respectively, \(a,b\in\mathbb F_p^\times\) and the
unit-residue/arbitrary-positive-modulus hypotheses, so no false
specialization is imported.  Likewise, the separable large-sieve
calculation remains explicitly a \(q\)-independent-coefficient diagnostic
in that report and is not applied to the candidate's
\(q\)-coupled weight.

## 3. Verification and derivation

**Finite support and normalization.**  Since the physical amplitude has
\(e\le e_+\ll E\), every retained term with \(\alpha^2\mid e\) has
\(\alpha^2\le e_+\).  The additional nonempty-lattice-support condition
in \(\mathcal P(d)\) is exact, rather than an analytic truncation.  With
this repair, all later uses of \(\alpha\le\sqrt E\) are legitimate.  The
Poisson factor, positive saddle, phase, and leading coefficient remain
\(e(1/8)N^{-1/4}(d\ell)^{-1}e(Nd\ell/q)\), so the transformed target is
\(RD X^\varepsilon\).

**Reduced denominator and small stratum.**  From
\(q=gq_0\), \(\ell=gL\), and \((L,q_0)=1\),

$$
 (q,\ell N)=g(q_0,LN)=g(q_0,N),
$$

which proves (F148.1).  Writing \(q=hr\), with
\(h\mid\ell N\) and \(r=q_*\le Y\), gives at most
\(Y\tau(\ell N)\) cells for fixed \(\ell\).  The exact \(1/\ell\)
and squarefree divisor sums are \(X^\varepsilon\)-bounded, hence the
aggregate is \(DYX^\varepsilon\).  Thus every \(Y\le R\), including all
three quoted progression ranges and \(Y=D\), is target-safe.

**Five-row power ledger.**  Each displayed ratio follows from
\(Q/(RD)=R/\sqrt M\), \(E=M/D\), and \(Q\sqrt{DE}=\sqrt N D\):

| Placement | Capacity divided by \(RD\) |
|---|---:|
| bare \(Q+D\) | \(R/\sqrt M+1/R\) |
| expand \(\mu^2(d)\), then apply the bare bound termwise | \(R\sqrt D/\sqrt M+1/R=R/\sqrt E+1/R\) |
| full absolute progression-cell mass | \(R\sqrt D\) |
| unrecombined cell Cauchy plus a separately positive \(d\)-diagonal | \(R\) |
| Round-147 \(H\)-menu | \(M^{1/4}\) below \(R^{4/3}\), \(R^{1/2}M^{-1/8}\) above |

The candidate labels all five as upper capacities, not lower bounds, and
does not conflate the \(R/\sqrt E\), \(R\sqrt D\), and \(R\) losses.

**Schlage--Puchta scope.**  Choosing the exact reduced denominator gives
the valid specialization

$$
 \sum_{d\asymp D}\mu^2(d)e(\ell Nd/q)
 \ll_\varepsilon D^{1+\varepsilon}/q_*+q_*D^\varepsilon.
$$

The candidate correctly calls the resulting
\(D/\ell+\ell Q^2\) aggregation an exact-denominator calculation only.
It then records that, for \(q_*\le\sqrt D\), an exact multiple in
\([\sqrt D,2\sqrt D]\) yields \(O(D^{1/2+\varepsilon})\), while other
admissible approximants for \(q_*>\sqrt D\) have not been jointly
classified.  Its terminal conclusion is therefore only that the audited
literature supplies no theorem aggregating the needed choices over the
varying outer \(q\); it makes no exhaustive Schlage--Puchta no-go claim.

**Diagonal and \(H\)-interface.**  The factor-\(R\) obstruction is
confined to a common interior \(d\)-plateau, unrecombined progression
cells, positive Cauchy weights, and separate nonnegative majorization of
the \(d_1=d_2\) part.  The candidate expressly leaves pre-Cauchy
regrouping, signed cross-cell cancellation, common-divisor effects, and
the \(N\)-dependent alignment fibres outside the result.  It does not
claim a lower bound for the signed transform.

After reduction, \(q_0\asymp LQ\), so the reciprocal nearest-integer
coordinate naturally ranges over \(|j|\ll LQ\).  A formal Round-147
choice \(k=L\) retains only
\(|j_H|\lesssim L\sqrt{N/M}=LQ/D\).  The candidate states this missing
complementary range and independently notes that \(L\) (or \(\ell\))
need not be the powerful Euler-convolution index.  It claims equivalence
only for the complete reconstructed physical identities after inverse
transforms and Euler recombination, never termwise for (148.C4).

**Remainder sanity check.**  In (148.C14c), multiplying the leading
absolute capacity \(R\sqrt D\) by the three first-order ratios gives
exactly
\(1/(R\sqrt E)\), \(\sqrt D/R\), and \(1/R\), as stated.  The exact
finite set \(\mathcal P(d)\), four frequency regions, endpoint owner,
and lower-symbol bookkeeping are present.  This is internally compatible
with the leading transform and source audit; the uniform analytic proof
remains for the blind reviewer.

## 4. First doubtful or unproved step

The first unproved arithmetic step remains a coefficient-sensitive joint
signed estimate for (148.C4) that retains the actual
\((\alpha,b,q)\)-coupled profile and neutralizes the cross-progression
diagonal before it is separately made positive.  The alternative is an
exact Euler recombination followed by a signed theorem for the Round-147
powerful \(H\)-correlation.  Neither the candidate, the three Round-148
reports, nor any audited primary theorem proves either route.

In particular, this review does not promote (148.C6), the absolute
squarefree \(Q+D\) analogue, a strict \((M,D,E)\)-range, or a signed lower
bound.  No earlier source seam has been hidden by the repairs.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| literal finite \(\alpha\)-support | **GREEN:** (148.C2a) is exact and is used in (148.C4) and the remainder sum. |
| UTF-8 and C0-byte scan | **GREEN:** strict UTF-8; zero bare CR, tabs, replacement characters, or other C0 bytes; seven numbered sections. |
| \(q_*\) and small-stratum count | **GREEN:** (F148.1) and the \(DYX^\varepsilon\) aggregation are correct. |
| source theorem classes | **GREEN:** pointwise progression, variance, additive, fixed-modulus trace, and Kloosterman-fraction results are not conflated. |
| Schlage--Puchta qualification | **GREEN:** exact denominator, exact multiples, unclassified other approximants, and lack of a varying-\(q\) aggregation theorem are all stated. |
| five-row power ledger | **GREEN:** all ratios and capacity/lower-bound labels are correct. |
| positive-diagonal scope | **GREEN:** the no-go is expressly method-local and excludes signed joint energies. |
| Round-147 interface | **GREEN:** reconstruction-only equivalence, non-powerful-index mismatch, and the factor-\(D\) bandwidth gap are explicit. |
| remainder/source compatibility | **GREEN on this limited check:** no scale or normalization conflict; independent analytic certification is not duplicated. |
| owner/downstream exclusions | **GREEN:** Round 138 cross, every \(t\ge2\) layer, lower GAR, M9--M1, M9--M2, endpoint uniformity, M9, bridge, quarter target, and global exponent remain outside the result. |

No source-side repair remains mandatory.  Reprinting the full Nunes
\(K_1,K_2\) and Lemma 1.3 cards in the conductor candidate would be
redundant because the candidate neither invokes them directly nor changes
their hypotheses, and it identifies the repaired source report as exact
evidence.

## 6. Dependencies and exact artifacts used

This final re-review used:

- `candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`;
- `reviews/source_conductor_round148_candidate_audit.md`;
- `reviews/source_applicability_seam_review.md`; and
- the repaired primary-source cards in
  `reports/squarefree_progression_source_audit.md`, only to verify that
  the candidate's compressed source summary imports the corrected literal
  hypotheses.

The primary cards are those for Schlage--Puchta Theorem 3; Nunes's large-
progression Theorems 1.1--1.3, least-squarefree Theorem 1.1 and Lemma 1.3,
and variance Theorems 1.1--1.2; Mangerel Theorems 1.1 and 3.1 with Remark
3.2; and Bettin--Chandee Theorems 1--2.  No new web inference or numerical
experiment was used, and no candidate or shared-state file was edited.

## 7. Recommended state effect and verdict

On the source/interface side, no further candidate repair is required.
Subject to the independent transform/remainder adjudication, the candidate
may promote only the two nodes it names: (i) the exact finite
\(t=1\) reciprocal-transform reduction, including owned collars, symbols,
and remainder, and (ii) the factor-\(R\) obstruction limited to early
progression-cell Cauchy with a separately positive diagonal, together with
the audited theorem-interface mismatch.

Retain (148.C6), all strict ranges, all alternative signed regroupings,
every listed downstream owner, the quarter target, and the global exponent
as open.  This review authorizes no broader source no-go and no state edit.

**GREEN**
