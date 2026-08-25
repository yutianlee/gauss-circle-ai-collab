# Round 150 conductor controls

- Campaign: `m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate`
- Round: 150
- Starting graph: `b6c5ee5b0d51d347876b389c05c78596c069b190af715d297bd937701ea893b6`
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| literal_nonzero_collar_expansion | GREEN. The candidate retains both compressed coefficients, both actual profiles, both exact prefixes, parity, squarefreeness, common gcd, centered wrap, character, reciprocal phase, and every support condition. |
| two_row_divisor_incidence_linearization | GREEN. Forced primes form $F=[a_1u_1,a_2u_2]$, forbidden primes form $P=\operatorname{rad}(c_1c_2s_1s_2v_1v_2)$, and exact Mobius inversion over $z\mid P$ has $X^\varepsilon$ arithmetic projective norm. The norm is not claimed for the remaining prefix/profile matrix. |
| prefix_profile_d_dependence | GREEN as an audit. Both prefixes and samples remain joint row-cell functions. The bounded-$M$ theorem uses the accepted actual-profile derivative ledger; no global variation follows from boundedness alone. |
| half_weight_coefficient_norm | GREEN. The $a\mid d_{\mathrm o}$, $c^{-3/2}$, and $s^{-1}$ sums prove $\sum_L|B(L)|/\sqrt L\ll X^\varepsilon$ for all $L\ll E$ and every finite prefix. |
| fixed_wrap_interval_and_count | GREEN. A supported solution forces both shifted linear factors positive and of sizes $NL_i$; one reduced denominator lies in an $O(1)$ interval after the other is fixed, giving $Q\min(L_1,L_2)/h$. |
| all_L_h_and_row_summation | GREEN. The literal $1/(L_1L_2)$ weight, global half-weight norm, harmonic $h$ sum, and $O(D)$ rows give $DQX^\varepsilon$ per fixed wrap. |
| k_zero_and_exceptional_factor | GREEN. The proof never divides by $k$ and includes $k=0$; an independent determinant count agrees. The exact relations exclude zero factors, including denominator-divides-$N$ cases. |
| packet_cardinality_and_power | GREEN. Every selected packet of $O(1+R^2/Q)=O(1+\sqrt M/D)$ wraps costs $DQ(1+R^2/Q)\ll R^2D$. The full wrap range is not identified with this packet. |
| shifted_factor_identity | GREEN. Direct expansion and the two one-factor identities verify signs, integrality, positivity, both signs of $k$, and both signs of $\rho$. |
| full_shift_divisor_summation | GREEN as a no-go, OPEN as a signed estimate. For $k\ne0$, fixed-shift divisor recovery is $X^\varepsilon$, but separate summation over $h,k,\rho$ loses at least $R$ at raw capacity. No upper capacity is called a signed lower bound. |
| bounded_M_actual_profile | GREEN. The accepted Round-148 factorization and derivative ledger give bounded variation at $M=O(1)$; weighted van der Corput and Abel yield $|G_U(d)|\ll RX^\varepsilon$. |
| statement_only_profile_falsifier | GREEN by scope. An arbitrary bounded smooth profile with uncontrolled variation can align the finite samples; this rejects a weakened-hypothesis theorem, not the actual profile or fixed-wrap bound. |
| source_theorem_collar_match | GREEN as a direct no-match. Bombieri--Iwaniec, Duke--Friedlander--Iwaniec, Bettin--Chandee, and Reuss fail exact separability, coefficient, weight, shift-family, cluster, or power hypotheses. No literature-impossibility claim is made. |
| D1_L1_full_frequency_test | GREEN/OPEN split. Bounded $M$ closes through actual curvature; fixed wraps close absolutely; growing-$M$ large wraps remain the literal no-row-average reciprocal endpoint. |
| tuple_absolute_signed_separation | GREEN. Raw fixed-wrap counts, coefficient-weighted absolute masses, signed large-wrap sums, and adverse method capacities remain distinct. |
| exact_generic_tge2_cross_and_downstream_scope | GREEN. Exact $\rho=0$ retains its prior owner; growing-$M$ generic, all $t\ge2$, the Round-138 cross owner, M1, M2, endpoint, M9, bridge, target, and exponents remain open or unchanged. |

## 2. Review gate

The terminal independent reviews are:

- `reviews/blind_fixed_wrap_lemma_review.md`: GREEN for every fixed
  wrap after the full $L_i\ll E$ summation, with the packet/full-collar
  distinction explicit;
- `reviews/independent_conductor_round150_math_review.md`: GREEN for
  the incidence, norm, every-fixed-wrap count, packet powers,
  shifted-factor audit, bounded-$M$ actual-profile edge, endpoint, and
  downstream scope after three candidate repairs; and
- `reviews/source_conductor_round150_final.md`: GREEN for the fixed-wrap
  core, bounded-$M$ variation/curvature placement, source-scoped
  large-wrap no-match, and downstream scope; the signed large-wrap sum
  remains OPEN.

The candidate repairs scope the projective norm to arithmetic incidence,
state $k\ne0$ for divisor recovery, and put the full support and
$k\notin\mathcal K$ condition into the residual signed sum.

## 3. Primary-source controls

The source report checks exact theorem statements and direct placements
in the original Bombieri--Iwaniec double-large-sieve paper,
Montgomery--Vaughan large sieve, Duke--Friedlander--Iwaniec quadratic
divisor paper, Bettin--Chandee Kloosterman-fraction paper, Reuss
squarefree-shift paper, and Robert second-derivative paper.  The first
five do not directly accept the literal large-wrap coefficient.  The
last supplies the exact interval estimate used at bounded $M$, with the
weighted form derived by discrete Abel summation.

## 4. Power and endpoint controls

The relevant identities are

$$
 Q\asymp\frac{DR^2}{\sqrt M},\qquad
 \frac{R^2}{Q}\asymp\frac{\sqrt M}{D},\qquad
 \frac NQ\asymp\frac{R^2\sqrt M}{D}.
$$

Thus the full centered wrap range is a factor $R^2$ larger than the
target-safe packet.  The fixed-wrap energy ratio to target is
$DQ/(R^2D)=D/\sqrt M\le1$.  The separate all-shift divisor capacity
relative to raw pairs is

$$
 \frac{N}{DQ}\asymp\frac{R^2\sqrt M}{D^2}\ge R.
$$

At bounded $M$, the reciprocal second-derivative terms are both
$O(R)$; for growing $M$, the first becomes $RM^{1/4}$.  At
$D=1,L=1$, the bounded-$M$ row is proved but the growing-$M$ large-wrap
character reciprocal sum remains open.

## 5. Pre-mutation validation

Before graph mutation:

- active campaign validation: PASS;
- graph validation at the starting SHA-256: PASS;
- State Patch JSON parse and dry validation: PASS;
- candidate equation check: 31 tags, 31 unique tags, and 31 balanced
  dollar-display pairs;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- Round-150 strict UTF-8/LF scan: PASS for all 17 artifacts after
  mechanical line-ending normalization, with no BOM, forbidden C0
  byte, zero-width character, replacement character, or missing final
  newline; and
- whitespace diff check: PASS.

The State Patch proposes two creates, five updates, nine rejections,
and eight no-change decisions.  Application and the resulting graph
hash are recorded below only after the validation matrix is GREEN.

## 6. State mutation and post-validation

After the validation matrix was GREEN, the State Patch applied:

- 2 obligations created;
- 5 obligations updated;
- 9 false inferences rejected; and
- 8 downstream obligations recorded unchanged.

Resulting graph SHA-256:
`521f626e4af7e75e29d2ba909efb0d48864d5da4785de786acbd746d7559c11f`.

Post-application graph validation, completed-campaign validation,
structured-state parsing, Python compilation, all 6 unit tests,
whitespace checking, the 31-tag candidate equation check, and the
complete 17-file Round-150 strict byte scan all pass.  The accepted
proof draft was updated only after graph mutation.

## 7. Downstream decision

Close only the strict fixed-wrap packet and bounded-$M$ actual-profile
edge.  The next owner is the growing-$M$ large-wrap collar with the
literal signed atom and the compulsory $D=1,L=1$ endpoint.  The
growing-$M$ generic complement remains separate.  The global exponents
do not change.
