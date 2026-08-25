# Final green source confirmation for the Round 143 conductor candidate

## 1. Result

**Final verdict: GREEN.**  Both last remnants are fixed.  Equation
(143.C19) contains U+005C immediately before “qquad”, and the
Deshouillers--Iwaniec sentence now explicitly assumes
\(\varepsilon>0\).  No source repair remains.

## 2. Exact statement and hypotheses

The candidate now correctly records the Kıral--Young even-character
boundary; the exact Blomer--Milićević level-\(4\) minus level-\(8\)
identity and Gauss factor; the full \(H+M+E\) ledger, singular cusps, and
oldclasses; the same-sign transforms; the \(2n\)-versus-\(4n\) sample
normalizations; the discretely qualified Linnik range; and the complete
BM, DI, and ABL hypotheses used at the interface.

## 3. Verification

The raw bytes of (143.C19) contain byte 92 (U+005C) immediately before
the letters “qquad”.  The DI paragraph states \(T\ge1\),
\(N\ge1/2\), \(\varepsilon>0\), the common sequence, and \(Y\ge1\)
for the exceptional theorem.  The candidate contains no stray control
byte or carriage return.

## 4. First doubtful or unproved step

There is no remaining doubtful source attribution or normalization.
The first unproved mathematical step is the candidate's stated project
gap: an owner-saving common-test, common-sequence, or vector-valued estimate
for the fully gcd-restored nonzero-frequency joint matrix.

## 5. Required controls and outcomes

KY parity, BM identity and \(\tau(\chi_4)=2i\), level-\(4/8\) spectrum,
cusps and oldclasses, same-sign transforms, \(2n/4n\) samples, Linnik
discreteness, DI hypotheses, ABL hypotheses, and TeX/control-byte hygiene
all pass.

## 6. Dependencies and exact artifacts used

This confirmation checked
candidates/conductor_round143_level_four_matrix_obstruction.md against
reports/kuznetsov_source_hypothesis_audit.md,
reviews/source_conductor_candidate_final_audit.md, and
reviews/source_conductor_candidate_green_confirmation.md.  No candidate,
shared-state, or proof-graph file was edited.

## 7. Recommended state effect

Mark the candidate's source audit GREEN.  Its scoped source-boundary and
joint-matrix obstruction are promotion-ready, while the quarter-bound and
all downstream obligations remain open.
