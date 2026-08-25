# Demeter--Wu v2 exact primary-source card

- Campaign: `gc-w7-16-cross-ray-hyperbolic-decoupling-source-map`
- Research round: `132`
- Task: `demeter_wu_exact_source_card`
- Role: `source_auditor`
- Status: candidate evidence only; no shared proof-state edit
- Primary source: Ciprian Demeter and Shukun Wu, *Restriction and decoupling estimates for the hyperbolic paraboloid in* $\mathbb R^3$, [arXiv:2505.09037v2](https://arxiv.org/abs/2505.09037v2), revised 14 April 2026

## 1. Result: exact source theorem and source-level no-go

**Source-card lemma.** The official v2 source proves two positive bilinear integral inequalities on the normalized hyperbolic paraboloid

\[
\mathbb H=\{(\xi,\eta,\xi\eta):(\xi,\eta)\in\mathbb R^2\}:
\]

1. a bilinear $\ell^2$ decoupling inequality for functions Fourier supported in $R^{-1}$-neighborhoods of two patches separated by a constant amount in **both** parameter coordinates, with decoupling into $R^{-1/2}$ parameter squares; and
2. a refined bilinear inequality for scale-$R$ wave-packet sums, localized to a union of disjoint $R^{1/2}$-balls in $B_R$, under a separate per-ball tube-incidence bound for each input family.

The source does **not** state a bound for a signed arithmetic exponential sum at one prescribed spatial centre. It does not state an arbitrary pair-coefficient bilinear-form estimate, a sampling/evaluation inequality, or a lemma transferring either bilinear integral estimate to such a fixed-centre scalar while preserving the placement of the modulus and ownership of coefficients. Consequently, the weakest direct implication of the cited theorems remains a bound for $\|f_1f_2\|_{L^2_x}^2$ (globally or in the stated localized form), not a pointwise exponential-sum bound.

The paper does contain a separate pointwise **broad--narrow decomposition** for an extension function, Proposition 4.11. That proposition retains a horizontal-or-vertical strip term; it is a decomposition, not a pointwise norm estimate or an arithmetic sampling bridge. The source's separate linear Theorem 2.4 controls such pieces only after retaining all dyadic rectangles of area $R^{-1}$ in a positive $L^4$ square function.

This is a source-level interface no-go only. It makes no claim about whether some separate, newly proved embedding and pointwise bridge could use the source.

## 2. Exact statements and hypotheses

### 2.1 Version control

The [official arXiv version record](https://arxiv.org/abs/2505.09037v2) identifies v2 as revised 14 April 2026. I audited the archive returned by the [official v2 TeX-source endpoint](https://arxiv.org/src/2505.09037v2), not a secondary exposition. The downloaded archive had 30,477 bytes and SHA-256

`8b9267fb67489ef6918cbbe92f18aad7fb127241a8022b6c05b65274c16625c4`.

Its top-level source is `main.tex`.

### 2.2 Definition 1.2: transversality

For a rectangle $\tau\subset[-1,1]^2$, the source writes

\[
\mathbb H_\tau=\{(\xi,\eta,\xi\eta):(\xi,\eta)\in\tau\}.
\]

For a physical-space function $f:\mathbb R^3\to\mathbb C$, $f_\tau$ means Fourier restriction in the first two frequency coordinates to $\tau\times\mathbb R$. [Definition 1.2](https://arxiv.org/html/2505.09037v2#S1.Thmtheorem2) calls squares $\tau_1,\tau_2\subset[-1,1]^2$ of arbitrary size transverse precisely when, for **every** $(\xi_j,\eta_j)\in\tau_j$,

\[
|\xi_1-\xi_2|\sim1,
\qquad
|\eta_1-\eta_2|\sim1.
\]

The source then records the equivalent formulation that the line between any two parameter points has slope of absolute value $\sim1$ and that the centre line is quantitatively transverse to both coordinate axes. Thus constant separation in just one parameter coordinate does not satisfy Definition 1.2. No conclusion of Theorem 1.6 or 1.10 is stated for such a one-coordinate-separated/ruling pair.

### 2.3 Definition 1.3 and Theorem 1.6: bilinear $\ell^2$ decoupling

[Definition 1.3](https://arxiv.org/html/2505.09037v2#S1.Thmtheorem3) begins with

\[
0<\delta<1,\qquad R\ge1.
\]

It defines $C(\delta,R)$ as the least constant such that, for every pair of transverse $\delta$-squares $\tau_1,\tau_2$ and every pair of functions $f_j$ satisfying

\[
\operatorname{supp}\widehat f_j\subset
N_{1/R}(\mathbb H_{\tau_j}),
\]

one has the exact squared inequality

\[
\int_{\mathbb R^3}|f_1f_2|^2
\le C(\delta,R)
\prod_{j=1}^2
\left(
\sum_{\theta_j\in\mathcal P_{R^{-1/2}}(\tau_j)}
\|f_{\theta_j}\|_{L^4(\mathbb R^3)}^2
\right).
\tag{DW-1.3}
\]

Here $N_{1/R}$ is a three-dimensional Fourier neighborhood of the surface patch, whereas $\theta_j$ is an $R^{-1/2}$-square in the two parameter coordinates. The modulus in the left side encloses the product before squaring:

\[
|f_1f_2|^2=|f_1|^2|f_2|^2.
\]

The right side is a product of two positive sums of squared $L^4$ norms. There is no outer signed sum and no pair-dependent coefficient array in (DW-1.3).

[Theorem 1.6](https://arxiv.org/html/2505.09037v2#S1.Thmtheorem6) states, for every $\varepsilon>0$,

\[
C(1,R)\lesssim_\varepsilon R^\varepsilon
\qquad(R\ge1\text{ through the definition of }C).
\tag{DW-1.6}
\]

There is a minor endpoint convention in the printed text: Definition 1.3 initially declares $0<\delta<1$, while Theorem 1.6 writes $C(1,R)$. The theorem plainly uses $1$ as the constant-scale endpoint; the source does not separately repair the strict inequality in the definition.

[Remark 1.5](https://arxiv.org/html/2505.09037v2#S1.Thmtheorem5) says that the Fourier-support hypothesis makes (DW-1.3) equivalent to a localized version with $\mathbb R^3$ replaced on both sides by “some smooth approximations” of $1_{B_R}$. The source does not replace this radius-$R$ integral by evaluation at one point, and it does not give an explicit sampling constant in that remark.

### 2.4 Definition 1.9 and Theorem 1.10: refined bilinear decoupling

[Definition 1.9](https://arxiv.org/html/2505.09037v2#S1.Thmtheorem9) quantifies over the following data:

- two transverse squares $\tau_1,\tau_2\subset[-1,1]^2$ of arbitrary size;
- a set $X$ that is a union of pairwise disjoint $R^{1/2}$-balls $Q$ contained in $B_R$;
- for each $j=1,2$, a scale-$R$ wave-packet sum
  \[
  f_j=\sum_{T\in\mathbb T_j}f_T,
  \qquad
  \operatorname{supp}\widehat f_j\subset
  N_{R^{-1}}(\mathbb H_{\tau_j});
  \]
- numbers $M_j\ge1$ such that each ball $Q\subset X$ intersects at most $M_j$ of the $R$-tubes in the separate family $\mathbb T_j$.

For all such configurations, $C(R)$ is the least constant for which

\[
\int_X|f_1f_2|^2
\le C(R)(M_1M_2)^{1/2}
\prod_{j=1}^2
\left(
\sum_{T\in\mathbb T_j}\|f_T\|_4^4
\right)^{1/2}.
\tag{DW-1.5}
\]

Equation (1.5) literally prints $f_{T_j}$ although its summation variable is $T$. This is an index typo: subsequent statements and the proof use $f_T$. Formula (DW-1.5) records that intended index while preserving the printed norm orientation. Each packet-family factor is the square root of a sum of fourth powers of global $L^4$ norms; it is not an $L^4$ norm of a signed arithmetic coefficient sum.

[Theorem 1.10](https://arxiv.org/html/2505.09037v2#S1.Thmtheorem10) states, for every $\varepsilon>0$,

\[
C(R)\lesssim_\varepsilon R^\varepsilon.
\tag{DW-1.10}
\]

No equal-size packet-norm hypothesis is present in Definition 1.9. The geometric inputs that must be verified are instead the Fourier support, the scale-$R$ wave-packet structure, two-coordinate transversality, the disjoint $R^{1/2}$-ball localization, and the two per-family incidence caps $M_1,M_2$.

### 2.5 Referenced wave-packet normalization

Definition 1.9 refers to [Section 4.1](https://arxiv.org/html/2505.09037v2#S4.SS1). There the paper switches to a two-variable frequency input $f$ and its extension $Ef$. The exact model has:

- the auxiliary thickness exponent $\varepsilon_0=\varepsilon^{1000}$ in that section;
- a finite-overlap cover of $[-1,1]^2$ by $R^{-1/2}$-balls $\theta$ and a smooth partition of unity;
- a physical $\mathbb R^2$ partition at radius $R^{1/2}$;
- $\Phi(\xi_1,\xi_2)=\xi_1\xi_2$;
- packets $f_{\theta,v}$ and tubes
  \[
  T_{\theta,v}
  =\{(\bar x,x_3)\in B_R:
  |\bar x-c_v+x_3\nabla\Phi(c_\theta)|
  \le R^{1/2+\varepsilon_0}\},
  \]
  of stated dimensions
  $R^{1/2+\varepsilon_0}\times R^{1/2+\varepsilon_0}\times R$;
- the direction notation $V(\theta)=(1,\nabla\Phi(c_\theta))$;
- decomposition, rapid decay off the associated tube inside $B_R$, frequency containment in $3\theta$, $\gtrsim R^{-1/2}$ direction separation, and $R^{O(\varepsilon_0)}$ overlap within a fixed direction, as listed in Lemma 4.3.

Thus the theorem's phrase “scale $R$ wave packets” carries more structure than an arbitrary finite sum indexed by tubes. Also, Definition 1.3 uses parameter **squares**, while the referenced smooth wave-packet construction uses comparable $R^{-1/2}$ parameter **balls**. The source treats these as standard finite-overlap variants; this card does not silently replace the required scale by another one.

### 2.6 Rescalings actually used by the source

The source does not license normalization from a Hessian determinant alone. Its proofs use explicit transformations that preserve $\mathbb H$ and track the neighborhood thickness.

In Section 2, for a parameter-space midpoint $(c_1,c_2)$ and separation $d$, it uses

\[
(\xi,\eta,\gamma)\longmapsto
\left(
\frac{\xi-c_1}{d},
\frac{\eta-c_2}{d},
\frac{\gamma-c_1\eta-c_2\xi+c_1c_2}{d^2}
\right).
\tag{DW-R1}
\]

The paper states that (DW-R1) maps $\mathbb H$ to itself and maps $N_{1/R}(\mathbb H)$ to $N_{1/(Rd^2)}(\mathbb H)$. It is invoked for specifically separated subrectangles, with the accompanying scale and transversality checks; it is not presented as an arbitrary affine-invariance theorem.

For refined decoupling, [Proposition 3.7](https://arxiv.org/html/2505.09037v2#S3.Thmtheorem7) assumes

\[
r\sqrt R\ge K_1,
\]

a general-position rectangle $\omega$ of dimensions $(r/K_2,r)$, almost adjacent rectangles $s,s'$ of dimensions $(r/K_2,r/K_1)$ inside $\omega$, and separate tube-incidence bounds $M,M'$. Rescaling by $K_1/r$ makes the containing $r/K_1$-squares transverse and changes the refined scale to

\[
R' = Rr^2/K_1^2.
\]

The proposition retains the factor $(MM')^{1/2}$ and the two positive packet $L^4$ energies. These hypotheses and costs are part of the permitted source rescaling. The paper also uses coordinate-specific dilations in its separate linear-decoupling application, but neither main bilinear theorem states invariance under an unspecified change of variables.

### 2.7 Explicit source handling of ruling/narrow pieces

The source does not extend Definition 1.2 by calling a one-coordinate-separated pair transverse. Instead, it keeps ruling-aligned pieces in separate positive terms.

[Theorem 2.4](https://arxiv.org/html/2505.09037v2#S2.Thmtheorem4) is a **linear** $L^4$ rectangle-cover decoupling statement. Let $\mathcal R_R$ be all dyadic rectangles $\omega\subset[-1,1]^2$ whose area is $R^{-1}$ and whose dyadic side length satisfies $R^{-1}\le2^n\le2$. If

\[
\operatorname{supp}\widehat f\subset
N_{1/R}(\mathbb H_{[-1,1]^2}),
\]

then

\[
\|f\|_{L^4(\mathbb R^3)}
\lesssim_\varepsilon R^\varepsilon
\left(
\sum_{\omega\in\mathcal R_R}
\|f_\omega\|_{L^4(\mathbb R^3)}^2
\right)^{1/2}.
\tag{DW-2.4}
\]

The cover deliberately contains horizontal and vertical rectangles of every permitted eccentricity, so the ruling-aligned contribution remains on the right side as positive rectangle energy. Theorem 2.4 is not Theorem 1.6 with the transversality hypothesis removed: it is linear, uses a logarithmically overlapping family of all area-$R^{-1}$ rectangles, and has a different right side.

[Proposition 4.11](https://arxiv.org/html/2505.09037v2#S4.Thmtheorem11) makes the same retention pointwise for the extension operator. For dyadic $K\gg1$, let $\mathcal C_K$ be the $K^{-1}$-square partition, let $\{S_1\}$ partition $[-1,1]^2$ into horizontal $1\times K^{-1}$ rectangles, and let $\{S_2\}$ partition it into vertical $K^{-1}\times1$ rectangles. For every $x\in\mathbb R^3$ and $\varepsilon>0$,

\[
|Ef(x)|
\lesssim_\varepsilon
K^{5\varepsilon}\max_{\tau\in\mathcal C_K}|Ef_\tau(x)|
+K^{2\varepsilon}\max_{S_j}|Ef_{S_j}(x)|
+K^3\operatorname{Br}_{K^\varepsilon}Ef(x).
\tag{DW-4.6}
\]

The middle term is the narrow horizontal-or-vertical strip term. It is **not discarded**. In the proof of Theorem 2.4, the broad case invokes Theorem 1.6, whereas a horizontal strip is rescaled by the non-isotropic dilation $(1,2K,2K)$ and a vertical strip by $(2K,1,2K)$, producing the separate recurrence $D(R)\le C D(R/(2K))$. This is the scoped source mechanism for rulings.

There is an editorial sign slip in the proof paragraph immediately following Proposition 4.11: the first strip-case comparison is printed with $\le$ where dominance of the second term requires $\ge$; the next “otherwise” sentence again prints $\le$. The proposition statement (DW-4.6) is unambiguous, and no conclusion here relies on deleting its strip term.

## 3. Proof or derivation of the source-level conclusion

The conclusion follows by checking the logical type of the source statements.

First, both theorem constants are defined only after supplying two physical functions whose Fourier supports already occupy two transverse surface neighborhoods. In particular, transversality and the scale relation “thickness $R^{-1}$ / parameter cap $R^{-1/2}$” are inputs, not consequences of nonzero Gaussian curvature.

Second, if one expands two input functions into pieces,

\[
f_1=\sum_\alpha F_\alpha,
\qquad
f_2=\sum_\beta G_\beta,
\]

then their product is

\[
f_1f_2=\sum_{\alpha,\beta}F_\alpha G_\beta.
\]

The source theorem controls the spatial integral of the modulus square of this product. It does not quantify over an independent joint coefficient $c_{\alpha,\beta}$ in

\[
\sum_{\alpha,\beta}c_{\alpha,\beta}F_\alpha G_\beta.
\]

One-index coefficients may be absorbed into the two inputs, but then pair coefficients factor through the two input families. An exact representation of a nonfactorable joint coefficient would be an additional lemma, not part of Definitions 1.3 or 1.9.

Third, the conclusions are spatial $L^2$-energy estimates. Even the localized form of (DW-1.3) is a radius-$R$ smooth integral, while (DW-1.5) is an integral over a union of $R^{1/2}$-balls. Neither statement includes the evaluation functional at a prescribed $x_0$, a sampling inequality, or the cost of converting an $L^2_x$ bound into a fixed-point bound. Joint spatial translation preserves all global norms and Fourier-support hypotheses while moving which physical point is sampled; this confirms that the theorem itself contains no distinguished centre. It does not rule out a separately proved band-limited evaluation lemma, but such a lemma and its complete scaling cost are absent from the source.

Proposition 4.11 does not alter this conclusion. Its pointwise inequality decomposes $|Ef(x)|$ into a single-square term, a retained horizontal/vertical strip term, and a broad term at the **same** point $x$; it does not bound those three quantities by the bilinear integral norms in (DW-1.3) or (DW-1.5), and it does not identify $Ef(x)$ with a prescribed arithmetic scalar.

Finally, the right sides of both estimates are positive norm expressions. They can exploit oscillation internal to the functions only through those norms; the statements do not assert cancellation from arithmetic signs, characters, ownership conventions, or a prescribed centre phase.

### Conclusions not contained in the source

The following are not statements or corollaries supplied by Theorems 1.6 or 1.10:

1. a pointwise bound for a discrete exponential sum at a fixed centre;
2. a supremum-over-centres estimate or a sampling theorem;
3. an arbitrary pair-coefficient bilinear-form inequality;
4. preservation or cancellation of arithmetic signs, characters, Möbius/Stieltjes coefficients, endpoint owners, or other coefficient metadata;
5. a bilinear theorem for patches separated in only one surface coordinate (the separate linear Theorem 2.4 instead retains all area-$R^{-1}$ rectangles);
6. a broad--narrow conclusion in which the narrow/ruling contribution may simply be discarded (Proposition 4.11 explicitly retains it);
7. an identification of an arithmetic scale with $R$, an $R^{-1}$ Fourier thickness, or $R^{-1/2}$ cap dimensions;
8. a wave-packet incidence bound $M_j$ for any external discrete family;
9. a generic “unit Hessian” or nonzero-curvature normalization theorem; or
10. any global arithmetic exponent or proof-state promotion.

## 4. First doubtful or unproved step

There is no doubtful step in the transcription of the five requested definitions/theorems. The first unproved step in any attempted fixed-centre use occurs **before** either theorem can return an estimate: one needs an exact interface lemma constructing two functions $f_1,f_2$ such that

1. every joint coefficient is represented without changing its ownership or forcing an unsupported rank-one factorization;
2. the two Fourier supports lie in $R^{-1}$-neighborhoods of patches transverse in both parameter coordinates at a specified common scale $R$; and
3. the desired fixed-centre scalar is exactly a controlled evaluation or linear functional of $f_1f_2$, with the full localization/evaluation cost recorded.

The source supplies none of these three assertions. Without the exact representation in item 1, the source theorem cannot even be instantiated for a general pair-weighted scalar. Even if items 1 and 2 were established elsewhere, item 3 would remain a separate pointwise bridge rather than part of Demeter--Wu.

## 5. Required control tests and outcomes

| Control | Outcome | Exact audit finding |
|---|---|---|
| `primary_source_version_and_theorem_text` | **PASS** | Official arXiv v2, revised 14 April 2026, was audited from the TeX archive. Definitions 1.2, 1.3, 1.9 and Theorems 1.6, 1.10 agree with the formulas above. The strict $\delta<1$ / printed $C(1,R)$ endpoint convention and the printed $f_{T_j}$ index typo are explicitly recorded. |
| `transversality_in_both_coordinates` | **PASS; one-coordinate case excluded from the bilinear theorems** | Definition 1.2 requires $|\xi_1-\xi_2|\sim1$ and $|\eta_1-\eta_2|\sim1$ for every pair of parameter points. Theorem 2.4 and Proposition 4.11 handle ruling/narrow pieces separately through retained horizontal/vertical rectangle terms; they do not relabel them transverse. |
| `Fourier_support_thickness_and_cap_scale` | **PASS** | Both main interfaces require support in $N_{R^{-1}}(\mathbb H_\tau)$. Definition 1.3 decouples into $R^{-1/2}$ parameter squares; Definition 1.9 requires scale-$R$ packets, with the referenced construction using $R^{-1/2}$ frequency balls and length-$R$, radius-$R^{1/2+\varepsilon_0}$ tubes. |
| `fixed_centre_scalar_vs_bilinear_L4_integral` | **SOURCE-LEVEL NO-GO** | The main bilinear left sides are $\int|f_1f_2|^2$, globally or over $X$. Proposition 4.11 is pointwise but only decomposes $Ef(x)$ and retains a strip term; it supplies no fixed-centre exponential-sum identification or localization-to-a-point norm cost. |
| `no_positive_energy_or_global_promotion` | **PASS** | The positive cap/packet energies have only been recorded as theorem right sides. They are not substituted for a signed scalar, and no global or proof-state conclusion is drawn. |

No numerical or experimental control was used; the allocation was 100% source/textual and algebraic.

## 6. Dependencies and exact artifacts used

Local artifacts read:

- `rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/briefs/demeter_wu_exact_source_card.md`
- `protocol.md`
- `human/current_directives.md`
- `rounds/codex-managed/gc-w7-16-cross-ray-hyperbolic-decoupling-source-map/blind_statement.md`

External primary artifacts read:

- [arXiv:2505.09037v2 version record](https://arxiv.org/abs/2505.09037v2)
- [official arXiv v2 TeX source](https://arxiv.org/src/2505.09037v2), especially `main.tex`
- [official arXiv v2 HTML rendering](https://arxiv.org/html/2505.09037v2), used only for stable direct anchors to the audited TeX statements

No secondary source, sibling report, shared graph, validation file, synthesis, or proof draft was used or edited.

## 7. Recommended state effect

**Recommended state effect: no change.** Retain this report as the exact primary-source card, and reject only the unsupported assertion that Demeter--Wu's Theorems 1.6 or 1.10 themselves furnish a fixed-centre arithmetic exponential-sum bound. No theorem applicability, exponent improvement, global promotion, or shared proof-state mutation is recommended.
