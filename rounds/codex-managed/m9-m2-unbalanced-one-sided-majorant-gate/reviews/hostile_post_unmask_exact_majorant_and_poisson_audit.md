# Post-unmask hostile audit: exact folded majorant and character Poisson

## 1. Result

**Verdict: confirm the exact folded-majorant theorem; retain the close label majorant_no_go with a sharper statement; confirm the character-Poisson normalization and reciprocal principal Gram; reject any claim that the principal stationary Gram alone is endpoint-complete.**

The post-unmask claim ledger is:

| Claim | Verdict | Exact correction or consequence |
|---|---|---|
| \(\mu(H,N)=Nm^2+(2m+1)s\), where \(H=mN+s\), \(0\leq s<N\) | **Confirmed exactly** | This is the minimum zeroth coefficient among all real degree-\((N-1)\) polynomials \(T\geq F_H\). |
| \(T^*=|mD_N+D_s|^2\) attains the minimum | **Confirmed exactly** | The proposed pointwise factorization is correct, including \(s=0\), \(N=1\), and \(N=H\). |
| The folded selector gives a lawful shorter physical form | **Confirmed with scope** | It is a global inequality after summing all translations \(n\), not a pointwise inequality for each individual block square. Zero extension makes it endpoint-exact at this stage. |
| The exact theorem changes the close label | **No** | It upgrades the lower bound \(H^2/N\) to the exact \(\mu(H,N)\) and proves existence of a strict noninvertible contraction, but the exact surviving diagonal factor is \(\rho(H,N)=\mu(H,N)/H\geq H/N\). The standalone mechanism still cannot yield \(\Gamma=1\) under fixed-power contraction. |
| Discovery character-Poisson factor \(i/2\) | **Confirmed** | It follows from \(\tau(\chi_4)=2i\) with the stated \(e(x)=e^{2\pi ix}\) convention. |
| Stationary coefficient and profiles in (3.8)--(3.9) | **Confirmed as the interior principal term** | The coefficient is \(2e(-1/8)(Mk)^{-1/4}\) in \(I_u(k)\), and the two outside phases/constants cancel to give exactly \(k^{-1}\). The profiles are \(W(X/(Du))q_L(4Xk/u^2)\). |
| Reciprocal Gram (3.10) | **Confirmed for the principal rows** | Its shifts, conjugations, denominator, character factors, and phase are correct. |
| Endpoint completeness after stationary phase | **Not established for the principal Gram alone** | The exact Poisson integral is endpoint-complete. The decomposition into principal rows plus \(\mathcal P_T\) is exact only when \(\mathcal P_T\) retains every principal--remainder and remainder--remainder term. No uniform bound for that ledger is proved. |
| Sibling artifact integrity | **Formatting repair required** | No unexpected C0/DEL bytes were found, but both reports have pervasive missing inline-TeX delimiters; the discovery report also has an unmatched closing delimiter. |

The blind theorem materially sharpens the mechanism: a lawful, strict, bandwidth-\(N\) majorant really exists. It therefore corrects any wording that suggested that no noninvertible majorant step exists. The noninvertibility is precisely the folded inequality. What remains true is narrower and decisive: its exact mass cost cancels any lag-count-only gain, and Poisson supplies no second noninvertible saving.

## 2. Exact statement and hypotheses

Let

\[
D_j(\alpha)=\sum_{a=0}^{j-1}e(a\alpha),\qquad D_0=0,
\qquad F_H=|D_H|^2,
\]

and let \(1\leq N\leq H\). Write

\[
H=mN+s,\qquad m\geq1,\qquad 0\leq s<N.
\]

Define the extremal value

\[
\mu_N(H):=
\inf\left\{
t_0:
T(\alpha)=\sum_{|r|<N}t_re(r\alpha)
\ \hbox{is real and }T(\alpha)\geq F_H(\alpha)\ \hbox{for all }\alpha
\right\}.
\]

Then the exact theorem is

\[
\boxed{\mu_N(H)=Nm^2+(2m+1)s
=\frac{H^2}{N}+s\left(1-\frac{s}{N}\right).}
\tag{2.1}
\]

It is attained by

\[
\boxed{T^*_{H,N}(\alpha)=|P_{H,N}(\alpha)|^2,\qquad
P_{H,N}=mD_N+D_s.}
\tag{2.2}
\]

If

\[
n_j=
\begin{cases}
m+1,&0\leq j<s,\\
m,&s\leq j<N,
\end{cases}
\]

then \(P_{H,N}=\sum_{j=0}^{N-1}n_je(j\alpha)\), and for every finitely supported complex \(A\), zero-extended before translation,

\[
\sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
\leq
\sum_n\left|\sum_{j=0}^{N-1}n_jA(n+j)\right|^2.
\tag{2.3}
\]

The exact capacity quantities are

\[
t_0^*=\sum_jn_j^2=\mu_N(H),\qquad
\rho(H,N)=\frac{\mu_N(H)}H\geq\frac HN,
\tag{2.4}
\]

and

\[
\int_{\mathbb T}(T^*_{H,N}-F_H)
=\mu_N(H)-H
=Nm(m-1)+2ms.
\tag{2.5}
\]

Moreover all Fourier coefficients of \(T^*\) are nonnegative, so

\[
\sum_{|r|<N}|t_r^*|
=\sum_{|r|<N}t_r^*
=T^*(0)=H^2.
\tag{2.6}
\]

Thus the folded optimizer also realizes exactly the raw \(H\)-factor in a natural-scale lagwise absolute closure.

For the Poisson seam, write

\[
Q_T(A):=C_H\int_{\mathbb T}T(\alpha)|\widehat A(\alpha)|^2\,d\alpha,
\]

and retain the frozen literal coefficient

\[
A(k)=e(-1/8)M^{1/4}k^{-3/4}
\sum_{p>0\ {\rm odd}}\chi_4(p)f_k(p)e(\sqrt{Mkp}),
\]

where

\[
f_k(x)=x^{-3/4}
W\!\left(\frac{X}{2D}\sqrt{\frac{x}{Mk}}\right)
q_L((X/M)x)
\]

is extended by zero outside its literal positive smooth support. With the Fourier convention

\[
\widehat g(\xi)=\int_{\mathbb R}g(x)e(-\xi x)\,dx,
\]

primitive Poisson modulo \(4\) gives the exact identity

\[
A(k)=\frac{i}{2}e(-1/8)M^{1/4}k^{-3/4}
\sum_{u\ {\rm odd}}\chi_4(u)I_u(k),
\tag{2.7}
\]

\[
I_u(k)=\int_0^\infty f_k(x)
e\!\left(\sqrt{Mkx}-\frac{ux}{4}\right)\,dx.
\tag{2.8}
\]

For \(u>0\), the standard interior stationary principal term is

\[
I_u^{\rm main}(k)=
2e(-1/8)(Mk)^{-1/4}
W\!\left(\frac{X}{Du}\right)
q_L\!\left(\frac{4Xk}{u^2}\right)e(Mk/u).
\tag{2.9}
\]

After multiplication by the outside factor in (2.7), it gives

\[
\mathcal R(k)=\frac1k
\sum_{u>0\ {\rm odd}}\chi_4(u)
W\!\left(\frac{X}{Du}\right)
q_L\!\left(\frac{4Xk}{u^2}\right)e(Mk/u).
\tag{2.10}
\]

If \(A=\mathcal R+\mathcal E\), where \(\mathcal E\) is defined by the exact difference between (2.7) and (2.10), then the majorized quadratic form is exactly

\[
Q_T(A)=Q_T(\mathcal R)
+2\Re B_T(\mathcal R,\mathcal E)+Q_T(\mathcal E).
\tag{2.11}
\]

Only the sum in (2.11) is endpoint-complete after stationary decomposition.

## 3. Proof and derivation

### 3.1 Exact lower bound by root-of-unity quadrature

Let \(T\) have degree at most \(N-1\). Since no nonzero Fourier frequency in its support is divisible by \(N\),

\[
t_0=\frac1N\sum_{\nu=0}^{N-1}T(\nu/N).
\tag{3.1}
\]

If \(T\geq F_H\), then

\[
t_0\geq\frac1N\sum_{\nu=0}^{N-1}|D_H(\nu/N)|^2.
\tag{3.2}
\]

At an \(N\)-th root of unity, fold the integers \(0,\ldots,H-1\) by their residue class modulo \(N\). The first \(s\) classes occur \(m+1\) times and the other \(N-s\) classes occur \(m\) times. Discrete Parseval therefore gives

\[
\frac1N\sum_{\nu=0}^{N-1}|D_H(\nu/N)|^2
=\sum_{j=0}^{N-1}n_j^2
=s(m+1)^2+(N-s)m^2
=Nm^2+(2m+1)s.
\tag{3.3}
\]

This proves the lower bound in (2.1). The optimizer \(P_{H,N}\) has precisely the folded coefficients \(n_j\), so its zeroth coefficient is the right side of (3.3). Exact optimality is reduced to the pointwise inequality \(|P_{H,N}|^2\geq|D_H|^2\).

### 3.2 Independent verification of the pointwise factorization

Put

\[
z=e(\alpha),\qquad w=z^N,\qquad v=z^s,
\]

\[
A_0=1-w,\qquad B_0=1-v,\qquad
G=\sum_{a=0}^{m-1}w^a,
\]

and

\[
S_m(\overline w)=
\sum_{j=1}^m\sum_{a=0}^{j-1}\overline w^{\,a}
=\sum_{a=0}^{m-1}(m-a)\overline w^{\,a}.
\]

For \(z\ne1\),

\[
(1-z)P_{H,N}=mA_0+B_0,
\qquad
(1-z)D_H=A_0G+w^mB_0.
\tag{3.4}
\]

Also

\[
m-G\overline w^{\,m}
=\sum_{j=1}^m(1-\overline w^{\,j})
=(1-\overline w)S_m(\overline w).
\tag{3.5}
\]

Expanding the difference of squares and using \(|w|=|v|=1\) gives

\[
\begin{aligned}
|1-z|^2(T^*_{H,N}-F_H)
&=|mA_0+B_0|^2-|A_0G+w^mB_0|^2\\
&=|A_0|^2\left(
m^2-|G|^2+2\Re S_m(\overline w)
-2\Re\{\overline vS_m(\overline w)\}
\right).
\end{aligned}
\tag{3.6}
\]

The auxiliary identity

\[
|G|^2
=m+2\Re\sum_{a=1}^{m-1}(m-a)w^a
\]

shows exactly that

\[
m^2-|G|^2+2\Re S_m(\overline w)=m(m+1).
\tag{3.7}
\]

Consequently the blind report's factorization is correct:

\[
\boxed{
|1-z|^2(T^*_{H,N}-F_H)
=|1-w|^2
\left(
m(m+1)-2\Re\{\overline vS_m(\overline w)\}
\right).
}
\tag{3.8}
\]

All coefficients in \(S_m\) are nonnegative and their sum is \(m(m+1)/2\). Hence

\[
2\Re\{\overline vS_m(\overline w)\}
\leq2|S_m(\overline w)|
\leq m(m+1),
\]

so (3.8) is nonnegative. At \(z=1\), both \(P_{H,N}(1)\) and \(D_H(1)\) equal \(H\), and the inequality follows there directly. At nontrivial \(N\)-th roots, \(1-w=0\), so equality holds, as required for equality in the sampling lower bound. This completes an independent proof of (2.1)--(2.3).

The edge cases are consistent:

- \(N=H\): \(m=1,s=0\), \(T^*=F_H\), and \(\mu_N(H)=H\);
- \(N=1\): \(m=H,s=0\), \(T^*=H^2\), and \(\mu_N(H)=H^2\);
- \(s=0\): \(P=mD_N\), and the inequality reduces to \(|D_m(z^N)|\leq m\).

### 3.3 What the exact theorem changes

For \(N<H\), (2.5) is positive, so the folded comparison is a genuinely strict, noninvertible inequality on some inputs. It is not merely the original Fejer identity and it is stronger than the nonsharp two-grid construction in the discovery report.

This does not contradict the rank-one internal-window obstruction. The false assertion would be a pointwise-in-\(n\) inequality

\[
\left|\sum_{a<H}A(n+a)\right|^2
\leq
\left|\sum_{j<N}n_jA(n+j)\right|^2
\quad\hbox{for every }n.
\]

The true statement (2.3) holds only after summing every translate \(n\); equivalently, it is a Toeplitz/multiplier PSD inequality.

The exact theorem sharpens, but does not change, the capacity no-go. If a lag-count-only strategy chooses

\[
N\leq \frac{H}{\Gamma_{\rm before}},
\qquad
\Gamma_{\rm before}=\min(H,Q),
\]

then even the optimal majorant has

\[
\Gamma_{\rm zeroth}
=\rho(H,N)
=\frac{Nm^2+(2m+1)s}{H}
\geq\frac HN
\geq\Gamma_{\rm before}.
\tag{3.9}
\]

If \(N\leq HX^{-\eta}\), this is at least \(X^\eta\); if \(N\leq H^{1-\sigma}\), it is at least \(H^\sigma\). No fixed \(X^\varepsilon\) allowance for every \(\varepsilon>0\) absorbs either fixed-power loss. Taking moduli of the folded lags at their natural diagonal scale uses (2.6) and returns the full factor \(H\).

Accordingly the close label remains majorant_no_go, but its correct wording is:

> An optimal strict one-sided contraction exists and is endpoint-exact. It cannot, by diagonal, positive-row, or lag-count-only bookkeeping, have both fixed-power bandwidth gain and target-safe mass. A new signed actual-family estimate could still control its right side.

The discovery two-grid majorant remains valid but is superseded as an extremizer: its zeroth coefficient \((9\pi^2/2)H^2/N\) is larger than the exact optimum (2.1).

### 3.4 Exact primitive-character Poisson constant

For a smooth compactly supported \(g\) on the positive line, extended by zero, split the integer sum into residue classes modulo \(4\). Ordinary Poisson gives

\[
\sum_{n\in\mathbb Z}\chi_4(n)g(n)
=\frac14\sum_{u\in\mathbb Z}
\left(\sum_{a\bmod4}\chi_4(a)e(au/4)\right)
\widehat g(u/4).
\tag{3.10}
\]

The Gauss sum is

\[
\sum_{a\bmod4}\chi_4(a)e(au/4)
=
\begin{cases}
2i\,\chi_4(u),&u\ {\rm odd},\\
0,&u\ {\rm even}.
\end{cases}
\tag{3.11}
\]

Thus

\[
\sum_n\chi_4(n)g(n)
=\frac{i}{2}\sum_{u\ {\rm odd}}\chi_4(u)
\int_{\mathbb R}g(x)e(-ux/4)\,dx.
\tag{3.12}
\]

Taking \(g(x)=f_k(x)e(\sqrt{Mkx})\) proves (2.7)--(2.8), including the sign \(-ux/4\) and the factor \(i/2\). No character conjugation is missing because \(\chi_4\) is real.

### 3.5 Stationary coefficient and profile

For \(u>0\), let

\[
\phi_u(x)=\sqrt{Mkx}-\frac{ux}{4}.
\]

Then

\[
x_*=\frac{4Mk}{u^2},\qquad
\phi_u(x_*)=\frac{Mk}{u},\qquad
\phi_u''(x_*)=-\frac{u^3}{32Mk}.
\tag{3.13}
\]

With the convention \(e(t)=e^{2\pi it}\), a negative nondegenerate saddle contributes \(e(-1/8)|\phi''(x_*)|^{-1/2}\). The amplitude and curvature factors are

\[
f_k(x_*)
=2^{-3/2}(Mk)^{-3/4}u^{3/2}
W\!\left(\frac{X}{Du}\right)
q_L\!\left(\frac{4Xk}{u^2}\right),
\]

\[
|\phi_u''(x_*)|^{-1/2}
=2^{5/2}(Mk)^{1/2}u^{-3/2}.
\]

Their product is

\[
2(Mk)^{-1/4}
W\!\left(\frac{X}{Du}\right)
q_L\!\left(\frac{4Xk}{u^2}\right),
\]

which proves (2.9). Multiplying by the prefactor in (2.7) gives

\[
\frac{i}{2}e(-1/8)M^{1/4}k^{-3/4}
\cdot2e(-1/8)(Mk)^{-1/4}
=i\,e(-1/4)\,k^{-1}
=k^{-1}.
\tag{3.14}
\]

Thus the discovery report's absence of a residual \(2\), \(4\), \(i\), \(M\), or \(u\) factor in (3.9) is correct.

### 3.6 Reciprocal Gram and endpoint scope

With

\[
R_r(\mathcal R)=\sum_k\mathcal R(k+r)\overline{\mathcal R(k)},
\]

and the stated Fourier convention,

\[
Q_T(\mathcal R)
=C_H\sum_{|r|<N}t_{-r}R_r(\mathcal R).
\]

Substitution of (2.10) gives

\[
\begin{aligned}
Q_T(\mathcal R)
=C_H\sum_{|r|<N}t_{-r}
\sum_{u,v>0\ {\rm odd}}&
\chi_4(u)\chi_4(v)
W\!\left(\frac{X}{Du}\right)
\overline{W\!\left(\frac{X}{Dv}\right)}
\\
\times\sum_k&
\frac{
q_L(4X(k+r)/u^2)
\overline{q_L(4Xk/v^2)}
}{(k+r)k}
e\!\left(\frac{M(k+r)}u-\frac{Mk}v\right).
\end{aligned}
\tag{3.15}
\]

This confirms every displayed feature of discovery equation (3.10): \(t_{-r}\), \(k+r\) in the first row, conjugation in the second row, denominator \((k+r)k\), character product, and reciprocal phase.

The scope correction is essential. Equations (2.7)--(2.8) are exact and endpoint-complete because they retain the full integrals for all odd \(u\), including nonstationary \(u<0\). Equation (3.15) is only the principal--principal component after a stationary decomposition. To recover the exact majorized energy one must also retain

\[
\mathcal P_T
=2\Re B_T(\mathcal R,\mathcal E)+Q_T(\mathcal E),
\tag{3.16}
\]

where \(\mathcal E\) contains all stationary remainders, nonstationary signs, support entries/exits, and transition regimes. Defining \(\mathcal E\) by subtraction makes (3.16) an exact identity, but supplies no estimate. In particular:

- the full exact integral Poisson formula has zero endpoint error;
- the principal row and principal Gram do not, by themselves, constitute an endpoint-complete asymptotic formula;
- the discovery report does not prove a uniform stationary remainder, a weighted \(\mathcal P_T\) bound, or permission to reuse the old Fejer endpoint ledger under the new coefficients;
- exact Poisson remains invertible and supplies no additional power beyond the already noninvertible folded majorant.

### 3.7 C0 and TeX integrity scan

A byte-level read-only scan found no unexpected C0 or DEL bytes in either sibling report: no NUL, tab, lone carriage return, backspace, form feed, escape, or DEL was present; both files use ordinary LF line endings.

Both reports nevertheless have pervasive TeX delimiter corruption.

- In blind_bandlimited_quadratic_majorant_feasibility.md, hundreds of intended inline expressions appear as plain parentheses, for example “Let (0\leq \Delta\leq H-1)” and repeated symbols such as “(T)” and “(q)”. A scan found only 28 surviving inline opening delimiters against 283 TeX-like plain-parenthesis starts.
- In actual_character_fejer_majorant_attack.md, the same corruption is more extensive: only 7 surviving inline opening delimiters against 351 TeX-like plain-parenthesis starts. There is also an unmatched closing delimiter in the table at line 173, after the fragment “(H\mathcal D_0”.

The numerical counts are lexical diagnostics rather than mathematical claims, but the displayed examples are conclusive. Display-math blocks are largely intact, so the arguments remain auditable. The sibling reports should not be treated as render-clean artifacts until their inline delimiters are repaired and rechecked by their owners. This review does not edit them.

## 4. First doubtful or unproved step

There is no doubtful step in the finite extremal theorem (2.1)--(2.6). The root-of-unity lower bound, the folded construction, and the pointwise factorization all check exactly.

There is also no normalization defect in the exact character-Poisson identity (2.7)--(2.8), and the interior stationary coefficient and profiles in (2.9)--(2.10) are correct.

The first unproved analytic step is the passage from the exact Poisson integrals to a useful, uniform endpoint-complete stationary estimate. The discovery report defines the difference as a remainder but does not bound it. After insertion into the majorized form, the missing theorem is a uniform estimate for

\[
Q_T(\mathcal R)+\mathcal P_T
\]

that simultaneously:

- retains the signed \(\chi_4(u)\chi_4(v)\) Gram before every modulus;
- offsets the exact zeroth price \(\rho(H,N)\);
- controls every \(r\)-weighted principal--remainder and remainder--remainder term;
- treats support entry, exit, nonstationary, and saddle-transition regimes with the folded coefficients \(t_r\); and
- remains in the literal flat-smooth strict-UNBAL owner.

No sibling report proves this. Consequently neither the exact optimizer nor exact character Poisson proves the target energy bound. The term “endpoint-complete reciprocal Gram principal survivor” must be read as “principal Gram inside an endpoint-complete Gram-plus-remainder identity,” not as a closed endpoint theorem for (3.15) alone.

## 5. Control tests and outcomes

| Control | Outcome | Consequence |
|---|---|---|
| Root-of-unity quadrature | **Pass exactly** | Every degree-\((N-1)\) majorant has \(t_0\geq Nm^2+(2m+1)s\). |
| Folded optimizer zeroth coefficient | **Pass exactly** | \(P=mD_N+D_s\) has coefficient vector \((m+1)^s,m^{N-s}\) and squared mass \(\mu_N(H)\). |
| Pointwise factorization identity | **Pass exactly** | Equation (3.8) follows algebraically; the bracket is nonnegative by the coefficient sum of \(S_m\). |
| Edge cases \(N=H\), \(N=1\), \(s=0\) | **Pass** | They give respectively \(F_H\), \(H^2\), and \(|D_m(z^N)|\leq m\). |
| Global versus per-block physical order | **Pass with correction** | The folded inequality holds after summing all \(n\); it does not contradict the rank-one falsifier for a single block. |
| Exact capacity and close label | **No label change** | \(\rho=\mu_N(H)/H\geq H/N\); fixed-power contraction remains above target under diagonal/lag-count closure. |
| Folded Fourier \(\ell^1\) mass | **Pass exactly** | All \(t_r^*\geq0\) and \(\sum|t_r^*|=H^2\), so natural-scale lagwise modulus returns factor \(H\). |
| Primitive \(\chi_4\)-Poisson constant | **Pass exactly** | \(\tau(\chi_4)=2i\) gives \(i/2\), odd dual frequencies, and phase \(-ux/4\). |
| Stationary saddle and coefficient | **Pass for the interior main term** | \(x_*=4Mk/u^2\), \(\phi(x_*)=Mk/u\), \(\phi''=-u^3/(32Mk)\), and the coefficient is \(2e(-1/8)(Mk)^{-1/4}\). |
| Profile transport | **Pass** | The profiles become \(W(X/(Du))q_L(4Xk/u^2)\), with \(u\asymp X/D\) and \(k\asymp K\) on the principal support. |
| Reciprocal Gram indices and conjugations | **Pass** | Discovery equation (3.10) matches direct substitution of the principal row. |
| Endpoint/transition completeness | **Fail for the principal Gram alone; pass for the exact integral identity** | \(\mathcal P_T\) must contain and control every omitted term; no such bound is supplied. |
| C0 scan | **Pass** | No unexpected control bytes or DEL were found. |
| TeX/render scan | **Fail** | Both siblings have widespread missing inline delimiters; discovery also has an unmatched closing delimiter at line 173. |

All checks were analytic or exact lexical checks. No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This review used:

- rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reports/blind_bandlimited_quadratic_majorant_feasibility.md
- rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reports/actual_character_fejer_majorant_attack.md
- rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/reports/majorant_cross_term_hostile_audit.md
- rounds/codex-managed/m9-m2-unbalanced-one-sided-majorant-gate/blind_statement.md
- protocol.md

The finite extremal proof, character Gauss sum, stationary coefficient, reciprocal Gram, and byte/TeX checks were independently reproduced in this review. No web source, external theorem lookup, numerical computation, symbolic algebra system, or shared-state file was used or changed.

## 7. Recommended state effect

**Recommended state effect: promote the exact finite theorem, retain the scoped no-go, and revise the Poisson endpoint wording.**

1. **Promote as candidate exact finite evidence** (2.1)--(2.6): the optimal zeroth coefficient, the folded optimizer, its pointwise factorization, the global endpoint-exact physical inequality, and the exact \(\ell^1\) mass \(H^2\).
2. **Supersede, but do not mark false,** the discovery report's two-grid upper bound as the extremal construction. It remains a valid nonsharp majorant.
3. **Retain the close label majorant_no_go.** Clarify that the no-go is not nonexistence of a contracted majorant: the optimizer provides one. The no-go is the exact bandwidth--mass tradeoff for every diagonal, positive-row, lag-count-only, or natural-scale lagwise-absolute closure.
4. **Promote the normalization identities** (2.7)--(2.10) and the principal Gram (3.15) as formal candidate identities, subject to the frozen smooth zero-extension hypotheses.
5. **Do not promote endpoint completeness for the principal Gram or any target bound.** Only the exact integral Poisson formula, or the full identity \(Q_T(\mathcal R)+\mathcal P_T\), is endpoint-complete. A uniform \(\mathcal P_T\) estimate and the signed actual-character Gram bound remain open.
6. **Require owner repair of both sibling report renderings** before they are used as clean archival evidence. The issue is TeX delimiter loss, not hidden C0 corruption; this review intentionally leaves both siblings untouched.

No shared proof state, synthesis, sibling report, or downstream claim should be edited on the strength of the unbounded stationary remainder.
