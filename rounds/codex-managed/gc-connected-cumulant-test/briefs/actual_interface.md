# Round234 actual connected-correlation interface

Starting graph SHA256: dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306

Use the literal actual f_d, B_T, Z_Q, E_(p,Q) from accepted233, the same rho, Psi, w, and all harmonics. Freeze p=12 and Q=floor(T^(2/5)); W=integral w>0; probability dnu_T=w(R/T)dR/(TW). For an ordered distinct label tuple d define

 m_S(d)=E_nu product_(j in S) f_(d_j),
 kappa_12(d)=sum_(pi partition[12]) (-1)^(|pi|-1)(|pi|-1)! product_(C in pi) m_C(d),
 K_12=TW sum_d^* kappa_12(d), D_12=I_12-K_12,
 C_conn=TW sum_d^* |kappa_12(d)|.

Proposed mechanism: subtract all lower-order disconnected correlations before estimating the connected aggregate. The exploratory target is K_12<=T^(29/25+epsilon) with D_12 paid at that budget. A hoped-for connected-cluster absolute estimate C_conn<=T^(29/25+epsilon) is a stronger candidate to falsify, NOT a granted hypothesis. Merely rewriting I as K+D is not an estimate.

Concrete tests to attempt: (i) exploit distinct square-root frequencies to show total first- and second-order cross-class means decay faster than every power with smooth radius averaging; (ii) bound the SIGNED sum of each remaining proper partition via independent radius variables, exact collision inclusion-exclusion, uniform square-sums, and accepted actual moments through order9; (iii) test whether cumulant subtraction can materially reduce the known full-harmonic tuple-absolute mass >=c T^(5/2). Keep the original signed target distinct from either certificate.

For the absolute test, a possible coarse block bound to prove or reject is A_q=sum_(distinct labels>Q)|m_[q]| <=T^(max(q/4-1,0)+epsilon), q>=3 fixed; smoothness plus the full Schwartz coefficient tail may give rapid A_1,A_2. If true, each disconnected12 partition is below T^(5/2) after the outer TW. Do NOT assume these bounds or that a coefficient-norm barrier transfers to actual cumulants without proof.

The full-harmonic lower certificate is reviewed admission evidence in strategy/round231_harmonic_admission, not an accepted graph theorem. Re-audit any exact proof used, including squarefree mass, mixed harmonics, and the infinite tail. Complete target restoration may use accepted216: head15/13 and repeated-class error8beta-1/5; target29/25 gives102/325, not quarter. The all-fixed-order233 bridge remains accepted, but no unbounded-order cumulant estimate is supplied by this p12 exercise. Upper-tail A's two-attempt reassessment remains in force; this is a different aggregate mechanism, not a third local packet cutoff.

Budget: 95% analytical/algebraic, at most5% exact diagnostic computation; three initial tasks about10 minutes and one bounded nonauthor review/repair cycle. No next round. Report seven protocol sections, precise limitations and hashes. No graph/draft/shared-state edits.
