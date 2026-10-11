# Round226 independent subordination application review

## 1. Result

**GREEN, with the scope stated below.** The reviewed conductor control, SHA256
69186e78d593c27618f89f16fba22436fec5e64dac078e182e1dbf235767ff8a,
correctly prices its specified straight-ray absolute heat majorant and
correctly finds no complete improvement. The sector, constant, damping
removal, arithmetic coefficient, tail and physical normalization checks
pass. No repair to that artifact is required.

The lower comparison is for the explicitly defined integral certificate
\(A_NQ_N\). It is not a lower bound for the actual signed wave, a theorem
about every heat estimate, or a lower bound for arbitrary contours.
This is a separate nonauthor application review after my isolated
derivation was frozen. It does not independently review my own derivation.

## 2. Exact statement and hypotheses

The application uses \(N\ge1\), positive damping \(\sigma>0\),
\(\omega\ge0\), and finitely many coefficients supported on the integers
in \([N,2N]\). Put
\[
 z=\sigma-i\omega,\quad Z=|z|,\quad
 A=\sum_n|a_n|,\quad H(t)=\sum_n a_ne^{-nt},\quad
 S(z)=\sum_n a_ne^{-z\sqrt n}.
\]
Only strict rays
\[
 -\pi/2<\theta<\pi/2,\qquad
 c=\cos\theta>0,\qquad D=\Re(z^2e^{-i\theta})>0
\]
are used. If \(\alpha=\arctan(\omega/\sigma)\), their precise interval
is \(-\pi/2<\theta<\pi/2-2\alpha\). On these rays,
\[
 S(z)=\frac{z}{2\sqrt\pi}\int_{0}^{e^{i\theta}\infty}
 t^{-3/2}e^{-z^2/(4t)}H(t)\,dt,\qquad
 |S(z)|\le A Q_N,\qquad
 Q_N=\frac Z{\sqrt D}e^{-\sqrt{NcD}}.                 \tag{R1}
\]
For \(\omega\ge2\sigma\),
\[
 \frac Z{\sqrt{2\sigma\omega}}e^{-\sigma\sqrt N}
 \le \inf_{\theta}Q_N
 \le \sqrt{\frac Z\sigma}e^{-\sigma\sqrt N}.          \tag{R2}
\]
Consequently, for \(0<\sigma\sqrt N\le C_0\),
\[
 \frac{e^{-C_0}}{\sqrt2}\sqrt{\frac\omega\sigma}
 \le\inf_\theta Q_N
 \le(5/4)^{1/4}\sqrt{\frac\omega\sigma}.              \tag{R3}
\]
The constants are independent of the finite coefficient vector.
The actual application has fixed accepted real Schwartz \(\Psi\),
real \(T\ge2\), \(R\in[c_0T,C_0'T]\) with fixed positive endpoints,
and a fixed bounded smooth shell cutoff. No uniformity over arbitrary
moving profiles or unbounded profile seminorms is asserted.

## 3. Proof and complete cost checks

**Identity, branches and the norm.** For \(\Re a,\Re b>0\), the
elementary Gaussian identity is
\[
 \int_0^\infty u^{-3/2}e^{-a/(4u)-bu}\,du
 =2\sqrt\pi\,a^{-1/2}e^{-\sqrt a\sqrt b}.
\]
Its holomorphic continuation is locally dominated at both endpoints.
The principal roots satisfy \(\sqrt a\sqrt b=\sqrt{ab}\) here:
the sum of their original arguments lies strictly between \(-\pi\)
and \(\pi\). Substitute \(a=z^2e^{-i\theta}\),
\(b=ne^{i\theta}\). The strict sector gives
\(\arg(z e^{-i\theta/2})\in(-\pi/4,\pi/4)\), so
\(\sqrt a=z e^{-i\theta/2}\), and
\(\sqrt a\sqrt b=z\sqrt n\). The factor
\(dt\,t^{-3/2}=e^{-i\theta/2}u^{-3/2}du\) gives exactly the
prefactor in (R1). The sum is finite.

Taking the modulus of the kernel and using
\(|H(e^{i\theta}u)|\le A e^{-Ncu}\) gives
\[
 \frac Z{2\sqrt\pi}\int_0^\infty
 u^{-3/2}e^{-D/(4u)-Ncu}\,du
 =\frac Z{\sqrt D}e^{-\sqrt{NcD}}.
\]
Thus (R1) is the exact norm of this majorant; no factor of \(2\),
\(\pi\), or ray Jacobian is missing.

**Optimization and boundaries.** Direct calculation gives
\[
 D=(\sigma^2-\omega^2)c-2\sigma\omega\sin\theta,
 \qquad
 cD=\sigma^2-(\sigma\sin\theta+\omega\cos\theta)^2.
\]
For \(\omega\ge2\sigma\), the first term in \(D\) is nonpositive,
so \(D\le2\sigma\omega\); the square identity gives \(cD\le\sigma^2\).
These prove the lower bound in (R2). The legal ray
\(\theta=\arg z=-\alpha\) has \(c=\sigma/Z\) and \(D=\sigma Z\),
which proves its upper bound. Using
\(\omega\le Z\le(\sqrt5/2)\omega\) proves (R3).
For \(\omega>\sigma\), \(D_0<0\); a real-ray substitution is illegal.
For \(\omega=0\),
\(Q_N=(\cos\theta)^{-1/2}e^{-\sigma\sqrt N\cos\theta}\)
is minimized at \(\theta=0\), with value \(e^{-\sigma\sqrt N}\).

As \(D\downarrow0\) with \(c>0\), this majorant diverges.
The other boundary \(c\downarrow0\) is different: for fixed
\(\sigma,\omega>0\) its lower-sector limit is
\(Z/\sqrt{2\sigma\omega}\). These observations do not assert either
necessity for special cancelling coefficient vectors or an infinite
theta-series boundary identity. The application requires neither.

**Actual coefficients and removal of damping.** Write
\[
 b_n=r_2(n)n^{-3/4}\Psi(\sqrt{n/T})v(n/N),\qquad
 \sigma=N^{-1/2},\quad\omega=2\pi R,\quad
 a_n=b_ne^{\sigma\sqrt n}.
\]
Then \(a_ne^{-z\sqrt n}=b_ne(R\sqrt n)\) exactly. On the shell,
\[
 e\le e^{\sigma\sqrt n}\le e^{\sqrt2},\qquad
 e\sum|b_n|\le A_N\le e^{\sqrt2}\sum|b_n|.
\]
The lower inequality is understood trivially for an empty or zero
shell. The restoring factor is the fixed scaled function
\(e^{\sqrt{n/N}}\), with every fixed scaled derivative bounded.
It changes neither the actual \(r_2\) coefficients nor their signs
through \(\Psi\) and \(v\). No multiplicativity or positive-weight
assumption is used.

The elementary \(r_2(n)\ll_\eta n^\eta\) estimate and Schwartz decay
give, for every fixed \(J\),
\[
 A_N\ll_{\eta,J}N^{1/4+\eta}(1+N/T)^{-J}.
\]
At large \(T\), \(\omega\ge2\sigma\) uniformly for all \(N\ge1\),
and \(Q_N(z,\arg z)\asymp T^{1/2}N^{1/4}\), since
\(\sigma\sqrt N=1\). Hence the displayed ray bound is
\[
 |S_N(R)|\ll_{\epsilon,J}
 T^{1/2+\epsilon}N^{1/2}(1+N/T)^{-J}.                 \tag{R4}
\]
The \(N^\eta\)-to-\(T^\epsilon\) conversion is legitimate. Below
\(N\le T^{3/2}\), choose \(\eta\) sufficiently small. If (R4) is
used for every shell, use
\(N^\eta\le T^\eta(1+N/T)^\eta\) and initially take a larger fixed
Schwartz order. Thus there is no hidden restriction to polynomial
\(N\) in the final decaying version of (R4).

**Complete wave, endpoints and tail.** Summing the displayed prices
in (R4) over a genuine dyadic covering gives \(T^{1+\epsilon}\).
The elementary original coefficient bound instead gives
\[
 \sum_{n\ge1}r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|
 \ll_\epsilon T^{1/4+\epsilon},                     \tag{R5}
\]
because \(\sum_N N^{1/4+\eta}(1+N/T)^{-J}
\ll T^{1/4+\eta}\) for \(J>1/4+\eta\).
The control correctly keeps this better fallback.

An arbitrary single smooth \(v\) supported on \([1,2]\) need not be
a dyadic partition of unity. This causes no gap: (R5) follows using
disjoint half-open integer blocks, for which the same coefficient
bound applies, or a fixed overlapping smooth partition. The heat
identity and coefficient estimate require no cutoff differentiability.
All partial blocks retain their exact integer membership. No endpoint
mass disappears through a proposed smooth partition.

The singleton \(n=1\) is \(O(1)\), since \(r_2(1)=4\) and \(\Psi\)
is bounded. With \(Z_0=T^{3/2}\), for a fixed decay order \(L\)
large enough that \(L/2>1/4+\eta\),
\[
 \sum_{n>Z_0}r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|
 \ll_{\eta,L}T^{L/2}Z_0^{1/4+\eta-L/2}
 =T^{3/8+3\eta/2-L/4}.
\]
Every prescribed \(O(T^{-A})\) follows by a sufficiently large
fixed \(L\). This is uniform in \(R\), includes real truncation
endpoints literally, and uses the original coefficients. Different
finite shells can have different \(\sigma\) and rays; no common
infinite heat integral or global exponentially enlarged coefficient
series has been introduced.

For the complete complex wave \(W_T(R)=\sum b_n^{\,0}e(R\sqrt n)\),
where \(b_n^{\,0}=r_2(n)n^{-3/4}\Psi(\sqrt{n/T})\) is real,
\[
 B_T(R)=\Re\!\left(e(-3/8)W_T(R)\right).
\]
This identity accounts for both cosine signs without assuming an
inherited complex-wave or separate-block exponent \(\beta\).

**Physical restoration.** Accepted204 gives the complete inclusive
bridge
\[
 P(R^2)=\frac{\sqrt R}{\pi}B_T(R)
       +O_\epsilon(T^{1/2+\epsilon}).
\]
It already pays the sharp annulus endpoints and the entire Bessel
remainder. A complete bound \(B_T\ll T^{\gamma+\epsilon}\) therefore
gives physical exponent \(1/4+\max(\gamma,0)/2\). Equation (R5)
has \(\gamma=1/4\), giving \(3/8\); the weaker summed ray menu would
give \(3/4\). Keeping the inherited complete real exponent
\(\beta=2\theta_{\rm LY}-1/2\) instead retains \(\theta_{\rm LY}\).
No improvement to an individual M1/M2/GAR owner or to the accepted
fixed-order moments follows.

## 4. First doubtful or unproved step

There is no unproved step in the scoped application above. The first
additional step needed for a gain would be a signed estimate for the
actual heat sum that improves its coefficient majorant after all
parameters and contours are paid, or another fully controlled transform.
Neither the finite identity nor (R2) supplies that estimate.

In particular, a lower bound for \(Q_N\) cannot be promoted to a
lower bound for \(|S_N|\), even if \(A_N>0\). Nor does the upper
estimate for \(A_N\) establish its matching lower size on every
actual shell. Possible vanishing, sign changes, empty shells and
boundary cancellation are consistent with this review.

## 5. Required controls and outcome

All controls are analytic; no experiments were performed.

- A single coefficient \(a_N=1\), with integer \(N\), has actual
  modulus \(e^{-\sigma\sqrt N}\), whereas its best certificate has
  the additional order \(\sqrt{\omega/\sigma}\). This demonstrates
  a loss of the method without asserting a large actual value.
- For an empty or zero coefficient vector all integrals vanish.
  At \(\omega=0\) the positive real ray gives the sharp coefficient
  certificate. The two different sector boundaries were checked
  separately.
- Shell damping removal is exact with bounded factor; all original
  coefficient signs survive. The full original tail, singleton,
  exact block endpoints and both real phases are restored.
- The complete real inherited estimate is used only for that whole
  real wave. The smoothing floor persists when a hypothetical
  \(\gamma<0\) is substituted into the physical bridge.

These controls support GREEN for the specified certificate and its
complete fallback comparison only.

## 6. Dependencies and exact artifacts used

This is a post-isolation, nonblind, nonauthor review of the conductor's
application. I retain earlier round history and authored the frozen
isolated report listed below. That report is disclosed prior work,
not a report independently reviewed by its author. No current source
report, sibling review, graph file, new primary source or unlisted
application context was opened for this task.

Exact authorized artifacts and SHA256:

- protocol.md:
  f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
- rounds/codex-managed/gc-full-goal-spectral-source-review/controls/conductor_subordination_application.md:
  69186e78d593c27618f89f16fba22436fec5e64dac078e182e1dbf235767ff8a.
- rounds/codex-managed/gc-full-goal-spectral-source-review/briefs/conductor_complete_spectral_interfaces.md:
  8e9cb720ca0495aafc003434877dcd0067779993fc1edd5657b93d35ef9e77e5.
- strategy/round226_full_goal_spectral_source_review.md:
  61ac5c2a26bf87f25133d8858dd2b4a0c6e377df657ddaeaa57d422d41e287ad.
- proofs/kernels/gc_complete_square_root_large_values_moment_bound.md:
  942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212.
- My previously frozen
  rounds/codex-managed/gc-full-goal-spectral-source-review/reports/blind_complex_subordination.md:
  35b28a172e791013cab241a44d47c43b0aea8fd6f7e372be3665b48146a45c0e.
  Its hash was verified; its retained derivation is disclosed reuse.

Only this assigned review was written.

## 7. Recommended state effect

Retain the conductor control as scoped method evidence after the other
required seams. No analytic bound, graph promotion, proof-draft change
or improvement to the inherited physical exponent is recommended by
this review. The signed heat/theta problem remains open. Stop after
freezing this review.
