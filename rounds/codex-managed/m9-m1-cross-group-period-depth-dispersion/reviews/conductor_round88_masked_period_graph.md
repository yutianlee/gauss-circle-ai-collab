# Round 88 conductor review: masked periods and the good-prime graph

## Verdict

Certify two algebraic routing identities and one restricted analytic
deletion:

1. the exact local period is the period of the complete masked weight;
2. a depth-\(j\) completed local trace descends with factor \(p^{2j}\);
3. after the coarse deletion, sufficiently deep good-prime
   reciprocal-mask fibres are target-safe by a directed-degree bound.

## Exact masked depth and descent

For a nonempty local unit mask modulo \(q=p^\nu\), let the masked
reciprocal weight have period \(p^{\nu-j}\). Its unprefactored Fourier
transform is supported on \(p^j\mid u\). Because the completed trace has
the extra outer factor \(q\), its exact descent is

\[
 \mathfrak T_q(p^ju')=p^{2j}
 \mathfrak T^{\downarrow}_{p^{\nu-j}}(u').
\]

The commonly guessed factor \(p^j\) belongs only to the unprefactored
Fourier transform. CRT tensorization is over full prime powers and keeps
the full \(2\)-part. Empty masks are zero tensors.

This frequency sparsity does not by itself save the Fejer mass: the
restricted Fejer sum has the compensating rescaling that returns total
mass \(D\).

## Good-prime rigidity

Assume \(p\geq11\), \(p\nmid K\), the mask is nonempty, and the
reciprocal masked weight has nontrivial period \(p^{\nu-j}\). With
\(a=\min(j,\nu-j)\), inverse Taylor expansion at a suitable multiple of
the period gives \(p^a\mid\Phi'(x)\) on every allowed residue. The
derivative numerator has degree at most five, while at least seven
residues are allowed. Six-point Vandermonde inversion and induction in
\(a\) therefore give

\[
 p^a\mid(B-A),\qquad p^a\mid AV,qquad
 p^a\mid AV(V+B).
\]

The root count uses the mask and fails as a uniform classification at
small primes. The exact \(p=3,5\) examples in the hostile report verify
that this restriction is substantive.

## Directed graph and exponent

For the unique maximal reciprocal-period vector set

\[
 \mathfrak a=
 \prod_{\substack{p^\nu\Vert M\\p\geq11,\ p\nmid K}}
 p^{\min(j_p,\nu-j_p)}.
\]

A fixed first physical pair has at most
\(X^\varepsilon M^2/\mathfrak a\) partners, and the same holds after
reversing the edge. Schur's inequality and the centered Fejer kernel
give

\[
 |\mathcal G_{\rm good\ depth}(D)|
 \ll_\varepsilon X^\varepsilon
 DB^3{M^2\over\mathfrak a}T^4Q^{-5/6}.
\]

With

\[
 \rho_*=min\!\left(M,
 \left\lfloor J^{11/30}B^{-2}\right\rfloor\right),
\]

the condition \(\mathfrak a\geq M^2/\rho_*^2\) is target-safe. Coarse
edges are removed first, so overlap only lowers the graph degrees.

## Retained residual

No estimate is certified here for affine/full-phase periods, small
primes, nonunit \(K\), the \(2\)-part, small \(\mathfrak a\),
projection-only depth, or aperiodic tensors. The exact \(q^2/3\)
small-prime trace rules out a coefficientwise square-root shortcut.
No external theorem is used in the promoted argument.

