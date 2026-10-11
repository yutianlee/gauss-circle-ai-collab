# Round226: actual shifted spectral sources

## 1. Result: a legal transfer, but no complete gain

Campaign: `gc-full-goal-spectral-source-review`; role: `actual_shifted_spectral_sources`; selected-context source audit, 2026-09-28. Starting graph SHA256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

The two audited source interfaces concern the **actual** coefficients \(r_2(n)r_2(n+h)\). Assing--Humphries supplies a current unconditional sharp-sum improvement in the growing-shift range. Neither audited theorem supplies the required oscillatory, uniformly growing-test estimate. Absolute Abel transfer pays \(1+Th/\sqrt N\), and already fails to improve the elementary coefficient bound at the critical block \(N=T^{2/3}\), even at \(h=1\). The Laplace theorem cannot be substituted for a theorem about arbitrary oscillatory tests with a constant independent of their derivatives.

This is a failure of these named transfers, not a lower bound for a signed circle wave and not a no-go theorem for direct spectral cancellation. Section 3 gives one fully normalized, sufficient **unproved** joint signed remainder estimate. It includes every shift through the support length, the density, diagonal, smooth dyadic reconstruction, singleton, and infinite tail. It would prove the complete complex wave bound, hence the quarter goal; it is stronger than the inherited complete real bound. No new moment or pointwise exponent is proved here.

Exactly two source works were audited. No numerical experiments or third-source imports were made. Retained history from rounds217--225 is disclosed in Section6; this was not a fresh, history-free or statement-only audit.

## 2. Exact statements and hypotheses

Write \(e(t)=e^{2\pi it}\), \(T\ge2\), and let \(cT\le R\le CT\) be **any real radius**, with fixed positive \(c,C\). The actual fixed mollifier has real even Schwartz transform \(\Psi\); \(\Psi\) need not be nonnegative. The target is
\[
 B_T(R)=\sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
                 \cos(2\pi R\sqrt n-3\pi/4)\ll_\epsilon T^\epsilon.
 \tag{1}
\]
The accepted bridge is
\[
 P(R^2)=\frac{\sqrt R}{\pi}B_T(R)+O_\epsilon(T^{1/2+\epsilon}).
 \tag{2}
\]
The inherited exponent is only for this complete real wave:
\[
 \beta=2\theta_{\rm LY}-\tfrac12,\qquad
 \theta_{\rm LY}=(3292+25\sqrt{1717})/13762.
\]
No per-block or complete complex \(\beta\) estimate is granted.

For both sources put
\[
 A_h(x)=\sum_{1\le n\le x}r_2(n)r_2(n+h),\qquad
 E_h(x)=A_h(x)-\mathfrak c_hx,
\]
\[
 \mathfrak c_h
 =8|2^{\alpha+1}-3|\frac{\sigma_1(h')}{h}
 =\frac8h\sum_{d\mid h}(-1)^{h+d}d,\quad
 h=2^\alpha h',\quad h'\ {\rm odd}.
 \tag{3}
\]
Thus all two-adic cases are retained; \(\mathfrak c_h>0\) and
\(\mathfrak c_h\ll_\epsilon h^\epsilon\).

**Source interface A.** Hulse--Kuan--Lowry-Duda--Walker, *The Laplace Transform of the Second Moment in the Gauss Circle Problem*, [1705.04771v3](https://arxiv.org/html/1705.04771v3), [primary PDF](https://arxiv.org/pdf/1705.04771v3), [version record](https://arxiv.org/abs/1705.04771). Current recorded revision: 1 April2020; published ANT15(2021),1--27. No withdrawal is displayed. Theorem7.1 gives, uniformly in integer \(h\ge1\),
\[
 \sum_{n\ge1}r_2(n)r_2(n+h)e^{-n/X}
 =\mathfrak c_hX+
 O_\epsilon(X^{1/2+\epsilon}e^{h/X}h^\Theta),
 \quad \Theta=7/64\ \hbox{admissible},
 \tag{4}
\]
and, for some \(\lambda_0>0\),
\[
 E_h(X)=O_{\lambda_0}((X+h)^{1-\lambda_0}+h).
 \tag{5}
\]
The proof retains \(h^\Theta\); the stronger following prose for \(h\ll X\) is excluded. Remark7.2's suggested \(\lambda_0=1/8\) is not imported as a proved numerical value. Theorem3.3, equation(3.10), and Lemma3.4 give the accompanying spectral expansion and poles, used below. Its constant form contributes zero; all three continuous cusps remain. The printed Laplace theorem has a fixed exponential test, not a growing-test norm assertion.

**Source interface B.** Assing--Humphries, *Spectral fourth moments of Hecke--Maaß cusp forms*, [2607.13518v1](https://arxiv.org/html/2607.13518v1), [primary PDF](https://arxiv.org/pdf/2607.13518v1), [version record](https://arxiv.org/abs/2607.13518). Only v1 is listed, submitted15 July2026; body date24 August2026 is not a second version. No withdrawal is displayed. Its \(r(n)\) is the actual ordered, signed representation count \(r_2(n)\). Theorem1.2 gives, for fixed level \(q\), fixed Heegner point of negative fundamental discriminant \(D\), and an orthonormal Hecke--Maaß basis,
\[
 \sum_{J\le t_\varphi\le2J}|\varphi(z_0)|^4
       \ll_{q,D,\epsilon}J^{2+\epsilon},\quad J\ge1.
 \tag{6}
\]
Theorem1.3 specializes the resulting correlation estimate to all integer \(x,h\ge1\):
\[
 E_h(x)\ll_\epsilon h^\epsilon
 \begin{cases}
 x^{2/3},&h^{3/4+3\theta}\le x,\\
 h^{(1+4\theta)/8}x^{1/2},&h\le x<h^{3/4+3\theta},\\
 h^{(3+4\theta)/8}x^{1/4},&h^{1/2+2\theta}\le x<h,\\
 h^{1/4}x^{1/2},&h^{1/2}\le x<h^{1/2+2\theta},\\
 h^{1/3}x^{1/3},&x<h^{1/2}.
 \end{cases}
 \tag{7}
\]
Here \(\theta=7/64\), a Ramanujan exponent unrelated to \(\theta_{\rm LY}\). The accompanying mean square is printed as
\[
 \sum_{M<h\le2M}|E_h(x)|^2
 \ll_\epsilon x^\epsilon(x^{4/2}M^{1/3}+M^4),
 \qquad1<M^2<x.
 \tag{8}
\]
Both HTML and PDF extraction have \(4/2\), retained literally. The proof's final self-reference to Theorem1.3 apparently means1.2; no stronger formula is silently substituted. Its stated application uses \(q=1,z_0=i\) and \(q=2,z_0=(-1+i)/2\), both \(D=-4\). These fixed parameters are legitimate; variable level/discriminant and arbitrary coefficient families are not.

## 3. Derivation: all costs and one complete sufficient inequality

**Actual smooth blocks.** Choose a fixed smooth nonincreasing \(\phi\), equal to1 on \(x\le1\), zero on \(x\ge2\), and put
\[
 w(x)=\phi(x)-\phi(2x),\qquad
 v_N(x)=(x/N)^{-3/4}\Psi(\sqrt{x/T})w(x/N).
\]
For dyadic integers \(N\ge2\), \(v_N\) is supported in \((N/2,2N)\). For every integer \(n\ge2\),
\(\sum_{N=2,4,\ldots}w(n/N)=1\); for \(n=1\) the sum is zero.
Let \(A_J(N)=(1+N/T)^{-J}\), where \(J\) is any fixed positive integer. The amplitude and all fixed-order scaled derivatives of \(v_N\) are \(O_J(A_J(N))\), with additional fixed-order constants.

Define the zero-extended finite vector and its complete correlations by
\[
 a_n=r_2(n)v_N(n)e(R\sqrt n),\quad
 F_N=N^{-3/4}\sum_n a_n,\quad D_N=\sum_n|a_n|^2,
\]
\[
 C_{N,h}=\sum_n a_{n+h}\overline {a_n}
       =\sum_{n\ge1}r_2(n+h)r_2(n)W_{N,h}(n),
\]
\[
 W_{N,h}(x)=v_N(x+h)\overline {v_N(x)}
             e(R(\sqrt{x+h}-\sqrt x)).
 \tag{9}
\]
The actual overlap is imposed by the two factors, without enlarging an endpoint or removing a phase. Negative shifts are conjugates; \(h=0\) is \(D_N\). On the support of \(W_{N,h}\), both arguments are comparable to \(N\), and
\[
 \Lambda_h=Rh/\sqrt N\asymp Th/\sqrt N,\qquad
 |\partial_x R(\sqrt{x+h}-\sqrt x)|\asymp ThN^{-3/2}.
\]
For \(h<2N\),
\[
 \|W_{N,h}\|_\infty+\operatorname {TV}(W_{N,h})
       \ll_J A_J(N)^2(1+\Lambda_h),
\quad
 \|(N\partial_x)^k W_{N,h}\|_\infty
       \ll_{k,J}A_J(N)^2(1+\Lambda_h)^k.
 \tag{10}
\]
Empty overlaps are exactly zero. If a sharp interval is separately imposed, its jumps cost the endpoint suprema in the variation bound; they are not differentiated as smooth factors.

**Main density and legal Abel remainder.** Stieltjes summation, with \(A_h\) defined using the literal floor, gives the exact identity
\[
 C_{N,h}=M_{N,h}+J_{N,h},\quad
 M_{N,h}=\mathfrak c_h\int_0^\infty W_{N,h}(x)\,dx,\quad
 J_{N,h}=\int_0^\infty W_{N,h}(x)\,dE_h(x).
 \tag{11}
\]
The boundary term vanishes for these compact smooth overlaps; for hard overlaps it must be retained. Extending (7) to real prefix arguments by flooring changes the centered main term by \(O(\mathfrak c_h)\), which is absorbed.

The phase derivative has no zero on a nonempty overlap and is monotone. Integration by parts with the actual amplitude, including its total variation, proves
\[
 |M_{N,h}|\ll_{\epsilon,J}h^\epsilon A_J(N)^2
          \min\{N,N^{3/2}/(Th)\}.
 \tag{12}
\]
For \(N\le T^{3/2}\), even \(h=1\) has \(\Lambda_h\gg T^{1/4}\).
Consequently
\[
 \sum_{1\le h<2N}|M_{N,h}|
       \ll_{\epsilon,J}T^\epsilon A_J(N)^2
                        N^{3/2}T^{-1}\log(2N).
 \tag{13}
\]
The positive arithmetic density is thus paid with its actual oscillatory integral, not discarded.

For \(x\asymp N\) and all nonempty shifts \(h<2N\), (7) implies
\[
 \mathcal E(N,h):=\sup_{x\in[N/2,2N]}|E_h(x)|
 \ll_\epsilon N^\epsilon
       (N^{2/3}+N^{1/2}h^{23/128}).
 \tag{14}
\]
If \(h\le c_0N^{64/69}\), for a sufficiently small fixed \(c_0\), only the first term is needed. For \(h>x\) with \(h,x\asymp N\), the third branch of (7) has the same comparable-scale upper bound as the second; the other branches remain part of the original theorem, not a fixed-\(h\) substitution. Abel gives precisely the admissible upper price
\[
 |J_{N,h}|\ll_{\epsilon,J}
 A_J(N)^2\mathcal E(N,h)(1+Th/\sqrt N).
 \tag{15}
\]
Independently, the coefficient triangle and (12) give
\(|J_{N,h}|\ll T^\epsilon A_J(N)^2N\) in the present \(N\)-range, so (15) can always be capped by that price. The physical correlation has the extra factor \(N^{-3/2}\). Using (5) instead gives
\(A_J(N)^2((N+h)^{1-\lambda_0}+h)(1+\Lambda_h)\), no improvement.

For an ambient interval of \(L\) integer sites containing the vector and any integer \(1\le H\le L\), finite Fejér/Cauchy gives
\[
 |F_N|^2\le \frac{L+H-1}{HN^{3/2}}
 \left[D_N+2\Re\sum_{1\le h<H}(1-h/H)C_{N,h}\right],
 \quad D_N\ll_{\epsilon,J}A_J(N)^2N^{1+\epsilon}.
 \tag{16}
\]
The bracket is nonnegative. The same displayed inequality holds for \(H>L\) after zero extension, with the stated factor.

For \(2\le H\le c_0N^{64/69}\), inserting (12),(15), \(L\asymp N\), gives
\[
 |F_N|^2\ll_{\epsilon,J}T^\epsilon A_J(N)^2
 \left[\frac{N^{1/2}}H+
       \frac{N\log(2H)}{TH}
       +N^{1/6}+THN^{-1/3}\right].
 \tag{17}
\]
At \(N=T^{2/3}\), the last term is \(T^{7/9}H\). Balancing it against the diagonal would require
\(H=N^{5/12}T^{-1/2}=T^{-2/9}<1\).
The legal \(H=1\) estimate is the elementary \(N^{1/2}\) wave-square price; trivial capping restores it, not a saving. The large-shift second term in (14), when summed up to \(H\), adds the upper prices
\[
 T^\epsilon A_J(N)^2
        (H^{23/128}+TN^{-1/2}H^{151/128}).
 \tag{18}
\]
Thus no omitted large-\(h\) complement improves (17). Summing the capped block estimates gives at most the elementary complete complex \(T^{1/4+\epsilon}\) bound. The stronger inherited complete real \(T^{\beta+\epsilon}\) remains unchanged.

The literal mean-square (8) also has a priced legal consequence. For \(M<h\le2M\), \(1<M^2<cN\), smooth overlaps and Minkowski followed by Cauchy in \(h\) give
\[
 \sum_{M<h\le2M}|J_{N,h}|
 \ll_{\epsilon,J}N^\epsilon A_J(N)^2
 (1+TM/\sqrt N)(NM^{2/3}+M^{5/2}).
 \tag{19}
\]
Indeed (8) yields the square-root size \(NM^{1/6}+M^2\), followed by \(\sqrt M\). This does not remove the phase cost. A hard \(h\)-dependent endpoint evaluates errors at differing prefixes; a fixed-prefix mean square alone does not justify that endpoint estimate. One must use (15) there or prove a maximal substitute. No expected replacement \(N^{4/3}\) for printed \(N^{4/2}\) is used.

**What a direct spectral treatment would actually contain.** For \(\Re s\) large, source A defines
\(D_2(s;h)=\sum_{n\ge0}r_2(n+h)r_2(n)(n+h)^{-s}\).
Its non-spectral term is \(\mathfrak c_hh^{1-s}/(s-1)\). The remaining terms in its equation(3.10) are
\[
 2\pi h^{1/2-s}\sum_j\rho_j(h)G(s,it_j)
                         \langle\mathcal V,\mu_j\rangle
\]
and
\[
 \sum_{\mathfrak a}\frac1i\int_{(0)}
 \frac{\pi^{1/2+z}\overline{\varphi_{\mathfrak ah}(1/2-z)}
                         G(s,z)}
 {h^{s-1/2-z}\Gamma(1/2+z)}
 \langle\mathcal V,E_{\mathfrak a}(\cdot,1/2-\bar z)\rangle\,dz,
 \quad
 G(s,z)=\frac{\Gamma(s-1/2+z)\Gamma(s-1/2-z)}{\Gamma(s)^2}.
 \tag{20}
\]
Here \(\mathcal V\) is the paper's square-integrable regularization of
\(y|\theta^2|^2\). All three cusps are retained. Lemma3.4 excludes exceptional poles to the right of \(1/2\) at this fixed level4; the discrete poles on \(1/2\) remain, and further contour motion requires all continuous residual terms. This is not a license to discard exceptional spectra at arbitrary varying levels. A special unweighted shift average in that paper is not the coupled \(h,R,N\) test in (9).

For \(q_h(y)=W_{N,h}(Ny-h)\), let
\(\widehat q_h(s)=\int_0^\infty q_h(y)y^{s-1}\,dy\). With the \(n=0\) term explicitly subtracted, Mellin inversion gives
\[
 J_{N,h}=\frac1{2\pi i}\int_{(\sigma)}
 N^s\widehat q_h(s)
 \left[D_2(s;h)-r_2(h)h^{-s}
              -\frac{\mathfrak c_hh^{1-s}}{s-1}\right]\,ds,
 \quad \sigma>1\ \hbox{sufficiently large}.
 \tag{21}
\]
The atom has zero transform in this application because \(W_{N,h}(0)=0\). Formula(21), rather than an uncentered Laplace sum, is the source-normalized oscillatory remainder.

The exponential test in (4) supplies \(\Gamma(s)\) with exponential vertical decay. Our test does not. For fixed \(\sigma\) and \(a\ge0\), smooth fixed-support Fourier estimates in \(\log y\) prove
\[
 \int_{\mathbb R}(1+|\tau|)^a
       |\widehat q_h(\sigma+i\tau)|\,d\tau
 \ll_{a,J,\sigma} A_J(N)^2(1+\Lambda_h)^{a+1/2}.
 \tag{22}
\]
For completeness, split at \(1+\Lambda_h\), use Plancherel and Cauchy on the central interval, and use a fixed integer number \(b>a+1/2\) of derivatives on successive outer dyadic intervals. Equation(10) bounds those derivative norms and the resulting geometric series gives (22). This is an upper price, not a lower bound on the transform or signed integral. Sharp jumps require the separately paid Abel treatment, not this smooth estimate.

Stirling's exponential factor in \(G(\sigma+i\tau,it)\) is
\(\exp[-\pi(\max(|\tau|,|t|)-|\tau|)]\); it does not suppress
\(|t|\le|\tau|\). Actual spectral heights can therefore reach
\(\Lambda_h\), up to order \(T\sqrt N\). The \(J^{2+\epsilon}\) in (6) cannot be replaced by a constant; nor can a Heegner value fourth moment be inserted for \(\langle\mathcal V,\mu_j\rangle\) without the requisite identity. The legally available bridge from source B is its printed (7).

Even **hypothetically** granting a remainder bound
\(h^\Theta(1+|\tau|)^a\) uniformly on \(\Re s=1/2+\epsilon\), an absolute contour transfer would pay
\(N^{1/2+\epsilon}h^\Theta A_J(N)^2(1+\Lambda_h)^{a+1/2}\).
For the optimistic \(a=0\), at \(N=T^{2/3}\) this certificate is already
\(A_J(N)^2Nh^{\Theta+1/2}\). The hypothesis and any smaller signed transfer remain unproved. No absolute certificate is asserted to lower-bound the actual oscillatory sum.

**One complete next inequality, with exact reconstruction.** Take \(H=2N\) and the ambient integer interval
\(\{N/2+1,\ldots,2N-1\}\), of length \(L_N=3N/2-1\). Retain **every**
\(1\le h<H\), including identically zero nonoverlap terms. Define
\[
 \boxed{\mathcal R_{T,N}(R)=
 2\Re\sum_{h=1}^{2N-1}(1-h/(2N))
 \int_0^\infty W_{N,h}(x)\,d(A_h(x)-\mathfrak c_hx).}
 \tag{23}
\]
Equivalently, insert (21) into (23), summing the complete bracket over \(h\) **inside** the contour integral before any modulus. This specifies the main-minus-density expression and all coefficients in the proposed direct spectral problem.

The proposed sufficient estimate is the one-sided assertion
\[
 \boxed{\mathcal R_{T,N}(R)
 \le C_{\epsilon,J}T^\epsilon A_J(N)^2N^{3/2}}
 \tag{24}
\]
for every dyadic \(2\le N\le T^{3/2}\), every real \(cT\le R\le CT\), and every fixed \(J\). It is unproved. There is no restriction to the \(h\le N^{64/69}\) range of the first branch in (7).

The exact Fejér prefactor is
\[
 \frac{L_N+2N-1}{2N\,N^{3/2}}.
\]
Using (13), the diagonal bound in (16), and (24) gives
\[
 |F_N|^2\ll_{\epsilon,J}T^\epsilon A_J(N)^2
       [N^{-1/2}+T^{-1}\log(2N)+1].
 \tag{25}
\]
Only an upper bound on the signed remainder is needed; no assertion of its positivity is made. The total original Fejér bracket remains nonnegative.

Let \(N_*\) be the largest dyadic integer at most \(T^{3/2}\); then
\(T^{3/2}/2<N_*\le T^{3/2}\). Telescoping gives
\(\sum_{2\le N\le N_*}w(n/N)=\phi(n/N_*)\) for integer \(n\ge2\).
The omitted coefficient factor \(1-\phi(n/N_*)\) vanishes for \(n\le N_*\) and is bounded by1. Thus the remainder begins at \(n>N_*\), which can be below \(T^{3/2}\), but remains a far tail. For any fixed \(D\), \(r_2(n)\ll_\eta n^\eta\) and Schwartz decay give
\[
 \sum_{n>N_*}r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|
 \ll_{\eta,D}T^{D/2}N_*^{1/4+\eta-D/2}
 \ll_{\eta,D}T^{3/8+3\eta/2-D/4}.
 \tag{26}
\]
This is arbitrarily small after choosing a fixed \(D\). The separate \(n=1\) term is \(O(1)\). Summing the square-root bound (25) over \(O(\log T)\) blocks proves the complete complex wave \(\ll T^\epsilon\), after rescaling \(\epsilon\); taking its real part with the fixed rotation \(e(-3/8)\) proves (1), and (2) gives the quarter goal. No interval gaps, averaged radii or unpriced tail occur.

## 4. First doubtful or unproved step

The first failed import is the replacement of a fixed Laplace or unweighted sharp theorem by a uniform theorem for \(W_{N,h}\) without its growing phase/test norms. Equations(10),(15),(17),(22) display the missing costs. Source B improves the unweighted error but not its absolute oscillatory transfer enough.

For the proposed next question, the first unproved statement is exactly (24), or an equivalent joint estimate for the complete \(h\)-sum in (21),(23). Neither separating every shift, replacing the coupled transform by an arbitrary bounded weight, ignoring spectral heights, nor retaining only the density establishes it. The new current arithmetic input is (6) and its actual-\(r_2\) application (7); it makes a direct joint spectral investigation more concrete, but is not itself that investigation or a gain.

The source-print discrepancies have been conservatively fenced off: no free deletion of \(h^\Theta\) from (4), no numerical sharp exponent from a preliminary remark, no replacement of \(4/2\) by \(4/3\), and no invented newer AH version.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Current primary versions | Official records, exact-version HTML and PDF text checked for the two works. PDF visual screenshots were unavailable; no visual verification is claimed. No withdrawal displayed. |
| Actual coefficients | Both correlation interfaces use \(r_2\), with normalization(3). They do not estimate GAR's angular-divisor coefficients or arbitrary cusp coefficients. |
| Every real radius and growing shift | All costs use \(cT\le R\le CT\) without arithmetic restrictions. Proposed(24) keeps every \(h<2N\); all branches of(7) and the large-shift complement are recorded. |
| Main, diagonal, zero and negative shifts | Density is(12)--(13); diagonal is(16); negative shifts are conjugates, \(h=0\) is not passed to a positive-shift theorem. Empty overlaps and \(H=1\) are valid. |
| Smooth tests and endpoints | Literal smooth overlap in(9); fixed derivative constants with growing \(\Lambda_h\). Sharp endpoints require explicit boundary costs. Fixed-prefix mean square is not a maximal endpoint theorem. |
| Spectral completeness | All three continuous cusps, discrete coefficients, gamma factors, and residual terms are retained. The fixed-level absence of exceptional poles is not extrapolated. Source B's real high spectral band does not by itself handle arbitrary imaginary spectrum. |
| Arithmetic masks | Squarefree-class deletion is not smooth. The closed221 report prices the physical correlation correction by \(T^\epsilon A_J(N)^2Q^{1/2}N^{-1}\), restoring a wave-square price \(Q^{1/2}\), hence amplitude \(Q^{1/4}\). No masked source theorem is inferred. Candidate(24) uses the complete unmasked wave and needs no such deletion. |
| Real versus complex | \(\Re(e(-3/8)F_N)^2=(|F_N|^2-\Im F_N^2)/2\). Bounding by \(|F_N|^2\) is an explicit stronger enlargement. Neither inherited real \(\beta\) nor average correlation results imply a complex block bound. |
| Complete reconstruction | Exact overlapping partition, every dyadic scale, singleton and tail in(26). A power \(T^\gamma\) for the complete real wave restores circle exponent \(1/4+\gamma/2\). |
| Actual versus certificate | Failure/size of the upper prices in(17)--(22) is not a lower bound on \(J_{N,h}\), \(\mathcal R_{T,N}\), or \(B_T\). No new positive-certificate obstruction is claimed. |
| Statement-only control | This source role is selected-context and nonblind. It supplies no purported independent statement-only certification; that campaign control belongs to the conductor's separate assignment. |
| Computation | Zero experiments. All transfer and restoration calculations above are analytic. |

The complete frontier is preserved. M1 HARD still requires the entire actual \(\chi_4\) cone at \(L^{3/2}\), including small-\(t\)/large-\(G\); M1 SMOOTH requires every literal physical block at \(X^{1/4+\epsilon}\). M2 TOP retains its hard endpoint or accepted outer-real-energy bridge; BAL requires all \(G P_G\), both quarter shifts and companions; UNBAL requires the actual \(\chi_4\) sum at \((LK)^{3/4}\) throughout \(K/L>16\), with the physical restoration \(X^{1/4}(LK)^{-3/4}\). Total-M1 GAR uses its actual angular-divisor coefficient and lower scales, and alone leaves M2/endpoints open. This audit discharges none of those owners. A proved whole-wave(24) would instead prove the discrepancy target directly.

Accepted204 still gives, with the complete high-value distribution,
\[
 D(V)\ll T^\epsilon(V^{-2}+TV^{-136/13}),\qquad
 M_p(B_T)\ll_{p,\epsilon}T^{1+\epsilon}+T^{(p-2)\beta+\epsilon}.
\]
For \(p>136/13\), layer cake above1 through a ceiling \(W\) retains both
\(W^{p-2}\) and \(TW^{p-136/13}\); lower orders and the equality logarithm are not obtained by dropping a term. No source here changes either contribution.

Accepted216 still has \(Q=\lfloor T^{2/5}\rfloor\), head twelfth moment \(T^{15/13+\epsilon}\), and repeated-class error \(T^{8\beta-1/5+\epsilon}\). The one-sided distinct target \(I_{12}\le T^{29/25+\epsilon}\) is unproved and yields only \(102/325\). An unbounded sequence of **fixed** even orders with \(Q_p=\lfloor T^{1/p}\rfloor\), \(I_p\le T^{5/4+\epsilon}\), and the established same-order absorption suffices for eventual quarter; every intermediate order is unnecessary, but uniform constants for \(p=p(T)\) are not granted. The associated pointwise exponents \(1/4+7/[8(p+1)]\) tend to quarter; complete \(M_p\ll T^{1+\epsilon}\) would give \(1/4+3/[4(p+1)]\). The current sources supply neither family. The five accepted Li--Yang source repairs and benchmark remain intact.

## 6. Dependencies, exact artifacts and provenance

This reusable agent retains rounds217--225 context and authored previous source, finite-seam and attack/review reports, including the round224 prime attack and round225 nonlinear-prime attack. That history is disclosed; it is not newly independent evidence. Only the present brief's authorized context and the two primary works were accessed for this assignment. No current sibling, blind packet, root control, review or synthesis was read. No external cited precursor of these two works was imported as a third audit.

The following local hashes bind this report's permitted context; prior acceptance remains the graph's decision. Prior reports are evidence, not independent theorem grants.

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 3f136e86091b999d4abf7db0b2141f4bced2e80480ee90a360c319c48b6e0d92 |
| strategy/round226_full_goal_spectral_source_review.md | 61ac5c2a26bf87f25133d8858dd2b4a0c6e377df657ddaeaa57d422d41e287ad |
| strategy/gauss_circle_strategy_review_2026-09-23.md | 0729f1d9c596867e7a06bdcd096847b32e6747653235706b01275a153bd617c6 |
| strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md | a0c75c5e2ef4ea45df4e388e3497d5be5133d6d49c7d7a2d71c166f11dd9dd33 |
| briefs/actual_shifted_spectral_sources.md, current campaign | 67a2941a4aab2fdbf3fc71a9225446d74173da2fea3ce32e1deeca39c2fb609a |
| briefs/conductor_complete_spectral_interfaces.md, current campaign | 8e9cb720ca0495aafc003434877dcd0067779993fc1edd5657b93d35ef9e77e5 |
| rounds/codex-managed/gc-complete-logarithmic-convolution/synthesis.md | c4324e2b8c75b8cb972ccf6a9e4f762ed9d8d648299acf7df77aff2b9b1546c7 |
| rounds/codex-managed/m9-m1-complete-gar-prime-amplification/synthesis.md | d5a94b25e876714c8e17602a497812afef3b42724a75dd4cc1501583d12fe98f |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| rounds/codex-managed/gc-actual-vector-gram-correlations/synthesis.md | 93413bbc466cd48bc9fe4ebeede40c62bb218bb077f8afda1750c23805fb05dd |
| rounds/codex-managed/gc-actual-vector-gram-correlations/reports/actual_shifted_correlations.md | 6e0c9a229fa81d37c137c87197e66d2bfc6eddc4bb231f8eef256f51bf9fdbca |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |

Primary citation binding is the exact-version URLs in Section2, not an unversioned search snippet. Theorem statements were audited for applicability and their transfer was independently derived; the full spectral proofs and the precursors invoked by source B were not re-proved. No source card or shared acceptance file was modified.

## 7. Recommended state effect

**Retain** the current actual-\(r_2\) source interfaces as candidate source evidence, with the literal discrepancies and all parameter costs recorded. **Reject** the free oscillatory-test import, the deleted-\(h^\Theta\) improvement, an unprinted \(4/3\) mean-square exponent, and any claimed current gain for the complete wave or moments.

**No change** to the accepted benchmark, full quarter status, M1/M2/GAR owners, or moment obligations. The one recommended complete quantitative question for conductor consideration is (24), exactly as centered and summed in (23), retaining its whole spectral expression(21) before moduli. Its implication is proved here; the inequality itself is not. It is motivated by the actual-coefficient fixed-CM spectral input, not an assertion that this input already controls the joint transform. Selection or a successor attempt belongs solely to the conductor. Stop after freezing this report.

