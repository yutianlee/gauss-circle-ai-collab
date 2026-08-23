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
| `M9-M1` | Round 98 proves the exact direct physical assembly. Round 119 proves that each of its two open physical parents has a separate accepted-menu (X^{1/3+o(1)}) witness at (L\asymp X^{1/6}), missing (X^{1/12}). The canonical Gram is not a blockwise owner. |
| `M9-M1-physical-one-count-assembly` | Proved in Round 98. `TOP_residual + SMOOTH_residual` implies full blockwise M9-M1 after exact profile, floor, star, sign, and logarithmic one-count ownership. |
| `M9-M1-direct-smooth-residual-blockwise-estimate` | Prove the uniform (X^{1/4+\varepsilon}) estimate for every literal smooth physical label in (\mathcal U_1). The first smooth (D=\lfloor\sqrt X\rfloor/2, L\asymp X^{1/6}) witness has accepted-menu capacity (X^{1/3+o(1)}), so a new (X^{1/12}) signed gain is required. |
| `M9-M1-canonical-Gram-route-scope-obstruction` | Proved in Round 98. The canonical Gram owns only one globally recombined transition-flattened smooth nonaxial principal packet and has no accepted inverse localization to physical dyadic blocks. |
| `M9-M1-canonical-hard-actual-symbol-Gram-estimate` | Canonical Round-92 core. Prove ( |\mathcal E_{\rm hard}(U)|\ll X^\varepsilon(U/B)J^{14/5}) on the literal (D_1<|d|<\Delta_b-E_*) hard complement. The required top gain is (J^{-1/6}) at Gram level, equivalently (J^{-1/12}) after Toeplitz. |
| `M9-M1-canonical-hard-actual-vector-directional-estimate` | Round 99 exact survivor. Prove the fixed actual-vector matrix coefficient at normalized strength \(J^{-1/6}\), with all configurations inside the entry and any conductor-row cancellation taken before a uniform norm. |
| `M9-M1-joint-four-row-separable-self-return-obstruction` | Proved in Round 99. The \((d,u)\) Hessian is integrally the two one-row Hessians, double completion returns to the centered four-row Gram, fixed configurations are rank one, and ordinary high traces are direct sums in conductor row. |
| `M9-M1-global-angular-radial-estimate` | This is the total-active alternative GAR route, not blockwise M9-M1. Round 120 proves the complete nonlower complement and the sharp radial interface; the exact signed lower-radial aggregate is now its sole analytic parent. |
| `M9-M1-global-lower-radial-signed-estimate` | Prove the signed lower-radial aggregate after the exact small-angle replacement, including the one-sided divisor correction above \(\nu=2/5\). |
| `M9-M1-global-radial-interface-estimate` | Proved in Round 120 by the terminal-height whole-nonlower theorem and exact subtraction of the fixed compact critical cells. The endpoint prefix and endpoint/R1 architecture are not inserted. |
| `M9-M1-global-radial-one-count-assembly` | Proved in Round 98 and sharpened in Round 120. Its interface child is now proved; the lower-radial signed aggregate is the only remaining GAR child. |
| `M9-M1-GAR-total-active-equivalence` | Proved in Round 98. GAR controls the total active M1 contribution but not individual blockwise M9-M1 estimates. |
| `GC-global-M1-alternative-bridge` | Conditional alternative bridge: H1-H3 + H4 + R5-Full + GAR + M9-M2 implies the quarter target. GAR now lacks only its lower-radial analytic parent; M9-M2 still has three independent analytic parents. |
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
| `M9-M1-top-endpoint-signed-cone` | Terminal shell is closed; the (D=\lfloor\sqrt X\rfloor, L\asymp X^{1/6}) middle/lower witness has normalized (L^2) capacity versus (L^{3/2}) target. A sign-sensitive (L^{-1/2}) gain remains. |
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

## Active next action after Round 115

The balanced smooth M2 child is reduced, modulo two target-safe corridors
and the proved phase-free mode, to one literal oscillatory zero-subtracted
double-far remainder. The next balanced step requires a new joint signed
nonzero-alias or local-energy inequality; the listed self-return mechanisms
may not be repeated as if they supplied a saving.

| Obligation | Immediate gap |
|---|---|
| `M9-M2-balanced-double-far-oscillatory-remainder` | Prove (\lvert\mathcal R_B^{\mathrm{osc}}\rvert\ll_\varepsilon L^3X^\varepsilon) with both gcd weights, both literal slanted symbols, the full shift family, and the pair-dependent determinant gate retained. |
| `M9-M2-smooth-balanced-quarter-packet-estimate` | Equivalent, modulo proved owners, to the open actual double-far energy and hence to the zero-subtracted remainder above. |
| `M9-M2-top-endpoint-density-discrepancy-energy` | Still prove the actual signed hard density-discrepancy energy; Round 115 is balanced-only. |
| `M9-M2-smooth-unbalanced-three-quarter-estimate` | Still prove the prescribed-centre truncated-divisor wavelet, equivalently save (H_D/L). |
| `M9-M1` | The direct hard-top signed cone and direct smooth residual estimate remain open; Round 115 makes no M1 change. |
| `M9-endpoint-uniformity` | Remains blocked by the two direct M1 and three M2 analytic parents. |
| Global exponent | No change: repository-certified external (0.3144831759740614\ldots); internally proved uniform (1/3); pointwise quarter open. |

## Active next action after Round 116

The balanced half-shifted alias reduction is now literal and target-safe at
every transform seam, but the complete signed bulk kernel is unestimated.
One-alias reciprocal counting, spacing-only large sieve, positive row Gram,
and the inverse B-process are parked as standalone mechanisms.

| Obligation | Immediate gap |
|---|---|
| `M9-M2-balanced-double-far-oscillatory-remainder` | Prove the (L^3X^\varepsilon) bound for the complete signed divisor-progressive ((d,\mu,h,k,v)) cluster-defect kernel. Both gates, both literal symbols, congruences, residue phases, and all transition packages must remain inside the joint estimate. |
| `M9-M2-smooth-balanced-quarter-packet-estimate` | Still open. Round 116 parks one proof class, not BAL. Revisit only with a new noninvertible joint signed theorem. |
| `GC-W7-16-actual-reduced-determinant-correlation` | Next bounded lane. Prove the literal one-sided signed determinant correlation at (Y^{1/2+\varepsilon}). The coefficient-blind minimax capacity is (Y^{43/48}), a (Y^{19/48}) deficit; full closure would give internal exponent (5/16), not the quarter theorem. |
| `M9-M2-top-endpoint-density-discrepancy-energy` | Still requires the actual joint density-discrepancy gain (\rho^{-1/2}). |
| `M9-M2-smooth-unbalanced-three-quarter-estimate` | Still requires the prescribed-centre truncated-divisor wavelet saving (H_D/L); the planned first step is a falsification probe. |
| `M9-M1` | The direct hard-top signed cone and direct smooth residual estimate remain open. |
| `M9-endpoint-uniformity` | Still blocked by the two direct M1 and three M2 analytic parents. |
| Global exponent | No change: audited external (0.3144831759740614\ldots), internally proved (1/3), pointwise quarter open. |

## Round 117 latest gap map

| Obligation | Immediate gap after the certified savings |
|---|---|
| `GC-W7-16-actual-reduced-determinant-correlation` | Complete minimax bound is now \(Y^{37/48+\varepsilon}\), leaving \(Y^{13/48}\) to the \(Y^{1/2}\) target. The bounded-lift \(B\asymp D\) shell is \(Y^{35/48+\varepsilon}\), leaving \(Y^{11/48}\). Lower shells require a transverse long-lift variation theorem or a different joint signed inequality. |
| `GC-nonsubcoherent-actual-cluster-local-moment` | Still open. The new complete-block saving is genuine but too weak for an all-block local moment or any pointwise exponent improvement. |
| `M9-M2-smooth-unbalanced-three-quarter-estimate` | Next probe: test the exact prescribed-centre truncated divisor wave for a rigorous coherent countermodel, a target-safe strict subrange, or a noninvertible signed estimate. Do not repeat Poisson inversion or clean \(r_2\) completion. |
| `M9-M2-smooth-balanced-quarter-packet-estimate` | Still parked behind the complete joint divisor-progressive alias kernel. |
| `M9-M2-top-endpoint-density-discrepancy-energy` | Still requires the actual joint density-discrepancy gain. |
| `M9-M1` | Both direct physical parents remain open; direct minimization follows if the unbalanced wave probe gives no viable pointwise mechanism. |
| Global exponent | Unchanged: internal \(1/3\), audited external \(0.3144831759740614\ldots\), quarter open. |

## Round 118 latest gap map

| Obligation | Immediate gap after the prescribed-centre probe |
|---|---|
| `M9-M2-smooth-unbalanced-three-quarter-estimate` | The flat wave has the certified envelope \(\min(D/L,\sqrt{XL/D}+\sqrt{X/(LD)})X^\varepsilon\), but it never reaches the quarter target at a strict residual point. The smallest survivor is the complete joint \((r,k)\) selector before the \(k\)-triangle, including all disconnected runs, coherent phases, shoulders, and the signed complement. |
| `M9-M2-unbalanced-coherent-sector-countermodel-no-go` | Central/tied levels, one same-residue central run, and the integer-centre interior phase-one sector are target-safe. This rules out those countermodels only; it is not a full selector bound. |
| `GC-W7-16-actual-reduced-determinant-correlation` | Round 118 supplies no transferable target estimate. The complete \(Y^{37/48}\) and bounded-lift \(Y^{35/48}\) bounds remain the graded best; the \(Y^{1/2}\) target still needs a joint signed product-wave inequality or long-lift control. |
| `M9-M2-smooth-balanced-quarter-packet-estimate` | Still parked behind the complete joint divisor-progressive alias kernel. |
| `M9-M2-top-endpoint-density-discrepancy-energy` | Still requires the actual joint density-discrepancy gain. |
| `M9-M1` | Both direct physical parents remain open. The next bounded campaign minimizes their exact residual capacities under all proved owners. |
| `M9-endpoint-uniformity` | Still blocked by the two M1 and three M2 analytic parents. |
| Global exponent | Unchanged: internal \(1/3\), audited external \(0.3144831759740614\ldots\), pointwise quarter open. |

## Round 127 latest gap map

| Obligation | Immediate gap after the frontier-selection gate |
|---|---|
| `M9-M2-top-endpoint-density-discrepancy-energy` | The \(hm=\square\) entry sector is safe, but the nonsquare actual direction is open. Support, pointwise magnitude, the displayed joint phase, parity filters, ambient spectra, and product-fibre averaging cannot supply the missing factor. A literal endpoint-coefficient property excluding phase alignment is required. |
| `M9-M1-global-lower-radial-signed-estimate` | The exact Round-122 centered scalar wavelet remains open. Its uncentered square function is false, while the centered \(k\)-energy and reduced-Farey determinant form are stronger separated norms that still ask for the full missing critical factor. |
| `GC-W7-16-actual-reduced-determinant-correlation` | The complete target remains \(Y^{1/2+\varepsilon}\). Scalar-per-cell continuation stops at \(Y^{37/48}\). The selected local transverse \(V^2\) connector is conditional on two unproved inequalities and would reach only \(Y^{73/96}\). |
| `M9-M1` | Both direct one-third-critical parents remain open; the alternative total-active route still lacks lower GAR. |
| `M9-M2` | Hard TOP, BAL, and every UNBAL owner remain independently open. |
| `M9-endpoint-uniformity` | Remains independent and open. |
| `M9` | Requires M9-M1, M9-M2, and endpoint uniformity; none changes in Round 127. |
| Global exponent | Unchanged: internal \(1/3\), audited external \(0.3144831759740614\ldots\), pointwise quarter open. The conditional graded \(73/96\) block exponent would not improve persistence. |

## Round 128 latest gap map

| Obligation | Immediate gap after the local coefficient gate |
|---|---|
| GC-W7-16-local-lift-BV-threshold-V2-lemma | Proved internally for the two exact M1 quarter-phase branches and one M2 branch, including every literal coefficient face and both \(V^2\) endpoints. |
| GC-W7-16-local-V2-normalization-obstruction | Proved internally. Birth count plus pointwise size is abstractly insufficient, and unsplit M1 has literal \(Q_B^{1/2}/L\) variation with bounded \(J_B\). |
| GC-W7-16-local-transverse-square-variation-connector | The coefficient hypothesis is closed. Prove the branchwise joint reciprocal-curvature inequality without an extra \(N_\rho^{1/2}\), full-lift norm, or owner separation. |
| GC-W7-16-actual-reduced-determinant-correlation | The full \(Y^{1/2+\varepsilon}\) target remains open. Even the intermediate \(Y^{73/96+\varepsilon}\) bound still depends on the preceding joint inequality. |
| M9-M1 | Both direct one-third-critical parents and the lower-GAR alternative remain open. |
| M9-M2 | Hard TOP, BAL, and every UNBAL owner remain open. |
| M9-endpoint-uniformity | Remains independent and open. |
| M9 | Requires M9-M1, M9-M2, and endpoint uniformity; none closes in Round 128. |
| Global exponent | Unchanged: internal \(1/3\), audited external \(0.3144831759740614\ldots\), pointwise quarter open. |

## Round 123 latest gap map

| Obligation | Immediate gap after the shifted near-alias reduction |
|---|---|
| `M9-M2-unbalanced-integer-centred-shifted-alias-reduction` | Proved internally. Integerization, the complete zero alias, every nonzero exact alias, and far defects are target-safe in the exact shifted square. |
| `M9-M2-smooth-unbalanced-three-quarter-estimate` | Prove the complete actual-sign aggregate with \(j\ne0\), \(E\ne0\), and \(|E|\leq X^{1+\rho}/L\) at \(X^{1/2+\varepsilon}\), jointly across transverse modes, shifts, aliases, reciprocal variables, literal profiles, and endpoints. |
| `M9-M2-unbalanced-alias-factor-and-derivative-self-return` | Exact factorization, automatic two-adic thinning, nominal selector-density multiplication, the positive unshifted Gram, and uniform fixed-alias first-derivative estimates are frozen. Reopen only with a genuinely joint signed stationary-lattice theorem. |
| `M9-M2` | Hard TOP and BAL remain open. Complete UNBAL remains open on the preceding flat-smooth survivor plus every nonflat owner. |
| `M9-M1` | Both direct one-third-critical parents remain open; the alternative GAR route still lacks the exact Round-122 lower survivor estimate. Round 123 supplies no M1 bridge. |
| `M9-endpoint-uniformity` | Remains independent and open after all M1 and M2 analytic parents. |
| Global exponent | Unchanged: internal \(1/3\), audited external \(0.3144831759740614\ldots\), pointwise quarter open. |

## Round 119 latest gap map

| Obligation | Immediate gap after the direct-parent minimax gate |
|---|---|
| `M9-M1-top-endpoint-signed-cone` | The literal hard (L\asymp X^{1/6}) shell has normalized (L^2) capacity versus (L^{3/2}) target. None of the accepted rows or adjacent-profile algebra supplies the missing (L^{1/2}=X^{1/12}). |
| `M9-M1-direct-smooth-residual-blockwise-estimate` | The first smooth (D=\lfloor\sqrt X\rfloor/2, L\asymp X^{1/6}) label has accepted-menu capacity (X^{1/3+o(1)}). A new actual-symbol (X^{1/12}) gain is required uniformly on the parent. |
| `M9-M1-adjacent-hard-smooth-profile-connector-no-go` | Raw profile telescoping, scale BV, adjacent differencing, and equal deficits do not merge the two direct leaves. A future connector must be a genuinely joint signed theorem with an exact owner map. |
| `M9-M1-global-radial-interface-estimate` | Next backup reconciliation: delete the already proved physical upper endpoint exactly once and isolate the remaining finite-support, cutoff, and top-interface package. |
| `M9-M1-global-lower-radial-signed-estimate` | Still prove the full signed lower-radial aggregate, including the one-sided divisor coefficient and correction above (\nu=2/5). |
| `M9-M1` | Direct closure still needs both one-third-critical parents. The alternative route still needs both GAR parents and then the separate total-M1 bridge. |
| `M9-M2` | Hard TOP, BAL, and complete UNBAL remain open independently of the M1 route choice. |
| `M9-endpoint-uniformity` | Still blocked by the analytic parents. |
| Global exponent | Unchanged: internal (1/3), audited external (0.3144831759740614\ldots), pointwise quarter open. |

## Round 120 latest gap map

| Obligation | Immediate gap after terminal-height interface completion |
|---|---|
| `M9-M1-terminal-height-nonlower-radial-completion` | Proved internally. It owns every fixed nonlower radial sector, including the sharp outer collar, by a fixed terminal-height cutoff and an antecedent-level compact subtraction. |
| `M9-M1-global-radial-interface-estimate` | Proved internally. The stronger whole nonlower complement minus the proved compact critical cells equals the old interface exactly. |
| `M9-M1-global-lower-radial-signed-estimate` | Sole remaining GAR analytic parent. Prove the exact lower-radial aggregate with the floor-perturbed Vaaler height symbol, all denominator profiles, hard sample, stars, signs, the small-angle replacement, and its correction counted once. |
| `M9-M1-global-angular-radial-estimate` | Still open only because of the lower-radial parent. Complete GAR would control total active M1, not the two blockwise parents. |
| `M9-M1` | Direct closure still needs both one-third-critical physical parents. The alternative total-active route now needs only lower radial on the M1 side, but it does not prove blockwise M9-M1. |
| `M9-M2` | Hard TOP, BAL, and complete UNBAL remain open independently. |
| `M9-endpoint-uniformity` | Remains independent and open; Round 120 uses no arbitrary finite-height endpoint extension. |
| Global exponent | Unchanged: internal (1/3), audited external (0.3144831759740614\ldots), pointwise quarter open. |

## Round 121 latest gap map

| Obligation | Immediate gap after the lower profile-height gate |
|---|---|
| `M9-M1-lower-radial-flat-discrepancy-equivalence` | Proved internally. The literal lower owner, flat sharp cone, integer-centred cone, and all-integer truncated-character divisor wavelet are equivalent at the (RX^\varepsilon) scale. |
| `M9-M1-lower-mod-four-resonance-tubewise-no-go` | Proved internally. Local mod-four pairing leaves a target-equivalent phase kernel, and resonance-tubewise moduli retain (R^{3/2}) capacity. |
| `M9-M1-global-lower-radial-signed-estimate` | Sole GAR analytic gap. Prove (\sum_kD_N(k)(\widehat J(k)-\widehat J(k+1))\ll_\varepsilon RX^\varepsilon), equivalently the complete flat phase-kernel bound, without separating heights or resonance labels by absolute value. |
| `M9-M1-global-angular-radial-estimate` | Still open only on the preceding lower signed inequality. Complete GAR remains a total-active result, not blockwise M1. |
| `M9-M1` | Direct closure still requires both one-third-critical physical parents; the alternative total-active route requires the lower discrepancy bound and the separate global bridge. |
| `M9-M2` | Hard TOP, BAL, and complete UNBAL remain independently open. |
| `M9-endpoint-uniformity` | Remains independent and open; lower-phase integerization is not endpoint uniformity. |
| Global exponent | Unchanged: internal (1/3), audited external (0.3144831759740614\ldots), pointwise quarter open. |

## Round 122 latest gap map

| Obligation | Immediate gap after the complementary-divisor gate |
|---|---|
| `M9-M1-lower-near-square-wavelet-reduction` | Proved internally. It deletes the far and central Fourier ranges, all high-two-adic cumulative increments, and the odd positive-character central factor band, leaving one exact medium-index low-two-adic survivor. |
| `M9-M1-near-square-complementary-divisor-self-return` | Proved internally and scoped. The negative odd residue branch self-returns; the positive branch retains a full circle coefficient; low even branches retain full-minus-tail. This blocks the involution alone, not a future joint signed inequality. |
| `M9-M1-global-lower-radial-signed-estimate` | Prove the exact Round-122 survivor at \(RX^\varepsilon\). Its absolute capacity is \(R^2\). Another complement, full-\(r_2\) circle input, residuewise norm, or Abel/Fourier inversion is frozen. |
| `M9-M1-global-angular-radial-estimate` | Still open only on the lower signed inequality. Complete GAR would control total active M1, not either direct blockwise parent. |
| `M9-M1` | Both direct physical parents remain one-third-critical; the alternative total-active route still lacks lower GAR. |
| `M9-M2` | Hard TOP, BAL, and complete UNBAL remain independently open. The next core round rotates here and must name a new actual-symbol noninvertible mechanism. |
| `M9-endpoint-uniformity` | Remains independent and open. |
| Global exponent | Unchanged: internal \(1/3\), audited external \(0.3144831759740614\ldots\), pointwise quarter open. |

## Round 129 latest gap map

| Obligation | Immediate gap after direct all-shell curvature |
|---|---|
| GC-W7-16-direct-Stieltjes-birth-block-curvature-lemma | Proved internally. Every exact branch and divisor progression has direct cost \(K_\rho/L\); no \(J_B\) or \(N_\rho^{1/2}\) loss remains. |
| GC-W7-16-complete-all-shell-curvature-saving | Proved internally. The complete critical fixed block is \(O_\varepsilon(Y^{35/48+\varepsilon})\) over all \(D/L\le B\le D\). |
| GC-W7-16-norm-relative-reciprocal-curvature-obstruction | Proved internally. The completed-\(V^2\)-norm theorem fails by \(Y^{1/48}\); use the fixed Stieltjes mass. |
| GC-W7-16-actual-reduced-determinant-correlation | The target remains \(Y^{1/2+\varepsilon}\), leaving \(Y^{11/48}\). The live interface is signed coupling across numerator increments and/or outer rays after the now-complete inner estimate. |
| M9-M1 | Both direct one-third-critical parents and the lower-GAR alternative remain open. |
| M9-M2 | Hard TOP, BAL, and every UNBAL owner remain open. |
| M9-endpoint-uniformity | Remains independent and open. |
| M9 | Requires M9-M1, M9-M2, and endpoint uniformity; none closes in Round 129. |
| Global exponent | Unchanged: internal \(1/3\), audited external \(0.3144831759740614\ldots\). The new block exponent persists only to \(7/18\). |

## Round 130 latest gap map

| Obligation | Immediate gap after post-inner outer-bilinear audit |
|---|---|
| GC-W7-16-post-inner-shell-support-refinement | Proved internally. The exact recombined shell costs $BK_B$; all lower shells gain $B/D$ and the exponent-critical residual is $B\asymp D$. |
| GC-W7-16-top-shell-determinant-residue-reindexing | Proved internally with fixed primitive outer-ray scope. The numerator increment is a bounded-multiplicity determinant-residue lift, but cancellation of its actual induced M1/M2 weight is open. |
| GC-W7-16-post-inner-outer-energy-obstruction | Proved internally and scoped. Resolved energy is $H^*H$ or $K_{B,+}^*K_{B,+}$, not full-row $G^2$; marginal support and norms allow $DK_B$ alignment. |
| GC-W7-16-actual-reduced-determinant-correlation | The target remains $Y^{1/2+\varepsilon}$. The sole graded residual is the signed bounded-lift $B\asymp D$ scalar at $Y^{35/48+\varepsilon}$, leaving $Y^{11/48}$. |
| M9-M1 | Both direct one-third-critical parents and the lower-GAR alternative remain open. |
| M9-M2 | Hard TOP, BAL, and every UNBAL owner remain open. |
| M9-endpoint-uniformity | Remains independent and open. |
| M9 | Requires M9-M1, M9-M2, and endpoint uniformity; none closes in Round 130. |
| Global exponent | Unchanged: internal $1/3$, audited external $0.3144831759740614\ldots$. The complete graded exponent remains $35/48$. |
