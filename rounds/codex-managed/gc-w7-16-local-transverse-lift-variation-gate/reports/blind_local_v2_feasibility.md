# 1. Result: sharp abstract no-go and a repaired lemma

The proposed estimate does **not** follow from the stated birth count, the
presence of the common character \(\chi _4\), and the pointwise coefficient
scale.  In fact, the sharp worst-case size permitted by those assumptions is

\[
   \|U_\rho\|_{V^2(I)}\asymp A G\sqrt{N_\rho},
   \qquad A:=L^{-1},
\]

up to absolute constants, even with a fixed window and hence zero births and
exits.  Take a fixed integer interval \(H\) containing \(M\asymp G\) odd
integers and

\[
  \omega_\rho(g,v)=A\chi _4(g)(-1)^v.
\]

Then \(U_\rho(v)=AM(-1)^v\), so, if \(I\) has \(n\asymp N_\rho\)
sampled values,

\[
 \|U_\rho\|_{V^2(I)}^2=(4n-2)A^2M^2.
\]

This matches the universal pointwise upper bound up to a constant.  A
constant-in-\(v\) version already disproves the desired estimate solely
through the two endpoint terms.  There are also independent countermodels
for clumped births and for every-step coefficient variation after endpoint
values have been set to zero.

The minimally informative repair is to control three distinct energies:
the two fixed endpoint values, the birth/exit packets, and the signed
continuous coefficient increments.  Under the explicit hypotheses in
Section 2, each is \(O(A^2J_B)\), and then

\[
  \|U_\rho\|_{V^2(I)}\ll A J_B^{1/2}.
\]

Taking \(A=L^{-1}Y^\delta\) and relabelling the epsilon budget gives the
displayed \(L^{-1}J_B^{1/2}Y^\varepsilon\) form.  The supplied statement does
not contain the literal M1/M2 coefficient formula, so this no-go is a logical
refutation of the proposed *abstract inference*, not a finding that the
actual coefficient package necessarily realizes the adversary.

# 2. Exact statement and hypotheses

Write the starred interval using multipliers
\(s_v(g)\in\{0,\tfrac12,1\}\), supported on the integer interval
\(I_\rho(v)\):

\[
 U_v=\sum_g\chi _4(g)s_v(g)\omega_v(g),\qquad |\omega_v(g)|\le A.
\]

For consecutive samples put \(r_v(g)=\min(s_v(g),s_{v+1}(g))\) and define

\[
\begin{aligned}
 C_v&:=\sum_g\chi _4(g)r_v(g)
              \bigl(\omega_{v+1}(g)-\omega_v(g)\bigr),\\
 B_v&:=\sum_g\chi _4(g)
 \Bigl((s_{v+1}(g)-r_v(g))\omega_{v+1}(g)
       -(s_v(g)-r_v(g))\omega_v(g)\Bigr).
\end{aligned}
\tag{2.1}
\]

Thus \(B_v\) includes births, exits, and changes of endpoint half-weight,
whereas \(C_v\) is the coefficient change on the persistent part of the
window.  The identity

\[
 U_{v+1}-U_v=B_v+C_v
\tag{2.2}
\]

is exact.

**Energy repair lemma.**  Uniformly in \(\rho\), suppose

\[
\begin{aligned}
 |U_{v_-}|^2+|U_{v_+}|^2&\le C_0A^2J_B, \tag{E}\\
 \sum_v|B_v|^2&\le C_1A^2J_B,                 \tag{B}\\
 \sum_v|C_v|^2&\le C_2A^2J_B.                 \tag{C}
\end{aligned}
\]

Then

\[
 \|U_\rho\|_{V^2(I)}
 \le (C_0+2C_1+2C_2)^{1/2}A J_B^{1/2}.
\tag{2.3}
\]

The literally necessary-and-sufficient extra condition is (E) together
with \(\sum_v|B_v+C_v|^2\ll A^2J_B\).  The separated conditions (B) and
(C) are the minimal cancellation-robust version: they do not assume a
fortuitous cancellation between geometrically unrelated endpoint motion and
coefficient motion.  The three countermodels in Section 3 show that none of
(E), (B), and (C) can be inferred from the other two and the stated data.

Here is one checkable structural set of hypotheses implying (E)--(C).  For
an integer interval \(H=[h_0,h_1]\), set

\[
 \|a\|_{\mathrm{BV}(H)}
 :=|a(h_0)|+\sum_{h=h_0}^{h_1-1}|a(h+1)-a(h)|.
\tag{2.4}
\]

Assume:

1. The two endpoint sequences \(g\mapsto s_{v_\pm}(g)\omega_{v_\pm}(g)\)
   have \(\mathrm{BV}\)-norm \(O(A)\) on their supports.
2. The support of every birth/exit packet in (2.1) is a union of \(O(1)\)
   integer intervals; its weighted sequence has total \(\mathrm{BV}\)-norm
   \(O(A)\).  The number of transitions with a nonzero packet is
   \(O(J_B)\).  Endpoint half-weight changes are included as packets.
3. The persistent increments satisfy the sampled square-variation bound

   \[
      \sum_v
      \bigl\|g\mapsto r_v(g)
      (\omega_{v+1}(g)-\omega_v(g))
      \bigr\|_{\mathrm{BV}}^2
      \ll A^2J_B.
   \tag{2.5}
   \]

Condition (2.5) may be replaced by the stronger bounded sampled total
variation condition in which the sum of these \(\mathrm{BV}\)-norms is
\(O(A)\).  Variation bounded separately for each \(g\), followed by an
unsigned sum over \(g\), is not a substitute: it can lose the full factor
\(G\).

A particularly transparent sufficient factorization is

\[
 \omega_v(g)=A\,a(g)b_v,
\tag{2.6}
\]

where \(a\) has uniformly bounded \(\mathrm{BV}\)-norm on every relevant
subinterval, \(|b_v|\ll1\),
\(\sum_v|b_{v+1}-b_v|^2\ll J_B\), and the number of active endpoint-motion
transitions is \(O(J_B)\).  Finite sums of such factorizations are also
allowed if the corresponding norms are summable.  Formula (2.6) is only a
sufficient structural example; it is not asserted for the unavailable
literal M1/M2 weights.

With pointwise control alone, let

\[
 m_v:=\sum_g|s_{v+1}(g)-s_v(g)|.
\]

Then \(|B_v|\le A m_v\).  Hence a total birth count
\(\sum_vm_v\ll J_B\) proves (B) only if one also has, for example,
\(\sum_vm_v^2\ll J_B\) (in particular \(m_v=O(1)\)).  Without such a
packet-multiplicity condition, clumping gives only the sharp bound
\(\sum_v|B_v|^2\ll A^2J_B^2\).  The character-BV hypothesis above is an
alternative way to control a large contiguous packet before taking its
absolute value.

# 3. Proof or derivation

## 3.1 Exact energy proof

Identity (2.2) follows term by term from

\[
\begin{aligned}
 &r_v(\omega_{v+1}-\omega_v)
 +(s_{v+1}-r_v)\omega_{v+1}
 -(s_v-r_v)\omega_v\\
 &\hspace{35mm}=s_{v+1}\omega_{v+1}-s_v\omega_v.
\end{aligned}
\]

Consequently,

\[
\begin{aligned}
 \|U\|_{V^2(I)}^2
 &=|U_{v_-}|^2+|U_{v_+}|^2+\sum_v|B_v+C_v|^2\\
 &\le |U_{v_-}|^2+|U_{v_+}|^2
       +2\sum_v|B_v|^2+2\sum_v|C_v|^2,
\end{aligned}
\]

which proves (2.3).

## 3.2 Why the character helps only before modulus

The partial sums of \(\chi _4\) over any integer interval are bounded by
an absolute constant.  Abel summation therefore gives

\[
 \left|\sum_{g\in H}\chi _4(g)a(g)\right|
 \ll \|a\|_{\mathrm{BV}(H)}.
\tag{3.1}
\]

Applying (3.1) separately to the \(O(1)\) endpoint pieces proves (E) and
gives \(|B_v|\ll A\) for each active birth transition.  There are
\(O(J_B)\) such transitions, so (B) follows.  Applying (3.1) to each
persistent increment and then using (2.5) proves (C).  This establishes the
structural repair and, in particular, the factorized case (2.6).

It is essential that (3.1) be applied to the signed character sum before an
absolute value is distributed over \(g\).  The pointwise estimate
\(|a(g)|\le A\) gives only \(AG\) after that distribution.  Moreover,
\(a(g)=A\chi _4(g)\) has \(\mathrm{BV}\)-norm \(\asymp AG\) and conjugates
the character, so (3.1) correctly returns the large answer rather than
creating nonexistent cancellation.

## 3.3 Sharp global countermodel

Fix the window: \(s_v=1_H\), with no half-weights and no births or exits.
Let \(M\) be the number of odd integers in \(H\); one can choose
\(M\asymp G\).  Put

\[
 \omega_v(g)=A\chi _4(g)(-1)^v.
\]

Then

\[
 U_v=A(-1)^v\sum_{g\in H}\chi _4(g)^2
     =AM(-1)^v,
\]

and for \(n\) sampled values,

\[
 \|U\|_{V^2(I)}^2=2A^2M^2+4(n-1)A^2M^2
                  =(4n-2)A^2M^2.
\tag{3.2}
\]

Conversely, pointwise control and support length at most \(G\) imply
\(|U_v|\ll AG\) and \(|U_{v+1}-U_v|\ll AG\), so the right side of (3.2),
with \(M\) replaced by \(G\), is a universal upper bound up to constants.
Thus the countermodel is sharp for the supplied abstract class.

At the critical longest-lift shell take \(B\asymp D/L=Y^{1/3}\) and
\(\rho=1\).  Since

\[
 \frac{D}{WL}=Y^{-5/48},
\]

one has

\[
 G=Y^{1/6},\qquad Q_B=Y^{11/48},\qquad
 N_1\asymp Y^{11/48},\qquad J_B\asymp Y^{1/16}.
\]

The ratio of (3.2) to the proposed norm scale \(A\sqrt{J_B}\) is

\[
 \frac{G\sqrt{N_1}}{\sqrt{J_B}}=Y^{1/4}.
\tag{3.3}
\]

Because the countermodel uses \(A=L^{-1}\), (3.3) cannot be absorbed by
\(Y^\varepsilon\) for all \(\varepsilon>0\).

## 3.4 Independent endpoint, birth, and continuous-variation obstructions

**Endpoint values.**  In the same fixed window, take instead
\(\omega_v(g)=A\chi _4(g)\), independent of \(v\).  All internal
increments vanish, but

\[
 \|U\|_{V^2(I)}=\sqrt2\,AM\asymp AG.
\]

At the critical shell its ratio to \(A\sqrt{J_B}\) is
\(G/\sqrt{J_B}=Y^{13/96}\).  Thus the endpoint values in the stated
definition cannot be discarded or inferred from the birth count.

**Clumped births.**  Let the endpoint windows be empty and a single
interior window be an interval \(H\) containing \(M\asymp K\) odd
integers, where \(K\asymp J_B\le G\).  (If nonempty intervals are required,
one may pad all samples by a fixed zero-weight singleton.)  Give the new
points the weight \(A\chi _4(g)\).  There is no change on a persistent
point and the endpoint values are zero.  The total number of individual
births plus exits is \(O(K)=O(J_B)\), but the two packet increments have
size \(AM\), so the norm is \(\asymp AK\), not \(A\sqrt K\).  This proves
that a total count alone does not control simultaneous packet energy.  If
each transition contains only \(O(1)\) births/exits, then
\(\sum m_v^2\ll\sum m_v\ll J_B\), and pointwise control does suffice for
the birth part.

**Continuous every-step variation.**  Keep a fixed window consisting of
one odd integer (or a long interval whose unweighted \(\chi _4\)-sum is
nonzero).  Set the weights to zero at \(v_-\) and \(v_+\), and to
\(A(-1)^v\) at interior samples.  There are no births, the two V2 endpoint
values vanish, and no adversarial long \(g\)-sum is involved, yet

\[
 \sum_v|C_v|^2\asymp A^2N_\rho,
 \qquad \|U\|_{V^2(I)}\asymp A\sqrt{N_\rho}.
\]

For \(\rho=1\) at the critical shell, the excess over
\(A\sqrt{J_B}\) is \(\sqrt{N_1/J_B}=Y^{1/12}\).  Thus even perfect
control of the \(g\)-sum does not replace a sampled \(v\)-variation
hypothesis.

# 4. First doubtful or unproved step

The first invalid inference in a proof from the supplied data would be

\[
 |\omega_v(g)|\ll A
 \quad\Longrightarrow\quad
 \left|\sum_{g\in I_\rho(v)}\chi _4(g)\omega_v(g)\right|\ll A.
\]

This implication is false: the admissible phase-conjugating choice
\(\omega_v(g)=A\chi _4(g)\) makes the sum \(\asymp AG\).  Hence the two
V2 endpoint values are already uncontrolled.  After adding endpoint and
\(g\)-regularity hypotheses, the first remaining literal counterterm is

\[
 C_v=\sum_g\chi _4(g)r_v(g)
       (\omega_{v+1}(g)-\omega_v(g)),
\]

which is invisible to the endpoint birth count and can contribute
\(A\sqrt{N_\rho}\), or \(AG\sqrt{N_\rho}\) with character-conjugating
phases.

No permitted artifact supplies the actual M1/M2 formula for
\(\omega_\rho(g,v)\).  It is therefore unproved whether the actual weights
satisfy (E)--(C), (2.5), or a factorization such as (2.6), and it is equally
unproved that the actual weights realize the adversarial examples.  The
next legitimate proof step is an exact algebraic audit of the literal
coefficient package against the endpoint, packet, \(g\)-BV, and sampled
\(v\)-variation conditions; pointwise scale alone cannot complete that
audit.

# 5. Control tests and outcomes

| Required control | Exact input | Expected failure or invariant | Outcome | Implication |
|---|---|---|---|---|
| `local_window_and_birth_count` | Fixed windows (zero births), and separately one block of \(K\asymp J_B\) simultaneous births followed by exits | A count can control only endpoint motion, and total count need not control squared packet size | Fixed-window countermodels fail independently of the count; the clumped packet has norm \(\asymp AK\) | Require direct packet square energy, bounded per-step multiplicity, or character-BV control of each contiguous packet |
| `V2_endpoint_terms` | Constant-in-\(v\) weight \(A\chi _4(g)\) on a fixed interval with \(M\asymp G\) odd points | Internal variation can vanish while the two displayed endpoints remain large | \(\|U\|_{V^2}=\sqrt2 AM\asymp AG\) | Endpoint values need their own hypothesis; the birth count says nothing about them |
| `continuous_weight_variation` | Fixed support, zero endpoint weights, alternating interior weights | Every-step changes survive when births and endpoint values are absent | One odd lift gives \(A\sqrt{N_\rho}\); conjugating a full lift gives \(AG\sqrt{N_\rho}\) | Require (2.5), bounded sampled variation in a signed \(g\)-regularity norm, or an audited factorization |
| `character_partial_sum_before_modulus` | Abel summation for \(\sum\chi _4(g)a(g)\), compared with \(a=A\chi _4\) and with \(\sum|a|\) | Character cancellation is available only with controlled \(g\)-variation and before distributing modulus | Bound (3.1) holds; the adversary has \(\mathrm{BV}\asymp AG\) and produces \(AG\) | A common character plus a pointwise scale is not a cancellation hypothesis |
| `actual_vs_adversarial_lift_coefficients` | All pointwise-admissible weights versus the unavailable literal M1/M2 coefficient | The abstract statement must survive adversarial phases unless exact structure is invoked | The abstract statement fails sharply; actual-package membership in the repaired class is undecided | Reject only the abstract inference; retain the literal coefficient question pending formula-level audit |
| `theta_two_thirds_capacity_threshold` | At \(B\asymp D/L\), \(J_B=Y^{1/16+o(1)}\), \(G=Y^{1/6+o(1)}\) | Only a proved local loss \(J_B^\theta/L\) with \(\theta<2/3\) has the supplied conditional capacity | The repaired square energy gives \(\theta=1/2\), but current hypotheses do not prove it.  A full-shell \(G^{1/2}\) loss equals \(J_B^{4/3+o(1)}\) | Full-shell variation cannot replace the desired local estimate; no downstream capacity claim is earned |
| `finite_stop_rule` | Analytic countermodels (3.2) and the three separated obstructions | A rigorous no-go closes the abstract feasibility test | Countermodels are exact and sharp up to constants; no numerical or web experiment is needed | Stop at the coefficient-norm obstruction and repaired hypotheses |
| `no_exponent_or_M9_promotion` | Scope restricted to (128.B3) | No coefficient-norm result alone changes a Gauss-circle exponent, proves an oscillatory inequality, or changes M9 | No such inference was made | This report is candidate evidence only |

The distinction between \(J_B\) and \(G\) is quantitative, not cosmetic.
On the critical shell,

\[
 J_B-1=Y^{1/16+o(1)},\qquad G=Y^{1/6+o(1)},
\]

so a fixed window may contain \(G\) adversarially aligned coefficients
while generating zero of the \(O(J_B)\) birth events.  Local birth geometry
therefore cannot by itself control full-window endpoint mass.

# 6. Dependencies and exact artifacts used

This statement-only derivation used exactly:

1. `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/briefs/blind_local_v2_feasibility.md`;
2. `rounds/codex-managed/gc-w7-16-local-transverse-lift-variation-gate/blind_statement.md`;
3. `problems/gauss_circle.md`;
4. `state/control_models.md`.

No historical report, sibling report, strategy file, proof-state file, web
source, or numerical experiment was used.  The only character fact invoked
is the elementary bounded partial-sum property of the explicitly named
modulo-four character, proved directly by its four-periodicity and zero
mean.

# 7. Recommended state effect

**Revise/retain, with no promotion.**  Reject the claim that (128.B3)
follows abstractly from birth count, \(\chi _4\), and pointwise scale.  Retain
the literal M1/M2 estimate as an open candidate only after replacing the
missing step by an exact coefficient audit proving either (E)--(C) or the
stated BV/factorization conditions.  Record the fixed endpoint sums and the
persistent increment \(C_v\) as the first two mandatory checks.  Do not
alter any Gauss-circle exponent, oscillatory estimate, graded-correlation
claim, or M9 status.
