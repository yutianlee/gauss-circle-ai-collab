# Round 224: independent review of the complete signed prime attack

## 1. Result

**GREEN for the scoped finite identities, complete cost accounting and no-new-bound conclusion.** The reviewed claimant is reports/complete_signed_prime_attack.md at SHA-256
0d734e579ccee82e08f6af9183a3246683b317eb395eafca2bead509be8251cd.
The on-disk hash was verified before review.

The full allocation formula, repeated-prime overlap, radial adjoint, five-term joint row, real quadratic form, elementary upper prices and actual-profile positive-certificate control are correct in the stated scope. The report correctly retains the inherited complete \(|G_X|\ll X^{1/12+\varepsilon}\) bound and physical \(X^{1/3+\varepsilon}\) estimate. Its positive closure costs \(X^{1/8+o(1)}\) before physical restoration and supplies no gain.

No mathematical repair is requested. GREEN does not promote GAR, a new analytic estimate, an actual lower bound, or an impossibility theorem for every use of prime amplification. The claimant explicitly excludes those interpretations.

This reviewer did not author the claimant. This is NONBLIND: I authored the separate Round 224 actual-profile-control report and have disclosed prior campaign history. I did not read the current blind report, conductor grouped control or sibling reviews. No experiment, source import or shared-state edit was used.

## 2. Exact reviewed hypotheses and quantities

The claimant uses the accepted literal profile
\[
 A_X(h,q)=\sum_j{\bf1}_{h\le H_j}\Phi(h/(H_j+1))
 [w_j(2\sqrt{Xh/q})]^*,
\]
with \(X\) fixed, \(R=X^{1/4}\), \(Y=\sqrt X\),
\(D_j=2^{-j}\lfloor\sqrt X\rfloor\),
\(H_j=\lfloor D_j/R\rfloor\), and \(M=\lfloor16Y\rfloor\).
Its real coefficient is \(c_A(n)=\sum_{hq=n}\chi_4(q)A_X(h,q)\). Even \(h\) is retained and even \(q\) vanishes only through the character.

The complete real target uses
\[
 F(n)={\bf1}_{1\le n\le M}n^{-3/4}e(\sqrt{Xn}),\qquad
 G_X=\Re\{e(1/8)S_A(F)\}.
\]
The lower test \(F_V=V_{\rm low}(n/Y)F(n)\) uses the fixed accepted cutoff. Round 120 supplies \(G_X-G_V=O_\varepsilon(X^\varepsilon)\); it does not estimate each dilated term at a changed centre.

The tested amplifier is the finite nonempty unit-weight set of split primes in \((P,2P]\), initially \(2\le P\le M\), with exact count \(K>0\). All primes above \(M\) are also treated. No prime-count input is used.

The claimant's positive certificate is specifically the sum of absolute values of the five individual incidence terms in its equation (6), divided by \(2K\). It differs from both an absolute norm of the divisor-aggregated defect and the signed joint expression. All certificate conclusions below refer to that defined object.

## 3. Independent derivation and checks

**Allocation and overlap.** For \(p\equiv1\pmod4\), partition the factorizations of \(pn\) into those having \(p\) in the first factor and those having \(p\) in the second. Their intersection has both factors divisible by \(p\), so it is indexed by \(hq=n/p\). Thus
\[
 c_A(pn)=c_{A(ph,q)}(n)+c_{A(h,pq)}(n)
 -{\bf1}_{p\mid n}c_{A(ph,pq)}(n/p).
\]
Adding \(c_A(n/p)-2c_A(n)\) gives the claimant's equation (2). This reasoning holds at every valuation, not just \(p\nmid n\). For \(n=p^rm\), the factor allocation \(p^a\) in the first factor and \(p^{r-a}\) in the second makes the overlap exactly the interior allocations, each subtracted once.

The actual shift table is also correct: the spatial arguments are respectively
\(\sqrt p\,d,d/\sqrt p,d\), while height weights are \(b_j(ph),b_j(h),b_j(ph)\). All scales, floors and starred evaluations remain at \(X\). There is no identification with \(A_{pX}\) or \(A_{X/p}\). The report's prime-2 and inert-prime exclusions from the split-prime eigenvalue-two amplifier are accurate and do not remove even original products.

**Adjoint, endpoints and complete row.** Reindexing the coefficient argument gives
\[
 T_p^*F(m)={\bf1}_{p\mid m}F(m/p)+F(pm).
\]
On positive integers this yields exactly the two powers \(p^{3/4},p^{-3/4}\), phases at \(X/p,pX\), cutoffs \(m\le pM,m\le\lfloor M/p\rfloor\), and divisibility indicator in claimant (4). Its first term needs no extra written \(m\ge p\) condition because \(m\ge1\) and \(p\mid m\) already imply it. The two lower multipliers become \(V_{\rm low}(m/(pY))\) and \(V_{\rm low}(pm/Y)\). No infinite tail is introduced.

Subtracting the full correction cancels the duplicate \(A(h,q)F_V(phq)\) term and gives precisely the five terms in claimant (6). Splitting the first remaining divisibility indicator by \(p\mid h\) or \(p\mid q\), with intersection subtracted, yields
\[
 \sum_{h,q}\chi_4(q)A(h,q){\bf1}_{p\mid hq}F_V(hq/p)
 =
 \sum_{h,q}\chi_4(q)[A(ph,q)+A(h,pq)]F_V(hq)
 -\sum_{h,q}\chi_4(q)A(ph,pq)F_V(phq).
\]
Hence the other shifted terms cancel exactly and
\(J_p=2S_A(F_V)\). This verifies all overlap cancellation without changing a cutoff or coefficient.

**Real channel and completed-row Cauchy.** With \(\gamma=e(1/8)\),
\[
 \Re(\gamma a)\Re(\gamma b)
 =\tfrac12\Re\{a\overline b+\gamma^2ab\}.
\]
Since \(\gamma^2=e(1/4)\), claimant (8) correctly includes both the conjugated and nonconjugated channels, with all four main/correction products inside each. Each completed real row is \(j_p=2G_V\), so Cauchy across \(p\) is equality and the quadratic form is exactly \(4K^2G_V^2\). This identity is not an all-method no-go; it only invalidates claiming a saving from independence of these completed rows.

**Complete inherited comparison.** The graph separately grants the actual fixed-BV M1 bounds
\[
 |B_1(D,L;X)|\ll X^\varepsilon\min(D,1+D/L)
 \quad\text{and}\quad
 |B_1(D,L;X)|\ll X^\varepsilon\min(D,\sqrt{LX/D}).
\]
The second is supplied by M9-M1-ordered-resonance-cell-decomposition; it is not a silently truncated generic second-derivative bound. Thus the claimant's displayed menu is legitimate. If \(D\le X^{1/3}\), use the trivial entry; otherwise separate at \(L=DX^{-1/3}\). Both sides cost \(O(X^{1/3+\varepsilon})\). Accepted labels, hard top and owned errors restore the complete physical bound, hence \(|G_X|+|G_V|\ll X^{1/12+\varepsilon}\). Its quadratic price \(K^2X^{1/6+\varepsilon}\) is correct after harmless epsilon relabelling.

**All-range absolute upper costs.** The accepted support \(d/D_j\ge1/2\) and \(h\le D_j/R\) implies \(hq\le16Y\). Applying this to the three shifted profiles gives \(phq\le16Y\) or \(p^2hq\le16Y\), exactly as in claimant (11). Bounded actual profile overlap gives \(|c_A(n)|\ll\tau(n)\). The elementary bound
\(\sum_{n\le z}\tau(n)n^{-3/4}\ll z^{1/4}\log(2z)\)
and \(\tau(pn)\le2\tau(n)\) suffice.

Consequently the two original adjoint pieces cost
\(M^{1/4}(p^{-1/4}+p^{-1})\log(2M)\). The five expanded incidence terms cost, respectively,
\[
 (M/p)^{1/4},\quad(M/p)^{1/4},\quad(M/p)^{1/4},
 \quad M^{1/4},\quad M^{1/4}p^{-5/4},
\]
up to a common logarithm. The last exponent combines \(p^{-3/4}\) from the radial weight with \((M/p^2)^{1/4}\) from actual support. Empty sums below one are handled literally. Averaging over \((P,2P]\) gives claimant (13)--(15), with no unpriced count of primes. If \(p>M\), all shifted terms and the main vanish, leaving the correction \(-2c_A\) on the original support. That limiting case is correctly a self-return.

**Actual lower control for this certificate.** Fix \(c>0\) small enough that \([c,2c]\) is inside \(V_{\rm low}=1\). At \(h=1\), odd \(q\in[cY,2cY]\), the spatial argument is \(\asymp c^{-1/2}R\). Choosing \(c\) smaller puts it above the inactive bottom; for sufficiently large real \(X\) it is strictly below the hard top. Every supported profile satisfies
\[
 D_j\ge(2/3)d(1,q),\qquad
 (H_j+1)^{-1}<R/D_j\ll\sqrt c.
\]
The exact nonnegative interior telescope and \(\Phi(u)=1+O(u^2)\) therefore yield \(A_X(1,q)=1+O(c)\ge1/2\). Height integrality is respected because the ratio is strictly below one, and no hard endpoint star occurs in this buffer.

The fourth term of the *defined positive certificate* contains \(2A_X(1,q)q^{-3/4}\). Its odd-\(q\) sum is \(\gg Y^{1/4}\); the \(K\) repetitions cancel exactly with the \(1/K\) normalization. This proves claimant (17), uniformly for the entire stated amplifier family, without a prime count, phase alignment or grouped-coefficient lower bound. The control lies in the retained lower range and survives payment of the fixed nonlower complement.

## 4. First doubtful or unproved step

No repairable mathematical defect was found in the reviewed finite derivations or certificate costs. The first missing analytic input is claimant (18), equivalently a bound for its exact real quadratic form better than \(K^2X^{1/6+\varepsilon}\), with a target of \(K^2X^\varepsilon\).

The report does not prove such cancellation between the actual mixed main/correction terms. The identities are compatible with a future estimate of the original complete target, but completed-row Cauchy and the explicitly expanded positive certificate do not provide one. The certificate lower control proves no lower bound for \(c_A(n)\), \(E_{p,A}(n)\), their signed wave or \(G_X\).

## 5. Required controls and review outcome

| Seam | Verdict |
|---|---|
| Complete joint identity | GREEN: all five terms, duplicate cancellation and repeated-prime intersections rederived. |
| Actual profiles and fixed centre | GREEN: spatial shifts and unchanged heights/scales/stars are explicit; changed-centre coefficients are not substituted. |
| Real pairing | GREEN: both quadratic channels and all mixed terms are retained. |
| All prime and radial ranges | GREEN: exact finite count, cutoffs, empty sums, large-prime self-return, even products and exceptional character cases retained. |
| Positive upper/lower certificate | GREEN: all five prices and the actual \(h=1\) interior control match the named expanded certificate. |
| Grouped versus incidence scope | GREEN: claimant explicitly excludes a grouped-defect or actual signed lower bound. |
| Complete baseline | GREEN: accepted actual M1 menu supports \(X^{1/12+\varepsilon}\) for GAR; certificate \(X^{1/8}\) is weaker. |
| Physical restoration | GREEN: multiply by \(X^{1/4}\), giving \(X^{3/8}\) certificate versus inherited \(X^{1/3}\); owned errors stay quarter-sized. |
| Lower owner through 159 | GREEN: all \(D>1,L>1,t=1,t\ge2\) and independent cross contributions remain; no local substitution closes them. |
| Scope and stopping | GREEN: no all-method no-go, no source grant, no full-quarter promotion, no successor. |

## 6. Dependencies and provenance

Reviewed claimant:
rounds/codex-managed/m9-m1-complete-gar-prime-amplification/reports/complete_signed_prime_attack.md

Reviewed SHA-256:
0d734e579ccee82e08f6af9183a3246683b317eb395eafca2bead509be8251cd

Principal accepted-context bindings used:

| Artifact | SHA-256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| Current briefs/conductor_actual_gar_interface.md | f5ea5afa70e8315179d56d066303bb17b1280b4fabd2bbfb5867aece531bd803 |
| Round 120 conductor_terminal_height_interface_completion.md | 712a31a8b83263cf5f975177a34058d3449d920a36d2fa088d73fde4aa49c26d |
| Round 121 conductor_profile_flattening_and_integer_phase.md | 6a60d62ff42c5b764a79e4303eb50b8a780572ef4ac6e635ff9406e9192d095d |
| proofs/kernels/m9_m1_d1_full_abel_common_profile_recombination.md | a60cfaf54611957fbd359bc07783f95886a0549150f53277104e3c508041f0f2 |

These are the same allowed accepted contexts used in my original profile-control task. In this review I additionally inspected the exact accepted graph statements for M9-M1-terminal-frequency-divisor-bound, M9-M1-ordered-resonance-cell-decomposition and M9-direct-menu-one-third-optimality to verify the baseline derivation.

Authorship disclosure: I authored reports/actual_prime_profile_control.md, frozen at
7ccf2997b5c1f7bfd610caa0faa89f5d4a3031ada2fb035c33042c0b4b5c0ec4.
It treats a different named incidencewise commutator certificate. I did not author the present claimant and did not transfer the scope of my certificate to the claimant's five-term certificate.

No blind allocation report, conductor grouped control, sibling review, new source or numerical experiment was read or used. No claim is made to history-free isolation. Only this assigned review is written.

## 7. Recommended state effect

**GREEN; no repair requested.** Accept this review as evidence that the frozen claimant's finite algebra and scoped no-gain conclusions are sound. Retain the complete GAR estimate, all lower dependencies, total/blockwise distinction, every M2 and endpoint obligation and both exponent ledgers unchanged.

Any promotion of a finite identity or scoped certificate fact remains the conductor's decision after the required reviews and state process. This review authorizes no graph edit and proves no new complete analytic gain. Stop with the reviewed hash fixed as above.
