# Round 174 dependency, power, and selection seam review

## 1. Result

**Verdict: REPAIR.**  The dependency reconstruction, owner separations,
power ledgers, and choice of K26 as the sole proposed Round-175 frontier are
substantively sound on authoritative graph

\[
04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a.
\]

The graph was parsed mechanically: its 377 obligation identifiers are unique,
all dependency, blocker, and implication references resolve, and the only two
obligation nodes with an implication to `GC-target` are
`Conditional-bridge` and `GC-global-M1-alternative-bridge`.  They are lawful
alternatives.  The first uses blockwise M9; the second uses complete GAR as a
total-active-M1 theorem together with all of M9--M2.  GAR has no implication
to blockwise `M9-M1` or `M9`.

Two exact-statement repairs are nevertheless mandatory before the Round-175
objective is frozen.

1. Equation (174.N) in the full-graph report is not self-contained: it uses
   (F_R), (U_{k,\ell}^{(\epsilon)}), and the terminal index (K) without
   defining them.  It also leaves the interpolation function and Fourier
   convention implicit.  The blind report expressly made copying the exact
   formula, ranges, normalization, and endpoint conventions a pre-launch
   condition.  Thus (175.K26-chain) is presently an exact pointer to the
   Round-172 artifact, but not yet a literal frozen theorem in the Round-174
   report.
2. In the (W=Y^{7/16}) row, a saving of exactly
   (Y^{8/48}=Y^{1/6}) takes the current exponent (35/48) only to the
   threshold (27/48=9/16); it does not cross it.  A strict sub-(1/3)
   conclusion requires a bound (Y^{27/48-\delta}), equivalently a saving
   (Y^{1/6+\delta}) for some fixed (\delta>0), up to epsilon rebudgeting.

These are repairable specification and strict-inequality defects.  They do
not change the selected frontier, any graph edge, any status, or either
certified exponent.  No source claim in the sibling literature report is
adjudicated here.

## 2. Exact statement and hypotheses

### Complete quarter-proof trees

Write

\[
\mathcal I=\{\mathrm{H1\!-\!H3},\mathrm{H4},\mathrm{R5\!-\!Full}\}.
\]

The standard route is the conjunction

\[
\begin{aligned}
&\{\mathrm{M1\mbox{-}TOP}_{\rm direct},
   \mathrm{M1\mbox{-}SMOOTH}_{\rm direct}\}
   \Longrightarrow \mathrm{M9\!-\!M1},\\
&\{\mathrm{TOP},\mathrm{BAL}_{\rm crit},
   \mathrm{BAL}_{\rm rest},\mathrm{UNBAL}\}
   \Longrightarrow \mathrm{M9\!-\!M2},\\
&\mathcal I\wedge\mathrm{M9\!-\!M1}\wedge
  \mathrm{M9\!-\!M2}\wedge\mathrm{Endpoint}_{\rm std}
  \Longrightarrow\mathrm{M9}
  \Longrightarrow\mathrm{Conditional\mbox{-}bridge}
  \Longrightarrow\mathrm{GC\mbox{-}target}.
\end{aligned}
\tag{2.1}
\]

Its analytic open leaves, after following blockers to their first unproved
leaf, are:

- `M9-M1-top-endpoint-signed-cone`;
- `M9-M1-direct-smooth-residual-blockwise-estimate`;
- `M9-M2-top-endpoint-density-discrepancy-energy`;
- `M9-M2-balanced-double-far-oscillatory-remainder`, equivalently the
  critical actual energy modulo the proved phase-free term;
- `M9-M2-balanced-remaining-label-owner-quantifier-completion`; and
- `M9-M2-smooth-unbalanced-three-quarter-estimate`.

`M9-endpoint-uniformity` is a separate validation/assembly seam blocked by
the same five standard analytic parents (counting full BAL as one parent);
it creates no missing cancellation by itself.  The full-graph report's
displayed `BAL_crit` and `BAL_rest` split is therefore essential and correct.
Round 171 concerns only the persistent critical (j=1) child; it does not
cover noncritical (j=1) scales, the exact-square (j=2,K/L=16) boundary,
or other remaining balanced labels.

The alternative route is

\[
\begin{aligned}
&\mathrm{LOWER}_{\rm radial}
  \wedge\mathrm{INTERFACE}_{\rm radial}
  \wedge\mathrm{NONLOWER}_{\rm terminal}
  \Longrightarrow\mathrm{GAR}
  \Longrightarrow\mathrm{M1}_{\rm total},\\
&\{\mathrm{TOP},\mathrm{BAL}_{\rm crit},
  \mathrm{BAL}_{\rm rest},\mathrm{UNBAL}\}
  \Longrightarrow\mathrm{M9\!-\!M2},\\
&\mathcal I\wedge\mathrm{M1}_{\rm total}\wedge
  \mathrm{M9\!-\!M2}
  \Longrightarrow\mathrm{GC\mbox{-}global\mbox{-}M1
  \mbox{-}alternative\mbox{-}bridge}
  \Longrightarrow\mathrm{GC\mbox{-}target}.
\end{aligned}
\tag{2.2}
\]

The interface and nonlower terminal pieces are proved.  The sole open GAR
leaf is `M9-M1-global-lower-radial-signed-estimate`.  The M2 leaves are the
same TOP, two BAL scopes, and UNBAL leaves as in (2.1), with their own hard
endpoint and real-centre quantifiers.  Hence the accepted top-level logic is

\[
\mathrm{GC\mbox{-}target}\quad\Leftarrow\quad
\mathsf T_{\rm std}\ \mathbf{OR}\ \mathsf T_{\rm GAR},
\tag{2.3}
\]

not a conjunction and not permission to move a local owner between trees.

### Literal repair of the proposed K26 theorem

The following is the minimum self-contained freeze required by the accepted
Round-172 formulas.  Let (X) be large and real,
(J=\sqrt X), (1\ll L\ll H\le J^{1/2}),
(R_0=\lceil L\rceil), and let (M=M_L\in\mathbb N),
(M\asymp L^2), be the exact length of the containing interval on which the
accepted residual coefficient is zero-extended.  Retain

\[
c_N^{\rm rem}
=\sum_{\substack{d\mid N\\d\ {\rm odd}}}
  \chi_4(d)\lambda_N(d),\qquad
z_N=c_N^{\rm rem}e(J\sqrt N),\qquad
D_L=\sum_N|z_N|^2\ll_\varepsilon L^2X^\varepsilon,
\tag{2.4}
\]

where (\lambda_N(d)) is exactly the accepted literal residual incidence
coefficient, including its selector/no-pair value, squarefree and
coprimality masks, two-adic branch, Vaaler/profile factor, floors, stars,
support crossings, endpoint values, and zero-extension values.

Define (K) and the stopped chain by

\[
R_{j+1}=\min(2R_j,M)\quad(0\le j<K),\qquad R_K=M,
\tag{2.5}
\]

with (K) minimal.  Thus the final link is retained when
(R_{K-1}<M<2R_{K-1}).  Put

\[
F_R(\theta)=\sum_{|r|<R}
 \left(1-\frac{|r|}{R}\right)e(r\theta),
\qquad B_{R,S}=F_S-F_R.
\tag{2.6}
\]

Fix once and for all a real
(\varphi\in C_c^\infty((-1/2,1/2))) with (\varphi(0)=1).  For the
absolute-parity branch (\eta\in\{0,1\}), set

\[
\begin{aligned}
\mathcal W_\eta(x,y)
 &=\sum_{\substack{d,m\ge1\\d\ {\rm odd}}}
   (-1)^{\eta m}\lambda_{dm}(d)
   \varphi(x-d)\varphi(y-m),\\
\mathcal B_{\eta,\theta}(x,y)
 &=\mathcal W_\eta(x,y)e(J\sqrt{xy}+\theta xy),\\
\widetilde{\mathcal B}_{\eta,\theta}(\xi,\nu)
 &=\iint_{\mathbb R^2}\mathcal B_{\eta,\theta}(x,y)
   e(-\xi x-\nu y)\,dx\,dy,\\
U_{k,\ell}^{(\eta)}(\theta)
 &=\widetilde{\mathcal B}_{\eta,\theta}(k/4,\ell).
\end{aligned}
\tag{2.7}
\]

For integer (R<S\le2R), define the complete nonzero ordinary-frequency
link by

\[
\begin{aligned}
\mathcal N_{R,S}={1\over8}\Re\sum_{\eta=0}^1
&\sum_{\substack{k,k'\in\mathbb Z\\k,k'\ {\rm odd}}}
 \sum_{\substack{\ell,\ell'\in\mathbb Z\\\ell,\ell'\ne0}}
 \chi_4(k)\chi_4(k')\\
&\times\int_0^1B_{R,S}(\theta)
 U_{k,\ell}^{(\eta)}(\theta)
 \overline{U_{k',\ell'}^{(\eta)}(\theta)}\,d\theta.
\end{aligned}
\tag{2.8}
\]

The sole proposed Round-175 inequality can then be frozen literally as

\[
\boxed{
\sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
\ll_\varepsilon L^3X^\varepsilon .}
\tag{R175.K26}
\]

This is one-sided: there is no absolute value around the displayed sum.
Both centred parity peaks, all cardinal cells, all arithmetic openings,
both ordinary frequencies, every endpoint and transition, and the final
strict link remain inside one outer real part.  A whole-sum absolute bound or
uniform linkwise signed bound would be stronger sufficient statements, not
the frozen requirement.

## 3. Proof or derivation

### Dependency and owner audit

The standard physical one-count assemblies have exactly the two direct M1
and three M2 analytic parents recorded in the report.  Full BAL itself has
two independent blockers.  Following the blocker graph gives precisely the
six standard open leaves listed in Section 2.  `Conditional-bridge` then has
only M9 open.

On the alternative side, the proved
`M9-M1-GAR-total-active-equivalence` has an implication only to
`GC-global-M1-alternative-bridge`.  Complete GAR is open only through the
global lower-radial signed estimate, while the alternative bridge also
requires the unchanged blockwise M9--M2 conjunction.  This proves the OR and
the direct-M1-versus-GAR noninterchangeability.

K17a and K26 are alternative sufficient estimates inside the residual
(t=1) subroute.  The full displayed (t=1) scalar is broader, but still
does not include the other (t=1) and few-point channels, collision collars,
or the complete hard-TOP parent.  None of these three residual/(t=1)
frontiers may replace TOP in either quarter tree.

### Target and capacity audit

Here “capacity” is an accepted coefficient-insensitive positive or absolute
upper ledger, not physical lower mass.

| Frontier | Target | Accepted capacity | Missing power and lawful effect |
|---|---:|---:|---|
| K26 whole chain | (L^3X^\varepsilon) | (MD_L\ll L^4X^\varepsilon) | (L); closes at most the K26 residual route |
| K17a non-polylogarithmic determinant range | (L^2X^\varepsilon) | (\|T\|\|u\|_2^2\ll L^3X^\varepsilon) | (L); closes the alternative residual route only |
| Full displayed (t=1) scalar | (L^{3/2}X^\varepsilon) | raw (L^2); favorable comparator (\min(L^2,\sqrt{JL})), with a separate structural (\sqrt J) loss in the fixed-angular mean-square placement | at least the displayed (\min(L^{1/2},H/L+O(L^{-1}))) factor on that comparator; closes only the full (t=1) face |
| Complete hard TOP | scalar (L^{3/2}), equivalently energy or completed real part (L^2) modulo proved terms | scalar (L^2), energy (L^3), or density (L^2\sqrt\rho) | (L^{1/2}), (L), or (\rho^{1/2}); closes TOP only |
| Critical BAL | (L^3X^\varepsilon) energy/remainder | (L^4X^\varepsilon) | (L); leaves `BAL_rest` |
| Remaining-label BAL | (L^{3/2}X^\varepsilon) per literal block | (L^2X^\varepsilon) | (L^{1/2}), worst (X^{1/12}) at (L\asymp X^{1/6}); leaves critical BAL |
| UNBAL | (M^{3/4}X^\varepsilon), (M=LK), (K/L>16) | (M X^\varepsilon) | (M^{1/4}); closes UNBAL only |
| Direct hard M1 | normalized (L^{3/2}X^\varepsilon), hence physical (X^{1/4+\varepsilon}) | normalized (L^2), hence physical (X^{1/4}L^{1/2}) | (L^{1/2}=X^{1/12}) at the critical scale; leaves smooth M1 |
| Direct smooth M1 | (X^{1/4+\varepsilon}) on every literal smooth label | (X^{1/3+o(1)}) on the first critical profile | (X^{1/12}); leaves hard M1 |
| Complete GAR lower owner | (G_X[V_{\rm low}]\ll X^\varepsilon), equivalently scalar (R) or squared residual (y), (R=X^{1/4},y\asymp R^2) | scalar (R^2), squared residual (y^2); deepest root-defect face raw (M) | (R), (y), or (M^{1/4}); only the complete all-layer lower theorem closes GAR |
| Generic local-moment lane | cluster (Y^{1/2+\varepsilon}) at (W=Y^\alpha), (1/3<\alpha<1/2) | no complete target bound | would give (1/6+\alpha/3), not a quarter-tree node |
| (W=Y^{7/16}) determinant lane | (Y^{24/48+\varepsilon}) | coefficient-blind (Y^{43/48}); best complete (Y^{35/48}) | (Y^{11/48}) to target; a **strictly greater** than (Y^{8/48}) saving is needed to cross below (1/3); target gives (5/16) |
| Endpoint uniformity | uniform validity of the five standard parents | no independent capacity | assembly seam only |

The determinant threshold follows from the accepted connector

\[
\Theta(\beta)=
\max\left\{\frac{7/16+\beta}{3},\frac\beta2\right\}.
\tag{3.1}
\]

Thus (\Theta(9/16)=1/3), while
(\Theta(1/2)=5/16).  This establishes the strict-threshold repair in
Section 1.  All other displayed powers in the two strategy reports agree
with the graph and the Round-171--173 ledgers.

### Selection and mechanism audit

The two strategy reports independently rank the same frontier first.  The
blind report conditions launch on a literal formula freeze; the full-graph
report supplies the correct Round-172 coefficient (1/8), one outer real
part, nonzero ordinary-frequency ranges, both parity branches, stopped
chain, and strict terminal link, but needs the definitions in (2.4)--(2.8)
to complete that freeze.

The selected objective is genuinely different from both parked routes:

- it does not take a coefficient-uniform positive norm over links, modes,
  cells, openings, or frequencies, the route whose sharp available capacity
  is (L^4X^\varepsilon);
- it does not form the Round-173 tangent first difference, its adjoint, or a
  second Abel primitive, whose actual-symbol complement returns exactly to
  K26 modulo target-safe terms; and
- it estimates the original whole stopped-chain signed aggregate and permits
  cancellation between links before any modulus.

This is a lawful new theorem class, not evidence that such cancellation
exists.  A linkwise actual-symbol theorem would be a stronger proof of the
same frozen inequality, but coefficient-uniform linkwise positivity remains
excluded.

The promotion gate, six false controls, first-failure stop rule, ban on an
in-round pivot, and downstream-scope guard are all present and correctly
limited.  After a successful proof and independent seam validation, the
largest immediate effect is a residual/K26 lemma.  Full (t=1), TOP, both
BAL scopes, UNBAL, M9--M2, both direct M1 parents or complete GAR, endpoint
assembly, both quarter bridges, the quarter theorem, and both exponent
ledgers remain unchanged.

## 4. First doubtful or unproved step

The first unsupported statement in document order is the claim that the
displayed Round-175 target is already literal and exact.  At (174.N), the
symbols (F_R) and (U_{k,\ell}^{(\epsilon)}) and the stopping index (K)
are not locally defined.  The cited Round-172 kernel supplies them, so this
is not a mathematical contradiction, but it fails the blind report's
mandatory pre-launch freeze and the campaign's “literal statement” gate.
Equations (2.4)--(2.8) are the exact repair.

The first incorrect power wording occurs later in the determinant row:
exactly (Y^{8/48}) of saving reaches, rather than crosses, the
(Y^{27/48}) threshold.  Replace “to cross” by “to reach,” and state that a
strictly larger power saving is required for a strict sub-(1/3) theorem.

After those repairs, the first genuinely unproved mathematical step is
precisely (R175.K26): no accepted theorem saves a factor (L) on the
complete literal nonzero-frequency stopped-chain aggregate.  No accepted
identity proves simultaneous cancellation across (j,k,k',\ell,\ell'),
cardinal cells, arithmetic openings, endpoints, and transitions.  Naming a
“whole-chain actual-symbol correlation” does not prove it.

## 5. Required control test and outcome

| Required control | Outcome |
|---|---|
| `authoritative_dependency_tree` | **GREEN.** All references resolve; both complete trees and all open mandatory leaves are correctly identified. |
| `standard_vs_GAR_logical_or` | **GREEN.** Exactly two accepted implications reach `GC-target`; GAR has no blockwise M1 or M9 implication. |
| `Round171_BAL_scope` | **GREEN.** Critical (j=1) and remaining-label BAL are separate mandatory scopes. |
| `Round172_transform_scope` | **REPAIR.** Constants, parities, zero-sector scope, and strict link are correct, but the selected theorem must copy the missing definitions and ranges. |
| `Round173_self_return_scope` | **GREEN.** The proposed target uses neither first difference nor its adjoint/second-Abel continuation. |
| `full_t1_vs_K17a_vs_K26` | **GREEN.** K17a and K26 are residual alternatives; full (t=1) is broader; none is TOP. |
| `residual_vs_full_hard_TOP_scope` | **GREEN.** No residual estimate is substituted for the hard-TOP parent. |
| `critical_vs_remaining_BAL_scope` | **GREEN.** Neither BAL child is allowed to imply the other. |
| `BAL_UNBAL_independence` | **GREEN.** Both remain mandatory independent M2 parents. |
| `direct_M1_vs_GAR_scope` | **GREEN.** Direct hard and smooth M1 occur only on the standard route; GAR occurs only through the alternative total-M1 bridge. |
| `endpoint_assembly_scope` | **GREEN.** Endpoint uniformity inherits the analytic parents and is not treated as a cancellation theorem. |
| `power_margin_and_global_exponent_connector` | **REPAIR.** All target/capacity ratios pass except the word “cross” at the exact (9/16) threshold. |
| `rejected_mechanism_bypass` | **GREEN at selection scope, unproved analytically.** The target preserves the literal whole sum and excludes positive and tangent-self-return proofs. |
| `single_Round175_objective` | **GREEN after formula freeze.** There is one inequality only, (R175.K26). |
| `literal_promotion_gate` | **GREEN after formula freeze.** It requires exact coefficient, parity, (i/2), (1/8), terminal link, one short correction, zero-sector recombination, endpoints, missing power, and independent reviews. |
| `false_controls` | **GREEN as vetoes, not proofs.** The dechirped one-parity, one-site, positive-character/no-pair, parity/endpoint, rank-one-centre, and literal-endpoint controls are all retained. |
| `stop_rule_and_no_pivot` | **GREEN.** A first literal, normalization, endpoint, restored-power, positive, self-return, or rank-one failure stops the round; no fallback frontier is licensed. |
| `limited_downstream_effect` | **GREEN.** Success reaches at most the residual/K26 face and changes no parent or exponent automatically. |
| `no_status_or_exponent_overpromotion` | **GREEN.** Internal (1/3), external (0.3144831759740614\ldots), and target (1/4) remain distinct. |

No numerical experiment was used.  The review is entirely algebraic,
graph-theoretic, and power-ledger based.

## 6. Dependencies and exact artifacts used

The review used the following artifacts:

- `protocol.md`;
- `state/proof_obligations.yml`, parsed at the SHA-256 above;
- `state/active_campaign.yml`;
- `strategy/round174_full_proof_strategy_current_literature_review.md`;
- all three Round-174 reports in
  `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reports/`;
- `rounds/codex-managed/m9-m2-balanced-critical-j1-two-defect-commutator-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate/synthesis.md`; and
- `proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md` for the exact definitions in (2.4)--(2.8).

The sibling current-primary-literature report was read as required by the
brief, but its source certifications were deliberately not re-reviewed in
this dependency/power/selection seam.  No web source or source-card theorem
is used to certify the present verdict.

## 7. Recommended state effect

**Recommended state effect: retain / no graph change, after exact report-level
repairs.**

Apply these repairs before the Round-174 synthesis freezes a successor:

1. replace the schematic target definition by (2.4)--(2.8), or copy those
   definitions verbatim into the eventual Round-175 brief, including
   (R_K=M), the strict final link, the Fejer normalization, interpolation,
   Fourier convention, all integer ranges, and the exact residual
   coefficient reference;
2. state explicitly that (R175.K26) is one-sided and uniform on the entire
   frozen (X,J,L,H,M) and literal-label range;
3. call it target-equivalent to K26 **modulo** the proved once-only short
   correction and collectively recombined ordinary-zero-containing sector,
   rather than leaving that equivalence implicit;
4. replace the determinant-row claim of a (Y^{1/6}) saving “to cross” the
   sub-(1/3) threshold by: (Y^{1/6}) reaches the threshold, and a strict
   (Y^{1/6+\delta}) saving is required to cross it; and
5. retain the existing promotion gate, false controls, stop rule, no-pivot
   rule, and narrow downstream effect without weakening them.

After these repairs, retain (R175.K26) as the unique proposed Round-175
inequality and retain the terminal strategy label
`strategy_frontier_retained`.  This review licenses no State Patch, no proof
promotion, no exponent change, no source promotion, and no start of
Round 175.
