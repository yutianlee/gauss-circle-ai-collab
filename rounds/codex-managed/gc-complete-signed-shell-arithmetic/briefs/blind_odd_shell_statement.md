# Round 206 isolated mathematical statement packet

Task: blind_odd_shell_bridge. Role: independent statement-only rederivation.
Read only this packet and protocol.md. Do not read graph, manifest,
strategy, predecessor or sibling/claimant reports. No external sources
or numerical experiments are needed. Write only
rounds/codex-managed/gc-complete-signed-shell-arithmetic/reports/blind_odd_shell_bridge.md.
Use the seven-section research report contract; stop after your report.

## Data supplied as hypotheses

T>=2 is real, X=T^2, and R in [T/sqrt(2),sqrt(3)T]. Let Psi be a fixed
real even Schwartz function, and v a fixed real smooth function supported
in [1,4]. For dyadic N in T^(52/125)<N<T^(99/125), set

\[
 \ell_{N,T}(u)=\int_0^\infty t^{-1}\Psi(\sqrt{N/T}\,t)
                  v(t^2)\sin(2\pi ut)dt,\qquad
 S_N(R)=\sum_{m\ge1}r_2(m)m^{-1/4}
                    \ell_{N,T}(\sqrt N(R-\sqrt m)).
\]

Here r2(m) counts all integer representations as two squares,
r2(m)=4 sum_(d|m)chi4(d), with chi4(d)=0 for even d and(-1)^((d-1)/2)
for odd d. You may use r2(m)<<_epsilon m^epsilon and the global inclusive
circle bound P(y)<<_epsilon y^(theta+epsilon), theta=(3292+25sqrt1717)/13762,
for y>=2 real, where P(y)=1+sum_(1<=m<=y)r2(m)-pi y.
Let beta=2theta-1/2. The current full middle-sum twelfth moment is at
most T^(10beta+epsilon). Desired moment is T^(29/25+epsilon).

## Assigned lemma and control questions

Independently investigate the additive-filter quantity

\[
 Z_{N,T}(x)=\sum_{m\ge1}(r_2(m)-\pi)
       \ell_{N,T}\!\left(\frac{x-m}{h_N(x)}\right),
 \qquad h_N(x)=\frac{2\sqrt x}{\sqrt N}.
\]

1. Derive a valid uniform relation between S_N(R) and R^(-1/2)Z_(N,T)(R^2),
   with a proved error strong enough for the complete moment target. Do not
   assume linearization or mean subtraction is free. Include all far tails,
   small m, the origin convention, exact integer x, and variable width.
2. Derive the best immediate supremum from the supplied circle bound using
   this filter, or explain why it fails. No arbitrary-coefficient bound may
   be substituted for actual r2.
3. Test whether the prospective uniform estimate
   integral_(X/2)^(3X)|Z_(N,T)(x)|^6 dx
   <<_epsilon X^(1+epsilon)(T/sqrt N)^3,
   for every middle N, would suffice for the desired full twelfth moment.
   Compute the exact exponent ledger, allowable losses and required window
   range. It is a hypothesis for this test, not an available theorem.
4. Give at least one analytical control for the bridge and one for the
   danger of upgrading low-order/positive information to the signed sixth
   moment. Distinguish a failed inference from a counterexample to actual r2.

No task may change the graph, draft, matrix, synthesis or next-round plan.
