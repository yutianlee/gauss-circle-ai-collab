# Conductor review: alias norms, involution, and source scope

Campaign: m9-m2-balanced-nonzero-alias-defect-gate

Decision: pass as a scoped mechanism obstruction; no estimate for the
actual signed remainder.

## 1. Linear and square capacities

For fixed ((h,k,k',d)), the literal transform has (dL^3) aliases of
size ((dL)^{-1}). Thus

\[
 \sum_\mu |\text{alias amplitude}|\asymp L^2,
 \qquad
 \sum_\mu |\text{alias amplitude}|^2\asymp {L\over d}.
\tag{116.N1}
\]

The second quantity matches primal Plancherel capacity. The first is a
factor (dL) larger than the (L/d)-point primal progression. At (d=1),
aliaswise absolute values therefore raise the global (L^4) coefficient
capacity to (L^5). The sharp-boundary Fourier tails also have only
conditional (1/\mu) decay and must be grouped signed.

## 2. Reciprocal-frequency count repays only the transform loss

Write (k'=dv), with (v)-length (L/d). The literal reciprocal
frequency is

\[
 \alpha_{d,\mu}={Xd^2\over2\mu}.
\tag{116.N2}
\]

Near integrality at the natural resolution is

\[
 |Xd^2-2j\mu|\ll d^2L^2,
 \qquad j,\mu\asymp dL^3.
\tag{116.N3}
\]

An elementary product-window divisor count gives
(O_\varepsilon(d^2L^2X^\varepsilon)) resonant aliases. Dyadic summation
of

\[
 \min\!\left({L\over d},
 {1\over\|Xd^2/(2\mu)\|}\right)
\]

and multiplication by ((dL)^{-1}) costs
(O_\varepsilon(L^2X^\varepsilon)) per outer ((h,k)) at (d=1).
The (L^2) outer rows return (L^4X^\varepsilon), not the target
(L^3X^\varepsilon). Sharpening the one-frequency resonance count cannot
supply the missing independent factor (L).

## 3. Forced large-sieve clusters

For fixed (d), there are

\[
 N_d\asymp dL^3
\]

frequencies sampled on only

\[
 Q_d\asymp L/d
\]

values of (v). Partitioning the circle into (O(Q_d)) arcs of length
(Q_d^{-1}) forces a cluster of size

\[
 \gg {N_d\over Q_d}\asymp d^2L^2
\]

and at least

\[
 \gg {N_d^2\over Q_d}\asymp d^3L^5
\tag{116.N4}
\]

ordered close pairs. Coefficients supported on a sufficiently short
subarc show that every coefficient-uniform large-sieve constant is at
least (Q_d(N_d/Q_d)=N_d\asymp dL^3). This diagonal already exhausts the
available square capacity. A spacing-only (v)-large sieve cannot close
the scalar target after outer Cauchy.

## 4. Exact second-B-process involution

With (h+2s_d=d\ell_d) and (k'=dv), the nonconstant dual phase is

\[
 g(\mu)=-{Xd^2v\over2\mu}-{\ell_d\mu\over2}.
\tag{116.N5}
\]

Poisson on (mu\in\mathbb Z+1/2) introduces an integer (n) and the
factor ((-1)^n). Its stationary equation and Legendre phase are

\[
 \mu^2={Xd^2v\over\ell_d+2n},
 \qquad
 g(\mu)-n\mu=-dR\sqrt{v(\ell_d+2n)}.
\tag{116.N6}
\]

This is the original square-root phase on

\[
 k'=dv,\qquad h'=d(\ell_d+2n).
\]

The second stationary Jacobian is the reciprocal of the first, the two
Fresnel factors cancel, and

\[
 (-1)^{s_d}(-1)^n=(-1)^{s_d+dn}
\]

restores the primal character. The full dual range has (L/d) terms, the
original progression length. Hence two successive one-variable
B-processes are algebraically involutive and yield no saving by themselves.

## 5. The proposed positive row energy is overstrong

Let

\[
 S_B=\sum_{h',k'}\overline{a_B^{<}(h',k')}
 e(-R\sqrt{h'k'})
\]

and let (C_{h,k}) be the inner sum over the union of the two accepted
width-(L) corridors relative to ((h,k)). The proposed double-far row is
exactly

\[
 T_{h,k}=S_B-C_{h,k}.
\]

On a nondegenerate block core with (asymp L^2) outer pairs,
(|C_{h,k}|\ll_\varepsilon LX^\varepsilon), so

\[
 \|T\|_2\ge cL|S_B|-O_\varepsilon(L^2X^\varepsilon).
\tag{116.N7}
\]

Therefore

\[
 \sum_{h,k}|T_{h,k}|^2\ll_\varepsilon L^4X^\varepsilon
 \quad\Longrightarrow\quad
 |S_B|\ll_\varepsilon LX^\varepsilon.
\tag{116.N8}
\]

The scalar balanced target requires only the corresponding
(L^{3/2}X^\varepsilon) linear scale. The row energy is a genuinely
stronger, almost-replicated Gram target. This does not prove it false for
the actual symbol, but it rejects it as an equivalent or harmless
reformulation. A phase-adapted bounded array also makes its
coefficient-uniform analogue have (L^6) capacity.

## 6. Source fit

Vandehey's one-dimensional van der Corput transform supports the
normalization and explicit involution check after the literal progression
and endpoint audit. It supplies no estimate for the joint signed kernel.

Li and Ma's three-dimensional exponential-sum theorem assumes a separated
monomial/reciprocal phase, factorized coefficients, fixed exponents and
perturbation, and an explicit parameter condition. The Round-116 kernel
has divisor-dependent lattices, coupled gcd and slanted weights, residue
phases, pair-dependent gates, and boundary kernels. Those hypotheses and
the abstract spacing energies have not been matched, so the theorem does
not import.

Primary-source audit:

- https://arxiv.org/abs/1205.0090
- https://arxiv.org/abs/2302.05870

## 7. Review decision

Promote a single scoped obstruction covering:

1. aliaswise absolute values;
2. reciprocal-(v) resonance counting alone;
3. coefficient-uniform spacing-only large sieves followed by outer
   absolute values or Cauchy;
4. a second one-variable B-process; and
5. treating the positive row energy as equivalent to the scalar target.

The smallest lawful survivor is the complete signed
((d,\mu,h,k,v)) divisor-reciprocal cluster-defect kernel with both gates,
the actual amplitudes, and all boundary pieces retained. No
(L^3X^\varepsilon) estimate for it is known. This obstruction does not
give a lower bound for the actual remainder, does not disprove BAL, and
does not alter any downstream exponent.
