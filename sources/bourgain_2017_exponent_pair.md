# Jean Bourgain 2017 exponent-pair source card

## Bibliography

Jean Bourgain, *Decoupling, exponential sums and the Riemann zeta
function*, Journal of the American Mathematical Society **30** (2017),
205--224, DOI 10.1090/jams/860, arXiv:1408.5794v2.

- Primary abstract and HTML source: https://arxiv.org/abs/1408.5794
- Journal DOI: https://doi.org/10.1090/jams/860
- Primary-source audit in this repository:
  `rounds/codex-managed/m9-m1-residual-upper-conductor-hybrid-energy/reports/hybrid_spectral_source_hostile_audit.md`
- Round 81 hypothesis re-audit:
  `rounds/codex-managed/m9-m1-upper-conductor-transition-flattening/reports/transition_gluing_hostile_audit.md`

This is Jean Bourgain's single-author 2017 paper.  It is not the withdrawn
Bourgain--Watt paper recorded separately in `sources/bourgain_watt.md`.

## Exact theorem used

Theorem 4 and the Section 5 refinement, summarized as Theorem 6, give the
exponent pair

\[
 \left(\frac{13}{84}+\varepsilon,
       \frac{55}{84}+\varepsilon\right).
\]

In the source's exponent-sum normalization, for a smooth model phase on a
dyadic interval of length \(M\), phase parameter \(\mathcal T\), and

\[
 \mathcal T^{17/42}\ll M\ll\mathcal T^{1/2},
\]

the resulting interval sum has the exponent-pair bound

\[
 \sum_{m\asymp M}e(\mathcal T F(m/M))
 \ll_\varepsilon
 (\mathcal T/M)^{13/84+\varepsilon}
 M^{55/84+\varepsilon},
\]

under the source's fixed smooth derivative hypotheses.  Section 5 treats a
proper subinterval by extending the phase to the ambient dyadic interval
and using the partial-sum device attributed there to P. Sargos, at an
additional logarithmic cost.

## Exact project specialization

For a fixed admissible residue progression in the order-\(J\) Farey row,
write

\[
 c=r+4b\ell,\qquad \alpha=r/(4b),\qquad
 K_{\kappa,b}=A_{\kappa,b}/(4b)\asymp X.
\]

Then

\[
 \frac{A_{\kappa,b}}{r+4b\ell}
 =\frac{K_{\kappa,b}}{\ell+\alpha},
 \qquad \ell+\alpha\asymp T,
\]

with

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5}.
\]

Take \(M=T\) and \(\mathcal T=K_{\kappa,b}/T\asymp JQ\).  The direct
source range holds because

\[
 \frac{\log M}{\log\mathcal T}=\frac37
 \in\left[\frac{17}{42},\frac12\right].
\]

Moreover \(\mathcal T/M\asymp Q^2\), so the theorem gives uniformly for
every proper subinterval

\[
 \sup_I\left|\sum_{\ell\in I}
 e\!\left(\pm\frac{K_{\kappa,b}}{\ell+\alpha}\right)\right|
 \ll_\varepsilon X^\varepsilon
 Q^{13/42}T^{55/84}
 =X^\varepsilon TQ^{-5/24}.
\]

The logarithmic proper-subinterval loss is absorbed in \(X^\varepsilon\).

## Hypothesis and scope audit

- The reciprocal phase has the required fixed smooth derivative pattern on
  every ambient progression, uniformly in the bounded shift \(\alpha\).
- A smooth or bounded-variation actual weight is inserted only by Abel
  summation after the unweighted interval estimate.
- The ambient length remains \(T\).  The theorem is not rescaled to the
  shorter Farey-neighbor cells.
- Arbitrary bounded weights, neighbor-by-neighbor gluing without global
  variation, and parity transfer between local classes are not licensed.
- The theorem supplies only a one-dimensional progression estimate.  It
  does not close the remaining upper conductors, cone edges, full
  \(M9\!-!M1\), \(M9\), or the Gauss-circle exponent.

## Audit status

`proved_external_dependency` for the scoped reciprocal progression bound
above.  The source is active and distinct from the excluded withdrawn
Bourgain--Watt paper.
