# Candidate: half-shifted alias defect and reciprocal-frequency local energy

Campaign: m9-m2-balanced-nonzero-alias-defect-gate

Status: conductor candidate for audit; no proof-state effect.

## 1. Proposed new information

The half-period shift from the actual character has a useful exact
stationary chart. With (h'=h+2s), (k'=k+q), and
(lambda=1/2-m>0), the interior stationary point and phase are

\[
 h'={X(k+q)\over\lambda^2},
\]

\[
 \Psi
 =R\sqrt{hk}-{X(k+q)\over2\lambda}-{\lambda h\over2}
 =-{h(\lambda-R\sqrt{k/h})^2\over2\lambda}
 -{Xq\over2\lambda}.
\tag{116.C1}
\]

At that point, both far gates have exact alias forms:

\[
 \rho={h(k+q)\over\lambda^2}
 \left(\lambda^2-{Xk\over h}\right),
\tag{116.C2}
\]

\[
 \Delta={hk\over\lambda^2}
 \left({X(k+q)^2\over hk}-\lambda^2\right).
\tag{116.C3}
\]

Thus determinant-far and radial-far delete critical-width neighborhoods of
two distinct dual centres. The (q)-dependence in (116.C1) is a reciprocal
linear phase with frequency (X/(2\lambda)). This is more precise than
the earlier statement that nonzero aliases merely survive.

## 2. Literal-legality problem

Classical smooth Poisson in (s) is not immediately lawful. The second gcd
mask is arithmetic, the far gates are sharp, the support has literal
crossings, and the zero-subtracted term contains a separate phase-free
piece. A literal derivation must first expand the gcd function over divisors,
split parity progressions, partition the two gate crossings, and retain all
endpoints and nonstationary integrals. The (s)-step then changes with the
divisor. Any formula that keeps the clean half-integer lattice but drops
these costs is only a model.

## 3. Capacity calculation

For one fixed (h,k,q), there are (asymp L^3) active aliases and each
stationary integral has size (L^{-1}). Modewise absolute values cost
(L^2), whereas the original (s)-sum has only (L) terms. Therefore
aliaswise ℓ1 loses a factor (L); applying the inverse B-process restores
the original capacity and nothing more.

Summing (q) first with the reciprocal phase suggests

\[
 \sum_{q\asymp L}w(q)e\!\left(-{Xq\over2\lambda}\right)
 \ll \min\!\left(L,{1\over\|X/(2\lambda)\|}\right)
\tag{116.C4}
\]

for a sufficiently regular amplitude. The resonant aliases satisfy the
near-product condition

\[
 |X-2j\lambda|\ll L^2,qquad j,\lambda\asymp L^3.
\tag{116.C5}
\]

Even an optimal divisor-type count for (116.C5) saves only the (q)-length
on average. That compensates the aliaswise Poisson loss; it does not yet
save the additional factor (L) required by the original target. A second
joint cancellation in (lambda,h,k) is mandatory.

## 4. Explicit inequality gate

The first positive candidate is the literal row local energy

\[
 \mathfrak L_B
 =\sum_{h,k}|T_{h,k}|^2,
\]

with (T_{h,k}) defined in (116.D9). The exact Cauchy implication is

\[
 \mathfrak L_B\ll_\varepsilon L^4X^\varepsilon
 \Longrightarrow
 E_{B,\mathrm{df}}\ll_\varepsilon L^3X^\varepsilon.
\tag{116.C6}
\]

This is an actual inequality, not an analogy. Its diagonal is target-sized.
However, it removes the outer character and can be stronger than the scalar
target. It passes the Round-116 gate only if the transformed alias geometry
controls its complete off-diagonal without proving an arbitrary-coefficient
false analogue.

The less positive but exact alternative is to keep the scalar alias family
fully signed. After a lawful stationary decomposition with amplitude
(L^{-1}), the needed unscaled joint bound has schematic size

\[
 \left|\sum_{h,k,q,\lambda}
 \Omega_B(h,k,q,\lambda)e(\Psi(h,k,q;\lambda))\right|
 \ll_\varepsilon L^4X^\varepsilon,
\tag{116.C7}
\]

where (Omega_B) must contain the divisor expansions, gate images,
stationary Jacobian, crossings, and all signs. Its raw unscaled capacity is
(L^6); ordinary B-process inversion accounts for one factor (L), and a
new noninvertible estimate must account for the second.

## 5. Falsification targets

The hostile audit should test:

1. whether (116.C6) is equivalent to an already-rejected stronger Gram;
2. whether its off-diagonal contains a coherent (L^5) or (L^6) actual
   sector even though the diagonal is (L^4);
3. whether a large-sieve Cauchy step has a diagonal above the required norm;
4. whether (116.C4)--(116.C5) merely invert the (s\leftrightarrow\lambda)
   transform;
5. whether the two alias centres in (116.C2)--(116.C3) create a genuinely
   smaller subrange when separated; and
6. whether any imported theorem is uniform for real (X), half-integer
   aliases, (L^3)-length dual range, (L^2)-width deletions, and the
   literal coefficient.

## 6. Promotion threshold

Promote only an exact alias chart whose literal errors are target-safe, an
actual estimate for (116.C6) or (116.C7), a strict target-safe subrange, or
a scoped no-go theorem for a precisely defined alias/large-sieve class.
The identities (116.C1)--(116.C5) alone do not estimate the balanced block.
