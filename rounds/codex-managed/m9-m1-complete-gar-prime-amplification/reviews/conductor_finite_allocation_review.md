# Round224 conductor finite allocation review

## 1. Result

GREEN for the finite identities and the narrowly scoped scalar-identity
control. This is a claimant-avoiding review of the frozen statement-only
report. It does not certify a complete GAR estimate.

## 2. Exact statement and hypotheses

An arbitrary array \(A:\mathbb N^2\to\mathbb C\) is contracted against
\(\chi_4(q)\) on \(hq=n\); \(F\) has finite support. For odd \(p\),
\(\epsilon=\chi_4(p)\), \(\lambda=1+\epsilon\). The definitions of
\(U,V,W\), the backward coefficient zero convention and the bilinear
pairing are exactly those in the reviewed report. No angular application
is assumed in this finite statement.

## 3. Independent check

Partitioning factorizations of \(pn\) into \(p\mid h\) and \(p\mid q\)
gives \(c_A(pn)=c_{VA}(n)+\epsilon c_{UA}(n)
-\epsilon c_{WA}(n/p)\). The intersection exists only if \(p\mid n\).
At valuation \(r\), the first allocation counts exponents \(1,\ldots,r+1\),
the second \(0,\ldots,r\), and the overlap \(1,\ldots,r\); each original
term remains once. Subtraction of \(\lambda c_A(n)\) and addition of
\(\epsilon c_A(n/p)\) give the claimed defect.

Reindexing \(m=pn\) in the forward coefficient term and \(n=pm\) in the
backward term verifies the stated adjoint and its minus-defect sign.
All sums remain finite. Direct substitution in the radial test gives
the factors \(p^{3/4}\), \(\epsilon p^{-3/4}\), cutoff \(p\lfloor N\rfloor\)
with divisibility, and cutoff \(\lfloor N/p\rfloor\). The array stays
fixed while the wave parameter changes. Empty supports and integral
terminal samples are correct.

For \(A=1\), the prime-power sum is \(\sum_{j=0}^r\epsilon^j\), whose
second-order recurrence is verified directly, including \(r=0\) with
the backward value zero. Inert primes have eigenvalue zero and cannot
be inverted. At 2, only odd second coordinates contribute, leaving the
single first-coordinate allocation and no backward term.

For split primes and \(F=\delta_1\), \(T_p^*F=\delta_p\) and \(c_1(p)=2\).
Thus the contracted sum and its coefficient triangle are both twice
the number of primes. Cauchy also has equality after both vector norms
are retained. The elementary infinitude argument using a prime divisor
of \((2\prod p)^2+1\) is valid: that divisor is odd, new, and admits an
element of order four. This controls an automatic scalar amplification
claim, not the actual angular radial family or all possible methods.

## 4. First doubtful or unproved step

No gap in these finite identities was found. Cross-prime cancellation,
control of the actual profile defect and a complete signed estimate
remain absent. The finite one-point example does not refute them.

## 5. Controls and outcome

GREEN for overlap at all valuations, the adjoint sign, inert and 2-adic
cases, exact integer cutoffs, constant-profile recurrence and the
one-point norm accounting. These are algebraic controls; no mathematical
experiment was run.

## 6. Dependencies and exact artifacts

Conductor reviewer, round224, 2026-09-28. Current isolation was preserved
by the reused derivation agent; historical memory is explicitly disclosed.
The conductor is not the claimant of that report.

- reports/blind_prime_allocation.md:
  468e3a453090e05a36f696f9cfaa3474340ee06ba8ddc8d3049e059cca75e616.
- briefs/blind_prime_allocation_statement.md:
  9d11e4a9c11a6a1e5728c20faad3ba3eee091cc0290ab97db8872802a402bdef.
- protocol.md:
  f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.

All relative paths above are in
rounds/codex-managed/m9-m1-complete-gar-prime-amplification except protocol.
No external theorem is needed.

## 7. Recommended state effect

Retain scoped finite evidence. No new complete estimate, graph change,
owner closure or successor follows.
