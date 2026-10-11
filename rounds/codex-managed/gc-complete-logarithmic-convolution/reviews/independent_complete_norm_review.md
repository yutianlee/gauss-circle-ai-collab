# 1. Result

**GREEN, with the stated certificate and source limitations. No repair requested.**

This NONAUTHOR review audits the final report
rounds/codex-managed/gc-complete-logarithmic-convolution/reports/complete_factor_norm_audit.md,
SHA256 **0a9eed845bbb0e2a3a32c1003f60fe2c85ce627061484d9463d657b32f0c6353**.

Its finite identities, actual norms, legal unweighted applications, complete complex \(T^{13/56+\epsilon}\) bound, tails, and restored scope check out. That complex bound is independently derived and weaker than the inherited complete real \(T^{\beta+\epsilon}\) estimate. The favorable \(47/378\) local exponent and optimistic \(81/614\) full-scale certificate are not asserted as complete arithmetic improvements. No actual signed lower bound or all-method impossibility follows.

# 2. Exact hypotheses and reviewed scope

Retain the prescribed fixed mollifier transform \(\Psi(\sqrt{n/T})\), real \(T\ge2\), every \(R\in[cT,CT]\), \(f=1*\chi_4=r_2/4\), and
\[
 F(n)=n^{-3/4}\Psi(\sqrt{n/T})e(R\sqrt n)/\log n
 \quad(n\ge2),\qquad F(1)=0.
\]
The original singleton is retained separately. Cutoffs \(U,V\ge1\) are real, with inclusive short factors and strict long complements. Dyadic shells may have their own cutoffs because the identity holds coefficientwise before summation.

The reviewed source is the already accepted global Bourgain pair
\((\kappa,\lambda)=(13/84,55/84)\), with its standard derivative class, ambient proper-interval extension, and length at most phase-parameter convention. This review does not refresh its primary-source status or import another theorem. The inherited \(\beta\) and classical \(1/6\) estimates apply to the complete real wave; neither is assigned to an arbitrary complex factor sum.

# 3. Independent derivation of the material estimates

**Finite algebra.** For \(\psi=1,\chi_4\), write
\(a=\psi,g=\mu\psi,b=\Lambda\psi,c=\psi\log\). Then
\(g*a=\delta_1\), \(a*b=c\), including even arguments where \(\chi_4\) vanishes. Splitting \(g*c\) and using \(g_{>U}*a=\delta_1-g_{\le U}*a\) gives exactly
\[
 b=b_{\le V}+g_{\le U}*c-g_{\le U}*a*b_{\le V}
                         +g_{>U}*a*b_{>V}.
\]
Also
\[
 f\log=f*((1+\chi_4)\Lambda),\quad
 f*\mu=\chi_4,\quad f*(\mu\chi_4)=1.
\]
Thus the inverse contractions and every minus sign in the claimant's equations (5)–(8) are correct. For
\(\ell_V(t)=\sum_{r\mid t,r\le V}\Lambda(r)\),
\[
 \beta_{\psi,>V}(t)=\psi(t)(\log t-\ell_V(t)),\qquad
 0\le\ell_V(t)\le\log t.
\]
The complete contraction returns \(f*b_\psi\), not a small error. At prime powers, the logarithmic coefficient is \(\log2\) at \(2^k\), \(2\log p\) at split powers, and \(0\) or \(2\log p\) at odd or even inert powers. No prime-only replacement occurs.

The bounds \(|f|\le d_2\), \(|\alpha_{\le U}|,|\alpha_{>U}|\le d_3\), and \(|\beta_{>V}|\le\log\) prove the actual norm table uniformly in both cutoffs. In particular \(\alpha_{\le U}=f*g_{\le U}\) need not be supported below \(U\); the report does not make that false inference.

**The affine-square-root source seam.** With a free variable \(m\asymp M\) and fixed complementary product \(v\), \(vM\asymp N\), the phase parameter is \(\mathcal T=R\sqrt N\). For \(N\le T^{3/2}\),
\[
 \mathcal T/M\gg T/\sqrt N\gg T^{1/4}.
\]
Splitting a periodic variable as \(m=4r+a\) introduces only finitely many constant character values. On an ambient \(r\)-interval of length \(L\asymp M/4\), the normalized phase is
\[
 \sqrt{t+\alpha/L},\qquad \alpha=a/4.
\]
Its derivatives are
\[
 \left(\prod_{i=0}^{j-1}(1/2-i)\right)
 (t+\alpha/L)^{1/2-j}.
\]
They are uniformly the affine-translated square-root model on a fixed positive interval. For large \(L\) they are uniformly close, in each required derivative, to the unshifted model; bounded \(L\) is paid trivially. This checks the accepted derivative-class premise rather than relying merely on smoothness. Also \(L\ll\mathcal T'\asymp R\sqrt N\).

Fixing all other variables and imposing their ordering and product bounds leaves a proper subinterval of the same ambient row. The source is applied there without replacing the ambient scale by a short intersection length. Logarithms and the actual radial weight enter by Abel summation afterwards. This yields
\[
 \sum_{m\in I}e(R\sqrt{vm})
 \ll T^{\kappa+\epsilon}N^{\kappa/2}\sqrt M.
\]
No Möbius, prime, or arbitrary bounded coefficient is inserted into this estimate.

**Whole-range Type I.** Fix a short product \(a\) and let \(r=2\) or \(3\) be the number of free periodic factors. Choosing their longest factor gives \(M\gg(N/a)^{1/r}\). Counting the other factors and restoring \(N^{-3/4}\) yields
\[
 T^\kappa N^{\kappa/2+1/4-1/(2r)}
                      a^{-1+1/(2r)}
\]
up to the explicitly allowed logarithms and Schwartz weight. Hence the three prices in claimant (13) are respectively
\[
 T^\kappa N^{\kappa/2}v^{1/4},\quad
 T^\kappa N^{\kappa/2+1/12}u^{1/6},\quad
 T^\kappa N^{\kappa/2+1/12}(uv)^{1/6}.
\]
The short sums use only \(|\mu|\le1\) and \(\Lambda(k)\le\log k\). Replacing the true short-product domain by the full short rectangle is an upper bound. Empty ranges and the \(N^{1/4}\) cap are correctly retained.

For a shell supported at \(n\le2N\), \(U\ge2N\) makes \(\alpha_{\le U}=\bar a_\psi\) on every relevant argument and kills the long term. Since \(\bar a_\psi*a_\psi=f\), \(Q_0-Q_2=0\) exactly. The remaining \(\bar a_\psi*c_\psi\) has two free periodic variables and price
\[
 (1+N/T)^{-A}\min\{N^{1/4},T^\kappa N^{\kappa/2}\}.
\]
For \(N\le T\), its second term is at most \(T^{3\kappa/2}\); for \(N>T\), choose \(A>\kappa/2\) and sum its decreasing dyadic tail. Including \(n=1\) proves the complete complex exponent
\(3\kappa/2=13/56\). It is not inferred from a real estimate. The other boundary cases \(V\ge2N\) and \(UV\ge2N\) also contract or empty exactly as claimed.

**Type II.** After Cauchy in \(s\), the diagonal costs \(S^2K\) before radial normalization. At displacement \(h=|t-t'|\ge1\),
\[
 u\asymp Rh/\sqrt K,\qquad u/\sqrt S\gg T/\sqrt N.
\]
The global unweighted pair gives
\(T^\kappa h^\kappa K^{-\kappa/2}S^{97/168}\).
This uses the global high-parameter interface; it does not apply the separate accepted kernel (L4) beyond its stated \(u\)-range. All parameters here remain polynomial in \(T\).

The two product masks have an interval intersection; the product of their smooth amplitudes has bounded normalized variation. The actual norms then give the off-diagonal square
\[
 \ll T^{\kappa+\epsilon}S^{265/168}K^{349/168}.
\]
Its square root times \((SK)^{-3/4}\) is
\(T^{13/168}S^{13/336}K^{97/336}\); the diagonal becomes \((S/K)^{1/4}\). This verifies (17), including the swapped orientation. The second-derivative alternative gives (18); its inverse-parameter term is dominated because \(u\gg\sqrt S\).

**Full-scale comparison and restoration.** With \(N=T^\nu,K=T^k\), equality of the two exponent costs gives
\[
 252k=71\nu-26,\qquad \gamma_*=(55\nu+26)/504.
\]
At \(\nu=2/3\), this is \(k=16/189,\gamma=47/378\). The \(\beta\)-favorable interval in (21) is correct. The actual prime-two short incidence persists whenever \(V\ge2\), while \(V<2\) does not confer an advantageous lower bound on the long factor. These are limitations of the named certificates.

Even granting every optimal split, the intersection with the classical high-scale price is
\(\nu=226/307,\gamma=81/614\). The second-derivative off-diagonal price is at least \(1/4-\nu/8\), larger at that intersection. Thus the quoted optimistic comparison is valid and still exceeds \(\beta<27/208\).

Every expanded coefficient is bounded by a fixed divisor function times \(\log n\). At \(Z=T^{3/2}\), absolute tail summation gives
\(T^{3/8+3\eta/2-L/4}\), so a fixed sufficiently large Schwartz order pays any required negative power. Partial shells, overlaps and the singleton are retained. Finally \(\sqrt R\) restoration gives \(1/4+\gamma/2\), including \(97/307\) for the hypothetical \(81/614\), and exactly \(\theta_{\rm LY}\) for \(\gamma=\beta\).

# 4. First doubtful or unproved step

No defect was found in the report's stated bounds. The first unproved step remains its equation (24): a stronger estimate for the entire actual real recombination, uniform in every prescribed radius and including all complements.

The prime-two absolute mass is interpreted at the short-convolution incidence \((k,r=2)\), with \(f(k)\) already grouped. Its order \(N^{1/4}/\log N\) follows from \(f\ge0\), elementary lattice-area counting and \(\Psi\to1\) at \(N=T^{2/3}\). Taking absolute values further inside \(f=1*\chi_4\) could increase that certificate. Neither interpretation is a signed lower bound.

The cutoff discussion identifies ranges allowed by the literal supports and costs of the chosen bounds; it does not prove positive signed mass in every allowed Type-II rectangle.

# 5. Controls and outcome

- Both character branches, prime powers, \(2\), and all real cutoff equalities: pass.
- Proper intervals, fixed-modulus affine shifts, derivative class and length-to-phase convention: pass within the accepted source interface.
- Actual \(\ell^1/\ell^2\) norms, Type-I short sums and Type-II diagonal/off-diagonal costs: pass.
- Complete complex \(13/56\), singleton, all scales and infinite Schwartz tail: pass.
- Inherited real-only benchmark and full physical reconstruction: pass.
- Optimistic versus actual factor ranges and absolute versus signed conclusions: correctly distinguished.

No external search or mathematical experiment was performed. No M1/M2/GAR, endpoint, pointwise benchmark or complete moment owner is discharged by this review.

# 6. Dependencies, hashes, and provenance

This is post-report NONBLIND review of another author's derivation. I authored the separate frozen round225 attack report (SHA256 952cd0ad2697cbe9c8cf28e4feba8bb04f2f22ce59884848dca7959c282dd521) and retain rounds217–224 history. This is not a history-free role or an independent review of my own report. No current sibling review or conductor control was read. The report under review was not edited.

| Artifact | SHA256 |
|---|---|
| Reviewed reports/complete_factor_norm_audit.md | 0a9eed845bbb0e2a3a32c1003f60fe2c85ce627061484d9463d657b32f0c6353 |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| Current briefs/conductor_complete_circle_wave.md | 6adcf15bf5850f080aefd63c00d83d3482f6c244f5244c340b4206c47c46e0ef |
| strategy/round225_complete_circle_logarithmic_convolution.md | 64be6a3fb32b2f33deea69cef87b846ec06732e002ffd2f5156f21f7ea8c878b |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| sources/bourgain_2017_exponent_pair.md | a2b13364b738457889546d0a52c027358d7eb450bebd4272a612d70f5e917361 |
| rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md | 6ea983ef7066a7dc1a7833bbf4a99889e79c75eef9c42190421a4248c104aa5a |

The source card refers to Bourgain, arXiv:1408.5794v2, global Theorem6/Section5, not the withdrawn Bourgain–Watt paper. This review audits the application against that accepted interface; it is not a new primary-source audit.

# 7. Recommended state effect

**GREEN for the frozen report's scoped finite identities, complete fallback estimates and failed-certificate evidence. No repair requested; no graph promotion implied.** Retain the unchanged complete real exponent \(\beta\), accepted moments and all independent full-proof owners. The complete signed inequality remains open. Stop after this review and its final hash.

