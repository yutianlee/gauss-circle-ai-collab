# Source Card: Bennett--Martin--O'Bryant--Rechnitzer 2018

## Bibliographic data

Michael A. Bennett, Greg Martin, Kevin O'Bryant, and Andrew Rechnitzer,
*Explicit bounds for primes in arithmetic progressions*, arXiv:1802.00085
[math.NT], version 3; *Illinois Journal of Mathematics* **62** (2018),
427--532.

- Record: https://arxiv.org/abs/1802.00085
- Primary source inspected: arXiv version 3, Theorem 1.2.

## Exact theorem used

The Round-164 capacity control uses only the fixed-modulus consequence of
Theorem 1.2.  For every integer \(q\geq3\) and reduced residue class
\((a,q)=1\), the theorem supplies explicit constants
\(c_\theta(q),x_\theta(q)>0\) for which

\[
 \left|\theta(x;q,a)-\frac{x}{\varphi(q)}\right|
 <c_\theta(q)\frac{x}{\log x}
 \qquad (x\geq x_\theta(q)).
\]

The printed tables give constants sufficient to use
\(c_\theta(4)\leq1/840\) and \(x_\theta(4)\leq8\cdot10^9\).
Only \(q=4\) and \(a\in\{1,3\}\) are used.

## Exact project deduction

Fix \(0<\alpha<\beta\).  For all sufficiently large \(T\), subtraction
at the two endpoints gives

\[
\begin{aligned}
 \theta(\beta T;4,a)-\theta(\alpha T;4,a)
 &\geq \frac{(\beta-\alpha)T}{2}
 -\frac{\beta T}{840\log(\beta T)}
 -\frac{\alpha T}{840\log(\alpha T)}\\
 &\gg_{\alpha,\beta}T.
\end{aligned}
\]

Since each counted prime contributes at most \(\log(\beta T)\),

\[
 \#\{p\in[\alpha T,\beta T]:p\equiv a\pmod4\}
 \gg_{\alpha,\beta}\frac{T}{\log T}.
\]

Round 164 applies this only to finitely many fixed relative-length prime
boxes.  With four prime variables of scale \(P\asymp\sqrt L\), unique
factorization gives \(\gg L^2/(\log L)^4\) squarefree diagnostic
products, up to a fixed permutation multiplicity.

## Hypothesis match

- The modulus is the fixed integer \(4\geq3\).
- The residue classes \(1,3\) are coprime to \(4\).
- The relative interval endpoints are fixed independently of \(L\).
- Both endpoints exceed the explicit source threshold once \(L\) is
  sufficiently large.
- Repeated-prime diagonals are discarded and are lower order.

## Scope and exclusions

The theorem supplies no information for the Round-163 shrinking selector
window, whose prime separation can be \(O(1)\).  It also supplies no
pointwise lower bound for the literal profile \(\eta_L\Phi W\), no signed
oscillatory estimate, and no lower bound for the physical residual scalar.
Its sole Round-164 use is a coefficient-uniform positive-transport
capacity control.

## Audit status

`proved_external_dependency_fixed_modulus_only`

## Evidence

- `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/reports/unmatched_transport_capacity_hostile_audit.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/reviews/transport_capacity_profile_power_source_review.md`
