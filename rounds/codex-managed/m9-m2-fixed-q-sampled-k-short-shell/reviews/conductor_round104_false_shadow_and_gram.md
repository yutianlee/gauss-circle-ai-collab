# Round 104 conductor false-shadow and Gram review

Starting graph SHA-256:
`d2502a33224fbcb1fe3b8ffe0ea1227b953112fa0c98216597e8b0ccfa887372`

## Exact Cauchy count

With zero extension,

\[
 \left|\sum_{0\le h<H}(-1)^hF_a(n+h)\right|^2
 \le H\sum_{0\le h<H}|F_a(n+h)|^2.
\]

After summing \(n\), each fixed row \(F_a(q)\) occurs in exactly \(H\)
translated windows away from the harmless zero boundary, and at most
\(H\) in all cases. Hence

\[
 \mathcal G_H^{\rm act}
 \le H^2\sum_{a,q}|F_a(q)|^2.
\]

The row theorem therefore loses \(D^2\), not \(D\), against the canonical
Gram target.

## Sharp coefficientwise false analogue

The sequence

\[
 \widetilde F_a(q)=(-1)^q{L^2\over A}
\]

on an \(A\)-by-\(D\) rectangle obeys the proposed pointwise row size but
satisfies

\[
 \sum_{0\le h<H}(-1)^h\widetilde F_a(n+h)
 =(-1)^nH{L^2\over A}.
\]

Thus its Gram is

\[
 \asymp {H^2DL^4\over A},
\]

which saturates the Cauchy ledger. This is an arbitrary-row false shadow,
not an actual-symbol counterexample. It proves only that the uniform row
bound, the visible \((-1)^q\) character, and coefficientwise inequalities
cannot produce a polynomial \(D\)-saving.

## Scope

For \(D\le(\log X)^C\), the false-shadow loss is still swallowed by
\(X^\varepsilon\), so the short-shell theorem is compatible with this
control. For polynomial \(D\), the actual coefficient must supply a new
signed \(q\)-correlation or a stronger averaged row theorem. No actual
lower obstruction is asserted.
