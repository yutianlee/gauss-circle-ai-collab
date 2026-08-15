# Resonance-cell literature and hostile audit

- Campaign: `m9-m1-ordered-denominator-resonance-cells`
- Round: 13
- Task: `resonance_cell_literature_hostile_audit`
- Role: primary-source and hostile reviewer
- Generated: 2026-08-12
- Isolation: no other Round-13 report was read

## 1. Result

### Exact increment and a scoped no-go theorem

Let \(I_D\) be an interval of odd denominators \(d\asymp D\), possibly
cut off at the hard upper endpoint, and let \(w_D\) be a real profile with

\[
 \|w_D\|_\infty+\sum_d|w_D(d+2)-w_D(d)|\ll 1.
\]

For fixed \(h>0\), put

\[
 S_h=\sum_{d\in I_D}\chi_4(d)w_D(d)e(hX/d),
 \qquad Q_h=\frac{hX}{D^2}.
\]

In the active range \(D\leq \sqrt X\), one has \(Q_h\gg1\).  On odd
\(d\),

\[
 \chi_4(d)=-i e(d/4).
\]

Writing \(d=2n+1\) and

\[
 F_h(n)=\frac{hX}{2n+1}+\frac{2n+1}{4},
\]

gives the exact increment

\[
 \boxed{
 F_h(n+1)-F_h(n)
 =\frac12-\frac{2hX}{d(d+2)}.}
 \tag{1.1}
\]

Thus the dangerous cells are exactly those for which

\[
 \frac{2hX}{d(d+2)}
 \quad\hbox{is near}\quad \mathbb Z+\frac12.
 \tag{1.2}
\]

However, applying the Kusmin--Landau lemma cell by cell, with absolute
values between cells and then between frequencies, gives only

\[
 \boxed{
 |S_h|\ll \min\left(D,\sqrt{DQ_h}\right)
 =\min\left(D,\sqrt{\frac{hX}{D}}\right).}
 \tag{1.3}
\]

For the actual dyadic Vaaler coefficient \(u_{L,H}(h)\), whose
\(\ell^1\)-mass on \(h\asymp L\) is \(O(1)\), this yields only

\[
 \boxed{
 |B_{1,L}(D;X)|
 \ll \min\left(D,\sqrt{\frac{LX}{D}}\right).}
 \tag{1.4}
\]

In exponent coordinates \(D=X^\delta,L=X^\ell\), the square-root term
reaches \(X^{1/4}\) only if

\[
 \ell\leq\delta-\frac12,
\]

which inside the active triangle occurs only at
\((\delta,\ell)=(1/2,0)\).  The trivial \(D\) branch reaches the target
only on the already trivial left boundary \(\delta=1/4\).  Hence the
proposed cell decomposition, if it estimates each \(h\) and each cell
separately, closes no point of the residual corridor \(\mathcal U_1\).

Moreover, the cells are the stationary pieces of the ordinary van der
Corput \(B\)-process.  The transformed phase is the same signed
square-root cone already present in the accepted M1 endpoint transform.
Consequently local cell summation does not create a new mechanism.  A
successful continuation must retain cancellation in the dual cell index
and/or jointly in \(h\); that is an estimate for the accepted M1 cone, not
a consequence of counting resonant cells.

This is a scoped no-go.  It does **not** exclude a new two-variable
\((h,m)\) estimate for the actual Vaaler profile.

## 2. Exact statement and proof

### 2.1 Character algebra and the exact odd-lattice phase

For odd \(d\), \(e(d/4)=i\chi_4(d)\), so

\[
 \chi_4(d)e(hX/d)=-i e\!\left(\frac{hX}{d}+\frac d4\right).
\]

Set \(d=2n+1\).  Direct subtraction gives

\[
\begin{aligned}
 F_h(n+1)-F_h(n)
 &=\frac{hX}{d+2}-\frac{hX}{d}+\frac12\\
 &=\frac12-\frac{2hX}{d(d+2)},
\end{aligned}
\]

proving (1.1).  The quantity

\[
 q_h(d)=\frac{2hX}{d(d+2)}
\]

is strictly decreasing, while the increments in (1.1) are strictly
increasing.  Also, uniformly on \(d\asymp D\),

\[
 q_h(d)\asymp Q_h,
 \qquad |q_h'(d)|\asymp \frac{Q_h}{D}.
 \tag{2.1}
\]

The distance of (1.1) from the nearest integer is exactly

\[
 \left\|F_h(n+1)-F_h(n)\right\|
 =\operatorname{dist}\!\left(q_h(d),\mathbb Z+\frac12\right).
 \tag{2.2}
\]

No differential approximation has been used.

### 2.2 Resonant set and nonresonant components

Fix \(0<\eta\leq1/2\).  Call \(d\) resonant if the right side of (2.2)
is \(<\eta\).  The range of \(q_h\) contains \(O(1+Q_h)\)
half-integers.  By (2.1), the inverse image of an interval of length
(2\eta) about one half-integer contains

\[
 O\!\left(1+\frac{\eta D}{Q_h}\right)
\]

odd integers.  Therefore

\[
 R_h(\eta)
 \ll (1+Q_h)\left(1+\frac{\eta D}{Q_h}\right)
 \ll 1+Q_h+\eta D
 \tag{2.3}
\]

when (Q_h\gg1), with the trivial cap (R_h(\eta)\leq D).

Removing these cells leaves \(O(1+Q_h)\) consecutive intervals.  On
each such interval the increments are monotone and, after subtracting
one fixed integer from every increment, lie between \(\eta\) and
\(1-\eta\).  The sharp Landau form of Kusmin--Landau gives

\[
 \left|\sum_{n\in J}e(F_h(n))\right|
 \leq \cot(\pi\eta/2)\ll \eta^{-1}
 \tag{2.4}
\]

for every subinterval \(J\) of a nonresonant component.  Abel summation
transfers (2.4) through \(w_D(2n+1)\).  Summing the local variations and
the \(O(1+Q_h)\) component endpoints gives

\[
 \left|\sum_{\text{nonresonant }d}
 \chi_4(d)w_D(d)e(hX/d)\right|
 \ll \frac{1+Q_h}{\eta}.
 \tag{2.5}
\]

The resonant denominators are bounded trivially using (2.3).  Thus

\[
 |S_h|\ll
 1+Q_h+\eta D+\frac{1+Q_h}{\eta}.
 \tag{2.6}
\]

If (1\ll Q_h\leq D), take
(\eta\asymp\sqrt{Q_h/D}).  Then (Q_h\leq\sqrt{DQ_h}), and
(2.6) gives (S_h\ll\sqrt{DQ_h}).  If (Q_h>D), the trivial bound
(S_h\ll D) is at least as good.  This proves (1.3).  Since

\[
 \sum_{h\asymp L}|u_{L,H}(h)|\ll1
\]

and \(Q_h\asymp LX/D^2\) on a dyadic \(h\)-block, (1.4) follows.

This proof retains the fixed normalized-BV spatial profile and the hard
endpoint.  It loses all phase information between different resonance
cells and between different \(h\)'s; that loss is exactly why it has no
new capacity.

### 2.3 The cells are the \(B\)-process cone

The continuous derivatives of the same odd-lattice phase are

\[
 F_h'(n)=\frac12-\frac{2hX}{d^2},\qquad
 F_h''(n)=\frac{8hX}{d^3},
\]

\[
 F_h^{(3)}(n)=-\frac{48hX}{d^4},\qquad
 F_h^{(4)}(n)=\frac{384hX}{d^5}.
 \tag{2.7}
\]

On an interval of length \(M\asymp D\), put \(T=hX/D\).  Then

\[
 F_h^{(j)}(n)\asymp_j T/M^j\quad (j=2,3,4),
\]

with fixed signs where relevant.  The van der Corput transform therefore
applies.  Its stationary equation (F_h'(n_m)=-m) is

\[
 d_m=2\sqrt{\frac{hX}{2m+1}}.
 \tag{2.8}
\]

At this point,

\[
 F_h(n_m)+m n_m
 =\sqrt{hX(2m+1)}-\frac m2,
 \tag{2.9}
\]

and

\[
 \frac1{\sqrt{F_h''(n_m)}}
 =\frac{(hX)^{1/4}}{(2m+1)^{3/4}}.
 \tag{2.10}
\]

Up to the global factor \(-i\), endpoint conventions, and the sampled
profile, the transformed sum is therefore

\[
 \sum_m
 w_D(d_m)\frac{(hX)^{1/4}}{(2m+1)^{3/4}}
 e\!\left(\sqrt{hX(2m+1)}-\frac m2+\frac18\right).
 \tag{2.11}
\]

This is the odd-lattice parametrization of the accepted signed affine
square-root M1 cone.  The number of \(m\)'s is \(\asymp Q_h\), and one
term has size \(\asymp\sqrt{D/Q_h}\).  Taking absolute values in (2.11)
again gives

\[
 Q_h\sqrt{D/Q_h}=\sqrt{DQ_h}.
\]

The transform error is

\[
 O\!\left(\sqrt{D/Q_h}+\log(Q_h+2)\right),
\]

which is no larger than the same scale for (Q_h\geq1).  Thus the
Kusmin--Landau cells and the (B)-process agree in capacity and in the
identity of the remaining oscillatory object.  Saving beyond (1.3)
requires cancellation in (2.11).

## 3. Primary-source search and hypothesis audit

The search was for a real reciprocal phase, a fixed Dirichlet-character
twist, or a nonlinear first-derivative/\(B\)-process theorem that treats
the present one-variable sum pointwise.  No searched source proves the
residual M1 corridor.

### 3.1 Arias de Reyna: directly applicable Kusmin--Landau input

J. Arias de Reyna,
[*On Kuzmin--Landau Lemma*](https://arxiv.org/abs/2002.05982),
Lemma 2, records Landau's sharp form.  If the increments
(a_{k+1}-a_k) are increasing and lie in
([\theta,1-\theta]), (0<\theta\leq1/2), then

\[
 \left|\sum_k e(a_k)\right|\leq\cot(\pi\theta/2).
\]

Hypothesis audit:

- **phase form:** exact, because (1.1) supplies monotone discrete
  increments; no derivative replacement is needed;
- **coefficients:** the source is unweighted; the project's fixed
  normalized-BV profile transfers by Abel summation, but arbitrary
  bounded coefficients do not;
- **interval:** applied separately on each component on which one
  integer has been subtracted from all increments;
- **absolute values:** the theorem bounds one component.  Summing
  component moduli causes the (Q_h/\eta) loss in (2.5);
- **endpoint:** every subinterval inherits the hypothesis, so moving or
  hard endpoints are harmless;
- **output:** pointwise in \(X\), but only (1.3) after the cell count.

### 3.2 Vandehey: the cells transform to the accepted cone

J. Vandehey,
[*Error term improvements for van der Corput transforms*](https://arxiv.org/abs/1205.0090),
states, in the theorem labelled `thm:textbook` (quoted there as Huxley,
Lemma 5.5.3), the following standard transform.  If \(f\) is real and
\(C^4\) on \([a,b]\), \(M\geq b-a\),

\[
 f''\asymp T/M^2,\qquad f^{(3)}\ll T/M^3,\qquad
 f^{(4)}\ll T/M^4,
\]

and \(g\) is real of variation \(V\), then

\[
 \sum_{a\leq n\leq b}g(n)e(f(n))
 =\sum_{f'(a)\leq r\leq f'(b)}
 \frac{g(x_r)e(f(x_r)-rx_r+1/8)}{\sqrt{f''(x_r)}}
 +O\!\left((V+|g(a)|)
 \left(\frac{M}{\sqrt T}+\log(f'(b)-f'(a)+2)\right)\right),
\]

where (f'(x_r)=r).  The source also records the starred endpoint
convention in its general transform formula.

Hypothesis audit for (f=F_h):

- **phase and smoothness:** (2.7) verifies all derivative conditions
  with \(M\asymp D,T=hX/D\), uniformly on a fixed dyadic shell;
- **coefficient norm:** \(g(n)=w_D(2n+1)\) has \(V+|g(a)|\ll1\);
- **parameter range:** the theorem itself does not require a hidden
  average in \(X\).  In the active range \(Q_h=T/M\gg1\);
- **absolute-value placement:** taking absolute values only after the
  transform preserves (2.11); taking them termwise gives exactly the
  square-root loss above;
- **endpoint:** the theorem permits \(M\geq b-a\), so a moving top
  truncation does not alter the derivative constants.  Starred versus
  included integer endpoint conventions differ by \(O(1)\), but an
  exact reuse should retain the project's already audited endpoint term;
- **conclusion:** it validates equivalence to the cone, not a bound for
  that cone.

### 3.3 Tao--Trudgian--Yang and Heath-Brown: applicable but already exhausted

T. Tao, T. Trudgian and A. Yang,
[*New exponent pairs, zero density estimates, and zero additive energy
estimates: a systematic approach*](https://arxiv.org/abs/2501.16779),
Definitions 5 and 11, Lemma 12, and Theorem 20, certify the exponent pair

\[
 (\kappa,\lambda)=\left(\frac{89}{1282},\frac{997}{1282}\right)
\]

for their reciprocal model phase.  Splitting (d\equiv1,3\pmod4)
makes (\chi_4) constant and leaves a pure shifted-lattice reciprocal
phase.  The fixed BV profile transfers by partial summation.  This is
the already accepted bound

\[
 B_{1,L}(D;X)
 \ll_\varepsilon
 X^{[89(1+\ell)+819\delta]/1282+\varepsilon},
\]

which closes exactly (178\ell+1638\delta\leq463), not the residual
corridor.  The source requires a model phase, (T\geq N\geq1), and an
unweighted interval; all are met only after the residue-class reduction
and BV transfer.  It does not accept arbitrary spatial coefficients.

D. R. Heath-Brown,
[*A new (k)-th derivative estimate for exponential sums via
Vinogradov's mean value*](https://arxiv.org/abs/1601.04493), Theorem 1,
assumes (f\in C^k), (k\geq3), and
(0<\lambda_k\leq f^{(k)}\leq A\lambda_k), and gives the three-term
derivative bound recorded in the Round-10 source audit.  For the
reciprocal phase, (|f^{(k)}|\asymp hX/D^{k+1}), so it applies after a
sign change if necessary.  It is coefficient-free and has no special
(\chi_4) saving; BV transfer is allowed, arbitrary bounded weights are
not.  Optimizing (k) does not close the residual corridor and supplies
no new graph dependency beyond the existing exponent-pair envelope.

### 3.4 Explicitly rejected analogies

1. **Finite-field reciprocals.**  I. Shparlinski,
   [*On Bilinear Exponential and Character Sums with Reciprocals of
   Polynomials*](https://arxiv.org/abs/1504.03192), estimates
   (\sum_{u,v}\alpha_u\beta_v\,\mathbf e_p(u/f(v))) over
   (\mathbb F_p).  Division is finite-field inversion and the phase is
   an additive character modulo (p).  The real phase (e(hX/d)) has
   neither a modulus nor an inverse residue.  No exact bridge exists.

2. **Kloosterman fractions.**  S. Bettin and V. Chandee,
   [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/abs/1502.00769),
   Theorem 1, treats (e(\vartheta a\overline m/n)) with
   ((m,n)=1), a modular inverse, three independent variables, and
   (\ell^2) coefficient norms.  None of these hypotheses matches
   (hX/d).

3. **Separable multilinear monomials.**  Robert--Sargos,
   [*Three-dimensional exponential sums with monomials*](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf),
   and Kowalski--Robert--Wu,
   [*Small gaps in coefficients of L-functions and B-free numbers in
   small intervals*](https://arxiv.org/abs/math/0507001), require two or
   three independent long variables and a separable monomial phase.
   Freezing or deleting a variable does not preserve their stated
   parameter terms.  In particular, the KRW proposition excludes a
   linear exponent in either independent variable.  A complete
   (B)-process creates (2.11), but then one must prove a new bound for
   that exact cone with its symbol and hard edge.  The analogy is not an
   import.

The search found no primary theorem for the full pointwise sum

\[
 \sum_{h\asymp L}u_{L,H}(h)
 \sum_{d\asymp D}\chi_4(d)w_D(d)e(hX/d)
\]

that retains the two variables and improves the accepted TTY wedge on
(mathcal U_1).

## 4. Required hostile controls and outcomes

### 4.1 Literal adjacent-pair cancellation: fail

Since (\chi_4(d+2)=-\chi_4(d)), one adjacent pair equals

\[
 \chi_4(d)e(hX/d)
 \left(1-e\!\left(-\frac{2hX}{d(d+2)}\right)\right),
\]

whose modulus is

\[
 2\left|\sin\!\left(\pi\frac{2hX}{d(d+2)}\right)\right|.
 \tag{4.1}
\]

It is small when (q_h(d)) is near an integer and maximal when
(q_h(d)) is near a half-integer.  At, for example,
(q_h(d)\equiv1/4\pmod1), the pair has size (\sqrt2), although it is
outside every sufficiently narrow half-integer resonance cell.  Thus
"nonresonant pairs cancel" is false if interpreted termwise.
Nonresonant cancellation is a multi-term Kusmin--Landau statement.

Outcome: **fail for termwise pairing; pass only in the interval-sum
sense of (2.4).**

### 4.2 A coherent resonance cell: scoped adversarial pass

Assume one stationary point (n_m) from (2.8) lies a fixed distance
inside the shell and (1\ll Q_h\ll D).  Put

\[
 R=c\sqrt{D/Q_h}
\]

with small fixed (c>0), and choose a triangular real weight supported
on (|n-n_m|\leq R), equal to one on the central half.  Its supremum
plus total variation is (O(1)).  Taylor's theorem and (2.7) give, after
subtracting the integral linear phase,

\[
 F_h(n_m+t)-F_h(n_m)-F_h'(n_m)t
 =O\!\left(\frac{Q_h}{D}t^2
 +\frac{Q_h}{D^2}|t|^3\right)=O(c^2)
\]

for (|t|\leq R).  Taking (c) small places all central summands in
one fixed angular sector, so that their sum has modulus

\[
 \gg R\asymp\sqrt{D/Q_h}.
\]

This saturates the size of one (B)-process stationary term.  It
falsifies any assertion that a resonance cell costs (O(1)) solely
because the spatial profile has normalized BV.

Scope: the triangular profile depends on the selected cell and is not
the project's fixed actual profile.  The control does not disprove
cancellation between different cells for the actual profile; it shows
that such cancellation is a necessary new ingredient.

Outcome: **pass as a scoped adversarial control.**

### 4.3 Exact-square top family: positive control only

For (X=y^2) and odd (d=y-2j) near the top,

\[
 \frac{2hy^2}{d(d+2)}
 =2h\left(1+O\left(\frac{j+1}{y}\right)\right).
\]

Hence a sufficiently short top segment lies near the integer, not the
half-integer, side of (4.1), and adjacent character terms cancel.  This
is consistent with the project's exact-square positive control.  It
does not control the half-integer cells farther inside the shell and
cannot prove a uniform bound for generic (X).

Outcome: **pass as a local positive control; no asymptotic promotion.**

### 4.4 Coefficient, endpoint, and averaging controls

- Actual Vaaler coefficients are retained in the block and only their
  proved dyadic (\ell^1) bound is used.
- The fixed spatial profile is retained in the no-go theorem; only the
  explicitly labelled coherent-cell test changes it.
- A hard upper cutoff is an interval endpoint or one BV jump, so all
  estimates are uniform there.
- Both frequency signs follow by conjugation and separate estimation.
- No average in (X) is used.
- No numerical experiment was performed.

## 5. First doubtful or unproved step

The first genuinely open step is cancellation in the dual cone (2.11),
possibly jointly with (h\asymp L), while retaining the actual Vaaler
coefficient, sampled spatial profile, affine parity factor, and hard
endpoint.  Neither the cell count nor any searched one-variable theorem
supplies that cancellation.

The adversarial coherent-cell control is deliberately scoped: it does
not show that the project's fixed profile saturates the sum of all cells.
Conversely, the exact-square control proves cancellation only in one
special nonresonant top segment.  Promoting either observation to a
global lower or upper bound would be unjustified.

## 6. Dependencies and exact artifacts used

Repository artifacts:

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md`
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_literature_hostile_audit.md`
- `rounds/codex-managed/m9-m1-cross-product-offset-pairing/synthesis.md`
- `sources/tao_trudgian_yang_2025.md`

Primary web sources inspected or audited:

- Arias de Reyna, arXiv:2002.05982, Lemma 2.
- Vandehey, arXiv:1205.0090, the standard BV (B)-process theorem and
  transform formula.
- Tao--Trudgian--Yang, arXiv:2501.16779v1, Definitions 5 and 11,
  Lemma 12, Theorem 20.
- Heath-Brown, arXiv:1601.04493v3, Theorem 1.
- Shparlinski, arXiv:1504.03192, finite-field reciprocal bilinear sums.
- Bettin--Chandee, arXiv:1502.00769v1, Theorem 1.
- Robert--Sargos, *J. reine angew. Math.* 591 (2006), Theorem 1.
- Kowalski--Robert--Wu, arXiv:math/0507001v1, Proposition 5.

## 7. Recommended state effect

1. **Promote** the exact increment identity (1.1).
2. **Promote a scoped no-go**: Kusmin--Landau resonance-cell summation
   performed separately in (h) yields only (1.4), hence no new point
   of (mathcal U_1).
3. **Record the equivalence warning**: a complete (B)-process sends
   the cells to the signed cone (2.11); local cell decomposition does
   not simplify the accepted M1 transform.
4. **Reject** literal termwise cancellation for all nonresonant adjacent
   pairs, resonance-cell (O(1)) bounds from normalized BV alone, and
   imports from finite-field reciprocals, modular inverses, or separable
   multilinear monomials without an exact bridge.
5. **Retain open** a joint ((h,m)) cone-cancellation lemma with the
   actual profile.  This is the only part of the proposed strategy not
   ruled out here.
6. Keep `M9-M1-shifted-divisor-correlation-PSC`,
   `M9-M1-cross-product-odd-kernel-discrepancy`, `M9-M1`, `M9`, and the
   Gauss-circle target open.
