# Round 163 candidate: canonical close opposite-prime exchange sector

- Campaign: m9-m2-hard-top-t1-near-square-divisor-involution-gate
- Starting graph:
  700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358
- Proposed terminal: strict_t1_prime_toggle_sector
- Evidence status: conductor candidate under seam review

## 1. Result

Fix \(\kappa>0\) and one \(L\)-block.  For each supported squarefree
\(N\), select canonically at most one pair of distinct odd prime
divisors \(\{p_{N,L,\kappa},q_{N,L,\kappa}\}\) such that

\[
 \chi_4(p_{N,L,\kappa}q_{N,L,\kappa})=-1,\qquad
 \left|\log\frac{q_{N,L,\kappa}}{p_{N,L,\kappa}}\right|
 \leq\kappa L^{-1/2}.
\tag{163.C1}
\]

The selection uses \(N,L,\kappa\), but not the divisor allocation.
Retain exactly those physical incidences for which one, but not both,
selected primes divide the odd character-bearing factor.  Their
complete literal contribution satisfies

\[
 \boxed{\mathcal S_{L,1}^{\rm cp}\ll_\kappa L^{3/2}+L
        \ll_\kappa L^{3/2}.}
\tag{163.C2}
\]

This is uniform in the real centre \(J=\sqrt X\).  It proves neither
density nor coverage of the complementary incidences.  Separately,
averaging any collection of sign-reversing full divisor-cube toggles
only averages exact representations of the original coefficient; in
particular, averaging every \(p\equiv3\pmod4\) one-prime toggle is exact
self-return.

## 2. Exact statement and hypotheses

Retain the frozen scalar on the inherited nonempty-block range
\(1\ll L\ll H\leq J^{1/2}\):

\[
 \mathcal S_{L,1}
 =\sum_{N\asymp L^2}\mu^2(N)
  \left(\frac{L^2}{N}\right)^{3/4}e(J\sqrt N)b_{L,X}(N),
\tag{163.C3}
\]

\[
 b_{L,X}(N)=
 \sum_{\substack{d\mid N,\ d\ {\rm odd}\\
                  \sqrt N\leq d\leq2\sqrt N}}
 \chi_4(d)P_N(d),\qquad
 P_N(d)=\eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right).
\tag{163.C4}
\]

Every inherited half-open shell, cone, even-\(N\) branch, floor, star,
endpoint, profile entry and exit, and zero extension is literal.  Use
only the accepted profile interface: \(\eta_L\) is one fixed smooth
dyadic profile at scale \(L\), \(\Phi\) is bounded \(C^1\), and \(W\)
is a fixed smooth top profile (equivalently, bounded \(C^1\) on each of
finitely many fixed cells).  Thus, away from the finitely many hard
faces, the soft symbol

\[
 Q_{L,X}(d,m)=\eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xd}{4m}}\right)
\tag{163.C5}
\]

satisfies, for \(d,m\asymp L\) and \(|u|\leq1\),

\[
 |Q_{L,X}(e^u d,e^{-u}m)-Q_{L,X}(d,m)|\ll |u|.
\tag{163.C6}
\]

Choose the pair in (163.C1), when it exists, by lexicographically
minimizing

\[
 \left(\left|\log(q/p)\right|,\min(p,q),\max(p,q)\right)
\tag{163.C7}
\]

among qualifying unordered pairs, then label by residue class.  This is
unique for fixed \((N,L,\kappa)\) and unchanged by reallocating factors.
Let

\[
 \mathscr D_{N,L,\kappa}^{\rm cp}
 =\left\{d\mid N:d\ {\rm odd},\
 {\bf1}_{p_{N,L,\kappa}\mid d}
 +{\bf1}_{q_{N,L,\kappa}\mid d}=1\right\}.
\tag{163.C8}
\]

With \(A_N(d)={\bf1}_{I_N}^{\rm lit}(d)P_N(d)\), including literal
star weights, the sector is

\[
 \mathcal S_{L,1}^{\rm cp}
 =\sum_{\substack{N\asymp L^2\ {\rm sf}\\N\ {\rm qualifies}}}
 \left(\frac{L^2}{N}\right)^{3/4}e(J\sqrt N)
 \sum_{d\in\mathscr D_{N,L,\kappa}^{\rm cp}}
 \chi_4(d)A_N(d).
\tag{163.C9}
\]

## 3. Proof and derivation

### Exact XOR exchange

Suppress the fixed subscripts on \(p,q\).  For
\(d\in\mathscr D_{N,L,\kappa}^{\rm cp}\), put \(m=N/d\) and define

\[
 T_N(d)=
 \begin{cases}
 dq/p,&p\mid d,\ q\mid m,\\
 dp/q,&q\mid d,\ p\mid m.
 \end{cases}
\tag{163.C10}
\]

Squarefreeness makes the quotients integral.  This is a fixed-point-free,
multiplicity-one involution of the complete XOR divisor set.  It
preserves \(N\), squarefreeness, coprimality, oddness of \(d\), and the
factor \(2\) in \(m\) when \(N\) is even.  Since \(\chi_4(pq)=-1\),

\[
 \chi_4(T_Nd)=-\chi_4(d).
\tag{163.C11}
\]

The canonical pair is unchanged because \((N,L,\kappa)\) is unchanged.
Reindexing the full ambient XOR set, not merely its physical part, gives

\[
 \sum_{d\in\mathscr D_{N,L,\kappa}^{\rm cp}}\chi_4(d)A_N(d)
 =\frac12\sum_{d\in\mathscr D_{N,L,\kappa}^{\rm cp}}\chi_4(d)
 \{A_N(d)-A_N(T_Nd)\}.
\tag{163.C12}
\]

Both legs have the same normalization and \(e(J\sqrt N)\) for every
real \(J\).

### Common-cell differences

Put \(\theta_N=\log(q/p)\), so
\[
 |\theta_N|\leq\kappa L^{-1/2}.
\tag{163.C13}
\]
The two orientations map
\((d,m)\) to \((e^{\pm\theta_N}d,e^{\mp\theta_N}m)\).
If both legs lie in one literal smooth cell, (163.C6) gives

\[
 |A_N(d)-A_N(T_Nd)|\ll_\kappa L^{-1/2}.
\tag{163.C14}
\]

For clarity, the \(\Phi\)-difference is
\[
 O\!\left(|\theta_N|\frac L H\right)
 \leq O_\kappa(L^{-1/2}),
\tag{163.C15}
\]
the \(W\)-argument is multiplied by \(e^{\pm\theta_N}\), and the
dyadic profile obeys the ordinary scale bound
\(\|\eta_L'\|_\infty\ll L^{-1}\).  No floor or profile
argument is replaced.  Since the physical support lies in one fixed
\(O(L)\)-by-\(O(L)\) box, there are \(O(L^2)\) possible integer pairs.
The total common-cell cost is \(O_\kappa(L^{3/2})\).

### Every hard crossing

The exchange multiplies \(d/m\) by \(e^{\pm2\theta_N}\) and \(d\) by
\(e^{\pm\theta_N}\).  A cone, ratio-profile, dyadic, vertical-profile,
or zero-extension face can therefore be crossed only in a strip

\[
 |d-\lambda m|\ll_\kappa L^{1/2}+1
 \quad\hbox{or}\quad
 |d-\lambda L|\ll_\kappa L^{1/2}+1.
\tag{163.C16}
\]

Each strip contains \(O_\kappa(L^{3/2}+L)\) integer pairs, and there are
only finitely many inherited faces.  Half-open ties, ceilings, and star
changes lie on the same lattice faces and supply the \(O(L)\) term.
The \(N\)-shell is invariant; all arithmetic selectors only delete
pairs.  If one orbit leg is physical, closeness keeps the zero-extended
partner in a fixed enlarged \(O(L)\)-by-\(O(L)\) box, so no partner tail
is omitted.  Crossing amplitudes are bounded.  Combining (163.C12),
(163.C14), and (163.C16) proves (163.C2).

### Exact toggle-averaging self-return

For \(p\mid N\), \(p\equiv3\pmod4\),

\[
 b_{L,X}(N)=
 \sum_{\substack{d\mid N/p\\d\ {\rm odd}}}
 \chi_4(d)\{A_N(d)-A_N(pd)\}.
\tag{163.C17}
\]

The two supports are disjoint because \(p\geq3\) while \(I_N\) has
multiplicative width two.  Let
\(\mathcal P_3(N)=\{p\mid N:p\equiv3\pmod4\}\).  Summing (163.C17)
gives

\[
 |\mathcal P_3(N)|b_{L,X}(N)
 =\sum_{p\in\mathcal P_3(N)}
  \sum_{\substack{d\mid N/p\\d\ {\rm odd}}}
  \chi_4(d)\{A_N(d)-A_N(pd)\}.
\tag{163.C18}
\]

For a fixed active divisor \(r\), a prime \(p\nmid r\) contributes
\(\chi_4(r)A_N(r)\) through the first term; \(p\mid r\) contributes
\(-\chi_4(r/p)A_N(r)=\chi_4(r)A_N(r)\) through the second.  Thus every
prime reinforces the original coefficient.  More generally, any
sign-reversing divisor-lattice involution \(T\) gives

\[
 b_{L,X}(N)=\frac12\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\{A_N(d)-A_N(Td)\}.
\tag{163.C19}
\]

A weighted average with total weight one is exactly \(b_{L,X}(N)\).
The strict sector succeeds only because its exchange moves by
\(O(L^{-1/2})\) and every profile difference and crossing is priced.

## 4. First doubtful or unproved step

The accepted profile interfaces resolve the finite-cell seam in
(163.C6).  The first unproved contribution is the complement of
(163.C8): incidences containing neither selected prime, both selected
primes, or belonging to \(N\) with no pair satisfying (163.C1).
No eligible-pair density or per-block nonemptiness statement is proved.
Hence (163.C2) is a strict incidence-sector theorem, not the full
\(t=1\) target.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| canonical multiplicity | Pass: one pair per fixed \((N,L,\kappa)\), one fixed-point-free orbit. |
| character sign | Pass: (163.C11) holds in both orientations. |
| product and phase | Pass: \(N\), its shell, normalization, and phase are invariant. |
| parity and even branch | Pass: only odd primes move; the factor \(2\) remains in \(m\). |
| literal profiles | Pass under accepted fixed-profile interfaces: (163.C14)--(163.C15). |
| floors, stars, entries and exits | Pass: all crossing faces occur in (163.C16). |
| target power | Pass: \(L^2L^{-1/2}+O(L^{3/2}+L)\ll L^{3/2}\). |
| density and complement | Open by design and never inferred. |
| one-prime averaging | Exact no-gain self-return: (163.C17)--(163.C19). |
| downstream scope | No full \(t=1\), hard TOP, BAL, UNBAL, M9--M2, M9, bridge, target, or exponent consequence. |

No computation or external theorem is used.

## 6. Dependencies and exact artifacts used

- protocol.md;
- state/proof_obligations.yml at the starting hash;
- the Round-163 strategy, barrier packet, blind statement, and conductor
  one-toggle/complement seed;
- the accepted Round-74 exact top-cone derivation;
- H4-Phi-regularity and the accepted Round-77 actual-symbol/profile
  interface;
- the Round-137 complementary-divisor self-return as scope only;
- the Round-161 exact \(t=1\) coefficient;
- the Round-162 product-collar obstruction.

## 7. Recommended state effect

After independent algebra, profile, power, and graph-scope reviews,
promote (163.C2) as a proved-internal strict close-opposite-prime XOR
incidence sector.  Retain (163.C17)--(163.C19), the general matching
classification, and parity-correct complement identities only as scoped
route evidence.  Keep both hard-TOP parents and the complete \(t=1\)
target open; record the exact uncovered incidence complement as the next
action.  Do not promote any remaining channel or downstream theorem.
