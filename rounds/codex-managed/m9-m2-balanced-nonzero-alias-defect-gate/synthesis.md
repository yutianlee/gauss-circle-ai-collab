# Round 116 synthesis: literal aliases exposed, one-alias route parked

Campaign: m9-m2-balanced-nonzero-alias-defect-gate

Round type: analytic proof-design gate

Starting recorded graph SHA-256:
6421d27cb531be922b11ec48b51002ba568f235d510d16ac28a7d84881d66dad

Resulting graph SHA-256:
a27a89fd4e688cae719a28fec8f48dd74190bafb64d0345c590f1caadc2805d9

## 1. Conductor decision

Promote the literal divisor-progressive half-shifted Poisson reduction and
a scoped one-alias/reciprocal-large-sieve self-return obstruction. Retain
the actual oscillatory remainder and the balanced packet estimate as open.

Round 116 makes the proposed nonzero-alias mechanism exact and then shows
why its coefficient-blind norm variants do not supply the missing factor
(L):

- the second gcd mask changes the clean half-integer lattice into a family
  of odd-divisor progressions with a non-removable residue phase;
- finite Poisson and stationary phase reduce the remainder to a complete
  signed lifted kernel with target-safe aggregate errors;
- aliaswise absolute values inflate (L^4) primal capacity to (L^5);
- reciprocal-frequency divisor counting only restores (L^4) capacity;
- spacing forces large clusters and a full-length large-sieve diagonal;
- a second B-process is exactly involutive; and
- the proposed positive row energy is substantially stronger than the
  scalar target.

No (L^3) bound, balanced packet estimate, M2 parent, M1 parent, M9
estimate, or new exponent is proved.

## 2. Literal divisor-progressive alias chart

Write (h'=h+2s), (k'=k+q). On character support,

\[
 \chi_4(h)\chi_4(h+2s)=(-1)^s.
\tag{116.S1}
\]

Expanding the second low-gcd mask introduces odd divisors (d\mid h',k').
Choose (s_d\pmod d) with (h+2s_d\equiv0\pmod d), and put

\[
 s=s_d+dt,\qquad h'=d(\ell_d+2t),\qquad
 \ell_d={h+2s_d\over d}.
\tag{116.S2}
\]

Poisson in (t) has

\[
 \mu={1\over2}-m\in\mathbb Z+{1\over2},qquad
 \lambda={\mu\over d}.
\tag{116.S3}
\]

An interior stationary point is

\[
 x=h'={Xk'\over\lambda^2},
\tag{116.S4}
\]

and the phase is

\[
 \Psi_d
 =R\sqrt{hk}-{Xk'\over2\lambda}-{\lambda h\over2}
 +s_d(1/2-\lambda).
\tag{116.S5}
\]

With (lambda_0=R\sqrt{k/h}), this is exactly

\[
 \Psi_d
 =-{h(\lambda-\lambda_0)^2\over2\lambda}
  -{Xq\over2\lambda}+s_d(1/2-\lambda).
\tag{116.S6}
\]

There are (asymp dL^3) aliases of spacing (1/d), each with stationary
amplitude (asymp(dL)^{-1}). Equal rational values of (lambda) from
different lifts may not be merged.

## 3. Gates, errors, and exact survivor

At (116.S4), with (lambda_r=Rk'/\sqrt{hk}),

\[
 \rho=hk'-xk
 ={hk'\over\lambda^2}(\lambda^2-\lambda_0^2),
\qquad
 \Delta=xk'-hk
 ={hk\over\lambda^2}(\lambda_r^2-\lambda^2).
\tag{116.S7}
\]

Each width-(L) forbidden corridor removes only (O(dL^2)) aliases from
the (dL^3)-long family. The two gates remain coupled through
(Delta+\rho=q(h+x)).

For fixed ((h,k,k',d)), the literal support and gates give only (O(1))
integer runs. Finite Poisson on half-integer-enclosed runs, with incomplete
Fresnel factors at transition modes, has total boundary, nonstationary,
support-crossing, and stationary-remainder cost (O(X^\varepsilon)) per
outer triple after divisor summation. Hence the global error is

\[
 O_\varepsilon(L^3X^\varepsilon).
\tag{116.S8}
\]

Let (mathcal K_B) be the complete signed lifted stationary kernel with
((h,k,k',d,\mu)), both symbols, both gates, (gamma_d), and all
transition factors retained. Then

\[
 \mathcal R_B^{\mathrm{osc}}
 =\mathcal K_B-M_B^{(0)}+O_\varepsilon(L^3X^\varepsilon).
\tag{116.S9}
\]

The Round-115 phase-free owner (M_B^{(0)}) is used once. The first open
analytic assertion is therefore

\[
 |\mathcal K_B^{\mathrm{bulk}}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{116.S10}
\]

No report proves (116.S10).

## 4. Reciprocal frequency, clusters, and involution

Writing (k'=dv), the (v)-frequency is

\[
 \alpha_{d,\mu}={Xd^2\over2\mu}.
\tag{116.S11}
\]

The natural near-integral condition is

\[
 |Xd^2-2j\mu|\ll d^2L^2,
\qquad j,\mu\asymp dL^3.
\tag{116.S12}
\]

An optimal elementary divisor-window count and dyadic geometric-sum bound
cost (L^2X^\varepsilon) per outer ((h,k)) at (d=1), hence (L^4)
globally. They repay the first-transform inflation but do not save the
extra factor (L).

More generally, (N_d\asymp dL^3) frequencies are sampled at only
(Q_d\asymp L/d) points. At resolution (Q_d^{-1}), pigeonhole forces
clusters of size (d^2L^2) and at least (d^3L^5) ordered close pairs.
Every coefficient-uniform large-sieve constant is at least
(N_d\asymp dL^3), its full diagonal length.

Finally, up to constants, the alias phase is

\[
 g(\mu)=-{Xd^2v\over2\mu}-{\ell_d\mu\over2}.
\]

A second B-process in (mu\in\mathbb Z+1/2) has

\[
 \mu^2={Xd^2v\over\ell_d+2n},
\qquad
 g(\mu)-n\mu=-dR\sqrt{v(\ell_d+2n)}.
\tag{116.S13}
\]

This is the original phase on (k'=dv),
(h'=d(\ell_d+2n)). The Jacobians and Fresnel factors cancel, the
half-lattice factor restores ((-1)^s), and the full dual range has the
original (L/d) length. Two B-processes therefore self-return exactly.

## 5. Stronger row energy and source scope

The proposed positive local energy

\[
 \sum_{h,k}|T_{h,k}|^2\ll_\varepsilon L^4X^\varepsilon
\tag{116.S14}
\]

is sufficient by Cauchy but not equivalent. If (S_B) is the unrestricted
inner scalar sum and (C_{h,k}) contains the two corridors, then
(T_{h,k}=S_B-C_{h,k}) and
(|C|_2\ll_\varepsilon L^2X^\varepsilon). On a nondegenerate core,
(116.S14) forces

\[
 |S_B|\ll_\varepsilon LX^\varepsilon,
\tag{116.S15}
\]

which is stronger than the (L^{3/2}) scalar scale. The row norm is a
nearly repeated full-sum Gram; it is false coefficient-uniformly and
remains unproved for the actual symbol.

Vandehey's B-transform paper supports the normalization and involution
audit, not (116.S10). Li--Ma's generalized double-large-sieve theorem has
separated phase and coefficient hypotheses not matched by the literal
divisor-progressive kernel; its abstract spacing form merely renames the
unproved coupled energy. No external theorem is imported.

## 6. Proof-state effect

Create a proved literal alias reduction and a proved scoped obstruction for
aliaswise absolute values, reciprocal-(v) counting alone, spacing-only
large sieves, second B-process gain, and equivalence of the row energy.
Update the open remainder, actual energy, and balanced packet to point to
the complete signed divisor-reciprocal cluster-defect kernel.

Reject the clean divisor-independent alias grid, merging of rational lifts,
aliaswise (\ell^1), reciprocal-frequency-only closure, second-transform
gain, row-energy equivalence, and direct Li--Ma transfer.

No status change is made to the oscillatory remainder, actual double-far
energy, BAL, hard TOP, UNBAL, M9-M2, either M1 parent, endpoint uniformity,
M9, the conditional bridge, or the Gauss-circle target.

## 7. Full-proof strategy after the gate

This is the authorized Round-116 review point for the broad balanced
follow-through. The literal alias route has produced an exact reduction and
a rigorous no-go, but neither a target-safe strict subrange nor any positive
power saving. Repeating a one-alias triangle, reciprocal-frequency large
sieve, positive row Gram, or inverse B-process is therefore parked. BAL
itself is not rejected: it may be revisited only with a genuinely new joint
signed theorem for the full lifted kernel.

The next bounded lane is the graded (W=Y^{7/16}) actual reduced-
determinant correlation. Its exact target (Y^{1/2+\varepsilon}) would
give the internal exponent (5/16), improving (1/3) but not proving the
quarter theorem or any M9 node. The first task is to audit the literal
one-sided determinant phase, recompute the (Y^{43/48}) coefficient-blind
capacity and (Y^{19/48}) deficit, and identify a sign-preserving mechanism
or a scoped obstruction. If that lane self-returns, proceed to the
prescribed-centre UNBAL falsification probe and then direct M1
minimization.
