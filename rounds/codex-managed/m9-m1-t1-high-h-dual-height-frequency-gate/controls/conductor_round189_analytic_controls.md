# Conductor analytic controls for Round 189

## 1. Slow projective sector

Put \(J=\lfloor mq/Y\rfloor=\lfloor U/Y\rfloor\). For fixed unit
\(a\bmod q\), the map

\[
 v\longmapsto a\bar v\pmod q
\]

is a bijection of the units.  Hence
\(1\le |a\bar v|_q\le J\) occupies at most \(2J\) residue classes.
The literal \(v\)-support has length \(O(u)\), and \(q\mid u\), so
each class occurs \(O(u/q)\) times.  Therefore

\[
 \#\{v:\text{literal outer predicates},
          1\le |a\bar v|_q\le J\}
 \ll \frac{uJ}{q}\le\frac {um}Y.
\tag{C189.1}
\]

If \(U<Y\), then \(J=0\) and this sector is empty. Coprimality and
literal endpoint predicates only delete values.

At fixed \((\kappa,u,U=mq,a,h)\), every retained \(v\) has
\(O(\kappa)\) live oriented affine sites and every atom is
\(O_\eta(X^\eta)\).  Since \(\kappa u\asymp L\), (C189.1) gives

\[
 \sum_{\omega,v,t}^{\rm slow}|B_{\mathfrak f,\omega}^\sigma(t)|
 \ll_\eta \frac{Lm}{Y}X^\eta.
\tag{C189.2}
\]

Summing the \(O(Y)\) heights and multiplying by the exact
\(m^{-1}c_q(a)\) weight cancels this factor \(m\). Summation over the
unit numerators therefore yields

\[
 \ll_\eta L\log(2q)X^\eta
\]

at fixed \((\kappa,u,m,q)\).  Finally,

\[
 \sum_{mq\mid u}\log(2q)
 \le \log(2u)\sum_{d\mid u}\tau(d)
 = \log(2u)\tau_3(u).
\tag{C189.3}
\]

Elementary dyadic divisor summation in
\(u\asymp L/\kappa\), followed by \(\kappa\), proves the complete
slow sector is

\[
 O_\eta(L^2\log^{O(1)}(2L)X^\eta)
 =O_{B,\varepsilon}(L^2X^\varepsilon).
\tag{C189.4}
\]

No positive power of \(Y\) is absorbed.  It disappears in (C189.1)
before positivity.

The same proof has a fixed-polylogarithmic strengthening. For \(P\ge1\)
put

\[
 J_P=\min\!\left\{\frac{q-1}{2},
                  \left\lfloor\frac{Pmq}{Y}\right\rfloor\right\}.
\tag{C189.4a}
\]

The projective count is
\(O(u\min\{1,Pm/Y\})\). After \(Y\) heights, \(O(\kappa)\) sites,
and the exact \(1/m\) lift weight, its cost is

\[
 L\frac Ym\min\!\left\{1,\frac{Pm}{Y}\right\}\le LP
\tag{C189.4b}
\]

before numerator and divisor sums. Therefore every fixed-polylogarithmic
\(P\) gives \(O(P L^2\log^{O(1)}(2L)X^\eta)\), still target-safe
after a fresh epsilon budget. There is no unique largest
polylogarithmic threshold; \(P=1\) is the power-exact baseline.

## 2. Exact complement

Every mode has \(j_q(a,v)\ge1\).  Thus the slow sector and

\[
 j_q(a,v)>mq/Y=U/Y
\tag{C189.5}
\]

are disjoint and exhaustive.  The split is imposed on the complex
Round-188 aggregate before its unique outer real part and does not
alter an orientation, height, affine site, selector, deletion, endpoint,
profile, phase, conjugation, or zero extension.

## 3. Exact-conductor and bad-slope controls

For a unit \(b\), exact-conductor inversion gives

\[
 nE_n(b)=\sum_{q\mid n}qK_q(b).
\]

Möbius inversion therefore gives

\[
 K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b).
\tag{C189.6}
\]

For an odd prime \(p\),
\(K_p(b)=E_p(b)-1/p\) and
\(K_p^\circ(b)=K_p(b)+1/p=E_p(b)\).  For
\(1\le h\le(p-1)/2\),

\[
 [-2h]_p=p-2h\quad\hbox{is odd},qquad
 K_p^\circ(-2h)=-1.
\]

Hence the unit-height prefix has modulus \((p-1)/2\).  Uniform
polylogarithmic centered-kernel prefix discrepancy is false.

## 4. First admissible full-complement interface

For one fixed row define the zero-extended literal height amplitude

\[
 A(h)=\mathbf1_{Y<h\le2Y}\mathbf1_{(U,h)=1}
       \sum_{t\in I_{\mathfrak f,\omega}}(-1)^t
       B_{\mathfrak f,\omega}^\sigma(t).
\]

On a dyadic band \(J<j_q(a,v)\le2J\), Abel summation would give the
needed balance if

\[
 \sup_h|A(h)|+\sum_h|A(h+1)-A(h)|
 \ll_\varepsilon \kappa X^\varepsilon.
\tag{C189.7}
\]

Indeed, the height cost \(q/J\) times the projective \(v\)-count
\(O(uJ/q)\) is \(O(u)\), and (C189.7) then gives
\(u\kappa\asymp L\) before the same divisor ledger (C189.3).

Relation (C189.7) is not inherited.  Zero extension across
\((U,h)=1\), squarefree and allocation-coprimality deletions, the moving
residual selector, profiles, endpoints, and affine positivity can all
create height jumps.  The prime bad-slope control also shows that a
kernel-only prefix theorem cannot replace it.  Thus (C189.7), or a
strictly weaker aggregate signed discrepancy theorem with the same
restored power, is the first positive interface to audit; it must not be
assumed.

These controls prove no literal lower mass and no failure of the desired
one-sided estimate.
