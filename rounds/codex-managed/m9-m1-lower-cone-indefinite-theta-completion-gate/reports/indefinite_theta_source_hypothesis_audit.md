# Round 144 source audit: level-four Appell completion and the later masked cone owner

## 1. Result: an exact scalar completion law, followed by a source-level no-go

Let

\[
 F(\sigma)=\sum_{\substack{h\geq1,\ r>4h\\r\ {\rm odd}}}
 \chi _4(r)e(hr\sigma)=\sum_{m\geq1}C(m)e(m\sigma),
 \qquad e(z)=e^{2\pi iz}.
\tag{144.S1}
\]

The Round-63 Appell classification is retained, not rediscovered:

\[
 A_4\!\left(\frac12,-3\sigma;2\sigma\right)
   =\frac12+2F(\sigma).
\tag{144.S2}
\]

The new source audit permits one structural sharpening.  In the exact
normalization of Bringmann--van Ittersum--Kaszian, equations
(2.12)--(2.15), put

\[
 \mathcal H(\sigma):=\frac12\widehat A_4
       \!\left(\frac12,-3\sigma;2\sigma\right).
\tag{144.S3}
\]

Then

\[
 \boxed{\mathcal H(\gamma\sigma)
   =\chi _4(d)(c\sigma+d)\mathcal H(\sigma)}
 \qquad
 \left(\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}
 \in\Gamma _0(4)\right).
\tag{144.S4}
\]

Thus the *completed torsion section* is genuinely scalar of weight one
and nebentypus \(\chi _4\) on \(\Gamma _0(4)\).  It is not a scalar
full-\({\rm SL}_2(\mathbb Z)\) object: outside \(\Gamma _0(4)\) the
section is not returned by integral elliptic shifts, and the natural
full-group object must retain the finite characteristic orbit (or the
corresponding vector-valued package).  The underlying level-four
lattice also has a nontrivial discriminant representation.  In
particular, lattice level four by itself would not prove the scalar
character in (144.S4); that character is obtained from the exact
Appell elliptic and modular factors below.

The completion is

\[
 \mathcal H(\sigma)=F(\sigma)+\frac14+
     \sum_{k=0}^{3}\mathcal R_k(\sigma),
\tag{144.S5}
\]
with the four separately compulsory terms

\[
 \boxed{\mathcal R_k(\sigma)=\frac{i}{4}(-1)^k
 \vartheta\!\left((2k-3)\sigma+\frac32;8\sigma\right)
 R\!\left(\frac12+(3-2k)\sigma;8\sigma\right)}.
\tag{144.S6}
\]

No audited source turns (144.S4)--(144.S6) into the required estimate
for the literal dyadic, hard-nonresonant, individual complex direction.
Exact coefficient extraction produces one pairing with \(\mathcal H\)
and four pairings with the \(\mathcal R_k\); no one of those five
pairings is covered by an audited summation theorem.  Globally removing
and restoring the microscopic mask by the accepted Round-141 lemma does
not remove the four correction owners, the incomplete cone coefficient,
the square-root phase, or the hard dyadic endpoints.  Round-142 rational
reconstruction still returns \(r_2/4\), leaves the negative-character
sector, and has top-block owner capacity \(R^{1/2+o(1)}\); the exact
character-Poisson owner has absolute capacity \(R=N^{1/4}\).

The rigorous round outcome is therefore

\[
 \boxed{\mathsf{indefinite\_theta\_completion\_no\_go}.}
\tag{144.S7}
\]

This is a mechanism obstruction, not a lower bound for the signed
scalar.  The scalar law (144.S4) is a structural sharpening only.  It
is neither a coefficient summation formula nor an estimate.

## 2. Exact statement, hypotheses, and primary-source theorem cards

### 2.1 Exact signature-\((1,1)\) lattice and boundaries

Work in the physical coordinates \((h,r)\) with

\[
 Q(h,r)=hr,qquad
 B((h,r),(h',r'))=hr'+rh'.
\tag{144.S8}
\]

Take

\[
 L_4=\mathbb Z(1,0)\oplus\mathbb Z(0,4).
\tag{144.S9}
\]

In this basis its Gram matrix is

\[
 A=\begin{pmatrix}0&4\\4&0\end{pmatrix},
 \qquad \det A=-16.
\tag{144.S10}
\]

Hence \(L_4\) is integral, even, nondegenerate, and of signature
\((1,1)\).  Since

\[
 A^{-1}=\begin{pmatrix}0&1/4\\1/4&0\end{pmatrix},
\]

its lattice level is four.  The two discriminant cosets represented in
physical coordinates by

\[
 \mu _1=(0,1)+L_4,qquad \mu _3=(0,3)+L_4
\tag{144.S11}
\]

and taken with coefficients \(+1,-1\) give exactly
\(\chi _4(r)\) on odd \(r\).  This is an exact signed coset difference,
not an untwisted full-divisor theta series.

Choose the negative vector and primitive rational isotropic vector
(primitive in the \(L_4\)-basis)

\[
 c_s=(1,-4),\qquad c_0=(0,-4).
\tag{144.S12}
\]

They satisfy \(Q(c_s)=-4\), \(Q(c_0)=0\), and
\(B(c_s,c_0)=-4<0\), so the null vector lies in the closure of the
same negative component.  Their sign kernel is

\[
 \kappa(h,r)=\frac12\{\operatorname {sgn}(r-4h)
                 -\operatorname {sgn}(-4h)\}
 =\frac12\{\operatorname {sgn}(r-4h)+\operatorname {sgn}h\}.
\tag{144.S13}
\]

Away from the walls, \(\kappa=1\) on \(h>0,r>4h\), \(\kappa=-1\)
on the opposite cone, and zero on the two mixed cones.  The sloping
wall \(r=4h\) has no odd lattice point.  The wall \(h=0\) is isotropic
and its formal constant-exponent series does not converge.  This is the
boundary that must be regularized; it may not be silently set to zero.

### 2.2 Exact Appell theorem and correction normalization

Bringmann--van Ittersum--Kaszian define, for \(\ell\in\mathbb N\),
\(\tau\in\mathbb H\), and away from the Appell polar divisor,

\[
 A_\ell(z,w;\tau)=\zeta^{\ell/2}
 \sum_{n\in\mathbb Z}
 \frac{(-1)^{\ell n}q^{\ell n(n+1)/2}\xi^n}
      {1-\zeta q^n},
\tag{144.S14}
\]

where \(q=e(\tau),\zeta=e(z),\xi=e(w)\).  Their equations
(2.13)--(2.15) state, in the same \(\vartheta,R\) normalization,

\[
\begin{aligned}
 \widehat A_\ell(z,w;\tau)
 &=A_\ell(z,w;\tau)\\
 &\quad+\frac{i}{2}\sum_{k=0}^{\ell-1}\zeta^k
 \vartheta\!\left(w+k\tau+\frac{\ell-1}{2};\ell\tau\right)
 R\!\left(\ell z-w-k\tau-\frac{\ell-1}{2};\ell\tau\right),
\end{aligned}
\tag{144.S15}
\]

\[
\begin{aligned}
 &\widehat A_\ell(z+m_1\tau+r_1,w+m_2\tau+r_2;\tau)\\
 &\quad=(-1)^{\ell(m_1+r_1)}
 \zeta^{\ell m_1-m_2}\xi^{-m_1}
 q^{\ell m_1^2/2-m_1m_2}\widehat A_\ell(z,w;\tau),
\end{aligned}
\tag{144.S16}
\]

and

\[
 \widehat A_\ell\!\left(\frac z{c\tau+d},\frac w{c\tau+d};
       \frac{a\tau+b}{c\tau+d}\right)
 =(c\tau+d)
 \exp\!\left(\frac{\pi ic}{c\tau+d}(-\ell z^2+2zw)\right)
 \widehat A_\ell(z,w;\tau).
\tag{144.S17}
\]

At \(\ell=4,z=1/2,w=-3\sigma,\tau=2\sigma\), the pole condition is
automatic on \(\mathbb H\): \(1/2\notin\mathbb Z(2\sigma)+\mathbb Z\).
Substitution into (144.S15), followed by division by two, gives exactly
(144.S5)--(144.S6).  In particular, the coefficient is \(i/4\), the
theta modulus and \(R\)-modulus are both \(8\sigma\), and all four
indices \(0\leq k<4\) occur.  These terms need only transform
collectively with the holomorphic Appell part; no source says that any
individual \(\mathcal R_k\) is invariant or negligible.

Semikhatov--Taormina--Tipunin, definition (1.1), assumes
\(\tau\in\mathbb H\) and \(\nu+\mu\notin\mathbb Z\tau+\mathbb Z\).
Their Theorem 1.1 (printed pp. 2--3) gives an \(S\)-law for
\(K_\ell\) with exactly \(\ell\) theta-times-Mordell \(\Phi\) terms.
The accepted Round-63 specialization

\[
 K_4\!\left(\tau,\frac\tau8,\frac12-\frac\tau8\right)
 =\frac12+2F(\tau/2)
\tag{144.S18}
\]

has \(\nu+\mu=1/2\) and is pole-free.  Their double-cone expansion
(2.2), printed p. 7, additionally requires
\(|q|<|e^{2\pi i(\nu+\mu)}|<1\); it does **not** apply here because the
middle modulus equals one.  The bilateral Appell definition and its
completed transform, not that double expansion, are the lawful
regularization.

### 2.3 Why direct indefinite- and false-theta theorems do not replace the Appell interface

* In Zwegers, *Mock Theta Functions*, Definition 2.1 (printed
  pp. 26--27), an isotropic endpoint \(c\in S_Q\) requires a
  characteristic \(a\in R(c)\), i.e.
  \(B(c,a)\notin\mathbb Z\).  Proposition 2.4 proves absolute
  convergence on that domain.  Proposition 2.7(7) (printed
  pp. 32--33) requires the still stronger \(D'(c)\) condition for the
  \(S\)-transform: both relevant real characteristics pair
  nonintegrally with \(c\).  For each odd coset (144.S11),
  \(B(c_0,\mu_s)=0\in\mathbb Z\).  Thus the literal zero-elliptic
  isotropic boundary is outside these hypotheses.

* Westerholt-Raum, *Indefinite Theta Series on Cones*, Theorem 2.7
  (printed p. 11) proves local absolute convergence for a
  nondegenerate nonnegative cone with rational isotropic edges only
  off the integral pairing hyperplanes.  Theorem 4.2 (printed p. 16)
  gives a real-analytic vector-valued Jacobi completion with
  meromorphic singularities on the same domain.  At zero elliptic
  characteristic the isotropic pairing set contains \(0\), so the
  displayed domain condition fails.  Theorem 1.1 is Vigneras's
  Schwartz-kernel/PDE theorem and does not regularize this polar wall.

* Bringmann--Nazaroglu, Theorem 1.2, starts with a positive-definite
  integral lattice and one sign of a linear functional.  Its Theorem
  1.5 is a fixed unary false-theta vector.  The form (144.S8) has
  signature \((1,1)\), and the isotropic Appell boundary is essential;
  neither theorem applies.

Consequently the failure of the direct cone hypotheses is real, while
the already accepted pole-free Appell regularization is source-legal.
There is no contradiction between these conclusions.

### 2.4 Summation/test hypotheses

No audited modular summation source has the required joint hypotheses.
The relevant mismatches are exact:

* Jutila, Theorem 1.1, treats the complete divisor coefficient; his
  Theorem 2.1 requires its stated holomorphic amplitude and does not
  license an arbitrary hard-masked \(C_c^\infty\) test.  Its divisor
  output is a paired cosine, not the individual \(e(+\sqrt{Nm})\)
  direction.
* Kaneko, Theorem 3.1 and Lemmas 3.2--3.3, treat the complete
  \(\sigma_\xi\), with \(\Re\xi>0\) at the convergence step, not the
  incomplete coefficient \(C\) at the limiting character exponent.
* Banerjee--Khurana, Theorems 4.3--4.4, require complete
  \(\sigma_{-\nu,\chi}\), \(0<\Re\nu<1/2\), and analytic testing.
* Beckwith--Diamantis--Gupta--Rolen--Thalagoda, Definition 3.1 and
  Theorem 4.1, require a weight-\(k\) harmonic Maass form
  (\(\Delta_kf=0\)) of polynomial cusp growth and give Riesz weights
  \((x-n)^\rho\), including the nonholomorphic Fourier coefficients.
  Equations (144.S15)--(144.S17) prove real-analytic Jacobi/modular
  covariance of this torsion section, but the audited source chain does
  not prove \(\Delta_1\mathcal H=0\).  Its literal masked square-root
  test is not a Riesz weight.
* Diamantis--Pimm, Definition 2.1 and Theorem 3.3, require harmonicity
  and, for a genuinely non-weakly-holomorphic form, state the theorem
  for nonpositive integral weight.  The present completed object has
  weight one and is nonholomorphic; their special Laplace/Bessel tests
  are not the literal test here.

Zwegers's Lemma 1.8, equations (1.4)--(1.5), does show that derivatives
of \(R\) produce unary-theta data.  After multiplication by the theta
factor in (144.S6), however, the correction ledger is theta-times-unary
theta (a Siegel--Narain-type boundary package), not a source-certified
single unary shadow of a harmonic Maass form.  This audit therefore
does not invoke a harmonic-Maass summation formula.

## 3. Proof and derivation

### 3.1 Strict cone, opposite cone, and Appell boundary

For the signed coset difference, (144.S13) contributes the desired
series on \(h>0,r>4h\).  On the opposite cone write
\((h,r)=(-h',-r')\).  Then
\(\kappa(h,r)=-1\), \(\chi _4(-r')=-\chi _4(r')\), and
\(hr=h'r'\).  Thus the opposite cone contributes a second copy of the
desired series.  Hence the strict two-cone sum, with \(h=0\) deleted,
is \(2F\).  The sloping boundary is empty by parity.  The isotropic
boundary is divergent, so it has no ordinary theta value.

The bilateral Appell series resolves precisely this defect.  Pairing
the \(n=h\) and \(n=-h\) summands in (144.S14) gives the two strict
cones, while the \(n=0\) summand is exactly \(1/2\).  This proves
(144.S2).  After the factor \(1/2\) in (144.S3), the isotropic Appell
boundary owner is the constant \(1/4\) in (144.S5).  This is a
regularized boundary term, not the sum of the divergent \(h=0\) wall.

### 3.2 Arbitrary-\(\gamma\) derivation of the scalar multiplier

Let

\[
 \gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma _0(4),
 \quad J=c\sigma+d,
 \quad
 \widetilde\gamma=
 \begin{pmatrix}a&2b\\c/2&d\end{pmatrix}\in\Gamma(2).
\tag{144.S19}
\]

Then \(\widetilde\gamma(2\sigma)=2\gamma\sigma\).  To make the left
side of (144.S17) equal
\(\widehat A_4(1/2,-3\gamma\sigma;2\gamma\sigma)\), take on its right
side

\[
 Z=\frac J2,qquad W=-3(a\sigma+b).
\tag{144.S20}
\]

Relative to \(z_0=1/2,w_0=-3\sigma,\tau_0=2\sigma\), these are the
integer elliptic shifts

\[
 Z=z_0+m_1\tau_0+r_1,quad
 W=w_0+m_2\tau_0+r_2,
\tag{144.S21}
\]

where

\[
 m_1=\frac c4,qquad r_1=\frac{d-1}{2},qquad
 m_2=-\frac{3(a-1)}2,qquad r_2=-3b.
\tag{144.S22}
\]

All four numbers are integers.  Equation (144.S16) gives the exact
elliptic factor

\[
 (-1)^{m_2}
 e\!\left(\frac{c(c+3a)}4\sigma\right).
\tag{144.S23}
\]

Equation (144.S17), for the lower-left entry \(c/2\) of
\(\widetilde\gamma\), gives the exact modular exponential

\[
 J\,e\!\left[-\frac c4
 \{(c+3a)\sigma+(d+3b)\}\right].
\tag{144.S24}
\]

The \(\sigma\)-dependent exponentials in (144.S23)--(144.S24)
cancel.  Since \(c=4C\), the remaining exponential is
\(e[-C(d+3b)]=1\).  Finally

\[
 (-1)^{m_2}=(-1)^{(a-1)/2}=\chi _4(a)=\chi _4(d),
\tag{144.S25}
\]

because \(ad\equiv1\pmod4\).  Division by two proves (144.S4).
This derivation uses the completed function throughout; applying its
factor to \(F\) alone would omit (144.S6).

The standard generator checks expose every normalization:

* For \(T=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\),
  \(\widetilde T=T^2\), the only nonzero shift is \(r_2=-3\), and both
  exponentials are one.  Hence \(\mathcal H(\sigma+1)=\mathcal H(\sigma)\).
* For \(U=\left(\begin{smallmatrix}1&0\\4&1\end{smallmatrix}\right)\),
  \(m_1=1\).  The elliptic factor is \(e(7\sigma)\), while the modular
  exponential is \(e(-7\sigma)\).  Hence
  \(\mathcal H(U\sigma)=(4\sigma+1)\mathcal H(\sigma)\).
* For \(-I\), one has \(r_1=-1,m_2=3\).  The elliptic factor is
  \(-1\), and the weight factor is \(J=-1\); their product is one, as
  required by \(\chi _4(-1)(-1)=1\).

The arbitrary-matrix calculation, rather than a presentation of
\(\Gamma _0(4)\), proves the law.  For an element outside
\(\Gamma _0(4)\), already \(m_1=c/4\) in (144.S22) need not be an
integer.  This is the first exact reason that the same section is not a
scalar full-group form.

### 3.3 Exact acceptance of the literal coefficient, direction, and mask

Let

\[
 b_M(m)=\mathbf1_{[M,2M)}(m)\mathbf1_{|k_m^2-Nm|>\sqrt M}
 m^{-3/4}V_{\rm low}(R^2m/N)e(\sqrt{Nm}).
\tag{144.S26}
\]

For any \(y>0\), define the finite Fourier kernel

\[
 K_M(x;y)=\sum_m b_M(m)e^{2\pi my}e(-mx).
\tag{144.S27}
\]

Fourier orthogonality gives, with no conjugation and no replacement by
a cosine,

\[
 T_M=\int_0^1F(x+iy)K_M(x;y)\,dx.
\tag{144.S28}
\]

Since \(K_M\) has zero constant coefficient, (144.S5) gives the exact
owner identity

\[
 \boxed{T_M=\int_0^1\mathcal H(x+iy)K_M(x;y)\,dx
 -\sum_{k=0}^{3}\int_0^1\mathcal R_k(x+iy)K_M(x;y)\,dx.}
\tag{144.S29}
\]

Thus the completion accepts the literal coefficient, positive complex
direction, and hard mask *algebraically*.  It does not accept them
analytically in the sense needed for the target: the source modular law
provides no estimate for any of the five terms in (144.S29), and the
four correction pairings cannot be discarded or bounded separately by
a theorem cited above.

Round 141 permits the microscopic nearest-square cells and floor
correction to be removed or restored once, after global reassembly, at
\(O_\varepsilon(X^\varepsilon)\).  It does not authorize branchwise
removal after splitting (144.S29), by rational denominator, or by a
correction index.  Moreover, its phase-value condition
\(|k_m^2-Nm|>\sqrt M\) does not exclude stationary *derivative* arcs of
\(m\mapsto\sqrt{Nm}\).

### 3.4 Rational cusp consistency and the correction-owner ledger

The accepted Round-142 prefix theorem says, for reduced \(a/q\),

\[
 \sum_{m\leq T}C(m)e(am/q)
 =\mathbf1_{4\mid q}\frac{i\pi\chi _4(a)}{2q}T
 +O\!\left((\sqrt T+q)\log(2q)\right).
\tag{144.S30}
\]

Abel summation therefore gives, for fixed \(q\) and \(y\downarrow0\),

\[
 F(a/q+iy)=\mathbf1_{4\mid q}\frac{i\chi _4(a)}{4qy}
 +O\!\left(y^{-1/2}\log(2/y)+q\log(2q)\right).
\tag{144.S31}
\]

The restriction \(4\mid q\) is consistent with the cusp orbit of
infinity under \(\Gamma _0(4)\) and with the character in (144.S4).
This consistency is not a coefficient summation theorem.  At all
cusps the completed object still contains the four terms (144.S6), and
outside the infinity orbit a full-group calculation necessarily moves
among characteristic components.  The audited sources do not provide
the individual cusp-growth estimates for all five masked pairings in
(144.S29).

Zwegers's differential formulas retain unary-theta boundary data in
every \(R\)-term.  The owner ledger is therefore:

1. the exact holomorphic coefficient \(C(m)\), not a completed divisor
   coefficient;
2. the Appell isotropic regularization \(1/4\), which vanishes in
   positive-index extraction but is needed for automorphy and cusp
   bookkeeping;
3. all four theta-times-\(R\) corrections \(\mathcal R_0,\ldots,
   \mathcal R_3\), including their unary-theta derivative/boundary
   data;
4. every cusp/characteristic component needed outside \(\Gamma _0(4)\);
5. after any rational reconstruction, all omitted modes, the moving
   cone boundary, and the surviving negative-character sector.

Round 142 proves that finite rational projections leave omitted modes
and that the canonical denominator-Abel completion reconstructs
\(\sigma_{\chi _4}=r_2/4\), not \(C\).  Hence (144.S4) explains the
four-divisible cusp hierarchy but does not repair the Round-142 Abel
return.

### 3.5 Complete \(R\)-\(M\)-\(N\) capacity ledger

Here \(N\asymp R^4\) and \(M\leq M_*\asymp R^2\).

| Owner or operation | Exact/rigorous capacity | Consequence |
|---|---:|---|
| Raw cone block, using \(|C(m)|\leq d(m)\) | \(M^{1/4+o(1)}\) | \(R^{1/2+o(1)}\) at \(M\asymp R^2\). |
| Abel pairing (144.S28), \(y\asymp M^{-1}\) | \(\|F_y\|_2\ll M^{1/2+o(1)}\), \(\|K_M\|_2\ll M^{-1/4}\), product \(M^{1/4+o(1)}\) | Exact automorphic packaging gives no norm gain. |
| Square-root frequency window | \(K_M\asymp\sqrt{N/M}=R^2/\sqrt M\); Fourier-transfer cost \(N^{1/4}M^{-1/2}=R/\sqrt M\) | A uniform additive-twist supremum cannot be inserted without this polynomial cost. |
| Curvature cell/Farey order | \(L_M\asymp Q_M\asymp M^{3/4}/R\) | The missing short-interval residual theorem is still required. |
| One rational branch | \(\min\{M^{1/4},RM^{-1/2}+R^{-1}\}\) | Rigorous second-derivative bound; not a completion gain. |
| All fixed-height denominators \(q\ll\sqrt M\) | \(\min\{M^{3/4},R+\sqrt M/R\}\) | Owner-sized; no target estimate. |
| Branches up to \(Q_M\) | \(Q_M(RM^{-1/2}+R^{-1})\asymp M^{1/4}+M^{3/4}/R^2\) | Top capacity \(R^{1/2+o(1)}\). |
| Exact character-Poisson stationary owner | for \(h\ll\sqrt M\), dual length \(\asymp h\sqrt{N/M}\) and amplitude \(\asymp N^{-1/4}/h\); absolute total \(N^{1/4}=R\) | Principal reciprocal owner self-returns; entry/exit/subtraction terms remain. |
| Appell half-boundary in the coefficient transform | \(O(M^{-1/4+o(1)})\) in the accepted Round-63 transform | Target-safe, but does not control the stationary bulk or the four nonholomorphic pairings. |
| Four correction pairings in (144.S29) | no hypothesis-matched source bound | They are owners, not errors. |

The rational main coefficient has \(\ell^1\)-mass \(\asymp Q\) and
squared mass \(\asymp\log Q\); its denominator-Abel ordering returns
the complete coefficient.  None of the capacities in the table is a
signed lower bound.  The only conclusion is that every currently
lawful way of taking absolute values is polynomially above
\(X^\varepsilon\), and no audited theorem supplies the missing joint
cancellation.

## 4. First doubtful or unproved step

There is no doubtful multiplier step after equations (2.12)--(2.15) of
Bringmann--van Ittersum--Kaszian are fixed as the source convention:
the shifts (144.S22), the elliptic factor (144.S23), the modular factor
(144.S24), and the character (144.S25) are exact.  Semikhatov--Taormina--
Tipunin Theorem 1.1 alone would *not* justify (144.S4); it supplies the
accepted four-term transformed Appell interface, while the scalar
\(\Gamma _0(4)\) simplification depends on the companion completed
Jacobi equations and the calculation above.  If those exact companion
equations were not accepted, the audit would have to stop at the
accepted Round-63 transformation.  No such normalization mismatch was
found.

The first unproved step is the next one:

> infer from the real-analytic scalar identity (144.S4) a coefficient
> summation formula, with uniform remainder, for all five pairings in
> (144.S29), accepting the literal incomplete coefficient \(C(m)\),
> hard dyadic/nonresonant test, moving cone boundary, and the individual
> complex direction \(e(+\sqrt{Nm})\).

No cited theorem has those hypotheses.  In particular, real-analytic
modularity is not itself a Voronoi formula; the audit has not proved
that \(\mathcal H\) is a harmonic Maass form; a cosine formula cannot
be projected to one complex direction without a separate identity;
and the four \(\mathcal R_k\) cannot be called negligible.  Even after
the globally lawful Round-141 mask restoration, the smooth full-cone
square-root twist retains top capacity \(R^{1/2}\) in the rational
route and \(R\) in the reciprocal stationary route.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_signature_11_lattice_and_integrality` | **Pass.** Equations (144.S8)--(144.S10) give the exact even integral signature-\((1,1)\) lattice, determinant \(-16\), dual matrix, and level four. |
| `strict_cone_kernel_opposite_cones_and_boundaries` | **Pass.** Equation (144.S13) gives the desired cone, opposite cone, zero mixed cones, empty odd sloping wall, and divergent isotropic wall. Opposite-cone character parity gives exactly a second copy of \(F\). |
| `odd_coset_chi4_level_multiplier` | **Pass.** The signed cosets (144.S11) give \(\chi _4\). Equations (144.S19)--(144.S25) derive, rather than assume, the scalar weight-one multiplier \(\chi _4(d)\) on \(\Gamma _0(4)\); the full-group package is not scalar. |
| `isotropic_boundary_regularization_and_convergence` | **Pass/obstruction.** The strict cone and pole-free bilateral Appell series converge, while the formal \(h=0\) wall diverges. Its lawful Appell regularization is the \(1/2\) in (144.S2), hence \(1/4\) in (144.S5). Direct isotropic-cone theorem domains fail. |
| `nonholomorphic_shadow_unary_residue_cusp_ledger` | **Pass as owner ledger.** All four normalized theta-times-\(R\) terms, the Appell boundary, unary-theta derivative data, cusp characteristic orbit, and rational residues are retained. No single harmonic unary shadow is asserted. |
| `holomorphic_coefficient_equals_C_not_complete_divisor` | **Pass.** Equations (144.S1), (144.S2), and (144.S28) extract exactly \(C(m)\). The denominator-Abel return \(r_2/4\) is explicitly rejected as a replacement. |
| `primary_source_hypothesis_match` | **Pass for Appell; fail for direct cone/false-theta shortcuts.** The Appell pole exclusion holds and four corrections are exact. Zwegers and Westerholt-Raum isotropic pairing domains fail at zero characteristic; positive-definite false-theta theorems fail by signature. |
| `coefficient_summation_formula_and_test_class` | **Fail at the needed theorem.** Equation (144.S29) is exact coefficient extraction, but no audited source estimates its five terms for this test. The harmonic-Maass and divisor-Voronoi tests do not match. |
| `individual_complex_direction_and_conjugate_control` | **Pass algebraically/fail analytically.** The kernel (144.S27) preserves \(e(+\sqrt{Nm})\) exactly. No cosine or conjugate pair is substituted, and no source bound for that individual branch exists. |
| `hard_nonresonant_mask_endpoints_and_owner` | **Pass as a prohibition.** The literal indicators occur in (144.S26). Round-141 permits one global target-safe restoration, not correctionwise or denominatorwise removal; phase-value nonresonance is not slope separation. |
| `round142_rational_spectrum_and_Abel_return_consistency` | **Pass/no-go.** The \(4\mid q\) pole (144.S31) matches the \(\Gamma _0(4)\) cusp/character structure, but finite modes omit owners and denominator-Abel returns \(r_2/4\) with the negative sector intact. |
| `full_R_M_N_capacity_and_downstream_scope` | **Pass/no-go.** Section 3.5 records \(M^{1/4}\), top \(R^{1/2}\), transfer \(R/\sqrt M\), local \(Q_M=M^{3/4}/R\), all-denominator and reciprocal \(R\) capacities. None is called a lower bound or a downstream theorem. |

No numerical or experimental evidence was used.  The allocation was
entirely analytical, algebraic, and source-audit work.

## 6. Dependencies, exact artifacts, and primary sources used

The permitted repository artifacts used were:

* `protocol.md`;
* `state/proof_obligations.yml`;
* `state/active_campaign.yml`;
* `strategy/conductor_0823_full_proof_strategy.md`;
* `rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/barrier_packet.md`;
* `sources/semikhatov_taormina_tipunin_2005.md`;
* `rounds/codex-managed/m9-m1-one-sided-divisor-false-theta/synthesis.md` and its conductor adjudication, derivation, and assigned Round-63 reports, used only to retain the accepted classification;
* `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md`;
* `rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reports/rational_shift_sqrt_twist_source_audit.md`;
* `rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reviews/conductor_round142_rational_spectrum_adjudication.md`;
* the assigned Round-144 brief.

Primary sources inspected and exact locations used were:

* S. Zwegers, [*Mock Theta Functions*](https://arxiv.org/abs/0807.4834), Lemma 1.8, equations (1.4)--(1.5); Definition 2.1; Proposition 2.4; Proposition 2.7(7).
* A. M. Semikhatov, A. Taormina, and I. Yu. Tipunin, [*Higher-Level Appell Functions, Modular Transformations, and Characters*](https://arxiv.org/abs/math/0311314), definition (1.1), Theorem 1.1, and double-cone equation (2.2); also [DOI](https://doi.org/10.1007/s00220-004-1280-7).
* K. Bringmann, J. van Ittersum, and J. Kaszian, [*Quasi-Jacobi forms, Appell--Lerch functions, and false theta functions as q-brackets of functions on partitions*](https://arxiv.org/abs/2401.02820), equations (2.12)--(2.15), printed pp. 9--10.  These reproduce the exact higher-Appell convention, completion, elliptic law, and modular Jacobi law used in (144.S14)--(144.S17).  The underlying completion source cited there is S. Zwegers, [*Multivariable Appell functions and nonholomorphic Jacobi forms*](https://doi.org/10.1007/s40687-019-0178-0).
* M. Westerholt-Raum, [*Indefinite Theta Series on Cones*](https://arxiv.org/abs/1608.08874), Theorem 1.1, Theorem 2.7, Corollary 4.1, and Theorem 4.2.
* K. Bringmann and C. Nazaroglu, [*A Framework for Modular Properties of False Theta Functions*](https://arxiv.org/abs/1904.05377), Theorems 1.2 and 1.5.
* O. Beckwith, N. Diamantis, R. Gupta, L. Rolen, and K. Thalagoda, [*Summation Formulas for Hurwitz Class Numbers and Other Mock Modular Coefficients*](https://arxiv.org/abs/2505.05574), Definition 3.1 and Theorem 4.1.
* N. Diamantis and J. Pimm, [*Summation Formulas for Harmonic Maass Forms*](https://arxiv.org/abs/2509.22607), Definition 2.1 and Theorem 3.3.
* M. Jutila, [*Lectures on a Method in the Theory of Exponential Sums*](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr80.pdf), Theorems 1.1, 2.1, and 2.2 and the negative-curvature remark.
* I. Kaneko, [*Mixed Moments of the Riemann Zeta and Dirichlet L-Functions*](https://arxiv.org/abs/2109.12495), Theorem 3.1 and Lemmas 3.2--3.3.
* D. Banerjee and K. Khurana, [*Character Analogues of Cohen-Type Identities and Related Voronoi Summation Formulas*](https://arxiv.org/abs/2306.12399), Theorems 4.3--4.4.

No graph, campaign, synthesis, validation, plan, proof draft, or shared
state file was edited.

## 7. Recommended state effect

**Retain, without calling it new:** the accepted Round-63 identity
(144.S2), pole-free level-four Appell classification, and compulsory
four-term completion.

**Promote only as a candidate structural sharpening after conductor
source-equation review:** equations (144.S3)--(144.S6), especially the
scalar weight-one \(\Gamma _0(4)\) law with nebentypus \(\chi _4\), its
arbitrary-matrix derivation, generator checks, and the qualification
that full-group covariance is vector-valued.  This promotion would say
nothing about coefficients or bounds.

**Promote as the Round-144 no-go:** direct isotropic indefinite-theta
theorems fail their nonintegral-pairing domain at the literal boundary;
the Appell route lawfully regularizes that boundary but exact extraction
is the five-owner identity (144.S29); no audited theorem supplies the
required test class, individual complex direction, correction bounds,
or uniform remainder; and the Round-142 rational/Abel and reciprocal
capacity owners remain unchanged.  Label this
`indefinite_theta_completion_no_go`.

**Leave open with no downstream promotion:** the fixed-centre
nonresonant scalar \(T_N\ll_\varepsilon X^\varepsilon\), the collar-tail
cross term, complete lower GAR, both direct-M1 parents, M9--M1, every
M2 owner, endpoint, M9, the quarter exponent, and the global theorem.
