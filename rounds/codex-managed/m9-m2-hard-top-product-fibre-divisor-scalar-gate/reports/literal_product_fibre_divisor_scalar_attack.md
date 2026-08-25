# Literal product-fibre divisor scalar attack: coherent fibres and reciprocal self-return

## 1. Result: product-fibre no-go

**Result (product_fibre_no_go).**  The nonsquare hard-TOP scalar has the
exact product-fibre form

\[
 \mathcal T_L^{\rm ns}
 =L^{3/2}\sum_{\substack{n\in\mathcal N_L\\n\ne\square}}
 n^{-3/4}C_L(n)e(J\sqrt n),
 \tag{137.D1}
\]

where

\[
 \begin{aligned}
 C_L(n)
 =\sum_{\substack{h\mid n,\ h\ {\rm odd}\\
                   \sqrt n\le h\le2\sqrt n}}
 &\chi_4(h)\eta_L(h)
 \Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xh^2}{4n}}\right).
 \end{aligned}
 \tag{137.D2}
\]

Every floor, half-open height support, hard affine face, endpoint value,
and real-centre parameter in (137.D2) is literal.  The map
\((h,m)\mapsto n=hm\) is a bijection between the original cone entries
and the divisor incidences in (137.D2).

This exact regrouping does not supply the missing factor \(L^{1/2}\).
There is no universal truncated-\(\chi_4\) cancellation inside a product
fibre.  Prime fibres may be empty; the nonsquare prime-power family

\[
 n=3^{2r+1},\qquad h=3^{r+1},\qquad m=3^r
 \tag{137.D3}
\]

has exactly one admissible divisor, whenever that height lies in the
literal block.  More generally, all retained divisors of an integer
whose odd prime factors are \(1\bmod4\) have the same character \(+1\).
Thus even a many-near-square-divisor fibre need not acquire any saving
from \(\chi_4\).

The one-dimensional phase does not repair this by itself.  On
\(n\asymp L^2\),

\[
 f'(n)\asymp\frac JL,\qquad |f''(n)|\asymp\frac J{L^3}.
\]

There are \(\asymp J/L\) stationary dual integers, each with natural
width \(L^{3/2}J^{-1/2}\).  Their coefficient-free B-process capacity is

\[
 \frac JL\cdot\frac{L^{3/2}}{\sqrt J}
 =\sqrt{JL}
 \asymp H\sqrt L
 =L^{3/2}\frac HL,
 \tag{137.D4}
\]

which is target-sized only at the already owned terminal scale
\(L\asymp H\), and loses \(H/L\) on a polynomial intermediate block.
Exact nonsquare stationary modes cannot be excluded uniformly in the
real centre: for any admissible nonsquare \(n_0\) and integer \(\nu\),
choosing \(X=4\nu^2n_0\) gives \(f'(n_0)=\nu\).

Divisor switching only transfers \(\chi_4\) to the complementary odd
divisor.  Completing (137.D2) to all odd divisors inserts
\(\sum_{d\mid n}\chi_4(d)=r_2(n)/4\) and leaves a complement of the same
uncontrolled type; the completed main term is a dyadic
Hardy--Voronoi/Gauss-circle radial block, not an easier input.
Finally, the legal interior B-process in the original \(m\)-variable
has stationary map

\[
 m_d=\frac{Xh}{4d^2},\qquad
 J\sqrt{hm_d}-dm_d=\frac{Xh}{4d},\qquad
 W\!\left(\sqrt{\frac{q_Xh}{4m_d}}\right)=W(d/y),
 \tag{137.D5}
\]

so it returns to the original hard reciprocal block.  A second
B-process sends \(d\) back to \(m\).  The actual character has exact
resonant dual modes, so this return creates no independent cancellation.

Consequently, fibrewise character cancellation, one-dimensional
curvature, divisor switching, full-divisor completion, and repeated
B-processes do not prove
\(\lvert\mathcal T_L^{\rm ns}\rvert\ll_\varepsilon
L^{3/2}X^\varepsilon\).  This is a method no-go, not a lower bound for
the literal scalar and not a disproof of the target.

## 2. Exact statement and hypotheses

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=\frac X{y^2},\qquad
 H=\lfloor yX^{-1/4}\rfloor,
 \tag{137.D6}
\]

and fix one literal polynomial intermediate block
\(1\ll L\ll H\).  Let \(\mathscr H_L\) be the exact finite odd support
of the half-open profile \(\eta_L\).  Define

\[
 V_{L,X}(h,m)
 =\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xh}{4m}}\right)
 \tag{137.D7}
\]

on

\[
 h\in\mathscr H_L,\qquad
 \lceil h/4\rceil\le m\le h,
 \tag{137.D8}
\]

and extend it by zero before every change of variables.  Then

\[
 a_{\rm end}(h,m)
 =\left(\frac{L^2}{hm}\right)^{3/4}V_{L,X}(h,m).
 \tag{137.D9}
\]

The square-entry scalar is already owned only through the proved matrix
projection and norm triangle:

\[
 |\mathcal T_L^\square|
 \ll_\varepsilon L^{5/4}X^\varepsilon.
 \tag{137.D10}
\]

No orthogonal energy decomposition is used.  The present report treats
only

\[
 \mathcal T_L^{\rm ns}
 =\sum_{\substack{h\in\mathscr H_L\\h\ {\rm odd}}}\chi_4(h)
   \sum_{\substack{\lceil h/4\rceil\le m\le h\\hm\ne\square}}
   a_{\rm end}(h,m)e(J\sqrt{hm}).
 \tag{137.D11}
\]

For an integer \(n\), set

\[
 \mathcal F_L(n)=
 \left\{h:\ h\mid n,\ h\in\mathscr H_L,\ h\ {\rm odd},\
              \sqrt n\le h\le2\sqrt n\right\}.
 \tag{137.D12}
\]

The actual product support is

\[
 \mathcal N_L=\{hm:\ h\in\mathscr H_L,\
                    \lceil h/4\rceil\le m\le h\},
 \tag{137.D13}
\]

with multiplicities retained in \(\mathcal F_L(n)\).  Equations
(137.D1)--(137.D2) are understood with these exact sets, rather than a
softened interval \(n\asymp L^2\).

The no-go statement is scoped as follows.  It rules out a closure based
only on:

1. cancellation of \(\chi_4\) separately inside each
   \(\mathcal F_L(n)\);
2. phase-derivative or B-process bounds that do not use a new theorem
   for the fixed sequence \(C_L(n)\);
3. switching to complementary divisors;
4. completing to \(r_2(n)/4\) and treating the completed radial block as
   already bounded; or
5. iterating the canonical reciprocal transform.

It does not rule out a new signed theorem coupling the literal
coefficients at distinct products \(n\) before an absolute value.

## 3. Proof and complete power ledger

**Exact product-fibre dictionary.**  For integer \(m\),

\[
 m\le h\quad\Longleftrightarrow\quad n=hm\le h^2
 \quad\Longleftrightarrow\quad h\ge\sqrt n.
 \]

Also,

\[
 m\ge\lceil h/4\rceil
 \quad\Longleftrightarrow\quad 4m\ge h
 \quad\Longleftrightarrow\quad h\le2\sqrt n.
 \]

Thus (137.D8) is equivalent, without moving an equality, to
\(h\in\mathcal F_L(n)\) and \(m=n/h\).  Conversely every such divisor
gives one integer \(m\) in (137.D8).  Since

\[
 \left(\frac{L^2}{hm}\right)^{3/4}
 =L^{3/2}n^{-3/4},
 \]

substitution proves (137.D1)--(137.D2).  The condition \(hm\ne\square\)
becomes exactly \(n\ne\square\), so the square projection is not
reintroduced.

**Literal coefficient controls.**  If \(n=p\) is prime and \(p>4\),
neither \(1\) nor \(p\) lies in
\([\sqrt p,2\sqrt p]\), so \(C_L(p)=0\).  This is support sparsity, not
character cancellation.

For \(n=3^{2r+1}\), the only power of \(3\) in
\([\sqrt n,2\sqrt n]\) is \(h=3^{r+1}\).  Its complement is
\(m=3^r\), so \(h/m=3\) lies strictly inside the hard cone.  Hence,
whenever the literal profiles do not vanish there,

\[
 C_L(3^{2r+1})
 =(-1)^{r+1}\eta_L(3^{r+1})
 \Phi\!\left(\frac{3^{r+1}}{H+1}\right)
 W\!\left(\sqrt{\frac{3q_X}{4}}\right).
 \tag{137.D14}
\]

There is no inner character sum.  In contrast,
\(3^{2r}\) is removed because it is a square.  For a prime power
\(p^{2r+1}\) with \(p\ge5\), the adjacent divisors straddle \(\sqrt n\)
by the factor \(\sqrt p>2\), so the hard fibre is empty.  These two
prime-power outcomes show that zero and nonzero fibres are decided by
the literal truncation, not by a uniform \(\chi_4\) identity.

Likewise, if \(n=pq\) for odd primes \(p<q<4p\), then the only divisor in
\([\sqrt n,2\sqrt n]\) is \(q\), and

\[
 C_L(pq)=\chi_4(q)\eta_L(q)
 \Phi\!\left(\frac q{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xq}{4p}}\right)
 \tag{137.D15}
\]

whenever \(q\in\mathscr H_L\).  Opposite choices
\(q\equiv1,3\bmod4\) give opposite signs but different products,
phases, and profile samples; no literal pairing follows.

At the other extreme, if every odd prime factor of \(n\) is
\(1\bmod4\), then \(\chi_4(h)=1\) for every retained divisor.  Thus on
any such many-near-square-divisor configuration the character is
coherent.  The varying profiles remain literal, but \(\chi_4\) itself
provides no cancellation.

**Complete \(L\)-power ledger.**  Put
\(r_L(n)=|\mathcal F_L(n)|\).  Boundedness of the fixed profiles and the
elementary divisor bound give

\[
 r_L(n)\le\tau(n)\ll_\varepsilon X^\varepsilon,\qquad
 \sum_n r_L(n)\ll L^2.
 \tag{137.D16}
\]

Consequently

\[
 \sum_n|C_L(n)|\ll L^2.
 \tag{137.D17}
\]

The literal multiplicative energy has the sharper elementary bound

\[
 \boxed{\sum_n|C_L(n)|^2\ll L^2\log(2L).}
 \tag{137.D18}
\]

Indeed, after expanding the square and dropping only signs, profiles,
and the nonsquare restriction for an upper bound, every equality
\(h_1m_1=h_2m_2\) has the unique parametrization

\[
 h_1=ga,\qquad h_2=gb,\qquad
 m_1=bt,\qquad m_2=at,\qquad (a,b)=1.
 \tag{137.D19}
\]

The odd-height condition makes \(g,a,b\) odd; \(t\) is unrestricted.
The two literal cone conditions give

\[
 \max\!\left(\frac a{4b},\frac b{4a}\right)
 \le\frac tg\le
 \min\!\left(\frac ab,\frac ba\right),
 \tag{137.D20}
\]

so \(1/2\le a/b\le2\).  The actual height support and cone also imply
\(ga,gb,at,bt\asymp L\).  Hence, for fixed comparable \(a,b\), there
are

\[
 O\!\left((1+L/a)^2\right)
\]

choices for \((g,t)\).  Summing first over
\(b\in[a/2,2a]\), and harmlessly dropping coprimality and oddness,
gives

\[
 \sum_{a\ll L}O(a)(1+L/a)^2
 \ll L^2\log(2L).
 \tag{137.D21}
\]

All half-open supports, ceilings, and actual profiles only restrict this
count.  Thus the bound is legal for the literal coefficient.  It gives
\(\|C_L\|_2\ll L\sqrt{\log(2L)}\); Cauchy over
\(O(L^2)\) products still returns
\(L^2\sqrt{\log(2L)}\), so it does not change the verdict.

| Item | Literal size or capacity |
|---|---:|
| active odd heights \(h\) | \(O(L)\) |
| admissible \(m\)'s per height | \(O(L)\) |
| total cone incidences \((h,m)\) | \(O(L^2)\) |
| ambient product values \(n\) | \(O(L^2)\) |
| one fibre \(r_L(n)\) | \(O_\varepsilon(X^\varepsilon)\) |
| normalized factor \(L^{3/2}n^{-3/4}\) | \(O(1)\) |
| raw scalar \(\ell^1\) capacity | \(L^{2+\varepsilon}\) |
| multiplicative energy \(\sum_n|C_L(n)|^2\) | \(O(L^2\log(2L))\) |
| coefficient \(\ell^2\) plus Cauchy | \(O(L^2\sqrt{\log(2L)})\) |
| removed square scalar | \(L^{5/4+\varepsilon}\) |
| required nonsquare scalar | \(L^{3/2+\varepsilon}\) |
| missing product-fibre gain | \(L^{1/2}\) |

The total variation of the zero-extended sequence
\[
 B_L(n)=L^{3/2}n^{-3/4}C_L(n)1_{n\ne\square}
\]
has only the full-capacity bound
\[
\operatorname{Var}(B_L)
 \le2\sum_n|B_L(n)|
 \ll_\varepsilon L^2X^\varepsilon.
 \tag{137.D22}
\]
Therefore Abel transfer of an unweighted square-root-phase estimate is
not lawful at target scale.

**Phase derivatives and dual resonances.**  On an actual product
interval \(I\asymp L^2\), let \(f(t)=J\sqrt t\).  The dual stationary
equation \(f'(t)=\nu\) gives

\[
 t_\nu=\frac{X}{4\nu^2},\qquad
 f(t_\nu)-\nu t_\nu=\frac{X}{4\nu}.
 \tag{137.D23}
\]

As \(t\) crosses \(I\), \(f'(t)\) crosses \(\asymp J/L\) integers.
Moreover

\[
 |f''(t_\nu)|^{-1/2}\asymp\frac{L^{3/2}}{\sqrt J}.
 \tag{137.D24}
\]

This proves the capacity (137.D4).  Equivalently, the elementary
second-derivative ledger is

\[
 |I|\sqrt{|f''|}+|f''|^{-1/2}
 \asymp\sqrt{JL}+\frac{L^{3/2}}{\sqrt J}.
 \tag{137.D25}
\]

Since \(H\asymp\sqrt J\) and \(L\ll H\), the first term exceeds the
target by \(H/L\).  This calculation is already optimistic: it has no
arithmetic coefficient.  Treating \(C_L(n)\) as an arbitrary bounded
coefficient cannot help, because the phase-conjugating array
\(b_n=e(-J\sqrt n)\) has \(L^2\) coherent capacity.  That array is a
method control, not the literal \(C_L(n)\).

The nonsquare restriction removes no uniform stationary family.  Given
an actual nonsquare \(n_0\), the real centres
\(X=4\nu^2n_0\) satisfy (137.D23) exactly at \(n_0\); taking \(\nu\)
large also places \(L\) strictly below \(H\).  Thus a proof uniform in
real \(X\) must retain stationary dual modes rather than discard them as
rare.

**Exact complementary-divisor switch.**  Write
\[
 n=2^\alpha n_{\rm o},\qquad n_{\rm o}\ {\rm odd},
 \]
and put \(r=n_{\rm o}/h\), so \(m=2^\alpha r\).  Multiplicativity and
\(\chi_4(r)^2=1\) give
\(\chi_4(h)=\chi_4(n_{\rm o})\chi_4(r)\).  Hence (137.D2) is exactly

\[
 \begin{aligned}
 C_L(n)=\chi_4(n_{\rm o})
 \sum_{\substack{r\mid n_{\rm o}\\
   \sqrt n/2^{\alpha+1}\le r\le\sqrt n/2^\alpha}}
 &\chi_4(r)\eta_L(n_{\rm o}/r)
 \Phi\!\left(\frac{n_{\rm o}/r}{H+1}\right)\\
 &\times
 W\!\left(\sqrt{\frac{q_Xn_{\rm o}^2}{4nr^2}}\right).
 \end{aligned}
 \tag{137.D26}
\]

Thus divisor switching preserves the same truncated divisor geometry
and merely moves the character to the complementary odd factor.

**Full-divisor completion.**  Extend
\[
 V_n(h)=1_{\sqrt n\le h\le2\sqrt n}\,
 \eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xh^2}{4n}}\right)
\]
by zero to every odd divisor of \(n\).  Then

\[
 C_L(n)=\frac{r_2(n)}4+
 \sum_{\substack{h\mid n\\h\ {\rm odd}}}
 \chi_4(h)\bigl(V_n(h)-1\bigr).
 \tag{137.D27}
\]

This is exact, but the second term contains every omitted divisor with
weight \(-1\), as well as every profile discrepancy on the retained
arc.  Completion gives no support reduction and no proved smaller norm;
any cancellation in this complement is a new unresolved estimate.
The first term contributes

\[
 \frac{L^{3/2}}4
 \sum_{\substack{n\asymp L^2\\n\ne\square}}
 r_2(n)n^{-3/4}e(J\sqrt n),
 \tag{137.D28}
\]

a dyadic classical radial block.  Using a target bound for (137.D28) as
the input would import the same Gauss-circle cancellation that this
program is meant to prove.  Completion therefore gives one circular
main term and one uncontrolled angular complement.

**Canonical B-process return.**  Fix \(h\) and write
\(\phi_h(m)=J\sqrt{hm}\).  On an interior smooth portion of the literal
\(m\)-interval,

\[
 \phi_h'(m)=\frac{J\sqrt h}{2\sqrt m}=d
 \quad\Longleftrightarrow\quad
 m=m_d=\frac{Xh}{4d^2}.
 \tag{137.D29}
\]

At this saddle,

\[
 \phi_h(m_d)-dm_d=\frac{Xh}{4d},\qquad
 |\phi_h''(m_d)|^{-1/2}
 =\sqrt{\frac{Xh}{2d^3}},
 \tag{137.D30}
\]

and

\[
 a_{\rm end}(h,m_d)|\phi_h''(m_d)|^{-1/2}
 =\frac{2L^{3/2}}{\sqrt J\,h}\eta_L(h)
  \Phi\!\left(\frac h{H+1}\right)W(d/y).
 \tag{137.D31}
\]

Thus the stationary principal term is, with the exact derivative range
and endpoint stars retained,

\[
 \frac{2e(-1/8)L^{3/2}}{\sqrt J}
 \sum_{\substack{h\in\mathscr H_L\\h\ {\rm odd}}}
 \frac{\chi_4(h)\eta_L(h)\Phi(h/(H+1))}{h}
 \sum_d^\star W(d/y)e\!\left(\frac{Xh}{4d}\right).
 \tag{137.D32}
\]

This is the original hard reciprocal M2 block, up to its already known
normalizing constant.  The equality
\(W(\sqrt{q_Xh/(4m_d)})=W(d/y)\) retains the real centre exactly.

Conversely, for \(\psi_h(d)=Xh/(4d)\), the dual mode \(-m\) has saddle

\[
 d_m=\frac{J\sqrt h}{2\sqrt m},\qquad
 \psi_h(d_m)+md_m=J\sqrt{hm},
 \tag{137.D33}
\]

and

\[
 W(d_m/y)=W\!\left(\sqrt{\frac{q_Xh}{4m}}\right).
 \tag{137.D34}
\]

The second B-process therefore returns coefficient-for-coefficient at
the canonical interior phase/profile level.

The character in (137.D32) is not automatically oscillatory:

\[
 \chi_4(h)e\!\left(\frac{Xh}{4d}\right)
 =-i\,e\!\left(\frac h4\left(\frac Xd+1\right)\right).
 \tag{137.D35}
\]

On consecutive odd heights the ratio is
\[
 e\!\left(\frac12\left(\frac Xd+1\right)\right).
 \tag{137.D36}
\]
It equals \(1\) whenever \(X/d\) is an odd integer.  In particular, at
the literal hard face \(X=y^2\) with \(y\) odd and \(d=y\),

\[
 \chi_4(h)e(yh/4)=i\chi_4(y)
 \tag{137.D37}
\]

is independent of \(h\).  At natural width \(1/L\), the reciprocal
range has \(J/L\) near-resonant mode capacity; multiplying this by the
single-mode scale \(L^{3/2}/\sqrt J\) again gives (137.D4).  Hence the
actual character, resonant modes, and self-return reproduce the known
deficit rather than remove it.

## 4. First doubtful or unproved step

The first failed step is the proposed inference that the truncated
divisor coefficient itself has a uniform square-root saving.  Neither

\[
 |C_L(n)|\ll r_L(n)^{1/2}
\]

nor any useful signed average over one fibre follows from \(\chi_4\):
(137.D14)--(137.D15) exhibit literal singleton fibres, while
all-\(1\bmod4\) divisor configurations are character-coherent.  The
periodic partial sums of \(\chi_4\) over consecutive integers do not
apply to the irregular divisor subset \(\mathcal F_L(n)\).

The next unlawful step would be to insert \(C_L(n)\) into a smooth
one-dimensional B-process.  The valid multiplicative energy
(137.D18) still gives only \(L^2\sqrt{\log(2L)}\) after Cauchy, while
the available variation bound (137.D22) has full \(L^2\) capacity.
Expanding the divisibility before transforming gives the stationary
ledger (137.D29)--(137.D32), ending in the original reciprocal hard
block; transforming again through (137.D33)--(137.D34) returns the
original cone.

Therefore the first genuinely new estimate would have to couple the
fixed literal values \(C_L(n)\) at distinct nonsquare products with the
square-root phase, while retaining every profile and the real centre:

\[
 \left|
 \sum_{\substack{n\in\mathcal N_L\\n\ne\square}}
 L^{3/2}n^{-3/4}C_L(n)e(J\sqrt n)
 \right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
 \tag{137.D38}
\]

Equation (137.D38) is the original target, not a strict smaller
survivor.  A complete finite B-process across the hard face would also
need an endpoint, star, floor, and remainder ledger; none is asserted
here.  That later owner issue does not rescue the proposed mechanism,
because its stationary interior already self-returns at the wrong
capacity.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| literal_hard_cone_and_square_projection | **Pass.** Equations (137.D7)--(137.D13) retain the literal cone and remove \(hm=\square\) only through the proved scalar projection. No orthogonal energy split is used. |
| exact_product_fibre_bijection | **Pass.** The integer ceiling is exactly equivalent to \(\sqrt n\le h\le2\sqrt n\), and \(m=n/h\) is unique. |
| truncated_chi4_divisor_coefficient | **Pass as a dictionary; fails as an automatic gain.** Equations (137.D14)--(137.D15) give singleton nonsquare fibres, while all-\(1\bmod4\) divisors are coherent. |
| hard_profile_floor_and_real_centre | **Pass.** The half-open \(\eta_L\), \(\Phi(h/(H+1))\), \(y=\lfloor J\rfloor\), \(q_X=X/y^2\), ceiling, and exact \(W\)-argument remain in every formula. |
| nonsquare_and_full_divisor_controls | **Pass with obstruction.** Prime fibres can be empty, \(3^{2r+1}\) gives a singleton, squares remain excluded, and (137.D27) separates the circular \(r_2/4\) completion from an uncontrolled complement. |
| phase_derivatives_and_resonant_dual_modes | **Exact obstruction.** Equations (137.D23)--(137.D25) give \(J/L\) stationary modes and \(\sqrt{JL}\) capacity. Real centres \(X=4\nu^2n_0\) give exact nonsquare stationary modes. |
| multiplicative_energy | **Pass, but no closure.** The literal cone parametrization (137.D19)--(137.D21) proves (137.D18), including all profile restrictions. Cauchy still gives \(O(L^2\sqrt{\log(2L)})\), above the \(L^{3/2+\varepsilon}\) target. |
| one_dimensional_scalar_capacity | **Failed closure.** Raw \(\ell^1\), coefficient \(\ell^2\) plus Cauchy, and total variation all remain at least \(L^{2}\) up to logarithms and \(X^\varepsilon\); the target is \(L^{3/2+\varepsilon}\). |
| completion_bprocess_and_self_return | **No gain.** Complementary-divisor switching is (137.D26); full completion is circular by (137.D27)--(137.D28); the two canonical B-processes (137.D29)--(137.D34) self-return. |
| coefficient_directionality_and_phase_alignment | **Pass as a method control only.** Phase-conjugating coefficients show coefficient-uniform derivative estimates are impossible, but they are not a lower bound for the literal \(C_L(n)\). Opposite character fibres have no profile- and phase-preserving pairing. |
| uniformity_in_L_and_X | **Failed for the proposed phase mechanism.** The B-process gap is \(H/L\) on every polynomial intermediate \(L\ll H\). Exact and near resonances occur for allowed real centres; no rationality of \(q_X\) is assumed. |
| boundary_and_owner_scope | **Pass.** The hard face, endpoint star, support crossings, floors, and square owner are not absorbed into the stationary principal term. No boundary or remainder is reclaimed. |
| full_hard_TOP_and_downstream_scope | **Pass.** The result concerns only the nonsquare polynomial intermediate hard-TOP scalar. It proves no complete hard TOP, BAL, UNBAL, M9-M2, M9-M1, endpoint assembly, M9, quarter theorem, or exponent change. |

The requested special configurations therefore have exact outcomes:
prime products may give one signed divisor; odd \(3\)-power products give
the infinite singleton family (137.D14); many near-square divisors can
be character-coherent; square products stay in the proved projection;
near-integral derivatives and stationary dual modes persist; and the
hard-face mode (137.D37) is exactly aligned.

## 6. Dependencies and exact artifacts used

This report used only the permitted Round-137 context:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/conductor_0823_full_proof_strategy.md;
- rounds/codex-managed/m9-top-endpoint-transform/synthesis.md;
- rounds/codex-managed/m9-m2-top-endpoint-affine-cone/synthesis.md;
- rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/blind_statement.md;
- rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/synthesis.md;
- rounds/codex-managed/full-proof-frontier-inequality-selection-gate/synthesis.md;
- rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/blind_statement.md; and
- the generated discovery brief for this task.

No Round-137 sibling report, web source, numerical experiment,
computation, or unstated external estimate was used.  All reasoning is
algebraic or analytic.  The accepted square-entry estimate and the
classical full-divisor identity are used only in their stated
directions.

## 7. Recommended state effect

Recommend **retain both target obligations as open** and record this
candidate under **product_fibre_no_go** after independent seam review.
The exact product-fibre dictionary (137.D1)--(137.D2), the
complementary-divisor self-switch (137.D26), the stationary capacity
(137.D4), and the canonical reciprocal return
(137.D29)--(137.D34) are suitable scoped facts.

Do not promote the hard-TOP target.  In particular, do not replace the
truncated coefficient by \(r_2(n)/4\), claim square-root cancellation
inside a divisor fibre, discard resonant dual modes, or count a repeated
B-process as a gain.  A continuation must prove a new fixed-direction
signed inequality for the exact \(C_L(n)\) across distinct nonsquare
products before any fibrewise modulus, coefficient-uniform norm, or full
divisor completion.

No status change is licensed for
M9-M2-top-endpoint-density-discrepancy-energy,
M9-M2-top-endpoint-signed-cone, complete M9-M2, endpoint uniformity, M9,
the quarter theorem, or any global exponent.
