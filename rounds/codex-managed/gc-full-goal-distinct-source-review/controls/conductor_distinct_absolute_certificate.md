# Round217 complete actual distinct-class absolute-certificate obstruction

## 1. Result

Conductor analytical candidate, NONBLIND, 2026-09-28.
Campaign:gc-full-goal-distinct-source-review. Starting graph SHA256:
f7c8b74e9acaa3bf5234c3678f20e2aaf8dbb9ba6179f73d839fa2f0537a14d7.

The termwise absolute Fourier certificate remains too large even after
restricting every tuple to pairwise distinct large squarefree classes.
For every fixed even p>=4 and fixed 0<=alpha<1, Q=floor(T^alpha),
one balanced sign pattern already gives certificate at least

    c_(p,alpha,rho,w) T^(p/4-1/2)

for all sufficiently large real T. At p=12 this is T^(5/2), exceeding
the target29/25. This is an actual-coefficient obstruction to the named
positive certificate. It is not a lower bound on I_p, a physical moment,
or the high-value tail, and does not reject signed correlation methods.
Independent final-hash review is required before any state effect.

## 2. Exact statement and hypotheses

Use the actual fixed nonnegative real radial smooth unit-mass mollifier,
Psi(s)=rho-hat(s e1), and fixed nonnegative smooth w supported in[1/2,2]
with integral positive. Put a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),
e(t)=exp(2pi i t), and w-hat(xi)=integral w(u)e(-u xi)du.

For a sufficiently small fixed c>0, restrict to

    N_T={integer n:cT<=n<=2cT, sf(n)>Q}.

Psi is positive and at least1/2 on this interval, so its a_n are
nonnegative. Zero representation counts cause zero weights. For
p=2k>=4, define the restricted balanced positive certificate

    A_(p,Q)(T)=T 2^-p
      sum_(n_1,...,n_p in N_T; sf(n_i) pairwise distinct)
        product_i a_(n_i)(T)
        |w-hat(-T[sum_(i<=k)sqrt(n_i)-sum_(i>k)sqrt(n_i)])|.

It is a subset of the full termwise absolute distinct-class Fourier
expansion. The theorem concerns exactly this quantity. Each ordered
index tuple corresponds uniquely to its squarefree labels and positive
harmonics in the class expansion. No s is reinterpreted or truncated
in the full certificate; a positive subcollection is selected for a
lower bound. The finite block and real endpoints are literal.

## 3. Proof and complete multiplicity ledger

### A. Actual retained coefficient mass

The elementary unit-square comparison gives N(R)=pi R^2+O(R+1).
It follows, including real interval endpoints, that
sum_(cT<=n<=2cT)r2(n) is comparable to T for large T. Since
n^(-3/4) is comparable to T^(-3/4) and Psi>=1/2 there, the full
positive block mass is comparable to T^(1/4).

The actual complete small-class mass is at most C Q^(1/4), by
r2(d s^2)<=r2(d)tau(s^2), the convergent s^(-3/2) divisor sum,
and sum_(d<=Q)r2(d)d^(-3/4)<<Q^(1/4). Removing small classes
therefore costs o(T^(1/4)) when alpha<1. Write

    M_T=sum_(n in N_T)a_n(T) as comparable to T^(1/4).      (1)

The upper bound also follows by the same positive block count and
|Psi|<=1; it has no T^epsilon loss.

### B. A block-specific same-class pair bound

For squarefree d, define the retained block class mass

    A_d=sum_(s>=1:d s^2 in N_T)a_(d s^2)(T).

It vanishes unless d<=2cT. The number of such s is at most
C_c sqrt(T/d); the possible additive1 is absorbed since nonempty
classes have d<=2cT. The divisor bound and |Psi|<=1 imply, for
arbitrarily small fixed eta>0,

    a_n(T)<<_eta T^(-3/4+eta),
    A_d<<_eta T^(-1/4+eta)d^(-1/2),
    S2:=sum_d A_d^2<<_eta T^(-1/2+3eta).                (2)

The last estimate sums d^-1 up to2cT and absorbs its logarithm.
There is no squarefree-density assumption. The estimate holds if
further indices are deleted. It includes all pairs with the same
squarefree class, whether their harmonics coincide or differ.

### C. Many close balanced tuples before excluding repeated classes

Choose delta>0 fixed so that |w-hat(xi)|>=w-hat(0)/2 for |xi|<=delta.
This uses continuity and w-hat(0)>0, not evenness of the window.
Place the product weight of every ordered k-tuple from N_T at its
root sum. The total mass is M_T^k and its root sums lie in an interval
of length O_(k,c)(sqrt(T)). Partition it into half-open bins of width
delta/T, with at most C_(k,c,delta) T^(3/2) bins. If their masses
are mu_j, Cauchy--Schwarz gives

    sum_j mu_j^2 >= (M_T^k)^2 / (#bins)
                         >> T^(p/4-3/2).                (3)

Every same-bin pair of k-tuples is an ordered balanced p-tuple with
|Delta|<=delta/T. Thus (3) is a lower bound for its weighted mass.
No distinctness has yet been imposed.

### D. Every repeated-class close tuple is a smaller error

Fix two distinct positions u,v whose squarefree labels coincide.
Since p>=4, choose one other position ell different from u,v to leave
unsummed until last. Fix the n at u,v and at all p-3 positions other
than u,v,ell. The condition |Delta|<=delta/T confines sqrt(n_ell)
to an interval of length2delta/T. On cT<=n_ell<=2cT, the corresponding
n interval has length at most C_(c,delta)T^(-1/2), hence less than1
for large T. There is at most one integer n_ell, regardless of whether
it has an allowed representation or squarefree label. Its weight is
at most the first bound in(2).

Consequently the weighted close mass for this fixed pair of positions
is at most

    S2 * M_T^(p-3) * max_(n in N_T)a_n(T)
                  <<_epsilon T^(p/4-2+epsilon).          (4)

The same-class pair contributes exactly sum_d A_d^2 after dropping
all other restrictions. The p-3 fixed arbitrary positions contribute
M_T^(p-3); the remaining single position contributes the maximum
weight rather than another full coefficient mass. This accounts for
all p positions. Signs do not affect the interval-length bound because
the coefficient of sqrt(n_ell) is +1 or -1.

Union over the binomial(p,2) possible equal-class pairs covers every
tuple with any repeated class, including multiple repeats and all
within-class harmonic relations. Overcounting is harmless because
all weights are nonnegative. Choose epsilon<1/2. Subtracting(4)
from(3) leaves at least c_p T^(p/4-3/2) in close tuples whose
squarefree classes are all distinct.

### E. Restore the actual Fourier factor

For those remaining tuples, |w-hat(-T Delta)|>=w-hat(0)/2.
Multiplication by T 2^-p proves

    A_(p,Q)(T)>>T^(p/4-1/2).                            (5)

The original balanced cosine phase is e(-3(k-k)/8)=1; the positive
certificate still takes the modulus of its Fourier factor. Distinct
squarefree radicals are rationally independent, so Delta is never
zero for these tuples. Thus no exact-frequency term has to be removed
after the distinctness restriction. This uses independence only to
classify zero frequencies, not to estimate their nonzero separation.

## 4. First doubtful or unproved step

The required cancellation of the complete signed I_p remains unproved.
Equation(5) shows that its termwise absolute Fourier certificate cannot
have the desired smaller power, already on this positive block and one
balanced sign pattern. Other signed terms, signs or frequency ranges
can cancel the selected near contribution. No lower bound for the
signed total is inferred. The case alpha>=1 is outside the statement;
the retained block mass argument then need not apply.

## 5. Controls and outcomes

All coefficients are actual. The head removal costs Q^(1/4), with
alpha<1 explicitly required. The sharper S2 is a same-block bound,
not an unproved improvement of the whole-class estimate. One remaining
integer is justified by the physical width1/T and n~T; its weight and
the p-3 other indices are all priced. The union over every repeated
pair removes all multiplicities, not only repeated norms. Real endpoints,
half-open bins, zero coefficients, all harmonics in the selected block
and actual distinct labels are respected. At p=4 the bound is T^(1/2),
which does not exceed a target T; at p=12 it is T^(5/2). This is a
positive-certificate no-go only. No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Read protocol.md, the current graph and frozen217 manifest/strategy,
the accepted distinct-class reduction and exact-resonance kernel,
and the closed216 conductor ledger and its actual-binding review.
The elementary coefficient head bound, lattice count and divisor bound
are the existing actual inputs. The block-specific pair estimate and
last-index subtraction are derived above. No new external theorem,
current sibling report, random model or unverified computation is used.

## 7. Recommended state effect

After independent exact-hash review, retain or narrowly promote this
actual distinct-class positive-certificate obstruction. It extends the
old whole-tail certificate control to precisely the remaining interface.
Do not reject H216, I_p, signed correlations or the quarter goal.
Use it to avoid selecting an absolute higher-root spacing bound as the
next complete closure unless the original oscillatory kernel is first
used to recover a saving.
