# Conductor-candidate source-scope review

## 1. Result

**Verdict: pass.**

The source-facing claims in the conductor candidate are consistent with the finalized Grimmelt--Merikoski audit and the literal/source reconciliation review. In particular, the candidate has incorporated the earlier mandatory repairs:

- it gives the exact bare-character orbit cancellation but does not transfer it to a selector-dependent coefficient;
- it restricts the explicit low-gcd orbit witness to \(0<\gamma<1/2\) and explains the \(\gamma\geq1/2\) case;
- it states only continuous rank-one nonseparability of the variable-\(r\) phase, preserving the possibility of a new discrete or controlled-rank construction;
- it records the phase seminorm scale, the conditional \(\mathcal R_0/\mathcal R_2/\mathcal K_+\) ledger, and no negative-power \(\mathcal K_+\) demand;
- it treats the fixed-\(r\) triangle inequality as a failure to prove the one-outer-real-part target;
- and it distinguishes the 2025 raw automorphic kernel, principal component, and nonnegative discrepancy-kernel forms.

The terminal label is appropriately limited to the audited black-box interfaces. It is not a claim that every determinant or oscillatory method fails.

Two precision notes are nonblocking: the bare coefficient satisfies the full class law \(\mathcal A(4,1,\chi_0,1)\), not merely left invariance under \(\Gamma_2(4,1)\); and the lower seminorm comparison is understood on a nonzero interior cell where the remaining amplitude does not cancel the phase derivative. Both facts follow from the candidate's stated setup and do not require changing its conclusion.

## 2. Exact source statements and parameter placement

### 2.1 Grimmelt--Merikoski 2024

Under
\[
 M=\begin{pmatrix}a&b\\c&d_0\end{pmatrix}
 =\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
 \qquad \det M=r=hk,
\]
the candidate uses
\[
 q_1=4,\qquad q_2=1,\qquad q=4,\qquad
 k=2^{v_2(r)},\qquad h\ \mathrm{odd}.
\]
Because \(d,d'\) are odd,
\[
 (h,kq)=1,\qquad (a,c,k)=(b,d_0,k)=1.
\]
These pass only the determinant and column-primitivity hypotheses.

Theorem 10.1 additionally requires:

- \(\alpha\in\mathcal A(4,1,\chi,\xi)\);
- one common
  \[
  f\in C^7_\delta
  \left(A/\sqrt{HK},C/\sqrt{HK},D/\sqrt{HK}\right);
  \]
- dyadic \(h,k\) coefficients, \(HK\leq(AD)^{1+\eta}\);
- the absolute orbit-correlation hypothesis (10.2), quantified by \(\mathcal K_+\);
- the principal-character main term; and
- the error
  \[
  Z^{O(\eta)}\delta^{-O(1)}(AD)^{1/2}
  \|\beta\xi\|_2\mathcal K_+^{1/2}
  \{\mathcal R_0+\min(\mathcal R_1,\mathcal R_2)\}.
\tag{S.1}
  \]

The candidate correctly treats the residual selector, common variable-\(r\) phase, smoothness, \(\mathcal K_+\), cells, endpoints, and completion as additional obligations.

### 2.2 Grimmelt--Merikoski 2025 Part I

Theorem 1.1 permits compactly supported linear functionals on
\(G=\mathrm{SL}_2(\mathbb R)\) and a complex function
\[
 f\in C^{10}_\delta(A,C,D),\qquad F:G\to\mathbb C.
\]
It does not prohibit oscillatory \(f\); all frequency is charged through the derivative bounds and \(\delta^{-O(1)}\). Its bound is for the discrepancy and contains two nonnegative forms
\[
 \langle\alpha_i\mid\Delta k_{X_i^2,R_i}\mid\alpha_i\rangle.
\]
The raw kernel satisfies
\[
 \Delta F=\mathcal K_{\Gamma,\chi}F
 -\frac{\mathbf 1_{\chi\ \mathrm{principal}}}{|\Gamma\backslash G|}
 \int_G F(g)\,dg.
\tag{S.2}
\]
The candidate correctly requires an endpoint embedding and raw kernel identity before invoking (S.2), then keeps the principal and discrepancy terms separate.

## 3. Proof and derivation of the source checks

### 3.1 Coefficient class and finite orbit main term

Let
\[
 \alpha_{\mathrm{bare}}(M)=\chi_4(a)\chi_4(b).
\]
For an integer matrix
\[
 g=\begin{pmatrix}p&4q\\r&s\end{pmatrix},
 \qquad (\det g,4)=1,
\]
the top row of \(gM\) is
\[
 (pa+4qc,\;pb+4qd).
\]
Since \(p\) is odd,
\[
\begin{aligned}
\alpha_{\mathrm{bare}}(gM)
&=\chi_4(pa+4qc)\chi_4(pb+4qd)\\
&=\chi_4(p)^2\chi_4(a)\chi_4(b)
=\chi_0(p)\alpha_{\mathrm{bare}}(M),
\end{aligned}
\]
where \(\chi_0\) is the principal character modulo \(4\). Hence
\[
 \alpha_{\mathrm{bare}}\in\mathcal A(4,1,\chi_0,1);
\]
in particular it is left \(\Gamma_2(4,1)\)-invariant. This supplies the full source-class fact implicit in the candidate.

The candidate's orbit calculation is exact. Representatives for
\[
 \Gamma_2(4,1)\backslash\mathrm{SL}_2(\mathbb Z)
\]
have top rows
\[
 (x,1)\quad(x=0,1,2,3),\qquad (1,0),\ (1,2),
\]
and representatives for
\(\mathrm{SL}_2(\mathbb Z)\backslash\mathcal M_{2,1,k}\) are
\[
 \sigma_b=\begin{pmatrix}1&b\\0&k\end{pmatrix},
 \qquad b\bmod k,\quad(b,k)=1,
\]
with \(b=0\) at \(k=1\). The top row becomes \((x,xb+yk)\). The six terms sum to zero for \(k=1\); for \(k=2\) they split as \(-2+2\); and for \(4\mid k\), each unit \(b\) contributes \(4\chi_4(b)\), whose unit sum is zero. Therefore
\[
 \sum_{\tau\in\Gamma_2(4,1)\backslash\mathcal M_{2,1,k}}
 \alpha_{\mathrm{bare}}(\tau)=0
 \qquad(k=2^v).
\tag{S.3}
\]

The candidate correctly makes (S.3) conditional on leaving all selectors outside \(\alpha_{\mathrm{bare}}\). A selector-dependent automorphic factor changes the orbit weights, so its main term must be recomputed.

### 3.2 Low-gcd witness and its scope

For \(0<\gamma<1/2\), choose odd \(G,T\) with
\[
 \gamma L\leq G<L/2,\qquad T\asymp L,
\]
and
\[
 M=\begin{pmatrix}G&3G\\T&3T+2\end{pmatrix},\qquad
 v=\begin{pmatrix}1&4\\0&1\end{pmatrix}\in\Gamma_2(4,1).
\]
The original top gcd is \(G\). The transformed top row is
\[
 (G+4T,\;3G+12T+8),
\]
whose gcd divides \(8\); both entries are odd, so the gcd is \(1\). Also \(\det M=2G<L\). Thus the globally defined low-gcd coefficient is not left invariant in this stated range.

The candidate does not claim that both matrices are literal project incidences. It also correctly avoids extending the witness to \(\gamma\geq1/2\). In that range, \(g=(d,d')\) is odd, \(g\mid r\), and \(r/g\) is even, so
\[
 g\leq r/2<L/2\leq\gamma L;
\]
the low-gcd cutoff is identically one. The residual-selector automorphy/interpolation gap remains independent of this witness.

### 3.3 Continuous phase rank and seminorm scale

In normalized variables, the phase is
\[
 P_r(x,z)=
 e\!\left(J\sqrt r\,G(x,z)\right),
 \qquad
 G(x,z)=\sqrt{xz}-\sqrt{xz-1}.
\]
For \(J\ne0\) and \(r_1\ne r_2\),
\[
 \frac{P_{r_1}(x,z)}{P_{r_2}(x,z)}
 =
 e\!\left(J(\sqrt{r_1}-\sqrt{r_2})G(x,z)\right)
\]
is nonconstant on every common two-dimensional open cell. Hence the exact family cannot be written as one determinant coefficient times one common analytic test function. The candidate explicitly limits this to continuous rank-one nonseparability and does not exclude a discrete interpolant or controlled-rank expansion.

For
\[
 \phi_r(a,d_0)=J
 \left(\sqrt{ad_0}-\sqrt{ad_0-r}\right)
\]
and \(a,d_0\asymp L\),
\[
 L|\partial_a\phi_r|+L|\partial_{d_0}\phi_r|
 \asymp_{\mathrm{cell}}\frac{|J|r}{L}.
\tag{S.4}
\]
Since the normalized source scale satisfies
\((A/\sqrt r)\partial_x=A\partial_a\), (S.4) is the relevant \(C^7_\delta\) scale. On a nonzero interior cell where the remaining amplitude has smaller scaled derivatives, the phase factor requires
\[
 \delta^{-1}\gtrsim_{\mathrm{cell}}
 1+\frac{|J|r}{L}.
\tag{S.5}
\]
At \(r\asymp L\), this is \(\asymp1+|J|\). The candidate correctly treats \(\delta^{-O(1)}\) as an unspecified source loss and does not turn it into a lower bound for the literal sum.

### 3.4 Conditional \(\mathcal R_0/\mathcal R_2/\mathcal K_+\) ledger

The candidate explicitly labels its source-scale assumptions as optimistic and does not assert literal nonemptiness or density. Under
\[
 A=C=D\asymp L,\quad H\asymp L/k,\quad
 |\beta_h|\asymp1\ \text{on}\ \asymp H\ \text{indices},\quad
 \mathcal K_+^{1/2}\ll k^{1/2}X^\varepsilon,
\]
one has
\[
 \|\beta\|_2\asymp H^{1/2},
 \qquad \mathcal R_0\asymp H^{1/2}.
\]
The \(\mathcal R_0\) contribution is
\[
 \ll\delta^{-O(1)}L^2k^{-1/2}X^\varepsilon
\]
and sums over two-powers at \(L^2X^\varepsilon\) before the seminorm loss. The displayed \(\mathcal R_2\) route gives
\[
 \ll\delta^{-O(1)}L^{2+\theta_4}k^{-1/2}X^\varepsilon,
\]
and hence (after the 2-adic sum) the candidate's stated
\[
 \ll\delta^{-O(1)}L^{2+\theta_4+\varepsilon}.
\tag{S.6}
\]
The source supplies \(\theta_4\leq7/64\), not \(\theta_4=0\).

The candidate properly keeps \(\mathcal K_+\) as a separate hypothetical orbit-correlation input. It neither infers \(\mathcal K_+=O(1)\) from bounded coefficients nor demands a negative power of \(J\).

### 3.5 Fixed-\(r\) absolute values and Part I

The candidate correctly distinguishes an exact aggregate from a family of fixed-\(r\) estimates. Applying either theorem at each \(r\) and summing its errors gives an absolute error sum over \(r\); no cited source proves that sum at \(L^2X^\varepsilon\). This is a failure of that black-box route, not a proof that fixed-\(r\) information can never be recombined by a new theorem.

For Part I, the candidate correctly states all three missing layers:

1. an embedding of the finite endpoint set into \(G\);
2. a raw identity
   \[
   (\mathcal K_{\Gamma,\chi}F)(\iota(x),\iota(y))
   =T_{R_0,\gamma}(y,x)
   \]
   with no extra relative pairs; and
3. separation of the principal component before applying the discrepancy estimate.

Complex oscillatory \(F\) is formally permitted, but its ten derivatives incur the source seminorm cost. If phase and selectors are placed in endpoint functionals instead, the raw identity remains unproved, and the two nonnegative discrepancy-kernel autocorrelations remain open.

## 4. First doubtful or unproved step

For the 2024 route, the first unproved source step is still an exact target-safe representation of the residual selector as an admissible automorphic coefficient or common smooth family while preserving the variable-\(r\) phase and the one outer real part.

For Part I, it is the endpoint embedding and exact raw relative-kernel identity without cross terms. The principal component and the two discrepancy-kernel correlations follow as separate obligations.

Nothing in the candidate supplies these steps, and it does not claim otherwise.

## 5. Required controls and outcomes

1. **Full 2024 coefficient law — pass.** The bare character obeys the complete \(\mathcal A(4,1,\chi_0,1)\) transformation law.

2. **Finite orbit main term — pass.** Equation (167.C14) is exact for every \(k=2^v\); selector-dependent \(\alpha\) is explicitly excluded from the conclusion.

3. **Low-\(\gamma\) witness — pass.** Its range is exactly \(0<\gamma<1/2\), it is stated as a global coefficient witness rather than two literal incidences, and the vacuous \(\gamma\geq1/2\) case is separated.

4. **Continuous phase rank — pass.** Only rank-one analytic nonseparability is claimed; discrete and controlled-rank repairs remain open.

5. **Seminorm scale — pass with the interior-cell reading in (S.5).** The candidate uses the correct scaled derivative \(1+|J|r/L\) and preserves the unspecified final \(\delta\)-exponent.

6. **Conditional restored power — pass.** Literal density is not asserted, \(\mathcal R_0\) is target-sized only before losses, \(\mathcal R_2\) retains \(L^{\theta_4}\), and \(\mathcal K_+\) remains hypothetical without negative-power demand.

7. **Fixed-shift aggregation — pass.** The candidate rejects only the black-box absolute error sum.

8. **Part-I raw/principal/discrepancy seams — pass.** Complex \(C^{10}_\delta\) weights are allowed; the raw identity, principal term, and nonnegative discrepancy forms are distinct.

9. **Terminal scope — pass.** The no-go is confined to the audited 2024 direct placement, its fixed-shift triangle variant, and the available 2025 Part-I placement.

No numerical test was required or used.

## 6. Dependencies and exact artifacts used

This review used:

- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/candidates/conductor_round167_determinant_endpoint_polylog_reduction.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reports/oscillatory_source_power_hostile_audit.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-oscillatory-determinant-interface-gate/reviews/literal_source_interface_reconciliation_review.md.

The exact source claims are those of:

- Grimmelt--Merikoski, arXiv:2404.08502v2, Definition 3 and Theorem 10.1: [versioned HTML](https://arxiv.org/html/2404.08502v2), [versioned PDF](https://arxiv.org/pdf/2404.08502v2);
- Grimmelt--Merikoski, arXiv:2505.00489v2, Theorem 1.1, Definition 3, and Corollary 1.5: [versioned HTML](https://arxiv.org/html/2505.00489v2), [versioned PDF](https://arxiv.org/pdf/2505.00489v2).

The candidate and shared state were not edited.

## 7. Recommended state effect

**Pass.**

The candidate's source-facing conclusions may be retained:

- the bare coefficient and exact finite-orbit cancellation;
- the small-\(\gamma\) global noninvariance witness with its stated scope;
- the continuous rank-one phase obstruction;
- the cellwise phase seminorm scale;
- the conditional \(\mathcal R_0/\mathcal R_2/\mathcal K_+\) ledger;
- the fixed-\(r\) black-box aggregation failure; and
- the Part-I raw/principal/discrepancy separation.

The terminal label
\[
 \mathrm{oscillatory\_determinant\_interface\_no\_go}
\]
is source-licensed only for those audited interfaces. It must not be read as excluding a new automorphic selector decomposition, discrete interpolation, controlled-rank phase expansion, signed variable-determinant theorem, or another joint method.
