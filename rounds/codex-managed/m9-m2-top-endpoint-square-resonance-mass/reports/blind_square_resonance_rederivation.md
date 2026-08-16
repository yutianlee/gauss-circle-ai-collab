## 1. Result.

The square-ray identities (78.5)--(78.9) and the combined-lift phase (C78.1) are exact.  The differential identity (C78.2), reciprocal curvature scale (C78.7), weighted reciprocal-mode estimate (C78.8), and aggregate count (C78.9) are also correct.

The newly supplied exact normalization (C78.3E), symbol (C78.3a), and uniform seminorms (C78.3b) prove the complete-integral variation claim (C78.6), its smooth-collar Gaussian remainder, and its sampled endpoint control.  In particular, \(E(g)\) is \(k\)-independent and uniformly bounded, and the two collars are uniform fixed profiles.  The proof is unconditional under the now-complete authorized statement-only data.  An arbitrary rescaling of \(E(g)\) would destroy (C78.6), but (C78.3E) excludes that hostile analogue.

Consequently, if the factorisation (C78.3) is literal with those uniform symbol bounds, then
\[
 |\mathcal S_L^\square(X)|
 \ll L^2\log(2+L)
 \ll_\varepsilon L^2X^\varepsilon.                 \tag{R78.1}
\]
This proves the signed target (78.10) at the statement-only interface.

The absolute Abel majorant claim (78.12) remains false.  One fixed populated square ray contributes
\[
 \mathcal M_L^\square(X)\gg_L X^{1/4}
\]
along a fourth-power sequence.  That obstruction comes from summing the unit floor
\(\min(N,(2\|\theta\|)^{-1})\geq1\) over \(\asymp J\) reciprocal modes, not from confusing an exact resonant mode with the signed sum.  Thus the signed proof and the absolute-majorant no-go are compatible.

## 2. Exact statement and hypotheses.

Let \(s,t\) be coprime odd integers with \(s<t<2s\), let
\[
 t=s+2u,\qquad A=Ju,\qquad
 I_{s,u}=(Ju/s,2Ju/t),
\]
and let \(g\) be an admissible odd lift with \(gt^2\asymp L\).  Put
\[
 K\asymp Ju/s,\qquad h=gk,\qquad r=A/k,\qquad
 w\asymp(gs)^{-1},\qquad
 \rho={w^{-2}\over gK}\asymp{L\over K}.
\]
Assume the complete coefficient has the exact form
\[
 \mathfrak B^\circ(g,k)
 =g^{-2}E(g)\int q_g(\tau)
 e\!\left(gk(\tau-A/k)^2\right)d\tau,               \tag{R78.2}
\]
where:

1. \(E(g)\) is the exact \(k\)-independent factor
\[
 E(g)=\eta_L(gs^2)\overline{\eta_L(gt^2)}
 \Phi\!\left({gs^2\over H+1}\right)
 \overline{\Phi\!\left({gt^2\over H+1}\right)},
 \qquad |E(g)|\ll1;                                 \tag{R78.2E}
\]
2. \(q_g\) is independent of \(k\) and is the literal symbol
\[
\begin{aligned}
 q_g(\tau)={}&2\tau P_{s^2,t^2}(\tau^2)
 \rho\!\left({g(\tau^2-t^2/4)\over M}\right)
 \rho\!\left({g(s^2-\tau^2)\over M}\right),\\
 P_{s^2,t^2}(v)={}&
 L^3(st)^{-3/2}v^{-3/2}
 W\!\left(\sqrt{{q_Xs^2\over4v}}\right)
 \overline{W\!\left(\sqrt{{q_Xt^2\over4v}}\right)};
\end{aligned}                                      \tag{R78.2a}
\]
3. its size is \(Q_0\asymp g^3s\), its broad interior varies on scale \(s\), its two physical collars have width \(w\asymp(gs)^{-1}\), and for every fixed \(m\geq1\),
\[
 \|q_g'\|_1\ll Q_0,\qquad
 \|q_g^{(m)}\|_1\ll_m Q_0w^{1-m},\qquad
 \|q_g^{(m)}\|_\infty\ll_m Q_0w^{-m};               \tag{R78.2b}
\]
in particular, for every fixed \(j\geq0\),
\[
 \|q_g^{(2j+1)}\|_1
 +\|q_g^{(2j)}\|_\infty
 \ll_j Q_0w^{-2j},                                  \tag{R78.3}
\]
and the exact fixed profiles in (R78.2a) give uniform rescaled-profile Schwartz seminorms;
4. the lift floors and endpoint stars only select \(g\) or multiply its coefficient by a \(k\)-independent factor of modulus at most one.

Then, uniformly on the open interval \(I_{s,u}\),
\[
 \sup_k|\mathfrak B^\circ(g,k)|
 +\operatorname{Var}_{k\in I_{s,u}}\mathfrak B^\circ(g,k)
 \ll\sqrt{gt^2/K}.                                  \tag{R78.4}
\]
The same bound controls the variation of the sampled sequence on
\(I_{s,u}\cap\mathbb Z\).  With
\[
 f(k)=-gXu^2/k,\qquad
 \lambda={gs^3\over Ju},
\]
one then has
\[
 \left|\sum_{k\in I_{s,u}\cap\mathbb Z}
 \mathfrak B^\circ(g,k)e(f(k))\right|
 \ll M\lambda+1
 \ll gs(2s-t)+1
 \ll L+1,                                           \tag{R78.5}
\]
where \(M\asymp Ju(2s-t)/(st)\) is the real interval length when that length is at least one.  Empty and one-point sampled intervals obey the same conclusion.

Finally,
\[
 \sum_{s\ll\sqrt L}\ \sum_{1\leq u<s/2}
 \#\mathcal G_{s^2,(s+2u)^2}
 \ll L\log(2+L),                                    \tag{R78.6}
\]
so (R78.1) follows.

Separately, let \(X=T^4\), \(J=T^2\), and let \(T\) tend to infinity through multiples of \(13\).  Fix a scale \(L=L_0\) for which the stated actual-weight-one control on \((s,t,u)=(9,11,1)\) supplies a lift, and write
\[
 N_0=N_{81,121}\geq1,\qquad G_0=G_{9,11}>0.
\]
Taking \(H=L_0\), all scale hypotheses hold for large \(T\), and
\[
 \mathcal M_{L_0}^\square(T^4)
 \gg\sqrt{G_0}\,T
 =\sqrt{G_0}\,X^{1/4}.                              \tag{R78.7}
\]
Hence (78.12) fails for any fixed \(0<\varepsilon<1/4\).

## 3. Proof or derivation.

For coprime positive integers \(a,b\), their prime supports are disjoint.  Thus \(ab\) is a square exactly when every exponent in \(a\) and in \(b\) is separately even:
\[
 ab=\square\quad\Longleftrightarrow\quad
 a=s^2,\quad b=t^2.
\]
Oddness and coprimality pass to \(s,t\), while \(a<b<4a\) is exactly
\(s<t<2s\).  Since \(s,t\) are odd, \(t=s+2u\) with \(u\geq1\), and
\[
 (s,t)=(s,s+2u)=(s,u)
\]
because \(s\) is odd.  Hence \(1\leq u<s/2\) and \((s,u)=1\).

Direct substitution gives
\[
 \delta=2u,\qquad
 {b-a\over4}=u(s+u),\qquad
 \Lambda=2Xu^2,
\]
\[
 e(\alpha)=e\!\left(u(s+u)-{Xu^2\over k}\right)
 =e(-Xu^2/k),
\]
and
\[
 {Ju\over s}<k<{2Ju\over t}.
\]
The inequalities are strict, including when an endpoint happens to be integral.  Also \(G\asymp L/t^2\), and
\((b-a)/2=2u(s+u)\) is even.  Substitution in (78.1) gives (78.9) with the original one-count \(s<t\) and external \(2\Re\).  If \(g=2n+1\), the two displayed reciprocal phases combine exactly:
\[
 e(-Xu^2/k)e(-2nXu^2/k)=e(-gXu^2/k).                \tag{R78.8}
\]

The centred phase
\[
 \psi(k,\tau)=k(\tau-A/k)^2
 =k\tau^2-2A\tau+A^2/k
\]
satisfies
\[
 \partial_k\psi=(\tau-A/k)(\tau+A/k),\qquad
 \partial_\tau\psi=2k(\tau-A/k).
\]
Multiplication by the derivative of \(e(g\psi)\) proves
\[
 k\partial_ke(g\psi)
 ={\tau+A/k\over2}\partial_\tau e(g\psi),
\]
which is (C78.2).  This identity is not used as a pointwise collar derivative bound.

The scale assertions (C78.3b) agree with the literal symbol.  On its support,
\(\tau\asymp s\asymp t\) and \(gt^2\asymp L\).  Thus the algebraic part of
\(P_{s^2,t^2}(\tau^2)\) has scale
\[
 L^3(st)^{-3/2}(\tau^2)^{-3/2}
 \asymp L^3s^{-6}\asymp g^3,
\]
and multiplication by \(2\tau\) gives \(Q_0\asymp g^3s\).  Differentiation of the broad algebraic and \(W\)-profile factors costs \(s^{-1}\).  At either physical cutoff, differentiation costs \(w^{-1}\asymp gs\), while the set on which that derivative is supported has length \(O(w)\).  The product rule therefore gives
\[
 \|q_g^{(m)}\|_\infty\ll_mQ_0w^{-m},\qquad
 \|q_g^{(m)}\|_1\ll_mQ_0w^{1-m},
\]
and for \(m=1\) the broad interior and the two collars each contribute
\(O(Q_0)\).  This rederives (C78.3b) from (C78.3a), using the review's stated fixed profiles and collar width; the broad interior terms are smaller than the collar bounds.

To prove the smooth-collar remainder, use
\(\widehat q(\xi)=\int q(\tau)e(-\tau\xi)d\tau\).  The exact Fresnel formula gives, for \(h>0\),
\[
 \int q(\tau)e(h(\tau-r)^2)d\tau
 ={e(1/8)\over\sqrt{2h}}
 \int\widehat q(\xi)e(r\xi)e(-\xi^2/(4h))d\xi.       \tag{R78.9}
\]
Taylor expansion of the last multiplier gives
\[
 \int q(\tau)e(h(\tau-r)^2)d\tau
 ={e(1/8)\over\sqrt{2h}}
 \sum_{j<N}c_jh^{-j}q^{(2j)}(r)+R_N(h,r),           \tag{R78.10}
\]
with constants \(c_j\) depending only on the Fourier convention.

It remains to justify the uniform remainder at a crossing rather than merely state a formal stationary-phase series.  On one collar write
\[
 q(\tau)=Q\Phi((\tau-c)/w),\qquad
 R=(r-c)/w,\qquad \eta=(hw^2)^{-1}.
\]
After the changes \(\zeta=w\xi\) and \(R=(r-c)/w\), the normalized remainder in (R78.10) is the inverse Fourier transform of
\[
 \widehat\Phi(\zeta)
 \left[
 e(-\eta\zeta^2/4)
 -\sum_{j<N}d_j(\eta\zeta^2)^j
 \right].                                          \tag{R78.11}
\]
The bracket and its \(\eta\partial_\eta\) derivative are
\(O_N(\eta^N|\zeta|^{2N})\).  Because \(\Phi\) is one fixed
\(C^\infty_c\) profile, its Fourier transform is Schwartz.  Applying the same observation after finitely many \(\zeta\)-derivatives shows that the inverse transform in (R78.11), its \(R\)-derivative in \(L^1(dR)\), and its \(\eta\partial_\eta\) derivative have total size
\[
 O_N(\eta^N).                                      \tag{R78.12}
\]
This is the needed value, crossing-variation, and logarithmic-\(h\) control.  Rescaling the fixed interior profile at scale \(s\) gives the same statement with \((hs^2)^{-1}\), which is no larger than the collar parameter \(\eta\).  Summing the fixed finite number of pieces yields
\[
 \sup_r|R_N(h,r)|
 +\operatorname{Var}_r R_N(h,r)
 +\sup_r|h\partial_hR_N(h,r)|
 +\operatorname{Var}_r(h\partial_hR_N(h,r))
 \ll_N {Q_0\over\sqrt h}
 \left({w^{-2}\over h}\right)^N.                   \tag{R78.13}
\]
The \(r\)-variation may be restricted to the physical interval, so it only decreases.  This fixed-profile proof is also why replacing a collar by a sharp endpoint would be invalid: its Fourier transform would not supply the Schwartz bounds used in (R78.12).

Now \(h=gk\asymp gK\), \(r=A/k\) is monotone and crosses the physical interval once, and
\[
 \rho={w^{-2}\over gK}
 ={gs^2\over K}
 \asymp {L\over K}
 \ll1,
\]
since \(J\geq L^2\), \(u\geq1\), \(s\ll\sqrt L\), and
\(K\asymp Ju/s\).  For the \(j\)-th displayed term of (R78.10), (R78.3) and monotonicity of \(r\) give
\[
 \sup_k+\operatorname{Var}_k
 \ll {Q_0\over\sqrt{gK}}\rho^j.                    \tag{R78.14}
\]
Variation of the factor \(h^{-j-1/2}\) costs only the same amount because \(k\) changes by a bounded ratio.  Formula (R78.13) treats the remainder, including the simultaneous changes in \(h\) and \(r\).  Therefore
\[
 \sup_k|\mathfrak B^\circ(g,k)|
 +\operatorname{Var}_k\mathfrak B^\circ(g,k)
 \ll g^{-2}{Q_0\over\sqrt{gK}}
 \asymp{\sqrt g\,s\over\sqrt K}
 \asymp\sqrt{gt^2/K},
\]
which proves (R78.4), hence (C78.6), under the explicit hypotheses of Section 2.

For the reciprocal-mode sum,
\[
 f''(k)=-{2gJ^2u^2\over k^3}.
\]
Since \(k\asymp Ju/s\) throughout the interval,
\[
 |f''(k)|\asymp\lambda={gs^3\over Ju}
 \asymp{gt^2\over K}.
\]
Furthermore \(\lambda\ll1\).  The second-derivative estimate, uniformly on every initial subinterval, is
\[
 \left|\sum e(f(k))\right|
 \ll M\sqrt\lambda+\lambda^{-1/2}.
\]
Discrete Abel summation and (R78.4) therefore give
\[
 \left|\sum_k\mathfrak B^\circ(g,k)e(f(k))\right|
 \ll\sqrt\lambda
 \left(M\sqrt\lambda+\lambda^{-1/2}\right)
 \ll M\lambda+1.
\]
The exact real interval length is
\[
 {Ju(2s-t)\over st},
\]
and hence
\[
 M\lambda
 \ll {Ju(2s-t)\over st}{gs^3\over Ju}
 \ll gs(2s-t)\ll gt^2\ll L.
\]
If there are no sampled integers the sum is zero.  If there is one, (R78.4) gives \(O(\sqrt\lambda)\), which is covered by the \(+1\).  Thus (R78.5) is valid without inserting closed endpoints.

For each fixed \(s,u\), the dyadic lift condition \(gt^2\asymp L\) gives
\[
 \#\mathcal G_{s^2,t^2}\ll {L\over t^2}.
\]
It also forces \(s\ll\sqrt L\).  Ignoring coprimality and oddness only enlarges the count, so
\[
 \begin{aligned}
 \sum_{s\ll\sqrt L}\sum_{1\leq u<s/2}
 \#\mathcal G_{s^2,(s+2u)^2}
 &\ll
 L\sum_{s\ll\sqrt L}\sum_{u<s/2}{1\over(s+2u)^2}\\
 &\ll
 L\sum_{s\ll\sqrt L}{1\over s}
 \ll L\log(2+L).
 \end{aligned}
\]
Summing (R78.5) over these triples and restoring \(2\Re\) proves
\[
 |\mathcal S_L^\square(X)|\ll L^2\log(2+L).
\]
Since \(L\leq X^{1/4}\), the logarithm is \(O_\varepsilon(X^\varepsilon)\), proving (R78.1).

The absolute-majorant obstruction is independent.  On the ray
\((s,t,u)=(9,11,1)\), its integer mode interval is
\[
 I_T=(T^2/9,2T^2/11),\qquad |I_T|=7T^2/99.
\]
It contains at least \(7T^2/198\) integers for large \(T\).  For every such integer,
\[
 \min\!\left(N_0,{1\over2\|2T^4/k\|}\right)\geq1
\]
and
\[
 {2T^2\sqrt{G_0}\over k^{3/2}}
 \gg{\sqrt{G_0}\over T}.
\]
Their positive sum proves (R78.7), contradicting (78.12) for, say,
\(\varepsilon=1/8\).

The distinguished mode \(k_0=2T^2/13\) is integral for \(13\mid T\) and is strictly interior because
\[
 {1\over9}<{2\over13}<{2\over11}.
\]
At this mode,
\[
 {2Xu^2\over k_0}=13T^2,\qquad
 e(-2nXu^2/k_0)=1,\qquad
 e(-Xu^2/k_0)=(-1)^T.
\]
It certifies the absence of an invented in-lift character cancellation, but the majorant lower bound uses the whole long interval rather than this single resonant mode.

Exact and near resonance remain distinct.  Exact resonance is
\[
 2Xu^2=mk
\]
for an integer \(m\); for integral \(X\) this is \(k\mid2Xu^2\), while irrational \(X\) has no exact resonance.  Saturation at the Abel window is instead
\[
 \left\|{2Xu^2\over k}\right\|\leq{1\over2N},
\]
equivalently, for some \(m\in\mathbb Z\),
\[
 \left|X-{mk\over2u^2}\right|
 \leq{k\over4Nu^2}.                                 \tag{R78.15}
\]
Thus divisor counting cannot replace metric counting at the actual window.

Finally, the reciprocal transform is rank one and self-returning.  With
\(B=(2n+1)Xu^2>0\), the phase \(-B/k-mk\) has saddle
\(k=\sqrt{B/m}\) and value \(-2\sqrt{Bm}\).  Differentiating the dual phase returns \(-k\), so its inverse transform returns the original reciprocal phase.  A second transform is not an independent gain.

## 4. First doubtful or unproved step.

There is no remaining analytic gap between (C78.3a)--(C78.3b), the bounded normalization \(|E(g)|\ll1\), and (C78.6)--(C78.10): the exact-profile Fourier argument proves the collar remainder, the sampled variation, the weighted mode sum, and the aggregate count.

No doubtful or unproved step remains for the signed square-family theorem under the authorized statement-only packet.  The exact readback (C78.3E) identifies \(E(g)\) as a product of fixed normalized \(\eta_L\)- and \(\Phi\)-profiles, proves its \(k\)-independence, and supplies \(|E(g)|\ll1\).  The added (C78.3a)--(C78.3b) likewise close the complete-symbol and collar-seminorm gates.

The first failure under an adversarial change of hypotheses would be multiplication of \(E(g)\) by an unbounded parameter-dependent factor: it would scale the left side of (C78.6) without scaling its right side.  This is a useful hostile control, not an unproved step for the actual coefficient.

## 5. Required control test and outcome.

1. **External normalization and one-count \(2\Re\): passed.**  The restriction \(s<t\) counts one orientation, and \(2\Re\) restores its conjugate partner.  No additional factor appears in the square substitution or aggregate sum.

2. **Equations (78.5)--(78.9) and (C78.1)--(C78.2): passed.**  Coprimality, odd parity, \(u<s/2\), the integer phase, combined lift phase, centred differential identity, and both strict \(k\)-inequalities were derived exactly.

3. **Complete integral, normalization, collars, floors, stars, and finite lifts: passed.**  The audit uses the exact bounded factor (C78.3E) and the literal \(q_g\) and \(P_{s^2,t^2}\) in (R78.2a), not a first stationary value.  The seminorms (C78.3b) and the two fixed smooth collars give the Schwartz remainder bound (R78.13).  Floors select the finite \(g\)-set, and stars of modulus at most one do not enlarge variation when they are \(k\)-independent.  A sharp physical endpoint would fail this proof.

4. **Gaussian remainder and sampled endpoint terms: passed.**  Rescaling a fixed collar reduces the remainder to (R78.11); its value, total crossing variation, and logarithmic-\(h\) derivative are \(O_N(\rho^N)\).  Restricting continuous variation to open-interval integer samples creates no endpoint term.  Empty and one-point samples are covered separately.

5. **Weighted reciprocal \(k\)-sum: passed.**  The curvature is \(\lambda\asymp gt^2/K\ll1\), Abel multiplies the second-derivative bound by \(\sup+\operatorname{Var}\ll\sqrt\lambda\), and the result is \(M\lambda+1\ll L+1\).

6. **Aggregate lift count: passed.**  The bound
\(\#\mathcal G_{s^2,t^2}\ll L/t^2\), followed by the \(u\)- and harmonic \(s\)-sums, gives \(L\log(2+L)\).

7. **Signed target versus absolute majorant: passed.**  The corrected complete-integral lemma proves (78.10), while the independent positive lower bound (R78.7) refutes (78.12).  Neither conclusion is inferred from the other.

8. **Exact versus metric resonance and fourth-power control: passed.**  Formula (R78.15) uses the actual \(1/(2N)\) window.  The fourth-power mode is integral, strictly interior, exactly resonant, has trivial lift character, and retains the outer sign \((-1)^T\).

9. **Small parameters, one-point lifts, and endpoints: passed.**  The first possible odd square ray is \((s,u,t)=(3,1,5)\).  Strict integer mode intervals may be empty.  One-point intervals use the value part of (R78.4), and integer endpoints are excluded.  A lift star can only reduce the estimate under the \(k\)-independence hypothesis.

10. **Cancellation, adversarial coefficients, and rank-one return: passed.**  The proof uses signed reciprocal curvature before absolute summation over triples.  Arbitrary coefficients controlled only raywise would still encounter the majorant no-go.  The reciprocal Legendre transform self-returns and supplies no second gain.

11. **Separation from later goals: passed.**  No claim is made for nonsquare rays, the full energy, \(M2\), \(M9\), endpoint uniformity, or the global exponent.

## 6. Dependencies and exact artifacts used.

Only the following three artifacts were read:

1. rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/derivation_packet.md.
2. rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/briefs/blind_square_resonance_rederivation.md.
3. rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/reviews/conductor_round78_preliminary_algebra.md.

The accepted inputs used are (78.1)--(78.14) and the exact factorisation, normalization, symbol, seminorm, and scale assertions (C78.1)--(C78.9), including (C78.3E) and (C78.3a)--(C78.3b).  No graph, proof draft, strategy file, earlier-round report, sibling report, source card, or external source was consulted.

## 7. Recommended state effect.

**Promote** the square-family theorem (R78.1).  The exact bounded normalization (C78.3E), definitions (C78.3a), seminorms (C78.3b), Gaussian remainder, smooth-collar crossings, sampled variation, weighted \(k\)-sum, and aggregate arithmetic have all been independently audited.

**Promote** the route no-go theorem that (78.12) is false, retaining the quantitative lower bound (R78.7) and the explanation that its source is the unit Abel floor over a long \(k\)-interval.

Retain the arbitrary-\(E(g)\) rescaling example only as a hostile control showing why (C78.3E) is necessary.  Make no state change to generic rays, the full energy, \(M2\), \(M9\), endpoint uniformity, or the exponent.
