## 1. Result

The finite Poisson formula (77.9) is correct provided the sum over
\(\nu\in\mathbb Z\) is read as a symmetric limit (or equivalently in
the usual distributional/Cesaro sense).  It is not an absolutely
convergent identity before the endpoint collars are inserted.  After
the collars are inserted, both endpoint values vanish and the
transformed series is absolutely convergent.

Subject to the fixed-symbol bounds stated in Section 2, both (77.16)
and (77.18) are correct.  In fact, for one dyadic block their right-hand
sides can be replaced by \(O_{M,\eta,\Phi,W}(L^2)\) and

\[
 \mathcal V_{a,b,k}
 \ll_{M,\eta,\Phi,W} {J\delta\sqrt G\over k^{3/2}},
\]

respectively; the displayed \(X^\varepsilon\) factors are harmless.
The key point for (77.18) is not a frozen first stationary term.  It is
the exact centred-square identity

\[
 -J\delta\sqrt u+ku+{X\delta^2\over4k}
 =k\left(\sqrt u-{J\delta\over2k}\right)^2,          \tag{R77.1}
\]

together with the slow \(g\)-variation of the actual symbol and the
fact that its two continuous collars have fixed width in the original
\(x\)-variable.  The top-range inequality \(L\le J^{1/2}\) makes that
fixed width at least as large as the stationary scale, uniformly at
saddle entry and exit.

There are two statement-level qualifications.  First, (77.9) needs the
summation convention just stated.  Second, the packet names the actual
profiles but does not state their support and derivative bounds.  Those
bounds are indispensable: without them a unit-scale oscillation in an
\(\eta_L\)-type coefficient gives the forbidden coefficient adversary
and makes (77.18) false.  Thus the result is a proof of the proposed
claims for the standard fixed smooth actual symbol, and a correction of
the literal packet statement by making those hypotheses explicit.

## 2. Exact statement and hypotheses

Let all definitions (77.1)--(77.17) be as in the derivation packet, and
make the following actual-symbol hypotheses explicit.

1. The dyadic localizer satisfies
   \(\operatorname{supp}\eta_L\subset[cL,CL]\) and
   \(\|\eta_L^{(j)}\|_\infty\ll_jL^{-j}\).  The actual odd support
   \(\mathscr H_L\) is the corresponding finite support, with all of
   its stated stars retained.  In particular, whenever a summand is
   nonzero, \(h,s,x\asymp L\).
2. \(\Phi\) and \(W\) are the fixed smooth profiles occurring in
   (77.1), with bounded derivatives of every required order.  Their
   arguments are not replaced by limiting values.  The numbers
   \(y,H,q_X\) retain their exact floors.  Notice directly from their
   definitions that \(q_X\asymp1\).
3. For a fixed primitive pair \((a,b)\), the actual admissible lifts
   form the stated step-two odd interval \(\mathcal G_{a,b}\), and on
   that interval \(g\asymp G\asymp L/b\).  A sharp support endpoint is
   allowed; it contributes only one endpoint jump.  No arbitrary
   lift-dependent coefficient is allowed.
4. \(M\ge1\) and \(\rho\) are fixed as in (77.12), and
   \(1\le L\le H\le J^{1/2}\).

Then the following statements hold.

* For integer \(A=\lceil s/4\rceil\) and \(B=h\),

  \[
  \sum_{m=A}^{B}F(m)
  ={F(A)+F(B)\over2}
   +\lim_{N\to\infty}\sum_{|\nu|\le N}
        \int_A^B F(x)e(-\nu x)\,dx.                 \tag{R77.2}
  \]

* With the complete integrals (77.13), and without inserting the
  external physical normalization,

  \[
  \mathcal O_L=\mathcal O_{L,\mathrm{stat}}^\circ
       +O_{M,\eta,\Phi,W}(L^2).                     \tag{R77.3}
  \]

* If \(k\) satisfies (77.14), then uniformly in the primitive pair,

  \[
  |\mathfrak B^\circ(g_{\max})|
  +\sum_{g,g+2\in\mathcal G_{a,b}}
       |\mathfrak B^\circ(g+2)-\mathfrak B^\circ(g)|
  \ll_{M,\eta,\Phi,W}{J\delta\sqrt G\over k^{3/2}}. \tag{R77.4}
  \]

These are precisely (77.16) and (77.18), with a stronger one-block
error and with their symbol hypotheses and Poisson convention made
explicit.  They say nothing about the size of the remaining reciprocal
sum.

## 3. Proof or derivation

For fixed odd \(h<s\le4h\), write

\[
 Q_{h,s}(x)=A_{h,s}(x)
 \rho\!\left({x-s/4\over M}\right)
 \rho\!\left({h-x\over M}\right),
 \qquad F^\circ(x)=Q_{h,s}(x)e(-C_{h,s}\sqrt x).
\]

The actual symbol and the dyadic support give, uniformly on
\([s/4,h]\),

\[
 \|Q_{h,s}\|_\infty\ll1,
 \qquad
 \|Q_{h,s}'\|_1+\|Q_{h,s}''\|_1+\cdots\ll_M1.       \tag{R77.5}
\]

In the bulk, each \(x\)-derivative costs \(L^{-1}\); in the two
collars it costs a fixed power of \(M^{-1}\), on a set of fixed length.
The \(W\)-derivatives obey the same estimate because their arguments
are exact smooth functions of \(h/x\) and \(s/x\).  No use of
\(q_X=1\) is made.

For odd \(s\),

\[
 \left\lceil{s\over4}\right\rceil-{s\over4}
 \in\left\{{1\over4},{3\over4}\right\}.
\]

Since \(M\ge1\) and \(\rho(t)=0\) for \(t\le1\), \(F^\circ\) vanishes
on a neighbourhood of both integer endpoints \(A\) and \(B\).
Replacing \(F\) by \(F^\circ\) in the primal sum changes at most
\(O_M(1)\) samples, including the full samples at both \(A\) and \(B\),
and hence costs \(O_M(1)\) for this pair.  There are \(O(L^2)\) ordered
pairs in a dyadic block, so all endpoint samples and both removed
collars have total capacity \(O_M(L^2)\).  The collar width has not been
allowed to grow.

The ordinary finite Poisson formula gives (R77.2).  The half endpoint
weights inside the Poisson integral sum, plus the displayed extra half
weights, give the full endpoint samples on the left.  For
\(F^\circ\), the endpoint terms are zero and repeated integration by
parts makes the mode series absolutely convergent.  Thus

\[
 \sum_{m=A}^{B}F^\circ(m)
 =\sum_{\nu\in\mathbb Z}\int_{s/4}^{h}
 Q_{h,s}(x)e(-C_{h,s}\sqrt x-\nu x)\,dx.            \tag{R77.6}
\]

It remains to show that all modes except the negative stationary ones
have \(O(1)\) total contribution for a fixed pair.  Put \(d=s-h\ge2\)
and

\[
 p(x)={C_{h,s}\over2\sqrt x},\qquad
 \mu={Jd\over L^2}.
\]

On the dyadic interval,

\[
 C_{h,s}\asymp {Jd\over\sqrt L},\qquad
 -p'(x)={C_{h,s}\over4x^{3/2}}\asymp\mu,
 \qquad \mu\gg {J\over L^2}\ge1.                  \tag{R77.7}
\]

For zero and positive Poisson modes the phase derivative has one sign
and size at least \(p(h)+\nu\asymp\mu L+\nu\).  For a negative mode
\(\nu=-k\), the derivative is \(k-p(x)\).  It vanishes in the geometric
interval exactly when

\[
 p(h)<k<p(s/4),                                      \tag{R77.8}
\]

which becomes (77.14) after \(h=ga,s=gb\).  If (R77.8) fails, the fixed
collar moves the support a distance \(M\) into the interval, so on the
support the derivative has the lower bound

\[
 |k-p(x)|\gg_M \mu+\operatorname{dist}
       \bigl(k,[p(h),p(s/4)]\bigr).                 \tag{R77.9}
\]

The same statement includes equality at either saddle boundary.
Twice applying the nonstationary operator
\((2\pi i f')^{-1}d/dx\), while retaining the linear growth
\(|f'(x)|\gg D+\mu\,\operatorname{dist}(x,\text{near collar})\), gives
for the mode at integer distance \(j\ge0\) from the geometric gradient
range

\[
 |I_j|\ll_M {1\over(\mu+j)^2}
              +{\mu\over(\mu+j)^3}.                \tag{R77.10}
\]

The collar derivative terms satisfy the same bound by (R77.5); the
bulk terms are smaller by powers of \(L^{-1}\).  Summing (R77.10) over
both negative tails is \(O_M(1)\).  The corresponding estimate with
\(\mu L+\nu\) sums the zero and positive modes to \(O_M(1)\).  This
proves that the zero, positive, negative nonstationary, and boundary
equality modes contribute \(O_M(1)\) per pair.  It also explains why a
fixed collar suffices: the smallest curvature is already \(\gg1\) in
the top range.

Now take a negative stationary mode and write uniquely
\(h=ga,s=gb\) as in (77.4).  Substituting \(x=gu\) into its complete
collared integral gives

\[
 \int A_{ga,gb}^\circ(x)e(-J\sqrt g\,\delta\sqrt x+kx)\,dx
 =e\!\left(-{gX\delta^2\over4k}\right)
       \mathfrak B_{a,b,k}^\circ(g).                \tag{R77.11}
\]

Multiplication by the parity sign and (77.6) yield

\[
 (-1)^r e\!\left(-{gX\delta^2\over4k}\right)
 =e(g\alpha).
\]

For \(g=2n+1\), the second identity in (77.6) gives

\[
 e(g\alpha)=e(\alpha)e(2n\alpha)
            =e(\alpha)e(-n\Lambda/k).              \tag{R77.12}
\]

Consequently the retained complete integrals are exactly (77.15), not
stationary approximations.  Combining (R77.6)--(R77.12), then summing
the \(O(1)\) remainders over \(O(L^2)\) pairs and applying the single
displayed \(2\Re\), proves (R77.3).  Every lower stationary term is
already inside the full integral \(\mathfrak B^\circ\); its omitted
remainder is therefore exactly zero.

It remains to prove variation.  Set

\[
 \beta={b\over a},\qquad
 t_0={J\delta\over2k\sqrt a},\qquad
 \lambda=gka,qquad u=at^2.
\]

Condition (77.14) is precisely

\[
 {\sqrt\beta\over2}<t_0<1.                          \tag{R77.13}
\]

Using (R77.1) and \(du=2at\,dt\), one has the exact formula

\[
 \mathfrak B_{a,b,k}^\circ(g)
 =ga\int_{\sqrt\beta/2}^{1}Q_g(t)
       e\bigl(\lambda(t-t_0)^2\bigr)\,dt,           \tag{R77.14}
\]

where

\[
\begin{aligned}
 Q_g(t)={}&2t\,A_{ga,gb}(gat^2)
 \rho\!\left({ga(t^2-\beta/4)\over M}\right)
 \rho\!\left({ga(1-t^2)\over M}\right).           \tag{R77.15}
\end{aligned}
\]

This displays the special actual-symbol structure.  Apart from the two
collars, \(Q_g\) is a fixed smooth function of \(t\), multiplied by

\[
 \eta_L(ga)\overline{\eta_L(gb)}
 \Phi\!\left({ga\over H+1}\right)
 \overline{\Phi\!\left({gb\over H+1}\right)}
 {L^3\over g^3a^{9/4}b^{3/4}}.                     \tag{R77.16}
\]

Indeed, the two \(W\)-arguments become exactly

\[
 {\sqrt{q_X}\over2t},
 \qquad {\sqrt{q_X\beta}\over2t},                  \tag{R77.17}
\]

so they have no \(g\)-derivative at all.  The remaining \(t\)-factor
is \(2t^{-2}\) times these two profiles.  On \(g\asymp G\), every
logarithmic \(g\)-derivative of the scalar factor in (R77.16) is
\(O(1)\): an ordinary \(g\)-derivative costs \(O(G^{-1})\).  This
includes a \(\Phi\)-transition, since
\(a/(H+1)\ll a/L\asymp G^{-1}\).  A collar has normalized width
\(\asymp(ga)^{-1}\), and its \(g\)-derivative is \(O(g^{-1})\) on that
collar.

The elementary inequality \(b-a\ge2\), together with \(b<4a\), gives

\[
 \delta={b-a\over\sqrt a+\sqrt b}\ge {2\over3\sqrt a}.
\]

Hence the lower saddle inequality and \(ga\asymp L\le\sqrt J\) imply

\[
 k>{J\delta\over2\sqrt a}\gg {J\over a}\gg ga.    \tag{R77.18}
\]

Thus the stationary width \(\lambda^{-1/2}\) in the \(t\)-variable is
at most a constant times \((ga)^{-1}\), the width of either continuous
collar.

For completeness, the centred-collar oscillatory lemma used here is
the following direct one-dimensional estimate.  If \(g\) ranges over a
fixed-ratio interval, \(t_0\) lies in a fixed compact interval such as
(R77.13), \(k\gg ga\), and \(Q_g\) has the symbol and moving-collar
bounds just recorded, then

\[
 \left|ga\int Q_g(t)e(gka(t-t_0)^2)dt\right|
 \ll \sqrt{ga\over k},                              \tag{R77.19}
\]

and, after extending \(g\) continuously,

\[
 \left|{d\over dg}\left\{ga\int
 Q_g(t)e(gka(t-t_0)^2)dt\right\}\right|
 \ll {1\over g}\sqrt{ga\over k}.                  \tag{R77.20}
\]

To prove the lemma, split at
\(|t-t_0|\le\lambda^{-1/2}\) and into dyadic annuli outside it.  The
central interval is bounded directly.  On each annulus apply
\((4\pi i\lambda(t-t_0))^{-1}d/dt\) three times.  Differentiating in
\(g\) produces only a logarithmic symbol derivative, a collar
derivative, or
\((\lambda/g)(t-t_0)^2\); the same annular integrations offset the last
factor.  In either collar use its scaled coordinate
\(ga(t^2-t_{\rm end}^2)/M\).  The inequality
\(\lambda^{-1/2}\ll(ga)^{-1}\) ensures that its derivatives are no
finer than the stationary scale.  The annular bounds form a geometric
series.  This proof remains uniform when \(t_0\) lies inside, enters, or
leaves either collar; no endpoint stationary expansion is used.

Apply (R77.19)--(R77.20) on the actual interval
\(g\asymp G\).  The fundamental theorem of calculus on each step-two
interval gives

\[
\begin{aligned}
 \mathcal V_{a,b,k}
 &\le |\mathfrak B^\circ(g_{\max})|
   +\int_{g_{\min}}^{g_{\max}}
          |(\mathfrak B^\circ)'(v)|\,dv \\
 &\ll \sqrt{aG\over k}.                             \tag{R77.21}
\end{aligned}
\]

Finally, (R77.13) says

\[
 {J\delta\over k}=2\sqrt a\,t_0\asymp\sqrt a,
\]

so (R77.21) is exactly (R77.4).  This proves (77.18) for the complete
integral, including moving support and both saddle transitions.

## 4. First doubtful or unproved step

The first input not literally proved or even stated in the permitted
packet is (R77.5), equivalently the fixed smooth symbol bounds for the
families \(\eta_L,\Phi,W\) and the precise interval structure of
\(\mathcal G_{a,b}\).  The algebra after that input is self-contained.
If those are the standard actual cutoffs, there is no further doubtful
step.  If they are not imposed, (77.18) is false: multiplying the lift
profile by bounded signs alternating on successive odd \(g\)'s leaves
pointwise size unchanged but enlarges the step-two variation by a
factor comparable to \(N_{a,b}\).

Accordingly, the packet alone does not justify an unconditional
promotion with no profile hypotheses.  The exact graph statement
should include the bounds in Section 2.  The symmetric-limit convention
in (R77.2) should also be recorded, although the collared formula used
in the proof is absolutely convergent and has no ambiguity.

## 5. Required control test and outcome

1. **External normalization and one-count physical factor — pass.**
   The proof starts from the normalized \(a_L\) in (77.1).  No external
   physical factor is inserted.  The conjugate off-diagonal pairing is
   accounted for exactly once by the existing \(2\Re\).
2. **Both full finite-Poisson endpoint samples — pass.**  Formula
   (R77.2) shows explicitly how the two half weights from the integral
   comb and the two displayed half weights make the full samples
   \(F(A),F(B)\).  Both samples then lie in the primal collar
   difference; neither is silently dropped.
3. **Fixed collar capacity — pass.**  The deleted primal set has
   \(O_M(1)\) integer points per pair and total \(O_M(L^2)\) capacity.
   The proof uses the fixed \(M\), never a growing collar.  The
   curvature lower bound \(J/L^2\ge1\) is what makes fixed width enough.
4. **Actual profiles, floors, stars, and finite support — pass under the
   explicit symbol hypotheses.**  Equations (R77.16)--(R77.17) retain
   \(\eta_L,\Phi,W,q_X\) exactly.  The definitions of \(y,H,q_X\), the
   lower ceiling, the odd stars, and the finite lift interval are not
   replaced by continuous asymptotics.  The packet's omission of the
   actual derivative bounds is the qualification recorded in Section
   4.
5. **All Poisson mode types — pass.**  Zero and positive modes and both
   negative nonstationary tails are summed in (R77.7)--(R77.10).
   Strict interior stationary modes are retained exactly.  Equality and
   exterior transition modes are nonstationary on the collared support
   and satisfy the same tail estimate.
6. **Stationary corrections and error summation — pass.**  No stationary
   asymptotic expansion is substituted into (77.15).  The leading term,
   every lower correction, and the transition shape all remain in
   \(\mathfrak B^\circ\).  Only the genuinely nonstationary tails are
   errors, and their \(O(1)\)-per-pair bounds sum to \(O(L^2)\).
7. **\(g\)-derivatives through all profile transitions — pass.**  The
   power and \(\eta_L\) factors cost \(O(G^{-1})\), a \(\Phi\)-edge
   costs \(a/H\ll G^{-1}\), and both exact \(W\)-arguments in
   (R77.17) are independent of \(g\).  The continuous collars satisfy
   the scaled derivative bounds used in (R77.20).
8. **Saddle entry and exit through each continuous collar — pass.**
   The centred-collar lemma is uniform for \(t_0\) on either collar.
   The inequality \(k\gg ga\) makes the stationary scale no wider than
   that fixed physical collar.  No frozen interior formula is used at
   entry or exit.
9. **Sharp lower-ceiling \(g\bmod4\) seam — pass.**  The gap from
   \(gb/4\) to \(\lceil gb/4\rceil\) is alternately \(1/4\) or \(3/4\)
   as the odd lift advances by two.  Since both lie inside the region
   where the lower collar is identically zero, this step-four seam is
   confined to the \(O(L^2)\) primal collar error.  The retained symbol
   consequently has genuine step-two variation.
10. **Coherent \((81,121)\) family — pass and sharpness warning.**  If
    \(X=T^4\), with odd \(13\mid T\), then
    \(J=y=T^2\), \(q_X=1\), \(H=T\), \(\delta=2\), and
    \(k=2T^2/13\) lies between \(T^2/9\) and \(2T^2/11\).  Moreover

    \[
      u_0=\left({J\delta\over2k}\right)^2={169\over4},
      \qquad {\Lambda\over k}=13T^2\in\mathbb Z.
    \]

    The two saddle profile arguments are exactly \(9/13\) and
    \(11/13\), hence are on the stated \(W=1\) plateau.  Also
    \(r=20g\) is even and
    \(e(-gX\delta^2/(4k))=-1\) for every odd \(g\); the lift phase is a
    constant, not a source of cancellation.  The scale in (R77.4) is
    therefore the correct one to retain in this hostile coherent
    family.
11. **Nonresonant actual-profile and \(\Phi\)-edge families — pass under
    the profile hypotheses.**  In the preceding family put
    \(N=2T^2/13\) and take \(k=N+1\).  For large \(T\) this is still in
    the saddle interval and the two \(W\)-arguments remain in the same
    plateau, whereas

    \[
      \left\|{\Lambda\over k}\right\|
      ={1\over2}-{169\over2(N+1)}\ge {1\over4}
    \]

    once \(N\) is sufficiently large.  Thus the same actual amplitude
    also has a genuinely nonresonant family.  For a \(\Phi\)-edge, take
    any admissible transition point \(\tau\), choose coprime odd
    \(a<b\) with \(b/a\) sufficiently close to one, and choose odd
    \(g\) with \(ga/(H+1)=\tau+O(a/H)\).  Successive lifts change the
    argument by \(2a/(H+1)=O(G^{-1})\); hence the total profile variation
    through the edge is \(O(1)\), exactly as (R77.20) requires.  The
    existence of a nonzero common-support edge is part of the actual
    profile data missing from the packet, not an additional algebraic
    assumption hidden in the proof.
12. **Rank-one reciprocal self-return and coefficient adversary —
    pass.**  The local kernel is the single centred quadratic
    \(e(\lambda(t-t_0)^2)\).  Its Fourier transform has the reciprocal
    quadratic phase and size \(\lambda^{-1/2}\); transforming back
    returns the original kernel (up to reflection and a unit scalar).
    Thus a second matched transform supplies no second gain.  On the
    coherent family, replacing the actual lift profile by
    \(c_g=(-1)^{(g-1)/2}\) times that profile makes successive complete
    integrals differ by approximately twice their size, so the
    variation is larger by \(N_{a,b}\).  This adversary is excluded
    precisely by the slow scalar factors (R77.16), the \(g\)-independent
    \(W\)-factors (R77.17), and the centred phase.
13. **Separation from later objectives — pass.**  The proof establishes
    only the exact bulk decomposition and its step-two symbol
    variation.  It does not take absolute values over the retained
    primitive-pair/reciprocal sum, estimate a resonance union, bound the
    full energy, or assert M2, M9, M9--M2, endpoint uniformity, or any
    exponent.

## 6. Dependencies and exact artifacts used

Only the following two permitted artifacts were used:

1. `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/briefs/blind_actual_symbol_rederivation.md`;
2. `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/derivation_packet.md`.

No Round-76 report, sibling Round-77 artifact, claim graph, proof draft,
source card, strategy memo, web source, or numerical experiment was
used.

## 7. Recommended state effect

**Revise, then promote the two local claims.**  Record (77.9) with
symmetric summation and record the fixed smooth actual-symbol/support
hypotheses from Section 2.  Under those hypotheses, promote the exact
aggregate identity (77.16) and the complete-integral step-two variation
(77.18).  Retain the stated no-go against arbitrary coefficients and
retain all separations in control 13.  Make no change to any
resonance-union, full-energy, M2, M9, M9--M2, endpoint-uniformity, or
global-exponent claim.
