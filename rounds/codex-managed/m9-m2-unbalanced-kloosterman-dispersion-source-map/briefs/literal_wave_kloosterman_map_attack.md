# Task brief: literal_wave_kloosterman_map_attack

- Campaign: `m9-m2-unbalanced-kloosterman-dispersion-source-map`
- Round: 135
- Role: discovery
- Graph SHA-256: `f9aa6fa43900b9cb73f705405f9a6090e6e84fb5d3c8a9e037ffe3c6911b9ea0`
- Evidence status: candidate only; do not edit shared state.
- Allocation: 100% analytical/algebraic work, 0% numerical experimentation.

## Objective

Start from both literal formulas for \(\mathscr R_{D,L}(X)\). Construct the
strongest exact owner-preserving map to a Bettin--Chandee/Wright
Kloosterman-fraction or dispersion form. If no map closes, prove the first
failure and quantify every legal degenerate specialization and completion
cost. The desired output is a theorem or a rigorous scoped no-go, not a
method analogy.

## Required context

Read completely the context files listed for this task in
`state/active_campaign.yml`, including the Round-107 return, Round-118
synthesis and square-sector seam, the Round-135 blind statement, and the
primary-source manifest.

## Required analysis

Treat separately:

1. `m=1,n=r,a=k` in the inverse-fraction theorem;
2. `k -> inverse(m) mod r` on a length-\(K\) interval;
3. completion of that sparse inverse image to full residues;
4. separation of \(q_L(4Xk/r^2)\);
5. integer and noninteger \(X\);
6. the physical condition \(r\mid s\), shifted residues around the real
   centre, and any independent-modulus dispersion formulation;
7. exact placement of \(\chi_4\), pointwise modulus, and source norms; and
8. the full exponent polytope.

Any strict reduction must be noninvertible, retain the centre and all moving
profiles, and be smaller than the existing \(\Delta=D/L\) capacity by the
power needed for \(X^{1/4}\). A source theorem that estimates a different
average is a no-go for direct import, not a counterexample to the project
wave.

## Output contract

Write only
`rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md`.
Use exactly seven numbered sections:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect.

Recommend one of `promote`, `retain`, `revise`, `reject`, or `no change`.
Do not edit shared state or the synthesis.
