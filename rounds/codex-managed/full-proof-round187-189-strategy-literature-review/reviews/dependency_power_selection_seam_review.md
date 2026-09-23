# Round 190 dependency, power, and selection seam review

- Campaign: `full-proof-round187-189-strategy-literature-review`
- Round: `190`
- Review seam: dependency graph, Round-189 normalization, final power ledger, and single-objective scope
- Starting graph SHA-256:
  `15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`
- Numerical theorem evidence: none
- Review verdict: **GREEN**

## 1. Result

**Seam-verification lemma.**  The conductor reconciliation is correct on
the dependency, normalization, power, and scope seams.

1. The authoritative graph has exactly the two lawful quarter routes stated
   in the full-graph report: the standard blockwise M9 route and the
   total-active GAR alternative.  The open owners and route-specific
   connectors are not conflated.
2. The Round-189 fast complement is retained with its exact lift and
   projective conditions, both orientations, every literal field, and one
   outer real part.  A hypothetical proof closes only the exact inherited
   original-\(t=1\) residual, not the complete hard-M1 parent.
3. For the zero-extended height sequence, the Abel identity used in
   (190.8) is endpoint-exact.  On
   \(J\le j_q(a,v)<2J\),
   \(|1-z_{\omega,v}|^{-1}\asymp q/J\) with absolute constants.
4. The proposed signed coboundary estimate

   \[
   |\mathscr J_{\kappa,u,m,q,a,J}^{\sigma}|
   \ll_{B,\varepsilon}H_Bm\kappa uX^\varepsilon
   \tag{R190.1}
   \]

   is sufficient for
   \(\Re\mathscr F_{Y,H_B}^{\sigma}\ll L^2X^\varepsilon\).
   The exact \(m^{-1}\) lift cancels the \(m\) in (R190.1); the dyadic
   \(J\)-sum, \(a\)-coefficient mass, \(mq\mid u\) ledger, and physical
   \((\kappa,u)\)-sum cost only fixed logarithmic factors.  No hidden
   \(Y/(H_Bm)\) power remains.
5. The reconciliation correctly rejects the blind report's positive total
   variation (R191-FB) as the *fresh* seam while retaining it as a valid
   sufficient benchmark.  The signed jump aggregate (R190.1), not the sum
   of individual variations, is the unique reconciled Round-191 attack.
6. All Round-190 conclusions are strategy/source evidence only.  No
   analytic estimate, parent, endpoint, bridge, source dependency, theorem,
   or exponent is promoted.

The appropriate review disposition is **GREEN**, with no repair to the
full-graph report or conductor reconciliation.

## 2. Exact statement and hypotheses

### 2.1 Lawful dependency routes

Let
\(\mathcal I=\{\mathrm{H1\!-\!H3},\mathrm H4,
\mathrm{R5\!-\!Full}\}\).  The standard route is

\[
\begin{aligned}
&\bigl(\mathrm{M1}_{\rm hard}\wedge
       \mathrm{M1}_{\rm smooth}\bigr)
 \xRightarrow{\rm proved\ Phys1}\mathrm{M9\!-\!M1},\\
&\mathrm{TOP}_{\rm M2}\wedge
  (\mathrm{BAL}_{\rm crit}\wedge\mathrm{BAL}_{\rm rest})
  \wedge\mathrm{UNBAL}
 \xRightarrow{\rm proved\ Phys2}\mathrm{M9\!-\!M2},\\
&\mathrm{M9\!-\!M1}\wedge\mathrm{M9\!-\!M2}
 \wedge\mathrm{M9\mbox{-}endpoint\mbox{-}uniformity}
 \Longrightarrow\mathrm M9,\\
&\mathcal I\wedge\mathrm M9
 \xRightarrow{\rm Conditional\mbox{-}bridge}
 \mathrm{GC\mbox{-}target}.
\end{aligned}
\tag{R190.std}
\]

The exact alternative is

\[
\begin{aligned}
&\mathrm{GAR}_{\rm low}\wedge\mathrm{GAR}_{\rm int}
 \xRightarrow{\rm proved\ radial\ assembly}\mathrm{GAR},\\
&\mathrm{GAR}
 \xRightarrow{\rm proved\ equivalence}\mathrm{M1}_{\rm total},\\
&\mathrm{TOP}_{\rm M2}\wedge
  (\mathrm{BAL}_{\rm crit}\wedge\mathrm{BAL}_{\rm rest})
  \wedge\mathrm{UNBAL}
 \xRightarrow{\rm proved\ Phys2}\mathrm{M9\!-\!M2},\\
&\mathcal I\wedge\mathrm{M1}_{\rm total}\wedge\mathrm{M9\!-\!M2}
 \xRightarrow{\rm GC\mbox{-}global\mbox{-}M1\mbox{-}alternative\mbox{-}bridge}
 \mathrm{GC\mbox{-}target}.
\end{aligned}
\tag{R190.alt}
\]

The graph statuses supporting these displays are: both physical assemblies,
the GAR radial interface, GAR radial one-count assembly, and GAR-to-total-
active equivalence are `proved_internal`; direct hard M1, direct smooth M1,
GAR, hard TOP, critical BAL, remaining-label BAL, UNBAL, M9--M1, M9--M2,
endpoint uniformity, M9, and the target are open; both final bridges are
`derived_under_assumptions`.  GAR has no edge to blockwise M9--M1 or M9.

### 2.2 Exact Round-189 complement and proposed seam

Put \(Q=H_B=\lfloor(\log(2X))^B\rfloor\).  On a nonempty dyadic
\(Y<h\le2Y\), \(Y>Q\), the exact fast domain is

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y,
\tag{R190.2}
\]

\[
 j_q(a,v)=|a\bar v_q|_q>
 T_Q=\min\!\left\{\frac{q-1}{2},
              \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\}.
\tag{R190.3}
\]

Here \(U,m,q\) are odd, \((a,q)=1\), and \(q\mid U\mid u\).  The lift is
unique and exact:

\[
 U=mq,\quad k=ma,\quad
 c_{mq}(ma)=m^{-1}c_q(a),\quad
 e(\epsilon_\omega k\bar vh/U)
 =e(\epsilon_\omega a\bar vh/q).
\tag{R190.4}
\]

For fixed admissible \((\kappa,u,m,q,a)\) and one fast dyadic band
\(J\le j_q(a,v)<2J\), let the exact zero-extended literal height sequence
be \(W_v(h)=W_{\kappa,u,mq,v,\omega}^{\sigma}(h)\), and define

\[
 \Delta^-W_v(h)=W_v(h)-W_v(h-1),\qquad
 z_{\omega,v}=e(\epsilon_\omega a\bar v_q/q).
\tag{R190.5}
\]

Then

\[
 \mathscr J_{\kappa,u,m,q,a,J}^{\sigma}
 =\sum_{\substack{\omega,v\ \mathrm{literal}\\
                   J\le j_q(a,v)<2J}}
 \frac{1}{1-z_{\omega,v}}
 \sum_h\Delta^-W_v(h)z_{\omega,v}^{h}.
\tag{R190.6}
\]

The single selected Round-191 objective remains the exact fast-complement
relation under one outer real part; (R190.1) is a proposed stronger
fixed-parameter sufficient seam.  All common-range differences, affine
births/deaths, masks, endpoints, orientations, phases, and zero extensions
must stay inside (R190.6).

## 3. Proof or derivation

### 3.1 Independent graph check

The file hash of `state/proof_obligations.yml` is exactly
`15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568`.
Direct graph inspection verifies the following decisive edges.

- `M9-M1-physical-one-count-assembly` depends on exactly the open hard and
  smooth direct-M1 analytic parents among its unresolved owners and implies
  M9--M1.
- `M9-M2-physical-one-count-assembly` depends on hard TOP, BAL, and UNBAL
  and implies M9--M2.  BAL separately depends on the critical double-far
  energy and the remaining-label owner.
- M9 is blocked by both M1 parents, all three M2 parents, and endpoint
  uniformity.  `Conditional-bridge` depends on M9.
- `M9-M1-global-angular-radial-estimate` is blocked by the lower-radial
  signed estimate.  Its proved equivalence implies only the alternative
  bridge, whose other live input is M9--M2.
- The Round-189 projective reduction is `proved_internal` but has no
  implication edge to its open small-\(t\) owner.  The small-\(t\) owner
  remains open and explicitly retains original \(t\ge2\) and near-resonant
  work.

This proves (R190.std)--(R190.alt) and the claimed owner quarantine.

### 3.2 Endpoint-exact Abel identity

Because \(W_v\) is finitely supported after zero extension, both sums below
are finite.  Reindexing without a boundary term gives

\[
\begin{aligned}
 \sum_h\Delta^-W_v(h)z^h
 &=\sum_hW_v(h)z^h-\sum_hW_v(h-1)z^h\\
 &=(1-z)\sum_hW_v(h)z^h.
\end{aligned}
\tag{R190.7}
\]

On the fast domain, \((a,q)=(v,q)=1\), so
\(a\bar v_q\not\equiv0\pmod q\); hence \(z\ne1\).  Division by
\(1-z\) is lawful and yields exactly (190.8), including both endpoint
birth/death jumps.  No endpoint remainder is omitted.

### 3.3 The \(q/J\) normalization

Let \(r\) be the centered residue of
\(\epsilon_\omega a\bar v_q\pmod q\).  Then
\(|r|=j_q(a,v)\) and, since \(q\) is odd,
\(1\le |r|\le(q-1)/2\).  Therefore

\[
 |1-z|=2\sin\!\left(\frac{\pi |r|}{q}\right).
\]

For \(0\le x\le\pi/2\), \(2x/\pi\le\sin x\le x\).  Thus

\[
 \frac{2|r|}{q}\ll |1-z|\ll\frac{|r|}{q}.
\]

Uniformly on \(J\le|r|<2J\), this is

\[
 \boxed{|1-z|^{-1}\asymp q/J.}
\tag{R190.8}
\]

The orientation sign does not alter the magnitude.  The estimate also
remains uniform at the largest band \(J\asymp q\).

### 3.4 Sufficiency and exact power ledger

Assume (R190.1).  For fixed
\((\kappa,u,m,q,a,J)\), multiply it by the exact Fourier lift weight:

\[
 \frac1m|c_q(a)|\,
 |\mathscr J_{\kappa,u,m,q,a,J}^{\sigma}|
 \ll Q\kappa u|c_q(a)|X^\varepsilon.
\tag{R190.9}
\]

This is the decisive cancellation: the \(m\) in the proposed signed seam
is cancelled exactly by \(m^{-1}\), before positive recombination.  There
is no \(Y\) on the right.

There are \(O(\log(2q))\) dyadic \(J\)-bands, and the accepted exact-
conductor coefficient mass is

\[
 \sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|c_q(a)|
 \ll\log(2q).
\tag{R190.10}
\]

Thus fixed \((\kappa,u,m,q)\) costs at most

\[
 Q\kappa u\log^2(2q)X^\varepsilon.
\tag{R190.11}
\]

Since \(U=mq\mid u\), the complete lift/conductor ledger is

\[
 \sum_{mq\mid u}1=\tau_3(u).
\tag{R190.12}
\]

Using the inherited physical support \(u\asymp L/\kappa\),

\[
\begin{aligned}
 &QX^\varepsilon
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log^2(2u)\\
 &\qquad\ll
 QL^2\log^{O(1)}(2L)X^\varepsilon
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\end{aligned}
\tag{R190.13}
\]

The final inequality uses fixed \(B\), the inherited live-shell bound
\(L\ll X^{1/4}\), and a fresh epsilon budget; only fixed logarithmic
factors are absorbed.  Summing the dyadic \(Y\)-blocks costs one more
logarithm.  Equations (R190.9)--(R190.13) prove that (R190.1) is sufficient
for the exact fast-complement target with no hidden positive power of
\(Y/(Qm)\).

For comparison, triangle inequality inside (R190.6) and (R190.8) gives the
positive sufficient gate

\[
 \sum_{\omega,v}\mathsf V(W_v)
 \ll \frac{Qm\kappa uJ}{q}X^\varepsilon.
\tag{R190.14}
\]

The available bound replaces \(Qm\) by \(Y\), so its exact deficit is
\(Y/(Qm)\), primitive \(Y/Q\).  The blind report's R191-FB is therefore a
valid sufficient inequality but cannot itself be called a signed fresh
seam.  The conductor reconciliation correctly makes (R190.1) the new seam
and retains (R190.14) only as a benchmark.

### 3.5 Strategy-only audit

The full-graph report labels (190.10) proposed strategy, limits a future
success to a subordinate exact-\(t=1\) result, and provides a stop rule.
The source report recommends no import and no analytic status change.  The
blind report recommends no state change.  The conductor reconciliation is
explicitly provisional before review and selects only a Round-191
objective.  None of these artifacts supplies a proof of (R190.1), creates
an implication edge, or changes the exponent ledger.

## 4. First doubtful or unproved step

The first doubtful step is exactly (R190.1).  The algebra after it is
complete, but no Round-190 report proves cancellation in the literal jump
family.  Height increments may change coprimality, squarefreeness, the
residual selector, anchors, affine ranges, profiles, floors, crossings,
Fejer factors, square-root phases, endpoints, and terminal zero extension.
The signed common-range and birth/death terms need not cancel merely because
the two orientations and projective band are aggregated.

The accepted pointwise information gives only the total-variation scale
with \(Y\) in place of \(Qm\).  The odd-prime slope-\(-2\) prefix also
rules out a coefficient-free uniform polylogarithmic centered-prefix
replacement.  Hence (R190.1) is a legitimate new analytic objective, not an
accepted lemma.  This is the exact boundary on which a Round-191 proof or
no-go result must stop.

## 5. Control tests and outcomes

| control | outcome |
|---|---|
| authoritative graph hash and edges | **PASS.** File hash is exact; standard and GAR routes, statuses, blockers, and implications agree with the reports. |
| both lawful quarter routes | **PASS.** GAR replaces only total active M1 and still requires complete M9--M2; no direct-M1/GAR hybrid is used. |
| exact open owners | **PASS.** Hard/smooth M1, GAR low survivor, hard TOP, both BAL scopes, UNBAL, endpoint, bridges, and target retain their graph statuses. |
| Round-189 fast-domain partition | **PASS.** (R190.2)--(R190.3) retain the exact complement; the saturated cutoff makes only that lift's fast sector empty. |
| one-outer-real-part scope | **PASS.** The physical objective retains one real part.  (R190.1) is clearly labelled a stronger fixed-parameter sufficient seam, not an equivalent relocation of the physical absolute value. |
| endpoint-exact Abel identity | **PASS.** Zero extension gives (R190.7) with all birth/death endpoints and no remainder; fast support guarantees \(z\ne1\). |
| \(|1-z|^{-1}\asymp q/J\) | **PASS.** Centered residue and elementary sine bounds give (R190.8), uniformly for both orientations and all fast bands. |
| exact \(m^{-1}\) lift | **PASS.** Unique \(U=mq,k=ma\) coordinates give (R190.4); (R190.9) cancels \(m\) before positivity. |
| coefficient and divisor ledger | **PASS.** Dyadic \(J\), \(\ell^1\) coefficient mass, \(\tau_3(u)\), and \((\kappa,u)\) summation yield only \(Q\log^{O(1)}L\). |
| no hidden \(Y/(H_Bm)\) power | **PASS.** (R190.13) is independent of \(Y\); dyadic-height assembly costs only a logarithm. |
| blind positive-BV distinction | **PASS after reconciliation.** R191-FB is sufficient but nonnegative; it is not the selected fresh seam.  The signed coboundary packet is. |
| literal coefficient and false unsigned control | **PASS at strategy scope.** The seam retains actual jumps; positive variation, arbitrary bounded coefficients, early absolute values, and separately absolutized orientations are explicitly rejected. |
| \(t=1\)/\(t\ge2\)/near-resonance ownership | **PASS.** Future fast success closes only the exact original-\(t=1\) residual; no hard-M1 parent is promoted. |
| source-import scope | **PASS.** The source report's conclusion is dated and corpus-scoped; it creates no theorem edge. |
| strategy-only and exponent quarantine | **PASS.** Internal \(1/3\), external \(0.3144831759740614\ldots\), and target \(1/4\) remain separate; no analytic state mutation is licensed. |
| single Round-191 objective | **PASS.** The reconciliation selects only the exact fast complement via (R190.1), with a stop rule and no in-round pivot. |

## 6. Dependencies and exact artifacts used

This review read or mechanically parsed exactly the requested context:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/full-proof-round187-189-strategy-literature-review/reports/full_graph_frontier_reconstruction.md`, SHA-256
  `acc925d2d3fd45d99847f6f9416086329daeee4d6003bb806e3ade327f887881`;
- `rounds/codex-managed/full-proof-round187-189-strategy-literature-review/reports/current_primary_literature_reassessment.md`, SHA-256
  `d96229160d7277b0f8e19c0a49035b79ce94edddb70c06f61a64f3aee5732725`;
- `rounds/codex-managed/full-proof-round187-189-strategy-literature-review/reports/blind_round191_frontier_selection.md`, SHA-256
  `9900f9c9a4310758cc5367a8ac077ac5aa8c85de81545bbc9d51dacbf4d0ad24`;
- `rounds/codex-managed/full-proof-round187-189-strategy-literature-review/reviews/conductor_round190_report_reconciliation.md`, SHA-256
  `4edb8ae8cbfe695486bafcffe67617cc4dbebd7d22f75d8d49bb092e361da060`.

No web search, numerical experiment, source import, sibling review, graph
edit, proof-draft edit, validation-matrix edit, or shared-state mutation was
used.  All power calculations are exact symbolic ledgers.

## 7. Recommended state effect

**Verdict: GREEN.**  Accept the conductor reconciliation on this seam.
Provisionally retain `strategy_frontier_retained` and select exactly the
Round-189 fast-complement relation, attacked through the joint literal
height-jump coboundary estimate (R190.1), as the Round-191 objective.

Preserve the following boundary in any State Patch or Round-191 brief:

1. (R190.1) is unproved and is a stronger sufficient seam for the exact
   one-real-part fast complement, not an accepted analytic statement.
2. The blind total-variation estimate remains only a positive sufficient
   benchmark; it must not be described as the fresh signed mechanism.
3. Stop if a proof takes total variation or another positive norm before the
   full \((h,v,\omega)\) jump aggregate, loses any literal field, invokes a
   uniform centered-prefix theorem, or restores a positive power of
   \(Y/(H_Bm)\).
4. A future GREEN analytic proof may promote at most the corresponding
   subordinate exact original-\(t=1\)-residual theorem after independent
   review.  It may not promote the complete small-\(t\) owner, hard or smooth
   M1, GAR, M9--M1, any M2 parent, endpoint uniformity, M9, a bridge, the
   quarter theorem, a source dependency, or an exponent.

No graph or shared-state change is recommended by this review itself.
