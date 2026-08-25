# Blind near-square divisor rederivation

Campaign: m9-m2-hard-top-t1-near-square-divisor-involution-gate
Task: statement-only blind divisor rederivation
Role: blind, independent, statement-only
Generated: 2026-08-25T22:52:18+08:00
Graph hash: deliberately not accessed under the blind brief
Exact context read: protocol.md; rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/blind_statement.md

## 1. Result

**Result: a rigorous no-go for the full-divisor prime-toggle or complementary-divisor argument, with the exact minimal leakage identity. No proof of the target, and no complete nontrivial sector of the physical coefficient, follows from the supplied statement.**

For a squarefree \(N>1\), put

\[
 D_o(N)=\{d:d\mid N,\ 2\nmid d\},\qquad
 I_N=\{d\in D_o(N):\sqrt N\le d\le 2\sqrt N\},
\]

with the displayed/inherited endpoint convention kept literally. If an odd prime \(p\mid N\) is toggled between \(d\) and \(N/d\), then every \(d\in I_N\) is sent outside \(I_N\). Thus a \(p\equiv3\pmod4\) gives an exact sign-reversing involution on the **full** odd-divisor lattice but gives no cancellation at all on the moving near-square interval: every physical term is interval-entry/exit leakage. Ordinary complementary divisors likewise leave the interval; for even \(N\), they additionally leave the odd-divisor lattice.

Multi-prime exchanges can sometimes keep both divisors in \(I_N\), but exact cancellation would then require equality of the entire literal profile at the two different divisors. No such equality is stated, and singleton near-square divisor sets show that no universal alternative sign-reversing divisor involution exists. The smallest obstruction is therefore support preservation itself, before estimates, smoothness, endpoint relaxation, or oscillation are considered.

## 2. Exact statement and hypotheses

Let \(\mathfrak N_L\) denote the literal shell represented by \(N\asymp L^2\); no replacement of it by a newly chosen dyadic interval is made. Define the exact physical profile

\[
 P_N(d)=\eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right),
 \qquad
 G_N(d)={\bf1}^{\rm lit}_{I_N}(d)P_N(d),
\]

and extend \(G_N\) by zero away from the physical divisor support. Any inherited profile support, half-open endpoint, or star is part of this literal value and is not silently filled in. The statement supplies no separate definitions or size bounds for \(\eta_L,\Phi,W\), so they are treated as the exact displayed functions, not as constant or symmetric weights.

The following claims use only \(\mu^2(N)\ne0\), hence squarefreeness, and the standard values \(\chi_4(d)\in\{\pm1\}\) for odd \(d\).

1. **Exact product coefficient and multiplicity.** With \(m=N/d\), the map \((N,d)\leftrightarrow(d,m)\) is a bijection, with no symmetry factor, and

   \[
   \begin{split}
   \mathcal S_{L,1}
   =L^{3/2}\sum_{d,m\ge1}&
   \frac{\mu^2(dm)\,{\bf1}^{\rm lit}_{\mathfrak N_L}(dm)
   {\bf1}_{2\nmid d}{\bf1}^{\rm lit}_{R}(d,m)}{(dm)^{3/4}}
   e(J\sqrt{dm})\chi_4(d)\\
   &\times\eta_L(d)\Phi\!\left(\frac d{H+1}\right)
   W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt{dm}}\right),
   \end{split}
   \tag{2.1}
   \]

   where \(R\) is exactly the translated near-square condition: with the displayed closed signs it is \(m\le d\le4m\), and inherited half-open signs translate correspondingly. Also

   \[
   \mu^2(dm)=\mu^2(d)\mu^2(m){\bf1}_{(d,m)=1}.
   \tag{2.2}
   \]

   Hence the exact coefficient of a physical product \((d,m)\) is the full summand in (2.1), including \(L^{3/2}(dm)^{-3/4}\), the literal shell, parity, profile, and phase. If \(dm\) is even, \(d\) is still odd and the unique factor \(2\) is forced into \(m\).

2. **Full-divisor diagnostic coefficient.** The unweighted full odd-divisor model is

   \[
   C_{\rm full}(N)
   :=\mu^2(N)\sum_{\substack{d\mid N\\2\nmid d}}\chi_4(d)
   =\mu^2(N)\prod_{\substack{p\mid N\\p\ {\rm odd}}}
       \bigl(1+\chi_4(p)\bigr).
   \tag{2.3}
   \]

   For squarefree \(N\), this is zero exactly when an odd prime \(p\equiv3\pmod4\) divides \(N\), and otherwise it is \(2^{\omega(N)-{\bf1}_{2\mid N}}\). The prime \(2\) contributes the factor \(1\), not \(2\) and not a sign. Formula (2.3) is a diagnostic full-lattice identity; it is not the physical \(b_{L,X}(N)\).

3. **Prime-toggle leakage.** Fix an odd \(p\mid N\) and define

   \[
   \tau_p(d)=
   \begin{cases}
   d/p,&p\mid d,\\
   pd,&p\nmid d.
   \end{cases}
   \tag{2.4}
   \]

   This is an involution of \(D_o(N)\). If \(p\equiv3\pmod4\), then
   \(\chi_4(\tau_p(d))=-\chi_4(d)\), and the exact zero-extension identity is

   \[
   b_{L,X}(N)=\frac12\sum_{d\in D_o(N)}\chi_4(d)
      \bigl(G_N(d)-G_N(\tau_p(d))\bigr).
   \tag{2.5}
   \]

   Nevertheless,

   \[
   \tau_p(I_N)\cap I_N=\varnothing.
   \tag{2.6}
   \]

   Thus (2.5) is pure support leakage, not a saving.

4. **Multi-prime exchange criterion.** Write \(N=dm\). For odd \(a\mid d\) and odd \(b\mid m\), move the primes of \(a\) from \(d\) to \(m\) and those of \(b\) from \(m\) to \(d\):

   \[
   d'=\frac{db}{a},\qquad m'=\frac{ma}{b},
   \qquad r=\frac dm,\qquad r'=r\left(\frac ba\right)^2.
   \tag{2.7}
   \]

   It reverses the character precisely when

   \[
   \frac{\chi_4(d')}{\chi_4(d)}=\chi_4(ab)=-1,
   \tag{2.8}
   \]

   and both products remain in the physical interval precisely when

   \[
   1\le r\le4,
   \qquad
   1\le r(b/a)^2\le4,
   \tag{2.9}
   \]

   with literal endpoint changes if inherited. In an even product, \(b\) cannot contain \(2\), since otherwise \(d'\) would be even; the factor \(2\) is immobile in \(m\). If (2.8)--(2.9) hold, the paired physical contribution is proportional to

   \[
   \chi_4(d)\bigl(P_N(d)-P_N(d')\bigr),
   \tag{2.10}
   \]

   not to zero. Equality in (2.10) would require the exact \(\eta_L\), \(\Phi(d/(H+1))\), and \(W(\sqrt{q_X}\,d/(2\sqrt N))\) values, including entries, exits, and zero extension, to match.

5. **Complementary divisors.** If \(N\) is odd, \(d\mapsto N/d\) preserves oddness but maps \(I_N\) into the disjoint lower interval \([\sqrt N/2,\sqrt N]\), modulo the inherited endpoint convention. If \(N\) is even, \(N/d\) is even and is not in \(D_o(N)\). Writing \(N=2M\), the odd-part complement \(d\mapsto M/d\) stays odd but maps \(I_N\) into \([\sqrt N/4,\sqrt N/2]\), still outside. A symmetric two-sided, unweighted diagnostic model would cancel complementary pairs for odd \(N\) with \(\chi_4(N)=-1\), because

   \[
   \chi_4(N/d)=\chi_4(N)\chi_4(d),
   \tag{2.11}
   \]

   but the one-sided physical interval and physical profile do not satisfy those hypotheses.

6. **Uniformity in the real centre and exact powers.** Every divisor repartition above fixes \(N=dm\). Therefore \(\mu^2(N)\), the literal \(N\)-shell, \(L^{3/2}N^{-3/4}\), and \(e(J\sqrt N)\) are unchanged. The identities hold with the phase centre \(J\) replaced by any real number. They also retain

   \[
   J=\sqrt X,\quad y=\lfloor J\rfloor,\quad q_X=X/y^2,
   \quad H=\lfloor yX^{-1/4}\rfloor
   \tag{2.12}
   \]

   exactly: neither \(q_X\) nor \(H\) is replaced by an asymptotic surrogate. The product \(\sqrt{q_X}\,d\) in the numerator and the denominator \(2\sqrt N\) in \(W\) both remain literal. No \(H\)- or \(X\)-power gain is produced by the involutions. Conversely, a pairwise cancellation intended to hold for an arbitrary real phase centre cannot pair distinct \(N\)'s: equality of \(e(\alpha\sqrt N)\) and \(e(\alpha\sqrt{N'})\) for every real \(\alpha\) forces \(N=N'\).

## 3. Proof or derivation

For (2.1), substitute \(N=dm\) with \(m=N/d\). The near-square inequalities square without a sign change:

\[
 \sqrt{dm}\le d\iff m\le d,
 \qquad
 d\le2\sqrt{dm}\iff d\le4m.
\]

Every original pair \((N,d)\) gives exactly one \((d,m)\), and conversely, so no factor \(2\) is allowed. Squarefreeness gives (2.2). Pulling \(L^{3/2}\) out of \((L^2/(dm))^{3/4}\) gives the exact power in (2.1). The displayed lower equality would imply \(d=m\), which together with \((d,m)=1\) gives \(N=1\); the displayed upper equality would imply \(d=4m\), impossible for odd \(d\). Hence for the active squarefree \(N>1\) terms the two near-square equality endpoints contain no divisor, although shell and profile endpoints must still be retained.

For (2.3), a squarefree odd divisor is obtained by independently selecting each odd prime of \(N\). Expanding the finite product \(\prod_{p\mid N,\,p\text{ odd}}(1+\chi_4(p))\) gives exactly one character value for each such divisor. Multiplication by \(\mu^2(N)\) makes the formula valid as stated even when \(N\) is not squarefree. This proves the exact full-lattice coefficient and the separate treatment of the factor \(2\).

For the prime-toggle claim, let \(r=d/m\in[1,4]\). If \(p\mid d\), toggling \(p\) gives

\[
 (d',m')=(d/p,mp),\qquad d'/m'=r/p^2\le4/9<1.
\]

If \(p\mid m\), it gives

\[
 (d',m')=(pd,m/p),\qquad d'/m'=rp^2\ge9>4.
\]

This proves (2.6), including the displayed endpoints. When \(p\equiv3\pmod4\), toggling changes the character sign in either direction because \(\chi_4(p)=-1\). Reindexing the second half of

\[
 \frac12\sum_{d\in D_o(N)}\chi_4(d)
 \bigl(G_N(d)-G_N(\tau_p(d))\bigr)
\]

by \(d\mapsto\tau_p(d)\) then proves (2.5). More generally, for any sign-reversing divisor involution \(T\), the exact decomposition

\[
 G_N(d)-G_N(Td)
 =\bigl({\bf1}_{I_N}(d)-{\bf1}_{I_N}(Td)\bigr)P_N(d)
 +{\bf1}_{I_N}(Td)\bigl(P_N(d)-P_N(Td)\bigr)
\tag{3.1}
\]

separates interval entry/exit leakage from literal-profile leakage. For a one-prime toggle the first term already accounts for the entire physical contribution; it is not a thin endpoint error.

For (2.7)--(2.10), squarefreeness means prime allocation between \(d\) and \(m\) is disjoint. Direct division gives \(r'=r(b/a)^2\). Since every relevant integer is odd, \(\chi_4(a)^{-1}=\chi_4(a)\), so

\[
 \chi_4(d')=\chi_4(d)\chi_4(a)\chi_4(b)
 =\chi_4(d)\chi_4(ab).
\]

The outer \(N,L,J\) factors agree for the two allocations, leaving exactly (2.10). Any map between two odd divisor allocations is of this exchange form: take \(g=(d,d')\), \(a=d/g\), and \(b=d'/g\). Thus allowing a differently named divisor involution does not remove the support and profile requirements.

Finally, ordinary complementation sends \(r=d/m\) to \(1/r\). For \(r\in[1,4]\), this lies in \([1/4,1]\), with the common value \(1\) impossible for squarefree \(N>1\). The parity assertions and the range for the odd-part complement follow directly from \(N=2M\) and \(M/d=N/(2d)\). This proves the complement claims.

The exact triangle inequality left by the leakage is

\[
 |\mathcal S_{L,1}|\le
 L^{3/2}\!\sum_{d,m\ge1}
 \frac{\mu^2(dm){\bf1}_{\mathfrak N_L}^{\rm lit}(dm)
 {\bf1}_{2\nmid d}{\bf1}_{R}^{\rm lit}(d,m)}{(dm)^{3/4}}
 |P_{dm}(d)|.
\tag{3.2}
\]

It contains no involutive gain. Even under the additional diagnostic assumption \(|P_N(d)|\le1\), the \(O(L^2)\) admissible lattice pairs only give the natural \(O(L^2)\) bound, not \(L^{3/2}X^\varepsilon\). The definitions and bounds needed for any sharper profile estimate are absent from the blind statement; cancellation across distinct \(N\) would be a separate analytic argument, not the tested fixed-product divisor involution.

## 4. First doubtful or unproved step

The first step needed by a positive prime-toggle or complement proof is that its sign-reversing partner remains in the physical near-square divisor set. This step is not merely unproved: (2.6) and the complement calculation show it is false for every physical divisor of every squarefree \(N>1\). The resulting leakage is the whole truncated coefficient, not an endpoint-sized remainder.

If one replaces a prime toggle by a support-preserving multi-prime exchange, the next required step is

\[
 P_N(d)=P_N(d'),
\]

including exact \(\eta_L\) values, \(H+1\), the factor \(\sqrt{q_X}\,d\) in \(W\), profile entries/exits, inherited stars and half-open endpoints, and zero extension. No such symmetry or even size hypothesis is present in the supplied statement. Consequently the target itself is underdetermined from the blind packet: rescaling an otherwise unspecified profile would rescale \(\mathcal S_{L,1}\). This missing profile information is secondary to, and does not repair, the already rigorous interval-leakage no-go.

## 5. Required control test and outcome

Exact divisor enumeration gives the following controls; no floating-point endpoint decision is needed because the inequalities can be squared.

| \(N\) | parity | \(D_o(N)\) | \(I_N\) | full \(\sum_{d\in D_o(N)}\chi_4(d)\) | outcome |
|---:|:---:|:---|:---|---:|:---|
| \(35=5\cdot7\) | odd | \(1,5,7,35\) | \(7\) | \(0\) | physical coefficient is \(-P_{35}(7)\); \(7\mapsto1\) under the \(7\)-toggle and \(7\mapsto5\) under complement, both outside |
| \(42=2\cdot3\cdot7\) | even | \(1,3,7,21\) | \(7\) | \(0\) | physical coefficient is \(-P_{42}(7)\); ordinary complement is \(6\), which is even, while odd-part complement is \(3\), below the interval |
| \(210=2\cdot3\cdot5\cdot7\) | even | \(1,3,5,7,15,21,35,105\) | \(15,21\) | \(0\) | exchanging \(5\mid15\) with \(7\mid14\) sends \((15,14)\) to \((21,10)\), stays physical, and flips sign; the physical pair is \(-P_{210}(15)+P_{210}(21)\), so only the constant-profile diagnostic cancels |

These controls pass the product, parity, toggle, complement, and multi-prime formulas. They also exhibit both kinds of failure: total support leakage and internal profile leakage. The singleton examples prove that a sign-reversing permutation of the physical divisor set need not exist at all when the displayed profile is nonzero there. More generally, if \(p<q<4p\) are odd primes, then \(I_{pq}=\{q\}\); if \(2p<q<8p\), then \(I_{2pq}=\{q\}\). Choosing a \(3\pmod4\) prime among the odd factors makes (2.3) vanish while the truncated set remains a singleton. Thus the obstruction is not a small-\(N\) endpoint accident whenever the literal \(N\)-shell and profiles admit the term.

## 6. Dependencies and exact artifacts used

- protocol.md.
- rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/blind_statement.md (reread after the formatting-only repair of \(\rm odd\)).
- Standard definitions of \(\mu^2\), the Dirichlet character \(\chi_4\), divisibility, and \(e(t)\).
- A bounded exact enumeration of the divisors of \(35,42,210\), reproduced in Section 5. It is diagnostic only; every general claim above has an algebraic proof.

No graph, campaign state, strategy, seed, nonblind artifact, sibling report, or earlier-round artifact was read. No unstated definition of a shell, profile, star, or zero extension was imported.

## 7. Recommended state effect

**Retain** the prime-toggle/complement calculation as a rigorous leakage obstruction, and **reject** the unqualified full-divisor-involution route to the physical target. Retain multi-prime exchange only as a diagnostic possibility requiring a separately proved exact profile symmetry and a complete pairing of the literal physical support. Make **no change** to the target obligation from this report: the bound \( |\mathcal S_{L,1}|\ll_\varepsilon L^{3/2}X^\varepsilon \) is neither proved nor disproved, because cancellation across \(N\) and the omitted profile hypotheses remain outside the supplied statement.
