# Round 97 hostile audit: M2 assembly and graph hygiene

## 1. Result

**Result: the implication “canonical residual hard top \(\Rightarrow\)
full M9-M2” is false as an assembly claim.** The canonical theorem, even
if assumed, owns only the residual part of the unique physical
denominator profile with the jump at
\(d=y=\lfloor\sqrt X\rfloor\). It does not own either of the following
nonempty parts of the accepted residual set \(\mathcal U\):

- smooth top-scale bands with \(K\asymp L\), whose accepted gcd/Poisson
  reduction ends at the open signed quarter-packet estimate; or
- smooth bands with \(K\not\asymp L\), whose accepted Poisson reduction
  ends at the open \(M^{3/4}\) product-phase estimate.

This failure is visible before any delicate estimate. For example,
\((\delta,\ell)=(2/5,0)\) lies in \(\mathcal U\), is a smooth
unbalanced cell, and is not a hard-top cell. A smooth physical band
\(D=c\sqrt X\) with fixed \(0<c<1\) and
\((\delta,\ell)=(1/2,1/10)\) is a balanced residual cell but is again
not the unique hard band. Thus the canonical theorem leaves actual
physical cells unowned.

The strongest clean conditional assembly supported by the selected
context is:

\[
\boxed{\text{hard-top canonical theorem}
 +\text{smooth balanced packet bound}
 +\text{smooth unbalanced dual bound}
 \Longrightarrow \text{M9-M2},}
\]

provided the three families are first made into a disjoint physical
owner table and all estimates are uniform for the literal real-\(X\)
bands, floors, profiles, stars, signs, and support crossings. The two
smooth assumptions are route-relative minimal interfaces, not logically
necessary theorems: a different direct pointwise estimate on the same
smooth cells could replace either.

The authoritative graph also fails hostile hygiene in four exact ways.

- It has the direct dependency cycle
  `M9-M2` \(\leftrightarrow\) `M9-near-collision-taxonomy`.
- It records partial owners and reductions as directly implying full
  `M9-M2`.
- It has no open node for either outside smooth estimate: the nodes
  `M9-M2-smooth-dual-three-quarter-equivalence` and
  `M9-M2-smooth-small-gcd-quarter-packet` are proved **reductions**, not
  the estimates to which they reduce.
- `M9-endpoint-uniformity` does not list the outside smooth packets among
  its blockers.

Therefore no M9-M2, endpoint-uniformity, M9, M9-M1, or exponent status is
licensed to change in this round.

## 2. Exact statement and hypotheses

Let the exact telescoping denominator partition have three physical
tags:

\[
\mathsf{Bot},\qquad \mathsf{Hard},\qquad \mathsf{Sm}.
\]

\(\mathsf{Bot}\) is the inactive remainder \(d\ll X^{1/4}\);
\(\mathsf{Hard}\) is the unique profile with the included endpoint
\(d=y\); and every \(\mathsf{Sm}\) profile is a full fixed smooth
rescaling supported away from that jump. For an active band,

\[
H_D=\lfloor DX^{-1/4}\rfloor,\qquad
D=X^\delta,\qquad L=X^\ell,
\]

and the exact active triangle and residual set are

\[
\Omega=\left\{(\delta,\ell):
{1\over4}\le\delta\le{1\over2},\
0\le\ell\le\delta-{1\over4}\right\},
\]

\[
\mathcal U=
\left\{(\delta,\ell)\in\Omega:
0\le\ell<\delta-{1\over4},\
178\ell+1638\delta>463\right\}
\setminus\{(1/2,0)\}.
\tag{2.1}
\]

For a smooth band put

\[
K={XL\over D^2},\qquad M=LK.
\tag{2.2}
\]

Call a literal smooth cell *balanced* only when it meets the exact
uniform hypotheses of the accepted balanced reduction, in particular
\(K\asymp L\) with a uniformly smooth two-variable symbol. Call the
remaining smooth cells in \(\mathcal U\) *unbalanced*. This definition
is intentionally physical: the exponent coordinate alone cannot detect
the hard cutoff or a uniform comparability constant.

Assume, conditionally, the following three estimates.

- **HB:** on every \(\mathsf{Hard}\cap\mathcal U\) frequency block, the
  canonical residual theorem, together with its already accepted
  internal owners, gives
  \(\mathcal T_{\rm end,L}\ll_\varepsilon
  L^{3/2}X^\varepsilon\).
- **SB:** on every \(\mathsf{Sm}\cap\mathcal U\) balanced block, the
  remaining signed packet obeys

  \[
  \left|\sum_GG\mathscr P_G\right|
  \ll_\varepsilon L^{3/2}X^\varepsilon.
  \tag{2.3}
  \]

- **SU:** on every \(\mathsf{Sm}\cap\mathcal U\) unbalanced block, the
  exact smooth dual sum obeys

  \[
  \mathcal T_{L,K}\ll_\varepsilon M^{3/4}X^\varepsilon.
  \tag{2.4}
  \]

Every statement retains both quarter shifts, \(\chi_4(h)\), the actual
\(1/h\) taper, both frequency signs, profiles, floors, endpoint stars,
and the literal real-\(X\) support.

With the owner priority shown below, HB+SB+SU are sufficient for the
full main-polynomial M2 assembly. The priority is part of the statement;
without it several rows overlap.

| Priority | Literal physical set | Unique owner or status |
|---:|---|---|
| 1 | \(d\ll X^{1/4}\), before Fourier expansion | bottom remainder, \(O(X^{1/4})\) |
| 2 | Fejer residual on every active band | `R5-Full`, globally once |
| 3 | main polynomial, \(L\asymp H_D\) | terminal T2S |
| 4 | remaining main polynomial at \((1/2,0)\) | full second-derivative menu |
| 5 | remaining main polynomial with \(178\ell+1638\delta\le463\) | audited TTY wedge |
| 6 | \(\mathsf{Hard}\cap\mathcal U\) | HB, including its disjoint internal top owners |
| 7 | balanced \(\mathsf{Sm}\cap\mathcal U\) | proved preliminary sectors plus open SB |
| 8 | unbalanced \(\mathsf{Sm}\cap\mathcal U\) | smooth Poisson equivalence plus open SU |

Smooth Poisson \(O_W(1)\) support-crossing terms belong to rows 7--8
once. The one-sided principal endpoint, half-weight, principal-value
renormalization, and stationary errors belong to row 6 once. They are
not ninth analytic packets.

## 3. Proof or derivation

The two witness cells prove insufficiency of HB alone. First,
\((2/5,0)\in\Omega\), it is nonterminal because
\(0<2/5-1/4\), and

\[
178\cdot0+1638\cdot{2\over5}=655.2>463.
\]

It is not \((1/2,0)\), hence lies in \(\mathcal U\). A physical band
\(D\asymp X^{2/5}\) is smooth, and (2.2) gives
\(K/L=X/D^2\asymp X^{1/5}\), so it is unbalanced. HB has disjoint
physical support.

Second, take a fixed smooth interior band \(D=c\sqrt X\), away from the
unique endpoint profile, and \(L=X^{1/10}\). It is nonterminal,
not the isolated point, and the TTY inequality fails strongly:

\[
178\cdot{1\over10}+1638\cdot{1\over2}=836.8>463.
\]

Here \(K/L=X/D^2=c^{-2}\), so this is a balanced smooth residual cell.
Again HB has disjoint physical support.

This also proves why exponent-scale labels are inadequate. For the
literal dyadic bands

\[
D_j=2^{-j}\sqrt X,\qquad
\delta_j={1\over2}-{j\log2\over\log X},\qquad
{K\over L}=4^j.
\tag{3.1}
\]

Every fixed \(j\) has exponent \(\delta_j=1/2+o(1)\), but only one
physical profile is hard. The others are smooth. If \(j\) grows slowly,
the exponent still looks top-scale while \(K/L\) ceases to be uniformly
bounded. Therefore neither “\(\delta=1/2\)” nor
“\(\delta=1/2+o(1)\)” is an owner.

The table is disjoint by construction. Row 1 is removed before the H4
frequency expansion. On active bands, row 2 is the Fejer remainder and
all later rows are the Vaaler main polynomial. Rows 3--5 are removed in
priority order, resolving the real overlaps between the terminal line
and the TTY wedge. Their exact complement is (2.1). The physical tag then
splits that complement into the unique hard band and all smooth bands;
the exact hypotheses \(K\asymp L\) versus its complement split the smooth
part.

Under HB, row 6 is target-sized. Under SB, the accepted exact-square,
near-square, and large-gcd preliminary owners plus (2.3) close row 7.
Under SU, the exact identity

\[
\mathcal B^+_{L,W}
=-{e(1/8)\over2\pi}X^{1/4}M^{-3/4}
\mathcal T_{L,K}+O_W(1)
\]

and (2.4) close row 8. The negative-frequency term is retained by
conjugation with the actual real-even coefficient. There are only
logarithmically many physical \(D\)-bands and dyadic \(L\)-blocks, so
the main terms assemble with an \(X^\varepsilon\) allowance after
shrinking the per-block epsilon. The bottom and `R5-Full` statements
already include their own global assembly and must not receive a second
dyadic sum.

For the hard band, the hostile endpoint audit proves that the stationary
point remains uniformly away from the endpoint width. It also proves
that the included endpoint contributes a plus half-weight and that the
boundary Fourier series must be symmetrically renormalized. The
principal endpoint is \(O(1)\) on each positive dyadic \(L\)-block,
sharp \(O(\log H)\) over the whole positive height, and \(O(1)\) for the
actual two-sided real-even total. Hence these terms are target-safe but
cannot be silently replaced by a full-height positive \(O(1)\).

The graph defects follow directly from the authoritative node fields.
`M9-M2` lists `M9-near-collision-taxonomy` as a dependency, while the
taxonomy lists `M9-M2` as a dependency and implication. This is a
literal two-node cycle. Moreover T2S, the phase-diagram reduction, the
TTY wedge, and the balanced small-gcd reduction each have a direct
`implies: M9-M2` edge despite owning only a proper subset or giving only
a reduction. The smooth dual and balanced nodes explicitly say their
target estimates remain open, yet both nodes have proved status because
the transformations are proved. Treating that status as an estimate
would be circular.

Finally, the fourth-moment taxonomy, weighted near-collision estimate,
denominator-paired fourth-moment bound, local fourth moment, and
average-to-pointwise upgrade are one alternative route to pointwise
M9-M2. None is used in the disjoint HB+SB+SU implication. Conversely,
the algebraic character identity is already proved in
`M9-M2-beta-algebra`; the open `M9-M2-character-factor` node is a
guardrail saying that the character must be retained, not an additional
analytic estimate.

## 4. First doubtful or unproved step

The first formal gap is an exact physical definition of the
balanced/unbalanced cut that is uniform in the band index \(j\), followed
by a proof that it partitions every smooth cell of \(\mathcal U\).
The selected context gives the exponent diagram, the smooth dual
identity, and a uniformly balanced reduction, but it does not specify
where a growing \(K/L=4^j\) leaves the uniform balanced symbol class.
Calling all \(\delta=1/2+o(1)\) cells balanced would be false by (3.1);
calling only the hard band top-scale would omit fixed-\(j\) smooth bands.

After that formal seam, the first analytic gaps are exactly SB and SU.
Neither is proved:

- the accepted balanced node stops at the outside-absolute signed
  aggregate (2.3), and its own statement excludes uncontrolled sharp gcd
  boundaries and the hard denominator edge;
- the accepted smooth Poisson node proves only equivalence between the
  original block and (2.4), not (2.4).

The real-\(X\) version must hold for every literal
\(D_j\), \(H_D=\lfloor DX^{-1/4}\rfloor\), dyadic odd \(L\), and every
support entry/exit. A bound only at the exponent point
\((\delta,\ell)\), or only for an asymptotic continuum endpoint, is not
the required statement.

## 5. Required control tests and source/graph outcomes

- **Active triangle and \(\mathcal U\): pass.** Formula (2.1) is used
  after terminal, isolated-point, and TTY owners are removed in that
  order.
- **Hard top versus smooth top scale: fail without correction.** Equation
  (3.1) proves that exponent scale does not identify the unique hard
  profile. The physical jump tag is mandatory.
- **Bottom and R5: pass only with separate scopes.** Bottom owns the
  inactive denominator remainder before Fourier expansion. `R5-Full`
  owns the Fejer residual on active bands. Neither is applied to the
  other's support, and neither is resummed after its accepted global
  assembly.
- **Terminal T2S, second derivative, and TTY: pass with priority.** These
  regions overlap at boundary cells. The table assigns T2S first, the
  isolated point second, and TTY only on the remaining main cells.
- **Smooth Poisson and support crossings: pass as a reduction only.**
  Smooth Poisson applies to full interior profiles and retains its
  \(O_W(1)\), zero/nonstationary modes, \(K\asymp1\), and support
  crossings. It is forbidden on the hard profile.
- **Hard one-sided boundary: pass with exact normalization.** The plus
  half endpoint, symmetric principal value, actual
  \(y=\lfloor\sqrt X\rfloor\), and positive-versus-two-sided endpoint
  scopes are retained. Boundary control does not prove the stationary
  signed cone.
- **Character, shifts, profiles, floors, stars, and signs: pass as
  mandatory data.** The two shifts project to odd \(h\) and reinforce
  rather than cancel. No row permits deleting \(\chi_4\), replacing the
  actual profiles by arbitrary coefficients, or omitting either sign.
- **Dyadic one count: conditional pass.** The priority table is disjoint,
  but the balanced/unbalanced physical cutoff must still be frozen
  exactly. Transform errors are attached to their parent row, not made
  duplicate owners.
- **Real-\(X\) endpoint uniformity: open.** The hard boundary
  infrastructure is uniform over square intervals. The two outside
  analytic estimates and their moving support constants remain open;
  exponent notation alone does not close this seam.
- **Reduction versus estimate: graph failure.** The proved smooth dual
  and quarter-packet nodes are reductions. Their desired estimates need
  separate open nodes before any mechanical implication to M9-M2.
- **Legacy route dependency: graph failure.** The exact M9-M2/taxonomy
  cycle must be broken. Near-collision and fourth-moment nodes are
  alternative route nodes, not mandatory dependencies of the direct
  physical assembly. The character-factor node is a proved algebraic
  guardrail in substance, not an open analytic blocker.
- **Downstream and exponent scope: pass with no promotion.** HB+SB+SU
  would prove only M9-M2. M9-M1 and full endpoint uniformity remain
  separate; hence M9 and the quarter target do not follow. No internal
  or external global exponent changes.
- **Primary-source map: no new source invoked.** The only external input
  used in the owner table is the already source-audited TTY exponent pair
  under the normalized discrete-BV hypothesis, which the accepted dyadic
  profile node verifies. H4/Vaaler is already source-audited. Li--Yang
  and Xiao are guardrails only and are not used. No new source claim
  requires web or primary-text import in this audit.

## 6. Dependencies and exact artifacts used

Isolation disclosure: I am a **reused, non-isolated hostile agent**. I
previously worked on Round 96 and was exposed to its selected context and
one Round-96 report. This is acceptable for the present hostile role but
means this report is not blind evidence. No sibling Round-97 report was
read. Every Round-97 finding above is supported by the selected files
below rather than by an unlisted Round-96 artifact.

Procedural instructions came from:

- `rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/briefs/m2_assembly_hostile_hygiene_audit.md`;
- `rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/plan.json`.

The exact selected mathematical context was:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/derivation_packet.md`;
- `rounds/codex-managed/m9-frequency-phase-diagram/synthesis.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/synthesis.md`;
- `rounds/codex-managed/m9-top-endpoint-transform/reports/endpoint_transform_hostile_audit.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/reviews/conductor_round92_source_and_graph_hygiene.md`;
- `strategy/conductor_0817_full_proof_strategy.md`.

Within the graph, the decisive nodes were `R5-Full`,
`M9-M2-dyadic-weight-nondegeneracy`,
`M9-M2-top-frequency-two-shift-T2S`,
`M9-M2-TTY-exponent-pair-wedge`,
`M9-M2-frequency-phase-diagram-R5`,
`M9-M2-smooth-dual-three-quarter-equivalence`,
`M9-M2-smooth-small-gcd-quarter-packet`,
`M9-M2-top-endpoint-transform`,
`M9-M2-top-endpoint-signed-cone`,
`M9-M2-top-endpoint-density-discrepancy-energy`,
`M9-near-collision-taxonomy`, `M9-M2-character-factor`,
`M9-endpoint-uniformity`, `M9-M2`, and `M9`.

No computation, sibling report, new external theorem, or unselected
source was used.

## 7. Recommended state effect

**Reject** any implication from the canonical hard-top theorem alone to
`M9-M2`. Retain the canonical theorem, signed cone, M9-M2, endpoint
uniformity, M9, and the quarter target as open.

After independent seam review, the conductor may promote a conditional
physical one-count assembly lemma with the priority table in Section 2.
Before doing so, freeze a uniform physical balanced/unbalanced cut and
the exact owner of every support-crossing term.

Repair the graph without analytic promotion:

- create separate open estimate nodes for the smooth balanced signed
  quarter packet (2.3) and the smooth unbalanced dual target (2.4);
- create a proved reduction/assembly node whose dependencies are the
  direct owners plus HB, SB, and SU, and make that node the sole forward
  interface to `M9-M2`;
- remove the direct dependency cycle between `M9-M2` and
  `M9-near-collision-taxonomy`, routing the taxonomy, local fourth moment,
  near-collision, and average-to-pointwise nodes as an alternative
  fourth-moment branch;
- replace direct `implies: M9-M2` edges from T2S, TTY, the phase diagram,
  and the balanced reduction by scoped owner edges into the assembly
  node;
- reclassify `M9-M2-character-factor` as an accepted invariant/guardrail
  backed by `M9-M2-beta-algebra`, or at minimum remove it as an open
  analytic blocker while retaining its no-erasure rule;
- add the two smooth outside-packet nodes to the M2 and endpoint-uniformity
  blocker lists.

Do not edit shared state from this report, do not infer M9-M1, and do not
start another round.
