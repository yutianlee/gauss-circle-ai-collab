Campaign: `m9-m1-beta-global-nonsaddle-signed-section`  
Task: `global_signed_section_attack`  
Role: discovery  
Allocation: 100% analytical/algebraic; no numerical experiment and no external theorem

# 1. Result

The global nonsaddle interface closes.  The appropriate normalization is
dyadic in the actual gamma height

\[
 R\asymp 1+|\alpha|,
\]

not in the stationary scale \(\lambda\).  On every such signed dyadic
cell, the complete phase-removed, after-Plemelj section satisfies

\[
 |\mathcal P|\ll P_XR^{\kappa-2},\qquad
 |\partial_L\mathcal P|\ll P_XR^{\kappa-3},       \tag{47.15}
\]

and its phase-conjugated logarithmic \(x\)-derivative satisfies

\[
 |\mathcal Q|\ll P_XR^{\kappa-1},\qquad
 |\partial_L\mathcal Q|\ll P_XR^{\kappa-2}.       \tag{47.16}
\]

Here derivatives are understood on each affine finite-section cell; the
corresponding moving traces have, on a dyadic \(L\)-cell, total sizes

\[
 O(P_XR^{\kappa-2})\quad\hbox{and}\quad
 O(P_XR^{\kappa-1})                                \tag{47.17}
\]

for \(\mathcal P\) and \(\mathcal Q\), respectively.  The estimates
hold uniformly in \(U,V\), in every actual index, in both signs of
\(\alpha\), and for all actual \(\lambda\).  The signed diagonal is
formed before absolute values.  It is strictly smaller than the bounds
in (47.15)--(47.16); the off-diagonal divided difference is the
power-determining term.

One \(L\)-integration by parts on the subordinate inner and outer
nonsaddle sectors gives, dyadically,

\[
 |I_R(x)|\ll P_XR^{\kappa-2},\qquad
 |x\partial_x I_R(x)|\ll P_XR^{\kappa-1}.          \tag{47.18}
\]

Both series converge because \(\kappa<1\).  For the inner sector the
sum is uniform as its upper endpoint grows with \(\lambda\); for the
outer sector it is
\(O(P_X\lambda^{\kappa-1})=O(P_X)\), since the actual scales have
\(\lambda\gg1\).  Consequently the complete normalized nonsaddle
amplitude obeys

\[
 \sup_{1\le x\le N_X}|\mathcal A_{\rm ns}(x)|
 +\int_1^{N_X}|\mathcal A_{\rm ns}'(x)|\,dx
 \ll \log^C(2X).                                   \tag{47.19}
\]

The exact radial-BV identity then gives a normalized
\(O(\log^C(2X))\) radial contribution, and the external physical
operator gives

\[
 \mathcal E_{\rm ns}(X)\ll X^{1/4}\log^C(2X).      \tag{47.20}
\]

There is also a cutoff-invariance corollary.  Any fixed finite smooth
middle partition supported in
\(2/3<|\alpha|/\lambda<3/2\), with its natural scaled seminorms, may be
inserted in the accepted Round-41 product-cell theorem.  In particular,
the repaired middle multipliers from Round 46 are covered exactly after
finite refinement into signed saddle/entry/exit pieces.  Literal
equality with a historical cutoff formula is unnecessary.

# 2. Exact statement and hypotheses

Assume all hypotheses and ownership conventions in the Round-47 packet.
In particular,

\[
 b={1\over\log(2X)},\quad 0\le a\le b,\quad
 \kappa={3\over4}+{a+b\over2}<1,
\]

\[
 \alpha=L+\beta,\qquad
 \eta={L+\nu\over2}+\beta,\qquad
 \lambda={\pi q\sqrt{Xx}\over D_j},               \tag{47.21}
\]

and \(\beta\) ranges in a fixed compact interval.  The height profile
\(p=p_{j,x}\) and its first three derivatives satisfy

\[
 |p^{(m)}(t)|\le P_X(1+|t|)^{-3},\qquad m\le3,
 \qquad P_X\ll\log^C(2X).                           \tag{47.22}
\]

All required finite seminorms of the smooth spatial profiles and masks
are bounded by \(P_X\).  The singular top is interpreted only through
the signed section (47.3), or equivalently through the exact diagonal
logarithm (47.5d) plus the divided difference (47.4).

Choose a smooth signed dyadic partition in \(1+|\alpha|\).  On a cell
\(J_R^\epsilon\), \(\epsilon\in\{+,-\}\), require

\[
 R\le 1+|\alpha|\le 2R,qquad \operatorname{sgn}\alpha=\epsilon,
                                                               \tag{47.23}
\]

with the bounded range treated as the first cell.  If \(R\) is large,
define

\[
 \mathcal G_R(L)=R^{-\kappa}e^{-i\Psi_\epsilon(L,x)}G(L),
                                                               \tag{47.24}
\]

where \(G\) is exactly (47.5a), except that the height factor \(p\) is
not included.  Uniform two-sided Stirling gives

\[
 |\partial_L^m\mathcal G_R(L)|\le P_XR^{-m},
 \qquad 0\le m\le2.                               \tag{47.25}
\]

For bounded \(R\), (47.25) means the corresponding uniform compact
bound.  This convention makes every occurrence of \(R^\kappa\) below
the actual gamma magnitude, not a stationary numerator.

Let \(m_{\rm ns}(L,x)\) be any one of the finite subordinate inner or
outer multipliers accepted in Round 46, including its sign and
preliminary-weight factors.  On a dyadic cell meeting its support,

\[
 |\partial_L^a(x\partial_x)^b m_{\rm ns}|
 \ll_{a,b}R^{-a},\qquad 0\le a\le2,\quad 0\le b\le1.       \tag{47.26}
\]

The only apparent exception is a derivative of the fixed \(\chi _0\)
collar; that collar has bounded \(R\), where (47.26) is again true.
The sign transition is contained in the zero set of \(1-\chi _0\).

The theorem asserts (47.15)--(47.20), the moving-face and exhaustion
claims below, and the following middle-cutoff statement.  If a finite
family \(m_k\) is supported where

\[
 c\lambda\le |\alpha|\le C\lambda
\]

for fixed \(0<c<C<\infty\), and

\[
 |\partial_L^a(x\partial_x)^b m_k|
 \le C_{a,b}\lambda^{-a},                          \tag{47.27}
\]

then multiplication by \(m_k\) preserves every hypothesis and every
conclusion of the accepted Round-41 product-cell theorem.  Hence any
finite one-count replacement of its fixed-ratio cutoff family gives the
same target bound.

# 3. Proof or derivation

### 3.1 Global gamma symbol on both signs

The numerator and denominator in \(R_\alpha\) have the same exponential
Stirling factor.  Their real-part difference is exactly

\[
 {1+\sigma+\zeta/2\over2}
 -{2-\sigma-\zeta/2\over2}
 =\sigma+{\zeta\over2}-{1\over2}=\kappa.           \tag{47.28}
\]

Uniform Stirling on either half-ray, with the exact elementary phase in
\(G\) retained, therefore gives

\[
 e^{-i\Psi_\epsilon(L,x)}G(L)
 =C_\epsilon(\beta,h,q,x)|\alpha|^\kappa
   \{1+O(|\alpha|^{-1})\},                         \tag{47.29}
\]

with the differentiated remainder of order
\(O(|\alpha|^{-1-m})\).  The fixed beta factors cost only \(P_X\).
Equation (47.25) follows on (47.23).  The argument is identical on the
negative half-ray; the phase and the sign of \(\Psi''=1/\alpha\) change,
but none of the magnitude estimates changes.  Compact \(|\alpha|\) is
covered directly because all gamma arguments stay in a fixed
pole-free set.

### 3.2 Off-diagonal section and the exact x numerator

Put

\[
 y=L-\nu,qquad
 D=-1-{b\over2}-i\left({L+\nu\over2}+\beta\right),
\]

\[
 E_0(L,\nu)={p(\nu)-p(L)\over y},qquad
 E_1(L,\nu)=
 {p(L)-p(\nu)-p'(L)y\over y^2}.                   \tag{47.30}
\]

Both quotients have their continuous diagonal values.  At fixed
physical \(\nu\), \(\partial_LE_0=E_1\).  The four separated centers
are the physical center \(\nu=0\), the top diagonal \(\nu=L\), the
radial ridge \(L+\nu+2\beta=0\), and their complement.  Since
\(|L|\asymp R\) on a large dyadic cell, the exact endpoint-quotient
calculus gives

\[
 \int_{\mathbb R}{|E_0|\over|D|}\,d\nu\ll P_XR^{-2},
 \quad
 \int_{\mathbb R}{|E_1|\over|D|}\,d\nu\ll P_XR^{-3},
 \quad
 \int_{\mathbb R}{|E_0|\over|D|^2}\,d\nu\ll P_XR^{-3}.
                                                               \tag{47.31}
\]

For clarity, near \(\nu=0\), both \(|y|\) and \(|D|\) are
\(\asymp R\), and (47.22) is integrated in \(L^1\).  Near \(\nu=L\),
the Taylor segments in (47.30) stay at height \(\asymp R\).  Near the
radial ridge, \(|y|\asymp R\), both endpoint profile values are
\(O(P_XR^{-3})\), and the sole \(|D|^{-1}\) integral costs a logarithm,
which is harmless in \(P_X\).  In the complement one uses the endpoint
forms in (47.30), not separate absolute long-translation integrals.
This proves (47.31) and is valid on both signed cells.

With \(\mathcal G_R\) from (47.24), the normalized off-diagonal section
and its fixed-height derivative are

\[
 \mathcal P_{\Delta,R}
 =\mathcal G_R\int_{I_{U,V}(L)}{E_0\over D}\,d\nu,
\]

\[
 \partial_L\mathcal P_{\Delta,R}
 =\mathcal G_R'\int{E_0\over D}\,d\nu
 +\mathcal G_R\int\left\{{E_1\over D}
                  +{iE_0\over2D^2}\right\}d\nu,              \tag{47.32}
\]

apart from the endpoint traces treated below.  Thus

\[
 |\mathcal P_{\Delta,R}|\ll P_XR^{-2},\qquad
 |\partial_L\mathcal P_{\Delta,R}|\ll P_XR^{-3}.              \tag{47.33}
\]

The x derivative must not be obtained by differentiating the two
endpoint values separately and discarding their common phase.  Equations
(47.5b) give the exact recombined numerator

\[
 E_x(L,\nu)
 ={\eta p(\nu)-\alpha p(L)\over y}
 =\alpha E_0(L,\nu)-{1\over2}p(\nu),              \tag{47.34}
\]

and, still at fixed \(\nu\),

\[
 \partial_LE_x=E_0+\alpha E_1.                    \tag{47.35}
\]

The elementary separated-center convolutions

\[
 \int{(1+|\nu|)^{-3}\over|D|}\,d\nu\ll R^{-1},
 \qquad
 \int{(1+|\nu|)^{-3}\over|D|^2}\,d\nu\ll R^{-2}             \tag{47.36}
\]

together with (47.31) imply

\[
 \int{|E_x|\over|D|}\,d\nu\ll P_XR^{-1},
 \quad
 \int{|\partial_LE_x|\over|D|}\,d\nu\ll P_XR^{-2},
 \quad
 \int{|E_x|\over|D|^2}\,d\nu\ll P_XR^{-2}.       \tag{47.37}
\]

Consequently the normalized phase-conjugated x section obeys

\[
 |\mathcal Q_{\Delta,R}|\ll P_XR^{-1},\qquad
 |\partial_L\mathcal Q_{\Delta,R}|\ll P_XR^{-2}.              \tag{47.38}
\]

Restoring the actual gamma magnitude \(R^\kappa\) proves the
off-diagonal parts of (47.15)--(47.16).

### 3.3 Signed diagonal, smooth shares, and moving faces

Write

\[
 \ell_{U,V}(L)=
 \Log D(L,q_{U,V}(L))-\Log D(L,p_{U,V}(L)).         \tag{47.39}
\]

The diagonal section is exactly

\[
 C_{U,V}[H](L)={G(L)p(L)\over A(L)}\ell_{U,V}(L)   \tag{47.40}
\]

before phase removal.  No absolute value has been taken before this
identity.  Uniformly in \(U,V\),

\[
 |\ell_{U,V}(L)|\ll\log(2+R),qquad
 |\ell_{U,V}'(L)|\ll1                              \tag{47.41}
\]

on every affine cell.  To verify the first assertion, choose the endpoint
for which \(|(L+\nu)/2+\beta|\) is smaller.  If that endpoint is
\(-V,V,L-U\), or \(L+U\), the intersection formula (47.5c) gives,
in each case,

\[
 q_{U,V}-p_{U,V}
 \ll R+\min_{\nu=p_{U,V},q_{U,V}}
       \left|{L+\nu\over2}+\beta\right|.
\]

Thus the moduli of the two left-half-plane logarithm arguments have
ratio \(O(R)\); their argument difference is bounded.  The derivative
claim follows because an endpoint has velocity zero or one and
\(|D|\ge1+b/2\).  The two affine formulae agree at each switch, and the
logarithm difference is zero when the section collapses.

Now

\[
 \left|R^{-\kappa}e^{-i\Psi}{G(L)p(L)\over A(L)}\right|
 \ll P_XR^{-4}.
\]

Its \(L\)-derivative is \(O(P_XR^{-4})\), with logarithmic scale phases
absorbed into \(P_X\).  Hence the normalized diagonal contribution is

\[
 |\mathcal P_{C,R}|\ll P_XR^{-4}\log(2+R),
 \quad
 |\partial_L\mathcal P_{C,R}|\ll P_XR^{-4}\log(2+R),        \tag{47.42}
\]

and its x derivative, whose exact multiplier is \(\alpha\), is

\[
 |\mathcal Q_{C,R}|\ll P_XR^{-3}\log(2+R),
 \quad
 |\partial_L\mathcal Q_{C,R}|\ll P_XR^{-3}\log(2+R).        \tag{47.43}
\]

These are stronger than the required powers.  Under symmetric
exhaustion, (47.5e) gives

\[
 C_{T,T}[H](L)\longrightarrow i\pi {G(L)p(L)\over A(L)},
\]

and (47.41)--(47.43) justify the limit on every dyadic cell.

For a smooth share, rapid decay of \(W(y)\) and cubic decay of
\(p(L-y)\) give, after the same \(R^{-\kappa}\) phase removal,

\[
 |\mathcal P_{W,R}|+|\partial_L\mathcal P_{W,R}|
 \ll P_XR^{-4},                                    \tag{47.44}
\]

and insertion of the exact x multiplier
\(\eta=\alpha-y/2\) gives

\[
 |\mathcal Q_{W,R}|+|\partial_L\mathcal Q_{W,R}|
 \ll P_XR^{-3}.                                    \tag{47.45}
\]

At a moving face \(\nu=L-c\), \(c=\pm U\), the singular quotient is
the continuous expression

\[
 {p(L-c)-p(L)\over c}.
\]

The separated-center argument from (47.31) gives, on \(J_R^\epsilon\),

\[
 \int_{J_R^\epsilon}
 \left|\mathcal G_R{p(L-c)-p(L)\over cD(L,L-c)}\right|dL
 \ll P_XR^{-2}.                                    \tag{47.46}
\]

For the x trace, keep

\[
 {(L-c/2+\beta)p(L-c)-(L+\beta)p(L)\over cD(L,L-c)}.          \tag{47.47}
\]

If \(|c|\ll R\), the mean-value segment stays in the cubic tail.  If
\(|c|\gg R\), the first endpoint is bounded using
\(|L-c/2+\beta|/|D(L,L-c)|\ll1\), while the other endpoint has cubic
decay.  This proves the uniform trace bound

\[
 \int_{J_R^\epsilon}|\mathcal Q_{\Delta,R}(L,L-c)|\,dL
 \ll P_XR^{-1}.                                    \tag{47.48}
\]

Smooth traces are better because of \(W(c)\).  Equations
(47.41)--(47.43) already contain the diagonal face terms.  Therefore
upper faces enter with the positive Leibniz sign, lower faces with the
negative sign, fixed faces have zero speed, switch values agree, and a
collapsed section contributes zero.  Multiplication by \(R^\kappa\)
gives (47.17).  As \(U,V\) exhaust symmetrically, off-diagonal faces
vanish like endpoint divided differences, smooth faces vanish by rapid
profile decay, and the diagonal converges to (47.5e).

### 3.4 Nonsaddle phase integration and outer limits

Multiplication by \(m_{\rm ns}\) preserves (47.15)--(47.17) by
(47.26).  Moreover

\[
 e^{-i\Psi}x\partial_x\{e^{i\Psi}m_{\rm ns}\mathcal P\}
 =m_{\rm ns}\mathcal Q+(x\partial_xm_{\rm ns})\mathcal P.    \tag{47.49}
\]

The ratio-cutoff derivative is indispensable here:
\(x\partial_x(|\alpha|/\lambda)=-|\alpha|/(2\lambda)\), so it
is \(O(1)\), not zero.

On either nonsaddle group,

\[
 |\Psi'|=\left|\log{|\alpha|\over\lambda}\right|
 \ge\log(4/3),\qquad |\Psi''|\ll R^{-1}.           \tag{47.50}
\]

For a smooth dyadic localization \(a_R=m_{\rm ns}\mathcal P\), one
integration by parts gives

\[
 \int e^{i\Psi}a_R\,dL
 =-\int e^{i\Psi}
 \left\{{a_R'\over i\Psi'}
       -{a_R\Psi''\over i(\Psi')^2}\right\}dL,    \tag{47.51}
\]

with the finite-section traces included in the variation of \(a_R\).
The smooth dyadic endpoints vanish.  Equations (47.15), (47.17), and
(47.50) give the first estimate in (47.18).  Applying (47.51) to the
right side of (47.49), and using (47.16)--(47.17), gives the second.

On the inner sector, \(R\ll\lambda\), so the dyadic sums start at a
fixed positive \(R\) and end at \(O(\lambda)\).  Since
\(\kappa-2<0\) and \(\kappa-1<0\), both are bounded by their first
cell, uniformly in \(\lambda\).  On the outer sector,
\(R\gg\lambda\), and the larger series is

\[
 \sum_{R\gg\lambda}R^{\kappa-1}
 \ll\lambda^{\kappa-1}\ll1,                       \tag{47.52}
\]

because (47.2a) implies \(\lambda\gg1\).  This proves the required
inner/outer uniformity rather than merely a fixed-\(\lambda\) result.
The geometric-series constant is uniform in \(X\): the actual choice
\(0\le a\le b=1/\log(2X)\) keeps \(1-\kappa\) bounded below by a
positive absolute constant for all sufficiently large \(X\); the
remaining bounded \(X\)-range is absorbed once.

The true outer boundary limits also follow from the same powers:

\[
 {m_{\rm ns}\mathcal P\over\Psi'}
 =O\left({R^{\kappa-2}\over\log(R/\lambda)}\right)\to0,
 \qquad
 {m_{\rm ns}\mathcal Q\over\Psi'}
 =O\left({R^{\kappa-1}\over\log(R/\lambda)}\right)\to0.      \tag{47.53}
\]

The inner multiplier vanishes at its finite ratio boundary and at the
central collar.  Thus no unrecorded \(L\)-boundary term survives.

### 3.5 Exact radial constant and raw power ledger

The unrestricted constant in the Round-38 height-tail theorem must not
be silently treated as polylogarithmic.  Directly from the exact radial
integral,

\[
 \int_1^{N_X}x^{-3/2-b/2}\,dx
 ={2\over1+b}\{1-N_X^{-(1+b)/2}\}\le2,             \tag{47.54}
\]

so the displayed absolute height-decay proof has the explicit constant
\(C_X\ll\sqrt X\).  One radial integration by parts gives the more
informative exact identity

\[
 R_1(\rho)
 =-{[x^\rho e(\sqrt{Xx})]_1^{N_X}\over\rho}
   +\int_1^{N_X}x^{\rho-1}e(\sqrt{Xx})\,dx,         \tag{47.55}
\]

which is \(O(1)\), as is one \(\eta\)-derivative, but it does not
provide the required uniform \((1+|\eta|)^{-1}\) decay through the
radial stationary band.  Thus Round 38 proves existence but cannot be
used as a target-sized black box.

The present proof instead leaves the radial oscillation uncollapsed.
After the \(L,\nu,\beta\) work, factor exactly

\[
 (-\pi i)\sqrt X,e(\sqrt{Xx})x^{-3/2-b/2}.         \tag{47.56}
\]

The remaining normalized amplitude has coefficient

\[
 h^{-r}q^{-p}
 \left({D_j\over2\sqrt X}\right)^a(H_j+1)^b.       \tag{47.57}
\]

Equations (47.18) and (47.49) bound its value and logarithmic x
derivative by \(P_X\), uniformly in every index.  Since \(r,p>1\),
the \(h\)- and \(q\)-sums, including one harmless logarithm, converge
absolutely.  The equality \(m=hq\) is imposed once and creates no extra
sum.  By (47.2a), the scale factors in (47.57) are \(O(1)\) and there
are \(O(\log X)\) active scales.  Hence

\[
 \sup_x|\mathcal A_{\rm ns}(x)|
 +\sup_x|x\mathcal A_{\rm ns}'(x)|\ll P_X.          \tag{47.58}
\]

Integrating the second estimate with \(dx/x\) proves (47.19).  Finally,
the exact radial integration-by-parts identity behind (47.2b) is

\[
\begin{aligned}
 &\sqrt X\int_1^{N_X}x^{-3/2-b/2}e(\sqrt{Xx})
       \mathcal A_{\rm ns}(x)\,dx\\
 &\quad={1\over\pi i}
 [x^{-1-b/2}e(\sqrt{Xx})\mathcal A_{\rm ns}(x)]_1^{N_X}
 -{1\over\pi i}\int_1^{N_X}e(\sqrt{Xx})
 d\{x^{-1-b/2}\mathcal A_{\rm ns}(x)\}.
                                                               \tag{47.59}
\end{aligned}
\]

This proves the normalized polylogarithmic bound without paying the
\(\sqrt X\) in the fixed-X Cauchy majorant.  Floors, inversion and
profile stars, \(\chi _4(q)\), contour constants, and the finite beta
integral are retained once.  The combined collision convention is not
expanded a second time.  Artificial, axial, endpoint, radial-side,
connector-axis, and corner modules remain with their already accepted
owners.  Applying the exterior \(X^{1/4}\) operator exactly once proves
(47.20).

### 3.6 Middle-cutoff invariance

Let \(m_k\) satisfy (47.27).  If \(G_{\lambda}\) is a normalized
Round-41 product-cell symbol, Leibniz gives

\[
 |\partial_L^a(m_kG_{\lambda})|
 \ll P_X\lambda^{-a},\qquad a\le2.                 \tag{47.60}
\]

The same multiplication preserves the endpoint divided differences,
ordinary smooth shares, signed diagonal section, moving traces, and the
exact Morse BV estimate.  An x derivative of \(m_k\) is \(O(1)\) and
therefore preserves the radial or coefficient ledger as well.  By a
finite refinement of its support, \(m_k\) is a sum of signed full-saddle,
entry, and exit multipliers of the exact type allowed by the statement
of the accepted Round-41 theorem.  Linearity then gives the same
large-alpha package estimate for the sum.

For the repaired middle family,

\[
 m_{\sigma,k}=(1-\chi _0(\alpha))s_\sigma(\alpha)
 \widetilde\vartheta_k(|\alpha|/\lambda)c_1(|\alpha|/\lambda),
                                                               \tag{47.61}
\]

the ratio factors have the seminorms (47.27).  For large \(\lambda\),
\(\chi _0\) is identically zero and \(s_\sigma\) is constant on the
support.  The remaining bounded range of \(\lambda\) is compact and
also satisfies (47.27), with a larger fixed constant.  Finally,
\(\sum_{\sigma,k}m_{\sigma,k}=c_1(|\alpha|/\lambda)(1-\chi _0(\alpha))\)
exactly.  This proves cutoff invariance and exact coverage of the repaired
middle group, without claiming that any individual new multiplier is
literally an old one.

# 4. First doubtful or unproved step

There is no doubtful analytic step in the stated global nonsaddle theorem
relative to the packet's exact returned-terminal formula, finite-section
Plemelj identity, profile seminorms, accepted radial-BV implication, and
accepted Round-41 theorem for any fixed-ratio saddle/entry/exit interval.

The narrowest point requiring conductor verification is the scope of the
already accepted Round-41 wording: the cutoff-invariance conclusion uses
its stated quantifier "any fixed-ratio signed saddle, entry, or exit
interval."  If the authoritative accepted node were intended to freeze
an undisclosed particular cutoff rather than this stated class, then
(47.60) would still prove the analytic stability, but the conductor would
need to promote that stability corollary before using (47.61).  No issue
remains in the nonsaddle proof itself.

This result does not reopen or reprove the separately routed artificial,
axial, endpoint, collision, or corner modules.  Nor does it address the
alpha-bounded zeta-high branch outside the beta positive-line
localization obligation.

# 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `global_gamma_both_signs` | **Pass.** Equations (47.28)--(47.29) give the exact power \(\kappa\) and dyadic symbol bounds on both half-rays; compact alpha is treated directly. |
| `signed_plemelj_before_absolute` | **Pass.** The singular top is first written as the exact diagonal logarithm (47.40) plus the divided difference. No absolute \(1/(L-\nu)\) integral is used. |
| `diagonal_offdiagonal_smooth_split` | **Pass.** Equations (47.30)--(47.45) separately control the signed diagonal, cancellation-preserving off-diagonal quotient, and ordinary smooth shares. |
| `phase_conjugated_x_derivative` | **Pass.** The exact numerator is (47.34), its exact fixed-height derivative is (47.35), and the ratio-cutoff contribution is retained in (47.49). |
| `moving_faces_and_outer_limits` | **Pass.** Equations (47.39)--(47.48) give the exact face velocities, signs, switch and collapse behavior, uniform traces, symmetric height limit, and (47.53) gives the true nonsaddle L-boundary limits. |
| `inner_outer_lambda_uniformity` | **Pass.** The inner dyadic series is controlled at its fixed lower cell and the outer series by (47.52); no fixed-\(\lambda\) constant is hidden. |
| `middle_cutoff_interface` | **Pass, subject only to the accepted quantifier noted in Section 4.** Equations (47.60)--(47.61) prove cutoff invariance and exact repaired-middle coverage. |
| `raw_coefficient_radial_sum` | **Pass.** Equations (47.54)--(47.59) expose the fixed-X constant, retain \(h^{-r}q^{-p}\), sum the actual scales, prove radial BV, and restore the exterior factor once. |
| `collision_and_external_once` | **Pass.** Floors, stars, character, equality, combined collision, contour constants, and routed modules retain their accepted owners; no stationary numerator is inserted in a nonsaddle cell. |

No numerical experiment, symbolic experiment, or web source was used.

# 6. Dependencies and exact artifacts used

Only the selected context in the generated brief was used:

1. `protocol.md`;
2. `state/proof_obligations.yml`, graph SHA-256
   `50afffd106f12da5d4b1d6aba6e15a28782f9c364f8960a084ca611a7a42cf0d`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-beta-global-nonsaddle-signed-section/derivation_packet.md`, including the conductor clarifications (47.2a)--(47.2b) and (47.5a)--(47.5e);
5. `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/reports/actual_cauchy_tail_attack.md`;
6. `rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/reports/off_diagonal_mixed_norm_attack.md`;
7. `rounds/codex-managed/m9-m1-beta-positive-line-localization/synthesis.md`;
8. `rounds/codex-managed/m9-m1-beta-large-alpha-complement-completion/synthesis.md`;
9. the generated Round-47 discovery brief.

Imported accepted facts are the exact returned-terminal normal form,
signed finite-section identity, actual profile bounds, finite ownership
ledger, exact subordinate partition, radial-BV implication, and the
Round-41 theorem for arbitrary fixed-ratio signed saddle/entry/exit
cells.  The global dyadic gamma normalization, exact x-divided
difference, global section powers, nonsaddle summation, explicit radial
constant analysis, and cutoff-invariance corollary are derived here.

# 7. Recommended state effect

**Promote after clean statement-only and hostile validation** a new global
direct nonsaddle signed-section/radial-BV lemma consisting of
(47.15)--(47.20), including both signs, exact x numerator, ratio-cutoff
derivative, moving traces, symmetric height exhaustion, true outer
limits, and the raw \(h^{-r}q^{-p}\) ledger.

Also promote the fixed-ratio cutoff-invariance corollary
(47.27), (47.60)--(47.61).  Compose it with the already accepted
Round-41 package to cover the repaired middle group exactly.  Together
with the accepted compact terminal, artificial shares, and subordinate
one-count partition, these two results close
`M9-M1-beta-positive-line-alpha-localization-certificate` and supply its
target-sized physical contribution.

Reject any proof that normalizes a nonsaddle cell by \(\lambda\), inserts
the saddle stationary numerator, splits the x numerator before retaining
its endpoint cancellation, takes absolute values before the diagonal
Plemelj logarithm, treats the Round-38 constant as polylogarithmic,
omits ratio-cutoff x derivatives, or proves only a fixed-\(\lambda\)
outer estimate.  Downstream beta-transition assembly, M9-M1, M9, and the
Gauss-circle target should change only after the conductor composes the
new lemma with their remaining accepted dependencies.
