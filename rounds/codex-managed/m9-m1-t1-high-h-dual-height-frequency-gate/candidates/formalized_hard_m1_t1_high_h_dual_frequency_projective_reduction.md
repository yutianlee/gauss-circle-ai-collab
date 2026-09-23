# Hard-M1 \(t=1\) high-height dual-frequency projective reduction

- Campaign: m9-m1-t1-high-h-dual-height-frequency-gate
- Round: 189
- Starting graph SHA-256:
  338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c
- Discovery report SHA-256:
  65636c38a3b0c3dbd4a26839dbc89daa88ef78dee5638d02d0de1192b9bdfd38
- Hostile report SHA-256:
  b8ec876aebcc6668646880813bad0abf576063f58e71518d29c8e5778d371608
- Blind report SHA-256:
  13169505840f9033fb8ddaac6eba62d12988a669127f593a8bc48438543621a3
- Evidence status: formal candidate pending independent seam review
- Numerical theorem evidence: none

## Candidate statement

Fix real \(X\ge2\), a nonempty literal middle or lower residual
hard-M1 shell \(L\ge2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\),
and

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor.
\tag{189.K1}
\]

On nonzero inherited hard-top support \(L\ll X^{1/4}\). Fix a
nonempty dyadic integer block \(Y<h\le2Y\) with \(Y>Q\). Retain
exactly the accepted Round-185 carrier (K185.27),
(K185.30)--(K185.35) and the Round-188 complement. Thus

\[
 \kappa,g,U\ {\rm odd},\quad u=gU,\quad (u,v)=1,\quad
 (U,h)=1,\quad 0<2\kappa gh<R_0,
\tag{189.K2}
\]

and every selector, squarefree and allocation-coprimality deletion,
profile, floor, star, half-weight, hard sample, crossing, endpoint,
conjugation, Fejer factor, square-root phase, sign, positivity
predicate, affine site, orientation, and zero extension remains
literal. The exact lift coordinates obey

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y,
\qquad (a,q)=1.
\tag{189.K3}
\]

Because \(U\) is odd, \(m\) and \(q\) are odd. Since
\(q\mid U\mid u\) and \((u,v)=1\), define

\[
 j_q(a,v)=|a\bar v_q|_q,
\qquad
 T_Q(m,q;Y)=\min\!\left\{\frac{q-1}{2},
       \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\}.
\tag{189.K4}
\]

Let \(\mathscr C_{Y,Q}^{\sigma}\) be the exact complex complement in
(188.K10)--(188.K12). Equivalently, writing the accepted literal
endpoint aggregate as \(A_{\kappa,u,mq,h,v,\omega}^{\sigma}\),

\[
\begin{aligned}
 \mathscr C_{Y,Q}^{\sigma}
 ={}&\sum_{\omega\in\{+,-\}}\sum_{\kappa,u}
 \sum_{\substack{mq\mid u\\mq>4Q,\ q>Q,\ Qm<Y}}
 \frac1m
 \sum_{\substack{Y<h\le2Y\\(mq,h)=1\\
       0<2\kappa(u/(mq))h<R_0}}
 \sum_{\substack{v>0\\(u,v)=1}}
 \sum_{\substack{a\in(\mathbb Z/q\mathbb Z)^\times\\
                   m|a|_q>Q}}
 c_q(a)e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right)
 A_{\kappa,u,mq,h,v,\omega}^{\sigma},
\end{aligned}
\tag{189.K5}
\]

with every sum interpreted through the inherited literal zero
extension. Insert \(1\le j_q(a,v)\le T_Q(m,q;Y)\) to define
\(\mathscr S_{Y,Q}^{\sigma}\), and insert
\(j_q(a,v)>T_Q(m,q;Y)\) to define
\(\mathscr F_{Y,Q}^{\sigma}\). Before any triangle inequality,

\[
 \boxed{\mathscr C_{Y,Q}^{\sigma}
 =\mathscr S_{Y,Q}^{\sigma}+\mathscr F_{Y,Q}^{\sigma}.}
\tag{189.K6}
\]

The complete projectively slow sector is absolutely target-safe:

\[
 \boxed{|\mathscr S_{Y,Q}^{\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{189.K7}
\]

The same proof with \(Q\) replaced by \(1\) proves the baseline
\(j_q(a,v)\le\lfloor U/Y\rfloor\). More generally, a predeclared
fixed polylogarithmic multiplier is harmless, but no positive power of
\(X\) is absorbed. The frozen candidate uses exactly \(Q\).

The exact remaining one-sided relation is

\[
 \boxed{\Re\mathscr F_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{189.K8}
\]

It is not proved. Equations (189.K6)--(189.K8) preserve one outer
real part over both orientations and every literal label. No complete
high-height relation, complete original-\(t=1\) residual, small-\(t\)
owner, parent, bridge, theorem, or exponent is asserted.

## Proof of the target-safe sector

For fixed \(a\in(\mathbb Z/q\mathbb Z)^\times\), the map

\[
 v\bmod q\longmapsto a\bar v_q\bmod q
\tag{189.K9}
\]

is a bijection on the units. For \(0\le T\le(q-1)/2\), the condition
\(1\le|a\bar v_q|_q\le T\) uses exactly

\[
 2\sum_{\substack{1\le r\le T\\(r,q)=1}}1\le2T
\tag{189.K10}
\]

unit classes. The two least-residue sides are disjoint because \(q\)
is odd. At \(T=0\) the set is empty; at \(T=(q-1)/2\) it is all unit
classes.

The literal \(v\)-support is contained in an interval of length
\(O(u)\). Each residue class modulo \(q\) occurs
\(O(u/q+1)=O(u/q)\) times because \(q\mid u\). Literal deletions can
only reduce the count. Hence, at fixed
\((\kappa,u,m,q,a)\),

\[
 \#\{v:1\le j_q(a,v)\le T_Q\}
 \ll\frac{uT_Q}{q}
 \ll\frac{Qum}{Y}.
\tag{189.K11}
\]

There are \(O(Y)\) heights and \(O(1+\kappa)=O(\kappa)\) live affine
sites per oriented row. The exact lift normalization and coefficient
mass are

\[
 c_{mq}(ma)=\frac1m c_q(a),\qquad
 \sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|c_q(a)|
 \ll\log(2q).
\tag{189.K12}
\]

Thus the factor \(Y\) in the height count cancels \(Y^{-1}\) in
(189.K11), and the factor \(m\) in (189.K11) cancels the exact
\(m^{-1}\) in (189.K12), before any outer positive recombination.
The fixed \((\kappa,u,m,q)\) cost is

\[
 \ll_\eta Q\kappa u\log(2q)X^\eta.
\tag{189.K13}
\]

There is no fourth divisor variable. Writing \(u=mqr\),

\[
 \sum_{mq\mid u}\log(2q)
 \le\tau_3(u)\log(2u).
\tag{189.K14}
\]

Using \(u\asymp L/\kappa\), elementary triple-divisor summation, and
the inherited \(L\ll X^{1/4}\),

\[
\begin{aligned}
 |\mathscr S_{Y,Q}^{\sigma}|
 &\ll_\eta QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log(2u)\\
 &\ll_\eta QL^2\log^{O(1)}(2L)X^\eta
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\end{aligned}
\tag{189.K15}
\]

No positive power of \(Y\) is absorbed. If the cap in (189.K4)
saturates, every unit slope is already included and the fast
complement is empty for that lift; (189.K11)--(189.K15) remain valid.
This proves (189.K7).

## Exact fast interface and quantitative deficit

For fixed \((\kappa,u,m,q,v,\omega)\), let
\(W_{\kappa,u,mq,v,\omega}^{\sigma}(h)\) be the exact
zero-extended height sequence obtained from (189.K5), including the
dyadic height block, \((mq,h)=1\), the carrier inequality, the complete
literal endpoint aggregate, and all selectors and masks. Let

\[
 \mathsf V(W)=\sum_{h\in\mathbb Z}|W(h+1)-W(h)|.
\tag{189.K16}
\]

On \(J\le j_q(a,v)<2J\), Abel summation gives

\[
 \left|\sum_hW(h)e(\epsilon_\omega a\bar v_qh/q)\right|
 \ll\frac qJ\mathsf V(W).
\tag{189.K17}
\]

Uniformly for every fixed admissible
\(a\in(\mathbb Z/q\mathbb Z)^\times\) with \(m|a|_q>Q\), and every
complementary dyadic \(J\)-band, the first target-scaled sufficient
input is

\[
 \boxed{
 \sum_{\substack{\omega,\ v\ {\rm literal}\\
                  J\le j_q(a,v)<2J}}
 \mathsf V(W_{\kappa,u,mq,v,\omega}^{\sigma})
 \ll_\eta\frac{Qm\kappa uJ}{q}X^\eta.}
\tag{189.K18}
\]

Together with (189.K17), the \(m^{-1}\) lift weight, coefficient mass,
dyadic \(J\)-sum, and (189.K14), this would prove (189.K8). A genuinely
joint signed discrepancy estimate with the same final ledger would
also suffice.

No accepted dependency proves (189.K18). Pointwise boundedness and
the literal \(O(\kappa)\) affine-site count give only

\[
 \mathsf V(W)\ll_\eta Y\kappa X^\eta,
 \qquad
 \sum_{v\ {\rm in\ the\ band}}\mathsf V(W_v)
 \ll_\eta\frac{Y\kappa uJ}{q}X^\eta.
\tag{189.K19}
\]

The deficit relative to (189.K18) is \(Y/(Qm)>1\). Primitive lifts
retain \(Y/Q\), a non-polylogarithmic height loss. Changing \(h\)
changes the coprimality and squarefree masks, residual selector,
profile, anchors, affine range, endpoints, floors, crossings, Fejer
factor, square-root phase, and terminal zero extension. The exact
first difference is a common-range difference plus births and deaths
of literal affine sites; none has a proved improvement over
(189.K19). Periodicity of the displayed exponential does not make
the literal coefficient periodic or bounded-variation.

## Centered-kernel and false-mechanism controls

For actual odd \(q\) and unit \(b\bmod q\), put

\[
 K_q(b)=\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
 c_q(a)e(ab/q),\qquad
 K_q^\circ(b)=K_q(b)-\frac{\mu(q)}q.
\tag{189.K20}
\]

Exact-conductor partition and Möbius inversion give

\[
 K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b),
 \qquad K_q^\circ(-b)=-K_q^\circ(b).
\tag{189.K21}
\]

Oddness is essential and is supplied by (189.K2). For odd prime \(p\),

\[
 K_p^\circ(b)=E_p(b),\qquad
 \sum_{h=1}^{(p-1)/2}K_p^\circ(-2h)=-\frac{p-1}{2}.
\tag{189.K22}
\]

Thus exact-conductor centering alone cannot supply a uniform
polylogarithmic height-prefix estimate. This is a full-kernel
falsifier, not literal lower mass: the open packet retains the
ordinary-frequency deletion, projective fast split, endpoint
coefficient, masks, and both orientations.

Likewise, an abstract bounded array can dephase the displayed height,
affine-parity, and square-root phases and attain carrier capacity. It
rules out a coefficient-uniform proof from support and boundedness
alone, but need not equal the literal endpoint coefficient. Positive
completion, large-sieve, Poisson, alias energy, and selector-blind
sieve opening return positive capacity and do not establish
(189.K18).

## Scope, dependencies, and controls

The proved content is only:

1. the projective unit-class bijection and exact capped count;
2. the complete \(j_q(a,v)\le T_Q\) absolute sector;
3. the exact one-real-part fast complement;
4. the first sufficient actual-coefficient discrepancy interface and
   its \(Y/(Qm)\) deficit; and
5. the odd-conductor centered-kernel bad-slope control.

Even a proof of (189.K8) would close only the exact original-\(t=1\)
residual through the accepted Round-184/185/187/188 connectors. Every
original \(t\ge2\) small-\(G\) incidence, the large-\(G\)
near-resonant complement, the complete hard and smooth M1 parents,
GAR, every M2 parent, endpoint uniformity, M9, both bridges, the
quarter target, and every exponent claim remain open.

Direct accepted dependencies are:

- M9-M1-hard-top-t1-high-h-imprimitive-lift-gcd-reduction;
- Divisor-bound-elementary.

The candidate reconciles the three Round-189 reports and
reviews/conductor_round189_report_reconciliation.md. The bounded
Wolfram diagnostic checks finite odd-conductor projective counts,
kernel identities, and bad slopes only; it is not asymptotic theorem
evidence.
