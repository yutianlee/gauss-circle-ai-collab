# Round 213 conductor review of the isolated certificate report

## 1. Result

GREEN for the isolated report's two-sided certificate theorem, exact
discretization, radius-norm identification and explicit signed control.
No repair is required. This is a conductor review after the original
statement-only report finished, not a new blind derivation.
Campaign: gc-complete-centered-arithmetic. Date: 2026-09-28.
Graph SHA256: 4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
Final claimant SHA256:
a16db0ca6ec19bace974febee7df1ed252b766772574a8469edf75dacfcc1e1a.

## 2. Exact statement reviewed

Under the packet's assumed mass and residue-zero hypotheses,
P has size N/sqrt(LK/U) up to epsilon powers, uniformly over its permitted
constant nonnegative centers. The certificate reaches the target on the
lower subband but fails for fixed alpha>204/325. It bounds the average
of weighted radius L2 norms and, by Minkowski, the weighted L2 norm of
the shift-average absolute value. It does not bound a supremum for free.

The exact error E-C is rho times the smooth sum-minus-integral. The
report proves a uniform error smaller than every prescribed negative
power after sufficiently many integrations by parts. It does not assert
the supplied absolute mass for an actual arithmetic system.

## 3. Independent checks

The mask absolute value is absolutely continuous with total variation
at most integral |W'|=O(1), even with infinitely many sign changes.
Residue sums therefore differ by O(1). If Q is total mask mass, q is
its residue-three mass and p=Q-q, then q=Q/4+O(1), p=3Q/4+O(1).
The exact inequality H>=rho q+|M-rho p| is valid because the coefficients
vanish on that residue. Minimizing over rho>=0 gives H>=(q/p)M.
This confirms the report's asymptotically sharp constant 1/3 at this
interface; the conductor's separately derived cruder constant also suffices.

The exact double derivative of the square root gives positive frequency
derivative comparable to Lambda/N. Bins of diameter cN/Lambda have
kernel modulus bounded below, so G>=cH^2/Lambda. Averaging uses the
assumed complete mass and Lambda<=LK/U. Conversely, Schwartz decay
and the same derivative lower bound sum to O(N/Lambda) per integer
row; the diagonal is covered because N/Lambda tends to infinity.
The sums h^(-1/2) and k^(-1/2) yield the matching complete upper cost.
Both computations give alpha-1/2+3b; its excess over 4b is
alpha-1/2-b. Fixed interior qualifications and epsilon choices are correct.

For the strong Poisson correction, scale t=Nx. Every nonzero integer
mode has phase derivative of magnitude at least |m|N/2, since
Lambda/N=O(T^-18/65). Higher derivatives are O_j(Lambda), hence
O_j(|m|N). Every fixed derivative of the reciprocal first derivative
is O_j((|m|N)^-1). Iterated integration by parts therefore costs
N^(1-J)|m|^-J, with no endpoint terms. Its summable mode bound proves
the asserted uniform superpolynomial error and its exact positive sign.

The radius measure has mass one, so its exact double sum contains no
extra T. Absolute kernel and coefficient values give an upper bound;
Minkowski and probability-measure Cauchy give the stated mixed norms.
The result has no reversed inequality and no hidden endpoint weight
assumption.

Finally the periodic control has coefficients 1 off residue three,
zero on it, and rho=3/4. The displayed Fourier expansion has precisely
the three nonzero quarter frequencies. Their distances from the integers
are at least 1/4. Nonstationary Poisson estimates therefore make both
signed sums tiny, while a positive fraction of the full shift rectangle
supplies the assumed absolute mass. This is a valid abstract control,
expressly not an r2 counterexample. Sign-changing masks do not affect it.

## 4. First unproved step

No defect was found relative to the packet. Application to actual r2
still needs the actual mass and mask hypotheses from independent
arithmetic evidence. No signed remainder estimate follows from the
certificate calculation. The periodic example rules out that inference.

## 5. Controls

GREEN: exact ceilings at fixed interior scales; residue mass; sign-changing
masks; lattice diagonal; support and smooth endpoints; every nonzero
Poisson mode; normalized radius measure; complete shift sum; sharp
threshold; certificate/signed distinction; explicit countermodel.
No numerical experiment or source import. The full goal is unchanged.

## 6. Dependencies and access

Reviewed protocol.md, the isolated packet
briefs/blind_centered_certificate_statement.md, and the final claimant
reports/blind_centered_certificate.md in this campaign. The claimant's
original access was limited to protocol and packet, as assigned in the
frozen brief and confirmed in its report. Later independent NONBLIND work
does not retroactively add context or blind credit to that completed report.
The conductor has broader task context and therefore claims no isolation.

## 7. State effect and binding

Retain the isolated theorem and analytical controls as reviewed scoped
evidence. No promotion of arithmetic cancellation, moments, pointwise
exponents or M1/M2 parents. GREEN binds to claimant SHA256
a16db0ca6ec19bace974febee7df1ed252b766772574a8469edf75dacfcc1e1a.
A material change requires renewed review.
