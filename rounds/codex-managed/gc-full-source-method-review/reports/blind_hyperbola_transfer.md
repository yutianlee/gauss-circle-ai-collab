# Round 211: statement-only complete hyperbola transfer

## 1. Result: conditional lemma

- Campaign: gc-full-source-method-review; round: 211.
- Task/role: blind_hyperbola_transfer, statement-only independent rederivation.
- Generated: 2026-09-28.
- Graph hash: not supplied in the isolated packet; the graph was not accessed.
- Exact context read: protocol.md and rounds/codex-managed/gc-full-source-method-review/briefs/blind_hyperbola_statement.md only.
- Status: proved implication from the packet's explicitly hypothetical inputs. No input theorem is proved here.
- Effort: entirely analytical; no numerical experiment.

Put
\[
 \beta=\frac{\lambda}{2}-\frac14,\qquad
 \delta=\min\left\{\frac16,\frac{\kappa+\beta}{1+2\beta}\right\}
 =\min\left\{\frac16,\frac{4\kappa+2\lambda-1}{4\lambda+2}\right\}.
\]
The formal exponential-sum hypothesis in the packet implies the complete block bound
\[
 \boxed{|F_N(R)|\ll_\varepsilon T^{\kappa+\varepsilon}
                   N^{\lambda/2-1/4}.}                         \tag{1}
\]
This includes both divisor arms. With the two additional, supplied complementary and reconstruction hypotheses, it implies
\[
 \boxed{|P(R^2)|\ll_\varepsilon T^{1/2+\delta+\varepsilon},\qquad
 |P(X)|\ll_\varepsilon X^{1/4+\delta/2+\varepsilon}
 \quad (X=R^2).}                                             \tag{2}
\]
The second assertion uses the fixed comparison \(R\asymp T\). Constants may depend on the formal pair and on the fixed functions and comparison bounds.

The strict criterion for this certificate to improve a radius-wave threshold \(b\in(0,1/6)\), meaning that the block-sum exponent is strictly less than \(b\), is
\[
 \boxed{4\kappa+2(1-2b)\lambda<1+2b.}                         \tag{3}
\]
Replace \(<\) by \(\le\) for a certificate of exponent at most \(b\). In particular, strict improvement over \(1/6\) occurs precisely when \(3\kappa+\lambda<1\).

A family of valid formal inputs whose pairs approach \((0,1/2)\), together with the two other supplied hypotheses, suffices for the full quantified quarter theorem
\[
 \forall\eta>0\quad |P(X)|\ll_\eta X^{1/4+\eta}.
                                                                  \tag{4}
\]
One fixed pair other than \((0,1/2)\) has \(\delta>0\) and does not give (4) by this certificate. This last conclusion concerns what these upper bounds certify, not a lower bound for the actual error.

## 2. Exact statement and hypotheses

Fix \(0<c<C<\infty\), \(T\ge2\), \(1\le N\le T\), and \(cT\le R\le CT\). Let \(v\) be fixed smooth with support in \([1,4]\), and let \(\Psi\) be the fixed real Schwartz function, smooth at zero, in the packet. All these parameters are real; no integrality of \(T,N,R\) is imposed.

The complete block is exactly
\[
 F_N(R)=4\sum_{d,m\ge1}\chi_4(d)(dm)^{-3/4}
 \Psi\!\left(\sqrt{\frac{dm}{T}}\right)v\!\left(\frac{dm}{N}\right)
 e(R\sqrt{dm}).
                                                                  \tag{5}
\]
Only terms with \(N\le dm\le4N\) can contribute. Endpoint values are retained even if smooth support happens to make them zero.

Write \(s=\lambda-\kappa\in[0,1]\). The sole analytic input used to prove (1) is the packet's bound for every partial interval in a square-root phase interval at scale \(K\):
\[
 \sup_J\left|\sum_{k\in J}e(A\sqrt{k/K})\right|
 \ll_\varepsilon
 (A^\kappa K^{s}+K/A)T^\varepsilon,\qquad K\ge1,\ A\ge K.       \tag{6}
\]
Here positive arguments remain in fixed compact multiples of \(K\), and the exact uniform fixed rescalings and shifts needed for the two nonzero residue classes modulo four are included, as stipulated by the packet. Short intervals with a bounded number of integers may be treated trivially. No arbitrary-coefficient version of (6) is assumed.

For transparency, an explicit finite-cutoff certificate underlying (1) is as follows. For any integer \(1\le D\le4N\), set
\[
 M_D=\left\lfloor\frac{4N}{D+1}\right\rfloor,\quad
 H_\sigma(L)=\sum_{u=1}^{L}u^{-\sigma},\quad H_\sigma(0)=0,
 \quad A=R\sqrt N.
\]
For \(T\) sufficiently large in terms of \(c\),
\[
 |F_N(R)|\ll_\varepsilon N^{-3/4}T^\varepsilon
 \left[
 A^\kappa N^s\{H_s(D)+H_s(M_D)\}
 +\frac{N}{A}\{H_1(D)+H_1(M_D)\}
 \right].                                                     \tag{7}
\]
The remaining bounded range of \(T\) satisfies (1) directly with a changed constant.

Equations (2)--(4) additionally assume, rather than establish,
\[
 |F_N(R)|\ll_\varepsilon T^\varepsilon
      \min\{N^{1/4},(T/N)^{1/2}\},                              \tag{8}
\]
and
\[
 |P(R^2)|\ll_\varepsilon T^{1/2+\varepsilon}
 \left[1+\sum_{\substack{\text{dyadic}\\1\le N\le T}}|F_N(R)|\right].
                                                                  \tag{9}
\]
The singleton and the entire \(N>T\) tail are paid by the \(1\) in (9), solely because that is part of the supplied reconstruction hypothesis.

## 3. Proof and derivation

### A. An exact, disjoint hyperbola identity with real endpoints

Define
\[
 a=\frac NT,\qquad h_a(t)=t^{-3/4}\Psi(\sqrt{at})v(t).
\]
For \(u>0\), define integer endpoints
\[
 L_u=\max\left\{1,\left\lceil\frac Nu\right\rceil\right\},\qquad
 U_u=\left\lfloor\frac{4N}{u}\right\rfloor.
\]
An integer sum with its lower endpoint exceeding its upper endpoint is zero. The exact identity is
\[
\begin{split}
 \frac{F_N(R)}4=N^{-3/4}\bigg[
 &\sum_{d=1}^{D}\chi_4(d)
    \sum_{m=L_d}^{U_d}h_a(dm/N)e(R\sqrt{dm})\\
 &+\sum_{m=1}^{M_D}
    \sum_{d=\max\{D+1,L_m\}}^{U_m}
       \chi_4(d)h_a(dm/N)e(R\sqrt{dm})
 \bigg].                                                       \tag{10}
\end{split}
\]
Indeed, every pair in (5) either has \(d\le D\), when it occurs exactly once in the first arm, or \(d\ge D+1\). In the latter case \(dm\le4N\) forces
\[
 m\le\left\lfloor\frac{4N}{D+1}\right\rfloor=M_D,
\]
and the second arm includes exactly that pair. Conversely, every pair in (10) has positive integer coordinates and \(N\le dm\le4N\). The two alternatives for \(d\) are disjoint. There is no overlap to discard and no third, uncontrolled complement.

### B. The complete smooth amplitude has uniform bounded variation

For \(0<a\le1\) and \(1\le t\le4\), both \(h_a(t)\) and its total variation are uniformly bounded:
\[
 \sup_{[1,4]}|h_a|+\int_1^4|h_a'(t)|\,dt\ll_{v,\Psi}1.          \tag{11}
\]
For example,
\[
\begin{split}
h_a'(t)={}&-\tfrac34t^{-7/4}\Psi(\sqrt{at})v(t)
 +t^{-3/4}\Psi'(\sqrt{at})\frac{\sqrt a}{2\sqrt t}v(t)\\
 &+t^{-3/4}\Psi(\sqrt{at})v'(t).
\end{split}
\]
All arguments of \(\Psi,\Psi'\) lie in \([0,2]\), and the factor \(\sqrt a\le1\) precludes an \(a\downarrow0\) loss. This explicitly uses smoothness at zero.

If the outer variable is \(u\), put \(K=N/u\). The inner weight is
\[
 w_u(z)=N^{-3/4}h_a(z/K).
\]
On any clipped inner interval in (10),
\[
 \|w_u\|_\infty+\int|w_u'(z)|\,dz\ll N^{-3/4}.                \tag{12}
\]
Thus Abel partial summation bounds a weighted inner sum by \(O(N^{-3/4})\) times the supremum of its unweighted partial sums. The endpoint term in Abel summation is included in the supremum norm in (12). The sharp lower cutoff \(d\ge D+1\) is an interval endpoint, not a differentiable amplitude; it is handled by the partial-interval uniformity of (6).

This is a proved extension from unweighted sums to these particular bounded-variation amplitudes. It does not posit an arbitrary smooth-weight theorem, much less an arbitrary-coefficient theorem.

### C. First arm: inner \(m\); second arm: inner \(d\) in two residue classes

In either arm the inner phase has the common amplitude
\[
 R\sqrt{uz}=A\sqrt{z/K},\qquad A=R\sqrt N,\quad K=N/u.          \tag{13}
\]
The first arm has the outer factor \(\chi_4(d)\), whose absolute value is at most one, and an unweighted inner exponential sum in \(m\). Equations (6) and (12) give its weighted inner bound.

In the second arm use the exact identity
\[
 \sum_{d\in J}\chi_4(d)w_m(d)e(A\sqrt{d/K})
 =\sum_{\substack{d\in J\\d\equiv1\ (4)}}w_m(d)e(A\sqrt{d/K})
  -\sum_{\substack{d\in J\\d\equiv3\ (4)}}w_m(d)e(A\sqrt{d/K}).
                                                                  \tag{14}
\]
For \(r=1,3\), writing \(d=4j+r\) gives
\[
 e\!\left(A\sqrt{\frac{j+r/4}{K/4}}\right).
                                                                  \tag{15}
\]
When \(K\ge4\), the scale \(K/4\ge1\), the positive shifted arguments are comparable to \(K/4\), and the stipulated residue-class version of (6) applies uniformly. The interval endpoints in \(j\) are exactly the corresponding ceilings and floors; no endpoint is rounded into the sum. The transformed amplitude has the same bounded total variation, since change of variable preserves its variation.

The factor \(4\) in the scale changes the two terms in (6) only by fixed constants. Adding the two residue-class upper bounds therefore costs only a fixed factor. When \(K<4\), the original support \(z\in[K,4K]\) has a bounded number of integers and is treated trivially.

There is no use here of cancellation between the two residue classes. The periodic structure matters because it reduces the coefficient to finitely many explicitly permitted phase restrictions. Arbitrary coefficients cannot be inserted into (6): for example coefficients \(c_z=e(-A\sqrt{z/K})\) would turn the corresponding exponential sum into its full interval length. Their variation is not uniformly bounded as in (12).

For sufficiently large \(T\), \(A\ge N\), since
\[
 \frac AN=\frac R{\sqrt N}\ge c\sqrt T.
\]
Consequently \(A\ge K\) for all inner scales \(K=N/u\le N\) to which (6) is applied, and also for \(K/4\). If \(T\) is below this fixed threshold, \(N\le T\) belongs to a bounded range and (5) gives a bounded trivial estimate, absorbed into (1). Thus small \(R/T\) within the fixed positive compact interval creates no unverified application of the condition \(A\ge K\).

For arbitrary admissible \(D\), all nonempty outer ranges satisfy \(u\le4N\), so \(K\ge1/4\). The small-scale trivial bound is absorbed into \(A^\kappa K^s\), because \(A\ge1\), \(s\in[0,1]\), and \(K\ge1/4\). Similarly, an actual clipped interval containing only \(O(1)\) integers costs \(O(N^{-3/4})\), including when its ambient \(K\) is large; then \(A^\kappa K^s\ge1\). Combining these cases, each weighted inner sum is bounded by
\[
 \ll_\varepsilon N^{-3/4}T^\varepsilon
       \left\{A^\kappa(N/u)^s+\frac{N/u}{A}\right\}.            \tag{16}
\]
Equation (16) for \(K<1\) comes from the stated trivial argument, not an enlargement of the range of (6).

### D. Restore both outer sums; optimize the cutoff and price the residuals

Summing (16) over \(d\le D\) and \(m\le M_D\) proves (7), with the original arithmetic factor \(4\) absorbed in the constant. No count in either arm is omitted.

Choose the integer cutoff
\[
 q=\lfloor2\sqrt N\rfloor,\qquad D=q.
\]
It satisfies \(1\le q\le4N\) for every real \(N\ge1\). Since
\[
 q^2\le4N<(q+1)^2,
\]
the exact other-arm endpoint satisfies
\[
 M_q=\left\lfloor\frac{4N}{q+1}\right\rfloor\in\{q-1,q\}.      \tag{17}
\]
Thus both outer lengths are \(O(\sqrt N)\), without replacing an integer endpoint by a real one in the identity.

If \(s<1\), then \(H_s(L)\ll_s L^{1-s}\). If \(s=1\), then \(H_1(L)\ll\log(2L)\); within the allowed pair range \(s=1\) occurs only at \((\kappa,\lambda)=(0,1)\). Define
\[
 \mathcal L_s(N)=
 \begin{cases}
 1,&s<1,\\
 \log(2N),&s=1.
 \end{cases}
\]
Equation (7) gives
\[
 |F_N(R)|\ll_\varepsilon T^\varepsilon
 \left\{
 R^\kappa N^{\lambda/2-1/4}\mathcal L_s(N)
 +R^{-1}N^{-1/4}\log(2N)
 \right\}.                                                     \tag{18}
\]
The exponent calculation is
\[
 N^{-3/4}A^\kappa N^sN^{(1-s)/2}
 =R^\kappa N^{-3/4+\kappa/2+(s+1)/2}
 =R^\kappa N^{\lambda/2-1/4}.
\]
The second term is the complete sum of the \(K/A\) residuals, since
\[
 N^{-3/4}(N/A)\log(2N)=R^{-1}N^{-1/4}\log(2N).
\]

If one accounts for all bounded-length intervals separately instead of absorbing them in (16), their total additional cost is at most
\[
 N^{-3/4}(q+M_q)\ll N^{-1/4}.                                 \tag{19}
\]
This explicitly prices every such interval, including both residue classes in the second arm. There is no separate rounding error: (17) uses the exact rounded cutoff and exact integer outer endpoint. There is also no smoothing or truncation error in (10).

Because \(\kappa,\beta\ge0\), the principal power \(T^\kappa N^\beta\) is at least one. It absorbs (19) and the residual in (18); logarithms are absorbed by arbitrarily small powers of \(T\), using \(N\le T\). Relabeling the input epsilon proves (1).

The chosen cutoff is optimal for the power of \(N\) in this positive upper certificate. Indeed, for every admissible \(D\), either \(D\ge\sqrt N\), or
\[
 M_D\ge\left\lfloor\frac{4N}{\sqrt N+1}\right\rfloor
       \ge\lfloor2\sqrt N\rfloor\ge\sqrt N.
\]
Therefore \(H_s(D)+H_s(M_D)\gg_s N^{(1-s)/2}\) for \(s<1\), and it is \(\gg\log(2N)\) for \(s=1\). The balanced choice achieves these orders. Finite floors can move the exact numerical minimizer away from \(q\); an exact minimizer, if desired, is the minimum over the explicit finite expression (7). No such movement improves its uniform power. This lower bound on the *positive cost expression* is not a lower bound for \(|F_N|\).

### E. Optimize the supplied complete block envelope

Combine (1) and (8), and write \(N=T^a\), \(0\le a\le1\). Up to \(T^\varepsilon\), the available exponent is
\[
 f(a)=\min\left\{\frac a4,\frac{1-a}{2},\kappa+\beta a\right\}.
                                                                  \tag{20}
\]
There are \(O(\log T)\) dyadic blocks, so the complete block sum is bounded by \(T^{\max_{[0,1]}f+\varepsilon}\).

The first line increases and the second decreases; they meet at \(a=2/3\), with value \(1/6\). The third line is nondecreasing. If
\[
 \kappa+\frac23\beta\ge\frac16,
\]
the peak remains \(1/6\). Otherwise the maximum is at the intersection of the second and third lines:
\[
 a_*=\frac{1-2\kappa}{1+2\beta}\in(2/3,1],\qquad
 f(a_*)=\frac{\kappa+\beta}{1+2\beta}.
\]
The endpoint \(\kappa=\beta=0\) gives maximum zero. These cases prove exactly
\[
 \max_{0\le a\le1}f(a)=\delta.
\]
This is the optimum of the displayed upper envelope, not an assertion that any block has this size. Because dyadic logarithms have vanishing spacing on the \(a\)-scale as \(T\) grows, replacing the continuous maximum by the finite dyadic maximum does not yield a fixed power improvement.

For \(0<b<1/6\), the relation \(\delta<b\) is equivalent to
\[
 \kappa+(1-2b)\beta<b,
\]
which after substituting \(\beta=(2\lambda-1)/4\) is precisely (3). At \(b=1/6\), its limiting strict condition simplifies to \(3\kappa+\lambda<1\).

### F. Complete reconstruction and the quantifier at the quarter exponent

Insert the full dyadic estimate into (9):
\[
 |P(R^2)|\ll_\varepsilon
 T^{1/2+\varepsilon}\{1+T^{\delta+\varepsilon}\}.
\]
Here \(\delta\ge0\), so the supplied singleton-and-tail cost \(1\) is included, also at \(\delta=0\). Relabeling epsilon and using \(R\asymp T\), \(X=R^2\), gives (2). The conversion from radius to squared-radius exponent divides the additional exponent \(\delta\) by two.

Suppose there is a family of pairs \((\kappa_j,\lambda_j)\to(0,1/2)\) for which the *full uniform input (6)* holds separately for every pair. Then \(\delta_j\to0\). Given any \(\eta>0\), first fix one pair with \(\delta_j/2<\eta/2\), then choose the epsilon losses in (6), (8), (9), and the logarithm absorptions so that the remaining squared-radius loss is less than \(\eta/2\). This proves (4). Pair-dependent constants become part of the final constant \(C_\eta\); no uniformity across the family and no rate of approach are needed.

For any single fixed allowed pair other than \((0,1/2)\), one has \(\kappa+\beta>0\), hence \(\delta>0\). Its fixed loss cannot be renamed an arbitrarily small epsilon. Such a pair may prove a strong fixed improvement, but this chain of estimates alone does not prove (4). Conversely, the endpoint pair itself, if supplied with the required uniform input, would suffice. A family approaching it does not establish the endpoint estimate without epsilon, nor an exact \(O(X^{1/4})\) bound.

## 4. First doubtful or unproved step

There is no identified doubtful algebraic, endpoint, or summation step in the implication above. The first unproved analytic step, if this were presented as an unconditional argument, is application of the formal input (6) for the chosen pair, with its full partial-interval, parameter, and residue-class uniformity.

The complementary estimate (8) and the complete reconstruction (9) are two further independent unproved inputs here. In particular, this report supplies no proof of the singleton/tail treatment inside (9). A family of admissible pairs approaching \((0,1/2)\) is also only a conditional supposition. None of these assumptions may be promoted by citing this report.

## 5. Required controls and outcomes

1. **Exact coverage of both arms — PASS.** Identity (10) partitions by the disjoint integer alternatives \(d\le D\) and \(d\ge D+1\). The latter forces the exact upper endpoint \(M_D\); every pair is present once. No short-divisor complement is silently assumed.
2. **Period four versus arbitrary coefficients — PASS.** Equations (14)--(15) use exactly two permitted residue-class phases. No cancellation across these classes is claimed. An arbitrary coefficient can undo the phase and is outside the argument. This transfer could also be obtained with an unsigned divisor coefficient if the corresponding scalar input holds; it is not an arithmetic-sign cancellation theorem.
3. **Real endpoints and rounding — PASS.** Every inner interval uses \(\lceil N/u\rceil,\lfloor4N/u\rfloor\), and the second arm uses \(D+1\). Equation (17) is exact for real \(N\). Bounded \(T\) is separated before enforcing \(A\ge K\).
4. **Amplitude derivatives, partial summation, and short lengths — PASS.** Equations (11)--(12) retain \(n^{-3/4}\), \(\Psi(\sqrt{n/T})\), and \(v(n/N)\). Input (6) controls every partial interval needed by Abel summation. Small scales \(K<4\), residue endpoints, and clipped \(O(1)\)-length intervals are treated trivially and are priced by (19), or absorbed termwise in (16).
5. **Optimization is an upper-certificate statement — PASS.** The lower comparison in part D is solely for the nonnegative cost in (7). It does not prohibit extra cancellation or prove a lower bound for \(F_N\). The optimization in part E likewise optimizes only the supplied upper envelope.
6. **Complete reconstruction — PASS, conditional on (9).** Both arms, both residual sums, all dyadic \(1\le N\le T\) blocks, the factor \(T^{1/2}\), and the supplied \(1\) for singleton and \(N>T\) tail are included. The final \(X\)-exponent is \(1/4+\delta/2\), not \(\delta\) or \(1/4+\delta\).
7. **Full-quarter quantifier — PASS.** A family approaching the endpoint allows a pair to be fixed after the target epsilon is specified. One fixed nonendpoint pair leaves a positive fixed loss. Neither observation is a claim about the truth or falsity of the actual quarter theorem.

These are exact analytical controls; there is no computational evidence to archive.

## 6. Dependencies and exact artifacts used

- protocol.md: the round and seven-section reporting rules; evidence remains distinct from accepted proof state.
- rounds/codex-managed/gc-full-source-method-review/briefs/blind_hyperbola_statement.md: the complete block definition, divisor identity, formal square-root input with allowed residue restrictions, complementary bound, reconstruction bound, and requested controls.
- Elementary tools proved or used explicitly in this report: disjoint finite summation, the residue values of \(\chi_4\), the chain rule, Abel partial summation, integral estimates for harmonic sums, and optimization of three affine functions.

No graph, active-campaign file, generated general brief, strategy, prior or sibling report, web source, or unlisted mathematical input was accessed. The only written artifact is this task report.

## 7. Recommended state effect

**Retain the conditional transfer lemma and its complete exponent/quantifier calculation for conductor review.** Subject to the independent required seam reviews, the finite hyperbola identity and the proved implication from the explicitly stated hypotheses are candidates for acceptance as conditional statements.

**No change** to the truth status of any formal exponent pair, the supplied complementary estimate, the supplied complete reconstruction, a family approaching the endpoint, or the quarter theorem. No authoritative state file was edited, and no successor round is proposed or started.
