# Round 147 conductor candidate: exact (t=1) Voronoi reduction and squarefree-(H) resonance no-go

- Campaign: `m9-m1-lower-cone-t1-squarefree-voronoi-gate`
- Round: 147
- Role: conductor-selected proof kernel
- Starting graph SHA-256: `1dc79cf41e0dea8888341e944c5d0bf025d87f22cfaa282da34fcd10eecd04f5`
- Allocation: 100% analytic, algebraic, and source verification; 0% numerical

## 1. Result and exact scope

Let

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 \mathcal I_M=\mathbb N\cap[M,B_M),\qquad B_M\le 2M,
\]

and retain every inherited half-open prefix (M\le U\le B_M).  The
mandatory (t=1) face of the Round-146 scalar is

\[
 \mathfrak U^{(1)}_{N,M}(U)=
 \sum_{\substack{M\le s<U\\ \mu^2(s)=1}}
 s^{-3/4}V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns}),
\tag{147.C1}
\]

where

\[
 C(s)=\sum_{\substack{de=s\\e\ {\rm odd}\\e>4d}}\chi _4(e).
\tag{147.C2}
\]

Its desired bound is

\[
 \sup_{M\le U\le B_M}|\mathfrak U^{(1)}_{N,M}(U)|
 \ll_{\varepsilon,V}X^\varepsilon.
\tag{147.C3}
\]

By partial summation, (147.C3) follows from the unweighted prefix bound

\[
 \sup_{M\le U\le B_M}
 \left|\sum_{\substack{M\le s<U\\\mu^2(s)=1}}
 V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns})\right|
 \ll_{\varepsilon,V}M^{3/4}X^\varepsilon.
\tag{147.C4}
\]

The selected kernel proves the following exact reductions.

1.  The odd and even squarefree coefficients, all character sectors,
    the strict cone, the two-adic Euler factor, and the powerful Euler
    correction are explicit.
2.  For every fixed complex ratio order in a lawful strip, the complete
    \(\zeta L\) coefficient has an exact compact-smooth conductor-four
    Voronoi formula.  Convolution with the complete squarefree correction
    is exact, including its sole polar term and every (J,Y,K) branch.
3.  For fixed order, each physically active \(k\)-th powerful channel
    has the resonance geometry

    \[
      m=kN+O\!\left(k\sqrt{N/M}\right),
    \tag{147.C5}
    \]

    not at \(kN/4\), and its one-term physical amplitude is
    \(O(R^{-1}k^{-1}X^\varepsilon)\).  Uniform use across the cone
    orders is conditional on the growing-order estimate isolated below.
4.  On the unitary ratio line (147.C12c), even after granting the
    missing growing-order kernel estimates, the
    best estimate obtained by optimizing the primal and dual bounds
    separately for each powerful (k), and then taking absolute values
    in (k), is

    \[
    X^\varepsilon
    \begin{cases}
      M^{1/4},&M\le R^{4/3},\\
      R^{1/2}M^{-1/8},&R^{4/3}\le M\le R^2,
    \end{cases}
    \tag{147.C6}
    \]

    after the physical weight.  It loses (R^{1/3}) at
    (M=R^{4/3}) and (R^{1/4}) at (M=R^2).

Thus this round closes under the scoped label

\[
 \boxed{\mathsf{squarefree\_H\_resonance\_no\_go}.}
\tag{147.C7}
\]

The no-go applies to fixed-index Voronoi followed by modulus, absolute
aggregation over the powerful index, the bare reciprocal-phase divisor
count after a literal squarefree expansion, and a reciprocal-(L)
contour shift which does not own zero residues.  It is not a lower bound
for (147.C1), and it is not an impossibility theorem for a signed joint
correlation.  Moreover, (147.C3) is a sufficient separate estimate for
routes which decompose the (t)-layers, but it is not logically necessary
for a future route which proves cancellation jointly across different
(t)-layers.

No strict top range, no complete lower scalar, no M1 or M2 parent, and no
new global exponent is proved.

## 2. Exact (t=1) arithmetic and cone interface

Write a squarefree integer uniquely as

\[
 s=2^\nu n,\qquad \nu\in\{0,1\},\qquad n\text{ odd and squarefree}.
\]

Because (e) is odd, the prime (2), if present, is forced into (d).
Consequently

\[
 \boxed{
 C(2^\nu n)=
 \sum_{\substack{e\mid n\\e>2^{1+\nu/2}\sqrt n}}\chi _4(e).}
\tag{147.C8}
\]

Put (c_\nu=2^{1+\nu/2}) and

\[
 \mathfrak B_\nu(n)=
 \sum_{\substack{e\mid n\\c_\nu^{-1}\sqrt n<e<c_\nu\sqrt n}}
 \chi _4(e).
\]

Neither boundary equality can occur: it would equate an odd square to
(2^{\nu+2}n).  Pairing (e) with (n/e) therefore gives the exact
sector identity

\[
 \sum_{e\mid n}\chi _4(e)
  =(1+\chi _4(n))C(2^\nu n)+\mathfrak B_\nu(n).
\tag{147.C9}
\]

For (chi _4(n)=+1), the cone coefficient is one half of the complete
coefficient minus the central band.  For (chi _4(n)=-1), the complete
coefficient and the paired central band vanish, while the two exterior
tails are antisymmetric and the high tail in (147.C8) remains.  Hence a
complete nonnegative divisor coefficient cannot replace the literal cone
coefficient.  The prime and even-prime controls are

\[
 C(p)=\chi _4(p)\quad(p>4),\qquad
 C(2p)=\chi _4(p)\quad(p>8),
\tag{147.C10}
\]

for odd primes (p), while (C(1)=C(2)=0).

On a ratio box (d\asymp D) meeting (e=4d), the collar

\[
 |e-4d|\le \sqrt D
\tag{147.C11}
\]

contains (O(D^{3/2}X^\varepsilon)) admissible pairs.  Since
(de\asymp D^2\), its cost is (O(M^{3/4}X^\varepsilon)) in (147.C4)
and (O(X^\varepsilon)) in (147.C3), uniformly for a clipped prefix.
Outside this owned collar a smooth ratio cutoff has effective Mellin
bandwidth

\[
 |\Im z|\lesssim D^{1/2}X^\varepsilon.
\tag{147.C12}
\]

For comparison, the exact hard cone has the Perron representation

\[
 \mathbf 1_{\{e>4d\}}
 =\lim_{T\to\infty}\frac1{2\pi i}
 \int_{c-iT}^{c+iT}4^{-z}(e/d)^z\frac{dz}{z},
 \qquad c>0,
\tag{147.C12a}
\]

because equality \(e=4d\) is absent.  Any displacement of this hard
line toward \(\Re z=0\) must retain the residue at \(z=0\).  The
target-safe collar instead permits an ordinary Fourier transform on
the unitary line.  If \(\psi_D(d)\) is a smooth \(d\asymp D\)
partition with Mellin order \(t\), and \(\tau\) is the Fourier order
of the smoothed ratio cutoff, the exact normalization is

\[
 \psi_D(d)=\frac1{2\pi}\int_{\mathbb R}
 \widehat\psi_D(t)D^{it}d^{-it}\,dt,
 \qquad
 d^{-it}(e/d)^{i\tau}
 =(de)^{-it/2}(e/d)^{i(\tau+t/2)}.
\tag{147.C12b}
\]

Thus the coefficient order used below is

\[
 z=i(\tau+t/2),
\tag{147.C12c}
\]

the radial test acquires the unitary twist \(s^{-it/2}\), and the
external constants are \(D^{it}4^{-i\tau}\).  Equivalently, writing
the external ratio constant as \(4^{-z}\) requires the compensating
factor \(4^{it/2}\).  The \(t\)-weight is rapidly decreasing,
\(|\tau|\lesssim D^{1/2}X^\varepsilon\), and both orders and the
zero Fourier mode remain part of every uniform estimate.

An exact hard Perron cutoff cannot use this shorter height: the lattice
pair (e=4d+1) forces height comparable with (D).  The bounded (D=1)
face remains literal and has bounded ratio bandwidth.

## 3. Euler product, powerful support, and the quadratic refactorization

For (|\Re z|<1/4), define

\[
 A_z(n)=\sum_{de=n}\chi _4(e)(e/d)^z
       =n^{-z}\sigma_{2z,\chi _4}(n),\qquad
 B_z(n)=\mu^2(n)A_z(n).
\tag{147.C13}
\]

Then

\[
 \sum_{n\ge1}\frac{A_z(n)}{n^w}
  =F_z(w):=\zeta(w+z)L(w-z,\chi _4),
\tag{147.C14}
\]

The unfactored squarefree Euler product, whose local terms still
contain the linear monomials \(p^{-w-z}\) and
\(\chi _4(p)p^{-w+z}\), is absolutely convergent only for

\[
 \Re(w+z)>1,\qquad \Re(w-z)>1.
\tag{147.C14a}
\]

and

\[
 \sum_{n\ge1}\frac{B_z(n)}{n^w}=H(w,z)F_z(w),
 \qquad B_z=h_z*A_z.
\tag{147.C15}
\]

The factor (4^{-z}) associated with the cone ratio (e/(4d)) is
external to (147.C14)--(147.C15) and must be retained in the cone Mellin
integral.

At (2),

\[
 H_2(w,z)=1-2^{-2w-2z}.
\tag{147.C16}
\]

At an odd prime put (a=p^{-w-z}) and
(b=\chi _4(p)p^{-w+z}).  Direct local division gives

\[
 H_p(w,z)=(1+a+b)(1-a)(1-b)
 =1-a^2-b^2-ab+a^2b+ab^2.
\tag{147.C17}
\]

Thus (H) is coefficientwise absolutely convergent when

\[
 \Re(w+z)>\frac12,\qquad \Re(w-z)>\frac12.
\tag{147.C18}
\]

Writing (H(w,z)=\sum h_z(k)k^{-w}), its only nonzero local
prime-power coefficients are

\[
\begin{aligned}
 h_z(2^2)&=-2^{-2z},\\
 h_z(p^2)&=-(p^{-2z}+p^{2z}+\chi _4(p)),\\
 h_z(p^3)&=p^z+\chi _4(p)p^{-z}\qquad(p\text{ odd}).
\end{aligned}
\tag{147.C19}
\]

Every supported integer is powerful.  Uniformly on a fixed strip
(z=c+iv),

\[
 |h_z(k)|\ll_\varepsilon k^{|c|+\varepsilon},\qquad
 \#\{k\le K:h_z(k)\ne0\}\ll_\varepsilon K^{1/2+\varepsilon}.
\tag{147.C20}
\]

This is weighted Dirichlet convergence, not an unweighted physical
(\ell^1) estimate.

There is a further exact factorization.  At odd primes, cancellation
of the pure powers gives the exact identity

\[
 H_p=(1-a^2)(1-b^2)(1-ab)\mathscr K_p,
\qquad
 \mathscr K_p=\frac{1+a+b}{(1+a)(1+b)(1-ab)}
 =1+\frac{a^2b+ab^2+a^2b^2}{(1+a)(1+b)(1-ab)},
\tag{147.C21}
\]

and at (2),

\[
 \mathscr K_2(w,z)=(1-2^{-2w+2z})^{-1}.
\tag{147.C22}
\]

Consequently

\[
 \boxed{
 H(w,z)=
 \frac{\mathscr K(w,z)}
 {\zeta(2w+2z)\zeta(2w-2z)L(2w,\chi _4)}.}
\tag{147.C23}
\]

If \(z=c+iv\), \(|c|<1/2\), then \(\mathscr K\) is absolutely
convergent, uniformly in \(v\), for

\[
 \Re w>\frac{1+|c|}{3}.
\tag{147.C24}
\]

Indeed, on each closed sub-half-plane of (147.C24), the denominators
in (147.C21) are uniformly separated from zero for all sufficiently
large primes, and

\[
 |\mathscr K_p-1|
 \ll p^{-(3\Re w-c)}+p^{-(3\Re w+c)}+p^{-4\Re w}.
\tag{147.C24a}
\]

Thus \(3\Re w-|c|>1\) makes the prime sum converge; it also makes
(147.C22) regular because \((1+|c|)/3>|c|\) for \(|c|<1/2\).
Formula (147.C23) is initially proved in the common
absolute-convergence region and then gives meromorphic continuation.

It does not license a fixed shift of a (w)-contour below (1/2).
Such a shift must cross or avoid possible poles arising from zeros of

\[
 \zeta(2w+2z),\qquad \zeta(2w-2z),\qquad L(2w,\chi _4).
\tag{147.C25}
\]

No audited source gives a fixed zero-free strip at the growing heights,
proves cancellation of those poles by \(\mathscr K\), or supplies the
corresponding zero-residue aggregate.  The lawful coefficient-domain
interpretation of (147.C23) retains three signed square-supported
Möbius factors; it does not turn them into absolute convergence below
(Re w=1/2+|c|).

## 4. Fixed-order level-four transform and exact (H)-convolution

For fixed \(z\) with \(|\Re z|<1/4\) and
\(F\in C_c^\infty(0,\infty)\), define

\[
 \mathscr B_\nu(y)=
 \left(\frac2\pi K_\nu(y)-Y_\nu(y)\right)
 \sin\frac{\pi\nu}{2}
 +J_\nu(y)\cos\frac{\pi\nu}{2}.
\tag{147.C26}
\]

The Banerjee--Khurana conductor-(4) formula, with its normalization
checked from the completed functional equation, is

\[
\boxed{
\begin{aligned}
 \sum_{n\ge1}A_z(n)F(n)
 ={}&L(1-2z,\chi _4)\int_0^\infty F(x)x^{-z}\,dx\\
 &+\pi4^z\sum_{m\ge1}A_{-z}(m)
 \int_0^\infty F(x)\mathscr B_{2z}(2\pi\sqrt{mx})\,dx.
\end{aligned}}
\tag{147.C27}
\]

The cited theorem states an analytic finite-interval identity for fixed
\(z\) in the strict source strip \(0<\Re z<1/4\).  For every fixed
\(|\Re z|<1/4\), Mellin inversion of
\(\zeta(w+z)L(w-z,\chi _4)\), rapid vertical decay of
\(\widehat F\), and the completed functional equation give the
compact-smooth Mellin--Barnes identity directly.  On the source strip
its kernel is (147.C26); analytic continuation in the fixed parameter
gives the same package on the unitary line (147.C12c).  This is an
identity, not a uniform growing-order estimate.  There is only one
polar term, at \(w=1-z\), because
\(L(w-z,\chi _4)\) is entire.

As an independent normalization control, a direct \(z=0\)
Mellin-functional-equation derivation yields

\[
 \sum_{n\ge1}A_0(n)F(n)
 =\frac\pi4\int_0^\infty F(x)\,dx
 +\pi\sum_{m\ge1}A_0(m)
 \int_0^\infty F(x)J_0(2\pi\sqrt{mx})\,dx,
\tag{147.C28}
\]

where \(A_0(n)=r_2(n)/4\).  The statement-only rederivation obtains
the same formula directly, so no appeal to the strict source strip at
its excluded boundary is required.

For the physical compact test, put
\(K_F=\lfloor\sup\operatorname{supp}F\rfloor=O(M)\).  Applying
(147.C27) to \(F(k\cdot)\) in the finite physical convolution and
using (147.C15) gives

\[
\boxed{
\begin{aligned}
 \sum_{n\ge1}B_z(n)F(n)
 ={}&L(1-2z,\chi _4)
       \left(\sum_{k\le K_F}h_z(k)k^{z-1}\right)
       \int_0^\infty F(u)u^{-z}\,du\\
 &+\pi4^z\sum_{k\le K_F}\frac{h_z(k)}k
   \sum_{m\ge1}A_{-z}(m)
   \int_0^\infty F(u)
      \mathscr B_{2z}(2\pi\sqrt{mu/k})\,du.
\end{aligned}}
\tag{147.C29}
\]

The scaling factors are exact:

\[
 \int F(kx)x^{-z}\,dx=k^{z-1}\int F(u)u^{-z}\,du,
 \qquad
 \int F(kx)\mathscr B_{2z}(2\pi\sqrt{mx})\,dx
 =\frac1k\int F(u)\mathscr B_{2z}(2\pi\sqrt{mu/k})\,du.
\tag{147.C30}
\]

This finite form is the identity used in the power ledger.  If
\(k>K_F\), then \(F(kn)=0\) for every integer \(n\ge1\); applying
(147.C27) to \(F(k\cdot)\) shows that its polar and dual terms cancel
exactly for that \(k\).  One may extend (147.C29) to an all-\(k\)
iterated identity with polar factor \(H(1-z,z)\) only while keeping
every such zero pair inseparable.  The outer polar majorant is
summable for \(z=c+iv\), \(0<c<1/4\), by the powerful-support bound
\(O_\varepsilon(K_F^{-1/2+2c+\varepsilon})\).  No \(k>K_F\)
term is a physical resonant channel.

The source audit proves (147.C27)--(147.C29) only order by order.  The
first unresolved identity-to-estimate seam is a uniform expansion, with
all required derivatives and summable remainders, of (147.C26) for the
orders in (147.C12b)--(147.C12c), through the small-argument, transition, and
large-argument regimes and for every clipped prefix.  Near resonance the
formal parameter is favorable:

\[
 \frac{|z|^2}{\sqrt{NM}}
 \ll \frac{D}{\sqrt{NM}}X^\varepsilon
 \ll N^{-1/2}X^\varepsilon,
\tag{147.C31}
\]

on boundary boxes, but this inequality alone is not the required
uniform Bessel theorem.

## 5. Prefix, polar, and conductor-four resonance ledger

A prefix shorter than (\sqrt M) has raw divisor-bounded mass
(O(M^{1/2}X^\varepsilon)), already below (147.C4).  Otherwise one may
smooth each radial endpoint across (O(\sqrt M)) integers and peel the
changed terms at the same target-safe cost.  The resulting compact test
has moving-endpoint seminorms which must remain explicit in the missing
uniform estimate; no unit-scale terminal transition is assigned
scale-(M) derivative bounds.

For the oscillatory profile (F(u)=W_{M,U}(u)V_{\rm low}(R^2u/N)
e(+\sqrt{Nu})), the polar integral in (147.C29) is nonstationary.  The
radial phase scale is (\sqrt{NM}), whereas the smoothed cone order obeys
(|z|^2\ll D X^\varepsilon\le\sqrt M X^\varepsilon).  Repeated
integration by parts, together with the standard polynomial vertical
bounds and the rapid cone-Mellin weight, makes the polar contribution
target-safe.  The cone collar and the peeled radial endpoint collars
remain separate owned target-sized errors.

For fixed order and large positive argument, the (J/Y) part of
(147.C26) has phases

\[
 e(\pm\sqrt{mu/k}).
\tag{147.C32}
\]

The positive branch is nonstationary against (e(+\sqrt{Nu})), and the
(K)-branch decays at fixed order.  The negative branch has phase

\[
 \left(\sqrt N-\sqrt{m/k}\right)\sqrt u.
\tag{147.C33}
\]

Therefore its exact centre is (m=kN), and across (u\asymp M) its
resonant window is (147.C5).  If (m=kN+j), then

\[
 \sqrt N-\sqrt{m/k}
 =-\frac{j}{2k\sqrt N}
  +O\!\left(\frac{j^2}{k^2N^{3/2}}\right).
\tag{147.C34}
\]

At (m\asymp kN), one dual integral in the unweighted formula
(147.C29), including its (1/k), has size

\[
 \frac{M^{3/4}}{kN^{1/4}}X^\varepsilon
 =\frac{M^{3/4}}{kR}X^\varepsilon.
\tag{147.C35}
\]

There are (O(k\sqrt{N/M})) integers in the band.  Thus fixed-(k)
modulus costs

\[
 RM^{1/4}X^\varepsilon
\tag{147.C36}
\]

in the raw prefix, or (R/\sqrt M) after the physical weight.  The
primal divisor bound for the same channel is (M/k) raw, or
(M^{1/4}/k) after the physical weight.  Hence the strongest lawful
fixed-channel menu is

\[
 \min\!\left(\frac{M^{1/4}}k,\frac R{\sqrt M}\right)X^\varepsilon.
\tag{147.C37}
\]

Equations (147.C35)--(147.C37) are fixed-order capacity statements.
Their uniform insertion into the \(\tau,t\) integrals of
(147.C12b)--(147.C12c) is conditional on the unresolved Bessel
estimate following (147.C29).

At (m=kN) the archimedean phase cancels with the same leading Maslov
phase for every (k).  The (k)-bands are disjoint at the top scale,
but disjoint support in the already-summed dual variable does not imply
orthogonality between the resulting complex scalars.  In particular,
at (z=0)

\[
 (h_0*A_0)(n)=\mu^2(n)\frac{r_2(n)}4\ge0,
\tag{147.C38}
\]

so no independent random-sign heuristic is available for the complete
zero ratio mode.

## 6. All-scale no-go and the first squarefree reciprocal loss

For the power ledger, take the exact unitary order
\(z=i(\tau+t/2)\) from (147.C12c).  Equivalently, a Perron
abscissa \(|\Re z|\ll1/\log X\) only contributes an
\(X^\varepsilon\) factor.  A fixed nonzero \(c=\Re z\) would add
\(k_0^{|c|}\) to (147.C40), and no bound uniform in such a fixed
strip is asserted.

Let

\[
 k_0=\frac{M^{3/4}}R.
\tag{147.C39}
\]

If (k_0\ge1), (147.C20), dyadic partial summation, and the raw
fixed-channel menu give

\[
 \sum_{k\le K_F}|h_z(k)|\min\!\left(\frac Mk,RM^{1/4}\right)
 \ll_\varepsilon R^{1/2}M^{5/8}X^\varepsilon.
\tag{147.C40}
\]

After division by the raw target (M^{3/4}), this is
(R^{1/2}M^{-1/8}X^\varepsilon).  If (k_0<1), the convergent
powerful sum in the direct estimate gives raw size (MX^\varepsilon),
hence normalized loss (M^{1/4}X^\varepsilon).  This proves
(147.C6).  It is an upper-capacity calculation for an absolute-value
placement, not a lower bound for the signed scalar.

An independent one-sided transform exposes the same first arithmetic
loss.  Suppose (q\asymp Q), (d\asymp D), and (Q\le N/4).  Then

\[
 \boxed{
 \sum_{q\asymp Q}
 \left|\sum_{d\asymp D}e(Nd/q)\right|
 \ll_\varepsilon (Q+D)(NQ)^\varepsilon.}
\tag{147.C41}
\]

To prove it, for each (q) choose the nearest integer (a) to (N/q)
and put (j=N-aq).  The geometric sum is

\[
 \ll\min(D,q/|j|)
\]

when (j\ne0), while (j=0) costs (D).  For fixed nonzero
(|j|\ll Q), every admissible (q) divides (N-j\asymp N); the
divisor bound and a dyadic or harmonic sum over (j) give
(O(Q(NQ)^\varepsilon)).  When (j=0), the divisors (q\mid N)
give (O(DN^\varepsilon)).  The hypothesis (Q\ll N) is essential
and is satisfied in the project, where (Q\le R^2\ll N\).

On a box (DE\asymp M), the one-sided transform has

\[
 Q\asymp D\sqrt{N/M}.
\tag{147.C42}
\]

The required transformed scale is (RD X^\varepsilon).  At
(M=R^2), (147.C41) is exactly target-safe; at smaller (M), its
\(Q\)-term exceeds that scale by \(R/\sqrt M\).  The crossover
\(M=R^{4/3}\) appears only after taking the minimum of this dual
price with the primal price \(M^{1/4}\); the \(q\)-average alone
does not single out that scale.

The same proof does not survive squarefreeness.  Expanding

\[
 \mu^2(d)=\sum_{a^2\mid d}\mu(a)
\]

and applying (147.C41) after the triangle inequality gives only

\[
 \sum_{q\asymp Q}
 \left|\sum_{d\asymp D}\mu^2(d)e(Nd/q)\right|
 \ll_\varepsilon QD^{1/2}+D.
\tag{147.C43}
\]

Indeed, the (a)-th inner length is (D/a^2), and summing
(Q+D/a^2) for (a\le\sqrt{2D}) proves (147.C43).  A split at (A)
costs (AQ+D) for small squares and (QD/A) for the large-square
tail, again optimizing at (A=D^{1/2}).  This loss occurs before the
squarefreeness of the other divisor, coprimality, parity, character,
cone, or prefix is expanded.  The (H)-convolution is the exact Euler
packaging of these signed square/progression indices.

Therefore the first missing arithmetic statement for this
separate-\(t=1\) Voronoi route, after granting the uniform kernel
theorem, is a genuinely signed estimate of the form

\[
 \boxed{
 \sum_{\substack{k\le K_F\\k\ {\rm powerful}}}\frac{h_z(k)}k
 \sum_{|j|\lesssim k\sqrt{N/M}}
 A_{-z}(kN+j)\,\mathcal W_{k,z,U}(j)
 \ll_\varepsilon X^\varepsilon,}
\tag{147.C44}
\]

after the physical normalization and after integration over the actual
orders \(z=i(\tau+t/2)\), including the radial twist
\(s^{-it/2}\) and the external constants in (147.C12b).  Here
\(\mathcal W_{k,z,U}\) must retain the exact
conductor-four kernel, profile, prefix, transition terms, and the
individual positive physical direction.  Equivalently, one may seek a
squarefree/coprime strengthening of (147.C41) which avoids
(147.C43).  No accepted theorem or audited source proves either form.

## 7. First doubtful steps, controls, and recommended state effect

The first unproved analytic step is the growing-complex-order and
moving-prefix estimate following (147.C29), uniformly through every
Bessel regime in (147.C12).  Granting it, the first missing power is the
signed correlation (147.C44).  The favorable near-resonance parameter,
powerful support, disjoint moving bands, and the improved convergence of
\(\mathscr K\) do not prove that correlation.

The campaign controls have the following outcomes.

1. **Exact face and arithmetic support: green.**  Equations
   (147.C1)--(147.C10) retain the physical weight, squarefreeness,
   coprimality, parity, strict cone, both character sectors, fixed
   (N=\lfloor X\rfloor), individual positive direction, and every
   half-open prefix.
2. **Cone collar and bandwidth: green as a target-sized reduction.**
   Equations (147.C11)--(147.C12c) distinguish the hard and smooth
   heights, retain the hard zero-mode residue, and connect the local
   \(d\)-partition exactly to the unitary coefficient order.  The
   collar is owned, not declared negligible.
3. **Euler product and (p=2): green.**  Equations
   (147.C13)--(147.C24) give the exact local factors, coefficients,
   convergence regions, powerful support, and quadratic refactorization.
4. **Fixed-order source identity: green.**  Equations
   (147.C26)--(147.C30) retain the scalar \(\pi4^z\), sole pole,
   conductor, reflected coefficient, and every (J,Y,K) branch.
   Growing-order estimates remain open.
5. **Polar and prefix boundaries: green as reductions.**  The polar
   phase is nonstationary; radial and cone collars are explicitly
   target-sized.  Uniform transformed seminorms remain part of the open
   analytic step.
6. **Fixed-order resonance: green.**  Equations
   (147.C32)--(147.C37) give the exact centre, width, raw and physical
   amplitudes.  Uniform nonresonant and transition bounds remain in
   the missing growing-order theorem.
7. **Powerful aggregation and all scales: adverse.**  Equation
   (147.C6) loses (R^{1/3}) at the intermediate transition and
   (R^{1/4}) at the top.  No lower bound is inferred.
8. **Bare reciprocal phase: green; literal squarefree transfer:
   adverse.**  Equation (147.C41) meets the bare top target, whereas
   (147.C43) is the first exact triangle loss.
9. **Exceptional and self-return controls: retained.**  \(D=1\),
   primes, and even squarefree inputs remain.  If \(N=sL^2\), then
   \(e(\sqrt{Ns})=1\); if \(N=sL^2+1\), then
   \(\sqrt{Ns}=sL+\rho\), where
   \(\rho=(\sqrt{L^2+1/s}+L)^{-1}\), so the primal phase can rotate
   arbitrarily slowly.  These are controls, not lower bounds.  The
   dual equality \(m=kN\) is always an exact radical, and slowly
   rotating \(m=kN+j\) families remain.  A second termwise transform
   or the zero ratio mode supplies no signed saving.
10. **Owner scope: green.**  The Round-138 cross owner, every
    (t\ge2) layer, the complete lower scalar, lower GAR, both direct
    M1 parents, M9--M1, every M2 owner, M9--M2, endpoint uniformity,
    M9, the bridge, and the quarter target are unchanged.

Subject to seam review, the recommended graph effect is:

- create a proved reduction recording (147.C8)--(147.C30), the
  target-safe cone and radial collars, and the fixed-order
  conductor-four resonance ledger, without promoting the
  growing-order estimate, (147.C3), or (147.C4);
- create a scoped squarefree-(H) resonance obstruction recording the
  uniform-order seam, (147.C6), the reciprocal-zero seam, and
  (147.C41)--(147.C44);
- reject the claims that the fixed-order source theorem is already
  growing-order uniform, that absolute convergence of (H) or
  \(\mathscr K\) supplies the physical signed saving, that
  (147.C23) allows a residue-free contour shift, that bare top capacity
  proves the literal squarefree top, or that disjoint (k)-bands imply
  scalar orthogonality;
- make no downstream theorem, proof-draft conclusion, target, or
  exponent change.

The internally proved exponent remains (1/3).  The separately audited
external Li--Yang exponent remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\tag{147.C45}
\]
