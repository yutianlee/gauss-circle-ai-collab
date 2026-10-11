# Gauss circle research review and revised strategy

Conductor review, Round230, 11 October2026. Campaign: `gc-research-status-strategy-reset`. This checkpoint supersedes the prospective strategy in checkpoint229 after final review and closure. It does not rewrite accepted mathematics. Starting graph:401 nodes, SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

## 1. Assessment and decision

The quarter-exponent theorem remains open. The project has substantial exact reductions, controls and some complete moment estimates, but its strongest certified pointwise exponent has not improved. The latest work has clarified the missing cancellation more than it has reduced it.

The principal strategic correction is to stop automatically continuing the cuspidal route merely because its continuous partner is paid. That leaves an important complete target, but no currently matched signed input. Future analytic rounds need a concrete new mechanism and a complete quantitative comparison before launch. A further trace identity, local normalization or shorter transformed sum is not itself a reason to launch another analytic round.

Use the complete twelfth moment as the preferred finite milestone when a new arithmetic mechanism is available. Keep the full cusp estimate as a parallel candidate for admission, not an automatic successor. Preserve the full quarter goal through a separately stated unbounded family of fixed-order moment bounds or a complete subpower wave bound. No Round231 analytic task is launched by this review.

## 2. Current status and measured progress

Write P(X)=#{(m,n) in Z^2:m^2+n^2<=X}-pi X. The target is P(X)<<_epsilon X^(1/4+epsilon), uniformly for real X.

| Item | Present status |
|---|---|
| Internal unconditional pointwise result | X^(1/3+epsilon), accepted by the graph. |
| Strongest certified external pointwise benchmark | X^(theta+epsilon), theta=(3292+25sqrt(1717))/13762=0.314483175974... . The repaired Li–Yang final application retains all five qualifications in the graph; its general printed propositions are not accepted wholesale. |
| H1–H4 and full Fejer residual R5 | Accepted infrastructure; the main signed sums remain. |
| M9, M1, M2, endpoint uniformity and quarter | Open. |
| Round201 | Accepted exact radical-resonance mass; no near-resonance bound. |
| Round202 | Accepted obstruction to a specified absolute majorant; no lower bound for the actual signed moment. |
| Round204 | Last accepted improvement of a complete moment bound. For the complete real wave, M_p<<T^(1+epsilon)+T^((p-2)beta+epsilon), beta=2theta-1/2. Both distribution terms V^-2 and T V^(-136/13) remain. No pointwise improvement. |
| Round216 | Accepted reduction of the complete twelfth moment to a signed distinct-radical integral, with all repeated-class terms paid. The remaining integral is unestimated. |
| Round217 | Accepted obstruction to the termwise absolute distinct-class certificate. |
| Rounds227–228 | Reviewed complete spectral reduction and target-sized entire continuous component. These are evidence, not dependency-closed accepted graph theorems. The entire cusp term remains. |
| Round229 | Reviewed source limitations and radial-kernel controls; no complete bound improvement. |

Rounds205–229 comprise25 rounds:16 analytic attempts and9 reviews. None improved a complete moment bound or pointwise exponent. Rounds218–229 are12 consecutive identity-patch rounds. These counts measure a stalled quantitative estimate, not a lack of useful reductions or an impossibility theorem.

Two provenance corrections matter. Checkpoint229's wording attributing an all-order class/head bridge to “Accepted216” is too strong: the accepted216 node is specifically twelfth-order and expressly excludes a sufficient unbounded-order family. The inherited complex13/56 comparison is also checkpoint evidence, not a matching accepted graph theorem located by this review. Neither is promoted here. The quarter implication from a *direct complete-wave* moment family is proved conditionally in this round; extending the distinct-class reduction to all orders remains a separate obligation.

## 3. Literature update and its consequence

The current primary [Li–Yang record](https://arxiv.org/abs/2308.14859) still lists v2 of14 September2023. The source audit's qualifications remain. The [Assing–Humphries record](https://arxiv.org/abs/2607.13518) remains v1; its CM majorant does not become an exact signed weight identity through a metadata check.

A genuine update since the last review is [Kim–Ko v3,2 October2026](https://arxiv.org/abs/2511.04503v3). Its Theorem1.1 and Remark1.2 strengthen the weight formulation and explicitly allow locally finite Borel measures. Point-mass evaluation can therefore be handled directly. For the complete application tested here, however, the actual coefficient norm, cap occupancy and tube factor still restore only the triangle-scale complex wave exponent1/4, hence physical3/8. The revision improves applicability without improving this project's complete bound. This conclusion concerns that explicit norm-based application, not all possible uses of the paper.

[Yang2608.23886v1, Theorem A](https://arxiv.org/html/2608.23886v1#S1.SS1) relates toric character sums to periods built from an induced Eisenstein representation. It does not provide the required signed sum over fixed-level Maaß cusp forms with actual CM point weights. The shared word “toric” does not bridge that family mismatch. Its other arithmetic applications are not imported here.

The bounded current-record review preserves the three withdrawal exclusions recorded in229. It has found no source that changes the complete benchmark after full hypothesis matching. This is not an exhaustive assertion about all current literature. Exact versions, searches, theorem cards and application costs are in the Round230 source report.

## 4. Quantitative admission gates

Let M_p(B_T) be the unnormalized complete real-wave moment over a fixed radial window of length comparable to T, large enough for sharp-discrepancy restoration. For each fixed p, suppose M_p(B_T)<<T^(b_p+epsilon). Monotonicity of the lattice count makes a discrepancy of size M persist on a one-sided interval of length comparable to M, including integer jumps. The wave relation and dx=2R dR give, for all b_p>=1 used below,

    theta_p = 1/4 + (b_p+1/2)/(2(p+1)).

Constants may depend on p. Thresholding the uniform smoothing error gives the sharper general formula max(1/4,1/4+(b_p+1/2)/(2(p+1))), including b_p<1. No assertion here uses p growing with T.

For the cusp gate below, D is the entire sum of both cusp levels in the [frozen complete interface](../rounds/codex-managed/gc-full-goal-cuspidal-source-review/briefs/complete_cuspidal_interfaces.md). It uses R comparable to T, every dyadic2<=N<=P<2T^(3/2) with P the least dyadic integer at least T^(3/2), A=(1+N/T)^(-J), and the actual g_N(x)=(x/N)^(-3/4)Psi(sqrt(x/T))w(x/N). All constants, local factors and complete partners are those of that interface.

| Complete proposed result | Admission comparison |
|---|---|
| Fixed twelfth moment | To improve theta, require b_12<13beta-1/2=1.1765625753... . The accepted exponent is10beta=1.2896635195... . |
| Concrete twelfth milestone | b_12=29/25 would give theta_12=102/325=0.3138461538... . This would improve the benchmark by0.0006370221..., but would not prove quarter. The complete target remains unproved. |
| Quarter by moments | An unbounded sequence of fixed even orders with b_p=o(p) suffices. In particular b_p<=5/4 gives1/4+7/[8(p+1)]. Choose p for the requested epsilon, then hold it fixed. Neither family is currently proved. |
| Complete cusp route | For every scale and real radius, 2Re D<<A^2N^(3/2)T^(2gamma+epsilon), with all partners retained, gives the sufficient complete complex exponent max(gamma,0). Benchmark improvement requires gamma<beta; quarter requires gamma<=0. |

At N=T, the elementary whole-cusp cap is A^2T^2. To beat the real benchmark through the stronger complex route requires a saving greater than T^(0.2420672961...) from that cap; quarter requires T^(1/2). A small improvement of the larger positive spectral certificate does not meet this gate. No one shell or single cusp level inherits a complete result automatically.

The accepted moment curve itself gives a pointwise exponent at least theta+(1-3theta)/(p+1)>theta for every finite p. Its limit recovers theta but cannot improve it. This explicitly rules out presenting interpolation of the current curve as new progress.

## 5. Revised work allocation and stopping rules

Before freezing an analytic round, require one short admission packet specifying the literal complete quantity, the new arithmetic or source input, the signed pairing it preserves, the legal parameter range, every complementary term, and the restored power against the gates above. A conjectured new lemma must come with an independent reason it could hold and a derivation that reaches a complete target; it cannot merely rename the original gap.

Prioritize a complete actual-coefficient twelfth-moment improvement if such a packet exists. Its advantage is a finite, graph-backed reduction and a precisely measurable intermediate result. Its difficulty is genuine signed cancellation: the accepted absolute-certificate obstruction remains binding. Keep the direct complete-wave fixed-order family as the long-term quarter route, without silently extending the twelfth-order distinct-class theorem.

Admit the cusp route when an exact local/CM weight identity is paired with a genuinely signed estimate for the moving test, or when a new complete derivation bypasses that interface. The whole continuous bound is retained, but cannot substitute for this missing input. Preserve both primitive conductors, the oldspace denominator, all two-adic descendants, analytic tests, all cusp levels, all spectral/geometric tails and the continuous reconstruction. A normalization-only task may be useful validation, but must be classified as such and must not trigger an analytic chain automatically.

Other full M1/M2/GAR routes can replace this priority if their admission packet has a stronger complete case. Preserve M1 HARD and independent SMOOTH; M2 TOP, BAL and UNBAL; GAR lower ownership through159 and its separate cross owner; all endpoints. M2 UNBAL retains K=XL/D^2 and phase e(sqrt(Xhk)); GAR retains its actual angular-divisor coefficient, not r2. No favorable local sector deletes its complement.

Retain the95/5 planned analytical/symbolic allocation, with the protocol's80/20 hard limit. Run at most two complete analytic attempts on an unchanged premise before reassessment. Reopen a failed source transfer only for a relevant source revision, a proved new coefficient/measure bridge, or a new complete cancellation estimate. Broad searches become event-driven after this review; repeated reviews with no changed input are not mathematical progress. Do not schedule automations or launch successors from this document.

## 6. Validation and limitations

Three independent tasks audit graph progress, current primary sources and statement-only moment restoration. The conductor independently derives the persistence and threshold calculations, checks current source statements, and compares all complete bounds. Wolfram checks exact exponent identities; local rational and high-precision arithmetic reproduces them. These are diagnostic controls, not proofs of asymptotic estimates.

The new strategy and source costs require nonauthor review before closure. The historical graph's accepted proofs and the entire literature have not been reproved in this round. In particular, retained228 spectral evidence still needs dependency-closed packaging if future work relies on it for theorem promotion.

## 7. State effect and next action

Apply an identity State Patch after green review and mechanical validation. Preserve all401 graph nodes and proof-draft bytes. Record the source revision and attribution corrections in current strategy/state summaries while leaving closed rounds immutable. No complete exponent or moment gain is claimed.

Round231 remains pending design. Its first action is to assess a concrete new complete-bound admission packet against Section4; it is not an instruction to repeat the missing CM normalization or another unestimated transform. If no new mechanism meets the gate, record that fact without manufacturing another analytic campaign. The full proof goal remains open.
