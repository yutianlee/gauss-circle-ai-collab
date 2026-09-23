# Round 196 final-kernel post-repair verification

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Kernel verified:
  `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md`
- Current kernel SHA-256:
  `dd1da266a32701f3e6f727feeec8868247a9aac6f56e36e613f3e721fc8b5ee8`
- Starting graph SHA-256:
  `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Numerical theorem evidence: none

## 1. Result

**Verdict: PASS.** The prior hostile-review PASS remains valid for the
current kernel. The two changes are correct and close the intended
wording seams without changing the operator, packet, power, owner, or
proof-state content:

1. (K196.10) now fixes the canonical representative by

   \[
   0\le S_{0,\omega}(h)<U;
   \tag{196.PR1}
   \]

2. K196.1 now says precisely that the only *formal* wrap carrying the
   shadow multiplier \(z_{q,a}\) is a live/dead zero-extension event and
   supplies no paired denominator cancellation.

The canonical range agrees with the Round-185/187 affine decomposition.
The wrap qualification agrees with K196.4: every live-to-live adjacent
edge is nonwrap, while the forward wrap lands at \(S_0=0\), hence at
\(U\mid h\), and survives only as an unpaired boundary atom. All earlier
\(T\)-branch, event-displacement, endpoint, Fejer, mask, power,
capacity, owner, and exponent checks continue to pass.

## 2. Exact statement and hypotheses

The kernel still retains exactly the accepted Round-192 original-\(t=1\)
core, imposes physical \(P_2\) before Fourier expansion and height
differencing, and restricts to

\[
 \kappa<D_L,\qquad \min(Y,D_L)>Q\mathfrak m\kappa.
\tag{196.PR2}
\]

The exact-conductor packet, K189 fast predicate, signed inverse, and R192
branches are unchanged:

\[
 U=\mathfrak m q>4Q,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,
\tag{196.PR3}
\]

\[
 j_q(a,v)>T_Q(\mathfrak m,q;Y),\qquad
 J\le j_q(a,v)<2J,
\tag{196.PR4}
\]

\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},\qquad
 \rho v-\gamma U=1,\qquad \gamma=\beta+n\rho.
\tag{196.PR5}
\]

At \(T=0\), the complete inherited \(|\rho|>0\) remainder stays. At
\(T\ge1\), every row retains all simultaneous inequalities

\[
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A),\qquad
 |\rho|\ge(A+1)(T+1).
\tag{196.PR6}
\]

The repaired canonical parametrization is now fully explicit:

\[
 S=S_{0,\omega}(h)+Ut,\qquad
 0\le S_{0,\omega}(h)<U,\qquad
 S_{0,\omega}(h)\equiv
 \epsilon_\omega\bar v_Uh\pmod U.
\tag{196.PR7}
\]

Both orientations, literal signs and labels, endpoint conjugations, and
the joint outer aggregate remain inherited unchanged. Separate
orientation norms and every mask, branch, wrap, array, or parity shadow
remain method controls only.

## 3. Proof and verification

### 3.1 Canonical range

Because \((U,v)=1\), the congruence in (196.PR7) has one residue class
modulo \(U\). The new range \(0\le S_0<U\) selects its unique
representative and makes \(t=(S-S_0)/U\) unambiguous. Since \(U\) is
odd,

\[
 (-1)^S=(-1)^{S_0}(-1)^t
 =E_U(S_0)(-1)^t,
\tag{196.PR8}
\]

so the literal atom and the normalization identity (K196.20)--(K196.22)
are unchanged. The repair also fixes the wrap indicator
\(\mathbf1_{\{S_0=U-1\}}\) on a canonical domain, exactly as required.

### 3.2 Formal wrap versus live operator

For the parity-restored shadow, \(x\mapsto x+2\) has multiplier

\[
 z_{q,a}=-e(a/q).
\tag{196.PR9}
\]

For the literal atom, \(S\mapsto S+1\) instead has ratio

\[
 (-1)^{\mathbf1_{\{S_0=U-1\}}}e(a/q).
\tag{196.PR10}
\]

When \(S_0\ne U-1\), this is \(e(a/q)\). At the sole formal wrap
\(S_0=U-1\mapsto0\), it is \(z_{q,a}\), but the new residue
\(S_0=0\) implies \(U\mid h\) and is killed by the coprimality mask.
Thus no live-to-live pair has multiplier \(z_{q,a}\). Zero extension
does not delete the contribution: it leaves an unpaired live/dead
boundary atom with the original exact-conductor coefficient. The new
K196.1 wording is therefore exact and agrees with K196.24--K196.27.

### 3.3 Previously verified seams

No other formula changed. In particular:

- the genuine K191 event still satisfies

  \[
  x_{h-1}^{\rm tr}=x_h-2\epsilon_\omega\rho;
  \tag{196.PR11}
  \]

- \(T\ge1\) forces \(|\rho|>1\), while \(T=0\) allows
  \(\rho=\pm1\) and forbids a unit-inverse submask escape;
- \(x=d'/g\) remains plus-far and \(x=d/g\) minus-close;
- the genuine physical-mask product rule remains distinct from the
  artificial adjacent-\(S\) predecessor;
- the artificial endpoint and height vectors remain

  \[
  (\Delta N,\Delta d)=(2g\kappa v,2g),\qquad
  h_+-h_+\circ\tau=v,\qquad h_--h_-\circ\tau=-v;
  \tag{196.PR12}
  \]

- its Fejer displacement remains

  \[
  |F(h)-F(h\circ\tau)|=\frac{2\kappa gv}{R_0},
  \tag{196.PR13}
  \]

  not the removed unit-height term; and
- every physical-mask, arithmetic, carry, affine birth/death, endpoint,
  conjugation, phase, cell/crossing, and zero-extension commutator
  remains literal.

The fixed estimate is still

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+M\}X^\varepsilon,
\tag{196.PR14}
\]

with unresolved multiplier

\[
 \frac{M}{Q\mathfrak m\kappa}>1.
\tag{196.PR15}
\]

The exact lift and coefficient/divisor sums produce the outer ledger only
after a fixed \(Q\mathfrak m\kappa u\) target is proved. Capacity remains
a method boundary, not literal lower mass, and no positive power is hidden
in \(X^\varepsilon\).

## 4. First doubtful or unproved step

No invalid or doubtful step was introduced by the repairs, and none was
found in the current route-scoped no-go. The canonical range and
live/dead wrap qualification make the relevant statements more precise.

The first genuinely unproved theorem remains the coefficient-sensitive,
jointly signed \(++,+-,-+,--\) estimate for the complete literal
\(P_2\) region, with all masks, endpoints, carries, affine events,
phases, conjugations, and zero extensions retained before positive norms.
The kernel explicitly leaves that theorem open.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `current_kernel_hash` | **PASS.** SHA-256 is `dd1da266a32701f3e6f727feeec8868247a9aac6f56e36e613f3e721fc8b5ee8`. |
| `canonical_S0_range` | **PASS.** (K196.10) now fixes \(0\le S_0<U\). |
| `formal_wrap_qualification` | **PASS.** The \(z_{q,a}\) wrap is live/dead and supplies no paired cancellation. |
| `T_branch_completeness` | **PASS.** Both \(T=0\) and simultaneous \(T\ge1\) cores remain exact. |
| `beta_gamma_interface` | **PASS.** Farey uses \(\beta\); literal transport uses \(\gamma\). |
| `genuine_event_displacement` | **PASS.** The directional law and unit-inverse exception are unchanged. |
| `artificial_endpoint_Fejer_vectors` | **PASS.** Endpoint, height, and Fejer shifts remain exact. |
| `mask_carry_birth_death_phase_zero_extension` | **PASS.** Every commutator family remains literal. |
| `one_outer_aggregate_and_no_submask` | **PASS.** No branch or shadow is promoted separately. |
| `fixed_to_outer_powers` | **PASS.** The exact deficit and conditional outer ledger remain. |
| `capacity_not_lower_mass` | **PASS.** The statement remains method-scoped. |
| `owner_boundary` | **PASS.** Only inconclusive evidence reaches the existing open owner. |
| `exponent_quarantine` | **PASS.** No downstream theorem or exponent changes. |
| `diagnostic_only` | **PASS.** No computation was used. |

## 6. Dependencies and exact artifacts used

Only the current kernel and its directly relevant verification artifacts
were used:

1. `protocol.md` —
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
2. `state/proof_obligations.yml` —
   `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`;
3. `state/active_campaign.yml` —
   `8aa8f0dea94adc77f6e3e4dbc8a2b43c3a6749aefe7f95c37be0c3867e85dfab`;
4. `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md` —
   `dd1da266a32701f3e6f727feeec8868247a9aac6f56e36e613f3e721fc8b5ee8`;
5. `candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md` —
   `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`;
6. `reviews/final_kernel_power_owner_scope_review.md` —
   `fa5c259dfa859620b585eeb0245470e5da8d43a001e2b7b283b54a3650fd8223`;
7. `reviews/commutator_power_owner_scope_final_verification.md` —
   `273afb36679a4b1f24f2dbc7708660079ef474c19130618a6fd5f3d892054cfa`.

Items 5--7 are relative to the Round-196 campaign directory. No web
source, external result, unlisted sibling artifact, or computation was
used.

## 7. Recommended state effect

**Retain the prior PASS.** The current kernel is ready for conductor graph
validation as the route-scoped node
`on_shell_carrier_denominator_self_return_no_go`.

Its admissible effect is unchanged: record the carrier-normalization,
live-wrap, parity-commutator, and no-common-\(\Delta_2\) obstruction;
keep complete \(P_2\) open; attach only inconclusive evidence to the
existing hard-M1 small-\(t\) owner; and leave \(P_1\), every original
\(t\) aggregate, all parents, GAR, endpoint uniformity, M9, both
bridges, the quarter theorem, and every exponent unchanged.

No shared-state edit is made by this verification.
