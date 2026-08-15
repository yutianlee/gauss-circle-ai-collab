## 1. Result

The proposed positive-line Cauchy-tail closure survives hostile audit, but only as an existence theorem and only after one correction in the artificial-pole cell.  Choose the legal fixed terminal line
\[
 \Re s=c'=\frac54,
 \qquad 0\leq a<a_0,\quad b>0,
 \qquad a+b<\frac12,\quad \frac a2+b<\frac14.                 \tag{38.1}
\]
For the actual choice \(b=1/\log(2X)\), these inequalities hold for all sufficiently large \(X\), uniformly as the physical top line \(a\downarrow0\).  On this line the complete terminal \(R_1\) density, after the signed hard-top Plemelj pairing and all actual \(h,q,m,j,x\) factors are retained, has the uniform majorant
\[
 |\mathcal F_T(\nu)|
 \ll_{X,W,b}(1+|\nu|)^{\kappa-4}\log(2+|\nu|),
 \qquad \kappa=\frac34+\frac{a+b}{2}<1.                       \tag{38.2}
\]
The bound is valid for both signs of the tangent height and is uniform in the truncation \(U\).

The artificial residue is also integrable, but it must not be estimated by the nonconvergent \(h,q\) expansion on its left real line.  Keeping its arithmetic factor recombined and using the exact two-factor functional equation gives an \(O_{X,W,b}((1+|\nu|)^{-3})\) tail.  The \(u=0\) delta part of that residue and every \(v=0\) or joint corner term have bounded \(\nu\)-support.

Consequently the Round-37 positive-\(b\) endpoint-free density has a signed Cauchy tail along the prescribed \(U=V=T\) and radial-side exhaustion.  This proves existence of that endpoint-free physical remainder.  It supplies neither the local terminal-symbol estimate nor an \(O(X^\varepsilon)\) normalized bound.  The local saddle \(q^{-2}\) lemma is not used and cannot be inferred globally.

## 2. Exact statement and hypotheses

Write
\[
 u=a+i\mu,\qquad v=b+i\nu,\qquad s=\frac54+it,
 \qquad \delta=a+b,
\]
and make the beta-slab change before taking absolute values:
\[
 t=\frac{\mu+\nu}{2}+\beta,qquad
 \alpha=\mu+\nu+\beta,qquad
 \eta=\frac\mu2+\nu+\beta.                                   \tag{38.3}
\]
The map \((\beta,\mu,\nu)\mapsto(t,\mu,\nu)\) is triangular with determinant \(1\), so \(dt\,d\mu\,d\nu=d\beta\,d\mu\,d\nu\), with no factor two.

For
\[
 A=s-\frac{u+v}{2},\qquad B=s+\frac{u+v}{2},
\]
one has exactly
\[
 A=\left(\frac54-\frac\delta2\right)+i\beta,qquad
 B=\left(\frac54+\frac\delta2\right)+i\alpha.                 \tag{38.4}
\]
Thus the zeta gamma quotient is bounded on the compact beta slab, while, for either sign of \(\alpha\),
\[
 |X_4(B)|\ll (1+|\alpha|)^\kappa,qquad
 \kappa=\Re B-\frac12=\frac34+\frac\delta2<1.                 \tag{38.5}
\]
The post-endpoint radial variable is
\[
 \rho=\frac14-s-\frac v2
      =-1-\frac b2-i\eta,                                      \tag{38.6}
\]
so the claimed real constant \(-1-b/2\) is correct.  The hypotheses also include the accepted compact beta mask and its derivatives, collision-separated contours, the actual profile estimate
\[
 f_b(\nu):=\widehat\phi(b+i\nu),qquad
 |f_b(\nu)|\ll_b(1+|\nu|)^{-3},                                \tag{38.7}
\]
the exact identity \(m=hq\), all scale profiles and floors, and the Round-37 common ownership of the terminal and artificial \(R_1\) cells.  The top limit is taken in its accepted order as
\[
 \frac1{2\pi}\frac1{0^++i\mu}
 =\frac12\delta_0(\mu)-\frac{i}{2\pi}\operatorname{PV}\frac1\mu. \tag{38.8}
\]

## 3. Proof or derivation

### Terminal tangent powers and actual sums

The exact coefficient phase on the beta slab is
\[
 \left(\frac hq\right)^{(u+v)/2}(hq)^{-s}
 =h^{-5/4+\delta/2}q^{-5/4-\delta/2}
   q^{-i(\mu+\nu)}(hq)^{-i\beta}.                               \tag{38.9}
\]
Hence
\[
 \sum_{h,q\ge1}h^{-5/4+\delta/2}q^{-5/4-\delta/2}(1+\log q)<\infty \tag{38.10}
\]
uniformly in a fixed strict subregion of (38.1).  The logarithm covers the one \(\mu\)-derivative needed by the PV difference quotient.  The factor \(\chi_4(q)\), odd stars, equality conventions, \(D_j^a(H_j+1)^b\), and the finite actual \(j\)-sum do not weaken (38.10).

For
\[
 I_1(\rho)=\int_1^{N_X}x^{\rho-1/2}e(\sqrt{Xx})\,dx,qquad
 R_{1,v}(1-s)=-\frac{\pi i\sqrt X}{\rho}I_1(\rho),
\]
(38.6) gives the uniform, nonoscillatory bounds
\[
 |I_1(\rho)|\leq\int_1^{N_X}x^{-3/2-b/2}\,dx\leq2,qquad
 |R_{1,v}(1-s)|\ll\frac{\sqrt X}{1+|\eta|}.                    \tag{38.11}
\]
The same bound, with at most a constant factor, holds after one \(\mu\)-derivative: differentiating \(I_1\) inserts \(\log x\), whose moment against \(x^{-3/2-b/2}\) is finite uniformly in \(N_X\).  Thus no unproved oscillatory integration by parts in \(x\) is needed.  In particular, the global proof has only one inverse \(\eta\) power; the second inverse power appearing in some local stationary discussions is neither assumed nor required.

After summing (38.10), integrating over compact \(\beta\), and suppressing harmless actual scale constants, the terminal numerator \(H\), excluding the hard-top distribution, obeys
\[
 |H(\mu,\nu)|
 \ll_{X,W,b}|f_b(\nu)|
 \frac{(1+|\mu+\nu|)^\kappa}{1+|\mu/2+\nu|},                  \tag{38.12}
\]
with bounded beta shifts understood.  Its \(\mu\)-derivative satisfies the same estimate times \(\log(2+|\mu|+|\nu|)\).  This covers positive and negative \(\alpha\), the bounded-\(\alpha\) plane, and the tangent \(\eta=0\) plane simultaneously.

For \(0\leq\kappa<1\), an elementary split at
\(0,-\nu,-2\nu\), followed by dyadic summation, gives
\[
 \int_{|\mu|>1}
 \frac{(1+|\mu+\nu|)^\kappa}
 {|\mu|(1+|\mu/2+\nu|)}\,d\mu
 \ll_\kappa (1+|\nu|)^{\kappa-1}\log(2+|\nu|).                \tag{38.13}
\]
The far range is exactly where \(\kappa<1\) is essential: its integrand is \(O(|\mu|^{\kappa-2})\).  Near \(\mu=0\), the signed PV must be used before absolute values:
\[
 \operatorname{PV}\!\int_{-U}^{U}\frac{H(\mu,\nu)}\mu\,d\mu
 =\int_{|\mu|\le1}\frac{H(\mu,\nu)-H(0,\nu)}\mu\,d\mu
  +\int_{1<|\mu|\le U}\frac{H(\mu,\nu)}\mu\,d\mu.             \tag{38.14}
\]
The derivative bound controls the first integral and (38.13) the second, uniformly in \(U\ge1\).  The delta term \(H(0,\nu)/2\) is smaller than the same right side.  Combining (38.7), (38.13), and (38.14) proves (38.2).  Notice that the \(\eta=0\) seam at \(\mu=-2\nu+O(1)\) is the logarithmic worst case and is already included in (38.13); both height signs give the same power.

### Artificial residue and axes

At the artificial pole \(\rho=0\),
\[
 s=\frac14-\frac v2,qquad
 \beta=-\frac\mu2-\nu,qquad \alpha=\frac\mu2.                 \tag{38.15}
\]
The compact beta mask therefore imposes \(\mu=-2(\nu+\beta)\), and the residue substitution has Jacobian \(|d\mu|=2|d\beta|\).  This is the only factor two; it is not present in the terminal Jacobian.

One must not sum (38.9) termwise after (38.15), because the residue line is outside its absolute Dirichlet chamber.  Instead retain the actual recombined arithmetic factor and use
\[
 K_{u+v}(1-s)F_{-(u+v)}(s)=\zeta(1-A)L(1-B,\chi_4),             \tag{38.16}
\]
where on (38.15)
\[
 A=\left(\frac14-\frac a2-b\right)+i\beta,qquad
 B=\left(\frac14+\frac a2\right)+i\alpha.                     \tag{38.17}
\]
Condition (38.1) keeps \(A=0\) away.  Since the partial sums of \(\chi_4\) are bounded, Abel summation gives, for every fixed \(\sigma>0\),
\[
 |L(\sigma+i\tau,\chi_4)|\ll_\sigma 1+|\tau|.                \tag{38.18}
\]
Thus \(\zeta(1-A)\) is bounded on the compact beta slab and
\(L(1-B,\chi_4)=O(1+|\nu|)\).  The residue of \(R_1\) is a constant multiple of \(\sqrt X I_1(0)\), independent of height.  The PV top factor is \(O(|\nu|^{-1})\), while (38.7) is \(O_b(|\nu|^{-3})\); hence the artificial-residue density is \(O_{X,W,b}(|\nu|^{-3})\).  Its top delta forces \(\mu=0\), and then (38.15) forces bounded \(\nu\).  Likewise \(v=0\) and the joint corner occur at bounded height.  Connector-axis and collision conventions change finite coefficients, not these tail powers.

### Joint exhaustion

The majorants just proved are in \(L^1(d\nu)\) and uniform in the symmetric \(\mu\)-cutoff.  They therefore control the moving \(u\)- and \(v\)-faces and imply the Cauchy property along \(U=V=T\).  The prescribed
\[
 S=(2+X+2T+2B_0)^2
\]
satisfies \(S>(U+V)/2+2B_0\), so the complete radial-side vector is identically zero by the accepted compact-support lemma.  The actual positive \(b=1/\log(2X)\) remains fixed during height exhaustion; its permitted polynomial \(b^{-1}\) loss is only polylogarithmic in \(X\).  Finally, multiplication by
\(-4X^{1/4}\Re\{e(1/8)\,\cdot\}/\pi\) preserves convergence.

## 4. First doubtful or unproved step

There is no remaining height-tail gap for the frozen Round-38 positive-line object once the Round-37 finite identity and the contour inequalities (38.1) are imposed.  The first unproved step lies strictly downstream: the constants in (38.2), (38.11), the finite scale sum, and the artificial-residue bound have not been reduced to \(O(X^\varepsilon)\).  In particular, this audit proves existence and uniqueness of the physical endpoint-free remainder, not the terminal-symbol estimate or the M1 target bound.

Two overextensions remain invalid.  First, (38.2) is not a statement uniform at \(b=0\); the \(v=0\) residue must remain extracted and the actual positive line retained.  Second, no global \(q^{-2}\) estimate follows.  The present proof uses absolute right-chamber powers in (38.10), while the artificial residue uses the analytically recombined expression (38.16).  Applying the local stationary \(q^{-2}\) normalization to either global tangent tails or the residue would be an ownership error.

## 5. Required control tests and outcomes

1. **Beta slab and Jacobian:** pass.  The terminal determinant is \(1\); the separate artificial-residue substitution contributes a factor \(2\).
2. **Two height signs and transition planes:** pass.  Stirling gives the same exponent \(\kappa\) for \(\alpha\to\pm\infty\); bounded \(\alpha\) is better, and \(\eta=0\) is the logarithmic seam already counted in (38.13).
3. **Radial integral:** pass with a correction.  The robust global estimate is \(R_1\ll\sqrt X/(1+|\eta|)\), obtained directly from the integrable \(x^{-3/2-b/2}\) weight.  No second inverse height is claimed.
4. **Hard top:** pass only in the signed order (38.14).  Absolute integration of \(1/|\mu|\) before subtracting \(H(0,\nu)\) diverges and would invalidate the proof.  Delta, PV, and the explicit crossed top residue must not be counted twice.
5. **Actual arithmetic and profiles:** pass on the terminal line by (38.9)--(38.10).  At \(\rho=0\), termwise \(h,q\) summation fails; the corrected analytic treatment (38.16)--(38.18) passes.  Floors, stars, characters, and finite scales remain attached.
6. **Axes, collisions, and corner:** pass under the accepted one-collision/one-corner convention and the strict separation in (38.1).  Every axial delta survivor has bounded \(\nu\)-support.
7. **Joint exhaustion:** pass.  The terminal and artificial tails have uniform \(L^1_\nu\) majorants, while the chosen \(S\) deletes radial sides exactly.  The proof follows the accepted top-before-height order and does not assert an arbitrary interchange with \(b\downarrow0\).
8. **Normalization and scope:** pass for convergence.  The external normalization cannot improve the \(X\)-size, and no target estimate is certified.

## 6. Dependencies and exact artifacts used

Used only `protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`, `rounds/codex-managed/m9-m1-beta-endpoint-free-axial-limit/reports/endpoint_free_limit_hostile_audit.md`, `rounds/codex-managed/m9-m1-beta-endpoint-free-axial-limit/synthesis.md`, `rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/reports/pushforward_bv_hostile_audit.md`, `rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/reports/regular_symbol_hostile_audit.md`, and `rounds/codex-managed/m9-m1-partial-functional-equation-transitions/reports/partial_FE_hostile_audit.md`.  No Round-38 claimant report, numerical experiment, web source, or unlisted project artifact was used.

## 7. Recommended state effect

**Promote, with the exact scope above, the actual positive-\(b\) endpoint-free signed Cauchy-tail theorem and hence the existence of the Round-37 endpoint-free axial remainder limit.**  Record the terminal majorant (38.2), the direct \(R_1\) bound (38.11), the signed top estimate (38.13)--(38.14), and the separately recombined artificial-residue estimate (38.16)--(38.18).

Retain the terminal-symbol and target-size obligations open.  Explicitly reject three shortcuts: absolute pre-Plemelj control, transferring local stationary \(q^{-2}\) to the global tail, and termwise use of the \(h,q\) expansion on the artificial-residue line.  The next round may start from a well-defined physical endpoint-free vector, but must obtain quantitative \(X\)-uniform symbol or arithmetic cancellation estimates rather than revisit outside-height existence.
