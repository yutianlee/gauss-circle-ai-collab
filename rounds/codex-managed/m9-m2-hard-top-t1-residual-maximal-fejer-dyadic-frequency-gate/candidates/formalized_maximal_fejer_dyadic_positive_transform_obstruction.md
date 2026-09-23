# Candidate kernel: residual maximal parity--Fejer positive-transform obstruction

Status: candidate Round-172 proof kernel  
Terminal scope: maximal_fejer_dyadic_character_poisson_no_go

## 1. Statement and hypotheses

Let \(e(t)=e^{2\pi it}\), \(J=\sqrt X\),

\[
 1\ll L\ll H\le J^{1/2},\qquad R_0=\lceil L\rceil<M,
 \qquad M\asymp L^2.
\tag{172.K1}
\]

Retain the complete literal residual opening

\[
 c_N^{\rm rem}=\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\lambda_N(d),
\tag{172.K2}
\]

where \(\lambda_N(d)\) contains pointwise every selected/no-pair selector,
squarefree/coprimality hole, complementary parity branch, profile, floor,
star, crossing, endpoint, hard point value, and zero-extension value. On
nonzero incidences \(N=dm\asymp L^2\), one has \(d,m\asymp L\) and
\(\lvert\lambda_{dm}(d)\rvert\ll1\). Extend by zero outside a positive
shell contained in \(M\) consecutive sites and put

\[
 z_N=c_N^{\rm rem}e(J\sqrt N),\quad
 C_r=\sum_Nz_{N+r}\overline{z_N},\quad A_r=\Re C_r,
\]

\[
 Z(\theta)=\sum_Nz_Ne(N\theta),\qquad
 D_L=C_0=\sum_N|z_N|^2\ll_\eta L^2X^\eta
\tag{172.K3}
\]

for every \(\eta>0\). The result below is one route-scoped obstruction:
the exact parity--Fejer chain and exact literal transform exist, and their
ordinary-zero-containing part is target-safe, but the first positive
replacement of the remaining signed nonzero-mode aggregate has sharp
capacity \(M D_L\asymp L^4X^\eta\), not \(L^3X^\varepsilon\).

## 2. Exact parity--Fejer stopped chain

For positive integer \(R\), define

\[
 F_R(\theta)=R^{-1}\left|\sum_{0\le j<R}e(j\theta)\right|^2,
 \qquad K_R^{(2)}(\theta)=\frac{F_R(\theta)+F_R(\theta+1/2)}2,
\]

\[
 \mathfrak E_R^{(2)}
 =\int_0^1K_R^{(2)}(\theta)|Z(\theta)|^2\,d\theta.
\]

Finite Fourier expansion gives

\[
 K_R^{(2)}(\theta)=
 \sum_{\substack{|r|<R\\2\mid r}}
 \left(1-\frac{|r|}{R}\right)e(r\theta),
 \qquad
 \mathfrak E_R^{(2)}=D_L+2\sum_{\substack{0<r<R\\2\mid r}}
 \left(1-\frac rR\right)A_r.
\tag{172.K4}
\]

Thus the diagonal coefficient is one, both absolute site parities remain,
and one real part is taken only after the positive-shift sum.

Let \(R_{j+1}=\min(2R_j,M)\), stopping at \(R_K=M\), and put
\(S=\min(2R_0,M)\). For

\[
 T_{26}=\sum_{\substack{R_0\le r<M\\2\mid r}}
 \left(1-\frac rM\right)A_r,
\]

ordinary telescoping gives exactly

\[
 T_{26}=\frac12\sum_{j=0}^{K-1}
 \bigl(\mathfrak E_{R_{j+1}}^{(2)}
       -\mathfrak E_{R_j}^{(2)}\bigr)-B_{\rm sh},
\tag{172.K5}
\]

\[
 B_{\rm sh}=\left(\frac1{R_0}-\frac1M\right)
 \sum_{\substack{0<r<R_0\\2\mid r}}rA_r,\qquad
 |B_{\rm sh}|\ll R_0D_L\ll_\eta L^3X^\eta.
\tag{172.K6}
\]

This is the only short correction. Full-line zero extension gives
\(|C_r|\le D_L\), without evaluating \(\sqrt N\) off positive support.

For integers \(R<S\le2R\), direct subtraction gives

\[
 b_{R,S}(r)=
 \begin{cases}
  r(S-R)/(RS),&0<r<R,\\
  1-r/S,&R\le r<S,\\
  0,&r\ge S,
 \end{cases}
 \qquad b_{R,S}(0)=0,
\tag{172.K7}
\]

\[
 \mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}
 =2\sum_{\substack{0<r<S\\2\mid r}}b_{R,S}(r)A_r,\qquad
 \sum_{r=1}^{S-1}b_{R,S}(r)=\frac{S-R}{2}.
\tag{172.K8}
\]

Therefore

\[
 |\mathfrak E_S^{(2)}-\mathfrak E_{R_0}^{(2)}|
 \le(S-R_0)D_L\le R_0D_L\ll_\eta L^3X^\eta.
\tag{172.K9}
\]

This includes \(S=M<2R_0\), but is not an owner-complete sector because
its complement is not target-safe.

At \(S=2R\), (172.K7) is the exact triangular tent. With absolute-site
parity blocks

\[
 Y_{s,R}^{(\epsilon)}
 =\sum_{\substack{0\le j<R\\s+j\equiv\epsilon\pmod2}}z_{s+j},\qquad
 \mathfrak H_R^{(2)}
 =\frac1{2R}\sum_{s,\epsilon}
 |Y_{s,R}^{(\epsilon)}-Y_{s+R,R}^{(\epsilon)}|^2,
\]

pair counting and the parallelogram identity give

\[
 \mathfrak E_R^{(2)}
 =\frac1R\sum_{s,\epsilon}|Y_{s,R}^{(\epsilon)}|^2,\qquad
 \mathfrak E_{2R}^{(2)}
 =2\mathfrak E_R^{(2)}-\mathfrak H_R^{(2)}.
\tag{172.K10}
\]

This remains exact for odd \(R\). A final \(R<M<2R\) link must use
(172.K7)--(172.K8), not a rounded Haar formula; \(r=M\) is absent and all
endpoint-crossing blocks are already present through zero extension.

## 3. Exact real-cardinal character--Poisson transform

Put

\[
 Z_\epsilon(\theta)=\sum_N(-1)^{\epsilon N}z_Ne(N\theta).
\]

Changing variables in the second Fejer peak yields

\[
 \mathfrak E_R^{(2)}
 =\frac12\sum_{\epsilon=0}^1
 \int_0^1F_R(\theta)|Z_\epsilon(\theta)|^2\,d\theta.
\tag{172.K11}
\]

Choose real \(\varphi\in C_c^\infty((-1/2,1/2))\),
\(\varphi(0)=1\), and define

\[
 \mathcal W_\epsilon(x,y)=
 \sum_{\substack{d,m\ge1\\d\ {\rm odd}}}
 (-1)^{\epsilon m}\lambda_{dm}(d)
 \varphi(x-d)\varphi(y-m),
\]

\[
 \mathcal B_{\epsilon,\theta}(x,y)=
 \mathcal W_\epsilon(x,y)e(J\sqrt{xy}+\theta xy).
\tag{172.K12}
\]

The disjoint cardinal cells preserve every lattice value and literal
incidence. Since \(d\) is odd,
\((-1)^{\epsilon N}=(-1)^{\epsilon m}\). With

\[
 \widetilde{\mathcal B}(\xi,\nu)
 =\iint\mathcal B(x,y)e(-\xi x-\nu y)\,dx\,dy,
\]

the identity

\[
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i}
\]

and ordinary Poisson imply

\[
 \sum_n\chi_4(n)f(n)=\frac i2
 \sum_{\substack{k\in\mathbb Z\\k\ {\rm odd}}}
 \chi_4(k)\widehat f(k/4).
\tag{172.K13}
\]

Ordinary Poisson in \(y\) has no further constant, hence exactly

\[
 Z_\epsilon(\theta)=\frac i2
 \sum_{\substack{k\in\mathbb Z\\k\ {\rm odd}}}\chi_4(k)
 \sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).
\tag{172.K14}
\]

For \(B_{U,V}=F_V-F_U\) and
\(U_{\epsilon;k,\ell}
=\widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell)\), substitution before
every modulus gives

\[
 \begin{aligned}
 \Delta_{U,V}:={}&\mathfrak E_V^{(2)}-\mathfrak E_U^{(2)}\\
 ={}&\frac18\Re\sum_{\epsilon=0}^1
 \sum_{\substack{k,k'\in\mathbb Z\\k,k'\ {\rm odd}}}
 \sum_{\ell,\ell'\in\mathbb Z}\chi_4(k)\chi_4(k')
 \int_0^1B_{U,V}(\theta)
 U_{\epsilon;k,\ell}\overline{U_{\epsilon;k',\ell'}}\,d\theta.
 \end{aligned}
\tag{172.K15}
\]

The constant is \(1/8=(1/2)|i/2|^2\); one real part encloses the full
aggregate, and there is no character zero frequency.

## 4. Recombined ordinary zero and the first open seam

Define the ordinary-zero component only after all odd character
frequencies have been recombined:

\[
 Z_{\epsilon,0}(\theta)=\frac i2
 \sum_{k\ {\rm odd}}\chi_4(k)U_{\epsilon;k,0}(\theta)
 =\sum_d\chi_4(d)\int_{\mathbb R}
 \mathcal B_{\epsilon,\theta}(d,y)\,dy.
\tag{172.K16}
\]

On each supported cell,

\[
 \partial_y(J\sqrt{dy}+\theta dy)
 =\frac J2\sqrt{d/y}+\theta d\asymp J
 \qquad(0\le\theta\le1).
\]

One cellwise integration by parts has no boundary term and costs
\(O(J^{-1})\). The \(O_\eta(L^2X^\eta)\) incidences therefore give

\[
 \sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\eta L^2J^{-1}X^\eta.
\tag{172.K17}
\]

Writing \(Z_{\epsilon,*}=Z_\epsilon-Z_{\epsilon,0}\), all terms of
(172.K15) with \(\ell=0\) or \(\ell'=0\) recombine to the bandpass
integral of
\(|Z_{\epsilon,0}|^2
+2\Re(Z_{\epsilon,0}\overline{Z_{\epsilon,*}})\).
Since \(|B_{U,V}|\le U+V\ll L^2\),
\(\|Z_\epsilon\|_2=D_L^{1/2}\), and \(L^2\le J\), Cauchy and (172.K17)
give, after shrinking the input epsilon,

\[
 |\Delta_{U,V}^{(0)}|
 \ll_\eta(U+V)
 \left(D_L^{1/2}\frac{L^2}{J}+\frac{L^4}{J^2}\right)X^{O(\eta)}
 \ll_\varepsilon L^3X^\varepsilon.
\tag{172.K18}
\]

This proves no termwise-\(k\) estimate and creates no standalone zero-mode
owner. The exact complement is

\[
 \begin{aligned}
 \mathcal A_{\ne0}(U,V)=\frac18\Re\sum_{\epsilon=0}^1
 &\sum_{\substack{k,k'\in\mathbb Z\\k,k'\ {\rm odd}}}
 \sum_{\substack{\ell\ne0\\\ell'\ne0}}\chi_4(k)\chi_4(k')\\
 &\times\int_0^1B_{U,V}(\theta)
 U_{\epsilon;k,\ell}\overline{U_{\epsilon;k',\ell'}}\,d\theta.
 \end{aligned}
\tag{172.K19}
\]

For every later unclosed chain link, the first open affirmative estimate in
this transform route is the one-sided bound

\[
 \boxed{\mathcal A_{\ne0}(U,V)\ll_\varepsilon L^3X^\varepsilon,}
\tag{172.K20}
\]

with all modes, cells, openings, endpoints, transitions, and cross terms
inside the one real part. An absolute link theorem would be stronger, and
cancellation among links is not excluded.

## 5. Physical diagonal versus dual diagonal

Extend \(b_{U,V}\) evenly and put

\[
 \mathscr B_{U,V}(t)=\int_0^1B_{U,V}(\theta)e(t\theta)\,d\theta,
 \qquad I(u)=\int_0^1e(u\theta)\,d\theta.
\]

Then

\[
 \mathscr B_{U,V}(t)=\sum_{h\in\mathbb Z}b_{U,V}(h)I(t+h).
\tag{172.K21}
\]

For integer \(n\), this is \(b_{U,V}(-n)=b_{U,V}(n)\), so the physical
diagonal has coefficient \(b_{U,V}(0)=0\). For noninteger \(t\), however,

\[
 \mathscr B_{U,V}(t)=
 \frac{(e(t)-1)(V-U)}{2\pi i t}
 -\frac1{2\pi i t}\int_0^1B'_{U,V}(\theta)e(t\theta)\,d\theta,
\tag{172.K22}
\]

because \(B_{U,V}(0)=B_{U,V}(1)=V-U\). In (172.K15) the argument is
\(t=xy-x'y'\). Even when \((k,\ell)=(k',\ell')\), the two cardinal-cell
variables are independent, so \(t\) is generally nonintegral and nonzero.
The physical diagonal therefore cancels only after dual diagonal and
off-diagonal terms, frequency endpoints, physical endpoint cells, and
zero-extension transitions fully recombine. A one-site sequence, whose
every physical increment is zero, checks this conclusion.

## 6. Sharp in-range positive-control capacity

Fejer positivity and sliding-window Cauchy give

\[
 0\le\mathfrak E_R^{(2)}\le RD_L,\qquad
 |\Delta_{U,V}|\le(U+V)D_L.
\tag{172.K23}
\]

This top power is sharp for the coefficient-uniform interface. Let
\(M=4P\), take a positive even \(N_0\), and set
\(z_{N_0+2j}=1\) for \(0\le j<2P\), with all other sites in the containing
interval zero. Then \(D=2P\), \(A_{2s}=2P-s\), and the terminal doubling
link \(2P\to4P\) has the exact value

\[
 \begin{aligned}
 \Delta_{2P,4P}
 &=\frac1P\left\{\sum_{s=1}^{P-1}s(2P-s)
 +\sum_{s=P}^{2P-1}(2P-s)^2\right\}\\
 &=P^2=MD/8.
 \end{aligned}
\tag{172.K24}
\]

Choose \(L=2^m\), \(M=L^2\), \(P=L^2/4\), \(X=L^8\), \(J=L^4\), and
\(H=L^2\). The link belongs to the stopped chain, and for fixed
\(0<\varepsilon_0<1/8\),

\[
 P^2/(L^3X^{\varepsilon_0})
 \asymp L^{1-8\varepsilon_0}\longrightarrow\infty.
\tag{172.K25}
\]

Taking \(c_N=e(-J\sqrt N)\) on these positive occupied sites produces this
dechirped \(z\). It is not the literal residual coefficient and proves no
physical lower bound. It proves precisely that support, \(D_L\), Parseval,
Haar positivity, phase alone, or a coefficient-uniform positive
dual/cell/opening/frequency norm cannot supply the missing factor \(L\)
before an actual-symbol saving.

## 7. Both peak centres and collar self-return

In (172.K11), the original \(1/2\)-peak is transferred exactly to the
amplitude \((-1)^N=(-1)^m\); both transformed families are centred at the
same common frequency. The control above is coherent at both original
peaks because it occupies one absolute parity.

For common-frequency displacement \(\omega\), the smooth product phase is

\[
 \Phi_\omega(u,v)=J\sqrt{uv}+\omega uv-\xi u-\eta v,\qquad
 \det\operatorname {Hess}\Phi_\omega
 =-\omega^2-\frac{J\omega}{2\sqrt{uv}}.
\tag{172.K26}
\]

Thus both peak centres \(\omega=0\) are rank one. For a top doubling,
\(F_{2R}-F_R\asymp R\) on \(|\omega|\le c/R\) for a sufficiently small
fixed \(c\). Since \(uv\asymp L^2\) and \(R\asymp M\asymp L^2\), the
perturbation \(\omega uv\) is only \(O(1)\) there.

After a lawful smooth Möbius opening \(u=Qm\), \(v=Rn\), simultaneous
Poisson at either centre returns the accepted phase

\[
 J\sqrt{QRmn}-km/4-\ell n,
\]

whose stationary equations and radial broadening are

\[
 k\ell=XQR,\qquad Q\ell\le Rk\le4Q\ell,\qquad
 |k\ell-XQR|\ll QRJ/L.
\tag{172.K27}
\]

One smooth-interior coefficient has scale \(L^{3/2}/(QR\sqrt J)\), while
positive collar counting costs

\[
 \ll_\eta\left(QRJ/L+1\right)(XQR)^\eta.
\tag{172.K28}
\]

The second peak has the same collar after its exact \((-1)^m\) gauge.
Thus positive dual summation self-returns to the accepted product collar,
not to a new factor-\(L\) mechanism. This collar capacity and the maximal
energy capacity \(MD_L\) are distinct diagnostics; neither is physical
residual mass.

## 8. First unproved step, state boundary, and evidence

The first unproved step is exactly (172.K20). There is no open finite
parity--Fejer identity, cardinal transform identity, or collectively
recombined ordinary-zero estimate in this kernel. Taking positivity before
an actual-symbol saving returns (172.K24)--(172.K25).

This kernel folds the first-link and ordinary-zero auxiliary estimates into
one smallest obstruction node; neither is a standalone owner. It neither
proves nor disproves (165.K26). The complete residual \(t=1\) scalar, other
\(t=1\) channels, hard TOP, BAL, UNBAL, M9--M2, M9--M1, GAR, endpoint
assembly, M9, both bridges, and the quarter theorem remain unchanged. No
global exponent is improved.

Accepted dependency kernels:

1. proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
2. proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md.

Round-172 evidence, relative to the campaign directory:

1. reports/literal_maximal_fejer_dyadic_frequency_attack.md;
2. reports/blind_maximal_fejer_dyadic_rederivation.md;
3. reports/maximal_fejer_transform_endpoint_hostile_audit.md;
4. reviews/parity_dyadic_endpoint_seam_review.md;
5. reviews/literal_common_frequency_transform_review.md;
6. reviews/power_owner_state_effect_review.md;
7. barrier_packet.md and blind_statement.md.

No computation, numerical experiment, web source, or external theorem is
used.
