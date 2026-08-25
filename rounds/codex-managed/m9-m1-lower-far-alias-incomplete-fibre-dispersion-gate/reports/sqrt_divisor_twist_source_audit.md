# Round 141 square-root divisor-twist source audit

- Campaign: `m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate`
- Task: `sqrt_divisor_twist_source_audit`
- Role: `source_auditor`
- Graph at assignment: `072e08848e9d368d65b89fbf03c36423a8e3662e7ae61c48052d4c352d1d71b0`

## 1. Result

**Source-audit no-go, with one target-safe reduction.** Put \(N_0=N=\lfloor X\rfloor=y^2+q\) and \(R=X^{1/4}\). On the inherited effective support \(hr\ll y\asymp R^2\), the exact floor-dependent mask may be replaced, at total cost

\[
O_\rho(\log R)=O_{\rho,\epsilon}(X^\epsilon),
\]

by the constant cone

\[
r>4h,\qquad r\ \text{odd}.
\]

On every dyadic block \(h\asymp H\), the sharp cone may then be replaced at cost \(O_\rho(1)\) by a smooth ratio cutoff with relative transition width \(H^{-1/2}\). The resulting smoothed dyadic scalar has an exact double-Mellin representation whose arithmetic factor is, after \(t\mapsto-t\),

\[
4^{-t}\zeta(s+t)L(s-t,\chi_4).
\]

Thus smoothing and Mellin separation do expose a two-variable shifted product of degree-one \(L\)-functions. No audited primary-source theorem, however, bounds the resulting fixed-centre scalar by \(X^\epsilon\):

* Robert--Sargos gives \(T_{R,R}\ll R^{1/2+\epsilon}\) only for the smoothed specialization in which the two long coefficient slots are separated. Putting the exact joint mask in its arbitrary joint slot and taking the third length to be \(1\) gives only \(T_{R,R}\ll R^{3/4+\epsilon}\).
* Sargos--Wu Theorem 9, restated as the 2019 paper's Lemma 5.1, admits \((\alpha,\beta)=(1/2,1/2)\) but requires separated coefficients and gives only \(T_{R,R}\ll R^{2/5+\epsilon}\) after smoothing and separation. The adjacent general-domain Lemma 5.2 permits a joint staircase domain but excludes this phase through \(\alpha+\beta-1=0\).
* The audited Tao--Trudgian--Yang exponent pair gives only \(T_{R,R}\ll R^{267/641+\epsilon}\).
* Complete-coefficient Voronoi and standard-twist formulae return the circle discrepancy or a resonant square-root twist and do not control the exact incomplete coefficient.
* Even pointwise Lindelöf bounds inserted by absolute values into the double-Mellin contour give \(R^{1+\epsilon}\); an ideal shifted mean square plus Mellin Plancherel and Cauchy--Schwarz gives the same \(R^{1+\epsilon}\).

For comparison, Popov's complete \(r_2\)-weighted cosine combination is controlled, after removing the outer \(N_0^{1/4}\asymp R\), only at

\[
R^{4\theta_*-1+\epsilon}
=R^{(50\sqrt{1717}-297)/6881+\epsilon}
=R^{0.257932\ldots+\epsilon}
\]

using Li--Yang's circle exponent. This controls one specific real combination of the two conjugate complete twists, not either individual complex branch; Li--Yang's stated discrepancy theorem alone does not separate them. The exponent is already too large, and completion additionally leaves an uncontrolled complementary cone. The Round-141 fixed-centre signed target remains open.

## 2. Exact statement and hypotheses

The audited object is

\[
T_N=\sum_{m\ge1}m^{-3/4}V_{\rm low}(R^2m/N_0)A_\rho(m)e(\sqrt{N_0m}),
\]

\[
A_\rho(m)=
\sum_{\substack{h\mid m,\ r=m/h\ \mathrm{odd}\\r\ge r_h+2}}\chi_4(r),
\quad
r_h=\min\{r\ge4N_0h/D_h^2:r\ \text{positive odd}\},
\quad
D_h=y-\lfloor\rho y/\sqrt h\rfloor-1.
\]

The target is \(T_N\ll_\epsilon X^\epsilon\), uniformly for every real \(X\), or \(O(RX^\epsilon)\) after the outer \(N_0^{1/4}\) factor.

**Robert--Sargos.** Theorem 1 of O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials* ([primary PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf)), assumes \(X_1>1\), \(|a(h,n)|,|b(m)|\le1\), and

\[
\alpha(\alpha-1)\beta\gamma\ne0.
\]

For

\[
S_0=\sum_{H<h\le2H}\sum_{N_1<n\le2N_1}a(h,n)
\sum_{M<m\le2M}b(m)
e\!\left(X_1\frac{h^\beta n^\gamma m^\alpha}
{H^\beta N_1^\gamma M^\alpha}\right),
\]

it proves

\[
S_0\ll_\epsilon(HN_1M)^{1+\epsilon}
\left\{
\left(\frac{X_1}{HN_1M^2}\right)^{1/4}
+(HN_1)^{-1/4}+M^{-1/2}+X_1^{-1/2}
\right\}.
\]

Smooth dyadic weights are removable by partial summation. The only arbitrary joint coefficient is \(a(h,n)\). This produces two different balanced specializations: \((H,N_1,M)=(R,1,R)\) puts the two long variables in separated coefficient slots after the proved ratio smoothing/Mellin separation, whereas \((H,N_1,M)=(R,R,1)\) is the direct dummy-variable specialization that can carry the exact joint mask.

**Sargos--Wu.** Theorem 9 of P. Sargos and J. Wu, *Multiple exponential sums with monomials and their applications in number theory* ([primary DOI](https://doi.org/10.1023/A:1006777803163)), is restated as Lemma 5.1 in *On a Diophantine inequality over primes* ([DOI](https://doi.org/10.1016/j.jnt.2019.01.008)). For \(Z>0\), \(M,N_1\ge1\), separated coefficients \(|a(m)|,|b(n)|\le1\), and

\[
\alpha\beta(\alpha-1)(\beta-1)(\alpha-2)(\beta-2)\ne0,
\]

it bounds

\[
S_{SW}=\sum_{m\asymp M}\sum_{n\asymp N_1}
a(m)b(n)e\!\left(Z\frac{m^\alpha n^\beta}{M^\alpha N_1^\beta}\right)
\]

by

\[
\begin{aligned}
(ZMN_1)^{-\eta}|S_{SW}|\ll{}&
(Z^4M^{31}N_1^{34})^{1/42}
+(Z^6M^{53}N_1^{51})^{1/66}
+(Z^6M^{46}N_1^{41})^{1/56}\\
&+(Z^2M^{38}N_1^{29})^{1/40}
+(ZM^9N_1^6)^{1/10}
+(Z^2M^7N_1^6)^{1/10}\\
&+(Z^3M^{43}N_1^{32})^{1/46}
+(ZM^6N_1^6)^{1/8}
+M^{1/2}N_1+MN_1^{1/2}+Z^{-1/2}MN_1.
\end{aligned}
\]

In particular, \(\alpha=\beta=1/2\) satisfies the written hypothesis. The theorem is pointwise in the phase scale \(Z\), but its coefficient class is separated; the sharp or exact joint cone is not one of its coefficients.

The immediately adjacent Lemma 5.2 is a different, general-domain estimate. It lets \(\mathcal D\) lie in

\[
M<m\le2M,\qquad N_1<n\le2N_1,\qquad M>N_1,
\]

with every axis-parallel line meeting \(\mathcal D\) in \(O(1)\) intervals. If \(f(m,n)\sim_\Delta\widehat A m^\alpha n^\beta\) in the theorem's derivative-comparability sense and

\[
\alpha\beta(\alpha+\beta-1)(\alpha+\beta-2)\ne0,
\]

then, for \(\mathcal X=MN_1\) and \(F=\widehat A M^\alpha N_1^\beta\),

\[
\begin{aligned}
(\mathcal XF)^{-\eta}\left|\sum_{(m,n)\in\mathcal D}e(f(m,n))\right|
\ll{}&(F^2\mathcal X^3)^{1/6}+\mathcal XN_1^{-1/2}+\mathcal X^{5/6}
+\mathcal X(\Delta M^{-1})^{1/4}\\
&+\mathcal X(FM)^{-1/8}
+(\Delta^4F^2\mathcal X^9M^{-4})^{1/10}
+\mathcal XF^{-1/4}.
\end{aligned}
\]

This second lemma allows the joint staircase geometry, and splitting \(r\) into the two odd residue classes modulo \(4\) removes \(\chi_4\), but \(f(h,r)=\sqrt{N_0hr}\) fails its displayed nondegeneracy hypothesis because \(\alpha+\beta-1=0\). That failure does not apply to Sargos--Wu Theorem 9 itself.

**Tao--Trudgian--Yang.** Definition 11 and Theorem 20 of T. Tao, T. Trudgian and A. Yang, *New exponent pairs, zero density estimates, and zero additive energy estimates* ([primary PDF](https://arxiv.org/pdf/2501.16779)), state that an exponent pair \((\kappa,\lambda)\) gives, for a model phase, \(T\ge N_1\ge1\), and \(I\subset[N_1,2N_1]\),

\[
\sum_{n\in I}e(TF(n/N_1))
\ll_\epsilon(T/N_1)^{\kappa+\epsilon}N_1^{\lambda+\epsilon}.
\]

Theorem 20 includes

\[
(\kappa,\lambda)=\left(\frac{89}{1282},\frac{997}{1282}\right).
\]

After fixing \(h\), splitting odd \(r\) by residue class modulo \(4\), and using partial summation, the exact endpoint \(r_h+2\) is allowed. The theorem is therefore valid rowwise but gives no cancellation between heights and no partial-sum estimate for \(A_\rho(m)\).

**Banerjee--Khurana.** Theorems 4.3--4.4 of S. Banerjee and R. Khurana, *Voronoï summation formula for the generalized divisor function* ([primary PDF](https://arxiv.org/pdf/2306.12399)), assume an odd primitive \(\chi\bmod q_0\), \(0<\Re\nu<1/2\), noninteger endpoints \(0<\alpha<\beta\), and an analytic test function. The relevant identity is

\[
\frac{q_0^{1+\nu/2}}{\tau(\chi)}
\sum_{\alpha<j<\beta}\sigma_{-\nu,\chi}(j)f(j)
=q_0^{\nu/2}L(1+\nu,\chi)\int_\alpha^\beta f(t)\,dt
+2\pi i\sum_{n\ge1}\overline{\sigma}_{-\nu,\chi}(n)n^{\nu/2}
\int_\alpha^\beta f(t)t^{-\nu/2}\mathcal B_\nu(4\pi\sqrt{nt/q_0})\,dt,
\]

with its stated endpoint convention and

\[
\mathcal B_\nu(z)=
\left(\frac2\pi K_\nu(z)+Y_\nu(z)\right)\sin\frac{\pi\nu}{2}
-J_\nu(z)\cos\frac{\pi\nu}{2}.
\]

At the formal endpoint \(\nu=0\), for real \(\chi_4\),

\[
d_{\chi_4}(m)=\sum_{r\mid m}\chi_4(r)=\frac{r_2(m)}4.
\]

The published strip is strict at \(\nu=0\), the test class is analytic, and the coefficient is complete rather than the height-dependent \(A_\rho\).

**Popov and Li--Yang.** Theorem 5 of D. A. Popov, *Voronoi's formulae and the Gauss problem* ([article](https://www.mathnet.ru/eng/rm10162), [primary PDF](https://www.mathnet.ru/links/9d83ce675a9437c9b763883aa94a5cfb/rm10162_eng.pdf)), proves for all \(x,M\ge3\)

\[
P(x)=-\frac{x^{1/4}}\pi\sum_{n\le M}r_2(n)n^{-3/4}
\cos(2\pi\sqrt{nx}+\pi/4)+\Delta_MP(x),
\]

\[
\Delta_MP(x)\ll\sqrt{x/M}\,\overline r(x)+\overline r(M)\log M,
\qquad \overline r(t)=t^{o(1)}.
\]

It controls precisely the displayed cosine combination, not the two complex branches independently. Theorem 1.2 of X. Li and X. Yang, *An improvement on Gauss's circle problem and Dirichlet's divisor problem* ([primary PDF](https://arxiv.org/pdf/2308.14859)), proves

\[
P(x),\Delta(x)\ll_\epsilon x^{\theta_*+\epsilon},
\qquad
\theta_*=\frac{3292+25\sqrt{1717}}{13762}=0.3144831759\ldots.
\]

Li--Yang's stated theorem controls the discrepancy and therefore Popov's real combination; it does not supply an individual-complex-direction estimate.

**Kaczorowski--Perelli.** J. Kaczorowski and A. Perelli, *Twists and resonance of \(L\)-functions, I* ([article](https://ems.press/journals/jems/articles/13843), [primary PDF](https://ems.press/content/serial-article-files/32124)), define for an extended-Selberg-class function of degree \(d\)

\[
F(s,\alpha)=\sum_{n\ge1}a(n)e(-\alpha n^{1/d})n^{-s}.
\]

With \(n_\alpha=q_Fd^{-d}\alpha^d\) and

\[
\operatorname{Spec}(F)=\{\alpha>0:a(n_\alpha)\ne0\},
\]

Theorem 1 makes a fixed nonspectral twist entire, while Theorem 2 gives a fixed spectral twist poles

\[
s_k=\frac{d+1}{2d}-\frac{k}{d}-i\theta_F,
\]

with a simple leading pole. Their smoothed sums are treated for fixed \(\alpha\), and the paper explicitly says the available \(\alpha\)-uniformity is weak. For \(F=\zeta L(\cdot,\chi_4)\), \(d=2\), \(q_F=4\), \(\theta_F=0\), and \(\alpha=\sqrt{N_0}\), one has \(n_\alpha=N_0\). Here \(\alpha\asymp R^2\) grows with the summation length, and \(A_\rho\) is not the coefficient sequence of one fixed \(F\).

**Subconvex and moment inputs.** Bourgain's Theorem 5 in *Decoupling, exponential sums and the Riemann zeta function* ([primary PDF](https://arxiv.org/pdf/1408.5794), [DOI](https://doi.org/10.1090/jams/860)) states

\[
\zeta(1/2+it)\ll_\epsilon|t|^{13/84+\epsilon}.
\]

Corollary 1.3 of Petrow--Young, *The Weyl bound for Dirichlet \(L\)-functions of cube-free conductor* ([primary PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v192-n2-p03-s.pdf), [DOI](https://doi.org/10.4007/annals.2020.192.2.3)), gives

\[
L(1/2+it,\chi)\ll_\epsilon q_0^{1/6+\epsilon}(1+|t|)^{1/6+\epsilon}
\]

for primitive \(\chi\) of cube-free conductor \(q_0\), including fixed conductor \(4\). W. Müller's *The mean square of the Dedekind zeta function in quadratic number fields* ([primary DOI](https://doi.org/10.1017/S0305004100068134)) gives, in particular,

\[
\int_0^T|\zeta(1/2+it)L(1/2+it,\chi_D)|^2dt
\ll_D T(\log T)^2.
\]

Theorem 1 and Corollary 1 of W. Heap, *The twisted second moment of the Dedekind zeta function of a quadratic field* ([primary PDF](https://arxiv.org/pdf/1211.2182)), require

\[
\operatorname{supp}w\subset[T/2,4T],\quad
w^{(j)}\ll_jT_0^{-j},\quad
T^{1/2+\epsilon}\ll T_0\ll T,
\]

\[
(h,k)=1,\quad hk\le T^{2/11-\epsilon},\quad
|\alpha|+|\beta|+|\gamma|+|\delta|\ll(\log T)^{-1},
\]

and consequently allow an arbitrary Dirichlet-polynomial twist only to length \(T^{1/11-\epsilon}\). The present opposite shifts have imaginary separation up to \(R^{1/2}=U^{1/6}\), not \(O(1/\log U)\).

## 3. Proof or derivation

**Exact mask to constant cone.** Set

\[
u_h=L_h+1,\qquad D_h=y-u_h,\qquad a_h=\frac{4N_0h}{D_h^2}.
\]

Since \(0<\rho<1/8\), \(D_h\gg_\rho y\) for all relevant \(h\). Also

\[
N_0-D_h^2
=y^2+q-(y-u_h)^2
=2yu_h-u_h^2+q
\le2yu_h+q,
\]

where \(u_h\le\rho y/\sqrt h+1\) and \(q\le2y\). Hence

\[
0<a_h-4h
=4h\frac{N_0-D_h^2}{D_h^2}
\ll_\rho\sqrt h+\frac hy.
\]

The least odd \(r_h\ge a_h\) satisfies \(r_h<a_h+2\). Thus the odd integers present in \(r>4h\) but absent from \(r\ge r_h+2\) lie in \(4h<r\le r_h\), and there are \(O_\rho(1+\sqrt h)\) of them. Since \(hr\ll y\) and \(r>4h\), one has \(h\ll R\), while \(r\asymp h\) on this collar. Therefore the correction is bounded absolutely by

\[
\sum_{h\ll R}(1+\sqrt h)(h\cdot4h)^{-3/4}
\ll_\rho\sum_{h\ll R}(h^{-3/2}+h^{-1})
\ll_\rho1+\log R.
\]

This retains the floor in \(L_h\), the least-odd convention, the omitted boundary odd integer \(r_h\), and every \(q\in[0,2y]\).

**Smoothing and sharp Perron tails.** On \(h\asymp H\), choose \(C_H(v)\) equal to \(0\) for \(v\le1\), equal to \(1\) for \(v\ge1+cH^{-1/2}\), and satisfying

\[
C_H^{(j)}(v)\ll_jH^{j/2}.
\]

Replacing \(\mathbf1_{r>4h}\) by \(C_H(r/(4h))\) changes \(O(H^{1/2})\) values of \(r\) per height. With \(O(H)\) heights and weight \(O(H^{-3/2})\), the error is \(O(1)\) per block and \(O(\log R)\) in total.

For \(x\ne1\), truncated Perron has error

\[
\mathbf1_{x>1}
=\frac1{2\pi i}\int_{c-iT}^{c+iT}\frac{x^z}{z}\,dz
+O\!\left(x^c\min\left\{1,\frac1{T|\log x|}\right\}\right).
\]

For \(x=r/(4h)\), the closest admissible odd \(r\) has \(|\log x|\asymp h^{-1}\). Uniform sharp resolution requires \(T\gg H\), and \(1/|t|\) has no absolutely convergent tail. Only after the target-safe smoothing does the Mellin transform decay rapidly beyond

\[
|\Im t|\lesssim H^{1/2}X^\epsilon.
\]

**Exact two-variable factorization.** Put

\[
u=hr,\qquad v=\frac r{4h},\qquad
h=\sqrt{\frac{u}{4v}},\qquad r=\sqrt{4uv}.
\]

All radial, dyadic, and ratio factors form a smooth compactly supported \(\Psi_{H,K,N_0}(u,v)\). If

\[
\widetilde\Psi(s,t)
=\int_0^\infty\int_0^\infty
\Psi(u,v)u^sv^t\,\frac{du}{u}\frac{dv}{v},
\]

then on \(\Re(s-t)>1\) and \(\Re(s+t)>1\),

\[
\begin{aligned}
T^{\rm sm}_{H,K}
&=\sum_{h,r\ge1}\chi_4(r)
\Psi_{H,K,N_0}\!\left(hr,\frac r{4h}\right)\\
&=\frac1{(2\pi i)^2}\iint
\widetilde\Psi(s,t)4^t
\left(\sum_{h\ge1}h^{-s+t}\right)
\left(\sum_{r\ge1}\chi_4(r)r^{-s-t}\right)\,ds\,dt\\
&=\frac1{(2\pi i)^2}\iint
\widetilde\Psi(s,t)4^t\zeta(s-t)L(s+t,\chi_4)\,ds\,dt.
\end{aligned}
\]

Changing \(t\) to \(-t\) gives \(4^{-t}\zeta(s+t)L(s-t,\chi_4)\). Parity is exact because \(\chi_4(r)=0\) for even \(r\). The centre-dependent square-root phase remains in \(\widetilde\Psi\).

**Source power ledgers.** On a balanced block, put

\[
X_1\asymp\sqrt{N_0HK}.
\]

At \(H\asymp K\asymp R\), one has \(X_1\asymp R^3\) and weight \((HK)^{-3/4}\asymp R^{-3/2}\). For the direct exact-joint Robert--Sargos specialization \((H,N_1,M)=(R,R,1)\), the first term is

\[
R^2\left(\frac{R^3}{R^2}\right)^{1/4}=R^{9/4},
\]

so the normalized conclusion is only

\[
T_{R,R}\ll R^{3/4+\epsilon}.
\]

The term \(M^{-1/2}=1\) separately shows the absence of cancellation in the dummy direction, but it is not the dominant term. For the smoothed and Mellin-separated specialization \((H,N_1,M)=(R,1,R)\), the two long variables occupy separated coefficient slots, the raw bound is \(R^{2+\epsilon}\), and hence

\[
T_{R,R}\ll R^{1/2+\epsilon}.
\]

For the actual Sargos--Wu Theorem 9, the proved smoothing and Mellin separation likewise provide separated bounded coefficients. Take

\[
Z\asymp\sqrt{N_0HK}\asymp R^3,\qquad M=N_1=R,\qquad
\alpha=\beta=\frac12.
\]

After multiplying by \(R^{-3/2}\), the eleven terms in the displayed theorem have respective \(R\)-exponents

\[
\frac13,\ \frac{23}{66},\ \frac38,\ \frac{13}{40},\
\frac3{10},\ \frac25,\ \frac{15}{46},\ \frac38,\ 0,\ 0,\ -1.
\]

The maximum is \(2/5\), so this fixed-centre application yields only

\[
T_{R,R}\ll R^{2/5+\epsilon}.
\]

By contrast, the adjacent general-domain Lemma 5.2 can carry a joint staircase domain but excludes the rank-one phase because its Hessian condition contains \(\alpha+\beta-1\ne0\). Neither route reaches \(R^\epsilon\).

For a fixed TTY row \(h\asymp H\), the phase scale is \(T\asymp\sqrt{N_0hK}\), yielding

\[
\sum_{r\asymp K}\chi_4(r)e(\sqrt{N_0hr})
\ll_\epsilon(N_0HK)^{\kappa/2}K^{\lambda-\kappa+\epsilon}.
\]

After summing \(H\) rows and restoring the weight,

\[
T_{H,K}\ll_\epsilon
N_0^{\kappa/2}H^{1/4+\kappa/2}
K^{\lambda-3/4-\kappa/2}X^\epsilon.
\]

At \(H=K=R\), this is

\[
R^{2\kappa+\lambda-1/2+\epsilon}
=R^{267/641+\epsilon}.
\]

**Complete-coefficient return and directionality.** Completion gives

\[
d_{\chi_4}(m)=\sum_{r\mid m}\chi_4(r)=r_2(m)/4,
\qquad A_\rho(m)=d_{\chi_4}(m)-B_\rho(m),
\]

with \(B_\rho\) uncontrolled. At \(x=N_0\asymp R^4\) and \(M\asymp R^2\), Popov's remainder is \(O(RX^\epsilon)\), hence target-safe after division by \(R\). What remains is the complete cosine combination \(P(N_0)/R\), for which Li--Yang gives only

\[
\frac{P(N_0)}R
\ll R^{4\theta_*-1+\epsilon}
=R^{(50\sqrt{1717}-297)/6881+\epsilon}.
\]

This is not an individual positive-frequency branch bound: cancellation between the two conjugate branches may occur inside the cosine. Even for the real combination, the formula self-returns to the circle discrepancy. Kaczorowski--Perelli likewise exposes complete-coefficient resonance but lacks growing-\(\alpha\) uniformity.

**Mellin subconvex and moment ledger.** On the balanced block, let

\[
M=HK\asymp R^2,\qquad U=\sqrt{N_0M}\asymp R^3.
\]

On \(\Re s=1/2\), the product-variable Mellin transform has stationary size \(M^{-1/4}U^{-1/2}\) across an interval of length \(U\), and Mellin Plancherel gives

\[
\left(\int_{\mathbb R}|\widetilde F(1/2+i\tau)|^2\,d\tau\right)^{1/2}
\asymp M^{-1/4}.
\]

The ratio bandwidth is \(H^{1/2}\asymp R^{1/2}=U^{1/6}\). Bourgain plus Petrow--Young, used by absolute values, gives

\[
M^{-1/4}U^{1/2+13/84+1/6+\epsilon}
=R^{55/28+\epsilon}.
\]

Even granting the ideal uniform shifted mean square

\[
\int_U^{2U}
|\zeta(1/2+i(\tau+v))L(1/2+i(\tau-v),\chi_4)|^2\,d\tau
\ll U^{1+\epsilon}
\]

for \(|v|\le U^{1/6+\epsilon}\), Cauchy--Schwarz gives only

\[
M^{-1/4}U^{1/2+\epsilon}=R^{1+\epsilon}.
\]

Müller supplies the expected scale only at \(v=0\); Heap permits shifts \(O(1/\log U)\) and Dirichlet-polynomial length \(U^{1/11-\epsilon}\), below the \(U^{1/6}\) ratio bandwidth. Beating Cauchy requires signed correlation with the high-frequency kernel. Expanding that correlation by approximate functional equations recreates the square-root divisor twist and its canonical self-return.

## 4. First doubtful or unproved step

The first unproved step in the Mellin route is

\[
\zeta(s+t)L(s-t,\chi_4)\ \text{is subconvex or small on average}
\quad\Longrightarrow\quad
T^{\rm sm}_{H,K}\ll X^\epsilon.
\]

This does not follow from the cited hypotheses. The product-variable kernel occupies height \(U\asymp R^3\), the ratio variable occupies \(U^{1/6}\), and absolute-value or Cauchy use of even Lindelöf-strength input loses \(R\). The missing result is a centre-dependent oscillatory linear-functional estimate for oppositely shifted \(\zeta\) and \(L(\cdot,\chi_4)\), uniform for every real centre.

The other first failures are exact:

* Robert--Sargos: the smoothed/separated specialization retains \(R^{1/2}\), while the direct exact-joint dummy specialization retains \(R^{3/4}\).
* Sargos--Wu: Theorem 9 admits the square-root monomial with separated coefficients but retains \(R^{2/5}\); only the adjacent general-domain Lemma 5.2 excludes \(\alpha+\beta-1=0\).
* Tao--Trudgian--Yang: the valid conclusion retains \(R^{267/641}\).
* Banerjee--Khurana: the coefficient is complete, \(\nu=0\) is outside the strict strip, and the test function is analytic.
* Popov/Li--Yang: only the complete cosine combination is controlled, at \(R^{0.257932\ldots+\epsilon}\), not either complex branch, and completion leaves \(B_\rho\).
* Kaczorowski--Perelli: \(\alpha\) is fixed in the theorem but grows like \(R^2\) here; \(A_\rho\) is not a fixed \(L\)-function coefficient.
* Müller/Heap: their quadratic functionals are averaged, Heap's shifts and twist are too short, and neither gives the required signed linear functional.

Accordingly, the proved exact-mask correction and Mellin algebra are not the doubtful steps. Invalid additional steps would include truncating the sharp ratio Perron integral without its tail, deleting the complementary cone, inferring an individual branch bound from the cosine identity, or claiming fixed-centre uniformity from an averaged theorem.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_incomplete_fibre_mask_floors_profiles_and_real_centre` | **Pass for the reduction.** The exact \(L_h,D_h,r_h\), least-odd convention, \(0\le q\le2y\), and every real \(X\) are retained. The omitted collar has \(O(1+\sqrt h)\) odd points at height \(h\), for total weighted size \(O_\rho(\log R)\). |
| `dyadic_m_range_weight_and_small_m_owner` | **Pass.** The effective range \(m=hr\ll y\asymp R^2\), weight \((hr)^{-3/4}V_{\rm low}\), small-\(m\) ownership, and all dyadic blocks are retained. |
| `chi4_parity_divisor_pairing_and_complete_fibre_comparison` | **Pass.** Even \(r\) vanish in \(L(s,\chi_4)\); \(d_{\chi_4}=r_2/4\) is exact; \(B_\rho=d_{\chi_4}-A_\rho\) is not deleted. |
| `phase_cell_definition_width_multiplicity_and_endpoints` | **No near-radical result.** The ratio transition has relative width \(H^{-1/2}\), \(O(H^{1/2})\) values of \(r\) per height, and \(O(1)\) cost per block. |
| `exact_radical_versus_near_radical_separation` | **Retained.** Exact-radical safety is not extended to near radicals or nonsquares. |
| `nonresonant_complement_target_return` | **Fail/open.** No source returns the near-radical/nonsquare or completed-cone complement at \(X^\epsilon\). |
| `fourth_power_rays_and_prime_square_fibres` | **Pass as falsification.** They prohibit automatic fibre cancellation and are not treated as a scalar lower bound. |
| `coefficient_variation_or_additive_partial_sum_hypothesis` | **Fail for grouped one-dimensional use.** No suitable bound for \(A_\rho(m)\) was found; TTY is used only after fixing \(h\). |
| `source_theorem_parameter_and_R_power_audit` | **Pass.** Robert--Sargos gives \(R^{1/2}\) for the smoothed/separated specialization and \(R^{3/4}\) for the direct exact-joint dummy specialization; Sargos--Wu Theorem 9 gives \(R^{2/5}\) after separation; TTY gives \(R^{267/641}\); the complete Popov/Li--Yang cosine combination gives \(R^{0.257932\ldots}\); absolute Mellin subconvexity gives \(R^{55/28}\); and an ideal shifted mean square gives \(R\). The Popov/Li--Yang figure is not asserted for an individual complex branch. |
| `canonical_transform_self_return_and_circularity` | **Pass.** Popov returns the complete cosine combination to \(P(N_0)\); standard twists expose resonance; approximate functional equations return the square-root divisor twist. |
| `fixed_centre_signed_directionality` | **Pass.** Accepted reductions are pointwise and preserve \(\chi_4(r)e(\sqrt{N_0hr})\). Averaged theorems remain averaged. Popov/Li--Yang are limited to their cosine combination and are not used for the independent complex direction. |
| `lower_GAR_and_downstream_scope` | **Pass.** No energy, centre average, residual deletion, lower-GAR, exponent improvement, or downstream theorem is claimed. |

No numerical experiment was performed; the allocation was 100% analytical/source verification.

## 6. Dependencies and exact artifacts used

The permitted local dependencies used were:

* `protocol.md`;
* `state/proof_obligations.yml`;
* `state/active_campaign.yml`;
* `strategy/conductor_0823_full_proof_strategy.md`;
* `rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reviews/conductor_round140_height_alias_adjudication.md`;
* `rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/synthesis.md`;
* `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/synthesis.md`;
* `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/briefs/sqrt_divisor_twist_source_audit.md`.

Primary sources, with direct links, were:

* Robert--Sargos ([PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf));
* Sargos--Wu ([DOI](https://doi.org/10.1023/A:1006777803163)) and the 2019 Lemma 5.1 restatement together with adjacent general-domain Lemma 5.2 ([DOI](https://doi.org/10.1016/j.jnt.2019.01.008));
* Tao--Trudgian--Yang ([PDF](https://arxiv.org/pdf/2501.16779));
* Banerjee--Khurana ([PDF](https://arxiv.org/pdf/2306.12399));
* Popov ([article](https://www.mathnet.ru/eng/rm10162), [PDF](https://www.mathnet.ru/links/9d83ce675a9437c9b763883aa94a5cfb/rm10162_eng.pdf));
* Li--Yang ([PDF](https://arxiv.org/pdf/2308.14859));
* Kaczorowski--Perelli ([article](https://ems.press/journals/jems/articles/13843), [PDF](https://ems.press/content/serial-article-files/32124));
* Bourgain ([PDF](https://arxiv.org/pdf/1408.5794), [DOI](https://doi.org/10.1090/jams/860));
* Petrow--Young ([PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v192-n2-p03-s.pdf), [DOI](https://doi.org/10.4007/annals.2020.192.2.3));
* Müller ([DOI](https://doi.org/10.1017/S0305004100068134));
* Heap ([PDF](https://arxiv.org/pdf/1211.2182)).

No shared state, proof graph, validation matrix, synthesis, or proof draft was edited.

## 7. Recommended state effect

**Promote only the exact-mask/smoothing/Mellin reduction as a proved auxiliary lemma; retain the main gate as open.** The promotable statement is:

> Uniformly for every real centre in the Round-141 range, the exact floor-dependent far scalar equals the scalar with cone \(r>4h\) plus \(O_{\rho,\epsilon}(X^\epsilon)\). After dyadic localization in \(h\asymp H\), the cone may be smoothed across relative width \(H^{-1/2}\) at total cost \(O_{\rho,\epsilon}(X^\epsilon)\), and each smoothed block has an exact double-Mellin representation with arithmetic factor \(4^{-t}\zeta(s+t)L(s-t,\chi_4)\).

**Retain** the fixed-centre signed estimate \(T_N\ll X^\epsilon\), near-radical/nonsquare phase-cell estimate, and nonresonant complement as unresolved. **Reject** as closure mechanisms: direct Robert--Sargos or Sargos--Wu import, rowwise exponent pairs alone, completion to \(r_2/4\), inference from the complete cosine combination to an individual complex branch, fixed-parameter standard-twist theory, sharp Perron truncation without its tail, and subconvex/moment bounds used only through absolute values or Cauchy--Schwarz. A successful next step would require a genuinely oscillatory shifted-\(L\) linear-functional theorem, uniform for \(|v|\lesssim U^{1/6}\), or an equally explicit arithmetic phase-cell argument.
