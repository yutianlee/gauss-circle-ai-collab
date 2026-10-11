# Round 204: actual large values with the complete Gram diagonal

Campaign: `gc-complete-large-values-duality`. Task: `actual_large_values_attack`. Role: discovery, selected context. Date: 2026-09-23. Starting graph SHA-256: `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`. Candidate evidence only. No sibling report was read. Effort: 100 percent analytical/algebraic; no numerical experiment. Only this report is written.

## 1. Result: a complete weaker distribution, with the frozen target open

Put
\[
 \kappa=\frac{13}{55},\qquad q=2+\frac2\kappa=\frac{136}{13},
 \qquad \beta=2\theta-\frac12,\qquad
 \theta=\frac{3292+25\sqrt{1717}}{13762}.
\]
The proposed weaker envelope has a complete proof:
\[
 \boxed{D_T(V)\ll_\varepsilon T^\varepsilon
       \{V^{-2}+T V^{-q}\}\quad(V\ge1).}                 \tag{1}
\]
This holds for the actual infinite tail in the brief, for the full series with no lower cutoff, and uniformly for every hard lower cutoff. The proof keeps every Gram diagonal, every localization interval, the ceiling in their number, the actual arithmetic coefficients, and the entire infinite upper tail. It uses the graph-accepted global Bourgain exponent-pair interface after the square-root derivative check below; it does not insert the arithmetic weights into an unweighted source theorem.

The diagonal term in (1) is decisive. At the inherited pointwise cutoff, the resulting full twelfth moment is
\[
 \boxed{\int w(R/T)|H_T(R)|^{12}\,dR
       \ll_\varepsilon T^{10\beta+\varepsilon}.}          \tag{2}
\]
The same holds for the brief's tail. Reproducing the complete inclusive sharp-to-smooth interface gives the candidate consequence
\[
 \boxed{\int_{Y/2}^{3Y}|P(x)|^{12}\,dx
       \ll_\varepsilon Y^{1+10\theta+\varepsilon}.}        \tag{3}
\]
This is a small improvement over the inherited moment comparison, not a pointwise improvement. Its persistence exponent is \((1+10\theta)/13>\theta\). In particular, it does not prove the frozen high-value bound or the quarter theorem.

For levels \(V=T^v\), (1) proves the frozen bound through \(v\le13/125\), with the usual epsilon convention. It does not reach its full range up to \(v=\beta\). A coefficient-sensitive weighted-Gram attempt is also carried out below. Its exact Stieltjes derivative term makes it weaker and leaves the high-value gap open. An aligned generic control explains why a coefficient-blind removal of the diagonal would be false; that control is not a counterexample for \(r_2\).

## 2. Exact statement and hypotheses

Use the actual mollifier from the permitted reconstruction interface: a fixed nonnegative radial \(\rho\in C_c^\infty(\mathbb R^2)\), supported in the unit disk and of integral one. Let \(\Psi(s)=\widehat\rho(se_1)\), with Fourier convention \(e(t)=\exp(2\pi it)\). Thus \(\Psi\) is real, even, Schwartz, and \(|\Psi|\le1\); it need not be nonnegative. Let \(w\in C_c^\infty((0,\infty))\) be fixed and nonnegative, with support in \([c,C]\), \(0<c<C\). For reconstruction choose it equal to one on \([1/\sqrt2,\sqrt3]\). The frozen choice \(w=\chi^2\) is included. For real \(T\ge2\), put
\[
 a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),\qquad
 H_T(R)=\sum_{n\ge1}a_n(T)\cos(2\pi R\sqrt n-3\pi/4),
\]
\[
 B_{T,U}(R)=\sum_{n>U}a_n(T)\cos(2\pi R\sqrt n-3\pi/4),\qquad
 D_{T,U}(V)=\int w(R/T){\bf1}_{|B_{T,U}(R)|>V}\,dR.       \tag{4}
\]
Here \(U\ge0\) is an integer; \(U=0\) gives \(H_T\), and the brief uses \(U=\lfloor T^{1/2047}\rfloor\). Formula (1) is uniform in \(U\). Its constants depend on \(\varepsilon\), fixed windows and finitely many Schwartz seminorms, not on real \(T,R\), the level or cutoff. The elementary divisor bound gives \(r_2(n)\ll_\eta n^\eta\).

The only non-elementary exponential-sum input is the accepted global exponent pair \((13/84+\eta,55/84+\eta)\), in exactly the derivative class and parameter range of `sources/bourgain_2017_exponent_pair.md`. The accepted repaired Li--Yang theorem supplies \(P(x)\ll_\varepsilon x^{\theta+\varepsilon}\) for all real \(x\). Its narrow accepted scope is unchanged. The previously printed \(q_0=262/27\) moment is used only for comparison and to explain the frozen lower threshold; no part of the proof of (1)--(3) needs an enlarged printed endpoint.

The Poisson/Bessel reconstruction is rederived in Section 3 below. It remains candidate proof evidence until the conductor's required seam reviews and graph decision. Citation of the earlier candidate interface does not promote it, nor does this report change the inherited status of any source or parent.

## 3. Proof and complete cost accounting

### Correlations: small parameters, the global source range, and interpolation

For a dyadic integer \(N\ge1\), let
\[
 C_N(u)=\sum_{N<n\le2N}e(u\sqrt n).
\]
For every \(0<|u|\le C_1T\) and \(N\le T^{3/2}\),
\[
 |C_N(u)|\ll_\varepsilon T^\varepsilon\sqrt N
                    (|u|^\kappa+|u|^{-1}).              \tag{5}
\]
There is a separate diagonal \(C_N(0)=N\); (5) is never used at zero.

It suffices to take \(u>0\), as the negative case is conjugate. If \(u\le\sqrt N\), then
\[
 f'(x)=\frac{u}{2\sqrt x}\in
 \left[\frac{u}{2\sqrt{2N}},\frac{u}{2\sqrt N}\right]
 \subset(0,1/2].
\]
This derivative is monotone and separated from every integer by a constant times \(u/\sqrt N\). The elementary first-derivative estimate gives \(|C_N(u)|\ll\sqrt N/u\). For \(u<N^{-1/2}\) this is weaker than the trivial \(N\), which is retained if needed; no large-parameter theorem is used in this smallest regime. The same estimates hold on every proper subinterval.

For \(u\ge\sqrt N\), the second-derivative estimate gives
\[
 |C_N(u)|\ll u^{1/2}N^{1/4}+u^{-1/2}N^{3/4}
             \ll u^{1/2}N^{1/4}.                         \tag{6}
\]
For the source input set \(\mathcal T=u\sqrt N\), \(M=N\), and \(F(t)=\sqrt t\) on \([1,2]\). For every fixed derivative order \(j\ge1\),
\[
 f^{(j)}(x)=u\left(\prod_{h=0}^{j-1}(1/2-h)\right)x^{1/2-j}.
\]
These are the exact nonvanishing monomial derivatives in the standard exponent-pair class (the first derivative is a positive constant times \(x^{-1/2}\)). All normalized constants are fixed. Moreover \(1\le M\le\mathcal T\) is precisely \(u\ge\sqrt N\). Thus the accepted global Theorem-6 interface gives
\[
 |C_N(u)|\ll_\eta
 (u/\sqrt N)^{13/84+\eta}N^{55/84+\eta}
 \ll_\varepsilon T^\varepsilon u^{13/84}N^{97/168}.      \tag{7}
\]
The last loss is legitimate because \(u\ll T\), \(N\le T^{3/2}\), and \(\eta\) can be chosen arbitrarily small. We do not impose the direct Theorem-4 window. Our Gram vectors use the full dyadic interval, so no shorter-interval rescaling is involved. Proper intervals, if desired, are allowed by the accepted source's partial-sum device.

The minimum of (6) and (7) is at most their geometric mean with powers \(13/55\) and \(42/55\). The resulting exponents are
\[
 \tfrac12\tfrac{13}{55}+\tfrac{13}{84}\tfrac{42}{55}
       =\tfrac{13}{55},\qquad
 \tfrac14\tfrac{13}{55}+\tfrac{97}{168}\tfrac{42}{55}
       =\tfrac12.
\]
This proves (5) in every regime. No source assertion for arbitrary weights is used.

### Finite-vector duality and the diagonal

Take any actual finite dyadic block, allowing a hard lower or upper truncation, and set its missing coefficients to zero on the ambient interval:
\[
 S_N(R)=\sum_{N<n\le2N}b_n e(R\sqrt n),\quad
 b_n=a_n(T){\bf1}_{U<n\le M_0}.
\]
The proof in fact permits arbitrary complex coefficients satisfying the same bound
\[
 \sum|b_n|^2\ll_\eta N^{-1/2+2\eta}.                  \tag{8}
\]
Let \(R_1,\ldots,R_L\) be \(\delta\)-separated points in an interval of length at most \(h\), all lying in \([cT,CT]\), where \(\delta=N^{-1/2}\), and suppose \(|S_N(R_j)|>v\). Choose unit complex numbers \(z_j\) that align the values. Cauchy--Schwarz in the actual coefficient space gives
\[
 L^2v^2\le\Big(\sum|b_n|^2\Big)
       \sum_{i,j}z_i\overline{z_j}C_N(R_i-R_j).          \tag{9}
\]
The expression on the right is nonnegative before taking entrywise bounds. Its diagonal contributes exactly \(L N\) inside the Gram form. Ordered separation gives
\[
 \sum_{i\ne j}|R_i-R_j|^{-1}
 \ll L\delta^{-1}\log(2+T/\delta),\qquad
 \sum_{i\ne j}|R_i-R_j|^\kappa\le L^2h^\kappa.
\]
After (5), (8), and absorption of the finite logarithm, for every fixed small \(\tau>0\) there is \(G=C_\tau T^\tau\) such that
\[
 L^2v^2\le G\{L\sqrt N+L^2h^\kappa\}.               \tag{10}
\]
The first term contains both the full diagonal and the inverse-distance row sum. It is not discarded even when \(L=1\).

Choose
\[
 h=(v^2/(2G))^{1/\kappa}.
\]
Then every such separated family obeys
\[
 L\le 2G\sqrt N\,v^{-2}.                             \tag{11}
\]
This argument is valid also when \(h<\delta\); in that case a separated family in one interval has at most one point, and (10) still pays for it.

### Real level sets and the localization ceiling

Partition \([cT,CT]\) into at most
\[
 J_h\le1+(C-c)T/h                                    \tag{12}
\]
intervals of length at most \(h\). This includes one interval when \(h\) exceeds the entire physical window. In each interval take a maximal \(\delta\)-separated subset of \(\{|S_N|>v\}\). Its cardinality is finite, and maximality covers that entire level set by intervals of radius \(\delta\) around the selected points. No differentiability, persistence width, or integer sampling assumption is needed. Equations (11)--(12) therefore give
\[
 \operatorname{meas}\{R\in[cT,CT]:|S_N(R)|>v\}
 \ll Gv^{-2}\{1+T(2G/v^2)^{1/\kappa}\}
 \ll_\varepsilon T^\varepsilon(v^{-2}+T v^{-q}).        \tag{13}
\]
Choose \(\tau\) small enough in terms of the desired \(\varepsilon\) before this final absorption. In particular, the factor \(G^{1+1/\kappa}\) is included. Multiplication by \(\|w\|_\infty\) gives the weighted version. The corresponding cosine block has modulus at most \(|S_N|\), since it is \(\operatorname{Re}(e(-3/8)S_N)\). Formula (13) holds for every \(v>0\). Extremely small \(v\) merely produces a bound weaker than the interval's length.

The summand \(v^{-2}\) is exactly the product of the Gram diagonal's \(\sqrt N\), the covering radius \(N^{-1/2}\), and the ceiling's constant term. Dropping any of these costs would change the assertion.

### Every dyadic block and the infinite upper tail

Take \(M_0=\lfloor T^{3/2}\rfloor\). Schwartz decay and the divisor bound give, for every fixed \(A>1/2+2\eta\),
\[
 \sum_{n>M_0}|a_n(T)|
 \ll_{A,\eta}T^{A/2}M_0^{1/4+\eta-A/2}
 \ll T^{3/8+3\eta/2-A/4}.                            \tag{14}
\]
Consequently this tail is \(O_K(T^{-K})\) for any prescribed \(K\), by selecting a sufficiently large fixed Schwartz seminorm. The estimate is uniform in real \(R\) and in the lower cutoff. The actual series is absolutely convergent.

There are at most \(J\ll\log(2T)\) dyadic blocks below \(M_0\), including the partial block at \(U\) and the one at \(M_0\). If \(|B_{T,U}(R)|>V\ge1\), the discarded upper tail is at most \(V/2\) for sufficiently large \(T\), so some retained cosine block exceeds \(V/(2J)\). Union over all blocks in (13) yields factors at most \(J^3\) and \(J^{q+1}\); choosing the earlier epsilon losses sufficiently small absorbs them. This proves (1). If \(U\ge M_0\), (14) alone makes the level set empty for large \(T\). Bounded \(T\) is absorbed by the constants.

Thus all tails and every mixed contribution are restored before any moment is taken. No moment expansion or termwise absolute twelve-frequency majorant was used. For completeness, should a finite twelfth-moment comparison be desired, \(\sum|a_n|\ll T^{1/4+\eta}\) makes its upper-tail error at most \(T^{15/4+11\eta-K}\), arbitrarily small after increasing \(K\).

### Exact smoothing cost, pointwise cutoff, and complete moments

This subsection independently reproduces the authorized reconstruction seam. Fix the same smoothing length \(s=T^{-1/2}\) over the entire window and let
\[
 S_s(R)=\sum_{m\in\mathbb Z^2}(1_{B_R}*\rho_s)(m).
\]
The difference from the inclusive sharp count is supported on the annulus \(R-s\le|m|\le R+s\). Its squared radii occupy a real interval of length \(O(Rs+1)\), so
\[
 |N(R)-S_s(R)|\le
 \sum_{(R-s)^2\le n\le(R+s)^2}r_2(n)
 \ll_\varepsilon T^{1/2+\varepsilon}.                 \tag{15}
\]
Both endpoints, and hence the full jump at an integral \(R^2\), are included.

Poisson summation applies to the smooth compactly supported convolution. The disk transform and the fixed order-one Bessel asymptotic give
\[
 S_s(R)-\pi R^2
 =R\sum_{n\ge1}r_2(n)n^{-1/2}\Psi(\sqrt{n/T})
                         J_1(2\pi R\sqrt n),
\]
\[
 J_1(z)=\sqrt{2/(\pi z)}\cos(z-3\pi/4)+O(z^{-3/2}).
\]
The summed Bessel remainder is
\[
 \ll R^{-1/2}\sum_{n\ge1}r_2(n)n^{-5/4}|\Psi(\sqrt{n/T})|
 \ll T^{-1/2}.                                       \tag{16}
\]
The last sum converges by the divisor bound with a fixed exponent below \(1/4\). Thus the exact full-window interface is
\[
 P(R^2)=\frac{\sqrt R}{\pi}H_T(R)
                  +O_\varepsilon(T^{1/2+\varepsilon}).\tag{17}
\]
The mollifier remains fixed as \(R\) varies. Uniformity is for all real \(R\in[cT,CT]\), not only integer or nonjump radii.

The accepted pointwise theorem and (17) yield
\[
 \|H_T\|_\infty\ll_\varepsilon T^{\beta+\varepsilon}+T^\varepsilon
                   \ll_\varepsilon T^{\beta+\varepsilon}.
\]
For the brief's tail, subtracting the head costs
\(\sum_{n\le U}|a_n|\ll U^{1/4+\varepsilon}\); at its fixed cutoff \(1/(4\cdot2047)<\beta\), so the same supremum follows. For other lower cutoffs the distribution (1) still holds, but this same supremum is not asserted without paying the head.

Layer cake with (1), including levels below one by the trivial finite measure, gives for every fixed \(p>q\)
\[
 \mathcal M_p(T)\ll_\varepsilon
 T^{1+\varepsilon}+T^{(p-2)\beta+\varepsilon}
                 +T^{1+(p-q)\beta+\varepsilon}.          \tag{18}
\]
For \(2\le p\le q\), the last term is replaced by \(T^{1+\varepsilon}\), with a logarithm at \(p=q\). Exactly \(\beta(q-2)>1\), equivalently \(\beta>13/110\), so the third term in (18) is dominated by the second. Hence
\[
 \mathcal M_p(T)\ll_\varepsilon
          T^{1+\varepsilon}+T^{(p-2)\beta+\varepsilon}
          \quad(p\ge2\text{ fixed}).                   \tag{19}
\]
At \(p=12\), \(10\beta>1\), giving (2). In particular, the apparently favorable term \(T^{1+(20/13)\beta}\) alone is not the twelfth-moment conclusion: the diagonal contributes the larger \(T^{10\beta}\).

To return to the inclusive discrepancy, \(x=R^2\), \(dx=2R\,dR\), and (17) give
\[
 \int_{Y/2}^{3Y}|P(x)|^{12}dx
 \ll_\varepsilon T^7\mathcal M_{12}(T)+T^{8+\varepsilon}
 \ll_\varepsilon T^{7+10\beta+\varepsilon}
 =Y^{1+10\theta+\varepsilon}.                          \tag{20}
\]
The powers \(T^6\) from the leading amplitude, \(T\) from the Jacobian, and \(T^8\) from the full annulus error are all present. This proof uses (1) for \(H_T\) itself, so it does not rely on the tiny-head theorem or on transferring an old sharp-residual source theorem to the mollified series.

The inherited comparison has radius moment exponent \(1+(12-q_0)\beta\), \(q_0=262/27\). Its excess over the new \(10\beta\) is exactly
\[
 1-(q_0-2)\beta=1-\frac{208}{27}\beta>0.               \tag{21}
\]
This is positive because the accepted exact \(\theta<131/416\), equivalently \(\beta<27/208\). Thus the improvement is strict but small. Inclusive one-sided persistence applied to (20) gives \((1+10\theta)/13\), and
\[
 \frac{1+10\theta}{13}-\theta=\frac{1-3\theta}{13}>0.
\]
It is weaker than the already accepted pointwise exponent. No pointwise improvement is obtained by feeding this moment back into persistence.

### Quantitative confrontation with the full frozen target

At \(V=T^v\), divide each summand of (1) by the frozen right side \(T^{29/25}V^{-12}\). The powers are respectively
\[
 10v-\frac{29}{25},\qquad
 -\frac4{25}+\frac{20}{13}v.                           \tag{22}
\]
Thus both are nonpositive only through
\[
 v\le\min\{29/250,13/125\}=13/125.
\]
This covers a genuine initial segment of the required \([54/775,\beta]\), but not its high end. The two summands in (1) cross at \(v=13/110\). Above that value the complete diagonal is larger. At \(v=\beta\), the needed saving relative to (1) is at least
\[
 T^{10\beta-29/25}
\]
for its diagonal-sized bound; the second summand also exceeds target by \(T^{(20/13)\beta-4/25}\). Both exponents are strictly positive. The complete moment exponent misses \(29/25\) by exactly \(10\beta-29/25\). These are quantified deficiencies of the proved upper bound, not lower bounds for the arithmetic distribution.

### A coefficient-sensitive attempt and its exact failure

The previous proof used the arithmetic coefficients only through their norm. To retain more arithmetic, factor \(r_2(n)\) between the coefficient vector and Gram vectors. The weighted correlation becomes
\[
 W_N(u)=\sum_{N<n\le2N}r_2(n)e(u\sqrt n),
\]
while the coefficient energy is
\[
 \sum_{N<n\le2N}r_2(n)n^{-3/2}|\Psi(\sqrt{n/T})|^2\ll N^{-1/2},
\]
and the weighted diagonal remains \(\sum_{N<n\le2N}r_2(n)\asymp N\). No power is saved on the diagonal.

Use the exact summatory identity
\(\sum_{n\le x}r_2(n)=\pi x+P(x)-1\), with Stieltjes endpoint conventions matching \((N,2N]\). Integration by parts retains
\[
 W_N(u)=\pi\int_N^{2N}e(u\sqrt x)dx
 +[(P(x)-1)e(u\sqrt x)]_N^{2N}
 -\pi i u\int_N^{2N}(P(x)-1)x^{-1/2}e(u\sqrt x)dx.     \tag{23}
\]
The accepted pointwise theorem therefore gives, for \(|u|\ge N^{-1/2}\),
\[
 |W_N(u)|\ll_\varepsilon
 \sqrt N/|u|+N^{\theta+\varepsilon}(1+|u|\sqrt N).       \tag{24}
\]
The integral main term follows by substituting \(y=\sqrt x\) and integrating \(2y e(uy)\); its \(|u|^{-2}\) remainder is dominated in this range. Formula (23) displays the essential phase derivative; omitting it would manufacture a saving.

After division by \(\sqrt N\) in the Gram estimate, the additional error is
\[
 N^{\theta-1/2+\varepsilon}+|u|N^{\theta+\varepsilon}.
\]
The second term forces a local length only of size \(h\lesssim v^2N^{-\theta}\), up to epsilon factors, instead of the generic \(v^{2/\kappa}\). For \(v\) larger than a fixed constant, the same complete covering yields at best
\[
 D_N(v)\ll_\varepsilon T^\varepsilon
                 (v^{-2}+T N^\theta v^{-4}),            \tag{25}
\]
which is weaker in the relevant range, and still contains the identical diagonal. This bounded coefficient-sensitive attempt fails at the absolute estimation of the oscillatory \(P(x)\) integral in (23). Improving it requires a new oscillatory arithmetic estimate, not the accepted pointwise theorem alone.

A generic aligned control makes the diagonal obstruction concrete. Choose an interior \(R_0\asymp T\), \(N\asymp T^{4v}\), and arbitrary complex coefficients \(b_n=N^{-3/4}e(-R_0\sqrt n)\). Their energy has exactly the scale (8), and \(|S_N(R)|\gg N^{1/4}\) on an interval of length \(\gg N^{-1/2}\) around \(R_0\). Thus their level-set measure is \(\gg V^{-2}\) for \(V\asymp N^{1/4}\). A real cosine version at the relevant high levels takes
\[
 b_n=N^{-3/4}\cos(2\pi R_0\sqrt n-3\pi/4).
\]
At \(R_0\), its cosine sum is \(N^{-3/4}\sum\cos^2(2\pi R_0\sqrt n-3\pi/4)\gg N^{1/4}\), because (5) bounds the oscillatory part by \(T^\varepsilon\sqrt N T^\kappa=o(N)\) when \(v>\kappa/2=13/110\). The derivative bound \(O(N^{3/4})\) preserves this size on an interval of length \(cN^{-1/2}\). In particular \(v=\beta\) is allowed. These coefficient families violate any proposed generic deletion of the \(V^{-2}\) term and the generic frozen estimate when \(10v>29/25\). They are not the actual \(r_2(n)n^{-3/4}\Psi\), and prove no arithmetic counterexample.

## 4. First doubtful or unproved step

No missing diagonal, ceiling, small-parameter regime, or upper tail remains in the proof of (1). The new candidate distribution and its moment consequences still require the conductor's independent source, covering, and reconstruction reviews before graph promotion.

The first genuinely new estimate needed for the frozen objective is an arithmetic improvement of the complete level distribution for \(T^{13/125}<V\le T^{\beta+\varepsilon}\), ultimately paying both positive exponents in (22). The coefficient-blind Gram operator estimate cannot supply it, as the aligned control shows. This does not prove that (1) is sharp for the arithmetic coefficients.

In the explicit coefficient-sensitive attempt, the first unresolved analytic quantity is the oscillatory integral in (23). The available \(|P(x)|\ll x^{\theta+\varepsilon}\) bound controls its modulus only after paying \(|u|\sqrt N\), leading to (24)--(25). An estimate that removes this cost, or a different arithmetic projection bound, has not been established here. Rephrasing it as an arithmetic Gram matrix is not a proof.

The full frozen bound, the quarter theorem, M1, M2, M9 and endpoint obligations remain open. The improved moment does not alter the accepted pointwise exponent.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `actual_coefficients` | PASS: (4), (8), and (14) use the exact arithmetic coefficients, with no positivity requirement on \(\Psi\). The source theorem acts only on unweighted Gram correlations. The coefficient-sensitive attempt is exactly (23). |
| `complete_distribution` | PASS for (1): every level \(V\ge1\), every physical point and every finite block is covered; the upper tail is restored uniformly. The frozen stronger distribution remains open. |
| `full_diagonal_and_ceiling` | PASS: \(C_N(0)=N\) is retained in (9)--(11), and the constant one in (12) produces \(V^{-2}\). Both one-sample and \(h>T\) cases are included. |
| `source_hypotheses` | PASS at the accepted-card specialization level: exact square-root derivatives, \(\mathcal T=u\sqrt N\ge N\), global Theorem 6, fixed ambient interval, and small-\(u\) replacement are explicit. A fresh independent primary-source audit belongs to the separate assigned task. |
| `all_tails_and_ranges` | PASS: \(u<N^{-1/2}\), \(N^{-1/2}\le u\le\sqrt N\), \(u\ge\sqrt N\), arbitrary localization lengths, hard partial blocks, all dyadic blocks, and \(n>T^{3/2}\) are priced. |
| `real_uniformity` | PASS: the covering uses real level sets; (15) includes both annular endpoints and every inclusive jump. No integer-radius restriction is introduced. |
| `net_moment_and_pointwise_powers` | PASS: full moment exponent \(10\beta\), sharp twelfth-moment exponent \(1+10\theta\), full target gap \(10\beta-29/25\), and weaker persistence exponent \((1+10\theta)/13\) are explicit. |
| `independent_statement_only_control` | Not claimed by this selected-context report. No sibling report was read. The separate statement-only task and conductor-required seams remain mandatory. The aligned control above is an additional internal falsification control. |
| `no_parent_overclaim` | PASS: (1)--(3) are candidate subordinate evidence only; no source status, parent, or pointwise exponent is promoted. Generic aligned coefficients are explicitly distinguished from actual \(r_2\). |

Other analytical edge checks: \(L=1\) retains its full energy; \(h<\delta\) is allowed; \(h\ge(C-c)T\) retains one localization interval; a partial dyadic block is embedded by zero coefficients; a lower cutoff beyond the upper truncation is covered solely by (14); \(u=0\) never enters (5); \(U=0\) directly proves the full-series bound. No computational experiment is used.

## 6. Dependencies and exact artifacts used

The selected-context inputs read are:

- `protocol.md`.
- `state/proof_obligations.yml`, with targeted extraction of the accepted Bourgain global interface, repaired Li--Yang theorem and audit, exact-resonance mass and absolute-majorant obstruction; none is altered.
- `state/active_campaign.yml`, Round 204.
- `strategy/round204_complete_large_values_attack.md`.
- `rounds/codex-managed/gc-complete-large-values-duality/briefs/actual_large_values_attack.md`.
- `rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md`.
- `sources/bourgain_2017_exponent_pair.md`.
- `rounds/codex-managed/gc-complete-signed-convolution-attack/reports/arithmetic_signed_tail_attack.md`.
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/signed_cutoff_tail_moment_audit.md`.

During the bounded task, the conductor explicitly authorized the additional reconstruction context `rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/reports/whole_moment_analytic_attack.md`, Sections 2 and 3.1--3.3. The reconstruction subsection above uses only those authorized definitions and the Poisson/Bessel/annulus/tail seam. It is rederived, not accepted by citation. No sibling derivation or other new research context is used.

The external exponential-sum source remains Jean Bourgain, *Decoupling, exponential sums and the Riemann zeta function*, JAMS **30** (2017), 205--224, DOI [10.1090/jams/860](https://doi.org/10.1090/jams/860), [arXiv:1408.5794v2](https://arxiv.org/abs/1408.5794), Section 5 and Theorem 6, in the exact accepted source-card scope. This task does not claim to have conducted the separately assigned new primary-source/version audit. Elementary first/second derivative bounds, finite-dimensional Cauchy--Schwarz, separated-point covering, Schwartz decay, Poisson summation for a smooth convolution, the fixed Bessel asymptotic, Stieltjes integration by parts and layer cake supply the remaining steps.

## 7. Recommended state effect

Recommend **retain as candidate evidence pending independent seams**, then **promote only if all required reviews pass**, the complete distribution (1), including its full-series variant, and its complete moment consequences (19)--(20). The scope is a better moment bound with unchanged pointwise benchmark. The natural round exit, if these seams pass, is `complete_distribution_gain_target_open`.

**Retain** the full frozen target and all parent obligations as open. **Reject** any conclusion omitting \(V^{-2}\), using the offdiagonal moment term alone, guessing a new printed source endpoint, or treating the generic aligned control as an arithmetic counterexample. **Retain** (23)--(25) as a bounded unsuccessful coefficient-sensitive attempt, not a universal no-go for arithmetic large values.

No graph, proof draft, validation matrix, synthesis, source card, or successor plan was edited. This assigned discovery report is complete and the task stops here.
