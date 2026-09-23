# Round 172 synthesis

Campaign: m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate

Starting graph:
c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853

Terminal label: maximal_fejer_dyadic_character_poisson_no_go

## Outcome

The maximal even medium/long residual aggregate (165.K26) remains open.
Round 172 proves the exact parity--Fejer stopped-chain and literal
common-frequency transform required to state its first unresolved signed
dual family without hidden endpoint or diagonal losses.

For

\[
 \mathfrak E_R^{(2)}
 =D_L+2\!\sum_{\substack{0<r<R\\2\mid r}}
 \left(1-\frac rR\right)A_r,
\]

the stopped chain \(R_{j+1}=\min(2R_j,M)\) gives

\[
 T_{26}
 =\frac12\sum_j
 \left(\mathfrak E_{R_{j+1}}^{(2)}
       -\mathfrak E_{R_j}^{(2)}\right)-B_{\rm short},
 \qquad
 |B_{\rm short}|\ll_\varepsilon L^3X^\varepsilon.
\]

The exact \(R<S\le2R\) link has zero diagonal and weight

\[
 b_{R,S}(r)=
 \begin{cases}
 r(S-R)/(RS),&0<r<R,\\
 1-r/S,&R\le r<S,\\
 0,&r\ge S.
 \end{cases}
\]

At a doubling this is the triangular tent and has the exact
absolute-site-parity Haar representation.  A strict terminal link uses the
displayed Fejer difference.  The first link and the one short correction
are target-safe, but have no owner-complete target-safe complement.

## Exact transform and first open seam

A disjoint real-cardinal interpolation of the complete literal residual
coefficient gives

\[
 Z_\epsilon(\theta)=\frac i2
 \sum_{k\ {\rm odd}}\chi_4(k)\sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).
\]

After squaring and parity averaging, the exact link coefficient is \(1/8\)
with one real part around the full dual aggregate.  The ordinary-zero-
containing sector is \(O_\varepsilon(L^3X^\varepsilon)\), but only after
all signed odd character frequencies are recombined.  It is not a
standalone owner or the Round-169 scalar zero mode.

The first open transformed object is

\[
 \mathcal N_{R,S}
 =\frac18\Re\sum_{\epsilon=0}^1
 \sum_{k,k'\ {\rm odd}}\sum_{\ell,\ell'\ne0}
 \chi_4(k)\chi_4(k')
 \int_0^1B_{R,S}(\theta)
 U_{k,\ell}^{(\epsilon)}(\theta)
 \overline{U_{k',\ell'}^{(\epsilon)}(\theta)}\,d\theta.
\]

The zero physical diagonal does not delete a fixed dual diagonal, because
the two cardinal variables remain independent and their product difference
is generally noninteger.  Physical cancellation appears only after the
complete dual, cell, endpoint, transition, and zero-extension assembly
recombines.

## Route obstruction

Fejer positivity gives an available maximal-link scale
\(MD_L\ll_\varepsilon L^4X^\varepsilon\).  This is sharp at order
\(L^4\) for the coefficient-uniform envelope: on the admissible
\(M=4P\) stopped-chain subfamily, a dechirped sequence on the \(2P\)
sites of one absolute parity has

\[
 \mathfrak E_{4P}^{(2)}-\mathfrak E_{2P}^{(2)}
 =P^2=\frac18MD_L.
\]

This sequence is not the literal residual coefficient and is not a
physical lower bound.  It rules out only a continuation which, before
proving an actual-symbol saving, replaces the signed nonzero family by a
coefficient-uniform positive norm over modes, cells, openings, or common
frequency.  Cross-link cancellation and a coefficient-sensitive literal
positive theorem remain possible.

At either centred Fejer peak the smooth-interior product phase has

\[
 \det\operatorname{Hess}
 \{J\sqrt{uv}+\phi uv-\xi u-\eta v\}
 =-\phi^2-\frac{J\phi}{2\sqrt{uv}},
\]

so a fixed lawful smooth-interior opening returns at \(\phi=0\) to the
accepted rank-one product collar.  This statement does not replace or
estimate the full cardinal, noncentral, endpoint, or transition family.

## Review resolution

The report repairs corrected the initial out-of-range sharpness example,
first-link endpoint scope, overstrong owner language, absolute-link
necessity wording, and the hostile report's transform ordering.  Independent
parity and transform post-repair checks are GREEN.

Three final kernel reviews checked normalization, transform, endpoint,
power, counterexample, collar, and owner seams.  The durable kernel was
locally repaired to extend the bandpass weight evenly, separate an upper
capacity from its sharp diagnostic family, rebudget epsilon losses, and
narrow collar return to its accepted smooth-interior fixed-opening scope.
The final mathematical and transform verifications are GREEN:

proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md.

## State effect

Create one proved-internal route obstruction:

M9-M2-hard-top-t1-residual-maximal-fejer-dyadic-positive-transform-obstruction.

Add it only as an inconclusive dependency/evidence constraint to the two
open hard-TOP endpoint interfaces that already inherit the residual Fejer
route.  Do not create separate first-link or ordinary-zero owners and do
not add an implication edge.

No residual target, hard-TOP parent, BAL, UNBAL, M9--M2, direct M1 parent,
GAR, endpoint assembly, M9, bridge, theorem, or exponent is promoted.

## Full-proof status

The Gauss circle conjecture is not proved.  The exponent ledger is
unchanged:

- internal: \(1/3\);
- accepted repaired external benchmark:
  \(0.3144831759740614\ldots\);
- target: \(1/4\).

The next round may be selected only after the Round-172 State Patch passes
independent scope review, applies to the authoritative graph, and passes
the exact reverse audit.
