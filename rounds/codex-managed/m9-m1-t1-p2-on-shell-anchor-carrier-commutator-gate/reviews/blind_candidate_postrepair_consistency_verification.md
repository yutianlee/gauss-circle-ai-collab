# Blind candidate post-repair consistency verification

- Campaign: m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate
- Round: 196
- Role: independent blind/post-unmask candidate verifier
- Starting graph SHA-256:
  f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2
- Final candidate SHA-256:
  **d996d60d09ed8b6b58cf9cc3e7462215843780f00938840ed425247ec92e9bf9**
- Status: post-repair verification evidence only; no shared-state edit
- Numerical theorem evidence: none

## 1. Result

**PASS.**  The repaired formal candidate is mathematically consistent
with both the statement-only blind derivation and the subsequent
post-unmask normalization review.  I found no remaining sign,
representative, parity, exact-conductor, wrap, displacement, power, or
scope inconsistency.

The candidate makes the required distinction exactly:

1. the phase
   \[
   (-1)^S e(\epsilon_\omega a\bar v_qh/q)
   =\chi_4(\kappa U)\chi_4(x)e(a\bar2_qx/q)
   \tag{V196.1}
   \]
   is a valid **primitive parity-restored shadow** modulo \(4q\), with
   step-two multiplier \(-e(a/q)\);
2. the literal fixed exact-conductor atom is instead
   \[
   \mathfrak m^{-1}c_q(a)(-1)^t
   e(\epsilon_\omega a\bar v_qh/q)B_\omega(h,t),
   \tag{V196.2}
   \]
   whose on-shell factorization contains the indispensable
   \(E_U(S_{0,\omega})=(-1)^{S_{0,\omega}}\);
3. every live-to-live adjacent-\(x\) edge has literal multiplier
   \(+e(a/q)\); the sole negative wrap lands on the coprimality zero and
   remains as a live/dead zero-extension boundary rather than a
   cancelling pair;
4. the \(T=0\) unit-inverse rows are explicitly retained as an unpriced
   exception, not silently excluded or promoted;
5. no accepted event operator gives one common \(\Delta_2\) on the full
   two-orientation core; and
6. the fixed and outer power ledgers preserve the exact unresolved factor
   \(M/(Q\mathfrak m\kappa)>1\).

The formal candidate therefore proves only the stated
normalization/support self-return for this proposed mechanism.  It does
not prove literal lower mass, failure of the desired estimate by another
method, a new strict sector, an owner, a bridge, a theorem, or an exponent.

## 2. Exact statement and hypotheses

The verification concerns the exact open Round-195 packet
\[
 \kappa<D_L,\qquad
 M:=\min(Y,D_L)>Q\mathfrak m\kappa,
\tag{V196.3}
\]
with the physical mask \(P_2\) imposed before Fourier expansion and
height differencing.  The candidate retains
\[
\begin{gathered}
 U=\mathfrak m q>4Q,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,\quad
 J\le |a\bar v_q|_q<2J,\\
 U\mid u,\quad g=u/U,\quad (u,v)=1,\quad (U,h)=1,\quad
 (a,q)=1,\quad \kappa,g,U\ {\rm odd}.
\end{gathered}
\tag{V196.4}
\]
Thus \(q,\mathfrak m,\kappa,U,x=\kappa U+2S\) have the required
parities, \((U,v)=1\), and the canonical anchors
\[
 S=S_{0,\omega}(h)+Ut,\qquad
 S_{0,\omega}\equiv\epsilon_\omega\bar v_Uh\pmod U
\tag{V196.5}
\]
are units modulo \(U\).

The \(T\)-branch statement is exact.  If
\[
 T=\min\!\left\{\frac{U-1}{2},
 \left\lfloor\frac{Q\mathfrak mU}{Y}\right\rfloor\right\},
\tag{V196.6}
\]
then \(T=0\) retains the complete inverse-large remainder
\(|\rho|>0\), including \(\rho=\pm1\).  For \(T\ge1\), the simultaneous
strict Farey conditions imply \(|\rho|>1\).  Both orientations,
frequency signs, all four cross-row blocks, literal masks and endpoints,
and every commutator remain before one final real part.

The candidate's claimed conclusion is only that the carrier-denominator
route does not improve
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+M\}X^\varepsilon
\tag{V196.7}
\]
to the desired
\[
 Q\mathfrak m\kappa uX^\varepsilon
\tag{V196.8}
\]
on (V196.3), using the accepted interfaces alone.

## 3. Proof or derivation

### 3.1 Primitive-shadow algebra

The plus and minus determinant identities reduce modulo \(q\mid U\) to
\[
 2h\equiv vx\pmod q\quad(+),\qquad
 2h\equiv-vx\pmod q\quad(-),
\]
so
\[
 \epsilon_\omega\bar v_qh\equiv\bar2_qx\pmod q.
\tag{V196.9}
\]
Because \(\kappa,U,x\) are odd,
\[
 (-1)^S=\chi_4(\kappa U)\chi_4(x),
\]
which proves (V196.1).  With
\[
 b_{q,a}\equiv q+4a\bar2_q\pmod{4q},
\]
\(b_{q,a}\) is odd and is congruent to \(2a\) modulo every prime
dividing \(q\).  Since \((a,q)=1\),
\((b_{q,a},4q)=1\).  Thus the shadow is primitive modulo \(4q\) and has
ratio
\[
 z_{q,a}=-e(a/q)
\]
under \(x\mapsto x+2\).  The scalar identity
\[
 (1-z_{q,a})c_q(a)=\frac{2e(a/q)}q
\tag{V196.10}
\]
is consequently exact.  This agrees with the blind algebra and is
correctly quarantined from the literal atom in the repaired candidate.

### 3.2 Literal normalization

Since \(U\) is odd, (V196.5) gives
\[
 (-1)^S=E_U(S_{0,\omega})(-1)^t,\qquad
 E_U(s)=(-1)^s.
\tag{V196.11}
\]
The accepted anchor expansion Fourier-expands \(E_U(S_0)\), not
\((-1)^t\).  At \(k=\mathfrak m a\),
\[
 c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a),
\tag{V196.12}
\]
so (V196.2) is the literal atom and its on-shell form is
\[
 \mathfrak m^{-1}c_q(a)E_U(S_{0,\omega})
 \chi_4(\kappa U)\chi_4(x)e(a\bar2_qx/q)B_\omega(h,t).
\tag{V196.13}
\]

Multiplying one retained mode by \(E_U(S_0)\) yields a convolution with
all \(U\)-Fourier modes.  The shifted modes do not inherit the original
exact-conductor coefficient, conductor, projective band, or safe/core
status.  Full mode recombination merely restores physical parity and
removes the distinguished coefficient needed in (V196.10).  The
candidate states this normalization boundary without double-counting the
parity kernel.

### 3.3 Live/dead wrap qualification

Under \(S\mapsto S+1\),
\[
 S_0'=[S_0+1]_U,\qquad
 t'=t+\mathbf1_{\{S_0=U-1\}},
\]
so the literal ratio is
\[
 (-1)^{\mathbf1_{\{S_0=U-1\}}}e(a/q).
\tag{V196.14}
\]
The mask \((U,h)=1\), together with
\(S_0\equiv\epsilon_\omega\bar v_Uh\), makes every live \(S_0\) a unit
and excludes \(S_0=0\).  Hence every live-to-live edge is nonwrap and
has multiplier \(+e(a/q)\).  A wrap from \(U-1\) to \(0\) is
live-to-dead, and the following \(0\)-to-\(1\) edge is dead-to-live.
Zero extension retains both boundary events with their original
coefficient; neither is a live cancelling pair.

For \(a=(q-1)/2\),
\[
 |(1-e(a/q))c_q(a)|
 =\frac2q\cot\!\left(\frac{\pi}{2q}\right)\asymp1,
\tag{V196.15}
\]
so the literal live factor retains the near-half mass.  Alternatively,
\[
 \Delta_2(E_UB)
 =E_U\Delta_2B+(E_U-E_U^-)B^-
\tag{V196.16}
\]
has \(|E_U-E_U^-|=2\) on every possible live-to-live adjacent edge.
At the wrap this bulk commutator is replaced by the just-described
live/dead boundary.  The candidate therefore qualifies the empty live
wrap correctly and drops no boundary atom.

### 3.4 The \(T=0\) unit-inverse exception

The accepted height transport is
\[
 (S,w)\mapsto
 (S-\epsilon_\omega\rho_U(v),\,
  w-\epsilon_\omega\gamma_U(v)),
\qquad
 x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\rho_U(v).
\tag{V196.17}
\]
For \(T\ge1\), \(|\rho_U(v)|>1\), so (V196.17) cannot be a step-two
event.  For \(T=0\), \(\rho_U(v)=\pm1\) is possible and gives a
directional displacement of magnitude two.  The candidate does not
overstate this exception: it identifies those rows as an unpriced proper
restriction of the complete \(T=0\) branch.  Their two signs and two
orientations do not form one common directed operator, and even an
orientation-specific adjacent difference still has the literal
normalization, live-wrap, endpoint, mask, carry, phase, and zero-extension
obstructions in Sections 3.2--3.3.  The exception therefore cannot close
the full branch or define a target-safe sector without its exact
complement.

### 3.5 No common literal operator and commutators

The genuine K191 event has the displacement (V196.17).  At fixed height,
successive affine indices move \(x\) by \(2U\).  The artificial
\(S\mapsto S+1\) map instead changes height by \(+v\) in plus and
\(-v\) in minus.  It moves the plus far upper endpoint but the
conjugated minus close lower endpoint.  Therefore these three maps cannot
be identified as one common \(\Delta_2\).

The candidate correctly retains:

1. the \(E_U\) commutator;
2. the physical \(P_2\) commutator;
3. \((U,h)=1\) live/dead flips;
4. canonical carries and affine common-site, birth, death, and
   multiplicity events;
5. ordered endpoint and conjugation changes, including squarefree,
   divisibility, allocation-coprimality, residual, shell, profile, floor,
   star, half-weight, sample, crossing, cell, trace, and endpoint
   zero-extension fields;
6. the square-root-phase change and both signs;
7. outer and endpoint zero extensions;
8. all four orientation Gram blocks under one outer real part; and
9. the \(T=0\) branch and every strict simultaneous \(T\ge1\) condition.

It also distinguishes the already removed unit-height terminal and Fejer
projections from the artificial adjacent-\(S\) Fejer displacement
\[
 |F(h)-F(h\circ\tau)|=\frac{2\kappa gv}{R_0}.
\tag{V196.18}
\]
When the artificial sites do not overlap, the candidate assigns the term
to an outer birth/death rather than pretending that (V196.18) is a
common-site derivative.  This matches the post-unmask repair.

### 3.6 Fixed and outer powers

The candidate keeps the fixed positive capacity (V196.7) and identifies
the exact remaining deficit
\[
 \frac{M}{Q\mathfrak m\kappa}>1.
\tag{V196.19}
\]
It restores
\[
 c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),\qquad
 \sum_{\mathfrak m q\mid u}1\le\tau_3(u),
\tag{V196.20}
\]
and uses the correct conditional outer ledger
\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll L^2X^\varepsilon.
\tag{V196.21}
\]
The candidate says explicitly that (V196.21) is available only after the
fixed target is proved.  The \(\mathfrak m^{-1}\) lift would then cancel
the fixed target's \(\mathfrak m\); it cannot cancel (V196.19).  No
positive power of \(M,Y,D_L,q,U\), or \(L\) is hidden in
\(X^\varepsilon\).

## 4. First doubtful or unproved step

No doubtful algebraic or normalization step remains inside the repaired
candidate.  Its first unproved inequality is deliberately outside the
candidate theorem: a coefficient-sensitive, jointly signed
\(++,+-,-+,--\) estimate for the complete literal \(P_2\) remainder on
(V196.3), gaining \(M/(Q\mathfrak m\kappa)\) before positive norms while
retaining all endpoint, mask, carry, phase, coprimality, birth/death, and
zero-extension terms.

The assertion that the parity commutator has full **available positive
capacity** is correctly used only as a method boundary.  It is not
asserted as realized literal lower mass.  Accordingly, the candidate
neither proves nor refutes that future coefficient-sensitive inequality.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact primitive-shadow congruence and parity | **PASS.** Both orientation signs, oddness, \((a,q)=1\), primitivity modulo \(4q\), the multiplier, and (V196.10) are exact. |
| Literal exact-conductor normalization | **PASS.** The candidate keeps \(\mathfrak m^{-1}c_q(a)(-1)^t\) and the extra \(E_U(S_0)\); no parity kernel is counted twice. |
| Live/dead wrap qualification | **PASS.** Live-to-live edges have \(+e(a/q)\); the negative wrap is killed by \((U,h)=1\), and both live/dead boundaries remain under zero extension. |
| Near-half falsifier | **PASS.** Equation (V196.15) retains order-one mass and is an exact analytic control. |
| \(T=0\) unit-inverse exception | **PASS.** The candidate allows \(\rho=\pm1\), treats it as an unpriced directional submask, and does not infer the full branch or a strict sector. |
| No common event operator | **PASS.** The height, affine, and artificial-\(S\) transports have distinct displacements and opposite orientation geometry. |
| Literal commutator ledger | **PASS.** All mask, arithmetic, endpoint, carry, birth/death, Fejer, phase, crossing, cell, conjugation, Gram, and zero-extension terms are retained or explicitly identified as already safe projections. |
| Fixed-packet powers | **PASS.** The bound \(u(\kappa+M)X^\varepsilon\), target \(Q\mathfrak m\kappa uX^\varepsilon\), and deficit (V196.19) are exact. |
| Outer powers | **PASS.** The lift, exact-conductor mass, divisor ledger, conditional \(L^2X^\varepsilon\) assembly, and epsilon quarantine are correct. |
| False controls | **PASS.** Consecutive support, cumulative primitives, arbitrary arrays, phase conjugation, deleted masks or \(T\)-branches, wrap-only cuts, and separate orientation norms are method controls only. |
| One outer real part and scope | **PASS.** Complete \(P_2\), all parents, bridges, theorem, and exponents remain open or unchanged at their inherited scopes. |
| Diagnostic-only policy | **PASS.** No computation was used as theorem evidence. |

## 6. Dependencies and exact artifacts used

This consistency verification re-read and compared exactly:

1. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md,
   SHA-256
   d996d60d09ed8b6b58cf9cc3e7462215843780f00938840ed425247ec92e9bf9;
2. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reports/blind_on_shell_phase_rederivation.md,
   SHA-256
   a1f0f342c4e19f43cf1e6f216821af46fa51ff6fd134b20f14d22db1fdecd80e;
3. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/blind_post_unmask_on_shell_carrier_review.md,
   SHA-256
   f4c4045bd512607f7a8617b7e7ce112c90efb91d0eba4fdfe21fe30b51a77949;
4. protocol.md.

No shared proof state, graph, proof draft, validation matrix, synthesis,
source card, web result, or additional round artifact was read or edited
for this verification.  No external theorem or computation was used.

## 7. Recommended state effect

**Accept the repaired formal candidate as internally consistent evidence
for the route-scoped terminal label
on_shell_carrier_denominator_self_return_no_go, subject to the conductor's
remaining lifecycle and State Patch checks.**

Retain the primitive \(4q\) statement only as the explicitly labeled
parity-restored shadow.  Retain the literal normalization, empty
live-to-live cancelling wrap, \(T=0\) unit-inverse exception, absence of a
common \(\Delta_2\), complete commutator ledger, and exact power deficit as
the proved mechanism boundary.  Do not promote a target-safe sector,
complete \(P_2\), \(P_1\), complete original \(t=1\), another original
\(t\) range, the hard small-\(t\) owner, smooth M1, GAR, an M2 parent,
endpoint uniformity, M9, a bridge, the quarter theorem, or any exponent.
