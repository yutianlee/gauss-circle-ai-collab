# Conductor strategy, 2026-08-26: full-proof frontier after Round 166

## Decision

Round 166 closes under `strategy_frontier_retained`.  The sole Round-167
analytic inequality is

\[
 \boxed{
 \Re\mathfrak C_{R_0,2,{\rm opp},\,g<\gamma L}^{\rm rem}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon,
 \qquad R_0=\lceil L\rceil .}
 \tag{167.F}
\]

This is the open Round-165 estimate (165.K17a).  Its selection is a
strategy decision only.  No report or source proves it, no proof status
changes, and no global exponent improves in Round 166.

## Authoritative proof trees

The standard route is

```text
GC-target
`-- Conditional-bridge
    `-- M9
        |-- M9-M1
        |   |-- direct hard/top M1 parent
        |   `-- direct smooth M1 parent
        |-- M9-M2
        |   |-- hard TOP
        |   |-- BAL
        |   `-- UNBAL
        `-- endpoint-uniform blockwise assembly
```

The alternative route is

```text
GC-target
`-- global-M1 alternative bridge
    |-- complete GAR theorem
    `-- M9-M2
        |-- hard TOP
        |-- BAL
        `-- UNBAL
```

GAR replaces the two direct M1 parents only in the alternative total-active
bridge.  It proves neither blockwise `M9-M1` nor standard `M9`.

The current residual work lies strictly below hard TOP:

```text
hard TOP
`-- complete hard-TOP channel assembly
    |-- t=1 residual
    |   |-- (165.K17a), minimal window, open
    |   `-- (165.K26), maximal window, open alternative
    `-- other small-t/intermediate-D channels and near collars, open
```

Thus even a proof of (167.F) closes only the complete residual scalar.

## Why (167.F) remains first

At the minimal scale, the direct opened-incidence positive ledger is
\(L^3X^\varepsilon\), while (167.F) asks for
\(L^2X^\varepsilon\).  The missing saving is one factor \(L\).  At the
maximal scale, fixed-shift Cauchy gives \(L^4X^\varepsilon\) against the
\(L^3X^\varepsilon\) target (165.K26), again missing \(L\), while its
short-shift connector already spends the full \(L^3\) allowance.

The direct residual scalar has a smaller formal deficit \(L^{1/2}\), but
the accepted direct methods return or erase its signed structure and expose
no comparably exact new interface.  A complete hard-TOP shortcut, GAR, the
direct M1 parents, BAL, and UNBAL have greater eventual owner leverage but
contain larger independent unresolved surfaces.  Endpoint uniformity is an
assembly seam, not an independent cancellation theorem.  The separate
\(W=Y^{7/16}\) determinant lane may yield an intermediate exponent but
closes no M9 parent.

## The new, narrowly frozen mechanism

After the exact signed divisor opening, the project equation is

\[
 d'm'-dm=r.
\]

The matrix

\[
 \begin{pmatrix}a&b\\c&d\end{pmatrix}
 =\begin{pmatrix}d'&d\\m&m'\end{pmatrix}
\]

has determinant \(r\).  With \(r=hk\),
\(k=2^{v_2(r)}\), and \(h\) odd, the preliminary determinant, two-adic
gcd, and fixed \(\chi_4(d')\chi_4(d)\) map into the framework of
Grimmelt--Merikoski, arXiv:2404.08502v2, Theorem 10.1.  This matches only
the determinant skeleton.

The first literal source failure is that no admissible automorphic or smooth
representation of the actual selector-dependent multiplier has been proved.
If that is repaired, the next gates are:

1. the square-root phase requires
   \(\delta^{-1}\gtrsim1+Jr/L\), reaching \(J\) on
   \(r\asymp L\);
2. a single admitted test function must retain the variable-\(r\) aggregate,
   rather than specialize to fixed \(r\) and sum absolute errors;
3. the principal main term, \(\mathcal K_+\), every \(\mathcal R_j\),
   two-adic and Möbius sums, cells, endpoints, and completion costs must total
   \(O_{\gamma,\varepsilon}(L^2X^\varepsilon)\).

The 2025 Part-I automorphic-kernel theorem is explicitly non-oscillatory.
Its general form replaces the desired discrepancy by two new positive
selector/phase autocorrelations, while its determinant corollary restores
invariance and smoothness.  It is therefore not a black-box solution.

## Round-167 promotion gate

Promotion is conjunctive:

1. prove an exact multiplicity-preserving determinant dictionary for every
   literal residual incidence;
2. preserve the one outer real part and price every intermediate modulus at
   the target scale;
3. pass the exact Grimmelt--Merikoski coefficient, smoothness, determinant,
   gcd, orbit-correlation, main-term, and restored-power hypotheses, or
   extract the exact literal determinant-kernel statement at the first failed
   source interface;
4. show explicitly which actual selector or character structure defeats the
   phase-aligned arbitrary-coefficient diagnostic;
5. retain every real centre, parity branch, hard crossing, profile, star,
   endpoint, and fixed \(\gamma\); and
6. pass statement-only, source, power/endpoint, and graph-scope reviews.

The phase-aligned array is a control at the unfiltered or filter-erased
Fejer level.  It is not a literal counterexample to the post-opening
`opp, g<gamma L` sector unless an explicit incidence-level lift is built.

## Stop rule and continuation

Round 167 stops at the first exact source-class failure or fixed positive
restored-power loss.  It must not pivot inside the round to (165.K26), the
direct residual scalar, another hard-TOP channel, GAR, BAL, UNBAL, or a
parent theorem.  A rigorous source-to-interface no-go is a successful round
result and is scoped only to that placement.

If the gate succeeds and (167.F) is proved, the next work is the residual
connector and then the remaining hard-TOP channels and collars.  If it fails,
the conductor closes the round and only then compares (165.K26) against a
direct residual reformulation.  After hard TOP, BAL and UNBAL remain
independent.  In parallel proof-tree terms, a complete M1 route and endpoint
assembly are still required before either quarter bridge can close.

The next scheduled full-proof and current-literature reassessment is at the
three-round cadence after Rounds 167--169.  No open result is carried across
that review as accepted mathematics.

## Exponent ledger

- strongest internally proved exponent: \(1/3\);
- source-audited external Li--Yang benchmark:
  \[
  {3292+25\sqrt{1717}\over13762}
  =0.3144831759740614\ldots;
  \]
- target exponent: \(1/4\).

All three entries are unchanged by Round 166.
