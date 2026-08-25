# Round 163 barrier packet: near-square divisor involution gate

- Campaign: `m9-m2-hard-top-t1-near-square-divisor-involution-gate`
- Starting graph:
  `700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358`
- Evidence status: frozen barriers and controls, not a proof

## Accepted input

The literal $t=1$ scalar has the exact squarefree product form in the
Round-163 strategy. Round 161 removes only fixed-constant long channels
and exact collisions. Round 162 proves exact character-Poisson
involution, rank-one product-collar capacity, and local-divisor return;
it leaves the complete signed physical coefficient and every hard edge
open.

## Forbidden restarts

1. Do not open squarefree/coprime conditions termwise and repeat the
   positive Round-162 collar ledger.
2. Do not complete the moving divisor interval to $r_2/4$ without an
   estimate for the complement.
3. Do not use full-divisor vanishing as vanishing of the upper near-square
   coefficient.
4. Do not claim a $p\equiv3\pmod4$ toggle cancels physical terms until
   both members are proved to remain in the literal cone with their
   profiles and parity.
5. Do not suppress the even-$N$ branch or treat its even complement as a
   character-supported physical divisor.
6. Do not infer polynomial sparsity from the sum-of-two-squares condition
   without an exact weighted count at the required scale.
7. Do not treat a constant-weight or phase-aligned diagnostic as a
   physical lower bound.
8. Do not restart a bare character transform, standard positive
   differencing, coefficient-uniform Bessel placement, or any named
   Round-162 source placement.
9. Do not transfer a $t=1$ statement to the other few-point channels,
   hard TOP, M9--M2, M9, the bridge, or either global exponent.

## Mandatory hostile tests

- single-prime toggle on the exact interval $[\sqrt N,2\sqrt N]$;
- two-prime exchanges with congruence classes and ratio constraints;
- complementary divisor on odd products, and both the even physical
  complement $N/d$ and odd-part complement $N/(2d)$ when $N=2M$;
- semiprime and multi-prime squarefree configurations;
- literal profile asymmetry and all half-open endpoints;
- arbitrary-real centre and phase preservation when $N$ is fixed;
- restored count or norm against the missing $L^{1/2-o(1)}$.

## Exit rule

Close only under `hard_top_t1_near_square_divisor_target`,
`strict_t1_prime_toggle_sector`, or
`hard_top_t1_divisor_involution_leakage_no_go`.
