# Round217 actual twelve-distinct-class frequency control

## 1. Result

Conductor analytical control, NONBLIND, 2026-09-28.
Campaign:gc-full-goal-distinct-source-review. Starting graph SHA256:
f7c8b74e9acaa3bf5234c3678f20e2aaf8dbb9ba6179f73d839fa2f0537a14d7.

The actual twelve-distinct-class kernel can contain nonzero frequencies
with T|Delta| tending to zero. This statement holds after the cutoff
Q=floor(T^alpha) for every fixed 0<=alpha<1/2, including alpha=2/5.
The construction uses actual positive r2 coefficients and twelve distinct
squarefree classes; no cancelling repeated-class padding is used.
It refutes only a proposed uniform frequency-separation inference.
Its entire displayed family's absolute mass is negligible, so it is
not a no-go result for the remaining signed moment estimate.

## 2. Exact hypotheses and family

Use the fixed actual mollifier and weight of accepted216. For each
j in{1,3,5}, take four squared offsets

    a=j^2, 16j^2, 49j^2, 64j^2,

with signs respectively +,-,-,+. These twelve a's are pairwise
distinct:1,16,49,64,9,144,441,576,25,400,1225,1600.
For integers m in[M,2M], put n_a=m^2+a. Each n_a is a sum of two
integer squares and therefore has r2(n_a)>0. Let T=C0 M^2, where
C0 is one sufficiently large fixed constant, and Q=floor(T^alpha).
The actual term uses a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)).

## 3. Proof and complete cost

For a fixed positive a and fixed positive integer d, solutions
m^2+a=d s^2 with m in[M,2M] have distinct ratios m/s. Otherwise
s^2(d-(m/s)^2)=a would force identical s and m. For M>=sqrt(a),
the ratios lie in an interval of width at most a sqrt(d)/(2M^2),
while s<=3M/sqrt(d) makes distinct ratios at least d/(9M^2) apart.
There are at most1+9a/(2sqrt(d)) solutions for this d. Consequently

    #{m in[M,2M]: sf(m^2+a)<=Q} <<_a Q.

Sum this bound over the twelve fixed offsets. Since alpha<1/2,
Q=O(M^(2alpha))=o(M), so all but o(M) integers m retain all twelve
indices in the large-class tail. This is an elementary ratio-spacing
argument, not an assumption about squarefree values of polynomials.

For large M their squarefree classes are pairwise distinct. If
n_b=d t^2 and n_a=d s^2 had the same d, with b>a, then t>s and

    b-a=d(t-s)(t+s)>=2M sqrt(d)>=2M,

contradicting b-a<=1599. Thus this distinctness holds for all sufficiently
large m, independently of the exceptional-set count.

In each four-offset group the signs sum to zero and the signed sum of
the offsets is j^2(1-16-49+64)=0. The signed sum of their squares is
j^4(1-256-2401+4096)=1440j^4. The fixed Taylor expansion gives

    Delta_m=sum_a epsilon_a sqrt(m^2+a)
           =-180(1^4+3^4+5^4)m^-3+O(m^-5)
           =-127260m^-3+O(m^-5).

It is negative and nonzero for large m, and T Delta_m=O(M^-1)->0.
There are exactly six positive and six negative signs, so the original
cosine coefficient e(-3 sum epsilon_a/8) equals1. Every class occurs
once, with its genuine positive harmonic s in n_a=d_a s_a^2.

Since Psi(0)=1 and is continuous, choosing fixed C0 sufficiently large
ensures Psi(sqrt(n_a/T))>=1/2 for all these m and offsets, once M
is large. Hence the coefficients are actual and positive. Continuity
of w-hat and w-hat(0)>0 gives w-hat(-T Delta_m)->w-hat(0), although
the displaced Fourier transform need not be real at nonzero arguments.
No cancellation from other tuples has been excluded.

The size of this family is explicitly harmless. For every eta>0,
the divisor bound gives a_(n_a)(T)<<_eta M^(-3/2+eta).
There are O(M) selected m, and boundedly many orderings/sign variants.
Even summing the absolute Fourier contributions with the factor T gives

    T sum_m product_a |a_(n_a)(T)| |w-hat(-T Delta_m)|
                     <<_epsilon T^(-15/2+epsilon).

The exponent is T*M*M^-18=M^-15. Thus this sparse family does not
exhaust, challenge, or lower-bound the full target T^(29/25+epsilon).

## 4. First doubtful or unproved step

The adequate signed estimate for the complete distinct-class kernel
remains open. A uniform claim that every distinct-class frequency has
T|Delta| bounded away from zero is false by this construction. A
weighted estimate that includes such rare near relations may still
be true. No positive-certificate obstruction for all distinct tuples
is established here.

## 5. Controls and outcomes

All twelve offsets are distinct positive squares. The signs balance
6 against6, cancel the leading two Taylor levels, and retain a nonzero
cubic inverse-power term. Actual norm multiplicities and positive
mollifier values are verified. The cutoff survives for every fixed
alpha<1/2 by a uniform O(Q) exceptional count. There are no repeated
classes or artificial cancelling pairs. The absolute contribution is
priced rather than mistaken for an obstruction. All checks are
analytical; no numerical experiment or source theorem is needed.

## 6. Dependencies and exact artifacts used

Read protocol.md, state/proof_obligations.yml, the frozen217 strategy
and manifest, accepted proofs/kernels/gc_complete_distinct_radical_moment_reduction.md,
and closed216 controls/conductor_radical_ledger.md with its independent
actual-binding review. The elementary ratio-spacing argument is fully
reproduced and now applied to twelve distinct offsets. The actual
coefficient divisor bound and mollifier normalization are the same
accepted dependencies. No external theorem or sibling report is used.

## 7. Recommended state effect

Retain as a scoped actual-frequency control after independent review.
Do not promote or reject the distinct-class moment target from it.
It supplies an admissible control family for source hypothesis audits
and future cancellation estimates. No graph, proof-draft or successor
change follows without the conductor's separate closure decision.
