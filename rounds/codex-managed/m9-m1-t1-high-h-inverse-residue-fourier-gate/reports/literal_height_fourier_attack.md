# 1. Result

Fix (B>0), (X\geq2), a literal middle or lower residual hard-M1
shell (L\geq2), (\sigma\in\{+1,-1\}), and a nonempty dyadic block

\[
 H_B=\lfloor(\log(2X))^B\rfloor<Y<h\leq2Y,
 \qquad R_0=\lceil L\rceil .
\]

The complete one-sided estimate (K185.37) is **not proved**.  The exact
inverse-residue expansion does, however, prove a strict target-safe
Fourier packet and isolate a canonical signed complement.

Put (Q=H_B\geq1), and for odd (U>1) write

\[
 c_U(k):={\widehat E_U(k)\over U}
 ={2\over U\{1+e(-k/U)\}},\qquad
 |k|_U:=\min\{k,U-k\}\quad(0\leq k<U).
\tag{1.1}
\]

The following pieces have total absolute size

\[
 O_{B,\varepsilon}(L^2X^\varepsilon):
\tag{1.2}
\]

1. the complete (U=1) physical contribution, with its separate
   canonical anchors and index sets;
2. the **complete exact-conductor packet** \(q\leq Q\), where
   \(q=U/(k,U)\); this contains the exact \(k=0\) mode \(1/U\) as
   \(q=1\) and includes every primitive numerator at every such
   conductor;
3. within the exact \(q>Q\) complement, every remaining mode when
   \(1<U\leq4Q\); and
4. within \(q>Q\) and \(U>4Q\), every mode with
   \(0<|k|_U\leq Q\).

All four statements retain both orientations, both endpoint
coefficients, the residual selector, squarefree and coprimality
deletions, profiles, floors, stars, hard samples, crossings, phases,
and zero extensions.  Their union is a transformed Fourier sector, not
an assertion that its individual frequencies are physical incidences.

The exact complementary signed aggregate consists of

\[
 q={U\over(k,U)}>Q,\qquad U>4Q,\qquad |k|_U>Q,
\tag{1.3}
\]

with every (h,v,t,k) and both orientations still under one outer real
part.  Positive recombination gives only

\[
 |\mathscr R_{Y,Q}^{\sigma}|
 \ll_\varepsilon YL^2X^\varepsilon,
\tag{1.4}
\]

after the usual divisor-logarithm absorption.  Thus its full power
deficit is exactly the missing factor (Y).  Moreover, the two
near-half residues already carry an absolute positive proportion of
the Fourier (\ell^2)-mass.  Hence centering, deleting a fixed
polylogarithmic low band, Fourier Cauchy, positive alias energy, or
positive Poisson recombination cannot themselves supply that factor.
This is a rigorous mechanism-scoped capacity/self-return obstruction,
not a lower bound for the literal M1 coefficient and not a disproof of
the one-sided target.

The exact reparametrization \(u=gU\), \(n=gh\) is decisive for item 2:
literal support gives \(u,v\asymp L/\kappa\), \(h\ll U\), and
\(O(\kappa)\) live affine sites, hence \(O(UL)\) atoms at fixed
\((\kappa,u,U)\).  Exact conductor \(q\) has Fourier mass
\(O((q/U)\log(2q))\), so its positive cost is only
\(O(Lq\log(2q))\) before divisor summation.  This proves the complete
\(q\leq Q\) packet, not merely ordinary residues near zero.

The proved exit is therefore a
`strict_high_h_inverse_residue_fourier_sector`, with the exact
complement (1.3).  The proof works with (Q=(\log(2X))^A) for every
fixed (A>0); (Q=H_B) is used to keep the packet canonical for this
campaign.  There is no maximal fixed-polylogarithmic choice.

# 2. Exact statement and hypotheses

## 2.1 Literal carrier

The primitive domain is

\[
 \mathcal D_Y=\left\{(\kappa,g,h,U,v):
 \begin{array}{c}
 \kappa,g,h,U,v>0,\quad \kappa,g,U\ {\mathrm{odd}},\\
 (gU,v)=1,\quad(U,h)=1,\quad
 0<2\kappa gh<R_0,\quad Y<h\leq2Y
 \end{array}\right\}.
\tag{2.1}
\]

For (U>1), with (\bar v v\equiv1\pmod U) and least residues in

\(
\{0,\ldots,U-1\}
\), set

\[
 \begin{array}{lll}
 +:&S_{0,+}=[\bar vh]_U,&w_{0,+}=(S_{0,+}v-h)/U,\\[1mm]
 -:&S_{0,-}=[-\bar vh]_U,&w_{0,-}=(h+vS_{0,-})/U.
 \end{array}
\tag{2.2}
\]

For (U=1), retain exactly

\[
 (S_{0,+},w_{0,+})=(0,-h),\qquad
 (S_{0,-},w_{0,-})=(0,h).
\tag{2.3}
\]

For either orientation,

\[
 S_{t,\omega}=S_{0,\omega}+Ut,\qquad
 s_{t,\omega}=gS_{t,\omega},\qquad
 w_{t,\omega}=w_{0,\omega}+vt,
\tag{2.4}
\]

\[
 I_{\mathfrak f,\omega}
 =\{t\in\mathbb Z:S_{t,\omega}>0,\ w_{t,\omega}>0\}.
\tag{2.5}
\]

Thus for (U=1), (I_{\mathfrak f,+}=\{t\geq1:vt>h\}) and

\(I_{\mathfrak f,-}=\{t\geq1\}\); the literal zero extension makes
both sums finite.  Positivity in (2.5) is imposed before every square
root.

The endpoint coefficient is exactly

\[
 \lambda_{N,\sigma}(d)=
 \begin{cases}
 \mu^2(N)\rho_N(d)
 a_{L,X}^{\mathrm{lit},\sigma}(N/d,d),
 &N,d>0,\ \mu^2(N)=1,\ d\mid N,\ 2\nmid d,\\
 0,&\text{otherwise},
 \end{cases}
\tag{2.6}
\]

where (\rho_N) is exactly the Round-184 no-pair or selected
neither/both mask.  In the plus orientation,

\[
 N_{\mathfrak f,t}^{+}
 =\kappa gU(\kappa v+2w_{t,+}),\qquad
 N_{\mathfrak f,t}^{+}+r
 =(\kappa gU+2s_{t,+})\kappa v,
\tag{2.7}
\]

\[
 \begin{aligned}
 B_{\mathfrak f,+}^{\sigma}(t)={}&
 \left(1-{r\over R_0}\right)
 \lambda_{N_{\mathfrak f,t}^{+}+r,\sigma}
        (\kappa gU+2s_{t,+})
 \overline{\lambda_{N_{\mathfrak f,t}^{+},\sigma}(\kappa gU)}\\
 &\times e\!\left({\sigma\sqrt X\,r\over
 \sqrt{N_{\mathfrak f,t}^{+}+r}
 +\sqrt{N_{\mathfrak f,t}^{+}}}\right),
 \qquad r=2\kappa gh.
 \end{aligned}
\tag{2.8}
\]

In the minus orientation,

\[
 N_{\mathfrak f,t}^{-}
 =(\kappa gU+2s_{t,-})\kappa v,\qquad
 N_{\mathfrak f,t}^{-}+r
 =\kappa gU(\kappa v+2w_{t,-}),
\tag{2.9}
\]

\[
 \begin{aligned}
 B_{\mathfrak f,-}^{\sigma}(t)={}&
 \left(1-{r\over R_0}\right)
 \lambda_{N_{\mathfrak f,t}^{-}+r,\sigma}(\kappa gU)
 \overline{\lambda_{N_{\mathfrak f,t}^{-},\sigma}
        (\kappa gU+2s_{t,-})}\\
 &\times e\!\left({\sigma\sqrt X\,r\over
 \sqrt{N_{\mathfrak f,t}^{-}+r}
 +\sqrt{N_{\mathfrak f,t}^{-}}}\right),
 \qquad r=2\kappa gh.
 \end{aligned}
\tag{2.10}
\]

Equations (2.6)--(2.10) retain the literal selector, shell, strict
cone, height, profile, floor, star, half-weight, hard-sample, real-

\(X\) crossing, endpoint, sign, phase, squarefree, coprimality, and
zero-extension fields.  No coefficient is regularized.

Write

\[
 A_{\mathfrak f,\omega}^{\sigma}
 :=\sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t),
 \qquad \epsilon_+=1,\quad\epsilon_-=-1.
\tag{2.11}
\]

The frozen block is

\[
 \mathcal S_Y^\sigma
 =\Re\sum_{\omega\in\{+,-\}}
 \sum_{\mathfrak f\in\mathcal D_Y}
 (-1)^{S_{0,\omega}}A_{\mathfrak f,\omega}^{\sigma}.
\tag{2.12}
\]

This is one real part over the complete sum, not a sum of separately
absoluted orientations.

## 2.2 Exact (U=1), zero, and centered pieces

Define the complete (U=1) complex piece

\[
 \mathscr U_{1,Y}^{\sigma}
 :=\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\in\mathcal D_Y\\U=1}}
 A_{\mathfrak f,\omega}^{\sigma}.
\tag{2.13}
\]

For odd (U>1), put (a_{\mathfrak f}=[\bar vh]_U).  Exact Fourier
inversion gives

\[
 (-1)^{S_{0,\omega}}
 =E_U(\epsilon_\omega a_{\mathfrak f})
 ={1\over U}
 +\sum_{k=1}^{U-1}c_U(k)
 e\!\left({\epsilon_\omega k\bar vh\over U}\right).
\tag{2.14}
\]

Accordingly the exact zero-mode piece is

\[
 \mathscr Z_Y^\sigma
 :=\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\in\mathcal D_Y\\U>1}}
 {1\over U}A_{\mathfrak f,\omega}^{\sigma},
\tag{2.15}
\]

and the centered nonzero-mode piece is

\[
 \mathscr C_Y^\sigma
 :=\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\in\mathcal D_Y\\U>1}}
 \sum_{k=1}^{U-1}c_U(k)
 e\!\left({\epsilon_\omega k\bar vh\over U}\right)
 A_{\mathfrak f,\omega}^{\sigma}.
\tag{2.16}
\]

Thus, with no rearrangement error,

\[
 \boxed{
 \mathcal S_Y^\sigma
 =\Re\{\mathscr U_{1,Y}^\sigma
       +\mathscr Z_Y^\sigma+\mathscr C_Y^\sigma\}.}
\tag{2.17}
\]

The change of variables

\[
 u=gU,\qquad n=gh,\qquad g={u\over U}
\tag{2.18}
\]

is a bijection from (2.1) with \(U>1\) to

\[
 \kappa,u,U,h,v>0,\quad U>1,\quad \kappa,u,U\ {\rm odd},\quad
 U\mid u,\quad (u,v)=1,\quad(U,h)=1,\quad
 0<2\kappa {u\over U}h<R_0,\quad Y<h\leq2Y.
\tag{2.19}
\]

For \(k\bmod U\), set

\[
 q_U(k):={U\over(k,U)}.
\tag{2.20}
\]

For \(q>1\), let \(\mathbb U(q)\) denote the reduced residues modulo
\(q\), and set

\[
 c_q(a):={2\over q\{1+e(-a/q)\}}.
\tag{2.21}
\]

Use the exact special convention
\(\mathbb U(1)=\{0\}\), \(c_1(0)=1\).  The map

\[
 k={U\over q}a,\qquad q\mid U,\qquad a\in\mathbb U(q)
\tag{2.22}
\]

is a disjoint parametrization of all \(k\bmod U\), including \(k=0\)
at \(q=1\), and

\[
 c_U(k)={q\over U}c_q(a),\qquad
 e\!\left({\epsilon_\omega k\bar vh\over U}\right)
 =e\!\left({\epsilon_\omega a\bar vh\over q}\right).
\tag{2.23}
\]

Here the inverse \(\bar v\bmod U\) reduces to the inverse modulo every
\(q\mid U\).  For \(Q=H_B\), define the complete low exact-conductor
packet

\[
 \boxed{
 \begin{aligned}
 \mathscr P_{Y,\leq Q}^{\sigma}:={}&
 \sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\in\mathcal D_Y\\U>1}}
 \sum_{\substack{q\mid U\\q\leq Q}}{q\over U}
 \sum_{a\in\mathbb U(q)}
 c_q(a)e\!\left({\epsilon_\omega a\bar vh\over q}\right)
 A_{\mathfrak f,\omega}^{\sigma}.
 \end{aligned}}
\tag{2.24}
\]

Its \(q=1\) summand is exactly \(\mathscr Z_Y^\sigma\).  Its exact
complement before any further split is

\[
 \mathscr D_{Y,>Q}^{\sigma}
 :=\sum_{\omega}\sum_{\substack{\mathfrak f\in\mathcal D_Y\\U>1}}
 \sum_{\substack{0\leq k<U\\q_U(k)>Q}}
 c_U(k)e\!\left({\epsilon_\omega k\bar vh\over U}\right)
 A_{\mathfrak f,\omega}^{\sigma},
\tag{2.25}
\]

so that exactly

\[
 \mathscr Z_Y^\sigma+\mathscr C_Y^\sigma
 =\mathscr P_{Y,\leq Q}^{\sigma}
  +\mathscr D_{Y,>Q}^{\sigma}.
\tag{2.26}
\]

Inside (2.25), define the still target-safe ordinary low-residue packet

\[
 \mathscr L_{Y,Q}^{>,\sigma}
 :=\sum_{\omega}\sum_{\substack{\mathfrak f\in\mathcal D_Y\\U>1}}
 \sum_{\substack{0\leq k<U,\ q_U(k)>Q\\
          U\leq4Q\ {\rm or}\ 0<|k|_U\leq Q}}
 c_U(k)e\!\left({\epsilon_\omega k\bar vh\over U}\right)
 A_{\mathfrak f,\omega}^{\sigma}.
\tag{2.27}
\]

The final exact complementary signed aggregate is

\[
 \boxed{
 \begin{aligned}
 \mathscr R_{Y,Q}^{\sigma}:={}&
 \sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\in\mathcal D_Y\\U>4Q}}
 \sum_{\substack{1\leq k<U\\q_U(k)>Q,\ |k|_U>Q}}
 c_U(k)e\!\left({\epsilon_\omega k\bar vh\over U}\right)
 \sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t).
 \end{aligned}}
\tag{2.28}
\]

The exact strict decomposition is therefore

\[
 \boxed{
 \mathcal S_Y^\sigma
 =\Re\{\mathscr U_{1,Y}^\sigma
       +\mathscr P_{Y,\leq Q}^\sigma
       +\mathscr L_{Y,Q}^{>,\sigma}
       +\mathscr R_{Y,Q}^\sigma\}.}
\tag{2.29}
\]

# 3. Proof or derivation

## 3.1 Fourier normalization and orientation algebra

For odd (U), finite geometric summation gives

\[
 \widehat E_U(k)
 =\sum_{a=0}^{U-1}(-1)^ae(-ka/U)
 ={1-\{-e(-k/U)\}^U\over1+e(-k/U)}
 ={2\over1+e(-k/U)}.
\tag{3.1}
\]

In particular (\widehat E_U(0)=1), so the mean is exactly (1/U),
not (1).  Moreover

\[
 c_U(k)={e(k/(2U))\over U\cos(\pi k/U)},\qquad
 \sum_{k\bmod U}|c_U(k)|\ll\log(2U),\qquad
 \sum_{k\bmod U}|c_U(k)|^2=1.
\tag{3.2}
\]

The last equality is Parseval.  Since ((U,hv)=1),

\(a_{\mathfrak f}\ne0\pmod U\).  Hence

\[
 E_U(-a_{\mathfrak f})=-E_U(a_{\mathfrak f}).
\tag{3.3}
\]

Thus the unsplit two-orientation anchor is exactly

\[
 E_U(a_{\mathfrak f})
 \bigl(A_{\mathfrak f,+}^{\sigma}
       -A_{\mathfrak f,-}^{\sigma}\bigr).
\tag{3.4}
\]

Equation (3.4) supplies no cancellation because the two literal
amplitudes are not equal.  It also explains a useful centering
identity:

\[
 E_U^\circ(-a)=-E_U^\circ(a)-{2\over U}
 \quad(a\not\equiv0\pmod U),
 \qquad E_U^\circ(a):=E_U(a)-{1\over U}.
\tag{3.5}
\]

Thus pairing orientations after centering merely creates another
target-safe (1/U) trace and leaves the literal orientation difference;
it does not annihilate the complement.

## 3.2 Literal counting lemma

The accepted multiplicity-one carrier gives, for fixed

\((\kappa,g,h,U)\) and either orientation,

\[
 \#\{v\}\ll {L\over\kappa},\qquad
 \#\{\text{live }t\text{ on one }v\text{-row}\}\ll\kappa,
\tag{3.6}
\]

and therefore

\[
 \sum_v\sum_{t\in I_{\mathfrak f,\omega}}
 |B_{\mathfrak f,\omega}^{\sigma}(t)|
 \ll_\varepsilon LX^\varepsilon.
\tag{3.7}
\]

The two endpoint bounds are absorbed by epsilon rebudgeting.  A live
term also has

\[
 U\ll {L\over\kappa g},\qquad
 \kappa g<{R_0\over2h}\ll {L\over h}.
\tag{3.8}
\]

For (M\geq1), elementary divisor counting gives

\[
 \sum_{\kappa g<M}1\ll M\log(2M),\qquad
 \sum_{\kappa g<M}{1\over\kappa g}\ll\log^2(2M),
\tag{3.9}
\]

where imposing oddness only decreases the sums.  Consequently

\[
 \sum_{Y<h\leq2Y}
 \sum_{\kappa g<R_0/(2h)}1
 \ll L\log(2L).
\tag{3.10}
\]

This is the precise height ledger used below: the (Y) possible
heights are offset by the (L/h\asymp L/Y) available products

\(\kappa g\).

## 3.3 Target-safe pieces

For (U=1), (3.7) and (3.10) give

\[
 |\mathscr U_{1,Y}^{\sigma}|
 \ll_\varepsilon L^2\log(2L)X^\varepsilon
 \ll_\varepsilon L^2X^\varepsilon.
\tag{3.11}
\]

This pays all admissible (\kappa,g,h,v,t); no claim of an empty

\(U=1\) high-height range is needed.

For the zero mode, (3.7)--(3.10) and

\(\sum_{U\leq M}U^{-1}\ll\log(2M)\) give

\[
 \begin{aligned}
 |\mathscr Z_Y^\sigma|
 &\ll_\varepsilon LX^\varepsilon
 \sum_{Y<h\leq2Y}\sum_{\kappa g<R_0/(2h)}
 \sum_{2\leq U\ll L/(\kappa g)}{1\over U}\\
 &\ll L^2\log^2(2L)X^\varepsilon
 \ll_\varepsilon L^2X^\varepsilon.
 \end{aligned}
\tag{3.12}
\]

Thus the exact mean (1/U) recovers the complete height factor before
any positive orientation or endpoint recombination.

The stronger exact-conductor grouping follows from (2.18).  On a live
atom, the original cross-gcd variables satisfy

\[
 u=gU\asymp {L\over\kappa},\qquad
 v\asymp {L\over\kappa},\qquad
 n=gh\ll {L\over\kappa}.
\tag{3.12a}
\]

Since \(g=u/U\), the last relation gives \(h=n/g\ll U\).  At fixed
\((\kappa,u,U)\), the number of possible \(h\)'s is therefore
\(O(U)\), the number of \(v\)'s is \(O(L/\kappa)\), and each affine
row has \(O(\kappa)\) live sites.  Both orientations together thus
have

\[
 O(UL)
\tag{3.12b}
\]

literal atoms at fixed \((\kappa,u,U)\).  This is an upper count over
all heights, so imposing \(Y<h\leq2Y\) only deletes atoms.

By (2.23) and (3.2), the complete Fourier mass at exact conductor \(q\)
is

\[
 {q\over U}\sum_{a\in\mathbb U(q)}|c_q(a)|
 \ll {q\over U}\log(2q).
\tag{3.12c}
\]

Multiplying (3.12b) and (3.12c) shows that exact conductor \(q\) costs

\[
 O_\varepsilon\!\left(Lq\log(2q)X^\varepsilon\right)
\tag{3.12d}
\]

at fixed \((\kappa,u,U)\).  Now \(U\mid u\), \(q\mid U\), and literal
support permits \(O(L/\kappa)\) values of \(u\) for each \(\kappa\).
Consequently

\[
 \begin{aligned}
 |\mathscr P_{Y,\leq Q}^{\sigma}|
 &\ll_\varepsilon
 LQ\log(2Q)X^\varepsilon
 \sum_{\kappa\ll L}
 \sum_{u\asymp L/\kappa}\tau(u)^2\\
 &\ll_\varepsilon
 QL^2\{\log(2LQ)\}^{O(1)}X^\varepsilon
 \ll_{B,\varepsilon}L^2X^\varepsilon .
 \end{aligned}
\tag{3.12e}
\]

The divisor factor counts the nested choices \(q\mid U\mid u\).
Thus (3.12e) proves the **complete** \(q\leq Q\) packet, including
near-half ordinary residues when their reduced conductor is small.  It
is strictly stronger than paying only \(k=0\) or only residues near
zero.  Equation (3.12) remains the independent requested zero-mode
power check.

For (1<U\leq4Q), (3.2) gives

\[
 \sum_{2\leq U\leq4Q}\sum_{k=1}^{U-1}|c_U(k)|
 \ll Q\log(2Q).
\tag{3.13}
\]

For (U>4Q) and (0<|k|_U\leq Q),

\[
 |\cos(\pi k/U)|\geq2^{-1/2},\qquad
 \sum_{0<|k|_U\leq Q}|c_U(k)|
 \leq {2\sqrt2Q\over U}.
\tag{3.14}
\]

Equations (3.7), (3.10), (3.13), and (3.14) yield

\[
 |\mathscr L_{Y,Q}^{>,\sigma}|
 \ll_\varepsilon
 QL^2\{\log(2LQ)\}^{O(1)}X^\varepsilon
 \ll_{B,\varepsilon}L^2X^\varepsilon,
\tag{3.15}
\]

because \(Q=H_B\) is a fixed power of \(\log(2X)\).  This estimate is
applied only to the \(q>Q\) subpacket in (2.27).  All moduli

all remaining \(q>Q\) modes of moduli \(U\leq4Q\) are paid
completely; for larger \(U\), the factor \(Q/U\) is paid before the
triangle inequality over the retained ordinary low residues.
The same estimates survive summation over the (O(\log(2L))) dyadic
height blocks, including the first and the terminal block truncated by

\(2\kappa gh<R_0\).

## 3.4 Restored power of the centered complement

For the remaining modes, positive frequency summation and (3.2) give,
at fixed (\kappa,g,h,U\),

\[
 \sum_{\omega,v,t}
 \sum_{\substack{k\bmod U\\q_U(k)>Q,\ |k|_U>Q}}
 |c_U(k)B_{\mathfrak f,\omega}^\sigma(t)|
 \ll_\varepsilon L\log(2U)X^\varepsilon.
\tag{3.16}
\]

Summing (U\ll L/(\kappa g)), then using the second estimate in
(3.9), gives

\[
 \begin{aligned}
 |\mathscr R_{Y,Q}^{\sigma}|
 &\ll_\varepsilon L^2\log(2L)X^\varepsilon
 \sum_{Y<h\leq2Y}
 \sum_{\kappa g<R_0/(2h)}{1\over\kappa g}\\
 &\ll_\varepsilon
 YL^2\{\log(2L)\}^{3}X^\varepsilon
 \ll_\varepsilon YL^2X^\varepsilon.
 \end{aligned}
\tag{3.17}
\]

The (L,Y,\kappa,g,U) ledger is therefore:

| piece | Fourier weight at fixed (U) | fixed ((\kappa,g,h,U)) cost | dyadic cost before log absorption |
|---|---:|---:|---:|
| (U=1) | (1) | (L) | (L^2\log L) |
| (k=0, U>1) | (1/U) | (L/U) | (L^2\log^2L) |
| exact conductor \(q\) in \((\kappa,u,U)\) coordinates | \(O((q/U)\log q)\) | \(O(Lq\log q)\) after all \(h,v,t\) | \(O(QL^2\log^{O(1)}L)\) for all \(q\leq Q\) |
| \(q>Q,\ k\ne0,\ U\leq4Q\) | \(O(\log U)\) | \(O(L\log U)\) | \(O(QL^2\log^{O(1)}L)\) |
| \(q>Q,\ 0<|k|_U\leq Q,\ U>4Q\) | \(O(Q/U)\) | \(O(LQ/U)\) | \(O(QL^2\log^{O(1)}L)\) |
| exact remainder \(q>Q,\ U>4Q,\ |k|_U>Q\) | \(O(\log U)\) | \(O(L\log U)\) | \(O(YL^2\log^{O(1)}L)\) |

Only the last line retains the full factor (Y).  Since the other
three complex pieces are bounded absolutely at target size, (2.29)
shows that the original one-sided target is equivalent, up to a
target-safe additive term, to

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{3.18}
\]

No absolute value is required or asserted in (3.18).

## 3.5 Exact positive-norm and self-return obstruction

The high packet is not small in Fourier energy.  For odd \(U>4Q\), the
two residues \(k=(U-1)/2,(U+1)/2\) are coprime to \(U\), so their
exact conductor is \(q=U>Q\); they belong to (1.3), and

\[
 |c_U(k)|={1\over U\sin(\pi/(2U))}\geq {2\over\pi}.
\tag{3.19}
\]

Therefore

\[
 \sum_{\substack{q_U(k)>Q\\|k|_U>Q}}|c_U(k)|^2
 \geq {8\over\pi^2}.
\tag{3.20}
\]

Deleting the zero and low modes leaves a coefficient vector of
constant (\ell^2)-mass; there is no hidden (Y^{-1/2}), much less

\(Y^{-1}\), in a positive Fourier norm.

More explicitly, for arbitrary finite weights (W_j) carrying residue

\(a_j\bmod U\), put (F(k)=\sum_jW_je(ka_j/U)).  Then

\[
 \sum_{k\bmod U}c_U(k)F(k)
 =\sum_jE_U(a_j)W_j,
\tag{3.21}
\]

while Parseval gives

\[
 \sum_{k\bmod U}|F(k)|^2
 =U\sum_{a\bmod U}
 \left|\sum_{j:a_j=a}W_j\right|^2.
\tag{3.22}
\]

Thus a positive alias (TT^*\) measures positive residue-bucket energy,
and the full inverse transform (3.21) exactly reconstructs the original
signed block.  Literal squarefree, coprimality, residual-selector,
profile, endpoint, and zero-extension deletions give no proved bound on
the bucket energy or its variation in (h,v,t\).  A Poisson or geometric
sum in (h) after replacing these weights by absolute values is subject
to the same obstruction.

Finally, on any fixed retained finite carrier,

\[
 \sup_{|W_j|\leq1}
 \left|\sum_jE_{U_j}(a_j)(-1)^{t_j}W_j\right|
 =\#\{j\},
\tag{3.23}
\]

by choosing (W_j=E_{U_j}(a_j)(-1)^{t_j}).  Adding the conjugate of
the square-root phase gives the same control when that phase is present.
This rigorously rules out a coefficient-uniform use of nonresonance or
bare alternation.  It is an artificial adversarial control only; the

\(W_j\) need not be realizable by the actual Vaaler endpoint product.
The strict gain proved here uses exactly the \(\chi_4\)-induced affine
anchor: its residue mean is \(1/U\), and its exact-conductor mass is
\(O((q/U)\log(2q))\).  The literal Vaaler/profile coefficient is
retained in both endpoints and used only through its accepted pointwise
bound and support count; no unproved smoothness of it is invoked.
Accordingly this report proves no full arbitrary-coefficient theorem.
For an unsigned anchor the zero Fourier coefficient is \(1\), so even
the zero-mode height ledger loses its \(1/U\) gain.

# 4. First doubtful or unproved step

The first unproved literal estimate is exactly

\[
 \boxed{
 \begin{aligned}
 \Re\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\kappa,g,h,U,v>0\\
 \kappa,g,U\ {\mathrm{odd}},\ (gU,v)=1,\ (U,h)=1\\
 0<2\kappa gh<R_0,\ Y<h\leq2Y,\ U>4H_B}}
 \sum_{\substack{1\leq k<U\\
 q_U(k)=U/(k,U)>H_B,\ |k|_U>H_B}}
 {2e(\epsilon_\omega k\bar vh/U)
  \over U\{1+e(-k/U)\}}
 \sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t)
 \ \ll_{B,\varepsilon}L^2X^\varepsilon .
 \end{aligned}}
\tag{4.1}
\]

There is one outer real part in (4.1).  Both orientations, every
primitive row, every inverse residue, every affine index, and every
literal field remain joint until that real part.  The available
positive estimate is (3.17), larger by the complete factor (Y).

The first missing input is therefore a theorem about the **actual**
joint literal amplitude in (h,v,t\) (and possibly the two
orientations), strong enough to recover (Y) before a positive norm.
No bounded variation, translation invariance, residue equidistribution,
orientation equality, or Fourier-energy saving for that amplitude is
present in the permitted dependencies.  Calling the modes in (4.1)
"nonresonant" does not prove such an estimate: arbitrary deletion can
align the amplitude with their additive phases, as (3.23) shows.

# 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_one_sided_outer_real_part` | **PASS.** (2.12), (2.17), (2.29), and (4.1) have one real part outside both orientations, all rows, modes, and indices.  Absolute values occur only after a strict packet has been isolated. |
| `literal_K185_27_30_35_carrier` | **PASS.** (2.1)--(2.10) reproduce the invariant domain, anchors, index sets, endpoint products, Fejer factor, and phase. |
| `both_orientations_and_sigma` | **PASS.** Every formula holds for each fixed (\sigma=\pm1), and (\epsilon_+=1,\epsilon_-=-1) retains both anchor signs. |
| `primitive_domain_and_multiplicity_one` | **PASS.** (2.18)--(2.19) independently verify that \(u=gU,\ n=gh\) is bijective, with \(U\mid u\), \(g=u/U\), and no row multiplicity; (2.22) is a disjoint exact-conductor partition of every \(k\bmod U\). |
| `U1_anchor_convention` | **PASS.** (2.3), (2.5), and (2.13) retain (w_{0,+}=-h,w_{0,-}=h) and pay all live (U=1) sites. |
| `selector_squarefree_coprime_deletions` | **PASS.** They remain inside both literal (\lambda)'s.  They are used only as deletions in positive counts and never as regular signed weights. |
| `profile_endpoint_phase_zero_extension` | **PASS.** (2.6)--(2.10) retain both endpoints, conjugation, phase, profiles, crossings, and zero extension. |
| `inverse_residue_fourier_normalization` | **PASS.** (3.1)--(3.2) give (\widehat E_U(k)=2/(1+e(-k/U))), coefficient (c_U(k)=\widehat E_U(k)/U), mean (1/U), and exact Parseval normalization. |
| `height_zero_mode_power` | **PASS.** (3.10)--(3.12) give (L^2\log^{O(1)}L), independent of (Y), before absorption. |
| `centered_nonzero_modes_remain_joint` | **PASS.** (2.16), the exact \(q>Q\) complement (2.25), and the final complement (2.28)/(4.1) keep \(h,v,t,k\), both orientations, and all literal fields joint. |
| `full_factor_Y_before_positive_recombination` | **PASS for the strict packet; FAIL for the remainder.** The exact-conductor ledger (3.12a)--(3.12e) pays all \(h\) at fixed \((\kappa,u,U)\) before mode/divisor triangle; the \(1/U\), \(Q/U\), and \(U\leq4Q\) ledgers do likewise.  Positive recombination of (2.28) gives (3.17), so no full-target claim is made. |
| `no_positive_Poisson_alias_energy_or_conductor_self_return` | **PASS as a no-go.** (3.19)--(3.22) show constant high-mode (\ell^2)-mass and exact reconstruction/positive bucket energy.  No positive transform is used as cancellation. |
| `false_unsigned_and_adversarial_controls` | **PASS.** For the unsigned residue function (1), the zero Fourier coefficient is (1), not (1/U), so the height-zero-mode proof fails.  Equation (3.23) rules out an arbitrary-coefficient extension and is not called literal lower mass. |
| `original_t1_only_downstream_scope` | **PASS.** Even (4.1) would close only the exact Round-184 residual and original (t=1) face through accepted connectors. |
| `exponent_quarantine` | **PASS.** No (t\geq2), near-resonant, M1/M2 parent, endpoint, M9, bridge, quarter-theorem, or exponent status is changed. |

No numerical or symbolic experiment and no external theorem were used.

# 6. Dependencies and exact artifacts used

Only the assigned brief and its permitted context were used:

1. `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/briefs/literal_height_fourier_attack.md`;
2. `protocol.md`;
3. `state/proof_obligations.yml` (the five active target nodes and their exact graph relations);
4. `state/active_campaign.yml`;
5. `strategy/round187_m1_t1_high_h_inverse_residue_fourier_strategy.md`;
6. `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`;
7. `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`;
8. `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reports/literal_residual_fejer_tangent_gcd_attack.md`;
9. `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/reports/tangent_gcd_transfer_capacity_audit.md`;
10. `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/synthesis.md`; and
11. `rounds/codex-managed/full-proof-round183-185-strategy-literature-review/reviews/conductor_round186_adjudication.md`.

The direct proof dependencies are the accepted K185.27 and
K185.30--K185.35 carrier, its fixed-\((\kappa,g,h)\) multiplicity
count, the literal endpoint bound, and
elementary divisor counting.  No unlisted source, M2 estimate, or
coefficient-regularity assertion is imported.

# 7. Recommended state effect

**Promote only after the required independent seam reviews** the strict
target-safe Fourier packet (1.2), including the complete
\(q\leq H_B\) exact-conductor block, the exact decomposition (2.29),
and the exact complement (2.28) under the Round-187 exit label
`strict_high_h_inverse_residue_fourier_sector`.

**Retain open** the complete high-height target.  Its first unresolved
relation is the one-sided joint estimate (4.1), whose positive bound has
the full factor-\(Y\) deficit.  Record (3.19)--(3.23) only as subordinate
evidence that
centering, low-mode deletion, positive Fourier/alias energy, positive
Poisson recombination, bare affine alternation, orientation
antisymmetry without amplitude control, and arbitrary-coefficient
nonresonance self-return to capacity.

Make no state change to the original \(t\geq2\) small-\(G\)
incidences, the large-\(G\) near-resonant complement, the complete
small-\(t\) owner, either M1 parent, any M2 owner, endpoint uniformity, M9,
either bridge, the Gauss-circle target, or any exponent claim.
