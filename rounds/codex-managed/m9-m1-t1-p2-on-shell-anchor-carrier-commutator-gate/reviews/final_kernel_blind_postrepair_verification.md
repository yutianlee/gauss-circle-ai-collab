# Final durable-kernel blind post-repair verification

- Campaign: m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate
- Round: 196
- Role: independent blind/post-unmask post-repair verifier
- Starting graph SHA-256:
  f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2
- Current durable-kernel SHA-256:
  **51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb**
- Bound formal-candidate SHA-256:
  **5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380**
- Status: final post-repair verification evidence only; no shared-state edit
- Numerical theorem evidence: none

## 1. Result

**PASS.**  The current durable kernel repairs every statement-level
defect identified in my preceding blind consistency review, while leaving
the verified mathematics and its narrow proof-state boundary intact.
Specifically, it now states the global and local quantifiers, defines
\(H_B,Q,R_0,D_L,M\), restores the canonical \(v_0,n,S_0\) ranges,
declares the inherited \(A,\mathcal F_A\) interface, preserves both
orientations, both surviving signs, all four cross-row blocks, every
literal field, and one final real part, and classifies artificial-site
nonoverlap as outer birth/death.

I found no false equation, missing hypothesis, illicit restriction,
target promotion, owner promotion, or exponent overclaim.  The kernel
proves exactly the route-scoped normalization/support no-go it claims and
nothing stronger.

## 2. Exact statement and hypotheses

The repaired statement explicitly fixes
\[
 X\ge2,\quad B>0,\quad \varepsilon>0,\quad L\ge2,\quad
 \sigma\in\{+1,-1\},\quad Y<h\le2Y,\quad J,\quad
 0<\eta<\varepsilon,
\tag{VPR.1}
\]
with a nonempty literal middle or lower residual shell, a nonempty
dyadic height block, and a nonempty inherited power-of-two projective
band.  It defines
\[
 H_B=\lfloor(\log(2X))^B\rfloor,\quad Q=H_B,\quad
 R_0=\lceil L\rceil,\quad D_L=\lceil\sqrt L\rceil,\quad
 M=\min(Y,D_L),
\tag{VPR.2}
\]
and imposes the physical \(P_2\) mask before Fourier expansion and
height differencing.  The operative region remains exactly the strict
open region
\[
 \kappa<D_L,\qquad M>Q\mathfrak m\kappa.
\tag{VPR.3}
\]

For every retained exact-conductor packet the kernel includes
\[
\begin{gathered}
 U=\mathfrak m q>4Q,\quad k=\mathfrak m a,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,\quad (a,q)=1,\\
 U\mid u,\quad g=u/U,\quad (u,v)=1,\quad (U,h)=1,\quad
 \kappa,g,U\ \text{odd},\\
 j_q(a,v)>T_Q(\mathfrak m,q;Y),\qquad J\le j_q(a,v)<2J.
\end{gathered}
\tag{VPR.4}
\]
The canonical coordinates and two quotients are now fully quantified:
\[
 v_0=[v]_U\in\{1,\ldots,U-1\},\quad v=v_0+nU,\quad n\in\mathbb Z,
\tag{VPR.5}
\]
\[
 \rho v_0-\beta U=1,\quad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},\quad
 \rho v-\gamma U=1,\quad \gamma=\beta+n\rho.
\tag{VPR.6}
\]
The Farey selector uses \(\beta\), the literal transport uses
\(\gamma\), and \(A,\mathcal F_A\) explicitly inherit their accepted
Round-192 definitions.  At \(T=0\), all inherited \(|\rho|>0\) rows
remain, including \(\rho=\pm1\); for \(T\ge1\), (K196.9) gives
\(|\rho|>1\).

Finally,
\[
 S=S_{0,\omega}(h)+Ut,\qquad 0\le S_{0,\omega}(h)<U,\qquad
 S_{0,\omega}(h)\equiv\epsilon_\omega\bar v_Uh\pmod U
\tag{VPR.7}
\]
is a genuine least-residue convention.  The explicit complete-aggregate
clause prevents any one-orientation, one-sign, one-block, wrap-only,
unit-inverse, or mask subpiece from becoming the claimant without an
empty or estimated complement.  The fixed \(\sigma\) notation labels a
fixed component, while the claimant aggregate still retains both
surviving signs before its final real part.

## 3. Proof or derivation

### 3.1 Primitive shadow

The plus and minus determinant identities (K196.13)--(K196.14) both
reduce to
\[
 \epsilon_\omega\bar v_qh\equiv\bar2_qx\pmod q,
 \qquad x=\kappa U+2S.
\tag{VPR.8}
\]
Since inherited oddness makes \(\kappa U\) and \(x\) odd,
\[
 (-1)^S=\chi_4(\kappa U)\chi_4(x),
\tag{VPR.9}
\]
so (K196.17) has the correct orientation-independent phase.  For
\[
 b_{q,a}\equiv q+4a\bar2_q\pmod{4q},
\]
the numerator is odd and is congruent to \(2a\) at every prime dividing
the odd modulus \(q\), hence \((b_{q,a},4q)=1\).  The exact step-two
shadow multiplier and scalar identity are
\[
 z_{q,a}=-e(a/q),\qquad
 (1-z_{q,a})c_q(a)=\frac{2e(a/q)}q.
\tag{VPR.10}
\]
The kernel correctly confines these formulas to the parity-restored
shadow.

### 3.2 Literal normalization and live/dead wrap

The literal atom retains the exact conductor coefficient and affine
parity:
\[
 \mathfrak m^{-1}c_q(a)(-1)^t
 e(\epsilon_\omega a\bar v_qh/q)B_{\omega,\sigma}(h,t),
\tag{VPR.11}
\]
\[
 (-1)^S=E_U(S_{0,\omega})(-1)^t,\qquad
 c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a).
\tag{VPR.12}
\]
Thus the repaired on-shell factorization (K196.22), including the
nonconstant \(E_U(S_0)\), is exact.  Equation (K196.23) is correctly a
frequency convolution: recombination mixes conductors, reduced
numerators, projective bands, and packet classes, so the shadow
multiplier cannot be assigned to one frozen literal atom.

Under the artificial adjacent \(S\)-step, the literal ratio is
\[
 (-1)^{\mathbf1_{\{S_0=U-1\}}}e(a/q).
\tag{VPR.13}
\]
Live support has \((S_0,U)=1\), hence every live-to-live edge is
nonwrap and has multiplier \(+e(a/q)\).  The only negative wrap lands
at \(S_0=0\), equivalently \(U\mid h\), and is therefore live-to-dead;
zero extension leaves an unpaired boundary atom.  For
\(a=(q-1)/2\),
\[
 |(1-e(a/q))c_q(a)|
 =\frac2q\cot\!\left(\frac{\pi}{2q}\right)\asymp1,
\tag{VPR.14}
\]
and the exact product rule
\[
 \Delta_2(E_UB)=E_U\Delta_2B+(E_U-E_U^-)B^-
\tag{VPR.15}
\]
produces a modulus-two parity commutator on every live-to-live nonwrap
edge.  The kernel correctly calls this a capacity/method obstruction,
not literal lower mass.

### 3.3 Transport, commutators, and absence of a common operator

The genuine height event uses the literal quotient \(\gamma\):
\[
 (S,w)\mapsto(S-\epsilon_\omega\rho,
 w-\epsilon_\omega\gamma),\qquad
 x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\rho.
\tag{VPR.16}
\]
For \(T\ge1\) this is not a step-two displacement.  At \(T=0\), the
possible rows \(\rho=\pm1\) cannot replace the branch without controlling
their exact complement, and every physical commutator remains.  The
fixed-height affine displacement is \(2U\); moreover \(x\) is plus-far
but minus-close, so the literal minus-far step fixes it.  These operators
therefore do not furnish a common \(\Delta_2\) on the complete aggregate.

The physical product rule (K196.30) retains the mask commutator.  The
artificial \(S\)-predecessor has the stated opposite-orientation endpoint
geometry, displacement \((2gC_v,2g)\), and height shifts \(+v,-v\).
Consequently all divisor, arithmetic-mask, carry, affine-range, endpoint,
square-root-phase, cell, crossing, coprimality, and zero-extension terms
remain.  Its Fejer change is exactly
\[
 |F(h)-F(h\circ\tau)|=\frac{2\kappa gv}{R_0},
\tag{VPR.17}
\]
not the unit-height difference.  The repaired sentence now correctly
classifies nonoverlap as an outer birth or death, not a common-site Fejer
commutator.

### 3.4 Fixed and outer powers

The unchanged fixed capacity and exact target deficit are
\[
 u\{\kappa+M\}X^\varepsilon,\qquad
 \frac{M}{Q\mathfrak m\kappa}>1.
\tag{VPR.18}
\]
The lift, coefficient mass, and divisor ledger in (K196.37) are exact.
Equation (K196.38) is expressly conditional on first proving the fixed
target; the lift then cancels the target's \(\mathfrak m\), not the
deficit (VPR.18).  Because the kernel quantifies a fresh
\(0<\eta<\varepsilon\) and expressly forbids hiding positive powers of
\(M,Y,D_L,q,U,L\) in \(X^\varepsilon\), its power ledger makes no
target or exponent overclaim.

## 4. First doubtful or unproved step

There is no doubtful or unproved step inside the claimed route-scoped
no-go.  The first genuinely unproved mathematical step is exactly the
one the kernel leaves open: a coefficient-sensitive, jointly signed
\(++,+-,-+,--\) cross-row estimate for the complete literal region
(K196.3), before positive norms and with every literal field retained.
Nothing in the primitive-shadow, wrap, or commutator analysis supplies
that estimate.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Current kernel hash | **PASS.** Independently computed SHA-256 is `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb`. |
| Candidate binding | **PASS.** The recorded candidate hash `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380` matches the candidate file. |
| Global quantifiers | **PASS.** \(X,B,\varepsilon,L,\sigma,Y,J,\eta,H_B,Q,R_0,D_L,M\) are stated or defined. |
| Canonical coordinates | **PASS.** The \(v_0,n,S_0\) ranges, \(\beta/\gamma\) split, and \(A,\mathcal F_A\) inheritance are explicit. |
| Complete claimant scope | **PASS.** Both orientations, both signs, all four blocks, every literal field, exact complements, and one final real part are retained. |
| Primitive-shadow algebra | **PASS.** Congruence, parity, primitive \(4q\) carrier, multiplier, and scalar identity are exact. |
| Literal normalization | **PASS.** The \(\mathfrak m^{-1}c_q(a)(-1)^t\) atom and nonconstant \(E_U(S_0)\) are retained. |
| Live/dead wrap | **PASS.** Live ratio, dead wrap, boundary atom, and near-half mass are correctly distinguished. |
| \(T=0\) unit-inverse exception | **PASS.** \(\rho=\pm1\) remains possible but cannot replace the complete branch. |
| No common operator | **PASS.** Height, fixed-height affine, minus-far, and artificial-\(S\) events do not give one complete-core \(\Delta_2\). |
| Literal commutators | **PASS.** All physical terms remain, and nonoverlap is expressly outer birth/death. |
| Fixed/outer powers | **PASS.** The deficit, conditional outer ledger, lift, logarithmic mass, divisor count, and exponent quarantine are exact. |
| No-go scope | **PASS.** The conclusion is mechanism-specific and capacity-only, not a literal lower bound. |
| Target/owner/exponent boundary | **PASS.** No sector, owner, parent, bridge, theorem, or exponent is promoted. |

## 6. Dependencies and exact artifacts used

This verification used only:

1. `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md`,
   SHA-256
   `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb`;
2. `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md`,
   SHA-256
   `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`;
3. `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reports/blind_on_shell_phase_rederivation.md`,
   SHA-256
   `a1f0f342c4e19f43cf1e6f216821af46fa51ff6fd134b20f14d22db1fdecd80e`;
4. `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/blind_post_unmask_on_shell_carrier_review.md`,
   SHA-256
   `f4c4045bd512607f7a8617b7e7ce112c90efb91d0eba4fdfe21fe30b51a77949`;
5. `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/final_kernel_blind_consistency_review.md`,
   SHA-256
   `1f6dd336b77ba610ccb52e59731efd6179fa4aab70ac3c66c423a3d3dcf5d929`;
6. `protocol.md`.

No shared state, proof graph, proof draft, validation matrix, synthesis,
source card, web result, or unlisted proof artifact was read or edited.
No computation was used as theorem evidence.

## 7. Recommended state effect

**PASS; promote/retain only the durable route-scoped no-go.**  The
kernel may be treated as verified evidence for
`on_shell_carrier_denominator_self_return_no_go`, subject to the
conductor's ordinary mechanical State Patch and graph validation.  It
remains only inconclusive evidence for the open hard-M1 small-\(t\)
owner.  It must not create a target-safe obligation or promote complete
\(P_2\), \(P_1\), complete original \(t=1\), any other original-\(t\)
range, the hard small-\(t\) owner, smooth M1, GAR, an M2 parent, endpoint
uniformity, M9, either bridge, the quarter theorem, or any exponent.
