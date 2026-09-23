# Formalized hard-M1 (t=1) high-height inverse-residue conductor reduction

## 1. Exact statement

Fix real (X\ge2), a literal middle or lower residual hard-M1 shell
(L\ge2), (sigma\in\{+1,-1\}), and fixed (B>0).  Put

\[
 R_0=\lceil L\rceil,\qquad
 Q=H_B=\lfloor(\log(2X))^B\rfloor.
\]

Fix a nonempty dyadic block (Y<h\le2Y) with (Y>H_B).  Use exactly
the primitive carrier, canonical anchors, positive affine index sets,
and literal endpoint amplitudes (B_{\mathfrak f,\omega}^\sigma(t))
of (K185.27) and (K185.30)--(K185.35).  Thus

\[
 \mathfrak f=(\kappa,g,h,U,v),\quad
 \kappa,g,h,U,v>0,\quad \kappa,g,U\text{ odd},
\]

\[
 (gU,v)=1,\quad(U,h)=1,\quad
 0<2\kappa gh<R_0,
\]

and

\[
 A_{\mathfrak f,\omega}^\sigma
 :=\sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^\sigma(t).
\]

Every selector, squarefree and coprimality deletion, profile, floor,
star, hard sample, crossing, endpoint, conjugation, Fejer factor,
square-root phase, sign, and zero extension remains inside (B).

For (U>1), let

\[
 a_{\mathfrak f}=[\bar vh]_U,\qquad
 \epsilon_+=1,\quad\epsilon_-=-1,
\]

\[
 E_U(a)=(-1)^{[a]_U},\qquad
 c_U(k)={2\over U\{1+e(-k/U)\}},\qquad
 q_U(k)={U\over(k,U)},
\]

and (|k|_U=\min(k,U-k)) for (0\le k<U).  Retain for (U=1) the
separate anchors

\[
 (S_{0,+},w_{0,+})=(0,-h),\qquad
 (S_{0,-},w_{0,-})=(0,h).
\]

Then the dyadic high-height block has the exact decomposition

\[
 \mathcal S_Y^\sigma
 =\Re\{\mathscr U_{1,Y}^\sigma
       +\mathscr P_{Y,\le Q}^\sigma
       +\mathscr L_{Y,Q}^{>,\sigma}
       +\mathscr R_{Y,Q}^\sigma\},
\tag{187.K1}
\]

where

\[
 \mathscr U_{1,Y}^\sigma
 =\sum_{\omega}\sum_{\substack{\mathfrak f\\U=1}}
 A_{\mathfrak f,\omega}^\sigma,
\tag{187.K2}
\]

\[
 \begin{aligned}
 \mathscr P_{Y,\le Q}^\sigma
 ={}&\sum_{\omega}
 \sum_{\substack{\mathfrak f\\U>1}}
 \sum_{\substack{q\mid U\\q\le Q}}{q\over U}
 \sum_{a\in\mathbb U(q)}c_q(a)
 e(\epsilon_\omega a\bar vh/q)
 A_{\mathfrak f,\omega}^\sigma,
 \end{aligned}
\tag{187.K3}
\]

with the exact convention

\[
 \mathbb U(1)=\{0\},\quad c_1(0)=1,
 \qquad
 c_q(a)={2\over q\{1+e(-a/q)\}}\quad(q>1),
\]

\[
 \begin{aligned}
 \mathscr L_{Y,Q}^{>,\sigma}
 ={}&\sum_{\omega}
 \sum_{\substack{\mathfrak f\\U>1}}
 \sum_{\substack{0\le k<U,\ q_U(k)>Q\\
              U\le4Q\ \mathrm{or}\ 0<|k|_U\le Q}}
 c_U(k)e(\epsilon_\omega k\bar vh/U)
 A_{\mathfrak f,\omega}^\sigma,
 \end{aligned}
\tag{187.K4}
\]

and

\[
 \begin{aligned}
 \mathscr R_{Y,Q}^\sigma
 ={}&\sum_{\omega}
 \sum_{\substack{\mathfrak f\\U>4Q}}
 \sum_{\substack{1\le k<U\\q_U(k)>Q,\ |k|_U>Q}}
 c_U(k)e(\epsilon_\omega k\bar vh/U)
 A_{\mathfrak f,\omega}^\sigma.
 \end{aligned}
\tag{187.K5}
\]

All outer sums in (187.K2)--(187.K5) retain (Y<h\le2Y) and the
full primitive domain above.  There is exactly one real part in
(187.K1).

The strict packet obeys

\[
 |\mathscr U_{1,Y}^\sigma|
 +|\mathscr P_{Y,\le Q}^\sigma|
 +|\mathscr L_{Y,Q}^{>,\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{187.K6}
\]

The remaining positive estimate is only

\[
 |\mathscr R_{Y,Q}^\sigma|
 \ll_\varepsilon YL^2X^\varepsilon.
\tag{187.K7}
\]

Consequently the original one-sided dyadic target is equivalent, up to
the absolutely target-safe term (187.K6), to the still-open relation

\[
 \boxed{
 \Re\mathscr R_{Y,Q}^\sigma
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{187.K8}
\]

## 2. Fourier normalization and exact partition

For odd (U), finite geometric summation gives

\[
 \widehat E_U(k)
 =\sum_{a=0}^{U-1}(-1)^ae(-ka/U)
 ={2\over1+e(-k/U)}.
\tag{187.K9}
\]

Hence

\[
 E_U(a)=\sum_{k\bmod U}c_U(k)e(ka/U),\qquad
 c_U(0)={1\over U},
\tag{187.K10}
\]

\[
 c_U(k)={e(k/(2U))\over U\cos(\pi k/U)},\qquad
 \sum_{k\bmod U}|c_U(k)|\ll\log(2U),\qquad
 \sum_{k\bmod U}|c_U(k)|^2=1.
\tag{187.K11}
\]

If (q=q_U(k)), then uniquely

\[
 k={U\over q}a,\qquad q\mid U,\qquad a\in\mathbb U(q),
\]

including (k=0) through (q=1,a=0), and

\[
 c_U(k)={q\over U}c_q(a),\qquad
 e(\epsilon_\omega k\bar vh/U)
 =e(\epsilon_\omega a\bar vh/q).
\tag{187.K12}
\]

Equations (187.K9)--(187.K12), followed only by the disjoint conditions
in (187.K3)--(187.K5), prove the exact identity (187.K1).

## 3. Literal counting and power ledger

The accepted literal support and multiplicity-one carrier give, for
fixed ((\kappa,g,h,U)),

\[
 \sum_{\omega,v,t}
 |B_{\mathfrak f,\omega}^\sigma(t)|
 \ll_\varepsilon LX^\varepsilon,
\tag{187.K13}
\]

as well as

\[
 U\ll {L\over\kappa g},\qquad
 \kappa g\ll {L\over h},
\tag{187.K14}
\]

and

\[
 \sum_{Y<h\le2Y}
 \sum_{\kappa g\ll L/h}1
 \ll L\log(2L).
\tag{187.K15}
\]

Thus the (U=1) block costs (O_\varepsilon(L^2X^\varepsilon)).

For the complete exact-conductor packet, put

\[
 u=gU,\qquad n=gh.
\]

On a live atom,

\[
 u,v\asymp {L\over\kappa},\qquad
 n\ll {L\over\kappa},
\]

so (h=n/g\ll U).  At fixed ((\kappa,u,U)), there are (O(U))
heights, (O(L/\kappa)) values of (v), and (O(\kappa)) live affine
sites per row.  Both orientations therefore contain (O(UL)) atoms.
For exact conductor (q), (187.K11)--(187.K12) give coefficient mass

\[
 {q\over U}
 \sum_{a\in\mathbb U(q)}|c_q(a)|
 \ll {q\over U}\log(2q).
\tag{187.K16}
\]

The fixed-((\kappa,u,U)) cost is consequently

\[
 O_\varepsilon(Lq\log(2q)X^\varepsilon).
\tag{187.K17}
\]

Since (q\mid U\mid u), elementary divisor summation yields

\[
 \begin{aligned}
 |\mathscr P_{Y,\le Q}^\sigma|
 &\ll_\varepsilon
 LQ\log(2Q)X^\varepsilon
 \sum_{\kappa\ll L}
 \sum_{u\asymp L/\kappa}\tau(u)^2\\
 &\ll_\varepsilon
 QL^2\{\log(2LQ)\}^{O(1)}X^\varepsilon
 \ll_{B,\varepsilon}L^2X^\varepsilon.
 \end{aligned}
\tag{187.K18}
\]

For (U\le4Q), (187.K11) costs (O(\log(2U))) per modulus.  For
(U>4Q) and (0<|k|_U\le Q),

\[
 \sum_{0<|k|_U\le Q}|c_U(k)|\ll {Q\over U}.
\tag{187.K19}
\]

Summing (187.K13)--(187.K15), first in (U), proves the third term of
(187.K6).  All factors (Q\) and all logarithms are absorbed by epsilon
rebudgeting because (Q=(\log(2X))^B+O(1)).

For the complement, the full Fourier mass in (187.K11), followed by
(U\ll L/(\kappa g)), gives

\[
 \begin{aligned}
 |\mathscr R_{Y,Q}^\sigma|
 &\ll_\varepsilon
 L^2\log(2L)X^\varepsilon
 \sum_{Y<h\le2Y}
 \sum_{\kappa g\ll L/h}{1\over\kappa g}\\
 &\ll_\varepsilon
 YL^2\{\log(2L)\}^{O(1)}X^\varepsilon,
 \end{aligned}
\]

which is (187.K7) after rebudgeting.  It does not prove (187.K8).

## 4. Exact centered-conductor self-return

For a unit (b\bmod q), define

\[
 K_q(b)=\sum_{a\in\mathbb U(q)}c_q(a)e(ab/q),\qquad
 K_q^\circ(b)=K_q(b)-{\mu(q)\over q}.
\tag{187.K20}
\]

Möbius inversion of (187.K12) gives

\[
 E_U(b)=\sum_{q\mid U}{q\over U}K_q(b),\qquad
 K_q(b)+K_q(-b)={2\mu(q)\over q}.
\tag{187.K21}
\]

Therefore (K_q^\circ(-b)=-K_q^\circ(b)), and for every odd (U>1)

\[
 E_U(b)A_+ +E_U(-b)A_-
 =\sum_{\substack{q\mid U\\q>1}}{q\over U}
 K_q^\circ(b)(A_+-A_-),
\tag{187.K22}
\]

because (sum_{q\mid U}\mu(q)=0).  For prime (U=p),

\[
 K_p^\circ(b)=E_p(b).
\tag{187.K23}
\]

Thus conductor centering is an exact rewriting, not an estimate: on a
prime modulus above (Q), the sole centered high conductor is literally
the original orientation block.

## 5. Positive-norm and false-control boundary

For odd (U>4Q), the two residues (k=(U\pm1)/2) lie in (187.K5),
have exact conductor (U), and satisfy

\[
 |c_U(k)|={1\over U\sin(\pi/(2U))}\ge {2\over\pi}.
\tag{187.K24}
\]

Hence the retained coefficient vector has

\[
 \sum_{\substack{q_U(k)>Q\\|k|_U>Q}}|c_U(k)|^2
 \ge {8\over\pi^2}.
\tag{187.K25}
\]

For arbitrary finite weights (W_j) with residues (a_j\bmod U),
put (F(k)=\sum_jW_je(ka_j/U)).  Then

\[
 \sum_{k\bmod U}c_U(k)F(k)=\sum_jE_U(a_j)W_j,
\]

and

\[
 \sum_{k\bmod U}|F(k)|^2
 =U\sum_{a\bmod U}
 \left|\sum_{j:a_j=a}W_j\right|^2.
\]

Positive Fourier, Poisson, or alias energy therefore reconstructs the
original signed block or its positive residue-bucket energy.  An
adversarial bounded coefficient can cancel the anchor, affine parity,
and phase and attain the full carrier capacity.  This is only a
coefficient-uniform mechanism control: it is not asserted realizable by
the literal Vaaler endpoint product and proves no literal lower mass.

## 6. First unproved step and downstream scope

The first unproved relation is exactly (187.K8), with every literal
field and both orientations retained under its single real part.  It
requires a new jointly signed property of the actual deleted endpoint
amplitude in ((h,v,t,k)) strong enough to recover the full factor (Y)
before any positive recombination.

Even a proof of (187.K8) closes only the exact original-(t=1) residual
through the accepted Round-184/185 connectors.  Every original
(t\ge2) small-(G) incidence, the large-(G) near-resonant
complement, the complete hard and smooth M1 parents, GAR, all M2
parents, endpoint uniformity, M9, both bridges, and the quarter target
remain open.

## 7. Dependencies and recommended state effect

Direct proof dependencies are:

- `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`;
- `Divisor-bound-elementary`.

The Mathematica exact Fourier check is diagnostic only and is not used
as theorem evidence.  Promote this candidate, after independent seam
review, as

`M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction`

with status `proved_internal`.  Add it only as an inconclusive
dependency of the still-open hard-M1 small-(t) residual owner.  Change
no complete owner, bridge, theorem, or exponent.
