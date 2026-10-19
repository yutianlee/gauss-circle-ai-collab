# Round234: signed disconnected remainder and connected aggregate

Campaign: `gc-connected-cumulant-test`. Task: `signed_connected_attack`.
Role: discovery; selected-context claimant evidence, not accepted mathematics.
Generated: 2026-10-12 Asia/Shanghai. Starting graph SHA256:
`dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306`.
Only the assigned report is written. No sibling report or excluded historical
certificate was read. Analytical derivation is the substantive work; exact
finite diagnostics are auxiliary and do not certify any asymptotic estimate.

## 1. Result: paid disconnected remainder; no new connected saving

With the literal actual functions, full harmonics, cutoff and probability
measure in the frozen interface, the following candidate lemma is proved:

\[
 |D_{12}(T)|\ll_\epsilon T^{1+\epsilon}.                 \tag{1}
\]

More precisely, every proper moment partition containing a singleton or
pair has a rapidly decaying distinct-label absolute sum. Every other proper
partition has block sizes between 3 and 9, and its SIGNED distinct-label sum
is bounded using independent radius variables and exact collision algebra.
No interchange of a signed sum with a sum of moduli is used in (1).

The connected aggregate therefore satisfies

\[
 K_{12}=M_{12}(Z_Q)+O_\epsilon(T^{1+\epsilon}),\qquad
 K_{12}\ge -O_\epsilon(T^{1+\epsilon}),                 \tag{2}
\]

and the available quantitative upper estimate is only

\[
 |K_{12}|\ll_\epsilon T^{1+\epsilon}+T^{10\beta+\epsilon}.
                                                               \tag{3}
\]

Here \(\beta=2\theta_{LY}-1/2>1/8\), so (3) does not meet 29/25.
The one-sided estimate \(K_{12}\ll T^{29/25+\epsilon}\) remains open
and is equivalent, at this paid budget, to the pre-existing complete
twelfth-moment target. The cumulant identity alone gives no further saving.

Independently, this report proves the proposed absolute block estimate

\[
 A_q:=\sum_{d_1,\ldots,d_q>Q}^{*}|m_{[q]}(\mathbf d)|
 \ll_{q,\epsilon}T^{\max(q/4-1,0)+\epsilon},\quad q\ge3
 \text{ fixed}.                                             \tag{4}
\]

Writing \(C_{raw}=TW\sum^*|m_{[12]}|\), its consequence is

\[
 |C_{conn}-C_{raw}|\ll_\epsilon T^{9/4+\epsilon}.           \tag{5}
\]

Thus a separately audited actual full-harmonic lower bound
\(C_{raw}\ge cT^{5/2}\) would imply \(C_{conn}\ge(c/2)T^{5/2}\)
for large T. This is a conditional transfer: this task was not permitted
the historical lower-certificate artifacts and does not certify that premise.
It is never a lower bound for the signed I or K.

## 2. Exact statements and hypotheses

Use precisely the fixed nonnegative real radial smooth unit-mass mollifier
rho and its real even Schwartz transform Psi from accepted216/233; the
fixed nonnegative smooth w is supported in [1/2,2], with W=integral w>0.
For real T>=2 let Q=floor(T^(2/5)) and

    a_n=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    f_d(R)=sum_(s>=1) a_(d s^2) cos(2pi R s sqrt(d)-3pi/4),
    Z(R)=Z_Q(R)=sum_(squarefree d>Q)f_d(R),
    dnu(R)=w(R/T)dR/(TW).

All squarefree tuples are ordered. A star always imposes pairwise
distinctness. Every harmonic s, both cosine signs and the full infinite
Schwartz tail are included. Define

    m_C(d)=E_nu product_(j in C) f_(d_j),
    c_pi=(-1)^(|pi|-1)(|pi|-1)!,
    S_pi=sum_d^* product_(C in pi)m_C(d),
    kappa_12(d)=sum_(pi partition[12]) c_pi product_(C in pi)m_C(d),
    I12=TW sum_d^* m_[12](d),
    K12=TW sum_d^* kappa_12(d), D12=I12-K12.

In particular, the exact sign convention is

    D12=-TW sum_(pi proper partition[12]) c_pi S_pi.        (6)

"Proper" excludes the one-block partition only. No centered replacement
of f_d is made, and no assertion of independence of the actual functions
on a single radius probability space is made. Separate radius variables
are only an exact representation of a PRODUCT of their moments.

The accepted inputs required for (1) are the uniform bounds

    A_d(T)=sum_s |a_(d s^2)| << r2(d)d^(-3/4),
    sum_(d>Q) A_d(T)^h <<_(h,eta) Q^(1-3h/4+eta), h>=2 fixed, (7)
    E_nu |Z|^r <<_(r,epsilon) T^epsilon, 0<=r<=9.            (8)

Bound (8) includes r=0 and 1. It follows from accepted216's actual masked
distribution, actual supremum bound and lower-moment estimate, since
(r-2)beta<=7beta<1 for 2<=r<=9. The normalization divides its unnormalized
O(T^(1+epsilon)) moment by TW. There is no use of a pointwise bound for
arbitrary coefficient masks or finite subsets of the class family.

## 3. Proof and derivation

### 3.1 Convergence, rapid singleton and cross-class pair sums

The divisor bound and Schwartz decay give, for every eta>0,

    S(T):=sum_(n>=1)|a_n(T)| <<_eta T^(1/4+eta),
    sum_(n>T^(3/2))|a_n(T)| <<_M T^(-M) for every M.        (9)

For the second assertion, use a decay order L in
|Psi(sqrt(n/T))|<<_L(n/T)^(-L/2). The upper-tail sum is at most
T^(L/2)(T^(3/2))^(1/4+eta-L/2)
=T^(3/8+3eta/2-L/4); choose L sufficiently large. Thus replacing any fixed
product of at most 12 functions by its n<=T^(3/2) truncation has arbitrarily
rapid total absolute error after multiplying the tail by S(T)^11.
All finite-to-infinite interchanges below are therefore also justified by
the fixed-T uniform absolute convergence S(T)<infinity.

With the Fourier convention w-hat(xi)=integral w(u)e(-u xi)du,

    E_nu e(R lambda)=w-hat(-T lambda)/W.                   (10)

For a singleton, |lambda|=sqrt(n)>=1. For two distinct squarefree classes
and n=d s^2, m=e t^2, one has n!=m. When both n,m<=T^(3/2), every signed
sum has either |sqrt(n)+sqrt(m)|>=2 or

    |sqrt(n)-sqrt(m)|=|n-m|/(sqrt(n)+sqrt(m))
                     >= (1/2)T^(-3/4).                  (11)

Consequently T|lambda|>=(1/2)T^(1/4). The smooth Fourier transform in
(10) decays to every order, while the coefficient totals cost only S or
S^2. Together with (9), this proves, for every M,

    A1=sum_(d>Q)|m_{1}(d)| <<_M T^(-M),
    A2=sum_(d!=e>Q)|m_{1,2}(d,e)| <<_M T^(-M).            (12)

This claim concerns cross-class pairs. Equal-class diagonal pairs are
not rapidly small and have not been discarded from any expansion.

Suppose a proper pi contains a singleton or pair. Take absolute values
of that moment only after representing the exact product; discard the
remaining cross-block distinctness restrictions for an upper bound.
The chosen block sums to A1 or A2, while every remaining position costs
at most S(T). Hence

    sum_d^* product_(C in pi)|m_C(d)| <<_M T^(-M)         (13)

for every M. The polynomial S(T) loss is absorbed by selecting a larger
decay order in (12). This pays all shapes including (11,1) and (10,2).

### 3.2 Exact mixed-radius collision inclusion-exclusion

Now pi={C_1,...,C_b} is proper and every q_k=|C_k|>=3. Then b>=2 and
q_k<=9. Assign independent variables R_1,...,R_b with product probability
nu^b. For j in C_k write b(j)=k. Exact Fubini gives

    S_pi=E_(nu^b) sum_d^* product_(j=1)^12 f_(d_j)(R_(b(j))). (14)

For an equality partition sigma of [12], define

    mu(sigma)=product_(B in sigma)(-1)^(|B|-1)(|B|-1)!,
    G_B(R_1,...,R_b)=sum_(d>Q) product_(j in B) f_d(R_(b(j))).

The exact finite collision identity is

    sum_d^* product_j f_(d_j)(R_(b(j)))
       =sum_sigma mu(sigma) product_(B in sigma) G_B.     (15)

It follows by expanding into all label tuples: on an equality class of
size h, the total coefficient is the sum of signs of permutations of h
letters, interpreted by cycle partitions. This equals zero for h>=2
by composition with a transposition, and one for h=1. This proves (15)
for arbitrary real arrays at different radii; it does not invoke any
single-radius specialization.

The all-singleton sigma term is product_k Z(R_k)^(q_k), whose expectation
is product_k E_nu Z^(q_k). For any other sigma, let its nonsingleton blocks
have sizes h_1,...,h_c, and put H=sum h_i>=2. Every mixed block satisfies

    |G_B| <= sum_(d>Q) A_d(T)^h
           <<_(h,eta) Q^(1-3h/4+eta), h=|B|>=2.          (16)

The remaining singleton factors are Z(R_k)^(r_k), with 0<=r_k<=q_k<=9.
Only these collective Z factors are placed in modulus. By (8), independence
of the integration variables, and c<=H/2, the integrated modulus of the
term is at most

    T^epsilon Q^(c-3H/4+c eta)
       <= T^epsilon Q^(-H/4+c eta)
       <= T^epsilon Q^(-1/2+c eta).                     (17)

Choose all input epsilons and eta smaller than the desired output epsilon;
there are only finitely many partitions of 12. We obtain the stronger
signed comparison

    S_pi=product_k E_nu Z^(q_k)
                      +O_epsilon(Q^(-1/2)T^epsilon),
    |S_pi| <<_epsilon T^epsilon.                         (18)

Absolute convergence proves the infinite version of (15) before applying
the actual moment bound (8). This ordering avoids an unjustified assertion
that an arbitrary finite class truncation has the actual Z moment bound.
The elementary domination by S(T)^12 permits passage to the infinite sum.

Combining (13), (18) and the exact finite sum (6), with its single outer
TW, proves (1). Products of b moments do not introduce an extra T^b:
they are expectations with respect to b probability variables.

### 3.3 Available signed connected bound and complete restoration

Accepted216 gives

    I12=M12(Z_Q)+O_epsilon(T^(8beta-1/5+epsilon)),
    8beta-1/5<21/25<1.

Together with (1) and K=I-D this proves (2). Accepted204 bounds the full
B_T twelfth moment by T^(1+epsilon)+T^(10beta+epsilon); the accepted216
head costs T^(15/13+epsilon). The scalar inequality for B_T-L_Q gives
M12(Z_Q)<<T^(10beta+epsilon), since 10beta>5/4>15/13. This proves (3).
No new exponent has been extracted from the connected subtraction.

If the still-unproved ONE-SIDED hypothesis

    K12<=C_epsilon T^(29/25+epsilon) for every epsilon>0  (19)

is supplied, then I=K+D has the same one-sided upper bound. Accepted216's
nonnegative moment comparison and (1) pay its negative part and yield
M12(Z_Q)<<T^(29/25+epsilon). The entire head costs 15/13, which is below
29/25 by exactly 2/325. The repeated-class error costs less than 21/25.
The scalar B=L+Z inequality pays every head/tail mixed term, yielding the
complete M12(B_T) bound. This retains all signs, harmonics and tails.

The already accepted sharp reconstruction, including smoothing, Bessel
error, real radii and inclusive integer jumps, gives at X=T^2

    integral_(X/2)^(3X)|P(x)|^12 dx
      <<T^7 M12(B_T)+T^(8+epsilon)
      <<X^(102/25+epsilon).

The two-sign persistence argument then gives

    P(X)<<_epsilon X^(102/325+epsilon).                  (20)

Conversely the complete target moment gives (19) by (1) and accepted216.
The implication asserted here is the conditional moment-to-pointwise
direction, not equivalence of the pointwise conclusion with the moment.
There is no all-order extrapolation and no quarter bound from p=12.

### 3.4 Actual full-harmonic absolute block control

Expand each cosine in m_[q] exactly, then apply the triangle inequality.
The map n=d s^2 is unique. Relaxing squarefree-core distinctness and d>Q
only enlarges this nonnegative upper sum. It suffices to bound

    sum_(n_1,...,n_q>=1) product_j |a_(n_j)|
         sum_(epsilon_j=+-1)|w-hat(T sum_j epsilon_j sqrt(n_j))|.
                                                               (21)

The fixed constants 2^(-q)/W are harmless. Select a maximal n_j and its
dyadic range N<=n_j<2N; the remaining n_i are at most 2N. For fixed other
variables and signs, the points sqrt(n_j) have spacing at least c/sqrt(N).
The elementary separated-point sum for L>1 therefore gives, uniformly
in the real center alpha,

    sum_(N<=n<2N)(1+T|sqrt(n)-alpha|)^(-L)
        <<_L 1+sqrt(N)/T.                                (22)

To see this directly, order the points by distance from alpha: apart from
at most two nearest points, the k-th distance is >=c k/sqrt(N); compare
the remaining summable series to its integral. No arithmetic spacing for
the other q-1 frequencies is required.

For any eta>0 and arbitrary fixed A, the maximal coordinate coefficient
is at most

    C_(eta,A) N^(-3/4+eta) min(1,(N/T)^(-A)).

Every other coordinate's coefficient L1 sum up to 2N is
O_eta(N^(1/4+eta)). Thus the contribution of this maximal dyadic range
to (21) is at most

    C N^(q/4-1+q eta) (1+sqrt(N)/T)
                           min(1,(N/T)^(-A)).            (23)

For N<=T, summing dyadic N gives
O(T^(max(q/4-1,0)+epsilon)); q=4 contributes a harmless logarithm.
For N>T, choose A sufficiently large in terms of fixed q and epsilon.
The two resulting geometric tails cost at most
T^(q/4-1+epsilon) and T^(q/4-3/2+epsilon), respectively, both within
the same bound. This proves (4) while retaining every high harmonic
and the full tail. No hard frequency cutoff is being hidden in (4).

For any proper pi, the sum of product moment moduli with global
distinctness is at most product_(C in pi) A_(|C|), because deleting
cross-block distinctness constraints only enlarges the nonnegative sum.
For singleton/pair shapes use (13), not an invented A1/A2 diagonal bound.
For the remaining shapes, the outer-T exponents from (4) are:

| Block sizes | Outer exponent |
| --- | --- |
| 9+3 | 9/4 |
| 8+4, 7+5, 6+6 | 2 |
| 6+3+3 | 3/2 |
| 5+4+3 | 5/4 |
| 4+4+4, 3+3+3+3 | 1 |

The reverse triangle inequality for each tuple, summed absolutely, now
gives (5). If the actual lower certificate C_raw>=cT^(5/2) is independently
verified, choose epsilon<1/4 and (5) transfers it to C_conn. This diagnoses
the stronger absolute-cluster mechanism only. Cancellation between
different signed cumulants is untouched by this lower-bound transfer.

## 4. First doubtful or unproved step

No doubtful step is knowingly used in the proofs (1), (4), (5), subject to
nonauthor review of the probability, mixed-radius, infinite-tail and source
dependency seams. The first unproved arithmetic step for a complete gain
is exactly (19). Estimate (3) is weaker, and (2) shows the required saving
still resides in the high actual twelfth moment. Calling the remaining
correlation "connected" supplies neither separation nor cancellation.

The unconditional lower bound for C_raw is a separate unverified premise
inside this task's evidence. No inference from a finite-harmonic example,
arbitrary coefficient family or generic norm control is substituted for it.
The authorized certificate-audit task must establish or reject that premise.
Even if it succeeds, the result refutes only the proposed absolute route,
not the signed bound (19) or every possible connected-correlation method.

## 5. Control tests and outcomes

1. `probability_normalization`: PASS analytically. Integral dnu=1;
   Fourier mean is w-hat(-T lambda)/W; products use nu^b and have only
   the final TW in I,K,D. This is essential to the exponent 1 in (1).
2. `actual_full_harmonics`: PASS for the proved statements. Formula (7)
   includes all s. Formula (9) explicitly pays every omitted term in the
   rapid-mean argument; (23) pays the entire tail in the absolute bound.
3. `rapid_single_pair`: PASS analytically, (11)-(13). The distinct-class
   restriction is indispensable; equal-class pair means are not declared
   small. Frequency cutoff exponent 3/2 leaves physical spacing T^(1/4).
4. `signed_collision_sum`: PASS analytically and finite exact diagnostic.
   Identity (15) leaves singleton sums as actual Z, then takes moduli after
   regrouping. It never uses sum|f_d| in place of |sum f_d| at those slots.
5. `connected_absolute_control`: PASS for the upper correction (5).
   The actual C_raw lower-certificate premise is NOT verified by this task;
   its conditional transfer is exact. No signed lower bound is deduced.
6. `complete_budget`: PASS conditionally on (19). Costs are 1 for D,
   15/13 for head, <21/25 for repeated error, and the complete smoothing
   term T^8; target 29/25 gives 102/325 after sharp restoration.
7. `no_signed_lower_bound`: PASS. Equation (2) only supplies a negative
   floor and an additive comparison to a nonnegative moment. Neither a
   positive signed lower bound nor any refutation of (19) is claimed.
8. `wolfram_local_exact`: PASS after a repaired diagnostic expression.
   Two signed rows at two radii were used:
   x=(1,-2,3,-1,2,0,-3), y=(2,1,-1,3,-2,4,1), with slot types xxx yyy.
   Direct sum over 7P6=5040 distinct tuples and the 203-partition mixed
   collision sum both equal -68112. Python exact integers and Wolfram
   both reproduce this value. Exact rational shape exponents and 102/325
   also agree. The first Wolfram collision expression had an unbound
   pure-function parameter and returned errors; replacing it by an explicit
   Function[p,...] repaired the expression. No erroneous output is used.
9. `blind_isolation`: PASS. No sibling reports, isolated-collision brief,
   or historical certificate files were opened. Own proof was derived
   from the permitted actual interface and accepted kernels only.
10. `history_preservation`: PASS by scope. Only this assigned report is
    written; graph, proof draft, shared synthesis, and legacy folders are
    untouched. Graph hash matches the frozen starting graph at read time.

Exact diagnostic reproduction (Python, standard library; run through
`python -` with UTF-8 source, no files created):

```python
from itertools import permutations
from math import factorial
from functools import reduce
from fractions import Fraction
def partitions(items):
    if not items:
        yield []
        return
    x,*rest=items
    for p in partitions(rest):
        yield [[x]]+[b[:] for b in p]
        for i in range(len(p)):
            q=[b[:] for b in p]
            q[i]=[x]+q[i]
            yield q
rows=[[1,-2,3,-1,2,0,-3],[2,1,-1,3,-2,4,1]]
which=[0,0,0,1,1,1]
lhs=sum(reduce(lambda a,j:a*rows[which[j]][ds[j]],range(6),1)
        for ds in permutations(range(7),6))
rhs=0
for p in partitions(list(range(6))):
    term=1
    for block in p:
        mu=(-1)**(len(block)-1)*factorial(len(block)-1)
        power=sum(reduce(lambda a,j:a*rows[which[j]][d],block,1)
                  for d in range(7))
        term*=mu*power
    rhs+=term
assert lhs==rhs==-68112
def iparts(n,lo=3):
    if n==0:
        yield []
    for a in range(lo,n+1):
        for rest in iparts(n-a,a):
            yield [a]+rest
shapes=[(p,1+sum(max(Fraction(q,4)-1,0) for q in p))
        for p in iparts(12) if len(p)>=2]
assert max(e for p,e in shapes)==Fraction(9,4)
assert (14+2*Fraction(29,25))/52==Fraction(102,325)
```

Wolfram repaired mixed-radius diagnostic, time constraint 15 seconds:

```wolfram
Clear[sp]; sp[{}]:={{}};
sp[l_List]:=Module[{x=First[l],ps=sp[Rest[l]]},
  Flatten[Table[Join[{{{x}}~Join~p},
    Table[ReplacePart[p,i->Prepend[p[[i]],x]],{i,Length[p]}]],
    {p,ps}],1]];
rows={{1,-2,3,-1,2,0,-3},{2,1,-1,3,-2,4,1}};
which={1,1,1,2,2,2};
direct=Total[Times@@Table[rows[[which[[j]],#[[j]]]],{j,6}]& /@
  Flatten[Permutations /@ Subsets[Range[7],{6}],1]];
ie=Total[Function[p,Times@@Table[
  (-1)^(Length[b]-1) Factorial[Length[b]-1]
  Sum[Times@@Table[rows[[which[[j]],d]],{j,b}],{d,7}],{b,p}]] /@
  sp[Range[6]]];
{Length[sp[Range[6]]],direct,ie,direct==ie}
(* {203,-68112,-68112,True} *)
```

These bounded exact controls check normalization and finite combinatorics
only. They neither certify the analytic estimates nor sample high-T behavior.
The Wolfram context tool returned only computational documentation and no
relevant theorem; none of its generated suggestions is an analytic input.

## 6. Dependencies and exact artifacts used

All filesystem reads used explicit UTF-8. The large graph was additionally
parsed to inspect the accepted statuses/statements of the three relevant
GC-complete nodes. No new external theorem was imported. Existing qualified
Li--Yang and Bourgain source dependencies are inherited only through the
accepted actual-moment/distribution kernels, with their scope preserved.

| Context artifact | SHA-256 |
| --- | --- |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306 |
| state/active_campaign.yml | 191a128598ac25cc35d736a97dc6b9e9f86e6eca40789da4d514ead5e71e6cd5 |
| rounds/codex-managed/gc-connected-cumulant-test/briefs/signed_connected_attack.md | 875d24fc778ab6568e5a2a2233742236e6f25567102b936493ae4e1287e81c1d |
| rounds/codex-managed/gc-connected-cumulant-test/briefs/actual_interface.md | 8d7cd13111517df44932faef0420e5c4679b69a70e23a0520561497d0a3caee6 |
| proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md | b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |

Accepted graph nodes used: GC-complete-distinct-radical-twelfth-reduction;
GC-complete-fixed-even-moment-distinct-absorption;
GC-complete-square-root-large-values-moment-bound; their elementary divisor
and qualified source dependencies as stated in the permitted kernels.
The mixed-radius identity, block-spacing estimate, and disconnected bound
are proved here rather than imported from sibling evidence.

## 7. Recommended state effect

Promote only after nonauthor seam review: the paid actual signed disconnected
remainder (1), its exact mixed-radius collision comparison (18), and the
absolute upper correction (5), with full probability normalization and
infinite-harmonic scope. Retain the open actual signed bound (19) and the
conditional complete restoration. Retain (5)'s lower-certificate premise
as conditional until the separately authorized audit verifies it.

Reject the inference that paying D alone proves a complete gain, and reject
any automatic replacement of signed K by a target-sized absolute-cluster
bound. Do not promote an improved full twelfth moment, a pointwise exponent,
an all-order connected estimate, any M1/M2/GAR parent or endpoint, or the
quarter target. No successor round is proposed or started by this task.
