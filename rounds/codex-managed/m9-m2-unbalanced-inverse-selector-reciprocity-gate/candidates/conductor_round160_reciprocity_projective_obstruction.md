# Conductor Round 160 candidate: reciprocity kernel projective obstruction

Campaign: `m9-m2-unbalanced-inverse-selector-reciprocity-gate`

Task: conductor_round160_reciprocity_projective_obstruction

Role: conductor candidate

Generated at: 2026-08-25T18:31:50+08:00

Starting graph SHA-256:
`4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`

This is candidate evidence only. It changes no proof status.

## 1. Result

Additive reciprocity gives an exact shorter-modulus representation, but
the resulting inverse-residue kernel is not low-projective-cost. For every
integer \(j>1\), put \(U_j=(\mathbb Z/j\mathbb Z)^*\),
\(m_j=\varphi(j)\), and

\[
 F_j(a,h)=e(h\overline a_j/j),
 \qquad a\in U_j,\quad 1\le h\le j-1.
 \tag{160.CP1}
\]

Then

\[
 \boxed{F_jF_j^*=jI_{m_j}-{\bf 1}{\bf 1}^*.}
 \tag{160.CP2}
\]

Consequently the singular values of \(F_j\) are

\[
 \sqrt j\quad(m_j-1\text{ times}),
 \qquad \sqrt{j-m_j}\quad(1\text{ time}),
 \tag{160.CP3}
\]

and

\[
 \|F_j\|_{S_1}=(m_j-1)\sqrt j+\sqrt{j-m_j},
 \qquad
 \|F_j\|_{S_2}^2=m_j(j-1).
 \tag{160.CP4}
\]

The actual positive range also contains \(h=j\), because \(j<n\). Thus
the complete residue block \(1\le h\le j\) has normalized matrix

\[
 \mathcal F_j(a,h)=j^{-1/2}e(h\overline a_j/j),
 \qquad
 \mathcal F_j\mathcal F_j^*=I_{m_j},
 \quad
 \|\mathcal F_j\|_{S_1}=m_j,
 \quad
 \|\mathcal F_j\|_{S_2}=\sqrt{m_j}.
 \tag{160.CP4a}
\]

Thus every exact Hilbert-space rank-one common-test decomposition pays

\[
 \frac{\|F_j\|_{S_1}}{\|F_j\|_{S_2}}
 \gg \sqrt{\varphi(j)}
 \gg_\varepsilon j^{1/2-\varepsilon}.
 \tag{160.CP5}
\]

The centered deletion removes only \(h=0\pmod n\); it does not remove the
positive frequencies \(h=j,2j,\ldots\), which are \(0\pmod j\). Even the
artificially smaller block \(1\le h\le j-1\) remains full rank by
(160.CP2). Conditionally, if the literal support contains a buffered
odd-\(n\) interval covering every unit class and its joint smooth amplitude
is uniformly comparable to a nonzero value there, the same lower bound
survives restoration of the row weights and \(e(-h/(jn))\), up to
\(O(\Delta^{-1}j/\varphi(j))=o(1)\) relative error. The campaign
hypotheses do not supply this lower-buffer premise.

For the primitive stratum \(g=1\), \(j\asymp K\). The projective inflation
\(K^{1/2-o(1)}\) is at least the entire missing boundary power at every
fixed strict admissible exponent pair; no open-face-uniform margin is
claimed. Therefore additive reciprocity does not produce
the low-projective-cost scalar common-test decomposition missing in Round
143. This is a capacity no-go for canonical termwise scalarization of the
reciprocity kernel. It is not a bound for the signed owner and does not
exclude a genuinely vector-valued theorem acting on the literal full-rank
matrix before positive norms.

## 2. Exact statement and hypotheses

Retain the Round-160 parameters

\[
 D=X^\delta,\qquad L=X^\ell,\qquad
 R=X/D,\qquad K=XL/D^2,\qquad \Delta=D/L,
 \tag{160.CP6}
\]

\[
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,
 \qquad a=\delta-\ell\in(1/4,1/2).
 \tag{160.CP7}
\]

For \(r=gn\), \(k=gj\), \((j,n)=1\), the exact coefficient is

\[
 \widehat\gamma_{g,n}(h)=\frac1n
 \sum_j b_{g,n}(j)
 e(h\overline n_j/j-h/(jn)),
 \tag{160.CP8}
\]

with the literal moving support and

\[
 b_{g,n}(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n).
 \tag{160.CP9}
\]

The exact additive Fourier expansion of the nonsmooth factor is

\[
 \boxed{
 1_{(n,j)=1}e(h\overline n_j/j)
 =\frac1j\sum_{t\bmod j}S(h,-t;j)e(tn/j).}
 \tag{160.CP10}
\]

Here \(S(u,v;j)=\sum_{x\bmod j}^*e((u\bar x+vx)/j)\).
Equation (160.CP10) is valid for odd and even \(j\). It is a change of
basis, not an estimate.

The projective conclusion applies to decompositions

\[
 F_j(a,h)=\sum_s u_s(a)\overline{v_s(h)}
 \tag{160.CP11}
\]

that feed scalar modulus tests termwise and close by the triangle
inequality. Their Hilbert projective mass obeys

\[
 \sum_s\|u_s\|_2\|v_s\|_2\ge\|F_j\|_{S_1}.
 \tag{160.CP12}
\]

No claim is made about an estimate that keeps \(F_j\), the Kloosterman
matrix, both characters, and all \(j,n,h\) coupled inside one new vector
theorem.

## 3. Proof and derivation

### 3.1 Reciprocity and additive Fourier expansion

For \((j,n)=1\),

\[
 j\overline j_n+n\overline n_j\equiv1\pmod{jn}.
\]

Dividing by \(jn\) modulo one and negating the first term gives

\[
 e(-h\overline j_n/n)=e(h\overline n_j/j-h/(jn)).
 \tag{160.CP13}
\]

For fixed \(j,h\), Fourier inversion on \(\mathbb Z/j\mathbb Z\) gives

\[
 \begin{aligned}
 &\sum_{a\bmod j}1_{(a,j)=1}e(h\overline a_j/j)e(-ta/j)\\
 &\hspace{35mm}=S(h,-t;j),
 \end{aligned}
\]

which proves (160.CP10).

### 3.2 Exact singular spectrum

For \(a,b\in U_j\),

\[
 (F_jF_j^*)(a,b)=
 \sum_{h=1}^{j-1}e(h(\overline a_j-\overline b_j)/j).
\]

This equals \(j-1\) when \(a=b\), and \(-1\) otherwise, because inversion
permutes \(U_j\). Hence (160.CP2). The all-ones direction has eigenvalue
\(j-m_j\), and its orthogonal complement has eigenvalue \(j\), proving
(160.CP3)--(160.CP4). For \(m_j\ge2\),

\[
 \frac{\|F_j\|_{S_1}}{\|F_j\|_{S_2}}
 \ge\frac{(m_j-1)\sqrt j}{\sqrt{m_j(j-1)}}
 \gg\sqrt{m_j}.
\]

The standard elementary bound
\(\varphi(j)\gg_\varepsilon j^{1-\varepsilon}\) gives (160.CP5).

If the column \(h=j\equiv0\pmod j\) is restored, additive orthogonality
instead gives \(jI_{m_j}\) exactly. Division by \(\sqrt j\) proves
(160.CP4a). This complete block is a literal submatrix of the campaign's
\(1\le h<n\) range, not the deleted \(h=0\pmod n\) row.

### 3.3 Literal odd-\(n\) block and smooth-weight robustness

At \(g=1\), write \(C\asymp R\), \(J\asymp K\), so
\(C/J\asymp\Delta\). Add the following hypothesis solely for this
paragraph: for some \(j\asymp J\), the literal support contains a
buffered odd-\(n\) interval of physical length at least \(2j\), and its
joint smooth row amplitude equals \(A_0(1+O(\Delta^{-1}))\) there for
some \(A_0\ne0\). A run of \(j\) consecutive odd integers covers every
class modulo odd \(j\); for even \(j\), a run of \(j/2\) consecutive odd
integers covers every odd class and hence every unit class. Thus the
added interval hypothesis supplies one representative of every unit
class. The scale relation \(\Delta\to\infty\) makes this premise
geometrically compatible with a cell of length \(\asymp C\), but does not
prove the required nonvanishing interval.

On this block the literal smooth row factor varies relatively by
\(O(j/C)=O(\Delta^{-1})\). For \(1\le h\le j-1<n\),

\[
 e(-h/(jn))=1+O(C^{-1}).
\]

After row permutation and extraction of the unit diagonal
\(\chi_4(n)\), the weighted matrix is therefore \(A_0F_j+E_j\), where

\[
 \|E_j\|_{S_2}\ll |A_0|\Delta^{-1}j,
 \qquad
 \|E_j\|_{S_1}\ll |A_0|\Delta^{-1}j^{3/2}.
 \tag{160.CP14}
\]

Since \(j/\varphi(j)=j^{o(1)}\) and \(\Delta=X^a\), (160.CP14) is
negligible relative to the main nuclear norm. Thus, under the added
hypothesis, the projective inflation (160.CP5) survives on the selected
buffered block. This conditional robustness statement is not a claim that
the campaign's literal profile contains such a block, and it is only a
lower control on a positive projective norm.

### 3.4 Required power comparison

At \(g=1\), \(j\asymp K=X^\kappa\), where

\[
 \kappa=1+\ell-2\delta=1-2a-\ell>0.
 \tag{160.CP15}
\]

The required saving exponent is

\[
 \mu(a)=
 \begin{cases}
 a-1/4,&1/4<a\le1/3,\\
 (1-2a)/4,&1/3\le a<1/2.
 \end{cases}
 \tag{160.CP16}
\]

If \(a\le1/3\), the condition
\(\ell<1/2-a\), equivalent to \(\delta<1/2\), gives

\[
 \frac\kappa2-\mu(a)
 =\frac34-2a-\frac\ell2
 >\frac{1-3a}{2}\ge0.
 \tag{160.CP17}
\]

If \(a\ge1/3\),

\[
 \frac\kappa2-\mu(a)
 =\frac{1-2\delta}{4}>0.
 \tag{160.CP18}
\]

Thus \(K^{1/2-o(1)}\) absorbs at least the whole missing factor at every
fixed strict point. No uniform extra margin at an open face is claimed.

### 3.5 Fourier-bandwidth control

For completeness, (160.CP10) also exhibits the Sobolev tradeoff. Parseval
gives, for every \(h\),

\[
 \sum_{t\bmod j}|S(h,-t;j)|^2=j\varphi(j).
 \tag{160.CP19}
\]

For \(j=p\) prime, a stronger aggregate identity avoids any pointwise
Kloosterman estimate. For every nonzero \(t\bmod p\), orthogonality in
\(h\) gives

\[
 \sum_{h=1}^{p-1}|S(h,-t;p)|^2=p(p-1)-1,
 \tag{160.CP20}
\]

because the complete \(h\)-sum is \(p(p-1)\) and
\(S(0,-t;p)=c_p(t)=-1\). Therefore every fixed positive proportion of
centered frequencies with \(|t|_p\asymp p\) carries a fixed positive
proportion of the joint \((h,t)\) energy of the full nonzero-\(h\) block.
On an \(n\)-cell of length \(C\), the corresponding common tests
\(e(tn/p)\) have normalized oscillation \(|t|C/p\asymp C\). Hence, for
every fixed derivative order \(A>0\), the orthogonal Fourier realization
has joint vector Sobolev price at least a constant times \(C^A\). The
short displayed modulus has become a full modulus-frequency bandwidth.

## 4. First doubtful or unproved step

The exact reciprocity, Fourier expansion, singular spectrum, projective
lower bound, and exponent comparisons are algebraic. The first unproved
positive step is a new vector-valued level-\(4/8\) trace or large-sieve
theorem that acts on the literal full-rank \(j,n,h\) matrix before its
nuclear or Sobolev norm, retains \(\chi_4(g)\chi_4(n)\), covers the full
long-\(h\) range, and gains the boundary power after every spectral and
endpoint cost.

The buffered weighted-block paragraph uses the inherited fixed-profile
meaning of a nonzero flat component. If the campaign's literal profile
normalization does not provide a buffered region on which the active
profile is bounded away from zero, that paragraph must be weakened to the
unweighted kernel theorem. The algebraic no-low-projective-cost conclusion
for the inverse factor remains exact, but no lower bound for the literal
signed scalar follows in either formulation.

The prime-modulus high-frequency paragraph is an aggregate orthogonality
identity, not a pointwise Kloosterman estimate. Matching its joint
Sobolev price to any particular trace theorem still requires that theorem's
exact source normalization and vector-norm hypotheses.

## 5. Required controls and outcomes

1. **Parity and representatives:** pass. Equations (160.CP10) and
   (160.CP13) cover even and odd \(j\); odd \(n\)-runs cover all relevant
   unit classes.
2. **Centered nonzero frequency:** pass. Restricting to \(1\le h<j\)
   produces \(jI-{\bf1}{\bf1}^*\), while the literal block \(1\le h\le j\)
   gives \(jI\); neither is low rank.
3. **Full-\(h\) self-return:** pass as a no-gain control. For fixed \(g,n\),
   summing \(1\le h<n\) gives the original reciprocal row minus the already
   safe Ramanujan zero class.
4. **Primitive stratum:** pass. The decisive price already occurs at
   \(g=1\); no outer-\(g\) cancellation is credited.
5. **Moving profile and real centre:** conditional only, and not promoted.
   Equation (160.CP14) applies under the explicit lower-buffer hypothesis
   in Section 3.3; the campaign does not prove that premise.
6. **Residue and projective price:** pass. The exact nuclear norm is
   (160.CP4); neither residue indicators nor additive characters make the
   kernel low rank.
7. **Sobolev/Bessel bandwidth:** the joint prime-modulus orthogonality
   diagnostic passes; matching it to a particular trace theorem still
   requires its exact printed vector norm.
8. **Boundary power:** pass pointwise in the strict polytope by
   (160.CP17)--(160.CP18).
9. **Source and spectral ledger:** supplied only by the separate
   Round-160 source audit and its independent source-level seam. They
   retain the long-\(h\) complement and every compatible induced level
   and spectral piece; this candidate does not independently certify
   those source claims.
10. **Scope:** pass. This is a canonical scalarization obstruction, not a
    lower bound, a vector-theorem impossibility, or a result for any other
    owner.

## 6. Dependencies and exact artifacts used

The exact accepted dependencies are:

- `M9-M2-unbalanced-truncated-divisor-fixed-centre-return`;
- `M9-M2-unbalanced-Kloosterman-dispersion-interface-obstruction`;
- `M9-M2-unbalanced-level-four-spectral-matrix-obstruction`;
- `M9-M2-unbalanced-flat-wave-curvature-envelope`;
- `M9-M2-character-factor`;
- `Divisor-bound-elementary`.

The exact Round-160 inputs are:

- `strategy/round160_m2_unbalanced_inverse_selector_reciprocity_strategy.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/candidates/conductor_round160_reciprocity_seed.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/inverse_selector_reciprocity_attack.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/blind_reciprocity_matrix_rederivation.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/reciprocity_projective_source_audit.md`; and
- for the post-draft scope repairs,
  `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/post_blind_reciprocity_projective_seam.md`.

The inherited source and normalization boundary is recorded in:

- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/candidates/conductor_round143_level_four_matrix_obstruction.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/conductor_round143_level_four_matrix_adjudication.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/source_post_unmask_spectral_claims_audit.md`.

No numerical experiment, average over \(X\), or erased gcd stratum is used.
The projective and prime-modulus bandwidth calculations are algebraic apart
from the elementary totient lower bound. Application of a spectral theorem
remains source-review dependent.

## 7. Recommended state effect

Subject to independent verification and source/power review, create one
scoped obstruction recording (160.CP2)--(160.CP5), the exact Fourier
expansion (160.CP10), the primitive-\(g=1\) power comparison
(160.CP17)--(160.CP18), and the conclusion that additive reciprocity does
not supply a low-projective-cost scalar common-test decomposition.

Retain `M9-M2-smooth-unbalanced-three-quarter-estimate` as open. Do not
change M2, M9, the bridge, the quarter target, or any global exponent. A
future return to this exact surface requires a genuinely vector-valued
literal-matrix theorem with complete long-frequency, level-\(4/8\),
profile, endpoint, and restored-power control.
