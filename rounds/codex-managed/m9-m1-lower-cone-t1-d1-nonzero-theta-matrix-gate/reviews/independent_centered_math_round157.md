# Round 157 independent centered-discrepancy mathematics review

- Campaign: m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate
- Round: 157
- Role: independent terminal mathematics reviewer
- Starting graph SHA-256: 3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea
- Scope: exact centering and normalization, literal moving-cell variation, centered quadratic completion, incidence capacity, theta-coordinate power ledgers, folds, endpoints, and downstream scope

## 1. Result

The centered-discrepancy report is mathematically sound in its stated
route-scoped sense. The exact nonzero projection is

\[
 \mathcal T_{\ne 0,U}(V)
 =
 \sum_{V<|j|\leq 2V}\sum_{x\bmod 4N}
 \left(B_j(x)-\frac{\widehat B_j(0)}{4N}\right)
 G_N(x^2-j),
\]

with no missing factor, sign, divisor stratum, or second zero-row
subtraction. The report also correctly proves:

1. the currently accepted one-variable profile controls do not imply a
   target-sized mixed rectangular norm;
2. elementary centered completion has capacity
   \[
   \sup_{I,J}|\mathscr D_N(I,J)|
   \ll \sqrt N\,\tau(N)(\log(2N))^2;
   \]
3. the true selected incidence capacity is
   \[
   L_U(V)\ll_\varepsilon \min(M,V)X^\varepsilon;
   \]
4. a genuine square-root theorem for the literal selected signed terms
   would therefore be sufficient for every allowed \(V\); and
5. the separated Fourier-\(L^1\), fixed-\(v\), and sampled-Parseval
   placements retain the powers printed in the report and do not prove
   a new positive-power range.

These are reductions, corrected capacities, and method-specific no-go
statements. They do not prove that the literal nonzero matrix is large,
and they do not close the target.

**Terminal verdict: GREEN.**

## 2. Exact statement and hypotheses audited

I retained

\[
 q=4N,\qquad c=\frac qd,\qquad H=\frac c2,\qquad
 1\ll M\leq N^{1/2},\qquad
 M^{3/4}(\log(2X))^A<V\leq K=\sqrt{NM},
\]

for arbitrary \(N\), every odd \(d\mid N\), and each signed defect block
separately. I treated \(B_j\) as the literal complex ambient coefficient:
the exact residual phase, real zero-extended profile, asymmetric cell,
strict mask, all transitions, physical endpoints, and hard endpoints
remain present. The only coefficient norms used in the no-go are

\[
 \|B_j\|_\infty+\operatorname {Var}_x B_j
 \ll_\varepsilon M^{-3/4}X^\varepsilon
\]

and

\[
 \sup_j|A_j|+\operatorname {Var}_jA_j
 \ll_\varepsilon K M^{-3/4}X^\varepsilon,
 \qquad A_j=\widehat B_j(0).
\]

The centered discrepancy is considered only for cyclic consecutive
\(x\)-intervals and consecutive \(j\)-intervals contained in one signed
block. Since \(K<N<q\), the physical support has a unique nonwrapping
lift. Zero extension in \(j\) charges the strict block endpoints.

The report's complementary-mode formula has now been correctly restricted
to two-element orbits \(1\leq v<H/2\). The self-complementary mode
\(v=H/2\) occurs once and is isolated as a separate Nyquist fold. The
combined conductor kernel records the same orbit split and a separate
fold estimate; this review uses it only to verify consistency of that
split, not to certify the remaining interior modes.

## 3. Proof and derivation audit

### 3.1 Exact \(1/q\) centering

The accepted complete half-period inversion gives

\[
 \mathcal T_U(V)=\sum_{j,x}B_j(x)G_N(x^2-j).
\]

Round 156 gives

\[
 \mathscr S_N(j)
 =-\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,K(0,-j;c).
\]

Therefore the \(v=0\) term in the frozen matrix, whose exterior
normalization is \(-i(1+i)/(2Nq)\), is exactly

\[
 \frac1q\sum_j A_j\mathscr S_N(j).
\]

Subtracting it once proves all three forms of (157.R1). For a nonzero
sampled mode,

\[
 2dv\equiv0\pmod q
 \quad\Longleftrightarrow\quad
 v\equiv0\pmod H,
\]

so the constant \(A_j/q\) has no nonzero sampled Fourier coefficient.
Its cyclic \(x\)-difference, and hence its mixed \(j\)-\(x\) difference,
is zero. This verifies the full constant-tail ledger without discarding
its physical \(L^1\) mass.

### 3.2 Moving cell and mixed variation

For \(x>0\), the exact cell

\[
 -x\leq j\leq x-1
\]

reduces on a positive block to \(x\geq j+1\), and on a negative block to
\(x\geq-j\). Hence

\[
 B_j(x)=\mathbf 1_{x\geq\lambda_\sigma(j)}F_j(x),
 \qquad
 \lambda_+(j)=j+1,\quad \lambda_-(j)=-j,
\]

is an exact factorization when every other profile and endpoint factor
is left in \(F_j\). The positive difference loses the point \(j+1\);
the negative difference gains the point \(-j-1\). The remaining bulk
difference contains all moving profile endpoints and transitions. Thus
(157.R22) and (157.R23) correctly identify the diagonal trace without
claiming that it cannot cancel against the literal bulk.

The two-dimensional Abel inequality is legitimate. The centered kernel
has zero \(x\)-sum for every \(j\); cyclic Abel summation in \(x\),
followed by Abel summation in the zero-extended \(j\)-variable, expresses
the pairing through \(\Delta_j\Delta_xB\) and consecutive rectangular
partial sums. No separate constant-tail or endpoint term is omitted.

The control array

\[
 B_j^{\mathrm{ctl}}(x)=a\mathbf 1_{j+1\leq x\leq x_1},
 \qquad a=M^{-3/4},
\]

has the accepted spatial amplitude and BV scales and
\(\sup|A_j|+\operatorname {Var}_jA_j\ll Ka\), but

\[
 \sum_{j,x}|\Delta_j\Delta_xB_j^{\mathrm{ctl}}(x)|
 =2a(L-1)+O(a).
\]

It therefore rigorously disproves the inference from the accepted
one-variable controls to an \(O(a)\) mixed norm. The report correctly
does not present this model as a lower bound for the actual coefficient.

### 3.3 Centered quadratic completion

The projector

\[
 G_N(t)=-\frac{i}{2N}
 \sum_{\substack{h\bmod q\\h\ \mathrm{odd}}}
 \chi_4(h)e_q(ht)
\]

has the correct sign and normalization. Substitution into the centered
rectangle deletes exactly the \(r=0\) completion term and gives
(157.R33). For \(g=(h,q)=(h,N)\), reduction of the imprimitive quadratic
sum gives

\[
 \mathcal G_q(h,r)=0\quad\text{unless }g\mid r,
 \qquad
 |\mathcal G_q(h,r)|\leq\sqrt{2qg}.
\]

The nonzero Fourier \(L^1\) norm of an interval then yields

\[
 |E_I(h)|\ll\sqrt{q(h,N)}\log(2q).
\]

The \(j\)-interval factor is

\[
 \ll\min\left(V,\frac q{1+|h|_q}\right).
\]

Expanding \((h,N)^{1/2}\) by odd divisors \(d\mid N\), and writing
\(h=da\), gives

\[
 \sum_{1\leq a\leq q/(2d)}
 \min\left(V,\frac{q/d}{a}\right)
 \ll\frac qd\log(2V).
\]

Consequently the complete normalization is

\[
 \frac{\sqrt q}{N}\,q
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}d^{-1/2}
 \ll \sqrt N\,\tau(N),
\]

up to absolute constants, and (157.R38) follows. No coprimality of
\(d\) and \(N/d\) is used. Multiplication by the hypothetical ideal
mixed norm \(M^{-3/4}X^\varepsilon\) restores
\(N^{1/2}M^{-3/4}X^\varepsilon\), which is \(O(X^\varepsilon)\) only
from \(M\geq N^{2/3-o(1)}\), outside the frozen \(M\leq N^{1/2}\)
range. This is a capacity of the elementary completion placement, not a
lower bound or an impossibility theorem for all joint methods.

### 3.4 Corrected incidence count

For the selected relation \(j=k^2-Nn\), the cell is equivalent to

\[
 k^2-k+1\leq Nn\leq k^2+k.
\]

The upper endpoint for \(k\) is followed immediately by the lower
endpoint for \(k+1\). These intervals partition the positive integers,
so each positive \(n\) supplies exactly one pair \((k,j)\). The dyadic
\(M\)-block therefore gives \(L_U(V)\ll M\). Independently, the accepted
summed root estimate gives \(L_U(V)\ll_\varepsilon VX^\varepsilon\);
the latter dependency is essential and is not reproved here. Combining
the two bounds, separately for the signs and then taking their union,
proves

\[
 L_U(V)\ll_\varepsilon\min(M,V)X^\varepsilon.
\]

Thus a genuine square-root theorem for the actual signed, weighted
selected terms would have capacity

\[
 M^{-3/4}L_U(V)^{1/2}X^\varepsilon
 \leq M^{-1/4}X^\varepsilon
\]

for every \(V\). The report correctly labels this as hypothetical and
corrects the older \(V\leq M^{3/2}\) capacity statement without
promoting signed cancellation.

### 3.5 Theta-coordinate capacities

Let \(a=M^{-3/4}\). Spatial BV gives

\[
 |\widehat B_j(2dv)|
 \ll a\min\left(K,\frac H{|v|_H}\right),
 \qquad
 \sum_{v\neq0}|\widehat B_j(2dv)|
 \ll aH\log(2H).
\]

Theta-Weil, with the gcd factors summed over the nonzero \(j\)-interval,
has capacity \(V\sqrt c\,X^\varepsilon\) for each fixed \(v\).
Restoring \(d\sqrt c/(Nq)\) and \(H=c/2\) therefore gives
\(aV/d\) for one \(d\), and \(aV X^\varepsilon\) after all odd
divisors. This verifies (157.R43)--(157.R44).

For fixed-\(v\) Abel, the required norm is the full sum of the
\(j\)-supremum and \(j\)-variation over \(v\). The diagonal cell trace
prevents replacing that norm by spatial Fourier decay. Even under the
explicitly hypothetical favorable bound \(\Lambda_d\ll aH X^\varepsilon\),
the exterior powers give

\[
 a\min\left(\frac Vd,\frac{\sqrt N}{d^{3/2}}\right)
\]

for one \(d\), hence \(a\min(V,\sqrt N)X^\varepsilon\) after summation.
This verifies the conditional capacity (157.R47), not a theorem for the
literal coefficient.

Sampled Parseval is exactly

\[
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 =H\sum_{r\bmod H}|C_{j,d}(r)|^2.
\]

The residue multiplicity \(O(1+dK/N)\) produces both

\[
 \frac{N^{3/2}}{dM}
 \quad\text{and}\quad
 \frac N{M^{1/2}}.
\]

The second term is the large-\(d\) fold collision and cannot be deleted.
Combining this with

\[
 \sum_v|K(-v^2,-j;c)|^2
 \ll_\varepsilon c^2(j,c)X^\varepsilon
\]

and
\(\sum_{V<|j|\leq2V}(j,c)^{1/2}\ll_\varepsilon VX^\varepsilon\)
reproduces (157.R51) and, after divisor summation,

\[
 V\left(N^{1/4}M^{-1/2}+M^{-1/4}\right)X^\varepsilon.
\]

This is only an absolute Cauchy-Parseval capacity. The corrected
two-element complementary-mode formula supplies no automatic
cancellation, while the single Nyquist fold is kept outside that
pairing.

## 4. First doubtful or unproved step

There is no unproved step in the exact centering identity, the logical
one-variable-to-mixed-norm countermodel, the elementary completion
upper bound, the corrected incidence count, or the stated capacity
ledgers.

The first unproved literal step is a joint signed theorem. One needs
either the actual mixed norm together with a target-sized centered root
discrepancy, or a mask-preserving estimate that couples the moving
diagonal directly to the arithmetic kernel. Equivalently, one needs the
weighted selected incidence estimate (157.R57), with both signs,
transitions, and endpoints retained. The cardinality
\(\min(M,V)\) is not that theorem.

The separate Nyquist-fold result closes only the isolated fixed mode
after its own terminal review. It does not address the paired interior
frequencies and is not used here as evidence for the full nonzero
matrix.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact \(1/(4N)\) projection | PASS. The complete transform minus the Round-156 zero row gives one and only one constant-tail subtraction. |
| Global constant tail | PASS. Its nonzero sampled Fourier coefficients and cyclic mixed difference vanish, while its physical mass remains accounted for by the zero row. |
| Positive and negative moving cells | PASS. The two endpoint motions and their distinct gained or lost points are exact; all other moving transitions remain in the bulk term. |
| Mixed-norm scope | PASS. The control model proves insufficiency of the accepted one-variable norms only; it is not claimed to be the literal coefficient or an actual lower bound. |
| Centered Gauss completion | PASS. The imprimitive gcd condition, even-modulus Gauss magnitude, nonzero completion modes, divisor sum, and \(q^{3/2}/N\) normalization are retained. |
| Incidence correction | PASS. The \(O(M)\) partition argument is combined explicitly with the accepted independent \(O_\varepsilon(VX^\varepsilon)\) root count. |
| Fourier-\(L^1\) and fixed-\(v\) capacities | PASS. The full \(d\sqrt c/(Nq)\), \(H=c/2\), divisor, and variation costs are restored; the favorable \(\Lambda_d\) input is visibly hypothetical. |
| Parseval and folds | PASS. The period \(2N/d\), collision multiplicity, large-\(d\) term, all odd \(d\), two-element orbits, and isolated Nyquist row are retained. |
| Signs, endpoints, and external seam | PASS. Signed blocks are separate, zero extension charges strict endpoints, and the external \(B_{1,U}(1)\) costs only \(X^\varepsilon\). |
| Downstream scope | PASS. No broader M1 or M2 owner, endpoint assembly, M9 theorem, bridge, quarter theorem, or global exponent is claimed. |

The review is entirely analytic and algebraic. No numerical experiment
or numerical certification was used.

## 6. Dependencies and exact artifacts used

I read and audited:

- protocol.md;
- state/active_campaign.yml;
- strategy/round157_d1_nonzero_theta_matrix_strategy.md;
- the centered nonzero root-discrepancy report;
- the conductor centered seed;
- proofs/kernels/m9_m1_d1_theta_zero_row.md; and
- the Round-156 independent recombination mathematics review.

I also inspected
proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md solely to
confirm that its two-element orbit range and isolated fixed fold agree
with the corrected centered report; this report does not serve as a
terminal proof review of the fold estimate.
The accepted \(O_\varepsilon(VX^\varepsilon)\) incidence input is the
existing summed root estimate cited by the claimant. No external source
theorem is invoked.

I made no change to the proof graph, proof draft, validation matrix,
synthesis, campaign state, candidate, or claimant report.

## 7. Recommended state effect and terminal verdict

Promote, route-scoped:

1. the exact centered physical identity (157.R1), including the
   \(1/(4N)\) constant tail;
2. the mixed-cell ledger and the control-model no-go against deriving a
   target mixed norm from the accepted one-variable controls;
3. the elementary centered completion bound (157.R38);
4. the corrected incidence capacity
   \(L_U(V)\ll_\varepsilon\min(M,V)X^\varepsilon\); and
5. the restored Fourier-\(L^1\), fixed-\(v\), and Parseval capacities,
   explicitly as upper capacities rather than signed estimates.

Use the terminal label
outer_defect_centered_discrepancy_no_go. Do not promote the full
nonzero target, a strict positive-power range, a signed square-root
incidence theorem, or any downstream owner or exponent. The first open
interface remains a mask-preserving joint signed theorem for the
interior nonzero modes.

**GREEN. First defect: none in the reviewed centered identity and
route-scoped no-go package; the first unproved object is the joint signed
interior-frequency estimate.**
