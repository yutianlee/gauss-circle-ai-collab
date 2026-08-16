# Round 79 conductor divisor-strip check

Status: independent conductor verification of the statement-only
candidate; no graph mutation authorized by this file.

## 1. Per-ray metric incidence

Fix a primitive ray and a block \(k\asymp K\).  From

\[
 |\Lambda-\ell k|\leq {ck\over R}
\]

the integer \(M=\ell k\) lies in an interval of length
\(O_c(K/R)\) about \(\Lambda\).  There are
\(O_c(1+K/R)\) possible integers \(M\).  For each \(M\), every
admissible \(k\) divides \(M\), so the divisor bound gives

\[
 \#\{(k,\ell)\}\ll_\varepsilon X^\varepsilon(1+K/R). \tag{C79.D1}
\]

The open reciprocal interval implies

\[
 {bk^2\over2}<\Lambda<2ak^2,                         \tag{C79.D2}
\]

so \(M\ll AK^2\), which makes the divisor loss
\(X^\varepsilon\).  Empty and singleton intervals are included.
Summing over \(P\) rays proves

\[
 \mathcal I_{\rm ns}\ll_\varepsilon
 X^\varepsilon P(1+K/R).                            \tag{C79.D3}
\]

The calculation is exact and uses metric, not exact, resonance.

## 2. Exact algebraic isolation

Write

\[
 ab=D h^2,\qquad D>1\text{ squarefree},\qquad
 u=(\sqrt b-\sqrt a)^2=a+b-2h\sqrt D.
\]

If \(u_1/u_2\in\mathbb Q\), distinct squarefree fields are excluded by
linear independence.  In one field, comparison of rational and radical
parts gives

\[
 {a_1+b_1\over h_1}={a_2+b_2\over h_2}.
\]

Since \((a+b)/h=\sqrt D(\sqrt{b/a}+\sqrt{a/b})\) and
\(x+x^{-1}\) is strictly increasing for \(x>1\), the ratios \(b/a\)
agree.  Primitive ordered pairs are then identical.  Thus two exact
resonances at one real \(X\) lie on one ray; the remaining modes are
divisors of the common integer \(\Lambda\).

For two metric incidences set \(M_i=2\ell_i k_i\) and
\(E_i=Xu_i-M_i\).  Then

\[
 \eta=M_2u_1-M_1u_2=E_1u_2-E_2u_1,
 \qquad |\eta|\ll {D^2K\over AR}.                   \tag{C79.D4}
\]

If the rays differ, \(\eta\ne0\).  Its other conjugates have size
\(O(A^2K^2)\).  The degree-four norm therefore gives

\[
 |\eta|\gg A^{-6}K^{-6},                            \tag{C79.D5}
\]

and hence

\[
 R\ll A^5D^2K^7.                                    \tag{C79.D6}
\]

Within one squarefree field, the quadratic norm instead gives
\(R\ll AD^2K^3\).  These are correct but much finer than the active
window in general.

## 3. Coefficient ledger and sharpness

On a dyadic block,

\[
 V={JD\sqrt G\over\sqrt A K^{3/2}}.
\]

Multiplying (C79.D3) by \(VR\), and using \(P\ll AD\), yields

\[
 \mathcal A_{\rm ns}(R)
 \ll_\varepsilon X^\varepsilon
 JD^2\sqrt{AG}\left(K^{-1/2}+RK^{-3/2}\right).      \tag{C79.D7}
\]

The separate conductor \(X\)-average shows that the \(PK/R\) term in
(C79.D3) is the ordinary random-density population on a stable inner
cone.  It therefore cannot be removed by an algebraic inverse theorem.
The fine norm thresholds apply only far beyond the usual metric window.

## 4. Decision seam

Equations (C79.D3), (C79.D6), and (C79.D7) are narrow promotable
incidence statements if the analytic and hostile reports agree.  They
do not estimate the signed primitive-ray sum.  A phase-conjugated lift
profile can saturate the Abel scale while obeying the same variation
norm, so incidence plus variation cannot prove the literal signed
energy.

The correct next object is the coefficient-weighted off-diagonal inside
the integer-product fibers \(M=\ell k\), together with whatever
off-fiber kernel survives the exact \(TT^*\) expansion.  No status of
the signed cone, \(M9\!-!M2\), \(M9\), or the exponent should change
from this incidence lemma alone.
