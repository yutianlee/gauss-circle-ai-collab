# Round 135 post-unmask source and capacity audit

## 1. Result

The Round-135 source-level no-go survives, but several seams require
material repair before it is promotion-ready.

The strongest corrected conclusion is as follows.  On the frozen flat
smooth packet, write

\[
X=x_0+\xi,\qquad x_0=\lfloor X\rfloor\in\mathbb Z_{>0},\qquad
0\leq\xi<1.
\]

The factor \(e(\xi k/r)\) is part of a uniformly smooth normalized
amplitude because \(k/r\asymp K/R=\Delta^{-1}\).  It has an exact
independent-coefficient Fourier--Mellin separation with \(O(1)\) integrated
projective norm.  Consequently the integral frequency \(x_0\), rather than
the real number \(X\), may drive every source phase below.  This makes the
direct \(m=1\) specialization source-legal for both Bettin--Chandee and
Wright for every real \(X\), and it also makes the \(a=m^2\) connector and
both completion formulas classical for every real \(X\).  The claims that
Wright is available only at integral centres and that the nonconstant
connector necessarily fails at nonintegral centres are therefore too
strong.

After the split, the direct source bounds remain

\[
E_{\rm BC,1}={29\over20}+{7\ell\over20}-{13\delta\over10},
\qquad
E_{\rm BC,2}={3\over2}+{\ell\over2}-{3\delta\over2},
\]

and

\[
E_{\rm W,dir}={13\over8}+{\ell\over4}-{13\delta\over8}.
\]

They exceed the existing absolute exponent
\(u=\delta-\ell\) by more than \(3/10\), \(1/4\), and \(5/16\),
respectively, throughout the full polytope.

The conductor's elementary detector of \(a=m^2\) is legal but not sharp.
The sharp diagonal projective norm is
\(\sum_{m\asymp K}m^{-1}\asymp1\), a factor \(K^{1/2}\) above the
direct \(k^{-1}\) vector norm, not the additional \(K^{1/2}\) paid by the
conductor detector.  With this repair the square-connector source bounds
are smaller than the conductor candidate's displayed bounds, but every one
still exceeds \(X^{u+\varepsilon}\) by a fixed power.

The two completion orders must be kept distinct.

* If the smooth short \(k\)-weight is completed first and inversion is then
  used, the complete inverse-only sum is a Ramanujan sum, because inversion
  permutes the reduced residues.  After the full gcd decomposition, the
  Fourier coefficients have size
  \(R^{-1}(1+|h|/\Delta)^{-B}\), and the modulus-gcd summation gives exactly
  \(\Delta X^\varepsilon\).  This recovers the existing absolute capacity;
  it does not produce the larger
  \(\Delta R^{19/20}\) cost asserted in the statement-only report.
* If the sparse inverse selector is formed first and that irregular
  \(m\)-weight is then completed, the complete sum is the genuine
  Kloosterman sum \(S(x_0,h;n)\).  Its exact Fourier coefficient mass and
  complete \(h\)-second moment give
  \(R\sqrt{\Delta}\,X^\varepsilon\), which is much worse than \(\Delta\).

The shifted physical fixed residue remains structurally outside Wright's
dispersion corollaries.  Bettin--Chandee Corollary 1 does admit the exact
fixed-determinant map, but its per-level error is
\(X^{3/5}R^{17/20}X^\varepsilon\), while its main terms aggregate only to
the already known \(\Delta X^\varepsilon\) capacity.

Thus no audited source theorem improves the accepted envelope

\[
X^\varepsilon\min\left(\Delta,
\sqrt{XL/D}+\sqrt{X/(LD)}\right),
\]

whose exponent is
\(\beta(u)=\min(u,(1-u)/2)>1/4\).  The smallest owner-complete
quarter-scale survivor remains the entire flat smooth prescribed-centre
packet.  This is a scoped source-method obstruction, not a lower bound for
the literal signed wave.

## 2. Exact statement and hypotheses

Let

\[
D=X^\delta,\qquad L=X^\ell,\qquad
R=X^{1-\delta},\qquad K=X^{1+\ell-2\delta},\qquad
\Delta={R\over K}=X^{\delta-\ell},
\]

where

\[
{1\over4}\leq\delta<{1\over2},\qquad
0\leq\ell<\delta-{1\over4},\qquad
178\ell+1638\delta>463.
\]

Put \(u=\delta-\ell\) and
\(F=XK/R=X^{1-u}\).  Then

\[
{1\over4}<u<{1\over2},\qquad K<R,\qquad F\to\infty.
\]

Only the flat smooth principal packet

\[
\mathscr R_{D,L}(X)=
\sum_{\substack{r\geq1\\r\ {\rm odd}}}\chi_4(r)
W\!\left({X\over rD}\right)
\sum_{k\geq1}{q_L(4Xk/r^2)\over k}e(Xk/r)
\tag{2.1}
\]

and its exact prescribed-centre divisor form are in scope.

The primary-source hypotheses used are these.

1. Bettin--Chandee, arXiv:1502.00769v1, Theorem 1 has three independent
   dyadic coefficient sequences, \((m,n)=1\), and one absolute value
   outside the whole trilinear sum.  Its printed theorem does not type
   \(\vartheta\), but its proof uses gcds with \(\vartheta\) and primes
   coprime to it.  The source-safe reading is
   \(\vartheta\in\mathbb Z\setminus\{0\}\).  Remark 1 permits a smooth
   real phase perturbation with its stated derivative cost.
2. Wright, arXiv:2604.25177v2, Theorem 2.1 explicitly inherits a nonzero
   integral frequency and assumes
   \(M\ll N^2\), \(R_0\ll M^C\), and
   \((m,nR_0)=1\).  Its coefficients are independent and arbitrary and
   its absolute value is outside the total trilinear sum.  The fifth
   parenthetical term, which is decisive here, agrees in the printed
   theorem and proof.
3. Wright Corollary 2.2 and Theorem 2.3 concern a modulus sum of individual
   absolute discrepancies for a fixed nonzero coprime integer residue,
   independent convolution coefficients, and a principal reduced-residue
   subtraction.  Corollary 2.2 additionally imposes divisor bounds,
   a Siegel--Walfisz hypothesis, and its three printed size regions.
4. Bettin--Chandee Corollary 1 assumes a fixed nonzero determinant,
   four dyadic supports, smooth \(f,g\), and has the main term and error
   printed in primary equation (1.4).

Under the normalized uniform smoothness supplied for the flat packet, the
following proposition is valid.

> **Corrected Round-135 proposition.**  The complete smooth profile,
> including the fractional-centre factor \(e(\xi k/r)\), has an exact
> independent-coefficient separation of \(O(1)\) integrated norm.
> With source frequency \(x_0\), the direct \(m=1\) and coprime
> \(a=m^2\) dictionaries are source-legal for every real \(X\), but all
> their Bettin--Chandee and Wright bounds exceed \(\Delta\) by a fixed
> power throughout the stated polytope.  Smooth-weight-first completion is
> an owner-complete Ramanujan calculation of size
> \(\Delta X^\varepsilon\); inverse-selector-first completion is a
> Kloosterman calculation of size
> \(R\sqrt{\Delta}\,X^\varepsilon\).  The physical fixed residue does not
> meet Wright's dispersion hypotheses.  The exact fixed-determinant
> Corollary 1 map has aggregate main-term capacity \(\Delta X^\varepsilon\)
> and an error far larger than \(\Delta\).  Hence these sources prove
> neither the quarter estimate nor a strict improvement of the accepted
> flat-wave envelope.

## 3. Proof or derivation

**Primary-source frequency and exact profile separation.**  Set
\(k=Ku\), \(r=Rv\), and write
\(\widetilde q_L(z)=q_L(Lz)\).  On the buffered fixed compact support,
the complete normalized amplitude is

\[
G_\xi(u,v)=u^{-1}\widetilde q_L(4u/v^2)W(1/v)
e\!\left(\xi\Delta^{-1}{u\over v}\right).
\tag{3.1}
\]

All normalized derivatives are bounded uniformly in
\(0\leq\xi<1\), because \(\Delta^{-1}<1\).  Fourier inversion in
\((\log u,\log v)\), after a fixed smooth extension, gives

\[
G_\xi(u,v)=\iint_{\mathbb R^2}\widehat G_\xi(t_1,t_2)
u^{it_1}v^{it_2}\,dt_1dt_2,\qquad
\iint|\widehat G_\xi(t_1,t_2)|\,dt_1dt_2\ll1.
\tag{3.2}
\]

Thus

\[
e(Xk/r)=e(x_0k/r)e(\xi k/r)
\]

may be treated with the integral source frequency \(x_0\), while the
fractional factor remains inside the exactly separated arbitrary
coefficients.  Each direct fibre has

\[
\|\alpha\|_2=1,\qquad
\|\beta\|_2\ll R^{1/2},\qquad
\|\nu\|_2\ll K^{-1/2},
\tag{3.3}
\]

and \(\chi_4(r)\) remains in \(\beta_r\) until the positive norm is taken.
This argument is legal for Wright as well as Bettin--Chandee; it does not
need a source perturbation theorem.  For comparison, Bettin--Chandee
Remark 1 also handles the direct map with perturbation
\(f=\xi a/n\) and parameter \(Y\asymp K\).

**Direct \(m=1\).**  Take

\[
a=k,\qquad m=1,\qquad n=r,\qquad
(A,M,N,R_0,\vartheta)=(K,1,R,1,x_0).
\tag{3.4}
\]

The phase is exact and the coprimality is automatic.  From (3.3),
Bettin--Chandee gives

\[
F^{1/2}\left(R^{11/10}K^{-3/20}+R\right)X^\varepsilon.
\tag{3.5}
\]

Its two exponents are

\[
E_{\rm BC,1}={29\over20}+{7\ell\over20}-{13\delta\over10},
\qquad
E_{\rm BC,2}={3\over2}+{\ell\over2}-{3\delta\over2}.
\tag{3.6}
\]

The first dominates because
\(R^{1/10}K^{-3/20}>1\).  More importantly,

\[
\begin{aligned}
E_{\rm BC,1}-u
&={29\over20}+{27\ell\over20}-{23\delta\over10}
>{3\over10},\\
E_{\rm BC,2}-u
&={3\over2}+{3\ell\over2}-{5\delta\over2}
>{1\over4}.
\end{aligned}
\tag{3.7}
\]

Wright's conditions hold with \(R_0=1\).  Its fifth term dominates and
gives

\[
R^{11/8}F^{1/4}X^\varepsilon
=X^{E_{\rm W,dir}+\varepsilon},
\qquad
E_{\rm W,dir}={13\over8}+{\ell\over4}-{13\delta\over8},
\tag{3.8}
\]

with

\[
E_{\rm W,dir}-u
={13\over8}+{5\ell\over4}-{21\delta\over8}
>{5\over16}.
\tag{3.9}
\]

A growing fixed factor is unavailable in the owner-complete direct row:
\(M=1\) forces \(R_0=O(1)\), and the moduli have no common growing
factor.

**The nonconstant connector and its sharp norm.**  On \((k,r)=1\), take

\[
m=k,\qquad a=j^2,\qquad j=m,\qquad n=r,\qquad\vartheta=x_0.
\tag{3.10}
\]

Then

\[
x_0m^2\overline m/r\equiv x_0m/r\pmod1.
\]

The fractional factor has already been placed in the separated amplitude
(3.1).  Equivalently, Bettin--Chandee Remark 1 can use
\(f=\xi m/n\) and \(Y\asymp K^2\), whose contribution is negligible
beside \(x_0A\).  Thus the connector is legal for arbitrary real \(X\),
not merely integral \(X\).

The exact diagonal decomposition is

\[
\mathbf1_{j=m}=\int_0^1e(t(j-m))\,dt,\qquad
\alpha_m(t)=m^{-1/2}e(-tm),\qquad
\nu_{j^2}(t)=j^{-1/2}e(tj).
\tag{3.11}
\]

Both norms are \(O(1)\).  It is sharp for the unit flat diagonal: the
matrix \(C_{j,m}=m^{-1}\mathbf1_{j=m}\) has singular values \(m^{-1}\),
so

\[
\|C\|_*=\sum_{m\asymp K}m^{-1}\asymp1.
\tag{3.12}
\]

Any Hilbert-space rank-one decomposition has total product norm at least
this nuclear norm.  Relative to
\(\|k^{-1}\|_2\asymp K^{-1/2}\) in the direct map, the diagonal costs the
sharp factor \(K^{1/2}\).  For a separated literal profile the same
argument gives an \(O(1)\) upper cost; the matching lower bound uses the
flat nonzero subcell and is not a lower bound for the oscillatory sum.

The conductor detector
\(\mathbf1_{a=m^2}=\int e(t(a-m^2))dt\), with all
\(a\asymp K^2\) present, has norm product \(K^{1/2}\).  It is a valid
but nonminimal expansion and makes the conductor's square bounds too large
by \(K^{1/2}\).

With the sharp decomposition,

\[
A=K^2,\qquad M=K,\qquad N=R,\qquad
\|\alpha\|_2\|\nu\|_2\|\beta\|_2\ll R^{1/2}.
\]

The two Bettin--Chandee terms are

\[
F^{1/2}K^{21/20}R^{11/10},
\qquad
F^{1/2}K^{11/8}R,
\tag{3.13}
\]

with exponents

\[
\begin{aligned}
E_{\rm BC,sq,1}
&={53\over20}+{31\ell\over20}-{37\delta\over10},\\
E_{\rm BC,sq,2}
&={23\over8}+{15\ell\over8}-{17\delta\over4}.
\end{aligned}
\tag{3.14}
\]

Their margins over \(u\) satisfy

\[
E_{\rm BC,sq,1}-u>{3\over10},\qquad
E_{\rm BC,sq,2}-u>{1\over4}.
\tag{3.15}
\]

Wright's fifth term gives

\[
F^{1/4}K R^{11/8}
=X^{{21\over8}+{5\ell\over4}-{29\delta\over8}},
\tag{3.16}
\]

whose exponent exceeds \(u\) by more than \(5/16\).  The square connector
therefore repairs the nonconstant inverse coordinate but has no useful
capacity.

**Completion order I: smooth weight first, then inversion.**  The complete
owner ledger starts with the exact gcd decomposition

\[
\mathscr R_{D,L}(X)
=\sum_{\substack{g\geq1\\g\ {\rm odd}}}\chi_4(g)
\sum_{\substack{n\geq1\\n\ {\rm odd}}}\chi_4(n)
W\!\left({X\over gnD}\right)
\sum_{\substack{j\geq1\\(j,n)=1}}
b_{g,n}(j)e(x_0j/n),
\tag{3.17}
\]

where

\[
b_{g,n}(j)={q_L(4Xj/(gn^2))\over gj}e(\xi j/n).
\tag{3.18}
\]

Here \(n\asymp R/g\), \(j\asymp J=K/g\), and
\(n/J=\Delta\).  Define the normalized Fourier coefficients

\[
\widehat b_{g,n}(h)
={1\over n}\sum_{j\bmod n}b_{g,n}(j)e(-hj/n).
\tag{3.19}
\]

Smoothness, support length \(J\), and pointwise size \(K^{-1}\) give, for
every fixed \(B>2\),

\[
|\widehat b_{g,n}(h)|
\ll_B {1\over R}
\left(1+{\|h\|_n\over\Delta}\right)^{-B},
\qquad
\sum_h|\widehat b_{g,n}(h)|\ll {1\over K}.
\tag{3.20}
\]

The factor \(e(\xi j/n)\) does not change these estimates because
\(J/n=\Delta^{-1}\).

Fourier inversion followed, if desired, by \(j=\overline m\) gives

\[
\begin{aligned}
\sum_{(j,n)=1}b_{g,n}(j)e(x_0j/n)
&=\sum_{h\bmod n}\widehat b_{g,n}(h)
\sum_{j\bmod n}^{*}e((x_0+h)j/n)\\
&=\sum_{h\bmod n}\widehat b_{g,n}(h)
\sum_{m\bmod n}^{*}e((x_0+h)\overline m/n)\\
&=\sum_{h\bmod n}\widehat b_{g,n}(h)
\mathfrak c_n(x_0+h),
\end{aligned}
\tag{3.21}
\]

where \(\mathfrak c_n\) is the Ramanujan sum.  The second equality uses
that inversion permutes the reduced residues.  There is no two-variable
Kloosterman sum in this completion order.

Since
\(|\mathfrak c_n(q)|\leq(n,q)\) and, uniformly for nonzero
\(q\asymp X\),

\[
\sum_{n\asymp T}(n,q)\ll_\varepsilon T X^\varepsilon,
\tag{3.22}
\]

equations (3.20)--(3.22) give

\[
\begin{aligned}
|\mathscr R_{D,L}(X)|
&\ll_\varepsilon
\sum_{g\ll K}\sum_h {1\over R}
\left(1+{|h|\over\Delta}\right)^{-B}
{R\over g}X^\varepsilon\\
&\ll_\varepsilon \Delta X^\varepsilon.
\end{aligned}
\tag{3.23}
\]

The harmonic \(g\)-sum is absorbed in \(X^\varepsilon\).
This is owner-complete and retains every noncoprime stratum until the
final triangle.  It exactly recovers the known divisor capacity and does
not improve it.

**Completion order II: inverse selector first, then completion.**  Instead
put

\[
\gamma_{g,n}(m)=b_{g,n}(\overline m_n)
\]

on reduced residues whose inverse lies in the \(J\)-short support, and
zero elsewhere.  This is the joint inverse-selector matrix.  Its normalized
Fourier transform satisfies the exact Parseval ledger

\[
\sum_{h\bmod n}|\widehat\gamma_{g,n}(h)|^2
={1\over n}\sum_{m\bmod n}|\gamma_{g,n}(m)|^2
\ll {1\over RK}.
\tag{3.24}
\]

Fourier inversion now gives

\[
\sum_{m\bmod n}^{*}\gamma_{g,n}(m)e(x_0\overline m/n)
=\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(x_0,h;n),
\tag{3.25}
\]

with the genuine Kloosterman sum

\[
S(a,h;n)=\sum_{m\bmod n}^{*}e((a\overline m+hm)/n).
\]

The exact complete-frequency second moment is

\[
\sum_{h\bmod n}|S(x_0,h;n)|^2=n\varphi(n)\leq n^2.
\tag{3.26}
\]

It follows from (3.24)--(3.26) that one modulus row is at most

\[
{n\over\sqrt{RK}}\asymp{\sqrt\Delta\over g}.
\]

There are \(O(R/g)\) such \(n\)-rows at fixed \(g\), so taking the
\(n\)-triangle and then summing \(g\) gives

\[
|\mathscr R_{D,L}(X)|
\ll_\varepsilon R\sqrt\Delta\,X^\varepsilon.
\tag{3.27}
\]

Its exponent is \(1-(\delta+\ell)/2\), and

\[
1-{\delta+\ell\over2}-u
=1-{3\delta\over2}+{\ell\over2}>{1\over4}.
\tag{3.28}
\]

Thus inverse-selector-first completion is strictly worse than the
Ramanujan order and the existing capacity.  The fractional centre changes
only \(\gamma_{g,n}\) by a unit smooth factor, so it changes neither
(3.24) nor the integral complete sum.

**Physical residue and fixed determinant.**  With
\(s=x_0+t\), the divisor form is exactly

\[
\sum_t\sum_{\substack{r\asymp R,\ r\ {\rm odd}\\
t\equiv-x_0\ ({\rm mod}\ r)}}
\chi_4(r)W\!\left({X\over rD}\right)
\mathcal Q_L\!\left({r(\xi-t)\over4X}\right),
\tag{3.29}
\]

effectively for \(|t-\xi|\ll\Delta X^\varepsilon\).
Using \(s\) gives residue zero.  Using \(t\) gives the fixed integer
residue \(-x_0\), but it is not uniformly coprime to \(r\); the short
variable \(t\) is not a product of two independent positive dyadic
sequences; its coefficient is joint in \((r,t)\); and the product scale
would be \(\Delta\), while the residue has size \(x_0\asymp X\).
Wright's corollaries also place an absolute value inside the modulus sum
and subtract a principal reduced-residue mean.  Formula (3.29) has neither
that convolution nor that absolute-value structure.  Hence no literal
Wright dispersion application exists.

There is, however, an exact Bettin--Chandee Corollary 1 map.  For each
fixed nonzero integer
\(\tau=x_0-dr\), take

\[
(m_1,n_2,m_2,n_1)=(d,r,1,x_0),\qquad
\Delta_{\rm det}=-\tau.
\tag{3.30}
\]

Put the complete character and kernel into

\[
\beta_r^{(\tau)}=\chi_4(r)W\!\left({X\over rD}\right)
\mathcal Q_L\!\left({r(\xi+\tau)\over4X}\right).
\]

Then \(M_1\asymp D\), \(M_2\asymp1\),
\(N_1\asymp X\), \(N_2\asymp R\),
\(\|\alpha\|_2=1\), \(\|\beta^{(\tau)}\|_2\ll R^{1/2}\), and
the source aspect ratio is \(O(1)\) because \(DR=X\).
The Corollary 1 error is therefore

\[
R^{1/2}(XR)^{7/20}X^{1/4+\varepsilon}
=X^{3/5}R^{17/20}X^\varepsilon,
\tag{3.31}
\]

with exponent

\[
E_{\rm det}={29\over20}-{17\delta\over20}>{41\over40}.
\tag{3.32}
\]

Its margin over \(u\) is greater than \(21/40\).
For the main term, the source integral is \(O(X)\); after the gcd
prefactor its absolute contribution is
\(O((x_0,r)/r)\), and

\[
\sum_{r\asymp R}{(x_0,r)\over r}\ll_\varepsilon X^\varepsilon.
\tag{3.33}
\]

There are \(O(\Delta X^\varepsilon)\) effective nonzero determinant
levels.  Their main terms therefore return
\(\Delta X^\varepsilon\), while their errors acquire another factor
\(\Delta\).  The excluded level \(\tau=0\) is one product level and is
divisor-bounded by \(X^\varepsilon\).

Finally, all source exponents above are strictly larger than \(u\), while
(3.23) and the determinant main terms merely equal the absolute branch.
The additional inequality
\(178\ell+1638\delta>463\) opens no hidden chamber.  The already proved
curvature branch has exponent \((1-u)/2\) when it is smaller than \(u\);
none of these source interfaces reaches it, much less \(1/4\).

## 4. First doubtful or unproved step

The corrected no-go has no remaining source or exponent gap.  The first
unproved step in a positive continuation is a new theorem for the literal
joint signed family

\[
\sum_{k\asymp K}{1\over k}\sum_{r\asymp R}
\chi_4(r)G(k/K,r/R)e(Xk/r),
\tag{4.1}
\]

or its exact fixed-centre form (3.29), that keeps the
\(\chi_4(r)\)-sum before positive row norms and beats

\[
X^{\beta(u)+\varepsilon},\qquad
\beta(u)=\min(u,(1-u)/2).
\]

Neither primary source accepts the required modulus-dependent coefficient
matrix or supplies a pointwise signed fixed-centre dispersion estimate.

Four precise overclaims must be repaired in the Round-135 evidence.

1. The source report's statement that Wright is legal only for integral
   \(X\) overlooks the exact coefficient split (3.1)--(3.2).
2. The discovery report's restriction of the \(a=m^2\) connector and
   Kloosterman completion to integral \(X\) overlooks the same split.
3. The conductor's \(a=m^2\) detector is nonsharp by \(K^{1/2}\);
   (3.11)--(3.16) are the sharp replacement.
4. The statement-only report's
   \(\Delta R^{19/20}\) completion estimate is a legal but extremely
   wasteful source bound for the completed blocks, not the correct
   completion capacity.  The complete inverse-only sum in that order is
   Ramanujan and gives (3.23).  This must not be conflated with the
   inverse-selector-first Kloosterman order (3.25).

These repairs strengthen the exact dictionaries and completion capacity,
but none proves the quarter target.  They also do not show that the literal
sum is large, prohibit a future coupled-coefficient theorem, or license a
claim outside the flat packet.

## 5. Required control test and outcome

1. **Primary-source control -- pass with frequency repair.**  The audited
   versions are Bettin--Chandee arXiv:1502.00769v1, Theorem 1, Remark 1,
   and Corollary 1, and Wright arXiv:2604.25177v2, Theorem 2.1 and the
   stated dispersion corollaries.  Integral frequency is enforced through
   \(x_0\); the withdrawn arXiv:2601.00292 is not used.
2. **Real-centre control -- pass.**  The exact factor
   \(e(\xi k/r)\) is uniformly smooth at normalized scale
   \(k/r\asymp\Delta^{-1}\) and is separated with the profile.  It repairs
   \(m=1\), \(a=m^2\), Ramanujan completion, and Kloosterman completion
   without changing their norms.
3. **Moving-profile control -- pass.**  Equation (3.2) has \(O(1)\)
   integrated coefficient mass and preserves \(q_L\), \(W\), \(1/k\), and
   the fractional centre.  No profile is frozen or deleted.
4. **Direct-source capacity -- fail target.**  Equations
   (3.7) and (3.9) show fixed positive margins over \(\Delta\) on the
   full polytope.  Wright's fixed factor cannot grow in the direct row.
5. **Nonconstant-connector control -- pass algebraically, fail
   capacity.**  The \(a=m^2\) identity is exact on each coprime stratum;
   its sharp diagonal norm is (3.12), and the repaired bounds
   (3.13)--(3.16) still exceed \(\Delta\).
6. **Smooth-first completion -- pass with no gain.**  The complete sum is
   Ramanujan, the coefficient is
   \(R^{-1}(1+|h|/\Delta)^{-B}\), the gcd strata are all retained, and
   their harmonic sum gives exactly \(\Delta X^\varepsilon\).
7. **Inverse-first completion -- pass with capacity failure.**  The
   complete sum is \(S(x_0,h;n)\), Parseval gives \(1/(RK)\), and its exact
   complete-frequency second moment gives \(R\sqrt\Delta X^\varepsilon\).
8. **Physical and determinant controls -- pass as a no-go.**  The fixed
   residue fails Wright's convolution, coprimality, size, coefficient, and
   absolute-value interfaces.  The determinant dictionary is legal, but
   its main term returns \(\Delta\) and its error is (3.31).
9. **Character and adversary control -- pass.**  The true
   \(\chi_4\) remains in the modulus coefficient through every exact
   identity.  Direct source norms, Ramanujan gcd summation, rowwise
   Kloosterman completion, and determinant triangulation then erase its
   special sign.  Their failure is a method-capacity statement, not a
   lower bound for the literal array.
10. **Full-polytope and scope control -- pass.**  Every margin uses only
    \(\ell\geq0\), \(\delta<1/2\), and
    \(\ell<\delta-1/4\), so it holds throughout the frozen region.
    No sharp, clipped, starred, hard, arithmetic-owner, stationary,
    transition, remainder, complete-UNBAL, M9-M2, endpoint, M9, or global
    owner is absorbed.

The review used 100% analytical/algebraic work and no numerical
experiment.

## 6. Dependencies and exact artifacts used

Repository artifacts read for this review:

1. protocol.md.
2. state/proof_obligations.yml, especially the three active Round-135
   obligations.
3. state/active_campaign.yml.
4. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/briefs/blind_post_unmask_source_and_capacity_audit.md.
5. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/primary_source_manifest.md.
6. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/wright_bc_exact_source_card.md.
7. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md.
8. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/blind_inverse_congruence_interface_audit.md.
9. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/candidates/conductor_degenerate_source_capacity.md.
10. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/blind_statement.md.

Primary pages checked independently:

* Bettin--Chandee,
  [arXiv:1502.00769v1](https://arxiv.org/html/1502.00769v1):
  Theorem 1, Remark 1, the proof's integrality uses, and Corollary 1.
* Wright,
  [arXiv:2604.25177v2](https://arxiv.org/html/2604.25177v2):
  the integral-frequency setup, Theorem 2.1, Corollary 2.2, and
  Theorem 2.3.
* The [withdrawal record for arXiv:2601.00292](https://arxiv.org/abs/2601.00292)
  was used only as a negative bibliographic control.

No secondary source, sibling review, or numerical computation supplied a
mathematical claim.

## 7. Recommended state effect

**revise.**  Revise the conductor candidate and the two nonblind reports
by incorporating the real-centre coefficient split, the sharp
\(a=m^2\) diagonal norm, and the distinction between Ramanujan
smooth-first completion and Kloosterman inverse-first completion.  After
those repairs, the corrected proposition in Section 2 is suitable for
promotion as a scoped source-level obstruction.

Keep
M9-M2-smooth-unbalanced-three-quarter-estimate and every downstream
complete-UNBAL, endpoint, M9-M2, M9, quarter-target, and global obligation
open.  The only positive completion bound recovered here is the already
accepted \(\Delta X^\varepsilon\) capacity, so no proof-state target or
downstream implication changes.
