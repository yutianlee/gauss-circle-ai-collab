# Complete square-root large values and circle moment bound

Round204 proof kernel, 2026-09-23. Campaign:
gc-complete-large-values-duality. Authoritative acceptance is determined
by the claim graph and validated State Patch, not by this file alone.
Starting graph SHA256:
abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb.

## 1. Result and exact scope

Let Psi be a fixed real even Schwartz function. For real T>=2 and any
real lower cutoff U>=0 define

\[
 B_{T,U}(R)=\sum_{n>U}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
                 \cos(2\pi R\sqrt n-3\pi/4).
\]

For a fixed bounded nonnegative window w supported in [c,C], with
0<c<C<infinity, put

\[
 D_{T,U}(V)=\int w(R/T)1_{|B_{T,U}(R)|>V}\,dR.
\]

Uniformly for U>=0 and V>=1, for every epsilon>0,

\[
 \boxed{D_{T,U}(V)\ll_\epsilon T^\epsilon
                   (V^{-2}+TV^{-136/13}).}                 \tag{L1}
\]

The constant depends on fixed window bounds and Schwartz seminorms.
This estimate retains all arithmetic coefficients and the entire
infinite upper tail. It is a coefficient-uniform bound and does not
by itself prove the frozen stronger large-value target.

For the mollifier choice in Section6 and theta=theta_LY, let
beta=2theta-1/2. For every fixed p>=2,

\[
 \int w(R/T)|B_{T,0}(R)|^p\,dR
 \ll_{p,\epsilon}T^{1+\epsilon}+T^{(p-2)\beta+\epsilon}.   \tag{L2}
\]

Consequently the inclusive sharp circle discrepancy satisfies

\[
 \boxed{\int_{Y/2}^{3Y}|P(x)|^pdx
 \ll_{p,\epsilon}Y^{1+p/4+\epsilon}
                     +Y^{1+(p-2)\theta+\epsilon}.}         \tag{L3}
\]

In particular, its complete twelfth moment is
O(Y^(1+10theta+epsilon)). The normalized full-series sixth-power
norm is O(T^(5beta+epsilon)); its exponent is0.6448317597... .
For U=floor(T^(1/2047)), the same p-moment estimate follows from
the pointwise bound for the subtracted head; no head moment theorem
is needed. The corresponding sharp normalized moment endpoint is
q_star=2+1/beta, larger than the project's printed q0=262/27.

These bounds improve this project's recorded moment comparison.
No novelty claim is made. They yield no new pointwise exponent:
(1+10theta)/13>theta since theta<1/3. The quarter theorem, frozen
distribution target, and all M1/M2 obligations remain open.

## 2. Dependencies and source specialization

Use the accepted global Bourgain2017 exponent-pair interface
(13/84+epsilon,55/84+epsilon), elementary divisor bound, and
r2(n)=4 sum_(d|n)chi4(d), so r2(n)<=4d(n). The repaired accepted
Li--Yang bound is used only for the moment consequences in Section6.

For n in (N,2N], the phase f(n)=u sqrt(n) has fixed monomial
derivative pattern f'(x)=(u/2)x^(-1/2). Its normalized phase is
sqrt(t), with all derivatives on a fixed positive interval bounded
and the required second, third and fourth derivatives nonzero.
In the standard exponent-pair class it is the exact model s=1/2,
not an arbitrary perturbation. The source phase parameter is
mathcalT=|u|sqrt(N), and its length is comparable to N.
The source's length<=mathcalT convention is met for
|u|>=C0 sqrt(N), with fixed C0 large enough for the chosen interval.
Negative u is handled by conjugation. Only the unweighted interval
kernel below uses the exponent pair.

The primary location is Bourgain, *Decoupling, exponential sums and
the Riemann zeta function*, Section5, Theorem6, following (5.1),
[arXiv1408.5794v2](https://arxiv.org/html/1408.5794v2#S6).
The graph's existing source card is
`sources/bourgain_2017_exponent_pair.md`. Its global theorem and
proper-interval extension are used, not merely Theorem4's narrower
direct range. The fresh Round204 source audit records the exact
hypothesis match. No new external exponent pair is assumed.

## 3. Complete correlation kernel estimate

Put kappa=13/55 and
\[
 K_N(u)=\sum_{N<n\le2N}e(u\sqrt n).
\]
For1<=N<=T^(3/2), 0<|u|<=C1T, every epsilon>0,
\[
 |K_N(u)|\ll_\epsilon T^\epsilon\sqrt N
                 (|u|^\kappa+|u|^{-1}).                  \tag{L4}
\]

Here and below fixed enlargement constants in the dyadic ranges
do not change the conclusions. Three regimes establish (L4).

For0<|u|<=c0 sqrt(N), choose c0 so |f'(x)| stays below1/2.
The monotone first-derivative estimate gives O(sqrt(N)/|u|).
When that exceeds the number of terms, use O(N). This includes
the smallest u and introduces no false nonstationary condition
across an integer value of f'.

For c0 sqrt(N)<=|u|<=C0 sqrt(N), the elementary second-derivative
bound is O(sqrt(N)), since |f''| is comparable to1/N. This is
bounded by the right side of (L4). All constants are fixed.

For |u|>=C0 sqrt(N), the second-derivative bound and the accepted
source give respectively
\[
 |K_N(u)|\ll |u|^{1/2}N^{1/4},\qquad
 |K_N(u)|\ll_\epsilon T^\epsilon
             |u|^{13/84}N^{97/168}.                      \tag{L5}
\]
The usual second-derivative term |u|^(-1/2)N^(3/4) is dominated
by its first term in this range. Source epsilon factors are
absorbed in T^epsilon since both |u| and N have fixed polynomial
bounds in T. Take the geometric mean of the two valid bounds,
with weights13/55 and42/55 respectively. The resulting exponents are
\[
 \tfrac{13}{55}\tfrac12+\tfrac{42}{55}\tfrac{13}{84}
 =\tfrac{13}{55},\qquad
 \tfrac{13}{55}\tfrac14+\tfrac{42}{55}\tfrac{97}{168}
 =\tfrac12.
\]
This is an interpolation of two numerical upper bounds on the
same unweighted sum. It is not an assertion for arbitrary weighted
phases. These three regimes prove (L4).

## 4. Finite duality, localization and covering

This section isolates the finite kernel. Suppose
S(R)=sum_(N<n<=2N)a_n e(R sqrt(n)),
sum|a_n|^2<=A N^(-1/2), and
|K_N(u)|<=A sqrt(N)(|u|^kappa+|u|^(-1)), with A>=1.
Let I be an interval of length at most C1T. For every v>0,
\[
 |\{R\in I:|S(R)|>v\}|
 \ll A^2\log(2+T\sqrt N)\left(v^{-2}
               +T A^{2/\kappa}v^{-(2+2/\kappa)}\right).  \tag{L6}
\]
The upper bound may of course be capped by |I|.

Partition I into at most C(1+T/h) intervals of length at most h,
where h=(v^2/(4C2 A^2))^(1/kappa) and C2 is a fixed large
absolute constant absorbing the kernel bound. If h exceeds |I|,
there is one interval, not a fractional number of intervals.

In a local interval take a maximal delta-separated subset of its
level set, with delta=N^(-1/2). Such a finite set exists because
the interval is bounded; maximality covers the level set by intervals
of radius delta around the selected points. No persistence or
derivative bound for S is needed. Write the selected points as
R_1,...,R_J and choose unit z_j to align their values. Cauchy gives
\[
 J^2v^2\le \left(\sum_n|a_n|^2\right)
       \sum_n\left|\sum_j z_j e(R_j\sqrt n)\right|^2.
\]
Expanding the finite square, bounding off-diagonal terms by their
absolute values and dividing by J gives
\[
 Jv^2\le C A\sqrt N
       +C A^2\left(Jh^\kappa+\delta^{-1}\log(2+J)\right).
                                                               \tag{L7}
\]
The first term is the full Gram diagonal K_N(0), which is the
number of positive integers in the dyadic interval. The harmonic
sum follows by ordering the delta-separated points on both sides
of any one point. Always J<=1+C1T/delta, so its logarithm has
the size used in (L6). Choosing C2 large absorbs the Jh^kappa
term. Hence Jv^2<<A^2 sqrt(N)log(2+T sqrt(N)).

The local level-set measure is at most2delta J, giving
O(A^2log(2+T sqrt(N))v^(-2)). Multiply by the *full* number of
local intervals to prove (L6). For J=0 the statement is immediate;
for J=1 the diagonal is retained. Arbitrary real endpoints, v and
coefficients are allowed.

With A a fixed small power of T, (L6) and2+2/kappa=136/13 give
\[
 |\{|S|>v\}\cap I|\ll_\epsilon
 T^\epsilon(v^{-2}+Tv^{-136/13}),                         \tag{L8}
\]
after choosing the input epsilon sufficiently small relative to the
requested output epsilon. Every displayed power of A is finite.

## 5. Actual coefficients and complete infinite recombination

Take an upper truncation Z=T^(3/2). For each fixed K, Schwartz
decay and the divisor bound imply
\[
 \sum_{n>Z}r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|\ll_K T^{-K}.
                                                               \tag{L9}
\]
For example use a decay order L: the left side is bounded by
T^(L/2)Z^(1/4+eta-L/2), and then increase the fixed L.
This estimate holds uniformly after any lower cutoff U.

If U>=Z, the entire tail is covered by (L9) and no level V>=1
occurs once T is large. Otherwise retain the singleton {1} separately
and partition integers2<=n<=Z into dyadic blocks; set coefficients
to zero unless n>U. For the singleton, the proof of Section4 applies
verbatim with N=1, index set {1}, and K(u)=e(u): its diagonal is1,
its coefficient energy is bounded by a fixed constant, and
1<=|u|^kappa+|u|^(-1) for all u!=0. Thus (L8) holds for this block
as well, after including that fixed constant in A.
The possibly partial first/last blocks are zero-extended into
their full ambient dyadic intervals. For each block,
\[
 \sum |a_n|^2\ll_\eta N^{-1/2+2\eta}
                     \ll_\eta T^{3\eta}N^{-1/2}.         \tag{L10}
\]
Thus (L8) applies directly. No weighted exponent-pair estimate is
being asserted: all actual weights stay in the coefficient vector.
The cosine block is the real part of e(-3/8)S(R), so its large
values are contained in those of |S|. Both original phases are
therefore accounted for exactly.

There are O(log T) blocks. If |B|>V, then, after the uniformly
small error (L9), at least one block has modulus exceeding
V/(C log T). Apply (L8) and sum the finitely many level sets.
All logarithmic powers are absorbed in T^epsilon. Multiplication
by the fixed upper bound for w proves (L1). For bounded T, the
Schwartz/divisor l1 bound gives a uniformly bounded possible V,
and enlarging the constant proves the same result. This argument
also treats U=0, with no tiny-head or exact-resonance assumption.

## 6. Pointwise input, moments and sharp reconstruction

Fix a nonnegative real radial rho in C_c^infinity(R^2), supported
in the unit disk and of integral1, and set Psi(s)=rho-hat(s e1)
under the e(-x dot xi) Fourier convention. For T=sqrt(Y), use the
single fixed smoothing width delta=T^(-1/2) over all R~T.

The difference between the inclusive sharp count and
S_delta(R)=sum_m(1_(B_R)*rho_delta)(m) is supported in the closed
annulus R-delta<=|m|<=R+delta. Including its endpoints costs
\[
 |N(R)-S_\delta(R)|\ll_\epsilon
             (R\delta+1)T^\epsilon\ll T^{1/2+\epsilon}.  \tag{L11}
\]
This pays every possible integer-radius jump. Periodize the smooth
compactly supported convolution and evaluate its absolutely
convergent Fourier series at zero to obtain Poisson summation.
The polar disk transform is R J1(2pi R|k|)/|k|. Thus
\[
 S_\delta(R)-\pi R^2
 =R\sum_{n\ge1}r_2(n)n^{-1/2}\Psi(\sqrt{n/T})
                         J_1(2\pi R\sqrt n).
\]
The fixed-order positive-real Bessel expansion yields
\[
 P(R^2)=\frac{\sqrt R}{\pi}B_{T,0}(R)
                           +O_\epsilon(T^{1/2+\epsilon}). \tag{L12}
\]
Its entire Bessel remainder is
O(R^(-1/2) sum_n r2(n)n^(-5/4))=O(T^(-1/2)), since the series
converges by the divisor bound. Standard identities used here are
[DLMF10.9.1](https://dlmf.nist.gov/10.9.E1),
[DLMF10.6.6](https://dlmf.nist.gov/10.6.E6), and
[DLMF10.17.3](https://dlmf.nist.gov/10.17.E3), for real argument
and orders0,1. All sums converge absolutely after the fixed cutoff.

The accepted pointwise P(x)<<x^(theta+epsilon) and (L12) give
\[
 \sup_{R\in[cT,CT]}|B_{T,0}(R)|\ll T^{\beta+\epsilon}.
                                                               \tag{L13}
\]
Subtracting the head up to floor(T^(1/2047)) adds only
O(T^(1/8188+epsilon)), smaller than this bound. No estimate for
that head's high moments is required.

Let q=136/13. The exact accepted theta obeys
5/16<theta<131/416<1/3. Therefore
1/8<beta<27/208 and beta(q-2)>1. Layer cake, (L1), the trivial
measure O(T) below V=1, and (L13) give, for fixed p>2,
\[
 M_p\ll T^{1+\epsilon}+T^\epsilon W^{p-2}
       +T^{1+\epsilon}\int_1^W V^{p-1-q}\,dV,
 \qquad W\ll T^{\beta+\epsilon}.                        \tag{L14}
\]
If p<q the last integral is bounded; if p=q it is logarithmic.
For p>q its power contribution is dominated by T^((p-2)beta),
because beta(q-2)>1. The case p=2 has only an additional logarithm
in the first integral. Renaming epsilon proves (L2) for every fixed
p>=2, including the endpoint q_star=2+1/beta<q.

Choose a smooth nonnegative w equal to1 on
[1/sqrt(2),sqrt(3)]. Restoring the leading amplitude, the Jacobian
dx=2R dR and the smoothing error in (L12) gives
\[
 \int_{Y/2}^{3Y}|P(x)|^pdx
 \ll T^{1+p/2}M_p+T^{2+p/2+\epsilon},
\]
which is precisely (L3). This proof applies to the full series
directly, retaining every mixed term through the physical norm
inequality. Constants may depend on the fixed p; no p growing with
Y is asserted.

At p=12, the norm exponent is5beta=10theta-5/2, the sharp
moment exponent is1+10theta, and its loss from Y^4 is10theta-3.
Compared with the previously recorded loss
(62/27)(theta-1/4), the reduction is positive since
theta<131/416. The old q0 equals2+208/27, while
q_star=2+1/beta>q0. These are consequences of the independently
proved distribution inequality, not substitutions into an
uninspected Ivić theorem.

## 7. Controls, remaining gap and formalization boundary

The V^-2 term in (L1) is essential to this generic mechanism.
For a block N<n<=2N, choose a_n=N^(-3/4)e(-R0 sqrt(n)), with
R0 in the interior of the radius window. At R0 the sum has size
comparable to N^(1/4); on a sufficiently small fixed multiple of
N^(-1/2) around it, all phases remain close enough for the same
lower bound. Its twelfth moment is at least cN^(5/2).
Taking N comparable to T^(4beta) gives T^(10beta), the high-moment
term in (L2), while its coefficient norm and supremum satisfy the
generic data used above. This is an aligned coefficient control,
not the fixed arithmetic r2 family. It prevents removal of the
diagonal/one-interval term by coefficient-uniform reasoning alone.

The actual r2 target remains unproved. In particular, V^-2
already exceeds the desired T^(29/25)V^-12 when
V>T^(29/250). That range lies below the available supremum
T^beta, since beta>29/250. The remaining saving must exploit
information beyond the generic norm and unweighted correlation
bound, or use a different complete argument.

No numerical experiment supports this theorem. The finite duality
identity in Section4 is isolated for possible formalization; a
formal proof of that finite algebra would not certify the external
source or replace the analytic seam checks. The independent
statement-only report rederives the finite mechanism and its
one-peak control; independent source, power and full-error reviews
are required before graph promotion.
