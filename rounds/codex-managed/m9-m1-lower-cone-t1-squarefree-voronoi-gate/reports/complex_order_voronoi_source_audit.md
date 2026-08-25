# Round 147 complex-order level-four Voronoi source audit

## 1. Result

**Source verdict: the fixed-shift complete transform is derivable with the correct conductor, pole, and all three Bessel species, but no audited theorem gives the growing-order estimate or the signed squarefree-convolution estimate needed by the exact scalar.** At graph SHA-256

```text
1dc79cf41e0dea8888341e944c5d0bf025d87f22cfaa282da34fcd10eecd04f5
```

put

\[
 A_z(n)=\sum_{de=n}\chi _4(e)(e/d)^z
       =n^{-z}\sigma _{2z,\chi _4}(n)
       =n^z\bar\sigma _{-2z,\chi _4}(n).
\tag{147.1}
\]

Banerjee--Khurana Theorem 4.3, specialized with \(q=4\), \(\nu=2z\), and its test \(f(x)=x^{z+1}F(x)\), gives the exact identity

\[
\begin{aligned}
 \sum_{n\ge1}A_z(n)F(n)
  ={}&L(1-2z,\chi _4)\int_0^\infty F(x)x^{-z}\,dx \\
  &+\pi4^z\sum_{n\ge1}\sigma _{-2z,\chi _4}(n)n^z
       \int_0^\infty F(x)\,
       \mathcal B_{2z}(2\pi\sqrt{nx})\,dx,
\end{aligned}
\tag{147.2}
\]

where

\[
 \mathcal B_\nu(y)=
 \left(\frac2\pi K_\nu(y)-Y_\nu(y)\right)\sin\frac{\pi\nu}{2}
 +J_\nu(y)\cos\frac{\pi\nu}{2}.
\tag{147.3}
\]

The source states (147.2) for an analytic test on a finite interval, nonintegral endpoints, and \(0<\Re z<1/4\). Mellin inversion of the same completed \(\zeta(s+z)L(s-z,\chi _4)\) functional equation extends it to \(F\in C_c^\infty(0,\infty)\) for each fixed \(z\) in that strip. Thus the analytic-versus-smooth mismatch is removable at the identity level; it is not the first surviving obstruction.

The exact conductor-four Bessel argument is \(2\pi\sqrt{nx}\), so its two oscillatory branches are \(e(\pm\sqrt{nx})\). Against the individual physical direction \(e(+\sqrt{Nx})\), the negative branch resonates at \(n=N\), not \(N/4\). After the squarefree Euler convolution indexed by \(k\), the centre and width are

\[
 n=kN+O\!\left(k\sqrt{N/M}\right).
\tag{147.4}
\]

The first exact **source-hypothesis gap** is uniformity of (147.2)--(147.3), including derivatives and transition ranges, for \(|\Im z|\lesssim D^{1/2}X^\varepsilon\) after the legal cone collar (and \(|\Im z|\gtrsim D\) for the hard cone). Banerjee--Khurana is a fixed-parameter identity and states no such estimate.

The first independent **power gap**, even granting the most favorable uniform transform, is signed aggregation over the exact Euler correction. Termwise Voronoi followed by the optimal elementary split gives the normalized all-block loss

\[
 \min\!\left\{M^{1/4},\;N^{1/8}M^{-1/8}\right\}X^\varepsilon,
\tag{147.5}
\]

which peaks at \(M=N^{1/3}=R^{4/3}\) with \(N^{1/12}=R^{1/3}\); at \(M\asymp R^2\) it still loses \(R^{1/4}\). This is a limitation of this absolute-value placement, not an impossibility theorem for the signed scalar.

A useful further exact refactorization is

\[
 H(w,z)=
 \frac{K(w,z)}{\zeta(2w+2z)\zeta(2w-2z)L(2w,\chi _4)}.
\tag{147.6}
\]

It exposes three signed square-supported Möbius factors and a cubically convergent remainder. It suggests a mathematically distinct signed square-convolution inequality. It does **not** license a uniform shift of a \(w\)-contour below \(1/2\): reciprocals of the three degree-two factors have poles at zeros of the corresponding \(\zeta\)- or \(L\)-function, and no audited zero-avoidance or residue theorem controls the growing Mellin heights. This is a method limitation, not a theorem that the target estimate is false.

## 2. Exact statement and hypotheses

### Exact target

For \(R=X^{1/4}\), \(N=\lfloor X\rfloor\), and every inherited half-open prefix \(M\le U\le B_M\le2M\), the mandatory face is reduced by partial summation to

\[
 \sup_{M\le U\le B_M}
 \left|\sum_{\substack{M\le s<U\\ \mu^2(s)=1}}
 V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns})\right|
 \ll_{\varepsilon,V}M^{3/4}X^\varepsilon,
\tag{147.7}
\]

where

\[
 C(s)=\sum_{\substack{de=s\\e\ {\rm odd},\ e>4d}}\chi _4(e).
\tag{147.8}
\]

All statements below retain fixed \(N\), the individual positive direction, squarefreeness, parity, the strict cone or its proved collar, the profile, and the clipped prefix.

Whenever the source strip is used, choose \(z=c+iv\) with \(0<c<1/4\) sufficiently small in terms of the requested \(\varepsilon\). Then factors such as \(n^c\), \(k^c\), and dyadic ratio powers are absorbed in \(X^\varepsilon\). No estimate below silently takes the excluded endpoint \(c=0\).

### Exact ratio factor and coefficient

Before the cone is imposed,

\[
 Z(w,z)=\sum_{d,e\ge1}
 \frac{\mu^2(de)\mathbf1_{e\ {\rm odd}}\chi _4(e)}
      {d^{w+z}e^{w-z}}
 =\zeta(w+z)L(w-z,\chi _4)H(w,z).
\tag{147.9}
\]

The scalar \(4^{-z}\) belonging to the ratio \(e/(4d)\) remains outside (147.9). At \(2\),

\[
 H_2=1-2^{-2w-2z}.
\tag{147.10}
\]

At an odd prime, put \(a=p^{-w-z}\), \(b=\chi _4(p)p^{-w+z}\). Then

\[
 H_p=(1+a+b)(1-a)(1-b)
 =1-a^2-b^2-ab+a^2b+ab^2.
\tag{147.11}
\]

Consequently \(H\) is absolutely convergent for

\[
 \Re(w+z)>\frac12,\qquad \Re(w-z)>\frac12.
\tag{147.12}
\]

Writing \(H(w,z)=\sum h_z(k)k^{-w}\), the local coefficients are exactly

\[
\begin{array}{lll}
 h_z(2^2)=-2^{-2z}, & h_z(2^j)=0 &(j\ne0,2),\\[2mm]
 h_z(p^2)=-(p^{-2z}+p^{2z}+\chi _4(p)),
 &h_z(p^3)=p^z+\chi _4(p)p^{-z},
 &h_z(p^j)=0\ (j\ne0,2,3)
\end{array}
\tag{147.13}
\]

for odd \(p\). Thus \(h_z\) is multiplicative and supported on integers whose prime exponents are all \(2\) or \(3\), in particular on powerful integers. For \(z=c+iv\), fixed \(0<c<1/4\),

\[
 |h_z(k)|\ll_\varepsilon k^{c+\varepsilon},
 \qquad \#\{k\le K:h_z(k)\ne0\}\ll_\varepsilon K^{1/2+\varepsilon},
\tag{147.14}
\]

uniformly in \(v\). These facts do not give an unweighted physical \(\ell^1\) bound.

### Primary theorem card and exact specialization

The primary source is D. Banerjee and K. Khurana, *Character analogues of Cohen type identities and related Voronoi summation formulas*, arXiv:2306.12399v2, equation (5.11) and Theorem 4.3. Its hypotheses are:

- \(\chi\) is an odd primitive character modulo \(q\);
- \(0<\alpha<\beta\) are nonintegers;
- the test \(f\) is analytic inside a closed contour containing \([\alpha,\beta]\);
- \(0<\Re\nu<1/2\).

Its coefficient is \(\bar\sigma_{-\nu,\chi}(j)/j\); its dual coefficient is \(\sigma_{-\nu,\bar\chi}(n)n^{\nu/2}\); and its kernel is (147.3) at \(4\pi\sqrt{nt/q}\). It states an exact identity for fixed \(\nu\), not a quantitative theorem uniform as \(|\Im\nu|\to\infty\).

For \(\chi=\chi _4\), \(q=4\), \(\tau(\chi _4)=2i\), \(\nu=2z\), and \(f(x)=x^{z+1}F(x)\), its left side becomes (147.1), the main integrand becomes \(F(x)x^{-z}\), and the dual integrand becomes exactly \(F(x)\). Its scalar is

\[
 -2\pi i\,\tau(\chi _4)4^{z-1}=\pi4^z,
\tag{147.15}
\]

which proves the normalization in (147.2). There is one polar term because \(\zeta(s+z)\) has its pole at \(s=1-z\), while the primitive nonprincipal \(L(s-z,\chi _4)\) is entire. No second divisor-polynomial main term is present.

### Compact-smooth extension and prefix hypothesis

For each fixed \(z\) with \(0<\Re z<1/4\), (147.2) is valid for \(F\in C_c^\infty(0,\infty)\). This extension is derived in Section 3 from Mellin inversion and the completed functional equations; it is not quoted as an additional Banerjee--Khurana theorem. Uniform estimates may depend on finitely many seminorms of \(F\) and on \(z\).

A sharp prefix of length less than \(M^{1/2}\) is already \(O(M^{1/2}X^\varepsilon)\), below (147.7). Otherwise one may smooth each radial endpoint across \(O(M^{1/2})\) integers and peel the changed terms at the same cost. Thus compact-smooth testing is compatible with every prefix at the target scale, but the transform estimate must remain uniform in the moving endpoint and in the resulting collar seminorms.

### Every Bessel branch and the required order range

For fixed \(\nu\), the large-positive-argument algebra in (147.3) is

\[
\begin{aligned}
 \mathcal B_\nu(y)
 =\left(\frac2{\pi y}\right)^{1/2}
 \left\{
 \cos(y-\pi/4)-\frac{4\nu^2-1}{8y}\sin(y-\pi/4)+\cdots
 \right\}
 +\frac2\pi K_\nu(y)\sin\frac{\pi\nu}{2}.
\end{aligned}
\tag{147.16}
\]

The leading \(J/Y\) combination is independent of the order phase and contains both \(e(+\sqrt{nx})\) and \(e(-\sqrt{nx})\). The latter alone resonates with the physical positive direction. The \(K\)-branch is nonoscillatory and exponentially small at the resonant large argument for fixed order. None of these fixed-order statements is yet a uniform bound for complex \(\nu=2c+2iv\), nor does it control the small-argument/transition part of every off-resonant \((n,k)\) range.

The target-safe cone collar gives

\[
 |v|\lesssim D^{1/2}X^\varepsilon.
\tag{147.17}
\]

At resonance the Bessel argument is \(y\asymp\sqrt{NM}\). Since \(D\ll M^{1/2}\), the formal asymptotic parameter obeys

\[
 \frac{|z|^2}{y}\ll \frac{D}{\sqrt{NM}}X^\varepsilon\ll N^{-1/2}X^\varepsilon
\tag{147.18}
\]

for the smoothed cone; even the hard height \(|v|\lesssim D\) gives \(|z|^2/y\ll\sqrt{M/N}\). This makes a uniform expansion plausible. It is not a cited or completed proof.

### Quadratic refactorization card

At every odd prime,

\[
 K_p(w,z)=\frac{H_p(w,z)}{(1-a^2)(1-b^2)(1-ab)}
 =1+a^2b+ab^2+O((|a|+|b|)^4),
\tag{147.19}
\]

and at \(2\),

\[
 K_2(w,z)=(1-2^{-2w+2z})^{-1}.
\tag{147.20}
\]

Equations (147.19)--(147.20) prove (147.6). If \(z=c+iv\), \(|c|<1/2\), then \(K\) is absolutely convergent, uniformly in \(v\), in

\[
 \Re w>\frac{1+|c|}{3}.
\tag{147.21}
\]

For \(c=0\), this is \(\Re w>1/3\). The coefficient identity corresponding to (147.6) is the finite convolution

\[
 h_z(n)=
 \sum_{a^2b^2c_0^2r=n}
 \mu(a)\mu(b)\mu(c_0)\chi _4(c_0)
 a^{-2z}b^{2z}k_z(r),
\tag{147.22}
\]

where \(K(w,z)=\sum k_z(r)r^{-w}\). Formula (147.22) is algebraically exact; it does not assert absolute convergence of the three square-supported Möbius series below \(\Re w=1/2+|c|\).

### Adjacent reciprocal-zeta source controls

Charge--Dixit, [*Voronoi summation formulas, oscillations of Riesz sums, and Ramanujan--Guinand and Cohen type identities*](https://arxiv.org/abs/2410.04506), derives formulas for \(\mu(n)\), \(\lambda(n)\), and \(d(n)^2\). Its primary abstract explicitly says that sums over nontrivial zeros of \(\zeta\) are essential in these reciprocal-zeta formulas and that the \(\lambda\)-formula uses the Vinogradov--Korobov zero-free region. This is relevant source-class evidence for the seam (147.38): reciprocal-zeta corrections generally create zero terms that must be owned. It is not an applicable theorem for the level-four coefficient (147.9), a growing complex ratio shift, the fixed square-root centre, or the \(H\)-convolution.

Dixit--Maji--Vatwani, [*Voronoi summation formula for the generalized divisor function \(\sigma_z^{(k)}(n)\)*](https://arxiv.org/abs/2303.09937), defines \(\sigma_z^{(k)}(n)\) by summing \(d^z\) over divisors with \(d^k\mid n\), for fixed \(z\) and fixed \(k\). It supplies analytic finite-sum and Schwartz infinite-sum formulas with a new kernel, but its coefficient is neither \(A_z(n)\) with \(\chi _4\) nor the squarefree coefficient \(h_z*A_z\). It therefore does not repair the present coefficient, conductor, growing-order, or power hypotheses.

### Post-\(B\)-process linear-twist source control

Schlage--Puchta's squarefree linear-twist theorem, as audited in the permitted Round-145 source report, bounds one sum

\[
 \sum_{d\le D}\mu^2(d)e(\alpha d)
\tag{147.23a}
\]

at one frequency. Under \(|\alpha q_*-a|\le q_*^{-1}\), its Theorem 3 gives \(D^{1+\varepsilon}/q_*+q_*D^\varepsilon\). A post-\(B\)-process phase \(e(Nd/q)\) has reduced denominator \(q_*=q/(N,q)\). Even in the favorable generic stratum \(q_*\asymp Q\), summing this pointwise result over \(q\asymp Q\) gives \(D+Q^2\), not the exact bare-geometric-sum scale \(D+Q\). The latter uses the fact that \(\sum_de(Nd/q)\) is a geometric progression and then counts divisors near a product; inserting \(\mu^2(d)\) destroys that identity.

Expanding \(\mu^2(d)=\sum_{r^2\mid d}\mu(r)\) and applying the bare \(q\)-average after triangle already gives the schematic loss

\[
 \sum_{r\le\sqrt D}(Q+D/r^2)\ll Q\sqrt D+D,
\tag{147.23b}
\]

before the exact coprimality strata, parity, character, cone, profile, and prefix are restored. Those conditions couple \(d\), \(q\), and the remaining divisor variables, whereas (147.23a) has only \(\mu^2(d)\). Therefore Schlage--Puchta does not lawfully upgrade the bare \((Q+D)X^\varepsilon\) count to the exact post-\(B\)-process coefficient. A new averaged squarefree rational-frequency estimate retaining the gcd strata would be needed; no such result is supplied by that source.

## 3. Proof or derivation

### Derivation of the compact-smooth formula

Equation (5.11) of Banerjee--Khurana gives

\[
 \sum_{n\ge1}\bar\sigma_{u,\chi}(n)n^{-s}
 =\zeta(s-u)L(s,\chi).
\tag{147.23}
\]

Taking \(u=-2z\) and multiplying the coefficient by \(n^z\) proves

\[
 \sum_{n\ge1}A_z(n)n^{-s}
 =\zeta(s+z)L(s-z,\chi _4).
\tag{147.24}
\]

For \(F\in C_c^\infty(0,\infty)\), Mellin inversion initially on an absolute-convergence line gives

\[
 \sum_nA_z(n)F(n)
 =\frac1{2\pi i}\int_{(\sigma)}
 \zeta(s+z)L(s-z,\chi _4)\widetilde F(s)\,ds.
\tag{147.25}
\]

The Mellin transform \(\widetilde F\) decays faster than every power on vertical lines. Shift the contour past \(s=1-z\). Its residue is

\[
 L(1-2z,\chi _4)\widetilde F(1-z)
 =L(1-2z,\chi _4)\int_0^\infty F(x)x^{-z}\,dx.
\tag{147.26}
\]

Multiplying the standard completed functional equations of \(\zeta(s+z)\) and the odd primitive conductor-four \(L(s-z,\chi _4)\), expanding the dual Dirichlet series \(\zeta(1-s-z)L(1-s+z,\chi _4)\), and Mellin-inverting the gamma quotient gives (147.3). The root number is one and \(\tau(\chi _4)=2i\); comparison with the source's Mellin--Barnes evaluation fixes the scalar as (147.15). Rapid decay of \(\widetilde F\) justifies the contour shift and interchange for every fixed \(z\) in the source strip, and yields (147.2) for compact-smooth tests. This derivation gives local uniformity only when \(z\) remains in a fixed compact subset; it does not establish (147.17).

### Polar term after the exact squarefree convolution

The coefficient in (147.9) is \(h_z*A_z\). Applying (147.2) to \(F_k(x)=F(kx)\) gives the polar contribution

\[
 L(1-2z,\chi _4)\sum_{k\le2M}h_z(k)k^{z-1}
 \int_0^\infty F(u)u^{-z}\,du.
\tag{147.27}
\]

The infinite sum is \(H(1-z,z)\), and (147.12) applies because

\[
 (1-z)+z=1,\qquad \Re((1-z)-z)=1-2\Re z>\frac12.
\tag{147.28}
\]

Extending the finite sum in (147.27) to infinity costs at most

\[
 \sum_{k>2M}|h_z(k)|k^{c-1}\ll_\varepsilon M^{-1/2+2c+\varepsilon}.
\tag{147.29}
\]

Even with the trivial bound \(\left|\int F(u)u^{-z}du\right|\ll M^{1-c}\), this is \(O(M^{1/2+c+\varepsilon})\), target-safe for \(c<1/4\). In fact the physical phase in \(F\) is nonstationary, and repeated integration by parts makes (147.27) smaller; the added derivative of \(u^{-iv}\) is harmless in the formal range (147.17). Thus the pole is not the first power obstruction, provided the required uniform seminorm bounds are proved.

### Exact dual convolution and resonance

The dual part after convolution is

\[
 \pi4^z\sum_{k\le2M}\frac{h_z(k)}k
 \sum_{n\ge1}\sigma_{-2z,\chi _4}(n)n^z
 \int_0^\infty F(u)
 \mathcal B_{2z}\!\left(2\pi\sqrt{nu/k}\right)du.
\tag{147.30}
\]

The leading \(J/Y\) terms in (147.16) have phases

\[
 e\!\left(\sqrt{Nu}\pm\sqrt{nu/k}\right).
\tag{147.31}
\]

The plus sign is nonstationary. The minus sign is resonant precisely at \(n=kN\). Across \(u\asymp M\), linearization gives

\[
 |n-kN|\lesssim k\sqrt{N/M}.
\tag{147.32}
\]

At \(n\asymp kN\), one dual integral in (147.30), including its displayed \(1/k\), has absolute size

\[
 \frac1k\,M(NM)^{-1/4}
 =\frac{M^{3/4}N^{-1/4}}k.
\tag{147.33}
\]

There are \(\asymp k\sqrt{N/M}\) resonant integers, so the complete resonant capacity for each \(k\) is the flat quantity

\[
 B:=M^{1/4}N^{1/4}X^\varepsilon.
\tag{147.34}
\]

All statements (147.31)--(147.34) are fixed-order asymptotic ledgers. A proof that all complementary \(n\)-ranges and the \(K\)-branch are negligible uniformly in (147.17) is part of the missing theorem.

### Full \(H\)-triangle and all-scale power

For a fixed \(k\), the direct bound is \(M/k\), while the favorable complete-transform bound is (147.34). Let

\[
 k_0=M/B=M^{3/4}N^{-1/4}.
\tag{147.35}
\]

If \(k_0\ge1\), the powerful support count (147.14) gives

\[
 \sum_k|h_z(k)|\min(B,M/k)
 \ll_\varepsilon BK_0^{1/2+\varepsilon}
      +MK_0^{-1/2+\varepsilon}
 \ll_\varepsilon M^{5/8}N^{1/8}X^\varepsilon.
\tag{147.36}
\]

After division by the raw target \(M^{3/4}\), this is \(N^{1/8}M^{-1/8}X^\varepsilon\). If \(k_0<1\), the direct estimate gives the normalized price \(M^{1/4}X^\varepsilon\). Their better envelope is (147.5). The two prices meet at \(M=N^{1/3}=R^{4/3}\), where both equal \(R^{1/3}\). At the top, (147.36) is \(R^{7/4+\varepsilon}\) raw against target \(R^{3/2}\), hence the \(R^{1/4}\) loss. This proves that termwise modulus cannot close (147.7); it does not lower-bound the signed expression.

### Quadratic refactorization and the zero seam

For odd \(p\), the three reciprocal Euler factors in (147.6) have local product

\[
 (1-a^2)(1-b^2)(1-ab)
 =1-a^2-b^2-ab+O((|a|+|b|)^4).
\tag{147.37}
\]

Dividing (147.11) by (147.37) proves (147.19). When \(\Re z=c\), its first new monomials have magnitudes \(p^{-3\Re w-c}\) and \(p^{-3\Re w+c}\); hence \(3\Re w-|c|>1\) proves (147.21). The factor (147.20) is uniformly regular there because \(\Re w>|c|\).

The factorization is initially an identity in the common absolute-convergence region \(\Re w>1/2+|c|\), and then a meromorphic continuation. Shifting a \(w\)-contour into (147.21) encounters possible poles at

\[
 \zeta(2w+2z)=0,\qquad \zeta(2w-2z)=0,
 \qquad L(2w,\chi _4)=0.
\tag{147.38}
\]

For growing \(\Im z\), these zero sets move relative to the contour. The audited sources give no fixed zero-free strip down to \(\Re w>1/3\), no cancellation of these potential poles by \(K\), and no residue aggregate compatible with every fixed centre and prefix. Therefore (147.6) is lawfully useful as the finite signed coefficient identity (147.22), but not as a free contour shift or as an \(\ell^1\) saving.

The distinct custom estimate suggested by (147.22) is the uniform signed square-convolution resonance bound

\[
\boxed{
 \int_{|v|\lesssim D^{1/2}X^\varepsilon}\!\widehat W_D(c+iv)
 \sum_{a^2b^2c_0^2r\le2M}
 \mu(a)\mu(b)\mu(c_0)\chi _4(c_0)
 a^{-2z}b^{2z}k_z(r)\,
 \mathcal R_{a^2b^2c_0^2r}(z;M,N,U)\,dv
 \ll M^{3/4}X^\varepsilon,}
\tag{147.39}
\]

where \(\mathcal R_k\) is the exact conductor-four dual expression (147.30) restricted to (147.32), with the prefix, profile, and all kernel factors retained. This is stronger and more structured than a triangle over powerful \(k\). No audited theorem proves (147.39).

## 4. First doubtful or unproved step

The first unresolved **identity-to-estimate seam** is not the fixed-shift compact-smooth formula: (147.25)--(147.26) derive that formula. It is the following uniform assertion, which has not been proved or sourced:

\[
 \mathcal B_{2(c+iv)}(y)
 \text{ and all required }y\text{-derivatives admit (147.16) with a summable remainder,}
\tag{147.40}
\]

simultaneously for \(|v|\lesssim D^{1/2}X^\varepsilon\), every \(D,E,M,U\), every relevant \(n,k\), and through the small-, transition-, and large-argument regimes. Banerjee--Khurana's hypotheses give an exact identity for each fixed order only. The favorable ratio (147.18) near resonance does not by itself prove (147.40), nor does it dispose of the off-resonant \(K\) and transition ranges.

Granting (147.40), the first missing **arithmetic saving** is (147.39), or an equivalent signed aggregation of (147.30) across the moving bands (147.32). Absolute convergence of \(H\), powerful support, or the improved convergence of \(K\) cannot replace it: (147.36) leaves the explicit positive powers in (147.5).

The proposed use of (147.6) to move \(\Re w\) below \(1/2\) has an even earlier analytic seam if implemented by contour shifting: potential poles (147.38) must be crossed or avoided uniformly at growing height. No zero-free hypothesis in the permitted sources authorizes that step. This does not refute a coefficient-domain use of (147.22), and it is not an impossibility result for (147.7).

Finally, even a top-block proof would not address the all-scale maximum at \(M=R^{4/3}\). A lawful full proof must beat both branches of (147.5), not merely make the top transform target-borderline.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `t1_exact_extraction_and_prefix_target` | **Pass for interface.** Equations (147.7)--(147.8) retain the exact mandatory face and every half-open prefix. No \(t\ge2\) layer is claimed. |
| `ratio_Mellin_Euler_product_p2_and_H` | **Pass.** Equations (147.9)--(147.14) verify the \(2\)-factor, odd local factors, exact coefficients, support, and convergence. The scalar \(4^{-z}\) is kept outside. |
| `target_safe_cone_collar_and_ratio_bandwidth` | **Pass as reduction.** The inherited collar \(|e-4d|\le\sqrt D\) changes \(O(D^{3/2})=O(M^{3/4})\) raw terms on boundary boxes and permits (147.17). The hard cone still needs height comparable to \(D\). |
| `shifted_zeta_L_functional_equations_and_poles` | **Pass at fixed shift.** Equation (147.24) has one pole at \(s=1-z\), producing (147.26); \(L(s,\chi _4)\) is entire. The squarefree polar factor is legal by (147.28). |
| `level_four_generalized_divisor_Voronoi_kernel` | **Pass at fixed shift.** Equations (147.2)--(147.3) have \(q=4\), \(\tau(\chi _4)=2i\), argument \(2\pi\sqrt{nx}\), scalar \(\pi4^z\), and the exact \(J,Y,K\) combination. |
| `uniform_complex_order_and_Bessel_asymptotics` | **Open/source fail.** The source has no growing-order estimate; (147.40) remains unproved despite the favorable resonant parameter (147.18). |
| `H_powerful_coefficients_tail_and_signed_aggregation` | **Coefficient/tail pass; saving fail.** Equations (147.13)--(147.14), (147.29), and (147.36) are exact. Triangle loses a power. The signed targets are (147.39) or its unrefracted \(h_z\)-form. |
| `dual_resonance_centre_width_amplitude_and_off_resonance` | **Centre/width/amplitude pass.** Equations (147.31)--(147.34) give \(n=kN\), width \(k\sqrt{N/M}\), and flat capacity \(M^{1/4}N^{1/4}\). Uniform off-resonance and every \(K\)/transition range remain open. |
| `all_M_D_E_capacity_and_R4over3_barrier` | **Adverse.** Equation (147.5) peaks at \(M=R^{4/3}\) with \(R^{1/3}\); top triangle loses \(R^{1/4}\). The ledger is independent of a favorable balanced-box asymptotic. |
| `clipped_prefix_profile_terminal_endpoint` | **Pass at target-cost reduction.** A prefix shorter than \(\sqrt M\) is trivial; otherwise a \(\sqrt M\) radial collar makes a compact-smooth test at raw cost \(O(M^{1/2}X^\varepsilon)\). Uniform collar seminorms are part of (147.40). |
| `individual_positive_direction_and_fixed_centre` | **Pass.** The negative dual branch is paired with the exact physical \(+\) branch at fixed \(N\). No cosine, conjugate pairing, or centre average is used. |
| `Round141_142_144_self_return_and_zero_mode` | **Adverse/no new owner.** The transform exposes the same resonant square-root wave. A second transform is not counted as a saving, and no constant or zero mode removes (147.32). |
| `quadratic_H_refactorization_and_zero_seam` | **Algebra pass; contour fail.** Equations (147.6), (147.19)--(147.22) are exact. The improved \(K\)-half-plane does not move the reciprocal factors absolutely, and (147.38) blocks an unaudited uniform contour shift. |
| `reciprocal_zeta_source_class` | **Relevant but inapplicable.** Charge--Dixit confirms that explicit nontrivial-zero terms are essential in analogous reciprocal-zeta Voronoi formulas; it does not control this coefficient. Dixit--Maji--Vatwani treats a different generalized divisor function. |
| `post_B_linear_squarefree_q_average` | **Source fail.** Schlage--Puchta is pointwise in one linear frequency. At reduced denominators \(q_*\asymp Q\), summing its bound gives \(D+Q^2\), not \(D+Q\); the square-divisor expansion gives the independent \(Q\sqrt D\) loss (147.23b), before gcd and cone couplings. |
| `prime_even_and_D_equals_one_controls` | **Pass for formulas.** Equation (147.10) treats \(2\); \(\chi _4\) kills even \(e\); (147.13) treats odd primes. For bounded \(D\), the ratio bandwidth and cone collar are bounded and do not remove the independent \(H\)-aggregation/all-scale loss. |
| `Round138_cross_and_downstream_scope` | **No effect.** The Round-138 collar-tail cross, lower GAR, M9--M1, every M2 owner, endpoint uniformity, M9, the bridge, quarter target, and both global exponents remain open. |

## 6. Dependencies and exact artifacts used

The repository context was limited to the assigned files:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round147_source_and_method_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reports/sqrt_divisor_twist_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/reports/quadratic_irrational_divisor_twist_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/reports/multidimensional_monomial_source_audit.md`;
- `sources/banerjee_khurana_2023.md`.

The exact primary source used for (147.2)--(147.3) is D. Banerjee and K. Khurana, [*Character analogues of Cohen type identities and related Voronoi summation formulas*](https://arxiv.org/abs/2306.12399), arXiv:2306.12399v2, equation (5.11) and Theorem 4.3. The locally recorded PDF has SHA-256

```text
434E3C01D841D2DCC5F7762AC4F1F9FC5ADD290E3644F502210490591CCAF22C
```

The compact-smooth extension, the full \(H\)-power ledger, and the quadratic refactorization are derivations in this report, not theorem statements attributed to that paper. No primary theorem has been verified for (147.40) or (147.39); both are explicitly unproved.

Three adjacent primary sources were used only as source-class controls:

- S. Charge and A. Dixit, [arXiv:2410.04506](https://arxiv.org/abs/2410.04506), whose reciprocal-zeta formulas explicitly retain nontrivial-zeta-zero series;
- A. Dixit, B. Maji, and A. Vatwani, [arXiv:2303.09937](https://arxiv.org/abs/2303.09937), whose \(\sigma_z^{(k)}\) coefficient is different from (147.1) and (147.9);
- J.-C. Schlage-Puchta, [*The exponential sum over squarefree integers*](https://arxiv.org/abs/1105.1616), Acta Arith. 115 (2004), Theorems 1 and 3, used only for the mismatch (147.23a)--(147.23b).

No numerical experiment was performed.

## 7. Recommended state effect

**Recommended effect: `squarefree_H_resonance_no_go`; retain the target open and make no exponent change.** Promote no theorem claim from this source report alone. The fixed-shift compact-smooth identity (147.2), the exact conductor-four centre (147.4), the pole ledger (147.27)--(147.29), the Euler coefficients (147.13), and the refactorization (147.6)/(147.22) are suitable candidate-level derivations for seam review.

Reject only the following inferences:

1. that Banerjee--Khurana's fixed-order identity is already uniform through the growing ratio-Mellin range;
2. that absolute convergence of \(H\), or of \(K\) for \(\Re w>1/3\) on the imaginary \(z\)-line, supplies the physical signed saving;
3. that (147.6) permits an unconditional uniform \(w\)-contour shift below \(1/2\) without the zero residues in (147.38);
4. that a target-borderline bare top transform proves the exact squarefree scalar or improves the all-scale \(R^{1/3}\) barrier.

The one mathematically distinct inequality worth freezing is (147.39): it preserves the three Möbius-square signs, the absolutely convergent cubic remainder, the complex ratio frequency, and the moving conductor-four resonance. A subsequent candidate must either prove it with all Bessel regimes and prefixes, prove a quantitatively weaker range with a complete power ledger, or establish a scoped no-go for that particular signed placement. None of these outcomes alone would discharge the independent Round-138 owner, any \(t\ge2\) face, M9--M1, M9--M2, M9, the bridge, or the global exponent.
