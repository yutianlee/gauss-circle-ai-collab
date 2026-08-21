# Round 109 formalization report: linear owner completion attack

Campaign: m9-m2-blockwise-owner-completion

Task: linear_owner_completion_attack

Role: formalizer, selected context

Starting graph SHA-256: f861f43d46bec112682a73e4c6062cbebf82f83fdcf0639e6fe122c6a123ad0d

## 1. Result: full scalar blockwise owner completion

The literal hard-top owner family admits the strong completion required
in (109.12)--(109.13). After refining the owner key by the stage at which
an atom is removed, there is an exact finite identity

\[
 \mathfrak Q_B^{\rm res}
 =\mathfrak Q_B^{\rm comp}
  -\sum_{\nu\in\mathcal O}\mathfrak O_{B,\nu},
\qquad
 \sum_{B,\nu}|\mathfrak O_{B,\nu}|
 \ll_{\varepsilon,C}L^2X^\varepsilon .
\tag{1.1}
\]

The completion is on a fixed half-open dyadic \(k\)-lattice and the
literal collared physical range. The owner list contains the whole
Round-77 transform/error packet, square rays (including a separate exact
square-centre atom), exact nonsquare centres, the positive-safe range,
the singleton row, and any prescribed polylogarithmic fixed-\(q\) shell.
The last two are optional refinements of the older owned energy, but
their scalar cost is proved explicitly below.

Three repairs are decisive.

1. The Round-77 adjudication proves an absolute estimate before summing
   ordered pairs: endpoint/collar samples have \(O(1)\) capacity per
   ordered pair, and the equality/nonstationary mode packet has total
   \(O(\log(2+L))\) per collared ordered pair. Half-open \(A,D,G\)
   ownership and dyadic \(K,R\) refinement therefore preserve an
   outside-absolute \(O(L^2X^\varepsilon)\) ledger.
2. The Round-78 square theorem refines to each nonexact smooth metric
   annulus by opening \(W_R\): the frequency is
   \(n=|g-2\nu|\ge1\), including the metric density \(\nu=0\).
   Exact square centres are absent from every punctured \(W_R\), since
   \(W_R(0)=0\); they form a separate target-safe divisor atom.
3. The sharp terminal metric window is not Fourier-expanded. It is
   reconstructed as the full carrier multiplier minus the shallow
   smooth annuli and the exact-centre atom. The full multiplier uses
   \(n=g\ge1\) in the same sampled-\(k\) proof. Thus no terminal seam
   remains.

The weaker global signed completion is an immediate corollary:

\[
 \left|\sum_B\mathfrak Q_B^{\rm res}\right|
 \le
 \left|\sum_B\mathfrak Q_B^{\rm comp}\right|
 +O_\varepsilon(L^2X^\varepsilon).
\tag{1.2}
\]

Thus a future global signed directional estimate is sufficient for the
hard-top energy even without proving
\(\sum_B|\mathfrak Q_B^{\rm comp}|\). No estimate for the completed
directional vector itself is proved here.

## 2. Exact statement and hypotheses

Let \(X\ge2\), \(J=X^{1/2}\), and \(1\le L\le J^{1/2}\). For primitive
odd \(a<b<4a\), put

\[
 q={b-a\over2},\qquad
 \Lambda={X(\sqrt b-\sqrt a)^2\over2},
\]

\[
 I_{a,b}=(\kappa_-(a,b),\kappa_+(a,b))
 =\left({J(\sqrt b-\sqrt a)\over2\sqrt a},
        {J(\sqrt b-\sqrt a)\over\sqrt b}\right).
\tag{2.1}
\]

The interval is open. No endpoint is rounded, and no owner is evaluated
at a noninteger stationary sample. Let
\(\mathbb K_K=\mathbb Z\cap[K,2K)\), with the inherited dyadic weight,
stars, and symmetric half weights at genuine integer equalities. Let
\(\mathcal B_L^+\) contain one representative from each conjugate
orientation, with half-open \(A,D,K,G\) ownership, so

\[
 K\asymp {JD\over A},\qquad G\asymp {L\over A},\qquad
 \rho_B={AJD^3\over L^3}.
\tag{2.2}
\]

The refined owner key permits \(R={\rm eq}\) for exact metric centres and
\(R=\bot\) for atoms removed before the metric partition. This is a
placement tag, not an extra copy. Original Poisson zero modes use their
own stage tag rather than an artificial nonzero \(K\).

For the positive orientation define the literal stationary scalar atom

\[
 T^+_B(a,b,g,k;R)
 =\vartheta_B(a,b,g,k)\,
   \chi_4(ga)\chi_4(gb)\,
   W_R(\Lambda/k)\,
   \mathfrak C^\circ_{a,b,k}(g),
\tag{2.3}
\]

where every accepted profile, floor, star, finite odd-lift cutoff,
physical transition, and zero extension is contained in
\(\vartheta_B\mathfrak C^\circ\), and

\[
 \mathfrak C^\circ_{a,b,k}(g)
 =\int_{gb/4}^{ga}A^\circ_{ga,gb}(x)
 e\!\left(kx-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)dx.
\tag{2.4}
\]

The conjugate orientation is \(T^-_B=\overline{T^+_B}\). All formulas
use one orientation and the outer \(2\Re\). Equivalently one may sum
both orientations and omit \(2\Re\), but one may not do both.

On a shallow punctured metric annulus,

\[
 W_R(t)=\mu_R+\sum_{\nu\ne0}\widehat W_R(\nu)e(\nu t),
\qquad \mu_R=\widehat W_R(0).
\tag{2.5}
\]

The \(\nu=0\) term is the metric density and remains in the completed
coefficient. It is not the Round-77 original Poisson zero mode.

For the exact terminal reconstruction fix the accepted terminal scale
\(N=N_{a,b}\ll G\) and write

\[
 1={\bf1}_{\|t\|=0}
   +\sum_{R<N}W_R^{\rm sh}(t)
   +W_{{\rm deep},N}^{\rm punct}(t),
\tag{2.6}
\]

where

\[
 W_{{\rm deep},N}^{\rm punct}(t)
 ={\bf1}_{0<\|t\|\le c/N}.
\]

Thus the terminal scalar is defined exactly as full carrier minus the
shallow annuli minus the equality atom. No Fourier \(L^1\) claim is made
for the sharp terminal indicator.

Assign the boundary \(\rho_B=1\) literally by

\[
 \Pi_{\rm safe}={\bf1}_{\rho_B\le1},\qquad
 \Pi_{\rm hard}={\bf1}_{\rho_B>1}.
\tag{2.7}
\]

For a fixed prescribed \(C\), let \(q_{\log}\) mean
\(q>1\) on a dyadic shell \(D\le(\log(2+X))^C\), after all earlier
owners. Let \(\mathfrak Q_B^{\rm comp}\) be the exact finite full-Poisson,
fixed-\(\mathbb K_K\), collared completion with the same literal weights.
Then (1.1) holds for

\[
\begin{aligned}
\mathcal O=\{&
77_{\rm lat},77_{\rm col},77_{\ge0},77_{\partial I},77_{\rm out},\\
&\square_{\rm eq},\square_R,\square_{\rm deep},
{\rm ns}_{\rm eq},{\rm safe},q1,q_{\log}\}.
\end{aligned}
\tag{2.8}
\]

The diagonal of \(\mathcal E_L^\top\) is kept separate and is never
inserted into (1.1).

## 3. Proof, literal owner table, and norm ledger

All owners are applied on successive complements. On the tagged finite
Poisson universe the priority is

\[
\begin{aligned}
1={}&\Pi_{77}+(1-\Pi_{77})\bigl[
 \Pi_\square+(1-\Pi_\square)\bigl(
 \Pi_{=}+(1-\Pi_=)\bigl(
 \Pi_{\rho\le1}+(1-\Pi_{\rho\le1})\\
&\hspace{43mm}\cdot
 (\Pi_{q1}+\Pi_{q_{\log}}+\Pi_{\rm rem})
 \bigr)\bigr)\bigr].
\end{aligned}
\tag{3.1}
\]

Every projection is restricted to all preceding complements. On the
punctured metric set, (2.6) is the exact one-count identity. Half-open
shells and a fixed tie rule give one owner at scale boundaries. When
smooth annuli overlap, the literal objects are the disjoint tagged atoms
\((\xi,R)\) carrying weights \(W_R(\xi)\); their underlying untagged
sample may occur in finitely many tags, but its total algebraic weight is
exactly one. Thus disjointness refers to the expanded owner dictionary,
not to falsely disjoint supports of a smooth partition.

**Literal owner dictionary.**

| Priority/owner | Literal formula or mask | Block placement | Norm type and result |
|---|---|---|---|
| Diagonal \(\mathsf D\) | \(\sum_m\sum_{h\in\mathscr H_L,\,m\le h\le4m}|a_{\rm end}(h,m)|^2\) | Before primitive rays; not subtracted in (1.1) | Positive \(O(L^2X^\varepsilon)\); remains in \(\mathcal E_{\rm owned,L}\) |
| \(77_{\rm lat}\) | The two full finite-lattice endpoint samples with inherited symmetric weights | \(R=\bot\), before stationary rays | Absolute \(O(1)\) per ordered pair |
| \(77_{\rm col}\) | The exact integrals/samples on the two removed physical collars | \(R=\bot\); disjoint from retained smooth transition integrals | Absolute \(O(1)\) per ordered pair |
| \(77_{\ge0}\) | Original finite-Poisson indices \(j=0\) and \(j>0\), with equality/wrong-sign tags | \(R=\bot\); original \(j=0\neq\) metric \(\nu=0\) | Part of the absolutely convergent collared transform series |
| \(77_{\partial I}\) | \(\sum_{k\in\mathbb K_K\cap\{\kappa_-,\kappa_+\}}^\star T_B^{\rm full}\), only when the real endpoint is an integer | \(R=\bot\); \(I_{a,b}\) is open | Included in the per-pair \(O(\log(2+L))\) ledger |
| \(77_{\rm out}\) | \(\sum_{k\in\mathbb K_K\setminus\overline I_{a,b}}T_B^{\rm full}\), with exact wrong-sign/nonstationary tags | \(R=\bot\); fixed-\(K\) complement | Included in the per-pair \(O(\log(2+L))\) ledger |
| \(\square_{\rm eq}\) | \(a=s^2,b=t^2,t=s+2u,(s,u)=1\), \(k\in I_{a,b}\), \(2Xu^2/k\in\mathbb Z\) | After 77; \(R={\rm eq}\) | Absolute block sum \(O_\varepsilon(L^2X^\varepsilon)\) |
| \(\square_R\) | Same square parametrization, with shallow \(W_R(2Xu^2/k)\) | After 77, before nonsquares | Outside-absolute \(A,D,K,G,R\) sum \(O_\varepsilon(L^2X^\varepsilon)\) |
| \(\square_{\rm deep}\) | Full square carrier minus all shallow square annuli minus \(\square_{\rm eq}\) | Terminal \(R=N\); identity (2.6) | Outside-absolute \(O_\varepsilon(L^2X^\varepsilon)\) |
| \({\rm ns}_{\rm eq}\) | \({\bf1}_{ab\ne\square}{\bf1}_{\Lambda/k\in\mathbb Z}T_B^+\) | \(R={\rm eq}\), after squares | Accepted complete absolute contribution \(O_\varepsilon(LX^\varepsilon)\) |
| safe | \({\bf1}_{ab\ne\square}{\bf1}_{\|\Lambda/k\|>0}{\bf1}_{\rho_B\le1}T_B^+\) | Metric \(R\); \(\rho_B=1\) is here | Positive outside-absolute dyadic sum \(O_\varepsilon(L^2X^\varepsilon)\) |
| \(q1\) | \(\sum_{a\asymp A}(-1)F_{a,B}(1)\) on preceding complements | Hard metric \(R\); literal zero extension | Row energy gives scalar outside-absolute \(O_\varepsilon(L^2X^\varepsilon)\) |
| \(q_{\log}\) | \(\sum_{a\asymp A,q\asymp D}(-1)^qF_{a,B}(q)\), \(q>1\), \(D\le\log^C(2+X)\) | Optional new owner after \(q1\) | Cauchy gives \(DL^2X^\varepsilon\) per shell, hence \(O_{\varepsilon,C}(L^2X^\varepsilon)\) |
| Residual | Every preceding complement, \(\rho_B>1\), and \(D>\log^C(2+X)\) if used | Density and all discrepancies coupled; transitions retained | Open completed directional block |

The stationary saddle-entry, saddle-exit, and smooth collar-transition
integrals remain in (2.4). Only the literal endpoint/error atoms listed
above are owned.

### 3.1 Round-77 packet is blockwise outside-absolute

After the fixed collars are inserted, the finite-Poisson transform series
is absolutely convergent. The Round-77 proof gives, for each ordered
pair \((h,s)\),

\[
 \sum_{\text{endpoint/collar samples}}|\cdot|\ll1,
\qquad
 \sum_{\substack{\text{zero, positive, equality,}\\
                  \text{negative nonstationary modes}}}|\cdot|
 \ll\log(2+L).
\tag{3.2}
\]

The second estimate is obtained before the ordered-pair sum: nearby
modes use the first-derivative bound, and tails use two integrations by
parts. There are \(O(L^2)\) ordered pairs in the top block. Each pair
has a unique primitive factorization \(h=ga,s=gb\), hence unique
half-open \(A,D,G\) owners. Grouping an already absolute mode sum into
half-open \(K\)-shells cannot increase it. The equality/sentinel metric
tag or logarithmically many harmless metric refinements costs at most
\(\log^{O(1)}(2+X)\); finite orientations cost a constant. Hence

\[
 \sum_B\sum_{\nu\in\{77_{\rm lat},77_{\rm col},77_{\ge0},
                         77_{\partial I},77_{\rm out}\}}
 |\mathfrak O_{B,\nu}|
 \ll L^2\log^{O(1)}(2+X)
 \ll_\varepsilon L^2X^\varepsilon.
\tag{3.3}
\]

This is extracted from the literal per-pair proof, not inferred from the
aggregate error notation. Pre-metric endpoint, collar, and original-zero
atoms may stay at \(R=\bot\). If a fixed-\(R\) refinement is desired for
a nonzero mode, use the shallow annuli and reconstruct the sharp terminal
as full mode minus shallow annuli minus equality, exactly as in (2.6);
the per-pair absolute majorant and triangle inequality give the same
polylogarithmic cost.

### 3.2 Square owner, including the terminal metric block

For \(a=s^2,b=t^2,t=s+2u\),

\[
 \Lambda=2Xu^2,\qquad K={Ju\over s},\qquad
 \sup_k|B_g(k)|+\operatorname {Var}_kB_g(k)
 \ll_\varepsilon X^\varepsilon\sqrt{gt^2/K}.
\tag{3.4}
\]

For a shallow nonexact annulus, opening \(W_R\) changes the phase to
\(- (g-2\nu)Xu^2/k\). Since \(g\) is odd,
\(n=|g-2\nu|\ge1\), including \(\nu=0\). On \(k\asymp K\),

\[
 \left|{d^2\over dk^2}\left(-{(g-2\nu)Xu^2\over k}\right)\right|
 \asymp {nt^2\over K}.
\tag{3.5}
\]

Weighted second-derivative summation and (3.4) give

\[
 \left|\sum_{k\in I_{a,b}\cap\mathbb K_K}
 B_g(k)e(-(g-2\nu)Xu^2/k)\right|
 \ll_\varepsilon X^\varepsilon
 \left(t^2\sqrt{gn}+\sqrt g\,n^{-1/2}\right).
\tag{3.6}
\]

The accepted Fourier half-moments are

\[
 \sum_\nu|\widehat W_R(\nu)|\,|g-2\nu|^{1/2}\ll\sqrt G,
\qquad
 \sum_\nu|\widehat W_R(\nu)|\,|g-2\nu|^{-1/2}\ll G^{-1/2}.
\tag{3.7}
\]

Since \(g\asymp G\) and \(t^2G\asymp L\), one shallow metric block costs

\[
 X^\varepsilon\left(t^2\sqrt{gG}+\sqrt{g/G}\right)
 \ll X^\varepsilon(L+1)
\tag{3.8}
\]

per lifted square triple. There are
\(O(L\log(2+L))\) actual lifted triples, and the logarithmic block count
is absorbed in \(X^\varepsilon\). Thus
\(\sum_B|\mathfrak O_{B,\square_R}|
\ll_\varepsilon L^2X^\varepsilon\).

At an exact square centre every punctured \(W_R\) vanishes. If
\(2Xu^2/k\in\mathbb Z\), then \(2Xu^2\) is an integer and the possible
\(k\)'s are divisors of it. The elementary divisor bound and (3.4) give

\[
 \sum_{k:\,2Xu^2/k\in\mathbb Z}|B_g(k)|
 \ll_\varepsilon X^\varepsilon\sqrt{gt^2/K}
 \ll_\varepsilon X^\varepsilon\sqrt L.
\tag{3.9}
\]

Summing the triples gives \(O_\varepsilon(L^{3/2}X^\varepsilon)\), hence
\(O_\varepsilon(L^2X^\varepsilon)\).

For the terminal block use (2.6). The full carrier multiplier \(1\)
has only the phase \(-gXu^2/k\), so (3.5)--(3.6) apply with \(n=g\);
this is the original Round-78 complete \(k\)-sum and costs
\(O_\varepsilon(L+1)\) per lifted triple. Therefore

\[
 |\mathfrak O_{B,\square_{\rm deep}}|
 \le |\mathfrak O_{B,\square_{\rm full}}|
   +\sum_{R<N}|\mathfrak O_{B,\square_R}|
   +|\mathfrak O_{B,\square_{\rm eq}}|,
\tag{3.10}
\]

and the outside-absolute total remains
\(O_\varepsilon(L^2X^\varepsilon)\). No Fourier expansion of the sharp
terminal indicator is used.

### 3.3 Nonsquare, safe, short-row, and terminal-row bridges

The accepted exact-nonsquare theorem is absolute and gives
\(O_\varepsilon(LX^\varepsilon)\). On a safe block the positive
capacity is

\[
 X^\varepsilon A\sqrt G\sqrt J\,D^{3/2}
 \asymp X^\varepsilon\sqrt{ALJD^3}
 \le X^\varepsilon L^2
\tag{3.11}
\]

when \(\rho_B\le1\); the dyadic sum costs \(X^\varepsilon\).

For the singleton row, literal zero extension and Cauchy give

\[
 \left|\sum_{a\asymp A}(-1)F_{a,B}(1)\right|
 \le A^{1/2}
 \left(\sum_{a\asymp A}|F_{a,B}(1)|^2\right)^{1/2}
 \ll_\varepsilon X^\varepsilon L^2.
\tag{3.12}
\]

For \(q\asymp D\),

\[
 \left|\sum_{a\asymp A,q\asymp D}(-1)^qF_{a,B}(q)\right|
 \le (AD)^{1/2}
 \left(\sum_{a,q}|F_{a,B}(q)|^2\right)^{1/2}
 \ll_\varepsilon X^\varepsilon DL^2.
\tag{3.13}
\]

This is target-sized for a prescribed polylogarithmic \(D\)-range, not
for a fixed positive-power shell.

The terminal metric row is reconstructed exactly as in (2.6). The full
carrier multiplier \(1\) is the single \(\nu=0\) sampled-\(k\) argument,
so its nonzero frequency is \(n=g\ge1\) and the accepted actual-profile
proof gives the same \(O_\varepsilon(L^2/A)\) fixed-\(q\) row bound.
Subtracting the shallow annuli and the earlier exact-centre atom, then
using the triangle inequality, proves the same scalar bounds
(3.12)--(3.13) for the terminal row. Thus neither squares nor short rows
leave a deep-window seam.

### 3.4 Algebra, projective costs, and global signed completion

Inside \(\mathbb K_K\), the open interval, genuine integer equality
samples, and strict exterior partition the lattice exactly. The physical
profile equals the retained transition integral plus the removed
collars. Applying (3.1) and (2.6) proves (1.1) without a limiting
interchange.

Smooth difference localization has Fourier \(L^1\)-cost
\(\|\widehat\psi\|_1\). Primitivity has the exact Mobius expansion, and
the actual \(a^{-3/4}b^{-3/4}\) weights give
\(\sum_d d^{-3/2}<\infty\). These devices are used only for smooth
projective factors. Square, equality, safe, and short-row masks are
controlled by their own scalar estimates; the moving endpoint graph is
controlled by (3.2), not silently factorized.

Summing (1.1) gives (1.2), and

\[
 \mathcal E_L^\top
 =\mathcal E_{\rm owned,L}
  +2\Re\sum_B\mathfrak Q_B^{\rm comp}
  -2\Re\sum_{B,\nu}\mathfrak O_{B,\nu}.
\tag{3.14}
\]

The pre-104 completion complements lie among the accepted scalar pieces
of \(\mathcal E_{\rm owned,L}\); the diagonal remains separate. The
\(q1\) and \(q_{\log}\) refinements are newly moved pieces bounded by
(3.12)--(3.13), not silently asserted to be in the older identity.

## 4. First doubtful or unproved step

There is no remaining unproved norm conversion inside the scalar owner
completion (1.1). In particular, (3.3) comes from the Round-77
componentwise absolute proof and not from the invalid implication

\[
 \left|\sum_B\mathfrak O_B^{77}\right|\ll L^2X^\varepsilon
 \ \Longrightarrow\
 \sum_B|\mathfrak O_B^{77}|\ll L^2X^\varepsilon.
\tag{4.1}
\]

A two-block model \(o_{B_1}=M,o_{B_2}=-M\) refutes (4.1) for arbitrary
coefficients; it is only a norm control, not an actual-symbol
obstruction. The actual Round-77 proof majorizes endpoints, collars,
nearby modes, and tails before summing pairs.

The first genuinely unproved step after completion is the directional
theorem

\[
 \sum_B|\mathfrak Q_B^{\rm comp}|
 \ll_\varepsilon L^2X^\varepsilon,
\tag{4.2}
\]

or, for the weaker sufficient global route,

\[
 \left|\sum_B\mathfrak Q_B^{\rm comp}\right|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{4.3}
\]

Neither follows from completion. The exact finite triangular separation
of the sharp reciprocal ratio band has logarithmic projective cost, but
its factors remain jagged functions of ranks, ties, \(k\), and endpoints.
No owner projection is proved to commute with the Fejer operator, so
(1.1) gives no fixed-\(a\) Gram cross-energy estimate.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| owner_one_count_and_disjointness | **Pass.** Priority (3.1), reconstruction (2.6), half-open scales, \(R={\rm eq}\), \(R=\bot\), and zero extension give one weighted copy. |
| scalar_vs_energy_normalization | **Pass.** Equations (3.12)--(3.13) are explicit row-energy-to-oriented-scalar bridges. |
| blockwise_absolute_vs_signed_aggregate | **Pass.** Round 77 uses (3.2)--(3.3); squares retain \(k\)-cancellation before block absolute values. The false implication (4.1) is not used. |
| fixed_K_completion_and_open_endpoints | **Pass.** Equality occurs only at an actual integer endpoint and carries the inherited star/half weight. |
| physical_collar_and_entry_exit | **Pass.** Removed collars are 77 owners; complete stationary and transition integrals remain in \(\mathfrak C^\circ\). |
| original_zero_mode_vs_metric_density | **Pass.** Original Poisson \(j=0\) is \(77_{\ge0}\); metric \(\nu=0\) remains in \(W_R\) and in (3.7)--(3.8). |
| smooth_projective_separation | **Pass.** Smooth difference localization and Mobius separation have summable costs. |
| sharp_pair_owner_projective_norm | **Pass without false factorization.** Each sharp owner has its own scalar theorem; the sharp terminal is reconstructed, not Fourier-majorized. |
| square_fourth_power_and_Pell | **Pass.** Fourth-power square rays, metric, exact, and terminal, remain in (3.4)--(3.10). A nonsquare Pell/near-square singleton such as \((25,27)\) is covered by (3.12). |
| q1_polylog_and_empty_singleton | **Pass.** Zero extension handles empty/singleton fibres; no inverse interval-length bound is used; polynomial \(D\) is not claimed. |
| exact_centre_and_rho_boundary | **Pass.** \(W_R(0)=0\) forces separate exact atoms. \(\rho_B=1\) belongs to safe. |
| orientation_floor_star_halfweight | **Pass.** One orientation plus outer \(2\Re\) is used. Floors, stars, and half weights remain literal and are not doubled. |
| Fejer_commutator_and_Gram_nonimplication | **Pass as a negative control.** The result is scalar linear completion only. |
| downstream_and_exponent_scope | **Pass.** No completed-vector estimate, hard density-discrepancy theorem, smooth packet, M9-M2, M9-M1, endpoint uniformity, M9, or exponent is proved. |

No numerical experiment was used. All controls are finite algebraic or
analytic checks.

## 6. Dependencies and exact artifacts used

The report uses the context named in the task brief:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-blockwise-owner-completion/derivation_packet.md;
- rounds/codex-managed/m9-m2-blockwise-owner-completion/candidates/conductor_blockwise_owner_completion.md;
- rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md;
- the selected Round-77, Round-78, Round-79, Round-103, Round-104, and
  Round-108 synthesis files named in the brief.

At the conductor's requested seam check, the report also uses lines
56--129 of
rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reviews/conductor_round77_adjudication.md,
which expose the componentwise absolute proof behind the aggregate
Round-77 notation.

The new deductions are the Round-77 dyadic absolute refinement (3.3),
the \(R\)-resolved square calculation (3.4)--(3.8), the exact
square-centre estimate (3.9), terminal reconstruction (3.10), the
short-row scalar bridges (3.12)--(3.13), and the distinction between the
strong theorem (1.1) and global signed corollary (1.2). No external
theorem, web source, sibling Round-109 report, or computation is used.

## 7. Recommended state effect

**Promote narrowly** a proved-internal scalar blockwise owner-completion
interface consisting of (1.1), the literal owner table, and the
Round-77/square/terminal/short-row norm bridges. Record that exact centres
use \(R={\rm eq}\), pre-metric atoms use \(R=\bot\), \(\rho=1\) is safe,
and the normalization is one orientation plus outer \(2\Re\).

**Promote narrowly** the global signed corollary (1.2) as an alternative
sufficient bridge: a theorem of the form (4.3) would control the hard-top
energy, although it would not prove the canonical outside-absolute
directional theorem (4.2).

**Retain open** both completed directional estimates (4.2)--(4.3), the
fixed-\(a\) Gram, and the canonical density-discrepancy energy. Make no
status change to either smooth M2 packet, M9-M2, M9-M1, endpoint
uniformity, M9, the conditional bridge, or the quarter-exponent target.
