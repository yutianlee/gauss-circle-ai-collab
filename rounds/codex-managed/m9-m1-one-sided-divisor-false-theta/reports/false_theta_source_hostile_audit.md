## 1. Result

There is an exact, convention-sensitive Appell--Lerch classification, but the audited literature does not imply the required square-root radial estimate.

Put
\[
 \rho=e^{\pi i\tau},\qquad q=e^{2\pi i\tau}=\rho^2,
 \qquad \mathscr F(\rho)=\sum_{h\geq1}
 \frac{\rho^{4h^2+h}}{1+\rho^{2h}}.
\]
For Zwegers' level-four convention
\[
 A_4(u,v;\tau)=e^{4\pi iu}\sum_{m\in\mathbb Z}
 \frac{q^{2m(m+1)}e^{2\pi imv}}{1-e^{2\pi iu}q^m},
\]
one has the exact identity
\[
 \boxed{A_4\!\left(\frac12,-\frac{3\tau}{2};\tau\right)
       =\frac12+2\mathscr F(\rho).}
\tag{1.1}
\]
In the Semikhatov--Taormina--Tipunin convention this is
\[
 \boxed{K_4\!\left(\tau,\frac{\tau}{8},
                 \frac12-\frac{\tau}{8}\right)
       =\frac12+2\mathscr F(\rho),}
\tag{1.2}
\]
not (K_4(\tau,0,1/2)), and not the specialization
((\nu,\mu)=(-3\tau/8,1/2-9\tau/8)).  The latter convention errors change the numerator and are fatal.

The function is consequently a meromorphic level-four Appell--Lerch function (equivalently, an indefinite-theta object with a Lambert denominator), not a standard unary false theta and not a positive-definite rank-two false theta.  Its completed form has four explicit theta-times-(R) correction terms.  The moving elliptic section is stable modulo elliptic shifts under (\Gamma(2)), as verified below, but only the completed function transforms.  No primary theorem audited here controls those corrections uniformly through the continuum of additive frequencies required by (e(\sqrt{Xn})).  A direct Fourier reduction to additive twists also loses ((XN)^{1/4}).  Thus (1.1)--(1.2) are importable structural identities, while the Round-63 signed target and every exponent consequence remain open.

## 2. Exact statement and hypotheses

Let (\tau\in\mathbb H).  The bilateral series defining (A_4(1/2,-3\tau/2;\tau)) converges normally on compact subsets of (\mathbb H), and it has no pole there: its denominator is (1+q^m), which cannot vanish for (m\ne0) because (|q|\ne1), and is (2) for (m=0).  Under precisely this hypothesis, (1.1) and (1.2) hold.

The completion theorem used in the audit is the specialization of Zwegers' multivariable Appell completion (in the notation reproduced in Bringmann--van Ittersum--Kaszian):
\[
 \widehat A_\ell(u,v;\tau)=A_\ell(u,v;\tau)
 +\frac{i}{2}\sum_{k=0}^{\ell-1}e^{2\pi iku}
 \vartheta\!\left(v+k\tau+\frac{\ell-1}{2};\ell\tau\right)
 R\!\left(\ell u-v-k\tau-\frac{\ell-1}{2};\ell\tau\right).
\tag{2.1}
\]
Here (R) contains the sign-minus-error-function kernel; it is nonholomorphic in (\tau).  The theorem gives the exact elliptic law, for integers (m_1,m_2,r_1,r_2),
\[
\begin{aligned}
 &\widehat A_\ell(u+m_1\tau+r_1,v+m_2\tau+r_2;\tau)\\
 &\quad=(-1)^{\ell(m_1+r_1)}
 e^{2\pi iu(\ell m_1-m_2)}e^{-2\pi ivm_1}
 q^{\ell m_1^2/2-m_1m_2}\widehat A_\ell(u,v;\tau),
\end{aligned}
\tag{2.2}
\]
and the modular law
\[
 \widehat A_\ell\!\left(\frac{u}{c\tau+d},\frac{v}{c\tau+d};
 \frac{a\tau+b}{c\tau+d}\right)
 =(c\tau+d)e^{\frac{\pi ic}{c\tau+d}(-\ell u^2+2uv)}
 \widehat A_\ell(u,v;\tau).
\tag{2.3}
\]
At the present section, (2.1) is the explicit four-term correction
\[
 C(\tau)=\frac{i}{2}\sum_{k=0}^{3}(-1)^k
 \vartheta\!\left(\left(k-\frac32\right)\tau+\frac32;4\tau\right)
 R\!\left(\frac12+\left(\frac32-k\right)\tau;4\tau\right),
\tag{2.4}
\]
so that (\widehat A_4=A_4+C).  No term in (2.4) may be omitted without an additional identity proving cancellation.

Semikhatov--Taormina--Tipunin define
\[
 K_\ell(\tau,\nu,\mu)=\sum_{m\in\mathbb Z}
 \frac{e^{\pi i\ell m^2\tau+2\pi i\ell m\nu}}
 {1-e^{2\pi i(\nu+\mu+m\tau)}},
 \quad \nu+\mu\notin\mathbb Z\tau+\mathbb Z.
\tag{2.5}
\]
Their Theorem 1.1 transforms (2.5) under (S) into another (K_\ell) plus a sum of (\ell) theta functions multiplied by explicit Mordell-type functions (\Phi).  At level four there are four such correction terms.  Their double-cone expansion has the additional hypothesis 
(|q|<|e^{2\pi i(\nu+\mu)}|<1).  It is unavailable here because (e^{2\pi i(\nu+\mu)}=-1) has modulus one; the bilateral meromorphic definition and its transform remain the valid interface.

## 3. Proof or derivation

At (u=1/2) and (v=-3\tau/2), the (m)-th summand in (A_4) is
\[
 \frac{q^{2m(m+1)}q^{-3m/2}}{1+q^m}
 =\frac{q^{2m^2+m/2}}{1+q^m}
 =\frac{\rho^{4m^2+m}}{1+\rho^{2m}}.
\tag{3.1}
\]
For (h\ge1), the (m=-h) summand satisfies
\[
 \frac{q^{2h^2-h/2}}{1+q^{-h}}
 =\frac{q^{2h^2+h/2}}{1+q^h},
\tag{3.2}
\]
and is therefore identical to the (m=h) summand.  The (m=0) summand is (1/2).  Pairing (m=\pm h) proves (1.1).

For (1.2), set (\nu=\tau/8), (\mu=1/2-\tau/8) in (2.5).  Then
\[
 e^{8\pi im\nu}=q^{m/2},\qquad
 e^{2\pi i(\nu+\mu)}=-1,
\]
so its summand is again (3.1).  By contrast,
(K_4(\tau,0,1/2)) has numerator (q^{2m^2}); its (m=\pm h) terms collapse to (q^{2h^2}), an ordinary theta contribution, and do not give (\mathscr F).

Expanding the unilateral Lambert denominator gives
\[
 \mathscr F(\rho)=\sum_{h\ge1}\sum_{j\ge0}
 (-1)^j\rho^{4h^2+h+2hj}.
\tag{3.3}
\]
The homogeneous quadratic part in ((h,j)) is (4h^2+2hj), whose symmetric matrix has negative determinant.  This explains why the kernel is an Appell/signature-((1,1)) object and not a positive-definite rank-two false theta.

The dependence (v=-3\tau/2) does not invalidate the Jacobi theorem, but it prevents one from substituting a scalar modular law without tracking the moving section.  This tracking can be done exactly for (\Gamma(2)).  If
(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\Gamma(2)) and (\tau'=\gamma\tau), the preimages in (2.3) of the desired elliptic variables (1/2,-3\tau'/2) are
\[
 U=\frac{c\tau+d}{2}
   =\frac12+\frac c2\tau+\frac{d-1}{2},
\]
and
\[
 V=-\frac32(a\tau+b)
   =-\frac{3\tau}{2}-\frac{3(a-1)}2\tau-\frac{3b}{2}.
\]
All four displayed shift coefficients are integers because (a,d) are odd and (b,c) are even.  Equations (2.2)--(2.3) therefore prove that the completed moving section is stabilized modulo elliptic shifts by (\Gamma(2)); the full modular group permutes a finite orbit of half-characteristics.  This does not prove that the holomorphic part (\mathscr F) is modular, and the automorphy factor has not been simplified into a scalar law because (2.4) must travel with it.

Finally, modular/additive information does not directly reach the square-root phase.  Let (V) be supported in a fixed compact subset of ((0,\infty)), put
\[
 \lambda=\sqrt{XN},\qquad
 g_\lambda(t)=V(t)t^{-3/4}e(\lambda\sqrt t),
\]
and let (I_N) be the corresponding finite (n\)-block.  Fourier inversion gives exactly
\[
 \mathcal L_{X,V}(N)=N^{-3/4}\int_{\mathbb R}
 \widehat g_\lambda(\xi)
 \sum_{n\in I_N}D(n)e(\xi n/N)\,d\xi.
\tag{3.4}
\]
The stationary frequencies satisfy (|\xi|\asymp\lambda), hence the additive parameters are
(|\xi|/N\asymp\sqrt{X/N}) modulo one.  Moreover, the standard one-dimensional Sobolev estimate
\[
 \|\widehat g_\lambda\|_1
 \ll \|g_\lambda\|_2^{1/2}\|g_\lambda'\|_2^{1/2}
 \ll_V (1+\lambda)^{1/2}
 \asymp (XN)^{1/4}
\tag{3.5}
\]
shows that taking a supremum additive-twist bound in (3.4) incurs a polynomial loss.  None of the audited cusp theorems provides the correlated, uniform estimate needed to recover that loss.

## 4. First doubtful or unproved step

The first unproved step in any proposed proof of the Round-63 target is the passage from the completed Appell transformation to a uniform estimate for (3.4).  The exact completion creates the four terms (2.4), and near rational cusps these are Mordell/Eichler error integrals rather than negligible remainders.  Existing theorems do not bound their convolution with (\widehat g_\lambda) uniformly over the frequency window (|\xi|\asymp\sqrt{XN}).

The source hypotheses exclude the tempting shortcuts:

* Bringmann--Nazaroglu's general false-theta completion assumes a positive-definite integral lattice and a sign of one linear functional.  Its rational-cusp theorem is for unary false theta functions.  Equation (3.3) is indefinite and meromorphic.
* Bringmann--Kaszian--Milas--Nazaroglu's rank-two theorem assumes (ac-b^2>0) and two sign factors.  It retains both an iterated Eichler integral and explicit modular-theta/arctangent boundary corrections.  The determinant in (3.3) is negative.
* Bringmann--Folsom--Milas treat (\sum_{n\ge0}\zeta^{\ell n+d}q^{(\ell n+d)^2}) as (\tau=it\to0^+), with Stokes regimes in the elliptic variable.  This is neither the Appell kernel nor a uniform rational-cusp theorem.
* Bringmann--Nazaroglu's (O(\log k)) Mordell bound assumes a fixed rational cusp and (\Re V\ge1); it does not supply the non-tangential continuum estimate in (3.4).

Thus the exact Appell identification is a genuine reduction, but claiming the signed target from “mock/false modularity” would begin with an unsupported uniformity assertion.

## 5. Required control test and outcome

The rational-cusp control fails in the strong sense needed for a naive uniform bound.  At
\(\tau=1/2+it\), one has (q\to-1) and (\rho\to i).  For every odd (h),
\(1+\rho^{2h}=1+q^h\to0).  Although the specialization is pole-free for every (t>0), it approaches the Appell polar divisor at this cusp.  Therefore denominator separation is not uniform, and the correction terms in (2.4) are compulsory.  This observation alone is not a lower bound, because numerator phases may cancel.

The perfect-fourth control also finds exact coherence.  Let (X=R^4) with (R\in\mathbb N).  For every odd (h\equiv1\pmod4) and odd (r\ge3), take the divisor variable
\[
 q_d=hr^2>4h,qquad n=hq_d=(hr)^2.
\]
Then
\[
 \chi_4(q_d)=\chi_4(h)=1,
 \qquad e(\sqrt{Xn})=e(R^2hr)=1.
\tag{5.1}
\]
Hence an infinite positive incidence subcone is exactly phase coherent.  Other divisor incidences contributing to the same (D(n)) may cancel it, so (5.1) is not a disproof of the desired estimate.  It does prove that a generic phase-gap or irrationality argument is invalid and that any successful estimate must use the character, cone boundary, and Appell correction together.  No numerical evidence was used as proof; the only bounded numerical diagnostic performed confirmed that the four-term correction is not identically zero at a sample interior point.

## 6. Dependencies and exact artifacts used

Repository inputs were `protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`, `rounds/codex-managed/m9-m1-one-sided-divisor-false-theta/derivation_packet.md`, `rounds/codex-managed/m9-m1-lower-radial-small-angle-collapse/synthesis.md`, and the assigned brief `rounds/codex-managed/m9-m1-one-sided-divisor-false-theta/briefs/false_theta_source_hostile_audit.md`.  No other Round-63 report was used.

Primary sources audited were:

* Semikhatov--Taormina--Tipunin, [*Higher-Level Appell Functions, Modular Transformations, and Characters*](https://arxiv.org/abs/math/0311314), especially definition (1.1), Theorem 1.1, and the domain of the double-series formula (2.2).
* Zwegers, [*Mock Theta Functions*](https://arxiv.org/abs/0807.4834), for the (R)-completion mechanism, and Zwegers, [*Multivariable Appell functions and nonholomorphic Jacobi forms*](https://doi.org/10.1007/s40687-019-0178-0), for the multivariable completion cited by the next source.
* Bringmann--van Ittersum--Kaszian, [*Quasi-Jacobi forms, Appell--Lerch functions, and false theta functions as q-brackets of functions on partitions*](https://arxiv.org/abs/2401.02820), equations (2.12)--(2.15), which reproduce the exact (A_\ell), completion, elliptic law, and modular law used above.
* Bringmann--Nazaroglu, [*A Framework for Modular Properties of False Theta Functions*](https://arxiv.org/abs/1904.05377), Theorems 1.2 and 1.5 and Lemma 3.3.
* Bringmann--Folsom--Milas, [*Asymptotic behavior of partial and false theta functions arising from Jacobi forms and regularized characters*](https://arxiv.org/abs/1604.01977), Theorem 1.1.
* Bringmann--Kaszian--Milas--Nazaroglu, [*Integral Representations of Rank Two False Theta Functions and Their Modularity Properties*](https://arxiv.org/abs/2101.02902), Proposition 3.2.
* Bringmann--Rolen, [*Radial limits of mock theta functions*](https://arxiv.org/abs/1409.3782), checked for scope; it supplies no square-root-phase transfer theorem.

## 7. Recommended state effect

**Promote, scoped:** accept (1.1), (1.2), the correct (K_4) normalization, the explicit correction (2.4), and the verified (\Gamma(2)) stabilization of the completed moving section as structural lemmas.  Also retain (3.4)--(3.5) as a rigorous no-go for the naive “uniform additive twists plus (L^1) Fourier inversion” route.

**Reject as inapplicable:** unary false-theta, positive-definite rank-two false-theta, fixed vertical-cusp, and pointwise radial-limit theorems do not prove the Round-63 target.  Retain the signed estimate, M9-M1, M9, and the final exponent with no change.  Any continuation must derive a correction-preserving transform estimate uniform over the square-root frequency window; the Appell representation alone earns no exponent promotion.
