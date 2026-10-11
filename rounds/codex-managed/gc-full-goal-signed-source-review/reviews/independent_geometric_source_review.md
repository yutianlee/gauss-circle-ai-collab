# Round 223: independent geometric source review

## 1. Result

**Scoped GREEN after two transcription repairs.** This review binds the final report geometric_complete_frontiers.md at SHA-256

d68dc0c22687522cb31d78bee822ae0916924f55740634d96956f92e7de92c0c.

The exact product completion, actual coefficient norms, full-frequency Pascadi comparisons, legal FKMS variable orientation and restored prime power are correct. The tested estimates do not improve the inherited complete bounds after their stated absolute summations. This is a conclusion about those sufficient upper certificates, not an actual signed lower bound or a universal prohibition on either source.

The initial reviewed hash was 3cbf35984b7689e7b5c075e2775389bc1379932c2c37b7b12ed43e805582f070. The final version corrects the literal SMOOTH label to \(D=\lfloor\sqrt X\rfloor/2\), and the historical-source reference to rounds 220/217. Neither change alters a power comparison. No additional mathematical correction is required.

This is a nonblind, claimant-avoiding review by a reused agent. I authored earlier source/analytic reports, including round 222's product-phase report, and round 223's isolated oscillatory-transfer report and other assigned reviews. I am not independently reviewing those authored artifacts here. The present claimant is different. The conductor disclosed its prior formula/algebra checks and flagged the two transcription issues; the derivations below were checked independently. Allocation: analytical/source verification only, zero experiments.

## 2. Exact statement and hypotheses

The certified claim is restricted to the accepted flat inverse-selector component and the report's displayed theorem applications and partitions. Put
\[
 X=N_0+\xi,\quad N_0=\lfloor X\rfloor,\quad 0\le\xi<1,\qquad
 R=X/D,\quad K=XL/D^2,\quad \Delta=D/L.
\]
Rows have odd \(g,n\), \(gn\asymp R\), unit \(j\bmod n\), and literal zero-extended coefficients
\[
 b_j=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n),\qquad j\asymp J=K/g.
\]
The strict flat range gives \(\Delta>X^{1/4}\). Consequently fixed support constants do not cause residue collisions for sufficiently large \(X\). Bounded or empty rows retain their inherited elementary treatment.

Pascadi's [versioned Theorem 7.1](https://arxiv.org/html/2511.08445v2) has exactly the report's factorization, maximal square divisor, interval lengths, unit parameter and joint gcd condition. Its displayed three terms and sixth root agree. Theorem 1.2 is the stated short-interval specialization.

FKMS's [versioned Theorem 1.3(2)](https://arxiv.org/html/2511.09459v3) has exactly the report's prime field, dyadic coefficient vectors, two length restrictions, and dependence on fixed \(l\), exponents and sheaf complexity. Definition 1.2 requires irreducible gallant monodromy; lightness includes the stated weight conditions. Sections 9.5--9.6 justify nonzero dilations of the normalized rank-two Kloosterman example. No rank-one or arbitrary arithmetic mask is granted that status.

The applicability test is on each literal dyadic \(j\)-scale, with its integer endpoints and the printed constants, not merely on an asymptotic relation \(j\asymp J\). Ineligible pieces remain in the inherited complement.

## 3. Proof and cost verification

With the inverse-first convention, expand the finite completion:
\[
 \frac1n\sum_j b_j\sum_{x\bmod n}^{*}e(N_0\bar x/n)
                  \sum_{h\bmod n}e(h(x-\bar j)/n)
 =\sum_j b_j e(N_0j/n).
\]
The inner orthogonality forces \(x=\bar j\), hence \(\bar x=j\). It does not produce \(e(N_0\bar j/n)\). The coefficient's \(e(\xi j/n)\) restores the exact real centre \(X\).

For each unit \(j\), \(h=jv\bmod n\) is a bijection of all residues. Substitution \(x=\bar j u\) gives
\[
 S(N_0,jv;n)=S(N_0j,v;n),\qquad
 U_{g,n}=\frac1n\sum_j b_j\sum_{v\bmod n}e(-v/n)S(N_0j,v;n).
\]
Thus the two coefficient vectors really factor. Nonunit \(v\) are included. The full second vector has norm \(\sqrt n\); a \(V\)-entry interval has norm \(\sqrt V\). The zero residue satisfies \(h=0\) if and only if \(v=0\), and its contribution is \(c_n(N_0)n^{-1}\sum_j b_j\). The accepted kernel owns its target-safe removal once globally. Removing it does not remove positive nonzero aliases.

The literal amplitude gives
\[
 \|b\|_1\ll X^\varepsilon/g,\qquad
 \|b\|_2\ll X^\varepsilon(gK)^{-1/2}.
\]
These are upper bounds, with no lower buffer assumed. Distinct supported residues and finite Parseval give
\[
 \|\widehat\gamma\|_2=n^{-1/2}\|b\|_2,\qquad
 \sum_{h\bmod n}|S(N_0,h;n)|^2=n\varphi(n).
\]
The latter follows by forcing equal \(x\)'s and needs no coprimality between \(N_0\) and \(n\). Hence the inherited row ceiling is \(\sqrt{\varphi(n)}\|b\|_2\ll X^\varepsilon\sqrt\Delta/g\). Counting \(O(R/g)\) rows and summing \(g^{-2}\) costs \(X^\varepsilon R\sqrt\Delta=X^{1+\varepsilon}/\sqrt{DL}\). Direct completion also gives the smaller elementary ceiling \(X^\varepsilon R\). Neither is a claim about the signed output size.

For Pascadi, use \(c=n,a=N_0\) only on \((N_0,n)=1\). Since \(j\) is a unit, the joint gcd condition holds for every \(v\). At length \(\sqrt n\), the sum of \(v\)-norms is of order \(n^{3/4}\); partitioning \(j\) has the stated Cauchy upper charge \(\max(1,\sqrt J/n^{1/4})\). After \(1/n\), the displayed short-interval certificate is
\[
 n^{3/4+o(1)}F_n\|b\|_2\max(1,\sqrt J/n^{1/4}).
\]
Here \(d^2\mid nd\), so \(f\ge d\), while \(\min(n,d^2)\le d\sqrt n\). Therefore \(F_n\ge n^{-1/12}\). Its favorable expression is already \(n^{2/3+o(1)}\|b\|_2\), worse than the old \(n^{1/2}\|b\|_2\) price.

For the full \(v\)-interval, the theorem's bracket becomes \(dJ+f+f/d^2\). For comparable intervals of length \(V\), their norm sum is of order \(n/\sqrt V\). The first term of the theorem alone gives the following ratio of the resulting certificate expression to \(\sqrt n\|b\|_2\):
\[
 \begin{cases}
 (dJ)^{1/6},&V\ge J,\\
 d^{1/6}J^{1/2}V^{-1/3},&V<J.
 \end{cases}
\]
Both are at least one; integer end pieces change constants only. Swapping variables is legal because the source parameter is a unit. This proves the advertised comparison for this partition strategy, without claiming optimality among all signed uses of Pascadi.

For FKMS, let \(n=p\) be prime and \(p\nmid N_0\). With \(x=N_0y\),
\[
 p^{-1/2}S(N_0,t;p)=\mathrm{Kl}_2(N_0t;p).
\]
This is an eligible bounded-complexity dilation. The zero frequency has already been separated, so no value at the singular argument is silently used. Set the theorem's long variable to \(v\) and short variable to \(j\), with exponents both one. The range \(1\le v<p\) contains an actual dyadic block of length comparable to \(p\), even if its final dyadic piece is short. No translation of \(K(jv)\) is needed.

The factors \(1/p\) from completion, \(\sqrt p\) from the unnormalized Kloosterman sum, and \(\sqrt p\) from the long coefficient norm leave
\[
 p^\varepsilon\sqrt{pJ}\|b\|_2
 \left[p^{-1}+
       \left(p^{-1/4+7/(4l)}/J\right)^{1/l}\right]^{1/2}.
\]
The second summand's ratio to the old row expression is
\[
 J^{(l-1)/(2l)}p^{-1/(8l)+7/(8l^2)}
 \gg_l p^{(5l+1)/(8l^2)}
\]
on the eligible lower length range. The exponent follows by inserting \(J\ge10p^{3/(2l)}\). It is positive for every fixed eligible \(l\). Subsequent absolute summation over the other intervals cannot lower this particular certificate expression. Nothing here bounds the actual mandatory block from below.

If \(p\mid N_0\), the nonzero-frequency trace degenerates to a Ramanujan sum; it is not the asserted gallant family. Composite moduli, prime powers, unit failures and ineligible lengths keep the old bounds. A CRT extension is not supplied. Oddness removes even \(g,n\) only from this exact flat representation, not from independent frontiers.

Finally, in the report's strict region \(a=\delta-\ell\in(1/4,1/2)\), the accepted flat exponent is \(\min(a,(1-a)/2)>1/4\). The row-norm exponent \(1-(\delta+\ell)/2>5/8\), since \(\delta+\ell<3/4\). The physical-to-dual restoration is \((LK)^{3/4}X^{-1/4}\). The original-side fallback \(\min(D,\sqrt{XL/D})+O(1)\) is at most \(X^{3/8+\varepsilon}\) on its active triangle. Its scope is the exhibited original expression and verified cuts; an unrepresented correction retains its own owner and estimate.

## 4. First doubtful or unproved step

There is no remaining gap in the reviewed finite identity or displayed certificate comparisons. The first unproved positive step is a saving for the actual signed full-frequency/outer-row vector before those absolute norms, together with transfer to every complete UNBAL companion. The sources are not proved to supply that saving here.

HARD, SMOOTH, TOP, BAL, UNBAL and the GAR estimate remain distinct open owners. The proved GAR recombination identity is not the open global angular-radial estimate. Paying total M1 would not pay M2 or promote both blockwise M1 parents. The fixed twelfth-moment milestone is not the sufficient unbounded family of fixed even orders. These ownership distinctions are retained.

The two corrected transcription issues are resolved in the final binding. The conductor supplied the historical round-number correction; I verified the resulting text without opening the unassigned historical source report.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Completion sign and direct versus inverse \(j\) | GREEN by finite orthogonality and the exact substitutions. |
| Units, gcd failures, parity, real centre | GREEN; conditions are imposed only where needed, complements retained. |
| Moving coefficient masks and norms | GREEN as upper norms of the actual vector; no profile lower bound inferred. |
| Full and partitioned Pascadi powers | GREEN for the displayed triangle partitions, including all \(v\)-norms and \(1/n\). |
| FKMS geometry, variable swap and prime loss | GREEN; fixed complexity/order, literal eligible dyadic scales and mandatory long block included. |
| Zero residue and all remaining aliases | GREEN; the inherited Ramanujan deletion occurs once. |
| Physical normalization and original fallback | GREEN in the stated original-expression scope; no unspecified package certified. |
| Actual versus certificate scope | GREEN; no actual signed lower bound, arbitrary weighted rank lower bound or universal source no-go. |
| Complete owners | GREEN; graph status remains open for the required estimates. |
| Literal labels and provenance | GREEN after the two recorded repairs. |

All controls are algebraic or source-hypothesis checks. No numerical experiment or source-proof reconstruction was performed.

## 6. Dependencies and exact artifacts

Campaign: gc-full-goal-signed-source-review, round 223. Role: independent_geometric_source_review. Review date: 28 September 2026, Asia/Shanghai. Only the authorized target, protocol, accepted inverse-selector kernel, closed 222 synthesis, restricted graph ownership lookups and the two versioned primary sources were read for this task.

| Artifact | SHA-256 |
|---|---|
| Final reports/geometric_complete_frontiers.md | d68dc0c22687522cb31d78bee822ae0916924f55740634d96956f92e7de92c0c |
| Initial target, superseded for this binding | 3cbf35984b7689e7b5c075e2775389bc1379932c2c37b7b12ed43e805582f070 |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md | 584745fb9af72993a4b33eb95dad3421e8924ae5fb64c5b314511b08d4254baf |
| rounds/codex-managed/m9-m2-complete-unbalanced-vector/synthesis.md | 829f1ed9af8ca637345332028707723b5bce22cb7268238f40a1a1a9bcc64377 |
| state/proof_obligations.yml, status lookups only | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |

Primary statements: [Pascadi 2511.08445v2, Theorems 7.1 and 1.2](https://arxiv.org/html/2511.08445v2), and [FKMS 2511.09459v3, Definition 1.2, Theorem 1.3(2), Sections 9.5--9.6](https://arxiv.org/html/2511.09459v3). The [Pascadi version record](https://arxiv.org/abs/2511.08445v2) gives 21 June 2026 and the [FKMS version record](https://arxiv.org/abs/2511.09459v3) gives 11 March 2026; an internal body date does not change the binding.

No other current sibling, new source, shared-state edit or successor task was used. Prior authorship/history and conductor interventions are disclosed in Sections 1 and 4.

## 7. Recommended state effect

**Retain the report as scoped GREEN method evidence; no analytic parent or exponent promotion.** Retain all existing owners and inherited estimates. Reject only the claimed improvement from these tested absolute full-frequency/outer-row applications, were such an improvement asserted. A different genuinely signed use remains open.

The complete GAR recommendation is a possible conductor objective, not a demonstrated mechanism, theorem or successor authorization. This review ends with its frozen artifact and makes no shared-state change.
