# Round 202 conductor independent analysis

Campaign gc-strategy-signed-moment-majorant-review; 2026-09-23.
Starting graph SHA-256 682cb189a3ab0ef26f8d19701e2949547446d37505df01f7b7eaf1cfdd0f359c.
Context: protocol, current graph, closed Round200/201 syntheses,
user-supplied strategy review, and Round202 frozen strategy. This
derivation does not use the blind report. Analytical work only.

## Physical near-resonance mass

Take a fixed positive band n/T in [a,b] near zero, where Psi>=1/2.
Elementary disk area counting supplies sum_band r_2(n)>>T, so its
coefficient l^1 mass is >>T^(1/4). The weighted six-root-sum measure
has total mass >>T^(3/2), support length O(sqrt(T)), and hence at most
O(T^(3/2)) bins at resolution h/T. The sum of squared bin masses is
>>T^(3/2), by Cauchy. It counts ordered six-plus/six-minus near
resonances. Delete their O(1) exact mass by the Round201 accepted
lemma. Fourier continuity at zero gives positive real weight on these
remaining differences, proving a T^(5/2) positive subsum. This proves
the proposed majorant obstruction for actual coefficients, not for an
arbitrary adversarial vector. A full proof and sign controls are in
the conductor formal kernel.

The bin width is 1/T, the six-root support width is sqrt(T), and the
twelve weights total l^1 mass to the twelfth power is T^3. Therefore
the complete power is T * T^3/T^(3/2)=T^(5/2). No representation-number
or tuple-permutation factor has been suppressed. This exceeds the
required T^(1+2eta), but does not bound the signed moment below.

## A cutoff-dependent necessary constraint

For a positive band n~U with 1<<U<=bT, the same argument has mass
>>U^(1/4), support width O(sqrt(U)), and O(T sqrt(U)) bins. Thus at
order 2k its positive near-frequency contribution, including the
outer T and after exact deletion, is at least

  c U^((k-1)/2) - C T.

At order twelve this is c U^(5/2)-CT. A termwise absolute low-part
bound of size T^(1+2eta+epsilon) therefore necessarily requires
U^(5/2)<=T^(1+2eta+o(1)), or cutoff exponent
alpha<=2(1+2eta)/5 when U=T^alpha, in any range where the leading
term dominates. At the improvement threshold this is about0.470625.
This is a necessary restriction only, not a sufficient spacing bound.
A low cutoff also creates an actual high-frequency remainder; all
its mixed terms must be included or controlled before reconstruction.

## The complete proof frontier

The graph still has five independent analytic burdens across the
standard route: smooth M1; the full hard M1 residual, of which original
t=1 is only one sector; M2 TOP; M2 BAL including label completion;
and M2 UNBAL. Endpoint uniformity and one-count assembly remain
mandatory. The total-M1 alternative does not eliminate M2.

The graph statements were re-read directly. Smooth M1 first loses
X^(1/12). Hard M1 retains t>=2 and large-gcd near-resonant incidences
beyond the recombined t=1 source. M2 TOP requires the full signed
density-discrepancy energy; BAL keeps both critical j=1 energy and
other owner completion; UNBAL requires a literal signed matrix theorem,
not scalar inverse-residue cancellation. No Round200/201 component
closes those unrelated obligations.

This favors testing a complete whole-discrepancy route when its new
input is concrete. It does not authorize treating the moment route
as easier than those components: the positive mass calculation exposes
one reason its complete signed high-moment cancellation is difficult.
The strongest verified numerical exponent remains the repaired
Li--Yang value, with its general printed statements explicitly excluded.

## Literature and successor boundary

The conductor ran a fresh dated search and delegated exact theorem
and cutoff-source audits. Search snippets and third-party summaries
are not proof evidence. The primary numerical September2026 lead is
assigned for a computation/theorem scope check. Source and tail reports
must determine whether there is a new concrete inequality to attack.
No next-round objective is selected until their reviewed results and
this round's graph decision are closed. The next broad checkpoint is
Round205; source checks remain necessary in intervening rounds.

## Independent radical-separation seam

For a nonzero sum Delta of k signed roots sqrt(n_j), n_j<=U, let r
be the rank of their rational squareclasses over F_2. Its multiquadratic
field has degree2^r. Delta is a nonzero algebraic integer and every
conjugate has modulus<=k sqrt(U), so its nonzero integer norm has
absolute value at least one. If r<=k-1 this immediately gives
|Delta|>=(k sqrt(U))^(-(2^(k-1)-1)). If r=k, all k classes are
independent, so the simultaneous sign flip is an automorphism: both
Delta and -Delta occur in the 2^k field embeddings. Remove those two
factors from the norm and take a square root to obtain the same bound.
This covers perfect-square indices and dependent classes without
assuming an invalid global sign flip in their field.

For k=12 the resulting power is U^(-2047/2), not U^(-4095/2).
Thus U=T^(1/2047) gives T|Delta|>=c T^(1/2). Smooth Fourier decay
can dominate the polynomial l1 coefficient mass of the finite head,
while its entire exact part is O(T). This independently validates a
target-safe head cutoff at that exponent, provided the signed-tail
report states the rank split explicitly. The naive degree-only norm
argument would not suffice at this cutoff; that distinction was sent
to the task as a review question before closure.
