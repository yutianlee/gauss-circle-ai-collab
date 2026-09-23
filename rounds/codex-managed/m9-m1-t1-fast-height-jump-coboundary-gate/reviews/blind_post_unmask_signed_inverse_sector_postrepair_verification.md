# Blind-post-unmask signed-inverse sector post-repair verification

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Role: blind-post-unmask replay of the statement-only review
- Candidate reviewed:
  `candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md`
- Verified candidate SHA-256:
  `263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`
- Date: 2026-08-29

## 1. Result

**Verdict: PASS. REPAIR required: none.**

The repaired candidate resolves every qualification raised in the
statement-only review at the scope actually claimed:

1. Oddness of \(U\), and hence of \(m,q\), is explicit in (191.C3).
2. The unit condition on \(a\), the projective coordinate
   \(j_q(a,v)\), the fast cutoff, and the disjoint dyadic \(J\)-bands
   are explicit in (191.C1)--(191.C4).
3. The needed shell connectors
   \(u\asymp v\asymp L/\kappa\), literal \(v\)-support length
   \(O(u)\), and \(L\ll X^{1/4}\) are explicit in (191.C3a).
4. The fixed packet is normalized before the lift. The small-inverse
   sector is first bounded by \(Qm\kappa uX^\varepsilon\); the exact
   factor \(m^{-1}c_q(a)\) is applied only in the outer assembly, where
   it cancels that \(m\). This removes the normalization ambiguity in
   the statement-only packet.
5. The terminal and Fejer pieces are exact linear projections. The
   Fejer estimate uses the explicit pointwise atom bound and the
   \(O(\kappa)\) live-site count, not an unjustified division of the
   complete row by a possibly small Fejer factor.
6. The coefficient mass, dyadic-band loss, \((m,q)\)-divisor ledger,
   \((\kappa,u)\)-shell sum, and logarithmic absorption are all written
   explicitly in (191.C33)--(191.C35), matching the accepted Round-189
   kernel.
7. The jump-source partition and the safe/remainder projections are
   exact before the final real part. Neither orientation is discarded
   or separately promoted.
8. The modewise carry factor is correctly distinguished from the
   complete pre-Fourier parity law in (191.C20a).
9. The bounded-height-array capacity statement (191.C38) is correctly
   scoped as an operator-class insufficiency result, not as a literal
   realizability claim or a lower bound for the fixed coefficient.
10. The candidate does not claim the full fast packet. It leaves
    (191.C12) open with the exact \(Y/(Qm)\) deficit and expressly leaves
    every parent, bridge, downstream incidence, and exponent unchanged.

Accordingly, (191.C5)--(191.C11) form a valid strict reduction and
target-safe subpacket, conditional only on the accepted Round-189
kernel and the stated elementary divisor bound. They do not prove
(191.C12).

## 2. Exact statement and hypotheses

The post-repair replay verifies the following exact scope.

The literal fast packet has

\[
 Q=\lfloor(\log(2X))^B\rfloor,\qquad
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y,
\]

\[
 (a,q)=1,\quad U\mid u,\quad g=u/U,\quad
 \kappa,g,U\ {\rm odd},\quad (u,v)=1,\quad (U,h)=1,
 \quad0<2\kappa gh<R_0=\lceil L\rceil.
\tag{2.1}
\]

On nonzero inherited support,

\[
 u\asymp v\asymp L/\kappa,\qquad
 \operatorname{length}(\mathcal V_{\rm lit})\ll u,\qquad
 L\ll X^{1/4}.
\tag{2.2}
\]

These conditions supply every connector that was missing from the
statement-only review. In particular, the literal \(v\)-support lies
in an \(O(u)\)-scale interval, so a residue class modulo \(U\) occurs
\(O(u/U+1)=O(u/U)\) times and a residue class modulo \(q\) occurs
\(O(u/q+1)=O(u/q)\) times.

The fast projective variable and cutoff are exactly

\[
 j_q(a,v)=|a\bar v_q|_q,\qquad
 T_Q=\min\left\{\frac{q-1}{2},
 \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\},\qquad
 j_q(a,v)>T_Q.
\tag{2.3}
\]

If \(T_Q=(q-1)/2\), the fast packet is empty. Otherwise its positive
projective values are partitioned disjointly by the power-of-two bands
\(J\le j_q(a,v)<2J\), with automatic truncation of the last band.

The signed-inverse threshold is

\[
 T_\varrho=\min\left\{\frac{U-1}{2},
 \left\lfloor\frac{QmU}{Y}\right\rfloor\right\}.
\tag{2.4}
\]

The fixed packet in (191.C13a) does **not** yet contain the outer lift
coefficient. The exact lift

\[
 c_{mq}(ma)=m^{-1}c_q(a)
\tag{2.5}
\]

is inserted by the inherited linear outer assembly in Section 6 of the
candidate. This normalization is consistent with the accepted
Round-189 kernel and is essential to the ledger check below.

The reviewed theorem is only

\[
 |\mathscr J_{\rm fix}^{\rm safe}|
 \ll_\varepsilon Qm\kappa uX^\varepsilon,\qquad
 |\mathscr J_{Y,Q}^{\rm safe,\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon,
\tag{2.6}
\]

together with the exact decomposition

\[
 \mathscr F_{Y,Q}^{\sigma}
 =\mathscr J_{Y,Q}^{\rm safe,\sigma}
  +\mathscr R_{Y,Q}^{\sigma}.
\tag{2.7}
\]

The bound for \(\Re\mathscr R_{Y,Q}^{\sigma}\) remains explicitly open.

## 3. Proof or derivation

### 3.1 Hash and dependency normalization

The current file hash computed in this replay is exactly

`263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`,

after the candidate-status metadata line was updated to
`repaired; pending independent post-repair replay`. The conductor
identified this as a metadata-only change from the dispatch hash; it
does not alter any reviewed definition, equation, proof, dependency,
scope statement, or proposed state effect. Thus the reviewed
mathematical text remains the repaired candidate named in the brief.
Its packet normalization agrees with the accepted Round-189 kernel:
the fixed fast row is formed first, while \(m^{-1}c_q(a)\), coefficient
mass, projective bands, and divisor sums belong to the outer assembly.

This explains a superficial difference from the statement-only review.
That review inserted the lift while estimating the small inverse sector
and obtained the smaller fixed expression \(Q\kappa u\) up to logs.
The repaired candidate instead proves the pre-lift bound
\(Qm\kappa u\) and then cancels \(m\) by (2.5). These are the same
ledger at two different, now explicitly identified, packet levels.

### 3.2 Signed-inverse transport and Fourier carry

From

\[
 \varrho v-\gamma U=1
\]

one obtains, in the plus orientation,

\[
 (S-\varrho)v-U(w-\gamma)=h-1,
\]

and, in the minus orientation,

\[
 U(w+\gamma)-v(S+\varrho)=h-1.
\]

Thus (191.C17) is the exact full-fibre transport. Canonical reduction
modulo \(U\) gives

\[
 \nu_\omega(h)=
 \frac{S_{0,\omega}(h)-\epsilon_\omega\varrho
       -S_{0,\omega}(h-1)}U\in\{-1,0,1\},
\]

and the old affine index is \(t+\nu_\omega(h)\), contributing
\((-1)^{\nu_\omega(h)}\). The candidate does not extend this bijection
to positivity or literal masks; their failures are retained among the
birth/death and mask terms.

Oddness is now explicit in (191.C3), so before Fourier splitting
\((-1)^{S_0+t}=(-1)^S\) and the transported complete parity changes by
\((-1)^\varrho\). For one retained mode, the candidate uses the
**current divided by transported-previous** ratio

\[
 (-1)^{\nu_\omega(h)}
 e(\epsilon_\omega a\varrho/q).
\tag{3.1}
\]

The statement-only review wrote the reciprocal convention and hence
the conjugate phase. There is no disagreement. Equation (191.C20a)
correctly states that (3.1) is carry- and mode-dependent and is not the
constant \((-1)^\varrho\). No modewise parity strengthening remains.

### 3.3 Exact jump-source projections

The outer identity (191.C22d) is an exhaustive Boolean partition:

- the first line contains the live side of a \(K\)-interval entry or
  exit;
- the next two terms contain coprimality flips while \(K\) persists;
- only the persistent \(K,G\) branch passes to affine transport.

Thus simultaneous changes are neither omitted nor duplicated. On that
persistent branch, the integer-fibre bijection partitions indices into
common sites, current births, and previous deaths, proving (191.C23).

The common-site identity (191.C24) is algebraically exact. Expanding its
right side gives

\[
 F_h\Lambda_h\Psi_h
 -\chi F_-\Lambda_-^{\rm tr}\Psi_-^{\rm tr},
 \qquad \chi=(-1)^{\nu_\omega(h)}.
\]

The ordered endpoint expansion (191.C24a) and mask/literal expansion
(191.C25) are ordinary two-factor telescopings. The ordered
first-changed-field rule in (191.C25a) makes the listed changes disjoint
and exhaustive, while retaining the actual numerical profile difference
and the common-cell coefficient difference. Endpoint zero extension is
kept distinct from the outer \(K\)-terminal.

The projections (191.C28b)--(191.C28c) are then literal linear
restrictions of this partition, and (191.C28d) defines the remainder by
complex subtraction. Both orientations stay inside each complex
packet. Taking a triangle inequality among the three already defined
safe projections does not move an absolute value inside the remainder.

### 3.4 Small signed-inverse sector

Inversion is a bijection on the unit classes modulo \(U\), so the sector
\(0<|\varrho_U(v)|\le T_\varrho\) uses at most
\(2T_\varrho\) classes. By (2.2),

\[
 \#\{v\text{ in the sector}\}
 \ll \frac{uT_\varrho}{U}
 \ll \frac{Qmu}{Y}.
\tag{3.2}
\]

The \(J\)-band only deletes rows. Abel's exact identity returns the
normalized jump expression to the original row sum, so no \(q/J\)
factor is paid here. With \(O(Y)\) heights, \(O(\kappa)\) live sites,
and pointwise atom weight \(O_\varepsilon(X^\varepsilon)\), (3.2)
gives

\[
 |\mathscr J_{{\rm inv},{\rm fix}}|
 \ll_\varepsilon
 Y\kappa X^\varepsilon\frac{Qmu}{Y}
 \ll Qm\kappa uX^\varepsilon.
\tag{3.3}
\]

If \(T_\varrho=0\), this sector is empty. If the cap
\((U-1)/2\) is selected, every unit inverse class lies in the sector
and the complementary row packet is empty. No endpoint case is lost.
This is a positive cardinality theorem for a strict sector and asserts
no cancellation on its complement.

### 3.5 Terminal and Fejer projections

The projective map \(v\mapsto a\bar v_q\) permutes unit classes modulo
\(q\). A \(J\)-band has \(O(J)\) such classes, each occurring
\(O(u/q)\) times by (2.2), hence

\[
 \#\{v:J\le j_q(a,v)<2J\}\ll uJ/q.
\tag{3.4}
\]

The support of \(K\), the intersection of the dyadic height interval
and the carrier interval, is one integer interval. Its backward
difference has at most two live-side terminals. The fixed-row bound,
the Abel factor \(q/J\), and (3.4) give

\[
 |\mathscr J_{{\rm terminal},{\rm fix}}|
 \ll_\varepsilon(q/J)(uJ/q)\kappa X^\varepsilon
 \ll\kappa uX^\varepsilon.
\tag{3.5}
\]

The Fejer projection is even more directly controlled than in the
statement-only review. It is the exact common-site atom

\[
 (F_h-F_{h-1})\Lambda_h\Psi_h,\qquad
 |F_h-F_{h-1}|=\frac{2\kappa g}{R_0}.
\]

There are \(O(Y)\) heights and \(O(\kappa)\) live sites per row, and
the endpoint/phase atom is \(O_\varepsilon(X^\varepsilon)\). Since a
live height obeys \(h>Y\) and \(2\kappa gh<R_0\),

\[
 \frac{2\kappa gY}{R_0}<1.
\tag{3.6}
\]

Consequently

\[
\begin{aligned}
 |\mathscr J_{{\rm Fejer},{\rm fix}}|
 &\ll_\varepsilon(q/J)(uJ/q)
 Y\kappa\frac{2\kappa g}{R_0}X^\varepsilon\\
 &\ll_\varepsilon\kappa uX^\varepsilon.
\end{aligned}
\tag{3.7}
\]

This estimate does not divide a complete row by \(F\), does not assume
mask persistence, and does not absorb any power of \(Y\). Endpoint,
mask, carry, birth/death, and phase differences remain in the exact
remainder. Since \(Qm\ge1\), (3.3), (3.5), and (3.7) prove (191.C9).

### 3.6 Outer ledger

At the outer level, (191.C33) cancels the \(m\) in the fixed bound:

\[
 (Qm\kappa u)\,m^{-1}=Q\kappa u.
\]

The unit-frequency coefficient mass is \(O(\log(2q))\), the disjoint
dyadic bands cost a fixed logarithm, and with \(u=mqr\),

\[
 \sum_{mq\mid u}1\le\tau_3(u).
\tag{3.8}
\]

Using (2.2), the remaining positive ledger is

\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{3.9}
\]

This is the same divisor and shell ledger as (189.K11)--(189.K14).
The fresh exponent \(0<\eta<\varepsilon\), together with
\(L\ll X^{1/4}\), absorbs only the fixed polylogarithmic factors. It
does not absorb a positive power of \(Y\). Thus (191.C10) follows with
no unlisted outer multiplicity.

### 3.7 Exact complement, capacity, and scope

Linearity of the inherited outer assembly sends (191.C28d) to the exact
global identity (191.C11). The remainder contains every source not in
the three safe projections, including coprimality flips, affine
births/deaths, carries, endpoint masks and coefficient changes, literal
cell/crossing changes, and square-root-phase changes.

The positive pre-Abel capacity and required scale remain

\[
 \frac{Y\kappa uJ}{q}X^\varepsilon
 \quad\text{and}\quad
 \frac{Qm\kappa uJ}{q}X^\varepsilon,
\]

so their exact quotient is \(Y/(Qm)>1\). Candidate equation (191.C38)
correctly proves that Abel's normalized operator has full capacity on
the class of bounded zero-extended height arrays: choosing
\(W_r(h)=\overline{z_r}^{\,h}\mathbf1_{H_r}(h)\) attains
\(\sum_r|H_r|\). The candidate immediately limits this to an
operator-class obstruction. It neither asserts that these arrays are
literal endpoint rows nor uses them as a lower bound or disproof for
the fixed packet.

Finally, (191.C12) is labeled open, and the candidate lists every
unproved owner and downstream theorem explicitly. There is no hidden
claim of a full-fast estimate or an exponent improvement.

## 4. First doubtful or unproved step

There is no doubtful step in the strict-sector and safe-projection
proof at the reviewed scope. The first genuinely unproved mathematical
step is exactly the one the candidate marks open:

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{4.1}
\]

At fixed packet level, a proof of (4.1) needs a signed estimate saving
the factor \(Y/(Qm)\) for the complete transported remainder. It must
handle, jointly and with the retained Fourier carry, displaced endpoint
coefficients, literal masks and cells, effective affine births/deaths,
and the actual square-root phase. Neither the repaired candidate nor
the accepted Round-189 dependency claims such an estimate.

This is an intentionally preserved open seam, not a repair defect. A
future argument may not replace the modewise factor by the full-anchor
constant, separately absolutize orientations, assume mask persistence,
or treat the bounded-array capacity control as literal mass.

## 5. Required control test and outcome

Two permitted Round-191 finite control notes were replayed.

1. The ordinary-anchor/Abel diagnostic reports 470,029 exact
   anchor, determinant, transport, and symbolic Abel checks, plus 2,720
   bounded-array capacity cases. It has zero exact failures and maximum
   numerical capacity error \(3.21\times10^{-14}\), below its
   \(10^{-10}\) threshold.
2. The signed-inverse diagnostic reports 420,672 exact transport and
   pre-Fourier parity checks and 1,325 exact inverse-class-count checks,
   all with zero failures.

The recorded counts agree exactly with the candidate's summary. The
controls confirm the finite algebra used in (191.C14)--(191.C20) and
the inverse-sector class count. They do not test the asymptotic
multiplicity bound, the lift, the divisor ledger, literal density, or
remainder cancellation; the candidate states these limitations
correctly.

Analytically, the required adversarial control also passes: on bounded
zero-extended arrays, the normalized Abel expression has exact capacity
\(\sum_r|H_r|\). The candidate scopes this as diagnostic of method
insufficiency only. No false unsigned or adversarial theorem is
promoted.

## 6. Dependencies and exact artifacts used

Only the artifacts authorized by the post-unmask brief were read:

1. `protocol.md`.
2. `reviews/blind_signed_inverse_transport_sector_review.md`.
3. `candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md`,
   SHA-256
   `263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`.
4. `proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md`
   (the accepted Round-189 kernel).
5. `controls/conductor_round191_wolfram_height_jump_check.md`.
6. `controls/conductor_round191_signed_inverse_transport_check.md`.

The control programs themselves, proof graph, active campaign, strategy,
other Round-191 reports/candidates/controls, sibling reviews, and earlier
kernels were not read. No web source or new numerical computation was
used; the only hash computation was the required read-only candidate
identity check.

## 7. Recommended state effect

**PASS the repaired candidate at the verified hash; no textual or
mathematical repair is requested.** After the conductor's normal graph
and validation-matrix checks, the candidate's proposed narrow state
effect is justified: create one subordinate proved-internal reduction
for (191.C5)--(191.C11), attach it only as inconclusive evidence to the
open small-\(t\) owner, and leave all owners and exponents unchanged.

Do not mark the complete fast packet, the original-\(t=1\) residual,
any \(t\ge2\) incidence, hard or smooth M1 parent, GAR, M2 parent,
endpoint-uniformity obligation, M9, bridge, quarter theorem, or exponent
as proved. The exact remainder estimate (4.1), with deficit
\(Y/(Qm)\), remains the next open seam.
