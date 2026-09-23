# Round 172 review: literal common-frequency transform

Campaign: `m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate`  
Role: independent transform review  
Verdict: **REPAIR**

## 1. Result

The literal transform and its ordinary-zero-mode seam are **GREEN**.  The
overall report pair needs two local repairs, so the review verdict is
**REPAIR**, not RED.

First, (172.D13)--(172.D15) do supply the exact residual common-frequency
transform that the hostile report treated as still missing.  With a
real-valued cardinal bump, the interpolation is exact at every lattice
point; the physical divisor-incidence opening has multiplicity one; the
parity twist is exactly \((-1)^{\epsilon m}\); character Poisson has the
stated factor \(i/2\); ordinary Poisson has no further constant; and the
coefficient in the squared, parity-averaged formula is \(1/8\).

Second, (172.D18)--(172.D20) legitimately isolate and pay **the completely
recombined ordinary-zero sector**: all character frequencies must first be
summed, and then every term with \(\ell=0\) or \(\ell'=0\) is bounded
together.  The result is \(O_\varepsilon(L^3X^\varepsilon)\).  It is not a
termwise estimate for individual \(k\)-modes.

The earliest open transform seam is therefore (172.D23), the fully signed
\(\ell,\ell'\ne0\) aggregate before positivity.  Physical diagonal
cancellation does not delete the dual diagonal.  The noninteger product
difference kernel, frequency endpoints, physical endpoint cells, and
zero-extension transitions must remain until full recombination.

The central no-go is correct with its stated scope: the first presently
licensed coefficient-uniform positive closure is
\((U+V)D_L\), hence \(L^4X^\varepsilon\) at the maximal link.  This is not a
universal impossibility theorem for an actual-symbol positive estimate.

Two exact report repairs are required:

1. In the hostile report, replace “the doubt begins at the literal residual
   transform” by: the discovery construction (172.D13)--(172.D15) closes
   that identity gate; the doubt begins at the signed nonzero-mode estimate
   (172.D23).
2. The discovery control (172.D22), as phrased with \(Q\ge2R\) consecutive
   sites of one parity and then \(Q,R\asymp M\), cannot fit inside an
   \(M\)-site containing interval.  Replace it by the valid in-range control
   in (172.H15): \(M=4P\), \(2P\) even sites in \([0,M-1]\), and the link
   \(2P\to4P\).  This gives \(\gg MD_L\) and preserves the \(L^4\) no-go.

## 2. Exact statement and hypotheses

Assume the finite literal residual opening

\[
 c_N^{\rm rem}=\sum_{\substack{d\mid N\\d\ {m odd}}}
 \chi_4(d)\lambda_N(d),
 \qquad N=dm,
\]

where \(\lambda_N(d)\) contains, pointwise, the selected/no-pair residual
selector, squarefree and coprimality masks, both complementary parity
branches, all profiles, floors, stars, crossings, endpoint values, and zero
extension.  On support \(d,m\asymp L\), and
\(|\lambda_{dm}(d)|\ll X^\varepsilon\).  Put

\[
 z_N=c_N^{\rm rem}e(J\sqrt N),\qquad
 Z_\epsilon(\theta)=\sum_N(-1)^{\epsilon N}z_Ne(N\theta),
 \qquad D_L=\sum_N|z_N|^2\ll_\varepsilon L^2X^\varepsilon.
\]

Choose a **real-valued** \(\varphi\in C_c^\infty((-1/2,1/2))\) with
\(\varphi(0)=1\), and define

\[
 \mathcal W_\epsilon(x,y)=
 \sum_{\substack{d,m\ge1\\d\ {m odd}}}
 (-1)^{\epsilon m}\lambda_{dm}(d)
 \varphi(x-d)\varphi(y-m),
\]

\[
 \mathcal B_{\epsilon,\theta}(x,y)=
 \mathcal W_\epsilon(x,y)e(J\sqrt{xy}+\theta xy).
\]

Every cell is compactly contained in \(x,y>0\).  With
\(\widetilde{\mathcal B}(\xi,\nu)=\iint\mathcal B(x,y)
e(-\xi x-\nu y)\,dx\,dy\), the exact formula is

\[
 Z_\epsilon(\theta)=\frac i2
 \sum_{\substack{k\in\mathbb Z\\k\ {m odd}}}\chi_4(k)
 \sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).
\tag{R172.1}
\]

For \(B_{U,V}=F_V-F_U\), parity averaging gives

\[
 \Delta_{U,V}=\frac18\Re\sum_{\epsilon=0}^1
 \sum_{k,k'\ {m odd}}\sum_{\ell,\ell'\in\mathbb Z}
 \chi_4(k)\chi_4(k')
 \int_0^1 B_{U,V}(\theta)
 U_{k,\ell}(\theta)\overline{U_{k',\ell'}(\theta)}\,d\theta,
\tag{R172.2}
\]

where \(U_{k,\ell}=\widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell)\).
There is one outer real part.

## 3. Proof and derivation

### Cardinal interpolation, multiplicity, parity, and constants

Because the support of \(\varphi\) lies strictly inside one unit cell,
for integers \(a,b\)

\[
 \mathcal W_\epsilon(a,b)=
 \begin{cases}
 (-1)^{\epsilon b}\lambda_{ab}(a),&a\ge1\text{ odd},\ b\ge1,\\
 0,&\text{otherwise}.
 \end{cases}
\]

Thus the interpolation changes no lattice value.  The map from a physical
divisor incidence to \((d,m)=(d,N/d)\) is one-to-one.  This multiplicity-one
claim applies before a later Möbius \((Q,R)\) opening; such an
inclusion--exclusion opening is not a disjoint multiplicity-one partition.

Since \(d\) is odd,

\[
 (-1)^{\epsilon N}=(-1)^{\epsilon dm}=(-1)^{\epsilon m}.
\]

Hence both product parities are retained and the second Fejer peak is
represented exactly by the amplitude twist used above.

With \(\widehat f(\xi)=\int f(x)e(-\xi x)\,dx\),

\[
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i}
\]

and ordinary Poisson imply

\[
 \sum_n\chi_4(n)f(n)
 =\frac i2\sum_{k\ {m odd}}\chi_4(k)\widehat f(k/4).
\]

Indeed \(k\equiv1\pmod4\) receives \(i/2\), while
\(k\equiv3\pmod4\) receives \(-i/2\).  Applying ordinary Poisson in
the second variable introduces no scale factor.  This proves (R172.1).
The parity average contributes \(1/2\), and
\(|i/2|^2=1/4\), giving the exact \(1/8\) in (R172.2).

### Bandpass kernel and the two diagonals

After expanding the two Fourier integrals, the common-frequency kernel is

\[
 \mathscr B_{U,V}(t)=\int_0^1B_{U,V}(\theta)e(t\theta)\,d\theta
 =\sum_{h\in\mathbb Z}b_{U,V}(h)I(t+h),
 \quad I(u)=\int_0^1e(u\theta)\,d\theta.
\tag{R172.3}
\]

For integer \(n\), this is \(b_{U,V}(-n)=b_{U,V}(n)\); in particular
the physical lattice diagonal has coefficient \(b_{U,V}(0)=0\).  For
noninteger \(t\), integration by parts gives

\[
 \mathscr B_{U,V}(t)=
 \frac{(e(t)-1)(V-U)}{2\pi it}
 -\frac1{2\pi it}\int_0^1B'_{U,V}(\theta)e(t\theta)\,d\theta.
\tag{R172.4}
\]

It is therefore not a compact triangular tent on continuous product
differences.  On the dual diagonal \((k,\ell)=(k',\ell')\), the points
\((x,y)\) and \((x',y')\) in the two cardinal integrals remain independent,
so \(t=xy-x'y'\) is generally noninteger and nonzero.  The physical
diagonal is recovered only after dual diagonal and off-diagonal terms and
all cell/frequency endpoint pieces recombine.

### Ordinary-zero-mode sector

Let

\[
 Z_{\epsilon,0}(\theta)=\frac i2
 \sum_{k\ {m odd}}\chi_4(k)U_{k,0}(\theta).
\]

Applying the already verified character identity in the first variable
gives exactly

\[
 Z_{\epsilon,0}(\theta)=
 \sum_d\chi_4(d)\int_{\mathbb R}
 \mathcal B_{\epsilon,\theta}(d,y)\,dy.
\tag{R172.5}
\]

On every supported cell,

\[
 \partial_y(J\sqrt{dy}+\theta dy)
 =\frac J2\sqrt{d/y}+\theta d\asymp J
 \qquad(0\le\theta\le1),
\]

and the derivative of this quantity is \(O(J/L)\).  One cellwise
integration by parts costs \(O(J^{-1})\); compact support of \(\varphi\)
removes cell-boundary terms.  There are \(O(L^2X^\varepsilon)\) physical
incidences, so

\[
 \sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\varepsilon L^2J^{-1}X^\varepsilon.
\tag{R172.6}
\]

Write \(Z_\epsilon=Z_{\epsilon,0}+Z_{\epsilon,*}\).  The combined part
of (R172.2) with \(\ell=0\) or \(\ell'=0\) is exactly the expansion of

\[
 |Z_{\epsilon,0}|^2+
 2\Re(Z_{\epsilon,0}\overline{Z_{\epsilon,*}}).
\]

Using \(|B_{U,V}|\le U+V\),
\(\|Z_\epsilon\|_2=D_L^{1/2}\), and
\(Z_{\epsilon,*}=Z_\epsilon-Z_{\epsilon,0}\), its absolute value is

\[
 \ll (U+V)
 \left(D_L^{1/2}\frac{L^2}{J}+\frac{L^4}{J^2}\right)X^\varepsilon.
\tag{R172.7}
\]

Since \(U+V\ll L^2\), \(D_L^{1/2}\ll L X^\varepsilon\), and
\(L^2\le J\), (R172.7) is \(O_\varepsilon(L^3X^\varepsilon)\).
This proves (172.D18)--(172.D20), but only after the full \(k,k'\) sums
inside the ordinary-zero sector are recombined.

### Hessian, peak centres, and boundary retention

After locally centering either Fejer peak, the continuous product phase is

\[
 \Phi_\phi(u,v)=J\sqrt{uv}+\phi uv-\xi u-\eta v,
\]

and direct differentiation gives

\[
 \det\operatorname{Hess}\Phi_\phi
 =-\phi^2-\frac{J\phi}{2\sqrt{uv}}.
\tag{R172.8}
\]

Thus the phase is rank one at \(\phi=0\).  The original peak centres are
\(0\) and \(1/2\) modulo one; for the second, the exact lattice factor
\((-1)^N=(-1)^m\) is moved into \(\mathcal W_1\), leaving the same centred
phase.  The determinant statement is therefore valid at both centres.

The off-lattice cardinal interpolation is not periodic in \(\theta\).
Consequently the pieces near the two ends of a chosen fundamental interval
cannot be identified termwise.  Equation (R172.4), the original endpoint
cells stored in \(\lambda_N(d)\), missing zero-extension cells, and saddle
transitions must all remain until the exact dual sum is recombined.  No
global smooth-interior replacement is licensed.

### Positive-power endpoint

Fejer positivity gives

\[
 |\Delta_{U,V}|\le\mathfrak E_U^{(2)}+
 \mathfrak E_V^{(2)}\le(U+V)D_L.
\tag{R172.9}
\]

At the maximal link this is \(L^4X^\varepsilon\).  The valid sharp control
is the hostile construction \(M=4P\), \(z_N=1\) on the \(2P\) even sites
of \([0,M-1]\), with the link \(2P\to4P\); it gives
\(\Delta\gg P^2\asymp MD_L\).  Hence coefficient-uniform Parseval,
Haar, phase-only, or positive-dual closure cannot supply the missing
factor \(L\).  This does not exclude a new positive estimate that first
uses a proved special property of the literal coefficient.

## 4. First doubtful or unproved step

After (R172.1)--(R172.7), the first unproved statement is exactly the
complete signed nonzero ordinary-frequency aggregate

\[
 \frac18\Re\sum_{\epsilon=0}^1
 \sum_{k,k'\ {m odd}}\sum_{\ell,\ell'\ne0}
 \chi_4(k)\chi_4(k')
 \int_0^1B_{U,V}(\theta)
 U_{k,\ell}(\theta)\overline{U_{k',\ell'}(\theta)}\,d\theta
 \ll_\varepsilon L^3X^\varepsilon.
\tag{R172.10}
\]

No dual diagonal may be deleted, and no modulus over dual modes, cardinal
cells, or openings is licensed before (R172.10).  The permitted artifacts
contain no estimate for it.  Thus the earliest valid transform is
(172.D14)--(172.D15); the earliest open analytic seam is (172.D23), not
the transform itself and not the ordinary-zero sector.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| cardinal interpolation | **PASS**, after explicitly choosing \(\varphi\) real-valued; exact at every integer pair. |
| physical multiplicity | **PASS** for ordered \((d,m=N/d)\) incidences; not to be transferred to overlapping Möbius openings. |
| character/ordinary Poisson constants | **PASS**: \(i/2\), odd \(k\), no ordinary factor, and \(1/8\) after squaring and parity averaging. |
| parity twist | **PASS**: \((-1)^{\epsilon N}=(-1)^{\epsilon m}\), with both \(m\)-parities retained. |
| noninteger bandpass kernel | **PASS**: (R172.3)--(R172.4); it is not a tent off the physical lattice. |
| ordinary-zero-mode isolation | **PASS collectively** after summing all character modes; **not** termwise in \(k\). |
| ordinary-zero-mode power | **PASS**: \(L^2/J\) pointwise and \(L^3X^\varepsilon\) for all zero-containing cross terms. |
| physical versus dual diagonal | **PASS**: they are distinct and cancel only after full recombination. |
| Hessian determinant | **PASS**: (R172.8). |
| both peak centres | **PASS** with the exact \((-1)^m\) amplitude gauge at the second peak. |
| boundary/transition retention | **PASS as retained data**; no separate target estimate or smooth replacement is proved. |
| positive dual endpoint | **PASS as a scoped no-go** at \(L^4\); not a universal no-go for literal actual-symbol estimates. |
| discovery sharpness control | **REPAIR** (172.D22) to the in-range construction (172.H15). |
| earliest hostile failure | **REPAIR** from “missing transform” to the signed nonzero-mode bound (R172.10). |

No numerical experiment or external theorem is needed.

## 6. Dependencies and exact artifacts used

Only the assigned artifacts were read:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `strategy/round172_m2_hard_top_t1_residual_maximal_fejer_dyadic_strategy.md`;
4. `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
5. `proofs/kernels/m9_m2_hard_top_t1_joint_functional_equation_double_poisson_self_return.md`;
6. `reports/literal_maximal_fejer_dyadic_frequency_attack.md` in this campaign; and
7. `reports/maximal_fejer_transform_endpoint_hostile_audit.md` in this campaign.

No web source, computation, sibling review, synthesis, proof draft, or shared
state file was used.

## 7. Recommended state effect

Accept the literal common-frequency identity (172.D13)--(172.D15), the
noninteger bandpass kernel (172.D16)--(172.D17), and the fully recombined
ordinary-zero-mode estimate (172.D18)--(172.D20) as candidate evidence.
Apply the two local report repairs identified in Section 1.

Retain (165.K26) and the residual scalar as open.  If the round closes
without a proof of (R172.10), the mathematically supported terminal label is
`maximal_fejer_dyadic_character_poisson_no_go`, scoped to transforms followed
by coefficient-uniform positive dual/cell control.  Do not promote a strict
sector, parent, bridge, theorem, or exponent, and do not state that every
future actual-symbol positive theorem is impossible.
