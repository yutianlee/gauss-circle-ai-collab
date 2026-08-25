# Round 160 post-blind reciprocity/projective seam review

Campaign: `m9-m2-unbalanced-inverse-selector-reciprocity-gate`

Role: post-unmask seam reviewer.  This is review evidence only and changes no
proof status.

Task: post_blind_reciprocity_projective_seam

Starting graph SHA-256:
4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d

Generated at: 2026-08-25T18:45:16+08:00

## 1. Result

**Result: revise the conductor candidate, while promoting its unweighted
algebraic kernel.**  The reciprocity sign, inverse representatives, even-
(j) case, ordinary Kloosterman convention, complete-(h) reconstruction,
and single (h=0) deletion are all correct.  The exact nonzero-residue
kernel calculation is also correct:

\[
 F_{j,A}F_{j,A}^{*}=jI_M-\mathbf 1\mathbf 1^{*}
 \qquad(A\subseteq(\mathbb Z/j\mathbb Z)^*,\ |A|=M),
\tag{160.PR1}
\]

so its rank, singular values, nuclear norm, and Hilbert rank-one
projective lower bound are unconditional.  The complete residue-block map
in the long (h)-range has the sharp norm

\[
 \|P_{n,j}\|_{2\to2}
 =\sqrt{\left\lceil\frac{n-1}{j}\right\rceil},
\tag{160.PR2}
\]

and the primitive (g=1) exponent comparisons in the candidate are
algebraically correct at every fixed strict exponent point.

These facts prove a narrow no-go: **exact termwise Hilbert scalarization of
the unweighted inverse-residue kernel, followed by a triangle inequality,
is neither rank-free nor low-projective-cost.**  They do not by themselves
prove the same lower price for the literal moving weighted matrix.  The
frozen packet and authoritative graph provide upper support, size, and
variation information, but no quantified interval on which the joint
factor

\[
 W\!\left(\frac{X}{nD}\right)
 q_L\!\left(\frac{4Xj}{n^2}\right)
\tag{160.PR3}
\]

is uniformly bounded away from zero while a full set of unit residue
classes (n\bmod j) occurs.  Consequently the buffered-profile paragraph
and (160.CP14) are valid only after adding an explicit lower-buffer and
relative-smoothness hypothesis.  They are not presently an unconditional
statement about the literal owner.

Finally, neither the unweighted nuclear norm nor the conditional buffered
version rules out a bespoke vector-valued theorem acting on the actual
((j,n,h)) array, including (S(N_0,h;n)), before positive norms.  No
owner estimate, strict owner-complete range, or universal projective
impossibility follows.

## 2. Exact statement and hypotheses

Let (e(z)=e^{2\pi iz}), let (g,n) be odd, let (j\ge1) with
((j,n)=1), and use the Round-143 ordinary convention

\[
 S(a,b;n)=\sum_{x\bmod n}^{*}
 e\!\left(\frac{a\bar x+bx}{n}\right).
\tag{160.PR4}
\]

The blind convention

\[
 \sum_{x\bmod n}^{*}e\!\left(\frac{ax+b\bar x}{n}\right)
\]

is identical to (160.PR4) after the bijection (x\mapsto\bar x); it is
not a different sign convention.  With the fixed switched-cusp
normalization,

\[
 S^{\chi_4}_{\infty0}(4N_0,h;2n)=\chi_4(n)S(N_0,h;n)
\tag{160.PR5}
\]

for every (h) and arbitrary ((N_0,n)).

The exact post-reciprocity quadruple summand is therefore

\[
 \frac{\chi_4(g)\chi_4(n)}{gnj}
 W\!\left(\frac{X}{gnD}\right)
 q_L\!\left(\frac{4Xj}{gn^2}\right)
 e\!\left(\frac{\xi j}{n}+\frac{h\bar n_j}{j}
                -\frac{h}{jn}\right)S(N_0,h;n),
\tag{160.PR6}
\]

with the literal membership (j\in\mathcal J_{g,n}), coprimality,
zero extension, entries, exits, and endpoints retained.  No parity
condition on (j) and no coprimality condition on (N_0) or (h) is
added.

For (j>1), (A\subseteq U_j=(\mathbb Z/j\mathbb Z)^*), and
(|A|=M), define

\[
 F_{j,A}(a,h)=e(h\bar a_j/j),
 \qquad a\in A,\quad 1\le h\le j-1.
\tag{160.PR7}
\]

Then (160.PR1) holds and hence

\[
 \begin{aligned}
 \operatorname{rank}F_{j,A}&=M,\\
 \operatorname{sing}(F_{j,A})
   &=\{\sqrt j\ (M-1\text{ times}),\sqrt{j-M}\},\\
 \|F_{j,A}\|_{S_1}&=(M-1)\sqrt j+\sqrt{j-M},\\
 \|F_{j,A}\|_{S_2}^2&=M(j-1).
 \end{aligned}
\tag{160.PR8}
\]

For (A=U_j), this is exactly (160.CP2)--(160.CP4).  Equally, if all
residues (s\bmod j) are retained and the kernel is normalized by
(j^{-1/2}), its rows are orthonormal, giving the blind report's rank
(M), operator norm (1), and nuclear norm (M).  These are compatible
statements: (160.PR8) shows that even deleting the (s=0) column leaves
full row rank.  The deleted original frequency is (h=0\pmod n), not the
positive frequencies (h\equiv0\pmod j).

The weighted robustness claim requires an additional hypothesis not in
the frozen packet.  A sufficient version is: for some fixed (j\asymp K)
there is an odd-(n) interval (I) containing one representative (n_a)
of every (a\in A), a number (A_0\ne0), and (eta=o(M/j)) such that,
after extracting the unit diagonal \(\chi_4(n_a)\), the literal row
amplitude satisfies

\[
 A(n_a)=A_0(1+O(\eta))
\tag{160.PR9}
\]

uniformly in (a), with all (n_a) lying inside the literal support.
If (I) is a genuine fixed-width buffer, the normalized smoothness would
give (eta\ll j/C\asymp\Delta^{-1}), and the correction
(e(-h/(jn_a))) is (1+O(C^{-1})) for (1\le h<j).  Under these added
hypotheses the perturbation argument behind (160.CP14) is valid.  The
existence of such (I,A_0), and representatives is precisely the
unproved lower-control seam.

## 3. Proof and seam derivation

Choose inverse representatives (u=\bar j_n) and (v=\bar n_j).
The integer (ju+nv-1) is divisible by both (j) and (n), hence by
(jn).  Therefore

\[
 -\frac{u}{n}\equiv\frac{v}{j}-\frac1{jn}\pmod1,
\]

which proves

\[
 e(-h\bar j_n/n)=e(h\bar n_j/j-h/(jn)).
\tag{160.PR10}
\]

Changing either inverse representative changes the exponent by an
integer.  The proof uses only ((j,n)=1), so even (j) is covered.  The
Fourier expansion in the candidate also has the correct signs:

\[
 1_{(n,j)=1}e(h\bar n_j/j)
 =\frac1j\sum_{t\bmod j}S(h,-t;j)e(tn/j),
\tag{160.PR11}
\]

because summing over (t) forces the Kloosterman variable to equal
(n\pmod j).

For reconstruction, use (160.PR4) and sum a complete system
(h\bmod n):

\[
 \begin{aligned}
 &\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)\\
 &\quad=\frac1n\sum_j b_{g,n}(j)
 \sum_{x\bmod n}^{*}e(N_0\bar x/n)
 \sum_{h\bmod n}e(h(x-\bar j_n)/n)\\
 &\quad=\sum_j b_{g,n}(j)e(N_0j/n).
 \end{aligned}
\tag{160.PR12}
\]

Together with (e(\xi j/n)) inside (b_{g,n}(j)), this gives
(e(Xj/n)) and reconstructs the original reciprocal row exactly.  At
(h=0), the omitted term is exactly

\[
 \sum_{g,n}\chi_4(g)\chi_4(n)W\!\left(\frac{X}{gnD}\right)
 \frac{c_n(N_0)}n\sum_j b_{g,n}(j),
\tag{160.PR13}
\]

which is the already accepted target-safe zero class.  Thus
(1\le h<n) is full inversion minus (160.PR13), once.  Positive
multiples (h=mj) remain and cannot be deleted as a second zero row.

For the residue kernel, if (a,b\in A), additive orthogonality gives

\[
 \sum_{h=1}^{j-1}e(h(\bar a-\bar b)/j)
 =\begin{cases}j-1,&a=b,\\-1,&a\ne b,\end{cases}
\]

which is (160.PR1).  Since (M\le\varphi(j)\le j-1), its eigenvalues
are (j) with multiplicity (M-1) and (j-M>0) once.  This proves
(160.PR8).  Every exact Hilbert rank-one representation
(F_{j,A}=\sum_su_sv_s^*) has at least (M) terms and satisfies

\[
 \sum_s\|u_s\|_2\|v_s\|_2\ge\|F_{j,A}\|_{S_1}.
\tag{160.PR14}
\]

For (M\ge2), (160.PR8) gives

\[
 \frac{\|F_{j,A}\|_{S_1}}{\|F_{j,A}\|_{S_2}}
 \gg\sqrt M.
\tag{160.PR15}
\]

This proves the unconditional canonical scalarization obstruction, but
only for an exact factorization of this kernel followed termwise by a
triangle inequality.

For the long block, the rows of (P_{n,j}) have disjoint supports of
sizes

\[
 m_s=\#\{1\le h<n:h\equiv s\pmod j\}.
\]

Thus (P_{n,j}P_{n,j}^*=\operatorname{diag}(m_s)), proving
(160.PR2), including sharpness.  Moreover, for
(1\le m\le\lfloor(n-1)/j\rfloor),

\[
 e(mj\bar n_j/j)=1,
 \qquad e(-mj/(jn))=e(-m/n)=1+O(1/j).
\tag{160.PR16}
\]

Hence the short reciprocal phase supplies no oscillation on this
(\asymp n/j\asymp\Delta) subfamily.  Both (160.PR2) and (160.PR16)
are universal capacity controls, not lower bounds for the actual
(S(N_0,h;n))-weighted sum.

At (g=1), (j\asymp K=X^\kappa) with

\[
 \kappa=1+\ell-2\delta=1-2a-\ell>0,
 \qquad a=\delta-\ell.
\]

Writing the missing exponent as (mu(a)), the candidate's comparisons
are exact:

\[
 \frac\kappa2-\mu(a)
 =\begin{cases}
 \frac34-2a-\frac\ell2>\frac{1-3a}{2}\ge0,&a\le1/3,\\[1mm]
 \frac{1-2\delta}{4}>0,&a\ge1/3.
 \end{cases}
\tag{160.PR17}
\]

Also (a/2-\mu(a)>0) in both branches.  Using
(\varphi(j)\gg_\varepsilon j^{1-\varepsilon}), the full unweighted
kernel inflation (K^{1/2-o(1)}) and the long-block scale
(X^{a/2}) each exceed the missing power at every **fixed** strict
point.  This has no polytope-uniform margin as an open face is approached,
and it becomes a statement about the literal weighted owner only if the
missing class-coverage/lower-buffer hypothesis is proved.

## 4. First doubtful or unproved step

The first unproved step is the sentence in Section 3.3 of the conductor
candidate asserting that a complete odd-(n) residue block lies in a
literal buffered nonzero profile cell with relative variation
(O(\Delta^{-1})).  The parity count itself is correct: (j) consecutive
odd integers (physical span (<2j)) cover all classes modulo odd (j),
while (j/2) consecutive odd integers cover all odd classes modulo even
(j).  Since (C/j\asymp\Delta\to\infty), such a block fits inside an
interval of width comparable to (C).

What is absent is proof that the **joint literal active support contains
such an interval and has a nonzero reference amplitude there**.  The
accepted profile statements available in the frozen context give upper
bounds such as

\[
 |b_{g,n}(j)|\ll K^{-1}X^\varepsilon,
 \quad \sum_j|b_{g,n}(j)|\ll g^{-1}X^\varepsilon,
 \quad \sum_j|b_{g,n}(j)|^2\ll(gK)^{-1}X^\varepsilon,
\]

and the dyadic denominator profile has upper regularity and aggregate
nondegeneracy.  None states a uniform lower bound for the moving joint
product (160.PR3), a fixed (j) for which it holds through a complete
unit-class block, or relative derivative control after division by a
nonzero (A_0).  Upper bounds and zero extension alone allow a weighted
row restriction to have much smaller rank or nuclear norm than the
unweighted kernel.  Therefore (160.CP14) is a sound perturbation
calculation **conditional on** (160.PR9), but the literal profile has not
been shown to satisfy its premise.

Even after such a buffer is supplied, this controls only the smoothly
weighted inverse-factor submatrix.  Entrywise multiplication by the
actual Kloosterman array (S(N_0,h;n)), or a joint treatment retaining
that array before scalarization, need not preserve the unweighted nuclear
lower bound.  The next positive step would be a new coefficient-sensitive
vector theorem with complete long-(h), character, level-(4/8), moving
support, endpoint, and restored-power control.  No source theorem or
internal lemma in the reviewed packet supplies it.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Reciprocity sign, representatives, even/odd (j) | **PASS.** (160.PR10) is exact and parity-free. |
| Ordinary Kloosterman convention | **PASS.** The blind and Round-143 formulas differ only by \(x\leftrightarrow\bar x\); (160.PR5) supplies exactly \(\chi_4(n)\), with no extra sign or root of unity. |
| Literal post-reciprocity scalar | **PASS.** (160.PR6) has normalization (1/(gnj)), both character directions, real-centre factor, correction phase, support, and arbitrary ((N_0,n)). |
| Complete (h)-reconstruction | **PASS.** (160.PR12) returns the original (e(Xj/n)) row exactly. |
| (h=0) deletion | **PASS.** (160.PR13) is removed once; (h=mj>0) is not another deleted zero class. |
| Residue rank and nuclear norm | **PASS.** (160.PR8) verifies (160.CP2)--(160.CP4); the blind all-residue normalized matrix is also correct. |
| Exact Hilbert projective price | **PASS with scope.** (160.PR14)--(160.PR15) apply to exact rank-one scalarization plus triangle, not to arbitrary coefficient-sensitive vector methods. |
| Long-(h) block norm | **PASS with scope.** (160.PR2) is sharp and (160.PR16) is exact, but neither is a signed lower bound for the literal coefficient vector. |
| Primitive (g=1) and boundary power | **PASS pointwise.** (160.PR17) is strict at each fixed exponent point; no uniform open-face margin is proved. |
| Moving support and weighted-matrix lower control | **FAIL unconditionally / PASS conditionally.** The perturbation estimate is valid under (160.PR9), but the frozen literal profile supplies no such lower-buffer theorem. |
| Fourier/Sobolev diagnostic | **PASS algebraically only.** (160.CP19)--(160.CP20) follow from Parseval; translation into a particular automorphic Sobolev or Bessel norm remains unproved. |
| Bespoke vector theorem and spectral ledger | **OPEN.** No impossibility statement applies to a theorem acting on the full literal matrix before positive norms. |
| Owner and downstream scope | **PASS.** No target, strict range, M2, M9, bridge, or global exponent follows. |

No numerical test or external source was used.  All successful controls are
finite algebra, orthogonality, or elementary norm calculations.

## 6. Dependencies and exact artifacts used

The review used:

- `protocol.md`;
- `state/proof_obligations.yml`, in particular the frozen target, the
  accepted inverse-first return, character factor, dyadic-profile
  infrastructure, flat-wave envelope, and Round-143 matrix obstruction;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/blind_reciprocity_matrix_rederivation.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/candidates/conductor_round160_reciprocity_projective_obstruction.md`; and
- solely for the ordinary/generalized Kloosterman normalization,
  `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/candidates/conductor_round143_level_four_matrix_obstruction.md`.

The proof uses only additive reciprocity, finite Fourier orthogonality,
Schatten norm identities, the elementary totient lower bound, and the
accepted Round-143 cusp identity.  No claim graph, proof draft, validation
matrix, synthesis, or other shared state was edited.

## 7. Recommended state effect

1. **PROMOTE** (160.CP13)/(160.PR10), including representative and parity
   scope.
2. **PROMOTE** the ordinary Kloosterman convention match,
   (160.PR5)--(160.PR6), and the exact additive expansion (160.CP10).
3. **PROMOTE** the full-(h) reconstruction and the exactly-once zero-row
   deletion, (160.PR12)--(160.PR13).
4. **PROMOTE** (160.CP2)--(160.CP4), preferably in the stronger subset
   form (160.PR8), and **PROMOTE** (160.CP5) only under the explicit label
   `unweighted_exact_Hilbert_scalarization_plus_triangle`.
5. **PROMOTE** the blind full-residue orthonormal-row theorem and the
   sharp long-block norm (160.R11), while **REVISE** any wording that turns
   either universal operator capacity into a signed lower bound for the
   actual coefficient array.
6. **PROMOTE** (160.CP17)--(160.CP18) and the long-block exponent
   comparison only for each fixed strict exponent pair.  **REVISE**
   “throughout the strict polytope” if it is meant uniformly up to an open
   face.
7. **RETAIN CONDITIONALLY / DO NOT PROMOTE** the buffered weighted-block
   statement and (160.CP14).  Promote it later only after proving an exact
   lower-buffer, complete-class-coverage, and relative-smoothness lemma for
   the literal moving profile.  The present authoritative hypotheses do
   not provide that lemma.
8. **PROMOTE AS DIAGNOSTIC ONLY** (160.CP19)--(160.CP20).  **REJECT** any
   source-independent automorphic Sobolev conclusion drawn from them.
9. **REJECT** the broad claims that reciprocity obstructs every lawful
   projective realization, that the unweighted nuclear norm lower-bounds
   the literal Kloosterman-weighted matrix, or that a bespoke vector-valued
   theorem is impossible.
10. **REJECT** promotion of the owner target or any strict owner-complete
    range.  Retain `M9-M2-smooth-unbalanced-three-quarter-estimate` and all
    downstream obligations open.  The promotable outcome is only the
    scoped unconditional canonical-scalarization no-go, separated from
    the conditional buffered-profile robustness and from the still-open
    bespoke-vector route.
