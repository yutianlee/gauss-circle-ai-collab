# Round215 conductor review of the isolated spatial-kernel report

## 1. Result

GREEN for the exact identities, eventual spatial nonvanishing, the two
specified positive-certificate limitations, and the clarified interval
trace. Campaign:gc-complete-localized-wave-moment. Date:2026-09-28.
Role:conductor review, NONBLIND. Authoritative graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
Reviewed report:reports/blind_spatial_kernel.md, final SHA256:
f02eee61b7b829ae87b0b62c018bf8dd395157f324895bdf514d745e1d2ac44e.
This review adds no arithmetic hypothesis to the isolated packet.

## 2. Exact statement and hypotheses reviewed

The coefficients are nonnegative, supported on sqrt(N)<=|m|<=2sqrt(N),
with total mass comparable to N^(1/4). The coefficient cap is not used
in the lower proofs. The cutoffs, every center and both positive
certificates are explicitly defined in the report. Its identities allow
1<=N<=T^2; the spatial lower bounds require N sufficiently large for
the fixed cutoffs. The target-power comparison uses fixed interior
166/325<alpha<242/325, N=T^alpha. The trace on the whole interval uses
the separately recorded lower bound for eta on [-1,1].

The verdict is C<=U2<=U1, U1>=cTN^2 and U2>=cN^(5/2), with no
converse lower bound for C. The packet has no actual r2 binding;
that is supplied separately by the conductor ledger and its reviewer.

## 3. Independent checks of the derivation

With the report's minus-sign Fourier convention, expanding the finite
tenth power gives K_N(-k/sqrt(N)) and N H(-sqrt(N)rho). The common
phase e(aT rho) and D_J(sqrt(N)rho) reproduce every window. The change
to physical R instead gives du=sqrt(N)dR, with the exact full-tail
weight Theta=sum_j |eta((R-R_j)/sqrt(N))|^10. These two formulas agree.

The gamma-integral Fourier formula has the required two-dimensional
factor pi/t and exponent -pi^2|xi|^2/t. Its transform is strictly
positive on the entire frequency plane. Dominated L1 convergence of
W phi(y/N)^10 to W gives uniform Fourier convergence; hence Re K_N
is eventually bounded below on the compact disk of radius20. Each
tuple difference lies in that disk. This proves precisely the needed
eventual statement, not a finite-N sign theorem for arbitrary phi.

The report's finite-N control also checks out under its explicitly
weaker central-neighborhood hypotheses. Near the two translated
Schwartz bumps, the cosine tends to -1 and the weight has order
(N_*L)^(-200); rapid decay makes the remaining terms smaller. The
transform for g+t psi_L is a real polynomial with positive constant
and negative leading coefficient. A zero therefore exists for some
t>0 while phi(0)=1. This refutes a blanket compact-domain positivity
assertion only; it is not asserted to hit an actual discrete difference
or to satisfy the later specified larger central cube.

For U1, radial bins of width c/sqrt(N) number O(N). The tuple total
mass is S^5, so the same-bin pair mass is at least S^10/O(N), of
order N^(3/2). Multiplication by N(J+1) gives TN^2. For U2, bins of
width c/T number O(Tsqrt(N)), with pair mass N^2/T; all center
arguments are in one short arc, so |D_J|>=c(J+1), giving N^(5/2).
Both arguments retain nonnegative summands only in their named positive
certificates. The original complex expansion cannot be restricted in
that fashion as a lower bound.

The reproducing kernel has fixed spatial Fourier bandwidth. Weighted
Holder is valid because its Schwartz decay dominates the fixed
polynomial dual weight. It gives |F(0,R)|^10<=C B_N(R). The nearest
center is within sqrt(N)/2, including both partial endpoints, so the
clarified eta bound proves Theta>=c on the physical interval. The
trace restores precisely N^(-1/2), without a spatial volume factor.

## 4. First doubtful or unproved step

No correction is required for the reviewed statements. Their signed
arithmetic target remains unproved. The positive-certificate scale
N^(5/2) is not a lower bound for C, and an abstract two-term cancellation
example in the report is identified only as a logical control, not as
an admissible coefficient array. Actual circle consequences require
the independent arithmetic binding and then a new signed upper bound.

## 5. Controls and outcomes

- Fourier normalization and both changes of variables: GREEN.
- Whole spatial and radius tails, finite expansion and Fubini: GREEN.
- Full support, mass and two different bin widths: GREEN.
- Eventual versus finite-N positivity and the counterexample's scope: GREEN.
- Fixed-interior exponent gap: (5/2)alpha-83/65>0; no uniform gap
  when alpha approaches166/325 withT. GREEN.
- Clarified cutoff coverage, real endpoints and ceiling: GREEN.
- Certificate versus signed moment and generic versus actual coefficients: GREEN.
- Original statement-only isolation was maintained; this review and
  the agent's later conductor-ledger seam are explicitly NONBLIND.

All checks are analytical. No numerical experiment or fresh external
source is used in this review.

## 6. Dependencies and exact artifacts

Read protocol.md, the final isolated report at the hash above, its
briefs/blind_spatial_kernel_statement.md, and
controls/cutoff_normalization_clarification.md. The conductor's separately
derived kernel ledger was already available to the conductor and is
not presented as a blinded source. The original report's isolation
declaration and its final bytes are preserved. No sibling's result is
needed to establish the generic packet conclusions.

## 7. Recommended state effect

Retain the reviewed identities and scoped certificate controls as round
evidence. No new graph node, moment, exponent or full-goal parent is
promoted. The interval trace remains a sufficient implication only;
its hypothesis C215 and the quarter theorem stay open.
