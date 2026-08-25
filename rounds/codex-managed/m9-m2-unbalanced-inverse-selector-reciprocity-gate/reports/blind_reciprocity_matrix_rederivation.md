# Round 160 statement-only blind reciprocity-matrix rederivation

Campaign: m9-m2-unbalanced-inverse-selector-reciprocity-gate

Task: blind_reciprocity_matrix_rederivation

Role: statement-only blind rederiver

Starting graph SHA-256:
4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d

Generated at: 2026-08-25T18:35:27+08:00

## 1. Result: exact lemma and scoped no-go result

**Result.** Additive reciprocity is exact, including for even \(j\), and gives the termwise scalar

\[
 \boxed{
 C(g,n,j,h)=
 \frac{\chi _4(g)\chi _4(n)}{gnj}
 W\!\left(\frac{X}{gnD}\right)
 q_L\!\left(\frac{4Xj}{gn^2}\right)
 e\!\left(\frac{\xi j}{n}+\frac{h\overline n_j}{j}
             -\frac{h}{jn}\right)
 S(N_0,h;n) }
\tag{160.R1}
\]

for every admitted \(g,n,j\) and every \(1\leq h<n\). Adding the single row \(h=0\), and then summing a complete set of residues \(h\pmod n\), returns exactly

\[
 \sum_{\substack{g,n\ {\rm odd}\\gn\asymp R}}
 \chi _4(g)\chi _4(n)W\!\left(\frac{X}{gnD}\right)
 \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
 \frac{q_L(4Xj/(gn^2))}{gj}\,e(Xj/n).
\tag{160.R2}
\]

Thus the \(1\le h<n\) expression is (160.R2) minus the zero row exactly once.

There is, however, a rigorous reciprocity-only obstruction to the proposed short-modulus common-test mechanism. For fixed \(j\), the matrix

\[
 \mathcal F_j(r,s)=j^{-1/2}e(s\overline r_j/j),
 \qquad r\in(\mathbb Z/j\mathbb Z)^\times,
 \quad s\in\mathbb Z/j\mathbb Z,
\tag{160.R3}
\]

has orthonormal rows. Consequently it has rank \(\varphi(j)\), all its nonzero singular values are \(1\), and its Hilbert projective (nuclear) norm is exactly \(\varphi(j)\). On any set of \(M\) actually occurring \(n\bmod j\) classes, the corresponding quantities are \(M\), \(1\), and \(M\). Hence an exact common-test decomposition needs at least \(M\) tests and projective cost at least \(M\); a Bessel/Cauchy use is sharp and is necessarily a positive norm, not a signed power saving.

The complete long range supplies a second exact obstruction. Writing \(h=qj+s\), the reciprocal phase depends only on \(s\), while the map that collapses the \(h\)-range to \(s\pmod j\) has sharp \(\ell^2\) norm

\[
 \sqrt{\left\lceil\frac{n-1}{j}\right\rceil}\asymp \sqrt{\Delta}.
\tag{160.R4}
\]

In particular, the \(\lfloor(n-1)/j\rfloor\asymp\Delta\) positive frequencies \(h=mj\) have \(e(h\overline n_j/j)=1\). They receive no signed cancellation at all from the short reciprocal phase. The correction \(e(-m/n)\) varies by only \(O(1/j)\) over this whole subfamily.

Therefore additive reciprocity alone yields neither (160.BL6) nor any strict owner-complete subrange. It supplies no negative power with which to meet (160.BL7). This is a scoped no-go for a residue-class-free or low-projective-cost reciprocity argument, not a disproof of (160.BL6): a successful proof would need new cancellation in the actual \(S(N_0,h;n)\)-weighted coefficient array, with the class, long-frequency, moving-support, and spectral norms all proved.

## 2. Exact statement and hypotheses

Let \(e(z)=e^{2\pi iz}\). Retain all hypotheses (160.BL1)--(160.BL5), including odd \(g,n\), arbitrary \((N_0,n)\), unrestricted parity of \(j\), literal moving support \(\mathcal J_{g,n}\) with zero extension, and all \(1\le h<n\). Use the standard Kloosterman convention implicit in (160.BL5),

\[
 S(N_0,h;n)=\sum_{x\in(\mathbb Z/n\mathbb Z)^\times}
 e\!\left(\frac{N_0x+h\overline x_n}{n}\right).
\tag{160.R5}
\]

The statement proved here has four parts.

1. For every coprime positive \(j,n\), for arbitrary integral representatives of the inverses, and for every integer \(h\),
   \[
   e(-h\overline j_n/n)
   =e(h\overline n_j/j-h/(jn)).
   \tag{160.R6}
   \]
   No parity assumption on \(j\) is needed.

2. Substitution of (160.R6) and (160.BL5) into (160.BL4) gives (160.R1), with no omitted sign, character, support, endpoint, or real-centre factor. Complete \(h\)-summation gives (160.R2), and the removed row is
   \[
   \sum_{\substack{g,n\ {\rm odd}\\gn\asymp R}}
   \chi_4(g)\chi_4(n)W\!\left(\frac{X}{gnD}\right)
   \frac{c_n(N_0)}{n}
   \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}b_{g,n}(j),
   \tag{160.R7}
   \]
   where \(c_n(N_0)=S(N_0,0;n)\). This formula is valid without \((N_0,n)=1\).

3. For every subset \(\mathcal A\subseteq(\mathbb Z/j\mathbb Z)^\times\) of cardinality \(M\), the restriction \(\mathcal F_{j,\mathcal A}\) of (160.R3) to \(r\in\mathcal A\) satisfies
   \[
   \mathcal F_{j,\mathcal A}\mathcal F_{j,\mathcal A}^{*}=I_M,
   \quad \operatorname{rank}\mathcal F_{j,\mathcal A}=M,
   \quad \|\mathcal F_{j,\mathcal A}\|_{2\to2}=1,
   \quad \|\mathcal F_{j,\mathcal A}\|_{S_1}=M.
   \tag{160.R8}
   \]
   Every exact Hilbert rank-one representation
   \(\mathcal F_{j,\mathcal A}=\sum_{t=1}^T a_t b_t^*\) has
   \[
   T\ge M,
   \qquad
   \sum_{t=1}^T\|a_t\|_2\|b_t\|_2\ge M.
   \tag{160.R9}
   \]

4. If \(P_{n,j}:\mathbb C^{\{1,\ldots,n-1\}}\to
   \mathbb C^{\mathbb Z/j\mathbb Z}\) is the residue-block sum
   \[
   (P_{n,j}A)(s)=\sum_{\substack{1\le h<n\\h\equiv s\ (j)}}A(h),
   \tag{160.R10}
   \]
   then
   \[
   \|P_{n,j}\|_{2\to2}
   =\sqrt{\max_s\#\{1\le h<n:h\equiv s\pmod j\}}
   =\sqrt{\left\lceil\frac{n-1}{j}\right\rceil}.
   \tag{160.R11}
   \]
   This norm is attained. Thus it cannot be removed by a universal signed inequality.

These conclusions are confined to the scalar (160.BL4) in the stated flat-smooth strict-UNBAL owner.

## 3. Proof and derivation

### 3.1 Reciprocity, representatives, and parity

Choose any integers \(u,v\) satisfying

\[
 ju\equiv1\pmod n,
 \qquad nv\equiv1\pmod j.
\]

The integer \(ju+nv-1\) is divisible by \(n\): both \(ju-1\) and \(nv\) are. It is also divisible by \(j\): both \(ju\) and \(nv-1\) are. Since \((j,n)=1\), it is divisible by \(jn\). Therefore

\[
 -\frac{u}{n}-\frac{v}{j}+\frac1{jn}\in\mathbb Z,
\]

and multiplication by \(h\), followed by \(e(\cdot)\), proves (160.R6). Replacing \(u\) by \(u+tn\) or \(v\) by \(v+sj\) changes the exponent by an integer, so the identity is independent of representatives. The argument uses only \((j,n)=1\). In particular it remains valid when \(j\) is even and \(n\) is odd. If \(j=1\), the same congruence statement is interpreted with any representative modulo \(1\), and the displayed exponential identity still holds.

### 3.2 Complete scalar

Insert (160.BL2), (160.BL3), and (160.BL5) in (160.BL4), and then use (160.R6). The summand attached to one quadruple \((g,n,j,h)\) is

\[
 \chi_4(g)W\!\left(\frac{X}{gnD}\right)
 \frac1n\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n)
 e(h\overline n_j/j-h/(jn))\chi_4(n)S(N_0,h;n),
\]

which is exactly (160.R1). In particular:

- the normalization is \(1/(gnj)\), not \(1/(gj)\) or \(1/(nj)\);
- the two character directions remain as \(\chi_4(g)\chi_4(n)\);
- the real-centre factor \(e(\xi j/n)\) and the reciprocal correction \(e(-h/(jn))\) both remain;
- the indicator \(j\in\mathcal J_{g,n}\) and \((j,n)=1\) remain literal;
- no assumption on \((N_0,n)\) or on \((h,n)\) has entered.

At the fixed level-four normalization in the statement, the entire level factor is exactly the unit-modulus scalar \(\chi_4(n)\) in (160.BL5). Reciprocity creates no new level-\(4\) or level-\(8\) Kloosterman identity at modulus \(j\); it creates only an additive phase of modulus \(j\). Thus a later level-\(4/8\) spectral conversion would be an additional theorem, not part of this algebra.

### 3.3 Full-\(h\) self-return and the single centered deletion

Extend \(h\) temporarily to a complete residue system \(0\le h<n\). From (160.BL3) and (160.R5),

\[
\begin{aligned}
 \sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
 &=\frac1n\sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}b_{g,n}(j)
   \sum_{x\in(\mathbb Z/n\mathbb Z)^\times}e(N_0x/n)
   \sum_{h\bmod n}e\!\left(\frac{h(\overline x_n-\overline j_n)}n\right)\\
 &=\sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
   b_{g,n}(j)e(N_0j/n).
\end{aligned}
\tag{160.R12}
\]

The inner orthogonality condition \(\overline x_n=\overline j_n\) is equivalent to \(x=j\pmod n\), since inversion permutes the units. Multiplying by \(\chi_4(g)\chi_4(n)W(X/(gnD))\), and using \(N_0+\xi=X\), gives (160.R2).

At \(h=0\),

\[
 \widehat\gamma_{g,n}(0)=\frac1n\sum_j b_{g,n}(j),
 \qquad S(N_0,0;n)=c_n(N_0),
\]

which gives (160.R7). Hence (160.BL4) is full Fourier inversion minus (160.R7), once. When \(h\) is later written \(qj+s\), the class \(s=0\) contains the positive integers \(j,2j,\ldots\); those are not the deleted \(h=0\pmod n\) row and may not be removed.

The same reconstruction follows after reciprocity, because

\[
 \frac{h\overline n_j}{j}-\frac{h}{jn}
 \equiv-\frac{h\overline j_n}{n}\pmod1
\]

term by term. Thus full \(h\)-summation is a genuine hostile self-return: it reconstructs the original reciprocal row, rather than producing an estimate.

### 3.4 The \(n\bmod j\) matrix and exact common-test price

For fixed \(g,j\), put \(r=n\bmod j\). Because \((n,j)=1\), \(r\in(\mathbb Z/j\mathbb Z)^\times\), and

\[
 e(h\overline n_j/j)=e(h\overline r_j/j).
\]

The remaining coefficient is not a function of \(r\) alone: it contains \(n\), \(S(N_0,h;n)\), \(e(-h/(jn))\), \(\chi_4(n)\), the moving membership \(j\in\mathcal J_{g,n}\), and the profile values. Thus grouping by \(r\) produces a family of residue-class tests, not one common test.

For \(r,r'\in\mathcal A\), direct additive orthogonality gives

\[
 \sum_{s\bmod j}e\!\left(\frac{s(\overline r_j-\overline {r'}_j)}j\right)
 =j\,\mathbf 1_{r=r'}.
\tag{160.R13}
\]

This proves (160.R8), since inversion is injective on the unit group. The rank bound in (160.R9) follows because a sum of \(T\) rank-one matrices has rank at most \(T\). The projective bound follows from the triangle inequality for the nuclear norm:

\[
 M=\|\mathcal F_{j,\mathcal A}\|_{S_1}
 \le\sum_t\|a_tb_t^*\|_{S_1}
 =\sum_t\|a_t\|_2\|b_t\|_2.
\]

This also proves sharpness of the positive Bessel norm. Indeed, for \(x\in\mathbb C^{\mathcal A}\) and \(y=\mathcal F_{j,\mathcal A}^*x\),

\[
 \|y\|_2=\|x\|_2,
 \qquad
 \langle x,\mathcal F_{j,\mathcal A}y\rangle=\|x\|_2^2.
\tag{160.R14}
\]

No universal inequality can insert a factor \(X^{-\eta}\), \(\eta>0\), on the right of this normalized pairing. Any such gain must prove that the actual Kloosterman-weighted vectors avoid the extremizing subspace; reciprocity supplies no such fact.

The tempting constant-coefficient signed sum is only

\[
 \sum_{r\in(\mathbb Z/j\mathbb Z)^\times}e(s\overline r_j/j)
 =c_j(s).
\tag{160.R15}
\]

It does not apply to the varying \(n\)-coefficients. Even in the constant case it has no saving for \(s=0\), since \(c_j(0)=\varphi(j)\).

Parity does not reduce the matrix. If \(j\) is even, every unit residue is odd, exactly matching odd \(n\). If \(j\) is odd, the odd integers run through all residues modulo \(j\). Arbitrary inverse representatives give the same rows. A character expansion also cannot lower the exact dimension: on the unit group it is merely another basis for this rank-\(\varphi(j)\) matrix, and nonunit \(h\bmod j\) require their gcd strata rather than disappearing.

For a discrete Sobolev audit, let \(u_k(s)=j^{-1/2}e(sk/j)\), where \(k=\overline r_j\), and let \(\nabla u(s)=u(s+1)-u(s)\) cyclically. Then, exactly,

\[
 \|(j\nabla)^A u_k\|_2
 =\bigl(j|e(k/j)-1|\bigr)^A.
\tag{160.R16}
\]

Thus a normalized-coordinate Sobolev treatment must retain these frequencies; it cannot label every residue row as one uniformly low-complexity test. On \(M\) distinct rows, their centered frequencies are distinct, so the largest centered frequency is at least \((M-1)/2\), and (160.R16) gives a corresponding polynomial Sobolev cost. The precise automorphic Sobolev/Bessel norm and any level-\(4/8\) transform theorem are not supplied in the frozen statement, so no smaller spectral price can be asserted.

### 3.5 The complete long-\(h\) complement

For fixed \(n,j,r\), define

\[
 A_{n,j}(h)=\mathbf 1_{1\le h<n}
 e(-h/(jn))S(N_0,h;n).
\]

Then

\[
 \sum_{1\le h<n}A_{n,j}(h)e(h\overline r_j/j)
 =\sum_{s\bmod j}(P_{n,j}A_{n,j})(s)e(s\overline r_j/j).
\tag{160.R17}
\]

The rows of \(P_{n,j}\) have disjoint supports and squared row norms

\[
 m_s=\#\{1\le h<n:h\equiv s\pmod j\}.
\]

Hence \(P_{n,j}P_{n,j}^*=\operatorname{diag}(m_s)\), proving (160.R11). The bound is attained by an \(A\) constant on a residue class of maximum size. In the present scales,

\[
 \frac nj\asymp\frac RK=\frac DL=\Delta=X^a,
 \qquad a=\delta-\ell,
\tag{160.R18}
\]

so this sharp cost is \(\asymp X^{a/2}\).

More concretely, for

\[
 1\le m\le\left\lfloor\frac{n-1}{j}\right\rfloor,
 \qquad h=mj,
\]

one has

\[
 e(h\overline n_j/j)=1,
 \qquad e(-h/(jn))=e(-m/n).
\tag{160.R19}
\]

Moreover \(m/n<1/j\), so \(|e(-m/n)-1|\le 2\pi/j\). Thus neither part of the reciprocal phase oscillates meaningfully across these \(\asymp\Delta\) positive frequencies. Cancellation here would have to come from \(S(N_0,mj;n)\) or from another variable, not from the short \(j\)-modulus.

### 3.6 Moving support, endpoints, and level factors

Zero extension makes every reordering algebraically exact. For example, at fixed \(g,j\), define on the odd \(n\)-lattice

\[
 B_{g,j}(n)=\mathbf 1_{gn\asymp R}
 \mathbf 1_{j\in\mathcal J_{g,n}}
 \mathbf 1_{(j,n)=1}
 \frac{\chi_4(n)}{gnj}
 W\!\left(\frac{X}{gnD}\right)
 q_L\!\left(\frac{4Xj}{gn^2}\right)e(\xi j/n),
\tag{160.R20}
\]

and set it to zero elsewhere. Any summation-by-parts or Sobolev argument in \(n\) must pay the literal discrete variation

\[
 V_{g,j}=\sum_{n\ {\rm odd}}|B_{g,j}(n+2)-B_{g,j}(n)|.
\tag{160.R21}
\]

Every entrance to and exit from the moving support contributes its boundary jump to (160.R21). It is not legitimate to keep only derivatives in the interior. The frozen statement supplies no quantitative bound for (160.R21), for higher differences, or for a projective decomposition of the moving profiles, so a positive owner-complete spectral estimate cannot be closed from the permitted data.

The factor \(\chi_4(n)\) in (160.R20) has absolute price \(1\), but it cannot in general be pulled through the \(n\bmod j\) grouping: depending on the parity and \(2\)-adic class of \(j\), \(n\bmod4\) may also depend on the quotient in \(n=qj+r\). Splitting odd/even and finer \(2\)-adic \(j\)-classes is algebraically harmless and costs at most the number of retained strata under a triangle inequality, but no cancellation between them is furnished by reciprocity. Most importantly, (160.BL5) leaves the Kloosterman modulus equal to \(n\). There is no licensed step replacing it by a level-\(4\) or level-\(8\) spectral object of modulus \(j\).

### 3.7 Restored powers and the target boundary

The allowed conditions imply

\[
 \frac14<a=\delta-\ell<\frac12.
\]

The missing exponent in (160.BL7) is

\[
 s(a)=\min(a,(1-a)/2)-\frac14
 =\begin{cases}
 a-\frac14,&\frac14<a\le\frac13,\\[2mm]
 \frac{1-2a}{4},&\frac13\le a<\frac12,
 \end{cases}
\tag{160.R22}
\]

and is positive everywhere in the strict range.

The primitive \(g=1\) stratum remains present and has

\[
 n\asymp R=X^{1-\delta},
 \qquad j\asymp K=X^{1+\ell-2\delta}=X^{1-\delta-a},
 \qquad n/j\asymp X^a.
\tag{160.R23}
\]

Thus \(K\to\infty\), since \(1-\delta-a>1-2\delta>0\). In a complete residue-class family, even a single Bessel/Cauchy restoration has class scale

\[
 K^{1/2}=X^{(1-\delta-a)/2},
\tag{160.R24}
\]

up to the elementary \(j^{o(1)}\) distinction between \(j\) and \(\varphi(j)\), while the exact normalized projective cost is \(\varphi(j)\). This Bessel exponent is strictly larger than \(s(a)\): for \(a\le1/3\), it follows from \(\delta<1/2\), and for \(a\ge1/3\),

\[
 \frac{1-\delta-a}{2}-\frac{1-2a}{4}
 =\frac{1-2\delta}{4}>0.
\tag{160.R25}
\]

Likewise the sharp long-block restoration \(X^{a/2}\) is larger than \(X^{s(a)}\):

\[
 \frac a2-s(a)
 =\begin{cases}
 \frac14-\frac a2,&a\le1/3,\\[1mm]
 \frac{4a-1}{4},&a\ge1/3,
 \end{cases}
 \quad >0.
\tag{160.R26}
\]

Equations (160.R24)--(160.R26) are prices relative to a one-class or one-period normalization, not lower bounds for the final scalar: a deeper theorem could offset them. They do prove that an apparent saving of the size (160.R22) is completely unsupported if the class or long-block price is omitted. Since the normalized class transform has sharp norm \(1\), reciprocity itself contributes no compensating \(X^{-s(a)}\). No strict subrange follows.

## 4. First doubtful or unproved step

The first doubtful step in a positive reciprocity argument is the assertion that \(e(h\overline n_j/j)\) becomes one signed common test of low projective cost after grouping in the shorter modulus. If “common” means an exact representation across the occurring \(n\bmod j\) classes, (160.R8)--(160.R9) disprove it: the cost is exactly the number \(M\) of classes, and the Bessel bound is sharp. If “common” means an approximation adapted to the actual coefficients, the missing assertion is a new theorem that the array

\[
 \mathbf 1_{j\in\mathcal J_{g,n}}
 \chi_4(n)W\!\left(\frac{X}{gnD}\right)
 q_L\!\left(\frac{4Xj}{gn^2}\right)
 e\!\left(\frac{\xi j}{n}-\frac{h}{jn}\right)S(N_0,h;n)
\]

has small projective/Sobolev norm or avoids the extremizers in (160.R14), uniformly through the moving endpoints and every gcd and \(2\)-adic stratum. No such input occurs in the frozen statement. The positive frequencies \(h=mj\) in (160.R19) show that this missing theorem cannot come from the reciprocal phase alone.

In addition, the statement gives no quantitative derivative/variation hypotheses for \(q_L\), \(W\), or the moving sets, and no level-\(4/8\) spectral theorem on the \(j\)-side. Those are source and norm gaps for any claimed target estimate, although they are not needed for the exact no-go result above.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| exact_inverse_selector_reciprocity | **PASS.** The divisibility of \(j\overline j_n+n\overline n_j-1\) by \(jn\) proves (160.R6). |
| even_odd_j_and_representatives | **PASS.** The proof uses only coprimality. Even \(j\) is allowed, and changing either inverse representative changes the exponent by an integer. |
| centered_h_nonzero_once | **PASS.** BL4 contains precisely \(1\le h<n\). Formula (160.R7) is the one missing \(h=0\pmod n\) row. Positive multiples \(h=mj\) remain. |
| full_h_self_return | **PASS.** Complete \(h\pmod n\) orthogonality gives (160.R12) and reconstructs (160.R2) exactly. |
| primitive_g1 | **PASS.** No step removes \(g=1\). The obstruction persists at \(n\asymp R\), \(j\asymp K\), \(n/j\asymp\Delta\). |
| moving_j_support_and_zero_extension | **PASS algebraically / OBSTRUCTION analytically.** Zero extension makes reordering exact; (160.R21) shows the endpoint variation that must be paid. No bound for it is supplied. |
| n_mod_j_class_price | **PASS as a no-go control.** On \(M\) classes the exact rank and normalized nuclear cost are both \(M\); no class-free common test exists. |
| projective_Sobolev_Bessel_norms | **PASS as a no-go control.** Equations (160.R8), (160.R9), (160.R14), and (160.R16) give exact projective, sharp Bessel, and discrete normalized-coordinate Sobolev prices. No automorphic norm theorem is available in the permitted statement. |
| long_h_complement | **PASS as a no-go control.** The block map has sharp norm (160.R11), and the \(\asymp\Delta\) frequencies \(h=mj\) have trivial short phase. |
| boundary_power_saving | **FAIL for the proposed positive mechanism.** The required exponent \(s(a)>0\), while reciprocity's normalized operator norm is sharply \(1\). Restored class and long-block scales exceed \(X^{s(a)}\) unless offset by new cancellation. |
| flat_owner_and_downstream_scope | **PASS.** The result is stated only for (160.BL4); no transfer to another owner or downstream obligation is asserted. |

No numerical experiment or web/source import was used; all controls are exact algebraic or norm calculations.

## 6. Dependencies and exact artifacts used

- 'protocol.md'.
- 'rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/briefs/blind_reciprocity_matrix_rederivation.md'.
- 'rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/blind_statement.md'.

No proof graph, active campaign file, strategy file, seed, sibling report, historical round, shared proof draft, source, or computational artifact was read or used. The derivation depends only on finite Fourier orthogonality, coprimality, and elementary Hilbert-space matrix norms.

## 7. Recommended state effect

**Retain** (as candidate evidence) the exact reciprocity scalar, the full-\(h\) reconstruction, and the residue-matrix/long-frequency obstruction. **Reject** any claim that short \(j\)-modulus reciprocity by itself supplies a signed, class-free, or low-projective-cost proof of (160.BL6). Make **no promotion** of the target and no transfer beyond the flat-smooth strict-UNBAL owner. A later route would need an independently proved structural estimate for the actual Kloosterman-weighted coefficient array, including moving endpoint norms, all residue and gcd strata, the full \(h=mj\) complement, and an explicit level-\(4/8\) spectral hypothesis audit.
