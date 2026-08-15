# Source Card: Popov 2024 truncated Voronoi formula

## Bibliography

D. A. Popov, “Voronoi's formulae and the Gauss problem,” *Russian
Mathematical Surveys* **79** (2024), no. 1, 53–126.

- DOI: [10.4213/rm10162e](https://doi.org/10.4213/rm10162e)
- [Math-Net article record](https://www.mathnet.ru/eng/rm10162)
- [Official English PDF](https://www.mathnet.ru/links/e3363d53e79dddf8f594b8a071b52fd2/rm10162_eng.pdf)

## Exact result used

Popov's (r(n)) is the project's (r_2(n)), and his (P(x)) is the
closed-disc Gauss remainder. Theorem 5, equations (5.1)–(5.2), states for
all (N\ge3) and (x\ge3)

\[
 P(x)=-\frac{x^{1/4}}{\pi}\sum_{n\le N}
 \frac{r_2(n)}{n^{3/4}}
 \cos\!\left(2\pi\sqrt{nx}+\frac\pi4\right)
 +\Delta_NP(x),
\]

with

\[
 \Delta_NP(x)\ll
 \sqrt{\frac{x}{N}}\,\overline r(x)+\overline r(N)\log N,
 \qquad
 \overline r(t)=\exp\!\left(\frac{\log t}{\log_2t}\right)=t^{o(1)}.
\]

Taking (N\asymp X^{1/2}) makes the remainder
(O_\varepsilon(X^{1/4+\varepsilon})). Consequently a target-sized bound
for the complete radial cosine sum at that cutoff is equivalent, in both
directions and up to a target-sized error, to the Gauss-circle target.

Theorem 4, equation (4.1), gives the Bessel-series form, and equation
(4.15) supplies the (J_1) asymptotic. Together they confirm the same
radial constant and phase. The infinite Bessel identity uses midpoint
counting at represented integers; the resulting difference from the
closed-disc convention is (r_2(X)/2=O_\varepsilon(X^\varepsilon)). The
truncated Theorem 5 is already stated for the closed-disc remainder.

## Project normalization check

The hypothetical completed M1 stationary coefficient is

\[
 -\frac{2e(1/8)}\pi X^{1/4}n^{-3/4}
 \sum_{q\mid n}\chi_4(q)
 =-\frac{e(1/8)}{2\pi}X^{1/4}r_2(n)n^{-3/4}.
\]

Adding the negative frequency gives twice the real part, exactly Popov's
cosine term. Thus a full (r_2/4) completion is a Hardy–Voronoi return
map, not merely a resemblance.

## Scope

This source certifies the classical radial identity and its truncation
error. It does not show that the project's angular M1 coefficient equals
(r_2(n)/4), and it gives no new estimate for that radial sum.

## Audit provenance

- Independent source/hostile audit:
  `rounds/codex-managed/m9-m1-dual-r2-recombination/reports/hardy_return_hostile_source_audit.md`
- Conductor cross-check: official Math-Net record and Theorem 5 display,
  2026-08-12.

Audit status: `completed_primary_source_audit`.
