# Conductor Round 117 closing controls

Campaign: `gc-w7-16-actual-determinant-fibre-gate`

## Mathematical controls

- Exact increment: \(ab'-a'b=aq-bp\), with the strict one-sided
  orientation retained.
- Character placement: M1 has \(q=2r\), \((-1)^r\); M2 has
  \(p=2s\), \((-1)^s\), and \(\kappa_2=4\).
- Product-window layer cake: the number of denominators with norm below
  \(\eta\) is \(O_\varepsilon((1+\eta D)Y^\varepsilon)\); summation gives
  \(O_\varepsilon(DY^\varepsilon)\).
- Random cells: \(O(1+WL/D)\) occupied cells times squared cell amplitude
  \(D^2/L^2\) gives (117.S1).
- Top-shell curvature: a divisor progression has length \(Q_*/\rho\),
  second derivative \(\lambda\rho^2\), and weighted bound
  \(L^{-1}(Q_*\sqrt\lambda+(\rho\sqrt\lambda)^{-1})\).
- Minimax arithmetic:
  \[
   43/48-37/48=1/8,\qquad
   43/48-35/48=1/6,
  \]
  while \(37/48-1/2=13/48\) and
  \(35/48-1/2=11/48\).
- Adversary: phase conjugation removes the reciprocal curvature phase and
  therefore fails the actual finite-lift BV hypothesis used by (117.S2).
- Transform scope: the Legendre dual is again a ratio phase; its standard
  norm diagonal is \(Y^{43/48}\), and no actual lower bound is claimed.
- Product scope: the two literal truncated coefficients differ; only the
  unweighted completion is \(r_2/4\).

## Artifact and state controls

- State Patch dry run: passed for three created nodes, three updated nodes,
  and eight rejected shadows.
- Campaign validation: passed with the campaign marked complete.
- Unit tests: six of six passed with `python -m unittest discover -s tests -v`.
- Campaign artifacts: strict UTF-8, LF-only, no C0 controls, no trailing
  whitespace, and exactly seven numbered sections in each of the three
  required reports.
- `git diff --check`: exit code zero; only workspace line-ending warnings
  were emitted.
- Numerical work: none. The round allocation was entirely analytical,
  algebraic, and source-audit work.

## Promotion guardrail

Only (117.S1), (117.S2), and the scoped transform-and-norm obstruction are
eligible for promotion. The \(Y^{1/2}\) correlation, complete local moment,
pointwise exponent improvement, M9-M1, M9-M2, endpoint uniformity, M9, and
the quarter theorem remain open.

