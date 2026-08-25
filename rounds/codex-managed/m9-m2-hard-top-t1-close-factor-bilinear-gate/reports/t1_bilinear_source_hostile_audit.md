# Round 162 source-hostile audit: the literal \(t=1\) close-factor scalar

- Campaign: `m9-m2-hard-top-t1-close-factor-bilinear-gate`
- Round: 162
- Task: `t1_bilinear_source_hostile_audit`
- Role: primary-source hostile auditor
- Starting graph SHA-256:
  `8d39b06bd12357e337159473da3d4d6ec0c71d0ab3217588e4c6b5b34973b422`
- Allocation: 100% analytic, algebraic, and primary-source verification;
  0% numerical experimentation
- Status: candidate evidence only

## 1. Result: a literal named-route bilinear no-go

Let

\[
\begin{aligned}
\mathcal S_{L,1}=\sum_{\substack{d_1d_2\asymp L^2\\
d_1,d_2\ {\rm squarefree},\ (d_1,d_2)=1\\
d_1\ {\rm odd},\ d_2\le d_1\le4d_2}}
&\chi _4(d_1)\left(\frac{L^2}{d_1d_2}\right)^{3/4}
\eta_L(d_1)\Phi\!\left(\frac{d_1}{H+1}\right)\\
&\quad\times W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right)
e(J\sqrt{d_1d_2})
\end{aligned}
\tag{162.T1}
\]

with the literal shell, half-open block, floors, stars, cone entries and
exits, profile endpoint values, and zero extension from the frozen statement.
Here

\[
J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad q_X=X/y^2,
\qquad H=\lfloor yX^{-1/4}\rfloor=J^{1/2}+O(1),
\tag{162.T2}
\]

and \(1\ll L\ll H\).  The following route-scoped result is proved.

> **Named-source and positive-transform no-go.**  The character-preserving
> one-variable Poisson transform closed row by row, smooth two-variable
> Poisson followed by positive summation of its dual modes, Bombieri--Iwaniec
> separable double-large-sieve placement, the Duke--Friedlander--Iwaniec,
> Bettin--Chandee, and Dong--Robles--Zeindler Kloosterman-fraction theorems
> audited below, and the Robert--Sargos or Kowalski--Robert--Wu direct
> monomial theorems do not prove
> \[
> |\mathcal S_{L,1}|\ll_\varepsilon L^{3/2}X^\varepsilon
> \tag{162.T3}
> \]
> for the literal coefficient and the full allowed \(L,J,H,X\) range.

There are three independent, exact reasons.

1.  The phase \(J\sqrt{xz}\) has rank-one Hessian.  Two-dimensional
    Poisson has a one-dimensional stationary hyperbola, not isolated
    two-dimensional saddles.  For a smooth cost-one model its dual product
    collar has
    \[
      \#\{(q,\ell)\}\ll (J/L+1)X^\varepsilon,
      \qquad |I_{q,\ell}|\ll L^{3/2}J^{-1/2},
    \]
    hence positive capacity \(\sqrt{JL}\,X^\varepsilon\).  Together with
    triviality, the best such positive ledger is
    \[
      \min(L^2,\sqrt{JL})X^\varepsilon
      =L^{3/2}\min(L^{1/2},H/L)X^\varepsilon.
      \tag{162.T4}
    \]
    It is not target-sized on any polynomial interior range
    \(1\ll L=o(H)\).  It is merely target-scale when \(L\asymp H\), before
    the physical openings and hard pieces are restored.
2.  Exact squarefree/coprime opening produces Möbius-weighted, rescaled
    hard cones.  For each fixed opening, with \(Q=[\rho^2,\kappa]\) and
    \(R=[\tau^2,\kappa]\), the dual collar is
    \(|s\ell-XQR|\ll QRJ/L\), but its positive capacity remains
    \(\sqrt{JL}\); summing openings is not
    free.  Cancellation between these opened families or between the two
    quarter-shift character families is precisely the unproved arithmetic
    step.
3.  Even after granting a counterfactual cost-one separation of every
    physical profile and hard boundary, the strongest directly relevant
    real monomial card checked here, Kowalski--Robert--Wu Proposition 5,
    restores
    \[
      J^{1/8}L^{13/8}+L^{3/2}+L^{7/4}
      +J^{-1/2}L^{3/2}.
      \tag{162.T5}
    \]
    The Kloosterman-fraction sources concern modular inverses with integral
    numerators and moduli.  The actual character-Poisson phase is the
    ordinary real reciprocal \(e(Xd_2/q)\), with arbitrary real \(X\), and
    has no literal substitution into those theorems.

This result is not a lower bound for (162.T1), not an impossibility theorem
for all literature, and not a rejection of a bespoke theorem using the actual
Möbius and \(\chi_4\) signs before positive norms.

## 2. Exact statement, hypotheses, and primary-source cards

### 2.1 Literal coefficient and orientation

On \(t=1\), the accepted incidence forces \(g=u=v=1\).  Thus both variables
in (162.T1) are \(\asymp L\), and

\[
 d_1,d_2\text{ squarefree},\ (d_1,d_2)=1
 \quad\Longleftrightarrow\quad \mu^2(d_1d_2)=1.
\tag{162.T6}
\]

The displayed orientation \(d_2\le d_1\le4d_2\) is retained throughout;
no symmetric duplication or interchange of \(d_1,d_2\) is made.  In
particular, \(d_1\) is odd while \(d_2\) may be even.  The factor 2 in an
even product lies in \(d_2\), and a swap would move the character to a
coefficient that is not present in (162.T1).

For every integer \(n\), not merely for odd \(n\),

\[
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i}.
\tag{162.T7}
\]

The two signs in (162.T7) are therefore kept together until the explicitly
labelled hostile positive ledgers below.

### 2.2 Bombieri--Iwaniec, Lemma 2.4

For \(\mathcal X,\mathcal Y\subset\mathbb R^K\), arbitrary complex
coefficients \(a(x),b(\eta)\), and positive \(X_k,Y_k\), Bombieri--Iwaniec
consider the separated bilinear form

\[
 \sum_{\substack{x\in\mathcal X,\ |x_k|\le X_k\\
                   \eta\in\mathcal Y,\ |\eta_k|\le Y_k}}
 a(x)b(\eta)e(x\cdot\eta).
\]

Their Lemma 2.4 bounds its square by

\[
 (2\pi^2)^K\prod_{k=1}^K(1+X_kY_k)
 \mathcal B(b;X)\mathcal B(a;Y),
\tag{162.T8}
\]

where both \(\mathcal B\)-forms are sums of absolute coefficient products
over coordinatewise near-collision windows.  Thus the theorem requires a
coefficient \(a(x)b(\eta)\), not the joint physical coefficient in
(162.T1).  Primary source: E. Bombieri and H. Iwaniec, *On the order of
\(\zeta(1/2+it)\)*, Ann. Scuola Norm. Sup. Pisa 13 (1986), Lemma 2.4,
[primary PDF](https://www.numdam.org/item/ASNSP_1986_4_13_3_449_0.pdf).

### 2.3 Kowalski--Robert--Wu, Proposition 5

Put

\[
 S(M,N)=\sum_{m\sim M}\sum_{n\sim N}\varphi_m\psi_n
 e\!\left(F\frac{m^\alpha n^\beta}{M^\alpha N^\beta}\right),
\]

where \(F>0\), \(M,N\ge1\), \(|\varphi_m|,|\psi_n|\le1\),
\(m\sim M\) means \(M\le m<2M\), and
\(\alpha,\beta\in\mathbb R\setminus\{0,1\}\).  Proposition 5 states

\[
 S(M,N)\ll_\varepsilon
 \left((FM^6N^6)^{1/8}+M^{1/2}N+MN^{3/4}+F^{-1/2}MN\right)(MN)^\varepsilon.
\tag{162.T9}
\]

Primary source: E. Kowalski, O. Robert, and J. Wu, *Small gaps in
coefficients of L-functions and B-free numbers in short intervals*, Rev.
Mat. Iberoamericana 23 (2007), Proposition 5,
[official PDF](https://ems.press/content/serial-article-files/38194?nt=1).

### 2.4 Robert--Sargos, Theorem 1

For positive integers \(H_0,N_0,M_0\), \(\Xi>1\), coefficients
\(|a(h,n)|,|b(m)|\le1\), and fixed reals satisfying
\(\alpha(\alpha-1)\beta\gamma\ne0\), their Theorem 1 bounds

\[
 \sum_{h\sim H_0}\sum_{n\sim N_0}\sum_{m\sim M_0}
 a(h,n)b(m)e\!\left(\Xi
 \frac{h^\beta n^\gamma m^\alpha}
 {H_0^\beta N_0^\gamma M_0^\alpha}\right)
\]

by

\[
 (H_0N_0M_0)^{1+\varepsilon}
 \left\{
 \left(\frac{\Xi}{H_0N_0M_0^2}\right)^{1/4}
 +(H_0N_0)^{-1/4}+M_0^{-1/2}+\Xi^{-1/2}
 \right\}.
\tag{162.T10}
\]

Primary source: O. Robert and P. Sargos, *Three-dimensional exponential
sums with monomials*, J. reine angew. Math. 591 (2006), Theorem 1,
[author PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf).

### 2.5 Duke--Friedlander--Iwaniec: Theorems 1--2 and Lemma 8

For a positive integer \(a\), arbitrary complex \(\alpha_m,\beta_n\)
supported on \(M<m\le2M\), \(N<n\le2N\), and \((m,n)=1\), put

\[
 \mathcal B_a(M,N)=\sum_{m,n}\alpha_m\beta_n
 e\!\left(a\frac{\overline m}{n}\right),
\tag{162.T11}
\]

where \(\overline m\) is the multiplicative inverse modulo \(n\).
Theorems 1 and 2 state, respectively,

\[
 \mathcal B_a(M,N)\ll\|\alpha\|_2\|\beta\|_2
 \left((M+N)^{1/2}+left(1+\frac a{MN}\right)^{1/2}
 \min(M,N)\right)(MN)^\varepsilon,
\tag{162.T12}
\]

\[
 \mathcal B_a(M,N)\ll\|\alpha\|_2\|\beta\|_2
 (a+MN)^{3/8}(M+N)^{11/48+\varepsilon}.
\tag{162.T13}
\]

Their Lemma 8 takes

\[
 I=\{x:X_0<x\le X_0+U,\ x\equiv r\pmod k\},
\]

a Dirichlet character \(\chi\) modulo \(c\), \((c,k)=1\), and integers
\(a,b\), and gives

\[
 \left|\sum_{x\in I}\chi(x)
 e\!\left(\frac{a\overline x+bx}{c}\right)\right|
 \le \left(\frac{U}{ck}+2\log(3c)\right)
 (a,c)^{1/2}c^{1/2}\tau(c).
\tag{162.T14}
\]

Primary source: W. Duke, J. Friedlander, and H. Iwaniec, *Bilinear forms
with Kloosterman fractions*, Invent. Math. 128 (1997), Theorems 1--2 and
Lemma 8, [author PDF](https://www.math.ucla.edu/~wdduke/preprints/bilinear.pdf).

### 2.6 Bettin--Chandee, Theorems 1--2

For dyadic positive-integer variables \(a\sim A,m\sim M,n\sim N\),
\((m,n)=1\), arbitrary separated coefficients
\(\nu_a\alpha_m\beta_n\), and a fixed nonzero integral arithmetic
multiplier \(\vartheta\), Theorem 1 bounds

\[
 \sum_{a,m,n}\nu_a\alpha_m\beta_n
 e\!\left(\vartheta\frac{a\overline m}{n}\right)
\]

by

\[
\begin{aligned}
\|\nu\|_2\|\alpha\|_2\|\beta\|_2
\left(1+\frac{|\vartheta|A}{MN}\right)^{1/2}
\big(& (AMN)^{7/20+\varepsilon}(M+N)^{1/4}\\
& +(AMN)^{3/8+\varepsilon}(AN+AM)^{1/8}\big).
\end{aligned}
\tag{162.T15}
\]

Theorem 2 treats instead the additional Jacobi factor \((m/n)\), under
\((m,n)=(2,mn)=1\), and has the same large-parameter factor followed by

\[
 (MN)^{3/10}(AM+AN)^{7/20+\varepsilon}
 +A^{1/2}(M+N)^{7/8+\varepsilon}.
\tag{162.T16}
\]

Primary source: S. Bettin and V. Chandee, *Trilinear forms with
Kloosterman fractions*, Adv. Math. 328 (2018), Theorems 1--2,
[primary arXiv text](https://arxiv.org/html/1502.00769v1).

### 2.7 Dong--Robles--Zeindler, Theorem 1.6 (2026 preprint)

For positive integers \(a,b\), arbitrary separated coefficients, and the
dyadic coprime Kloosterman-fraction form

\[
 \mathcal B_{a,b}(M,N)=\sum_{\substack{M<m\le2M,\ N<n\le2N\\(m,n)=1}}
 \alpha_m\beta_n e\!\left(\frac{a\overline m}{bn}\right),
\tag{162.T17}
\]

with the inverse interpreted exactly as in the source, their Theorem 1.6
states

\[
\begin{aligned}
\mathcal B_{a,b}(M,N)\ll_\varepsilon
\|\alpha\|_2\|\beta\|_2,&(a+bMN)^{1/4}(M+N)^{1/6}\\
&\times\min(M,N)^{1/3}\max(M,N)^{-1/12}(MN)^\varepsilon.
\end{aligned}
\tag{162.T18}
\]

It removes an intermediate squarefree-support restriction from earlier
Kloosterman-fraction arguments, but retains the modular-inverse phase and
separated coefficient.  Primary source: A. Dong, N. Robles, and D.
Zeindler, *Bilinear forms with Kloosterman fractions and applications*,
arXiv:2601.00292v1 (1 January 2026), Theorem 1.6,
[primary record](https://arxiv.org/abs/2601.00292).

## 3. Proof and hostile power derivation

### 3.1 The exact character-Poisson identities

Use the Fourier convention
\(\widehat g(\xi)=\int_{\mathbb R}g(x)e(-\xi x)\,dx\).  For a smooth,
compactly supported model \(g\), (162.T7) and ordinary Poisson give the
exact identity

\[
 \sum_{m\in\mathbb Z}\chi_4(m)g(m)
 =\frac1{2i}\sum_{\sigma=\pm1}\sigma
 \sum_{k\in\mathbb Z}\widehat g(k-\sigma/4).
\tag{162.T19}
\]

For fixed \(z\), insert the square-root phase and write

\[
 r=k-\sigma/4,\qquad
 F_{r}(x;z)=J\sqrt{xz}-rx.
\]

An interior critical point requires \(r>0\) and is

\[
 x_0=\frac{Xz}{4r^2},\qquad
 F_r(x_0;z)=\frac{Xz}{4r},\qquad
 |F_r''(x_0;z)|^{-1/2}
 =\left(\frac{Xz}{2r^3}\right)^{1/2}.
\tag{162.T20}
\]

On the cone, \(r\asymp J\), and the individual stationary scale is
\(\asymp\sqrt{L/J}\).  Put \(q=4r=4k-\sigma\).  Then \(q\) is odd,
\(q\equiv-\sigma\pmod4\), and

\[
 \frac{\sigma}{2i}=-\frac{\chi_4(q)}{2i}.
\tag{162.T21}
\]

Thus the character has not disappeared: it becomes the signed difference
of the two odd dual residue classes, while the transformed phase is

\[
 e\!\left(\frac{Xz}{q}\right).
\tag{162.T22}
\]

Taking absolute values between the two residue classes would discard the
only literal arithmetic sign the proposed route was meant to exploit.

Poisson in the uncharactered variable \(z=d_2\) gives an even more literal
self-return.  For dual integer \(\ell>0\),

\[
 z_0=\frac{Xx}{4\ell^2},\qquad
 J\sqrt{xz_0}-\ell z_0=\frac{Xx}{4\ell},qquad
 |F''(z_0)|^{-1/2}=\left(\frac{Xx}{2\ell^3}\right)^{1/2}.
\tag{162.T23}
\]

At this saddle,

\[
 W\!\left(\sqrt{\frac{q_Xx}{4z_0}}\right)=W(\ell/y),
\tag{162.T24}
\]

and the product of \(z_0^{-3/4}\), the stationary factor, and the remaining
\(L^{3/2}x^{-3/4}\) is exactly

\[
 2L^{3/2}J^{-1/2}x^{-1}.
\tag{162.T25}
\]

Including the stationary signature gives the principal family

\[
\begin{aligned}
2e(-1/8)L^{3/2}J^{-1/2}
\sum_{x\ {
m odd}}\frac{\chi_4(x)\eta_L(x)
\Phi(x/(H+1))}{x}
\sum_{J/2\le\ell\le J}^{\star}
W(\ell/y)e\!\left(\frac{Xx}{4\ell}\right).
\end{aligned}
\tag{162.T26}
\]

The cone determines the displayed dual range and the literal endpoint
convention determines the star.  Formula (162.T26) is the accepted
Round-137 reciprocal hard-TOP principal carrier when the squarefree/coprime
indicator is absent.  With that indicator present, ordinary smooth Poisson
is not yet legal; the exact opening below produces rescaled returned
families.  Zero, nonstationary, crossing, endpoint, and remainder terms are
not included in (162.T26) and cannot be discarded.

### 3.2 Exact Möbius opening and its rescaled supports

A separation-safe exact opening is

\[
\begin{aligned}
&1_{d_1\ {
m sf}}1_{d_2\ {\rm sf}}1_{(d_1,d_2)=1}\\
&\qquad=\sum_{\rho^2\mid d_1}\mu(\rho)
\sum_{\tau^2\mid d_2}\mu(\tau)
\sum_{\substack{\kappa\mid d_1\\\kappa\mid d_2}}\mu(\kappa).
\end{aligned}
\tag{162.T27}
\]

For a fixed opening triple put

\[
 Q=[\rho^2,\kappa],\qquad R=[\tau^2,\kappa],
 \qquad d_1=Qm,\quad d_2=Rn.
\tag{162.T28}
\]

Because \(d_1\) is odd, only odd \(\rho,\kappa,Q\) survive, and
\(\chi_4(Qm)=\chi_4(Q)\chi_4(m)\).  The variable \(\tau\), the factor
\(R\), and hence \(d_2\), may be even.  The fixed opened sum has the
literal conditions

\[
 QRmn\asymp L^2,\qquad
 Rn\le Qm\le4Rn,\qquad
 m\asymp L/Q,\quad n\asymp L/R,
\tag{162.T29}
\]

and every profile in (162.T1) is evaluated at \((Qm,Rn)\), not at
\((m,n)\).  In particular, the cone, shell, \(W\)-ratio, \(H\)-profile,
floors, endpoints, and zero extension remain coupled.  Replacing (162.T27)
by a cost-one tensor factorization is not an identity.

The character-leg saddle must be rescaled as well.  For
\(r=k-\sigma/4\), put \(s=4r=4k-\sigma\).  Poisson in \(m\), with
\(d_2=Rn\) fixed, has

\[
 m_0=\frac{XQd_2}{4r^2}=\frac{4XQd_2}{s^2},\qquad
 J\sqrt{Qm_0d_2}-rm_0=\frac{XQd_2}{s},
 \qquad s\asymp JQ,\quad s\ {\rm odd},
\tag{162.T29a}
\]

and stationary scale

\[
 \left(\frac{XQd_2}{2r^3}\right)^{1/2}
 \asymp \frac1Q\sqrt{\frac LJ}.
\tag{162.T29b}
\]

Thus the exact reciprocal phase is \(e(XQd_2/s)\), and the opened
character is the fixed factor \(\chi_4(Q)\) times the transferred odd-dual
sign \(\chi_4(s)\).  Similarly, Poisson in the uncharactered \(n\)-leg has

\[
 n_0=\frac{XRd_1}{4\ell^2},\qquad
 J\sqrt{Rn_0d_1}-\ell n_0=\frac{XRd_1}{4\ell},
 \qquad \ell\asymp JR,qquad
 W\!\left(\sqrt{\frac{q_Xd_1}{4Rn_0}}\right)
 =W\!\left(\frac{\ell}{yR}\right).
\tag{162.T29c}
\]

At principal stationary level these two Legendre transforms are
involutive: dualizing the reciprocal principal carrier restores the
square-root carrier with the reciprocal Jacobian.  This does not include
hard endpoints, nonstationary ranges, or the opening sum, so it supplies no
estimate by itself.

### 3.3 Rank-one geometry and the dual product collar

For \(f(x,z)=J\sqrt{xz}\),

\[
 \operatorname{Hess}f=\frac J4
 \begin{pmatrix}
 -\sqrt z\,x^{-3/2}&(xz)^{-1/2}\\
 (xz)^{-1/2}&-\sqrt x\,z^{-3/2}
 \end{pmatrix},
 \qquad \det\operatorname{Hess}f=0,
\tag{162.T30}
\]

and the radial vector \((x,z)\) is null.  After two-variable Poisson in a
fixed opened \((m,n)\)-sum, the stationary equations are

\[
 r=\frac J2\sqrt{\frac{QRn}{m}},\qquad
 \ell=\frac J2\sqrt{\frac{QRm}{n}},
\tag{162.T31}
\]

so

\[
 s\ell=XQR,\qquad
 s=4r\asymp QJ,\quad\ell\asymp RJ.
\tag{162.T32}
\]

This is a one-dimensional stationary locus.  To derive the collar without
dividing by the zero Hessian determinant, first take \(Q=R=1\) and use

\[
 x=tu,\qquad z=t/u,\qquad dx\,dz=\frac{2t}{u}\,dt\,du.
\tag{162.T33}
\]

The cone has \(u\in[1,2]\), \(t\asymp L\), and a dual integral has phase

\[
 tG(u),\qquad G(u)=J-ru-\ell/u.
\tag{162.T34}
\]

The transverse critical point is \(u_0=\sqrt{\ell/r}\), with

\[
 G(u_0)=J-2\sqrt{r\ell},\qquad |G''(u_0)|\asymp J.
\tag{162.T35}
\]

The radial integral has length \(L\); hence the non-negligible interior
window is

\[
 |2\sqrt{r\ell}-J|\ll L^{-1}
 \quad\Longleftrightarrow\quad
 |r\ell-X/4|\ll J/L.
\tag{162.T36}
\]

With \(q=4r\), this is

\[
 |q\ell-X|\ll J/L.
\tag{162.T37}
\]

Because \(q\ell\) is an integer and \(q,\ell\asymp J\), the divisor bound
gives the rigorous smooth-collar count

\[
 \#\{(q,\ell)\text{ in (162.T37)}\}
 \ll (J/L+1)X^\varepsilon.
\tag{162.T38}
\]

Indeed, there are \(O(J/L+1)\) possible integers in the product window and
at most \(\tau(n)\ll_\varepsilon n^\varepsilon\) admissible factorizations
of each.  The odd residue restriction on \(q\) only reduces this count.

At a collar pair, the \(t\)-integration costs \(L\), transverse stationary
phase costs \((LJ)^{-1/2}\), and the Jacobian in (162.T33) costs \(L\).
Thus

\[
 |I_{q,\ell}|\ll L^{3/2}J^{-1/2}.
\tag{162.T39}
\]

For a fixed opening, \(\sqrt{mn}\asymp L/\sqrt{QR}\).  The same
calculation gives

\[
 |s\ell-XQR|\ll \frac{JQR}{L},
\tag{162.T40}
\]

\[
 \#\{(s,\ell)\}\ll
 \left(\frac{JQR}{L}+1\right)(XQR)^\varepsilon,
\qquad
 |I_{s,\ell}|\ll\frac{L^{3/2}}{QR\sqrt J}.
\tag{162.T41}
\]

Their product is again \(\sqrt{JL}\,X^\varepsilon\), independently of
the rescaling.  This is only a positive smooth-interior capacity.  It is
not a physical upper bound after summing the Möbius triples, and the hard
radial and cone boundaries create separate Fourier boundary pieces rather
than rapid-decay errors.  Consequently (162.T38)--(162.T41) prove neither
a signed saving nor a lower bound.

### 3.4 One-variable closure returns positive capacity

For fixed \(z\asymp L\), the original second derivative has size
\(|\partial_x^2J\sqrt{xz}|\asymp J/L^2\).  A rowwise second-derivative
estimate gives the numerical right side

\[
 \sqrt J+L/\sqrt J,
\tag{162.T42}
\]

which is no better than the trivial \(L\) in the allowed range
\(L\le J^{1/2}\).  The additive quarter shift changes the first derivative
but not (162.T42).

After (162.T20), a fixed-\(z\) reciprocal sum has phase \(Xz/q\),
\(q\asymp J\), and second derivative \(\asymp L/J\).  The analogous bound
is

\[
 \sqrt{JL}+\sqrt{J/L}.
\tag{162.T43}
\]

Multiplication by the stationary scale \(\sqrt{L/J}\) makes this
\(O(L+1)\) per \(z\)-row, and positive summation over \(z\) returns
\(L^{2+o(1)}\).  This is the one-variable self-return in power form.

### 3.5 Literal source maps and failures

**Bombieri--Iwaniec.**  A formal phase map is

\[
 K=1,\quad F=JL,\quad M=L/Q,\quad N=L/R,
 \quad u(m)=\sqrt{m/M},\quad v(n)=\sqrt{n/N},
\tag{162.T44}
\]

so that \(e(J\sqrt{QRmn})=e(Fu(m)v(n))\); notably \(F=JL\) is unchanged
by the opening.  The source coefficient must be \(a(m)b(n)\).  The physical
\(\mu^2(d_1d_2)W(\sqrt{q_Xd_1/(4d_2)})\), product shell, and hard cone are
joint.  Applying Lemma 2.4 after an arbitrary tensor decomposition charges
its absolute collision/projective norm; no bound for that norm follows
from (162.T1).  Opening (162.T27) does not remove the rescaled joint cone
and profiles.

**Kowalski--Robert--Wu.**  Grant all coefficient separation, endpoint,
and smoothing costs for free.  The literal source parameter map is

\[
 M=L/Q,\qquad N=L/R,\qquad
 \alpha=\beta=\tfrac12,\qquad F=JL.
\tag{162.T45}
\]

Substitution in (162.T9), before the unpaid opening sum, gives

\[
 J^{1/8}L^{13/8}(QR)^{-3/4}
 +L^{3/2}Q^{-1/2}R^{-1}
 +L^{7/4}Q^{-1}R^{-3/4}
 +J^{-1/2}L^{3/2}(QR)^{-1}.
\tag{162.T45a}
\]

The \(Q=R=1\) opening is exactly (162.T5).  In particular its source
right side divided by the target contains

\[
 (JL)^{1/8}\quad\text{and}\quad L^{1/4}.
\tag{162.T46}
\]

Since \(J\ge L^2\), even the first factor is at least \(L^{3/8}\).
Taking the better of (162.T5) and triviality still does not certify (162.T3).
The decay in (162.T45a) cannot be summed over the overlapping Möbius
openings for free, and does not remove the unsieved opening.  Restoring the
actual coefficient can only require an additional theorem; it cannot
improve the printed source bound by declaration.

**Robert--Sargos.**  Again grant cost-one separation.  The exact map is

\[
 H_0=L/Q,\quad M_0=L/R,\quad N_0=1,\quad
 \alpha=\beta=\tfrac12,\quad\gamma=1,\quad \Xi=JL/2.
\tag{162.T47}
\]

The value \(n=2\) is the sole integer in \(1<n\le2\), so \(\Xi=JL/2\)
matches \(e(J\sqrt{QRhm})\) exactly after the normalizations in
(162.T10).  Formula (162.T10) restores

\[
 J^{1/4}L^{3/2}Q^{-3/4}R^{-1/2}
 +L^{7/4}Q^{-3/4}R^{-1}
 +L^{3/2}Q^{-1}R^{-1/2}
 +J^{-1/2}L^{3/2}(QR)^{-1}.
\tag{162.T48}
\]

At \(Q=R=1\), its first term is at least \(L^2\) because \(J\ge L^2\).
The opening decay is not a cost-free aggregate estimate.  Moreover the
physical coefficient is not of the form \(a(h,n)b(m)\).

**Incomplete Kloosterman sums.**  The character-Poisson variable map is

\[
 s=4k-\sigma\asymp JQ,\qquad d_2\asymp L,\qquad
 e(XQd_2/s),\qquad X=J^2\in\mathbb R_{>0}.
\tag{162.T49}
\]

DFI Lemma 8 instead has one fixed integral modulus \(c\), an interval
variable \(x\), and phase \(e((a\overline x+bx)/c)\) with integral
parameters.  In (162.T49), \(s\) is the varying denominator; there is no
fixed modulus, no modular inverse, and \(XQd_2\) need not be integral.
Therefore \((U,k,c,a,b)\) has no literal physical substitution.

**Bilinear Kloosterman fractions.**  DFI, Bettin--Chandee, and the 2026
Dong--Robles--Zeindler theorem all retain the modular phase
\(e(a\overline m/(bn))\).  For one fixed integral \(X\), the only formal
degenerate representation of (162.T49) is

\[
 m=1,\qquad n=s\asymp JQ,\qquad
 a=XQd_2\asymp XQL=J^2QL,
 \qquad b=1.
\tag{162.T50}
\]

It fails for arbitrary real \(X\); for DFI it also has an \(a\) that changes
with every \(d_2\).  Bettin--Chandee can formally average \(a=d_2\) only
when \(X\) is integral, with

\[
 M=1,\quad N\asymp JQ,\quad A\asymp L,\quad\vartheta=XQ=J^2Q,
 \quad 1+\frac{|\vartheta|A}{MN}\asymp JL.
\tag{162.T51}
\]

The large-parameter factor in (162.T15) is then \(\asymp(JL)^{1/2}\),
before the theorem's other positive powers and before the physical
stationary amplitude is restored.  Crucially, this adverse factor is
independent of \(Q,R\).  Its coefficient
\(\alpha_1\beta_s\nu_{d_2}\) is also separated, whereas the actual dual
amplitude couples \(s,d_2,Q,R\) and every Möbius opening.  Theorem 2's Jacobi
symbol \((m/n)\) is not the fixed \(\chi_4(d_1)\); placing \(\chi_4\) in
an arbitrary coefficient gives no extra source saving.  The 2026 theorem's
removal of a temporary squarefree-support assumption does not change any
of these phase, integrality, or separation failures.

The table below records the complete \(L,J,H,X\) ledger.

| Route | Literal source parameters | Restored capacity or first no-match |
|---|---|---|
| character Poisson in \(d_1=Qm\) | \(s=4k-\sigma\asymp JQ\), \(d_2\asymp L\) | phase \(e(XQd_2/s)\), character becomes \(\chi_4(Q)\chi_4(s)\); rowwise closure returns positive capacity |
| Poisson in \(d_2=Rn\) | \(\ell\asymp JR\), \(d_1\asymp L\) | scaled principal self-return (162.T29c); arithmetic opening and all boundary owners remain |
| two-variable Poisson | \(q,\ell\asymp J\), \(|q\ell-X|\ll J/L\) | positive smooth collar \(\sqrt{JL}=L^{3/2}(H/L)\) |
| fixed Möbius opening | \(s\asymp QJ\), \(\ell\asymp RJ\), \(|s\ell-XQR|\ll QRJ/L\) | count and saddle rescale inversely, again \(\sqrt{JL}\); opening sum unpaid |
| KRW Proposition 5 | \(F=JL,\ M=L/Q,N=L/R,\ \alpha=\beta=1/2\) | (162.T45a); \(Q=R=1\) is (162.T5), not target-sized even with cost-one separation |
| Robert--Sargos Theorem 1 | \(H_0=L/Q,M_0=L/R,N_0=1,\Xi=JL/2\) | (162.T48); \(Q=R=1\) is at least trivial at \(J\ge L^2\) |
| DFI/BC/DRZ Kloosterman fractions | formal \(M=1,N=JQ,a=XQd_2\), or (162.T51) | ordinary-real reciprocal has no modular-inverse match; separated coefficient; adverse \(JL\) factor survives scaling |

## 4. First doubtful or unproved step

The earliest literal analytic seam is not a stationary-phase calculation.
It is the passage from the rough physical indicator to a Poisson-legal
amplitude.  The exact admissible passage is (162.T27)--(162.T29); after it,
the first unproved step is a signed estimate for the **aggregate** of all
Möbius-weighted, rescaled dual collars, with the two residue classes in
(162.T21), hard cone and shell boundaries, profiles, floors, stars, and
nonstationary pieces still coupled.

Equivalently, a continuation must prove cancellation in a family of the
schematic but coefficient-literal form

\[
 \sum_{\rho,\tau,\kappa}\mu(\rho)\mu(\tau)\mu(\kappa)
 \sum_{\substack{s,\ell\\
 |s\ell-XQR|\ll JQR/L}}
 \chi_4(Q)\chi_4(s)\,\mathcal A_{\rho,\tau,\kappa}(s,\ell),
\tag{162.T52}
\]

where \(\mathcal A\) is the actual stationary-plus-boundary amplitude, not
an arbitrary bounded diagnostic.  It must save the residual factor in
(162.T4), and globally the original \(L^{1/2-o(1)}\) gap, before any
positive norm.

For the direct product-phase sources, the first hypothesis failure is the
unproved cost-controlled separation of the joint physical coefficient; even
granting that false convenience, (162.T5) and (162.T48) fail by restored
powers.  For every Kloosterman proposal, the still earlier failure is the
replacement of the ordinary real reciprocal (162.T49) by a modular inverse
with integral numerator and fixed modulus.  No audited source proves
(162.T52), and none proves that its physical value is large.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_t1_coefficient_and_orientation` | **Pass.** Equation (162.T1) is retained in its displayed orientation; no \(d_1\leftrightarrow d_2\) symmetrization is used. |
| `squarefree_coprime_even_d2_branch` | **Pass.** Equations (162.T6), (162.T27)--(162.T29) are exact; \(Q\) is odd while \(R,d_2\) may be even. |
| `chi4_preserved_before_positive_norms` | **Pass.** The two signs remain in (162.T19); (162.T21) identifies the exact dual \(\chi_4(q)\).  Every later absolute ledger is explicitly labelled a route capacity. |
| `product_phase_rank_one_hessian` | **Pass.** Equation (162.T30) has determinant zero and radial null vector. |
| `one_variable_character_poisson_self_return` | **Pass as an obstruction.** Equations (162.T20)--(162.T26) and (162.T29a)--(162.T29c) give the quarter-shift reciprocal phase, its exact \(Q,R\) scaling, and principal-level involution.  No target is inferred. |
| `two_variable_dual_hyperbola` | **Pass.** Equations (162.T31)--(162.T32) give the exact rescaled stationary product. |
| `dual_product_collar_width_and_mass` | **Pass for the smooth hostile model.** Equations (162.T36)--(162.T41) prove the collar width, divisor count, per-pair scale, and \(\sqrt{JL}\) positive capacity.  A complete physical transform remains open. |
| `mobius_opening_and_rescaled_support_cost` | **Pass as exact algebra; aggregate bound open.** The lcm parametrization handles overlaps and retains all rescaled profiles.  No free summation over openings is claimed. |
| `hard_cone_profiles_floors_endpoints` | **Retained, not smoothed away.** They are explicit in (162.T1), (162.T29), and the caveats after (162.T26), (162.T41).  None of the source substitutions prices them literally. |
| `missing_L_half_power` | **Unpaid.** Original positive capacity is \(L^{2+o(1)}\); the best positive Poisson/trivial ledger is (162.T4), and the printed monomial cards leave fixed positive powers in (162.T46), (162.T48). |
| `source_theorem_literal_match` | **Fail at the target.** Exact cards and maps are in Sections 2 and 3.  The real-monomial sources require separation and fail in power even when it is granted; the Kloosterman sources have the wrong phase and arithmetic parameters. |
| `physical_coefficient_vs_diagnostic` | **Pass.** Cost-one separation and smooth collar models are counterfactual hostile controls only.  No density, lower energy, sign alignment, or lower bound for (162.T1) is asserted. |
| `remaining_few_point_and_downstream_scope` | **Pass.** Nothing here controls \(L\ll D\ll L^2\), \(t\ll\sqrt L\), the remaining few-point channels, full hard TOP, M9--M2, M9, either bridge, or any global exponent. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

The internal artifacts used were exactly the assigned brief and its permitted
context:

1. `protocol.md`;
2. the active Round-162 entries of `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `strategy/round162_m2_hard_top_t1_close_factor_strategy.md`;
5. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/barrier_packet.md`;
6. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/candidates/conductor_round162_t1_poisson_seed.md`;
7. `proofs/kernels/m9_m2_hard_top_radical_long_channel_collision_common_test_obstruction.md`;
8. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reports/square_root_spacing_source_hostile_audit.md`;
9. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reviews/source_power_seam_review.md`;
10. `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/conductor_round137_product_fibre_adjudication.md`.

The external primary sources were exactly:

1. Bombieri--Iwaniec, Lemma 2.4:
   <https://www.numdam.org/item/ASNSP_1986_4_13_3_449_0.pdf>;
2. Kowalski--Robert--Wu, Proposition 5:
   <https://ems.press/content/serial-article-files/38194?nt=1>;
3. Robert--Sargos, Theorem 1:
   <https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf>;
4. Duke--Friedlander--Iwaniec, Theorems 1--2 and Lemma 8:
   <https://www.math.ucla.edu/~wdduke/preprints/bilinear.pdf>;
5. Bettin--Chandee, Theorems 1--2:
   <https://arxiv.org/html/1502.00769v1>;
6. Dong--Robles--Zeindler, arXiv:2601.00292v1, Theorem 1.6:
   <https://arxiv.org/abs/2601.00292>.

No Round-162 sibling report, synthesis, candidate other than the assigned
conductor seed, validation file, proof draft, or graph mutation was read or
written.

## 7. Recommended state effect

**Recommend `promote` only after conductor seam review, under the terminal
label `hard_top_t1_close_factor_bilinear_no_go`, the following narrowly
scoped statement:**

> Exact character Poisson transfers \(\chi_4\) to odd dual residue classes;
> exact two-variable stationary geometry is a rank-one product hyperbola;
> after every fixed exact Möbius opening, the smooth positive dual collar has
> \(\sqrt{JL}\) capacity and does not certify the target away from
> \(L\asymp H\).  The audited separable monomial theorems fail after literal
> power restoration even with free coefficient separation, and the audited
> Kloosterman-fraction/incomplete-Kloosterman theorems have no literal match
> to the arbitrary-real ordinary reciprocal phase and physical joint
> coefficient.

Retain (162.T3) as open.  Retain as the first required new input a signed,
coefficient-sensitive estimate for (162.T52), or an equivalent theorem that
acts before every positive norm and fails on coefficient-uniform
phase-aligned diagnostics.  Do not infer a physical lower bound, a complete
\(t=1\) sector, any result for the remaining few-point channels, or any
downstream owner or exponent.
