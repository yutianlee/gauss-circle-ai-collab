# Round229 conductor radial Abel control and conditional application

## 1. Result

For the isolated compact-time profile, the complete absolute radial mass
is comparable to sqrt(U) exp(L/2), whereas its signed integral is
2cosh(L/2)H(i/(2U)). A nonzero smooth compact SPECTRAL cutoff does not,
by smoothness alone, produce an absolutely integrable radial kernel of
this kind: in fact it cannot have finite hyperbolic L1 mass.

These are scalar conclusions. The actual moving complex Hecke multiplier
has not been replaced by the scalar cosine test. Neither kernel mass nor
the phase alone estimates the full fixed-CM cuspidal sum.

## 2. Exact statement and hypotheses

Conductor, NONBLIND, campaign gc-full-goal-cuspidal-source-review,
Round229, 2026-09-29. G is fixed, even, nonnegative, smooth, compactly
supported in (-1,1), and integral G=1. U,L>=2 are independent real
parameters. H(t)=integral G(v)exp(itv)dv. Use exactly the packet's g,k:
g(s)=U[G(U(s-L))+G(U(s+L))] and

\[
k(r)=-\frac1{\pi\sqrt2}\int_r^\infty
       \frac{g'(s)}{\sqrt{\cosh s-\cosh r}}\,ds,
\quad r\ge0.
\]

Constants depend only on fixed seminorms of G and differentiation orders.
No automorphic identity is assumed merely from this definition. For the
compact-spectral contrast, h is even, nonzero and C_c^infinity(R), and
g(s)=(2pi)^(-1)integral h(t)exp(-its)dt; k uses the same Abel definition.

## 3. Independent derivation and scoped application

### Transform, support and local profile

The Fourier transform of g is exactly 2cos(Lt)H(t/U). For s>=0 only
the bump centered at L contributes. Its support is contained in
[L-1/U,L+1/U], so k vanishes for r>=L+1/U. It need not vanish below
L-1/U. At r=0 the denominator is comparable to s near zero, but the
support of g' is separated from zero; the integral is regular.

Put r=L+a/U and s=r+v/U. For a in a fixed compact interval, and U
sufficiently large in terms of that interval, r>=1. The exact formula is

\[
k(L+a/U)=-\frac{U^{3/2}}{\pi\sqrt{2\sinh r}}
 \int_0^\infty G'(a+v)v^{-1/2}
 \left[\frac{\cosh(r+v/U)-\cosh r}{(v/U)\sinh r}\right]^{-1/2}dv.
\]

The integration range is bounded by the support of G'. The bracket is
1+coth(r)v/(2U)+O_A(U^(-2)). Consequently, if
Phi(a)=integral_0^infinity G'(a+v)v^(-1/2)dv and
Psi(a)=integral_0^infinity G'(a+v)v^(1/2)dv, then

\[
k(L+a/U)=-\frac{U^{3/2}}{\pi\sqrt{2\sinh L}}
\left[\Phi(a)-\frac{\coth L}{U}
 \left(\frac a2\Phi(a)+\frac14\Psi(a)\right)+O_A(U^{-2})\right].
                                                               \tag{1}
\]

Every fixed a-derivative, and every fixed L-derivative, of the normalized
error has the same order on compact a intervals. Differentiate the
displayed smooth bracket and G under the integrable v^(-1/2) integral;
coth and its fixed derivatives are uniformly bounded for r>=1. This
also covers a meeting the smooth support edge. No large-U expansion is
claimed for an a interval so large that r could be negative at U=2.

The profile is not identically zero. For a<-1, integration by parts gives

\[
\Phi(a)=\frac12\int_{-1}^1G(y)(y-a)^{-3/2}dy>0.          \tag{2}
\]

It is zero for a>=1, and has an interior tail of order |a|^(-3/2),
rather than rapid decay toward negative a. Smooth compact TIME support
has not been confused with annular support of k.

### Full absolute mass, including the entire interior

On L-2/U<=r<=L+1/U, r>=1 and sinhr is comparable to exp(L).
The original integral therefore gives
|k(r)|<=C U^(3/2)exp(-L/2). The entire contribution of this interval
to 2pi integral |k|sinhr dr is O(sqrt(U)exp(L/2)).

For 0<=r<=L-2/U integrate by parts in s. Since g is nonnegative,

\[
k(r)=-\frac1{2\pi\sqrt2}\int g(s)
       \frac{\sinh s}{(\cosh s-\cosh r)^{3/2}}ds<0.      \tag{3}
\]

Write delta=L-r>=2/U. On the support of g,
coshs-coshr is bounded below by a constant times
exp(L)min(delta,1), and sinhs is comparable to exp(L). As integral
over positive s of g(s) equals1, (3) gives
|k(r)|<=C exp(-L/2)min(delta,1)^(-3/2).
Using sinhr<=C exp(L-delta), the entire interior mass is at most

\[
C e^{L/2}\int_{2/U}^{L}e^{-\delta}
                  \min(\delta,1)^{-3/2}d\delta
\le C\sqrt U e^{L/2}.                                  \tag{4}
\]

This includes r=0, with no unpriced inner disk.

For a lower bound use r=L-b/U, 2<=b<=5/2, an interval of length
1/(2U). Here r>=3/4, and uniformly for all U,L>=2,
sinhr and sinhs are comparable to exp(L), while
coshs-coshr is comparable to exp(L)/U on the entire positive bump.
Equation (3) and integral g=1 give
|k(r)|>=c U^(3/2)exp(-L/2). Integrating on this interval proves

\[
\boxed{c_G\sqrt U e^{L/2}\le
2\pi\int_0^\infty|k(r)|\sinh r\,dr
\le C_G\sqrt U e^{L/2}.}                               \tag{5}
\]

This direct lower bound also covers bounded U. It does not rely on an
unquantified limiting profile or a sampled numerical value.

### Signed integral

All integrals are absolutely justified before reversing order, since g'
has compact support away from zero. The inner integral is
integral_0^s sinhr/(coshs-coshr)^(1/2)dr=2sqrt(coshs-1).
Thus integration by parts gives

\[
\begin{aligned}
2\pi\int_0^\infty k(r)\sinh r\,dr
&=-2\sqrt2\int_0^\infty g'(s)\sqrt{\cosh s-1}\,ds\\
&=2\int_0^\infty g(s)\cosh(s/2)ds\\
&=2\cosh(L/2)H(i/(2U)).                                \tag{6}
\end{aligned}
\]

Evenness of G removes the odd sinh term. Since H(i/(2U)) is bounded
above and below by fixed positive constants, this signed mass is of
order exp(L/2), smaller than (5) by sqrt(U). The exact transform at
t=i/2 agrees with (6). Neither quantity is a discrete orbit sum.

### Why a smooth compact spectral cutoff is different

For even Schwartz g the same Abel definition has inverse

\[
g(s)=\sqrt2\int_s^\infty
  \frac{k(r)\sinh r}{\sqrt{\cosh r-\cosh s}}dr,
\quad s\ge0.                                          \tag{7}
\]

To verify constants, set x=coshr and F(x)=g(arccosh x). Compose
the two Abel integrals and use
integral_z^y((y-x)(x-z))^(-1/2)dx=pi. Boundary F(infinity)=0 gives
(7). For the g coming from even C_c^infinity h, all swaps here are
justified by rapid decay of g and its derivatives; k(r) is at most
e^(-r/2) times an arbitrary fixed negative power of 1+r.

If integral|k(r)|sinhr dr were finite, (7) would imply, for any
0<b<1/2,
integral_0^infinity |g(s)|e^(bs)ds<infinity. Indeed the inner kernel
integral integral_0^r e^(bs)/(coshr-coshs)^(1/2)ds is uniformly bounded:
for r<=1 compare the denominator with sqrt(r^2-s^2); for r>=1 set
v=r-s and bound it by C_b e^((b-1/2)r) times the convergent integral
of e^(-bv)(1-e^(-v))^(-1/2). Evenness supplies the negative axis.
Its Fourier transform h therefore extends holomorphically to every
strip |Im t|<b<1/2. If h also has compact real support, it vanishes
on an open real interval, so the identity theorem makes it identically
zero. This contradicts the hypothesis. Thus a nonzero even smooth
compact SPECTRAL h does not give finite radial hyperbolic L1 mass.
This is not a ban on trace formulas with other convergence procedures.

### Conditional mapping to the actual phase

Closed228's leading primitive dual phase at positive spectral height is
exp(-i pi/4)(qdR^2/n)^(it). On a shift dyad M, t~U=TM/sqrt(N),
with descendant d, its dual index scale is K~qdT/sqrt(N). For n~K,
X=qdR^2/n is comparable to T sqrt(N), and L=log X>=2 once T is
sufficiently large. If a term could LAWFULLY be replaced by the scalar
cosine multiplier 2cos(Lt)H(t/U), (5) would give radial mass

\[
\sqrt U\,X^{1/2}=R\sqrt{qdU/n}\asymp T\sqrt M.         \tag{8}
\]

This is only substitution into the scalar result. The actual weights
are complex, depend on n and t through exact transforms, and are paired
with Hecke eigenvalues and fixed CM point values. The even cosine test
does not equal the actual exp(itL) test on positive t. No decomposition
into such tests with controlled coefficient norm has been proved here.
Further, radial continuous L1 mass is not a bound for a fixed-point
Hecke orbit sum without a uniform weighted counting argument.
Exceptional modes, oldspace factors, all n tails and the full complement
must survive any legitimate application. Smooth compact spectral
localization also cannot be substituted into (5) for free, by (7).
The source auditors independently own all actual trace-formula premises.

## 4. First doubtful or unproved step

The scalar mass and signed formulas are proved under the stated
definitions. The first unavailable arithmetic step is an exact legal
representation of the complete actual moving multiplier by admissible
tests with a paid norm, followed by a signed fixed-CM Hecke orbit or
spectral estimate at the required raw size. Neither step follows from
phase oscillation, support in the time profile, or the scalar mass.
No improvement of the entire cusp target is claimed.

## 5. Required controls and outcomes

Fourier convention and evenness: exact. Front constant and fixed-order
derivatives: (1). Nonzero profile and interior sign: (2)--(3). Entire
interior and r=0: (4). Uniform bounded-U lower bound: (5). Signed mass
and imaginary transform check: (6). Compact-spectral integrability
failure: (7) and holomorphic uniqueness. Arithmetic phase substitution:
(8), explicitly conditional and with cosine/complex mismatch retained.
Zero experiments; all bounds are analytical. Absolute mass is not an
arithmetic lower bound, and failure of this particular automatic transfer
is not an all-method impossibility.

## 6. Dependencies and provenance

Conductor-authored derivation before reading any current blind report or
receiving any blind progress message. Inputs: protocol.md;
briefs/blind_radial_abel_statement.md and briefs/complete_cuspidal_interfaces.md
in this campaign; closed228 reports/signed_hecke_functional_attack.md,
reviews/independent_signed_hecke_review.md, and synthesis.md in
rounds/codex-managed/gc-signed-heegner-phase; checkpoint226; authoritative
graph and current manifest. Basic Fourier uniqueness, integration by
parts and the elementary beta integral are proved/used at scalar level;
no external automorphic theorem is imported. Current source-role progress
about the CM formula supplied no scalar calculation. No blind or sibling
report was read. A separate nonauthor application review must bind these
exact bytes before closure; the conductor does not self-certify it.

## 7. Recommended state effect

Retain as scalar and explicitly conditional application evidence after
nonauthor review. No graph, draft, complete moment, wave or exponent
change. Full quarter and all complete frontier owners remain open.
