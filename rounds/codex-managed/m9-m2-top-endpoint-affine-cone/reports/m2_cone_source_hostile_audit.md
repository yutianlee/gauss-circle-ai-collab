# Round 74 hostile/source audit: the M2 top-endpoint affine cone

Task: `m2_cone_source_hostile_audit`  
Role: independent selected-context source auditor  
Verdict: sharp no-go for the proposed closure; one source-backed but already dominated bilinear estimate

## 1. Result

The frozen estimate
\[
 T_{\mathrm{end},L}
 =\sum_{\substack{h\asymp L\\h\ \mathrm{odd}}}
   \sum_{\lceil h/4\rceil\le m\le h}
   \chi _4(h)a(h,m)e(\sqrt{Xhm})
 \ll_\varepsilon L^{3/2}X^\varepsilon
 \tag{1.1}
\]
is **not proved** for the open intermediate range \(1\ll L\ll H\). The normalization, character algebra, shear, product regrouping, hard affine edge, endpoint transition, perfect-power controls, and the formal two-dimensional Poisson route all survive audit. The obstruction is precisely the missing signed off-diagonal cancellation.

The quarter-shift two-dimensional Poisson calculation is degenerate, not a nondegenerate two-variable stationary-phase problem: its stationary equations give
\[
 (4u-\rho)v=X,\qquad \rho\in\{1,3\},
 \tag{1.2}
\]
and the Hessian has determinant zero. After preserving the actual symbol, its main term is a high-leg-character, fixed-centre near-product discrepancy
\[
 D_{L,X}=\sum_{\substack{j\asymp J\\j\ \mathrm{odd}}}
 \sum_{l\asymp J}\chi _4(j)B_{L,X}(j,l)
 K\!\left(\frac{L(X-jl)}{4l}\right),
 \qquad J=\sqrt X,
 \tag{1.3}
\]
with \(|X-jl|\ll J/L\), ratio cutoffs and endpoint factors contained in \(B_{L,X}\), and target \(D_{L,X}\ll J^{1/2}X^\varepsilon\). The unweighted display obtained by putting \(B=1\) is only shorthand and is not the transformed frozen sum.

Poisson summation in the character-bearing variable \(j\) transfers \(\chi _4\) to modes \(|h|\asymp L\) and reconstructs the original M2 reciprocal block, with the adjoint actual weight. This is an exact self-return and supplies no inequality. Poisson summation in the other variable gives the genuinely different sufficient problem
\[
 D_{L,X}=L^{-1}\sum_{|k|\ll L}S_k+\text{target-safe errors},
 \qquad
 S_k=\sum_{\substack{j\asymp J\\j\ \mathrm{odd}}}
 \chi _4(j)b_{j,k}e(-kX/j),
 \tag{1.4}
\]
for which Cauchy would close (1.1) if
\[
 \sum_{|k|\ll L}|S_k|^2\ll LJX^\varepsilon.
 \tag{1.5}
\]
No audited reciprocal large-sieve, exponent-pair, shifted-divisor, Kloosterman, or spectral theorem has the hypotheses needed for (1.5), or gives an outside-Cauchy estimate for (1.3) with the fixed centre and actual hard-edge symbol.

Kowalski--Robert--Wu Proposition 5 does apply after lawful separation of the actual bounded-variation angular cutoff. It gives
\[
 T_{\mathrm{end},L}
 \ll X^\varepsilon\bigl(
 J^{1/8}L^{13/8}+L^{3/2}+L^{7/4}+J^{-1/2}L^{3/2}
 \bigr).
 \tag{1.6}
\]
This is polynomially better than the trivial \(L^2\) only when \(L>J^{1/3}\) (a uniform power saving when \(L\ge J^{1/3+\delta}\)); it never reaches \(L^{3/2}\). Moreover, exactly on that nontrivial range the already accepted terminal-to-intermediate estimate
\[
 T_{\mathrm{end},L}\ll J^{1/2}L^{1/2}X^\varepsilon
 \tag{1.7}
\]
is no larger: the leading term in (1.6), divided by (1.7), is \((L^3/J)^{3/8}\ge1\). Thus (1.6) supplies no new accepted range or bound.

## 2. Exact statement and hypotheses

Assume \(X\) is large, put
\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,
\]
and let \(L\) be a dyadic scale with \(1\le L\le H\). The fixed weights are those of the derivation packet: \(\eta_L\) is the dyadic \(h\)-cutoff, \(\Phi(h/(H+1))\) is the inherited frequency cutoff, and
\[
 a(h,m)=\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 \left(\frac{L^2}{hm}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xh}{4m}}\right),
 \tag{2.1}
\]
where \(W(u)=0\) for \(u\le1/2\), \(W(1)=1\), and \(W(u)=1\) for \(2/3\le u\le1\). The lower line \(4m=h\) is therefore a genuine nonzero hard edge. All claims below retain the odd restriction, the moving bounds \(\lceil h/4\rceil\le m\le h\), and (2.1).

The audited structural statement is:

1. The exact one-sided transform contributes the positive stationary block
   \[
   -\frac2\pi e(1/8)X^{1/4}L^{-3/2}T_{\mathrm{end},L};
   \tag{2.2}
   \]
   the negative block is its conjugate and the full contribution is twice its real part. Hence (1.1), with the external factor counted once, is exactly the required \(O(X^{1/4+\varepsilon})\) block estimate.
2. Bounded \(L\) is trivial and the terminal scale \(L\asymp H\asymp J^{1/2}\) follows from (1.7). Nothing audited proves a strict additional target range.
3. The shear \(r=4m-h\), the product coefficient \(A_L(n)\), the dual incidence (1.3), and the reciprocal energy (1.5) are valid reformulations or sufficient conditions only with their actual weights and cutoffs. Replacing them by an unsigned count, a complete divisor coefficient, arbitrary coefficients, or an independently smoothed edge is not licensed.
4. Perfect-square and perfect-fourth-power values of \(X\) obey the available diagonal capacity bounds; they do not disprove (1.1), but they rule out arguments based on generic separation alone.
5. The primary-source conclusion is negative for the target. Formula (1.6) is a valid weaker import, subject to the project source-card rule stated in Section 7.

## 3. Proof, source mapping, and hostile derivation

**External normalization and the character.** The inherited exact transform is
\[
 \sum_{d\le y}W(d/y)e(hX/(4d))
 =\frac{e(hX/(4y))}{1-e(hX/(4y^2))}
 +\frac{e(1/8)}2(hX)^{1/4}
  \sum_{m=\lceil h/4\rceil}^{h}
  W\!\left(\sqrt{\frac{q_Xh}{4m}}\right)m^{-3/4}e(\sqrt{Xhm})
 +O_W(\log(2+h)).
 \tag{3.1}
\]
Because
\[
 L^{-3/2}\left(\frac{L^2}{hm}\right)^{3/4}=(hm)^{-3/4},
 \tag{3.2}
\]
the outside \(L^{-3/2}\) in (2.2) is neither missing nor to be applied twice. Also
\[
 e(h/4)-e(3h/4)=2i\chi _4(h)\quad(h\ \mathrm{odd}),
 \tag{3.3}
\]
while both sides vanish for even \(h\) under the primitive mod-four convention. Thus the signed cone, not its unsigned analogue, is the exact object.

**Hard edge and endpoint transition.** Put \(r=4m-h\). For odd \(h\), the equality \(r=0\) contains no lattice point; the first admissible row has \(r=1\) or \(3\), where the weight is already at the nonzero lower edge. Any fixed number of such rows has \(O(L)\) terms of bounded amplitude and is absolutely \(O(L)\), below (1.1). At \(m=h\), \(q_X-1=O(J^{-1})\) and \((q_X-1)h<1\) for \(h\le H\); only the endpoint row can be affected, and the flat vanishing of \(W\) at \(1/2\) makes it negligible (an \(O(L)\) bound already suffices). In scaled angular coordinates the stationary width at an edge is
\[
 L(JL)^{-1/2}=\sqrt{L/J}<1
 \tag{3.4}
\]
throughout \(L\le J^{1/2}\). Hence the half-Fresnel/entry transition occupies a sub-lattice-width region and is covered by exact extraction of the first rows. This permits smoothing the interior, but it does not permit replacing the original hard edge without that extraction.

**Shear and product multiplicity.** For odd \(h,r\),
\[
 1_{r\equiv-h\ (4)}=\frac{1-\chi _4(h)\chi _4(r)}2,
 \qquad
 \chi _4(h)1_{r\equiv-h\ (4)}
 =\frac{\chi _4(h)-\chi _4(r)}2.
 \tag{3.5}
\]
The transformed range is \(1\le r\le3h\), \(m=(h+r)/4\), and the phase is
\[
 e\!\left(\frac{\sqrt X}{2}\sqrt{h(h+r)}\right).
 \tag{3.6}
\]
Both character terms in (3.5), the original \(h\)-cutoff, and \(r\le3h\) must remain. The phase is not symmetric in \(h,r\). For fixed \(r\), its real second derivative is
\[
 F_r''(h)=-\frac{\sqrt X\,r^2}{8\{h(h+r)\}^{3/2}},
 \tag{3.7}
\]
but a large real curvature is not a lower bound for distance from integers and does not control aliases.

Grouping by \(n=hm\) gives
\[
 T_{\mathrm{end},L}=\sum_{n\asymp L^2}A_L(n)e(\sqrt{Xn}),
 \quad
 A_L(n)=\sum_{\substack{h\mid n,\ h\asymp L,\ h\ \mathrm{odd}\\
              \lceil h/4\rceil\le n/h\le h}}
       \chi _4(h)a(h,n/h).
 \tag{3.8}
\]
This is a moving, truncated divisor coefficient, not \(r_2(n)/4\), not multiplicative, and not the full divisor function. Nevertheless
\[
 |A_L(n)|\ll d(n),\qquad
 \sum_{n\asymp L^2}|A_L(n)|^2\ll L^2X^\varepsilon.
 \tag{3.9}
\]
Plain Cauchy therefore gives only \(L^2X^\varepsilon\). If instead Cauchy is taken outside the \(h\)-sum, the diagonal in the expanded \(m,m'\) correlation is \(O(L^3)\), exactly the square of the target. A sufficient off-diagonal statement is that the correlation before the outside factor be \(O(L^2X^\varepsilon)\). This is not an equivalent signed reformulation: outside Cauchy deletes \(\chi _4(h)\), so the missing estimate must exploit structure still present in the coupled phase and actual symbol.

**Two-dimensional quarter-shift Poisson and self-return.** Expand (3.3) with \(\rho=1,3\). For the continuous phase
\[
 \Psi_{\rho,u,v}(x,z)=J\sqrt{xz}+\frac\rho4x-ux-vz,
 \tag{3.10}
\]
stationarity gives
\[
 u-\rho/4=\frac J2\sqrt{z/x},\qquad
 v=\frac J2\sqrt{x/z},\qquad
 (4u-\rho)v=J^2=X.
 \tag{3.11}
\]
But
\[
 \det \operatorname{Hess}_{x,z}(J\sqrt{xz})=0
 \tag{3.12}
\]
identically: the Hessian has rank one because \(\sqrt{xz}\) is homogeneous of degree one. A two-dimensional nondegenerate stationary-phase theorem is therefore inapplicable. Integration in the nonflat direction and Fourier transformation in the radial direction yield (1.3), localized to
\[
 |X-jl|\ll J/L.
 \tag{3.13}
\]
This is a signed floor-character/near-product discrepancy at the prescribed centre \(X\), not a standard shifted-divisor average.

For fixed \(l\), the kernel in (1.3) has \(j\)-width \(1/L\). Poisson summation in \(j\) consequently has modes of length \(L\); the mod-four Fourier transform transfers \(\chi _4(j)\) to odd short modes and gives phases \(e(\pm hX/(4l))\). With the transformed amplitude this is the original M2 reciprocal block. It is an adjoint Poisson identity before Cauchy, and is therefore distinct from a long-character reciprocal-sum large sieve: it supplies neither frequency spacing nor a mean-square gain. Poisson in the uncharactered \(l\)-leg gives (1.4), and
\[
 |D_{L,X}|^2\ll L^{-1}\sum_{|k|\ll L}|S_k|^2
 \tag{3.14}
\]
shows that (1.5) is sufficient. Its diagonal is exactly of size \(LJ\). The off-diagonal contains
\[
 \sum_{j\ne j'}\chi _4(j)\chi _4(j')
 b_{j,k}\overline{b_{j',k}}
 \sum_{|k|\ll L}e\!\left(kX(1/j'-1/j)\right),
 \tag{3.15}
\]
so discarding the signs or the moving \(k\)-dependent symbol loses the only possible extra cancellation.

**Perfect powers and aliases.** If \(X\) is a square, exact original resonances \(Xhm=\square\) reduce in the worst case to \(h=da^2,m=db^2\) with a common squarefree kernel. Their number is
\[
 \ll\sum_{d\ll L}\frac Ld\ll L\log(2L),
 \tag{3.16}
\]
and hence is below \(L^{3/2}\); perfect fourth powers are a subset of this worst case. In the dual picture exact aliases \(jl=X\) have at most \(d(X)\ll X^\varepsilon\) representations. If \(X=R^4\), then \(J=R^2\) and the central alias \(j=l=J\) occurs when parity permits. Along \(j=J+s,l=J-s\),
\[
 X-jl=s^2,
 \tag{3.17}
\]
so the window (3.13) admits only \(|s|\ll\sqrt{J/L}\le J^{1/2}\) such points. They fit the target even by absolute counting. Perfect-fourth resonance thus neither falsifies the target nor proves the required cancellation.

**Exact primary-source mapping.**

- Kowalski--Robert--Wu, Proposition 5 in [*Small gaps in coefficients of L-functions and B-free numbers in short intervals*, Rev. Mat. Iberoamericana 23 (2007), 281--326](https://ems.press/content/serial-article-files/38194), defines
  \[
  S(M,N)=\sum_{m\sim M}\sum_{n\sim N}\varphi_m\psi_n
  e\!\left(\mathcal X\frac{m^\alpha n^\beta}{M^\alpha N^\beta}\right),
  \]
  under \(\mathcal X>0\), \(M,N\ge1\), \(|\varphi_m|,|\psi_n|\le1\), and fixed real \(\alpha,\beta\notin\{0,1\}\). For every \(\varepsilon>0\), it proves
  \[
  S(M,N)\ll_{\alpha,\beta,\varepsilon}
  \bigl((\mathcal XM^6N^6)^{1/8}+M^{1/2}N+MN^{3/4}
       +\mathcal X^{-1/2}MN\bigr)(MN)^\varepsilon.
  \tag{3.18}
  \]
  For the frozen sum, extract the \(O(L)\) first edge rows. The remaining ratio factor, including \(1_{m\ge h/4}\), is a compactly supported bounded-variation function of \(\log(m/h)\). A monotone smoothing inside the lattice gap followed by truncated Mellin/Fourier inversion separates it into \((m/h)^{it}=m^{it}h^{-it}\), with total coefficient norm \(O(\log^C L)\) and negligible tail. The factors \(\chi _4(h)\eta_L(h)\Phi(h/(H+1))h^{-3/4-it}\) and \(m^{-3/4+it}\), after harmless normalization on \(h,m\asymp L\), are separate sequences bounded by one. The upper row is handled as above. Thus (3.18) applies with
  \[
  M\asymp N\asymp L,\qquad \alpha=\beta=\tfrac12,\qquad
  \mathcal X=JL,
  \]
  and gives exactly (1.6), up to \(X^\varepsilon\). It improves \(L^2\) only for \(L>J^{1/3}\), while its first term can never be \(O(L^{3/2})\) for unbounded \(JL\). On its nontrivial range, \((L^3/J)^{3/8}\ge1\) proves that (1.7) is at least as strong. This is a lawful but non-new polynomial estimate.
- Robert--Sargos, Theorem 2 in [*Three-dimensional exponential sums with monomials*, J. reine angew. Math. 591 (2006), 1--20](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf), assumes fixed real \(\alpha\ne0,1\) and counts \(m_i\asymp M\) satisfying
  \[
  |m_1^\alpha+m_2^\alpha-m_3^\alpha-m_4^\alpha|\le\delta M^\alpha.
  \]
  It proves \(\ll_\varepsilon M^{2+\varepsilon}+\delta M^{4+\varepsilon}\). At \(\alpha=1/2\) this is the root-spacing input behind the double-large-sieve step in (3.18); it counts collisions but gives no fixed-\(X\), coefficient-weighted off-diagonal estimate beyond (1.6).
- The classical large sieve of Bombieri, [*On the large sieve*, Mathematika 12 (1965), 201--225](https://doi.org/10.1112/S0025579300005313), requires separated points and gives a constant of the shape \(L+\delta^{-1}\). Here the points \(X/j\pmod1\) are not uniformly separated. For \(X=J^2\),
  \[
  \frac{X}{J+s}=J-s+\frac{s^2}{J+s},\qquad
  \frac{X}{J-s}=J+s+\frac{s^2}{J-s},
  \]
  so the two fractional parts differ by \(2s^3/(J^2-s^2)\), already \(\asymp J^{-2}\) for \(s=1\). The spacing constant is therefore far too large, and the theorem ignores the actual character-weight correlation.
- Huxley--Watt, [*Exponential sums and the Riemann zeta function*, Proc. London Math. Soc. (3) 57 (1988), 1--24](https://doi.org/10.1112/plms/s3-57.1.1), proves under its smoothness and derivative nonvanishing hypotheses
  \[
  \sum_{M\le m<2M}e(TF(m/M))\ll M^{1/2}T^{9/56}\log T,
  \qquad T\ge M.
  \]
  Splitting \(\chi _4\) into residue classes and using partial summation makes it applicable to a smooth version of one row of \(S_k\), with \(M=J\) and \(T\asymp kJ\). Even optimistically this gives
  \[
  \sum_{1\le |k|\ll L}|S_k|^2
  \ll LJ\,(LJ)^{9/28}X^\varepsilon,
  \tag{3.19}
  \]
  not (1.5). The positive conductor loss is fatal.
- Ivi\'c, [*On the mean square of the divisor function in short intervals*, J. Th\'eorie des Nombres de Bordeaux 21 (2009), 251--261](https://doi.org/10.5802/jtnb.669), estimates integrals of \((\Delta_k(x+h)-\Delta_k(x))^2\) over \(X\le x\le2X\), with the full \(d_k\)-coefficients. It neither gives a pointwise prescribed-centre bound nor retains the mod-four sign and moving angular symbol.
- Bettin--Chandee, [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/abs/1502.00769), treats trilinear sums with phases \(e(\vartheta a\overline m/n)\), coprimality, modular inverses, and \(\ell^2\)-controlled coefficient sequences. The phase in (1.4) is the ordinary real reciprocal \(-kX/j\), not a Kloosterman fraction. Forcing a singleton-variable encoding introduces the theorem's conductor loss and does not yield (1.5).
- Deshouillers--Iwaniec, [*Kloosterman sums and Fourier coefficients of cusp forms*, Invent. Math. 70 (1982), 219--288](https://doi.org/10.1007/BF01390728), obtains spectral large-sieve bounds after completing Kloosterman sums and averaging the relevant moduli/spectral data. The fixed product band (1.3) has neither complete Kloosterman sums nor the required modulus or spectral average. Level four is not the obstruction; the absent averaging and moving hard-edge symbol are. Voronoi/Kuznetsov completion here is a transformation, not a pointwise estimate, and the phase-matched transform returns to the reciprocal block.

Finally, no theorem uniform over arbitrary \(b_{j,k}\) can prove (1.5): for one selected \(k_0\), take \(b_{j,k_0}=\chi _4(j)e(k_0X/j)\) on \(j\asymp J\). Then \(|S_{k_0}|\asymp J\), so the energy is \(\gg J^2\), whereas \(LJ\le J^{3/2}\). Any successful result must use the exact coupled symbol, not merely coefficient bounds.

## 4. First doubtful or unproved step

The first unproved step is not normalization, endpoint control, the shear, product multiplicity, or the Poisson algebra. It is the first claimed saving beyond diagonal capacity:
\[
 \sum_{|k|\ll L}\left|
   \sum_{\substack{j\asymp J\\j\ \mathrm{odd}}}
   \chi _4(j)b_{j,k}e(-kX/j)
 \right|^2
 \stackrel{?}{\ll}LJX^\varepsilon,
 \tag{4.1}
\]
or an equally strong outside-Cauchy estimate directly for (1.3). Expanding (4.1) exposes highly clustered reciprocal points, and applying Poisson in the leg that still carries \(\chi _4\) simply returns to the original M2 block. No audited source controls the actual \(j,k\)-coupled amplitude at this fixed centre with no averaging in \(X\).

A secondary rigor seam is that the simple display with a single fixed \(K\) must never be substituted for the finite separated sum of actual kernels without recording the hard-edge extraction, the ratio symbol \(B_{L,X}\), and the endpoint error. That seam is target-safe and repairable; it is not the source of the missing power saving.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| External normalization | **Pass.** Equation (3.2) reproduces the external \(L^{-3/2}\) exactly once; the full block is twice the real part of (2.2). |
| Odd character | **Pass.** Equation (3.3) gives \(2i\chi _4(h)\) on odd \(h\) and zero on even \(h\). |
| Hard lower edge | **Pass only with extraction.** The equality row is absent for odd \(h\), but the first nonzero rows are real and total \(O(L)\); smoothing them away silently is invalid. |
| Flat upper edge and \(q_X\ne1\) | **Pass.** Only an endpoint row is exposed and is target-safe; flatness at \(1/2\) makes it smaller. |
| All \(L\)-slices | **Open in the middle.** Bounded \(L\) is trivial, \(L\asymp H\) follows from (1.7), and no strict new target subrange is obtained. KRW is nontrivial only for \(L>J^{1/3}\), where (1.7) is already no larger. |
| Product multiplicity | **Pass as capacity, not proof.** Equation (3.9) gives the correct \(L^2\) coefficient second moment but only an \(L^2\) sum bound. |
| Shear projector | **Pass.** Both characters in (3.5), the congruence, \(r\le3h\), and cutoff ownership are retained. |
| Exact square/fourth power | **Pass.** Original exact resonances are \(O(L\log L)\); exact dual aliases are divisor-bounded; the fourth-power anti-diagonal has \(O(\sqrt{J/L})\) points. |
| Diagonal and near diagonal | **Pass/Fail.** The diagonal is exactly target-sized; the signed off-diagonal estimate is unproved. |
| Stationary aliases and self-return | **Pass as obstruction.** The 2D Hessian is rank one, the dual window is (3.13), and Poisson in the character leg reconstructs M2. |
| Source applicability | **Fail for target.** KRW gives only (1.6); every reciprocal, divisor, exponent-pair, and spectral source misses a stated hypothesis or loses a positive power. |
| Proves-too-much adversarial test | **Pass as rejection.** Arbitrary bounded coefficients make one \(S_k\) of size \(J\); an actual-symbol theorem is indispensable. |
| Downstream scope | **Pass.** No conclusion is drawn for all of M2, M9, or the global exponent. |

## 6. Dependencies and exact artifacts used

The repository evidence used, and only the selected-context evidence used, was:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/briefs/m2_cone_source_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/derivation_packet.md`;
- `rounds/codex-managed/m9-top-endpoint-transform/synthesis.md`;
- `rounds/codex-managed/m9-top-endpoint-transform/reports/endpoint_transform_hostile_audit.md`;
- `rounds/codex-managed/m9-combined-top-cones/reports/combined_cone_hostile_audit.md`.

No sibling Round-74 report, shared synthesis for this round, proof draft, validation matrix, or source card was used. The primary sources used are the seven directly linked papers in Section 3: Kowalski--Robert--Wu Proposition 5; Robert--Sargos Theorem 2; Bombieri's large sieve; Huxley--Watt's smooth one-dimensional exponential-sum theorem; Ivi\'c's centre-averaged divisor mean square; Bettin--Chandee's Kloosterman-fraction form; and Deshouillers--Iwaniec's complete Kloosterman/spectral framework.

The inherited mathematical dependencies are only the already proved exact top-endpoint transform and its target-safe boundary/error bookkeeping. The estimate (1.7) is used solely for the source-comparison control supplied by the conductor; it closes only the terminal scale at target strength.

## 7. Recommended state effect

**Retain** `M9-M2-top-endpoint-transform` as proved and **retain** `M9-M2-top-endpoint-signed-cone`, M9-M2, M9, and the global target as open. Do not promote (1.1), (1.3), or (1.5).

The narrowest lawful graph effect is to record a route-specific obstruction/rejected claim:

> Nondegenerate two-dimensional Poisson, a standard reciprocal large sieve, or an off-the-shelf shifted-divisor/Kloosterman/spectral theorem closes the M2 top-endpoint cone.

Reason: the Poisson Hessian is rank one; the high-character transform is an exact self-return; the alternative route requires the actual-symbol fixed-centre energy (4.1); and none of the audited primary theorems supplies it.

Formula (1.6) may be retained as source-backed diagnostic evidence, but it gives no new accepted range because it is nontrivial only where (1.7) is already at least as strong. This report alone is **not sufficient** for a `proved_external_dependency` node. Protocol requires a completed source card with the primary PDF locally preserved, hashed, rendered, and its exact pages, notation, constants, and hypotheses checked. No such card was created in this task, and no external-dependency promotion is warranted for a dominated estimate. The sharp state recommendation is therefore **no target promotion; add only the self-return/source-nonapplicability obstruction if the conductor chooses to patch it**.
