# Round 233: actual fixed-order distinct-class absorption bridge

Campaign: `gc-fixed-order-moment-absorption`.
Task: `actual_fixed_order_bridge`; role: formalizer; access: selected context.
Status: candidate evidence only, not accepted mathematics or a state patch.
Generated UTC: 2026-10-12T00:12:00Z.
Starting graph SHA-256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
Research allocation: analytical/algebraic only; no numerical experiment, external source import, sibling report, or successor round.

## 1. Result: a valid relative reduction, with the arithmetic target still open

For every fixed even integer p >= 2 and every 0 < delta < 1, the proposed inequality is valid for any real absolutely summable family x_d. Put Z=sum x_d, V=sum x_d^2, and let E_p be the sum of products over ordered pairwise distinct p-tuples. Then

    |Z^p-E_p| <= delta |Z|^p + C_(p,delta) V^(p/2).          (1)

For the complete actual family in the frozen interface, including every harmonic and the infinite smoothing tail, this proves

    integral |Z_Q^p-E_(p,Q)| dmu
       <= delta M_p(Z_Q)+A_(p,delta)(T,Q),
    A_(p,delta)(T,Q)
       := C_(p,delta) integral (sum_(d>Q) f_d^2)^(p/2)dmu
       <<_(p,delta,epsilon) T Q^(-p/4+epsilon).             (2)

In particular

    (1-delta)M_p(Z_Q)-A <= I_(p,Q)
                              <= (1+delta)M_p(Z_Q)+A.    (3)

This is a relative absorption result. It does not claim an additive error independent of the unknown moment with coefficient zero on M_p(Z_Q). It bypasses the earlier baseline term T^((p-4)beta) by retaining, and then absorbing, the unknown pth moment itself.

For Q=1, the head and absorption budgets are O_p(T). For Q=floor(T^(1/p)), the absorption budget is O_(p,epsilon)(T^(3/4+epsilon)) and a fully elementary head budget is O_p(T^(5/4)). A refinement using the accepted finite large-values mechanism gives

    M_p(L_Q) <<_(p,epsilon) T^(h_p+epsilon),
    h_p := max(1, 5/4-34/(13p)).                          (4)

The reduction supplies no new estimate for the remaining actual signed integral I_(p,Q). A sequence of one-sided estimates for that integral at an unbounded sequence of fixed even orders, with exponents o(p), would imply the quarter target after the complete restoration proved below. No such sequence is proved here.

## 2. Exact statement and hypotheses

Fix a nonnegative real radial rho in C_c^infinity(R^2), supported in the unit disk, of integral 1. Use e(t)=exp(2 pi i t), the Fourier convention with e(-x dot xi), and Psi(u)=rho-hat(u e_1). Thus Psi is real, even and Schwartz, and |Psi|<=1. Fix a nonnegative smooth w supported in [1/2,2], equal to 1 on [1/sqrt(2),sqrt(3)], and write dmu=w(R/T)dR.

For real T>=2 and real Q>=1 define, with d always squarefree,

    a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    f_d(R)=sum_(s>=1)a_(d s^2)(T)
                         cos(2 pi R s sqrt(d)-3 pi/4),
    B_T=sum_d f_d, L_Q=sum_(d<=Q)f_d,
    Z_Q=sum_(d>Q)f_d=B_T-L_Q,
    E_(p,Q)=sum_(ordered pairwise distinct d_1,...,d_p>Q)
                                              product_j f_(d_j),
    I_(p,Q)=integral E_(p,Q)dmu,
    M_p(F)=integral |F|^p dmu.

Membership d>Q is literal; Q need not be integral in (1)-(3). The concrete choices are Q=1 and Q=floor(T^(1/p)). The integer p is even, at least 2, and is fixed independently of T. Constants may depend on p, delta, epsilon and the fixed functions. No uniformity as p grows with T is asserted.

An explicit valid finite constant in (1) is

    K_p=p!-1,
    C_(p,delta)=K_p max(1,(K_p/delta)^((p-2)/2)).          (5)

The exact complete transfer, preserving the sign of I, is

    M_p(B_T) <= 2^(p-1) [ (I_(p,Q)+A)/(1-delta)
                                                   +M_p(L_Q)], (6)
    |I_(p,Q)| <= (1+delta)2^(p-1)
                         [M_p(B_T)+M_p(L_Q)]+A.          (7)

The numerator I+A in (6) is nonnegative by (3). One may replace A by any established nonnegative upper bound for it, with the same conclusion. There is no assumption that I itself is nonnegative.

For Q=1 and any fixed b>=1, the following are equivalent, in the convention that every estimate holds for each epsilon>0 with a corresponding fixed constant:

    M_p(B_T) << T^(b+epsilon);
    M_p(Z_Q) << T^(b+epsilon);
    |I_(p,Q)| << T^(b+epsilon);
    I_(p,Q) <= C_(p,epsilon) T^(b+epsilon).               (8)

For Q=floor(T^(1/p)), (8) holds whenever b>=h_p. The simpler assumption b>=5/4 suffices without the refined head argument. More generally, a one-sided I bound with exponent c_p yields a B_T bound with exponent max(c_p,1) for Q=1, or max(c_p,h_p) for Q=floor(T^(1/p)). No equivalence below the established head/error budgets is asserted.

## 3. Proof and complete derivation

### 3.1 Finite partition identity and relative absorption

For a finite real family, put P_h=sum_d x_d^h, so P_1=Z and P_2=V. Let Pi_p be the set partitions of [p], and set

    mu(pi)=product_(C in pi)(-1)^(|C|-1)(|C|-1)!.

Then

    E_p=sum_(pi in Pi_p) mu(pi) product_(C in pi)P_(|C|). (9)

To prove (9), expand into ordered index tuples. For an equality class of m labels, subordinate partitions contribute the sum of signs of permutations of those m labels: a block of size h has (h-1)! cyclic permutations and sign (-1)^(h-1). The sum is 1 when m=1 and 0 when m>=2, the latter by composition with a fixed transposition. Consequently exactly the pairwise distinct tuples survive with coefficient 1.

The all-singleton partition contributes Z^p. Every other partition has r singleton blocks with 0<=r<=p-2, and remaining block sizes h_i>=2, with sum h_i=p-r. For h>=2,

    |P_h| <= sum_d |x_d|^h <= V^(h/2).

Indeed |x_d|<=sqrt(V), so sum |x_d|^h<=V^((h-2)/2)sum x_d^2. Thus its corresponding term is bounded by |mu(pi)| |Z|^r V^((p-r)/2). The sum of |mu(pi)| over all partitions is p!, since it counts permutations by cycle decomposition. After removing the singleton partition the sum is K_p=p!-1.

If V=0, every x_d=0 and (1) is immediate. Otherwise let t=|Z|/sqrt(V) and R=max(1,sqrt(K_p/delta)). Then

    |Z^p-E_p| <= K_p max(1,t^(p-2)) V^(p/2).

For t>=R, this is <=delta t^p V^(p/2)=delta|Z|^p. For t<R it is <=K_p R^(p-2)V^(p/2). This proves (1) with (5), for every finite family size. At p=2, the identity is exactly E_2=Z^2-V and the constant in (5) is 1.

The identity and inequality pass to an absolutely summable infinite real family by finite truncation: Z, every P_h and the ordered distinct sum converge absolutely, the latter being dominated in absolute value by (sum |x_d|)^p. There is no size-dependent constant to lose in this limit. For a function family, integration additionally requires integrability of the displayed majorants; the actual family below has uniform convergence in R and a finite window, supplying it directly.

For even p, Z^p=|Z|^p. Multiplying (1) by the nonnegative measure and integrating proves (2)-(3), once A is estimated. In particular I>=-A. The norm inequality |u+v|^p<=2^(p-1)(|u|^p+|v|^p), applied to B=L+Z and Z=B-L, gives (6)-(7).

### 3.2 Complete actual amplitudes and the all-fixed-order input

Set A_d(T)=sum_(s>=1)|a_(d s^2)(T)|. The elementary formula r2=4(1*chi4) gives

    r2(d s^2)<=r2(d)tau(s^2)

for squarefree d. If a prime congruent to 3 modulo 4 divides d, both representation counts vanish. Otherwise each prime congruent to 1 modulo 4 which divides d contributes the inequality 2e+2<=2(2e+1); primes not dividing d and the prime 2 also satisfy the asserted product bound. Since tau(s^2)<=tau_3(s),

    A_d(T)<=zeta(3/2)^3 r2(d)d^(-3/4).                   (10)

This retains every s, including s>=2 for d=1. It uses |Psi|<=1, not positivity of Psi away from zero.

The disk/unit-square comparison gives sum_(n<=x)r2(n)<<x for x>=1. Partial summation of (10), enlarging the squarefree sum to all integers, proves

    sum_(d<=Q) A_d(T)<<Q^(1/4),
    sup_R |L_Q(R)|<<Q^(1/4).                            (11)

For each fixed integer h>=2 and each eta>0, the elementary divisor bound gives

    sum_(d>Q) A_d(T)^h <<_(h,eta) Q^(1-3h/4+eta).        (12)

For completeness choose gamma>0 smaller than both eta and 3h/4-1. Apply r2(d)<<d^(gamma/h) inside (10), and sum d^(-3h/4+gamma) by an integral or dyadic intervals. Its exponent is strictly below -1 and the resulting Q power is at most the one in (12). This proves the extension to every fixed h directly; no accepted all-order squarefree-class moment theorem is being assumed.

In particular V_Q(R)=sum_(d>Q)f_d(R)^2<=sum_(d>Q)A_d(T)^2<<Q^(-1/2+eta). Since mu(R)=T integral w,

    integral V_Q^(p/2)dmu <<_(p,eta) T Q^(-p/4+p eta/2).

Choose eta sufficiently small relative to the requested epsilon. This proves the A bound in (2), uniformly for all real T>=2 and Q>=1. The h>2 bounds in (12) verify the full stated amplitude interface but are not required for this shorter V-based proof.

For each fixed T, Schwartz decay implies sum_n |a_n(T)|<infinity. For example, beyond n>T use |Psi(sqrt(n/T))|<<_L T^(L/2)n^(-L/2), the divisor bound, and any sufficiently large fixed L. Hence sum_d A_d(T)<infinity. All harmonics, classes, powers, and ordered distinct sums converge absolutely and uniformly in R; products and integration against dmu pass to the infinite limit. This is an identity-level justification, not an asymptotic deletion of tails.

### 3.3 Head budgets, including the optional stronger head

From (11) alone,

    M_p(L_Q)<<_p T Q^(p/4)                              (13)

for every Q>=1. Therefore Q=1 gives O_p(T), and Q=floor(T^(1/p)) gives O_p(T^(5/4)). For the latter choice, 0.5 T^(1/p)<=Q<=T^(1/p), so (2) gives A<<T^(3/4+epsilon), after renaming epsilon. These comparisons also cover bounded T and floors equal to 1; constants may depend on fixed p.

Here is a derivation of (4), without treating a squarefree mask as an unproved final theorem. Use the finite correlation/Gram/covering mechanism in accepted204, Sections 3-5, with the coefficient mask 1_(sf(n)<=Q). Its coefficients do not depend on R. Remove only n>T^(3/2), whose full absolute Schwartz/divisor tail is O_A(T^-A), uniformly after this mask. In each of the remaining O(log T) ambient dyadic blocks, including singleton n=1, zero-extend the masked coefficients. Their energy is bounded by that of the actual full block:

    sum |a_n 1_(sf(n)<=Q)|^2 <<_eta T^(3eta) N^(-1/2).

The unweighted square-root correlation kernel is unchanged. Accepted204's finite covering inequality applies at every positive block level with the full Gram diagonal and full 1+T/h localization ceiling. The cosine wave is the real part of e(-3/8) times its complex wave. Apply the block inequality at V/(C log T), union the block events, and include the uniformly tiny upper tail. Absorb the fixed logarithmic powers by choosing the input eta suitably small. This proves, for V>=1,

    D_(L_Q)(V) <<_epsilon T^epsilon (V^-2+T V^(-q)),
    q=136/13,                                           (14)

uniformly in Q. This is a fresh application of the already accepted finite mechanism, not a claim about arbitrary mask suprema. Its inherited exponent-pair source qualifications remain unchanged.

For 1<=Q<=T, layer cake, the O(T) measure at levels <=1, and (11) give for every fixed even p>=2

    M_p(L_Q) <<_(p,epsilon) T^epsilon
       [T+Q^((p-2)/4)+T Q^(max(p-q,0)/4)].              (15)

At p=2 the first large-value integral is logarithmic in 2+Q and is absorbed into T^epsilon; q is not an even integer, so there is no p=q endpoint here. For p>2, integrate V^(p-3) and V^(p-1-q) up to C Q^(1/4), treating a ceiling below 1 through the already paid O(T) term. Input epsilon is chosen smaller before the logarithm absorption.

For Q=floor(T^(1/p)), the middle exponent is (p-2)/(4p)<1. The last exponent is 1 for p<q and 1+(p-q)/(4p)=5/4-34/(13p) for p>q. This proves (4). In particular h_p=1 for p=2,4,6,8,10; h_p<5/4 always. The coarse bound (13) already suffices for the all-order implication, so failure to use the optional inherited large-value refinement would not invalidate the main bridge.

### 3.4 One-sided signed targets, thresholds and exact remaining expression

Set delta=1/2 once and for all. Equations (3), (6), (7) prove (8) whenever A and M_p(L_Q) obey the same target budget. They also show directly that the negative part satisfies max(-I,0)<=A. Thus a one-sided upper target is enough: it cannot hide an arbitrarily large negative I. Conversely a B moment target, together with the paid head, bounds |I| by (7). Every mixed B=L+Z term is covered by the physical norm inequality; no individual mixed correlation is discarded.

These are complete moment statements. If a high-value target is used instead, its complementary low levels must be paid. The trivial bound is

    integral_(|B_T|<=T^v) |B_T|^p dmu << T^(1+pv).

Using the accepted full distribution and the same layer-cake argument sharpens this for fixed v>=0 to

    <<_(p,epsilon) T^epsilon
         [T+T^(v(p-2))+T^(1+v max(p-q,0))].             (16)

For p=2 the logarithm is again absorbed. Only when this bound fits the intended exponent may the upper-tail target replace a full moment target. No threshold is silently dropped in (8). No threshold transfer is needed for the present complete reduction.

Under the convention w-hat(xi)=integral w(u)e(-xi u)du, the exact remaining expression is

    I_(p,Q)=T 2^(-p) sum_(epsilon_j in {+1,-1})
       sum_(d_j>Q squarefree pairwise distinct; s_j>=1)
       [product_j a_(d_j s_j^2)(T)]
       e(-3 sum_j epsilon_j/8)
       w-hat(-T sum_j epsilon_j s_j sqrt(d_j)).          (17)

Absolute convergence for fixed T justifies this expansion. Conjugate sign vectors make its reality explicit; they do not make it positive. Distinct squarefree radicals are rationally independent, as stated in the accepted exact-resonance dependency, so each displayed frequency is nonzero. No lower bound on its nonzero magnitude appropriate for the scale 1/T follows. Replacing (17) by a target-sized absolute tuple sum, or declaring cancellation from distinctness, is not part of this proof.

### 3.5 Leading amplitude, sharp error and the p+1 persistence denominator

Let X=T^2, and use the one smoothing width delta_0=T^(-1/2) over R comparable to T. The difference between the inclusive lattice count and its rho_(delta_0) convolution is supported in the closed annulus R-delta_0<=|m|<=R+delta_0. The interval for |m|^2 has length O(T delta_0); the divisor bound for r2(n), including its endpoints, gives an error O_epsilon((T delta_0+1)T^epsilon)=O_epsilon(T^(1/2+epsilon)). This pays sharp jumps as well as continuous radii.

The accepted Poisson and fixed-order Bessel reconstruction in accepted204, Section 6, has the exact leading term

    P(R^2)=sqrt(R)/pi B_T(R)+O_epsilon(T^(1/2+epsilon)). (18)

Indeed the Fourier disk transform is R J_1(2 pi R sqrt(n))/sqrt(n). Multiplying its leading Bessel cosine by this factor gives sqrt(R)/pi times n^(-3/4) and phase 2 pi R sqrt(n)-3 pi/4, precisely the coefficients used here. The full Bessel remainder is bounded by

    O(R^(-1/2) sum_(n>=1) r2(n)n^(-5/4))=O(T^(-1/2)),

with the convergent sum justified by a sufficiently small divisor exponent. Thus (18) has no missing amplitude or harmonic truncation.

Since w=1 for the radii corresponding to x in [X/2,3X], and dx=2R dR, a complete normalized estimate M_p(B_T)<<T^(b_p+epsilon) gives

    integral_(X/2)^(3X) |P(x)|^p dx
       <<_(p,epsilon) T^(1+p/2+b_p+epsilon)
                         +T^(2+p/2+epsilon)
       <<_(p,epsilon) X^(E_p+epsilon),
    E_p=max(1+p/4, (1+p/2+b_p)/2).                     (19)

The second term is the complete smoothing error raised to the pth power and integrated over length O(X); it is never discarded. The leading T factor in the first term is the Jacobian.

For completeness, the elementary one-sided persistence proof works for the inclusive sharp count. At x_0 with P(x_0)=A>0, monotonicity of N implies P(x)>=A/2 for x in [x_0,x_0+A/(2pi)]. If P(x_0)=-A<0, it implies P(x)<=-A/2 for x in [x_0-A/(2pi),x_0]. The elementary unit-square comparison P(x)=O(sqrt(x)+1) ensures these intervals lie in [x_0/2,3x_0] for all sufficiently large x_0. It therefore follows that

    A^(p+1)/(2^(p+1)pi)
           <= integral_(x_0/2)^(3x_0)|P(x)|^p dx.

Thus (19) gives

    P(x) <<_(p,epsilon) x^(E_p/(p+1)+epsilon),
    E_p/(p+1)=1/4+max(3,1+2b_p)/(4(p+1)).               (20)

The denominator is p+1, not p. Neither differentiability of the sharp count nor two-sided persistence through its jumps is needed.

Suppose an unbounded sequence p_j of fixed even orders satisfies one-sided estimates I_(p_j,Q_j)<=C_(p_j,epsilon)T^(c_j+epsilon) for every epsilon>0 and all T>=2, with c_j=o(p_j), where each Q_j is either 1 or floor(T^(1/p_j)). The paid head/error budgets above give b_j=o(p_j). For any requested quarter-target loss, first select a sufficiently large fixed p_j so the loss in (20) is smaller, then select the arbitrary input epsilon sufficiently small. The resulting constant may depend on that chosen p_j and hence on the requested loss. This proves the conditional implication to P(x)<<_epsilon x^(1/4+epsilon), without taking p as a function of T or claiming uniform constants in p.

## 4. First doubtful or unproved step

No unproved analytic step is needed for (1)-(3), (6)-(13), or the conditional sharp restoration (18)-(20), relative to the already accepted reconstruction identities and elementary divisor input. The stronger head (14)-(15) uses the accepted finite204 mechanism with its source qualifications, and has been explicitly rebound to the current coefficient mask.

The first missing arithmetic assertion is any sufficiently strong one-sided upper bound on the complete actual signed integral (17), in particular an unbounded sequence with c_p=o(p). This report does not prove it. Distinctness removes zero frequencies but does not estimate the near-zero or other displaced signed aggregate. The finite relative inequality holds for arbitrary real families and contains no arithmetic cancellation theorem; it cannot distinguish the actual arithmetic family from an adversarial aligned one in order to manufacture that missing estimate.

The two inherited upper-tail attempts are not reset or bypassed by declaration. This is a different complete conditional reduction and does not assert the fixed twelfth target, any new pointwise exponent, any M1/M2/GAR parent, or the quarter theorem.

## 5. Required control tests and outcomes

- **finite_partition_identity -- analytical pass.** The coefficient of every equality class is computed in (9). With m equal entries x, E_p=(m)_p x^p; it is zero when m<p and has the exact ordered multiplicity when m>=p. All-zero inputs give zero throughout.
- **relative_absorption -- analytical pass.** V=0 is handled separately; the explicit constant (5) is independent of family size. At p=2, E_2=Z^2-V exactly. With m<p equal nonzero entries, the required large constant is allowed: (1-delta)m^p<=C m^(p/2). For m large, the relative difference of m^p and (m)_p tends to zero, consistent with absorption. Constants grow rapidly with p, which is permitted only because p is fixed.
- **signed_integral_negative_part -- analytical pass.** At p=2 the family (1,-1) has Z=0, V=2, E_2=-2. At p=4 the family (1,1,1,-1) has E_4=-24. Positivity of E or I is therefore not assumed. Inequality (3) gives the valid lower bound I>=-A and the nonnegative numerator I+A in (6).
- **actual_harmonics_and_head -- analytical pass.** Formula (10) sums all s. Q=1 retains the entire d=1 class, not merely n=1. Uniform absolute convergence and (13) pay every harmonic, tail and head. The refined masked argument includes singleton n=1, partial ambient blocks and the full localization ceiling.
- **fixed_order_quantifiers -- analytical pass.** All finite constants, Schwartz decay orders, epsilon allocations and head bounds are chosen after fixing p. The final sequence implication chooses p from the desired final loss before letting T vary. No growing-order estimate is asserted.
- **complete_sharp_restoration -- analytical pass.** Equation (19) retains sqrt(R)/pi, dx=2R dR, the full T^(2+p/2+epsilon) smoothing contribution, and real endpoints. Equation (20) proves the one-sided persistence denominator p+1. Equation (16) states the budget required before replacing a complete moment by an upper-tail target.
- **no_unproved_signed_gain -- analytical pass.** Equation (17) remains an exact unestimated signed expression. The result supplies no target-sized absolute certificate and no new arithmetic large-value estimate.
- **wolfram_exact_local_reproduction -- pending conductor gate.** No numerical or symbolic tool computation was performed in this task, as directed. The conductor owns the separate bounded Wolfram check and its independent local reproduction. This report does not label that gate passed.
- **blind_isolation -- respected, separate result pending.** No sibling reports or isolated sibling derivations were read. This is the selected-context formalizer report, not the statement-only independent certificate. The independently assigned certificate remains a conductor gate.
- **graph_history_preservation -- respected.** Only this assigned report is written. Neither graph, proof draft, validation matrix, synthesis, nor legacy evidence is modified. Any promotion still requires nonauthor reviews and a validated State Patch.

These are algebraic controls, not numerical proof of an asymptotic statement. The task used no experiment.

## 6. Dependencies and exact artifacts used

Only the assigned context and own brief were read. Existing graph acceptance was checked for `GC-target` (open), `Divisor-bound-elementary`, `GC-complete-square-root-large-values-moment-bound` (accepted204), `GC-complete-distinct-radical-twelfth-reduction` (accepted216), `GC-weighted-square-root-exact-resonance-mass`, and the qualified `GC-external-Li-Yang-theta-star`. Li--Yang is not used to pay the repeated-class or head budgets in the elementary bridge. The optional refinement inherits only the already accepted finite large-values mechanism; the sharp transfer reuses the accepted Poisson/Bessel reconstruction. No external article or unlisted local source was opened, imported, or re-audited.

Exact SHA-256 context hashes at read time:

| Artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `state/active_campaign.yml` | `58f07ad6959a485751d27e4df55fddc72d6cba7a474ce824c1426a390ab21b15` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/actual_fixed_order_bridge.md` | `cba3784e168c97c8f74167bc86b201cd77664ec82c6bd50f6245b71cf5e394a2` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/actual_interface.md` | `f7ca86a3d0565aff3234286b0f0949a02920ccd91af0521f51aa3bb3baa338a4` |
| `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` | `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee` |
| `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` | `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212` |

The permitted graph was inspected through the relevant entries, not treated as an all-order proof. Formulas (9)-(13) are independently derived here from their finite and elementary inputs. No novelty claim is made.

## 7. Recommended state effect

**Retain for required reviews, with conditional promotion of a narrow lemma only after the conductor gates pass.** The candidate state effect is an all-fixed-even-order relative absorption and complete actual distinct-class reduction, including the precise one-sided signed-target equivalence above the paid budgets and the conditional all-order sharp implication. Preserve accepted216's stronger order-12 additive statement and its historical scope; this relative result does not overwrite it.

Keep the actual signed estimates, the complete quarter target, all parents and endpoints open. Record the first gap as (17) with a sufficiently small all-fixed-order one-sided growth rate. Do not promote a full moment improvement from the reduction alone. No state change is made by this report. The task stops with this frozen artifact and does not propose or start a successor round.
