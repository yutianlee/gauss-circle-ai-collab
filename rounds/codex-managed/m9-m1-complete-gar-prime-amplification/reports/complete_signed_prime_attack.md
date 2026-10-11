# 1. Result

Round224, m9-m1-complete-gar-prime-amplification; complete_signed_prime_attack; 2026-09-28.

**complete_gar_amplification_no_new_bound.** The complete split-prime identity, including its actual angular commutator, is derived below. The attempted completed-row Cauchy estimate returns the inherited complete bound
\[
|G_X|\ll_\epsilon X^{1/12+\epsilon},
\]
hence physical total active M1 at \(X^{1/3+\epsilon}\). It gives no improvement.

A second, explicitly identified positive closure of the same joint expression has certificate between \(cX^{1/8}\) and \(CX^{1/8}\log(2X)\), uniformly over the tested amplifier family. This lower price uses actual profiles and remains after the fixed nonlower complement is paid. Physically it costs \(X^{3/8}\), worse than the inherited estimate. It is not a lower bound for the signed commutator, \(G_X\), or any discrepancy.

The missing estimate is the complete signed main-minus-commutator correlation, including its nonconjugated real-part channel. No external source is imported, no experiment is run, and no successor is started.

# 2. Exact statement and hypotheses

Let \(X\ge2\) be real, \(R=X^{1/4}\), \(Y=\sqrt X\), \(y=\lfloor Y\rfloor\), \(M=\lfloor16Y\rfloor\),
\[
D_j=2^{-j}y,\qquad H_j=\lfloor D_j/R\rfloor,\qquad
b_j(h)=1_{h\le H_j}\Phi(h/(H_j+1)).
\]
All labels, the finite denominator partition, top hard sample and stars are those in the supplied packet. Set
\[
d(h,q)=2\sqrt{Xh/q},\quad
A(h,q)=A_X(h,q)=\sum_jb_j(h)[w_j(d(h,q))]^*,\quad
c_A(n)=\sum_{hq=n}\chi_4(q)A(h,q).
\]
This real coefficient retains even \(h\); even \(q\) has character zero. Define
\[
F(n)=1_{1\le n\le M}n^{-3/4}e(\sqrt{Xn}),\qquad
S_A(F)=\sum_nc_A(n)F(n),\qquad
G_X=\Re\{e(1/8)S_A(F)\}.
\]
For complete lower-owner accounting one may instead use
\(F_V(n)=V_{\rm low}(n/Y)F(n)\), with the fixed accepted cutoff. Write \(G_V\) for its real projection. Accepted120 pays \(G_X-G_V=O_\epsilon(X^\epsilon)\).

The **one tested amplifier family** is the unit-weight set
\[
\mathcal P(P)=\{p\text{ prime}:P<p\le2P,\ p\equiv1\pmod4\},\qquad
K=|\mathcal P(P)|>0.
\]
Initially \(2\le P\le M\). All bounds keep \(K\) exact; no prime-count asymptotic or lower bound is assumed. Intervals with \(K=0\) are not amplifiers. The limiting choice of primes \(p>M\) is separately controlled below, not introduced as a second family.

The target remains \(|G_X|\ll_\epsilon X^\epsilon\) for every real \(X\). It is total M1, not a uniform individual block estimate or the full quarter theorem.

# 3. Derivation and complete quantitative attempt

**Allocation, with every repeated-prime overlap.** For a split prime define
\[
A_{10}(h,q)=A(ph,q),\quad A_{01}(h,q)=A(h,pq),\quad
A_{11}(h,q)=A(ph,pq),\quad
\Delta_pA=A_{10}+A_{01}-2A.
\]
Every factorization \(ab=pn\) has \(p\mid a\) or \(p\mid b\). The intersection, where both hold, is parametrized by \(hq=n/p\). Because \(\chi_4(p)=1\), inclusion-exclusion gives
\[
c_A(pn)=c_{A_{10}}(n)+c_{A_{01}}(n)
-1_{p\mid n}c_{A_{11}}(n/p).
\tag{1}
\]
This does not require \(p\nmid n\). Therefore
\[
\boxed{E_{p,A}(n):=c_A(pn)+1_{p\mid n}c_A(n/p)-2c_A(n)
=c_{\Delta_pA}(n)+1_{p\mid n}c_{A-A_{11}}(n/p).}
\tag{2}
\]
The overlap is not a negligible prime-power error.

For clarity, the actual shifted symbols are exactly
\[
\begin{aligned}
A_{10}(h,q)&=\sum_j b_j(ph)[w_j(\sqrt p\,d(h,q))]^*,\\
A_{01}(h,q)&=\sum_j b_j(h)[w_j(d(h,q)/\sqrt p)]^*,\\
A_{11}(h,q)&=\sum_j b_j(ph)[w_j(d(h,q))]^*.
\end{aligned}
\tag{3}
\]
Thus \(A-A_{11}\) retains the full difference \(b_j(h)-b_j(ph)\) at the unchanged spatial argument. The other two terms shift that argument and its hard boundary. No derivative estimate or smallness in \(1/p\) follows from these identities. All \(D_j,H_j\) remain at the original \(X\). In particular, changing the radial phase to \(pX\) does not change these symbols to \(A_{pX}\): that coefficient would have new floor-dependent scales, heights and spatial profiles.

**Adjoint and literal radial costs.** Finite reindexing gives
\[
T_p^*F(m)=1_{p\mid m}F(m/p)+F(pm),
\]
\[
\begin{aligned}
T_p^*F(m)={}&p^{3/4}m^{-3/4}1_{p\mid m}1_{m\le pM}
 e(\sqrt{(X/p)m})\\
&+p^{-3/4}m^{-3/4}1_{m\le\lfloor M/p\rfloor}
 e(\sqrt{(pX)m}).
\end{aligned}
\tag{4}
\]
For \(F_V\), the first and second lines additionally contain
\(V_{\rm low}(m/(pY))\) and \(V_{\rm low}(pm/Y)\), respectively. These are different cutoffs. The divisibility projector and both amplitude powers are compulsory.

Set
\[
U_p=S_A(T_p^*F_V),\qquad
V_p=\sum_nE_{p,A}(n)F_V(n),\qquad J_p=U_p-V_p.
\]
Equations (1)–(4) imply
\[
2KG_V=\Re\left\{e(1/8)\sum_{p\in\mathcal P}J_p\right\}.
\tag{5}
\]
The commutator remains with the main term inside this single real part.

A useful joint allocation form, obtained after cancelling the duplicate \(A(h,q)F_V(phq)\) terms, is
\[
\begin{aligned}
J_p=\sum_{h,q}\chi_4(q)\{&
 A(h,q)1_{p\mid hq}F_V(hq/p)
-A(ph,q)F_V(hq)\\
&-A(h,pq)F_V(hq)+2A(h,q)F_V(hq)
+A(ph,pq)F_V(phq)\}.
\end{aligned}
\tag{6}
\]
All five terms in (6) must stay together for a signed estimate. Splitting the first divisibility condition into \(p\mid h\) or \(p\mid q\), subtracting their intersection, and reindexing cancels the second, third and fifth terms exactly. Hence
\[
J_p=2S_A(F_V)\qquad\text{for each }p.
\tag{7}
\]
This is the exact self-return of the completed rows, not a theorem saying that every use of Hecke amplification is impossible.

**Attempted complete cross-prime estimate.** Let \(\gamma=e(1/8)\) and \(j_p=\Re(\gamma J_p)\). The exact real quadratic form is
\[
\begin{aligned}
\mathscr Q_{\mathcal P}
&=\sum_{p,r\in\mathcal P}j_pj_r\\
&=\frac12\Re\sum_{p,r}
\{(U_p-V_p)\overline{(U_r-V_r)}
+e(1/4)(U_p-V_p)(U_r-V_r)\}\\
&=4K^2G_V^2.
\end{aligned}
\tag{8}
\]
Both products retain main-main, main-commutator, commutator-main and commutator-commutator terms. The second product is the nonconjugated sum-phase channel; estimating only the first is not a lossless polarization of the stated real target.

Completed-row Cauchy gives
\[
\left|\sum_pj_p\right|^2\le K\sum_pj_p^2.
\]
By (7), every \(j_p=2G_V\), so this is equality. The cross-prime terms are \(4G_V^2\), not independent fluctuations. No averaging over \(X/p\) or \(pX\) is licensed by (4).

Here the inherited complete bound can be restored quantitatively. On each actual physical shell the accepted estimates give
\[
|B_1(D,L;X)|\ll_\epsilon X^\epsilon
 \min\{D,\ 1+D/L,\ \sqrt{LX/D}\}.
\]
If \(D\le X^{1/3}\), use the first entry. Otherwise use \(D/L\) when
\(L\ge DX^{-1/3}\), and \(\sqrt{LX/D}\) when \(L<DX^{-1/3}\).
Every shell is \(O(X^{1/3+\epsilon})\); all logarithmic labels, the hard top, owned transform errors and inactive bottom are included. The accepted reconstruction therefore gives
\[
|G_X|+|G_V|\ll_\epsilon X^{1/12+\epsilon}.
\tag{9}
\]
Consequently the **proved complete cross-prime bound** from this closure is
\[
\mathscr Q_{\mathcal P}\ll_\epsilon K^2X^{1/6+\epsilon},
\tag{10}
\]
uniformly in the tested \(P,K\). Dividing its square root by \(2K\) recovers (9), with no amplifier saving. The target would instead require
\(\mathscr Q_{\mathcal P}\ll_\epsilon K^2X^\epsilon\). Equation (8) shows precisely why that desired estimate has not been supplied by prime-row orthogonality.

**Full positive certificate and parameter optimization.** The actual profile bound is \(|A(h,q)|\le C\), uniformly in real \(X\), by bounded overlap of the fixed dyadic profiles and bounded \(\Phi\). Moreover every nonzero atom satisfies
\[
hq\le16Y,\quad
A_{10}\ne0\text{ or }A_{01}\ne0\Longrightarrow phq\le16Y,\quad
A_{11}\ne0\Longrightarrow p^2hq\le16Y.
\tag{11}
\]
Indeed \(d(h,q)/D_j\ge1/2\) and \(h\le D_j/R\) imply the first support statement; the others apply it to the shifted arguments. These support restrictions are used in the following bounds, not discarded.

For \(z\ge1\), elementary divisor summation gives
\[
\sum_{n\le z}\tau(n)n^{-3/4}\ll z^{1/4}\log(2z).
\tag{12}
\]
Also \(\tau(pn)\le2\tau(n)\). Thus the original main term alone obeys
\[
\frac1K\left|\sum_pU_p\right|
\ll M^{1/4}\log(2M)(P^{-1/4}+P^{-1}),
\tag{13}
\]
with fixed cutoff seminorms absorbed. The first term comes from
\(\sum_{n\le M/p}c_A(pn)F_V(n)\); the second comes from
\(\sum_{n\le M/p}c_A(n)F_V(pn)\).
For \(M\asymp X^{1/2}\), the optimistic main-term price matches the inherited \(M^{1/6}\) scale only near \(P\ge M^{1/3}\). This says nothing favorable about its commutator.

To price a complete closure, define \(\mathscr C_{\mathcal P}(F_V)\) by replacing each of the five individual summands inside braces in (6) by its absolute value, multiplying by \(|\chi_4(q)|\), summing over \(h,q,p\), and dividing by \(2K\). This is a genuine upper certificate for \(|G_V|\). It is the exact point where the original character signs, radial phases and cancellation between the five terms are lost.

By (11)–(12), for each \(p\), the five absolute sums have respective upper prices
\[
\ll\log(2M)\left\{
(M/p)^{1/4},\ (M/p)^{1/4},\ (M/p)^{1/4},\
M^{1/4},\ M^{1/4}p^{-5/4}\right\}.
\tag{14}
\]
For the first, write \(hq=pn\) and use \(\tau(pn)\le2\tau(n)\).
For the last, \(hq\le M/p^2\) and \(|F_V(phq)|\ll p^{-3/4}(hq)^{-3/4}\).
Sums with an upper endpoint below1 are empty. Every overlap and dilation is therefore paid. Averaging gives
\[
\mathscr C_{\mathcal P}(F_V)
\ll M^{1/4}\log(2M)(1+P^{-1/4}+P^{-5/4}).
\tag{15}
\]

There is also an **actual-symbol lower price** for this named certificate. Choose one fixed small \(c>0\) so that \(V_{\rm low}=1\) on \([c,2c]\), and so that for \(q\in[cY,2cY]\),
\[
d(1,q)=2\sqrt{X/q}\asymp c^{-1/2}R
\]
lies above the inactive bottom and far below the hard top for all sufficiently large real \(X\). Any supported \(D_j\) then satisfies \(D_j\ge(2/3)d(1,q)\), hence
\[
\frac1{H_j+1}<\frac R{D_j}\ll\sqrt c.
\]
The accepted small-argument expansion \(\Phi(u)=1+O(u^2)\), and the exact nonnegative telescoping partition at this interior point, give
\[
A_X(1,q)=1+O(c)\ge\frac12
\tag{16}
\]
after fixing \(c\) sufficiently small. Floors do not affect the strict inequality \(H_j+1>D_j/R\). No endpoint star is encountered in this buffer.

The fourth term in (6), by itself inside the **positive certificate**, therefore contributes
\[
\begin{aligned}
\mathscr C_{\mathcal P}(F_V)
&\ge \frac1{2K}\sum_p
 \sum_{\substack{cY\le q\le2cY\\q\ {\rm odd}}}
 2A_X(1,q)q^{-3/4}\\
&\gg Y^{1/4}\asymp M^{1/4}.
\end{aligned}
\tag{17}
\]
Only the elementary count of odd integers is used. There is no prime-count input, no phase alignment assumption, and no lower bound for \(c_A(n)\) after its signed divisor sum. This is also why (17) is not a lower bound for the grouped commutator.

Equations (15)–(17) price the **entire named positive closure** at
\[
M^{1/4+o(1)}=X^{1/8+o(1)}
\]
for every nonempty amplifier interval. Optimizing \(P\) cannot reduce the untouched term1 in (15) or the actual lower price (17). A fixed nonlower subtraction does not remove this control, since \(c\) is chosen inside its remaining lower cutoff. A different proof may exploit cancellation there; this certificate has discarded it.

For primes \(p>M\), all shifted coefficient terms and \(U_p\) vanish:
\(E_{p,A}(n)=-2c_A(n)\) on the original support. The whole target then sits in the correction. Taking an arbitrarily large amplifier is therefore not a loophole. The best complete result of the attempt is the minimum of the inherited (9) and the weaker (15), namely unchanged \(X^{1/12+\epsilon}\).

**All owners and physical restoration.** The target is recombined before amplification. The nonlower part is paid once by120; every scale in the lower cutoff remains in \(F_V\). This report does not apply121 flattening or integerization to discard any term. If that alternate lower representation is used later, its physical \(O(X^{1/4+\epsilon})\) errors remain compulsory. No narrow \(D=d=L=1\) estimate from159 pays the missing \(D>1,L>1\), generic \(t=1\), original \(t\ge2\), or independent cross contribution.

Finally,
\[
M_{1,\mathrm{active}}^{\mathrm{stat}}
=-\frac4\pi X^{1/4}G_X+O(\log^2X).
\]
The positive closure costs \(X^{3/8+\epsilon}\); (9) restores the stronger inherited \(X^{1/3+\epsilon}\), including the already paid bottom and transform errors. No M2 owner, endpoint obligation, complete moment or qualified external benchmark changes.

# 4. First doubtful or unproved step

The first missing input is a coefficient-sensitive bound for the complete expression (5), or equivalently its real quadratic form (8), stronger than (10), before replacing the signed mixed terms by separate positive norms. For the quarter-scale total-M1 target the required bound is
\[
\left|\Re\left\{e(1/8)\sum_{p\in\mathcal P}
 \left[S_A(T_p^*F_V)-\sum_nE_{p,A}(n)F_V(n)\right]\right\}\right|
\ll_\epsilon KX^\epsilon.
\tag{18}
\]
All symbols in (18) are fixed at the prescribed \(X\). This is the complete still-open inequality, not a newly proved reduction that enables a gain.

The shifted phases in the main term do not introduce independent oscillation into the correction: its \(c_{\Delta_pA}(n)F_V(n)\) terms share the same radial phase at each \(n\). A pointwise theorem cannot be obtained by assigning the dilated main terms to averages or high-value sets at different centers. Completed-row Cauchy self-returns exactly; the tested expanded positive norm has the fully priced loss (17). Neither observation excludes a genuinely different signed estimate of (18).

# 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Split-prime constant profile | For \(A\equiv1\), \(c_A=1*\chi_4\). At \(n=p^an_0\), \(p\nmid n_0\), the local factors give \(c_A(pn)+c_A(n/p)=2c_A(n)\), including \(a=0\); (2) vanishes exactly. |
| Repeated-prime overlap | The intersection in (1) has \(hq=n/p\) and symbol \(A(ph,pq)\), for every valuation. It is subtracted once, then retained in (2) and (6). |
| Prime2 and inert primes | Even \(q\) remains zero and even \(h\) is retained. At2 the allocation is \(c_A(2n)=c_{A(2h,q)}(n)\), not the split-prime eigenvalue2 relation. For an inert prime the unweighted eigenvalue is0; it is not included in this amplifier. |
| Actual commutator | Exact formulas (3), unchanged heights, moved spatial arguments and all hard stars retained; no \(1/p\) smallness asserted. |
| Radial dilation | Both powers, both phases, divisibility, floor cutoffs and shifted \(V_{\rm low}\) arguments appear in (4). |
| Real pairing | Both original signs are represented by \(\Re e(1/8)\); (8) includes the difference- and sum-phase channels. A complex-modulus bound would be stronger. |
| False prime orthogonality | Even the enlarged constant-profile control \(F=1_{\{1\}}\) has every completed real row equal to \(2\Re e(1/8)\), so its off-diagonal row products do not vanish. This is an algebraic control, not an actual-GAR lower bound. |
| Actual positive control | (16)–(17) use actual profiles at \(h=1\), odd \(q\asymp c\sqrt X\), uniformly for real \(X\). They lower-bound only the explicitly expanded certificate. |
| All ranges and errors | The full lower cutoff, the paid nonlower complement, finite upper cutoff, all dyadic labels, stars, bottom and physical reconstruction remain. |
| Gain comparison | \(X^{1/8}\) normalized certificate is worse than inherited \(X^{1/12}\); \(X^{3/8}\) physical is worse than \(X^{1/3}\). Neither is an actual lower bound. |

No source theorem or numerical computation is used. Statement-only finite verification belongs to the separately assigned blind role; this report does not claim that status or inspect its output.

# 6. Dependencies and provenance

NONBLIND selected-context discovery report. This reused agent retains round217–223 history, including authorship of the223 multiplicative-source report and its strategy review. It is not history-free. No current sibling report or blind packet was read. The conductor supplied the baseline clarification, consistent with the already authorized graph. Only this assigned report is written.

Exact dependency hashes at report preparation:

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 8e6526a9fd822d43f5ccfe65c67ec4db1f131e1c38e3e6eb953b8c0ddc915cf5 |
| strategy/round224_complete_gar_split_prime_amplification.md | c1f2364a958d484f523745bc06711aaebaf049c1c989f73639c55a48590da9a5 |
| Current224 briefs/conductor_actual_gar_interface.md | f5ea5afa70e8315179d56d066303bb17b1280b4fabd2bbfb5867aece531bd803 |
| Current224 briefs/complete_signed_prime_attack.md | 61e86493b46488a45ee9431e4eda6a42c5afed98cb3a18e631e97126561b4290 |
| strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md | a0c75c5e2ef4ea45df4e388e3497d5be5133d6d49c7d7a2d71c166f11dd9dd33 |
| rounds/codex-managed/gc-full-goal-signed-source-review/synthesis.md | 3f97b688827680d7c733116ebc6bd0107b5ec1af4d2df5258fc0ce1cb0b5ae78 |
| rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/candidates/conductor_terminal_height_interface_completion.md | 712a31a8b83263cf5f975177a34058d3449d920a36d2fa088d73fde4aa49c26d |
| rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/candidates/conductor_profile_flattening_and_integer_phase.md | 6a60d62ff42c5b764a79e4303eb50b8a780572ef4ac6e635ff9406e9192d095d |
| proofs/kernels/m9_m1_d1_full_abel_common_profile_recombination.md | a60cfaf54611957fbd359bc07783f95886a0549150f53277104e3c508041f0f2 |
| state/best_proof_draft.md | 65989358d00f0ecf7c4d385ea58bfad09eaa026af98924266207c5f8af872f00 |
| rounds/codex-managed/m9-m1-global-angular-shifted-correlation/synthesis.md | e3dd9e59aa2121d2f76189959247f4b058626e89090cba8e84519aa44d364ac0 |
| rounds/codex-managed/m9-m1-reflected-mode-correlation/synthesis.md | 31661528a9648120489ad3117073323321ac106a2651b7b7c623dcd0d548761c |

“Current224” denotes rounds/codex-managed/m9-m1-complete-gar-prime-amplification. Graph dependencies used in particular are H4-Phi-regularity, M9-M2-dyadic-weight-nondegeneracy, M9-M1-terminal-frequency-divisor-bound, M9-M1-ordered-resonance-cell-decomposition, M9-direct-menu-one-third-optimality, M9-M1-global-angular-recombination, the120 nonlower theorem and the lower owner's scope through159. Their acceptance comes from the graph, not the historical candidate headings.

# 7. Recommended state effect

**No change** to any complete analytic estimate or exponent. Retain, after the assigned reviews, only the exact allocation/adjoint algebra and the scoped failures of the completed-row and expanded positive closures. Reject deletion of the commutator, repeated-prime overlap, nonconjugated real channel, or changed-center cost.

The complete target (18) remains open. This attempt supplies neither a complete GAR gain nor an essential reduction demonstrated to enable one. Do not prolong it into another unestimated angular or prime sector. The conductor owns round closure and any later strategy; this task ends with this report and its final hash.

