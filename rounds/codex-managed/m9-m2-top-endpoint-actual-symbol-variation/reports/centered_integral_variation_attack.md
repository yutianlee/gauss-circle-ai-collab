# Complete centred-integral identity and actual-symbol variation

- Campaign: `m9-m2-top-endpoint-actual-symbol-variation`
- Round: 77
- Task: `centered_integral_variation_attack`
- Role: analytic discovery
- Starting graph SHA-256: `e14373a05ee7d55258b53f07e18afa33682806add90bee49789208f464e46166`
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

The candidate complete-integral formula (77.15)--(77.16) and the
step-two variation scale (77.18) are correct after the fixed physical
collars are removed exactly as in (77.12). In fact the aggregate error
can be stated in the stronger form

\[
 \boxed{\quad
 \mathcal O_L=\mathcal O_{L,\mathrm{stat}}^\circ
       +O_{M,\eta,\Phi,W}\!\left(L^2\log(2+L)\right).
 \quad}                                                    \tag{1.1}
\]

The error contains the two full lattice endpoint samples, all removed
collar samples, the zero and positive Poisson modes, and every negative
mode outside the continuous saddle interval. There is no stationary
expansion error: every stationary mode, including saddle entry into or
exit from a continuous collar, remains in the complete integral
\(\mathfrak B^\circ\).

More strongly, on the continuous hull of an actual odd lift interval,

\[
 |\mathfrak B^\circ_{a,b,k}(g)|
 +g\left|{d\over dg}\mathfrak B^\circ_{a,b,k}(g)\right|
 \ll_{M,\eta,\Phi,W}
 {J(\sqrt b-\sqrt a)\sqrt G\over k^{3/2}}.             \tag{1.2}
\]

Consequently

\[
 \boxed{\quad
 \mathcal V_{a,b,k}
 \ll_{M,\eta,\Phi,W}
 {J(\sqrt b-\sqrt a)\sqrt G\over k^{3/2}},
 \quad}                                                   \tag{1.3}
\]

so (77.18), with its harmless \(X^\varepsilon\), follows.

The actual coefficient property used in (1.2) is not merely
boundedness. After \((h,s,x)=(ga,gb,gu)\), the two \(W\)-arguments and
\(q_X\) are independent of \(g\), the power factor is exactly
homogeneous, the \(\eta_L\Phi\) factors have logarithmic derivative
\(O(G^{-1})\), and each fixed physical collar depends on \(g\) only as
\(\rho(g(u-u_e)/M)\). Centering makes the phase vanish to second order
at its saddle. The analogous assertion for arbitrary bounded lift
coefficients is false: multiplying successive odd lifts by arbitrary
alternating units makes their variation larger by a factor comparable
to the lift length. Thus neither an unsigned/adversarial coefficient
model nor absolute summation over primitive pairs is proved here.

## 2. Exact statement and hypotheses

Use exactly (77.1)--(77.13), with \(1\le L\le H\le J^{1/2}\), the
actual finite odd support \(\mathscr H_L\), and one fixed \(M\) and
\(\rho\). For a primitive odd pair

\[
 a<b<4a,\qquad (a,b)=1,qquad
 \delta=\sqrt b-\sqrt a,
\]

let \(\mathcal G_{a,b}\) be the actual odd lifts for which
\(ga,gb\in\mathscr H_L\), and put \(G=L/b\); throughout a nonempty
lift interval, \(g\asymp G\). Define

\[
 \mathcal K_{a,b}:=
 \left\{k\in\mathbb Z_{\ge1}:
 {J\delta\over2\sqrt a}<k<{J\delta\over\sqrt b}\right\}. \tag{2.1}
\]

For \(k\in\mathcal K_{a,b}\), put

\[
 u_0={X\delta^2\over4k^2},\qquad
 \phi(u)=-J\delta\sqrt u+ku+{X\delta^2\over4k}.
                                                               \tag{2.2}
\]

Then \(b/4<u_0<a\) and, exactly,

\[
 \phi(u)=k(\sqrt u-\sqrt{u_0})^2,qquad
 \phi(u_0)=\phi'(u_0)=0.                              \tag{2.3}
\]

The complete symbol is

\[
 \mathfrak B^\circ_{a,b,k}(g)
 =g\int_{b/4}^{a}A^\circ_{ga,gb}(gu)e(g\phi(u))\,du.   \tag{2.4}
\]

Writing \(g=2n+1\), \(\Lambda=X\delta^2/2\), and
\(\alpha=(b-a)/4-X\delta^2/(4k)\), the following exact bulk normal
form holds with the aggregate error in (1.1):

\[
\begin{aligned}
 \mathcal O_L={}&2\Re
 \sum_{\substack{a<b<4a\\a,b\ {\rm odd},\ (a,b)=1}}
 \sum_{k\in\mathcal K_{a,b}}e(\alpha)
 \sum_{\substack{n\in\mathbb Z\\2n+1\in\mathcal G_{a,b}}}
 \mathfrak B^\circ_{a,b,k}(2n+1)
 e(-n\Lambda/k)\\
 &\hspace{40mm}+O_{M,\eta,\Phi,W}(L^2\log(2+L)).       \tag{2.5}
\end{aligned}
\]

Equations (1.2)--(1.3) hold uniformly, including when \(u_0\) lies in
either continuous collar transition. If \(\mathcal G_{a,b}\) has one
point, (1.3) means its endpoint term alone. No assertion is made for
the uncollared sharp ceiling; retaining it requires the accepted
mod-four split.

## 3. Proof or derivation

For fixed odd \(h<s<4h\), let

\[
 C=J(\sqrt s-\sqrt h),\qquad p(x)={C\over2\sqrt x},
 \qquad \lambda(x)=-p'(x)={C\over4x^{3/2}}.            \tag{3.1}
\]

The finite Poisson formula (77.9) is correct: its integral sum is the
starred lattice sum, and the displayed two half samples restore the
two full endpoints. Compare the original lattice sum directly with
the lattice sum having amplitude \(A^\circ_{h,s}\). Their difference
is supported on \(O_M(1)\) integers at each end, including both full
endpoint samples. Since \(|A_{h,s}(m)|\ll1\) on the cone and there are
\(O(L^2)\) ordered pairs, this entire primal difference is
\(O_M(L^2)\).

Extend \(A^\circ_{h,s}\) smoothly by zero. Ordinary Poisson summation
now has no endpoint functional. The mode \(\nu=-k\) has phase
\(-C\sqrt x+kx\), and it has a saddle in the uncollared continuous
interval precisely when

\[
 p(h)<k<p(s/4).                                      \tag{3.2}
\]

For \(h=ga,s=gb\), (3.2) is exactly (2.1). Every such integral is
retained without approximation.

It remains to sum the other modes. Uniformly on the cone,

\[
 \|A^\circ_{h,s}\|_\infty+|(A^\circ_{h,s})'\|_1
 +\|(A^\circ_{h,s})''\|_1\ll_{M,\eta,\Phi,W}1.        \tag{3.3}
\]

Moreover, because \(s-h\ge2\), \(h,s,x\asymp L\), and
\(L\le J^{1/2}\),

\[
 \lambda(x)\asymp {J(s-h)\over L^2}\gg1,
 \qquad {p(x)\over\lambda(x)}\asymp L.               \tag{3.4}
\]

The collar gives a distance \(\gg_M\lambda\) between the derivative
range on the support of \(A^\circ\) and either boundary in (3.2).
One integration by parts therefore bounds a negative exterior mode by
the reciprocal of its integer distance from that range plus
\(M\lambda\). Summing these nearby bounds is a harmonic sum of length
\(O(p/\lambda)=O(L)\). Two integrations by parts sum the remote tail.
The same argument, with derivative \(-p(x)-\nu\), treats \(\nu=0\)
and every positive mode. Explicitly,

\[
 \sum_{\nu\ge0}\left|\int A^\circ(x)e(-C\sqrt x-\nu x)dx\right|
 +\sum_{\substack{k\ge1\\k\notin(p(h),p(s/4))}}
 \left|\int A^\circ(x)e(-C\sqrt x+kx)dx\right|
 \ll_M\log(2+L).                                    \tag{3.5}
\]

There are \(O(L^2)\) pairs, so (3.5) and the primal collar ledger prove
the error in (1.1). Modes at equality in (3.2) are also covered by
(3.5): the fixed physical collar moves their derivative a fixed
positive number of curvature units away from zero. Thus no one-sided
Fresnel half term has been omitted.

For a retained mode, the gcd factorization has multiplicity one and

\[
 (-1)^{g(b-a)/2}
 \int A^\circ_{ga,gb}(x)e(-J\sqrt g\,\delta\sqrt x+kx)dx
 =e(g\alpha)\mathfrak B^\circ_{a,b,k}(g).             \tag{3.6}
\]

Since \(g=2n+1\) and
\(2\alpha=(b-a)/2-\Lambda/k\),

\[
 e(g\alpha)=e(\alpha)e(-n\Lambda/k).                 \tag{3.7}
\]

Equations (3.6)--(3.7) prove the exact main term in (2.5), including
the sign and the step-two phase.

It remains to prove variation. Direct substitution into the actual
symbol gives the exact factorization

\[
 A_{ga,gb}(gu)=g^{-3}E_{a,b}(g)P_{a,b}(u),             \tag{3.8}
\]

where

\[
\begin{aligned}
 E_{a,b}(g)={}&\eta_L(ga)\overline{\eta_L(gb)}
 \Phi\!\left({ga\over H+1}\right)
 \overline{\Phi\!\left({gb\over H+1}\right)},\\
 P_{a,b}(u)={}&L^3(ab)^{-3/4}u^{-3/2}
 W\!\left(\sqrt{{q_Xa\over4u}}\right)
 \overline{W\!\left(\sqrt{{q_Xb\over4u}}\right)} .  \tag{3.9}
\end{aligned}
\]

Thus both actual \(W\)-profiles, including \(q_X\ne1\), are exactly
independent of the lift. Put

\[
 R_g(u)=\rho\!\left({g(u-b/4)\over M}\right)
        \rho\!\left({g(a-u)\over M}\right).
\]

Then

\[
 \mathfrak B^\circ(g)=
 g^{-2}E_{a,b}(g)\int P_{a,b}(u)R_g(u)e(g\phi(u))du.   \tag{3.10}
\]

On a lift interval, \(g\asymp G=L/b\), and the accepted bounded
\(C^1\)-norm of \(\Phi\), together with the dyadic cutoff, gives

\[
 |E(g)|\ll1,qquad |E'(g)|\ll G^{-1}.                 \tag{3.11}
\]

Also, for every fixed required order,

\[
 |P^{(j)}(u)|\ll_{j,W}G^3b^{-j}\quad(u\asymp b),
 \qquad
 |\partial_u^jR_g(u)|\ll_{j,M}g^j,                  \tag{3.12}
\]

with the latter derivatives confined to intervals of length
\(O_M(g^{-1})\).

For completeness, the uniform centred oscillatory estimate used here
is now derived. In (2.3) set

\[
 v=\sqrt k(\sqrt u-\sqrt{u_0});qquad \phi(u)=v^2,
 \qquad {du\over dv}={2\sqrt u\over\sqrt k}.          \tag{3.13}
\]

The stationary range gives \(k\asymp J\delta/\sqrt b\). Since the
odd primitive gap has \(b-a\ge2\),

\[
 \delta\gg b^{-1/2},\qquad
 \mu:=\phi''(u_0)={2k^3\over J^2\delta^2}\asymp{k\over b}
 \gg {J\over b^2}\ge {L^2\over b^2}\asymp G^2.       \tag{3.14}
\]

After (3.13), the amplitude in (3.10) has size and normalized bounded
variation \(O(G/\sqrt\mu)\). Equations (3.11)--(3.12) give the same
bound for its logarithmic \(g\)-derivative. Importantly, a physical
collar has \(v\)-width
\(\asymp\sqrt\mu/g\gg1\); hence its normalized derivatives remain
uniform even when \(v=0\), which is precisely saddle entry or exit.

To see that differentiating the phase causes no loss, use the exact
identity

\[
 g\partial_g e(gv^2)={v\over2}\partial_v e(gv^2).     \tag{3.15}
\]

Integrating (3.15) by parts produces no boundary term, because both
collars vanish on neighborhoods of the two physical endpoints. On
\(|v|\ll g^{-1/2}\), (3.11)--(3.14) give the bound directly. On the
dyadic complements, repeated use of
\((4\pi igv)^{-1}\partial_v\) gives a convergent geometric series;
the bounds (3.12) and \(\sqrt\mu/g\gg1\) apply equally to a collar
piece. This proves the elementary centred-Fresnel estimate

\[
 |\mathfrak B^\circ(g)|+g|\partial_g\mathfrak B^\circ(g)|
 \ll {G/\sqrt\mu\over\sqrt g}
 \asymp {\sqrt G\over\sqrt\mu}
 ={J\delta\sqrt G\over\sqrt2\,k^{3/2}}.              \tag{3.16}
\]

This argument uses the complete integral; all Gaussian correction
terms are already present. Finally, join consecutive odd lifts by the
continuous extension in (3.10). The lift hull has length \(O(G)\), so

\[
 \sum_g|\mathfrak B^\circ(g+2)-\mathfrak B^\circ(g)|
 \le\int |\partial_t\mathfrak B^\circ(t)|dt
 \ll {J\delta\sqrt G\over k^{3/2}}.                  \tag{3.17}
\]

The endpoint term obeys the same bound by (3.16), proving (1.2)--(1.3).

## 4. First doubtful or unproved step

There is no false term in (77.9), (77.13), or (77.15)--(77.18) after
the fixed collars are interpreted as above. The first unsupported step
in the Round-76 discovery report was the sentence that pointwise
stationary phase by itself gives complete step-two bounded variation,
especially through a moving collar. A pointwise leading term would not
justify that assertion. Equations (3.8)--(3.16) repair the gap: the
exact homogeneity, the lift-independent ratio profile, the exact Morse
coordinate, and (3.15) control the physical \(g\)-derivative without
freezing the integral.

After this repair, the first genuinely unproved step is the reciprocal
resonance-union estimate obtained by summing (77.19) over
\((a,b,k)\):

\[
 \sum_{a,b,k}{J\delta\sqrt G\over k^{3/2}}
 \min\!\left(N_{a,b},{1\over2\|\Lambda/k\|}\right)
 \stackrel{?}{\ll}_\varepsilon L^2X^\varepsilon.      \tag{4.1}
\]

Nothing here permits absolute summation in (4.1), estimates the
resonance union, or improves the accepted energy bound.

## 5. Control tests and outcomes

1. **External normalization -- pass.** Only the normalized energy
   symbol (77.1) is used. The exterior physical factor is not inserted.
2. **Full endpoint samples -- pass.** Finite Poisson has both half
   samples; comparison with the collarized lattice sum absorbs the two
   full original samples exactly once in the \(O_M(L^2)\) primal
   ledger.
3. **Fixed collar capacity -- pass.** Each ordered pair loses only
   \(O_M(1)\) lattice samples. No growing-width collar is substituted.
4. **Actual symbol and finite support -- pass.** Equations
   (3.8)--(3.10) retain \(\eta_L,\Phi,W,q_X\), the actual lift interval,
   and every floor before the collar comparison.
5. **All Poisson modes -- pass.** Equation (3.5) sums zero, positive,
   negative exterior, equality, and remote modes. Interior negative
   modes are retained exactly.
6. **Stationary corrections -- pass.** No asymptotic stationary term is
   substituted, so the aggregate stationary-correction error is zero.
7. **Lift derivative and variation -- pass.** Equations
   (3.8)--(3.17) prove the stronger pointwise-plus-derivative theorem
   (1.2).
8. **Saddle entry and exit -- pass.** The primitive gap and
   \(L^2\le J\) give \(\mu\gg G^2\); a fixed physical collar is smooth
   on at least unit scale in the exact Morse coordinate. No Fresnel
   discontinuity occurs.
9. **Sharp ceiling modulo four -- pass with stated scope.** The sharp
   ceiling is in the primal collar error. If it is retained, the
   accepted step-four split is still necessary; (1.3) is not asserted
   for that symbol.
10. **Half-integral actual-profile family -- pass.** For
    \(X=T^4\), odd \(13\mid T\), \((a,b)=(81,121)\), and
    \(k=2T^2/13\), one has \(u_0=169/4\), both \(W\)-arguments on the
    unit plateau, and \(\Lambda/k\in\mathbb Z\). Formula (2.5) remains
    fully coherent, exactly as it must; the variation theorem supplies
    no fictitious cancellation.
11. **Nonresonant and \(\Phi\)-edge families -- pass.** The proof is
    uniform through both \(W\)-transitions. Near \(gb=H\), bounded
    \(\Phi'\) gives the same \(O(G^{-1})\) lift derivative, and the
    terminal lift is covered by the endpoint term in variation.
    Nonresonance enters only later through exact Abel summation.
12. **Rank-one return -- pass as scope control.** The complete
    reciprocal transform remains an adjoint self-return; (1.1) does
    not count it as a second saving.
13. **Coefficient adversary and false unsigned analogue -- fail for the
    analogue, as required.** Arbitrary bounded multipliers need not
    satisfy (3.11). Alternating or phase-conjugating them makes the
    step-two variation comparable to the sum of pointwise masses. The
    proof works only for the actual slowly varying, ratio-homogeneous
    symbol and does not prove an unsigned/adversarial energy estimate.
14. **Downstream scope -- pass.** Neither (4.1), the transposed energy,
    the signed cone, full M2, M9, endpoint uniformity, nor the global
    exponent is proved.

No numerical experiment and no external source were used.

## 6. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/derivation_packet.md`
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/briefs/centered_integral_variation_attack.md`
- `rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reports/gcd_lift_resonance_attack.md`
- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/derivation_packet.md`
- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/reports/reciprocal_energy_attack.md`
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/derivation_packet.md`

No sibling Round-77 report, proof draft, external source, or
computational artifact was used.

## 7. Recommended state effect

**Promote after the required independent seam reviews.** Record (2.5)
with the stronger \(O(L^2\log(2+L))\) aggregate error and record the
complete-integral derivative/variation theorem (1.2)--(1.3) as a scoped
internal actual-symbol lemma. The statement should explicitly say that
the sharp ceiling has been removed by a fixed primal collar and that
the actual property is the factorization (3.8)--(3.12), not arbitrary
coefficient boundedness.

Do not promote the reciprocal resonance union, the transposed energy,
the signed cone, M9-M2, M9, endpoint uniformity, or the Gauss-circle
exponent. The next analytic obligation is precisely (4.1), with the
actual coefficient weight and step-two distance retained.
