# Blind post-unmask review of the on-shell carrier

- Campaign: m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate
- Round: 196
- Role: blind post-unmask reviewer
- Starting graph SHA-256:
  f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2
- Status: review evidence only; no shared-state edit
- Numerical theorem evidence: none

## 1. Result

**Overall verdict: REPAIR, with a decisive literal-mechanism FAIL and a
decisive route-scoped no-go PASS.**

The blind report correctly derived the two determinant congruences, the
physical-parity identity
\[
 (-1)^S e(\epsilon_\omega a\bar v_qh/q)
 =\chi_4(\kappa U)\chi_4(x)e(a\bar2_qx/q),
 \qquad x=\kappa U+2S,
\tag{R196.1}
\]
the primitive formal \(4q\)-carrier, its formal multiplier
\(z=-e(a/q)\), and
\[
 (1-z)c_q(a)=\frac{2e(a/q)}q.
\tag{R196.2}
\]
The previously flagged parity and unit hypotheses are fully resolved by
the unmasked accepted kernels: \(\kappa,U\) are odd, hence
\(\kappa U\) and \(x\) are odd, and exact conductor \(q\) has
\((a,q)=1\).

However, the primitive carrier in (R196.1) is **not** the literal
exact-conductor atom.  The accepted parametrization and Fourier
normalization are
\[
 S=S_{0,\omega}(h)+Ut,\qquad
 (-1)^S=E_U(S_{0,\omega}(h))(-1)^t,\qquad
 E_U(s)=(-1)^s,
\tag{R196.3}
\]
and the literal \((q,a)\) atom is
\[
 \boxed{
 \mathfrak m^{-1}c_q(a)(-1)^t
 e(\epsilon_\omega a\bar v_qh/q)B_\omega(h,t).}
\tag{R196.4}
\]
Its repaired on-shell form is therefore
\[
 \boxed{
 \mathfrak m^{-1}c_q(a)E_U(S_{0,\omega})
 \chi_4(\kappa U)\chi_4(x)
 e(a\bar2_qx/q)B_\omega(h,t).}
\tag{R196.5}
\]
The missing \(E_U(S_0)\) is precisely the canonical-anchor parity that
Round 187 Fourier-expanded.  Multiplying a fixed mode by it convolves all
\(U\)-modes and mixes exact conductors, projective bands, and safe/core
packets.  Full recombination returns to the pre-conductor physical
parity and leaves no distinguished \(c_q(a)\) on which to use (R196.2).

On every live-to-live \(x\)-step, the multiplier of (R196.4) is
\(+e(a/q)\), not \(-e(a/q)\).  The sole wrap step with multiplier
\(-e(a/q)\) lands at \(S_0=0\), equivalently \(U\mid h\), and is killed
by the literal mask \((U,h)=1\).  Thus the denominator-cancelling wrap
sector is empty on nonzero literal support.  Moving \(E_U\) through a
hypothetical \(\Delta_2\) instead creates a modulus-two bulk commutator
on every possible live adjacent edge.

There is also no inherited literal \(\Delta_2\) in \(x\).  The actual
Round-191 height difference transports
\[
 x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\varrho_U(v),
\tag{R196.6}
\]
while a fixed-height affine step changes \(x\) by \(2U\).  An artificial
\(S\mapsto S+1\) step changes height by \(+v\) in the plus chart and
\(-v\) in the minus chart and moves opposite endpoint factors.  It is
not the common literal event transport.

Consequently the blind conclusion that no full target or target-safe
strict sector follows is correct, but its first obstruction must be
repaired: the decisive first obstruction is the exact-conductor
normalization (R196.3)--(R196.5), not missing oddness or primitivity.
The proposed mechanism self-returns before any endpoint estimate.  This
is a capacity/operator-class no-go, not literal lower mass and not a
disproof of the desired signed estimate by every possible method.

## 2. Exact statement and hypotheses

Retain exactly the accepted Round-195 open packet
\[
 \kappa<D_L,\qquad
 M:=\min(Y,D_L)>Q\mathfrak m\kappa,\qquad Q=H_B,
\tag{R196.7}
\]
inside the physical \(P_2\) core, where
\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}}
\tag{R196.8}
\]
is imposed before Fourier expansion and height differencing.  The
accepted primitive and exact-conductor hypotheses are
\[
\begin{gathered}
 U=\mathfrak m q>4Q,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,\quad U\mid u,\\
 \kappa,g,U\ {\rm odd},\quad u=gU,\quad (u,v)=1,\quad
 (U,h)=1,\quad (a,q)=1.
\end{gathered}
\tag{R196.9}
\]
In particular \(q\) and \(\mathfrak m\) are odd,
\((v,U)=1\), and the exact lift is
\[
 c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a),\qquad
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\tag{R196.10}
\]

The canonical anchors are
\[
 S_{0,+}=[\bar v_Uh]_U,\qquad
 S_{0,-}=[-\bar v_Uh]_U,\qquad
 S=S_{0,\omega}+Ut.
\tag{R196.11}
\]
Because \((U,h)=(U,v)=1\),
\[
 (S_{0,\omega},U)=1,\qquad S_{0,\omega}\ne0.
\tag{R196.12}
\]

Both orientations, both frequency signs, the \(T=0\) branch, all
simultaneous strict \(T\ge1\) Farey conditions, projective bands, the
complete anchor aggregate, actual endpoint products, residual selectors,
squarefree/coprimality masks, carries, affine births/deaths, physical-mask
commutators, Fejer factors, square-root phases, cells, crossings,
conjugations, and zero extensions remain under one outer real part.

The known fixed-packet estimate and target are
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+M\}X^\varepsilon,
 \qquad
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \stackrel{?}{\ll}Q\mathfrak m\kappa uX^\varepsilon.
\tag{R196.13}
\]

## 3. Proof and post-unmask audit

### 3.1 Hypothesis resolution and formal carrier

In the plus chart, substitution of
\(x=\kappa v+\eta_+=\kappa U+2S\) gives
\[
 2h\equiv vx\pmod q.
\]
In the minus chart,
\(x=\kappa v+\delta_-=\kappa U+2S\) gives
\[
 2h\equiv-vx\pmod q.
\]
Thus, for \(\epsilon_+=1,\epsilon_-=-1\),
\[
 \epsilon_\omega\bar v_qh\equiv\bar2_qx\pmod q.
\tag{R196.14}
\]
The accepted \(\kappa,U\) oddness makes
\(\kappa U\) and \(x=\kappa U+2S\) odd, so
\[
 (-1)^S=\chi_4(\kappa U)\chi_4(x).
\tag{R196.15}
\]
This proves (R196.1) without the conditional caveat in the blind report.

Set
\[
 b_{q,a}\equiv q+4a\bar2_q\pmod{4q}.
\]
It is odd, and modulo every prime dividing \(q\) it is congruent to
\(2a\), a unit.  Hence \((b_{q,a},4q)=1\).  The formal carrier
\(e(b_{q,a}x/(4q))\) is primitive and has step-two ratio
\(-e(a/q)\).  Thus the blind algebraic carrier and (R196.2) pass exactly.

### 3.2 Literal exact-conductor normalization

K185 writes physical parity as
\[
 (-1)^{S_{0,\omega}+t}=(-1)^{S_{0,\omega}}(-1)^t,
\]
and K187 Fourier-expands only
\[
 E_U(S_{0,\omega})=(-1)^{S_{0,\omega}}
 =\sum_{k\bmod U}c_U(k)e(kS_{0,\omega}/U).
\tag{R196.16}
\]
At \(k=\mathfrak m a\), (R196.10) and the anchor congruence give
(R196.4).  Since \(U\) is odd,
\[
 (-1)^t=E_U(S_{0,\omega})(-1)^S,
\]
which proves the repaired formula (R196.5).

The factor \(E_U(S_0)\) is not a harmless amplitude constant.  For one
retained mode,
\[
 E_U(S_0)e(\mathfrak m aS_0/U)
 =\sum_{r\bmod U}c_U(r)
   e((r+\mathfrak m a)S_0/U).
\tag{R196.17}
\]
The shifted modes have varying exact conductors, reduced numerators,
projective bands, and safe/core status.  Therefore (R196.17) is not
internal to the fixed \((q,a)\) packet.  Recombining every mode merely
restores the pre-Fourier parity expansion.  This proves that the formal
primitive carrier is not the literal exact-conductor atom.

### 3.3 Live multiplier, wrap, and parity commutator

Under \(S\mapsto S+1\), let
\[
 S_0'=[S_0+1]_U,\qquad
 c_U^{\rm wrap}(S_0)=\mathbf1_{\{S_0=U-1\}},
\qquad t'=t+c_U^{\rm wrap}(S_0).
\]
The literal ratio is
\[
 \frac{(-1)^{t'}e(a(S+1)/q)}
      {(-1)^te(aS/q)}
 =(-1)^{c_U^{\rm wrap}(S_0)}e(a/q).
\tag{R196.18}
\]
Every live-to-live edge is nonwrap, so its ratio is \(e(a/q)\).  The
wrap ends at \(S_0'=0\), forbidden by (R196.12).  Other nonunit residues
also create coprimality holes; they do not create a cancelling chain.

Accordingly, even if a literal adjacent difference existed, its live
factor would be
\[
 (1-e(a/q))c_q(a)
 =\frac{2e(a/q)(1-e(a/q))}
        {q(1+e(a/q))}.
\tag{R196.19}
\]
For the primitive near-half mode \(a=(q-1)/2\), its modulus is
\[
 \frac2q\cot\!\left(\frac{\pi}{2q}\right)\asymp1,
\tag{R196.20}
\]
not \(O(q^{-1})\).

Equivalently, retaining the formal primitive carrier \(C_{q,a}(x)\) and
moving \(E_U\) into a hypothetical difference yields
\[
\begin{aligned}
 E_U(S_0(x))\Delta_2B(x)
 &=\Delta_2(E_UB)(x)\\
 &\quad+\{E_U(S_0(x-2))-E_U(S_0(x))\}B(x-2).
\end{aligned}
\tag{R196.21}
\]
On each possible live adjacent edge the bracket has modulus \(2\); it
vanishes only at the deleted wrap.  The first term receives (R196.2),
but the second retains \(c_q(a)\) and full positive event capacity.
Thus the two descriptions—wrong live multiplier or bulk parity
commutator—are the same exact self-return.

### 3.4 Actual transports and orientation mismatch

The inherited difference is the K191 height difference.  With signed
inverse \(\varrho v-\gamma U=1\), its transport is
\[
 (S,w)\mapsto
 (S-\epsilon_\omega\varrho,\,
  w-\epsilon_\omega\gamma),
\tag{R196.22}
\]
and therefore (R196.6) holds.  On strict \(T\ge1\) core rows the accepted
Farey conditions keep a genuinely long inverse transport.  At \(T=0\)
the full inherited rho-large branch remains; unit-inverse exceptions, if
present, still face (R196.18)--(R196.21) and all literal commutators.

At fixed height, affine sites have \(S=S_0+Ut\), hence successive sites
have \(x\)-spacing \(2U\).  If instead one forces
\(S\mapsto S+1\) at fixed \(w\), then
\[
 h_+(S+1)-h_+(S)=v,\qquad
 h_-(S+1)-h_-(S)=-v.
\tag{R196.23}
\]
This is not the unit-height transport.  Moreover, \(x=d'/g\) is the far
coordinate in the plus chart, while \(x=d/g\) is the retained close
coordinate in the minus chart.  Thus the same formal \(x\)-step moves
the nonconjugated upper endpoint in plus and the conjugated lower endpoint
in minus.  There is no common inherited event map producing a literal
\(\Delta_2\) across both orientations.

### 3.5 Exact commutator audit

Let \(A_0=\kappa gU\) and \(C_v=\kappa v\).  The ordered endpoint pairs
are
\[
\begin{array}{c|cc}
 & (N_{0,\omega},d_{0,\omega})&(N_{1,\omega},d_{1,\omega})\\ \hline
 +&(A_0(C_v+2w),A_0)&((A_0+2gS)C_v,A_0+2gS)\\
 -&((A_0+2gS)C_v,A_0+2gS)&(A_0(C_v+2w),A_0).
\end{array}
\tag{R196.24}
\]
An adjacent \(S\)-step changes the variable endpoint by
\((\Delta N,\Delta d)=(2gC_v,2g)\) and changes height by (R196.23).
Consequently the following terms all survive unless separately proved
safe:

1. the new bulk \(E_U\)-commutator (R196.21);
2. the physical \(P_2\) commutator: the plus far threshold or minus close
   threshold changes;
3. outer \((U,h)=1\) flips, including the zero extension that deletes the
   only denominator-cancelling wrap;
4. canonical carries, affine common-range terms, births, deaths, and
   multiplicity/collision changes;
5. ordered endpoint-product differences with the lower factor conjugated,
   including squarefree, divisibility, allocation-coprimality, parity,
   residual selected-prime, shell, ratio-cone, selector, profile, floor,
   star, half-weight, hard-sample, real-\(X\) crossing, endpoint-trace,
   cell, and endpoint-zero-extension changes;
6. the Fejer difference.  The accepted safe projection is the unit-height
   Fejer difference; the forced adjacent-\(S\) map changes height by
   \(|v|\asymp L/\kappa\), so its Fejer change is order one and is not that
   safe projection;
7. the actual square-root-phase difference and both frequency signs;
8. outer height/carrier zero extensions and endpoint zero extensions,
   which are distinct, plus the \(O(1)\)-sample birth/death structure
   caused by \(|v|\) being comparable to the whole live height scale;
9. the \(++,+-,-+,--\) orientation Gram blocks, same-site diagonal and
   collision multiplicities, and all conjugations under the one outer
   real part; and
10. the full \(T=0\) branch and every simultaneous strict \(T\ge1\)
    Farey predicate.  Any submask on which one item vanishes has an exact,
    unpriced complement.

This repairs the blind report's abstract product-rule ledger with the
literal K185/K191 endpoint and transport data.  The blind list was
structurally sound, but it omitted the decisive \(E_U\) commutator and
could not distinguish already removed unit-height terminal/Fejer
projections from the new long-step commutators.

### 3.6 Powers and scope

The repaired mechanism does not improve (R196.13).  The \(\kappa u\)
term is target-safe, but the remaining capacity has exact ratio
\[
 \frac{M}{Q\mathfrak m\kappa}>1.
\tag{R196.25}
\]
The fixed exact-conductor lift and mass are
\[
 \mathfrak m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),
\tag{R196.26}
\]
and the accepted outer ledger for a proved fixed target would be
\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{R196.27}
\]
The lift cancels the \(\mathfrak m\) in a proved fixed target; it does
not remove (R196.25).  The parity commutator and every still-open literal
commutator have no accepted estimate below the \(MuX^\varepsilon\)
positive capacity.  This is an available upper-capacity statement, not a
claim that the literal sequence realizes a lower bound.

The denominator-cancelling wrap sector is empty, so it gives no new strict
sector.  The only target-safe \(P_2\) sectors remain those already accepted
in Round 195.  Complete \(P_2\), \(P_1\), all other original-\(t\)
incidences, the remaining hard small-\(t\) owner, smooth M1, GAR, every
M2 parent, endpoint uniformity, M9, both bridges, the quarter theorem, and
all exponents remain separate.

## 4. First doubtful or unproved step

The blind report's “missing oddness and \((a,q)=1\)” is not a post-unmask
proof gap.  Those hypotheses are supplied exactly by K185 and K187.

The first invalid operator-level step is instead the identification of
(R196.1) with the literal exact-conductor atom.  It replaces \((-1)^t\)
by \((-1)^S\) while keeping the same
\(\mathfrak m^{-1}c_q(a)\), thereby deleting \(E_U(S_0)\).  Restoring
that factor either gives the live multiplier \(+e(a/q)\) and the
near-half mass (R196.19)--(R196.20), or produces the bulk commutator
(R196.21) and mixes every exact conductor.

The next invalid prerequisite is a literal event identity
\[
 \mathcal A_{\rm event}(x)=B(x)-B(x-2)
\tag{R196.28}
\]
before positive norms.  The accepted transports have steps
\(2\epsilon_\omega\varrho_U(v)\), \(2U\), or the non-literal
\(S\)-step with height displacement \(\pm v\), never one common
literal step two.

After those repairs, the first genuinely open inequality remains a
coefficient-sensitive joint estimate for the complete literal remainder
on (R196.7), controlling (R196.21), all terms in Section 3.5, and the four
orientation Gram blocks before positive norms with gain (R196.25).

## 5. Decisive review of every blind conclusion

| Blind conclusion | Verdict | Post-unmask finding |
|---|---:|---|
| Both orientation determinant congruences merge to \(\epsilon_\omega\bar v_qh\equiv\bar2_qx\pmod q\). | **PASS** | Equations (R196.14) and the literal charts verify both signs. |
| The physical parity has the \(\chi_4(\kappa U)\chi_4(x)\) form. | **PASS** | K185 supplies \(\kappa,U\) odd, so no even-lattice repair is needed on live support. |
| Oddness was a genuine unresolved hypothesis. | **REPAIR** | It was absent from the blind statement, but is resolved by the inherited literal domain. |
| \((a,q)=1\) was a genuine unresolved hypothesis. | **REPAIR** | K187 exact-conductor decomposition supplies \(a\in\mathbb U(q)\). |
| The parity-restored phase is a primitive additive carrier modulo \(4q\). | **PASS** | The numerator \(q+4a\bar2_q\) is coprime to \(4q\). |
| That primitive \(4q\) carrier is the literal fixed exact-conductor atom. | **FAIL** | The literal atom is (R196.4) and has the extra \(E_U(S_0)\) in its on-shell form (R196.5). |
| The step-two multiplier of the formal primitive carrier is \(-e(a/q)\). | **PASS** | This is exact for the parity-restored shadow. |
| The live literal fixed-mode multiplier is \(-e(a/q)\). | **FAIL** | It is \(+e(a/q)\) on every live-to-live edge; the sole negative wrap lands on the coprimality zero. |
| \((1-z)c_q(a)=2e(a/q)/q\). | **PASS** | It is an exact scalar identity for \(z=-e(a/q)\). |
| The scalar identity cancels the literal exact-conductor denominator. | **FAIL** | The live factor is (R196.19), which is order one on primitive near-half modes. |
| The exact-conductor normalization is just \(c_q(a)\) times the displayed physical-parity phase. | **REPAIR** | The atom carries \(\mathfrak m^{-1}c_q(a)(-1)^t\); the lift and \(E_U(S_0)\) are essential. |
| A genuine full-event \(\Delta_2\) is necessary before using the identity. | **PASS** | The necessity statement was correct and is strengthened by the exact normalization audit. |
| The inherited literal event sequence supplies such a \(\Delta_2\). | **FAIL** | The actual transports have the displacements in (R196.6), \(2U\), or \(\pm v\)-height motion. |
| The blind product-rule list identified the relevant classes of mask, endpoint, arithmetic, carry, phase, Fejer, and zero-extension errors. | **REPAIR** | Its taxonomy was sound, but the decisive bulk \(E_U\) commutator and the exact accepted transports/endpoints had to be added. |
| A manufactured cumulative primitive can self-return the conductor gain. | **PASS** | It remains a valid operator-class falsifier, but it is not the decisive literal obstruction and not literal lower mass. |
| The route yields no full target theorem and no target-safe strict sector with priced complement. | **PASS** | The wrap sector is empty and the exact deficit (R196.25) remains. |
| The first doubtful step is missing oddness/primitivity. | **REPAIR** | Post-unmask, the first invalid step is the deletion of \(E_U(S_0)\) from one fixed exact-conductor atom. |
| The inherited positive bound and unresolved multiplier were restored correctly. | **PASS** | The precise bound is (R196.13), with deficit \(M/(Q\mathfrak m\kappa)\); the unmasked review adds the \(\mathfrak m^{-1}\) lift and outer ledger. |
| Arbitrary-array and phase-conjugated controls prove no physical lower mass. | **PASS** | They delimit coefficient-uniform methods only. |
| Both orientations, both \(T\)-branches, one outer real part, owner scope, and exponent quarantine must remain intact. | **PASS** | No branch, parent, theorem, or exponent can be changed by this no-go. |

## 6. Dependencies and exact artifacts used

This post-unmask review used only:

1. protocol.md;
2. state/active_campaign.yml;
3. strategy/round196_m1_t1_p2_on_shell_anchor_carrier_commutator_strategy.md;
4. proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md;
5. proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md;
6. proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md;
7. proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md;
8. proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md;
9. rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/conductor_round195_report_reconciliation.md;
10. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reports/blind_on_shell_phase_rederivation.md;
11. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reports/literal_on_shell_carrier_commutator_attack.md;
12. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/conductor_round196_operator_normalization_analysis.md; and
13. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reports/carrier_collision_endpoint_hostile_audit.md.

No graph, proof draft, validation matrix, synthesis, source card, web
result, or unlisted prior-round artifact was read for this review.  No
computation was used.

## 7. Recommended state effect

**Record the terminal route label
on_shell_carrier_denominator_self_return_no_go; retain the Round-195 open
packet and make no target promotion.**

The exact on-shell congruence, physical-parity identity, formal primitive
\(4q\)-carrier, and scalar coefficient identity may be retained only with
the explicit label “parity-restored shadow.”  Reject their identification
with one literal exact-conductor atom.  Record (R196.4)--(R196.6),
(R196.18)--(R196.21), the empty live wrap sector, and the literal
commutator ledger as the normalization/support self-return.

Do not create a new target-safe strict sector: the only
denominator-cancelling sector is killed by \((U,h)=1\), and any
anchor-parity or mask restriction has an unpriced complement.  Keep the
fixed-packet target, complete \(P_2\), \(P_1\), all other original-\(t\)
incidences, the hard small-\(t\) owner, smooth M1, GAR, every M2 parent,
endpoint uniformity, M9, both bridges, the quarter theorem, and every
exponent unchanged.  A future advance must be a coefficient-sensitive
joint theorem for the actual literal remainder, not primitive-carrier
completion or full anchor recombination.
