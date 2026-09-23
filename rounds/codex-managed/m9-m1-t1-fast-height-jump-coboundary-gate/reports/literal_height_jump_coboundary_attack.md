# Round 191 discovery report: literal height-jump coboundary attack

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Task: `literal_height_jump_coboundary_attack`
- Role: discovery
- Starting graph SHA-256:
  `306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa`
- Resource use: 100% analytic/algebraic; 0% numerical theorem evidence
- Primary outcome: **strict target-safe subpacket plus scoped no-go**;
  the full fast packet is not proved

## 1. Result

I prove four facts.

First, the complete zero-extended Round-189 height sequence has the exact
backward-difference decomposition (3.15)--(3.22) below.  It contains,
exactly once, the global height/carrier terminal terms, the outer
coprimality-mask changes, transported affine births and deaths, the
canonical-anchor wrap sign, the Fejer change, the two endpoint arithmetic
mask changes, the common-cell endpoint-coefficient changes, every literal
profile/floor/star/half-weight/hard-sample/crossing/endpoint/zero-extension
change, and the actual square-root-phase change.

Second, there is an exact signed-inverse transport between adjacent
height fibres.  If

\[
 \varrho_U(v)v-\gamma_U(v)U=1,
 \qquad -\frac{U-1}{2}\leq \varrho_U(v)\leq\frac{U-1}{2},
\tag{191.1}
\]

then the plus fibre at height \(h\) maps to the plus fibre at \(h-1\)
by \((S,w)\mapsto(S-\varrho_U(v),w-\gamma_U(v))\), while the minus
fibre maps by the opposite shift.  The transport has an unavoidable
canonical-anchor wrap \(t\mapsto t+\nu_\omega(h)\) and sign
\((-1)^{\nu_\omega(h)}\).  This is an exact fibre identity, not a
cancellation theorem.

Third, with \(U=mq\), the complete fast-row sector

\[
 |\varrho_U(v)|\leq
 T_\varrho:=\min\left\{\frac{U-1}{2},
             \left\lfloor\frac{QmU}{Y}\right\rfloor\right\}
\tag{191.2}
\]

is absolutely target-safe.  For each fixed admissible
\((\kappa,u,m,q,a,J)\), its whole Abel packet is

\[
 \ll_{B,\varepsilon}Qm\kappa uX^\varepsilon.
\tag{191.3}
\]

The exact \(m^{-1}c_q(a)\) lift cancels the \(m\) in (191.3) before
the outer divisor ledger.  This sector can meet the Round-189 fast
sector, because small \(|\varrho_U(v)|\) need not make
\(|a\bar v_q|_q\) small.  It is nevertheless only a second projective
sector shaving: any prescribed set of \(O(QmU/Y)\) unit inverse classes
has the same positive proof.  It supplies no cancellation in the
remaining rows.  It may be empty in an individual literal packet when
\(T_\varrho=0\) or when the literal masks delete all such rows; when the
cap in (191.2) is saturated, its exact row complement is empty.

Fourth, on the exact large-\(|\varrho_U(v)|\) complement, the global
terminal-height/carrier terms and the common-range Fejer-difference term
are also target-safe, each in fact \(O_\varepsilon(\kappa uX^\varepsilon)\)
at the fixed packet interface.  After removing these proved pieces there
is one exact complement, (3.32), still under one outer modulus over both
orientations.  Already its transported common-range carry/square-root
correlation (3.35) has only the positive bound
\(O(Y\kappa uX^\varepsilon)\), missing the target by
\(Y/(Qm)\).  Arithmetic-mask flips, affine births/deaths, and literal
endpoint/crossing jumps remain coupled to it and have the same available
scale.

Thus this report does **not** prove (191.S).  It gives a strict
target-safe subpacket with a single exact complement and a scoped no-go:
support, pointwise size, rowwise variation, orientation bookkeeping, or
any positive/separable norm cannot recover the missing factor.  A new
signed theorem for the actual complement (3.32) is still required.

## 2. Exact statement and hypotheses

Fix the literal Round-189 data

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor,\qquad Y<h\leq2Y,
 \qquad Y>Q,
\tag{191.4}
\]

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y,
 \qquad (a,q)=1,
\tag{191.5}
\]

with \(U\mid u\), \(g=u/U\), and the inherited primitive carrier

\[
 \kappa,g,U\text{ odd},\qquad (u,v)=1,qquad (U,h)=1,
 \qquad0<r_h:=2\kappa gh<R_0:=\lceil L\rceil.
\tag{191.6}
\]

Fix a nonempty fast dyadic band

\[
 J\leq j_q(a,v):=|a\bar v_q|_q<2J,
 \qquad
 j_q(a,v)>
 \min\left\{\frac{q-1}{2},\left\lfloor\frac{Qmq}{Y}\right\rfloor\right\}.
\tag{191.7}
\]

If the cap in (191.7) is \((q-1)/2\), the fast packet is empty; all
formulas below then hold trivially.  Put

\[
 z_{\omega,v}=e(\epsilon_\omega a\bar v_q/q),
 \qquad \epsilon_+=1,\quad\epsilon_-=-1.
\tag{191.8}
\]

For \(U>1\), retain the canonical anchors

\[
 \begin{array}{lll}
 \omega=+:&S_{0,+}(h)=[\bar vh]_U,&
 w_{0,+}(h)=(vS_{0,+}(h)-h)/U,\\[1mm]
 \omega=-:&S_{0,-}(h)=[-\bar vh]_U,&
 w_{0,-}(h)=(h+vS_{0,-}(h))/U,
 \end{array}
\tag{191.9}
\]

and

\[
 S_{\omega}(h,t)=S_{0,\omega}(h)+Ut,
 \quad w_{\omega}(h,t)=w_{0,\omega}(h)+vt,
 \quad s_{\omega}(h,t)=gS_{\omega}(h,t),
\tag{191.10}
\]

\[
 I_\omega(h)=\{t\in\mathbb Z:S_\omega(h,t)>0,
                                  \ w_\omega(h,t)>0\}.
\tag{191.11}
\]

The fast domain has \(U>4Q\), so the separate \(U=1\) convention is
not used here.

Let \(A=\kappa gU\).  The two actual endpoint products and their odd
endpoint divisors are

\[
\begin{array}{c|c|c|c|c}
\omega&N_{0,\omega}(h,t)&d_{0,\omega}(h,t)
      &N_{1,\omega}(h,t)&d_{1,\omega}(h,t)\\ \hline
+&A(\kappa v+2w_+(h,t))&A
 &(A+2gS_+(h,t))\kappa v&A+2gS_+(h,t)\\
-&(A+2gS_-(h,t))\kappa v&A+2gS_-(h,t)
 &A(\kappa v+2w_-(h,t))&A .
\end{array}
\tag{191.12}
\]

They satisfy \(N_{1,\omega}=N_{0,\omega}+r_h\) exactly.

The Round-184 residual selector is retained literally:

\[
 \rho_N(d)=
 \begin{cases}
 1,&\text{no pair is selected for }N,\\
 1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
   +2\mathbf1_{p_Nq_N\mid d},&\text{a pair is selected}.
 \end{cases}
\tag{191.13}
\]

Define the exact zero-extended endpoint coefficient

\[
 \lambda_{N,\sigma}(d)=
 \mathbf1_{N,d>0}\mathbf1_{d\mid N}\mathbf1_{2\nmid d}
 \mu^2(N)\rho_N(d)
 a_{L,X}^{\mathrm{lit},\sigma}(N/d,d).
\tag{191.14}
\]

Here \(a_{L,X}^{\mathrm{lit},\sigma}\) is the actual accepted hard-M1
symbol, not a free weight.  Its moving factor on a live cell is the
accepted

\[
 \eta_L(x)\Phi\!\left(\frac{x}{H+1}\right)
 W\!\left(\sqrt{\frac{4q_Xx}{d}}\right)
 \left(\frac{L^2}{xd}\right)^{3/4},
 \qquad x=N/d,
\tag{191.15}
\]

together with the actual shell/sign constants and every literal strict
cone, profile, floor, star, half-weight, hard-sample, real-\(X\)
crossing, endpoint trace, and zero-extension field.  Nothing below
smooths, frees, or suppresses those fields.

Put

\[
 F(h)=1-\frac{r_h}{R_0},
 \qquad
 \Psi_\omega(h,t)=
 e\!\left(\sigma\sqrt X
       \{\sqrt{N_{1,\omega}(h,t)}-
          \sqrt{N_{0,\omega}(h,t)}\}\right),
\tag{191.16}
\]

\[
 \Lambda_\omega(h,t)=
 \lambda_{N_{1,\omega}(h,t),\sigma}(d_{1,\omega}(h,t))
 \overline{\lambda_{N_{0,\omega}(h,t),\sigma}(d_{0,\omega}(h,t))},
\tag{191.17}
\]

\[
 B_\omega(h,t)=F(h)\Lambda_\omega(h,t)\Psi_\omega(h,t).
\tag{191.18}
\]

Finally, with

\[
 K(h)=\mathbf1_{Y<h\leq2Y}\mathbf1_{0<r_h<R_0},
 \qquad G(h)=\mathbf1_{(U,h)=1},
\tag{191.19}
\]

the complete fixed-row height sequence is exactly

\[
 W_{\kappa,u,U,v,\omega}^{\sigma}(h)
 =K(h)G(h)
   \sum_{t\in I_\omega(h)}(-1)^tB_\omega(h,t),
\tag{191.20}
\]

extended by zero to every integer \(h\).  This is the
\(W_{\kappa,u,mq,v,\omega}^{\sigma}\) of (191.S).

The fixed packet to be estimated is

\[
 \mathscr J=
 \sum_{\substack{\omega,v\ \mathrm{literal}\\J\leq j_q(a,v)<2J}}
 \frac1{1-z_{\omega,v}}
 \sum_{h\in\mathbb Z}
 \{W_{v,\omega}(h)-W_{v,\omega}(h-1)\}z_{\omega,v}^h.
\tag{191.21}
\]

There is one modulus outside the complete sum in the target
\(|\mathscr J|\ll Qm\kappa uX^\varepsilon\).

## 3. Proof and derivation

### 3.1 Endpoint-exact Abel identity

Because (191.20) has finite support,

\[
 \sum_h\{W(h)-W(h-1)\}z^h
 =(1-z)\sum_hW(h)z^h.
\tag{191.22}
\]

Thus (191.21) is exactly the original fixed-mode row sum.  The sign is
\(1-z\), not \(1-z^{-1}\), and there is no endpoint error.  Equation
(191.22) supplies no cancellation by itself.

On (191.7),

\[
 |1-z_{\omega,v}|^{-1}\asymp q/J.
\tag{191.23}
\]

The projective bijection and \(q\mid u\) give

\[
 \#\{v\ \mathrm{literal}:J\leq j_q(a,v)<2J\}
 \ll \frac{uJ}{q}.
\tag{191.24}
\]

### 3.2 Exact adjacent-height transport and its wrap sign

Let \(\varrho=\varrho_U(v)\) and \(\gamma=\gamma_U(v)\) be as in
(191.1).  The two determinant equations are

\[
 Sv-Uw=h\quad(\omega=+),
 \qquad Uw-vS=h\quad(\omega=-).
\tag{191.25}
\]

Writing \(\epsilon_+=1\), \(\epsilon_-=-1\), the map

\[
 (S,w)\longmapsto(S-\epsilon_\omega\varrho,
                   w-\epsilon_\omega\gamma)
\tag{191.26}
\]

sends (191.25) at height \(h\) exactly to the same oriented equation at
height \(h-1\).  Indeed
\(\varrho v-\gamma U=1\).

Define the canonical-anchor wrap

\[
 \nu_\omega(h)=
 \frac{S_{0,\omega}(h)-\epsilon_\omega\varrho
       -S_{0,\omega}(h-1)}{U}\in\{-1,0,1\}.
\tag{191.27}
\]

Then exactly

\[
 S_\omega(h,t)-\epsilon_\omega\varrho
 =S_\omega(h-1,t+\nu_\omega(h)),
\tag{191.28}
\]

\[
 w_\omega(h,t)-\epsilon_\omega\gamma
 =w_\omega(h-1,t+\nu_\omega(h)).
\tag{191.29}
\]

Consequently the transported affine sign is multiplied by

\[
 \chi_\omega(h):=(-1)^{\nu_\omega(h)}.
\tag{191.30}
\]

On heights for which both \((U,h)=1\) and \((U,h-1)=1\), one has
\(S_{0,-}=U-S_{0,+}\), hence
\(\nu_-(h)=-\nu_+(h)\) and
\(\chi_-(h)=\chi_+(h)\).  The two orientations therefore do not acquire
opposite carry signs.

The wrap frequency is also exact.  On any interval \(I\) of consecutive
heights,

\[
 \#\{h\in I:\nu_\omega(h)\ne0\}
 \leq \frac{|I|\,|\varrho|}{U}+1.
\tag{191.31}
\]

This follows by telescoping (191.27); for \(\varrho>0\), for example,
\(\nu_+\) is zero or \(-1\), and the number of wraps differs from
\(|I|\varrho/U\) by less than one.  The other signs and orientation are
identical after reversal.

The actual endpoint displacement under (191.26) is not a unit
displacement.  With the previous-height endpoint evaluated at
\(t+\nu_\omega(h)\), one has

\[
\begin{array}{c|c|c|c|c}
\omega&N_{0,h}-N_{0,h-1}^{\rm tr}
      &N_{1,h}-N_{1,h-1}^{\rm tr}
      &d_{0,h}-d_{0,h-1}^{\rm tr}
      &d_{1,h}-d_{1,h-1}^{\rm tr}\\ \hline
+&2\kappa gU\gamma&2\kappa gv\varrho&0&2g\varrho\\
-&-2\kappa gv\varrho&-2\kappa gU\gamma&-2g\varrho&0.
\end{array}
\tag{191.32}
\]

In both rows the difference of the first two displayed increments is
\(2\kappa g=r_h-r_{h-1}\), as required.  Formula (191.32) retains the
actual products entering (191.14) and (191.16).  It shows why adjacent
height does not mean adjacent endpoint data.

### 3.3 Exact backward-difference partition

For fixed \((v,\omega)\), abbreviate

\[
 A_\omega(h)=\sum_{t\in I_\omega(h)}(-1)^tB_\omega(h,t).
\tag{191.33}
\]

The global carrier and outer arithmetic mask split first.  With
subscript \(-\) denoting \(h-1\),

\[
\begin{aligned}
 \Delta^-W(h)={}&
 \mathbf1_{K_h=1,K_-=0}G_hA_h
 -\mathbf1_{K_h=0,K_-=1}G_-A_- \\
 &+\mathbf1_{K_h=K_-=1}
 \bigl\{
   \mathbf1_{G_h=1,G_-=0}A_h
  -\mathbf1_{G_h=0,G_-=1}A_-\\
 &\hspace{42mm}
  +\mathbf1_{G_h=G_-=1}(A_h-A_-)
 \bigr\}.
\end{aligned}
\tag{191.34}
\]

The first line is the exact dyadic/carrier terminal zero extension.  The
second line before the last term is the exact \((U,h)=1\) mask change.

For the last term define

\[
 \mathcal C_\omega(h)=
 \{t\in I_\omega(h):t+\nu_\omega(h)\in I_\omega(h-1)\},
\tag{191.35}
\]

\[
 \mathcal B_\omega(h)=I_\omega(h)\setminus\mathcal C_\omega(h),
 \qquad
 \mathcal D_\omega(h)=I_\omega(h-1)\setminus
 \{t+\nu_\omega(h):t\in I_\omega(h)\}.
\tag{191.36}
\]

Then

\[
\begin{aligned}
 A_h-A_-={}&
 \sum_{t\in\mathcal C_\omega(h)}(-1)^t
 \{B_\omega(h,t)-\chi_\omega(h)
 B_\omega(h-1,t+\nu_\omega(h))\}\\
 &+\sum_{t\in\mathcal B_\omega(h)}(-1)^tB_\omega(h,t)
 -\sum_{t'\in\mathcal D_\omega(h)}(-1)^{t'}B_\omega(h-1,t').
\end{aligned}
\tag{191.37}
\]

The second and third sums are respectively every transported affine
birth and death.  No positivity site is omitted or duplicated.

On the transported common range write a superscript `tr' for evaluation
at \((h-1,t+\nu_\omega(h))\).  Exact telescoping gives

\[
\begin{aligned}
 B_h-\chi B_-^{\rm tr}={}&
 (1-\chi)B_-^{\rm tr}\\
 &+(F_h-F_-)\Lambda_h\Psi_h\\
 &+F_-(\Lambda_h-\Lambda_-^{\rm tr})\Psi_h\\
 &+F_-\Lambda_-^{\rm tr}(\Psi_h-\Psi_-^{\rm tr}).
\end{aligned}
\tag{191.38}
\]

These are, in order, the anchor-wrap/crossing term, the Fejer change,
the complete two-endpoint coefficient change, and the actual
square-root-phase change.  The phase is exactly (191.16), not a linear
or free oscillatory surrogate.

The endpoint change in (191.38) also splits exactly:

\[
\begin{aligned}
 \Lambda_h-\Lambda_-^{\rm tr}
 ={}&(\lambda_{1,h}-\lambda_{1,-}^{\rm tr})
       \overline{\lambda_{0,h}}\\
 &+\lambda_{1,-}^{\rm tr}
   (\overline{\lambda_{0,h}}-
    \overline{\lambda_{0,-}^{\rm tr}}).
\end{aligned}
\tag{191.39}
\]

For endpoint \(i\in\{0,1\}\), put

\[
 M_i=\mathbf1_{N_i,d_i>0}\mathbf1_{d_i\mid N_i}
 \mathbf1_{2\nmid d_i}\mathbf1_{(d_i,N_i/d_i)=1}
 \mu^2(N_i)\rho_{N_i}(d_i),
 \qquad a_i=a_{L,X}^{\mathrm{lit},\sigma}(N_i/d_i,d_i).
\tag{191.40}
\]

The redundant-looking allocation-coprimality predicate is retained
because it is a named literal deletion; on squarefree support it equals
one.  Now

\[
 \lambda_{i,h}-\lambda_{i,-}^{\rm tr}
 =(M_{i,h}-M_{i,-}^{\rm tr})a_{i,h}
 +M_{i,-}^{\rm tr}(a_{i,h}-a_{i,-}^{\rm tr}).
\tag{191.41}
\]

The first summand in (191.41) is exactly the squarefree,
allocation-coprimality, parity/divisibility, and residual-selector mask
change.

For the second summand, attach to each actual endpoint the ordered
literal **cell/predicate** label vector (the profile entry is its
support/branch label, not a replacement of the numerical profile)

\[
 \mathfrak c=(\text{dyadic profile},\text{floor},\text{star},
 \text{half-weight},\text{hard sample},\text{real-}X\text{ crossing},
 \text{endpoint trace},\text{terminal zero extension}).
\tag{191.42}
\]

If the two label vectors agree, retain the actual difference
\(a_{i,h}-a_{i,-}^{\rm tr}\) as the common-cell endpoint-coefficient
change.  If they differ, assign the whole actual difference to the
first differing entry of the fixed order (191.42).  The first-difference
events are disjoint and exhaustive, so

\[
 a_{i,h}-a_{i,-}^{\rm tr}
 =\delta a_i^{\rm common}
 +\sum_{\ell\in\mathfrak c}\delta a_i^{(\ell)}
\tag{191.43}
\]

is an exact partition, not a majorization.  In the common-cell term the
moving factors are precisely (191.15); in the other terms the literal
profile, floor, star, half-weight, hard sample, crossing, endpoint, or
zero-extension values themselves are retained.  Equations
(191.34), (191.37)--(191.43) are the requested complete jump-source
formula.

### 3.4 The signed-inverse strict row sector

The map

\[
 v\pmod U\longmapsto \varrho_U(v)pmod U
\tag{191.44}
\]

is a bijection on unit classes.  The condition
\(0<|\varrho_U(v)|\leq T_\varrho\) uses at most
\(2T_\varrho\) classes.  The literal \(v\)-interval has length
\(O(u)\); since \(U\mid u\), each class occurs
\(O(u/U+1)=O(u/U)\) times.  All literal masks only delete rows.  Hence

\[
 \#\{v\text{ literal}:0<|\varrho_U(v)|\leq T_\varrho\}
 \ll \frac{uT_\varrho}{U}
 \ll \frac{Qmu}{Y}.
\tag{191.45}
\]

The additional fast \(J\)-band restriction only decreases this count.
The accepted endpoint bound and affine geometry give

\[
 \left|\sum_{t\in I_\omega(h)}(-1)^tB_\omega(h,t)\right|
 \ll_\eta\kappa X^\eta.
\tag{191.46}
\]

There are \(O(Y)\) heights.  Applying (191.22) separately to the exact
row subset, but taking only one final modulus after its two orientations,
gives

\[
 |\mathscr J_{|\varrho|\leq T_\varrho}|
 \ll_\eta
 Y\kappa X^\eta\frac{uT_\varrho}{U}
 \ll Qm\kappa uX^\eta.
\tag{191.47}
\]

This proves (191.3).  No \(q/J\) loss is incurred: the endpoint-exact
Abel expression is returned to its equal original row sum before the
positive count.

The proof is cardinality-only.  More generally, any prescribed set of
\(O(QmU/Y)\) unit inverse classes is paid by the same argument.  Thus
the transport makes (191.2) canonical, but (191.47) is sector shaving,
not a signed height-jump gain.

### 3.5 Global terminal and Fejer jump terms

Restrict now to the exact row complement
\(|\varrho_U(v)|>T_\varrho\).  The support of \(K(h)\) in (191.19) is
one integer interval, so the first line of (191.34) is nonzero at at most
two heights.  By (191.23), (191.24), and (191.46), its packet satisfies

\[
 |\mathscr J_{\rm terminal}|
 \ll_\eta \frac qJ\frac{uJ}{q}\kappa X^\eta
 \ll_\eta\kappa uX^\eta
 \leq Qm\kappa uX^\eta.
\tag{191.48}
\]

For the Fejer term in (191.38),

\[
 F(h)-F(h-1)=-\frac{2\kappa g}{R_0}.
\tag{191.49}
\]

There are \(O(\kappa)\) live sites per row.  On any live common height
\(h>Y\), the carrier gives \(2\kappa gh<R_0\), hence
\(2\kappa gY/R_0<1\).  Therefore

\[
\begin{aligned}
 |\mathscr J_{\rm Fejer}|
 &\ll_\eta \frac qJ\frac{uJ}{q}
 Y\kappa\frac{2\kappa g}{R_0}X^\eta\\
 &\ll_\eta\kappa uX^\eta
 \leq Qm\kappa uX^\eta.
\end{aligned}
\tag{191.50}
\]

This uses the actual endpoint product in (191.38), bounded only after
the exact Fejer difference has been isolated.  It asserts no smoothness
of the remaining factors.

Define the proved strict packet

\[
 \mathscr J^{\rm safe}:=
 \mathscr J_{|\varrho|\leq T_\varrho}
 +\mathscr J_{{\rm terminal},\,|\varrho|>T_\varrho}
 +\mathscr J_{{\rm Fejer},\,|\varrho|>T_\varrho}.
\tag{191.51}
\]

Then

\[
 |\mathscr J^{\rm safe}|
 \ll_{B,\varepsilon}Qm\kappa uX^\varepsilon.
\tag{191.52}
\]

The single exact complement is

\[
 \boxed{\mathscr R^{\rm lit}:=\mathscr J-\mathscr J^{\rm safe}.}
\tag{191.53}
\]

It is the sum, on \(|\varrho|>T_\varrho\), of the outer
\((U,h)=1\) changes, transported affine births/deaths, wrap signs,
endpoint arithmetic-mask changes, common-cell coefficient changes,
every literal event in (191.42), the square-root-phase changes, and all
their original signs.  Both orientations remain inside one complex
sum.  No modulus has been moved inside (191.53).

### 3.6 Restored lift, divisor, and power ledger

At the fixed packet level, the desired estimate for either \(\mathscr J\)
or its exact complement is \(Qm\kappa uX^\varepsilon\).  The Round-188
lift is exactly

\[
 c_{mq}(ma)=m^{-1}c_q(a).
\tag{191.54}
\]

Thus (191.52), after the lift, costs

\[
 m^{-1}|c_q(a)|\,Qm\kappa u
 =Q\kappa u|c_q(a)|.
\tag{191.55}
\]

The actual coefficient mass is

\[
 \sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|c_q(a)|
 \ll\log(2q).
\tag{191.56}
\]

The \(J\)-bands cost another fixed logarithm, and

\[
 \sum_{mq\mid u}1=\tau_3(u).
\tag{191.57}
\]

Consequently the accepted outer ledger is

\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll QL^2\log^{O(1)}(2L)X^\eta
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{191.58}
\]

No positive power of \(Y\) is absorbed.  In (191.47) it is removed by
inverse-residue sparsity before a positive norm; in (191.50) it is
removed by the exact factor \(2\kappa g/R_0<1/Y\).

### 3.7 Scoped positive/separable no-go

The unresolved terms in (191.53) have the trivial jump-mass ledger

\[
 \frac{Y\kappa uJ}{q}X^\eta
\tag{191.59}
\]

before the Abel factor and therefore
\(Y\kappa uX^\eta\) after (191.23).  The target jump mass is

\[
 \frac{Qm\kappa uJ}{q}X^\eta,
\tag{191.60}
\]

so the exact deficit is \(Y/(Qm)\).

This is a rigorous method boundary, not just a failed estimate.  For any
finite jump index set \(\mathcal I\), consider the coefficient-insensitive
operator

\[
 \mathcal T(D)=
 \sum_{(\omega,v,h,t)\in\mathcal I}
 \frac{D_{\omega,v,h,t}z_{\omega,v}^h}
      {1-z_{\omega,v}},
 \qquad |D_{\omega,v,h,t}|\leq1.
\tag{191.61}
\]

Choosing each \(D\) to cancel the argument of its displayed multiplier
gives the exact norm identity

\[
 \sup_{|D|\leq1}|\mathcal T(D)|
 =\sum_{(\omega,v,h,t)\in\mathcal I}
  |1-z_{\omega,v}|^{-1}.
\tag{191.62}
\]

On a saturated ambient band with \(\asymp uJ/q\) rows and
\(\asymp Y\kappa\) atoms per row, (191.62) is
\(\asymp Y\kappa u\).  Hence no theorem using only support,
pointwise magnitude, separate row variation, a positive completion,
large-sieve/alias energy, or a separable positive norm can imply the
\(Qm\kappa u\) target uniformly when \(Y/(Qm)\) is unbounded.  The
array in (191.61) is an adversarial mechanism control, not the actual
hard-M1 coefficient; (191.62) proves no literal lower bound and does not
disprove (191.S).

## 4. First doubtful or unproved step

After the exact safe removal (191.51), the first unproved analytic input
is a signed correlation for (191.53).  It is already open on transported
common sites where both outer coprimality masks are one and no affine
birth or death occurs.

Indeed, after removing the target-safe Fejer difference, the literal
common-range carry/phase part contains

\[
\begin{aligned}
 \mathscr C_{\rm carry+phase}
 ={}&\sum_{\substack{\omega,v,h,t\ \mathrm{transported\ common}\\
                      |\varrho_U(v)|>T_\varrho}}
 \frac{(-1)^tz_{\omega,v}^h}{1-z_{\omega,v}}
 F(h-1)\Lambda_-^{\rm tr}\\
 &\quad\times
 \left\{(1-\chi_\omega(h))\Psi_-^{\rm tr}
       +\Psi_h-\Psi_-^{\rm tr}\right\},
\end{aligned}
\tag{191.63}
\]

with the exact endpoint coefficients (191.14), exact transported
products (191.32), and exact square-root phases (191.16).  The remaining
endpoint-difference terms in (191.38)--(191.43) must in general be kept
with (191.63); bounding (191.63) separately is a stronger sufficient
route, not a claimed necessary theorem.

The first invalid shortcut would be to set
\(\chi_\omega(h)=1\), to call the transported endpoints adjacent, or to
differentiate (191.15) while ignoring the arithmetic and literal event
fields.  Formula (191.31) shows that carry events persist, (191.32)
shows that endpoint displacement is controlled by
\((\varrho,\gamma)\), not by one, and (191.41)--(191.43) show that all
named masks can change.  On common unit heights the carry signs in the
two orientations agree rather than oppose.  The actual phase increment
has no established pointwise smallness, and its positive estimate in
(191.63) is exactly the \(Y\)-scale.

What remains to be proved is therefore a joint signed theorem for the
complete \(\mathscr R^{\rm lit}\), possibly allowing cancellation among
(191.63), arithmetic flips, births/deaths, and endpoint/crossing terms,
which recovers the full factor \(Y/(Qm)\) before any positive norm.  No
such theorem follows from the accepted context.

## 5. Required controls and outcomes

- **Exact Round-189 fast complement:** passed.  Equations
  (191.4)--(191.8) retain \(U=mq>4Q\), \(q>Q\),
  \(m|a|_q>Q\), \(Qm<Y\), and the capped fast condition.

- **Literal K185 carrier and amplitudes:** passed.  Equations
  (191.9)--(191.20) use K185.27 and K185.30--K185.35, including the
  actual two endpoint coefficients and square-root phase.

- **One outer operation and both orientations:** passed.  The exact
  complement (191.53) keeps both orientations in one complex packet;
  no orientation involution is asserted.

- **Endpoint-exact Abel sign and \(q/J\) scale:** passed in
  (191.22)--(191.24).

- **Complete jump-source coverage:** passed in
  (191.34), (191.37)--(191.43).  Global terminal terms, outer and endpoint
  arithmetic masks, affine births/deaths, anchor carries, common
  coefficients, profile/floor/star/half/hard/crossing/endpoint events,
  square-root phases, and terminal zero extensions occur exactly once.

- **Signed-inverse transport:** passed algebraically in
  (191.25)--(191.32).  The wrap sign is retained.  It gives no automatic
  orientation pairing or neighboring-projective-slope identity.

- **Strict inverse-residue sector:** passed at the fixed packet and outer
  ledger in (191.45)--(191.58).  It is a cardinality sector and may be
  empty in a literal packet; it is not promoted as a density theorem.

- **Arithmetic-mask invariance:** rejected.  The exact change is
  retained in (191.34), (191.40), and (191.41).

- **Actual phase and endpoint fields:** passed.  No free smooth or
  bounded weight replaces (191.14)--(191.18).

- **Positive completion, large sieve, alias energy, or arbitrary-array
  closure:** rejected by the scoped norm identity (191.62).  This is not
  a lower bound for the literal packet.

- **Prime bad-slope and centered-prefix control:** not invoked as a
  theorem.  Nothing here asserts a uniform centered-kernel prefix bound.

- **Empty and saturated packets:** passed after (191.7) and (191.47).
  A saturated Round-189 cutoff leaves no fast row; a saturated
  \(T_\varrho\) leaves no signed-inverse row complement.

- **Exact lift and coefficient mass:** passed in
  (191.54)--(191.58).  The \(m^{-1}\) is never suppressed.

- **Full \(Y/(Qm)\) saving before positivity:** passed only for the
  proved strict pieces (191.47)--(191.50); open for (191.53), with exact
  deficit recorded in (191.59)--(191.60).

- **Diagnostic computation:** none used.

- **Owner and exponent quarantine:** passed.  No statement is made for
  original \(t\geq2\), the large-\(G\) near-resonant complement, either
  M1 parent, any M2 parent, endpoint uniformity, M9, a bridge, the global
  theorem, or an exponent improvement.

## 6. Dependencies and exact artifacts used

Only the selected context named in the brief was used:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `state/failure_ledger.md`;
5. `strategy/round191_m1_t1_fast_height_jump_coboundary_strategy.md`;
6. `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`;
7. `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`;
8. `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md`;
9. `proofs/kernels/m9_m1_hard_top_t1_high_h_imprimitive_lift_gcd_reduction.md`;
10. `proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md`; and
11. `rounds/codex-managed/full-proof-round187-189-strategy-literature-review/reviews/conductor_round190_adjudication.md`.

No external theorem, web source, sibling Round-191 report, or numerical
artifact was used.

## 7. Recommended state effect

**Retain** this report as candidate evidence, with no analytic promotion
yet.

The signed-inverse transport, wrap sign, exact jump-source formula, and
the strict target-safe pieces (191.47)--(191.52) are rigorous and useful
for review.  The signed-inverse row cut is nevertheless arbitrary
sector shaving at density \(Qm/Y\), and the single literal complement
(191.53) still contains the full first unproved correlation (191.63) and
the exact \(Y/(Qm)\) deficit.  Therefore keep
`M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction`, the exact
original-\(t=1\) residual, the small-\(t\) owner, and every downstream
owner open.  No proof-state, theorem, bridge, or exponent change is
recommended.
