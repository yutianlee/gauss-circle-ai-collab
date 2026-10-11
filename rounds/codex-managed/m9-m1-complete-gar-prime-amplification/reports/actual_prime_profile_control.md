# Round 224: actual prime-profile commutator control

## 1. Result

**Complete commutator identity and actual-symbol certificate obstruction; no new GAR bound.** The fixed-\(X\) profile does not satisfy the constant-profile split-prime eigenrelation. Its exact correction includes two angular dilations, a height change and a repeated-prime overlap. All are retained below.

For every split prime \(p\equiv1\pmod4\), an explicitly proved set of actual lower-radial incidences has commutator
\[
 A_X(ph,q)+A_X(h,pq)-2A_X(h,q)\le-\tfrac12.
\]
It yields a lower bound \(cX^{1/8}\) for the complete **incidencewise absolute correction certificate**, uniformly in \(p\). The matching elementary upper price is \(O(X^{1/8}\log X)\). Averaging any nonempty finite split-prime set and dividing by twice its size preserves that certificate floor. Physical restoration costs \(X^{3/8+o(1)}\), worse than the inherited actual total-M1 bound \(X^{1/3+\varepsilon}\), equivalently \(|G_X|\ll X^{1/12+\varepsilon}\).

This is an actual-symbol control, not an alternate array. It is nevertheless **not** a lower bound for the divisor-aggregated correction, its signed radial sum or its real projection. Cancellation inside those quantities may occur. The complete joint signed inequality remains unproved. For \(p>N_X=\lfloor16\sqrt X\rfloor\), the adjoint main is exactly zero and the correction equals \(-2C_X^*(n)\) on the tested range: an explicit self-return.

This report independently derives the permitted interface. It is nonblind because this agent has prior campaign history, including the Round 223 frontier/source report. No current sibling or blind packet was read, no source theorem was imported, and no experiment or successor work was performed.

## 2. Exact statement and hypotheses

Put
\[
 R=X^{1/4},\quad Y=\sqrt X,\quad y=\lfloor Y\rfloor,\quad
 D_j=2^{-j}y,\quad H_j=\lfloor D_j/R\rfloor,\quad
 N_X=\lfloor16Y\rfloor.
\]
Use the fixed accepted finite nonnegative telescoping denominator partition, its inactive bottom, unique hard top and literal stationary stars. For positive integers \(h,q\), let
\[
 B_j(h)={\bf1}_{h\le H_j}\Phi(h/(H_j+1)),\qquad
 d_X(h,q)=2\sqrt{Xh/q},
\]
\[
 A(h,q)=A_X(h,q)=\sum_j B_j(h)[w_j(d_X(h,q))]^*,\qquad
 c(n)=\sum_{hq=n}\chi_4(q)A(h,q).
 \tag{1}
\]
Terms with \(H_j=0\) are empty. The real coefficient \(A\) is at the original prescribed \(X\) everywhere in this report. Write
\[
 F_X(n)={\bf1}_{1\le n\le N_X}n^{-3/4}e(\sqrt{Xn}),\qquad
 G_X=\Re\{e(1/8)\sum_n c(n)F_X(n)\}.
 \tag{2}
\]
The complete target is \(|G_X|\ll_\varepsilon X^\varepsilon\) for every real \(X\ge2\). Both original frequency signs are represented by this real projection.

For a prime \(p\), set \(\eta=\chi_4(p)\), and use the convention \(c(n/p)=0\) unless \(p\mid n\). Define
\[
 E_{p,\eta}(n)=c(pn)+\eta c(n/p)-(1+\eta)c(n).
 \tag{3}
\]
The amplifier uses split primes, hence \(\eta=1\), and \(E_p=E_{p,1}\). Its prime set \(\mathcal P\) is an arbitrary nonempty finite set; \(M=|\mathcal P|\) is kept exact. No prime-count estimate is assumed.

The adverse control concerns the explicitly defined nonnegative certificate
\[
 \begin{split}
 \mathfrak C_p(X)=\sum_{1\le n\le N_X}n^{-3/4}
 \bigg[&
 \sum_{hq=n}|\chi_4(q)|
 |A(ph,q)+A(h,pq)-2A(h,q)|\\
 &+{\bf1}_{p\mid n}\sum_{hq=n/p}|\chi_4(q)|
 |A(h,q)-A(ph,pq)|\bigg].
 \end{split}
 \tag{4}
\]
It majorizes \(|\sum_n E_p(n)F_X(n)|\), but is generally larger. For sufficiently large real \(X\), with constants depending only on accepted profiles and the fixed lower cutoff,
\[
 c_0X^{1/8}\le\mathfrak C_p(X)
 \ll X^{1/8}\log(2X)\qquad(p\equiv1\pmod4).
 \tag{5}
\]
The same lower bound holds if (4) is multiplied by the exact nonnegative lower cutoff \(V_{\rm low}(n/Y)\), since the constructed incidences lie where that cutoff is one. Finite bounded \(X\) may be absorbed into upper-bound constants; the lower assertion is asymptotic.

## 3. Derivation

### 3.1 Exact allocation and all prime-power overlaps

Every factorization of \(pn\) has \(p\) in its first factor, its second factor, or both. Inclusion-exclusion gives
\[
 \begin{split}
 c(pn)={}&\sum_{hq=n}\chi_4(q)A(ph,q)
 +\eta\sum_{hq=n}\chi_4(q)A(h,pq)\\
 &-\eta{\bf1}_{p\mid n}\sum_{hq=n/p}\chi_4(q)A(ph,pq).
 \end{split}
 \tag{6}
\]
Consequently
\[
 \begin{split}
 E_{p,\eta}(n)={}&
 \sum_{hq=n}\chi_4(q)
 [A(ph,q)-A(h,q)+\eta(A(h,pq)-A(h,q))]\\
 &+\eta{\bf1}_{p\mid n}\sum_{hq=n/p}\chi_4(q)
 [A(h,q)-A(ph,pq)].
 \end{split}
 \tag{7}
\]
This is an identity for the complete coefficient, with no assumption \(p\nmid n\).

For verification at every valuation, write \(n=p^rm,\ (p,m)=1\). Then
\[
 c(p^rm)=\sum_{de=m}\chi_4(e)
 \sum_{a=0}^r\eta^{r-a}A(p^ad,p^{r-a}e).
 \tag{8}
\]
In (8), the zero-th power is \(\chi_4(p^0)=1\), including \(p=2\). The overlap in (6) corresponds exactly to the interior allocations \(1\le a\le r\) of \(p^{r+1}\), each subtracted once. When \(A=1\), the geometric coefficient sum in (8) gives
\(c(pn)+\eta c(n/p)=(1+\eta)c(n)\). This checks the algebra, not applicability of the constant coefficient to GAR.

For \(p\equiv3\pmod4\), the eigenvalue \(1+\eta\) is zero; it supplies no division by two. For \(p=2\), \(\eta=0\), and every allocation with an even second factor vanishes. Formula (6) becomes
\(c(2n)=\sum_{hq=n}\chi_4(q)A(2h,q)\), while
\(E_{2,0}(n)=\sum_{hq=n}\chi_4(q)[A(2h,q)-A(h,q)]\).
All powers of two in the original first factor remain. The split-prime amplifier neither discards nor separately solves the even-\(n\) branches.

### 3.2 Actual angular shifts, heights, floors and stars

For \(d=d_X(h,q)\), the exact comparison is
\[
 \begin{array}{c|c|c}
 \text{profile} & \text{spatial argument} & \text{height weight}\\ \hline
 A_X(h,q)&d&B_j(h)\\
 A_X(h,pq)&d/\sqrt p&B_j(h)\\
 A_X(ph,q)&\sqrt p\,d&B_j(ph)\\
 A_X(ph,pq)&d&B_j(ph).
 \end{array}
 \tag{9}
\]
All \(D_j,H_j\), active indices and \(X\)-dependent boundaries remain unchanged. In particular the repeated-prime overlap has the same spatial argument and top star, but a different height.

Extend \(\Phi\) by zero for arguments at least one. Because \(\Phi(1)=\Phi'(1)=0\), for integer \(h\ge1\) the exact height weight is \(\Phi(h/(H_j+1))\) under this extension, including \(h=H_j+1\). Thus
\[
 |B_j(ph)-B_j(h)|
 \ll\min(1,(p-1)h/(H_j+1)).
 \tag{10}
\]
This includes the height cutoff crossing; it does not change \(H_j\) to \(pH_j\).

For split primes the first bracket in (7) can be written, with stars kept in each evaluation, as
\[
 \sum_j\left[
 (B_j(ph)-B_j(h))w_j^*(d)
 +B_j(ph)(w_j^*(\sqrt p\,d)-w_j^*(d))
 +B_j(h)(w_j^*(d/\sqrt p)-w_j^*(d))
 \right].
 \tag{11}
\]
Smooth-profile Lipschitz/BV estimates do not make these angular differences small uniformly: \(p\ge5\) is a finite multiplicative displacement. The unique top jump is crossed on the full intervals between \(y/\sqrt p,y,\sqrt p\,y\), not just within a unit-width collar. At equality its prescribed starred value remains in (9)--(11). No endpoint is removed or assigned an extra half weight.

Replacing coefficients by those at \(pX\) or \(X/p\) is incorrect. For example,
\[
 D_j(pX)=2^{-j}\lfloor\sqrt{pX}\rfloor,\quad
 H_j(pX)=\lfloor 2^{-j}\lfloor\sqrt{pX}\rfloor(pX)^{-1/4}\rfloor.
 \tag{12}
\]
Although the unnormalized spatial argument at \(pX\) is \(\sqrt p\,d\), its profile scale, height and hard endpoint are also changed. Even in a floor-free approximation, \(D_j(pX)\) scales by \(\sqrt p\) and \(H_j(pX)\) by \(p^{1/4}\), unlike (9). The corresponding statement at \(X/p\), if \(X/p\ge2\), changes scales in the opposite direction. There is no exact fixed-profile identification; phases at scaled centres do not confer membership in their original coefficient classes.

### 3.3 Uniform actual-symbol adverse control

The accepted Vaaler formula is
\(\Phi(u)=\pi u(1-u)\cot(\pi u)+u\).
For \(0<u\le1/2\), positivity and \(\cot(\pi u)\le1/(\pi u)\) imply \(0\le\Phi(u)\le1\); the identity
\(\Phi(1-u)=1-\Phi(u)\) supplies the rest of the interval. Together with the nonnegative telescoping profiles and endpoint stars,
\[
 0\le A(h,q)\le1.
 \tag{13}
\]
The exact active partition sums to one at spatial points strictly below \(y\) and above the inactive bottom support; its continuum telescoping identity is unchanged away from the unique hard jump. The accepted small-height estimate is
\(\Phi(u)=1+O(u^2)\) for \(u\le1/2\).

Fix a sufficiently small constant \(c>0\), depending only on that estimate and the accepted \(s_0\). Consider the actual integers
\[
 cR\le h\le2cR,\qquad 9h\le q\le10h,\qquad
 q\ {\rm odd},\qquad p\nmid hq.
 \tag{14}
\]
Choose \(40c^2<s_0\), so \(hq\le s_0Y\) and \(V_{\rm low}(hq/Y)=1\). Here
\[
 \frac{2Y}{\sqrt{10}}\le d_X(h,q)\le\frac{2Y}{3}.
 \tag{15}
\]
For large \(X\), this lies strictly below \(y\) and above the inactive bottom, without a hard star. Every nonzero atom has \(D_j\ge2d/3\); since \(H_j+1>D_j/R\),
\[
 \frac h{H_j+1}<\frac{hR}{D_j}
 \le\frac{3\sqrt{10}}4\frac hR
 \le\frac{3\sqrt{10}}2c.
 \tag{16}
\]
Take \(c\) smaller if necessary so all these ratios lie below \(1/2\) and their \(\Phi\)'s are at least \(3/4\). Integrality then also gives \(h\le H_j\). Exact profile telescoping proves
\[
 A(h,q)\ge3/4.
 \tag{17}
\]
For every split prime \(p\ge5\),
\(\sqrt p\,d\ge\sqrt2\,Y>y\), so \(A(ph,q)=0\).
Equation (13) gives \(A(h,pq)\le1\), even if the shifted argument enters the inactive range. Therefore
\[
 A(ph,q)+A(h,pq)-2A(h,q)\le-\tfrac12
 \tag{18}
\]
on every incidence in (14). No claim about the sign of the complete coefficient \(E_p(n)\) follows.

Elementary residue counting, uniformly for primes \(p\ge5\), leaves \(\gg_c R\) eligible \(h\)'s and \(\gg h\) odd eligible \(q\)'s for each such \(h\). For example excluding multiples of \(p\) costs at most a fifth of each interval plus \(O(1)\); odd-\(q\) multiples cost at most \(h/(2p)+O(1)\). Thus there are \(\gg_c R^2\) pairs. Each weight \((hq)^{-3/4}\gg_c R^{-3/2}\). Restricting (4) to these overlap-free pairs proves
\[
 \mathfrak C_p(X)\gg_c R^{1/2}=X^{1/8}
 \tag{19}
\]
uniformly in every split prime, however large. This uses the actual \(\Phi,w_j,H_j\), real \(X\), exact lower cutoff and original character magnitudes. It proves a lower bound on (4), not on an enlarged alternate-symbol model.

### 3.4 Full correction upper price and radial adjoint

If an atom in (1) is nonzero, the accepted support \(d/D_j\ge1/2\) and \(h\le D_j/R\) imply
\[
 hq=\frac{4Xh^2}{d^2}\le16Y.
\]
Hence \(c(m)=0\) for \(m>N_X\), and (13) gives \(|c(m)|\le\tau(m)\). Formula (4) is therefore bounded by a constant times
\(\sum_{n\le N_X}\tau(n)n^{-3/4}\).
The elementary divisor summation and partial summation give
\[
 \mathfrak C_p(X)\ll N_X^{1/4}\log(2N_X)
 \ll X^{1/8}\log(2X),
 \tag{20}
\]
uniformly in \(p\). Every overlap is included; no logarithmic number of actual profiles is hidden as an unpriced power.

For a finite radial test,
\[
 T_p^*F(m)={\bf1}_{p\mid m}F(m/p)+F(pm).
\]
For (2) this is exactly
\[
 \begin{split}
 T_p^*F_X(m)={}&
 p^{3/4}{\bf1}_{p\mid m}{\bf1}_{p\le m\le pN_X}
 m^{-3/4}e(\sqrt{(X/p)m})\\
 &+p^{-3/4}{\bf1}_{1\le m\le\lfloor N_X/p\rfloor}
 m^{-3/4}e(\sqrt{(pX)m}).
 \end{split}
 \tag{21}
\]
The first indicator can be shortened only by using the independent fact \(c(m)=0\) for \(m>N_X\). There is no fractional endpoint rounding freedom. With a lower cutoff, the two extra factors are respectively \(V_{\rm low}(m/(pY))\) and \(V_{\rm low}(pm/Y)\), not a common unshifted cutoff. The finite formula has no omitted far tail.

The phase changes by factors \(p^{\pm1/2}\); its difference from the original phase is not uniformly small modulo one. Its exact contribution is retained in (21), without an orthogonality grant or an average over new centres.

Let \(M_p=\sum_m c(m)T_p^*F_X(m)\). By changing variables back, using \(\tau(pn)\le2\tau(n)\), and keeping \(p\le N_X\),
\[
 \begin{split}
 |M_p|
 &\le\sum_{n\le N_X/p}\tau(pn)n^{-3/4}
 +p^{-3/4}\sum_{m\le N_X/p}\tau(m)m^{-3/4}\\
 &\ll X^{1/8}\log(2X)(p^{-1/4}+p^{-1}).
 \end{split}
 \tag{22}
\]
For \(p>N_X\), \(M_p=0\) exactly. In that case (3) gives \(E_p(n)=-2c(n)\) on \(1\le n\le N_X\). Thus choosing only very large primes makes the amplified identity an explicit unchanged copy of the original target.

### 3.5 Complete prime average, physical restoration and inherited owners

Equations (6)--(7) and finite adjunction prove
\[
 2M G_X=
 \Re\left\{e(1/8)
 \left[\sum_{p\in\mathcal P}M_p-
       \sum_{p\in\mathcal P}\sum_nE_p(n)F_X(n)\right]\right\}.
 \tag{23}
\]
All entries are real coefficients before the exponential; the negative-frequency expression is its conjugate. The two terms must stay together to seek signed cancellation.

Define
\[
 B_{\mathcal P}=\frac1M\sum_{\substack{p\in\mathcal P\\p\le N_X}}
 (p^{-1/4}+p^{-1}).
\]
Equations (20)--(22) give the complete separately priced certificate
\[
 |G_X|\ll X^{1/8}\log(2X)(1+B_{\mathcal P}).
 \tag{24}
\]
Its correction part is at least \(cX^{1/8}\) by (19), independently of \(\mathcal P\). Thus no optimization of the tested finite prime range improves this certificate, even under an optimistic prime count. This assertion is about the specified certificate only.

The inherited actual complete estimate is stronger:
\[
 |G_X|\ll_\varepsilon X^{1/12+\varepsilon},
 \tag{25}
\]
from the accepted direct \(X^{1/3+\varepsilon}\) total-M1 menu and exact GAR reconstruction. Even the real signed correction can be bounded using (23), but this only returns
\[
 \frac1M\left|\Re\{e(1/8)\sum_{p,n}E_p(n)F_X(n)\}\right|
 \ll_\varepsilon X^{1/12+\varepsilon}
       +X^{1/8+\varepsilon}B_{\mathcal P}.
 \tag{26}
\]
It is not a new estimate at the desired \(X^\varepsilon\) scale. No stronger complex estimate is inferred from the real bound (25).

The physical reconstruction is
\[
 M_{1,\mathrm{active}}^{\mathrm{stat}}
 =-\frac4\pi X^{1/4}G_X+O(\log^2X).
\]
Hence (24) costs \(X^{3/8+\varepsilon}\); cap it by the inherited \(X^{1/3+\varepsilon}\). Owned transform errors and the inactive bottom are already \(O(X^{1/4+\varepsilon})\).

Accepted Round 120 pays the exact nonlower complement, but not each shifted coefficient/phase in (21) at a changed centre. Accepted Round 121 flattening and phase integerization have \(O(X^{1/4+\varepsilon})\) physical errors, and retain the entire surviving lower functional. They cannot be used as a coefficientwise replacement \(A_X=1\) inside (7). This report has not applied that replacement.

Every lower scale remains: the complete Round 122 functional retains low two-adic and residue branches; later ownership through Round 159 includes the common-profile Abel self-return, all \(D>1,L>1\), generic \(t=1\), every \(t\ge2\) layer and the independent cross owner. The actual lower wedge (14) is a control inside this full ownership, not a substitute target.

## 4. First doubtful or unproved step

The missing step is a complete coefficient-sensitive bound for the joint real expression in (23),
\[
 \left|\Re\left\{e(1/8)
 [\sum_p M_p-\sum_{p,n}E_p(n)F_X(n)]\right\}\right|
 \ll_\varepsilon M X^\varepsilon,
 \tag{27}
\]
or a rigorously smaller complete exponent than \(M X^{1/12+\varepsilon}\). The identity itself equals \(2MG_X\) and proves no such inequality.

Taking main and correction norms separately, or taking incidence moduli inside the correction, loses the needed information. Equations (18)--(20) show that the latter certificate cannot pay the correction at target. They do not exclude cancellation between divisor allocations of one \(n\), across \(n\), across primes, or between main and correction. None of those cancellations has been proved here. No new source or arbitrary-vector orthogonality is granted.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Complete actual GAR owner | Exact \(A_X,c,F_X,G_X\), all scales and the original real centre are retained; current lower dependencies through 159 remain. |
| Exact divisor/character relation | Inclusion-exclusion (6), correction (7), valuation formula (8), inert-prime eigenvalue zero and prime-2 vanishing are explicit. |
| Prime-power overlap | Every interior allocation is subtracted once; the \(p\mid n\) term is never dropped from the full formula. |
| Actual profile commutator | Table (9), exact height extension, spatial changes and overlap height change are retained. |
| Floors/stars | Original \(D_j,H_j\), hard top, equality stars, finite cutoffs and empty heights stay literal. The adverse wedge is strictly away from the hard star, without deleting stars elsewhere. |
| Fixed versus scaled centre | Equation (12) shows why \(A_{pX}\) or \(A_{X/p}\) cannot replace the fixed-\(X\) coefficient. |
| Real pairing | Conjugacy gives the one real projection in (23); no bound for the separate complex target is inferred from its real part. |
| Radial dilation and cutoffs | Both \(p^{3/4},p^{-3/4}\), the divisibility mask, shifted phases, integer endpoints and shifted lower cutoffs are included in (21). |
| Actual adverse control | Uniform actual-symbol inequality (18) and elementary count prove (19). This is a lower bound only for the named incidence certificate. |
| Full range and costs | Arbitrary finite nonempty prime sets, including primes above \(N_X\), are priced in (20)--(26). No prime-count theorem or discarded exception. |
| Lower flattening and owners | Only inherited physical-error scope is cited; no coefficientwise flattening is used. Round 122 and later 159 residuals are all retained. |
| Statement-only derivation | Algebra and actual-symbol control were independently derived from the permitted conductor statement and accepted contexts; prior history is disclosed, so this is not a fresh blind review. |
| Source/experiment control | No external theorem, source audit or experiment is used. |
| Full goal | Total M1 only; blockwise M1, all M2, endpoints, M9, the moment alternative and quarter theorem are not closed. |

The finite constant-profile control checks (6)--(8), while (14)--(18) prove directly that the actual profile is not that eigenvector. These two controls must not be conflated. No actual signed lower bound is claimed.

## 6. Dependencies and exact artifacts

Campaign m9-m1-complete-gar-prime-amplification, round 224; role actual_prime_profile_control. The active brief fixes candidate-evidence status and one bounded mechanism. The following are the only file contexts used.

| Artifact | SHA-256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 8e6526a9fd822d43f5ccfe65c67ec4db1f131e1c38e3e6eb953b8c0ddc915cf5 |
| strategy/round224_complete_gar_split_prime_amplification.md | c1f2364a958d484f523745bc06711aaebaf049c1c989f73639c55a48590da9a5 |
| Current briefs/actual_prime_profile_control.md | 6e37b72a6c87bc75e8884299c6168bb68307fc10d89b189a42aacc9194eaeb2f |
| Current briefs/conductor_actual_gar_interface.md | f5ea5afa70e8315179d56d066303bb17b1280b4fabd2bbfb5867aece531bd803 |
| strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md | a0c75c5e2ef4ea45df4e388e3497d5be5133d6d49c7d7a2d71c166f11dd9dd33 |
| rounds/codex-managed/gc-full-goal-signed-source-review/synthesis.md | 3f97b688827680d7c733116ebc6bd0107b5ec1af4d2df5258fc0ce1cb0b5ae78 |
| rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/candidates/conductor_terminal_height_interface_completion.md | 712a31a8b83263cf5f975177a34058d3449d920a36d2fa088d73fde4aa49c26d |
| rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/candidates/conductor_profile_flattening_and_integer_phase.md | 6a60d62ff42c5b764a79e4303eb50b8a780572ef4ac6e635ff9406e9192d095d |
| proofs/kernels/m9_m1_d1_full_abel_common_profile_recombination.md | a60cfaf54611957fbd359bc07783f95886a0549150f53277104e3c508041f0f2 |
| rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md | 69b1a84a67fdd8cc2a35cfb783ea1697390b45c807bd0830907ac5271559c482 |
| rounds/codex-managed/m9-m1-angular-mellin-separation/synthesis.md | 1b23af89825a4f6fc4ec4613c199c251d227f8b403631e29acff4a6d271ca667 |

The graph supplies accepted nonnegative profile geometry, Vaaler regularity, complete reconstruction and the direct one-third menu. Round 120 supplies nonlower ownership; Round 121 supplies only the stated target-scale flattening scope; Round 122 and kernel 159 supply the retained lower residuals. The angular Mellin history prevents an unpriced reflection or hard-Perron import. The conductor separately reminded this role to compare all new certificate prices with the actual \(X^{1/12}\) GAR baseline; that comparison is explicit above.

No current claimant report, blind report, additional historical file, source or shared-state artifact was read beyond this list. Prior role history remains disclosed reuse.

## 7. Recommended state effect

**Retain the complete GAR target and every downstream owner open.** Subject to independent review, retain the exact fixed-\(X\) commutator, full radial costs and the actual-symbol incidence-certificate obstruction as scoped route evidence. Reject the claim that the actual split-prime commutator can be discarded, replaced by a changed-centre coefficient, or paid at target using the incidencewise absolute certificate (4).

This bounded mechanism supplies no complete improvement over \(|G_X|\ll X^{1/12+\varepsilon}\). It also supplies no actual lower bound contradicting the desired GAR theorem. A target-sized joint estimate (27) remains the first unproved step; naming it or reusing its exact self-return is not an analytic gain.

The conclusion is complete_gar_amplification_no_new_bound for this tested correction certificate and supplied estimates. No successor mechanism is begun. Complete total-M1 GAR, independent blockwise M1, all three M2 parents, endpoint uniformity and the full quarter goal remain unchanged.
