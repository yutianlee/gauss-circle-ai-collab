# Round 151 terminal primary-source review

- Campaign: `m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate`
- Reviewed candidate: `candidates/conductor_round151_character_ranges_and_bprocess_boundary.md`
- Role: independent terminal primary-source and theorem-hypothesis reviewer
- Starting graph SHA-256: `521f626e4af7e75e29d2ba909efb0d48864d5da4785de786acbd746d7559c11f`
- Terminal verdict: **GREEN**

## 1. Result

The material Bourgain correction is correct.  Bourgain's Theorem 4 proves
the estimate directly only in the window

\[
 \mathcal T^{17/42}\ll H\ll \mathcal T^{1/2},
\tag{151.SF1}
\]

whereas Section 5 culminates in Theorem 6, which states that

\[
 \left(\frac{13}{84}+\varepsilon,
       \frac{55}{84}+\varepsilon\right)
\tag{151.SF2}
\]

is an exponent pair.  Section 5 expressly addresses the two missing
interfaces: lengths above \(\sqrt{\mathcal T}\) and proper subintervals.
Thus (151.SF1) must not be inherited as a restriction on Theorem 6.

The conductor's reciprocal progression is in the required exponent-pair
derivative class.  The exact Mobius decomposition, the two mod-four
classes, the progression length, the oscillation parameter, and the
bounded-variation transfer are all placed in the correct order.  The
fixed comparable upper-support edge where \(\mathcal T_c<H_c\) is not
silently assigned to either external exponent-pair theorem: the candidate
covers it by the stronger second-derivative estimate.  Consequently the
all-\(L\) Bourgain row bound and its power condition

\[
 \boxed{D^{84}R^{52}\ll M^{29}}
\tag{151.SF3}
\]

are source-legal and algebraically correct.

The Tao--Trudgian--Yang statement and its low-\(L\) specialization are
also correct.  Their Theorem 20 lists

\[
 \left(\frac{89}{1282},\frac{997}{1282}\right)
\tag{151.SF4}
\]

as an exponent pair in the model-phase sense of their Definitions 5, 11,
and 12.  It yields exactly

\[
 \boxed{M^{819}\gg
 R^{1424}D^{1816}L_0^{534}}
\tag{151.SF5}
\]

for the recombined low-\(L\) row.  It does not estimate an isolated signed
large-wrap subset, the complementary \(L>L_0\) row, or the low-high cross
term.

The cited Duke--Friedlander--Iwaniec, Cowan, Blomer--Harcos, and
Bettin--Chandee theorems are genuine direct-specialization no-matches for
the literal recovery-weighted collar.  This is a statement about the
printed theorem interfaces, not a literature impossibility theorem.

No source repair is required before promotion.  One non-blocking wording
precision is recommended: when paraphrasing Bourgain Section 5, say that
it uses a near-square rescaling, the pair \((1/2,1/2)\) for the extreme
long range, and a Poisson/partial-summation \(B\)-process for the remaining
long range.  The candidate's shorter phrase "rescaling and the
\(B\)-process" has the right mathematical consequence but compresses this
three-part source discussion.

## 2. Exact statement and hypotheses

For the source interface, fix one supported odd \(L\), one row
\(d\asymp D\), and write

\[
 S_{d,L}=
 \sum_{\substack{q\asymp LQ\;\mathrm{odd}\\(L,q)=1}}
 \chi_4(q)\mathscr W_{d,U}(L/q)e(NdL/q),
 \qquad Q^2=\frac{4ND}{E}.
\tag{151.SF6}
\]

Mobius inversion is performed before invoking an exponent-pair theorem:

\[
 {\mathbf 1}_{(L,q)=1}=\sum_{c\mid(L,q)}\mu(c).
\tag{151.SF7}
\]

Because \(L,q,c\) are odd, after \(q=cm\) one has
\(\chi_4(q)=\chi_4(c)\chi_4(m)\).  Splitting
\(m=4n+a\), \(a\in\{1,3\}\), makes the remaining character constant.
On each of a fixed number of proper dyadic intervals,

\[
 H_c\asymp\frac{LQ}{c},\qquad
 f_c(n)=\frac{NdL}{c(4n+a)},\qquad
 \mathcal T_c\asymp\frac{Nd}{Q},
\tag{151.SF8}
\]

and hence

\[
 \frac{\mathcal T_c}{H_c}
 \asymp\frac{cNd}{LQ^2}
 \asymp\frac{cE}{L}.
\tag{151.SF9}
\]

After conjugation and harmless fixed rescaling, the normalized phase is

\[
 F_{c,a}(u)=-\frac{1}{u+a/(4H_c)}.
\tag{151.SF10}
\]

Since \(H_c\gg Q\gg R\), its first derivative is
\((u+a/(4H_c))^{-2}=u^{-2}+o(1)\), and all higher derivatives have the
corresponding uniform reciprocal pattern.  Thus it is a Tao--Trudgian--
Yang model phase with \(\sigma=2\), and it lies in Bourgain's standard
exponent-pair derivative class.  Complex conjugation only changes the sign
of the original phase and does not change the bound.

The external theorems are unweighted.  The project weight enters only
after their uniform interval estimates, through Abel summation and the
candidate's project-side bound

\[
 \|\mathscr W_{d,U}(L/\cdot)\|_\infty+
 \operatorname {Var}_q\mathscr W_{d,U}(L/q)
 \ll_\varepsilon X^\varepsilon.
\tag{151.SF11}
\]

The exact floor prefix remains in \(B_{d,U}(L)\), independent of \(q\).
Neither source theorem licenses an arbitrary bounded coefficient in place
of (151.SF11).

For \(\mathcal T_c\ge H_c\), either exponent pair
\((\kappa,\lambda)\) gives

\[
 \sum_{n\in I}e(f_c(n))
 \ll_\varepsilon
 (E/L)^\kappa(LQ)^\lambda
 c^{\kappa-\lambda}X^\varepsilon.
\tag{151.SF12}
\]

If \(\mathcal T_c<H_c\), the finite support \(L\ll E\) makes the ratio
in (151.SF9) bounded above and below by fixed positive constants.  Then
\(|f_c''|\asymp H_c^{-1}\), so the second-derivative estimate is
\(O(H_c^{1/2})\).  This is dominated by (151.SF12) for both pairs used in
the candidate because \(\lambda>1/2\).  This is the correct patch for the
formal source convention \(\mathcal T\ge H\).

## 3. Proof or derivation

### 3.1 Bourgain's direct window versus the global pair

The official arXiv text of Bourgain's paper states Theorem 4 after deriving
the bound for
\(17/42\le \log H/\log\mathcal T\le1/2\).  In Section 5 it then states
Theorem 6 as an exponent-pair theorem.  The intervening text explicitly
lists the two extra problems: \(H\) may exceed \(\sqrt{\mathcal T}\), and
the summation interval may be a proper subinterval on which the phase alone
is initially defined.

For the long-length problem, the source treats a near-square range by
rescaling, an extreme range by \((1/2,1/2)\), and the remaining range by
Poisson summation and partial summation in the manner of the exponent-pair
\(B\)-process.  The fixed-point identity

\[
 B(k,k+1/2)=(k,k+1/2)
\tag{151.SF13}
\]

applies to \((13/84,55/84)\).  For a proper subinterval, Bourgain extends
the phase to the ambient dyadic interval while preserving the derivative
class and invokes the partial-sum device attributed to Sargos, losing only
a logarithm.  These are printed source arguments, not a secondary-table
inference.

The reciprocal phase (151.SF10) is safer than the general source class:
all of its derivatives are explicit, nonzero on the fixed compact support,
and uniform in the vanishing residue shift.  Bourgain Theorem 6 therefore
applies whenever \(\mathcal T_c\ge H_c\); the candidate's second-derivative
edge covers the only remaining comparable case.

### 3.2 Mobius normalization, variation, and the all-\(L\) power

Applying the unweighted interval estimate first and Abel summation second
gives

\[
 |S_{d,L}|\ll_\varepsilon
 E^\kappa Q^\lambda L^{\lambda-\kappa}X^\varepsilon,
\tag{151.SF14}
\]

because

\[
 \sum_{c\mid L}c^{\kappa-\lambda}
 \leq\tau(L)\ll_\varepsilon X^\varepsilon.
\tag{151.SF15}
\]

For Bourgain,
\(\lambda-\kappa=55/84-13/84=1/2\).  The accepted half-weight norm
therefore yields

\[
 |G_U(d)|\ll_\varepsilon
 E^{13/84}Q^{55/84}X^\varepsilon.
\tag{151.SF16}
\]

After squaring and summing \(O(D)\) rows, division by the target
\(R^2D\) gives

\[
 \frac{E^{13/42}Q^{55/42}}{R^2}
 \asymp
 D R^{13/21}M^{-29/84}
 =\left(\frac{D^{84}R^{52}}{M^{29}}\right)^{1/84}.
\tag{151.SF17}
\]

This proves exactly (151.SF3).  At \(M\asymp R^2\), it becomes
\(D\ll R^{1/14}\).  No direct-window condition from Bourgain Theorem 4
is needed.

### 3.3 Tao--Trudgian--Yang low-\(L\) corridor

Tao--Trudgian--Yang Definition 11 supplies the estimate on every interval
\(I\subset[H,2H]\), with \(\mathcal T\ge H\), and Definition 12 supplies
the finite-derivative, non-asymptotic epsilon form.  Theorem 20 states
(151.SF4).  Here

\[
 \lambda-\kappa=\frac{908}{1282},\qquad
 \lambda-\kappa-\frac12=\frac{267}{1282}.
\tag{151.SF18}
\]

Thus (151.SF14) and the half-weight coefficient norm give

\[
 |G_{U,\le L_0}(d)|
 \ll_\varepsilon
 E^{89/1282}Q^{997/1282}
 L_0^{267/1282}X^\varepsilon.
\tag{151.SF19}
\]

Its squared ratio to the per-row target is

\[
 \frac{E^{178/1282}Q^{1994/1282}L_0^{534/1282}}{R^2}
 \asymp
 \left(
 \frac{R^{1424}D^{1816}L_0^{534}}{M^{819}}
 \right)^{1/1282}.
\tag{151.SF20}
\]

This confirms (151.SF5).  In fact the corridor itself places the TTY
application well inside its \(\mathcal T_c\ge H_c\) convention, since

\[
 \left(\frac{L_0}{E}\right)^{534}
 \ll \frac{M^{285}}{R^{1424}D^{1282}}
 \le R^{-854}.
\tag{151.SF21}
\]

Hence the second-derivative edge is needed for the complete Bourgain row
and for a globally phrased version of (151.SF14), but not for the strict
TTY corridor itself.

The source theorem controls the linear low-\(L\) row before squaring.
It therefore controls its recombined low-low energy, including all wraps
inside that component.  It does not control a proper signed subset of the
expanded energy, \(G_{>L_0}\), or
\(G_{\le L_0}\overline{G_{>L_0}}\).

### 3.4 Boundary-complete reciprocal \(B\)-process source

The cited Lutsko--Sourmelidis--Technau Theorem 1.3 is a half-open,
unweighted \(B\)-process.  Its hypotheses are satisfied on \(q\asymp Q\)
for

\[
 \phi_\sigma(q)=N/q+\sigma q/4,
 \qquad \Lambda\asymp N/Q^3,
\tag{151.SF22}
\]

because the second through fourth derivatives have exactly the required
scales.  Uniform application to prefixes followed by Abel summation is
the legal way to insert the actual BV weight.  The source error becomes

\[
 (\|w\|_\infty+\operatorname {Var}w)
 \left(\frac{Q^{3/2}}{\sqrt N}
       +\log\left(2+\frac{N}{Q^2}\right)\right).
\tag{151.SF23}
\]

The half-open dual interval retains its full endpoint convention.  The
stationary action, amplitude, and branch recombination are
\(\sqrt{N\ell}\), \(2N^{1/4}\ell^{-3/4}\), and
\(e(-1/8)\chi_4(\ell)\), respectively.  This verifies the source side of
the candidate's principal wave and target-safe transform error.  The
source does not turn the dual main sum into an error and does not prove
exact composition of lower stationary symbols; the candidate correctly
restricts self-return to the phase and principal stationary symbol.

### 3.5 Shifted-divisor and Kloosterman no-matches

The primary theorem statements confirm the source report's conclusions.

1. Duke--Friedlander--Iwaniec Theorem 1 treats
   \(\tau(m)\tau(n)f(am,bn)\) on \(am\pm bn=h\), with a smooth weight in
   the two product variables.  The formal identity
   \(AB-N^2L_1L_2=kh\rho\) fits its equation, but the literal project
   coefficient lives on the factor-recovery fibre, carries
   \(\chi_4\), prefixes, masks, and two sampled profiles, and is not the
   printed divisor coefficient with a smooth product-variable weight.
   Its printed error also has the adverse project size recorded in the
   source report.
2. Cowan Theorem 1.1 fixes a positive shift, a prime modulus, even
   nontrivial characters with nontrivial product, and nonzero \(u,v\),
   while every quantity other than the cutoff tends as a fixed parameter.
   The project's odd character modulo four, signed growing shift family,
   and recovery-weighted coefficients do not specialize to that theorem.
3. Blomer--Harcos Theorem 1 uses two fixed cuspidal Hecke sequences at
   conductor one.  Its arbitrary-level remark introduces additional
   cusps, complementary-series terms, and explicit level factors.  The
   project coefficient is not a pair of fixed cuspidal Hecke sequences,
   so the spectral decomposition has no direct literal specialization.
4. Bettin--Chandee Theorem 1 requires three independent coefficient
   sequences in a Kloosterman-fraction form.  Theorem 2 inserts a Jacobi
   symbol, not the project's mod-four character.  Corollary 1 fixes one
   determinant and uses separated weights.  The recovery fibre and sampled
   project profiles are graph-coupled, and the project ranges over a
   growing determinant/shift family.  Therefore none of these printed
   statements directly supplies the missing joint collar estimate.

These are exact interface failures.  They do not rule out a new argument
which first transforms the project coefficient into a legal source input.

## 4. First doubtful or unproved step

There is no failed external-theorem step in the conductor candidate.
The first unproved project continuation is the low-two-adic large-wrap
residual outside the strict row corridors, with the divisor fibre
\(h\mid g\) still coupled to both profiles, support, denominator, and
reconstructed wrap.  None of the audited shifted-divisor sources estimates
that literal object.

For the TTY component, the first unowned continuation is the
\(L>L_0\) square and the low-high cross term.  For the reciprocal
\(B\)-process component, it is a target-sized signed estimate of the
square-root dual main wave.  These are correctly left open.

The only source-wording refinement is the three-part description of
Bourgain's treatment of \(H>\sqrt{\mathcal T}\) given in Section 1 above.
It does not change any bound or state effect.  The source report's optional
fixed-constant renormalization at \(\mathcal T_c<H_c\) should not replace
the candidate's explicit second-derivative patch in the accepted proof;
the latter is direct and avoids any model-normalization ambiguity.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Bourgain Theorem 4 versus Theorem 6 | **GREEN.** The direct window belongs to Theorem 4; Theorem 6 is the global exponent-pair statement. |
| Long-length and proper-subinterval language | **GREEN.** Section 5 prints the rescaling, extreme-range, \(B\)-process, phase-extension, and Sargos partial-sum mechanisms. |
| Reciprocal derivative class | **GREEN.** The residue-shifted reciprocal phase has the uniform model derivatives required by both sources. |
| \(\mathcal T\ge H\) convention | **GREEN.** External pairs are used only there; the fixed comparable edge is covered by a second-derivative bound. |
| Mobius progression normalization | **GREEN.** The length is \(H_c\asymp LQ/c\), the parameter is \(\mathcal T_c\asymp Nd/Q\), and the divisor cost is \(c^{\kappa-\lambda}\). |
| Character placement | **GREEN.** \(\chi_4\) is resolved into two odd residue classes after exact coprimality inversion. |
| BV timing | **GREEN.** Both exponent-pair theorems are invoked on unweighted intervals; (151.SF11) is inserted only by Abel summation. |
| Bourgain all-\(L\) power | **GREEN.** The exact condition is \(D^{84}R^{52}\ll M^{29}\), with \(D\ll R^{1/14}\) at \(M\asymp R^2\). |
| TTY low-\(L\) power and source range | **GREEN.** The exact condition is (151.SF5), and it implies a power margin in \(\mathcal T_c/H_c\). |
| Whole-row versus isolated-collar scope | **GREEN.** The candidate claims recombined whole-row or low-subrow owners and expressly leaves arbitrary signed subsets open. |
| Boundary-complete \(B\)-process | **GREEN.** The half-open source, weighted Abel transfer, full dual main sum, error, and endpoint convention are retained. |
| Shifted-divisor source matches | **GREEN as no-matches.** The four printed theorem interfaces fail at the exact coefficients, parameter growth, independence, character, level, or determinant seams stated above. |
| Downstream scope | **GREEN.** No full collar, \(t\ge2\) layer, Round-138 cross owner, M9--M1, M9--M2, M9, bridge, quarter target, or global exponent is inferred. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Repository artifacts inspected were:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/candidates/conductor_round151_character_ranges_and_bprocess_boundary.md`;
3. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/reports/large_wrap_shifted_divisor_source_audit.md`;
4. `sources/bourgain_2017_exponent_pair.md` in its corrected Round-151 form; and
5. `sources/tao_trudgian_yang_2025.md`.

The primary texts checked were:

1. Jean Bourgain, [*Decoupling, exponential sums and the Riemann zeta function*](https://arxiv.org/html/1408.5794v2), especially Theorems 4 and 6 and Section 5;
2. Terence Tao, Tim Trudgian, and Andrew Yang, [*New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*](https://arxiv.org/html/2501.16779v1), especially Definitions 5, 11, and 12 and Theorem 20;
3. W. Duke, J. B. Friedlander, and H. Iwaniec, [*A quadratic divisor problem*](https://www.math.ucla.edu/~wdduke/preprints/quadraticdiv.pdf), Theorem 1;
4. Alex Cowan, [*A twisted additive divisor problem*](https://arxiv.org/html/2304.12572v1), Theorem 1.1;
5. Valentin Blomer and Gergely Harcos, [*The spectral decomposition of shifted convolution sums*](https://arxiv.org/html/math/0703246v2), Theorem 1 and Remark 2;
6. Sandro Bettin and Vorrapan Chandee, [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/html/1502.00769v1), Theorems 1 and 2 and Corollary 1; and
7. Christopher Lutsko, Athanasios Sourmelidis, and Niclas Technau, [*Pair correlation of the fractional parts of \(\alpha n^\theta\)*](https://ems.press/content/serial-article-files/51183?nt=1), Theorem 1.3 and Lemma 1.4.

No secondary exponent-pair table was used.  No candidate, source card,
proof-state file, validation matrix, synthesis, or proof draft was edited.

## 7. Recommended state effect

**Recommended effect: GREEN for the corrected source interface and the
two strict row corridors.**

The conductor may promote, subject to the other terminal seam reviews:

1. the corrected Bourgain source card distinguishing the direct Theorem-4
   window from the global Theorem-6 exponent pair;
2. the source-legal all-\(L\) Bourgain row bound under
   \(D^{84}R^{52}\ll M^{29}\);
3. the source-legal TTY low-\(L\) row bound under
   \(M^{819}\gg R^{1424}D^{1816}L_0^{534}\);
4. the boundary-complete reciprocal principal transform and its
   source-supported no-automatic-gain conclusion; and
5. the four shifted-source conclusions only as direct-specialization
   no-matches.

Promotion must retain the candidate's whole-row/low-subrow scope, the
second-derivative edge patch, Abel-after-unweighted ordering, exact
Mobius and character placement, and all named open complements.  It must
not relabel either row estimate as a theorem for an arbitrary isolated
signed collar subset, and it must not change any downstream global
exponent.
