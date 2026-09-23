# Candidate provenance, owner, and graph-scope final verification

- Campaign: `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Round: 197
- Candidate SHA-256 reviewed:
  `285ea0975eb3d48691ffb27b5a83e251d33a68062eb4d14dd54972f6af6296c0`
- Verdict: **GREEN**

## 1. Result

All four local corrections required by the post-repair review are present.
The candidate is green on sharp-code closure, selector definition, physical
and outer-operator typing, dependency provenance, graph direction, terminal
label, protected scope, and exponent quarantine.

## 2. Exact definitions

The selector now uses the lexicographically first ordered eligible pair
$(p_N,q_N)$ with $p_N<q_N$, depends only on
$(N,L,K_{\mathrm{sel}})$, and is distinct from physical $\kappa$.
The finite sharp code remains a closed tuple of accepted literal labels and
excludes coefficient, selector, BV, and smooth-factor values.  Hence
$P_{\mathrm{cc}}$ is a genuine coefficient-independent physical mask.

The packet prose now correctly identifies (J) as the accepted power-of-two
projective-band label $J\le j_q(a,v)<2J$, rather than an anchor length.
All previously verified physical, packet, Farey, core/cap/open,
$\mathscr H_{\rm out}$, and $\mathscr S_{\le192,\rm out}$ definitions
remain unchanged and correctly typed.

## 3. Verification derivation

The sharp-field dependency cross-reference now points to
(197.C8b)--(197.C8c).  The exact claimant/reconciliation paths are listed in
Section 6.  The accepted Round-184/185/193/195 interfaces retain their exact
node IDs, kernel paths, and roles.  No claimant report or diagnostic is
mistyped as an accepted prerequisite.

The proposed graph direction remains

\[
 \text{open hard small-}t\text{ owner}
 \longrightarrow \text{new Round-197 node}
 \longrightarrow \text{accepted ancestors},
\]

with the Round-195 node unchanged.  Therefore no Round-197/Round-195 cycle is
introduced.

## 4. First doubtful or unproved step

No remaining definition, provenance, owner-scope, or graph-scope defect was
found in this seam.  The unresolved mathematical step is still the expressly
quarantined complement
$P_{\partial\rm lit}\dot\cup P_{s\rm f}\dot\cup P_{g\rm f}$ on the exact
Round-195 open packet region; the candidate does not claim to estimate it.

## 5. Control outcomes

| Control | Outcome |
|---|---|
| candidate hash | **PASS** |
| lexicographic selector and $K_{\rm sel}$ dependence | **PASS** |
| finite sharp-code closure and nonvanishing independence | **PASS** |
| $J$-band and outer-operator typing | **PASS** |
| exact accepted and claimant provenance | **PASS** |
| exact physical/open complement | **PASS** |
| Round-197/Round-195 cycle avoidance | **PASS** |
| frozen terminal label | **PASS** |
| protected owner and parents | **PASS** |
| exponent quarantine | **PASS** |

## 6. Dependencies and artifacts used

This verification used the amended candidate, the initial review, repair
specification, post-repair review, `protocol.md`,
`state/proof_obligations.yml`, `state/active_campaign.yml`, and the accepted
Round-184/185/193/195 kernel paths named by the candidate.  No external source
or computation is theorem evidence.

## 7. Recommended state effect

**GREEN for the remaining formalization and State-Patch replay gates.**  The
permitted effect remains one subordinate `proved_internal` common-cell node,
added only to the still-open hard small-(t) owner.  Leave Round 184, 185,
193, and 195, every parent and bridge, the target theorem, and all exponent
records unchanged.  Close Round 197 only under
`p2_four_corner_orbit_boundary_self_return_no_go`.
