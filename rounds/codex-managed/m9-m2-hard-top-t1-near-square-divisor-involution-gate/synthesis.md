# Round 163 synthesis: a target-safe close-prime incidence sector and the exact residual

Round 163 closes under **strict_t1_prime_toggle_sector**.  The validated
State Patch creates one proved-internal lemma, updates only the two open
hard-TOP parents with dependency and inconclusive evidence, records
sixteen rejected overclaims, and preserves nineteen explicit no-change
decisions.  The resulting graph is
81690ebb72b0dedd99bdb6c6127f947df696a901a22af3f65ac8738209125306.

## What was proved

Fix \(\kappa>0\).  For each supported squarefree product \(N\), choose
canonically at most one pair of distinct odd prime factors \(p,q\) such
that

\[
 \chi_4(pq)=-1,\qquad |\log(q/p)|\leq\kappa L^{-1/2},
\]

using \((N,L,\kappa)\) alone.  Restrict the literal physical divisor
coefficient to incidences in which exactly one of \(p,q\) belongs to the
odd character-bearing divisor \(d\).  Exchanging \(p\) and \(q\) between
\(d\) and \(N/d\) is integral, fixed-point-free, multiplicity one, and
preserves squarefreeness, coprimality, \(N\), parity, the even-\(N\)
branch, product normalization, and \(e(J\sqrt N)\), while reversing
\(\chi_4(d)\).

For the complete zero-extended literal amplitude \(A_N(d)\), the exact
identity is

\[
 \sum_{d\in\mathscr D_N^\oplus}\chi_4(d)A_N(d)
 =
 \frac12\sum_{d\in\mathscr D_N^\oplus}
 \chi_4(d)\{A_N(d)-A_N(T_Nd)\}.
\]

The prime closeness moves \(d\) by \(O_\kappa(\sqrt L)\).  On common
smooth cells the accepted ordinary derivative of the dyadic profile and
the bounded \(C^1\) interfaces of \(\Phi\) and \(W\) give an
\(O_\kappa(L^{-1/2})\) amplitude difference.  There are \(O(L^2)\)
ambient incidences.  All cone, dyadic, profile, endpoint, star, ceiling,
and zero-extension crossings lie in finitely many lattice collars of
width \(O_\kappa(\sqrt L+1)\), containing
\(O_\kappa(L^{3/2}+L)\) incidences.  Therefore

\[
 \boxed{|\mathcal S_{L,1}^{\mathrm{cp}}|
 \ll_\kappa L^{3/2}}
\]

uniformly in the arbitrary real centre.  This is a literal target-safe
sector; it is not a model or a positive-capacity diagnostic.

## What was ruled out

The hostile audit gives exact route obstructions:

- a one-prime \(p\equiv3\pmod4\) toggle cannot have both legs in the
  multiplicative-width-two physical window;
- normalized averaging over all one-prime toggles, or over any family of
  sign-reversing full divisor-lattice involutions, is exact self-return;
- a general exchange graph has a perfect matching only when its two
  character-sign classes have equal size, and matching cycles merely
  rewrite profile gradients and unmatched terms;
- odd complementation enters the excluded lower window, while for
  \(N=2M\) the physical complement is even and the odd-part complement
  lies in \([\sqrt N/4,\sqrt N/2]\); and
- full-divisor character vanishing leaves an uncontrolled profiled
  complement.

These are route facts attached to the accepted sector lemma, not a second
obligation and not a physical lower bound.

## Exact remaining problem

No eligible-pair density, per-block nonemptiness, positive proportion, or
complement estimate was proved.  The first open scalar is

\[
 \mathcal S_{L,1}^{\mathrm{rem}}
 =\mathcal S_{L,1}-\mathcal S_{L,1}^{\mathrm{cp}},
\]

containing every no-pair product and every neither-prime or both-prime
incidence.  Its arbitrary-real-centre phase, profiles, parity, hard
boundaries, floors, stars, endpoints, and zero extension must remain
literal.  Mining another unquantified sparse sector would not close this
owner; the next useful mechanism must control the complete residual or
prove a quantitative transport/unmatched-mass obstruction.

Even a target estimate for the entire \(t=1\) residual would leave the
compatible \(L\ll D\ll L^2,\ t\ll\sqrt L\) few-point channels and their
near collars open.  Hard TOP therefore remains open.

## Full proof status

The three mandatory M9--M2 parents remain open:

1. hard-TOP signed-cone/density-discrepancy control;
2. balanced smooth quarter-packet control; and
3. unbalanced smooth three-quarter control.

M9--M1 remains open at its two direct blockwise parents, with the
alternative global-M1/GAR route also incomplete.  Endpoint uniformity,
M9, the conditional bridge, and the Gauss-circle quarter theorem remain
open.

The strongest internally proved global exponent remains \(1/3\).  The
separately audited external benchmark remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\]

No global exponent changed in Round 163.

## Validation and state effect

The three primary reports, conductor reproduction, statement-only
post-unmask review, profile/boundary/power review, downstream graph review,
conductor adjudication, dry patch validation, and terminal patch-scope
audit are green.  No numerical experiment or external theorem was used.

The accepted kernel is
proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md.
The State Patch creates only
M9-M2-hard-top-t1-close-opposite-prime-exchange-sector and attaches it as
a dependency and inconclusive evidence to
M9-M2-top-endpoint-signed-cone and
M9-M2-top-endpoint-density-discrepancy-energy.  Both parents remain open;
no blocker was removed.

## Next research interface

The proposed Round-164 interface is the complete signed residual
\(\mathcal S_{L,1}^{\mathrm{rem}}\).  A canonical monotone transport
between its positive and negative physical divisor masses should be
tested at the level of total logarithmic displacement and unmatched mass.
The exit must be either a target residual estimate, an owner-complete
quantitative residual sector, or a sharp transport-capacity no-go—not
another arbitrary sparse matching.
