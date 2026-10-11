# Round 200 actual-symbol, norm, and power audit

- Campaign: `m9-m1-t1-complete-source-coefficient-mask-analysis`.
- Task: `actual_symbol_norm_power_audit`; role: independent seam reviewer.
- Starting graph SHA-256: `2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`; locally rechecked unchanged.
- Generated: 2026-09-23, Asia/Shanghai.
- Evidence: candidate audit only. No shared proof-state edits, numerical experiments, or external theorem imports.
- Isolation: no other Round-200 report was read. Conductor messages requested an auxiliary pre-selector scalar audit and required an explicit qualification for incompletely expanded literal trace predicates; both are incorporated below.

## 1. Result: exact norm interfaces, with the analytic estimate open

The complete residual even-shift correlation has a cheap **actual coefficient** factorization in its original endpoint or product coordinates. In product coordinates its amplitude is exactly

\[
 A_{MN}=c_{M,\sigma}^{\rm rem}\overline{c_{N,\sigma}^{\rm rem}},
 \qquad \|A\|_\pi=\sum_N|c_{N,\sigma}^{\rm rem}|^2
 =D_{L,\sigma}\ll_\varepsilon L^2X^\varepsilon.
 \tag{200.N1}
\]

This keeps every squarefree, divisor, selector, profile, and endpoint condition. It does not estimate a replacement bounded array. However, the exact even Fejer band kernel in these coordinates has all-vector operator norm \(\asymp R_0\asymp L\), because its square-root phase is a removable row/column phase. Thus (200.N1) gives only \(L^3X^\varepsilon\) correlation capacity. This proves an obstruction to an all-vector saving for **that coarse kernel**, not a counterexample to the fixed actual-coefficient target.

Geometric interval sections can be identified for the explicit cone, shell, height, ratio-profile, product-band, and positive affine-row predicates. Squarefreeness, endpoint coprimality, and the product-dependent selected-pair residual mask are not thereby interval masks. In reparametrized arithmetic coordinates they must stay inside the exact kernel or the exact mixed amplitude until separately estimated. No affordable mixed-amplitude norm for an unspecified transformed arithmetic kernel has been established.

An auxiliary calculation before the XOR split is useful: the explicit smooth stationary core, including squarefreeness/coprimality, has projective norm \(O_\varepsilon(L\log^2(2L)X^\varepsilon)\) in the two original legs. This uses the elementary gcd expansion and row-interval decomposition. Its extension to **every inherited literal trace factor** is conditional on the finite interval/BV certificate stated in Section 3.6; this report does not replace the unnamed trace predicates by invented formulas. A square-root all-vector estimate for the resulting square-root phase matrices would then imply the full original-\(t=1\) scalar target. Neither that phase estimate nor the frozen residual correlation estimate is proved here.

Compatible exit label: `complete_source_interface_with_open_estimate`.

## 2. Exact statement and hypotheses

Fix the same real \(X\), literal middle/lower hard-M1 shell \(L\ge2\), sign \(\sigma\), canonical allocation-independent selected pair, and total zero extension as K185.1--3. Write

\[
 y=\lfloor\sqrt X\rfloor,\quad q_X=X/y^2,
 \quad H=\lfloor yX^{-1/4}\rfloor,\quad R=\lceil L\rceil.
\]

The uncharactered frequency leg is denoted \(m\), the odd character-bearing dual leg \(d\). The source antecedents give the stationary moving factor

\[
 a(m,d)=c_{L,X,\sigma}\,
 \eta_L(m)\Phi(m/(H+1))
 W\!\left(\sqrt{4q_Xm/d}\right)
 \left({L^2\over md}\right)^{3/4}
 \mathcal M_{L,X,\sigma}(m,d).
 \tag{200.N2}
\]

Here \(c_{L,X,\sigma}\) is allocation-independent, bounded by \(X^\varepsilon\); \(\mathcal M\) is the **exact inherited literal factor**, including the original shell, height, strict cone, residual labels, floor, star/tie/half-weight, hard-sample, crossing, and endpoint/zero-extension data. Formula (200.N2) preserves that factor without claiming that every named trace has been expanded into a numerical predicate in this report. On support \(m,d\asymp L\), \(md\asymp L^2\), and \(L\le H\).

The actual residual coefficient is

\[
 \lambda_N(d)=\mu^2(N)\rho_N(d)a(N/d,d)
 \mathbf1_{N,d>0,\ d\mid N,\ d\text{ odd}},
 \quad c_N=\sum_d\chi_4(d)\lambda_N(d),
 \tag{200.N3}
\]

with every unsupported value zero and \(\rho_N\) exactly K185.1. In particular \(\rho_N\in\{0,1\}\); this bound supplies no smoothness or interval complexity.

The frozen quantity is

\[
 C^{(2)}=\sum_{\substack{0<r<R\\2\mid r}}(1-r/R)
 \sum_Nc_{N+r}\overline{c_N}
 e\!\left(\sigma\sqrt X(\sqrt{N+r}-\sqrt N)\right).
 \tag{200.N4}
\]

All following exact source identities retain one outer real part when applied to the energy. Absolute bilinear estimates below are explicitly stronger sufficient estimates, not assertions that shiftwise or sectorwise triangle is harmless.

For a finite complex matrix define

\[
 \|A\|_\pi=\inf_{A_{ij}=\sum_k u_k(i)v_k(j)}
 \sum_k\|u_k\|_2\|v_k\|_2.
 \tag{200.N5}
\]

This is the complex nuclear norm, with a bilinear factorization convention; a conjugate can be absorbed into the second vector. The infimum is over exact factorizations.

## 3. Proof and derivation

### 3.1 Actual stationary normalization and endpoint factorization

The positive Vaaler coefficient is
\(\alpha_{m,H}=i\Phi(m/(H+1))/(2\pi m)\).
The stationary transform contributes \((mX)^{1/4}d^{-3/4}\), and the actual outer \(-4\alpha_{m,H}\) therefore gives

\[
 -{2e(1/8)\over\pi}X^{1/4}
 \Phi(m/(H+1))(md)^{-3/4}
 W\!\left(\sqrt{4q_Xm/d}\right).
\]

After inserting \(\eta_L\) and removing the physical multiplier
\(X^{1/4}L^{-3/2}\), the normalized power is precisely
\((L^2/(md))^{3/4}\). There is no \(H/L\), additional Vaaler \(m^{-1}\), or extra \(X^{1/4}\) inside (200.N2). The negative branch is the corresponding conjugate branch; the norm ledger is identical. The character remains on \(d\), while \(\eta_L\) and \(\Phi\) remain on \(m\).

Set, on a finite containing endpoint box,

\[
 F(m,d)=\chi_4(d)\mu^2(md)\rho_{md}(d)a(m,d)
 \mathbf1_{d\text{ odd}},
 \quad n(m,d)=md.
\]

Then (200.N4) is exactly

\[
 \sum_{x',x}F(x')\overline{F(x)}
 \mathbf1_{0<n(x')-n(x)<R,\ 2\mid n(x')-n(x)}
 (1-(n(x')-n(x))/R)
 e\!\left(\sigma\sqrt X(\sqrt{n(x')}-\sqrt{n(x)})\right).
 \tag{200.N6}
\]

Each ordered endpoint allocation pair occurs once. Compressing each endpoint fibre \(n(x)=N\) gives \(c_N\) exactly; it does not choose one representative divisor. Since there are \(O(L^2)\) endpoint pairs and bounded normalized coefficients,
\(\|F\|_2^2\ll L^2X^\varepsilon\). The projective norm of the endpoint amplitude \(F(x')\overline{F(x)}\) is exactly \(\|F\|_2^2\).

For compressed coefficients, the divisor bound gives
\(|c_N|\ll X^\varepsilon\) on \(O(L^2)\) product sites, so \(D\ll L^2X^\varepsilon\). A rank-one matrix \(u v^T\) has one nonzero singular value \(\|u\|_2\|v\|_2\), proving (200.N1). These are affordable complete-source norm bounds already proved; selector complexity has not been erased.

Any exact disjoint identity \(P_{\rm cl}+P_1+P_2=1\) on the opened domain can be inserted in (200.N6) and summed back without a boundary or multiplicity error. This is all that is needed here from that partition. Likewise, for one genuine common-domain transport \(U\),
\(\sum_j[M_j,U]=[I,U]=0\). This does not license sector-dependent transports, alter physical support, or supply a power saving. No separate absolute norm of \(P_1\) or \(P_2\) is taken in (200.N6).

### 3.2 Explicit geometric sections versus arithmetic deletions

The following statements concern geometry only; the full arithmetic support is not asserted to equal these intervals.

| Coordinates and fixed data | Explicit moving geometric conditions | Section in the ordered column |
|---|---|---|
| Fixed \(m\), column \(d\) | \(4m<d<16m\); a ratio cell for \(\sqrt{4q_Xm/d}\); product interval \(A<md\le B\) | Each is an interval; intersections are intervals; exact equality is a singleton. |
| Product rows \(N\), column \(M\), separated parity | \(N<M<N+R\) | One interval on the parity lattice. The Fejer factor is a bounded-variation weight on it. |
| Fixed odd \(d,d'\), lower row \(m\), upper column \(m'\) | \(0<d'm'-dm<R\) plus upper height/shell/cone/ratio conditions | One interval after intersecting the explicit conditions. Split \(m,m'\) into their two common parity classes. |
| K185 primitive row, fixed \((\kappa,g,h,U,v,\omega)\), column \(t\) | \(S_0+Ut>0\), \(w_0+vt>0\), leg shells/heights, cone and ratio cells, product bounds | Each is an interval or a half-line; their intersection is an interval on each explicit geometric cell. |

For the last line, in the plus orientation \(d=\kappa gU\), \(m'=\kappa v\) are constant while
\(d'=\kappa gU+2g(S_0+Ut)\) and
\(m=\kappa v+2(w_0+vt)\) increase affinely. Thus lower \(d/m\) decreases and upper \(d'/m'\) increases. In the minus orientation the endpoint roles reverse. Both products increase affinely in \(t\), at the same positive slope, with their difference \(r\) fixed. This proves the listed interval assertions directly. Positivity is enforced before evaluating square roots. The \(U=1\) anchors retain the same affine facts.

The remaining arithmetic tests are materially different:

- \(d\mid N\) is absorbed exactly by the incidence coordinates, or retained in (200.N3).
- \(\mu^2(md)=\mu^2(m)\mu^2(d)\mathbf1_{(m,d)=1}\); squarefreeness and coprimality of varying affine forms can leave repeated holes. Their row complexity has not been bounded by a constant.
- \(\rho_{md}(d)\) depends on the selected prime pair of the changing product. The selector is canonical and allocation-independent at **one fixed product**; this does not make it constant, BV, or a union of few intervals as the product varies.
- The primitive outer coprimalities \((gU,v)=1\), \((U,h)=1\) and any retained congruence conditions belong to the exact arithmetic domain. They are not geometric thresholds.
- \(\chi_4(d')\chi_4(d)=(-1)^{(d'-d)/2}\), or \((-1)^{S_0+t}\) on the affine row, is a signed factor. The inherited arithmetic deletions prevent a bare alternating-row argument.

Parity can be handled by a bounded split into lattices, or retained in the kernel. Arbitrary arithmetic deletions cannot be assigned the same bounded cost.

There is a separate literal-field seam. K184.11 and its coefficient reviews state a fixed finite vertical/horizontal/ratio/trace ledger, but the exact files read here do not give a numerical predicate and value formula for every inherited star, tie, half-weight, hard-sample, crossing, and residual-label field. Their names alone are insufficient to certify the coefficient norm of a **new** mixed-coordinate import. The present exact source keeps them in \(\mathcal M\). All interval claims in the table are verified for the displayed predicates; a complete-field claim requires the certificate in Section 3.6 or their retention in the import's norm/kernel.

### 3.3 The coarse product kernel has no all-vector power saving

On a positive containing interval \(I\) of \(M_L\asymp L^2\) product sites, put

\[
 K_{MN}=\mathbf1_{0<M-N<R,\ 2\mid M-N}
 (1-(M-N)/R)e\!\left(\sigma\sqrt X(\sqrt M-\sqrt N)\right).
\]

Let \(T\) be the same matrix with the last phase removed. Diagonal multiplication by \(e(\sigma\sqrt{XM})\) and its inverse gives \(K=UTU^*\); hence \(\|K\|_{2\to2}=\|T\|_{2\to2}\).

Each row and column sum of \(|T|\) is at most \(R\), so Schur's test gives \(\|T\|\le R\). Conversely test \(T\) on normalized constant vectors on \(I\). For all even \(r\le R/2\) the weight is at least \(1/2\), and there are \(M_L-r\) pairs at that gap. For \(R\ge8\), \(M_L\ge2R\),

\[
 {1\over M_L}\sum_{\substack{0<r<R\\2\mid r}}
 (1-r/R)(M_L-r)\gg R.
\]

Thus \(\|K\|\asymp R\), with bounded small cases irrelevant to the power ledger. The vectors in this norm test may absorb the phase. They are used only to establish a matrix norm fact, **not** as purported physical coefficients or as a lower bound on (200.N4).

The exact product-vector bound therefore gives

\[
 |C^{(2)}|\le\|K\|D\ll L^3X^\varepsilon.
 \tag{200.N7}
\]

An all-vector bound \(\|K\|\ll X^\varepsilon\) uniformly over power-sized \(L\) is impossible for this kernel. A gain must exploit the actual coefficient vector more specifically, improve its relevant quadratic-form estimate, or use arithmetic coordinates whose kernel retains useful arithmetic structure and whose amplitude norm is controlled. There is no Kloosterman kernel identification in (200.N7).

The same raw capacity follows without operator language: \(O(L)\) shifts, \(O(L^2)\) product sites, and two divisor-bounded coefficients. It is an upper capacity, not an asymptotic lower mass.

### 3.4 Interval masks and the precise projective interface

Suppose on finite ordered columns \(1,\ldots,n\) that

\[
 \left|\sum_{i,j}u_i v_jK_{ij}\right|
 \le B\|u\|_2\|v\|_2
 \quad\text{for all complex }u,v.
 \tag{200.N8}
\]

Let \(\Lambda(n)=1+\lceil\log_2n\rceil\). A row-prefix mask admits a dyadic decomposition with at most one dyadic interval per scale in each row. At a fixed scale the associated row subsets are disjoint and the column intervals are disjoint. Hence the sum of rectangular product costs is at most
\(B\|u\|_2\|v\|_2\) by Cauchy--Schwarz. Summing scales proves a prefix cost \(\Lambda(n)\), an interval cost \(2\Lambda(n)\), and a union of at most \(J\) intervals cost \(2J\Lambda(n)\).

For an exact mixed amplitude \(A=\sum_k u_kv_k^T\), apply this bound termwise and take the infimum:

\[
 \left|\sum_{i,j}A_{ij}K_{ij}M_{ij}\right|
 \le 2J\Lambda(n)B\|A\|_\pi.
 \tag{200.N9}
\]

The same dyadic rectangles prove directly
\(\|u v^T M\|_\pi\le2J\Lambda(n)\|u\|_2\|v\|_2\).
An integral or finite signed combination of these masks is allowed with its **total variation / total absolute coefficient mass** included. Merely naming many products proves no cheap norm.

After a new arithmetic coordinate change, a bounded \(p\)-by-\(q\) mixed amplitude has only the generic bound

\[
 \|A\|_\pi\le\sqrt{\min(p,q)}\,\|A\|_F
 \ll X^\varepsilon\sqrt{pq\min(p,q)}.
\]

The Frobenius norm alone is not the projective norm. No claim that the actual selector attains this larger bound is made; the point is that a smaller claimed cost needs proof.

### 3.5 All-cost conditional correlation estimate

An import must first supply an exact, multiplicity-correct representation

\[
 C^{(2)}=C_{\rm safe}+E+
 \sum_\nu\gamma_\nu\sum_{i,j}
 A^{(\nu)}_{ij}K^{(\nu)}_{ij}M^{(\nu)}_{ij}.
 \tag{200.N10}
\]

Here the index \(\nu\) includes every shift, orientation, gcd, height, modulus, packet, completion and exceptional component actually introduced. \(\gamma_\nu\) contains the exact reconstruction and transform normalizations. \(E\) includes every discarded remainder; any exceptional part not proved small stays on the right. Arithmetic masks not proved geometrical are inside \(A^{(\nu)}\) or \(K^{(\nu)}\), with that choice stated before applying a theorem. All literal factors remain present.

If (200.N8) holds for each exact \(K^{(\nu)}\) with constant \(B_\nu\), if \(M^{(\nu)}\) is a union of \(J_\nu\) row intervals, and if the actual amplitude has norm \(\Pi_\nu=\|A^{(\nu)}\|_\pi\), then

\[
 \boxed{
 \Re C^{(2)}\le |C_{\rm safe}|+|E|
 +\sum_\nu |\gamma_\nu|\,2J_\nu\Lambda(n_\nu)
 B_\nu\Pi_\nu.}
 \tag{200.N11}
\]

This is the all-cost sufficient interface. A bounded-variation mixture adds its total coefficient mass to the corresponding summand. If an import assumes special vector coefficients, (200.N8) must be replaced by a theorem stable under the actual projective decomposition; arbitrary-vector extension cannot be presumed.

The target requires the last sum and all remainders to be \(\ll L^2X^\varepsilon\), uniformly. To record net powers, suppose after normalization to the raw \(L^3\) capacity that an applicable theorem saves \(c^{-\delta}\), \(c\asymp X^\gamma\), while **all** norms, interval complexities, completions, exceptional terms, and positive recombinations increase the baseline by \(X^a\). Then its correlation contribution is at best

\[
 L^3X^{a-\gamma\delta+\varepsilon}.
 \tag{200.N12}
\]

For \(L\asymp X^\ell\), closing this route needs
\(\gamma\delta-a\ge\ell\), with epsilon rebudgeting; a positive saving smaller than \(\ell\) does not close the deficit. The subscript sums in (200.N11), rather than a modulus exponent alone, decide \(a\). No values of \(\gamma,\delta,a\) are imported here.

As a subsidiary ledger only, the accepted high-\(h\) slice \(Y<h\le2Y\) has positive capacity \(YL^2X^\varepsilon\). Its analogous deficit is \(Y\), while the complete unsplit correlation has deficit \(L\). Closing all high-\(h\) slices at \(L^2X^\varepsilon\) costs only a dyadic logarithm afterwards. A saving on one height range gives no bound on its unestimated complement.

### 3.6 Auxiliary pre-selector scalar norm audit

This subsection concerns the full original-\(t=1\) scalar before XOR removal:

\[
 T_{\rm full}=\sum_{m,d\ge1\atop d\text{ odd}}
 \mu^2(md)\chi_4(d)a(m,d)e(\sigma\sqrt{Xmd}).
 \tag{200.N13}
\]

There is no \(\rho\) in this identity. A bound for (200.N13) would imply the residual **scalar** bound by subtracting the accepted XOR sector; it does not imply the frozen correlation inequality (200.N4).

First consider the explicit smooth stationary core with its displayed cone/height/shell geometry. Its power is separable:

\[
 (L^2/(md))^{3/4}=(L/m)^{3/4}(L/d)^{3/4}.
\]

All remaining unary factors have bounded size. The ratio factor has a uniform threshold decomposition: on the compact physical range, write

\[
 W(s)=W(s_*)+\int W'(u)\mathbf1_{s\ge u}\,du,
\]

with the integration endpoint convention chosen to cover that range. The total variation is \(O(1)\), and
\(s=\sqrt{4q_Xm/d}\ge u\) is the row prefix
\(d\le4q_Xm/u^2\). Intersecting with the displayed geometric intervals preserves a row interval. This handles the actual smooth \(W\), not a constant substitute for it.

Use the exact arithmetic identity

\[
 \mu^2(md)=\mu^2(m)\mu^2(d)
 \sum_{g\mid m,\ g\mid d}\mu(g).
 \tag{200.N14}
\]

Only odd \(g\) contributes when \(d\) is odd. On \(m,d\asymp L\), the two unary factors restricted to \(g\mid m,d\) have norm product \(O(L/g)\). Applying the proved interval/projective decomposition termwise yields, for this explicit core,

\[
 \|A_{\rm core}\|_\pi
 \ll X^\varepsilon\sum_{g\ll L}{L\over g}
 \log(2+L/g)
 \ll L\log^2(2L)X^\varepsilon.
 \tag{200.N15}
\]

This is an actual arithmetic coefficient calculation. Squarefree and gcd masks are not mislabelled as intervals; their cost is paid through (200.N14). Unary \(\mu^2\), \(\chi_4\), and sampled \(\eta_L\Phi\) require no extra regularity for the product norm.

For the **complete** \(a\), define the additional literal certificate explicitly. After restricting \(m=ga,d=gb\), the residual factor \(\mathcal M(ga,gb)\), together with the ratio weight and displayed geometric restrictions, must have an exact finite/integral decomposition into row-interval masks times bounded unary factors, with total weighted interval complexity \(V_g\). Every star, tie, half-weight, hard-sample, real-\(X\) crossing, residual label, and zero-extension trace must be assigned a predicate, value, and term in that decomposition. Singleton row traces are allowed; their exact values must be supplied. This report proves \(V_g=O(1)\) for the displayed smooth core and named explicit inequalities; it **does not certify this bound for every unnamed inherited literal field**.

Let \(B_g\) be a proved all-complex-vector bound for the exact phase matrix

\[
 K_g(a,b)=e(\sigma g\sqrt{Xab}),
 \quad a,b\asymp L/g,
\]

on the relevant containing rectangles. Retain parity and unary \(\mu^2(ga),\mu^2(gb)\) in the vectors. Subject to the complete literal certificate, (200.N14) and (200.N9) give the precise conditional scalar interface

\[
 \boxed{|T_{\rm full}|\ll X^\varepsilon
 \sum_{g\ll L\atop g\text{ odd}}
 {L\over g}\,V_g\log(2+L/g)\,B_g.}
 \tag{200.N16}
\]

For example, uniformly subpower \(V_g\) and
\(B_g\ll (L/g)^{1/2}X^\varepsilon\) would give
\(L^{3/2}X^\varepsilon\), since \(\sum g^{-3/2}\) converges and logarithms are absorbed. If the trace certificate instead costs a power, that power must remain in (200.N16). No estimate for these phase matrices is proved or imported. The kernel is the displayed square-root phase, not a Kloosterman sum. After residual selection, (200.N14) alone does not control \(\rho_{md}(d)\); a separate selector norm or kernel treatment is necessary in these leg coordinates.

### 3.7 Parity connector and scalar/physical reconstruction

Set \(z_N=c_Ne(\sigma\sqrt{XN})\), zero on the full complement. In each length-\(R\) window write the sum as its even-offset and odd-offset parts. The inequality \(|u+v|^2\le2|u|^2+2|v|^2\), followed by exact window counting, gives

\[
 E_R\le2D+4\Re C^{(2)}.
\]

Each pair at even gap \(r\) belongs to exactly \(R-r\) windows. Hence the last positive even-gap coefficient is \(4/R\) for odd \(R\ge3\) and \(8/R\) for even \(R\ge4\), exactly as K185.11. For \(R=1,2\), \(C^{(2)}\) is empty. There is no lost boundary window and no endpoint error. Summing windows back and applying Cauchy gives

\[
 |T_{\rm rem}|^2\le{M_L+R-1\over R}E_R
 \ll L\{L^2X^\varepsilon+\Re C^{(2)}\}.
\]

Consequently raw correlation capacity \(L^3\) returns scalar capacity \(L^2\), whereas the desired \(L^2\) correlation gives scalar \(L^{3/2}\). If (200.N12) is the available stronger absolute bound, reconstruction gives

\[
 |T_{\rm rem}|\ll X^\varepsilon
 \left(L^{3/2}+L^2X^{(a-\gamma\delta)/2}\right).
 \tag{200.N17}
\]

The physical stationary shell multiplier is \(X^{1/4}L^{-3/2}\), so this particular contribution would be

\[
 \ll X^{1/4+\varepsilon}
 \left(1+L^{1/2}X^{(a-\gamma\delta)/2}\right).
\]

This displays the restored deficit; it is not a new global exponent. The accepted transform boundary/error terms retain their previously proved bounds and are not inserted into \(c_N\) a second time. Even a complete scalar \(t=1\) proof leaves all other original \(t\) sectors and independent parents untouched.

## 4. First doubtful or unproved step

The primary unresolved statement remains
\(\Re C^{(2)}\ll L^2X^\varepsilon\) for the exact coefficients (200.N3). The cheap actual rank-one norm (200.N1) is proved, but the associated coarse kernel norm is \(\asymp L\); an all-vector \(O(1)\) estimate for it cannot supply the missing factor.

For an alternative arithmetic import, the first absent data are a concrete exact kernel satisfying an audited all-vector theorem and the resulting complete actual mixed norm/interval/completion costs in (200.N11). A phase resemblance or a bound for an enlarged array class is insufficient.

For the auxiliary scalar route there are two explicit gates: certify \(V_g\) for all inherited literal trace fields, and prove the phase-kernel bounds \(B_g\) strong enough for (200.N16). The smooth-core estimate (200.N15) does not bypass either gate. The selector is absent only because (200.N13) intentionally precedes the XOR split.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `complete_source_multiplicity` | PASS: ordered endpoint opening and product compression are exact; both opposing orientations, monotone incidences, all shifts and gcds are retained before optional routing. |
| `actual_coefficients_only` | PASS: exact \(a,\lambda,\rho,c\) are retained. The coarse norm test concerns all-vector theorem applicability only and does not refute physical coefficients. |
| `literal_endpoint_zero_extension` | PASS with explicit certificate limitation: exact source uses total zero extension and all literal fields; only the auxiliary full-symbol interval decomposition remains conditional. |
| `partition_recombination` | PASS: exhaustive partition masks sum to the original coefficient on one domain; commutator cancellation requires one common genuine transport. |
| `row_interval_vs_arithmetic_masks` | PASS: explicit geometric sections are derived; squarefree/coprime/selector support is not asserted to have few components. Unexpanded inherited trace predicates are identified. |
| `product_and_projective_norms` | PASS: exact complete product norm is \(D\ll L^2X^\varepsilon\); mixed norms use nuclear/projective cost. Smooth-core gcd norm is proved, complete literal extension is conditional. |
| `even_parity_connector` | PASS: full-line window count gives \(2D+4\Re C^{(2)}\); terminal coefficients apply for odd \(R\ge3\) and even \(R\ge4\), while \(R=1,2\) have empty \(C^{(2)}\). |
| `one_outer_real_part` | PASS: source has one outer real part; the absolute conditional import is clearly a stronger sufficient step with every positive recombination charged. |
| `net_power_ledger` | PASS: full \(L^3\to L^2\) deficit, subsidiary \(YL^2\to L^2\), outer \(L\) energy factor, square root, and physical multiplier all displayed. |
| `no_capacity_lower_bound` | PASS: no capacity count or matrix norm example is asserted to be a lower bound for the literal sum. |
| `no_unverified_theorem_import` | PASS: no external theorem applied; no Kloosterman identification or literature exponent credited. |
| `protected_parent_and_exponent_scope` | PASS: no complete small-\(t\), M1/M2, bridge, endpoint, target, or exponent claim. |

All controls are analytic. No numerical experiment was performed.

## 6. Dependencies and exact artifacts used

Assigned context read:

1. `protocol.md`.
2. `state/proof_obligations.yml`: authoritative status and selected exact nodes; the large graph was read through targeted entries after its initial output exceeded the tool budget.
3. `state/active_campaign.yml`.
4. `strategy/round200_complete_source_coefficient_mask_strategy.md`.
5. `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`: K184.1--6, K184.11, K184.19--21 and literal face ledger.
6. `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`: K185.1--12, complete opening and canonical affine coordinates, capacities and scope.
7. `proofs/kernels/m9_m1_hard_top_small_t_primitive_ray_sector_and_truncated_mobius_self_return.md`: exact original-\(t=1\) face and ray-factor antecedents.
8. `strategy/gauss_circle_strategy_review_2026-09-23.md`: interval/norm strategy only. Its literature statements were not adopted as imported mathematical dependencies.
9. The assigned task brief.

Additional exact-symbol antecedents followed and their purposes:

| Artifact | Provenance reason and part used |
|---|---|
| `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/coefficient_profile_endpoint_power_seam_review.md` | Named by K184; (184.RC3), normalization derivation, and literal face/trace ledger. Its old unrestricted-active-set defect is not reused. |
| `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/coefficient_profile_endpoint_power_post_repair_verification.md` | Confirms repaired active-support qualification and unchanged factorization. |
| `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/coefficient_product_endpoint_seam_review.md` | Exact antecedent cited by the preceding review; ray coefficient placement, BV and endpoint statement. |
| `rounds/codex-managed/m9-combined-top-cones/reports/blind_m1_top_transform.md` | Accepted graph evidence for the M1 transform; equations (1.4)--(2.3) fix Vaaler sign, character leg, normalized symbol, and physical multiplier. |
| `rounds/codex-managed/m9-combined-top-cones/reports/combined_cone_algebra.md` | Exact antecedent cited by the coefficient reviews; equations (2.3), (3.12), and M1 piece of (1.5). No M2 cancellation theorem used. |
| `rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md` | Accepted frequency-profile antecedent; equations (2.1)--(2.3), (5.1)--(5.2) fix the normalized-BV \(\eta_L\), height truncation and shell coefficient. |
| `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/dyadic_profile_certificate.md` | Earlier accepted profile construction inspected to trace \(W\). |
| `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md` | Direct antecedent of the top transform; its section 2 gives the \(2/3\) plateau profile used there. The earlier construction has a \(3/4\) plateau; these are distinct allowable profiles and are not silently identified. The present norm proof uses the fixed top-transform profile and its bounded variation, not a plateau substitution. |

Accepted graph inputs checked: `M9-M1-top-endpoint-transform`, `M9-M1-frequency-phase-diagram-R10`, `H4-Phi-regularity`, `M9-M2-dyadic-weight-nondegeneracy`, `M9-M1-hard-top-t1-comparable-factor-exchange-sector`, `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`, and the still-open high-radical small-\(t\) residual owner. Shared files, older candidates, synthesis files, and other new reports were not edited. No new external source card is needed because no external result is imported.

## 7. Recommended state effect

**Retain all analytic obligations and exponent ledgers unchanged.** Archive this report as a complete-source coefficient/norm interface with a proved coarse-kernel norm obstruction, not as a refutation of the actual target.

The conductor may use (200.N11) as the required quantitative import checklist and (200.N16) as a separate conditional scalar interface. Do not promote a complete literal mixed-norm claim from the smooth-core calculation, and do not treat the auxiliary scalar target as equivalent to the frozen residual correlation target. No successor round is launched by this report.
