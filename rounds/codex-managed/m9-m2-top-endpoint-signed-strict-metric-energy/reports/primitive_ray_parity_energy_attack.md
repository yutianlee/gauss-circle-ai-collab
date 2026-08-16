# Primitive-ray parity energy attack

Campaign: m9-m2-top-endpoint-signed-strict-metric-energy  
Round: 80  
Task: primitive_ray_parity_energy_attack  
Role: analytic discovery  
Graph SHA-256: cb007911c1e9d407d9adbc8919ce44cc3eaab411a212d0925e1176f5a154a43a

## 1. Result

**Complete-symbol parity-cancellation and adjoint-density no-go lemma.**
The proposed quotient-parity and half-integer spectral-gap mechanisms give
no independent saving for the complete Round-77 coefficient. The reason is
an exact pointwise cancellation, not a capacity estimate. Define

\[
 \widetilde{\mathfrak B}_{a,b,k}^{\circ}(g)
 :=g\int_{b/4}^{a}A_{ga,gb}^{\circ}(gu)
 e\!\left(g[-J(\sqrt b-\sqrt a)\sqrt u+ku]\right)\,du.
\]

Then

\[
 \mathfrak B_{a,b,k}^{\circ}(g)
 =e\!\left(\frac{g\Lambda}{2k}\right)
  \widetilde{\mathfrak B}_{a,b,k}^{\circ}(g).       \tag{80.P1}
\]

Consequently, for every actual odd lift \(g\), every nearest integer
\(\ell\), and \(\eta=\Lambda/k-\ell\),

\[
 (-1)^{q+\ell}e(-g\eta/2)
 \mathfrak B_{a,b,k}^{\circ}(g)
 =(-1)^q\widetilde{\mathfrak B}_{a,b,k}^{\circ}(g). \tag{80.P2}
\]

Thus the fiber sign \((-1)^{p/k}\), \(p=\ell k\), disappears from the
complete actual-symbol summand. Likewise, the apparent half-integer
frequencies \(r-g/2\) obtained by Fourier expanding the metric window are
shifted back to the integer frequencies \(r\) by the factor in (80.P1),
and the literal density mode \(r=0\) remains.

After the exact change \(h=ga,\ s=gb,\ x=gu\), the sole outer sign is

\[
 (-1)^q=\chi _4(h)\chi _4(s),                       \tag{80.P3}
\]

and the kernel is exactly the adjoint Poisson kernel of the residual
transposed character energy. Hence this route proves neither the full
target nor a new hard parameter subrange. It does rigorously isolate the
strictly smaller complete-symbol survivor: the joint
density--discrepancy adjoint correlation (80.P9) below. This is an
actual-symbol route no-go, not a coefficient-uniform countermodel and not
a claim that the target estimate is false.

## 2. Exact statement and hypotheses

Let \(X\) be large, \(J=\sqrt X\), and fix a residual dyadic block from
the Round-80 packet. Thus \(a<b<4a\) are odd and coprime, \(ab\) is
nonsquare, and

\[
 a\asymp A,\qquad b-a\asymp D,\qquad
 k\asymp K,\qquad G_{a,b}\asymp G.
\]

The literal open reciprocal interval is

\[
 \frac{J(\sqrt b-\sqrt a)}{2\sqrt a}<k<
 \frac{J(\sqrt b-\sqrt a)}{\sqrt b},                \tag{80.P4}
\]

and the residual block obeys

\[
 K\asymp\frac{JD}{A},\qquad G\asymp\frac LA,
 \qquad AJD^3\gg L^3.                               \tag{80.P5}
\]

Primitive square rays, exact nonsquare centers, the blocks on the safe
side \(AJD^3\ll L^3\), and the accepted Round-77 endpoint/collar error
are not part of the block. Let \(W_R\) be the fixed smooth period-one
member of the punctured metric partition, supported on
\(0<c_1/R\leq\|t\|\leq c_2/R<1/2\), where
\(1\leq R\leq N_{a,b}\ll G\). Write

\[
 W_R(t)=\mu_R+\sum_{r\ne0}\widehat W_R(r)e(rt),
 \qquad \mu_R\asymp R^{-1}.                         \tag{80.P6}
\]

All harmless fixed dyadic cutoffs are denoted by \(\omega(k)\). They do
not alter the literal open interval or the endpoint convention. The
coefficient \(A_{ga,gb}^{\circ}(gu)\) in (80.P1) is the complete accepted
Round-77 coefficient: it contains both fixed physical collars, all
floors and stars, the exact \(\Phi\), \(q_X\), and \(W\)-profiles, the
finite odd lift support, and every saddle transition.

For \(g\in\mathcal G_{a,b}\), put

\[
 h=ga,\qquad s=gb,\qquad
 \Omega_{h,s,g}:=\frac{X(\sqrt s-\sqrt h)^2}{2g}
 =\Lambda.
\]

Define the finite metric adjoint kernel

\[
 \mathcal K_{R;h,s,g}(x)
 :=\sum_{k\ {\rm in}\ (80.P4)}
 \omega(k)W_R(\Omega_{h,s,g}/k)e(kx),               \tag{80.P7}
\]

with the already removed exact-center modes omitted, or restored only at
the accepted \(O_\varepsilon(LX^\varepsilon)\) cost. Also define

\[
 \mathcal K_{r;h,s,g}(x)
 :=\sum_{k\ {\rm in}\ (80.P4)}
 \omega(k)e\!\left(kx+\frac{r\Omega_{h,s,g}}k\right)
 \quad(r\in\mathbb Z).                              \tag{80.P8}
\]

Then the exact residual one-count sum, before the single outer
\(2\Re\) in (80.3), is

\[
\boxed{
 \begin{aligned}
 \mathfrak Q_{A,D,K,G,R}
  :={}&\sum_{\substack{a,b\ {\rm residual}}}
       \sum_{g\in\mathcal G_{a,b}}
       \chi _4(ga)\chi _4(gb)\\
 &\times\int_{gb/4}^{ga} A_{ga,gb}^{\circ}(x)
 e\!\left(-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)
 \mathcal K_{R;ga,gb,g}(x)\,dx .
 \end{aligned}}                                      \tag{80.P9}
\]

Moreover,

\[
 \mathcal K_R(x)=\mu_R\mathcal K_0(x)
 +\sum_{r\ne0}\widehat W_R(r)\mathcal K_r(x).      \tag{80.P10}
\]

With the chosen smooth one-count partition,

\[
 \mathcal S_{A,D,K,G,R}^{\rm hard}
 =\mathfrak Q_{A,D,K,G,R}.                           \tag{80.P11}
\]

Therefore the remaining desired statement is precisely

\[
 \sum_{A,D,K,G,R}|\mathfrak Q_{A,D,K,G,R}|
 \ll_\varepsilon L^2X^\varepsilon.                 \tag{80.P12}
\]

No such estimate is asserted here.

## 3. Proof and derivation

Put \(\delta=\sqrt b-\sqrt a\), \(\Lambda=X\delta^2/2\), and
\(g=2n+1\). The constant term in the centered quadratic phase of the
complete coefficient is

\[
 g\frac{X\delta^2}{4k}=\frac{g\Lambda}{2k}.
\]

It is independent of \(u\), so factoring it out proves (80.P1) without
changing any endpoint, collar, floor, profile, or saddle term. The two
external phases in the accepted normal form combine as

\[
 e\!\left(\frac q2-\frac\Lambda{2k}\right)
 e(-n\Lambda/k)
 =(-1)^q e(-g\Lambda/(2k)).                          \tag{80.P13}
\]

Multiplication by (80.P1) cancels the reciprocal phase exactly. In the
nearest-integer notation \(\theta=\Lambda/k=\ell+\eta\), the same
calculation is pointwise:

\[
 \begin{aligned}
 &(-1)^{q+\ell}e(-g\eta/2)
 e(g\theta/2)\widetilde{\mathfrak B}^{\circ}(g)\\
 &\qquad=(-1)^{q+\ell}e(g\ell/2)
 \widetilde{\mathfrak B}^{\circ}(g)
 =(-1)^{q+2\ell}\widetilde{\mathfrak B}^{\circ}(g)
 =(-1)^q\widetilde{\mathfrak B}^{\circ}(g),
 \end{aligned}                                      \tag{80.P14}
\]

because \(g\) is odd. Since \(\ell=p/k\) on a product fiber, (80.P14)
also proves that quotient parity is absent after the complete symbol is
restored. A divisor-fiber argument which keeps \((-1)^{p/k}\) but drops
the factor \(e(g\Lambda/(2k))\) has changed the coefficient and is not an
argument for (80.13).

Now change variables \(h=ga,\ s=gb,\ x=gu\). Since \(dx=g\,du\),

\[
 \widetilde{\mathfrak B}_{a,b,k}^{\circ}(g)
 =\int_{s/4}^{h}A_{h,s}^{\circ}(x)
 e\!\left(kx-J(\sqrt s-\sqrt h)\sqrt x\right)dx.   \tag{80.P15}
\]

For odd integers the character is completely multiplicative and
\(\chi _4(t)=(-1)^{(t-1)/2}\). Hence

\[
 \chi _4(h)\chi _4(s)
 =\chi _4(a)\chi _4(b)
 =(-1)^{(a+b-2)/2}=(-1)^{(b-a)/2}=(-1)^q,          \tag{80.P16}
\]

where the two exponents in the middle differ by the even integer
\(a-1\). Substitution of (80.P15)--(80.P16) into the strict one-count
sum gives (80.P9)--(80.P11).

The density--discrepancy identity (80.P10) follows by inserting the
absolutely convergent smooth Fourier series (80.P6) into the finite
\(k\)-sum. This also diagnoses the apparent spectral gap. If the
centered coefficient is left unexpanded, then

\[
 W_R(\theta)e(-g\theta/2)
 =\sum_{r\in\mathbb Z}\widehat W_R(r)
   e((r-g/2)\theta),                                 \tag{80.P17}
\]

and every displayed frequency is a nonzero half-integer. But (80.P1)
shifts every term in (80.P17) by \(+g/2\):

\[
 \mathfrak B^{\circ}(g)W_R(\theta)e(-g\theta/2)
 =\widetilde{\mathfrak B}^{\circ}(g)
  \sum_{r\in\mathbb Z}\widehat W_R(r)e(r\theta).    \tag{80.P18}
\]

Thus \(r=0\), with coefficient \(\mu_R\), is literally present. The
anti-periodicity of the nearest-integer factor is exactly conjugated away
by the centered phase of the actual symbol.

Finally, the \(r=0\) kernel is the adjoint of the Poisson step which
created \(k\). For fixed \(h,s\), extend (80.P15) to all integral \(k\).
The collared amplitude is smooth and compactly supported, so Poisson
summation, with the symmetric/star convention when the original
endpoints are restored, gives

\[
 \sum_{k\in\mathbb Z}
 \int_{s/4}^{h}A_{h,s}^{\circ}(x)
 e\!\left(kx-J(\sqrt s-\sqrt h)\sqrt x\right)dx
 =\sum_{m\in[s/4,h]\cap\mathbb Z}^{*}
 A_{h,s}^{\circ}(m)
 e\!\left(-J(\sqrt s-\sqrt h)\sqrt m\right).        \tag{80.P19}
\]

The right side is the original transposed \(h,s\) cross-row kernel with
the character product (80.P16). The literal interval (80.P4) and a
dyadic \(K\)-block are stationary projections of this adjoint identity;
the complementary endpoint and nonstationary pieces are precisely the
Round-77 terms already bounded in aggregate. Therefore reciprocal
Poisson on \(\mathcal K_0\) is a rank-one self-return, not a second
curvature saving.

## 4. First doubtful or unproved step

The first unproved step is (80.P12), already at the joint kernel

\[
 \mu_R\mathcal K_0(x)
 +\sum_{r\ne0}\widehat W_R(r)\mathcal K_r(x).       \tag{80.P20}
\]

The density part \(\mu_R\mathcal K_0\) has no reciprocal oscillation at
all; under the full adjoint it is the original transposed character
correlation (80.P19). The centered terms have phases
\(kx+r\Lambda/k\), but bounding them separately and taking absolute
values does not cancel the density population. Conversely, applying
Poisson to the density term merely restores the starting row energy.

The remaining sign \((-1)^q=\chi _4(h)\chi _4(s)\) is constant along the
odd lift \(g\) and is exactly the character product already present
before the gcd decomposition. There is no automatic \(q\)-alternation:
the hard near-square family \(b=a+2\) has \(q=1\) identically, and its
Pell subfamily \(a=s_0^2,\ b=3t_0^2=a+2\) is nonsquare. This does not
preclude a genuinely new character-energy theorem, but such a theorem
would have to estimate (80.P9) itself; it cannot follow merely by
renaming \(\chi _4(h)\chi _4(s)\) as primitive-ray parity.

Accordingly the smallest unresolved actual-symbol object exposed by this
attack is the single cross-row correlation (80.P9), equivalently the
coupled density--discrepancy form (80.P20). No coefficient lower bound
and no counterexample to (80.P12) is claimed.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| external_normalization | Passed. Equation (80.P13) uses the external phase once. The report treats the complex inner sum; the \(2\Re\) and \(O(L^2\log(2+L))\) error from (80.3) remain outside and occur once. |
| round78_round79_exclusions | Passed. The index set in (80.P4)--(80.P5) excludes primitive square rays, exact nonsquare centers, and positive-safe blocks. Restoring the at-most-one exact nonsquare ray is invoked only at its accepted \(O_\varepsilon(LX^\varepsilon)\) cost. |
| primitive_parity | Passed. Oddness and coprimality make \(q\in\mathbb Z\); (80.P16) proves the exact primitive-to-original character identity. |
| combined_odd_lift_phase | Passed. Equation (80.P13) uses \(g=2n+1\) with no missing half phase. |
| nearest_integer_sign | Passed, with a no-go outcome. Equation (80.P14) shows that \((-1)^\ell\) cancels rather than supplies an additional sign. |
| strict_metric_one_count | Passed. One fixed punctured \(W_R\) is inserted once; its tie convention is inherited, and \(W_R(0)=0\). |
| density_and_discrepancy | Passed algebraically, not estimated. Equation (80.P10) retains both \(\mu_R\mathcal K_0\) and every centered mode in one bracket. |
| complete_actual_coefficient | Passed. The full \(A_{h,s}^{\circ}\) remains inside (80.P9); only its exact constant phase is factored. |
| lift_support_and_step_two_variation | Passed. The literal finite odd support is kept. No false BV statement is made for the recentered \(\widetilde{\mathfrak B}\); multiplying by the compensating phase can change its lift variation. |
| fiber_product_parity | Passed, with a no-go outcome. On \(p=\ell k\), (80.P14) cancels \((-1)^{p/k}\) pointwise. Divisor re-enumeration has no parity twist after the actual symbol is restored. |
| safe_block_boundary | Passed. All claims are restricted to the fixed residual side \(AJD^3\gg L^3\); the already closed side is not recounted. |
| near_square_and_Pell | Passed. Both have \(q=1\), so they falsify uniform cancellation from \(q\)-alternation; no coefficient lower bound is inferred. |
| perfect_power_metric_recurrence | Passed. Perfect-power choices may populate \(W_R\), but (80.P14) remains an identity and gives no fictitious quotient-parity saving. |
| endpoints_stars_and_collars | Passed. They stay inside \(A^{\circ}\); (80.P19) states the star/symmetric convention explicitly. Empty and singleton \(k\)-intervals are finite kernels and require no discarded boundary term. |
| coefficient_adversary | Passed. The lemma is not coefficient-uniform and introduces no arbitrary or phase-conjugated coefficients. Its cancellation uses the literal phase in (80.P1). |
| rank_one_self_return | Passed, with a no-go outcome. Equation (80.P19) identifies the \(r=0\) adjoint Poisson return exactly. |
| downstream_scope | Passed. The result is a route obstruction and exact survivor only; it proves neither the signed cone nor \(M9\!-\!M2\), \(M9\), endpoint uniformity, R5-Full, or the Gauss-circle exponent. |

No numerical experiment was used. The exact, strict-metric, near-square,
Pell, perfect-power, empty/singleton, endpoint/star,
coefficient-adversary, and self-return controls are algebraic and hence
do not depend on sampled parameters.

## 6. Dependencies and exact artifacts used

The derivation uses only the selected Round-80 context:

1. protocol.md for evidence and state-ownership rules.
2. state/proof_obligations.yml for the open signed-cone and transposed-character-energy scope and the recorded Round-76--79 route failures.
3. state/active_campaign.yml for the frozen residual target and controls.
4. strategy/conductor_0816_full_proof_strategy.md for the signed-energy gate and the prohibition on transform self-returns.
5. rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/derivation_packet.md for (80.1)--(80.18), the one-count convention, and the exact removals.
6. rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reviews/conductor_round77_adjudication.md for the complete centered integral, finite lift support, collars, stars, and accepted aggregate error.
7. rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/reviews/conductor_round78_adjudication.md for the square-ray removal and reciprocal self-return/collar controls.
8. rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/reviews/conductor_round79_adjudication.md for the nonsquare exact-center removal, safe region, divisor-strip density, and surviving strict-metric scope.
9. rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/briefs/primitive_ray_parity_energy_attack.md for the assigned output contract.

No sibling Round-80 report, source card, web theorem, or computational
artifact was used.

## 7. Recommended state effect

**Retain the target as open; promote only the route no-go after
independent review.** The graph should not promote
M9-M2-top-endpoint-signed-cone, M9-M2, M9, endpoint uniformity, or the
exponent.

If the conductor's seam reviews validate (80.P1)--(80.P19), record two
rejected shortcuts:

1. “Nearest-integer quotient parity survives the complete Round-77
   symbol.” It is false by (80.P14).
2. “The half-integer Fourier gap removes the ordinary metric density.”
   It is false by (80.P18), whose integer \(r=0\) mode is the adjoint
   self-return (80.P19).

Retain (80.P9)--(80.P12) as the revised smallest actual-symbol obligation.
A productive next attack must prove a signed estimate for the coupled
integer-mode kernel (80.P20), exploiting the original
\(\chi _4(h)\chi _4(s)\) correlation without outer Cauchy deleting it,
or else produce an actual-coefficient obstruction. Another
quotient-parity fiber count or reciprocal Poisson transform cannot
advance the bound.
