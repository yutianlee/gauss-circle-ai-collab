# Conductor Round 163 adjudication

## 1. Result and terminal decision

**Terminal verdict:** strict_t1_prime_toggle_sector.

Round 163 proves one exact target-safe incidence sector of the literal
squarefree \(t=1\) coefficient.  For fixed \(\kappa>0\), choose at most
one canonical \(L^{-1/2}\)-close pair of opposite-\(\chi_4\) odd prime
factors of each supported product \(N\), and retain the incidences in
which exactly one selected prime lies in the odd character-bearing
factor.  The complete selected subsum is \(O_\kappa(L^{3/2})\).

The round does not prove eligible-pair density, per-block nonemptiness,
the complementary incidence scalar, the full \(t=1\) target, or any
downstream parent.  It also proves route-scoped self-return and leakage
identities for one-prime averaging, unrestricted matching, complement,
and full-divisor completion.  Those controls do not become a second
graph node.

## 2. Exact accepted statement and hypotheses

Let
\[
 J=\sqrt X,\quad y=\lfloor J\rfloor,\quad q_X=X/y^2,\quad
 H=\lfloor yX^{-1/4}\rfloor,\quad 1\ll L\ll H\leq J^{1/2},
\tag{163.A1}
\]
and retain every literal half-open shell, cone, profile, floor, star,
endpoint, parity branch, and zero extension in

\[
 \mathcal S_{L,1}
 =\sum_{N\asymp L^2}\mu^2(N)
  \left(\frac{L^2}{N}\right)^{3/4}e(J\sqrt N)
  \sum_{\substack{d\mid N,\ d\ {\rm odd}\\
                  \sqrt N\leq d\leq2\sqrt N}}
  \chi_4(d)P_N(d),
\tag{163.A2}
\]
\[
 P_N(d)=\eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right).
\tag{163.A3}
\]

The accepted interfaces give
\(\|\eta_L'\|_\infty\ll L^{-1}\), bounded \(C^1\) norms for the fixed
\(\Phi,W\) profiles, bounded amplitudes, and only finitely many hard
faces in one \(L\)-block.

Fix \(\kappa>0\).  For each supported squarefree \(N\), select
lexicographically at most one pair of distinct odd prime divisors
\(\{p_{N,L,\kappa},q_{N,L,\kappa}\}\) with

\[
 \chi_4(p_{N,L,\kappa}q_{N,L,\kappa})=-1,\qquad
 \left|\log\frac{q_{N,L,\kappa}}{p_{N,L,\kappa}}\right|
 \leq\kappa L^{-1/2}.
\tag{163.A4}
\]

The selection depends on fixed \((N,L,\kappa)\), never on a divisor
allocation.  Let \(\mathcal S_{L,1}^{\rm cp}\) be the complete literal
subsum of (163.A2) for which a pair is selected and exactly one selected
prime divides \(d\).  Then

\[
 \boxed{\mathcal S_{L,1}^{\rm cp}\ll_\kappa L^{3/2}.}
\tag{163.A5}
\]

No density, nonemptiness, or complement estimate belongs to (163.A5).

## 3. Proof reproduction and review synthesis

For one qualifying \(N\), write \(m=N/d\) and exchange the selected
primes:

\[
 T_Nd=
 \begin{cases}
 dq/p,&p\mid d,\ q\mid m,\\
 dp/q,&q\mid d,\ p\mid m.
 \end{cases}
\tag{163.A6}
\]

On the complete ambient XOR divisor set, squarefreeness makes this an
integral, fixed-point-free, multiplicity-one involution.  It preserves
\(N\), coprimality, oddness, the even-\(N\) factor \(2\) in \(m\), the
shell, normalization, and phase.  Opposite prime characters give

\[
 \chi_4(T_Nd)=-\chi_4(d).
\tag{163.A7}
\]

For the literal amplitude \(A_N\), zero-extended to every odd divisor,

\[
 \sum_d^\oplus\chi_4(d)A_N(d)
 =\frac12\sum_d^\oplus\chi_4(d)
 \{A_N(d)-A_N(T_Nd)\}.
\tag{163.A8}
\]

The ambient XOR domain in (163.A8), rather than the physical domain
alone, is essential for one-sided partner legs.

Put \(\theta_N=\log(q/p)\).  On a common smooth cell,
\(|\theta_N|\leq\kappa L^{-1/2}\), the ordinary derivative bound for
\(\eta_L\), bounded \(C^1\) norms for \(\Phi,W\), and \(L/H\ll1\) give

\[
 |A_N(d)-A_N(T_Nd)|\ll_\kappa L^{-1/2}.
\tag{163.A9}
\]

At most \(O(L^2)\) ordered integer pairs occur.  A cone, ratio-profile,
dyadic, vertical-profile, endpoint, star, or zero-extension status can
change only in one of finitely many strips

\[
 |d-\lambda m|\ll_\kappa L^{1/2}+1,\qquad
 |d-\lambda L|\ll_\kappa L^{1/2}+1.
\tag{163.A10}
\]

Their union contains \(O_\kappa(L^{3/2}+L)\) pairs.  Floors are
orbitwise fixed, the \(N\)-shell never moves, and arithmetic selectors
only delete pairs.  If one leg is supported, the close partner remains
in a fixed enlarged \(O(L)^2\) box.  Thus

\[
 L^2L^{-1/2}+O_\kappa(L^{3/2}+L)\ll_\kappa L^{3/2},
\]
which proves (163.A5).

All three primary reports independently found the exact prime-toggle
leakage and multi-prime exchange interface.  The discovery and hostile
reports independently proved (163.A5).  The statement-only report,
which did not receive the accepted profile seminorms, correctly stopped
at the profile-difference seam.  Its post-unmask review then reproduced
the profile estimate and every boundary count.  The independent
profile/boundary/power review traced the required regularity to accepted
nodes and found no later \(L\)-dependent transition family.  The graph
review certified one child node, two inconclusive parent attachments,
and no downstream effect.

For a single \(p\equiv3\pmod4\) toggle,

\[
 b_{L,X}(N)=
 \sum_{\substack{d\mid N/p\\d\ {\rm odd}}}
 \chi_4(d)\{A_N(d)-A_N(pd)\},
\tag{163.A11}
\]
and the supports are disjoint.  Averaging (163.A11) over every such
\(p\mid N\) reinforces each active term once per prime and returns the
original coefficient exactly.  General sign-reversing divisor-cube
averages have the same character-eigenvalue self-return.  Matching
cycles rewrite profile gradients and can leave sign-count/Hall defects.
Odd complement lies in \([\sqrt N/2,\sqrt N]\); for \(N=2M\), physical
complement is even and odd-part complement lies in
\([\sqrt N/4,\sqrt N/2]\).  These are scoped route obstructions only.

## 4. First doubtful or unproved step

The first open physical quantity is

\[
 \mathcal S_{L,1}^{\rm rem}
 :=\mathcal S_{L,1}-\mathcal S_{L,1}^{\rm cp},
\tag{163.A12}
\]
which consists of every product with no qualifying canonical pair and,
on qualifying products, every incidence containing neither or both
selected primes.  No artifact proves

\[
 |\mathcal S_{L,1}^{\rm rem}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\tag{163.A13}
\]

A density theorem alone would not prove (163.A13), because the residual
still carries its literal weights and arbitrary-real-centre phase.
Even (163.A13) would settle only the \(t=1,D\asymp L^2\) face; the
compatible \(L\ll D\ll L^2,\ t\ll\sqrt L\) channels and near collars
would remain.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| product grouping and multiplicity | GREEN: one squarefree divisor allocation, one canonical pair, one two-cycle. |
| sign and parity | GREEN: (163.A7); only odd primes move and the even branch is preserved. |
| common-cell profiles | GREEN: ordinary \(\eta_L\) derivative, bounded \(C^1\) \(\Phi,W\), and \(L/H\ll1\) prove (163.A9). |
| hard faces and partner tails | GREEN: every literal crossing is in (163.A10), including zero-extended partner legs, floors, stars, ceilings, and ties. |
| target power | GREEN: common cells and all crossings total \(O_\kappa(L^{3/2})\). |
| density and complement | OPEN and expressly absent from the theorem. |
| one-prime and graph averaging | GREEN obstruction: exact coherent self-return, not cancellation. |
| complement and full-divisor completion | GREEN obstruction: excluded lower windows and uncontrolled complement. |
| physical versus diagnostic | GREEN: constant-profile and PNT counts prove no literal lower mass. |
| downstream scope | GREEN: no full \(t=1\), remaining channel, parent, smooth packet, M9--M2, M9, bridge, target, or exponent promotion. |
| resource allocation | GREEN: 100% analytic/algebraic, 0% numerical. |

## 6. Dependencies and selected evidence

The accepted proof kernel is
proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md.

Primary reports:

- reports/literal_near_square_divisor_involution_attack.md;
- reports/blind_near_square_divisor_rederivation.md;
- reports/prime_toggle_complement_leakage_hostile_audit.md.

Selected candidate and conductor control:

- candidates/conductor_round163_close_opposite_prime_exchange_sector.md;
- controls/conductor_round163_reproduction_and_selection.md.

Independent reviews:

- reviews/blind_post_unmask_close_pair_sector_review.md;
- reviews/profile_boundary_power_seam_review.md;
- reviews/downstream_graph_scope_review.md.

The graph dependencies are
M9-M2-hard-top-t1-character-poisson-product-collar-obstruction,
M9-M2-top-endpoint-actual-symbol-variation, and H4-Phi-regularity.
No external theorem or computation enters (163.A5).

## 7. State decision and next action

Create one proved-internal lemma,
M9-M2-hard-top-t1-close-opposite-prime-exchange-sector, with the three
accepted dependencies above.  Attach it only as a dependency and
inconclusive evidence to M9-M2-top-endpoint-signed-cone and
M9-M2-top-endpoint-density-discrepancy-energy.  Both remain open.

Record the exact rejected overclaims identified by the graph review.
Leave every antecedent, remaining few-point channel, smooth packet,
assembly, M9 component, bridge, target, and exponent unchanged.  The
next action is (163.A13), followed by—not substituted for—the remaining
few-point channels.
