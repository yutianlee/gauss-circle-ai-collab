# Round 148 discovery report: literal signed squarefree reciprocal transform

## 1. Result: exact transform and a squarefree-reciprocal dispersion no-go

Put (R=X^{1/4}), (N=\lfloor X\rfloor), and let
(DE\asymp M\leq R^2), (D\leq \sqrt M).  For a nonempty
(d\asymp D,e\asymp E) box in the strict cone, the exact positive
one-sided transform has base length

$$
 Q:=2\sqrt{ND/E}\asymp D\sqrt{N/M}.
\tag{148.1}
$$

The factor (2) in this definition is the literal saddle constant;
only the comparability in (148.1) is used in the power ledger.  After
the target-safe cone and radial endpoint collars described below, the
retained amplitude has (e)-support in (0<e\leq e_+), with
(e_+\ll E).  For each (d), define the exact finite progression set

$$
 \mathcal P(d):=
 \left\{(\alpha,b):
 \begin{array}{l}
 \alpha,b\ {\rm odd},\quad \mu(\alpha)\mu(b)\ne0,\quad b\mid d,\\
 \alpha^2\leq e_+,\quad
 \{n\geq1:\mathscr A_{D,E,U}(d,[\alpha^2,b]n)\ne0\}\ne\varnothing
 \end{array}\right\}.
\tag{148.1a}
$$

The last condition omits precisely those progressions which were empty
in the original finite divisor sum.  With this convention, the box
equals

$$
 \frac{e(1/8)}{N^{1/4}D}\,\mathcal T_{D,E,U}
 +O_{\varepsilon,V}(X^\varepsilon),
\tag{148.2}
$$

where

$$
\boxed{
\begin{aligned}
 \mathcal T_{D,E,U}
 ={}&\sum_{d\geq1}\mu ^2(d)\frac Dd
 \sum_{(\alpha,b)\in\mathcal P(d)}\mu(\alpha)\mu(b)
 \frac{\chi _4(\ell)}{\ell}                                      \\
 &\qquad\times
 \sum_{\substack{q>0\\q\ {\rm odd}}}
 \chi _4(q)\,
 \mathscr W_{d,\ell,U}(q)
 e\!\left(\frac{Nd\ell}{q}\right),
 \qquad \ell=[\alpha ^2,b].
\end{aligned}}
\tag{148.3}
$$

All sums in (148.3) are now literally finite: the
(\alpha^2\leq e_+) and nonempty-progression restrictions are inherited
before Poisson and are not supplied by the continuous saddle weight.
Its stationary point is

$$
 e_0=e_0(d,\ell,q)=\frac{4Nd\ell ^2}{q^2},
\tag{148.4}
$$

and (\mathscr W_{d,\ell,U}(q)) is the literal (d,e)-box, radial
profile, clipped prefix, and accepted smoothed cone evaluated at
((d,e_0)).  Thus its support has (q\asymp \ell Q), not
(q\asymp Q).  In particular, the actual outer coefficient is

$$
 \mu^2(d)\mu(\alpha)\mu(b)
 \frac Dd\frac{\chi _4(\ell)\chi _4(q)}{\ell}
 \mathscr W_{d,\ell,U}(q),
\tag{148.5}
$$

not an arbitrary bounded (q)-coefficient and not the coefficient in
the absolute squarefree (Q+D) analogue.

Formula (148.3) is the leading member of an exact character-Poisson
B-process expansion.  Every further stationary symbol coefficient is
given explicitly below, and the negative frequencies, nonstationary
tails, endpoint collars, complementary Taylor-polynomial term, and exact
remainder are retained.  The (K=6) summed lemma (148.29c) makes their
aggregate target-safe.  Consequently the transformed target is exactly

$$
 |\mathcal T_{D,E,U}|
 \ll_{\varepsilon,V}N^{1/4}D X^\varepsilon
 \asymp RD X^\varepsilon.
\tag{148.6}
$$

The proposed bare parameter (j=N-Aq) does **not** parameterize
(148.3).  If (g=(\ell,q)), (L=\ell/g), and (q_0=q/g), then

$$
 e(Nd\ell/q)=e(NLd/q_0),\qquad (L,q_0)=1,
\tag{148.7}
$$

and the exact nearest-integer parameter is

$$
 A=A(L,q_0)=\operatorname {nint}(NL/q_0),\qquad
 j=NL-Aq_0,\qquad |j|<q_0/2.
\tag{148.8}
$$

There is no tie because (q_0) is odd.  The bare relation
(j=N-Aq) is only the (L=1) reduced stratum (in particular the
unexpanded cell (\alpha=b=1)); it misses the primitive majority of
the square-divisor progressions.

This algebraic defect is accompanied by a precise, narrowly scoped
dispersion barrier.  Fix a legal long prefix and a nonzero common
interior rectangle \(\mathcal J_d\times\mathcal J_e\) as defined in
Section 3.5.
Already its unrecombined cells (b=1) have outer absolute mass

$$
 \mathscr L\asymp
 \sum_{\substack{\alpha^2\in\mathcal J_e\\
                  \alpha\ {\rm odd},\ \mu^2(\alpha)=1}}
 \frac1{\alpha^2}\#\{q\asymp \alpha^2Q:q\ {\rm odd}\}
 \asymp Q\sqrt E.
\tag{148.9}
$$

Any coefficient-weighted Cauchy step on these individual cells which
then replaces its (d)-diagonal by a separate nonnegative majorant has
minimum diagonal capacity

$$
 \sqrt D\,\mathscr L
 \asymp Q\sqrt{DE}=Q\sqrt M=\sqrt N\,D,
\tag{148.10}
$$

which exceeds (148.6) by (N^{1/4}\asymp R).  This is a rigorous
no-go only for Mobius-progression separation followed by that
unrecombined cellwise Cauchy and separately positive
diagonal/off-diagonal ledger.  It is not a lower bound for (148.3).
Pre-Cauchy regrouping of equal or \(N\)-aligned integer phases, and
signed cross-(\alpha,b), common-divisor, and (q)-character cancellation,
remain outside the claim.
This placement is strictly weaker than the Round-147 optimized
\(H\)-menu, whose losses are \(M^{1/4}\) below \(R^{4/3}\) and
\(R^{1/2}M^{-1/8}\) above it (only \(R^{1/3}\) at the crossover and
\(R^{1/4}\) at the top).  Thus (148.10) scopes the no-go to the
progression-cell Cauchy placement; it is not a new obstruction to every
organization of the target.

Accordingly this report closes under

$$
 \boxed{\mathsf{squarefree\_reciprocal\_dispersion\_no\_go}}.
\tag{148.11}
$$

It proves neither the signed target nor a signed lower bound and
isolates no owner-complete strict range.

## 2. Exact statement and hypotheses

Let (M\leq U\leq B_M\leq2M).  Write the literal box as

$$
\begin{aligned}
 \mathcal S_{D,E,U}:={}&
 \sum_{d,e\geq1}
 \mu^2(de)\mathbf 1_{e\ {\rm odd}}\chi _4(e)
 (de)^{-3/4}e(+\sqrt{Nde})                                      \\
 &\quad\times
 \omega_D(d)\omega_E(e)V_{\rm low}(R^2de/N)
 \mathbf 1_{\{M\leq de<U\}}\mathbf 1_{\{e>4d\}}.
\end{aligned}
\tag{148.12}
$$

Here (\omega_D,\omega_E) are fixed smooth members of a partition of
unity on (d\asymp D,e\asymp E); they do not replace the half-open
product prefix.  The individual positive phase and the fixed centre
(N=\lfloor X\rfloor) are part of the definition.

Before transformation, peel the product intervals of width
(O(\sqrt M)) at (M) and (U).  Their number of lattice pairs is

$$
 \ll \sum_{d\asymp D}(\sqrt M/d+1)\ll \sqrt M+D\ll\sqrt M,
$$

so their contribution to (148.12) is
(O(M^{-1/4}X^\varepsilon)).  If the prefix itself has length less
than (O(\sqrt M)), the whole prefix is assigned to this owner.
On a box meeting (e=4d), also peel
(|e-4d|\leq C\sqrt D).  This contains (O(D^{3/2})) pairs and,
because then (M\asymp D^2), contributes (O(X^\varepsilon)).
Use smooth transitions inside the peeled collars.  Denote the resulting
smooth compact amplitude, excluding ((de)^{-3/4}), by
(\mathscr A_{D,E,U}(d,e)).  It retains the same radial profile and
equals the literal amplitude at every unpeeled lattice point.  The
strict-cone and clipped-prefix differences have therefore already been
priced, rather than declared negligible.  Fix \(e_+\ll E\) with
\(\operatorname {supp}_e\mathscr A_{D,E,U}(d,\cdot)\subset(0,e_+]\)
for every \(d\).  The finite set \(\mathcal P(d)\) in (148.1a) is
therefore exactly the set inherited when the finite
\(\alpha^2\mid e\) expansion is interchanged with the original sum.

For later reference its stationary value in (148.3) is

$$
\begin{aligned}
 \mathscr W_{d,\ell,U}(q)
 :={}&\mathscr A_{D,E,U}\!\left(d,\frac{4Nd\ell^2}{q^2}\right)\\
 ={}&\omega_D(d)\omega_E(e_0)
 V_{\rm low}\!\left(\frac{4R^2d^2\ell^2}{q^2}\right)
 W_{M,U}\!\left(\frac{4Nd^2\ell^2}{q^2}\right)
 \kappa_D(d,e_0),
\end{aligned}
\tag{148.13}
$$

where (W_{M,U}) and (\kappa_D) are the just-described exact-on-the-
retained-lattice smooth prefix and cone factors.  In particular,
(e_0>4d) is equivalent to (q<\ell\sqrt N) on the strict plateau.

The exact relation between squarefree and coprime support is

$$
 \mu^2(de)=\mu^2(d)\mu^2(e)\mathbf1_{(d,e)=1},
\tag{148.14}
$$

and the signed decomposition used in (148.3) is

$$
 \mu^2(e)\mathbf1_{(d,e)=1}
 =\sum_{\alpha^2\mid e}\mu(\alpha)
  \sum_{b\mid(d,e)}\mu(b).
\tag{148.15}
$$

Because (e) is odd, only odd (\alpha,b) occur.  Formula (148.15)
is never put under a square-divisor or progression triangle in the
claimed identity.  If a completely expanded Mobius kernel is desired,
also use

$$
 \mu^2(d)=\sum_{\gamma^2\mid d}\mu(\gamma),\qquad d=\gamma^2m.
\tag{148.16}
$$

Then (148.3) becomes the same signed sum over
((\gamma,m,\alpha,b,q)), with (b\mid\gamma^2m),
(\ell=[\alpha^2,b]), and phase
(e(N\gamma^2m\ell/q)).  No sign or coprimality condition has been
lost.

## 3. Proof or derivation

### 3.1 Exact character-Poisson formula

For the Fourier convention
(\widehat F(\xi)=\int_{\mathbb R}F(x)e(-\xi x)\,dx), the primitive
mod-four Gauss sum gives the exact identity

$$
 \sum_{n\in\mathbb Z}\chi _4(n)F(n)
 =\frac i2\sum_{\substack{q\in\mathbb Z\\q\ {\rm odd}}}
 \chi _4(q)\widehat F(q/4),
\tag{148.17}
$$

because
(\sum_{r\bmod4}\chi _4(r)e(qr/4)=2i\chi _4(q)) for odd (q)
and is zero for even (q).  Apply (148.15), put
(e=\ell n), and use
(\chi _4(\ell n)=\chi _4(\ell)\chi _4(n)).  This gives the exact
integral transform

$$
 \frac i2\sum_d\mu^2(d)
 \sum_{(\alpha,b)\in\mathcal P(d)}
 \mu(\alpha)\mu(b)\chi _4(\ell)
 \sum_{q\ {\rm odd}}\chi _4(q)I_{d,\ell,q},
$$

$$
 I_{d,\ell,q}:=
 \int_0^\infty(d\ell x)^{-3/4}
 \mathscr A_{D,E,U}(d,\ell x)
 e\!\left(\sqrt{Nd\ell x}-\frac{qx}{4}\right)dx.
\tag{148.18}
$$

This identity already includes all endpoints and all frequencies.  In
particular, the dual zero frequency is identically absent: the Gauss
transform vanishes at (q=0).  Frequencies (q<0) have no saddle for
the positive physical direction.

### 3.2 Exact saddle, Gaussian unit, and every symbol coefficient

For (q>0), the unique critical point of (148.18) is

$$
 x_0=\frac{4Nd\ell}{q^2},\qquad
 e_0=\ell x_0=\frac{4Nd\ell^2}{q^2},\qquad
 \lambda=\frac{Nd\ell}{q},
\tag{148.19}
$$

and the critical phase is (\lambda).  Also

$$
 \phi''(x_0)=-\frac{q^3}{32Nd\ell}.
\tag{148.20}
$$

The particularly important cancellation of every power of (q) in
the leading amplitude is exact.  Set
(x=x_0(1+u)^2).  Since

$$
 \sqrt{Nd\ell x}-qx/4=\lambda(1-u^2),
$$

(148.18) becomes

$$
 I_{d,\ell,q}=
 \frac{2\sqrt2\,N^{1/4}}{(d\ell q)^{1/2}}e(\lambda)
 \int_{-1}^{\infty}H_{d,\ell,q}(u)e(-\lambda u^2)\,du,
\tag{148.21}
$$

where

$$
 H_{d,\ell,q}(u)
 =(1+u)^{-1/2}
 \mathscr A_{D,E,U}(d,e_0(1+u)^2).
\tag{148.22}
$$

Put
$$
 C_{d,\ell,q}:=\frac{2\sqrt2\,N^{1/4}}{(d\ell q)^{1/2}},
$$
choose an even \(\eta\in C_c^\infty((-1/2,1/2))\) with
\(\eta=1\) on \([-1/4,1/4]\), and extend \(H=H_{d,\ell,q}\) by
zero to \(u<-1\).  This extension is smooth because the retained
\(e\)-support is separated from zero.  Fix
$$
 K=6,\qquad
 P_{11}(u):=\sum_{j=0}^{11}\frac{H^{(j)}(0)}{j!}u^j.
\tag{148.22a}
$$
Every full-line polynomial Gaussian integral below is understood as
the Abel limit obtained after inserting \(e^{-\delta u^2}\) and
letting \(\delta\downarrow0\).  Define
$$
\begin{aligned}
 \mathcal R^{\rm loc}_6(d,\ell,q)
 :={}&C_{d,\ell,q}e(\lambda)
 \int_{\mathbb R}\eta(u)\bigl(H(u)-P_{11}(u)\bigr)
 e(-\lambda u^2)\,du,\\
 \mathcal I^{\rm cmp}_6(d,\ell,q)
 :={}&C_{d,\ell,q}e(\lambda)
 \operatorname*{Abel\,lim}
 \int_{\mathbb R}(1-\eta(u))
 \bigl(H(u)-P_{11}(u)\bigr)e(-\lambda u^2)\,du .
\end{aligned}
\tag{148.22b}
$$
The second line includes both the unchanged complementary \(H\)-integral
and the mandatory complementary Taylor-polynomial subtraction, including
the artificial \(u<-1\) full-domain tail.  Therefore the identity
$$
 \int_{-1}^{\infty}He(-\lambda u^2)\,du
 =\operatorname*{Abel\,lim}\int_{\mathbb R}P_{11}e(-\lambda u^2)\,du
 +\int_{\mathbb R}\eta(H-P_{11})e(-\lambda u^2)\,du
 +\operatorname*{Abel\,lim}\int_{\mathbb R}
 (1-\eta)(H-P_{11})e(-\lambda u^2)\,du
\tag{148.22c}
$$
is literal.  Exact Gaussian moments now give
$$
\boxed{
 I_{d,\ell,q}=
 \frac{2e(\lambda-1/8)}{N^{1/4}d\ell}
 \sum_{r=0}^{5}
 \frac{H_{d,\ell,q}^{(2r)}(0)}{r!(8\pi i\lambda)^r}
 +\mathcal R^{\rm loc}_6(d,\ell,q)
 +\mathcal I^{\rm cmp}_6(d,\ell,q).}
\tag{148.23}
$$

For a general fixed \(K\), the same convention with \(P_{2K-1}\)
gives the coefficient
\(H^{(2r)}(0)/(r!(8\pi i\lambda)^r)\), \(0\le r<K\).
In particular, every coefficient in (148.23) follows from

$$
 \int_{\mathbb R}u^{2r}e(-\lambda u^2)du
 =\frac{e(-1/8)}{\sqrt{2\lambda}}
 \frac{(2r)!}{r!(8\pi i\lambda)^r}.
\tag{148.24}
$$

Since (H(0)=\mathscr A(d,e_0)), multiplying the (r=0) term by
((i/2)\chi _4(\ell)\chi _4(q)) produces exactly the global unit

$$
 i\,e(-1/8)=e(1/8)
$$

and the amplitude in (148.3)--(148.5).  This also proves the sign of
the reciprocal phase (e(+Nd\ell/q)).

On the support, (d\asymp D,e_0\asymp E), so (148.19) gives

$$
 q=2\ell\sqrt{Nd/e_0}\asymp\ell Q,\qquad
 \lambda\asymp\sqrt{NM}.
\tag{148.25}
$$

This proves the claimed dual length and all stationary constants.

### 3.3 B-process, endpoint, collar, and polar ledger

The logarithmic derivatives of the bulk amplitude in (148.22) are
(O_r(1)).  More precisely, for \(0\leq j\leq12\),
$$
 \|H^{(j)}\|_\infty+
 \|(x\partial_x)^j((d\ell x)^{-3/4}
       \mathscr A(d,\ell x))\|_\infty
 \ll_{j,V}1+M^{j/2}{\bf1}_{\rm rad}
 +D^{j/2}{\bf1}_{\rm cone}.
\tag{148.25a}
$$
Here a radial or terminal-prefix transition occupies an
(O(M^{-1/2})) fraction of the relevant \(x\)- or \(q\)-support.  A
cone transition occupies an (O(D^{-1/2})) fraction and occurs only
when (M\asymp D^2).  Moreover, the exact finite indexing gives

$$
 \sum_{(\alpha,b)\in\mathcal P(d)}
 \frac1\ell\#\{q:q\asymp\ell Q\}
 \ll Q\sqrt E X^\varepsilon.
\tag{148.26}
$$

Consequently the absolute capacity of the (r=0) normalized symbol is

$$
 L_0\ll DQ\sqrt E X^\varepsilon,\qquad
 \frac{L_0}{N^{1/4}D}\ll R\sqrt D X^\varepsilon.
\tag{148.27}
$$

For (r=1), relative to this capacity, the bulk, radial-transition,
and cone-transition factors are respectively

$$
 \lambda^{-1},\qquad
 M^{-1/2}\frac{M}{\lambda},\qquad
 D^{-1/2}\frac{D}{\lambda}\quad(M\asymp D^2).
\tag{148.28}
$$

After division by (N^{1/4}D), (148.28) costs at most

$$
 \frac1{R\sqrt E},\qquad
 \frac{\sqrt D}{R},\qquad
 \frac1R,
\tag{148.29}
$$

respectively.  These are target-safe because (D\leq R).  Every
higher displayed (r) has an additional factor at most
(M/\lambda\ll R^{-1}), (D/\lambda\ll R^{-2}), or
(\lambda^{-1}).  The following fixed \(K=6\) lemma supplies the
uniform sum of the exact remainder and all nonstationary frequencies.

Let \(\sigma=q/(\ell Q)\), and scale \(y=\ell x/E\), so the
retained \(x\)-support becomes a fixed compact \(y\)-interval.  On
the enlarged retained
\((d,e)\)-support, a saddle can occur only for
\(\sigma\) in a fixed compact interval
\([\sigma_0,\sigma_1]\subset(0,\infty)\).  Fix
\(0<c_-<\sigma_0<\sigma_1<c_+\), and partition the odd frequencies
exactly into
$$
\begin{aligned}
 \mathcal Q_-&=\{q<0\},&
 \mathcal Q_{\rm lo}&=\{0<q<c_-\ell Q\},\\
 \mathcal Q_{\rm mid}&=\{c_-\ell Q\le q\le c_+\ell Q\},&
 \mathcal Q_{\rm hi}&=\{q>c_+\ell Q\}.
\end{aligned}
\tag{148.29a}
$$
The middle set includes the complete saddle/end-support buffer and is
handled by (148.22a)--(148.23).  In the other three sets, on the
\(y\)-support of (148.18),
$$
 |\partial_y\phi(y)|\gg
 \Lambda\left(1+\frac{|q|}{\ell Q}\right),
 \qquad \Lambda:=\sqrt{NM}\asymp R^2\sqrt M.
\tag{148.29b}
$$
For \(\mathcal Q_{\rm lo}\), the second factor may be replaced by
\(1\); for \(\mathcal Q_-\cup\mathcal Q_{\rm hi}\), dyadic
subdivision supplies the displayed decay.  On a block
\(|q|/(\ell Q)\asymp2^v\), six applications of
\((2\pi i\partial_y\phi)^{-1}d/dy\) give \(2^{-6v}\), while the
number of frequencies grows by \(2^v\).  Thus the summed block is
\(O(2^{-5v})\), and the two tails are geometrically summable.

Define the literal post-Poisson error majorant
$$
 \mathcal E_{\geq1}^{\rm phys}:=
 \frac12\sum_d\mu^2(d)
 \sum_{(\alpha,b)\in\mathcal P(d)}
 \sum_{q\ {\rm odd}}
 \left|I_{d,\ell,q}
 -\mathbf1_{q>0}\frac{2e(\lambda-1/8)}{N^{1/4}d\ell}
 H_{d,\ell,q}(0)\right|.
 \tag{148.29b0}
$$
It contains the symbols \(1\le r\le5\), the exact pair
\(\mathcal R^{\rm loc}_6+\mathcal I^{\rm cmp}_6\) on
\(\mathcal Q_{\rm mid}\), and all integrals in
\(\mathcal Q_-\cup\mathcal Q_{\rm lo}\cup\mathcal Q_{\rm hi}\).
Summing first over \(q\), then over the finite
\(\mathcal P(d)\), and finally over \(d\), uses
$$
 \sum_{d\asymp D}\sum_{(\alpha,b)\in\mathcal P(d)}
 \frac1\ell\#\{q\in\mathcal Q_{\rm mid}\}
 \ll DQ\sqrt E\,X^\varepsilon.
 \tag{148.29b1}
$$
Thus, with \(P_0\ll R\sqrt D\,X^\varepsilon\) the physical absolute
capacity of the leading symbol,
$$
\begin{aligned}
 \mathcal E_{\geq1}^{\rm phys}
 \ll_{\varepsilon,V}P_0\bigg[&
 \Lambda^{-1}
 +M^{-1/2}\frac M\Lambda
 +{\bf1}_{M\asymp D^2}D^{-1/2}\frac D\Lambda\\
 &+\Lambda^{-6}
 +M^{-1/2}\left(\frac M\Lambda\right)^6
 +{\bf1}_{M\asymp D^2}D^{-1/2}
       \left(\frac D\Lambda\right)^6\\
 &+\Lambda^{1/2}\bigg[
   \Lambda^{-6}
   +M^{-1/2}\left(\frac{\sqrt M}\Lambda\right)^6
   +{\bf1}_{M\asymp D^2}D^{-1/2}
       \left(\frac{\sqrt D}\Lambda\right)^6\bigg]
 \bigg]
 \ll_{\varepsilon,V}X^\varepsilon.
\end{aligned}
\tag{148.29c}
$$
Indeed \(P_0\ll R M^{1/4}X^\varepsilon\).  Using
\(M\leq R^2\), the three second-line contributions after multiplication
by \(P_0\) are respectively
\(O(R^{-11}M^{-11/4})\), \(O(R^{-11/2})\), and
\(O(R^{-11})\); the last estimate is only on \(M\asymp D^2\).
The three third-line contributions are \(O(R^{-10})\), uniformly
(and smaller in the cone term).  Together with (148.29), this verifies
the final inequality in (148.29c) on the full allowed range.
The first line is the \(r=1\) majorant for all displayed higher
symbols.  The second is the order-twelve localized/full-domain
stationary remainder; the factors \(M^6\) and \(D^6\) are essential
and cannot be replaced by the smaller sixth-derivative nonstationary
factors.  The third line is the sixfold integration-by-parts bound for
the negative and positive tails.  Its \(\Lambda^{1/2}\) converts an
unintegrated oscillatory integral to the leading stationary capacity;
the geometric \(2^{-5v}\) sum just proved owns the unbounded
\(q\)-tails.  The finite middle mass is exactly (148.29b1), of order
\(DQ\sqrt E X^\varepsilon\).  The same middle-range estimate owns
the complementary polynomial subtraction and every saddle/end-support
transition.  The dual \(q=0\) term is absent by \(\chi_4(0)=0\).  A
terminal prefix shorter than its radial collar was assigned to the
primal owner; every longer terminal transition has the radial derivative
and support fractions already displayed.  This proves the aggregate
error assertion in (148.2), rather than merely asserting it.

The hard radial endpoints and strict-cone boundary were already retained
as the primal peels preceding (148.13); hence no unpriced half-saddle is
present.  Direct finite character-Poisson summation introduces no polar
term.  If one instead inserts the hard ratio Perron formula, its
(z=0) residue is a separate mandatory term; the present accepted
collar route neither crosses nor deletes it.

### 3.4 Correct near-divisor map, exact divisors, and common divisors

Equation (148.7) proves the correct reduced phase.  For fixed (L,j),
(148.8) implies

$$
 q_0\mid NL-j,\qquad q_0\asymp LQ,\qquad(q_0,L)=1,
\tag{148.30}
$$

up to the imprimitive lift (g\mid\ell), for which
(q=gq_0) and (L=\ell/g).  Hence a fixed nonzero (j) has at most
(\tau(|NL-j|)\ll X^\varepsilon) admissible (q_0)'s, but the
harmonic (j)-sum and its modulus depend on (L).  It cannot be
replaced by the bare divisor relation (q\mid N-j).

If (148.16) is also expanded, put

$$
 G=(\gamma^2\ell,q),\qquad
 L_\gamma=\gamma^2\ell/G,\qquad q_\gamma=q/G.
$$

Then the literal phase is (e(NL_\gamma m/q_\gamma)), and the
nearest parameter is

$$
 j=NL_\gamma-Aq_\gamma.
\tag{148.31}
$$

Thus expanding squarefreeness of (d) creates further reduced moduli
and common-divisor strata; it does not restore (j=N-Aq).

The exact zero phase in (148.8) is nevertheless harmless by itself:
since ((L,q_0)=1), (j=0) implies (q_0\mid N).  Summing all its
imprimitive lifts absolutely in the unexpanded-(d) formula gives

$$
 \mathcal T_{j=0}
 \ll \tau(N)\sum_{d\asymp D}
 \sum_{(\alpha,b)\in\mathcal P(d)}
 \frac{\tau(\ell)}\ell
 \ll D X^\varepsilon,
\tag{148.32}
$$

well below (148.6).  The obstruction is the complete nonzero-(j)
family, not (q\mid N) alone.

Comparing two reduced cells gives the phase difference

$$
 N\left(\frac{L_1}{q_1}-\frac{L_2}{q_2}\right)m
 =\frac{N(L_1q_2-L_2q_1)}{q_1q_2}m.
\tag{148.33}
$$

Its completion modulus is (q_1q_2) divided by the full gcd with the
numerator.  Large common divisors and imprimitive moduli are therefore
structural.  The exact aligned fibres
(L_1/q_1=L_2/q_2) include, for example,
(b=1,q=\alpha^2r), on which the phase is (e(Nd/r)) for every
(\alpha).  A coprime-modulus or distinct-phase large sieve cannot
discard these fibres.

### 3.5 The diagonal obstruction

Restrict only for this control to a legal long prefix for which the
retained profile has a nonzero compact interior plateau.  After a fixed
refinement of the dyadic cutoffs, choose a closed proportional
rectangle
$$
\begin{aligned}
 \mathcal J_d&=[d_-,d_+]\cap\mathbb Z,
   &|\mathcal J_d|&\asymp D,\qquad d\asymp D,\\
 \mathcal J_e&=[e_-,e_+^\circ],
   &|\mathcal J_e|&\asymp E,\qquad e\asymp E,
\end{aligned}
$$
inside that plateau, on which the retained profiles have absolute
value at least \(2w_0>0\).  Refine the rectangle once more, if
necessary, so that fixed \(0<\vartheta_-<\vartheta_+\) satisfy
$$
 \frac{E(d/D)}{\vartheta^2}\in\mathcal J_e
 \quad
 (d\in\mathcal J_d,\
   \vartheta_-\leq\vartheta\leq\vartheta_+).
\tag{148.34a0}
$$
This is possible because the plateau is open before the closed
rectangle is selected.

Now set
$$
 \mathcal A_e:=
 \{\alpha:\alpha\ {\rm odd},\ \mu^2(\alpha)=1,\
                \alpha^2\in\mathcal J_e\}.
$$
The interval for \(\alpha\) has proportional length, so the elementary
odd-squarefree count gives
\(\#\mathcal A_e\asymp\sqrt E\).  For every
\(d\in\mathcal J_d\) and \(\alpha\in\mathcal A_e\), the literal
progression with \(b=1\) is nonempty at \(n=1\):
$$
 [\alpha^2,1]\,n=\alpha^2\in\mathcal J_e,\qquad
 \mathscr A_{D,E,U}(d,\alpha^2)\ne0.
$$
Thus \((\alpha,1)\in\mathcal P(d)\), including both the finite
\(\alpha^2\leq e_+\) restriction and the nonempty-progression
restriction.  If \(q/(\alpha^2Q)=\vartheta\), then the exact saddle is
$$
 e_0(d,\alpha^2,q)
 =\frac{4Nd\alpha^4}{q^2}
 =\frac{E(d/D)}{\vartheta^2}\in\mathcal J_e.
$$
Consequently every odd \(q\) in
\(\vartheta_-\alpha^2Q<q<\vartheta_+\alpha^2Q\) obeys
$$
 \left|\mathscr W_{d,\alpha^2,U}(q)\right|\geq w_0
 \quad(d\in\mathcal J_d).
\tag{148.34a00}
$$
A clipped prefix shorter than its radial collar was already assigned
to the primal owner; the rectangle above is asserted only for a legal
long prefix.  No lower-mass claim is made for a short prefix.  One
legal long prefix is enough to test a purported uniform cellwise
Cauchy proof.

On this plateau restrict to \(b=1\), write \(i=(\alpha,q)\), and put

$$
 c_i=\frac{\mu(\alpha)\chi_4(q)}{\alpha^2},\qquad
 q\asymp\alpha^2Q.
$$

Define the literal inner sequence and its cell sum by
$$
\begin{aligned}
 a_{i,d}:={}&\mu^2(d)\frac Dd\,
 \mathscr W_{d,\alpha^2,U}(q)
 e\!\left(\frac{Nd\alpha^2}{q}\right),\\
 S_i:={}&\sum_{d\in\mathcal J_d}a_{i,d}.
\end{aligned}
\tag{148.34a1}
$$
The elementary squarefree count on a fixed proportional interval,
\(\sum_{d\in\mathcal J_d}\mu^2(d)\geq c_{\rm sf}D\), follows from
\(\mu^2(d)=\sum_{\gamma^2\mid d}\mu(\gamma)\), with an
\(O(\sqrt D)\) boundary error; the finitely many smaller \(D\) are
absorbed by refining a nonempty plateau.  Hence (148.34a00) gives the
uniform lower norm
$$
 \sum_{d\in\mathcal J_d}|a_{i,d}|^2\geq c_0D,
 \qquad c_0=c_0(w_0,d_-/D,d_+/D)>0,
\tag{148.34a2}
$$
for every selected cell.

More explicitly, take the fixed index set

$$
 \mathcal I^\circ=\{(\alpha,q):\alpha\in\mathcal A_e,\
 q\ {\rm odd},\
 \vartheta_-\alpha^2Q<q<\vartheta_+\alpha^2Q\},
\tag{148.34a}
$$

so every saddle and every \(d\in\mathcal J_d\) is in the common
plateau.
Since \(\ell=\alpha^2\), the number of \(q\)'s for one \(\alpha\) is
\(\asymp\ell Q=\alpha^2Q\).  The coefficient-square and absolute
masses are therefore

$$
\begin{aligned}
 \sum_{i\in\mathcal I^\circ}|c_i|^2
 &\asymp Q\sum_{\alpha\in\mathcal A_e}\frac1{\alpha^2}
 \asymp \frac Q{\sqrt E},\\
 \mathscr L:=\sum_{i\in\mathcal I^\circ}|c_i|
 &\asymp Q\,\#\mathcal A_e
 \asymp Q\sqrt E.
\end{aligned}
\tag{148.34b}
$$

In the full kernel, for every fixed \((\alpha,b)\), the literal
coefficient is \(1/\ell\), the \(q\)-count
is \(\ell Q\), and hence the absolute mass is \(Q\).  The multiplicity
\(b\mid d\) is only \(\tau(d)\ll X^\varepsilon\).  Thus all \(b\)'s
alter the ledger by a divisor factor, while the exact \(b=1\) subfamily
already has the claimed order.

The natural coefficient-squared Cauchy factorization is

$$
 c_iS_i=
 \left(\frac{\mu(\alpha)\chi_4(q)}{\sqrt\ell}\right)
 \left(\frac{S_i}{\sqrt\ell}\right).
\tag{148.34c}
$$

Its first squared norm is
\(\sum_i1/\ell=\mathscr L\), including both the literal \(1/\ell\)
and the \(\ell Q\) frequencies.  The \(d\)-diagonal in the second
squared norm has the separately positive lower majorant
$$
 \sum_i\frac1\ell\sum_{d\in\mathcal J_d}|a_{i,d}|^2
 \geq c_0D\mathscr L
$$
by (148.34a2).  Its square-root product with the first norm is at least
$$
 \sqrt{\mathscr L\cdot c_0D\mathscr L}
 =\sqrt{c_0D}\,\mathscr L
 \asymp_{c_0}Q\sqrt{DE}=Q\sqrt M=\sqrt N\,D,
$$
up to the fixed plateau constant; this is (148.10).

No alternative positive weighting repairs this.  For any choice of
positive Cauchy weights \(\rho_i\), the coefficient-weighted inequality
has factors

$$
 \left(\sum_i|c_i|\rho_i\right)
 \left(\sum_i|c_i|\rho_i^{-1}|S_i|^2\right).
$$

If diagonal and off-diagonal are estimated separately by nonnegative
majorants, the diagonal contribution to their product is at least

$$
 c_0D\left(\sum_i|c_i|\rho_i\right)
  \left(\sum_i|c_i|\rho_i^{-1}\right)
 \geq c_0D\left(\sum_i|c_i|\right)^2
\tag{148.34}
$$

by Cauchy.  Taking square roots proves (148.10) for every positive
choice of (\rho_i) on these **unrecombined cells**.  Mobius signs
disappear only after this \(d\)-diagonal has been separately replaced
by its nonnegative majorant.  No statement is made about a change of
cell basis or signed regrouping before Cauchy.

Exact gcd reduction does not by itself shrink this particular fixed-cell
positive norm.  Splitting by \(g=(\ell,q)\) is a bijective partition
of the cells and preserves \(\sum1/\ell\).  On the primitive part
\(g=1\), the fractions \(\ell/q\) are reduced; literal equality of two
such fractions forces the same \((\ell,q)\).
For squarefree \(\alpha\), primitive \(q\)'s have density
\(\varphi(\alpha^2)/\alpha^2\gg X^{-\varepsilon}\), and they still
carry \(Q\sqrt E X^{-\varepsilon}\) absolute mass.  The aligned
proportional fibres \(q=\ell r\) can be recombined, but their mass is
only
$$
 \sum_{\alpha\ll\sqrt E}\frac Q{\alpha^2}\ll Q.
\tag{148.34d}
$$
They do not remove the primitive bulk from the unrecombined norm.
However, equality of reduced fractions is not the full phase-alignment
condition on integer \(d\).  Two cells have identical \(d\)-phases
whenever
$$
 N(\ell_1q_2-\ell_2q_1)\equiv0\pmod{q_1q_2},
\tag{148.34e}
$$
or, after primitive reduction, the analogous congruence with
\((L_i,q_{0,i})\).  These additional \(N\)-dependent fibres, all
pre-Cauchy regrouping of them, and any signed cross-cell correlation
are expressly outside (148.34).

This does not say that the signed scalar is large.  It says exactly
that a successful proof must retain off-diagonal cancellation capable
of neutralizing the progression diagonal before it is separately
majorized.  Such cancellation must also survive the aligned fibres in
(148.33)--(148.34e), the reduced moduli in (148.31), and the actual
(\chi_4(q)\mathscr W(q)) coefficient.  No such theorem is contained
in the permitted context.

### 3.6 False analogues, all-scale power, and the (H)-interface

The arbitrary-(q)-coefficient target is rigorously false.  Take the
(D=1) cell and a long nonzero interior prefix.  If coefficients
(c_q), (|c_q|\leq1), may be chosen freely, take

$$
 c_q=\overline{\chi_4(q)\mathscr W_{1,1,U}(q)e(N/q)}
       /|\mathscr W_{1,1,U}(q)|
$$

on a plateau.  The resulting scalar is (\gg Q).  For (M<R^2),
(Q\asymp\sqrt{N/M}>R), whereas the target is (R).  Thus the actual
character and B-process profile cannot be discarded and then recovered
after phase alignment.

For the separate absolute squarefree analogue

$$
 \sum_{q\asymp Q}\left|
 \sum_{d\asymp D}\mu^2(d)e(Nd/q)\right|
 \stackrel{?}{\ll}(Q+D)X^\varepsilon,
\tag{148.35}
$$

the controls (D=1) and (q\mid N) are consistent with (Q+D), so
this report does not claim a counterexample.  But the literal Mobius
triangle gives only (Q\sqrt D+D), and a positive second-moment
dispersion sees the (QD) squarefree diagonal and hence the capacity
(Q\sqrt D) when (Q\gg D).  Therefore (148.35) is neither proved
nor available from the proposed diagonal ledger.  More importantly,
(148.35) is not (148.3): the latter has all (q\asymp\ell Q), the
factor (1/\ell), the reduced phase (NL/q_0), squarefreeness of both
variables, coprimality, parity, cone, and prefix.

The scale ledger is

$$
 Q\asymp \frac{DR^2}{\sqrt M},\qquad
 \frac{Q+D}{RD}\asymp\frac R{\sqrt M},
\tag{148.36}
$$

because (Q/D\geq R).  Thus the bare lemma is target-borderline only
at (M=R^2).  At (M=R^{4/3}) it loses (R^{1/3}); below that it is
worse.  Combining the bare dual price with the lawful primal capacity
(M^{1/4}) creates the familiar (R^{4/3}) crossover, but neither
side proves a target-sized all-scale estimate.  The literal progression
triangle (148.27) loses (R\sqrt D), while the best separated Cauchy
diagonal (148.10) loses (R) on every selected legal long-plateau
aspect; it makes no assertion about a different pre-Cauchy cell basis.
For comparison, grouping first into the Round-147 powerful
\(H\)-convolution and optimizing primal against dual before modulus
gives the strictly better adverse capacity
$$
 \begin{cases}
 M^{1/4},&M\leq R^{4/3},\\
 R^{1/2}M^{-1/8},&R^{4/3}\leq M\leq R^2.
 \end{cases}
\tag{148.36a}
$$
Thus the \(R\)-loss in (148.10) says only that progression-cell Cauchy
is too early.  It neither supersedes the stronger \(H\)-menu nor rules
out a reorganization preserving the signed cross-cell correlation.

There is no termwise identification with the Round-147 correlation

$$
 \sum_k\frac{h_z(k)}k
 \sum_{|j|\lesssim k\sqrt{N/M}}A_{-z}(kN+j)\mathcal W_{k,z,U}(j).
\tag{148.37}
$$

The index (k) in (148.37) is the powerful Euler-convolution index;
the present (L) is a reduced lcm/common-divisor index depending also
on (q), and (148.8) is (NL-Aq_0), not (m-kN).  Summing all
Mobius cells and inverting every transform returns the same physical
box, but that global equality is not an interface map between individual
terms.  A second canonical transform of the reciprocal phase is the
known square-root self-return.  At the zero ratio mode, recombination
gives

$$
 \mu^2(n)A_0(n)=\mu^2(n)r_2(n)/4\geq0,
$$

so random independent signs across the complete squarefree coefficient
are unavailable.  An exact map from (148.3) to (148.37) would itself
have to prove the missing signed regrouping and all boundary-symbol
interchanges; analogy is not enough.

## 4. First doubtful or unproved step

The exact one-sided transform, its unit (e(1/8)), its
(N^{-1/4}(d\ell)^{-1}) amplitude, all Gaussian symbol coefficients,
and the target normalization are proved above.  The first unproved
arithmetic step is a signed estimate for (148.3) which groups the
((\alpha,b,q)) cells before any positive progression diagonal and
handles simultaneously

$$
 j=NL-Aq_0,\qquad q_0\mid NL-j,\qquad
 (q_0,L)=1,\qquad q_0\asymp LQ,
$$

together with (148.33)--(148.34e)'s proportional, \(N\)-dependent, and
large-common-divisor fibres.  The
bare (j=N-Aq) divisor argument addresses only (L=1).  Cauchy plus a
separately majorized diagonal loses (R) by (148.10), while taking a
square-divisor/progression triangle loses (R\sqrt D) by (148.27).

It remains logically possible that the actual
\(\mu(\alpha)\mu(b)\chi_4(\ell)\chi_4(q)\mathscr W(q)\) coefficient
has the required cross-cell cancellation.  No result in the permitted
context proves it.  The no-go is therefore method-specific and is not
an adverse lower bound for the signed scalar.

## 5. Control tests and outcomes

1. **`exact_one_sided_B_process_and_q_amplitude` -- pass.**
   Equations (148.17)--(148.24) give the exact Gauss factor, positive
   saddle, unit (e(1/8)), reciprocal sign, amplitude, and every
   stationary coefficient.  Equations (148.22a)--(148.22c) include the
   complementary Taylor-polynomial subtraction, while the \(K=6\)
   partition and derivative sum (148.25a), (148.29a)--(148.29c) own
   the exact remainder and every nonstationary frequency.

2. **`Q_length_and_RD_target_normalization` -- pass.**
   The literal relation is (q\asymp\ell Q) with
   (Q=2\sqrt{ND/E}\asymp D\sqrt{N/M}).  Equation (148.2) makes the
   target (N^{1/4}D\asymp RD), without replacing (N^{1/4}) by
   (R) inside the exact constant.

3. **`squarefree_both_variables_coprime_parity_character_cone` -- pass.**
   Equations (148.14)--(148.16) retain squarefreeness of both variables,
   coprimality, odd (e), both mod-four signs, and the strict cone up
   to its explicitly owned collar.

4. **`Mobius_square_divisor_signed_decomposition` -- pass.**
   The finite \(\mathcal P(d)\) in (148.1a) retains
   \(\alpha^2\le e_+\), the nonempty progression, and every
   \((\alpha,\gamma,b)\) sign.  No triangle is used in the transform
   identity; (148.27) is only an adverse control.

5. **`near_divisor_j_parameter_and_multiplicity` -- obstruction to the
   proposed bare map.**  The correct formula is (148.8), or (148.31)
   after fully expanding (d).  Fixed-(j) multiplicity is divisor-
   bounded only for (NL-j), with the reduced modulus and coprimality
   retained.

6. **`dispersion_diagonal_offdiagonal_common_divisor` -- fail for
   the scoped separated positive dispersion.**  On the common plateau
   (148.34a0)--(148.34a2), weighted Cauchy on unrecombined cells followed
   by a separate nonnegative \(d\)-diagonal loses (R) by (148.34).
   Literal reduced-fraction duplicates are not the same as the
   \(N\)-dependent phase congruence (148.34e).  Pre-Cauchy regrouping
   and signed cross-cell cancellation remain open.

7. **`q_divides_N_small_j_and_zero_frequency` -- pass/adverse split.**
   The character-Poisson zero frequency is absent.  Reciprocal
   (j=0) means (q_0\mid N) and is target-safe by (148.32).  Small
   nonzero (j) retains (q_0\mid NL-j), harmonic summation, and all
   imprimitive lifts; it is not reduced to the bare lemma.

8. **`arbitrary_q_coefficient_phase_alignment_falsifier` -- fail for
   the false analogue.**  The (D=1) construction following
   (148.36) gives size (\gg Q>R) whenever (M<R^2).

9. **`squarefree_absolute_QplusD_feasibility` -- unresolved, not
   imported.**  It survives the elementary (D=1) and exact-divisor
   controls, but its Mobius triangle and positive dispersion diagonal
   cost (Q\sqrt D+D).  Even if true, it would not equal the literal
   transform (148.3).

10. **`H_resonance_interface_translation` -- exact mismatch proved.**
    The (L,q_0,j) and (k,m-kN) indices are not termwise the same.
    Only equality after complete inverse transformation is presently
    justified; a second B-process is a self-return, not a saving.

11. **`all_M_D_E_Q_power_ledger` -- adverse.**  Equations
    (148.27), (148.36), and (148.10) record respectively the literal
    progression triangle, bare reciprocal price, and optimized
    unrecombined-cell diagonal on a legal long interior plateau,
    including the transition (M=R^{4/3}) and top (M=R^2) aspects.

12. **`clipped_prefix_profile_collar_polar_boundary` -- pass.**
    The half-open radial endpoints and cone collar are first priced in
    the primal scalar.  The radial profile and prefix then occur
    literally in (148.13).  All smooth endpoint symbols, transition
    buffers, and terminal-prefix remainders are owned by
    (148.22a)--(148.29c); direct character-Poisson has no pole.  The
    optional hard Perron zero residue is not crossed.

13. **`D1_prime_even_exact_radical_and_slow_family` -- pass as
    controls.**  For (D=1), (b=1) and the long squarefree variable
    still requires the signed (\alpha,q) sum.  The inherited exact
    checks (C(p)=\chi_4(p)) for (p>4) and
    (C(2p)=\chi_4(p)) for (p>8) are unchanged; the prime (2) is
    forced into (d).  If (N=D_0L_0^2) with (D_0) squarefree, the
    (t=1) exact-radical product is (s=D_0) and is target-safe.  If
    (N=sL^2+1), then
    (\sqrt{Ns}=sL+(\sqrt{L^2+1/s}+L)^{-1}), so the slow physical
    family remains and is not declared cancelling.  Its reciprocal
    image lies among the retained small-(j) cells.

14. **`individual_positive_direction_and_fixed_centre` -- pass.**
    No cosine pairing, centre average, or negative physical phase is
    used.  The positive direction is why only (q>0) has a saddle,
    and (N=\lfloor X\rfloor) is fixed throughout.

15. **`Round138_cross_tge2_and_downstream_scope` -- retained open.**
    This report concerns only the (t=1) box.  It does not own the
    independent Round-138 cross mechanism, any (t\geq2) layer, lower
    GAR, M9--M1, M9--M2, endpoint uniformity, M9, the bridge, the
    quarter target, or an exponent improvement.

No numerical experiment and no external theorem were used.

## 6. Dependencies and exact artifacts used

Only the context authorized for this task was used:

- `protocol.md`;
- `state/proof_obligations.yml`, restricted to the four target nodes;
- `state/active_campaign.yml`;
- `strategy/round148_squarefree_reciprocal_dispersion_strategy.md`;
- the Round-148 barrier packet and task brief;
- the Round-147 candidate, discovery report, adjudication, controls,
  and synthesis listed in the campaign manifest;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reports/blind_incomplete_fibre_additive_twist.md`, only for the
  character-Poisson unit and one-transform self-return control;
- `rounds/codex-managed/m9-m1-direct-square-root-product-bilinear/derivation_packet.md` and
  `rounds/codex-managed/m9-m1-direct-square-root-product-bilinear/reports/direct_product_bilinear_attack.md`, only for normalization,
  summed stationary-symbol, endpoint, and self-return checks.

The distinct coefficients in the Round-141 and Round-69 artifacts were
not imported into (148.3).  The transform, Mobius kernel, reduced
moduli, diagonal calculation, and all power translations above were
derived directly.

## 7. Recommended state effect

**Recommendation: retain the (t=1) signed target open and retain this
report as a scoped method no-go; make no shared-state or exponent
change.**

The exact candidate mathematics is (148.1a)--(148.5) and
(148.17)--(148.34e): it fixes the literal finite progression support,
one-sided reciprocal phase, outer amplitude, progression length, every
stationary constant, the \(K=6\) aggregate remainder, and the true
near-divisor/common-divisor parameterization.  The obstruction to record
is that the proposed bare (j=N-Aq) route omits the (L\neq1) family and
that weighted Cauchy on the unrecombined common-plateau cells, followed
by a separately nonnegative \(d\)-diagonal ledger, loses the factor
(R) in (148.10).

A future attempt must prove a signed cross-progression estimate for the
actual coefficient (148.5) before the positive diagonal, or supply an
exact, boundary-complete map to the Round-147 (H)-correlation and
prove that correlation.  Pre-Cauchy recombination of the
\(N\)-dependent fibres in (148.34e) is expressly not ruled out.
Arbitrary-(q) coefficients and the unproved absolute squarefree
(Q+D) analogue remain false or unavailable substitutes.
