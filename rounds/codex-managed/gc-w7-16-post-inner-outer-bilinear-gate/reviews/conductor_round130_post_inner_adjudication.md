# Round 130 conductor adjudication: lower shells contract, the top signed scalar remains

Campaign: `gc-w7-16-post-inner-outer-bilinear-gate`

Starting graph SHA-256:
`354f5ca462467d091a9a50c8dbc1173ffba56516963274f9fc232ea11890d20e`

## 1. Result

Round 130 proves one shellwise refinement and three scoped structural
results, but no complete fixed-block or global exponent improvement.

First, on a half-open inner reduced-denominator shell $b'\asymp B$,
the exact Stieltjes-recombined complete-lift support forces

\[
 g\asymp D/B,
 \qquad |a'|\asymp LB/D,
 \qquad \#\{a'\}\ll LB/D.
 \tag{130.J1}
\]

The Round-129 branch theorem and the accepted outer coefficient energy
therefore give

\[
 \boxed{|\mathfrak O_{i,B}^{+}|\ll_\varepsilon
 B K_B Y^\varepsilon.}
 \tag{130.J2}
\]

This improves the former deliberately uniform $DK_B$ ledger by $B/D$
on every lower shell.  It localizes the complete obstruction to
$B\asymp D$, where (130.J2) is still

\[
 DK_D=Y^{35/48+o(1)}.
 \tag{130.J3}
\]

Second, the target outer energy is strictly stronger than the physical
scalar.  In atom coordinates its exact Gram is $H^*H$ at the fixed
input $\mathbf 1$; after physical reassembly its ray-space form is
$K_{B,+}^*K_{B,+}$.  The triangular full-row operator $G$ instead
satisfies $\lVert Gb\rVert_2^2=b^*G^2b$.  No connector identifies the
resolved energy with $G^2$, and support- and norm-matched aligned controls
attain the raw $LDK_B^2$ energy and $DK_B$ scalar capacities.  Thus marginal
norm facts do not prove the target, although this is not a lower bound for
the literal Vaaler family.

Third, for one fixed primitive top-shell outer ray, the determinant chart

\[
 n=aq-bp,
 \qquad n\equiv-bp\pmod {|a|},
 \qquad b'={b(a+p)+n\over a}
 \tag{130.J4}
\]

is bounded-to-one when the physical $p$-support has span $O(|a|)$.
The numerator increment is therefore a residue lift of the determinant,
not a second independent long variable.  This forbids automatic
independent-$p$ square-root credit but leaves cancellation between the
actual induced residue weights open.

Finally, exact threshold/Möbius/lift recombination restores the original
$(h',d')$ product wave.  A numerator-first product-window modulus and a
sequential unit-Hessian transform return capacities worse than (130.J3).
These are method no-gos, not physical lower bounds.

The complete fixed-block exponent remains $35/48$, the determinant
target remains $1/2$, and the surviving gap is $11/48$.  No global
exponent, M9 component, endpoint theorem, bridge, or quarter theorem is
promoted.

## 2. Exact statements and hypotheses

Fix

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},
 \qquad D/L\le B\le D,
\]

one literal M1 or M2 moving-symbol stratum, sign sector, half-open inner
shell, and one determinant orientation.  Before any remaining triangle,
the discovery report proves the exact formula

\[
 \mathfrak O_{i,B}^{+}
 =\sum_{r=(a,b)}A_i(r)e(ca/(\kappa_i b))
 \sum_p\sum_{\rho\mid a+p}\sum_\eta
 S_{i,r,a+p,\rho,\eta},
 \tag{130.J5}
\]

where every $S$ retains the literal Stieltjes threshold, common
$\chi_4(g)$ lift character, floor cutoff, Möbius progression, determinant
taper, shell owner, strict/weak/star convention, and the correct M1 or M2
quarter orientation.  In M1 the reduced denominator character is split
into the two phases $e(\pm\rho v/4)$; in M2 the numerator character
$\chi_4(|a+p|)$ stays in the $p$-coordinate.

The accepted facts are

\[
 \#\{r\}\ll LD,
 \qquad \sum_r|A_i(r)|^2\ll D/L,
 \qquad \sum_r|A_i(r)|\ll D,
 \tag{130.J6}
\]

and, after the divisor and branch sum for fixed (r,a'),

\[
 \left|\sum_{\rho\mid a'}\sum_\eta
 S_{i,r,a',\rho,\eta}^{(B)}\right|
 \ll_\varepsilon {K_B\over L}Y^\varepsilon,
 \tag{130.J7}
\]

with

\[
 K_B=\min(Q_B,Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2})
 \asymp Y^{11/48+o(1)}.
\]

Equations (130.J1), (130.J6), and (130.J7) are the exact hypotheses of
the shell refinement.  The support count in (130.J1) is imposed only
after the Stieltjes thresholds have recombined to the exact coefficient;
it is not asserted for each separate threshold atom.  The equations
include both numerator signs up to a constant, and $LB/D\ge1$ on the
allowed range.

For the energy seam, let $H$ be the literal incidence map from the
$(p,\rho,\eta)$ labels to outer rows.  Then

\[
 F=H\mathbf1,
 \qquad E_{\rm res}=\mathbf1^*H^*H\mathbf1.
 \tag{130.J8}
\]

After the algebraic labels are reassembled to physical primitive rays,
write the one-sided owned kernel as $K_{B,+}$; the same value is

\[
 E_{\rm res}=b^*K_{B,+}^*K_{B,+}b.
 \tag{130.J9}
\]

For comparison only, the complete symmetric triangular random-cell
operator

\[
 G_{rs}=(1-W|\lambda_r-\lambda_s|)_+
\]

has $b^*Gb$ as the scalar cluster energy and
$\lVert Gb\rVert_2^2=b^*G^2b\le\lVert G\rVert b^*Gb$.  Equations
(130.J8)--(130.J9) are not automatically $b^*G^2b$.

## 3. Proof and reconciliation

### 3.1 Shell support and capacity

The exact Stieltjes-recombined inner complete-lift coefficient is nonzero
only when

\[
 gb'\asymp D,
 \qquad g|a'|\asymp L,
 \qquad b'\asymp B.
\]

Consequently $g\asymp D/B$, $|a'|\asymp LB/D$, and the number of
integer $a'$ is $O(LB/D)$.  Outer Cauchy gives the last bound in
(130.J6).  Taking the (a')- and outer-ray triangles only after the
proved inner estimate gives

\[
 D\cdot {LB\over D}\cdot {K_B\over L}=BK_B,
\]

which proves (130.J2).  For $B=Y^b$, $16/48\le b\le24/48$, this is
$Y^{b+11/48+\varepsilon}$.  The smallest shell is $Y^{9/16}$; the
top shell is $Y^{35/48}$.  Hence every fixed range
$B\le DY^{-\sigma}$ gains $Y^{-\sigma}$, but the complete shell sum
has no strict fixed-power improvement.

### 3.2 Exact duality and the false control

Expanding the resolved row proves (130.J8), while Hilbert-space duality
allows a maximizing outer phase vector.  Positive energy therefore erases
the physical outer phase and coefficient direction.  A model with
$LD$ rows, $L$ increment slots, outer coefficient $L^{-1}$, and
inner entry $K_B/L$, phase aligned row by row, has

\[
 E_{\rm res}=LDK_B^2,
 \qquad |\mathfrak O|=DK_B.
\]

It satisfies all displayed support and marginal norm hypotheses.  It is
not asserted to satisfy the literal threshold formula; it proves only that
an actual-family angle or correlation theorem is indispensable.

The two post-unmask reviews distinguish three operators.  $H^*H$ acts
on auxiliary incidence labels, $K_{B,+}^*K_{B,+}$ acts on physical ray
coefficients for the resolved row, and $G^2$ is the pullback for the
deliberately completed full row.  Mixed shell, orientation, and diagonal
cross terms have no known sign, so no Loewner comparison is inferred.

### 3.3 Determinant residues

For fixed physical primitive $(a,b)$, if $a'=a+p$, $b'=b+q$, then
(130.J4) follows algebraically.  Since multiplication by $-b$ permutes
residues modulo $|a|$, fixed $n$ selects one $p$-class.  A bounded
union of intervals of total span $O(|a|)$ contains $O(1)$ lifts of
that class, and $q$ is then forced.  This is a fixed-outer-ray,
top-shell statement after Möbius reassembly.  It gives no global
multiplicity bound as the outer ray varies, and the induced M1/M2 weights
are not thereby proved to be clean characters of $n$.

The hostile same-denominator controls have $q=0$ and $p=-t$ in M1
or $p=-2j$ in M2.  They have multiplicity one in (130.J4) while their
carrier and actual character products align.  Thus bounded multiplicity
removes a fictitious Cartesian count but supplies no cancellation.

### 3.4 Exact inversion and transform returns

Summing the Stieltjes differences restores the denominator profile.
Summing the Möbius pieces restores primitivity, and the unique complete
lift $g=(|h'|,d')$ restores the original $(h',d')$ coefficient.  At
threshold equality, M1 recombines
\(\chi_4(g)\chi_4(b')=\chi_4(d')\), while M2 retains the fixed sector
factor
\(\epsilon_{\rm sgn}\chi_4(g)\chi_4(|a'|)
=\epsilon_{\rm sgn}\chi_4(|h'|)\).  Therefore full auxiliary
recombination is an identity, not a new estimate.  Only after all
half-open $B$-owners have been reassembled, the accepted complete
original product-window theorem gives $Y^{37/48+\varepsilon}$, worse
than (130.J3); no isolated top-owner version is inferred.

On the top shell, summing $p$ first and taking a product-window modulus
returns the cruder $D^2/L=Y^{40/48}$.  A complete two-variable
stationary transform has unit-order Hessian determinant, the quarter
characters only translate its dual lattice, and aliaswise modulus returns
$DQ_*=Y^{43/48}$.  None improves (130.J3); all remain method controls.

## 4. First doubtful or unproved step

The smallest open assertion is now the literal bounded-lift top-shell
scalar

\[
 |\mathfrak O_{i,B\asymp D}^{+}|
 \ll_\varepsilon DK_DY^{-\delta+\varepsilon}
 \tag{130.J10}
\]

for some fixed (delta>0).  The determinant target needs
(delta=11/48).  It must keep the actual outer coefficient, numerator
residue lifts, Stieltjes thresholds, reciprocal stationary aliases, and
the M1/M2 character orientation joint before an absolute value.  The
current results supply neither a nonzero Fourier-mode estimate for the
induced determinant residue weights nor an actual-vector angle excluding
the phase-aligned direction.

## 5. Control matrix

| Seam | Outcome |
|---|---|
| literal post-inner dictionary | Green: both complete lifts, thresholds, characters, phases, taper, stars, and owners are present before norms. |
| shell numerator count | Green: $\#a'\ll LB/D$, independently rechecked. |
| refined shell ledger | Green: $D(LB/D)(K_B/L)=BK_B$. |
| exact dual/Gram | Green after correction: $H^*H$ or $K_{B,+}^*K_{B,+}$, not resolved $G^2$. |
| phase-aligned false control | Green as a marginal-hypothesis obstruction, not a physical lower bound. |
| determinant residues | Green with primitive fixed-ray/top-shell/span scope. |
| actual character placement | Green: M1 denominator quarter phases and M2 numerator character are not interchanged. |
| product-window return | Green as a no-go; exact inversion returns the accepted original theorem. |
| unit-Hessian return | Green as a canonical-transform control, not an impossibility theorem. |
| Möbius, thresholds, faces, and owners | Green: every algebraic summand and physical atom is charged once. |
| capacity | Green: lower shells improve, top and complete block remain $35/48$, target $1/2$. |
| downstream scope | Green: no exponent or M9 promotion. |

The campaign used 100% analytical/algebraic reasoning, no computation,
and no external theorem.

## 6. Dependencies and exact evidence

Primary reports:

- `reports/blind_outer_bilinear_dual_feasibility.md`;
- `reports/actual_numerator_increment_recombination_attack.md`;
- `reports/outer_ray_bilinear_hostile_audit.md`.

Independent reviews:

- `reviews/blind_post_unmask_outer_gram_seam.md`;
- `reviews/hostile_determinant_residue_gram_addendum.md`;
- `reviews/independent_shell_refinement_and_inversion_audit.md`.

Conductor candidate:

- `candidates/conductor_determinant_residue_outer_gram.md`.

Accepted dependencies are the exact current scopes of
`GC-W7-16-reduced-Farey-cluster-reduction`,
`GC-W7-16-original-numerator-product-window-bound`,
`GC-W7-16-determinant-half-shift-transform-obstruction`,
`GC-W7-16-direct-Stieltjes-birth-block-curvature-lemma`, and
`GC-W7-16-complete-all-shell-curvature-saving`.

## 7. Conductor decision

Promote the shell support/refined $BK_B$ lemma, the primitive top-shell
determinant-residue bounded-multiplicity chart, and the exact scoped outer
Gram obstruction.  Update the existing product-window and transform
obstructions with the exact recombination returns.

Retain `GC-W7-16-actual-reduced-determinant-correlation` open, narrowed to
the signed $B\asymp D$ scalar (130.J10).  Reject automatic
independent-$p$ credit, support-only outer energy, resolved-$G^2$
identification, character-splitting nonresonance, product-window reversal,
and sequential-transform contraction.

The round closes with no change to the complete $Y^{35/48}$ exponent,
the internal global exponent $1/3$, the audited external benchmark,
M9-M1, M9-M2, endpoint uniformity, M9, the conditional bridge, or the
quarter target.
