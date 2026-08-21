# Conductor Strategy for a Full Proof

> Superseded for rounds after 89 by
> `strategy/conductor_0817_full_proof_strategy.md`. Retained for
> provenance and the Round-77--88 execution record.

Date: 2026-08-16  
Status: adopted strategy; no theorem or graph node is promoted by this file.  
Authoritative graph SHA-256 at adoption:
`e14373a05ee7d55258b53f07e18afa33682806add90bee49789208f464e46166`.

## 1. Evaluation of the four strategy memoranda

The common strategic diagnosis is correct:

1. retain the exact hyperbola--sawtooth--Vaaler reduction;
2. stop treating another matched Poisson, stationary-phase, Hankel, or
   Kuznetsov transformation as a source of cancellation by itself;
3. keep the actual character and Vaaler/profile coefficients until the
   final signed estimate;
4. formulate the remaining endpoint problem as a signed arithmetic
   energy problem, not as an unsigned spacing problem.

The strongest contribution of `A1_0816_1.md` is the conceptual pivot from
transform iteration to primitive-ray resonance geometry.  The strongest
contribution of `A2_0816_2.md` is the sequencing rule: the complete
actual-symbol interface must be certified before the resonant union is
estimated.

The following proposed features are revised.

- The square-family mass is **not** the first lawful round.  Its weight is
  not well-typed until the collar-extracted centred integral, all endpoint
  terms, the stationary error sum, and step-two variation are proved.
  Moreover, Round 76 already shows that the exactly integral square rays
  are target-safe; the unresolved square test is the complete
  coefficient-weighted *near*-resonant family.
- Administrative state reconciliation is required before new work is
  dispatched, but it is maintenance rather than the mathematical content
  of Round 77.
- A repository-wide retrospective `cb` tagging pass is not a prerequisite
  for the proof and risks introducing a second incomplete classification.
  New candidate statements and briefs will instead state explicitly
  whether they are coefficient-uniform and which false adversarial or
  unsigned analogue they avoid.
- Decoupling and incidence bounds may control a coefficient-blind counting
  input, but they cannot be the last step of the signed endpoint estimate.
- The M1 source lane is mandatory for a full proof, not merely optional.
  New Kloosterman results remain candidates until an exact input map passes.

One source-hygiene correction is also necessary.  The claim in
`A2_0816_2.md` that arXiv:2606.28986 is nonexistent is false: Yixiu Xiao's
paper exists.  Its moment results remain comparison material, not an M9
dependency.  Bourgain--Watt arXiv:1709.04340 and Dong--Robles--Zeindler
arXiv:2601.00292 are withdrawn and cannot be proof dependencies.

## 2. Accepted status at the decision point

The graph contains 204 obligations: 147 `proved_internal`, 8
`proved_external_dependency`, 16 `derived_under_assumptions`, 21 `open`,
7 `proposed`, 2 `diagnostic_only`, 2 `rejected`, and 1
`source_audit_required`.

The theorem-level implication remains

\[
  H1\text{--}H3+H4+R5\text{-Full}+M9
  \Longrightarrow
  P(X)\ll_\varepsilon X^{1/4+\varepsilon}.
\]

`M9`, `M9-M1`, `M9-M2`, endpoint uniformity, and the global target are
open.  No new global exponent has been proved.

For M1, the beta wrapper and several terminal modules are closed, and the
accepted conductor analysis is target-safe through

\[
  C\le J^{32/45}=X^{16/45}.
\]

The residual upper-conductor interval

\[
  J^{32/45}<C\le J
\]

still contains a coherent, actual-unit, incomplete-numerator
off-diagonal.  Current transformations and source imports do not close it.

For M2, the exact hard-top transposed energy is accepted:

\[
  \mathcal E_L^\top=\sum_m\left|
  \sum_{\substack{h\in\mathscr H_L\\m\le h\le4m}}
  \chi_4(h)a(h,m)e(\sqrt{Xhm})\right|^2,
  \qquad
  \mathcal E_L^\top\ll_\varepsilon L^2X^\varepsilon
\]

is sufficient.  Its diagonal, fixed offsets, and fixed endpoint collars
are target-safe.  The surviving interior is signed.  Round 76 proved that
odd gcd lifts have step two and that the correct bulk resonance is

\[
  \left\|\frac{X(\sqrt b-\sqrt a)^2}{2k}\right\|
  \lesssim G_{a,b}^{-1}.
\]

It did **not** prove the energy or the complete centred-integral symbol.

## 3. Full-proof architecture

The route has four mandatory analytic gates and one final assembly gate.

### Gate I: exact M2 actual-symbol normal form

Starting from the accepted finite transposed energy, prove a complete
collar-extracted Poisson/gcd-lift identity.  The theorem must retain the
actual `Phi`, spatial profile, floors, `q_X`, both endpoints, all
stationary corrections, and the summed nonstationary error.  It must prove
the step-two variation bound for the complete centred integral, not for a
frozen leading coefficient.

This is Round 77.  Until it passes, no weighted resonance theorem can be
promoted.

### Gate II: structured M2 resonances

With the accepted symbol from Gate I, separate the complete resonant union
into algebraically structured and generic parts.  Test first the full
near-resonant square/common-squarefree-kernel families, including metric
near-resonances and the actual signed unit.  Exact divisor resonances are
already known to be too small; the new work is the near-resonant weighted
mass.

The output must be either a target-size structured estimate or a rigorous
actual-coefficient obstruction.  Raw resonance counts are insufficient.

### Gate III: generic M2 signed energy

Prove a quantitative inverse theorem: high multiplicity in

\[
  \frac{X(\sqrt b-\sqrt a)^2}{2k}\pmod1
\]

forces one of the structured families removed at Gate II.  Apply any
incidence, determinant, or decoupling estimate only to the generic
counting input.  Close the energy with a signed primitive-ray large sieve,
`TT*`, or equivalent argument that retains the actual `chi_4`/profile
unit.  Taking absolute values over primitive pairs or reciprocal modes is
forbidden by the accepted controls.

### Gate IV: residual M1 upper conductor

Map the exact incomplete-numerator M1 kernel to current bilinear
Kloosterman/Sali\'e technology.  Each attempted import must provide a
table matching modulus, numerator and dual lengths, parity/character,
weight regularity, and uniformity.  A failed range match is a recorded
barrier.  Round 81 has reduced the target interval to
`J^(13/18) < C <= J`; do not spend another round on the already closed
transition representation.

Blomer--Pascadi arXiv:2607.24311 and Pascadi arXiv:2511.08445 exist and
are candidates, but neither is a dependency before a theorem-level input
map passes.  Withdrawn sources are excluded.

### Gate V: uniformity and final assembly

After both M1 and M2 close, prove uniformity over every active dyadic
`D`, reconcile `R5-Full`, and then apply the accepted conditional bridge.
Only this gate may promote `M9` and the exponent (1/4+\varepsilon).

## 4. Numbered round sequence

1. **Pre-Round-77 maintenance:** synchronize the completed Round 76 in
   the ledger, campaign pointers, failure ledger, reading packet, project
   summary, proof-draft scope, and source cards.  Do not change a theorem
   status merely to repair a derived document.
2. **Round 77 — M2 actual-symbol odd-lift normal form.**  Independently
   prove or refute the collar-extracted centred-integral identity, summed
   Poisson error, and step-two variation.  Required controls include the
   `(81,121)` half-integer family, saddle entry/exit, lower-ceiling mod-four
   seam, `Phi` and `W` transitions, stars, adversarial coefficients, and
   rank-one self-return.
3. **Round 78 — structured near-resonance mass.**  Treat square and
   common-squarefree-kernel families with the complete Round-77 symbol.
4. **Round 79 — generic reciprocal-resonance inverse theorem.**  Prove a
   spacing/incidence theorem or a sharp no-go for the remaining frequency
   set.
5. **Round 80 — signed primitive-ray energy.**  Combine Gates II--III
   without an absolute sum over rays or modes.
6. **Subsequent M1 rounds — exact modern-source input maps and residual
   conductor closure.**  Stop every source route at its first failed
   hypothesis.
7. **Assembly rounds — endpoint uniformity, R5 reconciliation, M9, and
   the final bridge.**

If Round 77 rejects the centred-integral or variation formula, redesign
from the exact finite energy before doing resonance counting.  If Round
78 produces an actual-coefficient lower bound above `L^2`, the current
M2 survivor is false and the program must return to the earlier row-energy
decomposition.  These are productive exit conditions, not failures of
the research protocol.

## 5. Secondary deliverables

The following are useful but cannot substitute for the five gates:

- extract the strongest unconditional global exponent actually implied by
  the accepted graph, without filling an open corridor by optimism;
- prove exceptional-set or averaged variants under separate obligation
  IDs;
- maintain source cards and withdrawal checks;
- formulate partial-exponent targets separately from `GC-target`;
- use bounded computation only to falsify resonance classifications or
  check exact constants.

## 6. Promotion discipline

Every new candidate must state:

1. whether it is coefficient-uniform;
2. which known-false unsigned or adversarial analogue it avoids;
3. where the actual `chi_4`, `Phi`, or moving profile enters;
4. exact endpoint and star ownership;
5. the first unproved step;
6. why the result is not another transform self-return;
7. its precise implication in the graph.

The proof program therefore adopts the shared strategic pivot, but with
the order

\[
  \boxed{
  \text{exact actual symbol}
  \longrightarrow
  \text{structured/generic resonance geometry}
  \longrightarrow
  \text{signed energy}
  }
\]

for M2, together with an exact incomplete-Kloosterman input-map program
for M1.  No global exponent changes at adoption.

## 7. Post-Round-80 execution update

Rounds 77--80 completed the planned M2 symbol and resonance audit.  The
primitive-square family is target-safe, exact nonsquare centers and the
positive-safe blocks are removed, but the remaining metric density cannot
be killed by nearest-integer parity: the complete coefficient carrier
cancels that parity and restores the zero Fourier mode.  M2 is therefore
now frozen at the genuine signed cross-row
\(\chi_4(h)\chi_4(s)\) density--discrepancy energy.  Further M2 work must
attack that correlation directly; another parity, recentering, or adjoint
Poisson representation is not a new mechanism.

Round 81 temporarily returns to Gate IV at a concrete, potentially
range-improving seam.  For the fixed-interior M1 Farey rows, test whether
the neighbor-dependent stationary factor has the complete-symbol split

\[
 W(c)=\Gamma V(c)+O_\varepsilon\!\left(X^\varepsilon\sqrt{C/J}\right),
\]

where \(V\) has global bounded variation on each residue progression and
\(\Gamma\) is the neighbor-independent full, half, or zero Gaussian
coefficient.  This formulation deliberately avoids the likely false
global-BV assertion for the raw Farey sawtooth.  Combined with the audited
reciprocal exponent pair, it would extend the accepted fixed-interior
range from \(C\leq J^{32/45}\) to \(C\leq J^{13/18}\).  This would be a
genuine local proof improvement, but it would not change the global Gauss
circle exponent or close the remaining M1 and M2 corridors.

## 8. Post-Round-81 execution update

Round 81 proves the proposed complete-symbol split.  The exact moving
Farey transition can have raw variation \(\sqrt{J/C}\), but it is
pointwise \(O(X^\varepsilon\sqrt{C/J})\).  The neighbor-independent
critical coefficient is globally BV.  Bourgain's audited reciprocal
exponent pair therefore extends the fixed-interior safe range to

\[
 T\le C\le J^{13/18}.
\]

The next M1 corridor is

\[
 J^{13/18}<C\le J^{3/4},
\]

where only the smooth nonaxial main energy is missing.  This is the clean
place to test a hybrid residue/numerator large sieve: open the exact local
unit, apply Poisson or reciprocity only once, and demand an average saving
that is demonstrably not the Round-73 short-Hecke self-return.  Any new
source route must quantify the remaining power deficit at both endpoints
of this band.  Above \(J^{3/4}\), transitions and axes re-enter and must
be retained.

No global exponent changes.  M2 remains frozen at the genuine complete
\(\chi_4(h)\chi_4(s)\) cross-row density--discrepancy energy.

## 9. Post-Round-82 execution update

Round 82 shows that the transition-flattened Kloosterman transform does
not close the first residual band by any coefficient-blind or current
black-box route.  It does, however, remove the entire same-residue mode
and each fixed nonzero residue-offset layer.  The exact first survivor is

\[
 \mathfrak X_C^{(\kappa,k)}=
 \sum_{b\asymp C/T}\sum_{r\ne s}
 u(r)\overline{u(s)}R(r)\overline{R(s)}.
\]

The next M1 step is therefore not another full Poisson or spectral
return.  It is a genuine offset-dispersion problem with the actual local
unit retained.  Absolute offset summation loses (B=C/T).  Any fixed
gain (B^{-\delta}) yields a polynomial range extension; the concrete
milestones are

\[
 \delta={1\over2}\Longrightarrow C\le J^{56/75},
 \qquad
 \delta={5\over9}\Longrightarrow C\le J^{3/4}.
\]

Current fixed-modulus bilinear Kloosterman theorems do not map to this
varying-modulus product correlation, and the complete transform is
involutive.  Round 83 should open the inverse/even unit directly and test
correlation across residue offsets, with a statement-only gate and a
current trace-function/source audit.  No global exponent changes.

## 10. Post-Round-83 execution update

Round 83 derives the two even arithmetic units rather than inferring them
from the odd class. After the exact rescaling \(c=g_\kappa x\), every
class has an inverse unit modulo \(M\in\{4b,2b,b\}\). Exact Poisson and
finite orthogonality then remove the literal dual difference \(d=0\)
target-safely. The first M1 survivor is now

\[
 {1\over M^2}\sum_{b\asymp B}\sum_{d\ne0}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.
\]

The strategic implication is narrow but useful: the next round should
not re-complete the residue offsets. It should first derive the uniform
stationary form of \(I_b(n)\), whose exact critical phase is

\[
 2\sqrt{{A_{\kappa,b}|n|\over g_\kappa M_\kappa}}
 =\left(\sqrt X+{\sqrt{\kappa k}\over b}\right)\sqrt{|n|},
 \qquad |n|\asymp Q^2,
\]

and then test signed cancellation in the nonzero difference \(d\), with
the Kloosterman product and Ramanujan subtraction retained. Nonstationary
tails, saddle entry and exit, \(d\equiv0\pmod M\) with \(d\ne0\), and
prime-power gcd modes must be owned explicitly. A transform that returns
to the original residue row is still a no-go.

No conductor range, `M9-M1`, `M9-M2`, `M9`, or global exponent changes.

## 11. Post-Round-84 execution update

Round 84 proves that the actual stationary Fourier profile does give a
genuine deletion before the completion self-return becomes binding.  For
the smooth principal row, exact Kloosterman residue Parseval and
second-derivative cancellation on \(n=r+M\ell\) make every

\[
 0<|d|\leq\lfloor J^{17/30}\rfloor
\]

target-safe, uniformly through \(C=J^{3/4}\).  The proof uses the
Round-81 smooth extension and its integrated \(c\)-seminorm; bare BV is
not enough.  It retains negative differences, nonzero modulus multiples,
prime-power gcd modes, entry and exit, and stationary errors.

The M1 first-band survivor is now the same centered Kloosterman-product
correlation restricted to larger differences.  The next mechanism must
couple \((d,b,r)\) before absolute values.  Re-completing \(d\), applying
a coefficientwise prime-field trace bound, or repeating the stationary
transform is excluded: all three either fail at prime powers or return to
the original rank-one progression.

This is a strict proof-state improvement but not a conductor-range or
global-exponent improvement.  M2 remains at the complete
\(\chi_4(h)\chi_4(s)\) cross-row density--discrepancy energy, and final
assembly remains gated by both M1 and M2 plus endpoint uniformity and
`R5-Full` reconciliation.

## 12. Post-Round-85 execution update

Round 85 proves a second, disjoint deletion in the same smooth principal
M1 dual correlation. If \(\Delta_b\asymp Q^2\) is the exact stationary
support diameter, compact endpoint flatness and a fresh all-difference
error summation make

\[
 |d|\geq\Delta_b-Q^2J^{-1/20}
\]

target-safe. The graph records \(E_*=Q^2J^{-1/20}=J^{3/4}\); the reports
prove the analogous fixed-\(\delta\) collar for every fixed
\(\delta>0\). Combined with Round 84, the exact first-band survivor is

\[
 \lfloor J^{17/30}\rfloor<|d|<\Delta_b-J^{3/4}.
\]

The shifted physical-row identity retains the \(Q^{-5/24}\) row saving,
but its multiplier triangle gives no power of \(B\). A literal
\(d\)-A-process has a safe diagonal and leaves an actual-symbol weighted
four-Kloosterman off-diagonal. This is the next M1 interface. Round 86
should attack it through the continuously twisted-row ambiguity form,
not through another full completion; prime-power modes, modulus multiples,
and the physical \(Q^{-5/12}\) energy factor must remain explicit.

No conductor or global exponent changes. M2 remains frozen at the
complete \(\chi_4(h)\chi_4(s)\) cross-row density--discrepancy energy.

## 13. Post-Round-86 execution update

Round 86 extracts one more strict deletion from the first M1 residual
band without opening the Kloosterman coefficient. On each progression,
the square-root difference phase has fixed-sign cubic curvature

\[
 \asymp {JM^3|d|\over Q^7}.
\]

Together with the exact residue \(L^1\) normalization, this makes every

\[
 \lfloor J^{17/30}\rfloor<|d|\le
 \lfloor J^{87/140}\rfloor
\]

target-safe. The remaining first-band interval is

\[
 \lfloor J^{87/140}\rfloor<|d|<\Delta_b-J^{3/4}.
\]

The next M1 attack must not be a generic complete-trace bound. Exact
completion shows prime-power near-returns and squarefree
divisor-aligned modes of near-quadratic size already at shifts below
one modulus. The lawful target is therefore a joint actual-symbol
exceptional-strata theorem: isolate and sum these aligned modes, then
control the generic remainder before absolute values, retaining both
Ramanujan cross terms, the square term, and \(Q^{-5/12}\).

No conductor or global exponent changes. M2 remains frozen at the
complete \(\chi_4(h)\chi_4(s)\) cross-row density--discrepancy energy.

## 14. Post-Round-87 execution update

Round 87 resolves the largest explicit exceptional complete traces
without a coefficientwise trace theorem.  After correcting a fatal
\(M^4\) normalization error, the normalized physical rows and the full
Fejer shift \(U=D\) give

\[
 \mathcal P_{\rm exc}(D,D)
 \ll_\varepsilon X^\varepsilon DB^3T^4Q^{-5/6}
 \ll_\varepsilon X^\varepsilon {D\over B}J^{14/5}.
\]

The full-factor active-set decomposition absorbs every mixture of the
local-zero and paired branches, including the prime-power and squarefree
near-quadratic hostile families.  The correct next M1 interface is no
longer “all exceptional strata.”  It is the cross-group off-diagonal
after the global \(u=0\) diagonal is owned once.  This residual has two
different mechanisms and should be split before another estimate:

1. exact partial-period/lower-conductor returns, including bad primes and
   the complete \(2\)-adic ledger;
2. genuinely aperiodic local traces with at least one full-factor group
   mismatch.

The next round should test tensor/CRT quasi-orthogonality for the second
class and an exact period-depth induction for the first.  It must use
\(U=D\), retain the actual fourfold stationary symbol and
\(Q^{-5/12}\), and must not reinsert the already-paid \(u=0\) diagonal.
No conductor range or global exponent changes.  M2 remains frozen at its
complete cross-row density--discrepancy energy.

## 15. Post-Round-88 execution update

Round 88 shows that the strict cross-group M1 object has two independent
depth notions. Coarse physical-label depth is a divisor-lattice
equivalence relation and yields an exact positive grouping. Functional
masked-period depth is edgewise and must be handled by a degree or signed
operator estimate.

The coarse grouping removes every

\[
 R_*\leq\rho_*=min\!\left(M,
 \left\lfloor J^{11/30}B^{-2}\right\rfloor\right).
\]

For \(p\geq11\), \(p\nmid K\), masked-period rigidity supplies a second
deletion when the product conductor satisfies

\[
 \mathfrak a\geq M^2/\rho_*^2.
\]

The next M1 campaign should not re-run coarse Möbius inversion or invoke
a generic prime-field trace bound. It should classify the exact remaining
bad-prime, nonunit-\(K\), and full \(2\)-adic masked periods as complete
physical fibres and test whether their combined edge degree is
target-safe. The aperiodic actual-symbol tensor should remain separate.
The normalization constraints are fixed: completed local descent is
\(p^{2j}\), Fejer mass remains \(D\), and the physical rows already
contain \(M^{-2}\).

No conductor range or global exponent changes. M2 remains frozen at the
complete \(\chi_4(h)\chi_4(s)\) cross-row density--discrepancy energy.
