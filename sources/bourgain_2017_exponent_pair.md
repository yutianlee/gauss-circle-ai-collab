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

## Exact theorems and their distinct ranges

Theorem 4 first proves the relevant estimate directly in the source window

\[
 \mathcal T^{17/42}\ll M\ll\mathcal T^{1/2}.
\]

Section 5 then removes that window as a restriction on the exponent-pair
statement.  Theorem 6 states that

\[
 \left(\frac{13}{84}+\varepsilon,
       \frac{55}{84}+\varepsilon\right)
\]

is an exponent pair.  In the source's normalization, for an admissible
exponent-pair phase on a dyadic interval of length \(M\), phase parameter
\(\mathcal T\), and \(1\le M\le\mathcal T\), this gives

\[
 \sum_{m\asymp M}e(\mathcal T F(m/M))
 \ll_\varepsilon
 (\mathcal T/M)^{13/84+\varepsilon}
 M^{55/84+\varepsilon}.
\]

Theorem 6 is not confined to the direct Theorem-4 window.  Section 5
explicitly treats \(M>\mathcal T^{1/2}\): it uses a near-square rescaling,
the pair \((1/2,1/2)\) in the extreme long range, and a Poisson/partial-
summation exponent-pair \(B\)-process in the remaining long range, using
that the new pair is fixed by \(B\).  It treats a proper subinterval by
extending the phase to the ambient dyadic interval and using the partial-sum
device attributed there to P. Sargos.  The latter costs only a logarithm.
These extensions require the standard exponent-pair derivative class; they
are not assertions for arbitrary smooth phases.

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

Take \(M=T\) and \(\mathcal T=K_{\kappa,b}/T\asymp JQ\).  This particular
specialization already lies in the direct Theorem-4 source range because

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
- The global Theorem-6 interface may be used outside the direct
  \(\mathcal T^{17/42}\ll M\ll\mathcal T^{1/2}\) window only after checking
  the same standard exponent-pair derivative class, the convention
  \(M\le\mathcal T\), and the proper-subinterval construction.  A fixed
  comparable edge with \(\mathcal T<M\) must be covered separately, not by
  silently violating the convention.
- A smooth or bounded-variation actual weight is inserted only by Abel
  summation after the unweighted interval estimate.
- The ambient length remains \(T\).  The theorem is not rescaled to the
  shorter Farey-neighbor cells.
- Arbitrary bounded weights, neighbor-by-neighbor gluing without global
  variation, and parity transfer between local classes are not licensed.
- The theorem supplies only a one-dimensional progression estimate.  It
  does not close the remaining upper conductors, cone edges, full
  \(M9\!-!M1\), \(M9\), or the Gauss-circle exponent.

## Round-151 reciprocal-row specialization

For the exact compressed reciprocal row, after Mobius inversion write
\(q=c(4n+a)\), \(a\in\{1,3\}\), with interval length
\(H_c\asymp LQ/c\) and phase \(NdL/[c(4n+a)]\).  Its scaled derivative
parameter satisfies

\[
 \mathcal T_c\asymp Nd/Q,
 \qquad \mathcal T_c/H_c\asymp cE/L.
\]

The shifted reciprocal is uniformly in the standard exponent-pair class,
and Section 5 supplies every proper subinterval.  On the part with
\(\mathcal T_c\ge H_c\), Theorem 6 applies directly.  The finite comparable
upper-support edge where \(\mathcal T_c<H_c\) is covered by the stronger
second-derivative estimate because \(55/84>1/2\).  Bounded-variation actual
weights are inserted only afterwards by Abel summation.  Consequently the
global pair, not merely Theorem 4's direct window, gives the all-\(L\) row
bound used in Round 151.

## Audit status

`proved_external_dependency` for the global Theorem-6 exponent-pair
interface after the derivative-class, interval, and \(M\le\mathcal T\)
checks above.  The source is active and distinct from the excluded withdrawn
Bourgain--Watt paper.  The earlier project wording that inherited the
Theorem-4 window as the scope of Theorem 6 is corrected by the Round-151
primary-source audit.
