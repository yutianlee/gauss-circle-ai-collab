# Round 114 hostile audit: mean square, radial corridor, and determinant ray

Campaign: `m9-m2-balanced-literal-energy-connector-fork`
Task: `mean_square_ray_hostile_audit`
Role: barrier/no-go
Graph SHA-256 read: `de0981e570e4a5f306abed5d16fa2fc34914160f27bf5621df78f927d8cfa9c9`

## 1. Result: literal connector lemma and double-far no-go

There is a valid fixed-block connector from the proposed **full-symbol**
diagonal-critical mean square to the Round-113 balanced packet.  It is
simpler than the gcd-masked Gram in the conductor candidate.  If

\[
 \mathfrak M_h^{\rm full}(B)
 :=\sum_{h\asymp L,\ h\ {\rm odd}}
 \left|\sum_{k\asymp K}A_B(h,k)e(R\sqrt{hk})\right|^2
 \ll_\varepsilon L^{1/2}K^{3/2}X^\varepsilon,
 \tag{114.H1}
\]

then Cauchy gives the full smooth sum at scale \((LK)^{3/4}\).  Subtracting
the already owned high-gcd part then gives

\[
 |Z_B(R)|\ll_\varepsilon L^{3/2}X^\varepsilon
 \qquad (1\le K/L\le16).
 \tag{114.H2}
\]

Thus Gate 0 passes for one literal balanced block.  The analytic estimate
(114.H1) remains completely unproved, is stronger than the scalar packet
target, and erases \(\chi _4(h)\) at the final Cauchy step.  The existing
mean-square node still does **not** imply all of `M9-M2`: the hard TOP
parent is independent.

The exact direct energy admits two target-safe absolute corridors.  With

\[
 \Delta=h'k'-hk,\qquad \rho=hk'-h'k,
 \tag{114.H3}
\]

both \(|\Delta|\le L\) and \(|\rho|\le L\) cost
\(O_\varepsilon(L^3X^\varepsilon)\).  The first is the full-product radial
corridor; the second is the determinant/rational-ray corridor proposed by
the conductor.  Their union may lawfully be removed from the energy.

This does not prove a broad estimate.  On the double-far survivor
\(|\Delta|>L\), \(|\rho|>L\), the phase depends on the two full products,
not on \(\rho\) inside a fixed product fibre.  The exact identities

\[
 \Delta+\rho=(k'-k)(h+h'),\qquad
 \Delta-\rho=(h'-h)(k+k')
 \tag{114.H4}
\]

give divisor-bounded generic multiplicity for a *fixed* \((\Delta,\rho)\),
but the invariant pair itself has full \(L^4\) range.  A phase-conjugating
bounded coefficient array makes the double-far energy \(\asymp L^4\).
Hence support geometry, radial separation, and determinant transversality
alone cannot prove the needed \(L^3\) energy bound.  The smallest surviving
analytic target is the actual \(\chi _4\)-weighted, gcd-truncated,
double-far shifted-divisor correlation written in (114.H18) below.  It is a
precise survivor, but at present it is another form of the original signed
core rather than a strict saving.

## 2. Exact statement and hypotheses

Let \(X\ge4096\) be real, \(R=\sqrt X\), and let \(B\) be one fixed
Round-113 full smooth balanced positive-frequency block.  Put

\[
 D=\frac{\lfloor R\rfloor}{2},\qquad
 G_0=\frac{\sqrt L}{2},\qquad
 K=\frac{XL}{D^2},\qquad 1\le K/L\le16.
\]

The persistent case is \(j=1\); the exact-square \(j=2\), \(K/L=16\)
case is only a boundary control.  Let \(A_B\) be the real Round-113 symbol,
supported in a fixed-comparability region \(h\asymp L\), \(k\asymp K\),
with \(|A_B|\ll1\), and define

\[
 a_B^<(h,k)=\chi _4(h)
 \eta\!\left(\frac{\gcd(h,k)}{G_0}\right)A_B(h,k).
 \tag{114.H5}
\]

Write

\[
 \begin{aligned}
 \mathcal T_B&=\sum_{h,k}\chi _4(h)A_B(h,k)e(R\sqrt{hk}),\\
 \mathcal T_B^{\rm low}&=\sum_{h,k}a_B^<(h,k)e(R\sqrt{hk}),\\
 \mathcal T_B^{\rm hi}&=\mathcal T_B-\mathcal T_B^{\rm low}.
 \end{aligned}
 \tag{114.H6}
\]

The accepted owner estimate is

\[
 |\mathcal T_B^{\rm hi}|\ll_\varepsilon L^{3/2}X^\varepsilon,
 \tag{114.H7}
\]

and the accepted coefficientwise packet identity is

\[
 Z_B(R)=\sum_\sigma G_\sigma Q_{B,\sigma}^{\rm full}(R)
       =2i\mathcal T_B^{\rm low}.
 \tag{114.H8}
\]

Under these hypotheses the following statements hold.

1. The exact direct energy is
   \[
   |\mathcal T_B^{\rm low}|^2
   =\sum_{h,k,h',k'}a_B^<(h,k)\overline{a_B^<(h',k')}
    e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right).
   \tag{114.H9}
   \]
   In primitive coordinates its full-product diagonal is
   \(g^2uv=g'^2u'v'\), not \(uv=u'v'\).

2. For
   \[
   c_B(n)=\sum_{hk=n}a_B^<(h,k),
   \tag{114.H10}
   \]
   the equal-full-product contribution satisfies
   \[
   E_0=\sum_n|c_B(n)|^2\ll_\varepsilon L^2X^\varepsilon.
   \tag{114.H11}
   \]

3. Uniformly for \(0\le U,Q\ll L^2\), the atomwise absolute masses obey
   \[
   E_{\rm rad}(U)
   :=\sum_{|h'k'-hk|\le U}|a_B^<(h,k)a_B^<(h',k')|
   \ll_\varepsilon L^2(U+1)X^\varepsilon,
   \tag{114.H12}
   \]
   \[
   E_{\rm det}(Q)
   :=\sum_{|hk'-h'k|\le Q}|a_B^<(h,k)a_B^<(h',k')|
   \ll_\varepsilon L^2(Q+1)X^\varepsilon.
   \tag{114.H13}
   \]
   Hence \(U=Q=L\) is target-safe at the squared budget \(L^3\).

4. The full-symbol mean-square hypothesis (114.H1) implies (114.H2).
   A character-preserving alternative is
   \[
   \mathfrak M_k^{\rm full}(B)
   :=\sum_{k\asymp K}
   \left|\sum_{h\asymp L}\chi _4(h)A_B(h,k)e(R\sqrt{hk})\right|^2
   \ll_\varepsilon L^{3/2}K^{1/2}X^\varepsilon,
   \tag{114.H14}
   \]
   which also implies (114.H2).  At \(K\asymp L\), both right sides are
   \(L^2X^\varepsilon\).  Neither mean square is equivalent to the direct
   scalar target.

5. The exact determinant identity is, for \(p=h'-h\), \(q=k'-k\),
   \(\rho=hq-kp\),
   \[
   \sqrt{h'k'}-\sqrt{hk}
   -\frac12\sqrt{\frac kh}\,p
   -\frac12\sqrt{\frac hk}\,q
   =-\frac{\rho^2}
   {4(hk)^{3/2}(P+\sqrt{Q_0})},
   \tag{114.H15}
   \]
   where
   \(P=1+\tfrac12(p/h+q/k)\) and
   \(Q_0=(1+p/h)(1+q/k)>0\).  This is a valid literal rank-one identity,
   but by itself it is not a broad cancellation estimate.

## 3. Proof or derivation

The map

\[
 (h,k)\longleftrightarrow
 (g,u,v)=\bigl(\gcd(h,k),h/g,k/g\bigr)
\]

is bijective and retains the lift.  Complete multiplicativity gives
\(\chi _4(g)\chi _4(u)=\chi _4(h)\), including the zero value on even
integers, while \(Rg\sqrt{uv}=R\sqrt{hk}\).  Moreover

\[
 e(g/4)-e(3g/4)=2i\chi _4(g).
\]

Thus the two quarter shifts, the factor \(2i\), the character, and the
complete internal gcd-shell sum collapse coefficientwise to (114.H8), not
shellwise by absolute values.  Squaring gives (114.H9) with both lift
variables present.

Grouping (114.H9) by \(n=hk\) proves

\[
 \mathcal T_B^{\rm low}=\sum_n c_B(n)e(R\sqrt n).
 \tag{114.H16}
\]

There are \(O(L^2)\) possible products and at most \(d(n)\) factor pairs
in each fibre.  Since \(|a_B^<|\ll1\) and
\(d(n)\ll_\varepsilon X^\varepsilon\), (114.H11) follows.  This is the
whole equal-product fibre, not merely the atom diagonal.

For the radial corridor, (114.H16) and the same divisor bound give

\[
 \begin{aligned}
 E_{\rm rad}(U)
 &\le \sum_{n\asymp L^2}d(n)
       \sum_{|r|\le U}d(n+r)\\
 &\ll_\varepsilon L^2(U+1)X^\varepsilon,
 \end{aligned}
\]

which proves (114.H12), including the full-product diagonal.

For the determinant corridor fix nonzero \(\rho\) and a base point
\((h,k)\), and put \(d=\gcd(h,k)\).  The equation

\[
 hk'-h'k=\rho
\]

has no solution unless \(d\mid\rho\).  If it has one, all solutions are

\[
 (h',k')=(h'_0,k'_0)+t(h/d,k/d).
\]

In fixed comparable boxes this gives \(O(1+d)\) possible integers \(t\).
There are \(O(L^2/d^2)\) base points of gcd \(d\), so the number for fixed
nonzero \(\rho\) is

\[
 \ll L^2\sum_{d\mid\rho}(d^{-2}+d^{-1})
 \ll_\varepsilon L^2X^\varepsilon.
\]

For \(\rho=0\), summing over all \(d\) gives \(O(L^2\log L)\).  Summation
over \(|\rho|\le Q\) proves (114.H13).  The slanted literal support is a
subset of the comparable boxes, so it cannot increase this count.

For the mean-square connector, write

\[
 S_h=\sum_kA_B(h,k)e(R\sqrt{hk}).
\]

Then

\[
 |\mathcal T_B|^2
 =\left|\sum_h\chi _4(h)S_h\right|^2
 \ll L\sum_{h\ {\rm odd}}|S_h|^2
 =L\mathfrak M_h^{\rm full}(B).
\]

Under (114.H1),

\[
 |\mathcal T_B|
 \ll_\varepsilon L^{3/4}K^{3/4}X^\varepsilon
 \ll L^{3/2}X^\varepsilon.
\]

Equations (114.H6)--(114.H8) and the high-gcd owner (114.H7) now prove
(114.H2).  This connector uses the original full smooth symbol \(A_B\).
The conductor candidate's displayed mean squares with the arithmetic mask
\(\eta(\gcd(h,k)/G_0)\) are also sufficient by Cauchy, but they are
different, stronger local statements and are not literally the old
full-symbol mean-square node.  Cauchy in \(k\) proves the analogous claim
from (114.H14).

To verify (114.H15), note that

\[
 P^2-Q_0=\frac14\left(\frac ph-\frac qk\right)^2
          =\frac{\rho^2}{4h^2k^2}
\]

and rationalize \(\sqrt{Q_0}-P\).  The additional identities (114.H4)
follow by direct expansion.  Equivalently, if
\(H=h+h'\), \(K_+=k+k'\), then

\[
 \Delta+\rho=qH,\qquad \Delta-\rho=pK_+.
 \tag{114.H17}
\]

For generic fixed \((\Delta,\rho)\), (114.H17) gives at most
\(d(|\Delta+\rho|)d(|\Delta-\rho|)\) choices, up to parity and support
conditions.  When \(\Delta=\pm\rho\), one increment vanishes and the
fixed-invariant multiplicity can be \(O(LX^\varepsilon)\).  Neither fact is
a global saving: the possible invariant pairs occupy full two-dimensional
range and the sum over them reconstructs \(\asymp L^4\) atom pairs.

After removing the union of the two target-safe corridors, the exact
survivor is

\[
 \boxed{
 \mathcal E_{\rm df}
 =\sum_{|r|>L}\ \sum_n
 e\!\left(R(\sqrt n-\sqrt{n+r})\right)
 \!\!\sum_{\substack{hk=n,\ h'k'=n+r\\
                      |hk'-h'k|>L}}
 a_B^<(h,k)\overline{a_B^<(h',k')} .}
 \tag{114.H18}
\]

The required remaining assertion is
\(|\mathcal E_{\rm df}|\ll_\varepsilon L^3X^\varepsilon\).  For fixed
\((n,r)\), every determinant fibre in the inner sum has the same outer
phase.  Therefore large \(|\rho|\) supplies no phase oscillation inside
that fibre; it only reorganizes the actual signed divisor correlation.

Finally, the coefficient-uniform broad analogue is false.  On a comparable
rectangle containing \(\asymp L^2\) allowed odd, low-gcd atoms, choose

\[
 b(h,k)=e(-R\sqrt{hk}).
\]

Every term in its squared energy equals one.  The radial-near and
determinant-near sets contain only \(O(L^3\log^C L)\) pairs, whereas the
whole rectangle has \(\asymp L^4\) ordered pairs.  Its double-far energy is
therefore \(\asymp L^4\), not \(O(L^3X^\varepsilon)\).  This falsifies only
the arbitrary bounded-coefficient theorem.  It is not a lower bound for
the fixed real Vaaler symbol.

## 4. First doubtful or unproved step

The first genuinely unproved actual-symbol step is (114.H18).  The two
corridor estimates remove target-sized pieces but leave a survivor of full
coefficient-blind capacity.  Neither the tangent-remainder identity nor
the two identities (114.H4) furnish a pointwise inequality at fixed real
\(R\).  At the critical relation \(R\asymp L^3\), the fact that the
transverse phase remainder is numerically large is not a modulo-one
separation theorem.

Equivalently, on the mean-square route the first unproved step is the
actual full-symbol inequality (114.H1), or the character-preserving
alternative (114.H14).  The row diagonal
\(\sum_{h,k}|A_B(h,k)|^2\asymp LK\asymp L^2\) is already at the proposed
mean-square scale, so there is no polynomial loss available.  A proof must
control the off-diagonal using a property of the fixed symbol.  The first
invalid shortcut would be to apply a coefficient-uniform broad,
large-sieve, or Hilbert statement: the phase-conjugating control above
rules that out.

Thus the lawful next analytic question is not generic cone
transversality.  It is whether the inner coefficient in (114.H18), with
its exact \(\chi _4(h)\chi _4(h')\), gcd cutoffs, and slanted symbol,
satisfies a signed shifted-divisor estimate.  No such estimate is proved
in the assigned artifacts.

## 5. Control tests and outcomes

| Seam or required control | Outcome |
|---|---|
| `literal_packet_to_physical_sum_identity` | **Pass.** Equation (114.H8) follows coefficientwise; the factor is exactly (2i). |
| `gcd_lift_and_full_product_retention` | **Pass with correction.** Both lifts remain in (114.H9), and the true diagonal is (g^2uv=g'^2u'v'). Any split by (uv=u'v') alone fails. |
| `quarter_shift_and_character_placement` | **Pass.** The (1/4-3/4) difference becomes (2i\chi _4(g)), then (chi _4(g)\chi _4(u)=\chi _4(h)). In (114.H1) Cauchy intentionally erases the outer character; in (114.H14) it remains inside the row. |
| `linear_vs_energy_capacity` | **Pass.** The linear budget is (L^{3/2}); the squared budget is (L^3). Equal product costs (L^2); each width-(L) corridor costs (L^3). |
| `mean_square_orientation_and_cauchy_cost` | **Conditional pass, candidate correction required.** The old (h)-outer full-symbol mean square implies the packet through (114.H6)--(114.H8). The candidate's gcd-masked rows are not the same theorem. The (k)-outer alternative preserves (chi _4). Both cost one outer factor (L\asymp K). |
| Mean-square row diagonal | **Pass and critical.** It is (k=k') in the (h)-outer Gram (or (h=h') in the opposite Gram), not the four-variable equal-product locus. Its mass is (LK\asymp L^2), the whole permitted mean-square scale. |
| `equal_full_product_diagonal` | **Pass.** The complete fibre square is (114.H11), including distinct factorizations and both gcd lifts; it has a factor (L) of room in direct energy. |
| Full-product radial corridor | **Pass.** Equation (114.H12) gives (|hk-h'k'|\le L) at cost (L^3X^\varepsilon), even for bounded coefficients. |
| `shifted_product_connector` | **Pass only for the full product.** Equation (114.H18) uses (r=h'k'-hk). The memo shadow (uv-u'v') is not literal without a further lift reduction. No shifted-product estimate is proved. |
| `ray_defect_connector_and_rank_one_identity` | **Algebra pass; analytic-connector fail.** Equations (114.H15) and (114.H17) are exact. They do not imply cancellation in the fixed-(R) scalar energy. |
| `narrow_broad_threshold_interface` | **Narrow pass, broad open.** (Q=L) makes the determinant-narrow branch exactly target-safe. It leaves no polynomial slack and the double-far survivor retains (L^4) coefficient-blind capacity. |
| (Delta\pm\rho) multiplicity test | **No gain.** Fixed generic invariants have divisor multiplicity, but there are (L^4)-capacity many invariant pairs; the exceptional (Delta=\pm\rho) cases are at most target-sized coordinate-parallel corridors. |
| `actual_symbol_vs_adversarial_coefficients` | **Coefficient-uniform claim fails.** Phase-conjugating (b) gives double-far energy (asymp L^4). The actual-symbol theorem remains open; the row diagonal is a coherent actual-symbol critical obstruction to any lossy proof. |
| `no_shellwise_l1_or_cross_block_cancellation` | **Pass.** The gcd telescope is collapsed before the norm, all (g,g') cross terms remain, and the argument uses one fixed physical block only. |
| `square_near_square_high_gcd_owner_scope` | **Pass with scope note.** The full packet contains the low square and near-square atoms. If they are removed, their accepted linear owner cost must be paid before squaring. High gcd is used exactly once in the full-symbol mean-square connector. No owner correction cancels (114.H18). |
| `critical_j1_and_exact_square_j2_boundary` | **Pass.** All identities and counts are uniform for fixed (1\le K/L\le16), but this round's analytic target is persistent (j=1). The isolated (j=2) boundary is not thereby estimated. |
| `involution_barrier_and_downstream_scope` | **Pass.** Rearrangements (114.H9)--(114.H18) change no capacity. Only the two absolute corridor counts are new lossy estimates. No BAL, M9-M2, M9, endpoint, or exponent claim follows. |

No numerical experiment was used.  The false-shadow construction is an
exact finite algebraic control, not computational evidence.

## 6. Dependencies and exact artifacts used

The audit used only the assigned context:

- `protocol.md`;
- `state/proof_obligations.yml` at the graph hash printed above, especially
  `M9-M2-smooth-balanced-quarter-packet-estimate`,
  `M9-M2-balanced-smooth-literal-atom-dictionary`,
  `M9-M2-dual-square-root-spacing-mean-square`,
  `M9-M2-smooth-dual-three-quarter-equivalence`,
  `M9-M2-smooth-small-gcd-quarter-packet`,
  `M9-M2-balanced-quarter-packet-normalization-scope`, and
  `M9-M2-physical-one-count-assembly`;
- `state/active_campaign.yml` and the task brief;
- `strategy/A1_0821_1.md`, `strategy/A1_0821_2.md`,
  `strategy/A2_0821_1.md`, `strategy/A2_0821_2.md`, and
  `strategy/conductor_0821_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/candidates/conductor_literal_energy_fork.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/reports/balanced_packet_actual_symbol_formalization.md`.

No sibling Round-114 report, web source, external theorem, or numerical
experiment was used.  The argument is algebraic and elementary counting.

## 7. Recommended state effect

1. **Promote or record as a proved reduction** the fixed-block implication
   from the old full-symbol mean square (114.H1) to the balanced packet,
   using the accepted high-gcd owner.  This is a connector only; it proves
   no mean-square estimate.

2. **Revise** `M9-M2-dual-square-root-spacing-mean-square` so that its
   actual symbol and row orientation are explicit.  Its implication scope
   may include the balanced and unbalanced smooth parents after their
   literal owner maps are recorded, but it must not point directly to all
   of `M9-M2`, because the hard TOP parent remains open.

3. **Promote or retain as proved finite estimates** the equal-full-product
   bound (114.H11), the radial corridor (114.H12) at (U=L), and the
   determinant corridor (114.H13) at (Q=L).  The first two are most
   naturally recorded as evidence on the balanced packet node; none is a
   strict power saving for the complete energy.

4. **Retain open** `M9-M2-smooth-balanced-quarter-packet-estimate`.  The
   smallest corrected direct survivor is (114.H18).  Any Round-115 broad
   campaign must name an inequality acting on its actual signed inner
   divisor correlation; determinant separation or the identities
   (114.H4) alone are insufficient.

5. **Reject** the coefficient-uniform double-far broad theorem and any
   inference that generic fixed-\((\Delta,\rho)\) divisor multiplicity
   yields a global (L^3) estimate.  Record the phase-conjugating array as
   its false shadow.

6. **No change** to the hard TOP parent, the unbalanced parent, `M9-M2`,
   either M1 parent, endpoint uniformity, `M9`, or the Gauss-circle target.
   No global exponent improves in this report.
