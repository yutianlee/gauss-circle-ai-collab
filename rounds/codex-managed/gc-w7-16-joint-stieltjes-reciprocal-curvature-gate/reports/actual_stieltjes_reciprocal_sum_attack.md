# Round 129 report: the actual Stieltjes thresholds admit a direct reciprocal-curvature bound

Campaign: `gc-w7-16-joint-stieltjes-reciprocal-curvature-gate`
Task: `actual_stieltjes_reciprocal_sum_attack`
Role: discovery
Starting graph SHA-256:
`476b1445ef73d86627fd87de8bd2dd76a5efa53564a5b195230f2ad33ba2bbe8`

## 1. Result

The exact character-split physical family satisfies a direct theorem which
is numerically stronger than the open norm-homogeneous inequality.  The
proof does not apply generic partial summation to the completed coefficient.
It first keeps one Stieltjes threshold, uses the common lift character before
a modulus, and partitions the reciprocal variable into the literal plateaux
of that same threshold.

Put

\[
 \Lambda_\rho=\lambda_B\rho^2,
 \qquad N_\rho\asymp {Q_B\over\rho},
 \qquad
 K_\rho=
 \min\!\left(N_\rho,
 N_\rho\sqrt{\Lambda_\rho}+\Lambda_\rho^{-1/2}\right).
 \tag{129.1}
\]

For each of the two exact M1 branches and the single M2 branch, for every
literal clipped interval and every divisor progression, the actual sum obeys

\[
 \boxed{
 \left|\sum_{v\in I}^{*}U_{i,\rho,\eta}(v)
 e\!\left(-{ca'\over\kappa_i\rho v}
          +\vartheta_{i,\eta}\rho v\right)\right|
 \ll_\varepsilon {K_\rho\over L}Y^\varepsilon .}
 \tag{129.2}
\]

Here

\[
 \vartheta_{1,+}={1\over4},\qquad
 \vartheta_{1,-}=-{1\over4},\qquad
 \vartheta_{2,0}=0,
 \qquad \kappa_1=1,\quad\kappa_2=4.
 \tag{129.3}
\]

Thus (129.2) certainly implies the numerical consequence requested in the
Round-128 connector,

\[
 |S_{i,\rho,\eta}(I)|
 \ll_\varepsilon {J_B^{1/2}\over L}K_\rho Y^\varepsilon,
 \qquad J_B=1+{DQ_B\over B^2},
 \tag{129.4}
\]

without an extra \(N_\rho^{1/2}\).  The gain comes from a scale identity
which is invisible to generic \(V^2\) duality.  If
\(J_{0,B}=J_B-1=DQ_B/B^2\), then

\[
 {N_\rho\Lambda_\rho\over J_{0,B}}
 \asymp L\rho,
 \qquad
 N_\rho\Lambda_\rho
 \asymp {Y\rho\over WB}\ge {D\over W}=Y^{1/16}.
 \tag{129.5}
\]

For one threshold, there are \(O(J_B)\) plateaux.  Weighted
second-derivative summation on all of them costs

\[
 {1\over L}\min\!\left(
 N_\rho,
 N_\rho\sqrt{\Lambda_\rho}
       +J_B\Lambda_\rho^{-1/2}\right).
 \tag{129.6}
\]

In the nontrivial curvature case, (129.5) absorbs the second term in the
first; in the other case the trivial branch is exactly \(N_\rho/L\).
The exact discrete Stieltjes coefficients have bounded total mass, so
Minkowski over the thresholds preserves (129.2).

The only atom separated from the plateau formula is the literal inner
star/equality term.  Relative to a weak face it is exactly

\[
 \begin{aligned}
 \mathcal R_{i,\rho,\eta}^{*}
 ={}&\sum_t c_{i,t}
 \sum_{\substack{v\in I:\ \rho v\mid t}}
 \sigma_{i,t,v}^{*}\,\zeta_{i,\rho,\eta}
 T_i(v)
 {\chi_4(g_{t,v})\over g_{t,v}}P_{i,a'}(g_{t,v})
 e\!\left(-{ca'\over\kappa_i\rho v}
          +\vartheta_{i,\eta}\rho v\right),\\
 &g_{t,v}={t\over\rho v},
 \qquad |\sigma_{i,t,v}^{*}|\le1.
 \end{aligned}
 \tag{129.7}
\]

For a half-star, \(\sigma^*=-1/2\); for the weak convention it is zero;
and for a strict face relative to the weak convention it is \(-1\).
The divisor bound and character-Abel scale give

\[
 |\mathcal R_{i,\rho,\eta}^{*}|
 \ll_\varepsilon {Y^\varepsilon\over L}.
 \tag{129.8}
\]

There is no unpriced floor or derivative residual.

Using only the already audited Round-127 outer ledger and weakening
(129.2) to (129.4) gives the complete shell estimate

\[
 |\mathfrak O_{i,B}|
 \ll_\varepsilon
 D J_B^{1/2}
 \min\!\left(Q_B,
 Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\right)Y^\varepsilon,
 \tag{129.9}
\]

and hence the strict complete fixed-block bound
\(Y^{73/96+\varepsilon}\).  If the identical outer counting interface is
applied directly to the stronger (129.2), it gives the sharper candidate

\[
 |\mathfrak O_{i,B}|
 \ll_\varepsilon
 D\min\!\left(Q_B,
 Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\right)Y^\varepsilon
 \ll_\varepsilon Y^{35/48+\varepsilon}
 \tag{129.10}
\]

for every \(B\)-shell.  Equation (129.10) uses no new analytic estimate,
but its complete cross-shell outer ledger should be conductor-audited
before promotion.  The conservative consequence (129.9) already passes
the frozen \(Y^{73/96}\) gate.

The stronger functional assertion

\[
 |S(U)|\ll \|U\|_{V^2(I)}K_\rho Y^\varepsilon
 \tag{129.11}
\]

is not proved.  The thresholdwise proof controls the physical sum by the
actual Stieltjes \(\ell^1\)-mass and the literal character prefix scale;
it does not replace those quantities by the possibly smaller norm of their
superposition.  Thus (129.2) is a direct actual-family theorem, not a
generic or norm-homogeneous \(V^2\) theorem.

## 2. Exact statement and hypotheses

Fix the critical block

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},
 \qquad {D\over L}\le B\le D,
 \tag{129.12}
\]

one literal M1 or M2 denominator-frequency block, one fixed moving-symbol
stratum, one frequency sign and M2 product-sign sector, one outer ray
\((a,b)\), one inner numerator \(a'\), and one half-open inner
reduced-denominator shell.  Set

\[
 G={D\over B},\qquad
 Q_B=\min\!\left(B,{BD\over WL}\right)={BD\over WL},
 \qquad
 J_B=1+{DQ_B\over B^2}.
 \tag{129.13}
\]

On the shell,

\[
 b'=\rho v\asymp B,qquad
 |a'|\asymp {LB\over D}={L\over G},qquad
 \rho\mid a',\qquad
 |I|\asymp N_\rho={Q_B\over\rho}.
 \tag{129.14}
\]

If a clipped literal interval is shorter, it is zero-extended inside a
reference interval of length comparable to \(Q_B/\rho\); this changes
only the two already-owned endpoint jumps of \(T_i\).  The estimate is
uniform for every divisor \(\rho\mid a'\).  In M1 the two additive
branches in (129.21) cancel pointwise when \(\rho v\) is even; in M2 the
fixed factor \(\chi_4(|a'|)\) already deletes even \(a'\).  Thus parity is
reconstructed by the exact branch algebra and is not inserted as a dense
indicator into the BV multiplier \(T_i\).

Before a norm, the accepted complete ray coefficients are

\[
 \begin{aligned}
 A_1(a,b)
 &=\chi_4(b)R_1(a,b),\\
 R_1(a,b)
 &={2\over\pi ia}
   \sum_{g\ge1}^{*}{\chi_4(g)\over g}
   \Phi_H(ga)v_L^{*}(g|a|)
   \omega_{1,D}^{*}(gb;c),\\[1mm]
 A_2(a,b)
 &=R_2(a,b),\\
 R_2(a,b)
 &=-{4\chi_4(|a|)\over\pi|a|}
   \sum_{g\ge1}^{*}{\chi_4(g)\over g}
   \Phi_H(ga)v_L^{*}(g|a|)
   \omega_{2,D}^{*}(gb;c).
 \end{aligned}
 \tag{129.15}
\]

All frequency floors and stars are contained in the zero-extended fixed
frequency factor

\[
 P_{i,a'}(g)=\Phi_H(ga')v_L^{*}(g|a'|),
 \tag{129.16}
\]

with the fixed literal variants absorbed into this notation.  It is
supported on \(g\asymp G\), and its zero extension has bounded supremum
plus sampled variation.  The exact denominator sample has the discrete
Stieltjes decomposition

\[
 c_{i,t}=\omega_{i,D}^{*}(t;c)-
         \omega_{i,D}^{*}(t+1;c),
 \qquad
 \omega_{i,D}^{*}(d;c)=\sum_{t\ge d}c_{i,t},
 \qquad
 \sum_t|c_{i,t}|\ll1.
 \tag{129.17}
\]

The indices in (129.17) satisfy \(t\asymp D\), including the two
zero-extension exits and the hard/star sample.  If conjugation is present
in the off-diagonal, it is absorbed into \(c_{i,t}\) and
\(P_{i,a'}\); the mass and BV assertions are unchanged.

For fixed outer data let \(T_i(v)\) be the exact zero-extended product of

\[
 \mathbf 1^{\rm literal}_{0<a\rho v-a'b<
                     \kappa_i b\rho v/W},
 \qquad
 1-{W(a\rho v-a'b)\over\kappa_i b\rho v},
 \qquad
 \mathbf 1^{\rm owner}_{\rho v\asymp B},
 \tag{129.18}
\]

and the literal cell, sign-sector, original-support, and cross-shell
faces.  On each of \(O(1)\) clipped intervals,

\[
 \|T_i\|_\infty+\operatorname {Var}T_i\ll1.
 \tag{129.19}
\]

After the nonprimitive extension and Möbius identity

\[
 \mathbf1_{(a',b')=1}
 =\sum_{\rho\mid a',\ \rho\mid b'}\mu(\rho),
 \tag{129.20}
\]

the reduced M1 character is split exactly before the amplitude is formed:

\[
 \chi_4(\rho v)
 ={e(\rho v/4)-e(-\rho v/4)\over2i}.
 \tag{129.21}
\]

With real literal profiles, the exact constants after conjugating
(129.15) are

\[
 \zeta_{1,\rho,+}={\mu(\rho)\over\pi a'},\qquad
 \zeta_{1,\rho,-}=-{\mu(\rho)\over\pi a'},\qquad
 \zeta_{2,\rho,0}=
 -{4\mu(\rho)\epsilon_{\rm sgn}\chi_4(|a'|)
    \over\pi|a'|}.
 \tag{129.22}
\]

For complex notation, conjugate the fixed factors in (129.22); only the
exact phase-independent constant changes.  Before any norm, every branch
sum is exactly

\[
 \boxed{
 \begin{aligned}
 S_{i,\rho,\eta}(I)
 ={}&\sum_{v\in I}^{*}
 \zeta_{i,\rho,\eta}T_i(v)
 \sum_t c_{i,t}
 \sum_{g\le t/(\rho v)}^{*}
 {\chi_4(g)\over g}P_{i,a'}(g)\\[-1mm]
 &\hspace{32mm}\times
 e\!\left(-{ca'\over\kappa_i\rho v}
          +\vartheta_{i,\eta}\rho v\right).
 \end{aligned}}
 \tag{129.23}
\]

This is the formula to which (129.2) applies.  No liftwise modulus, full
lift count, or arbitrary \(V^2\) amplitude occurs in the hypotheses.

For placement inside the determinant correlation, the exact outer
factorization is

\[
 \begin{aligned}
 \mathfrak O_{i,B}^{+}
 =\sum_{(a,b)}^{\rm literal}
 A_i(a,b)e\!\left({ca\over\kappa_i b}\right)
 \sum_{a'}^{\rm literal}
 \sum_{\rho\mid a'}
 \sum_{\eta\in\mathcal E_i}
 S_{i,\rho,\eta}^{(a,b,a',B)},
 \end{aligned}
 \tag{129.24}
\]

where \(\mathcal E_1=\{+,-\}\),
\(\mathcal E_2=\{0\}\), and all determinant restrictions and tapers in
the original one-sided sum are in \(T_i\).  Formula (129.24) follows from

\[
 e\!\left({c(ab'-a'b)\over\kappa_i bb'}\right)
 =e\!\left({ca\over\kappa_i b}\right)
  e\!\left(-{ca'\over\kappa_i b'}\right)
 \tag{129.25}
\]

and is written before any outside counting norm.
The real off-diagonal is \(2\Re\sum_B\mathfrak O_{i,B}^{+}\), with the
opposite orientation thereby retained rather than deleted.

## 3. Proof or derivation

### 3.1 Character cancellation is consumed before a modulus

Let

\[
 W_{i,a'}(g)={1\over g}P_{i,a'}(g).
 \tag{129.26}
\]

On \(g\asymp G\), the exact fixed frequency factor, its floors and star,
and \(1/g\) give

\[
 \sup_g|W_{i,a'}(g)|+
 \sum_g|W_{i,a'}(g+1)-W_{i,a'}(g)|
 \ll_\varepsilon {Y^\varepsilon\over G}.
 \tag{129.27}
\]

The partial sums of \(\chi_4\) have absolute value at most one.  Discrete
Abel summation, including a half endpoint if prescribed, therefore gives
for every integer \(M\)

\[
 \left|\zeta_{i,\rho,\eta}
 \sum_{g\le M}^{*}\chi_4(g)W_{i,a'}(g)\right|
 \ll_\varepsilon
 {Y^\varepsilon\over |a'|G}
 \ll_\varepsilon {Y^\varepsilon\over L}.
 \tag{129.28}
\]

This is the only place the common lift character is put into a modulus,
and it occurs after its complete interval cancellation.  A liftwise
triangle would give \(G/L\) and would invalidate everything below.

### 3.2 One threshold: exact plateau formula and birth phase

Fix \(t\) in (129.17) and define

\[
 M_t(v)=\left\lfloor {t\over\rho v}\right\rfloor,
 \qquad
 F_{i,t}(m)=\zeta_{i,\rho,\eta}
 \sum_{g\le m}\chi_4(g)W_{i,a'}(g).
 \tag{129.29}
\]

For the weak face, monotonicity of \(M_t\) gives the exact identity

\[
 S_{i,\rho,\eta,t}^{\rm wk}
 =c_{i,t}\sum_m F_{i,t}(m)
 \sum_{\substack{v\in I:\ M_t(v)=m}}^{*}
 T_i(v)e(f_{i,\rho,\eta}(v)),
 \tag{129.30}
\]

where

\[
 f_{i,\rho,\eta}(v)
 =-{ca'\over\kappa_i\rho v}
  +\vartheta_{i,\eta}\rho v.
 \tag{129.31}
\]

Each nonempty set in (129.30) is an integer interval, split only at the
\(O(1)\) literal faces already contained in \(T_i\).  Moreover

\[
 \begin{aligned}
 \#\{m:M_t(v)=m\text{ for some }v\in I\}
 &\le 2+|M_t(v_-)-M_t(v_+)|\\
 &\ll 1+{tQ_B\over B^2}
 \ll J_B.
 \end{aligned}
 \tag{129.32}
\]

The physical phase at an exact threshold birth \(t=\rho vg\) is

\[
 f_{i,\rho,\eta}\!\left({t\over\rho g}\right)
 =-{ca'g\over\kappa_i t}+{\vartheta_{i,\eta}t\over g}.
 \tag{129.33}
\]

Thus the birth character \(\chi_4(g)\), the reciprocal carrier, and the
M1 quarter phase remain on the same literal divisor point.  No
nonresonance assumption on (129.33) is made.

Changing (129.30) from weak to the prescribed strict/weak/star convention
gives exactly (129.7).  Indeed an exceptional sample occurs precisely
when \(t/(\rho v)\) is an integer.  For fixed \(t\), these are divisor
pairs \((\rho v,g)\) of \(t\); hence the pointwise consequence
\(|\zeta_{i,\rho,\eta}W_{i,a'}(g)|\ll L^{-1}Y^\varepsilon\) of
(129.27), together with the elementary divisor bound, gives

\[
 |\mathcal R_{i,\rho,\eta,t}^{*}|
 \ll_\varepsilon {|c_{i,t}|\over L}Y^\varepsilon.
 \tag{129.34}
\]

Summing (129.34) by (129.17) proves (129.8).  This explicitly prices the
only point at which a Fourier treatment of the floor would otherwise have
an endpoint ambiguity.

### 3.3 Reciprocal curvature and every stationary alias

On \(v\asymp B/\rho\),

\[
 \begin{aligned}
 f'_{i,\rho,\eta}(v)
 &={ca'\over\kappa_i\rho v^2}
   +\vartheta_{i,\eta}\rho,\\
 f''_{i,\rho,\eta}(v)
 &=-{2ca'\over\kappa_i\rho v^3},\\
 |f''_{i,\rho,\eta}(v)|
 &\asymp {Y|a'|\rho^2\over B^3}
 \asymp {YL\rho^2\over DB^2}
 =\Lambda_\rho.
 \end{aligned}
 \tag{129.35}
\]

The second derivative is monotone and has fixed sign on a sign sector.
Every discrete stationary alias is a solution of

\[
 {ca'\over\kappa_i\rho v^2}
 +\vartheta_{i,\eta}\rho=r,
 \qquad r\in\mathbb Z.
 \tag{129.36}
\]

For M1, (129.36) is the exact quarter-shifted lattice
\(r\mp\rho/4\); for M2 it is the unshifted lattice.  There is at most
one solution for each \(r\), including when \(a'<0\).  The weighted
second-derivative estimate is uniform across all these crossings, so no
alias is deleted or estimated by a first-derivative denominator.

If \(J\) is one plateau interval of length \(n_J\), (129.19) and
(129.35) give

\[
 \left|\sum_{v\in J}^{*}T_i(v)e(f_{i,\rho,\eta}(v))\right|
 \ll
 \min\!\left(n_J,
 n_J\sqrt{\Lambda_\rho}+\Lambda_\rho^{-1/2}\right).
 \tag{129.37}
\]

The outer endpoint stars in the \(v\)-sum are included in the weighted
form of (129.37).  Restricting a BV multiplier to a plateau adds only its
two displayed endpoint values, so it creates no unrecorded derivative
term.

By (129.28), (129.30), (129.32), and the fact that the plateau lengths
sum to at most \(N_\rho\),

\[
 |S_{i,\rho,\eta,t}^{\rm wk}|
 \ll_\varepsilon {|c_{i,t}|Y^\varepsilon\over L}
 \min\!\left(
 N_\rho,
 N_\rho\sqrt{\Lambda_\rho}
       +J_B\Lambda_\rho^{-1/2}\right).
 \tag{129.38}
\]

This is the exact weighted plateau sum requested by the gate.

### 3.4 The two curvature cases and the \(J_B-1\) seam

At the critical scales, the minimum in (129.13) is always its second
argument.  Put

\[
 J_{0,B}=J_B-1={DQ_B\over B^2}.
 \tag{129.39}
\]

Using \(D^2=Y\), one has the exact scale comparisons

\[
 \begin{aligned}
 {N_\rho\Lambda_\rho\over J_{0,B}}
 &\asymp
 { (Q_B/\rho)(YL\rho^2/(DB^2))
  \over DQ_B/B^2}
 ={YL\rho\over D^2}=L\rho,\\
 N_\rho\Lambda_\rho
 &\asymp {Y\rho\over WB}
 \ge {Y\over WD}={D\over W}=Y^{1/16}.
 \end{aligned}
 \tag{129.40}
\]

Equation (129.40) handles both possible sizes of \(J_{0,B}\).  If
\(J_{0,B}\ge1\), then
\(N_\rho\Lambda_\rho\gg L\rho J_{0,B}\gg J_B\).  If
\(J_{0,B}<1\), then \(J_B\asymp1\) while the second line of (129.40)
still gives \(N_\rho\Lambda_\rho\gg1\).  Consequently, uniformly on
every shell and progression,

\[
 J_B\Lambda_\rho^{-1/2}
 \ll N_\rho\sqrt{\Lambda_\rho}.
 \tag{129.41}
\]

Now there are exactly two cases.

1. If
   \(K_\rho=N_\rho\), use the first branch of (129.38).  It gives
   \(|S_t^{\rm wk}|\ll |c_{i,t}|K_\rho L^{-1}Y^\varepsilon\).

2. If
   \(K_\rho=N_\rho\sqrt{\Lambda_\rho}
       +\Lambda_\rho^{-1/2}<N_\rho\), use the second branch of
   (129.38).  Equation (129.41) makes it
   \[
    |S_t^{\rm wk}|
    \ll_\varepsilon {|c_{i,t}|Y^\varepsilon\over L}
       N_\rho\sqrt{\Lambda_\rho}
    \ll {|c_{i,t}|K_\rho\over L}Y^\varepsilon.
   \]

The equality/star residual (129.34) is also absorbed because
\(K_\rho\gg1\); this follows already from (129.40), or from
\(N\sqrt\Lambda+\Lambda^{-1/2}\ge2\sqrt N\) together with the
nonempty-window convention.  This proves the single-threshold form of
(129.2).

No \(N_\rho^{1/2}\) has appeared.  In particular, the generic
\(V^2\)-dual obstruction is bypassed by the literal plateau count and the
scale relation (129.40), not contradicted.

### 3.5 Threshold superposition and Möbius progressions

Return to the exact formula (129.23).  Minkowski is taken only over the
Stieltjes coefficients after the joint threshold sum has been estimated:

\[
 \begin{aligned}
 |S_{i,\rho,\eta}(I)|
 &\le \sum_t|c_{i,t}|
   \left|S_{i,\rho,\eta,t}(I)/c_{i,t}\right|\\
 &\ll_\varepsilon {K_\rho\over L}Y^\varepsilon
       \sum_t|c_{i,t}|
 \ll_\varepsilon {K_\rho\over L}Y^\varepsilon.
 \end{aligned}
 \tag{129.42}
\]

Thus no factor \(D\), \(G\), \(J_B\), or \(N_\rho^{1/2}\) is paid in
the threshold superposition.  The smooth profile, both zero-extension
exits, the hard top, and its star are all coefficients in the one exact
mass in (129.17); there is no continuous remainder.

For a divisor progression,

\[
 \begin{aligned}
 K_\rho
 &=\min\!\left({Q_B\over\rho},
 Q_B\sqrt{\lambda_B}+{1\over\rho\sqrt{\lambda_B}}\right)\\
 &\le
 \min\!\left(Q_B,
 Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\right)
 =:K_B.
 \end{aligned}
 \tag{129.43}
\]

The factors \(\mu(\rho)\) are already in (129.22).  Summing only after
(129.42), over \(\rho\mid a'\), costs
\(\tau(a')\ll_\varepsilon Y^\varepsilon\), and therefore

\[
 \sum_{\rho\mid a'}\sum_{\eta\in\mathcal E_i}
 |S_{i,\rho,\eta}(I)|
 \ll_\varepsilon {K_B\over L}Y^\varepsilon.
 \tag{129.44}
\]

There is no density heuristic, no parity deletion, and no hidden
\(\rho^{1/2}\).  In the M1 branch pair, even \(\rho v\) cancels by
(129.21); the separate estimates are uniform before that cancellation.

### 3.6 Outer ledger and shell-by-shell capacity

The accepted outer ledger behind the Round-127 connector has
\(O(LD)\) outer rays, \(O(L)\) inner numerator increments, outer
coefficient \(O(L^{-1})\), and inner coefficient scale
\(O(L^{-1})\).  Using the deliberately weakened (129.4) in the exact
outer formula (129.24) gives

\[
 (LD)\cdot L\cdot L^{-1}\cdot
 {J_B^{1/2}K_B\over L}
 =D J_B^{1/2}K_B,
 \tag{129.45}
\]

which is (129.9).  Using (129.44) without weakening gives instead

\[
 (LD)\cdot L\cdot L^{-1}\cdot {K_B\over L}=DK_B.
 \tag{129.46}
\]

The equality/star residual in (129.8), after the same ledger, is
\(O_\varepsilon(DY^\varepsilon)=O_\varepsilon(Y^{1/2+\varepsilon})\),
so it is target-safe even before curvature.  Every inner denominator has
one half-open \(B\)-shell owner; a \(Q_B\le B\) window meets only
\(O(1)\) adjacent shell faces, already included in \(T_i\).  The original
\(D\)-profile remains in (129.17), so no physical coefficient is counted
twice.

Write \(B=Y^b\), \(16/48\le b\le24/48\).  Then

\[
 \begin{aligned}
 Q_B&=Y^{b-5/48},\\
 \lambda_B&=Y^{32/48-2b},\\
 J_B&=1+Y^{19/48-b},\\
 Q_B\sqrt{\lambda_B}&=Y^{11/48},\\
 \lambda_B^{-1/2}&=Y^{b-16/48}\le Y^{8/48}.
 \end{aligned}
 \tag{129.47}
\]

Hence \(K_B\asymp Y^{11/48}\) on every allowed shell.  The complete
capacity ledger is

| Shell range | \(J_B\) scale | conservative \(D J_B^{1/2}K_B\) | direct \(DK_B\) | exact star residual |
|---|---:|---:|---:|---:|
| \(b=16/48\) | \(Y^{3/48}\) | \(Y^{73/96}\) | \(Y^{35/48}\) | \(Y^{1/2+\varepsilon}\) |
| \(16/48<b<19/48\) | \(Y^{19/48-b}\) | \(Y^{35/48+(19/48-b)/2}\) | \(Y^{35/48}\) | \(Y^{1/2+\varepsilon}\) |
| \(19/48\le b\le24/48\) | \(1\) | \(Y^{35/48}\) | \(Y^{35/48}\) | \(Y^{1/2+\varepsilon}\) |

The equal-ray diagonal is only \(D/L=Y^{1/3}\).  Summing logarithmically
many half-open shells preserves the worst conservative exponent
\(73/96\).  The direct column records the stronger consequence of the
same outer count; because that is a stronger complete cross-shell claim
than the frozen gate requested, it is marked for conductor seam audit
rather than silently promoted here.

The effective local power is \(\theta=0\) in (129.2), and it is at worst
\(\theta=1/2\) after weakening to the accepted connector.  Both are
strictly below the capacity stop \(\theta=2/3\).  An added
\(N_\rho^{1/2}\) would be a new factor and is absent from every line of
the ledger.

## 4. First doubtful or unproved step

The first unproved strengthening is the norm-homogeneous statement
(129.11).  The proof of (129.2) uses

\[
 \sum_t|c_{i,t}|
 \sup_M\left|zeta_{i,\rho,\eta}
       \sum_{g\le M}\chi_4(g)g^{-1}P_{i,a'}(g)\right|,
 \tag{129.48}
\]

whose physical size is \(O(L^{-1})\).  Minkowski proves that this
dominates the actual \(V^2\) norm, but there is no reverse inequality:
distinct Stieltjes thresholds can cancel inside \(U\).  Therefore this
argument cannot replace (129.48) by the possibly smaller
\(\|U\|_{V^2}\).  Generic \(V^2\) duality still has its known
\(N_\rho^{1/2}\) obstruction.

This doubt does not affect the direct actual-family estimate (129.2),
because (129.23) fixes the physical Stieltjes representation and
\(\sum|c_t|\ll1\).  It affects only the stronger abstract formulation of
the theorem.

At the determinant interface, (129.9) follows from the already audited
connector ledger.  The sharper replacement (129.10) is algebraically
suggested by exactly the same count, but it should receive an independent
outer-variable and cross-shell seam audit before graph promotion.  Even
(129.10) is \(Y^{11/48}\) above the desired \(Y^{1/2}\) determinant
bound.  No argument here closes that target.

## 5. Control tests and outcomes

| Required control | Exact test | Outcome |
|---|---|---|
| `branchwise_literal_dictionary` | Start from (129.15), perform (129.17), Möbius (129.20), and only then the exact M1 split (129.21). | **Pass.** Equations (129.22)--(129.24) retain both M1 branches, the M2 fixed character/sign, common lift character, factor four, and every outer phase. |
| `single_threshold_birth_phase` | Freeze \(t\), partition by \(M_t(v)\), and evaluate the carrier when \(t=\rho vg\). | **Pass.** The exact phase is (129.33), and the character factor remains on that divisor point. |
| `character_before_modulus` | Abel-sum the fixed sampled-BV lift factor against \(\chi_4(g)\). | **Pass.** Equation (129.28) is obtained before any lift modulus; an adversarial lift triangle would lose \(G\). |
| `M1_quarter_phase_aliases` | Solve (129.36) with \(\vartheta=\pm1/4\) for every divisor progression. | **Pass.** Both quarter-shifted integer lattices are included in the weighted second-derivative estimate; neither is declared nonstationary, and their pointwise sum reconstructs the zero even samples. |
| `reciprocal_second_derivative_and_stationary_lattice` | Differentiate the exact phase twice and retain all integer crossings. | **Pass.** Equation (129.35) gives \(\Lambda_\rho\), while (129.36)--(129.37) uniformly price every alias. |
| `threshold_superposition_and_Minkowski` | Apply the plateau estimate to one \(t\), then sum with the exact mass in (129.17). | **Pass.** Equation (129.42) costs no \(D,G,J_B\), or \(N_\rho^{1/2}\). |
| `V2_endpoint_terms` | Keep the first/last plateau values, outer starred endpoints, and inner equality atoms. | **Pass.** Weighted (129.37) includes the outer endpoints; the inner equality atom is exactly (129.7) and is bounded by (129.8). No endpoint is inferred from increments. |
| `mobius_progressions` | Prove (129.2) uniformly for each \(\rho\mid a'\), then sum divisors. | **Pass.** Equations (129.43)--(129.44) cost only \(Y^\varepsilon\), with no \(\rho^{1/2}\), parity heuristic, or density heuristic. |
| `floors_stars_taper_and_shell_owners` | Use the exact floor plateaux, display the equality residual, keep \(T_i\) BV, and use half-open \(B\)-owners. | **Pass.** Every term is in (129.23), (129.30), or the exact residual (129.7), and every inner denominator has one owner. |
| `N_rho_square_root_stop_rule` | Inspect (129.38)--(129.44) factor by factor. | **Pass.** The only count is \(J_B\Lambda^{-1/2}\), which is absorbed using (129.40); no \(N_\rho^{1/2}\) appears. |
| `theta_two_thirds_capacity_threshold` | Compare (129.45)--(129.47) with \(35/48+\theta/16\). | **Pass.** The direct theorem has \(\theta=0\); the conservative connector uses \(\theta=1/2<2/3\). |
| `no_exponent_or_M9_promotion` | Propagate only the fixed-block capacities and compare with the accepted persistence map. | **Pass.** The conservative persistence exponent is \(115/288>1/3\); even the possible complete \(35/48\) column gives \(7/18>1/3\). Neither improves the current theorem or touches M9. |

Two additional hostile controls also pass.

* **Generic \(V^2\) duality is not claimed.**  The proof explicitly stops
  at (129.48), so it does not contradict the phase-adapted generic
  countermodel or the Round-128 \(N_\rho^{1/2}\) warning.
* **Unsplit M1 is not reintroduced.**  The dense reduced character is
  wholly owned by (129.21) and (129.3).  The common lift character remains
  inside (129.28).  Reversing these ownership decisions would recover the
  literal \(Q_B^{1/2}/L\) obstruction.

All tests are analytical/algebraic.  No numerical experiment or external
theorem was used.

## 6. Dependencies and exact artifacts used

The graph facts used are the accepted statements and current scopes of:

* `GC-W7-16-reduced-Farey-cluster-reduction`, for the complete ray
  dictionary, exact determinant, outer coefficient scale, and owners;
* `GC-W7-16-original-numerator-product-window-bound`, for the current
  complete \(Y^{37/48}\) comparison;
* `GC-W7-16-bounded-lift-top-shell-curvature-saving`, for the weighted
  second-derivative normalization and top-shell outer interface;
* `GC-W7-16-local-lift-BV-threshold-V2-lemma`, for the exact discrete
  Stieltjes formula, literal coefficient BV masses, and branch ownership;
* `GC-W7-16-local-V2-normalization-obstruction`, to keep unsplit M1 and
  generic coefficient claims excluded;
* `GC-W7-16-local-transverse-square-variation-connector`, for the audited
  conservative outer ledger and capacity arithmetic; and
* `GC-W7-16-actual-reduced-determinant-correlation`, only to state the
  still-open \(Y^{1/2}\) target and its implication scope.

The exact permitted context artifacts read and used were:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reports/actual_rational_cluster_attack.md`;
5. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reports/actual_character_determinant_attack.md`;
6. `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/graded_determinant_long_lift_feasibility.md`;
7. `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/reports/literal_lift_coefficient_variation_attack.md`;
8. `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/reviews/conductor_round128_literal_v2_adjudication.md`; and
9. `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/synthesis.md`.

The derivation adds only the exact plateau identity (129.30), the
weighted per-plateau second-derivative sum (129.38), the scale comparison
(129.40), and the explicit equality residual (129.7).  No sibling
Round-129 report, computation, web source, or unlisted research artifact
was read or used.  The effort allocation was 100% analytical/algebraic.

## 7. Recommended state effect

**Promote after independent seam review** the direct actual-family
Stieltjes plateau lemma (129.2), with exact hypotheses (129.12)--(129.23)
and the equality residual (129.7)--(129.8).  Its proof must be recorded as
a thresholdwise theorem: common-character Abel first, reciprocal
curvature on the resulting floor plateaux second, and Stieltjes Minkowski
last.  It is not a generic \(V^2\) theorem.

**Promote after the existing outer ledger is rechecked** at least the
conservative complete-shell consequence (129.9) and the resulting
\(Y^{73/96+\varepsilon}\) complete fixed block.  The local proof is
actually strong enough for (129.10); the conductor should separately
audit whether the unchanged \(O(LD)\)-by-\(O(L)\) outer count and every
cross-shell owner transfer directly to that sharper \(DK_B\) statement.
Until that audit, retain \(Y^{35/48}\) as a candidate stronger
consequence rather than an accepted graph fact.

**Retain open** the norm-homogeneous assertion (129.11).  It is no longer
needed for the physical numerical shell bound, but it has not been proved
as stated because Stieltjes cancellation can make the norm of the summed
coefficient smaller than the thresholdwise Minkowski quantity.

**No change** is licensed for the \(Y^{1/2}\) actual determinant target,
the global pointwise exponent, M9-M1, M9-M2, endpoint uniformity, M9, the
conditional quarter bridge, or the Gauss-circle target.  Even the sharper
candidate fixed-block exponent \(35/48\) would persist only to \(7/18\),
which is worse than the already proved one-third theorem.
