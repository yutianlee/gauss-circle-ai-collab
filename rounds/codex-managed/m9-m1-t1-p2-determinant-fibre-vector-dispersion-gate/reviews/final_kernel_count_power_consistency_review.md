# Final kernel count and power consistency review

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Round: 195
- Role: final independent kernel consistency review
- Final candidate SHA-256:
  81198f76dfbad6d81fc4ed88d7582ff70ce200f755b82228b6eb4650c4996d72
- Kernel SHA-256:
  4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009

## 1. Result

**Verdict: PASS.**

The durable kernel is an exact mathematical copy of the final candidate.
The only differences are the intended title, candidate/kernel status and
hash metadata, and the Section-7 heading and proof-state wording.  After
normalizing only those differences in memory, the kernel bytes equal the
candidate bytes exactly and have the candidate SHA-256 shown above.

Both absolute-capacity sectors, the exact packet complement
\(\mathcal P_{\rm rem}\), and the fixed-to-outer \(L^2X^\varepsilon\)
ledger remain valid and unchanged.

## 2. Exact statement and hypotheses

The kernel retains the exact physical split
\[
 P_2=P_{2,\ge D_L}+P_{2,<D_L},
\]
where
\[
 P_{2,\ge D_L}=P_2\mathbf1_{\{\kappa\ge D_L\}}.
\]
For a fixed packet
\[
 p=(\kappa,u,\mathfrak m,q,a,J,Y,\sigma),
\]
the small-\(\kappa\) packets split exactly as
\[
 \mathcal P_{\rm cap}
 =\{p:\kappa<D_L,\ \min(Y,D_L)\le H_B\mathfrak m\kappa\},
\]
\[
 \mathcal P_{\rm rem}
 =\{p:\kappa<D_L,\ \min(Y,D_L)>H_B\mathfrak m\kappa\}.
\]
Equality belongs to the safe sector, so these sets are disjoint and
exhaust all small-\(\kappa\) packets.

The kernel asserts only:
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,\ge D_L}W)|
 \ll H_B\mathfrak m\kappa uX^\varepsilon,
\]
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D_L}W)|
 \ll H_B\mathfrak m\kappa uX^\varepsilon
 \quad(p\in\mathcal P_{\rm cap}),
\]
and the corresponding outer \(L^2X^\varepsilon\) estimate for their
union.  It leaves \(P_{2,<D_L}\cap\mathcal P_{\rm rem}\) open.

## 3. Proof and line-by-line verification

### 3.1 Exact copy check

A direct line diff found only four intended regions:

1. the kernel title omits “Formal candidate”;
2. one candidate-status line is replaced by the formal-candidate hash and
   kernel-status lines;
3. the Section-7 heading becomes “Dependencies and proof-state boundary”;
4. its introductory sentence is changed from a proposed effect to the
   exact effect supported by the kernel.

Replacing only those four regions in memory produced byte-for-byte
equality with the final candidate.  The normalized kernel SHA-256 was
\[
 81198f76dfbad6d81fc4ed88d7582ff70ce200f755b82228b6eb4650c4996d72,
\]
exactly the final candidate hash.  Thus no formula, hypothesis, proof
step, complement, power, scope statement, or exponent changed.

### 3.2 Large-\(\kappa\) sector

In each orientation, after \((\kappa,g,U,v)\) is fixed, lower closeness
leaves \(O(D_L)\) choices for one affine variable and the determinant
range leaves \(O(1)\) choices for the other.  Hence
\[
 D_L\sum_{\kappa\ge D_L}(1+L/\kappa)^2\ll L^2.
\]
At fixed packet there are \(O(D_L)\) atoms per row,
\(O(uJ/q)\) rows, and Abel costs \(q/J\), giving \(O(D_Lu)\).
Adding the accepted \(O(\kappa u)\) terminal and Fejer cost and using
\(\kappa\ge D_L\) proves the fixed target.  Physical-source counting
before Fourier, followed by deletion-stable recomputation of the masked
core, proves the outer target.

### 3.3 Small-\(\kappa\) absolute-capacity sector

For \(\kappa<D_L\), primitivity gives one close residue class per row and
height, so the fixed-height count is \(O(Yu)\) after the exact
\((q/J)(uJ/q)\) cancellation.  The independent all-height determinant
count is \(O(D_Lu)\).  Both estimates include the same
\(O(\kappa u)\) accepted safe cost; therefore
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D_L}W)|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon.
\]
On \(\mathcal P_{\rm cap}\),
\[
 \kappa+\min(Y,D_L)
 \ll H_B\mathfrak m\kappa,
\]
which is exactly the fixed-packet target.  On
\(\mathcal P_{\rm rem}\), the unresolved capacity multiplier remains
\[
 {\min(Y,D_L)\over H_B\mathfrak m\kappa}>1;
\]
the kernel does not claim to recover it.

### 3.4 Fixed-to-outer power

The spectral lift weight \(\mathfrak m^{-1}\) cancels the
\(\mathfrak m\) in the fixed target.  Anchor mass, dyadic bands, and
divisor choices give only logarithms and \(\tau_3(u)\), leaving
\[
 H_BX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\]
Restricting this positive majorant to the two safe sectors only deletes
terms.  No \(Y,D_L,q,J,U,\mathfrak m\), or far-defect power is hidden.

## 4. First doubtful or unproved step

There is no doubtful or unproved step in the two promoted
absolute-capacity sectors or their outer ledger.

The first open step is exactly the kernel's quarantined
coefficient-sensitive cross-row four-block Gram estimate on
\[
 P_{2,<D_L}\cap\mathcal P_{\rm rem}.
\]
The kernel calls this a remaining seam, not a proved estimate or literal
lower bound.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| candidate/kernel line consistency | PASS.  Normalization of only the intended four regions gives exact byte equality. |
| both-orientation large-\(\kappa\) count | PASS.  The \(O(D_L)\)-by-\(O(1)\) count is unchanged. |
| fixed-packet anchor ledger | PASS.  \(q/J\) cancels \(J/q\) explicitly. |
| masked-operator deletion stability | PASS.  The transported mask commutator and all new births/deaths remain in the core. |
| small-\(\kappa\) minimum bound | PASS.  The fixed-height and all-height bounds apply to the same operator. |
| exact \(\mathcal P_{\rm rem}\) | PASS.  Equality is safe; the strict reverse is the sole packet complement. |
| spectral lift and divisor ledger | PASS.  \(\mathfrak m^{-1}\) cancels \(\mathfrak m\), and the remaining sum is \(L^2\) up to logarithms. |
| outer safe-union scope | PASS.  Packet restriction only deletes terms from the positive outer majorant. |
| theorem and exponent quarantine | PASS.  Complete \(P_2\), every parent and bridge, the target, and all exponents remain unchanged. |

## 6. Exact dependencies and artifacts used

1. Final candidate:
   rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/candidates/formalized_hard_m1_t1_p2_large_kappa_sector.md —
   81198f76dfbad6d81fc4ed88d7582ff70ce200f755b82228b6eb4650c4996d72.
2. Durable kernel:
   proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md —
   4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009.

No other artifact was needed for this final copy, count, and power check.
No file other than this review was edited.

## 7. Recommended state effect

Pass the durable kernel through the final count/power/consistency gate at
SHA-256
4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009.
It supports only the subordinate proved-internal absolute-capacity
sectors and the exact open complement recorded above.  It does not support
closing complete \(P_2\), any owner or parent, M9, either bridge, the
Gauss-circle target, or any exponent.
