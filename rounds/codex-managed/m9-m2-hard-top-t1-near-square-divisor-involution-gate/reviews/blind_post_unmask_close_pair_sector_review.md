# Blind post-unmask review of the close opposite-prime sector

Campaign: m9-m2-hard-top-t1-near-square-divisor-involution-gate
Role: original blind rederiver, post-unmask independent seam reviewer
Generated: 2026-08-25T23:10:18+08:00
Candidate reviewed: conductor_round163_close_opposite_prime_exchange_sector.md
Review status: pass, with one harmless fixed-\(L\) notation correction

## 1. Result

**Pass.** I find no mathematically invalid line in (163.C1)--(163.C19). Under the accepted fixed-profile interfaces, the candidate proves

\[
 \mathcal S_{L,1}^{\rm cp}\ll_\kappa L^{3/2}
\]

for the complete incidence set defined in (163.C8)--(163.C9). The XOR exchange is exact and multiplicity one; the physical profile difference is \(O_\kappa(L^{-1/2})\) on common smooth cells; every hard crossing occupies \(O_\kappa(L^{3/2}+L)\) incidences; and the normalized amplitude is \(O(1)\). This is honestly a **strict incidence-sector theorem**. It is not a density theorem and has no implication for the uncovered incidences or any downstream parent.

The candidate does not contradict the blind no-go. The blind report ruled out exact cancellation from a one-prime toggle and observed that a support-preserving multi-prime exchange leaves a profile difference. The candidate prices precisely that difference using the accepted \(C^1\) interface and prices its hard crossings separately.

The formatting-only typo in the blind report has also been corrected everywhere from
\(\sqrt{q_X},d\) to the product \(\sqrt{q_X}\,d\).

## 2. Exact statement and hypotheses

Fix \(\kappa>0\), a scale \(1\ll L\le H\), and the literal squarefree \(N\asymp L^2\) shell. For each qualifying \(N\), choose the unique lexicographically minimal unordered pair of distinct odd prime factors \(\{p,q\}\) satisfying

\[
 \chi_4(pq)=-1,\qquad |\log(q/p)|\le \kappa L^{-1/2}.
\]

The selection is made once for the fixed \(L,\kappa\) block and depends on \(N\), not on the divisor allocation. Let

\[
 \mathscr D_{N,L}^{\rm cp}
 =\{d\mid N:2\nmid d,\ {\bf1}_{p\mid d}+{\bf1}_{q\mid d}=1\}.
\]

With \(m=N/d\), retain every incidence \(d\in\mathscr D_{N,L}^{\rm cp}\), with the literal physical indicator, profiles, endpoints, star weights, floors, zero extension, and even-\(N\) branch. The reviewed claim is the bound for the sum of all and only these incidences.

The profile hypotheses actually needed are exactly those supplied by the accepted interfaces:

- \(\eta_L\) is a fixed smooth dyadic profile at scale \(L\);
- \(\Phi\) is uniformly bounded \(C^1\);
- \(W\) is a fixed smooth top profile, or more generally has uniformly bounded \(C^1\) seminorms on finitely many fixed cells;
- every remaining nonsmooth support face, ceiling, half-open endpoint, or star is retained as a hard face;
- \(q_X\), \(H\), and the literal shells stay fixed during an exchange.

No density, prime-distribution theorem, or lower bound for the size of the sector is assumed.

## 3. Proof or derivation

### XOR algebra, sign, multiplicity, and parity

Suppose \(p\mid d\) and \(q\mid m\). Define

\[
 d'=d\,\frac qp,\qquad m'=m\,\frac pq.
\]

The other orientation interchanges \(p\) and \(q\). Squarefreeness ensures that the quotients are integers and that \(d'm'=dm=N\). Exactly one of \(p,q\) still divides \(d'\), so the XOR set is invariant. A second exchange returns \((d,m)\), and a fixed point would force \(p=q\). Hence the map is a fixed-point-free involution.

For odd primes,

\[
 \frac{\chi_4(d')}{\chi_4(d)}
 =\frac{\chi_4(q)}{\chi_4(p)}
 =\chi_4(pq)=-1.
\]

If \(N\) is even, \(d\) is odd and the unique factor \(2\) lies in \(m\). Only the two selected odd primes move, so \(d'\) remains odd and \(2\) remains in \(m'\). Squarefreeness, coprimality, the \(N\)-shell, the normalization, and \(e(J\sqrt N)\) are unchanged.

Each original incidence \((N,d)\) has one \(m=N/d\), the canonical pair is chosen once per fixed \((N,L,\kappa)\), and the involution has two orientations. Thus (163.C12) has exactly the required factor \(1/2\) and no divisor, pair-selection, or even-branch multiplicity is missing.

### Common-cell profile difference

Put

\[
 \theta=\log(q/p),\qquad |\theta|\le\kappa L^{-1/2},
\]

so one orientation is \((d,m)\mapsto(e^\theta d,e^{-\theta}m)\). The physical top argument is exactly

\[
 z(d,m)=\frac{\sqrt{q_X}\,d}{2\sqrt{dm}}
       =\sqrt{\frac{q_Xd}{4m}},
\]

and therefore \(z(e^\theta d,e^{-\theta}m)=e^\theta z(d,m)\). On one common smooth cell, scale-\(L\) regularity and bounded \(C^1\) norms give

\[
\begin{aligned}
 |\eta_L(e^\theta d)-\eta_L(d)|&\ll|\theta|,\\
 \left|\Phi\!\left(\frac{e^\theta d}{H+1}\right)
       -\Phi\!\left(\frac d{H+1}\right)\right|
   &\ll |\theta|\frac LH\ll|\theta|,\\
 |W(e^\theta z)-W(z)|&\ll|\theta|.
\end{aligned}
\]

All three factors are bounded, so their product changes by

\[
 |P_N(d)-P_N(d')|\ll_\kappa L^{-1/2}.
\]

The exact factor \((L^2/N)^{3/4}\) is \(O(1)\) on the literal shell and is invariant because \(N\) is invariant. There are \(O(L^2)\) possible integer pairs with \(N\asymp L^2\) and \(1\le d/m\le4\). Consequently all common-cell differences contribute

\[
 O(L^2)\,O_\kappa(L^{-1/2})=O_\kappa(L^{3/2}).
\]

For fixed \(\kappa\), the interface condition \(|\theta|\le1\) holds for all sufficiently large \(L\); the finitely many smaller scales are absorbed into the \(\kappa\)-dependent constant.

### Complete hard-boundary ledger

An exchange multiplies \(d/m\) by \(e^{\pm2\theta}\) and \(d\) by \(e^{\pm\theta}\). On \(d,m\asymp L\), a multiplicative collar of width \(O_\kappa(L^{-1/2})\) has integer thickness \(O_\kappa(L^{1/2}+1)\).

| Literal face or restriction | Behavior under the exchange | Crossing count |
|---|---|---:|
| cone faces \(d=m\) and \(d=4m\), equivalently \(m=d\) and \(m=\lceil d/4\rceil\) | ratio changes by \(e^{\pm2\theta}\) | \(O_\kappa(L(L^{1/2}+1))\) |
| each fixed \(W\)-cell or \(W\)-zero face \(z=c\) | a fixed ratio face \(d/m=4c^2/q_X\) | \(O_\kappa(L(L^{1/2}+1))\) |
| each dyadic \(\eta_L\) entry, exit, or cell face | a vertical \(d\)-face at scale \(L\) | \(O_\kappa(L(L^{1/2}+1))\) |
| each \(\Phi\) cell or zero-extension face that meets the block | a vertical \(d\)-face; \(H\) is fixed | \(O_\kappa(L(L^{1/2}+1))\) |
| any inherited horizontal fixed-profile face | the transposed count | \(O_\kappa(L(L^{1/2}+1))\) |
| exact ceilings, half-open endpoints, and star samples on a face | only the exact lattice face | \(O(L)\) |
| literal \(N\)-shell and its endpoints | \(dm=N\) is invariant | \(0\) |
| squarefree, coprime, odd-\(d\), even-\(N\), XOR, and canonical-pair restrictions | invariant | \(0\) |
| \(y,H,q_X\) floors and real centre \(J\) | fixed during the exchange | \(0\) |

The accepted profiles have only finitely many fixed cells, so the union has

\[
 O_\kappa(L^{3/2}+L)
\]

incidences. Each has bounded normalized amplitude. Together with the common-cell contribution, this proves (163.C2) with the exact \(L^{3/2}\) power and no hidden \(H/L\), \(X\), divisor-multiplicity, or boundary loss.

### Sector completeness and scope

The word “complete” is valid only relative to (163.C8)--(163.C9): every XOR incidence for the one canonical pair, in both orientations and at every literal boundary, is included and estimated. Products with no qualifying pair and incidences containing neither or both selected primes are explicitly excluded. The theorem may be vacuous on a particular \(L\)-block; no nonemptiness, polynomial density, positive proportion, or asymptotic count is claimed. This does not weaken the correctness of the strict incidence-sector estimate, but it forbids describing it as a positive-density sector.

## 4. First doubtful or unproved step

**No mathematically invalid line was found.** The earliest literal imprecision is candidate line 13, “using \(N\) only”: qualification and selection also use the fixed global scale \(L\) (and fixed \(\kappa\)). The harmless precise notation is \(p_{N,L,\kappa},q_{N,L,\kappa}\), or the phrase “depending only on \(N\) within the fixed \(L,\kappa\) block, and not on \(d\).” The same qualification applies to “\(N\)-canonical” at line 157. This does not affect the involution or estimate because \(L,\kappa,N\) are unchanged on both legs.

The candidate’s stated profile seam is resolved by the two accepted interfaces: the profiles are fixed smooth or bounded \(C^1\), with only finitely many literal faces. No \(L\)-dependent transition family is present in the permitted interfaces.

The first genuinely unproved mathematical contribution is exactly the complement listed by the candidate: neither-prime incidences, both-prime incidences, and all incidences for \(N\) with no qualifying pair. Sector density and even eventual nonemptiness are also unproved. None is used in (163.C2).

## 5. Required control tests and outcomes

| Seam | Outcome |
|---|---|
| XOR swap, integrality, and involution | Pass: squarefreeness puts the other selected prime in \(m\), and swapping twice is the identity. |
| Character sign | Pass: \(\chi_4(d')/\chi_4(d)=\chi_4(pq)=-1\) in either orientation. |
| Multiplicity and canonical choice | Pass: one \((d,m)\) per incidence, one selected pair per fixed \((N,L,\kappa)\), and the \(1/2\) in (163.C12) counts each two-cycle once. |
| Odd/even products | Pass: only odd primes move; for even \(N\), the factor \(2\) remains in \(m\). |
| Actual \(C^1\) profile difference | Pass: the corrected top argument is multiplied by \(e^{\pm\theta}\), \(\Phi\) costs only \(L/H\le1\), and all common-cell differences are \(O_\kappa(L^{-1/2})\). |
| All hard crossings and endpoints | Pass: finitely many ratio, vertical, horizontal, and exact lattice faces give \(O_\kappa(L^{3/2}+L)\); invariant faces give zero crossings. |
| Power ledger | Pass: \(L^2L^{-1/2}+L(L^{1/2}+1)\ll L^{3/2}\). |
| Complete strict sector | Pass with qualification: complete for (163.C8)--(163.C9), with no density or nonemptiness assertion. |
| Downstream scope | Pass: this does not close full \(t=1\), hard TOP, BAL, UNBAL, \(M9\!-\!M2\), \(M9\), the bridge, or an exponent. |
| Blind-report formatting correction | Pass: no occurrence of \(\sqrt{q_X},d\) remains; all five affected formula/prose locations now use \(\sqrt{q_X}\,d\). |

As an exact parity/multiplicity micro-control, \(N=210\), \(d=15\), \(m=14\), \(p=5\), \(q=7\) exchanges with \(d'=21\), \(m'=10\). The signs are opposite, both character-bearing factors are odd, the factor \(2\) remains in the complementary factor, and there is exactly one reverse exchange. This is diagnostic only; the general verification above is algebraic.

## 6. Dependencies and exact artifacts used

- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/candidates/conductor_round163_close_opposite_prime_exchange_sector.md.
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reports/blind_near_square_divisor_rederivation.md.
- rounds/codex-managed/m9-m2-top-endpoint-affine-cone/derivation_packet.md.
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reviews/conductor_round77_adjudication.md.
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/blind_statement.md.

No graph, state file, candidate dependency not listed above, sibling report, or earlier-round artifact was inspected. No external theorem or numerical certification is used.

## 7. Recommended state effect

**Promote** (163.C2) as a proved-internal strict close-opposite-prime XOR incidence sector, after making the fixed-\(L,\kappa\) dependence of the selected pair explicit in notation or prose. Promote (163.C17)--(163.C19) only as the stated route-scoped averaging obstruction. Keep the full \(t=1\) scalar, both hard-TOP parents, every other channel, \(M9\!-\!M2\), \(M9\), the bridge, and the global exponent open. Record the uncovered incidence complement and the absence of any density claim verbatim.
