# Round 171 strategy: critical balanced two-defect commutator gate

## Frozen objective

On graph
`4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`,
consider only a persistent critical \(j=1\) literal balanced block
\(B\) with \(L\asymp X^{1/6}\). Set

\[
 a_B^<(h,k)=\chi_4(h)
 \eta\!\left({(h,k)\over\sqrt L/2}\right)A_B(h,k),
\]

and, for a primed copy,

\[
 \Delta=h'k'-hk,\qquad \rho=hk'-h'k,
 \qquad \mathrm{df}=\{|\Delta|>L,\ |\rho|>L\}.
\]

The sole target is

\[
 \boxed{|\mathcal R_B^{\rm osc}|\ll_\varepsilon L^3X^\varepsilon.}
 \tag{171.BAL-j1}
\]

Here

\[
 \mathcal R_B^{\rm osc}
 =\sum_{\mathrm{df}}a_B^<(h,k)\overline{a_B^<(h',k')}
 \left[e\!\left(\sqrt X(\sqrt{hk}-\sqrt{h'k'})\right)-1\right].
\]

This is the complete actual fixed-block sum, with both character factors,
low-gcd weights, slanted symbols, floors, stars, support crossings, aliases,
signs, and endpoints retained. Positive capacity is
\(L^4X^\varepsilon\); exactly one factor \(L\) is missing.

## Identity under test

Write \(h'=h+p\), \(k'=k+q\). Then

\[
 \Delta+\rho=q(2h+p),\qquad
 \Delta-\rho=p(2k+q).
 \tag{171.C1}
\]

These are coordinate factorizations, not a commutator theorem. Round 171
must first derive a multiplicity-preserving coordinate domain and an exact
two-direction discrete-difference identity for the complete zero-subtracted
scalar. Only then may it estimate the resulting pieces.

On the nonzero character support, \(p=2s\) and

\[
 \chi_4(h)\chi_4(h+p)=(-1)^s.
 \tag{171.C2}
\]

The character is therefore constant on a fixed-\(p\) fibre. It gives no
inner \(h\)-cancellation there; any saving must arise from a larger exact
recombination. The axial sectors \(p=0\) and \(q=0\) may satisfy both far
gates and must be retained and paid. The proved phase-free subtraction does
not remove the fixed-\(Q\) rational rulings.

## Promotion gate

A proof must provide:

1. an exact finite coordinate map and inverse, including multiplicities;
2. two explicit discrete difference operators and a coefficientwise identity;
3. all sharp-gate, support, boundary, and axial correction terms;
4. a target-safe complement and complete \(L^3X^\varepsilon\) ledger;
5. the factor \(L\) saving before any positive norm or triangle inequality;
6. both gcd weights, both slanted symbols, characters, lifts, floors, stars,
   aliases, crossings, endpoints, and real centre;
7. controls identifying which literal structure supplies cancellation; and
8. independent blind, hostile-capacity, identity, power, and owner reviews.

A rigorous first failed identity or unavoidable positive-capacity theorem is
also useful, but must remain scoped to this commutator placement.

## False controls and quarantines

- A claimed proof must not also prove the bound for arbitrary phase-adapted
  coefficients, the constant-character shadow, or after erasing both
  gcd/slanted structures.
- Do not infer cancellation inside a fixed-\(p\) fibre from \(\chi_4\).
- Do not divide by \(p\) or \(q\) without an axial-sector theorem.
- Do not treat phase-free subtraction as deletion of fixed-\(Q\) rulings.
- Fixed-defect counting, determinant broad--narrow, positive row energy,
  aliaswise triangle, and a second B-process are not new savings.
- Do not replace the complete fixed-block modulus by blockwise absolute values
  or change the far gates.
- Do not transfer the critical child to another BAL label or full BAL.

## Stop rule and downstream scope

Stop at the first failed coordinate inverse, exact identity, multiplicity,
fixed-\(p\), axial, gate, boundary, complement, restoration, capacity,
false-control, or owner-scope gate. Do not pivot inside Round 171.

Even a proof closes only the persistent critical remainder and equivalent
energy, subject to the existing fixed-block connector. The remaining-label
BAL obligation, full BAL, hard TOP, UNBAL, M9--M2, both direct M1 parents or
GAR, endpoint assembly, M9, both bridges, and the quarter theorem remain open.

## Allocation and terminal labels

The round is 100% analytical/algebraic and 0% numerical. It closes under:

- `balanced_critical_j1_oscillatory_target`;
- `strict_balanced_two_defect_commutator_sector`; or
- `balanced_two_defect_commutator_no_go`.
