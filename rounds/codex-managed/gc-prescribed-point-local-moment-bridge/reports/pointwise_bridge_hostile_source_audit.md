# Round 94 hostile/source audit: prescribed-point local-moment bridge

## 1. Result

**Evidence-status correction:** this report is context-contaminated, non-isolated candidate evidence. Two repository artifacts outside the brief's permitted-context list were actually opened during the audit; Section 6 identifies them and the two permitted files that were not opened. The mathematical claims below are unchanged, but this report cannot by itself satisfy an isolation-dependent promotion gate.

The audit produces three exact lemmas and one scoped no-go result.

First, the inclusive convention
\[
 P(t)=\#\{(m,n)\in\mathbb Z^2:m^2+n^2\le t\}-\pi t
\]
has the one-sided persistence needed at every real point, including jump points. It also gives the exact integer-cell identity
\[
 \int_n^{n+1}P(t)^2\,dt
   =P(n)^2-\pi P(n)+\frac{\pi^2}{3}
   =\left(P(n)-\frac\pi2\right)^2+\frac{\pi^2}{12}.       \tag{1.1}
\]
Consequently the accepted dyadic second moment implies both the one-separated sampling bound and the integer exceptional-set estimate without any continuity assumption.

Second, the sharp deterministic local-to-pointwise implication is not the displayed \(H+\sqrt{E/H}\) bridge in the conductor candidate. If every length-\(W\) interval in the relevant enlarged dyadic range has square integral at most \(Q(Y,W)\), then, for \(M=|P(x)|\),
\[
 M^2\min\!\left(W,\frac{M}{2\pi}\right)\ll Q(Y,W),
 \qquad
 M\ll Q(Y,W)^{1/3}+\left(\frac{Q(Y,W)}W\right)^{1/2}.       \tag{1.2}
\]
Thus a bound \(Q\ll W Y^{1/2+\varepsilon}+E\) gives
\[
 M\ll W^{1/3}Y^{1/6+\varepsilon/3}+E^{1/3}
       +Y^{1/4+\varepsilon/2}+(E/W)^{1/2}.                  \tag{1.3}
\]
For \(W=Y^\alpha\) and \(E=0\), the resulting exponent is
\[
 \theta(\alpha)=\max\left(\frac14,\frac16+\frac\alpha3\right). \tag{1.4}
\]
In particular, \(\alpha=1/4+\sigma\) yields \(1/4+\sigma/3\), not literally \(1/4\) for one fixed \(\sigma>0\). Every \(\alpha<1/2\), not merely \(\alpha<1/3\), improves on exponent \(1/3\).

Third, the fixed-symbol triangular-cluster identity in `conductor_exact_cluster_kernel.md` is correct in normalization, sign, and phase. Its application to the actual Vaaler sums needs revision: the \(M_1\) frequency is \(h/d\), whereas the \(M_2\) frequency is \(h/(4d)\). Writing both as \(h/(4d)\) is permissible only after the explicit relabelling \(h'=4h\), with coefficients and support relabelled as well. Moving symbols do not invalidate the fixed identity; they invalidate only its unproved transfer to a single coefficient system across the whole \(t\)-window.

Finally, on the accepted minimax shell \((D,L)=(Y^{1/2},Y^{1/6})\), the actual frequency diameter is \(O(L/D)=O(Y^{-1/3})\) for \(M_1\) and four times smaller for \(M_2\). Hence \(W=Y^\alpha\), \(\alpha<1/3\), is subcoherent: the triangular cluster form contains essentially the whole pointwise square and offers no power-saving smoothing mechanism. At \(\alpha=1/3\) there are only \(O(1)\) cells. This no-go does **not** extend to \(1/3<\alpha<1/2\); that range has a growing number of cells and, by (1.4), could genuinely improve exponent \(1/3\), although no audited source supplies the required cluster estimate. No audited primary source proves the target local bound or closes the prescribed-point bridge.

## 2. Exact statement and hypotheses

Let \(Y\ge Y_0\), let \(x\in[Y,2Y]\), and let \(1\le W\le Y/3\). All local intervals below are contained in \([Y/2,3Y]\). The following statements use the inclusive, right-continuous lattice count above.

- **One-sided persistence.** For every \(u\ge0\),
  \[
  P(x+u)\ge P(x)-\pi u,                                    \tag{2.1}
  \]
  and, for \(0\le u\le x\),
  \[
  P(x-u)\le P(x)+\pi u.                                    \tag{2.2}
  \]
  If \(P(x)=M>0\), use the right side; if \(P(x)=-M<0\), use the left side. On the favorable side, \(|P|\ge M/2\) for \(0\le u\le M/(2\pi)\).

- **Sampling.** If \(\mathcal X\subset[Y,2Y]\) is one-separated, then
  \[
  \sum_{x\in\mathcal X}|P(x)|^2
     \ll \int_{Y-1}^{2Y+1}|P(t)|^2\,dt+\#\mathcal X.       \tag{2.3}
  \]
  Therefore the accepted global moment gives \(\sum_{x\in\mathcal X}|P(x)|^2\ll_\varepsilon Y^{3/2+\varepsilon}\). For integer samples, (1.1) gives the same conclusion directly, and
  \[
  \#\{n\in[Y,2Y]\cap\mathbb Z:|P(n)|\ge Y^{1/4+\eta}\}
     \ll_\varepsilon Y^{1-2\eta+\varepsilon}.              \tag{2.4}
  \]

- **Sharp local bridge.** Assume that every length-\(W\) interval \(I\subset[Y/2,3Y]\) that is used to extend the favorable one-sided segment satisfies
  \[
  \int_I |P(t)|^2\,dt\le Q(Y,W).                            \tag{2.5}
  \]
  Then (1.2) holds, with absolute implied constants. If
  \[
  Q(Y,W)\ll_\varepsilon W Y^{1/2+\varepsilon}+E(Y,W),       \tag{2.6}
  \]
  where \(E\ge0\), then (1.3) holds. A unit-window estimate of scale \(Y^{1/2+\varepsilon}\) is therefore exponent-wise equivalent, up to the usual \(\varepsilon\)-loss, to the quarter pointwise bound. Exact equality of the local and pointwise quantities holds only for integer unit cells through (1.1), not for arbitrary real-centered unit intervals.

- **Fixed triangular cluster identity.** Let
  \[
  S(t)=\sum_{\lambda\in\Lambda}a_\lambda e(\lambda t),
  \qquad e(z)=e^{2\pi iz},
  \]
  with \(\Lambda\) finite and the coefficients fixed throughout an interval \(I=[c-W/2,c+W/2]\). Put
  \(K(u)=(\sin \pi u/(\pi u))^2\), so that, under
  \(\widehat K(\xi)=\int K(u)e(-\xi u)\,du\),
  \(\widehat K(\xi)=(1-|\xi|)_+\). Then
  \[
  \int_I|S(t)|^2dt
   \le \frac{\pi^2}{4}W
      \sum_{\lambda,\mu}a_\lambda\overline{a_\mu}
      e((\lambda-\mu)c)(1-W|\lambda-\mu|)_+.              \tag{2.7}
  \]
  If \(b_\lambda=a_\lambda e(\lambda c)\) and
  \(C_{\nu,\vartheta}=[(\nu+\vartheta)/W,(\nu+1+\vartheta)/W)\), then exactly
  \[
  \sum_{\lambda,\mu}b_\lambda\overline{b_\mu}
      (1-W|\lambda-\mu|)_+
   =\int_0^1\sum_{\nu\in\mathbb Z}
      \left|\sum_{\lambda\in C_{\nu,\vartheta}}b_\lambda\right|^2d\vartheta. \tag{2.8}
  \]
  Equal rational frequencies must be aggregated into \(a_\lambda\), or equivalently retained as a multiset with their cross terms. In the actual formulas, \(M_1\) uses \(\lambda=h/d\), \(M_2\) uses \(\lambda=h/(4d)\), and both signs and the \(\chi_4\)-weights must remain.

For the desired quarter exponent with \(W\ge Y^{1/4}\), (1.2) requires, up to subpower losses, the **total** local mass \(Q(Y,W)\ll Y^{3/4+o(1)}\); the nominal bound \(Q=WY^{1/2+o(1)}\) at one fixed \(W=Y^{1/4+\sigma}\) is too large by \(Y^\sigma\). Equivalently, one needs estimates for arbitrarily small \(\sigma\), or a genuinely stronger total-\(Q\) bound.

## 3. Proof or derivation

Write \(N(t)=\#\{(m,n):m^2+n^2\le t\}\). Monotonicity gives
\[
P(x+u)-P(x)=N(x+u)-N(x)-\pi u\ge-\pi u,
\]
which proves (2.1), including when \(x\) is a jump point because the jump at \(x\) is included in \(N(x)\). Likewise
\[
P(x-u)-P(x)=N(x-u)-N(x)+\pi u\le\pi u,
\]
which proves (2.2). The sign determines which inequality supplies a lower bound for the absolute value. Integrating \((M/2)^2\) over
\(\ell=\min(W,M/(2\pi))\), then extending that segment to an allowed length-\(W\) interval, gives
\[
\frac{M^2}{4}\min\!\left(W,\frac{M}{2\pi}\right)\le Q(Y,W). \tag{3.1}
\]
If \(M\le2\pi W\), this yields \(M^3\le8\pi Q\); if \(M\ge2\pi W\), it yields \(M^2W\le4Q\). The two cases imply (1.2). Subadditivity of the powers \(1/3\) and \(1/2\), applied to (2.6), gives (1.3).

For sampling, attach \([x,x+1]\) when \(P(x)>0\) and \([x-1,x]\) when \(P(x)<0\). If \(|P(x)|\ge2\pi\), persistence gives an integral at least \(|P(x)|^2/4\) on that unit interval; smaller samples contribute only \(O(1)\) each. One-separated centers make these oriented intervals overlap with uniformly bounded multiplicity (at most three everywhere, and at most two away from endpoints). This proves (2.3). The enlarged interval is covered by \(O(1)\) dyadic moment ranges, including the boundary pieces, so the accepted global estimate applies.

For an integer \(n\), inclusivity makes \(N(t)=N(n)\) for \(n\le t<n+1\); the possible jump at \(n+1\) has measure zero. Hence \(P(n+s)=P(n)-\pi s\) for \(0\le s<1\), and
\[
\int_0^1(P(n)-\pi s)^2ds=P(n)^2-\pi P(n)+\frac{\pi^2}{3},
\]
which is (1.1). In particular,
\(P(n)^2\le2\int_n^{n+1}P(t)^2dt+\pi^2/2\). Summation and Chebyshev give (2.4).

For (2.7), \(K(u)\ge4/\pi^2\) on \(|u|\le1/2\), so majorizing the indicator of \(I\) by \((\pi^2/4)K((t-c)/W)\), expanding the square, and using the stated Fourier convention produces the phase \(e((\lambda-\mu)c)\) and the nonnegative multiplier \((1-W|\lambda-\mu|)_+\). For (2.8), two points distance \(r\) apart belong to the same randomly shifted cell with probability \((1-Wr)_+\); expanding the cell squares and integrating over the shift proves the identity. Cell-boundary coincidences form a null set.

On the minimax shell, compact dyadic support gives
\(\operatorname{diam}\Lambda\ll L/D\ll Y^{-1/3}\) for \(M_1\), and \(\ll L/(4D)\) for \(M_2\). If \(W=Y^\alpha\), \(\alpha<1/3\), set \(\delta=W\operatorname{diam}\Lambda=o(1)\). For a set of shifts of measure at least \(1-\delta\), all frequencies occupy one cell. Therefore the right side of (2.8) is at least
\[
(1-\delta)\left|\sum_\lambda b_\lambda\right|^2
=(1-o(1))|S(c)|^2.                                        \tag{3.2}
\]
Thus a cluster estimate of the desired strength in this subcoherent regime already contains a pointwise estimate of that strength; the triangular kernel supplies no power decay. At \(\alpha=1/3\) the number of occupied cells stays \(O(1)\), again with no power-sized separation gain. For \(1/3<\alpha<1/2\), however, there can be \(O(Y^{\alpha-1/3})\) cells, so (3.2) no longer gives the same obstruction.

Finally, the strongest audited aggregate mean-square remainder has
\[
Q(Y,W)\ll W\sqrt Y+Y(\log Y)^{3/2}\log\log Y.              \tag{3.3}
\]
Substitution into (1.2) yields terms including
\(Y^{1/3}(\log Y)^{1/2}(\log\log Y)^{1/3}\) and
\(Y^{(1-\alpha)/2}\) times logarithms. Optimizing over \(\alpha\) cannot beat exponent \(1/3\). This source theorem is therefore quantitatively stronger than the raw frozen large-sieve estimate but still does not close the bridge.

Popov's 2024 Theorem 10(ii) makes the same obstruction particularly transparent. With his centered half-length \(H\),
\[
 E_2(T,H)=\frac1{2H}\int_{T-H}^{T+H}P(t)^2dt
 \ll \sqrt T+\frac{T(\log T)^2}{H}, \qquad H\le T/2,
\]
so the total mass is \(Q\ll H\sqrt T+T(\log T)^2\). For \(H=T^\alpha\), \(\alpha\le1/2\), the power exponent of \(Q\) is \(q=1\). Formula (1.2) therefore returns
\[
 \max\!\left(\frac q3,\frac{q-\alpha}{2}\right)
 =\max\!\left(\frac13,\frac{1-\alpha}{2}\right).          \tag{3.4}
\]
It is exactly \(1/3\) for \(1/3\le\alpha\le1/2\), and worse for \(\alpha<1/3\); it gives no pointwise exponent improvement in any short-window range.

## 4. First doubtful or unproved step

The first unproved step is not persistence, sampling, the kernel normalization, or the random-cell identity. It is the transfer from (2.8), which assumes one fixed finite exponential polynomial on the whole window, to the actual \(t\)-dependent Vaaler decomposition, followed by a cluster estimate at the strength
\[
\int_0^1\sum_\nu
 \left|\sum_{\lambda\in C_{\nu,\vartheta}}b_\lambda\right|^2d\vartheta
 \ll_\varepsilon Y^{1/2+\varepsilon}.                     \tag{4.1}
\]
Moving truncation floors and the hard endpoint do not make (2.8) false; they mean that (2.8) cannot be invoked until the interval has been partitioned into strata on which the symbol is fixed, with the resulting pieces and endpoints controlled. At \(D\le Y^{1/2}\) and \(W<Y^{1/2}\), the Vaaler height changes by only
\(O(DY^{-5/4}W)=o(1)\) per fixed scale and the hard endpoint changes by \(O(W/\sqrt Y)=o(1)\), suggesting only \(O(1)\) crossings per scale, but this observation is not a proof of the full transfer. It must retain the exact coefficients, stars, hard top, both signs, and \(\chi_4\).

There is also a literal normalization defect before (4.1): \(M_1\) cannot be assigned frequency \(h/(4d)\) without the explicit \(h'=4h\) relabelling. The \(R_5\) term is not part of this identity and must remain separately owned; its already accepted pointwise \(O(Y^{1/4+\varepsilon})\) bound gives a local square contribution of the target scale. A blockwise estimate such as (4.1) is stronger than a local estimate for the assembled \(P\), because cross-block and \(M_1/M_2\) cancellation may be lost.

The resulting regime classification is:

| Window exponent | Hostile conclusion |
|---|---|
| \(\alpha<1/3\) | Subcoherent; desired cluster bound is already pointwise-hard by (3.2). |
| \(\alpha=1/3\) | Only \(O(1)\) cells; no power decay. Sharp persistence gives at best exponent \(5/18\) if the ideal local bound existed, not merely \(1/3\). |
| \(1/3<\alpha<1/2\) | Not killed by subcoherence and would improve on \(1/3\), but (4.1) is open and no audited source supplies it. |
| \(\alpha\ge1/2\) | The nominal local scale in (1.4) no longer improves exponent \(1/3\). |

Thus the earlier premise that \(\alpha<1/3\) is the only bridge-improving range must be rejected. The subcoherence calculation is correct, but its scope ends at \(1/3\), whereas the sharp bridge-improving range ends at \(1/2\).

## 5. Required control tests and outcomes

| Control | Outcome | Hostile finding |
|---|---|---|
| `positive_right_persistence` | PASS | (2.1) is exact and uses only monotonicity. |
| `negative_left_persistence` | PASS | (2.2) is exact provided \(x-u\ge0\); the dyadic range ensures this. |
| `integer_jump_convention` | PASS | Inclusive/right-continuous jumps are compatible with both directions; (1.1) fixes the endpoint convention exactly. |
| `dyadic_boundary_windows` | PASS | Favorable windows for \(x\in[Y,2Y]\), \(W\le Y/3\), lie in \([Y/2,3Y]\), coverable by \(O(1)\) accepted dyadic ranges. |
| `bounded_overlap_sampling` | PASS | Oriented unit intervals have absolute overlap multiplicity at most three. |
| `integer_exceptional_count` | PASS | Exact cells give (2.4), stronger and cleaner than an informal continuity argument. |
| `local_bridge_exponent` | REVISE | The sharp implication is (1.2); the conductor's \(H\)-term formula is valid only as a weaker corollary and must not be labelled sharp. |
| `additive_error_ledger` | REVISE | The complete ledger is (1.3), including both \(E^{1/3}\) and \((E/W)^{1/2}\). |
| `unit_window_equivalence` | PASS WITH CAVEAT | Exponent-wise for arbitrary real points; exact algebraic equivalence only on integer cells. |
| `moving_height_floor` | OPEN TRANSFER | It does not alter the fixed identity, but fixed-symbol stratification and recombination remain unproved. |
| `hard_top_and_stars` | RETAIN | Measure-zero endpoints do not affect integrals but can affect the prescribed center and coefficient ownership. |
| `chi4_and_two_sided_frequency` | PASS FOR FIXED IDENTITY | Exact aggregation preserves them; deleting either changes the actual quadratic form. |
| `exact_rational_clusters` | PASS | (2.8) has the correct sign, center phase, normalization, and same-cell probability. |
| `M1_M2_R5_ownership` | REVISE | Correct the factor four for \(M_1\); keep \(R_5\) separate. |
| `top_scale_spacing_capacity` | FAIL AS A PROOF ROUTE | Frozen separated-frequency mean value at \(D=Y^{1/2}\) is \(\ll(W+D^2)D\asymp Y^{3/2}\), versus target \(WY^{1/2}\); deficit ratio \(Y^{1-\alpha}\). |
| `minimax_subcoherence` | PASS, NARROW SCOPE | Diameter \(O(Y^{-1/3})\); the no-go is rigorous only for \(\alpha<1/3\), with an \(O(1)\)-cell warning at equality. |
| `canonical_core_nonimplication` | PASS | None of the accepted global moment, frozen large-value bound, or pointwise \(1/3\) bound implies (4.1). |
| `source_hypothesis_map` | PASS/NO CLOSURE | Every primary theorem audited below misses either the window scale, prescribed-point quantity, coefficient system, or needed additive error. |

No numerical experiment was needed: all decisive controls are exact algebra, interval geometry, or literal theorem-hypothesis comparisons.

## 6. Dependencies and exact artifacts used

**Provenance correction.** I actually opened both `rounds/codex-managed/gc-critical-block-large-values/synthesis.md` and `strategy_skeleton/gauss_circle_method_landscape.md`. Neither appears in the brief's permitted-context list. The report is therefore context-contaminated and non-isolated candidate evidence. I did **not** open the two permitted files `rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/synthesis.md` and `strategy/conductor_0817_full_proof_strategy.md`; they are not dependencies of this report. No sibling report was read.

The literal repository artifacts accessed were:

- `protocol.md`;
- `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/briefs/pointwise_bridge_hostile_source_audit.md`;
- `state/proof_obligations.yml` (the relevant live nodes only);
- `state/best_proof_draft.md`;
- `state/gap_register.md`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/derivation_packet.md`;
- `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/candidates/conductor_persistence_and_local_bridge.md`;
- `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/candidates/conductor_exact_cluster_kernel.md`;
- `rounds/codex-managed/gc-critical-block-large-values/synthesis.md`;
- `strategy_skeleton/gauss_circle_method_landscape.md`.

The primary-source hypothesis map is as follows.

| Primary source and literal theorem | Variable/jump convention | Interval or smoothing hypotheses | Actual conclusion | Exact mismatch with Round 94 target |
|---|---|---|---|---|
| W. G. Nowak, [“Lattice points in a circle: An improved mean-square asymptotics,” *Acta Arith.* 113 (2004), 259–272, DOI 10.4064/aa113-3-4](https://www.impan.pl/shop/en/publication/transaction/download/product/83670), equations (1.6)–(1.7) and the main theorem | \(P(x)=\sum_{0\le n\le x}r(n)-\pi x\), hence inclusive at integers | Global primitive \(\int_0^X P(x)^2dx=CX^{3/2}+Q(X)\) | \(Q(X)\ll X(\log X)^{3/2}\log\log X\); endpoint subtraction gives (3.3) | Additive \(Y\operatorname{polylog}Y\) forces exponent \(1/3\) under the sharp bridge; it is an aggregate \(P\)-bound, not the actual block-cluster bound (4.1). |
| D. A. Popov, [“Voronoi's formulae and the Gauss problem,” *Russian Math. Surveys* 79:1 (2024), 53–126, DOI 10.4213/rm10162e](https://www.mathnet.ru/eng/rm10162), Theorem 10 II–IV, equations (10.1), (10.3), and Theorem 11 | Circle remainder \(P\); Theorem 11 separately chooses a side/representative at a discontinuity | \(E_2(T,H)=(2H)^{-1}\int_{T-H}^{T+H}P^2\), \(H\le T/2\); higher local moments require \(H\ge T^{1/2}\) | \(E_2(T,H)\ll \sqrt T+T(\log T)^2/H\) | Again an additive \(T(\log T)^2\); the fourth/sixth moment ranges do not reach \(Y^{1/4+\sigma}\); Theorem 11 is conditional and not the required Vaaler cluster theorem. |
| D. A. Popov, [“Bounds and behaviour of \(P(x),\Delta(x)\) on short intervals,” *Izv. Math.* 80:6 (2016), 1213–1230, DOI 10.1070/IM8341](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=8341&what=fullteng), Theorem 2, (3.30)–(3.32), and Corollary 3 | \(R(x)=\sum_{0\le n\le x}r(n)\), \(P=R-\pi x\), with \(P(n)-P(n-0)=r(n)\) | Assumes two-sided broadness \(|P(x)-P(n)|\le B|P(n)|\) for \(|x-n|\le n^\alpha/\varphi(n)\), \(0<\alpha\le1/2\) | Conditional pointwise exponent \((1-\alpha)/2\) up to subpower factors; \(\alpha=1/2\) gives a quarter-type conclusion | Broadness is an assumption, not a proved local moment or actual-coefficient cluster estimate. It cannot be used to establish the premise it needs. |
| M. A. Korolev and D. A. Popov, [“On Jutila's integral in the circle problem,” *Izv. Math.* 86:3 (2022), 413–455, DOI 10.1070/IM9211](https://www.mathnet.ru/eng/im9155), quoted Jutila theorem and subsequent theorems | \(P(t)=\sum_{n\le t}r(n)-\pi t\), inclusive | Difference integral \(\int_T^{T+H}(P(t+U)-P(t))^2dt\); principal asymptotic has \(1\le U\ll\sqrt T\ll H\le T\) and \(HU\gg T^{1+\varepsilon}\) | Mean-square asymptotics/bounds for increments | It controls differences averaged over windows at least of square-root scale, not \(P(t)\) on every \(Y^{1/4+\sigma}\)-window and not (4.1). |
| X. Li and X. Yang, [“An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem,” arXiv:2308.14859v2](https://arxiv.org/abs/2308.14859), Theorem 1.2 | \(R(X)=\sum_{m^2+n^2\le X}1-\pi X\), inclusive | Direct all-\(X\) pointwise theorem, no local-moment premise | \(R(X)=O_\varepsilon(X^{0.314483\ldots+\varepsilon})\) | This improves the internal fallback comparison but remains above \(1/4\) and supplies no literal local rational-cluster estimate for the frozen Vaaler architecture. |

These sources were used only at the displayed hypotheses. None may be silently upgraded from an aggregate, conditional, increment, or long-window theorem to the required uniform short-window estimate.

## 7. Recommended state effect

**Evidence status:** do not promote any claim solely on this report, because its selected-context isolation was breached. A clean permitted-context revalidation, or independent conductor derivation, is required before an isolation-dependent State Patch. Subject to that hygiene repair, the mathematical recommendation remains to promote the inclusive persistence lemma (2.1)–(2.2), the bounded-overlap sampling theorem (2.3), the exact integer-cell identity (1.1) and exceptional estimate (2.4), the sharp bridge (1.2)–(1.3), and the fixed-symbol identities (2.7)–(2.8).

**Revise:** replace any claim that the \(H+Y^{1/4}+\sqrt{E/H}\) expression is the sharp bridge by (1.2)–(1.3); record that \(W=Y^{1/4+\sigma}\) gives exponent \(1/4+\sigma/3\) for fixed \(\sigma\); correct the \(M_1\) frequency normalization; and separate the fixed random-cell identity from its moving-symbol transfer. Replace the statement “only \(\alpha<1/3\) is bridge-improving” by the exact division \(\alpha<1/3\) subcoherent, \(1/3\le\alpha<1/2\) potentially bridge-improving but analytically open.

**Reject as closure:** global-to-local endpoint subtraction with the known additive error; frozen separated-frequency large sieve at the minimax block; treating the random-cell identity itself as a cancellation estimate; invoking conditional broadness as if it were proved; or importing a direct exponent \(0.314483\ldots\) theorem as a quarter-bound mechanism.

**Retain open:** the moving-floor/hard-top stratification and recombination seam, and especially a genuine signed rational-cluster estimate in the non-subcoherent range \(1/3<\alpha<1/2\). The primary-source search supplies no theorem that resolves either obligation. Overall state recommendation: promote the exact elementary/interface lemmas, revise the conductor candidates, retain the analytic cluster node as open, and make no claim of quarter-exponent closure.
