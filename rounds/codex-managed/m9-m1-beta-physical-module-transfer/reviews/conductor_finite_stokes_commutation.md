# Conductor finite Stokes commutation audit

Campaign: `m9-m1-beta-physical-module-transfer`  
Role: conductor independent seam analysis  
Allocation: 100% analytical/algebraic

The unmasked endpoint Cauchy collapse moves the radial \(w\)-rectangle,
while the two-axis transfer moves the outside \(u,v\)-rectangles. At fixed
finite \(U,V,S\), both are boundary operators on a product of rectangles.
If the integrand is meromorphic with normal-crossing divisors and common
small-tube regularization, the full product Stokes identity is independent
of the order in which the three coordinate rectangles are processed.

However, “full” is essential. Moving \(u,v\) first generates their
horizontals, axes, connectors, and corners on the radial terminal and sides.
Moving \(w\) first generates the endpoint right-line prefix, artificial and
arithmetic residues, and its radial sides on every outside face. Equality
requires all codimension-two and codimension-three intersections. In the
masked three-branch sum, the nonholomorphic connector coefficients cancel
by \(\sum\Theta_r=1\), leaving the ordinary unmasked product-boundary
identity.

This suggests a lawful order avoiding any new physical-limit interchange:

1. keep all variables finite and sum the full hierarchical partition;
2. use product Stokes to reorder the outside transfer and unmasked endpoint
   collapse;
3. recombine artificial and arithmetic residues at finite height;
4. remove the renormalized radial side (Round 21 / Round 35);
5. take the already accepted physical endpoint and \(R_1\) arithmetic
   limits.

The possible obstruction is not mask differentiation but an omitted
ordinary outside-axis image of the right-line prefix \(D_\xi\) or
\(R^{\rm ar}[R_1]\). The accepted physical endpoint and arithmetic lemmas
bound the unshifted physical sums; they do not explicitly state what a
later \(u,v\) transfer of those physical sums means. The proposed order
must show that no later transfer is needed: all outside-axis operations are
completed at finite height and, after global recombination, their total
endpoint/arithmetic contribution is exactly the same unmasked \(D_\xi\)
and \(R^{\rm ar}[R_1]\) already estimated, rather than their transfer.

This is the central Round-36 identity to prove or falsify. If an ordinary
axis/horizontal image survives after finite product Stokes, then the
existing physical bounds do not control it and the commutator stays open.
