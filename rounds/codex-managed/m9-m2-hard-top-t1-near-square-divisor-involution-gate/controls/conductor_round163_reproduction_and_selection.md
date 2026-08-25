# Round 163 conductor reproduction and kernel selection

- Campaign: m9-m2-hard-top-t1-near-square-divisor-involution-gate
- Starting graph:
  700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358
- Resource use: 100% analytic/algebraic; no numerical experiment
- Status: reproduced candidate pending final seam adjudication

## Selected smallest kernel

The smallest graph-changing statement is the exact target-safe subsum
formed as follows.  For each supported squarefree \(N\), select
canonically at most one pair of distinct odd prime factors
\(\{p_N,q_N\}\) with

\[
 \chi_4(p_Nq_N)=-1,\qquad
 |\log(p_N/q_N)|\leq\kappa L^{-1/2}.
\tag{163.K1}
\]

Retain all and only the physical divisor incidences in which exactly one
selected prime belongs to the odd character-bearing factor.  This
complete incidence sector is \(O_\kappa(L^{3/2}+L)\), uniformly in the
real centre.  It is narrower than the full \(t=1\) scalar and makes no
density claim.

The exact all-toggle averaging self-return and complement identities are
retained as route controls inside the same kernel.  A second durable node
is unnecessary unless a review identifies a downstream consumer that
needs the obstruction separately.

## Independent algebraic reproduction

For one eligible \(N\), let \(\mathscr D_N^\oplus\) be the full odd
divisor set on which exactly one selected prime occurs.  Exchange the two
primes between \(d\) and \(N/d\).  Squarefreeness makes the exchange
integral, involutive, fixed-point-free, and multiplicity one.  The
product, shell, phase, normalization, coprimality, oddness, and even-\(N\)
branch are invariant, while

\[
 \chi_4(T_Nd)=-\chi_4(d).
\tag{163.K2}
\]

For the literal zero-extended profile \(A_N\), reindexing the full
ambient XOR divisor set gives

\[
 \sum_{d\in\mathscr D_N^\oplus}\chi_4(d)A_N(d)
 =\frac12\sum_{d\in\mathscr D_N^\oplus}\chi_4(d)
 \{A_N(d)-A_N(T_Nd)\}.
\tag{163.K3}
\]

The ambient domain in (163.K3) is essential: restricting it to physical
divisors before reindexing would lose every one-sided partner.

Put \(\theta_N=\log(q_N/p_N)\).  On a common literal smooth cell,
\(|\theta_N|\leq\kappa L^{-1/2}\), the accepted fixed dyadic/top profile
seminorms, and bounded \(C^1\) norm of \(\Phi\) give

\[
 |A_N(d)-A_N(T_Nd)|\ll_\kappa L^{-1/2}.
\tag{163.K4}
\]

The \(\Phi\) contribution is
\(O(|\theta_N|L/H)\leq O(|\theta_N|)\); the \(W\)-argument is multiplied
by \(e^{\pm\theta_N}\); no \(H,y,q_X\), floor, shell, or phase is
approximated.  At most \(O(L^2)\) ordered integer pairs can occur.

Every status change lies in a fixed finite union of strips

\[
 |d-\lambda m|\ll_\kappa L^{1/2}+1
 \quad\hbox{or}\quad
 |d-\lambda L|\ll_\kappa L^{1/2}+1.
\tag{163.K5}
\]

Each strip contains \(O_\kappa(L^{3/2}+L)\) integer pairs.  The
half-open convention, ceilings, equality stars, and zero-extension
jumps lie on the same faces and contribute the \(O(L)\) part.  The
arithmetic selectors only delete pairs.  The \(N\)-shell is invariant.
Therefore

\[
 L^2\cdot L^{-1/2}+O_\kappa(L^{3/2}+L)
 \ll_\kappa L^{3/2}+L,
\tag{163.K6}
\]

which reproduces the claimed sector without cross-\(N\) cancellation.

## Reproduction of the route obstruction

For any \(p\equiv3\pmod4\) dividing \(N\),

\[
 b_{L,X}(N)=
 \sum_{\substack{d\mid N/p\\d\ {\rm odd}}}
 \chi_4(d)\{A_N(d)-A_N(pd)\}.
\tag{163.K7}
\]

The two supports are disjoint because the physical interval has
multiplicative width two and \(p\geq3\).  If
\(\mathcal P_3(N)=\{p\mid N:p\equiv3\pmod4\}\), summing (163.K7) gives
\[
 |\mathcal P_3(N)|b_{L,X}(N)
 =\sum_{p\in\mathcal P_3(N)}\sum_{d\mid N/p}
 \chi_4(d)\{A_N(d)-A_N(pd)\}.
\tag{163.K8}
\]

Every active divisor occurs with its original sign for every \(p\):
through \(A_N(d)\) if \(p\nmid d\), and through
\(-\chi_4(d/p)A_N(d)=\chi_4(d)A_N(d)\) if \(p\mid d\).  Hence averaging
these leaking identities is exact self-return, not a divisor-count gain.
The same character-eigenvalue argument applies to weighted averages of
arbitrary sign-reversing divisor-cube toggles.

For odd \(N\), complementation sends the physical window to
\([\sqrt N/2,\sqrt N]\).  For \(N=2M\), physical complementation is even,
while the odd-part complement \(M/d=N/(2d)\) lands in
\([\sqrt N/4,\sqrt N/2]\).  Both are excluded lower-window rewrites.

## Control matrix

| Control | Reproduced outcome |
|---|---|
| exact product grouping | Green: one divisor allocation per squarefree factor pair; no factor two. |
| canonical choice | Green: an \(N\)-only lexicographic choice is invariant under the exchange. |
| sign and fixed points | Green: opposite prime characters give (163.K2); distinct primes give no fixed point. |
| parity | Green: only odd primes move; the factor \(2\) stays in the second factor. |
| smooth profile power | Green: (163.K4), including the \(L/H\) factor for \(\Phi\). |
| hard support | Green candidate: every fixed inherited seam is counted by (163.K5); independent profile review remains required. |
| partner tails | Green: if one orbit leg is supported, closeness keeps the other in one fixed \(O(L)^2\) box. |
| arbitrary real centre | Green: \(N\) and hence \(e(J\sqrt N)\) are unchanged. |
| density | Deliberately unclaimed.  The theorem is a typed exact subsum, not an exceptional-set estimate. |
| complement of the sector | Open: neither/both/no-pair incidences receive no bound. |
| all-toggle averaging | Exact no-gain self-return (163.K7)--(163.K8). |
| downstream scope | No full \(t=1\), remaining channel, hard TOP, smooth packet, M9--M2, M9, bridge, target, or exponent consequence. |

## Selection decision

Subject to the three independent seam reviews, select the strict
close-opposite-prime sector as the only positive promotion.  Retain the
toggle-average, matching, and parity-correct complement identities as
scoped route evidence.  The next survivor is the exact complementary
\(t=1\) incidence sum, followed by the other few-point channels.
