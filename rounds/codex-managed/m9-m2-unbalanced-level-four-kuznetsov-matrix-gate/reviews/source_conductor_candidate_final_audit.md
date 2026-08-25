# Final source audit of the Round 143 conductor candidate

## 1. Result

**Verdict: REVISE, with all central source identities green and three
localized hypothesis repairs required before promotion.**

The following claims in
candidates/conductor_round143_level_four_matrix_obstruction.md pass the
primary-source audit:

1. Kıral--Young (2.20) cannot certify the odd character \(\chi _4\);
   the candidate correctly keeps (143.C3) as an internal double-coset
   identity rather than a sourced weight-one trace formula.
2. Blomer--Milićević's character identity is specialized correctly in
   (143.C20), including
   \(u=(N_0,4^\infty)\), \(M_0=N_0/u\), the argument \(16uh\), the fixed
   factor \(\chi _4(M_0)/\tau(\chi _4)\), the value
   \(\tau(\chi _4)=2i\), one common \(\omega\), and the level-\(4\) minus
   level-\(8\) sign.
3. The candidate's level-\(4/8\) \(H+M+E\) ledger, singular-cusp lists,
   level-\(8\) oldclasses, same-sign transforms (143.C21)--(143.C22), and
   refusal to promote an opposite-sign normalization all pass.
4. The conditional cross-cusp \(2nA_g\) sample and source-certified
   standard-cusp \(4nA_g\) sample are correctly distinguished.  Their
   Bessel arguments agree exactly, and the fixed factor two does not alter
   any norm exponent.

Three source-scope statements still require revision:

1. (143.C29) is valid as a ratio of continuous scales, but it is not
   unconditionally the proportion of integer frequencies covered.  The
   actual covered proportion is \(\ll1/(Dg)\), and is
   \(\asymp1/(Dg)\) only in the many-integer range
   \(H_{\rm Lin}(g)\gg1\), with fixed dyadic constants.
2. The Deshouillers--Iwaniec citation must record its fixed-cusp and
   \(T,N,Y\) hypotheses and state that its printed large sieve is not itself
   the odd-nebentypus, weight-one, level-\(4/8\) theorem used by
   Blomer--Milićević.
3. The Assing--Blomer--Li citation must record its positivity,
   coprimality, support, derivative, single-sequence, and scale hypotheses,
   and state that it contains neither the \(\chi _4\) modulus twist nor the
   level-\(4/8\) encoding.

The same paragraph should state the full hypotheses of the cited
Blomer--Milićević Linnik estimate: fixed positive Fourier arguments, a
fixed arithmetic weight, one fixed compactly supported smooth
archimedean test, and the printed Linnik range.  These are source-card
repairs only; they do not change the candidate's scoped matrix no-go.

## 2. Exact source statements and hypotheses

### 2.1 Kıral--Young parity boundary

Kıral--Young,
[*Kloosterman sums and Fourier coefficients of Eisenstein series*,
arXiv:1710.00914](https://arxiv.org/html/1710.00914), Definition 2.2 and
(2.3), work in the weight-zero multiplier setting.  Theorem 2.7 explicitly
assumes that \(\chi\) is even.  Its example (2.20) states

\[
 S_{\infty,0}(m,n;c\sqrt N;\chi)
 =\overline{\chi}(c)S(\overline N m,n;c),
 \qquad (c,N)=1.                                            \tag{A.1}
\]

Since \(\chi _4(-1)=-1\), (A.1) cannot be cited as a theorem for
\(\chi _4\).  The scaling rule (2.7) changes the sum only by one
modulus-independent phase and cannot repair parity.  The candidate states
this boundary correctly.

### 2.2 Blomer--Milićević identity and spectrum

Blomer--Milićević,
[*Kloosterman sums in residue classes*, JEMS 17 (2015), 51--69](https://ems.press/content/serial-article-files/32008?nt=1),
equation (2.3), p.55, gives, for a finitely supported weight \(\omega\)
(and more generally under their decay hypotheses),

\[
 \sum_{(c,q)=1}\chi(c)S(m,n;c)\omega(c)
 =\frac{\chi(m_0)}{\tau(\chi _1)}
   \sum_{d\mid q}\mu(d)\sum_{dq_1\mid C}
   S_{\chi _1}(m_0,n_0q_1^2;C)\omega(C/q_1),                \tag{A.2}
\]

where \(m_0=m/(m,q^\infty)\) and \(n_0=n(m,q^\infty)\).  For
\(q=q_1=4\), \(m=N_0\), \(n=h\),
\(u=(N_0,4^\infty)\), and \(M_0=N_0/u\), (A.2) becomes

\[
\begin{aligned}
 \sum_{n\ \mathrm{odd}}\chi _4(n)S(N_0,h;n)\omega(n)
 =\frac{\chi _4(M_0)}{\tau(\chi _4)}
 \left(\sum_{4\mid C}-\sum_{8\mid C}\right)
 S_{\chi _4}(M_0,16uh;C)\omega(C/4).                       \tag{A.3}
\end{aligned}
\]

With the candidate's convention

\[
 \tau(\chi _4)
 =\chi _4(1)e(1/4)+\chi _4(3)e(3/4)
 =i+(-1)(-i)=2i.                                           \tag{A.4}
\]

Thus (143.C19a)--(143.C20) are exact, including the Gauss factor and
relative sign.

Section 3, p.57, sets \(\kappa=1\) for odd primitive \(\chi _1\).
Equations (4.1)--(4.6) give, for \(\kappa=1\),

\[
 \dot g(k)=i^k\int_0^\infty J_{k-1}(x)g(x)\frac{dx}{x},
 \qquad k=3,5,\ldots,                                      \tag{A.5}
\]

\[
 \widetilde g(t)=\frac{it}{2\sinh(\pi t)}
 \int_0^\infty\{J_{2it}(x)+J_{-2it}(x)\}g(x)\frac{dx}{x}.   \tag{A.6}
\]

Formula (4.6) and Theorem 4 print \(H+M+E\), with no separate residual
term.  The Maaß part includes real parameters, \(t=0\) if present, and
exceptional parameters; the holomorphic tower begins at \(k=3\).
The singular-cusp criterion (5.1) gives \(\infty,0\) at level \(4\) and
\(\infty,0,1/2,1/4\) at level \(8\).  Primitive conductor four leaves no
proper-level oldspace at level \(4\), while the level-\(8\) basis includes
oldclasses lifted from level \(4\).  Every one of these claims is stated
correctly in the candidate.

### 2.3 Linnik, DI, and ABL hypotheses

Blomer--Milićević Theorem 1, pp.52--53, fixes positive Fourier arguments,
a fixed arithmetic weight
\(f:(\mathbb Z/q\mathbb Z)^*\to\mathbb C\), and a fixed compactly
supported smooth \(f_\infty\).  Its bound contains the normalized
\(q\)-Mellin norm \(\|\widehat f\|_1\) from (1.2) and is printed in the
range

\[
 mn\le C_0^2.                                               \tag{A.7}
\]

No complementary-range uniform theorem is printed.

Deshouillers--Iwaniec Theorem 2, p.230, fixes a cusp
\(\mathfrak a\) of \(\Gamma_0(q)\), assumes \(T\ge1\),
\(N\ge1/2\), and \(\varepsilon>0\), and uses the same sequence
\((a_n)_{N<n\le2N}\) in its holomorphic, Maaß, and Eisenstein quadratic
forms.  Theorem 5, p.232, additionally assumes \(Y\ge1\) for its
exceptional-weight statement.  These theorems are valid common-sequence
interface checks, but their printed form is not the odd-nebentypus,
weight-one, Blomer--Milićević level-\(4/8\) large sieve.

Assing--Blomer--Li Theorem 2.4 assumes positive integers \(n,r,s\) with
\((r,s)=1\), \(M,C,Z\ge1\), one sequence \(\alpha_m\), and a function
\(F\) supported on \([M,2M]\times[C,2C]\) satisfying all displayed
mixed-derivative bounds.  It also assumes

\[
 \frac{\sqrt{Mn}}{s\sqrt r\,C}\ll Z.                        \tag{A.8}
\]

It permits controlled smooth two-variable dependence, but it is not a
theorem for an arbitrary matrix and does not itself contain the
\(\chi _4\) twist or (A.3).

## 3. Source-claim derivation and seam audit

### 3.1 KY and the internal pure-level-\(4\) route -- green

The candidate explicitly calls (143.C3) an internal fixed-modulus
double-coset identity and says that the pure-level-\(4\) spectral inventory
remains conditional.  It neither applies Kıral--Young to \(\chi _4\) nor
imports weight-zero transform constants.  This is exactly the safe source
boundary.

### 3.2 BM identity, Gauss factor, and level split -- green

In (A.2), the only nonzero Möbius terms for \(q=4\) are \(d=1,2\), with
signs \(+1,-1\); \(\mu(4)=0\).  Hence the two standard-cusp levels are
\(4\) and \(8\), and their difference selects \(C=4n\) with \(n\) odd.
The substitutions \(m_0=M_0\) and \(n_0=uh\) give the second argument
\(16uh\).  Equations (A.3)--(A.4) therefore verify every constant in
(143.C20).

### 3.3 Spectrum, cusps, oldclasses, and transforms -- green

The candidate does not confuse the source-certified level-\(4/8\)
standard-cusp implementation with its conditional pure-level-\(4\)
cross-cusp proposal.  Its level-\(4\) and level-\(8\) cusp lists, oldspace
statements, \(H+M+E\) inventory, exceptional and \(t=0\) treatment, and
same-sign transforms agree with the primary source.  It also correctly
withholds an exact odd-weight opposite-sign \(K\)-transform.

### 3.4 The \(2n\)-versus-\(4n\) sample seam -- green

For the conditional cross-cusp route, the generalized modulus is \(c=2n\)
and the indices are \(4N_0,h\), so

\[
 \frac{4\pi\sqrt{(4N_0)h}}{2n}
 =\frac{4\pi\sqrt{N_0h}}{n}.                               \tag{A.9}
\]

An \(S/c\) geometric formula therefore requires the sample
\(2nA_g(n,h)\).

For the source-certified standard-cusp route, the modulus is \(C=4n\) and
the indices are \(M_0,16uh\).  Since \(M_0u=N_0\),

\[
 \frac{4\pi\sqrt{M_0(16uh)}}{4n}
 =\frac{4\pi\sqrt{N_0h}}{n}.                               \tag{A.10}
\]

An \(S/C\) formula requires \(4nA_g(n,h)\), together with the fixed factor
\(\chi _4(M_0)/\tau(\chi _4)\) and the level-\(4\) minus level-\(8\)
combination.  If the \(S/\sqrt C\) formulation of Theorem 1 is used, the
equivalent sample is \(\sqrt C\,A_g(n,h)\).  The candidate states all three
normalization boundaries correctly.

### 3.5 Linnik discreteness -- revise

After the fixed factors cancel between (A.10)'s index product and modulus,
the source range reduces to

\[
 0<h\ll H_{\rm Lin}(g)\asymp
 \frac{(R/g)^2}{N_0}
 \asymp\frac{X}{D^2g^2}
 =\frac{K}{Lg^2}.                                          \tag{A.11}
\]

The continuous ratio \(H_{\rm Lin}(g)/(R/g)\asymp1/(Dg)\) in
(143.C29) is correct.  The integer frequency count, however, satisfies only

\[
 \frac{\#\{1\le h<n:h\ll H_{\rm Lin}(g)\}}{R/g}
 \ll\frac1{Dg},                                             \tag{A.12}
\]

and is \(\asymp1/(Dg)\) only when \(H_{\rm Lin}(g)\gg1\), with support
constants fixed.  The candidate correctly uses
\(g\gg\sqrt{K/L}\) for the empty nonzero range, but it should add
(A.12) and label (143.C29) as a continuous scale ratio.  It should also
replace the exact-looking definition in (143.C28) by \(\asymp\), or state
that its right-hand side is merely the chosen comparison scale.

### 3.6 DI and ABL boundary -- revise

The candidate's short statements that DI uses a common sequence and ABL
uses controlled smooth two-variable dependence are true.  They are
insufficiently qualified for a final source-audit node.  Add the hypotheses
in Section 2.3 and the explicit disclaimers that DI is not itself the
needed odd-weight level-\(4/8\) large sieve and that ABL has neither the
\(\chi _4\) twist nor the BM level encoding.  With those additions, the
conclusion that the frozen controls provide no owner-saving admissible
representation is source-safe.

## 4. First doubtful or unproved step

No doubt remains in the candidate's Kıral--Young parity boundary,
Blomer--Milićević specialization, Gauss factor, level split, spectrum,
same-sign transforms, or \(2n/4n\) sample normalization.

The first source-reporting defect is the omission of the full
Deshouillers--Iwaniec and Assing--Blomer--Li hypotheses at the point where
their interface restrictions are invoked.  The first quantitative
qualification needed is the discrete Linnik count (A.12).  Neither defect
changes the mathematical obstruction.

After those repairs, the first genuinely unproved project step is exactly
the one identified by the candidate: no audited theorem supplies an
owner-saving common-test, common-sequence, or vector-valued estimate for
the fully gcd-restored nonzero-frequency matrix.  The moving inverse map
explains why that conclusion does not follow from row Parseval, but the
candidate correctly avoids claiming a universal factorization
impossibility.

## 5. Required controls and outcomes

1. **KY parity and weight -- pass.**  The even-character theorem is not
   applied to \(\chi _4\); weight zero is not promoted.
2. **BM character encoding -- pass.**  The arguments, Gauss factor,
   common \(\omega\), and Möbius signs in (143.C20) are exact.
3. **Level \(4\) versus level \(8\) -- pass.**  The standard-cusp route,
   cusp lists, and oldclasses are complete.
4. **Same-sign transforms -- pass.**  (143.C21)--(143.C22) match
   (A.5)--(A.6); no unsupported opposite-sign formula is added.
5. **Spectral ledger -- pass.**  The source prints \(H+M+E\); the candidate
   adds no residual or holomorphic weight-one term.
6. **\(2n\) versus \(4n\) samples -- pass.**  Equations (A.9)--(A.10)
   verify the Bessel argument and sample factors.
7. **Linnik range -- revise.**  The scale and
   \(g\gg\sqrt{K/L}\) cutoff pass; add the integer-count qualification
   (A.12) and the fixed-test hypotheses.
8. **DI common-sequence boundary -- revise metadata.**  Add the fixed cusp,
   \(T,N,Y\) conditions, and odd-weight source disclaimer.
9. **ABL smooth-matrix boundary -- revise metadata.**  Add
   \((r,s)=1\), positivity, support, all derivative bounds, the single
   \(\alpha_m\), (A.8), and the absent \(\chi _4\)/level encoding.
10. **Source-scope conclusion -- pass after those repairs.**  The claimed
    no-go is only from the frozen controls and is not a universal matrix
    impossibility.

All checks were analytical and source-comparative.  No numerical experiment
was used.

## 6. Dependencies and exact artifacts used

This audit used, without editing the candidate or shared state:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/conductor_0823_full_proof_strategy.md;
- candidates/conductor_round143_level_four_matrix_obstruction.md;
- reports/kuznetsov_source_hypothesis_audit.md;
- reviews/blind_post_unmask_source_hypothesis_audit.md;
- reviews/source_post_unmask_spectral_claims_audit.md; and
- reviews/discovery_conductor_candidate_seam_audit.md.

Every campaign-relative path above lies under
rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate.

Primary sources and exact locations:

1. E. M. Kıral and M. P. Young, arXiv:1710.00914: Definition 2.2 and
   (2.3), scaling rule (2.7), Theorem 2.7, and (2.20).
2. V. Blomer and D. Milićević, JEMS 17 (2015), 51--69: Theorem 1 and
   (1.2)--(1.3), character encoding (2.3)--(2.5), parity and oldclasses in
   Section 3, transforms and \(H+M+E\) in (4.1)--(4.11), singular-cusp
   criterion (5.1), and Theorem 4.
3. J.-M. Deshouillers and H. Iwaniec, Invent. Math. 70 (1982), 219--288:
   Theorems 2 and 5, printed pp.230 and 232.
4. E. Assing, V. Blomer, and J. Li, arXiv:2005.13915:
   Theorem 2.4, printed p.5.

The source links and transcribed theorem cards are recorded in
reports/kuznetsov_source_hypothesis_audit.md.  No sibling assertion was
used as a substitute for a primary source.

## 7. Recommended state effect and final verdict

**Final verdict: REVISE, then GREEN after the following source-only
amendments.**

1. Replace the unqualified Linnik proportion by (A.12), state that
   (143.C29) is the continuous scale ratio, and make
   \(H_{\rm Lin}(g)\) an \(\asymp\)-scale rather than an exact equality to
   the dyadic/source cutoff.
2. At the Linnik citation, add the fixed positive arguments, fixed
   arithmetic weight, fixed compact smooth test, normalized Mellin norm,
   and absence of a printed complementary-range theorem.
3. At the DI citation, add the fixed cusp, \(T\ge1\), \(N\ge1/2\),
   \(Y\ge1\) for Theorem 5, same-sequence support, and the disclaimer that
   the printed result is not the required odd-nebentypus weight-one
   level-\(4/8\) large sieve.
4. At the ABL citation, add positive \(n,r,s\), \((r,s)=1\),
   \(M,C,Z\ge1\), one sequence, support and all mixed-derivative bounds,
   (A.8), and the absence of the \(\chi _4\) twist and BM level encoding.

No repair is required to (143.C19a)--(143.C22), the level-\(4/8\)
spectrum ledger, or the \(2n/4n\) sample distinction.  After the four
amendments, the source portion is green for promotion as a scoped
source-boundary and matrix-interface obstruction.  Keep the quarter-bound
obligation and every downstream claim open.
