## 1. Result

**Verdict: GREEN.**  The isolated Nyquist-fold estimate

\[
 \mathcal F_U(V)\ll_{\varepsilon,A}M^{-1/4}X^\varepsilon
\]

is correct under the literal coefficient and endpoint hypotheses in the
allowed packet.  The unique nonzero self-complementary mode is
\(v=H/2=N/d\), its Fourier argument is exactly \(q/2\), complex discrete
Abel summation gives

\[
 |\widehat B_j(q/2)|\ll_\varepsilon
 M^{-3/4}X^\varepsilon,
\]

and demodulation by \((-1)^j\) produces only nonzero additive frequencies
\(c/2-u\).  The interval estimate remains valid for intervals longer
than \(c\), and restoring \(d\sqrt c/(Nq)\) gives exactly
\(M^{-1/4}\), with no residual power of \(N\), \(d\), \(c\), or \(V\).

The proof is genuinely signed.  Its essential input is the spatial
Nyquist character \((-1)^x\); replacing the alternating sum by an
unsigned spatial mass restores the support length \(K\) and does not
follow from this argument.

The verdict covers only the row (157.NF1).  It does not certify the
paired interior modes.  A later external scalar may be reinserted only
under its separately established \(X^\varepsilon\) bound; that external
bound is not part of the isolated row proved here.

## 2. Exact statement and hypotheses

The review uses

\[
 N=\lfloor X\rfloor,\qquad 1\ll M\le N^{1/2},\qquad
 K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,\qquad q=4N.
\]

For each odd \(d\mid N\), set

\[
 n={N\over d},\qquad c=4n={4N\over d},\qquad H={c\over2}=2n.
\]

The literal coefficient is

\[
 B_j(x)=
 \mathbf1_{x\ge1}\mathbf1_{-x\le j\le x-1}
 w_U\left({x^2-j\over N}\right)
 e\left(\sqrt{x^2-j}-x\right),
\tag{2.1}
\]

with the inherited off-congruence extension, all support components,
transitions, half-open choices, hard endpoints, and zero extension.  The
profile is real, but \(B_j\) is complex.  Put

\[
 a=M^{-3/4},\qquad
 \|w_U\|_\infty+\operatorname{Var}(w_U)
 \ll_\varepsilon aX^\varepsilon.
\tag{2.2}
\]

The endpoint source supplies only the endpoint facts used here: the
physical \(x\)-support has \(O(K)\) integer span, lies at \(x\asymp K\),
has no wrap in one residue system, and its profile-component and
zero-extension jumps are included in the total variation in (2.2).

Define

\[
 C_j=\widehat B_j(q/2)
 =\sum_{x\bmod q}(-1)^xB_j(x)
\tag{2.3}
\]

and let \(\mathcal F_U(V)\) be exactly (157.NF1).  No parity,
squarefree, primitivity, or coprimality assumption is made on \(N\) or
\(n\).

## 3. Proof or derivation

### 3.1 Nyquist normalization

The fixed points of \(v\mapsto-v\pmod H\) solve \(2v=0\pmod H\).
Because \(H=2n\), they are \(v=0\) and \(v=n\); hence \(v=n=H/2\) is the
unique nonzero fixed point.  Moreover

\[
 2dv=2d{N\over d}=2N={q\over2}.
\]

Using
\(e_c(-2vx)=e_q(-2dvx)\), its spatial character is

\[
 e_q\left(-{q\over2}x\right)=(-1)^x.
\]

Thus (2.3) and the normalization in (157.NF1) are exact.  This remains
true in the edge case \(c=4\), where \(H=2\) and the unique nonzero mode
is \(v=1\).

### 3.2 Literal complex spatial variation

Fix \(j\).  On positive \(x\), the map

\[
 x\longmapsto {x^2-j\over N}
\]

is increasing.  Sampling the zero-extended BV profile along a monotone
map cannot increase total variation, so every profile component,
transition, and zero-extension jump together costs at most
\(\operatorname{Var}(w_U)\).  No bound on the number of components is
used.

The cell indicator has exactly one possible spatial cutoff.  For
\(j>0\), it is \(x\ge j+1\); for \(j=-k<0\), it is \(x\ge k\).  Truncating
a BV sequence by either half-line adds at most a constant multiple of
its supremum.  The asymmetric endpoints are therefore charged exactly.

For

\[
 f_j(x)=\sqrt{x^2-j}-x
\]

one has

\[
 f_j'(x)=
 {j\over
 \sqrt{x^2-j}\bigl(x+\sqrt{x^2-j}\bigr)}.
\tag{3.1}
\]

On \(x\asymp K\), the literal cell and
\(|j|\le2V\le2K\) give
\(\sqrt{x^2-j}\asymp K\), hence

\[
 |f_j'(x)|\ll {V\over K^2}.
\]

Across the full \(O(K)\) physical span,
\(\operatorname{Var}_x(f_j)\ll V/K\ll1\).  Consequently
\(\operatorname{Var}_x(e(f_j))\ll1\).  The product-variation inequality,
the profile bound (2.2), and the single cell cutoff now yield

\[
 \sup_x|B_j(x)|+\operatorname{Var}_x(B_j)
 \ll_\varepsilon aX^\varepsilon.
\tag{3.2}
\]

This argument is valid for a complex product.  It neither replaces
\(B_j\) by its real profile nor assumes Fourier conjugacy.

Let \(P(t)=\sum_{x\le t}(-1)^x\).  Then \(|P(t)|\le1\), and discrete Abel
summation for the complex sequence \(B_j(x)\), including the first and
last nonzero cells, gives

\[
 |C_j|
 \le \sup_x|B_j(x)|+\operatorname{Var}_x(B_j)
 \ll_\varepsilon aX^\varepsilon.
\tag{3.3}
\]

### 3.3 Demodulation on both signed blocks

On either consecutive signed block define

\[
 D_j=(-1)^jC_j.
\]

For adjacent integers,

\[
 |D_{j+1}-D_j|
 =|C_{j+1}+C_j|
 \le |C_{j+1}|+|C_j|.
\]

Each block has \(O(V)\) integers.  Therefore (3.3) implies

\[
 \sup_j|D_j|+\operatorname{Var}_j(D_j)
 \ll_\varepsilon VaX^\varepsilon
 \le KaX^\varepsilon.
\tag{3.4}
\]

For the negative block, \((-1)^{-k}=(-1)^k\), and reversing the order of
the consecutive integers preserves variation.  Thus (3.4) covers both
signs.  Strict dyadic endpoints contribute only the standard two
supremum terms.

### 3.4 The nonzero twist and long intervals

Opening the kernel gives, for any consecutive integer interval \(I\),

\[
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 =
 \sum_{u\bmod c}^{*}
 \epsilon_u\left({c\over u}\right)e_c(-\bar u n^2)
 \sum_{j\in I}e_c((c/2-u)j).
\tag{3.5}
\]

For every unit \(u\bmod c\), the residue

\[
 r_u={c\over2}-u
\]

is nonzero and is itself a unit modulo \(c\).  It is odd at \(p=2\);
for every odd \(p\mid c\), one has
\(c/2\equiv0\pmod p\), so \(r_u\equiv-u\not\equiv0\pmod p\).
Translation by \(c/2\) therefore permutes the unit residues.

For an interval of length at most \(c\), the geometric-sum bound and a
harmonic summation over the distinct nonzero residues give

\[
 \sum_{u\bmod c}^{*}
 \left|\sum_{j\in I}e_c(r_uj)\right|
 \ll c\log(2c).
\tag{3.6}
\]

If \(|I|>c\), split it into complete blocks of length \(c\) and one
remainder.  Every complete block vanishes for each nonzero frequency
\(r_u\), so (3.6) remains unchanged.  Since all exterior factors in
(3.5) have modulus one,

\[
 \sup_I\left|
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 \right|
 \ll c\log(2c).
\tag{3.7}
\]

This includes \(c=4\), all powers of two, repeated odd prime powers, and
interval lengths that are exact multiples of \(c\).

### 3.5 Abel in \(j\), restored powers, and seam

Because \(C_j=(-1)^jD_j\), Abel summation using
(3.4) and (3.7), separately on the two signed blocks, gives

\[
 \left|\sum_{V<|j|\le2V}
 C_jK(-n^2,-j;c)\right|
 \ll_\varepsilon Ka\,cX^\varepsilon.
\tag{3.8}
\]

Restoring the literal outer factor before summing the divisor strata,

\[
 \begin{aligned}
 |\mathcal F_U(V)|
 &\ll_\varepsilon
 {Ka\over Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 d\,c^{3/2}X^\varepsilon\\
 &=
 {Ka\sqrt q\over N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 d^{-1/2}X^\varepsilon\\
 &\ll_\varepsilon
 {Ka\over\sqrt N}X^\varepsilon
 =a\sqrt M\,X^\varepsilon
 =M^{-1/4}X^\varepsilon.
 \end{aligned}
\tag{3.9}
\]

Here \(c=q/d\), \(q=4N\), \(K=\sqrt{NM}\), and the divisor count and
\(\log(2c)\) are absorbed into \(X^\varepsilon\).  Equation (3.9)
confirms every restored power and proves the isolated claim.

The external \(B_{1,U}(1)\) is absent from (157.NF1), so it is not used
in (3.9).  Reassembly with that scalar is a separate seam and is safe
only under its independently established \(X^\varepsilon\) estimate.

## 4. First doubtful or unproved step

No mathematical step in the isolated Nyquist-fold estimate remains
unproved under the stated literal and endpoint hypotheses.

The first open matrix term is the paired interior range

\[
 \sum_{v=1}^{H/2-1}
 \bigl(\widehat B_j(2dv)+\widehat B_j(-2dv)\bigr)
 K(-v^2,-j;c),
\]

summed over \(j\) and all odd \(d\mid N\).  The spatial character at a
general \(v\) does not have the fixed parity partial sums used in
(3.3), and estimating the frequencies separately restores a positive
power.

There is one external-seam qualification: the allowed literal row does
not contain \(B_{1,U}(1)\), and this review used the endpoint review only
for endpoint/support hypotheses.  Therefore the isolated verdict does
not independently certify the later bound on that external scalar.  It
must remain an explicit dependency when the larger expression is
assembled.

## 5. Required control tests and outcomes

1. **\(c=4\) edge case — PASS.**  Here \(H=2\), the only nonzero mode is
   \(v=1\), \(2dv=q/2\), and the two twisted frequencies are \(1\) and
   \(3\) modulo \(4\), never zero.
2. **Large two-adic and repeated-prime strata — PASS.**  For every
   \(c=4N/d\), \(c/2\) is even and \(c/2-u\) is a unit for every unit
   \(u\).  No squarefree or parity shortcut occurs.
3. **Intervals longer than \(c\) — PASS.**  Complete length-\(c\)
   periods vanish frequency by frequency; an interval of length
   \(Lc+r\) has exactly the cost of its remainder.
4. **Complex Abel — PASS.**  Abel uses absolute values and the complex
   BV norm (3.2); no realness or conjugacy is invoked.
5. **Arbitrarily many profile components — PASS.**  Monotone sampling of
   the single zero-extended BV profile charges their total variation,
   not their number.
6. **Asymmetric cell and strict endpoints — PASS.**  The spatial cutoffs
   are \(x=j+1\) for \(j>0\) and \(x=|j|\) for \(j<0\).  Each block has
   one cutoff and two Abel endpoints.
7. **Both signed blocks under demodulation — PASS.**
   \((-1)^{-k}=(-1)^k\), and reversal preserves the BV norm.
8. **Restored \(d,c,N,M\) ledger — PASS.**
   \(d\,c^{3/2}=q^{3/2}d^{-1/2}\), so normalization gives
   \(Ka/\sqrt N=a\sqrt M=M^{-1/4}\).
9. **Unsigned/adversarial analogue — PASS as a falsification.**  If
   \((-1)^x\) is removed before spatial Abel, the packet supplies only
   \(\sum_x|B_j(x)|\ll KaX^\varepsilon\).  The proof therefore does not
   establish the false unsigned analogue.
10. **External seam — CONDITIONAL PASS.**  The scalar is outside the
    isolated row.  Its reinsertion requires its separate
    \(X^\varepsilon\) theorem and is not silently included in this
    verdict.

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This review read and used exactly:

1. protocol.md;
2. rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/candidates/conductor_round157_nyquist_fold_target.md;
3. rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/blind_statement.md;
4. rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/hostile_profile_endpoint_round156_final.md, only for the endpoint and physical-support hypotheses explicitly identified in Section 2.

No graph, campaign state, strategy, proof draft, synthesis, sibling
Round-157 report, candidate dependency, web source, or computational
artifact was read or changed.

## 7. Recommended state effect

Promote the isolated estimate (157.NF2) as
\(\mathrm{proved\_internal}\), with its scope restricted to the unique
Nyquist-fold row (157.NF1).  Retain the literal complex spatial-BV lemma,
the two-block demodulation, and the nonzero-twist interval theorem as its
proof kernel.

Do not promote the paired interior frequencies or the full nonzero
matrix.  Keep the external scalar bound as an explicit downstream
dependency rather than part of this isolated review.

**Terminal verdict: GREEN.  First defect in the isolated row: none.**
