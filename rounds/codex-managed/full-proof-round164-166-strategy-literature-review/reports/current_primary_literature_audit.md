# Round 166 current-primary-literature audit

**Audit date:** 2026-08-26.  **Status:** candidate evidence only; no graph promotion.

## 1. Result: a dated source-audit lemma and no-go result

### Literature-audit lemma

As of the audit date, the best source-audited claimed **pointwise** exponent for the classical Gauss circle discrepancy
\[
R(X)=\sum_{m^2+n^2\le X}1-\pi X
\]
is Li--Yang's
\[
\theta_*={3292+25\sqrt{1717}\over13762}
=0.3144831759740614\ldots .
\]
Their arXiv:2308.14859v2, Theorem 1.2, asserts, for every \(\varepsilon>0\),
\(R(X)=O_\varepsilon(X^{\theta_*+\varepsilon})\), and the analogous estimate for the Dirichlet divisor discrepancy.  This is a pointwise-in-\(X\) assertion, not an averaged theorem.  It supersedes Huxley's \(131/416\) benchmark.  The completed primary-source search found no later indexed claimed improvement to the classical pointwise circle exponent as of 2026-08-26; it does not purport to exclude unpublished or unindexed work.  This conclusion is deliberately phrased as “source-audited claimed”: the local Li--Yang source card records repairs needed to read v2 correctly, and no journal version or erratum was found.

No audited primary-source theorem below directly proves either surviving project inequality
\[
\tag{165.K17a}
\Re \mathfrak C^{\rm rem}_{R_0,2,{\rm opp},g<\gamma L}\ll_{\gamma,\varepsilon}L^2X^\varepsilon,
\qquad R_0=\lceil L\rceil,
\]
or
\[
\tag{165.K26}
\Re\!\sum_{\substack{R_0\le r<M_L\\2\mid r}}
\left(1-{r\over M_L}\right)
\sum_Nc^{\rm rem}_{N+r}\overline{c^{\rm rem}_N}
e\!\left(J(\sqrt{N+r}-\sqrt N)\right)
\ll_\varepsilon L^3X^\varepsilon,
\qquad M_L\asymp L^2.
\]
Here
\[
c_N^{\rm rem}=\sum_{\substack{d\mid N\\2\nmid d}}\chi_4(d)\lambda_N(d),
\]
with \(d,m=N/d\asymp L\), \(|\lambda_N(d)|\ll1\), and the actual \(\lambda_N(d)\) contains the supported squarefree row, normalization, residual selectors, parity branches, profiles, hard point, endpoints, and zero extension.

The closest literal structural match is Grimmelt--Merikoski, arXiv:2404.08502v2, Theorem 10.1.  The determinant map
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
\qquad ad-bc=d'm'-dm=r,
\]
is exact.  After splitting \(r=hk\) with \(k=2^{v_2(r)}\) and \(h\) odd, its determinant and gcd hypotheses and the fixed \(\chi_4(d')\chi_4(d)\) twist can be made compatible.  They are **not** the first failure.  The first literal failure is the absence of a proved admissible coefficient/weight representation: the actual selector-dependent multiplier has not been shown to satisfy the required left-automorphy or to be a single \(C^7_\delta\) dyadic weight.  If it is conditionally replaced by a smooth surrogate, the square-root-difference phase forces
\[
\delta^{-1}\gtrsim 1+{Jr\over L},
\]
and the theorem incurs unspecified polynomial losses \(\delta^{-O(1)}\).  On the short range the seminorm demand varies with \(r\) and reaches order \(J\) on the top stratum \(r\asymp L\); near \(r\asymp L^2\) it reaches order \(JL\).  The source statement does not certify these hidden powers as target-safe.  Moreover, one common test function does not presently carry the \(r\)-dependent phase through the variable-\(r\) aggregate; applying the theorem one \(r\) at a time and then using the triangle inequality would lose the required Fejer cancellation.

Grimmelt--Merikoski, arXiv:2505.00489v2, Part I, is not a stronger directly applicable result.  Its main theorem permits arbitrary compactly supported linear functionals, so it could in principle store endpoint weights if an exact two-endpoint kernel realization were first proved.  But its determinant specialization (Corollary 1.5) again requires a left-invariant coefficient and a \(C^{10}_\delta\) non-oscillatory function, while the full Theorem 1.1 leaves two automorphic-kernel discrepancy quadratic forms on the right.  With project weights those unestimated forms contain essentially the selector/phase correlations one is trying to bound.  The paper explicitly labels itself “Part I: non-oscillatory functions” and announces an oscillatory Part II; no primary Part II preprint was found by the audit date.

Therefore the literature changes neither the accepted graph nor the certified internal exponent \(1/3\).  It supplies method templates and, especially, a precise determinant-kernel interface to investigate, but no theorem can be imported without proving a new selector-aware, oscillatory, variable-determinant aggregate estimate with endpoint control.

## 2. Exact statements and hypotheses of the audited candidates

### 2.1 Current pointwise circle exponent and its immediate provenance

1. **Li--Yang, arXiv:2308.14859v2, Theorem 1.2** ([primary arXiv HTML](https://arxiv.org/html/2308.14859v2)).  For every \(\varepsilon>0\), pointwise for real \(X\),
   \[
   R(X),\ \Delta(X)=O_\varepsilon(X^{\theta_*+\varepsilon}),
   \qquad \theta_*={3292+25\sqrt{1717}\over13762}.
   \]
   There are no arbitrary coefficients and no average over \(X\).  The local source audit requires the following v2 repairs: Definition 4.1 has \(M<T^{7/16}\); in (5.18), \(H=MT^x\) with \(-3/8<x\le-\theta\); the sawtooth step uses the exact two-sign/two-range formula of Bourgain--Watt v1 (7.2); (5.27) has \(\sqrt{-1-8x}\); and the printed (4.9) is bypassed by checking the original Lemma 4.1 condition (4.6) via corrected (5.23).  The missing Guth--Maldague \(\beta_2\) condition is repaired only in the final parameter range.  Thus the imported claim is the narrow final theorem, not every printed intermediate generality.

2. **Huxley, “Exponential sums and lattice points III,” Proc. LMS 87 (2003), 591--609** ([official journal DOI](https://doi.org/10.1112/S0024611503014485)).  The paper's published abstract states discrepancy exponent \(K=131/208\) in radius, hence \(K/2=131/416\) for the divisor/circle size variable.  It is a superseded pointwise benchmark, not a source for (165.K17a) or (165.K26).  The local Huxley card remains pending full theorem-level import, so no internal lemma is attributed to it here.

3. **Bourgain--Watt, arXiv:1709.04340** ([arXiv record](https://arxiv.org/abs/1709.04340)).  Version 2 (2023-07-16) is withdrawn.  Consequently its Propositions 1', 2, 3 and Theorems 1--3 are excluded as theorem dependencies.  Li--Yang's repaired final specialization may use the exact identity printed in v1, but withdrawal forbids promoting a Bourgain--Watt theorem.

### 2.2 One-dimensional square-root/exponent-pair and spacing inputs

4. **Tao--Trudgian--Yang, arXiv:2501.16779, Definitions 11--12 and Theorem 20** ([primary arXiv HTML](https://arxiv.org/html/2501.16779)).  In their epsilon-loss formalism, an exponent pair \((k,\ell)\) controls every model phase \(F\), every \(T\ge N\ge1\), and every interval \(I\subset[N,2N]\) by
   \[
   \left|\sum_{n\in I}e\!\left(TF(n/N)\right)\right|
   \ll_\varepsilon (T/N)^{k+\varepsilon}N^{\ell+\varepsilon}.
   \]
   The sum has coefficient \(1\); the absolute value surrounds the single interval sum.  Theorem 20 gives the four exact exponent pairs
   \[
   \left({89\over1282},{997\over1282}\right),\quad
   \left({652397\over9713986},{7599781\over9713986}\right),\quad
   \left({10769\over351096},{609317\over702192}\right),\quad
   \left({89\over3478},{15327\over17390}\right).
   \]
   Partial summation transfers these only to fixed normalized bounded-variation profiles with their variation cost; it does not supply arbitrary \(N\)-dependent coefficients.

5. **Robert--Sargos, “Three-dimensional exponential sums with monomials,” J. reine angew. Math. 591 (2006), 1--20, Theorems 1 and 2** ([author PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf), [official DOI](https://doi.org/10.1515/CRELLE.2006.012)).  Theorem 1 takes positive integers \(H,N,M\), \(X>1\), arbitrary coefficients \(|a(h,n)|,|b(m)|\le1\), and fixed real \(\alpha,\beta,\gamma\) satisfying \(\alpha(\alpha-1)\beta\gamma\ne0\); for its trilinear monomial sum \(S_0\),
   \[
   S_0\ll_\varepsilon(HNM)^{1+\varepsilon}
   \left\{\left({X\over HNM^2}\right)^{1/4}+(HN)^{-1/4}+M^{-1/2}+X^{-1/2}\right\}.
   \]
   Theorem 2 says that, for fixed \(\alpha\ne0,1\), \(M\ge1\), and \(\delta>0\), the number of \(m_i\in(M,2M]\cap\mathbb Z\) satisfying
   \[
   |m_1^\alpha+m_2^\alpha-m_3^\alpha-m_4^\alpha|\le\delta M^\alpha
   \]
   is \(\ll_\varepsilon M^{2+\varepsilon}+\delta M^{4+\varepsilon}\).  Taking \(\alpha=1/2\) gives square-root spacing, but it is an unsigned four-tuple count.

### 2.3 Determinant equations, periodic/character twists, and Kloosterman fractions

6. **Grimmelt--Merikoski, arXiv:2404.08502v2, Theorem 10.1** ([primary arXiv HTML](https://arxiv.org/html/2404.08502v2)).  Let \(q_1,q_2>0\), \(q=q_1q_2\), \(h,k\ne0\), and
   \[
   M_{2,h,k}(\mathbb Z)=\{(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}) : ad-bc=hk,
   \ (a,c,k)=(b,d,k)=1\}.
   \]
   Put \(\Gamma=\Gamma_2(q_1,q_2)\), \(T=\Gamma\backslash\mathrm{SL}_2(\mathbb Z)\), and \(T_{1,k}=\mathrm{SL}_2(\mathbb Z)\backslash M_{2,1,k}(\mathbb Z)\).  Let \(\chi\) have conductor dividing \(q\), let \(\xi_h\) be multiplicative, and require \(\alpha\in\mathcal A(q_1,q_2,\chi,\xi)\), i.e. the stated left-automorphy with character and determinant twist.  Let \(A,C,D,\delta,\eta>0\), \(AD>\delta\),
   \[
   Z=\max(A^{\pm1},C^{\pm1},D^{\pm1},\delta^{-1}),\qquad
   H,K\ge1,\quad HK\le(AD)^{1+\eta},
   \]
   \[
   f\in C^7_\delta\!\left({A\over\sqrt{HK}},{C\over\sqrt{HK}},{D\over\sqrt{HK}}\right),
   \]
   with \(\beta_h\) supported on \(|h|\in[H,2H]\), \(\gamma_k\) on \(|k|\in[K,2K]\).  Assume the explicit short-kernel autocorrelation hypothesis (10.2), bounded by \(Z^{O(\eta)}\mathcal K_+\).  Then the sum is restricted by \(\gcd(h,kq)=1\); the resulting complex determinant-matrix aggregate equals a main term (present only when \(\chi\) is principal) plus one global error after the full \(h,k\) aggregate:
   \[
   O\!\left(Z^{O(\eta)}\delta^{-O(1)}(AD)^{1/2}
   \|\beta\xi\|_2\mathcal K_+^{1/2}
   (\mathcal R_0+\min(\mathcal R_1,\mathcal R_2))\right),
   \]
   where
   \[
   \mathcal R_0={\|\beta\xi\|_1A^{1/2}\over\|\beta\xi\|_2q_1^{1/2}C^{1/2}},
   \]
   \[
   \mathcal R_1={\|\beta\xi\|_1\over\|\beta\xi\|_2}H^{\vartheta_q}
   \left(1+\left({CD\over HKq_2}\right)^{\theta_q}\right)
   \left(1+\operatorname{cond}(\chi)^{1/4}
   \left({C\over Aq_2}\right)^{1/2-\theta_q}\right),
   \]
   \[
   \mathcal R_2=\left(1+\left({CD\over Kq_2}\right)^{\theta_q}\right)
   \left(1+\operatorname{cond}(\chi)^{1/4}
   \left({HC\over Aq_2}\right)^{1/2-\theta_q}\right).
   \]
   The main term contains \(\int_{\mathbb R^3}f(a,c,d)\,da\,dc\,dd/c\) and is not automatically zero in the project map because the resulting automorphy character is principal.

7. **Lau, arXiv:2509.07556v2, Theorem 5.2** ([primary arXiv HTML](https://arxiv.org/html/2509.07556v2)).  This is an explicitly credited fixed-\((h,k)\), untwisted special case of Grimmelt--Merikoski Theorem 10.1: \(\alpha\in\mathcal A(q_1,q_2)\), \(|hk|\le(AD)^{1+\eta}\), \((h,kq_1q_2)=1\), \(f\in C^7_\delta(A/\sqrt{|hk|},C/\sqrt{|hk|},D/\sqrt{|hk|})\), and a displayed \(\mathcal K_+\) hypothesis.  It yields a main term plus
   \[
   O\!\left(Z^{O(\eta)}\delta^{-O(1)}(AD)^{1/2}\mathcal K_+^{1/2}
   (\mathcal R_0+\min(\mathcal R_1,\mathcal R_2))\right),
   \]
   with \(\mathcal R_0=A^{1/2}/(q_1^{1/2}C^{1/2})\) and the exact \(|h|,|k|,q_2,\theta\) factors in (5.2).  Lau's application verifies automorphy and \(\mathcal K_+\) for a particular periodic divisibility selector; it does not extend the coefficient class to arbitrary project selectors or oscillatory weights.

8. **Grimmelt--Merikoski, arXiv:2505.00489v2, Theorem 1.1 and Corollary 1.5** ([primary arXiv HTML](https://arxiv.org/html/2505.00489v2)).  For a congruence subgroup \(\Gamma\), group character \(\chi\), arbitrary compactly supported linear functionals \(\alpha_1,\alpha_2\), \(A,C,D,\delta>0\), \(AD>\delta\), \(f\in C^{10}_\delta(A,C,D)\), \(F((\begin{smallmatrix}a&b\\c&d\end{smallmatrix}))=f(a,c,d)\), \(R_1=A/C,R_2=D/C\), and every \(X_0,X_1,X_2\ge1\) with \(X_0X_1X_2\ge AD\), Theorem 1.1 states
   \[
   |\langle\alpha_1|\Delta F|\alpha_2\rangle|
   \ll \delta^{-O(1)}(AD)^{1/2+o(1)}X_0^\theta
   \sqrt{\langle\alpha_1|\Delta k_{X_1^2,R_1}|\alpha_1\rangle
   \langle\alpha_2|\Delta k_{X_2^2,R_2}|\alpha_2\rangle}.
   \]
   Both quadratic forms are nonnegative; \(k_{Y,R}\in[0,1]\) is bounded by the indicated skew-hyperbolic-ball majorant.  Thus the absolute value is outside the full two-weight discrepancy, but the price is two new positive autocorrelation quantities.  Corollary 1.5 specializes to determinant-orbit sums only for a left-\(\Gamma\)-invariant \(\alpha\) and \(C^{10}_\delta\) \(f\), with a right side containing the explicit absolute autocorrelation \(\mathcal K\).  The article explicitly says Part II will generalize to oscillatory weight functions.

9. **Bettin--Chandee, arXiv:1502.00769, Theorems 1--2 and Corollary 1** ([primary arXiv PDF](https://arxiv.org/pdf/1502.00769), [official journal DOI](https://doi.org/10.1016/j.aim.2018.01.026)).  For dyadic \(\mathcal A=[A/2,A]\), \(\mathcal M=[M/2,M]\), \(\mathcal N=[N/2,N]\), arbitrary coefficient sequences \(\alpha_m,\beta_n,\nu_a\), and \(\vartheta\ne0\), Theorem 1 places the absolute value outside the full coprime trilinear form
   \[
   \mathcal B=\sum_{a,m,n\atop(m,n)=1}\alpha_m\beta_n\nu_a
   e\!\left(\vartheta {a\bar m\over n}\right)
   \]
   and proves
   \[
   |\mathcal B|\ll_\varepsilon\|\alpha\|_2\|\beta\|_2\|\nu\|_2
   \left(1+{|\vartheta|A\over MN}\right)^{1/2}
   \left((AMN)^{7/20+\varepsilon}(M+N)^{1/4}
   +(AMN)^{3/8+\varepsilon}(AN+AM)^{1/8}\right).
   \]
   Remark 1 allows a \(C^1\) phase perturbation with the displayed derivative bounds, replacing \(|\vartheta|A\) by \(|\vartheta|A+X\).  Theorem 2 gives the Jacobi-twisted analogue, with \((m/n)\), \((m,n)=(2,mn)=1\), and bound
   \[
   \|\alpha\|_2\|\beta\|_2\|\nu\|_2
   \left(1+{|\vartheta|A\over MN}\right)^{1/2}
   \left((MN)^{3/10}(AM+AN)^{7/20+\varepsilon}
   +A^{1/2}(M+N)^{7/8+\varepsilon}\right).
   \]
   Corollary 1 treats one fixed \(\Delta\ne0\): for
   \(m_1n_2-m_2n_1=\Delta\), arbitrary \(\alpha_{n_1},\beta_{n_2}\), and smooth one-variable \(f(m_1),g(m_2)\) satisfying all derivative bounds \(f^{(j)}\ll\eta^jM_1^{-j}\), \(g^{(j)}\ll\eta^jM_2^{-j}\), it gives an explicit main term and error
   \[
   O\!\left((\eta\mathcal R)^{3/2}\|\alpha\|_2\|\beta\|_2
   (N_1N_2)^{7/20}(N_1+N_2)^{1/4+\varepsilon}(M_1M_2)^\varepsilon\right),
   \]
   \(\mathcal R=M_1N_2/(M_2N_1)+M_2N_1/(M_1N_2)\).

### 2.4 Shifted divisor/Hecke convolution and spectral formulas

10. **Lau, arXiv:2509.07556v2, Theorems 1.1--1.2** ([primary arXiv HTML](https://arxiv.org/html/2509.07556v2)).  Theorem 1.1 fixes \(k\ge4\), a nonnegative smooth \(w\) compactly supported in \([1/2,1]\), and a nonzero integer \(h\) with \(|h|\ll x^{25/28-\eta}\), \(0<\eta<25/28\); it proves
   \[
   \sum_nw(n/x)d_k(n)d(n+h)
   =xP_{k,h,w}(\log x)
   +O_{k,w,\varepsilon}\!\left(x^{1-7\eta/128+\varepsilon}+x^{127/128+\varepsilon}\right).
   \]
   Theorem 1.2 allows \(0\le\delta\le1/16\) and \(|h|\ll x^{1-\varepsilon}\), with error
   \[
   x^{1-\delta+2\delta\theta+\varepsilon}
   \left(1+{|h|^{1/4}\over x^{1/4-\delta/2}}\right)
   +x^{1-\delta+\theta/2+\varepsilon}
   \left(1+{|h|^{\theta/2}\over x^{\theta/3+(2\delta/3)\theta}}\right),
   \]
   and an explicit integral-polynomial main term.  These are fixed-shift asymptotics for the exact coefficients \(d_k(n)d(n+h)\), not arbitrary weighted correlations.

11. **Blomer--Jana--Nelson, arXiv:2404.10692v2 / GAFA 35 (2025), Theorems 3 and 5** ([primary arXiv HTML](https://arxiv.org/html/2404.10692v2), [official DOI](https://doi.org/10.1007/s00039-025-00714-0)).  Theorem 3 is an exact spectral decomposition for shifted Whittaker-coefficient convolution of two fixed cuspidal automorphic representations \(\pi_1,\pi_2\) on \(\mathrm{PGL}_2\) over a number field, with a finite set \(S\), prescribed local principal-series hypotheses, nonzero \(b\in\mathcal O_F[1/S]\), and \(h\in C_c^\infty(F_S^\times\times F_S^\times)\).  The coefficient class is strictly automorphic/Whittaker.  In the classical level-one case, Theorem 5 fixes Hecke--Maass eigenforms \(f,g\), a fixed smooth \(V\) supported in \([1,2]\), and
   \[
   S(X,Y,b)=\sum_n\lambda_f(n+b)\lambda_g(n)V((n-X)/Y),
   \]
   for \(1\le Y\le X/10\), \(1\le b\le X/2\).  It proves pointwise
   \[
   |S(X,Y,b)|\ll {X^{1+\varepsilon}\over Y}(Y^{1/2}+b^{1/2})
   \min\!\left(b^\theta,1+{Yb^{1/4}\over X}\right)
   \]
   and separately the real-centre mean square
   \[
   \int_X^{2X}|S(x,Y,b)|^2dx
   \ll b^{2\theta}X^{2+\varepsilon}(1+b/Y).
   \]

### 2.5 Kloosterman/Salié bilinear dispersion and large sieve

12. **Blomer--Pascadi, arXiv:2607.24311v1, Theorems 1.1 and 1.6** ([primary arXiv HTML](https://arxiv.org/html/2607.24311)).  Theorem 1.1 takes every integer modulus \(c>0\), \(1\le N\le c\), intervals \(\mathcal I,\mathcal J\) of length at most \(N\), arbitrary complex \(\alpha_m,\beta_n\), and \(a\in(\mathbb Z/c\mathbb Z)^\times\).  With the absolute value outside the complete bilinear aggregate,
   \[
   \left|\sum_{m\in\mathcal I,n\in\mathcal J\atop(m,n,c)=1}
   \alpha_m\beta_nS(am,n;c)\right|
   \ll\|\alpha\|_2\|\beta\|_2c^{1+o(1)}
   \left({N^{1/8}\over c^{3/32}}+{N^{5/16}\over c^{3/16}}+{N^{2/3}\over c^{7/18}}\right).
   \]
   If both intervals are \(\{1,\ldots,N\}\), the gcd restriction may be removed.  At \(N=\sqrt c\), the bound is \(\|\alpha\|_2\|\beta\|_2c^{1-1/32+o(1)}\).  Theorem 1.6, for level \(q=rs\), a specified cusp of \(\Gamma_0(q)\), arbitrary \((\alpha_n)_{n\sim N}\), and an orthonormal Maass basis, gives
   \[
   \sum_{\lambda_j<1/4}X^{2\theta_j}
   \left|\sum_{n\sim N}\alpha_n\rho_{j\mathfrak a}(n)\right|^2
   \ll(qN)^{o(1)}(1+N/q)\|\alpha\|_2^2,
   \]
   with
   \[
   X=1+{q\over N}+\min\!\left({q^{18/11}\over N^{23/11}},
   {q^{16/13}\over N^{18/13}},{q^{32/29}\over N^{33/29}}\right)+{q^2\over N^3}.
   \]

13. **Shparlinski--Xiao, arXiv:2601.10113v1, Theorems 2.2, 2.5 and Corollary 2.8** ([primary arXiv HTML](https://arxiv.org/html/2601.10113)).  Throughout, \(q\) is a large prime and the kernel is the Salié/modular-square-root kernel for fixed integers \(a,b,\lambda\) with \((a\lambda,q)=1\).  Theorem 2.2 bounds the Type-I sum \(V_{a,b,\lambda}\), for arbitrary \(M,N\ge1\), arbitrary complex \(\alpha_m\), arbitrary endpoints \(N_m\le N\), under
   \(M\le q\), \(MN\le q^{3/2}\), \(M\le N^2\), by
   \[
   |V_{a,b,\lambda}|\le
   \sqrt{\|\alpha\|_1\|\alpha\|_2}\,M^{1/12}N^{7/12}q^{1/4+o(1)}.
   \]
   Theorem 2.5 takes arbitrary complex \(\alpha_m,\beta_n\) and puts the absolute value outside the full Type-II sum
   \[
   W_{a,b,\lambda}=\sum_{m\le M,n\le N}\alpha_m\beta_n
   \sum_{x^2\equiv amn+b\ (q)}e_q(\lambda x),
   \]
   proving
   \[
   |W_{a,b,\lambda}|\ll\|\alpha\|_2\|\beta\|_\infty
   \left(M^{1/2}N^{1/2}+M^{1/2}Nq^{-1/4}
   +Nq^{1/4}(\log q)^{1/2}\right).
   \]
   Corollary 2.8 allows the sharp hyperbolic region \(mn\le P,m\ge U,n\ge V\), with \(|\alpha_m|,|\beta_n|\le q^{o(1)}\), and bound
   \[
   |T_{a,b,\lambda}|\le(PV^{-1/2}+Pq^{-1/4}+Pq^{1/4}U^{-1/2})(Pq)^{o(1)}.
   \]

14. **Pascadi, arXiv:2404.04239v3 / Forum Math. Pi 14 (2026), Theorem 1.2** ([primary arXiv record](https://arxiv.org/abs/2404.04239), [official journal article](https://doi.org/10.1017/fmp.2026.10025)).  For \(q\ge1\), a specified cusp \(\mathfrak a\) with \(\mu(\mathfrak a)=q^{-1}\), arbitrary complex \((a_n)_{n\sim N}\), \(N\ge1/2\), and the exceptional Maass spectrum,
   \[
   \sum_{\lambda_j<1/4}X^{2\theta_j}
   \left|\sum_{n\sim N}a_n\rho_{j\mathfrak a}(n)\right|^2
   \ll_\varepsilon(qN)^\varepsilon(1+N/q)\|a\|_2^2
   \]
   whenever \(X\ll\max(1,q/N,q^2/N^3)\).  Pascadi's improvements require specific sparse-Fourier-transform coefficient structures.  This is a positive spectral mean square at a fixed level/cusp, not a bound for an unsquared signed Fejer correlation.

### 2.6 Cone decoupling

15. **Guth--Maldague, arXiv:2206.01093v2, Theorem 3** ([primary arXiv HTML](https://arxiv.org/html/2206.01093v2)).  Let \(R\gg1\); let \(f\) be Schwartz with Fourier support in the \(R^{-1}\)-neighbourhood of the truncated cone in \(\mathbb R^3\); decompose into caps of dimensions \(R^{-\beta_2}\times R^{-\beta_1}\times R^{-1}\), with \(\beta_1\in[1/2,1]\), \(\beta_2\in[0,1]\).  For every \(p\ge2\),
   \[
   \int|f|^p\ll_\varepsilon R^\varepsilon
   \left(R^{(\beta_1+\beta_2)(p/2-1)}
   +R^{(\beta_1+\beta_2)(p-2)-1}
   +R^{(\beta_1+\beta_2-1/2)(p-2)}\right)
   \sum_\gamma\|f_\gamma\|_p^p.
   \]
   This is an \(L^p\) spatial-average theorem for Fourier-localized Schwartz functions, not a pointwise arithmetic correlation.

## 3. Proof/derivation of the applicability audit

### 3.1 Exact determinant and character map for Grimmelt--Merikoski

Expand one project correlation term as
\[
\sum_{d'm'=N+r\atop d',m'\asymp L}
\sum_{dm=N\atop d,m\asymp L}
\chi_4(d')\chi_4(d)\lambda_{N+r}(d')\overline{\lambda_N(d)}
e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right).
\]
The matrix assignment
\((a,b,c,d)=(d',d,m,m')\) gives \(ad-bc=r\) exactly and \(A,C,D\asymp L\).  Choose \(q_1=4,q_2=1\), upper-row characters \(\chi_1=\psi_1=\chi_4\), and lower-row characters principal.  The resulting automorphy character is \(\chi_4^2\), hence principal on the odd support, while the pointwise matrix twist is \(\chi_4(a)\chi_4(b)=\chi_4(d')\chi_4(d)\).

Write \(r=hk\), \(k=2^{v_2(r)}\), \(h\) odd.  Then \((h,kq_1q_2)=1\).  Because \(d,d'\) are odd,
\[
(a,c,k)=(d',m,k)=1,\qquad(b,d,k)=(d,m',k)=1.
\]
Thus the determinant/gcd conditions survive the parity split.  Also \(HK\asymp r\le L^2\asymp AD\), so the determinant range covers both \(r\lesssim L\) and \(r\lesssim L^2\), up to harmless dyadic and 2-adic splitting.

The actual multiplier
\[
\lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}
\]
has no proved left-automorphic realization under \(\Gamma_2(4,1)\) and no proved encoding as an admissible smooth function of \((a,c,d)\).  This absence of an admissible representation is the first literal failure; it is not an impossibility theorem for every conceivable representation.  Lau's Theorem 5.2 succeeds in its application precisely because its periodic divisibility selector is separately proved automorphic (Lau Lemma 5.4) and its \(\mathcal K_+\) is separately counted; no analogous statement exists for the actual project selector.

Even after replacing the selector by a smooth cell, put
\[
\Phi_r(a,d)=J\left(\sqrt{ad}-\sqrt{ad-r}\right).
\]
For \(a,d\asymp L\) and both \(ad\) and \(ad-r\asymp L^2\),
\[
L|\partial_a\Phi_r|+L|\partial_d\Phi_r|\asymp {Jr\over L}.
\]
The \(C^7_\delta\) derivative definition therefore forces
\(\delta^{-1}\gtrsim1+Jr/L\).  Across (165.K17a) this ranges from \(1+O(J/L)\) for bounded even \(r\) to order \(J\) on the top short-shift stratum \(r\asymp L\); near the (165.K26) endpoint \(r\asymp L^2\), it reaches order \(JL\).  The theorem records only \(\delta^{-O(1)}Z^{O(\eta)}\), so its hidden exponent, the \(J\)-range, the partition count, and all other factors must be restored before the loss can be certified target-safe.

Theorem 10.1 gives a complex \((h,k)\)-aggregate equality with one global error, which is directionally compatible with the target if every literal weight can first be admitted.  But it uses one common \(f\), while \(\Phi_{hk}\) depends on \(hk\); its factors \(\beta_h\gamma_k\) cannot carry the \(N\)-dependent phase.  Delta-localizing \(h,k\) makes the theorem fixed-\(r\); applying triangle inequality only after this specialization puts \(\sum_r|E_r|\) in place of \(|\Re\sum_rE_r|\).  The linear factor \(1-hk/R\) is rank-two separable on a localized \((h,k)\) piece, so it is not itself the first obstruction; the hyperbolic cutoff \(hk<R\), sharp endpoints, and recombination still require estimates.  Finally, because the chosen \(\chi\) is principal, a main term remains and would also require a uniform oscillatory bound.

### 3.2 Why Part I does not remove the obstruction

The phase itself factorizes as \(e(J\sqrt{N+r})\overline{e(J\sqrt N)}\), and the selector product also factorizes between the two endpoints.  Hence it is tempting to put both into the arbitrary linear functionals \(\alpha_1,\alpha_2\) of Part I.  That is not a theorem application yet: one must construct an exact relative-kernel parametrization in which the determinant condition, parity/gcd restrictions, shell endpoints, and Fejer range are represented by a single non-oscillatory \(F\), without cross-terms.  The paper's ready-made determinant Corollary 1.5 instead assumes a left-invariant one-matrix weight and so does not admit the selector.

Even granting such a new parametrization, Theorem 1.1 bounds the desired discrepancy by
\[
\sqrt{\langle\alpha_1|\Delta k|\alpha_1\rangle
\langle\alpha_2|\Delta k|\alpha_2\rangle}.
\]
For the proposed endpoint weights these are selector- and phase-dependent autocorrelations.  No bound at the \(L^2\) or \(L^3\) project scale is supplied.  Thus Part I trades the original sum for two new unproved positive correlations; it does not close either gate.  If instead the phase remains in \(F\), the \(C^{10}_\delta\) derivative loss is worse than the \(C^7\) loss above.  This is why the paper's announced oscillatory Part II matters and why Part I is not a stronger applicable substitute.

### 3.3 Fixed-shift divisor and spectral shifted-convolution maps

For Lau set \(x\asymp L^2\), \(h=r\).  The coefficient class fails immediately: \(d_k(n)d(n+r)\) with a fixed smooth nonnegative profile is not \(c^{\rm rem}_{n+r}\overline{c^{\rm rem}_n}\) with a rough \(n\)-dependent selector and an oscillatory square-root phase.  Its asymptotic also has a generally nonzero main term.  The error is per fixed \(r\); triangle summation loses the Fejer sign.  At maximal scale \(r\asymp x\), Theorem 1.1 stops at \(x^{25/28-\eta}\) and Theorem 1.2 at \(x^{1-\varepsilon}\), so neither supplies the endpoint.

For Blomer--Jana--Nelson set \(X\asymp L^2\), \(b=r\), and use long smooth pieces.  Even pretending that \(c_N^{\rm rem}\) were a fixed Hecke eigenvalue sequence, their pointwise bound at a long scale is at best of order \(Lr^\theta X^\varepsilon\).  Summing absolute values over \(r<L\) gives \(L^{2+\theta+o(1)}\), exceeding the \(L^2\) gate; over \(r<L^2\) it gives \(L^{3+2\theta+o(1)}\), exceeding \(L^3\).  Their second estimate averages over a real centre \(x\), whereas the project requires the fixed shell centre.  The stated ranges \(Y\le X/10\), \(b\le X/2\) also require new completion for the hard endpoint.

### 3.4 Kloosterman-fraction, Kloosterman, Salié, and large-sieve maps

Bettin--Chandee Corollary 1 has the exact determinant equation under
\((m_1,m_2,n_1,n_2)=(m',m,d,d')\), giving \(m'd'-md=r\).  The \(\chi_4\) factors can be put into the arbitrary \(n_1,n_2\) coefficients.  But \(\lambda_{dm}(d)\) couples the two sides of each product and is not of the separable form \(f(m)\alpha_d\); the phase \(\sqrt{m'd'}-\sqrt{md}\) is likewise nonseparable in the smooth one-variable weights.  With all four lengths \(\asymp L\), bounded arbitrary coefficients give \(\|\alpha\|_2\|\beta\|_2\asymp L\) and the fixed-\(r\) error \(L^{39/20+\varepsilon}\).  This is a useful fixed-determinant saving, but summing \(L\) or \(L^2\) such errors is far above the two gates.  Theorems 1--2 aggregate the Kloosterman numerator parameter before the absolute value, but deriving their exact reciprocal phase with factorizable coefficients and controlled perturbation from the project sum is an unproved transformation.

Blomer--Pascadi Theorem 1.1 is stronger than older bilinear Kloosterman bounds in the square-root-of-modulus range and allows composite \(c\), but the project summand is not \(S(am,n;c)\).  No accepted Poisson/Kuznetsov step produces one fixed modulus \(c\), two factorized coefficient sequences, and the stated gcd support: natural divisor completions make the level vary with \(d,m\), while the selector remains joint.  Theorem 1.6 and Pascadi Theorem 1.2 begin only after a fixed level, cusp, spectral basis, and a linear coefficient sequence have been produced.  Their positive sum of absolute squares cannot by itself preserve the signed \(r\)-aggregate.  Therefore the first failed hypothesis is the missing exact fixed-level spectral/Kloosterman transform, before exponent comparison.

Shparlinski--Xiao is still farther from the literal interface.  Its modulus \(q\) is one fixed large prime and its kernel is a modular square root (equivalently a Salié sum) of \(amn+b\).  The project has an Archimedean phase \(e(J(\sqrt{N+r}-\sqrt N))\), varying composite divisor levels, determinant rather than product congruence, selector-coupled coefficients, and hard shell endpoints.  Although Theorem 2.5 has arbitrary Type-II weights and its absolute value is well placed around its complete double sum, there is no parameter choice turning the project kernel into its Salié kernel.  Corollary 2.8's sharp hyperbolic cutoff does not cure the fixed-prime-modulus and coefficient mismatch.

### 3.5 Exponent pairs, spacing, and decoupling

For a fixed \(r\), the phase as a function of \(N\) is a legitimate smooth scalar phase on a completed interval, so an exponent-pair estimate may bound an **unweighted** block.  TTY's coefficient is exactly \(1\), however, whereas the project coefficient is \(c_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}\), not a fixed bounded-variation profile.  More decisively, the exponent-pair absolute value is taken for each single \(N\)-sum; summing these bounds over \(r\) destroys the Re-after-Fejer-aggregate cancellation.  Completion of the sharp shell and selector endpoints adds variation not in Theorem 20.

Robert--Sargos Theorem 2 controls how often four square roots nearly coincide and is useful in fourth-moment arguments, but Cauchy--Schwarz/Hölder converts the signed determinant correlation into an unsigned four-tuple count.  This discards the \(\chi_4\), selector, and \(r\)-aggregate cancellation, and its diagonal \(M^{2+\varepsilon}\) is not by itself the desired correlation estimate.

Guth--Maldague's cone theorem is an averaged \(L^p\) inequality.  To use it one would have to prove a discretization that sends every project dyadic sector, rough coefficient, real centre, and endpoint to Fourier caps with the required \((\beta_1,\beta_2)\) conditions, then recover a pointwise fixed-\(J\) signed correlation.  None of these is a conclusion of Theorem 3.  Its role in Li--Yang is a specialized first-spacing input, not a direct Fejer theorem.

## 4. First doubtful or unproved step, candidate by candidate

| Candidate | First failed project hypothesis | What fails next if it is repaired |
|---|---|---|
| Li--Yang, Thm. 1.2 | It is a final circle-discrepancy theorem, not an estimate for the project coefficient or either open graph node. | Importing its exponent would not prove the quarter target or any graph seam. |
| TTY, Defs. 11--12/Thm. 20 | Coefficient class: the theorem is unweighted (or fixed normalized BV after partial summation), not selector-weighted. | Absolute value is before the \(r\)-sum; completion/endpoints cost variation. |
| Robert--Sargos, Thms. 1--2 | Unsigned moment/spacing statement rather than the signed determinant correlation. | Hölder loses \(\chi_4\), selector, and Fejer cancellation. |
| Grimmelt--Merikoski 2024, Thm. 10.1 | No admissible automorphic/smooth realization of the actual selector-dependent multiplier is proved. | \(\delta^{-1}\gtrsim1+Jr/L\); one \(f\) does not presently carry all \(r\); \(\mathcal K_+\) and the principal-character main term need bounds. |
| Lau 2026, Thm. 5.2 | Same automorphic coefficient restriction; Lau verifies it only for its periodic divisibility selector. | Fixed \((h,k)\), smooth \(f\), \(\delta^{-O(1)}\), and \(\mathcal K_+\). |
| Grimmelt--Merikoski 2025 Part I, Thm. 1.1 | No proved exact two-endpoint kernel realization whose \(F\) encodes the determinant/Fejer support without unwanted cross-terms. | RHS discrepancy autocorrelations for the actual rough/oscillatory weights are unbounded; Cor. 1.5 reimposes left invariance and smoothness. |
| Bettin--Chandee, Cor. 1 | Actual coefficient and square-root phase do not factor as two arbitrary single-variable coefficients times two smooth single-variable weights. | Fixed-\(r\) absolute error sums to an excessive power; endpoints need smoothing. |
| Lau, Thms. 1.1--1.2 | Exact coefficient is \(d_k(n)d(n+h)\), not the residual character-selector coefficient. | Per-shift asymptotic/main term, absolute error summation, and \(h\asymp x\) endpoint failure. |
| Blomer--Jana--Nelson, Thms. 3/5 | Coefficients must be fixed automorphic Whittaker/Hecke coefficients. | Pointwise power loses after summing \(r\); mean square is in a real centre; endpoint ranges stop early. |
| Blomer--Pascadi, Thms. 1.1/1.6 | No exact transform to a fixed-modulus Kloosterman bilinear form or fixed-level spectral linear form. | Selector nonfactorization, varying composite levels, positivity/absolute-square loss, and completion. |
| Shparlinski--Xiao, Thms. 2.2/2.5 | Kernel/modulus: fixed prime modular-square-root/Salié kernel, not the real square-root-difference determinant kernel. | Type-I/II factorization, selector dependence, varying composite levels, and endpoints. |
| Pascadi, Thm. 1.2 | No fixed-level/cusp spectral representation of the target. | Positive spectral mean square loses the signed \(r\)-aggregate; improvements need sparse Fourier structure. |
| Guth--Maldague, Thm. 3 | Fourier-localized Schwartz \(L^p\) cone setting, not a pointwise arithmetic correlation. | Discretization, selector smoothing, cap conditions, real-centre and endpoint completion. |

The requested ordering for the Grimmelt--Merikoski map is therefore:

1. **First literal failure:** selector-dependent coefficient/automorphy and smooth-weight class.
2. **Second:** after smoothing, the oscillatory square-root-difference weight causes uncontrolled derivative loss.
3. **Third:** a variable-\(r\) Fejer aggregate is not represented by a single test function; fixed-\(r\) use moves absolute values inward.
4. **Not the first failure:** determinant, 2-adic gcd, and fixed \(\chi_4\) hypotheses; these pass after the explicit split above.

## 5. Required control tests and outcomes

1. **`primary_source_exact_hypotheses`: PASS WITH EXPLICIT CROSS-REFERENCES.**  Every technical candidate above is tied to an arXiv author manuscript or official journal/author PDF, with theorem number, coefficient class, support/ranges, and principal ancillary hypotheses stated or cross-referenced.  For TTY the full model-phase derivative class remains Definition 11 of the cited source; for Robert--Sargos the complete Theorem-1 sum is the source's displayed \(S_0\).  Huxley is used only at abstract-level benchmark scope.  Secondary summaries were not used to establish a technical bound.

2. **`current_pointwise_exponent`: PASS, dated 2026-08-26.**  Searches of arXiv, official journal records, author manuscripts, and forward references to the classical circle problem found Li--Yang v2 as the latest claimed improvement.  Huxley \(131/416\) is superseded; Bourgain--Watt is withdrawn.  No claim is made that an unpublished or unindexed result was ruled out.

3. **`average_vs_pointwise_quantifier`: PASS.**  Li--Yang Theorem 1.2 is pointwise.  BJN Theorem 5's second estimate is explicitly averaged over the real centre.  Guth--Maldague is an \(L^p\) spatial average.  Spectral large sieves average squared linear forms over a basis.  None was relabelled pointwise.

4. **`coefficient_and_absolute_value_placement`: PASS.**  TTY is coefficient-one; Robert--Sargos allows bounded trilinear coefficients but uses an unsigned spacing count; Bettin--Chandee and Blomer--Pascadi allow factorized arbitrary sequences; BJN fixes automorphic coefficients; Lau fixes divisor coefficients; Shparlinski--Xiao has Type-I/II factorization; Grimmelt--Merikoski requires automorphy or leaves explicit kernel autocorrelations.  The target's real part is outside the \(r\)-aggregate.  Any fixed-\(r\) theorem followed by triangle inequality was marked inapplicable.

5. **`endpoint_completion_and_real_centre`: PASS.**  The target has sharp selector and shell endpoints.  Smooth dyadic theorems require a new boundary estimate.  Lau stops at \(|h|\ll x^{1-\varepsilon}\) or earlier; BJN assumes \(b\le X/2\) and its mean square integrates the centre; TTY partial summation charges variation; determinant-kernel results charge \(\delta^{-O(1)}\).  No endpoint was silently completed.

6. **`minimal_vs_maximal_Fejer_scale`: PASS.**  At \(R_0\asymp L\), the target is \(L^2X^\varepsilon\) and the GM phase seminorm demand is \(1+Jr/L\), reaching order \(J\) on \(r\asymp L\).  At \(M_L\asymp L^2\), the target is \(L^3X^\varepsilon\), the phase cost reaches order \(JL\) near \(r\asymp L^2\), and fixed-shift divisor theorems miss that endpoint.  The two gates were not conflated.

7. **`no_status_or_exponent_overpromotion`: PASS.**  The external \(\theta_*\) is recorded only as an audited benchmark.  The accepted internal exponent remains \(1/3\).  No analogy, withdrawn theorem, averaged estimate, determinant template, or repaired final specialization is promoted to (165.K17a), (165.K26), or the quarter theorem.

## 6. Dependencies and exact artifacts used

### Repository artifacts read in full

- `protocol.md`
- `state/active_campaign.yml`
- `rounds/codex-managed/full-proof-round164-166-strategy-literature-review/briefs/current_primary_literature_audit.md`
- `strategy/round166_full_proof_strategy_current_literature_review.md`
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/synthesis.md`
- `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`
- `sources/li_yang_2023.md`
- `sources/huxley_2003.md`
- `sources/bourgain_watt.md`
- `sources/tao_trudgian_yang_2025.md`

### Primary literature URLs preserved

- Li--Yang: <https://arxiv.org/html/2308.14859v2>
- Huxley: <https://doi.org/10.1112/S0024611503014485>
- Bourgain--Watt withdrawal record: <https://arxiv.org/abs/1709.04340>
- Tao--Trudgian--Yang: <https://arxiv.org/html/2501.16779>
- Robert--Sargos author paper: <https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf>; journal DOI: <https://doi.org/10.1515/CRELLE.2006.012>
- Grimmelt--Merikoski 2024: <https://arxiv.org/html/2404.08502v2>
- Grimmelt--Merikoski 2025 Part I: <https://arxiv.org/html/2505.00489v2>
- Lau 2026: <https://arxiv.org/html/2509.07556v2>
- Bettin--Chandee: <https://arxiv.org/pdf/1502.00769>; journal DOI: <https://doi.org/10.1016/j.aim.2018.01.026>
- Blomer--Jana--Nelson: <https://arxiv.org/html/2404.10692v2>; journal DOI: <https://doi.org/10.1007/s00039-025-00714-0>
- Blomer--Pascadi: <https://arxiv.org/html/2607.24311>
- Shparlinski--Xiao: <https://arxiv.org/html/2601.10113>
- Pascadi: <https://arxiv.org/abs/2404.04239>; journal DOI: <https://doi.org/10.1017/fmp.2026.10025>
- Guth--Maldague: <https://arxiv.org/html/2206.01093v2>

The search was confined to primary arXiv manuscripts, author-hosted papers, and official journal pages for technical claims.  It covered the classical pointwise exponent; square-root exponent sums and spacing; shifted divisor and automorphic convolution; determinant equations and character twists; Kloosterman/Salié bilinear dispersion; spectral large sieves; and cone decoupling.  It did not treat search-result snippets, surveys, or database summaries as theorem evidence.

## 7. Recommended state effect

**No change to the accepted graph.**

- **Retain** Li--Yang's \(\theta_*=0.3144831759740614\ldots\) solely as the dated external pointwise benchmark, subject to the existing v2 repair card.
- **Reject** direct promotion of every candidate audited here to (165.K17a) or (165.K26).
- **Retain as a strategy lead, not a lemma:** the exact Grimmelt--Merikoski determinant map with the 2-adic split.  Any future use must first prove one of two genuinely new interfaces:
  1. a selector-aware automorphic coefficient and uniform \(\mathcal K_+\) theorem whose oscillatory dependence is polynomially controlled and which aggregates all even \(r\) before absolute values; or
  2. an exact Part-I two-endpoint kernel realization together with new bounds for both selector/phase autocorrelation discrepancies, including the principal main term and hard endpoints.
- **Do not cite** the announced but presently absent oscillatory Part II as an available result.
- **Do not promote** fixed-shift, real-centre-average, spectral-mean-square, Kloosterman/Salié, exponent-pair, spacing, or decoupling analogies without a literal parameter-and-coefficient transfer theorem.

The literature audit therefore supports keeping Round 167 focused on an internal signed variable-shift estimate rather than treating a published theorem as a missing black box.
