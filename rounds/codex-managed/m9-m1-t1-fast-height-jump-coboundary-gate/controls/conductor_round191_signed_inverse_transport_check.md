# Round 191 signed-inverse transport diagnostic

## Purpose and limitation

This bounded Wolfram check tests the exact signed-least-inverse transport,
its canonical carry, the pre-Fourier parity ratio, and the inverse-class
count used by the proposed strict sector.  It is diagnostic only.  It
does not prove a uniform asymptotic estimate, literal support density, or
cancellation in the large-inverse complement.

## Exact formulas tested

For every tested odd \(U\), every unit \(v\bmod U\), and the signed least
inverse \(\varrho\), define \(\gamma\) by

\[
 \varrho v-\gamma U=1.
\]

For both orientations, the check verifies

\[
 (S,w)\mapsto
 (S-\epsilon_\omega\varrho,w-\epsilon_\omega\gamma)
\]

from the height-\(h\) determinant fibre to height \(h-1\), including the
canonical affine reindexing \(t\mapsto t+\nu_\omega(h)\) with
\(\nu_\omega(h)\in\{-1,0,1\}\).  It also verifies that the complete
pre-Fourier parity ratio is \((-1)^\varrho\) in both orientations.

For every \(0\le R\le(U-1)/2\), it verifies the exact unit-class count

\[
 \#\{v\bmod U:0<|\varrho_U(v)|\le R\}
 =2\sum_{\substack{1\le r\le R\\(r,U)=1}}1.
\]

## Parameters and output

- transport/parity: every odd \(3\le U\le41\), every unit \(v\),
  \(1\le h\le3U\), both orientations, and \(-3\le t\le3\);
- inverse-class counts: every odd \(3\le U\le101\) and every admissible
  cutoff \(R\).

Command:

    wolframscript -file rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/controls/signed_inverse_transport_check.wls

Runtime output:

    ROUND191_SIGNED_INVERSE_TRANSPORT_DIAGNOSTIC
    transport_and_parity_checks=420672
    inverse_class_count_checks=1325
    failures=0
    interpretation=diagnostic_only

Outcome: **PASS**, with 420,672 exact transport/parity checks, 1,325
exact inverse-class-count checks, and zero failures.

## Evidence scope

The code checks finite exact algebra only.  The asymptotic multiplicity
bound in the literal \(v\)-interval, the \(m^{-1}\) lift, the divisor
ledger, and every endpoint/mask correlation remain analytical matters.
