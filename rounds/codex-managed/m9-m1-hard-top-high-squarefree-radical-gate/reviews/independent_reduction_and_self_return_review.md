# Independent reduction and self-return review

- Campaign: `m9-m1-hard-top-high-squarefree-radical-gate`
- Round: 181
- Role: independent mathematical reconciliation
- Generated: `2026-08-27T08:44:04.7412815Z`
- Starting graph SHA-256 checked: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Review status: **GREEN for a strict-sector close; no parent promotion**

## 1. Verdict and terminal label

The three reports are mathematically compatible after distinguishing three
different assertions:

1. the squarefree split is an exact partition, and its low-radical part is
   target-safe;
2. inside the high-radical part, the literal sector
   \(t\geq\lceil\sqrt L\rceil\) is also target-safe, leaving the exact
   complement \(s>L\), \(1\leq t<\lceil\sqrt L\rceil\);
3. complete Möbius linearization of the high-radical indicator returns to
   the original hard product wave modulo a target-safe term, while the
   bounded-coefficient envelope still has \(L^2\) capacity already at
   \(t=1\).

The complete literal high-radical estimate is not proved.  Nevertheless,
item 2 is a genuine positive, owner-compatible strict sector, whereas the
Möbius and capacity conclusions are mechanism-scoped obstructions and do
not disprove the literal target.  Selecting by mathematical strength rather
than by report count therefore gives the unique Round-181 terminal label

`strict_hard_m1_radical_sector`.

The discovery report's proposed
`hard_m1_high_radical_capacity_or_self_return_no_go` is valid as a scoped
barrier description, but is too weak as the round label once its own
large-\(t\) theorem is retained.  The hostile report's strict-sector label
is correct; its rationale should include the new high-radical large-\(t\)
sector, not rely only on the already anticipated low-radical payment.

## 2. Exact product and squarefree parametrizations

Fix one literal residual hard shell, one sign
\(\sigma\in\{+1,-1\}\), and extend its exact symbol by zero away from
the literal support.  Write

\[
 \mathcal T_{L,\sigma}
 =\sum_h\sum_{\substack{4h<n<16h\\n\ {\rm odd}}}
 \chi_4(n)a_{L,X}^{\mathrm{lit},\sigma}(h,n)
 e(\sigma\sqrt{Xhn})
\]

and

\[
 C_{L,X}^{\sigma}(r)=
 \sum_{\substack{h\mid r\\h\in I_{L,X}\\r/h\ {\rm odd}\\
                         4h<r/h<16h}}
 \chi_4(r/h)a_{L,X}^{\mathrm{lit},\sigma}(h,r/h).
\]

Finite regrouping gives exactly

\[
 \mathcal T_{L,\sigma}
 =\sum_r C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr})
 =\sum_{\substack{s\geq1\\\mu^2(s)=1}}
   \sum_{t\geq1}C_{L,X}^{\sigma}(st^2)
       e(\sigma t\sqrt{Xs}).                                      \tag{2.1}
\]

The first map is a bijection between literal incidences \((h,n)\) and
the pairs \((r,h)\) occurring in the divisor sum; it is not a claim that
a product fibre contains only one incidence.  The second map is unique
prime by prime:

\[
 s=\prod_{v_p(r)\ {\rm odd}}p,
 \qquad
 t=\prod_p p^{\lfloor v_p(r)/2\rfloor}.                            \tag{2.2}
\]

The more refined parametrization in the discovery report is also exact.
For a literal incidence put \(G=(h,n)\), \(h=Gu\), \(n=Gv\), and
\((u,v)=1\).  There are unique squarefree \(d,e\) and positive
\(a,b\) such that

\[
 u=da^2,\qquad v=eb^2.
\]

Consequently

\[
 h=Gda^2,\qquad n=Geb^2,\qquad s=de,\qquad t=Gab,                  \tag{2.3}
\]

with \((da,eb)=1\) and \(Geb\) odd.  Conversely these conditions,
together with the literal shell and strict cone tests, reconstruct one
and only one incidence.  Thus the exact fibre formula is

\[
 C_{L,X}^{\sigma}(st^2)=
 \sum_{de=s}^{\rm ord}
 \sum_{\substack{Gab=t,\ (da,eb)=1\\Geb\ {\rm odd}\\
                   Gda^2\in I_{L,X}\\4da^2<eb^2<16da^2}}
 \chi_4(Ge)
 a_{L,X}^{\mathrm{lit},\sigma}(Gda^2,Geb^2).                     \tag{2.4}
\]

Here \(\chi_4(Geb^2)=\chi_4(Ge)\) because \(b\) is odd.  Formula
(2.4) retains every floor, star, sign, hard sample, support crossing,
removed owner, and endpoint through the zero-extended literal symbol.

If \(c_0L\leq h\leq c_1L\) on the shell, then the strict cone gives

\[
 4c_0^2L^2<st^2<16c_1^2L^2,
 \qquad
 \frac{2c_0L}{\sqrt s}<t<\frac{4c_1L}{\sqrt s}.                  \tag{2.5}
\]

Hence \(s\ll L^2\), and \(s>L\) implies \(t\ll\sqrt L\).
For fixed supported \(t\), the ambient \(s\)-interval has length
\(O(L^2/t^2)\).  The notation \(S_t\asymp L^2/t^2\) in the blind
report describes this ambient interval scale, not a lower bound for the
number of nonzero literal coefficients.

Finally, if \(p^\alpha\Vert h\) and \(p^\beta\Vert n\), then

\[
 v_p((h,n))=\min(\alpha,\beta)
 \leq\left\lfloor\frac{\alpha+\beta}{2}\right\rfloor=v_p(t).
\]

Thus

\[
 (h,n)\mid t.                                                     \tag{2.6}
\]

This is one-way only.  At \(t=1\), it forces \(G=a=b=1\), so the
face is precisely the coprime squarefree cone \(h=d,n=e\); it loses no
power of geometric incidence.

## 3. Low radical, large \(t\), and fixed-\(t\) powers

The normalized literal coefficient is uniformly bounded on the fixed
cone.  Therefore

\[
 |C_{L,X}^{\sigma}(r)|\ll \tau(r)\ll_\varepsilon X^\varepsilon, \tag{3.1}
\]

where the last absorption uses \(r\ll L^2\) and the accepted active
range \(L\ll X^{1/4}\).  For fixed squarefree \(s\), (2.5) leaves
\(O(1+L/\sqrt s)\) integers \(t\).  It follows that

\[
 \sum_{\substack{s\leq L\\\mu^2(s)=1}}\sum_t
 |C_{L,X}^{\sigma}(st^2)|
 \ll_\varepsilon
 X^\varepsilon\sum_{s\leq L}
 \left(1+\frac L{\sqrt s}\right)
 \ll_\varepsilon L^{3/2}X^\varepsilon.                          \tag{3.2}
\]

This proves the low-radical payment uniformly and absolutely.  The
blind report's \(\gg L^{3/2}\) construction correctly shows sharpness
of this exponent for a full geometric dyadic cone; it is not a lower
bound for the literal signed coefficient.

For fixed \(t\) in the nonempty high-radical range,

\[
 \sum_{\substack{s>L\\\mu^2(s)=1}}
 |C_{L,X}^{\sigma}(st^2)|
 \ll_\varepsilon \frac{L^2}{t^2}X^\varepsilon.                  \tag{3.3}
\]

With \(T_L=\lceil\sqrt L\rceil\), the support restriction
\(t\ll\sqrt L\) and (3.3) give

\[
 \sum_{\substack{s>L,\ \mu^2(s)=1\\t\geq T_L}}
 |C_{L,X}^{\sigma}(st^2)|
 \ll_\varepsilon L^2X^\varepsilon
       \sum_{T_L\leq t\ll\sqrt L}t^{-2}
 \ll_\varepsilon L^{3/2}X^\varepsilon.                          \tag{3.4}
\]

Thus the full cone has the exact decomposition

\[
 \mathcal T_{L,\sigma}
 =\mathcal S_{s\leq L,\sigma}
  +\mathcal S_{s>L,\,t\geq T_L,\sigma}
  +\mathcal R_{s>L,\,1\leq t<T_L,\sigma},                       \tag{3.5}
\]

where each of the first two terms is already
\(O_\varepsilon(L^{3/2}X^\varepsilon)\).  Equation (3.5), with its
literal small-\(t\) complement, is the strict-sector result that governs
the terminal label.

The proposed stronger fixed-\(t\) estimate

\[
 \left|\sum_{\substack{s>L\\\mu^2(s)=1}}
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})\right|
 \ll_\varepsilon (L^2/t^2)^{3/4}X^\varepsilon                  \tag{3.6}
\]

would be sufficient, because

\[
 \sum_{t\ll\sqrt L}(L^2/t^2)^{3/4}
 =L^{3/2}\sum_{t\ll\sqrt L}t^{-3/2}\ll L^{3/2}.                \tag{3.7}
\]

This summation is correct.  Statement (3.6) is unproved and is stronger
than the aggregate target.  Relative to (3.3), it requires the factor
\(L^{1/2}t^{-1/2}\), in particular the full missing \(L^{1/2}\) on
the mandatory \(t=1\) face.  The blind shifted-correlation condition is
a valid sufficient condition for (3.6), but it is neither proved nor
necessary for the aggregate theorem and should not become a graph node.

On a full interior cone there are \(\gg L^2\) odd, coprime squarefree
pairs.  Sitewise complex dechirping therefore gives \(\gg L^2\) on
\(t=1\) in the arbitrary bounded-coefficient class.  This verifies the
coefficient-uniform capacity obstruction.  It is not a lower bound for
\(a_{L,X}^{\mathrm{lit},\sigma}\), and no report confuses the two after
its explicit quarantine.

## 4. Exact Möbius identity and self-return

Put

\[
 F_\sigma(r)=C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr}),\qquad
 K_L(b,u)=\sum_{\substack{a\mid u\\a^2b>L}}\mu(a).
\]

Since all sums are finite after zero extension, inserting
\(\mu^2(s)=\sum_{a^2\mid s}\mu(a)\), writing \(s=a^2b\), and then
\(u=at\), gives the exact identity

\[
 \mathcal H_{L,\sigma}:=
 \sum_{\substack{s>L\\\mu^2(s)=1}}\sum_tF_\sigma(st^2)
 =\sum_{b,u\geq1}K_L(b,u)F_\sigma(bu^2).                         \tag{4.1}
\]

For \(b>L\), every divisor \(a\mid u\) is admitted, so

\[
 K_L(b,u)=\sum_{a\mid u}\mu(a)=\mathbf 1_{u=1}.                 \tag{4.2}
\]

An exact all-\(L\) form of the self-return, avoiding the harmless
"sufficiently large \(L\)" shortcut in the discovery report, is

\[
 \mathcal H_{L,\sigma}=\mathcal T_{L,\sigma}+E_{L,\sigma},       \tag{4.3}
\]

where

\[
 E_{L,\sigma}=
 \sum_{\substack{b\leq L\\u\geq1}}K_L(b,u)F_\sigma(bu^2)
 -\sum_{r\leq L}F_\sigma(r).                                    \tag{4.4}
\]

Indeed, (4.2) supplies \(\sum_{b>L}F_\sigma(b)\), and adding (4.4)
restores \(\sum_rF_\sigma(r)\).  On product support
\(bu^2\asymp L^2\), one has \(u\asymp L/\sqrt b\), while
\(|K_L(b,u)|\leq\tau(u)\) and
\(|F_\sigma(bu^2)|\ll_\varepsilon X^\varepsilon\).  Hence

\[
 |E_{L,\sigma}|\ll_\varepsilon L^{3/2}X^\varepsilon.            \tag{4.5}
\]

For nontrivial large shells the second sum in (4.4) vanishes because
the product support lies above \(L\); in general it is only
\(O_\varepsilon(LX^\varepsilon)\).  Of course (4.3) is also consistent
with the tautological split
\(\mathcal H=\mathcal T-\mathcal S_{s\leq L}\): the Möbius correction
is exactly the negative low-radical contribution after regrouping.

Thus complete squarefree Möbius linearization retains the literal
direction but gives no new contraction: estimating the transformed main
term is owner-equivalent to estimating \(\mathcal T_{L,\sigma}\), modulo
(4.5).  This is a rigorous no-go for that mechanism only, not a
counterexample to the high-radical target.

The discovery report's central Mellin calculation is also correctly
scoped.  For the unrestricted divisor mode,

\[
 D_r(\tau)=r^{-i\tau}
 \prod_{p^k\parallel r}\sum_{j=0}^k\chi_4(p)^jp^{2ij\tau}.
\]

At \(\tau=0\), an odd \(p\equiv3\pmod4\) with odd \(k\) annihilates
its local factor.  The literal incomplete divisor coefficient, however,
requires the whole inverse Mellin integral and its nonsmooth endpoint
pieces; \(1-p^{2i\tau}\) is not uniformly small away from zero.  The
central mode is therefore not a literal high-radical estimate.

## 5. Hard-parent connector and remaining owner

If the complete high-radical estimate were proved for every residual hard
shell and both signs, then (3.2) would give

\[
 \mathcal T_{L,\sigma}\ll_\varepsilon L^{3/2}X^\varepsilon.      \tag{5.1}
\]

This is exactly the normalized statement of
`M9-M1-top-endpoint-signed-cone`.  The accepted one-sided transform is

\[
 \mathcal M^+_{1,\mathrm{end},L}
 =-\frac{2e(1/8)}{\pi}X^{1/4}L^{-3/2}\mathcal T_{L,+}
  +\mathcal E^+_{1,\mathrm{bdry},L}+O_W(\log(2L)),               \tag{5.2}
\]

with target-safe boundary error.  Equations (5.1)--(5.2), conjugate-sign
restoration, and the logarithmic shell sum would give the physical hard
residual block at \(O_\varepsilon(X^{1/4+\varepsilon})\).

Round 181 proves only the two safe pieces in (3.5), not its residual.
Therefore `M9-M1-top-endpoint-signed-cone` remains open.  Even a future
proof of that node would discharge only the hard residual child of
`M9-M1-physical-one-count-assembly`; the independent node
`M9-M1-direct-smooth-residual-blockwise-estimate` would remain open.
There is no implication here to `M9-M1`, GAR, M9-M2, M9, either bridge,
the quarter theorem, or an exponent improvement.

## 6. Candidate graph statements and dependencies

The following are the exact candidate statements supported by this
round.  They are recommendations for the conductor's State Patch, not
edits made by this review.

### Candidate R181-A: hard product/squarefree parametrization

- Proposed ID: `M9-M1-hard-product-squarefree-parametrization`
- Type/status: `reduction` / `proved_internal`
- Direct dependencies:
  `M9-M1-top-endpoint-transform`, `H4-Phi-regularity`,
  `M9-M2-dyadic-weight-nondegeneracy`.
- Exact statement: For every literal middle or lower residual shell of
  the unique hard M1 profile and each sign, (2.1)--(2.5) hold with the
  zero-extended actual symbol.  The incidence parametrization (2.3)--(2.4)
  is bijective, preserves \(\chi_4\), strict cone edges, floors, stars,
  signs, hard sample, and support crossings, and satisfies \((h,n)\mid t\).
- Intended consumers: Candidates R181-B, R181-C, R181-D, and the residual
  hard-cone obligation below.

### Candidate R181-B: strict safe radical/multiplier sectors

- Proposed ID: `M9-M1-hard-radical-large-multiplier-safe-sectors`
- Type/status: `lemma` / `proved_internal`
- Direct dependencies:
  `M9-M1-hard-product-squarefree-parametrization`,
  `Divisor-bound-elementary`.
- Exact statement: Uniformly for every literal residual hard shell and
  each sign,
  \[
   \sum_{s\leq L,\mu^2(s)=1}\sum_t|C(st^2)|
   +\sum_{s>L,\mu^2(s)=1}\sum_{t\geq\lceil\sqrt L\rceil}|C(st^2)|
   \ll_\varepsilon L^{3/2}X^\varepsilon.
  \]
  The exact unresolved complement is
  \(s>L\), \(1\leq t<\lceil\sqrt L\rceil\), including \(t=1\).
- Intended effect: justify the round's strict-sector label and narrow the
  next hard-cone owner; it does not itself imply the signed-cone node.

### Candidate R181-C: actual-direction Möbius self-return

- Proposed ID: `M9-M1-hard-high-radical-mobius-self-return`
- Type/status: `obstruction` / `proved_internal`
- Direct dependencies:
  `M9-M1-hard-product-squarefree-parametrization`,
  `M9-M1-hard-radical-large-multiplier-safe-sectors`,
  `Divisor-bound-elementary`.
- Exact statement: With \(F_\sigma\), \(K_L\), and \(E_{L,\sigma}\)
  as in (4.1)--(4.4), the complete literal high-squarefree-radical
  aggregate satisfies
  \[
    \mathcal H_{L,\sigma}=\mathcal T_{L,\sigma}+E_{L,\sigma},
    \qquad
    E_{L,\sigma}\ll_\varepsilon L^{3/2}X^\varepsilon.
  \]
  Therefore complete Möbius linearization and complete joint-\(t\)
  reindexing provide no saving beyond the original hard owner.  This does
  not obstruct a new literal small-\(t\) signed theorem.
- Intended effect: a route-scoped obstruction with no downstream
  implication.

### Candidate R181-D: coefficient-uniform \(t=1\) capacity obstruction

- Proposed ID: `M9-M1-hard-high-radical-t1-capacity-no-go`
- Type/status: `obstruction` / `proved_internal`
- Direct dependencies:
  `M9-M1-hard-product-squarefree-parametrization`,
  `Divisor-bound-elementary`,
  `M9-M1-direct-hard-smooth-separate-one-third-minimax`.
- Exact statement: On a full interior geometric hard cone, the high-radical
  bounded-complex-coefficient class has capacity \(\Theta(L^2)\), already
  on \(t=1\), via a positive-density set of odd coprime squarefree pairs
  and sitewise character/phase dechirping.  Hence product triangle,
  character erasure, coefficient-uniform Gram/\(TT^*\), gcd pruning, and
  square-multiplier averaging cannot yield the required \(L^{3/2}\)
  bound.  This is not literal lower mass; at \(L\asymp X^{1/6}\) it
  records only the missing capacity factor \(L^{1/2}=X^{1/12}\).
- Intended effect: a mechanism obstruction, consistent with the existing
  product-fibre and canonical-Gram scope obstructions.

### Candidate R181-E: open residual owner after the strict sector

- Proposed ID: `M9-M1-hard-high-radical-small-t-residual-estimate`
- Type/status: `candidate_lemma` / `open`
- Direct dependencies:
  `M9-M1-hard-product-squarefree-parametrization`,
  `M9-M1-hard-radical-large-multiplier-safe-sectors`.
- Exact statement: Uniformly for every literal residual hard shell and
  both signs,
  \[
   \left|\sum_{\substack{s>L,\ \mu^2(s)=1}}
     \sum_{1\leq t<\lceil\sqrt L\rceil}
     C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs})\right|
   \ll_\varepsilon L^{3/2}X^\varepsilon.
  \]
- Intended implication: together with Candidate R181-B, this implies
  `M9-M1-top-endpoint-signed-cone`; that existing node must remain open
  until the displayed residual estimate is proved.

## 7. Report reconciliation and first open step

- `blind_hard_m1_radical_rederivation.md` independently verifies the exact
  regrouping, low-sector power, high arbitrary-coefficient capacity,
  mandatory \(t=1\) control, and conditional fixed-\(t\) summation.  Its
  shifted-correlation display is only an illustrative sufficient input.
- `hard_m1_radical_connector_capacity_audit.md` correctly verifies the
  literal seams, \((h,n)\mid t\), low-radical ledger, coefficient-uniform
  obstruction, and conditional hard-parent connector.
- `hard_m1_high_radical_signed_attack.md` adds the strongest positive
  theorem of the round, namely (3.4), as well as the refined incidence
  parametrization and the exact actual-direction Möbius self-return.

The first unproved step is now the literal residual in Candidate R181-E,
and already its \(t=1\) face:

\[
 \sum_{\substack{de\ {\rm squarefree}\\d\in I_{L,X},\ e\ {\rm odd}\\
                  4d<e<16d}}
 \chi_4(e)a_{L,X}^{\mathrm{lit},\sigma}(d,e)
 e(\sigma\sqrt{Xde})
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

No report proves the required fixed-literal cross-radical cancellation.
The round should therefore promote only the exact reduction, the strict
safe sectors, and the scoped obstruction facts above; retain every parent
and downstream exponent owner unchanged.

## 8. Artifacts and controls

This review used `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`,
`strategy/round181_m1_hard_top_high_squarefree_radical_strategy.md`, and
all three Round-181 reports.  The relevant graph statements for
`M9-M1-top-endpoint-transform`, `M9-M1-top-endpoint-signed-cone`,
`M9-M1-direct-hard-smooth-separate-one-third-minimax`,
`M9-M1-physical-one-count-assembly`, `Divisor-bound-elementary`, and the
prior product-fibre, B-process, canonical-Gram, and combined-cone scope
obstructions were checked against the starting hash.

All requested checks are analytic and pass with the qualifications stated
above: exact product fibres; unique squarefree decomposition; literal
support; low-\(s\) and large-\(t\) bounds; \((h,n)\mid t\); fixed-\(t\)
power summation; perfect-square and \(t=1\) controls; arbitrary-coefficient
and character-erasure controls; exact Möbius self-return; literal endpoint,
sign, and zero-extension retention; conditional hard-parent connector; and
downstream/exponent quarantine.  No numerical or external-source evidence
was used.
