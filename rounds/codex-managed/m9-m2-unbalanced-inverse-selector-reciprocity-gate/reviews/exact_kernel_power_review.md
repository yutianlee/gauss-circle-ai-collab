# Round 160 independent exact-kernel and power review

Campaign: `m9-m2-unbalanced-inverse-selector-reciprocity-gate`
Role: independent exact-kernel reviewer
Task: round160_exact_kernel_review
Starting graph SHA-256:
`4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`

Generated at: 2026-08-25T18:56:20+08:00

This is review evidence only and changes no proof status.

## 1. Result

**Result: promote the exact unweighted kernel and its pointwise power
comparison, but keep every literal weighted-matrix conclusion
conditional.**

I independently obtain all of the following finite identities.

1. Additive reciprocity has the sign

   \[
   e(-h\overline j_n/n)
   =e(h\overline n_j/j-h/(jn))
   \tag{160.EK1}
   \]

   for every coprime \(j,n\), without a parity restriction on \(j\) and
   independently of the chosen inverse representatives.

2. With the accepted convention

   \[
   S(a,b;n)=\sum_{x\bmod n}^{*}
   e\!\left(\frac{a\overline x+bx}{n}\right),
   \tag{160.EK2}
   \]

   the literal post-reciprocity summand is

   \[
   \frac{\chi _4(g)\chi _4(n)}{gnj}
   W\!\left(\frac{X}{gnD}\right)
   q_L\!\left(\frac{4Xj}{gn^2}\right)
   e\!\left(\frac{\xi j}{n}
             +\frac{h\overline n_j}{j}
             -\frac{h}{jn}\right)S(N_0,h;n).
   \tag{160.EK3}
   \]

   Complete \(h\bmod n\) summation reconstructs the original
   \(e(Xj/n)\) reciprocal row exactly. The centered range
   \(1\le h<n\) is complete inversion minus the single \(h=0\pmod n\)
   Ramanujan row; positive multiples \(h=mj\) are not deleted.

3. For any \(A\subseteq U_j=(\mathbb Z/j\mathbb Z)^\times\),
   \(M=|A|\), and

   \[
   F_{j,A}(a,h)=e(h\overline a_j/j),
   \qquad a\in A,\quad 1\le h\le j-1,
   \tag{160.EK4}
   \]

   one has

   \[
   F_{j,A}F_{j,A}^{*}=jI_M-\mathbf1\mathbf1^{*}.
   \tag{160.EK5}
   \]

   Its singular values, nuclear norm, and Hilbert--Schmidt norm are

   \[
   \begin{aligned}
   \operatorname{sing}(F_{j,A})
      &=\{\sqrt j\ (M-1\text{ times}),\sqrt{j-M}\},\\
   \|F_{j,A}\|_{S_1}
      &=(M-1)\sqrt j+\sqrt{j-M},\\
   \|F_{j,A}\|_{S_2}^{\,2}
      &=M(j-1).
   \end{aligned}
   \tag{160.EK6}
   \]

   If all \(j\) residue columns are retained and the matrix is normalized
   by \(j^{-1/2}\), its rows are orthonormal:

   \[
   \mathcal F_{j,A}(a,s)=j^{-1/2}e(s\overline a_j/j),
   \quad s\bmod j,
   \qquad
   \mathcal F_{j,A}\mathcal F_{j,A}^{*}=I_M.
   \tag{160.EK7}
   \]

   Hence \(\operatorname{rank}\mathcal F_{j,A}=M\),
   \(\|\mathcal F_{j,A}\|_{S_1}=M\), and
   \(\|\mathcal F_{j,A}\|_{S_2}=\sqrt M\). These two spectra are fully
   compatible: deleting the zero-residue column changes \(I_M\) into
   \(I_M-j^{-1}\mathbf1\mathbf1^*\), but does not make the kernel
   low-rank.

4. The residue-block collapse

   \[
   (P_{n,j}v)(s)
   =\sum_{\substack{1\le h<n\\h\equiv s\pmod j}}v(h)
   \tag{160.EK8}
   \]

   has the sharp norm

   \[
   \|P_{n,j}\|_{2\to2}
   =\sqrt{\left\lceil\frac{n-1}{j}\right\rceil}.
   \tag{160.EK9}
   \]

5. At the primitive stratum \(g=1\), both the unweighted projective
   inflation \(K^{1/2-o(1)}\) and the long-block scale \(X^{a/2}\)
   exceed the required missing factor at every fixed strict admissible
   exponent point.

These statements certify a narrow capacity obstruction: exact Hilbert
rank-one scalarization of the **unweighted** inverse-residue kernel,
followed termwise by a triangle inequality, is neither rank-free nor
low-projective-cost. They do not lower-bound the literal signed owner,
the profile-weighted matrix, or the matrix after entrywise interaction
with \(S(N_0,h;n)\), and they do not rule out a genuinely coupled
vector-valued theorem.

## 2. Exact statement and hypotheses

Let

\[
X=N_0+\xi,\qquad
D=X^\delta,\qquad L=X^\ell,\qquad
R=X/D,\qquad K=XL/D^2,\qquad
\Delta=D/L,
\tag{160.EK10}
\]

where

\[
\frac14\le\delta<\frac12,\qquad
0\le\ell<\delta-\frac14,\qquad
a=\delta-\ell\in(1/4,1/2).
\tag{160.EK11}
\]

The auxiliary strict-polytope inequality
\(178\ell+1638\delta>463\) is retained but is not needed for the
finite kernel or the comparisons below. On the primitive scale,

\[
n\asymp R,\qquad j\asymp K,\qquad
\frac nj\asymp\Delta=X^a,
\qquad
K=X^\kappa,\quad
\kappa=1+\ell-2\delta=1-\delta-a>0.
\tag{160.EK12}
\]

Thus \(j<n\) for all sufficiently large \(X\) on the supported dyadic
scales, so \(1\le h\le j\) is a literal positive-frequency block.

Retain odd \(g,n\), arbitrary parity of \(j\), \((j,n)=1\), arbitrary
\((N_0,n)\), the literal condition \(j\in\mathcal J_{g,n}\), zero
extension, all moving entries and exits, and every \(1\le h<n\).
The accepted switched-cusp normalization is

\[
S^{\chi _4}_{\infty0}(4N_0,h;2n)
=\chi _4(n)S(N_0,h;n).
\tag{160.EK13}
\]

For the unweighted matrix conclusions assume only \(j>1\) and
\(A\subseteq U_j\). For a weighted robustness statement one must add a
separate hypothesis: at a fixed \(g,j\), the actual support contains one
representative \(n_a\) of every desired unit class and, after extracting
unit diagonal factors, its row amplitude is uniformly
\(A_0(1+o(1))\) for some \(A_0\ne0\). No such lower-buffer or
nonvanishing hypothesis is part of the frozen packet.

## 3. Proof and derivation

### 3.1 Reciprocity, parity, and representatives

Choose integers \(u=\overline j_n\) and \(v=\overline n_j\). The integer
\(ju+nv-1\) is divisible by \(n\), because \(ju\equiv1\pmod n\), and
by \(j\), because \(nv\equiv1\pmod j\). Coprimality makes it divisible
by \(jn\). Hence

\[
\frac{u}{n}+\frac{v}{j}\equiv\frac1{jn}\pmod1,
\]

which gives (160.EK1). Replacing \(u\) by \(u+qn\) or \(v\) by
\(v+rj\) changes the exponent by an integer. No division by \(2\)
occurs, so even \(j\) is covered.

Substitution in the normalized coefficient

\[
\widehat\gamma_{g,n}(h)
=\frac1n\sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n)e(-h\overline j_n/n)
\]

and then use of (160.EK13) proves (160.EK3), including the factor
\(1/(gnj)\), both character directions, and the real-centre and
correction phases.

### 3.2 Additive Fourier expansion and complete reconstruction

For every \(j,h,n\),

\[
\boxed{
\mathbf1_{(n,j)=1}e(h\overline n_j/j)
=\frac1j\sum_{t\bmod j}S(h,-t;j)e(tn/j),}
\tag{160.EK14}
\]

where

\[
S(h,-t;j)=\sum_{x\bmod j}^{*}
e\!\left(\frac{h\overline x-tx}{j}\right).
\tag{160.EK15}
\]

Indeed, after expanding (160.EK15), the \(t\)-sum is
\(\sum_t e(t(n-x)/j)\), which is \(j\) exactly when
\(x\equiv n\pmod j\) and zero otherwise. The sign \(-t\) and the
outside phase \(+tn/j\) are therefore forced.

For complete \(h\bmod n\) reconstruction, use (160.EK2):

\[
\begin{aligned}
\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
&=\frac1n\sum_j b_{g,n}(j)
  \sum_{x\bmod n}^{*}e(N_0\overline x/n)
  \sum_{h\bmod n}e(h(x-\overline j_n)/n)\\
&=\sum_j b_{g,n}(j)e(N_0j/n),
\end{aligned}
\tag{160.EK16}
\]

where

\[
b_{g,n}(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n)
\]

and every \(j\)-sum retains its literal support. Orthogonality forces
\(x=\overline j_n\), hence \(\overline x=j\pmod n\). The factor already
inside \(b_{g,n}(j)\) changes \(e(N_0j/n)\) into \(e(Xj/n)\).
At \(h=0\), \(S(N_0,0;n)=c_n(N_0)\), so the centered sum is
(160.EK16) minus

\[
\widehat\gamma_{g,n}(0)c_n(N_0)
\tag{160.EK17}
\]

exactly once. This calculation is unchanged if the inverted but
equivalent convention
\(\sum_x^*e((N_0x+h\overline x)/n)\) is used.

### 3.3 The two exact spectra and projective costs

For \(a,b\in A\),

\[
\begin{aligned}
(F_{j,A}F_{j,A}^{*})(a,b)
&=\sum_{h=1}^{j-1}
e\!\left(\frac{h(\overline a-\overline b)}j\right)\\
&=\begin{cases}
j-1,&a=b,\\
-1,&a\ne b.
\end{cases}
\end{aligned}
\]

This is (160.EK5). The all-ones direction has eigenvalue \(j-M\);
its orthogonal complement has eigenvalue \(j\). Since
\(M\le\varphi(j)\le j-1\), all \(M\) eigenvalues are positive, proving
(160.EK6) and full row rank.

If the column \(h=j\equiv0\pmod j\) is restored, the off-diagonal
\(-1\) becomes \(0\) and the diagonal \(j-1\) becomes \(j\).
Normalization by \(j^{-1/2}\) proves (160.EK7). Thus for the complete
normalized residue matrix

\[
\frac{\|\mathcal F_{j,A}\|_{S_1}}
     {\|\mathcal F_{j,A}\|_{S_2}}
=\sqrt M
\tag{160.EK18}
\]

exactly. For the nonzero-residue matrix and \(M\ge2\),

\[
\frac{\|F_{j,A}\|_{S_1}}{\|F_{j,A}\|_{S_2}}
\ge
\frac{(M-1)\sqrt j}{\sqrt{M(j-1)}}
\gg\sqrt M.
\tag{160.EK19}
\]

The nuclear norm is the infimum of
\(\sum_\nu\|u_\nu\|_2\|v_\nu\|_2\) over exact Hilbert rank-one
representations \(F=\sum_\nu u_\nu v_\nu^*\). Therefore
(160.EK18)--(160.EK19) are exact projective costs in that Hilbert
geometry, not estimates for the final signed sum.

For \(A=U_j\), the elementary bound
\(\varphi(j)=j^{1-o(1)}\) makes the inflation
\(j^{1/2-o(1)}\). On the primitive scale \(j\asymp K\), this becomes
\(K^{1/2-o(1)}\).

For completeness, (160.EK14) has the exact Parseval identities

\[
\sum_{t\bmod j}|S(h,-t;j)|^2=j\varphi(j),
\tag{160.EK20}
\]

and

\[
\sum_{h=1}^{j-1}|S(h,-t;j)|^2
=j\varphi(j)-|c_j(t)|^2.
\tag{160.EK21}
\]

Together with
\(\sum_t|c_j(t)|^2=j\varphi(j)\), these show that a fixed proportion
of the joint coefficient mass lies at centered
\(|t|\asymp j\). This is a valid finite Fourier-bandwidth diagnostic.
Turning it into an automorphic Sobolev or Bessel loss requires the exact
norm of a specified trace theorem and is not proved by these identities.

### 3.4 Odd classes, the long block, and positive \(h=mj\)

The simultaneous conditions \(n\) odd and \(n\equiv a\pmod j\),
\(a\in U_j\), form one class modulo

\[
\lambda_j=\operatorname{lcm}(2,j)
=\begin{cases}
j,&2\mid j,\\
2j,&2\nmid j.
\end{cases}
\tag{160.EK22}
\]

For even \(j\), every unit class is already odd. For odd \(j\), the
Chinese remainder theorem selects one of the two lifts modulo \(2j\).
Thus an interval \(I\) contains

\[
\#\{n\in I:n\text{ odd},\ n\equiv a\pmod j\}
=\frac{|I|}{\lambda_j}+O(1)
\tag{160.EK23}
\]

points of each fixed class. This count does not prove that the literal
profile is nonzero on a complete class block.

The rows of \(P_{n,j}\) in (160.EK8) have disjoint supports with squared
row norms

\[
m_s=\#\{1\le h<n:h\equiv s\pmod j\}.
\]

Consequently

\[
P_{n,j}P_{n,j}^{*}=\operatorname{diag}(m_s),
\]

and the maximum \(m_s\) is
\(\lceil(n-1)/j\rceil\), proving (160.EK9), including sharpness.
There are
\(\lfloor(n-1)/j\rfloor\asymp\Delta\) positive multiples \(h=mj\).
For them,

\[
e(h\overline n_j/j)=1,\qquad
e(-h/(jn))=e(-m/n)=1+O(1/j),
\tag{160.EK24}
\]

because \(m/n<1/j\). Thus the short inverse phase supplies no
oscillation on this subfamily. Equations (160.EK9) and (160.EK24) are
operator-capacity controls, not signed lower bounds after the
Kloosterman weights are inserted.

### 3.5 Every boundary-power comparison

The required saving exponent is

\[
\mu(a)=
\begin{cases}
a-\frac14,&\frac14<a\le\frac13,\\[1mm]
\frac{1-2a}{4},&\frac13\le a<\frac12.
\end{cases}
\tag{160.EK25}
\]

For the primitive projective scale, using
\(\kappa=1-\delta-a=1-2a-\ell\),

\[
\frac\kappa2-\mu(a)
=\frac{3-2\delta-6a}{4}
=\frac34-2a-\frac\ell2
>\frac{1-3a}{2}\ge0
\quad\left(\frac14<a\le\frac13\right),
\tag{160.EK26}
\]

where strictness uses \(\delta<1/2\). In the other branch,

\[
\frac\kappa2-\mu(a)
=\frac{1-2\delta}{4}>0
\quad\left(\frac13\le a<\frac12\right).
\tag{160.EK27}
\]

At \(a=1/3\), both formulas agree and the margin is
\((1-2\delta)/4\). Hence \(K^{1/2-o(1)}\) exceeds the missing factor
at every fixed strict exponent point; the \(o(1)\) can be absorbed only
after that point is fixed. There is no uniform positive margin as the
open face \(\delta=1/2\) is approached.

The long-block exponent obeys

\[
\frac a2-\mu(a)
=\begin{cases}
\frac14-\frac a2,&\frac14<a\le\frac13,\\[1mm]
\frac{4a-1}{4},&\frac13\le a<\frac12,
\end{cases}
>0.
\tag{160.EK28}
\]

Thus the sharp \(\sqrt\Delta=X^{a/2}\) capacity also exceeds the missing
factor pointwise. Neither comparison says that the literal signed scalar
is large or that a stronger coupled theorem could not offset these
prices.

## 4. First doubtful or unproved step

The first unproved step in the conductor candidate is the unconditional
use of its buffered weighted-block paragraph. Scale separation
\(n/j\asymp\Delta\to\infty\) ensures that a sufficiently long genuine
interval could contain all unit classes, but it does not prove that, for
some fixed \(j\), the **literal moving support** contains such an interval
on which

\[
W(X/(gnD))q_L(4Xj/(gn^2))
\]

is uniformly nonzero and relatively comparable. The inherited bounds are
upper size and regularity information; they do not supply the necessary
lower amplitude \(A_0\ne0\). Diagonal weighting can delete rows or make
their nuclear contribution arbitrarily small. Thus the perturbation
estimate is valid only after an explicit complete-class,
lower-buffer, and relative-smoothness hypothesis is added.

Even that conditional profile lemma would control only the inverse-phase
submatrix. Entrywise multiplication by the actual
\(S(N_0,h;n)\) array, or a vector theorem that keeps this array coupled
to \(F_j\) before positive norms, need not preserve the unweighted
nuclear lower bound. The finite Fourier bandwidth similarly does not
identify a source-valid automorphic Bessel norm. These are the first
remaining analytic and source seams.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact reciprocity, sign, and representatives | **PASS.** Equation (160.EK1) is exact. |
| Even and odd \(j\) | **PASS.** Reciprocity is parity-free; (160.EK22) gives the exact odd-\(n\) class period. |
| Literal scalar and character placement | **PASS.** Equation (160.EK3) retains \(1/(gnj)\), \(\chi_4(g)\chi_4(n)\), real centre, correction phase, and arbitrary \((N_0,n)\). |
| Centered nonzero range exactly once | **PASS.** Equation (160.EK17) is the single removed row; \(h=mj>0\) remains. |
| Full-\(h\) self-return | **PASS.** Equation (160.EK16) reconstructs the original \(e(Xj/n)\) row. |
| Additive/Kloosterman Fourier signs | **PASS.** Direct orthogonality proves (160.EK14). |
| Nonzero-residue spectrum and norms | **PASS.** Equations (160.EK5)--(160.EK6) are exact for every subset \(A\). |
| Full-residue normalized spectrum and norms | **PASS.** Equation (160.EK7) gives orthonormal rows and exact \(S_1/S_2=\sqrt M\). |
| Hilbert projective interpretation | **PASS WITH SCOPE.** It applies to exact rank-one scalarization plus termwise triangle, not arbitrary Banach geometries or coupled vector methods. |
| Long-\(h\) block and \(h=mj\) | **PASS WITH SCOPE.** Equations (160.EK9) and (160.EK24) are sharp operator controls, not signed lower bounds. |
| Primitive \(g=1\) and boundary powers | **PASS POINTWISE.** Equations (160.EK26)--(160.EK28) are strict at each fixed interior exponent point, not uniformly at an open face. |
| Moving support and literal weighted lower bound | **FAIL UNCONDITIONALLY / PASS CONDITIONALLY.** A lower-buffer and complete-class hypothesis is absent. |
| Fourier/Sobolev/Bessel price | **PASS as finite Fourier diagnostic only.** No automorphic norm conclusion follows without a theorem-specific audit. |
| Target and scope | **PASS.** No owner estimate, strict range, downstream closure, or exponent improvement is inferred. |

No numerical experiment or external theorem is used in this review.

## 6. Dependencies and exact artifacts used

The review used:

- `AGENTS.md`;
- `protocol.md`;
- `state/proof_obligations.yml`, especially
  `M9-M2-smooth-unbalanced-three-quarter-estimate`,
  `M9-M2-unbalanced-truncated-divisor-fixed-centre-return`,
  `M9-M2-unbalanced-Kloosterman-dispersion-interface-obstruction`,
  `M9-M2-unbalanced-level-four-spectral-matrix-obstruction`, and
  `M9-M2-physical-one-count-assembly`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/candidates/conductor_round160_reciprocity_seed.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/inverse_selector_reciprocity_attack.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/blind_reciprocity_matrix_rederivation.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/candidates/conductor_round160_reciprocity_projective_obstruction.md`; and
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/post_blind_reciprocity_projective_seam.md`.

All derivations here are finite reciprocity, additive orthogonality,
matrix-spectrum, and elementary exponent calculations. No shared state,
synthesis, candidate, or proof draft was edited.

## 7. Recommended state effect

1. **PROMOTE** the exact reciprocity identity, literal scalar,
   Fourier/Kloosterman expansion, complete-\(h\) reconstruction, and
   exactly-once zero-row deletion.
2. **PROMOTE** both unweighted matrix spectra
   (160.EK5)--(160.EK7), including their exact nuclear and
   Hilbert--Schmidt costs, under the explicit scope
   `exact_unweighted_Hilbert_rank_one_scalarization_plus_triangle`.
3. **PROMOTE** the sharp long-block norm and the survival of positive
   \(h=mj\), again as operator-capacity controls rather than signed lower
   bounds.
4. **PROMOTE** the primitive-\(g=1\) comparisons
   (160.EK26)--(160.EK28) only pointwise at fixed strict exponent pairs.
5. **RETAIN AS DIAGNOSTIC ONLY** the finite high-Fourier-bandwidth
   conclusion; do not convert it into an automorphic Sobolev/Bessel claim
   without a theorem-specific source and norm audit.
6. **DO NOT PROMOTE** an unconditional weighted-profile nuclear lower
   bound. Retain the candidate perturbation only under an explicit
   lower-buffer, complete-class, and relative-smoothness hypothesis.
7. **REJECT** any broader impossibility claim for the literal
   Kloosterman-weighted matrix or for bespoke vector-valued methods.
8. **RETAIN OPEN** `M9-M2-smooth-unbalanced-three-quarter-estimate` and
   every downstream obligation. The valid Round-160 outcome is the
   narrow canonical-scalarization capacity no-go, with no target, strict
   owner-complete range, or global-exponent improvement.
