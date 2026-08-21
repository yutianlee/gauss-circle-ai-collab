# M1 square-root capacity self-return barrier

## Statement

Let

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B=C/T,
\]

with \(J^{13/18}<C\leq J^{3/4}\) and \(M\asymp B\).  Fix one
transition-flattened smooth nonaxial M1 component, one exact arithmetic
class, one sign, and one reflected orientation.  Write

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_n I_b(n)e_M(nx)e(n\theta)
\]

and, for an ordered pair \(P=(x,y)\) of distinct units, put

\[
 F_{b,P}(\theta)=e_M\!\left(K(\bar x-\bar y)\right)
 \mathcal R_{b,x}(\theta)\overline{\mathcal R_{b,y}(\theta)}.
\]

Let \(\Pi_{b,D}\) be the accepted deep multiplier, including the
actual stationary support and zero extension, and define

\[
 H_{b,D}=\sum_{P:x\ne y}\Pi_{b,D}F_{b,P},\qquad
 \mathcal E_D=\sum_{b\asymp B}\int_{\mathbb T}
 |D_D(\theta)|^2|H_{b,D}(\theta)|^2\,d\theta.
\]

Then the following assertions hold.

1. The Fourier coefficient of \(H_{b,D}\) is exactly

   \[
   \widehat H_{b,D}(d)=\Pi_{b,D}(d){1\over M^2}\sum_n
   \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
   I_b(n+d)\overline{I_b(n)}.
   \]

2. The Gram form has one global \(u=0\) owner and an exact disjoint
   successive-complement decomposition into the Round-87, Round-88,
   Round-89, and hard edge sets.  Here an accepted positive majorant
   for an owned subset is not a second incidence owner.

3. Complete local descent is invertible.  If \(q=p^\nu\),
   \(q'=q/p^j\),

   \[
   \mathfrak T_q(p^ju')=p^{2j}\mathfrak T_{q'}^\downarrow(u'),
   \qquad
   \mathfrak T_q(u)=0\quad(p^j\nmid u),
   \]

   then

   \[
   {1\over q^2}\sum_{u\bmod q}\mathfrak T_q(u)e_q(-ux)
   ={1\over q'^2}\sum_{u'\bmod q'}
   \mathfrak T_{q'}^\downarrow(u')e_{q'}(-u'x).
   \]

   Thus the \(p^{2j}\) trace factor cancels the quotient-square
   normalization, and the restricted Fejer shifts retain their total
   mass.

4. For every length-\(D\) coefficient vector \(a\),

   \[
   \left|\sum_{j=1}^D a_j\right|^2
   \leq {2\over D+1}
   \int_{\mathbb T}|D_D(\theta)|^2
   \left|\sum_{j=1}^Da_je(j\theta)\right|^2d\theta.
   \]

   Consequently

   \[
   \left|\sum_{b\asymp B}H_{b,D}(0)\right|^2
   \ll_\varepsilon X^\varepsilon{B\over D}\mathcal E_D.
   \]

5. Put

   \[
   \mathsf C_{82}=B^3T^2Q^{-5/12},\qquad
   \mathsf T_{82}=J^2/T.
   \]

   For a full-degree Gram graph, \(\Delta\asymp B^2\),

   \[
   \mathsf C_{\rm deep}
   =DB^5T^4Q^{-5/6}={D\over B}\mathsf C_{82}^2,
   \qquad
   \mathsf T_{\rm deep}
   ={D\over B}J^{14/5}={D\over B}\mathsf T_{82}^2.
   \]

   Hence the deep energy gap is exactly the square of the Round-82
   linear gap.  The Fejer/Cauchy passage takes the compulsory square
   root and returns to equal analytic capacity.

## Proof

The unrestricted double unit sum factors as a Kloosterman product.  Its
deleted diagonal \(x=y\) is \(c_M(d)\), proving the first identity.
Expanding \(\mathcal E_D\) gives the complete four-row symbol with
normalization \(M^{-5}\mathfrak T_M=M^{-4}\sum_x\); therefore no
additional \(M^{-2}\) occurs.  The physical edge sets are partitioned
successively by the accepted Round-87, Round-88, and Round-89 labels,
with every later set intersected with earlier complements.  Removing
the constant coefficient of \(|D_D|^2\) leaves exactly \(u\ne0\), so
restoring it once gives the global diagonal.

The local inversion follows from \(q^2=p^{2j}q'^2\).  For the Fejer
inequality, let \(T_D(i,j)=D-|i-j|\) and \(v=e_1+e_D\).  Then
\(T_Dv=(D+1){\bf1}\) and \(v^*T_Dv=2(D+1)\).  Cauchy--Schwarz in the
positive \(T_D\)-inner product gives the displayed bound.  Finally,
four rows contribute \(Q^{-5/6}\), the full graph contributes
\(\Delta=B^2\), and direct algebra gives the two square identities.

## Scope and obstruction

This is a Gram-level and capacity-level self-return theorem, not a
linear involution.  The one-way step is the Fejer/Cauchy inequality.
The exact \(q=8\) residual cell retains full directed degree, so the
accepted local classifications do not yield a strict power gain.  The
first open estimate is the joint signed hard actual-symbol Gram
operator; no claim is made for the rest of M9-M1, M9-M2, M9, R5-Full,
or the Gauss-circle exponent.
