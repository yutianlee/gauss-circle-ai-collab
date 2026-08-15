# 1. Result

**No-go result (certificate failure, not a disproof of the ultimate complement estimate).**  The frozen data do permit an exact finite nonnegative one-count repair of the ratio partition.  They do **not** permit the repaired middle package to be identified literally with the accepted Round-41 cells, and they do not state the global signed-section inequalities needed by the direct positive-line radial-BV route on either repaired nonsaddle package.  The partition obstruction is already visible at the stationary ratio: the proposed normalized partition puts positive `infinity` weight at \(t=|\alpha|/\lambda=1\).  Removing that weight from the nonsaddle package necessarily changes the aggregate middle cutoff from the only aggregate cutoff specified in the packet.  Round 41 supplies no literal cutoff formula with which the changed aggregate could be compared.

The direct nonsaddle route does **not** require importing the Round-41 \(\lambda^{-2}\) normalized norm, and no stationary numerator should be multiplied into a nonsaddle cell.  A fixed \(\chi _0'\) collar is compact in \(\alpha\) and is not itself an obstruction.  The exact missing step is instead a global, after-signed-Cauchy estimate for the value, the x derivative, the outer boundary, and the moving traces.  The values and ranges needed to sum the untouched raw \(h,q,D_j,x\) coefficient are also absent.  Hence the requested \(O(X^{1/4+\varepsilon})\) conclusion cannot be certified from the authorized artifacts.

# 2. Exact statement and hypotheses

Let \(\lambda=\pi q\sqrt{Xx}/D_j>0\), \(\alpha=L+\beta\), and \(t=|\alpha|/\lambda\).  On either sign branch the only authorized phase information is
\[
 \Psi'(L)=\log t,\qquad \Psi''(L)=\frac1\alpha.
\]
The complement multiplier is \(1-\chi _0(\alpha)\), with the signed-origin smoothing performed wholly where this multiplier vanishes.  The exact terminal is (46.1)--(46.3), and the singular \(j=0\) share must first be converted into its signed Cauchy/Plemelj section.  Round 41 may be invoked only if a localized cell is literally one of its signed saddle/entry/exit cells.

The no-go claim is: under precisely these hypotheses, (i) a finite nonnegative smooth ratio partition with repaired supports exists, but (ii) neither literal Round-41 reuse nor a target-sized estimate for the remaining cells follows.  In particular, no unstated bound on \(R_\alpha\), no unstated endpoint geometry, no unstated coefficient-sum lemma, and no generalized compact-cutoff theorem is assumed.

# 3. Proof or derivation

At \(t=1\), the prescribed supports give \(b_0(1)=0\), \(b_1(1)=1\), and \(b_\infty(1)=1\).  Consequently
\[
 (\widetilde\vartheta _0,\widetilde\vartheta _1,
   \widetilde\vartheta _\infty)(1)=(0,1/2,1/2).
\]
Thus the raw \(k=\infty\) cell contains \(t=1\), where \(\Psi'=0\), and is not a nonsaddle cell.  This is a literal failure of the unrepaired proposal.

The failure is repairable at the level of a one-count partition.  Choose smooth functions \(f,g:[0,\infty)\to[0,1]\) with
\[
 f=1\ (t\le2/3),\quad f=0\ (t\ge3/4),
 \qquad
 g=0\ (t\le4/3),\quad g=1\ (t\ge3/2),
\]
and set
\[
 c_0=f,\qquad c_1=1-f-g,\qquad c_\infty=g.
\]
The transition supports are disjoint, so \(c_k\ge0\), \(\sum c_k=1\),
\[
 \operatorname{supp}c_0\subset\{t\le3/4\},\quad
 \operatorname{supp}c_1\subset\{2/3<t<3/2\},\quad
 \operatorname{supp}c_\infty\subset\{t\ge4/3\}.
\]
This can be viewed as a finite nonnegative redistribution of the original weights: the nine pieces \(c_k\widetilde\vartheta _\ell\) preserve every input weight on summing over \(k\), and give \(c_k\) on summing over \(\ell\).  Let \(\sigma_++\sigma_-=1\) be a fixed nonnegative smooth signed partition whose transition is contained where \(1-\chi _0=0\).  Then
\[
 \eta_{\pm,k}=(1-\chi _0(\alpha))\sigma_\pm(\alpha)c_k(t)
\]
is smooth, nonnegative, finite, and sums pointwise to \(1-\chi _0\).  It has the required fixed gap \(|\Psi'|\ge\log(4/3)\) on the two nonsaddle aggregates.

This repair also proves the cutoff mismatch.  At \(t=1\), any repaired nonsaddle cutoffs must both vanish, so their missing total weight must be assigned to the middle package.  The repaired middle aggregate therefore equals one at \(t=1\), whereas the packet's specified refined \(k=1\) pieces are required to add back to \(\widetilde\vartheta _1(1)=1/2\).  Round-41 synthesis states only a signed fixed-ratio cell \(|\alpha|\asymp\lambda\); it gives no cutoff functions, entry/exit masks, or equality showing that the additional half-weight is an accepted cell.  Exact partition and literal reuse therefore cannot both be inferred from the frozen statements.

The correct nonsaddle test is the direct positive-line radial-BV test.  After forming the signed Cauchy section when necessary, write a localized section as
\[
 I_k(x)=\int e^{i\Psi(L,x)}\eta_k(L,x)S(L,x)\,dL,
\]
where \(S\) is the complete signed diagonal/off-diagonal section or the complete smooth \(\nu\)-section, with \(R_\alpha\) and all exact factors retained.  With vanishing genuine endpoints, one integration by parts gives
\[
 I_k=-\int e^{i\Psi}
 \left\{\frac{(\eta_kS)'}{i\Psi'}+
 i\frac{\eta_kS\Psi''}{(\Psi')^2}\right\}\,dL. \tag{A}
\]
On the repaired nonsaddle supports \(|\Psi'|\ge\delta:=\log(4/3)\).  On moving ratio collars,
\[
 \partial_Lt=\frac{\operatorname{sgn}\alpha}{\lambda},
 \qquad \partial_Lc_k=O(\lambda^{-1}),
 \qquad |\alpha|\asymp\lambda,
\]
and hence \(|\alpha\,\partial_Lc_k|=O(1)\).  The fixed transition of \(\chi _0\) has \(|\alpha|=O(1)\), so its value and derivative are a genuinely compact direct term; no \(\lambda^{-1}\) gain is demanded there.

The exact x phase retained in (46.1)--(46.2) makes x differentiation of the section produce a term with at most one power of the large height (the compact proof's multiplier is \(((L+\nu)/2+\beta)\)).  Schematically writing its post-section leading part as \(\alpha S\), one application of (A) to that term gives
\[
 \partial_L(\alpha S)=S+\alpha\partial_LS,
 \qquad \alpha\Psi''=1. \tag{A1}
\]
Thus the direct route would close if, after forming the singular section before absolute values, one had a coefficient-summable global estimate of the form
\[
 \begin{aligned}
 &\int_{\mathrm{ns}}
 \left(|\partial_LS|+\frac{|S|}{1+|\alpha|}
       +|S|+|\alpha\partial_LS|\right)dL\\
 &\quad+\text{all moving-section traces}
 +\text{the corresponding lower-order x-derivative terms}
 \ \ll\ P_X, \tag{A2}
 \end{aligned}
\]
together with the boundary limits required by (A).  The grouping in (A2), rather than any particular absolute majorant of the unintegrated Cauchy kernel, is essential.  It is compatible with a favorable \(\kappa=3/4+(a+b)/2<1\) global asymptotic, but no such global asymptotic or inequality is stated in the frozen artifacts.  Round 41 supplies local fixed-ratio norms after its own normalization; Round 45 supplies the particular compact \(\chi _0\) terminal.  Neither states (A2) on the full inner and unbounded outer nonsaddle sectors.

The signed diagonal does not remove the trace issue.  If
\[
 C(L)=Z(L)\{\Log D(L,q(L))-\Log D(L,p(L))\},
 \qquad Z(L)=H(L,L)/A(L),
\]
then, before absolute values,
\[
 \begin{aligned}
 C'(L)={}&Z'(L)\{\Log D(L,q)-\Log D(L,p)\}\\
 &-\frac{iZ(L)(1+q'(L))}{2D(L,q(L))}
 +\frac{iZ(L)(1+p'(L))}{2D(L,p(L))},
 \end{aligned} \tag{B}
\]
and localization adds \((\eta C)'=\eta'C+\eta C'\).  Likewise an off-diagonal finite section has the exact traces
\[
 \frac d{dL}\int_{p(L)}^{q(L)}K(L,\nu)\,d\nu
 =\int_{p(L)}^{q(L)}K_L(L,\nu)\,d\nu
 +q'K(L,q)-p'K(L,p). \tag{C}
\]
Round 41 controls (B)--(C) on its own fixed-ratio cells.  The frozen nonsaddle packet gives neither the endpoint functions and speeds nor norms for these traces off those cells.  On the unbounded outer aggregate, (A) and its x-differentiated analogue also require
\[
 \frac{\eta_kS}{\Psi'}\longrightarrow0,
 \qquad
 \frac{\eta_k\alpha S}{\Psi'}\longrightarrow0
 \quad (|L|\to\infty). \tag{C1}
\]
The statement \(W_0=1\) makes it especially important not to borrow decay from a smooth spatial profile, while no global outer estimate for \(R_\alpha\) or the complete signed kernel is supplied.  Equations (A2) and (C1) are the exact first failed global signed-section inequalities.

There is also a radial cutoff term that cannot be counted as an inverse power of \(\lambda\).  At fixed \(q,j\),
\[
 x\partial_x\lambda=\frac\lambda2,
 \qquad x\partial_xt=-\frac t2,
 \qquad x\partial_xc_k(t)=-\frac t2c_k'(t)=O(1) \tag{D}
\]
on a ratio collar.  This term must accompany the complete x-phase derivative and all radial endpoint traces.

Finally, the raw coefficient, with the one external \(X^{1/4}\) factor and with no stationary numerator or artificial \(\lambda^{-m}\) gain inserted, has the exact magnitude
\[
 X^{1/4}|\mathfrak a_{j,h,q,x}|=
 \pi2^{-a}X^{3/4-a/2}h^{-r}q^{-p}D_j^a(H_j+1)^b
 x^{-3/2-b/2}. \tag{E}
\]
To obtain the target by the direct route, (A2) and its radial counterpart must be normalized so that the \(h^{-r}q^{-p}\) sums, the \(j\)-scale sum, and the x/radial BV norm reduce (E) to \(O(X^{1/4+\varepsilon})\).  The packet specifies neither \(p,r,a,b\), nor the \(h,q,j,x\) ranges and radial measure, nor the size relations for \(D_j,H_j\), nor a global bound for \(R_\alpha\).  Thus (E), together with the order-one radial cutoff derivative (D), is the end of the exact available ledger; no convergence or \(X\)-power conclusion follows.

# 4. First doubtful or unproved step

The first failed step is the claimed literal Round-41 cell match after subordinate repair.  Exact nonsaddle separation forces the middle aggregate to take all the mass at \(t=1\), changing its value there from \(1/2\) to \(1\).  No authorized artifact identifies this enlarged cutoff, or the redistributed pieces that make it up, with the accepted saddle/entry/exit masks.  Therefore Round 41 cannot yet be applied, even before any integration-by-parts estimate is attempted.

If that interface were supplied, the first analytic gap would be (A2)--(C1) for the complete signed Cauchy section and smooth shares on the global nonsaddle supports.  The fixed-\(\alpha\) \(\chi _0'\) term is compact and is not the obstruction.

# 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Same positive-line antecedent | **Pass algebraically:** the displayed repaired \(\eta_{\pm,k}\) sum to the same \(1-\chi _0\); no connector or residue is inserted. |
| Finite partition exactness and nonnegativity | **Raw proposal fails, explicit repair passes:** \(\widetilde\vartheta_\infty(1)=1/2\), but the \(c_0,c_1,c_\infty\) repair is finite, smooth, nonnegative, subordinate, and one-count. |
| Literal Round-41 cell match | **Fail:** the repaired middle aggregate differs pointwise from \(\widetilde\vartheta_1\), and Round 41 supplies no literal masks for comparison. |
| Inner nonsaddle sector and fixed collar | **Support passes; global norm missing:** the ratio sector has a fixed phase gap, and \(\chi _0'\) is a harmless fixed compact collar.  The complete after-section estimate (A2), including the one-height x derivative, is not stated. |
| Outer nonsaddle sector | **Not certified:** fixed phase gap holds, but (A2), both limits (C1), and global bounds for \(R_\alpha\) and the complete section are absent; \(W_0=1\) forbids using a fictitious smooth-profile tail. |
| Signed Cauchy before absolute values | **Order respected, norm missing:** (B) is formed signed, but its nonsaddle value, variation, branch-log, and endpoint trace bounds are not provided. |
| Moving traces and cutoff derivatives | **Fail as a bound:** (B)--(D) retain the exact terms; endpoint speeds and off-cell trace norms are unspecified, and the radial cutoff derivative is order one. |
| Coefficient, scale, and radial sum | **Fail:** (E) is the maximal raw ledger with no imported saddle numerator or \(\lambda\)-norm; the exponents, ranges, scale relations, radial measure, and global section normalization needed to sum it are absent. |
| Collision ownership and external factor once | **Bookkeeping statement passes only:** the antecedent says the closed modules remain attached once, and (E) uses one \(X^{1/4}\); this does not repair the missing analytic or summation estimates. |

No numerical, symbolic-experimental, or external-source control was used.

# 6. Dependencies and exact artifacts used

Only the following authorized artifacts were read and used:

1. `rounds/codex-managed/m9-m1-beta-large-alpha-complement-completion/derivation_packet.md`;
2. `rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/synthesis.md`;
3. `rounds/codex-managed/m9-m1-beta-positive-line-localization/synthesis.md`;
4. `rounds/codex-managed/m9-m1-beta-large-alpha-complement-completion/briefs/nonsaddle_hostile_audit.md`.

No reports directory was listed or read, and no graph, proof draft, validation matrix, prior report, web source, or numerical computation was used.

# 7. Recommended state effect

**Retain the positive-line complement certificate as open; do not promote the proposed nonsaddle completion.**  Retain the explicit \(c_0,c_1,c_\infty\) construction only as a candidate exact one-count repair.  Before a later promotion, require: (i) the literal Round-41 cutoff/entry/exit definitions and a proof that the repaired middle pieces are exactly covered; (ii) the direct global inner/outer signed-section inequalities (A2), the two outer limits (C1), and every moving trace, with the fixed \(\chi _0'\) collar treated directly as compact; and (iii) a stated raw coefficient/radial-scale lemma with \(p,r,a,b\), all ranges and measures, \(D_j,H_j\) scale relations, cutoff x-derivatives, floors/stars/equality restrictions/character, and the external operator counted once.  No saddle stationary numerator or pre-normalized \(\lambda^{-2}\) norm should be imported into this nonsaddle ledger.

Recommended report disposition: **revise** the proposed mechanism and make **no accepted-state change** from this audit alone.
