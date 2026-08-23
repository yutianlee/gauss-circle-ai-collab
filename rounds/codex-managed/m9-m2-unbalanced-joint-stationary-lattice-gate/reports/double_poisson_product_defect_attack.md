# Round 124 report: double-Poisson product-defect attack

Campaign: `m9-m2-unbalanced-joint-stationary-lattice-gate`

Task: `double_poisson_product_defect_attack`

Role: discovery

Starting graph SHA-256:
`2b60eca238542d4f321a19c90f20163c6dd4cd7c60da6f324910b6db10b638c6`

## 1. Result

The conductor's two character-Poisson signs, the two scalar saddles, the
Gaussian units, and the principal amplitude are correct.  There are two
necessary repairs.

First, the product defect

$$
 \mathcal N=p(k+h)-qk
\tag{124.1}
$$

is the numerator of the **phase**, but it is not the numerator of the
dual \(k\)-gradient.  The latter is

$$
 \mathcal G=pk-q(k+h)=\mathcal N-(p+q)h.
\tag{124.2}
$$

Thus small or zero \(\mathcal N\) does not remove the reciprocal-alias
stationarity.  The exact formula is

$$
 \partial_k\Theta
 =\frac{\sqrt M}{2}
 \frac{\mathcal G}
 {\sqrt{k(k+h)}\{\sqrt{pk}+\sqrt{q(k+h)}\}}
 =M\left(\frac1{r_*}-\frac1{s_*}\right).
\tag{124.3}
$$

Second, rowwise Poisson summation does not preserve the Round-123
indicator \(j\ne0,E\ne0,|E|\le X^{1+\rho}/L\).  The clean product
stationary formula is a formula for the full shifted square
\(\mathcal F_{M,H_0}\), not term by term for \(V_{M,H_0}\).  The lawful
use is

$$
 \mathcal F_{M,H_0}=V_{M,H_0}+\mathcal Q_{\rm safe},
 \qquad
 |\mathcal Q_{\rm safe}|\ll_\varepsilon X^{1/2+\varepsilon},
\tag{124.4}
$$

where the zero alias, nonzero exact aliases, and rapid tail remain in
\(\mathcal Q_{\rm safe}\).  No dual \((p,q,h,k)\) cell is thereby
identified with a primal nonexact \(E\)-cell.

After this repair, exact character-Poisson summation and uniform scalar
stationary phase give the complete principal stationary lattice

$$
 \begin{aligned}
 \mathcal F_{M,H}
  ={}& C_H\sum_{|h|<H}(H-|h|)\sum_k
       \sum_{p,q>0\atop p,q\ {\rm odd}}
       \chi _4(p)\chi _4(q)\\
 &\quad\times
 \frac{M^{1/2}\mathcal A_{p,k+h}
                    \overline{\mathcal A_{q,k}}}
 {[p q k(k+h)]^{3/4}}
 e\!\left(\Theta_{p,q,h}(k)\right)
 +O(1),
\end{aligned}
\tag{124.5}
$$

where

$$
 C_H=\frac{J+H-1}{H^2},\qquad
 \Theta_{p,q,h}(k)
 =\sqrt M\{\sqrt{p(k+h)}-\sqrt{qk}\},
\tag{124.6}
$$

$$
 r_{p,a}=2\sqrt{Ma/p},\qquad
 \mathcal A_{p,a}=
 W\!\left(\frac{X}{D r_{p,a}}\right)
 q_L\!\left(\frac XM p\right).
\tag{124.7}
$$

The \(O(1)\) in (124.5) is the aggregate of the two scalar stationary
remainders and all nonstationary \(p\le0\), \(q\le0\), and inactive
positive modes.  Smooth zero extension on the literal flat-smooth owner
is essential here.

The active product-equality sector is exactly
\(p=q,h=0\), and its complete principal mass is target-safe:

$$
 \mathcal D_0\ll X^{1/2}.
\tag{124.8}
$$

Consequently Round 123's fixed-power inverse theorem strengthens as
follows: any fixed-power violation forces the complete actual-sign
stationary aggregate in

$$
 p=q, h\ne0
 \qquad\text{or}\qquad
 p\ne q
\tag{124.9}
$$

to have the same power-excess size.  This is a strict removal of the dual
product-equality diagonal, but it is not the threshold estimate.

There is an exact joint stationary self-return.  If \(j\) and \(d\) are
the Poisson labels dual to \(k\) and \(h\), respectively, then

$$
 \det \operatorname {Hess}_{k,h}\Theta
 =-\frac{M\sqrt{pq}}
 {16[k(k+h)]^{3/2}}\ne0,
\tag{124.10}
$$

and the unique simultaneous saddle is

$$
 k_*^{\dagger}=\frac{Mq}{4(d-j)^2},\qquad
 h_*^{\dagger}=\frac M4
 \left\{\frac p{d^2}-\frac q{(d-j)^2}\right\},
\tag{124.11}
$$

with

$$
 r_*^{\dagger}=\frac Md,\qquad
 s_*^{\dagger}=\frac M{d-j}.
\tag{124.12}
$$

The Hessian has signature zero, and the exact Legendre phase is

$$
 \Theta-jk-dh
 =jk+dh
 =\frac M4\left\{\frac p d-\frac q{d-j}\right\}.
\tag{124.13}
$$

The determinant factor cancels every \(k\)-power in (124.5), leaving the
principal stationary coefficient

$$
 \frac{4C_H(H-|h_*^{\dagger}|)}{pq}.
\tag{124.14}
$$

Thus the joint transform returns a reciprocal phase with the same two
quarter characters.  Its inverse is (124.11), so this is a canonical
involution, not a new inequality.

The capacity confirms the obstruction.  Put

$$
 Q=\frac{D^2}{L\sqrt X}.
\tag{124.15}
$$

The strict UNBAL inequality \(\ell<\delta-1/4\) gives
\(Q\to\infty\).  For each fixed active \((p,q)\), the gradient image of
one interior \((k,h)\)-cell has area

$$
 \asymp \frac{XL}{K^3}\,KH
 =\frac{D^3}{L\sqrt X}=DQ.
\tag{124.16}
$$

Each stationary mode has size

$$
 \asymp \frac K{HL^2}=\frac{\sqrt X}{DL}.
\tag{124.17}
$$

There are \(L^2\) choices of \((p,q)\).  Hence the principal-symbol
absolute capacity is

$$
 L^2\cdot DQ\cdot\frac{\sqrt X}{DL}=D^2.
\tag{124.18}
$$

This is a norm diagnostic, not a positive lower bound.  Even granting a
square-root factor \(L\) from the \(L^2\) mode signs would leave

$$
 \frac{D^2}{L}=Q\sqrt X>\sqrt X.
\tag{124.19}
$$

Therefore triangle inequalities, coefficient-blind \(L^2\) norms, or
random-sign credit from \(\chi _4(p)\chi _4(q)\) cannot reach the energy
target.  A successful continuation would need an additional genuinely
joint signed saving of at least \(Q=D^2/(L\sqrt X)\) after the ordinary
mode-sign square-root credit.  No such inequality is proved here.

## 2. Exact statement and hypotheses

Let \(X\ge2\) be real and let

$$
 D=X^\delta,\qquad L=X^\ell,\qquad
 R=\frac XD,\qquad K=\frac{XL}{D^2},
\tag{124.20}
$$

with

$$
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
\tag{124.21}
$$

Let \(M\in\mathbb Z\), \(M\asymp X\), while every physical amplitude and
the denominator \(4X\) remain frozen at the original real \(X\).  Put

$$
 H=H_0=\left\lceil\frac{X^{1/2}}D\right\rceil,
 \qquad K\asymp LH^2,qquad 1\le H\ll K.
\tag{124.22}
$$

Fix one literal flat-smooth strict-UNBAL component, with its actual
zero-extended \(W\) and \(q_L\), and define

$$
 \begin{aligned}
 \mathcal F_{M,H}
 ={}&C_H\sum_{|h|<H}(H-|h|)\sum_k
 \sum_{r,s\ {\rm odd}}\chi _4(r)\chi _4(s)
 W_r\overline{W_s}\\
 &\quad\times
 \frac{q_{r,k+h}\overline{q_{s,k}}}{(k+h)k}
 e\!\left(\frac{M(k+h)}r-\frac{Mk}s\right).
 \end{aligned}
\tag{124.23}
$$

All sums are over the literal support, so \(k\asymp K\),
\(k+h\asymp K\), and \(r,s\asymp R\).  For \(a\asymp K\), define the
exact oscillatory integral

$$
 I_p(a)=\int_0^\infty
 W\!\left(\frac{X}{Dx}\right)
 \frac{q_L(4Xa/x^2)}a
 e\!\left(\frac{Ma}{x}+\frac{px}{4}\right)dx.
\tag{124.24}
$$

Then the complete exact character-Poisson identity is

$$
 \boxed{
 \mathcal F_{M,H}
 =\frac{C_H}{4}\sum_{|h|<H}(H-|h|)\sum_k
 \sum_{p,q\ {\rm odd}}
 \chi _4(p)\chi _4(q)
 I_p(k+h)\overline{I_q(k)}.}
\tag{124.25}
$$

Formula (124.25), with all positive and negative odd modes, is exact and
contains every support entry, exit, shift, conjugate, and Fejer
multiplicity.  Formula (124.5) is its stationary form.  Uniformly on the
active positive modes,

$$
 \begin{aligned}
 I_p(a)={}&2M^{1/4}a^{-3/4}p^{-3/4}
 \mathcal A_{p,a}
 e\!\left(\sqrt{Map}+\frac18\right)
 +\mathcal E_p(a),\\
 |\mathcal E_p(a)|\ll{}&
 \frac RK(LR)^{-3/2}.
 \end{aligned}
\tag{124.26}
$$

The active modes satisfy \(p\asymp L\); the total of the inactive modes
is rapidly small.  The same assertions hold on the conjugate \(q\)-leg.

The theorem proved in this report is the conjunction of (124.4),
(124.5), the repair (124.2)--(124.3), the diagonal estimate (124.8), the
fixed-power off-diagonal inverse implication (124.9), and the exact
joint canonical map (124.10)--(124.14).  Equations (124.18)--(124.19)
are explicitly only principal-symbol capacity diagnostics.  No target
bound for (124.9) is asserted.

## 3. Proof or derivation

### 3.1 Exact two-character Poisson formula

With (e(z)=e^{2\pi iz}),

$$
 \chi _4(n)=\frac{e(n/4)-e(-n/4)}{2i}.
\tag{124.27}
$$

For a smooth compactly supported (F), Poisson summation gives

$$
 \sum_n\chi _4(n)F(n)
 =\frac1{2i}\sum_{\sigma=\pm1}\sigma
 \sum_{m\in\mathbb Z}\int F(x)
 e(-(m-\sigma/4)x)dx.
\tag{124.28}
$$

On the \(r\)-leg set \(p=-4m+\sigma\).  This maps the pair
\((m,\sigma)\) bijectively onto all odd \(p\), and
\(\chi _4(p)=\sigma\).  Therefore

$$
 \sum_{r\ {\rm odd}}\chi _4(r)W_r\frac{q_{r,a}}a e(Ma/r)
 =\frac1{2i}\sum_{p\ {\rm odd}}\chi _4(p)I_p(a).
\tag{124.29}
$$

The (s)-leg is its complex conjugate and contributes
\(-1/(2i)\).  Hence the two Poisson coefficients multiply to (1/4),
proving (124.25).  Equivalently, on the two stationary sign branches
\(p=-4(m-\sigma/4)>0\) and
\(q=4(n-\tau/4)>0\), one has

$$
 -\frac{\sigma\tau}{4}
 =\frac{\chi _4(p)\chi _4(q)}4.
\tag{124.30}
$$

This verifies the conductor sign, including both quarter channels.

### 3.2 Scalar saddles, Gaussian units, and aggregate remainder

For the (r)-phase

$$
 \phi(x)=\frac{Ma}{x}+\frac{px}{4},
$$

an interior stationary point exists only for \(p>0\), at

$$
 r_{p,a}=2\sqrt{Ma/p},\qquad
 \phi(r_{p,a})=\sqrt{Map},\qquad
 \phi''(r_{p,a})=\frac{p^{3/2}}{4\sqrt{Ma}}>0.
\tag{124.31}
$$

Thus the Gaussian unit is (e(1/8)) and
\(|\phi''|^{-1/2}=2(Ma)^{1/4}p^{-3/4}\).  The \(s\)-leg has the
conjugate saddle and unit (e(-1/8)); the units cancel in the product.
At the saddle,

$$
 q_L(4Xa/r_{p,a}^2)=q_L((X/M)p),
\tag{124.32}
$$

which proves (124.26), (124.7), and the mode range \(p\asymp L\).

For completeness, scale (x=Ry).  On the literal flat-smooth support,
the phase has large parameter \(LR\), while the scaled amplitude and all
of its derivatives are \(O(R/K)\).  Uniform one-dimensional stationary
phase gives a main size

$$
 \mathfrak m\asymp\frac RK(LR)^{-1/2}
\tag{124.33}
$$

and a remainder \(O(\mathfrak m/(LR))\).  There are \(O(L)\) active
modes.  Repeated integration by parts makes \(p\le0\) and the inactive
positive modes rapidly small.  Since

$$
 C_H\sum_{|h|<H}(H-|h|)=J+H-1\asymp K,
\tag{124.34}
$$

the absolute aggregate of one main and one remainder is

$$
 K\cdot K\cdot
 \frac{(L\mathfrak m)^2}{LR}=O(1),
\tag{124.35}
$$

and the double remainder is smaller.  This proves (124.5) with its
aggregate \(O(1)\).  Smooth zero extension means a saddle crossing a
literal (r)- or (s)-support edge is covered by the same uniform
formula; there is no omitted hard endpoint owner in this flat-smooth
claim.

The coefficient of one central \((p,q,k,h)\) term after the Fejer
prefactor is

$$
 \asymp\frac{X^{1/2}}{HK^{1/2}L^{3/2}}
 =\frac{D^2}{X^{1/2}L^2},
\tag{124.36}
$$

so the conductor's nominal scale is also correct.

### 3.3 Phase defect versus gradient defect

Rationalizing the phase gives exactly

$$
 \Theta=\sqrt M\,
 \frac{\mathcal N}
 {\sqrt{p(k+h)}+\sqrt{qk}},
 \qquad
 \mathcal N=p(k+h)-qk.
\tag{124.37}
$$

However, rationalizing the derivative instead gives

$$
 \begin{aligned}
 \partial_k\Theta
 &=\frac{\sqrt M}{2}
 \left(\frac{\sqrt p}{\sqrt{k+h}}
       -\frac{\sqrt q}{\sqrt k}\right)\\
 &=\frac{\sqrt M}{2}
 \frac{pk-q(k+h)}
 {\sqrt{k(k+h)}\{\sqrt{pk}+\sqrt{q(k+h)}\}},
 \end{aligned}
\tag{124.38}
$$

which proves (124.2)--(124.3).  At the scalar saddles,

$$
 \partial_k\Theta=M(1/r_*-1/s_*),\qquad
 \partial_h\Theta=M/r_*.
\tag{124.39}
$$

Thus a \(k\)-Poisson label is the old reciprocal alias \(j\), but it is
not determined by \(\mathcal N\) alone.

Because odd \(p,q\asymp L\) differ by at least two, while
\(K/(LH)\asymp H\to\infty\),

$$
 \mathcal N=0\quad\Longleftrightarrow\quad p=q, h=0
\tag{124.40}
$$

on the active stationary support for large \(X\).  Moreover

$$
 |\mathcal N|\asymp |p-q|K\quad(p\ne q),\qquad
 |\mathcal N|\asymp L|h|\quad(p=q,h\ne0).
\tag{124.41}
$$

These are phase-size statements only.  In the equal-mode shifted sector,
\(|\partial_k\Theta|\asymp D|h|/K\), and its range reaches

$$
 \frac{DH}{K}=\frac{D^2}{L\sqrt X}=Q\to\infty.
\tag{124.42}
$$

It therefore contains many reciprocal-alias crossings.  In the unequal
sector the centre of the alias range is
\(\asymp D(p-q)/L\).  Neither sector has a uniform first-derivative gap.

### 3.4 Product-equality diagonal and the stronger inverse implication

On \(p=q,h=0\), the phase is zero and
\(\chi _4(p)^2=1\).  From (124.5),

$$
 \begin{aligned}
 |\mathcal D_0|
 &\ll C_HH M^{1/2}
 \sum_{k\asymp K}k^{-3/2}
 \sum_{p\asymp L}p^{-3/2}\\
 &\ll \frac KH X^{1/2}K^{-1/2}L^{-1/2}
 \ll X^{1/2},
 \end{aligned}
\tag{124.43}
$$

using \(K\asymp LH^2\).  Nonstationary diagonal modes are included in
the \(O(1)\) error.  This proves the complete active dual
product-equality one-count at the square target.

Let \(\mathcal S_{\rm eq}^{\ne0}\) be (124.5) restricted to
\(p=q,h\ne0\), and let \(\mathcal S_{\rm neq}\) be its restriction to
\(p\ne q\), with every sign of \(h\), both conjugate orientations, all
profiles, and no outside modulus.  Equations (124.4), (124.5), and
(124.43) give

$$
 V_{M,H}
 =\mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}
  +(\mathcal D_0-\mathcal Q_{\rm safe})+O(1).
\tag{124.44}
$$

In particular, if the Round-123 scalar row violates its target by a fixed
power \(X^\eta\), then, after choosing the bookkeeping epsilon below
\(\eta\),

$$
 \Re\{\mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}\}
 \gg X^{1/2+2\eta}.
\tag{124.45}
$$

Hence at least one of the two complete sectors in (124.9) is large.  This
is a stronger inverse localization, not an estimate for either sector.

### 3.5 Simultaneous \(k,h\) stationary map

For the joint phase (124.6), direct differentiation gives

$$
 \operatorname {Hess}_{k,h}\Theta
 =\frac{\sqrt M}{4}
 \begin{pmatrix}
  \sqrt q\,k^{-3/2}-\sqrt p\,(k+h)^{-3/2}
   &-\sqrt p\,(k+h)^{-3/2}\\
  -\sqrt p\,(k+h)^{-3/2}
   &-\sqrt p\,(k+h)^{-3/2}
 \end{pmatrix}.
\tag{124.46}
$$

Its determinant is (124.10).  Thus the apparent zero of
\(\partial_k^2\Theta\) in part of the unequal-mode sector is not a joint
degeneracy; the mixed Hessian is everywhere nondegenerate.

Apply Poisson with convention
\(e(\Theta-jk-dh)\).  The stationary equations are

$$
 j=\partial_k\Theta,qquad d=\partial_h\Theta.
\tag{124.47}
$$

Equation (124.39) gives \(d=M/r_*\) and \(d-j=M/s_*\), and solving the
two scalar saddle relations yields (124.11)--(124.12).  Conversely these
formulas recover one and only one \((k,h)\) for every admissible
\((j,d)\).  Thus there is no hidden saddle multiplicity.

At this point

$$
 \Theta=2d(k+h)-2(d-j)k=2(jk+dh),
\tag{124.48}
$$

which proves (124.13).  Since the Hessian has one positive and one
negative eigenvalue, the two-dimensional Gaussian unit is (1).  Also

$$
 |\det\operatorname {Hess}\Theta|^{-1/2}
 =\frac{4[k(k+h)]^{3/4}}{M^{1/2}(pq)^{1/4}}.
\tag{124.49}
$$

Multiplication by the principal coefficient in (124.5) proves
(124.14).  On any smooth interior \(k,h\)-patch the returned main term is
therefore

$$
 \begin{aligned}
 4C_H\sum_{p,q>0\atop p,q\ {\rm odd}}
 \frac{\chi _4(p)\chi _4(q)}{pq}
 q_L\!\left(\frac XM p\right)
 \overline{q_L\!\left(\frac XM q\right)}
 \sum_{j,d}&(H-|h_*^{\dagger}|)\,\Omega_{p,q}(j,d)\\
 &\times e\!\left(\frac M4
 \left\{\frac p d-\frac q{d-j}\right\}\right),
 \end{aligned}
\tag{124.50}
$$

where \(\Omega_{p,q}\) is exactly the transported literal interior
symbol, including

$$
 W\!\left(\frac{Xd}{DM}\right)
 \overline{W\!\left(\frac{X(d-j)}{DM}\right)}
\tag{124.51}
$$

and the conditions that (124.11) lies in the original \(k,h\)-patch.
No \(j\), \(d\), sign, or profile has been removed in (124.50).

At this saddle the phase defect becomes

$$
 \mathcal N_*=\frac M4
 \left\{\left(\frac p d\right)^2
       -\left(\frac q{d-j}\right)^2\right\}.
\tag{124.52}
$$

It is therefore the product of the returned reciprocal phase difference
and its complementary sum, not a new independent divisor coordinate.

### 3.6 Capacity and involution

For fixed \(p,q\asymp L\), the map
\((k,h)\mapsto(j,d)=\nabla_{k,h}\Theta\) is one-to-one.  On a fixed
central patch its Jacobian has size \(XL/K^3\), while the patch has area
\(KH\).  Its gradient image consequently has area (124.16).  More
geometrically, it is a curved strip of length \(\asymp D\) and transverse
width

$$
 Q=\frac{D^2}{L\sqrt X}.
\tag{124.53}
$$

Both dimensions grow, because

$$
 2\delta-\ell-\frac12>delta-\frac14>0.
\tag{124.54}
$$

Thus its nominal stationary-label count is \(DQ\), with one continuous
saddle per label.  On a central Fejer patch (124.14) has size (124.17).
This proves the arithmetic in (124.18)--(124.19).  It does not assert that
the signed terms add positively.

The return is also exact at the one-leg principal-symbol level.  If
\(F) is a smooth (r\)-amplitude, the forward stationary map is

$$
 \sum_r\chi _4(r)F(r)e(Ma/r)
 =\frac{(Ma)^{1/4}e(1/8)}i
 \sum_{p>0\atop p\ {\rm odd}}
 \chi _4(p)p^{-3/4}F(2\sqrt{Ma/p})e(\sqrt{Map})
 +\mathrm{rem}.
\tag{124.55}
$$

Poisson summation of the \(p\)-sum has stationary label
\(r=4m-\sigma>0\), Gaussian unit (e(-1/8)), and stationary amplitude

$$
 -\frac{(Ma)^{-1/4}e(-1/8)}i
 \chi _4(r)F(r)e(Ma/r).
\tag{124.56}
$$

The prefactors in (124.55)--(124.56) multiply to (1).  Thus the
character, Gaussian unit, amplitude, and reciprocal phase all return.
At the exact level this is simply Poisson inversion; (124.55)--(124.56)
verify that the principal stationary constants do not break the
involution.

Likewise, (124.11) is the explicit inverse of the joint gradient map and
the Legendre transform of (124.13) returns \(\Theta\).  The complete
coefficient-preserving stationary operation is therefore a self-return.
The product-defect regrouping inserts no inequality.

### 3.7 The primal projector and the endpoint ledger

Let

$$
 P(r,s)=\mathbf 1_{j(r,s)\ne0}
 \mathbf 1_{E(r,s)\ne0}
 \mathbf 1_{|E(r,s)|\le X^{1+\rho}/L}.
\tag{124.57}
$$

This is a joint, discontinuous arithmetic multiplier.  Poisson summation
of \(P(r,s)F(r,s)\) produces the two-dimensional Fourier transform of
the whole product \(PF\); it does not produce (124.25) with an analogous
indicator on \(p,q\).  Indeed at a simultaneous continuous saddle,
\(r_*=M/d\), \(s_*=M/(d-j)\), so

$$
 M(s_*-r_*)-jr_*s_*=0.
\tag{124.58}
$$

This tautological continuous exact alias cannot encode the original
integer defect \(E\ne0\).  Equation (124.4), rather than rowwise survival
of \(P\), is the only use of the clean dual formula made above.
In particular \(E_*=0\) yields no rigorous collar saving for the
nonexact primal sector: the width and weight of that sector have already
been folded into the Fourier transform of the omitted projector \(P\).
Recovering a collar gain would require estimating that coupled transform,
which is precisely an additional signed inequality and is not supplied
by stationary phase.

The scalar \(r,s\) stationary ledger is complete and target-safe by
(124.35).  A further full \(k,h\) stationary expansion has a separate
seam.  The exact finite Poisson identity is valid after splitting the
triangular Fejer weight into \(h>0\), \(h=0\), and \(h<0\), but
\(H-|h|\) is not a globally smooth \(h\)-symbol.  Therefore (124.50) is
only the smooth-interior principal module.  A claimed complete
two-dimensional asymptotic must additionally retain:

1. the \(h=0\) corner module;
2. both \(|h|=H\) entry/exit modules;
3. the literal \(k\)-support entries and exits;
4. stationary points crossing any of these faces; and
5. the nonstationary two-dimensional integrals.

No target bound for that entire boundary ledger is proved here.  This is
the first invalid seam in any claim that (124.50) alone estimates the
whole shifted square.  It does not weaken the no-go: the exact Poisson
operation, including all those modules, is invertible, while one fixed
smooth interior patch already has the over-target capacity
(124.18)--(124.19).

Negative \(h\) is retained through

$$
 (p,q,h,k)\longmapsto(q,p,-h,k+h),
\tag{124.59}
$$

which conjugates the phase and sends \(\mathcal N\) to
\(-\mathcal N\).  Negative aliases are retained by \(j<0\), with
\(d>0\) and \(d-j>0\).  No cancellation is inferred merely from either
orientation.

## 4. First doubtful or unproved step

The first open analytic estimate after the lawful repair is

$$
 \boxed{
 \mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}
 \ll_\varepsilon X^{1/2+\varepsilon},}
\tag{124.60}
$$

with the two quantities defined from the complete actual-sign stationary
sum (124.5), before an outside norm.  Equivalently one may seek this
bound after exact finite \(k,h\)-Poisson summation, but then all the
interior, corner, endpoint, transition, and nonstationary modules listed
in Section 3.7 must remain together.

Neither the strict phase-defect separation (124.40) nor joint Hessian
nondegeneracy (124.10) proves (124.60).  The alias strip has \(DQ\)
stationary labels per mode pair, and the character is the same rank-one
product \(\chi _4(p)\chi _4(q)\) that returns under inverse Poisson.
An \(L^2\) norm using only these mode signs still has capacity
\(D^2/L=Q\sqrt X\).  The missing input is a sign-preserving inequality
that couples \(p,q,j,d\) (or, before the transform, \(p,q,k,h\)) and saves
at least the extra factor (Q) beyond ordinary mode-sign square root.

The first **transform** error to avoid is earlier: (124.25) must not be
written directly for the projected survivor \(V_{M,H}\).  Doing so drops
the joint multiplier (124.57).  The first **stationary-ledger** error to
avoid is replacing the exact \(k,h\) transform by the interior expression
(124.50) without the five boundary modules in Section 3.7.

## 5. Required control tests and outcomes

| Control | Test and outcome |
|---|---|
| `literal_Round123_near_alias_survivor` | **Pass after repair.**  The exact relation is (124.4).  The primal \(j,E\) projector does not survive rowwise Poisson; no dual cell is called a primal nonexact alias, and \(E_*=0\) supplies no collar saving. |
| `H0_K_normalization` | **Pass.**  \(H_0\asymp X^{1/2}/D\), \(K\asymp LH_0^2\), \(C_H\sum_h(H-|h|)\asymp K\), and \(Q=DH_0/K=D^2/(L\sqrt X)\to\infty\). |
| `double_character_Poisson_signs` | **Pass.**  The exact coefficient is \(\chi _4(p)\chi _4(q)/4\); see (124.29)--(124.30). |
| `stationary_points_and_Gaussian_units` | **Pass on both scalar legs.**  Saddles, amplitudes, and units are (124.26), (124.31); the units (e(1/8)) and (e(-1/8)) cancel.  The joint Hessian has signature zero. |
| `dual_product_defect` | **Pass with correction.**  \(\mathcal N\) gives the rationalized phase and has only the active diagonal zero in (124.40), but it is not the gradient numerator. |
| `dual_gradient_to_primal_alias` | **Pass with correction.**  The numerator is \(\mathcal G=\mathcal N-(p+q)h\); (124.38)--(124.39) identify the \(k\)-dual label with the reciprocal alias. |
| `dual_diagonal_one_count` | **Pass.**  The complete active \(p=q,h=0\) principal sector is \(O(X^{1/2})\) by (124.43).  It yields the stricter inverse localization (124.45). |
| `equal_mode_shifted_sector` | **Open.**  Its defect is \(ph\), but its alias range has width \(Q\to\infty\).  Product inequality does not make it target-safe. |
| `unequal_mode_sector` | **Open.**  Its phase defect is \(\asymp|p-q|K\); possible zeros of \(\partial_k^2\Theta\) are removed only jointly, and the nondegenerate joint transform self-returns with over-target capacity. |
| `mode_shift_alias_multiplicity` | **Pass.**  Equations (124.11)--(124.12) give at most one continuous saddle for each \((p,q,j,d)\).  The image nevertheless contains nominally \(DQ\) labels per \((p,q)\), so one-count is not a saving. |
| `character_persistence` | **Pass.**  The character becomes exactly \(\chi _4(p)\chi _4(q)\), survives the joint transform, and returns to \(\chi _4(r)\chi _4(s)\) under (124.55)--(124.56). |
| `stationary_endpoint_and_error_ledger` | **Scalar pass; joint-main-only.**  The two scalar remainders total \(O(1)\).  The \(k,h\) interior formula requires the five explicit corner/endpoint modules of Section 3.7 and is not claimed as a complete target estimate. |
| `signed_joint_aggregation` | **Pass in the theorem; open as an estimate.**  Equations (124.44), (124.45), and (124.60) retain the complete real signed aggregate.  Absolute values enter only the explicitly labelled capacity diagnostic. |
| `transform_involution_and_norm_scope` | **Pass as a no-go.**  Both the one-leg constants and the joint Legendre map return exactly.  Absolute capacity is \(D^2\); mode-sign square-root capacity is \(D^2/L=Q\sqrt X\). |
| `owner_and_downstream_scope` | **Pass.**  Every claim is confined to the literal flat-smooth strict-UNBAL owner.  No hard, sharp, clipped, starred, arithmetic, transition, BAL, TOP, complete UNBAL, M9-M2, M9, uniformity, exponent, or quarter-theorem implication is asserted. |

All controls are analytic.  No numerical experiment, web source, or
external theorem was used.

## 6. Dependencies and exact artifacts used

This report used exactly the context assigned in the task brief:

1. `protocol.md`, for graph authority, the signed/unsigned distinction,
   proof-state scope, and the seven-section contract;
2. `state/proof_obligations.yml`, for the accepted Round-123 reduction,
   the open flat-smooth UNBAL parent, the character guardrail, and all
   downstream nonimplications;
3. `state/active_campaign.yml`, for the frozen Round-124 target,
   parameter range, required branches, controls, and promotion gate;
4. `strategy/conductor_0821_full_proof_strategy.md`, for the transform
   stop rule, the Round-118 and Round-123 survivors, and the requirement
   of a genuinely noninvertible signed inequality;
5. `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/synthesis.md`,
   for the accepted integer-centred shifted survivor and safe packages;
6. `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reports/signed_alias_product_attack.md`,
   for the literal shifted kernel, exact Fejer normalization, alias and
   factor definitions, and prior capacity ledger;
7. `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reviews/conductor_round123_integerization_gram_adjudication.md`,
   for the promoted theorem package and exact remaining gap; and
8. `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/derivation_packet.md`,
   for the candidate double-Poisson map and the formulas audited here.

The added inputs are Poisson summation, one- and two-dimensional
stationary phase, direct differentiation, and elementary lattice-area
capacity bookkeeping.  No sibling Round-124 report, candidate, review,
synthesis, validation file, shared proof draft, web source, or
computation was read.

## 7. Recommended state effect

**Promote after independent seam review** the exact double-character
Poisson identity (124.25), the scalar stationary formula (124.5)--(124.7)
with aggregate (O(1)) remainder, and the exact signs, Gaussian units,
and active mode ranges.

**Revise before promotion** the conductor defect description: retain
\(\mathcal N\) as the phase defect, but add the distinct gradient defect
\(\mathcal G=\mathcal N-(p+q)h\) and formula (124.38).  Also record that
the primal (j,E) projector does not survive rowwise Poisson.  The clean
dual formula applies only to the full shifted square, with the accepted
primal safe packages subtracted as in (124.4).

**Promote after seam review** the target-safe active dual
product-equality diagonal (124.43) and the resulting fixed-power
off-diagonal inverse localization (124.45).  This strictly says that a
large row must enter the complete equal-mode shifted or unequal-mode
stationary aggregate; it does not estimate either one.

**Promote as a method obstruction, not as a lower bound**, the exact
joint Hessian, inverse map, Legendre phase, and determinant cancellation
(124.10)--(124.14), together with the explicitly diagnostic capacity
ledger (124.18)--(124.19).  Record that the interior stationary map
returns the reciprocal phase and that ordinary mode-sign square-root
credit remains a factor (Q=D^2/(L\sqrt X)\) above target.

**Retain open** (124.60), the flat-smooth quarter estimate, and
`M9-M2-smooth-unbalanced-three-quarter-estimate`.  The smallest lawful
survivor is the complete actual-sign off-product-equality stationary
aggregate (124.44), or its exact (k,h)-Poisson image including all
corner, endpoint, transition, and nonstationary modules.

**Reject as standalone continuations**: treating \(\mathcal N\) as the
gradient defect; transferring the primal near-(E) projector termwise to
the dual lattice; deleting the equal-mode shifted sector; using only
joint Hessian nondegeneracy; taking a modewise absolute value or a
coefficient-blind square norm; assigning random independent signs to the
rank-one quarter character; or retaining only the interior expression
(124.50) while dropping the Fejer and support boundary ledger.

**No change** is licensed for nonflat UNBAL, hard TOP, BAL, complete
UNBAL, M9-M2, either M1 route, endpoint uniformity, M9, the internal
one-third exponent, the audited external exponent, or the Gauss-circle
quarter target.
