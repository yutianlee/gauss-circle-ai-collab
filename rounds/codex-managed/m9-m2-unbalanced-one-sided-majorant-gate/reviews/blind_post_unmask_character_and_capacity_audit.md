# Post-unmask character and capacity audit

- Campaign: `m9-m2-unbalanced-one-sided-majorant-gate`
- Round: `134`
- Role: post-unmask blind reviewer
- Status: review evidence only

## 1. Result

The sibling reports are compatible on universal order, coefficientwise failure, character placement, rank-one order, capacity, and the absence of a Poisson saving. Their zeroth-coefficient result can be sharpened from an order-optimal sandwich to an exact optimum.

Put

\[
N=\Delta+1,\qquad H=qN+s,\qquad 0\leq s<N.
\]

Then, among real trigonometric polynomials of degree at most \(\Delta\) satisfying \(T\geq F_H\),

\[
\boxed{
\min t_0=\mathsf S_N(H)
=(N-s)q^2+s(q+1)^2
=\frac{H^2}{N}+s\left(1-\frac{s}{N}\right).
}
\tag{1.1}
\]

The minimum is attained by

\[
\boxed{
T^{\rm fold}_{H,N}(\alpha)
=\left|qD_N(\alpha)+D_s(\alpha)\right|^2.
}
\tag{1.2}
\]

Thus the discovery two-grid polynomial is lawful but nonextremal. The hostile lower bounds are correct and sharp.

The folded comparison is an exact, endpoint-complete Parseval reduction, but it is only a no-go at the requested fixed-power bandwidth: its zeroth survivor is

\[
\rho(H,N)=\frac{\mathsf S_N(H)}H\geq\frac HN.
\tag{1.3}
\]

If \(N\leq HX^{-\eta}\), then \(\rho\geq X^\eta\). A target-safe zeroth coefficient requires \(N\geq HX^{-o(1)}\), so no fixed-power contraction is target-safe.

The discovery report's hygiene-corrected character-Poisson normalization passes. Its reciprocal principal Gram is not endpoint-complete by itself; endpoint completeness applies to the exact Poisson integral or to the principal Gram plus the retained remainder \(\mathcal P_T\).

## 2. Exact statement and hypotheses

For finitely supported complex \(A\), zero-extended before shifts, define

\[
Q_G(A)=\int_0^1G(\alpha)|\widehat A(\alpha)|^2\,d\alpha,
\qquad F_H=|D_H|^2.
\]

The following statements audit the two reports.

1. Universal order
   \[
   Q_T(A)\geq Q_{F_H}(A)\quad\text{for every finite }A
   \]
   is equivalent to \(T\geq F_H\) pointwise. For one fixed literal vector, pointwise order is sufficient but need not be necessary.

2. For \(0\leq\Delta\leq H-1\), (1.1) is the exact minimum, attained by (1.2). For \(\Delta\geq H-1\), the minimum is \(H\), attained by \(F_H\).

3. The two capacity notions are
   \[
   \min\|T-F_H\|_{L^1(\mathbb T)}
   =\mathsf S_N(H)-H
   \tag{2.1}
   \]
   and
   \[
   \sum_{|r|\leq\Delta}|t_r|\geq T(0)\geq H^2.
   \tag{2.2}
   \]
   The folded extremizer attains equality in (2.2).

4. The hostile rank-one lemma applies to one fixed internal block square. The folded inequality compares sums over all translations and is instead a global Toeplitz/frame inequality.

5. Every lawful multiplier acts after
   \[
   A(k)=\sum_p\chi_4(p)b_{p,k}
   \]
   is formed. It preserves, but does not create, actual-character cancellation.

All conclusions remain restricted to the flat-smooth strict-UNBAL owner.

## 3. Proof and seam audit

### 3.1 Exact optimum

Exact \(N\)-point quadrature and finite Parseval give, for every degree-\((N-1)\) majorant,

\[
t_0=\frac1N\sum_{j=0}^{N-1}T(j/N)
\geq\frac1N\sum_{j=0}^{N-1}F_H(j/N)
=(N-s)q^2+s(q+1)^2.
\tag{3.1}
\]

For the reverse inequality, set

\[
P_{H,N}=qD_N+D_s
=\sum_{j=0}^{N-1}c_je(j\alpha),
\qquad
c_j=\begin{cases}q+1,&j<s,\\q,&s\leq j<N.\end{cases}
\]

Then \(T^{\rm fold}=|P_{H,N}|^2\) has degree at most \(N-1\) and zeroth coefficient \(\sum c_j^2=\mathsf S_N(H)\). To check pointwise order, let \(z=e(\alpha)\), \(w=z^N\), \(v=z^s\), and

\[
S_q(\bar w)=\sum_{a=0}^{q-1}(q-a)\bar w^a.
\]

Direct geometric-sum algebra yields

\[
|1-z|^2(T^{\rm fold}-F_H)
=|1-w|^2
\left(q(q+1)-2\operatorname{Re}\{\bar vS_q(\bar w)\}\right)\geq0,
\tag{3.2}
\]

because the coefficients of \(S_q\) sum to \(q(q+1)/2\). Continuity handles \(z=1\). Equations (3.1)--(3.2) prove exact optimality. Accordingly, the discovery relation \(\mathsf S_N(H)\leq\mu(H,\Delta)\) should be equality.

### 3.2 Order and complex cross terms

Both reports use the correct universal order. The forward implication follows from integrating \((T-F_H)|\widehat A|^2\). The converse follows by testing against translated Fejer approximate identities.

The hostile coefficientwise falsifier is valid:

\[
T-F_H=\varepsilon(e(\alpha)+e(-\alpha)),\qquad
A(0)=1,\quad A(1)=-1
\]

gives \(Q_T(A)-Q_{F_H}(A)=-2\varepsilon\). The folded construction does not use coefficientwise order: it deletes the high Fejer coefficients but dominates through the complete multiplier.

### 3.3 \(L^1\), coefficient \(\ell^1\), and rank one

Since \(T-F_H\geq0\), its \(L^1\)-excess is \(t_0-H\), proving (2.1). For the folded extremizer,

\[
t_r^{\rm fold}=\sum_jc_{j+r}c_j\geq0,
\qquad
\sum_r|t_r^{\rm fold}|=T^{\rm fold}(0)
=\left(\sum_jc_j\right)^2=H^2.
\tag{3.3}
\]

Hence modewise modulus has sharp raw factor \(H\), while a positive-diagonal closure has exact factor \(\rho(H,N)\).

There is no conflict with the hostile rank-one lemma. That lemma forbids a nonproportional inequality at each fixed \(n\). The folded statement is

\[
\sum_n\left|\sum_{a<H}A(n+a)\right|^2
\leq
\sum_n\left|\sum_{j<N}c_jA(n+j)\right|^2,
\tag{3.4}
\]

which generally fails termwise in \(n\) and becomes true only after summing overlapping translations. It belongs to lawful P1/global PSD-frame order, not rejected P4 local-window order.

### 3.4 Character placement and \(\Gamma\)

Expanding only after the actual character sum gives

\[
Q_T(A)=\sum_rt_r
\sum_{p,p'}\chi_4(p)\chi_4(p')
\sum_kb_{p,k}\overline{b_{p',k+r}}.
\tag{3.5}
\]

Thus both reports correctly reject \(p\)-wise moduli and separate positive-row norms. The folded window acts on the combined \(A\), so it retains the character but supplies no estimate of (3.5).

With

\[
\Gamma_{\rm before}=\min(H,Q),\qquad \Gamma_{\rm claimed}=1,
\]

the exact zeroth survivor is \(\rho(H,N)\), not \(1\). If \(N\leq H/\Gamma_{\rm before}\), then \(\rho(H,N)\geq\Gamma_{\rm before}\). The discovery's optimistic survivor may be sharpened from \(H/N\) to \(\rho(H,N)\), but it remains a capacity surrogate because the signed nonzero lags are unestimated.

### 3.5 Character-Poisson normalization and self-return

Use

\[
\widehat g(\xi)=\int_{\mathbb R}g(x)e(-\xi x)\,dx,
\qquad
\tau(\chi_4)=2i.
\]

Primitive character Poisson is

\[
\sum_n\chi_4(n)g(n)
=\frac{\tau(\chi_4)}4\sum_u\chi_4(u)\widehat g(u/4)
=\frac i2\sum_{u\ {\rm odd}}\chi_4(u)\widehat g(u/4).
\tag{3.6}
\]

For \(g(x)=f_k(x)e(\sqrt{Mkx})\), this gives the discovery exponent \(\sqrt{Mkx}-ux/4\). For \(u>0\),

\[
x_*=\frac{4Mk}{u^2},\quad
\phi(x_*)=\frac{Mk}{u},\quad
\phi''(x_*)=-\frac{u^3}{32Mk}.
\]

The stationary factor is

\[
2e(-1/8)(Mk)^{-1/4}
W\!\left(\frac{X}{Du}\right)
q_L\!\left(\frac{4Xk}{u^2}\right)e(Mk/u).
\]

Multiplying by the original prefactor gives

\[
\frac i2e(-1/8)M^{1/4}k^{-3/4}
\cdot2e(-1/8)(Mk)^{-1/4}
=\frac1k,
\tag{3.7}
\]

since \(i\,e(-1/4)=1\). The corrected \(i/2\), phase, sign, and \(1/k\) normalization therefore pass.

Exact Poisson retains all odd modes and is invertible. After stationary decomposition, only \(\mathcal Q_T^{\rm recip}+\mathcal P_T\) is endpoint-complete. The strict-interior principal return has no spare factor and retains the same \(t_0=\mathsf S_N(H)\); it does not prove a saving.

## 4. First doubtful or unproved step

The finite order, exact optimum, capacity, rank-one distinction, and corrected Poisson normalization are proved.

The first unproved step toward the target is a joint signed bound

\[
C_H\sum_{|r|<N}t_r^{\rm fold}
\sum_{p,p'}\chi_4(p)\chi_4(p')
\sum_kb_{p,k}\overline{b_{p',k+r}}
\ll_\varepsilon X^{1/2+\varepsilon},
\tag{4.1}
\]

with moving profiles, zero-extension faces, and all endpoint regimes retained. After Poisson, the required object is the complete principal-plus-remainder expression. The folded majorant itself supplies none of this cancellation.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| Universal multiplier/PSD order | Pass in both reports. |
| Exact zeroth optimum | Sharpen discovery and hostile to (1.1)--(1.2). |
| \(L^1\)-excess | Exact minimum \(\mathsf S_N(H)-H\). |
| Fourier \(\ell^1\)-capacity | Sharp lower \(H^2\), attained by the folded extremizer. |
| Coefficientwise order | Fails by the two-coordinate test; folded order is pointwise/PSD. |
| Rank-one internal window | Correct locally; no conflict with the global translated folded frame. |
| Actual \(\chi_4\) placement | Correct only before any \(p\)-wise modulus; majorization is character-blind. |
| Opposite-character/single-row controls | Valid universal controls, not literal counterexamples. |
| Character-Poisson normalization | Pass after hygiene correction. |
| Poisson/self-return | Exact or strict-interior only; the principal Gram alone is not endpoint-complete. |
| \(\Gamma_{\rm claimed}=1\) | Fails for the standalone fixed-power mechanism; exact zeroth survivor is \(\rho(H,N)\geq H/N\). |
| Owner scope | Remains flat-smooth strict-UNBAL only. |

## 6. Dependencies and exact artifacts used

This review used:

1. `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reports/actual_character_fejer_majorant_attack.md`;
2. `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reports/majorant_cross_term_hostile_audit.md`;
3. `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reports/blind_bandlimited_quadratic_majorant_feasibility.md`;
4. `rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/blind_statement.md`;
5. `protocol.md`.

No web source, numerical experiment, symbolic computation, sibling edit, shared-state edit, or additional strategy artifact was used.

## 7. Recommended state effect

**Promote, subject to conductor validation,** the exact folded optimum (1.1)--(1.2), its exact \(L^1\)-excess, and its sharp coefficient-\(\ell^1\) capacity.

**Revise the discovery report's extremal characterization** from a sandwich to equality. Retain its two-grid polynomial only as a lawful nonextremal construction. Accept its corrected character-Poisson normalization and \(1/k\) reciprocal principal row.

**Retain the hostile report's order, rank-one, character-placement, and capacity conclusions.** Clarify that the folded physical reduction is global over translations and does not contradict the local rank-one no-go.

**Qualify endpoint language:** \(\mathcal Q_T^{\rm recip}\) is a principal survivor; only the exact Poisson formula or \(\mathcal Q_T^{\rm recip}+\mathcal P_T\) is endpoint-complete.

**Reject the fixed-power one-sided majorant as a standalone route to \(\Gamma_{\rm claimed}=1\).** The exact folded optimum is a sharper no-go, not a target proof. Retain the literal target as open pending a new endpoint-complete, actual-character, jointly signed correlation theorem.
