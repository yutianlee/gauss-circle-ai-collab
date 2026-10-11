# Round227 Heegner coefficient and complete joint norm audit

## 1. Result

Candidate evidence only. Campaign `gc-complete-joint-spectral-remainder`, task `heegner_joint_norm_audit`, NONBLIND coefficient/norm role, 2026-09-28. Starting graph SHA256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

There is a valid **whole-functional bridge** to the two fixed Heegner spectra used in Assing--Humphries (AH). It is obtained from the actual four-square determinant geometry, with every two-adic descendant restored. It does not identify an individual level-four regularized-theta pairing with a point value. Equations (7)--(10) below give the full signed remainder in terms of two explicit, spectral-parameter-dependent Hecke vectors. Both Eisenstein spectra are present, as are all shifts.

The growing test has an especially simple exact phase in hyperbolic distance:

\[
 2\pi R\sqrt h\,e^{-r/2}.
 \tag{1}
\]

Its spherical transform is concentrated at spectral height \(t\asymp Rh/\sqrt N\). The stationary phase contains \(h^{it}\), and a further common, rapidly varying spectral phase. Consequently neither a fixed-Heegner fourth moment nor a fixed-coefficient large sieve prices the complete signed expression without additional work.

Using the stated AH fourth moment and its separately stated Hecke second moment gives the full, applicable upper certificate

\[
 |\mathscr R_{N,T}(R)|\ll_{\epsilon,J}
 A_J(N)^2 T^{1+\epsilon}N^2.
 \tag{2}
\]

The elementary actual-coefficient bound caps this by \(A_J^2N^{2+\epsilon}\). The resulting complete complex-wave estimate is only \(T^{1/4+\epsilon}\); the inherited complex \(13/56\) certificate is already better, and the inherited complete REAL exponent \(\beta\) is stronger still. No complete gain, moment improvement, or quarter theorem is proved.

This is a quantitative assessment of the specified norm procedure, not a lower bound for the actual remainder. Even an optimistically granted, unpriced fixed-coefficient-size sieve for the true twisted vector would give raw size \(A_J^2TN^{3/2}\), still a factor \(T\) above the quarter target. Section 4 states the actual missing vector norm and the complete signed estimate, including their fully restored saving requirements.

## 2. Exact statement and hypotheses

Use every definition in the frozen complete interface: real \(T\ge2\), every real \(cT\le R\le CT\), dyadic \(2\le N\le P\), and \(P\) the smallest dyadic integer at least \(T^{3/2}\). The fixed real Schwartz \(\Psi\) may change sign. Write \(A=A_J(N)=(1+N/T)^{-J}\),

\[
 g(x)=(x/N)^{-3/4}\Psi(\sqrt{x/T})w(x/N),\qquad
 W_h(x)=g(x+h)g(x)e(R(\sqrt{x+h}-\sqrt x)),
\]
\[
 \alpha_h=1-h/(2N),\quad
 C_h=\sum_{n\ge1}r_2(n)r_2(n+h)W_h(n),\quad
 I_h=\int_0^\infty W_h(x)\,dx,
\]
\[
 \rho_h=\frac8h\sum_{d\mid h}(-1)^{h+d}d,\qquad
 \mathscr R_{N,T}(R)=2\Re\sum_{1\le h<2N}\alpha_h(C_h-\rho_h I_h).
 \tag{3}
\]

The target is the one-sided bound \(\mathscr R_{N,T}(R)\ll A^2N^{3/2}T^\epsilon\). Nothing below replaces its outer real part by a premise of separate positive shifts. Where moduli are introduced they are expressly upper certificates.

The following are the precise source interfaces used.

* [HKLDW, 1705.04771v3](https://arxiv.org/html/1705.04771v3): Theorem 3.3, equation (3.10), Lemma 3.4, and Remark 4.4, equation (4.2). The level is four, the vector is the square-integrable regularization \(\mathcal V\), and all three continuous cusps occur. The growing-test formula is derived, not supplied by its Laplace theorem.
* [AH, 2607.13518v1](https://arxiv.org/html/2607.13518v1): Theorem 1.2 at the two actual pairs \((q,z_q)=(1,i),(2,(-1+i)/2)\), both discriminant \(-4\); the proof of its actual-\(r_2\) application, Theorem 1.3; equation (8), with fixed \(q\), for the Hecke second moment; and the local-factor discussion in Section 2.4. The fourth-moment assertion is treated as the stated external source premise, not as a newly proved theorem. AH uses probability Haar normalization; below the orthonormal functions use hyperbolic area. If \(v_q=\operatorname{vol}(\Gamma_0(q)\backslash\mathbb H)\), then \(u_j=\varphi_j/\sqrt{v_q}\). Thus the fourth moment changes by the fixed factor \(v_q^{-2}\), with \(v_1=\pi/3,v_2=\pi\).
* The one additional indispensable theorem audit is [Chamizo, *The Additive Problem for the Number of Representations as a Sum of Two Squares*, published 26 January 2022, Proposition 2.2](https://link.springer.com/article/10.1007/s00009-021-01959-3). Its printed disk transforms contain a smoothing parameter \(\Delta\). They are **not** used as an arbitrary-test bound. The underlying determinant/pretrace identity is derived below for the actual compact smooth test, and its transform is estimated independently. The group, Hecke normalization, two points, and constant-spectrum normalizations are matched with that proposition and equations (2.2)--(2.3). No second additional work or theorem is imported.

Two new printing limitations require fencing. AH Lemma 2.1 in both the exact-version HTML and extracted PDF page 10 has no spectral cutoff in the displayed representation sum and has the empty RHS range \(N<n\le N\). Its equation (12) also displays that empty range. This is not a usable literal collective sieve statement, and this report does not silently repair it. Moreover, even the intended conventional sieve has spectral-independent coefficients, unlike (14) below. The already recorded AH \(N^{4/2}\) mean square and application-proof self-reference remain literal; no conjectured \(4/3\) substitution is used. The PDF screenshot attempt timed out, so no rendered-image verification is claimed.

## 3. Proof and derivation

### 3.1 What the level-four coefficient really is

With the source's Fourier and inner-product conventions, HKLDW (4.2) gives

\[
 \langle\mathcal V,\mu_j\rangle
 =\frac{2\rho_j(1)}{L(1,\chi_4)}
 \widetilde L(\tfrac12,\overline\mu_j)
 \widetilde L(\tfrac12,\overline\mu_j\times\chi_4)
 \Gamma(\tfrac12+it_j)\Gamma(\tfrac12-it_j).
 \tag{4}
\]

The source derives this by identifying \(y^{1/2}\theta^2\) with its weight-one Eisenstein series, unfolding the Rankin--Selberg pairing, and factoring the resulting Euler products. This is a central-value product with Fourier and archimedean factors. It is not \(\mu_j(z_0)\), nor an unweighted \(|\mu_j(z_0)|^2\).

There are two exact obstacles to the proposed free replacement. First, AH Section 2.4 requires that if \(p^2\mid q\), then \(p\) split in \(\mathbb Q(\sqrt D)\). For \(q=4,D=-4\), the prime 2 ramifies. Thus the discriminant \(-4\) point theorem does not apply directly to the entire level-four basis appearing in (4). Second, AH Lemma 2.4 bounds point values **above by** central-value products, with local toric integrals and oldform changes; that direction does not bound the products in (4) by the point fourth moment. Its local factors and the oldspace must be computed before any coefficientwise identification. Class number one alone does not remove those requirements.

There is nevertheless a different lawful bridge: represent the entire original correlation by the level-one and level-two Hecke orbits. Both this representation and HKLDW's initial, absolutely convergent Mellin pairing equal the same arithmetic functional. This suffices without granting a termwise equality between their different bases.

### 3.2 Exact orbit geometry, parity, and normalization

Let \(A_h[F]\) count the quadruples \((a,b,c,d)\in\mathbb Z^4\) with
\(a^2+b^2-c^2-d^2=h\), weighted by \(F(c^2+d^2)\), and with
\(a\equiv c\pmod2,b\equiv d\pmod2\). Let \(S_h[F]\) count all such quadruples. In this paragraph the term \(c=d=0\) may be included; our eventual test vanishes at zero.

For \(h=4m\), the bijection

\[
 (a,b,c,d)\longmapsto
 \begin{pmatrix}(a+c)/2&(b+d)/2\\(d-b)/2&(a-c)/2\end{pmatrix}=M
 \tag{5}
\]

maps the parity-restricted quadruples to all integral determinant-\(m\) matrices. If \(n=c^2+d^2\), then
\(\|M\|_F^2=2m+n\) and \(u(Mi,i)=n/(4m)\), where
\(u(z,w)=|z-w|^2/(4\Im z\Im w)\). Passing from matrices to their images in \(\mathrm{PSL}_2\) supplies exactly a factor 2.

For odd \(h\), use instead the integral matrix
\(M=\bigl(\begin{smallmatrix}a+c&b+d\\d-b&a-c\end{smallmatrix}\bigr)\).
It has determinant \(h\), \(u(Mi,i)=n/h\), and reduction modulo 2 in
\(\{I,\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)\}\).
Conversely precisely these determinant-\(h\) matrices give integral inverse quadruples. The resulting index-three group is
\(\gamma_0^{-1}\Gamma_0(2)\gamma_0\), with
\(\gamma_0=\bigl(\begin{smallmatrix}0&-1\\1&1\end{smallmatrix}\bigr)\)
and \(\gamma_0 i=(-1+i)/2=z_2\). The conjugated Hecke matrices have odd index \(h\), so all are prime to level 2. Again the matrix-to-PSL factor is exactly 2. This proves the two orbit realizations, including the group and point in Chamizo Proposition 2.2.

The pointwise parity recurrence is

\[
 S_h[F]=S_{h/2}[F(2\cdot)]\quad(v_2(h)=1),\qquad
 S_h[F]=2A_h[F]-S_{h/2}[F(2\cdot)]\quad(4\mid h).
 \tag{6}
\]

Indeed, if \(h\equiv2\pmod4\), only even \(n\) contribute, and \(r_2(2n)=r_2(n)\). If \(4\mid h\), all representations at even \(n\) satisfy the parity match; at odd \(n\) exactly half do, by swapping the two coordinates of one represented integer. Subtracting the even part proves the second identity. This is a measure identity, so it applies to every complex \(F\), not just prefixes.

Put

\[
 k_h(u)=W_h(hu),\qquad
 H_h(t)=4\pi\int_0^\infty k_h(u)
              P_{-1/2+it}(1+2u)\,du.
 \tag{7}
\]

It is compactly supported and smooth, vanishing near \(u=0\). For fixed \(N,h,T,R\), its automorphic kernel has a convergent smooth spectral expansion. Apply the Hecke operator normalized by \(m^{-1/2}\) to the kernel at \(z_q\). The orbit sum is \(\sqrt m\) times this expansion; (5) and its odd counterpart give the additional factor 2. Thus the primitive pieces have the exact form

\[
 2\sqrt m\left\{
 \sum_j\lambda_j^{(q)}(m)H_h(t_j)|u_j^{(q)}(z_q)|^2
 +\frac1{4\pi}\sum_{\mathfrak a\text{ of }q}\int_{\mathbb R}
 \eta_t(m)H_h(t)|E_{\mathfrak a}^{(q)}(z_q,\tfrac12+it)|^2dt
 \right\},
 \tag{8}
\]

including the constant function in the discrete sum initially. Here
\(\eta_t(m)=\sum_{ad=m}(a/d)^{it}\). This follows by unfolding the finite Hecke cosets and spectral resolution of the smooth radial kernel; no \(\Delta\)-dependent disk bound is transferred. The transform normalization is checked by
\(H_h(i/2)=4\pi I_h/h\), since \(P_{-1}(1+2u)=1\).

For \(h=2^k h_0\), \(h_0\) odd, define the two finite Hecke polynomials

\[
 L_{1,h}(j)=4\sum_{a=0}^{k-2}(-1)^a
     \sqrt{h/2^{a+2}}\,\lambda_j^{(1)}(h/2^{a+2})
 \quad(k\ge2),
 \tag{9a}
\]
with empty sum zero, and
\[
 L_{2,h}(j)=2\varepsilon_k\sqrt{h_0}\,\lambda_j^{(2)}(h_0),
 \qquad \varepsilon_0=1,\quad \varepsilon_k=(-1)^{k-1}\ (k\ge1).
 \tag{9b}
\]

In the continuous versions replace \(\lambda_j(m)\) by \(\eta_t(m)\). Iterating (6) proves these exact coefficients. Crucially, every descendant has the **same** radial test \(k_h\): an A-descendant has original argument \(2^a(4m u)=hu\), and the final odd descendant has argument \(2^k h_0u=hu\). No changing test or lost endpoint is concealed by the parity recursion.

Define the actual vectors
\(V_q(j)=\sum_{h<2N}\alpha_h L_{q,h}(j)H_h(t_j)\), and
\(V_q^{\mathrm{cts}}(t)=\sum_{h<2N}\alpha_h L_{q,h}^{\mathrm{cts}}(t)H_h(t)\).
Then the full remainder is exactly

\[
 \boxed{\mathscr R_{N,T}(R)=2\Re\left\{
 \sum_{q=1,2}\sum_{j\ne0}|u_j^{(q)}(z_q)|^2V_q(j)
 +\frac1{4\pi}\sum_{q=1,2}\sum_{\mathfrak a\text{ of }q}
 \int_{\mathbb R}|E_{\mathfrak a}^{(q)}(z_q,\tfrac12+it)|^2
                    V_q^{\mathrm{cts}}(t)dt\right\}.}
 \tag{10}
\]

To check centering, the level-one constant has
\(\lambda_0(m)|u_0|^2=3\sigma_1(m)/(\pi\sqrt m)\), and the level-two constant has
\(\sigma_1(m)/(\pi\sqrt m)\). For even \(h\), the restored density is

\[
 \frac{48}{h}\sum_{a=0}^{k-2}(-1)^a\sigma_1(h/2^{a+2})
 +\frac{8\varepsilon_k}{h}\sigma_1(h_0)
 =\frac{8|2^{k+1}-3|}{h}\sigma_1(h_0)=\rho_h.
 \tag{11}
\]

For odd \(h\), it is \(8\sigma_1(h)/h\). Thus (10) subtracts precisely the prescribed continuous density. The zero atom is zero because \(W_h(0)=0\). The two groups have respectively one and two continuous cusps; none has been removed. One need not move the HKLDW Mellin contour to prove (10): both are identities for the original compact smooth arithmetic sum. Consequently no unaccounted contour residue is being set to zero.

### 3.3 Transform size and the actual spectral twist

Write \(u=\sinh^2(r/2)\). On every nonempty overlap,
\(x=hu\), \(x+h=h\cosh^2(r/2)\), and

\[
 \sqrt{x+h}-\sqrt x=\sqrt h e^{-r/2}.
\]

Since \(N/2<x<x+h<2N\), one has \(r>\log3\),
\(\sinh r\asymp N/h\), and the support in \(r\) has bounded length, uniformly even when it shrinks. All fixed-order derivatives of its amplitude are \(O(A^2)\). Also
\(\Lambda_h=Rh/\sqrt N\gg T^{1/4}\), up to fixed constants throughout \(N\le P<2T^{3/2}\).

For \(r\ge\log3\), the elementary spherical-function expansion has branches
\[
 P_{-1/2+it}(\cosh r)
 = (t\sinh r)^{-1/2}
     \bigl(e^{itr}b_+(r,t)+e^{-itr}b_-(r,t)\bigr),\quad t\ge1,
 \tag{12}
\]
with bounded symbol derivatives and expansions in inverse powers of \(t\). One way to verify the uniformity needed here is to use the even Mehler integral on \([-r,r]\). Its only endpoint singularities are square roots; their endpoint expansions give (12). Equivalently, multiplication by \(\sqrt{\sinh r}\) changes the Legendre equation to
\(p''+(t^2+1/(4\sinh^2r))p=0\); on \(r\ge\log3\), the potential and all derivatives are bounded and decay, giving the same symbol bounds by the Volterra equation. No large-\(r\) constant grows polynomially in \(N/h\) after the displayed \((\sinh r)^{-1/2}\) is extracted.

The minus branch has no stationary point. The plus branch has phase
\(\Phi_h(r)+tr\), with
\(\Phi_h(r)=2\pi R\sqrt h e^{-r/2}\). Its stationary point satisfies

\[
 t=\pi R\sqrt h e^{-r/2}\asymp\Lambda_h,
 \qquad (\Phi_h+tr)''=t/2.
\]

Second-derivative estimation, with the true smoothly vanishing endpoint amplitudes, therefore gives uniformly

\[
 |H_h(t)|\ll_J A^2\sqrt{N/h}\,\Lambda_h^{-1}
 \quad(t\asymp\Lambda_h).
 \tag{13}
\]

Outside a fixed enlarged stationary band, integration by parts in \(r\), using (12), gives arbitrary inverse powers of the phase separation. For \(|t|\le1\) and any finite imaginary eigenparameters, use the exact Legendre function and integrate against \(\Phi_h\) directly; its fixed-order derivatives have at most polynomial growth in \(N/h\), defeated by arbitrarily many powers of \(\Lambda_h\). Smooth zero extension preserves uniform derivative bounds even at a disappearing overlap. By choosing a fixed sufficiently large number of integrations, summing all \(h<2N\), the spectral dyadic tails, and the at most logarithmically many parity terms leaves \(O(A^2T^{-B})\) for any prescribed fixed \(B\). Thus low spectrum and the entire high spectrum are paid; (13) is not a truncation assumption. In particular the exact Legendre formula is available through a Mellin/gamma transition at small \(h\), so no interior Stirling formula is used there.

At an interior stationary point, its leading phase is exactly

\[
 \Phi_h(r_*)+tr_*
 =2t+2t\log(\pi R\sqrt h/t)
 =t\log h+2t(1+\log(\pi R/t)).
 \tag{14}
\]

The phase of the connection coefficient in (12) is independent of \(h\). Its leading constant and lower symbols do not delete the \(h^{it}\) factor. The corresponding physical argument is
\[
 x_*(h,t)=\frac{\pi^2R^2h^2}{4t^2}-\frac h2+
                      \frac{t^2}{4\pi^2R^2}.
\]

Consequently, after the common spectral phase is factored out, the actual joint vector has leading form
\(\sum_h a_h(t)\lambda_j(m_h)h^{it}\), where \(a_h(t)\) retains the cutoff at \(x_*(h,t)\) and \(x_*+h\), the signed \(\Psi\)'s, every parity coefficient, and the Fejer weight. This statement describes the leading phase only; (7),(9),(10), not a truncated asymptotic, define the exact vector used for bounds.

### 3.4 Complete applicable norm menu

Partition shifts dyadically \(h\asymp M\), \(1\le M\ll N\), and spectral height in enlarged dyadic bands \(t\asymp U\). Significant interaction has
\(U\asymp TM/\sqrt N\). All tails are paid as above. Let \(V_{q,M,U}\) denote the exact vector restricted to such a pair. For a parity descendant \(m=h/2^b\), its coefficient has modulus \(O(\sqrt m)\), and

\[
 \sqrt m\,|H_h(t)|\ll A^2\frac{\sqrt N}{U}\sqrt{m/h}.
 \tag{15}
\]

The sum of the factors \(\sqrt{m/h}\) over the descendants of one shift is bounded. This is why parity restoration costs at most logarithms in reorganizing supports and no extra power.

The exact collective Holder/Cauchy consequence of AH Theorem 1.2 is

\[
 \left|\sum_{t_j\asymp U}|u_j(z_q)|^2V_{q,M,U}(j)\right|
 \ll U^{1+\epsilon}\|V_{q,M,U}\|_{\ell^2(j)}.
 \tag{16}
\]

This keeps the whole shift sum inside the vector before norms. AH equation (8) supplies
\(\sum_{t_j\asymp U}|\lambda_j(m)|^2\ll(mU)^\epsilon(U^2+\sqrt m)\), applicable at fixed level one, and at level two to the odd indices that actually occur. Because
\(U^2\asymp T^2M^2/N\gg\sqrt m\) in the entire range, Minkowski and (15) give the fully priced norm

\[
 \|V_{q,M,U}\|_2\ll A^2T^\epsilon M\sqrt N,
 \quad
 |\hbox{discrete contribution of this pair}|
 \ll A^2T^\epsilon U M\sqrt N
 \asymp A^2T^{1+\epsilon}M^2.
 \tag{17}
\]

Using instead the Ramanujan bound and the local Weyl law costs
\(A^2T^{1+\epsilon}M^{2+\vartheta}\), \(\vartheta=7/64\), which is weaker. Combining fourth moment and individual Hecke second moment is the stronger of these directly matched choices. Higher Holder exponents have no supplied better point moment; the fourth moment already yields the displayed \(U\) factor. The bounds concern the true vector; they do not establish any lower bound for it.

For completeness the standard local Weyl upper majorant used here includes the continuous spectrum:
\[
 \sum_{|t_j|\le2U}|u_j(z_q)|^2+
 \frac1{4\pi}\sum_{\mathfrak a}\int_{|t|\le2U}
 |E_{\mathfrak a}(z_q,\tfrac12+it)|^2dt\ll_q U^2.
 \tag{18}
\]
It can be seen directly within the same pretrace identity: choose the positive Gaussian spectral majorant \(e^{-t^2/U^2}\); its inverse spherical transform is \(O(U^2)\) at zero, has Gaussian decay in hyperbolic distance at scale \(U^{-1}\), and is rapidly decreasing beyond that scale. At the fixed point the stabilizer is finite, while elementary disjoint hyperbolic balls give orbit count \(O(e^r)\). Summing the inverse-transform bound therefore gives \(O(U^2)\). Positivity retains, rather than drops, the Eisenstein part. This is the local-Weyl argument also underlying AH's stated point second moment, with fixed area-normalization constants.

Since \(|\eta_t(m)|\le\tau(m)\), (15),(18) bound the **entire** continuous contribution of a pair by
\[
 \sup_{t\asymp U}|V_{q,M,U}^{\rm cts}(t)|\,O(U^2)
 \ll A^2T^\epsilon (M\sqrt N/U)U^2
 \ll A^2T^{1+\epsilon}M^2.
 \tag{19}
\]
AH's cusp fourth moment has not been substituted for an Eisenstein fourth moment. Formula (19) is deliberately the fully justified collective majorant, and it can be improved only with an applicable additional argument. Summing (17),(19) over all \(M\ll N\), the fixed number of corresponding spectral dyadic bands, and all tails proves (2).

The conventional fixed-coefficient large-sieve template, if separately proved with correct normalizations and spectral restriction, would read
\(\sum_{t_j\asymp U}|\sum_{m\asymp M}b_m\lambda_j(m)|^2
\ll(U^2+M)(UM)^\epsilon\sum|b_m|^2\).
It does not apply with \(b_m\) depending on \(t_j\). Our phase (14) is exactly such a dependence. Removing a common factor does not remove \(h^{it_j}\); freezing \(t\) to intervals where this is slowly varying introduces a spectral partition and its cost. No cost-free hybrid sieve is granted. The printed AH Lemma 2.1 defects are a separate reason not to cite its literal statement here.

To quantify even this optimistic menu, pretend that the exact twisted vector enjoyed the fixed-coefficient-size conclusion without a separation cost. Equations (15) and \(U^2\gg M\) would then give
\[
 \|V_{q,M,U}\|_2\ll A^2\sqrt{NM}T^\epsilon,
 \qquad (16)\ll A^2T^{1+\epsilon}M^{3/2}.
 \tag{20}
\]
Summing every \(M\) gives \(A^2TN^{3/2}T^\epsilon\), still too large. This is an explicitly hypothetical, optimistic comparison, not an imported large-sieve theorem or a new estimate. It also leaves the continuous counterpart to be justified. A spectral phase-sensitive estimate beyond absolute Holder is needed even after that optimistic square-root shift saving.

### 3.5 Full physical restoration

The elementary actual-coefficient inequality gives
\(\sum_{h<2N}|C_h|\ll A^2N^{2+\epsilon}\).
The entire density has already the accepted nonstationary bound
\(\sum_h\rho_h|I_h|\ll A^2T^{-1}N^{3/2+\epsilon}\log(2N)\).
Thus the applicable spectral certificate is capped by the raw elementary bound. Dividing by \(N^{3/2}\) in the exact Fejer inequality and including its bounded factor \((L+2N-1)/(2N)\), \(L=3N/2-1\), gives
\[
 |N^{-3/4}\sum_n r_2(n)g(n)e(R\sqrt n)|^2
 \ll A^2T^\epsilon\{N^{-1/2}+T^{-1}+N^{1/2}\}.
 \tag{21}
\]
The uncapped spectral menu (2) would instead give the worse last term \(TN^{1/2}\); the hypothetical menu (20) would give \(T\). At \(N\asymp T\), these are wave exponents respectively \(1/4,3/4,1/2\). The Schwartz factor controls the larger retained \(N\)'s. Summing all dyadic blocks gives the stated complete complex \(T^{1/4+\epsilon}\) cap, with \(O(1)\) singleton and an arbitrarily small full tail beyond \(P\), at a sufficiently large fixed Schwartz order. No omitted large-\(h\), large-\(N\), terminal, or overlap contribution supplies a hidden saving.

For a genuine complete wave exponent \(\gamma\), the accepted bridge restores
\(P(R^2)\ll T^{1/2+\max(\gamma,0)+\epsilon}\), or physical exponent
\(1/4+\max(\gamma,0)/2\). Thus the three menu prices above restore respectively \(3/8,5/8,1/2\), all weaker than the inherited qualified \(\theta_{\rm LY}\). The separate inherited complete complex \(13/56\) certificate restores \(41/112\), also weaker than \(\theta_{\rm LY}\). The inherited \(\beta=2\theta_{\rm LY}-1/2\) applies only to the entire REAL wave and remains unchanged; it has never been inserted as a block or complex estimate.

## 4. First doubtful or unproved step and exact missing saving

The first unproved full arithmetic estimate is (10) bounded above by
\(A^2N^{3/2}T^\epsilon\), with every term as written. The exact vector requiring a better norm is

\[
 V_{q,M,U}(j)=\sum_{h\asymp M}\alpha_hL_{q,h}(j)H_h(t_j)
                    \mathbf1_{t_j\asymp U},
 \quad U\asymp TM/\sqrt N.
 \tag{22}
\]

A stronger sufficient norm closure would control

\[
 \sum_{q,M,U}U^{1+\epsilon}\|V_{q,M,U}\|_2
 +\frac1{4\pi}\sum_{q,\mathfrak a,M,U}
 \int_{|t|\asymp U}|E_{\mathfrak a}(z_q,\tfrac12+it)|^2
                |V_{q,M,U}^{\rm cts}(t)|dt
 \ll A^2N^{3/2}T^\epsilon,
 \tag{23}
\]
with the already paid tails. This stronger positive certificate is unproved and is not necessary for the one-sided signed goal: cancellation between spectral bands, shifts, or components in (10) could instead establish the target. The common spectral phase in (14), discarded by (16), is part of that alternative.

At the largest significant shifts \(M\asymp N\), \(U\asymp T\sqrt N\). To close by (16) alone would require the sufficient vector size

\[
 \|V_{q,N,T\sqrt N}\|_2\ll A^2N/T\;T^\epsilon
 \tag{24}
\]
per a logarithmically apportioned band. The actual available Minkowski bound is \(A^2N^{3/2}T^\epsilon\). Their ratio is \(T\sqrt N\), not an unspecified missing transfer. At \(N\asymp T\) the norm/spectral certificate needs a saving \(T^{3/2}\) in the raw remainder to reach quarter. Even the hypothetical sieve (20) leaves a factor \(T\). For an intermediate complete complex exponent \(\gamma\), replace the RHSs of the raw target and (24) by their multiples \(T^{2\gamma}\); the respective deficits are \(T^{3/2-2\gamma}\) and \(T^{1-2\gamma}\) at \(N=T\).

After the better elementary cap is used, the actual unproved raw gain at that shell is \(T^{1/2}\) for quarter, or \(T^{1/2-2\gamma}\) for exponent \(\gamma\). To beat the inherited complete real benchmark by this sufficient complex route one needs \(\gamma<\beta\), hence strictly more than \(T^{1/2-2\beta}\) saving over that elementary raw cap. These comparisons are between upper certificates and required upper bounds. They do not assert that the actual vector or scalar has any of those lower sizes.

No coefficientwise identification replacing (4) by an AH point value was proved. The whole-functional determinant bridge (10) removes the need for that false shortcut; it does not solve (22)--(23), the spectral-parameter twist, or the full signed estimate (10).

## 5. Required control tests and outcomes

1. **Actual coefficients and density:** Passed algebraically. The four integer variables count exactly the ordered signed \(r_2(n)r_2(n+h)\), and (11) reproduces every two-adic density. There is no substitute cusp coefficient or arbitrary input vector.
2. **All shifts and scales:** All \(1\le h<2N\), all dyadic \(2\le N\le P\), and every real radius remain in (10). Shift dyads are recombined in (17)--(21), including the dominant \(M\asymp N\) range.
3. **Joint phase before norms:** The exact sum over \(h\) defines \(V_q\) before any norm. The \(h^{it}\) and common spectral phases in (14) are retained in the exact kernel and explicitly lost only by the declared certificate.
4. **Source/point/pairing hypotheses:** Direct level-four discriminant-\(-4\) transfer fails the AH square-level splitting hypothesis. Point-to-central-value inequality has the wrong direction for the proposed replacement. The lawful bridge uses the two source-supported fixed points after exact parity geometry.
5. **Discrete and continuous spectra:** Both levels' cusp bases and all three continuous cusps are retained. No imaginary eigenvalue is dropped; any fixed low spectrum is bounded by nonstationary integration. The constant is removed only after verifying (11).
6. **Spectral and Mellin heights:** \(U\asymp Rh/\sqrt N\) reaches \(T\sqrt N\). No exponential suppression below Mellin height is assumed. The direct Legendre identity covers the small-shift gamma transition, and fixed-order integration pays all high tails.
7. **Literal endpoints, zero, and empty support:** Smooth weights vanish at the actual endpoints. The atom at \(n=0\) vanishes exactly. If continuous support is empty then \(k_h=H_h=I_h=0\); if only the integer support is empty, its nonzero density is compensated by the nonconstant spectral expression. It is not deleted. Negative shifts are represented by the outer \(2\Re\), and the diagonal remains separately in Fejer.
8. **Real/complex and full powers:** (21) and the restoration in Section 3.5 are complete complex upper certificates, not a complex interpretation of inherited \(\beta\). Full tails, singleton, logarithmic shell reconstruction, and the exact Fejer multiplier are paid.
9. **Actual versus certificate:** No positive-norm loss, stationary-phase mass, or large-sieve comparison is an arithmetic lower bound or a disproof of quarter. Signed cancellation in (10) remains possible.
10. **Statement-only control:** This role is not blind and has not read the current isolated packet, its report, current sibling report, root controls, or current reviews. Any conductor-provided mathematical steering is disclosed in Section 6. This report makes no claim to provide the separate statement-only certification.
11. **Fixed-order full goal:** No new moment follows. The accepted distribution keeps both \(V^{-2}\) and \(TV^{-136/13}\); the sufficient unbounded sequence of fixed even orders remains open. The twelfth-order milestone is not quarter. All M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, GAR, and endpoint alternatives remain open.
12. **Experiments:** Zero. Source inspection, finite algebra, integral estimates, and exponent restoration only; at least 95 percent analytical/algebraic work.

## 6. Dependencies, exact artifacts, and provenance

This is a temporary task-specific role. No current sibling or blind report was read. No numerical control was run. The conductor sent two mathematical steering messages: a possible small-shift gamma transition, and a request to derive the arbitrary-test orbit/pretrace formula explicitly and convert AH's probability normalization. They supplied no current report or control contents. The exact Legendre formula and elementary determinant/parity derivation above independently resolve those interfaces within this report.

Authorized local context inspected or used:

* `protocol.md`; `state/proof_obligations.yml` (authority, target and relevant complete-frontier nodes); `state/active_campaign.yml`.
* `strategy/round227_complete_joint_spectral_remainder.md`.
* `strategy/gauss_circle_strategy_review_2026-09-23.md`.
* `strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md`.
* `rounds/codex-managed/gc-complete-joint-spectral-remainder/briefs/heegner_joint_norm_audit.md` and `briefs/complete_joint_spectral_interface.md`.
* `rounds/codex-managed/gc-full-goal-spectral-source-review/reports/actual_shifted_spectral_sources.md`.
* `rounds/codex-managed/gc-full-goal-spectral-source-review/reviews/independent_shifted_source_review.md` and that closed campaign's `synthesis.md`.
* `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
* `state/best_proof_draft.md`.
* `rounds/codex-managed/gc-complete-logarithmic-convolution/synthesis.md`.

Primary source bindings are [AH exact-version HTML](https://arxiv.org/html/2607.13518v1), [AH exact-version PDF](https://arxiv.org/pdf/2607.13518v1), [HKLDW exact-version HTML](https://arxiv.org/html/1705.04771v3), and [Chamizo published primary, DOI 10.1007/s00009-021-01959-3](https://link.springer.com/article/10.1007/s00009-021-01959-3). The Chamizo [arXiv record](https://arxiv.org/abs/2009.01667) was inspected for provenance only: it lists v1; an attempted guessed v3 HTML URL returned 404 and supplies no evidence. The printed publisher Proposition 2.2, rather than an invented version, is the additional audited theorem.

Source statements are not graph promotions. In particular AH's theorem assertion is used at its stated fixed parameters while the printing problems in a supporting collective-sieve display remain expressly uncorrected. No claim of a full independent proof audit of AH, HKLDW, or their cited precursors is made. Every new mathematical estimate in this report remains candidate evidence pending the required nonauthor review.

## 7. Recommended state effect

**Retain** the exact whole-functional Heegner bridge, parity/constant checks, explicit spectral twist, and complete norm-cost assessment as candidate evidence. **No change** to the accepted graph, proof draft, exponents, moment bounds, or complete quarter objective.

Use the exit label `complete_joint_spectral_remainder_no_new_bound` for this report's contribution. The exact remaining problem is the complete signed estimate (10), or a sufficiently strong fully paid replacement such as (23), with deficits quantified in Section 4. The named spectral norm menu is inadequate at the restored powers, but the actual signed remainder has not been disproved.

Freeze this report at the externally recorded final SHA256 and stop. Only the conductor may close the round or choose subsequent work.
