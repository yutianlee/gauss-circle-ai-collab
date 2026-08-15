# Round 69 conductor adjudication

## Decision

Promote the fixed-interior direct Poisson/product-wavelet return and its
strictly improved (X^{7/20+arepsilon}) bound at the benchmark
(Q=X^{1/5}). Retain the requested (Q^{3/2}X^arepsilon) estimate
open. No report proves the missing (X^{1/20}) saving, and no tested
actual-symbol resonance disproves it.

## Accepted normalization and return

With (J=sqrt X), (T=J/Q),

\[
 \mathcal T_Q=
 \sum_{k,q}\chi_4(q)\beta(k/Q)C(k/q)e(\sqrt{Xkq}),
 \qquad C(y)=y^{3/4}\Xi(2\sqrt y),
\]

the original wavelet antecedent is

\[
 \mathcal B_{\mathrm{main}}
 =\mathfrak u\,{\sqrt J\over Q^{3/2}}\mathcal T_Q.
\]

Direct ordinary Poisson in (k), character Poisson in (q), and the
fixed-sector angular stationary expansion give

\[
 \mathcal T_Q=e(1/8){Q^{3/2}\over J^{1/2}}\mathcal W_Q
 +O((QJ)^{-1/2}X^\varepsilon),
\]

where, in one exact stationary coordinate system,

\[
 \mathcal W_Q=
 \sum_{m>J}\sum_{\substack{r<J\\r\ \mathrm{odd}}}
 \chi_4(r)\Xi(J/m)
 K_\beta\!\left({m\over J}{X-mr\over T}\right)
\]

with fixed compact ratio restrictions. The independently rederived
accepted inverse-transform plus (k)-Poisson route gives the same
fixed-centre near-product class and the same normalization. The two
weights agree on the critical manifold; their off-centre forms belong
to the audited fixed-symbol expansion and must not be identified by an
unproved arbitrary-symbol theorem.

Every stationary correction retains a compact radial Fourier integral
and is Schwartz in ((mr-X)/T). Divisor grouping therefore makes the
first omitted term (O((QJ)^{-1/2}X^arepsilon)); the hostile report's
initial (J^2)-cell overcount was corrected before adjudication.

## Exact capacity

The divisor bound gives

\[
 |\mathcal W_Q|\ll (1+T)X^\varepsilon,
 \qquad
 |\mathcal T_Q|\ll
 Q^{3/2}J^{-1/2}(1+J/Q)X^\varepsilon.
\]

At (J=X^{1/2}), (Q=X^{1/5}), this is
(X^{7/20+arepsilon}=Q^{7/4}X^arepsilon). The target is
(X^{3/10+arepsilon}=Q^{3/2}X^arepsilon). Thus the exact survivor is

\[
 \mathcal W_Q\ll J^{1/2}X^\varepsilon,
\]

which asks for the factor (J^{1/2}/Q=X^{1/20}) beyond absolute
near-product counting. Averaging the unsigned actual-profile incidence
over the centre realizes order (T), so an all-absolute proof cannot
supply this factor.

## Geometry and source controls

The phase (J\sqrt{kq}) has identically zero two-dimensional Hessian
determinant. Its dual stationary aliases satisfy the near-hyperbola
condition (mr=X+O(TX^arepsilon)), so a nondegenerate Hessian theorem
is inapplicable. Exact products are divisor-safe; square-product and
fourth-power fibres have only (O(Q^{1+arepsilon})) and
(O(Q^{1/2+arepsilon})) capacity.

The primary-source audit found no closing import. Kumchev's quoted
Sargos--Wu bilinear bound contains a (Q^2) term; the applicable
Robert--Sargos/Fouvry--Iwaniec-method mapping has an (X^{17/40}) term;
the best audited Tao--Trudgian--Yang rowwise exponent is
(X^{0.388883\ldots}); and short-divisor/Voronoi results either have the
wrong coefficient, average the centre, or merely reproduce a transform.

## Scope

The promoted statement is fixed smooth interior only. The signed
near-product estimate, cone edges, remaining radial sectors, GAR,
M9--M1, M9, and the Gauss-circle exponent remain open.

