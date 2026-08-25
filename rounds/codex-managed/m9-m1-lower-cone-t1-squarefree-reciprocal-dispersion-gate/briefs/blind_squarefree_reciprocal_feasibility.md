# Task brief: blind_squarefree_reciprocal_feasibility

- Campaign: m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate
- Round: 148
- Role: blind rederiver
- Access: statement only
- Starting graph:
  bb43abb1e0fbd719b18ebf91f4c7e477bf18e46e7b5225faaa88a7fb38d31352
- Evidence status: candidate only; do not edit shared state.

## Target

Using only protocol.md and blind_statement.md, independently derive the
strongest true signed squarefree reciprocal estimate compatible with
the statement. Test whether the absolute squarefree \(Q+D\) analogue
is false or too strong, identify the minimal actual outer-coefficient
property needed to beat \(Q\sqrt D\), and prove a target, strict range,
or rigorous countermodel or method no-go.

Do not inspect the proof graph, strategies, proof draft, Round-147
artifacts, or Round-148 sibling work.

## Required controls

Run every blind-task control in state/active_campaign.yml as reproduced
conceptually in blind_statement.md: exact signed versus absolute versus
arbitrary-coefficient forms, Mobius decomposition, near-divisor
multiplicity, dispersion diagonals, \(q\mid N\), \(D=1\), balanced and
unbalanced aspects, profiles, collars, and terminal prefixes.

## Output

Write only:

rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/blind_squarefree_reciprocal_feasibility.md

Use seven sections:

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Control tests and outcomes.
6. Dependencies and artifacts used.
7. Recommended state effect.

A rigorous refutation is a successful result. Do not edit shared state
or any sibling artifact.
