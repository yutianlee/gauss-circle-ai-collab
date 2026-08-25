# Round 157 hostile profile, fold, endpoint, power, and scope review

- Campaign: m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate
- Round: 157
- Role: terminal hostile profile and scope reviewer
- Starting graph SHA-256: 3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea
- Allocation: 100% analytic and algebraic; 0% numerical

## 1. Result

**Terminal verdict: GREEN.**

The proposed Round 157 closure is sound with two sharply separated
conclusions.

First, the exact nonzero projection is the centered physical selector

\[
 \mathcal T_{\ne 0,U}(V)
 =
 \sum_{V<|j|\leq 2V}\sum_{x\bmod q}
 \left(B_j(x)-\frac{\widehat B_j(0)}q\right)G_N(x^2-j),
 \qquad q=4N.
\tag{157.H1}
\]

The moving-cell and completion conclusions attached to (157.H1) are
route-scoped no-go statements: the accepted one-variable profile data
do not imply the ideal mixed rectangular norm, and ordinary centered
completion, separated fixed-frequency Abel summation, Fourier
\(L^1\), and sampled Parseval restore the stated positive powers. None
of these statements is a lower bound for the literal matrix or an
impossibility theorem for a future joint signed argument.

Second, the unique self-complementary Nyquist mode is not an
obstruction. For every odd \(d\mid N\), with

\[
 c=\frac{4N}{d},\qquad H=\frac c2,\qquad n=\frac Nd,
\]

the single nonzero fixed point is \(v=H/2=n\), and its full normalized
row satisfies

\[
 \mathcal F_U(V)\ll_{\varepsilon,A}M^{-1/4}X^\varepsilon.
\tag{157.H2}
\]

The blind report's provisional support-sized fold obstruction is
superseded by the literal spatial-BV input available in the full
campaign packet. Its diagnostic alternating profile does not satisfy
the inherited \(O(M^{-3/4}X^\varepsilon)\) zero-extended profile
variation. The blind report's exact quotient projector, complementary
orbit split, and fold normalization remain useful; its inference that
the fold itself is the first open row does not.

The first open object is therefore the paired interior-frequency matrix
with representatives \(1\leq v<H/2\). No full nonzero target, strict
positive-power range, broader M1 or M2 owner, endpoint assembly, M9
theorem, bridge, quarter theorem, or global exponent follows.

## 2. Exact statement and hypotheses

Retain

\[
 1\ll M\leq N^{1/2},\qquad
 K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\leq K,\qquad q=4N.
\tag{157.H3}
\]

For every odd \(d\mid N\), put \(c=q/d\), \(H=c/2\), and
\(n=N/d\). No parity, squarefree, primitivity, or coprimality
hypothesis is imposed on \(N\), \(n\), or the odd divisor stratum.

On its unique nonwrapping physical lift, the literal coefficient is

\[
 B_j(x)=
 \mathbf 1_{x\geq1}\mathbf 1_{-x\leq j\leq x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right).
\tag{157.H4}
\]

The real profile is extended by zero with all of its actual components,
transitions, half-open choices, and hard support endpoints, and it
satisfies

\[
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon aX^\varepsilon,
 \qquad a=M^{-3/4}.
\tag{157.H5}
\]

Its total physical integer span is \(O(KX^\varepsilon)\). The
coefficient \(B_j\) is complex because its residual phase is retained.
No Fourier conjugacy is assumed.

The strict signed defect blocks are treated separately. On the positive
block, the cell is \(x\geq j+1\). On the negative block, it is
\(x\geq-j\). Thus each fixed \(j\) has one spatial cell cutoff, while
the zero-extended profile accounts for every other component,
transition, and support endpoint. Zero extension in \(j\) accounts for
the two strict dyadic block endpoints.

Define

\[
 A_j=\widehat B_j(0),\qquad
 B_j^\circ(x)=B_j(x)-\frac{A_j}{q},\qquad
 G_N(t)=\mathbf 1_{N\mid t}\chi_4(t/N).
\tag{157.H6}
\]

The constant tail in \(B_j^\circ\) is global in \(x\); it is not a
physical support truncation. The external factor \(B_{1,U}(1)\) is not
part of the frozen matrix or of \(\mathcal F_U(V)\). Its later
reinsertion is a separate accepted seam with
\(B_{1,U}(1)\ll_\varepsilon X^\varepsilon\).

## 3. Proof or derivation

### 3.1 Centering and the constant tail

The accepted complete half-period inversion and the accepted Round 156
zero-row recombination show that the \(v=0\) contribution is exactly

\[
 \frac1q\sum_j A_j\mathscr S_N(j),
 \qquad
 \mathscr S_N(j)=\sum_{x\bmod q}G_N(x^2-j).
\]

Subtracting it once gives (157.H1). For every sampled nonzero mode,

\[
 2dv\equiv0\pmod q
 \quad\Longleftrightarrow\quad
 v\equiv0\pmod H.
\]

Consequently the global constant tail has zero sampled Fourier
coefficient at every \(v\ne0\). It also has zero cyclic
\(x\)-difference, including across the zero-extended \(j\)-endpoints:

\[
 \Delta_j\Delta_x\left(\frac{A_j}{q}\right)=0.
\tag{157.H7}
\]

In particular, at the Nyquist argument \(q/2\),

\[
 \sum_{x\bmod q}\frac{A_j}{q}(-1)^x=0.
\]

Thus centering neither deletes nor changes the fold or any paired
interior coefficient. Its physical mass is accounted for exactly by
the already closed zero row.

### 3.2 Hostile profile and endpoint audit of the fold

For fixed \(j\), the map

\[
 x\longmapsto\frac{x^2-j}{N}
\]

is monotone on positive physical support. Sampling the single
zero-extended BV profile along this map cannot increase its total
variation. This charges all profile components and transitions without
assuming that their number is bounded.

For

\[
 f_j(x)=\sqrt{x^2-j}-x,
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
\tag{157.H8}
\]

The positive cell ensures that the radicand remains
\(\asymp K^2\); for negative \(j\) it is larger. Across the total
\(O(KX^\varepsilon)\) span, the phase variation is
\(O(X^\varepsilon)\), since \(V\leq K\). Multiplication by the
profile and by the one half-line cell cutoff therefore gives, on both
signed blocks,

\[
 \sup_x|B_j(x)|+\operatorname {Var}_x(B_j)
 \ll_\varepsilon aX^\varepsilon.
\tag{157.H9}
\]

Every half-open profile endpoint and zero-extension jump is already in
\(\operatorname {Var}(w_U)\); the nearest cell adds only its one
literal cutoff. Hence no hidden component-count, support-length, or
endpoint factor occurs in (157.H9).

The Nyquist coefficient is

\[
 C_j=\widehat B_j(q/2)=\sum_{x\bmod q}(-1)^xB_j(x).
\]

Partial sums of \((-1)^x\) have absolute value at most one. Complex
discrete Abel summation applied to (157.H9), with the first and last
physical cells included, gives

\[
 |C_j|\ll_\varepsilon aX^\varepsilon.
\tag{157.H10}
\]

This is the precise point that defeats the blind report's provisional
fold obstruction. The diagnostic profile
\(a(-1)^x\mathbf 1_I(x)\), after removal of the residual phase, has
variation \(\asymp a|I|\), not \(O(a)\), and is not the inherited
literal BV profile. Its support-sized alternating mass is therefore
not a counterexample to (157.H10). By contrast, the blind report's
low-frequency coherent-band diagnostic remains a valid warning for
general small \(v\); it does not contradict the special Nyquist
cancellation.

On either signed block put \(D_j=(-1)^jC_j\). There are \(O(V)\)
consecutive integers in each block, so

\[
 \sup_j|D_j|+\operatorname {Var}_j(D_j)
 \ll_\varepsilon VaX^\varepsilon
 \leq KaX^\varepsilon.
\tag{157.H11}
\]

For the negative block, \((-1)^{-k}=(-1)^k\), and reversal preserves
variation. The two strict endpoints contribute only the usual
supremum terms in Abel summation.

### 3.3 Exact orbit split and twisted kernel

Since \(H=2n\), the involution \(v\mapsto H-v\) on nonzero residues
has exactly one fixed point, \(v=n=H/2\). Every other orbit is
represented exactly once by

\[
 1\leq v<\frac H2,
\]

and contributes

\[
 \bigl(\widehat B_j(2dv)+\widehat B_j(-2dv)\bigr)
 K(-v^2,-j;c).
\tag{157.H12}
\]

There is no conjugacy or doubled-real-part simplification because
\(B_j\) is complex. The fixed point occurs once, has
\(2dv=q/2\), and contributes \(C_jK(-n^2,-j;c)\). When \(c=4\),
\(H=2\), the paired interior range is empty and this single fold is the
entire nonzero fibre.

Opening the kernel after demodulation gives, for every consecutive
integer interval \(I\),

\[
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 =
 \sum_{u\bmod c}^{*}
 \epsilon_u\left(\frac cu\right)e_c(-\bar u n^2)
 \sum_{j\in I}e_c((c/2-u)j).
\tag{157.H13}
\]

For every unit \(u\bmod c\), the residue \(c/2-u\) is a unit and is
nonzero modulo \(c\). Indeed it is odd at \(2\), and for every odd
prime \(p\mid c\), it is congruent to \(-u\pmod p\).
Translation by \(c/2\) permutes the unit residues. Geometric summation
and a harmonic sum therefore yield

\[
 \sup_I\left|
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 \right|
 \ll c\log(2c).
\tag{157.H14}
\]

If \(|I|>c\), every complete length-\(c\) period vanishes
frequency by frequency, so only the remainder is charged. This covers
arbitrary two-adic valuation, repeated odd prime powers, and the edge
case \(c=4\). Unlike the blind parity classification of the fold
kernel, this proof needs no transfer from the zero row and treats odd
and even \(N\) uniformly.

### 3.4 Complete power restoration

Abel summation using (157.H11) and (157.H14) gives, for one odd
\(d\mid N\),

\[
 \left|
 \sum_{V<|j|\leq2V}C_jK(-n^2,-j;c)
 \right|
 \ll_\varepsilon Ka\,cX^\varepsilon.
\tag{157.H15}
\]

Restoring the full exterior factor before the divisor sum gives

\[
\begin{aligned}
 |\mathcal F_U(V)|
 &\ll_\varepsilon
 \frac{Ka}{Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 d\,c^{3/2}X^\varepsilon\\
 &=
 \frac{Ka\sqrt q}{N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 d^{-1/2}X^\varepsilon\\
 &\ll_\varepsilon
 \frac{Ka}{\sqrt N}X^\varepsilon
 =a\sqrt M\,X^\varepsilon
 =M^{-1/4}X^\varepsilon.
\end{aligned}
\tag{157.H16}
\]

Here \(dc=q=4N\), \(K=\sqrt{NM}\), and the divisor and logarithmic
costs are absorbed into \(X^\varepsilon\). There is no residual
\(N\), \(d\), \(c\), or \(V\) power. Treating the two signs separately
changes only an absolute constant.

For the unresolved interior modes, the centered report's ledgers remain
upper capacities:

\[
\begin{array}{c|c}
\text{placement}&\text{restored capacity}\\ \hline
\text{Fourier }L^1\text{ plus pointwise theta bound}
 & aV X^\varepsilon\\
\text{fixed-}v\text{ Abel under the explicitly idealized norm}
 & a\min(V,\sqrt N)X^\varepsilon\\
\text{sampled Parseval and absolute Cauchy}
 & V\left(N^{1/4}M^{-1/2}+M^{-1/4}\right)X^\varepsilon\\
\text{ideal mixed norm plus ordinary centered completion}
 & N^{1/2}M^{-3/4}X^\varepsilon.
\end{array}
\tag{157.H17}
\]

The last quantity reaches the campaign's \(O(X^\varepsilon)\) block
scale only at \(M\geq N^{2/3-o(1)}\), outside
\(M\leq N^{1/2}\). The table states what those particular placements
can certify; it is not a claim that the literal signed matrix attains
these sizes or that every joint method must lose the same powers.

### 3.5 Incidence capacity versus a signed theorem

On the selected graph, \(j=k^2-Nm\), and the exact asymmetric cell is

\[
 k^2-k+1\leq Nm\leq k^2+k.
\tag{157.H18}
\]

The upper endpoint for \(k\) is immediately followed by the lower
endpoint for \(k+1\), so these integer intervals partition the
positive integers. Each positive \(m\) therefore determines one
\((k,j)\). The dyadic profile gives \(O(M)\) possible \(m\), while
the accepted root count independently gives
\(O_\varepsilon(VX^\varepsilon)\) selected incidences. Hence, for the
union of the two signs,

\[
 L_U(V)\ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{157.H19}
\]

This is an unsigned cardinality theorem. It does not imply cancellation.
If a future theorem proved square-root cancellation for the actual
weighted, signed literal incidences, including their profile,
transitions, phase, cells, and endpoints, then its capacity would be

\[
 aL_U(V)^{1/2}X^\varepsilon
 \leq aM^{1/2}X^\varepsilon
 =M^{-1/4}X^\varepsilon
\tag{157.H20}
\]

for every allowed \(V\). Thus the older conditional restriction
\(V\leq M^{3/2}\) is obsolete at the selected-incidence level.
Equation (157.H20) is conditional power bookkeeping, not the missing
signed theorem.

### 3.6 External seam and downstream quarantine

The frozen matrix and fold row omit \(B_{1,U}(1)\) exactly once. The
accepted Round 154 seam gives

\[
 B_{1,U}(1)\ll_\varepsilon X^\varepsilon.
\]

Reinserting it later multiplies (157.H2) by only another
\(X^\varepsilon\), which is absorbed by relabelling epsilon. It creates
no \(N\), \(M\), \(V\), \(d\), profile, or endpoint power and is not a
function of \(j\). This review does not reprove that external estimate;
it keeps it as an explicit accepted dependency.

Neither (157.H1), (157.H2), the route capacities (157.H17), nor the
conditional incidence calculation (157.H20) transfers to \(D>1\),
\(L>1\), generic \(t=1\), original \(t\geq2\), the cross owner, another
M1 component, M2, endpoint uniformity, M9, the bridge, the quarter
theorem, or either global exponent.

## 4. First doubtful or unproved step

No mathematical defect remains in the exact centering identity, the
literal Nyquist-fold estimate, the orbit decomposition, the corrected
incidence count, or the route-scoped capacity ledgers under their
printed hypotheses.

The first unproved literal object is

\[
 \sum_{V<|j|\leq2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{1\leq v<H/2}
 \bigl(\widehat B_j(2dv)+\widehat B_j(-2dv)\bigr)
 K(-v^2,-j;c),
\tag{157.H21}
\]

with the frozen exterior normalization restored. It requires a joint
mask-preserving signed estimate, or an exactly equivalent selected
incidence theorem. The moving-cell control model proves only that the
accepted one-variable norms do not imply the desired mixed absolute
norm. The completion and norm calculations prove only the capacities
of their stated placements. The selected count proves support size
only. None is a universal obstruction.

## 5. Required control tests and outcomes

| Control | Hostile outcome |
|---|---|
| exact \(1/(4N)\) centering | PASS. The zero row is subtracted once, and the global constant tail vanishes at every nonzero sampled frequency. |
| constant tail and hard endpoints | PASS. Its cyclic mixed difference is zero; profile and support endpoints are charged by zero-extended BV, and strict \(j\)-endpoints by Abel supremum terms. |
| positive and negative cells | PASS. The cutoffs are \(x\geq j+1\) and \(x\geq-j\); the proof treats the blocks separately. |
| profile components and transitions | PASS. Monotone sampling uses the total variation of the single zero-extended profile and assumes no bounded component count. |
| exact complex phase | PASS. Equation (157.H8) gives total spatial phase variation \(O(X^\varepsilon)\); no realness or conjugacy is used. |
| complementary range | PASS. Two-element orbits are exactly \(1\leq v<H/2\); the single \(v=H/2\) row is counted once. |
| \(c=4\) and arbitrary divisor strata | PASS. The interior range may be empty; the twisted kernel proof covers all two-adic and repeated-prime cases. |
| blind fold obstruction | REJECTED AS FINAL OBSTRUCTION. Its support-sized diagnostic violates the inherited profile-BV hypothesis; literal spatial Abel proves the fold target. |
| blind low-band warning | RETAINED AS ROUTE CONTROL. General low nonzero modes need not have Nyquist cancellation and remain in the paired matrix. |
| \(N,M,V,d,c\) power ledger | PASS. Equation (157.H16) leaves \(M^{-1/4}\) only; (157.H17) labels all unresolved-method outputs as capacities. |
| corrected incidence count | PASS. \(\min(M,V)\) is support cardinality; square-root cancellation remains a separate hypothetical signed theorem. |
| external \(B_{1,U}(1)\) | CONDITIONAL PASS. It is outside the frozen row and may be reinserted once using its accepted \(X^\varepsilon\) bound. |
| downstream scope | PASS. No full nonzero matrix, new range, broader owner, endpoint assembly, M9 result, bridge, target theorem, or exponent is promoted. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

This review read and used:

1. protocol.md;
2. state/active_campaign.yml;
3. rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/barrier_packet.md;
4. rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reports/centered_nonzero_root_discrepancy_attack.md;
5. rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reports/blind_nonzero_cross_fibre_rederivation.md;
6. proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md;
7. rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/candidates/conductor_round157_nyquist_fold_target.md;
8. rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reviews/independent_nyquist_fold_round157.md;
9. rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/hostile_profile_endpoint_round156_final.md; and
10. rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md, only for the accepted external-scalar seam.

No graph, proof draft, validation matrix, synthesis, campaign manifest,
candidate report, or shared proof state was edited.

## 7. Recommended state effect

Promote, after conductor patch validation:

1. the exact centered physical identity with its \(1/(4N)\) constant
   tail;
2. the exact complementary-orbit split;
3. the target-safe isolated Nyquist-fold estimate
   \(\mathcal F_U(V)\ll_{\varepsilon,A}M^{-1/4}X^\varepsilon\);
4. the literal profile and endpoint proof kernel used for that fold;
5. the corrected support capacity
   \(L_U(V)\ll_\varepsilon\min(M,V)X^\varepsilon\); and
6. the moving-cell, completion, fixed-frequency, Fourier-\(L^1\), and
   Parseval conclusions only as route-scoped no-go or upper-capacity
   statements.

Reject as a durable obstruction the blind report's claim that the
Nyquist alternating mass has only the support-sized bound. Retain its
exact projector, complex complementary-pair identity, and low-band
warning.

Use the terminal label
\(\mathrm{outer\_defect\_centered\_discrepancy\_no\_go}\) only in the
qualified route sense. Do not promote the full nonzero target, a strict
owner-complete positive-power range, a signed square-root incidence
theorem, any downstream owner, or a global exponent.

**GREEN. First defect in the promoted fold and centered package: none.
First open interface: the joint signed paired interior-frequency
estimate (157.H21).**
