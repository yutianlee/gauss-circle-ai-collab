## 1. Result

**Revise; do not promote the source report as written.**  Its main source
calculation passes: Blomer--Milićević (BM) gives the exact legal
odd-character encoding as a level-\(4\) term minus a level-\(8\) term, and the
same-sign Bessel argument agrees exactly with the frozen ordinary and
cross-cusp arguments.  The sourced BM spectrum is \(H+M+E\).  At level \(8\)
it includes oldclasses lifted from level \(4\), and its continuous term ranges
over all four singular cusps.

Two defects block promotion.

1. The audited scalar, common-sequence, and smooth-matrix theorems do not
   accept the literal joint coefficient with an owner-saving norm justified
   by the frozen data.  This proves a source-hypothesis gap.  It does not prove
   the categorical nonexistence of a smooth extension, low-rank
   factorization, useful projective norm, or future vector-valued theorem.
2. The report proves that the \(h=0\) owner contribution is
   \(O(X^\varepsilon)\), but then says that no strictly smaller
   owner-complete survivor exists and that the whole wave is minimal.  The
   strict unresolved survivor is the fully gcd-restored
   \(h\not\equiv0\pmod n\) matrix; the \(h=0\) term is target-safe.

The capacity algebra passes pointwise on the strict residual polytope.  The
Linnik fraction and cutoff require discrete and dyadic qualifications, and
the DI and ABL source cards require several omitted hypotheses.

## 2. Exact statement and hypotheses

Put

\[
 u=(N_0,4^\infty)=2^{v_2(N_0)},\qquad M_0=N_0/u.
\]

For every finitely supported weight \(\omega\) (or a weight satisfying the
decay in BM (2.3)), BM (2.3) gives exactly

\[
 \sum_{n\ {\rm odd}}\chi _4(n)S(N_0,h;n)\omega(n)
 =\frac{\chi _4(M_0)}{\tau(\chi _4)}
 \left(\sum_{4\mid C}-\sum_{8\mid C}\right)
 S_{\chi _4}(M_0,16uh;C)\omega(C/4).                 \tag{2.1}
\]

The nonzero Möbius terms are \(d=1,2\), of signs \(+1,-1\), while
\(\mu(4)=0\); hence the difference selects \(C=4n\) with \(n\) odd.  For
\(h>0\), its same-sign Bessel arguments satisfy

\[
 \frac{4\pi\sqrt{M_0(16uh)}}{4n}
 =\frac{4\pi\sqrt{N_0h}}{n}
 =\frac{4\pi\sqrt{(4N_0)h}}{2n}.                    \tag{2.2}
\]

Thus the Gauss factor, level-\(4\) minus level-\(8\) sign, and every power of
\(2\) in (2.1)--(2.2) are exact.  They do not source a pure-level-\(4\),
weight-one switched-cusp trace formula.

The omitted or blurred source hypotheses must be restored as follows.

- BM Theorem 1 has a fixed arithmetic weight
  \(f:(\mathbb Z/q\mathbb Z)^*\to\mathbb C\), one fixed smooth compactly
  supported \(f_\infty\), positive fixed Fourier arguments, and
  \(mn\le C_0^2\).  Its \(\|\widehat f\|_1\) is the normalized
  \(q\)-Mellin norm defined in BM (1.2).  The theorem permits the fixed
  \(\chi_4\) arithmetic weight, but no additional arbitrary
  modulus-frequency matrix at no cost.
- DI Theorem 2 assumes a cusp \(\mathfrak a\) of \(\Gamma_0(q)\),
  \(T\ge1\), \(N\ge1/2\), \(\varepsilon>0\), and one sequence
  \((a_n)_{N<n\le2N}\).  Each of its holomorphic, Maaß, and Eisenstein forms
  uses that same sequence and is bounded by
  \[
   \bigl(T^2+\mu(\mathfrak a)N^{1+\varepsilon}\bigr)
   \|a_N\|_2^2.                                      \tag{2.3}
  \]
  DI Theorem 5 additionally assumes its exceptional weight parameter
  \(Y\ge1\).  These are accurate interface comparisons, but DI's printed
  theorem is not itself the odd-nebentypus, weight-one, BM level-\(4/8\)
  large sieve needed here.
- ABL Theorem 2.4 assumes positive integers \(n,r,s\) with \((r,s)=1\),
  parameters \(M,C,Z\ge1\), a function supported on
  \([M,2M]\times[C,2C]\) satisfying every displayed mixed-derivative bound,
  one sequence \(\alpha_m\), and
  \[
    \frac{\sqrt{Mn}}{s\sqrt r\,C}\ll Z.               \tag{2.4}
  \]
  The claimant's displayed ABL sum and bound (2.17)--(2.18) match the
  source.  What is missing is a controlled representation of the frozen
  matrix as \(\alpha_hF(h,c)\).

For a fixed gcd row put \(C_g\asymp R/g\).  The BM Linnik condition is

\[
 0<h\ll H_{\rm Lin}(g):=\frac{C_g^2}{N_0}
 \asymp\frac{X}{D^2g^2}=\frac{K}{Lg^2}.              \tag{2.5}
\]

The proportion of positive residue representatives covered is
\(\ll1/(Dg)\), and is \(\asymp1/(Dg)\) only while
\(H_{\rm Lin}(g)\gg1\) with the dyadic constants fixed.  The range has no
nonzero integer once

\[
 g\gg\sqrt{K/L}.                                      \tag{2.6}
\]

The literal inequality \(g>\sqrt{K/L}\) is not justified without fixing all
support constants.  Parseval supplies no localization into (2.5).

## 3. Proof or derivation and seam verdicts

1. **BM level-\(4\) minus level-\(8\) identity -- pass.**  Substituting
   \(q=q_1=4\), \(m=N_0\), \(n=h\), \(m_0=M_0\), and \(n_0=uh\)
   into BM (2.3) gives (2.1).  The factor \(16uh\), the Gauss factor, and
   the relative minus sign must remain.

2. **Bessel scaling -- pass for \(h>0\).**  Equation (2.2) checks the exact
   scaling.  The claimant should append “for the positive-index same-sign
   formula.”  The zero index is arithmetic.  A negative centered index must
   be replaced rowwise by its positive residue representative unless a
   separately sourced opposite-sign theorem is supplied.

3. **DI common-sequence seam -- pass as an interface audit; revise source
   scope.**  The same \(a_n\) occurs in all three DI Theorem 2 forms and in
   Theorem 5's exceptional form.  Add the hypotheses in Section 2 and state
   explicitly that DI does not itself furnish the required odd-character,
   weight-one level-\(4/8\) large sieve.

4. **ABL smooth-matrix seam -- formula pass; categorical conclusion fail.**
   On a top-frequency block \(M\asymp C\asymp R/g\), with fixed
   Kloosterman argument \(N_0\asymp X\) and fixed level parameters, (2.4)
   forces \(Z\gg\sqrt{Dg}\).  But a finite matrix can be smoothly
   interpolated, and one can choose a trivial \(h\)-sequence.  What is not
   proved is an interpolation or factorization with derivative and aggregate
   norms small enough to save the owner.  Replace “does not factor” and
   “directly obstructs” by “the frozen statement supplies no controlled
   factorization or extension satisfying the theorem with an owner-saving
   norm.”

5. **Linnik fraction -- revise.**  The scale (2.5) passes.  The unconditional
   coverage statement is \(\ll1/(Dg)\); the claimant's \(\asymp\) fails
   after fewer than one positive integer remains.  Replace
   \(g>\sqrt{K/L}\) by (2.6).

6. **Singular cusps and oldclasses -- pass.**  BM's criterion
   \(4\mid[w,Q/w]\) gives only \(\infty,0\) at \(Q=4\), and gives
   \(\infty,0,1/2,1/4\) at \(Q=8\).  Primitive conductor \(4\) leaves no
   proper oldspace in the pure level-\(4\) space.  The level-\(8\) term in
   (2.1) contains level-\(8\) newforms and oldclasses lifted from level \(4\).
   The same-sign ledger is precisely \(H+M+E\), including exceptional
   parameters, \(t=0\) if present, and every singular-cusp Eisenstein family.
   No separate residual term is printed.

7. **Capacity algebra -- pass pointwise; revise uniformity wording.**  The
   positive Hilbert/Weil closure has exponent
   \[
     R\sqrt\Delta=X^{1-(\delta+\ell)/2},
   \]
   and its excess over \(\Delta=X^{\delta-\ell}\) is
   \[
     1-\frac{3\delta}{2}+\frac\ell2>\frac14.
   \]
   Also \(\delta+\ell<3/4\), so the closure exponent is \(>5/8\) and its
   gap above the quarter target is \(>3/8\).  These hold at each fixed point
   of the strict polytope, but no uniform extra margin beyond the strict
   boundary values follows.

8. **Owner minimality -- fail.**  The claimant correctly proves an
   \(O(X^\varepsilon)\) \(h=0\) contribution.  Therefore its statements that
   there is no strict survivor and that the whole wave is minimal are false.
   Replace the complete \(h\bmod n\) sum by
   \(h\not\equiv0\pmod n\), retaining every \(g\)-stratum and literal
   coefficient.  Positive representatives keep this survivor in the sourced
   same-sign setting.

9. **Source-use and TeX seam -- source wording revise; typography pass.**  I
   found no unbalanced display delimiter, malformed TeX command, control byte,
   or brace defect in the claimant.  Its equations (2.11)--(2.18) match the
   cited sources modulo harmless variable renaming.  The missing DI/ABL
   hypotheses, BM's undefined normalized \(\widehat f\)-norm in (2.14), and
   the words “cannot”, “does not factor”, and “whole wave” are source or logic
   overclaims, not typesetting defects.  The pure-level-\(4\) identity (1.1)
   remains an internal claimant lemma; Kıral--Young's even-character theorem
   does not certify its weight-one spectral continuation.  The independent
   legal source route is (2.1).

## 4. First doubtful or unproved step

After the exact BM encoding, the first unproved step is not the arithmetic or
Bessel normalization.  It is the assertion that the samples

\[
 W\!\left(\frac{X}{gnD}\right)\widehat\gamma_{g,n}(h)
\]

can enter a scalar Kuznetsov estimate or spectral large sieve with a common
test or sequence and with total Sobolev, spectral-bandwidth, or projective
cost below the accepted owner envelope.  The inverse selector and moving
support explain why no such control follows from Parseval; they do not prove
that every controlled interpolation or matrix theorem is impossible.

The rigorous conclusion is:

> None of the audited source theorems applies to the literal matrix with an
> owner-saving norm justified by the frozen hypotheses.

This failure occurs before estimating \(H\), \(M\), or \(E\).  A
pure-level-\(4\) switched-cusp formula, an exact opposite-sign weight-one
transform, or an added residual term is not supplied by the audited sources.

## 5. Required control tests and outcomes

1. **Exact character encoding:** pass for the BM standard-cusp identity
   (2.1); the pure-level-\(4\) cross-cusp identity remains internal.
2. **Moduli, Gauss factor, and Bessel root:** pass, with \(h>0\) stated.
3. **DI common-sequence hypotheses:** revise by adding
   \(T\ge1\), \(N\ge1/2\), \(Y\ge1\), the fixed cusp, and the
   odd-nebentypus applicability caveat.
4. **ABL smooth-matrix hypotheses:** revise by adding positivity,
   \((r,s)=1\), every mixed-derivative bound, and by weakening impossibility
   to absence of a controlled factorization in the frozen data.
5. **Linnik coverage:** revise \(\asymp\) to \(\ll\) outside the
   many-integer range and use \(g\gg\sqrt{K/L}\).
6. **Complete spectral ledger:** pass for sourced same-sign BM \(H+M+E\),
   including level-\(8\) oldclasses and every singular cusp.
7. **Full-polytope power ledger:** pass pointwise; remove any implication of a
   polytope-uniform extra margin.
8. **\(h=0\) control:** pass as target-safe; consequently the survivor must be
   \(h\ne0\).
9. **Literal coefficient geometry:** fail as a licensed source input, but do
   not promote categorical nonfactorization or SVD lower bounds.
10. **Downstream scope:** pass.  The audit concerns only the frozen
    flat-smooth strict-UNBAL owner.

## 6. Dependencies and exact artifacts used

This review used:

- protocol.md;
- the claimant report
  rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/kuznetsov_source_hypothesis_audit.md;
- BM, *Kloosterman sums in residue classes*, especially (1.2)--(1.3),
  (2.3)--(2.5), Section 3, (4.1)--(4.6), (5.1), and Theorem 4;
- Deshouillers--Iwaniec, *Kloosterman Sums and Fourier Coefficients of Cusp
  Forms*, Theorems 2 and 5, checked against the official GDZ scans of printed
  pp.230 and 232;
- Assing--Blomer--Li, *Uniform Titchmarsh divisor problems*, Theorem 2.4; and
- Kıral--Young, *Kloosterman sums and Fourier coefficients of Eisenstein
  series*, Theorem 2.7 and (2.20), only for the even-character attribution
  boundary.

No sibling conclusion was used to certify an external theorem.  The internal
pure-level-\(4\) cross-cusp identity was assessed only in the conditional role
assigned by the claimant.  All work was analytical and source-comparative; no
numerical experiment was used.

## 7. Recommended state effect

**Revise; no promotion from the source report as written.**  After the exact
repairs above, the following narrower content is promotable:

- the exact legal BM level-\(4\) minus level-\(8\) identity (2.1) and
  positive same-sign Bessel scaling (2.2);
- the complete sourced \(H+M+E\) ledger, with pure level \(4\) distinguished
  from the level-\(8\) oldclasses;
- the source-hypothesis obstruction that BM, DI, and ABL furnish no
  owner-saving estimate for the literal joint coefficient under the supplied
  controls; and
- the Linnik gap (2.5)--(2.6) and the pointwise capacity ledger.

Do not promote a categorical matrix/SVD impossibility, a custom
pure-level-\(4\) or opposite-sign spectral formula, a residual term, or the
claim that the whole wave is the smallest survivor.  The owner-complete
unresolved object is the fully gcd-restored
\(h\not\equiv0\pmod n\) matrix; the \(h=0\) term is a proved target-safe
complement.  The broader obligation remains open.
