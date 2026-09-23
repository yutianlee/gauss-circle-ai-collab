# Hard-M1 \(t=1\), \(P_2\): on-shell carrier normalization self-return

- Round: 196
- Campaign:
  m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate
- Starting graph SHA-256:
  f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2
- Formal candidate SHA-256:
  5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380
- Status: verified route-scoped no-go; not a target-safe estimate
- Numerical theorem evidence: none

## K196.1. Statement

Fix \(X\ge2\), \(B>0\), \(\varepsilon>0\), one nonempty literal
middle or lower residual shell \(L\ge2\), one surviving frequency sign
\(\sigma\in\{+1,-1\}\), one nonempty dyadic block \(Y<h\le2Y\),
and one inherited nonempty power-of-two projective band \(J\).
Choose a fresh \(0<\eta<\varepsilon\) for the outer ledger and put
\[
 H_B=\lfloor(\log(2X))^B\rfloor,\qquad
 Q=H_B,\qquad R_0=\lceil L\rceil,\qquad
 D_L=\lceil\sqrt L\rceil,\qquad M=\min(Y,D_L).
\tag{K196.0}
\]
Retain the exact accepted Round-192 hard-M1 original-\(t=1\) core and
the Round-195 physical mask
\[
 P_2=\mathbf 1_{\{|d-gm|\le D_L\}}
     \mathbf 1_{\{|d'-gm'|>D_L\}},
\tag{K196.1}
\]
imposed on the physical source before Fourier expansion and height
differencing.  Put
\[
 Q=H_B,\qquad M=\min(Y,D_L),
\tag{K196.2}
\]
and retain exactly the open packet region
\[
 \kappa<D_L,\qquad M>Q\mathfrak m\kappa.
\tag{K196.3}
\]

For one exact-conductor mode, retain
\[
\begin{gathered}
 U=\mathfrak m q>4Q,\qquad k=\mathfrak m a,\qquad
 q>Q,\qquad \mathfrak m|a|_q>Q,\qquad Q\mathfrak m<Y,\\
 (a,q)=1,\qquad U\mid u,\qquad g=u/U,\qquad
 (u,v)=1,\qquad (U,h)=1,
\end{gathered}
\tag{K196.4}
\]
with the inherited oddness of \(\kappa,g,U\), and
\[
 j_q(a,v):=|a\bar v_q|_q>
 T_Q(\mathfrak m,q;Y):=
 \min\!\left\{\frac{q-1}{2},
  \left\lfloor\frac{Q\mathfrak m q}{Y}\right\rfloor\right\},
 \qquad J\le j_q(a,v)<2J.
\tag{K196.5}
\]

Let
\[
 v_0=[v]_U\in\{1,\ldots,U-1\},\qquad
 v=v_0+nU,\qquad n\in\mathbb Z,
\tag{K196.6}
\]
and normalize the signed inverse and literal transport quotient by
\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},\qquad
 \rho v-\gamma U=1,\qquad \gamma=\beta+n\rho.
\tag{K196.7}
\]
The Round-192 Farey selector uses \(\beta\), whereas the Round-191
literal transport uses \(\gamma\).  With
\[
 T=\min\!\left\{\frac{U-1}{2},
  \left\lfloor\frac{Q\mathfrak m U}{Y}\right\rfloor\right\},
\tag{K196.8}
\]
the \(T=0\) branch retains the complete inherited \(|\rho|>0\)
remainder.  For \(T\ge1\), every retained row satisfies
\[
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A),
 \qquad |\rho|\ge(A+1)(T+1).
\tag{K196.9}
\]
Here \(A\) and the finite Farey family \(\mathcal F_A\) have exactly
their accepted Round-192 definitions.

In either primitive orientation,
\[
 S=S_{0,\omega}(h)+Ut,\qquad
 0\le S_{0,\omega}(h)<U,\qquad
 S_{0,\omega}(h)\equiv\epsilon_\omega\bar v_Uh\pmod U,
 \qquad \epsilon_+=1,\quad\epsilon_-=-1.
\tag{K196.10}
\]
Both primitive orientations, both surviving frequency signs, the
complete anchor aggregate, every literal endpoint label and
conjugation, and all four \(++,+-,-+,--\) cross-row blocks remain in
one complex aggregate before its final real part.  No \(T\)-branch,
unit-inverse, wrap, parity, mask, or orientation submask may replace the
complete core unless its exact complement is proved empty or estimated.

The literal exact-conductor atom is
\[
 \boxed{\;
 \mathfrak m^{-1}c_q(a)(-1)^t
 e(\epsilon_\omega a\bar v_qh/q)B_{\omega,\sigma}(h,t),\qquad
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
 \;}
\tag{K196.11}
\]

Then the proposed on-shell primitive-carrier argument does not prove the
fixed target
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll Q\mathfrak m\kappa uX^\varepsilon
\tag{K196.12}
\]
or any new target-safe strict sector.  Its primitive modulus-\(4q\)
phase is a parity-restored shadow, not the literal atom (K196.11).
Restoring the exact normalization either retains the singular
near-half conductor mass on every live-to-live step or creates a bulk
parity commutator.  The only formal wrap carrying the shadow multiplier
\(z_{q,a}\) is a live/dead zero-extension event and supplies no paired
denominator cancellation.  No accepted event operator
supplies a common step-two difference on the complete two-orientation
core.

This is an exact normalization/support no-go for that mechanism.  It is
not a literal lower bound and does not refute a different
coefficient-sensitive joint estimate for the complete \(P_2\)
remainder.

## K196.2. Formal primitive shadow

In the plus chart,
\[
 2h=v\eta_+ +U\delta_+-\kappa(U^2-v^2),\qquad
 x=\kappa v+\eta_+=\kappa U+2S=d'/g.
\tag{K196.13}
\]
In the minus chart,
\[
 2h=U\eta_- -v\delta_-+\kappa(U^2-v^2),\qquad
 x=\kappa v+\delta_-=\kappa U+2S=d/g.
\tag{K196.14}
\]
Reduction modulo \(q\mid U\) gives, in both orientations,
\[
 \epsilon_\omega\bar v_qh\equiv\bar 2_qx\pmod q.
\tag{K196.15}
\]
Because \(\kappa U\) and \(x\) are odd,
\[
 (-1)^S=\chi_4(\kappa U)\chi_4(x).
\tag{K196.16}
\]
Thus the physical-parity shadow obeys
\[
 (-1)^S e(\epsilon_\omega a\bar v_qh/q)
 =\chi_4(\kappa U)\chi_4(x)e(a\bar2_qx/q).
\tag{K196.17}
\]

For odd \(x\), its variable factor is, up to a constant,
\[
 e(b_{q,a}x/(4q)),\qquad
 b_{q,a}\equiv q+4a\bar2_q\pmod{4q}.
\tag{K196.18}
\]
The numerator is odd and is congruent to \(2a\) modulo every prime
dividing \(q\), so \((b_{q,a},4q)=1\).  Under \(x\mapsto x+2\), the
formal multiplier is
\[
 z_{q,a}=-e(a/q),\qquad
 (1-z_{q,a})c_q(a)=\frac{2e(a/q)}q.
\tag{K196.19}
\]
Equations (K196.17)--(K196.19) are exact algebra, but only for the
parity-restored shadow.

## K196.3. Literal normalization and conductor mixing

The accepted affine parity is
\[
 (-1)^S=E_U(S_{0,\omega})(-1)^t,\qquad
 E_U(s)=(-1)^s.
\tag{K196.20}
\]
Round 187 Fourier-expands \(E_U(S_0)\), not \((-1)^t\):
\[
 E_U(S_0)=\sum_{r\bmod U}c_U(r)e(rS_0/U),\qquad
 c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a).
\tag{K196.21}
\]
Consequently (K196.11), not the left side of (K196.17), is the literal
fixed-mode atom.  Its exact on-shell factorization is
\[
 \boxed{\;
 (-1)^t e(\epsilon_\omega a\bar v_qh/q)
 =E_U(S_{0,\omega})\chi_4(\kappa U)\chi_4(x)
  e(a\bar2_qx/q).
 \;}
\tag{K196.22}
\]

The missing factor is not constant.  Keeping the outside fixed-mode
coefficient,
\[
\begin{aligned}
 &\mathfrak m^{-1}c_q(a)E_U(S_0)e(kS_0/U)\\
 &\qquad=\mathfrak m^{-1}c_q(a)
   \sum_{r\bmod U}c_U(r)e((r+k)S_0/U).
\end{aligned}
\tag{K196.23}
\]
This is a convolution, not the original exact-conductor decomposition
at shifted frequency.  It mixes exact conductors, reduced numerators,
projective bands, and safe/core packets.  Full recombination restores
the pre-conductor physical parity and removes the distinguished
\(c_q(a)\).  Therefore (K196.19) cannot be attached to one literal atom
inside the frozen packet.

## K196.4. Live multiplier, wrap boundary, and parity commutator

Under \(S\mapsto S+1\), put
\[
 c_{\rm wr}(S_0)=\mathbf1_{\{S_0=U-1\}}.
\]
The literal phase ratio is
\[
 (-1)^{c_{\rm wr}(S_0)}e(a/q).
\tag{K196.24}
\]
On live support, (K196.4) and (K196.10) imply
\((S_0,U)=1\), hence \(S_0\ne0\).  Every live-to-live adjacent step is
therefore nonwrap and has ratio \(e(a/q)\), not \(-e(a/q)\).
The forward wrap lands at \(S_0=0\), equivalently \(U\mid h\), so
there is no live-to-live denominator-cancelling pair.  After zero
extension the live/dead transition survives as an unpaired
coprimality-boundary atom with the original coefficient.

For the primitive near-half mode \(a=(q-1)/2\),
\[
 |(1-e(a/q))c_q(a)|
 =\frac2q\cot\!\left(\frac{\pi}{2q}\right)\asymp1,
\tag{K196.25}
\]
not \(O(q^{-1})\).  This is a coefficient-level method falsifier, not
proof that any particular literal endpoint product is nonzero.

Equivalently, define
\[
 \Delta_2B(x)=B(x)-B(x-2),\qquad
 B^-=B(x-2),\qquad E_U^-=E_U(S_0(x-2)).
\]
Then
\[
 \Delta_2(E_UB)
 =E_U\Delta_2B+(E_U-E_U^-)B^-,
\tag{K196.26}
\]
or
\[
 E_U\Delta_2B
 =\Delta_2(E_UB)-(E_U-E_U^-)B^-.
\tag{K196.27}
\]
On every live-to-live nonwrap edge,
\(|E_U-E_U^-|=2\).  At the coprimality wrap, the boundary atom replaces
the paired commutator rather than disappearing.  Thus restoring the
literal parity returns the exact-conductor coefficient to full
available event capacity before the remaining physical commutators are
estimated.

## K196.5. No common literal step-two event

The genuine Round-191 height event transports
\[
 (S,w)\mapsto
 (S-\epsilon_\omega\rho,\,
  w-\epsilon_\omega\gamma).
\tag{K196.28}
\]
Therefore
\[
 x_{h-1}^{\rm tr}=x_h-2\epsilon_\omega\rho,\qquad
 x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\rho.
\tag{K196.29}
\]
For \(T\ge1\), (K196.9) forces \(|\rho|>1\).  At \(T=0\),
\(\rho=\pm1\) is not excluded, but the unit-inverse selector cannot
replace the complete branch unless its literal complement is proved
empty or estimated.  Even on those rows all physical commutators
remain.  At fixed height, \(t\mapsto t+1\) moves \(x\) by \(2U\).
Moreover, \(x=d'/g\) is the plus far coordinate, while \(x=d/g\) is
the minus close coordinate; the literal minus far step leaves \(x\)
fixed.  Hence no accepted operator supplies a common \(\Delta_2\) on
the complete two-orientation aggregate.

For clarity, the genuine physical-mask event obeys
\[
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
  +\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\tag{K196.30}
\]
The already safe terminal and isolated unit-height Fejer projections
do not remove the two coprimality flips, transported affine
births/deaths, carry, ordered endpoint arithmetic, cell/crossing,
square-root phase, and outer and endpoint zero extensions.

An artificial adjacent-\(S\) predecessor
\[
 \tau:(S,w)\mapsto(S-1,w),\qquad
 A_0=\kappa gU,\quad C_v=\kappa v,
\tag{K196.31}
\]
has ordered endpoint pairs
\[
\begin{array}{c|cc}
 &(N_{0,\omega},d_{0,\omega})&(N_{1,\omega},d_{1,\omega})\\ \hline
 +&(A_0(C_v+2w),A_0)&((A_0+2gS)C_v,A_0+2gS)\\
 -&((A_0+2gS)C_v,A_0+2gS)&(A_0(C_v+2w),A_0).
\end{array}
\tag{K196.32}
\]
The variable endpoint displacement and height shifts are
\[
 (\Delta N,\Delta d)=(2gC_v,2g),\qquad
 h_+-h_+\circ\tau=v,\qquad h_--h_-\circ\tau=-v.
\tag{K196.33}
\]
Thus the artificial step acts on the plus upper endpoint and the
conjugated minus lower endpoint.  The plus-far or minus-close \(P_2\)
boundary, variable divisor, arithmetic masks, carry, affine range,
endpoint product, square-root phase, cells, crossings, and both zero
extensions can flip and contribute their exact product-rule terms.
For \(F(h)=1-2\kappa gh/R_0\),
\[
 |F(h)-F(h\circ\tau)|=\frac{2\kappa gv}{R_0},
\tag{K196.34}
\]
not the already removed unit-height Fejer difference
\(2\kappa g/R_0\).  If the two artificial sites do not overlap, the
event is an outer birth or death, not a common-site Fejer commutator.
None of these terms has an accepted estimate below the Round-195
positive capacity.

Consecutive-support completion, a cumulative primitive, unsigned or
character-erased shadows, mask or \(T\)-deletion, wrap-only
restriction, arbitrary or phase-conjugated arrays, and separate
orientation norms are method controls only.  They are not claimant
operators and establish no literal lower mass.

## K196.6. Power and proof-state boundary

The unchanged fixed-packet estimate is
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+M\}X^\varepsilon.
\tag{K196.35}
\]
On (K196.3), the unresolved term has exact deficit
\[
 \frac{Mu}{Q\mathfrak m\kappa u}
 =\frac{M}{Q\mathfrak m\kappa}>1.
\tag{K196.36}
\]
The identities
\[
 c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),\qquad
 \sum_{\mathfrak m q\mid u}1\le\tau_3(u)
\tag{K196.37}
\]
produce the accepted outer ledger
\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log^{O(1)}(2u)
 \ll L^2X^\varepsilon
\tag{K196.38}
\]
only after the fixed target (K196.12) is proved.  The lift then cancels
the \(\mathfrak m\) in that proved target; it does not cancel
(K196.36).  No positive power of \(M,Y,D_L,q,U\), or \(L\) is hidden
in \(X^\varepsilon\).

Accordingly this kernel records only
on_shell_carrier_denominator_self_return_no_go.  It proves no new
target-safe sector and does not promote complete \(P_2\), \(P_1\),
complete original \(t=1\), any other original-\(t\) incidence, the hard
small-\(t\) owner, smooth M1, GAR, any M2 parent, endpoint uniformity,
M9, either bridge, the quarter theorem, or any exponent.  The first
open theorem remains a coefficient-sensitive joint
\(++,+-,-+,--\) cross-row estimate for the complete literal region
(K196.3), before positive norms and with every literal field retained.

## K196.7. Review provenance

The kernel formalizes the Round-196 candidate after:

1. independent normalization/live-wrap review and post-repair
   verification;
2. independent commutator/power/owner review, post-repair audit, and
   final canonical-coordinate verification;
3. blind derivation and post-unmask review; and
4. conductor reconciliation of all three independent reports.

The reviews verified the literal \(\mathfrak m^{-1}c_q(a)(-1)^t\)
normalization, the \(\beta/\gamma\) interface, live/dead wrap boundary,
\(T=0\) unit-inverse exception, two-orientation event geometry, power
ledger, capacity-only status, owner boundary, and exponent quarantine.
