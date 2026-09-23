# Final kernel normalization formalization: post-repair verification

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Round: 196
- Kernel:
  `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md`
- Current kernel SHA-256:
  `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb`
- Verified candidate SHA-256:
  `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`
- Verdict: **PASS**
- Numerical theorem evidence: none

## 1. Result

**PASS.** The statement-only self-containment repairs are exact and do not
alter any normalization, congruence, carrier, convolution, wrap,
commutator, event, power, or scope conclusion previously verified.

The new material does four useful things:

1. fixes \(X,B,\varepsilon,L,\sigma,Y,J\), defines
   \(H_B,Q,R_0,D_L,M\), and chooses the fresh outer-ledger
   \(\eta<\varepsilon\);
2. states \(v_0\in\{1,\ldots,U-1\}\), \(v=v_0+nU\), and
   \(n\in\mathbb Z\);
3. states that \(A,\mathcal F_A\) retain their exact accepted Round-192
   definitions and that the complete orientations, signs, anchor aggregate,
   endpoint labels, conjugations, and four cross-row blocks remain under one
   final real part; and
4. routes nonoverlap of the artificial adjacent-\(S\) sites to an outer
   birth/death rather than a common-site Fejer commutator.

Each addition was already part of the verified candidate or its accepted
interfaces. None changes K196.11--K196.38. The durable result remains only
`on_shell_carrier_denominator_self_return_no_go`.

## 2. Exact statement and hypotheses

The repaired statement now begins self-containedly with

\[
 X\ge2,\quad B>0,\quad \varepsilon>0,\quad L\ge2,\quad
 \sigma\in\{\pm1\},\quad Y<h\le2Y,
\tag{PV196.1}
\]

one nonempty power-of-two band \(J\), and

\[
 H_B=\lfloor(\log(2X))^B\rfloor,\quad Q=H_B,\quad
 R_0=\lceil L\rceil,\quad D_L=\lceil\sqrt L\rceil,\quad
 M=\min(Y,D_L).
\tag{PV196.2}
\]

It retains the physical-source mask

\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}}
\tag{PV196.3}
\]

and the exact open packet region

\[
 \kappa<D_L,\qquad M>Q\mathfrak m\kappa.
\tag{PV196.4}
\]

The exact-conductor packet, fast predicate, and band remain

\[
\begin{gathered}
 U=\mathfrak m q>4Q,\quad k=\mathfrak m a,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,\\
 (a,q)=1,\quad U\mid u,\quad g=u/U,\quad
 (u,v)=1,\quad(U,h)=1,\quad\kappa,g,U\ {\rm odd},
\end{gathered}
\tag{PV196.5}
\]

\[
 j_q(a,v)=|a\bar v_q|_q>
 \min\!\left\{\frac{q-1}{2},
 \left\lfloor\frac{Q\mathfrak m q}{Y}\right\rfloor\right\},
\qquad J\le j_q(a,v)<2J.
\tag{PV196.6}
\]

The repaired representative line is

\[
 v_0=[v]_U\in\{1,\ldots,U-1\},\qquad
 v=v_0+nU,\qquad n\in\mathbb Z,
\tag{PV196.7}
\]

followed by the unchanged canonical/literal interface

\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},\qquad
 \rho v-\gamma U=1,\qquad \gamma=\beta+n\rho.
\tag{PV196.8}
\]

The Farey selector still uses \(\beta\), literal transport still uses
\(\gamma\), and the \(T=0\) branch still retains the complete
\(|\rho|>0\) remainder. The canonical affine anchor remains

\[
 S=S_{0,\omega}(h)+Ut,\quad
 0\le S_{0,\omega}(h)<U,\quad
 S_{0,\omega}(h)\equiv
 \epsilon_\omega\bar v_Uh\pmod U.
\tag{PV196.9}
\]

The explicit full-aggregate paragraph now prevents any \(T\)-branch,
unit-inverse, wrap, parity, mask, or orientation submask from replacing
the complete core without control of its exact complement. This strengthens
statement precision without narrowing or enlarging the operator.

## 3. Proof and derivation

### Unchanged literal normalization

The exact atom is still

\[
 \mathfrak m^{-1}c_q(a)(-1)^t
 e(\epsilon_\omega a\bar v_qh/q)B_{\omega,\sigma}(h,t),
\qquad
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\tag{PV196.10}
\]

The added domains in (PV196.1)--(PV196.9) do not modify the K185 parity
\((-1)^{S_0}(-1)^t\), the K187 coefficient

\[
 c_U(\mathfrak m a)=\mathfrak m^{-1}c_q(a),
\tag{PV196.11}
\]

or the phase
\(e(\epsilon_\omega a\bar v_qh/q)\).

### Unchanged determinant and \(4q\) algebra

K196.13--K196.15 retain the two exact signs

\[
 2h\equiv vx\pmod q\quad(+),\qquad
 2h\equiv-vx\pmod q\quad(-),
\tag{PV196.12}
\]

and hence
\(\epsilon_\omega\bar v_qh\equiv\bar2_qx\pmod q\).
The parity identity and primitive numerator remain

\[
 (-1)^S=\chi_4(\kappa U)\chi_4(x),\qquad
 b_{q,a}\equiv q+4a\bar2_q\pmod{4q},\qquad
 (b_{q,a},4q)=1.
\tag{PV196.13}
\]

Therefore the formal shadow still has

\[
 z_{q,a}=-e(a/q),\qquad
 (1-z_{q,a})c_q(a)=\frac{2e(a/q)}q.
\tag{PV196.14}
\]

No statement-only addition touches these equations or promotes the shadow
to a literal mode.

### Unchanged parity convolution and wrap boundary

The literal factorization still inserts
\(E_U(S_{0,\omega})=(-1)^{S_{0,\omega}}\), and K196.23 remains

\[
\mathfrak m^{-1}c_q(a)E_U(S_0)e(kS_0/U)
=\mathfrak m^{-1}c_q(a)
\sum_{r\bmod U}c_U(r)e((r+k)S_0/U).
\tag{PV196.15}
\]

Thus the weights remain products rather than original shifted packet
coefficients, and full recombination still removes the distinguished
\(c_q(a)\).

The literal adjacent ratio is unchanged:

\[
 (-1)^{\mathbf1_{\{S_0=U-1\}}}e(a/q).
\tag{PV196.16}
\]

Every live-to-live edge is nonwrap with multiplier \(e(a/q)\). The formal
\(z_{q,a}\)-wrap lands at \(S_0=0\) and remains a live/dead
zero-extension boundary with no paired denominator cancellation. The
near-half value remains

\[
 |(1-e(a/q))c_q(a)|
 =\frac2q\cot\!\left(\frac{\pi}{2q}\right)\asymp1.
\tag{PV196.17}
\]

### Unchanged product rules and event geometry

The parity product rule and its solved form remain

\[
 \Delta_2(E_UB)=E_U\Delta_2B+(E_U-E_U^-)B^-,
\tag{PV196.18}
\]

\[
 E_U\Delta_2B
 =\Delta_2(E_UB)-(E_U-E_U^-)B^-.
\tag{PV196.19}
\]

The physical-mask identity remains

\[
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
  +\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\tag{PV196.20}
\]

The genuine transport still uses
\((S-\epsilon_\omega\rho,w-\epsilon_\omega\gamma)\) and has
\(x_h-x_{h-1}^{\rm tr}=2\epsilon_\omega\rho\). The artificial endpoint
tables, \((2gC_v,2g)\) displacement, opposite \(\pm v\) height shifts,
and raw Fejer difference \(2\kappa gv/R_0\) are unchanged.

The new nonoverlap sentence is exactly the verified interpretation: if
the artificial sites do not overlap, there is no common-site Fejer
difference; the contribution is an outer birth or death. This adds no
regularity and removes no atom.

### Unchanged power and proof-state boundary

The strongest fixed estimate remains

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+M\}X^\varepsilon,
\tag{PV196.21}
\]

with deficit

\[
 \frac{M}{Q\mathfrak m\kappa}>1.
\tag{PV196.22}
\]

The new explicit choice \(0<\eta<\varepsilon\) merely makes the existing
outer epsilon rebudgeting self-contained. It does not alter the conditional
outer ledger or hide a positive power.

## 4. First doubtful or unproved step

No doubtful step was introduced by the self-containment repairs. The first
unproved analytic step remains a coefficient-sensitive joint
\((++,+-,-+,--)\) cross-row estimate for the complete literal region
(PV196.4), with every endpoint, phase, mask, carry, coprimality,
birth/death, and zero-extension field retained before positive norms and
with gain \(M/(Q\mathfrak m\kappa)\).

## 5. Required controls and outcomes

1. **Current hash and text integrity — PASS.** SHA-256 is
   `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb`;
   no non-line ASCII controls occur.
2. **Global parameters — PASS.** \(X,B,\varepsilon,L,\sigma,Y,J,\eta\)
   and \(H_B,Q,R_0,D_L,M\) now have explicit domains and definitions.
3. **Representative self-containment — PASS.** The range of \(v_0\), the
   integer \(n\), normalized \(\rho\), canonical \(\beta\), and literal
   \(\gamma\) are exact.
4. **Full-aggregate scope — PASS.** All orientations, signs, anchor modes,
   labels, conjugations, and four cross-row blocks remain joint; no submask
   is promoted without its complement.
5. **Normalization and determinant algebra — PASS.** K196.11--K196.23 are
   unchanged in content and signs.
6. **Wrap and product rules — PASS.** K196.24--K196.30 retain the live/dead
   boundary and both exact product-rule signs.
7. **Artificial-event completion — PASS.** Nonoverlap is now explicitly an
   outer birth/death; endpoint, height, and Fejer vectors are unchanged.
8. **Power and scope — PASS.** K196.35--K196.38 retain the same deficit,
   conditional assembly, no-lower-mass status, owner boundary, and exponent
   quarantine.
9. **Candidate provenance — PASS.** The embedded candidate hash remains
   `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`.

## 6. Dependencies and exact artifacts used

- `proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md`,
  current SHA-256
  `51da98a07b52706a510f9ea07c52d952323e8282cb3ab6e100347c71b63f54fb`.
- `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/reviews/final_kernel_normalization_formalization_review.md`,
  pre-repair review SHA-256
  `e4c0d4fc80a64c38e981f930dd7090458f02718bd963a9d605a79d716367c9b4`.
- `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md`,
  SHA-256
  `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`.
- The exact K185, K187, K191, K192, and Round-195 kernels listed in the
  pre-repair formalization review.

No web source, numerical experiment, or computation is theorem evidence.

## 7. Recommended state effect

**PASS the current durable kernel with its improved self-contained
statement.** Retain only the exact route-scoped normalization/support no-go
for the proposed carrier-denominator mechanism.

Do not create a target-safe sector or close any \(P_2\) packet. Retain the
complete \(P_2\) remainder and hard-M1 small-\(t\) owner as open, and leave
\(P_1\), complete original \(t=1\), all other original-\(t\) incidences,
both M1 parents, GAR, every M2 parent, endpoint uniformity, M9, both
bridges, the quarter theorem, and every exponent unchanged. This review
makes no shared-state edit.
