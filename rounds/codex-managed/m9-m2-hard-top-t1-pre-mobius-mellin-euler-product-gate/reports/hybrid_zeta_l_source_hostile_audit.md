# Round 168 hostile primary-source audit: hybrid \(\zeta\)-\(L\) Mellin route

Audit date: 2026-08-26.  Terminal scope: the proposed pre-Mobius,
two-variable Mellin--Euler mechanism for the complete literal \(t=1\)
scalar only.

## 1. Result

### Audited-source nonlinear-weight no-go

Let \(J=\sqrt X\), \(1\ll L\ll H\leq J^{1/2}\), and let
\(\mathcal A_{L,X}(d_1,d_2)\) be the complete literal bounded amplitude
specified in (168.F1).  The arithmetic Dirichlet series does have the
claimed exact factorization

\[
 D(s_1,s_2)=L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2),
\]

where \(G\) is holomorphic and given by an absolutely convergent Euler
product whenever \(\Re s_1,\Re s_2>1/2\).  A contour shift from the
initial half-planes of absolute convergence to
\(\Re s_1=\Re s_2=1/2+\eta\) crosses the simple pole of
\(\zeta(s_2)\) at \(s_2=1\); the residue is explicit and is not forced
to vanish.

This algebra does **not** supply (168.F2).  In radial/angular variables,
the smooth bulk of a candidate Mellin transform on those shifted lines
has size

\[
 L^{2\eta}\sqrt{L/J}
\]

on a radial-frequency band of length \(T\asymp JL\), centred at
\(t_1+t_2\asymp-JL\).  Even if one grants Lindelof-size pointwise bounds
for both \(\zeta\) and \(L(s,\chi_4)\), taking absolute values before the
\(t_1+t_2\) integration costs

\[
 L^{2\eta}\sqrt{L/J}\,T^{1+\varepsilon}
   =L^{2\eta}\sqrt J\,L^{3/2}T^\varepsilon.
\]

The same \(T^{1+\varepsilon}\) cost results from a fixed-angular-frequency
mean square followed by Cauchy--Schwarz.  Thus the ideal pointwise-
Lindelof insertion and every audited absolute-moment insertion lose
\(\sqrt J\), before the angular tail is paid.  None of the primary
theorems audited below estimates the
actual signed, parameter-dependent, two-frequency weight

\[
 \widehat{\mathcal B}_{L,X}(s_1,s_2)
 \zeta(s_2)L(s_1,\chi_4)G(s_1,s_2)
\]

without first replacing its cancellation by a pointwise absolute value
or a positive moment.

The \(\zeta\)-pole is not, by itself, the first power obstruction.  At
\(t_2=0\), radial stationarity forces \(|t_1|\asymp JL\), hence also a
large angular frequency.  For a parameter-uniform bounded-variation
angular bulk this gives a factor \((JL)^{-1}\), making that bulk residue
target-safe even under convexity.  This is conditional on a lawful BV
realization: point-mass/Stieltjes endpoint corrections are not covered by
that decay and must be estimated separately.

Accordingly, the narrow conclusion is
`t1_mellin_euler_interface_no_go`: the exact primary inputs audited as of
2026-08-26 do not license the complete literal target through this route.
This is not a claim that no future bespoke signed transform theorem can
work, and it is not a lower bound for \(\mathcal S_{L,1}\).

## 2. Exact statement and hypotheses

### 2.1 Exact project interface

Initially for \(\Re s_1,\Re s_2>1\),

\[
 D(s_1,s_2)=
 \sum_{\substack{d_1,d_2\geq1\\d_1\ \mathrm{odd}\\
 d_1,d_2\ \mathrm{squarefree}\\(d_1,d_2)=1}}
 \frac{\chi_4(d_1)}{d_1^{s_1}d_2^{s_2}}.
\]

Writing \(x_p=\chi_4(p)p^{-s_1}\) and \(y_p=p^{-s_2}\), its local
factors are

\[
 D_2=1+y_2,
 \qquad D_p=1+x_p+y_p\quad(p\text{ odd}).
\]

Consequently

\[
 G_2=1-2^{-2s_2},
 \qquad
 G_p=(1+x_p+y_p)(1-x_p)(1-y_p)\quad(p\text{ odd}),
\]

and

\[
 G_p=1-x_p^2-x_py_p-y_p^2+x_p^2y_p+x_py_p^2.
\tag{2.1}
\]

For any \(\eta>0\), the product is locally uniformly absolutely
convergent on \(\Re s_i\geq1/2+\eta\) and
\(G(s_1,s_2)\ll\eta^{-O(1)}\) there.  It can have zeros; no zero-free
claim is needed.  It has no poles in this region.  The factorization by
itself gives no continuation across either boundary
\(\Re s_i=1/2\).

For an exact compactly supported interpolation
\(\mathcal B_{L,X}(x,y)\), use the convention

\[
 \widehat{\mathcal B}_{L,X}(s_1,s_2)
 =\int_0^\infty\!\int_0^\infty
 \mathcal B_{L,X}(x,y)x^{s_1-1}y^{s_2-1}\,dx\,dy.
\]

If Mellin inversion reproduces every literal lattice value, then on
initial lines

\[
 \mathcal S_{L,1}=\frac1{(2\pi i)^2}
 \iint \widehat{\mathcal B}_{L,X}(s_1,s_2)
 L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2)\,ds_2\,ds_1.
\tag{2.2}
\]

Moving \(s_2\) to \(1/2+\eta\), and then moving the entire remainder in
\(s_1\) to the same line, gives

\[
 \mathcal S_{L,1}=R_\zeta+\frac1{(2\pi i)^2}
 \iint_{\Re s_i=1/2+\eta}
 \widehat{\mathcal B}_{L,X}(s_1,s_2)
 L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2)\,ds_2\,ds_1,
\tag{2.3}
\]

and

\[
 R_\zeta=\frac1{2\pi i}
 \int_{\Re s=1/2+\eta}
 \widehat{\mathcal B}_{L,X}(s,1)L(s,\chi_4)G(s,1)\,ds.
\tag{2.4}
\]

No other pole is crossed inside the proven \(G\)-region:
\(L(s,\chi_4)\) is entire, and zeros of \(G\) or \(\zeta\) are not
singularities.

### 2.2 Exact primary-source cards

#### A. Topacogullari: same-height pointwise bounds, moments, and AFE

Berke Topacogullari, *The fourth moment of individual Dirichlet
L-functions on the critical line*, **Math. Z. 298** (2021), 577--624,
version of record published online 22 September 2020,
[DOI and official text](https://doi.org/10.1007/s00209-020-02610-9).
Throughout the paper \(\chi_i\pmod {q_i}\) are primitive and

\[
 L_{\chi_1,\chi_2}(s)=L(s,\chi_1)L(s,\chi_2)
 =\sum_{n\geq1}\frac{\tau_{\chi_1,\chi_2}(n)}{n^s},
 \quad
 \tau_{\chi_1,\chi_2}(n)=\sum_{d\mid n}\chi_1(d)\chi_2(n/d).
\]

- **Theorem 2.1.**  For \(\varepsilon>0\), \(0\leq\sigma\leq1\),
  and \(|\sigma+it-1|>\varepsilon\),
  \[
   L_{\chi_1,\chi_2}(\sigma+it)
   \ll (q_1q_2)^{3(1-\sigma)/8+\varepsilon}
        (|t|+1)^{3(1-\sigma)/4+\varepsilon}.
  \]
  With the principal primitive character of conductor \(1\) and
  \(\chi_4\) of conductor \(4\), this is a common-height bound for
  \(\zeta(s)L(s,\chi_4)\); at \(\sigma=1/2\) it costs
  \(t^{3/8+\varepsilon}\).  First literal failure: the project has
  independent heights \(t_1,t_2\), and even the common-height
  specialization is too large after integration over length \(JL\).

- **Theorem 2.2.**  For \(\varepsilon>0\), \(0\leq\sigma\leq1\), and
  \(q_1,q_2\leq T\),
  \[
   \int_1^T|L_{\chi_1,\chi_2}(\sigma+it)|\,dt
   \ll T^{1+\varepsilon}
     +(q_1q_2)^{1/2-\sigma}T^{2-2\sigma+\varepsilon}.
  \]
  At fixed conductors and \(\sigma=1/2+\eta\), this is
  \(T^{1+\varepsilon}\).  Absolute values are inside the integral and
  the two factors have a common height.  It neither sees the phase of
  \(\widehat{\mathcal B}\) nor gains the required \(T^{-1/2}\)-type
  cancellation.

- **Theorem 1.5.**  If \(K\) is quadratic of discriminant \(D\), then,
  for \(T\geq1\),
  \[
   \int_1^T|\zeta_K(1/2+it)|^2dt
   =\int_1^T P_K(\log t)dt
   +O\!\left(|D|^{5/4-3\theta/2}T^{1/2+\theta+\varepsilon}
             +|D|^{2/3}T^{2/3+\varepsilon}\right),
  \]
  where \(P_K\) is quadratic and \(\theta=7/64\) is admissible.
  For \(K=\mathbb Q(i)\), \(D=-4\) and
  \(\zeta_K(s)=\zeta(s)L(s,\chi_4)\).  Theorem 1.6 permits a fixed
  smooth compactly supported **complex** weight \(w(t/T)\), removes the
  \(T^{2/3+\varepsilon}\) error, and makes the implicit constant depend
  on \(w\).  Formal permission for complex \(w\) is not a uniform
  oscillatory-weight theorem: the integrand remains
  \(|\zeta_K|^2\), it is one-dimensional and same-height, and the source
  gives no seminorm dependence for an \((L,J,v)\)-dependent weight.

- **Theorem 2.7.**  Let \(\varepsilon>0\), let smooth
  \(V:(0,\infty)\to[0,\infty)\) satisfy
  \(V(\xi)+V(\xi^{-1})=1\), and let
  \(s=\sigma+it\), \(x,y\geq1\) satisfy
  \(1/2\leq\sigma\leq1\), \(q_1,q_2\leq t\), and
  \(4\pi^2xy=q_1q_2t^2\).  Then
  \[
  \begin{aligned}
   L_{\chi_1,\chi_2}(s)
   ={}&\sum_{n\geq1}\frac{\tau_{\chi_1,\chi_2}(n)}{n^s}V(n/x)\\
     &+\alpha_{\chi_1,\chi_2}(s)
       \sum_{n\geq1}\frac{\tau_{\overline\chi_1,\overline\chi_2}(n)}
       {n^{1-s}}V(n/y)+R_{\chi_1,\chi_2}(s;x,y),
  \end{aligned}
  \]
  with
  \[
   R\ll(q_1q_2)^{3(1-\sigma)/8}
        t^{-(1+3\sigma)/4+\varepsilon}.
  \]
  If \(T\gg\max(q_1,q_2)\), its balanced critical-line remainder also
  satisfies
  \[
   \int_{T/2}^T
   \left|R\!\left(\tfrac12+it;
      \tfrac{t\sqrt{q_1q_2}}{2\pi},
      \tfrac{t\sqrt{q_1q_2}}{2\pi}\right)\right|dt
   \ll T^\varepsilon.
  \]
  For \((q_1,q_2)=(1,4)\), balanced lengths are
  \(x=y=t/\pi\asymp JL\).  First literal failure: the theorem requires
  one common \(s\), whereas (2.3) has independent \(s_1,s_2\).  Even on
  the diagonal it returns the divisor convolution
  \(\tau_{1,\chi_4}\), not the original two-leg squarefree/coprime
  coefficient class; the factor \(G\), external hard transform, and
  endpoint corrections remain outside the theorem.

#### B. Bourgain: pointwise \(\zeta\) benchmark

Jean Bourgain, *Decoupling, exponential sums and the Riemann zeta
function*, **J. Amer. Math. Soc. 30** (2017), 205--224,
[DOI](https://doi.org/10.1090/jams/860).  The unnumbered displayed
consequence on p. 206 of the published article is

\[
 |\zeta(1/2+it)|\ll_\varepsilon t^{13/84+\varepsilon}.
\]

The [arXiv:1408.5794v2](https://arxiv.org/abs/1408.5794v2) abstract still
states the earlier \(53/342\); the journal's \(13/84\) is the
authoritative published form.  This theorem controls only the pointwise
absolute size of \(\zeta\), not \(L(s,\chi_4)\) or a signed long Mellin
integral.  More importantly, replacing \(13/84\) by the hypothetical
exponent \(0\) still leaves the \(\sqrt J\) loss in Section 3.4.

#### C. Ramana--Ramare: exact Perron formula retains a boundary correction

D. S. Ramana and O. Ramare, *Variant of the truncated Perron formula and
primes in polynomial sets*, **Int. J. Number Theory 16** (2020),
309--323, published 5 September 2019,
[author PDF](https://ramare-olivier.github.io/Maths/Perron-IJNT.pdf),
[DOI](https://doi.org/10.1142/S1793042120500165).

In Theorem 2.1 let \(F(s)=\sum_{n\geq1}a_nn^{-s}\) have finite
convergence abscissa \(\sigma_c\), put
\(\sigma_0=\max(0,\sigma_c)\), take \(\kappa>\sigma_0\), \(x\geq1\),
and let \(\phi,\widehat\phi\in L^1(\mathbb R)\) with \(\phi(0)=1\).
Then exactly

\[
\begin{aligned}
 \sum_{n\leq x}a_n
 ={}&\frac1{2\pi i}\int_{\kappa-i\infty}^{\kappa+i\infty}
 F(s)\phi\!\left(\frac{s-\kappa}{2\pi i}\right)\frac{x^s}{s}\,ds\\
 &+\int_{\mathbb R}\left(
 \sum_{n\leq x}a_n-e^{-\kappa u}\sum_{n\leq xe^u}a_n
 \right)\widehat\phi(u)\,du.
\end{aligned}
\tag{2.5}
\]

Corollary 2.2 adds an evenness and decay hypothesis on
\(\widehat\phi\), scales the contour kernel by \(T\), and leaves an
explicit signed local sum over
\(xe^{-u/T}<n\leq xe^{u/T}\), plus a quantified truncation error.  Thus
the cited exact theorem does not turn a hard endpoint into a pure contour:
the nearby-boundary correction is part of the identity.  No theorem in
this paper bounds the two-dimensional, profile- and star-dependent
corrections in (168.F1).

#### D. Durkan--Karak--Mahatab: current shifted Dedekind-zeta moment

Benjamin Durkan, Nilmoni Karak, and Kamalakshya Mahatab, *Sharp Upper
Bounds for Moments of Dedekind Zeta Functions*,
[arXiv:2606.27516v3](https://arxiv.org/abs/2606.27516v3), 27 July 2026.
Their Theorem 1.1 fixes number fields \(K_1,\ldots,K_r\) with common
Galois closure \(L\), assumes GRH for \(\zeta_L\), and takes a compact
\(\mathcal A\subset(0,\infty)^r\).  Uniformly for
\(\mathbf a\in\mathcal A\), \(|b_i|\leq T/2\), and sufficiently large
\(T\), it proves

\[
 \int_T^{2T}\prod_{j=1}^r
 \left|\zeta_{K_j}\!\left(\tfrac12+i(t+b_j)\right)\right|^{a_j}dt
 \ll T B(T,\mathbf b,\mathbf a),
\tag{2.6}
\]

where

\[
 B(T,\mathbf b,\mathbf a)=
 \prod_{i,j=1}^r\left|
 \mathcal Z_{ij}\!\left(1+\frac1{\log T}+i(b_i-b_j)\right)
 \right|^{a_ia_j/4},
\]

and \(\mathcal Z_{ij}\) is the stated double-coset product of Dedekind
zeta functions of fixed intermediate fields.  The first literal failure
is the unproved GRH hypothesis.  Even granting GRH, (2.6) concerns
positive powers of absolute values.  At \(v=0\), taking
\(K=\mathbb Q(i)\) controls an absolute moment of
\(\zeta(s)L(s,\chi_4)\), still with the natural factor \(T\).  At
\(v\neq0\), writing
\(L(s,\chi_4)=\zeta_{\mathbb Q(i)}(s)/\zeta(s)\) introduces a quotient
and a negative zeta power, which Theorem 1.1 does not permit.  The theorem
also has neither the factor \(G\) nor the signed nonlinear weight
\(\widehat{\mathcal B}\).

## 3. Proof or derivation

### 3.1 Euler factors and continuation actually obtained

Squarefreeness and coprimality allow, at each odd prime, exactly three
choices: the prime lies in neither leg, in the first leg, or in the second
leg.  This gives \(1+x_p+y_p\).  At \(p=2\), the odd-first-leg condition
forbids the first choice and gives \(1+y_2\).  Multiplication by the local
reciprocals of \(L(s_1,\chi_4)\zeta(s_2)\) yields (2.1), while

\[
 (1+y_2)(1-y_2)=1-y_2^2.
\]

On \(\Re s_i\geq1/2+\eta\),

\[
 |G_p-1|\ll p^{-2\Re s_1}+p^{-\Re s_1-\Re s_2}
                  +p^{-2\Re s_2}+p^{-3/2-3\eta},
\]

so \(\sum_p|G_p-1|<\infty\).  Local uniform convergence proves
holomorphy.  The logarithmic divergence as \(\eta\downarrow0\) costs at
most \(\eta^{-O(1)}\); choosing \(\eta\asymp1/\log X\) therefore costs
only a power of \(\log X\).  Nothing in this calculation moves a contour
through \(\Re s_i=1/2\).

### 3.2 The pole and its exact arithmetic residue

Since \(\operatorname{Res}_{s=1}\zeta(s)=1\), (2.4) is the exact crossed
residue.  Its coefficient series can be read off explicitly.  For odd
\(p\),

\[
 L_p(s,\chi_4)G_p(s,1)
 =(1-p^{-2})+(1-p^{-1})\chi_4(p)p^{-s},
\]

and the factor at \(2\) is \(1-2^{-2}\).  Hence, initially for
\(\Re s>1\),

\[
 L(s,\chi_4)G(s,1)
 =\frac1{\zeta(2)}
 \sum_{\substack{n\geq1\\n\ \mathrm{odd,\ squarefree}}}
 \frac{\chi_4(n)}{n^s}\prod_{p\mid n}(1+p^{-1})^{-1}.
\tag{3.1}
\]

Mellin inversion on the initial line, where the interchange is absolute,
therefore gives

\[
 R_\zeta=\frac1{\zeta(2)}
 \sum_{\substack{n\geq1\\n\ \mathrm{odd,\ squarefree}}}
 \chi_4(n)\prod_{p\mid n}(1+p^{-1})^{-1}
 \int_0^\infty\mathcal B_{L,X}(n,y)\,dy.
\tag{3.2}
\]

Equation (3.2) shows that there is no character identity forcing the
residue to vanish.  It does not assert that the residue is nonzero for
every possible amplitude.

### 3.3 Radial and angular transform geometry

Put

\[
 x=rw,\qquad y=r/w,\qquad dx\,dy=2r\,dr\,\frac{dw}{w},
\]

and set \(u=t_1+t_2\), \(v=t_1-t_2\).  The Mellin phase is

\[
 e(Jr)r^{iu}w^{iv}.
\]

The derivative of its radial phase is \(2\pi J+u/r\).  On \(r\asymp L\),
stationarity is therefore

\[
 u=-2\pi Jr\asymp-JL,
\]

and, because the radial shell has scale \(L\), the stationary band has
length \(T\asymp JL\).  On
\(\Re s_1=\Re s_2=1/2+\eta\), the radial amplitude is
\(r^{2\eta}\); one-dimensional stationary phase has curvature
\(\asymp J/L\) and gives the bulk scale

\[
 \widehat{\mathcal B}(s_1,s_2)
 \asymp_{\text{scale}}L^{2\eta}\sqrt{L/J}
\tag{3.3}
\]

when the stationary point lies in a smooth nonvanishing cell.  Here
``scale'' is not a lower bound and does not suppress profile-dependent
coefficients.

If the angular amplitude is BV in \(\log w\), integration by parts gives
\(O((1+|v|)^{-1})\).  A nonzero endpoint jump contributes an explicit
boundary term of order \(1/v\), so rapid decay cannot be assumed.  The
tail \(\int_1^Vdv/v\) is logarithmic even before any growth of the
L-functions is inserted.  A Stieltjes atom has no \(v\)-decay at all.
Thus a hard literal contour requires either proved endpoint vanishing,
cancellation retained across \(v\), or separate endpoint corrections.

### 3.4 Full-length power ledger and absolute-value placement

Fix a bounded \(v\)-cell, so that (3.3) is the relevant transform scale.
Even under the hypothetical bounds

\[
 |\zeta(1/2+\eta+it)|+|L(1/2+\eta+it,\chi_4)|\ll T^\varepsilon,
\]

triangle inequality over the entire \(u\)-band gives

\[
 L^{2\eta}\sqrt{L/J}\int_{|u+O(T)|\ll T}
 |\zeta(s_2)L(s_1,\chi_4)|\,du
 \ll L^{2\eta}\sqrt J\,L^{3/2}T^\varepsilon.
\tag{3.4}
\]

At \(v=0\), Topacogullari's Theorem 1.5 and Cauchy--Schwarz give the
same \(T\) (up to logarithms), not \(T^{1/2}\).  Theorem 2.2 states this
directly as an absolute first moment.  Theorem 2.1 used pointwise is
worse:

\[
 \sqrt{L/J}\,T^{1+3/8+\varepsilon}
 =J^{7/8}L^{15/8}T^\varepsilon.
\]

For fixed nonzero \(v\), the L-factors occur at shifted heights; none of
the cited unconditional theorems supplies a signed weighted estimate for
that slice.  Durkan--Karak--Mahatab supplies conditional positive moments,
but still begins with the natural \(T\) factor and does not represent the
quotient needed to isolate \(L(s_1,\chi_4)\).

The missing operation is cancellation between the nonlinear phase of
\(\widehat{\mathcal B}\) and the L-functions *before* absolute values.
Topacogullari's smooth Theorems 1.2, 1.4, and 1.6 do not provide it: their
weight is a fixed one-variable \(w(t/T)\), their integrands are absolute
squares, and their implicit constants are not quantified in the
parameter-dependent seminorms generated here.  Therefore no cited
mean-value theorem controls the signed nonlinear Mellin weight itself.

### 3.5 Why the zeta pole is large-frequency but not zero

On the residue line \(s_2=1\), \(t_2=0\).  Radial stationarity then forces
\(t_1\asymp-JL\), and the angular frequency is simultaneously
\(v=t_1\asymp-JL\).  Before angular decay, stationary phase on
\(\Re s_1=1/2+\eta\) gives

\[
 L^{1/2+\eta}\sqrt{L/J}.
\]

For a parameter-uniform BV angular bulk, the extra \((JL)^{-1}\) gives

\[
 |\widehat{\mathcal B}(1/2+\eta+it,1)|
 \ll L^\eta J^{-3/2}
 \qquad(|t|\asymp JL).
\tag{3.5}
\]

A standard fixed-conductor first moment then yields

\[
 R_{\zeta,\mathrm{bulk}}
 \ll L^{1+\eta}J^{-1/2}(JL)^\varepsilon.
\tag{3.6}
\]

Even using only the convexity bound
\(|L(1/2+\eta+it,\chi_4)|\ll t^{1/4+\varepsilon}\), which follows from
the Dirichlet series, functional equation, and the convexity principle,
(3.5) gives

\[
 R_{\zeta,\mathrm{bulk}}
 \ll L^{5/4+\eta}J^{-1/4}(JL)^\varepsilon,
\]

still below \(L^{3/2}X^\varepsilon\).  Thus large angular frequency can
suppress the ordinary BV bulk of the pole, although (3.2) proves there is
no automatic vanishing.  This conclusion does not cover literal
point-value corrections, Stieltjes atoms, or an angular variation growing
with \(L,J\).

### 3.6 Perron endpoints, AFE output, and the Round-162 collar

An ordinary Lebesgue Mellin transform is unchanged if a function is
altered at isolated endpoints.  Symmetric inversion at a jump returns an
averaged boundary value, not an arbitrary half-open convention.  Formula
(2.5) is an exact primary-source remedy only because it retains the local
partial-sum correction.  No cited result proves that the two-dimensional
correction created by the literal real centre, floors, profiles, stars,
cone edges, and zero extension is \(O(L^{3/2}X^\varepsilon)\).

Topacogullari's Theorem 2.7 can be applied to the common-height product
\(\zeta(s)L(s,\chi_4)\), with AFE length \(\asymp JL\), only on the
diagonal \(s_1=s_2\).  It does not transform (2.3), where the radial band
and angular variable make the heights independent.  Applying separate
AFEs simply opens two new Dirichlet variables while retaining \(G\) and
the hard external kernel.  No audited theorem identifies that output
with the Round-162 collar

\[
 s\ell=XQR,\qquad |s\ell-XQR|\ll QRJ/L,
\]

or proves that its \(\sqrt{JL}\) positive capacity has disappeared.
Therefore an exact AFE self-return is **not established**; the source
route fails earlier, and this report does not promote analogy to an exact
collar equivalence.

## 4. First doubtful or unproved step

The first step after the Euler algebra that is not proved for the literal
scalar is an exact interpolation/Mellin--Perron--Stieltjes identity with
parameter-uniform transform control and target-safe corrections for every
half-open endpoint, real centre, floor, star, profile transition, and zero
extension.  Ordinary Mellin inversion cannot encode isolated hard values,
and the exact Perron theorem explicitly retains nearby-boundary sums.

Even if that step and uniform BV bounds are granted, the first
**primary-source interface** failure is the signed hybrid estimate: none
of the audited theorems estimates the two-dimensional nonlinear weight in
(2.3), while every available absolute/second-moment insertion yields
(3.4) and loses \(\sqrt J\).  A bespoke theorem would have to state its
coefficient class, both height variables, full \(u\)-length \(JL\), hard
\(v\)-tail, dependence on weight seminorms, \(G\)-factor, residue, and
endpoint corrections.  No such conclusion is licensed by the cited
sources.

## 5. Required control tests and outcomes

| Control | Outcome | Exact finding |
|---|---|---|
| `exact_Euler_local_factors_including_p2` | PASS | \(D_2=1+2^{-s_2}\), \(G_2=1-2^{-2s_2}\); the first leg remains odd. |
| `G_absolute_convergence_and_singularities` | PASS only in the proved region | Absolute/local-uniform convergence for \(\Re s_i>1/2\); \(G\ll\eta^{-O(1)}\) on offset lines; no pole there and no licensed continuation across the boundary. |
| `hard_half_open_profile_BV_endpoints` | FAIL for the literal scalar | Ordinary Mellin ignores isolated endpoint values; exact Perron retains local corrections; uniform BV/seminorm bounds and all literal corrections are absent. |
| `zeta_pole_and_residue` | PASS algebraically; CONDITIONAL analytically | The only crossed pole is \(s_2=1\), with (3.1)--(3.2).  It is not forced to vanish.  Its ordinary BV bulk is target-safe by high angular frequency; endpoint atoms remain open. |
| `radial_angular_frequency_support` | PASS for the candidate bulk | \(u=t_1+t_2=-2\pi Jr\asymp-JL\), band length \(JL\); \(v=t_1-t_2\) is the angular frequency. |
| `full_transform_length_and_tail` | FAIL | The full radial length is \(JL\); a nonzero hard angular jump gives only \(1/|v|\), and no source owns the complete tail. |
| `no_absolute_hybrid_moment_inflation` | FAIL for the proposed source insertion | Even Lindelof plus triangle, or mean square plus Cauchy, gives \(\sqrt J L^{3/2+o(1)}\).  No audited theorem estimates the signed nonlinear weight. |
| `functional_equation_AFE_self_return` | FAIL / not reached | Theorem 2.7 is common-height with \(\tau_{1,\chi_4}\) and length \(JL\); separate AFEs leave a double kernel.  No exact self-return map is proved. |
| `round162_product_collar_comparison` | PASS as a scope check | The known collar and \(\sqrt{JL}\) capacity were compared; no equality with the Mellin/AFE output is asserted. |
| `arbitrary_real_centre_floors_and_stars` | FAIL | None of the primary theorems reproduces or bounds all such two-dimensional endpoint corrections. |
| `target_L_three_halves_power_ledger` | FAIL | The best absolute route is larger than the target by \(\sqrt J\), before the hard angular tail. |
| `primary_source_exact_hypotheses` | PASS | The theorem numbers, quantifiers, coefficient/field classes, weights, ranges, absolute-value placement, parameter maps, and first failed hypotheses are recorded above. |
| `downstream_scope_and_no_exponent_promotion` | PASS | No claim is made for other hard-TOP channels, BAL/UNBAL, M1, M9, bridges, the quarter theorem, or either exponent ledger. |
| `no_in_round_pivot` | PASS | No determinant, Fejer, or other-channel substitute was used. |

Research allocation was 100% analytical/algebraic and 0% numerical.

## 6. Dependencies and exact artifacts used

Only the generated task brief and its permitted local context were used:

- `protocol.md`;
- `state/active_campaign.yml`;
- `strategy/round168_m2_hard_top_t1_pre_mobius_mellin_euler_strategy.md`;
- `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/briefs/hybrid_zeta_l_source_hostile_audit.md`.

Primary-source web scope was searched through 2026-08-26 for exact
Dirichlet-product moments and AFE statements, pointwise zeta
subconvexity, exact/truncated Perron formulae, and current shifted
Dedekind-zeta moments.  The exact primary URLs used are the
Topacogullari DOI above, the Bourgain DOI and arXiv version above, the
Ramana--Ramare author PDF and DOI above, and Durkan--Karak--Mahatab
arXiv v3 above.  The negative literature conclusion is deliberately
limited to this dated audited source set; it is not a universal
nonexistence assertion.

## 7. Recommended state effect

**Recommended effect: retain.**  Retain (168.F2) as open and record the
narrow terminal label `t1_mellin_euler_interface_no_go` as source/strategy
evidence.  The exact Euler factors, \(G\)-region, residue identity, and
absolute-value power ledger are suitable for independent seam review, but
the complete literal target, residual target, any downstream parent, and
both exponent ledgers receive **no promotion**.  A future attempt should
proceed only with (i) a literal endpoint-lawful transform with quantified
BV/seminorm costs and (ii) a new signed two-frequency hybrid theorem that
beats the natural \(JL\) length before absolute values.
