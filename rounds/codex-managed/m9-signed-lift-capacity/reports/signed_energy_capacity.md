# Round 3 report: capacity of the B1 signed-lift envelope

## 1. Result and verdict

**Result: a B1-only capacity lemma and a rigorous no-go theorem.**  Freeze the
Vaaler coefficients at one dyadic scale.  The B1 envelope, together with its
exact reduced-fraction support, is strong enough to give

\[
 \|A_\chi\|_1\ll D\log(2H),\qquad
 \|A_\chi\|_2^2\ll D,
 \qquad
 \sum_r|R_\chi(r)|^2\ll_\varepsilon D^2X^\varepsilon,
\]

where \(R_\chi=A_\chi*A_\chi\).  Thus B1 controls the exact pair-sum
diagonal.  For a Schwartz global smoothing it gives only

\[
 \frac1X\int_{\mathbb R}V(t/X)|S_D(t)|^4\,dt
 \ll_{\varepsilon,V}
 D^2X^\varepsilon\left(1+\frac{D^4}{X}\right).
\]

The factor \(1+D^4/X\) is the unresolved off-diagonal capacity.  It is not a
technical artifact that can be discarded from B1 alone.  There is an even,
odd-numerator, exact-support coefficient system saturating the B1 envelope
for which the normalized signed fat-band form is

\[
 \gg \frac{D^3}{X}
\]

for \(D\ge X^{1/3+\delta}\), up to a divisor-bound error.  Consequently B1
alone cannot imply \(|c_\chi(D;X)|\ll_\varepsilon X^\varepsilon\), or even
the corresponding critical signed fat-band estimate, in the upper range.
This is a logical obstruction to using only the pointwise envelope.  It is
**not** a lower bound for the actual Vaaler/\(\chi_4\) signed form, because the
countermodel deliberately omits correlations among the other numerators.

Verdict:

- retain B1 as a pair-weight lemma if its independent normalization audit
  succeeds;
- reject the implication “B1 \(\Rightarrow\) signed fat-band constant”;
- keep the actual signed cancellation theorem and the average-to-pointwise
  bridge open and separate.

No numerical experiment was used.

## 2. Exact frozen normalization

Let \(H=H_D\) be fixed while the moment variable \(t\) varies, and let
\(w_D\) be the fixed dyadic denominator weight.  Put

\[
 S_D(t)=
 \sum_{1\le |h|\le H}\beta_{h,H}
 \sum_d w_D(d)e\!\left(\frac{th}{4d}\right).
\]

Let \(\mathcal X_{D,H}\) be the finite set of reduced fractions \(x=p/q\),
with \(q>0\), for which there is an integer \(g\ge1\) satisfying

\[
 gq\in\operatorname{supp}(w_D),\qquad 1\le g|p|\le H.
\]

Define the exact signed lift weight

\[
 A_\chi(p/q)=
 \sum_{\substack{g\ge1:\ gq\in\operatorname{supp}(w_D)\\
                         1\le g|p|\le H}}
 \beta_{gp,H}w_D(gq).
\]

Reduction and collection of all lifts gives the exact identity

\[
 S_D(t)=\sum_{x\in\mathcal X_{D,H}}A_\chi(x)e(tx/4).
\]

For complex weights define

\[
 R_\chi(r)=\sum_{x+y=r}A_\chi(x)A_\chi(y).
\]

If the weights are real, then \(A_\chi\) and \(R_\chi\) are real; the
following conjugated form is valid without that restriction.

Choose a fixed real, nonnegative, nonzero \(V\in C_c^\infty((1/2,3))\), and
use the Fourier convention

\[
 K(\xi)=\int_{\mathbb R}V(u)e(\xi u)\,du.
\]

Then the frozen-coefficient smoothed global fourth moment is exactly

\[
 \boxed{
 \mathcal G_4^V(D;X)
 :=\frac1X\int_{\mathbb R}V(t/X)|S_D(t)|^4\,dt
 =\sum_{r,s}R_\chi(r)\overline{R_\chi(s)}
 K\!\left(\frac{X(r-s)}4\right). }
\tag{2.1}
\]

Thus the exact normalization of the full signed off-diagonal constant is

\[
 \boxed{
 c_\chi^V(D;X)
 :=D^{-2}\operatorname{Re}
 \sum_{r\ne s}R_\chi(r)\overline{R_\chi(s)}
 K\!\left(\frac{X(r-s)}4\right). }
\tag{2.2}
\]

Since \(V\) is real, the full sum in (2.2) is already real, and

\[
 \mathcal G_4^V(D;X)
 =K(0)\sum_r|R_\chi(r)|^2+D^2c_\chi^V(D;X).
\tag{2.3}
\]

For a fixed \(\kappa>0\), the exact critical fat-band subform is

\[
 \boxed{
 c_{\chi,\le\kappa}^{V}(D;X)
 :=D^{-2}\operatorname{Re}
 \sum_{0<|r-s|\le\kappa/X}
 R_\chi(r)\overline{R_\chi(s)}
 K\!\left(\frac{X(r-s)}4\right). }
\tag{2.4}
\]

This reduced-fraction band is the exact band selected by global smoothing.
For an individual lifted tuple,

\[
 r-s=\frac{N}{d_1d_2d_3d_4};
\]

hence (2.4) is equivalent tuple by tuple to
\(0<|N|\le \kappa d_1d_2d_3d_4/X\).  Replacing the varying denominator
product by \(D^4\) is only a dyadic comparability, not an exact identity.

## 3. B1-only capacity lemma

Assume the sharp-shell support \(D\le gq<2D\), \(1\le g|p|\le H\), and B1:

\[
 A_\chi(p/q)=0\quad(2\mid p),
 \qquad
 |A_\chi(p/q)|\le C_B\frac{q}{D|p|}\quad(2\nmid p).
\tag{3.1}
\]

The proof below uses no sign cancellation.  Put

\[
 B(p/q)=C_B\frac{q}{D|p|}\mathbf1_{\mathcal X_{D,H}}(p/q)
 \mathbf1_{2\nmid p}.
\]

The exact support implies \(q<2D\), \(|p|\le H\), and, more sharply,
\(q\ge D|p|/H\) whenever the lift set is nonempty.  Therefore

\[
 \sum_xB(x)
 \ll \frac1D\sum_{1\le|p|\le H}\frac1{|p|}
                    \sum_{q<2D}q
 \ll D\log(2H),
\tag{3.2}
\]

\[
 \sum_xB(x)^2
 \ll \frac1{D^2}\sum_{p\ne0}\frac1{p^2}
                     \sum_{q<2D}q^2
 \ll D,
\tag{3.3}
\]

and similarly

\[
 \sum_xB(x)^4\ll D,\qquad \|B\|_\infty\ll1.
\tag{3.4}
\]

These estimates immediately imply the same bounds for \(|A_\chi|\).

There is also a stronger quartic/additive-energy conclusion.  Define the
nonnegative pair majorant

\[
 R_B(r)=\sum_{x+y=r}B(x)B(y).
\]

If \(r=\mu/Q\ne0\) is reduced and
\(p_1/q_1+p_3/q_3=\mu/Q\), then

\[
 (\mu q_1-Qp_1)(\mu q_3-Qp_3)=Q^2p_1p_3.
\tag{3.5}
\]

For fixed nonzero \(p_1,p_3\), (3.5) gives at most
\(2\tau(Q^2|p_1p_3|)\) denominator pairs.  Here
\(Q\le q_1q_3<4D^2\) and \(|p_i|\le H\).  The elementary divisor bound,
the inequality \(B(p/q)\le2C_B/|p|\), and two harmonic sums give

\[
 \sup_{r\ne0}R_B(r)\ll_\varepsilon X^\varepsilon.
\tag{3.6}
\]

For \(r=0\), reducedness forces \(q_3=q_1\), \(p_3=-p_1\), so

\[
 R_B(0)\le\sum_xB(x)^2\ll D.
\tag{3.7}
\]

Finally, \(\sum_rR_B(r)=(\sum_xB(x))^2\ll D^2\log^2(2H)\).  Combining
(3.6)--(3.7),

\[
 \boxed{
 \sum_r|R_\chi(r)|^2
 \le\sum_rR_B(r)^2
 \ll_\varepsilon D^2X^\varepsilon. }
\tag{3.8}
\]

Thus B1 does control the exact pair-sum diagonal in (2.3).  Notice that
(3.8) is still character-blind: it also holds for unsigned and adversarial
coefficients obeying the same envelope.

Every pair sum \(r\) has reduced denominator at most \(4D^2\).  Consequently
two distinct pair sums are separated by at least \(1/(16D^4)\).  Since \(K\)
is Schwartz,

\[
 \sup_r\sum_s\left|K\!\left(\frac{X(r-s)}4\right)\right|
 \ll_V 1+\frac{D^4}{X}.
\tag{3.9}
\]

Schur's test applied to (2.1), followed by (3.8), gives the strongest direct
B1-plus-rational-spacing capacity estimate:

\[
 \boxed{
 \mathcal G_4^V(D;X),\quad
 D^2|c_\chi^V(D;X)|,quad
 D^2|c_{\chi,\le\kappa}^V(D;X)|
 \ll_{\varepsilon,V,\kappa}
 D^2X^\varepsilon\left(1+\frac{D^4}{X}\right). }
\tag{3.10}
\]

For the two off-diagonal quantities, (3.10) is understood as an absolute
upper bound; the diagonal in \(\mathcal G_4^V\) is covered by (3.8).
This reaches the desired \(D^2X^\varepsilon\) global fourth-moment scale only
when \(D\lesssim X^{1/4+o(1)}\), not in the upper active range.

## 4. Envelope-saturating obstruction

The following countermodel obeys every condition visible in B1, including
odd numerator support, exact lift participation, and the actual evenness
\(A(-x)=A(x)\).

Let

\[
 \mathcal Q_D=\mathbb Z\cap[5D/4,7D/4],
\]

and choose a fixed \(0<a\le C_B/2\).  Define

\[
 A^*(1/q)=A^*(-1/q)=a\quad(q\in\mathcal Q_D),
 \qquad A^*(x)=0\quad\text{otherwise}.
\tag{4.1}
\]

For \(q\in\mathcal Q_D\), the lift \(g=1\) has \(d=q\in[D,2D)\) and
\(h=\pm1\), so (4.1) has exact support whenever \(H\ge1\).  Moreover
\(a\le C_Bq/D\), so it saturates (3.1) up to a fixed constant on the generic
single-lift band \(p=\pm1\), \(q\asymp D\).

Let \(m(r)\) count ordered pairs \((q_1,q_3)\in\mathcal Q_D^2\) with
\(1/q_1+1/q_3=r\).  These \(\asymp D^2\) ordered pairs have pair sums in an
interval of length \(\ll D^{-1}\).  Partition that interval into half-open
windows of length \(\kappa/X\).  The number of windows is \(\ll X/(\kappa D)\)
throughout the active range.  Cauchy--Schwarz therefore gives

\[
 \#\left\{(q_1,q_3,q_2,q_4):
 \left|\frac1{q_1}+\frac1{q_3}-\frac1{q_2}-\frac1{q_4}\right|
 \le\frac\kappa X\right\}
 \gg_\kappa \frac{D^5}{X}.
\tag{4.2}
\]

The exact-equality part of (4.2) is only \(O_\varepsilon(D^{2+\varepsilon})\).
Indeed, for a fixed reduced \(r=\mu/Q\ne0\),

\[
 (\mu q_1-Q)(\mu q_3-Q)=Q^2,
\]

so \(m(r)\ll_\varepsilon D^\varepsilon\), and hence
\(\sum_rm(r)^2\le(\sup_rm(r))\sum_rm(r)\ll_\varepsilon D^{2+\varepsilon}\).
It follows that the strictly off-diagonal count in (4.2) is

\[
 \gg_\kappa \frac{D^5}{X}-O_\varepsilon(D^{2+\varepsilon}).
\tag{4.3}
\]

Because \(K(0)=\int V>0\), continuity supplies a fixed sufficiently small
\(\kappa=\kappa(V)>0\) such that

\[
 \operatorname{Re}K(\xi)\ge K(0)/2
 \qquad (|\xi|\le\kappa/4).
\]

All pair weights in (4.1) have the same sign, so \(R^*(r)\ge0\).  Restricting
(2.4) to the positive fractions used in (4.2) and applying (4.3) gives

\[
 \boxed{
 c_{*,\le\kappa}^V(D;X)
 \ge c_{V,a}\frac{D^3}{X}-O_\varepsilon(D^\varepsilon). }
\tag{4.4}
\]

For every fixed \(\delta>0\), choose the divisor-bound epsilon small enough.
If \(D\ge X^{1/3+\delta}\), the main term in (4.4) is at least
\(X^{3\delta}\) and dominates the exact-equality error.  Choosing the target
epsilon below \(3\delta\) contradicts a uniform
\(c_{\chi,\le\kappa}^V\ll_\varepsilon X^\varepsilon\) theorem for the B1
envelope class.

The obstruction is deliberately an envelope-class construction.  It need
not arise from one fixed smooth profile \(w_D\), and therefore it does not
refute the actual \(A_\chi\).  It proves the exact logical statement needed
here: the pointwise inequality (3.1), its support, parity, and evenness do not
contain enough information to force signed fat-band cancellation.

## 5. Missing cancellation statement

The minimal missing theorem is not another pointwise estimate for
\(A_\chi\).  It is an off-diagonal signed autocorrelation estimate for the
*actual* lift weights:

\[
 \boxed{
 \left|
 \sum_{0<|r-s|\le\kappa/X}
 R_\chi(r)\overline{R_\chi(s)}
 K\!\left(\frac{X(r-s)}4\right)
 \right|
 \ll_{\varepsilon,V,\kappa}D^2X^\varepsilon. }
\tag{5.1}
\]

For the full global moment, (5.1) must be supplemented by a graded tail
estimate, or replaced by the full off-diagonal bound

\[
 \left|
 \sum_{r\ne s}R_\chi(r)\overline{R_\chi(s)}
 K\!\left(\frac{X(r-s)}4\right)
 \right|
 \ll_{\varepsilon,V}D^2X^\varepsilon.
\tag{5.2}
\]

A proof of (5.1) or (5.2) must use information absent from B1: the exact
\(\chi_4(gp)\) alternation, the \(\Phi(g|p|/(H+1))\) variation, and/or
correlations among distinct numerators and denominators.  In particular, the
generic band \(q\asymp D\) has only one lift and B1 gives no gain there.  The
positive \(p=1\) subtotal in (4.1) is also present, with a fixed sign, inside
the actual coefficient system; only complementary numerator classes can
cancel it.  A positive subtotal cannot lower-bound or upper-bound the full
signed form without such a theorem.

## 6. Controls

### `signed-vs-unsigned`

Input: actual signed \(A_\chi\), its absolute majorant \(B\), and the
same-sign envelope model (4.1).

Outcome: (3.2)--(3.10) are sign-blind and hold for all three.  The same-sign
model has fat-band size \(\gg D^3/X\) after normalization.  Thus B1 contains
no signed cancellation.  The actual signed form may still be small; proving
that requires (5.1) or (5.2).

### `proves-too-much`

Input: replace \(A_\chi\) by unsigned or adversarial coefficients satisfying
the same envelope.

Outcome: any claimed derivation of
\(c_\chi\ll X^\varepsilon\) using only (3.1) would also apply to (4.1), in
contradiction with (4.4).  Therefore such a derivation proves a false
stronger statement.  The control rejects the B1-implies-energy step.

### `dyadic-endpoints`

For the obstruction scale \(D^3/X\):

\[
\begin{array}{c|c|c}
D & D^3/X & \text{consequence}\\ \hline
X^{1/3} & 1 & \text{crossover only; no power contradiction}\\
X^{3/8} & X^{1/8} & \text{B1-only }X^\varepsilon\text{ target fails}\\
X^{1/2} & X^{1/2} & \text{B1-only }X^\varepsilon\text{ target fails strongly.}
\end{array}
\]

For comparison, the Schur capacity loss \(1+D^4/X\) in (3.10) is
\(1+X^{1/3}\), \(1+X^{1/2}\), and \(1+X\), respectively.  At the lower
endpoint \(D=X^{1/4}\), that loss is only \(O(1)\).

No endpoint is silently crossed, and \(H_D\asymp DX^{-1/4}\ge1\) is required
for the countermodel.

## 7. Pointwise-scope warning

Even a proof of (5.2) would give a frozen-coefficient **global fourth
moment**, not the pointwise estimate

\[
 |S_2(D;X_0)|\ll_\varepsilon X_0^{1/4+\varepsilon}.
\]

The accepted derivative propagation from a global fourth moment yields only

\[
 |S_2(D;X_0)|\ll_\varepsilon D^{3/5}X^{3/20+\varepsilon},
\]

which is \(X^{9/20+\varepsilon}\) at \(D=X^{1/2}\).  A large-value theorem,
coefficient-unfreezing argument, or direct signed pointwise estimate remains
necessary.  No moment-only conclusion in this report changes `M9-M2`.

## 8. First doubtful or unproved step

There is no unproved step in the abstract capacity obstruction once B1 and
the elementary divisor bound are assumed.  The first unproved step toward
the project goal is (5.1), or the stronger (5.2), for the actual lift
weights.  The separate B1 proof must also state and verify the exact
smooth/BV weight norm and every truncation edge; this report assumes B1 and
does not rederive it.

The countermodel's non-realizability by a single fixed dyadic profile is a
scope boundary, not a hidden proof step: it is why the result rejects only a
B1-*only* implication and does not reject the actual signed mechanism.

## 9. Dependencies and exact artifacts used

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `state/control_models.md`
- `rounds/obligation-main/round_008/responses/A4-008.md`
- `rounds/obligation-main/round_008/reviews/A1.md`
- `rounds/codex-managed/m9-unit-frequency-w1-validation/synthesis.md`

Mathematical dependencies used: the frozen two-sided fourth-moment algebra,
the exact reduced-fraction lift collection, the elementary divisor bound,
and B1 as an assumption.  No external theorem and no numerical computation
was used.

## 10. Recommended state effect

- `M9-M2-signed-lift-cancellation-B1`: **retain**, subject to the independent
  proof's exact weight and endpoint audit.  Do not enlarge its implication.
- `M9-M2-signed-fat-band-constant`: **retain as proposed**.  Add this report
  as negative evidence against the step “B1 alone implies the constant.”
- Add a scoped obstruction/no-go statement: B1 controls the exact pair-sum
  energy but cannot, by itself, yield upper-range signed fat-band
  cancellation; any successor must prove (5.1) or (5.2) from the actual
  \(\chi_4\)-structured lifts.
- `M9-M2`, `M9-near-collision-estimate`, `M9`, and the pointwise bridge:
  **no promotion**.

