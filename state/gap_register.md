# Gap Register

Generated from the open nodes in
`state/proof_obligations.yml` at graph SHA-256
`2b61ad459192c94e83ee80adfa3bdda5374df87b01f42c4a0ab306c07eb817de`.
This file is a navigation aid; the graph is authoritative.

## Certified baselines

Round 95 certifies the repaired external theorem

\[
 P(X)\ll_\varepsilon X^{\theta_{\rm LY}+\varepsilon},
 \qquad
 \theta_{\rm LY}=0.3144831759740614\ldots .
\]

This is the strongest certified global pointwise exponent overall. It is
a direct external route and does not close any M9 node.

Round 91 proves \(P(X)\ll_\varepsilon X^{1/3+\varepsilon}\)
uniformly for real \(X\ge2\). The accepted direct menu is minimax-sharp
at exponent \(1/3\), so no further menu optimization can improve this
baseline. The remaining exponent gap to the target is \(1/12\), and it
must be supplied by a new signed M1 or M2 hard-core estimate.

Round 93 also proves

\[
 \int_Y^{2Y}|P(t)|^2\,dt\ll_\varepsilon Y^{3/2+\varepsilon}
\]

and the exceptional-set bound
\(\operatorname{meas}\{|P(t)|>Y^{1/4+\eta}\}
\ll Y^{1-2\eta+\varepsilon}\).  This is a density-one theorem for real
parameters, not a prescribed-point estimate.  Any pointwise bridge must
add genuinely local information at scales where the global moment's
\(D^2\) spacing term dominates.

Round 94 proves the sharp deterministic bridge

\[
 |P(X)|\ll Q(Y,W)^{1/3}+\bigl(Q(Y,W)/W\bigr)^{1/2},
\]

where \(Q(Y,W)\) is a uniform length-\(W\) local second-moment bound,
and upgrades the density-one quarter theorem to integer and arbitrary
one-separated samples.  It also gives the exact triangular cluster
kernel for the literal M1 frequencies \(h/d\) and M2 frequencies
\(h/(4d)\).  The first genuinely averaging window range is
\(Y^{1/3+o(1)}<W<Y^{1/2-o(1)}\); at smaller windows the minimax block is
subcoherent and the cluster form is pointwise-hard.  No actual-symbol
cluster estimate is yet known in the averaging range.

At the frozen window \(W=Y^{7/16}\), Round 95 reduces the internal
cluster exactly to a signed determinant correlation. The complete
equal-lift diagonal is \(O_\varepsilon(D/L)\). At the minimax block,
coefficient-blind Farey spacing has capacity \(Y^{43/48}\), missing the
target by \(Y^{19/48}\), while Popov's assembled local discrepancy
misses by only \(Y^{1/16}\). Neither estimate supplies the literal
signed block theorem.

## Final bridge

| Obligation | Immediate gap |
|---|---|
| `GC-target` | The standard bridge still needs `M9`; the alternative global bridge needs both GAR and `M9-M2`. |
| `M9` | Both blockwise `M9-M1` and `M9-M2` plus endpoint uniformity must close. |
| `M9-endpoint-uniformity` | Uniform control is required through \(D=X^{1/2}\); average-to-pointwise degeneration is unresolved. |

## M9-M2 gaps

| Obligation | Immediate gap |
|---|---|
| `M9-M2` | The physical assembly is now proved and noncircular. Three analytic parents remain: the canonical hard density-discrepancy energy, the balanced smooth signed quarter packet, and the unbalanced smooth \(M^{3/4}\) product-phase estimate. |
| `M9-M2-physical-one-count-assembly` | Proved in Round 97. With the exact bottom/R5/direct-owner table and the fixed physical hard/balanced/unbalanced split, TOP+BAL+UNBAL implies full M9-M2 after logarithmic one-count assembly. |
| `M9-M2-smooth-balanced-quarter-packet-estimate` | Prove \(\left|\sum_GG\mathscr P_G\right|\ll_\varepsilon L^{3/2}X^\varepsilon\) for every actual smooth residual label with \(1\le K/L\le16\), keeping the absolute value outside the \(G\)-sum. |
| `M9-M2-smooth-unbalanced-three-quarter-estimate` | Round 107 reduces this exactly to the prescribed-centre signed truncated-divisor wavelet \(\mathscr R_{D,L}(X)\ll_\varepsilon X^{1/4+\varepsilon}\), rapidly supported on \(|dr-X|\lesssim D/L\). Absolute capacity misses by \(H_D/L\); automatic \(r_2/4\) completion and further scalar transforms are closed routes. |
| `M9-M2-hard-top-alone-outside-packet-obstruction` | Proved in Round 97. A hard canonical theorem has no owner relation to the nonempty balanced and unbalanced smooth residual cells. |
| `M9-M2-top-endpoint-density-discrepancy-energy` | Canonical Round-92 core. Prove the complete actual-symbol hard-block sum at (L^2X^\varepsilon), jointly retaining metric density and discrepancy. The missing block gain is exactly (\rho^{-1/2}). |
| `M9-M2-primitive-ray-fixed-a-actual-Gram` | Round 103 closes the disjoint \(q=1\) actual diagonal. On longer rows prove the signed mode-resolved near-determinant package jointly with a literal separated complement; sampled-\(k\) control alone does not correlate polynomially many \(q\)-rows. |
| `M9-M2-primitive-ray-q-dispersion-obstruction` | Proved in Round 96. Fixed-\(m\) legal shifts erase the character; coefficientwise or diagonal-separated one-step bounds gain at most \(D^{-1/2}\); parity-aware Poisson and adjoint reciprocal transformation return at equal capacity. This does not rule out the actual Gram estimate. |
| `M9-M2-determinant-carrier-short-ray-route-obstruction` | Proved in Round 102. The density carrier is not the complete metric determinant, algebraic spacing is below the active scale, raw exact/near incidence is unweighted, and the singleton \(q=1\) block has no nonzero determinant shift. |
| `M9-M2-primitive-ray-q1-actual-diagonal-energy` | Proved in Round 103 by complete actual sampled-\(k\) variation and reciprocal curvature, with density and every discrepancy mode retained. |
| `M9-M2-top-endpoint-signed-cone` | The square family, exact nonsquare centers, and blocks \(AJD^3\ll L^3\) are closed. Quotient parity and the half-frequency gap cancel inside the complete coefficient. Bound the residual \(\chi_4(h)\chi_4(s)\) cross-row kernel directly on \(AJD^3\gg L^3\). |
| `M9-M2-top-endpoint-nonsquare-divisor-strip` | Proved in Round 79; use the factor-\(R\) incidence theorem and do not reclassify the ordinary \(1/R\) density as exceptional. |
| `M9-M2-top-endpoint-metric-density-obstruction` | Proved route obstruction; the density and centered discrepancy must be estimated together outside absolute values. |
| `M9-M2-top-endpoint-strict-metric-carrier-cancellation` | Proved in Round 80; the coefficient carrier restores the Fourier zero mode and returns exactly to the original transposed character energy. |
| `M9-M2-top-endpoint-actual-symbol-variation` | Proved internally in Round 77; use it as the exact interface for structured and generic resonance analysis. |
| `M9-M2-character-factor` | Proved normalization guardrail: \(e(h/4)-e(3h/4)=2i\chi_4(h)\) for odd \(h\), and zero for even \(h\). It must be retained but is not an analytic blocker. |
| `M9-near-collision-taxonomy` | Alternative fourth-moment route only. The \(0<|N|\asymp T\) bands and pointwise endpoint remain open, but this node is no longer a mandatory parent of direct M9-M2 assembly. |
| `M9-M2-fourth-moment-average-to-pointwise` | Global \(L^4\) plus the accepted derivative bound loses too much; a direct signed or new large-value theorem is needed. |
| `M9-M2-local-fourth-moment-LFM` | Coherence-window control is equivalent-hard at the endpoint and requires full signed cancellation. |
| `GC-nonsubcoherent-actual-cluster-local-moment` | On a fixed window \(W=Y^\alpha\) with \(1/3<\alpha<1/2\), prove the literal signed M1/M2 random-cell cluster energy \(\ll Y^{1/2+\varepsilon}\). The bridge would then give exponent \(1/6+\alpha/3<1/3\). No coefficient-blind spacing bound is sufficient. |
| `GC-W7-16-actual-reduced-determinant-correlation` | At \(W=Y^{7/16}\), prove the exact one-sided signed determinant sum after all equal lifts are combined. The diagonal and all owners are closed; the minimax coefficient-blind gap is \(Y^{19/48}\), while the assembled Popov additive gap is \(Y^{1/16}\). |

## M9-M1 gaps

| Obligation | Immediate gap |
|---|---|
| `M9-M1` | Round 98 proves the exact direct physical assembly. After accepted owners, precisely two analytic parents remain: the middle/lower hard-top residual and the literal direct smooth residual. The canonical Gram is not a blockwise owner. |
| `M9-M1-physical-one-count-assembly` | Proved in Round 98. `TOP_residual + SMOOTH_residual` implies full blockwise M9-M1 after exact profile, floor, star, sign, and logarithmic one-count ownership. |
| `M9-M1-direct-smooth-residual-blockwise-estimate` | Prove the uniform \(X^{1/4+\varepsilon}\) estimate for every literal smooth physical label in \(\mathcal U_1\), retaining the actual Vaaler profile, floors, stars, signs, and real-\(X\) endpoint clipping. |
| `M9-M1-canonical-Gram-route-scope-obstruction` | Proved in Round 98. The canonical Gram owns only one globally recombined transition-flattened smooth nonaxial principal packet and has no accepted inverse localization to physical dyadic blocks. |
| `M9-M1-canonical-hard-actual-symbol-Gram-estimate` | Canonical Round-92 core. Prove ( |\mathcal E_{\rm hard}(U)|\ll X^\varepsilon(U/B)J^{14/5}) on the literal (D_1<|d|<\Delta_b-E_*) hard complement. The required top gain is (J^{-1/6}) at Gram level, equivalently (J^{-1/12}) after Toeplitz. |
| `M9-M1-canonical-hard-actual-vector-directional-estimate` | Round 99 exact survivor. Prove the fixed actual-vector matrix coefficient at normalized strength \(J^{-1/6}\), with all configurations inside the entry and any conductor-row cancellation taken before a uniform norm. |
| `M9-M1-joint-four-row-separable-self-return-obstruction` | Proved in Round 99. The \((d,u)\) Hessian is integrally the two one-row Hessians, double completion returns to the centered four-row Gram, fixed configurations are rank one, and ordinary high traces are direct sums in conductor row. |
| `M9-M1-global-angular-radial-estimate` | This is the total-active alternative GAR route, not blockwise M9-M1. Round 98 reduces it exactly to the signed lower-radial aggregate and the sharp radial-interface aggregate. |
| `M9-M1-global-lower-radial-signed-estimate` | Prove the signed lower-radial aggregate after the exact small-angle replacement, including the one-sided divisor correction above \(\nu=2/5\). |
| `M9-M1-global-radial-interface-estimate` | Prove the sharp upper radial/interface package: upper conductors, axes, raw transitions, cone edges, and radial/top seams with one-count ownership. |
| `M9-M1-global-radial-one-count-assembly` | Proved in Round 98. Lower radial plus sharp radial interface implies GAR after the compact critical sector is inserted. |
| `M9-M1-GAR-total-active-equivalence` | Proved in Round 98. GAR controls the total active M1 contribution but not individual blockwise M9-M1 estimates. |
| `GC-global-M1-alternative-bridge` | Conditional alternative bridge: H1-H3 + H4 + R5-Full + GAR + M9-M2 implies the quarter target. GAR and M9-M2 remain open. |
| `M9-M1-transition-flattened-residue-offset-reduction` | Proved in Round 82; Rounds 83--84 remove literal \(d=0\) and the polynomial small-nonzero-difference range. |
| `M9-M1-nonzero-residue-offset-dual-difference-reduction` | Proved in Round 83 and sharpened in Rounds 84--86. The first survivor is \(J^{87/140}<|d|<\Delta_b-J^{3/4}\); smaller nonzero modulus multiples, gcd modes, and the outer edge are already included in proved bounds. |
| `M9-M1-centred-dual-difference-small-shift-bound` | Proved in Round 84 and extended by the Round-86 cubic shell theorem. Use second- and third-derivative cancellation below \(J^{87/140}\) and compact-support flatness at the outer edge; do not infer a whole-range \(B\)-saving. |
| `M9-M1-centred-dual-difference-support-edge-bound` | Proved in Round 85. It removes \(|d|\ge\Delta_b-J^{3/4}\) only for the smooth principal symbol; it does not own the raw transition or the interior four-Kloosterman correlation. |
| `M9-M1-centred-dual-difference-cubic-shell-bound` | Proved in Round 86. It removes \(J^{17/30}<|d|\le J^{87/140}\) by progressionwise cubic curvature while retaining the complete arithmetic coefficient and physical energy factor. |
| `M9-M1-deep-full-factor-same-group-fejer-bound` | Proved in Round 87. With \(U=D\), every one-count mixture of full-prime-power local-zero and paired branches is target-safe as a symmetric signed Fejer package. Only the cross-group off-diagonal remains. |
| `M9-M1-cross-group-period-depth-subaggregate-bound` | Proved in Round 88. Centered Fejer grouping removes \(R_*\le\rho_*\), and restricted good-prime masked-period rigidity removes \(\mathfrak a\ge M^2/\rho_*^2\) after that deletion. The complementary hard cross-group operator remains open. |
| `M9-M1-bad-prime-cellwise-period-graph-bound` | Proved in Round 89. Complete bad-prime cells have degree \(M^2/\mathfrak b_\sigma\), and the explicit conductor threshold or union summability condition is target-safe. The full bad-prime/nonunit union remains open and retains a top-band \(J^{1/6}\) capacity deficit. |
| `M9-M1-square-root-capacity-self-return-barrier` | Proved in Round 90. Complete cells and descent reassemble the exact deep Gram operator; its target and full-degree capacity are \((D/B)\) times the squares of the Round-82 target and capacity. After the compulsory square root there is no new loss. This does not estimate the hard signed core. |
| `M9-M1-upper-conductor-transition-flattened-subrange-bound` | Proved in Round 81; use the global-BV principal symbol plus pointwise transition error only through \(C=J^{13/18}\). |
| `M9-M1-top-endpoint-signed-cone` | Terminal shell is closed; middle/lower hard-top shells remain. |
| `M9-M1-cross-product-odd-kernel-discrepancy` | A whole-sum signed ordered-denominator estimate is missing. |
| `M9-M1-shifted-divisor-correlation-PSC` | The moving short-numerator correlation keeps the \(H/L\) deficit. |
| `M9-M1-dual-restricted-convolution-RCS` | Product completion self-returns and supplies no signed estimate. |
| `M9-M1-top-Perron-angular-correlation` | Retained axial residues and matching profile projection remain. |
| `M9-M1-maximal-angular-sign-kernel` | The swept transition/horizontal operator is the principal reflected-mode blocker. |
| `M9-M1-post-FE-vector-kernel` | Complete vector kernel requires the alpha transition after the closed beta branch. |
| `M9-M1-swept-transition-horizontal-operator` | Prove the projected alpha cosine-Cauchy/GAR-return bound. |
| `M9-M1-renormalized-radial-boundary-operator` | Prove the connector-completed projected alpha trace. |
| `M9-M1-alpha-bounded-zeta-high-transition-bound` | Solve the physical signed short twisted-divisor core and height-limit interface. |

| M9-M1-q8-actual-vector-cross-projection-reduction | Proved in Round 100. On \(v_2(M)=3\), the local \(q=8\) mode is the exact \(\mathbb Z/4\mathbb Z\) cross-projection of the four actual rows. The only aligned square has \(R_*=4\) and is prior-owned. The remaining scalar odd-cofactor/conductor cross-projection is unbounded. |
| M9-M1-full-two-adic-actual-row-unitary-convolution | Proved in Round 101. The full \(2^\nu\) local factor is an exact full-rank unitary cyclic convolution with guaranteed twisted period \(1,2,L/8\). Period sparsity gives only block self-return; long-return aligned/reversal and all generic actual-vector coefficients remain in the open conductor scalar. |

## Closed infrastructure

`R5-Full-reconciliation` and `R5-Full` are proved internally by the
pointwise divisor-product argument, including exact products, shifted
legs, integer jumps, hard-top profiles, and real-\(X\) uniformity. They
are no longer blockers.

## Historical next action after Round 107

Round 107 is closed. The unbalanced smooth product packet is now an exact
width-\(D/L\) prescribed-centre truncated-divisor wavelet. Its character,
Gaussian constant, flat-smooth aggregate error, dual lengths and
outside-absolute correlation interface are certified. The remaining
unbalanced problem is a genuine signed estimate, not another completion or
functional-equation calculation. The next canonical round may return to the
hard M2 signed density--discrepancy energy, where a new mechanism must gain
the explicit factor \(\rho^{-1/2}\).

| Round 107 obligation | Immediate gap |
|---|---|
| M9-M2-unbalanced-truncated-divisor-fixed-centre-return | Proved internally on flat smooth components, with sharp endpoint kernels retained separately. |
| M9-M2-smooth-unbalanced-three-quarter-estimate | Prove the actual signed fixed-centre wavelet at \(X^{1/4+\varepsilon}\), equivalently save \(H_D/L\) in the shifted product correlation. |
| M9-M2-smooth-balanced-quarter-packet-estimate | Still prove the outside-absolute signed \(G\)-aggregate; Round 107 does not touch it. |
| M9-M2-top-endpoint-density-discrepancy-energy | Prescribed polylogarithmic shells are closed. Every fixed positive-power shell still needs joint density--discrepancy cancellation with gain \(\rho^{-1/2}\). |
| M9-M1 | The two direct blockwise parents and the alternative global radial parents remain open. |
| Global exponent | No change: certified external \(0.3144831759740614\ldots\); internal uniform \(1/3\); quarter open. |

## Active next action after Round 113

The balanced smooth M2 child now has a literal coefficientwise
actual-symbol dictionary and exact physical one-count equation. Its
remaining obstruction is a genuine signed analytic estimate, not another
normalization or owner-reconciliation step.

| Obligation | Immediate gap |
|---|---|
| M9-M2-smooth-balanced-quarter-packet-estimate | Prove the fixed-block outside-absolute complete gcd-shell sum at \(L^{3/2}X^\varepsilon\). The persistent denominator is \(j=1\); \(j=2\) occurs only at exact-square \(X\). |
| M9-M2-top-endpoint-density-discrepancy-energy | Prove the actual signed primitive-ray off-diagonal with density and every discrepancy mode coupled; fixed positive-power shells still need the explicit \(\rho^{-1/2}\) gain. |
| M9-M2-smooth-unbalanced-three-quarter-estimate | Prove the prescribed-centre truncated-divisor wavelet, equivalently save \(H_D/L\). |
| M9-M1 | Prove the direct hard-top signed cone and direct smooth residual estimate, or a complete alternative whole-\(U_1\) theorem. |
| M9-endpoint-uniformity | Reconcile all physical endpoint and interface labels after the M1/M2 analytic parents close. |
| Global exponent | No change: repaired external \(0.3144831759740614\ldots\); internally proved uniform \(1/3\); pointwise quarter open. |
