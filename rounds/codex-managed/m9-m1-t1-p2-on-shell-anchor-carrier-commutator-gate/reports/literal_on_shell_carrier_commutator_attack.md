# Literal on-shell carrier and commutator attack

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Round: 196
- Task: `literal_on_shell_carrier_commutator_attack`
- Role: discovery
- Starting graph SHA-256: `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Status: candidate evidence only
- Numerical theorem evidence: none

## 1. Result

The complete fixed-packet target is **not proved**.  The proposed primitive
common-(x) carrier is a correct algebraic factor, but it is not the carrier
of one literal exact-conductor summand.  The first failure is an exact
normalization failure inherited from the Round-187 parity expansion.

Let (U=\mathfrak m q), let (k=\mathfrak m a) be the mode of exact
conductor (q), and write the literal affine site in either orientation as

$$
 S=S_{0,\omega}(h)+Ut,
 \qquad 0\le S_{0,\omega}(h)<U,
 \qquad S_{0,\omega}(h)\equiv
 \epsilon_\omega\bar v_Uh\pmod U.
\tag{196.1}
$$

The exact-conductor atomic factor in the literal operator is

$$
 \boxed{
 \mathfrak m^{-1}c_q(a)(-1)^t
 e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right),}
 \qquad
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\tag{196.2}
$$

It is not the same as the expression obtained by replacing ((-1)^t) by
((-1)^S).  On the determinant shell, with

$$
 x=\kappa U+2S,
\tag{196.3}
$$

one has exactly

$$
 \boxed{
 (-1)^t e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right)
 =E_U(S_{0,\omega}(h))\,
   \chi_4(\kappa U)\chi_4(x)
   e\!\left(\frac{a\overline2_qx}{q}\right),}
 \qquad E_U(s)=(-1)^s.
\tag{196.4}
$$

The factor after (E_U) is a primitive additive carrier modulo (4q)
with step-two multiplier

$$
 z_{q,a}=-e(a/q),
 \qquad
 (1-z_{q,a})c_q(a)=\frac{2e(a/q)}q.
\tag{196.5}
$$

But (E_U(S_0)) is the complete Round-187 parity Fourier kernel.  Inserting
or deleting it at a fixed exact conductor convolves all modes modulo (U).
After complete Fourier recombination the physical parity ((-1)^S) is
recovered, but then there is no distinguished exact-conductor coefficient
(c_q(a)) left on which to use (196.5).

There are two independent exact obstructions to a genuine literal
(\Delta_2) argument.

1. The Round-191 event sequence compares height (h) with height (h-1).
   Its determinant transport sends (S) to
   (S-\epsilon_\omega\rho_U(v)), hence sends (x) to
   (x-2\epsilon_\omega\rho_U(v)).  It is a long inverse-residue shift,
   not the step (x\mapsto x-2).  On the (T\ge1) Round-192 core one even
   has
   \(|\rho|\ge(A+1)(T+1)>1\).  At (T=0) the complete rho-large branch,
   not merely the exceptional unit-inverse rows, remains.
2. Even if a hypothetical literal term (E_U(S_0)\Delta_2A(x)) were
   present, moving (E_U) through the difference gives the exact identity

$$
   \begin{aligned}
   c_q(a)\sum_x C_{q,a}(x)E_U(S_0(x))\Delta_2A(x)
   ={}&c_q(a)(1-z_{q,a})
       \sum_x C_{q,a}(x)E_U(S_0(x))A(x)\\
    &-c_q(a)\sum_x C_{q,a}(x)
       \{E_U(S_0(x))-E_U(S_0(x-2))\}A(x-2),
   \end{aligned}
   \tag{196.6}
$$

   where (C_{q,a}(x)=\chi_4(\kappa U)\chi_4(x)
   e(a\overline2_qx/q)).  The first line has the desired cancellation.
   The second is a parity-kernel commutator.  It vanishes only at the
   canonical wrap and equals (2E_U(S_0(x))A(x-2)) at every nonwrap step.
   Thus it retains the singular coefficient (c_q(a)) on (U-1) of the
   (U) ambient carrier residues.

This is the first rigorous literal self-return.  It is a route-scoped
no-go, not a lower bound for the actual endpoint coefficients.  With only
the accepted literal pointwise and support inputs, the parity commutator and
the already present endpoint, mask, carry, birth/death, and phase
commutators have the same available positive capacity

$$
 u\min(Y,D_L)X^\varepsilon.
\tag{196.7}
$$

The target is (Q\mathfrak m\kappa uX^\varepsilon), and on the frozen
open region

$$
 \kappa<D_L,
 \qquad \min(Y,D_L)>Q\mathfrak m\kappa,
\tag{196.8}
$$

the unresolved multiplier remains exactly

$$
 \frac{\min(Y,D_L)}{Q\mathfrak m\kappa}>1.
\tag{196.9}
$$

No full target or new target-safe strict sector follows.

## 2. Exact statement and hypotheses

Fix the exact accepted Round-192 hard-(M_1), original-(t=1),
rho-large core, a literal middle or lower residual shell (L\ge2),
(X\ge2), (\sigma\in\{+1,-1\}), and

$$
 Q=H_B,
 \qquad R_0=\lceil L\rceil,
 \qquad D_L=\lceil\sqrt L\rceil.
\tag{196.10}
$$

Retain the exact spectral packet

$$
 U=\mathfrak m q>4Q,
 \quad q>Q,
 \quad \mathfrak m|a|_q>Q,
 \quad Q\mathfrak m<Y,
 \quad U\mid u,
 \quad g=u/U,
 \quad J\le |a\bar v_q|_q<2J,
\tag{196.11}
$$

and the exact inverse-small and Farey complements.  Thus, if

$$
 \rho v_0-\beta U=1,
 \qquad
 T=\min\!\left\{\frac{U-1}{2},
             \left\lfloor\frac{Q\mathfrak m U}{Y}\right\rfloor\right\},
\tag{196.12}
$$

then the retained row has
(|\rho|>T).  At (T=0) the Farey projector is empty and the complete
inherited rho-large remainder is retained.  At (T\ge1), with

$$
 A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},
 \qquad
 \mathcal F_A=
 \{(c,d):1\le c\le A, 0\le d\le c, (c,d)=1\},
\tag{196.13}
$$

every retained row satisfies simultaneously

$$
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A),
 \qquad |\rho|\ge(A+1)(T+1).
\tag{196.14}
$$

The physical mask is imposed before Fourier expansion and before height
differencing:

$$
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}}.
\tag{196.15}
$$

Only its exact open Round-195 packet region (196.8) is considered.  The
spectral lift (\mathfrak m) is never identified with the physical
cofactor (m) or with the primitive cross gcd (\kappa).

The two primitive charts are

$$
 \begin{array}{c|cccc|c}
 \omega&d&d'&m&m'&h\\ \hline
 +&\kappa gU&g(\kappa U+2S)&\kappa v+2w&\kappa v&Sv-Uw\\
 -&g(\kappa U+2S)&\kappa gU&\kappa v&\kappa v+2w&Uw-vS.
 \end{array}
\tag{196.16}
$$

Put

$$
 \begin{array}{c|cc}
 &\delta_\omega&\eta_\omega\\ \hline
 +&\kappa(U-v)-2w&\kappa(U-v)+2S\\
 -&\kappa(U-v)+2S&\kappa(v-U)+2w.
 \end{array}
\tag{196.17}
$$

Then

$$
 2h=v\eta_+ +U\delta_+-\kappa(U^2-v^2),
 \qquad
 2h=U\eta_- -v\delta_-+\kappa(U^2-v^2),
\tag{196.18}
$$

and the common allocation coordinate is

$$
 x=\kappa U+2S
 =\kappa v+\eta_+=\frac{d'}g\quad(+),
 \qquad
 x=\kappa U+2S
 =\kappa v+\delta_- =\frac d g\quad(-).
\tag{196.19}
$$

Every residual selector, endpoint squarefree and allocation-coprimality
mask, profile, floor, star, half weight, hard sample, cell, crossing,
endpoint trace, conjugation, Fejer factor, square-root phase, affine
birth/death, physical-mask commutator, and zero extension remains literal.
Both orientations and both frequency signs remain in the same complex
aggregate before the one outer real part.

### 2.1 Exact physical-to-core operator

For one oriented row, let

$$
 B_{\omega}(h,t)=F(h)\Lambda_\omega(h,t)\Psi_\omega(h,t),
 \qquad
 F(h)=1-\frac{2\kappa gh}{R_0},
\tag{196.20}
$$

where

$$
 \Lambda_\omega(h,t)
 =\lambda_{N_{1,\omega},\sigma}(d_{1,\omega})
  \overline{\lambda_{N_{0,\omega},\sigma}(d_{0,\omega})}
\tag{196.21}
$$

is the actual zero-extended endpoint product and (\Psi_\omega) is the
actual square-root phase.  With (A_0=\kappa gU), the endpoint pairs are

$$
 \begin{array}{c|cc}
 & (N_{0,\omega},d_{0,\omega})&(N_{1,\omega},d_{1,\omega})\\ \hline
 +&(A_0(\kappa v+2w),A_0)&
   ((A_0+2gS)\kappa v,A_0+2gS)\\
 -&((A_0+2gS)\kappa v,A_0+2gS)&
   (A_0(\kappa v+2w),A_0).
 \end{array}
\tag{196.22}
$$

Let (K(h)) be the dyadic-height/carrier interval, let
(G(h)=\mathbf1_{(U,h)=1}), and write (P_\omega(h,t)) for the literal
(P_2) value at that physical atom.  The zero-extended masked row is

$$
 W^P_{\omega,v}(h)
 =K(h)G(h)\sum_{t\in I_\omega(h)}
   (-1)^tP_\omega(h,t)B_\omega(h,t).
\tag{196.23}
$$

Put

$$
 \zeta_{\omega,v}
 =e\!\left(\frac{\epsilon_\omega a\bar v_q}{q}\right).
\tag{196.24}
$$

Before the inverse-small, terminal, Fejer, and Farey projections, the fixed
mode is exactly

$$
 \mathscr J_{\rm fix}^sigma(P_2W)
 =\sum_{\omega,v}
   \frac1{1-\zeta_{\omega,v}}
   \sum_{h\in\mathbb Z}
   \{W^P_{\omega,v}(h)-W^P_{\omega,v}(h-1)\}
   \zeta_{\omega,v}^{,h}.
\tag{196.25}
$$

The upper zero-extension death is present, so (196.25) has no missing
boundary term.  The exact core is obtained linearly as follows:

- restrict to the fast rows satisfying (196.11), the inverse-large rows,
  and the (T=0) or simultaneous (T\ge1) core just stated;
- remove the live-side outer (K)-terminal projection;
- remove the isolated common-site Fejer-difference projection;
- retain every other event below and form one complex subtraction before
  any modulus.

To display those retained events, put (A_h^P=\sum_t(-1)^tP_hB_h).
The exact gated difference first separates the (K) birth/death, the two
(G)-flips, and the persistent-(K,G) term (A_h^P-A_{h-1}^P).  The
first is the removed terminal projection; both (G)-flips remain.  On the
persistent branch, signed-inverse transport gives

$$
 (S,w)\longmapsto
 (S-\epsilon_\omega\rho,
  w-\epsilon_\omega\gamma),
\qquad \rho v-\gamma U=1,
\tag{196.26}
$$

and a canonical carry (\nu_\omega(h)\in\{-1,0,1\}).  With
(\chi=(-1)^{\nu_\omega(h)}), the affine ranges split disjointly into
transported common sites, current births, and previous deaths.  At a common
site one has the exact mask identity

$$
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
  +\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\tag{196.27}
$$

The second term is the physical-mask commutator.  The first expands as

$$
\begin{aligned}
 B_h-\chi B_-^{\rm tr}={}&
 (1-\chi)B_-^{\rm tr}
 +(F_h-F_-)\Lambda_h\Psi_h\\
 &+F_-(\Lambda_h-\Lambda_-^{\rm tr})\Psi_h
 +F_-\Lambda_-^{\rm tr}(\Psi_h-\Psi_-^{\rm tr}).
\end{aligned}
\tag{196.28}
$$

These are respectively carry, Fejer, endpoint-product, and square-root
phase events.  The isolated Fejer term is the removed safe projection; the
other three remain.  Endpoint order and conjugation are fixed by

$$
\begin{aligned}
 \Lambda_h-\Lambda_-^{\rm tr}={}&
 (\lambda_{1,h}-\lambda_{1,-}^{\rm tr})
 \overline{\lambda_{0,h}}
 +\lambda_{1,-}^{\rm tr}
 (\overline{\lambda_{0,h}}
  -\overline{\lambda_{0,-}^{\rm tr}}),
\end{aligned}
\tag{196.29}
$$

and, for each endpoint (\lambda=M a^{\rm lit}),

$$
 \lambda_h-\lambda_-^{\rm tr}
 =(M_h-M_-^{\rm tr})a_h^{\rm lit}
  +M_-^{\rm tr}(a_h^{\rm lit}-a_-^{{\rm lit},{\rm tr}}).
\tag{196.30}
$$

Thus (196.25)--(196.30), after the stated exact projections, are the full
fixed (P_2) core operator.  Squarefree, divisibility, coprimality,
residual-mask, profile, floor, star, half-weight, hard-sample, crossing,
trace, cell, conjugation, and endpoint-zero-extension changes occur in
(196.29)--(196.30); none is suppressed.

Finally, the literal exact-conductor outer contribution has the weight

$$
 c_U(\mathfrak m a)=\frac1{\mathfrak m}c_q(a),
\tag{196.31}
$$

and is assembled, together with all packets, orientations, signs, and
literal labels, inside one outer real part.  Formula (196.31), not an
unweighted primitive carrier, is the normalization to be audited below.

## 3. Proof and derivation

### 3.1 Determinant shell and common coordinate

Since (U=\mathfrak m q\), reduction of the plus identity in (196.18)
modulo (q) gives

$$
 2h\equiv v\eta_++\kappa v^2
       =v(\eta_++\kappa v)=vx\pmod q.
\tag{196.32}
$$

Because ((v,q)=1) and (q) is odd,

$$
 \bar v_qh\equiv\overline2_qx\pmod q.
\tag{196.33}
$$

The minus identity gives

$$
 2h\equiv-v\delta_- -\kappa v^2
       =-v(\delta_-+\kappa v)=-vx\pmod q,
\tag{196.34}
$$

so

$$
 -\bar v_qh\equiv\overline2_qx\pmod q.
\tag{196.35}
$$

Equations (196.33)--(196.35) prove the common on-shell phase in both
orientations.  Since (\kappa U) and (x=\kappa U+2S) are odd,

$$
 (-1)^S=\chi_4(\kappa U)\chi_4(x).
\tag{196.36}
$$

Therefore

$$
 (-1)^S e\!\left(
 \frac{\epsilon_\omega a\bar v_qh}{q}\right)
 =\chi_4(\kappa U)\chi_4(x)
  e\!\left(\frac{a\overline2_qx}{q}\right).
\tag{196.37}
$$

This identity is correct.  The issue is whether its left side is the
literal exact-conductor atom.

### 3.2 Primitive carrier and formal denominator cancellation

For odd (x), (\chi_4(x)=-i e(x/4)).  If

$$
 b_{q,a}\equiv q+4a\overline2_q\pmod{4q},
\tag{196.38}
$$

then (196.37) is the constant
(-i\chi_4(\kappa U)) times (e(b_{q,a}x/(4q))).  The integer
(b_{q,a}) is odd.  If (p\mid q), then
(b_{q,a}\equiv2a\not\equiv0\pmod p); hence

$$
 (b_{q,a},4q)=1.
\tag{196.39}
$$

Its step-two ratio is

$$
 \frac{e(b_{q,a}(x+2)/(4q))}{e(b_{q,a}x/(4q))}
 =-e(a/q)=z_{q,a}.
\tag{196.40}
$$

Since (1+e(-a/q)=e(-a/q)\{1+e(a/q)\}),

$$
 (1-z_{q,a})c_q(a)
 =(1+e(a/q))\frac{2}{q\{1+e(-a/q)\}}
 =\frac{2e(a/q)}q.
\tag{196.41}
$$

Thus every algebraic assertion about the bracketed primitive carrier is
valid.

### 3.3 The literal exact-conductor normalization

Round 187 does not attach (196.37) to one mode.  It writes

$$
 E_U(s)=\sum_{k\bmod U}c_U(k)e(ks/U),
 \qquad
 c_U(k)=\frac{2}{U\{1+e(-k/U)\}},
\tag{196.42}
$$

and, at each orientation and height, multiplies the mode by

$$
 A_{\omega}(h)=\sum_{t\in I_\omega(h)}(-1)^tB_\omega(h,t).
\tag{196.43}
$$

At (k=\mathfrak m a), (196.42) gives (196.31), while

$$
 e\!\left(\frac{\epsilon_\omega k\bar v_Uh}{U}\right)
 =e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right).
\tag{196.44}
$$

Consequently (196.2) is the exact atomic factor.  From (196.1) and oddness
of (U),

$$
 (-1)^S=(-1)^{S_{0,\omega}(h)}(-1)^t,
 \qquad
 (-1)^t=E_U(S_{0,\omega}(h))(-1)^S.
\tag{196.45}
$$

Combining (196.37) and (196.45) proves (196.4).

The missing (E_U(S_0)) cannot be absorbed into a constant or into the
literal endpoint amplitude.  Indeed, multiplication by it gives

$$
 E_U(S_0)e(\mathfrak m aS_0/U)
 =\sum_{r\bmod U}c_U(r)
   e\!\left(\frac{(r+\mathfrak m a)S_0}{U}\right).
\tag{196.46}
$$

The conductors of (r+\mathfrak m a\) vary.  Thus (196.46) is a convolution
of the complete mode set, not an identity within the fixed (q,a) packet.
Conversely, complete Fourier recombination gives

$$
 (-1)^t\sum_{k\bmod U}c_U(k)e(kS_0/U)
 =(-1)^tE_U(S_0)=(-1)^S.
\tag{196.47}
$$

In (196.47) the anchor modes and their individual coefficients have been
summed away.  One therefore cannot retain both the physical parity
((-1)^S) and a distinguished exact-conductor anchor
(c_q(a)e(aS_0/q)).  Doing so double counts the parity kernel.  This is the
first invalid literal step in the proposed mechanism.

### 3.4 Literal step multiplier and the parity-kernel commutator

Suppose an on-shell step (x\mapsto x+2) is taken at fixed
((\kappa,U,v,w)).  In both charts (S\mapsto S+1), and

$$
 S_0\mapsto[S_0+1]_U.
\tag{196.48}
$$

Let (c_x=1) when (S_0=U-1) and (c_x=0) otherwise.  Then the new affine
index is (t+c_x).  The anchor phase changes by (e(a/q)), and hence the
literal ratio is

$$
 \boxed{
 \frac{(-1)^{t+c_x}e(\epsilon_\omega a\bar v_qh'/q)}
      {(-1)^t e(\epsilon_\omega a\bar v_qh/q)}
 =(-1)^{c_x}e(a/q).}
\tag{196.49}
$$

It is not the constant (-e(a/q)).  Equivalently,

$$
 \frac{E_U([S_0+1]_U)}{E_U(S_0)}
 =\begin{cases}-1,&S_0\ne U-1,\\+1,&S_0=U-1,
 \end{cases}
\tag{196.50}
$$

and (196.49) is the product of (196.50) and the primitive ratio
(z_{q,a}).

At a wrap, the literal multiplier is (-e(a/q)), and (196.41) applies.
At every nonwrap step it is (e(a/q)), and instead

$$
 \left|(1-e(a/q))c_q(a)\right|
 =\frac{2}{q}\left|\tan\frac{\pi a}{q}\right|.
\tag{196.51}
$$

For the primitive unit (a=(q-1)/2), the right side is
(2q^{-1}\cot(\pi/(2q))\asymp1), not (O(q^{-1})).  Thus the near-half
singularity remains on nonwrap steps.

Identity (196.6) is now immediate from

$$
 \Delta_2(E_UA)(x)
 =E_U(S_0(x))\Delta_2A(x)
  +\{E_U(S_0(x))-E_U(S_0(x-2))\}A(x-2)
\tag{196.52}
$$

and the finite-support summation identity

$$
 \sum_x C_{q,a}(x)\Delta_2F(x)
 =(1-z_{q,a})\sum_x C_{q,a}(x)F(x).
\tag{196.53}
$$

There is no endpoint omission because all sequences are zero-extended.
For the backward step, the parity difference in (196.52) is zero precisely
when the current residue is (0), and is (2E_U(S_0(x))) otherwise.  It
is therefore an interior, full-density commutator, not a two-endpoint
error.

### 3.5 The actual event shift is not (\Delta_2)

The literal event sequence is already displayed in
(196.25)--(196.30).  Its persistent common-site pair is the signed-inverse
transport (196.26).  In the common coordinate,

$$
 x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\rho.
\tag{196.54}
$$

Therefore the actual difference is a (2\epsilon_\omega\rho)-shift.  It
does not contain a factor (\Delta_2) on the full row set.  Decomposing a
long shift into unit (S)-steps would introduce (|\rho|) terms and all
intermediate masks and endpoints; the accepted core supplies no
(|\rho|^{-1}) factor.  This is the same long-step Abel self-return already
recorded by the Round-192 kernel.

The determinant step proposed in (196.48) is a different pairing.  From
(196.16), at fixed ((U,v,w)),

$$
 h_+(S+1)-h_+(S)=v,
 \qquad
 h_-(S+1)-h_-(S)=-v.
\tag{196.55}
$$

It does not pair the adjacent heights in (196.25).  On the live packet
(v\asymp L/\kappa\), whereas the event difference is one height unit.
The two mechanisms cannot be identified.

Even on an exceptional unit-inverse row, the physical step changes the
literal fields.  In the plus chart (x=d'/g) is the far coordinate, so
(x\mapsto x\pm2) moves the upper-failure boundary and the moving upper
endpoint.  In the minus chart (x=d/g) is the close coordinate, so the
same step moves the lower-close boundary.  The exact difference therefore
contains the physical-mask commutator (196.27), squarefree/divisibility and
coprimality flips (196.30), canonical carries, affine births/deaths,
unequal endpoint translations, cell and crossing changes, Fejer and
square-root-phase changes, and zero-extension events.  No permitted
artifact proves target-sized bounds for these commutators.

### 3.6 Complete packet power ledger

Round 195 proves, on all (\kappa<D_L) packets,

$$
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon.
\tag{196.56}
$$

The (\kappa u) term is target-safe.  Put (M=\min(Y,D_L)).  The open
region has (M>Q\mathfrak m\kappa).  The repaired literal carrier gives no
reduction of the (Mu) term: its parity commutator has coefficient (2)
at every nonwrap step and retains (c_q(a)), while all further literal
commutators are bounded only by the same atom count.  Hence the strongest
available fixed estimate remains (196.56), with exact deficit

$$
 \frac{Mu}{Q\mathfrak m\kappa u}
 =\frac{M}{Q\mathfrak m\kappa}.
\tag{196.57}
$$

The exact lift is (\mathfrak m^{-1}c_q(a)), with

$$
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),
 \qquad
 \sum_{\mathfrak m q\mid u}1\le\tau_3(u).
\tag{196.58}
$$

If the fixed target had been proved, the accepted outer ledger would be

$$
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{196.59}
$$

Instead, the unresolved term carries the packetwise multiplier (196.57).
It is strictly larger than one and is not a fixed logarithm.  No positive
power of (M), (Y), (D_L), (q), (U), or (L) can be absorbed into
(X^\varepsilon).  Thus the fixed-to-outer passage does not repair the
self-return.

The statement that the parity commutator has ambient full capacity is a
mechanism statement.  A bounded-array control can be supported on nonwrap
sites and dephase the carrier, attaining the corresponding operator
capacity.  Such arrays need not be literal endpoint products; no literal
lower mass or failure of the desired theorem is asserted.

## 4. First doubtful or unproved step

The first invalid step is not an analytic inequality.  It is the proposed
replacement

$$
 (-1)^t e(\epsilon_\omega a\bar v_qh/q)
 \quad\rightsquigarrow\quad
 (-1)^S e(\epsilon_\omega a\bar v_qh/q)
\tag{196.60}
$$

inside one fixed exact-conductor mode.  Equation (196.4) shows that
(196.60) drops the nonconstant factor (E_U(S_{0,\omega}(h))).  Equation
(196.46) shows that restoring it convolves the complete (U)-mode family.
Equation (196.47) shows that complete recombination returns the original
physical parity and removes the isolated coefficient to which (196.41)
was to be applied.

After this normalization is repaired, the first unproved analytic step
would be a jointly signed estimate for the second line of (196.6) together
with every literal event in (196.27)--(196.30), gaining

$$
 \frac{\min(Y,D_L)}{Q\mathfrak m\kappa}
\tag{196.61}
$$

before any positive norm, uniformly over the whole open region and both
(T)-branches.  No accepted dependency supplies such an estimate.  The
actual event sequence also lacks the prerequisite genuine (\Delta_2)
factor by (196.54)--(196.55).

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_round195_open_P2_packet_region` | PASS.  The analysis is restricted exactly to (196.8), with no widening or deletion. |
| `physical_mask_before_spectral_operations` | PASS.  (P_2) is inserted in (196.23) before (196.25) and before exact-conductor assembly. |
| `both_T_branches` | PASS.  (T=0) keeps the entire inherited rho-large branch; (196.14) is retained simultaneously at (T\ge1). |
| `both_orientations_and_frequency_signs` | PASS.  The two charts are (196.16)--(196.19), and the operator sum is kept complex and joint. |
| `spectral_lift_gcd_vs_kappa` | PASS.  (U=\mathfrak m q), (c_U(\mathfrak ma)=\mathfrak m^{-1}c_q(a)), and (\mathfrak m\ne\kappa). |
| `on_shell_x_coordinate_identity` | PASS.  Equation (196.19) proves both identities. |
| `determinant_anchor_congruence` | PASS.  Equations (196.32)--(196.35) give the exact signs. |
| `parity_character_identity` | PASS.  Equation (196.36) is exact, but it concerns ((-1)^S), not the literal fixed-mode parity ((-1)^t). |
| `primitive_4q_carrier` | PASS with normalization caveat.  Equations (196.38)--(196.40) prove primitivity for the bracket in (196.4); the literal atom has the extra (E_U(S_0)). |
| `exact_conductor_coefficient_normalization` | PASS.  Equations (196.2), (196.31), and (196.42)--(196.44) retain the exact lift and coefficient. |
| `step_two_multiplier_denominator_cancellation` | PASS for the nonliteral bracket, FAIL for the literal fixed mode.  The literal multiplier is (196.49); (196.51) retains constant near-half capacity on nonwrap steps. |
| `genuine_Delta2_before_identity` | FAIL, rigorously.  The actual event shift is (196.54), and the determinant (x\)-step changes height by (196.55). |
| `actual_endpoint_event_vectors` | PASS.  Equations (196.20)--(196.22) and (196.29)--(196.30) retain endpoint order, conjugation, masks, and actual values. |
| `physical_mask_commutator` | PASS.  It is the second term of (196.27) and is not discarded. |
| `squarefree_coprimality_flips` | PASS.  Outer (G)-flips and endpoint-mask differences remain in (196.27)--(196.30). |
| `carry_birth_death_zero_extension` | PASS.  The canonical carry, disjoint affine births/deaths, outer death, and endpoint zero extensions remain in the operator reconstruction. |
| `Fejer_square_root_phase` | PASS.  Both differences appear in (196.28); only the already accepted isolated Fejer projection is removed. |
| `one_outer_real_part` | PASS.  No orientation, sign, or event family is separately normed. |
| `complete_packet_power_ledger` | PASS/OPEN.  Equations (196.56)--(196.59) expose every relevant power and the unchanged multiplier (196.57); the target remains open. |
| `no_consecutive_or_arbitrary_array_replacement` | PASS.  No such replacement is used as theorem evidence.  Bounded arrays are used only as a mechanism falsifier, explicitly not as literal lower mass. |
| `no_separate_orientation_norm` | PASS.  The normalization obstruction holds before, and therefore also inside, the joint two-orientation aggregate. |
| `no_T_branch_or_submask_escape` | PASS.  No wrap-only, unit-inverse-only, mask-deleted, or proper-submask estimate is claimed. |
| `original_t1_only_downstream_scope` | PASS.  The conclusion is confined to the exact inherited original-(t=1) (P_2) core. |
| `exponent_quarantine` | PASS.  No parent, bridge, theorem, or exponent is changed. |

The unsigned, character-erased, phase-conjugated, consecutive-support, and
arbitrary-array shadows confirm only that the repaired commutator can have
full operator capacity.  They are not promoted to physical counterexamples.
The low-carrier and wrap-only shadows are proper submasks and do not prove
the assigned target.  Separate orientations or deletion of (T=0) would
change the operator and were not used.

No symbolic or numerical diagnostic was needed.  The work was entirely
analytical and algebraic.

## 6. Dependencies and exact artifacts used

Only the permitted Round-196 context was used:

1. `protocol.md`;
2. `state/proof_obligations.yml` at graph hash
   `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`;
3. `state/active_campaign.yml`;
4. `state/failure_ledger.md`;
5. `strategy/round196_m1_t1_p2_on_shell_anchor_carrier_commutator_strategy.md`;
6. `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md`;
7. `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md`;
8. `proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md`;
9. `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`;
10. `proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md`;
11. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reports/literal_p2_determinant_fibre_vector_attack.md`;
12. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/conductor_round195_report_reconciliation.md`;
13. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/synthesis.md`;
14. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/conductor_round195_adjudication.md`;
15. the assigned Round-196 task brief.

No sibling Round-196 report, external source, web result, or unpermitted
kernel was used.  Computation was not used.

## 7. Recommended state effect

**Retain the complete (P_2) remainder open.**  After independent review,
record the following as a route-scoped obstruction, not as a disproof of the
literal estimate:

1. the common on-shell coordinate, determinant congruences, primitive
   (4q) bracket, and formal identity (196.41) are exact;
2. the literal fixed exact-conductor mode is (196.2), equivalently (196.4),
   and necessarily contains the complete parity kernel (E_U(S_0));
3. the literal step multiplier is the carry-dependent (196.49), while
   forcing the primitive multiplier through a hypothetical difference
   creates the full-density parity commutator (196.6);
4. the actual recombined event sequence has the long shift (196.54), not a
   genuine (\Delta_2), and every physical/event commutator remains
   unpriced at the inherited (u\min(Y,D_L)X^\varepsilon) capacity; and
5. the precise first missing theorem is the signed literal commutator
   estimate in Section 4, with the packet deficit (196.61).

Do not promote the full fixed-packet bound, complete (P_2), (P_1),
complete original (t=1), any other original-(t) incidence, the hard
small-(t) owner, smooth (M_1), GAR, any (M_2) parent, endpoint
uniformity, (M9), either bridge, the quarter theorem, or any exponent.
