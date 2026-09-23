# Source Card: Milicevic--Robinson--Shupe 2026

## Bibliographic data

Djordje Mili\'cevi\'c, Catherine Robinson, and Chloe Shupe,
*Sums of products of Kloosterman sums to prime power moduli*,
arXiv:2608.21346v1, submitted 2026-08-21.

## URL

- https://arxiv.org/abs/2608.21346v1
- https://arxiv.org/html/2608.21346v1

## Exact theorem audited

For an odd prime (p), (q=p^n), and a fixed (k)-tuple of shifts
\(\boldsymbol a\), Theorem 1.1 studies the complete product

\[
 S(\boldsymbol a;q)=
 \sum_{\substack{x\bmod q\\(x+a_i,q)=1\ \forall i}}
 \prod_{i=1}^k\operatorname{Kl}_2(x+a_i;q)
\]

and proves

\[
 S(\boldsymbol a;p^n)
 \ll_k
 p^{n-(n-\Delta^*(\boldsymbol a)-1)/\lceil k/2\rceil+1},
\]

where \(\Delta^*(\boldsymbol a)\) is the alignment depth from Definition
2.  In the generic case \(\Delta^*=0\), with
\(r=\lceil k/2\rceil\), this is

\[
 |S(\boldsymbol a;q)|\ll_k q^{1-1/r}p^{1+1/r}.
\]

The theorem is pointwise in a fixed shift tuple, complete in one residue
variable, and restricted to one odd prime-power modulus.  Deeply aligned
tuples may have full-size behavior.  Remark 4 treats the (k=2)
Ramanujan-sum case.  Proposition 5.3 permits only bounded
\(p^{\kappa_0(F)}\mathbb Z/p^n\mathbb Z\)-invariant weights on
\(A_F\); it does not license generic invariant or scale-invariant
weights.

## Project interface audit

No theorem is imported as a proof dependency.  The first failure occurs
before a lawful parameter or power map:

- K17a is a centered projector/orientation defect over arbitrary odd
  reduced conductors with lifted selectors, aliases, phases, and endpoints.
- K26 is an Archimedean unequal-product Gram row with literal cell phases
  and hard endpoints, not a complete finite-ring sum.
- The Round-185 high-height relation is a primitive affine integer-row
  aggregate over varying (h), two orientations, literal zero extensions,
  and one outer real part; it has no fixed prime-power Kloosterman-product
  modulus.
- UNBAL requires a signed varying-modulus literal-matrix vector estimate
  before norms, not a scalar complete sum at one modulus.

The generic power keeps the residual factor
\(p^{1+1/r}\); it must not be advertised as a pure full-modulus saving.

## Audit status

Primary v1, Theorem 1.1, Definition 2, Remark 4, Example 1, and
Proposition 5.3 were independently checked in Round 186.  The source is a
current non-importable guardrail, not an analytic lemma of this project.

## Rounds referencing this source

- rounds/codex-managed/full-proof-round183-185-strategy-literature-review/reports/current_primary_literature_reassessment.md
- rounds/codex-managed/full-proof-round183-185-strategy-literature-review/reviews/source_hypotheses_currency_interface_review.md
