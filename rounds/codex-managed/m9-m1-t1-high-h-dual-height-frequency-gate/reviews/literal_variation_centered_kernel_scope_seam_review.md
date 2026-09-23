# Round 189 literal-variation, centered-kernel, and owner-scope seam review

- Campaign: m9-m1-t1-high-h-dual-height-frequency-gate
- Review seam: literal variation, centered conductor, and scope
- Frozen candidate SHA-256:
  03d5f66eea725f619678e30cfe211163d4d245c5529f57e853831bf31585a95b
- Starting graph SHA-256:
  338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c
- Numerical theorem evidence: none

## 1. Result and verdict

**GREEN.** The frozen candidate is promotion-worthy for exactly its
stated subordinate reduction:

\[
 j_q(a,v)\le
 T_Q(m,q;Y):=
 \min\!\left\{\frac{q-1}{2},
       \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\}
\tag{189.R1}
\]

is an absolutely target-safe sector of the exact Round-188 complement,
and its exact complementary aggregate remains under one outer real
part. The proof retains the correct \(Q\), \(m\), \(q\), \(Y\),
\(\kappa\), \(u\), and \(L\) powers.

Equations (189.K16)--(189.K19) are also correctly scoped. The
\(Qm\)-scaled variation bound (189.K18) is sufficient, but is not
asserted as proved. The available literal variation is larger by
exactly \(Y/(Qm)>1\), with primitive-lift deficit \(Y/Q\), not
uniformly absorbable over the full height range.

The centered inversion is invoked only for actual odd conductors. The
prime identity and slope \(-2\) survivor are correct and are
quarantined as mechanism falsifiers, not literal lower mass. No
periodicity, positive-energy closure, complete high-height result,
downstream theorem, or exponent is overclaimed.

No mathematical or scope repair is required.

## 2. Exact claim and hypotheses reviewed

The review freezes the actual Round-185 carrier
(K185.27), (K185.30)--(K185.35), inherited through the Round-188
complement. Thus

\[
 \kappa,g,h,U,v>0,\quad
 \kappa,g,U\ {\rm odd},\quad
 (gU,v)=1,\quad(U,h)=1,\quad
 0<2\kappa gh<R_0,
\tag{189.R2}
\]

with \(u=gU\), \(u,v\asymp L/\kappa\), and \(O(\kappa)\) live
affine sites per oriented row. The candidate's reference to the exact
carrier and its literal zero extension retains the omitted shorthand
positivity and support predicates in every displayed sum.

The unique lift coordinates satisfy

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad
 Qm<Y,\qquad(a,q)=1.
\tag{189.R3}
\]

Since \(U\) is odd and \(m\mid U,\ q=U/m\), both \(m\) and \(q\)
are odd. Since \(q\mid U\mid u\) and \((u,v)=1\), \(v\) is a unit
modulo \(q\), and \(j_q(a,v)=|a\bar v_q|_q\) is well defined.

The candidate retains, by exact reference and inside
\(A_{\kappa,u,mq,h,v,\omega}^{\sigma}\), both orientations, the
affine parity, every \(t\), selector, squarefree and
allocation-coprimality deletion, profile, floor, star, half-weight,
hard sample, crossing, endpoint order, conjugation, Fejer factor,
square-root phase, positivity predicate, terminal block, sign, and
zero extension.

The complex identity

\[
 \mathscr C_{Y,Q}^{\sigma}
 =\mathscr S_{Y,Q}^{\sigma}
  +\mathscr F_{Y,Q}^{\sigma}
\tag{189.R4}
\]

is formed before a triangle inequality. Only
\(\mathscr S\) is then bounded absolutely; the unresolved statement is
\(\Re\mathscr F\), with one real part outside every label and both
orientations.

The sentence following (189.K7), “with \(Q\) replaced by \(1\),”
has only the local multiplier meaning: replace \(Q\) in the cutoff
\(T_Q\) by \(1\), while the fixed campaign parameter
\(Q=H_B\) and all predicates in (189.K3) remain unchanged. The
adjacent baseline formula and the frozen \(Q\)-candidate make this
scope unambiguous.

## 3. Checks and proof

### Literal projective and power ledger

For fixed unit \(a\bmod q\), inversion followed by multiplication by
\(a\) permutes the unit classes. For
\(0\le T\le(q-1)/2\), the two least-residue sides give exactly

\[
 2\sum_{\substack{1\le r\le T\\(r,q)=1}}1\le2T.
\tag{189.R5}
\]

They are disjoint because \(q\) is odd. This also proves the empty
\(T=0\) case and the saturated \(T=(q-1)/2\) case.

The literal \(v\)-interval has length \(O(u)\). Each residue class
occurs \(O(u/q+1)=O(u/q)\) times because \(q\mid u\). Therefore

\[
 \#\{v:j_q(a,v)\le T_Q\}
 \ll {uT_Q\over q}
 \ll {Qum\over Y}.
\tag{189.R6}
\]

Restoring \(O(Y)\) heights, \(O(\kappa)\) affine sites, two
orientations, and the exact lift coefficient gives

\[
 Y\cdot{Qum\over Y}\cdot\kappa X^\eta
 \cdot {1\over m}|c_q(a)|
 =Q\kappa u|c_q(a)|X^\eta.
\tag{189.R7}
\]

Thus both \(Y\) and \(m\) cancel before outer positive
recombination. Summing
\(\sum_{(a,q)=1}|c_q(a)|\ll\log(2q)\), followed by

\[
 \sum_{mq\mid u}1=\tau_3(u),
\tag{189.R8}
\]

and then \(\kappa,u\), yields

\[
 QX^\eta
 \sum_{\kappa}\sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log(2u)
 \ll QL^2\log^{O(1)}(2L)X^\eta.
\tag{189.R9}
\]

The inherited \(L\ll X^{1/4}\), fixed
\(Q=(\log(2X))^B+O(1)\), and a fresh epsilon budget prove
(189.K7). No positive power of \(Y\) is hidden.

### Abel interface and exact \(Qm\)-scaled deficit

The sequence \(W\) in (189.K16) is zero-extended on the complete
integer line and includes the height block, \((mq,h)=1\), the
carrier inequality, all endpoint amplitudes, and all masks. Therefore
its variation includes both endpoint jumps and every internal literal
jump.

For \(J\le j_q(a,v)<2J\), discrete Abel summation gives

\[
 \left|\sum_hW(h)e(\epsilon_\omega a\bar v_qh/q)\right|
 \ll {q\over J}\mathsf V(W),
\tag{189.R10}
\]

which is (189.K17). If (189.K18) held, then at fixed
\((\kappa,u,m,q,a,J)\),

\[
 {q\over J}
 \sum_{\omega,v\ {\rm in\ band}}\mathsf V(W_v)
 \ll Qm\kappa uX^\eta.
\tag{189.R11}
\]

Multiplying by the exact \(1/m\) lift weight gives
\(Q\kappa u|c_q(a)|X^\eta\). The \(a\)-mass, the
\(O(\log q)\) dyadic \(J\)-sum, the exact \(\tau_3(u)\) ledger, and
the outer \(\kappa,u\)-sum then reproduce (189.R9) with only another
fixed logarithm. Hence the scale in (189.K18) is precisely sufficient;
no factor \(m,q,J\), or \(Y\) is missing.

The available bound is also exact at the stated level:

\[
 |W(h)|\ll_\eta\kappa X^\eta,\qquad
 \mathsf V(W)\le2\sum_h|W(h)|
 \ll_\eta Y\kappa X^\eta.
\tag{189.R12}
\]

A \(J\)-band has \(O(uJ/q)\) literal \(v\)'s, so

\[
 \sum_{v\ {\rm in\ band}}\mathsf V(W_v)
 \ll_\eta {Y\kappa uJ\over q}X^\eta.
\tag{189.R13}
\]

The quotient of (189.R13) by the sufficient scale is exactly
\(Y/(Qm)\), strictly greater than one on \(Qm<Y\). At \(m=1\) the
uniform deficit is \(Y/Q\). This need not be large on every individual
block, but it is not uniformly bounded by a fixed polylogarithm over
the allowed height range.

Changing \(h\) changes \((mq,h)=1\), \(r=2\kappa gh\), Fejer
weight, anchors, positive affine range, births and deaths of sites,
physical endpoints, squarefree/coprime masks, residual selector,
profiles, floors, stars, crossings, conjugation, square-root phase,
and terminal zero extension. The candidate correctly infers no
improvement over (189.R12).

### Odd-conductor inversion and the bad slope

For unit \(b\bmod q\) and actual odd \(q\),

\[
 K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b).
\tag{189.R14}
\]

For every odd \(d>1\), \(E_d(-b)=-E_d(b)\); the sole \(d=1\)
trace gives

\[
 K_q(b)+K_q(-b)={2\mu(q)\over q},\qquad
 K_q^\circ(-b)=-K_q^\circ(b).
\tag{189.R15}
\]

For odd prime \(p\),
\(K_p(b)=E_p(b)-1/p\) and \(K_p^\circ(b)=E_p(b)\).
At slope \(-2\), for \(1\le h\le(p-1)/2\),
\([-2h]_p=p-2h\) is odd, so

\[
 \sum_{h=1}^{(p-1)/2}K_p^\circ(-2h)
 =-{p-1\over2}.
\tag{189.R16}
\]

This proves the exact parity and sign. It concerns the full centered
kernel, not the ordinary-edge-deleted fast packet or the literal
endpoint amplitude.

### False-mechanism and scope controls

The phase is periodic in \(h\bmod q\), but \(W(h)\) is not proved
periodic or bounded-variation. Möbius or sieve opening retains moving
selector, profile, endpoint, and phase data and supplies no estimate
of (189.K18). Positive Cauchy, Parseval, completion, large sieve,
Poisson, or alias energy returns positive residue-bucket capacity.

An abstract bounded array can dephase all displayed oscillation, so a
coefficient-uniform closure is false. Such an array need not be the
actual endpoint coefficient. Likewise (189.R16) is a kernel survivor,
not literal lower mass. The candidate makes both quarantines explicit.

## 4. First doubtful or unproved step

The first unproved mathematical step is exactly (189.K18), or a
genuinely joint signed discrepancy estimate with the same final
\(Qm\)-scaled ledger. The candidate labels it sufficient and
unproved; it does not use it to prove (189.K8).

The exact first difference of \(W\) is the sum of the common-index
difference and the birth/death contributions from the two adjacent
literal affine sets. No accepted dependency bounds those terms beyond
(189.K19). Thus the candidate stops at the correct first open
interface and records the exact deficit \(Y/(Qm)\).

There is no doubtful step before this interface and no artifact defect
in the frozen candidate bytes.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| exact Round-188 complement | PASS: all four predicates (189.R3) remain. |
| literal K185.27 and K185.30--35 carrier | PASS: every field remains inside \(A\) and \(W\). |
| one outer real part and both orientations | PASS: the complex split precedes the absolute bound. |
| projective bijection, two sides, floor, and cap | PASS: (189.R5)--(189.R6). |
| \(q\mid U\mid u\) interval multiplicity | PASS: no stray \(+1\). |
| \(O(\kappa)\) affine sites | PASS: it occurs exactly once in (189.R7). |
| exact \(1/m\) normalization | PASS: it cancels the projective \(m\) before divisor summation. |
| \(Q\)-enlarged slow cutoff and exact complement | PASS: (189.R1), (189.R4). |
| \(\kappa,u,m,q\) divisor ledger | PASS: exactly \(\tau_3(u)\), no fourth divisor. |
| K16--K19 Abel and variation scale | PASS: (189.R10)--(189.R13), with deficit \(Y/(Qm)\). |
| odd-conductor inversion | PASS: \(U,m,q\) are odd before (189.R14). |
| prime bad-slope survivor | PASS: exact value (189.R16), no lower-mass inference. |
| no invented periodicity or BV | PASS: (189.K18) remains open. |
| no positive-energy closure | PASS: positive transforms are mechanism self-returns only. |
| adversarial and literal-lower-mass quarantine | PASS. |
| original-\(t=1\)-only and exponent quarantine | PASS: all downstream owners remain open. |

## 6. Dependencies and hashes

The review used the following exact artifacts:

1. Formal candidate —
   03d5f66eea725f619678e30cfe211163d4d245c5529f57e853831bf31585a95b.
2. Conductor reconciliation —
   f7486ccf02a7fb43e1bde82e94e7da410a1d691fc8b629f2b877bc40ca6a902e.
3. Discovery report —
   65636c38a3b0c3dbd4a26839dbc89daa88ef78dee5638d02d0de1192b9bdfd38.
4. Hostile report —
   b8ec876aebcc6668646880813bad0abf576063f58e71518d29c8e5778d371608.
5. Blind report —
   13169505840f9033fb8ddaac6eba62d12988a669127f593a8bc48438543621a3.
6. Round-188 durable carrier/reduction —
   ca313d2ed11884bdb3ff237c51380de7aadd713a5dc01b565935fbdb8fe9744a.
7. Round-187 inverse-residue conductor kernel —
   a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2.
8. Round-185 literal tangent-gcd carrier —
   4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160.
9. Current proof graph —
   338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c.
10. Current active campaign —
    4d8661258570c3152d464f38d76798f1aadd271e9f4e221c80011d3ec60d68f5.

The finite Wolfram controls are diagnostic only and were not used as
asymptotic theorem evidence. No external theorem is invoked.

## 7. Recommended state effect

**Promote after the remaining required independent seams only the
strict dual-height projective reduction (189.K1)--(189.K7), together
with the exact fast complement and the scoped mechanism controls.**

Retain (189.K8) and (189.K18) as open. Keep every complete high-height
claim, complete original-\(t=1\) residual, original \(t\ge2\)
small-\(G\) incidence, large-\(G\) near-resonant complement, hard and
smooth M1 parent, GAR, M2 owner, endpoint-uniformity owner, M9, both
bridges, the quarter theorem, and every exponent unchanged and open.

Recommended Round-189 label:

strict_dual_height_resonance_sector.
