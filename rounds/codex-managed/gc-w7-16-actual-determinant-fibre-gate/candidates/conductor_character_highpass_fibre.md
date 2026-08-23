# Candidate: determinant-increment character high-pass

Campaign: gc-w7-16-actual-determinant-fibre-gate

Status: conductor candidate for audit; no proof-state effect.

## 1. Proposed new interface

Round 95 leaves the one-sided determinant sum (117.D2). In increments
(p=a'-a), (q=b'-b), its exact arithmetic and phase are

\[
 n=aq-bp,
 \qquad
 e\!\left({cn\over\kappa_i b(b+q)}\right)
 =e\!\left({ca\over\kappa_i b}
 -{c(a+p)\over\kappa_i(b+q)}\right).
\tag{117.C1}
\]

The literal characters create complementary half-period shifts:

\[
 \text{M1: }q=2r,\quad
 \chi_4(b)\chi_4(b+q)=(-1)^r;
\tag{117.C2}
\]

\[
 \text{M2: }p=2s,\quad
 \chi_4(|a|)\chi_4(|a+p|)=(-1)^s.
\tag{117.C3}
\]

This is the first exact sign mechanism not used by coefficient-blind
Farey spacing.

## 2. Fibre widths

On (b,b'\asymp B), (|a|,|a'|\asymp A=LB/D), the determinant range is
(N_B\asymp B^2/W). Hence

\[
 |\{q:0<aq-bp<N_B\}|\asymp {BD\over WL}
\]

at fixed (p), while

\[
 |\{p:0<aq-bp<N_B\}|\asymp {B\over W}
\]

at fixed (q), away from clipped endpoints. At the top minimax shell
these are (Y^{19/48}) and (Y^{1/16}). The two orientations expose
different possible savings and must not be multiplied without checking
the determinant congruence and Cauchy factors.

## 3. One-dimensional candidates

For fixed (a,b,q), the (p)-phase is linear with frequency
(-c/(\kappa_i(b+q))). On a literal progression, Abel summation would
give a factor of the form

\[
 \min\!\left(P_B,
 {1\over\|\omega_{i,p}(c,b+q)\|}\right),
 \qquad P_B={B\over W},
\tag{117.C4}
\]

where the M2 half-character shifts (omega_{2,p}) by (1/2) after
the even-(p) reparametrization. The M1 phase has no (p)-character but
the same reciprocal frequency.

For fixed (a,b,p), the (q)-phase has

\[
 \phi_q'={c(a+p)\over\kappa_i(b+q)^2},
 \qquad
 \phi_q''=-{2c(a+p)\over\kappa_i(b+q)^3},
\tag{117.C5}
\]

and the M1 high-pass shifts the even-(q) dual lattice. At the top
minimax shell, (|\phi_q''|\asymp L^{-2}) on a (Y^{19/48})-long
interval. A one-variable B-process has (Y^{1/16}) dual modes of size
(L), so it saves one factor (L) over a (q)-triangle but still leaves
capacity above the target.

## 4. Two-dimensional diagnostic

The exact shift Hessian is

\[
 \det\nabla^2_{p,q}\phi
 =-{c^2\over\kappa_i^2(b+q)^4}.
\tag{117.C6}
\]

At (B\asymp\sqrt Y), (117.C6) is order one. A full two-dimensional
stationary transform may therefore preserve the determinant-strip area and
return to the primal correlation. The audit must compute the dual lattice,
parity shifts, strip boundary, and lift symbol before calling this an
obstruction or a saving.

## 5. First coefficient seam

Round 95 proves sampled variation only in the lift variable (g). It does
not supply bounded variation of

\[
 (a,b)\longmapsto
 \sum_g{\chi_4(g)\over g}U_{i,a,b}(g)
\]

along a determinant fibre. Primitivity, support entry/exit, and changing
lift ranges can create jumps. Before applying (117.C4) or (117.C5), a
lawful proof must either establish fibrewise variation after a Möbius and
endpoint decomposition or retain the actual lift sum inside the transform.

## 6. Promotion threshold

Promote only:

1. a complete (Y^{1/2+\varepsilon}) estimate;
2. a rigorously target-safe strict block region;
3. a quantified saving with its exact remaining capacity; or
4. a scoped no-go proving that the named high-pass/fibre transform
   self-returns after every literal coefficient and boundary is restored.

The identities and isolated one-variable savings do not by themselves
improve the global exponent.
