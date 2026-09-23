# Final durable-kernel blind consistency review

- Campaign: m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate
- Round: 196
- Role: independent final kernel/blind consistency reviewer
- Starting graph SHA-256:
  f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2
- Durable kernel SHA-256:
  **dd1da266a32701f3e6f727feeec8868247a9aac6f56e36e613f3e721fc8b5ee8**
- Formal candidate SHA-256 recorded by the kernel and independently
  matched:
  **5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380**
- Status: final consistency review evidence only; no shared-state edit
- Numerical theorem evidence: none

## 1. Result

**REPAIR.**  The durable kernel faithfully preserves the repaired
candidate's mathematics: every on-shell sign, primitive-shadow identity,
literal exact-conductor factor, \(\beta/\gamma\) interface, live/dead
wrap statement, \(T=0\) unit-inverse exception, transport displacement,
commutator, fixed/outer power, no-go qualification, and owner/exponent
boundary is correct.  I found no false equation and no target or exponent
overclaim.

The kernel is not yet fully self-contained as a durable statement,
however.  Relative to the hash-matched formal candidate, its opening
statement omits several quantifiers and canonical definitions that are
subsequently used:

1. the candidate's explicit \(X\ge2\), nonempty residual shell
   \(L\ge2\), frequency sign \(\sigma\), and
   \(R_0=\lceil L\rceil\) are absent; in particular, \(R_0\) is used in
   (K196.34) without a local definition;
2. (K196.6) should retain
   \(v_0=[v]_U\in\{1,\ldots,U-1\}\) and \(n\in\mathbb Z\);
3. (K196.9) should retain the candidate's explicit inheritance of the
   accepted definitions of \(A\) and \(\mathcal F_A\);
4. the statement no longer explicitly says that both orientations, both
   surviving signs, all four cross-row blocks, and every literal field
   remain inside one complex aggregate before the final real part; and
5. the candidate's explicit classification of artificial-site
   nonoverlap as outer birth/death, rather than a common-site Fejer
   commutator, has been compressed away.

In addition, both artifacts rely on the inherited meanings of
\(H_B,\varepsilon,\eta\), the dyadic \(Y\)-block, and the projective
\(J\)-band rather than quantifying them locally.  A durable standalone
kernel should either state that inheritance explicitly or spell out the
quantifiers.

These are formal statement/normalization omissions, not defects in the
no-go argument.  Restoring the candidate-level clauses verbatim and
making the remaining inherited quantifiers explicit would make the
durable kernel consistent and self-contained.  Until that repair is
rehashed and replayed, the appropriate verdict is REPAIR rather than
PASS.

## 2. Exact statement and hypotheses

The kernel's intended quantifiers are recoverable unambiguously from the
hash-matched candidate and inherited interface.  They should be stated
directly as follows.

Fix \(X\ge2\), \(L\ge2\), \(B>0\),
\(\sigma\in\{+1,-1\}\), and \(\varepsilon>0\), together with one
nonempty literal middle or lower residual shell and one nonempty dyadic
block \(Y<h\le2Y\).  Put
\[
 H_B=\lfloor(\log(2X))^B\rfloor,\qquad Q=H_B,\qquad
 R_0=\lceil L\rceil,\qquad D_L=\lceil\sqrt L\rceil,\qquad
 M=\min(Y,D_L),
\tag{VFK.1}
\]
and, for the outer ledger, choose a fresh \(0<\eta<\varepsilon\).
Retain exactly
\[
 \kappa<D_L,\qquad M>Q\mathfrak m\kappa
\tag{VFK.2}
\]
inside the accepted Round-192 original-\(t=1\) core with the physical
\(P_2\) mask imposed before every spectral operation.

For each retained exact-conductor/projective packet, quantify
\[
\begin{gathered}
 U=\mathfrak m q>4Q,\quad k=\mathfrak m a,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,\quad (a,q)=1,\\
 U\mid u,\quad g=u/U,\quad (u,v)=1,\quad (U,h)=1,\quad
 \kappa,g,U\ {\rm odd},\\
 j_q(a,v)>T_Q(\mathfrak m,q;Y),\qquad
 J\le j_q(a,v)<2J,
\end{gathered}
\tag{VFK.3}
\]
where \(J\) is one inherited nonempty power-of-two projective band.
Write uniquely
\[
 v_0=[v]_U\in\{1,\ldots,U-1\},\qquad v=v_0+nU,\qquad n\in\mathbb Z,
\tag{VFK.4}
\]
and use the kernel's exact normalization
\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},\qquad
 \rho v-\gamma U=1,\qquad \gamma=\beta+n\rho.
\tag{VFK.5}
\]
The Round-192 Farey selector uses \(\beta\); the Round-191 literal
transport uses \(\gamma\).

Finally, define the canonical anchors by
\[
 S=S_{0,\omega}(h)+Ut,\qquad
 0\le S_{0,\omega}(h)<U,\qquad
 S_{0,\omega}(h)\equiv\epsilon_\omega\bar v_Uh\pmod U.
\tag{VFK.6}
\]
Retain both orientations, both surviving signs, the complete anchor
aggregate, all \(++,+-,-+,--\) blocks, every literal endpoint and
commutator, and one final outer real part.  With these additions, the
kernel statement has exactly the quantifier scope needed by all later
equations.

## 3. Proof or derivation

### 3.1 Equations (K196.1)--(K196.12): packet and literal atom

The physical mask, open region, exact-conductor lift, projective
threshold, and \(T\)-branch formulas are consistent with the current
formal candidate.  In particular, the added canonical-coordinate repair
is exact:
\[
 \rho v_0-\beta U=1,\qquad v=v_0+nU
 \quad\Longrightarrow\quad
 \rho v-(\beta+n\rho)U=1.
\tag{VFK.7}
\]
Thus \(\beta\) correctly belongs to the Farey covector condition and
\(\gamma=\beta+n\rho\) correctly belongs to the literal transport.
The \(T=0\) branch retains all \(|\rho|>0\) rows, including
\(\rho=\pm1\); for \(T\ge1\), (K196.9) forces \(|\rho|>1\).

The literal atom
\[
 \mathfrak m^{-1}c_q(a)(-1)^t
 e(\epsilon_\omega a\bar v_qh/q)B_{\omega,\sigma}(h,t)
\tag{VFK.8}
\]
is normalized correctly.  Equation (K196.10) now includes the required
least-residue range.  The remaining formal defects in this block are the
missing range for \(v_0\), the missing declaration \(n\in\mathbb Z\),
and the unstated inherited definitions used in (K196.9).

### 3.2 Equations (K196.13)--(K196.19): primitive shadow

The two determinant equations give
\[
 \epsilon_\omega\bar v_qh\equiv\bar2_qx\pmod q,\qquad
 x=\kappa U+2S,
\tag{VFK.9}
\]
with the correct plus and minus signs.  Since inherited
\(\kappa,U\) oddness makes \(\kappa U,x\) odd,
\[
 (-1)^S=\chi_4(\kappa U)\chi_4(x).
\]
For
\[
 b_{q,a}\equiv q+4a\bar2_q\pmod{4q},
\]
\(b_{q,a}\) is odd and congruent to \(2a\) modulo each prime dividing
\(q\); therefore \((b_{q,a},4q)=1\).  Its step-two multiplier and scalar
identity are exactly
\[
 z_{q,a}=-e(a/q),\qquad
 (1-z_{q,a})c_q(a)=\frac{2e(a/q)}q.
\tag{VFK.10}
\]
The kernel correctly labels these equations as applying only to the
parity-restored shadow.

### 3.3 Equations (K196.20)--(K196.27): literal normalization and wrap

The affine parity and Fourier normalization give
\[
 (-1)^S=E_U(S_{0,\omega})(-1)^t,\qquad
 c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a),
\tag{VFK.11}
\]
so the repaired on-shell literal factor necessarily contains
\(E_U(S_{0,\omega})\).  Equation (K196.23) is a Fourier convolution,
not a shifted exact-conductor decomposition; its conclusion that full
recombination loses the distinguished \(c_q(a)\) is correct.

With the canonical range already present in (K196.10), the literal
adjacent ratio is
\[
 (-1)^{\mathbf1_{\{S_0=U-1\}}}e(a/q).
\tag{VFK.12}
\]
Because \((U,h)=1\) and
\(S_0\equiv\epsilon_\omega\bar v_Uh\), every live \(S_0\) is a unit.
Hence all live-to-live edges are nonwrap and have ratio \(+e(a/q)\).
The negative wrap \(U-1\mapsto0\) is live-to-dead, and zero extension
retains the unpaired boundary atom.  The near-half relation
\[
 |(1-e(a/q))c_q(a)|
 =\frac2q\cot\!\left(\frac{\pi}{2q}\right)\asymp1
\tag{VFK.13}
\]
is exact, as is the product rule
\[
 \Delta_2(E_UB)
 =E_U\Delta_2B+(E_U-E_U^-)B^-.
\tag{VFK.14}
\]
The kernel consistently treats their capacity consequence as a method
falsifier, not literal lower mass.

### 3.4 Equations (K196.28)--(K196.34): no common operator

The genuine height transport uses the literal quotient \(\gamma\):
\[
 (S,w)\mapsto(S-\epsilon_\omega\rho,\,
 w-\epsilon_\omega\gamma),\qquad
 x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\rho.
\tag{VFK.15}
\]
For \(T\ge1\) this is not a step-two event.  For \(T=0\),
\(\rho=\pm1\) is possible, but the kernel correctly keeps that set as an
unpriced restriction whose complement is neither empty nor estimated.
Even there the literal normalization and physical commutators remain.

At fixed height the affine spacing is \(2U\).  The artificial
\(S\mapsto S+1\) map changes height by \(+v\) in plus and \(-v\) in
minus, moves opposite ordered endpoint factors, and changes the plus-far
or minus-close physical boundary.  Equations (K196.30)--(K196.33) retain
the mask, endpoint, conjugation, arithmetic, carry, birth/death, phase,
cell, crossing, and zero-extension terms.  Equation (K196.34) is
mathematically correct after defining \(R_0\) by (VFK.1):
\[
 |F(h)-F(h\circ\tau)|=\frac{2\kappa gv}{R_0}.
\tag{VFK.16}
\]
For exact bookkeeping, the candidate's sentence should also be restored:
when the two artificial sites do not overlap, the event is an outer
birth/death, not a common-site Fejer commutator.

### 3.5 Equations (K196.35)--(K196.38): fixed and outer powers

The kernel preserves the exact fixed estimate and deficit:
\[
 u\{\kappa+M\}X^\varepsilon,\qquad
 \frac{M}{Q\mathfrak m\kappa}>1.
\tag{VFK.17}
\]
It also restores the exact lift, coefficient mass, and divisor ledger:
\[
 c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),\qquad
 \sum_{\mathfrak m q\mid u}1\le\tau_3(u).
\tag{VFK.18}
\]
The outer inequality (K196.38) is explicitly conditional on first proving
the fixed target.  The lift then cancels the target's \(\mathfrak m\);
it does not cancel (VFK.17).  With \(0<\eta<\varepsilon\) stated, no
positive power is hidden in \(X^\varepsilon\).  There is no power or
exponent overclaim.

## 4. First doubtful or unproved step

The first defect in the durable artifact is formal, at the opening
quantifier block: \(X,L,\sigma,\varepsilon,Y,J,\eta,R_0\) and the
inherited meanings of \(H_B,A,\mathcal F_A\) are not all defined or
quantified.  The first literal undefined symbol not covered even by an
explicit inheritance sentence is \(R_0\) in (K196.34).  The wrap
analysis itself is now fully qualified by the least-residue condition
\(0\le S_0<U\) in (K196.10).

After those textual repairs, no doubtful step remains in the kernel's
route-scoped no-go.  The first genuinely unproved mathematical theorem is
exactly the one the kernel leaves open: a coefficient-sensitive, jointly
signed \(++,+-,-+,--\) estimate for the full literal region (K196.3),
before positive norms and with every literal field retained.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Kernel/candidate hash binding | **PASS.** The kernel records the current candidate SHA-256 \(5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380\), which independently matches the file. |
| Statement quantifiers | **REPAIR.** Add the explicit variables and definitions in Section 2, including \(R_0\), \(0<\eta<\varepsilon\), the dyadic \(Y\)-block, and the projective \(J\)-band. |
| Canonical representatives | **REPAIR.** Restore \(v_0\in\{1,\ldots,U-1\}\) and \(n\in\mathbb Z\).  The kernel now states \(0\le S_{0,\omega}<U\). |
| Farey/literal quotient interface | **PASS.** \(\beta\) occurs in (K196.9), while \(\gamma=\beta+n\rho\) occurs in the literal transport (K196.28). |
| Primitive-shadow algebra | **PASS.** Equations (K196.13)--(K196.19) have the correct signs, primitivity, multiplier, and coefficient normalization. |
| Literal atom and conductor mixing | **PASS.** Equations (K196.11) and (K196.20)--(K196.23) retain \(\mathfrak m^{-1}c_q(a)(-1)^t\) and the nonconstant \(E_U(S_0)\). |
| Live/dead wrap | **PASS.** The least-residue range, live multiplier, deleted wrap, unpaired boundary, and capacity-only qualification are exact. |
| \(T=0\) unit-inverse exception | **PASS.** \(\rho=\pm1\) is retained but is not allowed to replace the full branch without an empty or estimated complement. |
| No common operator | **PASS.** The height, affine, and artificial-\(S\) maps remain distinct across both orientations. |
| Literal commutators | **PASS with one clarity repair.** All classes survive; restore the candidate's explicit nonoverlap-as-birth/death sentence beside (K196.34). |
| Fixed and outer powers | **PASS after exponent quantification.** The fixed deficit, lift, coefficient mass, divisor ledger, conditional outer assembly, and no-positive-power rule are correct. |
| No-go scope | **PASS.** The result is expressly mechanism-specific, capacity-only, and not literal lower mass. |
| Target/exponent quarantine | **PASS.** No new sector, complete \(P_2\), owner, parent, bridge, theorem, or exponent is promoted. |
| Diagnostic-only policy | **PASS.** No computation is used as theorem evidence. |

## 6. Dependencies and exact artifacts used

This review compared:

1. proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md,
   SHA-256
   dd1da266a32701f3e6f727feeec8868247a9aac6f56e36e613f3e721fc8b5ee8;
2. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md,
   SHA-256
   5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380;
3. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reports/blind_on_shell_phase_rederivation.md,
   SHA-256
   a1f0f342c4e19f43cf1e6f216821af46fa51ff6fd134b20f14d22db1fdecd80e;
4. rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/blind_post_unmask_on_shell_carrier_review.md,
   SHA-256
   f4c4045bd512607f7a8617b7e7ce112c90efb91d0eba4fdfe21fe30b51a77949;
5. protocol.md.

The current candidate differs from the earlier candidate hash quoted in
my first post-repair verification because subsequent canonical-coordinate
repairs added the \(j_q/T_Q\) and \(v_0,\beta,\gamma\) interface.  The
durable kernel correctly binds the current candidate hash.  This review
audits the current files directly and does not reuse the obsolete hash as
verification evidence.

No shared state, proof graph, proof draft, validation matrix, synthesis,
source card, web result, or unlisted proof artifact was read or edited.
No external theorem or computation was used.

## 7. Recommended state effect

**Do not treat the durable kernel as final until the statement-level
repairs in Sections 1--2 are applied, rehashed, and independently
replayed.**

The mathematical content should otherwise be retained unchanged.  After
repair, the kernel is suitable only for the route-scoped terminal label
on_shell_carrier_denominator_self_return_no_go and as inconclusive
evidence attached to the already open hard-M1 small-\(t\) owner.  It
must not create a target-safe obligation or promote complete \(P_2\),
\(P_1\), complete original \(t=1\), another original-\(t\) range, the
hard small-\(t\) owner, smooth M1, GAR, an M2 parent, endpoint
uniformity, M9, a bridge, the quarter theorem, or any exponent.
