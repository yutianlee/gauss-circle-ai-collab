# Direct attack on the top \(M2\) affine cone

- Campaign: `m9-m2-top-endpoint-affine-cone`
- Round: 74
- Task: `m2_affine_cone_attack`
- Role: discovery
- Starting graph SHA-256: `6e094849c4bbdeb08bb04771667f64cd6a36f0d56ba2cb811942693c3597e767`
- Status: candidate evidence only; no shared state was edited.

## 1. Result

The full estimate (74.2) is not proved, and no new power-sized
intermediate-\(L\) interval is claimed.  The smallest exact survivor found
is a diagonal-scale reciprocal energy obtained from the genuine
quarter-shifted two-dimensional Poisson transform.  This also gives a
route-specific no-go: applying Poisson once more to the near-product dual
wavelet is an exact self-return to the top \(M2\) reciprocal block, not a
new long-character estimate.

Put \(J=\sqrt X\).  After removing two primal boundary strips containing
\(O(L^{3/2})\) terms in total, the smooth interior of (74.2) has the
transform

\[
 \mathcal T_{L,\mathrm{int}}^{\mathrm{end}}
 =e(1/8)L^{3/2}X^{-1/4}\,\mathcal D_L
   +O_A(L^{3/2}X^{-A}),                                      \tag{1.1}
\]

with the harmless error understood after a fixed dyadic partition of the
two transition zones, and

\[
 \mathcal D_L=
 \sum_{\substack{j\asymp J\\j\ \mathrm{odd}}}\chi _4(j)
 \sum_{l\asymp J}W(l/y)\,
 K_{L,H}\!\left({L(X-jl)\over4l}\right).                    \tag{1.2}
\]

Here the ranges are the exact stationary images of
\(1/2<\sqrt{m/h}<1\), namely \(J/2<l<J\) and \(J<j<2J\), with the
corresponding shrunken ranges on each interior layer; the actual endpoint
profile remains \(W(l/y)\).  The wavelet \(K_{L,H}\) is the Fourier
transform of the actual radial factor
\(\eta_L(Lz)\Phi(Lz/(H+1))/z\), multiplied by the chosen interior-layer
cutoff.  Thus it is rapidly decreasing and (1.2) is effectively supported
on

\[
 |X-jl|\ll_A {JX^\varepsilon\over L}.                       \tag{1.3}
\]

Consequently the exact remaining target at this stage is

\[
 \boxed{\mathcal D_L\ll_\varepsilon X^{1/4+\varepsilon}.}   \tag{1.4}
\]

Poisson summation in \(l\), performed without taking absolute values,
gives

\[
 \mathcal D_L={1\over L}\sum_{k\in\mathbb Z}S_k,
 \qquad
 S_k=\sum_{\substack{j\asymp J\\j\ \mathrm{odd}}}
       \chi _4(j)b_{j,k}e(-kX/j),                            \tag{1.5}
\]

where \(b_{j,k}\) is the exact fixed-profile amplitude displayed in
(3.15) below and is negligible to arbitrary order for
\(|k|>L X^\varepsilon\).  Cauchy therefore reduces (1.4) to

\[
 \boxed{\sum_{|k|\ll LX^\varepsilon}|S_k|^2
       \ll_\varepsilon LJX^\varepsilon.}                    \tag{1.6}
\]

The diagonal in (1.6) is already \(O(LJX^\varepsilon)\).  Its
off-diagonal reciprocal correlation is the first unproved quantity.  A
second use of Poisson in the high dual variable transfers \(\chi _4\)
back to the short frequency and reconstructs the original fixed-profile
\(M2\) reciprocal block (including its two quarter shifts).  Hence
two-dimensional Poisson plus formal inversion does not itself save a
power.

## 2. Exact statement and hypotheses

Let

\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,\qquad 1\le L\le H,
\]

and let \(\eta_L,\Phi,W\) be exactly those in the derivation packet.  In
particular \(0\leq\Phi,W\leq1\), \(W=0\) on \(( -\infty,1/2]\),
\(W=1\) on \([2/3,1]\), and the primal coefficient is

\[
 a(h,m)=\eta_L(h)\Phi\!\left({h\over H+1}\right)
 \left({L^2\over hm}\right)^{3/4}
 W\!\left(\sqrt{{q_Xh\over4m}}\right).              \tag{2.1}
\]

All constants below may depend on fixed derivatives of these cutoffs.
For \(B=\lceil\sqrt L\rceil\), remove

\[
 0\le m-\lceil h/4\rceil\le2B,
 \qquad 0\le h-m\le2B.                              \tag{2.2}
\]

There are \(O(LB)=O(L^{3/2})\) such lattice points and \(a(h,m)\ll1\),
so (2.2) is target-safe absolutely.  On the complement insert cutoffs
which equal one at distance at least \(2B\) and zero at distance at most
\(B\).  The insertion changes only (2.2).  A dyadic partition by distance
to each edge makes every remaining angular amplitude smooth.  The
stationary point is at least \(L^{-1/2}\) in angular distance from a
transition, whereas its natural width is \((LJ)^{-1/2}\); hence there is
no edge-stationary transition.

For a fixed interior layer, define

\[
 \kappa_{L,H}(z)=
 {\eta_L(Lz)\Phi(Lz/(H+1))\over z}\,c(z),\qquad
 K_{L,H}(s)=\int_{\mathbb R}\kappa_{L,H}(z)e(sz)\,dz, \tag{2.3}
\]

where \(c\) is the induced fixed layer cutoff.  Summing the
\(O(\log L)\) layers costs \(X^\varepsilon\).  Equations (1.1)--(1.6)
are uniform for \(1\ll L\ll H\); bounded \(L\) is trivial, while
\(L\asymp H\) is independently closed by the accepted two-shift theorem.

The external normalization is counted exactly once.  With

\[
 \alpha_{h,H}={i\Phi(h/(H+1))\over2\pi h},\qquad
 C_h=e(h/4)-e(3h/4)=2i\chi _4(h)\quad(h\ \mathrm{odd}),
\]

one has

\[
 4\alpha_{h,H}C_h=-{4\Phi(h/(H+1))\chi _4(h)\over\pi h}.
\]

Multiplication by the stationary factor
\(e(1/8)(hX)^{1/4}m^{-3/4}/2\) gives precisely

\[
 -{2e(1/8)\over\pi}X^{1/4}L^{-3/2}
 \mathcal T_L^{\rm end}.                            \tag{2.4}
\]

The negative frequency is its conjugate and the full block is twice the
real part.  No additional factor is inserted into (2.4).

## 3. Proof or derivation

The identity

\[
 \chi _4(h)={e(h/4)-e(-h/4)\over2i}                 \tag{3.1}
\]

holds for every integer \(h\), including the vanishing of even
frequencies.  For one smooth interior layer, two-dimensional Poisson
therefore gives exactly

\[
 \mathcal T_{L,\mathrm{int}}
 ={1\over2i}\sum_{\rho=\pm1}\rho
  \sum_{u,l\in\mathbb Z}I_{\rho,u,l},               \tag{3.2}
\]

where

\[
 I_{\rho,u,l}=\iint a_{\rm int}(x,m)
 e\!\left(J\sqrt{xm}+{\rho x\over4}-ux-lm\right)dx\,dm.
                                                               \tag{3.3}
\]

Put \(t=\sqrt{m/x}\), so \(m=xt^2\) and
\(dx\,dm=2xt\,dx\,dt\).  Apart from the layer cutoff, the amplitude in
(3.3) becomes

\[
 2L^{3/2}\eta_L(x)\Phi(x/(H+1))x^{-1/2}t^{-1/2}
 W\!\left({\sqrt q_X\over2t}\right),                \tag{3.4}
\]

and the phase is \(x\Psi(t)\), with

\[
 \Psi(t)=Jt+{\rho\over4}-u-lt^2.                    \tag{3.5}
\]

A stationary point exists only for \(l>0\), and then

\[
 t_0={J\over2l},\qquad
 \Psi(t_0)={X-(4u-\rho)l\over4l}.                  \tag{3.6}
\]

Writing \(j=4u-\rho\), the stationarity equations are

\[
 j=2Jt_0,\qquad l={J\over2t_0},\qquad jl=X.          \tag{3.7}
\]

Thus the affine quarter shift is what produces the odd high dual
variable \(j\), and the image of \(1/2<t_0<1\) is
\(J<j<2J\), \(J/2<l<J\).  Moreover

\[
 W\!\left({\sqrt q_X\over2t_0}\right)=W(l/y),       \tag{3.8}
\]

so the actual non-square profile is retained rather than replaced by its
\(q_X=1\) limit.

The angular phase is exactly quadratic:

\[
 \Psi(t)=\Psi(t_0)-l(t-t_0)^2.                      \tag{3.9}
\]

The Gaussian integral in the \(e(z)=e^{2\pi iz}\) convention is

\[
 \int_{\mathbb R}e(-xlv^2)\,dv
 ={e(-1/8)\over\sqrt{2xl}}.                         \tag{3.10}
\]

Combining (3.4), (3.8), and (3.10), and then scaling \(x=Lz\), gives

\[
 I_{\rho,u,l}
 =2e(-1/8)L^{3/2}X^{-1/4}W(l/y)
 K_{L,H}\!\left({L(X-jl)\over4l}\right)+E_{\rho,u,l}.
                                                               \tag{3.11}
\]

The factor is \(2\), not \(2\sqrt2\): the \(\sqrt2\) from
\(t_0^{-1/2}l^{-1/2}=\sqrt{2/J}\) cancels the
\(\sqrt2\) in (3.10).  Two integrations by parts outside the angular
stationary neighborhood, followed by arbitrary integration by parts in
the radial variable, give the summed error in (1.1).  The transition
derivatives cost powers of \(L^{1/2}\), while the angular derivative gap
is \(\gg J L^{1/2}\); each such cost is absorbed by a power of \(J^{-1}\).

For \(j=4u-\rho\), one has \(\rho=-\chi _4(j)\).  Hence the coefficient
from (3.2) and (3.11) is

\[
 {\rho\over2i}\,2e(-1/8)=e(1/8)\chi _4(j),          \tag{3.12}
\]

which proves (1.1)--(1.2), including the character transfer and phase
constant.  Rapid decay of \(K\) gives (1.3).

For completeness, the second Poisson step leading to (1.5) can be made
without asymptotic notation.  For fixed \(j\), set

\[
 F_j(l)=W(l/y)K_{L,H}\!\left({L(X-jl)\over4l}\right).
\]

Poisson in \(l\) and the change of variable
\(z=L(X/l-j)/4\), equivalently \(l=X/(j+4z/L)\), give

\[
 \widehat F_j(k)={1\over L}b_{j,k}e(-kX/j),          \tag{3.13}
\]

where

\[
 \begin{aligned}
 b_{j,k}={}&4X\int_{\mathbb R}K_{L,H}(z)
 W\!\left({X\over y(j+4z/L)}\right)
 (j+4z/L)^{-2}\\
 &\quad\times
 e\!\left(-{kX\over j+4z/L}+{kX\over j}\right)dz .
 \end{aligned}                                      \tag{3.14}
\]

Thus

\[
 \mathcal D_L={1\over L}\sum_{k\in\mathbb Z}
 \sum_{\substack{j\asymp J\\j\ \mathrm{odd}}}
 \chi _4(j)b_{j,k}e(-kX/j),                         \tag{3.15}
\]

exactly.  Since \(j\asymp J\), the prefactor in (3.14) is \(O(1)\);
Fourier decay of the compact radial factor gives
\(b_{j,k}\ll_A(1+|k|/L)^{-A}\).  Cauchy in \(k\) proves that (1.6) is
sufficient for (1.4), and its diagonal is
\(\ll LJX^\varepsilon\).

Finally, Fourier inversion of \(K\) followed by Poisson in \(j\) uses

\[
 \sum_{j\in\mathbb Z}\chi _4(j)e(-j\xi)
 ={1\over2i}\!\left(
 \sum_n\delta(\xi-n-1/4)-
 \sum_n\delta(\xi-n+1/4)\right).                  \tag{3.16}
\]

It samples the radial variable at the two odd quarter lattices and yields
the short frequencies with their original \(\chi _4\) factor and phases
\(e(hX/(4l))\).  Together with (3.8), these are exactly the actual top
denominator profile and the two additive shifts.  This proves the claimed
self-return; discarding either term of (3.16) would be a false source of
cancellation.

## 4. First doubtful or unproved step

The first unproved analytic step is the off-diagonal part of (1.6):

\[
 \sum_{|k|\ll LX^\varepsilon}
 \sum_{j\ne j'}\chi _4(j)\chi _4(j')
 b_{j,k}\overline{b_{j',k}}
 e\!\left(-kX\left({1\over j}-{1\over j'}\right)\right)
 \ll_\varepsilon LJX^\varepsilon.                 \tag{4.1}
\]

No derivative-gap estimate uniform in \(X\) proves (4.1): the near
diagonal has reciprocal phase increments which can alias, and Poisson in
the high variable returns (3.16) to the original \(M2\) block.  Thus
(4.1) is a genuinely smaller, exact actual-symbol correlation, but the
present derivation supplies no saving for it.  In particular, neither
(1.4) nor (74.2) follows merely from counting the expected
\(J/L\) near-product pairs.

## 5. Required control test and outcome

1. **External normalization — pass.**  Equation (2.4) derives the frozen
   factor \(-2e(1/8)\pi^{-1}X^{1/4}L^{-3/2}\) and the two-sided block is
   exactly twice the real part.
2. **Odd character — pass.**  Equation (3.1) includes the zero even
   frequencies; (3.12) transfers the character to the odd high dual
   variable rather than deleting it.
3. **Hard lower edge — pass with extraction.**  The exact ceiling is kept.
   Its \(O(\sqrt L)\)-wide strip has \(O(L^{3/2})\) terms and is removed
   absolutely before smooth Poisson.
4. **Flat upper edge and \(q_X\ne1\) — pass.**  The analogous upper strip
   is target-safe, and (3.8) retains the exact factor as \(W(l/y)\).
5. **All \(L\)-slices — scoped pass.**  Bounded \(L\) is trivial and
   \(L\asymp H\) is inherited safe.  Every intermediate slice reduces to
   (4.1), but no new intermediate subrange is proved.
6. **Product multiplicity — pass.**  No multiplicativity is assumed.  If
   one groups \(n=hm\), its coefficient remains the moving near-square
   truncated divisor sum (74.11), with all divisor multiplicities.
7. **Shear projector — pass/no use.**  The exact identity is
   \(\chi _4(h)1_{r\equiv-h(4)}=(\chi _4(h)-\chi _4(r))/2\).
   Both terms survive because the phase, range, and original-\(h\) cutoff
   are not symmetric.  No shear cancellation is imported into (3.2).
8. **Exact squares and fourth powers — pass.**  Primal pairs for which
   \(Xhm\) is a square lie on squarefree-kernel rays and number
   \(O_\varepsilon(L^{1+\varepsilon})\), hence are target-safe
   absolutely.  For integral \(X\), exact dual aliases \(jl=X\) have
   divisor multiplicity \(O_\varepsilon(X^\varepsilon)\).  They remain in
   (1.2); perfect fourth powers are not silently declared nonresonant.
9. **Diagonal and near diagonal — partial.**  The energy diagonal is
   exactly of size \(LJ\).  The near-diagonal/off-diagonal expression
   (4.1) is the survivor, not an omitted error.
10. **Stationary aliases, errors, and self-return — pass.**  The alias
    width is (1.3), the Gaussian constant is audited in (3.10)--(3.12),
    transition and nonstationary errors are summed before (1.1), and
    (3.16) records the exact self-return.
11. **Proves-too-much — pass.**  The quarter-shift difference is essential.
    Replacing \(\chi _4\) by arbitrary coefficients removes (3.12), and
    coefficients chosen against the phase can make a two-dimensional sum
    of order \(L^2\).  No unsigned or arbitrary-coefficient analogue is
    claimed.
12. **Downstream scope — pass.**  No \(M1\) cancellation, smooth-interior
    packet theorem at the hard edge, full \(M9\), endpoint-uniformity, or
    Gauss-circle exponent is inferred.

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/briefs/m2_affine_cone_attack.md`
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/derivation_packet.md`
- `rounds/codex-managed/m9-top-endpoint-transform/synthesis.md`
- `rounds/codex-managed/m9-top-endpoint-transform/reports/one_sided_poisson_derivation.md`
- `rounds/codex-managed/m9-combined-top-cones/reports/combined_cone_hostile_audit.md`

No proof draft, sibling Round-74 report, external source, or computational
artifact was used.

## 7. Recommended state effect

**Retain/revise, but do not promote the cone bound.**  Record (1.2)--(1.6)
as a scoped candidate reduction for the smooth interior after the two
target-safe \(O(\sqrt L)\) boundary strips are extracted.  The narrowest
successor is the actual-amplitude reciprocal energy (4.1), whose diagonal
already has the required \(LJ\) scale.  Also record the no-go that a
second Poisson transform is an exact quarter-lattice self-return to the
top \(M2\) reciprocal block.  Keep
`M9-M2-top-endpoint-signed-cone`, `M9-M2`, endpoint uniformity, `M9`, and
the global exponent open.
