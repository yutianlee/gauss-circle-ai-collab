# Round 197 common-cell power/operator/scope seam review

- Campaign: `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Role: independent hostile seam review
- Starting graph SHA-256:
  `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`
- Reviewed candidate SHA-256:
  `28c572898eb4c7950024342dfb931cc1c1ee49b8815ab54af2bc7a60f7bf9e8f`
- Numerical theorem evidence: none

## 1. Result

**PASS, at exactly the stated common-cell scope.**  The formal candidate's
two estimates

\[
 \mathscr R_{\mathrm{core,out}}^\sigma(P_{\rm cc}W)
 \ll L^2X^\varepsilon,
 \qquad
 \mathscr R_{\mathrm{open,out}}^\sigma(P_{\rm cc}W)
 \ll L^2X^\varepsilon
\]

are genuinely proved from the accepted interfaces.  The proof does not
need a sharp-face collar estimate.  It uses the exact lower two-cycle on
the symmetric common-cell mask, the complete physical count

\[
 O_\varepsilon(D_LL^2X^\varepsilon),
\]

and either the actual smooth gain (D_L/L) or the normalized-BV
telescoping charge.  Both ledgers end at

\[
 D_L^2L X^\varepsilon\ll L^2X^\varepsilon.
\]

The monotone and low-height orbit exits are removed by the accepted
Round-185 absolute estimate.  The Round-187--Round-192 projectors are
then rerun on the physically masked source using the accepted
Round-193/Round-195 deletion-stable operator calculus.  Only after that
complete core estimate is established is the accepted Round-195 safe
packet union subtracted.  No packet predicate is inserted into the
orbit, and there is only one outer real part.

The proof stops exactly where the candidate says it stops.  The disjoint
complement

\[
 P_{\partial\mathrm{lit}}\ \dot\cup\ P_{s\mathrm f}
 \ \dot\cup\ P_{g\mathrm f}
\]

is not proved target-safe.  An aligned sharp ratio face can be crossed by
all close lower pairs, so no automatic (O(D_L^2)) face-collar estimate
is available.  Its (D_LL^2X^\varepsilon) ledger is an upper capacity,
not literal lower mass.

This conclusion is consistent with the earlier hostile report's
no-immediate-mutation recommendation.  That recommendation rejected a
whole-(P_0) or whole-four-corner promotion before a formally isolated
common-cell theorem and independent seam review existed.  The present
review validates only the subsequently formalized (P_{\rm cc})
subsector.

## 2. Exact statement and hypotheses

Fix real (X\ge2), one nonempty literal middle or lower hard-M1 shell
(L\ge2), (sigma\in\{+1,-1\}), fixed (B>0),

\[
 H_B=\lfloor(\log(2X))^B\rfloor,
 \quad R_0=\lceil L\rceil,
 \quad D_L=\lceil\sqrt L\rceil.
\]

Use the accepted total zero-extended physical coefficient

\[
 \lambda_{N,\sigma}(d)=\mu^2(N)\rho_N(d)
 a_{L,X}^{\mathrm{lit},\sigma}(N/d,d),
 \qquad |\lambda_{N,\sigma}(d)|\ll_\varepsilon X^\varepsilon
\]

on its literal support, and open the complete even-shift source as

\[
 N=dm,\qquad N+r=d'm',\qquad 0<r<R_0,\quad 2\mid r.
\]

Put (g=(d,d')), (d=g\alpha), (d'=g\beta), and impose

\[
 P_2=\mathbf1_{|d-gm|\le D_L}
     \mathbf1_{|d'-gm'|>D_L},
\]

\[
 P_0=P_2\mathbf1_{(m,\beta)=1}
          \mathbf1_{\chi_4(\alpha m)=-1}.
\]

Let (C_{\rm lit}) assert equality of the **complete** sharp literal
codes at ((m,g\alpha)) and ((\alpha,gm)), including the exact literal
cell and every support, branch, trace, half-weight, and zero-extension
state.  Define

\[
 P_{\rm cc}=P_0C_{\rm lit}.
\]

The following accepted hypotheses are essential.

1. On one common live cell the exact lower symbol is a fixed finite
   product of bounded sharp factors, normalized one-dimensional BV
   factors, and uniformly scale-normalized (C^1) factors.  For a
   smooth factor the two lower inputs differ by (O(D_L)), so its
   change is (O_\varepsilon(D_L/L\,X^\varepsilon)).  Each BV factor
   has (O(1)) normalized total variation.
2. The residual-selector truth table is ((1,0,0,1)).  Under the lower
   swap the selector can change only when exactly one selected prime
   divides bounded (g); the accepted logarithmic-gap argument excludes
   that event for all sufficiently large (L), and the bounded
   remaining shells are paid absolutely.
3. The lower close relation and strict hard cone make (g) range over a
   fixed finite set.  The physical primitive charts are multiplicity
   one.
4. Pairing is performed before height, orientation, Fourier, anchor,
   Farey, or packet decomposition.  The complete outer aggregation
   retains both opposing orientations, all high blocks, both frequency
   signs, all anchors, and one outer real part.
5. Round 185 supplies the absolute target bound for the monotone sector
   and both opposing sectors with (h\le H_B).  Rounds 193 and 195
   supply the exact coordinatewise masked-operator passage and the
   deletion-stable safe projectors.  Round 195 also supplies the exact
   safe/open packet partition.

Under precisely these hypotheses the candidate proves (197.C10) and
(197.C12).  It makes no assertion that (P_{\rm cc}) is nonempty or has
positive coefficient mass.

## 3. Proof and hostile derivation

### 3.1 Orbit closure and the actual coefficient difference

On (P_0), the lower allocation map is

\[
 \tau_0(g\alpha,m,g\beta,m')=(gm,\alpha,g\beta,m').
\]

Its image gcd is

\[
 (gm,g\beta)=g(m,\beta)=g,
\]

and the reverse cross condition is ((\alpha,\beta)=1).  It preserves
both endpoint products, (r), the Fejer scalar, the radical phase, and
both physical defects.  The condition
(chi_4(\alpha m)=-1) reverses the character.  It also excludes a
fixed point: if (\alpha=m), then (alpha m) is an odd square and its
character is (+1).

The (P_2), gcd, and sign conditions are invariant under the two-cycle.
Equality of the two complete sharp codes is symmetric, so (P_{\rm cc})
is also invariant.  Since the original endpoint is live, code equality
forces the swapped endpoint to have the same live sharp state; ambient
zero extension is still retained.  After the separately audited
selector agreement, one orbit contributes the exact actual-coefficient
factor

\[
 \chi_4(g\beta)\chi_4(g\alpha)\Phi_{r,\sigma}(N)
 \lambda_{N+r,\sigma}(g\beta)
 \overline{\lambda_{N,\sigma}(g\alpha)
           -\lambda_{N,\sigma}(gm)}.
\]

There is no arbitrary coefficient replacement and no missing-corner
convention in this identity.

### 3.2 Complete physical outer count

The close relation is

\[
 g|\alpha-m|=|d-gm|\le D_L.
\]

Together with (d/m\in(4,16)) on live support, it bounds (g=O(1))
uniformly in (L,X).  In either accepted primitive chart, after fixing
((\kappa,g,U,v)), the close defect gives (O(D_L)) choices for the
moving lower variable.  The constraint (0<h<R_0/(2\kappa g)) then
places the other displacement in an interval of length (O(1)), because
(kappa U,\kappa v\asymp L).  Both (U) and (v) have
(O(1+L/\kappa)) choices.  Hence, including both orientations only in
the implied constant,

\[
 \mathcal C_\kappa
 \ll D_L(1+L/\kappa)^2.
\]

Summing over the full canonical range gives

\[
\begin{aligned}
 \sum_{\kappa\ll L}\mathcal C_\kappa
 &\ll D_L\sum_{\kappa\ll L}
       \left(1+{2L\over\kappa}+{L^2\over\kappa^2}\right)\\
 &\ll D_L\{L+L\log(2L)+L^2\}
 \ll D_LL^2X^\varepsilon.
\end{aligned}
\]

There is no height-block factor: (h) is determined by the physical
variables and the count covers the whole Fejer range.  Equivalently,
there are (O(LD_L)) possible lower close pairs, and for a fixed lower
pair

\[
 \sum_{0<r<R_0}\tau(N+r)\ll_\varepsilon LX^\varepsilon
\]

counts every upper factorization.  This second count confirms the same
(D_LL^2X^\varepsilon) ledger without using a post-spectral row norm.

### 3.3 Smooth and normalized-BV powers

On a common live cell, write one moving-factor term as

\[
 a(u,v)=K_{\rm sharp}\eta_L(u)b^{\rm sm}(u,v).
\]

The same (K_{\rm sharp}) occurs at both inputs.  The product rule
separates the (C^1) and BV changes.  The smooth change obeys

\[
 |b^{\rm sm}(m,g\alpha)-b^{\rm sm}(\alpha,gm)|
 \ll_\varepsilon {D_L\over L}X^\varepsilon.
\]

Multiplying this by the complete raw count gives

\[
 {D_L\over L}\,D_LL^2X^\varepsilon
 =D_L^2LX^\varepsilon
 \le4L^2X^\varepsilon.
\]

No pointwise derivative is assigned to (eta_L).  If
(Delta\eta(j)=\eta(j+1)-\eta(j)), then every ordered pair
((a,b)) with (|a-b|\le D_L) is opened into the crossed increments.
A fixed increment is crossed by (O(D_L^2)) such ordered pairs, so

\[
 \sum_{|a-b|\le D_L}|\eta(a)-\eta(b)|
 \ll D_L^2\sum_j|\Delta\eta(j)|
 \ll D_L^2.
\]

For each lower pair there are (O(LX^\varepsilon)) upper completions.
The BV contribution is consequently

\[
 D_L^2L X^\varepsilon\ll L^2X^\varepsilon.
\]

A fixed finite product of moving factors produces only finitely many
such terms.  Divisor, dyadic-block, (H_B), and logarithmic losses are
absorbed by fresh epsilon allocation; no positive power of (L) is
hidden there.  The selector exception occurs only on bounded (L) and
is paid by the same absolute physical count.

Crucially, this proof never assigns an (O(D_L^2)) collar to a sharp
literal face.  Every sharp factor is equal on (P_{\rm cc}); all sharp
code disagreements lie in (P_{\partial\mathrm{lit}}).

### 3.4 Monotone and low-height exits

The lower swap may change the opposing orientation, canonical height,
dyadic block, or packet coordinates.  Pairing therefore cannot be done
inside any one such component.  It is done on the complete physical
even-shift aggregate.

For a two-cycle with both atoms in the high opposing union, the two
terms give the commutator above.  If exactly one atom is in that union,
its partner is either monotone or opposing with (h\le H_B).  The
desired high term equals the paired commutator minus this exit term.
The paired differences are counted by the high-side physical count in
Section 3.2, with at most constant orbit multiplicity.  The exit partners
form a coordinatewise deletion of the absolute sector in (K185.7), so
their total is (O_{B,\varepsilon}(L^2X^\varepsilon)).  If the image is
still high opposing but in another orientation or block, it remains in
the complete outer union.  Common-code equality rules out a literal
support exit on (P_{\rm cc}).

This proves the complete high physical estimate.  It does not price an
orientation separately and it introduces no extra (Y), (h), or
orbit-boundary multiplicity.

### 3.5 Round-187--Round-192 masked passage

The mask (P_{\rm cc}) is a coordinatewise physical predicate and is
independent of every Fourier mode.  It is imposed before expansion and
height differencing.  At a transported affine site the exact identity is

\[
 M_hB_h-\chi M_-^{\rm tr}B_-^{\rm tr}
 =M_h(B_h-\chi B_-^{\rm tr})
  +\chi(M_h-M_-^{\rm tr})B_-^{\rm tr}.
\]

Thus an interior mask jump is retained in the recomputed remainder;
births, deaths, unequal translations, carries, phases, crossings, and
zero extensions are not discarded.  The Round-193 proof shows that the
Round-187--Round-192 safe projectors use exact linear return followed by
positive atom/row counts, Fourier (ell^1) mass, residue sparsity, or a
row indicator.  The Round-195 replay applies the same calculus to the
(P_2) source.  Since (P_{\rm cc}\subset P_2), adding the common-cell
deletion cannot increase any of those positive estimates.

Consequently the recomputed safe union on (P_{\rm cc}W) is
(O(L^2X^\varepsilon)).  Subtracting it through the exact linear source
identity from the physical bound of Section 3.4 proves (197.C10).  This
retains the (T=0) convention, all simultaneous strict (T\ge1) Farey
conditions, full anchors, both orientations and frequency signs, and all
literal fields.  Summing the logarithmically many high blocks is absorbed
by fresh epsilon allocation.

### 3.6 Round-195 safe/open subtraction and the real part

Round 195 partitions the recomputed (P_2) core into the disjoint safe
packet union

\[
 \kappa\ge D_L
 \quad\text{or}\quad
 \bigl(\kappa<D_L,
       \min(Y,D_L)\le H_B\mathfrak m\kappa\bigr)
\]

and the exact open packets

\[
 \kappa<D_L,qquad
 \min(Y,D_L)>H_B\mathfrak m\kappa.
\]

Its fixed-packet and fixed-to-outer estimates are positive and stable
under the additional physical deletion (P_{\rm cc}).  Hence the safe
packet subaggregate of the already recomputed masked core remains
(O(L^2X^\varepsilon)).  Linearity gives exactly

\[
 \mathscr R_{\rm open,out}^\sigma(P_{\rm cc}W)
 =\mathscr R_{\rm core,out}^\sigma(P_{\rm cc}W)
  -\mathscr R_{\rm cap,out}^\sigma(P_{\rm cc}W),
\]

which proves (197.C12).  The possibly noninvariant packet variables are
introduced only here, after physical pairing and masked-core passage.

Throughout, the complete complex sums over anchors, signs, orientations,
blocks, and packets are restored before the single accepted outer real
part.  Taking the absolute value of the complete paired commutator and
of already accepted absolute exit/safe terms is legitimate and does not
replace the claimant by separate orientation or frequency norms.

### 3.7 Exact complement and aligned-face quarantine

The successive binary tests give the exact disjoint truth table

\[
\begin{aligned}
 P_{g\mathrm f}&=P_2\mathbf1_{(m,\beta)>1},\\
 P_{s\mathrm f}&=P_2\mathbf1_{(m,\beta)=1}
                  \mathbf1_{\chi_4(\alpha m)\ne-1},\\
 P_{\partial\mathrm{lit}}&=P_0(1-C_{\rm lit}),
\end{aligned}
\]

and therefore

\[
 P_2=P_{\rm cc}\ \dot\cup\ P_{\partial\mathrm{lit}}
       \ \dot\cup\ P_{s\mathrm f}\ \dot\cup\ P_{g\mathrm f}.
\]

There is no missing parity case: (chi_4(\alpha m)\ne-1) includes every
tuple on which the odd character-reversing lower swap is unavailable.

The sharp-face exclusion is necessary.  At the two swapped lower inputs,
the ratios are (g\alpha/m) and (gm/\alpha), and for
(alpha\ne m),

\[
 \left({g\alpha\over m}-g\right)
 \left({gm\over\alpha}-g\right)
 =-{g^2(\alpha-m)^2\over\alpha m}<0.
\]

Thus a sharp face aligned with ratio (g) can be crossed by every
nontrivial close lower pair.  The (O(LD_L)) lower-pair capacity followed
by (O(LX^\varepsilon)) upper completions is then
(D_LL^2X^\varepsilon), not (D_L^2LX^\varepsilon).  The accepted
interfaces contain no literal-face transversality theorem uniform in
real (X).  The candidate correctly leaves this entire class in
(P_{\partial\mathrm{lit}}) and infers neither nonvanishing nor lower
mass from the capacity.

## 4. First doubtful or unproved step

There is no remaining doubtful step inside the stated (P_{\rm cc})
theorem once the named accepted coefficient and operator interfaces are
used.  A necessary definitional seam is that “literal cell” in the sharp
code means the exact cell, not merely a branch label that may recur on
disconnected pieces.  The formal candidate states the exact literal
cell and every discontinuous state, so this seam is closed.  Replacing
that code by a coarser profile label would invalidate the (C^1) step.

The first unproved step beyond the theorem is an estimate for

\[
 P_{\partial\mathrm{lit}}\ \dot\cup\ P_{s\mathrm f}
 \ \dot\cup\ P_{g\mathrm f}
\]

inside the Round-195 open packet region.  Already on
(P_{\partial\mathrm{lit}}), the aligned-face calculation shows that a
universal (O(D_L^2)) collar assertion is false without an exhaustive
face-by-face transversality or continuity theorem uniform in real (X).
No such theorem is present.  The sign-failure and cross-gcd-failure
pieces also lack the character-reversing two-cycle.  These are exact
open sectors, not defects in the common-cell proof.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Complete (kappa)-sum | **PASS.** (D_L\sum_{\kappa\ll L}(1+L/\kappa)^2\ll D_LL^2X^\varepsilon); no extra (Y), row, orientation, or frequency factor occurs. |
| Independent lower-pair/upper-completion count | **PASS.** (O(LD_L)) lower pairs times (O(LX^\varepsilon)) upper completions reproduces the same raw capacity. |
| Actual (D_L/L) gain | **PASS on (P_{\rm cc}).** The same sharp multiplier occurs at both inputs, and only the accepted smooth factor receives a pointwise derivative. |
| Normalized BV | **PASS.** A fixed increment is crossed by (O(D_L^2)) ordered close pairs; multiplying by (O(LX^\varepsilon)) upper completions gives (D_L^2LX^\varepsilon). |
| Sharp collar | **NOT USED / correctly quarantined.** The aligned ratio-(g) test restores (D_LL^2X^\varepsilon) capacity and defeats an automatic collar claim. |
| Selector | **PASS.** Its only possible swap failure has exactly one selected prime in bounded (g); the accepted gap argument removes it for large (L), and bounded shells are absolute. |
| Monotone/low-height exits | **PASS.** Exit partners are one-to-one subsets of the absolute sector (K185.7); high-to-high images remain in the complete outer union. |
| Round-187--Round-192 passage | **PASS.** The physical mask is applied before expansion; the transported mask commutator and all births/deaths remain in the core, including both (T) branches. |
| Round-195 subtraction | **PASS.** Safe packet estimates are rerun after physical deletion, and the open packet is obtained by exact linear subtraction only after the core estimate. |
| One outer real part | **PASS.** No componentwise claimant is substituted; both orientations, frequency signs, blocks, anchors, and packets are restored first. |
| Exact complement | **PASS.** The gcd, sign, and common-code first-failure tests are disjoint and exhaustive on (P_2). |
| Capacity versus mass | **PASS.** Neither the candidate nor this review infers nonemptiness, coefficient nonvanishing, density, or literal lower mass. |

## 6. Dependencies and exact artifacts used

The review read the following artifacts completely.

1. `protocol.md`, SHA-256
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
2. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md`,
   SHA-256
   `28c572898eb4c7950024342dfb931cc1c1ee49b8815ab54af2bc7a60f7bf9e8f`.
3. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/conductor_round197_report_reconciliation.md`,
   SHA-256
   `dff0651c22b56bea4f34d2f65edacc930265fbc231afecc60805e49a2dba3b47`.
4. `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`,
   SHA-256
   `470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`.
5. `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md`,
   SHA-256
   `4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009`.
6. `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`,
   SHA-256
   `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160`.

For comparison with the earlier route warning, the review also used
`rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reports/four_corner_orbit_power_hostile_audit.md`,
SHA-256
`945966d4e4a0a6297af94420f78a05499111f9b41f924392239534b9fd30620c`.
That report is claimant evidence and not an accepted dependency.

No web source, external theorem, or diagnostic computation was used.

## 7. Recommended state effect

**Promote the narrowly stated common-cell result, subject to completion
of the campaign's other independent reviews and a mechanically valid
State Patch.**  More precisely:

1. accept one subordinate `proved_internal` node for (197.C1)--(197.C35),
   with (P_{\rm cc}) and the complete outer operator fixed exactly as in
   the candidate;
2. use it only as strict-sector evidence for the still-open hard-M1
   small-(t) owner;
3. remove its exact intersection from the Round-195 open packet region,
   leaving that region intersected with
   (P_{\partial\mathrm{lit}}\dot\cup P_{s\mathrm f}\dot\cup
   P_{g\mathrm f});
4. retain the aligned-face self-return and the forced (kappa=1)
   four-corner boundary as route-scoped obstructions; and
5. leave every parent, bridge, theorem, endpoint-uniformity claim, and
   exponent unchanged.

The round may still close under
`p2_four_corner_orbit_boundary_self_return_no_go`: that label truthfully
describes the full four-corner/full-(P_0) route, while the reviewed
(P_{\rm cc}) sublemma is a valid strict-sector gain.
