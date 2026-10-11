# Round 213 independent centering seam review

## 1. Result and verdict

**GREEN for the scalar-centering equivalence at the paid target scale, the uniform sum-integral correction, and the two precisely defined positive-certificate bounds. No mathematical repair is required at the bound claimant hash.**

Campaign: `gc-complete-centered-arithmetic`; round: 213.
Task: `independent_centering_review`.
Role: conductor-directed **NONBLIND** seam review, performed after the reviewer's separate statement-only report was completed. This seam claims no additional blind credit.
Generated: 2026-09-28T00:53:16+08:00.
Graph hash, inherited metadata only:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.

Claimant: `rounds/codex-managed/gc-complete-centered-arithmetic/controls/conductor_centering_ledger.md`.

**Final claimant SHA-256:**
`9d626e323eff1239ec7a5fa76def29d0e53c90b48cebd9701894329d12e0a22d`.

The filesystem hash agrees with the conductor-supplied hash. The lower bounds retain their essential fixed-interior qualification. Both lower bounds concern explicit positive upper certificates, never the actual signed remainder or its radius energy. The complete signed target remains open.

## 2. Exact hypotheses and statements checked

The parameters are

\[
b=83/650,\quad T^{4b}<N<T^{1-2b},\quad
L=\max(2,\lceil\sqrt N T^{-2b}\rceil),\quad
K=\max(2,\lceil NT^{-4b}\rceil),
\]
\[
U=N^{3/2}/T,\quad \Lambda_s=hk/U,\quad
\Lambda_*=LK/U\asymp T^{76/325},
\]

with \(1\le h<L\), \(1\le k<K\), and \(\Omega=\{h\ne k,\ \Lambda_s>1\}\). Radii lie in \([T/\sqrt2,\sqrt3T]\). Upper statements use the entire open band, including bounded integer cutoffs. Lower statements use each fixed interior power \(N=T^\alpha\), \(4b<\alpha<1-2b\).

The actual amplitude supplied in the permitted closed-212 report is

\[
g_N(t)=(t/N)^{-3/4}\Psi(\sqrt{t/T})v(t/N),
\]
\[
W_s(t)=g_N(t)g_N(t+h)g_N(t+k)g_N(t+h+k),
\quad
a_s(n)=r_2(n)r_2(n+h)r_2(n+k)r_2(n+h+k).
\]

Here \(v\) is fixed, real, smooth, nonzero, and supported in \([1,4]\); \(\Psi\) is the actual real mollifier transform, smooth near zero, with \(\Psi(0)=1\). Only its bounded fixed-order derivatives on a fixed neighborhood of zero are needed. There is no physical \(N^{-3/4}\) factor in this amplitude. All products retain their smooth zero extension and complete overlap.

For an arbitrary nonnegative scalar \(\rho_s\ll_\varepsilon T^\varepsilon\), independent of \(t,R\), the ledger defines

\[
D_s=\sum_na_s(n)W_s(n)e(R\psi_s(n)),\quad
I_s=\int W_s(t)e(R\psi_s(t))\,dt,
\]
\[
E_s=D_s-\rho_sI_s,\qquad
C_s=\sum_n(a_s(n)-\rho_s)W_s(n)e(R\psi_s(n)).
\]

The discrete certificate \(P'\) uses the coefficient magnitudes \(|a_s-\rho_s||W_s|\). The second certificate \(P^\nu\) uses total variation of the real measure

\[
\nu_s=\sum_na_s(n)W_s(n)\delta_n-\rho_sW_s(t)\,dt.
\]

Both employ the modulus of \(\widehat w_+(T[\psi_s(t)-\psi_s(u)])\), where \(w\ge0\) is fixed smooth of integral one and compactly supported inside the normalized radius interval. The reviewed bounds are

\[
cN/\sqrt{\Lambda_*}\le P',P^\nu
\ll_\varepsilon T^\varepsilon N/\sqrt{\Lambda_*},
\tag{R1}
\]

with only the lower inequality restricted to fixed interior scales. This review does not independently certify any local-density candidate as an integer mean. Any use of a particular \(\rho_{\rm loc}\) falls under the proved theorem only through the stated scalar, nonnegative, subpower hypotheses.

## 3. Independent derivation and seam audit

### A. Actual translated masks meet the needed hypotheses

Put \(q=\sqrt{N/T}\). On the fixed scaled support,

\[
g_N(Nx)=x^{-3/4}\Psi(q\sqrt x)v(x),\qquad q\le T^{-b}.
\]

The actual mollifier transform has bounded derivatives on this shrinking neighborhood of zero. The chain and product rules therefore give \(\|g_N^{(j)}\|_\infty\ll_jN^{-j}\), hence \(\|W_s^{(j)}\|_\infty\ll_jN^{-j}\), uniformly in all allowed shifts. Smooth compact support of \(v\) makes the extension by zero smooth; the upper overlap endpoint \(4N-h-k\) is not replaced by a sharp cutoff.

The exact cutoffs are within a factor two of their unrounded values. Thus

\[
\frac{h+k}{N}\ll N^{-1/2}T^{-2b}+T^{-4b}\ll T^{-4b}=o(1)
\]

uniformly on the full band. Choose a closed interval strictly inside \((1,4)\) on which \(|v|\) is bounded below, then shrink it by a fixed amount. For all large \(T\), all four translated arguments over the shrunken interval remain in the original interval. Also \(\Psi(q\sqrt x)\to1\) uniformly there. Every factor \(|g_N|\) is bounded below there; consequently

\[
cN\le S_s:=\sum_n|W_s(n)|\le CN
\tag{R2}
\]

uniformly in the shift. This does not require \(v\) or \(W_s\) to have a fixed global sign.

### B. Residue total variation and centered mass

Although \(|W_s|\) need not be smooth, it is absolutely continuous and

\[
\operatorname{Var}(|W_s|)\le\int|W_s'(t)|\,dt=O(1).
\]

For the four sums \(S_{s,r}=\sum_{n\equiv r\ (4)}|W_s(n)|\), translating an index by one bounds \(|S_{s,r}-S_{s,r+1}|\) by this total variation. The relevant unit intervals are disjoint, and smooth zero extension handles the exterior points. Hence

\[
Z_s:=S_{s,3}=S_s/4+O(1)\ge S_s/5
\tag{R3}
\]

for sufficiently large \(T\), uniformly. No finite-zero-set assumption and no derivative of \(|W_s|\) at a zero is needed.

Actual sums of two squares cannot be \(3\pmod4\), since a square is \(0\) or \(1\pmod4\). The unshifted factor \(r_2(n)\) therefore gives \(a_s(n)=0\) there. Set

\[
M_s=\sum_na_s(n)|W_s(n)|,\qquad
M'_s=\sum_n|a_s(n)-\rho_s||W_s(n)|.
\]

The exact inequalities

\[
M'_s\ge\rho_sZ_s,\qquad M_s\le M'_s+\rho_sS_s
\]

give \(\rho_sS_s\le5M'_s\) and therefore \(M'_s\ge M_s/6\). The ledger's weaker constant is valid without any optimization of the scalar mean. All quantities at this seam are absolute masses, so sign changes of the original mask cannot defeat the comparison.

### C. The inherited actual mass really survives the removed sectors

The permitted closed-212 report and its review supply a complete proof, which checks independently as follows. For \(u_n=r_2(n)|g_N(n)|\), elementary one-point disk-area counting on an interval where \(|v|\) is bounded below gives

\[
\sum_nu_n\asymp N,\qquad \max_nu_n\ll_\eta N^\eta.
\]

For any nonnegative zero-extended sequence \(z\) supported in an interval of length \(O(N)\), the length-\(H\) moving sums yield

\[
\sum_nz_n^2+2\sum_{r=1}^{H-1}(1-r/H)\sum_nz_nz_{n+r}
\ge c(H/N)(\sum_nz_n)^2.
\tag{R4}
\]

This follows by expanding the squares of \(\sum_{j=0}^{H-1}z_{m+j}\), then applying Cauchy over the \(O(N+H)\) possible \(m\). Here both needed lengths satisfy \(H=o(N)\).

Apply (R4) first with \(z=u,H=L\). After subtracting the \(h=0\) term \(O_\eta(N^{1+\eta})\), one obtains \(\sum_{1\le h<L}\sum_nu_nu_{n+h}\gg LN\). Apply it again to \(z_n=u_nu_{n+h},H=K\), and use Cauchy over \(h\). The \(k=0\) terms total \(O_\eta(LN^{1+\eta})\). This proves \(\sum_{h<L,k<K}M_s\gg LKN\), provided \(N^\eta=o(L)\) and \(N^\eta=o(K)\).

The repeated pairs and small-product pairs have total mass at most

\[
O_\eta\bigl(N^{1+\eta}[L+U\log(2L)]\bigr).
\]

Relative to \(LKN\) this is \(O_\eta(N^\eta/K+N^\eta\log(2L)/\Lambda_*)\). At every fixed interior power, choose a single sufficiently small \(\eta>0\) to make all these error ratios tend to zero. Thus

\[
\sum_{s\in\Omega}M_s\gg LKN,\qquad
\sum_{s\in\Omega}M'_s\gg LKN.
\tag{R5}
\]

This is actual arithmetic mass; it neither assumes an individual four-point asymptotic nor retains either moving-sum axis as residual mass. The fixed-interior qualification is necessary for the axis subtractions and is preserved by the ledger.

### D. Phase, scalar subtraction, and full-band discretization

The exact identity

\[
\psi_s(t)=-\frac14\int_0^h\int_0^k(t+x+y)^{-3/2}\,dy\,dx
\]

gives \(T\psi'_s(t)\asymp\Lambda_s/N>0\) on the complete support, and \(|R\psi_s^{(j)}(t)|\ll_j\Lambda_sN^{-j}\). Smooth nonstationary integration by parts therefore gives \(|I_s(R)|\ll_A N(1+\Lambda_s)^{-A}\), uniformly in the allowed radius window.

For \(A>1\), summing in \(k\) and distinguishing \(h\le U\) from \(h>U\) proves

\[
\sum_{h<L}\sum_{k\ge1,\ hk>U}(hk/U)^{-A}
\ll_A U\sum_{h<L}h^{-1}\ll_A U\log(2L).
\]

The estimate remains valid when \(U<1\). Hence the averaged scalar term is

\[
\frac1{LK}\sum_{\Omega}\rho_s|I_s(R)|
\ll_\varepsilon T^\varepsilon N/\Lambda_*
\ll_\varepsilon T^{4b+\varepsilon},
\tag{R6}
\]

after a separate small epsilon allowance for the logarithm. The inequality \(N/\Lambda_*\ll NT^{6b-1}\le T^{4b}\) uses the upper band endpoint correctly. Both directions of the triangle inequality prove the stated equivalence of target-sized upper bounds for the complete correlation average and the centered residual average once the closed-212 complement costs are restored. It proves neither upper bound on its own.

The identity

\[
E_s-C_s=\rho_s(\sum_nf_s(n)-\int f_s(t)\,dt)
\tag{R7}
\]

has the correct sign. The smoothly zero-extended \(f_s\) satisfies

\[
\|f_s^{(A)}\|_1\ll_A N^{1-A}(1+\Lambda_s)^A.
\]

Poisson summation followed by \(A\ge2\) integrations by parts at each nonzero integer Fourier mode gives the ledger's displayed error bound. On the entire band, including non-power scales and bounded cutoffs,

\[
N/(1+\Lambda_s)\gg T^{(166-76)/325}=T^{90/325},
\quad N\le T^{242/325}.
\]

Thus its right-hand side is \(O_A(T^{(242-90A)/325})\). Choosing \(A\) sufficiently large gives any prescribed negative power of \(T\), also after the factor \(\rho_s\). All constants use fixed-order mask seminorms and the fixed radius window; no support endpoint term or additional atom is omitted.

### E. Both positive lower bounds and the exact measure variation

Continuity at \(\widehat w_+(0)=1\) gives a neighborhood on which its modulus is at least \(1/2\). Partition the full real support interval into \(O(1+\Lambda_s)\) bins of diameter at most a sufficiently small constant times \(N/(1+\Lambda_s)\). Every integer is assigned to exactly one bin. The phase derivative bound puts each within-bin pair in that neighborhood. Positivity and Cauchy yield

\[
G'_s\gg (M'_s)^2/(1+\Lambda_s).
\]

Combining this with (R5) and \(1<\Lambda_s\le\Lambda_*\) gives the first lower bound in (R1).

The atomic and absolutely continuous parts of \(\nu_s\) are mutually singular, regardless of the signs of \(W_s\). Their total variations therefore add exactly:

\[
d|\nu_s|(t)=\sum_na_s(n)|W_s(n)|\delta_n(t)
+\rho_s|W_s(t)|\,dt.
\tag{R8}
\]

There is no cancellation of an atom against an absolutely continuous density in total variation. The positive energy of (R8) contains the complete uncentered atomic-atomic term as a nonnegative summand. The same bin argument with \(M_s\), followed by (R5), proves the second lower bound in (R1). This measure proof indeed needs no residue-zero comparison once actual mass is supplied.

### F. Matching upper bounds retain all lattice and measure terms

The derivative lower bound and Schwartz decay imply

\[
K_s(t,u):=|\widehat w_+(T[\psi_s(t)-\psi_s(u)])|
\ll_A(1+\Lambda_s|t-u|/N)^{-A}.
\]

The actual divisor envelope gives every atomic weight and every continuous density in (R8), as well as each discrete centered weight, the bound \(O_\eta(T^\eta)\). For \(A>1\),

\[
\sum_mK_s(n,m)\ll1+N/\Lambda_s,
\qquad \int K_s(t,u)\,du\ll N/\Lambda_s.
\]

There are \(O(N)\) support integers and support length \(O(N)\). The discrete centered energy and atomic-atomic measure term are therefore \(O_\varepsilon(T^\varepsilon[N+N^2/\Lambda_s])\). Each of the two atomic-continuous terms and the continuous-continuous term is \(O_\varepsilon(T^\varepsilon N^2/\Lambda_s)\). The lattice diagonal \(N\) is explicitly retained; no measure cross term is discarded when obtaining the upper bound.

After taking square roots and allocating epsilon again,

\[
P',P^\nu\ll_\varepsilon T^\varepsilon
\left[\sqrt N+\frac N{LK}\sum_{h<L,k<K}\sqrt{U/(hk)}\right]
\ll_\varepsilon T^\varepsilon[\sqrt N+N/\sqrt{\Lambda_*}].
\]

The two sums of inverse square roots give the last step. Finally \(\Lambda_*/N\ll T^{-90/325}\), so the second term dominates uniformly. This proves both upper bounds in (R1).

### G. Norm normalization and claim scope

The measure \(d\mu_T(R)=T^{-1}w(R/T)dR\) is a probability measure. Exact expansion gives the signed, complex-kernel mean square of \(C_s\), while the analogous finite-measure expansion gives that of \(E_s\). Their bounds are

\[
\|C_s\|_{L^2(\mu_T)}\le\sqrt{G'_s},\qquad
\|E_s\|_{L^2(\mu_T)}\le\sqrt{G_s^\nu}.
\]

The ledger's normalized radius \(L^1\) inequalities follow by Cauchy. More precisely, the same certificates also bound the corresponding normalized shift averages of these \(L^2\) norms, and by Minkowski the \(L^2(\mu_T)\) norm of the shift average of the absolute values. None of these inequalities reverses, and none identifies a pointwise supremum with a radius average.

The exponent in (R1) is \(\alpha-38/325\). Its gap above \(4b=166/325\) is \(\alpha-204/325\). For every fixed \(\alpha>204/325\), a sufficiently small target epsilon cannot absorb that gap. This excludes exactly the two stated positive closures on that subband. It does not exclude a signed energy estimate, a nonconstant arithmetic centering scheme, or the original pointwise target.

## 4. First doubtful or unproved step

No defect was found in the reviewed finite comparisons, the uniform analytic errors, or either certificate's bounds at the stated hash. The first unproved research input remains cancellation in the actual signed centered remainder or signed radius energy, together with any pointwise transfer needed by the target.

In particular, replacing the signed energy by total variation and then expecting that same positive object to have target size on the upper subband is refuted. The invalid reverse implication would be to infer a large signed energy from the large positive certificate. The ledger explicitly avoids it.

The review verifies only the stated hypotheses on an arbitrary \(\rho_s\). It neither proves a candidate local expression is the integer correlation mean nor imports such a mean as a dependency.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Actual mask and normalization | GREEN: the four size-one translated factors have uniform scaled derivatives and a common interval of nonzero absolute mass; no extra physical power or sharp overlap cutoff appears. |
| Sign-changing mask | GREEN: original signs remain in signed sums; bounded variation of the absolute mask, rather than fictitious smoothness, supplies residue equidistribution. |
| Residue-zero centering | GREEN: the actual unshifted r2 factor vanishes on residue three, and the exact two-inequality argument gives \(M'_s\ge M_s/6\). |
| Actual inherited mass | GREEN at fixed interior scales: both moving-sum axes and both paid sectors are accounted for before asserting residual mass. |
| Continuous signed-measure variation | GREEN: atomic and continuous parts are singular; their variations add and all positive mixed terms remain available. |
| Matching certificate upper bounds | GREEN: lattice spacing contributes \(N\), continuous integration contributes \(N^2/\Lambda_s\), and both are correctly averaged over the shift rectangle. |
| Scalar subtraction cost | GREEN throughout the band: product summation, including \(U<1\), gives the paid \(N/\Lambda_*\) scale. |
| Sum-integral error | GREEN throughout the band: exact correction sign, smooth zero extension, real support endpoints, uniform radius constants, and exponent \(90/325\) are all correct. |
| Norm and scope | GREEN: probability normalization, signed identities, upper certificates, radius means, and pointwise supremum remain distinct. |
| Endpoint quantifiers | GREEN: upper statements remain uniform; actual lower mass and certificate obstruction are only claimed at fixed interior powers. |
| Full goal | GREEN scope control: no signed correlation estimate, milestone, quarter theorem, or M1/M2 parent is proved or promoted. |

All controls are analytical; no numerical experiment or external source was used. As a logical control, dropping the residue-zero hypothesis would permit \(a_s\equiv\rho_s\) and zero discrete centered certificate, confirming the specific role of the actual zero residue. The measure certificate would still retain positive variation because its discrete and continuous parts are singular, confirming that the two lower-bound mechanisms are genuinely distinct.

## 6. Dependencies, provenance, and access boundary

Only these files were read during this nonblind seam:

1. `protocol.md`.
2. `rounds/codex-managed/gc-complete-centered-arithmetic/controls/conductor_centering_ledger.md`.
3. `rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_oscillatory_attack.md`.
4. `rounds/codex-managed/gc-complete-four-point-correlation/reviews/independent_oscillatory_attack_review.md`.

The independently checked hashes are:

| Artifact | SHA-256 |
|---|---|
| Current conductor ledger | `9d626e323eff1239ec7a5fa76def29d0e53c90b48cebd9701894329d12e0a22d` |
| Closed-212 oscillatory report | `7c84d41e28c726d39b13cfe6b1e65f6cf8800ff746ca43b56157954908db423f` |
| Closed-212 independent review | `00ce71e758a0b0776c6df10a69b08a942812a7ff2da3b55eb9dbb0c65f120e0e` |

The reviewer had previously completed the separate isolated report, but did not reread or edit it during this seam. Its conductor-supplied preservation hash is `a16db0ca6ec19bace974febee7df1ed252b766772574a8469edf75dacfcc1e1a`; that hash is recorded as supplied, not newly certified here. The present review is explicitly nonblind and derives its actual-source application from the permitted closed-212 files. No other current report, local-arithmetic source, state file, synthesis, web source, or successor artifact was opened.

Only this assigned review file was written. The claimant and the separate isolated report remain untouched by this reviewer.

## 7. Recommended state effect and final binding

**Retain as GREEN reviewed scoped evidence** the ledger's scalar-centering equivalence, complete error bounds, and both named positive-certificate obstructions. Do not promote an integer correlation mean, signed correlation or energy bound, pointwise exponent, milestone, quarter theorem, or M1/M2 parent.

This GREEN verdict binds only to conductor-ledger SHA-256
`9d626e323eff1239ec7a5fa76def29d0e53c90b48cebd9701894329d12e0a22d`.
Any material revision requires a renewed binding. The same-round seam is complete; no next round is designed or begun.
