# Independent review of the actual product covariance controls

Round231; campaign `gc-actual-upper-tail-a`; reviewer `signed_upper_tail_attack`, acting as nonauthor reviewer after freezing the independent discovery report. Reviewed artifact: `reports/resonance_hostile_controls.md`, SHA256 `89693f8519e735dbdd9582850e5465c85fef30835aeab50e398b16fe34f837e8`. Generated 2026-10-11. Candidate review evidence; no shared state or frozen report edited.

## 1. Result: pass at the stated scope

The arithmetic sign classification, actual positive/negative/disjoint localized covariance constructions, smooth d-Poisson decay estimate, and many-distinct-product necessary condition pass this review. No mathematical repair is required for their stated scopes.

Two clarifications should accompany any synthesis: at a nearest-q cell boundary there are two equally close d-Poisson aliases, both paid by the displayed bound; and the counterexamples concern the explicitly localized individual reciprocal contributions, not the full F or its high-level-set covariance. The reviewed report already preserves the second distinction. Neither control proves or disproves target A.

The global sign of the constructed main-term covariance is valid on the complete w window. Thus the proof does not rely on cancelling unexamined sharp endpoint pieces. The construction also survives replacement of the stationary leading fibres by their exact one-variable Poisson fibres, by the small per-fibre error estimated below; that robustness is not needed to correct the report.

## 2. Exact statements and hypotheses checked

The review uses the original frozen full-band interface and its actual fixed Psi, phi, character chi4 and radius measure. The reviewed controls take

    T=15g, N=T^(2/3), D=M=T^(1/3), W=T/sqrt(N),
    a_T(d,m)=4 omega(d/D)nu(m/D)phi(dm)(dm)^(-3/4)
                                      Psi(sqrt(dm/T)).

The functions omega,nu are fixed nonnegative smooth cutoffs with the supports and positive interiors stated in the report. This is an actual smooth summand of the divisor identity. No termwise positivity of chi4 or of the complete infinite Fourier series is assumed.

For each fixed h the report chooses one positive odd q through the half-open cell

    h(q-1)<=R^2<h(q+1).

It then localizes the actual leading real fibre by a fixed nonnegative tau((R^2-hq)/W). The tested statement is uniform power-saving decorrelation for every distinct pair of these localized fibres. The counterexample does not require uniform decorrelation of the complete unlocalized h sum to be false.

The packet estimate is pointwise, with every actual h assigned exactly once to p=hq. The resulting number-of-products statement is a necessary condition for a large event, not an estimate for the measure of such events.

## 3. Independent derivations and seam checks

### Arithmetic signs and genuine central amplitudes

Write h=ga, h'=gb with (a,b)=1 and aq-bq'=c. If a,b are odd, c is even. For odd v, chi4(v+c)=(-1)^(c/2)chi4(v), so multiplication by chi4(a)chi4(q') gives

    chi4(q)chi4(q')=chi4(ab)(-1)^(c/2).

At c=0 the solutions are q=bk,q'=ak, with k odd. If a,b have opposite parity then c is odd and the admissible odd solutions advance by (2b,2a), reversing the product character. These exhaust coprime a,b and verify the sign/valuation classification, including negative c.

On the selected amplitude support, dm is between fixed positive multiples of T^(2/3). Since 64/125<2/3<93/125, phi=1 for all sufficiently large T. Also dm/T tends uniformly to zero, so continuity and Psi(0)=1 imply uniform positivity. This verifies the amplitude sign without any extra hypothesis on Psi away from zero.

At R=T the stationary ratios m/d for h=5g,9g,7g,6g are respectively

    9/4, 25/36, 225/196, 25/16.

For d/D in a compact interval inside [1.02,1.08], all corresponding m/D values lie in the positive interior of nu. They remain there on a sufficiently small fixed relative interval around R=T. Hence b_h is comparable to T^-1/2 D^-1 on a d interval containing a positive proportion of odd integers.

### Positive, negative and disjoint covariance

For (h,h')=(5g,9g), common centers are p=45gk, k odd. Their spacing is 90g, comparable to T. An x=R^2 interval of length comparable to T^2 therefore contains comparable to T centers. Each detuned shoulder has exact R measure comparable to W/T=N^-1/2. On the shoulder, the sine argument is bounded away from zero on the chosen interior d interval, and remains within (-pi/2,pi/2) on the entire active support. Thus each fibre has magnitude comparable to T^-1/2 there.

If both localized fibres are nonzero, their centers differ by an even multiple of g but by at most 2c2W=o(g). Therefore their centers coincide. The character product is chi4(45)=1, and both sine sums have the same detuning sign. Every other factor is nonnegative. This proves the product is nonnegative throughout the entire w window, not merely near the selected interior centers.

The covariance is consequently comparable to

    (number of centers) times (shoulder width) times (amplitude squared)
          =T times N^-1/2 times T^-1=N^-1/2.

The same support counting gives each individual energy comparable to N^-1/2. This disproves a uniform T^-sigma correlation coefficient for distinct h for every fixed sigma>0.

For (5g,7g), common centers are 35gk and chi4(35)=-1; the same argument gives a globally nonpositive main-term product and covariance negative with magnitude comparable to N^-1/2. For (5g,6g), odd-quotient products cannot coincide, and distinct centers are separated by at least g. Their o(g) neighborhoods are disjoint, giving identically zero product. All statements use real radii and an admissible subsequence of real T. The fibers vanish exactly at their centers; the quadratic mass resides on the shoulders.

### d-Poisson decay, cell boundaries and bounded D

The frequency in the odd-d sine is f=Delta/(4h), with |f|<=1/4. Poisson on d=2j+1 has frequency lattice (1/2)Z. The zero alias is closest in the cell interior; at f=+/-1/4 it ties with one adjacent alias. For a smooth symbol with |b^(j)|<<A0D^-j, every alias satisfies

    |hat b(ell/2-f)|<<_B A0D(1+D|ell/2-f|)^(-B).

For D>=1, choose B>A+2 and sum all aliases. The at most two closest aliases contribute the asserted A0D(1+D|Delta|/h)^(-A); all others are bounded by the same quantity after summing a convergent tail. Fixed factors of four are absorbed in constants. For 1/2<=D<=1, or any bounded D range, the trivial sum bound O(A0D) proves the assertion because D|Delta|/h stays bounded. Thus the stated estimate is uniform at cell boundaries and at the small-factor endpoint.

When q changes to q+2, both chi4(q) and the odd-d sine reverse sign. Their product is unchanged, so the exact fibre has no artificial jump. Packet ownership may change at a boundary, but the pointwise regrouping remains exact and no boundary derivative estimate is used.

### Distinct-product count and discarded tails

For every assigned p, each h divides p and p is comparable to T^2. The divisor bound and A0D comparable to T^-1/2 therefore give

    |P_p(R)|<<T^(-1/2+epsilon)(1+|R^2-p|/W)^(-A).

This allows all divisors of p to reinforce; none is assumed to cancel. Because W is a positive power of T throughout the frozen band, summing beyond T^eta W gives

    O(T^(-1/2+epsilon) W T^(-(A-1)eta)),

which is O(T^-K) on choosing fixed A sufficiently large. For either sign of S, the packets having that sign sum to at least the absolute value of the net near-product sum. Bounding each by T^-1/2+epsilon proves the required count c V T^(1/2-epsilon).

The full F has only logarithmically many rectangles; the triangle inequality supplies a rectangle at height V divided by that logarithmic count. The summed stationary error is much smaller than V0. Hence the same necessary count holds for at least one rectangle with epsilon loss. At V0 it is T^(157/250-epsilon). At N=T^(2/3), the available natural-window capacity T^(2/3) is larger by exponent 29/750. This confirms that capacity alone neither excludes nor produces the event.

### Stationary errors and exact-fibre robustness

The report correctly uses the inherited total per-rectangle stationary error O(T^-1/2), yielding global M12 error O(T^-5+epsilon). No claim that this summed error is smaller than one main fibre is needed for its stated leading-fibre controls.

A stronger local check is available if the phrase actual contribution is read as requiring the exact Poisson h integral: the inherited remainder for one d,h is N^-3/4 M(R sqrt N)^-3/2. Summing over d for one fixed h gives

    O(T^-3/2 N^-1/2)=O(T^-11/6)

at the selected central scale. Its localized L2 norm over a radius interval of length O(T) is O(T^-4/3), while the leading G_h norm is comparable to T^-1/6. The change in pair covariance is therefore O(T^-3/2), much smaller than N^-1/2=T^-1/3. The positive and negative integrated controls survive replacement by exact h fibres. The disjoint-support control remains exact because the same tau supports are disjoint.

## 4. First unproved step and limitations

The reviewed report's first missing step is correctly stated: estimate the actual measure or integrated excess of radii at which the signed sum over at least T^(157/250-epsilon) distinct centers is large. The sign classification can obstruct a uniform pairwise power saving while still permitting aggregate cancellation between product differences, frequencies and rectangles.

In particular, these constructions do not estimate covariance after multiplication by the actual full-band exceptional-set indicator. Their individual amplitudes T^-1/2 are far below V0, and no constructed radius is shown to lie in that exceptional set. They cannot be substituted for either an upper or a lower bound on the full upper tail. No repair is needed because the reviewed artifact repeatedly preserves this scope.

## 5. Controls, outcomes and review verdict

- Actual amplitude and character: pass; the central support lies in phi=1 and Psi>0, while all chi4 signs remain actual.
- Coincident, detuned, positive, negative and disjoint cases: pass by the independent calculations above.
- Sharp real endpoints: pass; only O(1) centers are lost at each interior interval boundary, the global covariance sign is controlled, and dR=dx/(2sqrt(x)) is used.
- Unique q and d-Poisson boundary aliases: pass, with the two-alias boundary clarification recorded above.
- Bounded D and all smooth tails: pass; trivial bounded-D control and rapid Fourier decay cover the full stated range.
- Many-center count: pass as a necessary condition only, including rectangle recombination and error subtraction.
- Complete moment ledger: pass; low and boundary budget 32/25, unchanged first high-tail 10beta, second high-tail 1+20beta/13, exact L,H restoration and ceiling epsilon are retained. The report proves no complete gain.
- Independence and resource scope: the author's report was first read after my own discovery report was frozen. This review used analytic rederivation only, with no numerical experiment or external theorem import.

## 6. Dependencies and exact artifacts used

Primary reviewed artifact, hash verified during this review:

    rounds/codex-managed/gc-actual-upper-tail-a/reports/resonance_hostile_controls.md
    SHA256 89693f8519e735dbdd9582850e5465c85fef30835aeab50e398b16fe34f837e8

Original authorized context retained from discovery: protocol.md; state/proof_obligations.yml; state/active_campaign.yml; the campaign actual_interface.md; strategy/gauss_circle_upper_tail_strategy_2026-10-11.md; the complete square-root large-values kernel; and the three specified prior balanced-cancellation artifacts. Their hashes are recorded in the frozen discovery report. No new historical or external source was opened for this review.

The original discovery report was already frozen at SHA256 `ccd6592b215eecd1c38909fb088d40de2f0ea0b1916b1e568a58d54ba3c94e20`. It is not an independent proof source for the reviewed construction; the present calculations directly audit the reviewed statement. No sibling other than the explicitly assigned reviewed report was read.

## 7. Recommended state effect

Pass the reviewed arithmetic classification, localized covariance controls, smooth packet bound and many-center necessary condition as candidate evidence at their precise scopes. No mathematical correction of the frozen report is required. Retain the boundary-alias clarification and exceptional-set distinction in conductor synthesis. Recommend no promotion of target A, complete 32/25, a pointwise bound or any parent obligation. Freeze this review and stop; no shared-state edit, initial-report edit or successor.
