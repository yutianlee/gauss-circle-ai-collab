# Round 151 conductor candidate: shifted-factor character ranges and the reciprocal self-return boundary

- Campaign: `m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate`
- Round: 151
- Role: conductor-selected proof kernel
- Starting graph SHA-256: `521f626e4af7e75e29d2ba909efb0d48864d5da4785de786acbd746d7559c11f`
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical
- Terminal label: `strict_large_wrap_character_range`

## 1. Result and exact scope

Put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq\sqrt M,\qquad
 Q=2\sqrt{ND/E}\asymp\frac{DR^2}{\sqrt M}.
\tag{151.C1}
$$

Round 151 proves two strict target-safe ranges and one exact structural
reduction for the growing-$M$ large-wrap interface.

First, for every nonzero centered wrap $k$, the mod-four character
transfers exactly to the two odd shifted differences after removal of the
full two-adic part of $k$.  The inverse transfer is not one-to-one: it has
a compulsory divisor fibre $h\mid g$ which remains in the two profiles,
the phase denominator, the support, and the reconstructed wrap.  This is
an exact reindexing, not an estimate.

Second, the wraps whose two-adic part is at least a fixed multiple of
$N/R^2\asymp R^2$ form only $O(1+R^2/Q)$ classes.  The accepted
arbitrary-packet fixed-wrap theorem therefore proves their complete
coefficient-weighted contribution is

$$
 O_\varepsilon(R^2D X^\varepsilon)
\tag{151.C2}
$$

at every allowed scale.

Third, the actual retained reciprocal profile has uniform sampled
bounded variation at all $M$.  Exact coprimality inversion and the two
mod-four residue classes then permit one-dimensional exponent-pair
estimates before the row energy is expanded.  Bourgain's global exponent
pair $(13/84,55/84)$ proves the complete compressed row is target-safe
when

$$
 \boxed{M^{29}\gg R^{52}D^{84}.}
\tag{151.C3}
$$

The stronger Tao--Trudgian--Yang pair
$(89/1282,997/1282)$ proves the complete low-$L$ subrow $L\leq L_0$
is target-safe when

$$
 \boxed{M^{819}\gg
 R^{1424}D^{1816}L_0^{534}.}
\tag{151.C4}
$$

At $D=1$, (151.C3) owns the full transformed row for
$M\gg R^{52/29}$.  Since centering makes every nonexact pair a collar
pair when $D=1$, subtraction of the accepted exact and fixed-wrap packet
owners gives the complete $D=1$ large-wrap collar in that range.  The
$D=1,L=1$ scalar already becomes target-safe in the wider range

$$
 M\gg R^{1424/819}.
\tag{151.C5}
$$

At the top scale $M\asymp R^2$, (151.C3) permits
$D\ll R^{1/14}$, while (151.C4) is

$$
 D^{1816}L_0^{534}\ll R^{214}.
\tag{151.C6}
$$

For $D>1$, these are whole-row or low-subrow owners.  They do not bound
an arbitrarily isolated signed collar subset after the energy expansion;
the collar and generic pieces are controlled jointly in (151.C3), and
only the recombined low-low component is controlled in (151.C4).

The exact $D=L=1$ reciprocal $B$-process has square-root dual phase,
the same mod-four character, and absolute capacity $RM^{1/4}$.  Its
principal transform is an involution: a second $B$-process returns the
original reciprocal phase and amplitude.  The dual main sum is therefore
neither an error nor an automatic gain.  This leaves the low-two-adic
large-wrap sum outside (151.C3)--(151.C4) open.

The full growing-$M$ collar is not proved.  No $t\geq2$ layer, independent
Round-138 cross term, full M9--M1 or M9--M2 estimate, endpoint assembly,
M9, bridge, quarter target, or global exponent follows.

## 2. Literal row and large-wrap residual

All $L,q,h,r$ below are positive odd integers.  The retained saddle
support is

$$
 q\asymp LQ,\qquad (L,q)=1,\qquad L\ll E.
\tag{151.C7}
$$

For a squarefree row write $d=\eta m$, where
$\eta\in\{1,2\}$ and $m=d_{\mathrm o}$ is odd squarefree.  For
$L_i=t_is_i^2$, with $t_i,s_i$ odd squarefree and $(t_i,s_i)=1$,
choose $a_i\mid t_i$, put $c_i=t_i/a_i$, and retain

$$
 n_i=a_iu_i(c_is_iv_i)^2,\qquad
 F=[a_1u_1,a_2u_2],\qquad
 P=\operatorname {rad}(c_1c_2s_1s_2v_1v_2),
\tag{151.C8}
$$

$$
 \beta_i=
 \frac{\mu(a_i)\mu(c_i)\mu(s_i)\mu(u_i)\mu(v_i)}
      {c_iu_iv_i^2}.
\tag{151.C9}
$$

Here $u_i\geq1$, while $v_i\geq1$ is odd squarefree and
$(v_i,c_is_i)=1$; the sums retain all these restrictions and the
literal finite support of each prefix.  The literal two-row arithmetic
coefficient is the finite expression

$$
 \sum_{\mathbf a,\mathbf u,\mathbf v}
 \sum_{z\mid P}\beta_1\beta_2\mu(z)
 {\mathbf1}_{(F,P)=1}{\mathbf1}_{Fz\mid m}
 \kappa_{\eta m,U}(n_1)\kappa_{\eta m,U}(n_2),
\tag{151.C10}
$$

with all restrictions from (151.C8)--(151.C9).  Thus both floor prefixes
and every forced or excluded odd prime remain literal.

For $q_i=hr_i$, $(r_1,r_2)=1$, define

$$
 \delta=L_1r_2-L_2r_1,\qquad
 \rho=N\delta-khr_1r_2,
 \qquad |\rho|\leq\frac{hr_1r_2}{2},
\tag{151.C11}
$$

with the unique centered integer $k$.  A tie is impossible because the
modulus $hr_1r_2$ is odd.  Fix an accepted symmetric packet
$\mathcal K_0$ of $O(1+R^2/Q)$ wrap classes.  The frozen residual is

$$
\begin{aligned}
 \mathcal C_{\mathrm{LW},U}={}&
 \sum_{\eta=1,2}
 \sum_{\substack{m\ \mathrm{odd\ squarefree}\\\eta m\asymp D}}
 \sum_{\substack{L_i,q_i\ \mathrm{satisfy}\ (151.C7)\\
                  q_i=hr_i,\ (r_1,r_2)=1\\
                  k\notin\mathcal K_0\\
                  0<|\rho|\leq hr_1r_2/D}}
 &\frac{\chi_4(L_1L_2r_1r_2)}{L_1L_2}
 e\!\left(\frac{\eta m\rho}{hr_1r_2}\right)\\
 &\times\mathscr W_{\eta m,U}(L_1/q_1)
 \overline{\mathscr W_{\eta m,U}(L_2/q_2)}
 \times\bigl[\text{the exact sum }(151.C10)\bigr].
\end{aligned}
\tag{151.C12}
$$

No coefficient, prefix, profile, character, common factor, imprimitive
denominator, or phase has been replaced by an arbitrary weight in
(151.C12).

Before expansion, the exact compressed row is

$$
 G_U(d)=
 \sum_L\frac{\chi_4(L)B_{d,U}(L)}L
 \sum_{\substack{q\asymp LQ\ \mathrm{odd}\\(L,q)=1}}
 \chi_4(q)\mathscr W_{d,U}(L/q)e(NdL/q),
\tag{151.C13}
$$

and the accepted prefix-uniform norm is

$$
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}
 \ll_\varepsilon X^\varepsilon.
\tag{151.C14}
$$

## 3. Exact two-adic transfer and recovery

Assume $k\ne0$, put $j=\nu_2(|k|)$, and define

$$
 A=NL_1-khr_1,\qquad B=NL_2+khr_2.
\tag{151.C15}
$$

Direct expansion and (151.C11) give

$$
 AB=N^2L_1L_2+kh\rho,
\tag{151.C16}
$$

$$
 r_2A=NL_2r_1+\rho,\qquad
 r_1B=NL_1r_2-\rho.
\tag{151.C17}
$$

On the collar,

$$
 \frac{|\rho|}{NL_2r_1}
 \leq\frac{q_2}{DNL_2}
 \ll\frac{Q}{DN}\ll R^{-2},
\tag{151.C18}
$$

and symmetrically for the other factor.  Hence $A,B>0$, including when
a denominator divides $N$.

Write $k=2^j\kappa$ with $\kappa$ odd and signed, and put

$$
 x=\frac{NL_1-A}{2^j}=\kappa hr_1,\qquad
 y=\frac{B-NL_2}{2^j}=\kappa hr_2.
\tag{151.C19}
$$

The integers $x,y$ are odd, nonzero, and have the same sign.  Since
$xy=\kappa^2h^2r_1r_2$,

$$
 \boxed{
 \chi_4(L_1L_2r_1r_2)=\chi_4(L_1L_2xy).}
\tag{151.C20}
$$

This uses neither the sign of $k$ nor the parity of $N$.  It is generally
unlawful to apply $\chi_4$ directly to $A$ or $B$.  If
$n=\nu_2(N)$, then

$$
\begin{array}{c|c}
 j<n&(\nu_2(A),\nu_2(B))=(j,j)\\
 j>n&(\nu_2(A),\nu_2(B))=(n,n)\\
 j=n&(\nu_2(A),\nu_2(B))\geq(n+1,n+1).
\end{array}
\tag{151.C21}
$$

Also, since $\delta$ is even and $hr_1r_2$ is odd, $\rho$ is odd
exactly when $j=0$.  More precisely, put $\nu_2(0)=+\infty$; for
$t=\nu_2(\delta)$ and $j\ne n+t$,

$$
 \nu_2(\rho)=\min(j,n+t),
\tag{151.C22}
$$

while equality gives valuation at least $j+1$.

Conversely, fix $A,B,j$ and impose

$$
 2^j\Vert NL_1-A,\qquad
 2^j\Vert B-NL_2,\qquad xy>0.
\tag{151.C23}
$$

Let

$$
 g=(|x|,|y|),\qquad \epsilon=\operatorname {sgn}x,
 \qquad r_1=|x|/g,\quad r_2=|y|/g.
\tag{151.C24}
$$

Then $r_1,r_2$ are positive odd and coprime, and

$$
 \delta=L_1r_2-L_2r_1,\qquad
 \rho=N\delta-\epsilon2^jg r_1r_2.
\tag{151.C25}
$$

Every original preimage is recovered by a positive divisor $h\mid g$
through

$$
 k=\epsilon2^j\frac gh,\qquad kh=\epsilon2^jg,
 \qquad q_i=hr_i,
\tag{151.C26}
$$

subject to the literal support, coprimality, centeredness, collar, and
$k\notin\mathcal K_0$ tests.  Conversely every divisor passing those
tests is an original tuple.  The fibre has at most
$\tau(g)\ll_\varepsilon X^\varepsilon$ elements, but it cannot be
deleted: $q_i$, both profile samples, the phase denominator, and $k$
vary with $h$.

With $2^{J_*}\asymp R^2$, the remaining low-two-adic residual is therefore
the exact joint sum

$$
\begin{aligned}
 \sum_{d,L_1,L_2}\sum_{j<J_*}
 \sum_{\substack{A,B>0\\(151.C23)}}
 \sum_{h\in\mathfrak H(A,B,j)}
 &\chi_4(L_1L_2xy)
 \frac{B_{d,U}(L_1)\overline{B_{d,U}(L_2)}}{L_1L_2}\\
 &\times\mathscr W_{d,U}(L_1/(hr_1))
 \overline{\mathscr W_{d,U}(L_2/(hr_2))}
 e\!\left(\frac{d\rho}{hr_1r_2}\right),
\end{aligned}
\tag{151.C27}
$$

The displayed $B_{d,U}(L_1)\overline{B_{d,U}(L_2)}$ is shorthand for,
not an additional multiplier of, the exact expansion (151.C10), with
every support restriction understood literally.  This reindexes all
remaining shifts before absolute values but proves no cancellation by
itself.

## 4. High-two-adic target range

Support and centering give

$$
 |k|\ll N/Q.
\tag{151.C28}
$$

Indeed $|\delta|\ll L_1L_2Q/h$ and
$hr_1r_2\asymp L_1L_2Q^2/h$.  Choose $J_*$ with
$2^{J_*}\asymp N/R^2\asymp R^2$.  The number of nonzero signed
integers in (151.C28) divisible by $2^{J_*}$ is

$$
 \ll1+\frac{N/Q}{2^{J_*}}
 \ll1+\frac{R^2}{Q}.
\tag{151.C29}
$$

The set $\nu_2(|k|)\geq J_*$ is a subset of these multiples, and
intersecting it with $k\notin\mathcal K_0$ only decreases the count.
Round 150 already sums every $d,L_i,h$ and coefficient weight for one
arbitrary fixed wrap at cost $DQX^\varepsilon$.  Therefore

$$
 DQ\left(1+\frac{R^2}{Q}\right)X^\varepsilon
 \ll R^2D X^\varepsilon,
\tag{151.C30}
$$

which proves (151.C2) and leaves exactly $j<J_*$.

## 5. Actual-profile variation and exponent-pair ranges

Write $q=LQy$ on one retained compact support component.  The sampled
physical coordinate is exactly

$$
 e_0=\frac{4NdL^2}{q^2}=\frac{dE}{D}y^{-2}.
\tag{151.C31}
$$

The accepted Round-148 factorization and derivative ledger give first
derivative $O(1)$ on bulk pieces, $O(M^{1/2})$ on a radial transition of
normalized $y$-length $O(M^{-1/2})$, and $O(D^{1/2})$ on a cone
transition of length $O(D^{-1/2})$.  There are only finitely many factors
and transition components, all have bounded supremum, and zero extension
adds only finitely many bounded endpoint jumps.  The product-variation
inequality therefore gives, uniformly at every scale,

$$
 \boxed{
 \|\mathscr W_{d,U}(L/\cdot)\|_\infty+
 \operatorname {Var}_q\mathscr W_{d,U}(L/q)
 \ll_\varepsilon X^\varepsilon.}
\tag{151.C32}
$$

Sampling on a monotone arithmetic progression cannot increase variation.
The exact floor prefix is in $B_{d,U}(L)$ and is independent of $q$.
The previously peeled radial-prefix and cone boundary pieces retain their
accepted owners; a collar-short terminal prefix is not silently returned
to (151.C32).

Define

$$
 S_{d,L}=
 \sum_{\substack{q\asymp LQ\ \mathrm{odd}\\(L,q)=1}}
 \chi_4(q)\mathscr W_{d,U}(L/q)e(NdL/q).
\tag{151.C33}
$$

Use exact Mobius inversion and multiplicativity:

$$
 {\mathbf1}_{(L,q)=1}=\sum_{c\mid(L,q)}\mu(c),\qquad
 \chi_4(cm)=\chi_4(c)\chi_4(m).
\tag{151.C34}
$$

For $c\mid L$, write $q=cm$, split $m\equiv1,3\pmod4$, and put
$m=4n+a$.  The interval length and phase are

$$
 H_c\asymp\frac{LQ}{c},\qquad
 f_c(n)=\frac{NdL}{c(4n+a)}.
\tag{151.C35}
$$

Writing $f_c(n)=\mathcal T_cF_c(n/H_c)$ gives

$$
 \mathcal T_c\asymp\frac{Nd}{Q},\qquad
 \frac{\mathcal T_c}{H_c}\asymp\frac{cE}{L}.
\tag{151.C36}
$$

The bounded residue shift in $F_c$ has the uniform reciprocal derivative
pattern.  Proper subintervals are allowed.  If
$\mathcal T_c\geq H_c$, an exponent pair $(\kappa,\lambda)$ gives

$$
 \sum_{n\in I}e(f_c(n))
 \ll_\varepsilon
 (E/L)^\kappa(LQ)^\lambda
 c^{\kappa-\lambda}X^\varepsilon.
\tag{151.C37}
$$

The finite support only guarantees $L\ll E$, so the ratio in (151.C36)
can be a fixed constant below one at an upper support edge.  There the
second-derivative estimate is $O(H_c^{1/2})$, which is dominated by the
right side of (151.C37) because every pair used below has
$\lambda>1/2$ and $\mathcal T_c/H_c$ is bounded below by a fixed support
constant.  Bounded intervals are trivial.  Thus (151.C37) holds on the
complete support without applying a source theorem outside its hypotheses.

Abel summation with (151.C32), followed by
$\sum_{c\mid L}c^{\kappa-\lambda}\ll_\varepsilon X^\varepsilon$, gives

$$
 \boxed{
 |S_{d,L}|\ll_\varepsilon
 (E/L)^\kappa(LQ)^\lambda X^\varepsilon.}
\tag{151.C38}
$$

### 5.1 Correct Bourgain source interface and the complete row

Bourgain's Theorem 4 first proves the relevant estimate in the direct
window

$$
 \mathcal T^{17/42}\ll H\ll\mathcal T^{1/2}.
\tag{151.C39}
$$

That is not the scope of Theorem 6.  Section 5 explicitly promotes

$$
 (\kappa,\lambda)=\left(\frac{13}{84},\frac{55}{84}\right)
\tag{151.C40}
$$

to an exponent pair, treats $H>\sqrt{\mathcal T}$ by rescaling and the
$B$-process, and treats proper subintervals by phase extension and the
partial-sum device.  The reciprocal phase in (151.C35) is in that model
class.  Hence inheriting (151.C39) as a restriction on Theorem 6 is a
source error; the global pair is legal in (151.C38).

Since $\lambda-\kappa=1/2$, (151.C14) gives

$$
 |G_U(d)|\ll_\varepsilon
 E^{13/84}Q^{55/84}X^\varepsilon.
\tag{151.C41}
$$

After squaring and summing $O(D)$ rows,

$$
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll_\varepsilon
 D E^{13/42}Q^{55/42}X^\varepsilon.
\tag{151.C42}
$$

Its ratio to $R^2D$ is

$$
 \frac{E^{13/42}Q^{55/42}}{R^2}
 =\left(\frac{D^{84}R^{52}}{M^{29}}\right)^{1/84}
\tag{151.C43}
$$

up to fixed support constants.  This proves (151.C3).

### 5.2 Tao--Trudgian--Yang low-$L$ corridor

The global Tao--Trudgian--Yang pair is

$$
 (\kappa,\lambda)=
 \left(\frac{89}{1282},\frac{997}{1282}\right),\qquad
 \lambda-\kappa-\frac12=\frac{267}{1282}.
\tag{151.C44}
$$

For $L\leq L_0$, (151.C14) and (151.C38) give

$$
 |G_{U,\leq L_0}(d)|
 \ll_\varepsilon
 E^{89/1282}Q^{997/1282}
 L_0^{267/1282}X^\varepsilon.
\tag{151.C45}
$$

The squared ratio to the per-row target is

$$
 \frac{E^{178/1282}Q^{1994/1282}L_0^{534/1282}}{R^2}
 =\left(
 \frac{R^{1424}D^{1816}L_0^{534}}{M^{819}}
 \right)^{1/1282}.
\tag{151.C46}
$$

This proves (151.C4).  The complementary $L>L_0$ square and the
low-high cross term are not included.

## 6. The $D=L=1$ reciprocal transform and self-return

At $D=L=1$, put

$$
 w_U(q)=\mathscr A_{1,M,U}\!\left(1,\frac{4N}{q^2}\right),\qquad
 S_U=\sum_{q>0}\chi_4(q)w_U(q)e(N/q).
\tag{151.C47}
$$

Before Poisson summation, extend this compactly supported smooth weight
by zero to the whole real line.

The literal compressed-row component is
$\widetilde S_U=B_{1,U}(1)S_U$, with
$|B_{1,U}(1)|\ll_\varepsilon X^\varepsilon$; the corresponding pair
component is $\widetilde S_U\overline{\widetilde S_V}$.  Thus the
coefficient is not being suppressed in the deductions below.

The identity

$$
 \chi_4(q)=\frac{e(q/4)-e(-q/4)}{2i}
\tag{151.C48}
$$

holds for every integer and kills even $q$.  For
$f_\sigma(x)=N/x+\sigma x/4$, Poisson frequency $n$ has a stationary
point precisely when

$$
 \lambda=\frac\sigma4-n>0,\qquad
 x_{\sigma,n}=\sqrt{N/\lambda}.
\tag{151.C49}
$$

Put $\ell=\sigma-4n$.  Then $\ell>0$ is odd,
$\ell\equiv\sigma\pmod4$, and

$$
 x_{\sigma,n}=2\sqrt{N/\ell},\qquad
 f_\sigma(x_{\sigma,n})-nx_{\sigma,n}=\sqrt{N\ell},
\tag{151.C50}
$$

$$
 f_\sigma''(x_{\sigma,n})^{-1/2}
 =2N^{1/4}\ell^{-3/4},\qquad
 \frac{4N}{x_{\sigma,n}^2}=\ell.
\tag{151.C51}
$$

Combining the two branches, the interior principal dual wave is

$$
 \boxed{
 N^{1/4}e(-1/8)
 \sum_{\substack{\ell>0\ \mathrm{odd}\\
                  \ell\ \mathrm{in\ the\ reversed\ dual\ support}}}
 \chi_4(\ell)\ell^{-3/4}
 \mathscr A_{1,M,U}(1,\ell)e(\sqrt{N\ell}).}
\tag{151.C52}
$$

For a generic piecewise continuation, every literal integer jump requires
the Fejer--Poisson correction from the Fourier-series average to the
literal value, and a saddle at, or within one stationary width of, an
endpoint has its truncated Fresnel factor rather than a full Gaussian.
The actual retained Round-148 amplitude is instead compact smooth after
the hard radial-prefix and cone collars receive their prior owners.  Its
accepted derivative, middle-buffer, and tail ledger supplies the
boundary-complete relation

$$
 P_U=e(1/8)N^{-1/4}S_U+O_\varepsilon(X^\varepsilon),
 \qquad
 P_U:=\sum_{\substack{\ell>0\ \mathrm{odd}}}
 \chi_4(\ell)\ell^{-3/4}
 \mathscr A_{1,M,U}(1,\ell)e(\sqrt{N\ell}),
\tag{151.C52a}
$$

or equivalently

$$
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon).
\tag{151.C52b}
$$

Thus the actual application has no uncontrolled every-integer jump seam;
the first open step is the signed estimate for $P_U$.  Formula (151.C52)
is its principal main wave, not the whole generic piecewise identity.

The principal transform is involutive.  In the unit-spaced dual variable
put

$$
 \lambda=m+\frac\sigma4,\qquad
 g_\sigma(m)=2\sqrt{N\lambda},\qquad
 q(m)=g_\sigma'(m)=\sqrt{N/\lambda}.
\tag{151.C53}
$$

For a second Poisson frequency $p>0$, the saddle is
$m_p=N/p^2-\sigma/4$, and its Legendre phase is

$$
 g_\sigma(m_p)-pm_p
 =\frac Np+\frac{\sigma p}{4}.
\tag{151.C54}
$$

The two stationary amplitudes multiply to one,

$$
 \left(\frac{N^{1/4}}{\sqrt2}\lambda^{-3/4}\right)
 \left(\sqrt2N^{-1/4}\lambda^{3/4}\right)=1,
\tag{151.C55}
$$

and the curvature signs contribute $e(1/8)e(-1/8)=1$.  Thus the
second phase and principal stationary symbol return the original
reciprocal wave.  This does not assert exact composition of every lower
symbol, nonstationary integral, or endpoint transition; those terms remain
in the accepted boundary ledger.

Here $Q\asymp R^2M^{-1/2}$, the dual length is $\asymp M$, and one
dual term has size $RM^{-3/4}$.  The two elementary row capacities are

$$
 \min\{R^2M^{-1/2},\ RM^{1/4}\}X^\varepsilon.
\tag{151.C56}
$$

The dual is row-target-sized for bounded $M$; the original length is
row-target-sized at $M\asymp R^2$; the intermediate range loses a
power.  Equation (151.C55) explains why another bare $B$-process does
not supply the missing saving.  This is a no-go for iteration of that
principal transform, not a lower bound for the signed sum.

## 7. First unproved object and controls

After removing the accepted exact, bounded-$M$, fixed-wrap packet,
high-two-adic, complete Bourgain-row, and TTY low-subrow owners in their
respective ranges, the first unproved large-wrap object is (151.C27) with

$$
 j<J_*,\qquad k\notin\mathcal K_0,\qquad
 0<|\rho|\leq hr_1r_2/D,
\tag{151.C57}
$$

outside (151.C3), or outside (151.C4) for the low-$L$ component.  The
character is now a product of odd shifted differences, but the divisor
$h\mid g$ remains coupled to both profiles, support, phase denominator,
and reconstructed wrap.  Taking absolute values after the bijection gives
no saving; separately summing fixed $(h,k,\rho)$ bounds returns the
already rejected adverse capacity.

The control decisions are:

| Control | Decision |
|---|---|
| `literal_large_wrap_residual` | GREEN as (151.C12); open as a uniform estimate outside the strict ranges. |
| `accepted_small_packet_exclusion` | GREEN.  Every shifted-factor residual has $k\notin\mathcal K_0$; new ranges subtract rather than recount accepted owners. |
| `two_adic_character_transfer` | GREEN.  Equations (151.C19)--(151.C22) cover both signs of $k$, all parities of $N$, and every valuation relation. |
| `shifted_factor_positivity_and_recovery` | GREEN.  Equations (151.C17)--(151.C27) retain positivity, divisibility, signs, gcd, centering, support, and the $h\mid g$ fibre. |
| `joint_k_rho_h_summation` | GREEN/open split.  High-adic wraps and the source-legal row corridors are summed; the low-adic isolated residual outside them remains open. |
| `high_two_adic_sparse_range` | GREEN by (151.C28)--(151.C30). |
| `D1_L1_reciprocal_scalar` | GREEN in the strict range (151.C5); open below it after bounded $M$. |
| `exact_character_fourier_identity` | GREEN by (151.C48), with both branches retained. |
| `boundary_complete_B_process` | GREEN for the actual-profile transform (151.C52a)--(151.C52b) and for the principal-wave derivation.  The generic Fejer/Fresnel identity is not misidentified with an actual jump obstruction. |
| `actual_profile_derivative_ledger` | GREEN for bounded variation by (151.C31)--(151.C32) and for the accepted Round-148 transform error in (151.C52a).  The open term is the signed main wave $P_U$, not a missing continuum profile. |
| `dual_self_return_vs_gain` | GREEN as the principal-transform no-go (151.C53)--(151.C56). |
| `tuple_absolute_signed_separation` | GREEN.  Wrap counts, weighted absolute packet mass, signed rows, and adverse capacities remain distinct. |
| `source_theorem_large_wrap_match` | GREEN for Bourgain and TTY on the recombined rows; no audited shifted-divisor source directly estimates the isolated low-adic collar. |
| `all_M_D_E_Q_L_h_k_rho_power_ledger` | GREEN through (151.C3)--(151.C6), (151.C28)--(151.C30), (151.C43), (151.C46), and (151.C56). |
| `prime_parity_prefix_imprimitive_controls` | GREEN.  Even squarefree rows, odd-prime masks, both parities of $N$, exact prefixes, common factors, imprimitive fractions, and $q_i\mid N$ remain. |
| `generic_tge2_cross_and_downstream_scope` | GREEN.  Whole-row versus isolated-collar scope is explicit; all named complements and downstream obligations remain open. |

The primary-source correction is material: Bourgain Theorem 6 is global
in its exponent-pair class, whereas (151.C39) is only the direct Theorem 4
window.  The project source card is now corrected; subject to terminal
review, the narrower graph source-audit node must be corrected by the
State Patch rather than used to reject (151.C3).

No numerical experiment was used.
