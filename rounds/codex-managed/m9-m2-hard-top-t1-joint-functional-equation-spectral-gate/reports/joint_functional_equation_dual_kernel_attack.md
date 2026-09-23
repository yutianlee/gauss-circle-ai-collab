# Round 169 discovery report: exact joint functional equation and dual kernel

- Campaign: `m9-m2-hard-top-t1-joint-functional-equation-spectral-gate`
- Task: `joint_functional_equation_dual_kernel_attack`
- Role: discovery
- Starting graph: `a360b2913563c9c288438751729c5033acd2e91ee613e44f171e1d31bc7441be`
- Status: candidate evidence only

## 1. Result

**Exact collapsed-Mobius dual-kernel identity and scoped self-return no-go.**
The residual Euler coefficients can be computed completely.  They are
jointly multiplicative, are supported on the six odd-prime exponent
pairs

\[
 (0,0),(2,0),(0,2),(1,1),(2,1),(1,2),
\]

and on the two two-adic pairs \((0,0),(0,2)\).  More importantly, they
are exactly the Round-162 Mobius-opening coefficients after openings with
the same \((Q,R)\) are collapsed:

\[
 \boxed{
 g(Q,R)=\chi _4(Q)
 \sum_{\substack{u,v,c\geq1;\ u,c\ \text{odd}\\
                  [u^2,c]=Q,\ [v^2,c]=R}}
 \mu(u)\mu(v)\mu(c).}
\tag{169.D1}
\]

This includes the even-second-leg branch: locally at \(2\), the two
coefficients are \(g_2(1,1)=1\) and \(g_2(1,4)=-1\).

Both completed GL(1) functional equations may then be applied jointly,
with no positive norm and no truncation.  If

\[
 \widetilde{\mathcal B}(\xi,\nu)
 =\int_{\mathbb R^2}\mathcal B(x,z)e(-\xi x-\nu z)\,dx\,dz,
\tag{169.D2}
\]

where the exact cardinal weight is extended by zero, choose integers
\(M_x,M_z\ll L\) with
\(\operatorname{supp}\mathcal B\subset(0,M_x)\times(0,M_z)\).  Exact
finite Poisson gives

\[
 \boxed{
 \mathcal S_{L,1}
 =\frac i2\sum_{Q\leq M_x}\sum_{R\leq M_z}
   \frac{g(Q,R)}{QR}
   \sum_{\substack{k\in\mathbb Z\\k\ \text{odd}}}\chi _4(k)
   \sum_{\ell\in\mathbb Z}
   \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).}
\tag{169.D3}
\]

Let \(Z_{\rm fin}\) and \(\mathcal D_{\rm fin}\) be respectively the
\(\ell=0\) and \(\ell\ne0\) parts of the **finite** right side of
(169.D3).  The crucial residue law is

\[
 \boxed{
 R_\zeta
 =\frac i2\sum_{Q\leq M_x}\sum_{R\geq1}
   \frac{g(Q,R)}{QR}
   \sum_{\substack{k\in\mathbb Z\\k\ \text{odd}}}\chi _4(k)
   \widetilde{\mathcal B}\!\left(\frac{k}{4Q},0\right),
 \qquad
 \mathcal I_\eta=\mathcal D_{\rm fin}+Z_{\rm fin}-R_\zeta.}
\tag{169.D4}
\]

The \(R\)-series in the residue is absolutely convergent for fixed
\(Q\).  For \(R>M_z\), the whole physical \((Q,R)\)-block is zero, so
its complete Poisson zero and nonzero modes cancel.  It follows, in the
specified order which completes the Fourier sums inside each \(R\)-block,
that

\[
 \boxed{
 \mathcal I_\eta
 =\frac i2\sum_{Q\leq M_x}
   \mathop{\sum_{R\geq1}}\limits_{R\text{-block order}}
   \frac{g(Q,R)}{QR}
   \sum_{\substack{k\in\mathbb Z\\k\ \text{odd}}}\chi _4(k)
   \sum_{\ell\neq0}
   \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).}
\tag{169.D4a}
\]

This is not an unrestricted rearrangement of three infinite sums.  The
equivalent finite active kernel, which contains the stationary geometry,
is obtained by pairing signs:

\[
 \mathcal D_{\rm fin}
 =2\sum_{Q\leq M_x}\sum_{R\leq M_z}\frac{g(Q,R)}{QR}
   \sum_{\substack{k\geq1\\k\ \text{odd}}}\chi _4(k)
   \sum_{\ell\geq1}\int_{\mathbb R^2}\mathcal B(x,z)
   \sin\!\frac{\pi kx}{2Q}\cos\!\frac{2\pi\ell z}{R}\,dx\,dz.
\tag{169.D5}
\]

Moreover,

\[
 \left|Z_{\rm fin}-R_\zeta\right|
 \ll_\varepsilon L^2J^{-1}X^\varepsilon,
\tag{169.D5a}
\]

so this explicit residue-completion correction is target-safe.  Thus the
target for \(\mathcal I_\eta\) reduces to the finite active signed kernel
\(\mathcal D_{\rm fin}\), not to a finite nonzero-mode kernel with its
zero mode incorrectly identified as the full residue.

The joint phase in its only positive interior stationary branch is

\[
 J\sqrt{xz}-\frac{kx}{4Q}-\frac{\ell z}{R},
\qquad k\ell=XQR,
\qquad Q\ell\leq Rk\leq4Q\ell.
\tag{169.D6}
\]

The finite active kernel (169.D5) is coefficientwise the collapsed
version of the accepted Round-162 character-Poisson followed by ordinary
Poisson transform.  Formula (169.D4a) gives the same kernel after
adjoining the physically zero \(R>M_z\) blocks; their nonzero modes are
the compulsory negatives of their zero modes and supply exactly the
correction in (169.D4).  Hence the joint functional equation returns to
the pre-stationary Mobius--Poisson family **up to the explicit target-safe
residue-completion correction** (169.D5a), not by identifying the finite
zero mode with \(R_\zeta\).  On a recombined smooth active block its
principal saddle is precisely the Round-162 product collar.  Termwise
positive control of one opening has capacity
\(\sqrt{JL}X^\varepsilon\), hence still exceeds the target by
\(H/L+O(L^{-1})\); absolute summation over active \((Q,R)\) is worse.
The literal cardinal weight has \(O(L^2)\) unit cells and does not
lawfully inherit the smooth radial collar without an additional
recombination theorem.

Therefore the two functional equations, their exact coefficient
convolution, and their joint phase do **not** supply the requested signed
gain.  After paying (169.D5a), the first remaining step is exactly a new
signed estimate for the finite active \((Q,R,k,\ell)\) aggregate
(169.D5), before every positive norm.  This is the open Round-162 signed
family in collapsed coordinates.  The result is a
`t1_joint_FE_spectral_self_return_no_go`, scoped to bare joint
functional-equation dualization and subsequent termwise-positive
placements.  It does not rule out a bespoke theorem acting on the whole
signed aggregate.

## 2. Exact statement and hypotheses

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad q_X=X/y^2,
 \qquad H=\lfloor yX^{-1/4}\rfloor=\sqrt J+O(1),
 \qquad 1\ll L\ll H,
\tag{169.D7}
\]

and let \(\mathcal B\) be exactly the disjoint cardinal interpolation
from (168.K16).  In particular, it is a finite \(C_c^\infty\) function
supported in the positive quadrant, and its lattice values contain the
complete amplitude, phase, half-open product shell, real-centre floors,
stars, cone edges, profile transitions, parity branch, endpoints, and
zero-extension convention.  No global smooth replacement is made.
Fix integers \(M_x,M_z\ll L\) for which
\(\operatorname{supp}\mathcal B\subset(0,M_x)\times(0,M_z)\).

For \(\Re s_j>1/2\), write

\[
 G(s_1,s_2)=\sum_{Q,R\geq1}\frac{g(Q,R)}{Q^{s_1}R^{s_2}}.
\tag{169.D8}
\]

The exact local law is

\[
\begin{array}{c|rrrrrr}
(v_p(Q),v_p(R))&(0,0)&(2,0)&(0,2)&(1,1)&(2,1)&(1,2)\\ \hline
g_p(Q,R)&1&-1&-1&-\chi _4(p)&1&\chi _4(p)
\end{array}
\qquad(p>2),
\tag{169.D9}
\]

with every other odd-prime local coefficient zero, and

\[
 g_2(1,1)=1,\qquad g_2(1,4)=-1,
\tag{169.D10}
\]

with every other two-adic coefficient zero.  Hence \(Q\) is odd,
\(v_2(R)\in\{0,2\}\), and both variables are cube-free on the support.
The exact weighted absolute mass is

\[
\begin{aligned}
 \sum_{Q,R}\frac{|g(Q,R)|}{Q^{\sigma _1}R^{\sigma _2}}
  ={}&(1+2^{-2\sigma _2})
 \prod_{p>2}\bigl(1+p^{-2\sigma _1}+p^{-2\sigma _2}
 +p^{-\sigma _1-\sigma _2}\\
 &\hspace{42mm}+p^{-2\sigma _1-\sigma _2}
 +p^{-\sigma _1-2\sigma _2}\bigr).
\end{aligned}
\tag{169.D11}
\]

At \(\sigma _1=\sigma _2=\alpha=1/2+\eta\),

\[
 \sum_{Q,R}\frac{|g(Q,R)|}{(QR)^\alpha}
 =(1+2^{-1-2\eta})
 \prod_{p>2}(1+3p^{-1-2\eta}+2p^{-3/2-3\eta})
 \asymp \zeta(1+2\eta)^3\asymp\eta^{-3}.
\tag{169.D12}
\]

The implied constants are absolute for \(0<\eta\leq1/4\).  This mass is
used only to justify the pre-transform expansion on the \(\alpha\)-line;
it is not applied as an \(\ell^1\) norm to the transformed aggregate.

The completed functions and their exact functional equations are

\[
 \Lambda_\zeta(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad \Lambda_\zeta(s)=\Lambda_\zeta(1-s),
\tag{169.D13}
\]

and

\[
 \Lambda_4(s)=\left(\frac4\pi\right)^{(s+1)/2}
 \Gamma\!\left(\frac{s+1}{2}\right)L(s,\chi _4),
 \qquad \Lambda_4(s)=\Lambda_4(1-s).
\tag{169.D14}
\]

Here zeta has conductor one, even parity, root number \(+1\), and its
completion has the poles at \(0,1\).  The character \(\chi _4\) is
primitive of conductor four and odd parity; its Gauss sum is \(2i\), so
its root number is \(2i/(i\sqrt4)=+1\), and \(\Lambda_4\) is entire.
Equivalently,

\[
 \zeta(s)=\mathcal X_\zeta(s)\zeta(1-s),\qquad
 \mathcal X_\zeta(s)=
 \pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)},
\tag{169.D15}
\]

\[
 L(s,\chi _4)=\mathcal X_4(s)L(1-s,\chi _4),\qquad
 \mathcal X_4(s)=
 \left(\frac4\pi\right)^{1/2-s}
 \frac{\Gamma(1-s/2)}{\Gamma((s+1)/2)}.
\tag{169.D16}
\]

Under precisely these hypotheses, (169.D1)--(169.D6) and the ordered
residue completion (169.D4a) hold with no transform truncation or
remainder; (169.D5a) is the explicit target-safe correction between the
finite and completed zero modes.

## 3. Proof and derivation

### 3.1. Prime-by-prime coefficient law

For odd \(p\), put \(x=\chi _4(p)p^{-s_1}\) and \(z=p^{-s_2}\).
The accepted factor is

\[
 G_p=1-x^2-z^2-xz+x^2z+xz^2.
\tag{169.D17}
\]

Reading off the two exponents gives (169.D9).  At \(2\),
\(G_2=1-2^{-2s_2}\), giving (169.D10).  Multiplication over primes
proves joint multiplicativity and the support statement.  Taking
absolute values locally gives (169.D11).  On the equal line the three
quadratic monomials have size \(p^{-1-2\eta}\), and the two cubic
monomials have size \(p^{-3/2-3\eta}\), proving the exact product in
(169.D12).  Dividing it by the Euler product for
\(\zeta(1+2\eta)^3\) leaves a product whose local logarithms are
\(O(p^{-3/2}+p^{-2-4\eta})\), uniformly for \(0<\eta\leq1/4\).
This proves the last comparison in (169.D12).

### 3.2. The completed equations, pole, and contour directions

The root-number and parity data in (169.D13)--(169.D16) are immediate
from the displayed completions; in particular, no character pole or
character main term exists.  Gamma duplication and reflection also give

\[
 \mathcal X_\zeta(s)
 =2^s\pi^{s-1}\Gamma(1-s)\sin\frac{\pi s}{2},
\qquad
 \mathcal X_4(s)
 =\left(\frac\pi2\right)^{s-1}\Gamma(1-s)
   \cos\frac{\pi s}{2}.
\tag{169.D18}
\]

These are respectively the Mellin kernels of
\(2\cos(2\pi u)\) and \(\sin(\pi u/2)\) against \(u^{-s}\).  Thus the
two different gamma parities become an ordinary cosine transform and an
odd-character sine transform; they cannot be replaced by a common-height
or common-parity kernel.

The initial \(s_2\)-contour displacement from \(\Re s_2>1\) to
\(\alpha\) is leftward and crosses only the pole of \(\zeta(s_2)\) at
one, with positive residue \(R_\zeta\).  The subsequent \(s_1\) shift
crosses no pole.  Formula (169.D12) permits expansion of \(G\) on the
\(\alpha\)-lines.  For one fixed coefficient pair \((Q,R)\), insert both
equations (169.D15)--(169.D16) and shift that paired integrand to
\(\Re s_1=\Re s_2=-\delta\), \(\delta>0\).  No pole is crossed: the zeta
pole at one is already to the right, and the apparent factor singularity
at zero cancels inside
\(\mathcal X_\zeta(s)\zeta(1-s)=\zeta(s)\).  On the new lines both dual
Dirichlet series have real part \(1+\delta\) and are absolutely
convergent.  If \(w_j=1-s_j\) is introduced, an upward \(s_j\)-line maps
to a downward \(w_j\)-line and \(ds_j=-dw_j\); reversing it restores the
standard upward orientation with no residual sign.  Rapid vertical
decay of \(\widehat{\mathcal B}\) removes the horizontal sides.

This shift is **coefficientwise only**.  On \(\Re s_j=-\delta\), the
factors \(Q^{-s_1}R^{-s_2}=Q^\delta R^\delta\) grow, and (169.D12) gives
no right to resum the unrestricted \(G\)-series there.  Such a resummation
would be illicit and is not used.  The lawful starting point in Sections
3.3--3.4 is the exact finite physical convolution: compact positive
support makes a whole \((Q,R)\) physical block zero when \(Q>M_x\) or
\(R>M_z\), and finite Poisson proves (169.D3) blockwise.  Splitting off
the Mellin residue is subtler.  It requires the full \(R\geq1\) zero-mode
sum, not merely \(R\leq M_z\).  For each fixed physical \(Q\), that
\(R\)-series is absolutely convergent, and the missing \(R>M_z\)
nonzero modes are restored in complete \(R\)-blocks.  No \(Q\)-tail is
needed: the character-side physical samples vanish identically for
\(Q>M_x\).  The coefficientwise contour calculation identifies the
sine--cosine gamma kernel, while this block-grouped Poisson calculation
proves the summed formula, fixes the constants, and establishes endpoint
legality.

### 3.3. Exact collapse of the Mobius openings

Let

\[
 M(Q,R)=
 \sum_{\substack{u,v,c\geq1;\ u,c\ \text{odd}\\
                  [u^2,c]=Q,\ [v^2,c]=R}}
 \mu(u)\mu(v)\mu(c).
\tag{169.D19}
\]

This function is jointly multiplicative.  At an odd prime, the eight
states \((v_p(u),v_p(v),v_p(c))\in\{0,1\}^3\) give

\[
\begin{array}{c|c|c}
(u,v,c)&(v_p(Q),v_p(R))&
 \chi _4(p)^{v_p(Q)}\mu(p)^{u+v+c}\\ \hline
(0,0,0)&(0,0)&1\\
(1,0,0)&(2,0)&-1\\
(0,1,0)&(0,2)&-1\\
(0,0,1)&(1,1)&-\chi _4(p)\\
(1,1,0)&(2,2)&1\\
(1,0,1)&(2,1)&1\\
(0,1,1)&(1,2)&\chi _4(p)\\
(1,1,1)&(2,2)&-1.
\end{array}
\tag{169.D20}
\]

The two \((2,2)\) entries cancel, and all remaining entries are exactly
(169.D9).  At \(2\), oddness forces
\(v_2(u)=v_2(c)=0\), while \(v_2(v)=0\) or \(1\).  These give
\((v_2(Q),v_2(R))=(0,0)\) with coefficient one and \((0,2)\) with
coefficient minus one, respectively.  Hence
\(g(Q,R)=\chi _4(Q)M(Q,R)\), proving
(169.D1) including \(p=2\).

Equivalently, if

\[
 P(d_1,d_2)=\mu^2(d_1)\mu^2(d_2){\bf1}_{(d_1,d_2)=1},
\]

then the exact finite identity

\[
 \chi _4(d_1)P(d_1,d_2)
 =\sum_{Q\mid d_1}\sum_{R\mid d_2}
   g(Q,R)\chi _4(d_1/Q)
\tag{169.D21}
\]

is the Dirichlet-convolution form of (169.D1).  It retains, rather than
averages away, all squarefree, coprime, odd-first-leg and even-second-leg
conditions.

### 3.4. Exact coupled dual kernel and the zero mode

Because \(\mathcal B\) vanishes outside the positive quadrant,
(169.D21) gives the finite identity

\[
 \mathcal S_{L,1}
 =\sum_{Q\leq M_x}\sum_{R\leq M_z}g(Q,R)
   \sum_{m,n\in\mathbb Z}\chi _4(m)\mathcal B(Qm,Rn).
\tag{169.D22}
\]

Use the exact character transform

\[
 \sum_{m\in\mathbb Z}\chi _4(m)f(m)
 =\frac i2\sum_{\substack{k\in\mathbb Z\\k\ \text{odd}}}
   \chi _4(k)\widehat f(k/4).
\tag{169.D23}
\]

For \(f(m)=\mathcal B(Qm,Rn)\), Fourier scaling contributes \(Q^{-1}\)
and changes the frequency to \(k/(4Q)\).  Ordinary Poisson in \(n\)
then contributes \(R^{-1}\) and frequency \(\ell/R\).  This proves
(169.D3), including its factor \(i/(2QR)\), with no approximate
functional equation, cutoff, or error.

For later separation, define the complete Fourier blocks

\[
 Z_{Q,R}=\frac{i g(Q,R)}{2QR}
 \sum_{k\ \text{odd}}\chi _4(k)
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},0\right),
\qquad
 N_{Q,R}=\frac{i g(Q,R)}{2QR}
 \sum_{k\ \text{odd}}\chi _4(k)
 \sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).
\tag{169.D24}
\]

Then

\[
 Z_{\rm fin}=\sum_{Q\leq M_x}\sum_{R\leq M_z}Z_{Q,R},
\qquad
 \mathcal D_{\rm fin}=\sum_{Q\leq M_x}\sum_{R\leq M_z}N_{Q,R},
\qquad
 \mathcal S_{L,1}=Z_{\rm fin}+\mathcal D_{\rm fin}.
\tag{169.D24a}
\]

The finite zero mode \(Z_{\rm fin}\) is not the Mellin residue.  For a
fixed odd \(Q\) in the support of \(g\), the local table gives

\[
\begin{aligned}
 \sum_{R\geq1}\frac{|g(Q,R)|}{R}
 ={}&\frac54
 \prod_{\substack{p>2\\v_p(Q)=0}}(1+p^{-2})
 \prod_{\substack{p>2\\v_p(Q)=1}}(p^{-1}+p^{-2})
 \prod_{\substack{p>2\\v_p(Q)=2}}(1+p^{-1})
 \ll_\varepsilon Q^\varepsilon.
\end{aligned}
\tag{169.D24b}
\]

It is zero if \(Q\) is outside the \(g\)-support.  Thus the full
ordinary-Poisson zero mode may be summed absolutely in \(R\).  Before
character Poisson it is

\[
 R_\zeta
 =\sum_{Q\leq M_x}\sum_{R\geq1}\frac{g(Q,R)}{R}
 \sum_m\chi _4(m)\int_{\mathbb R}\mathcal B(Qm,z)\,dz.
\tag{169.D24c}
\]

Its one-variable Dirichlet series is
\(L(s,\chi _4)G(s,1)\), exactly the residue series in (168.K20); the
local two-adic multiplier is \(1-2^{-2}=3/4\).  Applying character
Poisson to (169.D24c) proves the first formula in (169.D4).  No
\(Q>M_x\) term is missing: before character Poisson its physical
\(m\)-sum is zero, and equivalently every residue coefficient has
\(Q\mid n\) with \(n\) in the \(x\)-support, so \(Q\leq M_x\).

For \(R>M_z\), the physical block in (169.D22) is identically zero.
Exact double Poisson therefore says, for each fixed \((Q,R)\),

\[
 Z_{Q,R}+N_{Q,R}=0\qquad(R>M_z).
\tag{169.D24d}
\]

The absolute convergence in (169.D24b) makes the blockwise tail
\(\sum_{R>M_z}N_{Q,R}=-\sum_{R>M_z}Z_{Q,R}\) lawful.  Combining this
with (169.D24a) gives both equalities (169.D4)--(169.D4a).  This explains
why deleting \(\ell=0\) from only the finite physical family would be
wrong: the compensating nonzero modes of the physically empty
\(R>M_z\) blocks are required.

The correction is target-safe.  Indeed, before character Poisson the
finite and full zero-mode coefficients at a physical integer \(n\) are

\[
 c_{\leq M_z}(n)=
 \sum_{Q\mid n}\chi _4(n/Q)\sum_{R\leq M_z}\frac{g(Q,R)}R,
\qquad
 c_\infty(n)=
 \sum_{Q\mid n}\chi _4(n/Q)\sum_{R\geq1}\frac{g(Q,R)}R.
\tag{169.D24e}
\]

By (169.D24b) and the elementary divisor bound, both are
\(O_\varepsilon(X^\varepsilon)\).  At \(x=n\), the cardinal cells give

\[
 \int_{\mathbb R}\mathcal B(n,z)\,dz
 =\sum_m A_{L,X}(n,m)
   \int\psi(z-m)e(J\sqrt{nz})\,dz.
\tag{169.D24f}
\]

On every supported cell the phase derivative is \(\asymp J\), so one
integration by parts is \(O(J^{-1})\).  There are \(O(L^2)\) cells.
Consequently

\[
 |Z_{\rm fin}|+|R_\zeta|\ll_\varepsilon L^2J^{-1}X^\varepsilon,
\qquad
 |Z_{\rm fin}-R_\zeta|\ll_\varepsilon L^2J^{-1}X^\varepsilon,
\tag{169.D24g}
\]

which proves (169.D5a).  Pairing \(k\) with \(-k\) uses
\(\chi _4(-k)=-\chi _4(k)\), and pairing \(\ell\) with \(-\ell\) is
even; for the active finite family this gives exactly (169.D5).

All literal endpoint data remain inside \(\mathcal B\).  Since it is the
finite sum of disjoint smooth cardinal cells, both Poisson identities are
exact.  No seminorm estimate or smooth replacement is being smuggled
into (169.D3)--(169.D5).  The only infinite outer operation is the
explicit, fixed-\(Q\), block-grouped \(R\)-completion justified above.

### 3.5. Joint phase, lengths, restored powers, and self-return

Expanding the sine and cosine in (169.D5), only the branch with both
subtracted positive frequencies can have a positive interior saddle.  Its
phase is the one in (169.D6), and

\[
 \frac J2\sqrt{z/x}=\frac{k}{4Q},\qquad
 \frac J2\sqrt{x/z}=\frac{\ell}{R}.
\tag{169.D25}
\]

Therefore

\[
 k\asymp QJ,\qquad \ell\asymp RJ,
 \qquad k\ell=XQR,
\tag{169.D26}
\]

and the physical cone \(1\leq x/z\leq4\) is exactly
\(Q\ell\leq Rk\leq4Q\ell\).  The exact sums are infinite; (169.D26)
states their stationary lengths, not an unsupported truncation.  For the
literal cardinal array, nonstationary tails are controlled only with the
actual cell seminorms, and a unit cell has unit radial bandwidth.

On a favorable recombined smooth radial block of length \(L\), the
rank-one Hessian broadens the product relation to

\[
 |k\ell-XQR|\ll QRJ/L.
\tag{169.D27}
\]

The exact prefactor \(1/(QR)\), the angular stationary factor, and the
physical normalization give one dual coefficient scale

\[
 \frac{L^{3/2}}{QR\sqrt J}.
\tag{169.D28}
\]

There are at most

\[
 \left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon
\tag{169.D29}
\]

factor pairs in the smooth central collar.  Thus a positive norm, taken
only after the phase has been exposed, restores

\[
 \frac{L^{3/2}}{QR\sqrt J}\frac{QRJ}{L}X^\varepsilon
 =\sqrt{JL}\,X^\varepsilon
 =L^{3/2}\left(\frac HL+O(L^{-1})\right)X^\varepsilon.
\tag{169.D30}
\]

Relative to the optimistic Mellin absolute capacity
\(L^{2\eta}\sqrt J\,L^{3/2}X^\delta\), the exact double transform has
recovered the Poisson normalization and collar length, but not a uniform
target: the unpaid factor in (169.D30) is \(H/L\), and positive summation
over the active collapsed openings is not licensed.  Applying (169.D1)
to un-collapse them changes (169.D5) exactly into the active nonzero-mode
part of the Round-162 Mobius-weighted character-Poisson/ordinary-Poisson
family.  The zero-mode mismatch is not suppressed: it is exactly
\(Z_{\rm fin}-R_\zeta\), and (169.D24g) proves it target-safe.  With this
correction included, there are no missing gamma factors, two-adic pieces,
profiles, endpoint values, transform errors, or contour remainders in the
map.

For the complete cardinal array, (169.D27)--(169.D30) remain only the
accepted smooth-interior capacity calculation: summing stationary-phase
estimates cell by cell restores the unit-cell complexity rather than the
length-\(L\) radial gain.  Hence neither the exact identity nor its
positive smooth model proves \(\mathcal I_\eta\ll L^{3/2}X^\varepsilon\).

## 4. First doubtful or unproved step

There is no doubtful coefficient, two-adic, gamma, root-number, pole,
contour, residue-completion, or normalization step in
(169.D1)--(169.D5a).  The first
unproved step is the proposed signed estimate

\[
 \frac i2\sum_{Q\leq M_x}\sum_{R\leq M_z}\frac{g(Q,R)}{QR}
 \sum_{k\ \text{odd}}\chi _4(k)
 \sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right)
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\tag{169.D31}
\]

with the finite active outer summation and the full Fourier sums kept
together.  The correction from this kernel to \(\mathcal I_\eta\) is
already target-safe by (169.D24g).  By (169.D1), (169.D31) is the active
nonzero-mode Round-162 signed Mobius--Poisson family before its positive
collar bound.  Neither the functional equations nor multiplicativity
gives cancellation among different active \((Q,R)\), among neighboring
products \(k\ell\), or among the cardinal cells.  A spectral or
reciprocity theorem proving (169.D31) would be genuinely new input and
must act before all those positive norms.  The present derivation supplies
no such theorem and therefore no complete \(\sqrt J\) gain.

This is a scoped self-return obstruction, not a physical lower bound and
not a no-go for every signed spectral method.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `literal_signed_two_height_integral` | Passed.  (169.D4) gives exactly \(\mathcal I_\eta=\mathcal D_{\rm fin}+Z_{\rm fin}-R_\zeta\), and (169.D4a) gives its lawful block-completed form. |
| `G_local_coefficients_and_p2` | Passed by (169.D9), (169.D10), and the eight-state audit (169.D20). |
| `G_weighted_l1_eta_cost` | Passed: the exact cost is (169.D11), and on the shifted equal lines it is \(\asymp\eta^{-3}\). |
| `zeta_completed_function_and_pole` | Passed.  Conductor one, even gamma factor, root number one, poles at zero and one; the crossed pole at one is the full \(R\geq1\) completed \(\ell=0\) aggregate, not the finite physical zero mode. |
| `chi4_completed_function_parity_root_number` | Passed.  Conductor four, odd gamma factor, Gauss sum \(2i\), root number one, no pole. |
| `joint_contour_orientation_and_gamma_factors` | Passed in Section 3.2; the apparent singularity at zero is kept in the analytic paired product and there is no orientation sign. |
| `exact_cardinal_cell_or_endpoint_lawful_replacement` | Passed as an identity: the original disjoint cardinal function is transformed exactly.  No favorable smooth estimate is claimed for it. |
| `dual_coefficients_phase_lengths_and_normalization` | Passed: \(i g(Q,R)\chi _4(k)/(2QR)\), frequencies \(k/(4Q),\ell/R\), active stationary lengths \(QJ,RJ\), and phase (169.D6) are explicit; the physically empty \(R>M_z\) completion is separately identified. |
| `no_l1_over_G_or_dual_variables_before_joint_phase` | Passed.  (169.D12) justifies the initial expansion only; the active signed aggregate is retained through (169.D6).  The fixed-\(Q\) \(R^{-1}\) absolute sum is used only after isolating the target-safe zero-mode correction. |
| `no_common_height_substitution` | Passed.  The two independent Mellin variables become distinct sine and cosine frequencies. |
| `no_absolute_or_positive_moment_inflation` | Passed through the exact phase.  The positive calculation is used afterward only to diagnose the failure (169.D30), not to claim the target. |
| `functional_equation_AFE_Round162_self_return` | Passed as a no-go control with the necessary qualification: (169.D1) and (169.D5) give the active Round-162 nonzero-mode family, while (169.D24g) supplies the explicit target-safe finite-zero-mode versus Mellin-residue correction, including \(p=2\). |
| `arbitrary_real_centre_floors_stars_profiles_and_p2_branch` | Passed.  All are values of the unchanged cardinal function; \(v_2(R)=2\) is retained. |
| `target_sqrtJ_gain_and_epsilon_order` | Failed at the analytic gate, not hidden in epsilon: the smooth positive ledger is (169.D30), with structural factor \(H/L\); the exact cardinal aggregate has an additional recombination problem.  The fixed \(\eta^{-3}\) cost carries no power of \(X\). |
| `false_unsigned_aligned_and_G_equals_one_controls` | Passed as falsifiers.  The identity alone supplies no cancellation when \(\chi _4\) is erased, phases are aligned, or only \((Q,R)=(1,1)\) is kept.  No bound for those false analogues is inferred. |
| `downstream_scope_and_no_exponent_promotion` | Passed.  No full \(t=1\) scalar, residual, hard TOP, BAL, UNBAL, M9--M2, M1, endpoint, M9, bridge, quarter theorem, or exponent is closed. |
| `no_in_round_pivot` | Passed.  The report treats only the frozen joint-FE mechanism. |
| `Round170_strategy_literature_review_due` | Recorded.  No source theorem is imported here; the mandatory Round-170 review remains due after this round closes. |

No numerical experiment was performed; the round allocation is 100%
analytical/algebraic.

## 6. Exact dependencies and artifacts used

The derivation uses exactly the following artifacts:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `proofs/kernels/m9_m2_hard_top_t1_mellin_euler_polylog_signed_moment_reduction.md`;
5. `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
6. `proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md`;
7. `strategy/round169_m2_hard_top_t1_joint_functional_equation_spectral_strategy.md`;
8. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/barrier_packet.md`;
9. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/briefs/joint_functional_equation_dual_kernel_attack.md`.

The coefficient collapse, completed-function algebra, contour ledger,
and double-Poisson identity are internal derivations.  The smooth collar
power comparison uses only the accepted Round-162 and Round-168 kernels.
No external source, sibling report, computation, graph edit, validation
matrix, synthesis file, or proof draft was used.

## 7. Recommended state effect

**Promote after the required independent coefficient/gamma and endpoint
seam reviews only the following scoped internal result:** the exact
coefficient law (169.D1), weighted mass (169.D11)--(169.D12), finite
physical dual identity (169.D3), full residue completion
(169.D4)--(169.D4a), target-safe correction (169.D5a), and the conclusion
that bare joint GL(1) functional equations return to the active
Round-162 pre-stationary Mobius--Poisson family modulo that explicit
target-safe correction.  Close this mechanism under
`t1_joint_FE_spectral_self_return_no_go`.

Retain
`M9-M2-hard-top-t1-mellin-euler-polylog-and-signed-moment-reduction`,
`M9-M2-top-endpoint-signed-cone`, and every downstream parent as they
stand.  In particular, (169.D31) remains open, and there is no target or
exponent promotion.
