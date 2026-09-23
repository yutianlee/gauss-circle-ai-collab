# Round 164 statement-only residual problem

Let \(J=\sqrt X\), \(y=\lfloor J\rfloor\),
\(q_X=X/y^2\), \(H=\lfloor yX^{-1/4}\rfloor\), and
\(1\ll L\ll H\leq J^{1/2}\).  Consider

\[
 \mathcal S_{L,1}
 =\sum_{N\asymp L^2}\mu^2(N)
 \left(\frac{L^2}{N}\right)^{3/4}e(J\sqrt N)b_{L,X}(N),
\]

where

\[
 b_{L,X}(N)
 =\sum_{\substack{d\mid N,\ d\ {\rm odd}\\
 \sqrt N\leq d\leq2\sqrt N}}
 \chi_4(d)\eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}d}{2\sqrt N}\right).
\]

All product shells and divisor windows are half-open as inherited.  The
amplitude is zero-extended outside the literal cone, dyadic support,
profiles, floors, stars, and endpoint rules.  The product \(N\) is
squarefree.  The character-bearing divisor \(d\) is odd; \(N\) may be
even through its complementary factor.

Fix \(\kappa>0\).  For every supported \(N\), a deterministic rule using
only \((N,L,\kappa)\) selects at most one pair of distinct odd prime
divisors \(\{p_N,q_N\}\) satisfying

\[
 \chi_4(p_Nq_N)=-1,\qquad
 |\log(q_N/p_N)|\leq\kappa L^{-1/2}.
\]

The already removed sector consists exactly of physical incidences where
one selected prime divides \(d\).  Define the residual indicator by

\[
 \rho_N(d)=
 \begin{cases}
 1,&\text{no pair is selected},\\
 1,&p_N,q_N\mid d,\\
 1,&p_N,q_N\nmid d,\\
 0,&\text{otherwise}.
 \end{cases}
\]

The statement-only task is to prove

\[
 \left|
 \sum_{N\asymp L^2}\mu^2(N)
 \left(\frac{L^2}{N}\right)^{3/4}e(J\sqrt N)
 \sum_{\substack{d\mid N,\ d\ {\rm odd}}}
 \chi_4(d)\rho_N(d)A_N(d)
 \right|
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\]

or to derive the first exact obstruction to doing so by within-product
signed transport.

Required work:

1. define the residual divisor universe without double subtraction;
2. derive the exact ordered-divisor Abel or Stieltjes identity;
3. separate equal sign mass, unmatched mass, and hard amplitude jumps;
4. derive the monotone-transport cost with its exact normalization;
5. restore all \(L,H,J,X\) powers;
6. retain the outer phase unless within-\(N\) control is already at
   target;
7. distinguish raw semiprime or multiprime counts from the literal
   physical scalar; and
8. state the exact first unproved cross-\(N\) theorem if the transport
   route fails.

No conclusion may be transferred to other few-point channels or any
downstream owner.
