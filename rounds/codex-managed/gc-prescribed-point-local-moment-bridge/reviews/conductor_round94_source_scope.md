# Conductor review: Round 94 source scope

Campaign: `gc-prescribed-point-local-moment-bridge`

Starting graph SHA-256:
`6b7b5b681890edd49b0e0a525fe813044943d4072dd7fc90e27620615d2e93ae`

## Clean primary-source revalidation

The hostile/source report is context-contaminated because it opened two
files outside its selected-context brief.  It remains useful candidate
evidence but is not the independent promotion gate.  The conductor
therefore rechecked the load-bearing external statement directly in the
published primary text.

Popov, Theorem 10(ii), defines

\[
 E_2(T,H)=\frac1{2H}\int_{T-H}^{T+H}P(x)^2\,dx
\]

and proves, for every \(H\le T/2\),

\[
 E_2(T,H)\ll \sqrt T+\frac{T(\log T)^2}{H}.
 \tag{R94.S1}
\]

Thus the total local mass obeys

\[
 Q(T,H)\ll H\sqrt T+T(\log T)^2.
 \tag{R94.S2}
\]

If \(H=T^\alpha\), \(\alpha\le1/2\), then the power exponent of
\(Q\) is \(q=1\).  The clean blind bridge gives

\[
 |P(T)|\ll Q^{1/3}+(Q/H)^{1/2}
 \ll T^{1/3+o(1)}+T^{(1-\alpha)/2+o(1)}.
 \tag{R94.S3}
\]

This returns exactly exponent \(1/3\) for
\(1/3\le\alpha\le1/2\), and is worse below \(1/3\).  Popov's fourth
and sixth local moments begin at \(H\ge T^{1/2}\); Section 11 likewise
states that the available moment input yields only the trivial
\(1/3+\varepsilon\) estimate.

## Other cited routes

Nowak's global mean-square asymptotic can be subtracted at nearby
endpoints, but its error remains \(T\) times logarithms and produces the
same power ledger.  Jutila-type results estimate averaged increments on
different window ranges.  Conditional broadness theorems assume the local
persistence they would need to prove.  None supplies the actual signed
rational-frequency cluster bound of Round 94.

Li--Yang's arXiv theorem states the direct exponent
\(0.314483\ldots\), which is below \(1/3\) but above \(1/4\).  The
existing graph correctly keeps `Li-Yang-source-audit` at
`source_audit_required` because the v2 auxiliary-range inconsistency has
not been resolved.  Round 94 does not import that preprint as a proof
dependency or as a quarter mechanism.

## Decision

Create a proved-external source-audit node for (R94.S1)--(R94.S3) as a
guardrail.  No external source closes the prescribed-point bridge, either
canonical core, M9, or the quarter target.  The internally certified
uniform exponent remains \(1/3\).

