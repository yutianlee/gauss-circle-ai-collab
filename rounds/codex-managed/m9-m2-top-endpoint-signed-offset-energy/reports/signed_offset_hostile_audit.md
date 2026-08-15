# Round 76 hostile/source audit: odd-lift resonance and endpoint Poisson seam

## 1. Result

The finite offset identity (76.2), the character identity (76.3), the
negative Poisson-mode orientation, the interior saddle, the Gaussian unit
in (76.8), and the algebraic gcd phase (76.14) are correct.  The proposed
gcd-lift saving is nevertheless **not promotable**.  There is one definite
parity error and one still-unproved analytic seam.

First, all lifts (g) are odd.  If

\[
 q=\frac{b-a}{2}\in\mathbb Z,
 \qquad
 \beta_{a,b,k}=\frac{X(\sqrt b-\sqrt a)^2}{4k},
 \qquad
 \alpha_{a,b,k}=\frac q2-\beta_{a,b,k},
\]

then on the admissible lattice

\[
 e(g\alpha_{a,b,k})=(-1)^q e(-g\beta_{a,b,k}),
 \qquad g\ {\rm odd}.                                      \tag{1.1}
\]

Thus the offset character is constant, not alternating, on each primitive
ray.  Consecutive lifts differ by (2), so their exact geometric ratio is

\[
 e(2\alpha_{a,b,k})
 =e\!\left(-\frac{X(\sqrt b-\sqrt a)^2}{2k}\right).          \tag{1.2}
\]

Consequently (76.17) is false: even for a genuinely step-(2) sampled-BV
symbol, the bulk resonance condition is

\[
 \boxed{\ \|2\alpha_{a,b,k}\|
   =\left\|\frac{X(\sqrt b-\sqrt a)^2}{2k}\right\|
   \lesssim G_{a,b}^{-1}.\ }                                \tag{1.3}
\]

It includes both integer and half-integer values of (alpha).  The packet's
(\|\alpha\|\lesssim G^{-1}) retains only one parity of the resonant
integers and incorrectly declares the other parity nonresonant.

This failure is exact, occurs strictly inside both \(m\)-endpoints, and
persists at perfect fourth powers with both actual spatial-profile factors
frozen at one.  Let \(T\) be any odd multiple of \(13\), and put

\[
 X=T^4,\quad J=T^2,\quad (a,b)=(81,121),\quad
 k=\frac{2J}{13}.
\]

Then \(k\) lies strictly in the saddle range,

\[
 \frac{J}{9}<\frac{2J}{13}<\frac{2J}{11},\qquad
 \frac{x_*}{g}=\frac{169}{4},
 \quad \frac b4<\frac{169}{4}<a,                            \tag{1.4}
\]

but

\[
 \alpha_{81,121,k}=10-\frac{13J}{2}\in\mathbb Z+\frac12.
                                                                    \tag{1.5}
\]

Here \(q_X=X/\lfloor\sqrt X\rfloor^2=1\), and the two top-\(M2\) profile
arguments at the saddle are

\[
 \sqrt{\frac{q_Xga}{4x_*}}=\frac9{13},\qquad
 \sqrt{\frac{q_Xgb}{4x_*}}=\frac{11}{13}.                  \tag{1.5a}
\]

Both lie strictly in the accepted frozen zone \(W=1\).  Hence
\(e(g\alpha)=-1\) for every odd \(g\), while the actual spatial-profile
product equals one.  Constant coefficients on an odd lift interval have
bounded step-\(2\) variation but add with full coherence while
\(\|\alpha\|=1/2\).  This is a direct counterexample to
every coefficient-blind shortcut based on (76.17).  It is not by itself a
lower bound for the actual energy: the remaining Vaaler/support factors
and the sum over the other primitive rays still matter.

Second, (76.8) is only the interior stationary term.  The packet has not
given an exact starred Poisson formula, the two half-endpoint corrections,
the incomplete Fresnel transitions, or an aggregate error theorem for the
actual amplitude.  A fixed-width collar is target-safe and the stationary
width is uniformly (O(1)), so this seam is plausibly repairable; it is not
proved by the displayed candidate formula.

The endpoint seam can be scoped sharply.  Fix an absolute integer
\(B_0\ge 3\).  In the original finite sum, put in the target-safe collar

\[
 0\le m-\left\lceil\frac{s}{4}\right\rceil\le 2B_0
 \quad\hbox{or}\quad
 0\le h-m\le 2B_0.                                         \tag{1.6}
\]

There are \(O(B_0L^2)=O(L^2)\) bounded summands in these strata.  The two
full endpoint samples, all half-star corrections, and every lower or upper
incomplete-Fresnel transition must be kept grouped with this collar; they
may not be summed alias by alias.  On the complement one can insert smooth
cutoffs based on the real affine distances \(x-s/4\) and \(h-x\).  The
resulting lattice correction is still supported in (1.6), while the
retained continuous symbol contains no ceiling parity.

Indeed, before this extraction, for odd \(g,b\),

\[
 \left\lceil\frac{gb}{4}\right\rceil
 =\frac{gb}{4}+\frac12+\frac{\chi_4(gb)}4.                  \tag{1.7}
\]

Thus an unextracted lower Fresnel transition can have a genuine
\(g\bmod4\) component.  If one insists on transforming that sharp stratum,
only step-\(4\) BV is structurally safe and its conservative resonance is

\[
 \|4\alpha\|\lesssim G^{-1}.                               \tag{1.8}
\]

After the lawful collar extraction (1.6), however, the retained hard
interior has no mod-\(4\) ceiling factor.  It is structurally a step-\(2\)
sampled symbol, so its sharp safe resonance is exactly (1.3).  A
quantitative \(V_2\) bound for the actual stationary corrections remains
to be proved.  The larger set (1.8) belongs only to an unextracted sharp
endpoint/Fresnel representation; it is not an additional interior
resonance.

The graph-worthy result is therefore a no-go: **the alternating offset
character supplies no cancellation in the gcd-lift direction, and the
rank-one lift transform reduces to an ordinary odd-lattice Fourier
resonance with exact perfect-power coherent rays.**

## 2. Exact statement and hypotheses

Assume (X) is sufficiently large, (J=\sqrt X), and
(1\le L\le H\le J^{1/2}).  Start with the accepted finite energy (76.1)
and its exact positive-offset expansion (76.2).  Fix an ordered pair
(h<s=h+2r) in the actual odd support and set

\[
 g=(h,s),\qquad h=ga,\qquad s=gb,qquad (a,b)=1.
\]

Then (g,a,b) are odd, (a<b), and the parametrisation is unique.  Put

\[
 \Delta=\sqrt b-\sqrt a,qquad q=\frac{b-a}{2},qquad
 C=J\sqrt g\,\Delta.
\]

For a positive integer (k), define

\[
 \lambda_{a,b,k}=\frac{X\Delta^2}{4k^2},\qquad
 x_*=g\lambda_{a,b,k},\qquad
 \beta_{a,b,k}=\frac{X\Delta^2}{4k},
 \qquad \alpha_{a,b,k}=\frac q2-\beta_{a,b,k}.              \tag{2.1}
\]

The exact saddle condition is

\[
 \left\lceil\frac{gb}{4}\right\rceil
 \le g\lambda_{a,b,k}\le ga.                              \tag{2.2}
\]

Away from the lower (O(1))-collar, this is equivalent to
(b/4<\lambda_{a,b,k}\le a), with a stated margin.  The corresponding
interior Poisson term has phase (e(g\alpha_{a,b,k})), Gaussian unit
(e(1/8)), and leading modulus

\[
 \frac{C}{\sqrt2\,k^{3/2}}
 =\frac{J\sqrt g\,\Delta}{\sqrt2\,k^{3/2}}.                 \tag{2.3}
\]

Let \(I\) be any interval of admissible lifts and let
(I_{\rm odd}=I\cap(2\mathbb Z+1)), with
(N=|I_{\rm odd}|\asymp G_{a,b}) when nonempty.  For a sequence (B(g))
on this lattice define

\[
 V_2(B;I)=|B(g_0)|+
 \sum_{\substack{g,g+2\in I_{\rm odd}}}|B(g+2)-B(g)|.       \tag{2.4}
\]

The exact odd-lift Abel bound is

\[
 \left|\sum_{g\in I_{\rm odd}}B(g)e(g\alpha)\right|
 \ll V_2(B;I)
 \min\!\left(N,\frac1{\|2\alpha\|}\right).                \tag{2.5}
\]

Therefore a nonresonant lift estimate requires both

\[
 V_2(B_{a,b,k};I)\ \hbox{bounded at the claimed actual-symbol scale}
 \quad\hbox{and}\quad
 \|2\alpha_{a,b,k}\|\gg G_{a,b}^{-1}.                     \tag{2.6}
\]

Neither condition may be replaced by coefficient size alone.  If the exact
sharp endpoint symbol is controlled only separately on
\(g\equiv1,3\pmod4\), define \(V_4\) on those two progressions.  Splitting
them yields instead

\[
 \left|\sum_{g\in I_{\rm odd}}B(g)e(g\alpha)\right|
 \ll (V_{4,1}+V_{4,3})
 \min\!\left(N,\frac1{\|4\alpha\|}\right),                 \tag{2.7}
\]

up to harmless absolute constants.  Thus (1.8), not (76.17), is the safe
resonance set for an unextracted sharp-endpoint transform.  Once the primal
collar (1.6) is grouped into its \(O(L^2)\) contribution and the retained
symbol uses the real affine cutoffs (3.16), the hard interior is step-\(2\)
and (1.3) is the sharp safe resonance.

No assertion in this report bounds the sum of all resonant
\((a,b,k)\), or the actual energy.  The preferred exact survivor is the
collar-extracted interior with its actual stationary symbol and the
channel (1.3).  If one instead insists on a full sharp transform, its
Fresnel symbol must retain the larger endpoint-only set (1.8).  Either
form still requires an \(L^2X^\varepsilon\) coefficient-weighted aggregate
bound.

## 3. Proof or derivation

### Finite offset algebra

Expanding the accepted row energy gives, for (s>h),

\[
 e(J\sqrt{hm})\overline{e(J\sqrt{sm})}
 =e\bigl(-J(\sqrt s-\sqrt h)\sqrt m\bigr).
\]

The common row constraints are

\[
 m\le h<s,qquad h\le4m,qquad s\le4m,
\]

so the stronger lower constraint is
(m\ge\lceil s/4\rceil), and the upper constraint is (m\le h).
Pairing the two orientations gives the factor (2\Re).  Since (h,s)
are odd, write (s=h+2r).  Directly from
(\chi_4(n)=(-1)^{(n-1)/2}) on odd integers,

\[
 \chi_4(h)\chi_4(s)=(-1)^{(s-h)/2}=(-1)^r.                 \tag{3.1}
\]

This proves (76.2)--(76.5).  There are (O(L^2)) ordered pairs
((h,s)).  Hence two endpoint samples, or any fixed number of samples at
each edge, have (O(L^2)) absolute capacity.  A fixed (r) has (O(L^2))
capacity, but summing this over (O(L)) offsets is not target-sized.

### Poisson sign, saddle, Gaussian, and endpoints

Use

\[
 \widehat F(n)=\int_{\mathbb R}F(x)e(-nx)\,dx.
\]

For the starred sharp interval, Poisson gives integrals with phase
(-C\sqrt x-nx).  A saddle is possible only for (n=-k<0); its phase is

\[
 \phi_k(x)=-C\sqrt x+kx,qquad
 x_*=\frac{C^2}{4k^2}.                                     \tag{3.2}
\]

At the saddle,

\[
 \phi_k(x_*)=-\frac{C^2}{4k},qquad
 \phi_k''(x_*)=\frac{2k^3}{C^2}=\frac{k}{2x_*}>0.           \tag{3.3}
\]

With (e(z)=e^{2\pi iz}), positive quadratic curvature contributes
(e(1/8)), and

\[
 \phi_k''(x_*)^{-1/2}=\frac{C}{\sqrt2\,k^{3/2}}.            \tag{3.4}
\]

Thus the sign, phase, Jacobian, and constant in the interior formula
(76.8) pass.

For integer endpoints (A=\lceil s/4\rceil) and (B=h), however, the
unstarred sum is the starred sum plus
(\tfrac12F(A)+\tfrac12F(B)).  A saddle meeting an endpoint contributes
an incomplete Fresnel factor, not the full (e(1/8)) Gaussian.  The local
stationary width is

\[
 \sigma_k=\phi_k''(x_*)^{-1/2}=\sqrt{\frac{2x_*}{k}}.
\]

On the active top range, (x_*\ll L) and
(k\gg J/L), whence

\[
 \sigma_k\ll \frac{L}{\sqrt J}\le1.                       \tag{3.5}
\]

This confirms that a fixed original (m)-collar can absorb every endpoint
transition at target capacity.  It does not supply the missing identity:
one must actually extract that collar, choose the interior cutoff, and sum
all nonstationary aliases and stationary remainders.  For a sharp cutoff,
termwise endpoint integration by parts produces non-absolutely summable
(1/n) tails; the starred formula and Fresnel pieces cannot be omitted.

### Gcd uniqueness and the parity correction

The representation

\[
 (h,s)=(ga,gb),\qquad g=(h,s),\qquad(a,b)=1
\]

is one-to-one.  Since (h,s) are odd, (g,a,b) are odd.  Conversely,
odd coprime (a<b) and an odd (g) give one ordered pair, subject to the
support and cone restrictions.  There is no further gcd multiplicity, but
an interval of Euclidean length (G) contains only (G/2+O(1)) admissible
lifts.

With (q=(b-a)/2),

\[
 r=gq,qquad (-1)^r=(-1)^{gq}=(-1)^q                       \tag{3.6}
\]

because (g) is odd.  Also

\[
 \frac{C^2}{4k}=g\frac{X(\sqrt b-\sqrt a)^2}{4k}=g\beta.
\]

Combining (3.6) with the stationary phase gives (1.1).  If
(g=g_0+2n), the ratio of consecutive terms is

\[
 \frac{e((g+2)\alpha)}{e(g\alpha)}=e(2\alpha)
 =e(q-2\beta)=e(-2\beta),                                  \tag{3.7}
\]

which proves (1.2).  The geometric partial sums are bounded by

\[
 \left|\sum_{n=u}^{v}e(2n\alpha)\right|
 \ll \min(v-u+1,\|2\alpha\|^{-1}).                         \tag{3.8}
\]

Partial summation gives (2.5).  Taking (B(g)\equiv1) shows that this is
sharp and that (V_2) alone gives no saving at (1.3).

### Exact fourth-power hostile control

For the parameters in (1.4), \(a,b\) are odd and coprime and
\(b/a=121/81<2\).  The divisibility \(13\mid T\) makes
\(k=2T^2/13\) integral.  The exact saddle calculation is

\[
 \frac{x_*}{g}
 =\frac{T^4(11-9)^2}{4(2T^2/13)^2}
 =\frac{169}{4}.
\]

For every odd \(g\ge1\),

\[
 \left\lceil\frac{121g}{4}\right\rceil
 <\frac{169g}{4}<81g,                                      \tag{3.9}
\]

so this is not an endpoint or Fresnel artefact.  Furthermore,

\[
 \frac{X(\sqrt b-\sqrt a)^2}{2k}=13J\in2\mathbb Z+1,
 \qquad
 2\alpha=20-13J\in2\mathbb Z+1.                           \tag{3.10}
\]

Because \(J=T^2\) is odd, \(\|2\alpha\|=0\),
\(\|\alpha\|=1/2\), and all odd lifts are coherent.  Moreover
\(q_X=1\), and at \(m=x_*=169g/4\) the two actual spatial-profile factors
are exactly

\[
 W\!\left(\sqrt{\frac{81g}{4x_*}}\right)=W(9/13)=1,\qquad
 W\!\left(\sqrt{\frac{121g}{4x_*}}\right)=W(11/13)=1.       \tag{3.10a}
\]

Indeed \(2/3<9/13<11/13<1\), strictly inside the accepted \(W=1\)
plateau.  Thus the former \(7/11\) transition ambiguity is absent.  In
the standard dyadic annulus \(L\le h,s\le2L\), the interval

\[
 \frac{L}{81}\le g\le\frac{2L}{121}                        \tag{3.11}
\]

has length \(41L/9801\), hence contains \(\asymp L\) odd lifts.  This
establishes a macroscopic coefficient-blind countermodel on an admissible
interior primitive ray whose spatial profile is the actual frozen profile,
not an arbitrary replacement.  For the repository's actual finite
frequency support, only the lifts on which its remaining cutoff is nonzero
are retained.

The same computation gives the near-resonance scale.  A perturbation is
coherent throughout (G) lifts whenever

\[
 \left\|\frac{X(\sqrt b-\sqrt a)^2}{2k}\right\|
 \lesssim G^{-1}.                                           \tag{3.12}
\]

Real curvature in (a,b) does not remove these prescribed-centre integer
windows.

### Exact ceiling parity and the required actual-symbol BV

For odd \(n\), direct inspection modulo \(4\) gives

\[
 \left\lceil\frac n4\right\rceil
 =\frac n4+\frac12+\frac{\chi_4(n)}4.
\]

Taking \(n=gb\) proves (1.7).  Consequently the lower saddle distance in
the unextracted sharp transform is

\[
 x_*-\left\lceil\frac{gb}{4}\right\rceil
 =g\left(\lambda_{a,b,k}-\frac b4\right)
  -\frac12-\frac{\chi_4(g)\chi_4(b)}4.                     \tag{3.13}
\]

When \(\lambda-b/4=O(G^{-1})\), this remains in the \(O(1)\) Fresnel
window for \(O(G)\) lifts and alternates with \(g\bmod4\).  Hence the exact
endpoint symbol can be written schematically as

\[
 B(g)=B_0(g)+\chi_4(g)B_1(g),                               \tag{3.14}
\]

where proving sampled BV for \(B_0,B_1\) is still required.  The first
part resonates at (1.3); because
\(\chi_4(g+2)=-\chi_4(g)\), the second can resonate when

\[
 \left\|2\alpha+\frac12\right\|\lesssim G^{-1},            \tag{3.15}
\]

equivalently when the quantity in (3.12) is near a half-integer.  Splitting
modulo \(4\) packages (1.3) and (3.15) into (1.8).

This mod-\(4\) channel is confined to the sharp endpoint seam.  To remove
it lawfully, choose fixed smooth functions \(U_-,U_+\) which vanish for
real distance at most \(B_0\) and equal one for distance at least
\(2B_0\), and multiply the continuous amplitude by

\[
 U_-\!\left(x-\frac{s}{4}\right)U_+(h-x).                  \tag{3.16}
\]

At integer \(m\), the difference between the original amplitude and
(3.16) is supported in the primal collar (1.6), so its complete
contribution is \(O(L^2)\) absolutely.  This grouped contribution includes
the endpoint samples and the lower and upper Fresnel transitions.  One
must not expand it into dual aliases and then take absolute values.

For the retained symbol, at the saddle \(h=ga,s=gb,x_*=g\lambda\), the
cutoff arguments are

\[
 g\left(\lambda-\frac b4\right),\qquad g(a-\lambda),        \tag{3.17}
\]

with no \(\chi_4(g)\) or ceiling term.  The leading factor (2.3), the two
sampled values
\(a(ga,g\lambda)\overline{a(gb,g\lambda)}\), the affine cutoffs, and every
interior stationary correction are therefore structurally smooth under
\(g\mapsto g+2\).  The retained hard symbol supports a step-\(2\) BV
statement, not merely a step-\(4\) statement.  Its required quantitative
bound is still absent from the packet and must be proved from the actual
symbol.  Bounds for \(\|B\|_\infty\) or its square mass do not imply
(2.4); artificial phase-conjugating or constant arrays satisfy ordinary
size budgets and defeat coefficient-blind conclusions.

### Rank one and self-return

Put

\[
 F(h,s)=(\sqrt s-\sqrt h)^2=h+s-2\sqrt{hs}.
\]

Its Hessian is

\[
 \nabla^2F=
 \frac12
 \begin{pmatrix}
  \sqrt{s}\,h^{-3/2}&-(hs)^{-1/2}\\
  -(hs)^{-1/2}&\sqrt{h}\,s^{-3/2}
 \end{pmatrix},                                             \tag{3.18}
\]

whose determinant is zero and whose null vector is ((h,s)).  The linear
term ((s-h)/4) has zero Hessian, so the same is true of (\Theta_k).
Indeed

\[
 \Theta_k(ga,gb)=g\alpha_{a,b,k}.                           \tag{3.19}
\]

Poisson summation in the radial variable is therefore just Fourier
analysis of the sampled lift symbol at the frequency (1.2).  It detects
the resonances (1.3), or (1.8) after a mod-\(4\) split; it does not create a
second curvature gain.  At exact resonance its zero-frequency mass is the
sum of the actual lift symbol.  This is the precise rank-one/self-return
obstruction.

### Primary-source applicability

No external theorem is needed for (2.5): it is the exact geometric-series
identity followed by Abel summation.  None of the primary results suggested
by the earlier method review supplies the missing resonant aggregate:

- [Kowalski--Robert--Wu, Proposition 5](https://ems.press/content/serial-article-files/38194?nt=1)
  assumes a separable bilinear form
  (\sum_{m\asymp M}\sum_{n\asymp N}\varphi_m\psi_n
  e(\mathcal X m^\mu n^\nu/(M^\mu N^\nu))), with bounded independent
  coefficient sequences and (mu,\nu\notin\{0,1\}).  The survivor here
  has the coprimality condition ((a,b)=1), a third varying integer (k),
  a prescribed modular resonance of ((\sqrt b-\sqrt a)^2/k), and an
  actual lift symbol.  Proposition 5 is not directly applicable and, in
  the already lawful pre-gcd separable use, retains the positive power
  loss recorded in the selected Round-75 audit.
- [Robert--Sargos, Theorem 2](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf)
  counts four variables for which
  (m_1^\mu+m_2^\mu-m_3^\mu-m_4^\mu) lies in a short interval around
  zero.  It has neither the prescribed integer centre in (3.12), the
  denominator (k), the primitive-pair condition, nor the moving lift
  symbol.  It can be an ingredient only after a new reduction that audits
  all of those hypotheses; it does not bound the present survivor.
- [Bombieri's separated-point large sieve](https://doi.org/10.1112/S0025579300005313)
  requires a positive spacing parameter for the points modulo one.  The
  fourth-power family (3.10) has exact collisions with the integer lattice,
  so no uniform positive separation exists.  Grouping collisions leaves
  their coefficient-weighted multiplicity, which is exactly the open
  resonance capacity.
- [Huxley--Watt](https://doi.org/10.1112/plms/s3-57.1.1) assumes a smooth
  phase with specified nonvanishing derivative conditions.  The radial
  phase (3.19) is linear and all derivatives of order at least two vanish.
  Its exact estimate is (3.8); the theorem supplies no gain at (1.3).
- [Bettin--Chandee](https://arxiv.org/abs/1502.00769) estimates trilinear
  Kloosterman fractions (e(a\overline m/n)) with modular inverses and
  associated coprimality and norm hypotheses.  The phase in (3.12) is an
  ordinary real algebraic quotient, not a modular inverse.
- [Deshouillers--Iwaniec](https://doi.org/10.1007/BF01390728) treats
  complete Kloosterman sums through spectral averaging.  The present
  primitive-ray sum contains no completed Kloosterman family, modulus
  average, or matching spectral coefficients.  Producing those objects
  would be an additional transform, and the rank-one direction already
  shows that radial Poisson alone merely returns the resonance.

Thus no cited exponent-pair, spacing, large-sieve, or spectral theorem has
both the hypotheses and conclusion required for the complete actual-symbol
resonance sum.

## 4. First doubtful or unproved step

In the order of the packet, the first unproved analytic step is the use of
(76.8) as though it were a complete transform of the sharp finite (m)-sum.
The displayed expression is the correct full-Gaussian interior main term,
but it does not state the starred Poisson convention, the two half-endpoint
samples, the incomplete Fresnel kernels, the nonstationary aliases, or a
summed remainder for the actual amplitude.  Equation (3.5) shows why a
fixed collar should make a target-safe repair possible; the repair still
has to be written and proved.

The first **false** step is (76.17).  Equations (3.6)--(3.8) show that odd
lifts sample with step \(2\), so \(\|2\alpha\|\), not \(\|\alpha\|\), is
the lawful bulk denominator.  Equations (3.9)--(3.10a) give an exact
interior perfect-fourth-power counterexample with both actual \(W\)-factors
equal to one.  The primal collar (1.6) and
real-affine cutoff (3.16) remove every ceiling/Fresnel parity stratum at
\(O(L^2)\), leaving a structurally step-\(2\) hard interior.  If this
extraction is not performed, (3.13)--(3.15) show that only step-\(4\) BV is
safe and the larger endpoint resonance (1.8) must be retained.

After these repairs, the first genuinely power-saving open step is the
coefficient-weighted total of the exact resonant channels.  Neither a
geometric estimate away from resonance nor a count of primitive triples
alone controls the actual moving-symbol mass on resonance.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| External normalization | **Pass, scoped.** Formula (76.2) starts from the accepted normalized (a(h,m)); the Poisson calculation introduces only the internal (e(1/8)) and (2.3).  No Round-75 physical factor may be inserted a second time. |
| Exact ceiling, stars, and endpoints | **Finite identity passes; transform incomplete.**  The exact lower edge is \(\lceil s/4\rceil\).  An unstarred sum equals the starred Poisson sum plus half of each endpoint.  The primal strata (1.6), including both endpoint samples and all incomplete-Fresnel transitions, have \(O(L^2)\) grouped capacity. |
| Diagonal and fixed offsets | **Pass as capacity only.**  The diagonal and any fixed-width endpoint collar are (O(L^2)).  Each fixed offset is (O(L^2)), but taking absolute values over (O(L)) offsets is not target-sized. |
| Alternating character sign | **Pass with a decisive degeneration.**  (\chi_4(h)\chi_4(h+2r)=(-1)^r), but after (r=g(b-a)/2) it equals the constant ( (-1)^{(b-a)/2}) on all odd lifts. |
| Poisson orientation and Gaussian | **Pass for an interior saddle.**  The active mode is (n=-k); (x_*=C^2/(4k^2)), the phase is (-C^2/(4k)), curvature is positive, and the unit and modulus are (e(1/8)C/(\sqrt2k^{3/2})). |
| Endpoint Fresnel and error sum | **Scoped correction.**  Both fixed-width primal collars can be discarded together at \(O(L^2)\); real-affine smooth cutoffs then leave no ceiling parity in the hard interior.  Formula (76.8) still lacks the nonstationary-alias and stationary-remainder aggregation for that retained symbol. |
| Gcd parity and multiplicity | **Pass with correction.**  The primitive representation is unique; (g,a,b) are odd, and there is one ordered lift per odd (g), not per integer (g).  Thus the sample count is (G/2+O(1)) and the phase step is (2\alpha). |
| Linear lift phase | **Algebra passes; resonance criterion fails.**  (\Theta_k(ga,gb)=g\alpha), but (76.17) misses every half-integer (\alpha) resonance.  The correct bulk test is (1.3). |
| Actual moving symbol | **Structure corrected; bound unproved.**  After (1.6) and (3.16), the retained interior is structurally step-\(2\), but the packet gives no quantitative \(V_2\) bound for all actual stationary corrections.  Only an unextracted sharp Fresnel symbol requires the conservative step-\(4\) split.  Size or square mass is insufficient. |
| Rank-one self-return | **Pass as an obstruction.**  The Hessian determinant is zero with radial null vector.  Poisson in (g) is Fourier inversion of the lift profile and returns the integer/half-integer resonance; it is not an independent two-dimensional saving. |
| Perfect powers and resonance capacity | **Packet criterion fails with the actual spatial profile.**  Equations (1.4)--(1.5a) give an exact, strictly interior, perfect-fourth-power coherent ray with \(\|\alpha\|=1/2\) and both \(W\)-factors exactly one.  It falsifies coefficient-blind nonresonance; the remaining Vaaler/support weights and aggregate capacity remain open. |
| Source applicability | **Fail for the target.**  The audited primary theorems miss at least one exact hypothesis: separability, prescribed-centre resonance, positive spacing, nonvanishing higher derivatives, modular inverses, or a completed Kloosterman/spectral family. |
| Downstream scope | **Pass.**  The corrected parity lemma and the no-go do not prove (76.4), the hard top cone, full (M2), (M9), or the Gauss-circle exponent. |

No numerical computation was used.  All controls were algebraic, analytic,
or primary-source checks.

## 6. Dependencies and exact artifacts used

The local artifacts used were exactly the selected context:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/briefs/signed_offset_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/synthesis.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/reports/near_product_energy_hostile_audit.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/synthesis.md`.

No sibling Round-76 report, proof draft, validation matrix, legacy response,
or source card was read.  The external primary artifacts checked were the
six papers linked in Section 3: Kowalski--Robert--Wu Proposition 5,
Robert--Sargos Theorem 2, Bombieri's large sieve, Huxley--Watt's smooth
exponential-sum theorem, Bettin--Chandee's Kloosterman-fraction theorem,
and the Deshouillers--Iwaniec Kloosterman/spectral framework.

The accepted mathematical dependency is only the finite transposed-row
energy and its exact positive-offset identity.  The full endpoint Poisson
transform, the actual-symbol sampled-BV estimate, and the resonant aggregate
remain candidate evidence.

## 7. Recommended state effect

**Revise and retain open; do not promote (76.4).**

Retain (76.1)--(76.6), the interior sign/saddle/Gaussian calculation
(76.7)--(76.10), gcd uniqueness (76.11)--(76.13), and the algebraic formula
for \(\alpha\) in (76.14).  Replace the proposed resonance statement
(76.17) by the following exact parity lemma:

> For each primitive odd pair \(a<b\), the offset sign is constant along
> the odd lifts.  The lift-to-lift ratio is
> \(e(-X(\sqrt b-\sqrt a)^2/(2k))\).  Under a proved step-\(2\) sampled-BV
> bound for the actual interior symbol, the lawful resonance is
> \(\|X(\sqrt b-\sqrt a)^2/(2k)\|\lesssim G_{a,b}^{-1}\).
> If the lower endpoint parity has not been extracted, split \(g\bmod4\)
> and also retain the half-integer channel.

Record two rejected shortcuts:

1. \(\|\alpha\|\gg G^{-1}\) implies cancellation on odd lifts;
2. the factor \((-1)^r\) supplies an alternating character in the gcd-lift
   direction.

The exact fourth-power family (1.4)--(1.5a) is a permanent hostile control
for both claims.  It lies strictly inside the \(m\)-cone and has the actual
spatial-profile product \(W(9/13)W(11/13)=1\).  Constant step-\(2\)-BV
coefficients are already enough to falsify the shortcuts, so no
coefficient-blind large sieve, root-spacing bound, or geometric argument
may be used to discard these rays.

The smallest useful hard survivor first removes the two primal collars
(1.6) at \(O(L^2)\), inserts the real-affine cutoffs (3.16), and then sums
the complete retained actual symbol over \((a,b,k)\) satisfying (2.2).
Its odd \(g\)-sum has the form

\[
 (-1)^{(b-a)/2}
 \sum_{g\in I_{a,b}\cap(2\mathbb Z+1)}
 B_{a,b,k}(g)
 e\!\left(-g\frac{X(\sqrt b-\sqrt a)^2}{4k}\right),         \tag{7.1}
\]

with all exact multiplicities but no ceiling-parity component.  Prove the
interior endpoint/error theorem and a quantitative sampled \(V_2\) ledger
before separating (7.1) at the sharp safe condition

\[
 \left\|\frac{X(\sqrt b-\sqrt a)^2}{2k}\right\|
 \lesssim G_{a,b}^{-1}.                                    \tag{7.2}
\]

Then bound the coefficient-weighted resonant union, not merely its raw
cardinality.  If a future argument instead transforms the unextracted
sharp lower edge, it must retain step-\(4\) variation and (1.8); that is an
endpoint/Fresnel representation, not an extra resonance of the preferred
interior survivor.

Keep `M9-M2-top-endpoint-signed-cone`, `M9-M2`, `M9`, and the global
exponent open.  The finite transposed-row reduction remains accepted; this
audit supplies a corrected obstruction, not an energy estimate.
