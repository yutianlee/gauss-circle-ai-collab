# Round 114 discovery: literal full-product energy and double-corridor connector

## 1. Result: exact connector and target-safe narrow lemma

For the literal Round-113 balanced block, the complete smooth low-gcd
packet has the exact original-coordinate form

\[
 Z_B(R)=2iT_B,
 \qquad
 T_B=\sum_{h,k}a_B^{<}(h,k)e(R\sqrt{hk}),
 \tag{114.A1}
\]

\[
 a_B^{<}(h,k)=\chi _4(h)
 \eta\!\left(\frac{(h,k)}{\sqrt L/2}\right)A_B(h,k).
 \tag{114.A2}
\]

Thus there is no missing datum in the squared object: its algebraic
phase diagonal is equality of the **full** products (hk=h'k'), or
(g^2uv=g'^2u'v'), and its exact one-dimensional coefficient is

\[
 c_B(n)=\sum_{hk=n}a_B^{<}(h,k).
 \tag{114.A3}
\]

The equal-full-product energy satisfies

\[
 E_{\rm prod,0}=\sum_n|c_B(n)|^2
 \ll_\varepsilon L^2X^\varepsilon,
 \tag{114.A4}
\]

one full factor (L) below the required energy budget (L^3X^\varepsilon).

There are two further exact target-safe corridors.  Put

\[
 \delta=h'k'-hk,
 \qquad
 \rho=hk'-h'k.
 \tag{114.A5}
\]

For every (1\le Q\ll L^2), uniformly for (K/L) in a fixed compact
subset of ((0,\infty)),

\[
 \sum_{|\delta|\le Q}|a_B^{<}(h,k)a_B^{<}(h',k')|
 +\sum_{|\rho|\le Q}|a_B^{<}(h,k)a_B^{<}(h',k')|
 \ll_\varepsilon L^2(Q+1)X^\varepsilon.
 \tag{114.A6}
\]

In particular, (Q=L) makes the union of the shifted-full-product and
determinant-narrow corridors target-safe in the exact packet energy.  The
determinant is a literal ray variable, because in primitive coordinates

\[
 \rho=gg'(uv'-u'v).
 \tag{114.A7}
\]

The rational-ray slice (\rho=0) is even smaller,
(O_\varepsilon(L^2X^\varepsilon)), and retains the actual quarter-shift
character as a square of a one-dimensional (g)-sum along each primitive
ray.

There is also an exact finite-divisor chart for the remaining pairs.  If
(p=h'-h) and (q=k'-k), then

\[
 \delta+\rho=q(h+h'),\qquad
 \delta-\rho=p(k+k').
 \tag{114.A8}
\]

The axial cases (p=0) or (q=0) have only (O(L^3)) pairs and are
target-safe absolutely.  Away from them, a fixed ((\delta,\rho)) has at
most (X^\varepsilon) representations.  This isolates the smallest lawful
broad survivor:

\[
 |\delta|>L,\qquad |\rho|>L,
 \qquad p q\ne0.
 \tag{114.A9}
\]

The chart has coefficient-blind capacity (L^4X^\varepsilon), not
(L^3X^\varepsilon).  Hence it does not prove the broad estimate.  A
bounded real phase-adapted coefficient array makes the broad survivor
itself have size \(\gg L^4\) in energy after the target-safe corridors are
removed.  Therefore no estimate based only on support, boundedness, the
rank-one identity, or divisor multiplicity can close the route.  The first
unproved step is a genuinely actual-symbol estimate saving one factor
(L) on (114.A9).  No balanced estimate or exponent improvement follows.

## 2. Exact statement and hypotheses

Let (X\ge4096) be real, (R=\sqrt X), and let (B) be one fixed
Round-113 full smooth balanced physical block.  For the persistent label
(j=1),

\[
 D=\frac{\lfloor R\rfloor}{2},\qquad
 \frac KL=4\frac{X}{\lfloor R\rfloor^2},
 \tag{114.A10}
\]

and the critical scale is (L\asymp R^{1/3}).  The same statements below
are uniform for the isolated exact-square (j=2) boundary (K/L=16).
Write (G_0=\sqrt L/2).  The real symbol (A_B) is the literal symbol in
the Round-113 dictionary; in particular it is supported in a fixed
comparability box

\[
 h\asymp L,\qquad k\asymp K\asymp L,
 \tag{114.A11}
\]

possibly further restricted by its slanted smooth support, and
(|A_B(h,k)|\ll1).  Define (114.A2), including the actual Vaaler taper,
floors, smooth gcd bottom, and slanted profile through (A_B).  No square
or near-square mask is inserted into this coefficient.

Then the following assertions hold.

1. Equations (114.A1)--(114.A3) are coefficientwise identities.  Moreover

   \[
   |T_B|^2=\sum_{h,k,h',k'}a_B^{<}(h,k)
   \overline{a_B^{<}(h',k')}
   e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right),
   \tag{114.A12}
   \]

   and grouping by (n=hk) gives

   \[
   |T_B|^2=\sum_r\sum_n c_B(n)\overline{c_B(n+r)}
   e\!\left(R(\sqrt n-\sqrt{n+r})\right),
   \tag{114.A13}
   \]

   with the natural positivity and support restrictions on (n+r).

2. The (r=0) term is (114.A4).  For any real (Q\ge0), each of the two
   absolute corridor masses in (114.A6) is
   (O_\varepsilon(L^2(Q+1)X^\varepsilon)).

3. With (h'=h+p, k'=k+q), define

   \[
   P=1+\frac12\left(\frac ph+\frac qk\right),\qquad
   Q_*=\left(1+\frac ph\right)\left(1+\frac qk\right).
   \]

   Then the literal square-root rank-one identity is

   \[
   \sqrt{h'k'}-\sqrt{hk}
   -\frac12\sqrt{\frac kh}\,p
   -\frac12\sqrt{\frac hk}\,q
   =-\frac{\rho^2}
   {4(hk)^{3/2}(P+\sqrt{Q_*})}.
   \tag{114.A14}
   \]

   Here (P+\sqrt{Q_*}\asymp1) on the fixed support.

4. If the target-safe set is

   \[
   \mathcal N=\{|\delta|\le L\}\cup\{|\rho|\le L\}
   \cup\{p=0\}\cup\{q=0\},
   \tag{114.A15}
   \]

   then the sub-sum of (114.A12) over (mathcal N) is
   (O_\varepsilon(L^3X^\varepsilon)), even after taking absolute values
   term by term.  The desired balanced result is reduced, but not proved,
   to the same bound for the complementary actual-symbol sum.

The direct linear target is (|Z_B|\ll L^{3/2}X^\varepsilon).  Since
(|Z_B|^2=4|T_B|^2), its squared budget is (L^3X^\varepsilon); constant
factors are harmless, but the linear and energy exponents are not
interchangeable.

## 3. Proof and derivation

Write (h=gu, k=gv), where (g=(h,k)) and ((u,v)=1).  Complete
multiplicativity of (chi _4), including its zero on even integers, gives

\[
 \chi _4(g)\chi _4(u)=\chi _4(h).
 \tag{114.A16}
\]

The map ((h,k)\leftrightarrow(g,u,v)) is a bijection.  Summing the exact
smooth gcd telescope before taking a modulus gives

\[
 \sum_\sigma\psi_\sigma(g)=\eta(g/G_0).
\]

Substitution into the accepted identity
(Z_B=2iT_B^{\rm low}) proves (114.A1)--(114.A2).  This is not a
shellwise triangle inequality.  It is also not character erasure: the
(1/4)-packet minus the (3/4)-packet was recombined coefficientwise into
(2i\chi _4(g)), and (114.A16) leaves (chi _4(h)) in the physical
coefficient.  Squaring only after this recombination proves (114.A12).

For (114.A3) and (114.A13), group the finite sum by the full product
(n=hk).  In primitive coordinates this product is (g^2uv); consequently
the zero shift is (g^2uv=g'^2u'v'), not (uv=u'v').  Since
(n\asymp LK\asymp L^2), there are (O(L^2)) possible (n), and

\[
 |c_B(n)|\ll \tau(n)\ll_\varepsilon X^\varepsilon.
\]

This proves (114.A4).

For the shifted-product corridor, the number of atom pairs with
(|h'k'-hk|\le Q) is at most

\[
 \sum_{n\asymp L^2}\tau(n)
 \sum_{|r|\le Q}\tau(n+r)
 \ll_\varepsilon L^2(Q+1)X^\varepsilon.
 \tag{114.A17}
\]

The support restrictions can only reduce this number.  Multiplying by the
uniform coefficient bound proves the first half of (114.A6).  Notice that
(114.A17) is an estimate on one branch of the exact energy; it does not
take absolute values inside (c_B(n)) in order to redefine the original
target.

For the determinant corridor, first fix (\rho\ne0) and a base point
((h,k)), and put (d=(h,k)).  The equation

\[
 hk'-h'k=\rho
 \tag{114.A18}
\]

has no solution unless (d\mid\rho).  If one solution exists, all of them
are

\[
 (h',k')=(h'_0,k'_0)+t(h/d,k/d),\qquad t\in\mathbb Z.
 \tag{114.A19}
\]

Because both points lie in fixed-comparability boxes, (114.A19) has
(O(d)) admissible values of (t).  There are
(O(LK/d^2)) base points of gcd (d).  Hence, for fixed nonzero (\rho),

\[
 \#\{h,k,h',k':hk'-h'k=\rho\}
 \ll LK\sum_{d\mid\rho}\frac1d
 \ll_\varepsilon L^2X^\varepsilon.
 \tag{114.A20}
\]

When (\rho=0), summing (LK/d) over (d\ll L) gives
(O(L^2\log(2L))).  Summing (114.A20) over the (O(Q+1)) integral values
of (\rho) proves the second half of (114.A6).  The actual low-gcd cutoff
(d\ll\sqrt L) only makes this estimate smaller.

The primitive-coordinate formula (114.A7) follows immediately from
((h,k)=g(u,v)) and ((h',k')=g'(u',v')).  Since the primitive vectors are
positive, (\rho=0) forces ((u,v)=(u',v')).  Therefore the exact
rational-ray contribution is

\[
 E_{\rho=0}=
 \sum_{\substack{(u,v)=1}}
 \left|\chi _4(u)\sum_g
 \eta(g/G_0)\chi _4(g)A_B(gu,gv)
 e(Rg\sqrt{uv})\right|^2,
 \tag{114.A21}
\]

and the preceding count proves
(E_{\rho=0}\ll L^2\log(2L)).  Thus the exact ray slice keeps both gcd
lifts and the character; no (uv-u'v') replacement has been made.

To prove (114.A14), set (x=p/h), (y=q/k).  Then

\[
 P^2-Q_*=\frac14(x-y)^2,
 \qquad x-y=-\frac{\rho}{hk}.
\]

Rationalizing
(sqrt{Q_*}-P=-(P^2-Q_*)/(P+\sqrt{Q_*})) yields (114.A14).
The positivity of (h',k') gives (P\ge\sqrt{Q_*}>0), and fixed
comparability gives the asserted uniform denominator bounds.  At the
critical relation (R\asymp L^3), the magnitude of the scaled transverse
remainder is (\asymp\rho^2).  This is a real-variable magnitude, not a
lower bound on distance modulo one.

It remains to prove the double-invariant chart.  Direct expansion gives

\[
 \delta+\rho=(h+h')(k'-k)=q(h+h'),
 \qquad
 \delta-\rho=(k+k')(h'-h)=p(k+k'),
\]

which is (114.A8).  Put (A=h+h'\asymp L) and (B=k+k'\asymp L).
If (p q\ne0), then for fixed ((\delta,\rho))

\[
 A\mid \delta+\rho,\quad q=\frac{\delta+\rho}{A},
 \qquad
 B\mid \delta-\rho,\quad p=\frac{\delta-\rho}{B},
 \tag{114.A22}
\]

and

\[
 h=\frac{A-p}{2},\quad h'=\frac{A+p}{2},\qquad
 k=\frac{B-q}{2},\quad k'=\frac{B+q}{2}.
 \tag{114.A23}
\]

After the parity, positivity, and literal support tests, (114.A22)--
(114.A23) give at most

\[
 \tau(|\delta+\rho|)\tau(|\delta-\rho|)
 \ll_\varepsilon X^\varepsilon
 \tag{114.A24}
\]

representations.  If (p=0), there are only (O(LK^2)=O(L^3)) atom
pairs; if (q=0), there are (O(KL^2)=O(L^3)).  Equations (114.A6),
(114.A24), and these axial counts prove the target-safe assertion
(114.A15).

There are (O(L^2)) possible values of each of (delta) and (\rho).
Consequently the finite-divisor chart alone still has absolute capacity
(L^4X^\varepsilon).  It saves multiplicity but not the factor (L)
needed for the energy target.

This failure is structural for coefficient-blind claims.  On any fixed
balanced rectangle containing (N\asymp L^2) atoms, bounded real signs
(\epsilon_{h,k}\in\{-1,1\}) can be chosen so that

\[
 \left|\sum_{h,k}\epsilon_{h,k}e(R\sqrt{hk})\right|\gg N.
 \tag{114.A25}
\]

Indeed, average over a direction (phi) the quantity
(sum|\operatorname{Re}(e^{-i\phi}e(R\sqrt{hk}))|); its average is
((2/\pi)N).  For a maximizing (phi), choose each sign to make that
real part nonnegative.  The total energy is then \(\gg L^4\), while the
union (114.A15) contributes (O(L^3X^\varepsilon)) absolutely.  Hence the
complementary broad energy is \(\gg L^4\).  If one insists on displaying a
(chi _4(h)) factor, absorb it into the adversarial real amplitude on odd
(h).  This array is deliberately nonsmooth and phase-adapted, so it
refutes only coefficient-uniform reasoning, not the actual Round-113
symbol.

Finally, the two row Grams are merely stronger sufficient statements.  If
(b(h,k)=\eta((h,k)/G_0)A_B(h,k)), then

\[
 |T_B|^2\ll L\sum_{h\asymp L}
 \left|\sum_{k\asymp K}b(h,k)e(R\sqrt{hk})\right|^2,
 \tag{114.A26}
\]

where (chi _4(h)) has disappeared outside the row modulus, while

\[
 |T_B|^2\ll K\sum_{k\asymp K}
 \left|\sum_{h\asymp L}\chi _4(h)b(h,k)e(R\sqrt{hk})\right|^2
 \tag{114.A27}
\]

retains it.  At (K\asymp L), a bound (O(L^2X^\varepsilon)) for either
displayed Gram is sufficient for the (L^3) energy target, but neither is
equivalent to it.  Row-wise phase-adapted signs make either arbitrary-
coefficient Gram of order (L^3), so its desired (L^2) bound also needs
actual-symbol input.

## 4. First doubtful or unproved step

The first unproved analytic step is the following literal broad estimate:

\[
 \sum_{\substack{h,k,h',k'\ \text{in the one block}\\
 |h'k'-hk|>L,\ |hk'-h'k|>L\\
 h'\ne h,\ k'\ne k}}
 a_B^{<}(h,k)\overline{a_B^{<}(h',k')}
 e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right)
 \ll_\varepsilon L^3X^\varepsilon.
 \tag{114.A28}
\]

The rank-one identity (114.A14) and finite-divisor chart
(114.A22)--(114.A24) do not prove (114.A28).  At (R\asymp L^3), large
(|\rho|) makes the real tangent remainder large, but gives no uniform
distance from an integer and no sign-preserving large-sieve inequality.
The phase denominator also depends on all four atom variables.  The
adversary (114.A25) proves that one cannot repair this by a theorem for
arbitrary bounded coefficients.

Thus a continuation would need a new inequality exploiting the literal
real smooth Vaaler/slanted amplitude together with (chi _4(h)), or a
proved inverse theorem showing that failure of (114.A28) forces an actual-
symbol structure that can be separately bounded.  No such inequality or
inverse theorem is proved here.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_packet_to_physical_sum_identity` | **Pass.** Equations (114.A1), (114.A2), and (114.A16) derive the physical sum coefficientwise. |
| `gcd_lift_and_full_product_retention` | **Pass.** The product is (g^2uv), and the determinant is (gg'(uv'-u'v)); neither lift is dropped. |
| `quarter_shift_and_character_placement` | **Pass.** The two packets are recombined before squaring, leaving (2i\chi _4(g)) and then (chi _4(h)). The character is not deleted from the direct energy. |
| `linear_vs_energy_capacity` | **Pass.** The linear target is (L^{3/2}), the energy target is (L^3), each (Q=L) corridor is target-safe, and the broad absolute capacity is (L^4). |
| `mean_square_orientation_and_cauchy_cost` | **Pass with restriction.** Equations (114.A26)--(114.A27) display the factor (L\asymp K); only the (k)-outer orientation keeps (chi _4(h)) inside. Both Grams are stronger sufficient norms. |
| `equal_full_product_diagonal` | **Pass.** It is (hk=h'k'), bounded by (114.A4), and is not replaced by primitive-product equality. |
| `shifted_product_connector` | **Pass.** Equation (114.A13) is exact; (114.A17) makes the absolute corridor (|\delta|\le L) target-safe. |
| `ray_defect_connector_and_rank_one_identity` | **Pass.** Equations (114.A7), (114.A14), and (114.A21) give the literal connector, exact tangent remainder, and rational-ray Gram. |
| `narrow_broad_threshold_interface` | **Pass for the split; broad estimate open.** The general narrow cost is (L^2(Q+1)); (Q=L) exactly meets the (L^3) budget. For (Q=L^{1-\kappa}) it is (L^{3-\kappa}), but the enlarged broad survivor is not bounded. |
| `actual_symbol_vs_adversarial_coefficients` | **Pass.** Narrow estimates are coefficient-robust. Equation (114.A25) refutes a coefficient-robust broad or Gram theorem but does not refute the actual symbol. |
| `no_shellwise_l1_or_cross_block_cancellation` | **Pass.** The smooth gcd telescope is collapsed exactly inside one fixed physical block before the modulus. No distinct (D,L) block is used. |
| `square_near_square_high_gcd_owner_scope` | **Pass.** The connector concerns the full smooth low-gcd packet. High gcd remains excluded by its owner; square and near-square terms remain explicit target-safe corrections and are not inserted as nonsmooth masks. |
| `critical_j1_and_exact_square_j2_boundary` | **Pass.** Capacity is stated at (j=1, L\asymp R^{1/3}), uniformly for fixed (K/L); (j=2) is mentioned only at its exact-square (K/L=16) boundary. |
| `involution_barrier_and_downstream_scope` | **Pass.** The corridor counts are genuine inequalities, but they leave (114.A28). No balanced parent, M9-M2, M9, endpoint theorem, or exponent is claimed. |

No numerical experiment or external theorem was used.  All estimates are
elementary divisor and lattice-line counts.

## 6. Dependencies and exact artifacts used

The report used only the assigned selected context:

- `protocol.md`;
- `state/proof_obligations.yml` at the Round-114 starting graph, in
  particular `M9-M2-smooth-balanced-quarter-packet-estimate`,
  `M9-M2-balanced-smooth-literal-atom-dictionary`,
  `M9-M2-dual-square-root-spacing-mean-square`,
  `M9-M2-smooth-small-gcd-quarter-packet`,
  `M9-M2-smooth-dual-three-quarter-equivalence`,
  `M9-M2-character-factor`, and
  `M9-M2-dyadic-weight-nondegeneracy`;
- `state/active_campaign.yml`;
- `strategy/conductor_0821_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/candidates/conductor_literal_energy_fork.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/reports/balanced_packet_actual_symbol_formalization.md`.

The exact product corridor and the double-invariant divisor chart are
additional derivations in this report.  No sibling Round-114 report,
unassigned historical artifact, web source, or computation was used.

## 7. Recommended state effect

- **Promote after the independent and hostile seams pass** a narrow
  reduction node containing (114.A1)--(114.A8), the full-product diagonal
  bound (114.A4), the two general corridor bounds (114.A6), the ray Gram
  (114.A21), and the target-safe decomposition (114.A15).  These are exact
  connector/counting facts, not the balanced estimate.
- **Retain open** `M9-M2-smooth-balanced-quarter-packet-estimate`.  Its
  smallest surviving analytic child is the literal broad sum (114.A28),
  which needs a factor (L) of cancellation over coefficient-blind
  capacity.
- **Revise** `M9-M2-dual-square-root-spacing-mean-square`: restrict any
  implication to the literal balanced block after the exact Cauchy
  orientation and owner audit; remove the current direct implication to
  all of `M9-M2`.  Keep the mean square proposed, because neither
  orientation is proved and both are stronger than the scalar target.
- **Reject as mechanism claims** any replacement of the full-product shift
  by (uv-u'v'), any ray defect that omits the factor (gg'), and any
  coefficient-uniform broad/Gram estimate based only on (114.A14) or
  divisor multiplicity.  The real phase-adapted adversary (114.A25) is the
  control.
- **No change** to the hard-top, unbalanced, M9-M1, endpoint-uniformity,
  M9-M2, M9, conditional bridge, or Gauss-circle target nodes.  No global
  exponent changes.
