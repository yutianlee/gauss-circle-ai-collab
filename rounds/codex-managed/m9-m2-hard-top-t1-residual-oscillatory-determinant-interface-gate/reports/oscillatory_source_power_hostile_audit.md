# Oscillatory source-power hostile audit

## 1. Result

**Terminal label: `oscillatory_determinant_interface_no_go`.**

There is no target-safe **direct black-box application** of Grimmelt--Merikoski, arXiv:2404.08502v2, Theorem 10.1, or of Grimmelt--Merikoski, arXiv:2505.00489v2, to the literal Round-167 \((165.K17a)\) sector on the evidence presently available.

This is deliberately narrower than a nonexistence result. It rules out the unproved interface currently suggested by the determinant identity
\[
 d'm'-dm=r,
 \qquad
 M=\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
\]
used as a single theorem call, or as theorem calls whose errors are then summed absolutely. It does **not** rule out a new automorphic decomposition, a controlled-rank expansion in the determinant, or a new signed family theorem proved specifically for the project weight.

The first literal failure of the 2024 interface is the coefficient/smooth-weight dichotomy. For \(0<\gamma<1/2\) and sufficiently large \(L\), the explicit orbit witness in Section 3.2 proves that the low-top-row-gcd selector \({\bf 1}_{(d,d')<\gamma L}\) is not left \(\Gamma_2(4,1)\)-invariant. For every \(\gamma\), no automorphy law is proved for the remaining residual selector, and its exact arithmetic values are not an admissible common \(C^7_\delta\) weight without a new interpolation or decomposition lemma. This is a missing source hypothesis, not a universal nonautomorphy claim. Independently of \(\gamma\), one common test function cannot encode the exact square-root-difference phase for more than one determinant \(r\), while splitting into individual \(r\)'s moves absolute values inside the signed shift aggregation and forfeits the missing factor \(L\).

The source audit also finds three conditional positive facts which must be retained:

1. The raw determinant map is exact and multiplicity-preserving, and the 2024 theorem's column primitivity conditions pass after an odd/2-adic factorization of even \(r\).
2. With the **bare** coefficient \(\alpha(M)=\chi_4(a)\chi_4(b)\), the induced theorem character is principal but the principal orbit sum vanishes for every 2-power \(k\). Thus a main term is not, by itself, the first obstruction if every project selector can be put elsewhere without altering \(\alpha\).
3. The theorem's spectral power is close to the required scale: under the optimistic assumptions made explicit in Section 3.6, its \(\mathcal R_0\) contribution sums at \(L^2\), whereas the displayed \(\mathcal R_2\) bound gives \(\ll\delta^{-O(1)}L^{2+\theta_4+\varepsilon}\) after the 2-adic sum. Both papers also retain an unspecified \(\delta^{-O(1)}\) loss. Consequently neither source restores the required power uniformly for the actual oscillatory weight.

## 2. Exact statements and hypotheses

### 2.1 Literal project target

The frozen target is
\[
 \Re\mathfrak C^{\mathrm{rem}}_{R_0,2,\mathrm{opp},g<\gamma L}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon,
 \qquad R_0=\lceil L\rceil.
\]
The permitted kernel fixes all of the following data: the residual divisor selector \(\lambda_N(d)\), the two \(\chi_4\) factors, even shifts \(0<r<R_0\), opposing displacements, the low gcd \(g=(d,d')<\gamma L\), the square-root-difference oscillation, the Fejer factor, endpoint restrictions, and one real part outside the entire aggregate. The positive-capacity estimate is of size \(L^3X^\varepsilon\); the source must therefore preserve and exploit one factor \(L\) of signed cancellation rather than return a separate absolute error for every shift or cell.

The exact divisor opening is
\[
 d'm'-dm=r,
 \qquad
 M=\begin{pmatrix}a&b\\c&d_0\end{pmatrix}
   =\begin{pmatrix}d'&d\\m&m'\end{pmatrix}.
\]
The opposing-displacement condition is \((d'-d)(m'-m)<0\). The tangent variables satisfy
\[
 a_{\rm tan}=d'-d\equiv0\pmod2,
 \qquad b_{\rm tan}=m'-m,
 \qquad r=d\,b_{\rm tan}+a_{\rm tan}m+a_{\rm tan}b_{\rm tan}.
\]

### 2.2 Grimmelt--Merikoski 2024: coefficient and smoothness classes

The primary source is [Grimmelt--Merikoski, arXiv:2404.08502v2](https://arxiv.org/abs/2404.08502v2), especially Definition 2, Definition 3, and Theorem 10.1.

Definition 2 defines \(C^J_\delta(X_1,\ldots,X_n)\) by support in
\[
 |x_i|\in[X_i,2X_i]
\]
and the derivative bounds
\[
 \left\|\partial_{x_1}^{J_1}\cdots\partial_{x_n}^{J_n}f\right\|_\infty
 \leq \prod_i(\delta X_i)^{-J_i},
 \qquad \sum_iJ_i\leq J.
\]

For \(q=q_1q_2\), Definition 3 requires \(\alpha\in\mathcal A(q_1,q_2,\chi,\xi)\), meaning
\[
 \ell_g\alpha=\chi(a)\xi_{\det g}\alpha
\]
for every integer matrix \(g=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)\) with \(q_1\mid b\), \(q_2\mid c\), and \((\det g,q)=1\). This is an exact left-automorphy law, not merely periodicity of the entries.

Theorem 10.1 takes positive integers \(q_1,q_2\), \(q=q_1q_2\), nonzero \(h,k\), and
\[
 \mathcal M_{2,h,k}
 =\left\{
 \begin{pmatrix}a&b\\c&d\end{pmatrix}\in M_2(\mathbb Z):
 \det M=hk,
 (a,c,k)=(b,d,k)=1
 \right\}.
\]
It uses \(\Gamma=\Gamma_2(q_1,q_2)\), \(T=\Gamma\backslash\mathrm{SL}_2(\mathbb Z)\), and \(T_{1,k}=\mathrm{SL}_2(\mathbb Z)\backslash\mathcal M_{2,1,k}\). The character \(\chi\) has modulus dividing \(q\), \(\xi_h\) is multiplicative, and \(\alpha\in\mathcal A(q_1,q_2,\chi,\xi)\).

For \(A,C,D,\delta,\eta>0\), it assumes \(AD>\delta\), sets
\[
 Z=\max(A^{\pm1},C^{\pm1},D^{\pm1},\delta^{-1}),
\]
takes \(H,K\geq1\) with \(HK\leq(AD)^{1+\eta}\), and requires
\[
 f\in C^7_\delta\left(A/\sqrt{HK},C/\sqrt{HK},D/\sqrt{HK}\right).
\]
The sequences \(\beta_h,\gamma_k\) are supported on \(|h|\in[H,2H]\), \(|k|\in[K,2K]\).

The theorem is conditional on its orbit-correlation hypothesis (10.2). With
\[
 w(\sigma,\sigma_1,\sigma_2)
 =\sum_{\tau\in T}\alpha(\tau\sigma\sigma_1)
                 \overline{\alpha(\tau\sigma_2)},
\]
the hypothesis puts an absolute value around the inner orbit sum and bounds the average over \(k_1,k_2\) and bounded real matrices \(g\in(k_1/k_2)^{1/2}\mathrm{SL}_2(\mathbb R)\) by \(Z^{O(\eta)}K_+\). Thus \(K_+\) is an additional theorem hypothesis; it is not supplied merely by \(|\alpha|\leq1\).

Under these assumptions, the sum over \((h,kq)=1\), weighted by
\[
 \beta_h\gamma_k\alpha(M)
 f\left(a/\sqrt{|hk|},c/\sqrt{|hk|},d/\sqrt{|hk|}\right),
\]
equals a principal-character main term plus one global error
\[
 O\!\left(
 Z^{O(\eta)}\delta^{-O(1)}(AD)^{1/2}
 \|\beta\xi\|_2K_+^{1/2}
 \{\mathcal R_0+\min(\mathcal R_1,\mathcal R_2)\}
 \right),
\]
where
\[
 \mathcal R_0=\frac{\|\beta\xi\|_1A^{1/2}}
 {\|\beta\xi\|_2q_1^{1/2}C^{1/2}},
\]
\[
 \mathcal R_1=\frac{\|\beta\xi\|_1}{\|\beta\xi\|_2}
 H^{\vartheta_q}
 \left(1+\left(\frac{CD}{HKq_2}\right)^{\theta_q}\right)
 \left(1+\operatorname{cond}(\chi)^{1/4}
 \left(\frac C{Aq_2}\right)^{1/2-\theta_q}\right),
\]
\[
 \mathcal R_2=
 \left(1+\left(\frac{CD}{Kq_2}\right)^{\theta_q}\right)
 \left(1+\operatorname{cond}(\chi)^{1/4}
 \left(\frac{HC}{Aq_2}\right)^{1/2-\theta_q}\right).
\]
The published exponents satisfy \(\theta_q,\vartheta_q\leq7/64\). The main term is present only when \(\chi\) is principal and contains
\[
 \sum_{\substack{h,k\\(h,kq)=1}}
 \beta_h\xi_h\sigma_1(|h|)\gamma_k
 \sum_{\tau\in\Gamma\backslash\mathcal M_{2,1,k}}\alpha(\tau)
 \int f(a,c,d)\,\frac{da\,dc\,dd}{c},
\]
times the stated zeta, level, and local factors.

The final power of the smoothness parameter is not explicit: the theorem and its proof retain \(\delta^{-O(1)}\). Proposition 4.1 contains particular derivative losses, including a displayed \(\delta^{-2}\) in one decay quantity, but subsequent steps again use unspecified \(\delta^{-O(1)}\). It is therefore not valid to assign a numerical final seminorm exponent from the paper without redoing those arguments.

### 2.3 Grimmelt--Merikoski 2025 Part I

The primary source is [Grimmelt--Merikoski, arXiv:2505.00489v2](https://arxiv.org/abs/2505.00489v2), especially Definition 3, Theorem 1.1, and Corollary 1.5.

Definition 3 permits \(\alpha_1,\alpha_2\in L_c(G)\), compactly supported continuous linear functionals; finite weighted point-evaluation sums are included. Theorem 1.1 takes a congruence subgroup \(\Gamma\), a group character, and
\[
 f\in C^{10}_\delta(A,C,D),\qquad AD>\delta,
\]
with \(F(M)=f(a,c,d)\), \(R_1=A/C\), \(R_2=D/C\), and auxiliary \(X_0,X_1,X_2\geq1\) satisfying \(X_0X_1X_2\geq AD\). It bounds the discrepancy by a quantity of the shape
\[
 \delta^{-O(1)}(AD)^{1/2+o(1)}X_0^{\theta}
 \sqrt{
 \langle\alpha_1\mid\Delta k_{X_1^2,R_1}\mid\alpha_1\rangle
 \langle\alpha_2\mid\Delta k_{X_2^2,R_2}\mid\alpha_2\rangle}.
\]
The two discrepancy-kernel quadratic forms in the theorem are nonnegative. The vertical bars in this notation delimit the sesquilinear form; they do not denote an operator absolute value. The discrepancy operator subtracts a principal component. Hence a bound for the raw project sum also requires an exact treatment of
\[
 \frac{\mathbf 1_{\chi\ \mathrm{principal}}}{|\Gamma\backslash G|}
 \overline{\langle1\rangle_{\alpha_1}}\langle1\rangle_{\alpha_2}
 \int_G F(g)\,dg,
\]
not merely the discrepancy estimate.

Corollary 1.5 is more concrete but requires an explicitly left-\(\Gamma\)-invariant coefficient on a left-invariant matrix set with finitely many orbits, together with a \(C^{10}_\delta\) archimedean weight. Its correlation factor is again an absolute autocorrelation quantity. The paper still writes the smoothness loss as \(\delta^{-O(1)}\); Theorem 7.1 supplies order-dependent derivative bounds but no explicit final exponent for the full theorem.

The 2025 theorem is formally compatible with a complex oscillatory \(f\): Theorem 1.1 explicitly defines \(F:G\to\mathbb C\) from \(f\in C^{10}_\delta(A,C,D)\) and imposes no positivity, reality, or nonoscillation hypothesis on \(f\). All frequency is then paid through the ten derivative bounds and the final \(\delta^{-O(1)}\). Thus “non-oscillatory” in the title describes the strength and intended use of Part I, not an exclusion from the literal theorem statement. Conversely, moving oscillatory coefficients to endpoint functionals avoids that archimedean derivative loss only after an exact relative-kernel identity has been proved.

## 3. Proof and derivation of the interface audit

### 3.1 Exact determinant, parity, and primitivity map

Set \(q_1=4,q_2=1\) and first retain only the bare character row
\[
 \alpha_{\rm bare}(M)=\chi_4(a)\chi_4(b).
\]
It can be obtained from the source's entry-character example using top-row characters \(\chi_1=\psi_1=\chi_4\) and principal bottom-row characters. The induced theorem character is
\[
 \chi=\chi_1\psi_1\overline{\chi_2\psi_2}=\chi_4^2,
\]
hence principal, and \(\xi=1\).

Write each positive even determinant uniquely as
\[
 r=hk,
 \qquad k=2^{v_2(r)},\qquad h\ \mathrm{odd}.
\]
Then \((h,kq)=1\). Since \(d,d'\) are odd, the theorem's two column conditions are automatic:
\[
 (d',m,k)=1,
 \qquad (d,m',k)=1.
\]
Dyadic decomposition in \(h\), and decomposition over the \(O(\log L)\) possible powers \(k\), costs only \(L^{o(1)}\). The determinant range \(HK\ll L\) is safely below \((AD)^{1+\eta}\) when \(A,C,D\asymp L\).

The Fejer factor \(1-r/R_0=1-hk/R_0\) is affine in \(h\) for each fixed \(k\), so it may be placed in \(\beta_h\). The determinant cutoff can likewise be divided into dyadic \(h\)-blocks for each \(k\). These operations are not the first obstruction.

### 3.2 The low-gcd selector fails the source coefficient law

Under the determinant dictionary, the literal selector is
\[
 S(M)={\bf1}_{(a,b)<\gamma L}.
\]
Fix \(0<\gamma<1/2\) and sufficiently large \(L\). Choose an odd integer
\[
 \gamma L\leq G<L/2
\]
and a positive odd integer \(T\asymp L\), and take
\[
 M=\begin{pmatrix}G&3G\\T&3T+2\end{pmatrix},
 \qquad \det M=2G,
 \qquad
 u=\begin{pmatrix}1&4\\0&1\end{pmatrix}\in\Gamma_2(4,1).
\]
Then \((G,3G)=G\), whereas the top row of \(uM\) is
\[
 (G+4T,\,3G+12T+8),
\]
and
\[
 \gcd(G+4T,\,3G+12T+8)\mid
 (3G+12T+8)-3(G+4T)=8.
\]
Both transformed top entries are odd, so their gcd is \(1\). Moreover \(r=2G<L\leq R_0\), the original top gcd obeys \(G\geq\gamma L\), and the transformed top gcd obeys \(1<\gamma L\). Thus the exact low-gcd indicator changes on one left orbit. Both matrices have opposing displacements: \(G-3G<0\), \((G+4T)-(3G+12T+8)<0\), and the unchanged lower displacement \((3T+2)-T\) is positive.

This proves, only in the stated range \(0<\gamma<1/2\), that the literal low-gcd indicator cannot simply multiply \(\alpha_{\rm bare}\) while retaining membership in \(\mathcal A(4,1,1,1)\). If \(\gamma\geq1/2\), then \(g\mid r\), \(g\) is odd, and \(r/g\) is even, so \(g\leq r/2<L/2\leq\gamma L\); the low-gcd cutoff is then identically one on the project range and this witness is irrelevant. The overall direct-call no-go does not rely on extending the witness to that range: the residual selector still has no verified source automorphy or target-safe interpolation, and the variable-\(r\) phase still fails the one-common-\(f\) interface. Nor does the witness rule out an as-yet-unproved orbit decomposition agreeing with the selector on restricted support.

Putting \(S\) into \(f\) does not repair the direct call: exact gcd cutoffs are discontinuous and have no \(C^7_\delta\) seminorm. Expanding \((a,b)\) by Möbius inversion and rescaling the top row changes the determinant to \(r/g\), produces skew scales, and leaves an external sum over \(g\). The 2024 theorem contains an internal Möbius treatment of \((h,k)=1\), but it does not price this project selector. Applying it separately and summing the errors over \(g\) puts absolute values inside the gcd decomposition unless a new joint estimate is proved.

The residual divisor selector \(\lambda_N(d)\) is only controlled in the permitted kernel by \(|\lambda_N(d)|\leq1\) and an energy bound. No exact automorphy law for it is provided. Consequently the audit cannot certify a selector-dependent \(\alpha\), and it does not claim that every conceivable extension is nonautomorphic.

### 3.3 Exact phase normalization and seminorm loss

For positive \(r\), introduce the normalized variables
\[
 x=a/\sqrt r,\qquad y=c/\sqrt r,\qquad z=d_0/\sqrt r.
\]
The determinant-one relation gives the normalized missing entry
\[
 b/\sqrt r=(xz-1)/y.
\]
Write the corresponding physical phase, up to the fixed sign convention, as
\[
 \phi_r(a,d_0)=J\left(\sqrt{ad_0}-\sqrt{ad_0-r}\right).
\]
In normalized variables it becomes
\[
 \Phi_r(x,z)
 =J\sqrt r\left(\sqrt{xz}-\sqrt{xz-1}\right).
\]
On a nondegenerate dyadic cell with \(a,d_0,A\asymp L\), a physical-scale first derivative satisfies
\[
 A\left|\partial_a\phi_r(a,d_0)\right|
 \asymp_{\mathrm{cell}} \frac{|J|r}{L}.
\]
This is exactly the source's normalized derivative scale because \((A/\sqrt r)\partial_x=A\partial_a\). All logarithmically scaled derivatives of \(\phi_r\) through order seven are \(O_{\mathrm{cell}}(|J|r/L)\), while differentiating \(e(\Phi_r)\) creates powers of this scale. On an interior subcell where the remaining amplitude is constant, or has strictly smaller scaled derivatives, an admissible source parameter must therefore satisfy
\[
 \delta^{-1}\gtrsim_{\mathrm{cell}}1+\frac{|J|r}{L}.
\]
Conversely, \(\delta^{-1}\asymp_{\mathrm{cell}}1+|J|r/L\) is sufficient for the phase factor's derivatives through order seven before adding the other cutoffs. This seminorm scale is \(\asymp_{\mathrm{cell}}1+|J|/L\) for bounded positive \(r\), and \(\asymp_{\mathrm{cell}}1+|J|\) when \(r\asymp L\). These are source-input seminorm comparisons, not lower bounds for the true sum.

The source's final factor \(\delta^{-O(1)}\) has no recoverable numerical exponent. Therefore even after supplying all missing selector identities, the published theorem cannot certify that the oscillatory seminorm loss is \(X^\varepsilon\) in the project's full \(J,L,X\) range.

There is also an exact variable-determinant obstruction. If \(J\ne0\) and a single theorem call used one common \(f(x,y,z)\) and determinant coefficients \(b(r)\), then for two determinants \(r_1\ne r_2\) it would require the ratio
\[
 \frac{e\!\left(J\sqrt{r_1}G(x,z)\right)}
      {e\!\left(J\sqrt{r_2}G(x,z)\right)},
 \qquad G(x,z)=\sqrt{xz}-\sqrt{xz-1},
\]
to be independent of \((x,z)\). It is not: \(G\) is nonconstant. Hence the exact phase is not a product of a determinant coefficient and one common test function. Putting it in \(\alpha\) instead is unsupported because this entry-dependent archimedean phase has not been shown to satisfy the left-automorphy law.

Localizing to a single \(r\) supplies a legal smooth phase but yields an error \(E_r\) for each shift. The black-box bound on the original real aggregate then becomes \(\sum_r|E_r|\), rather than an estimate for the one outer real part. That triangle inequality discards precisely the variable-\(r\) cancellation available in the frozen target, and no cited source estimate proves the resulting absolute error sum is target-sized. A controlled-rank Fourier or Mellin expansion uniform in \(r\) could in principle change this conclusion, but no such lemma is present in the permitted artifacts or either source.

### 3.4 Opposing signs, endpoints, cells, and two-adic costs

In normalized variables the opposing-displacement condition can be written
\[
 \left(x-\frac{xz-1}{y}\right)(z-y)<0.
\]
This condition is independent of \(r\), so it is geometrically compatible with a common normalized test function. Its **sharp** boundary is not \(C^7\); a source application still needs a smooth partition plus a separately bounded boundary layer. No such boundary estimate is supplied.

The exact dyadic endpoints and zero extensions have the same issue. Smooth partitions on interior cells cost only logarithmically, but the literal endpoint remainder must be priced rather than silently discarded. Project Möbius expansions and any cells resolving the residual selector are additional to the theorem's internal coprimality decomposition.

The 2-adic split itself is benign: there are \(O(\log L)\) powers \(k=2^v\), and the column gcd conditions pass. The problem is not the number of 2-adic cells but the lack of a theorem call preserving their signed aggregation and project selectors.

### 3.5 Conditional cancellation of the 2024 principal term

The induced character for \(\alpha_{\rm bare}\) is principal, so the theorem displays a main term. Nevertheless its finite orbit coefficient vanishes for every \(k=2^v\).

One may identify
\[
 \Gamma_2(4,1)\backslash\mathrm{SL}_2(\mathbb Z)
 \cong\mathbb P^1(\mathbb Z/4\mathbb Z)
\]
using top-row representatives
\[
 (x,1),\quad x=0,1,2,3,
 \qquad (1,0),\ (1,2).
\]
For \(T_{1,k}\), take
\[
 \sigma_b=\begin{pmatrix}1&b\\0&k\end{pmatrix},
 \qquad b\pmod k,\quad(b,k)=1,
\]
with the unique class \(b=0\) when \(k=1\). Equation (10.5) of the source, specialized to \(h=1\), shows that these representatives together with the six representatives of \(T\) parametrize \(\Gamma\backslash\mathcal M_{2,1,k}\).
If a representative has top row \((x,y)\), the top row of \(\tau\sigma_b\) is \((x,xb+yk)\). Therefore the relevant sum is
\[
 \sum_{\tau,b}\chi_4(x)\chi_4(xb+yk).
\]
For \(k=1\) the six \(\mathbb P^1(\mathbb Z/4\mathbb Z)\) terms sum to zero. For \(k=2\), the four \((x,1)\) representatives contribute \(-2\), while \((1,0),(1,2)\) contribute \(+2\). For \(4\mid k\), each odd \(b\) contributes \(4\chi_4(b)\), and summing over \(b\in(\mathbb Z/k\mathbb Z)^\times\) gives zero. Hence
\[
 \sum_{\tau\in\Gamma\backslash\mathcal M_{2,1,k}}
 \alpha_{\rm bare}(\tau)=0
 \qquad(k=2^v).
\]

This is useful only conditionally: all remaining selectors and the oscillation must be placed in the common smooth function while leaving \(\alpha=\alpha_{\rm bare}\). If a selector-dependent automorphic coefficient is introduced, the finite orbit sum changes and must be recomputed. Thus “principal character” is not itself a fatal main-term obstruction, but the project does not yet possess the placement needed to exploit the cancellation.

### 3.6 Orbit correlation and the restored-power ledger

For the bare coefficient, the elementary inequality
\[
 |w(\sigma,\sigma_1,\sigma_2)|
 \leq\sum_{\tau\in T}|\alpha_{\rm bare}(\tau)|^2
 \leq|T|=6
\]
does not prove \(K_+=O(1)\), because hypothesis (10.2) also counts all compatible Hecke-orbit pairs. In the source's Section 12 application, a specific periodic weight satisfies a correlation count of the shape
\[
 \frac1k(\text{correlation count})
 \ll Z^\varepsilon k
 \left(r_1r_2+(r_1,r_2)(C/D+D/C)\right).
\]
This shows the kind of extra factor that can enter \(K_+\), but it is not a proof for the K17a residual selector. A selector-dependent \(\alpha\) produces exactly the new orbit autocorrelation that the project would have to bound.

Even granting optimistically that an analogue gives \(K_+^{1/2}\ll k^{1/2}X^\varepsilon\), the source power is only borderline. Put \(A=C=D\asymp L\), fix a 2-power \(k\), take \(h\asymp H\), and assume \(|\beta_h|\asymp1\) on \(\asymp H\) supported indices, so that
\[
 \|\beta\|_2\asymp H^{1/2},
 \qquad \|\beta\|_1/\|\beta\|_2\asymp H^{1/2}.
\]
Then, up to fixed level factors,
\[
 \mathcal R_0\asymp H^{1/2},
\]
\[
 \mathcal R_1\ll H^{1/2+\vartheta_4}
 \left(1+\left(\frac{L^2}{Hk}\right)^{\theta_4}\right),
\]
\[
 \mathcal R_2\ll
 \left(1+\left(\frac{L^2}{k}\right)^{\theta_4}\right)
 \left(1+H^{1/2-\theta_4}\right).
\]
The dyadic-block error is therefore
\[
 E_{H,k}
 \ll X^\varepsilon\delta^{-O(1)}
 L H^{1/2}K_+^{1/2}
 \{H^{1/2}+\min(\mathcal R_1,\mathcal R_2)\}.
\]
At the top range \(H\asymp L/k\), the \(\mathcal R_0\) term is
\[
 \ll \delta^{-O(1)}L^2k^{-1/2}X^\varepsilon,
\]
which sums over 2-powers \(k\) at the target scale if \(\delta^{-O(1)}\) is harmless. The displayed theorem bound via \(\mathcal R_2\), however, gives only
\[
 \ll \delta^{-O(1)}L^{2+\theta_4}k^{-1/2}X^\varepsilon.
\]
With only the published unconditional \(\theta_4\leq7/64\), this source upper bound is not of the required \(L^2X^\varepsilon\) form: substituting the published exponent leaves a fixed positive power of \(L\). If one independently had \(\theta_4=0\), this part of the optimistic ledger would be target-sized; the paper does not furnish that input. This calculation audits what the stated upper bound certifies; it is not a lower bound on the project sum.

Thus even after assuming away the coefficient obstruction and supplying a favorable orbit bound, the combination of the exceptional-spectrum factor and the unspecified oscillatory seminorm exponent does not restore the target power in the literal uniformity range.

### 3.7 Why the 2025 Part I theorem does not close the gap

Part I can place arbitrary finite weights in endpoint functionals, so it weakens the superficial objection that every selector must be a smooth function. But a project application first needs an exact identity of the form
\[
 \mathfrak C^{\rm rem}_{R_0,2,\rm opp,g<\gamma L}
 =\langle\alpha_1,K_F\alpha_2\rangle
\]
with every determinant incidence counted once, the two characters and residual selector in the correct slots, the even-shift and opposing-sign restrictions preserved, and no cross terms. No such relative-kernel identity is proved in the source or permitted project artifacts.

Even if that identity were supplied, Theorem 1.1 bounds the desired signed discrepancy form by
\[
 \sqrt{
 \langle\alpha_1\mid\Delta k_{X_1^2,R_1}\mid\alpha_1\rangle
 \langle\alpha_2\mid\Delta k_{X_2^2,R_2}\mid\alpha_2\rangle}.
\]
These are nonnegative selector/phase discrepancy-kernel autocorrelations, not absolute-value operators. The kernel energy bound \(\mathcal D_L\ll L^2X^\varepsilon\) does not, by itself, imply the factor-\(L\) saving required for these new quantities; the source supplies no K17a-specific estimate. Thus Part I repackages the missing cancellation into unproved nonnegative correlations rather than proving it.

The principal component is an additional obligation. Bare-character cancellation analogous to Section 3.5 would have to be established in the exact relative-kernel model; it cannot be inferred before that model exists. Corollary 1.5 is not a shortcut, because its left-invariance hypothesis is violated by the literal low-gcd function just exhibited. Finally, Part I's \(C^{10}_\delta\) option has an even longer derivative ledger and still ends with \(\delta^{-O(1)}\).

Accordingly the 2025 paper contains no stronger directly applicable statement for this literal sector.

## 4. First doubtful or unproved step

The narrowest first unproved step is:

> Construct an exact, multiplicity-preserving decomposition of the literal K17a residual weight into a bounded or \(X^{o(1)}\)-rank family of coefficients satisfying the Grimmelt--Merikoski automorphy law and common \(C^7_\delta\) test functions, while keeping the variable-\(r\) phase and the one outer real part aggregated; then prove the corresponding orbit-correlation bound \(K_+\) and an explicit seminorm power that is \(X^\varepsilon\)-safe.

For \(0<\gamma<1/2\), the direct placement fails before that step because the explicit low-gcd function is not in the coefficient class and is not smooth enough for \(f\). For arbitrary \(\gamma\), the residual-selector automorphy/interpolation is unproved, and the determinant-dependent phase independently fails a one-function family representation. The source does not prove that no more elaborate decomposition can exist, so the report makes no universal nonexistence claim.

For the Part I route the first unproved step is earlier still: the exact relative-kernel identity with no cross terms. After that, the first quantitative gap is a project-specific bound for the two nonnegative \(\Delta k\) discrepancy-kernel autocorrelations at the strength needed to save \(L\).

## 5. Required control tests and outcomes

1. **Raw determinant and multiplicity control — passed.** The dictionary \((a,b,c,d_0)=(d',d,m,m')\) gives \(\det M=r\) exactly and loses no raw quadruples.

2. **Parity, 2-adic, and column-primitivity control — passed.** The factorization \(r=hk\), with \(h\) odd and \(k=2^{v_2(r)}\), satisfies \((h,kq)=1\); odd \(d,d'\) force both column gcd conditions. The number of 2-adic cells is logarithmic.

3. **Coefficient automorphy control — failed literally in the stated small-\(\gamma\) range, and otherwise uncertified.** For \(0<\gamma<1/2\), the explicit unipotent orbit changes \({\bf1}_{(a,b)<\gamma L}\). For arbitrary \(\gamma\), no automorphy law or target-safe interpolation is proved for the residual selector.

4. **Smoothness and phase-seminorm control — failed as a target certificate.** On a nonzero interior cell the required phase seminorm parameter satisfies \(\delta^{-1}\gtrsim_{\mathrm{cell}}1+|J|r/L\), a scale \(\asymp_{\mathrm{cell}}1+|J|\) at \(r\asymp L\), while both sources state only \(\delta^{-O(1)}\).

5. **Variable-shift aggregation control — failed.** Two distinct determinants give nonproportional normalized phases. Per-\(r\) application produces \(\sum_r|E_r|\), not a bound with the original single outer real part.

6. **Principal-main-term control — conditionally passed for the bare 2024 coefficient.** The finite orbit sum of \(\chi_4(a)\chi_4(b)\) vanishes for every \(k=2^v\). It is untested after any selector-dependent coefficient modification and unproved for a Part I kernel embedding.

7. **Orbit-correlation control — failed for the literal selector.** Bounded pointwise weights do not imply the theorem's hypothesis (10.2). The source's special periodic correlation count is not a K17a estimate.

8. **Power restoration control — failed.** Under favorable assumptions the \(\mathcal R_0\) piece is target-sized, but the stated \(\mathcal R_2\) piece retains \(L^{\theta_4}\), and the unspecified \(\delta\)-power remains. Per-shift localization additionally discards the signed family saving, with no source bound for the resulting absolute error sum at the target scale.

9. **Opposing-sign and endpoint control — unresolved.** The sign condition has a determinant-independent normalized formula, but its sharp boundary and the literal endpoints require smoothing and a boundary estimate not present in the sources.

10. **Part I relative-kernel control — failed at identity and correlation.** No exact no-cross-term embedding is given, and its nonnegative discrepancy-kernel autocorrelations are new unproved project quantities.

## 6. Dependencies and exact artifacts used

Local artifacts, and no other project files, were used:

- `protocol.md`.
- `state/active_campaign.yml`.
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/briefs/oscillatory_source_power_hostile_audit.md`.
- `strategy/round167_m2_hard_top_t1_residual_oscillatory_determinant_strategy.md`.
- `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`.
- `rounds/codex-managed/full-proof-round164-166-strategy-literature-review/reports/current_primary_literature_audit.md`.
- `rounds/codex-managed/full-proof-round164-166-strategy-literature-review/reviews/source_hypotheses_currency_interface_review.md`.
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/barrier_packet.md`.

Primary sources:

- J. Grimmelt and J. Merikoski, *Twisted correlations of the divisor function via discrete averages of \(\mathrm{SL}_2(\mathbb R)\) Poincaré series*, arXiv:2404.08502v2, Definitions 2--3, Proposition 4.1, Theorem 10.1, Lemma 10.2, and Section 12: [abstract/version page](https://arxiv.org/abs/2404.08502v2), [HTML full text](https://arxiv.org/html/2404.08502v2), [versioned PDF](https://arxiv.org/pdf/2404.08502v2).
- J. Grimmelt and J. Merikoski, *Weighted averages of \(\mathrm{SL}_2(\mathbb R)\) automorphic kernel. Part I: non-oscillatory functions*, arXiv:2505.00489v2, Definition 3, Theorem 1.1, Corollary 1.5, and Theorem 7.1: [abstract/version page](https://arxiv.org/abs/2505.00489v2), [HTML full text](https://arxiv.org/html/2505.00489v2), [versioned PDF](https://arxiv.org/pdf/2505.00489v2).

No numerical experiment was used. No shared state, strategy, review, synthesis, or proof-kernel file was edited.

## 7. Recommended state effect

**Retain K17a as the selected strategy, but record this source route as a narrow direct-interface no-go; make no proof-state promotion.**

The determinant identity and the conditional bare-character main-term cancellation are reusable structural facts. They justify continued work only if a later round proves a new interface lemma that simultaneously:

1. resolves the residual and low-gcd selectors into legal automorphic data or a legal relative kernel;
2. preserves variable-\(r\) aggregation and the one outer real part;
3. proves the exact \(K_+\) or \(\Delta k\) discrepancy-kernel correlation estimate;
4. prices Möbius, cells, 2-adic pieces, sharp sign boundaries, and endpoints; and
5. makes the final phase-seminorm exponent explicit and target-safe, while removing or absorbing the fixed \(L^{\theta_4}\) spectral loss.

Until those items are proved, neither Grimmelt--Merikoski theorem is a literal proof of the Round-167 target. This conclusion is source- and interface-specific and must not be promoted to a claim that no oscillatory determinant method can work.
