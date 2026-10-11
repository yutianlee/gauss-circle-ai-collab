# Round 201 synthesis

Campaign: `gc-whole-discrepancy-twelfth-moment`; 2026-09-23.
Frozen objective: a complete twelfth-moment bound
integral_(Y/2)^(3Y)|P(x)|^12 dx << Y^(4+eta+epsilon),
eta<13theta_LY-4. Budget: three analytical/source tasks and one bounded
repair/review cycle; no numerical experimentation. Starting graph hash:
`2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`.

## Decision

Terminal label: `whole_discrepancy_moment_reduction_open_offdiagonal`.
The round establishes the complete fixed-window moment interface and
one independently proved exact-resonance kernel. The complete
twelfth-moment target remains open. The State Patch adds only
`GC-weighted-square-root-exact-resonance-mass` as `proved_internal`.
It leaves all existing graph records and all exponents unchanged.

## Complete source and the first unproved inequality

With T=sqrt(Y), fixed delta=T^(-1/2), and fixed radial mollifier rho,
let Psi be its Fourier transform on a radial axis and put
a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T)). Then uniformly on fixed R~T windows,

\[
 P(R^2)=\frac{\sqrt R}{\pi}H_T(R)+O(T^{1/2+\epsilon}),\qquad
 H_T(R)=\sum_{n\ge1}a_n(T)\cos(2\pi R\sqrt n-3\pi/4).
\]

The annulus estimate includes every sharp boundary jump. The summed
Bessel remainder is O(T^(-1/2)), and the coefficients are fixed as R
varies. Every moment expansion tail is controlled with a cutoff
T^(1+alpha), alpha>0 fixed; no tail is silently cut at n=T.
For a fixed nonnegative smooth w, supported away from zero and equal
to one on [1/sqrt(2),sqrt(3)], the all-sign expansion is

\[
 M_{12}(T)=\frac{T}{2^{12}}\sum_{\epsilon\in\{-1,1\}^{12}}
 e\!\left(-\frac38\sum_j\epsilon_j\right)
 \sum_{\mathbf n}\left(\prod_j a_{n_j}(T)\right)
 \widehat w(-T\Delta),\quad \Delta=\sum_j\epsilon_j\sqrt{n_j}.
\]

Write M_12=D_12+O_12 by Delta=0 versus Delta!=0, retaining every phase.
The promoted kernel gives 0<=D_12<<T. The missing statement is exactly

\[
 O_{12}(T)\le C_{\eta,\epsilon,\rho,w}T^{1+2\eta+\epsilon},
 \qquad 0\le\eta<13\theta_{LY}-4.
\]

Since M_12>=0, the negative part of O_12 is already O(T); one outside
absolute value gives an equivalent target at these exponents. A sum
of moduli of individual terms would be a stronger, unproved estimate.
The Jacobian and leading amplitude give T^7 M_12, with entire smoothing
error T^(8+epsilon). Inclusive persistence then gives pointwise exponent
(4+eta)/13. Even the ideal eta=0 would not by itself prove one quarter.

## The accepted subordinate kernel

For b_n>=0 let A_d=sum_s b_(ds^2) for squarefree d and S=sum_d A_d^2.
For fixed k>=2 the full exact-resonance mass is at most
2^k B_k S^(k/2), where B_k counts partitions without singleton blocks.
For b_n<=C tau(n)n^(-3/4), S<=C^2 zeta(3/2)^10. This includes unequal
supports, nonpairing relations, all signs, infinite limits, and uniform
exact-resonance tails. Its proof uses radical independence and a
no-singleton partition bound, not a pairing or probabilistic shortcut.
The actual coefficients have C=4. Real even constant coefficients are
nonnegative as torus integrals, although individual exact terms need
not be positive.

Formal kernel: `proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md`.
This is a rigorously isolated useful component, not a new high-moment
theorem or claim of novelty. Near-resonance control remains entirely
separate. The physical family
sqrt(m^2+1)+sqrt(m^2+49)-2sqrt(m^2+25)=-144m^(-3)+O(m^(-5))
shows why exact radical independence does not provide the missing
finite-window separation.

## Audited benchmark and remaining power gap

The best fixed-order circle absolute range verified in this bounded
corpus is q<=262/27. The published source is Tsang--Zhai (2012),
Section 1.1, equation (1.5) and following sentence, with
R_I(t)=P(t/(4pi^2)):
https://hub.hku.hk/bitstream/10722/156281/1/Content.pdf .
This printed external benchmark is source-reviewed campaign evidence;
it is not promoted as a new graph theorem in this patch.

Together with the accepted theta_LY it yields only

\[
 \eta_0=\frac{62}{27}(\theta_{LY}-1/4)
 =0.148072478162659\ldots,
\]

where strict improvement requires eta<0.088281287662798... . The gap is
(185-578theta_LY)/54=0.059791190499861... in the Y exponent, or twice
that in the T exponent. Strict improvement requires more than this
saving. The source auditor's bound improves the analytic report's
second-moment-only baseline; it still gives no new pointwise exponent.
Signed odd asymptotics, divisor moments, translation averages, and
conjectural higher moments were not transferred into this task.

## Evidence, interventions, and validation

The three seven-section reports are under `reports/`. The blind
derivation used the statement packet and protocol only. The analytic
derivation independently included the full exact part. The conductor
independently derived its weighted partition estimate and persistence
bridge, then audited all seams in
`reviews/conductor_round201_reconciliation.md`. A separate post-report
review audits the formal kernel in
`reviews/independent_resonance_kernel_review.md`.

One formatting repair replaced two malformed squarefree labels in the
blind report; no mathematical repair was necessary. Controls are
analytic/algebraic, with zero numerical experiments. Green review gates
certify the stated identities and isolated kernel, not the open
offdiagonal estimate. Exact patch validation, restoration/replay,
artifact hygiene, protected records, and graph checks are recorded in
`controls/closure_validation.json`.

## Next boundary

Round 202 must perform the scheduled strategy and current-primary-
literature checkpoint after Rounds 199--201. Use the complete-source
Round-200 correlation and the exact whole-moment interface here to
compare routes. Do not count further exact-diagonal bookkeeping or
P2 mechanism exclusions as a new analytic saving. Any next analytic
campaign must name a complete signed estimate and price every tail,
mask, coefficient norm, and reconstruction exponent before delegation.
