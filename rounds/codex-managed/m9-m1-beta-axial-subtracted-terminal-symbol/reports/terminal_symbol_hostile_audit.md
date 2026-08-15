## 1. Result

**No-go for the frozen statement as written; narrow cellwise reformulation only.** The limiting endpoint-free terminal vector is an aggregate over \(j,h,q\), radial \(x\), beta, and both signs, whereas
\[
 \lambda_{j,q,x}=\frac{\pi q\sqrt{Xx}}{D_j}                    \tag{39H.1}
\]
varies inside that aggregate. Therefore a pointwise bound for the aggregate by one \(\lambda^{-2}w(\nu)\) is not well typed. Conversely, if all actual coefficients and the external \(X^{1/4}\) normalization are included inside a raw cell symbol, its value is not a bare \(X^\varepsilon\lambda^{-2}\): the exact stationary numerator and scale monomial remain.

There is a lawful quantitative interface. Freeze \((j,h,q,x,\beta,\pm)\), remove the complete stationary phase, keep the stationary numerator and physical prefactors outside, and seek a mixed physical-height norm for the pre-numerator amplitude. The separated singular-top \(R_1\) cell already satisfies that interface. Smooth spatial Mellin profiles satisfy it with a translated-ridge loss of one harmonic logarithm. The complete phase-removed second translation divided difference on saddle entry/exit, beta connectors, and moving traces is still unproved.

Two exact corrections are required before even this reformulation can be promoted. First, the singular Plemelj regularizer applies only to the \(u^{-1}\) share of the hard top, not to smooth top remainders or interior \(W_j\). Second, after the top distribution consumes the \(u\)-measure, two contour factors remain; a beta-slab formula displaying only \(-i/(2\pi)\) is short by \((2\pi)^{-2}\). These are definition errors, although fixed constants do not change exponent capacity.

## 2. Exact statement and hypotheses

On \(c'=5/4\), put
\[
 u=a+i(L-\nu),\quad v=b+i\nu,\quad
 s=\frac54+i\left(\frac L2+\beta\right),\quad \alpha=L+\beta,
\]
\[
 A(L)=-1-\frac b2-i(L+\beta),\qquad
 D(L,\nu)=A(L)+\frac i2(L-\nu)=\rho.              \tag{39H.2}
\]
At fixed physical \(\nu\),
\[
 \partial_L\mu=1,\quad \partial_Lt=\frac12,\quad
 \partial_L\alpha=1,\quad \partial_L\rho=-\frac i2.          \tag{39H.3}
\]
Here \(A(L)\) is auxiliary regularizer notation, not the functional-equation variable \(s-(u+v)/2\).

For the singular \(u^{-1}\) cell only, if \(H\) excludes the top and radial denominators, define
\[
 {\cal R}_A[H]= -\frac{iH(L,L)}{2A(L)D(L,\nu)}
 +\frac{H(L,\nu)-H(L,L)}{(L-\nu)D(L,\nu)}.                    \tag{39H.4}
\]
The top delta and constant-numerator PV/log term have already been removed once. Smooth shares instead retain the ordinary factor
\[
 \frac{f_b(\nu)\widehat W_j(a+i(L-\nu))}{D(L,\nu)}.            \tag{39H.5}
\]

The original vertical measure is
\[
 \frac{ds\,du\,dv}{(2\pi i)^3}=\frac{dt\,d\mu\,d\nu}{(2\pi)^3}. \tag{39H.6}
\]
Since \((2\pi)^{-1}(0^++i\mu)^{-1}=\frac12\delta_0(\mu)-\frac{i}{2\pi}\operatorname{PV}(1/\mu)\), the singular ordinary PV density has coefficient \(-i/(2\pi)^3\), before the radial coefficient \(-\pi i\sqrt X\). The remaining beta and \(\nu\) measures contribute \((2\pi)^{-2}\).

The admissible replacement target is cellwise and phase removed:
\[
 {\mathfrak M}_\lambda(K):=\sup_{L\in I_\lambda}\int|K(L,\nu)|d\nu
 +\int_{I_\lambda}\!\int|\partial_LK(L,\nu)|d\nu dL
 +\sum_\gamma\int_{I_\lambda}|K(L,\gamma(L))|dL
 \ll X^\varepsilon\lambda^{-2},                               \tag{39H.7}
\]
where \(|I_\lambda|\ll\lambda\) and \(\gamma\) runs over moving regular faces. The external normalization, character, stationary numerator, real coefficient monomial, radial integration, and Fresnel operator remain outside \(K\).

## 3. Proof or derivation

Writing \(H_0=H(L,L)\), \(\dot H_0=(\partial_L+\partial_\nu)H(L,L)\), direct fixed-\(\nu\) differentiation of (39H.4) gives
\[
\begin{aligned}
 \partial_L{\cal R}_A[H]={}&-\frac{i\dot H_0}{2AD}
 +\frac{H_0}{2A^2D}+\frac{H_0}{4AD^2}\\
 &+\frac{\partial_LH(L,\nu)-\dot H_0}{(L-\nu)D}
 -\frac{H(L,\nu)-H_0}{(L-\nu)^2D}
 +\frac{i\{H(L,\nu)-H_0\}}{2(L-\nu)D^2}.          \tag{39H.8}
\end{aligned}
\]
The first unsupported complete coefficient is
\[
 {\mathfrak E}_H=\frac{\partial_LH(L,\nu)-(\partial_L+\partial_\nu)H(L,L)}{L-\nu}
 -\frac{H(L,\nu)-H(L,L)}{(L-\nu)^2}.                         \tag{39H.9}
\]
For \(H=f_b(\nu)\), this is the accepted separated calculus. No accepted estimate controls (39H.9) for the full phase-removed gamma/radial/connector amplitude through entry/exit and moving faces.

Let \(\delta=a+b\), \(r=5/4-\delta/2\), \(p=5/4+\delta/2\), and \(\kappa=p-1/2\). Before stationary phase, one raw terminal \(x\)-cell has modulus
\[
 h^{-r}q^{-p}\left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 \sqrt X\,x^{-3/2-b/2}\lambda^\kappa
 \times|\text{top/radial kernel}|.                            \tag{39H.10}
\]
Including the external factor, a raw-cell comparison with \(X^\varepsilon\lambda^{-2}\) loses
\[
 X^{3/4-a/2}D_j^a(H_j+1)^b h^{-r}q^{-p}
 x^{-3/2-b/2}\lambda^\kappa.                                 \tag{39H.11}
\]
This is a normalization mismatch, not a counterexample to the pre-numerator symbol lemma.

Stationary phase supplies \(\lambda^{1/2}\), and \(q^{-p}\lambda^{\kappa+1/2}=\theta_j(x)^p\), where \(\theta_j(x)=\pi\sqrt{Xx}/D_j\). Exact rearrangement leaves the post-endpoint stationary numerator
\[
 \frac{D_j}{q}\lambda.                                        \tag{39H.12}
\]
Thus a pre-numerator \(\lambda^{-2}\) bound becomes \(D_j/(q\lambda)\), the accepted local \(q^{-2}\) scale. Neither (39H.12) nor the external normalization belongs inside the object satisfying (39H.7).

The stationary phase derivative is
\[
 \Psi_\pm'(L)=\log\frac{|L+\beta|}{\lambda}.                  \tag{39H.13}
\]
On a fixed-ratio entry/exit collar this is \(O(1)\), not \(O(\lambda^{-1})\). Retaining \(e^{i\Psi_\pm}\) inside the differentiated symbol therefore gives \(\lambda^{-2}\), not \(\lambda^{-3}\). Phase removal is mandatory. Moreover incomplete stationary phase is an operator equal to a leading Fresnel term plus a remainder; it is not an exact scalar factorization “Fresnel coefficient times \(K(L,\nu)\)” for a varying amplitude.

For the separated kernel, the translated \(f_b(L)/(AD)\) term causes no obstruction: on compact \(\nu\), it is \(O_b(\lambda^{-5})\); near \(\nu\asymp L\), the cubic height tail supplies the matching weight. For a smooth nonconstant spatial Mellin profile, choose \(\mu_0\) where \(\partial_\mu\widehat W_j(a+i\mu_0)\ne0\) and set \(\nu=L-\mu_0\). On \(|L|\asymp\lambda\),
\[
 \left|\partial_L\frac{f_b(\nu)\widehat W_j(a+i(L-\nu))}{D(L,\nu)}\right|
 \asymp_b\lambda^{-4}.                                       \tag{39H.14}
\]
An \(X\)-independent pointwise weight would require \(w(L)\gg1/|L|\), impossible in \(L^1\). This does not falsify the frozen polylogarithmic formulation: the actual range \(\lambda\ll X\) permits
\[
 w_{X,b}(\nu)\asymp_b\frac{\mathbf1_{1\le|\nu|\le CX}}{1+|\nu|}
 +(1+|\nu|)^{-2},\qquad \|w_{X,b}\|_1\ll_b\log X.            \tag{39H.15}
\]

Conditionally on (39H.7), the leading scale coefficient is
\[
 h^{-r}q^{-2}D_j^{2-r}X^{r/2-1/2+b/4}
 x^{-r/2-b/2-5/4},                                            \tag{39H.16}
\]
and radial integration gives \(\min(1,\{\sqrt X|2\mp q/D_j|\}^{-1})\). The \(q\)-sum is \(O(X^{-1/2}\log X)\). At exact resonance \(q=2D_j\), \(q\) is even and \(\chi_4(q)=0\), so the resonant term vanishes. Summing \(h\) and dyadic \(j\) gives a polylogarithm before external \(X^{1/4}\), conditional on (39H.7).

## 4. First doubtful or unproved step

The first failure is definitional: there is no exact aggregate \(K_{\rm term}^{\circ}(L,\nu)\) satisfying a bound with one cell-dependent \(\lambda\), and applying \({\cal R}_A\) to all \(j\) shares incorrectly subjects smooth profiles to a second Plemelj operation. Any exact aggregate definition must split the singular \(u^{-1}\) share from ordinary smooth shares and restore the missing \((2\pi)^{-2}\).

After this repair, the first analytic gap is (39H.7) for the complete phase-removed hard-top cell, equivalently (39H.9) with translated face traces, uniformly through both saddles, entry/exit, beta connectors, and common artificial ownership. The terminal line has \(\Re\rho=-1-b/2\), so no terminal \(\rho=0\) pole occurs; the crossed artificial residue is separately extracted. Entry/exit is the sharp obstruction to a raw oscillatory derivative claim by (39H.13). Round 38 proves only a fixed-\(X\) Cauchy limit and cannot supply this derivative.

## 5. Required control tests and outcomes

1. **One-count definition:** fail as an all-\(j\) Plemelj aggregate; pass after separating the singular top share and excluding already routed boundary/axial/artificial modules.
2. **Contour constants:** fail for a display with only \(-i/(2\pi)\); the exact PV density retains \(-i/(2\pi)^3\) before the radial coefficient.
3. **Fixed-\(\nu\) derivative:** pass for (39H.8); fixed-\(\mu\) differentiation would miss (39H.9).
4. **Type and normalization:** aggregate \(\lambda\)-bound fails typing. Raw cell has (39H.11); the pre-numerator phase-removed cell has the lawful target.
5. **Two saddles and entry/exit:** gamma powers agree for both signs. A raw-phase derivative fails by (39H.13); incomplete Fresnel is not an exact scalar multiplier.
6. **Rho, axial, collisions:** terminal \(D=\rho\) is separated in real part. Common artificial and \(v=0\) vectors, their connectors, collision, and corner are extracted once.
7. **Profiles and weights:** separated \(R_1\) passes. Smooth translated ridges rule out an \(X\)-independent \(w\), but (39H.15) has permitted polylogarithmic norm; the mixed norm is preferable.
8. **Scales, floors, stars, character:** (39H.16) retains the scale powers. The conditional sum is safe; exact \(q=2D_j\) vanishes by \(\chi_4\).
9. **External normalization:** it belongs after the cell estimate and yields \(X^{1/4}\) times the conditional internal polylogarithm. It cannot be hidden in a bare symbol bound.

## 6. Dependencies and exact artifacts used

Used only `protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`, `rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/reports/pushforward_bv_hostile_audit.md`, `rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/reports/regular_symbol_hostile_audit.md`, `rounds/codex-managed/m9-m1-beta-complete-physical-height-symbol/reports/complete_kernel_hostile_audit.md`, `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/reports/cauchy_tail_hostile_audit.md`, and `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/synthesis.md`. The requested hostile checks of Round-39 formulas were performed only after the independent audit. No numerical experiment, web source, or unlisted project artifact was used.

## 7. Recommended state effect

**Revise, do not promote, the frozen terminal-symbol statement.** Replace the aggregate pointwise claim by the phase-removed cellwise mixed-norm obligation (39H.7), with singular hard-top and smooth spatial shares explicitly separated and exact contour constants restored.

Retain as narrow controls: the regularizer and derivative (39H.4), (39H.8); the normalization ledger (39H.10)--(39H.12); the translated harmonic ridge weight (39H.15); and the conditional scale sum (39H.16), corrected by \(\chi_4(2D_j)=0\). Keep the quantitative obligation open at (39H.9) and its moving traces. Do not infer it from Round-38 existence, the separated \(R_1\) lemma, or downstream finite-section BV.
