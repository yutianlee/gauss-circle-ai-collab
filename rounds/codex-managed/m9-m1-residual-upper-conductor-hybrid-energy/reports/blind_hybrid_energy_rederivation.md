# 1. Result

**Packet-level hybrid-budget lemma and scoped no-go.**  For the actual
one-count rows (73.3), and without changing either their local units or their
transition weights, the exact energy diagonal is already within (73.8):

\[
 \mathcal E_{\rm diag}\ll_\varepsilon X^\varepsilon BC
 =X^\varepsilon\frac{C^2}{T}
 \leq X^\varepsilon\frac{J^2}{T}.
\]

The Farey-neighbor numerator label supplies no further orthogonality: it
labels disjoint one-count cells and does not occur in the exponential phase.
Moreover, even an optimistic square-root gain over the \(O(b)\) residue
classes followed by an optimistic square-root gain over the \(O(B)\) values
of \(b\) would improve the first-moment triangle bound by only
\((bB)^{1/2}\asymp B=C/T\).  It would give

\[
 \left|\sum_{b\asymp B}S_{b,k}^{(\kappa)}(C)\right|
 \ll_\varepsilon X^\varepsilon C Q^{-1/6}
 \qquad\text{(best-case mechanism budget)}.
\]

This is sufficient only for \(C\leq J^{14/15}\).  In the remaining top
slice it misses (73.10) by

\[
 H_1(C):=\frac{T\sqrt C}{JQ^{1/6}}>1,
 \qquad H_1(J)=J^{1/30}.
\]

Thus numerator orthogonality and separate square-root residue/\(b\)
orthogonality do not, by themselves, close all of (73.1).  The missing input
has to be a genuinely hybrid actual-unit curvature estimate.  The continuous
analytic phase is uniformly nondegenerate in the actual \(k=O(1)\),
\(b\asymp C/T\gg1\) range, but that fact alone is not an estimate for the
coupled inverse-unit lattice sum.  The odd exact unit also has an explicit
perfect-square resonance.  These conclusions are a scoped no-go
for the three elementary mechanisms, not a counterexample to (73.8) or
(73.10).

# 2. Exact statement and hypotheses

Assume exactly (73.1)--(73.7), including \(J=X^{1/2}\),
\(Q=J^{2/5}\), \(T=J^{3/5}\), \(B=C/T\), the actual admissible local units
\(u_{b,r,k}^{(\kappa)}\), the actual half-open one-count cells, and the symbol
bounds (73.4)--(73.5).  Fix one nonaxial compatible \(k=O(1)\), one
\(\kappa\in\{1/4,1/2,1\}\), one endpoint orientation, and one local parity
class.

The following assertions then hold.

1. Collapsing only the unique cell ownership, not altering any coefficient,
   writes the row as
   \[
     S_b=\sum_{c\in\mathscr C_b}a_b(c)e(\pm A_{\kappa,b}/c),
     \qquad |a_b(c)|\ll_\varepsilon X^\varepsilon,
     \qquad \#\mathscr C_b\ll C.
   \]
   Hence the exact diagonal is target-safe.  More generally, the portion of
   the energy expansion with \(|c_1-c_2|\leq H\) is bounded trivially by
   \[
     \ll_\varepsilon X^\varepsilon BC(H+1)
     =X^\varepsilon\frac{C^2(H+1)}T.
   \]
   Packet-level counting therefore makes only
   \(H+1\ll J^2/C^2\) automatically safe; at \(C=J\) this is merely a
   bounded-width band.

2. The post-(73.7) first-moment triangle bound is
   \[
     M_0(C)=X^\varepsilon\frac{C^2}{TQ^{1/6}}.
   \]
   Separate square-root residue and \(b\) gains have combined budget \(B\),
   so their residual ratio to (73.10) is exactly \(H_1(C)\) above.  The
   threshold \(H_1(C)=1\) is \(C=J^{14/15}\).

3. On the energy route, an optimistic square-root residue gain in amplitude
   gives at most a factor \(b\asymp B\) in energy and leads to
   \[
      \mathcal E_{r,\mathrm{budget}}
      =X^\varepsilon\frac{C^2}{Q^{1/3}}.
   \]
   Relative to (73.8), its remaining factor is
   \[
      H_E(C):=\frac{C^2T}{J^2Q^{1/3}}.
   \]
   It is sufficient only for \(C\leq J^{23/30}\), and
   \(H_E(J)=J^{7/15}\).  A square-root gain in the outer \(b\)-sum is not
   available merely from positivity of the energy sum; obtaining one would
   itself be a new second-moment/large-sieve theorem.

4. Put \(d=\kappa k>0\), \(\eta=\sqrt d/(bJ)\), and regard
   \(F(b,c)=A_{\kappa,b}/c\) as a continuous two-variable phase.  Its Hessian
   satisfies the exact identity
   \[
     \det D^2_{b,c}F
       =\frac{J^4(3\eta-1)(1+\eta)^3}{c^4}.
   \]
   In the frozen family \(k=O(1)\), while
   \(b\asymp C/T\gg J^{1/9}\), so \(\eta=O(J^{-10/9})=o(1)\) uniformly.  Hence
   \[
     \det D^2_{b,c}F=-\frac{J^4}{c^4}(1+o(1)),
     \qquad
     \partial_bA_{\kappa,b}=J^2(1+o(1)).
   \]
   The formal rank-drop locus \(\eta=1/3\) and the formal
   \(b\)-stationary locus \(\eta=1\) are both outside the actual Round-73
   parameter range.

5. In the odd class, if \(J\in\mathbb Z\), \(k=s^2\) with
   \(s\in\mathbb Z\), and \((4b,c)=1\), the exact phase in (73.12) combines
   to
   \[
      e_c(-k\overline{4b})
      e\!\left(-\frac{bJ^2+Js}{c}\right)
      =e_c\!\left(-(2bJ+s)^2\overline{4b}\right).
   \]
   It equals \(1\) whenever \(c\mid(2bJ+s)^2\).  This includes the
   perfect-fourth-power subfamily \(k=t^4\).  It does not by itself violate
   the desired bound, but it rigorously prevents treating the inverse unit
   as an independent random sign or asserting uniform nonresonance.

# 3. Proof or derivation

Half-open one-count ownership assigns each occurring denominator
\(c=r+4b\ell\) to a unique actual cell.  Relabeling that term gives
\(a_b(c)=u_{b,r,k}^{(\kappa)}w_{b,r,\nu,k}^{(\kappa)}(\ell)\); no weight or
unit is replaced.  Bounds (73.4)--(73.5) give the coefficient and counting
bounds in Section 2.  In the energy expansion, \(c_1=c_2\) therefore
contributes at most \(X^\varepsilon C\) for each \(b\), and there are
\(B\asymp C/T\) values of \(b\).  The same count with \(O(H+1)\) choices of
\(c_2\) for each \(c_1\) proves the stated near-diagonal bound.  Comparing it
with \(J^2/T\) gives \(H+1\ll J^2/C^2\).

Cauchy--Schwarz applied to (73.7) gives
\[
 \sqrt B\left(X^\varepsilon\frac{C^3}{TQ^{1/3}}\right)^{1/2}
 =X^\varepsilon\frac{C^2}{TQ^{1/6}}=M_0(C).
\]
There are \(O(b)\) residue classes and \(O(B)\) outer rows.  Granting, only
for a best-case mechanism budget, a square-root improvement in each gives
gain \(b^{1/2}B^{1/2}\asymp B=C/T\), hence \(M_0/B=CQ^{-1/6}\).  Division by
the right side of (73.10) gives
\[
 \frac{CQ^{-1/6}}{J\sqrt C/T}
 =\frac{T\sqrt C}{JQ^{1/6}}=H_1(C).
\]
Since \(T=J^{3/5}\) and \(Q^{1/6}=J^{1/15}\), the equality \(H_1=1\) is
\(C=J^{14/15}\), while \(H_1(J)=J^{1/30}\).  On the energy side, dividing
(73.7) by the optimistic residue energy gain \(B=C/T\) gives
\(C^2/Q^{1/3}\); comparison with \(J^2/T\) gives \(H_E\), its threshold
\(J^{23/30}\), and endpoint value \(J^{7/15}\).

For the curvature calculation,
\[
 A=bJ^2+2J\sqrt d+d/b,\quad
 A'=J^2-d/b^2=J^2(1-\eta^2),\quad
 A''=2d/b^3.
\]
As \(F=A/c\),
\[
 \det D^2F=\frac{2AA''-(A')^2}{c^4}.
\]
Substitution and factorization yield
\[
 2AA''-(A')^2
 =J^4(3\eta^4+8\eta^3+6\eta^2-1)
 =J^4(3\eta-1)(1+\eta)^3.
\]
Since \(C>J^{32/45}\) and \(T=J^{3/5}\), one has
\(b\asymp C/T\gg J^{1/9}\).  Together with \(k=O(1)\), this gives
\(\eta=O(J^{-10/9})=o(1)\), so the determinant is
\(-J^4c^{-4}(1+o(1))\) and \(A'=J^2(1+o(1))\) uniformly.  The two formal
degeneracy loci therefore do not occur in the actual family.

Finally, for the odd perfect-square specialization, (73.12) is an identity
of the actual inverse unit and analytic phase.  Because \(J,s\) are
integers, its two factors combine modulo \(c\), and
\[
 k+4b(bJ^2+Js)=s^2+4b^2J^2+4bJs=(2bJ+s)^2.
\]
Multiplication by \(\overline{4b}\pmod c\) proves the displayed resonance.
No adversarial or arbitrary coefficient choice enters any part of the
argument.

# 4. First doubtful or unproved step

The first unproved step is already the proposed square-root orthogonality:
the packet supplies no estimate that lets one multiply a residue
square-root gain by a \(b\)-square-root gain while retaining the coupled
inverse/even unit and all transition weights.  In the top slice
\(J^{14/15}<C\leq J\), even after granting that \(B\)-gain, the weakest
remaining sufficient input can be written as the genuinely joint bound
\[
 \left|\sum_{b\asymp B}S_{b,k}^{(\kappa)}(C)\right|
 \ll_\varepsilon
 X^\varepsilon\frac{CQ^{-1/6}}{H_1(C)}
 =X^\varepsilon\frac{J\sqrt C}{T}.
\]
Equivalently, it must produce total gain \(BH_1(C)\) over \(M_0(C)\), with
the extra factor \(J^{1/30}\) at \(C=J\).  A valid proof has to be one
actual-unit hybrid theorem, or a factorization with a proved seam; the
packet contains neither.  Here \(\eta=o(1)\), so analytic rank itself passes;
what remains absent is an estimate combining that valid curvature with the
exact unit and transition family.  The odd square resonance also rules out
a blanket random-residue-sign argument.

# 5. Required control test and outcome

- **Normalization:** Passed.  At \(C=J\), the first-moment deficit is
  \(J^{13/30}\), the two square-root budgets supply only
  \(B=Q=J^{12/30}\), and the exact residue is \(J^{1/30}\).  On the energy
  route the corresponding post-residue deficit is \(J^{7/15}\).
- **One-count geometry and Farey numerators:** Passed.  The numerator label
  partitions actual support; there is no numerator character in (73.3), so
  no numerator orthogonality is available.
- **Transitions:** Unresolved for closure.  Variation is controlled per
  cell only.  Applying completion separately to as many as
  \(QX^\varepsilon\) cells can cost \(Q\), so a full-progression estimate
  cannot simply be multiplied by the number of cells.  A hybrid theorem
  must retain the complete actual transition family before absolute values.
- **Diagonal and near diagonal:** Passed only in the quantified scope above.
  The diagonal is safe, and a band \(H+1\ll J^2/C^2\) is safe by counting.
  At the endpoint a wider band needs genuine cancellation.
- **Analytic rank and degeneracy:** Passed in the actual parameter range.
  Uniformly \(\eta=O(J^{-10/9})=o(1)\), so the Hessian determinant is
  \(-J^4c^{-4}(1+o(1))\) and the \(b\)-derivative of \(A\) is
  \(J^2(1+o(1))\).  The formal loci \(\eta=1/3\) and \(\eta=1\) are
  out of range.  This analytic audit alone does not control the exact
  inverse-unit lattice sum.
- **Exact inverse unit, perfect squares, and fourth powers:** Passed as a
  diagnostic, not as closure.  The exact odd identity gives the displayed
  square resonance.  Such terms must be isolated and counted; the packet
  provides no hypothesis allowing them to be discarded.  Fourth powers are
  a contained subcase.
- **Parity, orientation, axes, and gcds:** Unresolved for closure.  Formula
  (73.12) covers only the odd class.  No sign change proves the even classes,
  and the two axes remain separate nonstationary rows.  Every use of an
  inverse or completion must retain the admissible gcd condition; no
  unrestricted residue completion was used here.
- **Finite dual/error sums:** The derivation is for one fixed compatible
  nonaxial \(k\), one \(\kappa\), one parity class, and one orientation.  It
  supplies no summation over \(k\), no even/axis estimate, and no error-sum
  closure.
- **Self-return:** Passed.  No \(c\)-Poisson/\(B\)-process cycle was invoked.
  Repeating that forbidden cycle would not supply \(H_1(C)\).
- **Source hypotheses and downstream scope:** Passed.  No external theorem
  or source was invoked.  The result concerns only the fixed smooth-interior
  residual conductor block (73.1), and implies no cone-edge, other-sector,
  or global \(M9\!-\!M1\) exponent.

# 6. Dependencies and exact artifacts/sources used

**Isolation ledger.**  I read exactly these two substantive artifacts:

1. `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/briefs/blind_hybrid_energy_rederivation.md`;
2. `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/derivation_packet.md`.

I did not read state files, the proof graph or proof draft, prior or sibling
reports, claimant material, source cards, web pages, or any other repository
artifact.  An initial read attempt at
`briefs/derivation_packet.md` returned only a path-not-found error and no
artifact content.  I made a path-existence check only for this assigned
output and did not read any report.  No web search, external source,
numerical experiment, or computer-algebra computation was used.  During the
formatting audit, the coordinator supplied the frozen-scope fact \(k=O(1)\);
no additional repository artifact was read.  All dependencies are the
definitions, identities, and bounds frozen in the two listed artifacts plus
that coordinator-supplied scope correction.

# 7. Recommended state effect

**Retain.**  Keep (73.8) and (73.10) open for the upper residual range.  The
safe diagonal, the exact \(J^{1/30}\) endpoint hybrid deficit after the
optimistic two-level square-root budget, the actual-domain nondegenerate
Hessian audit, and the odd perfect-square resonance may be retained as
scoped diagnostics,
but they do not promote the residual energy or first-moment claim.  Make no
change to shared proof state from this report.
