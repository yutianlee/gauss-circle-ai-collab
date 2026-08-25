# Round 138 conductor adjudication: exact signed Farey residual

## 1. Result and decision

Close Round 138 under strict_signed_farey_reduction. The literal
integerized lower scalar admits an exact reduced-Farey representation, and
its square splits as

\[
 |\mathcal F_N|^2
 =\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon),
\qquad R=X^{1/4},\quad y=\lfloor\sqrt X\rfloor,\quad
N=\lfloor X\rfloor.
\tag{138.J1}
\]

Here \(\mathcal R_{y^{-2}}\) is a real, conjugation-closed sum over
different denominators whose ordinary carrier and character-adjusted
physical carrier are both separated from their partners by more than
\(y^{-2}\). The complete same-denominator block and the union of both
microscopic collision collars are target-square-safe with the actual
coefficients.

No report proves

\[
 |\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon.
\tag{138.J2}
\]

The decision is not a vote. The statement-only derivation independently
proved the lift, row, and exact-collision bounds; the discovery report
strengthened them to both \(y^{-2}\) collars and diagnosed the physical
stationary capacity; the hostile report supplied the complete hard-endpoint
Poisson owner ledger. Three post-unmask reviews recomputed the promoted
identity, fibre packing, determinant parity/aspect seam, Poisson constant,
radical scope, and downstream implications, and all three are green.

## 2. Exact scalar and strict residual statement

Let

\[
 L_\chi(T)=\sum_{g\le T}\frac{\chi_4(g)}g,\qquad
 \lambda_b=\frac{\chi_4(b)}bL_\chi(y/b).
\]

On the certified small positive arc \(1\le h<d\le y\), reducing
\(h/d=a/b\) and summing every odd lift before taking a norm gives

\[
 \mathcal F_N=
 \sum_{\substack{2\le b\le y\\b\ {\rm odd}}}\lambda_b
 \sum_{\substack{1\le a<b\\(a,b)=1}}
 e(aN/b)J_{R,y}(a/b)
 =
 \sum_{\substack{d\le y}}\chi_4(d)
 \sum_{h\ge1}\frac1h
 V_{\rm low}(4R^2h^2/d^2)e(hN/d).
\tag{138.J3}
\]

This is termwise the integerized cone
\(\mathcal B_{\rm flat}^{(N)}(X)\). Round 121 separately owns

\[
 \mathcal B_{\rm flat}^{+}(X)
 =\mathcal B_{\rm flat}^{(N)}(X)+O(R).
\tag{138.J4}
\]

At every rational sample \(\eta(ya/b)=1\). Since
\(\chi_4(b)=e((b-1)/4)\) for odd \(b\), put

\[
 c_{a,b}=\frac{L_\chi(y/b)}a
 V_{\rm low}(4R^2a^2/b^2),\qquad
 \theta_{a,b}=\frac{Na}{b},\qquad
 \phi_{a,b}=\frac{Na}{b}+\frac{b-1}{4}\pmod1.
\tag{138.J5}
\]

Then \(\mathcal F_N=\sum c_{a,b}e(\phi_{a,b})\),
\(|c_{a,b}|\ll a^{-1}\), and \(a\ll b/R\). Define

\[
 \mathcal R_\delta=
 \sum_{\substack{(a,b),(a',b')\\b\ne b'\\
 \|\theta_{a,b}-\theta_{a',b'}\|>\delta\\
 \|\phi_{a,b}-\phi_{a',b'}\|>\delta}}
 c_{a,b}\overline{c_{a',b'}}
 e(\phi_{a,b}-\phi_{a',b'}).
\tag{138.J6}
\]

Equation (138.J1) holds with \(\delta=y^{-2}\), uniformly for every real
\(X\ge2\). After renaming \(\varepsilon\), the scalar target
\(|\mathcal F_N|\ll_\varepsilon RX^\varepsilon\) is equivalent to
(138.J2).

## 3. Proof of the row and carrier deletions

The lift identity follows from \(h=ag,d=bg,(a,b)=1\):

\[
 \sum_{g\le y/b}\frac{\chi_4(bg)}{ag}
 V_{\rm low}(4R^2a^2/b^2)e(aN/b)
 =
 \frac{\chi_4(b)L_\chi(y/b)}a
 V_{\rm low}(4R^2a^2/b^2)e(aN/b).
\tag{138.J7}
\]

Even lifts vanish, the primitive numerator is retained, and no
multiplicity remains. The only \(b=1\) completion class is the zero
residue, killed exactly by \(J_{R,y}(0)=0\). The opposite frequency
sign is the complex conjugate.

The literal coefficient bounds give

\[
 \sum_{a,b}|c_{a,b}|\ll y\log(2X),\qquad
 \sum_{a,b}|c_{a,b}|^2\ll y.
\tag{138.J8}
\]

Writing \(F_b=\sum_a c_{a,b}e(\phi_{a,b})\), the complete
same-denominator owner is the nonnegative row square

\[
 \sum_b|F_b|^2
 \le\sum_{b\le y}\left(\sum_{a\ll b/R}\frac1a\right)^2
 \ll y\log^2(2X).
\tag{138.J9}
\]

This contains both the equality diagonal and every unequal-numerator pair
on one denominator. No rowwise modulus is taken on the survivor.

For an ordinary phase fibre, let \(g=(N,b)\) and \(q=b/g\). A fixed
reduced phase \(u/q\) has

\[
 b=qg,\qquad g\mid N,\qquad q,g\ {\rm odd},\qquad
 (N/g,q)=1,\qquad
 (N/g)a\equiv u\pmod q,
\tag{138.J10}
\]

subject to the literal support and primitive condition. Hence its
\(\ell^1\)-mass is at most

\[
 M_\theta^{\max}\ll\tau(N)\log(2X),\qquad
 \sum_zM_\theta(z)\ll y\log(2X).
\tag{138.J11}
\]

The case \(q=1\) includes all odd divisor denominators \(b\mid N\).
A \(\phi\)-fibre is the union of at most two restricted \(\theta\)-fibres,
according as \(b\equiv1\) or \(3\pmod4\), so (138.J11) also holds for
\(\phi\), up to an absolute factor.

Distinct \(\theta\)-values have spacing at least \(y^{-2}\); distinct
\(\phi\)-values have spacing at least \((4y^2)^{-1}\). Therefore, for
either carrier,

\[
 \sum_{\|z-z'\|\le\delta}M(z)M(z')
 \ll y\tau(N)\log^2(2X)(1+\delta y^2).
\tag{138.J12}
\]

At \(\delta=y^{-2}\), (138.J9) and the union bound applied to
(138.J12) prove (138.J1).

## 4. Determinant geometry and fourth-power controls

For \(b=Gr,b'=Gs,(r,s)=1\), every quantity \(G,r,s\) is odd and

\[
 \Delta=ab'-a'b=G\delta_0,\qquad
 \delta_0=as-a'r,\qquad
 \frac{N\Delta}{bb'}=\frac{N\delta_0}{Grs}.
\tag{138.J13}
\]

All solutions on one fibre are
\(a=a_0+r\ell,\ a'=a'_0+s\ell\). Both the determinant phase and
\(\chi_4(Gr)\chi_4(Gs)=\chi_4(rs)\) are constant in \(\ell\). Although

\[
 \frac1{aa'}=\frac1{\delta_0}
 \left(\frac{s}{a'}-\frac r a\right),
\tag{138.J14}
\]

summation retains first-point/aspect terms
\(r/a_{\min}+s/a'_{\min}\). This loss is necessary. For odd
\(S\to\infty\), take \(r=1,s=S,a=a'=1,\delta_0=S-1\), with odd
\(G\asymp R^{3/2}\), \(S\asymp R^{1/2}\), and \(GS\le y\). The
reciprocal kernel contains the contribution \(1\), whereas
\(\log(2X)/|\delta_0|\to0\). Thus (138.J14) alone gives no
aspect-free determinant contraction. This is an algebraic kernel
control, not a physical lower bound.

At fourth-power centres \(X=N=M^4\), \(R=M\), \(y=M^2\), with \(M\)
odd, the packet

\[
 a=1,\qquad b_u=y-4u,\qquad1\le u\le cR
\tag{138.J15}
\]

has \(b_u\equiv1\pmod4\), \(L_\chi(y/b_u)=1\), and, on the accepted
plateau \(V_{\rm low}=1\),

\[
 c_{1,b_u}=1,\qquad
 \frac N{b_u}=y+4u+\frac{16u^2}{y-4u}.
\tag{138.J16}
\]

For small fixed \(c\), these distinct phases lie in one short sector and
their gaps are much larger than \(y^{-2}\). Their unequal internal pairs
remain in the residual with target-square capacity \(\asymp R^2\).
Exterior terms may cancel them, so this is not a lower bound for
\(\mathcal F_N\). The accepted paired half-integer tubes give the
different post-pairing modulus capacity \(R^{3/2}\), also not a signed
lower bound.

## 5. Complete Poisson owner and radical scope

For fixed \(h\), set

\[
 a_h(x)=\frac1hV_{\rm low}(4R^2h^2/x^2).
\]

Symmetric Poisson summation of the inclusive hard interval gives the
complete identity

\[
 \begin{aligned}
 \sum_{d\le y}\chi_4(d)a_h(d)e(Nh/d)
 ={}&\frac12\chi_4(y)a_h(y)e(Nh/y)\\
 &+\frac1{2i}\sum_{\sigma=\pm1}\sigma
 \lim_{K\to\infty}\sum_{|k|\le K}
 \int_0^y a_h(x)
 e\!\left(\frac{Nh}{x}+(\sigma/4-k)x\right)\,dx.
 \end{aligned}
\tag{138.J17}
\]

The half-endpoint term is mandatory. For an interior stationary mode
\(r=\sigma-4k>0\), the saddle is

\[
 x_*=2\sqrt{Nh/r},\qquad
 \Phi(x_*)=\sqrt{Nhr},\qquad
 \Phi''(x_*)=\frac{r^{3/2}}{4(Nh)^{1/2}}.
\]

The correctly normalized principal factor is

\[
 e(-1/8)N^{1/4}\chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),
\qquad e(-1/8)=-i\,e(1/8).
\tag{138.J18}
\]

This is only an interior stationary principal family. Its complete
absolute ledger is

\[
 N^{1/4}\sum_{h\ll R}h^{-3/4}
 \sum_{h\ll r\ll y/h}r^{-3/4}
 \ll R^{3/2}\log(2X),
\tag{138.J19}
\]

above target \(R\). The hard endpoint and incomplete-Fresnel crossing,
nonstationary modes, profile and stationary entry/exit crossings,
remainders, small heights, both branches, floors, zero class, lift
reassembly, and conjugate sign retain separate owners.

Write \(N=Ds^2\), with \(D\) squarefree. Inside a bounded
principal/transition family,

\[
 e(\sqrt{Nhr})=1\quad\Longleftrightarrow\quad hr=Dt^2,
\]

and the unique exact radical channel has absolute mass

\[
 N^{1/4}D^{-3/4}
 \sum_{t\ll R/\sqrt D}t^{-3/2}\tau(Dt^2)
 \ll_\varepsilon RD^{-3/4}X^\varepsilon.
\tag{138.J20}
\]

This is a target-safe upper control only. Near radicals, nonsquare
principal modes, and all nonprincipal owners remain open. A second
Legendre step returns the reciprocal phase; exact Fourier completion
returns the earlier flat discrepancy. Neither invertible transform is a
contraction.

## 6. First open step, controls, dependencies, and scope

The first unproved step is exactly (138.J2). The residual has different
denominators, nonzero determinant, and ordinary and physical carrier
distances exceeding \(y^{-2}\), but its absolute capacity remains
\(y^{2+o(1)}\). A proof must save a full factor \(y\) in the square
while keeping the literal coefficient, primitive restrictions, both
carriers, determinant arithmetic, and prescribed centre joint.

The following controls are green: integerized lift and \(O(R)\) phase
seam; certified \(h<d\); \(b=1\) centre; complete rows; odd \(q,g\)
fibre converse; both microscopic collars; real-\(X\) floors; variable
odd-\(S\) aspect test; complete Poisson endpoint; constant \(e(-1/8)\);
unique radical upper control; conjugate sign; and directionality.

The following routes are red as gains: diagonal alone, exact collisions
alone, a wider unproved collar, aspect-free determinant summation,
oscillation in the coherent \(\ell\)-direction, rowwise or
determinantwise modulus on the survivor, uniform adjacent-character
pairing, replacement of (138.J17) by (138.J18), inference from
\(R^{3/2}\) capacity or the fourth-power packet to a signed lower bound,
extension of (138.J20) to near radicals, and a second-transform gain.

The exact evidence is the three primary reports, the conductor candidate,
the three post-unmask reviews, the Round-121 flat-cone synthesis, the
Round-122 near-square synthesis, and the Round-127 directionality
adjudication. No numerical experiment, symbolic experiment, centre
average, arbitrary coefficient array, or external theorem is used.

The strict reduction changes no complete lower-GAR, direct blockwise M1,
M9-M1, M2, endpoint, M9, quarter, or exponent status.

## 7. Recommended State Patch

Create one proved reduction recording (138.J1) and one proved obstruction
recording the determinant, Poisson, radical, packet, and self-return
controls. Add both to the open lower-radial signed owner and attach the
round evidence to the near-square and earlier Farey self-return nodes.

Reject every inference listed as red in Section 6, including the stale
even-\(s\) determinant example. Retain as open the exact residual
(138.J2), the lower-radial signed estimate, lower GAR, both direct M1
parents, M9-M1, every M2 parent, endpoint uniformity, M9, the conditional
quarter bridge, and the target.

The strongest internally proved global exponent remains \(1/3\). The
separately audited external Li--Yang exponent remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
\]
