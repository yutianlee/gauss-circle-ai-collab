# Round 184 statement-only hard-M1 t=1 problem

This packet is self-contained. Do not use a proof graph, strategy file,
prior round, sibling report, source, or conductor analysis.

Put e(z)=exp(2 pi i z). Let L>=2, X>0, and
sigma in {+1,-1}. Let A_(L,X)^sigma(u,v) be one fixed literal coefficient,
not an arbitrary sequence. It is zero outside

\[
 u\asymp L,\qquad v\ {\rm odd},\qquad 4u<v<16u.
\tag{B184.1}
\]

It retains fixed dyadic and ratio profiles, a Vaaler taper, normalized
powers, floors, stars and half weights, strict support edges, a hard
sample, real-parameter crossings, endpoint point values, and zero
extension. Uniformly in the block:

1. its normalized size is O(\mathcal X), where \mathcal X is an allowed
   subpolynomial loss;
2. on each common smooth cell, multiplying u by exp(theta) and v by
   exp(-theta), with |theta|<=kappa L^(-1/2), changes the coefficient by
   O_kappa(L^(-1/2)\mathcal X); and
3. the points where this displacement crosses any one of the finitely many
   cone, shell, profile, floor, star, hard-sample, endpoint, or
   zero-extension faces lie in a finite union of width
   O_kappa(L^(1/2)+1) strips containing
   O_kappa(L^(3/2)\mathcal X) integer pairs in total.

The task must treat these as hypotheses of the isolated finite problem and
must say which conclusions would fail without them. Define the complete
t=1 scalar

\[
 \mathcal T_{L,X,\sigma}
 =
 \sum_{\substack{u,v\geq1,\ (u,v)=1,\ v\ {\rm odd}\\
                  4u<v<16u,\ uv\ {\rm squarefree}}}
 \chi_4(v)A_{L,X}^{\sigma}(u,v)e(\sigma\sqrt{Xuv}).
\tag{B184.2}
\]

There is one absolute value only after the complete sum. The proposed
target is

\[
 \boxed{
 |\mathcal T_{L,X,\sigma}|
 \ll L^{3/2}\mathcal X.}
\tag{B184.3}
\]

Support gives uv asymp L^2. The coefficient-insensitive capacity is L^2
\mathcal X, so support and boundedness alone miss L^(1/2).

Fix kappa>0. For each supported squarefree N=uv, choose canonically at
most one unordered pair of distinct odd prime factors p,q satisfying

\[
 \chi_4(pq)=-1,\qquad
 |\log(q/p)|\leq\kappa L^{-1/2}.
\tag{B184.4}
\]

The selector depends only on N,L,kappa and not on the allocation N=uv.
Let the XOR sector contain allocations where exactly one of p,q divides
v. Exchange p and q between the two factors:

\[
 (u,v)\longmapsto
 \begin{cases}
  (up/q,vq/p),&q\mid u,\ p\mid v,\\
  (uq/p,vp/q),&p\mid u,\ q\mid v.
 \end{cases}
\tag{B184.5}
\]

Independently do all of the following.

1. Verify the exact capacity of (B184.2), including prime, semiprime,
   all-primes-1-mod-4, dechirped, character-erased, one-site, and endpoint
   controls without treating them as lower bounds for the fixed literal
   coefficient.
2. Prove or refute that (B184.5) is an integral, multiplicity-one,
   fixed-point-free involution on the complete ambient XOR set and that it
   preserves product, phase, squarefreeness, coprimality, parity, and the
   selector while reversing chi_4(v).
3. Derive the exact zero-extended paired-difference identity and use the
   three stated regularity hypotheses to decide whether the full canonical
   XOR incidence sector is O_kappa(L^(3/2)\mathcal X).
4. State the exact complement: every product with no selected pair plus
   the neither/both allocations when a pair is selected. Do not infer pair
   density, positive proportion, or per-block nonemptiness.
5. Test one-prime toggles, complementation, averaging over involutions,
   exchange-graph matching, ordered-divisor Abel transport, and a sliding
   Fejer short-shift energy. Retain one outer real part and do not take
   absolute values over shifts before a signed estimate.
6. Give either a proof of (B184.3), a strict target-safe signed sector with
   its exact complement, or the narrowest exact mechanism no-go and the
   first additional relation still needed.

A strict exchange sector is not the complete t=1 theorem. A complete t=1
theorem is not the full small-t theorem. Do not infer any statement for
t>=2, a near-resonant component, a parent estimate, a bridge, a global
theorem, or an exponent.

Computation, if any, is diagnostic only.

Return exactly:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect.
