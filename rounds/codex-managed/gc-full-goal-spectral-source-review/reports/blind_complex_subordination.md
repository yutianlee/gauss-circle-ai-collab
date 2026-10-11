# Round 226: isolated complex subordination

## 1. Result

Write
\[
 z=\sigma-i\omega=Z e^{-i\alpha},\quad
 Z=\sqrt{\sigma^2+\omega^2},\quad
 \alpha=\arctan(\omega/\sigma)\in[0,\pi/2).
\]
The universally admissible rays for absolute integration are exactly
\[
 \boxed{-\pi/2<\theta<\pi/2-2\alpha.}
 \tag{1}
\]
On these rays the stated subordination identity holds with its printed constant and outward orientation. There is a sequence-dependent boundary exception: when
\(\Re(z^2e^{-i\theta})=0\), a nonzero finite sequence gives an absolutely convergent integral exactly when \(\sum_n a_n=0\).

Put \(D_\theta=\Re(z^2e^{-i\theta})\). On (1), the exact absolute-envelope multiplier is
\[
 \boxed{
 Q_N(z,\theta)=\frac{Z}{\sqrt{D_\theta}}\,
       \exp\!\left(-\sqrt{N D_\theta\cos\theta}\right).}
 \tag{2}
\]
For \(\omega\ge2\sigma\),
\[
 \boxed{
 \frac1{\sqrt2}\sqrt{\frac Z\sigma}e^{-\sigma\sqrt N}
 \le\inf_{\theta\text{ in }(1)}Q_N(z,\theta)
 \le\sqrt{\frac Z\sigma}e^{-\sigma\sqrt N}.}
 \tag{3}
\]
The upper bound is achieved as a certificate by the legal ray \(\theta=-\alpha\). In the requested range \(0<\sigma\sqrt N\le C\), the infimum consequently has order \(\sqrt{\omega/\sigma}\), with constants depending only on \(C\). The stronger comparison (3) does not need that restriction.

This is current statement-only isolation by a reused agent with retained earlier reports and reviews. It is not history-free work. Only the assigned packet and protocol were read. No application, other brief, graph, strategy, source, sibling or experiment was consulted.

## 2. Exact hypotheses and conventions

Let \(a_n\) be finitely supported on positive integers, and define
\[
 S(z)=\sum_n a_n e^{-z\sqrt n},\qquad
 H(t)=\sum_n a_n e^{-nt}.
\]
Throughout \(\sigma>0,\omega\ge0\). The ray is parametrized outward by
\(t=e^{i\theta}u\), \(0<u<\infty\), with \(-\pi/2<\theta<\pi/2\). Its principal power and differential satisfy
\[
 t^{-3/2}=e^{-3i\theta/2}u^{-3/2},\qquad
 t^{-3/2}dt=e^{-i\theta/2}u^{-3/2}du.
 \tag{4}
\]
All exponentials here are ordinary exponentials, with no hidden \(2\pi\).

For the multiplier calculation assume \(N\) is an integer at least one, \(a_n=0\) outside \(N\le n\le2N\), and \(A=\sum_n|a_n|\). The upper endpoint is not needed for the envelope estimate beyond ensuring the stipulated finite setting. Empty sequences are treated separately.

“Universally admissible” means that absolute integration works for every such finite sequence. Particular sequences with cancellation at \(t=0\) have the boundary extension specified in Section 3.

## 3. Proof and exact constants

### Scalar integral and complex continuation

For positive real \(w,\lambda\), substitution \(v=w/(2\sqrt u)\) gives
\[
 \int_0^\infty u^{-3/2}e^{-w^2/(4u)-\lambda u}\,du
 =\frac4w\int_0^\infty e^{-v^2-c^2/v^2}\,dv,
 \qquad c=w\sqrt\lambda/2.
\]
Let \(J(c)\) be the last integral. Differentiation for \(c>0\), followed by \(v=c/y\), gives
\[
 J'(c)=-2c\int_0^\infty v^{-2}e^{-v^2-c^2/v^2}\,dv=-2J(c).
\]
Dominated convergence gives \(J(0)=\sqrt\pi/2\), from the Gaussian integral. Therefore
\[
 \int_0^\infty u^{-3/2}e^{-w^2/(4u)-\lambda u}\,du
 =\frac{2\sqrt\pi}{w}e^{-w\sqrt\lambda}.
 \tag{5}
\]
The differentiation is justified by exponential decay at both ends for \(c>0\). On compact subsets of
\[
 |\arg w|<\pi/4,\qquad \Re\lambda>0,
\]
the integral in (5) is holomorphic and uniformly dominated at both endpoints. The identity theorem, first in \(w\) and then in \(\lambda\), extends (5) throughout that domain, using the principal square root of \(\lambda\).

For a ray satisfying (1), set
\[
 w=z e^{-i\theta/2},\qquad \lambda=n e^{i\theta}.
\]
Then \(|\arg w|<\pi/4\), \(\Re\lambda>0\), and
\(w\sqrt\lambda=z\sqrt n\). Combining (4)--(5) yields
\[
 \frac{z}{2\sqrt\pi}
 \int_{0}^{\infty e^{i\theta}}
 t^{-3/2}e^{-z^2/(4t)}e^{-nt}\,dt=e^{-z\sqrt n}.
 \tag{6}
\]
This checks the sign, orientation, square-root branch and full constant. Finite summation of (6) proves the requested identity for \(S\).

### Exact absolute-convergence sector

Along the ray,
\[
 D_\theta=(\sigma^2-\omega^2)\cos\theta-2\sigma\omega\sin\theta
          =Z^2\cos(2\alpha+\theta).
 \tag{7}
\]
At infinity, \(\cos\theta>0\) and positive support ensure exponential decay of \(H(e^{i\theta}u)\). At zero, the universal absolute integrand is controlled by
\(u^{-3/2}e^{-D_\theta/(4u)}\).
Thus \(D_\theta>0\) suffices.

Because \(2\alpha+\theta\in(-\pi/2,3\pi/2)\), the condition \(D_\theta>0\) in the stipulated ray family is exactly (1). In particular the positive real ray works universally when \(\omega<\sigma\). When \(\omega>\sigma\), it has \(D_0<0\) and fails for every nonzero finite sequence. At \(\omega=\sigma\), it is the zero-\(D\) boundary and fails absolute convergence unless the coefficient sum vanishes.

For necessity and the exception, a nonzero finite \(H\) is entire and has a finite vanishing order \(m\ge0\) at zero. It is not identically zero: along positive real \(t\), the least supported exponential separates its nonzero coefficient. Therefore near zero the absolute integrand is comparable to
\[
 u^{m-3/2}e^{-D_\theta/(4u)}.
\]
For \(D_\theta<0\) it diverges for every finite \(m\). For \(D_\theta=0\) it is integrable exactly when \(m\ge1\), equivalently \(H(0)=\sum_n a_n=0\). If this boundary lies inside the stipulated open ray family, it is \(\theta=\pi/2-2\alpha\) with \(\omega>0\).

For such a zero-sum sequence, the boundary identity follows by approaching through the strict sector: uniformly near zero \(H(e^{i\theta}u)=O(u)\), giving the integrable bound \(O(u^{-1/2})\); at infinity a fixed positive lower bound for \(\cos\theta\) supplies exponential decay. Dominated convergence applies to the combined \(H\). This argument does not claim absolute convergence of each individual exponential integral at that boundary.

Contour deformation between any two strict legal rays is also justified directly. The intervening closed angular sector has positive lower bounds for both \(\cos\theta\) and \(D_\theta\). On its small circular arc the integral is bounded by \(O(\rho^{-1/2}e^{-c/\rho})\); on its large arc it is \(O(L^{-1/2}e^{-c'L})\). Both vanish. The principal power is analytic throughout the sector. One cannot justify rotation from an already divergent positive-real integral when \(\omega>\sigma\); the continuation proof above avoids that mistake.

### Exact ray multiplier

On every strict legal ray,
\[
 |H(e^{i\theta}u)|\le A e^{-N\cos\theta\,u}.
\]
Taking absolute values in the integral gives
\[
 |S(z)|\le
 A\frac Z{2\sqrt\pi}\int_0^\infty
 u^{-3/2}\exp\left(-\frac{D_\theta}{4u}-N\cos\theta\,u\right)\,du.
\]
Formula (5), applied with positive real \(w=\sqrt{D_\theta}\) and
\(\lambda=N\cos\theta\), proves (2). The angular factor in (4) has modulus one and introduces no additional factor.

At a sequence-dependent zero-\(D\) boundary, the crude envelope \(A e^{-N\cos\theta u}\) does not retain the cancellation \(H(0)=0\); its resulting multiplier is infinite. This does not contradict absolute convergence of the combined zero-sum integrand.

### Optimal order among straight rays

The central ray \(\theta=-\alpha\) is strict legal and has
\[
 \cos\theta=\sigma/Z,\qquad D_\theta=\sigma Z,\qquad
 Q_N(z,-\alpha)=\sqrt{Z/\sigma}\,e^{-\sigma\sqrt N}.
 \tag{8}
\]
Suppose \(\omega\ge2\sigma\). On the entire legal angular interval,
\(2\alpha+\theta\) lies between \(2\alpha-\pi/2>0\) and \(\pi/2\). Hence
\[
 0<D_\theta\le Z^2\sin(2\alpha)=2\sigma\omega.
 \tag{9}
\]
Also the exact identity
\[
 D_\theta\cos\theta
   =\sigma^2-Z^2\sin^2(\alpha+\theta)\le\sigma^2
 \tag{10}
\]
holds. Consequently every such ray obeys
\[
 Q_N(z,\theta)\ge
 \frac Z{\sqrt{2\sigma\omega}}e^{-\sigma\sqrt N}
 \ge\frac1{\sqrt2}\sqrt{Z/\sigma}\,e^{-\sigma\sqrt N}.
\]
Together with (8), this proves (3), without assuming existence or a formula for an exact minimizing angle.

Since \(1\le Z/\omega\le\sqrt5/2\) when \(\omega\ge2\sigma\), a fully explicit version in the requested range is
\[
 \frac{e^{-C}}{\sqrt2}\sqrt{\frac\omega\sigma}
 \le\inf_\theta Q_N(z,\theta)
 \le(5/4)^{1/4}\sqrt{\frac\omega\sigma}.
 \tag{11}
\]
This proves matching uniform order. It optimizes only the specified absolute-ray certificate.

## 4. First unproved step and scope

No gap remains in the finite identities, convergence classifications or certificate comparisons. None supplies a bound for an unprovided infinite theta series. Such a passage would need independent convergence, domination and interchange estimates uniform in the new parameters.

Nor is the infimum in (3) the norm of the original coefficient functional. Contour cancellation can make the original value much smaller than every absolute-ray certificate, as the following exact control shows.

## 5. Required controls and outcomes

For a single nonzero coefficient \(a_N=a\),
\[
 S(z)=a e^{-z\sqrt N},\qquad |S(z)|=|a|e^{-\sigma\sqrt N}.
\]
Moreover \(|H(e^{i\theta}u)|=|a|e^{-N\cos\theta u}\), so the absolute-integral certificate is exactly \(|a|Q_N(z,\theta)\). There is no loss in the preliminary bound on \(H\) in this test.

Indeed the exact operator norm on the coefficient space supported in \([N,2N]\), with its \(\ell^1\) norm, is
\[
 \|a\mapsto S(z)\|_{\ell^1\to\mathbb C}=e^{-\sigma\sqrt N}.
\]
The elementary coefficient triangle proves the upper bound, and the singleton at \(N\) attains it. For \(\omega\ge2\sigma\), (3) shows that the optimized absolute-ray price divided by this norm lies between
\(\sqrt{Z/\sigma}/\sqrt2\) and \(\sqrt{Z/\sigma}\). Thus the ray certificate can be arbitrarily more expensive without any actual functional growth.

If \(\omega=0\), all stipulated rays are strict legal and
\[
 Q_N(\sigma,\theta)=(\cos\theta)^{-1/2}
             e^{-\sigma\sqrt N\cos\theta}.
\]
Both factors are minimized together at \(\theta=0\), giving the exact minimum \(e^{-\sigma\sqrt N}\). The singleton then attains equality on the positive real ray.

For fixed \(\omega>0\), at the lower angular boundary,
\[
 \lim_{\theta\downarrow-\pi/2}Q_N(z,\theta)
 =\frac Z{\sqrt{2\sigma\omega}}.
\]
Although \(\theta=-\pi/2\) is outside the stipulated open family, the limiting integral itself is absolutely convergent for a finite sequence: at infinity \(|H(-iu)|\le A\) and \(u^{-3/2}\) is integrable; at zero \(D=2\sigma\omega>0\). Dominated convergence from legal rays retains identity (6) there.

At the other boundary \(\theta\uparrow\pi/2-2\alpha\), \(D_\theta\downarrow0\), while \(\cos\theta\to\sin(2\alpha)>0\), and \(Q_N\to\infty\). Generic nonzero-sum sequences lose absolute convergence. Zero-sum finite sequences have the combined-integrand extension proved above. If \(\omega=0\), both angular endpoints give \(Q_N\to\infty\); they are not included in the stipulated ray family. At those excluded endpoints a zero-sum finite sequence again has an absolutely convergent combined integral and the limiting identity: use \(O(u^{-1/2})\) at zero and \(O(u^{-3/2})\) at infinity. Without the zero sum, absolute convergence at zero fails.

The empty sequence has \(S=H=0\) and zero integral on every stipulated ray, regardless of \(D_\theta\). It is treated directly rather than through an expression \(0\cdot\infty\).

Finite sum exchange on strict rays is justified term by term by absolute convergence. All formulas include \(N=1\). As \(\sigma\downarrow0\) with fixed \(\omega>0,N\), the legal angular interval collapses toward \(-\pi/2\) and the optimized certificate diverges at order \(\sqrt{\omega/\sigma}\), while the singleton modulus tends to \(|a|\). The statement always keeps \(\sigma>0\); no boundary theorem at \(\sigma=0\) is asserted.

All controls are analytical or exact algebra. Zero experiments were used.

## 6. Exact inputs and provenance

Campaign: gc-full-goal-spectral-source-review. Round: 226. Role: blind_complex_subordination. Current statement-only isolation with retained prior history disclosed in Section 1.

Exactly two input files were read:

| Input | SHA-256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| rounds/codex-managed/gc-full-goal-spectral-source-review/briefs/blind_complex_subordination_statement.md | 5666b5ab44da69ab9b35dbcd28658cd9a9e9ba5dd454d25fe1df8ef21222b39a |

The proof uses elementary integration, the Gaussian integral, holomorphic continuation and finite sums. No external source was read or imported as an unverified theorem. No graph hash, application or other task conclusion is inferred. This report is the sole output.

## 7. Recommended state effect

Retain the finite subordination identity, exact sector qualification, absolute-ray norm calculation and singleton control as statement-only evidence for the conductor's review. They assert no application bound or universal obstruction to other representations. No shared state is changed and no successor is proposed. Stop after freezing this report.
