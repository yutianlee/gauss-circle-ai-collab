# Round 216: a complete reduction to distinct radical classes

Campaign: `gc-actual-radical-high-values`. Conductor synthesis, 2026-09-28.
The frozen objective was the actual complete twelfth high-value estimate
H216, with threshold T^(13/125) and target T^(29/25+epsilon).
The terminal label is `complete_actual_high_value_gate_open`.

## 1. Decision and accepted scope

The State Patch accepts one narrow lemma,
`GC-complete-distinct-radical-twelfth-reduction`. It pays the entire
small-class head and the collective contribution of every repeated
large squarefree class. It does not prove H216 or improve the accepted
complete moment or pointwise exponent. All 399 preceding graph nodes
remain unchanged. Acceptance is defined by the validated graph, with
the proof in `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md`.

This is a complete reduction with quantified remainder costs. It is
stronger than retaining only the exact-frequency diagonal: repeated
classes with nonzero aggregate frequency are also paid. The unestimated
part is explicitly the full correlation over twelve distinct classes.
No novelty claim is made.

## 2. Exact mathematical result

Use the frozen actual radial mollifier, nonnegative window w, and full
real series B_T. Write n=d s^2 with d squarefree, retain every s, and put
Q=floor(T^(2/5)), B_T=L_Q+Z_Q. Let f_d be the full class wave and let

    E12(R)=sum_(d_1,...,d_12>Q squarefree, pairwise distinct)
                                             product_j f_(d_j)(R),
    I12(T)=integral w(R/T)E12(R)dR.

Tuples are ordered. With beta=2theta_LY-1/2, the accepted result is

    M12(L_Q) << T^(15/13+epsilon),
    integral w(R/T)|Z_Q(R)^12-E12(R)|dR
                                  << T^(8beta-1/5+epsilon).

The second exponent is approximately 0.831731 and is less than 21/25.
The head exponent is below 29/25 by exactly 2/325. Consequently the
following bounds, each quantified for every positive epsilon, are
equivalent: H216; M12(B_T)<<T^(29/25+epsilon);
M12(Z_Q)<<T^(29/25+epsilon); and |I12(T)|<<T^(29/25+epsilon).
A one-sided upper bound on I12 also suffices because its negative part
is already bounded by the error. None of these equivalent bounds is
established. The small additive approximation concerns M12(Z_Q), not
M12(B_T); the latter transfer uses the paid head and power inequalities.

## 3. Why the repeated classes can be paid

The actual prime-factor comparison r2(d s^2)<=r2(d)tau(s^2), combined
with elementary lattice counting, gives the uniform head bound Q^(1/4).
The accepted finite large-value proof extends to these fixed masks by
zeroing inactive coefficients without changing its ambient correlation
kernel. Its full diagonal, localization ceiling, singleton, partial
blocks and Schwartz tail are retained. Layer cake gives the head
moment and the lower actual Z_Q moments through order ten.

Set p_h=sum_d f_d^h. The exact set-partition identity is

    E12=sum_(pi partition of [12])
         product_(C in pi)[(-1)^(|C|-1)(|C|-1)! p_(|C|)].

The singleton partition is Z_Q^12. Every other partition has at most
ten singletons, leaving signed powers Z_Q^r multiplied by small
higher class power sums. The class bound
sum_(d>Q) A_d^h<<Q^(1-3h/4+epsilon) and the lower signed moments
pay all these profiles. The largest error is the single-pair profile
Q^(-1/2)M10(Z_Q), giving T^(4/5)+T^(8beta-1/5). Absolute convergence
justifies the finite-to-infinite passage before applying full-Z moments.
Taking absolute values on the original repeated tuples would lose
this signed regrouping and is not the argument.

## 4. The surviving gap and independent route

The remaining expression is exactly

    T 2^-12 sum_(epsilon in {+1,-1}^12)
      sum_(distinct squarefree d_j>Q; s_j>=1)
      product_j a_(d_j s_j^2)(T) e(-3 sum epsilon_j/8)
                 w-hat(-T sum epsilon_j s_j sqrt(d_j)).

Every frequency is nonzero, but no adequate quantitative separation or
cancellation estimate follows. The original positive-radius window is
still present in the Fourier transform. Replacing it by torus averaging
or a positive frequency count would discard the missing argument.

The independent divisor report opens r2=4(1*chi4) before cofactor
Cauchy. Its real energy retains R_j sqrt(d)-R_l sqrt(e) and
R_j sqrt(d)+R_l sqrt(e), including the latter's minus-sine phase.
The exact signed energy input with loss rho implies
H12<<T^(113/125+42rho/13+epsilon); rho=208/2625 gives 29/25.
That signed input is open. The available absolute kernel estimate
instead costs J sqrt(N)+J^2 T^(13/55)D^(34/55), and does not close it.
This is retained as a priced conditional interface, not an accepted
new arithmetic estimate or a universal obstruction.

## 5. Controls, independent derivations and sources

Three original reports were frozen before their reviews. The isolated
cutoff report derived every-sign exact mass, threshold transfer and a
fixed generic coefficient counterexample to exact-to-finite-window
inference. Its coefficients are not the actual circle coefficients.
A separately isolated abstract packet produced an independent full
partition identity, exhaustive exponent table, infinite-limit argument
and signed-integral transfer without access to the claimant or ledger.

Independent final-hash reviews cover the complete candidate, the
original radical report, the actual head and masked distribution, the
conductor's actual controls, and the anchored divisor report. The
conductor also checked the original isolated cutoff report. All reviews
retain their blind or nonblind provenance; no claim is accepted by vote.
The candidate's exact bytes become the final kernel.

The actual quadratic norm family m^2+1,m^2+25,m^2+49 survives the
cutoff outside O(Q) radius parameters and has a nonzero frequency of
order m^-3. This controls frequency-separation claims only. Its repeated
classes are already covered by the new collective estimate. The
T^(5/2) positive frequency certificate is also only a limitation of a
termwise absolute closure, not a lower bound on the signed moment.

No new external theorem is accepted. The qualified Li--Yang final
application and the existing Bourgain square-root kernel retain all
their restrictions. The divisor report rechecks the latter primary
source's proper-interval interface. All mathematical work is analytical
or algebraic; numerical experiments number zero. Mechanical hash,
schema, dependency, inverse and replay checks are not mathematical proof.

## 6. Full-goal assessment

The complete bound remains M_p(B_T)<<T^(1+epsilon)+T^((p-2)beta+epsilon).
Even a proof of I12 at 29/25 yields only the 102/325 pointwise milestone.
The one-pair term at general p can retain
Q^(-1/2)[T+T^((p-4)beta)], so this round gives no sufficient family
E(p)=1+o(p) along unbounded fixed p and no quarter theorem.

Hard M1 still includes all its original small-t and large-G sources;
smooth M1 remains independent. TOP, BAL and UNBAL in M2, the actual
joint coefficients, moving endpoints, stars, floors and short blocks
remain open. A total-M1 GAR route would still leave M2. Whole physical
moments could bypass those parents only after their own complete bound;
the new reduction does not prove any of them.

## 7. Closure and successor discipline

The closure verifies the frozen target and briefs, final report hashes,
373 archived entries from rounds200--215, and all required green gates.
The create-only patch is checked on the accepted dependency cone,
reversed to the original graph bytes, and replayed. Only after its
validated application is the proof draft appended, preserving its old
bytes. Legacy evidence remains immutable. Historical mathematics is
not globally recertified by these mechanical checks.

Round217 is the mandatory broad strategy and current-literature review
after214--216. Its analytic successor remains unselected. That review
must compare the new distinct-class interface, the anchored signed
energy and every full-proof frontier against current primary sources;
it must not silently continue the fixed twelfth-moment milestone as
though it were the full quarter goal. No217 task starts before216 closes.
