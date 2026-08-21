# Conductor review: Gaussian normalization and exact smooth-symbol factorization

Campaign: m9-m2-metaplectic-two-character-energy

Starting graph SHA-256:
7347081c1a765acafc6a4d1e3a96171d7b971079c2af144f7a0eaa825309bb2a

## Gaussian normalization

With \(e(z)=\exp(2\pi i z)\), real \(\alpha\ne0\), and the symmetric
oscillatory limit,

\[
 \int_{\mathbb R}e\!\left(-{t^2\over4\alpha}+ty\right)dt
 =\sqrt{2|\alpha|}\,e(-\operatorname {sgn}(\alpha)/8)
 e(\alpha y^2).
\]

Therefore

\[
 e(\alpha y^2)
 ={e(\operatorname {sgn}(\alpha)/8)\over\sqrt{2|\alpha|}}
 \int_{\mathbb R}e\!\left(-{t^2\over4\alpha}+ty\right)dt.
\]

For \(h=ga\), \(s=gb\), \(y=\sqrt s-\sqrt h\), and
\(\alpha=rX/(2gk)\), let \(t=J\sqrt x-\tau\). Then

\[
\begin{aligned}
 &e(-J\sqrt x\,y)e(\alpha y^2)\\
 &\quad={e(\operatorname {sgn}(r)/8)\over\sqrt{2|\alpha|}}
 \int_{\mathbb R}
 e\!\left(-{(J\sqrt x-\tau)^2\over4\alpha}\right)
 e(\tau\sqrt h)e(-\tau\sqrt s)\,d\tau.
\end{aligned}
\]

The sign is forced: the last two factors equal \(e(-\tau y)\).
For \(\alpha=0\), the same pairing is the atom
\(\delta_{J\sqrt x}\), since

\[
 e(-J\sqrt x\,y)=e(J\sqrt{hx})e(-J\sqrt{sx}).
\]

Thus the density is not deleted; it is the zero-time member of the
same free metaplectic kernel. The identity is exact termwise for the
finite physical sum. Any exchange with the infinite metric Fourier
series still requires symmetric regularization and the accepted decay
of \(\widehat W_R\).

## Exact factorization already present in the accepted symbol

Round 77 gives, before the fixed collars,

\[
 A_{ga,gb}(gu)=g^{-3}E_{a,b}(g)P_{a,b}(u),
\]

where

\[
\begin{aligned}
 E_{a,b}(g)
 &=E_a(g)\overline{E_b(g)},\\
 P_{a,b}(u)
 &=L^3u^{-3/2}P_a(u)\overline{P_b(u)},\\
 P_a(u)
 &=a^{-3/4}W\!\left(\sqrt{q_Xa/(4u)}\right).
\end{aligned}
\]

The collar factor

\[
 \rho\!\left({g(u-b/4)\over M}\right)
 \rho\!\left({g(a-u)\over M}\right)
\]

also separates into a \(b\)-factor and an \(a\)-factor at fixed
\((g,u)\). Consequently the complete smooth collar-extracted amplitude
has exact rank one in the two base variables at fixed \((g,u)\).

Three couplings remain:

1. \((a,b)=1\), which is exactly Möbius-separable;
2. the moving reciprocal interval, equivalently a sharp interval for
   \(\sqrt{b/a}\) at fixed \(k/J\);
3. prior-owner and residual masks.

The first is harmless up to divisor factors. The second needs an exact
Mellin/triangular-projection norm and cannot be called \(X^\varepsilon\)
without proof. At linear block level the third may be reinserted only if
the already-owned terms are subtracted once and their accepted global
bound is retained; this does not automatically justify the same step
inside the fixed-\(a\) positive Gram.

## Capacity check for the one-character square-root transform

For a smooth base interval \(a\asymp A\) and one fixed odd lift \(g\),
write

\[
 \Theta_{v,g}(\tau)
 =\sum_{a\ {\rm odd}}\chi_4(a)v(a)e(\tau\sqrt g\,\sqrt a).
\]

The harmless fixed factor \(\chi_4(g)\) from
\(\chi_4(ga)=\chi_4(g)\chi_4(a)\) cancels between the two character
rows. Resolving \(\chi_4(a)\) and applying the ordinary one-variable
B-process with \(T_g=\tau\sqrt g\)
has saddle

\[
 a_*={4T_g^2\over r^2},\qquad r\ {\rm odd},
\]

phase \(e(T_g^2/r)\), and leading coefficient

\[
 2\sqrt2\,i\,e(-1/8)\,
 T_g\,\chi_4(r)r^{-3/2}v(4T_g^2/r^2)
\]

for the positive branch. If
\(|\tau|\asymp J\sqrt L\) and \(g\asymp G=L/A\), then the
dual length in the base-\(a\) Poisson lattice is

\[
 R_g\asymp {|T_g|\over\sqrt A}
 \asymp {JL\over A}=JG.
\]

The squared coefficient mass is

\[
 \sum_{r\asymp R_g}
 |T_g|^2r^{-3}\asymp {|T_g|^2\over R_g^2}\asymp A.
\]

This equals the primal coefficient mass. Hence Gaussian separation
followed by separate character B-processes is capacity preserving before
any genuinely joint denominator estimate. It is not itself the required
\(\rho^{-1}\) energy saving.

This calculation is local in a dyadic \(\tau\)-range.  The exact chirp
\(K_\alpha(J\sqrt x-\tau)\) has constant modulus and does not localize
\(\tau\) near \(J\sqrt x\).  Therefore it is not lawful to retain only
\(|\tau|\asymp J\sqrt L\), sum absolute dyadic masses, or assign the
chirp a finite total-variation norm.  Remote \(\tau\)-ranges must remain
inside the oscillatory Gaussian integral.  Applying the two separate
B-processes and then evaluating that integral is a metaplectic
composition; without an additional joint estimate it returns a chirp
of the same capacity.

The carrier-level closure can be checked exactly.  If a pair of
one-character transforms contributes the quadratic phase
\(e(\beta\tau^2)\), put
\(\gamma=1-4\alpha\beta\).  For \(\gamma\ne0\), another exact Fresnel
completion gives

\[
 \int_{\mathbb R}^{\rm osc}
 K_\alpha(J\sqrt x-\tau)e(\beta\tau^2)\,d\tau
 ={ \epsilon(\alpha,\gamma)\over\sqrt{|\gamma|}}\,
 e\!\left({Xx\beta\over\gamma}\right),
\]

where

\[
 \epsilon(\alpha,\gamma)
 =e\!\left({\operatorname {sgn}(\alpha)
       -\operatorname {sgn}(\alpha)\operatorname {sgn}(\gamma)
       \over8}\right)
\]

is unimodular.  Indeed, the quadratic coefficient in \(\tau\) is
\(-\gamma/(4\alpha)\).  Thus a Gaussian separation followed by two
scalar reciprocal phases is closed under the same metaplectic family:
it produces another reciprocal chirp with the exact Jacobian
\(|\gamma|^{-1/2}\), not a uniform contraction.  The locus
\(\gamma=0\) is a distributional caustic and cannot be bounded by
discarding the Jacobian.

## Current seam

The genuinely new question is whether the exact separated two-character
pair, after the sharp ratio interval and the remaining actual block
parameters are included, satisfies a joint vector-valued inequality
that saves \(\rho^{-1}\). A proof must be outside absolute values and
must fail for arbitrary phase-aligned coefficients. If the two
one-character transforms are estimated separately, the displayed mass
identity returns exactly to the previous capacity.
