# Absolute-capacity sector and power post-repair review

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Round: 195
- Role: independent absolute-capacity and outer-power review
- Candidate SHA-256:
  cd0230f22b31f3454c975cf8b8625026687adba97a0d180e2556156bd990d0d7
- Reconciliation SHA-256:
  3ff78bbb5f491ec4dfb30ae05123dfcecf8a93e38e17d7fee1c124c5c45b9436

## 1. Result

**Verdict: PASS.**

For every fixed packet with \(1\le\kappa<D_L\), the current candidate
correctly proves
\[
 \left|\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)\right|
 \ll_\varepsilon
 u\{\kappa+\min(Y,D_L)\}X^\varepsilon.
\tag{R1}
\]
Consequently the exact packet sector
\[
 \kappa<D_L,\qquad
 \min(Y,D_L)\le H_B\mathfrak m\kappa
\tag{R2}
\]
is target-safe, and its exact small-\(\kappa\) packet complement is
\[
 \kappa<D_L,\qquad
 \min(Y,D_L)>H_B\mathfrak m\kappa.
\tag{R3}
\]
The accepted lift/divisor assembly of the fixed target gives an outer
\(O(L^2X^\varepsilon)\) bound after restriction to (R2).  The pre-existing
theorem for every \(\kappa\ge D_L\) remains separate and unchanged in
content: its both-orientation physical count, fixed-packet \(q/J\) ledger,
masked-operator passage, and direct outer \(L^2\) proof do not use (R2).

## 2. Exact statement and hypotheses

Write
\[
 Q=H_B,\qquad D=D_L=\lceil\sqrt L\rceil,\qquad
 M=\min(Y,D).
\tag{R4}
\]
Retain the candidate's complete Round-192 packet, including
\[
 U=\mathfrak m q,\qquad u=gU,\qquad
 (u,v)=1,\qquad Q\mathfrak m<Y,
\tag{R5}
\]
the literal endpoint shells, both primitive orientations, both frequency
signs, the \(T=0/T\ge1\) convention, every endpoint and residual field,
the physical-mask commutator, and one outer real part.

The physical mask is still
\[
 P_2=\mathbf1_{\{|d-gm|\le D\}}
     \mathbf1_{\{|d'-gm'|>D\}},
\tag{R6}
\]
with the exact physical split
\[
 P_2=P_{2,\ge D}+P_{2,<D}.
\tag{R7}
\]
Only after fixing a small-\(\kappa\) spectral packet is
\(P_{2,<D}\) partitioned by \(M\le Q\mathfrak m\kappa\) or its strict
reverse.  Thus (R2)--(R3) are an exact packet partition, not an additional
physical mask inserted before Fourier expansion.

## 3. Proof and independent derivation

### 3.1 Fixed-height capacity

Fix a packet, one literal projective row, and one height \(h\).  In the
plus chart,
\[
 h=Sv-Uw,\qquad (U,v)=1.
\tag{R8}
\]
For fixed \(h\), the possible \(w\)'s lie in one residue class modulo
\(v\).  Lower closeness confines \(w\) to an interval of length
\(O(D)\), so the number of sites is
\[
 O(1+D/v)=O(1+\kappa D/L)=O(1)
 \qquad(\kappa<D),
\tag{R9}
\]
using \(v\asymp L/\kappa\).  In the minus chart,
\[
 h=Uw-vS,
\tag{R10}
\]
and the possible \(S\)'s lie in one residue class modulo \(U\).
Since \(g=O(1)\) and \(U\asymp L/\kappa\), the same bound (R9) holds.

There are \(O(Y)\) heights and \(O(uJ/q)\) projective rows.  Exact Abel
return costs at most \(q/J\).  Hence the complete masked source part of
the fixed packet is
\[
 \ll (q/J)(uJ/q)YX^\varepsilon
 \ll YuX^\varepsilon.
\tag{R11}
\]
The accepted terminal and Fejer projections add
\(O(\kappa uX^\varepsilon)\); the inverse-small set is disjoint from the
core and the Farey projector only deletes rows.  This proves
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll u(\kappa+Y)X^\varepsilon.
\tag{R12}
\]

### 3.2 All-height determinant capacity

There is an independent estimate for the same exact packet.  At fixed
\((\kappa,g,U,v)\), in the plus orientation lower closeness leaves
\(O(D)\) values of \(w\), and the full determinant range
\[
 0<Sv-Uw<R_0/(2\kappa g)
\tag{R13}
\]
leaves \(O(1)\) values of \(S\) for each \(w\), because
\(\kappa v\asymp L\).  In the minus orientation lower closeness leaves
\(O(D)\) values of \(S\), and the corresponding determinant interval
leaves \(O(1)\) values of \(w\), because \(\kappa gU\asymp L\).
Thus there are \(O(D)\) atoms per row over the entire height range.

The same projective-density and Abel factors give
\[
 \ll(q/J)(uJ/q)DX^\varepsilon
 \ll DuX^\varepsilon
\tag{R14}
\]
for the masked source part.  Adding the same accepted safe projections,
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll u(\kappa+D)X^\varepsilon.
\tag{R15}
\]
Both (R12) and (R15) bound the identical literal packet, so taking the
smaller right side gives
\[
 \min\{\kappa+Y,\kappa+D\}
 =\kappa+\min(Y,D),
\tag{R16}
\]
which proves (R1).  No cancellation or coefficient replacement enters
this minimum.

### 3.3 Target-safe packet sector and exact complement

On (R2),
\[
 \kappa+M
 \le(1+Q\mathfrak m)\kappa
 \le2Q\mathfrak m\kappa,
\tag{R17}
\]
because \(Q\mathfrak m\ge1\).  Inserting (R17) into (R1) proves
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll Q\mathfrak m\kappa uX^\varepsilon.
\tag{R18}
\]
Equality in \(M=Q\mathfrak m\kappa\) belongs to the safe sector; hence
the strict reverse inequality (R3) is exactly its complement among
small-\(\kappa\) packets.  Together with all \(\kappa\ge D\), this gives
the candidate's exact safe union and one exact open packet complement.

### 3.4 Fixed-to-outer power ledger

Apply (R18) only to the safe packet set.  The exact spectral lift weight
\(\mathfrak m^{-1}\) cancels \(\mathfrak m\) before the positive outer
sum.  The anchor coefficient mass, dyadic \(J\)-bands, and divisor choices
cost only logarithms and
\(\tau_3(u)\).  The resulting majorant is
\[
 QX^\eta
 \sum_{\kappa\ll L}
 \sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log^{O(1)}(2u).
\tag{R19}
\]
For fixed \(\kappa\), the elementary average triple-divisor bound gives
\[
 \sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log^{O(1)}(2u)
 \ll {L^2\over\kappa}\log^{O(1)}(2L);
\tag{R20}
\]
therefore (R19) is
\[
 \ll QL^2X^\eta\log^{O(1)}(2L)
 \ll_{B,\varepsilon}L^2X^\varepsilon
\tag{R21}
\]
after the fresh epsilon split.  Restricting to (R2) only deletes terms
from this positive majorant.  No \(Y,D,q,J,U,\mathfrak m\), or far-bin
power remains.

### 3.5 Preservation of the large-\(\kappa\) theorem

The current candidate's large-\(\kappa\) proof still uses exactly:

1. \(O(D)\) choices for the close variable and \(O(1)\) for the
   determinant variable in each orientation;
2. \(D\sum_{\kappa\ge D}(1+L/\kappa)^2\ll L^2\);
3. \(O(D)\) atoms per fixed row, followed by
   \((q/J)(uJ/q)=u\);
4. the accepted \(O(\kappa uX^\varepsilon)\) terminal/Fejer cost and
   \(D\le\kappa\); and
5. physical-source counting before Fourier, followed by deletion-stable
   recomputation of the exact core.

The new packet condition (R2) occurs only for \(\kappa<D\) and is not
used in any of these five steps.  Thus the whole
\(P_{2,\ge D}\) fixed and outer theorem is semantically unchanged.

## 4. First doubtful or unproved step

There is no doubtful or unproved step in the absolute-capacity sector or
its outer ledger.

On the exact open packet region (R3), the remaining positive-capacity
multiplier is
\[
 {M\over Q\mathfrak m\kappa}>1.
\tag{R22}
\]
Recovering it requires the candidate's stated coefficient-sensitive
cross-row four-block Gram estimate.  The current candidate explicitly
leaves that step open, so it does not affect this PASS verdict.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| fixed-height residue-class count | PASS.  Each orientation has \(O(1)\) close sites per row and height for \(\kappa<D\). |
| all-height determinant count | PASS.  Each orientation has \(O(D)\) atoms per row over the full range. |
| identical-operator minimum | PASS.  The two bounds apply to the same literal packet, giving \(\kappa+\min(Y,D)\). |
| anchor \(q/J\) ledger | PASS.  It cancels \(uJ/q\) in both counts and is not absorbed into epsilon. |
| terminal/Fejer and core passage | PASS.  Both estimates add the same accepted \(O(\kappa u)\) term and retain mask jumps in the core. |
| target normalization | PASS.  \(M\le Q\mathfrak m\kappa\) implies (R18), with an absolute factor two. |
| exact packet complement | PASS.  Equality is safe and the strict reverse is the sole small-\(\kappa\) remainder. |
| spectral lift cancellation | PASS.  \(\mathfrak m^{-1}\) cancels the fixed-target \(\mathfrak m\) before summation. |
| divisor and shell sum | PASS.  Equations (R19)--(R21) restore the outer \(L^2\) scale. |
| large-\(\kappa\) preservation | PASS.  Its proof and scope do not use the new small-\(\kappa\) condition. |
| scope and exponent quarantine | PASS.  Complete \(P_2\), every parent and bridge, the target, and all exponents remain unchanged. |

## 6. Exact dependencies and artifacts used

Only the two assigned current artifacts were read:

1. rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/candidates/formalized_hard_m1_t1_p2_large_kappa_sector.md —
   cd0230f22b31f3454c975cf8b8625026687adba97a0d180e2556156bd990d0d7;
2. rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/conductor_round195_report_reconciliation.md —
   3ff78bbb5f491ec4dfb30ae05123dfcecf8a93e38e17d7fee1c124c5c45b9436.

No other artifact, computation, web source, or current state file was read
or used for this bounded review.

## 7. Recommended state effect

Pass the broadened absolute-capacity candidate through this sector and
power gate at the hashes in Section 6.  Subject to all remaining declared
reviews, the subordinate evidence may record:

- every \(P_2\) packet with \(\kappa\ge D_L\);
- every small-\(\kappa\) packet with
  \(\min(Y,D_L)\le H_B\mathfrak m\kappa\); and
- the single exact open packet complement (R3).

Do not promote complete \(P_2\), the hard-M1 owner, any parent, M9, either
bridge, the Gauss-circle target, or any exponent.
