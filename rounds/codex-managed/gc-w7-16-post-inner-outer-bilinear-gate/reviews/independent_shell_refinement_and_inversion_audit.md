# Round 130 independent seam review: shell refinement and exact inversion

## 1. Result

The shell refinement

\[
\#\{a'\}\ll 1+{LB\over D}\ll {LB\over D},
\qquad
|\mathfrak O_{i,B}^{+}|\ll_\varepsilon BK_BY^\varepsilon
\]

is **rigorous with one ordering qualification**: the reduced-numerator support may be imposed on the exact coefficient only after the Stieltjes thresholds have recombined. It is not a support statement for each separate threshold atom. The report applies the \(a'\)-triangle after the Round-129 recombined branch theorem, so its actual derivation (130.37)--(130.39) is in the lawful order.

The displayed shell and capacity exponents are correct. In particular,

\[
K_B=Y^{11/48+o(1)},\quad
(D/L)K_{D/L}=Y^{27/48+o(1)},\quad
DK_D=Y^{35/48+o(1)},
\]

and the other stated returns \(Y^{37/48}\), \(Y^{40/48}\), and \(Y^{43/48}\) have the correct arithmetic.

The Stieltjes--Möbius--complete-lift inversion is algebraically exact. The M1 character returns \(\chi_4(d')\). In M2 the **full displayed sector factor** returns

\[
\epsilon_{\rm sgn}\chi_4(g)\chi_4(|a'|)
=\epsilon_{\rm sgn}\chi_4(|h'|),
\]

not a bare \(\chi_4(|h'|)\) unless \(\epsilon_{\rm sgn}\) is explicitly declared absorbed into the fixed original sign-sector coefficient. The report retains this sign in (130.17), but its prose and control table should not appear to delete it.

One substantive scope correction is needed: (130.33) follows directly from the accepted original-variable theorem only after all half-open \(B\)-owners have been summed back to the complete fixed block. It is not automatically a bound for the isolated \(B\asymp D\) owner. Such a top-owner version would require rerunning the product-window proof with the reduced-denominator/gcd owner retained.

The \(p\)-first and unit-Hessian conclusions are valid method controls in their stated positive-norm scopes. They are not lower bounds and do not exclude a new signed top-shell correlation estimate.

## 2. Exact shell-support statement and hypotheses

Before Stieltjes expansion, the exact inner complete-lift coefficient at reduced ray \((a',b')\) contains only lifts \(g\) for which the two physical profiles overlap:

\[
g|a'|\asymp L,
\qquad
gb'\asymp D.
\tag{A1}
\]

On the half-open reduced-denominator shell \(b'\asymp B\), (A1) implies

\[
g\asymp {D\over B},
\qquad
|a'|\asymp {L\over g}\asymp {LB\over D}.
\tag{A2}
\]

For each fixed outer ray \(r=(a,b)\), the map \(p\mapsto a'=a+p\) is injective. The signed support in (A2) is contained in two integer intervals of total cardinality

\[
O\!\left(1+{LB\over D}\right).
\]

The hypotheses \(D/L\le B\le D\) give \(LB/D\ge1\), so this is \(O(LB/D)\). Frequency signs contribute only the two intervals; fixed profiles, sampled exits, sign sectors, determinant gates, cells, and shell intersections only delete points or split the support into \(O(1)\) pieces. The estimate is therefore uniform in those data and in the outer ray.

The necessary qualification is that the discrete Stieltjes expansion

\[
\omega_{i,D}^*(gb';c)=\sum_{t\ge gb'}^*c_{i,t}
\tag{A3}
\]

can have nonzero individual threshold atoms even when the cumulative left side vanishes outside its physical support. Thus (A2) must not be asserted threshold by threshold after replacing (A3) by absolute Stieltjes mass. It becomes exact again for the fully recombined \(S_{i,r,a',\rho,\eta}^{(B)}\). This is precisely the object bounded in (130.37), so the report's final counting order is valid even though the phrase “a nonzero term” in section 3.3 should read “a nonzero exact recombined complete-lift coefficient.”

Half-open ownership is also essential: each physical reduced denominator \(b'\) has one \(B\)-owner. A bounded number of clipped faces changes constants only and does not restore an \(O(L)\) numerator count.

## 3. Derivation of the \(BK_B\) bound and exponent audit

The accepted outer facts give, without using the pointwise bound,

\[
\sum_r|A_i(r)|
\le \#\mathscr R^{1/2}\left(\sum_r|A_i(r)|^2\right)^{1/2}
\ll (LD)^{1/2}(D/L)^{1/2}=D.
\tag{A4}
\]

For each fixed \((r,a')\), Round 129 proves after threshold recombination and only then after summing the Möbius divisors and M1/M2 branches that

\[
\sum_{\rho\mid a'}\sum_{\eta\in\mathcal E_i}
|S_{i,r,a',\rho,\eta}^{(B)}|
\ll_\varepsilon {K_B\over L}Y^\varepsilon.
\tag{A5}
\]

The report writes an absolute value outside the branch sum in (130.37), which is weaker than the accepted sum-of-absolute-values form (A5) and is therefore legitimate. No extra divisor or branch factor may be appended afterward.

Combining (A2), (A4), and (A5) gives exactly

\[
|\mathfrak O_{i,B}^{+}|
\ll_\varepsilon
D\,{LB\over D}\,{K_B\over L}Y^\varepsilon
=BK_BY^\varepsilon.
\tag{A6}
\]

There is no missing \(L\), sign, shell, or outer-ray factor. Logarithmically many half-open shells are absorbed by \(Y^\varepsilon\).

For \(B=Y^b\), \(16/48\le b\le24/48\),

\[
Q_B={BD\over WL}=Y^{b-5/48},
\quad
\lambda_B={YL\over DB^2}=Y^{32/48-2b},
\]

so

\[
Q_B\sqrt{\lambda_B}=Y^{11/48},
\qquad
\lambda_B^{-1/2}=Y^{b-16/48}\le Y^{8/48}.
\]

Also \(Q_B\ge Y^{11/48}\), with equality at the smallest shell. Hence the minimum defining \(K_B\) is \(Y^{11/48+o(1)}\) throughout the allowed range. All exponents in (130.33), (130.41), (130.46), (130.51), and (130.52) check:

\[
{D^2\over L^2}=Y^{32/48},\quad
{WD\over L}=Y^{37/48},\quad
{D^2\over L}=Y^{40/48},\quad
Q_*={D^2\over WL}=Y^{19/48},\quad
DQ_*=Y^{43/48}.
\]

No exponent error was found in the audited claims.

## 4. Exact inversion and character audit

After setting \(a'=\rho u\), \(b'=\rho v\), a complete lift \(g\) gives

\[
h'=ga'=g\rho u,
\qquad
d'=gb'=g\rho v.
\tag{A7}
\]

The Stieltjes identity is exact with the prescribed star:

\[
\sum_t c_{i,t}\mathbf1_{d'\le t}^{*}
=\omega_{i,D}^{*}(d';c).
\tag{A8}
\]

The Möbius sum restores

\[
\sum_{\rho\mid a',\,\rho\mid b'}\mu(\rho)
=\mathbf1_{(a',b')=1}.
\tag{A9}
\]

Once (A9) has removed nonprimitive reduced pairs, every original pair has the unique factorization

\[
g=(|h'|,d'),\qquad a'=h'/g,\qquad b'=d'/g.
\tag{A10}
\]

The phase becomes the conjugated original inner phase

\[
e\!\left(-{ca'\over\kappa_i b'}\right)
=e\!\left(-{ch'\over\kappa_i d'}\right).
\]

For M1, the two constants and carrier phases in (130.17) reconstruct

\[
{e(b'/4)-e(-b'/4)\over2i}=\chi_4(b'),
\]

and complete multiplicativity, including zero even samples, gives

\[
\chi_4(g)\chi_4(b')=\chi_4(d').
\tag{A11}
\]

For M2,

\[
\chi_4(g)\chi_4(|a'|)=\chi_4(|h'|).
\tag{A12}
\]

Equation (A12) is correct, but the full coefficient in (130.17) also contains \(\epsilon_{\rm sgn}\). Exact inversion therefore retains \(\epsilon_{\rm sgn}\chi_4(|h'|)\) as the fixed sector factor. If the intended original one-oriented sector already includes that sign, the report should say so at (130.29)--(130.32) and in the `actual_character_placement` control. It must not be described as having disappeared.

Summing all half-open \(B\)-owners after (A8)--(A10) returns the complete original block exactly once. This validates inversion as an identity. It also locates the scope issue in (130.33): the cited original-variable product-window theorem is a complete-fixed-block theorem. Its \(Y^{37/48}\) estimate follows immediately after the all-owner sum, but not for one isolated top owner merely because the complete signed block obeys that estimate. A top-owner version needs an owner-compatible rerun of the product-window proof.

## 5. First doubtful steps and no-go scopes

1. **Full inversion.** Exact inversion is reversible and supplies no estimate. “Return to \(Y^{37/48}\)” means inversion followed by the already accepted complete-block product-window theorem. It is a no-go only for that known continuation, not for every analysis in \((h',d')\).

2. **Top-shell \(p\)-first route.** At \(B\asymp D\), the physical complete lift \(g\) is bounded, the \(p\)-window has length \(O(1+D/W)\), and the accepted real-centre product-window count gives \(D/L\) for one outer ray and \(D^2/L\) after (A4). This is a rigorous upper bound for the route that takes the reciprocal/outer modulus at the stated point. It is not a lower bound and does not exclude a signed joint \(p,b'\), or outer-ray estimate.

3. **Sequential transform.** The differentiated formulas are correct:

\[
\det\nabla^2_{p,q}f_i=-{c^2\over\kappa_i^2(b+q)^4},
\]

and after \(b'=\rho v\),

\[
\det\nabla^2_{p,v}f_i=-{c^2\over\kappa_i^2\rho^2v^4}
=-{c^2\rho^2\over\kappa_i^2b'^4}.
\]

The first determinant is unit order on the whole pre-Möbius top shell. The second is unit order as stated only on the \(\rho=1\) progression; for \(\rho>1\) it has size \(\rho^2\) and the progression spacing and dual range must be rescaled together. The \(DQ_*\) conclusion is a scoped capacity return after aliaswise absolute values, not a literal-family lower bound. Linear M1/M2 quarter shifts translate aliases and do not alter either Hessian.

4. **Remaining open route.** None of these controls rebuts an actual signed threshold/alias correlation. The report's final open scalar (130.54) is correctly scoped.

## 6. Formula integrity, dependencies, and control-character check

The audited report and the exact comparison artifacts were:

- `rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reports/actual_numerator_increment_recombination_attack.md`
- `rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/reports/actual_stieltjes_reciprocal_sum_attack.md`
- `rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/reviews/conductor_round129_direct_curvature_adjudication.md`
- `rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/synthesis.md`
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reports/actual_character_determinant_attack.md`
- `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/graded_determinant_long_lift_feasibility.md`
- `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reports/actual_rational_cluster_attack.md`

A code-point scan found no embedded ASCII carriage return or other control byte in place of `\\rho`; the stored `\\rho` tokens are intact. There are, however, several source-level TeX corruptions where a leading backslash is missing:

- current source lines 62, 146, 183, 404, and 453 contain `qquad` instead of `\\qquad`;
- current source line 337 contains `lfloor` instead of `\\lfloor`;
- several prose occurrences such as `(chi_4(...))` are outside math delimiters and should be normalized;
- in (130.35), write `g\\,|a+p|` to distinguish multiplication by an absolute value from divisibility.

These are rendering/formula-token defects, not exponent errors. They should be corrected before promotion because (130.13), (130.32), and (130.35) currently render as malformed displayed formulas.

## 7. Recommended state effect

**Promote after textual repair** the support lemma and shell bound (130.3), (130.5), and (130.37)--(130.41), with the explicit rule that \(\#a'\ll LB/D\) applies to the exact Stieltjes-recombined coefficient, not to each threshold atom.

**Promote with a sign clarification** the inversion (130.28)--(130.32): M1 returns \(\chi_4(d')\), while M2 retains the fixed \(\epsilon_{\rm sgn}\chi_4(|h'|)\) sector factor. Summing all \(B\)-owners returns the complete original block.

**Revise the scope** of (130.33) to “complete all-owner inversion followed by the accepted original-variable theorem.” Do not cite it as an isolated top-shell bound without an owner-compatible proof.

**Record only as scoped method controls** the \(p\)-first \(D^2/L\) return and the aliaswise-transform \(DQ_*\) return. They exclude those positive-norm continuations, not a new signed scalar estimate. No shared proof state, exponent, M9 component, or downstream theorem should be changed by this review alone.
