# 1. Result: complete spectral interface, no complete gain

Round227, campaign `gc-complete-joint-spectral-remainder`; task
`joint_shift_spectral_attack`; discovery, NONBLIND. Generated
2026-09-28T07:33:02+08:00. Starting graph SHA256:
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

The complete signed inequality (F) remains unproved. I obtain an exact
ordered spectral representation with a quantitative finite-contour
approximation, keeping every positive shift, the zero atom, the density,
the cuspidal spectrum and all three continuous cusps. I also derive the
inverse gamma kernel and its actual joint phase. That kernel is a
Legendre transform, and its stationary phase is

\[
 t=\pi R(\sqrt{x+h}-\sqrt x),\qquad
 \Phi_*(t,h)=2t+t\log(\pi^2R^2h/t^2).                 \tag{1}
\]

The exact transform treats the small-shift gamma transition uniformly;
an interior Stirling calculation alone would not. It does **not** prove
cancellation of the spectral coefficients or of the complete h sum.

A second seam must be made explicit: ordinary square integrability of
the regularized theta function controls its unweighted spectral
coefficients, whereas the Legendre representation uses exponentially
renormalized coefficients. This audit does not prove their required
joint bound or justify reversing the two limiting operations merely
from L2. The safe finite-contour formula below needs no such reversal.
Its first missing estimate is (25), for the entire expression, not for
a selected h or spectral range.

The completely justified coefficient fallback is a raw remainder upper
bound O(A_J^2 N^(2+epsilon)); (F) requests N^(3/2). At N comparable to T
the missing raw saving is T^(1/2), corresponding to T^(1/4) in the
complex wave. This fallback restores physical exponent 3/8, and is
weaker than the inherited complete REAL exponent theta_LY. Nothing
here is an actual-value lower bound, a disproof of (F), or a new
complete analytic bound. The full quarter goal remains open.

# 2. Exact statement and hypotheses

Use exactly the complete interface packet. Thus T>=2, cT<=R<=CT is
arbitrary real, P is the smallest dyadic integer at least T^(3/2),
2<=N<=P is dyadic, H=2N, and

\[
 g(x)=(x/N)^{-3/4}\Psi(\sqrt{x/T})w(x/N),\quad
 A=A_J(N)=(1+N/T)^{-J},\quad b_h=1-h/(2N).
\]

The fixed real Schwartz function Psi is the actual radial Fourier
transform; it may change sign. Smooth zero extension gives support
N/2<x<2N and fixed scaled derivative bounds O(A). Put

\[
 W_h(x)=g(x+h)g(x)e(R(\sqrt{x+h}-\sqrt x)),
\quad q_h(y)=W_h(Ny-h),
\quad\widehat q_h(s)=\int_0^\infty q_h(y)y^{s-1}dy.
\]

Every positive integer 1<=h<2N is retained. Define

\[
 \rho_h={8\over h}\sum_{d\mid h}(-1)^{h+d}d,
 \quad\mathcal R_h=\sum_{n\ge1}r_2(n+h)r_2(n)W_h(n)
                  -\rho_h\int_0^\infty W_h(x)dx.
                                                               \tag{2}
\]

The full target is

\[
 \mathcal F=2\Re\sum_{h=1}^{2N-1}b_h\mathcal R_h
 \le C_{\epsilon,J}A^2N^{3/2}T^\epsilon.             \tag{F}
\]

HKLDW means the exact version
[1705.04771v3, Sections3 and7](https://arxiv.org/html/1705.04771v3).
Its Fourier convention is
mu_j(z)=sum rho_j(n)sqrt(y)K_(it_j)(2pi|n|y)e(nx), with ordinary
hyperbolic measure, at the fixed level4. Let

\[
 v_j=\langle\mathcal V,\mu_j\rangle,\quad
 v_{\mathfrak a}(t)=
 \langle\mathcal V,E_{\mathfrak a}(\cdot,1/2+it)\rangle,
\]

where V is precisely its Laurent-constant regularization, and the
cusps are infinity,0,1/2. Use the coefficient exactly as printed in
its equation(3.10):

\[
 c_{\mathfrak a,h}(t)=
 {\pi^{1/2+it}h^{it}\over\Gamma(1/2+it)}
 \overline{\varphi_{\mathfrak a h}(1/2-it)}.             \tag{3}
\]

No Heegner value is substituted for v_j. The constant spectral form
has zero pairing with P_h. HKLDW Lemma3.4 supplies the fixed-level
absence of exceptional poles in Re(s)>1/2, not a varying-level rule.

The only additional source audit is HKLDW
[1703.10347v3, Lemma6.1 and its proof](https://arxiv.org/html/1703.10347v3#S6).
The normalized Fourier-coefficient second-moment inequality used in
(20) concerns the same level4 Maaß basis and is independent of the
dimension parameter k. Its separate bound for theta pairings is not
silently specialized from the paper's k>=3 regularization to k=2.
No further source was opened or imported.

# 3. Derivation and complete cost accounting

## 3.1 A safe formula with all contours and spectral components

Set sigma=2; the original Dirichlet series is absolutely convergent
there by r2(n)<<n^epsilon. Mellin inversion and the source expansion
give

\[
 \mathcal R_h={1\over2\pi i}\int_{(2)}
 N^s\widehat q_h(s)
 \left[D_2(s;h)-r_2(h)h^{-s}
             -{\rho_hh^{1-s}\over s-1}\right]ds.       \tag{4}
\]

The density term is its exact Mellin integral on [h,infinity) after
the change m=x+h. It is not just a residue prescription. The atom is
explicitly removed although its full inverse transform is
r2(h)W_h(0)=0. A finitely truncated contour need not have zero atom.

For L>=1 define the finite test

\[
 K_{h,L}(t)={1\over2\pi i}\int_{2-iL}^{2+iL}
 N^s h^{1/2-s}\widehat q_h(s)G(s,it)ds,
\quad G(s,it)={\Gamma(s-1/2+it)\Gamma(s-1/2-it)\over\Gamma(s)^2},
                                                               \tag{5}
\]

and

\[
 Z_L={1\over2\pi i}\int_{2-iL}^{2+iL}
 N^s\sum_{h<2N}b_h\widehat q_h(s)r_2(h)h^{-s}ds.
\]

Then the following is an exact **ordered** identity:

\[
 \mathcal F=2\Re\lim_{L\to\infty}\left\{
 2\pi\sum_j v_j\sum_{h<2N}b_h\rho_j(h)K_{h,L}(t_j)
 +\sum_{\mathfrak a}\int_{\mathbb R}v_{\mathfrak a}(t)
          \sum_{h<2N}b_h c_{\mathfrak a,h}(t)K_{h,L}(t)dt
 - Z_L\right\}.                                      \tag{6}
\]

For each fixed L the spectral sum/integral is taken first. The source
expansion is locally absolutely convergent on this compact contour.
The outer limit follows directly from (4), with the entire arithmetic
bracket, so it does not assume uniform convergence after an exchange
of limits. All h sums in (6) stay inside each spectral pairing.
No contour is moved across a pole. In particular there are no omitted
discrete residues on Re(s)=1/2, no extra continuous residues, and no
unaccounted crossing at s=1: its whole density term was subtracted.

The ordering can be implemented with quantitative tails. Let
Lambda_max=O(R sqrt(N)). Fixed-order integration by parts in log(y)
gives, for any fixed B,

\[
 |\widehat q_h(2+i\tau)|
 \ll_{B,J} A^2(1+Rh/\sqrt N)^B(1+|\tau|)^{-B}.
\]

Moreover |D2(2+i tau;h)|<<_eta h^(-1+eta), after increasing the
constant at h=1. The atom and centered density satisfy the same
adequate envelope. Consequently the omitted Mellin tail in (4),
summed over every h, is

\[
 O_{B,J,\eta}\left(A^2N^{2+\eta}
        (1+\Lambda_{\max})^B L^{1-B}\right).            \tag{7}
\]

The fixed-level spectral Parseval bound for V, the Fourier bound in
(20), the explicit three cusp coefficients, and Stirling give, for
U>=4L, a bound for the spectral portion |t|>U of the finite contour
of the form

\[
 O_{J,\eta}\left(A^2 N^{2+\eta}(1+L)^C(1+U)^C
                 e^{-\pi U/2+\pi L}\right),            \tag{8}
\]

with some fixed absolute C; its exact polynomial degree is irrelevant
beside this exponential. Here the factor e^(pi|t|/2) in Fourier
coefficients is canceled by the e^(-pi|t|+pi|tau|) from G, leaving
e^(-pi|t|/2+pi|tau|) before Cauchy. The continuous coefficient in (3)
has the same exponential size and only divisor/logarithmic additional
growth. Parseval applies to v_a with its 1/(4pi) measure; fixed
measure factors are included in the implicit constant. Formula(8)
does not use an exponentially weighted Parseval estimate for V.

For example choose L=T^Q(1+Lambda_max), U=4L, with fixed sufficiently
large Q and B. Equations(7)--(8) are then O(A^2T^(-D)) for any
prescribed fixed D, by choosing Q,B once. Keeping -Z_L, (6) is thereby
a finite-contour, finite-height expression with every discarded tail
paid. The remaining region, including Lambda_max<|t|<=4L, is part
of the complete test (25); it is not declared negligible merely
because its formal full Legendre kernel is nonstationary.

## 3.2 Exact inverse gamma kernel

For each fixed real t, the following elementary identity holds for
Re(s)>1/2:

\[
 G(s,it)=\int_1^\infty P_{-1/2+it}(2u-1)u^{-s}du.       \tag{9}
\]

Here P is equivalently defined by
P_(-1/2+it)(2u-1)=2F1(1/2-it,1/2+it;1;1-u).
To check (9), write a=1/2-it, b=1/2+it. The product of the two
Euler beta integrals for Gamma(s-a)/Gamma(s) and
Gamma(s-b)/Gamma(s) has inverse Mellin kernel supported on u>1.
On imposing the product variable uv=1/x, its one-dimensional
integral is

\[
 {x\over\Gamma(a)\Gamma(b)}
 \int_0^1 r^{b-1}(1-r)^{a-1}
                (1+(x-1)r)^{-a}dr
 =xP_{-1/2+it}(2x-1).
\]

This proves (9), including the x factor in the inverse kernel.
The beta integrals converge for Re(s)>1/2; the equalities can also
be checked after pairing against a compact smooth test, avoiding a
pointwise delta-function interpretation.

For a fixed mode, taking L to infinity in (5) is therefore legitimate
and gives

\[
 K_h(t)=h^{-1/2}J_h(t),\qquad
 J_h(t)=\int_0^\infty W_h(x)
                  P_{-1/2+it}(1+2x/h)dx.               \tag{10}
\]

This calculation preserves the source's n+h denominator and its
zero atom. It has no missing power of N, h, or 2pi. As a useful
analytic continuation control, at t=i/2 the Legendre function is1
and G(s,it)=1/(s-1), recovering the density inversion.

An unqualified replacement of all K_(h,L) by K_h in (6) also exchanges
the spectral and Mellin limits. That additional exchange is not
proved by (9). In particular, it cannot be deduced from V in L2.
The exact statement here is (6), and (10) is an exact individual-mode
transform. I keep that distinction in the norm ledger below.

## 3.3 Uniform joint phase; no false small-shift simplification

On every nonempty continuous overlap x,x+h are between N/2 and2N.
Put

\[
 r=2\operatorname{arsinh}\sqrt{x/h},\quad
 x=h\sinh^2(r/2),\quad a_x=\sqrt{x(x+h)}.
\]

Then dr/dx=1/a_x, r is bounded below by a positive constant, and
its support is contained in an interval of bounded length even when
h/N tends to zero. Exactly,

\[
 \sqrt{x+h}-\sqrt x=\sqrt h e^{-r/2},\quad
 1+2x/h=\cosh r.                                      \tag{11}
\]

The elementary oscillatory representation

\[
 P_{-1/2+it}(\cosh r)={\sqrt2\over\pi}
   \int_0^r {\cos(tu)\over\sqrt{\cosh r-\cosh u}}du
\]

can be verified by its differential equation and its value1 at r=0.
Expansion of the integrable endpoint singularity u=r, with integration
by parts away from that endpoint, gives for t>=1 and r>=r0

\[
 P_{-1/2+it}(\cosh r)=
  \left({2\over\pi t\sinh r}\right)^{1/2}
     \cos(tr-\pi/4)+\text{successive oscillatory symbol terms}.
                                                               \tag{12}
\]

The next term is O(t^(-3/2)(sinh r)^(-1/2)); expansion to any fixed
order has corresponding derivative bounds on bounded r windows.
Uniformity for large r follows by factoring sinh r in the endpoint
denominator; coth r and all its derivatives are bounded for r>=r0.
At u=0 the even extension cancels the apparent boundary terms.

In (10), the two large-t phases in the r variable are

\[
 2\pi R\sqrt h e^{-r/2}+tr,\qquad
 2\pi R\sqrt h e^{-r/2}-tr.                            \tag{13}
\]

The second has no stationary point for t>=0. The first has a unique
possible stationary point, specified in (1), and its second derivative
there is t/2>0. On the whole physical support its second derivative
is comparable to Lambda_h=Rh/sqrt(N). Thus there is no degenerating
curvature as h/N tends to zero. The stationary spectral heights are
t comparable to Lambda_h, ranging from R/sqrt(N) through R sqrt(N).
Because N<=2T^(3/2), the smallest of these grows at least as a fixed
multiple of T^(1/4). Bounded T is handled by fixed constants.

The phase at the stationary point is exactly (1). The leading
stationary-phase term, when the critical point is inside the smooth
support, is

\[
 J_h(t)=g(x_t+h)g(x_t){\sqrt{h a_{x_t}}\over t}
             e^{i\Phi_*(t,h)}
       +O_J(A^2\sqrt{hN}\,t^{-2}),                    \tag{14}
\]

locally uniformly away from a fixed outer padding boundary; the same
uniform bound below applies when the point meets or leaves the support.
There is no hard endpoint jump: the actual amplitude extends smoothly
by zero. The two stationary-phase factors exp(-i pi/4) from (12) and
exp(i pi/4) from the positive curvature cancel.

The corresponding rigorous scalar bounds, valid for the exact J_h,
are

\[
 {|J_h(t)|\over\sqrt h}\ll_J A^2 {\sqrt N\over\Lambda_h}
          \quad(t\asymp\Lambda_h),                    \tag{15}
\]

and arbitrarily high nonstationary inverse powers outside a fixed
enlargement of that range. For 1<=t far from Lambda_h one may use
A^2 sqrt(N)t^(-1/2)(t+Lambda_h)^(-B); for |t|<=1 one may use
A^2 sqrt(N)log(2N)(1+Lambda_h)^(-B). Constants depend on B and fixed
Schwartz seminorms. These bounds follow by the positive curvature in
(13), fixed-order stationary phase, and repeated integration by parts
in the two nonstationary phases. P and J are even in t.

The resulting h phase contains h^(it), coupled to spectral height.
An arbitrary-vector or fixed-coefficient spectral large sieve cannot
erase that dependence. Differentiating only the displayed scalar
phase in t, or treating the discrete eigenvalues as an unweighted
integral, would erase the unknown oscillation of v_j and rho_j(h).
The continuous coefficients have their own gamma and Dirichlet-series
phases as well. These must be combined before a claimed cancellation.

In particular, neither (14) nor nonstationarity of a model with
constant spectral coefficients shows that the actual arithmetic
spectral sum is small. Conversely, the phase calculation does not
show that the original wave has a large value. It exposes where the
arithmetic cancellation must occur, with all powers fixed.

## 3.4 Actual norm menu and its first unsupplied entries

For a dyadic spectral interval K<=|t|<=2K and a dyadic shift interval
M<=h<2M, write

\[
 \alpha_j(h)=e^{-\pi t_j/2}\rho_j(h),\quad
 V_j=e^{\pi t_j/2}v_j,\quad
 \mathcal V_K=\left(\sum_{K\le t_j\le2K}|V_j|^2\right)^{1/2},
                                                               \tag{16}
\]

with analogous V_a(t) and alpha_(a,h)(t)=e^(-pi|t|/2)c_(a,h)(t)
for the continuous part. The exact vector norm for a finite contour is

\[
 \mathcal U_{K,M,L}=
 \left(\sum_{K\le t_j\le2K}
 \left|\sum_{M\le h<2M}b_h\alpha_j(h)K_{h,L}(t_j)\right|^2
 \right)^{1/2}.                                      \tag{17}
\]

Its full Legendre counterpart replaces K_(h,L) by J_h/sqrt(h).
Cauchy gives exactly 2pi V_K U_(K,M,L) for this band, retaining the
h sum inside the norm. Holder would require the actual V fourth norm
and the dual 4/3 norm of this same coupled vector. Neither is supplied
by replacing V_j with a point value by name.

For clarity, the elementary applicable prices for the full Legendre
counterpart, at K comparable to RM/sqrt(N), are as follows:

\[
 \begin{array}{c|c}
 \text{input/norm} & \text{resulting raw band price}\ \hline
 \text{actual joint Cauchy} & 2\pi\mathcal V_K\mathcal U_{K,M}\cr
 \text{Minkowski in h plus coefficient second moment}
  & \ll A^2\sqrt N\,M^{1+\Theta+\epsilon}\mathcal V_K\cr
 \text{one continuous cusp, Cauchy and explicit divisor coefficients}
  & \ll A^2\sqrt N\,M^{1+\epsilon}K^{-1/2}\mathcal V_{a,K}\cr
 \text{ordinary Parseval for V only}
  & \mathcal V_K,\mathcal V_{a,K}\ll e^{\pi K}\|\mathcal V\|_2 .
 \end{array}                                         \tag{18}
\]

The continuous norm includes both signs of t and the fixed Plancherel
measure. The second line is proved using (15) and

\[
 \sum_{K\le t_j\le2K}e^{-\pi t_j}|\rho_j(h)|^2
       \ll_\epsilon h^{2\Theta+\epsilon}K^{2+\epsilon},
 \qquad\Theta=7/64,                                  \tag{20}
\]

which is the fixed-level Fourier bound in the additional source's
Lemma6.1 proof. Its hypotheses are exactly a level4 Maaß basis,
positive integer h and K>=1; no theta-power or varying-level
specialization is used for this inequality. For (3), the explicit
divisor formula and Gamma(.5+it) give
|alpha_(a,h)(t)|<<h^epsilon log(2+|t|); integration over a K band gives
K^(1/2+epsilon), proving the third line. All three cusps remain.

These prices are upper certificates. They supply no lower bound for
U, V, or the signed expression. Ordinary Parseval's exponential price
does not combine with polynomial decay in (15) to justify absolute
summation of the full Legendre expansion. That is why (6), rather than
an unjustified reordered series, is the authoritative exact interface
in this report.

If the second line of (18) were the chosen mechanism, its normalized
wave-square contribution would be

\[
 A^2 N^{-1}M^{1+\Theta+\epsilon}\mathcal V_{RM/\sqrt N}.
                                                               \tag{21}
\]

Thus a sufficient absolute-norm replacement would need
sum_(M<=2N) M^(1+Theta) V_(RM/sqrtN)<<N T^epsilon,
together with all continuous and spectral-tail entries. At M comparable
to N this asks for V_K<<N^(-Theta)T^epsilon under this particular
Minkowski mechanism. That is a statement of the missing saving in a
named norm mechanism, not a necessary condition for the true signed
bound. Joint cancellation can be stronger than (18).

The AH point-value fourth moment is not such a bound. At level4 and
discriminant -4 even its stated Heegner local hypotheses fail: 2^2
divides the level while 2 is ramified, whereas its Section2.4 requires
splitting at square-dividing primes. AH's r2 application uses levels1
and2. A lawful transfer would have to derive the theta-pairing identity
and its old/new and 2-adic factors at those levels; no equality between
these two coefficient vectors is presumed here.

There is also a version-specific obstacle to quoting AH Lemma2.1
literally as the requisite coefficient large sieve. Its displayed
right side sums over N<n<=N, its first spectral sum lacks a height
cutoff, and equation(9) prints a sqrt(n) coefficient factor. The exact
v1 PDF text, pp.10--11, agrees with the HTML on these features. Under
the printed Whittaker convention W_(0,it)(4pi n y)=2sqrt(ny)K_it(2pi n y),
the usual Hecke normalization instead requires an inverse sqrt(n)
in that particular Fourier coefficient. These observations do not
refute its separately stated Theorem1.2. They prevent an unannounced
repair of a large-sieve normalization during this application audit.
No corrected theorem or omitted height restriction is imported.

Even a correctly sourced product-vector large sieve would still need
to price the joint h^(it) amplitude in (14). A decomposition
B(t,h)=sum_l f_l(t)a_l(h) can be used only with the sum of the relevant
product norms, not with one arbitrary a_h while t varies. No subpower
separation norm has been proved here.

## 3.5 Complete arithmetic fallback and physical restoration

For every h<2N, including a discrete-empty overlap,

\[
 |\mathcal R_h|\ll_{\epsilon,J}A^2N^{1+\epsilon}
       +\rho_h\left|\int W_h\right|.
\]

The smooth oscillatory density is bounded by
A^2N^(3/2)/(Rh), uniformly over the literal continuous overlap.
Consequently

\[
 |\mathcal F|\ll_{\epsilon,J} A^2N^{2+\epsilon}
       +A^2N^{3/2+\epsilon}T^{-1}\log(2N).             \tag{22}
\]

This is a complete bound with no unestimated shift complement. It is
the fallback price, not new progress. Normalized Fejer, with exact
factor (3N/2-1+2N-1)/(2N), gives shell wave-square O(A^2N^(1/2+epsilon))
and hence shell modulus O(A N^(1/4+epsilon)).

The real diagonal costs O(A^2N^(1+epsilon)) before multiplying by
N^(-3/2); negative shifts are the conjugates already included by
2Re. All dyadic N<=P are summed. For fixed sufficiently large J,
sum_N A_J(N)N^(1/4+epsilon)<<T^(1/4+epsilon). The singleton n=1 is O(1).
The dyadic partition is exactly phi(n/P) for n>=2; the remainder n>P
is O(T^(-D)) for any fixed D by a sufficiently large fixed Schwartz
order. Thus (22) gives the complete complex wave exponent gamma=1/4
and the physical exponent

\[
 1/4+\gamma/2=3/8.                                   \tag{23}
\]

The checkpoint's already recorded complex cap13/56 may cap this
weaker certificate; it is not a result of this report. The inherited
complete real beta=2theta_LY-1/2 remains stronger for the actual real
goal. No per-block or complex beta estimate is used. If (F) were
proved, precisely the same complete reconstruction would give gamma=0
and the physical quarter theorem. No fixed moment has been substituted
for that full objective.

# 4. First doubtful or unproved step

With L,U chosen as after (8), let

\[
 \mathcal S_{L,U}=2\pi\sum_{t_j\le U}v_j
       \sum_{h<2N}b_h\rho_j(h)K_{h,L}(t_j)
 +\sum_{\mathfrak a}\int_{-U}^{U}v_{\mathfrak a}(t)
       \sum_{h<2N}b_hc_{\mathfrak a,h}(t)K_{h,L}(t)dt-Z_L.
                                                               \tag{24}
\]

The exact first unproved complete inequality of this attack is

\[
 \boxed{\quad 2\Re\mathcal S_{L,U}
       \le C_{\epsilon,J} A^2N^{3/2}T^\epsilon,
 \quad\text{uniformly in every required }T,N,R.\quad}  \tag{25}
\]

The paid errors (7)--(8) make this equivalent to the required bound
at epsilon-loss level. There is no unestimated complementary shift or
spectral region hidden in (25). Its full spectral coefficient/test
pairing is the missing estimate.

For the attractive Legendre reformulation, an earlier analytic seam
is the interchange from (6) to the termwise sum of (10), with explicit
normalized spectral growth and tails. The additional source's
k>=3 theta-pairing estimate, or plain V in L2, is not a proof of that
k=2 weighted assertion in this audit. Even granting the interchange,
(18)--(21) display the next unsupplied joint norm. Therefore neither
a formal transform identity nor the stationary sector is counted as
completion or as a complete bound improvement.

# 5. Required controls and outcomes

| Control | Outcome and limitation |
|---|---|
| Actual coefficients/density | Actual r2 and all two-adic rho_h retained in (2),(4); no cusp-coefficient substitution. |
| All shifts/scales | Every 1<=h<2N remains inside (24); all dyadic N<=P and all real R are required. |
| Joint phase before norms | Exact kernel and phase (10)--(14); norms in (17) retain h inside the vector. No spectral-point differentiation of unknown coefficients. |
| Continuous/discrete/constant | Cuspidal sum and all three cusp integrals retained; constant P_h coefficient is zero by the source. |
| Contours/residues | Fixed sigma=2 throughout; whole density subtracted; finite atom retained. No unlisted contour crossing. |
| Mellin/spectral tails | Quantified ordered finite truncation (7)--(8). Reversed-limit Legendre series is explicitly not asserted. |
| Small shifts/gamma transition | Hyperbolic variable (11) has uniform curvature; h=1 is included without Stirling at tau-t small. |
| Endpoints/empty overlap | Smooth zero extension pays endpoints. Discrete-empty but continuous-nonempty shifts keep their compensating remainder. Truly empty continuous overlap has q_h=0. |
| Source bridge | AH point values do not equal HKLDW theta pairings by assumption; level4,D=-4 hypotheses are explicitly checked. |
| Literal printed formulas | No deletion of h^Theta, no N^(4/3) for printed N^(4/2), and no silent correction of the newly inspected Lemma2.1 normalizations. |
| Real/complex | (F) is stronger sufficient complex closure; inherited beta is only complete real. |
| Full reconstruction | Diagonal, Fejer constant, negative shifts, dyadic overlap, singleton and original infinite Schwartz tail included. |
| Actual/certificate | Every norm loss above is an upper-certificate price, never an actual-value lower bound. |
| Statement-only isolation | This report is not statement-only; no sibling or blind report was read. It does not certify the blind role's result. |
| Fixed-order/full goal | No fixed moment, local h range, or formal identity is promoted to the full quarter goal. |

All work was analytical/algebraic. Zero numerical experiments were
performed. Source retrieval and exact file hashing are provenance
operations, not mathematical experiments.

# 6. Dependencies and exact provenance

Read only the assigned local context and the permitted primary works.
The graph was inspected for the named target obligations; the initial
whole-file retrieval was output-truncated, so no claim is made to have
reviewed the whole historical graph. The named target nodes retain
their recorded statuses. No current sibling report, blind packet,
conductor control/review, or unassigned historical file was read.

The conductor sent an interior stationary-phase calculation and a
warning about its gamma transition. I independently obtained the same
locus from the beta/Legendre kernel; that communication is disclosed,
and this report is not an independent statement-only phase review.

Exact local dependencies at the read/hash time:

| Path | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | ab4e6440ce041a984364e755c2ee24a6606f548dabd566190677f1d44d992291 |
| strategy/round227_complete_joint_spectral_remainder.md | c91b9ec5836a4b1c998b18724c951c059241a975f55caa149ba4449ab0f5e19e |
| strategy/gauss_circle_strategy_review_2026-09-23.md | 0729f1d9c596867e7a06bdcd096847b32e6747653235706b01275a153bd617c6 |
| strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md | f6aba7be605277ef9e09915e749ce07d22deb3cbfe95cc761660508a7f5c53c9 |
| rounds/codex-managed/gc-complete-joint-spectral-remainder/briefs/complete_joint_spectral_interface.md | ed64b7189d806dae4dfbf5a2da598268e09722d9c3812ec0c1376727d8b05d7c |
| rounds/codex-managed/gc-full-goal-spectral-source-review/reports/actual_shifted_spectral_sources.md | 1bcb14e1899138097a3ab0e273060f2deaa800e3eb732e2924afb2f1f02d25bc |
| rounds/codex-managed/gc-full-goal-spectral-source-review/reviews/independent_shifted_source_review.md | ddc722665f6417515cd1039b1538018e8e8c0fa9c98a00773253705505430df8 |
| rounds/codex-managed/gc-full-goal-spectral-source-review/synthesis.md | 8c43670fa6021fc30a3c0a421f26abd4f1636045b79084a272556b54ef273720 |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |

Primary version bindings:

* [HKLDW1705.04771v3](https://arxiv.org/html/1705.04771v3): equations(3.3),
  (3.4),(3.9),(3.10), Lemma3.4, and Theorem7.1. The exact source
  expansion was already assigned context; new analytic manipulations
  are proved above. No global w=0 shift average is substituted.
* [AH2607.13518v1](https://arxiv.org/html/2607.13518v1): Theorem1.2,
  Theorem1.3/application, Section2.1 and Section2.4. The
  [exact PDF](https://arxiv.org/pdf/2607.13518v1), pp.10--11, was checked
  by extracted text for the displayed coefficient/sieve issues.
  PDF screenshots did not provide a usable visual check; none is claimed.
* [HKLDW1703.10347v3](https://arxiv.org/html/1703.10347v3#S6): only
  Lemma6.1's polynomial-growth proof and its fixed-level normalized
  Fourier second moment were audited. This is the single additional
  source audit, needed to state explicit safe spectral truncation and
  Fourier norm costs. Its k>=3 theta-pairing bound is not granted as
  the missing k=2 exponential-weighted norm.

# 7. Recommended state effect and stopping rule

Recommended effect: **no change** to the accepted graph, proof draft,
M1/M2/GAR/endpoints, complete moment bounds, or pointwise exponents.
Retain this as evidence for the actual joint kernel, the safe ordered
spectral interface and the precisely located missing estimate (25),
subject to independent kernel/source/normalization review.

The successful scalar kernel derivation is not the complete analytic
gain required by the campaign. The bounded attack ends with
`complete_joint_spectral_remainder_no_new_bound`. No universal
spectral-method impossibility is asserted. The conductor alone closes
the round and chooses any successor. This agent stops after hashing
this assigned report and does not edit authoritative state.
