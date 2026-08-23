# Round 123 synthesis: integer-centred shifted near-alias reduction

Campaign: m9-m2-unbalanced-reciprocal-gram-factorization-gate

Starting graph SHA-256:
d29ae6c0f398cc2df699b15ee2901b525290263b6cde5eecece49cdeee095bb1

## Frozen objective

The round tested the exact flat-smooth strict-UNBAL row

\[
 \mathscr R_X=
 \sum_{r\ {\rm odd}}\chi_4(r)W(X/(rD))
 \sum_k{q_L(4Xk/r^2)\over k}e(Xk/r),
\]

where \(D=X^\delta\), \(L=X^\ell\), \(R=X/D\), and
\(K=XL/D^2\). The required scalar estimate is
\(\mathscr R_X\ll X^{1/4+\varepsilon}\). Round 118 supplied only the
strictly larger one-dimensional envelope, so this round retained the
joint \(r,k\) dependence.

## Centre stability

The real phase may be moved to any integer \(M\asymp X\) at the exact
cost

\[
 |\mathscr R_X-\mathscr R_M^\sharp|
 \ll_\varepsilon(1+|M-X|)X^\varepsilon,
\tag{123.S1}
\]

with all amplitudes and the denominator \(4X\) frozen at the original
real \(X\). The proof is physical: the derivative of the product kernel
costs \(L/D\), and a uniform divisor layer cake has effective length
\(D/L\). It includes the zero-product and rapid-tail branches.

Thus floor integerization costs \(X^\varepsilon\). An odd multiple of a
power \(2^t\asymp X^{1/4}\) can also be chosen within target distance,
but its large two-adic order does not thin the live near-defect pairs.

## Exact Gram and factor algebra

The ordinary weighted \(k\)-Cauchy Gram is only a sufficient norm. Its
nondegenerate diagonal is \(R=X/D>X^{1/2}\), so it is strictly stronger
than the scalar target.

For the unique nearest alias \(j\), set

\[
 E=M(s-r)-jrs,\qquad u=M-jr,\qquad v=M+js.
\]

Then

\[
 uv-M^2=jE,\qquad
 \chi_4(r)\chi_4(s)=(-1)^{(jrs+E)/2^{t+1}}
\tag{123.S2}
\]

when \(M=2^tM_0\), \(M_0\) odd. The factor map is invertible for
\(j\ne0\) only after its congruences, orientations, supports, and literal
profiles are retained; it collapses at \(j=0\). Negative aliases are
conjugate orientations with the same character product.

All nonzero exact aliases \(E=0\) together are
\(O_\varepsilon(X^\varepsilon)\). Smooth summation deletes
\(|E|>X^{1+\rho}/L\) rapidly. Exact factorization therefore removes no
live near-defect difficulty.

## Shifted zero-alias theorem

Averaging length-\(H\) \(k\)-blocks before Cauchy gives an exact positive
block square. Its ordered-pair kernel satisfies

\[
 |\Gamma_{M,H}(r,s)|
 \ll_A\psi_H(M/r)\psi_H(M/s)
 \left(1+K\|M(1/r-1/s)\|\right)^{-A},
\tag{123.S3}
\]

where \(\psi_H(x)=\min(1,(H\|x\|)^{-1})\). A product-level layer cake
gives

\[
 \sum_{r\asymp R}\psi_H(M/r)^2
 \ll_\varepsilon(1+R/H)X^\varepsilon.
\tag{123.S4}
\]

Consequently the entire nearest-alias sector \(j=0\), not merely its
unshifted diagonal, satisfies

\[
 \sum_{j(r,s)=0}|\Gamma_{M,H}(r,s)|
 \ll_\varepsilon(1+R/H)X^\varepsilon.
\tag{123.S5}
\]

At \(H_0=\lceil X^{1/2}/D\rceil\), this is the square target. This is the
round's strict analytic gain.

## Power-excess inverse reduction

For every fixed \(\eta>0\), if
\(|\mathscr R_X|\geq X^{1/4+\eta}\), then after either lawful
integerization the exact shifted Gram has a positive-real contribution
\(\gg X^{1/2+2\eta}\) in

\[
 j\ne0,\qquad E\ne0,\qquad
 |E|\leq X^{1+\eta/10}/L.
\tag{123.S6}
\]

Both reciprocal selectors, every shifted profile and endpoint, positive
and negative aliases and defects, and all ordered-pair conjugates remain
inside (123.S6). This is a one-way fixed-power inverse theorem. It does
not prove the threshold estimate.

## Method obstructions and smallest survivor

The large two-adic centre changes the displayed congruence but the
quotient is exactly the original mod-four sign, so no near-defect saving
is automatic. A flat-density capacity formula is only a heuristic ledger;
no joint incidence estimate was proved.

A further fixed-alias attempt also fails as a uniform method. Transverse
Poisson summation has active quarter-shift translates of size
\(\nu\asymp L\). With the exact \(e(Mh/r)\) shift, the opposite character
channel satisfies

\[
 \partial_r\Phi+m=-{Mh+\nu(s^2-r^2)\over r^2}.
\]

Allowed shifts create nondegenerate interior stationary crossings for a
nonempty alias range. Thus Poisson plus a first-derivative
Kusmin--Landau bound does not prove a summable fixed-alias estimate.

The smallest shifted survivor is the complete signed sector (123.S6);
the smallest scalar survivor remains the complete Round-118 joint row
before either \(k\)-Cauchy or the \(k\)-triangle. A continuation needs a
joint stationary-lattice estimate across transverse mode, shift, alias,
and reciprocal variables, or a stronger inverse theorem for their
complete aggregate.

## Decision and proof status

Promote (123.S1)--(123.S5), the exact algebra (123.S2), the
exact-alias and rapid-tail deletions, and the fixed-power inverse
reduction (123.S6). Record the unshifted-Gram, automatic two-adic, and
fixed-alias first-derivative mechanisms as scoped obstructions.

The flat-smooth quarter estimate remains open. Sharp, starred, clipped,
hard, arithmetic-owner, and transition packets remain separate. Complete
UNBAL, hard TOP, BAL, M9-M2, both M1 parents, endpoint uniformity, M9,
and the Gauss-circle quarter target all remain open.

The internal global exponent remains \(1/3\). The audited external
benchmark remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots .
\]

Round 123 proves no global exponent improvement.

Resulting graph SHA-256:
`2b60eca238542d4f321a19c90f20163c6dd4cd7c60da6f324910b6db10b638c6`.
