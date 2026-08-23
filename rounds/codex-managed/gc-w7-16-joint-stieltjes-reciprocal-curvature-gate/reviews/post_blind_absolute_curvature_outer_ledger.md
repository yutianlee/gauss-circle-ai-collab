# Post-blind seam addendum: absolute threshold curvature and outer ledger

## Verdict

The direct **absolute** theorem survives:

\[
 \boxed{\left|\sum_{v\in I}^{*}
 U_{i,\rho,\eta}(v)e(f_{i,\rho,\eta}(v))\right|
 \ll_\varepsilon {K_\rho\over L}Y^\varepsilon,}
 \qquad
 K_\rho=\min\!\left(
 N_\rho,\,
 N_\rho\sqrt{\lambda_B\rho^2}
+(\lambda_B\rho^2)^{-1/2}\right).
 \tag{A.1}
\]

It is strictly different from, and does not imply, the false
norm-relative theorem.  The threshold-first proof in (129.H18)--(129.H22)
is valid for the literal packages (128.10)--(128.20).  It is stronger
than the conductor candidate's \(J_B^{1/2}K_\rho/L\): the factor
\(J_B^{1/2}\) is unnecessary once one estimates constant threshold
plateaux before Stieltjes superposition.

Using the complete outer ledger in Round 127, Section 3.3, (A.1) gives
the complete all-\(B\) fixed-block estimate

\[
 \boxed{|\mathfrak O_i(c)|\ll_\varepsilon
 Y^{35/48+\varepsilon}.}
 \tag{A.2}
\]

This conclusion is candidate seam evidence only.  It does not restore
the false \(V^2\)-relative claim and gives no global, M9, or quarter
promotion.

## Verification of the direct theorem

For one exact literal branch, (128.15)--(128.20) give

\[
 U(v)=\sigma_{i,\rho,\eta}\,T_i(v)
 \sum_k c_k P_i(M_k(v)),\qquad
 M_k(v)=\left\lfloor {k\over\rho v}\right\rfloor ,
 \tag{A.3}
\]

where

\[
 |\sigma_{i,\rho,\eta}|\ll1,\qquad
 \sum_k|c_k|\ll1,\qquad
 \sup_m|P_i(m)|\ll_\varepsilon L^{-1}Y^\varepsilon.
 \tag{A.4}
\]

The last bound is character Abel summation before any liftwise modulus.
It uses the complete common factor \(\chi_4(g)\) in (128.10).  All fixed
frequency restrictions remain inside \(P_i\); all moving denominator
faces, including their actual hard/star values, are exactly in the
Stieltjes coefficients \(c_k\).  The remaining multiplier \(T_i\) has
bounded sampled supremum plus variation on \(O(1)\) clipped intervals.

Fix \(k\asymp D\).  The monotone integer function \(M_k(v)\) has

\[
 R_k\ll 1+{DQ_B\over B^2}
 \tag{A.5}
\]

maximal constant plateaux on a physical \(b'\)-window of length at most
\(Q_B\).  A strict/weak or starred equality is \(k=\rho vg\); for fixed
\((k,\rho)\) these give divisor-many singleton pieces.  Their total cost
is \(Y^\varepsilon\) and does not change (A.5) at power scale.

Put

\[
 \mu_\rho=\lambda_B\rho^2,\qquad
 N_\rho\asymp {Q_B\over\rho}.
\]

On a plateau \(J\), \(P_i(M_k(v))\) is constant.  Weighted
second-derivative summation, including every integer derivative alias
and either M1 quarter shift, gives

\[
 \left|\sum_{v\in J}^{*}T_i(v)e(f(v))\right|
 \ll
 \bigl(\|T_i\|_{\infty,J}+\operatorname{Var}_J T_i\bigr)
 \min\bigl(|J|,|J|\sqrt{\mu_\rho}+\mu_\rho^{-1/2}\bigr).
 \tag{A.6}
\]

Summing the trivial alternatives over all plateaux costs \(O(N_\rho)\).
For the curvature alternatives, disjointness and global bounded
variation give

\[
 O\!\left(
 N_\rho\sqrt{\mu_\rho}
+(R_k+1)\mu_\rho^{-1/2}\right).
 \tag{A.7}
\]

This explicitly prices the artificial endpoint values created by
cutting \(T_i\) into plateaux: interior variations sum to
\(\operatorname{Var}_I T_i=O(1)\), while the plateau endpoint suprema
produce exactly the \(R_k\mu_\rho^{-1/2}\) term.

The nonconstant part of (A.5) is absorbed without a \(J_B\)-loss:

\[
 {DQ_B\over B^2}\mu_\rho^{-1/2}
 ={DQ_B\over B^2\rho\sqrt{\lambda_B}}
 ={Q_B\sqrt{\lambda_B}\over\rho L}
 \le Q_B\sqrt{\lambda_B}
 =N_\rho\sqrt{\mu_\rho}.
 \tag{A.8}
\]

Here \(D^2=Y\) and
\(\lambda_B=YL/(DB^2)\).  The constant part of \(R_k+1\) is the single
allowed \(\mu_\rho^{-1/2}\) endpoint term.  Multiplying by (A.4), taking
the better of the trivial and curvature estimates, and finally summing
\(\sum_k|c_k|\ll1\) proves (A.1).

This order of operations is essential.  The conductor birth-block/Abel
argument controls variation in the lift variable and retains
\(J_B^{1/2}\).  The threshold-first argument needs only the uniform
character partial-sum bound (A.4); the exact plateau endpoint ledger
(A.8) then removes \(J_B\) completely.  It never replaces
\(L^{-1}\sum|c_k|\) by the smaller \(V^2\) norm, so the post-blind
counterexample is irrelevant to (A.1).

## \(\rho\)-sum and all-\(B\) capacity

Let

\[
 K_1=\min\!\left(
 Q_B,\,
 Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\right).
\]

For every \(\rho\mid a'\),

\[
 N_\rho={Q_B\over\rho},\quad
 N_\rho\sqrt{\mu_\rho}=Q_B\sqrt{\lambda_B},\quad
 \mu_\rho^{-1/2}={\lambda_B^{-1/2}\over\rho},
\]

and hence \(K_\rho\le K_1\).  Therefore

\[
 \sum_{\rho\mid a'}|\mu(\rho)|\,K_\rho
 \ll_\varepsilon K_1Y^\varepsilon.
 \tag{A.9}
\]

There is no hidden positive power from the Möbius progressions.

Write \(B=Y^b\), \(1/3\le b\le1/2\).  At the fixed critical block,

\[
 Q_B=Y^{b-5/48},\qquad
 \lambda_B=Y^{2/3-2b},
\]

so

\[
 Q_B\sqrt{\lambda_B}=Y^{11/48},\qquad
 \lambda_B^{-1/2}=Y^{b-1/3}\le Y^{8/48}.
 \tag{A.10}
\]

At \(b=1/3\), the trivial branch \(Q_B\) is also \(Y^{11/48}\);
for larger \(b\) it is longer.  Thus

\[
 K_1\ll Y^{11/48}
 \tag{A.11}
\]

uniformly over every allowed shell.

The complete Round-127 outer ledger has \(O(LD)\) outer rays, \(O(L)\)
reduced-numerator increments, and one outer coefficient
\(O_\varepsilon(L^{-1}Y^\varepsilon)\).  The all-\(\rho\) inner cost
from (A.1) and (A.9) is \(O_\varepsilon(K_1L^{-1}Y^\varepsilon)\).
Consequently

\[
 (LD)\cdot L\cdot L^{-1}\cdot {K_1\over L}
 =D K_1
 \ll Y^{24/48+11/48}=Y^{35/48}.
 \tag{A.12}
\]

The owner count is complete:

- (128.10) is already the fully aggregated lift dictionary, so no lift
  multiplicity remains outside either coefficient;
- the denominator profile, floors, hard/star samples, and its support
  exits are owned once by (128.18)--(128.20);
- determinant taper, cell and sign faces, and strict/weak values are
  owned once by \(T_i\);
- one \(Q_B\)-window meets only \(O(1)\) adjacent half-open \(B\)-shell
  owners, and the dyadic shell sum costs only \(Y^\varepsilon\);
- M1's two quarter phases, M2's fixed sign, both orientations, and the
  already smaller diagonal add only absolute constants;
- the outer ray is not recounted inside the Stieltjes or \(\rho\) sums.

Thus no \(G\), \(J_B\), \(\rho\), cross-shell, or endpoint factor is
missing from (A.12).

## Seam outcomes and recommendation

| Seam | Outcome |
|---|---|
| threshold stars/equalities | Pass: exact Stieltjes values are retained; exceptional equalities are divisor-many singletons and cost \(Y^\varepsilon\). |
| \(T_i\) BV on plateaux | Pass: interior variation sums globally; artificial plateau endpoints are exactly the term absorbed in (A.8). |
| \(J_B\) absorption | Pass exactly by (A.8); no \(J_B^{1/2}\) remains. |
| \(\rho\)-sums | Pass by (A.9); \(K_\rho\le K_1\). |
| outer owners | Pass using the complete Round-127 ledger and the no-unidentified-support statement after (128.10). |
| false norm-relative theorem | Still rejected; it is neither used nor implied. |

Recommended state effect: **promote only after conductor adjudication**
the direct absolute theorem (A.1) and its complete fixed-block consequence
(A.2).  Revise the conductor candidate by deleting the unnecessary
\(J_B^{1/2}\) loss and replacing its norm-relative motivation by the
threshold-first proof above.  Make no shared-state edit from this
addendum.

## Exact artifacts used

- Round-129 hostile report, equations (129.H18)--(129.H22);
- Round-129 conductor candidate
  conductor_birth_block_abel_curvature.md;
- Round-128 literal report, equations (128.10)--(128.20), with the
  immediately following plateau/BV owner verification;
- Round-127 graded_determinant_long_lift_feasibility.md, Section 3.3.
