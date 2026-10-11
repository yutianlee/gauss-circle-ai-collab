# Round226 conductor complex-heat application control

## 1. Result

Absolute heat majorization on legal straight subordination rays loses a
factor comparable to sqrt(omega/sigma) as z=sigma-i omega approaches
the imaginary direction with omega>=2sigma and sigma sqrt(N) bounded.
For the actual circle-wave shell with sigma=N^(-1/2), omega=2pi R,
this factor is T^(1/2)N^(1/4). It supplies no complete improvement.
This is a lower price for this explicitly defined absolute-integral
certificate, not a lower bound on the actual oscillatory wave.

## 2. Exact statement and hypotheses

First use arbitrary finite coefficients a_n on integer N<=n<=2N.
Let A=sum|a_n|, H(t)=sum a_n exp(-nt), S(z)=sum a_n exp(-z sqrt(n)).
For -pi/2<theta<pi/2 put c=cos(theta) and
\[
 D_\theta=\Re(z^2e^{-i\theta})
 =(\sigma^2-\omega^2)c-2\sigma\omega\sin\theta.
\]
The strict rays considered satisfy D_theta>0. Principal powers have
continuous arguments along each ray. The finite subordination identity
and resulting absolute certificate are
\[
 S(z)=\frac z{2\sqrt\pi}\int_{0}^{e^{i\theta}\infty}
      t^{-3/2}e^{-z^2/(4t)}H(t)\,dt,\qquad
 |S(z)|\le A Q_N(z,\theta),
\]
\[
 Q_N(z,\theta)=\frac{|z|}{\sqrt{D_\theta}}\,
            e^{-\sqrt{N cD_\theta}}.
 \tag{1}
\]
This application requires only strict rays, not any extension of
boundary identities to infinite theta series.

## 3. Independent derivation and actual full cost

For Re(a),Re(b)>0 the Gaussian integral gives
\[
 \int_0^\infty u^{-3/2}e^{-a/(4u)-bu}\,du
       =2\sqrt\pi\,a^{-1/2}e^{-\sqrt{ab}}.
\]
The positive-real identity extends holomorphically in the right
half-planes; the branch is continued from positive a,b.
On the ray substitute a=z^2e^(-i theta), b=n e^(i theta).
The strict conditions ensure the square roots give
sqrt(a)=z e^(-i theta/2) and sqrt(ab)=z sqrt(n).
The factor dt*t^(-3/2)=e^(-i theta/2)du*u^(-3/2) cancels
the same phase in sqrt(a). Finite summation then proves the identity.
The elementary bound |H(e^(i theta)u)|<=A exp(-Nc u) gives (1).
For omega>sigma the real positive ray has D_0<0 and cannot be
substituted into this absolutely convergent formula.

For omega>=2sigma, D_theta<=2sigma omega on every strict legal ray,
and the exact square identity
\[
 cD_\theta=\sigma^2-(\sigma\sin\theta+\omega\cos\theta)^2
                         \le\sigma^2
\]
gives
\[
 Q_N(z,\theta)\ge
 \frac{|z|}{\sqrt{2\sigma\omega}}e^{-\sigma\sqrt N}.
 \tag{2}
\]
The legal ray theta=arg(z) has c=sigma/|z| and
D_theta=sigma|z|, so
\[
 Q_N(z,\arg z)=
 \sqrt{|z|/\sigma}\,e^{-\sigma\sqrt N}.
 \tag{3}
\]
Equations (2)--(3) give matching constant-factor bounds on the infimum
over these rays. If sigma sqrt(N)<=C, that infimum is comparable to
sqrt(omega/sigma), with constants depending only on C.

For a single coefficient a_N=1, the actual value is
|S(z)|=exp(-sigma sqrt(N)). The certificate's excess factor is therefore
real, but it cannot be transferred to an actual-value lower bound.
For omega=0, theta=0 attains the sharp elementary bound.
As D_theta decreases to zero while c>0 the certificate diverges.
The distinct boundary c->0 can have a finite coefficientwise limit;
it does not grant an infinite-theta boundary theorem.

Now take an actual finite circle-wave shell
\[
 S_N(R)=\sum_n r_2(n)n^{-3/4}\Psi(\sqrt{n/T})v(n/N)e(R\sqrt n)
\]
with fixed smooth v supported in [1,2]. Choose sigma=N^(-1/2),
omega=2pi R and coefficients
a_n=r_2(n)n^(-3/4)Psi(sqrt(n/T))v(n/N)exp(sigma sqrt(n)).
Then S(z)=S_N(R) EXACTLY; exp(sigma sqrt(n))<=exp(sqrt2)
on the shell, and its scaled derivatives are bounded. Thus, for each
fixed Schwartz order J,
\[
 A_N\ll_{\epsilon,J}N^{1/4+\epsilon}(1+N/T)^{-J}.
\]
At large T with R~T, (3) yields the absolute-ray certificate
\[
 |S_N(R)|\ll T^{1/2+\epsilon}N^{1/2}
                        (1+N/T)^{-J}.
 \tag{4}
\]
The lower comparison (2) diagnoses the same loss in that coefficient
majorant; it does not assert A_N has any fixed lower size on every shell.
For positive nonempty low shells it can be tested directly, but no
such arithmetic lower test is needed for the complete comparison.

The elementary original shell bound A_N is already stronger than (4).
Summing its dyadic prices gives the complete complex T^(1/4+epsilon).
The whole inherited real T^(beta+epsilon) is stronger still.
Pay n=1 separately. For every prescribed A the original full tail
n>T^(3/2) is O(T^(-A)) at sufficiently large FIXED Schwartz order.
No global coefficient exp(sigma sqrt(n)) is introduced into the
infinite original series: damping is undone only inside each finite
shell, before summation. This avoids a false infinite convergence claim.

The accepted sharp bridge converts a complete exponent gamma>=0 to
1/4+gamma/2; for a general gamma use max(gamma,0). The above elementary
complex fallback gives3/8 and the inherited real bound keeps theta_LY.
No new full wave, moment, M1/M2/GAR or endpoint bound is proved.

## 4. First doubtful or unproved step

A signed heat/theta estimate might retain cancellations discarded in
|H(t)|<=A exp(-N Re t), or a different contour might have other costs.
Neither is supplied here. The control excludes only this named
straight-ray absolute-majorant transfer as a source of improved bounds.
It neither prices arbitrary contours nor refutes any actual theta method.

## 5. Controls and outcome

All ray constants and branches, finite interchange, omega=0, empty
sequence, one-coefficient comparison, different sector boundaries,
shellwise damping removal, actual coefficients, both real signs,
singleton and full tail are included. Zero mathematical experiments.
The separate isolated derivation and independent application review
are required before this control contributes to round closure.

## 6. Dependencies and provenance

Conductor, round226, 2026-09-28. Graph SHA256
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
Inputs: protocol, graph/manifest, strategy226, current complete interface,
pinned Sep23 review, closed223 checkpoint, closed225 synthesis and
accepted204 sharp-wave kernel. Equations (1)--(4) were independently
derived by the conductor before the isolated report was available.
No external theorem is imported by this elementary control.

## 7. Recommended state effect

Retain as scoped transfer evidence after independent review. Identity
graph effect; no proof-draft edit or complete improvement follows.
The actual signed heat/theta kernel remains eligible for a separately
proved bound with all contours and parameters controlled.
