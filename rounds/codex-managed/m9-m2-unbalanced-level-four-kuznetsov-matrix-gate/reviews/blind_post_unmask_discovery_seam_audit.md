# Blind post-unmask discovery seam audit (Round 143)

## 1. Result

**Verdict: do not promote the discovery report as written; promote its arithmetic kernel only after the exact repairs below.**

The central mathematical result survives review.  With

\[
 \Gamma_0(4),\qquad \chi_4,\qquad \kappa=1,\qquad
 (\mathfrak a,\mathfrak b)=(\infty,0),\qquad
 \sigma_0=\begin{pmatrix}0&-1/2\\2&0\end{pmatrix},
\]

the positive moduli are \(2n\), \(n\) odd, and

\[
 S^{\chi_4}_{\infty0}(4N_0,h;2n)
 =\chi_4(n)S(N_0,h;n).                                      \tag{A.1}
\]

The sign, inverse-of-four normalization, unrestricted \((N_0,n)\), gcd restoration, real-centre placement, \(h=0\) estimate, row/HS/nuclear norm powers, Linnik-scale algebra, and full-polytope power comparisons are correct.

The report nevertheless fails promotion as a finished artifact for five repairable reasons:

1. its displayed definition (3.4) omits the fixed-lower-left-entry condition and contains `Gamma_\infty` without a leading backslash;
2. three displayed sums contain a literal carriage-return byte where `\mathrm{odd}` was intended;
3. the Linnik threshold uses \(g>\sqrt{K/L}\) where the theorem's implicit constants justify only \(g\gg\sqrt{K/L}\), and the cited theorem is same-sign, positive-index, common-test input rather than an opposite-sign or joint-matrix theorem;
4. several sentences turn “no controlled decomposition has been proved” into the stronger, unproved assertion that the literal matrix cannot have one, and the claimed exact return of point-mass Kuznetsov to (1.7) is not derived;
5. the final “smallest survivor is the whole flat wave” statement contradicts the report's own target-safe \(h=0\) lemma: the unresolved survivor can already be restricted to \(h\ne0\).

Accordingly, the exact embedding and the scoped coefficient-matrix obstruction are **repair-and-promote**; the report as a whole is **fail pending revision**.  Nothing in this audit supports (143.B2), a complete M9-M2 estimate, or any broader owner.

## 2. Exact audited statement and hypotheses

The audit checks only the claimant's flat-smooth strict-UNBAL scalar on the stated residual polytope

\[
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.                                    \tag{A.2}
\]

Write

\[
 R=X/D,\qquad K=XL/D^2,\qquad \Delta=R/K=D/L,\qquad
 C_g=R/g,\qquad J_g=K/g.                                    \tag{A.3}
\]

For the matrix assertions, centered representatives must be fixed explicitly:

\[
 -\frac{n-1}{2}\le h\le\frac{n-1}{2},                       \tag{A.4}
\]

and each row must be zero-padded to a common \(|h|\ll C_g\) column set.  This convention is absent from the claimant but is needed for its positive/negative spectral split and its \(C_g\)-by-\(C_g\) Schatten norms.  It does not change any sum because both \(\widehat\gamma_{g,n}(h)\) and (A.1) are periodic modulo \(n\).

The promotion-safe statement is:

- (A.1) is exact in the generalized-sum convention repaired in (3.1) below.
- The complete gcd-restored scalar is the claimant's (1.2), with \(\chi_4(n)\) correctly absorbed into the generalized sum and \(\chi_4(g)\) left outside.
- The \(h=0\) complement is \(O_\varepsilon(X^\varepsilon)\).
- The unresolved owner is therefore the same joint matrix with \(h\ne0\), not literally the whole flat wave.
- From the current data one has only the row Parseval, Hilbert--Schmidt, and automatic nuclear upper bounds recorded by the claimant.  These show a missing interface; they do not prove a lower bound for the actual matrix or exclude a future low-cost vector theorem.

## 3. Seam-by-seam proof audit and exact repairs

### 3.1. Double-coset normalization and sign — **FAIL as written; underlying algebra PASS**

The matrix computation is correct:

\[
 \begin{pmatrix}A&B\\4C&D\end{pmatrix}\sigma_0
 =\begin{pmatrix}2B&-A/2\\2D&-2C\end{pmatrix},
 \qquad AD-4BC=1.                                           \tag{A.5}
\]

For positive lower-left entry, \(D=n>0\) is odd and the generalized modulus is \(2n\equiv2\pmod4\).  The determinant congruence gives

\[
 4BC\equiv-1\pmod n,\qquad
 -C\equiv\overline4_n\,\overline B_n\pmod n.               \tag{A.6}
\]

Consequently the phase in the claimant's \(B\)-parameterization is

\[
 MB-HC\equiv MB+H\overline4_n\overline B_n\pmod n,
\]

and hence

\[
 \sum_{B\bmod n}^{*}e_n(MB-HC)
 =S(H\overline4_n,M;n)
 =S(M,H\overline4_n;n)
 =S(\overline4_nM,H;n).                                     \tag{A.7}
\]

Thus \(M=4N_0\) gives (A.1) with no sign error and with no restriction on \((N_0,n)\).  The geometric phase in the claimant's chosen convention is one; another compatible cusp-Fourier convention may move one global unit into all cusp-\(0\) coefficients, but cannot create an \(n\)- or \(h\)-dependent root.

The claimant's displayed (3.4), however, is not a definition of a fixed-modulus Kloosterman sum: it sums over the whole double-coset space and never imposes lower-left entry \(c\).  It also prints `/Gamma_\infty` and does not say whether the odd multiplier's stabilizer quotient uses translations alone or includes \(-I\).  Put \(\Gamma_\infty^+=\langle T\rangle\).  One unambiguous arithmetic convention is

\[
 \begin{aligned}
 \mathcal D_{\infty0}(c)
 :=\Bigl\{[\rho]\in
 \Gamma_\infty^+\backslash
 \sigma_\infty^{-1}\Gamma_0(4)\sigma_0/\Gamma_\infty^+:
 \rho=\begin{pmatrix}a&b\\c&d\end{pmatrix}\Bigr\},\\
 S^{\chi_4}_{\infty0}(M,H;c)
 :=\sum_{[\rho]\in\mathcal D_{\infty0}(c)}
 \overline{\chi_4(D(\rho))}
 e\!\left(\frac{Ma+Hd}{c}\right),                          \tag{A.8}
 \end{aligned}
\]

where \(D(\rho)\) is the lower-right entry of an underlying
\(\gamma_0\) in \(\rho=\gamma_0\sigma_0\); its \(\chi_4\)-value is invariant under these translation stabilizers.  If a standard trace-formula convention quotients by \(\{\pm T^j\}\), the weight-one multiplier must be included and its resulting global cusp phase fixed simultaneously with the cusp-\(0\) Fourier coefficients.  With (A.8), the claimant's (3.5) is valid.

The singular-cusp audit also passes: \(\infty\) and \(0\) are singular, while the width-normalized stabilizer at \(1/2\) has lower-right entry \(3\pmod4\), so \(1/2\) is nonsingular.  Since \(\chi_4(-1)=-1\), weight parity \(\kappa=1\) is mandatory.

### 3.2. Gcd restoration and real centre — **PASS, after typography repair**

With \(g=(r,k)\), \(r=gn\), \(k=gj\), one has \(g,n\) odd and \((j,n)=1\).  The identities

\[
 \chi_4(r)=\chi_4(g)\chi_4(n),\quad
 \frac{q_L(4Xk/r^2)}k
 =\frac{q_L(4Xj/(gn^2))}{gj},\quad
 e(Xk/r)=e(N_0j/n)e(\xi j/n)                               \tag{A.9}
\]

verify the claimant's (2.4), (3.6), and (3.7).  In (1.2), the absence of an extra \(\chi_4(n)\) outside the generalized sum is correct because (A.1) has already absorbed it.  Reversing Fourier inversion gives the exact original row, so (3.8) also passes.

The only repairs here are the three corrupted occurrences in (1.2), (2.3), and (3.6): replace the literal `{<CR>m odd}` byte sequence by `\mathrm{odd}`.  These are source-file defects, not cosmetic rendering choices.

### 3.3. The \(h=0\) seam — **PASS**

On support, \(|b_{g,n}(j)|\ll X^\varepsilon/K\), there are \(O(K/g)\) entries, and \(n\asymp R/g\).  Therefore

\[
 |\widehat\gamma_{g,n}(0)|
 \le\frac1n\sum_j|b_{g,n}(j)|
 \ll \frac{X^\varepsilon}{R}.                              \tag{A.10}
\]

Since \(S(N_0,0;n)=c_n(N_0)\), \(|c_n(N_0)|\le(n,N_0)\), and

\[
 \sum_{n\asymp R/g}(n,N_0)\ll (R/g)X^\varepsilon,          \tag{A.11}
\]

the fixed-\(g\) contribution is \(O(X^\varepsilon/g)\).  The supported range has \(g\ll K\), so the total is \(O(X^\varepsilon)\).  No coprimality between \(N_0\) and \(n\) was used.

### 3.4. Joint-matrix norms and interpolation — **FAIL in conclusion wording; displayed norm algebra PASS**

The claimant's coefficient powers are correct:

\[
 \sum_j|b_{g,n}(j)|^2\ll\frac{X^\varepsilon}{gK},\qquad
 \sum_h|\widehat\gamma_{g,n}(h)|^2
 \ll\frac{X^\varepsilon}{RK},                              \tag{A.12}
\]

\[
 \|\widehat\gamma_g\|_{HS}^2\ll\frac{X^\varepsilon}{gK},
 \qquad
 \|\widehat\gamma_g\|_*
 \le\sqrt{C_g}\|\widehat\gamma_g\|_{HS}
 \ll\frac{\sqrt\Delta}{g}X^\varepsilon.                  \tag{A.13}
\]

The pointwise and row-\(\ell^1\) bounds in (3.11) and the canonical disjoint-bump upper cost

\[
 \sum_{n,h}|2n\widehat\gamma_{g,n}(h)|
 \ll\frac{C_g^2}{\sqrt{gK}}X^\varepsilon                   \tag{A.14}
\]

also pass.  Adjacent logarithmic sample points are \(\asymp C_g^{-1}\) apart, so a literal disjoint-bump interpolant can indeed have order-\(r\) logarithmic derivative cost of size \(C_g^{r-1}\) times its nodal \(\ell^1\) mass.

What does not follow is a lower bound on the actual matrix's nuclear or Sobolev cost.  Equations (A.13)--(A.14) are upper prices for two generic exact representations.  They prove that row Parseval alone does not supply the needed controlled interface; they do not prove that the literal profile cannot possess a better decomposition.  Replace categorical phrases such as “the inverse ... prevent (1.3) from being a common sequence” by:

> The frozen hypotheses prove neither a common-sequence factorization nor a simultaneously low-projective-cost, modulus-smooth decomposition of (1.3).

Likewise, the report proves (1.7) by direct row Cauchy using the exact Kloosterman second moment.  It does **not** derive that point-mass interpolation followed by a specific spectral large sieve equals or “returns” (1.7).  Replace that claim by:

> Atomic interpolation has grid-scale transform width; no estimate better than the separately available coefficient-blind closure (1.7) is derived from it here.

With those repairs, the matrix seam is a valid missing-lemma obstruction, not an impossibility theorem.

### 3.5. Linnik range algebra — **FAIL as stated; algebraic scales PASS**

For fixed same-sign positive indices, the cited Blomer--Milićević theorem has Linnik range \(mn\le X_{\rm mod}^2\).  Here

\[
 m=N_0,\qquad n=|h|,\qquad X_{\rm mod}\asymp C_g=R/g,
\]

so

\[
 |h|\ll H_{\rm Lin}(g)\asymp\frac{C_g^2}{N_0}
 \asymp\frac{X}{D^2g^2}=\frac{K}{Lg^2},\qquad
 \frac{H_{\rm Lin}(g)}{C_g}\asymp\frac1{Dg}.               \tag{A.15}
\]

Thus (1.5)--(1.6) pass, including the factors of four from generalized index \(4N_0\) and modulus \(2n\), which cancel.

Two statements need repair.  First, because both `\ll` and `\asymp` hide constants, “for \(g>\sqrt{K/L}\), not even one nonzero frequency” is too sharp.  Write

\[
 g\gg\sqrt{K/L}                                             \tag{A.16}
\]

with a sufficiently large fixed constant, or use a power-separated range
\(g\ge X^\eta\sqrt{K/L}\).  Such supported strata genuinely exist because

\[
 \frac{K}{\sqrt{K/L}}=\sqrt{KL}=X^{(1-2(\delta-\ell))/2}\to\infty. \tag{A.17}
\]

Second, the cited theorem is a same-sign theorem for positive fixed indices, one arithmetic modulus weight of fixed modulus, and one common smooth archimedean test.  It does not itself cover \(h<0\) or the joint tests (3.13).  For negative \(h\), (A.15) is a correct small-Bessel-argument scale, but it must not be called a direct application of that theorem without an opposite-sign citation.

### 3.6. Full-polytope comparisons — **PASS**

Let \(a=\delta-\ell\).  In the second branch of (143.B3),

\[
 \sqrt{XL/D}=X^{(1-a)/2},\qquad
 \sqrt{X/(LD)}=X^{(1-\delta-\ell)/2},                        \tag{A.18}
\]

and the first exponent dominates the second because \(\ell\ge0\).  Hence the envelope exponent is correctly

\[
 \beta(a)=\min\{a,(1-a)/2\}.                               \tag{A.19}
\]

The row-positive closure has exponent

\[
 p=1-(\delta+\ell)/2,                                       \tag{A.20}
\]

and the claimant's differences are exact:

\[
 p-a=1-3\delta/2+\ell/2>1/4,
 \qquad
 p-(1-a)/2=1/2-\ell>1/4.                                   \tag{A.21}
\]

Also \(\delta+\ell<3/4\), hence \(p>5/8\).  The extra inequality in (A.2) creates no exceptional chamber and is not needed for these comparisons.  The report consistently treats \(R\sqrt\Delta\) as the size of an available upper closure, not as a lower bound for the actual signed scalar.

### 3.7. Primary-source scope and spectral inventory — **FAIL for promotion-level completeness; scoped use otherwise PASS**

The source caveat concerning Kıral--Young is accurate.  Their equation (2.20) prints

\[
 S_{\infty,0}(m,n;c\sqrt N;\chi)
 =\overline\chi(c)S(\overline N m,n;c),\qquad (c,N)=1,       \tag{A.22}
\]

which at \(N=4\), \(c=n\) odd, and \(m=4N_0\) matches (A.1).  Their Theorem 2.7 explicitly assumes \(\chi\) even.  The claimant correctly does not use it as a black box for odd \(\chi_4\); its direct double-coset derivation is therefore essential.

The Blomer--Milićević source also confirms:

- \(\kappa=1\) for primitive odd character;
- the same-sign transforms printed by the claimant,

  \[
  \dot\Phi(k)=i^k\int_0^\infty J_{k-1}(x)\Phi(x)\frac{dx}{x},
  \quad
  \widetilde\Phi(t)=\frac{it}{2\sinh\pi t}
  \int_0^\infty(J_{2it}(x)+J_{-2it}(x))\Phi(x)\frac{dx}{x}; \tag{A.23}
  \]

- the holomorphic, Maass, and Eisenstein architecture; and
- the Linnik hypothesis \(mn\le X_{\rm mod}^2\).

However, that paper's Theorem 4 is phrased for ordinary Kloosterman sums with a fixed arithmetic modulus weight and a common scalar archimedean test; it is not itself the claimant's displayed switched-cusp, joint-\((n,h)\), opposite-sign formula.  The discovery report uses it safely as architecture for its no-go, but not sufficiently to promote an exact full cross-cusp spectral formula.  In particular, the report mentions the negative-\(h\) \(K\)-Bessel transform without printing its convention-dependent normalization.  Exact repair: either add a primary citation and the full convention-matched opposite-sign cross-cusp formula, or weaken the promotion claim to a structural spectral inventory.  No exact opposite-sign transform should be promoted from the present text.

The oldspace statement passes: a proper divisor level cannot carry primitive conductor-four nebentypus.  The two continuous cusp families are also correct.

### 3.8. Owner scope and survivor — **FAIL in the final minimality sentence; exclusions PASS**

The claimant stays within one flat-smooth strict-UNBAL scalar and explicitly excludes sharp, clipped, starred, transition, BAL, TOP, complete M9-M2, endpoint, M9, bridge, and global claims.  That scope discipline passes.

The recommendation that “the smallest owner-complete survivor remains the whole flat-smooth prescribed-centre wave, equivalently (4.1)” does not pass.  Section 3.5 already proves the \(h=0\) complement target-safe.  Therefore the unresolved quantity can and should be written

\[
 \sum_g\chi_4(g)
 \sum_{n\asymp R/g}
 \sum_{\substack{h\bmod n\\h\ne0}}
 W_{g,n}\widehat\gamma_{g,n}(h)
 S^{\chi_4}_{\infty0}(4N_0,h;2n),                           \tag{A.24}
\]

using the centered convention (A.4).  Its complement is
\(O_\varepsilon(X^\varepsilon)\).  This correction does not prove a spectral estimate for (A.24), but it prevents the report from overstating the unresolved owner.

### 3.9. Displayed-formula and TeX audit — **FAIL pending mechanical repair**

Formula-by-formula status is:

- (1.1), (1.3)--(1.7), (2.1)--(2.2), (2.4)--(2.5), (3.1)--(3.3), (3.5), and (3.7)--(4.2): mathematically and syntactically pass, subject to the qualification of claims surrounding (3.12)--(3.14) and (1.5).
- (1.2), (2.3), and (3.6): mathematical content passes, but each contains an embedded carriage return before `m odd`; replace the entire condition by `\mathrm{odd}`.
- (3.4): fails both syntax and mathematical completeness; apply (A.8).

The file has balanced braces and balanced display delimiters.  The remaining prose-level TeX spellings should be made renderer-safe:

- `K\i ral--Young` \(\to\) `Kıral--Young`;
- `Blomer--Mili\'cevi\'c` \(\to\) `Blomer--Milićević`;
- `Maa\ss` \(\to\) `Maaß`.

These replacements are required wherever those strings occur, including Sections 2, 3.4, 5, 6, and 7.

## 4. First doubtful or unproved step

The first unproved positive step remains exactly the joint interface identified by the claimant: converting

\[
 \widehat\gamma_{g,n}(h)
 =\frac1n\sum_j b_{g,n}(j)e(-h\overline j_n/n)               \tag{A.25}
\]

into a family accepted by a generalized-cusp trace formula and a positive spectral large sieve without first losing the modulus direction.  Neither row Parseval nor the nuclear upper bound proves a controlled common test, a low-Schatten decomposition with smooth modulus vectors, or Bessel-transform decay uniform in \((g,h,\xi)\).

The claimant is correct that expanding (A.25) and summing all \(h\) returns the original reciprocal row.  The doubtful step is not the double-coset algebra; it is any assertion that the actual inverse-selector matrix has the missing projective--Sobolev control.  Conversely, the audit rejects the stronger assertion that it cannot have such control: that also remains unproved.

## 5. Control tests and outcomes

1. **Small-modulus sign control — pass.**  At \(n=3\), (A.6) gives the same two phases as \(S(\overline4M,H;3)\), and \(\chi_4(3)=-1\).  No hidden sign or modulus-dependent unit appears.
2. **Arbitrary-gcd control — pass.**  The passage \(\overline4(4N_0)\equiv N_0\pmod n\) uses only oddness of \(n\), not \((N_0,n)=1\).
3. **Gcd restoration and real-centre control — pass.**  Equation (A.9) reproduces every factor in the frozen row.
4. **Zero-frequency control — pass.**  Equations (A.10)--(A.11) give \(O(X^\varepsilon)\) after all \(g\).
5. **Matrix-power control — pass for computations.**  Direct substitution of \(C_g=R/g\) into (A.12)--(A.14) reproduces \((gK)^{-1}\), \(\sqrt\Delta/g\), and \(C_g^2/\sqrt{gK}\).
6. **Complete Kloosterman second moment — pass.**  Additive orthogonality gives \(\sum_h|S(N_0,h;n)|^2=n\varphi(n)\) for every gcd, and hence \(R\sqrt\Delta=X/\sqrt{DL}\).
7. **Linnik control — repair required.**  The scale (A.15) is exact up to constants; the sharp `>` threshold and negative-index source attribution are not.
8. **Full-polytope extremal control — pass.**  Equations (A.18)--(A.21) remain strict at every boundary approach allowed by (A.2); there is no missed chamber from the extra linear inequality.
9. **Unsigned/adversarial control — pass as a no-go diagnostic.**  The positive row closure is unchanged after removing \(\chi_4(n)\) or inserting arbitrary row phases, so it is not evidence of actual-character cancellation.
10. **Source-hypothesis control — repair required.**  Kıral--Young's even-character restriction is correctly flagged; Blomer--Milićević supports (A.23) and the same-sign Linnik range, but not the unprinted opposite-sign cross-cusp normalization.
11. **Owner-minimality control — fail.**  The target-safe \(h=0\) lemma permits the strict nonzero-frequency survivor (A.24).
12. **Byte/TeX control — fail.**  Three embedded carriage returns and the malformed (3.4) must be corrected before rendering or promotion.

All mathematical controls were analytical.  No numerical experiment was used.

## 6. Dependencies and exact artifacts used

- Campaign: `m9-m2-unbalanced-level-four-kuznetsov-matrix-gate`.
- Task: `blind_post_unmask_discovery_seam_audit`.
- Role: statement-only blind reviewer, post-unmask seam audit.
- Starting graph hash inherited from the claimant metadata: `7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789`.
- Local mathematical context already read in the blind phase: `protocol.md` and `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/blind_statement.md`.
- Claimant report audited: `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/level_four_kloosterman_embedding_attack.md`.
- Primary source checked for (A.22) and its even-character hypothesis: E. M. Kıral and M. P. Young, *Kloosterman sums and Fourier coefficients of Eisenstein series*, [arXiv:1710.00914](https://arxiv.org/abs/1710.00914), especially equation (2.20) and Theorem 2.7.
- Primary source checked for parity, transforms, spectrum, and Linnik scope: V. Blomer and D. Milićević, *Kloosterman sums in residue classes*, [arXiv:1410.4538](https://arxiv.org/abs/1410.4538), especially Theorem 1, equations (4.2)--(4.6), and Theorem 4.
- Sibling reports, synthesis, proof graph contents, and shared state were not used in reaching the seam verdict.
- Generated: 2026-08-24 (Asia/Shanghai).

## 7. Recommended state effect and promotion verdict

**Promotion verdict: `revise`, not `promote` or `reject` wholesale.**

After the mechanical and scope repairs above, the following may be promoted as scoped candidate facts:

1. the exact weight-one level-four identity (A.1), with repaired fixed-modulus definition (A.8);
2. the exact gcd-restored owner formula and self-return;
3. the \(h=0\) bound;
4. the row Parseval, Hilbert--Schmidt, nuclear-upper-bound, and positive-capacity ledgers;
5. the same-sign Linnik-scale obstruction with the corrected \(\gg\) threshold; and
6. the full-polytope comparison showing that the coefficient-blind closure is above both branches of (143.B3).

Do **not** promote from the current text:

- the malformed definition (3.4);
- an impossibility claim for every low-cost decomposition of the actual matrix;
- an exact statement that atomic Kuznetsov returns (1.7);
- a Blomer--Milićević theorem for negative \(h\), arbitrary joint tests, or the exact switched-cusp spectral formula;
- an exact opposite-sign \(K\)-Bessel normalization; or
- the claim that the whole flat wave is the smallest unresolved survivor.

The corrected unresolved survivor is (A.24).  Its \(h=0\) complement is target-safe, but no bound for the nonzero joint matrix is proved.  Keep the quarter-bound obligation open and make no change to any excluded owner or downstream theorem.
