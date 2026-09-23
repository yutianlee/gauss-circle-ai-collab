# Formalized candidate: hard-M1 \(t=1\) fast signed-inverse transport reduction

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Round: 191
- Starting graph SHA-256:
  `306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa`
- Candidate status: repaired; pending independent post-repair replay
- Numerical theorem evidence: none

## Candidate statement

Fix real \(X\ge2\), a nonempty literal middle or lower residual hard-M1
shell \(L\ge2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\), and

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor.
\tag{191.C1}
\]

All arithmetic labels \(\kappa,g,u,v,m,q,h\) below are positive
integers, and \(1\le a<q\) with \((a,q)=1\).

On a nonempty dyadic block \(Y<h\le2Y\), with \(Y>Q\), retain the exact accepted
Round-189 fast packet

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y,
 \qquad(a,q)=1,
\tag{191.C2}
\]

\[
 U\mid u,\quad g=u/U,\quad \kappa,g,U\text{ odd},\quad
 (u,v)=1,\quad (U,h)=1,
\quad 0<2\kappa gh<R_0:=\lceil L\rceil,
\tag{191.C3}
\]

Also, on nonzero inherited support,

\[
 u\asymp v\asymp \frac{L}{\kappa},\qquad
 \operatorname{length}(\mathcal V_{\rm lit})\ll u,
 \qquad L\ll X^{1/4}.
\tag{191.C3a}
\]

Here the length assertion means the total length of the inherited
literal \(v\)-intervals; every further literal field only deletes rows.
Finally, retain

\[
 j_q(a,v)=|a\bar v_q|_q>
 T_Q:=\min\left\{\frac{q-1}{2},
                  \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\}.
\tag{191.C4}
\]

If \(T_Q=(q-1)/2\), (191.C4) is impossible and the inherited fast
packet is empty; all conclusions below are then vacuous.  Otherwise,
the positive values of \(j_q(a,v)\) are partitioned exactly by powers of
two \(J=2^r\) through the disjoint conditions
\(J\le j_q(a,v)<2J\); the last nonempty band truncates automatically at
\((q-1)/2\).

Every inherited selector, squarefree and allocation-coprimality
deletion, residual selector, profile, floor, star, half-weight, hard
sample, crossing, endpoint trace, Fejer factor, square-root phase,
affine site, orientation, terminal block, and zero extension remains
literal.  Both orientations and all literal labels remain inside one
complex aggregate before the final real part.

For each unit \(v\bmod U\), let \(\varrho_U(v)\) be its signed least
inverse and let \(\gamma_U(v)\in\mathbb Z\) satisfy

\[
 \varrho_U(v)v-\gamma_U(v)U=1,
 \qquad -\frac{U-1}{2}\le\varrho_U(v)\le\frac{U-1}{2}.
\tag{191.C5}
\]

Put

\[
 T_\varrho(U,m;Y)=
 \min\left\{\frac{U-1}{2},
             \left\lfloor\frac{QmU}{Y}\right\rfloor\right\}.
\tag{191.C6}
\]

Then the complete fast sector

\[
 0<|\varrho_U(v)|\le T_\varrho(U,m;Y)
\tag{191.C7}
\]

is absolutely target-safe.  More precisely, on every fast dyadic band
\(J\le j_q(a,v)<2J\), its fixed
\((\kappa,u,m,q,a,J,\sigma)\) complex packet, jointly summed over both
orientations and every literal \(v,h,t\), is

\[
 \boxed{|\mathscr J_{{\rm inv},{\rm fix}}|
 \ll_\varepsilon Qm\kappa uX^\varepsilon.}
\tag{191.C8}
\]

The exact outer height/carrier-interval terminal projection and the
isolated Fejer-difference projection on the complementary rows
\(|\varrho_U(v)|>T_\varrho\) are also target-safe.  At the same fixed
packet level, define all three complex projections before a modulus and
denote their sum by \(\mathscr J_{\rm fix}^{\rm safe}\).  Then

\[
 \boxed{|\mathscr J_{\rm fix}^{\rm safe}|
 \ll_\varepsilon Qm\kappa uX^\varepsilon.}
\tag{191.C9}
\]

After the exact lift \(c_{mq}(ma)=m^{-1}c_q(a)\), the coefficient mass,
dyadic bands, and divisor ledger, let
\(\mathscr J_{Y,Q}^{\rm safe,\sigma}\) denote the resulting full complex
safe aggregate.  Its total contribution is

\[
 \boxed{|\mathscr J_{Y,Q}^{\rm safe,\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{191.C10}
\]

There is an exact decomposition, before the final real part,

\[
 \boxed{\mathscr F_{Y,Q}^{\sigma}
       =\mathscr J_{Y,Q}^{\rm safe,\sigma}
        +\mathscr R_{Y,Q}^{\sigma}.}
\tag{191.C11}
\]

The remainder retains only \(|\varrho_U(v)|>T_\varrho\), and contains
the outer coprimality flips, transported affine births and deaths,
canonical-anchor carries, endpoint arithmetic-mask changes, literal
cell and crossing changes, common-cell endpoint-coefficient changes,
and square-root-phase changes, with their original signs and both
orientations under one outer real part.  Its required estimate

\[
 \boxed{\Re\mathscr R_{Y,Q}^{\sigma}
       \ll_{B,\varepsilon}L^2X^\varepsilon}
\tag{191.C12}
\]

remains open.  At fixed \((\kappa,u,m,q,a,J)\), positive control gives
only \(Y\kappa uX^\varepsilon\), whereas the target is
\(Qm\kappa uX^\varepsilon\); the exact deficit is \(Y/(Qm)\).

This candidate proves only the strict sector and the exact reduction.
Every original \(t\ge2\) small-\(G\) incidence, the large-\(G\)
near-resonant complement, the rest of the small-\(t\) owner, the hard
and smooth M1 parents, GAR, every M2 parent, endpoint uniformity, M9,
both bridges, and the Gauss-circle quarter target remain open or
conditional at their existing scopes.  The internal exponent \(1/3\),
accepted external benchmark \(0.3144831759740614\ldots\), and target
\(1/4\) are unchanged.

## 1. Endpoint-exact Abel identity

For a fixed row and orientation, let \(W_{v,\omega}(h)\) be the complete
zero-extended literal height sequence and put

\[
 z_{\omega,v}=e(\epsilon_\omega a\bar v_q/q),
 \qquad\epsilon_+=1,\quad\epsilon_-=-1.
\tag{191.C13}
\]

For a power-of-two band \(J\), define the fixed complex packet

\[
 \mathscr J_{\kappa,u,m,q,a,J}^{\sigma}
 =\sum_{\substack{\omega,v\ {\rm literal}\\
                   J\le j_q(a,v)<2J\\j_q(a,v)>T_Q}}
 \frac1{1-z_{\omega,v}}
 \sum_{h\in\mathbb Z}\Delta^-W_{v,\omega}(h)z_{\omega,v}^h.
\tag{191.C13a}
\]

This is jointly summed over both orientations and every literal
\(v,h,t\) label before a modulus.  All local packets below are exact
linear restrictions or projections of (191.C13a).

Finite support gives the exact identity

\[
 \sum_h\{W(h)-W(h-1)\}z^h
 =(1-z)\sum_hW(h)z^h.
\tag{191.C14}
\]

The upper death in the zero extension is included, so there is no
boundary term.  Consequently

\[
 \frac1{1-z}\sum_h\Delta^-W(h)z^h=\sum_hW(h)z^h.
\tag{191.C15}
\]

The sign is positive.  Abel's identity is therefore a re-expression of
the original row sum and supplies no saving by itself.  On a fast
\(J\)-band, \(|1-z|^{-1}\asymp q/J\).

## 2. Exact signed-inverse transport

The two oriented determinant fibres are

\[
 Sv-Uw=h\quad(\omega=+),\qquad
 Uw-vS=h\quad(\omega=-).
\tag{191.C16}
\]

Writing \(\varrho=\varrho_U(v)\), \(\gamma=\gamma_U(v)\), the map

\[
 (S,w)\longmapsto
 (S-\epsilon_\omega\varrho,
  w-\epsilon_\omega\gamma)
\tag{191.C17}
\]

carries the height-\(h\) fibre exactly to height \(h-1\).  Let
\(S_{0,\omega}(h)\in[0,U)\) be the canonical anchor and define

\[
 \nu_\omega(h)=
 \frac{S_{0,\omega}(h)-\epsilon_\omega\varrho
       -S_{0,\omega}(h-1)}{U}\in\{-1,0,1\}.
\tag{191.C18}
\]

For \(S_\omega(h,t)=S_{0,\omega}(h)+Ut\) and the corresponding
\(w_\omega(h,t)\), one has exactly

\[
 S_\omega(h,t)-\epsilon_\omega\varrho
 =S_\omega(h-1,t+\nu_\omega(h)),
\tag{191.C19}
\]

\[
 w_\omega(h,t)-\epsilon_\omega\gamma
 =w_\omega(h-1,t+\nu_\omega(h)).
\tag{191.C20}
\]

Thus the transported affine parity contributes
\((-1)^{\nu_\omega(h)}\).  Before Fourier splitting, odd \(U\) gives
\((-1)^{S_{0,\omega}+t}=(-1)^S\), and either orientation changes this
bare parity by the constant \((-1)^\varrho\).  This is a full-anchor
identity only.  For the accepted character
\(e(kS_{0,\omega}/U)\), the current/transported-previous
mode-and-affine ratio is instead

\[
 \frac{(-1)^t e(kS_{0,\omega}(h)/U)}
 {(-1)^{t+\nu_\omega(h)}e(kS_{0,\omega}(h-1)/U)}
 =(-1)^{\nu_\omega(h)}e(\epsilon_\omega k\varrho/U)
 =(-1)^{\nu_\omega(h)}e(\epsilon_\omega a\varrho/q).
\tag{191.C20a}
\]

It depends on the carry and retained mode and is not
\((-1)^\varrho\) inside the fast projector.  Multiplication by the
carry sequence mixes Fourier modes.  The constant parity law is
reconstructed only after the complete Fourier sum; recombining all
modes returns to the pre-Round-187 packet and is not a proof of the
fast remainder.

## 3. Exact jump-source partition

Write

\[
 W(h)=K(h)G(h)A(h),\qquad
 A(h)=\sum_{t\in I_\omega(h)}(-1)^tB_\omega(h,t),
\tag{191.C21}
\]

where \(K\) is the intersection of the dyadic height interval and the
carrier interval, \(G(h)=\mathbf1_{(U,h)=1}\), and

\[
 B_\omega(h,t)=F(h)\Lambda_\omega(h,t)\Psi_\omega(h,t),
 \qquad F(h)=1-\frac{2\kappa gh}{R_0}.
\tag{191.C22}
\]

Let \(A_0=\kappa gU\).  For the plus orientation, the ordered lower and
upper endpoint/divisor pairs are

\[
 (N_{0,+},d_{0,+})=
 (A_0(\kappa v+2w_+),A_0),\qquad
 (N_{1,+},d_{1,+})=
 ((A_0+2gS_+)\kappa v,A_0+2gS_+).
\tag{191.C22a}
\]

For the minus orientation they are

\[
 (N_{0,-},d_{0,-})=
 ((A_0+2gS_-)\kappa v,A_0+2gS_-),\qquad
 (N_{1,-},d_{1,-})=
 (A_0(\kappa v+2w_-),A_0).
\tag{191.C22b}
\]

They satisfy \(N_{1,\omega}=N_{0,\omega}+2\kappa gh\).  With the
actual zero-extended endpoint coefficient \(\lambda\),

\[
 \Lambda_\omega(h,t)=
 \lambda_{N_{1,\omega},\sigma}(d_{1,\omega})
 \overline{\lambda_{N_{0,\omega},\sigma}(d_{0,\omega})}.
\tag{191.C22c}
\]

The factor \(\Psi\) in (191.C22) is the exact square-root phase.

Put a minus subscript for height \(h-1\).  The exact gated outer-mask
partition is

\[
\begin{aligned}
 \Delta^-W(h)={}&
 \mathbf1_{K_h=1,K_-=0}G_hA_h
 -\mathbf1_{K_h=0,K_-=1}G_-A_-\\
 &+\mathbf1_{K_h=K_-=1}
 \bigl\{
   \mathbf1_{G_h=1,G_-=0}A_h
  -\mathbf1_{G_h=0,G_-=1}A_-\\
 &\hspace{38mm}
  +\mathbf1_{G_h=G_-=1}(A_h-A_-)
 \bigr\}.
\end{aligned}
\tag{191.C22d}
\]

The first line contains the complete live-side outer height/carrier
birth or death.  The next two terms are the complete live-side
coprimality flips.  Only the final persistent-\(K,G\) branch is passed
to the transported affine partition below, so simultaneous outer-mask
changes are neither omitted nor counted twice.

On the third part, use (191.C19)--(191.C20).  Let \(\mathcal C\) be the
current indices whose transported indices lie in the previous
positivity range, and let \(\mathcal B\) and \(\mathcal D\) be the
disjoint current births and previous deaths.  Then

\[
\begin{aligned}
 A(h)-A(h-1)={}&
 \sum_{t\in\mathcal C}(-1)^t
 \{B(h,t)-(-1)^{\nu_\omega(h)}
 B(h-1,t+\nu_\omega(h))\}\\
 &+\sum_{t\in\mathcal B}(-1)^tB(h,t)
 -\sum_{t'\in\mathcal D}(-1)^{t'}B(h-1,t').
\end{aligned}
\tag{191.C23}
\]

This is an exact common-range/birth/death partition.  On a common site,
write a superscript \({\rm tr}\) for evaluation at
\((h-1,t+\nu_\omega(h))\) and \(\chi=(-1)^{\nu_\omega(h)}\).  Exact
telescoping gives

\[
\begin{aligned}
 B_h-\chi B_-^{\rm tr}={}&
 (1-\chi)B_-^{\rm tr}
 +(F_h-F_-)\Lambda_h\Psi_h\\
 &+F_-(\Lambda_h-\Lambda_-^{\rm tr})\Psi_h
 +F_-\Lambda_-^{\rm tr}(\Psi_h-\Psi_-^{\rm tr}).
\end{aligned}
\tag{191.C24}
\]

The four terms are respectively the carry, Fejer change, endpoint
coefficient change, and actual square-root-phase change.  Before
opening either endpoint, the ordered product and conjugation give

\[
\begin{aligned}
 \Lambda_h-\Lambda_-^{\rm tr}={}&
 (\lambda_{1,h}-\lambda_{1,-}^{\rm tr})
 \overline{\lambda_{0,h}}\\
 &+\lambda_{1,-}^{\rm tr}
 (\overline{\lambda_{0,h}}
  -\overline{\lambda_{0,-}^{\rm tr}}),
\end{aligned}
\tag{191.C24a}
\]

where \(\lambda_{i,h}=\lambda_{N_{i,\omega}(h,t),\sigma}
(d_{i,\omega}(h,t))\) uses (191.C22a)--(191.C22b).  Apply the next
identity separately to \(i=0,1\), conjugating the \(i=0\) instance.
If \(\lambda_i=M_i a_i^{\rm lit}\), with \(M_i\) the complete endpoint
arithmetic mask, then

\[
 \lambda_h-\lambda_-^{\rm tr}
 =(M_h-M_-^{\rm tr})a_h^{\rm lit}
 +M_-^{\rm tr}(a_h^{\rm lit}-a_-^{{\rm lit},\rm tr}).
\tag{191.C25}
\]

The first term contains every endpoint squarefree, divisibility,
allocation-coprimality, parity, and residual selected-prime-mask change.
Partition the second term by the first changed entry in this fixed
ordered endpoint-field list:

\[
 (\text{original shell/height branch},
  \text{strict endpoint-ratio cone},
  \text{inherited selector state},
  \text{profile support/branch},
  \text{floor},\text{star},\text{half-weight},
  \text{hard sample},\text{real-}X\text{ crossing},
  \text{endpoint trace},\text{endpoint zero extension}).
\tag{191.C25a}
\]

The profile entry is its cell/branch label, not a replacement for the
actual numerical profile, whose difference remains inside
\(a_i^{\rm lit}\).  Conjugation and endpoint order are already fixed by
(191.C24a).  The endpoint zero extension in (191.C25a) is distinct from
the outer height/carrier terminal in (191.C22d).  Simultaneous endpoint
changes are assigned to the first differing entry, leaving an actual
common-cell coefficient difference when no label changes.  These events
are disjoint and exhaustive.  Equations (191.C21)--(191.C25a) therefore
contain every named literal jump source exactly once and assert no
regularity for any source.

## 4. Proof of the signed-inverse strict sector

The map

\[
 v\bmod U\longmapsto\varrho_U(v)\bmod U
\tag{191.C26}
\]

is a bijection on the unit classes.  Hence (191.C7) uses at most
\(2T_\varrho\) residue classes.  The literal \(v\)-support has length
\(O(u)\), and \(U\mid u\), so every residue class occurs
\(O(u/U+1)=O(u/U)\) times.  Literal masks only delete rows.  Thus

\[
 \#\{v\text{ literal}:0<|\varrho_U(v)|\le T_\varrho\}
 \ll\frac{uT_\varrho}{U}
 \ll\frac{Qmu}{Y}.
\tag{191.C27}
\]

The fast \(J\)-band restriction only decreases this count.  Each row has
\(O(Y)\) heights, \(O(\kappa)\) live affine sites per height, and
pointwise endpoint weight \(O_\varepsilon(X^\varepsilon)\).  Returning
the Abel packet to the exactly equal original row sum by (191.C15), and
only then using the positive count, proves

\[
 |\mathscr J_{{\rm inv},{\rm fix}}|
 \ll_\varepsilon
 Y\kappa X^\varepsilon\frac{uT_\varrho}{U}
 \ll Qm\kappa uX^\varepsilon.
\tag{191.C28}
\]

There is no \(q/J\) loss in (191.C28).  If \(T_\varrho=0\), the sector
is empty.  If the cap is saturated, all unit inverse classes are in the
sector and its row complement is empty.  The proof is a cardinality
argument; the transport makes the cut canonical but supplies no
cancellation on the remaining rows.

## 5. Terminal and Fejer pieces

At the fixed packet level (191.C13a), let
\(\mathscr J_{{\rm inv},{\rm fix}}\) be its exact restriction to
\(0<|\varrho_U(v)|\le T_\varrho\).  On the complementary rows define
the live-side outer terminal atom from the first line of (191.C22d):

\[
 D_K(h)=
 \mathbf1_{K_h=1,K_-=0}G_hA_h
 -\mathbf1_{K_h=0,K_-=1}G_-A_-.
\tag{191.C28a}
\]

Define the two exact complex projections

\[
 \mathscr J_{{\rm terminal},{\rm fix}}
 =\sum_{\substack{\omega,v\ {\rm literal}\\
                   J\le j_q(a,v)<2J, j_q(a,v)>T_Q\\
                   |\varrho_U(v)|>T_\varrho}}
 \frac1{1-z_{\omega,v}}
 \sum_h D_K(h)z_{\omega,v}^h,
\tag{191.C28b}
\]

\[
\begin{aligned}
 \mathscr J_{{\rm Fejer},{\rm fix}}
 ={}&\sum_{\substack{\omega,v\ {\rm literal}\\
                   J\le j_q(a,v)<2J, j_q(a,v)>T_Q\\
                   |\varrho_U(v)|>T_\varrho}}
 \frac1{1-z_{\omega,v}}
 \sum_h z_{\omega,v}^h
 \mathbf1_{K_h=K_-=G_h=G_-=1}\\
 &\qquad\times
 \sum_{t\in\mathcal C_\omega(h)}(-1)^t
 (F_h-F_-)\Lambda_{\omega,h}(t)\Psi_{\omega,h}(t).
\end{aligned}
\tag{191.C28c}
\]

Both orientations and every surviving literal label are completed in
these complex sums before a modulus.  Put

\[
 \mathscr J_{{\rm safe},{\rm fix}}
 =\mathscr J_{{\rm inv},{\rm fix}}
  +\mathscr J_{{\rm terminal},{\rm fix}}
  +\mathscr J_{{\rm Fejer},{\rm fix}},
 \qquad
 \mathscr R_{\rm fix}
 =\mathscr J_{\kappa,u,m,q,a,J}^{\sigma}
  -\mathscr J_{{\rm safe},{\rm fix}}.
\tag{191.C28d}
\]

These are exact linear projections and a complex subtraction, not
separate orientation norms.  The remainder retains every term of
(191.C22d)--(191.C25a) not displayed in (191.C28b)--(191.C28c).

On \(|\varrho|>T_\varrho\), the support of \(K\) in (191.C21) is one
integer interval, so (191.C28a) is supported at at most two heights.
The projective-band count is

\[
 \#\{v:J\le j_q(a,v)<2J\}\ll uJ/q.
\tag{191.C29}
\]

Using \(|1-z|^{-1}\asymp q/J\), the endpoint-row bound, and both
orientations only inside the same packet gives

\[
 |\mathscr J_{{\rm terminal},{\rm fix}}|
 \ll_\varepsilon(q/J)(uJ/q)\kappa X^\varepsilon
 \ll\kappa uX^\varepsilon.
\tag{191.C30}
\]

On a common live height,

\[
 F(h)-F(h-1)=-\frac{2\kappa g}{R_0},
 \qquad \frac{2\kappa gY}{R_0}<1.
\tag{191.C31}
\]

There are \(O(Y)\) heights and \(O(\kappa)\) sites per row.  Therefore

\[
 |\mathscr J_{{\rm Fejer},{\rm fix}}|
 \ll_\varepsilon(q/J)(uJ/q)
 Y\kappa\frac{2\kappa g}{R_0}X^\varepsilon
 \ll\kappa uX^\varepsilon.
\tag{191.C32}
\]

Equations (191.C28), (191.C30), and (191.C32), followed by triangle
inequality among the three already defined joint complex projections,
prove (191.C9).  No absolute value is placed inside
\(\mathscr R_{\rm fix}\).

## 6. Outer ledger

Let \(\mathcal O_{Y,Q}^{\sigma}\) denote the exact inherited linear
outer assembly that defines the Round-189 complex aggregate
\(\mathscr F_{Y,Q}^{\sigma}\).  It sums the disjoint power-of-two
\(J\)-bands and every inherited outer label and weight, including
\(m^{-1}c_q(a)\), before any final real part.  Thus, by definition and
linearity,

\[
 \mathscr F_{Y,Q}^{\sigma}
 =\mathcal O_{Y,Q}^{\sigma}
   (\{\mathscr J_{\kappa,u,m,q,a,J}^{\sigma}\}),
\tag{191.C32a}
\]

\[
 \mathscr J_{Y,Q}^{\rm safe,\sigma}
 =\mathcal O_{Y,Q}^{\sigma}
   (\{\mathscr J_{{\rm safe},{\rm fix}}\}),\qquad
 \mathscr R_{Y,Q}^{\sigma}
 =\mathcal O_{Y,Q}^{\sigma}(\{\mathscr R_{\rm fix}\}).
\tag{191.C32b}
\]

Equations (191.C28d) and (191.C32a)--(191.C32b) prove the exact global
identity (191.C11), with no packet-type conflation.

The exact Round-188 lift and coefficient mass are

\[
 c_{mq}(ma)=m^{-1}c_q(a),
 \qquad\sum_{(a,q)=1}|c_q(a)|\ll\log(2q).
\tag{191.C33}
\]

Thus the \(m\) in (191.C9) cancels before the positive outer sum.
The dyadic bands cost only a fixed logarithm, and with \(u=mqr\),

\[
 \sum_{mq\mid u}1\le\tau_3(u).
\tag{191.C34}
\]

Using the inherited shell connector (191.C3a) and a fresh local exponent
\(0<\eta<\varepsilon\),

\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{191.C35}
\]

The fixed polylogarithmic \(Q\), divisor logarithms, and band logarithm
are absorbed only into the fresh \(X^{\varepsilon-\eta}\) budget, using
\(L\ll X^{1/4}\).  No positive power of \(Y\) is absorbed.  This proves
(191.C10).

## 7. Exact complement and method boundary

The fixed and global safe packets and remainders are defined exactly in
(191.C28d) and (191.C32b).  Equations (191.C21)--(191.C25a) identify
their sources without an inner absolute value.  Positive jump mass on
the \(J\)-band is only

\[
 \frac{Y\kappa uJ}{q}X^\varepsilon,
\tag{191.C36}
\]

whereas Abel variation would require

\[
 \frac{Qm\kappa uJ}{q}X^\varepsilon.
\tag{191.C37}
\]

The deficit is \(Y/(Qm)\).  The legitimate coefficient-uniform control
is on bounded zero-extended height arrays, not independent jump atoms.
For finite height sets \(H_r\) and row phases \(z_r\ne1\), Abel's exact
identity gives

\[
 \sup_{|W_r(h)|\le1}
 \left|\sum_r\frac1{1-z_r}
       \sum_h\Delta^-W_r(h)z_r^h\right|
 =\sum_r|H_r|,
\tag{191.C38}
\]

where every \(W_r\) is zero off \(H_r\).  The upper bound is triangle
inequality after Abel; equality is attained by the lawful coboundaries
\(W_r(h)=\overline{z_r}^{\,h}\mathbf1_{H_r}(h)\), including all births,
deaths, and holes.  Both orientations may be chosen to reinforce under
one outer operation.  Consequently support, pointwise size, separate
total variation, positive completion, or any separable positive norm
cannot prove (191.C12) for the whole bounded-height-array class.  This
is an operator-class insufficiency control, not a realizability claim,
not a lower bound for the fixed literal endpoint coefficient, and not a
disproof of (191.C12).

The first missing input is a signed theorem for the complete remainder,
already on transported common sites where the carry, displaced literal
endpoint coefficients, and actual square-root phases interact.  The
endpoint displacements are controlled by \((\varrho,\gamma)\), not by a
unit step, and the literal masks need not persist.  No accepted
dependency supplies the required \(Y/(Qm)\) gain.

The archived finite controls check only algebra: the ordinary-anchor and
Abel diagnostic records 470,029 exact checks and 2,720 capacity cases,
and the signed-inverse diagnostic records 420,672 exact
transport/parity checks and 1,325 inverse-class counts, all with zero
failures.  They are diagnostic only and supply no asymptotic theorem,
literal density, lift, divisor ledger, or remainder cancellation.

## Dependencies and proposed state effect

Direct dependencies:

- `M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction`;
- `Divisor-bound-elementary`.

Proposed state effect after green post-repair replay: create one
subordinate `proved_internal` reduction node for (191.C5)--(191.C11),
add it as an inconclusive dependency/evidence item to the open
small-\(t\) owner, and keep every owner and exponent unchanged.  Every
original \(t\ge2\) small-\(G\) incidence, the large-\(G\) near-resonant
complement, the rest of the small-\(t\) owner, the hard and smooth M1
parents, GAR, every M2 parent, endpoint uniformity, M9, both bridges,
and the Gauss-circle quarter target remain open or conditional at their
existing scopes.  The internal exponent \(1/3\), accepted external
benchmark \(0.3144831759740614\ldots\), and target \(1/4\) remain
unchanged.
