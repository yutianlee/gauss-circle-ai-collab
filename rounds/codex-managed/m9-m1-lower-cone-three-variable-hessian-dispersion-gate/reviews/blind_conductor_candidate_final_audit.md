# Final blind audit of the Round-146 conductor candidate

## 1. Verdict

**CONDITIONAL GREEN.** Equations (146.C1)--(146.C34) are mathematically consistent with the accepted owners and the three Round-146 reports. The coefficient bijections, parity, capacity, Hessian and eigenvalues, cone faces, \(h=0\) split, phase-level Legendre qualification, Cao--Zhai power ledger, and downstream no-claim scope all pass.

Promotion should wait for two local but owner-relevant wording repairs:

1. define the masked small-\(t\) scalar separately from the inherited \(\mathfrak T_N\), so the two disjoint error owners in (146.C2) are explicit;
2. state (146.C33) as a sufficient separate \(t=1\) prefix estimate, not a logically necessary consequence of the full joint target.

A third provenance tightening is recommended in the state-effect paragraph: the new Round-146 fact is (146.C2)--(146.C8); (146.C9)--(146.C14) are inherited accepted coefficient identities and should be linked rather than presented as a new promotion. These are mechanical corrections. After they are applied, the candidate is GREEN without a new mathematical derivation.

## 2. Required line-specific corrections

### Correction 1 — lines 28--66, equations (146.C1)--(146.C3)

The displayed sum (146.C1) is called “the exact masked small-\(t\) scalar” but is never assigned a symbol. Equation (146.C2) then uses \(\mathfrak T_N\). In the accepted Round-145 notation, \(\mathfrak T_N\) denotes the pre-tail Round-144 cone scalar and satisfies

\[
\mathfrak T_N=(\text{masked small-}t\text{ scalar})
O_{\varepsilon,V}(X^\varepsilon)
\]

by the large-\(t\) owner. If that inherited meaning is retained, the direct comparison \(\mathfrak T_N=\mathfrak U_N^{<}+O(X^\varepsilon)\) contains **two** disjoint errors: the inherited large-\(t\) tail and the newly restored small-\(t\), small-displacement window. Lines 61--62 currently say that “the comparison adds only” the latter.

Introduce, for example,

\[
\mathfrak S_N^{<,>}
:=(146.C1),
\]

and state the two steps

\[
\mathfrak S_N^{<,>}
=\mathfrak U_N^{<}+O_{\varepsilon,V}(X^\varepsilon)
\]

from the restricted cell owner, and

\[
\mathfrak T_N
=\mathfrak S_N^{<,>}+O_{\varepsilon,V}(X^\varepsilon)
=\mathfrak U_N^{<}+O_{\varepsilon,V}(X^\varepsilon)
\]

after the inherited large-\(t\) owner. Equivalently, explicitly redefine \(\mathfrak T_N\) to mean (146.C1), but that would conflict with Round-145 notation and is not recommended.

This repair does not change (146.C2); it makes its definition and owner accounting exact. Equation (146.C6) already supplies the correct disjoint sets \(A,B,C\), and (146.C7), (146.C8) correctly own \(B\), \(C\), respectively.

### Correction 2 — lines 551--562, equation (146.C33)

The phrase “the \(t=1\) face requires” is too strong if read as a logical consequence of the full estimate (146.C32): a genuinely joint proof could use cancellation between \(t=1\) and other \(t\)-layers. What is true is that any route owning \(t=1\) separately needs a signed estimate of this strength, and (146.C33) is a sufficient exact prefix formulation.

Replace the prose by “A separate owner for the \(t=1\) face would be supplied by the uniform prefix estimate” and write its literal form as

\[
\sup_{M\leq U\leq B_M}
\left|
\sum_{\substack{M\leq s<U\\s\ {\rm squarefree}}}
V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns})
\right|
\ll_{\varepsilon,V}M^{3/4}X^\varepsilon.
\]

Partial summation then restores \(s^{-3/4}\). This retains the intended no-go: no reviewed proof supplies such a separate face estimate, while a stronger joint theorem is still logically possible.

### Provenance tightening — lines 609--618

Change “create a proved unmasking reduction recording (146.C2)--(146.C14)” to “create a proved unmasking reduction recording (146.C2)--(146.C8), depending on and restating the accepted coefficient interface (146.C9)--(146.C14).” The coefficient formulas are correct, but their proof status is inherited from Round 145; the new graph mutation is the exact unmasking.

## 3. Equation audit: definitions, owners, and coefficient algebra

| Equations | Verdict | Audit |
|---|---|---|
| (146.C1)--(146.C3) | **GREEN after Correction 1.** | The masked and unmasked sums are exact. The cell and large-\(t\) errors are target-safe and disjoint after restricting the accepted absolute owners. |
| (146.C4)--(146.C5) | **GREEN.** | \(T^2DE\asymp M\), and the no-go label is correctly scoped to the listed mechanisms. |
| (146.C6)--(146.C8) | **GREEN.** | For integral \(t\), \(t<M^{1/4}\iff t<\lceil M^{1/4}\rceil\). Strict \(>\), complementary \(\leq\), exact radicals, half-open blocks, and the unmasked tail are accounted for without double charging. |
| (146.C9)--(146.C14) | **GREEN; inherited.** | The squarefree-common-kernel and full-gcd formulas are bijective. \(\gamma,d,e\) are pairwise coprime squarefree variables; \(\gamma,e,b\) are odd; there is no false coprimality on \(a,b\) or \(G\); the character and strict cone are exact; \(|\kappa_t(d,e)|\leq\tau_3(t)\). |
| (146.C15) | **GREEN.** | A box has \(O(TDE)=O(M/T)\) triples and weighted coefficient-envelope price \(X^\varepsilon M^{1/4}/T\). The terminal logarithmic shell is epsilon-safe but gives no fixed-power reduction. |

The exact-radical term in (146.C7) is legitimately included via its separate accepted absolute owner. The use of the unrestricted cell owner on only \(t<T_M\) is monotone and legal. The Round-145 estimate used in (146.C8) is genuinely unmasked because its proof discarded the mask after taking absolute values.

## 4. Equation audit: Hessian, cone, faces, and transforms

Equations (146.C16)--(146.C18) are correct:

\[
f^{-1}\operatorname{diag}(t,d,e)\nabla^2f\operatorname{diag}(t,d,e)
=
\begin{pmatrix}
0&1/2&1/2\\
1/2&-1/4&1/4\\
1/2&1/4&-1/4
\end{pmatrix},
\]

with eigenvalues

\[
-\frac12,\quad \frac1{\sqrt2},\quad-\frac1{\sqrt2},
\]

determinant \(1/4\), and unscaled determinant \(f^3/(4t^2d^2e^2)\).

Equations (146.C19)--(146.C21) and the face ledger are GREEN. From \(t=\gamma ab\),

\[
\frac ab=\frac{\gamma a^2}{t}\geq\frac1t,
\]

so \(e/d>4/t^2\), \(d^2<m/4\), and \(e^2>4m/t^4\). Hence \(E=1\) is empty, fixed bounded \(E\) lies in a terminal target-safe shell, \(D=1\) remains structural rather than universally nonzero, and \(t=1\) has the stated singular \(d,e\) Hessian. The corrected \(B_M\) product-boundary phase and the cone-collar scope are accurate. A fixed lattice-width cone collar costs

\[
M^{-3/4}TD\,X^\varepsilon\ll X^\varepsilon
\]

using \(T<M^{1/4}\), \(D\ll M^{1/2}\).

Equation (146.C22) is exact under zero extension. Lines 347--349 correctly separate the constant \(h=0\) diagonal from the rank-one \(h\neq0\) phases.

Equations (146.C23)--(146.C26) are also exact at their stated level. For positive first aliases, the critical point and value are correct. The gradient-image volume \(F^3/V_3\), stationary amplitude \(V_3/F^{3/2}\), aliaswise upper price \(F^{3/2}\), and weighted price \(N^{3/4}\) have the correct powers. The candidate now correctly says that:

- this is an ideal smooth-interior alias count, not an exact lattice asymptotic for the literal amplitude;
- triangle inequality gives only an adverse upper price, not a lower bound;
- \(c\mapsto-2/c\mapsto c\) is a phase-monomial involution only after reversing the second alias orthant;
- it is not an amplitude-level two-step identity.

Equation (146.C27) is the exact \(N=sL^2+1\) slow-frequency family and is used only to refute false uniform separation.

## 5. Equation audit: source powers and first open estimate

Equations (146.C28)--(146.C31) are GREEN. Cao--Zhai Theorem 6 has the stated coefficient class \(a(m)b(m_1,m_2)\), excludes exponent \(1\) from the distinguished \(\alpha,\gamma\) slots, and permits the placement

\[
(m,m_1,m_2)=(d,t,e),\qquad
(\alpha,\beta,\gamma)=(1/2,1,1/2).
\]

The fourteen exponents in (146.C30) agree term by term with the source audit. In particular,

\[
R^{-3/2}(FD^5T^7E^7)^{1/8}
=R^{3/8-5\tau/8},
\]

so the term remains \(R^{1/16}\) at the formal \(\tau=1/2\) endpoint and becomes target-sized only at \(\tau\geq3/5\). The candidate correctly treats this as a limitation of that upper bound, not a lower bound for the scalar.

Equation (146.C32) is the exact new open scalar after unmasking. Equation (146.C33) has the right target power and partial-summation role, subject to Correction 2. Equation (146.C34) reproduces the unchanged accepted external exponent and is not used as a new conclusion.

## 6. Owner and downstream scope

The no-go scope is exact:

- coefficient-blind cancellation is refuted only for arbitrary bounded arrays;
- the \(t\)-difference route stops at an unproved exact correlation;
- the full transform followed by aliaswise modulus supplies no gain, but a future signed dual theorem is not excluded;
- a three-long-side theorem cannot discard \(t=1\), bounded \(t\), or \(D=1\);
- the direct primary-source cards fail first at the coefficient class and independently at a fixed positive power on balanced boxes.

The candidate does not infer a signed lower bound or failure of the desired estimate. The Round-138 collar-tail cross owner, complete lower-radial estimate, lower GAR, direct M1 parents, M9-M1, every M2 owner, M9-M2, endpoint uniformity, M9, bridge, quarter theorem, and both recorded exponent statuses remain unchanged. Lines 567--577 and 606--623 are GREEN after the provenance tightening above.

## 7. Recommended final action

Repair the symbol/owner chain around (146.C1)--(146.C3), weaken and literalize the separate \(t=1\) prefix statement (146.C33), and distinguish the new unmasking fact from the inherited coefficient interface in the state-effect bullet. Then accept:

1. the exact small-\(t\) unmasking reduction;
2. the scoped three-variable Hessian/source/transform no-go;
3. the unmasked \(\mathfrak U_N^{<}\) scalar as the first open owner;
4. no downstream theorem or exponent change.

No further mathematical correction is required.
