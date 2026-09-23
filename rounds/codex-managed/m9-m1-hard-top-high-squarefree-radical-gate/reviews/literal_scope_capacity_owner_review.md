# Round 181 literal, scope, capacity, and owner review

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Review role: hostile literal/scope/capacity/owner seam
- Starting graph SHA-256: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Generated: `2026-08-27T08:35:57.6171565Z`
- Status: review evidence only; no shared proof-state edit is authorized

## 1. Verdict

**Conditional pass with three mandatory local repairs and a terminal-label
correction.**  The exact product regrouping, squarefree-kernel split,
literal support bounds, low-radical estimate, and the new disjoint
large-square-multiplier sector are valid.  For each literal frequency sign,
put

\[
 T_L=\lceil\sqrt L\rceil .
\]

The owner is partitioned exactly as

\[
 \{s\le L\}\ \dot\cup\
 \{s>L,\ t\ge T_L\}\ \dot\cup\
 \{s>L,\ 1\le t<T_L\}.
\tag{R181.V1}
\]

The first two pieces have absolute price
\(O_\varepsilon(L^{3/2}X^\varepsilon)\); the last is the exact retained
literal complement and contains the full \(t=1\) squarefree-coprime face.
Its coefficient-insensitive capacity remains
\(O_\varepsilon(L^2X^\varepsilon)\), and no literal signed bound for it is
proved.

Accordingly the correct unique terminal exit is
`strict_hard_m1_radical_sector`, not
`hard_m1_high_radical_capacity_or_self_return_no_go`.  The large-\(t\)
piece is a genuine strict sector inside the frozen high-radical owner.  The
Möbius and Mellin observations may be retained only as narrowly scoped
route diagnostics; they do not supply the required new terminal no-go.

Before promotion, repair:

1. insert an absolute value (or, more strongly, the sum of absolute values)
   in (1.4) of `hard_m1_high_radical_signed_attack.md`;
2. repair the blind \(t=1\) density control at the prime \(2\) by also
   requiring \(4\nmid h\), or simply by restricting \(h\) to be odd; and
3. add the protocol-required generated-time metadata to the two selected-
   context reports, and add both the opaque brief-supplied graph hash and
   generated time to the blind report.

These repairs are local.  They do not affect (R181.V1), the capacity ledger,
or the owner decision.

## 2. Literal fields, signs, and exact algebra

The two selected-context reports correctly zero-extend the actual symbol
before grouping.  This is the decisive literal convention: the dyadic
shell, \(\Phi(h/(H+1))\), hard sample
\(W(\sqrt{4q_Xh/n})\), normalized powers, strict cone edges, floors,
stars/half weights, removed terminal and isolated owners, real-\(X\)
crossings, and sign tag remain coefficient values rather than altered
support conditions.  Product grouping therefore preserves every incidence
and every product-fibre multiplicity.

The signwise formulation is sound.  With the actual zero-extended
\(a_{L,X}^{\sigma}\), \(\sigma\in\{+1,-1\}\), one has exactly

\[
 \mathcal T_{L,\sigma}^{M1}
 =\sum_r C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr})
 =\sum_{\mu^2(s)=1}\sum_{t\ge1}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}).
\tag{R181.V2}
\]

All counting and Möbius identities are independent of \(\sigma\).  The
accepted hard transform needs the positive stationary cone and restores
the opposite frequency by the already accepted conjugate/two-sided
combination.  Thus no independent negative-frequency theorem has silently
been assumed.  A State Patch should nevertheless state every promoted
reduction signwise, rather than suppressing \(\sigma\) midway through the
formulae.

The parametrization

\[
 h=Gda^2,\qquad n=Geb^2,\qquad s=de,\qquad t=Gab,
\]

with squarefree \(d,e\), \((da,eb)=1\), and \(Geb\) odd, is bijective.
It gives \((h,n)=G\mid t\) and
\(\chi_4(n)=\chi_4(Ge)\), including the even-\(h\) branch.  It agrees with
the already accepted squarefree-coordinate algebra in the graph; it is a
valid owner-specific rederivation, not a new generic mechanism.

## 3. Thresholds, constants, capacities, and overlap

If the literal shell is contained in
\(c_0L\le h\le c_1L\), then strict \(4h<n<16h\) gives

\[
 4c_0^2L^2<r<16c_1^2L^2,
 \qquad
 \frac{2c_0L}{\sqrt s}<t<\frac{4c_1L}{\sqrt s}.
\tag{R181.V3}
\]

This justifies \(s\ll L^2\), \(t\asymp L/\sqrt s\), and
\(s>L\Rightarrow t\ll\sqrt L\), with constants uniform in the fixed
profile.  For fixed \(s\), there are
\(O(1+L/\sqrt s)\) possible \(t\)'s; for fixed supported \(t\), there are
\(O(L^2/t^2)\) possible \(s\)'s.  Together with
\(|C(st^2)|\ll_\varepsilon X^\varepsilon\), these give

\[
 \sum_{s\le L}\sum_t|C(st^2)|
 \ll_\varepsilon L^{3/2}X^\varepsilon
\]

and, on the disjoint high-radical tail,

\[
 \sum_{\substack{s>L\\t\ge T_L}}|C(st^2)|
 \ll_\varepsilon L^2X^\varepsilon
 \sum_{t\ge T_L}t^{-2}
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{R181.V4}
\]

Equation (1.4) of the signed-attack report currently omits modulus bars even
though it is a complex sum.  Its proof establishes the stronger (R181.V4),
so this is a statement defect, not a mathematical obstruction.

The low-\(s\) and large-\(t\) descriptions overlap if they are stated on
the whole cone.  There is no overlap in (R181.V1), because the promoted
large-\(t\) child must retain the explicit condition \(s>L\).  Likewise
\(G\ge\sqrt L\) is only an alternative target-safe subset: since
\(G\mid t\), it is contained in the large-\(t\) region (apart from the
separate low-\(s\) part).  It must not be installed as a third disjoint
owner or have its bound added again.

The blind report's universal high capacity follows independently from
\(\#\mathcal D_L\asymp L^2\) and the
\(L^{3/2+o(1)}\) low count, so it survives the following repair.  Its
specific \(t=1\) construction excludes \(p^2\mid h\), \(p^2\mid n\), and
\(p\mid(h,n)\) only for odd primes, but then incorrectly says every
remaining \(h\) is squarefree.  Add \(4\nmid h\), or restrict to odd
\(h\).  The union bound still leaves positive density and restores the
claimed \(\gg L^2\) squarefree-coprime \(t=1\) control.

The fixed-\(t\) ledger is also correct: its positive capacity is
\(S_t=L^2/t^2\), the proposed \(S_t^{3/4}\) estimate needs
\(S_t^{1/4}=L^{1/2}t^{-1/2}\), and the proposed bounds would sum because
\(\sum t^{-3/2}<\infty\).  This is a sufficiency calculation only.

## 4. Mellin factor and full-versus-truncated divisor sums

For the complete unweighted divisor kernel

\[
 D_r(\tau)=\sum_{hn=r}\chi_4(n)(n/h)^{i\tau},
\]

the signed-attack factorization is correct:

\[
 D_r(\tau)=r^{-i\tau}
 \prod_{p^k\parallel r}\sum_{j=0}^k
 \chi_4(p)^j p^{2ij\tau}.
\tag{R181.V5}
\]

The prime \(2\) must not be dropped.  When \(2^k\parallel r\), its inner
polynomial is \(1\), because \(\chi_4(2^j)=0\) for \(j\ge1\), but its full
local factor is still
\(2^{-ik\tau}\) from the prefactor.  The report states this correctly and
is consistent with the accepted graph cocycle.

At \(\tau=0\), an odd \(p\equiv3\pmod4\) occurring to odd exponent makes
the corresponding complete local sum vanish.  This is only a central-mode
identity.  The literal coefficient

\[
 C_{L,X}(r)=\sum_{h\mid r}\chi_4(r/h)
 1_{h\asymp L}1_{4h<r/h<16h}
 a^{\rm lit}_{L,X}(h,r/h)
\]

is a truncated, \((L,X)\)-dependent weighted divisor sum and is not
multiplicative.  On a genuinely smooth piece it may be represented as an
inverse Mellin superposition of the *full* kernels (R181.V5), with an
\(r\)-dependent transform; sharp edges, stars, floors, crossings, and
other nonsmooth pieces remain separate.  No uniform transform-seminorm
bound is proved.  Therefore a promoted statement must not identify
\(C_{L,X}\) with \(D_r\), import an Euler product for \(C_{L,X}\), or infer
the target from the single value \(D_r(0)\).  The lawful conclusion is only
that the central zero alone gives no estimate for the complete inverse
Mellin integral.

## 5. No-repeat and mechanism scope

The reports correctly stop product-fibre triangle at \(L^2\), retain the
\(t=1\) face, and use the second \(B\)-process, canonical Gram, combined
M1/M2 cone, and joint-\(t\) lift only as controls.  The joint-\(t\) map is a
permutation of product indices, so it creates no automatic orthogonality;
this does not rule out a future theorem exploiting additional literal
coefficient correlations.

The exact Möbius formula

\[
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_tF(st^2)
 =\sum_{b,u}K_L(b,u)F(bu^2)
 =\mathcal T_L^{M1}+O_\varepsilon(L^{3/2}X^\varepsilon)
\tag{R181.V6}
\]

is valid once (R181.V3) ensures \(r>L\) for sufficiently large \(L\), with
bounded \(L\) handled separately.  Its no-go scope must be exactly:
**complete Möbius inversion followed by complete recombination supplies no
automatic gain**.  It does not rule out a coefficient-sensitive signed
bilinear estimate before recombination.  Moreover, the authoritative graph
already contains the same mechanism class in
`M9-M1-lower-cone-t1-d1-squarefree-mobius-collapse-obstruction`
(Round 153).  Thus (R181.V6) is a useful owner-specific identity and
no-repeat check, but it is not the first genuinely new mechanism needed to
justify Round 181's no-go terminal label.

The gcd and central-Mellin conclusions require the same narrow language:
\(G\mid t\) gives no power at \(t=1\); a central complete-divisor zero does
not control noncentral or literal truncated modes.  Neither statement is
an impossibility theorem for all future gcd-aware, Mellin, spectral, or
signed correlation methods.  All \(L^2\) examples remain adversarial or
coefficient-insensitive capacities, never literal lower bounds.

## 6. Owner implication, downstream scope, and exponent quarantine

If the complete high-radical estimate were proved for every literal
residual hard shell, then adding the low-radical bound would give
\(\mathcal T_{L,\sigma}^{M1}\ll L^{3/2}X^\varepsilon\).  Through the
accepted one-sided transform and conjugate-sign restoration, this would
close only `M9-M1-top-endpoint-signed-cone`, i.e. the middle/lower hard
residual child of `M9-M1-physical-one-count-assembly`.

That hypothesis is not proved.  After Round 181 the small-\(t\) remainder
in (R181.V1), especially \(t=1\), remains open.  Hence
`M9-M1-top-endpoint-signed-cone` stays open.  The independent literal
smooth M1 parent also stays open, so there is no implication to `M9-M1`,
GAR, M9-M2, endpoint uniformity, `M9`, either bridge, the quarter theorem,
or a Gauss-circle exponent improvement.

The normalized deficit is \(L^{1/2}\).  It equals \(X^{1/12}\) only on
the critical shell \(L\asymp X^{1/6}\); it is not a new global exponent.
The reports otherwise maintain this quarantine.

## 7. Artifact hygiene and recommended state effect

The authoritative graph parses successfully and its current SHA-256 is
exactly the frozen campaign hash.  All three reports obey the seven-section
contract, list their context artifacts, declare candidate-only status, use
no numerical theorem evidence, and make no shared-state mutation.  The
blind report's mathematical vocabulary is consistent with its isolated
packet; no sibling-specific dependency is visible.

The protocol nevertheless requires generated-time metadata on every
artifact.  Both selected-context reports omit it; the blind report also
omits the graph hash supplied opaquely by its brief.  Repair those headers
before treating the reports as promotion evidence.  Also repair the two
formula-level defects identified in Sections 1 and 3.

After those local repairs, promote only:

1. the signwise exact product/squarefree identities and literal support
   constants;
2. the low-radical absolute bound;
3. the disjoint strict high-radical sector
   \(s>L,\ t\ge\lceil\sqrt L\rceil\), with exact complement
   \(s>L,\ 1\le t<\lceil\sqrt L\rceil\);
4. optionally, the owner-specific identity (R181.V6), explicitly linked to
   the pre-existing Round-153 mechanism class and scoped to complete
   inversion/recombination; and
5. the coefficient-insensitive/adversarial controls and central-Mellin
   warning, with no literal lower-bound language.

Use the unique exit label `strict_hard_m1_radical_sector`.  Retain (181.HR)
and `M9-M1-top-endpoint-signed-cone` open, and make no downstream or
exponent promotion.

### Exact artifacts reviewed

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round181_selection/conductor_round181_selection_decision.md`
- `strategy/round181_m1_hard_top_high_squarefree_radical_strategy.md`
- `strategy/round181_selection/m1_gar_frontier_selection.md`
- `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/plan.json`
- `rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/blind_statement.md`
- all three task briefs and all three Round-181 reports
- the authoritative Round-145 squarefree-coordinate and Round-153
  complete-Möbius obstruction entries used only for the no-repeat check
- the accepted Round-119 hard normalization/owner connector and Round-9
  combined-top synthesis used only to verify owner scope
