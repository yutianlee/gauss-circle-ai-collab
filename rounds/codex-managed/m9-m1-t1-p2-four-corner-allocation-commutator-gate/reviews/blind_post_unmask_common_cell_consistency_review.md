# Round 197 blind post-unmask common-cell consistency review

## 1. Result

**Decision on the pre-repair candidate: REPAIR.**

The candidate's finite allocation and character algebra was correct.
The lower mask \(P_{\rm cc}\) was genuinely symmetric, the actual lower
endpoint difference had the required smooth/BV/selector product
decomposition, the abstract one-dimensional BV translation estimate was
correct, and literal zero extension was used consistently.  The strict
common-cell repair was fully consistent with the blind no-go: it removed
the live/dead and sharp-field exits from the claimed piece and left them,
without a target claim, in \(P_{\partial\mathrm{lit}}\).

The pre-repair candidate was not yet GREEN because two quantitative
links were not stated at an auditable level.

1. Its common-cell formula said “up to a fixed finite product” and did
   not display the exact product rule for
   \(\mu^2(N)\rho_N(d)a(N/d,d)\), including the selector commutator and
   the separate factor norms.
2. Its translation from the abstract BV sum to physical lower pairs
   used a uniformly bounded number of possible \(g\)'s.  The sentence
   that closeness and the cone alone imply \(g\le G_0\) was insufficient;
   the live-shell inequality and the resulting multiplicity lemma needed
   to be stated or cited exactly.  The selector-exception argument used
   the same missing link.

These were local, repairable gaps rather than evidence against the
common-cell mechanism.

## 2. Exact statement and hypotheses audited

The review audited only the narrow assertion on

\[
 P_0=P_2\mathbf1_{(m,\beta)=1}
          \mathbf1_{\chi_4(\alpha m)=-1}
\]

and

\[
 C_{\rm lit}=
 \mathbf1_{\{\mathfrak c_{N,\sigma}(m,g\alpha)
              =\mathfrak c_{N,\sigma}(\alpha,gm)\}},
 \qquad P_{\rm cc}=P_0C_{\rm lit}.
\]

The lower allocation involution was supposed to turn each physical
two-term orbit into an actual endpoint difference and to bound the
smooth and normalized-BV parts after summation.  No conclusion about
\(P_{\partial\mathrm{lit}}\), the other pieces of \(P_2\), or any parent
theorem was inferred.

The displayed proof required the following exact literal facts:

1. On a common live code,

   \[
   a(u,v)=K_{\rm sharp}\eta_L(u)b(u,v)
   \]

   with the same \(K_{\rm sharp}\) at both inputs.
2. At the epsilon scale used in the count,

   \[
   |K_{\rm sharp}|+\|\eta_L\|_\infty
   +\operatorname {Var}(\eta_L)
   +\|b\|_\infty+L\|\nabla b\|_\infty
   \ll_\varepsilon X^\varepsilon.
   \]
3. Every live lower tuple in the shell has only \(O(1)\) admissible
   values of \(g\), uniformly in \(L,X\).
4. The selector uses two distinct selected primes with the asserted
   \((1,0,0,1)\) truth table and a uniform
   \(O(L^{-1/2})\) logarithmic-gap constant.

The pre-repair candidate invoked these facts but did not state or cite
items 2--4 precisely enough for this seam.

## 3. Proof or derivation

### 3.1 Gcd, parity, allocation, and character algebra

At the lower swapped corner,

\[
 (gm,g\beta)=g(m,\beta).
\]

Thus \((m,\beta)=1\) is necessary and sufficient for the image to retain
the original gcd \(g\); the reverse condition is
\((\alpha,\beta)=1\), already true by normalization.  The allocation
distances, \(N,N+r,r\), the Fejer factor, and the radical phase are
unchanged.

There is no hidden parity failure.  Since \(g,\alpha\) are odd and
\(\chi_4(\alpha m)=-1\), \(m\) is odd, so \(gm\) is an odd physical
divisor.  Also \(\chi_4(\alpha m)=-1\) excludes \(\alpha=m\), hence the
lower action is a genuine two-cycle.

If

\[
 w_0=\chi_4(g\beta)\chi_4(g\alpha),
\]

then

\[
 \chi_4(g\beta)\chi_4(gm)
 =w_0\chi_4(\alpha m)=-w_0.
\]

This proves the two-term character difference with the common physical
phase retained.  For the subsidiary rectangle, the four gcds and
relative character multipliers are

\[
 g,\quad g(m,\beta),\quad g(\alpha,m'),\quad g(m,m')
\]

and

\[
 (1,s_0,s_1,s_0s_1).
\]

Therefore the common sign \(\chi_4(\alpha\beta)\), the alternating table
in the \((-1,-1)\) sector, \(4\mid r\), and the mixed endpoint
factorization agree with the blind derivation.

### 3.2 Symmetry of the sharp code and exact complement

The lower involution exchanges

\[
 (m,g\alpha)\quad\hbox{and}\quad(\alpha,gm).
\]

Equality of their complete sharp codes is therefore invariant.  The
same is true for a common dead code, and accidental numerical
nonvanishing is not part of the code.  The other factors in \(P_0\) are
also invariant, so \(P_{\rm cc}\) is a union of complete lower
two-cycles.

The first-failure partition is Boolean-exact: \(P_{g\mathrm f}\) takes
\((m,\beta)>1\), \(P_{s\mathrm f}\) takes the remaining wrong-character
terms, and the remaining \(P_0\) splits into \(P_{\rm cc}\) and
\(P_{\partial\mathrm{lit}}\).

### 3.3 Exact product rule for the actual coefficient

Put

\[
\begin{aligned}
 \rho_0&=\rho_N(g\alpha),&
 \rho_1&=\rho_N(gm),\\
 \eta_0&=\eta_L(m),&
 \eta_1&=\eta_L(\alpha),\\
 b_0&=b(m,g\alpha),&
 b_1&=b(\alpha,gm).
\end{aligned}
\]

On a common live code, direct expansion gives

\[
\boxed{
\begin{aligned}
 \lambda_{N,\sigma}(g\alpha)-\lambda_{N,\sigma}(gm)
  ={}&\mu^2(N)K_{\rm sharp}
  \bigl[\rho_0\eta_0(b_0-b_1)\\
  &\quad+\rho_0b_1(\eta_0-\eta_1)
       +(\rho_0-\rho_1)\eta_1b_1\bigr].
\end{aligned}}
\]

The three brackets are the smooth displacement, normalized-BV
translation, and selector commutator.  This retains the actual
coefficient, including \(\mu^2(N)\) and \(\rho_N\).  On a common dead
code both endpoint values are literally zero; code equality excludes a
live/dead pair.

The masked-operator product rule

\[
 M_hB_h-\chi M_-^{\rm tr}B_-^{\rm tr}
 =M_h(B_h-\chi B_-^{\rm tr})
  +\chi(M_h-M_-^{\rm tr})B_-^{\rm tr}
\]

is also an exact identity and explicitly retains the transported-mask
commutator.

### 3.4 Normalized-BV translation sum

For a sequence \(\eta:\mathbb Z\to\mathbb C\) of finite discrete total
variation \(V\),

\[
 \sum_{0<|a-b|\le D}|\eta(a)-\eta(b)|
 \le D(D+1)V.
\]

For \(a<b\), telescope into increments.  A fixed increment is crossed by
at most \(D(D+1)/2\) ordered pairs; reversing orientation doubles the
bound.  Thus the claimed \(O(D_L^2)\) estimate is correct and is sharp
at that order for a one-jump profile.

For physical pairs, \(|m-\alpha|\le D_L/g\le D_L\).  To apply the
abstract lemma, however, the number of possible \(g\)'s above a fixed
\((m,\alpha)\) must be \(O(1)\).  With that multiplicity lemma, the
\(O(LX^\varepsilon)\) upper-completion count gives

\[
 O(D_L^2LX^\varepsilon)=O(L^2X^\varepsilon).
\]

### 3.5 Selector exception

For a selected prime outside \(g\), squarefreeness of \(N\) makes the
lower swap complement its divisor/complement bit.  A selected prime in
\(g\) stays on the divisor leg.  The truth table \((1,0,0,1)\) changes
only when exactly one selected prime divides \(g\), precisely the third
bracket in the boxed product rule.

If \(g\le G_0\), one exceptional prime lies in a fixed finite set.
Distinct selected primes with

\[
 |\log p-\log q|\le C L^{-1/2}
\]

cannot have exactly one member in that set for sufficiently large
\(L\), because the minimum nonzero logarithmic separation of distinct
primes in a fixed finite interval is positive.  The remaining bounded
shells are target-safe by the raw count since \(D_L=O(1)\).  This
argument was valid conditional on the missing finite-\(g\), distinctness,
and uniform-gap hypotheses.

### 3.6 Zero extension and the blind no-go

On \(P_{\rm cc}\), a dead/dead orbit is zero, a live/live orbit uses the
boxed product rule, and a live/dead orbit is excluded by code inequality.
A selector zero is not confused with a literal dead state; it stays in
\(\rho_0-\rho_1\).

This is exactly the strict repair permitted by the blind report.  Every
support or sharp-field first failure remains in
\(P_{\partial\mathrm{lit}}\), for which the candidate proves no target
bound.  Hence the narrow result does not contradict the whole-sector
no-go.

## 4. First doubtful or unproved step

The first unproved quantitative step in the pre-repair candidate was
the physical multiplicity assertion \(g\le G_0\).  Cone and closeness
alone do not give a uniform constant.  Ignoring the unstated shell
restriction, one may take \(\alpha=1\), odd \(m\equiv3\pmod4\), and
\(g=4m+1\); then

\[
 4m<g\alpha<16m,\qquad \chi_4(\alpha m)=-1,
\]

and closeness holds whenever \(D_L\ge g(m-1)\), while \(g\) is
unbounded.  This example was not claimed to lie in the actual live
shell; it showed that the live-shell lower bound had to be used
explicitly.

The required repair was to state the exact shell inequality, derive the
uniform \(g\)-bound, and use it in both the BV multiplicity and selector
arguments.  The next repair was the exact actual-coefficient product
rule and separate factor norms.

## 5. Required control test and outcome

1. **Gcd and reverse orbit — PASS.**  Only \((m,\beta)=1\) and the
   normalized reverse condition are used by the lower edge.
2. **Character erased — PASS as a falsification.**  Removing
   \(\chi_4\) changes the difference into a sum.
3. **Sharp-code symmetry — PASS.**  Input exchange preserves equality;
   dead/dead is zero and live/dead is excluded.
4. **Actual product rule — REPAIR REQUIRED in the pre-repair text.**
   The three exact brackets above had to replace the vague finite-product
   phrase.
5. **Single-jump BV — PASS.**  A unit jump produces
   \(\asymp D_L^2\) close translations, validating and saturating the
   stated order.
6. **Repeated-\(g\) translations — REPAIR REQUIRED in the pre-repair
   text.**  The live-shell \(O(1)\) multiplicity needed proof or an exact
   citation.
7. **Selector truth table — CONDITIONAL PASS.**  The large-shell
   exclusion follows from finite \(g\), distinctness, and the uniform
   logarithmic-gap constant.
8. **Zero extension — PASS.**  It preserves exact algebra but does not
   smooth a live/dead jump; the mask excludes that jump.
9. **Masked product rule — PASS algebraically.**  It retains the mask
   commutator rather than silently commuting the mask.

## 6. Dependencies and exact artifacts used

Only these four artifacts were used in the pre-repair review:

1. protocol.md.
2. rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reports/blind_four_corner_commutator_rederivation.md.
3. rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/conductor_round197_report_reconciliation.md.
4. rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md.

The discovery report, hostile report, graph, active campaign, source
cards, earlier-round artifacts, controls, and shared state were not read.
The review checked displayed algebra and internal compatibility, not the
content of the earlier accepted dependencies.

## 7. Recommended state effect

**REPAIR; no state change from the pre-repair version.**  Preserve the
gcd/character algebra, symmetric code, exact complement, zero-extension
treatment, abstract BV lemma, and route-scoped no-go.  Before promotion,
the candidate needed:

1. the exact actual-coefficient product rule and factor norms;
2. the live-shell finite-\(g\) lemma;
3. the exact selector constants, distinctness, and bounded-shell audit;
4. exact dependency equations for the masked outer passage.

Subject to those repairs and the independent operator/provenance
reviews, only the subordinate \(P_{\rm cc}\) node and its exact open
packet intersection could be promoted.  The complement and all parents,
bridges, theorems, and exponents had to remain unchanged.
