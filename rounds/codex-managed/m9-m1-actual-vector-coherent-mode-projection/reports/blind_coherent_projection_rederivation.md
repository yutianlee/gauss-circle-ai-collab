# Blind coherent-projection rederivation

## 1. Result

The statement packet determines an exact **conditional local algebra**, but it does not determine a target-scale global estimate or a global actual-vector lower bound.

Assume first that “the local factor modulo \(8\)” means the genuine coprime factorization

\[
M=8Q,\qquad (8,Q)=1.
\]

Then the \(u\equiv4\pmod 8\) trace component is

\[
\mathbf 1_{u\equiv4(8)}\mathfrak T_M
=-32\,\mathbf 1_{u\equiv4(8)}
 e_8\!\bigl(\alpha K(A-B_2)\bigr)
 \mathfrak T_Q(\beta u,A_Q,B_{2,Q},V_Q;\beta K),                 \tag{1}
\]

where \(\alpha Q\equiv1\pmod8\) and \(8\beta\equiv1\pmod Q\). The corresponding local orthogonal projector is the rank-one constant projector on the four odd residue classes. On those classes \(e_8(4x)=-1\), so the local \(u=4\) vector and the local \(u=0\) vector span the same line; their Fourier coefficients differ only by a minus sign. Removing the single **global** coefficient \(u=0\) therefore does not remove the local coherent line for nonzero \(u\equiv4\pmod8\), for nonzero \(u\equiv0\pmod8\), or in particular for nonzero multiples of \(M\).

For the fixed rows, the exact \(u=4\) coupling is not (1) multiplied by an arbitrary norm. It is a cofactor exponential sum weighted by the literal four-row local average displayed in (8) below. This average can vanish or cancel. Likewise, full physical backtracking is governed by the reversal projections \((1\pm J_M)/2\), whose actual couplings are squares of the symmetric and antisymmetric parts of the fixed pair vector; local backtracking modulo \(8\) alone is only \(J_8\otimes I_Q\), not full physical reversal \(J_8\otimes J_Q\).

Consequently, neither the nonzero local trace nor a large coefficient-blind capacity proves a global actual-vector lower bound. The weakest target-scale assertion is the signed fixed-vector bound (12), with the literal hard mask and every original normalization retained. It cannot be proved or refuted from the packet because the exact hard-owner predicate and literal \(I\)-data are absent (and, before even that, mere divisibility \(8\mid M\) does not by itself supply a CRT factor \(8\)).

## 2. Exact statement and hypotheses

Write \(\mathbb U_8=\{1,3,5,7\}\). The following statement uses only these hypotheses.

- \(M=8Q\) with \(Q\) odd. Put \(\alpha=Q^{-1}\pmod8\) and \(\beta=8^{-1}\pmod Q\).
- The inverse phase \(\Phi\) is CRT-compatible on the four-unit locus, as is necessary for the supplied local trace formula.
- The local four-unit locus is nonempty. Modulo \(8\) this forces \(A,B_2,V\) to be even, and then the allowed \(x_8\)'s are all of \(\mathbb U_8\).
- All congruences defining physical equality or reversal are taken modulo the modulus explicitly indicated. Equality modulo \(8\) is not silently upgraded to equality modulo \(M\).
- The global zero owner deletes precisely \(u=0\). Every further deletion is made only by the literal multiplier \(\mathbf1_{\mathscr H}\).

For \(r\in\mathbb U_8\) and \(y\pmod Q\), let

\[
x(r,y)=rQ\alpha+y8\beta\pmod M.                                  \tag{2}
\]

The CRT character identity is

\[
e_M(t)=e_8(\alpha t)e_Q(\beta t),                                \tag{3}
\]

and hence the normalized trace factors with no extra factor of \(M\):

\[
\mathfrak T_M(u,A,B_2,V;K)
=\mathfrak T_8(\alpha u,A_8,B_{2,8},V_8;\alpha K)
 \mathfrak T_Q(\beta u,A_Q,B_{2,Q},V_Q;\beta K).                 \tag{4}
\]

Since multiplication by the odd number \(\alpha\) fixes the residue class \(4\pmod8\), (4) and the supplied formula give

\[
\mathfrak T_M=
\begin{cases}
 32e_8(\alpha K(A-B_2))\mathfrak T_Q,&u\equiv0\pmod8,\\
-32e_8(\alpha K(A-B_2))\mathfrak T_Q,&u\equiv4\pmod8,\\
0,&u\not\equiv0,4\pmod8,
\end{cases}                                                       \tag{5}
\]

with the arguments on \(\mathfrak T_Q\) as in (4).

On each fixed \(Q\)-fibre define

\[
(\Pi_{8,\mathrm{coh}}f)(r,y)
=\frac14\sum_{s\in\mathbb U_8}f(s,y),
\qquad
\Pi_{8,\mathrm{coh}}^M=\Pi_{8,\mathrm{coh}}\otimes I_Q.         \tag{6}
\]

This is the exact orthogonal projector onto the local coherent line. If

\[
\widehat f_8(a;y)=\frac14\sum_{r\in\mathbb U_8}f(r,y)e_8(-ar),
\]

then

\[
\widehat f_8(4;y)=-\widehat f_8(0;y).                             \tag{7}
\]

Thus the residue selector \(\mathbf1_{u\equiv4(8)}\) selects one set of global Fourier labels, whereas (6) is the local \(x\)-space projector; they must not be identified as operators because \(u=0\) and \(u=4\) alias on \(\mathbb U_8\).

For the fixed actual rows put

\[
z_I(P;\theta)=\mathcal R_x(\theta)\overline{\mathcal R_{x-A}(\theta)},
\quad
F_I(r,y;\theta)=z_I(P;\theta)\overline{z_I(P';\theta)},
\]

so explicitly

\[
F_I(r,y;\theta)=
\mathcal R_x\overline{\mathcal R_{x-A}}
\overline{\mathcal R_{x-V}}\mathcal R_{x-V-B_2},
\qquad
C_I(y;\theta)=\frac14\sum_{r\in\mathbb U_8}F_I(r,y;\theta),     \tag{8}
\]

where \(x=x(r,y)\). Formula (8), rather than a free coefficient vector, is the fixed actual coupling.

For paired modes, let \(J_m\) reverse an ordered physical pair modulo \(m\), and set

\[
\Pi_{m,\pm}=\frac12(I\pm J_m).
\]

The exact entry conditions are

\[
D_m:\ V\equiv0,\ B_2\equiv A\pmod m,
\qquad
R_m:\ V\equiv A,\ B_2\equiv-A\pmod m.                          \tag{9}
\]

The one-count backtracking indicator relative to the diagonal is
\(\mathbf1_{R_m}(1-\mathbf1_{D_m})\). Full diagonal or reversal requires (9) at both CRT factors. In operator language,

\[
J_M=J_8\otimes J_Q,
\qquad
\text{whereas local reversal alone is }J_8\otimes I_Q.           \tag{10}
\]

For the complete, unmasked full-pair space,

\[
\langle z_I,\Pi_{M,\pm}z_I\rangle
=\frac14\sum_P\left|z_I(P)\pm z_I(P^{\mathrm{op}})\right|^2.   \tag{11}
\]

Pointwise in \(\theta\), \(z_I(P^{\mathrm{op}})=\overline{z_I(P)}\); hence (11) measures respectively the real and imaginary parts of the actual pair row. Either projection may be zero.

Finally, for any explicitly one-counted coherent package \(S\) (for example \(u\equiv4\pmod8\), or a diagonal/reversal package made disjoint by (9)), define \(E_{S}^{I,\mathscr H}\) by inserting \(\mathbf1_S\mathbf1_{\mathscr H}\) into the **original fixed actual energy**, leaving its four \(I\)-factors, Fejér factor, conductor sums, and all normalizations unchanged. The weakest sufficient target-scale statement is exactly

\[
\boxed{\quad
|E_{S}^{I,\mathscr H}|
\ll_\epsilon X^\epsilon\frac UB J^{14/5}.
\quad}                                                            \tag{12}
\]

There are no absolute values inside the defining sum in (12). An arbitrary-coefficient operator bound, an absolute summand bound, or a coefficient-blind capacity bound is strictly stronger and is not required by (12).

## 3. Proof or derivation

The CRT reconstruction (2) gives

\[
\frac{x(r,y)}M\equiv\frac{\alpha r}{8}+\frac{\beta y}{Q}\pmod1,
\]

which proves (3). Units and inverses factor over coprime moduli, so the complete \(x\)-sum factors. Because the convention is \(\mathfrak T_m=m\sum_x(\cdots)\), the product of the two local prefactors is \(8Q=M\), proving (4), not \(M^{-1}\mathfrak T_8\mathfrak T_Q\). Substitution of \(c_8(0)=4\), \(c_8(4)=-4\), and \(c_8(a)=0\) otherwise proves (5) and (1).

On an odd residue \(r\), \(e_8(4r)=-1\). Therefore the \(u=4\) character restricted to \(\mathbb U_8\) is minus the \(u=0\) character. Averaging over the four odd residues proves (6) and (7). It also shows directly why deleting the single global label \(u=0\) cannot delete the local line: global labels \(u\equiv4\pmod8\) still restrict to that line, as do nonzero labels \(u\equiv0\pmod8\). If \(u=tM\ne0\), both CRT frequency components are zero, so it is a completely coherent nonzero shift unless the Fejér support or \(\mathscr H\) deletes it.

The exact fixed-vector content of (6) follows by expanding all four rows. With

\[
\Delta=n_1-n_2-n_3+n_4,
\qquad
L=A n_2+V(n_3-n_4)-B_2n_4,
\]

one obtains

\[
F_I(r,y;\theta)=\frac1{M^4}\sum_{n_1,n_2,n_3,n_4}
 I(n_1)\overline{I(n_2)}\overline{I(n_3)}I(n_4)
 e(\Delta\theta)e_M(L)e_M(x(r,y)\Delta).
\]

Using (3) and averaging \(r\in\mathbb U_8\) yields the literal formula

\[
C_I(y;\theta)=\frac1{M^4}\sum_{\mathbf n}
 I(n_1)\overline{I(n_2)}\overline{I(n_3)}I(n_4)
 e(\Delta\theta)e_M(L)e_Q(\beta y\Delta)
 \frac{c_8(\alpha\Delta)}4.                                      \tag{13}
\]

Thus all four rows and their signs remain present. The \(u=4\) local Fourier coefficient is \(-C_I\); equivalently its multiplier in (13) is
\(c_8(\alpha\Delta-4)/4=-c_8(\alpha\Delta)/4\). This is an actual-symbol identity, not a replacement of \(I\) by arbitrary coefficients.

For clarity, insert the four-row weight directly into the trace and define

\[
\mathfrak K_M^I
=M\sum_x^{\mathrm{four\ units}}
e_M\!\left(ux+K\Phi(x)\right)F_I(x;\theta).
\]

On \(u\equiv4\pmod8\), the local phase is constant on the odd residues, so exact CRT summation gives

\[
\mathbf1_{u\equiv4(8)}\mathfrak K_M^I
=-4M\,\mathbf1_{u\equiv4(8)}e_8\!\bigl(\alpha K(A-B_2)\bigr)
\sum_y^{\mathrm{four\ units}}
 e_Q\!\bigl(\beta(uy+K\Phi_Q(y))\bigr)C_I(y;\theta).            \tag{14}
\]

When \(F_I\equiv1\), \(C_I\equiv1\), and (14) reduces to (1), since \(4M=32Q\). For the actual rows, however, (14) is a weighted cofactor correlation and need not be a scalar multiple of \(\mathfrak T_Q\). The Fejér expansion merely takes the appropriate Fourier coefficient of (13) and multiplies it by \((U-|u|)_+\); it does not turn \(C_I\) into \(1\).

The pair identities in (9) follow by solving \(P'=P\) and \(P'=P^{\mathrm{op}}\). The involution \(J_m\) is unitary and self-adjoint, so \((I\pm J_m)/2\) are orthogonal projectors, and expanding their quadratic forms proves (11). CRT of pair indices proves (10). In particular, a local reversal cycle may have an arbitrary cofactor pair and therefore is not by itself a global physical backtrack.

Lastly, a conjugation-closed mask guarantees at most the Hermitian symmetry of retained Gram entries. It need not be constant on an entire four-point local fibre, invariant under \(J_8\otimes I_Q\), or compatible with both factors of (10). Hence Schur restriction by \(\mathbf1_{\mathscr H}\) can preserve, delete, or fragment these projectors. Only after the literal mask is inserted can the signed scalar in (12) be formed and estimated.

## 4. First doubtful or unproved step

The first attempted implication that is not proved is

\[
\text{nonzero/large local trace}
\quad\Longrightarrow\quad
\text{nontrivial global projection of the fixed actual vector}.
\]

It fails as a matter of linear algebra: (14), not (1), is the actual coupling, and \(C_I\) may be orthogonal to the cofactor phase or identically zero in the relevant fibres. The mask may also remove only part of a local orbit, in which case there is no surviving orthogonal projector to which (11) applies.

The missing literal data occur in the following strict order.

- As written, the packet assumes only \(8\mid M\). An exact CRT factor \(8\) first requires \(M=8Q\) with \(Q\) odd, or else the complete \(2\)-power local factor and its lift must be supplied. If \(16\mid M\), formulas (1)--(5) are not justified from the mod-\(8\) trace alone.
- If “local factor modulo \(8\)” is intended to grant \(Q\) odd, the first datum deciding survival is the exact pointwise owner predicate \(\mathbf1_{\mathscr H}(u,A,B_2,V,K,\ldots)\), including its priority order. Conjugation closure alone does not say whether the mode is preserved, deleted, or fragmented.
- Conditional on survival, the first datum deciding a lower bound or (12) is the literal support and values of \(I(n)\), together with the exact outer/conductor normalization of the actual energy. The symbol \(I\) in the packet permits the exact identity (13), but not an estimate of it.

Thus no target-safe bound and no actual-symbol obstruction is established here; the rigorous output is the conditional projector identity plus this no-go seam.

## 5. Required control test and outcome

| Control | Exact input | Expected invariant or failure | Observed outcome | Implication |
|---|---|---|---|---|
| Literal fixed actual vector | The four factors in (8) and (13) | A trace-only argument must fail unless it evaluates their projection | The coupling is \(C_I\), not \(1\); literal values of \(I\) are absent | No actual-vector lower or target upper bound follows |
| \(q=8\) as a local CRT factor | Only \(8\mid M\) is stated | CRT with a factor \(8\) requires an odd cofactor | (4) is valid only under \(M=8Q\), \(Q\) odd | Exact \(2\)-adic factorization is a prerequisite |
| Unique global \(u=0\) owner | Delete the single label \(u=0\) | It must not delete an entire local coherent line | Equation (7) leaves every nonzero \(u\equiv4(8)\) and nonzero \(u\equiv0(8)\) label available | The zero owner cannot be reused to discard them |
| Nonzero \(u=4\) and modulus multiples | \(0<|u|<U\), with \(u\equiv4(8)\) or \(u=tM\ne0\) | These survive unless support or a literal owner removes them | Their local factors are respectively \(-4\) and \(+4\); modulus multiples are coherent at both CRT factors | They require explicit masked treatment |
| All four rows and physical pairs | \(P=(x,x-A)\), \(P'=(x-V,x-V-B_2)\) | No two-row or absolute-value shadow may replace the Gram entry | Expansion (13) retains \(I_1\bar I_2\bar I_3I_4\) and the exact signs | The derived coupling is the correct fixed four-row object |
| Hard-owner one count | \(\mathbf1_{\mathscr H}\), \(D_m\), \(R_m\) | Overlap must be assigned once | \(R_m(1-D_m)\) is disjoint from \(D_m\), but the packet gives no priority between parity and pair packages or prior owners | The exact mask/owner map is still required |
| Paired/backtracking cycles | Local and full reversal | Local reversal must not be promoted to physical reversal | \(J_M=J_8\otimes J_Q\), while the mod-\(8\) cycle is only \(J_8\otimes I_Q\) | Local paired coherence alone gives no global backtracking energy |
| Local trace versus global projection | \(c_8(4)=-4\) and (14) | A nonzero trace should not imply fixed-vector overlap | A fibre vector with four entries summing to zero has zero coherent projection despite the same nonzero trace; additionally the \(Q\)-correlation can cancel | The proposed lower-bound inference is falsified |
| Dense-plateau/capacity inference | Coefficient-blind capacity is target times \(J^{1/6}\) at the top | Capacity may not be read as fixed-vector mass | Equations (12)--(14) expose the missing signed actual correlation | Excess capacity is neither a lower-bound obstruction nor a proof of target failure |
| Downstream and exponent scope | Only one coherent package is under discussion | No full hard estimate or exponent follows | The remaining hard complement, endpoints, conductors, and transitions are untouched | All downstream claims remain open |

No numerical experiment was used. The zero-sum fibre example is a falsifying linear-algebra control, not a claim that the unspecified literal \(I\) realizes that example.

## 6. Dependencies and exact artifacts used

This report used only the incoming task brief, the Round-100 routing entry in state/active_campaign.yml, and the following statement-only context files:

- problems/gauss_circle.md
- state/control_models.md
- rounds/codex-managed/m9-m1-actual-vector-coherent-mode-projection/blind_statement.md

No proof graph, prior Round-87--99 derivation, sibling report, shared synthesis, external source, or numerical computation was used.

## 7. Recommended state effect

**Retain.** Retain (4)--(14) as a conditional statement-only CRT/projector lemma and retain the target obligation as open. Do not promote a target bound or an actual-vector obstruction. Before promotion, supply and audit, in order, the exact \(2\)-adic factorization of \(M\), the literal hard-owner mask with one-count priority, and the literal \(I\)-symbol plus all outer/conductor normalizations; then evaluate the signed fixed-vector quantity (12), not the coefficient-blind trace.
