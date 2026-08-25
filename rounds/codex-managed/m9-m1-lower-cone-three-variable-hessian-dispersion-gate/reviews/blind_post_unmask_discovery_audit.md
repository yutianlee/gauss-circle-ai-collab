# Blind post-unmask audit of the three-variable Hessian discovery report

## 1. Verdict

**GREEN for the mathematical kernel, with five local wording/precision corrections required before the report is cited as an exact seam artifact.** The mask-removal reduction, both coefficient parametrizations, Hessian algebra, cone inequalities, bounded-face obstruction, \(t\)-difference identity, Legendre critical point, power ledger, and scoped no-go are correct. None of the corrections below changes the conclusion

\[
\mathsf{three\_variable\_dispersion\_no\_go}
\]

for a Hessian-only, coefficient-blind, or stationary-transform-followed-by-modulus argument. The report correctly does not claim a lower bound for the signed scalar or a downstream theorem.

## 2. Mask removal and disjoint owner seam

Let

\[
\begin{aligned}
A&=\{t<M^{1/4},\ |j|>M^{3/4}\},\\
B&=\{t<M^{1/4},\ |j|\leq M^{3/4}\},\\
C&=\{t\geq\lceil M^{1/4}\rceil\}.
\end{aligned}
\]

For integral \(t\), \(t<M^{1/4}\) is exactly \(t<\lceil M^{1/4}\rceil\), so \(A,B,C\) are disjoint and partition the unmasked squarefree-kernel support. The Round-145 survivor is \(A\), while (146.D2) is \(A\dot\cup B\). The accepted nonzero-cell estimate with \(J=M^{3/4}\), together with the separately accepted exact-radical estimate, controls \(B\) absolutely. Restricting that absolute owner to small \(t\) is legal. The accepted Round-145 tail majorant controls the unmasked set \(C\), because its proof discarded the mask only after taking absolute values.

Thus the target equivalence \(A\sim A\dot\cup B\) uses only the restricted cell owner; the large-\(t\) owner is a separate check on \(C\). No overlap is charged in this partition even though the unrestricted inherited majorants would overlap on large-\(t\), small-displacement points. Equations (146.D1), (146.D15)--(146.D17), and the accompanying prose handle this correctly.

One clarification is advisable: (146.D1) partitions the **unmasked ambient squarefree-kernel support**, not the already masked Round-145 survivor. The report's argument already uses the correct interpretation.

## 3. Coefficient, Hessian, cone, and short-face seams

The coefficient seam is exact.

- In the squarefree-common-kernel form, \(\gamma,d,e\) are pairwise coprime and squarefree, \(de=s\), \(t=\gamma ab\), \(e,\gamma,b\) are odd, and
  \[
  \chi_4(r)=\chi_4(\gamma)\chi_4(e),\qquad r>4h\iff eb^2>4da^2.
  \]
  No coprimality on \(a,b\), or between them and \(\gamma\), is inserted.
- In the full-gcd form, \(G=(h,r)\), \(Gab=t\), \((da,eb)=1\), \(Geb\) is odd, and the character is \(\chi_4(Ge)\). No false coprimality involving \(G\) is imposed.
- The inverse constructions are multiplicity one, and
  \[
  |\kappa_t(d,e)|\leq\sum_{\gamma ab=t}1=\tau_3(t)
  \]
  is valid.

The scaled Hessian in (146.D28) is correct. Its eigenvalues are

\[
-\frac12,\quad \frac1{\sqrt2},\quad-\frac1{\sqrt2},
\]

so its determinant is \(1/4\), and

\[
\det\nabla^2f=\frac{f^3}{4t^2d^2e^2}.
\]

The cone ledger is also correct:

\[
\frac{e}{d}>4\left(\frac ab\right)^2\geq\frac4{t^2},
\quad d^2<\frac m4,
\quad e^2>\frac{4m}{t^4}.
\]

It follows that \(D\ll\sqrt M\), \(E\gg\sqrt M/T^2\), \(E=1\) is empty, and fixed bounded \(E\) is forced into a terminal \(T\)-shell. The \(T=1\) face has singular \(d,e\) Hessian and capacity \(M^{1/4+o(1)}\); the \(D=1\) face is not removed by the cone and is at best a separate two-variable problem.

Two local corrections are needed.

1. In the product-boundary row of the face table, \(f=\sqrt{NM}\) only on \(t^2de=M\). On the upper level \(t^2de=B_M\), the constant is \(f=\sqrt{NB_M}\). The intended statement is that the phase is constant on each fixed product level.
2. “\(D=1\) persists throughout every fixed-power range” should be read structurally/existentially: the displayed tuple \(\gamma=1,a=t,b=1,d=1\) shows that the cone does not exclude this face when \(e>4t^2\). It does not prove nonemptiness in every arbitrarily clipped block or nonvanishing of the net \(\kappa_t(1,e)\), since other factor tuples may cancel. The report already acknowledges the latter; the headline wording should be weakened accordingly. The exact \(t=1\), prime corner is enough to prove mandatory nonvacuity.

## 4. Difference and full Legendre-transform seams

With zero extension, (146.D37) is the exact identity

\[
\left|\sum_tA_t e(\lambda t\sqrt{de})\right|^2
=\sum_{h\in\mathbb Z}e(\lambda h\sqrt{de})
\sum_tA_{t+h}\overline{A_t}.
\]

For \(h\neq0\), the returned \(d,e\) phase has scaled Hessian

\[
\begin{pmatrix}-1/4&1/4\\1/4&-1/4\end{pmatrix}
\]

and rank one. For \(h=0\) the phase is constant, so that diagonal should be named separately rather than called rank one. This is a wording correction only; the coefficient correlation remains uncontrolled and the \(A\)-process supplies no proved saving.

For the smooth bare phase \(f_c(t,d,e)=c\,t\sqrt{de}\) with \(c=\sqrt N>0\), the critical equations for \(f_c-ut-vd-we\) have, for \(u,v,w>0\), the unique positive solution

\[
t_*=\frac{2\sqrt{vw}}c,\qquad
d_*=\frac uc\sqrt{\frac wv},\qquad
e_*=\frac uc\sqrt{\frac vw},
\]

and critical value

\[
-\frac{2u\sqrt{vw}}c.
\]

Thus (146.D38)--(146.D39) are correct. On a full smooth interior box, with \(F\asymp\sqrt{NM}\) and \(V_3=TDE\),

\[
|\det\nabla^2f|\asymp\frac{F^3}{V_3^2},\qquad
|\det\nabla^2f|^{-1/2}\asymp\frac{V_3}{F^{3/2}}.
\]

The gradient-image volume is \(\asymp F^3/V_3\), so an aliaswise absolute estimate has price at most

\[
\frac{F^3}{V_3}\frac{V_3}{F^{3/2}}=F^{3/2};
\]

after \(M^{-3/4}\), this is \(N^{3/4}\). The powers in (146.D40)--(146.D43) are correct.

Two precision qualifications are required here.

- Unless a lattice-point boundary estimate for the gradient image is supplied, write the alias count as \(Q\ll F^3/V_3\), or explicitly restrict \(\asymp\) to the ideal full smooth interior model. Likewise, “costs \(F^{3/2}\)” means the aliaswise triangle-inequality upper price; it is not a lower bound and does not rule out signed dual cancellation. The report's no-go scope already has this intended meaning.
- The coefficient map \(c\mapsto-2/c\) is an involution at the **phase-monomial level with an orthant reversal**. Starting from \(c>0\), the first stationary aliases have \(u,v,w>0\) and the dual coefficient is negative. A second stationary transform then uses the opposite alias orthant; after changing signs of those aliases,
  \[
  -\frac2{-2/c}=c.
  \]
  Therefore (146.D44) is algebraically correct, but it is not by itself a literal two-step Poisson identity for amplitudes. Maslov factors, transformed coefficients, boundaries, and the alias-orthant change remain. The report should say “phase-level involution after alias sign reversal,” which is all the scoped no-go needs.

## 5. First doubtful step and no-go scope

The first open inference remains the passage from algebraic nondegeneracy to a signed estimate for the literal coefficient. Divisor boundedness is insufficient because an arbitrary bounded coefficient class contains \(e(-f)\); smooth-amplitude theorems do not accept the exact divisor, squarefree, coprimality, parity, cone, product-endpoint, and profile structure without further work. The \(t\)-difference returns an unproved exact correlation, and the full transform returns an unproved signed dual-alias sum. Bounded \(t\), especially \(t=1\), remains outside any theorem requiring three growing sides.

Accordingly the report's no-go is correctly scoped to:

- Hessian determinant alone;
- arbitrary-coefficient or smooth-tensor substitution;
- one coefficient-robust \(t\)-difference without a correlation theorem;
- one full stationary transform followed by aliaswise modulus;
- any three-long-side theorem that leaves short faces to absolute disposal.

It is not a no-go for every possible signed theorem for the exact scalar, and it is not a lower bound. The discovery report states these limitations correctly.

## 6. Controls and artifacts checked

The following seams are GREEN after the local corrections above:

- disjoint mask/small-displacement/large-\(t\) owner logic;
- exact coefficient and multiplicity in both parametrizations;
- Hessian entries, eigenvalues, determinant, and box scaling;
- cone inequalities and the \(T=1,D=1,E=1\), bounded-\(E\), and terminal-\(T\) faces;
- exact \(t\)-difference identity;
- Legendre critical point and critical value;
- dual volume, stationary-amplitude, and physical-weight powers;
- phase-level self-return and coefficient-blind adversarial control;
- individual positive direction, fixed center, exceptional family, and downstream scope.

Artifacts checked were protocol.md, state/active_campaign.yml, the relevant accepted entries in state/proof_obligations.yml, the Round-146 discovery brief and report, the Round-145 conductor candidate and adjudication, and the Round-141 conductor candidate. No numerical or external-source input was used.

## 7. Recommended state effect

**Promote after the five local corrections/clarifications** the narrow mask-removal equivalence (146.D1)--(146.D2). **Retain** the exact coefficient, Hessian, capacity, cone, \(t\)-difference, and phase-level Legendre-return calculations as obstruction evidence. Record the transform statement only as an aliaswise-modulus and phase-involution no-go, with the orthant qualification. Keep the unmasked strict small-\(t\) scalar open, keep all short-face signed estimates open, and make no downstream promotion.
