# Preliminary hostile TTY-corridor review

- Campaign: `m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate`
- Round: 151
- Role: independent hostile seam reviewer
- Verdict: **GREEN**
- First failed step: **none in the stated low-\(L\) full-row component**.  The first unowned continuation is the complementary \(L>L_0\) row; interpreting the estimate as an isolated large-wrap-collar bound would be a scope failure.

## 1. Result

The proposed estimate is correct with the precise scope below.  For the actual retained Round-148 profile, not for an arbitrary bounded smooth coefficient, one has uniformly in the row, prefix, and supported \(L\)

\[
 \|\mathscr W_{d,U,L}\|_\infty+
 \operatorname{Var}_q(\mathscr W_{d,U,L})
 \ll_\varepsilon X^\varepsilon.
\]

Resolving \((L,q)=1\) by divisor inclusion and \(\chi _4\) by its two odd residue classes gives

\[
 |S_{d,L}|
 \ll_\varepsilon
 E^{89/1282}Q^{997/1282}L^{908/1282}X^\varepsilon.
\]

The accepted half-weight norm then gives

\[
 |G_{\leq L_0}(d)|
 \ll_\varepsilon
 E^{89/1282}Q^{997/1282}L_0^{267/1282}X^\varepsilon.
\]

Consequently its \(d\)-energy is at most \(R^2D X^\varepsilon\) whenever

\[
 \boxed{M^{819}\geq R^{1424}D^{1816}L_0^{534}}.
\]

This is a genuine strict corridor for the complete unexpanded low-\(L\) row.  It is not a theorem about the pairwise large-wrap collar cut out after squaring.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq \sqrt M,
 \qquad Q=2\sqrt{ND/E}.
\]

Use the accepted Round-149 compressed row after the Round-148 physical product and cone collars have retained their separate owners.  Thus \(d\asymp D\), all supported \(L,q\) are positive odd integers, \((L,q)=1\), \(q\asymp LQ\), and

\[
 \mathscr W_{d,U,L}(q)
 :=\mathscr A_{D,E,U}\!\left(d,{4NdL^2\over q^2}\right).
\]

Define the complete one-variable reciprocal sum

\[
 S_{d,L}:=
 \sum_{\substack{q>0\;\mathrm{odd}\\(q,L)=1}}
 \chi _4(q)\mathscr W_{d,U,L}(q)
 e\!\left({NdL\over q}\right),
\]

where the compact support of \(\mathscr W\) imposes \(q\asymp LQ\), and define the exact low-\(L\) linear row

\[
 G_{\leq L_0}(d):=
 \sum_{L\leq L_0}{\chi _4(L)B_{d,U}(L)\over L}S_{d,L}.
\]

The hypotheses used are exactly:

1. the accepted actual Round-148 amplitude and its transition-derivative ledger after the separately owned short physical collars;
2. the finite progression support, which gives \(L\leq \ell\leq e_+\ll E\);
3. the accepted prefix-uniform norm
   \(\sum_L|B_{d,U}(L)|/\sqrt L\ll_\varepsilon X^\varepsilon\);
4. the Tao--Trudgian--Yang exponent pair
   \((\kappa,\lambda)=(89/1282,997/1282)\) for reciprocal model phases; and
5. \(1\leq L_0\), with the sum automatically truncated at the actual finite \(L\)-support.

No regularity in \(L\), no smoothing of \(B_{d,U}(L)\), and no row cancellation are assumed.

## 3. Proof and seam derivation

### 3.1 Uniform variation of the actual profile

Put \(q=LQy\).  The factor \(L\) cancels exactly from the sampled physical coordinate:

\[
 {4NdL^2\over q^2}
 ={4Nd\over Q^2y^2}
 ={dE\over D}y^{-2},
 \qquad Q^2={4ND\over E}.
\]

The supported \(y\)-range is a fixed compact subinterval of \((0,\infty)\).  Bulk dyadic and fixed smooth factors therefore have bounded variation.  The Round-148 ledger gives derivative scale \(M^{1/2}\) on a radial/prefix transition occupying an \(O(M^{-1/2})\) fraction of the normalized \(q\)-range, and derivative scale \(D^{1/2}\) on a cone transition occupying an \(O(D^{-1/2})\) fraction when that transition is present.  Each contributes \(O(1)\) to total variation.  There are only finitely many such factors and endpoint buffers, so zero extension outside the support adds only bounded endpoint jumps.  Hence

\[
 \sup_q|\mathscr W_{d,U,L}(q)|+
 \operatorname{Var}_q(\mathscr W_{d,U,L})
 \ll_\varepsilon X^\varepsilon
\]

uniformly in \(d,L,U,M\).  Sampling this function on any increasing arithmetic progression cannot increase its variation.  A prefix shorter than its peeled radial collar is not being re-estimated here; it remains with the accepted primal collar owner.  This argument uses the quantitative actual-profile ledger and would be false for the arbitrary smooth interpolation countermodel rejected in Round 150.

### 3.2 Coprimality, character, proper intervals, and the TTY parameter

Because \(L\) and \(q\) are odd,

\[
 {\bf1}_{(L,q)=1}
 =\sum_{a\mid(L,q)}\mu(a),\qquad
 \chi _4(am)=\chi _4(a)\chi _4(m).
\]

Thus

\[
 S_{d,L}=
 \sum_{a\mid L}\mu(a)\chi _4(a)
 \sum_{m\ \mathrm{odd}}
 \chi _4(m)\mathscr W_{d,U,L}(am)
 e\!\left({NdL\over am}\right).
\]

Split the inner sum into \(m\equiv1,3\pmod4\), on which the character is constant, and into \(O(1)\) proper dyadic intervals.  On any such interval the running variable has scale

\[
 H_a\asymp {LQ\over a},
\]

and the reciprocal phase has the form \(T_aF(n/H_a)\), up to the harmless fixed affine residue shift, with

\[
 T_a\asymp {NdL/a\over H_a}\asymp {Nd\over Q},
 \qquad
 {T_a\over H_a}\asymp {aNd\over LQ^2}\asymp {aE\over L}.
\]

The intervals are legitimate source intervals \(I\subset[H_a,2H_a]\) after a fixed-number partition.  Also \(a\leq L\) and \(Q\gg R\), so nonempty intervals have \(H_a\gg1\); bounded exceptional intervals are covered trivially.

For \(T_a\geq H_a\), the TTY pair and weighted partial summation give

\[
 \left|\sum_{m\ \mathrm{in\ one\ class}}\cdots\right|
 \ll_\varepsilon
 \left({T_a\over H_a}\right)^\kappa
 H_a^\lambda X^\varepsilon
 \ll_\varepsilon
 E^\kappa Q^\lambda L^{\lambda-\kappa}
 a^{\kappa-\lambda}X^\varepsilon.
\]

There is a small convention seam at the top of the finite \(L\)-support: the accepted support gives only \(L\ll E\), so \(T_a/H_a\) can be a fixed constant below one.  This does not license a literal invocation of the source theorem with \(T_a<H_a\).  In that fixed transition range, however,

\[
 |f''(n)|\asymp {T_a\over H_a^2}\asymp H_a^{-1},
\]

and the elementary second-derivative estimate is \(O(H_a^{1/2})\).  Since \(\lambda=997/1282>1/2\) and \(E/L\gg1\) up to a fixed support constant, this is bounded by the same displayed right side.  Thus the claimed global estimate is valid, but a final proof should retain this one-line \(T<N\) patch rather than state that TTY itself applies there.

Finally \(\kappa-\lambda=-908/1282<0\), so

\[
 \sum_{a\mid L}a^{\kappa-\lambda}
 \leq \tau(L)\ll_\varepsilon X^\varepsilon.
\]

The BV bound from Section 3.1 makes Abel transfer uniform on every divisor progression.  Consequently

\[
 |S_{d,L}|
 \ll_\varepsilon E^\kappa Q^\lambda
 L^{\lambda-\kappa}X^\varepsilon
 =E^{89/1282}Q^{997/1282}L^{908/1282}X^\varepsilon.
\]

The positive reciprocal sign differs from the source-card normalization only by complex conjugation.  The exact factor \(2\) in \(Q\), \(d/D\asymp1\), the two character classes, and fixed interval partitions affect only the implied constant.

### 3.3 Summation over the exact compressed coefficient

Using \(\lambda-\kappa-1=-374/1282\) and

\[
 -{374\over1282}=-{1\over2}+{267\over1282},
\]

the accepted half-weight norm gives

\[
\begin{aligned}
 |G_{\leq L_0}(d)|
 &\leq E^\kappa Q^\lambda X^\varepsilon
 \sum_{L\leq L_0}|B_{d,U}(L)|L^{\lambda-\kappa-1}\\
 &\leq E^\kappa Q^\lambda L_0^{267/1282}X^\varepsilon
 \sum_L{|B_{d,U}(L)|\over\sqrt L}\\
 &\ll_\varepsilon
 E^{89/1282}Q^{997/1282}L_0^{267/1282}X^\varepsilon.
\end{aligned}
\]

The exact clipped prefix remains inside \(B_{d,U}(L)\); no prefix regularity is inserted at this step.

### 3.4 Energy bookkeeping

Since \(E\asymp M/D\), \(Q\asymp R^2D/\sqrt M\), and \(d\asymp D\),

\[
 {E^{2\kappa}Q^{2\lambda}L_0^{534/1282}\over R^2}
 \asymp
 \left(
 {R^{1424}D^{1816}L_0^{534}\over M^{819}}
 \right)^{1/1282}.
\]

Therefore the displayed corridor condition makes the pointwise bound \(O(RX^\varepsilon)\).  Summing over \(O(D)\) rows, with the harmless accepted factor \(D/d\asymp1\), gives

\[
 \sum_{d\asymp D}\mu^2(d)|G_{\leq L_0}(d)|^2
 \ll_\varepsilon R^2D X^\varepsilon.
\]

All exponents in the candidate are therefore arithmetically consistent.

## 4. First doubtful or unproved step

The first doubtful seam was the literal source hypothesis \(T\geq N\) for \(L\) at the fixed upper edge \(L\ll E\).  A bare statement that TTY applies globally would be incomplete there.  Section 3.2 closes that seam with the second-derivative bound in the only range where \(T_a/H_a<1\); the desired TTY-shaped majorant is weaker than \(H_a^{1/2}\) there.  Hence this is not a failed mathematical step.

There is no failed step in the exact low-\(L\) component.  The first genuinely unproved continuation is either:

- a target estimate for the complementary full row \(L>L_0\); or
- a theorem for the isolated large-wrap collar after the two-row energy has been expanded.

The present one-variable estimate supplies neither.  In particular, the pair-dependent collar and wrap indicators cannot be inserted into \(S_{d,L}\) while retaining the proved one-variable BV/TTY argument.

## 5. Required controls and outcomes

1. **Normalization and constants — GREEN.**  The exact relation \(Q^2=4ND/E\) produces the claimed \(E/L\) phase ratio.  The positive phase is covered by conjugation; fixed factors from modulus four and the definition of \(Q\) do not change powers.
2. **Actual-profile BV — GREEN.**  Bulk, radial/prefix, and cone variations are respectively \(O(1)\), \(M^{1/2}M^{-1/2}\), and \(D^{1/2}D^{-1/2}\).  This uses the accepted Round-148 profile only.
3. **Half-open prefix seam — GREEN.**  The exact prefix remains in \(B_{d,U}(L)\); the smooth sampled profile is used only after the accepted physical collar removal.  Collar-short prefixes keep their prior owner.
4. **Proper intervals — GREEN.**  Each divisor/residue progression is split into \(O(1)\) intervals contained in a dyadic scale \([H_a,2H_a]\), with uniform sampled variation.
5. **Source condition \(T\geq N\) — GREEN with explicit patch.**  TTY is used only when \(T_a\geq H_a\); the fixed comparable range below it is covered by the stronger second-derivative estimate.
6. **Coprimality and \(\chi _4\) — GREEN.**  Divisor inclusion costs \(\sum_{a\mid L}a^{-908/1282}\ll X^\varepsilon\), and the character costs two residue classes, not \(O(L)\) classes.  No additive \(\chi _4\) twist or reciprocal B-process is needed.
7. **Exponent ledger — GREEN.**  The successive exponents are \(908=997-89\), \(267=908-641\), and the squared target identity yields exactly \((1424,1816,534;819)\).
8. **Compulsory \(D=1,L=1\) scalar — GREEN in a strict high-\(M\) corridor.**  With \(L_0=1\), the condition is \(M^{819}\geq R^{1424}\).  At \(M=R^2,D=1\), it holds with a power margin.
9. **Nonempty boundary test — GREEN.**  At \(M=R^2,D=1\), the maximal equality-scale choice \(L_0=R^{107/267}\) gives \(R^{1638}=R^{1424}L_0^{534}\).
10. **Row-component scope — GREEN.**  Restricting the exact linear compressed row to \(L\leq L_0\) is legitimate and its full \(q\)-sum is controlled before squaring.  Calling the result an isolated large-wrap-collar estimate would be RED.
11. **Downstream scope — GREEN.**  No claim is obtained for \(L>L_0\), the full growing-\(M\) row, a separately cut collar, the growing-\(M\) generic complement, \(t\geq2\), the cross owner, M9-M1, M9-M2, endpoint assembly, M9, the bridge, or either global exponent.

## 6. Dependencies and exact artifacts used

The review used only:

- `protocol.md`;
- the relevant `state/proof_obligations.yml` entries for the M1/M2 TTY source dependency, the Round-148 reciprocal transform, the Round-149 compressed row and half-weight norm, the Round-150 fixed-wrap range/large-wrap obstruction, and the associated Round-148--150 rejected claims;
- `sources/tao_trudgian_yang_2025.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/candidates/conductor_round150_small_wrap_collar_and_large_wrap_boundary.md`; and
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/barrier_packet.md`.

No numerical experiment or additional source was used.  The control tests above are exact algebraic and analytic checks.

## 7. Recommended state effect

**Promote**, subject to the conductor's remaining round gates, the strict statement that the complete retained compressed-row component \(G_{\leq L_0}(d)\) satisfies the displayed TTY bound and target energy under

\[
 M^{819}\geq R^{1424}D^{1816}L_0^{534}.
\]

Record the proof as a direct low-\(L\) row estimate, with the actual-profile BV lemma and the \(T<N\) second-derivative patch explicit.  Do not label it a proof of the isolated large-wrap collar, and do not infer the full \(t=1\) scalar until the complementary \(L>L_0\) component has an owner.  Retain all downstream obligations listed in Section 5 as open.

Final decision: **GREEN**.
