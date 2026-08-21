# Blind unbalanced divisor rederivation

## 1. Result

**Result: coefficient-preserving no-go, with an exact smaller survivor.**  The
product regrouping and its positive energy estimate are exact, and a separated
Mellin mode has Dirichlet series

\[
L(s-it_1,\chi _4)\zeta(s-it_2).
\]

They do not by themselves prove
\(\mathcal T_{L,K}\ll (LK)^{3/4}X^\varepsilon\) on any new residual
corridor.  The modewise functional-equation capacity calculation has dual
conductor \(F^2=XM\), dual centre \(m\asymp X\), resonant width

\[
\Delta={X\over F}={D\over L},
\]

and resonant transform size \(M^{3/4}X^{-1/4}\) per dual integer.  Even if one
grants a uniform literal-symbol transform theorem and uses the divisor bound
optimally on each term, absolute summation therefore gives only

\[
\mathcal T_{L,K}
 \ll_\varepsilon
 M^{3/4}X^{-1/4}\Delta X^\varepsilon
 =M^{3/4}X^{\delta-\ell-1/4+\varepsilon}.
\]

In the active triangle, \(\ell\leq\delta-1/4\), so the excess exponent
\(\mu:=\delta-\ell-1/4\) is nonnegative.  Equality occurs only on the
already-owned terminal line \(\ell=\delta-1/4\); it is strictly positive in
the interior.  Thus the straightforward functional equation has no strict
new residual subrange.

The weakest non-circular signed condition produced by one exact van der
Corput differencing step is an upper bound for one **real, aggregated,
oscillatory truncated \(\chi _4\)-divisor correlation**; no absolute value is
required on the individual shifts.  This condition is stated precisely in
Section 2 and proved sufficient in Section 3.  It retains every literal symbol
decoration.  Proving it, or equivalently finding a saving of
\(X^\mu=\Delta/X^{1/4}\) in the dual resonant packet, is the first genuine
signed task left by the regrouping.  No such estimate is proved here.

## 2. Exact statement and hypotheses

Let \(X\geq2\),

\[
D=X^\delta,\qquad L=X^\ell,\qquad
K={XL\over D^2},\qquad M=LK,\qquad F=\sqrt{XM}={XL\over D},
\]

with

\[
{1\over4}\leq\delta\leq{1\over2},\qquad
0\leq\ell\leq\delta-{1\over4},\qquad K/L>16.
\]

The coefficient \(a=a_{L,K}\) is the literal smooth slanted M2 symbol from
the statement-only packet.  It may be complex.  On each member of its fixed
finite subdivision, assume its support lies in
\(h\asymp L, k\asymp K\), its absolute value is bounded, and its normalized
derivatives have the asserted bounds.  No separability, reality, or symmetry
is assumed.  Define

\[
A(n)=\sum_{\substack{hk=n\\h\asymp L,\ k\asymp K}}
       \chi _4(h)a(h,k),
\qquad
\mathcal T=\sum_n A(n)e(\sqrt{Xn}).
\]

Then the following assertions are unconditional consequences of these
hypotheses.

1. The equality above is the exact regrouping of the original double sum, and

   \[
   \sum_n|A(n)|^2\ll_\varepsilon MX^\varepsilon.
   \]

2. For a pure separated mode, in \(\Re s>1\),

   \[
   b_{t_1,t_2}(n):=\sum_{hk=n}\chi _4(h)h^{it_1}k^{it_2},
   \qquad
   \sum_{n\geq1}{b_{t_1,t_2}(n)\over n^s}
   =L(s-it_1,\chi _4)\zeta(s-it_2).
   \]

   Double Mellin inversion represents the Dirichlet series of the actual
   truncated coefficient as a rapidly convergent integral of these products;
   it does not replace \(A(n)\) by the complete coefficient \(r_2(n)/4\).

3. Let the support of \(A\) be placed in one integer interval of length
   \(N\ll M\), extending \(A\) by zero.  For an integer
   \(1\leq Q\leq N\), put

   \[
   C(q):=\sum_n A(n+q)\overline{A(n)}
   e\!\left(\sqrt X\bigl(\sqrt{n+q}-\sqrt n\bigr)\right)
   \quad(1\leq q<Q).
   \]

   Choose any \(Q\) with \(Q\asymp M^{1/2}\) (rounding to an integer).  The
   signed inequality

   \[
   \boxed{
   \Re\sum_{q=1}^{Q-1}\left(1-{q\over Q}\right)C(q)
       \ll_\varepsilon MX^\varepsilon }
   \tag{SC}
   \]

   is sufficient for
   \(\mathcal T\ll_\varepsilon M^{3/4}X^\varepsilon\).  More generally, for
   \(M^{1/2}\ll Q\ll M\), the sufficient right side is
   \(QM^{1/2}X^\varepsilon\).  Only an upper bound on the displayed real
   aggregate is needed; bounds for \(|C(q)|\), for every individual shift, or
   for an unsigned four-variable count are strictly stronger than (SC).

The exact expansion of the survivor is

\[
\begin{aligned}
C(q)=
\sum_{\substack{h_1k_1-h_2k_2=q\\
                  h_i\asymp L,\ k_i\asymp K}}
 &\chi _4(h_1)\overline{\chi _4(h_2)}
 a(h_1,k_1)\overline{a(h_2,k_2)}\\
 &\times e\!\left(\sqrt X
    (\sqrt{h_1k_1}-\sqrt{h_2k_2})\right).
\end{aligned}
\tag{TC}
\]

Thus (SC) is a signed, actual-symbol, truncated divisor correlation, with the
exact-product case \(q=0\) kept outside it as the energy term.

The functional-equation bound in Section 1 is a **conditional capacity
statement**: it assumes a uniform modewise transform formula for every
literal cell whose resonant kernel is negligible away from an interval of
length \(O(\Delta X^\varepsilon)\) about \(m\asymp X\), and is
\(O(M^{3/4}X^{-1/4}X^\varepsilon)\) there.  That actual-symbol transform
lemma is not proved in this report.

## 3. Proof or derivation

### Exact regrouping and positive energy

The original sum is finite.  Mapping a pair \((h,k)\) to its exact product
\(n=hk\), with no rounding or replacement of the support, gives

\[
\sum_{h,k}\chi _4(h)a(h,k)e(\sqrt{Xhk})
=\sum_n\left(\sum_{hk=n}\chi _4(h)a(h,k)\right)e(\sqrt{Xn}).
\]

This proves the regrouping, including all lift multiplicities.  If
\(d_{L,K}(n)\) denotes the number of supported factorizations, Cauchy--Schwarz
inside one exact-product fibre gives

\[
|A(n)|^2
 \leq d_{L,K}(n)
       \sum_{\substack{hk=n\\h\asymp L,\ k\asymp K}}|a(h,k)|^2
 \leq d(n)
       \sum_{\substack{hk=n\\h\asymp L,\ k\asymp K}}|a(h,k)|^2.
\]

Summing and using the divisor bound on \(hk\asymp M\), together with
\(O(LK)=O(M)\) supported pairs, yields

\[
\sum_n|A(n)|^2
 \ll_\varepsilon X^\varepsilon\sum_{h,k}|a(h,k)|^2
 \ll_\varepsilon MX^\varepsilon.
\]

This argument is deliberately weight-aware, but it uses no cancellation from
\(\chi _4\).

### Mellin modes without a false completion

On one smooth cell set

\[
\widehat a(t_1,t_2)
=\int_0^\infty\!\int_0^\infty
 a(Lx,Ky)x^{-it_1}y^{-it_2}{dx\over x}{dy\over y}.
\]

The asserted normalized smoothness gives rapid decay, and Mellin inversion
recovers the cell exactly.  Finite summation over the cells retains the
slanted support, Vaaler taper, quarter shifts, frequency signs, physical
profiles, floors, stars, support crossings, and the assigned transform-error
owner inside \(\widehat a\); none is set equal to one.

For \(\Re s>1\), absolute convergence justifies

\[
\begin{aligned}
\sum_{n\geq1}{b_{t_1,t_2}(n)\over n^s}
&=\sum_{h,k\geq1}{\chi _4(h)h^{it_1}k^{it_2}\over(hk)^s}\\
&=\left(\sum_{h\geq1}{\chi _4(h)\over h^{s-it_1}}\right)
  \left(\sum_{k\geq1}{1\over k^{s-it_2}}\right)\\
&=L(s-it_1,\chi _4)\zeta(s-it_2).
\end{aligned}
\]

Consequently, after inserting the harmless unit-modulus powers of \(L\) and
\(K\) dictated by the chosen Mellin normalization, the actual coefficient
Dirichlet series is a double integral of this product.  This statement is
made first in \(\Re s>1\), where all interchanges are absolute; a compact
product bump equal to one on the actual support can then be Mellin-inverted
before any contour move.  There is no step in this calculation that sums over
all factor fragments with coefficient one.  Hence it supplies no identity
with \(r_2(n)/4\).

### Scale, conductor, and transform capacity

Direct substitution gives

\[
{K\over L}={X\over D^2},\qquad
M={XL^2\over D^2},\qquad
F=\sqrt{XM}={XL\over D},\qquad F^2=XM.
\]

As a check on the original orientation, for fixed \(h\asymp L\),
\(f_h(k)=\sqrt{Xhk}\) has

\[
|f_h''(k)|\asymp \sqrt{XL}\,K^{-3/2}.
\]

The scalar second-derivative estimate, followed by the \(L\) rows, is

\[
\mathcal T\ll_\varepsilon X^\varepsilon
\left(X^{1/4}L^{5/4}K^{1/4}
      +X^{-1/4}L^{3/4}K^{3/4}\right).
\]

Relative to \(M^{3/4}\), its two factors are respectively

\[
X^{1/4}\sqrt{L/K}=DX^{-1/4},
\qquad X^{-1/4}.
\]

Thus the first scalar term loses \(X^{\delta-1/4}\), exactly the physical
height deficit recorded in the packet.

For the product orientation, insert a smooth bump in \(n/M\).  The Mellin
transform of
\(w(n/M)e(\pm\sqrt{Xn})=w(x)e(\pm F\sqrt x)\) is concentrated at Mellin
height \(|\tau|\asymp F\).  The rapidly decreasing symbol Mellin modes have
\(|t_1|+|t_2|\ll X^\varepsilon\) after a power-saving truncation, so the two
degree-one factors have combined conductor

\[
(1+|\tau-t_1|)(1+|\tau-t_2|)\asymp F^2.
\]

A functional equation therefore exchanges the physical length \(M\) with
the dual scale

\[
{F^2\over M}=X.
\]

For a separated mode its dual Dirichlet coefficient is, up to the
unit-modulus normalizations,

\[
b^*_{t_1,t_2}(m)
=\sum_{uv=m}\chi _4(u)u^{-it_1}v^{-it_2};
\]

the signs of the heights reverse under the two functional equations.  A
degree-two oscillatory kernel has branches with phase on the scale
\(\pm2\sqrt{mx}\).  Against the input phase on \(x\asymp M\), a stationary
branch can occur only at \(m\asymp X\).  Changing \(m\) by \(r\) changes the
phase over the physical interval by order
\(r\sqrt{M/X}=rF/X\).  Hence the resonant width is

\[
|r|\lesssim {X\over F}={D\over L}=:\Delta.
\]

The standard kernel amplitude \((mx)^{-1/4}\), integrated over an interval
of length \(M\), has resonant size

\[
M(MX)^{-1/4}=M^{3/4}X^{-1/4}.
\]

These last kernel assertions are the formal stationary-phase capacity of the
functional equation, not an asserted literal-symbol transform theorem.  If
that theorem is granted, \(|b^*_{t_1,t_2}(m)|\ll_\varepsilon X^\varepsilon\)
and absolute summation over the \(O(\Delta X^\varepsilon)\) resonant integers
give

\[
|\mathcal T|
\ll_\varepsilon M^{3/4}X^{-1/4}\Delta X^\varepsilon
=M^{3/4}X^{\delta-\ell-1/4+\varepsilon}.
\]

The target condition for this route is
\(\Delta\leq X^{1/4+\varepsilon}\), or, at the exponent level,
\(\ell\geq\delta-1/4\).  The active triangle imposes the reverse inequality.
Thus only equality, the prior terminal line, is reached.  In the strict
interior the missing power is

\[
{\Delta\over X^{1/4}}=X^{\delta-\ell-1/4}=X^\mu.
\]

Mellin inversion of all factor fragments could give \(r_2(n)/4\) only if an
additional pointwise partition identity made their literal weights sum to
one for every factor pair.  No such hypothesis is present.  Applying the
functional equations twice reverses the height signs twice and returns the
same coefficient information; without signed cancellation in the resonant
packet, this is a self-return at the capacity just computed.

### Exact derivation of the sufficient signed correlation

Put
\(z_n=A(n)e(\sqrt{Xn})\) and extend it by zero outside an interval of length
\(N\ll M\).  The usual sliding-window Cauchy--Schwarz argument is an exact
identity/inequality:

\[
Q^2\left|\sum_nz_n\right|^2
\leq (N+Q)
\left(Q\sum_n|z_n|^2
+2\sum_{q=1}^{Q-1}(Q-q)\Re\sum_nz_{n+q}\overline{z_n}\right).
\]

Consequently

\[
|\mathcal T|^2
\leq {N+Q\over Q}
\left(
 \sum_n|A(n)|^2
+2\Re\sum_{q=1}^{Q-1}\left(1-{q\over Q}\right)C(q)
\right).
\]

For \(Q\asymp M^{1/2}\), the prefactor is \(O(M^{1/2})\).  The energy bound
and (SC) make the bracket \(O_\varepsilon(MX^\varepsilon)\), proving
\(|\mathcal T|^2\ll_\varepsilon M^{3/2}X^\varepsilon\), and hence the target
after relabelling \(\varepsilon\).  Expanding the two exact divisor fibres
gives (TC), so no coefficient or lift is lost.

For orientation, if
\(g_q(n)=\sqrt X(\sqrt{n+q}-\sqrt n)\), then on \(n\asymp M\),

\[
|g_q'(n)|\asymp {q\sqrt X\over M^{3/2}}={qF\over M^2},
\qquad
M|g_q'(n)|\asymp {qF\over M}={qD\over L}.
\]

Thus even \(q=1\) has substantial phase variation in the active triangle.
This does not permit a scalar first-derivative estimate, because the
amplitude \(A(n+q)\overline{A(n)}\) is an arithmetic correlation rather than
a smooth weight.  Establishing (SC) is precisely the missing signed input,
not a consequence of phase variation alone.

## 4. First doubtful or unproved step

The regrouping, weighted energy estimate, separated-mode Dirichlet series,
scale identities, and the implication (SC) \(\Rightarrow\) target are proved
above from the allowed packet and elementary inequalities.

The first unproved actual-symbol step in the functional-equation route is the
following uniform transform lemma: after double Mellin separation, contour
motion and both functional equations must be justified simultaneously for
every literal smooth cell, all retained height floors, stars, slanted support
entries and exits, both quarter shifts, both frequency signs, and the full
\((t_1,t_2)\)-tails; the resulting pieces must recombine with their original
owners, and the resonant kernel must have the width and amplitude used in the
capacity calculation with power-saving nonresonant and transform errors.
No primary-source theorem with these precise hypotheses was supplied in the
statement-only packet, and no such theorem is proved here.  The capacity
calculation was therefore explicitly conditional at that seam.

Even granting this seam in its strongest routine form does not open a strict
residual corridor: absolute dual summation loses \(X^\mu\).  The next step
would have to prove cancellation by this factor in the actual recombined dual
coefficient, or prove (SC).  Neither follows from positive energy, from the
Euler product, or from phase variation, and it is the first genuinely
unproved signed step.  The report stops there.  In particular, it does not
assert an \(r_2/4\) completion or a literal transform self-identity.

## 5. Required control test and outcome

| Control | Exact input and expected invariant/failure | Observed analytical outcome | Implication |
|---|---|---|---|
| Raw product count versus weighted energy | Expand each exact fibre and retain \(|a(h,k)|\) and its lift multiplicity.  A raw tuple exponent must not be transferred. | Fibrewise Cauchy--Schwarz gives \(\sum|A|^2\ll MX^\varepsilon\) with the actual weights.  It gives only \(|\mathcal T|\ll MX^\varepsilon\) by global Cauchy--Schwarz. | Positive energy is valid but short of the target by \(M^{1/4}\). |
| Signed, unsigned, random, and phase-conjugating shadows | Compare true \(\chi _4\), absolute values, arbitrary random phases, and an adversary that conjugates the oscillatory phase while preserving magnitudes. | The true pure mode has \(L\zeta\); the unsigned mode has \(\zeta\zeta\); random phases generally have no such product; a phase-conjugating adversary can make a positive proportion of the pair terms add with size comparable to their total mass.  Energy and absolute transform capacity do not distinguish these cases. | Any improvement must identify true signed cancellation, such as (SC); a magnitude-only argument cannot prove the fixed-symbol target. |
| Exact versus near resonance | Keep \(q=0\) separate from \(1\leq q<Q\). | The exact-product part is precisely \(\sum|A|^2\).  The near-product bands are precisely (TC) and are not controlled by that energy. | Exact Fejer/product energy cannot be promoted to a near-collision estimate. |
| Products, squares, fourth powers, primes, and one-divisor rows | Inspect factor fibres rather than assuming a typical divisor count. | Every case is retained exactly.  Squares and fourth powers merely have more supported lifts, covered by \(d(n)\); a prime contributes only when one of its two factorisations enters the dyadic cone; a one-divisor row contributes one literal term. | No exceptional fibre creates a completion or signed saving; no fibre is silently discarded. |
| Unbalanced endpoints | Evaluate \(\Delta\) and \(\mu\) at \(D=X^{1/4}\) and as \(D\uparrow X^{1/2}\). | At \((\delta,\ell)=(1/4,0)\), \(M=X^{1/2}\), \(F=X^{3/4}\), \(\Delta=X^{1/4}\), and \(\mu=0\).  As \(\delta\uparrow1/2\), \(\mu=1/4-\ell+o(1)\), vanishing only on the terminal line; \(K/L=X^{1-2\delta}>16\) must still be imposed, so \(\delta=1/2\) itself is not an unbalanced block. | The capacity conclusion does not cross the endpoint and gives no strict interior gain. |
| Prior owners | Exclude the terminal line, the isolated full second-derivative point, and \(178\ell+1638\delta\leq463\). | The only target-capable functional-equation capacity line is \(\ell=\delta-1/4\), already listed as terminal.  No conclusion is drawn on any prior-owned cell. | There is no new ownership claim. |
| Both quarter shifts and frequency signs | Keep them inside the literal symbol and track both functional-equation kernel branches. | Regrouping, energy, and (SC) are independent of dropping neither.  For either frequency sign only the oppositely oscillating kernel branch can be stationary; quarter shifts alter gamma phases and constants, not the scale ledger.  Their exact uniform transform remains part of the unproved seam. | No branch or shift can be discarded to manufacture a gain. |
| Smooth slanted support and profile/floor/star crossings | Use the stated fixed finite subdivision and never replace the symbol by a rectangle or by one. | Exact regrouping survives every crossing.  Cellwise Mellin inversion is algebraically available.  Uniform transformed errors at all crossings were not proved. | The exact algebra is retained; the functional-equation estimate is not promoted. |
| Double Mellin tails and conductors | Compare symbol heights \(t_1,t_2\) with oscillatory Mellin height \(\tau\asymp F\). | Rapid decay formally restricts \(|t_1|+|t_2|\ll X^\varepsilon\) after choosing a power-saving tail; the central conductor is \(F^2\).  Uniformity when moving contours and summing every tail is included in the unproved actual-symbol lemma. | The scale \(F^2\) is a capacity ledger, not yet a certified transform theorem. |
| Exact \(r_2/4\) completion versus truncated cone | Require a pointwise compatible partition over all factor fragments. | The identity \(\sum_{h\mid n}\chi _4(h)=r_2(n)/4\) applies to the complete unit-weight divisor sum.  No identity says the literal fragment weights sum to one. | The actual coefficient remains a truncated, decorated divisor cone. |
| Transform inversion and capacity | Apply both scalar functional equations twice and compare resource scales. | Heights reverse and then return; the root conductor is \(F\), the dual centre is \(X\), and absolute resonant capacity loses \(X^\mu\). | A change of variables is a self-return unless the short dual packet has new signed cancellation. |
| Real versus complex pairing | Allow genuinely complex and asymmetric \(a(h,k)\). | The energy and (TC) use exact complex conjugates.  No \(\operatorname{Re}B_h\) or hidden conjugacy shortcut is used. | The sufficient correlation criterion is valid for the literal complex symbol. |
| Coefficient adversary | Replace the fixed coefficient phases by arbitrary phases of the same magnitude. | A phase-conjugating choice defeats the target at mass scale, while leaving the raw support and magnitude data unchanged. | Any theorem uniform over arbitrary phases is false at the desired strength; fixed \(\Phi\) and \(\chi _4\) structure must enter a proof of (SC). |
| Support and degeneracy | Check sharp versus smooth edges, \(uv=0\), repeated products, and lift boundaries. | The dyadic variables are positive, so \(uv=0\) is absent.  Repeated products and lift boundaries are retained by exact fibres.  The report uses smooth cells only and makes no hard-edge transfer. | No degeneracy is hidden in the algebra; hard-cone conclusions are out of scope. |
| Known unsigned lower-bound families | The control file requires UNC, TS, and W-1 parity/support/lower-envelope audits before any unsigned near-collision claim. | Their definitions are not in the permitted statement-only packet.  No unsigned near-collision upper bound is asserted here, so no incompatible claim is promoted; a nonblind audit would still be required before promotion of any such claim. | This control remains intentionally unresolved rather than guessed. |
| Primary-source hypotheses | Any imported functional-equation/Voronoi theorem must be checked against the literal symbol and height ranges. | No external theorem or source was read under blind isolation.  The only source-dependent transform step is marked conditional. | The transform capacity cannot be accepted as an actual-symbol estimate on this report alone. |
| Downstream and exponent scope | Restrict the conclusion to the smooth unbalanced residual packet. | No balanced, hard-cone, M9-M2, M9-M1, M9, endpoint-uniform, or global-exponent conclusion was used or inferred. | The no-go and survivor have strictly local scope. |

No numerical experiment was used.  The controls above are algebraic
falsification and scope checks, not numerical certification.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read and used:

1. `problems/gauss_circle.md` — definition and repository-level scope of the
   Gauss circle problem.
2. `state/control_models.md` — mandatory proof-unit controls and reporting
   requirements.
3. `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/blind_statement.md`
   — all parameters, the literal packet, prior-owner descriptions, and the
   frozen question.
4. `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/briefs/blind_unbalanced_divisor_rederivation.md`
   — isolation, task, and output instructions.

The derivation additionally uses only elementary finite regrouping,
Cauchy--Schwarz, Mellin inversion for a compact smooth function, absolute
factorisation of Dirichlet series in \(\Re s>1\), the elementary divisor
bound, and the sliding-window van der Corput inequality.  The degree-two
functional-equation kernel description is used only as an explicitly
conditional capacity calculation.  No proof graph, strategy file,
derivation packet, candidate, earlier derivation, sibling report, web source,
or computation was consulted.

## 7. Recommended state effect

**Overall recommendation: retain; do not promote a target estimate.**

Promote, after an independent seam check, only the exact local algebraic
claims: the product regrouping, the weighted energy bound, the separated-mode
\(L\zeta\) Dirichlet series, and the implication (SC) \(\Rightarrow\) target.
Retain the functional-equation ledger as a conditional no-go diagnostic:
routine absolute dual summation reaches only the prior terminal line and
misses a strict residual point by \(X^{\delta-\ell-1/4}\).  Reject any
inference that the physical fragments automatically complete to \(r_2/4\),
or that functional-equation inversion alone proves a new corridor.  The next
candidate proof obligation should be the exact aggregate correlation (SC),
or an equivalent actual-symbol saving of \(X^{\delta-\ell-1/4}\) in the dual
resonant packet, with the literal transform seam and primary-source
hypotheses audited first.
