# 1. Result

Round228, campaign `gc-signed-heegner-phase`, task
`signed_hecke_functional_attack`; temporary discovery role, NONBLIND.
Generated 2026-09-28. Starting graph SHA256:
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
Candidate evidence only.

The resonant Hecke functional equation does shorten the shift polynomial,
but does **not** give a complete signed bound in this attempt. Its correct
dual scale for a descendant of length L and spectral height t is

\[
 K={q t\over \pi^2L},                                      \tag{1}
\]

with primitive conductor q=1 or 2. It is not q t^2/L. The small gamma
factor remains a cosine transform. The large gamma phase combines with
the original common phase to give

\[
 e^{-i\pi/4}(q d R^2/n)^{it},\qquad h=dm.                  \tag{2}
\]

Thus a signed spectral wave remains after the functional equation.
Discarding that phase and using the previously audited point fourth
moment and individual Hecke second moment produces no bound better than
the original coefficient cap, even after every descendant is summed.

There is a useful exact simplification at the actual CM points. Only even
reflection parity survives at both points; only Fricke-plus survives at
level two. The level-one oldspace at level two contributes the explicit
factor

\[
 {2\over 3+\sqrt2\lambda_f(2)}|u_f(i)|^2.                  \tag{3}
\]

It cannot be omitted or replaced by 1. The surviving primitive functional
equations have root number +1. These facts, the exact dual transform, and
the complete upper-cost ledger below are the report's limited conclusions.
The whole actual signed target remains open; no impossibility theorem or
actual arithmetic lower bound is claimed.

# 2. Exact statement and hypotheses

Use the frozen actual signed g_N, r_2, W_h, rho_h and I_h without change.
Thus T>=2, cT<=R<=CT is every real radius, N is every dyadic integer
2<=N<=P<2T^(3/2), and A=(1+N/T)^(-J). Smooth zero extension gives
support N/2<x<2N and every fixed scaled derivative O(A). Put

\[
 \alpha_h=1-h/(2N),\quad
 H_h(t)=4\pi\int_0^\infty W_h(hu)
                    P_{-1/2+it}(1+2u)\,du.
\]

Let V_q(j)=sum_(h<2N) alpha_h L_(q,h)(j) H_h(t_j), with the exact
two-adic polynomials of the complete interface. Define the ENTIRE cusp
and continuous partners by

\[
 \mathcal C=\sum_{q=1,2}\sum_{j\ne0}|u_j(z_q)|^2V_q(j),
\quad
 \mathcal E={1\over4\pi}\sum_{q=1,2}\sum_{\mathfrak a}
 \int_{\mathbb R}|E_{\mathfrak a}(z_q,\tfrac12+it)|^2
                       V_q^{\rm cts}(t)\,dt,             \tag{4}
\]

where z_1=i, z_2=(-1+i)/2, and there are one plus two continuous cusps.
All functions use hyperbolic-area normalization. The frozen full target is

\[
 2\Re(\mathcal C+\mathcal E)
       \ll_{\epsilon,J} A^2N^{3/2}T^\epsilon.              \tag{5}
\]

The density is already subtracted exactly, and the zero atom vanishes.
This report owns the complete cusp attempt. A sufficient separate-partner
closure would bound both 2 Re C and 2 Re E above by the RHS of (5), or
bound their moduli by that quantity. Separate modulus bounds are stronger
than (5), and are not necessary: cross-component cancellation is allowed.
No conclusion about the other owner's current report is presumed.

For the functional-equation lemma, f is a primitive weight-zero Maaß
cusp form of trivial character and conductor q=1 or 2, with spectral
parameter t>0, reflection parity delta=0 or 1, and Fricke eigenvalue w_f.
Its normalized Fourier coefficients are lambda_f(n), lambda_f(1)=1.
All actual surviving modes below have delta=0, w_f=+1. Oldforms are first
resolved into their conductor-one primitive representation. Finite low
and exceptional spectrum is retained and paid by the exact kernel tails;
the large-t expansions are never applied to it.

The only external inequalities reused are the already audited AH
Theorem1.2 at the two fixed level/point pairs and its equation(8) at the
actual Hecke indices. In area normalization they give respectively a
point fourth-moment O(U^(2+epsilon)) and individual Hecke second-moment
O((mU)^epsilon(U^2+sqrt(m))). The probability-to-area constants are the
fixed volumes pi/3 and pi from closed227. The literal defective collective
sieve and printed mean-square exponent are not used. The exact-version
primary is [Assing--Humphries2607.13518v1](https://arxiv.org/html/2607.13518v1).
No additional primary work or theorem is imported: the functional equation
and local factors used here are derived below.

# 3. Derivation and full cost accounting

## 3.1 Reflection, Fricke, primitive conductor and oldspace

Let Jz=-conjugate(z). We have Ji=i and Jz_2=z_2+1. Translation by 1
belongs to both groups. Hence a reflection-odd eigenfunction has zero
value at either relevant point. Choose the bases simultaneously with
reflection and, at level two, Fricke; these commute with the odd Hecke
operators occurring there. Also

\[
 W_2z_2=-1/(2z_2)=(1+i)/2=z_2+1.
\]

Therefore a Fricke-minus level-two form vanishes at z_2. This is a point
identity, not a root-number cancellation guessed from class number one.

For a level-one area-normalized primitive u, let F(z)=u(z), G(z)=u(2z)
on Gamma_0(2). Their Gram matrix is

\[
 \begin{pmatrix}3&\sqrt2\lambda_u(2)\\
                 \sqrt2\lambda_u(2)&3\end{pmatrix}.      \tag{6}
\]

Indeed, the index is 3, W_2 interchanges F and G, and tracing G to level
one gives u(2z)+u(z/2)+u((z+1)/2)=sqrt(2) T_2u. This proves both norms
and the cross term. At z_2, F(z_2)=G(z_2)=u(i): the first equality uses
z_2=gamma_0 i with gamma_0 in SL_2(Z), and the second uses
2z_2=-1+i. Thus the normalized plus vector has squared point value (3),
and the minus vector has value zero. The Gram denominator is positive.
The already available bound |lambda_u(2)|<=2^theta+2^(-theta), theta<1/2,
keeps it bounded above and away from zero uniformly. Indeed
sqrt(2)(2^theta+2^(-theta))<3. No varying-level factor is hidden here.

Consequently the exact cusp contribution can be regrouped as

\[
 \begin{split}
 \mathcal C={}&\sum_{f\ {\rm level}\ 1,\ {\rm even}}
 |u_f(i)|^2\left(V_{1,f}+
       {2V_{2,f}^{\rm odd}\over3+\sqrt2\lambda_f(2)}\right)\\
 &+\sum_{f\ {\rm new}\ 2,\ {\rm even},\ W_2=+1}
 |u_f(z_2)|^2 V_{2,f}^{\rm odd}.                          \tag{7}
 \end{split}
\]

This preserves all modes, with identically zero modes removed by proof.
For the second sum, lambda_f(2)=-1/sqrt(2). To check the local sign,
the trace of a newform to level one is zero. Coset representatives
I,S,ST give trace(f)=f+w_f sqrt(2)U_2 f, hence
lambda_f(2)=-w_f/sqrt(2). This also gives the ramified Euler factor.

For completeness the functional equation can be obtained directly.
For even f, its Fourier expansion gives

\[
 \int_0^\infty f(iy)y^{s-3/2}\,dy
 ={\rho_f(1)\over2}\pi^{-s}
 \Gamma((s+it)/2)\Gamma((s-it)/2)L(s,f).
\]

Here the Mellin integral of K_it is evaluated by its elementary integral
representation and a gamma integral. Substituting y=1/(qv) and using
Fricke gives the completed equation

\[
 \Lambda(s,f)=\epsilon_f\Lambda(1-s,f),\quad
 \Lambda(s,f)=q^{s/2}\pi^{-s}
 \Gamma((s+\delta+it)/2)\Gamma((s+\delta-it)/2)L(s,f),
 \quad \epsilon_f=(-1)^\delta w_f.                       \tag{8}
\]

For odd f use the x derivative on the imaginary axis; differentiating
Fricke supplies the minus sign. Only the even calculation is needed in
(7). Cusp decay at both ends makes the completed Mellin integral entire,
and supplies the usual contour shifts. Thus all surviving primitive
signs in (8) are +1; their conductors remain respectively 1 and 2.

## 3.2 Exact descendant reorganization and odd local factors

The level-one polynomial can be regrouped without approximation as

\[
 V_{1,f}=4\sum_{a\ge0}(-1)^a\sum_{m\ge1}
       \alpha_{dm}\sqrt m\lambda_f(m)H_{dm}(t_f),
 \qquad d=2^{a+2},\quad dm<2N.                           \tag{9}
\]

The level-two polynomial is

\[
 V_{2,f}^{\rm odd}=2\sum_{k\ge0}\varepsilon_k
       \sum_{m\ge1,\ m\ {\rm odd}}
       \alpha_{dm}\sqrt m\lambda_f(m)H_{dm}(t_f),
 \qquad d=2^k,\quad dm<2N.                              \tag{10}
\]

All sums in d are finite. No descendant has acquired a new H_h.
For conductor one,
L^(2)(s,f)=(1-lambda_f(2)2^(-s)+2^(-2s))L(s,f);
for conductor two it is (1-lambda_f(2)2^(-s))L(s,f).
Equivalently, for any smooth compact F,

\[
 \sum_{m\ {\rm odd}}\lambda_f(m)F(m)=
 \sum_m\lambda_f(m)\{F(m)-\lambda_f(2)F(2m)
                         +{\bf1}_{q=1}F(4m)\}.         \tag{11}
\]

This follows coefficientwise from the prime-two Hecke recurrence;
at conductor two the recurrence is geometric. Therefore every odd
restriction becomes at most three full primitive sums with lengths
L, L/2, L/4 and the displayed bounded local factors. The phases 2^(it)
or 4^(it), and sqrt(2) or 2 from any sqrt(m) in F, are retained inside
F(2m) or F(4m). No fictitious conductor-two functional equation is
applied to a conductor-one oldform.

## 3.3 Exact resonant transform

Let a be smooth, supported in a fixed compact subinterval of (0,infinity),
with fixed derivative bounds, and define
S_f(L,t;a)=sum_m lambda_f(m)m^(it)a(m/L). Its Mellin transform is
a-hat(s)=integral a(y)y^(s-1)dy. Mellin inversion, (8), and a shift to a
fixed negative real part -B give the exact formula

\[
 S_f(L,t;a)=\epsilon_f(q/\pi^2)^{1/2+it}
 \sum_{n\ge1}{\lambda_f(n)\over n^{1+it}}
 {1\over2\pi i}\int_{(-B)}\widehat a(s)
       (\pi^2Ln/q)^s\,G_\delta(s,t)\,ds,                \tag{12}
\]

where

\[
 G_\delta(s,t)=
 {\Gamma((1+\delta-s+2it)/2)\Gamma((1+\delta-s)/2)
  \over
  \Gamma((\delta+s)/2)\Gamma((\delta+s-2it)/2)}.         \tag{13}
\]

Take B a positive nonintegral constant large enough for the dual series.
Initially the original Dirichlet series is used on Re s>1. The shifted
L(s-it,f) is entire; thus the shift has no residues. Expand the dual
series only after reaching Re(1-s+it)>1. Formula (12), not a sharply
truncated dual polynomial, defines the exact transform. Arbitrary fixed
decay orders follow by taking B larger.

Here are explicit transition checks without using a hidden interior
Stirling approximation. Write s=sigma+iv, with sigma a fixed line on
which numerator gamma factors have no poles. Gamma modulus estimates
give the full-axis envelope

\[
 |G_\delta(\sigma+iv,t)|\ll_\sigma
 [(1+|v|)(1+|v-2t|)]^{1/2-\sigma}.                     \tag{14}
\]

Reciprocal gamma zeros can make the left side smaller; no lower envelope
is asserted on such lines. On sigma=1/2 the numerator factors are the
complex conjugates of the denominator factors, so the modulus is exactly
1 for every real v,t. Both transitions v=0 and v=2t are therefore regular
in the exact ratio. Neither supplies exponential suppression.

For |v|<=t^kappa, any fixed kappa<1/2, apply Stirling only to the pair
whose arguments have imaginary part approximately t. For delta=0,

\[
 G_0(s,t)=t^{1/2-s}
 e^{i\{2t(\log t-1)-\pi/4\}}
 {\Gamma((1-s)/2)\over\Gamma(s/2)}
 \left(1+O_\sigma((1+|v|)^2/t)\right).                 \tag{15}
\]

There is an arbitrary fixed-order expansion with polynomial-in-s
coefficients and fixed-order derivative control on a smaller such
window. This follows by Taylor expanding the logarithmic Stirling
series at t-v/2; its linear v term is -v log t, exactly the t^(-s)
factor. The constant phase is -pi/4, because the two real gamma
arguments sum to 1/2. For parity delta the constant is delta*pi/2-pi/4.
The small gamma quotient is retained exactly, including v=0. On the
complementary v range use (14) and the arbitrarily rapid Mellin decay
of a, rather than (15). This pays in particular the other transition
v approximately 2t.

The remaining gamma quotient is a cosine transform. Precisely, on a
valid initial strip and then by Mellin continuation,

\[
 {\Gamma((1-s)/2)\over\Gamma(s/2)}
 ={2\over\sqrt\pi}\int_0^\infty\cos(2y)y^{-s}\,dy.
\]

Therefore, writing C_a(x)=integral_0^infinity a(y)cos(2xy)dy, the leading
term of (12) is

\[
 \epsilon_f e^{i\{2t(\log t-1)-\pi/4\}}
 (q/\pi^2)^{it}{2\sqrt\pi L\over\sqrt{qt}}
 \sum_{n\ge1}\lambda_f(n)n^{-it}
 C_a\left({\pi^2Ln\over qt}\right).                    \tag{16}
\]

The factor 2 sqrt(pi) follows also from
integral cos(2y)y^(-s)dy=(sqrt(pi)/2)Gamma((1-s)/2)/Gamma(s/2).
Every fixed correction to (16) has the same dual scale (1), a fixed
finite combination of derivatives of this transform, and its explicit
inverse powers of t. Smooth compact support gives arbitrarily rapid
decay when n/K is large, not compact dual support. The exact formula
(12) retains all corrections and the entire dual tail. Bounds following
from the expansion use enough fixed terms and derivatives for a chosen
error O(T^(-D)); the finite parameter ranges make that choice uniform.

## 3.4 Application to the actual stationary symbol and its surviving phase

Split the h sum smoothly into h comparable to M. The exact kernel tails
from closed227 leave t comparable to U=TM/sqrt(N), with U bounded below
by a constant times T^(1/4), and O(A^2T^(-D)) after all modes and shifts
are summed. At h=dm the m length is L=M/d. The stationary phase is

\[
 \Phi(t)+t\log h,\qquad
 \Phi(t)=2t(1+\log(\pi R/t)).                           \tag{17}
\]

After factoring exp(i Phi(t))d^(it)m^(it), the stationary amplitude for
sqrt(m) alpha_(dm) H_(dm)(t) has fixed scaled m derivatives bounded by

\[
 c_{d,U}=O\left({A^2\sqrt N\over U\sqrt d}\right).       \tag{18}
\]

Here is why this is a valid symbol assertion, rather than a replacement
of the exact transform by its leading value. In hyperbolic coordinates,
the sole stationary point satisfies
x_* = pi^2 R^2 h^2/(4t^2)-h/2+t^2/(4pi^2 R^2).
On an enlarged stationary band, scaled h derivatives of x_* and x_*+h
are O(N); hence the fixed derivatives of their g factors are O(A).
The curvature is t/2. The uniform r-symbol and parameter stationary
phase expansion thus have (18) at every fixed order. Smooth zero
extension covers a stationary point meeting the support edge. Outside
a padded stationary region, integration by parts gives any inverse
power of U, also after any fixed h derivatives. A sufficiently long
finite expansion plus its exact remainder therefore yields (18) for
the retained symbols and an arbitrarily small fully summed error.
Alternatively the exact weight can be left in (12) throughout.

Insert (16) into (17). The two t log t phases cancel, but the phase does
not disappear:

\[
 e^{i\Phi(t)}d^{it}e^{i\{2t(\log t-1)-\pi/4\}}
       (q/\pi^2)^{it}n^{-it}
   =e^{-i\pi/4}(q d R^2/n)^{it}.                       \tag{19}
\]

Local terms F(ell m) in (11) make d become d ell in this formula, with
the corresponding bounded local multipliers and length L/ell. Every
parity sign remains. For every descendant the dual length is

\[
 K\asymp {qU\over L}\asymp {qTd\over\sqrt N};          \tag{20}
\]

thus deep descendants have longer dual vectors and are not assigned
the d=1 length. Formula (19) has a large spectral frequency on the
effective dual support: qdR^2/n is comparable to R sqrt(N). It is not
legitimate to integrate by parts in t over a discrete spectrum. Neither
pointwise bounds nor a positive spectral moment see this phase.

## 3.5 A fully paid positive price for the transformed cusp component

This subsection deliberately discards the signed phase only after (19),
to test whether the shortening alone suffices. It does not assert a
lower bound. For a mode t comparable to U, a transformed coefficient has
envelope, for any fixed B,

\[
 O_B\left(c_{d,U}{L\over\sqrt U}
                     (1+n/K)^{-B}\right).              \tag{21}
\]

All q and local-ell constants are bounded. The envelope includes fixed
corrections and paid remainders. Although the coefficients depend on t,
the per-coefficient envelope permits Minkowski with the individual Hecke
second moment; no fixed-coefficient sieve is invoked. On the effective
support K=O(U), since L is bounded below whenever an integer contributes.
Thus U^2 dominates sqrt(n) there. The polynomially weighted dual tail is
summable by increasing B. The resulting vector norm and point pairing
are bounded by

\[
 \|V_{d,M,U}\|_2\ll T^\epsilon U c_{d,U}{L\over\sqrt U}K
       \ll T^\epsilon c_{d,U}U^{3/2},
\]
\[
 \left|\sum_{t_f\asymp U}|u_f(z_q)|^2V_{d,M,U}(f)\right|
 \ll T^\epsilon c_{d,U}U^{5/2}
 \ll A^2T^\epsilon {\sqrt N U^{3/2}\over\sqrt d}.       \tag{22}
\]

The extra U in the second line is exactly the square root of the point
fourth moment. The oldspace factor (3) is bounded, and a conductor-two
primitive Hecke second moment at even n follows from its fixed geometric
two-factor and the odd-index moment. Conductor-one terms use their own
level-one second moment. This justifies (22) for the precise basis (7).

Sum d over its actual powers of two: sum d^(-1/2) is bounded. Sum all
shift dyads M<=O(N), with U comparable to TM/sqrt(N), and pay all original
spectral tails. The complete cusp upper certificate furnished by this
procedure is

\[
 |\mathcal C|\ll_{\epsilon,J}
       A^2T^{3/2+\epsilon}N^{5/4}.                      \tag{23}
\]

One can also retain the older complete cusp price A^2 T N^2 and take
their minimum. Even (23) exceeds the full arithmetic cap A^2N^2
throughout N<=2T^(3/2), up to harmless bounded small parameters: their
ratio is T^(3/2)N^(-3/4), at least a constant times T^(3/8).
At N comparable to T, (23) is A^2T^(11/4), while the quarter raw target
is A^2T^(3/2), and the full arithmetic cap is A^2T^2. This comparison
does not use the full arithmetic cap as a bound for the cusp partner
alone. It compares the attempted complete route after its independent
partners are restored. The shorter dual length by itself proves no gain.

## 3.6 Pretrace return and complete physical reconstruction

Returning the complete spectrum in (4) to the geometric side simply
inverts the same smooth radial pretrace identity used to obtain it.
Then applying the determinant bijection and the parity recurrence of
closed227 gives exactly sum_h alpha_h(C_h-rho_h I_h). The test is still
g(x+h)g(x)e(R(sqrt(x+h)-sqrt(x))); neither oscillation nor subtraction
has disappeared. The functional equation is invertible as well.
Therefore a formal return through these identities, without a new bound
for that oscillatory kernel or orbit sum, is a reconstruction of the
original circle-wave problem. This conclusion concerns the named
identity-only operation, not all possible geometric estimates.

The existing entire continuous price from closed227 is A^2 T N^2, with
all three cusps. This report does not improve it. A separate proof paying
the ENTIRE continuous partner at A^2N^(3/2) still leaves the ENTIRE cusp
inequality of Section4. No local or partial component closes (5).

The valid full fallback remains A^2N^(2+epsilon) for (5)'s left side in
modulus, obtained from the actual coefficients and the already paid
density. In Fejer, the diagonal is A^2N^(1+epsilon), the density costs
A^2N^(3/2+epsilon)/T times a logarithm, the exact multiplier is bounded,
and normalization divides the square by N^(3/2). Hence the fallback
shell is O(A N^(1/4+epsilon)). Sum every dyadic shell, the O(1) singleton,
and the arbitrarily small original Schwartz tail beyond P. This gives
only complete complex T^(1/4+epsilon), physical exponent 3/8, weaker
than the prior complete complex13/56 cap and the inherited complete
REAL beta=2 theta_LY-1/2. The latter remains a bound for the whole real
wave only. No block or complex use of beta is made.

# 4. First doubtful or unproved step

After the exact reductions and paid tails, the missing arithmetic
estimate is still (5). If the separately owned entire continuous
component is paid at the target, a sufficient remaining complete task is

\[
 2\Re\left[
 \sum_{f\ {\rm level}\ 1,\ {\rm even}}|u_f(i)|^2
 \left(V_{1,f}+{2V_{2,f}^{\rm odd}\over3+\sqrt2\lambda_f(2)}\right)
 +\sum_{f\ {\rm new}\ 2,\ {\rm even},\ W_2=+1}
 |u_f(z_2)|^2V_{2,f}^{\rm odd}\right]
 \ll A^2N^{3/2}T^\epsilon.                              \tag{24}
\]

Every h, d, spectral mode and tail is in these exact V's. Equivalently,
one can retain their exact dual transforms (12), with phase (19), all
local terms (11), and all correction transforms. The first unavailable
step would be to assign useful cancellation to this actual signed
spectral pairing. A smooth common phase is not enough for a sum over
discrete spectral parameters, and a formal length K is not a norm bound.

Equation (23) is an upper certificate from a specific positive procedure,
not a necessary size. At N=T it misses (24) by T^(5/4); the original full
coefficient cap misses (5) by T^(1/2). A complete complex wave exponent
gamma requires replacing the raw quarter RHS by its multiple T^(2gamma).
To improve the inherited real benchmark by this sufficient complex route
requires gamma<beta. This attempt supplies neither such a gain nor a
counterexample. No hidden complementary range is claimed to be solved.

# 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| actual_full_target | Exact whole C+E in (4)--(5); original signed g and r_2 retained. No substitute coefficients. |
| all_shifts_parity_and_scales | Exact d,m reorganizations (9)--(11), all h<2N and N<=P; every d has its own dual length. |
| signed_joint_phase_before_norms | Original h^(it) and common phase combine as (19); discarded only in the explicitly priced certificate (22). |
| source_and_functional_equation_hypotheses | Primitive q=1/2, trivial character, parity and Fricke checked; FE derived from Fourier Mellin; no additional source theorem. |
| complete_discrete_and_continuous_spectra | Basis identity (7) preserves every nonzero cusp mode; all three continuous cusps stay in (4), with their entire independent owner. |
| gamma_transitions_and_dual_lengths | Exact ratio (13), both centers in (14), modulus1 at sigma=1/2, small gamma retained; K=q t/(pi^2 L), full tails. |
| literal_endpoints_and_tails | Smooth zero extension, exact Fejer weight, vanishing zero atom, original full spectral and Schwartz tails retained. Discrete-empty overlap does not delete continuous density. |
| real_complex_scope | No inherited beta for complex blocks; the sufficient complex route and whole real benchmark remain distinct. |
| full_power_restoration | Complete cusp price (23), complete partner statement (24), entire arithmetic cap and Fejer normalization restored. |
| certificate_not_actual_lower_bound | All failed prices are upper-procedure costs; no arithmetic or vector lower bound is inferred. |
| statement_only_control | NONBLIND role; no current sibling, blind packet/report, or root control read. Independent isolated gamma review remains conductor-owned. |
| fixed_order_full_goal | No new moment claim. Both accepted distribution terms remain; quarter still needs the full wave or adequate unbounded fixed even orders. |

Additional exact controls: at level two W_2z_2=z_2+1, and the oldspace
minus value is identically zero; the plus denominator in (3) comes from
the entire Gram matrix. At t-resonance v=0, (15) keeps the finite small
gamma factor; at sigma=1/2 its modulus is1. Composing (8) twice restores
the original L-function since epsilon_f^2=1 and the gamma/conductor
ratios are reciprocal. Applying the pretrace inverse restores the
original arithmetic functional. None of these controls is an experiment.

Zero numerical or symbolic experiments; analytical/algebraic effort
exceeds95 percent. No source typo is repaired, and no extra primary work
is introduced.

# 6. Dependencies and exact provenance

Read the protocol and assigned brief, then only permitted context:

* `state/proof_obligations.yml` (authority and relevant complete-wave/frontier entries), `state/active_campaign.yml`.
* `strategy/round228_signed_heegner_phase.md`.
* `strategy/gauss_circle_strategy_review_2026-09-23.md` and `strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md`.
* Current `briefs/complete_signed_heegner_interface.md` and closed227 `briefs/complete_joint_spectral_interface.md`.
* Closed227 `reports/heegner_joint_norm_audit.md`, `reviews/independent_heegner_norm_review.md`, `reports/joint_shift_spectral_attack.md`, `reviews/independent_spectral_attack_review.md`, and `synthesis.md`.
* `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` for preserved full-wave and fixed-moment scope.

The closed227 exact Heegner report is bound in its review to SHA256
`cc921c6d04fb7015e68915000badffa82ff284734460e0be57b2260197443909`;
its independent spectral report is bound to
`9df8afa574a54a6d9c7ca587030aeaec00a7daa345594d224116a93e823d3560`.
Their exact arbitrary-test bridge and scalar tail bounds are the inherited
premises here; none of their unproved norm closures is assumed.

The only direct primary reinspection was the already permitted
[AH2607.13518v1](https://arxiv.org/html/2607.13518v1), for its normalization
and the two stated moment inequalities. No new primary work was needed.
The new reflection, Fricke, trace, oldspace, Mellin, gamma and transform
calculations in this report are analytical derivations, pending nonauthor
review. No current sibling or blind result was used. The conductor was
sent two substantive progress messages describing the CM simplification
and the resonant length/phase. Two conductor steering messages then
required full dual tails, the complete positive norm ledger, explicit
Euler-two depletion and surviving geometric scope; these are implemented
above. The conductor reported agreement with its own gamma calculation
without supplying that control or any blind report. The continuous
owner's work was described as pending; no result from it was supplied.

Provenance repair after initial freeze: replaced unintended standalone carriage-return bytes in LaTeX roman-type commands with literal \rm commands. This byte-only formatting repair changes no mathematical content or source dependency.

Only this assigned report was written. Shared graph, draft, matrices,
synthesis, old rounds and legacy directories were not changed.

# 7. Recommended state effect and stopping rule

**Retain** the exact CM/oldspace simplification, resonant functional
equation, transformed phase and limited certificate assessment as candidate
evidence after the required seam review. **No change** to accepted graph,
proof draft, complete exponents, moments or quarter status.

Exit label: `complete_signed_heegner_no_new_bound`. The exact first
unproved complete inequality is (5), with (24) the entire remaining
cuspidal partner if the other entire partner is paid. No successor task
is proposed or started. Freeze at the externally recorded SHA256 and
stop; only the conductor assesses and closes Round228.
