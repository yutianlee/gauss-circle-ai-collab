# Round 147 terminal hostile power reread

## 1. Result

**ONE EXACT REMAINING CORRECTION; otherwise GREEN.**

The repaired conductor candidate now correctly:

- qualifies (147.C5) and (147.C35)--(147.C37) as fixed-order capacity
  statements;
- places (147.C6) and (147.C40) on the exact unitary order
  \(z=i(\tau+t/2)\), with only a harmless
  \(|\Re z|\ll1/\log X\) alternative;
- uses the true physical cutoff
  \(K_F=\lfloor\sup\operatorname{supp}F\rfloor=O(M)\) in the exact
  convolution and proves cancellation separately for every
  \(k>K_F\);
- attributes \(M=R^{4/3}\) to the minimum of the primal and reciprocal
  prices, not to the \(q\)-average alone;
- truncates the missing signed correlation (147.C44) at \(k\le K_F\);
  and
- limits graph promotion to fixed-order identities and the scoped
  method no-go, with no target or exponent change.

The only remaining literal defect is that the left side of (147.C40)
still reads \(\sum_k\).  It must read

\[
\sum_{k\le K_F}|h_z(k)|
\min\!\left(\frac Mk,RM^{1/4}\right).
\tag{147.G1}
\]

Equivalently, the sentence immediately before (147.C40) may explicitly
declare that every \(k\)-sum in the power ledger is restricted to
\(k\le K_F\).  This is a notation/scope repair only; it does not alter
the bound.

## 2. Exact statement and hypotheses

The terminal audit interprets the candidate on the unitary
ratio/Fourier decomposition (147.C12b)--(147.C12c), for a compact
physical test \(F\) and the finite convolution (147.C29).  Thus the
actual channel set is

\[
1\le k\le K_F,\qquad K_F=O(M).
\]

For \(k>K_F\), the primal sum vanishes and (147.C27) makes the polar and
dual terms cancel for that same \(k\).  Such indices cannot be counted
as independent resonant channels.

## 3. Verification

The repaired raw and weighted prices remain

\[
\frac Mk,\quad RM^{1/4}
\qquad\text{and}\qquad
\frac{M^{1/4}}k,\quad\frac R{\sqrt M},
\]

respectively.  Their crossover is \(k_0=M^{3/4}/R\).  Restricting
(147.G1) to \(k\le K_F\) can only decrease the candidate's displayed
majorant.  Powerful counting therefore still gives

\[
\begin{cases}
M^{1/4+\varepsilon},&M\le R^{4/3},\\
R^{1/2+\varepsilon}M^{-1/8},&R^{4/3}\le M\le R^2,
\end{cases}
\]

after physical normalization.  The excess remains \(R^{1/3}\) at
\(M=R^{4/3}\) and \(R^{1/4}\) at \(M=R^2\).

The bare lemma (147.C41) retains its necessary \(Q\le N/4\) hypothesis.
The project range \(Q\le R^2\ll N\) satisfies it.  Its ratio to the
required \(RD\) scale is \(R/\sqrt M\); only its minimum with
\(M^{1/4}\) produces the \(R^{4/3}\) crossover.  The Möbius-triangle
bound (147.C43) remains \(QD^{1/2}+D\), an upper-bound limitation of
that method and not a lower bound.

## 4. First doubtful or unproved step

After the notation repair (147.G1), the first mathematical seam is
unchanged: uniform growing-order Bessel analysis for the exact
unitary orders and moving prefixes.  Granting it, the first missing
power is the truncated signed correlation (147.C44).  No target bound
or strict top range follows.

## 5. Controls and outcomes

| Item | Outcome |
|---|---|
| Fixed-order qualification | **GREEN.** Explicit in (147.C5) and after (147.C37). |
| Unitary/small-\(c\) power hypothesis | **GREEN.** Explicit before (147.C39). |
| Finite physical convolution | **GREEN.** Equation (147.C29) uses \(k\le K_F\). |
| Per-\(k\) tail cancellation | **GREEN.** Explicit after (147.C30). |
| Power-ledger notation | **REPAIR.** Add \(k\le K_F\) to (147.C40). |
| \(q\)-average crossover | **GREEN.** Correctly stated after (147.C42). |
| Signed gate | **GREEN.** Equation (147.C44) is truncated and retains the actual orders. |
| Method no-go versus lower bound | **GREEN.** The candidate preserves the distinction. |
| Graph and exponent scope | **GREEN.** No downstream owner or exponent is promoted. |

## 6. Dependencies and scope

This terminal reread used only the current conductor candidate.  Its
scope exclusions are correct: the \(t=1\) target, every \(t\ge2\)
layer, the Round-138 cross, the complete lower scalar, M1 and M2
parents, \(M9\!-\!M1\), \(M9\!-\!M2\), endpoints, M9, the bridge,
the quarter target, and any exponent improvement remain open.

## 7. Promotion verdict

**Verdict: GREEN immediately after the single correction
\(\sum_k\mapsto\sum_{k\le K_F}\) in (147.C40).**

No other mathematical or scope correction is required by this terminal
power reread.  After that edit, the exact fixed-order reduction and
\(\mathsf{squarefree\_H\_resonance\_no\_go}\) may be promoted in the
strictly scoped form stated by the candidate.
