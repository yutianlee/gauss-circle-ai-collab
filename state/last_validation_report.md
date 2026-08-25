# Last validation report

## Round and graph

- Round: 163
- Campaign: m9-m2-hard-top-t1-near-square-divisor-involution-gate
- Starting graph:
  700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358
- Resulting graph:
  81690ebb72b0dedd99bdb6c6127f947df696a901a22af3f65ac8738209125306
- Terminal label: strict_t1_prime_toggle_sector

## Promoted mathematics

For every fixed \(\kappa>0\) and supported squarefree \(N\), select
canonically at most one pair of distinct odd prime factors \(p,q\) with

\[
 \chi_4(pq)=-1,\qquad |\log(q/p)|\leq\kappa L^{-1/2},
\]

using \((N,L,\kappa)\) but not the divisor allocation.  On the complete
incidence set where exactly one selected prime belongs to the odd
character-bearing divisor \(d\), exchanging \(p\) and \(q\) between
\(d\) and \(N/d\) is integral, fixed-point-free, and multiplicity one.
It preserves \(N\), squarefreeness, coprimality, parity, the even-\(N\)
branch, normalization, shell, and \(e(J\sqrt N)\), and reverses
\(\chi_4(d)\).

With the literal amplitude extended by zero, exact pairing gives

\[
 \sum_d\chi_4(d)A_N(d)
 =
 \frac12\sum_d\chi_4(d)\{A_N(d)-A_N(T_Nd)\}.
\]

The close-prime condition moves a divisor by \(O_\kappa(\sqrt L)\).
On common smooth cells, accepted ordinary profile derivatives yield
\(O_\kappa(L^{-1/2})\) amplitude difference.  The ambient incidence
count is \(O(L^2)\).  Every cone, dyadic, profile, endpoint, star,
ceiling, and zero-extension crossing belongs to finitely many lattice
collars with \(O_\kappa(L^{3/2}+L)\) points.  Therefore

\[
 \boxed{|\mathcal S_{L,1}^{\mathrm{cp}}|
 \ll_\kappa L^{3/2}}
\]

uniformly in the real centre.

## Qualified route obstruction

A single \(p\equiv3\pmod4\) toggle cannot keep both legs in the
multiplicative-width-two window.  Normalized averaging over all such
toggles or any family of full divisor-lattice sign-reversing involutions
returns the original coefficient.  General exchange matching requires
equal character-sign counts, while cycles only rewrite profile gradients
and unmatched terms.  Odd and even complementary divisors enter excluded
lower intervals, and full-divisor character vanishing leaves an
uncontrolled profiled complement.

These are route facts, not a physical lower bound and not a theorem that
all future divisor or cross-product mechanisms fail.

## Remaining gap and scope

No eligible-pair density, per-block nonemptiness, positive proportion, or
complement estimate is proved.  The exact first survivor is

\[
 \mathcal S_{L,1}^{\mathrm{rem}}
 =\mathcal S_{L,1}-\mathcal S_{L,1}^{\mathrm{cp}},
\]

containing every no-pair product and every neither-prime and both-prime
incidence.  Its literal profiles, parity, boundaries, floors, stars,
endpoints, zero extension, and arbitrary-real-centre phase remain open.

Even a complete residual target estimate would leave the
\(L\ll D\ll L^2,\ t\ll\sqrt L\) few-point channels.  Hard TOP, BAL,
UNBAL, M9--M2, M9--M1, endpoint uniformity, M9, the bridge, and the
quarter theorem are unchanged and open.

The strongest internally proved global exponent remains \(1/3\).  The
audited external benchmark remains
\(0.3144831759740614\ldots\).

## State mutation

The validated State Patch applied:

- 1 obligation creation;
- 2 obligation updates;
- 0 rejected-claim corrections;
- 16 fresh rejected-inference records; and
- 19 explicit no-change decisions.

Both updated hard-TOP parents remain open and receive only a dependency
and inconclusive evidence.  The accepted proof draft was updated only
after graph mutation.

## Validation

- Three primary reports, conductor reproduction, statement-only
  post-unmask review, profile/boundary/power review, downstream graph
  review, conductor adjudication, and terminal State Patch review certify
  the scoped result.
- Dry and applied patch validation, graph validation, and completed
  campaign validation pass.
- Seven structured JSON/YAML files parse, Python compilation passes, and
  all 6 unit tests pass.
- All 20 campaign, kernel, and strategy Markdown files generate MathJax
  previews.
- The 20 files contain 160 per-file-unique equation tags, 232 balanced
  display pairs, zero double-dollar tokens, and no byte, whitespace,
  delimiter, or duplicate-tag issue.
- Git diff check passes with line-ending conversion notices only.

Full evidence is under
rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/.
