# Round 181 product, squarefree, and connector review

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Task: `product_squarefree_and_low_radical_seam`
- Role: conductor seam review
- Generated: `2026-08-27T08:44:04.7412815Z`
- Starting graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Context: `protocol.md`, the active campaign, all three Round-181 reports,
  the formal candidate, the independent reduction review, and the accepted
  Round-119 hard transform and physical assembly
- Review status: **GREEN for the exact reduction and strict sectors; no
  hard-parent promotion**

## 1. Result

For every literal residual hard-M1 shell and each frequency sign, product
regrouping and squarefree-kernel coordinates are exact and preserve
multiplicity. The low-radical sector and the disjoint high-radical sector
with (t\geq\lceil\sqrt L\rceil) are each absolutely
(O_\varepsilon(L^{3/2}X^\varepsilon)). The exact remaining owner is

\[
 s>L,\qquad 1\leq t<\lceil\sqrt L\rceil,
\]

including the complete (t=1) coprime-squarefree literal cone. This is a
strict owner-compatible reduction, not the desired signed estimate.

## 2. Exact statement and hypotheses

Zero-extend the full literal coefficient
(a_{L,X}^{\mathrm{lit},\sigma}(h,n)), retaining the Vaaler taper,
hard denominator profile, normalized powers, floors, stars, strict cone
edges, hard sample, real-(X) crossings, and both signs. Define

\[
 C_{L,X}^{\sigma}(r)=
 \sum_{\substack{h\mid r,\ h\asymp L\\r/h\ {\rm odd}\\4h<r/h<16h}}
 \chi_4(r/h)a_{L,X}^{\mathrm{lit},\sigma}(h,r/h).
\]

Then

\[
 \mathcal T_{L,\sigma}^{M1}
 =\sum_r C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr})
 =\sum_{\substack{s\geq1\\\mu^2(s)=1}}\sum_{t\geq1}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}).
\tag{181.P1}
\]

If (G=(h,n)), uniquely

\[
 h=Gda^2,\quad n=Geb^2,\quad s=de,\quad t=Gab,
 \quad (da,eb)=1,
\tag{181.P2}
\]

where (d,e) are squarefree and (Geb) is odd. In particular
(G\mid t). On the fixed shell (st^2=hn\asymp L^2).

## 3. Proof and connector

The first equality in (181.P1) is finite regrouping by (r=hn); it
retains every incidence in the divisor sum. The second is the unique
prime-by-prime representation (r=st^2) with (s) squarefree. Removing
(G) leaves coprime factors, whose squarefree parts give (181.P2).

Divisor multiplicity and bounded literal normalization give

\[
 |C_{L,X}^{\sigma}(r)|\ll\tau(r)\ll_\varepsilon X^\varepsilon.
\]

For fixed (s\leq L), support permits
(O(1+L/\sqrt s)) multipliers. For fixed (t), it permits
(O(1+L^2/t^2)) squarefree kernels. Hence

\[
 \sum_{s\leq L}\sum_t|C(st^2)|
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\]

and

\[
 \sum_{\substack{s>L\\t\geq\lceil\sqrt L\rceil}}|C(st^2)|
 \ll_\varepsilon
 L^2X^\varepsilon\sum_{\lceil\sqrt L\rceil\leq t\ll\sqrt L}t^{-2}
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

The three sectors are disjoint and exhaustive. If the remaining signed
small-(t) sum had the same bound for every shell and both signs, it would
first prove M9-M1-top-endpoint-signed-cone. The accepted top transform
would then discharge only the hard residual child of
M9-M1-physical-one-count-assembly. The smooth direct-M1 parent would remain
independent, so no full M1 or downstream implication follows.

## 4. First doubtful or unproved step

The first open step is the literal aggregate

\[
 \left|\sum_{\substack{s>L,\ \mu^2(s)=1\\1\leq t<\lceil\sqrt L\rceil}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

It is open already on (t=1). Nothing in the incidence proof supplies
the missing (L^{1/2}).

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Product fibre and multiplicity | **PASS.** Finite bijection of incidences. |
| Squarefree uniqueness | **PASS.** Prime-exponent parity. |
| (G,d,e,a,b) parametrization | **PASS.** Exact in both directions. |
| Literal fields and endpoints | **PASS.** Carried by zero extension. |
| Low radical | **PASS.** Absolute target-sized bound. |
| High radical, large (t) | **PASS.** New disjoint absolute target-sized sector. |
| (t=1) | **PASS as retained owner.** It is not discarded or averaged away. |
| Hard connector | **PASS conditionally.** Only the signed-cone child follows. |
| Smooth/GAR/M2/bridge/exponent scope | **PASS.** No implication. |

No numerical evidence or external theorem is used.

## 6. Dependencies and artifacts

The proof uses only `M9-M1-top-endpoint-transform`,
`H4-Phi-regularity`, `M9-M2-dyadic-weight-nondegeneracy`, and
`Divisor-bound-elementary`, together with the exact Round-181 reports and
candidate named in the header.

## 7. Recommended state effect

Promote one subordinate proved reduction containing the exact coordinates,
both target-safe sectors, and the exact small-(t) complement. Create that
complement as an explicit open obligation and add it as a dependency of the
hard signed-cone owner. Leave every parent, bridge, theorem, and exponent
status unchanged.
