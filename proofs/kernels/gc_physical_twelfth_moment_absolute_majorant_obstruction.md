# Actual circle coefficients obstruct a termwise absolute twelfth-moment bound

Round 202, campaign `gc-strategy-signed-moment-majorant-review`, 2026-09-23.
Conductor proof; candidate until a validated State Patch accepts it.
Starting graph SHA-256:
`682cb189a3ab0ef26f8d19701e2949547446d37505df01f7b7eaf1cfdd0f359c`.

## Statement and scope

Let r_2(n) count ordered signed representations of n as two integer
squares. Fix real even Schwartz Psi with Psi(0)=1 and a nonzero
nonnegative w in C_c^infinity((0,infinity)). Define
a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T)), T>=2, and use Fourier convention
w-hat(xi)=integral w(u)e(-u xi)du, e(v)=exp(2pi i v).

There are fixed constants 0<a<b, h>0 and c>0 such that for all
sufficiently large real T the coefficients on I_T=[aT,bT] intersect N
are nonnegative and

\[
 T\sum_{\substack{n_1,\ldots,n_{12}\in I_T\\
             0<|\Delta|\le h/T}}
 \left(\prod_{j=1}^{12}a_{n_j}(T)\right)
 \operatorname{Re}\widehat w(-T\Delta)\ge cT^{5/2},
 \quad \Delta=\sum_{j=1}^6\sqrt{n_j}-\sum_{j=7}^{12}\sqrt{n_j}.
                                                               \tag{A1}
\]

All indices are ordered, repetitions are permitted, and the exact
frequencies Delta=0 have been removed. Thus the full all-sign termwise
absolute majorant, with prefactor T/2^12, is at least c' T^(5/2), even
when its exact-frequency part is deleted. It cannot be bounded by
O_epsilon(T^(1+2eta+epsilon)) for every epsilon>0 if eta<3/4.

This is a no-go for that majorant only. It is not a lower bound for
the full signed finite-window moment or its complete offdiagonal.
It does not reject any true low-moment theorem, the actual twelfth-
moment target, a pointwise bound, or any M1/M2 obligation.

## Proof: physical mass on a positive band

Continuity at zero permits fixed 0<a<b with Psi(sqrt(u))>=1/2 for
all u in [a,b]. The union of unit squares centered at lattice points
of a disk of radius R lies in B_(R+sqrt(2)/2) and covers
B_max(R-sqrt(2)/2,0). Comparing areas proves
N(R)=pi R^2+O(R+1), uniformly in real R, with inclusive boundaries.
Consequently

\[
 \sum_{aT<n\le bT}r_2(n)
 =\pi(b-a)T+O(\sqrt T+1)\gg T.
\]

Using the open lower endpoint avoids any need to subtract an atom;
this set is contained in I_T, and every extra atom is nonnegative.
It follows that

\[
 M_T:=\sum_{n\in I_T}a_n(T)
 \ge\tfrac12(bT)^{-3/4}\sum_{aT<n\le bT}r_2(n)
 \gg T^{1/4}.                                                  \tag{A2}
\]

Since w>=0 is nonzero, w-hat(0)>0. Continuity provides h>0 with
Re w-hat(xi)>=w-hat(0)/2 for |xi|<=h. This assertion neither requires
nor asserts that w-hat is nonnegative or real at other frequencies.

## Proof: ordered weighted pairs and removal of exact frequencies

For each ordered six-tuple n in I_T^6 put
s(n)=sum_(j=1)^6 sqrt(n_j), v(n)=product_(j=1)^6 a_(n_j)(T).
These sums lie in an interval of length at most
6(sqrt(b)-sqrt(a))sqrt(T). Partition that interval into half-open
bins of length h/T, with a final endpoint bin if necessary. The
number J is at most C_(a,b,h) T^(3/2), for T>=2. Let v_l be the total
six-tuple weight in bin l. Every tuple belongs to exactly one bin and
sum_l v_l=M_T^6. Weighted Cauchy gives

\[
 \sum_{\substack{\mathbf n,\mathbf m\in I_T^6\\
       |s(\mathbf n)-s(\mathbf m)|\le h/T}}v(\mathbf n)v(\mathbf m)
 \ge\sum_{l=1}^J v_l^2
 \ge J^{-1}M_T^{12}\gg T^{3/2}.                              \tag{A3}
\]

No permutation factor is missing: the two six-tuples are ordered and
their ordered pair is exactly an ordered twelve-tuple. Tuples in
different bins can add terms to the left but are not needed.

The Schwartz function Psi is bounded by some fixed C_Psi. The actual
weights have the common envelope
|a_n(T)|<=4 C_Psi tau(n)n^(-3/4), by the two-square identity.
The accepted `GC-weighted-square-root-exact-resonance-mass` lemma
bounds the entire exact twelve-root absolute mass by a fixed constant,
uniformly in T and cutoff. In particular the balanced-sign exact
subsum in A3 is O(1). Its deletion leaves at least c_0 T^(3/2)-C,
which is >=(c_0/2)T^(3/2) for sufficiently large T. Every remaining
summand is nonnegative and Re w-hat(-T Delta)>=w-hat(0)/2.
Multiplying by T proves A1.

## Consequence for the actual Fourier majorant

At each fixed T the sequence a_n(T) is absolutely summable, by Schwartz
decay and the divisor bound. Thus the all-sign twelve-fold moment
expansion is absolutely convergent at fixed T. Its termwise absolute
majorant is

\[
 \mathfrak A_{12}(T)=\frac{T}{2^{12}}
 \sum_{\epsilon\in\{-1,1\}^{12}}
 \sum_{\substack{n_j\ge1\\ \sum_j\epsilon_j\sqrt{n_j}\ne0}}
 \prod_j|a_{n_j}(T)|\,
 \left|\widehat w\!\left(-T\sum_j\epsilon_j\sqrt{n_j}\right)\right|.
\]

Retaining just one six-plus/six-minus pattern and the band from A1
gives A_12(T)>=2^(-12)cT^(5/2). Its cosine phase is one because the
sign sum is zero. Other terms of this absolute majorant are nonnegative.
For eta<3/4 choose epsilon in (0,3/2-2eta); the asserted target exponent
is smaller than 5/2, so such a uniform upper bound is impossible.

The same argument at order 2k, k>=2 fixed, gives the nonzero positive
band subsum >=c_k T^((k-1)/2)-C_k T. For k>=4 the leading term dominates;
for k=2,3 this reasoning gives no positive asymptotic lower bound after
exact-frequency deletion. In particular it does not conflict with
the second-moment control, and at orders eight and above it tests a
termwise absolute proof strategy rather than the known signed moments.

## A control explaining why the signed conclusion is different

The subsum in A1 has positive real Fourier weight, but other differences
can have negative real weight or nontrivial cosine phase. The full
displaced moment has not been bounded below by discarding them.
Indeed choose any fixed nonnegative nonzero f in C_c^infinity((a,b))
and set F_T(R)=T^(1/4) integral f(u)e(R sqrt(T) sqrt(u))du.
On R comparable to T, repeated integration by parts gives
F_T(R)=O_A(T^(1/4)(R sqrt(T))^(-A)), since the phase derivative in u
never vanishes. Thus its displaced twelfth moment decreases faster
than any prescribed negative power of T. At |R|<=c/sqrt(T), however,
its modulus is comparable to T^(1/4), producing order T^(5/2)
in the unweighted moment near the origin. The same positive close-pair
bin argument applies to its continuous frequency measure.
This control demonstrates the possibility of the requisite Fourier
cancellation. It is not an approximation theorem for the discrete
arithmetic coefficients.

## Dependencies and first open step

The proof uses elementary disk area counting, the accepted two-square
identity, divisor bound, and the full exact-resonance lemma of Round201.
No numerical experiment, asymptotic conjecture, or external source is
used. The independent statement-only report and subsequent kernel
seam review are recorded in the Round202 campaign.

The remaining analytic problem is a coefficient-preserving estimate
of the complete signed displaced sum, or a complete signed cutoff-tail
estimate. The lower bound above supplies neither. A new strategy must
retain cancellations lost by termwise absolute Fourier estimation.
