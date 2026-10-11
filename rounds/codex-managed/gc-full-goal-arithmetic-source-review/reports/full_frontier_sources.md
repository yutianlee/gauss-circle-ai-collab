# Round220: full frontier and two current harmonic-source audits

Campaign: `gc-full-goal-arithmetic-source-review`. Task: `full_frontier_sources`.
Role: source auditor; selected-context, nonblind. Date: 2026-09-28.
Graph SHA256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
Candidate method evidence only. Prior218--219 work in this reused agent is
disclosed; no current sibling report was read. Mathematical experiments: zero.
Exactly two complete external theorem audits are performed below.

## 1. Result: two costed transfers, no complete frontier gain

Neither audited theorem supplies the complete signed moment or any complete
M1/M2/GAR estimate. This is a limitation of the specified transfers, not a
refutation of the actual arithmetic targets or of other uses of the sources.

* Guth--Maynard's current Dirichlet-polynomial theorem has a legal local
  square-root-to-log transfer, but its short-interval count, original index
  length and level normalization cost too much. The resulting distribution
  certificate is already trivial on a relevant full dyadic scale.
* Glidewell's new four-dimensional small-cap theorem admits an exact
  square-root lift. Paying all cap occupancies and all three added-variable
  traces gives the critical twelfth-moment price `T^(7/3+epsilon)` at
  `N~T^(2/3)`. Merely observing exponent12 or four-dimensional curvature
  omits this price. Coarser caps do not improve that critical certificate.

The unchanged complete bound remains
`M12(B_T) << T^(1+epsilon)+T^(10 beta+epsilon)`,
`beta=2 theta_LY-1/2`. The target `T^(29/25+epsilon)` is open and would
give only the fixed-order milestone `102/325`. A sufficient unbounded
sequence of fixed moment orders remains necessary for the displayed
moment-based route to the quarter exponent.

There is also a forward correction to strategy transcription: the graph
and its proved Poisson normalization say `K=XL/D^2` and
`e(sqrt(Xhk))` for M2 UNBAL. Checkpoint217 prints `K=XL^2/D^2` and
`e(sqrt(X) h k)`. Both are transcription errors, confirmed by the conductor;
the closed217 file, graph and proof draft are not edited here.

## 2. Exact quantities, source statements and hypotheses

Use `e(x)=exp(2 pi i x)`, the actual fixed radial mollifier, and

    a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    B_T(R)=sum_(n>=1)a_n(T)cos(2 pi R sqrt(n)-3 pi/4),
    M_p(F)=integral w(R/T)|F(R)|^p dR.

The actual `Psi` is real, even and Schwartz; its signs are retained.
The exact distinct-class integral `I12(T,floor(T^(2/5)))`, all harmonic
indices, both cosine signs and all unequal blocks are as in the accepted216
kernel. Its one-sided upper bound at `T^(29/25+epsilon)` is equivalent,
in the usual every-epsilon sense, to the complete physical moment target.

Audit A is [Guth--Maynard, arXiv:2405.20552v2, Theorem1.1](https://arxiv.org/html/2405.20552v2#S1),
revised 7 April2026; the current primary record identifies v2. In source
variables `L,S,W`, coefficients obey `|b_n|<=1`, and the sample times in
`[0,S]` are 1-separated. If every sampled value of
`sum_(L<=n<=2L)b_n n^(it)` has modulus at least `W`, their number is

    << S^o(1)[L^2 W^-2 + L^(18/5) W^-4 + S L^(12/5) W^-4].       (A)

This is an infinity-norm hypothesis on a single fixed coefficient vector.
Neither a coefficient energy bound alone nor arbitrary square-root
frequencies are its statement. We audit this theorem only, not the other
large-value, difference-set or zeta statements in the paper.

Audit B is [Glidewell, arXiv:2605.27065v1, Theorem1.2](https://arxiv.org/html/2605.27065v1#S1),
submitted 26 May2026, the sole version on the current primary record.
For `1/3<=b<=1/2`, `0<a<=b`, and `p=6+2(a+1)/b>=11`, a Schwartz
function with Fourier support in the specified thickened moment curve,
partitioned into first-coordinate caps of width `Q^-b`, satisfies

    integral_Omega |F|^p <<_epsilon Q^(p b/2+epsilon)|Omega|,     (B)

provided each cap projection has infinity norm at most1; `Omega` is any
regular `Q x Q x Q x Q^a` box. The exact support is `xi1 in[1/2,1]`,

    |xi2-xi1^2|<=Q^(-2b),
    |xi3-3xi1 xi2+2xi1^3|<=Q^-1,
    |xi4+4xi1 xi3-9xi2^2+4xi1^4|<=Q^-1.

At `p=12`, `a=3b-1` and `1/3<b<=1/2`. The arbitrary Fourier-support
form (B), rather than a corollary restricted to equally spaced parameters,
is used below. No extrapolation to arbitrary moment order is imported.

## 3. Derivation and complete restoration

### A. An exact local log-phase map and its cost

Take an actual block `N<n<=2N`, allowing any fixed deletion mask or partial
endpoints, and put `S_N(R)=sum a_n(T)e(R sqrt(n))`. Coefficients are
`O_epsilon(T^epsilon N^-3/4)` on the full truncated range
`N<=T^(3/2)`. A constant cosine rotation and taking the real part cost
no extra power. The argument below treats every term of the block.

For a center `n0~N`, define

    g(n)=sqrt(n)-sqrt(n0)-(sqrt(n0)/2)log(n/n0).

Then `g(n0)=g'(n0)=0`, `g''(n0)=1/(4 n0^(3/2))`, and on a sufficiently
small fixed relative interval `g''(n)~N^-3/2`. On length `M<=cN`,

    R g(n)=O(T M^2/N^(3/2)),       t_R=pi R sqrt(n0),
    e(R sqrt(n))=e(R[sqrt(n0)-(sqrt(n0)/2)log(n0)])
                 n^(i t_R) e(R g(n)).                         (A1)

Thus the residual is not uniformly small on a whole dyadic block: its
natural size there is `T sqrt(N)`. To retain it by the following bounded
smooth separation, choose

    M~N^(3/4)T^-1/2,    B~N/M=T^(1/2)N^(1/4),                 (A2)

when `N>=c T^(2/3)`, with singleton intervals at the transition. On scaled
coordinates `R/T` and `(n-n0)/M`, every fixed derivative of `e(R g(n))`
is bounded. Smooth extension on a fixed rectangle therefore gives an
exact two-variable Fourier series with rapidly decreasing coefficients,
uniformly in the block and center. Its row factors have modulus1; its
column factors modify one fixed vector `b_n`. This does not discard a
pointwise error. Endpoint indicators are fixed column masks, requiring
no smoothness of arithmetic masks.

For completeness, choose polynomially growing positive levels `q_l`
with both `sum |c_l|q_l<infinity` and `sum q_l^-2<infinity`. If the
separated sum is large, some factor polynomial exceeds its correspondingly
weighted level. Applying (A) and summing these levels costs a constant
in each of its three terms. This justifies use of the infinite exact
expansion, not an unquantified product-norm grant.

The source index length remains `L~N`, even though the vector is supported
on `M` integers. Translation of the index gives `log(n0+m)`, not `log(m)`;
one cannot replace the source length by `M`. The source time interval has
length `S~T sqrt(N)`. Translating its left endpoint into the coefficients
is legal. A maximal 1-separated subset covers a level set in the time
variable by intervals of bounded length, so converting back to radial
measure costs `N^-1/2`. This uses no unproved persistence assertion.

If `|S_N|>V`, one of the `B` pieces exceeds `V/B`. After coefficient
normalization the source threshold is

    W~V N^(3/4)/B                                             (A3)

up to a harmless `T^epsilon` loss. The union over all pieces and Fourier
factors therefore gives the full-block certificate

    meas{|S_N|>V}
      <<_epsilon T^epsilon min{T,
           B^3 V^-2 + B^5 N^(1/10)V^-4
                      + T B^5 N^(-3/5)V^-4}.                 (A4)

Indeed multiply (A) by `B/sqrt(N)` and insert (A3). All three terms of
the source are retained. For `N~T^(2/3)`, one has `B~T^(2/3)` and the
first price is `T^2 V^-2`. It exceeds `T` throughout the relevant range
`1<=V<=T^(beta+o(1))`, since `beta<13/100`. Thus this transfer gives
only the trivial radial measure on that scale. The normalized level
`W~V T^-1/6` is also far below a useful high-value scale for the source.
This is a computation of the available upper certificate; it asserts
neither actual high points nor a lower bound on the physical distribution.

When (A2) would have `M<1`, the proposed multi-integer local map has no
useful range; singletons or accepted204 controls remain. The unchanged
complete argument can use accepted204 on every such block, on any block
where (A4) is weaker, and on all remaining levels. No band is omitted.

### B. The exact moment-curve lift, cap occupancy and every trace variable

Choose `t_n=sqrt(n/(3N))`, which stays in a compact subinterval of
`(1/2,1)`, and define the finite exponential polynomial

    F(x)=sum_(N<n<=2N)a_n(T)e(x1 t_n+x2 t_n^2+x3 t_n^3+x4 t_n^4).

Then `S_N(R)=F(R sqrt(3N),0,0,0)` exactly. There is no Taylor approximation.
The `t_n` have spacing comparable to `N^-1`. Write `C=Q^b`, the number
of available caps up to fixed constants. Every cap contains at most
`O(1+N/C)` indices, and hence its normalized infinity price is

    A_cap << T^epsilon N^-3/4 (1+N/C).                        (B1)

This is an actual amplitude bound; no square-root cancellation within
a coarse cap is assumed. To apply the Schwartz formulation rigorously,
multiply `F` by a Schwartz function whose Fourier transform is a unit-L1
bump of arbitrarily small support around zero. The support remains in
the source tube, and each cap projection has the bound (B1), including
neighboring boundary caps. Letting the support shrink proves the same
box inequality for `F` by convergence on compact boxes. No spatial
cutoff cost or artificial frequency regularity is hidden here.

At `p=12`, `Q^a=C^3/Q` and `|Omega|=Q^2 C^3`. Retain the source
loss `Q^eta` for every fixed `eta>0` independently of the coefficient
loss `T^epsilon`: arbitrary Q is not assumed polynomially bounded in T.
Thus (B) and (B1) give

    integral_Omega |F|^12
      << T^epsilon Q^eta N^-9(1+N/C)^12 Q^2 C^9.             (B2)

To restrict to `x2=x3=x4=0`, choose a fixed Schwartz reproducing kernel
`kappa` in those three coordinates whose Fourier transform is1 on their
bounded frequency support. Holder gives

    |F(x1,0,0,0)|^12 <= C integral_R^3 |kappa(y)||F(x1,y)|^12 dy.

Partition this integral into boxes of sides `Q,Q,Q^a`. Their weighted
suprema of `|kappa|` have bounded sum because all side lengths are at
least1. Apply (B2) to each translated source box. Cover the physical
`x1` interval, of length `S~T sqrt(N)`, by `O(1+S/Q)` intervals of
length `Q`, and restore `dR=dx1/sqrt(3N)`. The exact resulting price is

    M12(S_N) << T^epsilon Q^eta N^(-19/2)(1+N/C)^12
                          Q^2 C^9 max(1,S/Q).               (B3)

The source average cannot replace this trace: the added spatial volume
`Q^2 Q^a` is fully present in (B3). Paying just one or two added variables
would be an incorrect application.

For `C<=N`, (B3) becomes

    T^epsilon Q^eta N^(5/2) Q^2 C^-3 max(1,S/Q).            (B4)

For fixed `Q`, choose the largest permitted `C<=N`, namely
`min(N,Q^(1/2))`, if compatible with `C>Q^(1/3)`. When `C>=N`, the
price increases as `C^9`, so finer empty caps do not help. At the critical
scale `N~T^(2/3)`, one has `S~N^2`:

* `Q<=N^2`: `C<=sqrt(Q)` gives price at least
  `N^(5/2) S Q^-1/2`, minimized at `Q~N^2`.
* `N^2<=Q<=N^3`: `C~N` gives price `N^-1/2 Q^2`, again minimized
  at `Q~N^2`.
* `Q>N^3`: admissibility forces `C>Q^(1/3)>N`; the certificate in
  (B3) retains `Q^eta N^(-19/2)Q^5`, which is larger. No conversion
  of `Q^eta` into `T^epsilon` is made on this unrestricted range.

Here “at least” refers to the algebraic size of this explicit source
certificate, never to the actual moment; its extra `Q^eta>=1` does
not weaken these comparisons. The admissible optimizing choices below
have Q bounded by a fixed power of T, so choosing eta sufficiently
small absorbs that loss into the final `T^epsilon`. The choice
`Q=N^2,b=a=1/2` attains the minimum algebraic price

    N^(7/2)=T^(7/3).                                        (B5)

For reference, optimizing the same whole-block certificate more generally
gives `T N^2` for `N<=T^(2/3)` by covering with `Q=N^2` boxes, and
`T^(1/2)N^(11/4)` for `N>=T^(2/3)` by taking `Q=S,C=sqrt(S)`.
Partial final boxes only reduce support; all their occupancy and covering
costs were included. These formulas do not claim to optimize every
possible further arithmetic localization of the source.

### C. Complete tails, moment reconstruction and all other frontiers

The accepted Schwartz/divisor estimate makes the entire `n>T^(3/2)`
tail `O_A(T^-A)` uniformly in `R`; its fixed-order moments and mixed
terms are negligible by the power inequality and the finite L1 envelope.
The singleton `n=1`, partial lower blocks and `O(log T)` remaining blocks
are kept. Minkowski or `|sum z_i|^p<=m^(p-1)sum|z_i|^p` pays every
unequal block at a logarithmic cost. Neither audit improves the critical
block certificate, so restoration falls back to accepted204:

    D_B(V)<<T^epsilon(V^-2+T V^(-136/13)),
    sup|B_T|<<T^(beta+epsilon),
    M_p(B_T)<<T^(1+epsilon)+T^((p-2)beta+epsilon).             (C1)

For `V0=T^(13/125)` the complete twelfth high-tail upper price remains
`W^10+T W^(20/13)+V0^10+T V0^(20/13)<<T^(10 beta+epsilon)` with
`W=T^(beta+epsilon)`. The improved target has not been proved by the
new sources. None of the auxiliary complex-source bounds changes the
actual real signs or authorizes arbitrary rephasing as a counterexample.

| Complete frontier | Literal required estimate and conclusion of this audit |
|---|---|
| M1 HARD | Entire actual `sum_(h~L)sum_(4h<n<16h,n odd)chi4(n)a(h,n)e(sqrt(Xhn)) << L^(3/2)X^epsilon`, with all original small-t/large-G ranges. The source needs either one common log-phase coefficient vector across times or the paid four-variable lift. Actual joint symbols and pointwise real-X control are not supplied by either theorem. The P2 complement alone would not close HARD. |
| M1 SMOOTH | Every physical `B1(D,L;X)<<X^(1/4+epsilon)` with the literal taper, floors, stars, short blocks and transform boundaries. The first critical profile still has capacity `X^(1/3+o(1))`, missing `X^(1/12)`. A mean estimate on an added box does not supply this uniform physical block estimate. |
| M2 TOP | `E_top=E_owned+2 Re C_comp`, and the complete single outer `Re C_comp<<L^2 X^epsilon`. Neither audit bounds the actual unequal-product complement. Separate row or product norms omit precisely the required signed completion. |
| M2 BAL | `|sum_G G P_G|<<L^(3/2)X^epsilon` for every smooth `1<=K/L<=16`, both shifts and all labels including the exact-square j=2 boundary. Four-dimensional curvature alone supplies neither this joint packet nor its complete coefficient norm. |
| M2 UNBAL | `sum_(h~L,k~K)chi4(h)a(h,k)e(sqrt(Xhk))<<(LK)^(3/4)X^epsilon`, **`K=XL/D^2`**, `K/L>16`. The proved physical factor is `X^(1/4)(LK)^(-3/4)`, up to its stated constant phase and O(1) error. Neither a log-phase average nor an uncosted moment-curve lift proves this full matrix estimate. |
| Total-M1 GAR | `Re{e(1/8)sum_(n<=16sqrt X)C_X^*(n)n^(-3/4)e(sqrt(Xn))}<<X^epsilon`. The actual angular divisor symbol differs from `r2`; the accepted nonlower radial assembly leaves the lower aggregate open. GAR controls total active M1 only and still requires all M2 and endpoint restoration; it does not prove blockwise M1. |
| Complete anchored energy | The sufficient219 reciprocal-energy input is `E<=J^2 v^2 T K/256+C_eta T^(208/2625+eta)JAK`, `A=T sqrt(N)/D,K=N/D`. All `R_j^2/a-R_l^2/b-m` and `R_j^2/a+R_l^2/b-m`, `m in Z`, odd labels, actual signs and moving weights remain. Neither audited theorem estimates this whole quantity. |
| Unbounded fixed orders | For an unbounded sequence of fixed even `p`, `Q_p=floor(T^(1/p))` and `I_p(T,Q_p)<=C_(p,epsilon)T^(5/4+epsilon)` suffice. Neither audit supplies these signed grants. A theorem at p12, or at a bounded collection through p14, is insufficient. |

All direct parents retain real `X,D`, floors, stars, half weights, support
crossings, all denominator ranges and their endpoint assembly. If a new
external kernel were embedded by rounding `R_j^2=M_j+delta_j`, the exact
factor `e(delta_j k/a)` must remain with its proved product/operator norm.
The fact `K/A<=T^-1/4` alone does not pay an accumulated error. A row
indexed by `(j,a)` is not automatically a product of a j-vector and an
a-vector. No result from the current isolated operator task is assumed.

The moment-family implication is transparent: same-order absorption pays
repeated classes, and the head costs `T Q_p^(p/4)=T^(5/4)`. A complete
normalized exponent `E(p)=5/4` restores the sharp pointwise exponent

    [E(p)+1+p/2]/[2(p+1)]=1/4+7/[8(p+1)].                  (C2)

Take an arbitrarily large fixed `p` for a prescribed final epsilon;
no `p=p(T)` is asserted. For the current twelfth target, inserting
`E(12)=29/25` gives `102/325`. The whole-moment route could prove the
final circle theorem independently without proving the original M1/M2
parent statements.

## 4. First doubtful or unproved step

For Audit A the first invalid shortcut would replace the full square-root
phase by a log phase at length `N`, or use short support length `M` as
the source index scale. Formula (A1) shows the derivative mismatch and
(A4) pays a legal replacement. The resulting price fails, without ruling
out a new theorem proved directly for the square-root phase.

For Audit B the first invalid shortcut would restrict a four-variable
average to its physical line at no cost, or assert unit cap norm while
a cap contains `N/C` terms. Equations (B1)--(B5) pay both. A sharper
trace theorem exploiting actual arithmetic coefficients is not supplied
by (B), and remains an additional unproved premise.

For the complete objective the missing step remains actual signed
cancellation before the decisive norm. Neither changing variables,
paying endpoint masks, exact-frequency independence, nor bounding an
enlarged coefficient class supplies it. All claims of failure here are
restricted to the written import and cost certificate.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Current primary versions | GREEN: current records pin2405.20552v2 and2605.27065v1; exact theorem text inspected. Benchmark/withdrawal work is left to the conductor. |
| Exact theorem hypotheses | GREEN: common fixed infinity-bounded vector, 1-separated log times; exact moment-curve tube, p range, cap norms, regular boxes and Schwartz limit are explicit. |
| Complete kernel map | GREEN for the two limited transfers; RED for a target-sized complete import. No logarithmic phase or regular parameter spacing is silently substituted. |
| Coefficient norms | GREEN: divisor envelope, B-piece threshold, source ambient length, all cap occupancies, Fourier separation and every trace variable paid. |
| Aliases/endpoints | GREEN scope control: actual signs, plus/minus modular aliases and moving stars remain necessary; neither source removes them. Column masks in the finite audits are exact. |
| All frontiers | GREEN: both M1, all three M2, total-M1 GAR, anchored energy and fixed-order family compared. Forward correction of both UNBAL transcription errors recorded. |
| Full exponent restoration | GREEN: (A4), critical `7/3`, unchanged `10 beta`, conditional `102/325`, and (C2) are distinct. No new global exponent. |
| Actual versus enlarged scope | GREEN: no rephased model refutes actual high points, and no certificate price is called an actual lower bound. |
| Statement-only control | This source report is nonblind. Its elementary derivative, cap-count and trace calculations are exposed for an independent seam; no blind validation is claimed. Current isolated work is neither read nor presumed. |
| Unbounded fixed orders | GREEN: fixed p constants are allowed; bounded p source ranges do not close quarter. |

The controls are analytical. No numerical experiment, data fitting or
asymptotic inference from finite tests was performed.

## 6. Dependencies, exact artifacts and bounded source screen

Only the brief and its listed local context were used. SHA256 at reading:

| Artifact | SHA256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `state/active_campaign.yml` | `a3bbd8a17eeb5e5b492f0bccf115332823dfe4d1a6c748c595dd0fee5b286e2b` |
| `strategy/round220_full_goal_arithmetic_source_review.md` | `043f5629f643064c5597a92b7005b7596de11264bdb9d2a14bdc2d1a20857162` |
| `strategy/gauss_circle_strategy_review_2026-09-23.md` | `0729f1d9c596867e7a06bdcd096847b32e6747653235706b01275a153bd617c6` |
| `strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md` | `39054e4123c11b85e55d9146794cfdd7453915ebefd8a1286763e08b4ecabcd2` |
| `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md` | `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212` |
| `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` | `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee` |
| `rounds/codex-managed/gc-complete-anchored-divisor-energy/synthesis.md` | `4515ccc38fecea9d486df9663f2717c4fcbf508f85a446229467d5a4e31b5711` |
| `state/best_proof_draft.md` | `65989358d00f0ecf7c4d385ea58bfad09eaa026af98924266207c5f8af872f00` |
| `rounds/codex-managed/gc-full-goal-distinct-source-review/reports/full_frontier_sources.md` | `3fcd969a5fb4b53edb6cbbd337b19ae18c363fb44bc1cdc0042a80f05c1fd338` |
| `rounds/codex-managed/gc-full-source-method-review/reports/bilinear_arithmetic_sources.md` | `26425644ad0a0473b315a61d7499f82f4f053ebd363c15340032dea873ce2978` |

The relevant authoritative statements were inspected directly, including
the proved smooth M2 Poisson normalization, all five complete parents,
GAR equivalence and radial assembly. Historical source failures are
context only and are not counted as new progress.

The bounded primary search also produced the following scope screens,
not additional full theorem audits or imports:

* [Fouvry--Kowalski--Michel--Sawin,2511.09459v3](https://arxiv.org/abs/2511.09459v3),
  revised11 March2026: finite-field trace-function bilinear estimates with
  geometric monodromy requirements. No exact project trace kernel with
  these structural requirements and uniform conductor is supplied here.
  A real reciprocal phase or `chi4` factor alone does not establish one.
* [Yao Zhi,2608.15458v1](https://arxiv.org/abs/2608.15458v1),16 August2026:
  higher additive congruences involving inverse powers over a prime field.
  Prime-field congruence counts do not yet map the signed real anchored
  energy with all ordinary denominators, aliases and moving weights.
* [Robles,2609.11070v1](https://arxiv.org/abs/2609.11070v1),10 September2026:
  effective linear exponential sums with multiplicative coefficients and
  a uniform mean-square coefficient hypothesis. The abstract bound keeps
  an `N/log N` term. No fixed power saving or exact nonlinear square-root
  phase/coefficient application follows from that scope description.
* [Dong--Song--Wang--Zhang--Zhao,2509.09771v1](https://arxiv.org/abs/2509.09771v1),
  11 September2025: Omega results for multiplicative Dirichlet polynomials;
  this is not the missing upper-bound theorem.

These screens identify possible mathematical themes, not accepted source
cards. The two exact audited statements are (A) and (B) only. This is a
bounded current search, with no claim of exhaustive literature coverage.

## 7. Recommended state effect and one next complete objective

**No change** to mathematical graph status, accepted exponents or proof
draft. Retain the two source-transfer cost audits as reviewed method
evidence if their independent seams pass. Correct both checkpoint217
UNBAL transcriptions forward in the conductor's220 checkpoint, without
altering the historical file or graph-owned normalization.

Recommendation only: after220 closure, select one bounded attempt at the
complete actual `I12(T,floor(T^(2/5)))<=T^(29/25+epsilon)`, with the paid
small-class head removed before the joint signed estimate. A reasonable
changed mechanism to test is a direct high-value/Gram argument for the
actual square-root phase, retaining the arithmetic mask and coefficient
vector through the joint step. Audit A motivates looking for joint
large-value cancellation but gives no theorem for this new phase; Audit B
shows why adding variables and then taking a generic trace is not enough.

The objective is the full integral, not a diagonal, inverse envelope,
one alias, one cofactor rectangle or a smoother substitute. All signs,
unequal blocks, moving endpoints and infinite tails must be restored in
the final inequality. Success requires a verified complete moment power;
otherwise close with the exact failed certificate and its full cost.
This recommendation does not authorize a successor here and does not
claim the mechanism will work. Its eventual-quarter criterion remains
the unbounded-fixed-order family in (C2), or an independent complete
closure of the necessary original parents.

The assigned bounded report ends here; no sibling, shared-state or
successor artifact was edited.
