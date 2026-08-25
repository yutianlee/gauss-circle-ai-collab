# Round 160 M2 UNBAL majorant-history audit

- Role: history and no-repeat auditor
- Current graph SHA-256: 4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d
- Current graph last-updated round: 159
- Scope: the flat-smooth strict-UNBAL positive-energy and one-sided-majorant surfaces only
- State effect: none

## 1. Result

**Result: a Round-160 one-sided band-limited-majorant feasibility campaign
would repeat Round 134 and must not be opened under that formulation.** The
sentence in strategy/conductor_0823_full_proof_strategy.md proposing the
parked positive energy as one of two prospective UNBAL surfaces was written
from the Round-130 graph. It was executed exactly in Round 134,
m9-m2-unbalanced-one-sided-majorant-gate, and closed under
majorant_no_go. The current graph already contains both the optimal finite
majorant theorem and the exact obstruction:

- M9-M2-unbalanced-sharp-folded-Fejer-majorant;
- M9-M2-unbalanced-bandwidth-mass-majorant-obstruction.

The finite extremal problem is not merely source-audited or partially
explored. It is solved exactly. If $1\leq N\leq H$, $H=mN+s$, and
$0\leq s<N$, then the least zeroth coefficient of any real
degree-$(N-1)$ trigonometric polynomial $T\geq F_H=|D_H|^2$ is

\[
 \mu_N(H)=(N-s)m^2+s(m+1)^2
 =\frac{H^2}{N}+s\left(1-\frac{s}{N}\right),
\tag{160.A1}
\]

attained by

\[
 T^*_{H,N}=|mD_N+D_s|^2.
\tag{160.A2}
\]

The contraction is lawful and strict for $N<H$, but its exact mass factor
is

\[
 \rho(H,N)=\frac{\mu_N(H)}H\geq\frac HN,
\tag{160.A3}
\]

and its Fourier-coefficient $\ell^1$-mass is exactly $H^2$. Hence the
bandwidth gain is repaid at the zeroth mode, while lagwise modulus restores
the full factor $H$. Character Poisson returns the same reciprocal shifted
Gram and supplies no second saving.

The strongest still-open interface **on the energy surface** is therefore
not another majorant construction. It is the actual-family signed folded
Gram estimate, before every modulus, with its complete weighted endpoint
remainder ledger. The later Round-143 physical completion identifies an
even smaller equivalent analytic frontier on the wavelet surface: the
fully gcd-restored centered $h\ne0$ modulus-frequency matrix. Neither is
proved, but neither question can honestly be called a new
"one-sided-majorant feasibility" gate.

## 2. Exact statement and hypotheses

Use the literal flat-smooth strict-UNBAL parameters

\[
 M\asymp X,\qquad D=X^\delta,\qquad L=X^\ell,
 \qquad K=\frac{XL}{D^2},\qquad
 H=\left\lceil\frac{X^{1/2}}D\right\rceil,
\tag{160.A4}
\]

\[
 \frac14\leq\delta<\frac12,\qquad
 0\leq\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463,
\tag{160.A5}
\]

and

\[
 Q=\frac{D^2}{L\sqrt X}\longrightarrow\infty,
 \qquad K\asymp LH^2.
\tag{160.A6}
\]

For positive odd $p$, retain the literal zero-extended row

\[
 b_{p,k}=e(-1/8)M^{1/4}k^{-3/4}p^{-3/4}
 W\!\left(\frac{X}{2D}\sqrt{\frac p{Mk}}\right)
 q_L((X/M)p)e(\sqrt{Mpk}).
\tag{160.A7}
\]

Form the actual character sum before every modulus,

\[
 A(k)=\sum_{p>0\atop p\ \mathrm{odd}}\chi_4(p)b_{p,k},
\tag{160.A8}
\]

and put

\[
 \mathcal E_\chi
 =C_H\sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
 =C_H\int_{\mathbb T}F_H(\alpha)|\widehat A(\alpha)|^2\,d\alpha.
\tag{160.A9}
\]

Round 125 proves that the complete flat-smooth off-product survivor is

\[
 \mathcal S_{\mathrm{off}}=\mathcal E_\chi-\mathcal D_0,
 \qquad \mathcal D_0\ll X^{1/2},
\tag{160.A10}
\]

so its absolute target is equivalent to

\[
 \boxed{\mathcal E_\chi\ll_\varepsilon X^{1/2+\varepsilon}.}
\tag{160.A11}
\]

This makes "positive energy" a lawful target-equivalent sign localization
for this one owner. It does **not** license the separate positive-row
energy

\[
 \mathcal E_{\mathrm{eq}}\ll_\varepsilon
 X^{1/2+\varepsilon}\min(H,Q),
\tag{160.A12}
\]

which is strictly stronger and loses a power.

The only still-open folded interface is, for a genuinely shortened
$1\leq N<H$,

\[
 \boxed{
 \mathcal G_N:=
 C_H\sum_{|r|<N}t^*_{-r}
 \sum_{p,q\ \mathrm{odd}}\chi_4(p)\chi_4(q)
 \sum_k b_{p,k+r}\overline{b_{q,k}}
 \ll_\varepsilon X^{1/2+\varepsilon}.}
\tag{160.A13}
\]

Here $t_r^*$ are the exact Fourier coefficients of (160.A2), every row
is zero-extended before shifting, and every moving profile, entry, exit,
stationary transition, nonstationary sign, and remainder is retained. A
meaningful shortening may take, for example,

\[
 \Gamma=\min(H,Q),\qquad
 N=\max\{1,\lfloor H/\Gamma\rfloor\},
\tag{160.A14}
\]

but then (160.A3) forces $\rho(H,N)\geq\Gamma$ up to harmless integer
rounding. Thus (160.A13) must obtain signed cancellation jointly across
$p,q,r,k$; diagonal, rowwise, or lagwise bookkeeping cannot prove it.

## 3. Proof, history, and exact no-repeat ledger

The no-repeat decision follows from the accepted chronological chain.

| Round | Exact surface tested | Accepted outcome | What is now forbidden as a purportedly new move |
|---:|---|---|---|
| 107 | Product regrouping, Mellin/functional equation, $h$-process, and $k$-Poisson | Exact return to the width-$D/L$ prescribed-centre truncated-divisor wave; deficit $H_D/L$ remains | Another coefficient-preserving one-variable transform or an $r_2/4$ completion |
| 118 | Literal prescribed-centre wave, row curvature, coherent runs, exact-centre and square-sector controls | Envelope $\min(D/L,\sqrt{XL/D}+\sqrt{X/(LD)})X^\varepsilon$, always above the strict quarter target | Row-curvature closure, central-core positivity, or a square-sector countermodel as a complete argument |
| 123 | Integer-centred shifted Gram and reciprocal aliases | Zero alias and exact aliases are safe; the signed nonzero nonexact near-alias aggregate remains | Same-$k$ positive Gram, positive diagonal, or fixed-alias derivative closure |
| 124 | Double-character Poisson and joint stationary lattice | Exact off-product inverse reduction and principal Legendre self-return | Projector-through-Poisson, another sequential stationary transform, or unsigned $D^2/L$ capacity as a theorem |
| 125 | Equal/unequal dual sectors and full-character block energy | Exact target-equivalent $\mathcal E_\chi$ reduction; sectorwise norms can be too large by $H$; $\mathcal E_{\mathrm{eq}}$ loses $\min(H,Q)$ | Fejer positivity as an upper bound, separate sectors, positive rows, cellwise Cauchy, re-Poissonization, or the incomplete $4a$ alias lattice |
| 134 | One-sided Beurling--Selberg/Vaaler/trigonometric majorants for $\mathcal E_\chi$ | Exact folded optimizer (160.A1)--(160.A2) and majorant_no_go | Any new universal band-limited-majorant feasibility gate, coefficientwise window order, lag-count-only gain, lagwise modulus, rowwise majorization, or Poisson as a second gain |
| 135 | Physical wave mapped to Bettin--Chandee and Wright Kloosterman-fraction/dispersion sources | Real centre repaired exactly; direct and square connectors lose fixed powers; smooth-first completion returns capacity; inverse-first gives a rough joint matrix | Reusing the same scalar source maps, calling the centre irrationality fatal, or treating every completion as a Kloosterman saving |
| 143 | Exact level-four odd-character Kloosterman embedding and Kuznetsov matrix interface | $h=0$ is safe; the centered $h\ne0$ joint matrix survives; scalar trace formulas and positive second moments do not save | Fixed-index scalar Kuznetsov, row-Parseval localization, full-frequency positive closure, complete $h$-summation, or a pure-level-four source claim without the level-$4/8$ ledger |

Round 134 additionally settled the following placement claims exactly.
They form the minimum no-repeat checklist for any proposed return to this
surface.

1. A strict band-limited majorant **does** exist; nonexistence is false.
2. Coefficientwise Fourier or physical-window order does not order a
   complex block square.
3. Fixed-power bandwidth cannot have target-safe $L^1$ excess.
4. The lag-count saving is repaid by $\mu_N(H)/H$.
5. Lagwise modulus restores Fourier mass $H^2$, hence factor $H$.
6. Rowwise majorization erases actual $\chi_4$ cancellation.
7. The folded inequality is global after summing translations, not
   block-by-block.
8. The folded zeroth factor is a universal closure obstruction, not a
   literal lower bound.
9. The two-grid majorant is valid but not extremal.
10. Character Poisson supplies no independent power.
11. The principal reciprocal Gram alone is not endpoint-complete.
12. The optimal folded majorant does not prove the $\mathcal E_\chi$
    target.

For completeness, the exact extremal proof has two finite steps. Exact
$N$-point quadrature gives

\[
 \widehat T(0)
 =\frac1N\sum_{j=0}^{N-1}T(j/N)
 \geq\frac1N\sum_{j=0}^{N-1}|D_H(j/N)|^2
 =\mu_N(H).
\tag{160.A15}
\]

The last equality is discrete Parseval after folding
$0,\ldots,H-1$ into its $N$ residue classes. The bound is attained
because, with $z=e(\alpha)$,

\[
 |1-z|^2(T^*_{H,N}-F_H)
 =|1-z^N|^2\sum_{a=0}^{m-1}(m-a)
 |1-z^{s+aN}|^2\geq0.
\tag{160.A16}
\]

Thus no better universal degree-$(N-1)$ majorant is left to discover.
Universal Toeplitz quadratic-form order is equivalent to pointwise
multiplier order, by testing the converse with translated Fejer
approximate identities. Changing the brand name of the extremal
construction cannot evade (160.A15).

After exact character Poisson, the principal row is

\[
 \mathcal R(k)=\frac1k\sum_{u>0\atop u\ \mathrm{odd}}
 \chi_4(u)W\!\left(\frac{X}{Du}\right)
 q_L\!\left(\frac{4Xk}{u^2}\right)e(Mk/u).
\tag{160.A17}
\]

Writing the exact transformed row as $A=\mathcal R+\mathcal E$, the
folded form is

\[
 Q_{T^*}(A)=Q_{T^*}(\mathcal R)
 +2\Re B_{T^*}(\mathcal R,\mathcal E)
 +Q_{T^*}(\mathcal E).
\tag{160.A18}
\]

The principal term is the old reciprocal shifted Gram with the same
folded weights. Dropping either cross term or the remainder square is not
an endpoint-complete theorem.

## 4. First doubtful or unproved step

There is no doubtful step in the no-repeat conclusion, the exact folded
extremal theorem, the bandwidth--mass obstruction, the character placement
rule, or the transform self-return. Those are accepted graph facts with
independent blind, discovery, hostile, and post-unmask verification.

The first unproved positive step is precisely (160.A13), or equivalently a
target bound for the full right side of (160.A18). It must cancel the
forced factor $\rho(H,N)$, keep the $r=0$ and $r\ne0$ pieces together,
keep the $p=q$ and $p\ne q$ pieces together, preserve both
$\chi_4$-factors before every modulus, and pay every weighted endpoint
and transition remainder. No accepted theorem does this.

On the later physical completion, the first missing theorem is an
owner-saving estimate for

\[
 \sum_{\substack{g,n\ \mathrm{odd}\\gn\asymp R}}
 \chi_4(g)W\!\left(\frac{X}{gnD}\right)
 \sum_{\substack{h\bmod n\\h\ne0}}
 \widehat\gamma_{g,n}(h)
 S^{\chi_4}_{\infty0}(4N_0,h;2n),
\tag{160.A19}
\]

with a controlled common test, common sequence, projective/vector norm,
long-frequency complement, full level-$4/8$ spectrum, profiles, gcd
strata, and endpoints. The automatic positive closure is
$R\sqrt\Delta X^\varepsilon$, worse than the accepted envelope, and
complete $h$-summation returns the original row. Thus (160.A19) is a
genuine new joint-matrix theorem, not an unfinished line of the majorant
calculation.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Strategy chronology | Pass. The August-23 conductor strategy is a Round-130 strategy; Round 134 subsequently executed its proposed energy-surface feasibility gate. |
| Exact campaign match | Pass. Round 134 froze the same question: apply a one-sided band-limited majorant directly to endpoint-complete $\mathcal E_\chi$, preserving the character, and prove the target or the first obstruction. |
| Exact extremal theorem | Pass. Root-of-unity quadrature and the sum-of-squares factorization prove (160.A1)--(160.A2) sharply. |
| Universal order | Pass only as pointwise multiplier/Toeplitz PSD order. Coefficientwise and nonproportional internal-window placements are false. |
| Character placement | Pass only after forming $A=\sum_p\chi_4(p)b_p$. Positive rows and sectorwise norms erase the needed cancellation. |
| Capacity | No-go. Shortening to $N$ costs $\rho\geq H/N$; lagwise modulus costs $H$; the prior rowwise bound costs $\min(H,Q)$. |
| Endpoint completeness | Pass for exact zero-extended Parseval and exact Poisson integrals. The principal reciprocal Gram alone fails without both cross and remainder terms in (160.A18). |
| Transform novelty | No-go. Exact character Poisson and the second strict-interior process self-return. |
| Later source novelty | No-go for the audited scalar Bettin--Chandee, Wright, and fixed-index Kuznetsov interfaces. Their exact failures are already graph-recorded. |
| Literal versus adversarial controls | Pass. Opposite-row and coherent-row arrays falsify universal shortcuts but are not lower bounds or counterexamples for the literal family. |
| Owner scope | Pass. Every statement here is restricted to one flat-smooth strict-UNBAL owner; hard, sharp, clipped, starred, transition, arithmetic, BAL, TOP, M9-M2, endpoint, M9, bridge, and exponent owners remain unchanged. |

No numerical experiment or web import was used. The audit is entirely
analytical, algebraic, and documentary.

## 6. Dependencies and exact artifacts used

The following authoritative or strategy files were read and used:

- protocol.md;
- state/proof_obligations.yml at the hash recorded above;
- state/round_ledger.yml;
- state/best_proof_draft.md, accepted Round-125 and Round-134 sections;
- strategy/conductor_0823_full_proof_strategy.md.

The complete Round-134 campaign was inspected, including its plan, blind
statement, three briefs, three reports, two conductor candidates, three
post-unmask reviews, conductor adjudication, controls, State Patch, and
synthesis under
rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/.

The origin and later continuation of the interface were checked in:

- rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/;
- rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/;
- rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/;
- rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/;
- rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/;
- rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/;
- rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/.

The exact current graph nodes used are:

- M9-M2-smooth-unbalanced-three-quarter-estimate;
- M9-M2-unbalanced-truncated-divisor-fixed-centre-return;
- M9-M2-unbalanced-flat-wave-curvature-envelope;
- M9-M2-unbalanced-integer-centred-shifted-alias-reduction;
- M9-M2-unbalanced-double-character-stationary-offdiagonal-reduction;
- M9-M2-unbalanced-joint-stationary-principal-return;
- M9-M2-unbalanced-dual-block-energy-one-sided-reduction;
- M9-M2-unbalanced-dual-sector-curvature-no-go;
- M9-M2-unbalanced-sharp-folded-Fejer-majorant;
- M9-M2-unbalanced-bandwidth-mass-majorant-obstruction;
- M9-M2-unbalanced-Kloosterman-dispersion-interface-obstruction;
- M9-M2-unbalanced-level-four-spectral-matrix-obstruction.

## 7. Recommended state effect and Round-160 disposition

**Recommended state effect: no change.** This is a history audit, not new
mathematics.

**Recommended Round-160 disposition: reject the positive-energy
one-sided-majorant surface as a frozen objective.** A question of the
form

> Can a Beurling--Selberg, Vaaler, Fejer, or other universal one-sided
> band-limited majorant prove the $\mathcal E_\chi$ target?

is exactly Round 134 and violates the no-repeat rule. Replacing the name
of the majorant, changing from Fourier to physical-window language, or
performing Poisson after it does not create a new interface.

A return to this owner is legitimate only if the round begins with a
specific new theorem candidate that acts jointly on the literal actual
family before modulus. The narrowest admissible conditional frozen
question would be:

> For $N$ fixed by (160.A14) and the exact optimal folded coefficients
> $t_r^*$, can one prove (160.A13) by a genuinely joint
> $\chi_4(p)\chi_4(q)$ cross-$p$, cross-lag estimate, including the full
> weighted remainder (160.A18), or reduce it noninvertibly to a strictly
> smaller owner-complete signed matrix with an explicit power gain beyond
> $\rho(H,N)$?

This formulation is not a recommendation to launch a generic discovery
round: without a concrete new joint-family mechanism, it merely restates
the known open target in a stronger majorized form. If no such theorem
candidate is available, rotate away from this surface. If M2 UNBAL is
reopened at all, the current smallest exact frontier is (160.A19), and the
brief must explicitly bypass the Round-135 scalar-source and Round-143
joint-matrix obstructions rather than rerun them.

No M2 parent, M9 parent, bridge, quarter theorem, or global exponent changes
on this audit.
