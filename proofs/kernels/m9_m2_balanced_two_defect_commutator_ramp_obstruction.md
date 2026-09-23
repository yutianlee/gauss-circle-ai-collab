# M9--M2 balanced two-defect commutator and ramp obstruction

- Campaign: `m9-m2-balanced-critical-j1-two-defect-commutator-gate`
- Round: 171
- Role: conductor-selected proof kernel
- Starting graph SHA-256:
  `4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`
- Terminal label: `balanced_two_defect_commutator_no_go`
- Allocation: 100% analytic/algebraic; 0% numerical experimentation

## 1. Exact scope and result

Fix one literal persistent critical \(j=1\) balanced block, so
\(L\asymp K\asymp X^{1/6}\).  Put

\[
 a(h,k)=\chi _4(h)\eta\!\left(\frac{(h,k)}{\sqrt L/2}\right)A_B(h,k),
\]

with the accepted profiles, floors, stars, crossings, shifts, and endpoints,
and extend \(a\) by zero off its positive literal support.  If the accepted
divisor-alias expansion is opened, every lift and alias remains
corner-dependent; it is not a separate coordinate of \(a\).  For an ordered
pair write

\[
 p=h'-h,\quad q=k'-k,\quad
 \Delta=h'k'-hk,\quad \rho=hk'-h'k.
\tag{171.K1}
\]

The following facts are proved.

1. The increment chart is a multiplicity-one bijection and

   \[
    \Delta+\rho=q(2h+p),\qquad
    \Delta-\rho=p(2k+q).
    \tag{171.K2}
   \]

   On character support \(p=2s\) and
   \(\chi _4(h)\chi _4(h+p)=(-1)^s\).
2. The genuine \(p=0\) and \(q=0\) sectors, and every fixed-width slice
   \(|(k+k')-(h+h')|\le C\), have absolute mass
   \(O_{C,\varepsilon}(L^3X^\varepsilon)\).
3. The four canonical first multiplication/difference commutators supplied
   by (171.K2), after normalization by their exact affine increments, are
   translations.  Their normalized two-direction commutators therefore
   vanish.  A parity-compatible unnormalized diagonal commutator is nonzero,
   but its multiplier cancels on division and returns only the original
   alternating diagonal difference.
4. The exact real endpoint-swap decomposition has only two parity pieces:
   the double-antisymmetric term and one \((++)\) complement.  The complement
   is not algebraically zero and retains coefficient-blind
   \(L^4X^\varepsilon\) capacity.
5. A second, coefficient-independent local summation by parts in the
   uncharactered \(q\)-direction necessarily uses a primitive of size
   \(\gg L\) on a full balanced fibre.  It raises the target-scale
   one-step gate/support-face ledger from \(L^3X^\varepsilon\) back to
   \(L^4X^\varepsilon\), while the bulk has no coefficientwise small phase
   difference.

Consequently the canonical coordinate-multiplier commutators, independent
endpoint swaps, and coefficient-independent two-step local Abel placement do
not supply the missing factor \(L\) before a positive norm.  This is a
route-scoped obstruction, not a lower bound for the physical scalar and not
a disproof of the open estimate

\[
 |\mathcal R_B^{\rm osc}|\ll_\varepsilon L^3X^\varepsilon.
\tag{171.K3}
\]

## 2. Coordinate, character, and axial ledger

Let \(\mathcal S_B\) be the literal support of \(a\).  The ordered far domain
is

\[
 \Omega_B=\{(h,k,h',k')\in\mathcal S_B^2:
 h,h'\text{ odd},\ |\Delta|>L,\ |\rho|>L\}.
\]

It is in bijection with

\[
\begin{aligned}
 \mathcal D_B=\{(h,k,p,q):
 &(h,k),(h+p,k+q)\in\mathcal S_B,\ h,h+p\text{ odd},\\
 &|hq+kp+pq|>L,\ |hq-kp|>L\}
\end{aligned}
\tag{171.K4}
\]

through \(p=h'-h,\ q=k'-k\), with inverse
\((h,k,p,q)\mapsto(h,k,h+p,k+q)\).  Thus the multiplicity is one, including
negative \(p,q\).  Direct substitution proves

\[
 \Delta=hq+kp+pq,\qquad \rho=hq-kp,
\]

and hence (171.K2).  If \(pq\ne0\), putting
\(u=\Delta+\rho,\ v=\Delta-\rho\) gives

\[
 h=\frac12\left(\frac uq-p\right),\qquad
 k=\frac12\left(\frac vp-q\right).
\tag{171.K5}
\]

The exact reconstructed-character conditions include

\[
 p\in2\mathbb Z,\quad q\mid u,\quad p\mid v,\quad
 \frac uq-p\equiv2\pmod4,\quad \frac vp-q\equiv0\pmod2,
\tag{171.K6}
\]

and \(u\equiv v\pmod2\) if \(u,v\) are introduced independently.  Formula
(171.K5) is not used on an axis.

For \(p=2s\) and odd \(h\),

\[
 \chi _4(h)\chi _4(h+2s)=(-1)^s.
\tag{171.K7}
\]

The sign is constant on a fixed-\(p\) fibre.  On \(p=0\),
\(\Delta=\rho=hq\), and there are \(O(LK^2)\) literal triples.  On \(q=0\),
\(\Delta=kp,\ \rho=-kp\), and there are \(O(KL^2)\) triples.  Since
\(K\asymp L\), bounded literal weights and \(|e(t)-1|\le2\) give

\[
 \text{axis }p=0\; +\; \text{axis }q=0
 \ll_\varepsilon L^3X^\varepsilon.
\tag{171.K8}
\]

Their intersection is excluded by the far gates.

## 3. Normalized and unnormalized commutators

Fix \(h,k\), put \(p=2s\), and let

\[
 T_sf(s,q)=f(s+1,q),\qquad T_qf(s,q)=f(s,q+1),
\]

\(D_s=T_s-I,\ D_q=T_q-I\).  With

\[
 x=h+h'=2h+2s,\quad y=k+k'=2k+q,\quad
 U=qx,\quad V=2sy,
\tag{171.K9}
\]

and \(M_w\) denoting multiplication by \(w\), the identity

\[
 [D_t,M_w]=(D_tw)T_t
\tag{171.K10}
\]

gives

\[
\begin{array}{c|cc}
 &M_U&M_V\\ \hline
 [D_s,\,\cdot]&2qT_s&2yT_s\\
 [D_q,\,\cdot]&xT_q&2sT_q.
\end{array}
\tag{171.K11}
\]

Away from the already paid axes, normalizing by the displayed nonzero
increment yields \(T_s\) or \(T_q\); normalizing the two nonsingular side-sum
entries yields

\[
 x^{-1}[D_q,M_U]=T_q,\qquad
 (2y)^{-1}[D_s,M_V]=T_s.
\tag{171.K12}
\]

Thus the normalized operators commute.  This does not say that all
unnormalized multiplication/shift commutators vanish.  Indeed, for
\(\mathcal C_s=2yT_s,\ \mathcal C_q=xT_q\),

\[
 [\mathcal C_s,\mathcal C_q]=2(2y-x)T_sT_q.
\tag{171.K13}
\]

For fixed \(t=2y-x\), choosing \(h,h',k\) determines at most one \(k'\);
therefore every fixed-width \(|2y-x|\le C\) strip has absolute mass
\(O_{C,\varepsilon}(L^3X^\varepsilon)\).  Off the singular line, division
by \(2(2y-x)\) gives \(T_sT_q\), and

\[
 \sum_{s,q}(-1)^s(T_sT_q-I)F(s,q)
 =-2\sum_{s,q}(-1)^sF(s,q).
\tag{171.K13a}
\]

Thus (171.K13) is also a shift tautology after its singular strip is paid.

For the parity-compatible \(q\)-shift \(\widehat T_q=T_q^2\), put

\[
 \mathfrak P=[D_s,M_V]=2yT_s,\qquad
 \mathfrak Q=[\widehat T_q-I,M_U]=2x\widehat T_q.
\]

Since \(T_sx=x+2\) and \(\widehat T_qy=y+2\),

\[
 \boxed{[\mathfrak P,\mathfrak Q]
 =8(y-x)T_s\widehat T_q.}
\tag{171.K14}
\]

On \(y\ne x\), division by \(8(y-x)\) gives precisely the shift
\(T_s\widehat T_q\).  Moreover, for every finitely supported \(F\),

\[
 \sum_{s,q}(-1)^s(T_s\widehat T_q-I)F(s,q)
 =-2\sum_{s,q}(-1)^sF(s,q).
\tag{171.K15}
\]

Hence the multiplier in (171.K14) cancels coefficientwise before any
estimate and returns the original alternating scalar, with \(L^4\) positive
capacity.  The singular strip is not discarded: for fixed integer
\(t=y-x\), choosing \(h,h',k\) determines \(k'=h+h'+t-k\).  Therefore

\[
 \sum_{|y-x|\le C}|\text{literal summand}|
 \ll_{C,\varepsilon}L^3X^\varepsilon.
\tag{171.K16}
\]

Equations (171.K11)--(171.K16) cover only the four displayed elementary
placements and the two displayed ordinary/parity-compatible commutators.
The backward and composite Weyl commutators recorded in the independent
ramp review, as well as every coefficient-adapted or nonlocal commutator,
are outside this kernel.

## 4. Exact real endpoint-swap identity

Choose finite positive-integer intervals \(I_h,I_k\) containing the
geometric \(h\)- and \(k\)-supports, zero extend \(a\), and sum over the
endpoint rectangle

\[
 \Omega=I_h^2\times I_k^2
 =\{(h,k,p,q):h,h+p\in I_h,\ k,k+q\in I_k\}.
\tag{171.K17a}
\]

This shifted image, rather than independent rectangular ranges for
\((h,k,p,q)\), is invariant under the commuting swaps

\[
 \tau_h(h,k,p,q)=(h+p,k,-p,q),\qquad
 \tau_k(h,k,p,q)=(h,k+q,p,-q).
\tag{171.K17}
\]

They preserve the double-far gate \(G\), because

\[
 \tau_h:(\Delta,\rho)\mapsto(\rho,\Delta),\qquad
 \tau_k:(\Delta,\rho)\mapsto(-\rho,-\Delta).
\]

Put

\[
 a_{ij}=a(h+ip,k+jq),\qquad
 z_{ij}=e\!\left(\sqrt X\sqrt{(h+ip)(k+jq)}\right),
\]

with \(z_{ij}\) defined throughout the positive ambient rectangle.  Any
coefficient involving a point outside literal support is zero.  Let

\[
 W=a_{00}a_{11},\qquad H=z_{00}\overline{z_{11}}-1.
\]

The coefficient is real, and the full atom swap is \(\tau_h\tau_k\).
The global sum is therefore real.  With

\[
 P_{\epsilon\eta}=\frac14(I+\epsilon\tau_h)(I+\eta\tau_k),
 \qquad D_h=I-\tau_h,\quad D_k=I-\tau_k,
\]

self-adjointness of the permutations gives

\[
 \langle W,H\rangle_G
 =\sum_{\epsilon,\eta}\langle
 P_{\epsilon\eta}W,P_{\epsilon\eta}H\rangle_G.
\]

Writing \(A=z_{00}\overline{z_{11}}\) and
\(B=z_{01}\overline{z_{10}}\), reality gives

\[
 P_{+-}W=P_{-+}W=0,
\]

\[
 P_{++}W=\frac12(a_{00}a_{11}+a_{10}a_{01}),\qquad
 P_{++}H=-\frac14\bigl(|z_{00}-z_{11}|^2+|z_{01}-z_{10}|^2\bigr),
\]

and \(P_{--}H=\frac14D_hD_kH\).  Thus

\[
 \boxed{
 \langle W,H\rangle_G
 =\langle P_{++}W,P_{++}H\rangle_G
 +\frac1{16}\langle D_hD_kW,D_hD_kH\rangle_G.}
\tag{171.K18}
\]

Global zero extension includes all cross-corner support failures, so no
extra support-crossing sum belongs in (171.K18).  The mixed parity pieces
vanish, but the \((++)\) term does not.  In the nonnegative erased-structure
control it can accumulate with one sign; for the literal coefficient its
available positive ledger remains \(L^4X^\varepsilon\).  This is a capacity
control, not a literal lower bound.

## 5. Mixed summation by parts and the forced ramp

Remove the character product from the complete zero-extended literal
summand and write it as \(F_{h,k}(s,q)\), including both strict gates and
\(e(\sqrt X(\sqrt{hk}-\sqrt{(h+2s)(k+q)}))-1\).  Piecewise define
\(F_{h,k}(s,q)=0\) unless both diagonal atoms lie in the positive literal
support, and evaluate the displayed square roots only on the remaining
positive domain.  With this convention,

\[
 \mathcal R_B^{\rm osc}
 =\sum_{h,k,s,q}(-1)^sF_{h,k}(s,q).
\tag{171.K19}
\]

Finite reindexing yields

\[
 \sum_s(-1)^sD_sG(s)=-2\sum_s(-1)^sG(s),
\]

and, for any \(q_0\in\mathbb R\),

\[
 \sum_qG(q)=-\sum_q(q-q_0)D_qG(q).
\]

Therefore

\[
 \boxed{
 \mathcal R_B^{\rm osc}
 =\frac12\sum_{h,k,s,q}(-1)^s(q-q_0)D_sD_qF_{h,k}(s,q).}
\tag{171.K20}
\]

The ramp is unavoidable for any coefficient-independent first-difference
representation.  If an interval \(I=\{a,\ldots,b\}\) has length \(N\) and

\[
 \sum_{q\in I}f(q)=\sum_qc(q)(f(q)-f(q-1))
\tag{171.K21}
\]

for every \(f\) supported on \(I\), coefficient comparison gives
\(c(r)-c(r+1)=1\) on \(I\).  Hence

\[
 \max_q|c(q)|\ge N/2.
\tag{171.K22}
\]

The ambient geometric/profile \(q\)-intervals contain runs of length
\(\asymp K\asymp L\).  The far gates remove only \(O(1)\)-width intervals
from such a run, because their \(q\)-slopes are \(h\) and
\(h'=h+2s\asymp L\).  Arithmetic zeros of the low-gcd weight remain inside
the coefficient rather than defining new support components.  Splitting a
geometric run only moves the same total variation into new endpoints.  Thus
the second coefficient-independent local primitive has size \(\gg L\).

## 6. Boundaries, powers, and surviving rulings

Write the geometric/profile-support and far-gate indicator as

\[
 I=JH^\Delta H^\rho,\qquad
 J=1_{(h+2s,k+q)\text{ in positive geometric/profile support of }A_B},\quad
 H^\Delta=1_{|\Delta|>L},\quad H^\rho=1_{|\rho|>L}.
\]

At the four corners \((s+i,q+j)\), the exact product rule is

\[
\begin{aligned}
 D_sD_q(IY)=\;&I_{11}D_sD_qY
 +(I_{11}-I_{01})D_qY+(I_{11}-I_{10})D_sY\\
 &+(I_{11}-I_{10}-I_{01}+I_{00})Y_{00}.
\end{aligned}
\tag{171.K23}
\]

On each oriented edge the exact three-factor expansion is

\[
\begin{aligned}
 I_+-I_0={}&(J_+-J_0)H^\Delta_+H^\rho_+\\
 &+J_0(H^\Delta_+-H^\Delta_0)H^\rho_+\\
 &+J_0H^\Delta_0(H^\rho_+-H^\rho_0).
\end{aligned}
\tag{171.K23a}
\]

Here both arithmetic low-gcd factors, including their holes and unit
differences, remain in \(Y\).  They are not used in the geometric face
count.  The defect increments are

\[
\begin{array}{c|cc}
 &\Delta_+-\Delta&\rho_+-\rho\\ \hline
 s\mapsto s+1&2(k+q)&-2k\\
 q\mapsto q+1&h+2s&h.
\end{array}
\tag{171.K24}
\]

They are \(O(L)\).  A changed sharp gate therefore lies in an
\(O(L)\)-width collar around \(\pm L\).  The accepted corridor theorem and
the geometric/profile one-coordinate support count give

\[
 \text{unweighted one-step gate/geometric-support faces}
 \ll_\varepsilon L^3X^\varepsilon.
\tag{171.K25}
\]

Absent a new signed face theorem, multiplication by the forced ramp in
(171.K20) restores the available coefficient-independent positive ledger to
\(L^4X^\varepsilon\).  This is not a physical lower bound for a literal
face.  In the common interior, the exact mixed product rule
contains the undifferenced literal coefficient times

\[
 e(\theta_{11})-e(\theta_{10})-e(\theta_{01})+e(\theta_{00}),
\]

which can be \(O(1)\); the arithmetic gcd differences have no uniform
\(L^{-1}\) bound.  Hence positive closure after (171.K20) supplies no target
estimate.

The accepted fixed-\(Q\) ruling is also untouched.  With

\[
 c=\frac\lambda R\sqrt{h/k},\qquad A=k'/k,qquad
 Q=\frac{\mu^2h}{d^2k}=Xc^2,
\]

the real stationary centre gives

\[
 \rho=hk'\frac{c^2-1}{c^2},\qquad
 \Delta=hk\frac{A^2-c^2}{c^2}.
\tag{171.K26}
\]

At \(A=1\), \(\Delta=-\rho\), and fixed \(Q\) can remain beyond both
corridors.  Coordinate differences move between, rather than eliminate,
these ruling classes.  This only blocks reuse of the accepted positive
broad--narrow estimate; it is not a universal no-go for a new signed
rulingwise theorem.

## 7. State boundary

The exact power ledger is

| object | certified positive capacity | target |
|---|---:|---:|
| complete double-far block | \(L^4X^\varepsilon\) | \(L^3X^\varepsilon\) |
| \(p=0\), \(q=0\), and fixed-width \(y-x\) slices | \(L^3X^\varepsilon\) | \(L^3X^\varepsilon\) |
| endpoint-swap \((++)\) complement | \(L^4X^\varepsilon\) | \(L^3X^\varepsilon\) |
| unweighted one-step faces | \(L^3X^\varepsilon\) | \(L^3X^\varepsilon\) |
| faces after the forced \(q\)-ramp | \(L^4X^\varepsilon\) | \(L^3X^\varepsilon\) |
| coefficient-blind mixed bulk after triangle | \(L^5X^\varepsilon\) | \(L^3X^\varepsilon\) |

The last line is an upper-capacity diagnosis, not physical mass.  The first
unproved statement remains (171.K3).  A successful continuation needs a
new signed, nonlocal \(q\)-primitive/correlation theorem for the complete
actual gcd, slanted-symbol, alias, character, gate, and endpoint scalar, or
another mechanism outside the audited operator class.

The kernel licenses one proved-internal, route-scoped obstruction node.  It
does not change the status of the oscillatory remainder or the equivalent
actual energy.  The separate remaining-label owner, full BAL, hard TOP,
UNBAL, direct M1, GAR, endpoint assembly, M9, both bridges, the internal
\(1/3\) exponent, the repaired external \(0.3144831759740614\ldots\)
benchmark, and the \(1/4\) target all remain unchanged.

## 8. Dependencies and evidence

Accepted dependencies:

- `M9-M2-balanced-smooth-literal-atom-dictionary`;
- `M9-M2-character-factor`;
- `M9-M2-balanced-full-product-double-corridor-reduction`;
- `M9-M2-balanced-double-far-phase-free-mode-reduction`;
- `M9-M2-balanced-divisor-progressive-alias-reduction`; and
- `M9-M2-balanced-broad-narrow-gauge-ruling-obstruction`.

Round-171 evidence consists of the literal discovery report, the
statement-only blind rederivation, the hostile capacity/boundary audit, the
post-unmask real-symmetry review, the independent ramp/power review, the
literal-restoration owner-scope review, the final kernel verification, the
post-repair verification, and the conductor adjudication.  No numerical
experiment or external theorem is used.
