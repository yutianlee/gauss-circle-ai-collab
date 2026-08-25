# Round 157 conductor adjudication

- Campaign: m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate
- Round: 157
- Starting graph SHA-256: 3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea
- Terminal label: outer_defect_centered_discrepancy_no_go
- Terminal reviews: independent centered mathematics GREEN; independent Nyquist-fold mathematics GREEN; hostile profile, endpoint, power, and scope GREEN; independent source audit GREEN
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical

## 1. Result

Round 157 proves an exact centered form of the incomplete nonzero
theta projection and closes its unique self-complementary Nyquist row.
Put

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,
\tag{157.A1}
\]

and, for every odd \(d\mid N\), put

\[
 c=\frac{4N}{d},\qquad H=\frac c2,\qquad n=\frac Nd.
\tag{157.A2}
\]

If

\[
 G_N(t)=\mathbf 1_{N\mid t}\chi_4(t/N),\qquad
 A_j=\widehat B_j(0),\qquad
 B_j^\circ(x)=B_j(x)-\frac{A_j}{4N},
\tag{157.A3}
\]

then the full nonzero projection is exactly

\[
 \boxed{
 \mathcal T_{\ne0,U}(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod4N}
 B_j^\circ(x)G_N(x^2-j).}
\tag{157.A4}
\]

The nonzero frequency involution \(v\mapsto H-v\) has the unique fixed
point \(v=H/2=n\).  Its complete normalized contribution

\[
 \mathcal F_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,
 \widehat B_j(q/2)K(-n^2,-j;c)
\tag{157.A5}
\]

satisfies

\[
 \boxed{\mathcal F_U(V)
 \ll_{\varepsilon,A}M^{-1/4}X^\varepsilon.}
\tag{157.A6}
\]

The selected incidence count is also corrected to

\[
 L_U(V)\ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{157.A7}
\]

Thus a future genuine signed square-root incidence theorem would be
target-safe for every selected \(V\), not only
\(V\le M^{3/2}\).  Equation (157.A7) is an unsigned support count and
does not supply that theorem.

The terminal label is a qualified route no-go.  One-variable BV does
not imply the ideal mixed rectangular norm, and the audited completion,
fixed-frequency, Fourier-\(L^1\), Parseval, operator-norm, and current
source placements do not close the paired interior matrix.  These are
capacity or interface statements, not a lower bound and not a
mathematical impossibility theorem.

No complete positive-power defect range, broader owner, quarter
theorem, or global exponent changes.

## 2. Exact statement and hypotheses

On one nonwrapping residue lift modulo \(q=4N\), retain the literal
coefficient

\[
 B_j(x)=
 \mathbf 1_{x\ge1}\mathbf 1_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right),
\tag{157.A8}
\]

component by component, with the inherited off-congruence extension,
both defect signs, the asymmetric cell, strict dyadic mask, all
profile transitions, half-open choices, hard endpoints, and zero
extension.  The real profile and physical support obey

\[
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon M^{-3/4}X^\varepsilon,
 \qquad
 \operatorname {span}(\operatorname {supp}_x B_j)
 \ll KX^\varepsilon.
\tag{157.A9}
\]

The residual phase in (157.A8) is kept, so \(B_j\) is complex.  No
Fourier conjugacy is assumed.  There is no parity, squarefree,
primitivity, or coprimality hypothesis on \(N\) or \(N/d\), and every
odd divisor \(d\mid N\) remains in the normalized sum.

The external scalar \(B_{1,U}(1)\) is not part of (157.A4)--(157.A6).
It remains a separate accepted assembly seam of size
\(O_\varepsilon(X^\varepsilon)\).

## 3. Proof or derivation

### 3.1 Exact centering and orbit decomposition

The accepted complete half-period inversion is

\[
\begin{aligned}
 &-\frac{i(1+i)}{2Nq}
 \sum_j\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)\\
 &\hspace{32mm}
 =\sum_j\sum_{x\bmod q}B_j(x)G_N(x^2-j).
\end{aligned}
\tag{157.A10}
\]

Round 156 gives

\[
 \mathscr S_N(j):=\sum_{x\bmod q}G_N(x^2-j)
 =
 -\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,K(0,-j;c).
\tag{157.A11}
\]

The \(v=0\) term in (157.A10) is therefore exactly
\(q^{-1}\sum_jA_j\mathscr S_N(j)\).  Subtracting it once proves
(157.A4), with the constant \(q^{-1}=(4N)^{-1}\).  The global constant
tail has zero sampled Fourier coefficient at every nonzero mode; it is
controlled by the closed zero row, not by pointwise smallness.

For \(1\le v<H/2\), the two-element orbit contributes

\[
 \left(\widehat B_j(2dv)+\widehat B_j(-2dv)\right)
 K(-v^2,-j;c).
\tag{157.A12}
\]

The unique nonzero fixed point is \(v=H/2=n\), occurs once, and has
\(2dv=q/2\).  This proves the exact split into paired interior modes
and the fold (157.A5).

### 3.2 Literal spatial BV closes the Nyquist coefficient

For fixed \(j\), the map \(x\mapsto(x^2-j)/N\) is monotone on positive
physical support.  Hence the zero-extended sampled profile retains the
variation in (157.A9).  For

\[
 f_j(x)=\sqrt{x^2-j}-x
\]

one has

\[
 |f_j'(x)|
 =
 \left|
 \frac{j}
 {\sqrt{x^2-j}\bigl(x+\sqrt{x^2-j}\bigr)}
 \right|
 \ll\frac V{K^2}.
\tag{157.A13}
\]

Across the \(O(KX^\varepsilon)\) physical span this costs
\(O(X^\varepsilon)\), since \(V\le K\).  The cell adds one spatial
jump, and all other transitions and endpoints are already charged by
zero extension.  Product variation gives

\[
 \sup_x|B_j(x)|+\operatorname {Var}_x(B_j)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{157.A14}
\]

Partial sums of \((-1)^x\) are bounded.  Complex discrete Abel
summation therefore yields

\[
 C_j:=\widehat B_j(q/2)
 =\sum_{x\bmod q}(-1)^xB_j(x),
 \qquad
 |C_j|\ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{157.A15}
\]

This supersedes the blind report's provisional support-sized fold
obstruction.  Its alternating diagnostic violates the inherited
zero-extended spatial-BV hypothesis.  The blind report's exact
projector, complex orbit split, fold normalization, and low-frequency
warning remain valid.

### 3.3 Twisted interval theorem and restored powers

On either signed \(j\)-block put \(D_j=(-1)^jC_j\).  The crude
variation implied by (157.A15) is sufficient:

\[
 \sup_j|D_j|+\operatorname {Var}_j(D_j)
 \ll_\varepsilon K M^{-3/4}X^\varepsilon.
\tag{157.A16}
\]

Opening the fold kernel gives, for every consecutive interval \(I\),

\[
\begin{aligned}
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 &=
 \sum_{u\bmod c}^{*}
 \epsilon_u\left(\frac cu\right)e_c(-\bar u n^2)
 \sum_{j\in I}e_c((c/2-u)j).
\end{aligned}
\tag{157.A17}
\]

Because \(c/2\) is even and every unit \(u\) is odd,
\(c/2-u\) is a nonzero unit modulo \(c\).  Complete periods vanish,
including when \(|I|>c\), and geometric summation gives

\[
 \sup_I\left|
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 \right|
 \ll c\log(2c).
\tag{157.A18}
\]

Abel summation followed by restoration of every exterior factor yields

\[
\begin{aligned}
 |\mathcal F_U(V)|
 &\ll_\varepsilon
 \frac{K M^{-3/4}}{Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 d\,c^{3/2}X^\varepsilon\\
 &=
 \frac{K M^{-3/4}\sqrt q}{N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 d^{-1/2}X^\varepsilon
 \ll_\varepsilon M^{-1/4}X^\varepsilon.
\end{aligned}
\tag{157.A19}
\]

Here \(dc=q\), \(K=\sqrt{NM}\), and divisor and logarithmic factors are
absorbed into \(X^\varepsilon\).  This proves (157.A6), uniformly in
all divisor strata, including \(c=4\), and on both strict signed
blocks.

### 3.4 Corrected incidence capacity and remaining route bounds

On the selected graph \(j=k^2-Nm\), the asymmetric nearest cell is

\[
 k^2-k+1\le Nm\le k^2+k.
\tag{157.A20}
\]

The upper endpoint for \(k\) is followed by the lower endpoint for
\(k+1\), so these integer intervals partition the positive integers.
Each positive \(m\) determines one \(k\), hence one \(j\).  Intersecting
the \(O(M)\) physical \(m\)-support with the accepted
\(O_\varepsilon(VX^\varepsilon)\) root count proves (157.A7).  If, and
only if, a future theorem supplied signed square-root cancellation,

\[
 M^{-3/4}L_U(V)^{1/2}X^\varepsilon
 \le M^{-1/4}X^\varepsilon.
\tag{157.A21}
\]

The two obsolete Round 155 rejected-record explanations using only
\(L(V)\ll V\) must be corrected in the State Patch.

The centered report proves

\[
 \sup_{I,J}|\mathscr D_N(I,J)|
 \ll \sqrt N\,\tau(N)(\log(2N))^2.
\tag{157.A22}
\]

Even granting the ideal mixed norm, this restores
\(N^{1/2}M^{-3/4}X^\varepsilon\), outside \(M\le N^{1/2}\).
The moving-cell control model separately shows that the accepted
one-variable BV hypotheses alone permit a diagonal mixed-variation
capacity \(VM^{-3/4}X^\varepsilon\).  Fixed-\(v\) Abel, Fourier
\(L^1\), sampled Parseval, and generic nuclear-norm transfer retain
their documented positive powers.  These statements calibrate only
the named methods.

The source audit finds no primary theorem through 25 August 2026 that
matches the fixed arbitrary even composite theta multiplier, the
entrywise coefficient \(\widehat B_j(2dv)\), every odd divisor stratum,
the paired interior cutoff, signs, folds, and endpoints.  DFI Lemma
6.1 remains the exact pointwise kernel theorem.  Current fixed-modulus
bilinear results use ordinary, prime, odd-squarefree, or prime-square
kernels and separated weights; half-integral Kuznetsov formulas average
moduli and retain all spectral pieces.  This is a dated direct-interface
no-match, not a literature impossibility result.

## 4. First doubtful or unproved step

There is no unproved step in the promoted centering identity,
complementary-orbit split, Nyquist-fold theorem, or corrected incidence
count under the printed hypotheses.

The first open literal object is the paired interior matrix

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{1\le v<H/2}
 \left(\widehat B_j(2dv)+\widehat B_j(-2dv)\right)
 K(-v^2,-j;c).
\tag{157.A23}
\]

It requires a joint mask-preserving signed estimate, or an exactly
equivalent selected signed incidence theorem, retaining the literal
profile, complex residual phase, diagonal cell trace, both defect
signs, all transitions, strict endpoints, every odd \(d\), and the
external scalar seam.  No current report proves that estimate.

## 5. Required control tests and outcomes

All campaign controls are GREEN or correctly classified as no-match.

- Exact projector and centering: GREEN.  The \(v=0\) row is subtracted
  exactly once and the constant is \(1/(4N)\).
- Constant tail: GREEN.  It is exactly the closed zero row and vanishes
  at every sampled nonzero Fourier mode.
- Complex complementary representatives: GREEN.  The range is
  \(1\le v<H/2\); coefficients add without an assumed conjugacy.
- Unique fold, \(c=4\), and all divisor strata: GREEN.
- Literal profile, residual phase, transitions, signs, and endpoints:
  GREEN.
- Fold interval theorem and \(N,M,V,d,c\) ledger: GREEN, with only
  \(M^{-1/4}X^\varepsilon\) remaining.
- Selected incidence count: GREEN as support cardinality; no signed
  square-root theorem is inferred.
- Mixed variation, completion, fixed-frequency, Fourier, Parseval, and
  operator placements: GREEN as route-scoped capacities only.
- Source interface: GREEN no-match through the stated cutoff.
- External scalar and downstream quarantine: GREEN.  No result is
  transferred beyond the frozen \(D=d=L=1\) row.

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

The accepted package depends on the Round 154 literal ambient profile,
the Round 155 normalized theta completion, and the Round 156 zero-row
theorem.  Its direct Round 157 evidence is:

- centered_nonzero_root_discrepancy_attack.md;
- blind_nonzero_cross_fibre_rederivation.md;
- nonzero_theta_matrix_source_audit.md;
- conductor_round157_nyquist_fold_target.md;
- m9_m1_d1_nonzero_centering_nyquist_fold.md;
- independent_centered_math_round157.md;
- independent_nyquist_fold_round157.md;
- hostile_profile_scope_round157.md; and
- independent_source_round157.md.

The blind report is retained only for the exact identities and controls
explicitly accepted above; its final fold obstruction is superseded.
The source report's DFI test-function and Frobenius-pairing precision
corrections are incorporated before closure.  No subagent edited the
proof graph, proof draft, validation matrix, synthesis, State Patch, or
campaign state.

## 7. Recommended state effect

Apply a State Patch that:

1. creates a route-scoped proved-internal node containing the exact
   centering, orbit decomposition, Nyquist-fold theorem, corrected
   incidence capacity, and qualified method frontier;
2. adds that node only to the \(D=d=L=1\) outer-defect frontier and the
   global lower-radial dependency list;
3. corrects the two stale Round 155 incidence-capacity rejected records
   to use \(\min(M,V)\), while recording that no signed theorem exists;
4. rejects double zero-row subtraction, false Fourier conjugacy,
   double-counting the fold, the support-sized Nyquist obstruction,
   unlicensed mixed-BV, completion, fixed-frequency, Parseval,
   operator-norm, source-match, and downstream inferences;
5. leaves the paired interior matrix (157.A23), every complete
   positive-power D=1 range, \(D>1\), \(L>1\), generic \(t=1\), every
   \(t\ge2\) layer, cross, remaining M1, all M2, endpoint uniformity,
   M9, and the bridge open; and
6. leaves the quarter target, the strongest internally proved global
   exponent \(1/3\), and the separately audited external Li--Yang
   exponent unchanged.
