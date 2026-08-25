# 1. Result: exact-repair verdict

**Verdict: REPAIR the three exact points below, then GREEN.**  The mathematical core of the conductor candidate passes every requested gate: the gcd-averaged count, the exact-radical channel, the scoped maximality of \(J=M^{3/4}\), the Appell/cone normalization, the outer \(i/2\), the aggregate Round-140 return, the phase-versus-slope distinction, and the first open scalar are all correct.  No repair changes a claimed exponent, owner, or state effect.

The required repairs are:

1. In (144.C2) and (144.C24), replace the embedded carriage-return corruption in `r\ {\rm odd}` by clean TeX, for example \(r\ \mathrm{odd}\).  The current file contains a literal U+000D at both occurrences.
2. Before (144.C9), replace “the full positive stationary family is” by “the positive-\(j\) principal stationary family is.”  In Section 3.3, likewise say that the principal stationary contribution of the factor \(h^{-1}\int\cdots\) is the displayed saddle term.  Stationary phase has retained remainders; (144.C9) is the principal family, while owner completeness is supplied only by the later aggregate Round-140/141 ledger.
3. Replace the final comparison in (144.C33) by
   
   \[
   \left|\frac{k_m}{2m}-\frac{\sqrt N}{2\sqrt m}\right|
   =\frac{|j_m|}{2m(k_m+\sqrt{Nm})}
   \asymp\frac{|j_m|}{m\sqrt{Nm}}
   \gg\frac1{R^2M^{3/4}}.
   \tag{144.C33 corrected}
   \]
   
   The candidate's literal \(>\) after an \(\asymp\) is not justified with constant \(1\); the invariant conclusion is the displayed \(\gg\)-bound.  Its ratio to \(L_M^{-1}\asymp R/M^{3/4}\) is still \(R^{-3}\), and it still says nothing about arbitrary Farey slopes.

# 2. Exact statement and hypotheses audited

Assume the candidate's large-\(X\) regime

\[
R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
m\in\mathcal I_M\subset[1,M_*],\qquad M_*\asymp R^2,
\]

with disjoint half-open dyadic blocks, bounded smooth \(V_{\rm low}\), \(k_m=\lfloor\sqrt{Nm}+1/2\rfloor\), and \(j_m=k_m^2-Nm\).  Then \(0\le k_m<N\) for all sufficiently large active \(X\).  With the accepted nonzero root estimate

\[
\rho_N(j)\ll_\varepsilon N^\varepsilon\sqrt{(N,j)},
\]

the candidate correctly proves, for every real \(J\ge1\),

\[
\#\{m\in\mathcal I_M:0<|j_m|\le J\}
\ll_\varepsilon JX^\varepsilon.
\tag{A144.1}
\]

If \(N=Du^2\) with \(D\) squarefree, the exact-radical identity is precisely

\[
j_m=0\iff m=Dt^2,
\tag{A144.2}
\]

and its weighted contribution is \(O_{\varepsilon,V}(X^\varepsilon)\).  The nonzero window has block cost

\[
O_{\varepsilon,V}(M^{-3/4}JX^\varepsilon).
\tag{A144.3}
\]

Thus \(J=M^{3/4}\) is target-safe and is the largest fixed power \(M^\beta\) certified by this particular absolute root-count plus divisor-bound ledger.  This yields exactly the survivor (144.C4), but not its estimate.

For the automorphic seam, using the stated \(A_4\), \(\vartheta\), and \(R_{\rm Zw}\) conventions, the exact identities are

\[
A_4(1/2,-3\tau;2\tau)=\frac12+2F(\tau),
\]

\[
\mathcal H=\frac12\widehat A_4(1/2,-3\tau;2\tau)
=F+\frac14+\sum_{a=0}^3\mathcal R_a,
\]

with the four terms (144.C7), and

\[
\mathcal H(\gamma\tau)=\chi_4(d)(c\tau+d)\mathcal H(\tau)
\qquad(\gamma\in\Gamma_0(4)).
\tag{A144.4}
\]

The four-term sum is exactly the single error-kernel cone correction (144.C24), after the two TeX control characters are repaired.  The separate \(1/4\) is compulsory.

# 3. Proof and derivation audit

## 3.1 Gcd average, exact radicals, and maximal window

For fixed nonzero \(j\), the identity \(m=(k_m^2-j)/N\) and \(0\le k_m<N\) inject the relevant \(m\)'s into the residue roots counted by \(\rho_N(j)\).  Summing the accepted root bound without first replacing the gcd by \(|j|\) gives

\[
\begin{aligned}
\sum_{1\le |j|\le J}\sqrt{(N,j)}
&\le 2\sum_{d\mid N}\sqrt d\left\lfloor\frac Jd\right\rfloor\\
&\le 2J\sum_{d\mid N}d^{-1/2}
\ll_\varepsilon JN^\varepsilon.
\end{aligned}
\tag{A144.5}
\]

This proves (144.C3), including squareful \(N\).  The argument is valid for real \(J\ge1\); no hidden \(J<N\) hypothesis is needed for the displayed count.

For \(j_m=0\), unique squarefree decomposition \(N=Du^2\) gives \(k_m^2=Du^2m\), hence \(m=Dt^2\), and conversely \(m=Dt^2\) gives \(k_m=Du t\).  Therefore

\[
\sum_{j_m=0}m^{-3/4}|V_{\rm low}(R^2m/N)C(m)|
\ll X^\varepsilon D^{-3/4}\sum_{t\ge1}t^{-3/2+\varepsilon}
\ll X^\varepsilon.
\]

For \(j_m\ne0\), (A144.1) and \(|C(m)|\ll_\varepsilon X^\varepsilon\) give (A144.3).  If \(J=M^\beta\), the residual absolute price is \(M^{\beta-3/4}X^\varepsilon\).  Hence \(\beta=3/4\) is maximal within this ledger.  The candidate correctly scopes this as a method limit, not a lower bound and not a prohibition on a new signed argument.

## 3.2 Appell completion and cone correction

At the specified torsion section, the \(n\)-th bilateral Appell summand is

\[
\frac{e((4n^2+n)\tau)}{1+e(2n\tau)}.
\]

The \(n=0\) term is \(1/2\), while the \(n=h\) and \(n=-h\) terms agree and each unfolds to the strict odd cone.  This proves (144.C16) and fixes the outer factor \(1/2\), the isotropic constant \(1/4\), and the four \(i/4\) corrections.  Expanding those corrections and sorting the odd difference \(r-4h\) into its four residue classes gives (144.C24).  The combined Gaussian exponent is negative definite in \(h,r\), so the error-kernel sum is absolutely convergent.  The candidate's elliptic return data (144.C25)--(144.C26) then give weight one with scalar character \(\chi_4(d)\) precisely on \(\Gamma_0(4)\).  No extra scalar phase or fifth correction is present.

## 3.3 Outer \(i/2\) and reciprocal return

Period-four character Poisson has Gauss factor \(2i/4=i/2\), so (144.C27) has the correct outer constant.  For positive \(j\), the phase

\[
\phi(u)=\sqrt{Nu}-\frac{ju}{4h}
\]

has \(u_0=4Nh^2/j^2\), negative curvature, and Gaussian unit \(e(-1/8)\).  Moreover

\[
u_0^{-3/4}|\phi''(u_0)|^{-1/2}=2N^{-1/4}.
\]

Including the \(1/h\) preceding the integral and then multiplying by \(i/2\) gives

\[
\frac i2\frac{2N^{-1/4}}h e(-1/8)
=\frac{e(1/8)N^{-1/4}}h,
\tag{A144.6}
\]

so (144.C9) has the exact principal-saddle factor, individual complex direction, and no missing two.  The repair in Section 1 is needed only to prevent (144.C9) from being read as the exact integral without stationary remainders.

The accepted aggregate identity (144.C30), not a termwise comparison of Appell corrections, yields

\[
\mathcal S_{\rm cone}^{+}
=e(1/8)N^{-1/4}\mathcal S_{\rm recip}^{+}
+O_{\varepsilon,V}(X^\varepsilon),
\]

because \(N^{1/4}\asymp R\).  Thus the outer constant exactly inverts the Round-140 factor after the full Round-140/141 boundary, alias, collar, profile, and remainder ledger is reassembled.  The candidate correctly denies correctionwise and rational-branchwise owner inheritance.

## 3.4 Slope comparison and first open scalar

The exact special-slope identity is

\[
\left|\frac{k_m}{2m}-\Phi'(m)\right|
=\frac{|j_m|}{2m(k_m+\sqrt{Nm})}.
\]

On \(m\asymp M\), \(N\asymp R^4\), and the survivor \(|j_m|>M^{3/4}\), this is \(\gg R^{-2}M^{-3/4}\).  Compared with \(L_M^{-1}\asymp RM^{-3/4}\), the scale ratio is \(R^{-3}\).  It controls only the specially induced slope \(k_m/(2m)\), so no arbitrary Farey \(u/q\) is excluded.  After the notation repair in Section 1, the candidate's Round-142 compatibility statement is exact.

# 4. First doubtful or unproved step

After the three exact repairs, the first genuinely unproved step is exactly (144.C34):

\[
\boxed{
\sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
\ll_{\varepsilon,V}X^\varepsilon.}
\tag{A144.7}
\]

The exact-radical channel and the nonzero deleted cells are already \(O(X^\varepsilon)\), so no earlier arithmetic term is missing from (A144.7).  By the aggregate Round-140/141 relation, (A144.7) is target-equivalent to

\[
\mathcal S_{\rm recip}^{+}\ll_{\varepsilon,V}RX^\varepsilon
\]

with the literal floors, collar, half endpoint, subtraction, negative aliases, entry/exit terms, profiles, and remainders retained.  Neither real-analytic modularity nor the five completed coefficient pairings proves this estimate.

# 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| gcd-averaged nonzero count | **Pass.** The fixed-\(j\) injection and (A144.5) give \(O_\varepsilon(JX^\varepsilon)\), including squareful \(N\). |
| exact radicals | **Pass.** \(j_m=0\iff m=Dt^2\), and the weighted \(t^{-3/2}\) sum is target-safe. |
| maximal \(J=M^{3/4}\) claim | **Pass with stated scope.** It is maximal among fixed powers for this absolute root-count/divisor-bound ledger only. |
| Appell/cone equivalence | **Pass after hygiene repair.** The \(1/4\), four \(i/4\) terms, single cone kernel, weight, and \(\chi_4(d)\) agree exactly; remove the two embedded U+000D characters. |
| outer \(i/2\) saddle constant | **Pass after wording repair.** The principal factor is \(e(1/8)N^{-1/4}/h\); stationary remainders remain in their accepted owner ledger. |
| aggregate Round-140 self-return | **Pass.** It is global after full reassembly, not termwise in Appell corrections or rational branches. |
| phase/slope comparison | **Pass after replacing \(>\) by \(\gg\).** The scale ratio is \(R^{-3}\), with no statement about arbitrary Farey slopes. |
| exact first open scalar | **Pass.** (144.C34), equivalently (144.C35) with the complete ledger, is the first unproved estimate. |
| numerical evidence | **Excluded.** Every accepted step in this audit is analytic or algebraic; numerical diagnostics supply no campaign evidence. |

# 6. Dependencies and exact artifacts used

This audit used only the following campaign artifacts:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/candidates/conductor_round144_appell_completion_and_cell_reduction.md`;
3. `rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/blind_cone_automorphy_feasibility.md`;
4. `rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/indefinite_theta_source_hypothesis_audit.md`;
5. `rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/indefinite_theta_lattice_completion_attack.md`;
6. `rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reviews/blind_post_unmask_appell_return_and_cell_audit.md`;
7. the accepted Round-140 height--alias candidate, exact connector, adjudication, and synthesis named in item 6;
8. the accepted Round-141 cone-reduction candidate, adjudication, and synthesis named in item 6;
9. the accepted Round-142 rational-spectrum candidate, adjudication, and synthesis named in item 6.

No proof graph, state file, proof draft, validation matrix, or synthesis was edited.  No numerical computation or external source was used in the final audit.

# 7. Recommended state effect

1. **Repair before promotion:** remove the two embedded carriage returns, qualify (144.C9) as the principal positive-\(j\) saddle family with retained remainders, and replace the last relation in (144.C33) by the exact identity followed by \(\asymp\) and \(\gg\) as displayed in Section 1.
2. **Then promote unchanged:** the gcd-averaged bound (144.C3), exact-radical ledger (144.C20)--(144.C21), target-safe maximal absolute window \(J=M^{3/4}\), and strict survivor (144.C4).
3. **Retain/promote unchanged:** the completed scalar (144.C5)--(144.C8), including its separate \(1/4\), four corrections, cone-kernel equivalence, and exact \(\Gamma_0(4)\) multiplier.
4. **Retain with aggregate wording:** the outer \(i/2\), inverse saddle factor, and Round-140 self-return are exact only with the full accepted Round-140/141 owner ledger.
5. **Leave open:** (144.C34)--(144.C35) and every downstream M1/M2, endpoint, M9, bridge, exponent, and quarter-theorem claim.  The candidate is GREEN after the three repairs; no stronger bound follows.
