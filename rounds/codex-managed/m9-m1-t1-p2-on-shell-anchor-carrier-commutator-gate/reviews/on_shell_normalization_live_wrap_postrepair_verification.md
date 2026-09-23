# Post-repair verification: on-shell normalization and live wrap

- Round: 196
- Verdict: **PASS**
- Candidate SHA-256:
  `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`
- Numerical theorem evidence: none

## 1. Result

**PASS.** The repaired candidate implements every requested mathematical
repair. Equations (196.K5)--(196.K18a) have the correct exact-conductor
normalization, orientation signs, primitive carrier, live-wrap
qualification, near-half coefficient, product-rule sign, and conductor
convolution. The result is only a route-scoped normalization/support no-go;
it is neither literal lower mass nor a failure theorem for complete \(P_2\).
The final repair also restores the explicit K189 fast predicate and correctly
separates the canonical Farey quotient \(\beta\) from the literal transport
quotient \(\gamma\).

The prior seam-review artifact was repaired in place. A character scan now
finds zero U+0008 characters and zero tabs; the three intended `\bar`
commands and the intended `\text` command are literal backslash commands.

## 2. Exact statement and hypotheses

The candidate retains the complete Round-195 open packet region

\[
 \kappa<D_L,\qquad M:=\min(Y,D_L)>Q\mathfrak m\kappa,\qquad Q=H_B,
\tag{V196.1}
\]

and one exact-conductor mode with

\[
\begin{gathered}
 U=\mathfrak m q>4Q,\quad k=\mathfrak m a,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,\quad (a,q)=1,\\
 U\mid u,\quad g=u/U,\quad (u,v)=1,\quad (U,h)=1,\quad
 \kappa,g,U\ {\rm odd},\quad J\le j_q(a,v)<2J.
\end{gathered}
\tag{V196.2}
\]

Here the inherited fast predicate is stated explicitly:

\[
 j_q(a,v):=|a\bar v_q|_q>
 T_Q(\mathfrak m,q;Y):=
 \min\!\left\{\frac{q-1}{2},
 \left\lfloor\frac{Q\mathfrak m q}{Y}\right\rfloor\right\}.
\tag{V196.2a}
\]

Thus \((U,v)=1\), \(q\) is odd, and all inverses exist. For
\(\epsilon_+=1,\epsilon_-=-1\),

\[
 S=S_{0,\omega}(h)+Ut,\qquad
 S_{0,\omega}(h)\equiv\epsilon_\omega\bar v_Uh\pmod U,\qquad
 0\le S_{0,\omega}(h)<U.
\tag{V196.3}
\]

For the Round-192 core, the repaired candidate now defines

\[
 v_0=[v]_U,\qquad v=v_0+nU,
\tag{V196.3a}
\]

\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},\qquad
 \rho v-\gamma U=1,\qquad \gamma=\beta+n\rho.
\tag{V196.3b}
\]

With
\[
 T=\min\!\left\{\frac{U-1}{2},
 \left\lfloor\frac{Q\mathfrak m U}{Y}\right\rfloor\right\},
\tag{V196.3c}
\]
the \(T=0\) branch retains the complete inherited \(|\rho|>0\)
remainder, while the \(T\ge1\) core satisfies
\[
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A),\qquad
 |\rho|\ge(A+1)(T+1).
\tag{V196.3d}
\]
The covector condition correctly uses canonical \(\beta\), not the
lift-dependent \(\gamma\). The latter remains confined to literal height
transport. This is exactly K192.K3, K192.K11, and K192.K15.

The literal exact-conductor atom is

\[
 \boxed{\mathfrak m^{-1}c_q(a)(-1)^t
 e(\epsilon_\omega a\bar v_qh/q)B_\omega(h,t),}
 \qquad c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\tag{V196.4}
\]

This completes the formerly missing unit, oddness, fast-packet,
signed-inverse, and branch hypotheses before the live-wrap argument.

## 3. Proof and derivation

K192.K2 gives (V196.2a). K192.K3 and K192.K15 give
\(\gamma=\beta+n\rho\), so replacing \(\beta\) by \(\gamma\) in the Farey
selector would change the core mask by a lift-dependent multiple of
\(\rho\). Equation (V196.3d) avoids that error and matches K192.K11
exactly. The \(T=0\) wording also makes no unsupported claim that the
unit-inverse selector is a proper nonempty submask: it cannot replace the
complete branch unless its literal complement is empty or estimated.

K187.15--K187.16 give

\[
 k=(U/q)a=\mathfrak m a,\qquad
 c_U(k)=(q/U)c_q(a)=\mathfrak m^{-1}c_q(a),
\tag{V196.5}
\]

and the phase in (V196.4). Round 187 expands
\(E_U(S_{0,\omega})=(-1)^{S_{0,\omega}}\), leaving \((-1)^t\).

For \(x=\kappa U+2S\), the determinant charts are

\[
\begin{array}{ll}
2h=v\eta_+ +U\delta_+-\kappa(U^2-v^2),
&x=\kappa v+\eta_+=d'/g,\\
2h=U\eta_- -v\delta_-+\kappa(U^2-v^2),
&x=\kappa v+\delta_-=d/g.
\end{array}
\tag{V196.6}
\]

Modulo \(q\mid U\),

\[
 \bar v_qh\equiv\bar2_qx\pmod q\quad(+),\qquad
 -\bar v_qh\equiv\bar2_qx\pmod q\quad(-).
\tag{V196.7}
\]

Both orientations therefore yield \(e(a\bar2_qx/q)\). Since
\(x,\kappa U\) are odd,

\[
 (-1)^S=\chi_4(\kappa U)\chi_4(x).
\tag{V196.8}
\]

For \(b_{q,a}\equiv q+4a\bar2_q\pmod{4q}\), \(b_{q,a}\) is odd and
\(b_{q,a}\equiv2a\not\equiv0\pmod p\) for every \(p\mid q\). Hence
\((b_{q,a},4q)=1\), and

\[
 z_{q,a}=e(b_{q,a}/(2q))=-e(a/q),\qquad
 (1-z_{q,a})c_q(a)=\frac{2e(a/q)}q.
\tag{V196.9}
\]

This proves (196.K6)--(196.K7) for the parity-restored shadow. The literal
mode differs because oddness of \(U\) gives

\[
 (-1)^t=E_U(S_{0,\omega})(-1)^S.
\tag{V196.10}
\]

Thus (196.K8) has the required extra \(E_U(S_{0,\omega})\).

The repaired conductor identity includes the outside coefficient:

\[
\mathfrak m^{-1}c_q(a)E_U(S_0)e(kS_0/U)
=\mathfrak m^{-1}c_q(a)
\sum_{r\bmod U}c_U(r)e((r+k)S_0/U).
\tag{V196.11}
\]

Its coefficients are
\(\mathfrak m^{-1}c_q(a)c_U(r)\), not the original shifted packet weights
\(c_U(r+k)\). It mixes exact conductors and packet partitions. Full
recombination gives

\[
 (-1)^t\sum_{k\bmod U}c_U(k)e(kS_0/U)
 =(-1)^tE_U(S_0)=(-1)^S,
\tag{V196.12}
\]

so the distinguished \(c_q(a)\) disappears.

For \(S\mapsto S+1\), put
\(c(S_0)=\mathbf1_{\{S_0=U-1\}}\). The literal ratio is

\[
 (-1)^{c(S_0)}e(a/q).
\tag{V196.13}
\]

A wrap lands at \(S_0'=0\), hence \(U\mid h'\), and cannot be live-to-live
under \((U,h')=1\). Every live-to-live adjacent step is nonwrap and has
ratio \(e(a/q)\), not \(z_{q,a}\). The wrap is not discarded: zero
extension retains a live/dead coprimality boundary atom with the original
coefficient and no paired denominator cancellation.

For \(a=(q-1)/2\),

\[
 |(1-e(a/q))c_q(a)|
 =\frac2q\cot\!\left(\frac{\pi}{2q}\right)\asymp1.
\tag{V196.14}
\]

This is a coefficient-level control, not literal lower mass.

With

\[
 \Delta_2B=B(x)-B(x-2),\quad B^-=B(x-2),\quad
 E_U^-=E_U(S_0(x-2)),
\tag{V196.15}
\]

direct expansion gives

\[
 \Delta_2(E_UB)=E_U\Delta_2B+(E_U-E_U^-)B^-,
\tag{V196.16}
\]

and therefore

\[
 \boxed{E_U\Delta_2B
 =\Delta_2(E_UB)-(E_U-E_U^-)B^-.}
\tag{V196.17}
\]

The solved commutator has the correct minus sign, and
\(|E_U-E_U^-|=2\) on every possible live-to-live adjacent edge.

Finally,

\[
(S,w)\mapsto
(S-\epsilon_\omega\varrho_U(v),w-\epsilon_\omega\gamma_U(v))
\tag{V196.18}
\]

has current-minus-transported-previous \(x\)-displacement
\(2\epsilon_\omega\varrho_U(v)\); equivalently the forward map shifts
\(x\) by \(-2\epsilon_\omega\varrho_U(v)\). The signs are exact, and this
is not a common literal \(\Delta_2\) event.

## 4. First doubtful or unproved step

There is no doubtful algebraic step in the repaired no-go. The first
genuinely unproved analytic step is a coefficient-sensitive joint cross-row
\((++,+-,-+,--)\) estimate on

\[
 P_{2,<D_L}\cap\{M>Q\mathfrak m\kappa\},
\tag{V196.19}
\]

with the actual endpoints, phases, masks, carries, births/deaths, and zero
extensions. No accepted interface supplies it.

## 5. Required controls and outcomes

1. K189 fast predicate and Round-192 core normalization: **PASS** by
   (V196.2a)--(V196.3d). The signed inverse is normalized, the Farey
   covector uses \(\beta\), and \(\gamma\) is used only for literal
   transport.
2. Exact-conductor normalization and orientation signs: **PASS** by
   (V196.5)--(V196.7).
3. \(4q\)-primitivity and coefficient identity: **PASS** by (V196.9).
4. Unit support, no live-to-live wrap, and retained boundary atom:
   **PASS** by (V196.13).
5. Near-half coefficient: **PASS** by (V196.14), explicitly scoped as a
   method control.
6. Product-rule definitions and solved sign: **PASS** by
   (V196.15)--(V196.17).
7. Conductor mixing, outside coefficient, and non-packet weights:
   **PASS** by (V196.11)--(V196.12).
8. Power and scope: **PASS**. The accepted bound remains
   \[
    |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
    \ll u\{\kappa+M\}X^\varepsilon,
   \]
   with unresolved factor \(M/(Q\mathfrak m\kappa)>1\). No strict sector,
   lower bound, parent, bridge, theorem, or exponent is claimed.
9. Text integrity: **PASS**. The repaired review has no U+0008 or tab
   characters; the candidate has no non-line ASCII controls.

## 6. Dependencies and exact artifacts used

- `protocol.md`.
- `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`:
  K185.27, K185.30--K185.36.
- `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md`:
  K187.7, K187.14--K187.16.
- `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md`:
  K191.C2--C5, K191.C17, K191.C20a.
- `proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md`:
  K192.K1--K192.K5, K192.K11, K192.K15.
- `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md`:
  (195.C3)--(195.C5a), (195.C8)--(195.C13), (195.C19)--(195.C20a).
- The three Round-196 reports, the conductor reconciliation, and the
  repaired `reviews/on_shell_normalization_live_wrap_seam_review.md`.
- `candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md`,
  final SHA-256
  `5174129858c2ced67c2d637a0cbdb1153d1b18da7491c1b80316532485497380`.

No web source, numerical experiment, or computation is theorem evidence.

## 7. Recommended state effect

**Promote only the repaired route-scoped normalization/support no-go as a
durable kernel.** Record that the literal exact-conductor mode lacks the
proposed bare primitive carrier and that inserting the missing parity factor
causes conductor mixing and a live bulk/boundary commutator.

Do not create a target-safe obligation or mark any remaining \(P_2\) packet
proved. Complete \(P_2\), \(P_1\), complete original \(t=1\), the hard
small-\(t\) owner, smooth M1, GAR, all M2 parents, endpoint uniformity, M9,
both bridges, the quarter theorem, and every exponent remain unchanged.
This review makes no shared-state edit.
