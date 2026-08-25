# Round 144 discovery report: the exact level-four completion self-returns to the Round-140 owner

Campaign: `m9-m1-lower-cone-indefinite-theta-completion-gate`  
Task: `indefinite_theta_lattice_completion_attack`  
Role: discovery  
Starting graph SHA-256: `179e40fb38e6a5e26623c2584d469b1c4c8d5ae444a70d791298852f2d511204`

## 1. Result: exact completion, but no strict automorphic survivor

The exact cone series does have a source-legal signature-\((1,1)\),
level-four Appell completion.  This is not a new discovery: it is exactly
the completion accepted in Round 63, rewritten in the present
\(e(m\tau)\) normalization.  What is new in the present comparison is that
the later Round-140/141/142 owner ledger leaves no gap in which that
completion could give a smaller survivor.

Let

\[
 C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi _4(r),
 \qquad F(\tau)=\sum_{m\geq1}C(m)e(m\tau),
 \qquad q=e(\tau).
\tag{144.1}
\]

Then:

1.  The exact lattice is the hyperbolic plane with
    \(Q(h,r)=hr\), restricted to the two level-four cosets
    \(r\equiv1,3\pmod4\).  Its strict cone is
    \(h>0\), \(r-4h>0\).  The sloping boundary is orthogonal to the
    negative vector \((1,-4)\), while the boundary \(h=0\) is
    isotropic.  The latter cannot be inserted as an ordinary boundary
    theta series: its terms do not tend to zero.
2.  With the shear \(k=r-4h\),

    \[
      F(\tau)=\sum_{h\geq1}\frac{q^{4h^2+h}}{1+q^{2h}}
      =\frac12 A_4\!\left(\frac12,-3\tau;2\tau\right)-\frac14
      =\frac12K_4\!\left(2\tau,\frac\tau4,
                    \frac12-\frac\tau4\right)-\frac14.
    \tag{144.2}
    \]

    The bilateral zero term is \(1/2\), and the two opposite cones give
    equal contributions because both the sign kernel and \(\chi _4\)
    change sign under \((h,r)\mapsto(-h,-r)\).
3.  The completed moving section has weight one, level four, and
    nebentypus \(\chi _4\).  More precisely, if

    \[
    \begin{split}
      \mathcal H(\tau)
      &:={1\over2}\widehat A_4\!\left({1\over2},-3\tau;2\tau\right)\\
      &=F(\tau)+{1\over4}+\mathcal C_{\rm nh}(\tau),
    \end{split}
    \tag{144.3}
    \]

    then for \(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)
    \in\Gamma _0(4)\),

    \[
      \boxed{\mathcal H(\gamma\tau)
      =\chi _4(d)(c\tau+d)\mathcal H(\tau).}
    \tag{144.4}
    \]

    The correction \(\mathcal C_{\rm nh}\) is the explicit sum of four
    theta times Zwegers-\(R\) terms displayed in (144.16) below.  Thus
    \(F\) alone is not modular, and no one of the four correction terms
    is disposable.
4.  The holomorphic positive Fourier coefficient in (144.3) is still
    exactly \(C(m)\).  The completion does not replace it by
    \(r_2(m)/4\), a full divisor sum, or an opposite-cone coefficient.
    The Round-142 denominator-Abel reconstruction to \(r_2/4\) is a
    different, non-Cauchy rational-spectrum grouping and remains an
    obstruction rather than an owner reduction.
5.  Round 141 permits the hard nearest-square mask to be restored only
    before any Appell, rational-mode, or correction-piece split.  After
    this lawful restoration, the accepted Round-63 character-Poisson
    formula applies to a smooth dyadic weight.  Its full positive-\(j\)
    saddle, including the outer \(i/2\), is

    \[
      e(1/8)N^{-1/4}
      \sum_{h,j>0}{\chi _4(j)\over h}
      V_{\rm low}\!\left({4R^2h^2\over j^2}\right)
      \psi_M\!\left({4Nh^2\over j^2}\right)e(Nh/j).
    \tag{144.5}
    \]

    This is precisely the inverse of the accepted Round-140 stationary
    relation
    \(\mathcal P^+=e(-1/8)N^{1/4}\mathcal S^+\), after restoring that
    round's half-boundary, harmonic subtraction, negative aliases,
    collar, entry/exit, and stationary remainder owners.  It is the
    same reciprocal height--alias owner, not a strict survivor.
6.  On \(m\asymp M\), \(M\leq N/R^2\asymp R^2\), the original/Appell
    \(L^2\) capacity is \(M^{1/4+\varepsilon}\), hence
    \(R^{1/2+\varepsilon}\) at the top block.  The termwise absolute
    capacity of (144.5) is \(N^{1/4+o(1)}\asymp R\) on every nonempty
    dyadic block.  Thus the exact coefficient transform is a capacity
    self-return to the older reciprocal owner and is strictly worse
    than the accepted Round-142 holomorphic owner at the top scale.

Accordingly the round label supported by this report is
\[
  \boxed{\mathsf{indefinite\_theta\_completion\_no\_go}.}
\]
Here “no-go” means no completion-to-target or strict-survivor theorem;
it does **not** mean that a completion fails to exist.  No upper or lower
bound for the signed scalar is proved.

Finally, the automorphic object is \(F\), because its exponent is the
quadratic lattice value \(hr\).  The factor \(e(\sqrt{Nm})\) remains in
the external test function throughout.  It is not, and is never
relabelled as, a theta phase.

## 2. Exact statement and hypotheses

### 2.1 The lattice, cosets, cone, and boundaries

Let \(U=\mathbb Z^2\) in coordinates \(x=(h,r)\), with

\[
 Q(x)=hr,\qquad
 B((h,r),(h',r'))=hr'+rh'.
\tag{144.6}
\]

The Gram matrix of \(B\) on \(U\) is
\(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\); hence
\(U\) is even, unimodular, and of signature \((1,1)\).  To encode the
odd character without an informal weight, take

\[
 L=\mathbb Z(1,0)\oplus\mathbb Z(0,4),
 \qquad {\rm Gram}(L)=
 \begin{pmatrix}0&4\\4&0\end{pmatrix}.
\tag{144.7}
\]

Then \(L'=(\frac14\mathbb Z)\times\mathbb Z\),
\(|L'/L|=16\), and the level is exactly four.  Put
\(\mu_1=(0,1)\), \(\mu_3=(0,3)\), viewed in \(L'/L\).  The character
combination is \({\bf e}_{\mu_1}-{\bf e}_{\mu_3}\).

Set

\[
 c_-=(1,-4),\qquad c_0=(0,-1).
\tag{144.8}
\]

Then

\[
 Q(c_-)=-4,\quad B(c_-,x)=r-4h,qquad
 Q(c_0)=0,\quad B(c_0,x)=-h.
\tag{144.9}
\]

With \({\rm sgn}(0)=0\), the coefficient-preserving sign-kernel identity
is

\[
 \boxed{
 F(\tau)={1\over4}
 \sum_{\substack{h\in\mathbb Z\setminus\{0\}\\r\in\mathbb Z, r\ {\rm odd}}}
 \chi _4(r)
 \{\operatorname {sgn}B(c_-,(h,r))
    -\operatorname {sgn}B(c_0,(h,r))\}
 q^{hr}.}
\tag{144.10}
\]

The kernel is \(2\) on \(h>0,r>4h\), \(-2\) on its opposite, and
zero on the two mixed cones.  The factor \(1/4\) accounts for the
opposite-cone doubling.  The line \(r=4h\) has no odd lattice point.
The line \(h=0\), however, would formally contribute
\(\chi _4(r)\operatorname {sgn}(r)q^0\); its terms have modulus one and
do not tend to zero.  Therefore the exclusion \(h=0\) is part of the
statement, not an endpoint convention that a standard convergent theta
sum may silently choose.

Equivalently, with \(k=r-4h\),

\[
 Q(h,k)=4h^2+hk,qquad
 B((u,v),(h,k))=8uh+uk+vh,
\tag{144.11}
\]

and the cone is simply \(h>0,k>0\), with \(k\) odd and
\(\chi _4(k)=\chi _4(r)\).  In these coordinates the negative and null
vectors are \((1,-8)\) and \((0,-1)\).

### 2.2 Appell normalization, completion, and source hypotheses

Use the accepted higher Appell convention

\[
 A_\ell(u,v;\sigma)=e^{\pi i\ell u}
 \sum_{n\in\mathbb Z}
 {(-1)^{\ell n}e(\sigma)^{\ell n(n+1)/2}e(nv)
  \over1-e(u)e(n\sigma)}.
\tag{144.12}
\]

The exact current normalization is \(\sigma=2\tau\),
\(u=1/2\), \(v=-3\tau=-3\sigma/2\).  Its denominator is
\(1+q^{2n}\), which is nonzero for \(\tau\in\mathbb H\), and the
bilateral series converges normally on compact subsets.

In the Semikhatov--Taormina--Tipunin convention

\[
 K_\ell(\sigma,\nu,\mu)=
 \sum_{n\in\mathbb Z}{
 e^{\pi i\ell n^2\sigma+2\pi i\ell n\nu}
 \over1-e(\nu+\mu+n\sigma)},
\tag{144.13}
\]

the parameters are

\[
 (\ell,\sigma,\nu,\mu)=
 \left(4,2\tau,{\tau\over4},{1\over2}-{\tau\over4}\right),
 \qquad \nu+\mu={1\over2}.
\tag{144.14}
\]

Thus the hypotheses \(\ell\in\mathbb Z_{>0}\),
\(\sigma\in\mathbb H\), and
\(\nu+\mu\notin\mathbb Z\sigma+\mathbb Z\) in Theorem 1.1 of the
primary source are satisfied.  Its \(S\)-law gives one transformed
\(K_4\) plus exactly four theta--Mordell \(\Phi\) terms.  The same
source's double-cone expansion has the extra condition
\(|e(\sigma)|<|e(\nu+\mu)|<1\); it is **not** applicable because the
middle modulus here is one.

Writing \(R_{\rm Zw}\) for Zwegers' sign-minus-error-function kernel
(to avoid confusion with \(R=X^{1/4}\)), the accepted completed Appell
law gives

\[
 \widehat A_4(1/2,-3\tau;2\tau)
 =A_4(1/2,-3\tau;2\tau)+2\mathcal C_{\rm nh}(\tau),
\tag{144.15}
\]

where

\[
 \boxed{
 \mathcal C_{\rm nh}(\tau)
 ={i\over4}\sum_{a=0}^{3}(-1)^a
 \vartheta\!\left((2a-3)\tau+{3\over2};8\tau\right)
 R_{\rm Zw}\!\left({1\over2}+(3-2a)\tau;8\tau\right).}
\tag{144.16}
\]

This is the complete nonholomorphic/unary ledger.  Its
\(\bar\partial\)-image is the corresponding four-component product of
unary theta kernels; there is no audited collapse to one scalar unary
shadow.  The constant \(1/4\) in (144.3), all four terms in (144.16),
and the transformed Appell section are parts of one owner.

At the zero cusp, direct Riemann summation gives

\[
 F(iy)\sim{1\over8\sqrt{2y}}\qquad(y\downarrow0).
\tag{144.17}
\]

At \(\tau=1/4+iy\), every odd-\(h\) denominator
\(1+q^{2h}\) approaches zero.  The section is pole-free for every
\(y>0\), but no uniform separation from the Appell polar divisor is
available at the cusp.  This is why the four correction terms and their
cusp cancellations cannot be bounded away independently.

### 2.3 Frozen scalar and lawful test class

Let \(R=X^{1/4}\), \(N=\lfloor X\rfloor\asymp R^4\), and
\(M\leq M_*\asymp N/R^2\asymp R^2\).  Round 141 proves, globally over
the original disjoint blocks,

\[
 \mathfrak T_N=
 \sum_{m\geq1}m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 +O_\varepsilon(X^\varepsilon).
\tag{144.18}
\]

The error in (144.18) contains the exact radicals and every cell
\(0<|k_m^2-Nm|\leq\sqrt M\), as well as the accepted floor-to-cone
correction.  Equation (144.18) is a whole-coefficient statement.  It
does not license assigning the deleted cells separately to a rational
mode, an Appell correction, or one Poisson branch.

After (144.18), choose a smooth dyadic partition \(\sum_M\psi_M=1\)
on the positive support and put

\[
 w_M(u)=u^{-3/4}V_{\rm low}(R^2u/N)\psi_M(u)e(\sqrt{Nu}).
\tag{144.19}
\]

Then \(w_M\in C_c^\infty((0,\infty))\), including the smallest and
terminal blocks after the usual zero extension.  This is exactly the
test class accepted by the Round-63 character-Poisson formula.  The
literal hard nonresonant mask itself is not in that test class; its
prior owner-complete restoration is essential.

The sign in (144.19) is the individual positive complex direction.
The negative direction is its conjugate and is not used to replace
(144.19) by a cosine.

## 3. Proof and derivation

### 3.1 Cone, Lambert series, and coefficient preservation

In the sheared variables, absolute convergence gives

\[
\begin{split}
 F(\tau)
 &=\sum_{h\geq1}\sum_{\substack{k\geq1\\k\ {\rm odd}}}
   \chi _4(k)q^{4h^2+hk}\\
 &=\sum_{h\geq1}q^{4h^2}
   (q^h-q^{3h}+q^{5h}-\cdots)
 =\sum_{h\geq1}{q^{4h^2+h}\over1+q^{2h}}.
\end{split}
\tag{144.20}
\]

For \(n>0\), the \(n\)-th bilateral Appell summand in (144.12) is
\(q^{4n^2+n}/(1+q^{2n})\), while the \((-n)\)-th summand is

\[
 {q^{4n^2-n}\over1+q^{-2n}}
 ={q^{4n^2+n}\over1+q^{2n}}.
\tag{144.21}
\]

The zero term is \(1/2\).  This proves (144.2), including both factors
of two and the subtraction \(1/4\).  It also proves that every positive
Fourier coefficient remains \(C(m)\); no complete divisor fibre has
been inserted.

Formula (144.10) follows by checking the four sign regions.  On the
opposite cone, the sign kernel and \(\chi _4\) each reverse, so the two
minus signs cancel.  The explicit deletion of \(h=0\) is necessary for
convergence and is represented analytically by the bilateral zero term
and the nonholomorphic/Mordell correction ledger, not by a convergent
isotropic unary boundary sum.

### 3.2 Exact level-four modular law

The completed Appell function satisfies the accepted elliptic law

\[
\begin{split}
 &\widehat A_\ell(u+m_1\sigma+r_1,v+m_2\sigma+r_2;\sigma)\\
 &\quad=(-1)^{\ell(m_1+r_1)}
 e\{u(\ell m_1-m_2)-vm_1\}
 e(\sigma)^{\ell m_1^2/2-m_1m_2}
 \widehat A_\ell(u,v;\sigma),
\end{split}
\tag{144.22}
\]

and its weight-one modular Jacobi law.  For
\(\delta=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)
\in\Gamma_0(4)\), the corresponding matrix on \(\sigma=2\tau\) is

\[
 \widetilde\delta=
 \begin{pmatrix}a&2b\\c/2&d\end{pmatrix}\in\Gamma(2).
\tag{144.23}
\]

To return the moving section after applying the Jacobi law, take

\[
 m_1={c\over4},\quad r_1={d-1\over2},\qquad
 m_2=-{3(a-1)\over2},\quad r_2=-3b.
\tag{144.24}
\]

All four numbers are integers.  Substitution in (144.22) cancels the
\(\tau\)-dependent exponential in the modular Jacobi factor.  The
remaining multiplier is
\((-1)^{(a-1)/2}=\chi _4(a)=\chi _4(d)\), since
\(ad\equiv1\pmod4\).  This proves (144.4).  The calculation also shows
why the moving elliptic point is stable only after the exact elliptic
shifts: applying a scalar modular law directly to \(F\) would omit
(144.16) and the constant term.

### 3.3 Exact coefficient summation formula

For every \(w\in C_c^\infty((0,\infty))\), the accepted Round-63
identity is

\[
\boxed{
\begin{split}
 \sum_{m\geq1}C(m)w(m)
 &=\frac12\sum_{h\geq1}w(4h^2)\\
 &\quad+\frac i2\sum_{h\geq1}\sum_{j\ne0}\chi _4(j)
 \left\{{1\over h}\int_{4h^2}^{\infty}
 w(u)e\!\left(-{ju\over4h}\right)du
 -{2w(4h^2)\over\pi i j}\right\}.
\end{split}}
\tag{144.25}
\]

The bracketed double sum is absolutely convergent.  The displayed
half-boundary and subtraction are not separately absolutely summable:
using
\(\sum_{j\ne0}\chi _4(j)/j=\pi/2\), the subtraction cancels the
half-boundary only after the prescribed full symmetric recombination.
This is the exact isotropic/sloping-boundary owner in coefficient form.

Apply (144.25) to \(w=w_M\).  For \(j>0\), the phase in the integral is

\[
 \phi_{h,j}(u)=\sqrt{Nu}-{ju\over4h},qquad
 u_0={4Nh^2\over j^2},\qquad \phi_{h,j}(u_0)={Nh\over j}.
\tag{144.26}
\]

An interior stationary point requires \(j<\sqrt N\), and on a dyadic
block it has

\[
 h\ll\sqrt M,qquad j\asymp h\sqrt{N/M}.
\tag{144.27}
\]

The stationary contribution to the integral **inside the braces** in
(144.25) is

\[
 {2N^{-1/4}\over h}
 V_{\rm low}\!\left({4R^2h^2\over j^2}\right)
 \psi_M\!\left({4Nh^2\over j^2}\right)e(Nh/j-1/8).
\tag{144.28}
\]

Multiplying (144.28) by the outer \(i/2\) is essential.  Since
\(i e(-1/8)=e(1/8)\), the full principal family is exactly (144.5),
not twice (144.5) and not a cosine.

For \(j<0\), the positive-direction phase has no stationary point.
Those modes, the positive nonstationary modes, the two dyadic support
crossings, the \(j=\sqrt N\) endpoint/Fresnel transition, the
half-boundary, the harmonic subtraction, and all stationary remainders
remain in (144.25).  They may not be inferred term by term from the four
Appell corrections in (144.16); no such termwise identification is
claimed here.  What is proved is the owner-complete equality (144.25)
and the aggregate match to the already accepted Round-140 ledger.

### 3.4 Reverse match with Round 140

The reciprocal scalar before the Round-140 forward transform is

\[
 \mathcal S^+_{\rm recip}
 =\sum_{h\geq1}{1\over h}
 \sum_{1\leq j\leq D_h}\chi _4(j)
 V_{\rm low}\!\left({4R^2h^2\over j^2}\right)e(Nh/j),
\tag{144.29}
\]

with its literal floors, half endpoint, collar, and zero extension.
Round 140 proves

\[
 \mathcal S^+_{\rm recip}
 =\mathcal P^++O(R\log^C(2X)),
 \qquad
 \mathcal P^+=e(-1/8)N^{1/4}\mathcal S^+_{\rm cone},
\tag{144.30}
\]

where \(\mathcal S^+_{\rm cone}\) is the product-cone scalar, first with
the exact incomplete coefficient and then, by Round 141, with \(C(m)\)
outside the target-safe floor and microscopic cells.  Solving (144.30)
for the cone scalar gives

\[
 \mathcal S^+_{\rm cone}
 =e(1/8)N^{-1/4}\mathcal S^+_{\rm recip}
 +O(X^\varepsilon),
\tag{144.31}
\]

because \(N^{-1/4}\asymp R^{-1}\).  This is exactly the constant and
phase in (144.5).

The apparent difference between \(j<\sqrt N\) in (144.26) and the
literal \(j\leq D_h\) in (144.29) is precisely the accepted
Round-139/140 curvature collar and endpoint transition.  Its complete
forward cost is \(O(R\log^C X)\), hence its normalized reverse cost is
\(O(\log^C X)\).  The same is true of the negative aliases,
nonstationary modes, profile crossings, and stationary remainders by
the owner-complete Round-140 theorem.  Thus (144.25) does not create a
new piece after (144.5): with all owners restored, it returns exactly
to (144.29).

### 3.5 Rational spectrum and Abel compatibility

Round 142 proves for every reduced \(a/q\)

\[
 \sum_{m\leq Y}C(m)e(am/q)
 =\mathbf1_{4\mid q}{i\pi\chi _4(a)\over2q}Y
 +O((\sqrt Y+q)\log(2q)).
\tag{144.32}
\]

The level four and \(\chi _4\) multiplier in (144.4) are consistent
with this hierarchy, but automorphy does not make the hierarchy a
convergent Fourier projection.  Its limiting coefficient \(\ell^1\)
mass is \(\asymp Q\) and its squared mass is \(\asymp\log Q\).  Every
finite projection leaves main terms at omitted denominators.

When complete numerator sets are summed first and denominators are
Abel damped, Round 142 gives

\[
 P_\eta(m)={\pi\over4L(1+\eta,\chi _4)}
 \sum_{\ell\mid m}\chi _4(m/\ell)\ell^{-\eta}
 \longrightarrow \sigma_{\chi _4}(m)={r_2(m)\over4}.
\tag{144.33}
\]

Equation (144.33) is not the nonholomorphic completion (144.16).  It is
a distinct rational-spectrum regularization, and it changes the
holomorphic coefficient from \(C\) to the complete divisor coefficient.
For \(m=2^\nu n\), \(n\) odd and \(\chi _4(n)=-1\), the complete
coefficient vanishes, so the residual remains exactly \(C(m)\).  A
fixed-height reconstruction also leaves the moving wedge of weighted
unsigned capacity \(M^{1/4}\).  Thus neither the Appell completion nor
the Abel reconstruction removes the accepted negative-character or
moving-boundary owner.

The principal stationary self-return in Round 142 is also the same
mechanism as (144.26)--(144.31): automorphy, rational projection, and
character Poisson all preserve the reciprocal/cone pair rather than
produce signed cancellation.

### 3.6 Full \(R\)-\(M\)-\(N\) capacity

The complete power ledger is as follows.

1.  **Hard mask.**  Restoring all exact and microscopic cells costs
    \(O_\varepsilon(X^\varepsilon)\) globally by Round 141.  This saving
    is unavailable branchwise after a modular or rational split.
2.  **Holomorphic cone/Appell pairing.**  On \(m\asymp M\),

    \[
      \sum_{m\asymp M}m^{-3/4}|C(m)|
      \ll_\varepsilon M^{1/4+\varepsilon}.
    \tag{144.34}
    \]

    At Abel radius \(\eta\asymp M^{-1}\),
    \(\|F\|_2\ll M^{1/2+\varepsilon}\) and the periodized radial kernel
    has \(L^2\)-norm \(\asymp M^{-1/4}\).  Cauchy--Parseval therefore
    returns exactly \(M^{1/4+\varepsilon}\).  At
    \(M\asymp R^2\), this is \(R^{1/2+\varepsilon}\), the accepted
    Round-142 owner size, not the target.
3.  **Four Appell corrections and cusps.**  The continuous radial
    kernel alone has translate-wise \(L^1\) cost

    \[
      N^{1/4}M^{-1/2}\asymp R M^{-1/2}.
    \tag{144.35}
    \]

    This is only a kernel cost, not a bound for the scalar.  In
    particular, it equals one at \(M\asymp R^2\), but the zero-cusp
    Appell size is \(\asymp\sqrt M\), and other rational cusps approach
    the polar divisor.  Separating the transformed Appell term from any
    of the four terms in (144.16) has no owner-safe uniform bound.  The
    source theorem supplies an identity, not the missing correlated
    convolution estimate.
4.  **Poisson half-boundary.**  On a dyadic block,

    \[
      \sum_h|w_M(4h^2)|\ll M^{-1/4},
    \tag{144.36}
    \]

    hence it is target-safe.  The harmonic subtraction is not
    absolutely summable separately; only the bracket in (144.25) is a
    legal owner.
5.  **Reciprocal principal family.**  From (144.27), for each
    \(h\ll\sqrt M\) there are
    \(\asymp h\sqrt{N/M}\) stationary \(j\)'s, each with weight
    \(N^{-1/4}/h\).  Therefore

    \[
    N^{-1/4}\sum_{h\ll\sqrt M}{1\over h}
       h\sqrt{N/M}
    \asymp N^{1/4}\asymp R.
    \tag{144.37}
    \]

    Before the normalizing factor \(N^{-1/4}\), the Round-140
    reciprocal scalar has absolute capacity \(\asymp R^2\) and target
    \(R X^\varepsilon\).  Thus (144.37) is exactly its missing factor
    \(R\), not a gain.
6.  **Nonstationary, transition, and remainder owners.**  Round 140
    bounds their complete forward ledger by \(O(R\log^C X)\).  After
    multiplying by \(N^{-1/4}\), they cost
    \(O(\log^C X)=O_\varepsilon(X^\varepsilon)\).  This safety belongs
    to their complete reassembly, not to individual Appell corrections
    or rational modes.
7.  **Rational reconstruction.**  The moving wedge and the original
    holomorphic dyadic owner each retain \(M^{1/4}\), hence \(R^{1/2}\)
    at the top block; the denominator-Abel completion returns
    \(r_2/4\) and leaves the negative-character cone unchanged.

The ledger gives two rigorous self-returns: the Appell/Parseval route
returns (144.34), while the lawful coefficient transform returns the
older and larger capacity (144.37).  Neither capacity statement is a
lower bound for the signed scalar.

## 4. First doubtful or unproved step

There is no doubtful step in the lattice/coset identity, strict-cone
kernel, Lambert/Appell normalization, four-term completion, modular
multiplier, mask restoration, or exact character-Poisson formula.

The first unproved step remains exactly

\[
\boxed{
 \sum_M\sum_{\substack{m\in\mathcal I_M\\
 |k_m^2-Nm|>\sqrt M}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_\varepsilon X^\varepsilon.}
\tag{144.38}
\]

After the accepted Round-141 restoration, (144.38) is equivalent to
the smooth full-cone version in (144.18).  After the owner-complete
Round-63/Round-140 transform, it is equivalently the still-open signed
reciprocal estimate

\[
\boxed{
 \sum_{h\geq1}{1\over h}
 \sum_{1\leq j\leq D_h}\chi _4(j)
 V_{\rm low}\!\left({4R^2h^2\over j^2}\right)e(Nh/j)
 \ll_\varepsilon R X^\varepsilon,}
\tag{144.39}
\]

with the literal floors, collar, half endpoint, subtraction,
entry/exit, negative aliases, and stationary remainders understood as
in the accepted Round-140 owner.  No primary completion theorem supplies
the cancellation in (144.38) or (144.39).

The first false positive step would be any one of the following:

- treating \(e(\sqrt{Nm})\) as a theta exponent;
- inserting the divergent \(h=0\) lattice boundary;
- transforming the holomorphic Appell term without all four corrections;
- applying the completion to the hard mask without Round-141 restoration;
- using the per-kernel cost (144.35) as a scalar bound;
- replacing the positive complex direction by its cosine;
- or declaring the reciprocal principal family (144.5) smaller before
  restoring the Round-140 boundary and transition ledger.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `exact_signature_11_lattice_and_integrality` | **Pass.** Equations (144.6)--(144.7) give the even signature-\((1,1)\) lattice, dual, discriminant, and exact level four. |
| `strict_cone_kernel_opposite_cones_and_boundaries` | **Pass.** Equation (144.10) has the strict cone, opposite cone, negative sloping vector, null vector, and the explicit deletion of the divergent isotropic boundary. |
| `odd_coset_chi4_level_multiplier` | **Pass.** The cosets \(\mu_1,\mu_3\), their signed combination, and the derived weight-one \(\Gamma_0(4)\) multiplier \(\chi_4(d)\) are exact. |
| `isotropic_boundary_regularization_and_convergence` | **Pass/obstruction.** The strict cone and bilateral Appell series converge absolutely; the formal \(h=0\) series diverges.  The zero term, half-boundary/subtraction, and four corrections are retained. |
| `nonholomorphic_shadow_unary_residue_cusp_ledger` | **Pass/owner retained.** Equation (144.16) lists all four theta--\(R_{\rm Zw}\) terms.  Their unary \(\bar\partial\)-images and cusp cancellations are not collapsed or discarded. |
| `holomorphic_coefficient_equals_C_not_complete_divisor` | **Pass.** Equations (144.20)--(144.21) preserve every coefficient \(C(m)\); (144.33) is explicitly separated as the rejected owner-changing Abel reconstruction. |
| `primary_source_hypothesis_match` | **Pass.** Integer level, upper-half-plane, pole exclusion, and moving arguments meet the primary Appell theorem.  The source's stricter double-cone hypothesis fails and is not used. |
| `coefficient_summation_formula_and_test_class` | **Pass.** Equation (144.25) is exact for \(C_c^\infty((0,\infty))\); (144.18)--(144.19) explain why the literal test enters that class only after owner-complete mask restoration. |
| `individual_complex_direction_and_conjugate_control` | **Pass.** The positive branch gives (144.28) and the full constant (144.5).  The negative branch is merely recorded as the conjugate; no cosine inference is made. |
| `hard_nonresonant_mask_endpoints_and_owner` | **Pass.** Round-141 restoration is used globally before splitting.  Original block endpoints recombine, and a new smooth dyadic partition is then exact. |
| `round142_rational_spectrum_and_Abel_return_consistency` | **Pass.** Equations (144.32)--(144.33) retain all \(4\mid q\) modes, divergent spectral masses, the \(r_2/4\) Abel return, negative-character survivor, moving wedge, and principal self-return. |
| `full_R_M_N_capacity_and_downstream_scope` | **Pass/no-go.** Equations (144.34)--(144.37) give every relevant power: \(M^{1/4}\), top \(R^{1/2}\), kernel \(RM^{-1/2}\), and reciprocal \(R\).  None is mislabelled as a signed lower bound or a downstream theorem. |

No numerical or symbolic experiment was used.  The allocation was 100
percent analytical/source verification.

## 6. Dependencies and exact artifacts used

The required Round-144 context was read in full or, for the claim graph,
parsed in full with the exact active and Appell/cone obligations expanded:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md`;
- `rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/candidates/conductor_round142_rational_spectrum_self_return.md`;
- `rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reviews/conductor_round142_rational_spectrum_adjudication.md`.

After the conductor's scope intervention, the following accepted
predecessors were used to avoid re-claiming the Round-63 Appell identity
and to settle the exact reverse seam:

- `rounds/codex-managed/m9-m1-one-sided-divisor-false-theta/synthesis.md`;
- `rounds/codex-managed/m9-m1-one-sided-divisor-false-theta/reviews/conductor_false_theta_adjudication.md`;
- the three Round-63 reports, derivation packet, and validation control;
- `sources/semikhatov_taormina_tipunin_2005.md`;
- `rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/candidates/conductor_round140_smoothed_far_alias_reduction.md`;
- the Round-140 adjudication and exact Poisson connector.

The external theorem interface is confined to primary sources:

1. A. M. Semikhatov, A. Taormina, and I. Yu. Tipunin,
   *Higher-Level Appell Functions, Modular Transformations, and
   Characters*, Commun. Math. Phys. 255 (2005), 469--512,
   [arXiv:math/0311314v3](https://arxiv.org/abs/math/0311314),
   definition (1.1), Theorem 1.1, formulas (1.3)--(1.4), and the
   separate domain of their double-cone formula (2.2).
2. S. Zwegers, *Multivariable Appell functions and nonholomorphic Jacobi
   forms*, Research in the Mathematical Sciences 6 (2019), article 16,
   [DOI 10.1007/s40687-019-0178-0](https://doi.org/10.1007/s40687-019-0178-0),
   for the higher-Appell nonholomorphic Jacobi completion underlying the
   already accepted Round-63 four-term law.

Neither source is used for an exponential-sum estimate.  Every capacity
and coefficient transformation in this report is derived internally
from the accepted exact identities.

## 7. Recommended state effect

**Retain** the already proved Round-63 level-four Appell/source records;
do not create a duplicate discovery claim.  The useful Round-144 state
effect, after independent review, is a scoped obstruction:

> The exact level-four, weight-one completion of the floor-free cone
> coefficient remains valid after Round 141, but its strongest lawful
> coefficient transform, with the individual complex direction and all
> owners retained, is exactly the reverse of the accepted Round-140
> height--alias transform.  The holomorphic/Appell route retains
> \(M^{1/4}\) capacity, while the reciprocal principal owner has
> normalized capacity \(R\).  Round-142 rational/Abel reconstruction
> likewise returns \(r_2/4\) and leaves the negative-character and
> moving-wedge owners.  Hence no target bound and no strict
> owner-complete automorphic survivor follows.

Close this task under
`indefinite_theta_completion_no_go`.  Leave (144.38)--(144.39) open.
Make no change to the collar--tail cross term, complete lower GAR, either
direct M1 parent, M9-M1, any M2 owner, endpoint uniformity, M9, the
conditional bridge, the internal exponent \(1/3\), the separately
audited Li--Yang exponent, or the Gauss-circle target.
