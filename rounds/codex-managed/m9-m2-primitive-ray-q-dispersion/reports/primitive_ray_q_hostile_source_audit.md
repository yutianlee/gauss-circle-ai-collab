# Round 96 hostile/source audit: legal q-shifts erase the character and coefficient-blind q dispersion cannot cover the hard cone

Campaign: `m9-m2-primitive-ray-q-dispersion`

Task: `primitive_ray_q_hostile_source_audit`

Role: hostile mathematical and primary-source reviewer

Status: candidate evidence only; no shared proof state is edited.

## 1. Result

**Legal-shift character self-return and one-step capacity no-go.**  Write

\[
 a=m-q,\qquad b=m+q,\qquad
 r=(m^2-q^2)^{1/2},\qquad
 F(m,q)=m-r,
 \tag{96.H1}
\]

so that \(\Lambda=XF(m,q)\).  On the primitive odd lattice one has

\[
 m\not\equiv q\pmod 2,\qquad (m,q)=1,
 \qquad 0<q<3m/5.
 \tag{96.H2}
\]

Consequently, at fixed \(m\), every shift which stays on the actual odd
lattice is

\[
 q\longmapsto q+2h.
 \tag{96.H3}
\]

The character therefore has the exact autocorrelation

\[
 (-1)^{q+2h}(-1)^q=1.                              \tag{96.H4}
\]

Thus a fixed-\(m\) van der Corput step, completion, or Poisson step in
\(q\) is identical, as far as the character is concerned, to the unsigned
operation.  There is no alternating character left in the off-diagonal
correlation and the step-two Poisson lattice retains its zero frequency.

Moreover, a dyadic \(q\)-row has only \(O(D)\) legal points.  In the
orthogonality idealization in which all nonzero shifted correlations are
bounded away or vanish, one coefficient-uniform \(q\)-A-process saves only
\(D^{-1/2}\) over positive row capacity.  It therefore cannot *certify* the
required \(\rho^{-1/2}\) by diagonal or absolute-correlation estimates on
the nonempty hard range

\[
 \rho>D.                                           \tag{96.H5}
\]

This coefficient-blind failure is decisive for the proposed *full-cone*
mechanism unless a new signed actual-correlation theorem is supplied:
primitive
near-square rows with \(q=1\) have \(D\asymp1\), while
\(\rho=AJD^3/L^3\) can tend to infinity and the reciprocal interval can
remain populated.  Any successful estimate there must obtain cancellation
in \(m\), \(k\), \(g\), or the complete actual symbol; it cannot attribute
the full gain to a single dispersion step in \(q\).

There is a second exact obstruction to a determinant-curvature argument.
The stationary metric phase is proportional to \(F(m,q)\), and

\[
 \nabla^2F(m,q)
 ={1\over r^3}
 \begin{pmatrix}q^2&-mq\\-mq&m^2\end{pmatrix},
 \qquad \det\nabla^2F=0,
 \qquad \nabla^2F\binom mq=0.                     \tag{96.H6}
\]

Before stationary phase, the physical phase is degree-one homogeneous in
\((m,q,y)\), and its Hessian has the same radial null direction.  The
one-variable fixed-\(m\) curvature is nonzero, of size
\(gJD/A^2\), but that fact neither creates more than \(O(D)\) shifts nor
provides a nondegenerate multidimensional Hessian.

The primary-source audit found no literal theorem among the bilinear
Kloosterman-fraction, double-large-sieve, spectral/Kuznetsov, delta-method,
radical-spacing, or Li--Yang cone/second-spacing inputs that accepts the
moving reciprocal interval, the complete joint coefficient, the owner
masks, and the fixed-\(X\) density--discrepancy sum and then outputs
\(\rho^{-1/2}\).  Importantly, cone decoupling *can* handle a radial null
direction in its own extension setting, so Hessian degeneracy alone is not a
universal no-go.  The failure is the absence of a hypothesis-preserving map
from the present moving actual-symbol operator to that setting.

This report does **not** disprove (96.11).  It disproves the character gain
claimed from legal fixed-\(m\) \(q\)-shifts and the claim that a
coefficient-blind, diagonal/absolute-correlation \(q\)-A-process can close
all hard blocks.  A genuinely
joint cross-\(m\) actual-symbol theorem remains possible and open.

## 2. Exact statement and hypotheses

Let \(\mathscr L_{A,D}\) be the literal residual primitive-ray set in the
Round-96 packet, expressed in \((m,q)\) coordinates, including

\[
 a=m-q\asymp A,\quad b=m+q<4a,\quad b-a=2q\asymp D,
 \quad (a,b)=1,
 \tag{96.H7}
\]

and all exclusions for primitive square rays, exact nonsquare metric
centres, and \(\rho\ll1\).  Empty fibers are allowed.  Put

\[
 I_{m,q}:=
 \left({Ju_{m,q}\over1-u_{m,q}},
       {2Ju_{m,q}\over1+u_{m,q}}\right),\qquad
 u_{m,q}={q\over m+r},                              \tag{96.H8}
\]

and aggregate the *complete* coefficient only for notation:

\[
 \mathcal F_{m,q}:=
 \mathbf 1_{\mathscr L_{A,D}}(m,q)
 \sum_{g\in\mathcal G_{m-q,m+q}}
 \sum_{k\in I_{m,q}\cap\mathbb Z}
 \omega(k)W_R\!\left({XF(m,q)\over k}\right)
 \mathfrak C^\circ_{m-q,m+q,k}(g).                 \tag{96.H9}
\]

No factor in (96.H9) is replaced by a majorant.  In particular, the open
endpoints, floors, stars, profiles, collars, entry/exit samples, finite odd
lift set, and all density and discrepancy modes remain inside
\(\mathcal F_{m,q}\).  For one orientation the block is

\[
 \mathfrak Q_{A,D,K,G,R}
 =\sum_{(m,q)\in\mathscr L_{A,D}}(-1)^q\mathcal F_{m,q},
 \tag{96.H10}
\]

with the conjugate orientation and outer \(2\Re\) retained by the accepted
one-count assembly.

The no-go consists of the following exact assertions.

- **Lattice and character assertion.**  The map
  \((a,b)\leftrightarrow(m,q)\) is a bijection between primitive odd rays
  and (96.H2).  At fixed \(m\), the support is one parity class modulo
  two, so every nonempty shifted product in a \(q\)-correlation has shift
  \(2h\), and (96.H4) holds term by term.

- **Coefficient assertion.**  For

  \[
  \mathcal C_h=
  \sum_m\sum_q
  \mathcal F_{m,q+2h}\overline{\mathcal F_{m,q}},   \tag{96.H11}
  \]

  with zero extension outside the exact residual support, the character
  factor in the corresponding autocorrelation is identically one.  The
  product in (96.H11) contains two independently moving \(k\)-intervals,
  two lift sets, and the product of two complete metric coefficients.  It
  is not lawful to replace it by a same-\(k\), same-\(g\), rectangular, or
  discrepancy-only correlation without a separate proof.

- **Capacity assertion.**  A single coefficient-uniform A-process on a
  row of \(N_m\ll D\) legal \(q\)'s, when its shifted correlations are
  controlled only in magnitude or by orthogonality, has square-root gain
  \(N_m^{-1/2}\), hence at most \(D^{-1/2}\).  Thus \(\rho\leq D\) is a
  necessary capacity condition for that *coefficient-blind square-root
  implementation* to be capable of producing \(\rho^{-1/2}\).  Signed
  negative actual-symbol correlations could in principle do better, but
  proving them is precisely an additional theorem.

- **Curvature assertion.**  With \(y=x/g\) and

  \[
  \delta(m,q)=\sqrt{m+q}-\sqrt{m-q},qquad
  \Psi(m,q,y)=g\{ky-J\delta(m,q)\sqrt y\},          \tag{96.H12}
  \]

  one has \(\Psi(tm,tq,ty)=t\Psi(m,q,y)\) for fixed \(g,k\).
  Hence \(\nabla^2\Psi(m,q,y)(m,q,y)^T=0\).  At fixed
  \((m,g,k,y)\), however,

  \[
  \delta_{qq}
  ={1\over4}\{(m-q)^{-3/2}-(m+q)^{-3/2}\}
  \asymp {D\over A^{5/2}},
  \qquad |\Psi_{qq}|\asymp {gJD\over A^2},         \tag{96.H13}
  \]

  on a residual cone bounded away from \(q=m\).  Thus fixed-\(m\)
  curvature exists, but determinant-only multidimensional curvature does
  not.

- **Scope assertion.**  The result concerns only the proposed source of
  cancellation.  It gives no lower bound for the actual coefficient, no
  counterexample to (96.11), and no estimate for other M2 packets.

## 3. Proof or derivation

Since \(a=m-q\) and \(b=m+q\), both endpoints are odd exactly when
\(m\) and \(q\) have opposite parity.  A common divisor of \(a,b\) is odd
and divides \(2m,2q\); conversely every divisor of \(m,q\) divides
\(a,b\).  Therefore

\[
 (a,b)=(m,q).                                      \tag{96.H14}
\]

The cone condition \(b<4a\) is \(m+q<4m-4q\), or
\(q<3m/5\).  Finally,

\[
 \chi_4(a)\chi_4(b)
 =(-1)^{(a-1)/2+(b-1)/2}
 =(-1)^{m-1}=(-1)^q,                               \tag{96.H15}
\]

because \(m-1\equiv q\pmod2\).  If \(m\) is held fixed, preserving
opposite parity forces the shift in \(q\) to be even.  Equation (96.H4)
follows.  If the row is written as \(q=q_m+2n\), then
\((-1)^q=(-1)^{q_m}\) is constant in \(n\).  Poisson summation on \(n\)
therefore has an ordinary zero dual frequency, not a translated
half-frequency.

Coprimality does not restore the missing sign.  Möbius inversion gives

\[
 \mathbf1_{(m,q)=1}=\sum_{d\mid m,\ d\mid q}\mu(d),                 \tag{96.H16}
\]

and every such \(d\) is odd on (96.H2).  Completion occurs on progressions
of step \(2d\), on which \((-1)^q\) is still constant; its zero dual mode
survives.  In the shifted product one instead obtains the coupled mask
\(\mathbf1_{(m,q)=1}\mathbf1_{(m,q+2h)=1}\), whose local density depends
on the prime divisors of \(m\) and \(h\).  It is not an independent
oscillatory character.

For completeness, van der Corput's elementary averaging identity gives,
for a zero-extended sequence of length \(N\),

\[
 \left|\sum_n z_n\right|^2
 \leq {N+H-1\over H^2}
 \left\{H\sum_n|z_n|^2
 +2\Re\sum_{1\leq h<H}(H-h)
       \sum_nz_{n+h}\overline{z_n}\right\}.        \tag{96.H17}
\]

If every nonzero correlation in braces vanishes, increasing \(H\) saves
only until \(H\asymp N\), after which the diagonal term leaves the
square-root floor \(N^{-1/2}\).  Here \(N=N_m\ll D\).  Signed negative
correlations can make the braces smaller, but that is extra structure, not
a consequence of the A-process or of (96.H4).  An arbitrary
coefficient sequence supported at one legal \(q\) in each row attains that
floor and has no off-diagonal \(q\)-correlations at all.  Hence no theorem
uniform over bounded coefficients can infer \(\rho^{-1/2}\) from this one
step when \(\rho>D\).  This is a control on the method, not on the genuine
actual coefficients.

The moving support prevents a hidden translation identity.  The two
endpoints in (96.H8) are equivalently

\[
 \alpha_m(q)={J(\sqrt{m+q}-\sqrt{m-q})\over2\sqrt{m-q}},
 \qquad
 \beta_m(q)={J(\sqrt{m+q}-\sqrt{m-q})\over\sqrt{m+q}}.              \tag{96.H18}
\]

On \(q<3m/5\), both derivatives are \(O(J/A)\).  Thus a legal shift
\(q\mapsto q+2h\) moves each endpoint by \(O(Jh/A)\), and the integer
fibers can gain or lose \(O(1+Jh/A)\) modes.  The lift endpoints and
saddle entry/exit samples also move.  Zero extension makes (96.H17)
lawful, but it does not make the correlation rectangular or remove these
boundary terms.

Likewise, if
\(W_R(t)=\mu_R+\sum_{r\ne0}\widehat W_R(r)e(rt)\), then the shifted
product contains

\[
 \mu_R^2,qquad
 \mu_R\widehat W_R(r),\qquad
 \widehat W_R(r)\overline{\widehat W_R(r')}.        \tag{96.H19}
\]

The density--density term has neither a metric Fourier oscillation nor a
character oscillation after (96.H4).  Estimating only \(r,r'\ne0\), or
taking norms of the pieces separately, does not estimate (96.H11) with the
complete coefficient.

For the curvature calculation, differentiation of
\(F=m-(m^2-q^2)^{1/2}\) gives (96.H6).  Euler's identity applied to the
degree-one function (96.H12) gives the radial Hessian null vector before
stationary phase.  The saddle in \(y\) is

\[
 y_0={J^2\delta(m,q)^2\over4k^2},
 \qquad
 \Psi(m,q,y_0)=-{gJ^2\delta(m,q)^2\over4k}
              =-{g\Lambda\over2k},                 \tag{96.H20}
\]

so the reduced phase has exactly the rank-one Hessian (96.H6), multiplied
by \(-gX/(2k)\).  Formula (96.H13) follows by differentiating \(\delta\)
twice and using \(y\asymp A\).  It is therefore incorrect either to claim
that there is no one-variable curvature or to replace it by a nonzero
multidimensional Hessian determinant.

The short-\(q\) obstruction is literal.  For every even \(m>2\),

\[
 (a,b)=(m-1,m+1),\qquad q=1,\qquad (a,b)=1,
 \qquad ab=m^2-1\ne\square.                         \tag{96.H21}
\]

The sign is constantly \(-1\).  A Pell subfamily is obtained from

\[
 m^2-3n^2=1,
 \tag{96.H22}
\]

using the odd powers of \(2+\sqrt3\), for which \(m\) is even.  Then
\(ab=3n^2\) is nonsquare and

\[
 F(m,1)=m-n\sqrt3=(m+n\sqrt3)^{-1}.                \tag{96.H23}
\]

The explicit member \((a,b)=(25,27)\), \((m,q,n)=(26,1,15)\), has
\(F=26-15\sqrt3\).  Its reciprocal interval contains \(k=J/32\), since

\[
 {3\sqrt3-5\over10}<{1\over32}
 <{3\sqrt3-5\over3\sqrt3}.                        \tag{96.H24}
\]

Choose a lawful populated lift scale with fixed \(L\geq A\).  As
\(J\to\infty\), this block has \(D\asymp2\), a long nonempty \(k\)-fiber,
and

\[
 \rho\asymp {AJ\over L^3}\longrightarrow\infty.   \tag{96.H25}
\]

Thus the hard side contains blocks with no growing \(q\)-length but an
arbitrarily large requested gain.

This survives the fourth-power control.  Take \(X=T^4\), \(J=T^2\),
\(32\mid T\), and \(k=T^2/32\).  Then

\[
 {\Lambda\over k}=32(26-15\sqrt3)T^2.              \tag{96.H26}
\]

Weyl's polynomial equidistribution theorem gives infinitely many such
\(T\) for which (96.H26) lies in either prescribed fixed strict metric
annulus.  This use is qualitative for fixed \(R\); it gives no shrinking
window rate and no lower bound for \(\mathfrak C^\circ\).  Primitive square
rays can have exact fourth-power resonances, but they are prior owners.
For a nonsquare ray an exact centre can be forced at a chosen real \(X\),
but the punctured \(W_R\) and the exact-centre owner remove it.  Neither
owner may be reinserted into a shifted correlation.

## 4. First doubtful or unproved step

The smallest honest survivor is not a scalar spacing estimate, nor merely
the same-\(m\) correlation (96.H11).  To state the actual cross-\(m\)
object, let \(\epsilon_m\in\{0,1\}\) be determined by
\(\epsilon_m\equiv1-m\pmod2\), zero-extend all fibers, and put

\[
 \mathcal Z_n:=
 \sum_m(-1)^{\epsilon_m}
 \mathcal F_{m,\epsilon_m+2n},
 \qquad
 \mathfrak Q_{A,D,K,G,R}=\sum_n\mathcal Z_n,       \tag{96.H27}
\]

and

\[
 \widetilde{\mathcal C}_h
 :=\sum_n\mathcal Z_{n+h}\overline{\mathcal Z_n}
 =\sum_{m,m',n}(-1)^{\epsilon_m+\epsilon_{m'}}
 \mathcal F_{m,\epsilon_m+2n+2h}
 \overline{\mathcal F_{m',\epsilon_{m'}+2n}},
 \tag{96.H27a}
\]

\[
 \widetilde{\mathcal V}_H:=
 H\sum_n|\mathcal Z_n|^2
 +2\Re\sum_{1\leq h<H}(H-h)
       \widetilde{\mathcal C}_h.                  \tag{96.H27b}
\]

A sufficient theorem-shaped input for a single block is

\[
 {D+H\over H^2}\,\widetilde{\mathcal V}_H
 \ll_\varepsilon L^4X^\varepsilon                 \tag{96.H28}
\]

for some admissible averaging length \(H\), with the literal residual masks,
both moving \(k\)-intervals and lift sets, all stars and entry/exit samples,
and the complete products of density and discrepancy modes.  Equation
(96.H17) would then give the target-sized block bound.  Logarithmic block
summation would still have to be checked separately.

On the same-\(m\) diagonal inside (96.H27a), the character factor is one by
(96.H4); only the genuinely cross-\(m\) terms retain a possible sign
\((-1)^{\epsilon_m+\epsilon_{m'}}\).  On \(\rho>D\), (96.H28) cannot be a
theorem uniform over arbitrary bounded coefficients and justified only by
the \(q\)-A-process: the diagonal floor and (96.H21) forbid that.  The
missing input must exploit this cross-\(m\) sign or another physical
variable together with the actual symbol.  It must also explain why the
same claim is false for the unsigned and phase-aligned coefficient
analogues.

No audited source supplies (96.H28).  The closest cone result genuinely
allows a null direction, but it estimates an \(L^p\) extension norm on a
specific separated rectangular cone sampling.  The present saddle phases
sample essentially a fixed dual ray at fixed \(X\), while their coefficients
and supports depend jointly on \((m,q,k,g)\).  Converting this into the
required multi-parameter norm without losing the fixed-point problem or the
density term is precisely an unproved theorem, not an invocation of existing
decoupling.  Similarly, a double large sieve merely replaces the desired
bound by two close-pair energies; it does not bound those energies at the
\(\rho^{-1}\) squared scale.

## 5. Required control tests, outcomes, and primary-source hypothesis map

| Required control | Exact test | Outcome |
|---|---|---|
| `m_q_parity_and_coprimality` | Derived (96.H2), (96.H14), and the legal shift \(q\mapsto q+2h\). | Pass; the character is constant on every fixed-\(m\) legal row. |
| `chi4_equals_minus_one_power_q` | Proved (96.H15) before differencing. | Pass algebraically; it fails as a shifted cancellation mechanism by (96.H4). |
| `moving_k_interval` | Used the literal open endpoints (96.H18) and their \(O(Jh/A)\) displacement. | Pass as bookkeeping; a shifted correlation is not rectangular and has boundary modes. |
| `entry_exit_and_stars` | Used zero extension only; no endpoint, floor, star, collar, or transition was smoothed away. | Pass for the no-go; no cancellation estimate follows. |
| `density_discrepancy_jointness` | Expanded only the product to display (96.H19). | Discrepancy-only closure fails; the density--density mode survives with character product \(1\). |
| `square_ray_prior_owner` | Kept all primitive square rays outside \(\mathscr L_{A,D}\). | Pass; their exact fourth-power resonances cannot be borrowed. |
| `exact_nonsquare_centre_owner` | Kept \(W_R(\Lambda/k)=0\) at exact centres and used the prior-owner mask in both shifted factors. | Pass; translation invariance is broken at the owner boundary. |
| `near_square_and_Pell` | Used all \((m-1,m+1)\) with even \(m\), and the fixed-\(q=1\) Pell family (96.H22). | Pass; these are primitive, odd, nonsquare, constant-sign, and have no growing \(q\)-fiber. |
| `fourth_power_metric_resonance` | Used (25,27), \(X=T^4\), \(k=T^2/32\), and (96.H26). | Pass qualitatively for strict metric recurrence at fixed \(R\); no coefficient lower bound or uniform shrinking-window claim. |
| `false_unsigned_and_arbitrary_coefficients` | Replaced the actual symbol only in the hostile analogue by phase-aligned coefficients supported on one legal \(q\) per row. | Any coefficient-uniform \(\rho^{-1/2}\) q-dispersion theorem is false on \(\rho>D\); this does not refute the genuine symbol. |
| `rho_gain_and_block_sum` | Compared the coefficient-blind square-root ceiling \(D^{-1/2}\) with \(\rho^{-1/2}\). | Diagonal/absolute-correlation closure fails on \(\rho>D\); a stronger signed actual-correlation theorem remains possible.  No block sum or target-safe complement is proved here. |
| `transform_self_return` | Performed the exact step-two character correlation and Poisson-frequency check. | Exact character self-return: the zero mode remains.  No claim is made that the entire actual-symbol operator has been diagonalized. |
| `both_orientations_and_outer_real_part` | The calculation is termwise; under \(q\mapsto-q\) the parity is unchanged, and conjugation preserves (96.H4). | Pass; neither orientation supplies a missing sign, and no positivity of \(2\Re\) is assumed. |
| `downstream_scope` | Compared only with the canonical residual hard top cone. | No inference to other M2 packets, M9-M2, M9, endpoint uniformity, or the quarter target. |
| `primary_source_hypothesis_map` | Audited the seven primary sources below. | No literal source match for (96.H28) or \(\rho^{-1/2}\). |

The exact primary-source map is:

| Primary source | Theorem and hypotheses audited | Literal map and verdict |
|---|---|---|
| E. Bombieri and H. Iwaniec, *On the order of \(\zeta(1/2+it)\)*, Lemma 2.4, pp. 452--454 ([primary Numdam PDF](https://www.numdam.org/article/ASNSP_1986_4_13_3_449_0.pdf)) | Two finite point sets in \(\mathbb R^K\), factorized coefficients \(a(x)b(y)\), phase \(e(x\cdot y)\), coordinate boxes \(|x_j|<X_j,|y_j|<Y_j\), and weighted close-pair energies at reciprocal coordinate scales.  The conclusion is a product of those two close-pair energies and \(\prod_j(1+X_jY_j)\). | A Taylor or cone parametrization would still have to separate the complete coefficient into the two point sets.  Here the reciprocal interval, \(W_R\), lift set, and \(\mathfrak C^\circ\) depend jointly on the variables.  Even after a formal dot-product lift, the theorem exports the problem to close-pair energies containing the diagonal, short-\(q\), and Pell fibers; it supplies no \(\rho^{-1/2}\) estimate for them. |
| W. Duke, J. Friedlander, and H. Iwaniec, *Bilinear forms with Kloosterman fractions*, Theorems 1--3 and weighted (1.7)--(1.8), pp. 23--25 ([author-hosted primary PDF](https://www.math.ucla.edu/~wdduke/preprints/bilinear.pdf)) | The form is \(\sum_{(m,n)=1}\alpha_m\beta_ne(a\bar m/n)\), with fixed positive integer \(a\), dyadic \(m,n\), modular inverse \(m\bar m\equiv1\pmod n\), and factorized coefficients.  The weighted extension requires a smooth \(F(m,n)\) with \(|F^{(j,k)}|\ll\eta^{j+k}m^{-j}n^{-k}\) for \(0\le j,k\le2\). | \(e(r\Lambda/k)\) is not a modular-inverse phase with fixed integral numerator; \(\Lambda\) moves irrationally on nonsquare rays.  Floors, stars, moving endpoints, owner masks, and the joint integral do not factor as \(\alpha_m\beta_nF(m,n)\).  The theorem is inapplicable. |
| J.-M. Deshouillers and H. Iwaniec, *Kloosterman sums and Fourier coefficients of cusp forms*, especially Theorem 2 and Sections 1.1--1.4, pp. 223--237 ([primary journal DOI](https://doi.org/10.1007/BF01390728)) | At fixed \(\Gamma_0(q_0)\) and cusp, Theorem 2 is a spectral large sieve for a common complex sequence \(a_n\) against holomorphic/Maass/Eisenstein Fourier coefficients, with spectral cutoff and bound of the form \(K^2+\mu(\mathfrak a)N^{1+\varepsilon}\).  The trace inputs are generalized Kloosterman sums over their allowed moduli with admissible Bessel test functions. | The primitive separation \(q\) and reciprocal mode \(k\) are not Kloosterman moduli, and no complete modular-inverse sum or fixed automorphic level occurs in (96.H9).  The actual coefficient is row-dependent, not one common \(a_n\).  Möbius completion of (96.H16) does not create the required Kuznetsov family.  All trace, level, cusp, test-transform, and common-coefficient hypotheses therefore fail before a spectral bound can be invoked. |
| D. R. Heath-Brown, *A new form of the circle method, and its application to quadratic forms*, Theorems 1--2 ([author-deposited primary record and PDF](https://ora.ox.ac.uk/objects/uuid%3Abbd3c62f-f010-44b5-8be5-87e903fb0084)) | Theorem 1 is an exact delta-symbol identity for an **integer** \(n\), using coprime residue classes modulo \(q\) and a smooth kernel \(h(q/Q,n/Q^2)\).  Theorem 2 applies that identity and Poisson summation to a polynomial equation with a fixed smooth compactly supported weight, producing complete arithmetic sums and oscillatory integrals. | The strict metric condition is an inequality in the generally irrational number \(XF(m,q)/k\), not an integer polynomial equality.  Applying the delta symbol merely to \(q'-q-2h=0\) re-encodes an equality already present and gives no cancellation.  No complete sum or integral estimate in the theorem includes the moving actual symbol, and the delta identity itself supplies no \(\rho\)-gain. |
| O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials*, Theorem 2, §5 ([author-hosted primary PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf)) | For fixed real \(\alpha\ne0,1\), \(M\ge1\), and \(\delta>0\), it counts unweighted quadruples \(M<m_i\le2M\) satisfying \(|m_1^\alpha+m_2^\alpha-m_3^\alpha-m_4^\alpha|\le\delta M^\alpha\), with \(\ll_\varepsilon M^{2+\varepsilon}+\delta M^{4+\varepsilon}\). | With \(\alpha=1/2\) it can majorize an unweighted four-radical near-collision count after discarding arithmetic and coefficient structure.  It does not include \(k^{-1}\), the moving \(k,g\) fibers, the punctured metric coefficient, or the signed actual symbol.  Its unavoidable diagonal \(M^{2+\varepsilon}\) contains the controls above.  It is a positive spacing input, not (96.H28), and supplies no stated \(\rho^{-1/2}\). |
| X. Li and X. Yang, *An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem*, Proposition 3.1 and Theorem 4.2 ([primary arXiv v2 HTML](https://arxiv.org/html/2308.14859v2)) | Proposition 3.1 treats the specific cone extension \(\sum_{k\sim K,l\sim L}a_{kl}e(lx_1+klx_2+l\sqrt kx_3)\), \(|a_{kl}|\le1\), \(1\le L<K\le\eta^{-1}\le KL\), \(4\le p\le4.5\), and \((L/K)^{(p-2)/(p-4)}\le\eta\).  It explicitly resolves circular and null cone directions.  Theorem 4.2 treats the separably weighted sum \(\sum_hg(h/H)\sum_mG(m/M)e((hT/M)F(m/M))\), with \(g,G\) of bounded variation, \(F\in C^3[1,2]\), two-sided bounds for \(|F^{(r)}|\), \(r=1,2,3\), \(|F'F'''-3(F'')^2|\gg1\), and all Case A/B parameter inequalities (4.4)--(4.11). | This source shows that a radial Hessian null direction is not, by itself, fatal: cone decoupling handles one.  But the current frequency samples, fixed-\(X\) evaluation, coprimality/parity mask, independently moving \(k,g\) fibers, and complete coefficient do not have the displayed cone-extension or separably weighted double-sum form.  None of the derivative and Case A/B hypotheses has been mapped to all actual fibers.  The v2 Case-A threshold inconsistency already recorded in the selected Round-92 source review is an additional guardrail.  Structural analogy is not theorem applicability. |
| H. Weyl, *Über die Gleichverteilung von Zahlen mod. Eins*, Satz 9 ([primary DOI](https://doi.org/10.1007/BF01475864), [open primary scan](https://zenodo.org/records/2425535/files/article.pdf)) | A real polynomial with an irrational nonconstant coefficient is uniformly distributed modulo one; the test interval is fixed while the averaging length tends to infinity. | Applies to (96.H26), including \(T\) restricted to multiples of 32, and proves only the qualitative fourth-power recurrence control.  It gives no rate uniform in \(R\), no fixed-\(X\) energy estimate, and no actual-coefficient cancellation. |

## 6. Dependencies and exact artifacts used

The internal derivation used only the selected task context:

- `protocol.md`, for evidence, source-audit, and no-promotion rules;
- `state/active_campaign.yml`, for the frozen Round-96 target, capacity,
  controls, scope, and assigned report path;
- `rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/derivation_packet.md`,
  for (96.1)--(96.13), the actual coefficient, and prior owners;
- `rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md`,
  for the exact hard-block and one-count assembly;
- `rounds/codex-managed/m9-canonical-core-formalization/reviews/conductor_round92_source_and_graph_hygiene.md`,
  for the existing Li--Yang/Xiao source guardrails and downstream hygiene;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reports/strict_metric_energy_hostile_source_audit.md`,
  for the already proved carrier return, the (25,27) Pell normalization,
  and the exact fourth-power recurrence setup;
- `strategy/conductor_0817_full_proof_strategy.md`, for the canonical M2
  false shadows, capacity discipline, and later-core scope;
- the task brief
  `rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/briefs/primitive_ray_q_hostile_source_audit.md`.

No sibling Round-96 report was read.  No shared state, synthesis,
validation matrix, or proof draft was edited.  No numerical experiment was
used.  The only external sources used are the seven primary works mapped in
Section 5; Weyl is used positively and only for a qualitative control, while
the other six are rejected after literal hypothesis comparison.

## 7. Recommended state effect

**Recommended effect: revise the route, retain the canonical target as open,
promote no estimate, and record the exact no-go.**

The graph should reject any candidate claim that
\(\chi_4(a)\chi_4(b)=(-1)^q\) alternates under an exact fixed-\(m\)
primitive-ray \(q\)-shift.  Legal shifts have step two and the character
autocorrelation is identically one.  It should also reject the claim that one
coefficient-blind diagonal/absolute-correlation \(q\)-A-process supplies
the full \(\rho^{-1/2}\) on all hard blocks: its square-root row gain is
only \(D^{-1/2}\), and fixed-\(q\)
near-square/Pell blocks occur with \(\rho>D\), including at fourth-power
values of \(X\).

The Hessian calculation should be retained with the correct qualification.
The complete physical and saddle phases have a radial null direction, so a
determinant-only multidimensional second-derivative argument is unavailable.
This is not a blanket rejection of cone decoupling: Li--Yang's cone input
does handle a null direction, but no literal map presently preserves the
moving actual symbol or produces the fixed-\(X\) signed bound.

The smallest honest survivor is (96.H28), or an equivalent direct theorem
for the complete cross-\(m\) autocorrelations (96.H27a), with density and
discrepancy joint, all moving fibers present, and actual-symbol cancellation
across an additional variable.  Such a theorem must state why the unsigned and
phase-aligned coefficient analogues fail and must overcome the short-\(q\)
range by genuine cross-\(m\), cross-\(k\), cross-\(g\), or profile structure.
No audited primary theorem supplies it.

Accordingly, `M9-M2-top-endpoint-density-discrepancy-energy`,
`M9-M2-top-endpoint-signed-cone`, and `M9-M2` remain open.  There is no new
target-safe polynomial range, no block-sum theorem, and no change to M9,
endpoint uniformity, or the Gauss-circle quarter target.
