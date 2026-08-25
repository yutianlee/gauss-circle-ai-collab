# Round 146 primary-source audit: three-variable monomial dispersion

- Campaign: `m9-m1-lower-cone-three-variable-hessian-dispersion-gate`
- Round: `146`
- Role: `source_auditor`
- Access mode: `selected_context`
- Starting graph SHA-256: `7d56a2cf6725cbcbd1746e41c300e01bd2028b9a855cbd057e02546df8a4d18d`
- Status: candidate evidence only; no shared proof-state edit
- Allocation: 100% analytic/algebraic/source verification; 0% numerical
- Outcome label: `three_variable_dispersion_no_go`

## 1. Result

### No-go lemma

Let \(R=X^{1/4}\), \(N=\lfloor X\rfloor\), and denote the radial dyadic scale by \(Q\) in this report (so that \(Q\) is the \(M\) of the frozen brief). On a box

\[
 t\asymp T,\qquad d\asymp D,\qquad e\asymp E,
 \qquad T^2DE\asymp Q,
\]

the phase is

\[
 g(t,d,e)=\sqrt N\,t\sqrt{de},\qquad
 \mathcal F:=\sqrt N\,T\sqrt{DE}\asymp \sqrt{NQ}.
\]

The following conclusions are rigorous.

1. The Round-144 nearest-square mask may be removed **completely but only at its already accepted threshold** inside the Round-145 small-\(t\) survivor: the deleted nonzero window \(0<|j_{st^2}|\le Q^{3/4}\), together with the exact-radical channel \(j=0\), has total weighted price \(O_{\varepsilon,V}(X^\varepsilon)\). The restriction \(t<Q^{1/4}\) can only decrease that absolute price. Independently, the Round-145 complement \(t\ge Q^{1/4}\) has total price \(O_{\varepsilon,V}(X^\varepsilon)\). This verifies the Round-144+145 unmasking seam. It does **not** authorize a new thicker phase window or an arbitrary internal smoothing partition.
2. The phase is genuinely nondegenerate on every three-dimensional positive box: its relative-coordinate Hessian determinant is \(1/4\), and its normalized gradient map is injective. Thus failure is not caused by the algebraic Hessian.
3. No audited primary theorem accepts the literal coefficient. The first exact source mismatch is the required separated or smooth amplitude: Cao--Zhai Theorem 6 permits only \(a(d)b(t,e)\), Cao--Zhai Theorem 7 permits only \(a(t)b(e)\) with no \(d\)-coefficient, Robert--Sargos permits only \(a(t,e)b(d)\), Sargos--Wu Theorem 9 permits only separated bilinear coefficients after \(t\) is frozen, and Sargos's multidimensional \(B\)-process permits a \(C^k_c\) amplitude but no arithmetic weight. The exact squarefree, coprimality, parity, character, auxiliary-divisor, strict-cone, product-profile, and block-endpoint ledger is a joint function of all three variables.
4. Even if one grants, at \(R^\varepsilon\) cost, every missing coefficient separation and every remaining profile/boundary reduction, Cao--Zhai Theorem 6 still does not reach the target. On the balanced top box

   \[
   Q=R^2,\qquad T=R^\tau,\qquad D=E=R^{1-\tau},
   \qquad 0\leq\tau<\tfrac12,
   \]

   its first displayed contribution, after the compulsory weight \(Q^{-3/4}=R^{-3/2}\), is

   \[
   R^{(3-5\tau)/8+\varepsilon}.
   \]

   At the formal limiting value \(\tau=1/2\) this is \(R^{1/16+\varepsilon}\); throughout every fixed-power small-\(t\) range \(\tau<1/2\) it is larger. All fourteen contributions are audited below. Taking the minimum with the trivial price \(R^{1/2-\tau+\varepsilon}\) is target-safe only at the already discharged endpoint \(T\asymp Q^{1/4}\), not on any new fixed-power intermediate corridor.
5. Sargos's exact three-dimensional van der Corput transformation also supplies no estimate here. It maps the phase to the same monomial shape, with dual side lengths \(\mathcal F/T,\mathcal F/D,\mathcal F/E\); trivial estimation of the transformed sum has weighted top capacity \(R^3\). A second transform returns the original phase up to the conventional sign/reflection. Hessian nondegeneracy by itself therefore creates no cancellation.

Consequently there is neither a source-legal target theorem nor a source-legal strict fixed-power intermediate-\(t\) reduction. This is a theorem-interface and upper-bound-power no-go, not a lower bound for the signed scalar and not a disproof of the desired target.

## 2. Exact statement and hypotheses

### 2.1 Frozen coefficient, masks, and phase scale

The retained scalar is

\[
 \mathfrak T_N=
 \sum_Q\sum_{1\le t<Q^{1/4}}
 \sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_Q\\
 |j_{s,t}|>Q^{3/4}}}
 (st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
 C(st^2)e(t\sqrt{Ns}),
\]

where \(k_{s,t}=\lfloor t\sqrt{Ns}+1/2\rfloor\) and
\(j_{s,t}=k_{s,t}^2-Nst^2\). The exact multiplicity-one coefficient is

\[
 C(st^2)=
 \sum_{\substack{\gamma\mid t\\
                   \gamma\ {\rm squarefree},\ (\gamma,s)=1\\
                   \gamma\ {\rm odd}}}
 \chi_4(\gamma)
 \sum_{\substack{de=s\\e\ {\rm odd}}}\chi_4(e)
 \sum_{\substack{ab=t/\gamma\\b\ {\rm odd}\\
                   eb^2>4da^2}}1.                                      \tag{2.1}
\]

Here \(de=s\) forces \(d,e\) to be squarefree and coprime. Equivalently,

\[
 C(st^2)=
 \sum_{de=s}^{\rm ord}
 \sum_{\substack{Gab=t\\(da,eb)=1\\Geb\ {\rm odd}\\
                   eb^2>4da^2}}
 \chi_4(Ge).                                                           \tag{2.2}
\]

There is no legal extra coprimality involving \(G\). After expanding \(de=s\), (2.1) is a joint coefficient in \(t,d,e\), because the divisor relation \(ab=t/\gamma\) and the strict cone \(eb^2>4da^2\) couple all three variables. The squarefree/coprimality/parity restrictions, \(\chi_4(\gamma e)\), the product condition \(t^2de\in\mathcal I_Q\), the profile \(V_{\rm low}(R^2t^2de/N)\), and (before the legal unmasking) \(j_{de,t}\) are additional joint factors.

The coefficient-blind number of triples on a \(T,D,E\) box is
\(TDE\asymp Q/T\). Thus its normalized absolute price is

\[
 Q^{-3/4}TDE\asymp Q^{1/4}/T.                                         \tag{2.3}
\]

### 2.2 Primary-source card: Cao--Zhai Theorem 6

Xiaodong Cao and Wenguang Zhai, [*Multiple exponential sums with monomials*, Acta Arith. 92 (2000), 195--213, Theorem 6](https://doi.org/10.4064/aa-92-3-195-213), define

\[
 S_I(M,M_1,M_2)=
 \sum_{m\sim M}\sum_{m_1\sim M_1}\sum_{m_2\sim M_2}
 a(m)b(m_1,m_2)e(A m^\alpha m_1^\beta m_2^\gamma).
\]

The exact stated hypotheses are

\[
 \alpha(\alpha-1)(\alpha-2)(\alpha-3)\gamma(\gamma-1)\ne0,
 \quad A\ne0,
 \quad M,M_1,M_2\ge1,
\]


\[
 |a(m)|\le1,qquad |b(m_1,m_2)|\le1,qquad
 F=|A|M^\alpha M_1^\beta M_2^\gamma\gg M.
\]

No restriction is imposed on \(\beta\). The conclusion is

\[
 |S_I|M^{-\varepsilon}\ll \sum_{i=1}^{14}\mathcal B_i,                \tag{2.4}
\]

where the fourteen \(\mathcal B_i\) are recorded, without omission, in the first formula column of the table in Section 3.3.

There is only one phase-legal placement, up to \(d\leftrightarrow e\):

\[
 m=d,\quad m_1=t,\quad m_2=e,qquad
 (\alpha,\beta,\gamma)=(\tfrac12,1,\tfrac12),qquad
 (M,M_1,M_2)=(D,T,E),quad A=\sqrt N.                                 \tag{2.5}
\]

Indeed, the linear \(t\)-exponent cannot occupy the \(\alpha\)-slot or the \(\gamma\)-slot because the theorem excludes \(\alpha=1\) and \(\gamma=1\). With (2.5),

\[
 F=\sqrt N\,D^{1/2}TE^{1/2}=\mathcal F=\sqrt{NQ}.
\]

Since \(Q\ll_VR^2\), \(D\le Q/T^2\), and \(\sqrt N\asymp R^2\), the condition \(F\gg D\) holds uniformly (and likewise after swapping \(d,e\)). The phase, dimension, sign \(A>0\), fixed center, and scale hypotheses therefore pass. The separated coefficient hypothesis does not.

### 2.3 Primary-source card: Cao--Zhai Theorem 7

In the same paper, Theorem 7 treats

\[
 S_{II}(M,M_1,M_2)=
 \sum_{m\sim M}\sum_{m_1\sim M_1}\sum_{m_2\sim M_2}
 a(m_1)b(m_2)e(A m^\alpha m_1^\beta m_2^\gamma).
\]

Its exact stated hypotheses are

\[
 M,M_1,M_2\ge1,qquad A>0,qquad
 \frac{\alpha\beta}{\alpha-1}\notin\{0,1,2,\ldots\},qquad
 a(m_1)\ll1,quad b(m_2)\ll1.
\]

Writing \(F=A M^\alpha M_1^\beta M_2^\gamma\), the displayed right side of (6.2) is

\[
\begin{aligned}
 |S_{II}|M^{-\varepsilon}\ll{}&
 (F^2M^3M_1^7M_2^7)^{1/8}
 +(F^4M_1^7M_2^7)^{1/8}
 +(F^{18}M^{15}M_1^{54}M_2^{54})^{1/58}\\
&+(F^{35}M^{26}M_1^{100}M_2^{100})^{1/108}
 +(F^{31}M^{24}M_1^{92}M_2^{92})^{1/98}
 +(F^{10}M^6M_1^{27}M_2^{27})^{1/29}\\
&+(F^{111}M^{86}M_1^{294}M_2^{294})^{1/336}
 +(F^{103}M^{74}M_1^{266}M_2^{266})^{1/304}
 +(F^{119}M^{74}M_1^{294}M_2^{294})^{1/336}\\
&+(F^{80}M^{19}M_1^{188}M_2^{188})^{1/200}
 +(F^{149}M^{34}M_1^{344}M_2^{344})^{1/368}
 +(F^{43}M^5M_1^{94}M_2^{94})^{1/100}\\
&+(F^2MM_1^6M_2^6)^{1/6}
 +(F^4M^{-1}M_1^8M_2^8)^{1/8}
 +F^{-1/2}MNH.                                                        \tag{2.6}
\end{aligned}
\]

The final symbols \(N,H\) in (2.6) are printed in the primary source but are not defined in this theorem. That final term is therefore **source-inconclusive in this audit** and is not silently repaired. This is immaterial to the present no-go because earlier, well-defined terms already fail by a fixed power.

The only useful placement is again (2.5), for which

\[
 \frac{\alpha\beta}{\alpha-1}=-1,
\]

so the phase condition passes. But Theorem 7 has no coefficient at all in the distinguished \(d\)-variable and requires the remaining coefficients to split as \(a(t)b(e)\). The literal coefficient fails this hypothesis. Even under ideal separation, its second term alone gives \(R^{7/8+\varepsilon}\) after top balanced normalization, independently of \(\tau\).

### 2.4 Primary-source card: Robert--Sargos Theorem 1

Olivier Robert and Patrick Sargos, [*Three-dimensional exponential sums with monomials*, J. reine angew. Math. 591 (2006), 1--20, Theorem 1](https://doi.org/10.1515/CRELLE.2006.012), consider

\[
 S_0=\sum_{h\sim H}\sum_{n\sim N_0}a(h,n)
       \sum_{m\sim M_0}b(m)
 e\!\left(\mathcal X\frac{h^\beta n^\gamma m^\alpha}
 {H^\beta N_0^\gamma M_0^\alpha}\right),
\]

where \(H,N_0,M_0\) are positive integers, \(\mathcal X>1\),
\(|a(h,n)|,|b(m)|\le1\), and
\(\alpha(\alpha-1)\beta\gamma\ne0\). Their conclusion is

\[
 S_0\ll_\varepsilon(HN_0M_0)^{1+\varepsilon}
 \left\{
 \left(\frac{\mathcal X}{HN_0M_0^2}\right)^{1/4}
 +(HN_0)^{-1/4}+M_0^{-1/2}+\mathcal X^{-1/2}
 \right\}.                                                          \tag{2.7}
\]

The favorable placement is

\[
 (h,n,m)=(t,e,d),\quad
 (\beta,\gamma,\alpha)=(1,\tfrac12,\tfrac12),\quad
 (H,N_0,M_0)=(T,E,D),\quad \mathcal X=\mathcal F.
\]

It accepts the individual positive complex sum at fixed \(N\), but only with a coefficient \(a(t,e)b(d)\). On the balanced top box, the first contribution in (2.7), after \(R^{-3/2}\) normalization, is \(R^{1/2-\tau/2+\varepsilon}\), hence \(R^{1/4+\varepsilon}\) at \(\tau=1/2\). It is weaker than the Cao--Zhai Theorem-6 contribution relevant here.

### 2.5 Primary-source card: Sargos--Wu Theorem 9

Patrick Sargos and Jie Wu, [*Multiple exponential sums with monomials and their applications in number theory*, Acta Math. Hungar. 87 (2000), 333--354, Theorem 9](https://doi.org/10.1023/A:1006777803163), give a bilinear monomial estimate for

\[
 S(M_1,N_1)=\sum_{m\sim M_1}a_m\sum_{n\sim N_1}b_n
 e\!\left(Z\frac{m^\alpha n^\beta}{M_1^\alpha N_1^\beta}\right).
\]

The exact relevant hypotheses are \(Z>0\), separated bounded coefficients
\(|a_m|,|b_n|\le1\), and

\[
 \alpha\beta(\alpha-1)(\beta-1)(\alpha-2)(\beta-2)\ne0.              \tag{2.8}
\]

Up to \((ZM_1N_1)^\varepsilon\), the theorem's displayed bound is the sum of

\[
\begin{gathered}
 (Z^4M_1^{31}N_1^{34})^{1/42},\quad
 (Z^6M_1^{53}N_1^{51})^{1/66},\quad
 (Z^6M_1^{46}N_1^{41})^{1/56},\\
 (Z^2M_1^{38}N_1^{29})^{1/40},\quad
 (ZM_1^9N_1^6)^{1/10},\quad
 (Z^2M_1^7N_1^6)^{1/10},\\
 (Z^3M_1^{43}N_1^{32})^{1/46},\quad
 (ZM_1^6N_1^6)^{1/8},\quad
 M_1^{1/2}N_1,\quad M_1N_1^{1/2},\quad Z^{-1/2}M_1N_1.              \tag{2.9}
\end{gathered}
\]

For a fixed \(t\)-row, take

\[
 (m,n)=(d,e),\qquad (\alpha,\beta)=(\tfrac12,\tfrac12),\qquad
 (M_1,N_1)=(D,E),\qquad Z=\mathcal F.
\]

The exponent hypothesis passes and the estimate is pointwise in the individual complex direction. The coefficient hypothesis fails because even at fixed \(t\), (2.1) contains the joint coprimality and strict cone. If separation and all boundary work are granted and the \(t\asymp T\) rows are summed trivially, the sixth contribution in (2.9) gives

\[
 Q^{-3/4}T(\mathcal F^2D^7E^6)^{1/10}
 =R^{\,2/5-3\tau/10+\varepsilon}                                  \tag{2.10}
\]

on the balanced top box. This is \(R^{2/5+\varepsilon}\) at \(t=1\) and still \(R^{1/4+\varepsilon}\) at the formal \(\tau=1/2\) endpoint. It is therefore weaker than Cao--Zhai Theorem 6 for the proposed three-variable use and does not handle the mandatory short face.

### 2.6 Primary-source card: Sargos's multidimensional \(B\)-process

Patrick Sargos, [*The multidimensional van der Corput transformation*, Functiones et Approximatio 52.1 (2015), 133--176, Theorem 5.2 and Proposition 5.2](https://doi.org/10.7169/facm/2015.52.1.11), works in fixed dimension \(p>1\) with

\[
 S=\sum_{\mathbf m\in\mathbb Z^p}
 \chi(\mathbf m/\mathbf M)e(\mathcal T f(\mathbf m/\mathbf M)).
\]

The hypotheses in Section 5.1 are: \(k>p+5\); a connected bounded open \(\Omega\subset\mathbb R^p\); \(f\in C^k(\Omega,\mathbb R)\); \(\chi\in C_c^k(\Omega,\mathbb C)\), extended by zero; \(\mathcal T,M_1,\ldots,M_p>1\); uniformly bounded derivatives of \(f\) of orders \(2,\ldots,k\) and of \(\chi\) of orders \(0,\ldots,k\); support a fixed positive distance from \(\Omega^c\); 

\[
 |\det H_f(x)|\ge\delta>0\quad(x\in\Omega),
 \qquad f':\Omega\longrightarrow\mathbb R^p\ \text{injective}.       \tag{2.11}
\]

Put \(N_i=\mathcal T/M_i\), \(P=M_1\cdots M_p\), let \(\omega=(f')^{-1}\), and use Sargos's convention
\(f^*(y)=f(\omega(y))-\langle y,\omega(y)\rangle\). With

\[
 R_0=\frac{P}{\mathcal T^p}
 \#\{\mathbf n\in\mathbb Z^p:\mathbf n/\mathbf N\in f'(\Omega)\},
\]

Theorem 5.2 gives

\[
\begin{aligned}
 S={}&\frac{P}{\mathcal T^{p/2}}e^{i\pi\sigma/4}
 \sum_{\mathbf n\in\mathbb Z^p}
 \frac{\chi(\omega(\mathbf n/\mathbf N))}
 {|\det H_f(\omega(\mathbf n/\mathbf N))|^{1/2}}
 e(\mathcal T f^*(\mathbf n/\mathbf N))\\
 &+O(R_0\mathcal T^{(p-1)/2}\delta^{-2})
 +O\!\left(\frac{R_0\mathcal T^p}{(\mathcal T\delta^6)^{k-1}}\right)
 +O\!\left(\prod_{i=1}^p(\mathcal T+M_i)
             (\mathcal T\delta^2)^{-(k-1)}\right).                  \tag{2.12}
\end{aligned}
\]

Proposition 5.2 treats a compact geometric boundary \(D_0\) by inserting an integral over \(\vartheta\in[0,1]^p\), a boundary Fourier factor \(Z_{D_0}(\vartheta)\), and
\(\mu(D_0)=\int|Z_{D_0}(\vartheta)|d\vartheta\); for a hyperrectangle it has \(\mu(D_0)\ll L^p\). Its errors carry this \(\mu(D_0)\). Neither result permits an arbitrary arithmetic coefficient. The later regular-boundary Theorem 5.3 additionally carries a lattice-near-boundary counting error; it is not a coefficient-weighted black-box estimate.

For the coefficient-free normalized target phase \(f(x,y,z)=x\sqrt{yz}\) on a compact positive box, (2.11) passes with \(\delta\asymp1\), and the gradient is injective. The literal arithmetic amplitude and the short faces do not pass.

### 2.7 Newer-primary-source screen

- Jiamin Li and Jing Ma, [*Three-dimensional exponential sums under constant perturbation*, Indag. Math. 34 (2023), 1223--1236, Theorem 1.1](https://doi.org/10.1016/j.indag.2023.04.001), treat

  \[
  \sum_{h\sim H,m\sim M,n\sim N_0}a(h,m)b(n)
  e\!\left(\mathcal X\frac{M^\beta N_0^\gamma}{H^\alpha}
  \frac{h^\alpha}{m^\beta n^\gamma+\delta}\right),
  \]

  with \(\alpha,\beta,\gamma>0\), \(\delta>0\), \(\mathcal X\le(8\delta)^{-1}KM^\beta N_0^\gamma\), and separated \(a(h,m)b(n)\). Their bound is

  \[
  (HMN_0)^{1+\varepsilon}
  \left\{\left(\frac{K\mathcal X}{HMN_0^2}\right)^{1/4}
  +\left(\frac{K^2}{HM}\right)^{1/4}
  +\left(\frac K{N_0}\right)^{1/2}
  +\frac K{\mathcal X^{1/2}}\right\}.
  \]

  This is a reciprocal, constantly perturbed phase. The authors explicitly note that Robert--Sargos implies their displayed bound when \(\delta=0\). It is not an improvement for the positive-power phase \(t\sqrt{de}\), and its coefficient class is still separated.
- Javier Pliego, [*Estimates for a three-dimensional exponential sum with monomials*, J. Théorie des Nombres de Bordeaux 36 (2024), 725--766, Corollary 1.1](https://doi.org/10.5802/jtnb.1294), obtains a bound for one special weighted sum with phase \(\kappa h^bn^cm^{-a}\), conditions \(0<a<c<b\), \(b+c-a=1\), \(c<2a\), a prescribed weight, and a prescribed curved global domain \(D_T\). It is not a rectangular theorem for three positive exponents, nor does it permit the target coefficient.
- Lingyu Guo, Victor Z. Guo, and Mengyao Jing, [*Exponential sums with polynomials and their applications to primes in sparse sets*, arXiv:2510.20562v1 (2025), Theorem 1.1](https://arxiv.org/abs/2510.20562), treat a two-variable bilinear polynomial-phase sum with \(mn\asymp X\). It is not a three-variable refinement applicable to this box.

Thus the newer audited primary results do not improve the Cao--Zhai Theorem-6 normalization for the present exponent vector and coefficient class.

## 3. Proof or derivation

### 3.1 Owner-complete mask removal and the Round-145 complement

The proved node `M9-M1-lower-far-cone-microscopic-cell-reduction` gives, on each literal half-open radial block,

\[
 \#\{m\in\mathcal I_Q:0<|j_m|\le J\}\ll_\varepsilon JX^\varepsilon
\]

and

\[
 \#\{m\in\mathcal I_Q:|j_m|\le J\}
 \ll_\varepsilon (J+\sqrt Q+1)X^\varepsilon,
\]

with the exact-radical fibre separately target-safe. Since \(C(m)\ll_\varepsilon m^\varepsilon\), the nonzero window has weighted price

\[
 Q^{-3/4}JX^\varepsilon.
\]

At \(J=Q^{3/4}\) this is \(O(X^\varepsilon)\). Intersecting with the unique-square-part condition \(t<Q^{1/4}\) only removes terms, so it cannot increase this absolute price. Therefore, if \(\widetilde{\mathfrak T}_{N,<}\) denotes the Round-145 small-\(t\) scalar with the condition 
\(|j|>Q^{3/4}\) deleted, including the target-safe exact radicals, then

\[
 \mathfrak T_{N,<}=\widetilde{\mathfrak T}_{N,<}+O_{\varepsilon,V}(X^\varepsilon). \tag{3.1}
\]

This is the exact source-theorem unmasking seam. It does not remove squarefreeness, coprimality, the strict cone, the product profile, or the half-open endpoints.

Separately, `M9-M1-lower-cone-squarefree-kernel-reduction` proves

\[
 \sum_{t\ge T}(\text{absolute weighted terms on }\mathcal I_Q)
 \ll_{\varepsilon,V}X^\varepsilon Q^{1/4}/T.
\]

Taking \(T=Q^{1/4}\) and assembling the logarithmically many blocks proves the Round-145 large-\(t\) complement target-safe. These two reductions are compatible and leave exactly the unmasked small-\(t\) coefficient problem.

### 3.2 Hessian, gradient, and aspect ratios

Direct differentiation gives

\[
 g^{-1}\operatorname{diag}(t,d,e)\nabla^2g\operatorname{diag}(t,d,e)
 =\begin{pmatrix}
 0&1/2&1/2\\
 1/2&-1/4&1/4\\
 1/2&1/4&-1/4
 \end{pmatrix},qquad \det=\frac14.                                  \tag{3.2}
\]

Its inertia is one positive and two negative directions. For
\(f(x,y,z)=x\sqrt{yz}\),

\[
 \det H_f(x,y,z)=\frac{x}{4\sqrt{yz}},
\]

which is bounded away from zero on a normalized positive box, and

\[
 f'(x,y,z)=\left(\sqrt{yz},\frac x2\sqrt{z/y},\frac x2\sqrt{y/z}\right)
\]

has the unique inverse

\[
 x=2\sqrt{vw},\qquad y=u\sqrt{w/v},\qquad z=u\sqrt{v/w}.
\]

Thus all smooth phase-only hypotheses of Sargos's \(p=3\) transform hold. This does not cover \(T=1\), \(D=1\), or \(E=1\) as a genuinely growing three-dimensional box. In particular, fixing \(t\) leaves the two-variable phase \(\sqrt{de}\), whose relative Hessian

\[
 \begin{pmatrix}-1/4&1/4\\1/4&-1/4\end{pmatrix}
\]

has determinant zero. The mandatory \(t=1\) and bounded-\(t\) layers therefore return exactly to the rank-one obstruction, regardless of the nonzero three-dimensional determinant. Cao--Zhai formally allows a side length equal to \(1\), but its stated upper bound then supplies no genuinely three-variable saving and still has the coefficient mismatch.

### 3.3 Complete Cao--Zhai Theorem-6 power ledger

Under the only legal placement (2.5), multiply every source contribution by the exact radial weight \(Q^{-3/4}\). On the balanced top box \(Q=R^2\), \(T=R^\tau\), \(D=E=R^{1-\tau}\), \(\mathcal F=R^3\), write

\[
 Q^{-3/4}\mathcal B_i=R^{\eta_i(\tau)+\varepsilon}.
\]

The complete ledger is:

| \(i\) | exact \(\mathcal B_i\) after \(M=D,M_1=T,M_2=E,F=\mathcal F\) | \(\eta_i(\tau)\) | \(\eta_i(1/2)\) |
|---:|---|---:|---:|
| 1 | \((\mathcal F D^5T^7E^7)^{1/8}\) | \((3-5\tau)/8\) | \(1/16\) |
| 2 | \((D^8T^7E^7)^{1/8}\) | \(3/8-\tau\) | \(-1/8\) |
| 3 | \((\mathcal F^4D^{43}T^{54}E^{54})^{1/58}\) | \((22-43\tau)/58\) | \(1/116\) |
| 4 | \((\mathcal F^7D^{82}T^{100}E^{100})^{1/108}\) | \((41-82\tau)/108\) | \(0\) |
| 5 | \((\mathcal F^3D^{37}T^{46}E^{46})^{1/49}\) | \((37-74\tau)/98\) | \(0\) |
| 6 | \((\mathcal F^3D^{46}T^{54}E^{54})^{1/58}\) | \((11-23\tau)/29\) | \(-1/58\) |
| 7 | \((\mathcal F^{29}D^{250}T^{294}E^{294})^{1/336}\) | \((127-250\tau)/336\) | \(1/168\) |
| 8 | \((\mathcal F^{25}D^{230}T^{266}E^{266})^{1/304}\) | \((115-230\tau)/304\) | \(0\) |
| 9 | \((\mathcal F^{25}D^{262}T^{294}E^{294})^{1/336}\) | \((127-262\tau)/336\) | \(-1/84\) |
| 10 | \((\mathcal F^{-1}D^{181}T^{188}E^{188})^{1/200}\) | \((66-181\tau)/200\) | \(-49/400\) |
| 11 | \((\mathcal F^{-1}D^{334}T^{344}E^{344})^{1/368}\) | \((123-334\tau)/368\) | \(-11/92\) |
| 12 | \((\mathcal F^{-4}D^{190}T^{188}E^{188})^{1/200}\) | \((66-190\tau)/200\) | \(-29/200\) |
| 13 | \((D^5T^6E^6)^{1/6}\) | \((2-5\tau)/6\) | \(-1/12\) |
| 14 | \((\mathcal F^{-1}D^9T^8E^8)^{1/8}\) | \((2-9\tau)/8\) | \(-5/16\) |

For example, term 1 is exactly

\[
 Q^{-3/4}(\mathcal F D^5T^7E^7)^{1/8}.                               \tag{3.3}
\]

Using \(\mathcal F\asymp R^2Q^{1/2}\) and \(DE\asymp Q/T^2\), (3.3) may also be written

\[
 R^{1/4}Q^{-1/16}E^{1/4}T^{-3/8}                                   \tag{3.4}
\]

when \(d\) is the distinguished variable; after \(d\leftrightarrow e\), the final \(E^{1/4}\) is replaced by \(D^{1/4}\). For **term 1 alone**, its smaller version is obtained by taking the larger of \(D,E\) as the distinguished side. One theorem placement must then be held fixed across all fourteen terms; termwise swapping is not legal. Balanced boxes remain mandatory and give (3.3) with exponent \((3-5\tau)/8\).

Term 1 would become target-sized only at \(\tau\ge3/5\), outside the small-\(t\) range. At \(\tau=1/2\), terms 1, 3, and 7 are still positive, with term 1 largest. The \(O(\log^C X)\) dyadic assembly is absorbable in \(X^\varepsilon\), but no logarithm absorbs the fixed \(R^{1/16}=X^{1/64}\) loss. Since the theorem's right side is a sum of these nonnegative displayed contributions, term 1 cannot be discarded.

The coefficient-blind bound (2.3) is \(R^{1/2-\tau+\varepsilon}\). Hence, even after taking the better of the theorem and the trivial estimate, every fixed \(\tau<1/2\) retains a positive power. The constant-factor layer immediately below \(T=Q^{1/4}\) is already target-safe by (2.3); Cao--Zhai creates no new fixed-power range.

### 3.4 Exact coefficient and boundary mismatch

The source-theorem tensor \(a(d)b(t,e)\) cannot equal the literal amplitude without a new decomposition theorem. The obstructions are concrete:

- \(1_{de\ {\rm squarefree}}\) imposes squarefreeness and \((d,e)=1\);
- \(\gamma\mid t\), \((\gamma,de)=1\), and \(ab=t/\gamma\) couple the \(t\)-variable to the auxiliary divisors;
- \(eb^2>4da^2\) is a sharp moving cone coupling \(d,e,a,b\);
- \(\chi_4(\gamma e)\) and the oddness restrictions depend on both sides of that cone;
- \(t^2de\in\mathcal I_Q\) is a sharp product boundary, while \(V_{\rm low}(R^2t^2de/N)\) is a smooth but joint product profile;
- before (3.1), \(1_{|j_{de,t}|>Q^{3/4}}\) is a discontinuous three-variable mask.

Möbius, Mellin, or Perron expansions may be plausible tools, but no permitted artifact proves an owner-complete expansion with \(R^\varepsilon\) total norm, uniform rectangular endpoints, and every cone boundary term. The Round-144 cell theorem supplies exactly (3.1) and nothing broader. Even granting all of these missing steps cannot overcome the independent power obstruction in Section 3.3.

### 3.5 Exact dual transform and self-return

For the unscaled phase \(g(t,d,e)=a\,t\sqrt{de}\), \(a=\sqrt N\), write the physical gradient variables as

\[
 u=a\sqrt{de},\qquad
 v=\frac{at}{2}\sqrt{e/d},\qquad
 w=\frac{at}{2}\sqrt{d/e}.
\]

The inverse is

\[
 t=\frac{2\sqrt{vw}}a,\qquad
 d=\frac ua\sqrt{w/v},\qquad
 e=\frac ua\sqrt{v/w}.                                               \tag{3.5}
\]

Euler homogeneity gives \(ut+vd+we=2g\). Consequently Sargos's dual convention gives

\[
 g^*(u,v,w)=g-(ut+vd+we)=-\frac{2u\sqrt{vw}}{\sqrt N}.                \tag{3.6}
\]

The conventional Legendre transform has the opposite sign. In either convention, the exponent vector is again \((1,1/2,1/2)\). Applying the transform again after the required alias-orthant reversal returns the original monomial **only at the phase level**; it does not return the arithmetic amplitude, boundary, or stationary factors. No conjugate-pair or cosine replacement has been used.

On a \(T,D,E\) box the dual side lengths are

\[
 \mathcal F/T,\qquad \mathcal F/D,\qquad \mathcal F/E.              \tag{3.7}
\]

The ideal smooth-interior dual-region volume is \(\asymp\mathcal F^3/(TDE)\); this is only an upper-order count for the supported dual aliases unless one separately supplies a boundary-lattice estimate. Multiplying that upper-order count by the local stationary-phase prefactor \(TDE/\mathcal F^{3/2}\) from (2.12) gives only the idealized transformed capacity scale

\[
 \mathcal F^{3/2}.                                                     \tag{3.8}
\]

At the top \(\mathcal F=R^3\), (3.8), multiplied by \(R^{-3/2}\), is \(R^3\). Also \(R_0\asymp1\), so the first error in the transform formula (2.12) has weighted size \(R^{3/2}\). Sargos notes that the standard useful \(B\)-process regime has both \(\mathcal F/M_i\) large and \(\mathcal F/M_i^2\) small. Here, on the balanced top box,

\[
 \mathcal F/T^2=R^{3-2\tau},\qquad
 \mathcal F/D^2=\mathcal F/E^2=R^{1+2\tau},
\]

so the second condition fails in every direction. A nontrivial bound for the much longer dual sum would be a new theorem of essentially the same monomial type, not a consequence of nonzero Hessian.

### 3.6 Fixed center, complex direction, and the slow family

Cao--Zhai Theorem 6 is pointwise for \(A\ne0\), Theorem 7 for \(A>0\), Robert--Sargos for \(\mathcal X>1\), and Sargos for one real phase. Thus \(A=\sqrt{\lfloor X\rfloor}>0\) and the individual direction \(e(+g)\) are phase-legal. None of these cards requires an average over the center or a conjugate pair. The failure lies elsewhere.

They also do not authorize an additional gradient-separation assumption. For squarefree \(s>1\), take

\[
 N=sL^2+1,qquad
 \sqrt{Ns}=sL+\rho,qquad
 \rho=\frac1{\sqrt{L^2+1/s}+L}.
\]

Whenever \(t\rho<1/2\),

\[
 k_{s,t}=sLt,qquad j_{st^2}=-st^2,qquad
 e(t\sqrt{Ns})=e(t\rho).                                             \tag{3.9}
\]

Thus the large-displacement mask is satisfied for \(st^2>1\), while the phase rotates arbitrarily slowly on an allowed \(t\)-range. For \(t=1\) and a prime \(s=p>4\), \(C(p)=\chi_4(p)\ne0\). Equation (3.9) falsifies any uniform Kusmin--Landau gap, empty-dual-lattice, or fixed-discriminant Diophantine shortcut. It is not a signed lower bound: cancellation across \(s\), boxes, or coefficient signs remains possible.

## 4. First doubtful or unproved step

The first exact source-applicability failure is the amplitude hypothesis. To invoke the strongest audited generic theorem one would have to prove an identity or bounded-norm superposition

\[
 \mathcal A(t,d,e)=\sum_\nu a_\nu(d)b_\nu(t,e),
 \qquad
 \sum_\nu\|a_\nu\|_\infty\|b_\nu\|_\infty\ll R^\varepsilon,         \tag{4.1}
\]

where \(\mathcal A\) contains (2.1), every squarefree/coprimality/parity condition, the strict cone, the literal product profile, and all endpoint corrections. No audited source or permitted artifact proves (4.1). Cao--Zhai Theorem 7 would require the still stronger absence of any distinguished-variable coefficient.

Even if (4.1) and every geometric separation are granted, Section 3.3 is an independent rigorous obstruction to this source route: Theorem 6's displayed term 1 leaves \(R^{(3-5\tau)/8}\), including \(R^{1/16}\) at the formal endpoint. Thus proving (4.1) alone cannot close even a new fixed-power balanced intermediate-\(t\) range.

The first genuinely open estimate remains a signed estimate for the exact unmasked small-\(t\) coefficient, strong enough on balanced \(T,D,E\) boxes to beat both the coefficient-blind price and every positive Cao--Zhai exponent. It must separately include the \(t=1\) and bounded-\(t\) rank-one faces. No theorem audited here supplies that input.

## 5. Required control tests and outcomes

| Control | Test | Outcome |
|---|---|---|
| `exact_t_d_e_coefficient_and_multiplicity` | Reproduce both multiplicity-one formulas and retain all auxiliary variables. | **Pass for ledger; source fail.** Equations (2.1)--(2.2) are exact. No audited coefficient class contains them. |
| `literal_profile_mask_and_block_endpoints` | Check what can legally be removed. | **Partial pass.** The nearest-square mask alone may be removed by (3.1). The product profile, half-open endpoint, strict cone, and any new internal partition still need an owner-complete separation. |
| `three_variable_scaled_Hessian_determinant` | Differentiate in \(t,d,e\). | **Pass.** The determinant is \(1/4\), with normalized \(\det H_f=x/(4\sqrt{yz})\asymp1\). |
| `aspect_ratio_and_short_face_ledger` | Test balanced, unbalanced, and length-one faces. | **No-go.** Balanced boxes force the positive term-1 power. \(t=1\) collapses to the rank-one \(\sqrt{de}\) phase; \(D=1\) or \(E=1\) is not a genuine three-dimensional box. |
| `M_T_D_E_capacity_and_dyadic_assembly` | Insert \(\mathcal F=\sqrt{NQ}\), \(T^2DE=Q\), and \(Q^{-3/4}\) in every source term. | **Pass; adverse.** All fourteen exponents are in Section 3.3. Logs are harmless, the fixed powers are not. |
| `t_equals_one_and_bounded_t_boundary` | Freeze \(t\). | **Fail for the proposed mechanism.** The remaining two-variable Hessian has determinant zero, and the exact coefficient remains nonseparable. |
| `exceptional_slow_frequency_family` | Test \(N=sL^2+1\). | **Adverse control.** Equation (3.9) survives the large-displacement mask and rules out uniform derivative/Diophantine separation. |
| `individual_complex_direction_and_fixed_centre` | Check source sign and parameter uniformity without cosine or averaging. | **Pass phase-only.** The sources bound one complex sum pointwise at positive \(A=\sqrt N\). No conjugate pairing was used. |
| `primary_source_dimension_coefficient_and_power_match` | Audit theorem statements, not titles or abstracts. | **Fail.** Dimension/phase pass for Cao--Zhai 6 and Sargos 5.2; coefficient fails first, and the idealized power fails independently. Sargos--Wu 9 is only bilinear after freezing \(t\) and leaves \(R^{1/4}\) even at the formal top endpoint. Cao--Zhai 7 also contains a printed undefined-variable term. |
| `dual_transform_and_self_return_controls` | Compute the inverse gradient, dual phase, dual lengths, and transformed capacity scale. | **Adverse control.** Equations (3.5)--(3.8) give phase-level monomial self-return after orthant reversal and the idealized weighted capacity scale \(R^3\); the alias volume remains only upper-order without a boundary count. |
| `strict_survivor_complement_target_safety` | Combine the Round-144 cell window with the Round-145 large-\(t\) tail. | **Pass.** Both complements are \(O(X^\varepsilon)\); only the exact small-\(t\) signed scalar remains. |
| `Round138_cross_owner_and_downstream_scope` | Check whether this source audit discharges any independent owner. | **No.** The Round-138 collar-tail cross owner, lower GAR, direct M1 parents, all M2 owners, endpoint uniformity, M9, the bridge, and any global exponent remain untouched. |

## 6. Dependencies and exact artifacts used

Only the assigned repository context was used:

- `protocol.md`;
- `state/proof_obligations.yml`, in particular `M9-M1-lower-far-cone-microscopic-cell-reduction` and `M9-M1-lower-cone-squarefree-kernel-reduction`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/candidates/conductor_round145_squarefree_kernel_reduction.md`;
- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/reports/quadratic_irrational_divisor_twist_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reports/sqrt_divisor_twist_source_audit.md`.

The theorem statements were checked in the following primary sources:

1. X. Cao and W. Zhai, [Acta Arith. 92 (2000), 195--213](https://matwbn.icm.edu.pl/ksiazki/aa/aa92/aa9231.pdf), Theorems 6--7, printed pp. 211--212.
2. O. Robert and P. Sargos, [J. reine angew. Math. 591 (2006), 1--20](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf), Theorem 1, pp. 1--2.
3. P. Sargos and J. Wu, [Acta Math. Hungar. 87 (2000), 333--354](https://doi.org/10.1023/A:1006777803163), Theorem 9.
4. P. Sargos, [Functiones et Approximatio 52.1 (2015), 133--176](https://doi.org/10.7169/facm/2015.52.1.11), Section 5.1, Theorem 5.2, Proposition 5.2, and Theorem 5.3.
5. J. Li and J. Ma, [Indag. Math. 34 (2023), 1223--1236](https://arxiv.org/pdf/2302.05870), Theorem 1.1.
6. J. Pliego, [J. Théorie des Nombres de Bordeaux 36 (2024), 725--766](https://www.numdam.org/item/10.5802/jtnb.1294.pdf), Corollary 1.1 and its domain/weight definitions.
7. L. Guo, V. Z. Guo, and M. Jing, [arXiv:2510.20562v1 (2025)](https://arxiv.org/pdf/2510.20562), Theorem 1.1.

No title, abstract, or secondary quotation was used as a substitute for a theorem statement. No numerical experiment was performed.

## 7. Recommended state effect

**Recommended effect: reject** the proposed inference that the nonzero three-variable Hessian, Cao--Zhai/Robert--Sargos monomial bounds, or a multidimensional \(B\)-process makes a new fixed-power small-\(t\) range target-safe.

Retain unchanged the proved Round-144 nearest-square deletion and Round-145 large-\(t\) deletion. If the conductor records this report, it supports only a scoped obstruction: (i) exact separated/smooth-coefficient hypothesis failure, (ii) the independent Cao--Zhai Theorem-6 term-1 loss \(R^{(3-5\tau)/8}\), (iii) mandatory short-face collapse, and (iv) phase-level dual monomial self-return after orthant reversal. It does not change the target's open status and has no downstream theorem or exponent effect.
