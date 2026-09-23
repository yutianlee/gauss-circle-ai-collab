# Round 183 synthesis

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Round: 183
- Generated: `2026-08-27T20:27:06.6678285+08:00`
- Starting graph:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Closing label: `strict_hard_m1_small_t_sector`
- Role: conductor synthesis; State Patch evidence, not self-authorizing
  state
- Numerical work: none; 100% analytic/algebraic

## Outcome

Round 183 proves a genuine actual-coefficient signed sector inside the
hard-M1 high-radical small-\(t\) owner.  After expanding the exact divisor
coefficient, write each incidence as

\[
 h=Gu,\qquad n=Gv,\qquad (u,v)=1,
\]

so

\[
 s=\operatorname{sf}(uv),\qquad
 t=G\sqrt{uv/\operatorname{sf}(uv)}.
\]

On the sector

\[
 G\geq\lceil L^{1/4}\rceil,\qquad
 \operatorname{dist}(2\sqrt{Xuv},\mathbb Z+\tfrac12)
 \geq(10\log(2X))^{-1},
\]

the zero-extended literal ray symbol has uniform step-two BV, while the
actual odd-\(G\) character-phase progression has geometric ratio
\(-e(2\sigma\sqrt{Xuv})\).  Abel summation followed by a count of
\(O(L^{3/2})\) primitive rays proves

\[
 |\mathcal A^{\mathrm{ray,nr}}_{L,X,\sigma}|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

This improves the coefficient-insensitive \(L^{7/4}\) incidence envelope
of that proper sector and is therefore real before-positivity progress.

## Exact remaining owner

The complete small-\(t\) theorem is not proved.  Its exact incidence-level
remainder is

\[
 \{G<\lceil L^{1/4}\rceil\}\ \dot\cup\
 \{G\geq\lceil L^{1/4}\rceil:
 \operatorname{dist}(2\sqrt{Xuv},\mathbb Z+\tfrac12)
 <(10\log(2X))^{-1}\},
\]

with every original literal predicate retained.  The entire \(t=1\) face
lies in the small-\(G\) part.  The sector is a partition of literal
incidences, not of product indices.

## Mechanism results

The exact two-cutoff Mobius kernel is

\[
 K_{L,T}(b,u)=
 \sum_{\substack{a\mid u\\a^2b>L\\u/a<T}}\mu(a),
 \qquad T=\lceil\sqrt L\rceil.
\]

On \(b>L,u<T\), it equals \(\mathbf1_{u=1}\).  All other transformed
regions are target-safe.  Consequently the complete small-\(t\) scalar
equals the full product wave modulo target size.  A cutoff at \(a=T\)
discards a safe tail, but its small-\(a\) core still self-returns to that
full wave and retains \(a=t=u=1\).

The exact fixed-row Fejer connector identifies a possible sufficient
radical-shift correlation theorem, but the required signed brace remains
unproved at \(t=1\).  Rowwise triangle makes it stronger than the frozen
owner.  It is not the old PSC, and the old delta/Kloosterman obstruction
does not transfer as a theorem.

## Proof status

The strict sector and truncated-Mobius self-return are subordinate
progress only.  `M9-M1-hard-top-high-radical-small-t-residual-estimate`
and `M9-M1-top-endpoint-signed-cone` remain open.  Even a future proof of
the complete hard cone would leave the independent smooth direct-M1 parent
open.  GAR, M9-M1, all M2 parents, endpoint uniformity, M9, both bridges,
and the Gauss-circle quarter theorem remain open.

There is no global exponent improvement: the strongest internally proved
exponent remains \(1/3\); the accepted external benchmark remains
\(0.3144831759740614\ldots\); the target remains \(1/4\).

## State decision

The reviewed patch creates one proved subordinate incidence-sector lemma,
updates only the open small-\(t\) owner and the existing scoped obstruction,
rejects thirteen overclaims, and makes no parent, theorem, bridge, or
exponent change.  Round 184 remains undesigned until the Round-183 patch,
reverse audit, proof-draft update, lifecycle closure, and final hygiene
review are complete.
