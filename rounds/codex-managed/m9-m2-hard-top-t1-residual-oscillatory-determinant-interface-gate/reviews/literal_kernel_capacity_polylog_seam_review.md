# Round 167 literal-kernel, capacity, and polylogarithmic-sector seam review

- Campaign: m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate
- Role: post-unmask seam reviewer
- Claimant artifact: reports/literal_determinant_kernel_attack.md
- Comparators: the accepted Round-165 Fejer kernel and the repaired statement-only blind report
- Status: review evidence only; no shared-state mutation is licensed

## 1. Result

**Verdict: REVISE the literal report before promoting its candidate evidence.**

The following four claims survive independent rederivation:

1. the ordered divisor-incidence to determinant-matrix map is multiplicity one, and its decomposition into free left orbits is multiplicity preserving, provided the orbit set and acting determinant-one group are defined as intended;
2. the endpoint-vector quadratic-form identity is exact and does not double-count the coefficient sums;
3. Schur's test gives an \(L X^\varepsilon\) operator-norm upper bound and hence the \(L^3X^\varepsilon\) positive capacity;
4. the complete sector \(r\le R_{\log}\) is owner-complete and target-safe after an explicit epsilon relabelling.

The source-power conclusion does **not** survive in its unconditional wording. Equations (167.41)--(167.46) assume not merely a nonempty \(k=2\), \(h\asymp L\) block, but \(\asymp L\) nonvanishing determinant weights of comparable size. Neither nonemptiness nor this density is proved for the literal selector. The displayed source error therefore has \(L^2\) base scale only conditionally. Likewise, the literal twist \(\chi_4(a)\chi_4(b)\) is not pointwise principal, and even a principal source channel would only permit a main term; it would not force the literal oscillatory main term to be nonzero.

The exact repair is to separate:

- unconditional algebraic evidence: determinant/orbit multiplicity, endpoint identity, Schur capacity, phase derivative, and the polylogarithmic strict sector;
- conditional source-model evidence: the \(L^2\) top-block base error, the required \(J^{-C_*}\) autocorrelation compensation, and any principal-main-term conclusion.

K17a remains open, and no parent or exponent status changes.

## 2. Exact statement and hypotheses

The reviewed literal aggregate is

\[
\mathfrak C^{\rm rem}_{R_0,2,\mathrm{opp},\,g<\gamma L}
=
\sum_{\substack{1\le r<R_0\\2\mid r}}
\left(1-\frac r{R_0}\right)
\sum_{\substack{d,d'\ \mathrm{odd},\ m,m'\ge1\\
d'm'-dm=r\\
(d'-d)(m'-m)<0\\
(d,d')<\gamma L}}
\chi_4(d')\chi_4(d)
\lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}
e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right),
\tag{2.1}
\]

with every literal shell, selector, parity branch, hard value, endpoint, and zero-extension restriction retained. The target is the one-sided bound

\[
\Re\mathfrak C^{\rm rem}_{R_0,2,\mathrm{opp},\,g<\gamma L}
\ll_{\gamma,\varepsilon}L^2X^\varepsilon,
\qquad R_0=\lceil L\rceil.
\tag{2.2}
\]

For exact agreement with the frozen Round-167 packet, the literal report should state \(0<\gamma<1\), rather than merely \(\gamma>0\). The accepted Round-165 high-gcd estimate works for each fixed positive \(\gamma\), so this is a statement-normalization repair, not a change to any derivation.

Define the endpoint incidence set

\[
\mathcal E_L=\{x=(d,m):d\ \mathrm{odd},\ dm\in\mathcal I_L^{\rm lit},
\ \lambda_{dm}(d)\ne0\},
\]

the product \(n(x)=dm\), and

\[
u_L(d,m)=\chi_4(d)\lambda_{dm}(d)e(J\sqrt{dm}).
\tag{2.3}
\]

For \(x=(d,m)\) and \(y=(d',m')\), let \(T(y,x)\) be the real directed kernel containing exactly the Fejer, positive even gap, opposing-displacement, and low-\(g\) indicators. The review checks the identity

\[
\mathfrak C^{\rm rem}_{R_0,2,\mathrm{opp},\,g<\gamma L}
=\langle Tu_L,u_L\rangle
\tag{2.4}
\]

under the claimant's convention

\[
(Tu)(x)=\sum_yT(y,x)u(y).
\]

For the source-power ledger, introduce the actual determinant-weight support size or mass explicitly. On the proposed \(k=2\), \(h\asymp L\) block, let

\[
S=\#\{h:\beta_h\xi_h\ne0\}
\]

in the unit-size model. The claimant's formulas imply an \(L^2\) base term only when \(S\asymp L\), not from nonemptiness \(S\ge1\).

## 3. Proof or derivation

### 3.1 Determinant and orbit multiplicity

Expanding the coefficient at \(N\) and \(N+r\) selects one ordered pair of divisors \(d\mid N\) and \(d'\mid N+r\). Put

\[
m=N/d,\qquad m'=(N+r)/d'.
\]

Then

\[
A=\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
\qquad \det A=d'm'-dm=r.
\tag{3.1}
\]

Conversely, reading the four entries of any literal matrix in (3.1) recovers

\[
N=dm,\qquad N+r=d'm',\qquad r=d'm'-dm
\]

and the same ordered divisor pair. No transpose, sign, divisor-order, or projective quotient occurs. The incidence-matrix map is therefore a bijection.

The factorization

\[
r=hk,\qquad k=2^{v_2(r)},\qquad h\ \mathrm{odd}
\]

is unique. If \(\Gamma\le\mathrm{SL}_2(\mathbb Z)\) acts on the left, it preserves the determinant. For \(r\ne0\), a matrix \(A\) is invertible over \(\mathbb Q\); hence \(\gamma A=A\) implies \(\gamma=I\). The action is free. Once one representative is chosen per orbit, every literal matrix has a unique pair consisting of its orbit and the unique \(\gamma\) carrying the representative to it. The orbit opening is therefore multiplicity preserving even though the literal subset is not orbit invariant.

The claimant should define \(M_{2,h,k}(\mathbb Z)\) explicitly as the intended determinant-\(hk\) matrix set and state \(\Gamma\le\mathrm{SL}_2(\mathbb Z)\). Subject to that notational repair, equations (167.20)--(167.24) pass.

### 3.2 Endpoint-vector quadratic-form identity

Substituting (2.3) gives

\[
\begin{aligned}
u_L(y)\overline{u_L(x)}
={}&\chi_4(d')\chi_4(d)
\lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}\\
&\times e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right).
\end{aligned}
\tag{3.2}
\]

Multiplication by \(T(y,x)\) adds exactly the Fejer weight and the four cross-endpoint restrictions. Summing over ordered \(x,y\) gives (2.1), proving (2.4).

There is no double counting. Several endpoint indices \(x=(d,m)\) can share the same product \(N=dm\), but this is exactly the divisor sum in \(c_N^{\rm rem}\). Pairing all such \(x\) with all endpoint indices \(y\) above \(N+r\) reproduces the intended double divisor sum once. The endpoint vector contains individual divisor contributions, not a second copy of the already-summed coefficient \(c_N^{\rm rem}\).

This distinction also explains why

\[
\|u_L\|_2^2
=\sum_N\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
|\lambda_N(d)|^2
\tag{3.3}
\]

is incidence energy, not the accepted coefficient energy

\[
D_L=\sum_N\left|\sum_{d\mid N}\chi_4(d)\lambda_N(d)\right|^2.
\]

The two quantities need not be equal because the latter contains cancellation among divisors. The claimant uses (3.3), so no invalid equality or hidden duplication occurs.

### 3.3 Schur degree and capacity

Fix \(x\) and a gap \(r\). The product of \(y\) is forced to be \(n(x)+r\). Each divisor \(d'\mid n(x)+r\) determines at most one \(m'\), so there are at most \(\tau(n(x)+r)\) possible endpoints \(y\). All literal filters only delete choices, and the Fejer weight has modulus at most one. Therefore

\[
\sup_x\sum_y|T(y,x)|
\ll_\eta R_0X^\eta
\ll_\eta LX^\eta.
\tag{3.4}
\]

The same argument with \(x\) and \(y\) reversed gives the column-degree bound. Schur's test yields

\[
\|T\|_{2\to2}\ll_\eta LX^\eta.
\tag{3.5}
\]

Since the shell contains \(O(L^2)\) products and \(|\lambda_N(d)|\ll1\),

\[
\|u_L\|_2^2
\ll_\eta\sum_{N\in\mathcal I_L^{\rm lit}}\tau(N)
\ll_\eta L^2X^\eta.
\tag{3.6}
\]

Combining (3.5) and (3.6), and taking the divisor-bound exponents small enough in terms of the final requested \(\varepsilon\), gives

\[
|\langle Tu_L,u_L\rangle|
\le\|T\|_{2\to2}\|u_L\|_2^2
\ll_\varepsilon L^3X^\varepsilon.
\tag{3.7}
\]

Thus the degree and Schur ledger are correct. The result is an upper capacity, not a lower bound or a proof that the literal form attains size \(L^3\).

### 3.4 Polylogarithmic-shift sector

Let

\[
R_{\log}=\min\{R_0-1,\lfloor(\log X)^B\rfloor\},
\qquad B>0\ \mathrm{fixed}.
\]

Taking one modulus outside the complete restricted sector and using \(|\lambda|\ll1\) gives

\[
\left|\mathfrak C^{\rm rem}_{r\le R_{\log}}\right|
\le
\sum_{\substack{r\le R_{\log}\\2\mid r}}
\sum_{N\in\mathcal I_L^{\rm lit}}
\tau(N)\tau(N+r).
\tag{3.8}
\]

The bound is owner-complete: every divisor incidence for every selected small shift is present before the majorization, while squarefree, selector, parity, opposing-displacement, low-\(g\), endpoint, and Fejer restrictions only delete terms or contribute weights of modulus at most one.

For an explicit epsilon relabelling, fix the desired final \(\varepsilon>0\). Since \(N,N+r\ll L^2+L\ll X\), use

\[
\tau(n)\ll_{\varepsilon}X^{\varepsilon/4}
\]

for both divisor factors, and

\[
(\log X)^B\ll_{\varepsilon,B}X^{\varepsilon/2}.
\]

There are \(O(L^2)\) possible \(N\). Equation (3.8) then gives

\[
\left|\mathfrak C^{\rm rem}_{r\le R_{\log}}\right|
\ll_{\varepsilon,B}L^2X^\varepsilon.
\tag{3.9}
\]

This proves the strict sector exactly. It controls only \(X^{o(1)}\) shifts at a genuine power-scale \(L\), so it does not close K17a or justify any source claim on \(r\asymp L\).

### 3.5 Source-power claims

The derivative calculation is correct. For

\[
\Phi_r(a,d_0)=J\{\sqrt{ad_0}-\sqrt{ad_0-r}\},
\]

one has

\[
\partial_a\Phi_r
=-\frac{Jd_0r}
{2\sqrt{ad_0}\sqrt{ad_0-r}
\{\sqrt{ad_0}+\sqrt{ad_0-r}\}},
\]

and hence, on entries of size \(L\),

\[
L|\partial_a\Phi_r|+L|\partial_{d_0}\Phi_r|
\asymp \frac{Jr}{L}.
\tag{3.10}
\]

Thus any implementation that absorbs the phase into a smooth amplitude and pays an uncompensated fixed positive power of the corresponding seminorm has a genuine restored-power problem. This algebraic conclusion does not require the source theorem.

The claimed \(L^2\) source base error is conditional. From the displayed formula

\[
\mathcal R_0^{\rm src}
=
\frac{\|\beta\xi\|_1\mathsf A^{1/2}}
{\|\beta\xi\|_2q_1^{1/2}\mathsf C^{1/2}},
\]

the compulsory branch before \(\delta\) and \(\mathcal K_+\) simplifies on
\(\mathsf A,\mathsf C,\mathsf D\asymp L\) to

\[
(\mathsf A\mathsf D)^{1/2}
\|\beta\xi\|_2\mathcal R_0^{\rm src}
\asymp L\|\beta\xi\|_1.
\tag{3.11}
\]

For \(S\) unit-size nonzero \(h\)-weights this is \(LS\), not automatically \(L^2\). Equation (167.44) follows only under the additional hypothesis \(S\asymp L\), equivalently the two norm assumptions in (167.42). The literal report proves neither that the \(k=2,\ h\asymp L\) sector is nonempty nor that it contains \(\asymp L\) nonvanishing comparable weights. Arithmetic values \(r=2h\) exist, but the literal selector, shell, opposing sector, and low-\(g\) restriction may delete their incidences. Therefore:

- the \(L^2\) base error is a dense-block model or capacity calculation;
- the requirement \(\mathcal K_+^{1/2}\ll J^{-C_*}X^\varepsilon\) is conditional on that dense block, on a genuinely positive seminorm exponent \(C_*\), and on no other source saving;
- neither statement is an unconditional obstruction for the literal aggregate.

The phase-seminorm issue can be stated without assuming a top block. For any nonempty even shift \(r\ge2\), the frozen range \(L\ll H\le J^{1/2}\) gives

\[
1+\frac{Jr}{L}\gg J^{1/2}.
\tag{3.12}
\]

Hence a fixed positive, uncompensated polynomial seminorm loss is not an \(X^\varepsilon\) loss. This does not determine the source base term or rule out compensating oscillatory decay.

The main-term wording also needs repair. From the literal formulas,

\[
\chi_4(a)\chi_4(b)=\chi_4(ab)
\]

is not pointwise principal; for example, \(a\equiv1\pmod4\) and \(b\equiv3\pmod4\) give product \(-1\). Any assertion that the relevant source channel is \(\chi_4^2\) uses a source-specific character pairing not derived in the displayed literal formulas. Even if that source pairing is principal, it only removes a nonprincipal-character automatic vanishing condition. It does not force the selector- and phase-weighted main term to be nonzero. The dimensional calculation around (167.47) is correctly described as capacity, not a lower bound.

Accordingly, replace “the principal-character main term is present” and “the character is principal, so the source main term must also be estimated” by:

> Under the proposed source character identification, a principal-channel main-term term may occur and is not automatically removed by character orthogonality. Its literal value may still vanish; no nonzero lower bound or target-size estimate has been proved.

The 2025 Part-I positive-autocorrelation assertions cannot be independently verified from a theorem formula displayed in the literal report. They may remain source-audit evidence, but this seam review does not license them as an internally derived power conclusion.

## 4. First doubtful or unproved step

For the exact algebraic kernel, the first remaining analytic gap is the same selector-aware signed cancellation identified in both reports: neither the determinant dictionary nor Schur control saves the missing factor \(L\).

For the source-power argument, the first exact unproved step occurs earlier than (167.44): prove an owner-complete, literal nonemptiness and density statement for the proposed \(k=2,\ h\asymp L\) block, together with the actual determinant-weight norm estimates

\[
\|\beta\xi\|_1\asymp L,\qquad
\|\beta\xi\|_2\asymp L^{1/2}.
\]

Without those estimates, the displayed base error is \(L\|\beta\xi\|_1\), not \(L^2\). Even after such a density lemma, one must still verify the exact positive seminorm exponent, source coefficient class, \(\mathcal K_+\) norm, main term, boundaries, and completion. None is supplied by the algebraic endpoint identity.

## 5. Required controls and outcomes

| Seam | Outcome | Exact repair |
|---|---|---|
| Determinant-incidence multiplicity | **GREEN.** Ordered incidences and matrices are bijective | Define the ambient determinant matrix set explicitly |
| Left-orbit multiplicity | **GREEN, conditional on the intended group definition.** Nonzero determinant makes the left action free | State \(\Gamma\le\mathrm{SL}_2(\mathbb Z)\) and that its action preserves the determinant set |
| Endpoint quadratic-form identity | **GREEN.** No coefficient sum is double-counted | Retain (167.16); state explicitly that \(u_L\) contains divisor incidences, not \(c_N\) |
| Endpoint energy | **GREEN.** It is incidence energy, not \(D_L\) | Keep the two quantities distinct |
| Schur row/column degree | **GREEN.** Each fixed product and gap has at most one endpoint per divisor | Add explicit epsilon relabelling when combining degree and norm bounds |
| Schur \(L^3\) capacity | **GREEN as an upper bound only** | Avoid language suggesting a matching lower bound |
| Polylogarithmic sector | **GREEN after epsilon relabelling.** It is owner-complete | Insert the divisor-bound and logarithm split used in (3.9) |
| Phase derivative/seminorm scale | **GREEN algebraically** | State the no-go conditionally on an uncompensated positive seminorm exponent |
| Nonempty top two-adic block | **RED.** Assumed, not proved | Remove “nonempty,” or prove literal support and \(\asymp L\) determinant-weight mass |
| \(L^2\) source base error | **AMBER/CONDITIONAL.** Correct only for \(\|\beta\xi\|_1\asymp L\) | Replace the unconditional claim by the general \(L\|\beta\xi\|_1\) ledger |
| Principal/nonzero main term | **RED as written in the result.** Neither pointwise principality nor nonzero literal main term follows from the displayed formulas | Use the conditional wording in Section 3.5 |
| 2025 Part-I positive forms | **UNVERIFIED HERE.** No theorem formula is displayed for an independent power check | Leave to the dedicated source audit; do not promote from this report alone |
| Downstream scope | **GREEN.** K17a, all parents, and all exponents remain open | No change |

No numerical control is needed. All checks are exact algebra, counting, or logical scope.

## 6. Dependencies and exact artifacts used

This review used only:

1. rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reports/literal_determinant_kernel_attack.md;
2. proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reports/blind_determinant_interface_rederivation.md.

No claimant file, proof graph, validation matrix, synthesis, or shared state was edited. No source theorem was independently consulted; source conclusions were checked only against formulas displayed in the literal report.

## 7. Recommended state effect

**REVISE / PARTIAL RETAIN; no graph change.**

Retain as candidate evidence, after the stated notation and epsilon repairs:

- the multiplicity-one determinant and free-orbit openings;
- the exact endpoint-vector identity;
- the Schur \(L^3X^\varepsilon\) upper-capacity bound;
- the phase derivative ledger;
- the owner-complete polylogarithmic-shift bound.

Do not retain as unconditional evidence:

- existence or density of the \(k=2,\ h\asymp L\) literal block;
- the universal \(L^2\) source base-error assertion;
- the consequent universal \(J^{-C_*}\) requirement on \(\mathcal K_+\);
- a forced principal or nonzero source main term;
- theorem-specific 2025 Part-I power conclusions not reproduced by displayed formulas.

Repair those statements to explicit conditional ledgers, keep the selector/source interface open, and retain K17a, every parent, and every exponent at their present status. This review licenses no source application and no shared-state edit.
