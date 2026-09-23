# Round 192 final-kernel literal, core, and owner-scope seam review

- Campaign: m9-m1-t1-rho-large-bezout-edge-gate
- Round: 192
- Review role: independent final-kernel literal/core/owner seam
- Starting graph SHA-256:
  75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13
- Reviewed kernel SHA-256:
  301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325
- Locked candidate SHA-256:
  9562954b65ac8c0f465b535e39d1c30724339098ef5a0d520507cd0983996cd5
- Numerical theorem evidence: none

## 1. Result and verdict

**Verdict: PASS.** The current repaired kernel faithfully preserves the
locked candidate's reduction at every audited seam: one complex literal
aggregate before the final real part, the canonical \(\beta\) versus
literal \(\gamma\) distinction, the long-step phase and affine-carry
identities, both endpoint-number and endpoint-divisor translation tables,
the exact union/core ownership with no double count, the \(T=0\) convention
and \(T\geq1\) floor, and the subordinate owner and exponent boundary.

Current (192.K33) now matches the locked hypothesis precision: its height
sequence is finite or absolutely summable and extended by zero to all
integer heights, and the displayed normalization is asserted only when
\(z^\Delta\ne1\). This edit changes no literal object, estimate, power,
dependency, core, or owner. No remaining defect was found, so the kernel
merits PASS at exactly its stated strict Farey-union/core-reduction scope.

## 2. Exact reviewed statement and hypotheses

The kernel inherits the exact accepted Round-191 hard-M1 original-\(t=1\)
rho-large remainder, including

\[
 U=mq>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y,\quad U\mid u,
\]

the oddness and coprimality hypotheses, literal support and shell
conditions, the exact fast predicate

\[
 j_q(a,v)=|a\bar v_q|_q>
 \min\left\{\frac{q-1}{2},
      \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\},
 \qquad J\leq j_q(a,v)<2J,
\tag{192.F1}
\]

and the already removed inverse-small, live-side terminal, and isolated
Fejer projections. The canonical selector data are

\[
 \rho v_0-\beta U=1,\qquad
 T=\min\left\{\frac{U-1}{2},
      \left\lfloor\frac{QmU}{Y}\right\rfloor\right\},
\tag{192.F2}
\]

\[
 A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},\qquad
 \mathcal F_A=\{(c,d):1\leq c\leq A,\ 0\leq d\leq c,\ (c,d)=1\}.
\tag{192.F3}
\]

For \(T\geq1\), \(P_A\) is the one union indicator of rows having
\(|c\beta-d\rho|\leq T\) for some \((c,d)\in\mathcal F_A\); for
\(T=0\), \(P_A=0\). The exact ownership identity under review is

\[
 \mathscr J_{\rm safe,192,fix}
 =\mathscr J_{\rm safe,191,fix}+P_A\mathscr R_{\rm fix},
 \qquad
 \mathscr R_{\rm core,fix}=(I-P_A)\mathscr R_{\rm fix}.
\tag{192.F4}
\]

The promoted scope contains the target-safe union estimate, its outer
estimate, (192.F4), the exact core and deterministic coverage corollaries,
and the bounded-array/ambient-cover method boundary. It contains no
estimate for a nonempty core and no complete rho-large, original-\(t=1\),
parent, bridge, theorem, or exponent conclusion.

## 3. Proof and seam replay

### 3.1 Literal fields, one outer real part, and exact ownership

The kernel starts from the **exact** Round-191 remainder and makes \(P_A\)
multiply every \(v\)-indexed atom. Consequently the projection retains,
with their original signs, both orientations; outer coprimality flips;
canonical carries; affine common sites, births, and deaths; both ordered
endpoint arithmetic masks and coefficients; squarefree, divisibility,
allocation-coprimality, parity, and residual-prime fields; shell, cone,
selector, profile, floor, star, half-weight, hard-sample, crossing, trace,
and endpoint-zero fields; the literal Fejer amplitude; actual square-root
phases; conjugations; and every zero extension. No field is replaced by a
free, smooth, or orientation-separated coefficient.

At fixed parameters the inherited identity is

\[
 \mathscr R_{\rm fix}=\mathscr J_{\rm fix}
 -\mathscr J_{\rm inv,fix}-\mathscr J_{\rm terminal,fix}
 -\mathscr J_{\rm Fejer,fix}.
\tag{192.F5}
\]

Because \(P_A\) lies on \(|\rho|>T\),
\(P_A\mathscr J_{\rm inv,fix}=0\), and the kernel correctly obtains

\[
 \mathscr J_{\rm safe,192,fix}
 =\mathscr J_{\rm inv,fix}
 +(I-P_A)\mathscr J_{\rm terminal,fix}
 +(I-P_A)\mathscr J_{\rm Fejer,fix}
 +P_A\mathscr J_{\rm fix}.
\tag{192.F6}
\]

Thus Farey rows replace their old terminal and Fejer pieces; they are not
added twice. Also

\[
 \mathscr J_{\rm safe,192,fix}+\mathscr R_{\rm core,fix}
 =\mathscr J_{\rm safe,191,fix}+\mathscr R_{\rm fix},
\tag{192.F7}
\]

so nothing is lost. The modulus in the fixed safe estimate is taken only
after this joint complex projection. The outer assembly is linear, and the
core remains under the single final real part. No inner real part or
orientation-wise modulus occurs. These typing, ownership, and literal-field
seams pass.

### 3.2 Canonical and literal transport, phase, and Abel identity

For \(v=v_0+nU\), comparison of
\(\rho v_0-\beta U=1\) and \(\rho v-\gamma U=1\) gives

\[
 \boxed{\gamma=\beta+n\rho.}
\tag{192.F8}
\]

The kernel therefore uses canonical \(\beta\) only in the static Farey
selector and literal \(\gamma\) in transport. With

\[
 d_v=cn+d,\qquad \Delta=cv-d_vU=cv_0-dU,\qquad
 \ell=c\beta-d\rho,
\]

direct substitution gives

\[
 \boxed{\rho\Delta=c+U\ell,\qquad
        \gamma\Delta=d_v+v\ell.}
\tag{192.F9}
\]

Since \(\rho\equiv\bar v_q\pmod q\) and \(U=mq\),

\[
 \boxed{z_{\omega,v}^{\Delta}=e(\epsilon_\omega ac/q).}
\tag{192.F10}
\]

This is valid for either sign of \(\Delta\), but it supplies no saving:
\(|\ell|\) disappears and the right side can equal or approach one. For a
finite or absolutely summable zero-extended sequence, reindexing gives

\[
 \sum_h\{W(h)-W(h-\Delta)\}z^h
 =(1-z^\Delta)\sum_hW(h)z^h,
\tag{192.F11}
\]

which proves (192.K33) only when \(z^\Delta\ne1\). The current kernel's
absolute-summability hypothesis and zero-extension direction are exact.

### 3.3 Affine carry and endpoint number/divisor translations

The canonical anchor definition makes

\[
 N_\omega(h;\Delta)
 =\frac{S_{0,\omega}(h+\Delta)-S_{0,\omega}(h)
        -\epsilon_\omega\rho\Delta}{U}
 =\theta_{\omega,c}(h)-\epsilon_\omega\ell,
\tag{192.F12}
\]

where

\[
 \theta_{+,c}\in\{-1,0\},\qquad
 \theta_{-,c}\in\{0,1\}.
\tag{192.F13}
\]

Hence the accumulated mode-and-affine factor is exactly

\[
 (-1)^{N_\omega(h;\Delta)}e(\epsilon_\omega ac/q).
\tag{192.F14}
\]

The core controls neither its parity nor its distance from one. Put
\(A_0=\kappa gU\), \(C_v=\kappa v\),
\(E=c+U\ell\), and \(F=d_v+v\ell\). Kernel tables
(192.K38)--(192.K39) are exactly

\[
\begin{array}{c|cc}
 &\Delta N_{i,+}&\Delta d_{i,+}\\ \hline
i=0&2A_0F&0\\
i=1&2gC_vE&2gE
\end{array},
\qquad
\begin{array}{c|cc}
 &\Delta N_{i,-}&\Delta d_{i,-}\\ \hline
i=0&-2gC_vE&-2gE\\
i=1&-2A_0F&0
\end{array}.
\tag{192.F15}
\]

The direction check passes in both orientations:

\[
 \Delta(N_{1,\omega}-N_{0,\omega})
 =2\kappa g\{vE-UF\}=2\kappa g\Delta.
\tag{192.F16}
\]

The unequal translations contain representative-dependent \(d_v\), shift
the plus \(d_{1,+}\) and minus \(d_{0,-}\) divisor arguments with the
displayed signs, and can flip every inherited literal field or create affine
births and deaths. No endpoint invariance or cancellation is overclaimed.

### 3.4 Exact core, floors, and method scope

The factorization

\[
 \rho(cv_0-dU)=c+U(c\beta-d\rho)
\tag{192.F17}
\]

is nonzero because \(1\leq c<U\). It gives the signed-divisor fibre bound
and target-safe union count used in (192.K17)--(192.K26). The circular
pigeonhole lemma, including gcd reduction, \(A=1\), both signs, and endpoint
fractions, gives

\[
 \min_{(c,d)\in\mathcal F_A}|c\beta-d\rho|
 \leq\left\lfloor\frac{|\rho|}{A+1}\right\rfloor.
\tag{192.F18}
\]

Thus a \(T\geq1\) core row has
\(|\rho|\geq(A+1)(T+1)\), and the core is empty under the exact kernel
condition

\[
 T\geq1,\qquad
 \left\lfloor\frac{(U-1)/2}{A+1}\right\rfloor\leq T.
\tag{192.F19}
\]

There is no sign, floor, or endpoint error. At \(T=0\), \(P_A=0\) and the
core is the whole inherited rho-large remainder; (192.F19) is not applied.

The prime-modulus covering control is expressly conditional on an
unsaturated \(T\geq1\) residue universe with \(\asymp U\) surviving central
classes. The bounded-array control is likewise coefficient-class only.
Kernel Section 6 explicitly disclaims literal lower mass and disproof of
the desired fixed-coefficient estimate. These method boundaries pass.

### 3.5 Owner and exponent boundary

Kernel Section 7 declares only one subordinate Farey-union/core reduction.
It keeps the nonempty-core estimate, complete rho-large remainder, complete
original \(t=1\), every original \(t\geq2\) range, the remaining small-\(t\)
owner, hard and smooth M1, GAR, all M2 parents, endpoint uniformity, M9,
both bridges, the quarter target, and every exponent open, conditional, or
unchanged. No node is silently promoted to original-\(t=1\) or global
closure. This seam passes.

## 4. First doubtful or unproved step

The first unproved mathematical estimate remains the nonempty-core bound

\[
 \Re\mathscr R_{\rm core,Y,Q}^{\sigma}
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon,
\tag{192.F20}
\]

or the sufficient stronger fixed-packet estimate

\[
 |\mathscr R_{\rm core,fix}|
 \ll_{C_0,\varepsilon}Qm\kappa uX^\varepsilon.
\tag{192.F21}
\]

Nothing in the kernel proves either. The first missing literal input is a
jointly signed correlation estimate for the complete coefficient under the
unequal endpoint translations, arithmetic masks, carries, actual
square-root phases, and affine births/deaths before any positive norm.

No formal kernel defect remains. The repaired absolute-summability wording
in (192.K33) introduces no change to the literal aggregate, core, or owner
scope.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| locked candidate hash and provenance | PASS: the kernel records the exact locked candidate SHA-256. |
| exact fast predicate and dyadic band | PASS: (192.K2) matches (192.C4a). |
| all literal fields under one outer real part | PASS: exact Round-191 inheritance, row-only projection, (192.F6), and linear outer assembly drop no field and introduce no inner real part or orientation norm. |
| terminal/Fejer ownership and no double count | PASS: (192.F6)--(192.F7) replace selected terminal/Fejer rows exactly. |
| canonical \(\beta\) versus literal \(\gamma\) | PASS: (192.F8)--(192.F9) preserve the representative-dependent quotient. |
| long-step phase | PASS: (192.F10) is exact for either sign of \(\Delta\) and is not claimed as a saving. |
| zero-extended Abel equation | PASS: current (192.K33) requires a finite or absolutely summable zero-extended height sequence and applies only when \(z^\Delta\ne1\). |
| affine carry sign and parity | PASS: (192.F12)--(192.F14) have the correct wrap ranges and signs. |
| endpoint-number translations | PASS: all four entries of (192.F15) match the locked candidate. |
| endpoint-divisor translations | PASS: only \(d_{1,+}\) and \(d_{0,-}\) shift, with signs \(+2gE\) and \(-2gE\). |
| endpoint-difference direction | PASS: both orientations give (192.F16). |
| \(T=0\), saturation, and empty-core floor | PASS: the piecewise selector and (192.F19) are exact. |
| core ownership | PASS: the core is exactly \((I-P_A)\mathscr R_{\rm fix}\), not an estimate or a second overlapping union. |
| covering and bounded-array scope | PASS: both are quarantined as coefficient-class controls, not literal mass. |
| fixed and outer powers | PASS: the \(m^{-1}\) cancellation, \(Q^{2C_0+1}\), bands, divisor ledger, and \(L^2X^\varepsilon\) scale are unchanged. |
| subordinate downstream owner | PASS: the kernel does not close the complete original-\(t=1\) residual or any parent. |
| exponent quarantine | PASS: no internal, external, target, parent, bridge, or theorem exponent changes. |
| computation | PASS: no computation is used as theorem evidence. |

## 6. Dependencies and exact artifacts used

Only the assigned artifacts were used:

1. protocol.md — SHA-256
   f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
2. proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md
   — SHA-256
   301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325.
3. rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/candidates/formalized_hard_m1_t1_rho_large_farey_covector_reduction.md
   — SHA-256
   9562954b65ac8c0f465b535e39d1c30724339098ef5a0d520507cd0983996cd5.
4. rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reports/central_core_phase_hostile_audit.md
   — SHA-256
   9051b23d31cea5eff00a1aece7ef66f26d007c1c750d5ada2e2641808f771008.
5. rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reviews/literal_phase_carry_core_owner_scope_seam_review.md
   — SHA-256
   58513c536b712170afc3def8c1e2da7bdf8541205807daa38cff18b895e8e6ea.

No state, synthesis, validation, graph, sibling review, external source, or
numerical diagnostic was read or used.

## 7. Recommended state effect and hygiene

Promote the current kernel only as one subordinate proved-internal
Farey-covector reduction. Keep (192.F20)--(192.F21) and every downstream
owner and exponent listed in Section 3.5 unchanged.

Reject any inference that the static Farey core itself supplies phase,
carry, endpoint, or literal cancellation; that the ambient covering or
bounded-array controls yield literal lower mass; or that this node closes
the complete rho-large or original-\(t=1\) owner.

Hygiene result: strict UTF-8 without BOM, no disallowed C0/DEL bytes,
LF-only line endings with one terminal newline, no trailing whitespace or
conflict markers, balanced TeX delimiters/environments/braces, unique TeX
tags, and clean path-scoped diff check.
