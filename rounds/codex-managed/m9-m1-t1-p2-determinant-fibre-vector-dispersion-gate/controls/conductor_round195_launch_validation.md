# Round 195 conductor launch validation

- Campaign: `m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate`
- Starting graph:
  `815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`
- Status: active
- Resource allocation: at least 98% analytical/algebraic and at most 2%
  bounded diagnostic computation

## 1. Result

Round 195 is validly frozen and prepared on exactly the complete physical
(P_2) complement. The campaign has one objective and three orthogonal
tasks: literal discovery, hostile Gram/collision audit, and statement-only
rederivation. No proof-graph status or exponent changes at launch.

## 2. Exact statement and hypotheses

The frozen physical mask is

\[
P_2=\mathbf1_{|d-gm|\le\lceil\sqrt L\rceil}
    \mathbf1_{|d'-gm'|>\lceil\sqrt L\rceil},
\]

imposed before Fourier expansion and height differencing. In plus primitive
coordinates,

\[
2h=v\Delta_+ + U\Delta_- -\kappa(U^2-v^2),
\quad |g\Delta_-|\le\lceil\sqrt L\rceil,
\quad g\Delta_+>\lceil\sqrt L\rceil.
\]

The complete fixed-packet target is

\[
|\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
\ll_{B,C_0,\varepsilon}H_B\mathfrak m\kappa uX^\varepsilon,
\]

followed by the outer (O(L^2X^\varepsilon)) bound. The full (T=0) and
strict (T\ge1) branches, both orientations, actual coefficient vectors,
and one outer real part are mandatory.

## 3. Strategy derivation

Round 194's exact geometry retains (g=O(1)) and a close coordinate on all
of (P_2). Round 195 therefore groups first by ((g,\Delta_-)), resolves
(E<g\Delta_+\le2E), and forms the literal determinant-fibre Gram matrix
before positive norms. The required gain is the full factor
(Y/(H_B\mathfrak m)). The stronger relative-positive-mass contraction is
not the promotion normalization.

## 4. First doubtful or unproved step

No theorem currently controls the exact vector Gram matrix. Its diagonal,
repeated effective phases, endpoint/carry/birth-death vectors, or physical
mask commutator may retain full positive capacity. This is the first
unproved step, and the campaign permits a rigorous scoped no-go.

## 5. Control tests and outcomes

- Graph validation: PASS at the exact starting hash.
- Campaign validation: PASS.
- Prepared plan campaign equals the active manifest deeply: PASS.
- Three task contexts exist; the blind task leaks neither the graph nor the
  proof draft and receives only `protocol.md` plus the isolated statement.
- Round ledger marks Round 194 closed and Round 195 active: PASS.
- Current/next pointers identify the same campaign and graph: PASS.
- Failure ledger is exactly regenerated from the live graph: PASS.
- Structured campaign, ledger, next-plan, validation-matrix, and plan JSON
  parsing: PASS.
- Campaign, strategy, and launch-pointer byte hygiene after replacing the
  two locally transport-corrupted strategy/isolated-statement artifacts:
  strict UTF-8, LF-only, no BOM, no forbidden controls, and formula spot
  checks: PASS.
- Six unit tests, bytecode compilation, and whitespace checks: PASS.
- False controls and no-pivot rules are explicit: unsigned,
  character-erased, phase-aligned adversarial, arbitrary-coefficient,
  separate-orientation, wider-width, extra-Farey, and proper-submask
  escapes are prohibited.

## 6. Dependencies and artifacts used

The launch uses the closed Round-194 synthesis/adjudication, the accepted
Round-193 double-close kernel, the accepted Round-191--192 spectral kernels,
the new strategy file, isolated statement, active manifest, generated plan
and briefs, authoritative graph, ledger, and synchronized proof-state
documents. No numerical theorem evidence is used.

## 7. Recommended state effect

Launch all three tasks. Promote nothing until reports, seam reviews, a
conductor adjudication, and—if warranted—a mechanically valid State Patch
with independent reverse/replay and protected-scope controls are complete.
Quarantine (P_1), all other original-(t) incidences, M1/M2 parents,
endpoint uniformity, M9, both bridges, the quarter theorem, and all
exponents.
