# Conductor candidate: exhaustive tangent-height partition

Campaign: `m9-m1-beta-actual-profile-cauchy-tail`  
Role: conductor strategy derivation  
Allocation: 100% analytical/algebraic

Let \(\alpha=\beta+\mu+\nu\), with beta confined to a fixed compact set.
Fix a smooth cutoff \(\vartheta\) equal to one near zero. Before any
absolute value, partition the endpoint-free top density by

\[
1=\vartheta(\alpha)
 +(1-\vartheta(\alpha))\vartheta(\rho)
 +(1-\vartheta(\alpha))(1-\vartheta(\rho)).
\tag{38.C8}
\]

This is only a proposed analytic partition; it introduces no contour move
and hence no residue.

## Bounded alpha

Here \(\mu=-\nu+O(1)\). Every smooth interior spatial transform and the
regular top transform decay rapidly in \(|\nu|\). For the hard top,

\[
\frac1{0^++i\mu}=O(|\nu|^{-1})
\]

away from a bounded set; the PV singularity is not approached. Together
with fixed-\(b\) cubic decay of \(\widehat\phi(b+i\nu)\), this region should
be absolutely integrable after the finite coefficient sums. The required
check is uniformity of the remaining bounded-alpha gamma/radial factor and
the actual sums.

## Large alpha, artificial seam

If \(|\alpha|\gg1\) and \(|\rho|=O(1)\), then

\[
\nu=-\alpha-\beta+O(1),\qquad \mu=2\alpha+O(1).
\]

Thus the height transform is \(O_b(|\alpha|^{-3})\) and the hard top is
\(O(|\alpha|^{-1})\). The common omega-\(G/E_1/R_1\) germ is regular, so
the raw transition gamma growth is offset by at least four inverse powers.
The exact remaining exponent depends on \(c',a,b\), but for the allowed
range \(c'<3/2\) the resulting alpha tail is integrable once the common
germ is shown order zero after its listed phase extraction.

## Large alpha, separated rho

This is the genuine two-saddle sector. The full top-R1 convolution—not its
factors separately—has the accepted local regular kernel

\[
K_{R_1}(L,\nu)
=-\frac{i f_b(L)}{2A\{A+i(L-\nu)/2\}}
 +\frac{f_b(\nu)-f_b(L)}
 {(L-\nu)\{A+i(L-\nu)/2\}},
\tag{38.C9}
\]

with \(|K_{R_1}|\ll_b\lambda^{-2}w_b(\nu)\) and
\(|\partial_LK_{R_1}|\ll_b\lambda^{-3}w_b(\nu)\) on separated saddle
patches. The moving-face logarithm has an even smaller local coefficient.
What remains is to prove that the complete gamma, radial, scale, and
coefficient multipliers are uniform order-zero symbols across saddle
entry/exit and that their \(h,q,j,x\) sum preserves an integrable
\(\nu\)-majorant.

The first two cells appear amenable to direct absolute estimates. The
third cell is the only plausible source of a genuinely new signed tail
theorem. A Round-38 proof should therefore avoid re-solving the complete
sixteen-stratum geometry and focus on globalizing (38.C9) through the
two-saddle partition and actual sums. If this globalization fails, the
first failing multiplier and its exact power should become the next graph
obligation.

No numerical experiment or external theorem was used.
