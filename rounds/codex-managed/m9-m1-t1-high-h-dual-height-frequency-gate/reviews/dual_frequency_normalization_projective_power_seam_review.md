# 1. Result and verdict

- Campaign: m9-m1-t1-high-h-dual-height-frequency-gate
- Round: 189
- Review seam: dual-frequency normalization, projective multiplicity,
  and slow-sector power ledger
- Frozen candidate SHA-256:
  03d5f66eea725f619678e30cfe211163d4d245c5529f57e853831bf31585a95b
- Verdict: **GREEN**

The candidate's proved content (189.K2)--(189.K15) is correct on the
literal inherited carrier. In particular, \(U,m,q\) are odd; the map
\(v\mapsto a\bar v_q\) is a bijection of unit classes; both
least-residue sides, the zero cutoff, and saturation are counted
without loss or duplication; and the literal multiplicity is
\(O(uT_Q/q)\). The factors \(Y\) and \(m\) cancel only through the
displayed projective sparsity and the exact \(1/m\) lift coefficient.
The remaining divisor cost is exactly an ordered three-factor cost,
not a fourth divisor variable, and the \(Q,L,X\) ledger reaches
\(L^2X^\varepsilon\) without absorbing a positive power of \(Y\).

The complex split (189.K6) is disjoint and exhaustive before
positivity. Both orientations and every literal field stay inside the
same complex aggregate, with the single outer real part applied only
at the inherited physical interface. No repair is required on this
seam.

# 2. Exact reviewed claim and hypotheses

Fix \(X\ge2\), \(L\ge2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\), and

\[
 Q=\lfloor(\log(2X))^B\rfloor,\qquad L\ll X^{1/4},\qquad
 Y>Q,\qquad Y<h\le2Y.
\]

The imported carrier is exactly (K185.27), (K185.30)--(K185.35):

\[
 \kappa,g,h,U,v>0,\qquad \kappa,g,U\ {\rm odd},\qquad
 u=gU,\qquad (u,v)=1,\qquad(U,h)=1,\qquad
 0<2\kappa gh<R_0,
\]

with the canonical anchors, both orientations, positive affine index
sets, endpoint amplitudes, arithmetic masks, and zero extensions left
literal. The exact Round-188 lift coordinates on the open complement
are

\[
 U=mq>4Q,\qquad q>Q,\qquad (a,q)=1,\qquad
 m|a|_q>Q,\qquad Qm<Y.
\]

The reviewed cutoff and complex partition are

\[
 j_q(a,v)=|a\bar v_q|_q,\qquad
 T_Q=\min\!\left\{\frac{q-1}{2},
                    \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\},
\]

\[
 \mathscr C_{Y,Q}^{\sigma}
 =\mathscr S_{Y,Q}^{\sigma}+\mathscr F_{Y,Q}^{\sigma},\qquad
 \mathscr S:\ 1\le j_q(a,v)\le T_Q,\qquad
 \mathscr F:\ j_q(a,v)>T_Q.
\]

The claim reviewed as proved is

\[
 |\mathscr S_{Y,Q}^{\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\]

The relation
\(\Re\mathscr F_{Y,Q}^{\sigma}\ll L^2X^\varepsilon\) is explicitly
open and is not part of the GREEN theorem verdict.

# 3. Derivation and checks

## 3.1 Oddness, inverses, and orientation normalization

The carrier gives \(U\) odd. Since the unique Round-188 lift has
\(U=mq\) with positive integers \(m,q\), both \(m\) and \(q\) are odd;
no assumption \((m,q)=1\) is used or needed. Also \(q>Q\ge1\), hence
\(q\ge3\). From \(q\mid U\mid u\) and \((u,v)=1\), every live \(v\)
is a unit modulo \(q\), so \(\bar v_q\) exists.

For \(\epsilon_+=1\) and \(\epsilon_-=-1\), the two phases in
(189.K5) have reduced frequencies
\(\epsilon_\omega a\bar v_q\bmod q\). Negating a residue interchanges
the two least-residue sides and leaves its distance unchanged:

\[
 |\epsilon_\omega a\bar v_q|_q=|a\bar v_q|_q=j_q(a,v).
\]

Thus the same slow/fast predicate is valid in both orientations and no
orientation is deleted or counted twice.

## 3.2 Projective bijection and exact capped count

For fixed \(a\in(\mathbb Z/q\mathbb Z)^\times\),
\[
 v\longmapsto a\bar v_q
\]
is a bijection of \((\mathbb Z/q\mathbb Z)^\times\), with inverse
\(b\mapsto ab^{-1}\). For an integer
\(0\le T\le(q-1)/2\), oddness of \(q\) makes the representatives
\(r\) and \(-r\) distinct. Therefore the number of unit classes with
\(1\le|a\bar v_q|_q\le T\) is exactly

\[
 2\sum_{\substack{1\le r\le T\\(r,q)=1}}1\le2T.
\]

At \(T=0\) the set is empty. At \(T=(q-1)/2\), the two sides exhaust
all nonzero residues, and the unit restriction leaves exactly
\(\varphi(q)\) classes. Hence the cap in (189.K4), including its
saturated case, is exact.

The full literal \(v\)-support lies in a containing interval of length
\(O(u)\), because \(u,v\asymp L/\kappa\). One residue class modulo
\(q\) occurs \(O(u/q+1)\) times. Since \(q\mid u\), \(u/q\ge1\), so
this is \(O(u/q)\) with no residual \(+1\). Arithmetic and endpoint
predicates only delete atoms. Consequently

\[
 \#\{v:1\le j_q(a,v)\le T_Q\}
 \ll \frac{uT_Q}{q}
 \le \frac{Qum}{Y}.
\]

This remains valid at both endpoints: it is exactly zero when
\(T_Q=0\), while a saturated cutoff costs \(O(u)\) and makes the fast
packet empty for that lift.

## 3.3 Exact coefficient and atom ledger

At fixed \((\kappa,u,m,q,a)\), the upper-capacity factors are

\[
 O(uT_Q/q)\quad(v),\qquad O(Y)\quad(h),\qquad
 O(1+\kappa)=O(\kappa)\quad(t),
\]

with two orientations contributing only an absolute constant. The
affine estimate includes the endpoint \(+1\) and terminal truncation.
Every literal atom is \(O_\eta(X^\eta)\). The lift normalization is
the exact identity

\[
 c_{mq}(ma)=\frac1m c_q(a),\qquad
 \sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|c_q(a)|\ll\log(2q).
\]

Thus, before any outer positive recombination, the weighted cost is

\[
 \frac{uT_Q}{q}\,Y\,\kappa\,\frac1m
 \sum_a|c_q(a)|\,X^\eta
 \ll Q\kappa u\log(2q)X^\eta.
\]

Equivalently, \(Y\) cancels the \(Y^{-1}\) in
\(T_Q\le Qmq/Y\), and the resulting \(m\) cancels the exact lift
factor \(m^{-1}\). Neither cancellation is deferred to a global
average, and no positive power of \(Y\) is hidden in an
\(X^\varepsilon\) allowance.

## 3.4 Divisor and outer-label ledger

For fixed \(u\), every ordered pair \((m,q)\) with \(mq\mid u\)
corresponds to the unique ordered factorization \(u=mqr\). Hence

\[
 \sum_{mq\mid u}\log(2q)
 \le\tau_3(u)\log(2u).
\]

There is no fourth divisor label and no coprimality between \(m\) and
\(q\) has been inserted. Using \(\kappa u\asymp L\) on live support
and elementary triple-divisor summation,

\[
\begin{aligned}
 |\mathscr S_{Y,Q}^{\sigma}|
 &\ll_\eta QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log(2u)\\
 &\ll_\eta QL^2\log^{O(1)}(2L)X^\eta.
\end{aligned}
\]

Since \(Q\le(\log(2X))^B\), \(L\ll X^{1/4}\), and the endpoint atom
bound is available with a fresh \(\eta<\varepsilon\), all displayed
logarithms are absorbed into \(X^{\varepsilon-\eta}\). This proves
(189.K7) with the full \(L,X,Q\) ledger exposed.

The \(P=1\) specialization is precisely the baseline
\(j_q(a,v)\le\lfloor U/Y\rfloor\): if the uncapped floor exceeds the
largest possible distance, the predicate is identical to its capped
version. The frozen \(P=Q\) enlargement costs the explicit factor
\(Q\), which is polylogarithmic rather than power-free.

## 3.5 Exact split and literal scope

Because \(a\) and \(v\) are units modulo odd \(q\),
\(1\le j_q(a,v)\le(q-1)/2\). Therefore the two predicates in
(189.K6) are disjoint and exhaustive, including \(T_Q=0\) and
saturation. They are inserted into the complex sum (189.K5) before a
triangle inequality. The inherited physical relation applies one
outer real part to the sum over both \(\omega=+,-\); it does not take
separate real parts or absolute values orientation by orientation.

All selectors, squarefree and allocation-coprimality masks, profiles,
floors, stars, half-weights, hard samples, crossings, endpoints,
conjugations, Fejer factors, square-root phases, positivity predicates,
affine sites, and zero extensions remain inside
\(A_{\kappa,u,mq,h,v,\omega}^{\sigma}\). The slow proof uses them only
as deletions or bounded weights and infers no support regularity.

# 4. First doubtful or unproved step

There is no doubtful step in the reviewed normalization, projective
count, saturation, \(1/m\) cancellation, \(Y\) cancellation,
coefficient mass, \(\tau_3\) count, outer power ledger, or exact
orientation-preserving split.

The first unproved mathematical step is exactly (189.K18), the stated
actual-coefficient height-variation/discrepancy input for the fast
packet. The candidate marks it as unproved and records only (189.K19),
which is larger by \(Y/(Qm)>1\). That open interface does not contaminate
the absolute proof of (189.K7).

First defect: **none**. Required repair: **none**.

# 5. Controls and outcomes

| Control | Outcome |
|---|---|
| frozen candidate hash | PASS: 03d5f66eea725f619678e30cfe211163d4d245c5529f57e853831bf31585a95b. |
| TeX/control-byte hygiene | PASS: zero CR, backspace, and NUL bytes. |
| odd \(U,m,q\) | PASS: (K185.27) gives odd \(U\); \(U=mq\) gives odd \(m,q\). |
| projective inverse and bijection | PASS: \(q\mid u\), \((u,v)=1\), and the inverse map \(b\mapsto ab^{-1}\) are exact. |
| both least-residue sides | PASS: odd \(q\) makes \(\pm r\) disjoint and gives the exact count (189.K10). |
| floor zero, cap, and saturation | PASS: empty at zero; all \(\varphi(q)\) unit slopes at \((q-1)/2\). |
| interval multiplicity \(O(uT/q)\) | PASS: \(q\mid u\) absorbs the class-count \(+1\); literal restrictions only delete. |
| affine and height atom count | PASS: \(O(Y)\cdot O(1+\kappa)\), including terminal truncation and affine \(+1\). |
| exact lift normalization | PASS: \(c_{mq}(ma)=m^{-1}c_q(a)\), with no \((m,q)=1\) assumption. |
| coefficient mass | PASS: \(\sum_a|c_q(a)|\ll\log(2q)\) in the inherited odd-\(q\) normalization. |
| \(Y\) and \(m\) cancellation | PASS: both occur at fixed \((\kappa,u,m,q)\) before the divisor sum. |
| divisor power | PASS: \(u=mqr\) gives exactly \(\tau_3(u)\), not \(\tau_4(u)\). |
| \(L,X,Q\) ledger | PASS: \(QL^2\log^{O(1)}(2L)X^\eta\ll_{B,\varepsilon}L^2X^\varepsilon\). |
| exact split and orientations | PASS: the complex identity precedes positivity and retains both orientations under one inherited outer real part. |
| literal carrier | PASS: no hidden density, periodicity, or support regularity is used. |
| fast complement scope | PASS: (189.K8) and (189.K18) remain explicitly open. |

No new numerical experiment was used. The finite Wolfram artifact is
diagnostic only and is unnecessary for the asymptotic verdict.

# 6. Dependencies and exact hashes

| Artifact | SHA-256 |
|---|---|
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/candidates/formalized_hard_m1_t1_high_h_dual_frequency_projective_reduction.md | 03d5f66eea725f619678e30cfe211163d4d245c5529f57e853831bf31585a95b |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reports/dual_height_frequency_signed_attack.md | 65636c38a3b0c3dbd4a26839dbc89daa88ef78dee5638d02d0de1192b9bdfd38 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reports/height_variation_projective_hostile_audit.md | b8ec876aebcc6668646880813bad0abf576063f58e71518d29c8e5778d371608 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reports/blind_dual_frequency_rederivation.md | 13169505840f9033fb8ddaac6eba62d12988a669127f593a8bc48438543621a3 |
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/conductor_round189_report_reconciliation.md | f7486ccf02a7fb43e1bde82e94e7da410a1d691fc8b629f2b877bc40ca6a902e |
| proofs/kernels/m9_m1_hard_top_t1_high_h_imprimitive_lift_gcd_reduction.md | ca313d2ed11884bdb3ff237c51380de7aadd713a5dc01b565935fbdb8fe9744a |
| proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md | 4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160 |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml (starting graph) | 338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c |
| state/active_campaign.yml | 4d8661258570c3152d464f38d76798f1aadd271e9f4e221c80011d3ec60d68f5 |

The Round-188 kernel supplies the unique lift, exact \(1/m\)
normalization, coefficient mass, and inherited complex complement. The
Round-185 kernel supplies the literal carrier, odd \(U\), common
\(u,v\asymp L/\kappa\) support, canonical orientations, and
\(O(1+\kappa)\) affine multiplicity. The three reports and current
reconciliation agree with the candidate on every reviewed formula. No
external theorem or unlisted support regularity is used.

# 7. Recommended state effect

Promote the formal candidate's narrow proved content after the remaining
scheduled independent seams are GREEN, under the Round-189 exit label
strict_dual_height_resonance_sector. The promotable statement is only
the exact projective bijection, capped \(P=Q\) slow sector, absolute
bound (189.K7), and its exact complex complement.

Retain (189.K8) and (189.K18) as open. Make no status change to the
complete high-height relation, complete original-\(t=1\) residual, any
original \(t\ge2\) or large-\(G\) near-resonant component, either M1
parent, GAR, any M2 parent, endpoint uniformity, M9, either bridge, the
Gauss-circle target, or any exponent.
