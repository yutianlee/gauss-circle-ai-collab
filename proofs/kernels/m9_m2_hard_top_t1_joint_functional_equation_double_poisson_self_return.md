# Kernel: hard-TOP \(t=1\) joint-FE double-Poisson self-return

## Statement

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 H=\lfloor yX^{-1/4}\rfloor=\sqrt J+O(1),
 \qquad 1\ll L\ll H,
\tag{169.K1}
\]

and retain the complete literal selector-free hard-TOP \(t=1\) scalar
\(\mathcal S_{L,1}\) and the exact Round-168 disjoint-cardinal
interpolant \(\mathcal B\).  Thus every shell, real-centre floor, star,
profile value, cone edge, endpoint transition, parity branch, and zero
extension is retained at the lattice points.  Put

\[
 \widetilde{\mathcal B}(\xi,\nu)
 =\iint_{\mathbb R^2}\mathcal B(x,z)e(-\xi x-\nu z)\,dx\,dz.
\tag{169.K2}
\]

Write

\[
 G(s_1,s_2)=\sum_{Q,R\ge1}\frac{g(Q,R)}{Q^{s_1}R^{s_2}}.
\tag{169.K3}
\]

For odd primes, the nonzero local coefficients are

\[
\begin{array}{c|rrrrrr}
(v_p(Q),v_p(R))&(0,0)&(2,0)&(0,2)&(1,1)&(2,1)&(1,2)\\ \hline
g_p&1&-1&-1&-\chi_4(p)&1&\chi_4(p),
\end{array}
\tag{169.K4}
\]

and at \(2\) they are \((0,0)\mapsto1\) and
\((0,2)\mapsto-1\).  Equivalently,

\[
 \boxed{
 g(Q,R)=\chi_4(Q)
 \sum_{\substack{u,v,c\ge1;\ u,c\ \mathrm{odd}\\
                  [u^2,c]=Q,\ [v^2,c]=R}}
 \mu(u)\mu(v)\mu(c).}
\tag{169.K5}
\]

For \(\sigma_1,\sigma_2>1/2\),

\[
\begin{aligned}
 \sum_{Q,R}\frac{|g(Q,R)|}{Q^{\sigma_1}R^{\sigma_2}}
 ={}&(1+2^{-2\sigma_2})\prod_{p>2}
 \bigl(1+p^{-2\sigma_1}+p^{-2\sigma_2}
 +p^{-\sigma_1-\sigma_2}\\
 &\hspace{30mm}+p^{-2\sigma_1-\sigma_2}
 +p^{-\sigma_1-2\sigma_2}\bigr).
\end{aligned}
\tag{169.K6}
\]

In particular, uniformly for \(0<\eta\le1/4\),

\[
 \sum_{Q,R}\frac{|g(Q,R)|}{(QR)^{1/2+\eta}}
 \asymp\zeta(1+2\eta)^3\asymp\eta^{-3},
 \qquad
 \sum_{Q,R}\frac{|g(Q,R)|}{QR}<\infty.
\tag{169.K7}
\]

Let \(\sum^{\mathrm{phys}}_{Q,R}\) be the canonical finite physical
block sum obtained before Poisson.  Equivalently, take the rectangle
bounded by the positive support suprema of \(\mathcal B\); any extra
block in that rectangle is identically zero before Poisson.  Then

\[
 \boxed{
 \mathcal S_{L,1}
 =\frac i2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{\substack{k\in\mathbb Z\\k\ \mathrm{odd}}}\chi_4(k)
 \sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).}
\tag{169.K8}
\]

Let \(Z_{\mathrm{phys}}\) be the \(\ell=0\) term in (169.K8), and
let \(R_\zeta\) be the full cardinal Mellin residue from Round 168.
They are not equal in general.  With

\[
 E_0=Z_{\mathrm{phys}}-R_\zeta,
\tag{169.K9}
\]

one has

\[
 Z_{\mathrm{phys}}\ll L^2/J,\qquad
 R_\zeta\ll L^2/J,\qquad E_0\ll L^2/J.
\tag{169.K10}
\]

Consequently the exact Round-168 signed two-height remainder satisfies

\[
 \boxed{
 \mathcal I_\eta
 =E_0+\frac i2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{\substack{k\in\mathbb Z\\k\ \mathrm{odd}}}\chi_4(k)
 \sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).}
\tag{169.K11}
\]

Pairing signs gives

\[
 \mathcal I_\eta=E_0+
 2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{\substack{k\ge1\\k\ \mathrm{odd}}}\chi_4(k)
 \sum_{\ell\ge1}\iint\mathcal B(x,z)
 \sin\!\frac{\pi kx}{2Q}\cos\!\frac{2\pi\ell z}{R}\,dx\,dz.
\tag{169.K12}
\]

The two completed functional equations underlying the sine and cosine
kernels are

\[
 \pi^{-s/2}\Gamma(s/2)\zeta(s)
 =\pi^{-(1-s)/2}\Gamma((1-s)/2)\zeta(1-s),
\tag{169.K13}
\]

and

\[
 \left(\frac4\pi\right)^{(s+1)/2}
 \Gamma\!\left(\frac{s+1}{2}\right)L(s,\chi_4)
 =\left(\frac4\pi\right)^{(2-s)/2}
 \Gamma\!\left(\frac{2-s}{2}\right)L(1-s,\chi_4).
\tag{169.K14}
\]

Zeta is even of conductor and root number one and has completed poles at
zero and one.  The primitive \(\chi_4\) is odd of conductor four, has
Gauss sum \(2i\), root number one, and entire completion.  The
uncompleted gamma quotients are

\[
 X_\zeta(s)=2^s\pi^{s-1}\Gamma(1-s)\sin(\pi s/2),
 \qquad
 X_4(s)=\left(\frac\pi2\right)^{s-1}
 \Gamma(1-s)\cos(\pi s/2),
\tag{169.K15}
\]

the Mellin kernels of \(2\cos(2\pi u)\) and
\(\sin(\pi u/2)\), respectively.

The only positive interior stationary branch in (169.K12) has phase

\[
 J\sqrt{xz}-\frac{kx}{4Q}-\frac{\ell z}{R},
\tag{169.K16}
\]

and obeys

\[
 \boxed{k\ell=XQR},\qquad
 \boxed{Q\ell\le Rk\le4Q\ell}.
\tag{169.K17}
\]

On a favorable recombined smooth interior block of radial length \(L\),
the product relation broadens to

\[
 |k\ell-XQR|\ll QRJ/L.
\tag{169.K18}
\]

The accepted coefficient scale and factor-pair count are

\[
 \frac{L^{3/2}}{QR\sqrt J},\qquad
 \left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon,
\tag{169.K19}
\]

so termwise-positive control has the inherited capacity

\[
 \sqrt{JL}\,X^\varepsilon
 =L^{3/2}\left(\frac HL+O(L^{-1})\right)X^\varepsilon.
\tag{169.K20}
\]

Substitution of (169.K5) into (169.K8) is coefficientwise exactly the
accepted Round-162 Mobius opening followed by character Poisson and
ordinary Poisson, including the even second leg and the two-adic branch.
Thus bare joint GL(1) functional-equation dualization is an exact
collapsed self-return of the full scalar, and a self-return up to the
target-safe correction \(E_0\) for \(\mathcal I_\eta\).  It does not
prove the signed aggregate in (169.K11).

## Proof

### 1. Euler and Mobius coefficients

For odd \(p\), put \(x=\chi_4(p)p^{-s_1}\) and \(y=p^{-s_2}\).  Then

\[
 (1+x+y)(1-x)(1-y)
 =1-x^2-y^2-xy+x^2y+xy^2,
\tag{169.K21}
\]

which gives (169.K4).  The factor \(G_2=1-2^{-2s_2}\) gives the
two-adic table.  Absolute local expansion gives (169.K6), and comparison
of local logarithms with \(\zeta(1+2\eta)^3\) gives (169.K7).

The exact projector identity is

\[
 \mu^2(d_1)\mu^2(d_2){\bf1}_{(d_1,d_2)=1}
 =\sum_{u^2\mid d_1}\mu(u)
  \sum_{v^2\mid d_2}\mu(v)
  \sum_{c\mid(d_1,d_2)}\mu(c).
\tag{169.K22}
\]

Set \(Q=[u^2,c]\), \(R=[v^2,c]\).  The character forces \(u,c,Q\)
odd and extracts \(\chi_4(Q)\).  At an odd prime, the eight states of
\((v_p(u),v_p(v),v_p(c))\) give

\[
\begin{array}{c|rrrrrrrr}
(u,v,c)&000&100&010&001&110&101&011&111\\ \hline
(v_p(Q),v_p(R))&(0,0)&(2,0)&(0,2)&(1,1)&(2,2)&(2,1)&(1,2)&(2,2)\\
\mathrm{weight}&1&-1&-1&-\chi_4(p)&1&1&\chi_4(p)&-1.
\end{array}
\tag{169.K23}
\]

The two \((2,2)\) terms cancel.  At \(2\),
\(v_2(u)=v_2(c)=0\) and \(v_2(v)=0,1\), giving the two-adic table.
This proves (169.K5) and the coefficient convolution

\[
 \chi_4(d_1)\mu^2(d_1)\mu^2(d_2){\bf1}_{(d_1,d_2)=1}
 =\sum_{Q\mid d_1}\sum_{R\mid d_2}
 g(Q,R)\chi_4(d_1/Q).
\tag{169.K24}
\]

### 2. Exact double Poisson and the residue correction

Applying (169.K24) on the finite lattice support gives

\[
 \mathcal S_{L,1}
 =\sum_{Q,R}^{\mathrm{phys}}g(Q,R)
  \sum_{m,n\in\mathbb Z}\chi_4(m)\mathcal B(Qm,Rn).
\tag{169.K25}
\]

The exact summation formulae are

\[
 \sum_m\chi_4(m)f(m)
 =\frac i2\sum_{\substack{k\in\mathbb Z\\k\ \mathrm{odd}}}
 \chi_4(k)\widehat f(k/4),
 \qquad
 \sum_n h(n)=\sum_{\ell\in\mathbb Z}\widehat h(\ell).
\tag{169.K26}
\]

Fourier scaling proves (169.K8).  Before character Poisson, its finite
zero mode is

\[
 Z_{\mathrm{phys}}
 =\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}R
 \sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz,
\tag{169.K27}
\]

whereas the Mellin residue is

\[
 R_\zeta
 =\sum_{Q\le M_x}\sum_{R\ge1}\frac{g(Q,R)}R
 \sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz.
\tag{169.K28}
\]

The \(Q\)-sum is finite because \(Qm\) must meet the positive
\(x\)-support; the residue retains the full \(R\)-sum from \(G(s,1)\).
For \(R\) beyond the positive \(z\)-support, the complete physical block
is zero, but its zero and nonzero Poisson modes cancel only after being
combined.  Hence (169.K27) cannot be identified with (169.K28).

At \(x=Qm\), cell disjointness leaves one \(x\)-cell.  Each supported
\(z\)-cell has phase derivative \(\asymp J\), so one integration by
parts is \(O(J^{-1})\).  There are \(O(L/Q)\) values of \(m\) and
\(O(L)\) second cells.  Therefore

\[
 |Z_{\mathrm{phys}}|
 \ll\frac{L^2}{J}\sum_{Q,R}\frac{|g(Q,R)|}{QR}
 \ll L^2/J.
\tag{169.K29}
\]

The same absolutely convergent calculation applies to (169.K28),
proving (169.K10).  Finally,
\(\mathcal I_\eta=\mathcal S_{L,1}-R_\zeta\); splitting (169.K8) into
zero and nonzero modes gives (169.K11), and pairing signs gives
(169.K12).

### 3. Completed kernels, phase, and self-return

Equations (169.K13)--(169.K15) follow from the standard completed
functional equations, gamma duplication, and reflection.  The character
Gauss sum \(2i\) gives the factor \(i/2\) in (169.K26).  On the intact
\(L\zeta G\) contour, moving the zeta line from \(\Re s_2>1\) to
\(1/2+\eta\) crosses only \(s_2=1\), producing (169.K28).  For one fixed
physical \((Q,R)\) block, the remaining contours may be moved left to a
line where the dual series converge.  The apparent zeta singularity at
zero cancels in \(X_\zeta(s)\zeta(1-s)=\zeta(s)\), and reversing
\(1-s\) restores upward orientation without a residual sign.

It is not lawful to resum the infinite \(G\)-series absolutely after
this left shift, because \(Q^{-s_1}R^{-s_2}\) then grows.  The finite
physical convolution (169.K25), followed by exact Poisson, is the lawful
summation order.  The difference between its finite zero mode and the
intact Mellin residue is exactly (169.K9).

Differentiating (169.K16) gives

\[
 \frac J2\sqrt{z/x}=\frac{k}{4Q},\qquad
 \frac J2\sqrt{x/z}=\frac{\ell}{R},
\tag{169.K30}
\]

which proves (169.K17).  With \(x=rw\), \(z=r/w\), angular stationarity
leaves radial phase

\[
 r\left(J-\sqrt{\frac{k\ell}{QR}}\right).
\tag{169.K31}
\]

It vanishes at exact resonance.  A favorable length-\(L\) smooth radial
block gives (169.K18), and the inherited Round-162 ledger gives
(169.K19)--(169.K20).  This is a smooth-interior route capacity only.
The exact cardinal array has \(O(L^2)\) unit cells and does not inherit
the global radial scale without a separately proved endpoint-lawful
recombination theorem.

Substituting (169.K5) in (169.K8) restores every Round-162 opening sign,
the character, \(p=2\), both Fourier variables, and their normalizations.
This proves the stated coefficientwise self-return and no more.

## First open interface and scope

Since \(E_0\) is target-safe, the first open estimate is

\[
 \frac i2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)\sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right)
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{169.K32}
\]

No audited shifted-convolution, Kuznetsov, spectral-large-sieve,
reciprocity, or weighted-moment placement accepts this moving product
collar with the literal cardinal weight and signed outer \(g(Q,R)\)
aggregate at target-safe restored power.  This conclusion is confined to
the dated audited placements.  It is not a physical lower bound and not
a universal no-go for a future bespoke signed theorem.

No polynomial-range full \(t=1\) scalar or residual, other hard-TOP
channel, hard TOP, BAL, UNBAL, M9--M2, direct M1 parent, GAR estimate,
endpoint uniformity, M9, bridge, quarter theorem, or exponent is proved.

## Provenance

The intact Mellin/cardinal representation and target-safe residue are
inherited from
`M9-M2-hard-top-t1-mellin-euler-polylog-and-signed-moment-reduction`.
The literal scalar, Mobius opening, character-Poisson normalization,
rank-one product collar, and positive capacity are inherited from
`M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`.
The local \(g\)-law, collapsed opening identity, exact finite double
Poisson formula, finite-zero/full-residue correction, completed-kernel
ledger, and coefficientwise comparison are internal deductions.
