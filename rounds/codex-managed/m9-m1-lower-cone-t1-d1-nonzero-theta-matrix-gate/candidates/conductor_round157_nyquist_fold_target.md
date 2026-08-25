# Round 157 conductor candidate: the Nyquist fold is target-safe

- Campaign: m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate
- Round: 157
- Role: conductor proof candidate pending independent review
- Starting graph: 3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea
- Allocation: 100% analytic and algebraic; 0% numerical

## 1. Result

Fix

\[
 q=4N,\qquad c=\frac{4N}{d},\qquad H=\frac c2,
 \qquad n=\frac Nd,
\]

for every odd \(d\mid N\).  The nonzero half-period has the unique
self-complementary frequency

\[
 v=\frac H2=n,\qquad 2dv=\frac q2.
\]

Let

\[
 C_j=\widehat B_j(q/2)=\sum_{x\bmod q}(-1)^xB_j(x).
\]

Then the full literal Nyquist-fold row

\[
\begin{aligned}
 \mathcal F_U(V)
 =-\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,
 C_jK(-n^2,-j;c)
\end{aligned}
\tag{157.NF1}
\]

satisfies

\[
 \boxed{\mathcal F_U(V)
 \ll_{\varepsilon,A}M^{-1/4}X^\varepsilon.}
\tag{157.NF2}
\]

This is uniform for arbitrary \(N\), every odd divisor stratum, both
signed defect blocks, the exact complex residual phase, the asymmetric
cell, every profile transition, zero extension, and all hard endpoints.
It closes only the self-complementary Nyquist frequency.  The remaining
paired nonzero frequencies and the complete nonzero matrix remain open.

## 2. Exact statement and hypotheses

Put

\[
 a=M^{-3/4},\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K.
\]

On one complete residue system modulo \(q\), the literal coefficient is

\[
 B_j(x)=
 \mathbf{1}_{x\ge1}\mathbf{1}_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right),
\tag{157.NF3}
\]

component by component, with the inherited off-congruence profile,
strict mask, transitions, half-open endpoints, and zero extension.  Its
physical support has total integer span \(O(KX^\varepsilon)\), and

\[
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon aX^\varepsilon.
\tag{157.NF4}
\]

No parity, squarefree, primitivity, or coprimality hypothesis is imposed
on \(N\) or \(N/d\).  The external \(B_{1,U}(1)\) factor remains outside
(157.NF1) and costs only another \(X^\varepsilon\).

## 3. Proof or derivation

### 3.1 Spatial cancellation of the alternating mass

For fixed \(j\), the map \(x\mapsto(x^2-j)/N\) is monotone on the
positive physical support.  Thus the zero-extended profile composition
has total variation at most \(\operatorname {Var}(w_U)\).  The exact
phase

\[
 f_j(x)=\sqrt{x^2-j}-x
\]

has derivative

\[
 f_j'(x)
 =\frac{x}{\sqrt{x^2-j}}-1
 =\frac{j}
 {\sqrt{x^2-j}\bigl(x+\sqrt{x^2-j}\bigr)}.
\tag{157.NF5}
\]

On literal support this is
\(O(V/K^2)\), and the total physical span is \(O(KX^\varepsilon)\).
Since \(V\le K\), the phase factor has total spatial variation
\(O(X^\varepsilon)\).  The cell has one spatial jump for fixed \(j\);
all profile and support transitions are already charged to the
zero-extended variation.  Product variation therefore gives

\[
 \sup_x|B_j(x)|+\operatorname {Var}_x(B_j)
 \ll_\varepsilon aX^\varepsilon.
\tag{157.NF6}
\]

Partial sums of \((-1)^x\) have absolute value at most one.  Discrete
Abel summation, including every support endpoint, now yields

\[
 |C_j|
 =\left|\sum_x(-1)^xB_j(x)\right|
 \ll_\varepsilon aX^\varepsilon.
\tag{157.NF7}
\]

On either signed block define

\[
 D_j=(-1)^jC_j.
\]

There are \(O(V)\) consecutive integers in the block.  Hence

\[
\begin{aligned}
 \sup_j|D_j|+\operatorname {Var}_j(D_j)
 &\le \sup_j|C_j|
   +\sum_j\bigl(|C_{j+1}|+|C_j|\bigr)\\
 &\ll_\varepsilon VaX^\varepsilon
 \ll_\varepsilon KaX^\varepsilon.
\end{aligned}
\tag{157.NF8}
\]

The two strict block endpoints cost two further supremum terms already
covered by (157.NF8).

### 3.2 Twisted interval theorem for the fold kernel

For a consecutive integer interval \(I\), expand the literal kernel:

\[
\begin{aligned}
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 &=
 \sum_{u\bmod c}^{*}
 \epsilon_u\left(\frac cu\right)
 e_c(-\bar u n^2)
 \sum_{j\in I}e_c((c/2-u)j).
\end{aligned}
\tag{157.NF9}
\]

Here \(c/2=2n\) is even, whereas every unit \(u\bmod c\) is odd.
Therefore \(c/2-u\) is an odd nonzero residue modulo \(c\).  Translation
by \(c/2\) is a bijection of the residue classes, so the elementary
geometric-sum estimate gives

\[
 \sup_I\left|
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 \right|
 \ll c\log(2c).
\tag{157.NF10}
\]

The proof is valid even when \(|I|>c\): every complete period of each
nonzero additive frequency vanishes.  The factors
\(\epsilon_u(c/u)e_c(-\bar u n^2)\) all have absolute value one.
Thus (157.NF10) uses no parity classification of \(n\) and no transfer
from the zero row.

### 3.3 Restored exterior powers

Since \(C_j=(-1)^jD_j\), Abel summation using (157.NF8)--(157.NF10)
gives, for each odd \(d\mid N\),

\[
 \left|
 \sum_{V<|j|\le2V}C_jK(-n^2,-j;c)
 \right|
 \ll_\varepsilon Ka\,cX^\varepsilon.
\tag{157.NF11}
\]

Restore the full theta factor before summing \(d\):

\[
\begin{aligned}
 |\mathcal F_U(V)|
 &\ll_\varepsilon
 \frac{Ka}{Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 d\,c^{3/2}X^\varepsilon\\
 &=
 \frac{Ka\sqrt q}{N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}d^{-1/2}
 X^\varepsilon\\
 &\ll_\varepsilon
 a\sqrt M\,X^\varepsilon
 =M^{-1/4}X^\varepsilon,
\end{aligned}
\tag{157.NF12}
\]

because \(dc=q=4N\), \(K=\sqrt{NM}\), and the divisor sum is absorbed
into \(X^\varepsilon\).  This proves (157.NF2).

## 4. First doubtful or unproved step

No step in the isolated fold estimate is unproved.  The first remaining
step is the paired interior-frequency matrix

\[
 \sum_{v=1}^{H/2-1}
 \bigl(\widehat B_j(2dv)+\widehat B_j(-2dv)\bigr)
 K(-v^2,-j;c),
\]

summed over \(j\) and every odd \(d\mid N\).  Its low frequencies do not
have the uniformly bounded alternating-mass norm (157.NF7), and
separated fixed-frequency Abel summation restores the known positive
power.  A joint mask-preserving signed theorem remains necessary.

## 5. Required control tests and outcomes

1. **Unique fold and Fourier argument — pass.**  Since \(H=2N/d\), the
   unique nonzero fixed point is \(v=H/2=N/d\), and
   \(2dv=2N=q/2\).
2. **Complex coefficient — pass.**  No realness or Fourier conjugacy is
   used.  Spatial Abel applies directly to the complex literal
   coefficient.
3. **Profile and endpoint ledger — pass.**  Monotone profile sampling,
   exact phase variation, the one cell jump, zero extension, and every
   transition are included in (157.NF6).
4. **Twist versus ordinary mass — pass.**  The alternating spatial
   character makes \(C_j\) small; the additional factor \((-1)^j\)
   transfers its crude \(j\)-variation to a nonzero additive twist of
   the fold kernel.
5. **All divisor strata and powers — pass.**  Equation (157.NF12)
   retains \(d\sqrt c/(Nq)\), the kernel interval cost \(c\), and all
   odd \(d\mid N\).
6. **Both signs and strict endpoints — pass.**  The proof is applied
   separately to the two consecutive signed blocks, with endpoint
   values charged through the supremum in Abel summation.
7. **Downstream scope — pass.**  The proof closes one nonzero frequency
   row only.  It does not prove the complete nonzero matrix, enlarge the
   complete defect collar, or change M1, M2, M9, the bridge, the quarter
   theorem, or either global exponent.

## 6. Dependencies and exact artifacts used

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- strategy/round157_d1_nonzero_theta_matrix_strategy.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/blind_statement.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reports/blind_nonzero_cross_fibre_rederivation.md
- proofs/kernels/m9_m1_d1_theta_zero_row.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/hostile_profile_endpoint_round156_final.md

## 7. Recommended state effect

After independent normalization, profile, endpoint, and power review,
promote the isolated Nyquist-fold estimate (157.NF2) as
proved_internal.  Reject the inference that the alternating fold has
only the support-sized bound \(KM^{-3/4}X^\varepsilon\): the literal
spatial BV gives the stronger pointwise bound
\(M^{-3/4}X^\varepsilon\), and the demodulated \(j\)-variation plus the
twisted geometric interval theorem closes the row.

Do not promote the full nonzero target.  The paired interior frequencies,
their coherent low band, and the equivalent selected signed incidence
theorem remain open.
