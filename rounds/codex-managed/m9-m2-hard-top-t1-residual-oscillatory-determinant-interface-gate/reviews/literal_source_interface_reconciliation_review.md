# Literal/source-interface reconciliation review

## 1. Result

**Review verdict: revise.**

The claimant's principal conclusion survives in a narrower and cleaner form: the exact finite endpoint-kernel identity is valid, the polylogarithmic-shift sector is target-safe, and neither Grimmelt--Merikoski source presently proves the literal K17a target. The claimant must nevertheless be revised before its source and power discussion can be retained.

Four repairs are mandatory.

1. The assertion that there is no character-forced principal-main-term vanishing is false for the bare coefficient
   \[
   \alpha_{\mathrm{bare}}(M)=\chi_4(a)\chi_4(b).
   \]
   Its finite orbit coefficient vanishes exactly for every \(k=2^v\). A selector-dependent automorphic coefficient has a different orbit sum, for which no vanishing is automatic.

2. The top \(k=2,\ r\asymp L\) literal incidence stratum is not proved nonempty or densely populated. Its norm and power calculations are legitimate only as a conditional source-scale stress test.

3. The target-sized \(\mathcal R_0^{\mathrm{src}}\) base leaves no multiplicative slack, but it does not justify demanding
   \(\mathcal K_+^{1/2}\ll J^{-C_*}X^\varepsilon\). The source exposes neither the exponent \(C_*\) nor any mechanism giving \(J\)-decay in \(\mathcal K_+\). The correct audit keeps \(\mathcal K_+\), \(\delta^{-O(1)}\), and the additional \(\mathcal R_2^{\mathrm{src}}\) loss as separate unproved inputs. Under the claimant's optimistic dense-block assumptions, \(\mathcal R_2^{\mathrm{src}}\) gives the source bound \(L^{2+\theta_4+\varepsilon}\), not \(L^2X^\varepsilon\), unless one additionally knows \(\theta_4=0\).

4. Grimmelt--Merikoski Part I formally permits complex oscillatory \(f\in C^{10}_\delta\); it simply charges all frequency through the derivative seminorms and \(\delta^{-O(1)}\). Moreover, the claimant's equation (167.48) incorrectly equates a raw literal kernel form with a discrepancy form. An exact Part-I interface first needs an embedding of endpoints into \(G=\mathrm{SL}_2(\mathbb R)\), an identity for the raw automorphic kernel \(\mathcal K F\), and then a separate principal-component calculation.

These repairs do not reopen the direct source call. The first source failure remains the absence of an admissible selector-dependent coefficient or a target-safe common smooth representation; the determinant-dependent phase supplies an independent one-common-\(f\) failure.

## 2. Exact statements and hypotheses under review

### 2.1 Exact finite claimant statements

For
\[
 x=(d,m),\qquad y=(d',m'),\qquad n(x)=dm,\qquad n(y)=d'm',
\]
the claimant defines
\[
 u_L(x)=\chi_4(d)\lambda_{dm}(d)e(J\sqrt{dm})
\]
and the real directed kernel
\[
\begin{aligned}
T_{R_0,\gamma}(y,x)
={}&\left(1-\frac{n(y)-n(x)}{R_0}\right)
\mathbf 1_{0<n(y)-n(x)<R_0}
\mathbf 1_{2\mid n(y)-n(x)}\\
&\times\mathbf 1_{(d'-d)(m'-m)<0}
\mathbf 1_{(d,d')<\gamma L}.
\end{aligned}
\]
The claimed exact identity is
\[
 \mathfrak C^{\mathrm{rem}}_{R_0,2,\mathrm{opp},g<\gamma L}
 =\langle T_{R_0,\gamma}u_L,u_L\rangle.
\tag{R.1}
\]

For each fixed \(B>0\), the restricted shift endpoint is
\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^B\rfloor\},
\]
and the claimant asserts
\[
 \left|\mathfrak C^{\mathrm{rem}}_{r\leq R_{\log}}\right|
 \ll_{\varepsilon,B}L^2X^\varepsilon.
\tag{R.2}
\]

### 2.2 Grimmelt--Merikoski 2024

The exact source is Grimmelt--Merikoski, arXiv:2404.08502v2, Theorem 10.1. The literal determinant map
\[
 M=\begin{pmatrix}a&b\\c&d_0\end{pmatrix}
  =\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
 \qquad \det M=r=hk,
\]
uses
\[
 q_1=4,\qquad q_2=1,\qquad q=4,\qquad
 k=2^{v_2(r)},\qquad h\ \mathrm{odd}.
\]
The conditions
\[
 (h,kq)=1,\qquad (a,c,k)=(b,d_0,k)=1
\]
pass because \(d,d'\) are odd. These are only the determinant and column-primitivity hypotheses.

A literal theorem call additionally requires:

- a Dirichlet character \(\chi\) of modulus dividing \(q=4\), multiplicative determinant coefficients \(\xi_h\), and \(\alpha\in\mathcal A(4,1,\chi,\xi)\), satisfying the exact left-automorphy law;
- \(A,C,D,\delta,\eta>0\), \(AD>\delta\), and
  \[
  Z=\max\{A^{\pm1},C^{\pm1},D^{\pm1},\delta^{-1}\};
  \]
- \(H,K\geq1\), \(HK\leq(AD)^{1+\eta}\), with \(\beta_h\) supported on \(|h|\in[H,2H]\), \(\gamma_k\) supported on \(|k|\in[K,2K]\), and the determinant sum restricted by \((h,kq)=1\);
- one common
  \[
  f\in C^7_\delta
  \left(A/\sqrt{HK},C/\sqrt{HK},D/\sqrt{HK}\right);
  \]
- the orbit-correlation hypothesis (10.2), with its absolute value placed around the inner orbit sum and a proved parameter \(\mathcal K_+\);
- the principal-character main term; and
- the full error
  \[
  Z^{O(\eta)}\delta^{-O(1)}(AD)^{1/2}
  \|\beta\xi\|_2\mathcal K_+^{1/2}
  \{\mathcal R_0+\min(\mathcal R_1,\mathcal R_2)\}.
\tag{R.3}
  \]

The project selector, sharp boundaries, endpoints, and square-root phase are not supplied by the determinant and gcd hypotheses.

### 2.3 Grimmelt--Merikoski 2025 Part I

Theorem 1.1 takes a congruence subgroup \(\Gamma\), a character \(\chi\), compactly supported linear functionals \(\alpha_1,\alpha_2\in\mathcal L_c(G)\), and
\[
 f\in C^{10}_\delta(A,C,D),\qquad F:G\to\mathbb C,\qquad F(M)=f(a,c,d_0).
\]
Here \(A,C,D,\delta>0\), \(AD>\delta\), \(R_1=A/C\), \(R_2=D/C\), and \(X_0,X_1,X_2\geq1\) obey \(X_0X_1X_2\geq AD\). It imposes no reality, positivity, or nonoscillation hypothesis on \(f\). Its bound is
\[
 \langle\alpha_1\mid\Delta F\mid\alpha_2\rangle
 \ll \delta^{-O(1)}(AD)^{1/2+o(1)}X_0^\theta
 \sqrt{
 \langle\alpha_1\mid\Delta k_{X_1^2,R_1}\mid\alpha_1\rangle
 \langle\alpha_2\mid\Delta k_{X_2^2,R_2}\mid\alpha_2\rangle},
\]
where the two displayed discrepancy-kernel forms are nonnegative. The vertical bars delimit the sesquilinear form; they are not an operator absolute value. The raw automorphic kernel and discrepancy satisfy
\[
 \Delta F=\mathcal K_{\Gamma,\chi}F
 -\frac{\mathbf 1_{\chi\ \mathrm{principal}}}{|\Gamma\backslash G|}
 \int_G F(g)\,dg.
\tag{R.4}
\]
Corollary 1.5 does not create left invariance: it assumes a left-\(\Gamma\)-invariant matrix set and coefficient and still requires \(f\in C^{10}_\delta\).

## 3. Proof and derivation of the review findings

### 3.1 The finite endpoint-kernel identity passes

With the claimant's convention,
\[
\begin{aligned}
\langle Tu_L,u_L\rangle
&=\sum_{x,y}T(y,x)u_L(y)\overline{u_L(x)}\\
&=\sum_{x=(d,m),\,y=(d',m')}T(y,x)
\chi_4(d')\chi_4(d)
\lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}
e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right).
\end{aligned}
\]
Here \(\chi_4(d)\) is real for odd \(d\). The five kernel factors impose the exact Fejer weight, positive even shift, opposing displacement, and low top-row gcd. Membership of both endpoints in \(\mathcal E_L\) imposes the literal shell, residual support, and zero extension. The ordered pair \((x,y)\) determines the four matrix entries, so no quotient or multiplicity is lost. Thus (R.1), the row and column degree bounds, and the Schur capacity \(L^3X^\varepsilon\) are correct finite statements.

This identity is not yet a Grimmelt--Merikoski kernel identity. It is an arbitrary finite directed matrix on \(\mathcal E_L\); the source kernel has the much more restrictive relative-orbit form.

### 3.2 The first 2024 source failure is correctly located

The raw character
\[
 \alpha_{\mathrm{bare}}(M)=\chi_4(a)\chi_4(b)
\]
belongs to the relevant source character skeleton, with induced principal character and \(\xi=1\). The literal multiplier
\[
 \lambda_{ad_0}(a)\overline{\lambda_{bc}(b)}
 \mathbf 1_{(a-b)(d_0-c)<0}
 \mathbf 1_{(a,b)<\gamma L}
\]
has no proved left-automorphic realization. If placed in \(f\), its arithmetic jumps and sharp endpoints are not one \(C^7_\delta\) function. The low-gcd indicator itself has an explicit left-orbit counterexample for \(0<\gamma<1/2\); for arbitrary \(\gamma\), the residual selector still has no verified automorphy or target-safe interpolation.

The phase is an independent obstruction. Normalizing by \(\sqrt r\) gives
\[
 \Phi_r(x,z)=J\sqrt r
 \left(\sqrt{xz}-\sqrt{xz-1}\right).
\]
For \(J\ne0\), two distinct values of \(r\) give nonproportional functions of \((x,z)\). Hence a determinant coefficient times one common \(f\) cannot represent the exact phase. Applying the theorem separately for each \(r\) replaces the one outer real part by an absolute error sum, for which the source supplies no target-size bound.

### 3.3 The principal main term must be reconciled, not declared nonzero

The claimant is correct only that the induced theorem character is principal, so the indicator selecting the source main term does not vanish. The finite orbit coefficient nevertheless cancels for the bare character.

For \(T=\Gamma_2(4,1)\backslash\mathrm{SL}_2(\mathbb Z)\), use the top-row representatives
\[
 (x,1)\quad(x=0,1,2,3),\qquad (1,0),\ (1,2).
\]
For
\[
 T_{1,k}=\mathrm{SL}_2(\mathbb Z)\backslash\mathcal M_{2,1,k},
\]
use
\[
 \sigma_b=\begin{pmatrix}1&b\\0&k\end{pmatrix},
 \qquad b\bmod k,\qquad (b,k)=1,
\]
with \(b=0\) for \(k=1\). If \(\tau\) has top row \((x,y)\), then \(\tau\sigma_b\) has top row \((x,xb+yk)\). Consequently
\[
 \sum_{\tau\in\Gamma\backslash\mathcal M_{2,1,k}}
 \alpha_{\mathrm{bare}}(\tau)=0
 \qquad(k=2^v):
\tag{R.5}
\]
for \(k=1\) the six terms sum to zero; for \(k=2\) the four \((x,1)\) terms contribute \(-2\) and the other two contribute \(+2\); and for \(4\mid k\), each odd \(b\) contributes \(4\chi_4(b)\), whose sum over units modulo \(k\) is zero.

Therefore the claimant must replace “no character-forced vanishing” by the following dichotomy:

- if \(\alpha=\alpha_{\mathrm{bare}}\) and every literal selector remains outside \(\alpha\), the source main term vanishes exactly by (R.5);
- if a selector-dependent automorphic factor is inserted into \(\alpha\), the finite orbit weights change and (R.5) no longer applies automatically; that new orbit sum must be recomputed or bounded.

The bare cancellation does not rescue the direct route because the necessary common smooth placement of the remaining selectors and variable-\(r\) phase is absent.

### 3.4 Correct restored-power ledger

The claimant's top-block calculation must first be made conditional. No argument in the report proves that literal K17a incidences with \(k=2\), \(r\asymp L\), Fejer weight bounded below, and \(\asymp L\) nonvanishing determinant coefficients exist. The correct introduction is: “On a hypothetical dense source block with these scales.”

On that conditional block, with \(A=C=D\asymp L\), \(H\asymp L/k\), and \(|\beta_h|\asymp1\) on \(\asymp H\) indices,
\[
 \|\beta\|_2\asymp H^{1/2},
 \qquad \mathcal R_0\asymp H^{1/2}.
\]
At fixed \(k=2\), the \(\mathcal R_0\) part of (R.3), before \(\delta^{-O(1)}\mathcal K_+^{1/2}\), is \(L^2\). This is a no-slack upper-bound ledger, not a lower bound for the literal sum or a proof that the block is populated.

The additional source term cannot be omitted. Under the optimistic auxiliary bound
\[
 \mathcal K_+^{1/2}\ll X^\varepsilon
\]
at fixed \(k=2\), the \(\mathcal R_2\) route gives
\[
 E_{H,2}\ll
 \delta^{-O(1)}L^{2+\theta_4}X^\varepsilon.
\tag{R.6}
\]
With only the published unconditional \(\theta_4\leq7/64\), substituting the available exponent does not yield the target form. If \(\theta_4=0\) were proved independently, this particular spectral power would disappear.

The phase contributes the source-input scale
\[
 \delta^{-1}\gtrsim_{\mathrm{cell}}1+\frac{|J|r}{L},
\]
which is \(\asymp1+|J|\) at \(r\asymp L\), while the theorem gives only \(\delta^{-O(1)}\). Its final exponent is not explicit.

Finally, \(\mathcal K_+\) is a separate absolute orbit-correlation hypothesis. Bounded \(\alpha\) does not prove it, and the phase in \(f\) does not generate \(J\)-decay in this parameter. It is algebraically true that a target-sized base would require the entire product of all losses to be \(X^\varepsilon\)-safe, but it is unsupported to promote this observation into the demanded estimate
\[
 \mathcal K_+^{1/2}\ll J^{-C_*}X^\varepsilon.
\]
The source does not expose \(C_*\) and supplies no negative-power \(\mathcal K_+\) mechanism. Equations (167.45)--(167.46) must be deleted or explicitly demoted to an unsupported hypothetical compensation, not listed as a missing theorem input.

### 3.5 Correct Part-I interface

The finite vector \(u_L\) is defined on \(\mathcal E_L\), whereas Part I takes functionals on \(G\). A literal application first needs an embedding
\[
 \iota:\mathcal E_L\longrightarrow G
\]
and the finite functional
\[
 \langle\varphi\rangle_{\alpha_u}
 =\sum_{x\in\mathcal E_L}u_L(x)\varphi(\iota(x)).
\]
It must then construct \(F\) such that, with the correct orientation,
\[
 (\mathcal K_{\Gamma,\chi}F)(\iota(x),\iota(y))
 =T_{R_0,\gamma}(y,x)
\tag{R.7}
\]
for every literal endpoint pair, with no extra relative-orbit pairs. No such \(\iota,F\) are given.

If (R.7) held, the raw literal form would be
\[
 \langle\alpha_u\mid\mathcal K F\mid\alpha_u\rangle
 =\langle T_{R_0,\gamma}u_L,u_L\rangle.
\]
The discrepancy form in the claimant's (167.48) differs by
\[
 \frac{\mathbf 1_{\chi\ \mathrm{principal}}}{|\Gamma\backslash G|}
 \left|\langle1\rangle_{\alpha_u}\right|^2
 \int_G F(g)\,dg.
\tag{R.8}
\]
Thus (167.48) is not the correct raw identity unless (R.8) is proved zero or explicitly absorbed.

Part I does allow complex oscillatory \(F\). Moving the square-root phase into it is formally legal but incurs the \(C^{10}_\delta\) derivative ledger and the paper's unspecified \(\delta^{-O(1)}\). Moving the phase and selectors into endpoint functionals avoids that particular derivative cost only after (R.7) is proved. Even then, Theorem 1.1 leaves two nonnegative discrepancy-kernel autocorrelations which have no K17a target-size bound.

### 3.6 The polylogarithmic-shift sector passes

For each fixed \(B\), absolute values, \(|\lambda_N(d)|\ll1\), and deletion of all restrictive selectors give
\[
\begin{aligned}
\left|\mathfrak C^{\mathrm{rem}}_{r\leq R_{\log}}\right|
&\leq
\sum_{\substack{r\leq R_{\log}\\2\mid r}}
\sum_N\tau(N)\tau(N+r)\\
&\ll_{\varepsilon,B}
(\log X)^B\,L^2X^\varepsilon
\ll_{\varepsilon,B}L^2X^{2\varepsilon}.
\end{aligned}
\]
Renaming \(2\varepsilon\) proves (R.2). The omitted condition \(N+r\in\mathcal I_L^{\mathrm{lit}}\) only decreases the sum. This is a valid owner-complete restricted-shift lemma.

Its scope must remain explicit. If \(R_0-1\leq(\log X)^B\), it covers the full shift interval. When \(L\) is a genuine power scale, it covers only \(X^{o(1)}\) shifts and gives no fixed-power fraction of the open \(r\asymp L\) range. It supplies no evidence that the claimant's hypothetical top \(k=2\) block is nonempty.

## 4. First doubtful or unproved step

For Grimmelt--Merikoski 2024, the first unproved step remains an exact, target-safe representation of the actual residual selector as either:

1. a coefficient satisfying the source left-automorphy law; or
2. a bounded-rank family of common \(C^7_\delta\) weights preserving the variable-\(r\) phase and the one outer real part.

After that would come the independent \(\mathcal K_+\), \(\mathcal R_2\), explicit seminorm, cell, boundary, endpoint, and completion obligations. The bare main term is not among these later obligations unless the coefficient is changed.

For Part I, the first missing step is the typed raw-kernel realization (R.7), including the endpoint embedding and exclusion of cross terms. It is followed by the principal component (R.8) and the two nonnegative discrepancy-kernel autocorrelation bounds.

## 5. Required controls and mandatory repairs

1. **Determinant and endpoint multiplicity — pass.** Retain (167.16), the ordered determinant dictionary, the outer real part, and the Schur capacity.

2. **2024 coefficient and smoothness class — pass as a no-go.** Retain the failure at the literal selector/common-\(f\) interface. Do not infer universal nonexistence of a new decomposition.

3. **Principal main term — mandatory repair.** Replace the statements in Sections 1, 3.5, 4, 5, and 7 that no forced zero exists. Insert the bare cancellation (R.5) and require recomputation only for selector-dependent \(\alpha\).

4. **Top-block existence — mandatory repair.** Delete “nonempty” from the claimant's line introducing (167.41). Mark (167.41)--(167.44) as a hypothetical dense-block source-scale test, not a fact about literal incidence support.

5. **Power and \(\mathcal K_+\) — mandatory repair.** Retain target-sized \(\mathcal R_0\) as a conditional no-slack base; add the \(\mathcal R_2\) bound (R.6), keep \(\delta^{-O(1)}\) and \(\mathcal K_+\) as separate unproved losses, and remove the demanded negative-power estimate (167.46).

6. **Part-I wording and identity — mandatory repair.** State that complex oscillatory \(f\) is formally allowed with \(C^{10}_\delta\) cost. Replace (167.48) by the raw identity (R.7) plus the principal correction (R.8), after defining the endpoint functional on \(G\).

7. **Part-I autocorrelations — pass as an open obligation.** They are nonnegative discrepancy-kernel forms, not a proved factor-\(L\) saving and not operator absolute values.

8. **Endpoints and polylog shifts — pass.** Retain the exact sharp endpoint kernel and (167.50), with fixed \(B\) and the restricted-shift scope stated above.

9. **Downstream scope — pass.** The route-scoped no-go does not close K17a, move to K26, or affect either exponent ledger.

No numerical control is needed or used.

## 6. Dependencies and exact artifacts used

This review used:

- protocol.md;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reports/literal_determinant_kernel_attack.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reports/oscillatory_source_power_hostile_audit.md.

Primary-source claims were checked against:

- Grimmelt--Merikoski, *Twisted correlations of the divisor function via discrete averages of \(\mathrm{SL}_2(\mathbb R)\) Poincaré series*, arXiv:2404.08502v2, Definition 3 and Theorem 10.1: [versioned HTML](https://arxiv.org/html/2404.08502v2), [versioned PDF](https://arxiv.org/pdf/2404.08502v2).
- Grimmelt--Merikoski, *Weighted averages of \(\mathrm{SL}_2(\mathbb R)\) automorphic kernel. Part I: non-oscillatory functions*, arXiv:2505.00489v2, Theorem 1.1, Definition 3, and Corollary 1.5: [versioned HTML](https://arxiv.org/html/2505.00489v2), [versioned PDF](https://arxiv.org/pdf/2505.00489v2).

The claimant's report and shared state were not edited.

## 7. Recommended state effect

**Revise.**

Retain as candidate evidence:

- the exact multiplicity-one determinant opening;
- the finite endpoint-kernel identity (167.16);
- its \(L^3X^\varepsilon\) Schur capacity;
- the scoped selector/common-phase direct-source no-go; and
- the fixed-\(B\) polylogarithmic-shift bound (167.50).

Reject or revise before any promotion:

- the claim that the bare principal main term has no character-forced zero;
- the assertion that the literal top \(k=2\) block is nonempty;
- the demanded negative-power \(\mathcal K_+\) estimate;
- the omission of the \(\mathcal R_2\) spectral loss; and
- the untyped discrepancy identity (167.48) and “nonoscillatory \(f\)” wording.

After those repairs, the terminal conclusion remains the narrow label
\[
 \text{\rm oscillatory\_determinant\_interface\_no\_go},
\]
with no K17a or downstream graph promotion.
