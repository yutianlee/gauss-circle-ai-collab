# 1. Result.

**No-go and conditional assembly lemma.**  In the frozen statement packet, the
canonical hard-top assumption alone does not imply the full M2 estimate.  It
closes only residual blocks belonging to the one physical hard top band.  The
residual set also contains smooth top-scale blocks and smooth unbalanced
blocks, and the packet supplies no implication from the canonical hard-top
sum to either kind of smooth block.

Relative to the accepted direct owners, the weakest class-by-class completion
requires precisely these two additional outside estimates:

* **(SB)** For every residual smooth balanced top-scale literal block, the
  already reduced, outside-absolute signed quarter packet satisfies
  \[
    \left|\sum_G G\mathscr P_G\right|
       \ll_\varepsilon L^{3/2}X^\varepsilon .
  \]
* **(SU)** For every residual smooth unbalanced literal block, with
  \(K=XL/D^2\) and \(M=LK\), every exact sign/quarter-shift version satisfies
  \[
    \mathcal T_{L,K}\ll_\varepsilon M^{3/4}X^\varepsilon .
  \]

Here “literal” means that the odd-frequency restriction, both quarter shifts,
\(\chi _4(h)\), the exact \(1/h\) taper, profiles, floors, stars, support
clipping, and both signs remain in place.  Assuming the canonical hard-top
theorem, (SB), and (SU), all uniformly in real \(X\) and in the physical
dyadic endpoints, every M2 block is
\(O_\varepsilon(X^{1/4+\varepsilon})\); one-count summation of the
logarithmically many blocks gives the full pointwise M2 estimate with the same
power after absorbing logarithms.  A single stronger alternative is the
smooth dual bound for *all* residual smooth blocks; it subsumes (SB) as an
assembly hypothesis but is not the weakest class-by-class completion because
the balanced class has already been reduced to (SB).

# 2. Exact statement and hypotheses.

Let \(X\) be real, put \(y=\lfloor\sqrt X\rfloor\), and use the frozen
physical denominator partition: the bottom remainder, the one hard top band
with cutoff \(d\le y\), and the smooth interior bands.  For every nonbottom
band use the actual height
\(H_D=\lfloor DX^{-1/4}\rfloor\) and the actual clipped dyadic odd-frequency
blocks \(1\le L\le H_D\).  Write \(D=X^\delta\), \(L=X^\ell\), with fixed
constant rescalings understood at the physical-band level.  The active set is
exactly
\[
 \Omega=\{(\delta,\ell):1/4\le\delta\le1/2,\
                  0\le\ell\le\delta-1/4\}.
\]

Give the following owner sets an explicit priority, solely to prevent double
counting:
\[
\begin{aligned}
 E_{\rm term}&=\{(\delta,\ell)\in\Omega:
                     \ell=\delta-1/4\},\\
 E_{2}&=\{(1/2,0)\},\\
 E_{\rm TTY}&=\{(\delta,\ell)\in\Omega:
                  178\ell+1638\delta\le463\}
                  \setminus(E_{\rm term}\cup E_2),\\
 \mathcal U&=\{(\delta,\ell)\in\Omega:
       0\le\ell<\delta-1/4,\ 178\ell+1638\delta>463\}
       \setminus\{(1/2,0)\}.
\end{aligned}
\]
Thus the main Fourier cells are the disjoint union of the terminal cells,
the second-derivative point, the remaining TTY cells, and \(\mathcal U\).
The endpoint labels are implemented on the actual clipped physical blocks;
the exponent notation does not merge a smooth band with the hard top band.

The hypotheses are exactly: the five accepted direct-owner statements in the
packet; the accepted smooth and hard transform/reduction statements and their
target-safe errors; the canonical hard-top estimate for every residual hard
literal block; and (SB) and (SU) above for their respective smooth residual
classes.  “Balanced top-scale” is the physical predicate in the accepted gcd
reduction (equivalently, \(K/L=X/D^2\) remains in its fixed balanced range),
not merely the exponent label \(\delta=1/2\).  Every residual smooth block not
in that physical balanced class is assigned to (SU).  The hypotheses are
uniform over the finitely many signs and quarter-shift legs and over all real
\(X\), including blocks clipped by \(y\) or by \(H_D\).

# 3. Proof or derivation.

The exact one-count physical packet table is as follows.  Rows are applied in
the displayed order within each component; the R5 residual is a separate
component from the main Vaaler polynomial.

| Physical piece | Exact cell predicate | Unique owner | Status |
|---|---|---|---|
| Bottom denominator remainder | \(d\ll X^{1/4}\), before Fourier expansion | Bottom | Accepted, \(O(X^{1/4})\) |
| Vaaler--Fejer residual in any nonbottom band, including hard top | Every exact product, jump, shifted leg, and cutoff piece | R5 | Accepted, \(O_\varepsilon(X^{1/4+\varepsilon})\) |
| Main literal frequency block, hard or smooth | \(E_{\rm term}\) (the actual clipped terminal block) | Two-shift terminal theorem | Accepted |
| Main literal frequency block, hard or smooth | \(E_2\), after the preceding row | Full second-derivative menu | Accepted |
| Main literal frequency block, hard or smooth | \(E_{\rm TTY}\), after the preceding rows | Audited TTY pair with normalized-BV profiles | Accepted |
| Main literal frequency block in the one hard top band | \((\delta,\ell)\in\mathcal U\) | Canonical hard-top theorem, together with its already owned diagonal, collars, Poisson modes, square rays, exact nonsquare centres, positive-safe blocks, boundary pieces, and errors | Conditional on the canonical theorem |
| Main literal block in a smooth balanced top-scale band | \((\delta,\ell)\in\mathcal U\) and the accepted balanced physical predicate | Accepted gcd reduction followed by (SB) | Conditional on (SB) |
| Main literal block in a smooth unbalanced band | \((\delta,\ell)\in\mathcal U\) and not balanced | Exact smooth transform followed by (SU) | Conditional on (SU) |
| Smooth transform support-crossing/stationary-phase error | The error attached to its unique clipped smooth block | Exact smooth Poisson/stationary-phase reduction | Accepted \(O_W(1)\) |
| Hard one-sided boundary and transform errors | The pieces attached to their unique hard block | Hard endpoint reduction | Accepted and target-safe |

For a smooth unbalanced cell the exact transform identity gives
\[
 \mathcal B^+_{L,W}
 =-\frac{e(1/8)}{2\pi}X^{1/4}M^{-3/4}\mathcal T_{L,K}
   +O_W(1).
\]
Applying (SU), separately to every literal sign and shifted version, makes
the main term \(O_\varepsilon(X^{1/4+\varepsilon})\), and the stated error is
target-safe.  This identity is a proved reduction; without (SU) it is not a
proved estimate.

For a smooth balanced residual cell, the accepted gcd decomposition says
that its remaining small-gcd contribution is reduced to the exact
outside-absolute signed quarter packet.  Applying (SB) closes that remaining
piece; all other pieces of the reduction are already owned.  The absolute
value is not moved through the \(G\)-sum.  Again, the gcd decomposition is a
proved reduction and (SB) is the unproved estimate needed after it.

For a hard residual cell, the canonical estimate
\[
 \sum_{A,D_{\rm ray},K_{\rm rec},G,R}
 |\mathfrak Q_{A,D_{\rm ray},K_{\rm rec},G,R}|
 \ll_\varepsilon L^2X^\varepsilon
\]
combines with the explicitly accepted hard pieces to yield
\(\mathcal T_{\rm end,L}\ll_\varepsilon L^{3/2}X^\varepsilon\), hence the
physical hard block target by the accepted endpoint reduction.  This
conclusion concerns only the one hard band.

The rows exhaust the bottom, the R5 component, and every main cell in
\(\Omega\).  Half-open dyadic ownership, with the last block clipped at the
actual integer height, assigns every admissible \((d,h)\) once; profiles may
overlap analytically but the frozen partition-of-unity decomposition, rather
than a second estimate, owns the corresponding literal summand once.  There
are only logarithmically many denominator and frequency blocks and finitely
many literal variants.  Invoke all estimates with a slightly smaller
epsilon and absorb the resulting logarithmic factor into \(X^\varepsilon\).

The canonical assumption alone leaves both smooth rows open.  This is not
just an empty-set objection.  An unbalanced residual test point is
\((\delta,\ell)=(1/3,0)\): it is strictly below the terminal line and
\(178\ell+1638\delta=546>463\).  A smooth physical band
\(D\asymp c\sqrt X\), distinct from the hard band, together with
\(L\asymp X^{1/8}\), lies with a fixed margin in the residual region for
large \(X\) and is balanced because \(K/L=X/D^2\asymp c^{-2}\).  Thus (SU)
and (SB) each owns a nonempty class that none of the accepted owners or the
canonical hard theorem covers.  This proves insufficiency within the frozen
dependency system and establishes the claimed class-by-class minimality.

# 4. First doubtful or unproved step.

After the canonical theorem has closed the residual cells of the one hard top
band, the first smooth top-scale residual cell is reduced to
\(\left|\sum_GG\mathscr P_G\right|\), but the bound (SB) is not proved in the
packet.  The first unjustified step would be to treat that reduction as if it
were the estimate \(\ll L^{3/2}X^\varepsilon\).  Independently, on leaving the
balanced range, the exact smooth transform does not prove (SU); it only shows
that (SU) would be sufficient.  No relation in the packet transfers the
canonical hard-top estimate to either smooth quantity.

# 5. Required control test and outcome.

1. **Active triangle and residual set — pass.**  The table uses the exact
   \(\Omega\), assigns the terminal line and the weak TTY half-plane before
   taking the strict complement, and removes exactly \((1/2,0)\) from
   \(\mathcal U\).  The test point \((1/3,0)\) confirms a genuine residual
   unbalanced cell.
2. **One hard band versus smooth top scale — pass.**  Physical band type is a
   separate table key.  A smooth \(D\asymp c\sqrt X\) cell is never sent to
   the canonical theorem merely because its exponent tends to \(1/2\).
3. **Bottom versus R5 — pass.**  They occupy separate rows and separate
   components: the bottom is owned before Fourier expansion; R5 owns only
   Vaaler--Fejer residual pieces.
4. **Quarter shifts and character — conditional pass.**  (SB), (SU), and the
   canonical hypothesis are required for every literal variant; neither a
   shift nor the exact \(\chi_4(h)\) is discarded or replaced by an unsigned
   model.
5. **Floors, profiles, hard cutoff, stars, and signs — conditional pass.**
   The table is indexed by the actual \(y\), \(H_D\), clipped blocks, and
   literal decorated sums.  The outside assumptions are not estimates for a
   smoothed surrogate.
6. **Support crossings and one-sided boundary — pass.**  Smooth crossings
   remain in their unique exact Poisson transform/error row; hard one-sided
   boundary terms remain with the accepted hard endpoint pieces.  Neither is
   silently put under (SB), (SU), or the canonical residual sum.
7. **One-count ownership — pass.**  Ordered owner sets resolve the possible
   terminal/TTY overlap, the TTY equality belongs to TTY, and strict
   inequalities define \(\mathcal U\).  Half-open physical bands and clipped
   frequency blocks prevent endpoint duplication.
8. **Real \(X\) and dyadic endpoints — conditional pass.**  No step replaces
   \(\lfloor\sqrt X\rfloor\) or \(\lfloor DX^{-1/4}\rfloor\) by an integer-free
   surrogate.  Full assembly follows only with the explicitly stated uniform
   real-\(X\), endpoint-clipped forms of the three open estimates.
9. **Reduction versus estimate — pass.**  The smooth transform, balanced gcd
   decomposition, and hard endpoint decomposition are labelled reductions;
   the canonical theorem, (SB), and (SU) are separately labelled estimates.
10. **Near-collision, fourth-moment, and average-to-pointwise routes — pass.**
    None is an assembly dependency.  They can only be alternative methods for
    proving one of the three open estimates.  In particular, an averaged
    statement cannot be substituted for the required pointwise, real-\(X\)
    hypotheses without a separate uniform implication, and no route may use
    the desired packet bound as one of its inputs.
11. **Downstream separation — pass.**  The conclusion is only the M2
    pointwise estimate.  It asserts neither M9-M1 nor M9 and infers no quarter
    target.
12. **Exponent ledger — pass.**  All three packet estimates remain
    conditional, so the global exponent ledger is unchanged.

The character-factor node is likewise not a separate dependency: the exact
\(\chi_4(h)\) is already part of each literal packet.  It would become a proof
sublemma only if a proposed proof of (SB), (SU), or the canonical theorem
needed it.  The same is true of near-collision and fourth-moment nodes.

# 6. Dependencies and exact artifacts used.

Only the following two authorized artifacts were read and used:

1. `rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/briefs/blind_m2_assembly_rederivation.md` — task scope, isolation rule, output path, and seven-section contract.
2. `rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/derivation_packet.md` — all mathematical statements, accepted owners, reductions, open estimates, and mandatory controls.

No proof graph, strategy file, prior or sibling report, legacy artifact, or web
source was read or used.

# 7. Recommended state effect.

**Promote only the conditional one-count assembly lemma and the no-go that the
canonical hard-top theorem alone is insufficient.**  Retain the canonical
hard-top estimate, (SB), and (SU) as open estimates; do not promote the full M2
estimate.  Reject any dependency edge that sends a smooth top-scale block to
the hard canonical theorem, or that treats the smooth transform or balanced
gcd reduction as a proved bound.  Make no change to M9-M1, M9, the quarter
target, or the global exponent ledger.
