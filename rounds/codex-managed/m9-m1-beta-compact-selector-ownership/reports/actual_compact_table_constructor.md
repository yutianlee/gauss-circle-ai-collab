## Result

The requested row-by-row map from the sixteen transferred cells to the
compact amplitude is not a lawful ownership statement.  The accepted
Round-37--38 construction uses the opposite order:

\[
 \boxed{
 \text{sum all sixteen cells at finite fixed-\(w\) height}
 \;\longrightarrow\;
 R_uR_v[\psi(\beta)Q_{\rm ef}]
 \;\longrightarrow\;
 \text{split in }\alpha .}
 \tag{44.1}
\]

The first arrow is the complete finite product Cauchy--Green/Stokes
identity.  It is performed before outside-height exhaustion.  No
individual transferred face, axis, connector, mixed area, or corner has a
licensed physical limit.  The second arrow is the ordinary pointwise
partition

\[
 1=\chi _0(\alpha)+\{1-\chi _0(\alpha)\}
 \tag{44.2}
\]

on the reassembled positive-\(a\), positive-\(b\), fixed-\(w\) terminal
density.  Consequently the actual compact one-count object is

\[
 \boxed{
 \mathfrak T_{\rm db}^{U,V,S}
   =R_uR_v[\psi(\beta)\chi _0(\alpha)Q_{\rm ef}],}
 \tag{44.3}
\]

not a sum of sixteen separately typed amplitudes.  Its only physical
profile selectors are the hard singular top
\(\mathbf 1_{j=0}u^{-1}\), the regular top
\(\mathbf 1_{j=0}\widehat W_{0,r}\), and the interior family
\(\mathbf 1_{j\geq1}\widehat W_j\).  The surviving finite
\(\psi''/4\) cell is real and indispensable in the transferred
representation, but it is consumed, together with the other fifteen
cells, by the exact first arrow in (44.1).  It is neither zero nor a
seventeenth local terminal type.

Thus the fullest lawful sixteen-row table is an **aggregate-only
representation table**.  Requiring a separate \(\tau\)-type and physical
limit for every row is overstrong and type-wrong.  If one nevertheless
insists that row 1 separately “reaches the compact amplitude,” the graph
is already underdetermined at row 1.

## Exact statement and hypotheses

Fix the Round-44 contour and scale data

\[
 b=\frac1{\log(2X)},\qquad 0\leq a<a_0,\qquad
 a+b<\frac12,\qquad \frac a2+b<\frac14,
 \tag{44.4}
\]

\[
 D_j=2^{-j}\lfloor\sqrt X\rfloor,qquad
 H_j=\lfloor D_jX^{-1/4}\rfloor,\qquad H_j\geq1,
 \tag{44.5}
\]

and finite fixed-\(w\) rectangles with no boundary pole.  All
artificial/arithmetic/axial collisions are evaluated from one combined
Laurent or derivative coefficient, and the iterated \(u=v=0\) corner is
counted once.  After the exact aggregate endpoint/arithmetic routing, the
endpoint-free terminal density can be represented by

\[
\begin{aligned}
Q_{\rm ef}={}&\mathbf1_{hq=m}\chi _4(q)
 \sum_j\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v
 \left(\frac hq\right)^{(u+v)/2}\\
&\quad\times {\cal R}_{\omega,v}(1-s)
 K_{u+v}(1-s)m^{-s},
 \qquad {\cal R}_{\omega,v}=R_{1,v},
\end{aligned}
\tag{44.6}
\]

where the last equality is meromorphic and is used only with common
mask, endpoint, and collision ownership.  In particular,

\[
 \widehat W_0(u)=\frac1u+\widehat W_{0,r}(u),
 \qquad
 \sum_j\widehat W_j
 =\mathbf1_{j=0}\left(\frac1u+\widehat W_{0,r}\right)
  +\mathbf1_{j\geq1}\widehat W_j .
 \tag{44.7}
\]

The packet's displayed \(Q_T[G]\) is a pre-routing density.  It can be
used in the finite full-vector identity only while its endpoint,
artificial, and arithmetic antecedents remain attached.  It cannot be
declared to be the compact terminal density by itself.  Formula (44.6)
is the endpoint-free terminal representative; the separately owned
\(\rho\)-residue, endpoint/arithmetic, axial, collision, and corner
modules are not inserted into (44.3) a second time.

Let \(\mathrm d\mathfrak m_s\) denote the unchanged outer fixed-\(w\)
terminal measure.  Let \(\mathrm dL_j\) denote the upward final vertical,
\(\mathrm dB_j=\mathrm dH_{j,+}-\mathrm dH_{j,-}\) with both
horizontals parametrized left-to-right, \(P_j\) the accepted
\(2\pi i\)-residue operator (which consumes that contour measure), and
\(\mathrm dA_j\) the positive Cauchy--Green area measure.  Put

\[
 \Sigma_j:=
 \mathbf1_{j=0}\{u^{-1}+\widehat W_{0,r}(u)\}
 +\mathbf1_{j\geq1}\widehat W_j(u).
 \tag{44.8}
\]

The complete lawful table is the following.  “Aggregate only” means that
the row has no separate alpha localization or physical limit; all rows
are first summed to (44.1).  A residue symbol applied to \(\Sigma_j\)
means exact coefficient extraction, so an analytic selector component is
automatically zero rather than being assigned a fictitious terminal
type.

| row | exact finite cell | coefficient and mask | remaining finite measure | inherited selector/profile | lawful ownership |
|---:|---|---|---|---|---|
| 1 | \(L_uL_v[\psi Q_{\rm ef}]\) | \(1,\psi\) | \(\mathrm d\mathfrak m_s\,\mathrm dL_u\,\mathrm dL_v\) | \(\Sigma_j\widehat\phi(v)\) | aggregate only |
| 2 | \(L_uB_v[\psi Q_{\rm ef}]\) | \(1,\psi\); \(H_{v,+}-H_{v,-}\) | \(\mathrm d\mathfrak m_s\,\mathrm dL_u\,\mathrm dB_v\) | \(\Sigma_j\widehat\phi(v)\) | aggregate only |
| 3 | \(B_uL_v[\psi Q_{\rm ef}]\) | \(1,\psi\); \(H_{u,+}-H_{u,-}\) | \(\mathrm d\mathfrak m_s\,\mathrm dB_u\,\mathrm dL_v\) | \(\Sigma_j\widehat\phi(v)\) | aggregate only |
| 4 | \(B_uB_v[\psi Q_{\rm ef}]\) | \(1,\psi\); product orientation | \(\mathrm d\mathfrak m_s\,\mathrm dB_u\,\mathrm dB_v\) | \(\Sigma_j\widehat\phi(v)\) | aggregate only |
| 5 | \(L_uP_v[\psi Q_{\rm ef}]\) | \(1,\psi|_{v=0}\) | \(\mathrm d\mathfrak m_s\,\mathrm dL_u\); \(v\) consumed | \(\operatorname {Res}_{v=0}(\Sigma_j\widehat\phi Q_{\rm ef}^{\flat})\) | aggregate only; not a termwise physical module |
| 6 | \(B_uP_v[\psi Q_{\rm ef}]\) | \(1,\psi|_{v=0}\) | \(\mathrm d\mathfrak m_s\,\mathrm dB_u\); \(v\) consumed | same exact \(v\)-residue | aggregate only |
| 7 | \(P_uL_v[\psi Q_{\rm ef}]\) | \(1,\psi|_{u=0}\) | \(\mathrm d\mathfrak m_s\,\mathrm dL_v\); \(u\) consumed | \(\operatorname {Res}_{u=0}(\Sigma_jQ_{\rm ef}^{\flat})\widehat\phi(v)\) | aggregate only; not the Plemelj terminal |
| 8 | \(P_uB_v[\psi Q_{\rm ef}]\) | \(1,\psi|_{u=0}\) | \(\mathrm d\mathfrak m_s\,\mathrm dB_v\); \(u\) consumed | same exact \(u\)-residue | aggregate only |
| 9 | \(P_uP_v[\psi Q_{\rm ef}]\) | \(1,\psi(t)\); corner once | \(\mathrm d\mathfrak m_s\); \(u,v\) consumed | combined iterated/derivative coefficient | aggregate only; no second corner |
| 10 | \(\frac12L_uA_v[\psi'Q_{\rm ef}]\) | \(\frac12,\psi'\) | \(\mathrm d\mathfrak m_s\,\mathrm dL_u\,\mathrm dA_v\) | \(\Sigma_j\widehat\phi(v)\) | aggregate only |
| 11 | \(\frac12B_uA_v[\psi'Q_{\rm ef}]\) | \(\frac12,\psi'\) | \(\mathrm d\mathfrak m_s\,\mathrm dB_u\,\mathrm dA_v\) | \(\Sigma_j\widehat\phi(v)\) | aggregate only |
| 12 | \(\frac12P_uA_v[\psi'Q_{\rm ef}]\) | \(\frac12,\psi'|_{u=0}\) | \(\mathrm d\mathfrak m_s\,\mathrm dA_v\); \(u\) consumed | exact \(u\)-residue of \(\Sigma_j\) package | aggregate only; connector-axis cell |
| 13 | \(\frac12A_uL_v[\psi'Q_{\rm ef}]\) | \(\frac12,\psi'\) | \(\mathrm d\mathfrak m_s\,\mathrm dA_u\,\mathrm dL_v\) | \(\Sigma_j\widehat\phi(v)\) | aggregate only |
| 14 | \(\frac12A_uB_v[\psi'Q_{\rm ef}]\) | \(\frac12,\psi'\) | \(\mathrm d\mathfrak m_s\,\mathrm dA_u\,\mathrm dB_v\) | \(\Sigma_j\widehat\phi(v)\) | aggregate only |
| 15 | \(\frac12A_uP_v[\psi'Q_{\rm ef}]\) | \(\frac12,\psi'|_{v=0}\) | \(\mathrm d\mathfrak m_s\,\mathrm dA_u\); \(v\) consumed | exact \(v\)-residue of the full selector package | aggregate only; connector-axis cell |
| 16 | \(\frac14A_uA_v[\psi''Q_{\rm ef}]\) | \(\frac14,\psi''\), positive | \(\mathrm d\mathfrak m_s\,\mathrm dA_u\,\mathrm dA_v\) | full selector package \(\Sigma_j\widehat\phi(v)\) | aggregate only; indispensable mixed cell |

Here \(Q_{\rm ef}^{\flat}\) means the density with only the displayed
profile factor suppressed; it avoids duplicating the factors of (44.6).
Every row retains its actual \(D_j,H_j+1\), floors, \(\chi _4(q)\),
product equality, radial and profile stars, and collision convention.
No transfer creates a new star.  None of the sixteen rows owns the
external factor.  The unique owner is the complete recombined vector:

\[
 \mathscr E(Z)=-\frac4\pi X^{1/4}
 \Re\{e(1/8)Z\},
 \tag{44.9}
\]

applied once after the terminal and separately routed modules have been
assembled.

The exact positive-line compact functional may be written in the same
normalization as the accepted Round-37 physical-top density.  If
\({\cal B}_{0,s}\) is (44.6) with \(j=0\) and the factor \(u^{-1}\)
removed, and \({\cal B}_{\rm reg}\) is the sum of the
\(j=0\) regular top and all \(j\geq1\) profiles, then

\[
\begin{aligned}
 \mathfrak T_{\rm db}^{U,V,S}
 ={}&\frac1{2\pi}\int_{-V}^{V}\frac1{2\pi}\int_{-S}^{S}
 \bigg[
   {\bf P}_U\!\left\{\psi(\beta)\chi _0(\alpha)
             {\cal B}_{0,s}\right\}\\
 &\hspace{29mm}
 +\frac1{2\pi}\int_{-U}^{U}
   \psi(\beta)\chi _0(\alpha){\cal B}_{\rm reg}\,d\mu
 \bigg]dt\,d\nu,
\end{aligned}
\tag{44.10}
\]

\[
 {\bf P}_UH=\frac12H(0)-\frac{i}{2\pi}
  \operatorname {PV}\int_{-U}^{U}\frac{H(\mu)}{\mu}\,d\mu .
 \tag{44.11}
\]

Formula (44.10) displays the three, and only three, terminal selector
classes.  The half in (44.11) is the hard-top symmetric inversion value,
not a radial endpoint half-weight.

## Proof or derivation

At every fixed finite box, the accepted product identity gives

\[
 \sum_{k=1}^{16}{\cal C}_k[\psi Q_{\rm ef}]
   =R_uR_v[\psi Q_{\rm ef}],
 \tag{44.12}
\]

where the \({\cal C}_k\)'s are exactly the rows in the table.  The signs
follow from

\[
 \partial_\mu\psi(\beta)=\partial_\nu\psi(\beta)
 =-\frac12\psi'(\beta),\qquad
 \partial_\mu\partial_\nu\psi(\beta)
 =\frac14\psi''(\beta).
 \tag{44.13}
\]

Thus row 16 has positive coefficient \(1/4\).  Finite Fubini and the
common collision convention make (44.12) independent of transfer order.
Compact beta support has already made every transferred renormalized
radial side zero under the prescribed support separation.  Endpoint and
recombined \(R_1\)-arithmetic terms have already been routed only after
the three masks are summed, so no individual beta-masked row can be
identified with one of those physical modules.

The decisive accepted Round-37 step is then finite Stokes recombination:
all transferred faces, axes, first connectors, connector axes, the mixed
area, and the corner in (44.12) return to the original positive-\(a\),
positive-\(b\), fixed-\(w\) vertical.  Round 38 proves the required
outside-height Cauchy limit for that aggregate positive-line terminal and
its separately retained artificial package.  It does not prove sixteen
termwise limits.  Therefore (44.12), not a list of sixteen limiting
amplitudes, is the accepted ownership operation.

Now insert (44.2) only on the right side of (44.12).  Linearity gives the
finite exact identity

\[
\begin{aligned}
R_uR_v[\psi Q_{\rm ef}]
={}&R_uR_v[\psi\chi _0 Q_{\rm ef}]\\
&+R_uR_v[\psi(1-\chi _0)Q_{\rm ef}].
\end{aligned}
\tag{44.14}
\]

The first term is (44.3), and the second is the already accepted
large-alpha terminal package.  This split is made at finite height, so no
interchange of multiplication with an already-taken distributional limit
is being assumed.

For comparison, if one separately transfers both terms of (44.14), all
\(\chi _0'\) and \(\chi _0''\) cells cancel when the two alpha shares are
added, while the beta \(\psi'\) and \(\psi''\) cells re-form the full
sixteen-row left side of (44.12).  They then disappear only **as members
of the complete Stokes sum**, not termwise.  This explains simultaneously
why the packet correctly insists that the \(\psi''/4\) row must not be
dropped and why it is incorrect to demand a local compact-amplitude type
for that row.

Finally, (44.7) splits the positive-line density before the
\(a\downarrow0\) limit.  The \(u^{-1}\) part gives (44.11); the regular
top and interior profiles retain ordinary \(\mu\)-integration.  This is
exactly (44.10).  All scale, character, equality, floor, star, and
external-normalization data are scalar passengers through (44.12)--(44.14),
so their one-count ownership is unchanged.

## First doubtful or unproved step

There is no doubtful step in the aggregate identity (44.12), the
positive-line alpha split (44.14), or the three-selector decomposition
(44.10).  The first unproved step in the **requested** certificate is its
first rowwise promotion:

\[
 L_uL_v[\psi Q_{\rm ef}]
 \stackrel{?}{\longrightarrow}
 \text{an individually limiting compact amplitude type}.
 \tag{44.15}
\]

No accepted statement gives (44.15).  Row 1 lives on the transferred
final verticals, whereas (44.3) lives on the original positive lines.
Round 36 expressly forbids termwise masked physical-module limits, and
Rounds 37--38 prove only the Cauchy limit after the whole cell complex is
reassembled.  Inserting \(\chi _0\) into row 1 alone also changes the
Cauchy--Green derivative ledger and is not an identity with (44.3).
Therefore the demanded row-1 ownership is not merely unproved; it has the
wrong operator type.

After replacing that gate by (44.10), the first genuinely open
mathematical step is quantitative: prove the claimed polylogarithmic
value and one-\(x\)-derivative bound for the exact positive-line compact
functional, including any \(x\)-derivative of its fixed multiplier, under
a genuinely isolated rederivation.  This report proves the one-count
representation, not that analytic estimate.

## Required controls and outcomes

| control | outcome |
|---|---|
| sixteen-row count | **Pass at finite representation level.** The table has four boundary products, four boundary-axis cells, one corner, four connector-boundary cells, two connector-axis cells, and one mixed area. |
| beta mixed connector | **Pass.** Row 16 is exactly \(+\frac14A_uA_v[\psi''Q_{\rm ef}]\). It is retained until the full Stokes recombination and is never asserted zero. |
| top and interior selectors | **Pass on the actual compact object.** Equation (44.10) has \(\mathbf1_{j=0}u^{-1}\), \(\mathbf1_{j=0}\widehat W_{0,r}\), and \(\mathbf1_{j\ge1}\widehat W_j\), with Plemelj applied only to the first. |
| aggregate module scope | **Pass.** Endpoint/arithmetic physical modules are invoked only after global three-mask routing. No finite beta row is relabelled as an individual physical module. |
| central/large-alpha order | **Pass.** Alpha localization is (44.14), after (44.12); separate transferred alpha cells are not used. |
| same-mask artificial cancellation | **Pass.** The common \({\cal R}_\omega=R_1\) representation precedes coefficient extraction. Artificial/axial collisions use one local germ, and the separately owned \(\rho\)-package is not reinserted into (44.10). |
| connector/axis/collision/corner one-count | **Pass finitely and in the aggregate.** Residue rows consume their own measures, collisions use one combined coefficient, and row 9 is the unique corner. No termwise limiting assertion is made. |
| residual measure count | **Pass.** The table records the common \(s\)-measure and exactly which of the \(u,v\) contour, residue, or area measures remain; (44.10) independently displays all three positive-line Mellin factors. |
| floors, stars, and profiles | **Pass.** Every row inherits (44.5)--(44.8). No star is created at finite height; accepted inversion stars retain their original owners. |
| external factor once | **Pass.** Equation (44.9) is applied only after the aggregate terminal and separately owned modules are assembled. |
| rowwise \(\tau\) map | **Refuted.** Row 1 already lacks a separate physical-limit/compact identity, and the other fifteen are cells of the same aggregate representation. |

No numerical experiment, symbolic computation, web source, or external
theorem was used.  The task was 100% analytical/algebraic.

## Dependencies and exact artifacts

The derivation used these exact project artifacts:

1. `protocol.md`;
2. `state/proof_obligations.yml`, especially
   `M9-M1-beta-finite-two-axis-product-Cauchy-Green`,
   `M9-M1-beta-finite-prelimit-axial-vector-ledger`,
   `M9-M1-beta-global-aggregate-physical-module-routing`,
   `M9-M1-beta-endpoint-free-axial-remainder-limit`,
   `M9-M1-beta-mask-endpoint-axial-compatibility`, and
   `M9-M1-beta-large-alpha-transition-package-bound`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-beta-compact-selector-ownership/derivation_packet.md`;
5. `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/synthesis.md`;
6. `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/reports/blind_two_axis_connector_identity.md`;
7. `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/reports/actual_axial_connector_ledger_attack.md`;
8. `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/reviews/conductor_operator_tensor_calculus.md`;
9. `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/reviews/conductor_actual_stratum_schema.md`;
10. `rounds/codex-managed/m9-m1-beta-axial-side-exhaustion/synthesis.md`;
11. `rounds/codex-managed/m9-m1-beta-physical-module-transfer/synthesis.md`;
12. `rounds/codex-managed/m9-m1-beta-endpoint-free-axial-limit/synthesis.md`;
13. `rounds/codex-managed/m9-m1-beta-endpoint-free-axial-limit/reviews/conductor_remainder_operator_definition.md`;
14. `rounds/codex-managed/m9-m1-beta-endpoint-free-axial-limit/reports/endpoint_free_axial_limit_attack.md`;
15. `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/synthesis.md`;
16. `rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/synthesis.md`;
17. `rounds/codex-managed/m9-m1-beta-translation-divided-difference/synthesis.md`;
18. `rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/synthesis.md`;
19. `rounds/codex-managed/m9-m1-beta-double-bounded-cell/synthesis.md`;
20. `proofs/kernels/m9_m1_beta_double_bounded_cell_candidate.md`;
21. `rounds/codex-managed/m9-m1-beta-double-bounded-explicit-validation/synthesis.md`;
22. `rounds/codex-managed/m9-m1-beta-double-bounded-explicit-validation/reviews/conductor_ownership_table_gap.md`; and
23. `rounds/codex-managed/m9-m1-beta-compact-selector-ownership/briefs/actual_compact_table_constructor.md`.

No other Round-44 report was read.

## Recommended state effect

**Revise, with a promotable exact replacement after independent audit.**

1. Replace the open requirement
   `M9-M1-beta-compact-sixteen-stratum-selector-table` by an
   aggregate positive-line selector identity: the sixteen finite cells
   are retained and summed exactly to \(R_uR_v[\psi Q_{\rm ef}]\), after
   which the compact amplitude is (44.3)/(44.10).
2. Record the current demand for a separate \(\tau\)-type, alpha cutoff,
   and physical limit on each transferred row as rejected.  It conflicts
   with the already accepted aggregate-before-limit architecture.
3. Retain the finite sixteen-cell identity, including the
   \(+\psi''/4\) row, as proved representation algebra.  Do not delete or
   separately estimate that row.
4. Use exactly three compact terminal selectors: singular top at
   \(j=0\), regular top at \(j=0\), and interior at \(j\geq1\).  Keep
   all genuine endpoint, arithmetic, artificial, axial, collision, and
   corner modules under their existing separate one-count ownership.
5. Revise `M9-M1-beta-double-bounded-cell-bound` to depend on this
   aggregate positive-line identity rather than a sixteen-row local
   amplitude family.  Keep the bound open until the corrected functional
   receives a genuinely isolated analytic proof of its value and
   one-\(x\)-derivative estimates.
6. Do not promote the complete beta transition, M9-M1, M9, or the Gauss
   circle target from this algebraic correction alone.
