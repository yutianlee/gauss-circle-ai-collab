# Formal candidate: hard-M1 (t=1) (P_2) on-shell carrier self-return

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Round: 196
- Starting graph:
  `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Status: seam repairs applied; pending independent post-repair verification
- Numerical theorem evidence: none

## 1. Exact statement

Fix \(X\ge2\), one nonempty literal middle or lower residual hard-M1
shell \(L\ge2\), a frequency sign \(\sigma\in\{+1,-1\}\), and
\[
 Q=H_B,\qquad R_0=\lceil L\rceil,\qquad
 D_L=\lceil\sqrt L\rceil,\qquad M=\min(Y,D_L).
\]
Retain the exact accepted Round-192 hard-M1 original-\(t=1\) core.  The
physical mask is imposed on the source before Fourier expansion and
before height differencing:

\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}},
\tag{196.K1}
\]

and only the still-open Round-195 packets

\[
 \kappa<D_L,
 \qquad M>Q\mathfrak m\kappa.
\tag{196.K2}
\]

Fix one exact-conductor mode

\[
 U=\mathfrak m q,\qquad k=\mathfrak m a,\qquad
 U>4Q,\qquad q>Q,\qquad \mathfrak m|a|_q>Q,
 \qquad Q\mathfrak m<Y,\qquad
 J\le j_q(a,v)<2J,
\tag{196.K3}
\]

where \((a,q)=1\), \(U\mid u\), \(g=u/U\), \((u,v)=1\),
\((U,h)=1\), and \(\kappa,g,U\) are odd.  In particular
\((U,v)=1\), so every inverse displayed below exists.  Here
\[
 j_q(a,v):=|a\bar v_q|_q>
 T_Q(\mathfrak m,q;Y):=
 \min\!\left\{\frac{q-1}{2},
  \left\lfloor\frac{Q\mathfrak m q}{Y}\right\rfloor\right\}.
\tag{196.K3a}
\]
In either
primitive orientation write

\[
 S=S_{0,\omega}(h)+Ut,\qquad
 0\le S_{0,\omega}(h)<U,\qquad
 S_{0,\omega}(h)\equiv\epsilon_\omega\bar v_Uh\pmod U,
\tag{196.K4}
\]

Put
\[
 v_0=[v]_U\in\{1,\ldots,U-1\},\qquad v=v_0+nU,
\tag{196.K4a}
\]
and choose the uniquely normalized signed inverse and literal transport
quotient by
\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},\qquad
 \rho v-\gamma U=1,\qquad \gamma=\beta+n\rho.
\tag{196.K4b}
\]
Retain the exact Round-192 branch convention
\[
 T=\min\!\left\{\frac{U-1}{2},
  \left\lfloor\frac{Q\mathfrak m U}{Y}\right\rfloor\right\}.
\tag{196.K4c}
\]
For \(T=0\), the Farey projector is zero and the complete inherited
\(\rho\)-large remainder \(|\rho|>0\) remains.  For \(T\ge1\), every
retained row satisfies simultaneously
\[
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A),
 \qquad |\rho|\ge(A+1)(T+1),
\tag{196.K4d}
\]
with the accepted definitions of \(A\) and \(\mathcal F_A\).
Both primitive orientations, both surviving frequency signs, the full
anchor aggregate, every literal endpoint label and conjugation, and all
four \(++,+-,-+,--\) cross-row blocks remain inside one complex
aggregate before its final real part.  No \(T\)-branch or unit-inverse,
wrap, parity, mask, or orientation submask may be promoted without an
estimate for its exact complement.

Here \(\epsilon_+=1\) and \(\epsilon_-=-1\). The literal
exact-conductor atom is

\[
 \boxed{
 \mathfrak m^{-1}c_q(a)(-1)^t
 e(\epsilon_\omega a\bar v_qh/q)B_\omega(h,t),}
 \qquad
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\tag{196.K5}
\]

Put (x=\kappa U+2S). Then:

1. the determinant congruence and parity identity give a formal primitive
   modulus-(4q) shadow

   \[
   (-1)^S e(\epsilon_\omega a\bar v_qh/q)
   =\chi_4(\kappa U)\chi_4(x)e(a\bar2_qx/q),
   \tag{196.K6}
   \]

   with step-two multiplier (z_{q,a}=-e(a/q)) and

   \[
   (1-z_{q,a})c_q(a)=2e(a/q)/q;
   \tag{196.K7}
   \]

2. the literal atom instead has the exact on-shell factorization

   \[
   \boxed{
   (-1)^t e(\epsilon_\omega a\bar v_qh/q)
   =E_U(S_{0,\omega})\chi_4(\kappa U)\chi_4(x)
    e(a\bar2_qx/q),}
   \qquad E_U(s)=(-1)^s;
   \tag{196.K8}
   \]

3. on every live-to-live adjacent-\(x\) step the literal multiplier is
   \(e(a/q)\), not \(z_{q,a}\); the only wrap carrying \(z_{q,a}\)
   lands at \(S_0=0\), so there is no live-to-live
   denominator-cancelling wrap, while the resulting live/dead
   coprimality flip remains as a zero-extension boundary atom with the
   original coefficient;
4. moving \(E_U\) through a hypothetical step-two difference creates a
   commutator of modulus \(2\) on every live-to-live nonwrap edge, while
   live/dead edges remain zero-extension boundary atoms;
5. the accepted event obeys the exact displacement
   \(x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\rho_U(v)\).  For \(T\ge1\)
   its magnitude is not \(2\); for \(T=0\), unit-inverse rows may have
   magnitude \(2\), but the unit-inverse selector cannot replace the
   complete branch unless its literal complement is proved empty or
   estimated.  No
   accepted literal common-\(\Delta_2\) operator exists on the complete
   two-orientation core; and
6. the carrier route therefore leaves the fixed-packet estimate at

   \[
   |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
   \ll u\{\kappa+M\}X^\varepsilon,
   \tag{196.K9}
   \]

   with the exact unresolved multiplier
   (M/(Q\mathfrak m\kappa)>1).

This is a route-scoped normalization/support self-return. It is not a
literal lower bound and does not disprove a different coefficient-sensitive
joint estimate for the complete (P_2) remainder.

## 2. Determinant and primitive-shadow algebra

In the plus chart

\[
 2h=v\eta_+ +U\delta_+-\kappa(U^2-v^2),
 \qquad x=\kappa v+\eta_+=\kappa U+2S=d'/g,
\tag{196.K10}
\]

while in the minus chart

\[
 2h=U\eta_- -v\delta_-+\kappa(U^2-v^2),
 \qquad x=\kappa v+\delta_-=\kappa U+2S=d/g.
\tag{196.K11}
\]

Reduction modulo (q\mid U) gives

\[
 \bar v_qh\equiv\bar2_qx\pmod q\quad(+),
 \qquad
 -\bar v_qh\equiv\bar2_qx\pmod q\quad(-).
\tag{196.K12}
\]

Because (x) and (kappa U) are odd,
((-1)^S=\chi_4(\kappa U)\chi_4(x)), proving (196.K6). For odd (x),
(chi_4(x)=-i e(x/4)). Thus the variable factor in (196.K6) is a
constant times

\[
 e(b_{q,a}x/(4q)),
 \qquad b_{q,a}\equiv q+4a\bar2_q\pmod{4q}.
\]

The numerator is odd and is congruent to (2a) modulo every prime
dividing (q), so ((b_{q,a},4q)=1). Its (x\mapsto x+2) ratio is
(-e(a/q)), and (196.K7) follows directly from the definition of
(c_q(a)).

## 3. Literal normalization and conductor mixing

The accepted Round-185 parity is

\[
 (-1)^S=E_U(S_{0,\omega})(-1)^t.
\tag{196.K13}
\]

Round 187 expands exactly

\[
 E_U(S_0)=\sum_{k\bmod U}c_U(k)e(kS_0/U),
 \qquad
 c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a),
\tag{196.K14}
\]

leaving ((-1)^t) in the affine sum. This proves (196.K5). Since
(S\equiv S_0\pmod U) and (q\mid U), the anchor exponential equals
(e(a\bar2_qx/q)). Combining this with (196.K13) proves (196.K8).

The extra \(E_U(S_0)\) is not constant. Multiplying one retained mode,
including its outside exact-conductor coefficient, by it gives

\[
 \mathfrak m^{-1}c_q(a)E_U(S_0)e(kS_0/U)
 =\mathfrak m^{-1}c_q(a)
  \sum_{r\bmod U}c_U(r)e((r+k)S_0/U),
\tag{196.K15}
\]

which mixes all \(U\)-frequencies and their exact conductors,
projective bands, and safe/core status.  The displayed convolution
coefficients are not the original exact-conductor packet weights at the
shifted frequencies.  Full recombination recovers physical parity and
removes the distinguished \(c_q(a)\). Consequently
(196.K6)--(196.K7) cannot be attached to (196.K5) inside the frozen
packet.

## 4. Live multiplier and parity commutator

Under (S\mapsto S+1), set

\[
 c(S_0)=\mathbf1_{\{S_0=U-1\}}.
\]

Then (S_0'=[S_0+1]_U), (t'=t+c(S_0)), and the literal phase ratio is

\[
 (-1)^{c(S_0)}e(a/q).
\tag{196.K16}
\]

On live support \(S_0\equiv\epsilon_\omega\bar v_Uh\) is a unit modulo
\(U\). If a step wraps, its new residue is \(0\), so the new height is
divisible by \(U\) and the endpoint is dead under the coprimality mask.
Hence every live-to-live step is nonwrap and has ratio \(e(a/q)\).
The live-to-dead and dead-to-live transitions are not discarded: after
zero extension they remain boundary atoms with the original coefficient
and provide no paired denominator cancellation.

For (a=(q-1)/2), which is a unit for every odd (q),

\[
 |(1-e(a/q))c_q(a)|
 =\frac2q\cot\!\left(\frac{\pi}{2q}\right)\asymp1.
\tag{196.K17}
\]

Thus the literal difference does not flatten the near-half coefficient to
(O(1/q)).

If instead \(E_U\) is absorbed into the amplitude, define

\[
 \Delta_2B(x)=B(x)-B(x-2),\qquad
 B^-=B(x-2),\qquad E_U^-=E_U(S_0(x-2)).
\]

Zero-extended step-two differencing gives

\[
 \Delta_2(E_UB)
 =E_U\Delta_2B+(E_U-E_U^-)B^-.
\tag{196.K18}
\]

Equivalently,

\[
 E_U\Delta_2B
 =\Delta_2(E_UB)-(E_U-E_U^-)B^-.
\tag{196.K18a}
\]

On every possible live-to-live adjacent edge
\(|E_U-E_U^-|=2\). The second term retains the singular exact-conductor
coefficient and the full available atom capacity.  At a coprimality
wrap, it is replaced by the zero-extension boundary atom described
above, not dropped.  This is the exact parity-kernel commutator
self-return.

## 5. Absence of a literal common step-two event

The accepted Round-191 persistent event compares height \(h\) to height
\(h-1\) by

\[
 (S,w)\mapsto
 (S-\epsilon_\omega\rho_U(v),
  w-\epsilon_\omega\gamma_U(v)),
 \qquad \rho_U(v)v-\gamma_U(v)U=1.
\tag{196.K19}
\]

The exact directional law is
\[
 x_{h-1}^{\rm tr}=x_h-2\epsilon_\omega\rho_U(v),
 \qquad x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\rho_U(v).
\tag{196.K19a}
\]
For \(T\ge1\), the simultaneous Farey conditions force
\(|\rho_U(v)|>1\), so this is not a step-two event.  At \(T=0\),
\(\rho_U(v)=\pm1\) is not excluded; the unit-inverse selector cannot
replace the complete inherited remainder unless its literal complement
is proved empty or estimated, and it retains all literal commutators
below.  A fixed-height affine step \(t\mapsto t+1\) moves
\(x\) by \(2U\).

On a genuine persistent K191 event the physical product rule is
\[
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
  +\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\tag{196.K19b}
\]
The terminal \(K\)-event and isolated unit-height Fejer projection have
already been removed safely.  The two coprimality flips, transported
affine births/deaths, carry, ordered endpoint arithmetic,
cell/crossing, square-root phase, and outer and endpoint zero extensions
remain.  This genuine event is not an adjacent-\(S\) operator.

Moreover, in the plus chart \(x=d'/g\) is the far coordinate, whereas in
the minus chart \(x=d/g\) is the retained close coordinate; the literal
minus far step \(w\mapsto w+1\) leaves \(x\) fixed. Therefore no
accepted common reindexing produces a genuine literal \(\Delta_2\) on
the complete two-orientation aggregate.

For the labelwise-minimal artificial adjacent-\(S\) predecessor
\[
 \tau:(S,w)\mapsto(S-1,w),\qquad
 A_0=\kappa gU,\qquad C_v=\kappa v,
\tag{196.K19c}
\]
the ordered endpoint pairs are
\[
\begin{array}{c|cc}
 &(N_{0,\omega},d_{0,\omega})&(N_{1,\omega},d_{1,\omega})\\ \hline
 +&(A_0(C_v+2w),A_0)&((A_0+2gS)C_v,A_0+2gS)\\
 -&((A_0+2gS)C_v,A_0+2gS)&(A_0(C_v+2w),A_0).
\end{array}
\tag{196.K19d}
\]
Thus the predecessor-to-current displacement of the variable endpoint
is
\[
 (\Delta N,\Delta d)=(2gC_v,2g),
 \qquad
 h_+-h_+\circ\tau=v,\quad h_--h_-\circ\tau=-v.
\tag{196.K19e}
\]
It acts on the plus upper factor and the conjugated minus lower factor.
Consequently the plus far or minus close \(P_2\) boundary, the variable
divisor, squarefree/divisibility/allocation-coprimality and residual
masks, canonical carry, affine range, endpoint product, square-root
phase, cell, crossing, and either zero extension can change and
therefore produces its corresponding product-rule commutator.  With
\(F(h)=1-2\kappa gh/R_0\), the raw artificial Fejer displacement is
\[
 |F(h)-F(h\circ\tau)|=\frac{2\kappa gv}{R_0},
\tag{196.K19f}
\]
not the already removed unit-height difference \(2\kappa g/R_0\).
Nonoverlap is an outer birth/death rather than a common-site Fejer
commutator.  Each surviving product-rule term has no accepted estimate
below positive event capacity.

Replacing the divisor-supported sequence by consecutive support or a
cumulative primitive is not a theorem for the literal operator.
Unsigned, character-erased, mask-deleted, \(T\)-deleted, wrap-only,
arbitrary-array, phase-conjugated, and separately normed orientation
shadows are method controls only.  None is claimant evidence without
the exact literal complement, and capacity attainment is not literal
lower mass.

## 6. Power and scope boundary

Equation (196.K9) is the accepted Round-195 positive estimate. On
(196.K2), its \(Mu\) term has deficit

\[
 \frac{Mu}{Q\mathfrak m\kappa u}
 =\frac{M}{Q\mathfrak m\kappa}>1.
\tag{196.K20}
\]

The exact lift and coefficient mass are
\[
 c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a),
 \qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),
\tag{196.K20a}
\]
and the divisor ledger uses
\(\sum_{\mathfrak m q\mid u}1\le\tau_3(u)\).
Together with the projective bands, divisor choices, dyadic heights, and
shell sum, they would give

\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll L^2X^\varepsilon
\tag{196.K21}
\]

only after the fixed \(Q\mathfrak m\kappa uX^\varepsilon\) target is
established.  The spectral lift then cancels the \(\mathfrak m\) in
that proved target; it does not remove (196.K20). No positive power of
\(M,Y,D_L,q,U\), or \(L\) is hidden in \(X^\varepsilon\).

The parity commutator's positive capacity is a method control, not a
literal lower bound. The complete (P_2) target remains logically open to
a new coefficient-sensitive (++,+-,-+,--) cross-row theorem using the
actual endpoint and phase vectors.

## 7. Proof-state recommendation

Record this candidate only as an exact normalization/support no-go for the
proposed carrier-denominator mechanism. Add it as inconclusive evidence to
the already open hard-M1 small-(t) owner and record the rejected
operator-identification, fixed-multiplier, live-wrap, common-(Delta_2),
and exponent overclaims.

Do not create a target-safe obligation. Do not promote complete (P_2),
(P_1), complete original (t=1), another original-(t) incidence, the
hard small-(t) owner, smooth M1, GAR, any M2 parent, endpoint uniformity,
M9, either bridge, the quarter theorem, or any exponent.
