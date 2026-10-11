# Round219 isolated fraction-packing rederivation

## 1. Result

**Verdict: GREEN for both proposed upper bounds.**

For the precise finite incidence count in the packet,

\[
 \boxed{
 C(A)\ll_{c,c'}D\sqrt{JA}+\frac{JAD^2}{X}.
 }
 \tag{1}
\]

Consequently, for every real \(B\geq1\),

\[
 \boxed{
 \sum_{0\leq m\leq\lfloor\log_2B\rfloor}2^{-m}C(2^m)
 \ll_{c,c'}
 D\sqrt J+\frac{JD^2}{X}\log(2+B).
 }
 \tag{2}
\]

The proof retains the exact multiplicity of every reduced fraction before estimating it. Two complementary bounds within each dyadic denominator interval produce the square-root term; a single local spacing bound without that minimum would lose the stated dependence on \(J\) and \(A\).

These are unsigned upper bounds for positive incidence counts. They contain no character or signed cancellation assertion.

## 2. Exact hypotheses and conventions

Assume \(X,D,A\geq1\) are real, \(c,c'>0\) are fixed, and \(z_1,\ldots,z_J\) are distinct real centers in \([1/16,16]\) with

\[
 |z_l-z_{l'}|\geq c/X\quad(l\ne l').
 \tag{3}
\]

The count is

\[
 C(A)=
 \#\{(l,d,e):1\leq l\leq J,\ d,e\in\mathbb Z,\ 
 D\leq d,e<2D,\ |d/e-z_l|\leq c'A/X\}.
 \tag{4}
\]

Write \(\Delta=c'A/X\). The inequalities in \(d,e\) are half-open exactly as in the packet, whereas the incidence interval is closed. All resulting endpoint counts below respect these conventions.

When \(J=0\), both conclusions are immediate, so the proof may assume \(J\geq1\). Constants in (1)--(2) depend only on \(c,c'\), with absolute numerical constants otherwise. No integrality of \(X,D,A,B\) is used.

The interval containing the centers implies \(J\leq1+(16-1/16)X/c\), but the proof does not need to substitute this bound for \(J\). It retains the actual number of centers.

## 3. Independent derivation with full gcd accounting

### Reduce the fraction without dropping its multiplicity

Every pair \(d,e\) in (4) has a unique representation

\[
 d=ga,\qquad e=gb,\qquad g=\gcd(d,e)\geq1,\qquad
 a,b\geq1,\quad \gcd(a,b)=1.
 \tag{5}
\]

For a fixed coprime pair \(a,b\), its exact multiplicity is

\[
 \begin{split}
 M_D(a,b)
 &=\#\{g\in\mathbb Z_{>0}:D\leq ga,gb<2D\}\\
 &=\max\left(
 0,\
 \left\lceil\frac{2D}{\max(a,b)}\right\rceil
 -
 \left\lceil\frac{D}{\min(a,b)}\right\rceil
 \right).
 \end{split}
 \tag{6}
\]

Indeed the allowed positive integers \(g\) lie in the half-open interval
\([D/\min(a,b),\,2D/\max(a,b))\).
Its left endpoint is positive, so no extra zero-integer correction is needed.

If \(M_D(a,b)>0\), necessarily

\[
 \frac12<\frac ab<2,\qquad a,b<2D.
 \tag{7}
\]

Also,

\[
 M_D(a,b)\leq \frac{2D}{\max(a,b)}
             \leq\frac{2D}{b}.
 \tag{8}
\]

For the first inequality one can simply count the positive integers strictly below \(2D/\max(a,b)\); this remains true even when the interval in (6) has length less than one.

Let
\[
 n(r)=\#\{l:|r-z_l|\leq\Delta\}.
\]
The exact count, before any inequality, is

\[
 C(A)=\sum_{\substack{a,b\geq1\\(a,b)=1}}
            M_D(a,b)n(a/b).
 \tag{9}
\]

Thus no gcd value, repeated rational value, or multiplicity from common factors has been discarded.

### Primitive fractions in a denominator interval

For dyadic \(Q=2^k\), \(k\geq0\), \(Q\leq2D\), let \(\mathcal F_Q\) be the set of reduced fractions \(a/b\) with

\[
 Q\leq b<2Q,\qquad M_D(a,b)>0.
 \tag{10}
\]

An empty final interval is harmless when \(2D\) itself is a power of two. The sets \(\mathcal F_Q\) partition the contributing reduced fractions.

From (7), each denominator in this interval has fewer than \(4Q\) possible numerators, and there are \(Q\) integer denominators before any terminal truncation. Therefore

\[
 |\mathcal F_Q|\leq4Q^2.
 \tag{11}
\]

Distinct reduced fractions in the same interval satisfy

\[
 \left|\frac ab-\frac{a'}{b'}\right|
 =\frac{|ab'-a'b|}{bb'}
 \geq\frac1{bb'}\geq\frac1{4Q^2}.
 \tag{12}
\]

The nonzero integer numerator in (12) requires that the fractions be distinct and reduced. Counting nonreduced pairs directly as if they enjoyed this spacing would be invalid; (9) has already separated their multiplicities.

Put
\[
 I_Q=\sum_{r\in\mathcal F_Q}n(r).
\]

### First incidence bound: count centers for each fraction

The centers incident to a fixed fraction lie in an interval of length \(2\Delta\). Their separation (3) gives

\[
 n(r)\leq 1+\frac{2\Delta X}{c}
       =1+\frac{2c'}c A
       \leq\left(1+\frac{2c'}c\right)A,
 \tag{13}
\]

where the final step uses \(A\geq1\). Equations (11) and (13) give

\[
 I_Q\leq K_1 A Q^2,\qquad K_1=4(1+2c'/c).
 \tag{14}
\]

This estimate allows overlaps between the incidence intervals; it bounds the actual overlap multiplicity instead of assuming the intervals disjoint.

### Second incidence bound: count fractions for each center

For a fixed center, the fractions in \(\mathcal F_Q\) in its closed interval of length \(2\Delta\) are separated by at least \(1/(4Q^2)\). Hence their number is at most
\(1+8\Delta Q^2\), and summing over centers gives

\[
 I_Q\leq J+\frac{8c'JAQ^2}{X}.
 \tag{15}
\]

This spacing bound is valid at both interval endpoints and when its length is smaller than one spacing.

### Take the minimum before summing denominator intervals

For nonnegative \(u,v,w\), \(\min(u,v+w)\leq\min(u,v)+w\). Combining (14)--(15) consequently gives

\[
 I_Q\ll_{c,c'}
 \min(AQ^2,J)+\frac{JAQ^2}{X}.
 \tag{16}
\]

Using the gcd multiplicity bound (8) separately on each interval in (9),

\[
 \begin{split}
 C(A)
 &\leq\sum_{\substack{Q=2^k\\1\leq Q\leq2D}}\frac{2D}{Q}I_Q\\
 &\ll_{c,c'}D
   \sum_{\substack{Q=2^k\\1\leq Q\leq2D}}
       \min(AQ,J/Q)
   +\frac{JAD}{X}
      \sum_{\substack{Q=2^k\\1\leq Q\leq2D}}Q.
 \end{split}
 \tag{17}
\]

Let \(Q_*=\sqrt{J/A}>0\). For \(Q\leq Q_*\), the first summand in (17) is \(AQ\); for \(Q>Q_*\), it is \(J/Q\). The two geometric sums satisfy

\[
 \sum_{\substack{Q=2^k\\1\leq Q\leq2D}}
       \min(AQ,J/Q)\leq4\sqrt{JA}.
 \tag{18}
\]

Here are the endpoint details. The part with \(Q\leq Q_*\) is at most \(2AQ_*=2\sqrt{JA}\). If \(Q_*\geq1\), the part with \(Q>Q_*\) is at most \(2J/Q_*=2\sqrt{JA}\). If \(Q_*<1\), all available intervals belong to the latter part, whose sum is at most \(2J\leq2\sqrt{JA}\), because then \(J<A\). If \(Q_*>2D\), the latter part is empty and the former estimate remains valid. Thus neither cutoff needs to lie in the actual denominator range.

The second geometric sum is bounded by

\[
 \sum_{\substack{Q=2^k\\1\leq Q\leq2D}}Q\leq4D.
 \tag{19}
\]

Substituting (18)--(19) into (17) proves (1). In particular the first term has no logarithmic loss from gcd multiplicities or denominator intervals.

### Weighted dyadic consequence

For \(M=\lfloor\log_2B\rfloor\), apply (1) at \(A=2^m\) and multiply by \(2^{-m}\):

\[
 2^{-m}C(2^m)
 \ll_{c,c'}
 D\sqrt J\,2^{-m/2}+\frac{JD^2}{X}.
 \tag{20}
\]

The first sum over \(0\leq m\leq M\) is bounded by the convergent geometric series
\((1-2^{-1/2})^{-1}D\sqrt J\).
The second has exactly \(M+1\) terms, and
\(M+1\ll\log(2+B)\) for every \(B\geq1\).
This proves (2), with the stated logarithm arising only from the second term.

## 4. First doubtful or unproved step

There is no remaining gap in the incidence bound or its weighted consequence.

Two possible incorrect transitions are specifically excluded:

1. Reduced fractions have reciprocal-square spacing, but the original pairs \((d,e)\) do not. Their full multiplicity is the exact quantity (6), retained in (9) and bounded in (17).
2. The per-center spacing estimate (15) alone would leave a term of order \(JD\) after weighting. The complementary per-fraction estimate (14), and taking the minimum before the dyadic sum, are what prove \(D\sqrt{JA}\).

Any further deduction of character or signed cancellation would need separate hypotheses and reasoning. Nothing in this positive counting argument supplies it.

## 5. Small, degenerate, and endpoint controls

All controls are analytical; no experiment, numerical evaluation, or symbolic computation was run.

| Control | Outcome |
|---|---|
| No centers | \(J=0\) gives \(C(A)=0\) and both bounds are exact. |
| \(D=1\) | The only integer pair is \(d=e=1\). Thus \(C(A)=\#\{l:|1-z_l|\leq\Delta\}\leq\min(J,1+2c'A/c)\ll_{c,c'}\sqrt{JA}\), so the first term already suffices. |
| Real, nonintegral \(D\) | The ceiling formula (6) handles both half-open endpoints exactly. The proof never replaces an exact integer count by an interval length without the valid upper bound (8). |
| One exact rational center | For \(z_1=1\), integer \(D\), and \(\Delta<1/(2D)\), only \(d=e\) are counted, giving \(C(A)=D\). This is the single reduced fraction \(1/1\) with multiplicity \(D\), not one incidence. |
| Necessity of a first term | Taking the preceding control with \(A=1\) and \(X\) much larger than \(D^2\) leaves \(C(1)=D\) while \(D^2/X\) is small. |
| Large-width or small-\(X\) regime | The trivial bound is \(C(A)\leq J(\lceil2D\rceil-\lceil D\rceil)^2\leq4JD^2\). If \(A\geq X\), the second term in (1) already dominates this. In particular \(X=1\) is covered. |
| Necessity of a bulk term | For \(J=X=A=1\), \(z_1=1\), and fixed \(c'>0\), choose \(d,e\) in \([D,(1+\theta)D)\), where \(0<\theta\leq\min(c'/2,1/4)\). All these pairs are incident, giving \(\gg_{c'}D^2\) pairs for large \(D\); a bound by the first term \(D\) alone would fail. |
| Crossover below denominator \(1\) | If \(J<A\), (18) uses the upper geometric tail, bounded by \(2J\leq2\sqrt{JA}\). |
| Crossover above all denominators | If \(J/A>(2D)^2\), the lower geometric part alone proves (18). No artificial nonempty high-denominator range is assumed. |
| Very short incidence intervals | The term \(1\) in (15) retains isolated exact or near incidences even when \(AQ^2/X\ll1\). |
| Overlapping intervals | Equation (13) controls their multiplicity by \(O_{c,c'}(A)\); no disjointness assumption is made. |
| Fractions or centers at endpoints | Closed incidence windows satisfy the ordinary length-over-spacing plus one bound. The half-open denominator and original integer ranges have their own exact conventions. |
| Centers outside the ratio range | All actual fractions lie strictly between \(1/2\) and \(2\); a center whose incidence window misses that range contributes zero. Other centers satisfy the same proof. |
| \(B=1\) | Only \(m=0\) occurs. The factor \(\log(2+B)=\log3\) is a harmless positive constant. |
| Arbitrarily large \(B\) | Every scale \(2^m\) satisfies \(A\geq1\), so (20) remains applicable. The logarithmic upper bound need not be sharp once the trivial count saturates, but remains valid. |

The stated hypotheses have real roles. If \(A\) were allowed to tend to zero with no replacement of \(\sqrt{JA}\) by a term containing \(1+A\), the example \(D=J=X=1,z_1=1\) would have \(C(A)=1\) while the proposed right side tends to zero. Likewise, if center separation were removed, arbitrarily many distinct centers could be placed inside a tiny interval about \(1\); for \(D=A=1\) and \(X\) much larger than \(J\), the count \(J\) would contradict the proposed \(O(\sqrt J+J/X)\) bound.

These checks concern only nonnegative counts. They do not turn upper bounds into lower bounds, and they do not assert cancellation for any choice of character or signed coefficients.

## 6. Exact dependencies and isolation provenance

- Campaign: gc-complete-anchored-divisor-energy, round219.
- Role: independent statement-only rederivation of the isolated fraction-incidence seam.
- Generated date: 2026-09-28, the supplied session date.
- Only files read for this new assignment:
  - protocol.md, SHA256 f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
  - rounds/codex-managed/gc-complete-anchored-divisor-energy/briefs/isolated_fraction_packing_statement.md, SHA256 445f82a9a20accc126798dd9dac406500e973ef41c8d3b305cf0c8131054e74b.
- The earlier anchor report was already frozen at SHA256 83e2f43ad76fe404379d79d308ce3da2b5653151218fdffad458630297150512. It was not reread or edited for this task and is not a mathematical dependency of the proof above.
- Mathematical dependencies: unique gcd reduction, exact integer counts in half-open intervals, the nonzero integer cross-product of two distinct reduced fractions, elementary spacing bounds, and finite/infinite geometric sums.
- No current application, conductor proof, claimant report, graph, manifest, strategy, source, or sibling was read. No web search, experiment, new agent, shared-state edit, or successor work was performed. Only the assigned review was written.

**Prior-history disclosure.** This agent retains prior round217 source/frontier and seam-review context, round218 abstract radial and packet-coherence work, and its own preceding round219 exact-anchor derivation. It is not a fresh history-free agent. The present fraction-packing derivation is statement-only as to this new lemma: no claimant argument or current application was supplied or inspected.

## 7. Recommended state effect

**Recommend promote the exact unsigned incidence bound (1) and its weighted dyadic consequence (2), subject to the conductor's ordinary seam and graph procedures.**

The proof accounts for gcd multiplicity, real parameter endpoints, all positions of the balancing denominator, and arbitrarily large dyadic upper limits. It supports no character or signed cancellation conclusion.

No state mutation, application claim, synthesis, or next-round decision is made. The assigned isolated seam ends with this report.
