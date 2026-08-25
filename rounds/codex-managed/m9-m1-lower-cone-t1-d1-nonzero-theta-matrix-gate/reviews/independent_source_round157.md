# Round 157 terminal independent source and hypothesis review

- Campaign: m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate
- Claimant: nonzero_theta_matrix_source_audit.md
- Role: independent terminal source reviewer
- Primary-source cutoff rechecked: 25 August 2026
- Starting graph: 3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea
- Status: review evidence only; no shared proof state was edited

## 1. Result

### GREEN: cutoff-dated source no-match, with two nonfatal precision clarifications

The claimant's source conclusion is correct. None of the audited primary
theorems accepts the literal fixed-modulus nonzero theta matrix

\[
 \mathcal T_{\ne0,U}(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{\substack{v\bmod(c/2)\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;c),
 \qquad q=4N,\quad c=\frac{4N}{d},
\tag{157.IS1}
\]

or its exactly centered physical form with one fixed arbitrary even
composite modulus. Duke--Friedlander--Iwaniec Lemma 6.1 is an exact
pointwise kernel match, but it only reproduces

\[
 |\mathcal T_{\ne0,U}(V)|
 \ll M^{-3/4}V X^\varepsilon.
\tag{157.IS2}
\]

The current fixed-modulus papers of Pascadi, Blomer--Pascadi, and
Milićević--Qin--Wu concern ordinary Kloosterman sums with separated
sequences. Shparlinski--Xiao and Baier concern prime or
odd-squarefree/prime-square Salié or modular-root families with separated
sequences. None has the theta multiplier, the full arbitrary-composite gcd
and fold structure, or the entrywise coefficient
\(\widehat B_j(2dv)\). The half-integral trace formulas have the correct
multiplier class but average the modulus and retain their complete spectral
side. Consequently the report correctly promotes no source-derived target
estimate and no source-legal positive-power range.

Two precision points should accompany the report:

1. DFI's weakening after Theorem 2.5 does not discard equation (2.8).
   One must retain \(g(0)=g'(0)=0\), together with the transform estimates
   (2.28)--(2.29), when replacing the stronger decay assumption (2.9).
2. With the standard sesquilinear Frobenius convention, the literal
   nonconjugated entrywise sum is
   \(\langle\overline{A^{(d)}},\Theta^{(d)}\rangle_F\), not
   \(\langle A^{(d)},\Theta^{(d)}\rangle_F\). Since complex conjugation
   preserves Frobenius and nuclear norms, this notation correction changes
   none of (157.SA37)--(157.SA40).

Neither point changes the source no-match, any restored power, or the
recommended state effect.

## 2. Exact statement and source-hypothesis audit

### 2.1 DFI theta normalization and Lemma 6.1

DFI Section 6 gives the classical theta multiplier

\[
 \vartheta(\gamma)=\overline{\epsilon_a}\left(\frac ca\right),
 \qquad
 \gamma=\begin{pmatrix} *&*\\ c&a\end{pmatrix},
 \qquad c\equiv0\pmod4.
\tag{157.IS3}
\]

Because the general Kloosterman definition uses the conjugate multiplier,
equation (6.3) is exactly

\[
 K(m,n;c)=
 \sum_{a\bmod c}^{*}
 \epsilon_a\left(\frac ca\right)e_c(m\overline a+na).
\tag{157.IS4}
\]

Thus the epsilon factor, Jacobi symbol, argument order, and signs in
(157.SA6) are correct. DFI Lemma 6.1, equation (6.8), states

\[
 |K(m,n;c)|\le (m,n,c)^{1/2}c^{1/2}\tau(c),
 \qquad c\equiv0\pmod4,
\tag{157.IS5}
\]

and its local proof covers the odd Salié factor and full two-adic factor.
It is legal for arbitrary integers \(m,n\), including imprimitive strata,
and arbitrary composite \(c\equiv0\pmod4\). The official erratum does not
alter Section 6, Theorem 2.5, or Lemma 6.1.

DFI Theorem 2.5 is a different interface. It assumes \(m,n\ge1\), a
singular cusp at infinity, and a smooth test satisfying

\[
 g(0)=g'(0)=0,\qquad
 g,g',g''\ll(1+x)^{-2-\varepsilon},
\tag{157.IS6}
\]

or, more precisely, (2.8) together with (2.28)--(2.29). Its geometric side
is

\[
 K_g(m,n)=
 \sum_{c\equiv0\ (q_0)}
 \frac{K(m,n;c)}{c}
 g\!\left(\frac{4\pi\sqrt{mn}}c\right),
\tag{157.IS7}
\]

and its spectral side is the full discrete spectrum, including residual
terms, the continuous Eisenstein spectrum at every singular cusp, and the
holomorphic spectrum. For the literal signs, \(j>0\) is the
negative-negative same-sign case after conjugation, while \(j<0\) is the
mixed-sign case. Sun's corresponding formulas cover these sign interfaces
with nonzero shifted frequencies. Since \(v\ne0\) and \(|j|>V\), the
zero-frequency objection is indeed gone in Round 157; the remaining
obstructions are fixed-modulus localization, the coupled matrix, and the
retained spectral pieces.

### 2.2 Current 2025--2026 fixed-modulus cards

The version histories and printed hypotheses were rechecked against the
primary pages.

| Source | Exact checked interface | Terminal comparison with (157.IS1) |
|---|---|---|
| Pascadi, version of record published 21 August 2026 | Theorem 1.1 has \(M_0,N_0\ll c^{1/2+o(1)}\), separated sequences, unit \(a\), ordinary \(S(am,n;c)\), and \((m,n,c)=1\), with \(c^{1-1/700+o(1)}\). Its second estimate assumes \(|\alpha_m|\le1\), retains \((n,c)=1\), and gives \(c^{1-1/276+o(1)}\). Proposition 4.10 is an operator-norm reduction for the ordinary Kloosterman matrix with the printed squarefree/square-full gcd weights. | Arbitrary modulus is legal, but the kernel, separation, length, and gcd interface are not. Proposition 4.10 is not an arbitrary entrywise-matrix or nuclear-norm theorem. |
| Blomer--Pascadi, arXiv:2607.24311v1, 27 July 2026 | Theorem 1.1 treats two intervals of length at most \(H_0\), separated weights, ordinary \(S(am,n;c)\), and \((m,n,c)=1\); only the two initial intervals may drop the gcd condition. Its saving factor is exactly the three-term expression in (157.SA22), and at \(H_0=\sqrt c\) the bound is \(c^{1-1/32+o(1)}\). | Ordinary kernel and rank-one weights; no theta multiplier, quadratic fold, mandatory imprimitive strata, or entrywise coefficient. |
| Milićević--Qin--Wu, arXiv:2511.07550v1 | Theorem 1.1 uses \(\mathrm{Kl}_2(a;c)=c^{-1/2}S(a,1;c)\), separated weights, a product argument \(amn\), and exactly the three inequalities and three right-side terms recorded in (157.SA24). | A raw ordinary sum requires restoration of \(c^{1/2}\). The normalized product kernel is not \(K(-v^2,-j;c)\). |
| Shparlinski--Xiao, arXiv:2601.10113v1 | The modulus is a large prime. Theorem 2.5 has separated \(\alpha_m,\beta_n\), \((a\lambda,p)=1\), the shifted product-root congruence \(x^2\equiv amn+b\pmod p\), and precisely the three terms in (157.SA14). | Prime shifted-product roots and a fixed additive root mode do not specialize to the arbitrary even-composite theta family. |
| Baier, arXiv:2605.01635v3, 20 July 2026 | Theorem 6 assumes \((r,j)=1\), \(r^\varepsilon\le L_0,M_0\le r^{1-\varepsilon}\), the derivative and \(H_0\) conditions, and either odd squarefree \(r\) or a prime square. Equations (21)--(22) and Corollary 7 give exactly the terms transcribed in (157.SA15)--(157.SA16), including the additional prime-square term. | The literal \(c=4N/d\) is even and arbitrary, the complete \(v\)-family has length \(c/2\), and the coefficients remain separated in Baier's theorem. |

The titles or proof methods do not change these kernels. In particular,
“quadratic characters” in Blomer--Pascadi describes the method, while the
theorem still bounds ordinary Kloosterman sums. Likewise, the exceptional
Maaß large-sieve applications of Pascadi and Blomer--Pascadi are
integral-weight, one-sequence consequences of the ordinary Kuznetsov
formula; they are not half-integral theta-multiplier replacements.

### 2.3 Root large sieves and half-integral trace formulas

The Dunn--Kerr--Shparlinski--Zaharescu theorem is prime-modulus,
product-root, fixed-root-mode, and separated-weight. Fouvry--Iwaniec
averages the modulus while fixing the congruence. Liu's quadratic large
sieve averages odd squarefree character moduli and odd squarefree
summation variables. DFI Theorem 1.1 fixes a positive odd fundamental
discriminant and smooths a modulus average. None may be converted into a
fixed-\(4N\) discrepancy by freezing the variable that supplies its
orthogonality.

DFI, Sun, and Andersen--Duke all retain a modulus sum on the geometric
side. A narrow test can write a formal trace identity near one modulus, or
one can raise the group level to that modulus, but the quoted uniform
bounds do not permit singleton localization with derivative and level
constants suppressed. Moreover, localization does not delete Maaß,
holomorphic, Eisenstein/continuous, residual/principal, or exceptional
pieces. The report correctly keeps every applicable piece rather than
treating Kuznetsov as an automatic fixed-modulus estimate.

## 3. Independent normalization, matrix, and power verification

### 3.1 Pointwise DFI capacity

Ignoring only the fixed absolute factor \(|1+i|\), one divisor stratum has

\[
 P_d=\frac{d\sqrt c}{2Nq}
 =\frac{\sqrt d}{4N^{3/2}}.
\tag{157.IS8}
\]

DFI's square-root modulus factor cancels exactly:

\[
 P_dc^{1/2}=\frac{dc}{2Nq}=\frac1{2N}.
\tag{157.IS9}
\]

The accepted BV/Fourier and gcd sum

\[
 \sum_{\substack{v\bmod(c/2)\\v\ne0}}
 |\widehat B_j(2dv)|(v^2,j,c)^{1/2}
 \ll M^{-3/4}cX^\varepsilon
\tag{157.IS10}
\]

therefore costs \(O(M^{-3/4}/d)\) per \(d,j\). Summing all odd
\(d\mid N\) and \(O(V)\) values of \(j\) gives (157.IS2), with top
capacity \(N^{1/2}M^{-1/4}X^\varepsilon\). This reproduces the claimant's
normalization and confirms that it is an upper capacity, not a signed
lower obstruction.

### 3.2 Operator versus entrywise pairing

Let

\[
 A^{(d)}_{j,v}=\widehat B_j(2dv),\qquad
 \Theta^{(d)}_{j,v}=K(-v^2,-j;c).
\]

Under the usual Frobenius convention, the literal sum is

\[
 \langle\overline{A^{(d)}},\Theta^{(d)}\rangle_F.
\]

The valid operator duality is consequently

\[
 |\langle\overline A,\Theta\rangle_F|
 \le \|\overline A\|_*\|\Theta\|_{\mathrm{op}}
 =\|A\|_*\|\Theta\|_{\mathrm{op}}.
\tag{157.IS11}
\]

An operator theorem for separated row and column vectors does not permit
\(\|A\|_*\) to be replaced by \(\|A\|_F\). The generic rank and sampled
Parseval bounds are

\[
 \|A^{(d)}\|_*
 \le\sqrt{\min(V,c/2)}\,\|A^{(d)}\|_F,
 \qquad
 \|A^{(d)}\|_F^2
 \ll VqK M^{-3/2}X^\varepsilon.
\tag{157.IS12}
\]

Even granting the illegal formal substitute
\(\|\Theta\|_{\mathrm{op}}\ll c^{1-\delta}\), restoration of (157.IS8) gives

\[
 M^{-3/4}N^{-\delta}d^{-1/2+\delta}
 \sqrt{VK\min(V,N/d)}X^\varepsilon.
\tag{157.IS13}
\]

For \(d=1\) and \(V=K\), this is

\[
 N^{3/4-\delta}X^\varepsilon.
\tag{157.IS14}
\]

Thus (157.SA39)--(157.SA40) have the correct powers. They are not
target-sized even with the square-root-length ordinary saving
\(\delta=1/32\), and they are expressly labeled formal because the kernel,
fold, dimensions, gcd strata, and coefficient class all fail first.

The hostile prime toy translations are also arithmetically correct.
Putting one first variable and a \(1\)-bounded second sequence supported on
\(L\) points in an interval of length \(V\) into
Dunn--Kerr--Shparlinski--Zaharescu gives exactly (157.SA33)--(157.SA34).
At \(V=K\), \(L\le M\), and after \(M^{-3/4}\), the powers become

\[
 N^{3/16+o(1)}M^{-1/48}
 \quad\text{and}\quad
 N^{5/32+o(1)}M^{1/32},
\tag{157.IS15}
\]

with the printed parenthetical factors retained. The analogous
Shparlinski--Xiao third term is
\(N^{3/4}M^{-1/4}(\log N)^{1/2}\). Baier's hypotheses fail before a
literal \(N,M,V,d\) substitution is legal. These calculations are
diagnostic upper capacities only.

### 3.3 Corrected incidence statement is internal and conditional

The report explicitly labels

\[
 L(V)\ll\min(M,V)X^\varepsilon
\tag{157.IS16}
\]

as an internally supplied selected-support count, not a literature
theorem. It then assumes, rather than asserts, a genuine signed
square-root theorem. Under that hypothesis,

\[
 M^{-3/4}\sqrt{L(V)}
 \ll M^{-3/4}\min(M,V)^{1/2}X^\varepsilon
 \le M^{-1/4}X^\varepsilon
\tag{157.IS17}
\]

for every selected \(V\). This correctly supersedes the older
ambient-only conditional ledger \(V\le M^{3/2}\). The report repeatedly
states that a cardinality bound is not cancellation and that the
mixed-variation reduction is owned by the analytical task. No external
source is credited with either (157.IS16) or the hypothetical signed
estimate.

## 4. First doubtful or unproved step

The first source-unproved step remains exactly one of the following
equivalent-strength inputs:

1. a fixed-arbitrary-even-composite centered discrepancy theorem for the
   two affine root families \(x^2\equiv j+N,j+3N\pmod{4N}\), with the
   literal signed \(j\)-block, short \(x\)-interval, complete-Gauss
   subtraction, gcd strata, and endpoints; or
2. a fixed-\(c\) theta-multiplier matrix theorem for
   \(K(-v^2,-j;c)\) which accepts
   \(A_{j,v}=\widehat B_j(2dv)\), every odd divisor stratum, all
   complementary modes and folds, and a target-sized structural norm.

There is also an internal, nonsource seam: the literal centered profile
must be reduced to rectangular discrepancies with its global constant tail
and full mixed variation charged. The source report correctly declines to
certify that step.

No cited theorem proves either input. Equally, the audit proves no lower
bound, no counterexample, and no impossibility for an internal argument or
future theorem. The only corrections to the claimant are the DFI
test-function wording and the harmless Frobenius-conjugation notation from
Section 1.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| DFI multiplier and argument order | **GREEN.** Equations (6.1), (6.3), and (6.8) give exactly (157.IS3)--(157.IS5), including the epsilon factor, signs, arbitrary composite modulus, and all gcd strata. |
| DFI Theorem 2.5 hypotheses | **GREEN with clarification.** It has \(m,n\ge1\); the weakened test condition retains (2.8) together with (2.28)--(2.29). |
| fixed modulus versus average | **GREEN / NO MATCH.** DFI, Sun, Andersen--Duke, Fouvry--Iwaniec, and quadratic large-sieve cards average the variable that supplies orthogonality; no quoted uniform theorem singleton-localizes at growing \(c\). |
| all spectral pieces | **GREEN.** Same-sign formulas retain holomorphic, Maaß, singular-cusp Eisenstein, residual/principal, and exceptional contributions as applicable; mixed sign retains Maaß and Eisenstein pieces. |
| Pascadi and Blomer--Pascadi | **GREEN / NO MATCH.** Dates, formulas, ordinary kernel, separation, interval lengths, and gcd restrictions match the primary pages. |
| Milićević--Qin--Wu | **GREEN / NO MATCH.** The normalized \(\mathrm{Kl}_2\), three range conditions, and three right-side terms are exact; raw \(S\) restores \(c^{1/2}\). |
| Shparlinski--Xiao and Baier | **GREEN / NO MATCH.** Prime or odd-squarefree/prime-square modulus, product-root geometry, separated coefficients, and length restrictions are exact. |
| entrywise versus operator norm | **GREEN with notation correction.** The standard pairing uses \(\overline A\); nuclear duality and every power in (157.SA37)--(157.SA40) are unchanged. |
| \(N,M,V,d\) ledger | **GREEN.** The \(1/(2N)\) cancellation, \(M^{-3/4}V\) pointwise capacity, prime toy capacities, and formal nuclear powers reproduce independently. |
| corrected selected incidence | **GREEN / CONDITIONAL.** \(L(V)\ll\min(M,V)X^\varepsilon\) is explicitly internal support information; square-root cancellation is only a hypothetical sufficient theorem. |
| cutoff and impossibility scope | **GREEN.** The conclusion is expressly a direct-interface source no-match through 25 August 2026, not a universal literature claim, lower bound, or mathematical impossibility. |
| downstream scope | **GREEN.** No claim is transferred to other \(D,L,t\) owners, M2, endpoint assembly, M9, the bridge, the quarter theorem, or a global exponent. |

No numerical or symbolic experiment was used.

## 6. Dependencies, artifacts, and primary sources used

### Repository artifacts

- protocol.md;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reports/nonzero_theta_matrix_source_audit.md; and
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/independent_spectral_source_review.md.

### Primary pages rechecked

1. W. Duke, J. B. Friedlander, and H. Iwaniec,
   [Weyl Sums for Quadratic Roots](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf),
   especially Theorem 2.5, equations (2.8), (2.27)--(2.29), and Section 6,
   together with the
   [official erratum](https://doi.org/10.1093/imrn/rnr240).
2. A. Pascadi,
   [Non-Abelian Amplification and Bilinear Forms with Kloosterman Sums](https://link.springer.com/article/10.1007/s00039-026-00746-0),
   version of record dated 21 August 2026, Theorems 1.1--1.2 and
   Proposition 4.10.
3. V. Blomer and A. Pascadi,
   [Bilinear forms with Kloosterman sums via quadratic characters](https://arxiv.org/html/2607.24311v1),
   arXiv:2607.24311v1, Theorems 1.1, 5.5, and 5.7.
4. D. Milićević, X. Qin, and X. Wu,
   [Bilinear forms with Kloosterman sums and moments of twisted L-functions](https://arxiv.org/html/2511.07550v1),
   arXiv:2511.07550v1, Theorem 1.1.
5. I. E. Shparlinski and Y. Xiao,
   [Shifted bilinear sums of Salié sums and the distribution of modular square roots of shifted primes](https://arxiv.org/html/2601.10113v1),
   arXiv:2601.10113v1, definition (1.3) and Theorem 2.5.
6. S. Baier,
   [Partial progress towards the large sieve for square moduli](https://arxiv.org/html/2605.01635v3),
   arXiv:2605.01635v3, Theorem 6 and Corollary 7.
7. A. Dunn, B. Kerr, I. E. Shparlinski, and A. Zaharescu,
   [Bilinear forms in Weyl sums for modular square roots and applications](https://arxiv.org/html/1908.10143v3),
   Theorem 1.7.
8. Z. Liu,
   [Explicit quadratic large sieve inequality](https://arxiv.org/abs/2505.09637),
   Acta Arithmetica 223 (2026), Theorem 1.

The Round 155 terminal review already checked the cited Sun,
Andersen--Duke, Lam, Fouvry--Iwaniec, and Ahlgren--Andersen source cards;
their uses here are unchanged except that the \(v=0\) objection is no
longer invoked. Current arXiv histories were checked: Milićević--Qin--Wu,
Blomer--Pascadi, and Shparlinski--Xiao remain at v1, while Baier's current
version at the cutoff is v3.

## 7. Recommended state effect

Accept the claimant report as terminal **source no-match evidence**. Retain
DFI Lemma 6.1 as the exact pointwise theta input and retain the normalized
capacity (157.IS2). Record that current ordinary-Kloosterman operator
theorems, modular-root bilinear theorems, quadratic large sieves, and
half-integral modulus-average trace formulas do not supply the missing
fixed-composite coupled theorem.

Retain (157.IS16)--(157.IS17) only as an internal, conditional capacity
correction: a genuine signed square-root theorem would now suffice for all
selected \(V\), but no audited source proves it. Promote no source-derived
strict range and make no downstream or global-exponent change.

If the conductor closes the route under
**outer_defect_centered_discrepancy_no_go**, the label must mean only
“no matching audited primary theorem through 25 August 2026.” It must not
be read as a proof that the discrepancy estimate is false or unprovable.

**Verdict: GREEN. First source defect: the required fixed-composite,
coupled theta/root-discrepancy theorem is absent; this is an open input, not
a flaw in the audit.**
