# Round227 conductor Mellin-phase and application control

## 1. Result

The actual scaled Mellin phase has one positive-frequency stationary band
with uniform nonzero curvature in log coordinates. Its weighted absolute
transform mass is at most O(L^(b+1/2)), and that power is attained by a
fixed nonzero interior amplitude. Thus a free bounded Mellin L1 norm is
not available from smoothness alone. This concerns a transform certificate,
not an arithmetic lower bound or a restriction on the signed joint spectral
kernel. No complete estimate improves here.

The joint leading-Stirling phase also has an explicitly computable saddle,
but its use requires distance from the gamma transition. Small shifts can
violate that requirement. An exact kernel representation can retain that
transition; it cannot be replaced by this interior asymptotic without proof.

## 2. Exact hypotheses

For 0<d<3/2, let a_d be smooth, zero extended, supported where
1/2<y-d<2 and 1/2<y<2, with uniformly bounded fixed-order derivatives.
Put f_d(y)=(sqrt(y)-sqrt(y-d))/d, L>=1, and
K_d(L,tau)=integral a_d(y) exp(i[L f_d(y)+tau log y])dy.
All constants depend on finitely many stated amplitude seminorms and
the fixed weight exponent b>=0. An amplitude need not be nonnegative
or nonzero. No uniform lower bound is asserted for all these amplitudes.

For the arithmetic application d=h/N, L=2pi R h/sqrt(N), y=(x+h)/N.
All actual nonempty overlaps have y,y-d in(1/2,2). For fixed sigma,
a_d(y)=g_N(Ny)g_N(Ny-h)y^(sigma-1), with all seminorms O(A_J^2).
No arithmetic coefficient, source theorem or contour is absorbed into it.

## 3. Independent derivation and application

Set u=sqrt(1-d/y); on every overlap, 1/2<u<1. Rationalization gives
f_d(y)=1/(sqrt(y)+sqrt(y-d)). If g_d(y)=-y f_d'(y), then directly
\[
g_d(y)=\frac1{2\sqrt y\,u(1+u)},\qquad
g_d'(y)=-\frac{1+u-u^2}{4y^{3/2}u^3(1+u)}.              \tag{1}
\]
Thus g_d is positive, strictly decreasing, bounded above and below by
fixed positive constants; so is -g_d'. These statements extend uniformly
to d=0, where f_0=1/(2sqrt(y)), g_0=1/(4sqrt(y)).

Use v=log y and F_d(v)=f_d(exp v), b_d(v)=exp(v)a_d(exp v).
The full phase is L F_d(v)+tau v. Its second derivative is
\[
L F_d''(v)=-L y g_d'(y)\asymp L>0.                    \tag{2}
\]
It is independent of tau. The stationary equation is tau/L=g_d(y).
It has at most one solution and only for positive tau~L. Van der
Corput's second-derivative estimate with amplitude of bounded variation
gives |K_d|<=C L^-1/2 uniformly in tau and d, including shrinking support.
There is no invocation of an interior expansion at a moving endpoint.
Outside a fixed positive interval cL<=tau<=CL containing every possible
stationary value, phase differentiation gives arbitrarily rapid decay
O_M((L+|tau|)^-M); successive derivatives of the phase are O(L) and the
first derivative has magnitude comparable to L+|tau|. Smooth zero
extension kills boundary terms. In particular tau=0 is nonstationary.

One may also obtain the entire weighted L1 estimate directly from
Plancherel. The log-coordinate amplitude has L2 norm O(1); each fixed
k-th derivative of b_d exp(i L F_d) has L2 norm O(L^k). Cauchy on
|tau|<=L gives O(L^(b+1/2)). On a dyadic outer annulus |tau|~S>=L,
weighted Plancherel and Cauchy give O(L^k S^(b+1/2-k)). Choose integer
k>b+1/2 and sum. Consequently
\[
\int_{\mathbb R}(1+|\tau|)^b |K_d(L,\tau)|\,d\tau
\ll_b L^{b+1/2}.                                     \tag{3}
\]

For the matching power fix d=d0 in(0,3/2), a fixed amplitude nonzero
on a compact interior interval, and nu in a compact subinterval of its
stationary image. The unique point y_nu solves g_d0(y_nu)=nu. The
ordinary interior stationary-phase formula, derivable by the quadratic
change of variable at the unique critical point, gives uniformly there
\[
K_{d0}(L,L\nu)=
a_{d0}(y_\nu)\left(\frac{2\pi y_\nu}{L[-g_{d0}'(y_\nu)]}\right)^{1/2}
\exp\{iL[f_{d0}(y_\nu)+\nu\log y_\nu]+i\pi/4\}
+O(L^{-3/2}).                                        \tag{4}
\]
The smooth compact amplitude may be complex. By choosing the subinterval
so its modulus is bounded below, (4) proves a lower mass c_b L^(b+1/2).
The leading reduced phase F(nu) has F'(nu)=log y_nu and
F''(nu)=1/(y_nu g_d0'(y_nu))<0. An amplitude vanishing on that interval,
an empty amplitude or shrinking supports need not have such a lower bound.

For the actual q_h(y)=W_h(Ny-h), its Mellin transform on sigma+i tau
is exactly K_d with the amplitude stated in Section2. Fixed sigma and
Schwartz seminorms give
\[
\int(1+|\tau|)^b|\widehat q_h(\sigma+i\tau)|d\tau
\ll A_J^2(1+Rh/\sqrt N)^{b+1/2}.                     \tag{5}
\]
At N<=P<2T^(3/2), the smallest positive shift already has L>>T^(1/4)
at large T. Bounded T is absorbed by fixed constants. All h with an
empty continuous overlap have q_h=0. A discrete-empty overlap is not
silently assigned zero q_h. There is no sharp mask in this assertion.

The inverse Mellin/Fourier integral recombines these phases exactly;
its absolute mass is not the value of that recombination. Consequently
(3)--(5) do not bound the actual wave from below, nor the norm of every
possible joint spectral transform. They explain one cost discarded by a
free fixed-test import, while leaving signed spectral cancellation open.

For an additional scoped check, write lambda=2pi R sqrt(N). In the
HKLDW gamma quotient, on an interior region tau>t>0 with tau-t large,
the leading Stirling phase of the full y,tau integrand is
\[
\Phi=\lambda(\sqrt y-\sqrt{y-d})+\tau\log(y/d)
+(\tau+t)\log(\tau+t)+(\tau-t)\log(\tau-t)-2\tau\log\tau.
                                                               \tag{6}
\]
The prefactor (N/h)^(i tau) is included in log(y/d). The stationary
equations in y,tau give, by differentiating (6),
\[
\frac t\tau=\sqrt{1-d/y}=u,\qquad
t=\frac\lambda2(\sqrt y-\sqrt{y-d}),\qquad
\Phi_{\rm crit}=2t+t\log\frac{\pi^2R^2h}{t^2}.        \tag{7}
\]
Indeed the tau equation says (y/d)(1-t^2/tau^2)=1; the y equation
then fixes t. The ratio (1+u)/(1-u)=pi^2 R^2 h/t^2 determines the
last expression. These are algebraic facts about the leading phase,
not a justified asymptotic for the full spectral sum.

At that saddle, tau~Rh/sqrt(N), while
\[
\tau-t\asymp Rh^2/N^{3/2}.                            \tag{8}
\]
Thus separate large-argument Stirling for both numerator gammas is not
uniform for h on or below N^(3/4)R^-1/2. This is a possible full-range
transition, not an omitted exception. Formula(7) can help identify a
signed kernel only when an exact or uniform representation owns it.
No contour shift or spectral tail theorem is proved by (6)--(8).

## 4. First doubtful or unproved step

The source coefficient and full all-shift spectral pairing are untouched
by these elementary phase bounds. The first required analytical gain
remains the complete signed remainder(F). Using an absolute Mellin
envelope or the interior saddle alone does not establish it. A proposed
uniform large-sieve application must also handle coefficients depending
on the spectral parameter and the actual source normalizations.

## 5. Controls and outcome

Zero amplitude, tau=0, d->0, shrinking overlap, stationary point crossing
a cutoff, fixed nonvanishing interior example, sign of frequency and
quadratic phase constant all checked analytically. The actual amplitude
keeps Psi signs and all scaled derivatives. Discrete-empty and continuous-
empty overlaps are distinguished. All tails and the sharp quarter bridge
remain those in the frozen complete packet; no new full exponent follows.
The isolated derivation and a separate nonauthor application review are
required before closure. Mathematical experiments: zero.

## 6. Dependencies and provenance

Conductor, NONBLIND, Round227. This control was derived before reading
the isolated report; only its progress synopsis was received, after the
independent curvature calculation. Inputs: protocol, graph/manifest,
strategy227, complete interface and isolated statement, closed226 report
and checkpoint, accepted204 bridge. The gamma quotient is the exact
HKLDW1705.04771v3 equation(3.10), already source-audited in226; its
leading phase is derived here, not a new external theorem import.
Graph SHA256 a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
No current sibling report or source-role derivation was used to establish
(1)--(5). Source-role correspondence independently agreed with (7).

## 7. Recommended state effect

Retain as scoped phase/application evidence after independent review.
No graph promotion or proof-draft update, no complete gain and no actual
signed lower bound. The important full joint spectral kernel remains
eligible for a stronger estimate retaining its oscillation.
