# Round 172 parity post-repair verification

Campaign: m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate  
Role: post-repair finite-seam verifier  
Date: 2026-08-26  
Verdict: **GREEN**

## 1. Result

The repaired discovery and blind reports now satisfy every correction
requested by the parity--dyadic endpoint seam review.

1. Discovery defines $S=\min(2R_0,M)$ and states its first-link estimate
   for $R_0\to S$, including the terminal non-doubling case
   $S=M<2R_0$.
2. The former affirmative “owner-complete strict sector” language is gone.
   Discovery now explicitly says that the local link is uncomplemented,
   its complement is not target-safe, and it is not an owner-complete
   strict sector or a strict-sector promotion.
3. The former out-of-range (172.D22) control has been replaced by the
   in-range $M=4P$ construction, aligned with hostile (172.H15). Its
   support, correlation, tent weights, full-energy normalization, and exact
   value $P^2=MD/8$ all check.
4. Blind now distinguishes the frozen one-sided gate (FG) from the stronger
   absolute-value sufficient condition (MF), and no longer calls (MF)
   equivalent, necessary, or unique.

No further repair is needed on these four seams.

## 2. Exact statement and hypotheses

For the first stopped link, let

\[
 S=\min(2R_0,M),\qquad R_0<M,\qquad
 D_L=\sum_N|z_N|^2.
\]

For the parity-projected Fejer energy,

\[
 0\le \mathfrak E_R^{(2)}\le RD_L.
\]

For the repaired hostile control, take $M=4P$, $R=2P$, and put $z_N=1$
on the $2P$ even sites of an $M$-site interval. Then

\[
 D=2P,\qquad A_{2s}=2P-s\quad(1\le s<2P).
\]

The frozen link statement is the signed one-sided upper bound

\[
 \mathfrak M_{R,S}(c)\ll_\varepsilon L^3X^\varepsilon,
 \tag{FG}
\]

whereas

\[
 |\mathfrak M_{R,S}(c)|
 \ll_\varepsilon L^3X^\varepsilon
 \tag{MF}
\]

is only a stronger sufficient condition.

## 3. Proof or derivation

Because $S\le2R_0$,

\[
\begin{aligned}
 |\mathfrak E_S^{(2)}-\mathfrak E_{R_0}^{(2)}|
 &\le \mathfrak E_S^{(2)}+\mathfrak E_{R_0}^{(2)}\\
 &\le (S+R_0)D_L
 \le3R_0D_L
 \ll_\varepsilon L^3X^\varepsilon.
\end{aligned}
\]

Thus repaired (172.D1) is valid for both an exact doubling and
$S=M<2R_0$. Discovery also correctly confines the Haar identity to exact
doublings and invokes the terminal weight (172.D10) in the latter case.
The estimate is a coefficient-uniform local bound; it does not make the
unsafe complement disappear.

For the repaired control, the sites

\[
 0,2,\ldots,4P-2
\]

lie in the containing interval $[0,4P-1]$. For the terminal doubling
$2P\to4P$,

\[
\begin{aligned}
 \Delta_{2P,4P}
 &=2\sum_{s=1}^{2P-1}b_{2P,4P}(2s)(2P-s)\\
 &=\frac1P\left\{
 \sum_{s=1}^{P-1}s(2P-s)
 +\sum_{s=P}^{2P-1}(2P-s)^2
 \right\}\\
 &=P^2.
\end{aligned}
\]

Since $MD=(4P)(2P)=8P^2$, this is exactly $MD/8$, not merely an
order-of-magnitude lower bound. The factor $2$ in the first line confirms
that $\Delta$ is the full Fejer-energy increment. This matches the hostile
construction and cures the former containing-interval defect in
(172.D22).

Blind now states (FG) and (MF) separately, explicitly records
$(\mathrm{MF})\Rightarrow(\mathrm{FG})$ but not conversely, and limits the
absolute Haar equivalence to (MF). Its common-frequency discussion also
asks only for an upper bound when targeting (FG). The repaired logical
scope is exact.

## 4. First doubtful or unproved step

There is no remaining doubt in the repaired parity, endpoint, first-link,
control, or MF-scope seams.

The first open mathematical step is the actual-coefficient signed,
one-sided estimate for every remaining large stopped-dyadic link. In the
discovery normalization, after the paid first link, short correction, and
ordinary zero modes, this is the nonzero-mode aggregate (172.D23):

\[
 \Re(\text{complete signed nonzero dual aggregate})
 \ll_\varepsilon L^3X^\varepsilon
\]

before any modulus or positive summation. No reviewed repair proves that
estimate.

## 5. Required control tests and outcomes

| Repair gate | Outcome |
|---|---|
| $S=\min(2R_0,M)$ | **PASS.** Present in discovery Result and Recommendation; terminal non-doubling case is explicit. |
| first-link normalization | **PASS.** $(S+R_0)D_L\le3R_0D_L$ is valid, though not the sharpest available bound. |
| owner-complete language | **PASS.** No affirmative promotion remains; discovery explicitly denies owner-completeness. |
| containing interval | **PASS.** Exactly $2P$ even sites fit inside the stated $M=4P$ interval. |
| H15/D22 correlation | **PASS.** $A_{2s}=2P-s$ for $1\le s<2P$. |
| H15/D22 full increment | **PASS.** Exact value is $P^2=MD/8$. |
| MF versus frozen gate | **PASS.** Blind labels MF strictly stronger and non-necessary. |
| finite identities changed by repair | **PASS.** None was altered. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

Only these artifacts were read:

1. reports/blind_maximal_fejer_dyadic_rederivation.md;
2. reports/literal_maximal_fejer_dyadic_frequency_attack.md;
3. reviews/parity_dyadic_endpoint_seam_review.md.

All paths are relative to the current Round-172 campaign directory. No
state, synthesis, validation, source, or external artifact was read or
edited.

## 7. Recommended state effect

**GREEN: retain the repaired reports as candidate evidence with no further
finite-seam repair.** The local first-link estimate remains
uncomplemented, the in-range dechirped array remains only a false control,
and MF remains only a stronger sufficient condition.

Make no proof-graph promotion from this verification. The first remaining
doubt is the unproved actual-coefficient, signed, one-sided
$L^3X^\varepsilon$ estimate for the complete large-link aggregate before
positivity.
