# Source audit of the Round 148 conductor candidate

## 1. Result and terminal assessment

**Result: AMBER, with local but mandatory repairs.** The candidate's
central mathematics agrees with the three Round-148 reports:

- the conductor-four Poisson factor and stationary normalization are
  correct;
- the true transformed support is \(q\asymp\ell Q\), with
  \(Q=2\sqrt{ND/E}\);
- the coefficient-separated positive-diagonal method loses exactly a
  factor \(R\), and the candidate correctly confines that no-go to this
  placement;
- the small reduced-denominator stratum is target-safe;
- the published progression, trace-function, and Kloosterman-fraction
  theorems do not match the hard signed form;
- there is no termwise map \(\ell\mapsto k\) to the Round-147 powerful
  \(H\)-index; and
- all owner and downstream exclusions are correctly retained.

The candidate is not GREEN as written for two concrete reasons. First,
(148.C4) omits the necessary finite support
\(\alpha^2\ll E\). The displayed weight depends only on
\((d,e_0)\), so it does not kill arbitrarily large \(\alpha\):
for every large \(\ell=[\alpha^2,b]\), values
\(q\asymp\ell Q\) still give \(e_0\asymp E\). Thus the statement that
the sum is finite through \(\mathscr W\) is false unless the original
divisibility support is explicitly retained. The discovery report uses
\(\alpha\leq\sqrt E\) in every subsequent mass calculation, and the
source audit correctly includes \(u^2\ll E\); the conductor formula
must do the same.

Second, the candidate contains six bare carriage-return bytes and one
horizontal-tab byte that corrupt \({\rm odd}\), \(\rho_i\), and
\(\theta\). This is not merely cosmetic in an authoritative formula:
(148.C1), (148.C4), (148.C9), (148.C21), and the source-range statement
do not render literally as intended.

After those repairs, plus the source-card and power-ledger
clarifications stated below, the exact transform reduction and the
scoped method obstruction are suitable for promotion.

## 2. Exact statement and hypotheses audited

The corrected transform statement must read
$$
\begin{aligned}
\mathcal T_{D,E,U}={}&
\sum_d\mu^2(d)\frac Dd
\sum_{\substack{\alpha^2\ll E\\\alpha\ {\rm odd}}}\mu(\alpha)
\sum_{\substack{b\mid d\\b\ {\rm odd}}}\mu(b)
\frac{\chi_4(\ell)}{\ell}\\
&\times
\sum_{\substack{q>0\\q\ {\rm odd}}}
\chi_4(q)\mathscr W_{d,\ell,U}(q)
e\!\left(\frac{Nd\ell}{q}\right),
\qquad \ell=[\alpha^2,b].
\end{aligned}
\tag{R148.1}
$$
Here \(\alpha^2\ll E\) is not an analytic truncation. It is the exact
finite support inherited from \(\alpha^2\mid e\) and
\(e\asymp E\). With (R148.1), all later uses of
\(\alpha\leq\sqrt E\), including (148.C18)--(148.C22), become
consistent with the main formula.

The two modulus coordinates in the candidate are both valid but must
be related explicitly. If
$$
g=(\ell,q),\qquad L=\ell/g,\qquad q_0=q/g,
$$
then
$$
e(Nd\ell/q)=e(NLd/q_0),\qquad (L,q_0)=1,
$$
and the nearest-integer coordinate is
$$
j=NL-Aq_0,\qquad |j|<q_0/2,\qquad q_0\mid NL-j.
\tag{R148.2}
$$
The fully reduced additive denominator used in the source audit is
$$
q_*=\frac q{(q,\ell N)}
=\frac{q_0}{(q_0,N)}.
\tag{R148.3}
$$
Adding the second equality prevents the candidate's \(q_0\) and
\(q_*\) discussions from appearing to be competing reductions. The
bare \(j=N-Aq\) formula applies literally to the unexpanded
\(\ell=1\) cell; on a general \(L=1\) lift it is
\(j=N-Aq_0\), not \(j=N-Aq\) with the original unreduced \(q\).

All other hypotheses are retained correctly: \(e\) is odd, \(d\) may
be even, \(b\) is therefore an odd divisor of \(d\),
\(\mu^2(d)\mu(\alpha)\mu(b)\) remains signed,
\(e_0>4d\) is kept through the cone profile, every product prefix is
kept after an owned collar, the physical direction is \(+\), and
\(N=\lfloor X\rfloor\) is fixed.

## 3. Verification of normalization, counts, powers, diagonal scope, and interfaces

**Transform normalization.** Equations (148.C9)--(148.C12) are
correct. With the convention
\(\widehat F(\xi)=\int F(x)e(-\xi x)\,dx\),
\(\tau(\chi_4)=2i\) gives the factor \(i/2\). For
$$
\phi(x)=\sqrt{Nd\ell x}-qx/4
$$
the positive saddle is
$$
x_0=\frac{4Nd\ell}{q^2},\quad
e_0=\frac{4Nd\ell^2}{q^2},\quad
\phi(x_0)=\frac{Nd\ell}{q}.
$$
The substitution \(x=x_0(1+u)^2\) gives
\(\phi=\lambda(1-u^2)\), \(\lambda=Nd\ell/q\). The leading integral is
$$
\frac{2e(\lambda-1/8)}{N^{1/4}d\ell}
\mathscr A(d,e_0).
$$
Multiplication by \(i/2\) gives
$$
\frac{e(1/8)}{N^{1/4}d\ell}
e(Nd\ell/q),
$$
so (148.C3)--(148.C6), including the sign, the factor
\(1/\ell\), and the target \(N^{1/4}D\asymp RD\), are correct.
The literal saddle support is
$$
q=2\ell\sqrt{Nd/e_0}\asymp\ell Q,\qquad
Q=2\sqrt{ND/E}.
$$
The lower-symbol ratios in (148.C14) are also correct:
$$
\frac1{R\sqrt E},\qquad \frac{\sqrt D}{R},\qquad \frac1R.
$$

**Small-\(q_*\) stratum.** For fixed \(\ell\), writing
\(q=hr\), \(h\mid\ell N\), shows
$$
\#\{q:q_*\leq Y\}\leq Y\tau(\ell N).
$$
Moreover
$$
\sum_{\alpha^2\ll E}\sum_{b\mid d}
\frac{|\mu(\alpha)\mu(b)|}{[\alpha^2,b]}
\ll X^\varepsilon.
$$
Thus (148.C25),
$$
\mathcal T(q_*\leq Y)\ll DY X^\varepsilon,
$$
is correct and is target-safe for every \(Y\leq R\). This includes
\(Y=D\), since \(D\leq R\).

**Primary-source distinction.** The conclusion of (148.C24)--(148.C26)
is correct, but its prose must distinguish the theorem classes
literally:

- Nunes, Squarefree numbers in large arithmetic progressions,
  Theorem 1.1: prime modulus, \(q_*\leq D^{13/19-\varepsilon}\);
- Nunes, A note on the least squarefree number in an arithmetic
  progression, Theorem 1.1: squarefree modulus,
  \(q_*\leq D^{25/36-\varepsilon}\);
- Mangerel, Theorem 1.1: squarefree \(D^\eta\)-smooth modulus,
  \(q_*\leq D^{196/261-\varepsilon}\);
- Nunes, Squarefree numbers in arithmetic progressions,
  Theorems 1.1--1.2: \(q_*\leq D\), but a fixed-modulus average over
  reduced residue classes with a genuine diagonal main term, not a
  pointwise signed estimate; and
- Schlage-Puchta, Theorem 3: no special modulus family, but only the
  pointwise bound \(D^{1+\varepsilon}/q_*+q_*D^\varepsilon\).

The candidate's sentence that the audited progression theorems all
require \(\theta<1\) and special modulus families is therefore not
literal for the Nunes variance theorem. The conclusion still holds:
its \(q_*\leq D\) range is already covered by the elementary
\(DY\)-bound, and its averaging and diagonal are wrong for (R148.1).
Nunes Theorems 1.2--1.3 and Mangerel Theorem 3.1 remain fixed-prime
inverse-square trace-function results; Mangerel explicitly excludes
the balanced diagonal. Bettin--Chandee Theorems 1--2 have inverse
phase \(e(\vartheta a\bar m/n)\). None is directly applicable.

**Complete power ledger.** Every numerical power asserted in the
candidate is correct. For clarity, the candidate should place the
following distinct quantities in one table rather than allowing three
different triangles to be conflated:

| Placement | Capacity relative to \(RD\) |
|---|---:|
| bare \(Q+D\) | \(R/\sqrt M+1/R\) |
| expand \(\mu^2(d)\), then use the bare lemma termwise | \(R\sqrt D/\sqrt M+1/R=R/\sqrt E+1/R\) |
| take full absolute mass of the \(e\)-progression cells | \(R\sqrt D\) |
| progression-cell Cauchy with separately majorized \(d\)-diagonal | \(R\) |
| Round-147 \(H\)-menu | \(M^{1/4}\) below \(R^{4/3}\), and \(R^{1/2}M^{-1/8}\) above |

Thus the bare term loses \(R^{1/3}\) at \(M=R^{4/3}\), the
Round-147 menu loses \(R^{1/3}\) there and \(R^{1/4}\) at
\(M=R^2\), the full progression absolute mass loses \(R\sqrt D\),
and the scoped positive diagonal loses exactly \(R\). These are upper
capacities, never lower bounds.

**Scope of the diagonal no-go.** Equations (148.C18)--(148.C22) are
correct after inserting \(\alpha^2\ll E\). On
\(\alpha\asymp A\),
$$
\sum|c_i|^2\asymp Q/A,\qquad
\sum|c_i|\asymp QA,
$$
and hence \(\mathscr L\asymp Q\sqrt E\). For any positive Cauchy
weights, separately majorizing the \(d\)-diagonal gives at least
$$
\sqrt D\,\mathscr L
\asymp Q\sqrt{DE}
\asymp \sqrt N\,D
=R(RD).
$$
The candidate correctly says this is not the diagonal of every
possible signed joint energy and not a lower bound for
\(\mathcal T\). No scope repair is needed.

**\(H\)-interface and owners.** The statement that
\(\ell=[\alpha^2,b]\) need not be powerful, whereas the Round-147
\(k\) is a powerful Euler-convolution index, is correct. Replace
"globally equivalent presentations" by the more exact statement:
the complete identity (148.C3), including lower symbols, collars, and
remainders, and the complete Round-147 identity reconstruct the same
physical box after all inverse transforms and Euler recombination;
\(\mathcal T\) in (148.C4) alone is not termwise or independently
identical to the \(H\)-correlation. The downstream exclusions in
Section 6 and Section 7 are complete and correct.

## 4. First doubtful or unproved step

After the finite-support repair, the transform normalization and its
target-safe analytic remainder are not the first open seam. The first
unproved step is exactly the one stated by the candidate: a
coefficient-sensitive signed estimate for (R148.1) that keeps the
\((\alpha,b,q)\) cells together before forming a separately positive
progression diagonal, including nonzero
$$
j=NL-Aq_0,
$$
imprimitive lifts, common-divisor strata, aligned fibres, the actual
\(\chi_4(q)\mathscr W(q)\), and every prefix.

Equivalently, one may first perform the exact Euler recombination and
then prove the Round-147 signed \(H\)-correlation. None of the three
reports or audited primary sources proves either statement. The
absolute squarefree \(Q+D\) assertion remains open, and the
arbitrary-\(q\)-coefficient falsifier cannot be transferred to the
actual signed coefficient.

## 5. Required repairs and control outcomes

1. **Finite support -- mandatory.** In (148.C4), (148.C8)--(148.C10),
   and every subsequent \(\alpha\)-sum, insert
   \(\alpha^2\ll E\) (with the precise constant inherited from the
   support of \(\omega_E\)). Delete the claim that
   \(\mathscr W(d,e_0)\) alone makes the \(\alpha\)-sum finite.

2. **Byte and TeX repair -- mandatory.** Replace the six bare carriage
   returns by the intended sequences: five occurrences are
   \({\rm odd}\) in (148.C1), (148.C4), and (148.C9), and one is
   \(\rho_i\) near (148.C21). Replace the horizontal tab before
   "heta" by \(\theta\) in the source-range paragraph. Re-run a
   control-character scan and require zero bare CR, tab, backspace, or
   other C0 bytes.

3. **Modulus notation -- mandatory.** Add
   \(q_*=q_0/(q_0,N)\) after (148.C24), and state that the \(L=1\)
   relation uses \(q_0\) unless \(\ell=1\).

4. **Source cards -- mandatory.** Separate the three pointwise
   subunit-range progression theorems from Nunes's
   \(q_*\leq D\) variance theorem, and name the theorem numbers and
   fixed-modulus residue average. Keep Schlage-Puchta Theorem 3
   separate from progression asymptotics.

5. **Power presentation -- required clarification.** Add the five-row
   ledger from Section 3 so that \(R/\sqrt E\),
   \(R\sqrt D\), and \(R\) are visibly attached to different
   placements. The existing powers themselves need no correction.

6. **Diagonal scope -- pass.** Retain verbatim the qualification
   following (148.C22): the obstruction concerns early
   progression-cell Cauchy followed by a separately majorized positive
   diagonal.

7. **False analogues -- pass.** The \(D=1\) arbitrary-coefficient
   alignment is correctly scoped, and the absolute squarefree
   \(Q+D\) analogue is correctly left unresolved.

8. **\(H\)-interface -- pass after wording repair.** Retain the
   non-powerful-\(\ell\) mismatch and self-return statement; qualify
   global equivalence as described above.

9. **Owner/downstream scope -- pass.** The Round-138 cross,
   \(t\geq2\), lower GAR, M9--M1, M9--M2, endpoint uniformity, M9,
   bridge, quarter target, and global exponent remain excluded.

## 6. Dependencies and artifacts used

This review checked the complete conductor candidate against:

- reports/signed_squarefree_reciprocal_attack.md;
- reports/blind_squarefree_reciprocal_feasibility.md;
- reports/squarefree_progression_source_audit.md;
- strategy/round148_squarefree_reciprocal_dispersion_strategy.md;
- the Round-148 barrier packet; and
- the Round-147 candidate, source audit, adjudication, and synthesis
  selected by state/active_campaign.yml.

The primary-source cards used for the source seam are the cited works
of Schlage-Puchta (Theorem 3), Nunes (the two progression papers, the
variance paper, and their theorem numbers recorded above), Mangerel
(Theorems 1.1 and 3.1), and Bettin--Chandee (Theorems 1--2). No
numerical experiment was used, and no candidate or shared-state file
was edited.

## 7. Recommended state effect and verdict

Do not promote the candidate in its current byte form. After the
finite-\(\alpha\)-support, control-character, modulus-notation,
source-card, power-ledger, and \(H\)-wording repairs, promote:

1. the exact \(t=1\) reciprocal-transform reduction, including all
   collars, lower symbols, remainders, and the corrected finite signed
   kernel; and
2. the factor-\(R\) obstruction expressly limited to
   progression-separated Cauchy methods that majorize the positive
   diagonal separately, together with the audited source mismatch.

Retain the signed target, every strict range, all downstream owners, and
every exponent claim as open.

**AMBER**
