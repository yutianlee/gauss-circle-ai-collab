# 1. Result

**GREEN for the frozen report's stated scope. No mathematical repair requested.**

Reviewed claimant: reports/actual_prime_profile_control.md, SHA256 **7ccf2997b5c1f7bfd610caa0faa89f5d4a3031ada2fb035c33042c0b4b5c0ec4**, under rounds/codex-managed/m9-m1-complete-gar-prime-amplification.

The actual wedge, its count uniform in every split prime, the profile commutator, prime-power overlap, adjoint cutoffs and physical costs check. The proved lower bound concerns precisely the incidencewise absolute correction certificate. It does not lower-bound the correction after grouping divisors, its signed radial sum, its real part, or the joint amplified target.

# 2. Exact reviewed statement and hypotheses

Use the frozen actual interface with real \(X\ge2\),
\[
R=X^{1/4},\quad Y=\sqrt X,\quad y=\lfloor Y\rfloor,\quad
D_j=2^{-j}y,\quad H_j=\lfloor D_j/R\rfloor,\quad N_X=\lfloor16Y\rfloor.
\]
The fixed actual profile is
\[
A_X(h,q)=\sum_j1_{h\le H_j}\Phi(h/(H_j+1))
[w_j(2\sqrt{Xh/q})]^*,
\]
and \(c(n)=\sum_{hq=n}\chi_4(q)A_X(h,q)\). For \(p\equiv1\bmod4\),
\[
E_p(n)=c(pn)+1_{p\mid n}c(n/p)-2c(n).
\]

The certificate being reviewed takes absolute values at the **individual divisor-allocation** level:
\[
\begin{aligned}
\mathfrak C_p(X)=\sum_{n\le N_X}n^{-3/4}\bigg\{&
\sum_{hq=n}|\chi_4(q)|
 |A(ph,q)+A(h,pq)-2A(h,q)|\\
&+1_{p\mid n}\sum_{hq=n/p}|\chi_4(q)|
 |A(h,q)-A(ph,pq)|\bigg\}.
\end{aligned}
\]
The claimant proves
\(c_0X^{1/8}\le\mathfrak C_p(X)\ll X^{1/8}\log(2X)\)
for sufficiently large \(X\), uniformly in every split prime. Its lower assertion is asymptotic; bounded \(X\) is included only in upper-bound constants. The same lower bound survives insertion of the exact fixed lower cutoff, since the selected products lie in its plateau.

# 3. Independent derivation and checks

**Character allocation.** For a general prime put \(\eta=\chi_4(p)\). Cover factorizations of \(pn\) by those with \(p\) in the first or second factor, subtracting the intersection. This gives
\[
c(pn)=c_{A(ph,q)}(n)+\eta c_{A(h,pq)}(n)
-\eta1_{p\mid n}c_{A(ph,pq)}(n/p).
\]
Adding \(\eta c(n/p)-(1+\eta)c(n)\) gives the claimant's correction. For \(n=p^rm\), \(p\nmid m\), each allocation \(p^a\) to the first factor has weight \(\eta^{r-a}\); the repeated-prime intersection comprises exactly the interior allocations, each subtracted once. This verifies all valuations, not only \(p\nmid n\).

At2, only the second-factor exponent zero survives, so
\(c(2n)=c_{A(2h,q)}(n)\). Even first factors remain. An inert prime has unweighted eigenvalue0, not2. The constant-profile geometric series checks the general recurrence but supplies no actual-profile estimate.

**Exact profile changes.** Writing \(d=2\sqrt{Xh/q}\), the spatial arguments for
\(A(h,pq),A(ph,q),A(ph,pq)\) are respectively \(d/\sqrt p,\sqrt p\,d,d\); their height weights are respectively \(B_j(h),B_j(ph),B_j(ph)\). This proves the table and the three-term commutator expansion in the claimant. All \(H_j,D_j\) stay fixed at \(X\).

The zero extension of \(\Phi\) at and beyond1 is Lipschitz, since its value and first derivative vanish at1. Thus the displayed height-change bound remains valid through the literal integer cutoff, including \(H_j=0\). Spatial hard-jump crossings are not covered by an assumed smooth derivative bound; the claimant retains their evaluations and stars. At \(pX\) or \(X/p\), the scale and height floors would change, so neither is the actual shifted coefficient.

**Global profile bound.** For \(0<u\le1/2\),
\[
0\le\Phi(u)=\pi u(1-u)\cot(\pi u)+u\le1,
\]
using \(0\le\cot(\pi u)\le1/(\pi u)\). Direct substitution gives
\(\Phi(1-u)=1-\Phi(u)\), establishing \(0\le\Phi\le1\) throughout. The nonnegative telescoping profile sum is at most1, including its half-valued hard boundary, so \(0\le A\le1\). Above \(y\), the hard top is zero and every interior profile ends below \(y\); this justifies the exact vanishing used below.

**Actual adverse wedge.** Fix the claimant's sufficiently small \(c>0\), independent of \(p,X\), and take
\[
cR\le h\le2cR,\qquad9h\le q\le10h,\qquad q\text{ odd},\qquad p\nmid hq.
\]
Then \(hq\le40c^2Y<s_0Y\), so the lower multiplier is exactly1. The spatial argument lies in
\([2Y/\sqrt{10},\,2Y/3]\), strictly below \(y\) for all sufficiently large real \(X\), and far above the inactive bottom. There is no top-star tie.

For a nonzero atom, \(D_j\ge2d/3\). The exact floor inequality
\(H_j+1>D_j/R\), not a floor-free approximation, yields
\[
\frac h{H_j+1}<\frac{hR}{D_j}
\le\frac{3\sqrt{10}}2c.
\]
Fixing \(c\) small makes the ratio below \(1/2\) and the Vaaler factor at least \(3/4\), by the accepted121 small-height estimate. It also ensures the original height cutoff is satisfied. The full interior partition then gives \(A(h,q)\ge3/4\).

For every split prime \(p\ge5\),
\(\sqrt p\,d\ge\sqrt2Y>y\), whence \(A(ph,q)=0\). Meanwhile \(A(h,pq)\le1\), even if its shifted argument enters the inactive range. Hence the actual commutator is at most \(-1/2\) on this wedge.

**Uniform counting.** The \(h\)-interval contains at least
\[
(1-1/p)cR-O(1)\ge(4/5)cR-O(1)
\]
integers not divisible by \(p\). For each such \(h\), the number of odd \(q\in[9h,10h]\) not divisible by \(p\) is at least
\[
\left(\frac12-\frac1{2p}\right)h-O(1)
\ge\frac25h-O(1).
\]
The error constants are absolute and uniform in \(p\), including \(p\) larger than the intervals. Thus there are \(\gg_cR^2\) pairs for all sufficiently large \(X\), with the threshold independent of \(p\). Every pair is overlap-free and has weight
\((hq)^{-3/4}\gg_cR^{-3/2}\). Their certificate contribution is therefore \(\gg_cR^{1/2}=X^{1/8}\).

Distinct pairs need not have distinct products. This is harmless for the certificate, which counts incidences, and is exactly why this proof does **not** give a divisor-grouped lower bound. Neither the sign of \(\chi_4(q)\) after grouping nor the radial phase is controlled by this argument.

**Complete upper bound and adjoint.** Each first-bracket modulus is at most2 and each overlap modulus at most1. Since \(\tau(n/p)\le\tau(n)\) when \(p\mid n\),
\[
\mathfrak C_p(X)\le3\sum_{n\le N_X}\tau(n)n^{-3/4}
\ll N_X^{1/4}\log(2N_X).
\]
This supplies a uniform full upper bound, including all overlaps and profiles.

Finite reindexing gives exactly
\[
T_p^*F_X(m)=p^{3/4}1_{p\mid m}1_{p\le m\le pN_X}m^{-3/4}
 e(\sqrt{(X/p)m})
+p^{-3/4}1_{m\le\lfloor N_X/p\rfloor}m^{-3/4}
 e(\sqrt{(pX)m}).
\]
The two lower cutoffs have the claimant's distinct arguments. The independent coefficient support \(c(m)=0\) for \(m>N_X\) follows from the original profile geometry, so the main-term bound
\[
|M_p|\ll X^{1/8}\log(2X)(p^{-1/4}+p^{-1}),\qquad p\le N_X,
\]
follows using \(\tau(pn)\le2\tau(n)\). For \(p>N_X\), both adjoint terms vanish on the coefficient support, and \(E_p=-2c\) on the radial test range. This verifies the entire prime range without a prime-count theorem.

**Restoration.** Averaging the separate positive certificates divides their sum by twice the number of primes and preserves its \(X^{1/8}\) price. Multiplication by the exact physical factor \(-(4/\pi)X^{1/4}\) gives \(X^{3/8}\). The unchanged accepted complete menu gives the stronger physical \(X^{1/3+\epsilon}\), hence normalized \(X^{1/12+\epsilon}\). The claimant correctly caps its result by that bound and does not infer a complex correction estimate from a real-part bound.

Accepted120 pays the original nonlower owner only. Accepted121's target-sized physical flattening error is not a coefficientwise grant \(A=1\), and the later lower owners through159 remain. These scopes are preserved.

# 4. First doubtful or unproved step

No unsupported step remains in the report's stated incidence-certificate claims. The first open step is the complete joint signed estimate in claimant (27), or a complete exponent smaller than the inherited \(1/12\).

A purported implication from the wedge to
\(\sum_n|E_p(n)|n^{-3/4}\), \(|\sum_nE_p(n)F_X(n)|\), its real part, or the full GAR quantity would be unproved. The claimant expressly makes none of these implications. No repair is requested.

# 5. Required controls and verdicts

| Seam | Verdict |
|---|---|
| Prime-power allocation and prime2 | GREEN; exact character factors and one overlap subtraction. |
| Actual shifted symbols | GREEN; original center, height cutoffs, spatial dilations and stars retained. |
| Wedge and literal floors | GREEN; strict spatial buffer and exact \(H_j+1>D_j/R\). |
| Uniform-in-\(p\) count | GREEN; explicit interval bounds above, no distribution theorem for primes. |
| Certificate scope | GREEN only for incidencewise absolute correction; no grouped or signed lower bound. |
| All adjoint ranges | GREEN; exact factors, divisibility and integer endpoints, including \(p>N_X\). |
| Physical and complete ownership | GREEN; \(3/8\) certificate capped by inherited \(1/3\); no M2, endpoint or quarter conclusion. |

All checks were analytical. No experiment, source audit or new mechanism was attempted.

# 6. Dependencies and provenance

Round224, NONBLIND independent application review, 2026-09-28. I did not author the reviewed actual-profile report. I retain earlier-round history and authored the separate complete_signed_prime_attack report before this assignment. That overlapping background is disclosed; this review does not count as independent validation of my own report or my different positive certificate. The claimant's wedge and its uniform count were rederived above. No other current review or conductor grouped-coefficient control was read.

| Artifact | SHA256 |
|---|---|
| Current224 reports/actual_prime_profile_control.md | 7ccf2997b5c1f7bfd610caa0faa89f5d4a3031ada2fb035c33042c0b4b5c0ec4 |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| Current224 briefs/conductor_actual_gar_interface.md | f5ea5afa70e8315179d56d066303bb17b1280b4fabd2bbfb5867aece531bd803 |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/candidates/conductor_profile_flattening_and_integer_phase.md | 6a60d62ff42c5b764a79e4303eb50b8a780572ef4ac6e635ff9406e9192d095d |
| rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/candidates/conductor_terminal_height_interface_completion.md | 712a31a8b83263cf5f975177a34058d3449d920a36d2fa088d73fde4aa49c26d |
| proofs/kernels/m9_m1_d1_full_abel_common_profile_recombination.md | a60cfaf54611957fbd359bc07783f95886a0549150f53277104e3c508041f0f2 |
| Current224 reports/complete_signed_prime_attack.md, authorship provenance only | 0d734e579ccee82e08f6af9183a3246683b317eb395eafca2bead509be8251cd |

Current224 denotes rounds/codex-managed/m9-m1-complete-gar-prime-amplification. The relevant graph records are Vaaler regularity, actual dyadic nondegeneracy, the direct one-third menu, exact GAR reconstruction, and the lower owner's current dependencies. Previously authorized120/121/159 context was used only at those stated scopes.

# 7. Recommended state effect

Retain this report as **GREEN scoped review evidence** for the exact frozen claimant hash. No mathematical promotion, shared-file edit or successor follows.

The incidence-certificate obstruction is valid; the complete signed GAR bound remains open, with every downstream owner and benchmark unchanged. No requested correction.

