## 1. Result

**No-go for promotion from the frozen packet alone.** The local compact-cell analysis, including a locally estimated masked radial endpoint, has no evident analytic obstruction. The displayed amplitude theorem is nevertheless not proved: the packet does not define the complete post-routing amplitude, quantify the dyadic \(j\)-sum, or state bounds for all owned remainder modules. Thus the radial consequence is rigorous *conditional on* the displayed BV bound, but that bound itself cannot yet be certified.

## 2. Exact statement and hypotheses

The conditional lemma is: if the exact post-routing amplitude satisfies

\[
\sup_{1\le x\le N_X}|\mathcal A(x)|+
\int_1^{N_X}|\mathcal A'(x)|\,dx\ll_\varepsilon X^\varepsilon,
\]

with endpoint stars retained, then the stated radial integral is \(O_\varepsilon(X^\varepsilon)\). For the packet's local estimates one also needs \(a+b<1/2\), Schwartz/moment bounds for the fixed Mellin profiles, pole-free compact gamma parameters, \(\log(2+N_X)\ll_\varepsilon X^\varepsilon\), and an \(O_\varepsilon(X^\varepsilon)\) quantitative \(j\)-scale mass.

## 3. Proof and derivation

Since \(\alpha=L+\beta\), compact \(\alpha,\beta\) force compact \(L\). The exact gamma ratios are uniformly bounded on this pole-free compact set; no asymptotic expansion is needed.

For either contour sign,
\((L-\nu\pm i0)^{-1}=\operatorname{pv}(L-\nu)^{-1}\mp i\pi\delta(L-\nu)\).
Hence the hard-top diagonal is the signed term \(\mp i\pi p_x(L)\), formed before absolute values. The principal-value part is bounded after subtracting \(p_x(L)\) locally, while its tail uses rapid decay of \(\widehat\phi\). The same argument survives one \(x\)-derivative because
\[
\partial_xp_x(\nu)=-\frac{i\nu}{2x}p_x(\nu).
\]
The remaining phase contributes exactly \(-i((L+\nu)/2+\beta)/x\); compact \(L,\beta\) and one Schwartz \(\nu\)-moment give \(O(dx/x)\), hence only \(\log N_X\).

Moreover \(r>1\) and \(p>1\), so \(\sum h^{-r}\sum q^{-p}<\infty\). This does not by itself bound the unstated \(j\)-mass.

Writing \(N=N_X\) and \(e(t)=e^{2\pi it}\), exact integration by parts gives
\[
\begin{aligned}
I={}&\frac{N^{-1-b/2}e(\sqrt{XN})\mathcal A(N)-e(\sqrt X)\mathcal A(1)}{\pi i}\\
&+\frac{1+b/2}{\pi i}\int_1^N x^{-2-b/2}e(\sqrt{Xx})\mathcal A(x)\,dx
-\frac1{\pi i}\int_1^N x^{-1-b/2}e(\sqrt{Xx})\mathcal A'(x)\,dx.
\end{aligned}
\]
Thus the BV hypothesis proves the radial claim. Existing stars remain inside the two displayed endpoint values, and no half-weight appears. Each beta-masked endpoint is bounded locally by the same compact/Schwartz majorant; no unmasked global endpoint limit is invoked.

## 4. First doubtful or unproved step

The first unsupported step is replacing the actual post-routing \(j\)-sum and remainder modules by an \(O_\varepsilon(X^\varepsilon)\) majorant. Neither their formulas, scale ranges, nor uniform profile norms occur in the packet. “Absolutely convergent” is not a quantitative uniform-in-\(X\) bound, and ownership of axial, collision, corner, connector, arithmetic, and artificial-pole terms cannot be checked.

## 5. Required control test and outcome

The analytic unsigned control fails: replacing the signed Plemelj section by \(\int|p_x(\nu)|/|L-\nu|\,d\nu\) diverges logarithmically whenever \(p_x(L)\ne0\). The signed subtraction plus diagonal passes. The endpoint control also passes conditionally: setting \(\mathcal A'=0\) in the exact formula retains both boundary coefficients and the integrable weight term.

## 6. Dependencies and artifacts

Used only protocol.md and rounds/codex-managed/m9-m1-beta-double-bounded-cell/statement_packet.md. No external theorem, computation, numerical experiment, or other round artifact was used.

## 7. Recommended state effect

**Revise/retain, not promote.** Preserve the exact radial lemma and the local masked-endpoint estimate, but require the explicit post-routing amplitude and a quantitative \(j\)-scale/module audit before accepting the compact-cell theorem.
