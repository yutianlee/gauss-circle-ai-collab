# Round 163 profile, boundary, and power seam review

- Campaign: `m9-m2-hard-top-t1-near-square-divisor-involution-gate`
- Candidate reviewed: `conductor_round163_close_opposite_prime_exchange_sector.md`
- Reports reviewed: all three Round-163 task reports
- Review status: **GREEN for the strict sector, with two nonblocking provenance/wording corrections**

## 1. Result

The profile/boundary/power seam passes.  Under the inherited one-block
hypotheses, the accepted graph supplies exactly the uniform regularity
needed in (163.C6): a fixed rescaling for \(\eta_L\), a bounded \(C^1\)
Vaaler profile \(\Phi\), and a fixed top profile \(W\), with only a
fixed number of hard faces.  The later Round-137 and Round-162 literal
coefficient packets introduce no new profile and no \(L\)-dependent
family of transitions.

I independently reproduce (163.C12)--(163.C16), including the complete
zero-extended partner set.  If

\[
 \delta_N=\left|\log(q_N/p_N)\right|
 \leq \kappa L^{-1/2},
\]

then common-cell pairs cost

\[
 O(L^2)O_\kappa(L^{-1/2})=O_\kappa(L^{3/2}),
\]

and every fixed hard face has a crossing collar containing

\[
 O\!\left(L(\delta_NL+1)\right)
 =O_\kappa(L^{3/2}+L)
\]

ordered integer incidences.  There are \(O(1)\) such faces and bounded
normalized amplitude, so

\[
 \mathcal S_{L,1}^{\rm cp}\ll_\kappa L^{3/2}+L
 \ll_\kappa L^{3/2}.
\]

No hidden \(\log X\), \(H/L\), divisor-function, eligible-pair, floor,
star, even-branch, or derivative loss occurs in this fixed-\(L\) sector.
The conclusion is only the complete canonical exactly-one incidence
sector.  It proves no density, per-block nonvacuity, estimate for the
uncovered complement, or full \(t=1\) theorem.

## 2. Exact statement and hypotheses

Fix \(\kappa>0\) and one nonempty physical block with \(1\ll L\ll H\)
(the weaker inherited relation \(L\ll H\) is enough).  For squarefree
\(N\asymp L^2\), write \(m=N/d\), require \(d\) odd, and encode every
literal cone, half-open convention, endpoint, and star weight in
\(\mathbf 1_{I_N}^{\rm lit}(d)\).  Put

\[
 A_N(d)=\mathbf 1_{I_N}^{\rm lit}(d)\,
 \eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xd}{4m}}\right),
\]

extended by zero to every odd divisor outside the physical window.
For each qualifying \(N\), choose one canonical pair of distinct odd
prime divisors \(p_N,q_N\) with

\[
 \chi_4(p_Nq_N)=-1,
 \qquad \left|\log(q_N/p_N)\right|\leq\kappa L^{-1/2},
\]

using only the fixed data \((N,L,\kappa)\), never the allocation \(d\).
The reviewed sum contains all and only odd divisors containing exactly
one of \(p_N,q_N\).

The precise regularity hypotheses, and their accepted provenance, are:

| Interface used here | Exact accepted source | Consequence needed here |
|---|---|---|
| `H4-Phi-regularity` (`proved_internal`) | `sources/vaaler_1985.md` and the Round-6 H4 normalization review | \(\Phi\in C^1[0,1]\), \(\|\Phi\|_\infty+\|\Phi'\|_\infty\ll1\), including its endpoints. |
| `M9-M2-dyadic-weight-nondegeneracy` (`proved_internal`) | Round endpoint fixed-profile certificate and endpoint-kernel validation synthesis | On an \(L\)-band, \(\eta_L(d)=\eta(d/L)\) up to the fixed normalization, \(\|\eta_L'\|_\infty\ll L^{-1}\), and the number of entries/exits is fixed.  There is exactly one hard top band, not an \(L\)-dependent collection inside a block. |
| `M9-M2-top-endpoint-transform` (`proved_internal`) | Round top-endpoint-transform synthesis | The transformed factor is the fixed \(W(\sqrt{q_Xd/(4m)})\); the one-sided top cutoff contributes one hard affine cone face. |
| Round-74 exact normalized cone packet | `m9-m2-top-endpoint-affine-cone/derivation_packet.md` and its conductor adjudication | The literal cone is \(m\in[\lceil d/4\rceil,d]\), the lower hard edge and exact normalization are retained, and \(d,m\asymp L\) on support. |
| `M9-M2-top-endpoint-actual-symbol-variation` (`proved_internal`) | Round-77 derivation, hostile/blind reports, adjudication, and synthesis | The actual symbol uses fixed \(\eta_L,W\), the accepted \(C^1\) \(\Phi\), exact \(q_X,H,y\), floors, stars, and finite support.  Its fixed auxiliary collars do not become physical coefficient seams. |
| Literal product-fibre and \(t=1\) packets | Round-137 product-fibre candidate/adjudication and Round-162 exact \(t=1\) candidate/adjudication/kernel | They reindex the same literal scalar coefficient and add no profile or transition family. |

The Round-77 actual-symbol theorem is not being imported as a black-box
pointwise estimate.  Its accepted symbol definition and uniform profile
seminorms, together with the elementary mean-value theorem, prove the
specific Lipschitz estimate needed below.  The still-open signed-cone
and full hard-TOP owners are not used.

## 3. Proof or derivation

### 3.1 Exact ambient involution and (163.C12)

On the complete exactly-one divisor set \(\mathscr D_N^{\rm cp}\), define

\[
 T_Nd=
 \begin{cases}
 dq_N/p_N,&p_N\mid d,\\
 dp_N/q_N,&q_N\mid d.
 \end{cases}
\]

Squarefreeness puts the other selected prime in \(m=N/d\), so this is
an integral, fixed-point-free, multiplicity-one involution.  It keeps
\(N\) fixed and reverses the character:

\[
 \chi_4(T_Nd)=-\chi_4(d).
\]

Because the reindexing is over the complete ambient exactly-one set,
not merely over its physical part,

\[
\begin{aligned}
 \sum_{d\in\mathscr D_N^{\rm cp}}\chi_4(d)A_N(T_Nd)
 &=-\sum_{d\in\mathscr D_N^{\rm cp}}\chi_4(d)A_N(d),\\
 \sum_{d\in\mathscr D_N^{\rm cp}}\chi_4(d)A_N(d)
 &=\frac12\sum_{d\in\mathscr D_N^{\rm cp}}\chi_4(d)
   \{A_N(d)-A_N(T_Nd)\}.
\end{aligned}
\]

This is exactly (163.C12).  The factor \(1/2\) is correct: the displayed
ambient sum contains the two orientations of each two-cycle.

There is no zero-extension tail.  If either \(A_N(d)\) or
\(A_N(T_Nd)\) is nonzero, one orbit leg lies in a fixed
\(O(L)\)-by-\(O(L)\) physical box.  Since the exchange is

\[
 (d,m)\longmapsto(e^{\pm\theta_N}d,e^{\mp\theta_N}m),
 \qquad \theta_N=\log(q_N/p_N),
\]

the other leg lies in a fixed \(\kappa\)-dependent enlargement of that
box.  Thus the union of all nonzero oriented partner legs contains
\(O_\kappa(L^2)\) integer pairs.  Equivalently, every physical seed
creates at most its one partner.  No divisor count or out-of-box partner
has been suppressed.

### 3.2 Common-cell estimate and (163.C13)--(163.C15)

Equation (163.C13) is the selection hypothesis.  On a common smooth
cell, set \(u=\pm\theta_N\).  The three changes satisfy

\[
\begin{aligned}
 |\eta_L(e^ud)-\eta_L(d)|
 &\ll L^{-1}|e^u-1|d\ll |u|,\\
 \left|\Phi\!\left(\frac{e^ud}{H+1}\right)
       -\Phi\!\left(\frac d{H+1}\right)\right|
 &\ll |u|\frac L H\ll |u|,\\
 \left|W\!\left(e^u\sqrt{\frac{q_Xd}{4m}}\right)
       -W\!\left(\sqrt{\frac{q_Xd}{4m}}\right)\right|
 &\ll |u|.
\end{aligned}
\]

Here \(q_X,H,y\) and every floor are fixed during the exchange.  The
\(W\)-argument is multiplied by exactly \(e^u\), so no derivative of
\(q_X\) occurs.  The \(\Phi\) estimate is (163.C15); if the block meets
the hard frequency cutoff, nonemptiness itself gives \(L\ll H\), while
the cutoff crossing is charged below.  Boundedness of the three factors
then gives

\[
 |A_N(d)-A_N(T_Nd)|\ll |u|\ll_\kappa L^{-1/2}
\]

whenever both legs remain in one cell.  The normalization
\((L^2/N)^{3/4}\) is invariant and \(O(1)\), and the phase
\(e(J\sqrt N)\) is invariant and has modulus one.  This proves
(163.C14) with no \(X\)- or \(J\)-dependent seminorm.

### 3.3 Complete boundary ledger and (163.C16)

Put \(\delta=\kappa L^{-1/2}\).  A ratio face
\(d=\lambda m+O(1)\) can be crossed only if

\[
 |d-\lambda m|\ll\delta L+1.
\]

For each of \(O(L)\) possible \(m\), this leaves
\(O(\delta L+1)\) possible integers \(d\).  A vertical face
\(d=d_0\asymp L\), including one at \(d_0=H\) or \(y\) when it meets
the block, has the identical count, as does a horizontal face.  Hence
each face contributes

\[
 O\!\left(L(\delta L+1)\right)
 =O_\kappa(L^{3/2}+L).
\]

The literal ledger is as follows.

| Literal feature | Audit of the exchange | Cost |
|---|---|---:|
| Half-open \(N\asymp L^2\) shell and its endpoints | \(dm=N\) is exact on both legs, so membership and phase do not change. | \(0\) |
| Upper near-square cone \(\sqrt N\le d\le2\sqrt N\), equivalently \(m\le d\le4m\) | The ratio \(d/m\) is multiplied by \(e^{\pm2\theta_N}\); its two half-open faces lie in ratio collars. | \(O_\kappa(L^{3/2}+L)\) |
| Exact lower endpoint \(m=\lceil d/4\rceil\) | For integer points, \(m\ge\lceil d/4\rceil\) is exactly \(d\le4m\); the ceiling is one affine face, not \(O(L)\) different seams.  Equality/star points are \(O(L)\). | Included above, plus \(O(L)\) |
| Dyadic \(\eta_L\) support and cell faces | Fixed base profile rescaled by \(L\); a fixed number of vertical faces, each with thickness \(O(\delta L+1)\). | \(O_\kappa(L^{3/2}+L)\) total |
| \(\Phi(d/(H+1))\) | \(\Phi\) is globally bounded \(C^1\) on \([0,1]\); there are no internal hard seams.  The exact frequency truncation, if it meets the block, is one vertical face. | Common-cell cost, plus at most one collar |
| \(W(\sqrt{q_Xd/(4m)})\) support/plateau cells | \(W\) is one fixed profile.  Each chosen cell boundary is one ratio face \(d/m=4c^2/q_X\); \(q_X\) moves the location but not the number or width of faces. | \(O_\kappa(L^{3/2}+L)\) total |
| One-sided top endpoint | The accepted endpoint transform produces one hard affine lower-cone face with bounded jump \(W(1)=1\). | Included in the cone collar |
| Floors \(H,y\), exact \(q_X\), and ceilings | These are global constants during an orbit.  Their \(O(1)\) location shifts do not create extra faces. | \(0\) away from the already counted faces |
| Star and half-endpoint weights | A star can change only on an exact endpoint lattice face; all star weights are bounded. | \(O(L)\) |
| Oddness and even-\(N\) branch | Only odd primes move.  If \(N=2M\), then \(d\) remains odd and the factor \(2\) remains in \(m\). | \(0\) |
| Squarefreeness, coprimality, XOR condition, and canonical pair | All are invariant under the exchange; arithmetic restrictions only delete lattice pairs. | \(0\) |
| Zero extension | A membership change crosses one of the listed support/cone faces, and both legs stay in the enlarged \(O(L)^2\) box. | Included in the collars |

The number of listed faces is uniform.  The dyadic partition has
\(O(\log X)\) blocks globally, but (163.C2) is a theorem for one fixed
\(L\)-block.  Inside that block the base profiles and the number of
hard faces are fixed.  Round-77's auxiliary fixed collars are not new
physical cutoffs; even if one refines by them, their number remains
\(O(1)\).  Round-137 and Round-162 add no later profile.  This proves
(163.C16) with no hidden transition cardinality.

### 3.4 Target-power ledger

Let \(K=O(1)\) be the total number of hard faces.  The complete estimate
following the exact identity is

\[
\begin{aligned}
 |\mathcal S_{L,1}^{\rm cp}|
 &\ll O_\kappa(L^2)L^{-1/2}
   +K\,O_\kappa\!\left(L(L^{1/2}+1)\right)\\
 &\ll_\kappa L^{3/2}+L
 \ll_\kappa L^{3/2}.
\end{aligned}
\]

There is one canonical pair per qualifying \(N\), so no eligible-pair
multiplicity is missing.  Counting ordered integer pairs already counts
all products and divisor incidences and is an upper bound before the
squarefree, parity, coprimality, or divisor conditions.  The normalized
crossing amplitude is \(O(1)\).  Consequently the displayed ledger is
the exact missing half-power and not merely an incidence count without
weights.

## 4. First doubtful or unproved step

No blocking profile, boundary, or power step remains.  Two statements
in the candidate should be read more precisely:

1. The sentence after (163.C15) says that the dyadic profile has a
   “fixed logarithmic derivative.”  A compactly supported smooth
   profile need not have bounded \(\eta_L'/\eta_L\) at its zeros.  The
   proof requires only the accepted ordinary bound
   \(\|\eta_L'\|_\infty\ll L^{-1}\), which proves (163.C6) directly.
   Thus this is a wording correction, not a loss or gap.
2. The inequality in (163.C15) uses the inherited nonempty-block
   relation \(L\ll H\).  It should be stated with the sector
   hypotheses rather than attributed to profile regularity alone.
   This relation is present in the literal packet; if the block is
   disjoint from \(d\le H\), its contribution is zero.

There is also a provenance distinction: `M9-M2-top-endpoint-actual-symbol-variation`
certifies the exact fixed-profile symbol interface, but (163.C6) itself
is the elementary mean-value consequence of the fixed seminorms.  No
stronger Round-77 variation estimate is needed.

After those clarifications, the first genuinely unproved step is the
uncovered incidence complement: products with no qualifying pair and
incidences containing neither or both selected primes.  No density,
eventual nonvacuity, or full-\(t=1\) conclusion follows from the seam
review.

## 5. Required control test and outcome

| Required test | Outcome |
|---|---|
| Reproduce (163.C12) on the right domain | **GREEN.** Reindexing the complete ambient exactly-one set with literal zero extension gives the exact factor \(1/2\).  Restricting first to the physical set would be invalid, but the candidate does not do so. |
| Zero-extended partner-leg count | **GREEN.** Every nonzero difference has a physical leg and at most one close partner in a fixed enlarged \(O(L)^2\) box; membership changes lie in the counted collars. |
| Reproduce (163.C13)--(163.C15) | **GREEN.** The exchange size is \(O_\kappa(L^{-1/2})\); fixed-profile ordinary derivatives give the same pointwise gain, and the \(\Phi\) term costs only \(L/H\ll1\). |
| Half-open cone and shell | **GREEN.** The product shell is invariant.  Each cone convention changes only on one of two fixed ratio faces, with exact ties costing \(O(L)\). |
| Dyadic support | **GREEN.** Fixed rescaling gives uniform \(L^{-1}\) derivative and a fixed number of faces in one block.  The global \(O(\log X)\) block count is outside this fixed-\(L\) claim. |
| \(W\) and \(\Phi\) cells | **GREEN.** \(W\) has fixed seminorms and finitely many fixed cells; \(\Phi\) is bounded \(C^1\) through its endpoints.  No cell number or derivative constant depends on \(L\). |
| Later-profile audit | **GREEN.** Round-137 and Round-162 retain the Round-74/77 symbol literally and introduce no extra transition family. |
| Floors, ceilings, and stars | **GREEN.** Floors are orbitwise constants; the ceiling is equivalent to one affine integer inequality; stars live on \(O(1)\) lattice faces and cost \(O(L)\). |
| Even \(N\) | **GREEN.** Odd-prime exchange preserves odd \(d\) and leaves the factor \(2\) in \(m\); there is no extra parity boundary. |
| Canonical-pair multiplicity | **GREEN.** One pair is selected per fixed \((N,L,\kappa)\), independently of \(d\), so there is no sum over all eligible pairs. |
| Reproduce (163.C16) and the missing power | **GREEN.** \(O(L^2)L^{-1/2}+O(L(L^{1/2}+1))=O(L^{3/2}+L)\).  Bounded normalization and phase introduce no further cost. |
| Hidden \(L\)-dependent seam or derivative | **GREEN.** None occurs in the accepted fixed-block interface. |
| Consistency of all three Round-163 reports | **GREEN.** The discovery and hostile reports prove the same strict-sector ledger and correctly flag this seam for review.  The blind report's no-go concerned exact cancellation without the supplied profile seminorms; it is compatible with the post-unmask Lipschitz estimate. |
| Density, nonvacuity, and uncovered complement | **OPEN by scope.** Neither this review nor the candidate proves them. |

No numerical experiment or external estimate was used.

## 6. Dependencies and exact artifacts used

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/briefs/literal_near_square_divisor_involution_attack.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/candidates/conductor_round163_close_opposite_prime_exchange_sector.md`;
- all three files in `rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/reports/`;
- `sources/vaaler_1985.md`;
- `rounds/codex-managed/m9-unit-frequency-w1-validation/reports/h4_weight_normalization_review.md`;
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/dyadic_profile_certificate.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/synthesis.md`;
- `rounds/codex-managed/m9-top-endpoint-transform/synthesis.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/reviews/conductor_round74_adjudication.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/derivation_packet.md`;
- the blind and hostile reports, conductor adjudication, and synthesis in
  `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/`;
- `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/candidates/conductor_round137_product_fibre_energy_and_self_return.md`;
- `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/conductor_round137_product_fibre_adjudication.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/candidates/conductor_round162_t1_character_poisson_collar_obstruction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reviews/conductor_round162_adjudication.md`; and
- `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`.

The graph interfaces used are `H4-Phi-regularity`,
`M9-M2-dyadic-weight-nondegeneracy`, `M9-M2-top-endpoint-transform`,
and `M9-M2-top-endpoint-actual-symbol-variation`, each at its recorded
`proved_internal` status.  The open signed-cone, full hard-TOP, and
downstream owners were checked only for scope and were not assumed.

## 7. Recommended state effect

**Promote** the conductor's (163.C2) only as
`strict_t1_prime_toggle_sector`, with its exact owner: the canonical
\(L^{-1/2}\)-close opposite-character prime-pair, exactly-one-incidence
subsum of the physical \(t=1\) coefficient.  The promotion may cite this
review as the independent profile/boundary/power seam closure.

Retain the two harmless clarifications from Section 4 in the accepted
statement: use the ordinary scale derivative of \(\eta_L\), and state
the inherited nonempty-block relation \(L\ll H\).  Make **no change**
to the uncovered complement, the complete \(t=1\) target, hard TOP,
BAL, UNBAL, either smooth M2 packet, M9--M2, M9, the bridge, the quarter
theorem, or either global exponent.
