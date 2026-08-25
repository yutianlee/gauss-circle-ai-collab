# Round 159 statement-only blind rederivation

Campaign: `m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate`
Task: `blind_full_abel_rederivation`
Role: statement-only blind rederiver
Method: analytic/algebraic only; no computation and no external source

## 1. Result: exact reconstruction and a literal-hypothesis no-go

Let \(\mathcal L\) denote the chosen set of \(q=4N\) consecutive integer representatives meant by “one complete physical lift.” For every odd \(d\mid N\) and every individual residue \(v\bmod H\), the positive block and the negative block each have an exact three-line Abel decomposition: the positive right endpoint, positive moving-mask atom, positive literal adjacent-profile difference, and respectively the negative left endpoint, negative moving-mask atom, negative literal adjacent-profile difference. Both moving atoms have positive sign. Recombining the six lines gives the original \(j\)-sum exactly, before any estimate or complete-frequency inversion.

After that recombination, and only then adjoining the two omitted rows, (159.BL6) gives the exact full physical scalar

\[
 \mathcal S_{\mathcal L}(V)
 =\sum_{V<|j|\le 2V}\sum_{x\in\mathcal L}B_j(x)G_N(x^2-j).
\]

If \(\mathcal Z\) and \(\mathcal Y\) are respectively the complete \(v=0\) and \(v=H/2\) rows, with the same \(d\)-sum and normalization as (159.BL5), then the paired-interior matrix is exactly

\[
 \boxed{\mathcal I(V)=\mathcal S_{\mathcal L}(V)-\mathcal Z(V)-\mathcal Y(V).}
 \tag{R159.1}
\]

Put

\[
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell.
\]

The exact selected-coordinate form derivable from the literal statement is

\[
 \boxed{
 \mathcal S_{\mathcal L}(V)
 =\sum_{\ell\ge1}\chi_4(\ell)w_U(\ell)e(\sqrt{N\ell})
 \mathbf 1_{\kappa(\ell)\in\mathcal L}
 \mathbf 1_{V<|r(\ell)|\le2V}.}
 \tag{R159.2}
\]

Here the lift indicator cannot be deleted from the hypotheses supplied. It may be deleted only after proving the additional containment

\[
 w_U(\ell)\ne0,\quad V<|r(\ell)|\le2V
 \quad\Longrightarrow\quad \kappa(\ell)\in\mathcal L.
 \tag{R159.3}
\]

No support interval for \(w_U\), and hence no such containment, appears in (159.BL1)--(159.BL7). In fact a compactly supported, real, zero-extended BV profile satisfying (159.BL3) can be placed at a selected \(\ell\) whose nearest coordinate lies outside any prescribed complete lift. Thus the candidate formula with no lift indicator is false under the literal hypotheses. This is the first exact obstruction. Consequently neither the asserted global scalar target nor a strict owner-complete \((N,M,V)\)-range can be promoted from the statement alone.

With the lift issue repaired, the scalar target is

\[
 \mathcal S_{\mathcal L}(V)\ll_\varepsilon X^\varepsilon,
 \tag{R159.4}
\]

and its BV-dual raw target is \(M^{3/4}X^\varepsilon\), not merely an unsigned support estimate. The two closed rows are already \(O_\varepsilon(M^{-1/4}X^\varepsilon)\), so they are harmless at this scale but must be subtracted exactly once as in (R159.1).

## 2. Exact statement and hypotheses

Write

\[
 J_+=\{j\in\mathbb Z:V<j\le2V\}=[a_+,b_+],
 \]
\[
 a_+=\lfloor V\rfloor+1,\qquad b_+=\lfloor2V\rfloor,
\]

and

\[
 J_-=\{j\in\mathbb Z:-2V\le j<-V\}=[a_-,b_-],
\]
\[
 a_-=-\lfloor2V\rfloor,\qquad b_-=-\lfloor V\rfloor-1.
\]

Empty blocks are interpreted as zero. Define, on the chosen lift,

\[
 m_j(x)=\mathbf1_{x\ge1}\mathbf1_{-x\le j\le x-1},
\]
\[
 F_j(x)=w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right),
 \qquad B_j(x)=m_j(x)F_j(x).
\]

Here \(F_j\) is needed only where its radicand is nonnegative; set it to zero elsewhere. Every occurrence below is in fact on a mask where the radicand is positive.

For fixed odd \(d\mid N\), fixed \(v\bmod H\), and
\(K_j=K_{d,v}(j)\), define \(P^+\) and \(P^-\) as in the statement. Then the exact positive reconstruction is

\[
\begin{aligned}
 \sum_{j=a_+}^{b_+}A_j(v)K_j
 ={}&P^+(b_+)\widehat B_{b_+}(2dv) \\[-2pt]
 &+\sum_{j=a_+}^{b_+-1}P^+(j)\widehat{T_j^+}(2dv)\\[-2pt]
 &+\sum_{j=a_+}^{b_+-1}P^+(j)\widehat{R_j^+}(2dv),
\end{aligned}
\tag{R159.5+}
\]

where

\[
 T_j^+(x)=\mathbf1_{x=j+1}F_j(x),
 \tag{R159.6+}
\]

and

\[
\begin{aligned}
 R_j^+(x)
 ={}&\mathbf1_{x\ge1}\mathbf1_{-x\le j+1\le x-1}\\
 &\times\left[
 w_U\!\left(\frac{x^2-j}{N}\right)e(\sqrt{x^2-j}-x)
 -w_U\!\left(\frac{x^2-j-1}{N}\right)e(\sqrt{x^2-j-1}-x)
 \right].
\end{aligned}
\tag{R159.7+}
\]

The exact negative reconstruction is

\[
\begin{aligned}
 \sum_{j=a_-}^{b_-}A_j(v)K_j
 ={}&P^-(a_-)\widehat B_{a_-}(2dv)\\[-2pt]
 &+\sum_{j=a_-+1}^{b_-}P^-(j)\widehat{T_j^-}(2dv)\\[-2pt]
 &+\sum_{j=a_-+1}^{b_-}P^-(j)\widehat{R_j^-}(2dv),
\end{aligned}
\tag{R159.5-}
\]

where

\[
 T_j^-(x)=\mathbf1_{x=-j}F_j(x),
 \tag{R159.6-}
\]

and

\[
\begin{aligned}
 R_j^-(x)
 ={}&\mathbf1_{x\ge1}\mathbf1_{-x\le j-1\le x-1}\\
 &\times\left[
 w_U\!\left(\frac{x^2-j}{N}\right)e(\sqrt{x^2-j}-x)
 -w_U\!\left(\frac{x^2-j+1}{N}\right)e(\sqrt{x^2-j+1}-x)
 \right].
\end{aligned}
\tag{R159.7-}
\]

The trace values are literally

\[
 T_j^+(j+1)=w_U\!\left(\frac{j^2+j+1}{N}\right)
 e\!\left(\sqrt{j^2+j+1}-(j+1)\right),
\]

and

\[
 T_j^-(-j)=w_U\!\left(\frac{j^2-j}{N}\right)
 e\!\left(\sqrt{j^2-j}+j\right).
\]

They are boundary profiles only inside the two moving atoms. They do not replace the quotient profile \(w_U(\ell)\) in (R159.2).

For the two omitted whole rows, set

\[
 C_d=-\frac{i(1+i)}{2Nq}\chi_4(d)d\sqrt c,
\]

\[
 \mathcal Z(V)=\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}C_d
 \sum_{j\in J_+\cup J_-}\widehat B_j(0)K(0,-j;c),
 \tag{R159.8}
\]

and, since \(2d(H/2)=dH=2N\),

\[
 \mathcal Y(V)=\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}C_d
 \sum_{j\in J_+\cup J_-}\widehat B_j(2N)
 K\!\left(-(H/2)^2,-j;c\right).
 \tag{R159.9}
\]

All formulas retain arbitrary \(N\), every odd divisor \(d\), every individual residue \(v\bmod H\), and both representatives \(v\) and \(H-v\); no complementary-pair folding or factor of two is used. When \(c=4\), \(H=2\) and the only residues are \(0\) and \(H/2=1\), so that particular interior \(v\)-sum is empty. Formula (R159.1) still holds because its complete two-row contribution is removed exactly by (R159.8)--(R159.9).

## 3. Proof and derivation

### 3.1 The six finite Abel lines

For the positive block, put \(P^+(a_+-1)=0\). Since
\(K_j=P^+(j)-P^+(j-1)\), ordinary finite summation gives

\[
 \sum_{j=a_+}^{b_+}A_jK_j
 =A_{b_+}P^+(b_+)
 +\sum_{j=a_+}^{b_+-1}(A_j-A_{j+1})P^+(j).
 \tag{R159.10+}
\]

For \(j>0\), the moving masks obey the pointwise identity

\[
 m_j(x)=m_{j+1}(x)+\mathbf1_{x=j+1}.
 \tag{R159.11+}
\]

Consequently

\[
 B_j-B_{j+1}=T_j^++R_j^+.
 \tag{R159.12+}
\]

Substitution into (R159.10+) proves (R159.5+), with a positive right outer endpoint and positive moving atom. The two terms in (R159.7+) are not differentiated or approximated; both the profile and phase are evaluated at their literal adjacent arguments.

For the negative block, put \(P^-(b_-+1)=0\). Since
\(K_j=P^-(j)-P^-(j+1)\),

\[
 \sum_{j=a_-}^{b_-}A_jK_j
 =A_{a_-}P^-(a_-)
 +\sum_{j=a_-+1}^{b_-}(A_j-A_{j-1})P^-(j).
 \tag{R159.10-}
\]

For \(j<0\),

\[
 m_j(x)=m_{j-1}(x)+\mathbf1_{x=-j},
 \tag{R159.11-}
\]

so

\[
 B_j-B_{j-1}=T_j^-+R_j^-.
 \tag{R159.12-}
\]

This proves (R159.5-), with a positive left outer endpoint and positive moving atom. Zero extension is essential here: whenever either adjacent profile argument crosses any component boundary of the profile, the relevant literal term in (R159.7+) or (R159.7-) becomes zero and the transition remains in the difference. Thus disconnected components, component transitions, and support endpoints create no omitted Abel endpoint.

The reconstruction can also be checked coefficient by coefficient. In (R159.10+), an interior \(B_t\) has coefficient
\(P^+(t)-P^+(t-1)=K_t\); the same holds at \(a_+\) and, after combining with the outer line, at \(b_+\). In (R159.10-), an interior \(B_t\) has coefficient
\(P^-(t)-P^-(t+1)=K_t\), with the left outer line supplying the correct coefficient at \(a_-\). Hence no individual Abel piece is estimated and no transition is lost.

### 3.2 Recombination, complete frequency, and the two rows

Apply the preceding identities separately for each \((d,v)\), recombine all six lines to recover

\[
 \sum_{j\in J_+\cup J_-}\widehat B_j(2dv)K(-v^2,-j;c),
\]

and only now enlarge the interior \(v\)-sum to all \(v\bmod H\). Summing (159.BL6) over the hard dyadic set \(J_+\cup J_-\) gives

\[
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}C_d
 \sum_{v\bmod H}\sum_{j\in J_+\cup J_-}
 \widehat B_j(2dv)K(-v^2,-j;c)
 =\mathcal S_{\mathcal L}(V).
 \tag{R159.13}
\]

Removing (R159.8) and (R159.9) once gives (R159.1). This also shows that the factor \(-i(1+i)/(2Nq)\), the \(d\sqrt c\) weight, the divisor sum, and the complete-frequency multiplicity have already been consumed exactly by (159.BL6). No residual factor of \(q\), \(N\), two, or a complementary representative remains in the physical scalar.

### 3.3 Physical-to-selected coordinates

In a nonzero term of \(\mathcal S_{\mathcal L}\), put

\[
 \ell=\frac{x^2-j}{N}.
\]

The factor \(G_N\) makes \(\ell\) an integer and contributes exactly
\(\chi_4(\ell)\). The moving mask gives

\[
 -x\le j=x^2-N\ell\le x-1,
\]

or equivalently

\[
 x^2-x+1\le N\ell\le x^2+x.
 \tag{R159.14}
\]

In particular \(N\ell>0\), so \(\ell\ge1\). Because \(N\ell\) is an integer, (R159.14) is exactly the nearest-cell condition

\[
 x-\frac12\le\sqrt{N\ell}<x+\frac12.
 \tag{R159.15}
\]

Indeed squaring (R159.15) and using integrality changes its lower and upper bounds into precisely (R159.14). A half-integer tie cannot occur because the square of a half-integer is not an integer. Therefore

\[
 x=\kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor
\]

is unique. Conversely every \(\ell\ge1\) for which this \(\kappa(\ell)\) lies in \(\mathcal L\) and \(j=r(\ell)\) lies in \(J_+\cup J_-\) gives exactly one physical pair \((x,j)\). This proves both uniqueness and multiplicity one.

At that pair the literal profile is \(w_U(\ell)\), and

\[
 e(\sqrt{N\ell}-\kappa(\ell))=e(\sqrt{N\ell})
 \tag{R159.16}
\]

only because \(\kappa(\ell)\) is integral. Moreover

\[
 j=r(\ell)\in J_+\cup J_-
 \quad\Longleftrightarrow\quad
 V<|r(\ell)|\le2V.
\]

This retains the strict inner endpoint and closed outer endpoint on both signs. It proves (R159.2).

For the exact residual geometry let

\[
 \delta(\ell)=\sqrt{N\ell}-\kappa(\ell)\in(-1/2,1/2).
\]

Then

\[
 r(\ell)=-\delta(\ell)\bigl(2\kappa(\ell)+\delta(\ell)\bigr).
 \tag{R159.17}
\]

Thus the two defect signs are explicitly

\[
 \mathbf1_{\delta<0}
 \mathbf1_{V<-\delta(2\kappa+\delta)\le2V}
 +
 \mathbf1_{\delta>0}
 \mathbf1_{V<\delta(2\kappa+\delta)\le2V}.
 \tag{R159.18}
\]

The endpoints depend on \(\kappa\). Hence (R159.18) is a variable residual band, not a fixed fractional interval in \(\delta\).

### 3.4 The lift obstruction is genuine

The implication (R159.3) is not a consequence of (159.BL3). Here is a purely finite countermodel to deleting the lift indicator. Take an admissible tuple with odd \(N\) and \(V\ge6\), and let

\[
 s=\lfloor\sqrt V\rfloor+1.
\]

Then \(V<s^2\le2V\). Choose a positive odd integer \(t\), as large as necessary, so that

\[
 \kappa_0=s+tN
\]

lies outside the fixed finite lift \(\mathcal L\) and satisfies \(s^2\le\kappa_0-1\). Put

\[
 \ell_0=\frac{\kappa_0^2-s^2}{N}=2st+t^2N.
\]

Since \(N\) and \(t\) are odd, \(\ell_0\) is odd and
\(\chi_4(\ell_0)=\pm1\). Also

\[
 \kappa_0^2-\kappa_0+1
 \le N\ell_0=\kappa_0^2-s^2
 \le\kappa_0^2+\kappa_0,
\]

so nearest-cell uniqueness gives \(\kappa(\ell_0)=\kappa_0\), while

\[
 r(\ell_0)=s^2\in(V,2V].
\]

Let \(w_U\) be a real constant of sufficiently small height \(a>0\) on
\([\ell_0-1/3,\ell_0+1/3]\) and zero elsewhere. It is zero-extended,
\(\|w_U\|_\infty+\operatorname{Var}(w_U)=3a\), and \(a\) may be chosen to satisfy (159.BL3). In the physical sum, divisibility makes the quotient an integer, so the only possible supported quotient is \(\ell_0\); nearest-cell uniqueness would then force \(x=\kappa_0\notin\mathcal L\). Hence \(\mathcal S_{\mathcal L}(V)=0\). The proposed selected sum without \(\mathbf1_{\kappa(\ell)\in\mathcal L}\), however, contains the single nonzero term

\[
 a\,\chi_4(\ell_0)e(\sqrt{N\ell_0}).
\]

Therefore the unqualified candidate compression is false under the supplied assumptions.

### 3.5 Scalar and raw calibration

Define

\[
 z_{N,V,\mathcal L}(\ell)=\chi_4(\ell)e(\sqrt{N\ell})
 \mathbf1_{\kappa(\ell)\in\mathcal L}
 \mathbf1_{V<|r(\ell)|\le2V}.
\]

Then \(\mathcal S_{\mathcal L}=\sum_{\ell\ge1}w_U(\ell)z_{N,V,\mathcal L}(\ell)\). Discrete Abel summation in \(\ell\), using that the variation of the integer samples is no larger than the real variation, shows that a sufficient uniform raw estimate is

\[
 \sup_{u\le v}
 \left|\sum_{u\le\ell\le v}z_{N,V,\mathcal L}(\ell)\right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
 \tag{R159.19}
\]

After splitting \(\varepsilon\), (159.BL3) times (R159.19) gives the scalar target (R159.4). Conversely, because real interval-step profiles have bounded variation comparable to their height, a scalar theorem uniform over every profile allowed by (159.BL3) would imply the corresponding interval version of (R159.19), up to constants and the usual redistribution of \(X^\varepsilon\). Thus \(M^{3/4}X^\varepsilon\) is the correct raw target.

If \(C\) is only the cardinality of the active selected support, the unsigned estimate is merely

\[
 |\mathcal S_{\mathcal L}(V)|
 \le \|w_U\|_\infty C
 \ll_\varepsilon M^{-3/4}C X^\varepsilon.
 \tag{R159.20}
\]

Even if an additional argument supplied \(C\ll_\varepsilon\min(M,V)X^\varepsilon\), this would be capacity, not signed cancellation. It reaches the target only in the conditional capacity range
\(\min(M,V)\ll M^{3/4}X^{O(\varepsilon)}\). No support hypothesis or cardinality theorem establishing that premise is present here, so (R159.20) is not an owner-complete \((N,M,V)\)-range result. In particular, after restoring the atom scale \(M^{-3/4}\), the unresolved loss in the larger-capacity region is the factor
\(\min(M,V)/M^{3/4}\).

### 3.6 What the character and a Fourier expansion do—and do not—supply

The character has the exact additive decomposition

\[
 \chi_4(\ell)=\frac{e(\ell/4)-e(-\ell/4)}{2i}.
 \tag{R159.21}
\]

If, after first retaining (R159.18), one Fourier-expands its fractional variable with an integer mode \(h\), the original phase and that mode combine into

\[
 e\bigl((h+1)\sqrt{N\ell}\bigr),
\]

and (R159.21) shifts the two phases to

\[
 e\bigl((h+1)\sqrt{N\ell}+\ell/4\bigr),
 \qquad
 e\bigl((h+1)\sqrt{N\ell}-\ell/4\bigr).
 \tag{R159.22}
\]

Thus the apparently dangerous mode \(h=-1\) is not a genuine zero mode: it retains the \(\pm\ell/4\) character shift. That algebraic control passes.

It does not prove (R159.19). The exact mask to be expanded is

\[
 g_{\kappa,V}(u)=
 \mathbf1_{V<|-u(2\kappa+u)|\le2V},
 \qquad -\tfrac12<u<\tfrac12,
\]

whose endpoints and Fourier coefficients depend on \(\kappa\). A fixed fractional band is therefore not equal to the literal mask. Moreover a finite Fourier truncation of this discontinuous function has boundary error at the hard surfaces \(|r|=V\) and \(|r|=2V\); the usual pointwise Fourier value at a jump also does not encode the required strict/closed convention. The statement supplies neither a majorant/minorant boundary count nor uniform estimates for all the nonzero phases (R159.22) with the \(\kappa\)-dependent coefficients. Bounding those errors by the number of active points returns (R159.20) and restores the same missing power. Hence shifted-zero-mode cancellation is a necessary algebraic observation, not the missing signed theorem.

## 4. First doubtful or unproved step

The first invalid step is deletion of
\(\mathbf1_{\kappa(\ell)\in\mathcal L}\) when passing from the finite physical lift to the proposed all-\(\ell\) selected sum. It requires a support/lift-containment hypothesis absent from the literal problem, and Section 3.4 gives an admissible countermodel.

If that source defect is repaired by explicitly assuming (R159.3), the next unproved step is the raw signed estimate (R159.19). Neither support cardinality nor the mean-zero identity for \(\chi_4\) proves it. Any proposed Fourier proof must additionally give, with exact hard endpoints, a uniform truncation error and nonzero-mode estimates for the variable family \(g_{\kappa,V}\). Those data are also absent. Accordingly this report proves no global target and no new strict owner-complete parameter range.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `literal_full_Abel_six_line_package` | Pass. Equations (R159.5+)--(R159.7-) give exactly three lines on each sign. |
| `positive_negative_signs_and_outer_endpoints` | Pass. The positive endpoint is \(b_+\), the negative endpoint is \(a_-\), and both moving atoms have positive sign. |
| `profile_difference_and_transition_reconstruction` | Pass. Equations (R159.7+) and (R159.7-) retain both literal adjacent profile-phase values; zero extension retains every component transition. |
| `all_d_all_v_complete_frequency_normalization` | Pass. Recombination is per \((d,v)\); (R159.13) uses exactly the prefactor in (159.BL6), with no extra factor. Both complementary representatives are retained. |
| `zero_and_Nyquist_whole_row_subtraction` | Pass. The rows (R159.8)--(R159.9) are removed once, after full reconstruction. No row theorem is applied to an Abel subpiece. |
| `physical_lift_and_nearest_cell_uniqueness` | Nearest-cell uniqueness and multiplicity one pass. Removal of the lift indicator fails under the stated hypotheses; Section 3.4 is an exact countermodel. |
| `quotient_profile_not_boundary_profile` | Pass. The selected scalar contains literal \(w_U(\ell)\); the two isolated trace profiles remain confined to (R159.6+) and (R159.6-). |
| `integral_phase_shift` | Pass. Equation (R159.16) uses only the integrality of \(\kappa(\ell)\). |
| `variable_residual_band` | Pass algebraically. Equations (R159.17)--(R159.18) retain both signs and \(\kappa\)-dependent endpoints; no fixed-band replacement is made. |
| `chi4_shifted_zero_mode` | Pass algebraically. Equation (R159.22) shows that \(h=-1\) leaves the nonzero additive shifts \(\pm1/4\). This alone is not a signed bound. |
| `Fourier_truncation_and_boundary_errors` | Open/obstructed. No exact hard-endpoint truncation control or boundary-count theorem is supplied; an unsigned error restores the capacity loss. |
| `N_M_V_power_and_scalar_target` | Pass as calibration, not as a bound. The normalized scalar target is \(X^\varepsilon\), the BV-dual raw target is \(M^{3/4}X^\varepsilon\), and the closed rows are \(O(M^{-1/4}X^\varepsilon)\). |
| `upper_capacity_vs_signed_bound` | Fail as a target proof. Cardinality gives only (R159.20) and does not provide the signed estimate (R159.19). |
| `external_scalar_and_downstream_scope` | Pass. Complete-frequency inversion leaves precisely (R159.2), and no claim is made beyond this paired-interior matrix. |

No numerical test was used: every control above is exact algebra or a stated analytic obstruction.

## 6. Dependencies and exact artifacts used

Mathematical dependencies used:

1. `protocol.md`.
2. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/blind_statement.md`, specifically (159.BL1)--(159.BL7).
3. The assignment and output contract in `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/briefs/blind_full_abel_rederivation.md`.

No proof graph, strategy file, conductor seed, nonblind Round-159 artifact, sibling report, proof draft, prior derivation, web source, or computation was inspected or used.

## 7. Recommended state effect

**Revise, with no proof-state promotion.** Retain (R159.5+)--(R159.13) as candidate evidence for the exact six-line reconstruction and whole-row subtraction. Revise the proposed selected compression to (R159.2), or add and prove the explicit containment hypothesis (R159.3) before deleting its lift indicator. Do not promote the scalar target or any owner-complete range: after that repair the raw signed estimate (R159.19), including variable-mask Fourier truncation and hard-boundary control, remains open. The conclusion is confined to the full paired-interior \(D=d=L=1\) matrix. It does not modify either isolated-trace statement and does not transfer to \(D>1\), \(L>1\), generic \(t=1\), \(t\ge2\), cross terms, another M1 or M2 owner, endpoint uniformity, M9, the bridge, the final target, or exponent owners.
