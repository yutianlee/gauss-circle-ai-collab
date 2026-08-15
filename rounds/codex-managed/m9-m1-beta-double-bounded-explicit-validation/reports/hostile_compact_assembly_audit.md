# Round 43 hostile compact-assembly audit

Task: `hostile_compact_assembly_audit`  
Role: hostile seam reviewer  
Allocation: 100% analytical/algebraic; no numerics and no web sources

## 1. Result

The displayed **abstract finite-family estimate is true**, after making the
inherited condition (a\geq0) explicit and differentiating the permitted
logarithmic connector weights.  In particular, for the family actually
displayed in the Round-43 packet,

\[
 \sup_{1\leq x\leq N_X}
 \bigl(|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\bigr)
 \ll \log ^C(2X).
 \tag{43H.1}
\]

The signed Plemelj constant and sign are correct, the central cutoff has no
moving (x)-boundary, the block (H_j=1) is harmless, radial integration by
parts has full endpoint coefficients, and the external (X^{1/4}) factor is
restored once.

The **actual one-count mapping does not pass** in the frozen formulation.
The first literal obstruction is already present in the smooth spatial
profiles.  The actual Round-42 candidate has the regular top profile

\[
 \mathscr W_{0,r}=\widehat W_{+,r}
 \quad (j=0)
\]

and the interior profile

\[
 \mathscr W_{j,r}=\widehat W(a+i\,\cdot)
 \quad (j\geq1).
\]

In contrast, every smooth type in the Round-43 packet has one fixed
(W_\tau) and is inserted for **every** (j).  The packet supplies an
indicator (\mathbf1_{j=0}) for the singular top but no corresponding
selector for the smooth regular top or the interior family; moreover its
(M_\tau) is declared independent of (j) apart from logarithmic
monomials.  Hence the displayed family either repeats the top remainder on
all interior scales, repeats the interior profile at (j=0), or omits one
of them.  No cited accepted identity equates these two profiles.

This is an exact-identity obstruction, not an exponent obstruction.  Its
worst absolute capacity under the displayed seminorms is only
(O(\log^{C+1}(2X))) before radial integration, because it creates at most
one (O(\log^C(2X))) smooth term on each of (O(\log X)) active scales.
Thus the proposed mechanism remains target-capable, but the present packet
does not certify the actual compact remainder and cannot support graph
promotion as written.

## 2. Exact statement and hypotheses

The abstract lemma proved here is the following.  Assume

\[
 b=\frac1{\log(2X)},\qquad a\geq0,\qquad
 a+b<\frac12,\qquad \frac a2+b<\frac14,
\]

and put

\[
 r=\frac54-\frac{a+b}{2},\qquad
 p=\frac54+\frac{a+b}{2}.
\]

Assume that (\mathfrak T) has (O(1)) elements; every multiplier is
compactly supported in ((L,\beta)), has the stated value and
(L)-derivative bounds, and depends on (x,j,h,q) only through a fixed
degree polynomial/monomial in the displayed logarithms.  Interpret this
last hypothesis literally, so that

\[
 |M_\tau|+|x\partial_xM_\tau|
 \ll \log^{C_\tau}(2Xhq).
 \tag{43H.2}
\]

Assume the height-profile norms and fixed Schwartz seminorms in the packet.
Then the functional defined by the displayed (\mathsf P_\tau),
(\mathsf S_\tau), and (\mathcal A_{\rm db}) obeys (43H.1).

The condition (a\geq0) is essential to the scale proof.  If “accepted
contour” is not understood to include it, the two inequalities printed in
the packet alone allow (a<0), and the last active scale has

\[
 \left(\frac{D_J}{2\sqrt X}\right)^a
 \asymp X^{-a/4},
\]

which is a genuine power loss.  Thus (a\geq0) must appear in any promoted
statement.

The separate routing assertion would require an explicit identity between
the actual endpoint-free compact operator and this finite family, including
the coefficient and orientation of every type and a selector for its
allowed (j)-range.  Those data are not hypotheses of the abstract lemma
and are not supplied by the packet.

## 3. Proof or derivation

First check the hard-top constant.  With

\[
 y=L-\nu,\qquad D=A+\frac{i}{2}y,
\]

and (\Re A<0), direct integration gives

\[
 \operatorname {PV}\!\int_{\mathbb R}
 \frac{dy}{y(A+iy/2)}=\frac{i\pi}{A}.
 \tag{43H.3}
\]

Indeed the (A^{-1}\operatorname {PV}(1/y)) part vanishes and
(\int_{\mathbb R}(A+iy/2)^{-1}dy=-2\pi).  Therefore the constant part of
the PV term contributes another (gp(L)/(2A)), which adds to the delta
term (gp(L)/(2A)).  The packet's full diagonal (gp(L)/A), the minus
(i/(2\pi)) off-diagonal coefficient, and all residual ((2\pi)^{-2})
measures are correct.

On the compact ((L,\beta))-support,

\[
 |A|\asymp1,\qquad |D|\asymp1+|\nu|.
 \tag{43H.4}
\]

For (|L-\nu|\leq1), the mean-value theorem gives

\[
 |p(\nu)-p(L)|\leq |L-\nu|\,\|p'\|_\infty.
\]

For (|L-\nu|>1), (43H.4), the cubic tail, and the (L^1) profile bound
control the two numerator terms separately.  Hence

\[
 \int_{\mathbb R}
 \frac{|p(\nu)-p(L)|}{|L-\nu|\,|D|}\,d\nu
 \ll \log^C(2X).
 \tag{43H.5}
\]

The exact phase derivative is slightly more general than the one printed
in the Round-42 candidate.  If (E) denotes the two displayed phases in
(g), then

\[
 x\partial_x\{M_\tau E p(\nu)\}
 =E\left\{x\partial_xM_\tau-i\eta M_\tau\right\}p(\nu),
 \qquad
 \eta=\frac{L+\nu}{2}+\beta.
 \tag{43H.6}
\]

Thus (x\partial_x(gp)=-i\eta gp) is exact only when the allowed
logarithmic multiplier has no (\log x) factor.  This does not cost an
exponent: (43H.2) controls the additional term.  In the divided
difference, the phase part is

\[
 \eta p(\nu)-\alpha p(L),\qquad \alpha=L+\beta.
\]

It vanishes at (\nu=L), is (O(|L-\nu|\log^C X)) locally, and satisfies

\[
 \int_{\mathbb R}
 \frac{|\eta p(\nu)-\alpha p(L)|}
 {|L-\nu|\,|D|}\,d\nu
 \ll \log^C(2X)
 \tag{43H.7}
\]

globally by the first height moment.  Equations (43H.2), (43H.5), and
(43H.7) prove the value and one-(x)-derivative bound for every singular
type.

For a smooth type, (W_\tau) is Schwartz and

\[
 \left|\frac{\eta}{D}\right|\ll1.
\]

Ordinary absolute convolution, (43H.2), and the same height norms therefore
give the identical polylogarithmic value and derivative bound.  The cutoff
(\chi_0(L+\beta)) is fixed in Mellin height coordinates; it has no
(x)-dependent boundary and produces no Leibniz trace.

The coefficient and scale sums are also target-safe.  With
(\delta=r-1>b/2), for each fixed (k),

\[
 \sum_{h\geq1}h^{-r}\log^k(2h)\ll_k\delta^{-k-1}
 \ll\log^{k+1}(2X),
\]

whereas (p\geq5/4) makes the corresponding (q)-sum uniformly bounded.
For active (j), including the last block (H_j=1),

\[
 \left(\frac{D_j}{2\sqrt X}\right)^a\leq1,
 \qquad
 (H_j+1)^b\leq(2X^{1/4})^b\ll1,
\]

and there are (O(\log X)) scales.  Summing the (O(1)) abstract types
proves (43H.1).

Finally,

\[
 d\,e(\sqrt{Xx})=\pi i\sqrt X\,x^{-1/2}
 e(\sqrt{Xx})\,dx.
\]

Integration by parts therefore cancels the internal (\sqrt X), creates
full upper-minus-lower endpoint coefficients, and is bounded by (43H.1).
No new half-star occurs.  Restoring
(-4X^{1/4}\Re(e(1/8)\,\cdot)/\pi) once gives the claimed target capacity
for any actual operator that has first been identified with the abstract
family.

## 4. First doubtful or unproved step

The first unproved step is not analytic; it is the equality between the
actual routed operator and the packet's (\mathfrak T)-sum.  The smooth
(j)-selector mismatch described in Section 1 is a literal defect in that
equality.  It can be repaired by replacing (W_\tau) with
(W_{\tau,j}), or by supplying fixed selectors

\[
 \varepsilon_\tau(j)\in
 \{\mathbf1_{j=0},\mathbf1_{j\geq1},1\}
\]

and including them explicitly in the amplitude.

Even after that repair, (\mathfrak T) is not enumerated.  Round 34 gives
a sixteen-stratum finite transfer, Round 36 removes the physical boundary
module only after aggregate three-mask recombination, and Round 38 still
tracks artificial, axial, collision, and corner shares in the
endpoint-free limiting vector.  Round 41 places these modules outside its
large-
\(|\alpha|\) product cells, but that scoped assertion does not supply the
compact-cell term list.  The Round-43 packet merely asserts that every such
module has been routed and that internal alpha-cutoff derivatives cancel;
it gives no coefficient table from which those assertions, connector signs,
or one-count exclusions can be checked.

The sharp consequence is an identity gap of polylogarithmic capacity, not
a demonstrated power loss.  A missing or duplicated fixed smooth type is
(O(\log^C X)) per scale and hence (O(\log^{C+1}X)) in aggregate.  That is
small enough to be estimable once displayed, but it is not zero and cannot
be silently absorbed into an “exact” one-count formula.

## 5. Required control test and outcome

1. **Signed-top constant and PV sign:** pass.  Equation (43H.3) produces
   the full (gp(L)/A) diagonal with the packet's sign.
2. **Full (x)-derivative:** pass for the bound, correction required for
   the identity.  The extra (x\partial_xM_\tau) term in (43H.6) is
   polylogarithmic but cannot be omitted when a connector weight contains
   (\log x).
3. **Central cutoff motion:** pass.  (\chi_0(L+\beta)) is (x)-fixed;
   no moving-boundary trace occurs.
4. **Absolute (h,q) and active (j) ledger:** pass provided (a\geq0)
   is explicit.  The (H_j=1) endpoint block is included and costs no
   power.
5. **Uniform finite family:** not validated.  Uniform cardinality is an
   assumption, not an enumerated consequence of the routed operator.
6. **Profile/connector one-count mapping:** fail as written.  The smooth
   top/interior (j)-selectors are absent, and no connector coefficient
   table exists.
7. **Artificial, axial, collision, corner, and module exclusion:** not
   testable from the packet.  The cited syntheses establish the aggregate
   ownership architecture, not the missing compact term-by-term equality.
8. **Local masked radial endpoints:** pass conditionally.  Once the actual
   amplitude obeys (43H.1), its two radial traces are bounded directly and
   are not identified with the unmasked endpoint module.
9. **Radial and external normalization:** pass.  The internal (\sqrt X)
   is removed by one radial integration by parts and the external
   (X^{1/4}) multiplier occurs once.

## 6. Dependencies and exact artifacts used

This audit used only the following mathematical artifacts:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-beta-double-bounded-explicit-validation/explicit_amplitude_packet.md`;
5. `rounds/codex-managed/m9-m1-beta-mask-endpoint-axial-compatibility/synthesis.md`;
6. `rounds/codex-managed/m9-m1-beta-complete-axial-connector-ledger/synthesis.md`;
7. `rounds/codex-managed/m9-m1-beta-physical-module-transfer/synthesis.md`;
8. `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/synthesis.md`;
9. `rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/synthesis.md`;
10. `rounds/codex-managed/m9-m1-beta-double-bounded-cell/synthesis.md`;
11. `rounds/codex-managed/m9-m1-beta-double-bounded-cell/reports/double_bounded_radial_attack.md`;
12. `proofs/kernels/m9_m1_beta_double_bounded_cell_candidate.md`;
13. the assigned Round-43 task brief.

No other Round-43 report, numerical experiment, or external source was
used.

## 7. Recommended state effect

**Retain and revise; do not promote the actual double-bounded-cell
obligation from this packet.**  The conductor may retain the abstract
finite-family estimate (43H.1) as a proved conditional lemma, since all of
its analytic, scale, endpoint, and normalization seams pass after the
(x\partial_xM_\tau) correction.

Before promoting the actual cell, revise the frozen amplitude to:

1. state (a\geq0) explicitly;
2. include (x\partial_xM_\tau) in the multiplier seminorm;
3. add exact (j=0) and (j\geq1) selectors, with the actual regular-top
   and interior profiles;
4. enumerate every surviving terminal/connector type with its coefficient,
   orientation, mask derivative, and allowed (j)-range; and
5. give a term-by-term exclusion table for endpoint, side, arithmetic,
   artificial-pole, axial, connector-axis, collision, and corner modules.

The obstruction is reparable and has only polylogarithmic capacity, so it
does not falsify the compact-cell strategy.  It does falsify the claim that
the currently displayed schematic family is already the exact actual
one-count assembly.
