# Round 196 final-kernel statement-scope verification

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Kernel verified:
  `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md`
- Current kernel SHA-256:
  `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb`
- Starting graph SHA-256:
  `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Numerical theorem evidence: none

## 1. Result

**Verdict: PASS.** The current durable kernel is statement-self-contained
at the required interfaces and preserves the prior PASS.

The new statement correctly quantifies \(X,B,\varepsilon,L,\sigma,Y,J\),
chooses a fresh outer-ledger exponent \(0<\eta<\varepsilon\), defines
\(H_B,Q,R_0,D_L,M\), fixes the dyadic height block and projective band,
and explicitly retains the one-outer-real-part assembly and no-submask
rule. The canonical \(S_0\) range, signed inverse,
\(\beta\)/\(\gamma\) division, and both \(T\)-branches remain exact.

K196.5 now states the missing-support alternative explicitly: if the two
artificial adjacent-\(S\) sites do not overlap, the event is an outer
birth or death, not a common-site Fejer commutator. This agrees with the
zero-extended operator and does not change the endpoint or Fejer vectors.

The fixed-to-outer power ledger, capacity-versus-lower-mass boundary,
owner restriction, and exponent quarantine remain correct. The kernel
continues to prove only a route-scoped no-go for the proposed
carrier-denominator mechanism.

## 2. Exact statement and hypotheses

K196.0 now fixes

\[
 X\ge2,\quad B>0,\quad \varepsilon>0,\quad L\ge2,\quad
 \sigma\in\{\pm1\},\quad Y<h\le2Y,
\tag{196.SF1}
\]

one nonempty power-of-two \(J\)-band, and a fresh
\(0<\eta<\varepsilon\), with

\[
 H_B=\lfloor(\log(2X))^B\rfloor,\quad Q=H_B,\quad
 R_0=\lceil L\rceil,\quad D_L=\lceil\sqrt L\rceil,\quad
 M=\min(Y,D_L).
\tag{196.SF2}
\]

The physical \(P_2\) mask is imposed before Fourier expansion and height
differencing, and the exact open packet is

\[
 \kappa<D_L,\qquad M>Q\mathfrak m\kappa.
\tag{196.SF3}
\]

The exact-conductor and K189 fast conditions remain

\[
 U=\mathfrak m q>4Q,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,
\tag{196.SF4}
\]

\[
 j_q(a,v)>T_Q(\mathfrak m,q;Y),\qquad
 J\le j_q(a,v)<2J.
\tag{196.SF5}
\]

The canonical quotient and literal transport data are

\[
 v_0=[v]_U\in\{1,\ldots,U-1\},\quad v=v_0+nU,\quad n\in\mathbb Z,
\tag{196.SF6}
\]

\[
 \rho v_0-\beta U=1,\quad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},\quad
 \rho v-\gamma U=1,\quad \gamma=\beta+n\rho.
\tag{196.SF7}
\]

For \(T=0\), the whole inherited \(|\rho|>0\) remainder remains. For
\(T\ge1\), the kernel retains simultaneously

\[
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A),\qquad
 |\rho|\ge(A+1)(T+1),
\tag{196.SF8}
\]

with \(A,\mathcal F_A\) explicitly tied to their accepted R192
definitions.

Finally, K196.10 states that both orientations, surviving frequency
signs, the full anchor aggregate, every endpoint label and conjugation,
and all four cross-row blocks remain in one complex aggregate before the
final real part. No \(T\)-branch, unit-inverse, wrap, parity, mask, or
orientation submask may replace the core unless its exact complement is
empty or estimated.

## 3. Proof and verification

### 3.1 Quantified normalization and branch scope

The added quantifiers introduce no change of operator. The definitions
of \(Q,R_0,D_L,M\) agree with K189--K195 and make the later Fejer and
outer-ledger formulas self-contained. The fresh
\(0<\eta<\varepsilon\) is used only in the conditional outer sum; no
positive geometric power is transferred into it.

The range

\[
 0\le S_{0,\omega}(h)<U
\tag{196.SF9}
\]

continues to select the unique canonical anchor. The signed inverse is
unique, Farey uses \(\beta\), literal K191 transport uses \(\gamma\),
and the genuine displacement remains

\[
 x_{h-1}^{\rm tr}=x_h-2\epsilon_\omega\rho.
\tag{196.SF10}
\]

At \(T\ge1\), \(|\rho|>1\). At \(T=0\), unit inverses are allowed but
cannot replace the complete branch without a complement estimate. Thus
the quantified statement does not narrow either branch.

### 3.2 Artificial nonoverlap and commutator ledger

For the artificial predecessor \(\tau:(S,w)\mapsto(S-1,w)\), the
endpoint and height vectors remain

\[
 (\Delta N,\Delta d)=(2g\kappa v,2g),\qquad
 h_+-h_+\circ\tau=v,\qquad h_--h_-\circ\tau=-v.
\tag{196.SF11}
\]

The raw Fejer displacement remains

\[
 |F(h)-F(h\circ\tau)|=\frac{2\kappa gv}{R_0},
\tag{196.SF12}
\]

not the removed unit-height difference \(2\kappa g/R_0\).

The added sentence correctly splits the zero-extended cases:

- if both artificial sites lie in the common live support, (196.SF12)
  is the common-site Fejer commutator alongside the endpoint, mask,
  carry, affine, and phase differences;
- if they do not overlap, there is no common-site Fejer pair, and the
  surviving site is an outer birth or death.

This is exactly the K191/K195 support logic. It neither drops a boundary
atom nor counts nonoverlap twice. The plus-upper/minus-conjugated-lower
endpoint order, physical \(P_2\) commutator, arithmetic masks, carry,
affine births/deaths, phase, cells/crossings, and endpoint zero extension
remain unchanged.

### 3.3 Powers and method boundary

The fixed estimate remains

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+M\}X^\varepsilon,
\tag{196.SF13}
\]

and the unresolved term still has exact ratio

\[
 \frac{M}{Q\mathfrak m\kappa}>1.
\tag{196.SF14}
\]

The exact \(\mathfrak m^{-1}\) lift, coefficient \(\ell^1\) mass, and
divisor count yield

\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll L^2X^\varepsilon
\tag{196.SF15}
\]

only after the fixed \(Q\mathfrak m\kappa uX^\varepsilon\) target is
proved. The lift then cancels \(\mathfrak m\) in that proved target; it
does not cancel (196.SF14). No positive power of
\(M,Y,D_L,q,U,L\) is hidden in \(X^\varepsilon\).

The near-half and array controls remain capacity statements only. They do
not realize literal endpoint coefficients or prove lower mass.

## 4. First doubtful or unproved step

No invalid or doubtful step was found in the current kernel. The
statement-only repairs make the quantifiers, joint assembly, submask
rule, and nonoverlap birth/death event explicit without altering any
proved identity or conditional power ledger.

The first open theorem remains the complete coefficient-sensitive,
jointly signed \(++,+-,-+,--\) estimate on (K196.3), with every literal
endpoint, mask, carry, affine event, phase, conjugation, and zero
extension retained before positive norms. The kernel expressly does not
claim it.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `current_kernel_hash` | **PASS.** SHA-256 is `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb`. |
| `quantified_X_B_epsilon_L_scope` | **PASS.** K196.0 fixes every global parameter used later. |
| `dyadic_Y_and_projective_J_scope` | **PASS.** Both nonempty blocks are explicit. |
| `fresh_outer_eta` | **PASS.** \(0<\eta<\varepsilon\) is used only in the conditional ledger. |
| `R0_DL_M_definitions` | **PASS.** Fejer, mask, and capacity scales are self-contained. |
| `T_branch_completeness` | **PASS.** \(T=0\) and simultaneous \(T\ge1\) scopes remain exact. |
| `one_outer_aggregate` | **PASS.** Orientations, signs, labels, conjugations, and cross-row blocks remain joint. |
| `no_submask_rule` | **PASS.** Every listed selector requires an empty or estimated complement. |
| `canonical_anchor_and_wrap` | **PASS.** \(0\le S_0<U\) and the live/dead formal wrap remain exact. |
| `genuine_event_displacement` | **PASS.** The directional K191 law and unit-inverse exception remain. |
| `artificial_nonoverlap_birth_death` | **PASS.** Nonoverlap is routed to an outer birth/death, not a Fejer pair. |
| `endpoint_mask_carry_phase_zero_extension` | **PASS.** All product-rule event families remain literal. |
| `fixed_to_outer_powers` | **PASS.** The exact multiplier and conditional outer sum are unchanged. |
| `capacity_not_lower_mass` | **PASS.** The no-go remains method-scoped. |
| `owner_boundary` | **PASS.** Only inconclusive evidence can reach the open hard-M1 small-\(t\) owner. |
| `exponent_quarantine` | **PASS.** No parent, bridge, theorem, or exponent is promoted. |
| `diagnostic_only` | **PASS.** No computation was used. |

## 6. Dependencies and exact artifacts used

Only the current kernel and its prior verification chain were used:

1. `protocol.md` —
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
2. `state/proof_obligations.yml` —
   `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`;
3. `state/active_campaign.yml` —
   `8aa8f0dea94adc77f6e3e4dbc8a2b43c3a6749aefe7f95c37be0c3867e85dfab`;
4. `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md` —
   `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb`;
5. `reviews/final_kernel_power_owner_scope_review.md` —
   `fa5c259dfa859620b585eeb0245470e5da8d43a001e2b7b283b54a3650fd8223`;
6. `reviews/final_kernel_power_owner_scope_postrepair_verification.md` —
   `d5855e876a3aa8fa4becb0b0589da9eb960fd7da2273837d82879a8217ea7a66`;
7. `reviews/commutator_power_owner_scope_final_verification.md` —
   `273afb36679a4b1f24f2dbc7708660079ef474c19130618a6fd5f3d892054cfa`.

Items 5--7 are relative to the Round-196 campaign directory. No web
source, external result, unlisted sibling artifact, or computation was
used.

## 7. Recommended state effect

**Retain PASS at the current kernel hash.** The durable kernel is
statement-self-contained and ready for conductor graph validation as
`on_shell_carrier_denominator_self_return_no_go`.

Its admissible effect is unchanged: record only the route-scoped
normalization/live-wrap/commutator/no-common-\(\Delta_2\) obstruction;
keep complete \(P_2\) open; attach inconclusive evidence only to the
existing hard-M1 small-\(t\) owner; and leave \(P_1\), all original
\(t\) aggregates, every parent, GAR, endpoint uniformity, M9, both
bridges, the quarter theorem, and every exponent unchanged.

No shared-state edit is made by this verification.
