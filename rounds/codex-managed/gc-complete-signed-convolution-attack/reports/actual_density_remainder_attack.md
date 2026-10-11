# Round 203: actual density subtraction and the complete remainder

Campaign: `gc-complete-signed-convolution-attack`. Task: `actual_density_remainder_attack`. Role: discovery, selected-context access. Date: 2026-09-23. Starting graph SHA-256: `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`. Candidate evidence only. The task used analytical/algebraic reasoning, no experiments and no new external theorem. Only the permitted context was consulted; no sibling derivation was read.

## 1. Result: the continuous bulk is negligible, but its complete remainder preserves the difficulty

The exact area-density subtraction gives a finite complex measure
\[
 d\lambda_{T,U}(y)=\pi |y|^{-1/2}\Psi(|y|/\sqrt T)
 \left\{e(-3/8)1_{y>\sqrt U}+e(3/8)1_{y<-\sqrt U}\right\}dy.
 \tag{1}
\]
Write \(\mu=\mu_{T,>U}=\lambda+\eta\), and let their inverse Fourier transforms be \(B=G+E\). Uniformly on the fixed physical window \(R\asymp T\),
\[
 |G(R)|\ll T^{-1}U^{-1/4},\qquad
 \|K_T*\lambda^{*6}\|_2\ll T^{-11/2}U^{-3/2}.
 \tag{2}
\]
Every term containing at least one density factor is controlled. With the inherited physical supremum and independently derivable tail second moment,
\[
 \boxed{\ \|K_T*(\mu^{*6}-\eta^{*6})\|_2
 \ll_\varepsilon T^{-1/2+4\beta+\varepsilon}U^{-1/2}\ },
 \qquad U=\lfloor T^{1/2047}\rfloor.
 \tag{3}
\]
Here \(\beta=2\theta-1/2\), so the displayed power of \(T\), before the favorable cutoff factor, is \(0.0158654077\ldots\). Thus the desired norm bound is equivalent, up to an already subtarget error, to
\[
 \|K_T*\eta^{*6}\|_2\ll_\varepsilon T^{29/50+\varepsilon}.
 \tag{4}
\]
The term \(\eta^{*6}\) cannot be omitted from a claimed density approximation. Exact Stieltjes summation displays it in terms of the original discrepancy; the accepted summatory bound alone does not estimate its high oscillation. The bounded attempt obtains no new exponent.

With the explicitly inherited, source-reviewed \(q_0=262/27\) moment benchmark and its smoothing interface, the strongest actual-coefficient inequality available here is still
\[
 \boxed{\ \|K_T*\mu^{*6}\|_2+\|K_T*\eta^{*6}\|_2
 \ll_\varepsilon T^{1/2+(12-q_0)\beta/2+\varepsilon}
 =T^{0.648072478\ldots+\varepsilon}\ }.
 \tag{5}
\]
This benchmark retains its inherited candidate source/interface status. The missing norm saving is exactly
\[
 \frac{(12-q_0)\beta}{2}-\frac2{25}
 =0.068072478\ldots.
 \tag{6}
\]
Neither (3) nor the density's smallness supplies that saving for the pure remainder.

## 2. Exact statement and hypotheses

Let \(T\ge2\) be real and \(U=\lfloor T^{1/2047}\rfloor\). Use the fixed real even Schwartz function \(\Psi\) with \(\Psi(0)=1\) arising from the prescribed radial mollifier. Let \(\chi\ge0\) be the fixed smooth compactly supported function in \((0,\infty)\), and put \(w=\chi^2\). Constants may depend on these fixed functions and on \(\varepsilon\), never on \(T\), \(U\), or physical \(R\). Fourier transform means \(\widehat f(\xi)=\int f(R)e(-R\xi)dR\).

The exact quantities are
\[
 a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),
\]
\[
 \mu=\frac12\sum_{n>U}a_n(T)
 \{e(-3/8)\delta_{\sqrt n}+e(3/8)\delta_{-\sqrt n}\},
 \quad K_T(\xi)=T\widehat\chi(T\xi),
\]
\[
 B(R)=\sum_{n>U}a_n(T)\cos(2\pi R\sqrt n-3\pi/4).
 \tag{7}
\]
All measures used below have finite total variation at each fixed \(T\). The signed measures and the oscillatory filter are kept inside the convolution until physical-space estimates are applied.

Set
\[
 A(x)=\sum_{1\le n\le x}r_2(n)=\pi x+Q(x),\qquad Q(x)=P(x)-1.
 \tag{8}
\]
This convention includes the lattice origin in \(P\) and includes the jump at an integer \(x\) in \(A(x)\). The accepted graph theorem gives \(Q(x)\ll_\varepsilon x^{\theta+\varepsilon}\), where
\[
 \theta=\frac{3292+25\sqrt{1717}}{13762},\qquad 1/4<\theta<1/2.
 \tag{9}
\]
The exact subtraction, (2), and the Stieltjes estimates below use only (8), (9), Schwartz decay and elementary coefficient bounds. The improved physical supremum used in (3) is the inherited smoothing consequence
\[
 \|B\|_{\infty,\operatorname{supp}\chi(R/T)}
 \ll_\varepsilon T^\varepsilon(T^\beta+U^{1/4})
 \ll_\varepsilon T^{\beta+\varepsilon}.
 \tag{10}
\]
Its full-series smoothing identity remains the specific candidate interface in the permitted Round-202 audit; it is not newly promoted here. Formula (5) additionally uses that audit's source-reviewed endpoint
\[
 \int w(R/T)|B(R)|^{q_0}dR\ll_\varepsilon T^{1+\varepsilon}.
 \tag{11}
\]
No stronger external moment theorem is assumed.

## 3. Proof and complete cost accounting

### Exact density and its displaced-window cancellation

Replace \(dA(x)\) by its area part \(\pi dx\) in the two signed branches of (7), retaining the hard lower cutoff. The substitution \(x=y^2\) gives exactly (1), including its factor \(\pi\), both phases, and the support \(|y|>\sqrt U\). Therefore
\[
 G(R)=\pi\int_U^\infty x^{-3/4}\Psi(\sqrt{x/T})
                  \cos(2\pi R\sqrt x-3\pi/4)dx
 =2\pi\int_{\sqrt U}^\infty y^{-1/2}\Psi(y/\sqrt T)
                  \cos(2\pi Ry-3\pi/4)dy.
 \tag{12}
\]
For \(b(y)=y^{-1/2}\Psi(y/\sqrt T)\), Schwartz decay and \(U\le T\) give
\[
 |b(\sqrt U)|+\int_{\sqrt U}^\infty|b'(y)|dy\ll U^{-1/4}.
\]
One integration by parts in the linear phase, including the lower boundary, proves \(|G(R)|\ll |R|^{-1}U^{-1/4}\). Since \(R\asymp T\) on the window, Plancherel proves (2). This cancellation estimate is for the actual continuous density; it makes no claim that the atomic measure is approximated by that density after six convolutions.

### Exact Stieltjes remainder, with every derivative restored

Put \(F_T(x)=x^{-3/4}\Psi(\sqrt{x/T})\) and \(\phi_R(x)=2\pi R\sqrt x-3\pi/4\). Stieltjes integration on \((U,\infty)\), with the right-continuous value \(Q(U)\), gives the identity
\[
 E(R)=B(R)-G(R)
 =-Q(U)F_T(U)\cos\phi_R(U)
   -\int_U^\infty Q(x)F_T'(x)\cos\phi_R(x)dx
   +\pi R\int_U^\infty Q(x)x^{-5/4}\Psi(\sqrt{x/T})
                                      \sin\phi_R(x)dx.
 \tag{13}
\]
The upper boundary is zero. All three terms converge absolutely at fixed \(T,R\); the Schwartz cutoff is still present at every \(x>U\). In particular,
\[
 F_T'(x)=-\frac34x^{-7/4}\Psi(\sqrt{x/T})
       +\frac1{2\sqrt T}x^{-5/4}\Psi'(\sqrt{x/T}).
 \tag{14}
\]
Call the first two terms in (13) \(L(R)\) and the final term \(J(R)\). For an arbitrarily small fixed \(\kappa>0\), chosen with \(\theta+\kappa<3/4\), direct integration yields
\[
 |L(R)|\ll_\kappa U^{\theta-3/4+\kappa}.
 \tag{15}
\]
For the second term of (14), substitute \(x=Tz^2\): its bound is \(O(T^{\theta-3/4+\kappa})\), which is at most the right side of (15). Thus the amplitude derivative is not discarded.

In contrast, the absolute estimate of the phase derivative is
\[
 |J(R)|\ll_\kappa |R|\int_U^\infty
       x^{\theta-5/4+\kappa}|\Psi(\sqrt{x/T})|dx
 \ll_\kappa T^{\theta+3/4+\kappa}\quad(R\asymp T).
 \tag{16}
\]
The integral is controlled at its effective upper scale because \(\theta>1/4\). The factor \(R\) in (13) is essential. Summatory control of one set of \(r_2\) weights therefore supplies neither a small oscillatory remainder nor a sixfold approximation theorem. Reintegrating (13) against \(dQ\) simply returns the original discrete tail.

For comparison, finite variation already gives \(|B|+|E|\ll_\varepsilon T^{1/4+\varepsilon}\), stronger than (16). With (10), the actual physical bound is stronger still. Thus (16) is the failed estimate in this density mechanism, not a claim to have improved the known bound.

### Tail second moment and all density/remainder mixed terms

The actual second moment can be derived without a density approximation:
\[
 \int w(R/T)|B(R)|^2dR
 =\frac T2\widehat w(0)\sum_{n>U}a_n(T)^2+O_K(T^{-K})
 \ll_\varepsilon T^{1+\varepsilon}U^{-1/2}.
 \tag{17}
\]
To see this, temporarily restrict to \(n\le V=\lfloor T^{1+\alpha}\rfloor\), \(0<\alpha<1\). For distinct \(m,n\le V\),
\[
 T|\sqrt m-\sqrt n|\ge T|m-n|/(2\sqrt V)
 \gg T^{(1-\alpha)/2}|m-n|.
\]
Schwartz decay of \(\widehat w\) gives an arbitrarily small absolute row sum for the difference-frequency off-diagonal, after \(2|a_ma_n|\le a_m^2+a_n^2\). Sum frequencies are also negligible. The diagonal uses \(r_2(n)\ll_\kappa n^\kappa\), and the upper tail is restored below. By (2), (17) also gives
\[
 \|\chi(R/T)E(R)\|_2\ll_\varepsilon T^{1/2+\varepsilon}U^{-1/4}.
 \tag{18}
\]

Convolution and Plancherel now give the exact finite expansion
\[
 K_T*\mu^{*6}=\sum_{j=0}^6\binom6j K_T*(\lambda^{*(6-j)}*\eta^{*j}),
\]
\[
 \|K_T*(\lambda^{*(6-j)}*\eta^{*j})\|_2
       =\|\chi(R/T)G(R)^{6-j}E(R)^j\|_2.
 \tag{19}
\]
This is valid for complex measures: the inverse transforms are real by conjugate symmetry, and the usual complex Plancherel identity also suffices. At \(1\le j\le5\), (2), (10) and (18) imply
\[
 \|\chi G^{6-j}E^j\|_2
 \ll_\varepsilon
 T^{1/2-(6-j)+(j-1)\beta+\varepsilon}
 U^{-(7-j)/4}.
 \tag{20}
\]
The \(j=0\) term is (2). Among \(j\le5\), (20) is largest at \(j=5\), proving (3). The same conclusion can be checked directly from
\[
 |B^6-E^6|\le C|G|(|B|+|E|)^5
\]
by taking four factors in the supremum and one in weighted \(L^2\). These are estimates after physical signed summation, not termwise absolute Fourier-kernel bounds.

If (11) is also used, then \(\int w|E|^{q_0}\ll T^{1+\varepsilon}\). For \(1\le j\le4\), interpolation with (18) gives
\[
 \|\chi G^{6-j}E^j\|_2
 \ll_\varepsilon T^{1/2-(6-j)+\varepsilon}
 U^{-(6-j)/4-(q_0-2j)/(4(q_0-2))}.
 \tag{21}
\]
For \(j=5\), using \(\|E\|_\infty^{10-q_0}\int w|E|^{q_0}\) gives
\[
 \|\chi GE^5\|_2
 \ll_\varepsilon T^{-1/2+(10-q_0)\beta/2+\varepsilon}U^{-1/4}.
 \tag{22}
\]
Consequently the entire difference in (3) satisfies the stronger right side of (22), with exponent \(-0.4808938737\ldots\). The \(j=6\) term is precisely the unremoved remainder. Its known estimate is (5), by the same interpolation with power \(12-q_0\). Without (11), the inherited supremum and (18) give only
\[
 \|K_T*\eta^{*6}\|_2\ll_\varepsilon
 T^{1/2+5\beta+\varepsilon}U^{-1/4}.
 \tag{23}
\]
Without the inherited smoothing supremum as well, the elementary coefficient supremum gives \(T^{7/4+\varepsilon}U^{-1/4}\). None of these becomes smaller merely by naming \(\eta^{*6}\) an error.

### Infinite upper tails and all twelfth/head cross terms

For every fixed \(M\) and \(V\ge T\), the discrete and continuous total variations above \(x=V\) obey
\[
 \|\mu_{n>V}\|_{\rm TV}+\|\lambda_{|y|>\sqrt V}\|_{\rm TV}
 \ll_{M,\kappa} T^{M/2}V^{1/4+\kappa-M/2}.
 \tag{24}
\]
Their complete variations are \(O(T^{1/4+\kappa})\), as is that of \(\eta\). At \(V=T^{1+\alpha}\), (24) is \(O(T^{-K})\) for any fixed \(K\) on choosing \(M\) sufficiently large. Young's inequality prices the error in every filtered sixth power by
\[
 O\!\left(\|K_T\|_2 T^{5/4+5\kappa}T^{-K}\right)
 =O(T^{7/4+5\kappa-K}).
 \tag{25}
\]
Likewise the total absolute twelfth-product integral having at least one discarded factor is \(O(T^{15/4+11\kappa-K})\). These estimates cover every sign and every mixed stratum. Our actual definitions never remove these tails; (24)-(25) justify the one temporary truncation in the derivation of (17). A cutoff at \(n=T\) would not suffice.

All cross terms in the square of (19) are included in its \(L^2\) norm. In particular, (3) bounds the difference of the norms by the reverse triangle inequality, rather than silently setting cross inner products to zero.

For the original full series, let \(A_0\) be the head \(n\le U\). The inherited reviewed head bound is \(\int w|A_0|^{12}\ll T\). If the target tail bound held, every head/tail term would satisfy
\[
 \left|\int w A_0^{12-j}B^j\right|
 \le\left(\int w|A_0|^{12}\right)^{(12-j)/12}
      \left(\int w|B|^{12}\right)^{j/12}
 \ll_\varepsilon T^{1+j/75+\varepsilon},\quad 0\le j\le12.
 \tag{26}
\]
Thus none is missing. The actual established bound uses \(1+(12-q_0)\beta j/12\) in place of \(1+j/75\), and supplies no new exponent.

## 4. First doubtful or unproved step

No gap occurs in the area-density calculation, Stieltjes identity, or finite binomial bookkeeping. The first needed new analytic estimate is (4). Equivalently, in (13) it is
\[
 \boxed{\ \int w(R/T)\left|\pi R\int_U^\infty
 (P(x)-1)x^{-5/4}\Psi(\sqrt{x/T})
 \sin(2\pi R\sqrt x-3\pi/4)dx\right|^{12}dR
 \ll_\varepsilon T^{29/25+\varepsilon}\ }.
 \tag{27}
\]
Indeed \(E=J+L\), and (15) gives \(\int w|L|^{12}\ll T U^{12(\theta-3/4+\kappa)}\ll T\). Weighted \(L^{12}\) triangle inequalities show that (27) and (4) are equivalent at the target exponent. If either target is granted, Hölder prices every \(L/J\) mixed twelfth product as well; there is no extra remainder assumption.

The pointwise summatory estimate gives (16), not (27). With the inherited strongest moment data the left side of (27) is bounded only by \(T^{1+(12-q_0)\beta+\varepsilon}\). Hence its missing moment saving is \((12-q_0)\beta-4/25\), twice (6). A proof of this oscillatory high-moment estimate would be new arithmetic information about the discrepancy; it cannot be inferred from the area term of (8).

This is a quantitative failure of this bounded density-plus-summatory attempt. It is not a theorem excluding other coefficient-sensitive approximations or a lower bound contradicting the desired signed moment.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| `actual_coefficients` | PASS: (1) is derived from the exact actual \(r_2\) Stieltjes sum; the remainder is exactly \(d(P-1)\), with the prescribed Schwartz factor. No random or independent squarefree coefficients are substituted. |
| `complete_tail_and_cross_terms` | PASS: (19) includes every density/remainder stratum; its square includes all cross terms. (24)-(26) restore upper tails and every low-head/tail term. |
| `signed_filter_preserved` | PASS: the two phases remain in (1), (7), and (19); bounds are made after inverse transformation. No absolute Fourier majorant is used. |
| `all_errors_priced` | PASS: the lower boundary, both parts of \(F_T'\), the \(R\)-weighted phase derivative, pure remainder, all mixed terms, and upper tails are explicit. |
| `real_uniformity` | PASS: the argument uses real \(T,R\), fixed windows, inclusive \(Q(U)\), and a hard integer \(U\); bounded parameter values are absorbed in constants. |
| `net_exponent` | PASS as no-gain audit: density terms are subtarget; pure remainder retains (5), leaving exactly (6) unproved. |
| `independent_statement_only_control` | Not performed by this selected-context discovery task. No sibling report was read. The conductor's separately assigned statement-only review remains required before any promotion. |
| `no_parent_overclaim` | PASS: (4)/(27), the proposed intermediate exponent, the quarter theorem and internal M1/M2/M9 obligations are not proved or refuted. |

A coefficient-sensitive falsification control for calling \(E\) negligible is available without experiments. From (8), for sufficiently large \(U\),
\[
 \sum_{U<n\le2U}r_2(n)\gg U.
\]
At our cutoff, \(U/T\to0\), so \(\Psi(\sqrt{n/T})\ge1/2\) on this block for sufficiently large \(T\). Cauchy-Schwarz then gives
\[
 \sum_{n>U}a_n(T)^2\gg U^{-3/2}
 \frac{(\sum_{U<n\le2U}r_2(n))^2}{U}\gg U^{-1/2}.
\]
By (17), \(\|\chi B\|_2\gg T^{1/2}U^{-1/4}\), whereas \(\|\chi G\|_2\ll T^{-1/2}U^{-1/4}\). Therefore
\[
 \|\chi E\|_2\gg T^{1/2}U^{-1/4}.
 \tag{28}
\]
The density captures a negligible part of the actual quadratic fluctuation on this displaced window. This control invalidates dropping the remainder; it does not contradict a twelfth-moment upper target. The implied lower bound for its sixth-power norm is only of scale \(T^{1/2}U^{-3/2}\), below the target.

## 6. Dependencies and exact artifacts used

The exact permitted local context used was:

- `protocol.md`.
- `state/proof_obligations.yml`, specifically the accepted repaired `GC-external-Li-Yang-theta-star`, elementary divisor bound, exact-resonance mass, physical absolute-majorant obstruction, and open target scopes.
- `state/active_campaign.yml`, Round 203, including this task's assigned output path.
- `strategy/round203_complete_signed_convolution_attack.md`.
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/candidates/conductor_signed_convolution_interface.md`.
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/signed_cutoff_tail_moment_audit.md`.
- This task's brief, `rounds/codex-managed/gc-complete-signed-convolution-attack/briefs/actual_density_remainder_attack.md`.

The physical smoothing, safe-head and printed \(q_0\) benchmark have exactly the inherited evidentiary qualifications stated in Sections 1-2. They are not upgraded by this report. The direct density identity and the loss (16) need no imported moment theorem. No external source check was essential; none was made. The conductor suggested a mixed-term consistency check during the task; its stronger \(L^2\) form (20) was verified directly here. No sibling or isolated-review output was accessed.

## 7. Recommended state effect

**No change** to the accepted graph or proof draft. **Retain** the exact density/remainder interface and its fully priced mixed terms as candidate evidence for this round's reconciliation. **Reject** the inference that the one-variable summatory asymptotic makes the complete sixfold filtered remainder small, and reject omission of \(\eta^{*6}\) or the phase derivative in (13).

The appropriate result for this bounded mechanism is `complete_analytic_attempt_no_new_bound`. Any promotion of the elementary interface still requires the conductor's independent seam checks; no exponent or parent obligation is discharged. This report ends the assigned task and proposes no successor round.
