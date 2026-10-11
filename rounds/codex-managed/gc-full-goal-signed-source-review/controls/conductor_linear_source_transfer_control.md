# Round223 conductor coefficient and absolute-transfer control

## 1. Result

The undamped multiplicative function f(n)=r2(n)/4 does not belong to any
fixed-A class with sum_(n<=x)|f(n)|^2<=A^2 x for all x. Fixed positive
power damping repairs that premise, but does not make the actual nonlinear,
masked wave a linear-phase theorem application. Even in a favorable smooth
unmasked block, the particular continuous absolute-Fourier transfer of a
generic N/log N source term has a power-sized certificate cost. This is
neither a lower bound for the actual sum nor an optimal discrete norm.

## 2. Exact hypotheses

Let chi4 be the real character modulo4, f=1*chi4, e(t)=exp(2pi i t).
Fix eta>0 and g_eta(n)=f(n)n^(-eta). Let omega be a fixed nonzero
nonnegative smooth function compactly supported in (1,2), and Psi the
actual even real Schwartz mollifier transform with Psi(0)=1. Consider
R comparable to T, T large, and N comparable to T^(2/3). The unmasked
complex block is
\[
 U(R)=4\sum_n f(n)n^{-3/4}\omega(n/N)
                      \Psi(\sqrt{n/T})e(R\sqrt n).
\]
The cosine and its negative-frequency companion require their own exact
pairing; an upper bound for U would suffice, but a lower bound for U is
not asserted. The large-squarefree mask is addressed separately below.

## 3. Derivation and exact scope of the source certificate

At p=2, f(p^k)=1; at p=1 mod4, f(p^k)=k+1; at p=3 mod4, f(p^k) is1 for
even k and0 for odd k. Therefore, for real s>1, the absolutely convergent
Euler factors give
\[
 \sum_{n\ge1}\frac{f(n)^2}{n^s}
  =\frac{\zeta(s)^2L(s,\chi_4)^2}
         {\zeta(2s)(1+2^{-s})}.
\]
The factors follow respectively from (1-t)^(-1), (1+t)/(1-t)^3 and
(1-t^2)^(-1). Since L(1,chi4)=pi/4, the right side has a positive double
pole at s=1. A hypothetical bound sum_(n<=x)f(n)^2<=A^2x would imply by
partial summation that this series is at most A^2 s/(s-1). This is a
contradiction as s decreases to1. No Tauberian asymptotic is needed.

For every fixed eta>0, the elementary divisor estimate
f(n)<=tau(n)<=C_eta n^(eta/2) gives |g_eta(n)|<=C_eta. One proof bounds
k+1 by p^(eta k/2) for every sufficiently large prime, and takes the finite
product of sup_(k>=0)(k+1)p^(-eta k/2) for the remaining primes. Thus
g_eta is multiplicative, g_eta(1)=1, and belongs to a fixed class A_eta.
The constant is allowed to depend on eta, which stays fixed as T grows.
In particular g_(3/4) is pointwise at most1: for p=1 mod4, k+1<=2^k
<=p^(3k/4), and the other prime factors are no larger. This legal damping
does not preserve a theorem's numerical scale for free. Multiplying a
multiplicative function by N^eta generally breaks its normalization at1.

The current [Robles2609.11070v1, Theorem1.1](https://arxiv.org/html/2609.11070v1)
concerns a LINEAR phase in this fixed coefficient class. Its displayed
majorant contains a term of order M/log M at length M, as well as a
rational-approximation term. This observation is used only to price the
specified transfer; no theorem is granted for a nonlinear phase, an
exceptional frequency, a new coefficient class or a growing A. The source
auditor separately checks the exact hypotheses and constant dependence.

Put lambda=R sqrt(N), and
\[
 W_{T,N}(x)=x^{\eta-3/4}\omega(x)\Psi(\sqrt{Nx/T}),\qquad
 F(x)=W_{T,N}(x)e(\lambda\sqrt x).
\]
Then U=4N^(eta-3/4) sum_(n<=2N)g_eta(n)F(n/N), exactly. The finite linear
sum in the transfer is S(alpha)=sum_(n<=2N)g_eta(n)e(n alpha). The integer
endpoint is floor(2N). Any source bound must be checked at that actual
length and at every frequency where it is used.

For the Fourier convention Fhat(u)=integral F(x)e(-ux)dx, inversion and
periodization give
\[
 U=4N^{\eta-3/4}\int_0^1G(\alpha)S(\alpha)d\alpha,
 \quad G(\alpha)=N\sum_{m\in\mathbb Z}\widehat F(N(\alpha+m)).
\]
The absolute periodization A(alpha)=N sum_m|Fhat(N(alpha+m))| satisfies
integral A=||Fhat||_1. On this selected scale the profiles W_(T,N) have
uniformly bounded derivatives of every fixed order, and their L2 norms
stay bounded below: N/T tends to0 and Psi(s) tends to1 near0. Curvature
of sqrt(x) is bounded away from0 on the fixed support. The elementary
second-derivative integral estimate gives ||Fhat||_infinity<=C lambda^(-1/2).
Parseval then gives ||Fhat||_1>=||Fhat||_2^2/||Fhat||_infinity>=c sqrt(lambda).
For the reverse inequality, use Cauchy--Schwarz on |u|<=C lambda and
integrate the repeated-integration-by-parts bound O_j(|u|^(-j)) outside
that band. Hence ||Fhat||_1 is comparable to sqrt(lambda), uniformly in
this explicitly bounded profile family. Arbitrary moving profiles do not
inherit that assertion.

Suppose a particular application assembles a legal nonnegative majorant
B(alpha)>=|S(alpha)|, using the generic source estimate where it applies
and valid fallbacks on its complement, and keeps its N/log N term so that
B(alpha)>=c_eta N/log N everywhere. Then the absolute-transfer certificate
\[
 \mathcal C=4N^{\eta-3/4}\int_0^1A(\alpha)B(\alpha)d\alpha
 \gg_\eta \frac{R^{1/2}N^{1/2+\eta}}{\log N}.
\]
At the selected scale this price is T^(5/6+2eta/3)/log T. This is a LOWER
bound on that named UPPER certificate. The actual coefficient triangle
already gives |U|<=N^(1/4+epsilon), a much better fallback. Neither price
is an actual signed lower bound or a new complete wave/moment estimate.
Using a sharper coefficient-specific majorant, the signed periodization G,
or a different transfer is outside this certificate and remains possible.

The large-squarefree mask does not automatically preserve multiplicativity.
For Q>=1, define f_Q(n)=f(n)1_(sf(n)>Q), where sf is the squarefree part.
It has f_Q(1)=0 while being nonzero. More explicitly, for an odd prime
p=1 mod4 with p>Q, f_Q(4)=0, f_Q(p)=2 and f_Q(4p)=2, although (4,p)=1.
The same contradiction holds after n^(-eta) damping. Thus direct source
substitution is invalid. A separately proved expansion or norm transfer
could still handle this mask; none is supplied by the linear theorem.

## 4. First unproved step

A complete coefficient-sensitive nonlinear estimate, with the actual
large-class mask if used, remains missing. Fixed damping resolves only a
coefficient-class premise. The positive transfer above prices one legal
fallback construction and does not establish a necessary cost of every
Fourier representation or source application. A theorem with a sharper
actual-arithmetic term could change this conclusion and must be audited.

## 5. Controls and outcome

Raw versus damped coefficients, fixed versus growing source constants,
linear versus square-root phase, exact integer endpoints and every
exceptional frequency are distinguished. For the independent alias control,
take N=1 and W supported in (1/2,3/2), W(1)!=0. Exact periodization is
G(alpha)=W(1)e(lambda)e(-alpha) for phi=sqrt(x), so ||G||_1=|W(1)|,
whereas integral A is comparable to sqrt(lambda). This disproves a transfer
of the continuous absolute-certificate floor to the exact discrete kernel.
It is not an actual arithmetic control. All calculations are analytical;
zero mathematical experiments.

## 6. Dependencies and provenance

Conductor control, campaign gc-full-goal-signed-source-review, round223,
2026-09-28. The frozen isolated packet supplied the transfer questions;
no current blind report has been read. Source-auditor progress and conductor
independent Euler-factor calculation agreed on the double-pole failure;
the conductor sent the fixed-damping qualification before final reports.
The current primary theorem text was opened directly at the link above.
Accepted r2, mollifier and full-wave conventions are from
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md and
proofs/kernels/gc_complete_distinct_radical_moment_reduction.md.
Starting graph SHA256:
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
Final dependency hashes will be bound in the independent application review
and round reconciliation. This artifact itself proposes no graph mutation.

## 7. Recommended state effect

Retain only after independent review as a scoped source/transfer control.
No pointwise, moment, M1/M2/GAR or endpoint estimate is promoted. Do not
equate a logarithmic improvement with the fixed missing power, or this
absolute certificate with an actual signed obstruction. The full quarter
goal and complete analytic frontiers remain open.
