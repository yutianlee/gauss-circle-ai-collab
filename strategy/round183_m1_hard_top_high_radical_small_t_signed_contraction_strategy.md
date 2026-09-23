# Round 183 strategy: hard-M1 complete small-t signed contraction gate

## Frozen owner and objective

Round 183 attacks only
`M9-M1-hard-top-high-radical-small-t-residual-estimate` on graph
`5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`.
For each literal middle or lower residual shell of the unique hard M1
profile and each sign \(\sigma\in\{+1,-1\}\), zero-extend the complete
normalized hard symbol and put

\[
 C_{L,X}^{\sigma}(r)=
 \sum_{\substack{h\mid r,\ h\asymp L\\
                   r/h\ \mathrm{odd},\ 4h<r/h<16h}}
 \chi_4(r/h)a_{L,X}^{\rm lit,\sigma}(h,r/h).
 \tag{183.1}
\]

The coefficient \(a_{L,X}^{\rm lit,\sigma}\) retains the literal dyadic
frequency cutoff, \(\Phi(h/(H+1))\),
\(W(\sqrt{4q_Xh/n})\), normalized \(h^{-3/4}n^{-3/4}\) powers,
profiles, floors, stars and half weights, strict cone edges, both signs, the
hard sample, real-\(X\) support crossings and endpoints, and zero extension.
No arbitrary bounded-coefficient replacement is allowed.

Writing uniquely \(r=st^2\), \(\mu^2(s)=1\), and
\(T_L=\lceil\sqrt L\rceil\), the frozen theorem is

\[
 \boxed{
 \left|
 \sum_{\substack{s>L,\ \mu^2(s)=1\\1\le t<T_L}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})
 \right|
 \ll_\varepsilon L^{3/2}X^\varepsilon .}
 \tag{183.ST}
\]

There is one absolute value only after the complete signed \((s,t)\)-sum.
The statement is uniform for every real \(X\ge2\), every admissible shell,
both signs, and every literal crossing and endpoint.  The complete \(t=1\)
coprime-squarefree cone is mandatory.

## Accepted seams and exact power ledger

Round 181 proves the multiplicity-preserving product regrouping, unique
coordinates

\[
 h=Gda^2,\qquad n=Geb^2,\qquad s=de,\qquad t=Gab,
 \qquad(da,eb)=1,
\]

and the support \(st^2\asymp L^2\).  It pays absolutely the disjoint sectors
\(s\le L\) and
\(s>L,\ t\ge T_L\) at
\(O_\varepsilon(L^{3/2}X^\varepsilon)\).  Thus (183.ST) is exactly the
remaining hard signed cone.

For fixed \(t\), the coefficient-insensitive support has size
\(O(L^2/t^2)\).  Hence the complete positive capacity is

\[
 \sum_{t<T_L}O_\varepsilon(L^2t^{-2}X^\varepsilon)
 =O_\varepsilon(L^2X^\varepsilon),
\]

already on \(t=1\).  The target needs a signed factor \(L^{1/2}\), equal to
\(X^{1/12}\) at \(L\asymp X^{1/6}\).  Capacity is not literal lower mass.

A uniform fixed-row estimate

\[
 \left|\sum_{s>L}\mu^2(s)C_{L,X}^{\sigma}(st^2)
 e(\sigma t\sqrt{Xs})\right|
 \ll_\varepsilon (L^2/t^2)^{3/4}X^\varepsilon
 \tag{183.FT}
\]

would suffice after summing \(t^{-3/2}\), but it is strictly stronger than
(183.ST) and is not the promotion object.

## Fresh mechanisms to test

The direct task may use any genuinely actual-coefficient signed relation
that proves (183.ST), including a joint \((s,t)\) transformation or a
noncentral divisor-orientation/Mellin analysis that retains the truncated
ratio cone and endpoints.  It must identify the literal feature that fails
for unsigned, dechirped, character-erased, and adversarial controls.

The hostile mechanism task tests two precise possible reductions without
substituting either for the owner.

1. With
   \(F_\sigma(r)=C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr})\), expand
   \(\mu^2(s)\) and set \(s=a^2b\), \(u=at\).  Derive the exact finite
   kernel
   \[
    K_{L,T_L}(b,u)=
    \sum_{\substack{a\mid u\\a^2b>L,\ u/a<T_L}}\mu(a)
   \]
   before estimating any part.  Determine whether a truncation near
   \(a\asymp\sqrt L\) leaves a genuinely smaller signed core or returns to
   the original hard cone plus target-safe terms.
2. Derive any fixed-row van der Corput/shifted-correlation implication with
   its exact coefficient, phase difference, shift range, diagonal, endpoint,
   and restored power.  Compare it explicitly with
   `M9-M1-shifted-divisor-correlation-PSC` and the accepted
   delta/Kloosterman \(H/L\)-deficit.  A correlation norm is only a
   sufficient route if it rigorously yields (183.ST).

A precise target-safe decomposition or mechanism self-return is useful
progress.  It is not a proof of the selected aggregate.

## No-repeat and stop boundary

Stop at the first exact seam if a proposed argument:

- deletes \(t=1\), one sign, one shell, a support crossing, or an endpoint;
- takes a positive \(s\)-, \(t\)-, divisor-, shift-, Mellin-, or Gram norm
  before the required gain;
- replaces the actual coefficient by an arbitrary, separable, character-
  erased, dechirped, or bounded-variation class without a proved transfer;
- uses only multiplier averaging, the central Mellin mode, complete Möbius
  recombination, a second reciprocal B-process, rank-one square-root wave,
  product-fibre triangle, canonical positive Gram, or combined M1/M2 cone;
- restates the old PSC or delta/Kloosterman deficit without a new literal
  contraction;
- proves only (183.FT), a shifted norm, or a strict subaggregate without an
  exact connector to (183.ST); or
- claims the smooth M1 parent, GAR, M9--M1, any M2 parent, endpoint
  uniformity, M9, a bridge, the quarter theorem, or an exponent change.

No in-round pivot to another owner is allowed.

## Orthogonal tasks

1. `literal_small_t_signed_contraction_attack`: attack the full aggregate
   directly with the exact coefficient, both signs, and one final absolute
   value; prove it, prove a strict target-safe signed sector, or isolate the
   first exact actual-direction self-return.
2. `partial_mobius_shifted_correlation_barrier_audit`: derive and audit the
   exact truncated-Möbius and shifted-correlation mechanisms, restored
   powers, old-PSC overlap, and owner connectors.
3. `blind_complete_small_t_rederivation`: from a self-contained statement
   only, rederive the finite kernel, capacity, false controls, and the first
   additional structural relation needed for target cancellation.

## Exit and promotion gates

The round closes under exactly one label:

- `hard_m1_small_t_target`;
- `strict_hard_m1_small_t_sector`; or
- `small_t_signed_mechanism_capacity_or_self_return_no_go`.

Promotion of (183.ST) requires a complete proof for every listed
quantifier, independent coefficient/product/endpoint and power reviews,
post-unmask blind consistency, exact failure of unsigned/adversarial
controls, and the accepted connector to the hard signed cone.  A strict
sector may be promoted only at its exact scope with its complement explicit.
A mechanism no-go may create or update only its exact obstruction scope.

Even complete success first closes only
`M9-M1-top-endpoint-signed-cone`.  The smooth direct-M1 parent, M9--M1,
all M2 parents, endpoint uniformity, M9, both bridges, and the quarter
theorem remain separate.  The exponent ledger remains internal \(1/3\),
accepted external \(0.3144831759740614\ldots\), target \(1/4\).
