# Round216 NONBLIND cross-check of the original radical report

Campaign: `gc-actual-radical-high-values`.
Reviewer role: independent NONBLIND mathematical cross-check.
Date: 2026-09-28.
Reviewed report: `reports/actual_radical_tail.md`.
Exact report SHA256:
`f8c6ff6b2ecd0f5b5458d63856d4615967d7442fe693e39c9633c5b61b56a954`.
Comparison candidate SHA256:
`d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee`.
No experiments, source expansion or shared-state edits.

## 1. Result

**GREEN.** The original report is mathematically sound at the stated
hash and reconciles with the already reviewed conductor candidate.
No mathematical correction is required. It proves the collective
repeated-class error and the complete bound equivalence, while keeping
the distinct-class correlation and H216 open. It claims no unsupported
complete actual moment or pointwise gain.

## 2. Exact statement and hypotheses

The report uses the same fixed mollifier, real cosine phases, actual
\(r_2\) coefficients, real \(T\ge2\), smooth positive-radius
window, integer \(Q=\lfloor T^{2/5}\rfloor\), and threshold
\(V_0=T^{13/125}\) as the candidate. All harmonics \(s\ge1\)
are included in every class wave. Its coefficient masks depend on
\(n,T\), never on the radius.

Its principal error bound is
\(T^{4/5+\epsilon}+T^{8\beta-1/5+\epsilon}\). Because
\(\beta>1/8\), the second term absorbs the first after harmless
constant and epsilon adjustments. Thus this is the same final error
power as the candidate, rather than a conflicting weaker frontier.

## 3. Proof and reconciliation

The head comparison \(r_2(ds^2)\le r_2(d)\tau(s^2)\),
\(\|L_Q\|_\infty\ll Q^{1/4}\), masked distribution, and
\(M_{12}(L_Q)\ll T^{15/13+\epsilon}\) are the same valid
arguments checked in the candidate seam. The complete tail supremum
is derived specifically from \(B_T-L_Q\). For any fixed \(p>q\),
the last moment contribution has power \(1+(p-q)\beta\), which
is smaller than \((p-2)\beta\) because \(\beta(q-2)>1\).
This verifies the report's extension to every fixed \(p\ge2\)
without asserting uniformity for \(p\) growing with \(T\).

The formal generating-function proof of the finite class identity is
correct at each fixed degree and needs no convergence of an analytic
logarithm. Its exact partition estimate (14) matches the candidate's
(D13). The original report then deliberately uses the coarser bound
\(Q^{-(12-r)/4}|Z_Q|^r\). Its exponents (17) consequently omit
the candidate's extra \(-1/5\) for odd singleton count. This is a
valid upper bound: the odd exponent, and any configuration with fewer
than the maximal number of nonsingleton blocks, is only smaller.
The maximal powers remain \(4/5\) and \(8\beta-1/5\), at
\(r=10\). The binomial estimate (15) also accounts for every such
monomial; its constant term integrates to \(TQ^{-3}\).

The event constants are correct: \(|B|>V_0\) implies
\(|Z|>V_0/2\) and \(|B|\le2|Z|\); conversely,
\(|Z|>2V_0\) implies \(|B|>V_0\) and
\(|Z|\le(4/3)|B|\). Distribution estimates pay the intervening
strip and low values. Complete power inequalities then give the
two-way transfer without deleting mixed terms. The small additive
error compares the distinct-class integral to \(M_{12}(Z)\), not
to \(M_{12}(B)\).

The extra exact-resonance estimate (18) is a valid application of the
accepted kernel: \(S_Q\ll Q^{-1/2+\epsilon}\) gives
\(T S_Q^6\ll TQ^{-3+\epsilon}\), and even constant-coefficient
nonnegativity applies to the real masked series. It does not assert
finite-radius independence.

The separation test is also correct. The product of the \(2^{11}\)
linear factors is invariant under every radical sign change, hence
is an integer polynomial in their squares. It is a nonzero integer
by distinct-class independence. Bounding its other \(2047\)
factors by \(12\sqrt U\), with \(U=T^{3/2}\), gives
\(T|\Delta|\ge12^{-2047}T^{-6137/4}\). The report correctly
identifies this as insufficient for uniform Fourier decay, without
claiming that an actual tuple attains the bound.

## 4. First doubtful or unproved step

No new gap in the original reduction was found. The remaining open
step is its signed estimate (2), with literal expansion (19).
Neither exact radical independence nor the paid repeated-class
configurations prove it. The report correctly warns that multiplying
the smooth window by the high-event indicator would not preserve
Schwartz Fourier decay; its proved complete-moment equivalence avoids
that unsupported step.

## 5. Controls and outcomes

* **Partition costs — PASS.** The original coarser ledger dominates
  the candidate's exact parity-sensitive ledger; both give the same
  final maximal exponent since \(8\beta>1\).
* **All indices and tails — PASS.** For fixed \(T\),
  \(\sum_d A_d<\infty\) justifies the uniform finite-to-infinite
  polynomial passage with every harmonic retained. The extra
  truncation used only for the separation test costs at most
  \(T\cdot O(T^{-K})\cdot O(T^{1/4+\eta})^{11}
    =O(T^{15/4+\epsilon-K})\), including all tail-containing
  tuples by a fixed union bound.
* **Signs and physical anchor — PASS.** The full Fourier expansion
  has all \(2^{12}\) signs, phase
  \(2^{-12}e(-3\sum\varepsilon_i/8)\), and
  \(T\widehat w(-T\Delta)\). No selected sector is asserted
  nonnegative.
* **Actual versus certificate bounds — PASS.** Collective signed
  regrouping is distinguished from the termwise absolute Fourier
  expansion. Both inherited high-level costs are retained, and no
  upper-bound diagnostic becomes an actual lower obstruction.
* **Scope — PASS.** The distinct-class estimate remains open; even
  proving it at this order yields only \(102/325\), not the full
  quarter theorem or any independent M1/M2/GAR parent.

## 6. Dependencies and exact artifacts used

The only newly read artifact was the original report at the hash
recorded above. This review also used the candidate already reviewed
at its recorded hash, the accepted201 exact-resonance kernel, and
the permitted original protocol/graph/accepted204 context.
No other sibling, blind document or conductor ledger was read.
The earlier candidate review and original assigned report were kept
unchanged. All checks were analytical; no numerical experiment or new
source import was used.

## 7. Recommended state effect

**GREEN** as provenance and mathematical evidence for the narrow
candidate reduction. No change to the accepted complete moment
power, pointwise benchmark or open target follows from this report.
Any narrow promotion remains the conductor's responsibility after
the required validation and State Patch. This verdict binds only the
report hash
`f8c6ff6b2ecd0f5b5458d63856d4615967d7442fe693e39c9633c5b61b56a954`.
Stop this cross-check here without modifying either reviewed artifact.
