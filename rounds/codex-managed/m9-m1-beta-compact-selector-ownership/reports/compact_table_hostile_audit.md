## Result

The requested strong row-by-row table is **not determined by the accepted
state**, and one of its intended columns is type-wrong.  The sixteen terms
are cells of a finite product-Stokes representation.  An operator label such
as (L_uL_v), (B_uP_v), or (A_uA_v) does not by itself say whether its
antecedent is terminal, a radial (w)-side, or the endpoint/arithmetic
module.  For the terminal antecedent it is a retained representation cell;
for a transferred radial (w)-side it is zero after support separation; for
the endpoint/arithmetic antecedent it is routed only after summing all three
hierarchical masks and all representation cells.  No accepted theorem routes
an individual beta-masked row to the physical module.

There is, however, a constructive architecture correction.  At finite
height first use the complete Stokes identity to return the endpoint-free
beta vector to its original positive-line representative, and only there
define

\[
 \mathfrak V^{\rm fin}_{\beta,0}
 :=R_uR_v[\psi(\beta)\chi _0(\alpha)Q_{\rm ef}],\qquad
 \mathfrak V^{\rm fin}_{\beta,\infty}
 :=R_uR_v[\psi(\beta)(1-\chi _0(\alpha))Q_{\rm ef}].
\]

Their sum is exactly (R_uR_v[\psi Q_{\rm ef}]).  This avoids assigning
each of the sixteen representation cells to an amplitude type.  It does not
delete the mixed beta connector.  If either localized share is transferred
again, the mixed row reappears with its full cutoff derivatives.  Thus the
correction is lawful only as a whole-vector positive-line decomposition.  A
new seam remains: identify the direct positive-line large-alpha complement,
including the artificial-residue share, with the already accepted
large-alpha package.

## Exact statement and hypotheses

Assume the Round-44 packet, in particular fixed finite (u,v,w) contours,
the common fixed-(w) antecedent, no boundary pole, and the combined
Laurent/derivative convention at axial--artificial or axial--arithmetic
collisions.  Let

\[
 B_j=H_{j,+}-H_{j,-},\qquad F_j=L_j+B_j,
\]

where (B_u,B_v) are horizontal sides of the **(u,v) contour
rectangles**, not radial (w)-sides.  Let (P_j) consume the corresponding
coordinate variable by the accepted residue functional and let (A_j) be
positive area integration.  Work on the actual contour

\[
 b=1/\log(2X),\quad 0\leq a<a_0,\quad a+b<1/2,
 \quad a/2+b<1/4.
\]

For terminal terms write

\[
 \Sigma_j={
 \mathbf1_{j=0}\,u^{-1}\text{ hard top},\ 
 \mathbf1_{j=0}W_{0,r}\text{ regular top},\ 
 \mathbf1_{j\geq1}W_j\text{ interior}}.
\]

Every member retains its actual (D_j,H_j+1), floors, stars,
(chi _4(q)), and physical profile.  A restriction (P_u) or (P_v)
acts on this already selected family; the packet does not supply enough
pole data to infer which smooth restricted subclasses vanish.

The exact conclusion supported by the hypotheses is the following scoped
certificate.

1. The sixteen normalized operators and their coefficients are fixed.
2. Applied to (Q_T), every row is a retained finite terminal
   representation cell carrying (Sigma_j); applied to a radial (w)-side,
   every row is eventually zero; applied to (mathfrak M_{\rm fin}), no
   row has an individual physical-module theorem.
3. Only the complete endpoint-free vector has the accepted joint
   height/profile limit.
4. The external factor
   (-4X^{1/4}\Re\{e(1/8)(\cdot)\}/\pi) is owned by the complete vector and
   restored outside the complete sum exactly once.

No conclusion follows that any one row equals a member of the corrected
compact-amplitude family.

## Proof or derivation

For compact notation let

\[
 C_0=\psi\chi _0,
 \quad C_1=\tfrac12(\psi'\chi _0-\psi\chi _0'),
 \quad C_2=\tfrac14(\psi''\chi _0-2\psi'\chi _0'
                         +\psi\chi _0'').
\]

Here (C_1=-\partial_\mu(\psi\chi _0)
=-\partial_\nu(\psi\chi _0)), while
(C_2=\partial_\mu\partial_\nu(\psi\chi _0)).  The following is the
largest exact table obtainable from the packet.  In the measure column,
“line” and “horizontal” mean the normalized measures already absorbed in
(L_j,B_j), “area” means the normalized positive area measure absorbed in
(A_j), and “--” means that a residue has consumed that variable.  The
packet does not expose further scalar (2\pi i) factors, so none may be
invented outside these normalized operators.

| row | beta operator and coefficient | remaining (u\times v) measure | central-transfer density | exact scope |
|---:|---|---|---|---|
| 1 | (L_uL_v[\psi Q]) | line x line | (C_0) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 2 | (L_uB_v[\psi Q]) | line x oriented horizontal | (C_0) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 3 | (B_uL_v[\psi Q]) | oriented horizontal x line | (C_0) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 4 | (B_uB_v[\psi Q]) | oriented horizontal x oriented horizontal | (C_0) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 5 | (L_uP_v[\psi Q]) | line x -- | (C_0|_{v=0}) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 6 | (B_uP_v[\psi Q]) | oriented horizontal x -- | (C_0|_{v=0}) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 7 | (P_uL_v[\psi Q]) | -- x line | (C_0|_{u=0}) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 8 | (P_uB_v[\psi Q]) | -- x oriented horizontal | (C_0|_{u=0}) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 9 | (P_uP_v[\psi Q]), once | -- x -- | (C_0|_{u=v=0}) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 10 | \(\frac12L_uA_v[\psi'Q]\) | line x area | (C_1) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 11 | \(\frac12B_uA_v[\psi'Q]\) | oriented horizontal x area | (C_1) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 12 | \(\frac12P_uA_v[\psi'Q]\) | -- x area | (C_1|_{u=0}) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 13 | \(\frac12A_uL_v[\psi'Q]\) | area x line | (C_1) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 14 | \(\frac12A_uB_v[\psi'Q]\) | area x oriented horizontal | (C_1) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 15 | \(\frac12A_uP_v[\psi'Q]\) | area x -- | (C_1|_{v=0}) | (T/0_{w\rm-side}/M_{\rm agg}) |
| 16 | \(\frac14A_uA_v[\psi''Q]\) | area x area | (C_2) | (T/0_{w\rm-side}/M_{\rm agg}) |

The notation in the last column is exact: (T) means a retained terminal
representation cell when the antecedent is (Q_T); (0_{w\rm-side})
means exact eventual vanishing only when the antecedent is a transferred
radial (w)-side; and (M_{\rm agg}) means that a module antecedent is
routed only in the full three-mask aggregate.  In particular, rows 2--4,
6, 8, 11, and 14 contain (B_u) or (B_v), but compact beta support does
not annihilate them merely because it annihilates radial (w)-sides.

For every terminal entry in the table, (Sigma_j) is selected before the
operator is applied.  The hard (j=0) line share uses the signed Plemelj
functional where that line reaches the top boundary; the regular (j=0)
and interior (j\geq1) shares use ordinary integration.  A (P_u) row
instead uses the accepted residue restriction.  The supplied data do not
justify replacing all these different residual measures by one universal
((\beta,L,\nu)) compact-amplitude formula.

The central/complement cancellation is also exact.  For
(c_\infty=\psi(1-\chi _0)), the corresponding first-connector density is

\[
 \tfrac12\{\psi'(1-\chi _0)+\psi\chi _0'\},
\]

and the mixed density is

\[
 \tfrac14\{\psi''(1-\chi _0)+2\psi'\chi _0'
                         -\psi\chi _0''\}.
\]

Adding central and complement cancels the (chi _0') and
(chi _0'') terms, but leaves

\[
 \tfrac14A_uA_v[\psi''Q].
\]

Hence the pure beta mixed connector survives every transferred
central/large-alpha recombination.  In the alternative positive-line
architecture it is absent from the display only because all sixteen cells
have already been recombined by the exact Stokes identity.  It is encoded
in that equality, not set equal to zero.

Finally, common transfer of (G=E_1+R_1) preserves artificial-pole
cancellation row by row before residue separation.  At an
axial--artificial or axial--arithmetic collision the single combined local
coefficient is used, and row 9 supplies the corner once.  After endpoint
module subtraction, however, the surviving (R_1) artificial residue must
remain analytically recombined; the terminal right-chamber (h,q) series
cannot be substituted on that residue line.

## First doubtful or unproved step

The first unlawful inference occurs already at row 1 if one tries to fill
the “terminal survivor or routed module” column from the operator label:

\[
 L_uL_v[\psi Q]
 \quad\not\Longrightarrow\quad
 \text{an individually routed beta physical module or a named compact }
 \tau.
\]

The accepted module theorem is

\[
 \sum_{\kappa\in\{\beta,\alpha,o\}}
 \mathsf X_{uv}[\Theta_\kappa\mathfrak M_{\rm fin}]
 =\mathfrak M_{\rm fin},
\]

not a theorem for (L_uL_v[\psi\mathfrak M_{\rm fin}]), and not even a
termwise theorem for the full beta-masked (mathsf X_{uv})-image.  The
same defect repeats in every row.  Only after specifying the antecedent can
one call the row terminal, radial-side zero, or aggregate-module data.

The proposed architecture correction has a different first open seam.
The identity

\[
 R_uR_v[\psi\chi _0Q_{\rm ef}]
 +R_uR_v[\psi(1-\chi _0)Q_{\rm ef}]
 =R_uR_v[\psi Q_{\rm ef}]
\]

is exact, but it does not by itself identify the second term with the
already proved post-routing large-alpha package.  Nor does the
terminal-only (Q_T) packet show where the endpoint-free artificial
residue is placed after this split.  That comparison, with the three
physical selectors and the external factor kept once, is the first new
proof required.  Inserting (chi _0) into the sixteen already integrated
rows is not a substitute: doing so requires (C_1,C_2) above and therefore
recreates all connector terms.

## Required controls and outcomes

1. **Sixteen-row count:** pass.  There are nine pure boundary/axis rows,
   six first-connector rows, and one mixed row.
2. **(B_u,B_v) versus radial (w)-sides:** pass negatively.  Only an
   antecedent supported on a radial (w)-side is annihilated; the
   (u,v)-horizontal rows are retained.
3. **Beta mixed connector:** pass.  Its sign is positive and its
   coefficient is (1/4); central/complement recombination leaves it.
4. **Top/interior selectors:** partial pass.  The exact selectors
   (j=0,j=0,j\geq1) precede every terminal operator.  The packet does not
   determine every zero after an axis residue or a universal rowwise
   Plemelj/ordinary-integral amplitude type.
5. **Aggregate module scope:** pass negatively.  No individual
   beta-masked face, axis, connector, or corner is licensed as the physical
   module.
6. **Artificial/arithmetic collision and corner:** pass at finite height
   under the common combined-coefficient convention; the corner is once.
   No individual-row physical limit is thereby proved.
7. **Residual measures:** pass only in normalized operator notation.  The
   rows have the line/horizontal/area/residue dimensions displayed above;
   the packet does not license one common residual contour density for all
   rows.
8. **External normalization:** pass only globally.  The factor
   (-4X^{1/4}\Re(e(1/8)\cdot)/\pi) belongs outside the complete vector and
   is restored once.
9. **Positive-line-before-alpha architecture:** finite identity passes.
   Compatibility with the accepted large-alpha theorem and explicit
   ownership of the artificial-residue share remain unproved.

These are algebraic controls; no numerical experiment is relevant or was
used.

## Dependencies and exact artifacts

- `protocol.md`.
- `state/proof_obligations.yml`, specifically the accepted nodes
  `M9-M1-beta-finite-two-axis-product-Cauchy-Green`,
  `M9-M1-beta-finite-prelimit-axial-vector-ledger`,
  `M9-M1-beta-global-aggregate-physical-module-routing`,
  `M9-M1-beta-endpoint-free-axial-remainder-limit`,
  `M9-M1-beta-complete-axial-connector-ledger`, and
  `M9-M1-beta-double-bounded-cell-bound`.
- `state/active_campaign.yml`.
- `rounds/codex-managed/m9-m1-beta-compact-selector-ownership/derivation_packet.md`.
- `rounds/codex-managed/m9-m1-beta-mask-endpoint-axial-compatibility/synthesis.md`.
- `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/synthesis.md`.
- `rounds/codex-managed/m9-m1-beta-axial-side-exhaustion/synthesis.md`.
- `rounds/codex-managed/m9-m1-beta-physical-module-transfer/synthesis.md`.
- `rounds/codex-managed/m9-m1-beta-endpoint-free-axial-limit/synthesis.md`.
- `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/synthesis.md`.
- `rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/synthesis.md`.
- `rounds/codex-managed/m9-m1-beta-translation-divided-difference/synthesis.md`.
- `rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/synthesis.md`.
- `rounds/codex-managed/m9-m1-beta-double-bounded-cell/synthesis.md`.

No other Round-44 report, external source, or computational artifact was
used.

## Recommended state effect

**Revise**, rather than promote, the sixteen-stratum selector-table
obligation.  Promote no rowwise compact-amplitude or rowwise physical-module
claim from this round.  Record the no-go statement that a geometric
product-Stokes row is not an ownership projector and that aggregate
three-mask routing cannot be disaggregated to beta-masked rows.

Replace the strong table target by a narrower positive-line certificate:

1. exact finite return of the complete endpoint-free beta vector to its
   positive-line representative;
2. direct (chi _0+(1-\chi _0)=1) decomposition there;
3. explicit inclusion and estimate of the central artificial-residue
   share;
4. exact identification of the positive-line complement with the accepted
   large-alpha theorem; and
5. the three physical profile selectors and external normalization once.

Retain `M9-M1-beta-double-bounded-cell-bound` open until that certificate
and an isolated analytic proof exist.  Reject any claim that
central/large-alpha recombination deletes
(A_uA_v[\psi''Q]/4), that (B_u,B_v) are radial sides, or that an
individual beta-masked representation cell inherits the aggregate physical
module theorem.
