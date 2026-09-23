# Round 183 blind post-unmask and owner-scope review

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Round: `183`
- Review seam: `blind_post_unmask_small_t_seam` and `hard_parent_and_exponent_scope`
- Role: independent post-unmask reviewer
- Generated: `2026-08-27T20:00:15.0138303+08:00`
- Starting graph SHA-256:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Evidence status: review evidence only; no shared proof-state edit

## 1. Verdict

**GREEN.**  The blind report is cleanly isolated at the artifact level, its
coefficient-unknown no-go is reconciled exactly with the literal
primitive-ray result, and none of the three reports promotes a fixed-row,
correlation, adversarial-capacity, or partial-Mobius surrogate to the frozen
owner.  The narrow positive result is only the literal nonresonant
primitive-ray **incidence** sector.  Its exact incidence complement contains
the whole (t=1) face and remains unproved.

This verdict is for provenance, post-unmask consistency, and graph scope.
Promotion of the literal sector still requires the separate coefficient/BV
and endpoint seam to validate the claimed uniform variation bound (2.2) in
the discovery report.

## 2. Isolation check

The repository evidence supports statement-only isolation.

1. `state/active_campaign.yml` assigns
   `blind_complete_small_t_rederivation` access mode `statement_only`, names
   exactly `protocol.md` and `blind_statement.md`, and explicitly excludes
   the proof graph, campaign state, strategy, prior rounds, durable kernels,
   sources, siblings, reviews, controls, syntheses, and conductor analysis.
2. The blind report's dependency declaration names exactly those two
   permitted artifacts and affirmatively disclaims every excluded class.
3. A content scan finds no graph node ID, prior-round statement, literature
   theorem, PSC terminology, or sibling-specific primitive-ray result.  Its
   capacity, Mobius kernel, and row-correlation formulas are derived from the
   finite statement rather than cited from hidden context.
4. The agreement with the selected-context reports is explained by the
   common finite packet: flattening (hn=st^2), expanding
   (mu^2(s)), and applying van der Corput force the same identities.  The
   blind report does not contain the literal BV relation used only after
   unmasking.

The blind source packet has SHA-256
`34f6a52867853fcf279c158744dd7d9b560aafa0ae292b36e13c0777fb819e1c`;
the blind report reviewed has SHA-256
`3325a0229f10ddaf995fa31ddfe5644ec7d9677abc09b646d44ba5ec5c7ec79f`.
No contamination marker is present.

## 3. Exact agreement and disagreement

| Interface | Blind report | Literal discovery report | Barrier report | Adjudication |
|---|---|---|---|---|
| Exact scalar | Flattens the frozen sum to the literal incidence sum with phase (e(\sigma\sqrt{Xhn})). | Regroups the same incidences by (h=Gu,n=Gv), retaining one signed sum before the ray estimate. | Writes the same scalar as (\sum K_{L,T}(b,u)F_\sigma(bu^2)). | Exact coordinate changes of one scalar; agreement. |
| Coefficient-insensitive capacity | Exact arbitrary-array norm is the incidence count (\mathcal K(L)=L^{2+o(1)}), already (\asymp L^2) at (t=1), under a nondegenerate dyadic window. | Explicitly retains complete capacity (L^2X^\varepsilon); on the selected (G\ge G_0) sector the absolute incidence capacity is only (L^2/G_0=L^{7/4}). | Uses support/divisor envelopes only to bound transformed correction regions. | Compatible objects.  None is literal lower mass. |
| Literal saving | Cannot derive one because the packet withholds the formula and quantitative BV relation for (a_{L,X}^\sigma). | Supplies a new coefficient-sensitive relation: step-two BV on each primitive ray plus the actual (\chi_4(G)e(\sigma G\sqrt{Xuv})) progression. | Supplies no new literal cancellation estimate. | No contradiction: the literal report adds information deliberately unavailable to the blind rederiver. |
| Character in joint-(t) form | Factors (C(st^2)=\chi_4(s_{\rm o})A_s(t)) and correctly says that visible (\chi_4) alone supplies no free (t)-oscillation. | Finds (\chi_4(G)) inside the literal (t)-dependent amplitude after primitive-ray expansion. | Retains both characters in the quadratic shifted coefficient. | Agreement.  The literal (G)-oscillation lives inside the blind report's unknown (A_s(t)). |
| (t=1) control | Identifies the full capacity-size (t=1) row as the first missing literal relation. | Its successful sector has (G\ge\lceil L^{1/4}\rceil), while (t=1) forces (G=\rho=1); hence all (t=1) remains in the exact complement. | The kernel identity (K_{L,T}(b,1)=\mathbf1_{b>L}) retains the original (u=1) hard wave. | Exact agreement; the central face remains untouched. |
| Partial Mobius | Derives $\mathfrak m_L(b,u)=\sum_{a\mid u,\ a^2b>L,\ u/a<T}\mu(a)$; a target-scale tail is safe while the $a=1$ core remains. | Does not use Mobius to claim the sector. | Derives the identical kernel, proves the $a\ge T_L$ tail safe, and proves the $a<T_L$ core self-returns to the product wave modulo target size. | Exact agreement.  This refines a mechanism obstruction only. |
| Fixed-row correlation | Gives a sufficient condition with separate moduli (\sum_q|R_t(q)|), hence a strong rowwise route. | Claims no fixed-row theorem. | Gives the weaker sufficient signed Fejer-energy condition with one weighted real shift aggregate. | Different sufficient hypotheses, not disagreement.  Both are unproved and stronger than the complete owner because both end with triangle over (t). |
| Old PSC | Could not compare it under isolation and makes no such claim. | Does not invoke it. | Shows the fixed-row radical-shift correlation is not the old linear centered-fibre PSC and imports no theorem from it. | GREEN.  PSC remains open and is neither owner nor proved prerequisite here. |
| Divisor orientation/Mellin | Finds no support-preserving swap or off-central theorem in the finite packet. | Proves the one-prime transfer leaves the literal cone, so its signed difference self-returns rather than contracts. | Does not use Mellin to claim a gain. | Consistent no-go evidence, not a disproof of the literal owner. |
| State recommendation | Retain the complete owner open. | Promote only the strict literal incidence sector; retain its exact complement. | Refine only the small-(t) Mobius obstruction and retain correlation as conditional evidence. | Compatible after taking the narrowest effects, without voting. |

There is one harmless scope difference: the blind finite packet is stated
for (X>0), while the literal graph result is formulated on the project's
relevant range (X\ge2).  Since the blind report proves no target estimate,
this creates no promotion gap; any accepted sector statement must use the
literal (X\ge2) hypotheses.

## 4. First defective implication

No such implication is asserted by the three reports.  The first
implication that synthesis must reject is

\[
 |\mathcal A^{\rm ray,nr}_{L,X,\sigma}|
 \ll L^{3/2}X^\varepsilon
 \quad\not\Longrightarrow\quad
 |\mathcal A^{\rm st}_{L,X,\sigma}|
 \ll L^{3/2}X^\varepsilon .
\]

The missing exact complement is

\[
 \{G<G_0\}\ \cup\
 \{G\ge G_0:\Delta_X(u,v)<\delta_X\},
 \qquad G_0=\lceil L^{1/4}\rceil,
\]

with all literal predicates retained; it contains the whole (t=1) face.
Calling the proved piece a sector of whole ((s,t))-rows would also be
defective: it is a disjoint sector only after expanding the literal
divisor incidences.

Two earlier false implications are likewise rejected:

\[
 \mathcal K(L)=L^{2+o(1)}
 \quad\not\Longrightarrow\quad
 |\mathcal A^{\rm st}_{L,X,\sigma}|\gg L^{2-o(1)}
\]

for the fixed literal coefficient, and

\[
 \text{generic van der Corput connector}
 \quad\not\Longrightarrow\quad
 \text{the required literal correlation estimate}.
\]

The arbitrary complex-dechirped control chooses a different coefficient;
the correlation hypotheses are unproved rowwise conditions and cannot
replace the one-absolute-value owner.

## 5. Control outcomes

| Control | Outcome |
|---|---|
| Blind statement-only provenance | **PASS.** Exactly two declared inputs; no post-unmask content occurs in the blind report. |
| Adversarial capacity versus literal mass | **PASS.** The (L^2) norm is quarantined to arbitrary bounded arrays and support capacity. |
| Literal primitive-ray reconciliation | **PASS.** The new saving uses the actual character/phase and a coefficient BV relation unavailable in the blind packet. |
| Mandatory (t=1) face | **PASS/open.** All of it lies in (G<G_0) and remains unproved. |
| Exact complement | **PASS.** Nonresonant equality is assigned to the proved incidence sector; small-(G) and near-resonant incidences are the exhaustive complement. |
| Partial-Mobius owner substitution | **PASS/no-go.** The target-scale tail is safe, but the core contains (u=1) and self-returns. |
| Fixed-row owner substitution | **PASS/conditional only.** Both correlation formulations are sufficient rowwise inputs, strictly stronger than the frozen aggregate, and unproved. |
| Old PSC overlap | **PASS.** Similar missing power is only a diagnostic; no algebraic connector or theorem import is asserted. |
| Character-erased, unsigned, and dechirped controls | **PASS as falsifiers only.** They reject coefficient-uniform proofs but yield no literal lower bound. |
| One-site, one-fibre, and square-centre controls | **PASS.** None is used as positive literal mass; exact squares lie in (s\le L), outside the selected sector. |
| Hard signed-cone connector | **PASS/open.** The full small-(t) owner, not the strict incidence sector, is what combines with the Round-181 safe sectors. |
| Downstream and exponent quarantine | **PASS.** No downstream status or certified exponent changes. |

No computation or external theorem was used in this review.

## 6. Owner, downstream, and exponent audit

The exact graph consequences are as follows.

| Graph item | Round-183 effect allowed by these reports |
|---|---|
| `M9-M1-hard-top-squarefree-radical-sector-reduction` | Remains `proved_internal`; it supplies the prior safe sectors and exact complement. |
| `M9-M1-hard-top-high-radical-small-t-residual-estimate` | Remains **open**.  The proved primitive-ray incidence sector is proper and the remainder contains (t=1). |
| `M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction` | May be revised only by the exact small-(t), (a<T_L) self-return and target-safe (a\ge T_L) refinement.  This proves no analytic parent. |
| `M9-M1-shifted-divisor-correlation-PSC` | Remains **open** and unchanged in theorem status.  The new row correlation is a distinct sufficient condition, not PSC and not a necessary owner. |
| `M9-M1-top-endpoint-signed-cone` | Remains **open**.  It would follow only after the *complete* small-(t) estimate combines with the Round-181 sectors. |
| `M9-M1-direct-smooth-residual-blockwise-estimate` | Remains **open** and independent. |
| `M9-M1-physical-one-count-assembly` / `M9-M1` | The conditional assembly is unchanged; `M9-M1` remains **open** because both its hard and smooth analytic parents are not jointly closed. |
| `M9-M2`, its three analytic parents, and `M9-endpoint-uniformity` | No effect; all retain their current open scopes. |
| `M9` | Remains **open**. |
| `Conditional-bridge` | Remains `derived_under_assumptions`; its `M9` hypothesis is not discharged. |
| `GC-global-M1-alternative-bridge` and GAR | No effect.  A hard blockwise M1 incidence sector neither proves GAR nor bypasses M2. |
| `GC-target` | Remains **open**; the Gauss circle conjecture is not proved. |
| Certified exponents | Unchanged: internal (1/3); external Li--Yang (0.3144831759740614\ldots); target (1/4). |

Even a future proof of the full frozen aggregate would first close only the
hard signed cone after the accepted Round-181 sector reduction.  It would
not by itself close smooth M1, M9--M1, M2, endpoint uniformity, M9, either
bridge, or the quarter theorem.

## 7. Dependencies and narrowest state effect

Artifacts reviewed:

1. `protocol.md`;
2. `state/proof_obligations.yml` at starting hash
   `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/blind_statement.md`;
5. all three Round-183 reports;
6. `proofs/kernels/m9_m1_hard_top_squarefree_radical_reduction_and_self_return.md`;
7. `rounds/codex-managed/full-proof-round179-181-strategy-literature-review/synthesis.md`;
8. the assigned review brief.

The report hashes reviewed were:

- literal attack:
  `1f151b8f99a02d0f1bf6ad0e2a0a4a29c51b4ed1e4b56454cbee222c7b58b98c`;
- partial-Mobius/correlation barrier:
  `be91b8e17260b448a5eb254d359c1206fea75838a6b5f59f59e4db937b4cc330`;
- blind rederivation:
  `3325a0229f10ddaf995fa31ddfe5644ec7d9677abc09b646d44ba5ec5c7ec79f`.

The narrowest recommended patch is:

1. after the separate coefficient/endpoint reviews are GREEN, record one
   subordinate `proved_internal` strict **incidence-sector** lemma for
   (1.6)--(1.7) of the literal report, or equivalently append it as positive
   evidence to the still-open small-(t) owner;
2. record its exact small-(G)/near-resonant complement and make that
   complement, especially (t=1), the owner's next action;
3. refine the existing Mobius/Mellin obstruction only by the exact
   target-scale small-(t) self-return;
4. retain the fixed-row correlation as inconclusive conditional mechanism
   evidence; and
5. make no status, theorem, bridge, downstream, or exponent promotion.

If a new graph edge is used for the strict sector, it must be only a
conjunctive subordinate dependency of the open complete owner; it cannot
be an implication that closes that owner.  The compatible Round-183 exit
label is `strict_hard_m1_small_t_sector`.
