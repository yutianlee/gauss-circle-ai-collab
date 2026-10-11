# Round226 independent strategy and application review

## 1. Result

**GREEN, with the stated conditional and method-specific scope.** This
nonauthor review binds both final targets:

- strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md:
  SHA256 f6aba7be605277ef9e09915e749ce07d22deb3cbfe95cc761660508a7f5c53c9.
- controls/conductor_current_primary_status.md, in the current campaign:
  SHA256 8ec44865166527e8b3c2bb5c76c441fc5b7167fd9b647cd82d907b672aeb7b4f.

The complete signed remainder criterion (F) is sufficient for the
quarter theorem, with the printed Fejer prefactor, density, partition,
singleton and infinite tail paid. It is unproved. The inspected primary
records support the limited status assertions. The checkpoint promotes
no estimate and retains every complete owner. No repair is required.

This is a post-blind, nonblind strategy/application review. I authored
the current isolated subordination report and its separate application
review, but neither the checkpoint nor either current source report.
Retained earlier-round history is disclosed, not treated as fresh
independence. No sibling review was read.

## 2. Exact statement and hypotheses

Use the checkpoint's fixed real smooth \(\phi\), equal to one on
\((0,1]\) and zero on \([2,\infty)\), and \(w(x)=\phi(x)-\phi(2x)\).
The accepted mollifier fixes real Schwartz \(\Psi\). For real \(T\ge2\),
every real \(cT\le R\le CT\), and dyadic integers \(2\le N\le P\), where
\[
 P=2^{\lceil\log_2(T^{3/2})\rceil},\qquad
 T^{3/2}\le P<2T^{3/2},
\]
put
\[
 g_N(t)=(t/N)^{-3/4}\Psi(\sqrt{t/T})w(t/N),\quad
 A_J=(1+N/T)^{-J},\quad z_n=r_2(n)g_N(n)e(R\sqrt n).
\]
The vector is zero outside the literal positive integer support. Let
\[
 H=2N,\quad L=3N/2-1,\quad
 C_h=\sum_n z_{n+h}\overline{z_n},\quad
 \rho_h=\frac8h\sum_{d\mid h}(-1)^{h+d}d,
\]
\[
 I_h=\int_0^\infty g_N(t+h)g_N(t)
 e(R(\sqrt{t+h}-\sqrt t))\,dt,\qquad
 {\cal R}_h=C_h-\rho_hI_h.
\]
The proposed hypothesis is, for each output \(\epsilon>0\) and fixed
sufficiently large \(J\), uniformly in all these parameters,
\[
 2\Re\sum_{h=1}^{2N-1}(1-h/(2N)){\cal R}_h
 \le C_{\epsilon,J}A_J^2N^{3/2}T^\epsilon.             \tag{V1}
\]
There is one outer real part and no absolute value on each remainder.
All shifts occur, including those beyond any favorable source regime.
The statement concerns the actual unmasked \(r_2\) wave, not the GAR
angular coefficient, an arbitrary vector, or a squarefree-deleted wave.

## 3. Independent derivation and full restoration

**Exact Fejer factor.** The possible nonzero integer sites are
\(\{N/2+1,\ldots,2N-1\}\), of length \(L\). For
\(U_m=\sum_{j=1}^H z_{m+j}\), zero extension gives
\[
 \sum_mU_m=H\sum_nz_n,\quad
 \#\operatorname{supp}U\le L+H-1,
\]
\[
 \sum_m|U_m|^2
 =H\sum_n|z_n|^2+
 2\Re\sum_{h=1}^{H-1}(H-h)C_h.
\]
Cauchy therefore proves exactly
\[
 \left|\sum_nz_n\right|^2\le
 \frac{L+H-1}{H}
 \left[\sum_n|z_n|^2+
 2\Re\sum_{h=1}^{H-1}(1-h/H)C_h\right].               \tag{V2}
\]
For the specified \(H\), its multiplier is \(7/4-1/N<2\).
There is no missing \(H\), \(N\), diagonal, or negative-shift factor.
The bracket equals \(H^{-1}\sum_m|U_m|^2\ge0\); this does not imply
positivity of its centered remainder. Only (V1)'s upper bound is needed.

**Density, all shifts and endpoints.** Every fixed scaled derivative
of \(g_N\) is \(O_J(A_J)\), using additional fixed Schwartz decay.
On a nonempty continuous overlap, \(t,t+h\in(N/2,2N)\). For
\(f_h(t)=R(\sqrt{t+h}-\sqrt t)\),
\[
 f_h'(t)=-\frac{Rh}
 {2\sqrt t\sqrt{t+h}(\sqrt{t+h}+\sqrt t)},\qquad
 |f_h'|\asymp ThN^{-3/2},\quad
 |f_h''/f_h'|\ll N^{-1}.
\]
The product amplitude has supremum \(O(A_J^2)\) and total variation
\(O(A_J^2)\), uniformly even when the overlap shrinks. Its smooth zero
extension kills the integration-by-parts boundary terms. Thus
\[
 |I_h|\ll_J A_J^2N^{3/2}/(Th).
\]
This argument covers the entire overlap range, not merely \(h\ll N\).
If the continuous overlap is empty, \(I_h=0\).

The two-adic density is retained: for \(h=2^ah'\), \(h'\) odd,
\[
 \rho_h=8|2^{a+1}-3|\sigma_1(h')/h>0,\qquad
 |\rho_h|\le8\sigma_1(h)/h\ll_\eta h^\eta.
\]
Hence its whole signed contribution may safely be bounded by
\[
 \sum_{h<2N}\rho_h|I_h|
 \ll_{\eta,J}A_J^2N^{3/2}T^{-1}N^\eta\log(2N).        \tag{V3}
\]
Near the last overlap a discrete correlation can be empty while
the continuous integral is nonzero. In that case
\({\cal R}_h=-\rho_hI_h\); the definition and full shift sum retain
the cancellation exactly. No assertion that both supports disappear
simultaneously is needed.

Using \(r_2(n)\ll_\eta n^{\eta/2}\), the complete diagonal is
\(\sum|z_n|^2\ll_{\eta,J}A_J^2N^{1+\eta}\). Substitution of
(V1),(V3) in (V2), followed by the actual shell factor \(N^{-3/2}\)
for the squared modulus, gives
\[
 \left|N^{-3/4}\sum_nz_n\right|^2
 \ll A_J^2\left[
 N^{-1/2+\eta}+T^{-1}N^\eta\log(2N)+T^\epsilon\right].
                                                               \tag{V4}
\]
Since \(N\le P<2T^{3/2}\), choosing \(\eta\) small and rescaling
\(\epsilon\) proves the claimed \(A_J^2T^{\epsilon'}\) bound.
Finite small \(T\), empty vectors and the smallest block \(N=2\)
are included by fixed constants.

**Exact recombination.** The coefficient normalization is literal:
\[
 N^{-3/4}g_N(n)=n^{-3/4}\Psi(\sqrt{n/T})w(n/N).
\]
Telescoping the dyadic scales gives
\[
 \sum_{N=2,4,\ldots,P}w(n/N)
 =\phi(n/P)-\phi(n)=\phi(n/P)\quad(n\ge2).
\]
For \(n=1\) the sum is zero, so the singleton is kept separately.
The remainder multiplier \(1-\phi(n/P)\) is bounded by a fixed
constant and vanishes for \(n\le P\). No monotonicity of \(\phi\)
is needed for this conclusion. For fixed decay order \(D\) large
enough, its absolute tail is at most
\[
 \ll_{\eta,D}T^{D/2}P^{1/4+\eta-D/2}
 \ll T^{3/8+3\eta/2-D/4}.
\]
It is \(O(T^{-A})\) for every requested fixed \(A\), after choosing
a sufficiently large fixed \(D\). Equality at a dyadic cutoff causes
no error. The source report uses the largest dyadic below \(T^{3/2}\);
the checkpoint uses the smallest one above it. Both are comparable to
\(T^{3/2}\), and the checkpoint explicitly requires (V1) up to its
larger \(P\). It does not silently apply the smaller-range hypothesis.

The singleton costs \(O(1)\). Taking square roots in (V4) and summing
the \(O(\log T)\) retained blocks, with a smaller input epsilon,
proves the full complex wave \(W_T(R)\ll_\epsilon T^\epsilon\).
The real wave is exactly
\(B_T(R)=\Re(e(-3/8)W_T(R))\). This is a stronger sufficient complex
route; no inherited complex or individual-block \(\beta\) is invoked.
Accepted204's inclusive bridge then gives
\[
 P(R^2)=\sqrt R\,B_T(R)/\pi+O(T^{1/2+\epsilon})
 \ll T^{1/2+\epsilon},
\]
which is the physical quarter bound after renaming epsilon. It pays
sharp annulus jumps and the complete Bessel remainder. For a general
complete exponent \(\gamma\), the bridge restores
\(1/4+\max(\gamma,0)/2\), as printed.

**Source-cost and moment consistency.** The checkpoint conservatively
summarizes the two frozen source reports. The first AH regime ends at
\(h\ll N^{64/69}\), since \(3/4+3(7/64)=69/64\). Its normalized
correlation error is \(N^{-5/6+\epsilon}\); absolute Abel transfer
costs \(1+Th/\sqrt N\). With Fejer length \(H\), summing these prices
and its prefactor produces \(N^{1/6}+THN^{-1/3}\), in addition to
the paid diagonal and density. At \(N=T^{2/3},h=1\), the phase
variation is \(T^{2/3}=N\). A fixed-test constant cannot hide it.
The Laplace factor \(h^\Theta\), all other shift regimes, and the
printed \(4/2\) mean-square exponent remain explicit.

The torus audit retains its legal three-dimensional lift and both
evaluation costs; its exponent \(N^{9/20}\) recombines to \(T^{9/20}\).
The quasicrystal specialization has growth parameter two and radius
exponent \(2/3\), hence physical \(1/3\) and real-wave \(1/6\).
The damped signed identity, its \(T^{-1/4+\epsilon}\) removal error
and its separately absolute \(T^{1/2+\epsilon}\) price are recorded
as candidate representation evidence, not a signed lower bound.
None improves the inherited complete real \(\beta\).

Both terms of accepted204's distribution and moment estimates survive.
The fixed twelfth target \(29/25\) remains only the \(102/325\)
milestone. The unbounded-fixed-order conditional route is consistent
with the class algebra; it does not extrapolate the proved twelfth
error. For a fixed even \(p\), each repeated-class term has \(r=p-s\),
\(s\ge2\), and at most \(s/2\) nonsingleton classes. The class bounds
give \(Q^{-s/4+\eta}\), so Holder followed by Young bounds its integral
by
\[
 C_pQ^{-s/4+\eta}T^{s/p}M_p(Z_Q)^{1-s/p}
 \le \delta M_p(Z_Q)+C_{p,\delta,\eta}TQ^{-p/4+O_p(\eta)}.
\]
There are only finitely many partitions for this fixed \(p\); choose
\(\delta\) to absorb them. With \(Q=\lfloor T^{1/p}\rfloor\), a
hypothetical one-sided \(I_p\ll T^{5/4+\epsilon}\), together with
the head bound \(TQ^{p/4}\ll T^{5/4}\), yields
\(M_p(B_T)\ll T^{5/4+\epsilon}\). The sharp moment bridge and
persistence then give \(1/4+7/[8(p+1)]\). An unbounded sequence of
fixed even \(p\) suffices for quarter; no constant uniform in \(p(T)\)
or unproved moment family has been supplied.

## 4. First doubtful or unproved step

The first unproved analytic statement is exactly (F)/(V1). Neither
the inspected sources nor the identities in this review prove it.
The new Heegner-point input motivates investigating the actual joint
spectral remainder, but its fixed-level fourth moment is not a bound
for the growing \(h,R,N\) test with every discrete and continuous
spectral contribution restored.

No further correctness gap was found in the checkpoint's conditional
sufficiency or bounded status conclusions. Failure of the stated
absolute transfers is not a disproof of (F), of the signed theta
alternative, or of the circle target.

## 5. Required controls and outcome

The following primary abstract/version records were inspected directly
on 2026-09-28; no new theorem-proof audit was performed.

| Primary record | Verified bounded status |
|---|---|
| [Li--Yang2308.14859](https://arxiv.org/abs/2308.14859) | v2, 14 September2023, latest listed. |
| [Bourgain--Watt1709.04340](https://arxiv.org/abs/1709.04340) | v2, 16 July2023, withdrawn; proof gaps and loss of theorem status stated. |
| [Dong--Robles--Zeindler2601.00292](https://arxiv.org/abs/2601.00292) | v2, 5 January2026, withdrawn; the omitted \(L^2\) factor removes the advertised gain. |
| [Kim2509.24152](https://arxiv.org/abs/2509.24152) | v4, 10 September2026, withdrawn; its stated assumptions make the comparison inferior to elementary Cauchy. |
| [Yamaguchi et al.2609.04725](https://arxiv.org/abs/2609.04725) | v1, 4 September2026; described as numerical evidence. |
| [HKLDW1705.04771](https://arxiv.org/abs/1705.04771) | v3, 1 April2020; ANT15(2021),1--27; no withdrawal displayed. |
| [Assing--Humphries2607.13518](https://arxiv.org/abs/2607.13518) | Only v1, 15 July2026, listed; no withdrawal displayed. |
| [Gan--He--Li--Wu2502.05973](https://arxiv.org/abs/2502.05973) | v2, 4 January2026, four authors; no withdrawal displayed. |
| [Edwin--Lin2412.05485](https://arxiv.org/abs/2412.05485) | Only v1, 7 December2024, listed; no withdrawal displayed. |

Metadata does not certify the full source proofs or establish that no
other relevant paper exists. The control makes neither assertion.
The graph retains exactly the five stated Li--Yang application repairs,
including bypassing false printed (4.9); the general source propositions
remain outside the accepted scope.

The graph still has 401 nodes. The complete M1 HARD and independent
SMOOTH owners, M2 TOP/BAL/UNBAL, all endpoints and lower GAR owners
remain open. The correct UNBAL phase and length are
\(e(\sqrt{Xhk})\) and \(K=XL/D^2\). GAR's paid nonlower part does
not remove its lower, generic, cross or M2 owners. The retained
closed224/225 controls concern their specified certificates.
No source assertion or complete improvement is promoted by this review.
All endpoint, empty-overlap, smallest-scale, sign and tail checks above
are analytic. Mathematical experiments: zero.

## 6. Dependencies and exact artifacts used

Current campaign root is
rounds/codex-managed/gc-full-goal-spectral-source-review/.
The two reviewed targets are bound in Section1. Other authorized
artifacts used, including disclosed earlier current work:

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 3f136e86091b999d4abf7db0b2141f4bced2e80480ee90a360c319c48b6e0d92 |
| strategy/round226_full_goal_spectral_source_review.md | 61ac5c2a26bf87f25133d8858dd2b4a0c6e377df657ddaeaa57d422d41e287ad |
| strategy/gauss_circle_strategy_review_2026-09-23.md | 0729f1d9c596867e7a06bdcd096847b32e6747653235706b01275a153bd617c6 |
| strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md | a0c75c5e2ef4ea45df4e388e3497d5be5133d6d49c7d7a2d71c166f11dd9dd33 |
| Current briefs/conductor_complete_spectral_interfaces.md | 8e9cb720ca0495aafc003434877dcd0067779993fc1edd5657b93d35ef9e77e5 |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |
| rounds/codex-managed/m9-m1-complete-gar-prime-amplification/synthesis.md | d5a94b25e876714c8e17602a497812afef3b42724a75dd4cc1501583d12fe98f |
| rounds/codex-managed/gc-complete-logarithmic-convolution/synthesis.md | c4324e2b8c75b8cb972ccf6a9e4f762ed9d8d648299acf7df77aff2b9b1546c7 |
| Current reports/actual_shifted_spectral_sources.md | 1bcb14e1899138097a3ab0e273060f2deaa800e3eb732e2924afb2f1f02d25bc |
| Current reports/theta_wave_full_frontiers.md | e5e95a4d49ab5220b0533e52a92f6d2fb727d3f4b475ce4813ab3ab698d69c79 |
| My frozen current reports/blind_complex_subordination.md | 35b28a172e791013cab241a44d47c43b0aea8fd6f7e372be3665b48146a45c0e |
| My frozen current reviews/independent_subordination_application_review.md | 3fed467c46d3a69b0a663c72aa20ae4c971279dbb9c3f4bb87382e69a9219860 |

The primary URLs in Section5 are metadata sources only in this review.
The current source reports supply the bounded audited theorem statements;
this review checks their use in the checkpoint without re-auditing source
proofs. I do not count my own earlier work as independent review of itself.
No sibling reviews or unlisted source texts were read, and only this
assigned review was written.

## 7. Recommended state effect

Retain both targets with scoped GREEN. The quantified next objective is
the single complete signed inequality (F), not an established spectral
gain. The checkpoint explicitly takes effect only after validated226
closure; it does not open227. Its proposed State Patch is the identity,
with graph and proof-draft acceptance unchanged and all complete owners
preserved. Actual closure and archive validation remain the conductor's
responsibility. Stop after this review's final hash; no successor work.
