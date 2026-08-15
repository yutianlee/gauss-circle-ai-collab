## 1. Result

The Poisson identity (64.4), including its sign, factor \(2T\), and unchanged \(j\)-cutoff, is exact. The all-moment assertion (64.6) is also exact. The corrected cutoff \(\Xi\in C_c^\infty((0,1))\) makes the primal sum finite and removes the collision \(j=\sqrt X\) from this interior piece.

The support assertion needs one qualification. On the primal side there is genuine compact support, and in fact the fixed cutoff gives the stronger relations \(j\asymp\sqrt X\) and \(h\asymp\sqrt N\). On the Poisson side, however, \(\widehat g\) is generally not compactly supported. Thus \(m\asymp X/j\) and \(|jm-X|\lesssim T\) describe rapid localization, not exact support; \(m\leq0\) terms are generally nonzero but are smaller than every power of \(X\).

These facts do not imply (64.2). They give an exact short product-wavelet reduction with a moving, truncated character-divisor coefficient, but no supplied fact bounds its correlation with the wavelet by \(X^{1/4+\varepsilon}\). Hence the result is an exact reduction plus a scoped no-go, not a new radial interval.

## 2. Exact statement and hypotheses

Assume \(X>1\), \(N=X^\nu\), \(0<\nu\leq2/5\), \(T=\sqrt{X/N}\), and \(V\in C_c^\infty((0,\infty))\), \(\Xi\in C_c^\infty((0,1))\). Choose constants

\[
 0<a<b<\infty,\qquad 0<\alpha<\beta<1
\]

such that \(\operatorname{supp}V\subset[a^2,b^2]\) and \(\operatorname{supp}\Xi\subset[\alpha,\beta]\). Put \(K=\widehat g\), with \(g\) as in (64.3). Then

\[
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{j\geq1}\chi_4(j)\Xi(j/\sqrt X)
   \sum_{m\in\mathbb Z}K\!\left(\frac{jm-X}{2T}\right).
 \tag{2.1}
\]

Every nonzero primal summand satisfies the exact endpoint bounds

\[
 \alpha\sqrt X\leq j\leq\beta\sqrt X,
 \qquad \frac{aj}{2T}\leq h\leq\frac{bj}{2T}.
 \tag{2.2}
\]

Consequently \(j\asymp\sqrt X\), \(h\asymp\sqrt N\), and \(j\asymp Th\). For every \(A\geq0\),

\[
 |K((jm-X)/(2T))|
 \ll_{A,V}\left(1+\frac{|jm-X|}{T}\right)^{-A}.
 \tag{2.3}
\]

Thus the claimed dual geometry is effective localization only.

For \(n\geq1\), define the moving truncated incidence

\[
 A_{X,\Xi}(n)
 :=\sum_{j\mid n}\chi_4(j)\Xi(j/\sqrt X).
 \tag{2.4}
\]

Then the exact nearest-product form is

\[
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{n\geq1}A_{X,\Xi}(n)
   K\!\left(\frac{n-X}{2T}\right)+E_{\leq0},
 \tag{2.5}
\]

where

\[
 E_{\leq0}
 :=\sum_{j\geq1}\chi_4(j)\Xi(j/\sqrt X)
   \sum_{m\leq0}K\!\left(\frac{jm-X}{2T}\right)
 \ll_{B,V,\Xi}X^{-B}
 \tag{2.6}
\]

for every \(B>0\). Finally,

\[
 \int_{\mathbb R}\xi^rK(\xi)\,d\xi=0
 \qquad(r=0,1,2,\ldots).
 \tag{2.7}
\]

## 3. Proof or derivation

Because \(V\) is compactly supported away from zero, the extension defining \(g\) is in \(C_c^\infty(\mathbb R)\), is zero on a neighborhood of zero, and is therefore Schwartz. With \(H_j=j/(2T)\), direct substitution gives

\[
 \frac1{H_j}g(h/H_j)
 =\frac1hV\!\left(\frac{4T^2h^2}{j^2}\right)
 =\frac1hV\!\left(\frac{4Xh^2}{j^2N}\right).
\]

The summand vanishes for every integer \(h\leq0\), so the \(h\)-sum may be extended to all of \(\mathbb Z\). For

\[
 f_j(x)=H_j^{-1}g(x/H_j)e(Xx/j),
\]

the stated Fourier convention gives

\[
 \widehat f_j(m)
 =\int_{\mathbb R}g(t)e((X/j-m)H_jt)\,dt
 =K\!\left(H_j(m-X/j)\right)
 =K\!\left(\frac{jm-X}{2T}\right).
\]

Poisson summation \(\sum_{h\in\mathbb Z}f_j(h)=\sum_{m\in\mathbb Z}\widehat f_j(m)\) proves (2.1). The factor \(\Xi(j/\sqrt X)\) is independent of \(h\), so it passes through Poisson unchanged. Its compact support leaves only finitely many \(j\), and hence no interchange issue occurs.

The endpoint relations (2.2) follow directly from the supports of \(\Xi\) and \(V\). In particular \(\beta<1\) gives a fixed gap from \(j=\sqrt X\); this identity owns no saddle-collision term. Since \(K\) is Schwartz, (2.3) follows. It also shows why the displayed dual window is not literal support.

For \(m=-k\leq0\), \(|jm-X|=X+jk\). Using \(j\asymp\sqrt X\), \(X/T=\sqrt{XN}\geq\sqrt X\), and Schwartz decay, for \(A>1\) one has

\[
 \sum_{j\asymp\sqrt X}\sum_{k\geq0}
 \left(1+\frac{X+jk}{T}\right)^{-A}
 \ll \sqrt X\left\{(X/T)^{-A}
       +\frac{T}{\sqrt X}(X/T)^{1-A}\right\}.
\]

Taking \(A\) arbitrarily large proves (2.6), including the zero-product term \(m=0\). For \(m\geq1\), regrouping the absolutely convergent sum by \(n=jm\) gives (2.4)--(2.5). This coefficient must not be replaced by \(r_2(n)/4\): the factor \(\Xi(j/\sqrt X)\) retains only a moving subset of the divisors.

Fourier inversion and differentiation at zero give

\[
 g^{(r)}(0)=\int_{\mathbb R}(2\pi i\xi)^rK(\xi)\,d\xi.
\]

Every derivative of \(g\) at zero vanishes, proving (2.7). This continuous moment identity does not say that \(K(0)=0\). Indeed

\[
 K(0)=\int_0^\infty\frac{V(t^2)}t\,dt
 =\frac12\int_0^\infty\frac{V(u)}u\,du,
\]

which is generally nonzero. Hence, when \(X\) is an integer, the exact products contribute

\[
 K(0)A_{X,\Xi}(X)
 =K(0)\sum_{j\mid X}\chi_4(j)\Xi(j/\sqrt X)
\]

and are not killed by (2.7).

The direct primal absolute ledger is

\[
 \sum_{j\asymp\sqrt X}\sum_{h\asymp j/T}\frac1h
 \ll\sqrt X.
\]

The product form improves the unconditional absolute ledger, since \(|A_{X,\Xi}(n)|\ll_\Xi d(n)\), \(d(n)\ll_\varepsilon n^\varepsilon\), and (2.3) yield

\[
 \sum_{n\geq1}|A_{X,\Xi}(n)|
 \left|K\!\left(\frac{n-X}{2T}\right)\right|
 \ll_{\varepsilon,V,\Xi}T X^\varepsilon
 =X^{1/2-\nu/2+\varepsilon}.
 \tag{3.1}
\]

The requested \(X^{1/4+\varepsilon}\) therefore still needs a factor \(X^{1/4-\nu/2}\) beyond (3.1), which is at least \(X^{1/20}\) throughout \(0<\nu\leq2/5\). Relative to the original \(X^{1/2+o(1)}\) ledger, the requested gain is \(X^{1/4}\). After multiplication by the external factor \(2X^{-1/4}e(-1/8)\), (64.2) would give an \(O(X^\varepsilon)\) normalized contribution; no extra \(X^{\pm1/4}\) is available inside (2.1).

## 4. First doubtful or unproved step

The first missing step is the coefficient-preserving short-product estimate

\[
 \boxed{
 \left|\sum_{n\geq1}
 \left(\sum_{j\mid n}\chi_4(j)\Xi(j/\sqrt X)\right)
 K\!\left(\frac{n-X}{2T}\right)\right|
 \ll_{\varepsilon,V,\Xi}X^{1/4+\varepsilon}.}
 \tag{4.1}
\]

Neither the continuous identities (2.7) nor the mean-zero period-four character proves (4.1). The coefficient \(A_{X,\Xi}(n)\) is arithmetic, nonsmooth in \(n\), and depends on \(X\) through a divisor cutoff. Thus there is no justified Taylor expansion against which all moments can be applied.

There is a direct countermodel to the overstrong claim that all zero moments plus a window of length \(T\) force the target. Suppose \(V\not\equiv0\), so \(K\not\equiv0\). Choose a compact interval \(I\) and \(c>0\) on which \(|K(u)|\geq c\). For integers \(n\) with \(u_n=(n-X)/(2T)\in I\), set

\[
 a_X(n)=\frac{\overline{K(u_n)}}{|K(u_n)|},
\]

and set \(a_X(n)=0\) otherwise. Then \(|a_X(n)|\leq1\), all the moment identities of \(K\) remain true, but

\[
 \sum_n a_X(n)K((n-X)/(2T))
 =\sum_{u_n\in I}|K(u_n)|\gg T.
\]

Since \(T=X^{1/2-\nu/2}\geq X^{3/10}\), this violates an \(X^{1/4+\varepsilon}\) conclusion for small enough \(\varepsilon\). It does not refute (4.1) for the actual coefficient; it proves that an arithmetic decorrelation input is indispensable. Likewise, periodicity alone gives no bound: an abstract inner sequence proportional to \(\chi_4(j)\overline{\Xi(j/\sqrt X)}\) makes the outer character sum have size \(\asymp\sqrt X\). Control of the actual inner wavelet sequence, not the character's mean in isolation, is the missing content.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Poisson normalization and sign | Passed: \(\widehat f_j(m)=K((jm-X)/(2T))\); neither the sign nor the factor \(2T\) changes. |
| Cutoff ownership | Passed for the corrected packet: \(\Xi(j/\sqrt X)\) remains exactly outside the \(m\)-sum and makes the \(j\)-sum finite. |
| Support endpoints and saddle collision | Primal support is exactly (2.2). The fixed \(\beta<1\) excludes \(j=\sqrt X\). Dual "support" is only Schwartz localization and should be stated that way. |
| Negative \(m\) and zero product | They are not identically zero; their complete contribution is \(O_B(X^{-B})\) for every \(B\). |
| Exact versus near products | Positive \(m\) gives the exact coefficient (2.4). If \(X\in\mathbb Z\), \(n=X\) survives with \(K(0)A_{X,\Xi}(X)\); other \(n\) are near products on scale \(T\), with rapid tails. |
| All moments | Passed as ordinary absolutely convergent integrals. They are continuous moments, not identities for the sampled arithmetic convolution. |
| Cutoff commutators | There is none in the \(h\)-Poisson step. After \(n=jm\), however, the cutoff lives inside \(A_{X,\Xi}(n)\); it cannot be pulled through a divisor pairing or replaced by a full divisor sum. |
| Period-four pairing | No automatic cancellation. The involution \(j\leftrightarrow n/j\) changes \(\Xi(j/\sqrt X)\); near \(n=X\), the partner of an interior \(j<\sqrt X\) lies above \(\sqrt X\) and is not owned by this cutoff. |
| Perfect-square/fourth-power coherence | If \(X=q^2\), the central pair \((j,m)=(q,q)\) has \(\Xi(1)=0\); if \(X=q^4\), the central pair \((q^2,q^2)\) is likewise excluded. Noncentral exact divisor pairs remain and need not cancel. |
| Target power | The target is \(X^{1/4}\) before the external \(X^{-1/4}\). The exact reduction alone gives only (3.1), not (4.1). |
| Near-product/PSC comparison | The isolated packet supplies no PSC formula to compare against. The auditable normalization produced here is precisely \(K((n-X)/(2T))\) with coefficient (2.4); any claimed comparison must match this sign, scale \(2T\), and moving cutoff. |
| Imported theorem hypotheses | No short-divisor, shifted-convolution, spectral, or other external theorem was imported, so there is no source claim to promote. |
| Full-cone implication | Failed: even (4.1) for this fixed interior \(\Xi\) would not control the sharp \(j\leq\sqrt X\) owner, subtraction, negative-frequency terms, or stationary entry/exit pieces listed in the packet. |

## 6. Dependencies and exact artifacts used

The derivation uses only elementary Poisson summation with the Fourier convention stated in the packet, Fourier inversion for a Schwartz function, Schwartz decay, and the standard pointwise divisor bound \(d(n)\ll_\varepsilon n^\varepsilon\).

**Strict isolation ledger.** I read exactly these repository content files:

1. `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/derivation_packet.md` (first before, and then after, the coordinator's announced \(\Xi\in C_c^\infty((0,1))\) correction; the corrected version is the sole mathematical input used here).
2. `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/briefs/blind_product_wavelet_rederivation.md`.

I did not read the protocol, claim graph, state files, prior rounds, prior syntheses, other briefs, or any Round-64 report. I used no web source and no numerical or symbolic experiment. Apart from a metadata existence check on the assigned destination, I inspected no other repository path. This report is the only file edited.

## 7. Recommended state effect

**Promote, scoped:** (2.1), the exact positive-product reduction (2.5), the all-moment identity (2.7), and the superpolynomial disposal of \(m\leq0\) are suitable exact lemmas for the fixed smooth interior cutoff.

**Revise:** describe (64.5) as exact primal support plus effective dual localization; with fixed \(\Xi\in C_c^\infty((0,1))\), record the stronger \(j\asymp\sqrt X\), \(h\asymp\sqrt N\), and the fixed separation from the saddle collision.

**Retain/reject implication:** retain (4.1) as an open arithmetic obligation and reject any inference of (64.2) from zero moments or period-four mean alone. Make no exponent change and no full-cone promotion without separate subtraction, transition, boundary, negative-frequency, and recombination controls.
