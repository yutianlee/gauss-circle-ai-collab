# Round 201 conductor: exact resonance and moment bridge

Campaign: gc-whole-discrepancy-twelfth-moment. Date: 2026-09-23.
Starting graph hash: 2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5.
Role: conductor independent analytical derivation; candidate evidence.
Context: protocol, active manifest, authoritative divisor and exponent
nodes, requested strategy review, closed Round-200 synthesis. This
derivation does not use the blind report. No numerical evidence.

## 1. Exact weighted resonance bound

Write each positive integer uniquely as n=d s^2, d squarefree, s>=1.
For nonnegative weights b_n let A_d=sum_s b_(d s^2), and assume
S=sum_d A_d^2<infinity. For each fixed integer k>=2,

\[
 \sum_{\epsilon\in\{-1,1\}^k}
 \sum_{\sum_j\epsilon_j\sqrt{n_j}=0}\prod_j b_{n_j}
 \le 2^k B_k^{(\ge2)} S^{k/2},
\tag{201.C1}
\]

where B_k^(>=2) is the finite number of set partitions of {1,...,k}
whose blocks all have size at least two.

To justify the algebraic premise, for distinct primes p_1,...,p_r,
inductively Q(sqrt(p_1),...,sqrt(p_r)) has the monomial basis sqrt(p_I)
and independent sign-change automorphisms. Given this at r-1, if an
element z in that field has z^2=q rational nonzero, every existing
automorphism sends z to plus or minus z. Expanding z in the monomial
basis shows it is a common eigenvector. The monomials have distinct
sign characters, so only one coefficient is nonzero: q=c^2 p_I.
The distinct new prime p_r is not in one of these rational square
classes, by its valuation. Therefore X^2-p_r is irreducible over the
old field, the basis doubles, the old sign maps extend, and the new
sign flip exists. This proves the induction and rational independence
of all distinct squarefree radicals, including sqrt(1)=1.

Consequently a radical resonance satisfies
sum_(j:d_j=d) epsilon_j s_j=0 for each d. Every occupied class contains
at least two indices. Partition the k labels by their squarefree class.
For each resulting partition, drop the remaining sign equations and
the distinctness restriction on assigned d's, increasing a nonnegative
sum. For a block of size h>=2 the sum is sum_d A_d^h <= S^(h/2), since
sup_d A_d<=sqrt(S). Multiplication over blocks and summation over signs
and partitions proves (201.C1). Truncation followed by monotone
convergence extends the statement to infinite weights. No pairing-only
classification or finite-radius independence assumption is used.

If b_n<=C tau(n)n^(-3/4), submultiplicativity of tau gives

\[
 A_d\le C d^{-3/4}\tau(d)
       \sum_{s\ge1}\tau(s^2)s^{-3/2}.
\]

Both the inner sum and sum_d d^(-3/2)tau(d)^2 converge by the elementary
divisor bound, choosing a fixed sufficiently small exponent. Thus S is
bounded by a constant depending only on C, and (201.C1) is uniform in
all cutoffs and all unequal index ranges. The actual circle weights
obey this envelope because r_2(n)=4 sum_(d|n)chi_4(d) <=4 tau(n) and
the fixed radial Fourier cutoff is bounded.

## 2. Exact versus nonzero differences

The conclusion is strictly an exact-resonance result. For instance
5+7=6+6 gives a nonpairing resonance at n=(25,49,36,36); pairing
multisets alone would omit it. Padding with cancelling pairs gives an
example at order twelve with positive actual r_2 coefficients.

Conversely sqrt(s^2+1)-s is nonzero and tends to zero. Its two terms
have different squarefree classes; the no-singleton argument no longer
applies. Both integers s^2 and s^2+1 have representations by two
squares. This is a scope control, not a large contribution or lower
bound for a complete physical moment.

For real cosine coefficients the total exact term in an even moment
is a nonnegative torus constant coefficient, although individual
expanded terms can have nontrivial phases. Its absolute mass is bounded
by (201.C1); multiplying by the smooth radius integral costs O(T).
It gives no estimate for the nonzero-frequency part on a displaced
finite radius window.

## 3. Moment-to-pointwise persistence

Let P(X)=N(sqrt(X))-pi X with the inclusive count. Monotonicity gives
P(X+h)>=P(X)-pi h and P(X-h)<=P(X)+pi h. If V=|P(X)|, one appropriate
one-sided interval of length V/(2pi) therefore has |P|>=V/2, with the
endpoint convention preserved. For X in [Y,2Y], any available sublinear
bound, including the accepted pointwise benchmark, places this interval
inside [Y/2,3Y] for all sufficiently large Y. Bounded Y is absorbed.
Hence, for any fixed p>0,

\[
 \frac{V^{p+1}}{2^{p+1}\pi}
 \le\int_{Y/2}^{3Y}|P(x)|^pdx.
\]

An upper moment Y^(1+p/4+eta+epsilon) gives the pointwise exponent
(1+p/4+eta)/(p+1)=1/4+(3/4+eta)/(p+1). For p=12 the exponent is
(4+eta)/13. Improvement of the accepted theta_LY requires
eta<13theta_LY-4. Arbitrarily large fixed sharp moments give the quarter
target after choosing p depending on the requested epsilon; a single
twelfth moment does not give the quarter theorem.

## 4. Exact interpolation ledger

If an independently verified absolute qth moment is sharp,
int|P|^q << Y^(1+q/4+epsilon), with q<=12, then the accepted pointwise
theta bound implies only

\[
 \int|P|^{12}\ll Y^{4+(12-q)(\theta-1/4)+\epsilon}.
\tag{201.C2}
\]

The threshold for such an interpolation to improve theta is
q>(1-theta)/(theta-1/4). A signed odd-moment asymptotic is not an
absolute moment input. The exact q and source hypotheses must come
from the primary-source audit; they are not supplied by this algebra.

## 5. State scope

(201.C1) is a candidate self-contained finite kernel suitable for
independent review. The smoothing/moment identity and primary-source
benchmark require separate source and normalization reviews. No
twelfth-moment or pointwise exponent improvement has been proved by
this document, and no M1/M2 parent is discharged.
