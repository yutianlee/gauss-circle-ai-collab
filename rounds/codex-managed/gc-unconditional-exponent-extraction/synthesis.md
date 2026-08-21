# Round 91 synthesis

## 1. Objective and outcome

Round 91 extracted the strongest exponent supplied uniformly by the
accepted direct M1/M2 menu and assembled it through the exact
hyperbola--Vaaler reduction. The result is

\[
 \boxed{P(X)\ll_\varepsilon X^{1/3+\varepsilon}}
\]

for every real \(X\geq2\).

This is the first unconditional global exponent theorem instantiated in
the current claim graph. It is not the target exponent \(1/4\), and it is
not a new record relative to the classical literature.

## 2. Exact block envelope

For every active actual M1 or M2 frequency block,

\[
 B_i(D,L;X)\ll_\varepsilon X^\varepsilon(1+D/L)
\]

and

\[
 B_i(D,L;X)\ll_\varepsilon X^\varepsilon
 \left\{(LX/D)^{1/2}+D^{3/2}(LX)^{-1/2}+1\right\}.
\]

Put \(R=D/L\). If \(R\leq X^{1/3}\), use the first bound. If
\(R\geq X^{1/3}\), then

\[
 (X/R)^{1/2}\leq X^{1/3},
 \qquad
 D(R/X)^{1/2}\leq X^{1/4},
\]

because \(R\leq D\leq X^{1/2}\). This proves the one-third envelope.

The derivation retains the actual \(1/h\) Vaaler coefficient, both
frequency signs, M1's spatial character, M2's two quarter shifts and
frequency character, the height floor, and the hard top sampled-BV
profile.

## 3. Pointwise Fejer residual

For \(H_D\asymp DX^{-1/4}\) and
\(\Delta=D/H_D\asymp X^{1/4}\), positivity and exact product grouping
give

\[
 {1\over H_D}\sum_{d\asymp D}|w_D(d)|K_{H_D}(X/d)
 \ll_\varepsilon X^\varepsilon
 \sum_{n\asymp X}\min\left(1,{\Delta^2\over|X-n|^2}\right)
 \ll_\varepsilon X^{1/4+\varepsilon}.
\]

The shifted legs use \(n=d(4m-\rho)\), \(\rho=1,3\). Exact products take
weight one, and the integer Vaaler jump is matched exactly. The far tail,
floors, half-open shells, and top cutoff are target-safe. This is a
pointwise real-\(X\) proof, not a mean-square argument.

## 4. One-count assembly

The bottom denominator remainder has \(O(X^{1/4})\) terms and is bounded
before Vaaler. The active denominator partition is exact, with one top
profile. Each active Vaaler polynomial has a bounded-overlap dyadic
frequency partition. The main blocks cost \(X^{1/3+\varepsilon}\), the
residuals cost \(X^{1/4+\varepsilon}\), and the \(O(\log^2X)\) assembly
cost is absorbed into \(X^\varepsilon\). H1-H3 then gives the theorem.

The transformed endpoint cones are not used in this direct proof.

## 5. Sharpness of the accepted menu

At \((\delta,\ell)=(1/2,1/6)\), T2S and the first
second-derivative term both have exponent \(1/3\). The remaining menu
entries are \(1/6\), \(0\), \(1/2\), and

\[
 {770\over1923}>{1\over3}
\]

for the audited TTY main term. Hence \(1/3\) is the exact minimax output
of the accepted menu. This is route sharpness only.

## 6. Validation gates

All three reports have exactly seven sections, are byte-clean, and agree:

- the statement-only derivation proves the frozen implication;
- the assembly report rederives the literal full block and one-count
  proof;
- the hostile report certifies small curvature, exact products, hard-top
  BV, dependency status, and menu optimality.

The conductor independently reproduced the block case split and the
positive lattice-tail estimate. No numerical experiment or new external
source was used.

## 7. State decision and remaining proof

The State Patch has promoted R5-Full-reconciliation and R5-Full to
proved internal status and created the direct one-third envelope, its
menu-optimality certificate, and the unconditional partial Gauss
theorem. The resulting graph SHA-256 is
`1bc91c527bfe3595436497483aeb058d4a3b3e87c073931f8517b53df24fe0e5`.

Retain M9-M1, M9-M2, M9, endpoint uniformity at exponent \(1/4\), the
conditional one-quarter bridge, and GC-target as open. The full proof
still requires a strict signed gain on the canonical M1 actual-symbol Gram
operator and on the M2 signed cross-row density--discrepancy energy,
followed by endpoint and final assembly at the \(1/4\) scale.
