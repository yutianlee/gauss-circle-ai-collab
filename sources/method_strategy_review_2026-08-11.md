# Method and Literature Strategy Review — 2026-08-11

## Scope

This is a strategy review, not a source card proving theorem applicability. It asks which analytic interfaces deserve study after the count-versus-weighted-mass adjudication. Any imported theorem still requires an exact hypothesis map and a dedicated source card.

## 1. Li--Yang and the Bombieri--Iwaniec route

Xiaochun Li and Xuerui Yang improve the known circle and divisor exponents by deriving a new first-spacing estimate and combining it with Huxley's second-spacing work:

- [Li--Yang, *An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem*](https://arxiv.org/abs/2308.14859)

The paper is strategically relevant because it treats exponential-sum norms through a first-spacing/second-spacing interface. It is not a drop-in theorem for M9. The paper itself stresses that conditions in the Bourgain--Watt argument cannot simply be taken for granted and checks mutually exclusive parameter regimes before applying its main estimate.

**Campaign implication.** Do not ask whether an M9 phase merely resembles the Li--Yang phase. Build an explicit input map containing the exact sum $S$, $H,M,T,N$, coefficient bounds, derivative conditions on $F$, Case A/B inequalities, smoothing, and the desired uniform $D$ range. A failed input map is a useful barrier result. This work belongs to a later analytic/source-audit campaign, not to promotion from the present finite diagnostic.

## 2. Small-cap decoupling

Demeter, Guth, and Wang develop small-cap decoupling and obtain sharp estimates for exponential sums with small frequency separation; their results are stated for general unit-modulus coefficients in relevant model sums:

- [Demeter--Guth--Wang, *Small cap decouplings*](https://arxiv.org/abs/1908.09166)

Li--Yang uses small-cap decoupling for a truncated cone in its first-spacing analysis. This suggests a possible global-norm module if M9 can be transformed to the required geometric frequency surface and scale.

**Control warning.** A theorem uniform over arbitrary bounded or unit-modulus coefficients will normally be insensitive to the special $\chi_4(h)$ sign. Such a theorem may help a global moment or spacing bound, but cannot by itself supply the sign-sensitive pointwise bridge if the corresponding unsigned control is known to be false. Any proposed decoupling input must be tested against `coefficient-adversary` and `signed-vs-unsigned`.

## 3. Bourgain--Watt as a structural reference

Bourgain and Watt revisit how exponential-sum estimates feed the zeta mean square, circle problem, and divisor problem:

- [Bourgain--Watt, *Mean square of zeta function, circle problem and divisor problem revisited*](https://arxiv.org/abs/1709.04340)

This is relevant to the global-statistics side of the project. It does not remove the need to prove that the project's fixed reciprocal sums satisfy the paper's normalization and parameter ranges.

**Campaign implication.** Treat Bourgain--Watt/Li--Yang as a candidate exported interface: exact transformed sum plus a parameter-feasibility certificate. Review the transformation and theorem application as different seams.

## 4. Recent square-root moment work

Yixiu Xiao proves second- and fourth-moment bounds for exponential sums of square roots and then combines the second moment with separate pointwise exponential-sum estimates and the Erdos--Turan inequality to obtain discrepancy bounds:

- [Xiao, *Moment Estimates and Discrepancy for Sums of Square Roots Modulo One*](https://arxiv.org/abs/2606.28986)

The phase and parameter geometry differ from M9, and this recent preprint is not evidence for a reciprocal-sum lemma. Its architecture is nevertheless informative: a global moment estimate is paired with a distinct pointwise input and discrepancy bridge.

**Campaign implication.** This reinforces the existing M9 barrier: ordinary global fourth-moment control should not be treated as a pointwise estimate. Future work should state the pointwise or large-value bridge as an independent lemma with its own endpoint review.

## 5. Ranked strategy after the active campaign

1. Finish the raw-count versus $\beta$-weighted-mass normalization adjudication.
2. Freeze a smallest sign-sensitive pointwise bridge for M9-M2 and attack it directly.
3. In parallel, construct an exact Li--Yang/Bourgain--Watt input map; stop immediately if a phase, coefficient, smoothness, or parameter condition fails.
4. Consider small-cap decoupling only after a valid transformed frequency geometry is written. Test whether the result proves too much for arbitrary coefficients.
5. Keep global moment estimates and pointwise upgrade as separate proof obligations.

This ranking is analytical. Numerical work may test finite normalizations or falsify a candidate mapping, but it should remain within the campaign's 20% cap.
