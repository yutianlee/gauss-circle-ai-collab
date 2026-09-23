# Round 166 full-proof strategy and current-literature review

## Purpose

Round 166 is the scheduled three-round strategy checkpoint.  It is not
licensed to promote an open estimate by analogy or to continue the next
analytic round automatically.  It must reconstruct the complete accepted
proof tree, audit current primary literature against the exact surviving
interfaces, and choose one frozen Round-167 inequality only after the
review closes.

Starting graph:
87d58660e7e11a23eb3d8759917e02376479ba38acaf727b0a2dc15d5920f5e0.

## Accepted global architecture

The quarter theorem remains conditional on the accepted reductions plus
M9.  The standard M9 route requires:

1. both direct M9--M1 parents;
2. all three M9--M2 parents: hard TOP, BAL, and UNBAL; and
3. endpoint uniformity.

The alternative global route replaces blockwise M9--M1 by the complete
GAR theorem, but still requires all of M9--M2.  It does not prove the
blockwise M9 node.

## Newly sharpened hard-TOP interface

Rounds 164--165 replace coefficient-uniform transport by exact
actual-direction Fejer interfaces.  At
\(R_0=\lceil L\rceil\), parity, the monotone tangent sector, and the
fixed-fraction high-divisor-gcd sector reduce the residual scalar to the
open estimate

\[
 \Re\mathfrak C_{R_0,2,{\rm opp},\,g<\gamma L}^{\rm rem}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.
\tag{166.S1}
\]

At \(R=M_L\asymp L^2\), short shifts can be paid and it is alternatively
sufficient to prove

\[
 \Re\sum_{\substack{R_0\le r<M_L\\2\mid r}}
 \left(1-\frac r{M_L}\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)
 \ll_\varepsilon L^3X^\varepsilon.
\tag{166.S2}
\]

Both are open, and either would close only the complete residual scalar.
The other few-point hard-TOP channels and near collars would still need
separate owners before either hard-TOP parent could close.

## Comparison questions

The review must compare, with explicit power and owner ledgers:

1. minimal-scale (166.S1);
2. maximal-scale (166.S2);
3. a direct full residual scalar theorem outside Fejer;
4. the remaining hard-TOP channels after a residual theorem;
5. BAL and UNBAL;
6. the two direct M1 parents;
7. the GAR alternative; and
8. any route to a certified exponent below \(1/3\) that does not falsely
   advertise local progress as a global theorem.

For each route record:

- exact input and output owner;
- target size and present positive capacity;
- already rejected mechanisms;
- one genuinely new mechanism needed;
- whether an external theorem could apply literally;
- number and severity of downstream owners still left; and
- effect on the internal exponent if every stated connector, but no
  unstated one, were proved.

## Literature standard

Search current primary sources, prioritizing official journal pages,
author manuscripts, and arXiv.  Secondary summaries may locate a source
but cannot certify a theorem.  For every candidate record:

- exact theorem number and statement;
- parameter ranges and coefficient class;
- pointwise, averaged, or almost-all quantifiers;
- absolute-value placement;
- smoothness, support, and endpoint hypotheses;
- character/modulus restrictions;
- the literal project parameter map;
- every completion or boundary cost; and
- the first failed hypothesis.

The search must include recent work on the Gauss circle problem and
closely relevant primary results on square-root exponential sums,
shifted-divisor correlations, character-twisted bilinear forms,
Kloosterman/Salié dispersion, spectral shifted convolution, and
large-sieve or decoupling estimates.  Structural resemblance is not
applicability.

## Selection rule

Round 167 receives exactly one analytic objective.  Prefer the route with
the smallest exact missing theorem, the strongest owner leverage, and a
credible new cancellation mechanism not already parked.  A rigorous
decision to rotate away from (166.S1) is useful progress.  No graph status
changes merely because a route is ranked first.

The review closes under exactly one label:

- strategy_frontier_retained;
- strategy_frontier_reselected; or
- strategy_source_update_only.
