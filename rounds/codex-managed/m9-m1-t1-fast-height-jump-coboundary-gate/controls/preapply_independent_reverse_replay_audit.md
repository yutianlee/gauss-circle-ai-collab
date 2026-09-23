# Round 191 pre-apply independent reverse-replay audit

## 1. Result

**PASS.** The Round 191 State Patch is valid against the current
authoritative graph. The independently recomputed starting-graph
SHA-256 is
306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa,
exactly the hash recorded by the patch. The operation counts are one
create, one update, zero rejected-claim corrections, fifteen new
rejections, and twenty-three no-change declarations.

The patch promotes only the strict signed-inverse-small sector and its
exact terminal/Fejer projections. It leaves the rho-large remainder,
the complete original \(t=1\) packet, M1, M2, M9, both bridges, the
target, and every exponent unchanged.

## 2. Exact statement and hypotheses

This verdict assumes the graph remains at the exact starting hash above
and the patch is applied with round index 191 and the Round 191
adjudication as judge reference.

The sole created obligation is
M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction, with status
proved_internal. Its statement is restricted to the strict
signed-inverse-small sector of the Round-189 fast packet, the exact
outer-terminal and isolated Fejer projections, their
\(O_{B,\varepsilon}(L^2X^\varepsilon)\) lifted contribution, and the
exact safe-plus-rho-large-remainder decomposition. It has no implied
parent.

The sole updated obligation is
M9-M1-hard-top-high-radical-small-t-residual-estimate. Its current and
post-patch status are both open. The update adds the new subordinate
dependency and inconclusive evidence, and narrows the next action to
the rho-large remainder; it does not change status.

## 3. Proof or derivation

The created ID and all fifteen rejected IDs are absent from the current
obligation and rejection namespaces. The update ID and all twenty-three
no-change IDs exist, and all operation IDs are disjoint.

The fifteen post-patch rejected IDs are:

1. Round191-Abel-height-jump-is-cancellation;
2. Round191-signed-inverse-transport-preserves-literal-support;
3. Round191-full-anchor-parity-applies-modewise;
4. Round191-carry-signs-cancel-between-orientations;
5. Round191-small-inverse-sector-is-a-jump-correlation-gain;
6. Round191-small-inverse-sector-proves-full-fast-packet;
7. Round191-saturated-inverse-cut-leaves-unit-rows;
8. Round191-residue-class-plus-one-causes-power-loss;
9. Round191-lift-does-not-cancel-inverse-sector-m;
10. Round191-terminal-and-Fejer-projections-break-one-outer-operation;
11. Round191-positive-variation-closes-rho-large-remainder;
12. Round191-completion-large-sieve-or-alias-energy-gains-height;
13. Round191-bounded-array-capacity-is-literal-lower-mass;
14. Round191-strict-sector-proves-complete-t1;
15. Round191-strict-sector-improves-global-exponent.

The twenty-three no-change IDs retain these exact statuses:

- proved_internal: M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction;
  M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction;
  M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction;
  M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction;
  M9-M1-hard-top-t1-comparable-factor-exchange-sector;
  M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector;
  M9-M1-physical-one-count-assembly; GC-partial-one-third; and
  Divisor-bound-elementary.
- open: M9-M1-top-endpoint-signed-cone;
  M9-M1-direct-smooth-residual-blockwise-estimate;
  M9-M1-global-angular-radial-estimate; M9-M1;
  M9-M2-top-endpoint-signed-cone;
  M9-M2-smooth-balanced-quarter-packet-estimate;
  M9-M2-smooth-unbalanced-three-quarter-estimate; M9-M2;
  M9-endpoint-uniformity; M9; and GC-target.
- derived_under_assumptions: Conditional-bridge and
  GC-global-M1-alternative-bridge.
- proved_external_dependency: GC-external-Li-Yang-theta-star.

Both direct dependencies of the created node exist and are
proved_internal:
M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction and
Divisor-bound-elementary. The patch contains 41 evidence references to
23 unique paths; all 23 paths exist. Evidence added to the still-open
owner is classified inconclusive.

The exact reversibility payload matches the current graph: the stored
old next action is identical to the owner's current next action, and
the stored metadata is exactly last_updated_round 190 and
last_updated_at 2026-08-29T20:38:31. The added dependency and evidence
entries are new. An in-memory forward application followed by the
declared inverse removed the created obligation and fifteen rejected
records, removed all additions, restored the old action and metadata,
and returned a graph deep-equal to the starting graph with the same
canonical digest.

Finally, the created node has an empty implies list, while the updated
owner remains open. The no-change statuses explicitly keep the hard and
smooth M1 parents, every M2 route, endpoint uniformity, M9, both
bridges, and GC-target unpromoted. The internal \(1/3\), external
\(0.3144831759740614\ldots\), and target \(1/4\) exponents are
unchanged.

## 4. First doubtful or unproved step

The first mathematical step still unproved is the rho-large signed
remainder estimate

\[
\Re\mathscr R_{Y,Q}^{\sigma}
\ll_{B,\varepsilon}L^2X^\varepsilon,
\]

with positive-control deficit \(Y/(Qm)\). The patch names this as the
next action and does not promote it. No patch-mechanics defect was
found. This audit is conditional on the starting graph hash remaining
unchanged until application.

## 5. Required control test and outcome

The official non-applying validator was run with graph
state/proof_obligations.yml, the Round 191 patch, round index 191, and
the Round 191 adjudication judge reference, without --apply. Its exact
outcome was:

Patch OK

The graph hash after validation was still the starting hash. Independent
controls also passed for operation preconditions, dependency statuses,
all 23 unique evidence paths, protected-scope comparison, and exact
forward/reverse recovery.

## 6. Dependencies and exact artifacts used

The audit used protocol.md; state/proof_obligations.yml; the Round 191
state_patch.json, conductor_round191_adjudication.md, and synthesis.md;
the final candidate at SHA-256
76c1a3adb14fc00063a2fcab06f73458ae8f5c9b0e7d19e41c5d8c78f103b978;
the final kernel at SHA-256
7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2;
and the three final post-hygiene verification reports.

The exact mathematical dependencies are the two proved_internal nodes
listed in Section 3. Evidence-path existence was checked without
treating finite controls as asymptotic proof. No state file or State
Patch was edited.

## 7. Recommended state effect

Apply the unchanged Round 191 State Patch to the unchanged starting
graph. Promote only
M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction as
proved_internal; retain the updated owner as open; add the fifteen
rejected overclaims; and make no other status or exponent change. If
the starting graph hash changes, rerun validation before applying.

**PASS**
