# Round 166 source-hypotheses, currency, and interface seam review

**Review date:** 2026-08-26.  **Verdict:** revise the source report in place before it is treated as final campaign evidence; retain its no-import conclusion and make no graph change.

## 1. Result

### Seam-review lemma

The four reviewed artifacts agree on the only conclusion that is presently source-licensed:

\[
\tag{167.F = 165.K17a}
\Re \mathfrak C^{\rm rem}_{R_0,2,{\rm opp},g<\gamma L}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon,
\qquad R_0=\lceil L\rceil,
\]

is a defensible **next strategy target**, but no audited primary-source theorem proves it, proves the maximal alternative (165.K26), or changes an accepted proof-graph status.  The graph strategy report and the blind rederivation select this target independently from its exact scalar size, owner locality, and missing factor \(L\).  Grimmelt--Merikoski, arXiv:2404.08502v2, Theorem 10.1, supplies a close determinant-orbit model and a useful source-to-interface test; it does not license promotion of (167.F) as a lemma.

The determinant identification

\[
 (a,b,c,d)=(d',d,m,m'),\qquad ad-bc=d'm'-dm=r,
\]

and the even-shift two-adic split pass literally.  The first failed source hypothesis is instead the absence of an admissible representation of the actual selector-dependent endpoint coefficient in the theorem's automorphic/smooth weight class.  Conditional on replacing that coefficient by a smooth surrogate, the square-root phase imposes the scaled derivative cost

\[
 \delta^{-1}\gtrsim 1+\frac{Jr}{L}.
\]

The current source report contains one material quantifier error here: over the full short range \(2\le r<R_0\asymp L\), this cost ranges from \(1+O(J/L)\) to \(1+O(J)\); it is of order \(J\) only on a top short-shift stratum \(r\asymp L\), not uniformly throughout (165.K17a).  Near \(r\asymp L^2\) it reaches order \(JL\).  This correction does not improve applicability: the source theorem states a polynomial \(\delta^{-O(1)}\) loss whose full restored power has not been shown target-safe.

The source report's other main conclusions pass after the precise repairs listed in Section 7:

- Li--Yang, arXiv:2308.14859v2, Theorem 1.2, remains the dated, primary-source-audited claimed pointwise benchmark, with
  \[
  \theta_*={3292+25\sqrt{1717}\over13762}=0.3144831759740614\ldots .
  \]
- Fixed-shift, fixed-level, fixed-modulus, spectral-mean-square, spatial \(L^p\), spacing-count, and restricted-coefficient statements were correctly kept distinct from the required pointwise signed variable-shift aggregate.
- Grimmelt--Merikoski, arXiv:2505.00489v2, Part I, is not a stronger directly applicable substitute: before its abstract two-functional theorem can touch the project sum, an exact two-endpoint kernel realization is needed, and its right side then leaves the relevant selector/phase autocorrelations unbounded.

## 2. Exact statements and hypotheses checked

### 2.1 Literal project interface

The Round-165 kernel fixes

\[
c_N^{\rm rem}
=\sum_{\substack{d\mid N\\2\nmid d}}
  \chi_4(d)\lambda_N(d),
\qquad N\asymp L^2,\quad d,N/d\asymp L,\quad
|\lambda_N(d)|\ll1,
\]

where \(\lambda_N(d)\) is the actual supported residual row, not an arbitrary smooth or periodic coefficient.  It includes the squarefree row, normalizations, residual neither/both selector, parity branch, profiles, hard point, endpoints, and zero extension.  The available energy statement is

\[
\sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon.
\]

The short target (165.K17a) sums all even \(0<r<R_0\), with the strict opposite-sign and \(g<\gamma L\) restrictions, the Fejer factor, the square-root-difference phase, and one real part after the full aggregate.  The maximal alternative (165.K26) instead sums the even range \(R_0\le r<M_L\), \(M_L\asymp L^2\), and asks for \(O(L^3X^\varepsilon)\).  Fixed-shift Cauchy gives capacities \(L^3X^\varepsilon\) and \(L^4X^\varepsilon\), respectively, so both targets require a genuine aggregate factor \(L\).  This agrees in the kernel, blind report, and graph report.

The absolute-value placement is part of the hypothesis, not presentation: a proof must control the single outer real part after recombining all allowed \(r\), gcd, two-adic, dyadic, and boundary pieces.  An estimate of \(\sum_r|E_r|\) is not the target.

### 2.2 Grimmelt--Merikoski 2024, Theorem 10.1

The audited source is Lasse Grimmelt and Jori Merikoski, *Twisted correlations of the divisor function via discrete averages of \(\operatorname{SL}_2(\mathbb R)\) Poincare series*, [arXiv:2404.08502v2](https://arxiv.org/html/2404.08502v2), Theorem 10.1.  The arXiv record identifies v2, revised 2024-04-26, as the current version on the audit date.

The theorem takes \(q_1,q_2>0\), \(q=q_1q_2\), nonzero determinant factors \(h,k\), and matrices

\[
M_{2,h,k}(\mathbb Z)=
\left\{
\begin{pmatrix}a&b\\c&d\end{pmatrix}:
ad-bc=hk,
\ \gcd(a,c,k)=\gcd(b,d,k)=1
\right\}.
\]

It requires \(\alpha\in\mathcal A(q_1,q_2,\chi,\xi)\), with the source's exact left-automorphy, character, and determinant-twist law; \(A,C,D,\delta,\eta>0\), \(AD>\delta\); \(Z=\max(A^{\pm1},C^{\pm1},D^{\pm1},\delta^{-1})\); \(H,K\ge1\), \(HK\le(AD)^{1+\eta}\); one common

\[
f\in C^7_\delta
\left(A/\sqrt{HK},C/\sqrt{HK},D/\sqrt{HK}\right);
\]

dyadically supported \(\beta_h,\gamma_k\); the restriction \(\gcd(h,kq)=1\); and the explicit autocorrelation hypothesis (10.2), measured by \(\mathcal K_+\).  Its conclusion is a main term when the induced character is principal plus a single error for the complete \(h,k\)-matrix aggregate, with the displayed factors

\[
Z^{O(\eta)}\delta^{-O(1)}(AD)^{1/2}
\|\beta\xi\|_2\mathcal K_+^{1/2}
\bigl(\mathcal R_0+\min(\mathcal R_1,\mathcal R_2)\bigr).
\]

Thus a future invocation must audit the exact \(\mathcal R_i\), \(\mathcal K_+\), principal main term, dyadic recombination, and boundary costs; the determinant equation alone is insufficient.

The exact project map is

\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
\qquad ad-bc=d'm'-dm=r.
\]

For even \(r\), write

\[
r=hk,\qquad k=2^{v_2(r)},\qquad h\text{ odd}.
\]

Choose \(q_1=4,q_2=1\), the upper-row characters \(\chi_1=\psi_1=\chi_4\), and principal lower-row characters.  The pointwise twist becomes

\[
\chi_4(a)\chi_4(b)=\chi_4(d')\chi_4(d),
\]

while the induced automorphy character is \(\chi_4^2\), hence principal on the odd support.  Since \(d,d'\) are odd and \(k\) is a power of two,

\[
\gcd(a,c,k)=\gcd(d',m,k)=1,
\qquad
\gcd(b,d,k)=\gcd(d,m',k)=1,
\]

and \(\gcd(h,kq)=1\).  Also \(HK\asymp r\le L^2\asymp AD\), after the necessary dyadic and two-adic decomposition.  Therefore determinant size, gcd, parity, and the bare \(\chi_4(d')\chi_4(d)\) twist are not the first literal failure.

The first missing hypothesis is a theorem-admissible realization of

\[
\lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}.
\]

No reviewed artifact proves that this selector-dependent multiplier belongs to \(\mathcal A(4,1,\chi,\xi)\).  Moving it into \(f\) does not repair the application because the exact selector and hard endpoint are not a single \(C^7_\delta\) weight.  Lau's [arXiv:2509.07556v2](https://arxiv.org/html/2509.07556v2), Theorem 5.2, does not enlarge the class: Lau separately proves the automorphy of his particular periodic divisibility selector in Lemma 5.4 and separately bounds its \(\mathcal K_+\).  Those verifications do not transfer to the project selector.

### 2.3 Conditional phase and variable-determinant hypotheses

Only after replacing the selector and endpoints by an admissible smooth surrogate does the phase become the next seam.  On \(a,d\asymp L\), with \(ad\asymp ad-r\asymp L^2\), set

\[
\Phi_r(a,d)=J\bigl(\sqrt{ad}-\sqrt{ad-r}\bigr).
\]

Then

\[
\partial_a\Phi_r
=\frac{Jd}{2}
\left((ad)^{-1/2}-(ad-r)^{-1/2}\right),
\]

and symmetrically for \(\partial_d\Phi_r\).  The mean-value theorem gives, uniformly away from the shell degeneration,

\[
L|\partial_a\Phi_r|+L|\partial_d\Phi_r|
\asymp \frac{Jr}{L}.
\]

Scaled higher derivatives of \(\Phi_r\) have the same base scale, while differentiating \(e(\Phi_r)\) produces products of these derivatives.  Consequently the \(C^7_\delta\) seminorm requires at least, and on a fixed nondegenerate smooth cell is controlled by,

\[
\delta^{-1}\gtrsim1+\frac{Jr}{L}.
\]

The correct scale ledger is therefore

\[
\begin{array}{c|c}
\text{shift stratum}&\text{required }\delta^{-1}\text{ scale}\\ \hline
r=O(1)&1+O(J/L)\\
r\asymp L&1+O(J)\\
r\asymp L^2&1+O(JL).
\end{array}
\]

The source statement leaves this as \(\delta^{-O(1)}\).  That is enough to say that the source theorem, as stated, does not certify the restored \(L\)-saving.  It is not enough to assert without calculation that every short shift individually loses a factor \(J^{O(1)}\), nor to declare the loss fatal before the hidden polynomial exponent, \(J\)-range, cell count, and all \(\mathcal R_i\) are restored.

There is a separate aggregate obstruction.  Theorem 10.1 permits one common \(f\) across its \(h,k\) aggregate.  In determinant-normalized variables the project phase contains

\[
J\sqrt{hk}\left(\sqrt{xz}-\sqrt{xz-1}\right),
\]

so its frequency varies with \(hk=r\) and cannot be placed in the scalar factors \(\beta_h\gamma_k\).  A new controlled-rank Fourier/Mellin decomposition could in principle address this, but none is present in the source or local artifacts.  Delta-localizing to one \(r\) makes the theorem fixed-shift; summing the resulting errors yields \(\sum_r|E_r|\), which destroys the required outer-real-part cancellation.

The Fejer multiplier itself should not be named as this obstruction: on a fixed dyadic/two-adic piece, \(1-hk/R\) is a rank-two separable combination in \(h\) and \(k\).  The hyperbolic cutoff \(hk<R\), hard endpoints, common phase, selector, main term, and correlation norm still require control.

### 2.4 Grimmelt--Merikoski 2025 Part I

The current source is [arXiv:2505.00489v2](https://arxiv.org/html/2505.00489v2), revised 2025-05-30, explicitly titled *Part I: non-oscillatory functions*.  Theorem 1.1 takes a congruence subgroup \(\Gamma\), group character \(\chi\), arbitrary compactly supported linear **functionals** \(\alpha_1,\alpha_2\), a non-oscillatory \(F\) induced by \(f\in C^{10}_\delta(A,C,D)\), \(AD>\delta\), and \(X_0X_1X_2\ge AD\).  It bounds the full discrepancy pairing by

\[
|\langle\alpha_1|\Delta F|\alpha_2\rangle|
\ll \delta^{-O(1)}(AD)^{1/2+o(1)}X_0^\theta
\sqrt{
\langle\alpha_1|\Delta k_{X_1^2,R_1}|\alpha_1\rangle
\langle\alpha_2|\Delta k_{X_2^2,R_2}|\alpha_2\rangle}.
\]

Its outer absolute value is favorably placed, but applicability fails first because no exact relative-kernel parametrization has been proved that places the two residual endpoints in \(\alpha_1,\alpha_2\) while encoding determinant, parity/gcd, Fejer truncation, shell, and endpoint restrictions in one non-oscillatory \(F\) without cross-terms.  Even if such a representation were supplied, both positive discrepancy autocorrelations on the right would remain to be bounded for the actual selector/phase weights; the source gives no \(L^2\) or \(L^3\) estimate for them.  Corollary 1.5's ready-made determinant specialization again requires a left-invariant one-matrix coefficient and \(C^{10}_\delta\) weight.  Part I therefore relocates rather than proves the missing cancellation.  The announced oscillatory Part II is not an available theorem in the dated audit.

### 2.5 Current pointwise benchmark and source currency

Li--Yang, [arXiv:2308.14859v2](https://arxiv.org/html/2308.14859v2), Theorem 1.2, states for every \(\varepsilon>0\), pointwise for real \(X\),

\[
R(X),\Delta(X)=O_\varepsilon(X^{\theta_*+\varepsilon}),
\qquad
\theta_*={3292+25\sqrt{1717}\over13762}.
\]

There is no average over \(X\) and no arbitrary coefficient class.  The final theorem may be retained only with the existing local v2 repair card; the withdrawn Bourgain--Watt theorems may not be imported.  The search conclusion must remain dated and scoped: the primary arXiv/journal/author-material search completed on 2026-08-26 found no later indexed primary-source claim improving this classical pointwise exponent.  It does not rule out unpublished, unindexed, or subsequently posted work.

The version ledger checked against primary records is:

| Source | Current audited version/status on 2026-08-26 | Review effect |
|---|---|---|
| Li--Yang, arXiv:2308.14859 | v2, 2023-09-14 | Dated claimed pointwise record; use only the repaired final Theorem 1.2. |
| Bourgain--Watt, arXiv:1709.04340 | v2, withdrawn, 2023-07-16 | Theorems 1--3 and Propositions 1', 2, 3 are not dependencies. |
| Grimmelt--Merikoski, arXiv:2404.08502 | v2, 2024-04-26 | Correct version for Theorem 10.1. |
| Grimmelt--Merikoski, arXiv:2505.00489 | v2, 2025-05-30 | Correct Part-I version; non-oscillatory only. |
| Lau, arXiv:2509.07556 | v2, 2026-07-09 | Correct version for Theorem 5.2 and the shifted-divisor results. |
| Blomer--Jana--Nelson, arXiv:2404.10692 | v2, 2025-05-22; GAFA 35 (2025) | Current source/journal version. |
| Pascadi, arXiv:2404.04239 | **v3**, 2026-01-15; Forum Math. Pi 14 (2026), e8 | The source report should cite v3 explicitly. |
| Tao--Trudgian--Yang, arXiv:2501.16779 | v1, 2025-01-28 | Current audited version. |
| Blomer--Pascadi, arXiv:2607.24311 | v1, 2026-07-27 | Current audited version. |
| Shparlinski--Xiao, arXiv:2601.10113 | v1, 2026-01-15 | Current audited version. |
| Guth--Maldague, arXiv:2206.01093 | v2, 2022-08-13 | Current audited version. |

## 3. Proof and source-to-interface derivation

### 3.1 Why the determinant seam passes but the theorem application fails

Expanding a project correlation gives terms

\[
\chi_4(d')\chi_4(d)
\lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}
e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right),
\qquad d'm'-dm=r.
\]

The matrix map in Section 2.2 is bijective at the displayed-variable level and preserves the determinant exactly.  For even \(r\), the chosen two-adic factorization makes \(h\) coprime to \(kq\); oddness of \(d,d'\) gives both column gcd conditions; and \(r\le L^2\asymp AD\) fits the determinant-size hypothesis after finite dyadic decomposition.  This proves the claimed determinant/gcd compatibility.

What remains is not a formal detail.  The theorem sums a coefficient satisfying a prescribed group transformation law against a smooth weight of specified seminorm.  The project multiplier contains a nonlocal residual selector depending on both endpoint products and their divisors.  No group transformation identity or admissible \(C^7\) encoding is proved for it.  Thus the application stops before spectral estimation.  This is the first failed hypothesis in the literal theorem-call order.

If one conditionally replaces the selector by a smooth cell, differentiating the phase proves the seminorm ledger in Section 2.3.  If one then freezes \(r\), the theorem's global error is global only for that fixed determinant cell.  Applying triangle inequality to recombine cells changes

\[
\left|\Re\sum_r E_r\right|
\quad\text{into}\quad
\sum_r|E_r|,
\]

precisely discarding the factor-\(L\) cancellation demanded by both (165.K17a) and (165.K26).  Hence selector admissibility, phase cost, and variable-\(r\) aggregation are logically distinct successive gates.

The induced principal character also means the theorem carries a main term.  That main term is not automatically killed by the project twist and would need its own uniform oscillatory, selector-aware, endpoint-complete bound.  The \(\mathcal K_+\) hypothesis is likewise not a bookkeeping norm: Lau's application works only after a separate correlation count, which the project does not possess.

### 3.2 Aggregate real part and absolute values

The source report is right that Grimmelt--Merikoski Theorem 10.1 is directionally better than a fixed-shift theorem: its stated asymptotic treats the entire admitted \(h,k\) sum before the single big-\(O\) error.  It should be described as a **complex aggregate equality with one global error**, not as a theorem specifically about a real part.  If an exact admissible representation existed, an absolute bound for the complex aggregate would imply the required real-part bound.  No representation currently exists.

The target's one outer real part must also survive all local decompositions.  Neither the positivity of a spectral large sieve nor an \(L^2\) or \(L^p\) average automatically preserves it.  The blind report's aligned-array control confirms why: phase-aligned arrays with the same energy reach Fejer capacity \(\asymp L^3\) at the short scale, so any coefficient-uniform argument claiming \(O(L^2)\) has silently discarded a necessary sign-sensitive hypothesis.

### 3.3 Pointwise, deterministic restricted-class, and averaged statements

The audited candidates split into three genuinely different quantifier types:

| Type | Primary-source examples | Literal limitation at the project interface |
|---|---|---|
| Pointwise final discrepancy | Li--Yang Theorem 1.2; Huxley benchmark | A conclusion about \(R(X)\) or \(\Delta(X)\), not a theorem for \(c_N^{\rm rem}\) or a graph node. |
| Deterministic/pointwise with restricted coefficients or kernel | TTY Theorem 20 coefficient-one model phase; Lau Theorems 1.1--1.2 (fixed divisor coefficients and fixed shift); BJN Theorem 5 first estimate (fixed Hecke data and centre); Bettin--Chandee (factorized sequences); Blomer--Pascadi Theorem 1.1 (fixed modulus Kloosterman kernel); Shparlinski--Xiao Theorems 2.2/2.5 (fixed large prime and Type I/II Salié kernel); Grimmelt--Merikoski Theorem 10.1 (automorphic coefficient and smooth determinant weight) | These are not “averaged” merely because their class is narrow.  They fail by coefficient, phase, modulus/level, fixed-shift, or endpoint hypotheses before any claim about averaging. |
| Genuine average/positive mean square | BJN Theorem 5 second estimate (integral over real centre); Pascadi Theorem 1.2 and related spectral large sieves (sum of squares over a spectral family at fixed level/cusp); Guth--Maldague Theorem 3 (spatial (L^p) cone norm); Robert--Sargos Theorem 2 after Hölder use (unsigned spacing count) | They do not directly imply a fixed-centre, unsquared, sign-sensitive Fejer aggregate. |

This distinction should remain explicit.  In particular, Lau's shifted-divisor asymptotics and Shparlinski--Xiao's Type I/II estimates are restricted-class deterministic statements, not average theorems.  Their failure is literal kernel/coefficient/range mismatch.  Conversely, a spectral large sieve may be uniform in its input coefficients while still averaging the square over the spectral family; that positivity is not the project cancellation.

### 3.4 Candidate-by-candidate first failed hypothesis

| Candidate | First literal project failure | Next unresolved seam |
|---|---|---|
| Li--Yang, Theorem 1.2 | Final circle/divisor discrepancy conclusion, not a bound for either open project node. | Its exponent cannot be imported into the internal graph. |
| TTY, Definitions 11--12/Theorem 20 | Coefficient-one/model-phase interval sum, not the residual selector coefficient. | Per-\(r\) absolute value and endpoint variation. |
| Robert--Sargos, Theorems 1--2 | Unsigned trilinear/moment or spacing object, not the signed determinant correlation. | Hölder loses character, selector, and aggregate signs. |
| Grimmelt--Merikoski 2024, Theorem 10.1 | No admissible automorphic/smooth realization of the actual selector-dependent multiplier. | \(C^7_\delta\) phase cost; common-\(f\) variable-\(r\) obstruction; \(\mathcal K_+\); principal main term; boundaries. |
| Lau 2026, Theorem 5.2 | Its verified automorphic periodic selector is not the project selector. | Fixed \((h,k)\), smoothness, \(\delta^{-O(1)}\), and \(\mathcal K_+\). |
| Grimmelt--Merikoski 2025 Part I, Theorem 1.1 | No exact two-endpoint relative-kernel representation. | Both positive selector/phase autocorrelations remain unbounded; Corollary 1.5 restores invariance/smoothness. |
| Lau, Theorems 1.1--1.2 | Coefficients are the specified divisor correlations, not \(c^{\rm rem}_{n+r}\overline{c^{\rm rem}_n}\). | Fixed-shift main/error, triangle loss, smooth support, and no \(h\asymp x\) endpoint. |
| BJN, Theorems 3/5 | Fixed automorphic Whittaker/Hecke coefficient class. | Absolute summation loses the required power; second estimate averages the centre; ranges need completion. |
| Bettin--Chandee, Corollary 1 | Required factorization of coefficients and smooth one-variable weights fails for the selector/product phase. | Fixed-\(r\) errors sum too large; sharp endpoints remain. |
| Blomer--Pascadi, Theorems 1.1/1.6 | No exact transform to one fixed-modulus Kloosterman or fixed-level spectral form. | Varying composite levels, joint selector, positive square, and completion. |
| Shparlinski--Xiao, Theorems 2.2/2.5 | Fixed-large-prime modular-square-root/Salié kernel is not the Archimedean square-root-difference determinant kernel. | Type I/II factorization, selectors, varying levels, and endpoints. |
| Pascadi, Theorem 1.2 | No fixed-level/cusp spectral representation of the target. | Positive spectral mean square does not preserve the \(r\)-aggregate sign. |
| Guth--Maldague, Theorem 3 | Spatial Fourier-localized \(L^p\) cone inequality, not the fixed-\(J\) arithmetic sum. | Discretization, cap hypotheses, coefficient smoothing, pointwise recovery, and endpoints. |

## 4. First doubtful or unproved step

The first unproved step in the proposed source route is:

> Construct a finite, target-safe partition of the literal residual determinant family for which the full selector-dependent multiplier is either an element of the exact Grimmelt--Merikoski automorphic class or is represented by a permitted smooth test function, without changing the outer-real-part aggregate and without introducing uncontrolled endpoint or correlation norms.

This step is prior to any appeal to spectral cancellation.  Determinant/gcd compatibility does not solve it.  Neither smoothing the selector nor saying that its two endpoints “factor” is enough: the proof must preserve the exact relative determinant kernel, avoid cross-terms, and bound the norm created by the representation.

If that step succeeds, the next unproved steps, in order, are:

1. quantify the \(C^7_\delta\) cost of \(e(\Phi_r)\) on every cell, including the top short stratum and maximal endpoint, and restore the hidden \(\delta^{-O(1)}\) power;
2. encode the \(hk\)-dependent frequency in one aggregate theorem, rather than applying a fixed-\(r\) estimate and summing absolute errors;
3. prove target-safe \(\mathcal K_+\), principal-main-term, boundary, cell-count, and \(\mathcal R_i\) bounds;
4. exhibit the actual coefficient/sign mechanism that fails for the phase-aligned arbitrary arrays.

For Part I, the corresponding first step is the exact two-endpoint relative-kernel realization; if achieved, the first new analytic step is bounding both discrepancy autocorrelations at the project scale.

## 5. Required controls and outcomes

1. **Primary-source currency — PASS with citation repairs.**  The principal version claims in Section 2.5 match the audited arXiv and official journal records.  Pascadi must be cited as arXiv:2404.04239v3.  Blomer--Pascadi and Shparlinski--Xiao should be explicitly labeled v1.  The Li--Yang conclusion must remain dated and must not claim to exclude unpublished or unindexed work.

2. **Li--Yang pointwise benchmark — PASS, scoped.**  Theorem 1.2 is pointwise for real \(X\) and yields the displayed \(\theta_*\).  It is external benchmark evidence only, subject to the local v2 repairs.  It neither proves a project node nor changes the certified internal exponent \(1/3\).

3. **Determinant and gcd map — PASS.**  The matrix assignment, determinant, \(q_1=4,q_2=1\) character choice, two-adic factorization, both gcd conditions, and determinant range are compatible.  The induced character is principal, so a source main term survives and must be estimated.

4. **First-failure ordering — PASS after wording repair.**  The first unverified application hypothesis is selector admissibility in the automorphic/smooth class.  Oscillatory seminorm loss is second, variable-\(r\) aggregation third.  Determinant/gcd hypotheses are not the first failure.  The report should avoid claiming an abstract impossibility of all automorphic representations; what is established is that no such representation is proved in the source or campaign artifacts.

5. **Phase seminorm — FAIL as presently quantified; repair is exact.**  The formula \(\delta^{-1}\gtrsim1+Jr/L\) is correct.  The statement that it is “at least order \(J\)” throughout \(r\lesssim L\) is false.  Replace it everywhere by: “the cost reaches order \(J\) on the top short-shift stratum \(r\asymp L\), while it ranges down to \(1+O(J/L)\) for bounded even \(r\); it reaches order \(JL\) near \(r\asymp L^2\).”  The theorem's hidden polynomial loss is “not certified target-safe,” not automatically proved fatal.

6. **Aggregate-real-part placement — PASS with a precision repair.**  The target has one real part after the full \(r\)-aggregate.  Theorem 10.1 has a complex \(h,k\) aggregate and one global asymptotic error, which is directionally compatible if all weights fit.  A fixed-\(r\) application followed by triangle inequality is not compatible.  State this distinction explicitly; do not describe the source theorem itself as moving absolute values inward.

7. **Fejer and endpoint control — OPEN.**  The linear Fejer multiplier is separable of rank two after fixed dyadic/two-adic localization and is not by itself the first obstruction.  The cutoff \(hk<R\), sharp shell/selectors, boundary cells, and recombination remain unproved and must be costed.

8. **Average versus restricted/pointwise — PASS.**  The source report correctly rejects average-to-pointwise promotion.  It should also preserve the finer distinction in Section 3.3: a fixed-shift or fixed-modulus theorem with restricted coefficients is deterministic/pointwise in its parameters, not an averaged theorem.

9. **Aligned-array falsification — PASS and mandatory.**  Energy-only/fixed-shift Cauchy gives \(L^3\) at (165.K17a) and \(L^4\) at (165.K26).  Phase-aligned arrays attain the short positive capacity.  Any claimed source transfer must visibly use a property of the actual coefficient and must fail for this control.

10. **K17a strategy licensing — PASS only at strategy level.**  The blind and graph reports support choosing K17a as the smallest exact surviving residual theorem.  The determinant source gives a candidate joint-orbit mechanism and a falsifiable checklist.  It supplies no accepted dependency, no truth evidence for K17a beyond structural compatibility, and no authorization to promote TOP, BAL, UNBAL, M1, M9, or the quarter exponent.

## 6. Dependencies and exact artifacts used

### Repository artifacts read in full

- `rounds/codex-managed/full-proof-round164-166-strategy-literature-review/reports/current_primary_literature_audit.md`
- `rounds/codex-managed/full-proof-round164-166-strategy-literature-review/reports/full_graph_frontier_strategy_audit.md`
- `rounds/codex-managed/full-proof-round164-166-strategy-literature-review/reports/blind_frontier_priority_rederivation.md`
- `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`

### Primary sources used to verify the seam

- Li--Yang: <https://arxiv.org/abs/2308.14859>, theorem text at <https://arxiv.org/html/2308.14859v2>
- Bourgain--Watt withdrawal record: <https://arxiv.org/abs/1709.04340>
- Grimmelt--Merikoski 2024: <https://arxiv.org/abs/2404.08502>, theorem text at <https://arxiv.org/html/2404.08502v2>
- Grimmelt--Merikoski Part I: <https://arxiv.org/abs/2505.00489>, theorem text at <https://arxiv.org/html/2505.00489v2>
- Lau: <https://arxiv.org/abs/2509.07556>, theorem text at <https://arxiv.org/html/2509.07556v2>
- Tao--Trudgian--Yang: <https://arxiv.org/abs/2501.16779>
- Blomer--Jana--Nelson: <https://arxiv.org/abs/2404.10692>; official journal record <https://doi.org/10.1007/s00039-025-00714-0>
- Pascadi: <https://arxiv.org/abs/2404.04239>; official journal record <https://doi.org/10.1017/fmp.2026.10025>
- Blomer--Pascadi: <https://arxiv.org/abs/2607.24311>
- Shparlinski--Xiao: <https://arxiv.org/abs/2601.10113>
- Guth--Maldague: <https://arxiv.org/abs/2206.01093>

The currency determination is limited to the completed primary-source audit as of 2026-08-26.  No secondary summary is used to establish a theorem statement.

## 7. Recommended state effect and precise repair ledger

**Recommended state effect: no change.**  Retain all accepted graph statuses and the certified internal exponent \(1/3\).  Retain Li--Yang only as the dated external pointwise benchmark.  Retain Grimmelt--Merikoski Theorem 10.1 only as a candidate strategy mechanism with the exact promotion gate above.  Reject direct import of every audited candidate into (165.K17a) or (165.K26).

Before the source report and graph strategy report are treated as final Round-166 evidence, make these precise documentary repairs:

1. In the source report's opening definition, replace
   `\sum_{d\mid N,,2\nmid d}` by
   `\sum_{\substack{d\mid N\\2\nmid d}}`, and use the authoritative symbol \(\mathfrak C\), not \(C\), in (165.K17a).
2. In source-report Sections 1, 3.1, and control 5.6, replace the uniform short-range claim \(\delta^{-1}\gtrsim J\) by the stratum-correct ledger: \(1+Jr/L\) throughout, reaching \(J\) only for \(r\asymp L\), and reaching \(JL\) for \(r\asymp L^2\).
3. Replace “cannot be absorbed into \(X^\varepsilon\)” by “the source statement's \(\delta^{-O(1)}\) loss is not shown target-safe until its exponent, the \(J\)-range, partition count, and all other factors are restored.”
4. Sharpen the Grimmelt--Merikoski failure order: first, no proved admissible representation of the actual selector-dependent coefficient; second, conditional \(C^7\) phase/endpoints; third, common-\(f\) variable-\(r\) aggregation.  Preserve determinant/gcd/character compatibility as a passed preliminary map.
5. Replace “sum over \((h,k)=1\) strengthened to \((h,kq)=1\)” by “sum restricted by \(\gcd(h,kq)=1\).”
6. Describe Theorem 10.1 as a complex aggregate equality with one global error.  State that a per-\(r\) specialization followed by triangle inequality, not the theorem itself, moves absolute values inside the required aggregate.
7. Record that the linear Fejer factor is rank-two separable on a localized \(h,k\) piece; keep the hyperbolic cutoff and endpoint completion as separate open costs.
8. In the Part-I summary, replace “linear-function weights” by “compactly supported linear functionals,” and retain the exact two-endpoint-kernel and two-autocorrelation gates.
9. Cite Pascadi as arXiv:2404.04239v3.  Add explicit v1 labels to Blomer--Pascadi arXiv:2607.24311 and Shparlinski--Xiao arXiv:2601.10113 where version currency is asserted.
10. Repair the Shparlinski--Xiao Corollary 2.8 display from `le` to `\le`.
11. Qualify the source report's `primary_source_exact_hypotheses` control.  For TTY, reproduce or explicitly cross-reference Definition 11's model-phase derivative hypotheses; for Robert--Sargos, reproduce or explicitly cross-reference the definition of the Theorem-1 sum.  Treat Huxley as abstract-level benchmark evidence only, as the report already intends.
12. In the graph strategy report, remove the malformed control character in the odd-divisor formula and write `2\nmid d` (or `d\ {\rm odd}`).
13. Wherever the graph report calls Grimmelt--Merikoski a “new mechanism,” qualify it consistently as a **candidate source model/mechanism subject to the source-to-interface gate**.  Its exact determinant map supports investigation; it does not prove that the missing cancellation exists.
14. Keep the pointwise-record wording explicitly dated: “the completed primary-source search found no later indexed claimed improvement as of 2026-08-26.”  Do not convert that search result into an unrestricted mathematical assertion about all unpublished or future work.
15. State explicitly in the Round-166 synthesis that selecting (165.K17a)/(167.F) is licensed only as strategy.  Even a proof of K17a would close only the complete residual scalar; the other hard-TOP channels, the TOP parent, BAL, UNBAL, a complete M1 route, M9 assembly, endpoints, and the final exponent bridge would remain.

After these repairs, the source audit is suitable evidence for one narrowly framed Round-167 experiment: attempt the literal selector-aware, oscillatory, variable-determinant aggregate, and stop with a scoped no-go at the first failed promotion gate.  It is not suitable evidence for a graph promotion.
