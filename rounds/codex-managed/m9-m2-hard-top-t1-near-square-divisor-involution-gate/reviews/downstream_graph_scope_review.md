# Round 163 downstream graph and scope review

## 1. Result and verdict

**Verdict: GREEN, with a strict incidence-sector scope.**  The smallest
legitimate proof-state effect is to create exactly one proved-internal
node,

`M9-M2-hard-top-t1-close-opposite-prime-exchange-sector`,

and to close Round 163 under the sole exit label
`strict_t1_prime_toggle_sector`.

For fixed \(\kappa>0\), this node owns the complete literal contribution
of those squarefree \(t=1\) incidences for which a canonical
\(L^{-1/2}\)-close pair of opposite-\(\chi _4\) odd prime divisors of
\(N\) exists and exactly one member lies in the odd character-bearing
factor.  That sub-sum is \(O_\kappa(L^{3/2})\), uniformly in the
arbitrary real centre.  The selection is explicit, depends only on
\((N,L,\kappa)\), and the proof owns every selected incidence, including
zero-extended partner legs and all literal profile and hard-face
crossings.

No eligible-pair density, positive proportion, per-block nonemptiness,
or complementary-incidence estimate is proved.  This does **not**
invalidate the strict-sector exit: the node is an exact
coefficient-independent arithmetic sub-sum theorem, not an
exceptional-set theorem whose complement is declared negligible.  The
condition is arithmetically realizable (for example, with \(\kappa=1\),
\(p=11,q=13,L=16\) one has
\(\log(13/11)<2/11<1/4=L^{-1/2}\)); this witness proves no asymptotic
density and need not be inserted into the node statement.  The word
“sector” must mean only the explicitly selected incidence class, never
a positive-density or owner-complete portion of full \(t=1\).

The one-prime toggle self-return, arbitrary exchange/matching
classification, complement identities, and full-divisor-completion
leakage should remain scoped route evidence, not become a second graph
node.  Only the two existing open hard-TOP owners may receive the new
sector as a dependency.  No implication edge, blocker removal,
downstream promotion, or exponent change is licensed.

## 2. Exact node statement, hypotheses, and evidence status

Retain the frozen literal scalar

\[
 \mathcal S_{L,1}
 =\sum_{N\asymp L^2}^{\rm lit}\mu ^2(N)
   \left(\frac{L^2}{N}\right)^{3/4}e(J\sqrt N)
   \sum_{\substack{d\mid N,\ d\ {\rm odd}\\
                   \sqrt N\le d\le2\sqrt N}}^{\rm lit}
   \chi _4(d)P_N(d),
\tag{G.1}
\]

where

\[
 P_N(d)=\eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right),
 \qquad J=\sqrt X,
\tag{G.2}
\]

and every inherited half-open shell, cone, even-\(N\) branch, floor,
star, endpoint, profile entry and exit, and zero extension is retained.
The accepted interfaces give one fixed smooth dyadic \(\eta_L\), one
fixed smooth \(W\), bounded \(C^1\) \(\Phi\), and finitely many literal
hard faces.  In particular, for \(d,m\asymp L\), \(|u|\le1\), and both
points in a common smooth cell,

\[
 \left|Q_{L,X}(e^u d,e^{-u}m)-Q_{L,X}(d,m)\right|
 \ll |u|,
\tag{G.3}
\]

with

\[
 Q_{L,X}(d,m)=\eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xd}{4m}}\right).
\]

For each supported squarefree \(N\), choose at most one unordered pair
of distinct odd prime divisors \(\{p_{N,L,\kappa},q_{N,L,\kappa}\}\)
satisfying

\[
 \chi _4(p_{N,L,\kappa}q_{N,L,\kappa})=-1,
 \qquad
 \left|\log\frac{q_{N,L,\kappa}}{p_{N,L,\kappa}}\right|
 \le \kappa L^{-1/2},
\tag{G.4}
\]

by lexicographically minimizing
\((|\log(q/p)|,\min(p,q),\max(p,q))\); choose no pair if none exists.
This rule depends on \((N,L,\kappa)\), not on a divisor allocation.  Let

\[
 \mathscr D_{N,L,\kappa}^{\rm cp}
 =\left\{d\mid N:d\ {\rm odd},\quad
   {\bf1}_{p_{N,L,\kappa}\mid d}
  +{\bf1}_{q_{N,L,\kappa}\mid d}=1\right\},
\tag{G.5}
\]

and zero-extend the full literal amplitude \(A_N(d)\), including star
weights, to all odd divisors.  The exact proposed node statement is

\[
 \boxed{
 \left|\mathcal S_{L,1}^{\rm cp}\right|
 =\left|\sum_{\substack{N\asymp L^2\ {\rm sf}\\N\ {\rm qualifies}}}
 \left(\frac{L^2}{N}\right)^{3/4}e(J\sqrt N)
 \sum_{d\in\mathscr D_{N,L,\kappa}^{\rm cp}}
 \chi _4(d)A_N(d)\right|
 \ll_\kappa L^{3/2}.}
\tag{G.6}
\]

The estimate is uniform for every allowed \(X,H,L\) and every real
\(J=\sqrt X\).  Its statement must expressly exclude any assertion
about the density or nonemptiness of qualifying \(N\), the number of
selected incidences, or the complementary incidences containing neither
or both selected primes.

The graph metadata should be:

- type: `lemma`;
- status: `proved_internal`;
- dependencies:
  `M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`,
  `M9-M2-top-endpoint-actual-symbol-variation`, and
  `H4-Phi-regularity`;
- `implies: []`;
- `blockers: []`.

The Round-162 node owns the exact squarefree \(t=1\) coefficient,
parity, phase, and literal hard conventions.  The latter two dependencies
make the smooth-profile and \(C^1\)-\(\Phi\) provenance explicit.  No
direct dependency on the Round-137 or Round-161 nodes, the top transform,
or the character-factor node is needed because those interfaces are
already inherited through the Round-162 dependency.  The new node must
not depend on either open parent to which it will be attached.

Use the conductor candidate, the literal discovery report, the hostile
audit, and this review as positive evidence for the new node.  Classify
the statement-only blind report as inconclusive for this node: it
correctly identifies profile regularity as unavailable in its frozen
statement, whereas the accepted graph dependencies above provide that
missing interface.  This is not negative evidence against (G.6).  The
prime-number-theorem diagnostic counts in the discovery report are not
part of (G.6), its proof, its dependencies, or its evidence claim.

## 3. Proof, dependency direction, and exact parent attachments

Suppress \((N,L,\kappa)\) from the canonical pair.  On the complete XOR
divisor set (G.5), define

\[
 T_Nd=
 \begin{cases}
 d\,q/p,&p\mid d,\ q\nmid d,\\
 d\,p/q,&q\mid d,\ p\nmid d.
 \end{cases}
\tag{G.7}
\]

Squarefreeness makes both quotients integral.  Since the selected pair
depends only on \((N,L,\kappa)\), \(T_N\) is a fixed-point-free,
multiplicity-one involution.  It preserves \(N=d(N/d)\), squarefreeness,
coprimality, oddness of \(d\), the even-\(N\) factor \(2\) in the other
leg, the product shell, normalization, and \(e(J\sqrt N)\) for every
real \(J\).  Opposite character gives

\[
 \chi _4(T_Nd)=-\chi _4(d).
\tag{G.8}
\]

Reindexing the complete zero-extended XOR set therefore gives the exact
identity

\[
 \sum_{d\in\mathscr D_{N,L,\kappa}^{\rm cp}}
 \chi _4(d)A_N(d)
 =\frac12\sum_{d\in\mathscr D_{N,L,\kappa}^{\rm cp}}
 \chi _4(d)\{A_N(d)-A_N(T_Nd)\}.
\tag{G.9}
\]

Put \(\theta_N=\log(q/p)\).  On every common smooth cell, (G.3) and
\(|\theta_N|\le\kappa L^{-1/2}\) give an
\(O_\kappa(L^{-1/2})\) paired amplitude difference.  The
\(\Phi\)-part is in fact
\(O(|\theta_N|L/H)\), hence no larger, and the exact values of
\(H,q_X\), floors, and profile arguments are not replaced.  The literal
support occupies a fixed \(O(L)\)-by-\(O(L)\) integer box, so there are
at most \(O(L^2)\) ambient factor pairs.  The common-cell contribution
is consequently \(O_\kappa(L^{3/2})\).

The exchange multiplies \(d\) by \(e^{\pm\theta_N}\) and \(d/(N/d)\)
by \(e^{\pm2\theta_N}\).  A half-open shell, cone, dyadic face,
ratio-profile face, vertical-profile face, endpoint, or zero-extension
status can change only in one of finitely many relative
\(O_\kappa(L^{-1/2})\) collars.  Counting the containing integer box,
without any divisor or prime-distribution estimate, gives
\(O_\kappa(L^{3/2}+L)\) pairs in all such collars.  Ceilings, stars, and
ties lie on the same faces and contribute within the \(O(L)\) term.
Arithmetic support conditions can only delete pairs.  Bounded amplitudes
and (G.9) prove (G.6).

No density fact entered this proof: \(O(L^2)\) is an ambient upper
count, not a count of qualifying products.  Thus lack of density weakens
only what the sector removes from the open parent; it does not weaken the
validity or target power of the selected sub-sum.

The exact parent mutations should be limited to the following.

1. Add `M9-M2-hard-top-t1-close-opposite-prime-exchange-sector` as a
   dependency of `M9-M2-top-endpoint-signed-cone`.  Add the Round-163
   candidate, all three reports, and this review as **inconclusive**
   evidence for that still-open parent.  Do not change its statement,
   status, blocker, or implication to
   `M9-M2-physical-one-count-assembly`.
2. Add the same new dependency and the same inconclusive parent evidence
   to `M9-M2-top-endpoint-density-discrepancy-energy`.  Do not change its
   statement, open status, blockers, or implication to the signed cone.
   In particular, (G.6) is a literal scalar sector bound, not a
   completed-real-part or density-discrepancy estimate.

The dependency direction is acyclic: accepted Round-162/profile nodes
feed the new sector, and the new sector feeds the two open owners.  There
is no reverse edge and no new `implies` edge.  Evidence that proves the
child is only inconclusive evidence for either larger parent.

## 4. First doubtful or unproved step

The first unproved physical quantity is the exact complementary
incidence scalar

\[
 \mathcal S_{L,1}^{\rm rem}
 :=\mathcal S_{L,1}-\mathcal S_{L,1}^{\rm cp}.
\tag{G.10}
\]

It consists precisely of:

1. every incidence belonging to a supported squarefree \(N\) with no
   canonical pair satisfying (G.4); and
2. for a qualifying \(N\), every incidence whose odd leg contains
   neither or both selected primes.

No report proves

\[
 \boxed{|\mathcal S_{L,1}^{\rm rem}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.}
\tag{G.11}
\]

Neither a density theorem for qualifying \(N\) nor a count of selected
incidences would by itself prove (G.11): the unselected weighted scalar
still requires cancellation at the arbitrary real centre.  The exact
one-prime identities self-return, unrestricted matching can leave a
sign-count defect, and matching cycles only rewrite literal profile
gradients.  Complement and full-divisor completion move the omitted
mass to uncontrolled scales.

Even a proof of (G.11), combined with (G.6), would settle only the
literal \(t=1,D\asymp L^2\) face.  The compatible channels
\(L\ll D\ll L^2\), \(t\ll\sqrt L\), including their near-collision
collars, would still remain before the full hard-TOP parents could close.
At graph level the first impermissible step would be to read the new
dependency as an implication to either parent, or to transfer this
scalar sector into the completed density-discrepancy energy without its
accepted one-count/real-part connector.

## 5. Control outcomes, quarantined nodes, and rejected claims

| Control | Outcome |
|---|---|
| Strict sector without density | **GREEN with exact scope.**  The selector is canonical and allocation-independent, and every selected incidence is bounded.  It proves no positive proportion or per-block nonemptiness. |
| Blind/nonblind evidence seam | **GREEN.**  The blind report's first open step is the unavailable profile interface.  The accepted profile dependencies resolve that seam; the blind report remains inconclusive, not contrary. |
| Literal profiles and zero extension | **GREEN for the selected sector.**  Common-cell differences cost \(L^{-1/2}\); all entries, exits, partner-zero legs, floors, stars, and half-open faces cost \(O(L^{3/2}+L)\). |
| Canonical multiplicity and phase | **GREEN.**  One pair is selected per \((N,L,\kappa)\), \(T_N\) is a fixed-point-free involution, and \(N\) and \(e(J\sqrt N)\) are unchanged. |
| Even-\(N\) branch | **GREEN.**  Only odd primes move, so the factor \(2\) remains in the non-character leg.  No even-\(N\) complement symmetry is inferred. |
| Full \(t=1\) and density power | **OPEN.**  (G.11) is untouched.  Diagnostic semiprime/multi-prime counts and logarithmic sparsity supply neither a physical lower bound nor the missing half-power. |
| General toggle/matching route | **SCOPED NO-GO ONLY.**  One-prime averaging exactly reproduces the coefficient; arbitrary exchange graphs require equal sign counts/Hall; even cycles and weighted transport retain profile gradients and unmatched fibres. |
| Parent evidence classification | **GREEN.**  Round-163 artifacts prove the child but are only inconclusive evidence for both open hard-TOP parents. |
| Downstream scope | **GREEN quarantine.**  No other few-point, smooth-packet, assembly, theorem, bridge, target, or exponent node is changed. |

The exact downstream quarantine is:

| Layer | Exact graph object | Required status/effect |
|---|---|---|
| Complete \(t=1\) residual and remaining few-point channels | Subproblems retained in the two hard-TOP owners | Open; next action only |
| Hard TOP | `M9-M2-top-endpoint-signed-cone`; `M9-M2-top-endpoint-density-discrepancy-energy` | Both remain open; dependency and inconclusive evidence only |
| Smooth BAL | `M9-M2-smooth-balanced-quarter-packet-estimate` | Open and unchanged |
| Smooth UNBAL | `M9-M2-smooth-unbalanced-three-quarter-estimate` | Open and unchanged |
| M2 assembly | `M9-M2-physical-one-count-assembly`; `M9-M2` | The reduction remains proved internal; `M9-M2` remains open with all three analytic blockers |
| Global analytic theorem | `M9` | Open and unchanged |
| Bridge | `Conditional-bridge` | Remains derived under assumptions, blocked by `M9` |
| Conjectural target | `GC-target` | Open and unchanged; no quarter theorem follows |
| Internal exponent | `GC-partial-one-third` | Remains proved internal and numerically unchanged |
| External benchmark | `GC-external-Li-Yang-theta-star` | Remains a proved external dependency and numerically unchanged |

Reject, or preserve rejection of, each of the following precise stronger
claims:

1. the close opposite-prime selector is nonempty in every block, has
   positive or polynomial density, or covers a quantified proportion of
   the physical coefficient;
2. (G.6) estimates the full \(t=1\) scalar or its residual (G.10);
3. a one-prime \(p\equiv3\pmod4\) toggle has two physical legs in the
   multiplicative-width-two upper window;
4. averaging one-prime toggles over \(p\mid N\) yields a
   \(1/|\mathcal P_3(N)|\) gain rather than the exact self-return
   \(|\mathcal P_3(N)|b_{L,X}(N)\);
5. the existence of some window-preserving two- or multi-prime partner
   gives a canonical injective global matching;
6. the unrestricted exchange graph always has a perfect matching, or a
   restricted graph avoids the sign-count and Hall obstructions;
7. even matching cycles, graph averaging, or profile-dependent weights
   erase unmatched/same-sign fibres or give cancellation beyond the
   exact transported profile differences;
8. odd complementation maps the upper physical window to itself;
9. for \(N=2M\), either the even factor swap \(N/d\) or the odd-part
   complement \(M/d=N/(2d)\) supplies an upper-window symmetry—the
   latter lies in \([\sqrt N/4,\sqrt N/2]\);
10. vanishing of the full odd-divisor character sum controls the
    truncated, profiled upper-window coefficient, or full-divisor
    completion has harmless complementary mass;
11. products without a \(3\pmod4\) prime, semiprime/multi-prime
    diagnostic counts, or logarithmic representable-sector sparsity
    give a polynomial saving for the literal coefficient;
12. constant-profile controls or the fixed-modulus-PNT diagnostics in
    the discovery report are physical mass or lower-bound statements;
13. the strict sector closes the other \(t=1\) incidences, the remaining
    \(L\ll D\ll L^2\) few-point channels, or either hard-TOP parent;
14. a hard-TOP scalar sector transfers to BAL or UNBAL;
15. the result removes any blocker of `M9-M2`, proves `M9`, validates
    `Conditional-bridge`, or proves `GC-target`; or
16. the result improves, reproves, or otherwise changes either
    `GC-partial-one-third` or `GC-external-Li-Yang-theta-star`.

No numerical or symbolic experiment is needed for this graph decision.

## 6. Dependencies and exact artifacts used

This review used the project instructions in `AGENTS.md`, together with:

- `protocol.md`;
- `state/proof_obligations.yml` at the Round-163 starting graph and its
  exact hard-TOP, BAL, UNBAL, M9-M2, M9, bridge, target, and exponent
  entries;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/briefs/prime_toggle_complement_leakage_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/candidates/conductor_round163_close_opposite_prime_exchange_sector.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reports/blind_near_square_divisor_rederivation.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reports/literal_near_square_divisor_involution_attack.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reports/prime_toggle_complement_leakage_hostile_audit.md`.

The graph interfaces used for the proposed child dependencies were
`M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`,
`M9-M2-top-endpoint-actual-symbol-variation`, and
`H4-Phi-regularity`.  The exact downstream nodes audited are those
listed in Section 5.  The accepted Round-161 downstream graph review was
consulted only for the existing dependency/evidence convention for a
target-safe hard-TOP sector; no Round-161 estimate is imported into
(G.6).  The M1 complementary-divisor synthesis enters only through the
hostile report's audit of full-minus-complement and parity logic and is
not an M2 dependency.

No web lookup, computation, external density theorem, or unlisted
mathematical estimate is used in the proposed node.  No shared state,
candidate, synthesis, report, or review other than this assigned file
was edited.

## 7. Recommended state effect and next action

Create exactly one node:

- id: `M9-M2-hard-top-t1-close-opposite-prime-exchange-sector`;
- type/status: `lemma`, `proved_internal`;
- statement: exactly (G.1)--(G.6), the canonical selection, exact XOR
  involution, complete common-cell and hard-crossing ledger, uniform
  \(O_\kappa(L^{3/2})\) bound, and explicit exclusions of density,
  per-block nonemptiness, complement coverage, and downstream transfer;
- dependencies:
  `M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`,
  `M9-M2-top-endpoint-actual-symbol-variation`, and
  `H4-Phi-regularity`;
- `implies: []`, `blockers: []`;
- positive evidence: the conductor candidate, literal discovery report,
  hostile audit, and this review;
- inconclusive evidence: the statement-only blind report, solely because
  its frozen context did not contain the accepted profile interface;
- negative evidence: none;
- node `next_action`: subtract only this exact selected incidence sector
  from the literal \(t=1\) scalar; do not infer eligible-pair density or
  any estimate for (G.10).

Update only the following two open parents.

1. For `M9-M2-top-endpoint-signed-cone`, add the new node as a
   dependency and add all Round-163 artifacts as inconclusive parent
   evidence.  Replace only `next_action` by: remove the already accepted
   long/exact-collision sectors and the new close-opposite-prime XOR
   incidence sector; prove the complete residual (G.11) with literal
   profiles, hard boundaries, and arbitrary-real-centre phase; then
   treat the remaining \(L\ll D\ll L^2,\ t\ll\sqrt L\) channels and
   near collars.
2. For `M9-M2-top-endpoint-density-discrepancy-energy`, add the same
   dependency and inconclusive parent evidence.  Replace only
   `next_action` by: preserve the accepted one-count and
   completed-real-part connector; first prove the literal signed
   residual (G.11), then the other few-point channels, before any
   transfer back to this energy.  Do not call (G.6) a completed-energy
   estimate.

Retain the general toggle, matching, complement, full-completion, and
diagnostic classifications only as scoped Round-163 route evidence.
Record the sixteen rejected stronger readings in Section 5, but create
no second obstruction node.  Leave unchanged the statements, statuses,
blockers, and implication edges of both hard-TOP parents, the Round-137,
Round-161, and Round-162 accepted nodes,
`M9-M2-physical-one-count-assembly`, both smooth packet parents,
`M9-M2`, `M9`, `Conditional-bridge`, `GC-target`,
`GC-partial-one-third`, and `GC-external-Li-Yang-theta-star`.

The next mathematical action is exactly (G.11), followed—not
preceded—by the remaining few-point channels.  No full \(t=1\), hard
TOP, BAL, UNBAL, M9-M2, M9, bridge, target, quarter theorem, internal
exponent, or external benchmark is promoted.
