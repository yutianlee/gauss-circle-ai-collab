# Round 191 final-kernel power, literal, and owner-scope review

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Reviewed kernel:
  `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`
- Frozen kernel SHA-256:
  `18b169b96ce9521ad91be748c3562e8974f4f5fcb3d067f76102ae6f54b4df05`
- Review role: independent power ledger, literal-source, fixed/full typing,
  one-outer-operation, and owner-scope seam
- Status: review evidence only; no kernel or shared-state edit

## 1. Result and verdict

**Verdict: PASS.**  The final kernel is a faithful subordinate
reduction of the accepted Round-189 fast packet.  Its strict
signed-inverse sector, outer-terminal projection, and isolated Fejer
projection have the stated fixed-packet bounds; the exact
\(m^{-1}\)-lift and triple-divisor ledger then give the full
\(L^2X^\varepsilon\) safe bound.  Fixed and full packets are typed
separately and related by one linear outer assembly.  Every literal
jump source is retained or assigned exactly once, both orientations
remain in one complex packet, and no inner modulus is inserted into the
open remainder.

The PASS does **not** include (191.C12).  The rho-large remainder stays
open with fixed-band positive cost \(Y\kappa uX^\varepsilon\) against
target \(Qm\kappa uX^\varepsilon\), hence exact unresolved deficit

\[
 \boxed{D_{\rm rem}=Y/(Qm)>1.}
\tag{191.F1}
\]

No parent, bridge, theorem, or exponent is closed by this kernel.

## 2. Exact verified statement, hypotheses, and dependencies

The Round-189 kernel defines the exact fast packet
\(\mathscr F_{Y,Q}^\sigma\) inside its one-real-part decomposition by

\[
 U=mq>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y,
 \quad j_q(a,v)>T_Q,
\tag{191.F2}
\]

with \(U\mid u\), \(g=u/U\), odd \(\kappa,g,U\), \((u,v)=1\),
\((U,h)=1\), \(0<2\kappa gh<R_0\), and all inherited literal fields.
The final kernel retains this exact packet, including its disjoint
power-of-two \(J\)-bands, and adds only the signed least inverse

\[
 \varrho_U(v)v-\gamma_U(v)U=1,qquad
 -(U-1)/2\leq\varrho_U(v)\leq(U-1)/2
\]

and the strict safe predicate

\[
 0<|\varrho_U(v)|\leq
 T_\varrho=min\left\{(U-1)/2,
 \left\lfloor QmU/Y\right\rfloor\right\}.
\tag{191.F3}
\]

The inherited support facts

\[
 u\asymp v\asymp L/\kappa,qquad
 \operatorname{length}(\mathcal V_{\rm lit})\ll u,qquad
 L\ll X^{1/4}
\tag{191.F4}
\]

are displayed before they are used.  The exact direct mathematical
dependencies are therefore correctly listed as

- `M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction`, which
  supplies the exact fast packet, lift, coefficient mass, support, and
  one-real-part interface; and
- `Divisor-bound-elementary`, used for the \(\tau_3\) outer summation.

No additional analytic theorem is imported.  Transport, the signed
inverse bijection, finite Abel summation, interval endpoints, and the
gated algebra are proved inside the kernel.  The metadata's formal
candidate hash agrees with the candidate hash certified by the assigned
post-repair PASS.

## 3. Proof and seam audit

### 3.1 Fixed/full typing and exact complement

Equation (191.C13a) defines a fixed
\((\kappa,u,m,q,a,J,\sigma)\) complex packet and completes both
orientations and every literal \(v,h,t\) label before any modulus.
At this level, (191.C28b)--(191.C28d) define

\[
 \mathscr J_{{\rm inv},{\rm fix}},\quad
 \mathscr J_{{\rm terminal},{\rm fix}},\quad
 \mathscr J_{{\rm Fejer},{\rm fix}},\quad
 \mathscr R_{\rm fix}
\]

as exact linear restrictions or projections and one complex
subtraction.  Equations (191.C32a)--(191.C32b) then apply the inherited
linear outer assembly \(\mathcal O_{Y,Q}^\sigma\) to obtain the full
safe packet and full remainder.  Hence

\[
 \mathscr F_{Y,Q}^\sigma
 =\mathscr J_{Y,Q}^{{\rm safe},\sigma}
  +\mathscr R_{Y,Q}^\sigma
\]

is exact before the final real part.  A fixed packet is never silently
identified with its full outer image.

### 3.2 Strict signed-inverse estimate

The map \(v\bmod U\mapsto\varrho_U(v)\bmod U\) is a bijection on unit
classes.  The strict sector uses at most \(2T_\varrho\) classes, and
each class occurs \(O(u/U+1)=O(u/U)\) times because \(U\mid u\) and
the inherited support has length \(O(u)\).  Thus

\[
 \#\{v:0<|\varrho_U(v)|\leq T_\varrho\}
 \ll \frac{uT_\varrho}{U}
 \ll \frac{Qmu}{Y}.
\tag{191.F5}
\]

The fast \(J\)-predicate only deletes rows.  Returning the Abel form to
the exactly equal original row sum avoids a \(q/J\) loss; \(O(Y)\)
heights and \(O(\kappa)\) sites per row then give

\[
 |\mathscr J_{{\rm inv},{\rm fix}}|
 \ll Y\kappa X^\varepsilon\frac{Qmu}{Y}
 \ll Qm\kappa uX^\varepsilon.
\tag{191.F6}
\]

The floor-zero sector is empty.  At saturation every unit inverse class
is included and the row complement is empty.  Both edge cases preserve
the exact decomposition.

### 3.3 Terminal and Fejer estimates

On rho-large rows, \(K\) is one integer interval.  Its complete
live-side terminal atom \(D_K\) is supported at at most two heights.
The Round-189 projective band count is \(O(uJ/q)\), while
\(|1-z|^{-1}\asymp q/J\).  With \(O(\kappa X^\varepsilon)\) live mass
at a terminal height,

\[
 |\mathscr J_{{\rm terminal},{\rm fix}}|
 \ll (q/J)(uJ/q)\kappa X^\varepsilon
 \ll \kappa uX^\varepsilon.
\tag{191.F7}
\]

The Fejer projection is taken only on persistent \(K,G\) masks and
transported common sites.  Since

\[
 |F(h)-F(h-1)|=2\kappa g/R_0,qquad
 2\kappa gY/R_0<1
\]

on a nonempty live block, its \(O(Y)\) heights and \(O(\kappa)\) sites
per row give

\[
 |\mathscr J_{{\rm Fejer},{\rm fix}}|
 \ll(q/J)(uJ/q)Y\kappa(2\kappa g/R_0)X^\varepsilon
 \ll\kappa uX^\varepsilon.
\tag{191.F8}
\]

Triangle inequality is applied only after these two joint complex
projections and the inverse projection have been defined.  Since
\(Qm\geq1\), (191.F6)--(191.F8) give (191.C9).

### 3.4 The \(m^{-1}\), \(\tau_3\), and \(L^2\) ledger

Round 189 supplies exactly

\[
 c_{mq}(ma)=m^{-1}c_q(a),qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q).
\tag{191.F9}
\]

The \(m^{-1}\) cancels the sole factor \(m\) in the fixed safe bound
before any positive outer sum.  The disjoint \(J\)-bands cost only a
fixed logarithm.  Writing \(u=mqr\), the number of \((m,q)\) pairs is
bounded by

\[
 \sum_{mq\mid u}1\leq\tau_3(u),
\tag{191.F10}
\]

with no fourth divisor variable.  Consequently

\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{191.F11}
\]

Only the fixed polylogarithmic \(Q\), divisor logarithms, and band
logarithm enter the fresh \(X^{\varepsilon-\eta}\) budget.  No positive
power of \(Y\) is absorbed, so the outer ledger has the claimed power.

### 3.5 Literal jump coverage and parity-projector boundary

The jump partition is exact and disjoint:

| Literal source | Exact location |
|---|---|
| dyadic/carrier birth or death | first line of (191.C22d) |
| \((U,h)=1\) flip | persistent-\(K\) branches of (191.C22d) |
| affine positivity birth/death | (191.C23) |
| canonical-anchor carry | first term of (191.C24) |
| Fejer change | second term of (191.C24) |
| both endpoint masks and values, with conjugation and orientation-specific divisors | (191.C24a)--(191.C25) |
| ordered shell/cone/selector/profile/floor/star/half-weight/sample/crossing/trace/endpoint-zero labels | (191.C25a) |
| actual common-cell endpoint value | no-label-change residue of (191.C25a) |
| actual square-root phase | last term of (191.C24) |

Simultaneous \(K,G\) changes are handled on the complete live side;
only persistent masks enter affine transport.  The endpoint zero
extension is explicitly distinct from the outer \(K\)-terminal zero,
and the first-changed-field order prevents double counting.  The
numerical profile difference is retained rather than replaced by its
cell label.

The transport signs are also exact: plus subtracts
\((\varrho,\gamma)\) and minus adds it.  The pre-Fourier parity change
\((-1)^\varrho\) is expressly restricted to the complete anchor.  A
retained mode instead has the carry-dependent factor in (191.C20a),
and recombination of all modes self-returns to the pre-Round-187
packet.  The kernel does not use the full-parity identity as fast-mode
cancellation.

### 3.6 One outer real part and bounded-array quarantine

Both orientations remain in every fixed projection before a modulus,
and the full assembly remains complex until the one final real part.
There is no orientation-wise norm, no inner real part, and no inner
absolute value in \(\mathscr R_{\rm fix}\) or
\(\mathscr R_{Y,Q}^\sigma\).  Absolute estimates are taken only for
already-defined target-safe projections.

For bounded zero-extended arrays, (191.C38) is exact:

\[
 \sup_{|W_r(h)|\leq1}
 \left|\sum_r\frac1{1-z_r}
 \sum_h\Delta^-W_r(h)z_r^h\right|
 =\sum_r|H_r|,
\]

with equality attained by the lawful coboundaries
\(W_r(h)=\overline z_r^{\,h}\mathbf1_{H_r}(h)\).  This includes births,
deaths, and holes and does not treat jump atoms as independent.  The
kernel correctly quarantines it as an operator-class capacity result:
it is neither literal realizability, a literal lower bound, nor a
disproof of (191.C12).  It only rules out obtaining the missing factor
(191.F1) from support, pointwise bounds, separate variation, or another
separable positive norm alone.

## 4. First doubtful or unproved step

The first unproved step is exactly the advertised estimate

\[
 \Re\mathscr R_{Y,Q}^\sigma
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{191.F12}
\]

Already at transported common sites this requires a genuinely signed
theorem coupling the anchor carry, displaced literal endpoint
coefficients, and actual square-root phases while literal masks may
change.  The displacement is \((\varrho,\gamma)\), not a unit step.
Neither exact transport, Abel's identity, terminal isolation, Fejer
isolation, nor bounded-array information supplies the factor
\(Y/(Qm)\).  The kernel states this obstruction and does not disguise it
as a proved variation estimate.

No earlier step assigned to this review remains doubtful.  The archived
finite checks are explicitly diagnostic only and are not used for the
asymptotic theorem, power ledger, literal density, or (191.F12).

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Final-kernel hash | PASS: exact match to `18b169b96ce9521ad91be748c3562e8974f4f5fcb3d067f76102ae6f54b4df05`. |
| Round-189 interface | PASS: the exact \(j_q>T_Q\) fast packet and its one-real-part typing are retained. |
| Direct dependency list | PASS: Round-189 projective reduction plus elementary divisor bound are sufficient and no unproved analytic input is hidden. |
| Fixed/full typing | PASS: (191.C28d) and (191.C32a)--(191.C32b) define distinct exact levels. |
| Strict signed-inverse sector | PASS: row count \(O(Qmu/Y)\), fixed cost \(O(Qm\kappa uX^\varepsilon)\), with empty/saturated cases covered. |
| Terminal estimate | PASS: two boundary heights and the \((q/J)(uJ/q)\) ledger give \(O(\kappa uX^\varepsilon)\). |
| Fejer estimate | PASS: persistent masks and \(2\kappa gY/R_0<1\) give \(O(\kappa uX^\varepsilon)\). |
| Exact \(m^{-1}\) lift | PASS: it cancels before the positive outer sum. |
| Divisor and shell ledger | PASS: \(\tau_3\), fixed logarithms, and \(u\asymp L/\kappa\) give \(L^2X^\varepsilon\); no positive \(Y\)-power is absorbed. |
| Literal jump coverage | PASS: every named outer, affine, parity, endpoint, common-cell, Fejer, and phase source occurs exactly once. |
| One outer operation | PASS: both orientations remain joint and the remainder receives no inner modulus or real part. |
| Bounded-\(W\) control | PASS: lawful coboundary norm identity, fully quarantined from literal realizability and theorem claims. |
| Open remainder | PASS: (191.C12) is explicitly open with exact deficit \(Y/(Qm)\). |
| Owner quarantine | PASS: all \(t\ge2\) small-\(G\), large-\(G\) near-resonant, remaining small-\(t\), hard/smooth M1, GAR, M2, endpoint, M9, bridge, and target owners remain open or conditional. |
| Exponent quarantine | PASS: \(1/3\), \(0.3144831759740614\ldots\), and \(1/4\) remain unchanged. |
| Kernel text hygiene | PASS: no NUL byte, conflict marker, or trailing-whitespace line was found in the frozen kernel. |

## 6. Dependencies and exact artifacts used

Only the four assigned artifacts were used:

1. `protocol.md` — SHA-256
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
2. `proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md`
   — SHA-256
   `31092b28826b9f36ecaedfb5efc5d7625f4caa4da2cf4c37bd48389c6ac6ee58`.
3. `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`
   — SHA-256
   `18b169b96ce9521ad91be748c3562e8974f4f5fcb3d067f76102ae6f54b4df05`.
4. `reviews/literal_jump_parity_projector_owner_scope_postrepair_verification.md`
   — SHA-256
   `56b098e9fc131e0f23a56f7f4e6cf99b0ee0bef7a1efc5213d94e6834f2fb145`.

No proof-state file, formal candidate, sibling report or review,
external source, web result, or numerical computation was used.

## 7. Recommended state effect

**Accept the final kernel as a durable `proved_internal` subordinate
reduction, subject to the conductor's normal graph patch and validation.**
Promote only the strict sector, the terminal/Fejer safe projections,
their \(L^2X^\varepsilon\) outer estimate, and the exact decomposition
(191.C11).  Add the reduction only as inconclusive evidence for the
still-open small-\(t\) owner.

Keep (191.C12) open with exact deficit \(Y/(Qm)\).  Keep every original
\(t\ge2\) small-\(G\) incidence, the large-\(G\) near-resonant
complement, the rest of the small-\(t\) owner, hard and smooth M1, GAR,
every M2 parent, endpoint uniformity, M9, both bridges, and the quarter
target open or conditional at their current scopes.  Do not change the
internal \(1/3\), external \(0.3144831759740614\ldots\), or target
\(1/4\) exponent, and do not promote the bounded-array or archived
finite controls beyond their stated diagnostic/no-go roles.
