# Final internal verification: Round 168 Mellin--Euler kernel

- Kernel: proofs/kernels/m9_m2_hard_top_t1_mellin_euler_polylog_signed_moment_reduction.md
- Kernel SHA-256: a973afdc81fcae9e2866ee1779e7d3c07e19b53e013c3eac2a9ff4fe13ba52f0
- Role: final accepted-kernel verifier
- Verdict: **PASS**

## 1. Result

**PASS.** The final kernel is a faithful homogeneous extraction of the
repaired conductor candidate. Every displayed identity and quantifier
checks: the literal scalar and floor normalization, Euler factors,
cardinal Mellin convention, ordered contour shift, residue coefficient
series including \(p=2\), one-cell integration-by-parts bound, shifted
integral normalization, radial stationary and Cauchy powers,
\(\eta/\varepsilon\) ordering, fixed-\(\kappa\) connector, fixed-\(B\)
polylogarithmic sector, provenance, and downstream quarantine.

The kernel does not transfer the cardinal residue saving to a discrete
Stieltjes realization, does not assert an AFE-to-Round-162 coefficient
bridge, and does not contain any source-dependent impossibility claim.
The expanded provenance paragraph merely names
M9-M2-top-endpoint-actual-symbol-variation as owner of the literal
bounded symbol and endpoint/profile conventions and H4-Phi-regularity as
owner of the \(\Phi\)-regularity convention. It changes no hypothesis,
equation, deduction, or promotion scope. No repair is required.

## 2. Exact statement and hypotheses

The parameter identities

\[
J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
q_X=X/y^2,\qquad
H=\lfloor yX^{-1/4}\rfloor=\sqrt J+O(1)
\tag{168.F1}
\]

are exact in the asserted sense. Indeed,
\(yX^{-1/4}=(J+O(1))J^{-1/2}=\sqrt J+O(J^{-1/2})\), and the final floor
adds \(O(1)\). Thus

\[
\frac{\sqrt J}{L}=\frac HL+O(L^{-1}),
\tag{168.F2}
\]

as used in (168.K23).

Equation (168.K2) matches the inherited literal selector-free \(t=1\)
scalar: the product shell, squarefree/coprime restriction, odd first leg,
even second-leg branch, cone, normalization, \(\eta_L\),
\(\Phi(n/(H+1))\), \(q_X\)-ratio profile, square-root phase, floors,
stars, half-open faces, endpoint transitions, and zero extension are all
retained. The cone and product shell give \(n,m\asymp L\), so the
non-arithmetic amplitude is bounded on \(O(L^2)\) ordered pairs.

The exact Mellin identity holds for every fixed \(0<\eta<1/4\). In the
capacity test, a requested output \(\varepsilon>0\) is fixed first, then
\(0<\eta\leq\min(1/8,\varepsilon/4)\), and finally an auxiliary
\(\delta>0\) sufficiently smaller than \(\varepsilon\). The strict
residual sector fixes both \(B>0\) and \(\kappa>0\).

## 3. Proof/derivation

### 3.1 Euler algebra

At \(p=2\),

\[
D_2=1+2^{-s_2},\qquad
G_2=(1+2^{-s_2})(1-2^{-s_2})=1-2^{-2s_2}.
\tag{168.F3}
\]

For odd \(p\), with
\(x_p=\chi_4(p)p^{-s_1}\) and \(y_p=p^{-s_2}\), the three admissible
local states give \(D_p=1+x_p+y_p\), and removal of the local
\(L(s_1,\chi_4)\zeta(s_2)\) factors gives

\[
\begin{aligned}
G_p
&=(1+x_p+y_p)(1-x_p)(1-y_p)\\
&=1-x_p^2-y_p^2-x_py_p+x_p^2y_p+x_py_p^2.
\end{aligned}
\tag{168.F4}
\]

For \(\sigma_1,\sigma_2>1/2\), the nonconstant terms have the summable
prime majorant printed in the kernel. Hence (168.K4)--(168.K5) and the
direct holomorphy region are correct. No nonvanishing is asserted.

### 3.2 Mellin convention and contour order

The kernel uses

\[
\widehat{\mathcal B}(s_1,s_2)
=\int_0^\infty\!\int_0^\infty
\mathcal B(x,z)x^{s_1-1}z^{s_2-1}\,dx\,dz.
\tag{168.F5}
\]

Because the cardinal cells are disjoint and
\(\psi(0)=1\), \(\mathcal B(n,m)=A_{L,X}(n,m)e(J\sqrt{nm})\) exactly.
The finite interpolant is smooth and compactly supported away from both
axes, so its transform is entire and rapidly decreasing on fixed
vertical strips. Mellin inversion gives inverse powers
\(n^{-s_1}m^{-s_2}\); summing them against the arithmetic coefficient
produces \(D(s_1,s_2)\), proving (168.K19) with the correct signs and
factor \((2\pi i)^{-2}\).

The contour order is lawful and explicit. Move \(s_2\) first while
\(\Re s_1=c_1>1\), crossing only the simple pole of \(\zeta(s_2)\) at
\(1\); then move the remaining \(s_1\)-line. The cardinal transform
controls the horizontal edges, \(G\) is holomorphic in the rectangle,
and \(L(s_1,\chi_4)\) is entire. On the final vertical lines,
\(ds_1ds_2=i^2dt_1dt_2\) cancels the sign in
\((2\pi i)^{-2}\), giving the positive factor \((2\pi)^{-2}\) in
(168.K7).

### 3.3 Residue series and integration by parts

For odd \(p\), at \(s_2=1\),

\[
L_p(s,\chi_4)G_p(s,1)
=(1+\chi_4(p)p^{-s}+p^{-1})(1-p^{-1})
=(1-p^{-2})+(1-p^{-1})\chi_4(p)p^{-s}.
\tag{168.F6}
\]

Together with the two-adic factor \(1-2^{-2}\), extracting
\(\prod_p(1-p^{-2})=\zeta(2)^{-1}\) gives exactly

\[
L(s,\chi_4)G(s,1)
=\frac1{\zeta(2)}
\sum_{\substack{n\geq1\\n\ \mathrm{odd,\ squarefree}}}
\frac{\chi_4(n)}{n^s}
\prod_{p\mid n}(1+p^{-1})^{-1}.
\tag{168.F7}
\]

Here the factors on successive lines are multiplied. Expanding on
\(\Re s>1\) and applying one-variable Mellin inversion gives
(168.K21). The \(n=1\) coefficient is correctly \(1/\zeta(2)\), and
every residue coefficient has modulus at most one.

On a supported cell, set
\(\phi(z)=2\pi J\sqrt{nz}\). Then
\(\phi'(z)=\pi J\sqrt{n/z}\asymp J\). Since
\(\psi(z-m)\) is compactly supported,

\[
\int\psi(z-m)e^{i\phi(z)}\,dz
=-\int
\frac{d}{dz}\left(\frac{\psi(z-m)}{i\phi'(z)}\right)
e^{i\phi(z)}\,dz
\ll J^{-1},
\tag{168.F8}
\]

with no boundary term. There are \(O(L^2)\) cells, proving
\(R_\zeta\ll L^2J^{-1}\), and hence the weaker displayed
\(R_\zeta\ll_\varepsilon L^2J^{-1}X^\varepsilon\). Since
\(L\ll J^{1/2}\), this is below \(L^{3/2}X^\varepsilon\).

The kernel asserts only this cardinal residue. It makes no claim that the
discrete Perron--Stieltjes residue inherits (168.F8), so the
representation distinction is preserved by omission rather than
conflated.

### 3.4 Radial and epsilon ledgers

For the explicitly qualified recombined smooth/BV control component,
\(x=rw\), \(z=r/w\), and \(t_+=t_1+t_2\) give radial phase

\[
2\pi Jr+t_+\log r.
\]

Its saddle is \(t_+=-2\pi Jr\asymp-JL\), and as \(r\asymp L\) varies,
the band length is \(T\asymp JL\). On
\(\Re s_1=\Re s_2=1/2+\eta\), stationary phase gives pointwise scale

\[
L^{1+2\eta}T^{-1/2}
=L^{2\eta}\sqrt{L/J},
\]

and radial \(L^2\)-norm \(L^{1+2\eta}\). Triangle inequality with the
granted pointwise majorant, and Cauchy with the granted fixed-angular
mean square, each give the raw capacity

\[
L^{2\eta}\sqrt J\,L^{3/2}X^\delta.
\tag{168.F9}
\]

Because \(L\leq X^{1/4+o(1)}\),

\[
L^{2\eta}X^\delta
\leq X^{\eta/2+o(1)+\delta}.
\]

With \(\eta\leq\varepsilon/4\) and then \(\delta\) sufficiently small,
this is \(O(X^\varepsilon)\). The remaining factor \(\sqrt J\) is the
correct structural deficit. The statement is confined to the two named
absolute placements and is not a physical lower bound or universal
no-go.

### 3.5 Polylogarithmic sector and \(\kappa\)-connector

Boundedness on \(O(L^2)\) pairs gives
\[
|\mathcal S_{L,1}|\ll L^2.
\]
For fixed \(B\), \(L\leq(\log X)^B\) implies
\[
L^{1/2}\ll_{\varepsilon,B}X^\varepsilon,
\]
which proves (168.K12) with every literal endpoint included.

For each fixed \(\kappa>0\), (168.K13) is the accepted exact
close-opposite-prime XOR decomposition and bound. Therefore
\[
|\mathcal S^{\rm rem}_{L,1;\kappa}|
\leq|\mathcal S_{L,1}|
+|\mathcal S^{\rm cp}_{L,1;\kappa}|,
\]
which proves (168.K14) with implied constant depending on
\(\varepsilon,B,\kappa\). No general residual estimate follows.

## 4. First doubtful or unproved step

No doubtful or unproved step remains inside the asserted kernel. The
first genuinely open theorem is (168.K8), the signed two-height estimate
in the polynomial \(L\)-range, or an equivalent endpoint-lawful physical
estimate.

The kernel expressly does not assert an exact coefficient bridge from
factorwise functional equations or approximate functional equations to
the Round-162 collar. Its imported collar comparison applies only after
deliberately reopening the original projector by the accepted Möbius
identity and then using positive physical Poisson.

## 5. Required controls and outcomes

| Required control | Outcome |
|---|---|
| Literal scalar and hard conventions | **PASS.** Equation (168.K2) matches the inherited object. |
| Mellin convention and inverse signs | **PASS.** Equations (168.K18)--(168.K19) have the correct forward and inverse powers. |
| Contour order and normalization | **PASS.** \(s_2\) moves first; only \(s_2=1\) is crossed; (168.K7) has factor \((2\pi)^{-2}\). |
| Euler local factors | **PASS.** Odd-prime algebra and \(G_2=1-2^{-2s_2}\) are exact. |
| Residue coefficient series | **PASS.** Equation (168.K20) includes the full \(1/\zeta(2)\) factor and correct odd-squarefree coefficients. |
| Residue IBP | **PASS.** One compact-cell integration gives \(J^{-1}\); \(O(L^2)\) cells give \(L^2/J\). |
| Cardinal/Stieltjes separation | **PASS.** No discrete-residue saving is inferred. |
| Radial stationary powers | **PASS.** Band \(JL\), pointwise scale \(L^{1+2\eta}(JL)^{-1/2}\), norm \(L^{1+2\eta}\). |
| \(\eta/\varepsilon\) ordering | **PASS.** The raw \(L^{2\eta}\) is retained and absorbed only after the output epsilon is fixed. |
| Fixed-\(B\) full sector | **PASS.** The absolute \(L^2\) bound gives the stated polylogarithmic sector. |
| Fixed-\(\kappa\) connector | **PASS.** Both pieces and the implied constant have the correct \(\kappa\)-dependence. |
| Homogeneous provenance | **PASS.** The scalar, collar comparison, XOR connector, literal bounded-symbol conventions, and \(\Phi\)-regularity are explicitly attributed; all new Euler/cardinal/residue/capacity/polylog deductions remain internal. |
| Nonpromotion scope | **PASS.** No polynomial full/residual target, other channel, parent, bridge, theorem, or exponent is promoted. |

## 6. Dependencies/exact artifacts used

Only the assigned artifacts were used:

1. protocol.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/candidates/conductor_round168_mellin_euler_polylog_and_signed_moment_reduction.md;
3. rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reviews/conductor_candidate_mathematical_review.md;
4. rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reviews/conductor_candidate_source_scope_review.md;
5. proofs/kernels/m9_m2_hard_top_t1_mellin_euler_polylog_signed_moment_reduction.md.

No proof graph, active campaign, shared state, synthesis, source report,
claimant report, or other kernel was inspected or edited in this task.
The graph identifiers M9-M2-top-endpoint-actual-symbol-variation and
H4-Phi-regularity were checked only as the provenance labels printed in
the assigned kernel.

## 7. Recommended state effect

**PASS.** Accept the final kernel at its literal scope: exact
Mellin--Euler/cardinal reduction with target-safe residue, the
two-placement \(\sqrt J\) capacity obstruction, and the fixed-\(B\)
full plus fixed-\(\kappa\) residual polylogarithmic sectors.

This verdict applies to kernel SHA-256
a973afdc81fcae9e2866ee1779e7d3c07e19b53e013c3eac2a9ff4fe13ba52f0.
The provenance-only expansion introduces no mathematical defect.

Retain (168.K8) as the first open polynomial-range signed two-height
interface. Do not infer an AFE self-return, general residual estimate,
other hard-TOP channel, hard TOP, BAL, UNBAL, M9--M2, either M1 parent,
GAR, endpoint assembly, M9, either bridge, quarter theorem, or exponent.
