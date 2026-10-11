## 1. Result and review verdict

**GREEN for both exact claimant artifacts, with no required correction.**

Round217, campaign `gc-full-goal-distinct-source-review`; reviewer
`distinct_correlation_sources`; bounded independent mathematical review,
explicitly **NONBLIND**. Date:2026-09-28, Asia/Shanghai. Starting graph:
`f7c8b74e9acaa3bf5234c3678f20e2aaf8dbb9ba6179f73d839fa2f0537a14d7`.
Analytical/algebraic effort100%; numerical experiments zero.

The exact reviewed claimant hashes, rechecked before reading, are:

- `controls/conductor_distinct_absolute_certificate.md`:
  `603aa69cb4b757707d6eb89bb8290b05190b6b6d5cae83be52ddc19658ef68bb`.
- `controls/conductor_distinct_frequency_control.md`:
  `9ac60977966c4368427daa62a4ebd16ac7e56ca60b291e02186a26d81cea4efa`.

The first proves an actual-coefficient lower bound for precisely the
termwise absolute distinct-class Fourier certificate. Its subtraction
of every repeated-class configuration is complete. The second supplies
twelve genuine distinct large squarefree classes with T|Delta| tending
to zero, while correctly bounding the displayed family's total
contribution by a negligible power. Neither result bounds the complete
signed integral from below or rejects the desired moment estimate.

## 2. Exact statements and hypotheses checked

The common inputs are the accepted actual coefficients

    a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),

with the fixed nonnegative radial smooth unit-mass mollifier, its real
Schwartz transform Psi, and a fixed smooth nonnegative positive-radius
window w with integral positive. T is real. The representation counts,
harmonics and Fourier convention agree with accepted216.

For each fixed even p=2k>=4 and fixed 0<=alpha<1, set
Q=floor(T^alpha). The first claim selects a sufficiently small fixed
positive c and the block cT<=n<=2cT with sf(n)>Q. For one balanced
sign pattern, the ordered p-fold sum of the actual nonnegative block
weights times T 2^-p |w-hat(-T Delta)|, restricted to all classes
distinct, is bounded below by a positive constant times
T^(p/4-1/2) for all sufficiently large real T. The constants may
depend on fixed p,alpha,c,rho,w; no order growing with T is asserted.

The frequency claim fixes the twelve offsets

    {1,16,49,64,9,144,441,576,25,400,1225,1600}

from j^2 times {1,16,49,64}, j=1,3,5, with signs +,-,-,+ in
each group. It uses n_a=m^2+a, m in[M,2M], T=C0 M^2 for a
sufficiently large fixed C0, and Q=floor(T^alpha) with fixed
0<=alpha<1/2. It asserts a family of actual retained distinct terms,
not a lower bound of target size or a statement for alpha>=1/2.

## 3. Independent derivation of the two controls

**Positive retained block mass.** Since Psi(0)=1 and Psi is continuous,
c can be fixed so Psi(sqrt(n/T))>=1/2 on the whole block. The
elementary disk count gives

    sum_(cT<=n<=2cT) r2(n)=pi cT+O_c(sqrt(T)+1).

Changing open/closed endpoints changes only the boundary error at
this precision. Multiplication by n^(-3/4) and the fixed positive
transform gives a full block mass comparable to T^(1/4), above
and below without an epsilon loss. The accepted actual small-class
L1 bound is O(Q^(1/4)); deleting these classes costs o(T^(1/4))
for every fixed alpha<1. This includes alpha=0, where Q=1.
Thus M_T, the retained mass, remains comparable to T^(1/4).
No density theorem about represented squarefree numbers is required.

**Block class energy.** For any nonempty class d, d<=2cT and the
number of s with cT<=d s^2<=2cT is O_c(sqrt(T/d)); its endpoint
additive constant is absorbed because sqrt(T/d) is bounded below
for nonempty classes. For arbitrarily small eta>0,

    max_n a_n <<_eta T^(-3/4+eta),
    A_d <<_eta T^(-1/4+eta)d^(-1/2),
    sum_d A_d^2 <<_eta T^(-1/2+3eta).

The last line follows from the harmonic sum over d<=2cT; restricting
to squarefree d or deleting more indices only decreases it. A_d^2
counts every ordered same-class pair, including different harmonics.
This sharper bound belongs to this one norm block and is not an
improvement of the complete infinite-class energy.

**Close tuples and subtraction.** Continuity at zero gives delta>0
with |w-hat(xi)|>=w-hat(0)/2 for |xi|<=delta. The ordered k-root
sums occupy an interval of length O_(p,c)(sqrt(T)). Half-open bins
of width delta/T, including a possibly partial endpoint bin, require
O_(p,c,delta)(T^(3/2)) bins. Their total weight is M_T^k. Cauchy
therefore gives same-bin pair weight at least

    c M_T^(2k) T^(-3/2) >> T^(p/4-3/2).                 (R1)

Pairing the two ordered k-tuples is exactly the chosen ordered
balanced p-tuple; no factorial division is missing.

For any specified pair of positions u,v with a common class, leave
a third position ell to be summed last. There are p-3 unrestricted
positions other than u,v,ell. Once these and the same-class pair are
fixed, |Delta|<=delta/T restricts sqrt(n_ell) to an interval of length
2delta/T. On the block, squaring expands this to an interval of length
O_(c,delta)(T^(-1/2)), eventually less than one. Hence at most one
integer is possible; its weight costs max_n a_n rather than M_T.
The sign at ell is irrelevant to this length estimate. Consequently,

    bad mass for this pair
      <= (sum_d A_d^2) M_T^(p-3) max_n a_n
      <<_epsilon T^(p/4-2+epsilon).                    (R2)

This prices exactly 2+(p-3)+1=p positions. Summing over the fixed
binomial(p,2) pairs removes every tuple with any repeated class,
regardless of further repetitions or harmonic identities. Although
(R1) counts only same-bin pairs, (R2) bounds the larger set of all
close repeated tuples, so the subtraction is valid. Choosing input
epsilon<1/2 makes (R2) smaller by a fixed positive power than (R1).
Multiplying the remaining mass by T 2^-p and the positive Fourier
modulus proves the claimed T^(p/4-1/2) lower bound.

Every retained ordered tuple maps uniquely to d_i=sf(n_i) and its
positive integer harmonic s_i. Since the full termwise absolute
series has nonnegative summands, omitting all other blocks, signs
and Schwartz tails is legitimate for this lower bound. Distinct
classes exclude exact zero frequencies by radical independence.

**Actual near-frequency family.** For fixed a>0 and d>=1, solutions
of m^2+a=d s^2 in[M,2M] have distinct rational numbers m/s. The
identity (m/s)^2=d-a/s^2 proves uniqueness of s if m/s is fixed.
For M>=sqrt(a), their ratios lie in an interval of width at most
a sqrt(d)/(2M^2). Also s<=3M/sqrt(d); two distinct ratios differ
by at least 1/(s s')>=d/(9M^2). The number of solutions is therefore
at most 1+9a/(2sqrt(d)). Summing over d<=Q, even without squarefree
restriction, gives O_a(Q). Across all twelve fixed offsets the same
O(Q) bound holds. Since Q=O(M^(2alpha))=o(M) for alpha<1/2,
there remain comparable to M choices with all classes above Q.

If two offsets b>a had a common class, writing
m^2+b=d t^2 and m^2+a=d s^2 gives t>s and

    b-a=d(t-s)(t+s)>=2m sqrt(d)>=2M.

This contradicts b-a<=1599 for sufficiently large M. Thus all twelve
classes are distinct, even before deleting the small-class exceptions.
Every n_a is represented by m^2 plus a genuine integer square.

For each group the signed sums of 1 and a vanish, while the signed
sum of a^2 is 1440j^4. The uniform Taylor expansion at large m gives

    Delta_m=-180(1+81+625)m^-3+O(m^-5)
           =-127260m^-3+O(m^-5).

Thus Delta_m is nonzero and negative, and T Delta_m=O(M^-1)
uniformly for m in[M,2M]. Fixed sufficiently large C0 places every
sqrt(n_a/T) in Psi's positive neighborhood. There are six plus and
six minus signs, making the cosine phase coefficient one. The
displaced Fourier values tend to w-hat(0)>0 but need not be real
at finite nonzero arguments; this causes no inference about the
other signed terms.

Finally each coefficient is O_eta(M^(-3/2+eta)). There are O(M)
parameters and only boundedly many order/sign variants, so their
absolute Fourier contribution, including the full factor T, is

    O_epsilon(M^2 M M^-18 M^(2epsilon))
                   =O_epsilon(T^(-15/2+epsilon)).       (R3)

Input divisor exponents are chosen small enough before multiplying
the twelve factors. Any accidental duplication between parameter
values only enlarges this upper certificate and cannot invalidate it.

## 4. First doubtful or unproved step

No unproved step was found inside either stated claim at the pinned
hashes. The unresolved step remains cancellation in the complete
signed I_p. The first result lower-bounds the sum of moduli; the
second only disproves uniform separation at physical resolution.
Neither lower-bounds the signed integral or its high-value part.

The parameter restrictions are essential to these proofs. At alpha=1
the head deletion need not be negligible in the selected block; at
alpha=1/2 the frequency-family exceptional count need not be o(M).
For p=2 the repeated-pair last-index argument is unavailable. None
of those excluded endpoints is asserted. No new source theorem or
probabilistic independence claim is used.

## 5. Controls and outcomes

| Seam | Verdict |
|---|---|
| Actual mass after class cutoff | GREEN: positive transform block, elementary representation count, O(Q^(1/4)) head deletion. |
| Same-block class energy | GREEN: all harmonics counted; additive endpoint constants absorbed; logarithm priced. |
| Close-root bins | GREEN: O(T^(3/2)) bins, ordered weights and displacement retained. |
| All repeated classes | GREEN: every pair covered; exactly one final integer; p-3 unrestricted positions. |
| p and alpha ranges | GREEN: fixed even p>=4; alpha<1 for the certificate, alpha<1/2 for the explicit family. |
| Fourier and sign scope | GREEN: continuity uses the actual complex Fourier transform; the certificate alone is positive. |
| Twelve distinct actual indices | GREEN: twelve distinct square offsets, common-class contradiction, no artificial padding. |
| Small-frequency expansion | GREEN: cancellations, coefficient127260, and T Delta=O(M^-1) checked algebraically. |
| Family's total cost | GREEN: T times O(M) twelvefold weights gives T^(-15/2+epsilon). |
| Complete target distinction | GREEN: no implication to a moment lower bound, target rejection or quarter proof. |

The p=4 absolute-certificate power is T^(1/2), consistent with a
complete fourth-moment upper bound of order T. At p=12 it is
T^(5/2), which excludes the smaller T^(29/25) termwise absolute
certificate directly on the distinct-class interface. These checks
are exact exponent comparisons, not numerical experiments.

## 6. Dependencies and provenance

Read the two exact claimant files listed in section1 and only the
already permitted context: protocol, current graph/manifest/frozen217
strategy, the214 checkpoint, closed216 synthesis, accepted complete
large-values and distinct-radical kernels, and exact-resonance kernel.
The arithmetic inputs used here are the elementary representation
identity/divisor bound, elementary disk count, accepted actual head
bound, radical independence, and mollifier normalization.

This is an independent rederivation after reading the claimant, not
a statement-only review. Before this task the reviewer had received
a short conductor outline of the first argument; that outline was
not used in the frozen source report and is now part of the disclosed
nonblind provenance. No sibling or isolated blind packet was read.
The previous source report remains frozen at
`45ec295cc04a23d061f7278015327af9ff7e4884c902c05319fb3629ed64bc59`.
No claimant file was edited and no shared proof state was changed.

## 7. Recommended state effect and corrections

**GREEN; no correction required at either reviewed hash.** Retain
the explicit near-frequency family as an actual admissibility control.
The conductor may retain or narrowly promote the distinct-class
absolute-certificate obstruction after the remaining protocol gates.
Its exact permitted conclusion is failure of the named termwise
absolute Fourier closure, including after the large-class distinctness
restriction. The signed I12 target, full physical moment family,
M1/M2/GAR parents and quarter theorem retain their existing statuses.

This review supplies no State Patch, successor choice or claim of
independent statement-only validation.
