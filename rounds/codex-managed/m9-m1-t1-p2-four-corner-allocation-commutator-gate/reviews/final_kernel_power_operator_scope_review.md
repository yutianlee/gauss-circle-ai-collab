# Round 197 final-kernel power/operator/scope review

- Campaign: m9-m1-t1-p2-four-corner-allocation-commutator-gate
- Role: independent durable-kernel power/operator/scope review
- Starting graph SHA-256:
  b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae
- Durable kernel SHA-256:
  d3d6ac897e8a193be83820136eab28d0b55eaff030351d060e72b4524d413cc9
- Numerical theorem evidence: none

## 1. Result

**PASS.**  The durable kernel is power/operator equivalent to the final
formal candidate.  A direct full-file comparison shows that its
mathematical body, equations (197.C1)--(197.C37), dependencies, scope,
and proposed state effect are byte-for-byte identical to the final
candidate.  The only substantive text difference is the expected
wrapper change from “Formal candidate” to “Proof kernel” and the status
sentence stating that graph acceptance still requires a valid State
Patch.

The kernel proves exactly the two narrow estimates

\[
 |\mathscr R_{\rm core,out}^\sigma(P_{\rm cc}W)|
 \ll_{B,C_0,K_{\rm sel},\varepsilon}L^2X^\varepsilon,
\]

\[
 |\mathscr R_{\rm open,out}^\sigma(P_{\rm cc}W)|
 \ll_{B,C_0,K_{\rm sel},\varepsilon}L^2X^\varepsilon.
\]

Its complete power ledger is correct:

\[
 D_L\sum_{\kappa\ll L}(1+L/\kappa)^2
 \ll D_LL^2X^\varepsilon,
\]

\[
 {D_L\over L}\,D_LL^2X^\varepsilon
 =D_L^2LX^\varepsilon
 \ll L^2X^\varepsilon,
\]

and the normalized-BV term has the same final power.  The selector
exception is confined to a \(K_{\rm sel}\)-dependent bounded set of
shells.  The complete masked outer passage, cap/open subtraction, one
outer real part, exact physical complement, aligned-face quarantine, and
strict scope are all retained without weakening or expansion.

## 2. Exact statement and hypotheses

Fix real \(X\ge2\), a nonempty literal middle or lower hard-M1 shell
\(L\ge2\), \(\sigma\in\{\pm1\}\), and fixed
\(B>0\), \(K_{\rm sel}>0\), \(C_0\ge2\).  Put

\[
 H_B=\lfloor(\log(2X))^B\rfloor,\qquad
 R_0=\lceil L\rceil,\qquad D_L=\lceil\sqrt L\rceil.
\]

Use the literal total zero-extended endpoint \(\lambda_{N,\sigma}\), the
physical atom \(W\) in (197.C9a), and

\[
 P_{\rm cc}
 =P_2\mathbf1_{(m,\beta)=1}
       \mathbf1_{\chi_4(\alpha m)=-1}C_{\rm lit}.
\]

Here \(C_{\rm lit}\) is equality of the arithmetic/live sharp code
(197.C8a)--(197.C8c).  The code records actual branch, cell, and trace
labels but not smooth values, \(\eta_L\), \(\rho_N\), or accidental
coefficient nonvanishing.  Those moving values are treated by the exact
three-term rule (197.C22d).

The accepted inputs used by the kernel are:

1. K184.4 and K184.11--K184.16 for the selector and actual literal
   smooth/BV factorization;
2. K185.1--K185.7 and K185.18--K185.27 for the zero-extended physical
   source, primitive charts, and monotone/low-height exit estimate;
3. 193.C13 and 193.C19b--193.C21 for finite \(g\) and physical-mask
   transport through the exact core; and
4. 195.C14--195.C20b for the fixed-\(\kappa\) count, masked replay,
   fixed-to-outer ledger, and safe/open packet split.

No new external theorem, numerical input, nonemptiness claim, or
coefficient-mass assertion occurs in the durable kernel.

## 3. Proof and equivalence verification

### 3.1 Candidate-to-kernel equivalence

The final candidate has SHA-256
285ea0975eb3d48691ffb27b5a83e251d33a68062eb4d14dd54972f6af6296c0.
The durable kernel has SHA-256
d3d6ac897e8a193be83820136eab28d0b55eaff030351d060e72b4524d413cc9.

A full no-index diff has exactly two content changes:

1. the title changes from “Formal candidate” to “Proof kernel”; and
2. the candidate-status sentence is replaced by the durable-kernel
   status sentence.

There is also one terminal blank line.  No theorem hypothesis,
definition, formula, bound, constant, dependency, complement, scope
sentence, or proposed state effect differs.  Therefore every completed
candidate seam review transfers to the kernel without a mathematical
gap.

### 3.2 Exact \(D_L\) ledger

For fixed inward cross gcd \(\kappa\), lower closeness gives
\(O(D_L)\) choices of the moving close variable.  The height equation
then gives \(O(1)\) choices of its mate over the complete Fejer range,
while \(U,v\) each have \(O(1+L/\kappa)\) choices.  Both orientations
cost only a constant.  Hence

\[
 \mathcal C_\kappa\ll D_L(1+L/\kappa)^2
\]

and

\[
\begin{aligned}
 \sum_{\kappa\ll L}\mathcal C_\kappa
 &\ll D_L\sum_{\kappa\ll L}
     \left(1+{2L\over\kappa}+{L^2\over\kappa^2}\right)\\
 &\ll D_L\{L+L\log(2L)+L^2\}
 \ll D_LL^2X^\varepsilon.
\end{aligned}
\]

There is no additional \(Y\), row, orientation, anchor, or frequency
factor.  Independently, \(O(LD_L)\) close lower pairs and

\[
 \sum_{0<r<R_0}\tau(N+r)\ll_\varepsilon LX^\varepsilon
\]

upper completions reproduce the same raw count.

On one common live cell,

\[
 a^{\rm lit}(u,v)
 =K_{\rm sharp}\eta_L(u)b^{\rm sm}(u,v),
\]

and the two lower inputs are \(O(D_L)\) apart.  The accepted
scale-normalized \(C^1\) bound gives

\[
 |b^{\rm sm}(m,g\alpha)-b^{\rm sm}(\alpha,gm)|
 \ll_\varepsilon {D_L\over L}X^\varepsilon.
\]

Multiplication by the raw count gives
\(D_L^2LX^\varepsilon\).  Since
\(D_L=\lceil\sqrt L\rceil\) and \(L\ge2\),
\(D_L^2\le4L\), so this is \(O(L^2X^\varepsilon)\).

For the BV term, a fixed increment is crossed by \(O(D_L^2)\) ordered
close pairs.  The finite \(g\le G_0\) multiplicity is uniform, and the
\(O(LX^\varepsilon)\) upper completions give

\[
 D_L^2\operatorname{Var}(\eta_L)\,
 LX^\varepsilon
 \ll L^2X^\varepsilon.
\]

The exact product rule (197.C22d) shows that the smooth, BV, and selector
terms exhaust the actual coefficient difference.  Fresh epsilon
rebudgeting absorbs only finite products, divisor losses, and logarithms;
no positive power is hidden.

### 3.3 Selector bounded-shell control

The selector truth table is \((1,0,0,1)\).  Under the lower swap, a
selected prime outside \(g\) is complemented and a selected prime in
\(g\) remains on the character leg.  The selector can change only when
exactly one selected prime divides \(g\).

Lower closeness and the strict cone give \(g\le G_0\), with \(G_0\)
absolute.  For distinct primes,

\[
 \delta_{G_0}
 =\min_{\substack{p\le G_0\ {\rm prime}\\q\ne p\ {\rm prime}}}
 |\log(q/p)|>0.
\]

The selected-pair condition gives
\(|\log(q_N/p_N)|\le K_{\rm sel}L^{-1/2}\).  Therefore the selector
commutator vanishes whenever
\(K_{\rm sel}L^{-1/2}<\delta_{G_0}\).  On the remaining bounded set of
shells, \(D_L=O_{K_{\rm sel},G_0}(1)\), so the raw
\(D_LL^2X^\varepsilon\) count is already
\(O_{K_{\rm sel},\varepsilon}(L^2X^\varepsilon)\).

This exactly accounts for the displayed \(K_{\rm sel}\) dependence.
\(B\) pays the low-height/polylogarithmic ledger and \(C_0\) the fixed
Farey projector.  All other suppressed constants are fixed structural
data of the accepted transform.

### 3.4 Masked outer passage

The kernel applies \(P_{\rm cc}\) to the physical parent (197.C9a) before
Fourier, height, anchor, Farey, or packet operations.  Equations
(197.C9d)--(197.C9g) retain the exact fixed packet, band label, centered
inverse, \(T=0\) convention, and all simultaneous strict \(T\ge1\)
conditions.

The outer map \(\mathcal O_{195}^\sigma\) restores the
\(\mathfrak m^{-1}\) lift, anchor, band, divisor, shell, dyadic,
orientation, and zero-extension data without taking a modulus at a
fixed component.  Equations (197.C9h)--(197.C9k) therefore give the exact
linear cap/open partition of the same recomputed masked core.

The typed identity

\[
 \mathscr R_{\rm core,out}^\sigma(MW)
 =\mathscr H_{\rm out}^\sigma(MW)
  -\mathscr S_{\le192,\rm out}^\sigma(MW)
\]

retains the complete opposing physical source after accepted
monotone/low-\(h\) exits and recomputes every Round-187--Round-192 safe
projector on \(MW\).  The transported mask commutator, births, deaths,
carries, unequal translations, cells, crossings, phases, anchors, both
\(T\) branches, and zero extensions remain in the core.

The Round-185 exit bound and deletion-stable Round-193/Round-195 safe
aggregate prove the full core estimate.  Only afterward is the
Round-195 safe packet union subtracted.  The packet condition is never
inserted into the allocation orbit.  One real part is taken only after
the complete complex outer assembly.

### 3.5 Complement, no-go, and scope

The first-failure partition

\[
 P_2=P_{\rm cc}\ \dot\cup\ P_{\partial\rm lit}
       \ \dot\cup\ P_{s\rm f}\ \dot\cup\ P_{g\rm f}
\]

is unchanged and exact.  Only \(P_{\rm cc}\) is proved safe.

For \(\alpha\ne m\),

\[
 \left({g\alpha\over m}-g\right)
 \left({gm\over\alpha}-g\right)
 =-{g^2(\alpha-m)^2\over\alpha m}<0.
\]

Thus an aligned sharp ratio face may be crossed by all
\(O(LD_L)\) lower pairs.  Upper completion restores the full
\(D_LL^2X^\varepsilon\) capacity.  The kernel correctly infers neither
literal nonvanishing nor lower mass and claims no automatic
\(O(D_L^2)\) collar.

The kernel proves neither full \(P_0\), complete \(P_2\), \(P_1\), the
complete original \(t=1\) residual, the hard small-\(t\) owner, either
M1 parent, GAR, any M2 parent, endpoint uniformity, M9, a bridge, nor the
Gauss-circle target.  It changes no exponent.

## 4. First doubtful or unproved step

There is no doubtful candidate-to-kernel transcription or power/operator
step.  The first unproved step remains a target bound for

\[
 P_{\partial\rm lit}\ \dot\cup\ P_{s\rm f}\ \dot\cup\ P_{g\rm f}
\]

inside the Round-195 open packet region.  The aligned-face calculation
shows why the common-cell method alone cannot supply it.  Any extension
would require a new literal transversality/continuity theorem or a
different signed mechanism.  The current \(D_LL^2\) statement is only an
upper-capacity obstruction.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Full candidate-kernel diff | **PASS.** Mathematical bodies are identical; only title/status wrapper and terminal blank line differ. |
| Raw \(\kappa\)-sum | **PASS.** \(D_L\sum_\kappa(1+L/\kappa)^2\ll D_LL^2X^\varepsilon\). |
| Independent lower/upper count | **PASS.** \(O(LD_L)\) lower pairs times \(O(LX^\varepsilon)\) upper completions. |
| Smooth power | **PASS.** \(D_L/L\) reduces raw capacity to \(D_L^2L\ll L^2\). |
| BV power | **PASS.** \(O(D_L^2)\) increment multiplicity times \(O(L)\) upper completion is target-safe. |
| Selector | **PASS.** Large shells have zero commutator; bounded shells are paid with \(K_{\rm sel}\)-dependent constant. |
| Physical-mask timing | **PASS.** Mask precedes every spectral operation. |
| Farey/core typing | **PASS.** Band, \(T=0\), simultaneous \(T\ge1\), lift, and outer weights are retained. |
| Masked source/safe subtraction | **PASS.** The exact \(\mathscr H_{\rm out}-\mathscr S_{\le192,\rm out}\) identity is present. |
| Cap/open subtraction | **PASS.** It is an exact partition of the same masked core after physical pairing. |
| One outer real part | **PASS.** No separate component norm replaces the claimant. |
| Complement and aligned face | **PASS.** Complement is exact and full-capacity face terms remain quarantined without a mass inference. |
| Scope | **PASS.** Only the subordinate \(P_{\rm cc}\) sector is claimed; all parents and exponents remain unchanged. |

## 6. Dependencies and exact artifacts used

The durable kernel was read completely:

- proofs/kernels/m9_m1_hard_top_t1_p2_common_cell_allocation_commutator_sector.md,
  SHA-256
  d3d6ac897e8a193be83820136eab28d0b55eaff030351d060e72b4524d413cc9.

It was compared in full with:

- rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md,
  SHA-256
  285ea0975eb3d48691ffb27b5a83e251d33a68062eb4d14dd54972f6af6296c0.

The accepted prerequisite kernels used in the power/operator replay are:

- proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md,
  SHA-256
  3387615b5522deeb4c63021fbdf4a665afa2c405052f2ff0868bed40338e602f;
- proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md,
  SHA-256
  4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160;
- proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md,
  SHA-256
  470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83;
- proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md,
  SHA-256
  4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009.

The immediately preceding final-candidate power review is:

- rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/common_cell_power_operator_postrepair_verification.md,
  SHA-256
  d1c6484ccd965b6f3b9257510679f4b656015bf7d6ebf78e615e2e8e6e8da8a0.

No web source, diagnostic computation, shared state, or sibling artifact
was used as theorem evidence.

## 7. Recommended state effect

**PASS: retain the durable kernel as exact proof evidence for the narrow
common-cell node.**  Subject to the remaining required final reviews and
a mechanically valid State Patch, create only one subordinate
proved_internal \(P_{\rm cc}\) node and attach it as strict-sector
evidence to the still-open hard-M1 small-\(t\) owner.

Leave the accepted Round-184, Round-185, Round-193, and Round-195 nodes
unchanged.  Record the refined complement only in the new node and the
open owner's next action.  Do not change any parent, bridge, endpoint
uniformity claim, theorem, or exponent.

The route-wide terminal label remains
p2_four_corner_orbit_boundary_self_return_no_go; the durable positive
result is only the fully typed common-cell subsector.
