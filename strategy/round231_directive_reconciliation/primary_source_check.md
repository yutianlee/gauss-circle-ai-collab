# Primary-statement check and independent power comparison

11 October 2026. Conductor, Round231 prelaunch reconciliation. This is a bounded statement-level check, not a complete source-proof audit or a new accepted dependency.

## Checked source statements

[Blomer–Pascadi, arXiv2607.24311v1](https://arxiv.org/html/2607.24311v1#S1.SS1), 27 July2026, Theorem1.1, has arbitrary complex coefficients, unit a modulo c, integer interval lengths at most N<=c, and the restriction (m,n,c)=1. Its norm factor is

    c^(1+o(1)) [N^(1/8)c^(-3/32)+N^(5/16)c^(-3/16)+N^(2/3)c^(-7/18)].

The gcd-free exception concerns both initial intervals. Theorem5.5 handles unequal lengths. Section1.4 equation(1.5) is a cyclic four-Kloosterman product; it does not identify the project's Gram operator. The [record](https://arxiv.org/abs/2607.24311) still lists v1 only.

[Li–Yang](https://arxiv.org/abs/2308.14859) still lists v2,14 September2023. Its [introductory first-spacing vector](https://arxiv.org/html/2308.14859v2#S1) is (l,kl,l sqrt(k),l/sqrt(k)). [Guth–Maldague](https://arxiv.org/abs/2206.01093) lists v2,13 August2022. [Bourgain–Watt](https://arxiv.org/abs/1709.04340) remains withdrawn,16 July2023, for specified spacing/reduction defects. This does not reject decoupling generally. The repository's five Li–Yang repairs and first-coordinate warning remain binding; they were not independently re-audited here.

## Conductor's algebraic consequence

Put N=c^eta, ignoring fixed constants and subpowers. Substituting into the displayed three terms gives

    E(eta)=max(29/32+eta/8, 13/16+5eta/16, 11/18+2eta/3).

Relative to the standard equal-length comparison c^min(1,1/2+eta), the saving in these displayed bounds is

    sigma(eta)=min(1,1/2+eta)-E(eta).

At eta=1/2, sigma=1/32. The three strict inequalities E(eta)<min(1,1/2+eta) intersect in 13/28<eta<7/12. At either endpoint the strict saving vanishes. Thus the valid c^(31/32+o(1)) upper bound for shorter intervals must not be called a uniform c^(-1/32) improvement over their own trivial bound. This is a comparison of upper-bound certificates, not a lower bound for any actual sum. For unequal lengths, use the literal unequal-length statement and recalculate.

If a matched transfer costs c^rho, the remaining linear saving is sigma(eta)-rho, before outer packet sums and reconstruction. A fourth-root extraction divides a gain in a fourth moment by four; a square-root extraction divides a gain in a Gram estimate by two. Each operation must be priced where it actually occurs. There is no automatic physical X-exponent improvement.

## Scope and first missing step

No source-compatible identity for a complete unresolved parent was supplied by this memo or by this spot check. Moduli, norm lengths, original weights, primitive restrictions, both branches, actual oscillatory multipliers, sharp masks and complete complementary terms remain to be matched. Prime, squarefree-composite, prime-power, gcd-return and endpoint controls belong to that prospective exact application; no invented model is used here as its validation. The external proof itself would require a complete source card before promotion.

Dependencies: requested memo; protocol.md; state/proof_obligations.yml (especially Li-Yang-source-audit and GC-external-Li-Yang-theta-star); sources/li_yang_2023.md; Round200 synthesis and conductor reconciliation. Graph SHA256: a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. State effect: retain candidate, sharpen admission arithmetic, no promotion.
