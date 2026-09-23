# Round 193 conductor strategy: rho-large gcd-scaled orientation involution

- Round: 193
- Starting graph:
  `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`
- Selected owner:
  `M9-M1-hard-top-high-radical-small-t-residual-estimate`
- Frozen component: the exact Round-192 jointly signed core, including the
  whole inherited rho-large remainder when (T=0)
- Planned allocation: at least 98% analytical/algebraic and at most 2%
  bounded diagnostic computation
- Mandatory next checkpoint: Round 194, after analytic Rounds 191--193

## 1. Frontier decision

Round 192 pays the complete small-Farey-covector union by signed-divisor
sparsity.  Its exact core has no static small covector and positive control
still loses (Y/(H_Bm)).  Static Farey iteration, long-step Abel, positive
covering, and arbitrary bounded-array control are therefore closed routes.

The first unused literal symmetry occurs before positive Fourier or height
norms, in the two opposing allocations of one opened even Fejer shift.  It
is not the complementary-factor map rejected in Round 185.  The original
character-leg gcd supplies an integral scale which can keep both transformed
allocations inside the hard cone.

Fix one opened opposing incidence

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\ {m odd},\qquad
 0<r<R_0,\quad 2\mid r,
\tag{193.1}
\]

and put

\[
 g=(d,d'),\qquad k=(m,m').
\tag{193.2}
\]

On (k=1), define

\[
 \tau_g(d,m,d',m')=
 (gm,d/g,gm',d'/g).
\tag{193.3}
\]

The tuple order in (193.3) is again character divisor, complementary
factor, upper character divisor, upper complementary factor.  Since the
two cofactors have the same parity and (k=1), they are odd.  The map is
integral, preserves (N,N+r,r), preserves (g) and (k=1), interchanges
the two opposing orientations, and is an involution.  On (r\equiv2\pmod4),

\[
 \chi_4(d')\chi_4(d)
 =-\chi_4(gm')\chi_4(gm).
\tag{193.4}
\]

Thus (193.3) is a genuine character-reversing relation before an absolute
value.  The round must decide whether its actual literal coefficient
commutator is target-safe on the widest rigorously priced invariant sector.

## 2. Frozen sector and target

Put

\[
 D_L=\lceil L^{1/2}\rceil.
\tag{193.5}
\]

Let (P_{\rm sw}) be the tau-invariant physical atom mask inside the exact
Round-192 core defined by

\[
 k=1,\qquad r\equiv2\pmod4,
\qquad |d-gm|\le D_L,
\qquad |d'-gm'|\le D_L.
\tag{193.6}
\]

The mask is inserted on the opened incidence labels retained by every
Fourier mode; it does not erase any endpoint field.  The frozen target is

\[
 \boxed{
 |P_{\rm sw}\mathscr R_{{\rm core},Y,Q}^{\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon}
\tag{193.T}
\]

uniformly for both signs and every dyadic (Y>H_B).  A stronger target for
the complete core is admissible only if every literal seam is proved.

The intended exact pairing for the full physical high-height block is

\[
 \frac12\sum_{\iota\in P_{\rm sw}}
 \chi_4(d')\chi_4(d)\,\Phi_r(N)
 \left\{
 \lambda_{N+r}(d')\overline{\lambda_N(d)}
 -\lambda_{N+r}(gm')\overline{\lambda_N(gm)}
 \right\},
\tag{193.7}
\]

where (\Phi_r(N)) denotes the unchanged Fejer and square-root phase
factor.  Equation (193.7) is a proposed identity to be verified, not an
accepted estimate.

## 3. Primitive-coordinate ledger

In the plus orientation, use the accepted variables

\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,
\quad Sv-Uw=h.
\tag{193.8}
\]

The condition (k=1) implies (U,v) odd, ((v,h)=1), and makes the
image the canonical minus tuple

\[
 (\kappa,g,U',v',S',w')=(\kappa,g,v,U,w,S).
\tag{193.9}
\]

The two close-allocation conditions imply

\[
 S+w\ll D_L/g,qquad
 |\kappa(v-U)|\ll D_L/g.
\tag{193.10}
\]

On the orbit-closed active support, the strict hard cone and (193.6) force
(g=O(1)).  A first deliberately coarse incidence envelope is

\[
 \sum_{\kappa,g}
 O\!\left({L\over\kappa g}
 \left(1+{D_L\over\kappa g}\right)
 \left(1+{D_L\over g}\right)^2\right)
 \ll L D_L^2\log(2L)+L D_L^3.
\tag{193.11}
\]

No height or site is to be counted twice.  The common-cell coefficient
commutator is expected to be (O(D_L/L)), so (193.11) is compatible with
(L^2X^\varepsilon).  The actual proof must separately price normalized
dyadic BV, every boundary collar, floors, stars, half weights, hard samples,
crossings, endpoint traces, and zero extensions.

## 4. Arithmetic-mask seam

For a squarefree endpoint product, write (d=g d_0).  The transformed
character divisor is (gm).  A prime dividing (g) remains on the
character leg, while every prime outside (g) is complemented.  Therefore
the Round-184 residual truth table (1,0,0,1) is invariant unless exactly
one selected prime lies in (g).

On the close active sector, (g) belongs to a fixed finite set.  The
Round-184 selected primes are distinct and satisfy a fixed
(O(L^{-1/2})) logarithmic separation.  The round must prove that a
one-selected-prime-in-(g) mismatch is absent for sufficiently large (L)
and costs (O_{B,\varepsilon}(L^2X^\varepsilon)) in the bounded remainder.
No selector invariance may be assumed without this argument.

Squarefreeness, divisor status, oddness, and allocation coprimality are
preserved exactly on every live endpoint because the product is unchanged,
(g\mid d), and the original product is squarefree.  All remaining literal
fields are handled by the close common-cell/BV/collar ledger, not deleted.

## 5. Passage through the Round-192 core

Let (\mathscr F_Y^\sigma) be the exact physical high-height block and
write the accepted linear decomposition through Round 192 as

\[
 \mathscr F_Y^\sigma
 =\mathscr S_{\le192,Y}^\sigma
 +\mathscr R_{{\rm core},Y,Q}^\sigma.
\tag{193.12}
\]

The physical mask (P_{\rm sw}) is independent of the Fourier mode and
may be inserted before the complete anchor Fourier expansion.  The full
mode sum must be recombined before using (193.4).  Every inherited safe
projection may be restricted only after proving that its existing absolute
count survives atom deletion.  The required exact relation is

\[
 P_{\rm sw}\mathscr R_{\rm core}
 =P_{\rm sw}\mathscr F
  -P_{\rm sw}\mathscr S_{\le192}.
\tag{193.13}
\]

No low-conductor, edge, imprimitive, projectively slow, inverse-small,
terminal, Fejer, or Farey-safe term may be lost or counted twice.  If even
one inherited safe estimate is not deletion-stable at the required atom
level, (193.13) is the first unproved seam and must be reported rather than
papered over.

## 6. Exact complement and method boundary

If (193.T) is proved, the exact new core complement consists of the
Round-192 core atoms satisfying at least one of

\[
 r\equiv0\pmod4,qquad
 (m,m')>1,qquad
 |d-gm|>D_L,qquad
 |d'-gm'|>D_L.
\tag{193.14}
\]

This disjunction is a partition only after a fixed first-failure ordering
is declared.  It is not a density statement.  A coefficient-uniform far
sector, separate-orientation norm, positive Fourier completion, or
unscaled complementary-factor exchange is already known to return capacity
or zero extension.  The new mechanism is admitted only because the gcd
scale makes (193.3) integral, cone-compatible on an active close sector,
and character reversing at (r\equiv2\pmod4).

Even complete success at (193.T) proves only a strict part of the exact
original-(t=1) residual.  It proves no original (t\ge2) estimate,
large-(G) near-resonant estimate, hard or smooth M1 parent, GAR, M2
parent, endpoint theorem, bridge, Gauss-circle target, or exponent.

## 7. Orthogonal tasks

### Task A: scaled-orientation discovery

Prove (193.3)--(193.13) and the strongest target-safe invariant sector.
Derive the exact involution, sign, mask, count, coefficient-difference,
BV/collar, and outer ledgers.  If (D_L=L^{1/2}) is too wide, identify the
largest rigorously priced scale rather than silently shrinking it.

### Task B: hostile core-projection and power audit

Attack integrality, gcd preservation, parity, selected-pair mask stability,
zero extension, active-box multiplicity, boundary collars, and restriction
of every inherited safe projection.  Construct the first exact failure or
prove the proposed power ledger.  Distinguish an operator-class capacity
control from literal lower mass.

### Task C: statement-only rederivation

From a finite self-contained packet, independently derive the scaled
orientation involution, character reversal, primitive-coordinate map,
close-sector count, and the first coefficient hypothesis needed for target
size.  It must not see the claimant strategy or reports.

## 8. Promotion and exit gates

Allowed terminal labels are:

- `hard_m1_t1_rho_large_core_target`;
- `strict_rho_large_gcd_scaled_orientation_sector`; or
- `gcd_scaled_orientation_involution_capacity_or_self_return_no_go`.

A strict result may create one subordinate proved node and update only the
already-open small-(t) owner.  A no-go may add only exact obstruction
evidence and rejected overclaims.  No graph mutation is applied without
independent seam reviews, exact reverse/replay, lifecycle validation, and
GREEN tests.  Round 194 is designed only after Round 193 closes.
