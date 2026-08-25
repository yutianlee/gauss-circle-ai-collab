# 1. Result and verdict

**GREEN.** The two-collar connector is mathematically valid. The repaired (140.C19e) now reads

\[
\sqrt h\,{w^2\over h\Delta_h}\ll {1\over h},
\]

with the verified multiplicative thin space. For fixed \(0<\rho _1<\rho _2<1/8\), the literal sharp tail at \(\rho _1\) satisfies

\[
\mathcal S_{N,\rho _1}^{\pm}
=\mathcal P_{\rho _2}^{\pm}
+O_{\rho _1,\rho _2,V}\!\left(R\log ^C(2X)\right),
\]

where

\[
\mathcal P_{\rho _2}^{+}
=e(-1/8)N^{1/4}
\sum_h\sum_{\substack{r\ge r_{2,h}+2\\r\ {\rm odd}}}
\chi _4(r)(hr)^{-3/4}
V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),
\qquad
\mathcal P_{\rho _2}^{-}=\overline{\mathcal P_{\rho _2}^{+}},
\]

and \(r_{2,h}\) is the least positive odd integer at least \(4Nh/D_{2,h}^2\). The error is a signed scalar error, not a square or positive-energy deletion. The sharp-to-smooth band, smoothing-ramp aliases, closest clean alias, all smooth nonstationary aliases, profile crossings, and stationary remainders can all be returned to \(R\log ^C(2X)\).

The proposed rowwise smooth \(B\)-process error is dimensionally supported, but only after the derivative variation is counted on the aliases where it is actually supported. In particular, the smoothing derivative is supported on \(O(\sqrt h)\) ramp aliases, not on all \(O(h)\) upper physical-block aliases. With that localization, the rowwise local and nonstationary error is \(O(h^{-1}\log ^2(2X))\). The conductor candidate already removes the ramp separately, so it does not rely on the potentially misleading unlocalized count. The exact insertions recommended in Section 5 make this seam mechanically auditable; they do not change the result or its hypotheses.

# 2. Exact connector and owner partition

Let

\[
L_{i,h}=\left\lfloor{\rho_i y\over\sqrt h}\right\rfloor,\qquad
D_{i,h}=y-L_{i,h}-1,\qquad
\Delta_h=D_{1,h}-D_{2,h}+1.
\]

On active rows, \(h\ll R\), \(D_{i,h}\asymp y\), and

\[
\Delta_h=L_{2,h}-L_{1,h}+1\asymp_{\rho_1,\rho_2}{y\over\sqrt h}.
\]

Choose a fixed flat step \(\eta\), zero on \((-\infty,0]\) and one on \([1,\infty)\), and put

\[
W_h(x)=\eta\!\left({D_{1,h}+1-x\over\Delta_h}\right),\qquad
\widetilde A_h(x)={1\over h}
V_{\rm low}\!\left({4R^2h^2\over x^2}\right)W_h(x).
\]

Then \(W_h=1\) for \(x\le D_{2,h}\), \(W_h=0\) for \(x\ge D_{1,h}+1\), and all endpoint derivatives vanish. At integer samples the sharp-minus-smooth difference is supported exactly on

\[
D_{2,h}<d\le D_{1,h}
\quad\Longleftrightarrow\quad
L_{1,h}<v=y-d\le L_{2,h}.
\]

Thus no sample beyond the sharp tail is introduced. The exact sharp formula retains its half-endpoint and branchwise symmetric boundary series; the physical band above is estimated before Poisson summation. Whole-line Poisson is then legitimate for \(\widetilde A_h\), with no boundary harmonic.

For

\[
p_h(x)={4Nh\over x^2},
\]

the aliases whose saddle lies in the smoothing ramp form

\[
\mathfrak R_h=
\left\{r\ {\rm odd}:
{4Nh\over(D_{1,h}+1)^2}\le r\le {4Nh\over D_{2,h}^2}\right\}.
\]

The owner partition is: the sharp-to-smooth physical band; \(\mathfrak R_h\); the single alias \(r_{2,h}\) if it is not already in \(\mathfrak R_h\); far stationary aliases \(r\ge r_{2,h}+2\); positive aliases below the derivative image; negative aliases; aliases beyond the profile image; profile-edge transitions; and stationary remainders. This partition is exhaustive and does not rearrange the conditionally convergent sharp formula.

# 3. Two-collar equivalence and derivative ledger

On the band \(L_{1,h}<v\le L_{2,h}\), the exact parity-reduced phase has constant-sign second derivative of size \(h/y\), because \(v\le\rho _2y/\sqrt h<y/8\). The multiplier \(1-W_h(y-v)\), multiplied by the fixed profile, has uniformly bounded sampled supremum plus variation. The Round-139 second-derivative estimate therefore applies to this subinterval and gives, before the \(h^{-1}\) height weight,

\[
\left|\hbox{one band row}\right|
\ll \sqrt y+\sqrt{y/h}.
\]

Since \(h\ll R\) and \(\sqrt y\asymp R\),

\[
\sum_{h\ll R}{1\over h}
\left(\sqrt y+\sqrt{y/h}\right)
\ll R\log(2X).
\]

This proves the sharp-to-smooth scalar equivalence uniformly in all floors, \(0\le q\le2y\), both parities, and both signs.

The derivative ledger is also correct. On the profile-variation scale write \(x=Rh\,u\); then

\[
{1\over h}V_{\rm low}(4/u^2)
\]

has second-derivative \(L^1\)-mass \(O((Rh^2)^{-1})\). On the upper ramp,

\[
\|W_h'\|_1\ll1,\qquad
\|W_h''\|_1\ll\Delta_h^{-1}.
\]

The mixed term is bounded by either the profile variation times \(\|W_h'\|_\infty\) or the ramp variation times the profile derivative supremum. Consequently

\[
\|\widetilde A_h\|_\infty+
\|\widetilde A_h'\|_1\ll h^{-1},
\qquad
\|\widetilde A_h''\|_1
\ll {1\over Rh^2}+{1\over h\Delta_h}
={1\over h}\left({1\over Rh}+{1\over\Delta_h}\right).
\]

No omitted support-length factor occurs: integrating \(W_h''\) over its interval of length \(\Delta_h\) produces \(\Delta_h^{-1}\), while integrating the rescaled profile second derivative over length \(Rh\) produces \((Rh^2)^{-1}\).

# 4. Independent smooth \(B\)-process and complete error ledger

The ramp alias count follows directly from the derivative-image length:

\[
\begin{aligned}
|\mathfrak R_h|
&\ll 1+4Nh\left({1\over D_{2,h}^2}
-{1\over(D_{1,h}+1)^2}\right)\\
&\ll 1+{Nh\,\Delta_h\over y^3}
\ll1+\sqrt h.
\end{aligned}
\]

On the ramp, \(\phi''(x)=2Nh/x^3\gg h/y\). The weighted second-derivative integral estimate and the preceding variation bound give, for each ramp alias,

\[
|\widetilde I_{h,r}|
\ll h^{-1}\sqrt{y/h}
\ll Rh^{-3/2}.
\]

Adding \(r_{2,h}\) if necessary does not change the count, and hence

\[
\sum_{h\ll R}\sum_{r\in\mathfrak R_h\cup\{r_{2,h}\}}
|\widetilde I_{h,r}|
\ll
\sum_{h\ll R}Rh^{-3/2}(1+\sqrt h)
\ll R\log(2X).
\]

For \(r\ge r_{2,h}+2\),

\[
\phi'(D_{2,h})={r-4Nh/D_{2,h}^2\over4}\ge {1\over2},
\qquad
\sqrt{\phi''(D_{2,h})}\asymp\sqrt{h/y}.
\]

Thus the saddle is at least \(c\sqrt{y/h}\) Gaussian widths inside the plateau \(W_h=1\), uniformly on active rows. Put \(m=hr\), \(\lambda=\sqrt{Nm}\), and \(x=2\sqrt{N/m}\,h\,u\). The far integral becomes

\[
2\sqrt{N/m}\int
V_{\rm low}\!\left({R^2m\over Nu^2}\right)W_h(x_*u)
e\!\left({\lambda\over2}(u+u^{-1})\right)du.
\]

Local stationary phase at \(u=1\) gives

\[
\widetilde I_{h,r}
=2e(1/8)N^{1/4}(hr)^{-3/4}
V_{\rm low}(R^2hr/N)e(\sqrt{Nhr})
+\mathcal E_{h,r}.
\]

The full-line Gaussian constant is correct, and multiplication by the character-Poisson factor \((2i)^{-1}\chi_4(r)\) gives \(e(1/8)/i=e(-1/8)\). The local Taylor error is

\[
\mathcal E^{\rm loc}_{h,r}
\ll N^{-1/4}(hr)^{-5/4},
\]

whose complete sum is

\[
\sum_{h,r}|\mathcal E^{\rm loc}_{h,r}|
\ll N^{-1/4}\sum_m\tau(m)m^{-5/4}
\ll_\varepsilon R^{-1}X^\varepsilon.
\]

The plateau-to-ramp tail is bounded by

\[
{1\over h\{1+r-4Nh/D_{2,h}^2\}}\ll {1\over r},
\]

and the remaining fixed-profile off-saddle part is \(O((hr)^{-1})\). Therefore the deliberately coarse far-owner sum is

\[
\sum_{\substack{h\ll R\\h\ll r\ll y/h}}
\left({1\over r}+{1\over hr}\right)
\ll R\log(2X).
\]

The proposed rowwise \(O(h^{-1}\log^2 X)\) smooth \(B\)-process error also passes a separate dimensional check. On a physical block \(x\asymp Z\), where \(Rh\ll Z\ll y\), put

\[
P={Nh\over Z^2},\qquad
w=\left({Z^3\over Nh}\right)^{1/2}.
\]

There are \(O(1+P)\) stationary aliases and \(w\) is one Gaussian width. The cubic parameter is

\[
\epsilon_3={Nh\over Z^4}w^3=\sqrt{Z\over Nh}
\le {1\over R\sqrt h};
\]

at the actual lower support \(Z\asymp Rh\) it is \(O(R^{-3/2})\). After the already-present \(h^{-1}\) weight, the counted cubic error and the counted fixed-profile variation error are respectively

On the true support \(Z\ll y\) and \(N\ge y^2\), so \(P=Nh/Z^2\gg h\ge1\). Consequently \(1+P\ll P\); using \(P\), rather than \(1+P\), in the next two counted errors loses no endpoint alias.

\[
{1\over h}P\,w\,\epsilon_3={1\over h},
\qquad
P\,{w^2\over hZ}={1\over h}.
\]

At the upper smoothing ramp one must not multiply its derivative error by all \(P\asymp h\) aliases. Its derivative is supported on only \(O(\sqrt h)\) aliases, and with \(Z\asymp y\), \(w^2\asymp y/h\), and \(\Delta_h\asymp y/\sqrt h\),

\[
\sqrt h\,{w^2\over h\Delta_h}\asymp {1\over h}.
\]

All second-amplitude-derivative terms are smaller. Hence the local error is \(O(h^{-1})\) per relevant block. For aliases outside a derivative-image block, monotonicity of \(\phi'\) gives \(O((hj)^{-1})\) at odd-alias distance \(j\); summing \(j\) gives one logarithm and summing the \(O(\log X)\) physical blocks gives the second.

The infinite negative and remote positive tails require two, not one, integrations by parts. With \(p=p_h(x)\), summing the twice-integrated negative-mode bound first in \(r\) gives terms dominated by

\[
\int\left\{
{|\widetilde A_h''|\over1+p}
+{|\widetilde A_h'|\,p/x\over(1+p)^2}
+{|\widetilde A_h|\,p/x^2\over(1+p)^2}
+{|\widetilde A_h|\,p^2/x^2\over(1+p)^3}
\right\}dx.
\]

On the true support \(x\ge cRh\), \(x\le y\), and \(p\gg h\); the derivative ledger makes this \(O(h^{-1})\), with room to spare. The positive tail beyond the profile image is identical after replacing \(p+|r|\) by the distance to the image. The closest image aliases do not spoil the rowwise bound. At the lower profile edge \(x_0\asymp Rh\), one Gaussian width is \(w_0\asymp h/\sqrt R\), so \(w_0/x_0\asymp R^{-3/2}\). Flatness gives, for any fixed \(M\),

\[
|\widetilde I_{h,r}^{\rm lower\ edge}|
\ll h^{-1}w_0(w_0/x_0)^M\ll h^{-1}
\]

already with \(M=1\). At the upper zero endpoint, one width is \(w_1\asymp R/\sqrt h\) and \(w_1/\Delta_h\asymp R^{-1}\); the same flatness estimate is \(O(h^{-1}w_1(w_1/\Delta_h)^M)\ll h^{-1}\) with \(M=1\). Thus flat zero extension at the profile edge and at \(D_{1,h}+1\) removes every boundary term and prices the at-most-one closest endpoint alias without a second-derivative loss. Consequently

\[
\sum_{r\ {\rm smooth\ nonstationary}}
|\widetilde I_{h,r}|
\ll { \log ^2(2X)\over h},
\qquad
\sum_{h\ll R}{ \log ^2(2X)\over h}
\ll \log ^3(2X).
\]

This proves the complete smooth nonstationary/remainder ledger and, a fortiori, the conductor's coarser \(O(R\log ^C(2X))\) allowance.

# 5. First unproved step and exact repairs

After the connector, the first unproved statement is exactly

\[
|\mathcal P_{\rho_2}^{\pm}|
\ll_\varepsilon RX^\varepsilon.
\]

Nothing in the smoothing or \(B\)-process proves this signed far-family estimate. Its rank-one Hessian, incomplete product fibres, \(R^{3/2+o(1)}\) coefficient-blind capacity, near radicals, and self-return remain genuine open owners.

The patched candidate now contains the substantive insertions requested by the first review:

- It defines the far summand to be zero on empty or inactive rows.
- It removes \(r_{2,h}\) separately when that alias lies just above the real ramp interval.
- It separates the local Taylor sum (140.C23) from the plateau/ramp and fixed-profile off-saddle bounds.
- Equations (140.C19c)--(140.C19f) give the block count, ramp localization, twice-integrated tails, and harmonic height sum.
- It keeps the closest derivative-image alias in the transition ownership rather than forcing one-derivative summability.

The current text is now fully GREEN. Equation (140.C19c) has \(P\gg h\ge1\) on the true support, so replacing \(1+P\) by \(P\) in (140.C19d) is valid, and the repaired (140.C19e) has the correct multiplication. There is no doubtful connector step left. A future proof that omits the \(O(\sqrt h)\) localization of the cutoff derivative should be marked REVISE, and one that multiplies this derivative by all \(P\asymp h\) upper-block aliases should be rejected.

# 6. Controls, dependencies, and directionality

| Seam | Independent outcome |
|---|---|
| Two-collar sharp-to-smooth equivalence | GREEN. The exact difference is \(L_{1,h}<v\le L_{2,h}\), has bounded sampled variation, and costs \(O(R\log X)\) by the accepted curvature collar. |
| Derivative ledger | GREEN. Rescaling at the lower profile support and integrating over the ramp give exactly \(1/(Rh^2)+1/(h\Delta_h)\). |
| Ramp count and price | GREEN. The derivative-image length is \(O(1+\sqrt h)\); including \(r_{2,h}\) gives \(O(R\log X)\). |
| Far threshold | GREEN. The first retained odd alias \(r_{2,h}+2\) is \(c\sqrt{y/h}\) Gaussian widths into \(W_h=1\). |
| Gaussian coefficient | GREEN. The leading integral is \(2e(1/8)N^{1/4}(hr)^{-3/4}\), and the branch factor produces \(e(-1/8)\chi_4(r)\). |
| Local error count | GREEN after the explicit support-localized count in Section 4; no dimension is missing at \(x\asymp Rh\) or \(x\asymp y\). |
| Smooth nonstationary owners | GREEN. Finite distance classes give the harmonic logarithm; flat endpoints and two integrations close both infinite tails. |
| Scalar directionality | GREEN. The result is only \(\mathcal S_{\rho_1}^{\pm}=\mathcal P_{\rho_2}^{\pm}+O(R\log^C X)\), hence scalar target equivalence. It yields no tail-square identity, collar--tail cross-term estimate, or Round-138 residual deletion. |

The exact artifacts used were:

- protocol.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/blind_statement.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/briefs/blind_height_alias_joint_feasibility.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/candidates/conductor_round140_smoothed_far_alias_reduction.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/candidates/conductor_round139_curvature_collar_and_quadratic_obstruction.md;
- rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/synthesis.md;
- the three primary Round-140 reports in rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reports/.

No shared proof-state file, proof draft, numerical experiment, web source, or downstream proof artifact was used.

# 7. Recommended state effect

Promote the strict scalar reduction: the literal \(\rho_1\) tail is target-equivalent to the clean far stationary family beginning at \(r_{2,h}+2\), with a fixed \(O(R\log^C X)\) owner-complete error. Promote with it the two-collar smoothing lemma, the derivative ledger, the \(O(\sqrt h)\) ramp count, the \(O(R\log X)\) ramp cost, the exact Gaussian coefficient, and the complete smooth nonstationary/remainder ledger.

Retain as obstructions the sharp endpoint harmonic series, rank-one Hessian, incomplete product fibres, coefficient-blind \(R^{3/2+o(1)}\) capacity, near-radical gap, and transform self-return. Keep the far signed estimate, lower radial estimate, lower GAR, M9-M1, every M2 obligation, endpoint uniformity, M9, the bridge, the quarter theorem, and every exponent improvement open. No shared state or candidate file was edited by this review.
