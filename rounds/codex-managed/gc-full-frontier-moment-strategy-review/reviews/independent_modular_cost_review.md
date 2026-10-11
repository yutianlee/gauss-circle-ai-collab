# Round205 — independent modular identity and cost review

Campaign: `gc-full-frontier-moment-strategy-review`.
Role: independent line auditor, explicitly unmasked after completing the separate statement-only task.
Generated: 2026-09-26 01:47:39 UTC.
Status: **SCOPED GREEN**; no error found in the finite modular completion or the stated upper-cost ledger.

Audited report:
`rounds/codex-managed/gc-full-frontier-moment-strategy-review/reports/internal_arithmetic_routes.md`.
Exact SHA-256, checked before and after the audit:
`e128c8d9121a4553681943e7716130c75cfe9e25383ef01cad8bc60f677983ef`.

Antecedent:
`rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/reports/complete_source_analytic_derivation.md`.
Exact SHA-256:
`aca866f155dea0acbfca6b161649c4f82d166340bbb6a1d8aefffaa85cf69ccd`.

The starting graph hash quoted by the audited report is provenance only; the graph was not read or revalidated in this review. The completed blind report was not changed.

## 1. Result

The following claims pass this scoped audit:

- The physical determinant chart and finite identity (205.I9) are exact, with the actual modulus \(q=d/g\).
- The bounded extension in (205.I6) preserves the original coefficient on the modular hyperbola. Its use requires no smoothness assertion for unspecified literal traces.
- The Fourier normalization, Parseval norm, and second moment (205.I10)–(205.I11) are correct, including nonunit k.
- The complete Fourier/Cauchy cost \(L^{7/2}X^\varepsilon\), direct cost \(L^3X^\varepsilon\), and stated legal-part theorem costs \(L^{119/32}X^\varepsilon\) and \(L^{11/3}X^\varepsilon\) are correct upper certificates for the displayed procedures.
- The source forces q to be odd and squarefree on live charts. It does not force a balanced factorization of q.
- The two linked theorem statements match the hypotheses and exponents used. Their primitive restrictions are retained by the kernel during the singular-value decomposition.
- Nonunit shifts, nonprimitive frequencies, the zero mode, and \(q=1\) are explicitly accounted for. No target-safe estimate for all exceptions is asserted.

**This is a weak-bound/no-certified-import conclusion, not an impossibility theorem.** The certified cost of a particular positive estimate being too large does not prove that the actual completed matrix has a large projective norm, that the actual correlation is large, or that another extension, signed recombination, or theorem cannot succeed. The audited report explicitly preserves these distinctions.

The graph-frontier inventory, other parent routes, whole-discrepancy strategy comparison, withdrawal metadata, and the separate fresh literature lead are outside this review's assigned scope. GREEN does not independently certify those sections.

## 2. Exact statement and hypotheses under review

The reviewed source is (205.I2), identical to the complete endpoint opening (200.A10) of (200.A4), with all literal coefficients retained:

\[
C_{\rm even}=\sum_{\substack{0<r<R\\2\mid r}}(1-r/R)
\sum_{d'm'-dm=r}b(m',d')\overline{b(m,d)}
e\!\left(\sigma\sqrt X(\sqrt{d'm'}-\sqrt{dm})\right).
\]

Here \(R=\lceil L\rceil\), live m and d are comparable to L, d is odd, \(\mu^2(md)=1\), and \(|b(m,d)|\ll_\varepsilon X^\varepsilon\). The exact character, selector, sign, and endpoint traces are inside b. The target remains the one-sided upper bound on \(\Re C_{\rm even}\), equivalently a target-size parity energy after adding the already controlled diagonal.

For each fixed d, put \(g=(d,d')\), \(q=d/g\), \(a=d'/g\), and \(r=gk\). Then \((a,q)=1\) and k is positive and even. Formula (205.I6) defines A on all residue pairs; (205.I8) evaluates it only at \((x,k\bar x)\) with x a unit. For \(q>1\), the Fourier transform is normalized by \(q^{-2}\), and S is the unnormalized ordinary Kloosterman sum defined in the report.

The theorem calls are restricted to \((k,q)=1\) and \((s,t,q)=1\), with arbitrary product vectors supported on translated intervals of length \(O(\sqrt q)\). Pascadi's favorable \(q^{-1/12}\) saving is additionally restricted to compatible balanced factorizations; it is not assumed for every physical q.

## 3. Proof and independent derivation

### 3.1 Exact physical chart, lifts, and squarefree modulus

Dividing \(d'm'-dm=r\) by g gives

\[
am'-qm=k.
\]

Conversely, any chart point with \((a,q)=1\), \(am'\equiv k\pmod q\), and live endpoint coefficients recovers

\[
d'=ga,\qquad m=(am'-k)/q,\qquad r=gk.
\]

Moreover \((d,d')=g(q,a)=g\), so the gcd label is neither lost nor multiply counted. Since every live d is odd, g is odd, and the condition that r is even is exactly the condition that k is even. No unit condition on k is needed here.

For \(a\asymp L/g\asymp q\), a containing interval has length \(O(q)\) and hence \(O(1)\) representatives of any residue. The m-prime interval has length \(O(L)=O(gq)\), giving \(O(g)\) representatives of a residue. Therefore

\[
|A(x,y)|\ll_\varepsilon gX^\varepsilon.
\]

On \(xy\equiv k\pmod q\), every lifted pair satisfies \(am'\equiv k\pmod q\), so the floor in (205.I6) is the exact integer quotient. Off that hyperbola it merely defines an extension. Both endpoint coefficients still enforce all original predicates, and positivity is tested before evaluating the square roots. Thus no sharp endpoint has been rounded in the physical source.

Squarefreeness of md implies squarefreeness of d, and every divisor \(q=d/g\) of that d is squarefree. In fact \((g,q)=1\), though that extra fact is not needed for (205.I9). Dead nonsquarefree-d charts contribute zero. No nontrivial prime-square modulus is available on live support.

### 3.2 Fourier inversion and the exact Kloosterman second moment

With the report's Fourier sign convention,

\[
A(x,y)=\sum_{s,t\bmod q}\widehat A(s,t)e((sx+ty)/q).
\]

Substituting \(y=k\bar x\) and summing over units x gives exactly

\[
T_{d,g,k}=\sum_{s,t\bmod q}\widehat A(s,t)S(s,kt;q).
\]

There is no additional power of q, no conjugation missing, and no multiplicity from a residue lift. Opening the Kloosterman sums and reversing Fourier inversion returns (205.I8).

Parseval with this normalization gives

\[
\sum_{s,t}|\widehat A(s,t)|^2
=q^{-2}\sum_{x,y}|A(x,y)|^2\ll_\varepsilon g^2X^\varepsilon.
\]

For any integer k, opening the squared Kloosterman sum yields

\[
\begin{aligned}
\sum_{s,t}|S(s,kt;q)|^2
&=\sum_{u,v\bmod q}^{*}
\sum_s e(s(u-v)/q)
\sum_t e(kt(\bar u-\bar v)/q)\\
&=q^2\varphi(q).
\end{aligned}
\]

The s sum forces \(u=v\); after that the t phase is identically one, whether or not k is a unit. Cauchy consequently gives
\(|T_{d,g,k}|\ll gq\sqrt{\varphi(q)}X^\varepsilon\ll gq^{3/2}X^\varepsilon\).
The direct hyperbola estimate is \(|T_{d,g,k}|\ll g\varphi(q)X^\varepsilon\ll gqX^\varepsilon\).

### 3.3 Independent outer-sum ledger

If the per-chart estimate is \(gq^\kappa X^\varepsilon\), positive summation over the \(O(L/g)\) allowed k values gives

\[
\sum_{d\asymp L}\sum_{g\mid d}\frac Lg\,g(d/g)^\kappa
\ll L^{\kappa+2+\varepsilon}.
\tag{R1}
\]

For \(\kappa>1\), the divisor sum \(\sum_{g\mid d}g^{-\kappa}\) is even bounded by a convergent zeta sum; for \(\kappa=1\), a subpower estimate suffices. The fixed Fejer factor is at most one. The live height condition bounds L polynomially in X, so these subpower factors may be absorbed in \(X^\varepsilon\).

Thus \(\kappa=3/2\) gives \(L^{7/2}\), while \(\kappa=1\) gives \(L^3\), as asserted. This is the full d, g, k ledger, rather than a single-chart estimate.

### 3.4 Theorem hypotheses and matrix norms

The linked [Blomer–Pascadi Theorem 1.1](https://arxiv.org/html/2607.24311v1) allows translated integer intervals of lengths at most N, a unit multiplier, arbitrary complex product vectors, and the kernel restriction \((m,n,c)=1\). At \(N\asymp\sqrt c\), its three saving powers are \(c^{-1/32},c^{-1/32},c^{-1/18}\); the resulting operator bound is \(c^{31/32+o(1)}\). The unrestricted variant applies only to the specified initial intervals. The report correctly does not use that variant on its translated rectangles.

For unit k, the substitution \(x=ky\) proves \(S(s,kt;q)=S(ks,t;q)\). This leaves s in its original interval and supplies the theorem's unit multiplier k; it does not require claiming that multiplication by k maps intervals to intervals. The primitive condition is unchanged because k is invertible.

Let \(B=\widehat A\,\mathbf1_{(s,t,q)=1}\). On each rectangle J of side lengths \(O(\sqrt q)\), finite singular-value decomposition gives

\[
\|B_J\|_\pi\le\sqrt{\operatorname{rank}B_J}\,\|B_J\|_{\rm HS}
\ll q^{1/4}\|B_J\|_{\rm HS}.
\]

There are \(O(q)\) disjoint rectangles, so

\[
\sum_J\|B_J\|_\pi
\ll q^{1/4}q^{1/2}
\left(\sum_J\|B_J\|_{\rm HS}^2\right)^{1/2}
\ll gq^{3/4}X^\varepsilon.
\]

The projective norm here uses products \(u(s)v(t)\); complex conjugation in the usual singular-value notation is absorbed into v. Individual factors need not be primitive-supported. Pair each factor with the theorem's primitive kernel; summing the decomposition recovers B paired with that same kernel, exactly as stated in the report. This does not discard an arithmetic mask.

Multiplying \(q^{31/32}\) by this norm certificate gives \(gq^{55/32}\). Equation (R1) then gives \(L^{119/32}\).

The linked [Pascadi Theorem 1.2 and Example 1.3](https://arxiv.org/html/2511.08445v2) have the stated factorization, interval, unit, product-vector, and primitive-kernel hypotheses. For squarefree physical q, write the theorem's divisor as D to avoid confusion with the physical d. Then \(D'=1\), \(e=q/D\), and \(f=D\); the saving is \(\min(D,q/D)^{-1/6}\). Balanced squarefree factors give \(q^{-1/12}\). Such a factorization is not guaranteed by squarefreeness. Its favorable operator power \(q^{11/12}\), multiplied by \(gq^{3/4}\), gives \(gq^{5/3}\), and hence \(L^{11/3}\).

Both primary theorem statements therefore support their reported legal-part upper prices. The favorable Pascadi row is not a uniform theorem for all physical moduli. Unfavorable moduli require another bound, such as the already checked general-modulus bound or the elementary completion estimate.

### 3.5 Explicit exception partition and reconstruction

A disjoint accounting of the source is:

1. \(q=1\), handled directly.
2. \(q>1\) and \((k,q)>1\), retaining the complete physical chart.
3. \(q>1\), \((k,q)=1\), and primitive frequencies \((s,t,q)=1\).
4. \(q>1\), \((k,q)=1\), and nonprimitive frequencies, with the zero frequency pair a subpiece of this last part.

Part 1 costs at most \(L^2X^\varepsilon\): then \(g=d\asymp L\), there are \(O(1)\) shifts per d, and the one-residue chart costs \(O(gX^\varepsilon)\). The report does not need any sharper support exclusion.

Part 2 has the direct \(L^3X^\varepsilon\) bound; the unit-multiplier theorem calls do not apply as written. Part 4 has the restricted Cauchy bound \(L^{7/2}X^\varepsilon\), because restricting a frequency set cannot increase either squared-norm sum used above. Its zero mode individually has \(|\widehat A(0,0)|\ll gX^\varepsilon\) and \(S(0,0;q)=\varphi(q)\), giving at most \(L^3X^\varepsilon\). The report's zero-mode row is a diagnostic subrow of its general nonprimitive complement; these should not be mistaken for two disjoint identities.

The report therefore does not silently suppress any exceptional part. It also does not claim that these coarse costs are target-safe. The same interpretation applies to the favorable-modulus restriction in the Pascadi row.

Finally, (200.A25)–(200.A26) imply \(|\sum_Nz_N|^2\ll LQ_R\). An absolute correlation bound of order \(L^3\) gives \(Q_R\ll L^3X^\varepsilon\), a scalar bound \(L^2X^\varepsilon\), and, after the stationary factor \(X^{1/4}L^{-3/2}\), the physical bound \(X^{1/4}L^{1/2}X^\varepsilon\). A target correlation \(L^2\) would instead give scalar \(L^{3/2}\) and physical \(X^{1/4}\). The square-root conversion of correlation savings and deficits is correct.

## 4. First doubtful or unproved step

No doubtful step was found in (205.I5)–(205.I15) when read with their stated restrictions and upper-bound interpretation.

The first unresolved analytic step remains an affordable estimate sensitive to the actual completed coefficient, or a signed aggregate estimate across charts, together with target-safe treatment of the exceptional portions. The current projective-norm bound is an upper certificate. Its size cannot establish a lower bound on the actual norm. Likewise, a theorem price above the target is not evidence that the actual sum exceeds the target.

The extension (205.I6) is not claimed optimal. This review does not rule out a different extension, smaller actual projective mass, cancellation between rectangles or charts, or a stronger compatible theorem. No full arithmetic import or impossibility claim receives GREEN.

## 5. Controls and outcome

| Control | Outcome |
|---|---|
| Physical bijection and gcd recovery | GREEN: \((d,d')=g\) follows exactly from \((a,q)=1\). |
| Even shifts and both endpoint configurations | GREEN: g is odd; k even is exactly r even; no orientation restriction was introduced. |
| Off-hyperbola extension | GREEN: exact on the source, bounded off it, all literal coefficients retained. |
| Fourier sign and normalization | GREEN: inverse transform produces (I9) without an additional factor. |
| Nonunit-k second moment | GREEN: s orthogonality alone forces the diagonal, giving \(q^2\varphi(q)\). |
| Squarefree modulus | GREEN: follows from the actual lower endpoint squarefreeness; balanced divisors are not inferred. |
| Matrix/projective ledger | GREEN: rank factor \(q^{1/4}\), rectangle-sum factor \(q^{1/2}\), and Hilbert norm \(O(g)\) are all charged. |
| Primary theorem restrictions | GREEN: both linked theorem texts checked; unit multiplier and primitive kernel retained. |
| Complete summation exponents | GREEN: independent formula (R1) reproduces all four principal exponents. |
| Exceptions | GREEN: direct q=1 and nonunit charts; nonprimitive/zero modes explicit; favorable-modulus restriction preserved. |
| One outer real part | GREEN: stronger absolute estimates are only sufficient procedures, not the original target. |
| No impossibility upgrade | GREEN: no actual-vector or norm lower bound is inferred from the weak upper ledger. |

All controls were analytical. Hashing was solely artifact identity verification, not a mathematical experiment. No numerical evidence was used to certify an asymptotic claim.

## 6. Exact dependencies

Local files read for this separate, unmasked audit:

1. `protocol.md`.
2. `rounds/codex-managed/gc-full-frontier-moment-strategy-review/reports/internal_arithmetic_routes.md`, exact hash above.
3. `rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/reports/complete_source_analytic_derivation.md`, exact hash above; specifically the complete coefficient/source identities, coefficient norms, parity energy, and reconstruction formulas.

Primary theorem texts inspected, solely for the two reported imports:

- [Blomer–Pascadi, arXiv 2607.24311v1, Theorem 1.1 and its critical-range specialization](https://arxiv.org/html/2607.24311v1).
- [Pascadi, arXiv 2511.08445v2, Theorem 1.2 and Example 1.3](https://arxiv.org/html/2511.08445v2).

No other local source, graph, manifest, sibling report, source card, or successor artifact was read for this review. The earlier statement-only analysis had already ended before these files were opened. No claim of latest-version or withdrawal-record certification is added by this scoped theorem-text check.

## 7. Recommended state effect

Record **SCOPED GREEN** for the exact modular completion and the specified upper-cost/no-certified-import ledger, tied to the audited report hash above. No correction to the reviewed modular formulas is required.

Do not convert this result into a universal modular impossibility theorem, a lower bound for the actual arithmetic correlation, or proof of any open parent. Any promotion of the finite identity alone must retain the actual coefficient extension, normalization, live squarefree modulus, and exception scope. Parent statuses, accepted exponents, and the quarter target remain unchanged.

Only this review file was written. The completed blind report, state, and successor artifacts remain untouched. The review stops here.
