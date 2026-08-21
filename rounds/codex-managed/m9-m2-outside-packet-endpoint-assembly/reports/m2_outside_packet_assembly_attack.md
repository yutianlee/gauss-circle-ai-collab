# M2 outside-packet assembly attack

Campaign: m9-m2-outside-packet-endpoint-assembly
Task: m2_outside_packet_assembly_attack
Role: discovery / assembly constructor
Access: selected context; no sibling Round-97 report used
Starting graph SHA-256: a2b3387c43d467aaa2223ecb31807cd09cf0d429dcebd9b7bde0db6f14cf3657
Generated: 2026-08-17T14:16:56.6989994+08:00
Claimant status: candidate reduction and no-go report; no state-edit authority

## 1. Result

The canonical residual hard-top theorem does **not** by itself imply
M9-M2.  After every accepted owner is applied once, the literal residual
main blocks split into three disjoint families:

\[
\mathcal U_{\rm hard},\qquad
\mathcal U_{\rm sm,bal},\qquad
\mathcal U_{\rm sm,unbal}.
\]

The canonical theorem closes only \(\mathcal U_{\rm hard}\).  The two
independent outside families are:

\[
\boxed{\left|\sum_GG\mathscr P_G\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon}
\tag{BAL}
\]

for every residual **smooth balanced** physical block, and

\[
\boxed{\mathcal T_{L,K}
 \ll_\varepsilon (LK)^{3/4}X^\varepsilon,\qquad
 K={XL\over D^2}}
\tag{UNBAL}
\]

for every residual **smooth unbalanced** physical block, with the actual
signed symbols in both displays.  Together with the canonical hard-top
bound, (BAL) and (UNBAL) are sufficient for the full literal
one-block-at-a-time M9-M2 target.  Relative to the accepted exact
transforms and the frozen requirement that every literal block be bounded,
they are also the minimal remaining packet interfaces: no accepted owner
contains either residual.

The balanced quarter packet covers only the fixed-comparability
top-scale slice \(K\asymp L\), equivalently \(D\asymp\sqrt X\).  It does
not cover the full smooth residual corridor.  In particular,
\((D,L)\asymp(X^{1/3},1)\) lies in the residual corridor and has
\(K/L\asymp X^{1/3}\), so it is genuinely unbalanced.

This is a conditional assembly lemma and a rigorous owner-table no-go,
not a proof of (BAL), (UNBAL), the canonical hard-top theorem, M9-M2,
M9-M1, M9, or the quarter exponent.

## 2. Exact statement and hypotheses

Let \(X\ge X_0\) be real and

\[
y=\lfloor\sqrt X\rfloor,\qquad
H_D=\lfloor DX^{-1/4}\rfloor.
\]

Use the accepted exact telescoping denominator partition: one bottom
remainder supported on \(d\ll X^{1/4}\), active profiles \(w_D\) with
\(D\ge X^{1/4}\), exactly one hard profile containing the physical cutoff
\(d\le y\), and otherwise full smooth interior profiles.  Decompose each
active Vaaler main polynomial using the accepted fixed dyadic partition in
odd frequency magnitude \(1\le |h|\le H_D\).  A labeled main block is

\[
B_2(D,L;X)
=\sum_d w_D(d)
 \sum_{0<|h|\le H_D}v_L(h)\,
 \beta_{h,H_D}\,e\!\left({hX\over4d}\right),
\]

where

\[
\beta_{h,H}
=\alpha_{h,H}\bigl(e(h/4)-e(3h/4)\bigr)
=-{\Phi(|h|/(H+1))\chi_4(|h|)
       \mathbf 1_{h\ {\rm odd}}\over\pi|h|}.
\]

Thus both quarter shifts, the odd-frequency projector, the exact
\(\chi_4(h)\) sign, the \(1/h\) taper, both frequency signs, the height
floor, the physical profiles, all endpoint stars, and the real-\(X\)
data are part of the object.  A positive-frequency transform and its
negative-frequency conjugate are counted separately before the final
real-even recombination.

Put

\[
D=X^\delta,\qquad L=X^\ell,\qquad
\Omega=\left\{(\delta,\ell):
 {1\over4}\le\delta\le{1\over2},\
 0\le\ell\le\delta-{1\over4}\right\}.
\]

At power scale, the accepted terminal, second-derivative, and TTY owners
leave exactly

\[
\mathcal U=
\left\{(\delta,\ell)\in\Omega:
0\le\ell<\delta-\frac14,\
178\ell+1638\delta>463\right\}
\setminus\left\{\left(\frac12,0\right)\right\}.
\tag{2.1}
\]

For the literal finite-\(X\) table, owners are applied in the following
priority order: terminal T2S; then the full second-derivative estimate;
then TTY; then the residual.  Equivalently, the physical tests are made
with the accepted bounds

\[
1+{D\over L},\qquad
1+\left({LX\over D}\right)^{1/2}
  +{D^{3/2}\over(LX)^{1/2}},\qquad
X^{89/1282}L^{89/1282}D^{819/1282},
\tag{2.2}
\]

and a block is passed to the next owner only if the preceding displayed
bound is not target-sized.  The power shadow of this literal rule is
exactly (2.1); fixed rescalings, height floors, and boundary labels cost
only the already allowed \(X^\varepsilon\).

For a smooth residual block put

\[
K={XL\over D^2},\qquad M=LK,\qquad {K\over L}={X\over D^2}.
\]

Freeze the same fixed comparability constants used by the accepted
balanced-symbol reduction.  A block is balanced when \(K\asymp L\)
within those constants; boundary ratio labels are assigned to the
balanced side once.  Every other smooth label is unbalanced.  Since
\(D\le\sqrt X\), the latter case is \(K\gg L\), not \(K\ll L\).

Assume, uniformly in real \(X\), all physical labels, and both signs:

- **(TOP)** For every hard-top residual frequency label,
  \[
  \sum_{A,D_{\rm ray},K_{\rm rec},G,R}
  |\mathfrak Q_{A,D_{\rm ray},K_{\rm rec},G,R}|
  \ll_\varepsilon L^2X^\varepsilon,
  \]
  with the complete actual coefficient, density mode, discrepancy modes,
  collars, floors, stars, orientations, and owner masks.

- **(BAL)** For every smooth balanced residual label, the accepted fixed
  smooth gcd partition satisfies the signed outside-absolute estimate
  displayed in Section 1.  The absolute value is outside the \(G\)-sum;
  the stronger and unassumed quantity
  \(\sum_GG|\mathscr P_G|\) is not substituted.

- **(UNBAL)** For every smooth unbalanced residual label, the exact
  product-phase transform with its actual slanted symbol satisfies the
  display in Section 1.

Then every literal \(B_2(D,L;X)\) is
\(O_\varepsilon(X^{1/4+\varepsilon})\), uniformly over the active
triangle, and hence the exact dyadic assembly proves M9-M2.  “Minimal”
here means minimal for this frozen blockwise transform-and-owner
architecture; an entirely different proof that cancels distinct physical
packets against one another is not ruled out.

## 3. Proof or derivation

The literal owner table is as follows.  Each row receives a labeled
partition component only after all earlier rows have declined it.

| Physical piece | Exact cell or object | Unique owner | Status at the quarter scale |
|---|---|---|---|
| Bottom denominator remainder | \(d\ll X^{1/4}\), before any Fourier expansion | accepted bottom owner | \(O(X^{1/4})\) |
| Vaaler Fejer residual | every active \(D\), including the hard top; both shifted legs and integer jumps | R5-Full | \(O_\varepsilon(X^{1/4+\varepsilon})\) pointwise |
| Active M2 main block | terminal frequency \(L\asymp H_D\) | two-shift T2S | accepted |
| Remaining active main block | the target-sized part of the full second-derivative bound in (2.2), whose power cell is \((1/2,0)\) | second-derivative owner | accepted |
| Remaining active main block | \(L^{178}D^{1638}\le X^{463}\), up to the harmless boundary \(X^\varepsilon\) | audited TTY owner | accepted |
| Residual main block, hard physical profile | \((\delta,\ell)\in\mathcal U\) and \(d\le y\) lies in the unique nonsmooth top profile | hard one-sided transform, its prior owners, then (TOP) | conditional |
| Residual main block, smooth balanced profile | \((\delta,\ell)\in\mathcal U\), \(K\asymp L\) | smooth transform, preliminary balanced owners, then (BAL) | open outside packet |
| Residual main block, smooth unbalanced profile | \((\delta,\ell)\in\mathcal U\), \(K\not\asymp L\) | smooth transform errors, then (UNBAL) | open outside packet |

This table is exhaustive.  The first two rows partition the original
physical reduction into the unexpanded bottom, the main Vaaler polynomial,
and the Fejer residual.  Within the main polynomial, the first three
analytic owners have complement (2.1).  The physical profile is then
either the unique hard top or smooth.  Finally \(K/L=X/D^2\) places every
smooth residual label in exactly one of the fixed balanced or unbalanced
ratio classes.

The hard row itself has the following one-count refinement.

| Hard-top transformed term | Owner |
|---|---|
| Included endpoint \(E_h(X)=e(hX/(4y))/(1-e(hX/(4y^2)))\), symmetric endpoint tails, nonstationary remainder, and transform errors | accepted one-sided endpoint transform |
| Energy diagonal, fixed physical collars, original Poisson zero and positive modes, equality modes, wrong-sign tails, entry/exit errors, primitive square rays, exact nonsquare centres, positive-safe blocks, and transformation error | \(\mathcal E_{\mathrm{owned},L}\) in the accepted canonical reduction |
| Successive residual complement with density and discrepancy still coupled | the \(\mathfrak Q\)-sum in (TOP) |

Consequently

\[
\mathcal E_L^\top
=\mathcal E_{\mathrm{owned},L}
+2\Re\sum_{A,D_{\rm ray},K_{\rm rec},G,R}
 \mathfrak Q_{A,D_{\rm ray},K_{\rm rec},G,R}
\ll_\varepsilon L^2X^\varepsilon.
\]

The exact transposed-row Cauchy bridge gives

\[
|\mathcal T_{\mathrm{end},L}|^2
\ll L\mathcal E_L^\top,
\qquad
\mathcal T_{\mathrm{end},L}
\ll_\varepsilon L^{3/2}X^\varepsilon.
\]

The accepted one-sided transform, including its boundary and
\(O(\log^2 H_D)\) weighted error, then gives the target for the hard
physical block.  Nothing in this argument mentions a smooth \(w_D\).

For a smooth profile, exact Poisson and stationary phase give, separately
for the positive sign,

\[
\mathcal B^+_{L,W}
=-{e(1/8)\over2\pi}X^{1/4}M^{-3/4}
 \mathcal T_{L,K}+O_W(1).
\tag{3.1}
\]

The zero and nonstationary modes, support crossings, and stationary
transition errors belong only to the accepted transform-error owner.
The negative sign is the corresponding exact conjugate and has the same
bound.

If \(K\not\asymp L\), (UNBAL) inserted into (3.1) immediately yields

\[
\mathcal B^\pm_{L,W}
\ll_\varepsilon X^{1/4+\varepsilon}.
\]

If \(K\asymp L\), then \(M^{3/4}\asymp L^{3/2}\).  The accepted balanced
reduction first owns exact squares, \(X^{-1/2}\)-scale near-squares, and
the large-gcd sector \(g\ge L^{1/2}\) at or below \(L^{3/2}X^\varepsilon\).
On the remaining fixed smooth gcd partition,

\[
\mathcal T_G={G\over2i}\mathscr P_G.
\]

Therefore (BAL), with its single outer absolute value, gives the remaining
small-gcd signed sum at the same \(L^{3/2}\) scale.  Hence
\(\mathcal T_{L,K}\ll_\varepsilon M^{3/4}X^\varepsilon\), and (3.1)
again gives the physical target.  No sharp gcd cutoff or unowned
\(1/\xi\)-tail is introduced.

The distinction between the two smooth rows is substantive.  A fixed
smooth band just below the hard profile can have

\[
D\asymp c\sqrt X,\qquad L\asymp X^{1/8},\qquad
{K\over L}\asymp c^{-2},
\]

with fixed \(0<c<1\).  Its power cell is in \(\mathcal U\), it is
balanced, and it is not the hard top.  By contrast,

\[
D\asymp X^{1/3},\qquad L\asymp1,\qquad
{K\over L}\asymp X^{1/3}
\]

also lies in \(\mathcal U\), because \(1638/3>463\), but is unbalanced.
The balanced reduction has both product variables on the \(L\)-scale and
does not apply to this \(L\times K\) rectangle.  A band with the same
limiting exponent \(\delta=1/2\) but with \(X/D^2\) escaping the fixed
comparability constants is likewise unbalanced: physical balance, not
the exponent label alone, is the owner test.

Finally, the number of physical \(D\)-labels and dyadic \(L\)-labels is
\(O(\log X)\) in each variable.  The fixed signs, shifts, profiles, and
boundary orientations add only constant multiplicity.  Applying every
owner with \(\varepsilon/3\) and summing the
\(O(\log^2 X)\) labeled pieces proves the asserted
\(O_\varepsilon(X^{1/4+\varepsilon})\) assembly.  The partition identity,
not support disjointness of overlapping smooth cutoffs, supplies one
count: every labeled partition component occurs once, and its raw and
transformed forms are never added as two contributions.

The canonical theorem alone fails the assembly test because its premise
contains only the last row of the hard-top refinement.  It supplies no
inequality for either smooth witness above.  Formally, after all accepted
identities are frozen, the hard \(\mathfrak Q\)-family and the two smooth
families are distinct coordinates of the direct-sum packet ledger; an
inequality on the hard coordinate cannot bound either smooth coordinate
without an additional relation.  This is a logical non-implication of
the stated hypotheses, not a lower bound for the actual smooth sum.

## 4. First doubtful or unproved step

Even after granting (TOP), the first unproved seam appears at the first
smooth top-scale residual band: the accepted gcd calculation proves only
the identity reducing its small-gcd remainder to
\(\sum_GG\mathscr P_G\).  It does **not** prove (BAL).  The first doubtful
inference would be to read the proved reduction node
M9-M2-smooth-small-gcd-quarter-packet as though its displayed target were
already an estimate.

(UNBAL) is a second, logically independent unproved seam rather than a
consequence of (BAL).  The exact Poisson formula proves equivalence between
the raw smooth block target and the \(M^{3/4}\) product-phase target; it
does not estimate the product-phase sum.  The balanced gcd argument cannot
be extended to \(K/L\to\infty\) from the selected evidence.

Before the conditional assumption is granted, (TOP) is itself open:
Round 96 leaves the complete fixed-\(a\), density-discrepancy coupled
actual Gram as its first strict survivor.  That Gram is a possible way to
prove (TOP), not an extra outside-packet dependency once (TOP) is assumed.

No source, computation, or algebra in the selected context proves any of
these three inequalities.  The report therefore stops at the sharp
conditional assembly and does not silently import an open Gram,
near-collision estimate, local fourth moment, or product-phase estimate.

## 5. Required control test and outcome

No numerical experiment was used; every control was an exact
algebraic/owner test.

| Required control | Outcome |
|---|---|
| Active triangle and residual \(\mathcal U\) | Pass: the priority complement of T2S, the full second-derivative point, and TTY is exactly (2.1). |
| Hard top versus smooth top scale | Pass: the hard owner is selected by the unique physical cutoff profile, not by \(\delta=1/2\); \(D\asymp c\sqrt X\) gives an explicit smooth balanced survivor. |
| Bottom and R5 owners | Pass: the bottom is never Fourier-expanded, while R5 owns only active Fejer residuals, including the hard top. |
| Terminal T2S and TTY wedge | Pass: terminal labels go to T2S first; TTY owns only the remaining labels satisfying \(L^{178}D^{1638}\le X^{463}\).  No overlap is counted twice. |
| Smooth Poisson and support crossings | Pass: only full smooth interior profiles are transformed; zero/nonstationary modes, support crossings, \(K\asymp1\) transitions, and transform errors stay with the accepted transform owner. |
| Hard one-sided boundary | Pass: \(E_h(X)\), its full endpoint weight, symmetric tail convention, and the \(y=\lfloor\sqrt X\rfloor\) separation are outside the canonical residual \(\mathfrak Q\)-sum and already target-safe. |
| \(\chi_4\), two shifts, profiles, floors, and stars | Pass: the literal \(\beta_{h,H}\) is displayed, both signs are retained, and (TOP), (BAL), and (UNBAL) are stated only for the actual symbols. |
| Dyadic one count | Pass: bottom/main/R5, analytic owner priority, physical hard/smooth type, and balanced/unbalanced ratio form successive disjoint owner decisions. |
| Real-\(X\) endpoint uniformity | Conditional pass: all three open packet hypotheses are explicitly uniform in real \(X\); the accepted owners retain \(y\), \(q=X/y^2\), height floors, and endpoint stars.  Without that uniformity the theorem is not asserted. |
| Reduction versus estimate | Pass: smooth Poisson, balanced gcd decomposition, endpoint transform, and hard energy decomposition are labeled reductions; only the accepted baseline bounds and the three explicit hypotheses are estimates. |
| Legacy-route dependency | Pass: character normalization is retained, while near-collision, fourth-moment, global-moment, and average-to-pointwise nodes are not used in any implication arrow of this proof. |
| Downstream and exponent scope | Pass: the conclusion is M2-only and conditional.  M9-M1, global M9 endpoint uniformity, M9, the conditional bridge, and the quarter target do not follow.  The existing global exponent ledger is unchanged. |

The two witness cells also provide the decisive falsification control:
removing (BAL) leaves a smooth balanced residual label with no owner, and
removing (UNBAL) leaves the \((1/3,0)\) smooth residual label with no owner.
Removing (TOP) similarly leaves the hard residual cone.  Thus none of the
three rows is redundant in this owner architecture.

## 6. Dependencies and exact artifacts used

The genuine logical inputs to the conditional assembly are:

- H4 coefficient normalization and the accepted exact dyadic profile;
- the bottom owner and R5-Full;
- the terminal T2S estimate, full second-derivative menu, and audited TTY
  wedge;
- the smooth Poisson equivalence and its support-crossing/error control;
- the balanced smooth preliminary-sector and gcd reduction;
- the one-sided hard endpoint transform and exact row-to-energy
  decomposition;
- the three explicitly stated hypotheses (TOP), (BAL), and (UNBAL).

The legacy dependency audit is:

| Node family | Classification for this direct assembly |
|---|---|
| M9-M2-beta-algebra and the exact character factor | Required normalization/guardrail, already carried literally in every packet; no separate character estimate is assumed. |
| M9-M2-character-factor as an open analytic program | Not an additional outside estimate.  Its “retain \(\chi_4\)” requirement is satisfied syntactically; character-based cancellation is only one possible way to prove an open packet. |
| M9-near-collision-taxonomy and M9-near-collision-estimate | Alternative fourth-moment route, not a dependency of the direct physical Poisson assembly. |
| M9-M2-fourth-moment-expansion, exact-\(N=0\) nodes, local fourth moment, and near-collision strip nodes | Algebra and partial estimates for that alternative route; unused here. |
| M9-M2-average-to-pointwise-AP-lemma, global second moments, persistence, and local-moment bridge nodes | Alternative average-to-pointwise route; unused because every hypothesis here is already pointwise and uniform in real \(X\). |
| M9-M2-primitive-ray-fixed-a-actual-Gram | A possible proof mechanism internal to (TOP), not an outside assembly dependency after (TOP) is granted. |
| M9-endpoint-uniformity | A required uniformity property of all packet hypotheses and a downstream M2 consequence of the assembly, not a license to infer the still-open M1/M9 endpoint statement. |

Exact artifacts read and used, and no others:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/briefs/m2_outside_packet_assembly_attack.md;
- rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/derivation_packet.md;
- rounds/codex-managed/m9-frequency-phase-diagram/synthesis.md;
- rounds/codex-managed/m9-endpoint-kernel-validation/synthesis.md;
- rounds/codex-managed/m9-top-endpoint-transform/synthesis.md;
- rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md;
- rounds/codex-managed/gc-unconditional-exponent-extraction/synthesis.md;
- rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/synthesis.md.

No sibling Round-97 report, strategy file, computation, or new external
source was used.  The accepted TTY theorem is invoked only through its
already source-audited graph node.

## 7. Recommended state effect

**Promote** a proved internal conditional-assembly reduction with the
exact implication

\[
\mathrm{(TOP)}+\mathrm{(BAL)}+\mathrm{(UNBAL)}
\Longrightarrow \mathrm{M9\!-\!M2},
\]

subject to the literal real-\(X\), one-count, coefficient, profile, floor,
star, sign, and endpoint hypotheses in Section 2.

**Create or retain as open two explicit outside estimate nodes**:

- the smooth balanced outside-absolute signed quarter-packet estimate
  (BAL), distinct from the already proved reduction bearing similar
  wording;
- the smooth unbalanced actual-symbol \(M^{3/4}\) product-phase estimate
  (UNBAL), distinct from the already proved Poisson equivalence.

**Retain as open** the canonical hard-top density-discrepancy energy,
the top signed cone, and M9-M2 itself.  The canonical theorem alone has
an exact no-go certificate for full M2 assembly because the two smooth
rows remain ownerless.

**Revise dependency presentation, without promoting a theorem**, so the
near-collision, fourth-moment, and average-to-pointwise nodes are shown as
alternative routes rather than mandatory parents of this direct assembly.
Keep the exact character factor as a packet invariant/normalization
guardrail.

**No change** is licensed for M9-M1, M9-endpoint-uniformity as a global
M1/M2 obligation, M9, Conditional-bridge, GC-target, or either certified
global exponent.  In particular, this report proves no new exponent and
does not start another core attack.
