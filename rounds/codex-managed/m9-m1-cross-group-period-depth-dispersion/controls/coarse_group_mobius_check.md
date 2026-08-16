# Round 88 diagnostic: coarse-group divisor lattice

Evidence level: diagnostic only.  This finite check can falsify the
combinatorial formulas but cannot certify an asymptotic estimate.

## Code and command

Code:

rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/controls/coarse_group_mobius_check.py

Command:

python rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/controls/coarse_group_mobius_check.py

## Parameters

The check enumerated every ordered pair of distinct units for

\[
 M\in\{12,18,27,40,72\}.
\]

For every divisor \(R\mid M\), it compared:

1. the number of ordered physical-pair pairs that have the same
   Round-87 active-set/active-label group after reduction modulo
   \(M/R\);
2. the sum of exact first-coincidence shell counts over \(s\mid R\).

It also checked the finite counting inequality

\[
 \sum_\gamma \#\{P:\Gamma_{M/R}(P)=\gamma\}^2
 \leq M^2R^2
\]

and the \(M=27\), \(R=3\) hostile physical-label coincidence.

## Output

All identities and inequalities passed.  The hostile pair

\[
 P_1=(1,2),\qquad P_2=(19,2)\pmod {27}
\]

has different full groups modulo \(27\) and the same active label
\((1,2)\) modulo \(9\), hence first coarse quotient \(R=3\).

## Limitations

- Only small finite moduli were tested.
- The script checks group combinatorics, not normalized row bounds,
  Fejer analysis, source hypotheses, or asymptotic exponent estimates.
- It does not identify every functional additive period with a coarse
  congruence shell.
