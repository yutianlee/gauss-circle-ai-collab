# Round 184 coefficient/profile/endpoint/power post-repair verification

- Campaign: m9-m1-hard-top-t1-comparable-factor-exchange-gate
- Review seam: coefficient_profile_endpoint_power_seam
- Candidate SHA-256 reviewed:
  C514B10BED4C673618179C158258C362373696730C691900D250ED43E379E97F
- Role: independent post-repair verifier
- Evidence status: review evidence only; no candidate or shared-state edit
- Numerical work: none

## 1. Result: GREEN

**Verdict: GREEN.**

The bounded repair requested in
coefficient_profile_endpoint_power_seam_review.md was applied correctly.
The candidate now:

1. defines the \(\tau_N\)-closed active exchange set
   \(\mathscr B_{L,X,\sigma,\kappa}\) by requiring at least one literal
   orbit coefficient to be nonzero;
2. proves that this set lies in a fixed enlarged
   \(O(L)\)-by-\(O(L)\) box;
3. restricts (184.C12), (184.C14), and (184.C15) to that set; and
4. states that outside it both terms in the complete ambient paired
   difference vanish.

This exactly repairs the former mismatch between the displayed
unrestricted BV sum and the \(O(wL)\) support-box multiplicity count.
It retains every zero-extension crossing, because an orbit with one
supported leg and one cemetery leg belongs to
\(\mathscr B_{L,X,\sigma,\kappa}\).

No new assumption, power, endpoint convention, selector restriction, or
density assertion was introduced.  With this repair, (184.C7)--(184.C16)
are GREEN at the actual hard-M1 coefficient/profile/endpoint/power seam.

## 2. Exact repaired statement and hypotheses

For an ambient XOR allocation \(x=(N,u,v)\), write
\(\tau x=(N,u',v')\).  The repaired candidate defines

\[
 \mathscr B_{L,X,\sigma,\kappa}
 =\{x:(u,v)\in\mathscr A_N^\oplus,\ 
       a(u,v)\ne0\ {\rm or}\ a(\tau_N(u,v))\ne0\}.
\tag{184.P1}
\]

The definition is symmetric in the two orbit legs.  Therefore

\[
 x\in\mathscr B_{L,X,\sigma,\kappa}
 \quad\Longleftrightarrow\quad
 \tau x\in\mathscr B_{L,X,\sigma,\kappa},
\tag{184.P2}
\]

so the set is exactly \(\tau_N\)-closed.  If \(x\notin\mathscr B\), then

\[
 a(u,v)=a(\tau_N(u,v))=0.
\tag{184.P3}
\]

Consequently

\[
 \sum_{\mathscr A_N^\oplus}
 |a(u,v)-a(\tau_N(u,v))|
 =
 \sum_{(N,u,v)\in\mathscr B}
 |a(u,v)-a(\tau_N(u,v))|.
\tag{184.P4}
\]

No incidence contributing to the exact XOR scalar is removed.

If \(x\in\mathscr B\), one orbit leg lies in the literal hard-M1 support,
where \(u,v\asymp L\).  Since

\[
 (u',v')=(e^{\pm\theta_N}u,e^{\mp\theta_N}v),
 \qquad |\theta_N|\le\kappa L^{-1/2},
\]

the other leg lies in a fixed \(\kappa\)-dependent enlargement of that
box and

\[
 |u'-u|+|v'-v|\ll_\kappa L^{1/2}+1.
\tag{184.P5}
\]

Thus \(\#\mathscr B=O_\kappa(L^2)\), before arithmetic deletion.

The repaired BV assertion is

\[
 \sum_{(N,u,v)\in\mathscr B}
 |\eta_L(u')-\eta_L(u)|
 \ll_\kappa
 wL\sum_m|\eta_L(m+1)-\eta_L(m)|
 \ll_\kappa L^{3/2},
\tag{184.P6}
\]

where \(w\ll_\kappa L^{1/2}+1\).  Together with the already verified
common-cell and collar estimates, it gives

\[
 \sum_{(N,u,v)\in\mathscr B}
 |a(u,v)-a(\tau_N(u,v))|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\tag{184.P7}
\]

Equations (184.P3)--(184.P4) extend this bound back to the complete
ambient XOR identity, proving (184.C16).

## 3. Proof of the post-repair checks

### 3.1 Active-set closure and exactness

Applying \(\tau_N\) to the predicate in (184.P1) interchanges its two
disjuncts, because \(\tau_N^2=1\).  This proves (184.P2).  Hence complete
two-element exchange orbits are either retained in full or omitted in
full; the repair cannot create a single-orientation sector, alter the
factor \(1/2\) in (184.C6), or change multiplicity.

Equation (184.P3) is the negation of the defining disjunction.  Therefore
the complete ambient paired difference is identically zero off
\(\mathscr B\).  Restricting the coefficient-difference estimates to
\(\mathscr B\) changes neither the exact XOR scalar nor its
zero-extended pairing identity.

In particular, a supported-to-unsupported exchange is retained: one
coefficient is nonzero, so the orbit belongs to \(\mathscr B\).  Thus
cone, shell, profile, floor, star, half-weight, hard-sample, real-\(X\)
crossing, endpoint, and missing-partner leakage remains in the collar
sum.

### 3.2 Enlarged-box implication

On a supported leg the exact M1 cone and shell give \(u,v\asymp L\).
For fixed \(\kappa\),

\[
 |e^{\pm\theta_N}-1|\ll_\kappa L^{-1/2},
\]

so the partner differs in each coordinate by
\(O_\kappa(L^{1/2}+1)\).  Both orientations therefore lie in one fixed
enlarged \(O(L)\)-by-\(O(L)\) box.  This proves the geometric hypothesis
used in the smooth-pair count, the discrete-BV multiplicity count, and
the boundary-collar count.

### 3.3 Repaired C12 multiplicity

Fix a discrete increment \(m\).  If the interval between \(u\) and \(u'\)
crosses \(m\), then \(|u-m|\ll_\kappa w\).  There are
\(O_\kappa(w)\) possible integers \(u\) and \(O(L)\) possible integers
\(v\) in the enlarged box.  Each ordered pair determines \(N=uv\), and
the canonical selector supplies at most one exchange partner.  Hence an
increment is charged at most \(O_\kappa(wL)\) times.

Summing this charge against the accepted normalized variation

\[
 \sum_m|\eta_L(m+1)-\eta_L(m)|\ll1
\]

proves (184.P6).  There is no additional divisor, product-row, selector,
or orbit-orientation multiplicity.  Since
\(wL\ll L^{3/2}+L\ll L^{3/2}\), the restored power is exact.

### 3.4 Repaired C14 and C15

The repaired (184.C14) restricts its different-cell sum to
\(\mathscr B\).  This is the correct domain: all nonzero
zero-extension leakage is present, while pairs with two zero
coefficients are irrelevant.  Every ratio, vertical, or horizontal face
still has

\[
 O_\kappa(L(L^{1/2}+1))
 =O_\kappa(L^{3/2}+L)
\]

crossing pairs, and every exact trace has \(O(L)\) sites.  Multiplication
by the bounded normalized literal symbol gives the same
\(L^{3/2}X^\varepsilon\) collar cost.

The repaired (184.C15) now sums the discrete product-rule estimate over
the same active domain.  Its components remain:

- \(O(L^2)\) common-cell pairs times an
  \(O_\kappa(L^{-1/2})\) \(\Phi/W\) change;
- the \(O(L^{3/2})\) aggregate \(\eta_L\) variation in (184.P6);
- the \(O(L^{3/2}X^\varepsilon)\) face/cemetery cost; and
- zero change in the product-only power and product phase.

Thus (184.P7) follows with no new loss.  By (184.P4), it is exactly the
complete ambient difference bound required in (184.C6).

### 3.5 No regression in C7--C11, C13, or C16

The repair does not alter the accepted M1 factorization

\[
 \eta_L(u)\Phi(u/(H+1))
 W(\sqrt{4q_Xu/v})(L^2/(uv))^{3/4},
\]

the exchange scaling, the \(O(L^{1/2}+1)\) displacement, the
common-cell \(C^1\) changes, the telescoping identity, or the literal
face geometry.  The normalized product power remains invariant because
\(uv=N\).

The exact paired identity (184.C6) is also unchanged.  Since its
complementary ambient terms have zero coefficient difference by
(184.P3), inserting the repaired C15 and taking triangle only after
character reversal proves

\[
 |\mathcal T_{L,X,\sigma}^{\rm cp}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon
\]

for both signs and all real-\(X\) endpoints.

## 4. First doubtful or unproved step

No doubtful step remains in the repaired coefficient/profile/endpoint/
power seam (184.C7)--(184.C16).

The first still-unproved owner-relevant analytic assertion is outside
this seam: the complete residual one-outer-real-part correlation
(184.C25).  The repaired strict XOR-sector estimate neither proves that
correlation nor estimates no-pair and selected neither/both incidences.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| current candidate hash | **GREEN.** SHA-256 is C514B10BED4C673618179C158258C362373696730C691900D250ED43E379E97F. |
| UTF-8/control-byte hygiene | **GREEN.** Strict UTF-8 decoding succeeds and there are zero non-tab/newline/carriage-return control bytes. |
| active-set definition | **GREEN.** At least one nonzero literal orbit coefficient is necessary and sufficient for a nonzero paired difference. |
| \(\tau_N\)-closure | **GREEN.** The defining disjunction is invariant under the involution. |
| complete ambient identity | **GREEN.** Outside the active set both coefficient terms vanish, so restriction changes no scalar or multiplicity. |
| zero-extension leakage | **GREEN.** One-supported/one-cemetery orbits remain active and are charged. |
| fixed enlarged box | **GREEN.** One supported leg plus close exchange puts both legs in an \(O(L)\)-by-\(O(L)\) enlargement. |
| repaired C12 domain | **GREEN.** The displayed sum now matches the domain used in the \(O(wL)\) count. |
| discrete-BV multiplicity | **GREEN.** A fixed increment has \(O(w)\) possible \(u\)'s and \(O(L)\) possible \(v\)'s; \(N\) and the selected partner are then fixed. |
| repaired C14 collar domain | **GREEN.** Every nonzero different-cell pair is retained, and double-zero pairs are harmlessly omitted. |
| repaired C15 product-rule domain | **GREEN.** All factor differences are summed on one common active set and extend by zero to the ambient set. |
| literal coefficient and normalization | **GREEN.** No M1 factor, normalized power, sign, profile, or endpoint convention changed. |
| common-cell and endpoint powers | **GREEN.** \(L^2L^{-1/2}=L^{3/2}\) and \(L\cdot L^{1/2}=L^{3/2}\). |
| both signs and real-\(X\) crossings | **GREEN.** The active-set repair is signwise and preserves all fixed-\(X\) faces and traces. |
| no M2 theorem transfer | **GREEN.** The repaired proof remains the direct hard-M1 coefficient proof. |
| C16 final implication | **GREEN.** The repaired difference bound inserts into the unchanged exact signed pairing. |
| scope quarantine | **GREEN.** Only the possibly empty strict \(t=1\) XOR incidence sector is affected. |

No numerical experiment, symbolic calculation, or external theorem was
used.

## 6. Dependencies and exact artifacts used

This verification used:

1. protocol.md;
2. state/proof_obligations.yml for the previously audited named direct
   dependencies and scope;
3. state/active_campaign.yml;
4. the repaired
   rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/candidates/formalized_hard_m1_t1_comparable_factor_exchange_sector.md,
   SHA-256
   C514B10BED4C673618179C158258C362373696730C691900D250ED43E379E97F;
5. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/coefficient_profile_endpoint_power_seam_review.md;
6. the exact M1 factorization and endpoint sources already audited there:
   rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/coefficient_product_endpoint_seam_review.md,
   rounds/codex-managed/m9-combined-top-cones/reports/combined_cone_algebra.md,
   and
   rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md; and
7. the Round-184 reconciliation and two nonblind reports previously
   compared in the seam review.

The post-repair check itself required only the new active-set definition,
the repaired C12/C14/C15 domains, their implication into C16, and
mechanical hash/encoding/control-byte verification.  No M2 exchange
estimate was imported.

## 7. Recommended state effect

**Mark this seam GREEN for the repaired candidate.**  No further
coefficient/profile/endpoint/power repair is required.

The candidate may proceed to the remaining independent seam reviews and
final validation.  This verification does not itself authorize a State
Patch.  If every other required seam is GREEN, the maximum result
supported here is one subordinate proved-internal, possibly empty,
strict hard-M1 \(t=1\) comparable-factor XOR incidence sector with its
exact residual left open.

Keep the complete \(t=1\) face, \(t\ge2\) small-\(G\) incidences, the
large-\(G\) near-resonant complement, the complete small-\(t\) owner,
both direct M1 parents, every M2 owner, endpoint uniformity, M9, both
bridges, the quarter theorem, and all exponent ledgers unchanged.
