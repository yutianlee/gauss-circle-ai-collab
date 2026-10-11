## 1. Result: bounded source-import no-go and finite-window cost

Campaign: `gc-full-goal-distinct-source-review`; round 217; task
`distinct_correlation_sources`; role: source auditor, selected context,
nonblind candidate evidence. Generated 2026-09-28, local Asia/Shanghai.
Starting and rechecked graph SHA-256:
`f7c8b74e9acaa3bf5234c3678f20e2aaf8dbb9ba6179f73d839fa2f0537a14d7`.
Work allocation: analytical/algebraic/source work 100%; experiments zero.

Neither of the two fully audited theorem interfaces supplies the complete
actual twelve-distinct-class integral or an unbounded-order moment family.
Xiao's current fourth-moment theorem fails its frequency-length range
already on the physical transition block. Zhai's actual-circle
higher-moment theorem first requires a higher optimal absolute moment
which is unavailable. These are application failures, not refutations of
the sources, the arithmetic target, or either broader method.

An elementary finite-window lemma below also quantifies why radical
independence is insufficient here. For p distinct classes and indices at
most U it gives a separation certificate of size U^(-A_p), where
A_p=(2^(p-1)-1)/2. At p=12, A_p=2047/2. A cutoff small enough for that
certificate to ensure oscillation on a window of length T is far below
the already growing class cutoff Q=T^(2/5). The paid reduction therefore
does not make qualitative torus independence a quantitative estimate.

No new estimate of I12, complete physical moment, pointwise exponent,
M1/M2/GAR parent, or quarter theorem is obtained. The new comparison
below also rules out a bootstrap using only the existing moment exponents
and the audited moment theorem.

## 2. Exact hypotheses and primary theorem interfaces

Use the accepted216 mollifier and window: rho is real, nonnegative,
radial, smooth, supported in the unit disk, with integral one;
Psi(s)=rho-hat(s e1). The fixed smooth w is nonnegative, supported in
[1/2,2], and equals one on [1/sqrt(2),sqrt(3)]. For every real T>=2,

    a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    f_d(R)=sum_(s>=1) a_(d s^2)(T)cos(2pi R s sqrt(d)-3pi/4),
    Q=floor(T^(2/5)), Z_Q=sum_(squarefree d>Q) f_d,
    I12(T)=integral w(R/T)
           sum_(ordered distinct squarefree d_1,...,d_12>Q)
                                     product_j f_(d_j)(R)dR.

Every harmonic, sign and upper tail is included. The r2 coefficients are
representation multiplicities, not representability indicators. They and
the mollifier are fixed by this problem. Set beta=2theta_LY-1/2 with all
existing source qualifications. The inherited target is the one-sided
bound I12(T)<=C_epsilon T^(29/25+epsilon), equivalent to the full
twelfth-moment milestone by accepted216. No positivity of its integrand
is presumed.

**Interface A, current square-root moments.** Yixiu Xiao,
[*Moment Estimates and Discrepancy for Sums of Square Roots Modulo One*,
arXiv:2606.28986v1](https://arxiv.org/abs/2606.28986v1), sole listed version
27 June 2026; primary [Theorem 1.2](https://arxiv.org/html/2606.28986v1#S1.SS1)
and definitions (1.1)--(1.2). With integer summation variables,

    S(h,n)=sum_(n/2<=a<=n) e(h sqrt(a)),
    M4(H,n)=sum_(H/2<=h<=H) |S(h,n)|^4,

for fixed 0<delta<1/6 and epsilon>0 the theorem gives
M4(H,n)<<_(epsilon,delta) H n^(2+epsilon) uniformly only when
n^(1/2+delta)<=H<=n^(2/3). Coefficients in S are one.
The higher-order ideal bounds in Section3.8 are conjectural.
The first stopped application is H~T,n~T: T<=T^(2/3) fails.
No continuation past that failed range, weighted extension, or continuous
sampling theorem is credited.

**Interface B, actual-circle higher moments.** Wenguang Zhai,
[*On higher-power moments of Delta(x)(II)*,
arXiv:0805.1270v1](https://arxiv.org/abs/0805.1270v1), sole listed version
9 May 2008; journal Acta Arith.114 (2004),35--54,
[DOI 10.4064/aa114-1-3](https://doi.org/10.4064/aa114-1-3).
The primary [Theorem3, PDF p.6](https://arxiv.org/pdf/0805.1270v1)
assumes A0>9 and, for every epsilon>0,

    integral_1^Y |P_source(x)|^A0 dx << Y^(1+A0/4+epsilon).

For integers 3<=k<A0 it gives

    integral_1^Y P_source(x)^k dx
        = C_k Y^(1+k/4)+O(Y^(1+k/4-delta1+epsilon)),
    C_k=(-1)^k B_k(r2)/[(1+k/4)2^(k-1)pi^k].

Here B_k is the exact-resonance constant in (1.5)--(1.6),
K0 is the least even integer >=A0,
b(k)=2^(k-2)+(k-6)/4, delta1=sigma(k,A0)/(2b(K0)), and
sigma=1/4 when k-1<A0/2, otherwise (A0-k)/(2(A0-2)).
The source counts positive n; adding the origin changes P by one and
preserves its absolute-moment hypothesis. The first failed hypothesis
for k=12 is the required optimal A0-moment at some A0>12.

Both current arXiv records and primary statements were checked on
2026-09-28. No external theorem is proposed for graph acceptance.

## 3. Derivation and complete costs

**Literal signed window.** Absolute convergence for each fixed T gives
the exact expansion

    I12 = T 2^-12 sum_(epsilon_j=+/-1)
          sum_(distinct squarefree d_j>Q; s_j>=1)
          product_j a_(d_j s_j^2)(T)
          e(-3 sum_j epsilon_j/8)
          w-hat(-T sum_j epsilon_j s_j sqrt(d_j)).             (1)

Changing every sign conjugates a term, so the total is real. The Fourier
transform here belongs to the actual positive-radius window. Even for
w>=0 its value at a nonzero frequency need not be nonnegative or real.
Neither replacing it with a centered positive kernel nor taking all
terms in modulus preserves the unproved cancellation claim.

**A proved algebraic certificate, including all harmonics.** Let p>=2
be fixed; take pairwise distinct positive squarefree d_j, positive s_j,
n_j=d_j s_j^2<=U, and Delta=sum_j epsilon_j sqrt(n_j). Then

    Delta != 0,
    |Delta| >= (p sqrt(U))^(-(2^(p-1)-1)).                    (2)

Indeed every signed combination is nonzero by the accepted radical
independence. The polynomial product over all 2^p formal sign choices
of sum_j eta_j sqrt(n_j) is an integer: it is invariant under separately
changing each formal square root's sign, hence is a polynomial in the
n_j with integer coefficients. It is nonzero, so its modulus is at
least one. Its two factors Delta and -Delta have product modulus
|Delta|^2; each remaining factor has modulus at most p sqrt(U).
This proves (2), without assuming multiplicative independence of the
squareclasses. Harmonic sizes are already incorporated in n_j.

For the integral of one character, integration by parts gives

    |integral w(R/T)e(R Delta)dR|
       <= min(T||w||_1, ||w'||_1/(2pi |Delta|)).              (3)

Writing I_(p,U) for the truncated p-distinct-class expression, the
divisor envelope and sum_(n<=U)|a_n(T)|<<U^(1/4+epsilon) give

    |I_(p,U)| <<_(p,w,epsilon)
                  U^(p/4+epsilon) min(T,U^A_p),
    A_p=(2^(p-1)-1)/2.                                     (4)

This is a valid but weak bound; it is not a lower bound for I_(p,U).
At p=12 its integration-by-parts certificate is U^(2053/2+epsilon).
Using that branch alone to reach T^(29/25) would require
U<=T^(58/51325), whereas a nonempty retained class needs U>Q~T^(2/5).
The other branch is T U^3 and does not supply the target on that range
either. Repeated integration by parts improves matters only after
T U^(-A_p) is large. Its sufficient condition U=T^eta,
eta<1/A_p=2/2047 at p=12, is again below Q. Thus this elementary
uniform-separation certificate cannot certify the retained integral.

For a genuinely fixed finite family, (3) divided by T tends to zero
term by term; this recovers its torus average. Each individual f_d has
zero torus mean, so the distinct product has zero mean. The argument
does not give a uniform rate when d, s and the number of terms grow
with T. Formula (4) records the lost uniformity explicitly.

**Full upper tails and unequal ranges.** At U=T^(3/2), the accepted
Schwartz estimate gives sum_(n>U)|a_n(T)|=O_A(T^-A) for any fixed A.
Moreover sum_n|a_n(T)|<<T^(1/4+epsilon); this follows by dyadic summation
of the divisor envelope and arbitrarily high fixed Schwartz decay.
The omitted terms of a fixed p-fold distinct expansion are bounded
by p times the tail mass times the (p-1)-st power of the total mass,
and their integral costs a further O(T). Choosing A large in terms
of fixed p pays the entire tail. This grants no small tail at
U=T^eta with eta<2/2047. It also proves why all harmonics above a
small cutoff cannot simply be erased. A common upper cutoff is used
only in the weak certificate (4); unequal original blocks remain in
(1) and in the tail union bound. No equal-block reduction is imported.

**An ideal positive-count comparison, expressly hypothetical.** Even
if one were handed a p-root absolute spacing estimate on n_j~N of
the random-density form

    count{|Delta|<=h} << N^epsilon (N^(p/2)+h N^(p-1/2)),     (5)

using it only after taking absolute values in the Fourier expansion
would give, by dyadic shells h~2^j/T and rapid Fourier decay,

    integral certificate << T^epsilon
                      (T N^(-p/4)+N^(p/4-1/2)).            (6)

This calculation uses the actual envelope |a_n|<<N^(-3/4+epsilon).
At p=12,N~T its second term is T^(5/2), much larger than T^(29/25).
For unbounded fixed p it has linear slope 1/4. Removing exact or
repeated classes does not, by itself, remove the density term in a
supplied upper bound. Equations (5)--(6) assert neither a proved
spacing theorem for distinct classes nor a matching lower bound;
they quantify the insufficiency of that positive certificate. A
signed cancellation estimate could be much smaller.

**The two stopped source transfers.** Interface A does not cover even
the unweighted transition test. Its integer h cannot be replaced for
free by R=h+t: the coefficient becomes e(t sqrt(n)), and translations
of the interval introduce further fixed phases. Absolute domination
of r2(n) by n^epsilon is not a weighted moment theorem. These are
additional unproved transfers, not permissions to continue the failed
import. Raising a fourth moment by a supremum factor would retain a
power linear in p and cannot supply the quarter family.

For Interface B, the accepted physical moment family is

    M_p(B_T)<<T^(1+epsilon)+T^((p-2)beta+epsilon).

Its sharp restoration is optimal at exponent 1+p/4 only through
q_star=2+1/beta, which lies strictly between 9 and 10. Thus existing
input can meet the audited source hypothesis only at orders below ten;
it cannot make the k=12 hypothesis true. Even hypothetical success
at the current I12 milestone restores the sharp bound Y^(102/25+epsilon),
which still exceeds the optimal twelfth power Y^4 and supplies no
optimal moment at A0>12.

There is also no automatic iteration. With E(p)=max(1,(p-2)beta),
the accepted restoration reads

    Theta(p)=[p/4+(1+E(p))/2]/(p+1).

For p>=q_star,

    Theta(p)-theta_LY=(1/4-3beta/2)/(p+1)>0,

since beta<1/6. For p<=q_star, Theta(p)=1/4+3/[4(p+1)] is
decreasing, and its value at q_star is still greater than theta_LY
by the same comparison. Hence the existing exponent family followed
by this bridge gives no improved pointwise input with which to restart
the process. A recursive argument needs a new complete estimate and
its availability at each changed cutoff/order; neither source supplies
that premise.

## 4. First doubtful or unproved step

There is no doubtful algebra in (1)--(4). The first open analytic step
is a bound for the complete actual signed sum (1), retaining its thin
frequency scale |Delta|~T^-1 and its displaced window, strong enough
to give I12<=T^(29/25+epsilon). Distinctness proves Delta!=0 and pays
no quantitative mass cancellation at that scale.

The precise source stops are H<=n^(2/3) in Interface A and the optimal
A0>12 absolute-moment premise in Interface B. Neither is repaired by
radical independence. The earlier Lamzouri good-set and Matthiesen
thin-box gaps in the permitted205 control remain inherited barriers;
this report does not spend another full audit on those unchanged
imports or promote their exceptional complements.

For the full quarter goal the required output is a complete physical
family E(p)=1+o(p) along unbounded fixed even p, or another complete
parent route. Fixed-order success, torus moments, and an assertion
about a selected favorable frequency range are insufficient. A
general distinct-class program must pay the head and every repeated
partition at its chosen Q_p(T), as well as the signed distinct term;
the inherited one-pair term Q^(-1/2)[T+T^((p-4)beta)] shows why those
costs cannot be ignored. No assertion about optimal one-pass cutoff
powers is made here; that belongs to the isolated task.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| actual_coefficients | r2 multiplicities, actual Psi and phase remain in (1); no arbitrary weights are declared equivalent. PASS. |
| distinct_repeated_class_scope | Distinctness is used only to show all signed factors in (2) are nonzero. Accepted216 pays repeated classes; a three-class example is not relabeled as a twelve-distinct control. PASS. |
| finite_window_not_torus | Formula (3) and its explicit U cost distinguish fixed torus averaging from this growing family. PASS. |
| all_harmonics_signs_tails | All s and all 2^12 signs occur; the full omitted-index union bound pays Schwartz tails for every fixed p. PASS. |
| source_versions_hypotheses | Two exact primary theorem interfaces, version dates and first failed hypotheses recorded. No source import. PASS. |
| complete_norm_cost | Coefficient L1, p-fold product, radius measure and restoration costs displayed. Hypothetical positive-count certificate labeled. PASS. |
| real_endpoints | R and T are real throughout (1)--(4); w retains its prescribed window. Integer sampling cannot replace it. PASS. |
| full_quarter_family | E(p)=1+o(p) required; 29/25 is only the 102/325 milestone. PASS. |
| recursive_hypothesis_scope | Existing family cannot improve theta through the bridge; every improved-input step would need a new available complete bound. PASS. |
| signed_certificate_distinction | No upper certificate is a lower bound for the signed moment. No generic control refutes the arithmetic target. PASS. |
| statement_only_control | This report is explicitly nonblind; no sibling/blind packet was read and no independent-review status is claimed. PASS for isolation. |
| complete_frontier | M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, GAR, wave and anchored-energy alternatives retained below. PASS. |

As a normalization control for (2), p=2 yields
|sqrt(n_1)-sqrt(n_2)|>=1/(2 sqrt(U)), agreeing with rationalizing
the difference for unequal integers. The proof works when squareclasses
are multiplicatively dependent, because the formal full-sign product
is used. For (1), conjugate sign pairing verifies reality without
positivity. These are analytical controls; no numerical experiment was
used or needed.

## 6. Exact dependencies and screened sources

Permitted local artifacts actually read:

- `protocol.md` and this task's generated brief.
- `state/proof_obligations.yml` (target, M1/M2 frontier and accepted216
  node were extracted for the bounded audit; no whole-graph recertification).
- `state/active_campaign.yml`.
- `strategy/round217_full_goal_distinct_source_review.md`.
- `strategy/gauss_circle_strategy_review_2026-09-23.md`.
- `strategy/gauss_circle_strategy_checkpoint_round214_2026-09-28.md`.
- `rounds/codex-managed/gc-actual-radical-high-values/synthesis.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
- `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md`.
- `proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_arithmetic_source_gate.md`.

Only the primary texts in section2 support the two theorem audits.
Additional current screening used official primary records and did not
import their theorems:

- [Zhai0805.1523v1](https://arxiv.org/pdf/0805.1523v1), pp.3--5:
  fourth-circle moments and four-root spacing, including unequal ranges.
  This is a low-order comparison, not a twelve-root theorem.
- [Lester--Wigman2305.03549v2](https://arxiv.org/abs/2305.03549v2),
  version17May2023: boundary-point correlation/distribution problem.
- [Bordignon--Kurlberg2607.13659v1](https://arxiv.org/abs/2607.13659v1),
  15July2026: area observables for circle flows. Its abstract concerns
  a different correlation observable; no dictionary into (1) is claimed.
- [Robles--Zaharescu--Zeindler2609.03961v1](https://arxiv.org/abs/2609.03961v1),
  3September2026: linear phases over squarefree integers.
- [Robles2609.11070v1](https://arxiv.org/abs/2609.11070v1),
  10September2026: linear exponential sums with multiplicative
  coefficients. Its abstract's square-root displacement is not a real
  radical-phase theorem.

These last four were metadata/abstract scope screens, not evidence that
their full methods cannot be adapted. Search snippets and nonprimary
copies were discovery aids only. This bounded search makes no exhaustive
claim about the literature. Li--Yang's benchmark and qualifications are
inherited, not reaudited in this task.

## 7. Recommended state effect

**No change to accepted mathematics.** Retain accepted216's complete
reduction and its unestimated actual distinct integral. Archive the
two failed imports and the finite-window/full-family cost calculations
as strategy evidence. Do not promote the source hypotheses, the
hypothetical spacing estimate (5), or the target.

For selection by the conductor, the distinct-class formulation remains
a legitimate complete milestone because its complements are already
paid at p=12. Any new attempt should attack the signed expression (1)
through actual arithmetic and specify how its estimate extends to a
sufficient fixed-order family. This audit offers no source-backed
reason to prefer generic equidistribution or positive spacing over
the already priced anchored divisor energy. The latter's loss
rho<=208/2625 remains an unproved sufficient input, not an alternative
theorem obtained here. The localized wave objective likewise retains
its complete spatial/radius norm and unresolved narrow contribution.

All complete alternatives stay open: hard M1 includes all original
small-t and large-G contributions; smooth M1 is independent; M2 TOP,
BAL and UNBAL retain their joint arithmetic symbols, complements and
single outer absolute values. GAR would supply total M1 only and
still need M2. Every real endpoint, star, floor and short block remains
in its parent. A successful whole-physical-moment family could bypass
those parents for the final theorem but would not prove them individually.

This report chooses no successor round and changes no shared state.
The conductor must reconcile it with the isolated family derivation
and full-frontier audit before selecting one complete objective.
