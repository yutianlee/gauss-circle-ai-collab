# Formalized hard-M1 \(t=1\) rho-large Farey-covector reduction

- Campaign: m9-m1-t1-rho-large-bezout-edge-gate
- Round: 192
- Starting graph SHA-256:
  75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13
- Evidence status: formal candidate pending seam review
- Numerical theorem evidence: none

## Candidate statement

Fix \(X\ge2\), a nonempty literal middle or lower residual hard-M1 shell
\(L\ge2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\), and

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor.
\tag{192.C1}
\]

Retain every hypothesis and every literal field of the accepted Round-191
rho-large remainder. In particular, on \(Y<h\le2Y\),

\[
 U=mq>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y,\quad
 (a,q)=1,\quad U\mid u,\quad g=u/U,
\tag{192.C2}
\]

\[
 \kappa,g,U\ {\rm odd},\quad (u,v)=1,\quad (U,h)=1,\quad
 0<2\kappa gh<R_0=\lceil L\rceil,
\tag{192.C3}
\]

\[
 u\asymp v\asymp L/\kappa,\qquad
 \operatorname{length}(\mathcal V_{\rm lit})\ll u,\qquad
 L\ll X^{1/4}.
\tag{192.C4}
\]

Keep

\[
 j_q(a,v)=|a\bar v_q|_q>
 T_Q=\min\!\left\{\frac{q-1}{2},
       \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\},
\qquad
 J\le j_q(a,v)<2J,
\tag{192.C4a}
\]

for one nonempty power-of-two fast band. Remove exactly the accepted
Round-191 inverse-small, live-side terminal, and isolated Fejer projections.
For \(v_0=[v]_U\in\{1,\ldots,U-1\}\), let

\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},
\tag{192.C5}
\]

and put

\[
 T=\min\!\left\{\frac{U-1}{2},
       \left\lfloor\frac{QmU}{Y}\right\rfloor\right\}.
\tag{192.C6}
\]

Only rows with \(|\rho|>T\) remain. Fix \(C_0\ge2\), independent of all
asymptotic variables, and define

\[
 A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},
\quad
 \mathcal F_A=
 \{(c,d):1\le c\le A,\ 0\le d\le c,\ (c,d)=1\},
\tag{192.C7}
\]

\[
 \ell_{c,d}=c\beta-d\rho.
\tag{192.C8}
\]

When \(T\ge1\), let

\[
 \mathcal E_A=
 \{v:\exists(c,d)\in\mathcal F_A,\,
       |\ell_{c,d}(v)|\le T\};
\tag{192.C9}
\]

when \(T=0\), set \(\mathcal E_A=\varnothing\). Let \(P_A\) be multiplication
by this single union indicator on the exact Round-191 complex remainder
\(\mathscr R_{\rm fix}\). Then

\[
 \boxed{
 |P_A\mathscr R_{\rm fix}|
 \ll_{B,C_0,\varepsilon}
 Qm\kappa uX^\varepsilon.}
\tag{192.C10}
\]

After the exact \(m^{-1}c_q(a)\) lift, coefficient mass, power-of-two bands,
divisor ledger, and shell sum,

\[
 \boxed{
 |\mathcal O_{Y,Q}^{\sigma}
   (\{P_A\mathscr R_{\rm fix}\})|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.}
\tag{192.C11}
\]

At the fixed-packet level, if
\(\mathscr J_{\rm safe,191,fix}\) is the accepted Round-191 safe aggregate,
then

\[
\mathscr J_{\rm safe,192,fix}
=\mathscr J_{\rm safe,191,fix}+P_A\mathscr R_{\rm fix},
\qquad
\mathscr R_{\rm core,fix}=(I-P_A)\mathscr R_{\rm fix}.
\tag{192.C12}
\]

Applying the inherited linear outer assembly gives the identically typed
global decomposition. Both decompositions occur before the single final real
part. They retain both orientations, outer coprimality flips, affine common
sites, births and deaths, canonical carries, both ordered endpoint arithmetic
masks and coefficients, every shell, cone, selector, profile, floor, star,
half-weight, hard-sample, crossing, trace, endpoint-zero field, the actual
square-root phases, and all zero extensions.

For \(T\ge1\), every core row satisfies

\[
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A),
\qquad
 |\rho|\ge(A+1)(T+1).
\tag{192.C13}
\]

For \(T\ge1\), the core is guaranteed empty when

\[
\boxed{
T\ge1,\qquad
\left\lfloor
 \frac{(U-1)/2}{A+1}
 \right\rfloor\le T,}
\tag{192.C14}
\]

equivalently \(U\le2(A+1)(T+1)-1\). In particular, if
\(|\rho|\le A\), the primitive covector
\((c,d)=(|\rho|,|\beta|)\) has \(\ell=0\).

Outside (192.C14), the estimate

\[
 \Re\mathscr R_{\rm core,Y,Q}^{\sigma}
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon
\tag{192.C15}
\]

remains open. Positive fixed-packet control gives only
\(Y\kappa uX^\varepsilon\), against target
\(Qm\kappa uX^\varepsilon\), with deficit \(Y/(Qm)\).

This candidate proves only the strict Farey union, exact core, coverage
corollaries, and scoped method boundary. It does not prove the complete
rho-large packet, original \(t=1\), any \(t\ge2\) range, a parent, bridge,
theorem, or exponent.

## 1. Canonical coordinates and exact factorization

Equation (192.C5) gives

\[
 (\rho,\beta)=1,\qquad
 0\le\frac{\beta}{\rho}\le1.
\tag{192.C16}
\]

For \(\rho>0\), \(0\le\beta<\rho\). For \(\rho<0\),
\(\rho\le\beta<0\), with \((\rho,\beta)=(-1,-1)\) at the negative edge.
If \(v=v_0+nU\) and

\[
 \rho v-\gamma U=1,
\]

then

\[
 \boxed{\gamma=\beta+n\rho.}
\tag{192.C17}
\]

Thus \(\beta\), not \(\gamma\), is the canonical residue coordinate.

For \(1\le c<U\),

\[
 \begin{aligned}
 \rho(cv_0-dU)
 &=c\rho v_0-d\rho U\\
 &=c+U(c\beta-d\rho),
 \end{aligned}
\]

so

\[
 \boxed{\rho(cv_0-dU)=c+U\ell_{c,d}.}
\tag{192.C18}
\]

The right side is nonzero because it is congruent to \(c\not\equiv0\pmod U\).
This is why \(c<U\) is indispensable.

## 2. Divisor multiplicity and literal row count

Fix \((c,d,\ell)\) and put \(N=c+U\ell\ne0\). Every admissible row gives a
signed divisor \(\rho\mid N\). A selected signed least inverse determines
at most one canonical unit class \(v_0\pmod U\). Hence

\[
 \#\{v_0\bmod U:\ell_{c,d}(v_0)=\ell\}
 \le2\tau(|c+U\ell|).
\tag{192.C19}
\]

For \(|\ell|\le T\),

\[
 0<|c+U\ell|<U^2\ll X^{1/2},
\tag{192.C20}
\]

using \(T\le(U-1)/2\), \(c<U\), and
\(U\le u\ll L\ll X^{1/4}\). Thus the elementary divisor bound gives

\[
 \#\{v_0\bmod U:|\ell_{c,d}|\le T\}
 \ll_\eta TX^\eta
\tag{192.C21}
\]

when \(T\ge1\). The case \(\ell=0\) is included. At \(T=0\), (192.C21)
is not used and the sector is empty.

The family has

\[
 |\mathcal F_A|
 =2+\sum_{2\le c\le A}\varphi(c)
 \ll A^2\le Q^{2C_0}.
\tag{192.C22}
\]

The exact union projector counts every row once; the sum over covectors is
only an upper bound. Since the inherited literal support has total length
\(O(u)\) in a fixed finite interval union and \(U\mid u\), each residue
occurs \(O(u/U+1)=O(u/U)\) times. Therefore

\[
 \#\{v\ {\rm literal}:v\in\mathcal E_A\}
 \ll_\eta
 A^2\frac{uT}{U}X^\eta
 \ll_\eta
 A^2\frac{Qmu}{Y}X^\eta.
\tag{192.C23}
\]

The projective band and every literal mask only delete rows.

## 3. Exact safe projection and no double count

At fixed parameters, the Round-191 identity is

\[
 \mathscr R_{\rm fix}
 =\mathscr J_{\rm fix}
  -\mathscr J_{\rm inv,fix}
  -\mathscr J_{\rm terminal,fix}
  -\mathscr J_{\rm Fejer,fix}.
\tag{192.C24}
\]

Since \(P_A\) acts only on \(|\rho|>T\),
\(P_A\mathscr J_{\rm inv,fix}=0\). Thus

\[
 P_A\mathscr R_{\rm fix}
 =P_A\mathscr J_{\rm fix}
  -P_A\mathscr J_{\rm terminal,fix}
  -P_A\mathscr J_{\rm Fejer,fix}.
\tag{192.C25}
\]

Apply endpoint-exact Abel inversion row by row to
\(P_A\mathscr J_{\rm fix}\), returning exactly to the original row sum
before positive counting. Each selected row has \(O(Y)\) heights,
\(O(\kappa)\) live sites per height, and
\(O_\eta(X^\eta)\) endpoint weight. Equation (192.C23) gives

\[
 |P_A\mathscr J_{\rm fix}|
 \ll_\eta A^2Qm\kappa uX^{2\eta}.
\tag{192.C26}
\]

Deleting rows cannot increase the accepted positive terminal and Fejer
bounds, so their restricted sum is
\(O_\eta(\kappa uX^\eta)\). Since \(A^2\le Q^{2C_0}\) is a fixed
polylogarithm, a fresh epsilon allocation proves (192.C10).

Algebraically, the new safe aggregate is

\[
 \mathscr J_{\rm inv,fix}
 +(I-P_A)\mathscr J_{\rm terminal,fix}
 +(I-P_A)\mathscr J_{\rm Fejer,fix}
 +P_A\mathscr J_{\rm fix}.
\tag{192.C27}
\]

Thus terminal and Fejer pieces on Farey rows are replaced by the complete
original Farey-row packet; nothing is counted twice.

## 4. Exact outer ledger

The accepted lift and coefficient mass are

\[
 c_{mq}(ma)=m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q).
\tag{192.C28}
\]

The \(m^{-1}\) cancels the \(m\) in (192.C26) before positive outer
summation. Power-of-two projective bands cost a logarithm and

\[
 \sum_{mq\mid u}1\le\tau_3(u).
\tag{192.C29}
\]

Consequently

\[
 Q^{2C_0+1}X^{2\eta}
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.
\tag{192.C30}
\]

All fixed powers of \(Q\), divisor and band logarithms, and
\(X^{2\eta}\) are assigned fresh epsilon budget. No positive power of
\(Y\), \(U\), or \(L\) is absorbed. This proves (192.C11).

## 5. Circular-pigeonhole coverage

Put \(r=|\rho|\), \(b=|\beta|\). Then
\(0\le b\le r\), \((b,r)=1\), and

\[
 |c\beta-d\rho|=|cb-dr|.
\tag{192.C31}
\]

Consider \(0,b,\ldots,Ab\pmod r\) on the circle of circumference \(r\).
If \(A\ge r\), a repeated point gives zero error. If \(A<r\), the
\(A+1\) distinct circular gaps sum to \(r\), so one has integral length
at most \(\lfloor r/(A+1)\rfloor\). Its index difference gives
\(1\le c\le A\) and \(0\le d\le c\) with

\[
 |cb-dr|\le\left\lfloor\frac r{A+1}\right\rfloor.
\tag{192.C32}
\]

Dividing \((c,d)\) by its gcd preserves the constraints and only decreases
the determinant. Hence

\[
 \min_{(c,d)\in\mathcal F_A}|c\beta-d\rho|
 \le\left\lfloor\frac{|\rho|}{A+1}\right\rfloor.
\tag{192.C33}
\]

If a \(T\ge1\) row lies in the core, the left side is at least \(T+1\).
Equations (192.C13)--(192.C14) follow. This is deterministic coverage, not
cancellation.

## 6. Exact phase/carry identities and method boundary

For \(v=v_0+nU\), put

\[
 d_v=cn+d,\qquad
 \Delta=cv-d_vU=cv_0-dU.
\tag{192.C34}
\]

Then

\[
 \rho\Delta=c+U\ell,\qquad
 \gamma\Delta=d_v+v\ell.
\tag{192.C35}
\]

For
\(z_{\omega,v}=e(\epsilon_\omega a\rho/q)\),

\[
 z_{\omega,v}^{\Delta}
 =e(\epsilon_\omega ac/q).
\tag{192.C36}
\]

For every finite or absolutely summable height sequence \(W\), extended by
zero to all \(h\in\mathbb Z\), the long-step Abel identity

\[
 \frac1{1-z^\Delta}
 \sum_h\{W(h)-W(h-\Delta)\}z^h
 =\sum_hW(h)z^h
\tag{192.C37}
\]

is an exact self-return when \(z^\Delta\ne1\), and is unavailable when
\(z^\Delta=1\). It gives no saving.

Let \(S_{0,\omega}(h)\in[0,U)\) be the unique canonical anchor satisfying
\(S_{0,\omega}(h)\equiv\epsilon_\omega\rho h\pmod U\), and define

\[
 N_\omega(h;\Delta)=
 \frac{S_{0,\omega}(h+\Delta)-S_{0,\omega}(h)
       -\epsilon_\omega\rho\Delta}{U}.
\tag{192.C38}
\]

Then

\[
N_\omega(h;\Delta)
=\theta_{\omega,c}(h)-\epsilon_\omega\ell,
\tag{192.C39}
\]

where

\[
\theta_{\omega,c}(h)=
\frac{S_{0,\omega}(h+\Delta)-S_{0,\omega}(h)
      -\epsilon_\omega c}{U},
\qquad
\theta_{+,c}\in\{-1,0\},\quad
\theta_{-,c}\in\{0,1\}.
\tag{192.C39a}
\]

The inherited affine reindexing changes parity by \((-1)^{N_\omega}\).
The accumulated retained mode-and-affine factor is

\[
 (-1)^{N_\omega(h;\Delta)}e(\epsilon_\omega ac/q).
\tag{192.C40}
\]

The core condition controls neither its parity nor its distance from one.
Put \(A_0=\kappa gU\) and \(C_v=\kappa v\). Under forward displacement by
\(\Delta\), the signed changes in the ordered endpoint number/divisor pairs
are

\[
\begin{array}{c|cc}
 &\Delta N_{i,+}&\Delta d_{i,+}\\ \hline
i=0&2A_0(d_v+v\ell)&0\\
i=1&2gC_v(c+U\ell)&2g(c+U\ell)
\end{array}
\tag{192.C40a}
\]

and

\[
\begin{array}{c|cc}
 &\Delta N_{i,-}&\Delta d_{i,-}\\ \hline
i=0&-2gC_v(c+U\ell)&-2g(c+U\ell)\\
i=1&-2A_0(d_v+v\ell)&0.
\end{array}
\tag{192.C40b}
\]

These translations need not coincide and contain the
representative-dependent \(d_v\). Consequently masks, cells, phases, births,
and deaths are not transport invariant.

In the ambient prime-modulus control, restrict to an unsaturated regime
\(1\le T<(U-1)/2\) in which the two inherited fast predicates leave
\(\asymp U\) central residue classes. Each fixed covector meets only
\(O_\eta(TX^\eta)\) classes. A coefficient-blind cover therefore requires,
up to divisor slack,
\[
 M\gg_\eta \frac{U}{TX^\eta}
 \asymp \frac{Y}{Qm}X^{-\eta}
\tag{192.C41}
\]
covectors. Positive recombination restores the original deficit. This is a
residue-universe mechanism control, not a lower bound for the masked literal
core. Bounded zero-extended height arrays likewise retain full
normalized-Abel capacity after any static Farey selector. These are
coefficient-class controls, not literal lower mass and not a disproof of
(192.C15).

## 7. First unproved step, dependencies, and state scope

The first unproved step is (192.C15), or the stronger fixed-packet estimate

\[
 |\mathscr R_{\rm core,fix}|
 \ll_{C_0,\varepsilon}Qm\kappa uX^\varepsilon.
\tag{192.C42}
\]

A future proof needs a jointly signed correlation theorem for the actual
unequal endpoint translations, masks, carry, square-root phases, and affine
births/deaths before any positive norm.

Direct dependencies:

- M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction;
- Divisor-bound-elementary.

The exact lift, projective-band, shell, and endpoint connectors are inherited
through the accepted Round-191 dependency chain. The proposed state effect is
one subordinate proved-internal reduction added only as a dependency and
inconclusive evidence of the still-open hard-M1 small-\(t\) owner.

Every original \(t\ge2\) small-\(G\) incidence, the large-\(G\)
near-resonant complement, the remaining small-\(t\) owner, hard and smooth
M1, GAR, every M2 parent, endpoint uniformity, M9, both bridges, the quarter
target, and every exponent remain open, conditional, or unchanged.
