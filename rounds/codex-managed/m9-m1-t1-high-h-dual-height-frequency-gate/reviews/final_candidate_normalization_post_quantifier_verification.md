# 1. Result and verdict

- Campaign: m9-m1-t1-high-h-dual-height-frequency-gate
- Round: 189
- Verification: final candidate normalization after K18 quantifier repair
- Previous candidate SHA-256:
  03d5f66eea725f619678e30cfe211163d4d245c5529f57e853831bf31585a95b
- Current candidate SHA-256:
  123d697198c3c20d710fe5880db75f09423ff457820694dd8671e5b8564e1e28
- Verdict: **GREEN**

The current candidate differs from the previously reviewed candidate
only by the stated admissible-\(a\), complementary-dyadic-\(J\)
quantifier immediately before the unproved relation (189.K18). The
formula (189.K18), every proved formula (189.K1)--(189.K17), and every
formula after (189.K18) are byte-identical. The prior GREEN verdict on
normalization, projective multiplicity, power bookkeeping, and the
exact split is unchanged.

# 2. Exact delta

In the previous candidate, the prose immediately before (189.K18) was

> The first target-scaled sufficient input is

In the current candidate, that prose is exactly

> Uniformly for every fixed admissible
> \(a\in(\mathbb Z/q\mathbb Z)^\times\) with \(m|a|_q>Q\), and every
> complementary dyadic \(J\)-band, the first target-scaled sufficient
> input is

The replacement occurs once. Its old byte length is 43, its new byte
length is 180, and the file grows by exactly 137 bytes, from 10020 to
10157 bytes. The replacement starts at byte offset 6277. Replacing this
single current passage in memory by the previous passage produces
exactly 10020 bytes and SHA-256
03d5f66eea725f619678e30cfe211163d4d245c5529f57e853831bf31585a95b.
This hash equality proves that there is no other byte drift.

# 3. Mathematical replay

The new quantifier is correct. In (189.K5), \(a\) is already restricted
by

\[
 a\in(\mathbb Z/q\mathbb Z)^\times,\qquad m|a|_q>Q.
\]

The fast packet is already defined by \(j_q(a,v)>T_Q(m,q;Y)\), and its
dyadic decomposition uses complementary \(J\)-bands. Hence (189.K18)
is properly read for each fixed admissible \(a\) and each such band:

\[
 \sum_{\substack{\omega,\ v\ {\rm literal}\\
                  J\le j_q(a,v)<2J}}
 \mathsf V(W_{\kappa,u,mq,v,\omega}^{\sigma})
 \ll_\eta \frac{Qm\kappa uJ}{q}X^\eta.
\]

The quantifier changes no assertion from proved to unproved or vice
versa. Relation (189.K18) remains explicitly sufficient and unproved.

All reviewed proved seams precede this insertion and are unchanged:

1. \(U,m,q\) are odd, \(q\mid U\mid u\), and \((u,v)=1\).
2. \(v\mapsto a\bar v_q\) is a unit-class bijection.
3. Both least-residue sides give
   \(2\sum_{1\le r\le T,(r,q)=1}1\), including \(T=0\) and saturation.
4. The literal count is \(O(uT_Q/q)\le O(Qum/Y)\).
5. \(O(Y)\) heights and \(O(1+\kappa)\) affine sites combine with
   \(c_{mq}(ma)=m^{-1}c_q(a)\) to cancel \(Y\) and \(m\) before outer
   recombination.
6. \(\sum_a|c_q(a)|\ll\log(2q)\),
   \(\sum_{mq\mid u}1=\tau_3(u)\), and the inherited
   \(L\ll X^{1/4}\) yield
   \(QL^2\log^{O(1)}(2L)X^\eta\ll L^2X^\varepsilon\).
7. The slow/fast split remains a complex identity before positivity,
   with both orientations under one inherited outer real part.

# 4. First doubtful or unproved step

The first unproved step remains (189.K18). The added quantifier removes
an ambiguity about which \(a\) and \(J\) are held fixed; it supplies no
new estimate and assumes no regularity of the literal coefficient.

There is no defect in the quantifier repair and no new doubtful step in
the previously GREEN normalization/projective/power proof.

# 5. Controls

| Control | Outcome |
|---|---|
| current candidate hash | PASS: 123d697198c3c20d710fe5880db75f09423ff457820694dd8671e5b8564e1e28. |
| operation-derived reverse | PASS: one exact passage replacement recovers SHA-256 03d5f66eea725f619678e30cfe211163d4d245c5529f57e853831bf31585a95b. |
| byte-count delta | PASS: \(10157-10020=137=180-43\). |
| occurrence count | PASS: the new passage occurs exactly once. |
| formula preservation | PASS: (189.K18) itself and all K-formulas are unchanged. |
| normalization/projective proof | PASS: (189.K2)--(189.K15) are unchanged. |
| split and orientation scope | PASS: (189.K5)--(189.K8) are unchanged. |
| proved/open boundary | PASS: (189.K7) remains proved; (189.K8) and (189.K18) remain open. |
| file hygiene | PASS: strict UTF-8/LF; zero CR, backspace, and NUL bytes. |

No numerical evidence was used.

# 6. Dependencies and hashes

| Artifact | SHA-256 |
|---|---|
| current formal candidate | 123d697198c3c20d710fe5880db75f09423ff457820694dd8671e5b8564e1e28 |
| reconstructed previous formal candidate | 03d5f66eea725f619678e30cfe211163d4d245c5529f57e853831bf31585a95b |
| reviews/dual_frequency_normalization_projective_power_seam_review.md | 5af4ffb3fd3da05287cf217a9ffad412dd888aea716686466bd76fe90c4b8b95 |
| proofs/kernels/m9_m1_hard_top_t1_high_h_imprimitive_lift_gcd_reduction.md | ca313d2ed11884bdb3ff237c51380de7aadd713a5dc01b565935fbdb8fe9744a |

The previous bytes were reconstructed only in memory by reversing the
single declared passage replacement. No candidate, kernel, or state
file was modified.

# 7. Recommended state effect

Retain the prior **GREEN** normalization/projective/power verdict with
no repair. The candidate remains eligible for promotion only in its
narrow scope: the exact capped projective slow sector and its exact
complex complement. Keep (189.K8) and (189.K18) open, and make no
downstream parent, bridge, theorem, or exponent change from this
verification.
