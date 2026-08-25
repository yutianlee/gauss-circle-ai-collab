# Round 149 hostile seam review of the conductor candidate

- Campaign: m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate
- Reviewed artifact: candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md
- Role: independent hostile mathematical seam reviewer
- Verdict: **RED**
- Status: review evidence only; no shared-state edit

## 1. Result

**RED.** The lcm formula, closed \(B_{d,U}\) formula,
prefix-uniform norms, \(DQ\) diagonal, and imprimitive exact-alignment
count all pass direct rederivation, including even \(d\), common
denominator factors, and the distinct-cell cross terms.

The first precise defect occurs in the paragraph following
(149.C30). The candidate asserts that a “standard second-derivative
estimate” gives

\[
\sum_{q_0\asymp Q}
\chi_4(q_0)\mathscr W_{d,U}(1/q_0)e(Nd/q_0)
\ll_\varepsilon RX^\varepsilon
\qquad (D=1,\ M\asymp1),
\tag{R1}
\]

but it states only that the profile is uniformly bounded. A weighted
second-derivative estimate requires quantitative variation or symbol
bounds on the sampled profile, for example

\[
\|\mathscr W_{d,U}(1/\cdot)\|_\infty+
\sum_{q\asymp Q}
\left|\mathscr W_{d,U}(1/(q+2))
      -\mathscr W_{d,U}(1/q)\right|
\ll_\varepsilon X^\varepsilon,
\tag{R2}
\]

or corresponding derivative bounds at scale \(Q\). Smoothness and
boundedness without a quantitative derivative condition are
insufficient. The candidate neither states (R2), derives it from the
actual radial-cone-prefix profile, nor cites an exact accepted
equation that supplies it.

Conditional on (R2), the numerical second-derivative powers in the
candidate are correct:

\[
\ll_\varepsilon
(NM)^{1/4}+N^{1/4}M^{-3/4}
\ll_\varepsilon RM^{1/4},
\tag{R3}
\]

and hence \(O_\varepsilon(RX^\varepsilon)\) when \(M\asymp1\).
Likewise, the derivative range has length \(\asymp M\), so the stated
dual self-return diagnosis has the correct formal scale. What is
missing is the hypothesis that permits either theorem to be applied
to the actual profile and its clipped boundaries.

This defect does not overturn the exact compression or the stated
near/generic no-go. It does prevent a GREEN verdict for the candidate
as written and prevents promotion of the unconditional \(D=1\)
second-derivative assertion.

## 2. Exact statement and hypotheses checked

The review checks the following claims from the conductor candidate.

1. For squarefree \(d\), with \(d_{\mathrm o}=d/(d,2)\),

   \[
   C_d(n)=\mu(u)\mu(v)
   \]

   exactly when
   \(n=uv^2\), \(u\mid d_{\mathrm o}\),
   \(\mu^2(uv)=1\), and \((v,d)=1\), and is zero otherwise.

2. With the exact finite nonempty-progression indicator retained,
   gcd-lift compression gives

   \[
   B_{d,U}(L)=
   \sum_{g\ {\rm odd}}
   \frac{C_d(gL)\kappa_{d,U}(gL)}g
   \]

   and the closed expression (149.C15).

3. Uniformly in every finite \(0\)-\(1\) prefix,

   \[
   \sum_L\frac{|B_{d,U}(L)|^2}{L}
   +\sum_L\frac{|B_{d,U}(L)|}{L}
   \ll_\varepsilon X^\varepsilon.
   \]

4. With the accepted bounded profile, the literal diagonal is
   \(O_\varepsilon(DQX^\varepsilon)\).

5. Uniform exact outer-frequency alignments
   \(q_1q_2\mid N\Delta\) have divisor multiplicity
   \(O_\varepsilon(X^\varepsilon)\), including common factors and
   even rows.

6. For the \(D=1,L=1\) row, a weighted second-derivative theorem
   applies to the actual profile with the powers stated after
   (149.C30).

Claims 1--5 pass. Claim 6 is not established under the hypotheses
actually displayed in the candidate. The required correction is a
hypothesis/source correction, not a change to the powers in (R3).

## 3. Proof and derivation

### 3.1 Lcm coefficient

For an odd prime \(p\), the local ledger is

| local case | \(v_p(n)=0\) | \(v_p(n)=1\) | \(v_p(n)=2\) |
|---|---:|---:|---:|
| \(p\nmid d_{\mathrm o}\) | \(1\) | \(0\) | \(-1\) |
| \(p\mid d_{\mathrm o}\) | \(1\) | \(-1\) | \(-1+1=0\) |

The last cell is the exact cancellation between
\(p\mid\alpha,p\nmid b\) and \(p\mid\alpha,p\mid b\).
Consequently exponent-one primes form \(u\mid d_{\mathrm o}\), while
exponent-two primes form \(v\) with \((v,d_{\mathrm o})=1\). Since
\(v\) is odd, \((v,d)=1\) is equivalent. The condition
\(\mu^2(uv)=1\) supplies squarefreeness and coprimality. The prime
\(2\) is absent because \(\alpha,b,n\) are odd. Thus (149.C2) is
correct, including even \(d\).

The pair-membership hypothesis allows the common exact factor
\(\kappa_{d,U}(n)\), so (149.C8) is also correct. The floor formula
(149.C9) is the exact condition for an interval component.

### 3.2 Gcd lift and closed \(B\) formula

For \(\ell=gL,\ q=gq_0,\ (L,q_0)=1\),

\[
\chi_4(\ell)\chi_4(q)
=\chi_4(g)^2\chi_4(Lq_0)
=\chi_4(Lq_0),
\]

while the phase, ratio profile, and saddle support reduce respectively
to \(NdL/q_0\), \(L/q_0\), and \(q_0\asymp LQ\). The remaining
\(1/g\), coefficient, and prefix dependence is exactly (149.C5).

Write \(L=ts^2\), with \(t,s\) squarefree and coprime, and set

\[
a=(t,d_{\mathrm o}),\qquad r=t/a.
\]

If \((s,d_{\mathrm o})>1\), the compulsory squared-prime
cancellation makes every lift zero. Otherwise the unique
parameterization is

\[
u=au',\qquad v=rsv',\qquad
u'\mid d_{\mathrm o}/a,\qquad
(v',d_{\mathrm o}rs)=1,
\]

with \(v'\) squarefree and

\[
g=u'r(v')^2.
\]

The sign is

\[
\mu(au')\mu(rsv')
=\mu(a)\mu(r)\mu(s)\mu(u')\mu(v'),
\]

which proves (149.C15), including its \(1/r\) factor. The exact prefix
couples \(u'\) and \(v'\), so the candidate correctly avoids an
unjustified Euler factorization.

### 3.3 Prefix-uniform norms

Taking absolute values after compression gives

\[
|B_{d,U}(ts^2)|
\leq
\frac{1}{r}
\prod_{p\mid d_{\mathrm o}}\left(1+\frac1p\right)
\prod_{p\ {\rm odd}}\left(1+\frac1{p^2}\right)
\ll_\varepsilon \frac{X^\varepsilon}{r}.
\]

Since \(L=ars^2\), the two relevant sums are bounded by

\[
\sum_{a\mid d_{\mathrm o}}\frac1a
\sum_r\frac1{r^3}\sum_s\frac1{s^2}
\quad\text{and}\quad
\sum_{a\mid d_{\mathrm o}}\frac1a
\sum_r\frac1{r^2}\sum_s\frac1{s^2},
\]

respectively. They converge up to the divisor factor
\(X^\varepsilon\), uniformly in an arbitrary finite prefix. Thus
(149.C16)--(149.C17) are correct.

If \(L\ll E\), summing \(1/r\) or \(1/r^2\) over
\(ars^2\ll E\) gives \(O_\varepsilon(\sqrt E X^\varepsilon)\), so
(149.C18) is also correct.

### 3.4 Literal diagonal

For each \(L\), the support contains \(O(LQ)\) odd \(q_0\). Therefore

\[
\begin{aligned}
\mathscr E_{\rm diag}
&\ll_\varepsilon
\sum_{d\asymp D}\sum_L
\frac{|B_{d,U}(L)|^2}{L^2}(LQ)X^\varepsilon\\
&\ll_\varepsilon DQX^\varepsilon.
\end{aligned}
\]

Moreover

\[
Q^2=\frac{4ND}{E}
\asymp \frac{XD^2}{M}
\ll X=R^4
\]

because \(D^2\leq M\). Hence \(Q\ll R^2\), and (149.C19) is
target-safe for every allowed aspect. No squarefree-denominator
\(Q+D\) bound is used.

### 3.5 Exact alignments, common factors, even rows, and cross terms

For reduced cells define

\[
\Delta=L_1q_2-L_2q_1.
\]

If \(\Delta=0\), reducedness makes the cells identical. For a
distinct pair write

\[
q_1=HA,\qquad q_2=HB,\qquad (A,B)=1,
\qquad
\delta=L_1B-L_2A.
\]

Then

\[
\Delta=H\delta,\qquad
(\delta,A)=(\delta,B)=1.
\]

Uniform exact alignment is

\[
HAB\mid N\delta,
\]

so

\[
AB\mid N,\qquad
H\mid (N/AB)\delta.
\]

If \(\delta=0\), then \(A\mid L_1\) and \(B\mid L_2\);
individual reducedness forces \(A=B=1\), after which the cells are
identical. Hence every distinct exact cross term has
\(\delta\ne0\), and the choices of \(A,B,H\) have divisor
multiplicity \(X^\varepsilon\) because all variables are polynomially
bounded. The weighted \(\ell^1\) norm then proves (149.C25).

For even rows write \(d=2m\). The denominator \(HAB\) is odd, so

\[
HAB\mid 2N\delta
\quad\Longleftrightarrow\quad
HAB\mid N\delta.
\]

Thus parity creates no additional uniform exact alignment. Cross
terms for which \(q_1q_2\mid Nd\Delta\) only on selected rows, but
not \(q_1q_2\mid N\Delta\), are not silently declared safe in
Section 5: they remain among the nonexact variable-row terms in
(149.C27)--(149.C31). This scope separation is correct.

If \(q_0\mid N\), the phase is identically one and the divisor count
\(\tau(N)\), followed by the weighted \(\ell^1\) norm, proves
(149.C26).

### 3.6 The \(D=1\) second-derivative calculation

For \(D=1\), \(E\asymp M\) and

\[
Q\asymp\sqrt{N/M}.
\]

Split the odd \(q\)-sum into the two residue classes modulo \(4\), on
which \(\chi_4\) is constant. For \(q=4n+c\), the phase is

\[
f_c(n)=\frac{Nd}{4n+c},
\]

and throughout \(q\asymp Q\),

\[
|f_c''(n)|\asymp\frac{N}{Q^3}=:\Lambda.
\]

A weighted van der Corput second-derivative lemma, **provided** the
weight has total variation \(O_\varepsilon(X^\varepsilon)\), yields

\[
\begin{aligned}
\sum_{q\asymp Q}
\chi_4(q)w(q)e(Nd/q)
&\ll_\varepsilon
Q\Lambda^{1/2}+\Lambda^{-1/2}\\
&\asymp
(NM)^{1/4}+N^{1/4}M^{-3/4}.
\end{aligned}
\tag{R4}
\]

For \(M\geq1\), the first term dominates; for \(M\asymp1\), both are
\(\asymp R\). Also

\[
\Lambda Q\asymp\frac{N}{Q^2}\asymp M,
\]

so a legitimate \(B\)-process has a dual index interval of length
\(\asymp M\) and the expected square-root phase.

The powers and the transform-self-return scale in the conductor
candidate therefore pass. The theorem invocation does not: (149.C19)
states only uniform boundedness of the accepted profile, and no
quantitative variation/symbol estimate appears before the claim
following (149.C30). The exact profile may well satisfy the needed
bound, but that fact must be derived or cited with its hypotheses.

## 4. First doubtful or unproved step

The first doubtful step is exactly the invocation of the standard
weighted second-derivative estimate after (149.C30).

To repair it, the candidate must do one of the following:

1. state and prove scale-correct symbol estimates such as

   \[
   Q^j\sup_{q\asymp Q}
   \left|\frac{d^j}{dq^j}\mathscr W_{d,U}(1/q)\right|
   \ll_{\varepsilon,j}X^\varepsilon
   \]

   for enough \(j\), uniformly in \(U,M\), all clipped boundaries,
   and both \(d=1,2\); or

2. cite an exact accepted artifact and equation that gives the
   corresponding bounded-variation estimate, then verify that the
   profile in (149.C30) is exactly the profile covered there.

The same source check is required before asserting that the dual
transform “returns” a square-root phase with controlled endpoints.
Merely saying that the profile is smooth and uniformly bounded does
not meet the theorem hypotheses.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| exact lcm formula | **GREEN.** The odd-prime local ledger and \(p\mid d_{\mathrm o}\) squared-prime cancellation are correct. |
| absent \(p=2\) factor | **GREEN.** Even \(d\) changes no lcm or gcd-lift local factor. |
| closed \(B_{d,U}\) formula | **GREEN.** The parameterization and all signs and powers of \(g\) in (149.C15) are exact. |
| finite prefix | **GREEN.** The indicator is retained inside the coupled \(u',v'\) sum. |
| prefix-uniform square and weighted \(\ell^1\) norms | **GREEN.** Both convergent ledgers in (149.C17) are valid. |
| finite-support unweighted norms | **GREEN.** The \(\sqrt E\) price in (149.C18) follows from \(L\ll E\). |
| \(DQ\) literal diagonal | **GREEN.** Equation (149.C19) has the correct normalization and all-aspect power ledger. |
| distinct reduced fractions | **GREEN.** \(\Delta=0\) forces identical cells. |
| exact-alignment divisor count | **GREEN.** The \(H,A,B,\delta\) classification and \(AB\mid N\) consequence are correct. |
| common factors and imprimitive denominators | **GREEN.** No squarefreeness of \(q_i\) is assumed. |
| even-\(d\) exact alignments | **GREEN.** Multiplication by \(2\) creates no new exact congruence modulo an odd denominator. |
| selected-row exact cross terms | **GREEN by scope.** Those not uniformly exact remain in the explicitly open variable-row correlation. |
| \(q_0\mid N\) | **GREEN.** The divisor count and weighted \(\ell^1\) norm suffice. |
| \(D=1\) second-derivative powers | **GREEN conditionally.** Formula (R4) confirms the powers and \(M\)-length dual scale. |
| applicability to the actual \(D=1\) profile | **RED.** No quantitative variation/symbol hypothesis or exact source citation is supplied. |
| near/generic boundary | **GREEN as a no-go boundary.** The candidate does not claim the missing variable-row estimate. |

Required control outcome: **RED**, with the first precise defect at
the weighted theorem invocation after (149.C30).

## 6. Dependencies and exact artifacts used

This review used:

1. protocol.md, already read under the campaign protocol;
2. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/blind_statement.md, including the corrected even-\(d\) convention;
3. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/briefs/blind_compressed_energy_feasibility.md;
4. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md.

The sealed blind report was not reopened. No graph, proof draft,
sibling report, computation, or web source was used.

## 7. Recommended state effect

**Revise before promotion.** The exact lcm/gcd-lift compression,
closed coefficient, prefix-uniform norms, literal diagonal, and
exact-alignment divisor estimate are mathematically sound and may be
retained as separable candidate lemmas. The conductor candidate as a
whole should remain RED until the paragraph after (149.C30) either:

1. adds and verifies uniform bounded-variation/symbol hypotheses for
   the actual profile and its clipped endpoints; or
2. downgrades the \(M\asymp1\) second-derivative assertion and the
   dual-transform statement to conditional diagnostics.

No change should be made to the open near/generic energy, scalar
target, independent cross owner, \(t\geq2\) layers, or downstream
obligations.
