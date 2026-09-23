# Full-graph post-repair verification

- Campaign: `full-proof-round171-173-strategy-literature-review`
- Task: post-repair verification of K26 freeze and local-moment threshold
- Role: verification only; not a claimant or state owner
- Generated: 2026-08-27, Asia/Shanghai
- Verdict: **GREEN**

## 1. Result

**GREEN.**  The repaired K26 definitions and the sole proposed target in
`reports/full_graph_frontier_reconstruction.md` agree with the exact
Round-172 kernel and satisfy every literal repair required by
`reviews/dependency_power_selection_seam_review.md`.

The local-moment row is also repaired correctly: a saving of exactly
\(Y^{8/48}=Y^{1/6}\) reaches the \(Y^{27/48}=Y^{9/16}\) one-third
threshold, while a strict sub-\(1/3\) conclusion requires a saving
\(Y^{1/6+\delta}\) for some fixed \(\delta>0\), with epsilon rebudgeted
below \(\delta\).

There is no definitional, normalization, range, target, strict-inequality,
owner-scope, or byte-hygiene discrepancy.  No proof or proof-state
promotion follows from this verification.

## 2. Exact statement and hypotheses checked

The repaired report now freezes all data that the earlier seam review found
missing:

1. \(e(t)=e^{2\pi i t}\), real large \(X\), \(J=\sqrt X\),
   \(1\ll L\ll H\le J^{1/2}\), \(R_0=\lceil L\rceil\), and integer
   \(M=M_L\asymp L^2\);
2. the literal residual coefficient
   \[
   c_N^{\rm rem}=
   \sum_{\substack{d\mid N\\d\ {\rm odd}}}
   \chi_4(d)\lambda_N(d),\qquad
   z_N=c_N^{\rm rem}e(J\sqrt N),\qquad
   D_L\ll_\varepsilon L^2X^\varepsilon;
   \]
3. the minimal stopped chain
   \(R_{j+1}=\min(2R_j,M)\), \(R_K=M\), retaining a strict final
   non-doubling link;
4. the exact Fejer convention
   \[
   F_R(\theta)=\sum_{|r|<R}
   \left(1-\frac{|r|}{R}\right)e(r\theta),\qquad
   B_{R,S}=F_S-F_R;
   \]
5. a fixed real disjoint-cardinal bump
   \(\varphi\in C_c^\infty((-1/2,1/2))\), \(\varphi(0)=1\), and the
   complete definitions of \(\mathcal W_\epsilon\),
   \(\mathcal B_{\epsilon,\theta}\), its Fourier transform with kernel
   \(e(-\xi x-\nu y)\), and
   \(U_{k,\ell}^{(\epsilon)}(\theta)=\widetilde{\mathcal
   B}_{\epsilon,\theta}(k/4,\ell)\); and
6. the exact complete nonzero ordinary-frequency link
   \[
   \begin{aligned}
   \mathcal N_{R,S}=\frac18\Re\sum_{\epsilon=0}^1
   &\sum_{\substack{k,k'\in\mathbb Z\\k,k'\ {\rm odd}}}
    \sum_{\substack{\ell,\ell'\in\mathbb Z\\\ell,\ell'\ne0}}
    \chi_4(k)\chi_4(k')\\
   &\times\int_0^1B_{R,S}(\theta)
    U_{k,\ell}^{(\epsilon)}(\theta)
    \overline{U_{k',\ell'}^{(\epsilon)}(\theta)}\,d\theta .
   \end{aligned}
   \]

The repaired sole objective is

\[
\boxed{
\sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
\ll_\varepsilon L^3X^\varepsilon .}
\tag{V.K26}
\]

It is expressly one-sided.  No absolute value surrounds the whole chain,
and no linkwise estimate is required.  The full literal coefficient,
absolute-parity branches, integer frequency ranges, both nonzero ordinary
frequencies, cardinal cells, arithmetic openings, endpoints, transitions,
zero extension, and strict terminal link remain inside the signed
recombination.

## 3. Proof or derivation of the verification

### K26 term-by-term comparison

| Seam | Round-172 kernel | Repaired full-graph report | Outcome |
|---|---|---|---|
| Residual coefficient | (172.K1)--(172.K2) | report (2.4) | exact match in formula, support role, energy scale, and literal-label scope |
| Stopped chain | (172.K5), with \(R_K=M\), repetitions removed, strict terminal link | report (2.5), \(K\) minimal | exact match |
| Fejer normalization | \(F_R\) and \(B_{R,S}=F_S-F_R\) in (172.K3), (172.K7)--(172.K8) | report (2.6) | exact match |
| Cardinal interpolation | (172.K12)--(172.K13) | report (2.7) | exact match in parity sign, phase, bump support, Fourier convention, and \(k/4\) sampling |
| Nonzero link | (172.K20) | report (2.8) | exact match in \(1/8\), one outer real part, parity sum, odd \(k,k'\), nonzero \(\ell,\ell'\), characters, bandpass, and conjugation |
| Whole-chain target | kernel Section 5 permits signed cancellation among the links of (172.K5) | report (175.K26-chain) | exact lawful target; absolute whole-chain or linkwise control remains only a stronger sufficient statement |
| Recombination scope | (172.K5), (172.K6), and (172.K19) | report promotion gate | exact: K26 follows only after the once-only short correction and collectively recombined ordinary-zero-containing sector are restored |

The use of \(\epsilon\) in the report where the seam repair displayed
\(\eta\) is a bound-variable rename and changes no definition.  The report
also makes \(k,k',\ell,\ell'\in\mathbb Z\) explicit, which is consistent
with and slightly more self-contained than the compact notation in
(172.K20).

### Strict local-moment threshold

The accepted connector is

\[
\Theta(\beta)=
\max\left\{\frac{7/16+\beta}{3},\frac\beta2\right\}.
\]

The current complete correlation exponent is \(35/48\).  Saving exactly
\(8/48\) gives \(\beta=27/48=9/16\), and

\[
\Theta(9/16)=\max\{1/3,9/32\}=1/3.
\]

Therefore equality reaches but does not cross the one-third threshold.  A
saving \(Y^{1/6+\delta}\) gives
\(\beta=9/16-\delta\), and after choosing the requested epsilon smaller
than \(\delta\), both branches of \(\Theta(\beta)\) are strictly below
\(1/3\).  The repaired wording in the full-graph matrix states precisely
this distinction.  Its separate target \(Y^{24/48}=Y^{1/2}\) still yields
the lawful exponent \(5/16\), not \(1/4\), and proves no M9 node.

## 4. First doubtful or unproved step

There is no post-repair documentary discrepancy.  Consequently there is no
“first discrepancy” to report.

The first genuinely unproved mathematical step remains (V.K26): no
accepted theorem saves the missing factor \(L\) on the complete literal
whole-chain signed nonzero-frequency aggregate.  This verification checks
only that the theorem is stated exactly and lawfully; it supplies no
evidence for the estimate.

## 5. Required controls and byte/hygiene outcome

| Control | Outcome |
|---|---|
| exact residual definition | GREEN |
| stopped-chain start, terminal index, and strict final link | GREEN |
| Fejer and Fourier conventions | GREEN |
| \(i/2\) transform normalization and \(1/8\) squared/parity normalization | GREEN |
| odd \(k,k'\) and nonzero integer \(\ell,\ell'\) ranges | GREEN |
| one outer real part and one-sided whole-chain target | GREEN |
| target equivalence modulo the once-only short correction and collective ordinary-zero sector | GREEN |
| exact versus strict local-moment threshold | GREEN |
| no owner or exponent overpromotion | GREEN |

Byte-level checks on all three compared artifacts and this output found:

- zero bare carriage returns;
- zero forbidden C0 controls other than ordinary tab/line-ending bytes;
- zero raw `0xC0` bytes and zero NUL bytes;
- valid UTF-8 throughout; and
- zero Unicode replacement characters.

The compared SHA-256 values were:

- full-graph report: `454D4296FE04F1898B3503D83BDFB976382238FBB14BFB1C34050A3A7013EE0B`;
- Round-172 K26 kernel: `29062AB64C6137546990FF234FFCE2E48E269BD607D630B3F0576E2CCC905AA1`;
- dependency/power seam review: `9898D27D157CB9F3F211FB60EED077B24E182CC9C599695DC90C5A8D8D27F5D5`.

## 6. Dependencies and exact artifacts used

This verification used only:

1. `protocol.md` and the already-loaded authoritative Round-174 campaign context;
2. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reports/full_graph_frontier_reconstruction.md`;
3. `proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md`; and
4. `rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reviews/dependency_power_selection_seam_review.md`.

No web source, numerical experiment, unassigned report, or state mutation
was used.

## 7. Recommended state effect

**No state edit.**  Accept the repaired full-graph K26 definition and
strict local-moment wording as GREEN at the statement, normalization,
power, and hygiene seams.  Retain every proof status and exponent.  The
verification licenses neither a State Patch nor the start of Round 175.
