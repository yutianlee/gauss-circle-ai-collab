# Strategy update after the 11 October campaign memo

Conductor supplement to checkpoint230. Round231 remains pending design. Requested input: `strategy/next_campaign_gauss_circle_20261011.md`. Graph:401 nodes, SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. This document changes strategy and admission requirements only.

## Decision

Adopt the memo's precise operator-transfer requirements, its separation of sharp masks from oscillatory coefficients, and its emphasis on complete quantitative progress. Keep complete signed moments as the first priority. Do not restart the proposed Kloosterman exercise merely because the memo selects it: its reviewed snapshot ends at Round199, whereas Round200 already completed the mask/source analysis, Round204 improved the complete moment bound, Round216 supplied an accepted twelfth-order reduction, and Round230 plus later admission tests sharpened the present missing inequality.

The memo supplies no new estimate that presently warrants replacing this priority or launching an analytic campaign. A Kloosterman or decoupling proposal can take priority when it provides an exact complete application with a better restored bound. The next work should seek a new signed arithmetic inequality; another equivalent expansion is not the default next task.

## Recommendations reconciled with current evidence

| Memo recommendation | Adopted treatment |
|---|---|
| Stop P2-only cellular variations | Retain. Round199's obstruction concerns the specified mechanism. Reopening requires a quantitative boundary estimate and all transported P1/P2 terms with original weights. It gives no physical lower bound. |
| Logarithmic sharp-mask transfer | Retain the reviewed Round200 lemma. The memo's Fourier construction is a useful explicit alternative certificate. Apply it before paying any avoidable smoothing error, but only after the unmasked all-vector estimate is available. |
| Separated expansion of the full symbol | Make the distinction explicit: bounded-factor multiplier cost and physical coefficient nuclear norm are different quantities. Include nonseparable oscillation and arithmetic deletions in the budget. |
| Selected Blomer–Pascadi exercise | Conditional candidate. Round200 left the exact external matrix identity unproved. Require that identity and a scale-dependent saving calculation before prioritizing an attack. |
| Decoupling plus arithmetic concentration | Retain as an alternative requiring a literal normal form and an estimate for the actual configurations that saturate the geometric bound. Cone resemblance alone is insufficient. |
| Global high moments | Already the preferred finite milestone. Translate the memo's sharp-X target to current radial normalization explicitly, as below. |
| Measure complete mathematical progress | Apply to future reporting: distinguish a stronger complete bound, a reusable estimate with a quantified application, a reduction, and a method-specific obstruction. Do not count the latter two as an exponent gain. |

## 1. The present moment target

Let theta=(3292+25sqrt(1717))/13762 and beta=2theta-1/2. The accepted unnormalized complete radial moment satisfies M12(B_T)<<T^(10beta+epsilon), with 10beta=1.289663519481... . The external pointwise benchmark remains theta=0.314483175974... with the graph's existing source qualifications.

The sharp-variable and radial-variable exponents must not be interchanged. With Y=T^2, the accepted mollifier relation P(R^2)=R^(1/2)B_T(R)/pi+O(T^(1/2+epsilon)), and dx=2R dR, a complete M_p(B_T)<<T^(b_p+epsilon) gives

    integral |P(x)|^p dx << Y^(1+p/4+lambda_p+epsilon),
    lambda_p=max(0,(b_p-1)/2).

The integration windows are fixed enlargements containing the one-sided persistence intervals. For b_p>=1, monotonicity of the inclusive lattice count then gives

    theta_p=1/4+(b_p+1/2)/(2(p+1)).

These are implications of upper bounds, not an additive approximation between moments or a converse moment equivalence.

| Purpose | Complete radial target | Sharp twelfth excess lambda | Consequence |
|---|---|---|---|
| Any new complete moment gain | b12<10beta | lambda<10theta-3=0.144831759741... | Does not necessarily improve pointwise theta. |
| Explicit modest milestone | b12<=32/25=1.28 | lambda<=7/50=0.14 | Improves the complete moment; its persistence exponent207/650 is still above theta. |
| Beat the pointwise benchmark | b12<13beta-1/2=1.176562575326... | lambda<13theta-4=0.088281287663... | Strict improvement in the pointwise exponent. |
| Preferred finite milestone | b12<=29/25=1.16 | lambda<=2/25=0.08 | Pointwise102/325=0.313846153846... . |
| Optimal twelfth moment | b12<=1 | lambda=0 | Pointwise4/13, still above one quarter. |

Preserve the separate quarter route: an unbounded sequence of fixed even orders with complete b_p=o(p). Choose each order after fixing the requested epsilon, not as a growing function of T. The accepted distinct-class reduction is twelfth-order only. Neither optimal eleventh/twelfth moments nor an adequate all-order family has been proved.

The latest reviewed central owner is C_gamma from `strategy/round231_balanced_cancellation/conductor_decision.md`, with T^(4gamma)<n<2T^(1-2gamma), actual divisor characters and d,m>=T^(2gamma-13/42)x(n)^(29/84). Its complete complementary moment budget is m(gamma)=max(1,10gamma,1+20gamma/13). At gamma16/125 the sufficient target is32/25; at gamma13/125 it is29/25. A new bound for a component must be combined with that complementary floor. This owner is reviewed admission evidence, not an accepted new graph reduction.

For this family to beat the pointwise benchmark with its current complementary estimates, both 10gamma and1+20gamma/13 must be below13beta-1/2. The stricter condition is gamma<13(13beta-3/2)/20=0.114765673961... . Thus gamma16/125 can support a modest moment improvement but cannot deliver a pointwise gain merely by improving its central term; its companions would also need improvement. This is a restriction on the current upper-bound calculation, not a lower bound or a restriction on different methods.

Seek a signed estimate across reciprocal frequencies or directly in the radius average for this owner, or a different genuinely complete mechanism. Exact quarter-frequency cancellation in the leading real term is useful structure; nearby frequencies can be coherent. Uniform square-root cancellation in each separate fibre is already excluded. Preserve signs across frequencies and squarefree-label tuples. The accepted and reviewed absolute-certificate obstructions do not lower-bound the actual signed moment.

## 2. Kloosterman transfer: use the mask tool, price the actual operator

The row-prefix proof in the memo is valid for N>=1: n-b stays in [1-N,N], so Q=4N+1 prevents aliasing of h(n-b)=1_(n<=b); the finite geometric-series bound gives a logarithmic Fourier coefficient mass. An interval is the difference of two prefixes. N=0 is the empty matrix. Round200 already proved the corresponding bound independently by dyadic rectangles.

For a multiplier w=sum_j a_j(m)b_j(n), its sufficient cost is A_infinity(w)=sum_j||a_j||_infinity||b_j||_infinity. For a physical amplitude A=sum_j u_j(m)v_j(n), its sufficient coefficient cost is ||A||_pi=inf sum_j||u_j||_2||v_j||_2, equal to its nuclear norm. Do not substitute the Frobenius norm, an entrywise bound, or one of these two costs for the other. Failure of a particular separated certificate does not reject every Schur-multiplier method.

Round200 already has a rank-one complete product coefficient of norm D=sum|c_N|^2<<L^2X^epsilon. Nevertheless the full even-Fejer operator has norm of order L. Its universal estimate is L^3, while the sufficient complete correlation target is L^2; the scalar reconstruction loses L^(1/2). A cheap coefficient norm and sharp-mask lemma therefore do not supply the required arithmetic estimate. Even closing that entire original-t=1 contribution would leave other small-t sectors, independent M1 smooth terms, M2 and endpoints.

The primary-statement check is recorded in `strategy/round231_directive_reconciliation/primary_source_check.md`. For equal source length N=c^eta, use

    E(eta)=max(29/32+eta/8,13/16+5eta/16,11/18+2eta/3),
    sigma(eta)=min(1,1/2+eta)-E(eta).

This compares the cited bound with the standard equal-length baseline. The saving is1/32 at eta=1/2; it is positive only for13/28<eta<7/12 in this comparison. A transfer cost c^rho leaves sigma(eta)-rho before outer reconstruction. The coarser c^(31/32) bound for shorter intervals is valid but need not improve their trivial bound. Unequal lengths require a fresh literal calculation.

An admissible proposal must identify every modulus, unit and gcd condition; stationary factor; summation range; oscillatory symbol; coefficient norm; sharp interval and arithmetic selector; both branches and orientations; endpoint and tail; and the complete complementary contribution. Match the cyclic four-Kloosterman product or bilinear matrix algebraically. Preserve the distinction between linear saving and a gain under square/fourth roots. Require prime, squarefree-composite, prime-power, gcd-return and sharp-endpoint controls for the actual matched coefficients. A failed match rejects that attachment, not the external theorem.

## 3. Decoupling and other complete routes

The identity (l sqrt(k))^2=l(kl) checks cone geometry for the stated triple only. A new application must derive its own surface, integration box, cap scales, Jacobians, Taylor errors and full symbol, then restore first spacing, second spacing and the outer pointwise argument. Retain the source card's l-versus-k warning and all five repairs in the accepted narrow Li–Yang application. The withdrawn Bourgain–Watt results are not available as analytic estimates; their withdrawal is not a ban on decoupling.

Quantify any exclusion of equal rays, near rays, prime-power concentration and endpoint configurations for the literal arithmetic coefficients. Generic positive geometry cannot be presented as signed cancellation. Keep the complete cusp estimate as a separately gated alternative, with both levels and every continuous/local/tail term retained. Full M1/M2/GAR routes may replace the priority if their complete quantitative case is stronger; no route is discarded by preference alone.

## 4. Execution and state effect

Before a new analytic round, use the existing exact interface where possible and supply: the new signed inequality, independent reason it is plausible, prior obstruction bypassed, complete power ledger, and a falsifying control. Compare against both the complete-moment and pointwise thresholds. Stop an attachment when its full cost exhausts its saving at the bottleneck. Reopen only on a relevant source revision, a new proved bridge or a new complete estimate. Do not repeat the Round200 mask proof, old Hankel tail, unchanged source import or equivalent centering as a fresh campaign.

There are at most three candidate tracks, not three automatic concurrent campaigns. Freeze one objective per numbered round, delegate orthogonal interfaces, and close it before choosing a successor. The present work is a bounded user-requested strategy reconciliation; it does not launch analytic Round231.

The reconciliation packet contains two bounded reports, a primary-statement check, an independent strategy review and preservation/graph validation. Update only the workflow pointer in `state/next_round_plan.yml`. Preserve the submitted memo, closed Round230 checkpoint and manifest, graph, proof draft, accepted kernels, validation matrices, ledger and historical evidence. No State Patch, proof promotion or new complete exponent is asserted.
