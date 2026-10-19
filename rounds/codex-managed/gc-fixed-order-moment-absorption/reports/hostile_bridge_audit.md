# Round233 hostile audit: fixed-order relative absorption

Campaign: `gc-fixed-order-moment-absorption`.
Task: `hostile_bridge_audit`; role: independent barrier/no-go audit.
Generated: 2026-10-12 Asia/Shanghai.
Starting graph SHA-256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
Status: candidate evidence only. No sibling report was read. No numerical experiment, external source import, state edit, or successor design was performed. The proof below is independent of the other current-round derivations, but this task is not the statement-only blind task.

## 1. Result: valid reduction, with a remaining signed arithmetic gap

The proposed relative absorption inequality is valid for every fixed even order p >= 2, uniformly in the number of classes. It does bypass the previous use of the baseline pointwise exponent to pay repeated classes. Its correct consequence is an inequality with a signed integral and an explicitly nonnegative offset; the signed integral itself need not be nonnegative.

For the actual complete family, write V_Q(R) = sum_(d>Q) f_d(R)^2. For 0 < delta < 1 there is a constant C_(p,delta), independent of T and Q, such that, with

    K_(p,Q) = C_(p,delta) integral V_Q(R)^(p/2) dmu(R),

one has

    |M_p(Z_Q) - I_(p,Q)| <= delta M_p(Z_Q) + K_(p,Q),
    I_(p,Q) >= -K_(p,Q),
    M_p(Z_Q) <= [I_(p,Q) + K_(p,Q)]/(1-delta),
    integral (E_(p,Q))_- dmu <= K_(p,Q),
    K_(p,Q) <<_(p,delta,eta) T Q^(-p/4+eta).                 (1)

The numerator in the third line is nonnegative. The precise complete bridge is

    M_p(B) <= 2^(p-1) {M_p(L_Q)
                         + [I_(p,Q)+K_(p,Q)]/(1-delta)},
    |I_(p,Q)| <= (1+delta)2^(p-1){M_p(B)+M_p(L_Q)}
                         + K_(p,Q).                       (2)

The crude but complete head bound is M_p(L_Q) <<_p T Q^(p/4). Thus Q=1 gives an O(T) head and absorption error. For Q=floor(T^(1/p)), the error is O_(p,epsilon)(T^(3/4+epsilon)) and the head is O_p(T^(5/4)). The latter exponent is independent of p. An optional proved refinement below replaces 5/4 by

    h_p = 1 + (p-136/13)_+/(4p) < 5/4.                    (3)

These statements estimate neither the remaining signed I_(p,Q) nor the complete moment at a new exponent. They also do not replace Round216's stronger additive twelfth-order estimate by a smaller additive error: delta M_p(Z_Q) remains on the right side of (1).

## 2. Exact statement and hypotheses

The abstract lemma concerns a finite or countable absolutely summable family of real numbers x_j. Put

    Z = sum_j x_j,  V = sum_j x_j^2,
    E_p = sum_(ordered pairwise distinct j_1,...,j_p)
                                      x_(j_1)...x_(j_p).

For every fixed even integer p >= 2 and every delta > 0,

    |Z^p-E_p| <= delta |Z|^p + C_(p,delta) V^(p/2).        (4)

One admissible explicit constant is

    J_p = p! - 1,
    C_(p,delta) = J_p max(1,(J_p/delta)^((p-2)/2)).        (5)

When these are measurable functions on a positive measure space, the integral consequences in (1), with K=C integral V^(p/2), hold provided M_p(Z) and integral V^(p/2) are finite. Formula (4) then also proves integrability of E_p. The actual family has these properties directly.

The application uses exactly the frozen actual interface: a fixed nonnegative real radial C-infinity mollifier rho supported in the unit disk with integral 1; Psi(s)=rho-hat(s e_1); a fixed nonnegative smooth w supported on [1/2,2], equal to 1 on [1/sqrt(2),sqrt(3)]; real T>=2; and dmu=w(R/T)dR. Set

    a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    f_d(R)=sum_(s>=1) a_(d s^2)(T)
                         cos(2pi R s sqrt(d)-3pi/4),

where d is squarefree. B, L_Q, Z_Q, E_(p,Q), I_(p,Q), and M_p have the literal definitions in the frozen interface. The cutoff Q>=1 can be real; d>Q means exactly that inequality. Every s>=1 is retained. Nonnegativity of rho does not imply nonnegativity of Psi or of f_d, and no such implication is used.

p is fixed independently of T. Constants may depend on p, delta, the desired epsilon, rho, and w. No estimate uniform in p, no p=p(T), and no interchange of p and T limits is asserted.

## 3. Proof and derivation

### 3.1 The exact finite identity and uniform relative bound

For a finite family define P_h=sum_j x_j^h. The ordered distinct polynomial satisfies

    E_p = sum_(pi partition of [p]) mu(pi)
                                      product_(C in pi) P_(|C|),
    mu(pi)=product_(C in pi) (-1)^(|C|-1)(|C|-1)!.         (6)

For a fixed index tuple, subordinate partitions of an equality class of size m contribute the sum of permutation signs on m labels: each block is a cycle and (|C|-1)! counts its cyclic orders. This is 1 for m=1 and 0 for m>=2, by pairing permutations under a transposition. Hence exactly the ordered tuples with all distinct labels survive. This verifies the multiplicity and all signs.

The all-singleton term is Z^p. Every other term has r singleton blocks, 0<=r<=p-2, and non-singleton sizes h_i>=2 with r+sum_i h_i=p. Since

    |P_h| <= sum_j |x_j|^h <= V^(h/2)  (h>=2),

its absolute value is at most |Z|^r V^((p-r)/2). The sum of the absolute partition coefficients in (6) is p!, because it counts permutations by their cycle partitions. Excluding the singleton partition leaves J_p=p!-1.

If V=0 the claim is immediate. Otherwise put t=|Z|/sqrt(V). It follows that

    |Z^p-E_p| <= J_p max(1,t^(p-2)) V^(p/2).              (7)

For t>max(1,sqrt(J_p/delta)), this is at most delta |Z|^p. On the complementary range it is at most C_(p,delta)V^(p/2), with (5). Combining the two ranges proves (4), also for p=2. This argument contains no baseline pointwise exponent.

For an absolutely summable infinite family, truncate by increasing finite subsets. The Z and V sums converge, while the sum of absolute values of all ordered p-fold products is at most (sum_j |x_j|)^p. Therefore E_p converges absolutely and the finite identity and (4) pass to the limit. An l2 hypothesis alone would not justify defining the unconditionally summed Z or E_p; absolute summability is an essential sufficient hypothesis here.

### 3.2 Signs and integration

Evenness of p gives Z^p=|Z|^p. Consequently (4) implies pointwise

    (1-delta)|Z|^p-C V^(p/2) <= E_p
                      <= (1+delta)|Z|^p+C V^(p/2).       (8)

Taking the negative part in the first inequality gives (E_p)_- <= C V^(p/2). Integrating (4) and (8) proves (1), including its negative-part assertion. It is incorrect to replace I+K by I in the upper bound for M, or to declare I>=0. Notice also that the integral of the negative part is bounded, which is stronger than merely bounding the negative part of the integral.

For delta=1/2, one particularly transparent form is

    M_p(Z_Q) <= 2(I_(p,Q)+K_(p,Q)),
    |I_(p,Q)| <= (3/2)M_p(Z_Q)+K_(p,Q).

Applying |u+v|^p <= 2^(p-1)(|u|^p+|v|^p) to B=L_Q+Z_Q and to Z_Q=B-L_Q proves both directions in (2), paying every mixed term.

### 3.3 All actual harmonics and the uniform Q factors

Let A_d(T)=sum_(s>=1)|a_(d s^2)(T)|. The elementary prime-factor argument retained in the accepted Round216 kernel gives

    r2(d s^2) <= r2(d)tau(s^2),
    A_d(T) <= C r2(d)d^(-3/4).                            (9)

For a prime 3 modulo 4 dividing squarefree d both representation counts vanish. For a prime 1 modulo 4 dividing d, the relevant inequality is 2e+2 <= 2(2e+1); the remaining factors and powers of 2 also obey (9). The convergence of sum_s tau(s^2)s^(-3/2) follows, for example, from tau(s^2)<=tau_3(s). Thus no harmonic truncation is needed for (9).

The elementary disk area estimate sum_(n<=x)r2(n)<<x and partial summation imply

    sum_(d<=Q) A_d(T) << Q^(1/4).                        (10)

The divisor bound and dyadic summation give, for every fixed eta>0,

    sum_(d>Q) A_d(T)^2 <<_eta Q^(-1/2+eta).              (11)

Choosing the input divisor exponent sufficiently small relative to eta/p and raising (11) to p/2 proves

    V_Q(R)^(p/2) <<_(p,eta) Q^(-p/4+eta).

Since integral dmu=T integral w, this proves the last line of (1). More general fixed-h estimates are available by the same divisor argument, but no new all-order graph statement is needed: (11) alone suffices for the relative reduction.

For each fixed T, Schwartz decay gives sum_n |a_n(T)|<infinity. Therefore sum_d A_d(T)<infinity, uniformly in R. This justifies grouping by squarefree part, every harmonic, the infinite ordered distinct polynomial, and passage of the finite identity under dmu. The possibly T-dependent l1 bound is used only to justify convergence; it is not inserted as a power loss into (1). Confusing this fixed-T summability with the divergent sum of the uniform majorants in (9) would be an error.

From (10),

    M_p(L_Q) <<_p T Q^(p/4).                             (12)

For Q=1, (1) and (12) are O(T), uniformly in T. For Q=floor(T^(1/p)), the elementary inequalities

    (1/2)T^(1/p) <= Q <= T^(1/p)

hold for every T>=2. They give K << T^(3/4+epsilon) and M_p(L_Q)<<T^(5/4). The lower comparison contributes a fixed factor such as 2^(p/4), which is harmless only because p is fixed. Floors are therefore retained rather than suppressed as an unqualified identity.

### 3.4 Optional sharper complete head, proved through the allowed finite mechanism

This refinement is not required for the coarse order-independent bridge. The Round204 finite block proof depends on the coefficient l2 energy and the full ambient unweighted square-root Gram kernel. Setting coefficients to zero unless their squarefree part is <=Q changes neither its hypotheses nor the Gram kernel. Retain the singleton n=1, truncate only above T^(3/2), and use the Schwartz/divisor estimate to bound the omitted tail uniformly by O_A(T^-A). Zero-extend partial blocks in their full dyadic ambient intervals. The coefficient energy in each block remains at most T^eta N^(-1/2), and all masks are independent of R. The finite Gram proof, its full diagonal, the 1+T/h localization ceiling, and the union of O(log T) block level sets therefore give

    D_(L_Q)(v) <<_epsilon T^epsilon(v^-2+T v^(-q)),
    q=136/13, v>=1.                                    (13)

This is a proof from the accepted finite mechanism, not an assumption that its stated lower-cutoff theorem automatically covers arbitrary masks. The underlying accepted source qualifications are unchanged.

Combine (13) with the complete ceiling |L_Q|<<Q^(1/4), then apply layer cake. For every fixed even p>=2,

    M_p(L_Q) <<_(p,epsilon) T^epsilon
                  [T+Q^((p-2)/4)+T Q^((p-q)_+/4)].      (14)

At p=2 the first integral has a logarithm, absorbed in T^epsilon for either proposed Q. More generally a logarithm in Q must be retained if Q is unrestricted and p=2; the displayed form (14) is asserted here for Q=1 or Q=floor(T^(1/p)), which are the only uses of it. Since q is not an even integer, p=q does not occur. Bounded T is covered by enlarging fixed constants. Formula (14) proves (3); for even p<=10, h_p=1.

For any nonnegative target budget A(T) which dominates K_(p,Q) and M_p(L_Q), (2) proves the equivalence

    M_p(B)=O(A)  <=>  |I_(p,Q)|=O(A)
                   <=> I_(p,Q)<=C A.                    (15)

Thus for Q=1, exponent targets T^(b+epsilon) are equivalent when b>=1. For Q=floor(T^(1/p)), the refined sufficient condition is b>=h_p; b>=5/4 suffices without (13). If a proposed b is smaller than the paid head or error exponent, one must take their maximum instead of asserting (15) at b unchanged.

### 3.5 Thresholds, the sharp circle, and the order of quantifiers

The argument above is a complete moment argument and requires no value threshold. If one chooses instead to work on {|B|>V}, the implication |Z_Q|>|B|/2 requires V>=2C Q^(1/4), with C from (10). For Q=floor(T^(1/p)) a threshold T^nu meets this eventually when nu>1/(4p); equality requires a constant check. Transferring a high event does not pay the complementary low values. Those must be bounded separately, for example by O(T V^p) or the complete layer-cake bound. A high-value assertion alone is not silently promoted here.

The accepted actual reconstruction, with the same fixed smoothing width T^(-1/2) throughout the R window, is

    P(R^2) = sqrt(R) B_T(R)/pi + O_epsilon(T^(1/2+epsilon)).

It includes inclusive endpoint jumps and the full convergent Bessel remainder. With Y=T^2, w=1 on the required radius interval, and dx=2R dR, a complete normalized estimate M_p(B)<<T^(b_p+epsilon) yields

    integral_(Y/2)^(3Y)|P(x)|^p dx
       << T^(1+p/2+b_p+epsilon)+T^(2+p/2+epsilon)
       << Y^(A_p+epsilon),
    A_p = max(1+p/4,(1+p/2+b_p)/2).                      (16)

The smoothing term is indispensable. The p-dependent loss in its epsilon is absorbed by choosing the input epsilon after fixing p.

For completeness, persistence uses monotonicity of the inclusive count. If P(x_0)=H>0, then P(x_0+h)>=H-pi h for h>=0. If P(x_0)=-H<0, then P(x_0-h)<=-H+pi h for h>=0. Hence one appropriate one-sided interval of length H/(2pi) has |P|>=H/2. For x_0 in [Y,2Y], this interval lies in [Y/2,3Y] for large Y, using the elementary disk/unit-square bound |P(x_0)|<<sqrt(Y)+1. Formula (16) therefore gives

    |P(x_0)| <<_(p,epsilon) Y^(A_p/(p+1)+epsilon).        (17)

The denominator is p+1, not p. Real endpoints and either sign are included.

An unbounded sequence of fixed even p with b_p=o(p) would imply the quarter target, since A_p/(p+1) tends to 1/4. Equally, one-sided estimates on I at exponents b_p=o(p) suffice after replacing b_p by max(b_p,1) for Q=1, or by max(b_p,h_p) for the second cutoff. Given a desired final epsilon, choose a sufficiently large p from that sequence and then keep it fixed while T tends to infinity. No uniformity in p is needed for this quantified implication. In contrast, setting p=p(T) is unsupported: (5), all divisor constants, moment constants, and sufficiently-large-T thresholds can grow with p.

## 4. First doubtful or unproved step

There is no unresolved algebraic step in (4), and the stated actual convergence and head/error transfers follow from the allowed accepted kernels and the derivations above. The first remaining arithmetic step is a useful one-sided estimate

    I_(p,Q)(T) <= C_(p,epsilon) T^(b_p+epsilon)             (18)

for the literal complete signed integral. To reach the full target by this route, such estimates must hold on an unbounded sequence of fixed even orders with b_p=o(p). No such family is proved in this report.

The exact remaining Fourier expression is

    I_(p,Q)=T 2^(-p) sum_(epsilon_j in {+1,-1})
       sum_(distinct squarefree d_j>Q; s_j>=1)
       [product_j a_(d_j s_j^2)(T)] e(-3 sum_j epsilon_j/8)
       w-hat(-T sum_j epsilon_j s_j sqrt(d_j)).           (19)

It is real by conjugate pairing, but its summands are signed/complex. Distinct squarefree radicals ensure nonzero frequencies through the accepted independence fact; they do not establish sufficient quantitative separation on the physical T window. Infinite harmonics and the smoothing factors must stay in (19).

The already accepted graph entry `GC-distinct-radical-absolute-certificate-obstruction` applies to Q=1 (alpha=0) and to floor(T^(1/p)) (alpha=1/p) for each fixed even p>=4. It gives a positive subcollection of the termwise absolute Fourier certificate of size at least c_p T^(p/4-1/2). Thus a strategy taking every tuple in modulus cannot establish a sublinear-in-p exponent family. This is an inherited graph obstruction, not a newly reproduced proof and not a lower bound for signed I.

The relative absorption proof uses only real algebra and a square-sum envelope. It provides no arithmetic cancellation absent from that envelope. Feeding the inherited baseline moment into the reverse bridge merely recovers signed-integral bounds of baseline size; feeding those bounds back proves no improvement. The conductor should promote only a reduction, if its remaining review gates pass.

## 5. Required control tests and outcomes

All controls here are exact analytical checks, not numerical evidence.

- `finite_partition_identity`: PASS. Equation (6) has ordered multiplicity one for distinct labels and zero for every tuple with a repeated label. Its absolute coefficient sum is p!.
- `relative_absorption`: PASS. Equations (7) and (5) give a uniform family-size bound. For V=0 both sides vanish. For fewer than p labels, E_p=0; Cauchy-Schwarz gives |Z|^p<=m^(p/2)V^(p/2), consistent with the fixed-p constant. For m equal values x, E_p=(m)_p x^p and Z^p=m^p x^p; the relative repeated-class cost tends to zero as m grows for fixed p. This does not provide a p-uniform constant.
- `signed_integral_negative_part`: PASS; the positivity shortcut is REJECTED. For p=2 and (x_1,x_2)=(1,-1), Z=0, V=2, E_2=-2. More generally, exactly p labels consisting of p-1 copies of 1 and one -1 give E_p=-p! for even p. Constant functions on a positive measure set make I negative. Equation (8) pays the negative part without assuming its disappearance.
- `actual_harmonics_and_head`: PASS at the stated scope. Equations (9)-(12) retain every harmonic and uniformity in real Q. Fixed-T l1 convergence and uniform-in-T l2 bounds have separate roles. The floor factors are explicit. The optional refinement (14) is restricted to the proposed cutoffs, avoiding an unabsorbed log Q at p=2 for arbitrary Q.
- `fixed_order_quantifiers`: PASS. The implication to a quarter exponent uses an unbounded sequence of fixed p, with p chosen after the desired final epsilon. A choice p(T) is REJECTED as unsupported.
- `complete_sharp_restoration`: PASS. Equations (16)-(17) retain sqrt(R)/pi, dx=2R dR, the full smoothing term, both signs, inclusive jumps, and denominator p+1. High-event transfer alone is explicitly insufficient without the low levels.
- `no_unproved_signed_gain`: PASS. Neither (18) nor a new full moment is claimed. Constant artificial functions with many equal positive entries have V fixed but Z^p and E_p both growing with the number of entries, demonstrating that algebra alone cannot bound I. This is an abstract control, not a counterexample to the actual arithmetic family. The inherited actual absolute-certificate obstruction remains intact.
- `wolfram_exact_local_reproduction`: NOT PERFORMED BY THIS TASK. The conductor explicitly owns that separate diagnostic control. No computational pass is claimed; no computation is needed for the proofs above.
- `blind_isolation`: PASS for this task's selected-context scope. No sibling was read; this report is independent but is not the separately commissioned statement-only report.
- `graph_history_preservation`: PASS for task actions. Only the assigned report was written. The accepted Round216 additive twelfth-order result is retained without replacement or weakening. All parent targets remain open.

## 6. Dependencies and exact artifacts used

No external source was imported. The accepted Round204 finite block mechanism and sharp reconstruction were used with their existing qualifications; the accepted Round216 coefficient/divisor argument was rederived as needed. The graph's absolute-certificate obstruction is cited only at its already accepted statement. The historical Round232 reassessment supplies the restriction against mislabeling this as a third local upper-tail attempt.

The exact read context and SHA-256 hashes are:

| Artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `state/active_campaign.yml` | `58f07ad6959a485751d27e4df55fddc72d6cba7a474ce824c1426a390ab21b15` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/hostile_bridge_audit.md` | `d1235dbc32d40221b1db5c31bd5c50964db8dce3e9853467f0af7725423050d6` |
| `rounds/codex-managed/gc-fixed-order-moment-absorption/briefs/actual_interface.md` | `f7ca86a3d0565aff3234286b0f0949a02920ccd91af0521f51aa3bb3baa338a4` |
| `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` | `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee` |
| `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` | `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212` |
| `rounds/codex-managed/gc-upper-tail-separated-products/candidates/strategy_reassessment.md` | `286415c548b027b986f939d17ef9654d51a4d5083253d2df09117d656a20c476` |

Relevant graph entries inspected: `GC-target`; `GC-complete-square-root-large-values-moment-bound`; `GC-complete-distinct-radical-twelfth-reduction`; and `GC-distinct-radical-absolute-certificate-obstruction`. Referenced historical evidence paths inside those artifacts were not opened.

Effort allocation: analytical/algebraic 100%; numerical experimentation 0%. Filesystem reading, writing, and hashing are not mathematical experiments.

## 7. Recommended state effect

Recommend RETAIN as a valid candidate for a narrow all-fixed-even-order complete relative reduction, and PROMOTE only after the conductor's distinct final-hash seams, statement-only rederivation, separate diagnostic control, and mechanically validated State Patch all pass.

The promoted statement, if any, should include the nonnegative I+K interpretation, complete head costs, fixed-order quantifiers, full sharp restoration, and explicit open signed estimate (18). It should not claim a stronger additive approximation, a new complete moment, a new pointwise exponent, or the quarter theorem. Preserve the existing accepted twelfth-order lemma and all inherited obstacles. No next round is proposed or started by this task.
