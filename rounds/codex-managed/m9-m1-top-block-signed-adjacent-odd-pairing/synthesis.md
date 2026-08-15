# Round 57 synthesis: adjacent character pairing leaves the signed hyperbola sum

## 1. Conductor decision

Round 57 closes with an exact adjacent-odd decomposition and a sharp
scoped no-go.  Pairing \(q\) with \(q+2\) is lawful only on two-point
rows and cannot by itself produce the missing square root.  No high-shell
estimate or exponent is proved.

## 2. Exact row identity

On \(R/4<h\le R/2\), a length-\(R\) product window contains at most two
odd denominators for a fixed \(h\).  The two-point case is uniquely
\(q,q+2\), giving

\[
 \chi_4(q)e(\sqrt{Xhq})
 \{\mathcal A_X(h,q)-\mathcal A_X(h,q+2)e(\Theta_h(q))\},
\]

\[
 \Theta_h(q)={2\sqrt{Xh}\over\sqrt{q+2}+\sqrt q}\asymp hR.
\]

Every one-point row remains a full unmatched term.  Pair availability is
an exact two-edge alignment condition, not a consequence of \(2h\le R\).

## 3. Capacity obstruction

The paired bracket splits into an actual-amplitude difference plus
\(\mathcal A(h,q+2)(1-e(\Theta))\).  The smooth amplitude difference
totals \(O(1)\), but profile/star seams remain explicit and the phase
factor has no automatic smallness modulo one.

For infinitely many \(X=K^4\), a strict top-profile length-\(K\) window
has \(\gg K=R\) unmatched rows, each with amplitude at least \(1/2\),
and no star or endpoint ambiguity.  Hence post-pair absolute values retain
\(R\) capacity against the \(\sqrt R\) target.

## 4. Remaining theorem

The high shell still requires a signed cross-\(h\) estimate for the full
matched-plus-unmatched decomposition.  The selector

\[
 q_h=\min\{q\ \text{odd}:hq\ge A\}
\]

is a discontinuous hyperbola-floor function, so the surviving phase is a
signed sawtooth/product-fibre sum.  A new theorem must exploit this joint
arithmetic structure before absolute values.

## 5. Rejected shortcuts

- Not every occupied row has an adjacent partner.
- \(\chi_4(q+2)=-\chi_4(q)\) gives a difference, not automatic smallness.
- Artificial completion endpoints are full owners, not inherited stars.
- Fixed-row sampled BV does not control the outer signed \(h\)-sum.
- The strict unmatched-mass witness is not a signed counterexample.

## 6. State effect

Promote the exact decomposition and the post-pair absolute-capacity
obstruction.  Retain the high shell, lower shell, GAR, alpha transfer,
M9-M1, M9, and the target open.  The unconditional exponent is unchanged.

## 7. Next strategy

Work directly with the signed high-shell hyperbola selector.  The next
round should derive its exact floor-sawtooth/Fourier representation and
test a two-variable cross-\(h\) estimate, including zero Fourier mode,
truncation error, top plateau, and fourth-power resonances.  Do not return
to local pair counting or residuewise absolute values.

