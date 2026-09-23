# Candidate provenance, owner, and graph-scope post-repair verification

- Campaign: `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Round: 197
- Candidate SHA-256 reviewed:
  `cb4867784fe051a09ce703b133dfc1b90a82526573a56223123d9c07d075b5e0`
- Verdict: **REPAIR**
- Repair class: local definition/provenance corrections; the physical mask,
  theorem scope, graph direction, terminal label, protected scope, and
  exponent quarantine are otherwise green

## 1. Result

The amended candidate closes the substantive defects from the initial
provenance review.  It gives a finite closed sharp-code tuple independent of
coefficient values, fixes $K_{\mathrm{sel}}$, defines the physical atom and
both physical $\kappa$-charts, imports the packet/Farey data, defines the
core/cap/open outer operators, and now also defines
$\mathscr H_{\mathrm{out}}^\sigma$ and
$\mathscr S_{\le192,\mathrm{out}}^\sigma$ with the exact linear core
identity.  Its State-Patch direction is cycle-safe, its no-go terminal label
is frozen, and every parent and exponent remains quarantined.

Three local repairs still prevent a fully green formalization verdict.

1. In (197.C1a), replace “the first pair under the accepted canonical
   ordering” by the actual fixed rule, for example “the lexicographically
   first ordered pair $(p,q)$ with $p<q$.”  Round 184 permits any fixed
   allocation-independent canonical rule but does not turn the phrase
   “accepted canonical ordering” into a self-contained ordering definition.
2. In the prose after (197.C9d), (J) is not an “anchor length.”  It is the
   inherited dyadic projective band $J\le j_q(a,v)<2J$; the associated Abel
   denominator is (q/J).  Replace that phrase by “the accepted power-of-two
   projective-band label.”
3. Dependency item 1 cites the sharp fields as “used in (197.C8a).”  The
   arithmetic conjunction is (197.C8a); the sharp-field list and code are
   (197.C8b)--(197.C8c).  Correct the cross-reference and list the four
   Round-197 claimant/reconciliation paths explicitly rather than only by
   role names.

These changes do not alter the sector, proof, power, complement, graph, or
owner scope.  After them, this seam is eligible for **GREEN** without another
mathematical repair.

## 2. Exact sharp-code and selector verification

**Sharp code: GREEN.**  Equations (197.C8a)--(197.C8c) give a genuinely
finite, closed tuple.  The live tuple contains only accepted named truth,
branch, cell, crossing, tie, half-weight, sample, endpoint, and sign labels.
The dead value is determined only by arithmetic/support/zero-extension
predicates.  The code expressly excludes $a^{\rm lit}$, $\lambda$,
$\rho_N$, $\eta_L$, $\Phi$, $W_{\rm tr}$, and all smooth-factor
values.  Thus $C_{\rm lit}$ is a pre-spectral physical mask, is symmetric
under the lower swap, and is independent of accidental coefficient
nonvanishing.  Collapsing all dead causes to $\dagger$ is harmless: in that
case both lower literal symbols are zero, while every live/dead mismatch lies
in $P_{\partial\rm lit}$.

The later exact identity (197.C22d) confirms that the code has not hidden the
selector or BV profile.  The smooth, BV, and selector differences are three
separate summands.  The aligned-face complement remains explicit; no
nonemptiness, density, or mass is inferred.

**Selector parameter: GREEN after one wording repair.**  The candidate fixes
$K_{\mathrm{sel}}>0$, keeps it distinct from physical $\kappa$, makes the
pair allocation-independent, states the exact ((1,0,0,1)) mask, includes
$K_{\mathrm{sel}}$ in the final constants, and supplies the bounded-$g$
exception argument.  Only the canonical tie-break needs to be named rather
than referenced abstractly.

## 3. Operator and proof typing

**GREEN except for the (J) label.**  The candidate now distinguishes:

- the transformed hard profile $W_{\rm tr}$ from the physical atom $W$;
- physical cofactor $m$, spectral lift gcd $\mathfrak m$, selector width
  $K_{\mathrm{sel}}$, and physical inward gcd $\kappa$;
- the plus chart $\kappa=(d,m')$ from the minus chart
  $\kappa=(d',m)$;
- fixed-packet, safe-packet, open-packet, physical-source, safe-projector, and
  restored outer operators.

Equations (197.C9h)--(197.C9k) are correctly typed linear restrictions of the
same accepted fixed-to-outer assembly.  The physical mask is applied to the
parent atom before Fourier or height operations.  Equations (197.C28a),
(197.C30), and (197.C34) retain the transported-mask commutator, births,
deaths, $T=0$, all simultaneous $T\ge1$ conditions, orientations, anchor
copies, zero extensions, and the one outer real part.  The packet condition
is introduced only after the complete physical pairing.  This resolves the
previous missing definitions of $\mathscr H_{\rm out}$ and
$\mathscr S_{\le192,\rm out}$.

The only false operator-description phrase is “(J) is the accepted anchor
length.”  The accepted Round-189/191 interface defines a dyadic band
$J\le j_q(a,v)<2J$; it is this band that yields $O(uJ/q)$ rows and the
(q/J) Abel return used by Round 195.  Correcting the noun does not change
any formula in the candidate.

## 4. Dependency provenance and first doubtful step

The four accepted interfaces are correctly typed and cited by exact node ID,
kernel path, and equation ranges:

1. Round 184 for the selector and exact literal $C^1$/BV ledger;
2. Round 185 for the total endpoint, physical opening, primitive charts, and
   monotone/low-height exits;
3. Round 193 for finite (g), coordinatewise physical masking, and the
   transported-mask product rule; and
4. Round 195 for the $P_2$ count, deletion-stable packet estimate,
   fixed-to-outer ledger, and exact packet split.

The candidate correctly says that these are accepted theorem interfaces and
that Round-197 reports, reviews, and diagnostics are evidence rather than
prerequisites.  Correct only the reference “sharp fields used in
(197.C8a)” to “sharp fields used in (197.C8b)--(197.C8c).”  For exact artifact
provenance, replace the role-only claimant sentence by these paths:

- `reports/literal_four_corner_allocation_commutator_attack.md`;
- `reports/four_corner_orbit_power_hostile_audit.md`;
- `reports/blind_four_corner_commutator_rederivation.md`; and
- `reviews/conductor_round197_report_reconciliation.md`.

All four are relative to the current Round-197 campaign directory.

The first remaining doubtful statement in document order is therefore the
undefined selector ordering in (197.C1a), not a mathematical orbit or power
step.  The required control is to instantiate the fixed lexicographic rule
already permitted by the Round-184 candidate.  Outcome: **local wording
repair required; no theorem narrowing**.

## 5. Graph direction, complement, and terminal label

**GREEN.**  Proposed state effect 7.3 now leaves the accepted Round-184,
185, 193, and 195 nodes unchanged.  The new node depends only on accepted
ancestors, while the still-open hard small-(t) owner may depend on the new
node.  No Round-195-to-Round-197 reverse edge is proposed, so the repaired
direction introduces no Round-197/Round-195 cycle.

The exact physical partition (197.C13)--(197.C14) remains disjoint and
exhaustive.  The later open packet region is exactly (197.C11) intersected
with

\[
 P_{\partial\rm lit}\ \dot\cup\ P_{s\rm f}\ \dot\cup\ P_{g\rm f}.
\]

Only $P_{\rm cc}$ is removed.  The full rectangle still forces
$\kappa=1$, and the aligned literal-face complement retains the stated
route capacity.  The frozen terminal label
`p2_four_corner_orbit_boundary_self_return_no_go` is therefore exact.  No
unsupported strict-four-corner label is used.

## 6. Protected owner and exponent controls

| Control | Outcome |
|---|---|
| candidate hash | **PASS:** reviewed hash is `CB4867784FE051A09CE703B133DFC1B90A82526573A56223123D9C07D075B5E0` |
| finite sharp-code closure | **PASS** |
| coefficient-nonvanishing independence | **PASS** |
| selector parameter and constants | **PASS**, subject only to naming the tie-break |
| physical/packet/operator typing | **PASS**, except the local (J)-description repair |
| exact complement | **PASS** |
| accepted dependency typing | **PASS**, with one cross-reference typo |
| graph direction and cycle control | **PASS** |
| frozen terminal label | **PASS** |
| hard small-(t) owner remains open | **PASS** |
| Round-184/185/193/195 protection | **PASS** |
| M1 parents, GAR, M2, endpoint uniformity, M9, bridges, target | **PASS: all unchanged** |
| $1/3$, external $0.3144831759740614\ldots$, and $1/4$ records | **PASS: unchanged** |
| diagnostic-only computation | **PASS** |

The report uses only the current candidate, the initial review and repair
specification, `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`, the four accepted kernel paths named in Section
6 of the candidate, the Round-184 formal candidate for its canonical-selector
wording, and the accepted Round-189 projective kernel for the exact meaning of
(J).  No external source or computation is theorem evidence.

## 7. Recommended state effect

**REPAIR, then GREEN.**  Make only these textual changes:

1. name the fixed lexicographic selector ordering in (197.C1a);
2. replace “accepted anchor length” by “accepted power-of-two projective-band
   label $J\le j_q(a,v)<2J$” after (197.C9d);
3. change dependency item 1 from (197.C8a) to
   (197.C8b)--(197.C8c); and
4. spell out the four claimant/reconciliation paths.

Do not alter the theorem, mask, complement, power ledger, dependency-edge
direction, owner status, protected nodes, terminal label, or exponent
records.  Once these four local corrections are present, this
provenance/owner/graph seam is green for formalization and State-Patch replay.
