# Round 148 transform and diagonal seam review

Campaign: `m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate`
Reviewed report: `reports/signed_squarefree_reciprocal_attack.md`
Role: hostile seam review

## 1. Result

**Verdict: AMBER.**  The arithmetic identities (148.14)--(148.16),
the character-Poisson constant in (148.17), and the leading saddle
unit, phase, amplitude, and base support in (148.19)--(148.25) are
correct.  The scale calculation behind the progression-cell diagonal
barrier is also correct for the explicitly scoped method: weighted
Cauchy over the unrecombined \((\alpha,b,q)\) cells followed by a
separate nonnegative majorant for the \(d\)-diagonal.

The report is not yet exact enough for promotion for three reasons.

1. Formula (148.3) omits the finite square-divisor/progression range
   inherited before Poisson.  As \(\mathscr W\) is defined in (148.13),
   it does not cut off \(\alpha\): for \(b=1\), every arbitrarily large
   \(\alpha\) has \(\ell=\alpha^2\) and has \(\asymp\alpha^2Q\)
   possible saddle frequencies.  Thus the assertion that all sums in
   (148.3) are finite through the displayed weight is false as written.
   The original divisor expansion supplies an explicit
   \(\alpha^2\leq e_+\ll E\) bound, and empty \(e=\ell n\)
   progressions may be omitted before Poisson.  Those restrictions must
   appear in the displayed exact transform.

2. The leading Gaussian constant is right, but (148.23) is not a
   literal equality under the stated description of
   \(\mathcal I_{\rm ns}\) as the "unchanged complementary integral."
   Replacing a cutoff Gaussian moment by its full-line moment introduces
   the complementary Taylor-polynomial subtraction.  That subtraction,
   the lower-domain tail, and an even localization convention must be
   included in the defined nonstationary remainder.  The later claim
   that the aggregate exact Taylor and nonstationary remainders is
   \(O(X^\varepsilon)\) is asserted but not proved with a quantitative
   \(q\)-partition and derivative ledger.

3. The diagonal result is valid only in its cellwise, positive-ledger
   scope.  It is not independent of an arbitrary "completion order."
   Regrouping equal or correlated frequencies, retaining signed
   cross-cell terms, or taking Cauchy after summing the cells changes
   the quadratic form.  Moreover primitive equality of \(\ell/q\)
   rules out only literal rational duplicates; equality of the
   \(d\)-phases is governed by
   \(N(\ell_1/q_1-\ell_2/q_2)\in\mathbb Z\), so additional
   \(N\)-dependent aligned fibres are not excluded by primitive gcd
   reduction.  They belong to the cross-cell seam and must be expressly
   outside the no-go.

These are repairable defects.  They do not reverse the leading
constant or the narrow diagonal calculation, and they do not establish
the signed target.

## 2. Exact statement and hypotheses of the reviewed result

Let the smoothed retained physical support for fixed \(d\) be contained
in \(0<e\leq e_+\), where \(e_+\ll E\), and define

$$
 \mathcal P(d):=
 \left\{(\alpha,b):
 \begin{array}{l}
 \alpha,b\text{ odd},\quad \mu(\alpha)\mu(b)\ne0,\quad b\mid d,\\
 \alpha^2\le e_+,\quad
 \{n\ge1:\mathscr A_{D,E,U}(d,[\alpha^2,b]n)\ne0\}\ne\varnothing
 \end{array}
 \right\}.                                                    \tag{R148.1}
$$

The last condition may be replaced by an equivalent exact finite
progression convention; it is included here to avoid applying Poisson
to a progression which was empty in the original finite divisor sum.
Put \(\ell=[\alpha^2,b]\).  The exact character-Poisson identity is

$$
 \begin{aligned}
 \mathcal S^{\rm ret}_{D,E,U}
  =\frac i2\sum_d\mu^2(d)
   \sum_{(\alpha,b)\in\mathcal P(d)}
   \mu(\alpha)\mu(b)\chi_4(\ell)
   \sum_{\substack{q\in\mathbb Z\\q\ {\rm odd}}}
   \chi_4(q) I_{d,\ell,q},                                  \tag{R148.2}
 \end{aligned}
$$

with \(I_{d,\ell,q}\) as in (148.18).  This finite outer indexing is
the missing hypothesis in (148.3).

For \(q>0\), let

$$
 x_0=\frac{4Nd\ell}{q^2},\quad e_0=\ell x_0,
 \quad\lambda=\frac{Nd\ell}{q}.
$$

On a retained saddle, the reviewed leading term is exactly

$$
 \frac i2\chi_4(\ell)\chi_4(q) I_{d,\ell,q}^{(0)}
 =\frac{e(1/8)}{N^{1/4}d\ell}
   \chi_4(\ell)\chi_4(q)
   \mathscr A_{D,E,U}(d,e_0)e(\lambda).                     \tag{R148.3}
$$

Its support is

$$
 q=2\ell\sqrt{Nd/e_0}\asymp\ell Q,qquad
 Q=2\sqrt{ND/E},qquad \lambda\asymp\sqrt{NM}.             \tag{R148.4}
$$

The exact progression-cell no-go which the report actually proves can
be stated as follows.  On a fixed interior \(b=1\) plateau, let
\(i=(\alpha,q)\), \(c_i=\mu(\alpha)\chi_4(q)/\alpha^2\), and
let \(S_i=\sum_{d\in\mathcal J}a_{i,d}\) for a common interval
\(|\mathcal J|\asymp D\) on which

$$
 \sum_{d\in\mathcal J}|a_{i,d}|^2\ge c_0D                 \tag{R148.5}
$$

uniformly in the selected cells.  Suppose one applies weighted Cauchy
in these individual cells and then replaces the \(d_1=d_2\) portion of
each \(|S_i|^2\) by a separate nonnegative majorant.  For every
\(\rho_i>0\), that majorant has square at least

$$
 c_0D
 \left(\sum_i|c_i|\rho_i\right)
 \left(\sum_i|c_i|\rho_i^{-1}\right)
 \ge c_0D\left(\sum_i|c_i|\right)^2.                        \tag{R148.6}
$$

For the cells in (148.34a),
\(\sum_i|c_i|\asymp Q\sqrt E\), so the resulting capacity is

$$
 \gg \sqrt D\,Q\sqrt E=Q\sqrt M=\sqrt N\,D,                \tag{R148.7}
$$

a factor \(R\) above \(N^{1/4}D\).  Statement (R148.6) makes no
claim about a method which recombines cells or uses signed off-diagonal
terms before this positive majorization.

## 3. Proof and seam derivation

### 3.1 Squarefree and coprime expansion

For all positive integers \(d,e\),

$$
 \mu^2(de)=\mu^2(d)\mu^2(e)\mathbf1_{(d,e)=1}.              \tag{R148.8}
$$

Also

$$
 \mu^2(e)\mathbf1_{(d,e)=1}
 =\left(\sum_{\alpha^2\mid e}\mu(\alpha)\right)
  \left(\sum_{b\mid(d,e)}\mu(b)\right),                   \tag{R148.9}
$$

which is (148.15).  Since \(e\) is odd, every contributing
\(\alpha,b\) is odd.  Moving \(b\mid d\) outside, putting
\(\ell=[\alpha^2,b]\), and writing \(e=\ell n\) is exact; then
\(\chi_4(e)=\chi_4(\ell)\chi_4(n)\).  Likewise (148.16) is the
exact identity \(\mu^2(d)=\sum_{\gamma^2\mid d}\mu(\gamma)\).
No squarefree or coprime sign is lost in these steps.

The finite range is part of the same interchange.  Before Poisson,
\(\alpha^2\mid e\) and \(e\le e_+\) force
\(\alpha^2\le e_+\).  By contrast, (148.13) evaluates a continuous
amplitude at \(e_0\) and has no dependence capable of enforcing that
divisor bound.  Indeed, with \(b=1\) and \(\ell=\alpha^2\), for every
large \(\alpha\) the interval \(q\asymp\alpha^2Q\) makes
\(e_0\asymp E\), so \(\mathscr W\) can be nonzero.  Its absolute
mass is \(\asymp Q\) for every such \(\alpha\).  Thus the omitted
range is necessary both for literal exactness and for convergence.

### 3.2 Character-Poisson constant and the saddle

With \(\widehat F(\xi)=\int F(x)e(-\xi x)\,dx\), Poisson in each
class modulo four gives

$$
 \sum_n\chi_4(n)F(n)
 =\frac14\sum_q\widehat F(q/4)
   \sum_{r\bmod4}\chi_4(r)e(qr/4).
$$

For odd \(q\), the inner sum is \(2i\chi_4(q)\), and it is zero for
even \(q\).  This proves the factor \(i/2\), including its sign.

For the phase
\(\phi(x)=\sqrt{Nd\ell x}-qx/4\), a positive saddle exists only for
\(q>0\), and direct differentiation gives

$$
 x_0=4Nd\ell/q^2,\qquad
 \phi(x_0)=Nd\ell/q=\lambda,\qquad
 \phi''(x_0)=-q^3/(32Nd\ell).
$$

Under \(x=x_0(1+u)^2\),
\(\phi(x)=\lambda(1-u^2)\), and the amplitude/Jacobian factor is

$$
 \frac{2\sqrt2\,N^{1/4}}{(d\ell q)^{1/2}}
 (1+u)^{-1/2}\mathscr A(d,e_0(1+u)^2).
$$

Using
\(\int_{\mathbb R}e(-\lambda u^2)du=e(-1/8)/\sqrt{2\lambda}\)
gives \(2e(\lambda-1/8)/(N^{1/4}d\ell)\).  Multiplication by
\(i/2\) yields \(i e(-1/8)=e(1/8)\), proving (R148.3).  Thus the
reported phase sign, unit, \(N^{-1/4}(d\ell)^{-1}\) amplitude, and
\(q\asymp\ell Q\) support all pass hostile recalculation.

### 3.3 Endpoint and higher-symbol ledger

The two primal peel counts are correct.  A product collar of width
\(O(\sqrt M)\) contains

$$
 \ll\sum_{d\asymp D}(\sqrt M/d+1)\ll\sqrt M+D\ll\sqrt M
$$

lattice points and hence costs \(O(M^{-1/4}X^\varepsilon)\).
On \(e=4d\), a width \(O(\sqrt D)\) collar contains
\(O(D^{3/2})\) points; since \(M\asymp D^2\), it costs
\(O(X^\varepsilon)\).  Direct character-Poisson has no polar term,
and the \(q=0\) character transform vanishes.

The fixed stationary-symbol power ledger is also consistent.  If
\(P_0\ll R\sqrt D X^\varepsilon\) denotes the normalized absolute
capacity of the leading symbol, the \(r\)-th even symbol has capacity

$$
 P_0\left{
   \lambda^{-r}
  +M^{-1/2}(M/\lambda)^r
  +\mathbf1_{M\asymp D^2}D^{-1/2}(D/\lambda)^r
 \right\}.                                                   \tag{R148.10}
$$

For \(r=1\), these are respectively
\(1/(R\sqrt E)\), \(\sqrt D/R\), and \(1/R\), as claimed in
(148.29).  Each further radial factor is
\(M/\lambda=\sqrt M/R^2\le R^{-1}\), and each further cone factor
is \(D/\lambda\ll R^{-2}\).  Thus every *fixed displayed symbol*
is target-safe.

The exact-remainder statement needs another line of algebra and then a
uniform estimate.  If \(\eta\) is an even cutoff and \(P_{2K-1}\) is
the Taylor polynomial of \(H\), replacing localized moments by
full-line moments gives schematically

$$
 \int_{-1}^{\infty}He(-\lambda u^2)du
 =\int_{\mathbb R}P_{2K-1}e(-\lambda u^2)du
  +\int\eta(H-P_{2K-1})e(-\lambda u^2)du
  +\int\bigl((1-\eta)H-(1-\eta)P_{2K-1}\bigr)
        e(-\lambda u^2)du,                                  \tag{R148.11}
$$

with the full-line/domain extension made explicit.  The last integral
is not the unchanged complementary integral.  After defining it
correctly, the report must partition positive \(q\) into saddle,
transition, near-endpoint buffer, and quantitatively nonstationary
ranges; record derivative norms through the integration-by-parts order;
and sum the resulting bounds over \(d,\alpha,b,q\).  Equation
(R148.10) alone does not prove the asserted aggregate bound for
\(\mathcal R_K+\mathcal I_{\rm ns}\).

### 3.4 Scope of the Cauchy diagonal no-go

For \(b=1\), \(\ell=\alpha^2\), and a dyadic
\(\alpha\asymp A\), the number of odd plateau frequencies is
\(\asymp\alpha^2Q\).  Hence

$$
 \sum_{i\in\mathcal I_A}|c_i|^2\asymp Q/A,qquad
 \sum_{i\in\mathcal I_A}|c_i|\asymp QA.
$$

Summing the second quantity over dyadic blocks up to
\(\alpha\ll\sqrt E\) gives \(\mathscr L\asymp Q\sqrt E\).
Under (R148.5), weighted Cauchy and ordinary Cauchy on the two positive
weight sums prove (R148.6), then (R148.7).  The factor-\(R\) loss is
therefore genuine for this proof placement, and Mobius signs cannot
alter a diagonal which has already been separately made positive.

This proof does not survive a change of basis before Cauchy.  In
particular, reduced primitive fractions satisfy
\(\ell_1/q_1=\ell_2/q_2\Rightarrow(\ell_1,q_1)=(\ell_2,q_2)\),
but the actual integer-\(d\) phases agree whenever

$$
 N(\ell_1q_2-\ell_2q_1)\equiv0\pmod{q_1q_2},                \tag{R148.12}
$$

which is weaker than equality of the fractions.  Regrouping (R148.12)
fibres, or exploiting their signed correlations, is precisely a
pre-diagonal cross-cell operation.  It is not refuted by (R148.6).

## 4. First doubtful or unproved step

The first literal defect is the absent finite \(\alpha\)/progression
restriction in (148.3).  Until it is restored, the displayed leading
transform is not a finite scalar and cannot be called the exact image
of the finite divisor expansion.

After that local repair, the first analytic gap is the aggregate
remainder assertion in Section 3.3 of the discovery report.  The
fixed-symbol exponents are favorable, but no uniform nonstationary
phase lower bound, endpoint buffer, derivative-order choice, or summed
remainder inequality is displayed.  This gap lies before the arithmetic
signed-dispersion problem and must be closed if (148.2) is to be used as
an equality up to \(O(X^\varepsilon)\).

The diagonal calculation has no comparable algebraic gap once its
quantifiers are narrowed to (R148.5)--(R148.6).  Its doubtful step is
only the report's broader wording ("independent of completion order"),
which is not proved and is false for a completion/regrouping that
changes the cell basis before Cauchy.

## 5. Control tests and outcomes

1. **Squarefreeness of both variables and coprimality -- AMBER.**
   Identities (148.14)--(148.16) are exact, including odd parity and
   \(\chi_4(\ell)\chi_4(n)\).  Formula (148.3) must restore the finite
   \(\alpha\) and nonempty-progression indexing inherited from them.

2. **Character-Poisson constant -- GREEN.**  The Gauss sum is
   \(2i\chi_4(q)\) for odd \(q\), so the transform factor is \(i/2\).
   Even and zero frequencies vanish.

3. **Saddle unit, amplitude, phase and support -- GREEN.**  Hostile
   recalculation gives \(e(1/8)\), phase \(e(+Nd\ell/q)\), amplitude
   \(N^{-1/4}(d\ell)^{-1}\), and \(q\asymp\ell Q\) with the literal
   factor two in \(Q\).

4. **Gaussian exactness -- AMBER.**  The full-line moments and every
   displayed stationary coefficient are correct.  The definition of
   \(\mathcal I_{\rm ns}\) omits the complementary Taylor-polynomial
   correction needed for the claimed equality.

5. **Hard endpoints, prefix and cone collar -- GREEN.**  The physical
   lattice counts and their weights are target-safe, including a prefix
   shorter than its product collar.  The direct Poisson route creates
   no pole.

6. **Higher fixed symbols -- GREEN; total remainder -- AMBER.**  The
   derivative/fraction powers in (148.28)--(148.29) check out.  A
   uniform summed estimate for the exact Taylor remainder, negative
   frequencies, positive nonstationary tails, and saddle/end-support
   transition is still required.

7. **Progression-cell Cauchy diagonal -- GREEN in narrow scope.**  The
   absolute mass \(Q\sqrt E\) and capacity
   \(Q\sqrt M=\sqrt N D\) are correct for unrecombined cells satisfying
   a common plateau lower bound.  It is a method capacity, not a lower
   bound for the signed scalar.

8. **Completion-order and primitive-channel scope -- RED as worded.**
   Positive weighting cannot repair the fixed cellwise Cauchy step, but
   pre-Cauchy recombination, signed off-diagonal use, and
   \(N\)-dependent phase alignments are outside the proof.  Remove the
   claim of completion-order independence and state this exclusion.

9. **Endpoint and downstream ownership -- GREEN.**  Even after repair,
   the report supplies only a scoped \(t=1\) method no-go.  It owns no
   \(t\ge2\) layer, Round-138 cross term, lower GAR, M9--M1, M9--M2,
   endpoint uniformity, M9, bridge, or exponent claim.

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

This review used only:

- `protocol.md`;
- the four Round-148 target nodes in `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round148_squarefree_reciprocal_dispersion_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/signed_squarefree_reciprocal_attack.md`.

No shared state, sibling report, web source, or computation was used.

## 7. Recommended state effect and precise repairs

Retain the signed \(t=1\) target open.  Do not yet promote (148.2)--
(148.3) as an exact target-safe transform.  The narrow positive-diagonal
barrier may be retained after the following repairs:

1. Insert the exact finite \(\alpha\) range and the original nonempty
   \(e=\ell n\) progression convention into (148.3), (148.5), and every
   subsequent sum.  At minimum display \(\alpha^2\le e_+\ll E\); do not
   say that (148.13) supplies this cutoff.

2. Choose and state an even saddle cutoff, define the Taylor polynomial,
   and redefine \(\mathcal I_{\rm ns}\) to include the complementary
   polynomial subtraction and full-line/domain tail so that (148.23) is
   an actual equality.

3. Add a uniform remainder lemma: exact \(q\)-range partition, lower
   bounds for \(|\phi'|\) off the saddle buffer, amplitude derivative
   norms through the chosen order, the value of fixed \(K\), and the
   completed sum over \(d,\alpha,b,q\).  State separately the radial,
   cone, terminal-prefix, negative-frequency, and positive-tail bounds.

4. Define \(S_i\), its common interior \(d\)-plateau, and the uniform
   lower bound (R148.5) before invoking the diagonal.  State the no-go
   only for weighted Cauchy on unrecombined progression cells with a
   separately nonnegative diagonal/off-diagonal ledger.

5. Delete "independent of completion order."  Replace the primitive
   duplicate sentence by the distinction between literal equality of
   reduced fractions and the \(N\)-dependent congruence (R148.12).
   Explicitly leave all pre-Cauchy signed regrouping and cross-cell
   cancellation open.

With these changes, the report supports a rigorous, method-specific
`squarefree_reciprocal_dispersion_no_go`; without them it is not a
promotion-ready exact transform.

AMBER
