# Blind rederivation: deep exceptional strata

## 1. Result: exact lift and actual-symbol no-go lemma

Let \(q=p^\nu\Vert M\), put \(A=h_1\), \(B=h_2\), and \(V=v\), and interpret all three variables locally modulo \(q\). The numerator of the reciprocal part of the local phase is

\[
 \Phi_{A,B,V}(x)
 =\frac{N_{A,B,V}(x)}{x(x-A)(x-V)(x-V-B)},
 \qquad
 N_{A,B,V}(x)
 =(B-A)x^2+2AVx-AV(V+B).                         \tag{R87.1}
\]

Consequently, at an odd prime power, with \(s_p=v_p(K)\) and \(v_p(0)=+\infty\), the exact coefficientwise cancellation depth is

\[
 \kappa_p=\min\{\nu,\ s_p+v_p(B-A),\ s_p+v_p(A)+v_p(V)\}.       \tag{R87.2}
\]

In particular, when \(p\nmid K\), the reciprocal phase vanishes modulo \(p^\nu\) as a rational function precisely when

\[
 B\equiv A\pmod {p^\nu},
 \qquad v_p(A)+v_p(V)\geq\nu.                                \tag{R87.3}
\]

For \(\nu=1\), (R87.3) is exactly the union of the two prime-field branches in (87.11). For \(\nu>1\), it also contains genuinely mixed lifts, for example

\[
 A=B=p^r,\qquad V=p^{\nu-r},\qquad 1\leq r<\nu,                \tag{R87.4}
\]

which belong to neither naive full-prime-power lift \(A=B=0\pmod {p^\nu}\) nor \(V=0,\ A=B\pmod {p^\nu}\). If also \(p^\nu\mid u\), the local phase is constant and the pure-\(q\) trace in (87.10) is \(q\varphi(q)\asymp q^2\). Thus a branch-by-branch lift of (87.11) leaves a maximal trace in the purported generic remainder.

At the 2-part, the local unit set is empty unless \(A,B,V\) are all even. If they are all even, it is the full odd unit set. Writing

\[
 a_2=B-A,\qquad b_2=2AV,\qquad c_2=-AV(V+B),
\]

the largest power \(2^{\mu_2}\) which divides \(N(x)\) for every odd \(x\) is given exactly by

\[
 \mu_2=\min\bigl\{
 v_2(a_2+b_2+c_2),
 v_2(8a_2+2b_2),
 v_2(8a_2)
 \bigr\}.                                                     \tag{R87.5}
\]

Hence the reciprocal phase \(K\Phi\) vanishes on the entire 2-adic unit locus modulo \(2^\nu\) exactly when

\[
 \min\{\nu,v_2(K)+\mu_2\}=\nu.                               \tag{R87.6}
\]

This includes the extra degeneracy caused by a nonunit \(K\), relevant in particular to the displayed \(g=2\) class. Moreover, once the reciprocal phase vanishes, \(ux\) is constant on all odd \(x\pmod {2^\nu}\) already when \(2^{\nu-1}\mid u\), not only when \(2^\nu\mid u\).

The exceptional coefficients do not disappear against the actual stationary symbol. On the exact paired branch, define

\[
 F_{b,d,h}=\sum_n I_b(n+d)\overline{I_b(n)}e_M(hn),             \tag{R87.7}
\]

with zero extension enforcing the exact deep support. Then the complete transform of the actual fourfold weight satisfies

\[
 \widehat\Omega_{b,u}(0,h,h)
 =\sum_d F_{b,d+u,h}\overline{F_{b,d,h}}.                      \tag{R87.8}
\]

For \(u=jM\), the arithmetic factor is the nonnegative self-return value (positive whenever \(N_M(h)>0\))

\[
 \mathfrak T_M(jM,0;h,h)=M N_M(h),\qquad
 N_M(h)=\#\{x\bmod M:(x(x-h),M)=1\}.                          \tag{R87.9}
\]

If \(U=LM\), the two-sided Fejer form of (R87.8) is the exact nonnegative row energy

\[
 \sum_{|j|<L}(U-|jM|)\widehat\Omega_{b,jM}(0,h,h)
 =M\sum_{r\bmod M}\sum_t
 \left|\sum_{j=0}^{L-1}F_{b,r+(t+j)M,h}\right|^2.             \tag{R87.10}
\]

Therefore the complete-transform self-return supplies no arithmetic square-root saving: after the compulsory diagonal is restored, it is a positive norm of the actual stationary row. Target-safety can only come from a separate physical row-energy estimate. The permitted interfaces contain no proof of the required \(Q^{-5/12}\) energy saving and no uniform treatment of integer/perfect-power resonances. Accordingly, (87.2), target-safety of the full exceptional aggregate, and a quantitatively sufficient generic remainder do **not** follow from the permitted packet. The rigorous outcome is a no-go for the naive prime-field lift and for any arithmetic-only disposal of the exceptional modes; the exact signed exceptional survivor must remain.

## 2. Exact statement and hypotheses

Assume exactly the scales, support, three \((g,M,K)\) classes, stationary representation (87.3)--(87.4), periodic normalization (87.5), zero extension, and completed correlation (87.9)--(87.16) in the derivation packet. No coprimality beyond what is explicitly stated is imposed; \(s_p=v_p(K)\) in (R87.2) therefore also records any nonunit local \(K\). CRT changes the local additive coefficients by units, which does not change any valuation in (R87.2). The claims involving the prime-field square-root alternative use its stated hypothesis \(p\nmid K\).

For each \(b,u\), let

\[
 \widehat\Omega_{b,u}(v,h_1,h_2)
 =\sum_{d,n,m}\Omega_{b,d,u}(n,m)
   e_M(vd+h_1n-h_2m),                                        \tag{R87.11}
\]

where the sum is only over the exact common support of \(d,d+u,n,m\). Then the exact off-diagonal row correlation is

\[
 \sum_d Z_b(d+u)\overline{Z_b(d)}
 =\frac1{M^5}
 \sum_{\substack{h_1,h_2\bmod M\\h_1,h_2\ne0}}
 \sum_{v\bmod M}
 \mathfrak T_M(u,v;h_1,h_2)
 \widehat\Omega_{b,u}(v,h_1,h_2).                            \tag{R87.12}
\]

An exact divisor-alignment label for odd factors is

\[
 R_{\rm align}(u;h_1,h_2,v)
 =\prod_{p^\nu\Vert M,\ p\ {\rm odd}}
 p^{\min\{v_p(u),\kappa_p\}},                               \tag{R87.13}
\]

augmented at \(p=2\) by the unit-locus criterion (R87.5)--(R87.6) and the possibility \(2^{\nu-1}\mid u\). Partitioning the finite frequency set in (R87.12) according to (R87.13), with each tuple assigned once, gives an exact signed exceptional part \(R_{\rm align}>1\) and an exact complementary residual. This is only an algebraic partition; no estimate for either part is asserted.

For squarefree odd local factors, (R87.3) says that at each \(p\) one independently chooses the zero branch \(p\mid h_1,h_2\) or the paired branch \(p\mid v,h_1-h_2\), with their overlap counted once. Thus the global squarefree exceptional set is divisor-aligned and is not a single global branch. For prime powers, the split valuations in (R87.3) must also be included.

The conclusion is uniform in all three displayed classes, both signs and reflected compatible orientations, and positive or negative deep differences. It is deliberately limited to the deep survivor and its A-process correlation; it makes no M1, M2, uniformity, assembly, or global exponent claim.

## 3. Proof or derivation

First, put the four reciprocal terms in (87.10) over their common denominator. Pairing the first two and last two terms gives

\[
\begin{aligned}
N(x)
&=-A(x-V)(x-V-B)+Bx(x-A)\\
&=(B-A)x^2+2AVx-AV(V+B),
\end{aligned}
\]

which proves (R87.1). For an odd \(p\), the denominator is a unit on the summation locus. The three coefficients of \(K N(x)\) have minimum valuation

\[
 \min\{s_p+v_p(B-A),\ s_p+v_p(A)+v_p(V)\},
\]

because the constant coefficient has at least the valuation of \(KAV\), while the linear coefficient has exactly that valuation when \(p\ne2\). This proves (R87.2). When \(s_p=0\), full cancellation is therefore equivalent to (R87.3). Reduction to \(\nu=1\) gives \(A=0\) or \(V=0\), together with \(A=B\), exactly recovering (87.11). The mixed example (R87.4) has \(AV=p^\nu\) and \(A=B\), so \(N(x)=0\pmod {p^\nu}\) although neither naive lifted branch holds. If \(u=0\pmod {p^\nu}\), every permitted \(x\) contributes \(1\); in the example all shifts are divisible by \(p\), so the permitted set is all units and the trace equals \(q\varphi(q)\).

For \(q=2^\nu\), an admissible \(x\) is odd. The other three entries are odd exactly when \(A,V,B\) are even; otherwise the local sum is empty. In the nonempty case write \(x=1+2t\). For \(N(x)=a_2x^2+b_2x+c_2\), Newton expansion in \(t\) has initial value, first difference, and second difference

\[
 a_2+b_2+c_2,\qquad 8a_2+2b_2,\qquad 8a_2.
\]

A quadratic integer sequence is divisible by \(2^j\) at every integer \(t\) exactly when these three Newton coefficients are divisible by \(2^j\). This proves (R87.5); multiplying by \(K\) proves (R87.6). If \(K\Phi=0\pmod {2^\nu}\), then for odd \(x,x'\), \(u(x-x')\) is always divisible by \(2^\nu\) exactly when \(2^{\nu-1}\mid u\), proving the stated 2-adic self-return condition.

The paired branch also gives a complete prime-power check independent of \(K\):

\[
 \mathfrak T_q(u,0;h,h)
 =q\sum_{\substack{x\bmod q\\ (x(x-h),q)=1}}e_q(ux).          \tag{R87.14}
\]

For odd \(p\), this equals

\[
\begin{cases}
q\,c_q(u),&p\mid h,\\
q\,p^{\nu-1}(p-2),&p\nmid h,\ q\mid u,\\
-q\,p^{\nu-1}\bigl(1+e_p(\alpha h)\bigr),
 &p\nmid h,\ u=p^{\nu-1}\alpha,\ p\nmid\alpha,\\
0,&p\nmid h,\ v_p(u)\leq\nu-2.
\end{cases}                                                    \tag{R87.15}
\]

For \(p=2\), it is \(0\) when \(h\) is odd and \(q\,c_q(u)\) when \(h\) is even. Formula (87.13) follows from the first line of (R87.15) when \(\nu\ge2\). As written in the packet it needs that hypothesis: for \(\nu=1\), its left side is instead

\[
 -p\bigl(1+e_p(\alpha)\bigr).
\]

The squarefree family (87.14) follows by CRT: modulo \(R\), \(h=u=R\) makes the local count \(\varphi(R)\); modulo \(\ell\), the two excluded residues give \(-1-e_\ell(R)\). This also shows why squarefree divisor alignment can be of order \(M^2\).

Next, the Fourier normalization is exact. If

\[
 \mathcal P_d(n)=S(n+d,K;M)\overline{S(n,K;M)},
\]

then opening the two Kloosterman sums gives

\[
 \mathcal P_d(n)=\sum_{h\bmod M}\mathcal C(d,h)e_M(nh),
 \qquad \mathcal C(d,0)=c_M(d).
\]

Thus

\[
 A_{M,K,d}(n)=\sum_{h\ne0}\mathcal C(d,h)e_M(nh).              \tag{R87.16}
\]

The inverse \(d\)-Fourier transform of the definition (87.10) contributes \(1/M\). Combining it with the two factors \(M^{-2}\) in the two \(Z_b\)'s yields \(M^{-5}\), proving (R87.12). Equation (R87.16) incorporates the four-Kloosterman term, both Ramanujan cross terms, and the Ramanujan-square term exactly once: the latter three are precisely what removes the global \(h_1=0\) or \(h_2=0\) modes. A local congruence \(h_i=0\pmod p\) is not a deleted global zero mode.

Finally, setting \(v=0,h_1=h_2=h\) in (R87.11) separates the \(n\)- and \(m\)-sums and proves (R87.8). For \(u=jM\), (87.12) reduces to the count (R87.9). Expanding the square on the right of (R87.10), putting the two window indices \(j,k\) together according to their difference, and summing the residue classes \(r\pmod M\) proves (R87.10). This calculation uses the actual phase

\[
 -\eta\lambda_b\bigl(\sqrt{|n+d|}-\sqrt{|n|}\bigr)
\]

inside each \(F_{b,d,h}\); no separated arbitrary coefficient and no pre-emptive absolute value has been introduced.

## 4. First doubtful or unproved step

The first unavailable step is a uniform prime-power trace theorem for the complement of the exact cancellation-depth strata (R87.2), (R87.5), including nonunit \(K\), sparse local unit sets, mixed lifts, and the 2-part. The packet supplies only a prime-field square-root statement. Applying that statement factorwise after extracting only the two naive \(p^\nu\)-branches is invalid by (R87.4).

Even if such a local theorem were added, the next unproved step would be the physical estimate for the actual rows (R87.7). The phase of (R87.11), with \(\rho(t)=\sqrt{|t|}\), has formal gradients

\[
\begin{aligned}
\partial_n\Psi&=-\eta\lambda_b(\rho'(n+d+u)-\rho'(n))+h_1/M,\\
\partial_m\Psi&= \eta\lambda_b(\rho'(m+d)-\rho'(m))-h_2/M,\\
\partial_d\Psi&=-\eta\lambda_b(\rho'(n+d+u)-\rho'(m+d))+v/M.
\end{aligned}                                                   \tag{R87.17}
\]

For integer sums, any of these can return to an integral frequency. The hypotheses \(\lambda_b\asymp J\) and \(\|P_b\|_\infty+\operatorname{Var}P_b\ll X^\varepsilon H\) provide no stated uniform separation from such integer or perfect-power resonances. Thus (R87.10) cannot presently be bounded with the required \(Q^{-5/12}\) energy factor. This is an open estimate, not a permissible cancellation assumption.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| external_normalization | **Pass.** Two \(M^{-2}\) row normalizations and one inverse \(d\)-transform give exactly \(M^{-5}\) in (R87.12). |
| all_class_local_units | **Pass for the exact identities; open for a generic bound.** The argument is per \(M,K\), hence applies to all three displayed classes. Odd nonunit \(K\) is retained through \(s_p\); the 2-adic unit set and nonunit-\(K\) enlargement are explicit. |
| physical_row_energy_factor | **Not proved.** The self-return is the row norm (R87.10); no \(Q^{-5/12}\) estimate follows from (87.3)--(87.4). |
| deep_difference_ownership | **Pass.** Every \(F_{b,d,h}\) is zero-extended, so only the exact common deep support of \(d\) and \(d+u\) occurs. |
| negative_and_modulus_multiple_differences | **Pass.** The use of \(\sqrt{|\cdot|}\) keeps both signs/reflections, and \(u=jM\) is treated explicitly. Negative \(d\) is unchanged arithmetically. |
| ramanujan_cross_and_square_terms | **Pass.** Equation (R87.16) shows their exact one-time cancellation of the global zero modes. |
| prime_power_and_2adic_strata | **Prime-power obstruction proved; generic estimate open.** Mixed lifts (R87.3), exact paired sums (R87.15), and the 2-adic unit-locus criterion are included. |
| squarefree_divisor_aligned_modes | **Pass.** Independent local branch choices and the exact CRT derivation of (87.14) are recorded. |
| fejer_prefactor_and_diagonal | **Pass.** The weights \(U-|u|\), the \(u=0\) diagonal, and the resulting positive norm all appear in (R87.10). No claim is made by omitting the diagonal. |
| actual_fourfold_stationary_symbol | **Pass.** Equations (R87.7)--(R87.12) use (87.15)--(87.16) without coefficient separation. |
| generic_trace_remainder | **Fail/open.** Prime-field square-root cancellation does not control the mixed prime-power complement of a naive extraction, and no corrected prime-power theorem is available. |
| entry_exit_and_error_ownership | **Pass.** Zero extension handles entry/exit exactly; no collar, shell, axis, stationary error, tail, or Farey transition is reintroduced. |
| integer_and_perfect_power_resonance | **Fail/open.** The possible integral returns in (R87.17) have no supplied separation or resonant subcase estimate. |
| complete_transform_self_return | **Pass as an obstruction.** Equations (R87.9)--(R87.10) identify the exact positive stride-\(M\) Fejer energy. |
| downstream_scope | **Pass.** No global exponent or closure of any other M1/M2/uniformity/assembly gate is asserted. |

The controls therefore falsify a promotion claim: the algebraic classification advances, but the quantitative exit gate remains open.

## 6. Dependencies and exact artifacts used

The only mathematical artifact used was

- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/derivation_packet.md.

The task instructions were read from

- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/briefs/blind_exceptional_strata_rederivation.md.

No shared proof state, strategy file, prior-round or sibling report, source card, web source, or numerical computation was consulted. All identities above were derived algebraically from the packet.

## 7. Recommended state effect

**Revise; do not promote.** Replace any naive prime-power lift of (87.11) by the cancellation-depth classification (R87.2), include the exact 2-adic unit-locus behavior (R87.5)--(R87.6), and amend (87.13) to state \(\nu\ge2\). Retain the paired and divisor-aligned modes as an exact signed survivor expressed through (R87.8), including modulus-multiple self-return (R87.10). The frozen target should remain open until two independent estimates are supplied and checked: a uniform generic prime-power/2-adic trace theorem and an actual-row Fejer energy bound delivering the required \(Q^{-5/12}\) saving while treating (R87.17) resonances. No downstream state should change on the basis of this report alone.

### Supplemental seam audit (2026-08-17): full-prime-power group extraction

**Verdict.** The conductor's proposed estimate is correct as a conditional, strictly scoped lemma, with three qualifications that must be part of its statement:

1. the normalized physical-row estimate
   \[
   \sup_{b,x,\theta}|R_{b,x}(\theta)|
   \ll_\varepsilon X^\varepsilon TQ^{-5/24}                  \tag{R87.S1}
   \]
   must already be proved uniformly for all three classes and all retained sign/orientation components;
2. \(\Pi_D\) must be the exact deep-difference Fourier projection (or a smooth projection dominating it), with
   \[
   \|\Pi_D\|_{L^\infty\to L^\infty}
   \ll \log(2+D)\ll_\varepsilon X^\varepsilon;                \tag{R87.S2}
   \]
3. the result removes only the modes which, at **every exact prime-power factor** \(q\Vert M\), lie on one of the two full-\(q\) branches. It does not remove the mixed prime-power strata (R87.3)--(R87.4), partial-factor degeneracies, or the remaining cross-group correlation.

Under (R87.S1)--(R87.S2), the full-factor exceptional Fejer block obeys

\[
 \mathcal P_{\mathrm{full}}
 \ll_\varepsilon
 X^\varepsilon U B^3T^4Q^{-5/6}.                              \tag{R87.S3}
\]

At the admissible choice \(U=D\),

\[
 \mathcal P_{\mathrm{full}}
 \ll_\varepsilon
 X^\varepsilon\frac{D}{B}J^{14/5},                            \tag{R87.S4}
\]

so this block is target-safe at the normalization of (87.8). This is promotable as a nonempty scoped exceptional-core lemma if (R87.S1) is an accepted upstream estimate. It does not promote (87.2), the complete exceptional aggregate, or a generic remainder theorem.

**Normalization and Ramanujan audit.** With normalized Haar measure \(d\theta\) on \(\mathbb R/\mathbb Z\), define

\[
 R_{b,x}(\theta)
 =\frac1M\sum_n I_b(n)e_M(nx)e(n\theta),\qquad
 F_{b;x,y}(\theta)
 =e_M\!\left(K(x^{-1}-y^{-1})\right)
 R_{b,x}(\theta)\overline{R_{b,y}(\theta)}.                   \tag{R87.S5}
\]

Before the deep projection, changing variables from \((n,d)\) to \((n,r=n+d)\) gives exactly

\[
 \sum_d Z_b^{\mathrm{unres}}(d)e(d\theta)
 =\sum_{\substack{x,y\bmod M\\x,y\ {\rm units}\\x\ne y}}
 F_{b;x,y}(\theta).                                           \tag{R87.S6}
\]

There is no omitted power of \(M\): the two factors \(M^{-1}\) in (R87.S5) are precisely the \(M^{-2}\) in \(Z_b\). Opening the uncentered Kloosterman product gives the sum over all ordered unit pairs \((x,y)\). The Ramanujan term gives

\[
 \frac1{M^2}\sum_{r,n}c_M(r-n)I_b(r)\overline{I_b(n)}
 e((r-n)\theta)
 =\sum_{z\bmod M}^{*}|R_{b,z}(\theta)|^2,                     \tag{R87.S7}
\]

which is exactly the \(x=y=z\) diagonal of the Kloosterman-pair sum. Thus subtraction of \(c_M\) leaves \(x\ne y\) once and only once. After applying \(\Pi_D\), (R87.S6) is the exact retained deep row, so the four-Kloosterman term, both Ramanujan cross terms, and the Ramanujan-square term are all represented correctly when the projected row is squared.

**One-count CRT equivalence.** Write \(M=\prod_{q\Vert M}q\), where every \(q\) is an exact prime-power factor. For each ordered unit pair \(x\ne y\), define

\[
 S(x,y)=\{q\Vert M:x_q\ne y_q\},
\]

which is nonempty, and let

\[
 \alpha=((x_q,y_q))_{q\in S},\qquad
 z=(x_q=y_q)_{q\notin S}.
\]

For fixed \(S,\alpha\), set

\[
 G_{b;S,\alpha}=\sum_z F_{b;x(\alpha,z),y(\alpha,z)},\qquad
 H_{b;S,\alpha}=\Pi_DG_{b;S,\alpha}.                           \tag{R87.S8}
\]

Every \(x\ne y\) occurs in exactly one triple \((S,\alpha,z)\). Consider a cross term between two ordered pairs \((x_1,y_1)\) and \((x_2,y_2)\). In the variables underlying (87.10),

\[
 h_1=x_1-y_1,\qquad h_2=x_2-y_2,\qquad v=x_1-x_2.             \tag{R87.S9}
\]

The two pairs occur in the same group exactly when, for every \(q\Vert M\),

- \(q\notin S\): \(x_{1,q}=y_{1,q}\) and \(x_{2,q}=y_{2,q}\), hence
  \(h_1=h_2=0\pmod q\) (the full-\(q\) zero branch); or
- \(q\in S\): \((x_{1,q},y_{1,q})=(x_{2,q},y_{2,q})=\alpha_q\), hence
  \(v=0\) and \(h_1=h_2\pmod q\) (the full-\(q\) paired branch).

Conversely, either full-\(q\) branch implies the corresponding same-group relation. At their overlap \(h_1=h_2=v=0\pmod q\), the canonical rule puts \(q\notin S\), so there is no double count. The impossible global group \(S=\varnothing\) is exactly the diagonal already removed by (R87.S7). It follows that

\[
 \sum_{\varnothing\ne S}\sum_\alpha |H_{b;S,\alpha}|^2        \tag{R87.S10}
\]

is exactly the within-group block comprising all mixtures of the two full-\(q\) branches across every exact prime-power factor. Every cross-group term fails both full-\(q\) alternatives for at least one \(q\), and is left in the residual. In particular, stride-\(M\) self-return lies in (R87.S10), whereas the mixed lift (R87.4) is a cross-group term and is not claimed here.

**Counting and row-energy bound.** Put \(L=TQ^{-5/24}\). For fixed \(S\), the number of active labels and inactive diagonal choices are

\[
 A_S=\prod_{q\in S}\varphi(q)(\varphi(q)-1),\qquad
 Z_S=\prod_{q\notin S}\varphi(q).
\]

By (R87.S1)--(R87.S2),

\[
 |H_{b;S,\alpha}|
 \ll_\varepsilon X^\varepsilon Z_SL^2.
\]

Therefore

\[
\begin{aligned}
 \sum_{\varnothing\ne S}\sum_\alpha|H_{b;S,\alpha}|^2
 &\ll_\varepsilon X^\varepsilon L^4
   \sum_{\varnothing\ne S}A_SZ_S^2\\
 &\le X^\varepsilon L^4\,2^{\omega(M)}\varphi(M)^2\\
 &\ll_\varepsilon X^\varepsilon M^2T^4Q^{-5/6}.               \tag{R87.S11}
\end{aligned}
\]

This verifies the delicate power of \(B\): the inactive diagonal sum is squared, but the exact group count makes \(A_SZ_S^2\le\varphi(M)^2\); there is no additional factor \(M\). Summing \(b\asymp B\) with \(M\asymp B\) gives \(B^3\), proving (R87.S3) after the Fejer step.

**Fejer implication.** Use the unnormalized Dirichlet kernel

\[
 D_U(\theta)=\sum_{j=0}^{U-1}e(j\theta),
 \qquad \int_0^1|D_U(\theta)|^2\,d\theta=U.
\]

Then

\[
 \mathcal P_{\mathrm{full}}
 :=\sum_{b\asymp B}\int_0^1|D_U(\theta)|^2
   \sum_{\varnothing\ne S}\sum_\alpha
   |H_{b;S,\alpha}(\theta)|^2\,d\theta                         \tag{R87.S12}
\]

is the exact positive Fejer form of the within-group exceptional block, including its diagonal and the weights \(U-|u|\). Equation (R87.S11) and \(\int|D_U|^2=U\) prove (R87.S3).

This is not the literal inside-absolute quantity \(\mathcal E_1(D,U)\). If
\(\Delta_{\mathrm{full}}\) denotes the \(u=0\) within-group diagonal and
\(\mathcal O_{\mathrm{full}}\) its two-sided signed off-diagonal, then

\[
 \mathcal P_{\mathrm{full}}
 =U\Delta_{\mathrm{full}}+\mathcal O_{\mathrm{full}}.          \tag{R87.S13}
\]

The same argument without \(|D_U|^2\), followed by multiplication by \(U\), gives

\[
 U\Delta_{\mathrm{full}}
 \ll_\varepsilon X^\varepsilon UB^3T^4Q^{-5/6}.
\]

Thus \(|\mathcal O_{\mathrm{full}}|\) has the same bound by (R87.S13). This supplies the permitted outside-absolute signed estimate, but it must not be advertised as a proof of the literal absolute-value estimate for each \(u\).

Finally, at \(U=D\),

\[
 B^4T^4Q^{-5/6}
 \le J^{4(3/20)}J^{4(3/5)}J^{-(2/5)(5/6)}
 =J^{8/3}
 \le J^{14/5}.                                                 \tag{R87.S14}
\]

Hence (R87.S3) implies (R87.S4), matching
\(U^2J^{14/5}/(B(D+U))\asymp (D/B)J^{14/5}\) at \(U=D\).
The choice \(U=D\) is essential to this comparison as stated; no all-\(U\) version of (87.8) has been proved.

**Supplemental recommended state effect.** Promote only the conditional statement: “assuming the uniform normalized row bound (R87.S1), the exact all-local-full-factor exceptional core is target-safe at \(U=D\).” Retain the cross-group residual as an explicit survivor. The mixed prime-power modes, 2-adic partial strata, generic trace remainder, and global frozen target remain open, so the original report's no-go verdict continues to apply beyond this newly closed seam.
