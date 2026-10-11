# Round217 — isolated rederivation of the distinct-label positive certificate

- Campaign: `gc-full-goal-distinct-source-review`; round: 217.
- Role: statement-only independent seam reviewer; task: `isolated_distinct_certificate_rederivation`.
- Generated: 2026-09-28T02:40:38+08:00.
- Supplied graph SHA256: `f7c8b74e9acaa3bf5234c3678f20e2aaf8dbb9ba6179f73d839fa2f0537a14d7` (inherited metadata only; graph not read).
- Original reviewer report remains frozen at SHA256 `fe681f61a48faac2825138c8b7e0884e4f73c05b6cca789cb0f72b9f33e49e35` and was not edited.
- Isolation: only the protocol, the previously permitted isolated context, and the new statement packet were available. No claimant proof, graph, ledger, strategy, control file, source, or sibling report was inspected.
- Resources: analytical proof only; zero experiments.

## 1. Result

**The proposed lower bound is valid asymptotically under exactly the stated abstract hypotheses.** For every fixed even (p=2k\ge4),

\[
\boxed{\mathcal C_p(T)\gg_{p,c,W,\text{hypothesis constants}}
                  T^{p/4-1/2}}
\]

for all sufficiently large real (T\). No assumption on how labels are distributed along the integer interval is needed.

The decisive estimate includes every close tuple with any repeated label. If (b_* =\max_n b_n), (B_\ell=\sum_{\ell(n)=\ell}b_n), and (S=\sum_\ell B_\ell^2), that total repeated-label mass is at most

\[
\binom p2 b_* S M^{p-3}
\ll_{p,\eta}T^{p/4-2+2\eta}.
\tag{1}
\]

The total close mass furnished by weighted Cauchy is \(\gg T^{p/4-3/2}\), so any fixed \(0<\eta<1/4\) makes the subtraction negligible. The factor (T2^{-p}\) in the certificate then gives the claimed power.

This is a lower bound for the stated nonnegative certificate. It is not a lower bound for a signed sum.

## 2. Exact statement and hypotheses

For each real (T\ge2\), let \(\mathcal N_T\subset\mathbb Z\cap[cT,2cT]\), with fixed (c>0\). The weights \(b_n\ge0\) and labels \(\ell(n)\) satisfy

\[
aT^{1/4}\le M=\sum_{n\in\mathcal N_T}b_n\le AT^{1/4}
\]

with constants (a,A>0\), and, for every \(\eta>0\),

\[
b_*\le K_\eta T^{-3/4+\eta},qquad
S=\sum_\ell B_\ell^2\le L_\eta T^{-1/2+\eta}.
\]

The constants may depend on the chosen \(\eta\), but not on (T\). The finite active label set can be arbitrary and can change with (T\). Let (W\) be continuous with \(|W(0)|>0\), and let (p=2k\ge4\) be fixed. Define

\[
\mathcal C_p(T)=T2^{-p}
\sum_{\substack{n_1,\ldots,n_p\in\mathcal N_T\\
                \ell(n_1),\ldots,\ell(n_p)\text{ pairwise distinct}}}
\left(\prod_{j=1}^p b_{n_j}\right)
\left|W\!\left(T\left[\sum_{j\le k}\sqrt{n_j}
                         -\sum_{j>k}\sqrt{n_j}\right]\right)\right|.
\]

The conclusion holds for all (T\ge T_0\), with (T_0\) depending on the fixed data and the constants in the assumptions. This is the usual asymptotic meaning of \(\gg\). A positive lower bound for every individual (T\ge2\), including arbitrarily prescribed bounded-(T\) data, is not forced: finitely many small-(T\) instances may have fewer than (p\) active labels. No such bounded-(T\) exception affects the asserted asymptotic conclusion.

No Fourier representation, cancellation law, arithmetic origin, independence property, regular spacing of labels, or uniformity in growing (p\) is assumed.

## 3. Proof

### 3.1 A positive neighborhood and bins for ordered half-tuples

By continuity choose fixed numbers \(\delta>0\) and \(w_0>0\) such that

\[
|W(x)|\ge w_0\qquad (|x|\le\delta).
\tag{2}
\]

For an ordered (k\)-tuple \(\mathbf u=(u_1,\ldots,u_k)\in\mathcal N_T^k\), repetitions allowed for the moment, define

\[
s(\mathbf u)=\sum_{i=1}^k\sqrt{u_i},\qquad
b(\mathbf u)=\prod_{i=1}^k b_{u_i}.
\]

Its sum lies in the closed interval

\[
[L_T,U_T]=[k\sqrt{cT},\ k\sqrt{2cT}],
\quad
U_T-L_T=D\sqrt T,
\quad D=k(\sqrt{2c}-\sqrt c)>0.
\]

Partition this interval using half-open bins of width \(h=\delta/T\), starting at (L_T\). Use indices

\[
0\le i\le \left\lfloor\frac{U_T-L_T}{h}\right\rfloor.
\]

The last bin may extend beyond (U_T\). In particular, if the upper endpoint lies exactly on a bin boundary, its bin is still included. Every half-tuple belongs to exactly one bin, including tuples at the real endpoints. The number of bins is

\[
J=1+\left\lfloor\frac D\delta T^{3/2}\right\rfloor
\le(1+D/\delta)T^{3/2}
\qquad(T\ge1).
\tag{3}
\]

Let

\[
P_i=\sum_{\mathbf u:\ s(\mathbf u)\text{ in bin }i}b(\mathbf u).
\]

All these numbers are nonnegative, and

\[
\sum_i P_i=M^k.
\]

Weighted Cauchy therefore gives

\[
\sum_iP_i^2\ge\frac{M^{2k}}J=\frac{M^p}J
\gg T^{p/4-3/2}.
\tag{4}
\]

The left side is exactly the product-weighted mass of ordered (p\)-tuples whose first ordered half and second ordered half lie in the same bin. Each such tuple satisfies

\[
\left|\sum_{j\le k}\sqrt{n_j}-\sum_{j>k}\sqrt{n_j}\right|
<\delta/T.
\tag{5}
\]

There is no division by (k!\), (p!\), or any permutation multiplicity. Each ordered (p\)-tuple has one ordered first half and one ordered second half, and contributes once to the applicable bin square. This matches the order convention in the proposed certificate.

### 3.2 All close tuples with repeated labels

Write \(\sigma_j=1\) for (j\le k\) and \(\sigma_j=-1\) for (j>k\). Define the unweighted-by-(W\), product-weighted bad mass

\[
\mathcal B(T)=
\sum_{\substack{\mathbf n\in\mathcal N_T^p\\
                |\sum_j\sigma_j\sqrt{n_j}|\le\delta/T\\
                \exists a<b:\ \ell(n_a)=\ell(n_b)}}
\prod_{j=1}^p b_{n_j}.
\tag{6}
\]

This includes all close repeated-label tuples, whether or not their half-sums belong to the same bin. It includes a repeated label within either half, across the two halves, repeated integer indices, and arbitrarily many simultaneous repeated labels.

Fix one position pair (a<b\). Choose an index (j\notin\{a,b\}\), possible because (p\ge4\). Fix all variables except (n_j\), retaining the constraint \(\ell(n_a)=\ell(n_b)\). The close-sum constraint forces \(\sqrt{n_j}\) into an interval of length at most \(2\delta/T\), regardless of the sign \(\sigma_j\).

There is at most one possible integer (n_j\in[cT,2cT]\) for all sufficiently large real (T\). Indeed, if two distinct integers (u<v\) in this interval were allowed, then

\[
1\le v-u=(\sqrt v-\sqrt u)(\sqrt v+\sqrt u)
\le\frac{2\delta}{T}\,2\sqrt{2cT}
=4\delta\sqrt{2c}\,T^{-1/2},
\]

which is impossible once \(T>32c\delta^2\). Intersecting the candidate interval with \([cT,2cT]\), or with the subset \(\mathcal N_T\), can only decrease the number of candidates. This argument is independent of the positions of the real interval endpoints.

Consequently the sum of (b_{n_j}\) over admissible (n_j\) is at most (b_*\). Summing the remaining variables freely gives

\[
\begin{aligned}
&\sum_{\substack{\mathbf n\in\mathcal N_T^p\\
                 |\sum_i\sigma_i\sqrt{n_i}|\le\delta/T\\
                 \ell(n_a)=\ell(n_b)}}\prod_i b_{n_i}\\
&\hspace{1cm}\le
b_*\left(\sum_{\ell(n_a)=\ell(n_b)}b_{n_a}b_{n_b}\right)
          M^{p-3}
=b_* S M^{p-3}.
\end{aligned}
\tag{7}
\]

The exponent (p-3\) counts precisely the fixed, unrestricted positions other than the two collision positions and the solved position. Choosing the solved position outside the collision pair is essential: it preserves the full label-square factor (S\).

A union bound over the \(\binom p2\) position pairs now proves (1). A tuple with several equal-label pairs is overcounted by this upper bound, which is harmless and ensures that none is omitted. In particular, the argument does not subtract only repeated integer indices; it subtracts all repeated labels.

### 3.3 Subtraction and restoration of the certificate's prefactor

Let \(\mathcal G(T)\) be the product-weighted mass of same-bin tuples with all labels pairwise distinct. Equations (4) and (6) imply

\[
\mathcal G(T)\ge\frac{M^p}J-\mathcal B(T)
\ge\frac{M^p}J-\binom p2 b_* S M^{p-3}
\tag{8}
\]

for all sufficiently large (T\). This subtracts a possibly larger set than the bad same-bin tuples, so the direction is correct.

Choose, for example, \(\eta=1/8\) in both weight hypotheses. Their constants are fixed before taking (T\to\infty\). The second term in (8) is then

\[
O_p\left(T^{(p-3)/4-3/4+1/8-1/2+1/8}\right)
=O_p(T^{p/4-7/4}),
\]

whereas the first is \(\gg T^{p/4-3/2}\). The ratio is \(O_p(T^{-1/4})\). Thus for sufficiently large (T\),

\[
\mathcal G(T)\ge\frac12\frac{M^p}J
\gg T^{p/4-3/2}.
\tag{9}
\]

Every tuple counted in \(\mathcal G(T)\) satisfies (5), hence its kernel factor is at least (w_0\) by (2). All other terms of the certificate are nonnegative and can be discarded. Therefore

\[
\mathcal C_p(T)\ge T2^{-p}w_0\mathcal G(T)
\gg T^{p/4-1/2},
\]

as claimed. No upper bound for (W\) outside its positive neighborhood is needed, and the bad mass in (6) is a product-weighted mass before applying the lower bound (w_0\); no incorrect subtraction of kernel-weighted quantities occurs.

## 4. First doubtful or unproved step

There is no remaining unproved step in this abstract lemma. Continuity at zero, weighted Cauchy, the spacing of distinct integers after the square-root map, and the supplied coefficient bounds suffice.

Two limitations must remain explicit. First, a proposed application must independently establish the packet's nonnegative coefficients, mass, maximum-weight bound, and distinct-label square-mass bound for its actual data. None is established here for any arithmetic object. Second, replacing \(|W|\) by a signed kernel or by complex phases would remove the nonnegative restriction step in §3.3. The present proof gives no signed-sum lower bound.

The global repeated-label estimate without the close constraint would be only \(\binom p2 S M^{p-2}\), of size \(T^{p/4-1+\eta}\). This exceeds the main close mass by a positive power of (T\). Thus that simpler subtraction would be invalid. The solved-index estimate (7) is the necessary repair, and it uses an index outside each chosen collision pair.

## 5. Required controls and outcomes

1. **Every repeated-label pattern: PASS.** The set (6) contains every close tuple with any equal-label position pair. The union bound includes pairs within either half and across halves. Multiple pairs and simultaneous coincidences are overcounted, never dropped.
2. **Distinct labels versus distinct indices: PASS.** Equation (7) uses \(\sum_\ell B_\ell^2\), including different integers sharing the same label. It never replaces this by \(\sum_n b_n^2\). The final tuples have pairwise distinct labels and hence pairwise distinct integer indices, but that weaker condition is not substituted into the proof.
3. **Ordering and multiplicities: PASS.** Ordered (k\)-tuple mass is exactly (M^k\); its bin square gives ordered (p\)-tuples exactly once. The factor \(\binom p2\) arises only as an upper bound for the union of bad position-pair events. The definition's (2^{-p}\) is retained unchanged.
4. **Real endpoints: PASS.** The bin count is \(1+\lfloor(D/\delta)T^{3/2}\rfloor\), so upper-endpoint bin coincidences are included. The one-candidate inequality holds for arbitrary real (T\) and for integer points in the closed real interval \([cT,2cT]\). No integrality or dyadic assumption on (T\) is made.
5. **Order (p=4\): PASS.** The close main mass is \(\gg T^{-1/2}\). The repeated-label mass is \(\ll b_*SM\ll T^{-1+2\eta}\). For \(\eta=1/8\), the latter is \(O(T^{-3/4})\), and multiplication by (T2^{-4}\) yields \(\mathcal C_4(T)\gg T^{1/2}\).
6. **Order (p=12\): PASS.** The close main mass is \(\gg T^{3/2}\). The error is \(\ll66 b_*SM^9\ll T^{1+2\eta}\), hence \(O(T^{5/4})\) at \(\eta=1/8\). The certificate is \(\gg T^{5/2}\).
7. **Fewer than (p\) active labels: PASS as a consistency check.** Cauchy over active labels gives \(\#\{\ell:B_\ell>0\}\ge M^2/S\gg_\eta T^{1-\eta}\). Thus fewer than (p\) active labels is impossible for sufficiently large (T\) under these hypotheses. It may occur at bounded (T\), which is why the conclusion is explicitly asymptotic.
8. **Strict epsilon allocation and constants: PASS.** The two losses are added as (2\eta\), and the proof needs \(2\eta<1/2\). Choosing \(\eta=1/8\) leaves a strict power saving. Bin counts, pair counts, (2^{-p}\), weight bounds, and thresholds all depend only on fixed data. Nothing is asserted uniformly for (p=p(T)\).
9. **Why (p\ge4\) matters: PASS.** The proof requires an index outside a collision pair. The analogous claim at (p=2\) can fail: for a continuous (W\) supported sufficiently near zero, different integers in \([cT,2cT]\) have (T|\sqrt u-\sqrt v|\gg\sqrt T\), so no distinct-label pair contributes for large (T\). The present packet excludes this case.
10. **No signed inference: PASS.** Only \(|W|\), nonnegative (b_n\), and a positive neighborhood of (W(0)\) are used. Signed terms outside or inside the selected bins could cancel in another expression. The conclusion is expressly confined to the positive certificate.

All controls are exact analytic checks; no numerical experiment was performed.

## 6. Dependencies and exact artifact hashes

Only the new isolated statement is a mathematical data dependency. Its SHA256 is:

- `rounds/codex-managed/gc-full-goal-distinct-source-review/briefs/isolated_distinct_certificate_statement.md`
  — `23962eb512ba6f2183581e8c356e95007b16ae91f624ed4cd04779aa1b7c442d`.

Protocol and previously allowed context, recorded for isolation provenance:

- `protocol.md`
  — `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
- `rounds/codex-managed/gc-full-goal-distinct-source-review/briefs/blind_moment_family_statement.md`
  — `89ec2e5ef9a814da0fa1e1cd7efcdc941bdeca673e4688228b084b9fab8717c5`.
- Own frozen preceding report, `rounds/codex-managed/gc-full-goal-distinct-source-review/reports/blind_moment_family.md`
  — `fe681f61a48faac2825138c8b7e0884e4f73c05b6cca789cb0f72b9f33e49e35`; not edited, and none of its mathematical results is needed for this proof.

The supplied graph hash is metadata only. No graph contents, claimant derivation, conductor synthesis, other report, external source, or numerical control artifact is a dependency.

## 7. Recommended state effect

**Promote the abstract lemma**, subject to the conductor's graph validation and any required remaining seam checks: the stated positive certificate has the lower bound \(\mathcal C_p(T)\gg T^{p/4-1/2}\) for each fixed even (p\ge4\), with the exact distinct-label restriction preserved.

**Retain application hypotheses separately.** This report does not establish the coefficient and label bounds for any concrete arithmetic data and does not convert the positive-certificate lower bound into a signed lower bound. The result is asymptotic in real (T\), with fixed-order constants.

No state file, original report, sibling report, synthesis, validation matrix, or successor-round artifact was changed. This task stops after this report.
