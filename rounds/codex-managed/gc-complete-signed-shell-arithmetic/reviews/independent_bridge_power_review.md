# Round 206: independent bridge and sixth-moment power review

Campaign: gc-complete-signed-shell-arithmetic. Task: independent_bridge_power_review. Role: independent post-report seam reviewer, not statement-only. Date: 2026-09-26. Starting graph SHA-256: 4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71. This is a bounded review assignment after the reviewer's discovery report was frozen. No discovery report was changed.

## 1. Result

**GREEN for the mathematical claims in both reviewed artifacts.** The blind shell bridge, its origin and discrete-mean conventions, actual supremum, full tails, and conditional moment conversion are correct. Its positive surrogate refutes only an inference from the stated coarse properties; it is not an actual-\(r_2\) counterexample.

The conductor's direct block second moment, Fourier-multiplier block supremum, intersected sixth-moment estimate, all exponent maxima, and sufficient sixth-moment saving profile are also correct. In particular,
\[
 \int_I|H_N|^6\,dR\ll_\epsilon T^{1+\epsilon}N^{-29/110}
\]
is a valid complete middle-block estimate. Its resulting twelfth-moment exponent \(1+(272/55)\beta\) is worse than the accepted \(10\beta\), exactly as stated. The first unproved input remains the actual signed arithmetic improvement with the complete profile \(g(\alpha)\), or a different direct twelfth-moment argument.

The blind packet lacked the original-block \(N^{1/4}\) supremum. Its conditional exponent \(47/125+6\beta\) is valid but does not give the strongest consequence after that additional legal bound is supplied. The conductor correctly restores it: a variance-scale sixth moment would give the middle twelfth moment \(O(T^{1+\epsilon})\), and a uniform \(T^{4/25}\) loss in that sixth input still suffices for \(T^{29/25+\epsilon}\).

No mathematical correction or additional source theorem is required. The blind report's two noted formatting defects are separate from the mathematics; the final format-corrected hash is bound in Section6.

## 2. Exact reviewed statements and hypotheses

The reviewed artifacts are the campaign's reports/blind_odd_shell_bridge.md and controls/conductor_sixth_moment_power_ledger.md, at the exact hashes in Section6.

Use real \(T\ge2\), \(X=T^2\), \(I=[T/\sqrt2,\sqrt3T]\), and every dyadic \(N=T^\alpha\) with \(T^{52/125}<N<T^{99/125}\). The conductor uses the actual fixed radial-mollifier transform \(\Psi\), the exact Round205 smooth partition \(v\), and its actual original block \(H_N\) and shell \(S_N\). The dimensionless blind sine kernel and additive quantity are
\[
 L(u)=\int_1^2t^{-1}\Psi(\sqrt{N/T}\,t)v(t^2)\sin(2\pi tu)\,dt,
 \quad
 Z_N(x)=\sum_{m\ge1}(r_2(m)-\pi)L((x-m)/h_N(x)),
 \quad h_N(x)=2\sqrt x/\sqrt N.
\]

The blind bridge only needs its coefficient bound, inclusive discrepancy bound, fixed real even Schwartz \(\Psi\) and smooth supported \(v\). Nonvanishing is only needed for its separate surrogate control. The conductor's complete supremum uses the actual mollifier so that the accepted Round204 reconstruction applies. Put
\[
 \theta=\theta_{LY},\quad \beta=2\theta-\tfrac12,\quad
 q=136/13,\quad \omega(\alpha)=\min\{\alpha/4,\beta,(1-\alpha)/2\}.
\]
Constants may depend on the fixed filters and windows. No growing moment, varying test function, missing middle scale, or fixed-width-to-variable-width transfer is assumed.

## 3. Independent derivation of the seams

### Curvature, mean, origin and full tails

On \(x/4\le m\le4x\), let \(z=(x-m)/h\), \(u=\sqrt N(R-\sqrt m)\). Direct algebra gives
\[
 u=\frac{2R}{R+\sqrt m}z,\qquad
 \frac23\le\frac{u}{z}\le\frac43,\qquad
 u-z=\frac{\sqrt N(R-\sqrt m)^2}{2R}.
\]
The ratio is used only for \(z\ne0\); both kernels vanish for \(z=0\). Thus \(u-z\ll z^2/(R\sqrt N)\), while the amplitude difference is \(O(R^{-1/2}|z|/(R\sqrt N))\). Every intermediate kernel argument is comparable to \(z\), so Schwartz bounds absorb the polynomial factors. The lattice sum is \(O(h)\); summing with actual coefficients gives the claimed \(T^{-1/2+\epsilon}N^{-1}\). The first correction in blind (5.1) is correct: both \(zL(z)\) and \(z^2L'(z)\) are even, so symmetric offsets need not cancel the error.

Below \(x/4\), the radial argument is \(\gg T\sqrt N\), and the coefficient mass with fourth-root weight is \(O(T^{3/2+\epsilon})\). Above \(4x\), summing \(m^{-1/4+\epsilon}(Nm)^{-B/2}\) gives the same tail order. The additive tails have prefactor \(T^{2+\epsilon}\). Increasing a fixed decay order makes both \(O_A(T^{-A})\) uniformly. This includes all positive small and arbitrarily large \(m\), without defining \(m^{-1/4}\) at zero.

Fourier support of \(L\) lies in \([-2,-1]\cup[1,2]\). Since \(h>\sqrt2\,T^{151/250}>2\), Poisson summation gives \(\sum_{m\in\mathbb Z}L((x-m)/h)=0\) for each real \(x\). The nonpositive terms have size \(O_B(h(1+x/h)^{1-B})\). Thus subtracting \(\pi\) is justified uniformly, including integer centers. Oddness alone is not being used to cancel an arbitrary discretized mesh.

For \(f(y)=L((x-y)/h)\), the inclusive discrepancy has
\[
 dP=\sum_{m\ge1}r_2(m)\delta_m-\pi\,dy\quad\hbox{on }(0,\infty),
 \qquad P(0)=1.
\]
Integration by parts gives exactly
\[
 Z_N(x)=-L(x/h)+h^{-1}\int_0^\infty P(y)L'((x-y)/h)\,dy
 +\pi\left(\int_0^\infty f(y)\,dy-\sum_{m\ge1}f(m)\right).
\]
The origin term has the correct sign, and the two mean terms are separately negligible. The parameter \(h=h(x)\) is fixed during integration in \(y\); no derivative \(h'(x)\) appears. Applying the inclusive pointwise bound inside the integral, with the large-\(y\) part paid by rapid decay, gives \(Z_N\ll X^{\theta+\epsilon}\). The coefficient estimate separately gives \(Z_N\ll hT^\epsilon\). This verifies blind (1.1)--(1.2).

### Jacobian, conditional moment and surrogate scope

The exact variable change is
\[
 \int_I|R^{-1/2}Z_N(R^2)|^6\,dR
 =\tfrac12\int_{X/2}^{3X}x^{-2}|Z_N(x)|^6\,dx.
\]
It loses exactly \(T^4\), with the actual variable width unchanged. The bridge error has sixth moment \(O(T^{-2+\epsilon}N^{-6})\), and its summed twelfth moment is \(O(T^{-5-12(52/125)+\epsilon})=O(T^{-1249/125+\epsilon})\).

Under the prospective variance sixth input, the supplied \(T^\beta\) supremum gives block exponent \(1+6\beta-3\alpha/2\). Twelfth roots and the geometric dyadic sum of \(N^{-1/8}\) give \(47/125+6\beta\). The margin \(98/125-6\beta>0\), and its rational verification using \(\sqrt{1717}<83/2\), are correct. Blind (3.23)--(3.24) correctly price additional losses for that specified certificate. Bounded \(R\)-dependent coefficients in the final sum need only their supremum for Minkowski.

The report correctly requires the exact variable-width family. A theorem for each fixed \(h\), without a proved uniform transfer or maximal estimate, is not enough.

For the positive surrogate, \(\lambda=cA_0/h_0\) and \(A_0=\min(h_0,X^\theta)\). The cosine geometric sum is \(O(h_0)\), so every endpoint of the perturbed block has discrepancy \(O(A_0)\). Before it the baseline discrepancy is \(1-\pi\{y\}\), and after it the accumulated perturbation remains \(O(A_0)\). Thus the global \(O(y^\theta)\) bound has uniform constants; small fixed \(c\) ensures positivity.

Inside the stated fixed interior interval, truncation tails are rapidly small. Poisson has no nonzero alias because \(h(x)\to\infty\). The frequency \(\tau h(x)/h_0\) remains on a fixed interval where the purely imaginary Fourier transform has fixed sign and magnitude bounded below. The main term in blind (5.5) is therefore a sine of amplitude comparable to \(A_0\), with \(\asymp X/h_0\to\infty\) periods. Its sixth integral is \(\gg XA_0^6\).

The intended cube in blind (5.7) is
\[
 (A_0^2/h_0)^3=\min\{h_0,X^{2\theta}/h_0\}^{3}.
\]
For \(N=T^\nu\) its exponent is
\[
 \min\{3-3\nu/2,\ 12\theta-3+3\nu/2\},
\]
uniformly at least \(\min\{453/250,12\theta-297/125\}>0\). Positivity follows already from \(\theta>5/16\). The rendering defect did not conceal a wrong exponent.

These are \(T,N\)-dependent surrogate sequences with uniform coarse bounds. They need not satisfy the divisor identity, original-block multiplier interface, or actual second-moment estimate. The report uses them only against an inference from positivity, bounded coefficients and global discrepancy alone. That scope is valid; they do not refute the actual arithmetic target.

### Conductor second moment and multiplier supremum

The complex square has diagonal \(T\sum|a_n|^2\). Each off-diagonal integral is \(O(\sqrt N/|n-m|)\) on the fixed annulus. Applying \(2|a_na_m|\le|a_n|^2+|a_m|^2\) and the harmonic sum gives
\[
 \int_I|F|^2\ll(T+\sqrt N\log(2N))\sum|a_n|^2
 \ll_\epsilon TN^{-1/2}T^\epsilon.
\]
The actual \(N<T^{99/125}\) gives power slack for \(\sqrt N\log N\ll T\). Taking the real part or splitting into two fixed ambient annuli loses no power. No diagonal or coefficient is dropped.

The even multiplier \(m_N(\xi)=v(\xi^2/N)\) evaluates to \(v(n/N)\) at both \(\pm\sqrt n\). Its kernel is \(\sqrt Nq_0(\sqrt N u)\) for a fixed Schwartz function, with bounded \(L^1\) norm. Absolute convergence licenses termwise convolution of the complete original series. On a fixed larger positive radius interval its accepted supremum is \(T^{\beta+\epsilon}\); outside, \(|u|\gg T\), and the global coefficient sum \(T^{1/4+\epsilon}\) is multiplied by an arbitrarily small convolution tail. This proves the block \(T^\beta\) bound. Combining the original coefficient and shell suprema yields (C3). It is not a bound on an arbitrary summand inferred from its whole sum.

### Sixth layer cake, domination and twelfth maximization

Chebyshev gives \(D(V)\ll TN^{-1/2}V^{-2}\) for all \(V>0\), while the accepted distribution gives \(D(V)\ll V^{-2}+TV^{-q}\) for \(V\ge1\). At \(V_0=N^{13/220}\), \(V_0^{q-2}=N^{1/2}\). Below \(V_0\), sixth layer cake gives \(TN^{-1/2}V_0^4\). This is integrable at zero and needs no artificial \(O(T)\) baseline. Above it, both accepted terms give \(W^4+TV_0^{6-q}\). The exact powers are
\[
 -\tfrac12+4(13/220)=-29/110,\qquad
 (13/220)(6-136/13)=-29/110.
\]
If \(W<V_0\), the low integral alone is smaller. Otherwise \(W^4\) is dominated: \(4\omega\le4\beta<2/3\), whereas \(1-(29/110)\alpha>1-(29/110)(99/125)>3/4\). Small epsilon losses preserve this fixed gap. This proves (C1); the Gram-diagonal term is retained and then lawfully dominated.

The twelfth exponents obtained by multiplying by \(W^6\) are
\[
 \begin{cases}
 1+(68/55)\alpha,&\alpha\le4\beta,\\
 1+6\beta-(29/110)\alpha,&4\beta\le\alpha\le1-2\beta,\\
 4-(359/110)\alpha,&\alpha\ge1-2\beta.
 \end{cases}
\]
They are continuous, increase on the first piece, and decrease thereafter. The accepted bounds on \(\beta\) put both breakpoints inside the middle interval in the stated order. The maximum is \(1+(272/55)\beta\) at \(4\beta\). Its excess over \(10\beta\) is \(1-(278/55)\beta>0\). Minkowski over every middle block costs only logarithms. Thus (C5) is correctly not claimed as a new complete twelfth bound.

### Exact sixth certificate and saving profile

An arithmetic sixth input \(K_6(N)\) certifies a twelfth bound \(T^{-4+6\omega+\epsilon}K_6(N)\), with the already negligible errors. Its exact sufficient threshold is therefore
\[
 K_6(N)\ll_\epsilon T^{129/25-6\omega(\alpha)+\epsilon}.
\]
Relative to \(XH^3=T^5N^{-3/2}\), the allowed loss is \(4/25+3\alpha/2-6\omega\ge4/25\), because \(\omega\le\alpha/4\). Thus variance scale itself gives \(T^{1+\epsilon}\); a uniform \(T^{4/25}\) loss still suffices. Calling (C7) weakest is correct only with the printed qualification: it is weakest for these supremum bounds and this interpolation certificate, not necessary for the actual moment.

The proved sixth estimate loses \(N^{68/55}\) over variance scale. Subtracting the allowed loss gives
\[
 g(\alpha)=6\omega(\alpha)-4/25-(29/110)\alpha.
\]
On the first interval this is \(68\alpha/55-4/25\), with value \(2436/6875\) at \(52/125\). On the middle interval it decreases. On the last it is \(71/25-(359/110)\alpha\), with value \(3509/13750\) at \(99/125\). Continuity and these positive endpoint minima prove positivity throughout. Its maximum is \((272/55)\beta-4/25\) at \(4\beta\). Every middle scale and breakpoint is retained.

## 4. First doubtful or unproved step

No mathematical gap was found under the stated accepted dependencies. Neither artifact proves (C7). The first unproved step is the complete actual signed sixth improvement with profile \(g(\alpha)\), including all shifts and exact varying widths, or a direct twelfth argument bypassing this certificate.

The blind report's missing variance sixth input is interpreted within its isolated packet. Once the conductor supplies the original-block bound, weaker (C7) is the appropriate sufficient frontier. Neither sufficient input is converted into a necessary condition here.

## 5. Controls and outcomes

| Seam or control | Outcome |
|---|---|
| Curvature and amplitude | GREEN: exact ratio, summable first correction, no error-free odd-pair assertion. |
| Mean, origin, integer centers | GREEN: Fourier support, explicit origin term, inclusive convention and zero central value. |
| All tails | GREEN: arithmetic low/high tails, nonpositive mean tail, convolution tail and complete dyadic errors. |
| Variable width and endpoints | GREEN: actual width, fixed-parameter Stieltjes integration and exact Jacobian; no endpoint deletion. |
| Surrogate scope | GREEN: uniform coarse bounds and coherent filter response; no actual divisor identity or arithmetic counterexample. |
| Second moment and multiplier | GREEN: all coefficients, all spacing terms, exact even multiplier and positive-window enlargement. |
| Sixth layer cake | GREEN: integrability at zero, threshold, both high terms and diagonal domination. |
| Complete powers | GREEN: interior maximum, accepted comparison, exact certificate and positive endpoint savings. |
| Stronger versus sufficient input | GREEN: variance scale is stronger than needed; its failure does not refute the twelfth target. |
| Source and proof scope | GREEN: accepted theorem only, with inherited qualifications; no Gaussian inference or parent closure. |

All controls are analytical. Hashing and format inspection are mechanical provenance checks, not mathematical experiments.

## 6. Exact artifacts and hashes

| Artifact | SHA-256 |
|---|---|
| rounds/codex-managed/gc-complete-signed-shell-arithmetic/reports/blind_odd_shell_bridge.md | f7c7e3362acc69e71ca8c38b2ec37a1d5b5a08f87682f9c056f2bc4c6770d511 |
| rounds/codex-managed/gc-complete-signed-shell-arithmetic/controls/conductor_sixth_moment_power_ledger.md | 0a60519b209389501b62a82225e5ca9506cf01c0e739acab8d7836b05d275f5a |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md | f297dadc44d0113097d6549650228992b6e969740b75e25451eab3a514cebffb |
| rounds/codex-managed/gc-full-frontier-moment-strategy-review/reviews/independent_middle_band_review.md | 48eef2b091ddbdb0e853aa8a7ea4f6a8fef68227e34fb3e35f2058a9c6263037 |

The final blind hash was verified after the format-only correction, and its corrected cubic expression was reread; the conductor ledger hash was reverified unchanged. The accepted kernel and Round205 material were read during this task's prior discovery assignment and rechecked at the relevant seams here. This review is expressly post-report and claims no statement-only isolation. The blind author's original isolation remains its own provenance; this reviewer did not read its statement packet. No new web theorem or unlisted report is used.

## 7. Recommended state effect

**GREEN as reviewed analytical evidence; retain the current mathematical state.** No correction to (C1)--(C9) is required. The blind bridge and conditional consequence are valid with the stated scope and final format correction.

The conductor may retain these artifacts for closure and arithmetic comparison, but neither closes the signed sixth input, frozen twelfth target, any M1/M2 parent, or exponent one quarter. No graph promotion follows merely from compatible interface calculations.

Only this assigned review was written. The discovery report, shared state, proof draft, validation matrix, synthesis and all other artifacts were unchanged. This review stops here.
