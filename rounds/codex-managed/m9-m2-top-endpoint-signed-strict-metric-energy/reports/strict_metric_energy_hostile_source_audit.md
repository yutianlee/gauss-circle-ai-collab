# Round 80 hostile/source audit: the actual carrier fills the alleged spectral gap

Campaign: `m9-m2-top-endpoint-signed-strict-metric-energy`  
Task: `strict_metric_energy_hostile_source_audit`  
Role: `source_auditor`  
Access mode: `selected_context`  
Starting graph SHA-256: `cb007911c1e9d407d9adbc8919ce44cc3eaab411a212d0925e1176f5a154a43a`  
Status: candidate evidence only; no shared proof state is edited.

## 1. Result

**Actual-carrier return and parity no-go lemma.**  The proposed nearest-integer-parity or half-integer-spectral-gap closure is false for the complete Round-77 coefficient.  Put

\[
 \theta_{a,b,k}=\frac{\Lambda}{k}
 =\frac{X(\sqrt b-\sqrt a)^2}{2k}
\]

and define the uncentred complete integral

\[
 \mathfrak C^\circ_{a,b,k}(g)
 :=g\int_{b/4}^{a}A^\circ_{ga,gb}(gu)
 e\!\left(g\bigl(ku-J(\sqrt b-\sqrt a)\sqrt u\bigr)\right)\,du .
 \tag{80.H1}
\]

In the original variables \(h=ga\), \(s=gb\), and \(x=gu\), this is exactly

\[
 \mathfrak C^\circ_{a,b,k}(g)
 =\int_{s/4}^{h}A^\circ_{h,s}(x)
 e\!\left(kx-J(\sqrt s-\sqrt h)\sqrt x\right)\,dx,
 \qquad (-1)^q=\chi_4(h)\chi_4(s).                 \tag{80.H1a}
\]

Then, identically and with the complete actual symbol still present,

\[
 \mathfrak B^\circ_{a,b,k}(g)
 =e(g\theta_{a,b,k}/2)\mathfrak C^\circ_{a,b,k}(g).       \tag{80.H2}
\]

If \(\theta=\ell+\eta\), with either nearest-integer tie convention, and \(g\) is odd, then

\[
 \boxed{
 (-1)^{q+\ell}\mathfrak B^\circ_{a,b,k}(g)e(-g\eta/2)
 =(-1)^q\mathfrak C^\circ_{a,b,k}(g).}
 \tag{80.H3}
\]

Thus the quotient parity \((-1)^\ell=(-1)^{p/k}\) does not remain as an independent sign in the complete summand.  It is cancelled exactly by the carrier phase already inside \(\mathfrak B^\circ\).  Likewise, although \(W_R(\theta)e(-g\theta/2)\) alone has only half-integral Fourier frequencies, multiplication by the actual coefficient shifts them back to the integral frequencies of \(W_R\), including its zero mode.  The density term therefore survives literally.  The transform has returned to the original rank-one phase \(g(ku-J\delta\sqrt u)\); it has not acquired a new spectral gap.

This is a rigorous no-go for any closure using (i) nearest-integer parity alone, (ii) the absence of a zero Fourier frequency after suppressing the phase carried by \(\mathfrak B^\circ\), or (iii) only the pointwise scale and step-two variation bound for \(\mathfrak B^\circ\).  Equation (80.H1a) shows that the alleged new metric-parity transform is a literal return to the residual actual-symbol two-character correlation in the original \((h,s,x)\) variables.  It is **not** a counterexample to (80.14): cancellation in that remaining \(\chi_4(h)\chi_4(s)\)-signed correlation is still possible and is not estimated here.

## 2. Exact statement and hypotheses

Let \(\mathcal T_{A,D,K,G}^{\mathrm{res}}\) be one literal residual block of primitive odd coprime triples \(\tau=(a,b,k)\) satisfying

\[
 a\asymp A,\qquad b-a\asymp D,\qquad k\asymp K,
 \qquad G_{a,b}\asymp G,
\]

the open reciprocal inequalities (80.1), \(ab\ne\square\), exclusion of exact nonsquare centres, and

\[
 AJD^3\gg L^3.                                      \tag{80.H4}
\]

All floors, stars, fixed physical collars, profiles, lift endpoints, and saddle transitions are those inside \(A^\circ_{ga,gb}\); none is replaced by a majorant.  Let \(g\) range over the actual finite odd set \(\mathcal G_{a,b}\).  Let \(W_R\) be the fixed period-one smooth strict-metric window, with

\[
 W_R(t)=\mu_R+\sum_{r\ne0}\widehat W_R(r)e(rt),
 \qquad \mu_R\asymp R^{-1}.                         \tag{80.H5}
\]

The lemma consists of the following four exact assertions.

1. Equations (80.H2) and (80.H3) hold term by term, including at a nearest-integer tie and for an empty or singleton reciprocal interval.

2. If

\[
 Z_r:=\sum_{\tau\in\mathcal T_{A,D,K,G}^{\mathrm{res}}}
 (-1)^{q_\tau}e(r\theta_\tau)
 \sum_{g\in\mathcal G_{a,b}}\mathfrak C^\circ_\tau(g),
 \tag{80.H6}
\]

then the exact windowed block is

\[
 \boxed{
 \mathcal S_R
 =\mu_R Z_0+\sum_{r\ne0}\widehat W_R(r)Z_r.}
 \tag{80.H7}
\]

In particular, the mean and centred discrepancy have not separated into a harmless density and a cancellative error: \(Z_0\) is a complete actual-symbol signed sum which still needs an estimate.

3. On a product fiber \(p=\ell k\), the *bare* quotient signs have no uniform cancellation.  If \(p=2^v m\), \(m\) odd, then on the full divisor set

\[
 \sum_{k\mid p}(-1)^{p/k}
 =\sum_{d\mid p}(-1)^d=(v-1)\tau(m).                \tag{80.H8}
\]

This is \(-\tau(p)\) for odd \(p\), vanishes only when \(v=1\), and is positive for \(v\ge2\).  A dyadically truncated divisor interval need not even retain the exceptional \(v=1\) cancellation.  More decisively, (80.H3) removes \((-1)^{p/k}\) from the actual complete summand before any divisor cancellation can be invoked.

4. The hard residual set contains arithmetic controls on which \(q\) is constant, strict metric hits recur at prescribed nearest-integer parity, and the modes can lie on one odd product fiber.  These controls invalidate a universal parity-balance premise, while making no coefficient lower-bound claim.

The conclusion is limited: a successful next argument may still exploit the exact \((-1)^q=\chi_4(a)\chi_4(b)\) sign together with the full cross-row structure of \(\mathfrak C^\circ\).  It may not infer that saving from quotient parity, a formal half-frequency gap, or the Round-77 variation estimate alone.

## 3. Proof or derivation

The constant used to centre (80.2) is exactly half of \(\theta\):

\[
 \frac{X(\sqrt b-\sqrt a)^2}{4k}=\frac{\theta}{2}.
\]

It is independent of \(u\), so it factors out of the complete integral without changing any component of its amplitude or support.  This proves (80.H2).  Now \((-1)^\ell=e(\ell/2)\), \(\theta=\ell+\eta\), and \((g+1)/2\in\mathbb Z\).  Hence

\[
\begin{aligned}
 (-1)^{q+\ell}\mathfrak B^\circ(g)e(-g\eta/2)
 &=(-1)^q e(\ell/2)e(g(\ell+\eta)/2)
    e(-g\eta/2)\mathfrak C^\circ(g)\\
 &=(-1)^q e((g+1)\ell/2)\mathfrak C^\circ(g)\\
 &=(-1)^q\mathfrak C^\circ(g).
\end{aligned}
\]

Also \(dx=g\,du\), \(\sqrt s-\sqrt h=\sqrt g\,\delta\), and
\(\sqrt x=\sqrt g\sqrt u\), which proves the original-variable identity
(80.H1a).  Since \(h,s,g,a,b\) are odd,

\[
 \chi_4(h)\chi_4(s)
 =\chi_4(g)^2\chi_4(a)\chi_4(b)
 =\chi_4(a)\chi_4(b)=(-1)^{(b-a)/2}=(-1)^q.
\]

Thus the only literal character left after carrier cancellation is precisely the original transposed-row product \(\chi_4(h)\chi_4(s)\); the nearest-centre character is not additional arithmetic information.

Changing the tie representative from \((\ell,\eta)\) to \((\ell+1,\eta-1)\) multiplies both nearest-integer factors by \(-1\), so the identity is tie invariant.  This also verifies directly the external normalization and the combined odd-lift phase: no factor of two or extra outer real part has entered.

There is a tempting but incomplete spectral observation:

\[
 W_R(\theta)e(-g\theta/2)
 =\sum_{r\in\mathbb Z}\widehat W_R(r)
 e((r-g/2)\theta),                                  \tag{80.H9}
\]

and \(r-g/2\ne0\) for odd \(g\).  The observation ceases to be relevant once the actual coefficient is restored.  By (80.H2),

\[
 W_R(\theta)\mathfrak B^\circ(g)e(-g\theta/2)
 =W_R(\theta)\mathfrak C^\circ(g)
 =\sum_{r\in\mathbb Z}\widehat W_R(r)e(r\theta)
  \mathfrak C^\circ(g).                             \tag{80.H10}
\]

The carrier \(e(g\theta/2)\) fills the alleged half-integral gap exactly.  Summing (80.H10) gives (80.H7), whose \(r=0\) term is \(\mu_R Z_0\).  Expanding the square in the centred phase also shows the return explicitly:

\[
 k\left(\sqrt u-\frac{J\delta}{2k}\right)^2
 -\frac{\theta}{2}=ku-J\delta\sqrt u.              \tag{80.H11}
\]

Thus a Fourier shift or a second reciprocal re-enumeration has not created independent curvature; it has restored the collar-extracted uncentred phase.

For (80.H8), put \(d=p/k\).  There are \(\tau(m)\) odd divisors of \(p\), and, when \(v\ge1\), there are \(v\tau(m)\) even divisors.  Since \((-1)^d\) is \(-1\) on odd \(d\) and \(+1\) on even \(d\), their difference is \((v-1)\tau(m)\).  For odd \(p\), every quotient \(p/k\) is odd, so the sign is perfectly coherent on every truncated fiber as well.

Here is a literal near-square Pell fiber.  Take

\[
 (a,b)=(25,27)=(5^2,3\cdot3^2),\qquad q=1,
 \qquad \delta=3\sqrt3-5,
\]

so

\[
 \lambda:=\frac{\delta^2}{2}=26-15\sqrt3.
\]

The pair is odd, primitive, satisfies \(b=a+2<4a\), and
\(ab=3\cdot15^2\) is nonsquare.  Put

\[
 p_0=8925,qquad
 \mathcal K_0=\{15,17,21,25\}.
\]

The quotients \(p_0/k_0\) are respectively
\(595,525,425,357\), all odd, while

\[
 \frac{p_0}{k_0^2}\in
 \left\{\frac{119}{3},\frac{525}{17},
              \frac{425}{21},\frac{357}{25}\right\}
 \subset (27/2,50).                                 \tag{80.H12}
\]

For any \(R\ge1\) and any odd integer \(Q\), define

\[
 p=p_0Q^2,\quad k=k_0Q,\quad
 \ell=\frac{p_0}{k_0}Q,\quad
 \Delta=\frac{5Q}{R},\quad
 X=\frac{p+\Delta}{\lambda}.                       \tag{80.H13}
\]

Then

\[
 \theta=\frac{X\lambda}{k}
 =\ell+\frac{5}{Rk_0},
 \qquad \frac1{5R}\le\eta\le\frac1{3R}<\frac12. \tag{80.H14}
\]

All four modes are therefore strictly metric and lie in one dyadic \(K\)-range.  Since \(\lambda=\delta^2/2\), the reciprocal interval is exactly equivalent to

\[
 \frac b2<\frac{p+\Delta}{k^2}<2a.                 \tag{80.H15}
\]

Equations (80.H12)-(80.H13) put all four modes strictly inside it.  Every \(\ell\) is odd, so the displayed nearest-integer sign \((-1)^{q+\ell}\) is \(+1\) on the whole fiber.  The complete summand is nevertheless, by (80.H3), \(-\mathfrak C^\circ(g)\) on the whole ray.  The coefficient has not been bounded below; the conclusion is only that neither quotient parity nor mode parity supplies cancellation.

This control can be placed beyond the safe boundary.  Here \(A\asymp25\), \(D\asymp2\), and \(J\asymp Q\).  After choosing any lawful \(L\) and populated lift scale, take \(Q\gg L^3\); then \(AJD^3\gg L^3\) and also \(L\le J^{1/2}\).  Thus it is not a square ray, exact centre, or Round-79 positive-safe block.

Perfect powers do not restore a parity gap.  For the same Pell ray,

\[
 \frac{3\sqrt3-5}{10}<\frac1{32}
 <\frac{3\sqrt3-5}{3\sqrt3}.                       \tag{80.H16}
\]

For \(d=1,2\), take \(X=T^{2d}\), \(J=T^d\), and
\(k=T^d/32\), with \(32\mid T\).  The mode is strictly inside (80.1) and

\[
 \theta=32(26-15\sqrt3)T^d.                        \tag{80.H17}
\]

As \(T\) runs through multiples of \(32\), \(\theta/2\) is a real polynomial with an irrational nonconstant coefficient.  Weyl's theorem therefore gives equidistribution modulo one.  For each fixed \(R\), either parity of \(\ell\), either sign of \(\eta\), and any fixed strict annulus \(c_1/R<|\eta|<c_2/R\) occur infinitely often.  Taking \(T\) later and larger places the block beyond (80.6).  This proves the perfect-square and fourth-power metric recurrence control.  It is qualitative in \(R\), and no shrinking-window rate or actual-symbol lower bound is inferred.

Finally, the Round-77 variation estimate alone cannot close the sum.  On the hostile analogue \(R\asymp G\), coefficients

\[
 \widetilde B_\tau(g)=V_\tau\phi(g/G)e(g\eta_\tau/2)
\]

obey \(|\widetilde B|+g|\partial_g\widetilde B|\ll V_\tau\) for a fixed smooth compactly supported \(\phi\), yet they cancel the residual lift phase pointwise.  An outer phase can align the remaining rows.  Such arbitrary coefficients are forbidden in the theorem, so this is only a false-analogue control.  The stronger actual observation is (80.H2): the genuine complete coefficient already carries exactly the phase which defeats the proposed half-frequency argument.

## 4. First doubtful or unproved step

The first unproved step is now isolated without a fictitious quotient sign.  One must prove, with the complete \(A^\circ\) and the literal residual set,

\[
 \sum_{A,D,K,G,R}
 \left|\mu_R Z_0+
       \sum_{r\ne0}\widehat W_R(r)Z_r\right|
 \ll_\varepsilon L^2X^\varepsilon,                 \tag{80.H18}
\]

or an equivalent one-count estimate before dyadic triangle inequality.  No bound in the permitted context controls \(Z_0\) at the required scale.  The known \(1/R\) incidence density only accounts for \(\mu_R\); it does not estimate the signed complete-coefficient mass in \(Z_0\).  The discrepancy modes \(Z_r\) cannot be declared smaller without a uniform cross-row estimate for the coupled coefficients \(\mathfrak C^\circ_{a,b,k}(g)\).

In particular, the complete coefficient depends on the same \((a,b,k)\) that determines \(\theta\).  It is not a frequency-independent vector to which a standard scalar large sieve can be applied.  The radial phase has already returned, by (80.H1a), to the accepted original-variable rank-one form, and the near-square/Pell controls contain constant \(q\)-parity subfamilies.  A new theorem would have to estimate the residual actual-symbol correlation

\[
 \sum_{h<s}\chi_4(h)\chi_4(s)\sum_k
 \int_{s/4}^{h}A^\circ_{h,s}(x)
 e\!\left(kx-J(\sqrt s-\sqrt h)\sqrt x\right)dx
\]

with the strict-metric selector and exact ownership still attached, or exploit additional algebra of its profiles, floors, stars, collars, or cross-row integrals.  This report neither proves such a theorem nor proves a lower bound contradicting (80.14).

## 5. Control tests and outcomes

| Required control | Test | Outcome |
|---|---|---|
| `external_normalization` | Used \(e(t)=e^{2\pi it}\), \(\theta=X\delta^2/(2k)\), and the exact constant \(X\delta^2/(4k)=\theta/2\). | Pass; (80.H2)-(80.H3) have no missing factor of two. |
| `round78_round79_exclusions` | The explicit pair has \(ab=3\cdot15^2\ne\square\), \(\eta\ne0\), and \(Q\) or \(T\) can be chosen so \(AJD^3\gg L^3\). | Pass; none of the control terms is one of the three removed classes. |
| `primitive_parity` | \((25,27)=1\), both are odd, and \(q=1\). | Pass; the surviving \((-1)^q\) sign is constant on the Pell/near-square control. |
| `combined_odd_lift_phase` | Combined the outer factor and odd lift before any estimate. | Pass; it yields (80.H3). |
| `nearest_integer_sign` | Retained \((-1)^{q+\ell}\) and multiplied it by the exact carrier in \(\mathfrak B^\circ\). | Pass algebraically; fails as an independent cancellation mechanism. |
| `strict_metric_one_count` | Used one period-one window and \(0<|\eta|\asymp1/R<1/2\); (80.H14) is literal. | Pass; no exact centre is reinserted and no term is counted twice. |
| `density_and_discrepancy` | Expanded the window only after unfolding the complete carrier. | Proposed spectral-gap closure fails: (80.H7) contains the literal mean term \(\mu_RZ_0\). |
| `complete_actual_coefficient` | Defined \(\mathfrak C^\circ\) with the unchanged \(A^\circ_{ga,gb}\). | Pass; no absolute coefficient majorant or pointwise lower bound is used. |
| `lift_support_and_step_two_variation` | All identities are termwise on the actual finite odd support; the hostile analogue shows that variation alone is insufficient. | Pass as bookkeeping; no closure follows from (80.5). |
| `fiber_product_parity` | Proved (80.H8) and exhibited the odd fiber (80.H12)-(80.H14). | Parity cancellation fails; for odd \(p\) every quotient is odd, and in the actual term the quotient sign cancels anyway. |
| `safe_block_boundary` | On the explicit family \(AJD^3\asymp Q\), while \(L\) is chosen first. | Pass by taking \(Q\gg L^3\); the control is in the hard side. |
| `near_square_and_Pell` | Used \(25=5^2\), \(27=3\cdot3^2=25+2\), coming from \(5^2-3\cdot3^2=-2\). | Pass; it is primitive, nonsquare, strict interior, and has constant \(q=1\). |
| `perfect_power_metric_recurrence` | Used (80.H16)-(80.H17) for \(X=T^2\) and \(X=T^4\), then Weyl equidistribution. | Pass qualitatively for each fixed window and prescribed centre parity; no uniform shrinking-window estimate is claimed. |
| `endpoints_stars_and_collars` | Factored only a constant phase; the ratios in (80.H12) and (80.H16) are strict. | Pass; floors, stars, collars, endpoint samples, and saddle transitions remain owned exactly once. |
| `coefficient_adversary` | Tested phase-conjugated variation-class coefficients and then the genuine carrier (80.H2). | Coefficient-uniform/variation-only theorem is false; the actual carrier also defeats the proposed formal spectral gap. |
| `rank_one_self_return` | Expanded the centred square and changed back via \(h=ga,s=gb,x=gu\). | Pass as a no-go: (80.H11) and (80.H1a) return exactly to the original \(\chi_4(h)\chi_4(s)\)-weighted radical phase, giving no second independent saving. |
| `source_hypothesis_map` | Audited the four primary sources below against the literal kernel. | No imported theorem matches (80.H18). |
| `downstream_scope` | Compared the result only with the three Round-80 target obligations. | No downstream promotion is licensed. |

The primary-source hypothesis map is as follows.

| Primary source | Exact theorem/hypotheses audited | Literal map and verdict |
|---|---|---|
| H. Weyl, *Über die Gleichverteilung von Zahlen mod. Eins*, Satz 9 ([original article/DOI](https://doi.org/10.1007/BF01475864), [open scan](https://zenodo.org/records/2425535/files/article.pdf)) | A real polynomial whose nonconstant part has an irrational coefficient is uniformly distributed modulo one.  The interval is fixed while the averaging length tends to infinity. | Applies exactly to \(\theta(T)/2\) in (80.H17), including an arithmetic progression of \(T\), and proves the stated qualitative recurrence.  It supplies no rate uniform in a shrinking \(1/R\) window, no fixed-\(X\) energy estimate, and no coefficient-weighted cancellation. |
| H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, Theorem 1 ([author-hosted primary PDF](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)); see also their sharp analytic large sieve ([primary-paper DOI](https://doi.org/10.1112/S0025579300004708)) | The circle version assumes real points distinct modulo one and pays explicitly for \(\delta=\min^+\|x_r-x_s\|\); the derived large sieve acts on one common coefficient sequence against a separated frequency set. | No usable \(\delta\) is available at the active resolution (the accepted Round-79 algebraic separation is much finer), and \(\mathfrak C^\circ_\tau(g)\) is a row-dependent coefficient coupled to \(\theta_\tau\).  The carrier identity also restores a zero mode and, through (80.H1a), the original radical row phase.  The theorem gives no target-sized bound for \(Z_0\), (80.H18), or the residual two-character correlation. |
| D. R. Heath-Brown, *A mean value estimate for real character sums*, Theorem 1 ([journal primary PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf), pp. 237-238) | Theorem 1 sums \(\left|\sum_{n\le N}^{*}a_n(n/m)\right|^2\) over positive odd squarefree \(m\), with positive odd squarefree \(n\), a Jacobi-symbol kernel, and coefficients \(a_n\) independent of \(m\), obtaining \((MN)^\varepsilon(M+N)\sum|a_n|^2\).  Corollary 2 permits nonsquarefree inner support only with an explicit square-product correlation term. | \((-1)^{p/k}\) is parity of a quotient, not a Jacobi symbol; \(p,k\) need not be squarefree; and the quotient sign disappears by (80.H3).  After return, \(\chi_4(h)\chi_4(s)\) is merely a fixed mod-4 product multiplying a radical, mode-coupled actual symbol; it is not the varying quadratic kernel \((n/m)\), and its coefficient is not independent of the outer variable.  No hypothesis-preserving substitution exists. |
| W. Duke, J. Friedlander, and H. Iwaniec, *Bilinear forms with Kloosterman fractions*, Theorems 1-3 and (1.7)-(1.8) ([author-hosted primary PDF](https://www.math.ucla.edu/~wdduke/preprints/bilinear.pdf), pp. 23-25) | The basic form has \((m,n)=1\), a fixed positive integer \(a\), factorised coefficients \(\alpha_m\beta_n\), and phase \(e(a\bar m/n)\), where \(\bar m\) is the inverse of \(m\bmod n\).  The weighted extension requires a smooth \(F(m,n)\) with stated mixed derivative bounds through order two. | The product identity is \(p=\ell k\), not a modular inverse; the radical phase and \(A^\circ_{ga,gb}\) couple \((a,b,k,g,u)\); and floors, stars, moving support, and collars do not factor into the required \(\alpha_m\beta_nF(m,n)\).  Reciprocal inversion merely returns to the same product fibers.  The theorem is inapplicable. |

## 6. Dependencies and exact artifacts used

The proof uses only the selected local context:

- `protocol.md`, for evidence status, source-audit, and no-promotion rules;
- `state/proof_obligations.yml`, restricted to the current statuses and interfaces of `M9-M2-top-endpoint-signed-cone`, `M9-M2-top-endpoint-transposed-character-energy`, and `M9-M2`;
- `state/active_campaign.yml`, for the frozen target, controls, and report path;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/derivation_packet.md`, especially (80.1)-(80.18);
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/briefs/strict_metric_energy_hostile_source_audit.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reviews/conductor_round76_adjudication.md`, for the accepted odd-lift parity and rank-one self-return warning;
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reviews/conductor_round77_adjudication.md`, for the complete centred integral and step-two variation interface;
- `rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/reviews/conductor_round79_adjudication.md`, for exact-centre removal, the hard boundary, sharp ordinary density, and the failure of active-scale algebraic separation.

No sibling Round-80 report was read.  The only external dependencies are the four primary papers linked in Section 5.  Weyl is used positively and only for the recurrence control; the other three are rejected after literal hypothesis comparison.  The Pell and fiber calculations are elementary derivations in this report and do not depend on an external theorem.

## 7. Recommended state effect

**Recommended effect: retain the target as open; promote no estimate; record the no-go and revise the survivor.**

The graph should reject any candidate assertion that the nearest-integer sign \((-1)^{q+\ell}\), the odd-fiber quotient sign \((-1)^{p/k}\), or the half-integral frequencies in (80.H9) by themselves remove the ordinary \(1/R\) density.  The exact actual-symbol identity (80.H3) shows why: the centred coefficient supplies the conjugate carrier, quotient parity cancels, and the \(r=0\) density term returns.

The smallest honest survivor is (80.H18), equivalently the family of complete uncentred correlations \(Z_r\) in (80.H6), with \(Z_0\) and all relevant discrepancy modes controlled together.  In original variables it is exactly the residual actual-symbol \(\chi_4(h)\chi_4(s)\) correlation (80.H1a), not a new metric Fourier object.  A future proof must retain this sign, exploit structure beyond the Round-77 variation estimate, and handle the near-square/Pell constant-parity subfamilies and actual endpoint ownership.  No audited source treats this literal coupled radical phase with its moving mode, overlap interval, and full symbol; the metric Fourier/parity route is therefore certified as a self-return, not a closure.

Accordingly, `M9-M2-top-endpoint-signed-cone` and `M9-M2` remain open; `M9-M2-top-endpoint-transposed-character-energy` remains proved only as its existing reduction.  There is no new polynomial \(L\)-range, no promotion of endpoint uniformity or `M9`, and no change to the Gauss-circle exponent.
