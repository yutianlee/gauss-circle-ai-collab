# Round 179 statement-only primitive-conductor packet

## Isolation

Use only this file and protocol.md. Do not inspect any proof graph, active
campaign, strategy, prior round, sibling report, source file, or conductor
analysis. This packet deliberately withholds the proposed derivation.

## Exact finite kernel

Let \(q\) be odd and

\[
c_q(a)=\frac{2}{q\{1+e(-a/q)\}},\qquad
E_q(x)=(-1)^{[x]_q}
=\sum_{a\bmod q}c_q(a)e(ax/q).
\tag{B179.1}
\]

Define the primitive-frequency projection

\[
K_q(b)=\sum_{\substack{a\bmod q\\(a,q)=1}}
c_q(a)e(ab/q).
\tag{B179.2}
\]

Independently derive an exact divisor formula for \(K_q(b)\), and then
classify \(K_q(b)+K_q(-b)\) for every unit \(b\bmod q\). Track the divisor
\(d=1\) separately.

Now let \(u_0\) be odd, let \(q\mid u_0\), and let
\(B^+_{q,b},B^-_{q,b}\) be two complex bucket arrays supported only on
units \(b\bmod q\). The exact-\(q\) signed block is

\[
\mathcal C_{u_0,q}
=\frac q{u_0}\sum_{b\in U(q)}
\{K_q(b)B^+_{q,b}+K_q(-b)B^-_{q,b}\}.
\tag{B179.3}
\]

Each bucket array comes from disjoint orientations of one literal finite
sum. For each fixed \((u_0,q)\), the total number of contributing atoms in
either orientation is \(O(u_0L)\), and every atom has magnitude
\(O(X^\varepsilon)\). The outer problem sums \(q\mid u_0\) and
\(u_0\mid u\), so divisor factors are harmless.

## Required task

1. Derive the exact primitive projection formula and its sign-reversal
   law without assuming the answer.
2. Decompose (B179.3) into the smallest exact symmetric/trace component
   and the remaining orientation-defect component.
3. Prove the sharp absolute capacity of the symmetric/trace component
   after summing divisor labels.
4. Decide what, if anything, follows for the defect from the finite kernel
   alone. Test arbitrary and adversarial bucket arrays and distinguish a
   universal algebraic statement from a theorem about the undisclosed
   literal coefficients.
5. State the narrowest exact lemma or no-go result, the first unproved
   step, and what additional relation between \(B^+\) and \(B^-\) would be
   sufficient.

Do not infer a parent theorem or exponent. Computation is unnecessary and
cannot certify the asymptotic application.
