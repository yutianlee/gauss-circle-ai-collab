# Round 169 hostile audit: signed spectral reciprocity and the moving product collar

## 1. Result: a narrow source-interface no-go

### Source-interface no-go lemma

Let

\[
 \mathcal I_\eta=\frac1{(2\pi)^2}\int_{\mathbb R^2}
 \widehat{\mathcal B}(\alpha+it_1,\alpha+it_2)
 L(\alpha+it_1,\chi_4)\zeta(\alpha+it_2)
 G(\alpha+it_1,\alpha+it_2)\,dt_1dt_2,
 \qquad \alpha=\tfrac12+\eta,
\]

be the exact Round-168 cardinal integral, with \(J=\sqrt X\),
\(H\asymp\sqrt J\), and \(1\ll L\ll H\).  In the primary-source set
audited below, there is no theorem that may be applied to deduce

\[
 \mathcal I_\eta\ll_\varepsilon L^{3/2}X^\varepsilon
\tag{1.1}
\]

after retaining all of the following simultaneously:

1. the signed two-variable coefficients \(g(a,b)\), including the
   two-adic factor;
2. two independent height variables and the two distinct GL(1) gamma
   quotients;
3. the complete literal cardinal-cell weight and its endpoint values;
4. every main, residual, continuous, holomorphic, Maass, and exceptional
   spectral term; and
5. the full dual lengths and outer normalizations.

The source-interface conclusion is made after granting the exact finite
double-Poisson transform supplied by a separate Round-169 conductor
candidate.  The first surviving imported-theorem seam is therefore the
conversion of that transform's moving product collar into a legal
shifted-convolution, Kloosterman, Kuznetsov, or reciprocity input while
preserving the signed outer aggregate.  No audited theorem supplies that
conversion.

For completeness, a derivation using only the bare functional equations
would still have to address the nonabsolute dual Dirichlet series on the
reflected lines.  That observation is an audit warning, not the
round-closing source obstruction now that the separate finite transform
is available.

The source no-go remains true after granting the exact double-Poisson
expression with moving collar

\[
 k\ell\approx XQR,\qquad |k\ell-XQR|\ll QRJ/L,
 \qquad \text{outer weight }\frac{g(Q,R)}{QR}.
\tag{1.2}
\]

The relation (1.2) is a multiplicative near-equality about two integer
variables and an arbitrary-real moving centre.  It is not a Kloosterman
sum, an additive shifted convolution, or a fixed-level automorphic
moment.  The audited Kuznetsov and Kloosterman theorems require exact
integral modular data and controlled smooth weights.  Their estimates
place an absolute value or a positive \(\ell^2\) norm after aggregation;
none preserves the literal parameter-dependent collar weight together
with the signed \(g(Q,R)/(QR)\) aggregate in a form that yields the
missing \(\sqrt J\).

Quantitatively, the favorable smooth/BV absolute placements remain

\[
 L^{2\eta}\sqrt J\,L^{3/2}X^\delta,
\tag{1.3}
\]

and the granted positive collar remains

\[
 \sqrt{JL}\,X^\varepsilon
 =L^{3/2}\left(\frac{\sqrt J}{L}\right)X^\varepsilon
 =L^{3/2}\left(\frac HL+O(L^{-1})\right)X^\varepsilon.
\tag{1.4}
\]

Thus the cited sources supply neither the structural \(\sqrt J\) gain
needed in (1.3) nor the factor \(L/\sqrt J\) needed in (1.4).  This is a
no-go for the *audited source placements*, not a lower bound for
\(\mathcal I_\eta\) and not a universal assertion that no new signed
two-height theorem can prove (1.1).

## 2. Exact statements and hypotheses

### 2.1 Exact arithmetic and functional-equation ledger

For odd primes put

\[
 x_p=\chi_4(p)p^{-s_1},\qquad y_p=p^{-s_2}.
\]

The accepted residual Euler factor is

\[
 G_p=1-x_p^2-y_p^2-x_py_p+x_p^2y_p+x_py_p^2,
\qquad G_2=1-2^{-2s_2}.
\tag{2.1}
\]

Consequently \(G(s_1,s_2)=\sum_{a,b}g(a,b)a^{-s_1}b^{-s_2}\) has the
following odd-prime local coefficient table:

| \((v_p(a),v_p(b))\) | \((0,0)\) | \((2,0)\) | \((0,2)\) | \((1,1)\) | \((2,1)\) | \((1,2)\) |
|---|---:|---:|---:|---:|---:|---:|
| \(g_p\) | \(1\) | \(-1\) | \(-1\) | \(-\chi_4(p)\) | \(1\) | \(\chi_4(p)\) |

Every other odd-prime exponent pair has coefficient zero.  At \(p=2\)
the only nonzero pairs are \((0,0)\), with coefficient \(1\), and
\((0,2)\), with coefficient \(-1\).  The coefficients are multiplicative
as a function of the pair \((a,b)\).  On
\(\Re s_1=\Re s_2=\alpha=1/2+\eta\),

\[
 \begin{aligned}
 A_\eta
 &:=\sum_{a,b\ge1}\frac{|g(a,b)|}{(ab)^\alpha}\\
 &=(1+2^{-2\alpha})
   \prod_{p\ {\mathrm{odd}}}(1+3p^{-2\alpha}+2p^{-3\alpha})
   \asymp \eta^{-3}\qquad(\eta\downarrow0).
 \end{aligned}
\tag{2.2}
\]

Indeed the quotient of the odd-prime product in (2.2) by
\(\prod_{p\ {\mathrm{odd}}}(1-p^{-2\alpha})^{-3}\) converges to a finite
positive limit.  Formula (2.2) licenses the coefficient expansion on the
original line, but taking this \(\ell^1\) norm before exposing a joint
phase is precisely the forbidden loss of the signed \(G\)-aggregate.

The completed functions and exact functional equations are

\[
 \Lambda_\zeta(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)
 =\Lambda_\zeta(1-s),
\tag{2.3}
\]

where \(\Lambda_\zeta\) is meromorphic with simple poles at \(s=0,1\),
and

\[
 \Lambda_{\chi_4}(s)=
 \left(\frac4\pi\right)^{(s+1)/2}
 \Gamma\!\left(\frac{s+1}{2}\right)L(s,\chi_4)
 =\Lambda_{\chi_4}(1-s).
\tag{2.4}
\]

Here \(\chi_4\) is primitive, real, odd, of conductor \(4\), its Gauss
sum is \(2i\), and its root number is
\(i^{-1}(2i)/\sqrt4=1\); (2.4) is entire.  In uncompleted form,

\[
 \begin{aligned}
 \zeta(s)&=\gamma_0(s)\zeta(1-s),&
 \gamma_0(s)&=\pi^{s-1/2}
  \frac{\Gamma((1-s)/2)}{\Gamma(s/2)},\\
 L(s,\chi_4)&=\gamma_1(s)L(1-s,\chi_4),&
 \gamma_1(s)&=\left(\frac4\pi\right)^{1/2-s}
  \frac{\Gamma(1-s/2)}{\Gamma((s+1)/2)}.
 \end{aligned}
\tag{2.5}
\]

Stirling's formula gives, uniformly away from bounded height,

\[
 |\gamma_j(\alpha+it)|\asymp_j(1+|t|)^{-\eta},
 \qquad j=0,1.
\tag{2.6}
\]

The reflection sends \(\alpha+it_j\) to
\(1-\alpha-it_j\).  Changing variables \(u_j=1-s_j\) reverses each
vertical orientation; the reversed endpoints cancel that sign in each
one-dimensional integral.  Functional equation alone crosses no
contour.  Any later displacement to a line where the dual Dirichlet
series converges must retain the completed meromorphic factors and all
residues or pole-zero cancellations generated by that displacement.

A balanced degree-one approximate functional equation at height
\(T_j\) has primal and dual lengths \(\asymp\sqrt{T_j}\).  Applying two
such equations independently produces four primal/dual combinations and
a coefficient grid of natural cardinality
\(\asymp\sqrt{T_1T_2}\), hence \(\asymp T\) when
\(T_1\asymp T_2\asymp T\).  It is not a free square-root shortening of
the two-factor problem.

The exact cardinal transform is a finite sum of \(O(L^2)\) unit-cell
transforms retaining the real centre, floors, starred endpoints,
half-open shell, cone edges, even second leg, profile transitions, zero
extension, and literal endpoint values.  The favorable recombined
smooth/BV model instead has radial length \(T\asymp JL\) and transform
scale

\[
 L^{2\eta}\sqrt{L/J}.
\tag{2.7}
\]

No imported theorem may substitute (2.7) for the exact cardinal weight
without proving an equality and pricing the relevant Sobolev or
derivative seminorms.

### 2.2 Shifted-convolution sources

**Blomer--Harcos.**  Theorem 1 of Valentin Blomer and Gergely Harcos,
*The spectral decomposition of shifted convolution sums*, Duke Math. J.
144 (2008), 321--339,
[arXiv:math/0703246v2](https://arxiv.org/html/math/0703246v2),
[DOI 10.1215/00127094-2008-038](https://doi.org/10.1215/00127094-2008-038),
fixes two cuspidal automorphic representations \(\pi_1,\pi_2\) of
\(\operatorname{PGL}_2(\mathbb Z)\backslash
\operatorname{PGL}_2(\mathbb R)\).  For integers \(a,b,c\ge0\), it
requires the norms

\[
 \|W\|_{A^d}=\sum_{j=0}^d
 \left(\int_{\mathbb R^\times}
 (|u|+|u|^{-1})^d|W^{(j)}(u)|^2\,d^\times u\right)^{1/2},
 \quad d=18+2a+2b+4c.
\]

For every fixed positive integer shift \(h\) and \(Y>0\), it proves

\[
 \sum_{m+n=h}\frac{\lambda_{\pi_1}(|m|)\lambda_{\pi_2}(|n|)}
 {\sqrt{|mn|}}W_1(m/Y)W_2(n/Y)
 =\int_{\tau\ne\tau_0}\frac{\lambda_\tau(h)}{\sqrt h}
 W_\tau(h/Y)\,d\tau,
\tag{2.8}
\]

where the full nontrivial spectrum consists of holomorphic and Maass
cusp representations and the Eisenstein continuum.  Its uniform bound
is

\[
 \int_{\tau\ne\tau_0}\widetilde\lambda_\tau^c
 \left|\left(y\frac d{dy}\right)^aW_\tau(y)\right|d\tau
 \ll C_{a,b,c}\min(y^{1/2-\epsilon},y^{1/2-b-\epsilon}),
\tag{2.9}
\]

with \(C_{a,b,c}\) polynomial in the input Laplace parameters and a sum
of products of the displayed high \(A^d\)-norms.  A negative-axis choice
of \(W_2\) treats \(m-n=h\).  The arbitrary-level remark treats
\(\ell_1m\pm\ell_2n=h\), but introduces complementary spectrum
\(0<\nu_\tau\le7/64\), a factor
\((\ell_1\ell_2)^{1/2+\epsilon}\), and a weakened region.

The project coefficients are not Hecke eigenvalues of two fixed
cuspidal GL(2) representations; (1.2) is not a fixed additive equation;
and no bound for the cardinal weight's required \(A^d\)-norms is
available.  Therefore neither (2.8) nor its level remark has a literal
parameter map.

**Blomer--Jana--Nelson.**  Theorem 3 of Valentin Blomer, Subhajit Jana,
and Paul D. Nelson, *Local integral transforms and global spectral
decomposition*, Geom. Funct. Anal. 35 (2025), 1051--1107,
[arXiv:2404.10692v2](https://arxiv.org/html/2404.10692v2),
[DOI 10.1007/s00039-025-00714-0](https://doi.org/10.1007/s00039-025-00714-0),
is built from an exact local gamma transform, but with restrictive input
data.  In its Theorem 1, \(\pi_1\) is
\(\vartheta_1\)-tempered, \(\pi_2\) is a
\(\vartheta_2\)-tempered principal series, and
\(W_i(a(\cdot))\in C_c^\infty(F^\times)\).  For a
\(\vartheta\)-tempered \(\pi\),
\(\vartheta_1+\vartheta_2+\vartheta<1/2\), it gives

\[
 \begin{aligned}
 h^\vee(\pi,y)=\int_{\Re\xi=\sigma}
 &\gamma(\tfrac12,\pi\otimes\xi)
 \gamma(1,\pi_1\otimes\bar\chi_2^{-1}\otimes\xi^{-1})\\
 &\times\int_{F^\times}h(yt,y(t-1))\xi^{-1}(t)
 \bar\chi_2((t-1)/t)\left|\frac t{t-1}\right|^{1/2}
 \frac{dt}{|t|}\,d\xi,
 \end{aligned}
\tag{2.10a}
\]

for \(\vartheta_1+\vartheta_2<\sigma<1/2-\vartheta\).  The forward
integrals converge absolutely.  Its inversion formula for
\(y_1\ne y_2\) has absolutely convergent inner and outer iterated
integrals but is explicitly *not* absolutely convergent as a double
integral.  Thus even this very general exact gamma transform does not
license unqualified interchange of the project coefficient, height, and
spectral integrations.

The global Theorem 3 then
fixes cuspidal PGL(2) representations \(\pi_1,\pi_2\) over a number
field \(F\), a finite set \(S\) containing every archimedean and
ramified place, assumes \(\pi_{2,\mathfrak p}\) principal series for
\(\mathfrak p\in S\), takes a nonzero *additive* shift
\(b\in\mathcal O_F[1/S]\), and requires
\(h\in C_c^\infty(F_S^\times\times F_S^\times)\).  It proves

\[
 \sum_{n_1-n_2=b}W_{\pi_1}^{(S)}(a(n_1))
 \overline{W_{\pi_2}^{(S)}(a(n_2))}h(n_1,n_2)
 =\int_{\widehat{[G]}^u_{{\rm gen},S}}
 W_\pi^{(S)}(a(b))c_\pi^{(S)}h^\vee(\pi_S,b_S)\,d\pi.
\tag{2.10}
\]

For \(F=\mathbb Q\), the spectrum contains holomorphic, Maass, and
continuous Eisenstein contributions.  Theorem 4 in the same paper gives
an exact second-moment identity

\[
 \int_{\eta\in\widehat{[A]}^u_S}
 \frac{L^{(S)}(\tfrac12,\pi_1\otimes\chi\eta^{-1})
 L^{(S)}(\tfrac12,\bar\pi_2\otimes\eta)}
 {\operatorname*{res}_{s=1}\zeta_F^{(S)}(s)}w(\eta,\chi)\,d\eta
 =\mathcal M+\int_{\widehat{[G]}^u_{{\rm gen},S}}
 L^{(S)}(\tfrac12,\sigma\otimes\chi)c_\sigma^{(S)}
 h_S^\sharp(\sigma,\chi)\,d\sigma,
\tag{2.11}
\]

where the mandatory main term is the sum of

\[
 \frac{L^{(S)}(1,\pi_1\otimes\bar\pi_2\otimes\chi)}
 {L^{(S)}(2,\chi^2)}\int h(z,z)\chi(z)d^\times z
\]

and

\[
 \frac{L^{(S)}(1,\pi_1\otimes\bar\pi_2\otimes\chi^{-1})}
 {L^{(S)}(2,\chi^{-2})}\int\mathcal J(h)(z,z)
 \chi^{-1}(z)d^\times z.
\]

At the real place, \(\eta\) is one unitary character parameter; the two
heights in (2.11) are coupled with opposite signs.  They are not two
independent variables.  The representations in (2.10)--(2.11) are
cuspidal GL(2) inputs, and the test function is compact-smooth.  The
theorems therefore do not accept \(L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2)\)
with the cardinal weight.

### 2.3 Kuznetsov, Kloosterman, and spectral-large-sieve sources

The normalization and full terms can be read directly in Alexandru
Pascadi, *Large sieve inequalities for exceptional Maass forms and the
greatest prime factor of \(n^2+1\)*, Forum Math. Pi 14 (2026), e8,
[arXiv:2404.04239v3](https://arxiv.org/html/2404.04239v3),
[DOI 10.1017/fmp.2026.10025](https://doi.org/10.1017/fmp.2026.10025),
which restates and refines J.-M. Deshouillers and H. Iwaniec,
*Kloosterman sums and Fourier coefficients of cusp forms*, Invent. Math.
70 (1982), 219--288,
[DOI 10.1007/BF01390728](https://doi.org/10.1007/BF01390728).

Pascadi's Proposition E fixes a positive integer level \(q\), two cusps
\(\mathfrak a,\mathfrak b\) of \(\Gamma_0(q)\), positive integers
\(m,n\), a sign, and \(\varphi\in C_c^\infty(\mathbb R)\).  It states

\[
 \sum_{c\in\mathcal C_{\mathfrak a\mathfrak b}}
 \frac{S_{\mathfrak a\mathfrak b}(m,\pm n;c)}c
 \varphi\!\left(\frac{4\pi\sqrt{mn}}c\right)
 =\begin{cases}
 \mathcal H+\mathcal M+\mathcal E,&+,\\
 \mathcal M'+\mathcal E',&-,
 \end{cases}
\tag{2.12}
\]

where \(\mathcal H\) is the holomorphic spectrum, \(\mathcal M,\mathcal
M'\) are the complete Maass spectra with \(\widehat{\mathcal B}_\varphi\)
or \(\check{\mathcal B}_\varphi\), and \(\mathcal E,\mathcal E'\) are
integrals over \(r\in\mathbb R\) and all cusps.  The holomorphic term is
absent only for the minus sign.  Exceptional eigenvalues
\(\lambda_j<1/4\), with \(\theta_j=\sqrt{1/4-\lambda_j}\le7/64\), are
part of \(\mathcal M\).  If \(\varphi\) is supported at
\(y\asymp Y\asymp\sqrt{mn}/C\), their Bessel transforms can cost

\[
 \max(1,Y^{-2\theta(q)})
 \asymp\left(1+\frac C{\sqrt{mn}}\right)^{2\theta(q)}.
\tag{2.13}
\]

For regular spectrum, the Deshouillers--Iwaniec large sieve as recorded
in Pascadi's Lemma H bounds each of the holomorphic, Maass, and
Eisenstein positive square sums by

\[
 \left(K^2+\mu(\mathfrak a)N^{1+\varepsilon}\right)
 \|a_n\|_2^2.
\tag{2.14}
\]

For the exceptional spectrum, Pascadi's Theorem A gives

\[
 \sum_{\lambda_j<1/4}X_0^{2\theta_j}
 \left|\sum_{n\sim N}a_n\rho_{j,\mathfrak a}(n)\right|^2
 \ll_\varepsilon(qN)^\varepsilon
 \left(1+\frac Nq\right)\|a_n\|_2^2
\tag{2.15}
\]

only for

\[
 X_0\ll\max(1,q/N,q^2/N^3).
\tag{2.16}
\]

Its Theorem 2 improves the admissible exceptional weight for the special
sequence \(a_n=e(n\beta)\):

\[
 \sum_{\lambda_j<1/4}X_0^{2\theta_j}
 \left|\sum_{n\sim N}e(n\beta)\rho_{j,\mathfrak a}(an)\right|^2
 \ll_\varepsilon(qaN)^\varepsilon(1+aN/q)N,
\tag{2.17}
\]

provided

\[
 X_0\ll
 \frac{\max(N,q/a)}{\min_{t\ge1}(t+N\|t\beta\|)}.
\tag{2.18}
\]

A smooth factor \(\Phi(n/N)\) is allowed only with uniform derivative
bounds.  The general Fourier-concentrated version is encoded in
Assumption 14: it still requires a positive spectral square bound with
parameters \(A_N\ge\|a\|_2\), \(Y_N\), and a restricted \(X_0\)-range.

Most relevant to a possible outer \((Q,R)\)-average, Pascadi's Corollary
18 assumes coprime integral \(r\sim R,s\sim S\), coefficient sequences
satisfying Assumption 14 at the integral level \(rs\), and
\(\Phi_{r,s}\) smooth on a fixed three-dimensional box with uniform
derivative bounds.  It estimates

\[
 \sum_{\substack{r\sim R,s\sim S\\(r,s)=1}}w_{r,s}
 \sum_{n\sim N}a_{n,r,s}
 \sum_{\substack{c,d\\(rd,sc)=1}}
 \Phi_{r,s}(n/N,d/D,c/C)
 e\!\left(\pm n\frac{\overline{rd}}{sc}\right)
\tag{2.19}
\]

by

\[
 (RSNCDZ)^{O(\varepsilon)}
 \|w_{r,s}A_{N,r,s}\|_2\,\mathscr I,
\qquad
 \mathscr I^2=D^2NR+
 \left(1+\frac{C^2}{R^2SY_N}\right)^{2\theta_{\max}}
 CS(C+DR)(RS+N).
\tag{2.20}
\]

Thus even the current moving-level theorem requires an integral modular
inverse, coprimality, a smooth modulus average, a special coefficient
large-sieve hypothesis, and an outer positive \(\ell^2\) norm.  These
are not formal consequences of the product collar (1.2).

### 2.4 Reciprocity and weighted-moment sources

**Blomer--Khan spectral reciprocity.**  Theorem 1 of Valentin Blomer and
Rizwanur Khan, *Twisted moments of L-functions and spectral reciprocity*,
Duke Math. J. 168 (2019), 1109--1177,
[arXiv:1706.01245v2](https://arxiv.org/html/1706.01245v2),
[DOI 10.1215/00127094-2018-0060](https://doi.org/10.1215/00127094-2018-0060),
assumes an admissible even rapidly decaying spectral test
\(\mathfrak h=(h,h^{\rm hol})\), coprime positive integers \((q,\ell)=1\),
\(1/2\le\Re s\le\Re w<3/4\), and a fixed cuspidal GL(3) form or the
minimal parabolic Eisenstein series.  The moment
\(\mathcal M_{q,\ell}^{\pm}\) is the sum of Maass and Eisenstein
contributions, plus the holomorphic contribution for the plus sign,
with local correction factors.  The Eisenstein term itself is a
one-variable integral of four L-functions with denominators
\(L(1+2it,\chi^2)L(1-2it,\bar\chi^2)\).  The theorem states

\[
 \mathcal M^+_{q,\ell}(s,w;\mathfrak h)
 =\mathcal N_{q,\ell}(s,w;\mathfrak h)
 +\sum_\pm\mathcal M^\pm_{\ell,q}
 (s',w';\mathscr T^\pm_{s',w'}\mathfrak h),
\tag{2.21}
\]

with

\[
 s'=\tfrac12(1+w-s),\qquad w'=\tfrac12(3s+w-1),
 \qquad
 \mathcal N_{q,\ell}\ll
 \ell^{\theta-1+\varepsilon}+q^{\theta-1+\varepsilon}.
\tag{2.22}
\]

This is a reciprocity identity between *complete fixed-level automorphic
spectral moments*.  It is not an estimate for an arbitrary two-variable
GL(1) Mellin weight, and neither \(q\) nor \(\ell\) can be identified
with an arbitrary pair \((Q,R)\) without producing the required local
correction factors, coprimality, complete spectra, and admissible
transform.

**Common-height weighted moments.**  Berke Topacogullari,
*The fourth moment of individual Dirichlet L-functions on the critical
line*, Math. Z. 298 (2021), 577--624,
[DOI 10.1007/s00209-020-02610-9](https://doi.org/10.1007/s00209-020-02610-9),
Theorem 2.2, proves for primitive fixed-conductor characters

\[
 \int_1^T|L(\sigma+it,\chi_1)L(\sigma+it,\chi_2)|dt
 \ll T^{1+\varepsilon}+
 (q_1q_2)^{1/2-\sigma}T^{2-2\sigma+\varepsilon}.
\tag{2.23}
\]

Its Theorems 1.5--1.6 give same-height positive moments (with a fixed
one-variable smooth complex weight), and Theorem 2.7 gives a
common-height approximate functional equation for
\(L(s,\chi_1)L(s,\chi_2)\).  Its balanced critical-line length satisfies
\(4\pi^2xy=q_1q_2t^2\), so for fixed conductors \(x\asymp y\asymp t\).
These statements do not accept independent \(t_1,t_2\), and the absolute
value in (2.23) discards the required phase.

For a current exact Motohashi-type comparison, Theorem 1.3 of Chung-Hang
Kwan, *Spectral Moment Formulae for GL(3) x GL(2) II: The Eisenstein
Case*, [arXiv:2310.09419v3](https://arxiv.org/html/2310.09419v3), states,
for an even holomorphic spectral weight \(H\) with exponential decay in a
wide strip and \(1/4+\epsilon_0<\Re s<3/4\),

\[
 \mathfrak M_{-\boldsymbol\alpha}^{(3)}(s;H)
 +\mathcal R_{-\boldsymbol\alpha}(s;H)
 +\mathcal R_{\boldsymbol\alpha}(1-s;H)
 =\sum_{i=1}^3\mathcal M_{-\boldsymbol\alpha}^i(s;H)
 +\frac12\int_{(1/2)}\zeta(2s-s_0)
 \prod_{i=1}^3\zeta(s_0+\alpha_i)
 (\mathcal F_{\boldsymbol\alpha}H)(s_0,s)\frac{ds_0}{2\pi i}.
\tag{2.24}
\]

The formula explicitly retains residual terms, three displayed
main-term packages, and continuous spectrum.  Its GL(1) fourth-moment input has one shared
variable

\[
 \int_{\mathbb R}\eta(t)
 \prod_{i=1}^2\zeta(1/2+it+\alpha_i)
 \zeta(1/2-it+\beta_i)\,dt.
\tag{2.25}
\]

It therefore illustrates why spectral inversion does not permit removal
of residual, main, or continuous pieces, but (2.25) is still a smooth
one-height four-zeta moment.  It has no literal map to the two-height
\(\zeta(t_2)L(t_1,\chi_4)G\) integral.

## 3. Proof and hostile applicability derivation

### 3.1 What the joint functional equation actually gives

Expanding \(G\) on the original lines is justified by (2.2), subject to
the integrability already established for the exact cardinal scalar.  A
lawful formal insertion of (2.5) is

\[
 \begin{aligned}
 \mathcal I_\eta
 =\frac1{(2\pi)^2}\sum_{a,b\ge1}\frac{g(a,b)}{a^\alpha b^\alpha}
 \int_{\mathbb R^2}&\widehat{\mathcal B}(s_1,s_2)
 \gamma_1(s_1)\gamma_0(s_2)\\
 &\times L(1-s_1,\chi_4)\zeta(1-s_2)
 a^{-it_1}b^{-it_2}\,dt_1dt_2,
 \end{aligned}
\tag{3.1}
\]

where \(s_j=\alpha+it_j\).  The dual L-functions in (3.1) lie on
\(\Re(1-s_j)=1/2-\eta\).  Their ordinary Dirichlet series do not converge
absolutely there.  Thus the next step cannot be the unqualified opening
of two dual sums.  One needs either an exact contour argument with every
completed pole and residue, or two parameter-uniform approximate
functional equations with all four pieces and remainders.

The gamma factors in (3.1) have size
\((1+|t_1|)^{-\eta}(1+|t_2|)^{-\eta}\).  After choosing \(\eta\) in the
required epsilon order they change only epsilon powers; they do not
display a \(J^{-1/2}\) normalization.  Their oscillatory phases may not
be discarded, but none of the audited theorems takes the exact
two-dimensional weight
\(\widehat{\mathcal B}\gamma_1\gamma_0\) as input.

Separate balanced AFEs yield four coefficient grids of the lengths
recorded in Section 2.1.  A common-height product AFE such as
Topacogullari's cannot collapse those grids because \(t_1,t_2\) are
independent.  Consequently an exact coefficientwise return from (3.1)
to the Round-162 collar is not supplied by functional equations alone.
This does not contradict, and the source verdict now expressly grants,
the separate conductor candidate's exact finite double-Poisson
transform.

### 3.2 Exact mismatch with shifted-convolution and reciprocity inputs

The decisive interfaces are:

| Source mechanism | Exact required arithmetic geometry | Exact project geometry after the proposed step | First mismatch |
|---|---|---|---|
| Blomer--Harcos (2.8) | \(m\pm n=h\), fixed integral \(h\), two fixed cuspidal GL(2) Hecke sequences | independent GL(1) dual coefficients convolved with \(g(a,b)\), or \(k\ell\approx XQR\) | multiplicative collar is not an additive shift; coefficient class is wrong |
| Blomer--Jana--Nelson (2.10) | \(n_1-n_2=b\ne0\) in \(\mathcal O_F[1/S]\), compact-smooth Whittaker weight, cuspidal GL(2) inputs | literal cardinal two-height kernel | no fixed additive \(b\), wrong representations, unpriced weight |
| Kuznetsov (2.12) | integral Fourier indices, a fixed integral level and cusps, generalized Kloosterman moduli, compact-smooth Bessel weight | an inequality restricting an integer product near an arbitrary-real centre | no modular inverse or Kloosterman sum has been derived |
| Spectral large sieve (2.14)--(2.20) | a fixed coefficient sequence inside a positive square, or special Fourier-concentrated sequences and smooth modulus averaging | signed \((Q,R,k,\ell)\)-aggregate with parameter-dependent endpoint weight | positive norm and hypothesis verification are missing; signs across moving levels are not retained |
| Blomer--Khan (2.21) | complete fixed-level GL(2) spectrum, coprime \(q,\ell\), admissible one-parameter spectral test, local corrections | two independent GL(1) heights and arbitrary \((Q,R)\) | no automorphic-moment identity or level/twist map |
| Topacogullari/Kwan | one common height with fixed smooth weight; positive or complete moment and all main terms | independent \((t_1,t_2)\), nonlinear radial/angular cardinal transform | common-height substitution changes the object |

These are hypothesis failures, not merely nonoptimal exponents.  A
theorem cannot be used and then repaired by inserting the omitted
\(G\)-coefficients, endpoint cells, or levels after its estimate, because
those insertions alter the coefficient norm and the transform on which
the theorem's constant depends.

### 3.3 Audit of the granted moving product collar and
\(g(Q,R)/(QR)\)

The conductor reports that a separate Round-169 candidate has lawfully
obtained an exact finite double-Poisson transform.  This source report
does not reproduce that derivation; for theorem applicability it grants
one signed aggregate of the schematic form

\[
 \mathscr C=
 \sum_{Q,R}\frac{g(Q,R)}{QR}
 \sum_{\substack{k,\ell\ge1\\
 |k\ell-XQR|\ll QRJ/L\\Q\ell\le Rk\le4Q\ell}}
 c_{Q,R}(k,\ell)\,\mathscr W_{Q,R}(k,\ell),
\tag{3.2}
\]

where \(\mathscr W_{Q,R}\) still contains the literal cardinal profiles,
gamma pieces, endpoints, and completion errors.  The question here is
only whether a cited primary theorem takes (3.2) from this exact finite
transform to the target.

1. **A collar is not a trace-formula input.**  Kuznetsov starts only
   after one has derived an exact exponential sum
   \(S_{\mathfrak a\mathfrak b}(m,\pm n;c)\), with integral Fourier
   indices and modulus belonging to a fixed cusp-modulus set.  The
   inequality \(|k\ell-XQR|\ll QRJ/L\) supplies neither an additive
   congruence nor a modular inverse.  The centre \(XQR\) is generally
   nonintegral because \(X\) and the accepted centre data are literal;
   replacing it by a nearest integer is an endpoint-changing operation.

2. **Fixed modulus/level does not mean moving product collar.**  One may
   apply a fixed-level identity separately after deriving the needed
   Kloosterman sum for a particular \((Q,R)\), but \(Q,R\) then enter the
   level, cusps, coefficient support, and Bessel weight.  The local
   factors of \(g(Q,R)\) allow common primes and include a distinct
   two-adic branch; Pascadi's explicit moving-level corollaries instead
   assume coprime factorizations \(q=rs\).  No permissible substitution
   \((r,s)=(Q,R)\) is available for all nonzero \(g(Q,R)\).

3. **The signed outer aggregate is not preserved by the cited bounds.**
   Identities such as (2.12) could be summed algebraically with signed
   outer coefficients if all hypotheses had first been met.  The bounds
   then available are (2.14), (2.15), or (2.20), which use positive
   spectral squares or \(\|w_{r,s}A_{N,r,s}\|_2\).  Applying a theorem
   separately and summing absolute values invokes (2.2); applying the
   moving-level corollary replaces the literal signed cancellation by an
   outer \(\ell^2\) norm and still requires Assumption 14.  Neither step
   is a theorem preserving the exact signed
   \(g(Q,R)/(QR)\mathscr W_{Q,R}\) aggregate.

4. **The literal weight is outside the stated smooth class until proved
   otherwise.**  The cardinal identity is a sum of \(O(L^2)\) unit
   cells.  Pascadi requires a smooth horizontal modulus average and
   uniform derivatives; Blomer--Harcos prices derivatives through high
   \(A^d\)-norms.  No source statement makes those constants uniform in
   the real-centre floor, stars, half-open shell, cone edges, profile
   transitions, or zero extension.  Treating a single smooth interior
   cell at the global scale (2.7) is not lawful.

5. **All spectra and zero frequencies remain.**  Even after an exact
   Kloosterman derivation, (2.12) produces holomorphic, regular Maass,
   exceptional Maass, and continuous Eisenstein terms.  Reciprocity
   adds explicit main and residual packages.  Keeping only a favorable
   cuspidal part, or treating a zero frequency as automatically
   negligible, is not an application of the cited theorem.

This proves the requested distinction: existing fixed-modulus and
fixed-integral-shift theorems do not by themselves control the moving
product collar (3.2), and the current averaged Kloosterman theorem does
not accept or preserve its exact collapsed \(G\)-weight and literal
parameter-dependent profile.

### 3.4 Restored power ledger

On the favorable recombined smooth/BV component, the radial length and
transform scale are

\[
 T\asymp JL,\qquad L^{2\eta}\sqrt{L/J}.
\]

The already audited triangle or positive-moment placements give (1.3).
Choose first the requested \(\varepsilon>0\), then
\(0<\eta\le\min(1/8,\varepsilon/4)\), and only then the auxiliary
\(\delta\) sufficiently smaller than \(\varepsilon\).  This absorbs
\(L^{2\eta}X^\delta\), but the quotient by the target remains
\(\sqrt J\).  The gamma quotients (2.6) and the coefficient cost (2.2)
are at most epsilon/polylogarithmic costs in this order; neither is a
negative half-power of \(J\).

For the granted collar, one smooth-interior dual
coefficient has scale

\[
 \frac{L^{3/2}}{QR\sqrt J},
\]

while the number of admissible factor pairs is

\[
 \ll_\varepsilon
 \left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon.
\]

The \((QR)^{-1}\) normalization is repaid by the collar width, giving
(1.4).  For polynomial intermediate blocks \(L\ll H\), the unpaid ratio
is \(H/L\); it reaches target scale only at \(L\asymp H\).  The spectral
large sieve cannot simply be credited with a further square root: its
right side includes the full coefficient \(\ell^2\) norm, level/length
terms such as \(1+N/q\), smooth-transform norms, and the exceptional
factor (2.13) or (2.20).  No parameter map has shown those restored
terms to be \(O(L^{3/2}X^\varepsilon)\).

Finally, (2.2) shows why a post-theorem restoration of \(G\) is not
innocent.  At \(\eta\asymp1/\log X\) its absolute cost is
\(\asymp(\log X)^3\), and for fixed \(\eta\) chosen after epsilon it is
an epsilon-dependent constant; either can be absorbed numerically, but
the operation erases the only possible cancellation between distinct
\((Q,R)\)-blocks.  It therefore cannot be used to certify the signed
mechanism being tested.

## 4. First doubtful or unproved step

After granting the separate conductor candidate's exact finite
double-Poisson transform, the first surviving source step is an exact
coefficientwise conversion of the moving product inequality (3.2) into a
source theorem's integral additive/Kloosterman data.  It must
name the level, cusps, Fourier indices, moduli, modular inverse,
coprimality, Bessel test, derivative norms, and outer coefficient
sequence.  No audited primary theorem performs that conversion or
provides a bound that retains the signed \(g(Q,R)/(QR)\) aggregate.

If a claimant instead derives the same object solely from (3.1), that
derivation must still justify the reflected Dirichlet-series opening or
give parameter-uniform independent-height AFEs with all four pieces,
gamma weights, poles/residues, \(p=2\), endpoints, and remainders.  The
separate finite transform means this auxiliary warning is no longer the
surviving source seam for the round.

Therefore a citation to “Kuznetsov”, “spectral large sieve”, “shifted
convolution”, “Motohashi”, or “reciprocity” at this point is not a
mathematical step.  The first failure precedes any claimed
\(\sqrt J\)-saving.

## 5. Required control tests and outcomes

Here “PASS” means that the audit has accounted for the item; it does not
mean that the target theorem is proved.

| Required control | Outcome | Exact reason |
|---|---|---|
| `G_local_coefficients_and_p2` | **PASS** | Table (2.1) gives all six odd-prime monomials and the separate \(p=2\) coefficient \(g(1,4)=-1\). |
| `G_weighted_l1_eta_cost` | **PASS algebraically; forbidden as placement** | Equation (2.2) gives \(A_\eta\asymp\eta^{-3}\).  Taking it before the joint phase destroys cross-block signs. |
| `zeta_completed_function_and_pole` | **PASS** | Equation (2.3) records the conductor-one gamma factor, root number \(1\), and completed poles at \(0,1\); contour moves must keep cancellations and residues. |
| `chi4_completed_function_parity_root_number` | **PASS** | Equation (2.4) records conductor \(4\), odd parity, Gauss sum \(2i\), root number \(1\), and entireness. |
| `joint_contour_orientation_and_gamma_factors` | **PASS for the formal identity; FAIL for a dual opening** | Equation (2.5) and the orientation discussion are exact.  Opening the reflected series on \(1/2-\eta\) is not justified. |
| `exact_cardinal_cell_or_endpoint_lawful_replacement` | **FAIL for every imported theorem** | The accepted identity remains exact, but no source placement prices its \(O(L^2)\) cell/Sobolev complexity or proves a lawful smooth replacement. |
| `dual_coefficients_phase_lengths_and_normalization` | **GRANTED FROM SEPARATE CANDIDATE; not rederived here** | The conductor reports an exact finite double-Poisson transform.  This source audit begins at its moving-collar output; bare separate AFEs would still have four grids with product length \(\asymp T\). |
| `no_l1_over_G_or_dual_variables_before_joint_phase` | **PASS as an audit guard** | Every route using (2.2), triangle over AFE pieces, or a separate fixed-\((Q,R)\) estimate is rejected as certification of the proposed mechanism. |
| `no_common_height_substitution` | **PASS** | Equations (2.11), (2.21), (2.23), and (2.25) have one shared/coupled parameter and are not substituted for \((t_1,t_2)\). |
| `no_absolute_or_positive_moment_inflation` | **PASS as a rejection** | The positive norms (2.14)--(2.20) and absolute moment (2.23) retain the known \(\sqrt J\) deficit. |
| `spectral_exceptional_main_and_continuous_terms` | **PASS as a source ledger; FAIL as a target bound** | Equations (2.12)--(2.13), (2.21), and (2.24) retain holomorphic, regular/exceptional Maass, Eisenstein, main, and residual pieces.  None is placed target-safely. |
| `functional_equation_AFE_Round162_self_return` | **PARTIAL / outside this source audit** | The conductor reports an exact finite double-Poisson transform.  Bare independent AFEs still do not equal a common-height product AFE; exact coefficientwise comparison with every accepted Round-162 branch belongs to the candidate review, while the surviving source seam is the collar-to-trace-formula placement. |
| `arbitrary_real_centre_floors_stars_profiles_and_p2_branch` | **FAIL for source applicability** | Fixed integral shifts/moduli and smooth weights do not reproduce the real-centre collar or its literal endpoint branches. |
| `target_sqrtJ_gain_and_epsilon_order` | **FAIL for gain; PASS for order** | The legal epsilon order is recorded in Section 3.4; the restored capacities remain (1.3) and (1.4). |
| `primary_source_exact_hypotheses` | **PASS** | The dated source cards state coefficient classes, level/shift integrality, weights, spectra, main terms, exceptional factors, and norm placements. |
| `false_unsigned_aligned_and_G_equals_one_controls` | **FAIL for any claimed source proof** | Once the cited positive norms are invoked, the bounds are insensitive to the actual cross-block signs and would also apply to aligned/adversarial coefficients or \(G=1\).  No extra use of \(\chi_4\), the nonlinear phase, or the local \(g\)-law has been identified. |
| `downstream_scope_and_no_exponent_promotion` | **PASS** | Even (1.1) would close only the exact \(t=1\) scalar/residual connector; all other channels and exponent ledgers remain quarantined. |
| `no_in_round_pivot` | **PASS** | The report audits only the frozen Round-169 joint-FE/spectral mechanism. |
| `Round170_strategy_literature_review_due` | **PASS** | This dated, interface-specific search does not replace the mandatory Round-170 full-proof strategy and current-literature review. |

The phase-aligned, unsigned, and \(G=1\) controls are especially
decisive.  A positive spectral large sieve can be useful only after a
new derivation shows that its coefficient sequence and norm preserve a
specific arithmetic saving unavailable to those controls.  No such
derivation is present in the audited source interface.

## 6. Dependencies and exact artifacts used

### Repository artifacts, read in full

- `protocol.md`;
- `state/active_campaign.yml`;
- `strategy/round169_m2_hard_top_t1_joint_functional_equation_spectral_strategy.md`;
- `proofs/kernels/m9_m2_hard_top_t1_mellin_euler_polylog_signed_moment_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reports/hybrid_zeta_l_source_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/briefs/signed_spectral_reciprocity_source_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/candidates/conductor_round169_joint_fe_double_poisson_self_return.md`, consulted after the conductor's seam update to grant the exact finite transform while retaining the source-placement audit.

The brief's authoritative graph hash is
`a360b2913563c9c288438751729c5033acd2e91ee613e44f171e1d31bc7441be`.
No sibling-agent report, synthesis, validation matrix, or shared state
file was used or edited.

### Primary literature checked, through 26 August 2026

1. Blomer--Harcos, Theorem 1 and arbitrary-level remark:
   [arXiv primary text](https://arxiv.org/html/math/0703246v2).
2. Blomer--Jana--Nelson, Theorems 1, 3, and 4:
   [arXiv primary text](https://arxiv.org/html/2404.10692v2).
3. Deshouillers--Iwaniec, Invent. Math. 70 (1982):
   [publisher DOI](https://doi.org/10.1007/BF01390728).
4. Pascadi, Proposition E, Lemma H, Theorems A and 2, Assumption 14,
   Corollaries 17--18:
   [arXiv v3 primary text](https://arxiv.org/html/2404.04239v3) and
   [published DOI](https://doi.org/10.1017/fmp.2026.10025).
5. Blomer--Khan, Theorem 1:
   [arXiv primary text](https://arxiv.org/html/1706.01245v2).
6. Topacogullari, Theorems 1.5--1.6, 2.2, and 2.7:
   [publisher DOI](https://doi.org/10.1007/s00209-020-02610-9).
7. Kwan, Theorem 1.3 and the shifted fourth-moment input:
   [arXiv v3 primary text](https://arxiv.org/html/2310.09419v3).

The literature conclusion is deliberately limited to these exact
versions and hypotheses.  The audit used analytic/algebraic reasoning
only and no numerical experiment.

## 7. Recommended state effect

**Recommended state effect: no change to the accepted proof graph; reject
promotion of any Round-169 target or strict sector based solely on the
audited source placements.**

The exact local \(g(a,b)\) table, weighted \(\ell^1\) cost, and GL(1)
functional-equation ledger may be retained as candidate audit facts.
They do not prove (1.1).  The separate conductor candidate supplies an
exact finite double-Poisson transform, but the collar-to-trace-formula
map and a target-safe source placement remain absent.  On that surviving
seam, the source evidence supports the scoped exit label

`t1_joint_FE_spectral_self_return_no_go`.

That label must be read narrowly: the proposed joint-FE/imported-spectral
route has reached its first unproved interface and, if forced through
the already accepted positive collar, returns to the \(H/L\) deficit.
It does not settle the physical sum, any other hard-TOP channel, BAL,
UNBAL, M1, endpoint uniformity, M9, either bridge, the quarter theorem,
or either exponent ledger.  Round 170's mandatory full-proof strategy
and current-literature review remains due.
