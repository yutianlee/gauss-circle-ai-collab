# Round 184 coefficient, profile, endpoint, and power seam review

- Campaign: m9-m1-hard-top-t1-comparable-factor-exchange-gate
- Review seam: coefficient_profile_endpoint_power_seam
- Candidate reviewed:
  candidates/formalized_hard_m1_t1_comparable_factor_exchange_sector.md
- Candidate SHA-256 reviewed:
  609EB3BFA2EEE1566D913F63CBF4997E48AC7A7D6FD927213529C01528B8FC6E
- Role: independent hostile line audit of (184.C7)--(184.C16)
- Evidence status: review evidence only; no candidate or shared-state edit
- Numerical work: none

## 1. Result: REPAIR

**Verdict: REPAIR, with one bounded domain correction.**

The actual hard-M1 factorization, normalization, common-cell
\(\Phi/W\) changes, aggregate discrete-BV charging principle, literal
face geometry, endpoint powers, both-sign uniformity, and the final
\(L^2\) to \(L^{3/2}\) ledger are sound.  They are obtained directly
from the accepted M1 transform and frequency-shell evidence; no M2
coefficient theorem is used or inferred.

The first defective displayed step is (184.C12).  Its proof counts only
pairs in the fixed enlarged M1 support box, but its displayed left-hand
side sums over every \(N\) and the complete ambient XOR allocation set.
The factor \(\eta_L(u)\) alone does not constrain \(v\), so the stated
sum is broader than the \(O(wL)\)-multiplicity count used to bound it.
The line must be restricted to the active exchange set

\[
 \mathscr B_{L,\kappa,\sigma}
 :=\{(N,u,v):(u,v)\in\mathscr A_N^\oplus,\ 
       a(u,v)\ne0\ {\rm or}\ a(\tau_N(u,v))\ne0\},
\tag{184.RC1}
\]

or to any explicitly defined fixed enlarged box containing this set.
Then the correct statement is

\[
 \sum_{(N,u,v)\in\mathscr B_{L,\kappa,\sigma}}
 |\eta_L(u')-\eta_L(u)|
 \ll_\kappa wL\sum_m|\eta_L(m+1)-\eta_L(m)|
 \ll_\kappa L^{3/2}.
\tag{184.RC2}
\]

This repair is sufficient: outside \(\mathscr B_{L,\kappa,\sigma}\) both
literal coefficients in (184.C6) are zero, so there is no difference to
bound.  With (184.C12) replaced by (184.RC2), the discrete product rule
proves (184.C15), and (184.C16) is GREEN at this seam.

No second mathematical defect was found.  In particular, the repair does
not add a regularity hypothesis, change a power, delete an endpoint, or
restrict the claimed XOR sector.

## 2. Exact statement and hypotheses

Fix real \(X\ge2\), a nonempty literal middle or lower residual frequency
shell \(L\), \(\sigma\in\{\pm1\}\), and \(\kappa>0\).  Put

\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor .
\]

The accepted one-sided hard-M1 transform gives, on a positive-frequency
shell \(u\asymp L\), the exact stationary coefficient

\[
 {\eta_L(u)\Phi(u/(H+1))
  W(\sqrt{4q_Xu/v})\over (uv)^{3/4}}
\]

times the fixed outer constant
\(-2e(1/8)X^{1/4}/\pi\), the odd-\(v\) character, and the strict cone
\(4u<v<16u\).  After the common outer \(X^{1/4}\) is removed and the
shell target is normalized by \(L^{3/2}\), the moving scalar symbol is

\[
 a_{L,X}^{\mathrm{lit},\sigma}(u,v)
 =c_{L,X,\sigma}\,
 \eta_L(u)\Phi\!\left({u\over H+1}\right)
 W\!\left(\sqrt{{4q_Xu\over v}}\right)
 \left({L^2\over uv}\right)^{3/4}
 \mathcal M_{L,X,\sigma}(u,v),
\tag{184.RC3}
\]

where:

1. \(c_{L,X,\sigma}\) is allocation-independent and
   \(O_\varepsilon(X^\varepsilon)\); the negative-frequency coefficient
   is the corresponding conjugate/sign branch and has the same
   seminorms.
2. \(\eta_L\) is zero-extended, bounded, and has normalized discrete
   variation
   \[
    \|\eta_L\|_\infty+
    \sum_m|\eta_L(m+1)-\eta_L(m)|\ll1.
   \tag{184.RC4}
   \]
3. \(\Phi\in C^1([0,1])\) with a uniform derivative bound, and \(W\) is
   the fixed hard transformed profile with a uniform \(C^1\) bound on
   each literal smooth cell.
4. \(\mathcal M_{L,X,\sigma}\) is the finite product of the inherited
   height, shell, cone, support, floor, star, half-weight, hard-sample,
   real-\(X\) crossing, endpoint, and zero-extension masks/traces.
   At fixed \((L,X,\sigma)\), every moving boundary is a vertical,
   horizontal, or fixed-real-\(X\) ratio face, apart from exact
   one-dimensional trace values.
5. Nonempty support gives \(L\le H\), \(u,v\asymp L\), and
   \(uv\asymp L^2\).

Formula (184.RC3) is the M1 factorization reproduced in the Round-183
coefficient review from the exact stationary formula.  It is not the M2
profile with variables relabelled.

For a canonical selected pair let
\(\theta_N=\log(q_N/p_N)\).  On an XOR orbit,

\[
 (u',v')=(e^{\pm\theta_N}u,e^{\mp\theta_N}v),\qquad
 |\theta_N|\le\kappa L^{-1/2}.
\tag{184.RC5}
\]

If either literal orbit leg is supported, both legs lie in a fixed
\(\kappa\)-dependent \(O(L)\)-by-\(O(L)\) enlarged box and

\[
 |u'-u|+|v'-v|\ll_\kappa w,\qquad
 w:=L^{1/2}+1.
\tag{184.RC6}
\]

The reviewed conclusion, after the repair (184.RC2), is

\[
 \sum_N\sum_{(u,v)\in\mathscr A_N^\oplus}
 |a(u,v)-a(\tau_N(u,v))|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon,
\tag{184.RC7}
\]

and hence the exact character-reversing identity gives

\[
 |\mathcal T^{\rm cp}_{L,X,\sigma}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\tag{184.RC8}
\]

## 3. Proof or derivation

### 3.1 C7: exact factorization and normalization

The exact M1 transform has

\[
 \alpha_{u,H}={i\over2\pi u}\Phi\!\left({u\over H+1}\right)
\]

for the positive frequency.  Its stationary contribution supplies
\((uX)^{1/4}v^{-3/4}\).  Multiplication by the actual outer
\(-4\alpha_{u,H}\) therefore changes the \(u\)-power to
\(u^{-3/4}\), leaving

\[
 X^{1/4}\Phi\!\left({u\over H+1}\right)(uv)^{-3/4}.
\]

The exact combined-cone formula fixes the leading constant as
\(-2e(1/8)/\pi\), and the shell insertion contributes \(\eta_L(u)\).
After the outer \(X^{1/4}\) and the target normalization are removed,
the power is exactly

\[
 L^{3/2}(uv)^{-3/4}
 =\left({L^2\over uv}\right)^{3/4}.
\]

It depends only on \(N=uv\), so it is invariant under \(\tau_N\).
There is no hidden factor \(H/L\), \(J\), \(X^{1/4}\), \(u/v\), or
additional single-leg power in (184.C7).  Since \(N\asymp L^2\), this
normalized power is \(O(1)\) on support.

The character is on \(v\), while \(\eta_L\) and \(\Phi\) are on \(u\).
This confirms the M1 placement used by the candidate and also confirms
that the proof is not an M2 transfer.

### 3.2 C8--C10: displacement and common smooth cells

Equation (184.RC5) is exact because the exchange multiplies one leg by
\(p_N/q_N\) and the other by its reciprocal.  For \(L\ge1\),

\[
 |e^{\pm\theta_N}-1|
 \ll_\kappa|\theta_N|
 \ll_\kappa L^{-1/2}.
\]

Together with \(u,v\asymp L\), this proves (184.C9), including the
\(+1\) allowance for bounded shells.

The product power is invariant.  On a common smooth cell,

\[
 \left|\Phi\!\left({u'\over H+1}\right)
       -\Phi\!\left({u\over H+1}\right)\right|
 \ll {w\over H+1}
 \ll L^{-1/2},
\]

because \(L\le H\).  Also

\[
 \sqrt{{4q_Xu'\over v'}}
 =e^{\pm\theta_N}\sqrt{{4q_Xu\over v}},
\]

so the fixed \(C^1\) bound for \(W\) gives another
\(O_\kappa(L^{-1/2})\) difference.  The enlarged box contains
\(O(L^2)\) ordered pairs; coprimality, parity, squarefreeness, XOR, and
the canonical selector only delete pairs.  The total common-cell
\(\Phi/W\) cost is therefore
\[
 O_{\kappa,\varepsilon}
 (L^2L^{-1/2}X^\varepsilon)
 =O_{\kappa,\varepsilon}(L^{3/2}X^\varepsilon).
\]

The same argument applies to both signs because all profile factors are
real and the sign branch changes only an allocation-independent constant
and the product phase, which is invariant on an orbit.

### 3.3 C11--C12: aggregate discrete-BV charge and multiplicity

For integer \(u,u'\), telescoping proves (184.C11) without a derivative
hypothesis.  On the repaired active set (184.RC1), fix an increment
\(m\).  If the interval between \(u\) and \(u'\) crosses \(m\), then
\(|u-m|\ll_\kappa w\).  There are \(O_\kappa(w)\) possible \(u\)'s and,
inside the enlarged literal box, \(O(L)\) possible \(v\)'s.  The product
\(N=uv\) is then determined, and the selector supplies at most one
partner.  Hence the charge multiplicity is \(O_\kappa(wL)\), not
\(O(wL\tau(N))\) and not \(O(wL)\) separately for every selected pair.

Summing first over pairs crossing \(m\), then over \(m\), gives
(184.RC2).  By (184.RC4) and \(w\ll L^{1/2}+1\),

\[
 wL\sum_m|\Delta\eta_L(m)|
 \ll L^{3/2}+L
 \ll L^{3/2}.
\]

This independently validates the intended aggregate-BV mechanism and its
multiplicity.  It also identifies why the unrestricted displayed
(184.C12) must be repaired: the \(O(L)\) count for \(v\) comes from the
enlarged literal box, not from \(\eta_L(u)\) by itself.

### 3.4 C13--C14: exhaustive literal faces and endpoints

Crossing an affine ratio face \(v=\lambda u+O(1)\) under a displacement
of size \(w\) forces

\[
 |v-\lambda u|\ll_\kappa w.
\]

There are \(O(L)\) possible values along the face and \(O(w)\) transverse
values, hence \(O_\kappa(Lw)=O_\kappa(L^{3/2}+L)\) ordered pairs.  The
same count holds for vertical and horizontal faces.  Exact trace sites
on one face have only \(O(L)\) incidences.  The literal ledger is:

| Literal field | Orbit behaviour | Required charge |
|---|---|---:|
| \((L^2/(uv))^{3/4}\) and the product shell | exactly invariant | \(0\) |
| outer product phase | exactly invariant | \(0\) |
| \(\eta_L(u)\), including shell entries/exits and sampled endpoint values | discrete BV | \(O(L^{3/2})\) by (184.RC2) |
| \(\Phi(u/(H+1))\) | common-cell \(C^1\); \(u=H\) is vertical | \(O(L^{3/2})\) |
| \(W(\sqrt{4q_Xu/v})\) | common-cell \(C^1\); support, plateau, and hard sample are ratio faces | \(O(L^{3/2})\) |
| strict cone \(v=4u,16u\) | ratio faces | \(O(L^{3/2})\) |
| floors \(y,H\) and real-\(X\) value \(q_X\) | fixed for each real \(X\); induced moving faces are vertical or ratio faces | \(O(L^{3/2})\) uniformly |
| stars, ties, and half weights | fixed finite endpoint traces | \(O(L)\) per trace |
| missing partner and zero extension | union of the same face collars | \(O(L^{3/2})\) |
| \(\sigma=\pm1\) | fixed/conjugate coefficient branch | no extra power |

The exact M1 formula and the Round-183 coefficient review show no
additional two-dimensional moving field.  A smooth plateau edge may be
kept inside the \(C^1\) estimate; treating it as a face only overcounts.
Squarefree, coprime, odd-\(v\), and XOR restrictions again only delete
points.

Multiplying the \(O_\kappa(L^{3/2})\) collar count by the bounded
normalized literal symbol gives (184.C14).  Any two occurrences of
\(X^\varepsilon\), such as a harmless logarithmic face multiplicity and
the coefficient envelope, are absorbed by the standard relabelling
\(\varepsilon\mapsto\varepsilon/2\); no \(X^{2\varepsilon}\) is retained.
The collar constants are uniform as \(X\) crosses a value where \(y\),
\(H\), or a sampled endpoint changes, because the proof uses the number
and geometry of the faces, not their locations.

### 3.5 C15--C16: discrete product rule and final power

On the active set, apply the discrete product rule to (184.RC3).
The terms are:

- the invariant product power, with zero difference;
- pointwise \(O(L^{-1/2})\) changes of \(\Phi\) and \(W\) on
  \(O(L^2)\) common-cell pairs;
- the aggregate \(\eta_L\) charge (184.RC2); and
- coefficient-weighted face crossings from (184.C14).

Each term is \(O_{\kappa,\varepsilon}(L^{3/2}X^\varepsilon)\).
This proves the repaired form of (184.C15).  Outside the active set both
coefficients vanish, so extending the sum back to the complete ambient
XOR set costs zero.

Finally, (184.C6) has one factor \(1/2\), one common product phase, and
exact character reversal.  Triangle is taken only after that signed
pairing.  It therefore gives (184.C16) with no additional divisor,
endpoint, sign, or shell multiplicity.  The exact power comparison is

\[
 \underbrace{L^2}_{\text{ambient pairs}}
 \times
 \underbrace{L^{-1/2}}_{\text{smooth exchange difference}}
 =
 L^{3/2},
\qquad
 \underbrace{L}_{\text{face length}}
 \times
 \underbrace{L^{1/2}}_{\text{collar width}}
 =
 L^{3/2}.
\]

## 4. First doubtful or unproved step

The first doubtful step is exactly the domain of (184.C12), not the BV
telescoping or multiplicity calculation.  Read literally, its left side
ranges over the complete ambient XOR cube for all \(N\), while the proof
uses \(v=O(L)\) from the fixed enlarged literal box.  The correct domain
is (184.RC1), or an explicitly named enlarged box containing it.

After this repair, no doubtful coefficient, endpoint, or power step
remains in (184.C7)--(184.C16).  The next unproved analytic step lies
outside this review seam: the complete residual correlation (184.C25).
This review neither validates that correlation nor claims the complete
\(t=1\) target.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| candidate hash and hygiene | **PASS.** The reviewed post-hygiene SHA-256 is 609EB3BFA2EEE1566D913F63CBF4997E48AC7A7D6FD927213529C01528B8FC6E. |
| C7 exact M1 factorization | **GREEN.** The \(\eta_L,\Phi,W\) placement and product-only normalized power follow from the exact M1 stationary formula. |
| normalization and restored powers | **GREEN.** The Vaaler \(u^{-1}\) and stationary \(u^{1/4}\) combine to \(u^{-3/4}\); normalization gives \((L^2/(uv))^{3/4}\), with no hidden \(H,J,X\), or \(L\) loss. |
| C8 exchange scaling | **GREEN.** The two legs are multiplied by reciprocal \(e^{\pm\theta_N}\) factors. |
| C9 displacement | **GREEN on the union of literal supports.** The width is \(O_\kappa(L^{1/2}+1)\). |
| C10 common-cell \(\Phi/W\) changes | **GREEN.** Each is \(O_\kappa(L^{-1/2})\), uniformly for \(L\le H\). |
| C11 telescoping | **GREEN.** It uses only integer discrete BV. |
| C12 aggregate BV charge | **REPAIR.** Restrict the displayed sum to (184.RC1) or the named enlarged box.  The \(O(wL)\) multiplicity and \(L^{3/2}\) bound then pass. |
| BV multiplicity/no double count | **GREEN after repair.** A pair determines \(N\), and the canonical selector supplies at most one exchange; no divisor factor is restored. |
| C13 face collars | **GREEN.** Every vertical, horizontal, ratio, or staircase face has \(O(L^{3/2}+L)\) crossing pairs. |
| C14 coefficient-weighted collar | **GREEN.** The finite literal face list, exact traces, zero extension, and coefficient envelope give \(L^{3/2}X^\varepsilon\). |
| floors, stars, half weights, and hard sample | **GREEN.** They are fixed global values, one-variable/ratio faces, or \(O(L)\) exact traces; none creates a two-dimensional family of independent jumps. |
| real-\(X\) crossings and endpoints | **GREEN.** \(y,H,q_X\) are fixed at each \(X\), and uniformity depends only on face geometry and seminorms. |
| both signs | **GREEN.** The actual negative branch is conjugate/signwise with identical absolute seminorms; the product phase is orbit-invariant. |
| C15 product rule | **GREEN conditional on the C12 repair.** All factor differences sum to target size. |
| C16 final sector bound | **GREEN conditional on the C12 repair.** Positivity occurs only after exact character-reversing pairing. |
| \(L^2\) to \(L^{3/2}\) power | **GREEN.** Both common-cell and boundary ledgers earn exactly the missing \(L^{1/2}\). |
| M2-to-M1 scope | **GREEN.** The proof uses the explicit M1 transform and profile; the M2 sector theorem is not invoked. |
| arbitrary-coefficient false control | **PASS.** Removing the actual BV/\(C^1\) relation leaves \(L^2\) capacity, so the proof does not establish the false adversarial analogue. |
| owner and exponent quarantine | **PASS.** Only a possibly empty strict \(t=1\) incidence sector is under review. |

No numerical experiment, symbolic computation, or external theorem was
used.

## 6. Dependencies and exact artifacts used

The review used only the assigned context:

1. protocol.md;
2. state/proof_obligations.yml, only for the named direct dependencies
   and downstream scope;
3. state/active_campaign.yml;
4. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/candidates/formalized_hard_m1_t1_comparable_factor_exchange_sector.md,
   post-hygiene SHA-256
   609EB3BFA2EEE1566D913F63CBF4997E48AC7A7D6FD927213529C01528B8FC6E;
5. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/conductor_round184_report_reconciliation.md;
6. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reports/literal_t1_exchange_residual_attack.md;
7. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reports/m2_transfer_transport_capacity_audit.md;
8. rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/coefficient_product_endpoint_seam_review.md;
9. rounds/codex-managed/m9-combined-top-cones/reports/combined_cone_algebra.md; and
10. rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md.

The exact accepted graph inputs checked were
M9-M1-hard-top-squarefree-radical-sector-reduction,
M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector,
M9-M1-top-endpoint-transform,
M9-M1-frequency-phase-diagram-R10,
H4-Phi-regularity,
M9-M2-dyadic-weight-nondegeneracy, and
Divisor-bound-elementary.  No M2 exchange estimate was treated as a
dependency.

## 7. Recommended state effect

**Repair the candidate, then recheck this seam.**  Replace (184.C12) by
(184.RC2), or equivalently define once before (184.C9) that every
coefficient-difference estimate is restricted to the union of the two
literal orbit supports and its fixed enlarged box.  Update the candidate
hash and reproduce the one-line multiplicity check.  No other
coefficient/profile/endpoint/power alteration is recommended.

After that bounded repair, this seam supports GREEN for
(184.C7)--(184.C16) and hence supports only the subordinate strict
hard-M1 \(t=1\) comparable-factor XOR incidence sector.  It does not
support the complete \(t=1\) face or residual.

Make no graph change from the present REPAIR review.  Keep
M9-M1-hard-top-high-radical-small-t-residual-estimate,
M9-M1-top-endpoint-signed-cone,
M9-M1-direct-smooth-residual-blockwise-estimate, M9-M1, every M2 owner,
endpoint uniformity, M9, both bridges, the quarter theorem, and the
internal/external/target exponent ledgers unchanged.
