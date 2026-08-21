# Conductor review: parity high-pass, orientation, and one-count jumps

Campaign: m9-m2-adjacent-ray-transport-commutator

Starting graph SHA-256:
c93f14d6790341b792b54bbaa7ccb96c211741d666729f08addc80fb91d1b759

## Exact finite high-pass

For every finitely supported, zero-extended sequence \(f\), put
\(\epsilon_q=(-1)^q\) and \(d^+f(q)=f(q)-f(q+1)\). Then

\[
 \sum_q\epsilon_q f(q)
 =\sum_r\{f(2r)-f(2r+1)\}
 ={1\over2}\sum_q\epsilon_qd^+f(q).
\tag{111.C1}
\]

Thus, for the literal Round-75 row,

\[
 \mathcal K_L^+
 :=\sum_{a,q}(-1)^q
       \{F_{L,a}(q)-F_{L,a}(q+1)\}
 =2\mathfrak C_L^{\mathrm{off}}.
\tag{111.C2}
\]

This uses one ordered orientation \(a<b\) and the one outer \(2\Re\)
already present in the energy identity. The backward difference gives the
same scalar and is not a second contribution.

For a cutoff \(Q\), the exact terminal correction is

\[
 \sum_{q\le Q}(-1)^qd^+f(q)
 =2\sum_{q\le Q}(-1)^qf(q)
   +(-1)^{Q+1}f(Q+1).
\tag{111.C3}
\]

If the first and last nonzero indices are \(u,v\), zero extension gives

\[
 d^+f(u-1)=-f(u),\qquad d^+f(v)=f(v).
\tag{111.C4}
\]

No maximal theorem follows without these endpoint atoms.

## Norm scope

Equation (111.C2) is an exact signed reformulation. The target is

\[
 |\Re\mathcal K_L^+|\ll_\varepsilon L^2X^\varepsilon.
\tag{111.C5}
\]

Complex modulus, total variation, maximal partial sums, row energy,
operator norm, and an undirected Gram are stronger surrogates unless an
explicit directional and dimensional bridge is proved. The blind
singleton, truncated-endpoint, alternating-row, large-variation with zero
survivor, and coherent-row controls show that none of the reverse
implications is available for arbitrary finite coefficients. They are norm
falsifiers, not models of the actual Vaaler coefficient.

## Exact jump ownership

Let \(M_{j,q}\in\{0,1\}\) be the literal masks, ordered by first failure:
zero extension, primitivity, odd lift and height cell, hard support and
ceiling, reciprocal support and equality convention, collars, entry/exit
and half-open scale data, then terminal, puncture, and metric data. Split
nonbinary weights into finite tagged atoms first. With

\[
 P=\prod_jM_{j,q},\qquad Q=\prod_j(M_{j,q+1}\circ T_q),
\]

one has

\[
 PU-QV=PQ(U-V)+P(1-Q)U-Q(1-P)V,
\tag{111.C6}
\]

and

\[
 1-\prod_jM_j
 =\sum_j(1-M_j)\prod_{i<j}M_i.
\tag{111.C7}
\]

Equations (111.C6)--(111.C7), followed by ordinary telescoping for the
remaining scalar factors, assign every birth and death once. They prevent
double ownership when arithmetic and support jumps coincide. They do not
estimate any packet.

For odd \(a\),

\[
 1_{(a,a+2q)=1}=1_{(a,q)=1}
 =\sum_{d\mid a}\mu(d)1_{d\mid q}.
\tag{111.C8}
\]

Every \(d\mid a\) is odd, so parity is preserved on \(q=du\), but the
adjacent mask has recurring interior jumps. The raw lower ceiling changes
exactly by

\[
 \left\lceil{g(a+2q+2)\over4}\right\rceil
 -\left\lceil{g(a+2q)\over4}\right\rceil
 ={g-\chi_4(g(a+2q))\over2}.
\tag{111.C9}
\]

The accepted lower profile has \(W(1)=1\), so this atom is not killed.

## Decision

Certify (111.C1)--(111.C9) as finite algebra and ownership interfaces.
They do not prove (111.C5), a variation or Gram bound, a hard-cone
estimate, either smooth M2 packet, M9-M2, M9-M1, endpoint uniformity, M9,
or an exponent.

