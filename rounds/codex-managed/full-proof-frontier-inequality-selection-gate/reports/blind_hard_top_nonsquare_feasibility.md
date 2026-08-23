# Round 127 statement-only report: nonsquare hard-TOP feasibility

## 1. Result: a sharp statement-level no-go

The live fixed-direction quantity is

\[
 \mathcal E_L^{\rm ns}
 =\|A_L^{\rm ns}\chi _4\|_2^2
 =\sum_m\left|
   \sum_{\substack{h\in\mathscr H_L\\m\leq h\leq4m\\hm\notin\square}}
   a_{\rm end}(h,m)\chi _4(h)e(\sqrt{Xhm})
 \right|^2 .
\]

Its requested bound is

\[
 \mathcal E_L^{\rm ns}\ll_\varepsilon L^2X^\varepsilon.
 \tag{1}
\]

The square-entry estimate does not permit an algebraic subtraction of
energies.  It gives only

\[
 \|A_L\chi _4\|_2
 \leq \|A_L^{\rm ns}\chi _4\|_2
      +\|A_L^\square\chi _4\|_2.
 \tag{2}
\]

Thus (1), together with the supplied
\(\|A_L^\square\chi _4\|_2^2\ll L^{3/2}X^\varepsilon\), would put the
whole block at the desired \(L^2X^\varepsilon\) energy scale.  The
nonsquare diagonal is already at that scale; the problem is the signed
off-diagonal correlation.

The rigorous result of this report is a no-go at the supplied interface.
Under only the displayed support condition and
\(|a_{\rm end}(h,m)|\ll X^\varepsilon\), even the fixed character
\(\chi _4\) and the genuinely joint phase \(e(\sqrt{Xhm})\) admit exact
entrywise phase alignment.  There are admissible arrays with no square
entries, Hilbert--Schmidt energy \(\asymp L^2\), and fixed-direction
energy \(\asymp L^3\).  Consequently the declared coherent capacity
\(L^3X^\varepsilon\) is sharp for the class described in the packet.
No inequality, invertible or noninvertible, can recover the missing
factor \(L\) uniformly from those hypotheses alone.

This is a **method/interface obstruction**, not a physical lower bound
for the literal hard-TOP coefficient array.  The counterexample chooses
adversarial coefficient phases.  Since the packet does not give the
formula or any variation, factorization, reality, or arithmetic
constraint for the actual \(a_{\rm end}\), it is impossible to decide
whether the actual array permits the alignment.  In particular, this
report does not refute (1) for the actual hard-TOP block.

## 2. Exact statement and hypotheses

### Phase-alignment lemma

Let \(M\) and \(H\) be finite, let
\(S\subseteq M\times H\), and write
\(S_m=\{h:(m,h)\in S\}\) and \(q_m=|S_m|\).  Let
\(|c_h|=1\) and let \(\phi_{m,h}\) be arbitrary real phases.  For arrays
\(|a_{m,h}|\leq1\), set

\[
 (T_ac)(m)=\sum_{h\in S_m}a_{m,h}e(\phi_{m,h})c_h.
\]

Then the exact variational identity is

\[
 \sup_{|a_{m,h}|\leq1}\|T_ac\|_2^2
   =\sum_{m\in M}q_m^2.
 \tag{3}
\]

An extremizer is

\[
 a_{m,h}=\overline{c_h}\,e(-\phi_{m,h}).
 \tag{4}
\]

Thus any class of coefficients specified only by support and pointwise
magnitude has worst-case energy equal to the coherent row capacity,
irrespective of how nonlinear or joint the displayed phase is.

### Nonsquare hard-TOP countermodel

For every sufficiently large integer \(N\) and every \(X\geq2\), take

\[
 M_N=\{N,N+1,\ldots,2N-1\},\qquad
 H_N=\{h\in[2N,3N]\cap\mathbb Z:h\text{ is odd}\},
\]

and

\[
 S_N=\{(m,h)\in M_N\times H_N:hm\notin\square\}.
\]

Every pair in the rectangle obeys \(m\leq h\leq4m\).  Define the
zero-extended endpoint array by

\[
 a_{\rm end}(h,m)=
 \begin{cases}
  \chi _4(h)e(-\sqrt{Xhm}),&(m,h)\in S_N,\\
  0,&\text{otherwise}.
 \end{cases}
 \tag{5}
\]

On odd heights \(\chi _4(h)^2=1\), so

\[
 A_N^{\rm ns}(m,h)\chi _4(h)=1_{S_N}(m,h).
 \tag{6}
\]

Moreover \(A_N^\square=0\),

\[
 \|A_N\|_{HS}^2=|S_N|\asymp N^2,
 \qquad
 \|A_N^{\rm ns}\chi _4\|_2^2
   =\sum_{m\in M_N}|(S_N)_m|^2\gg N^3.
 \tag{7}
\]

This family satisfies every explicit mathematical condition in the
statement-only packet, including \(|a_{\rm end}|\leq1\).  Taking
\(L=N\), it rules out a uniform \(O(L^2X^\varepsilon)\) conclusion from
those conditions.  The statement gives no relation between \(L\) and
\(X\), so one may already fix \(X=2\).  If an omitted hard-TOP
definition imposes such a relation or restricts the endpoint array,
that omitted condition is precisely additional structure outside this
no-go's hypotheses.

### Literal target and capacity ledger

| Quantity | Supplied/current capacity | Needed capacity | Exact gap |
|---|---:|---:|---:|
| Nonsquare diagonal \(\mathcal D_L^{\rm ns}\) | \(\leq\mathcal D_L\ll L^2X^\varepsilon\) | \(L^2X^\varepsilon\) | none |
| Square-entry direction | \(L^{3/2}X^\varepsilon\) in energy | lower order than \(L^2X^\varepsilon\) | none, but usable only through (2) |
| Nonsquare coherent direction | \(L^3X^\varepsilon\) | \(L^2X^\varepsilon\) | one factor \(L\) in energy, or \(L^{1/2}\) in norm |

The fixed-direction expansion makes the missing cancellation literal.
With

\[
 S_m^{\rm ns}=\{h\in\mathscr H_L:m\leq h\leq4m, hm\notin\square\},
\]

one has

\[
 \mathcal E_L^{\rm ns}=\mathcal D_L^{\rm ns}+\mathcal C_L^{\rm ns},
 \tag{8}
\]

where

\[
 \mathcal C_L^{\rm ns}
 =\sum_m\!\sum_{\substack{h_1,h_2\in S_m^{\rm ns}\\h_1\ne h_2}}
 a_{\rm end}(h_1,m)\overline{a_{\rm end}(h_2,m)}
 \chi _4(h_1)\overline{\chi _4(h_2)}
 e\!\left(\sqrt{Xm}(\sqrt{h_1}-\sqrt{h_2})\right).
 \tag{9}
\]

Therefore a sufficient literal inequality is
\(\mathcal C_L^{\rm ns}\ll L^2X^\varepsilon\) (and an absolute bound
for (9) would be stronger).  But (9) is the correlation to be proved,
not a new estimate.  The phase-alignment lemma shows that support and
coefficient magnitudes alone allow (9) to have size \(\asymp L^3\).

## 3. Proof and derivation

First, (2) follows from
\(A_L=A_L^{\rm ns}+A_L^\square\) and the norm triangle.  Squaring (2)
is harmless, but replacing it by an equality of the two sector energies
would omit their output cross term and is not justified.

Second, expanding the nonsquare norm gives (8)--(9).  The terms with
\(h_1=h_2\) are exactly

\[
 \mathcal D_L^{\rm ns}
 =\sum_m\sum_{h\in S_m^{\rm ns}}|a_{\rm end}(h,m)|^2,
\]

because the exponential and \(\chi _4\) both have unit modulus on odd
heights.  All possible saving beyond Hilbert--Schmidt energy must occur
in the signed off-diagonal sum (9), before an outside absolute value or
norm destroys it.

Third, for the upper half of (3), the triangle inequality gives, row by
row,

\[
 |(T_ac)(m)|\leq\sum_{h\in S_m}|a_{m,h}|\leq q_m.
\]

Summing squares proves \(\|T_ac\|_2^2\leq\sum_mq_m^2\).  The choice
(4) makes every summand in every row equal to one, so equality holds.
This also proves that multiplication by the fixed height character
cannot itself yield a uniform signed gain: the allowed coefficient
class is invariant under the inverse column phases
\(a_{m,h}\mapsto a_{m,h}\overline{\chi _4(h)}\).  Entrywise phases also
absorb the joint oscillation, so merely retaining the joint phase in
notation is insufficient.

### Joint product-shear/averaging test

It is useful to test the most natural genuinely joint noninvertible
operation explicitly.  Put

\[
 F(m,h)=1_{S^{\rm ns}}(m,h)a_{\rm end}(h,m)\chi _4(h)
        e(\sqrt{Xhm}),
 \qquad (RF)(m)=\sum_hF(m,h).
 \tag{10}
\]

Thus the desired energy is \(\|RF\|_2^2\).  Let \(\sigma_j\) be joint
input-output shears of the entry set, so
\(\sigma_j(m,h)=(m',h')\), with \(m'h'=mh\).  Each pullback
\(U_{\sigma_j}F=F\circ\sigma_j\) is unitary on its finite permutation
domain, but the genuine average

\[
 P=\sum_j\theta_jU_{\sigma_j},\qquad
 \theta_j\geq0,\quad\sum_j\theta_j=1,
 \tag{11}
\]

is an \(\ell^2\)-contraction and is noninvertible whenever it collapses
a nontrivial product fibre.  Its invariant space contains

\[
 \mathcal V_{\rm prod}
 =\{F:F(m,h)=f(mh)\text{ on every connected product-fibre component}\}.
 \tag{12}
\]

In particular \(F\equiv1\) is fixed.  But (5) gives exactly
\(F=1_{S_N}\), and \(RF(m)=q_m\), whose energy is \(\asymp N^3\).
Consequently exact product-fibre averaging produces no contraction on
the coherent direction.  The complementary shear difference
\((I-P)F\) is even less useful: it vanishes on (12), while \(RF\) need
not vanish.  Hence no Poincare inequality controlling \(RF\) solely by
product-shear differences can hold.

The same invariant can be written before absorbing the character.  For
an arbitrary unit-modulus fixed direction \(c_h\), the character-aware
shear is conjugate to (11) by \(G\mapsto(c_hG(m,h))\); its invariant
fibre is

\[
 \mathcal V_c=\{G:G(m,h)=\overline{c_h}f(mh)\}.
 \tag{13}
\]

Thus the obstruction handles arbitrary aligned vectors, not just the
constant direction.  For \(c=\chi _4\), it is the twisted fibre
\(G(m,h)=\chi _4(h)f(mh)\).

Allowing a positive near-product kernel rather than exact shears does
not remove the obstruction: every unital averaging kernel still fixes
the global constant \(F\equiv1\).  Giving the kernel total mass less
than one contracts constants, but then it cannot be a literal lossless
interface for \(R\).  More generally, if an \(\ell^2\)-contraction
\(P\) satisfies the exact pre-norm interface \(R=RP\), and \(F_0\) is
an aligned right singular vector with
\(\|RF_0\|=\|R\|\|F_0\|\), then

\[
 \|R\|\|F_0\|=\|RPF_0\|
 \leq\|R\|\|PF_0\|
 \leq\|R\|\|F_0\|.
 \tag{14}
\]

All inequalities are equalities, so \(P\) cannot strictly contract that
aligned vector.  If instead a high-pass or sub-unital map discards it,
the discarded fibre mean must be restored as a remainder; (7) shows
that remainder has the full coherent capacity.  The precise failure
space is therefore the product-fibre mean (12), or its character-twisted
version (13), with singleton product-fibre components as an additional
degenerate case.  This is not a unitary-equivalence objection: (11) is
genuinely noninvertible, yet its fixed space carries the bad energy.

Fourth, it remains to verify (7).  Write any fixed
\(m=d r^2\), where \(d\) is squarefree.  Then

\[
 hm\in\square\quad\Longleftrightarrow\quad h=d s^2
\]

for an integer \(s\).  Hence the number of square-product heights in
\([2N,3N]\) is at most

\[
 (\sqrt3-\sqrt2)\sqrt{N/d}+2\leq
 (\sqrt3-\sqrt2)\sqrt N+2.
\]

There are at least \((N-1)/2\) odd integers in that interval.  Thus,
uniformly in \(m\in M_N\),

\[
 |(S_N)_m|\geq N/3

\]

for all sufficiently large \(N\).  There are \(N\) rows, giving

\[
 |S_N|\geq N^2/3,
 \qquad
 \sum_{m\in M_N}|(S_N)_m|^2\geq N^3/9.
\]

The reverse estimates \(|S_N|\ll N^2\) and
\(\sum_m|(S_N)_m|^2\ll N^3\) are immediate from the rectangle sizes.
Equations (5)--(6) now prove (7).  Notice that all exact square products,
including fourth-power subfamilies, were deleted before alignment.  The
obstruction is therefore genuinely nonsquare.

Finally, the conclusion applies to any proposed noninvertible estimate
whose hypotheses and proved capacity use only the displayed support,
the phase, and pointwise coefficient magnitudes.  Such an estimate must
also hold for (5), and hence its right-hand capacity cannot be
\(O(N^2)\).  A viable noninvertible estimate must use a concrete property
of the *actual* endpoint array which is not invariant under the
entrywise phase twist (5), and it must control the component discarded
by the noninvertible operation.  Neither ingredient is present in the
permitted statement.

## 4. First doubtful or unproved step

There is no doubtful step in the phase-alignment lemma or its explicit
countermodel under the hypotheses stated in Section 2.  The first
unproved seam in transferring this obstruction analysis to the actual
hard-TOP problem is earlier than any exponential-sum estimate: it is the
missing literal formula and structural hypotheses for
\(a_{\rm end}(h,m)\).

In particular, the packet does not say whether the actual coefficient
is real, has bounded variation on each affine profile, factors into
one-variable pieces, has bounded profile rank, is independent of the
oscillatory phase, or obeys a relation tying its mod-4 behavior to the
hard faces.  Without at least one such proved property, differencing in
\(m\) or \(h\) creates uncontrolled differences of \(a_{\rm end}\), and
the joint phase may be cancelled exactly as in (5).  Claiming that the
literal endpoint coefficient “does not look adversarial” would be the
first doubtful step.

The precise seam a future proposal must close is therefore:

> Exhibit an exact identity or regularity lemma for every literal
> floor/ceiling/star/profile piece of the actual \(a_{\rm end}\) which
> fails for (5), and use that property in a joint, noninvertible
> inequality whose discarded remainder is bounded at
> \(L^2X^\varepsilon\) capacity.

Until that is done, (9) cannot be bounded by appealing only to the
curvature of \(\sqrt{mh}\) or to the fixed signs \(\chi _4(h)\).

## 5. Control tests and outcomes

### `literal_three_frontier_statements`

Only the literal information in the task brief was used.

| Frontier | Literal target and present capacity | Literal proof payoff/limitation |
|---|---|---|
| Hard TOP | \(\mathcal E_L^{\rm ns}\ll L^2X^\varepsilon\), versus coherent \(L^3X^\varepsilon\), after the square-entry sector is handled only by (2) | Completion still leaves BAL and UNBAL, and does not remove the mandatory M9--M2 bridge |
| Lower GAR | Exact medium-index, low-two-adic cumulative wavelet \(\ll RX^\varepsilon\), versus \(O(R^2)\) absolute capacity | Would close the alternative total-M1 analytic parent, but not M9--M2 |
| Graded determinant | Literal \(W=Y^{7/16}\) signed nonzero determinant correlation \(\ll Y^{1/2+\varepsilon}\); complete bound \(Y^{37/48+\varepsilon}\), bounded-lift top shell \(Y^{35/48+\varepsilon}\) | Target gives the internal exponent \(5/16\), not M9 or the quarter theorem; a partial saving needs exact propagation |

No estimate for one frontier was transferred to another.

### `capacity_and_missing_power_table`

The capacity table in Section 2 was checked at both energy and norm
level.  The required improvement is exactly \(L\) in energy, equivalently
\(L^{1/2}\) in norm.  The countermodel has
\(\mathcal D_N^{\rm ns}\asymp N^2\) and
\(\mathcal E_N^{\rm ns}\asymp N^3\), so it realizes the whole missing
power.  There is no hidden credit from the square estimate because the
countermodel has \(A_N^\square=0\).

### `noninvertible_mechanism_test`

Input: an arbitrary proposed inequality derived uniformly from the
support envelope, the displayed joint phase, \(|a_{\rm end}|\), and a
noninvertible projection or averaging map.

Outcome: failed for that level of generality.  If the map retains the
aligned rectangle (5), its capacity is \(\gg L^3\).  If it discards that
rectangle, a literal domination of \(\|A^{\rm ns}\chi _4\|_2\) must
include a remainder which is itself \(\gg L^{3/2}\) in norm on (5).
Therefore noninvertibility by itself is not the gain.  The map must be
coupled to a proved, actual-coefficient property that excludes (5).
The explicit joint product-shear test (10)--(14) reaches the same
conclusion for a noninvertible conditional expectation: exact fibre
means \(F=f(mh)\), and in particular \(F\equiv1\), are invariant and
carry coherent output energy.  A near-product unital averaging still
fixes constants; a high-pass averaging kills them and therefore needs a
full-capacity remainder.  The failing subspace is the character-twisted
product-fibre space (13), not merely a height-only or unitary image.

### `actual_vs_adversarial_coefficients`

The four sign variants separate cleanly.

* Adversarial phases of the allowed magnitude give (5) and energy
  \(\asymp L^3\).
* Taking absolute values of the aligned summands also gives
  \(\asymp L^3\).
* Independent random signs would have expected energy at the diagonal
  scale \(\asymp L^2\), but this is only a heuristic and provides no
  credit for the fixed direction.
* The true \(\chi _4\) direction is already used in (5), and still gives
  \(\asymp L^3\) for the adversarial endpoint array.  For the actual
  endpoint array its behavior is undecidable from the permitted formula
  \(|a_{\rm end}|\ll X^\varepsilon\).

Thus the obstruction defeats coefficient-blind bounds.  It is not a
lower bound for the actual coefficients.  If the actual coefficients
are, for example, constrained to be real, that would be relevant new
input; reality is not among the stated hypotheses.

### `endpoint_floor_star_and_support_scope`

The countermodel lies strictly inside the explicit outer support faces:
\(m< h\) and \(h<4m\) with macroscopic room.  Hence the simple moving
faces \(m\leq h\leq4m\) do not prevent alignment.  The array is
zero-extended, and all \(hm\in\square\) pairs (including fourth-power
cases) are absent.  Pell-type or other near resonances cannot rescue a
coefficient-uniform theorem, because (5) cancels the complete phase
without using resonance.

The literal internal affine faces, floor/ceiling values, star
conditions, profile tags, reduced-lift boundaries, and the relation of
\(L\) to the dyadic endpoints \(D=X^{1/4},X^{3/8},X^{1/2}\) are not
specified in the permitted statement.  They therefore cannot be
audited here.  The countermodel is a lower bound for the displayed
model class, while the absence of those data is a method/interface
obstruction only.  Any actual theorem must check each endpoint and star
piece separately rather than infer it from the interior model.

### Aligned-vector and resonance controls

The arbitrary aligned-vector control is stronger than a test at
\(\chi _4\): formula (3) works for every unit-modulus vector \(c_h\).
The square, fourth-power, and exact-resonance controls were removed at
the entry level.  Near-resonance spacing was not invoked.  Consequently
the no-go does not confuse an arithmetic physical lower-bound family
with coefficient phase alignment.

### `finite_stop_rule`

Give the hard-TOP route one further, bounded interface attempt only if
the exact actual endpoint formula is made available.  That attempt must
meet all three gates:

1. list every literal face/star/profile piece and prove a structural
   property not invariant under the phase twist (5);
2. state a joint non-height-only, noninvertible inequality with an
   explicit controlled remainder and show exactly where the adversarial
   array fails its hypotheses;
3. derive an \(L^2X^\varepsilon\) capacity on all support and endpoint
   pieces, with square/Pell/fourth-power and aligned-vector controls.

If Gate 1 or Gate 2 is absent, or if Gate 3 merely renames (9), after
that single attempt the hard-TOP interface should be stopped rather
than cycled through another transform or norm.  This is a finite
selection rule, not a claim that the actual estimate is false.

### `no_proof_status_from_strategy_only`

The proved content is only the conditional no-go for the coefficient
class explicitly described in Section 2.  The comparative ranking below
is strategy evidence.  It proves none of the three frontier estimates,
changes no proof status, and authorizes no proof-graph update.

## 6. Dependencies and exact artifacts used

The report used only:

1. `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/briefs/blind_hard_top_nonsquare_feasibility.md` for the assigned question,
   controls, and the literal comparison of the three frontiers;
2. `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/blind_statement.md` for the hard-TOP operator, capacities, square-sector
   estimate, admissibility exclusions, and requested stress tests;
3. `state/control_models.md` for the meanings of the adversarial,
   signed/unsigned, endpoint, resonance, and support controls;
4. `problems/gauss_circle.md` for the ambient problem and the repository's
   non-claim research goal.

No strategy file, proof-state file, Round-75--127 nonblind artifact,
sibling report, web source, or numerical experiment was used.  The
derivation is entirely algebraic.

## 7. Recommended state effect

**Recommended effect: retain the phase-alignment no-go as candidate
evidence; revise the hard-TOP interface; do not promote (1), and make no
proof-graph change.**  At its present statement-only interface, hard TOP
is ineligible for selection because the actual coefficient property
needed to beat the sharp \(L^3\) model capacity is not stated.

A statement-only feasibility ranking is:

1. **Graded determinant, provisional first.**  It is the only packet
   option with quantified complete and top-shell signed bounds already
   stated, so it offers a finite exponent-propagation question.  Its
   proof payoff remains only the internal \(5/16\) exponent.
2. **Lower GAR, provisional second.**  Its graph payoff is stronger than
   the graded payoff, but the packet supplies only the target and the
   full missing factor \(R\), not a literal signed mechanism.
3. **Hard TOP, stop at the current interface.**  It has the exact
   coefficient-phase invariance obstruction above, needs the full factor
   \(L\), and completion alone would still leave BAL, UNBAL, and the
   mandatory M9--M2 bridge.

The order of the first two is necessarily provisional because their
full literal formulas were outside this task's permitted context.  The
rigorous conclusion of this report is only that the supplied hard-TOP
interface cannot support the desired inequality without new,
actual-coefficient structure.
