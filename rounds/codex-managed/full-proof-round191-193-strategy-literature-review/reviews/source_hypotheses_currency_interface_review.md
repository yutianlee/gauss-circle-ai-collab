# Round 194 source-hypotheses, currency, and interface review

## 1. Result

**Verdict: REPAIR.**

The dated primary-source conclusion survives: through the stated cutoff, the
audited corpus contains no theorem that accepts either complete physical mask
\(P_1\) or \(P_2\), the actual endpoint coefficient array, and the single
outer real part while removing the full \(Y/(H_B\mathfrak m)\) deficit.  The
cutoff, current-version ledger, withdrawal controls, coefficient/norm
failures, and exponent quarantine are substantively sound.

Four source/interface repairs are required:

1. Pascadi's uniform \(c^{-1/700+o(1)}\) saving belongs to Theorem 1.1,
   whereas Theorem 1.2 has a factorization-dependent saving and additional
   hypotheses.
2. Wright's Theorem 2.1 and Corollary 2.2 have different objects and
   hypotheses and must not be described jointly as one trilinear theorem.
3. The graph reconstruction incorrectly routes the GAR alternative through
   blockwise \(M9\), and it copies the critical BAL \(L^4\)-to-\(L^3\)
   ledger onto the separate remaining-label owner.
4. The preference for \(P_1\) is strategy opinion, not a consequence of the
   source audit.  The source evidence is neutral between \(P_1\) and \(P_2\)
   and cannot by itself override the exact \(P_2\) geometric selection.

- Claimant report SHA-256:
  `d4ee4001c122a6fc840d52239db03913d83f0afd506035ea141736ad0c5ac36a`
- Frozen graph SHA-256:
  `cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`

## 2. Exact corrections and retained hypotheses

### 2.1 Primary-source corrections

The following exact replacements are required in Section 2.3 of the
claimant report.

**Pascadi.**  In
[arXiv:2511.08445v2](https://arxiv.org/html/2511.08445v2), Theorem 1.1,
for \(M,N\ll c^{1/2+o(1)}\), gives

\[
 \sum_{(m,n,c)=1}\alpha_m\beta_nS(am,n;c)
 \ll \|\alpha\|\|\beta\|c^{1-1/700+o(1)}.
\]

Theorem 1.2 instead assumes

\[
 c=dd'e,\qquad d'\mid d,\qquad (d,e)=1,
\]

defines \(f\) as the largest integer with \(f^2\mid cd\), and gives the
factor

\[
 c^{o(1)}\left({f\over\min(c,d^2)}\right)^{1/6}.
\]

Example 1.3 yields a \(c^{-1/12}\) saving in the balanced \(p^2\) or \(pq\)
case.  Thus \(Lq^{699/700}\) is a correct restored diagnostic only for the
uniform Theorem-1.1 insertion; it is not the restored residual of the entire
Theorems-1.1--1.2 family.  This correction does not create a project match:
both theorems still require a fixed scalar modulus and separable coefficient
sequences and do not accept the physical \(P_iW\) array or the outer-real-part
placement.

**Wright.**  In
[arXiv:2604.25177v2](https://arxiv.org/html/2604.25177v2), Theorem 2.1 is the
fixed-factor trilinear Kloosterman-fraction estimate for the separable
\(\alpha_m\beta_n\nu_a\) form.  Corollary 2.2 is a positive modulus-average
convolution result with divisor-bounded \(\alpha,\beta\), a Siegel--Walfisz
hypothesis on \(\beta\), and explicit \(M,N,Q,a\) ranges.  Replace the joint
attribution by these two separate statements.  Neither has the claimant's
literal physical coefficient or norm location, so the no-match conclusion
is unchanged.

For theorem-number precision, the Tao--Trudgian--Yang exponent-pair statement
in [arXiv:2501.16779v1](https://arxiv.org/html/2501.16779v1) is **Theorem
20**, together with Table 1 and Lemmas 13--15.  The pair
\((89/1282,997/1282)\) is transcribed correctly.

### 2.2 Frozen-interface corrections

The standard route is

\[
 \text{direct M1}+\text{M9-M2}
 \longrightarrow M9
 \longrightarrow \text{Conditional-bridge}
 \longrightarrow \text{GC-target}.
\]

`M9-M1-physical-one-count-assembly` and
`M9-M2-physical-one-count-assembly` are already `proved_internal`
connectors.  Their named analytic inputs remain open, as does standard
`M9-endpoint-uniformity`.

The alternative route is instead

\[
\begin{aligned}
 &\text{M9-M1-global-angular-radial-estimate}\\
 &\quad\longrightarrow
   \text{M9-M1-GAR-total-active-equivalence}\\
 &\quad\text{together with M9-M2}\\
 &\quad\longrightarrow
   \text{GC-global-M1-alternative-bridge}
   \longrightarrow \text{GC-target}.
\end{aligned}
\]

It bypasses blockwise `M9-M1` and `M9`.  The GAR equivalence is
`proved_internal`; the alternative bridge is `derived_under_assumptions`
and remains blocked by GAR and M9-M2.  Any endpoint uniformity required by
its inputs is internal to them; the route must not be drawn through the
standard M9 endpoint node.  Consequently the claimant's statements that GAR
"does not replace M9" and that the GAR bridge is followed by M9 must be
deleted.

For BAL, the \(L^4\) coefficient-uniform capacity versus \(L^3\) target
belongs only to `M9-M2-balanced-double-far-actual-energy`, the persistent
critical \(j=1\) child.  The separate
`M9-M2-balanced-remaining-label-owner-quantifier-completion` target is

\[
 \left|\sum_G GP_G\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\]

over all remaining literal labels, including the isolated exact-square
\(j=2\), \(K/L=16\) boundary.  The graph assigns no \(L^4\) capacity to that
owner.  The claimant's second BAL row and the corresponding restored-power
paragraph must use this \(L^{3/2}\) target and mark the current numerical
capacity unavailable.

## 3. Verification against the primary records

The official [`math.NT` listing](https://arxiv.org/list/math.NT/new) confirms
the Friday 28 August 2026 boundary and exactly 44 records: 24 new, 6
cross-listed, and 14 replacements.  This is the last official listing before
the 2026-08-30 Asia/Shanghai cutoff.  The no-match is correctly limited to a
dated, named corpus and is not stated as a universal impossibility theorem.

The primary version histories confirm the decisive version ledger used by
the report: Mili\'cevi\'c--Robinson--Shupe v1, Shen v1,
Blomer--Pascadi v1, Pascadi v2, Mili\'cevi\'c--Qin--Wu v1, Wright v2,
Baier v4, Xiao v1, Tao--Trudgian--Yang v1, Li--Yang v2, and the August
energy records v3/v2/v1.  The checked theorem statements agree as follows:

- [Mili\'cevi\'c--Robinson--Shupe Theorem 1.1 and Definition 2](https://arxiv.org/html/2608.21346v1)
  concern one odd prime-power modulus, a fixed shift tuple, and a complete
  product; the displayed \(\Delta^*\)-dependent power is correct.
- [Shen Theorems 2--4](https://arxiv.org/html/2607.06575v1) have the stated
  prime-modulus ranges, and Theorem 4 is the positive odd-modulus second
  moment with scale \(\|\alpha\|_2^2N^{11/12}Q^{1+\varepsilon}\).
- [Blomer--Pascadi Theorem 1.1](https://arxiv.org/html/2607.24311v1) is a
  fixed-modulus separable bilinear form and saves \(c^{-1/32}\) at
  \(N=\sqrt c\).
- [Baier Theorems 2 and 4](https://arxiv.org/html/2601.15448v4) have the
  stated modular-square-root phase, derivative and support conditions, and
  positive restricted energies.
- [Xiao Theorems 1.1--1.2](https://arxiv.org/html/2606.28986v1) have the
  stated coefficient-one second- and fourth-moment ranges.
- [Popov's published article](https://www.mathnet.ru/eng/rm10162) is
  *Russian Mathematical Surveys* 79:1 (2024), 53--126; Theorem 5 is the
  truncated Voronoi formula and Theorem 10 gives the listed local moments.

The withdrawal controls are exact.  The
[Bourgain--Watt v2 record](https://arxiv.org/abs/1709.04340v2) says that
Theorems 1--3 lose theorem status.  The
[Dong--Robles--Zeindler v2 record](https://arxiv.org/abs/2601.00292v2)
identifies the omitted \(L^2\) factor, changing \(L^5\) to \(L^7\), and is
withdrawn.  Neither is used positively.

After the two source corrections above, the restored-power conclusions are
sound.  A fictitious Blomer--Pascadi insertion leaves \(Lq^{31/32}\), and a
fictitious Pascadi-Theorem-1.1 insertion leaves \(Lq^{699/700}\), against
the K17a target \(L\).  More fundamentally, every audited scalar, separable,
positive-moment, or fixed-modulus theorem fails before insertion because it
does not accept the joint physical mask, actual endpoint products, moving
affine sites and conductors, or the single outer real part.  Applying an
absolute value or positive norm rowwise restores the existing positive
ledger and therefore retains \(Y/(H_B\mathfrak m)\).

The external Li--Yang exponent, the internal \(1/3\), and the target
\(1/4\) remain in separate ledgers.  No source result is promoted into an
internal owner or used as an internal capacity.

## 4. First doubtful or unproved step

The first mathematical step remains unproved for **both** complement masks:

\[
 \left|\mathscr R_{{\rm core},Y,Q}^{\sigma}[P_i]\right|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon,
 \qquad i=1,2,
\]

with the mask on the physical source and all signs retained through the
single outer real part.  The source audit proves only that the named corpus
does not supply this step.

The claimant's first additional doubtful inference is that Boolean
"first-failure" order makes \(P_1\) the best next objective.  It does not.
The partition orders the masks but supplies no theorem-readiness, collision,
Gram, or dispersion comparison.  In particular, the same source audit finds
no match for either mask and the same positive deficit for both.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Claimant hash | **PASS.** Exact SHA stated in Section 1. |
| Cutoff and listing counts | **PASS.** 2026-08-28; 24/6/14 = 44. |
| Current primary versions | **PASS.** Named decisive records are current at the stated versions. |
| Theorem numbers and hypotheses | **REPAIR.** Separate Pascadi 1.1 from 1.2; separate Wright 2.1 from Corollary 2.2; identify TTY as Theorem 20. |
| Restored powers | **PASS after qualification.** \(699/700\) is specifically the Pascadi-Theorem-1.1 diagnostic. |
| Literal coefficient/norm placement | **PASS.** No audited theorem accepts the complete \(P_iW\) operator before the decisive outer real part. |
| Withdrawal controls | **PASS.** Both records are correctly excluded. |
| Dated corpus scope | **PASS.** No universal no-go is claimed. |
| Standard route | **PASS after status/order normalization.** Proved assemblies are connectors; M9 precedes the conditional bridge. |
| GAR route | **REPAIR.** It bypasses M9 and blockwise M9-M1. |
| Critical versus remaining BAL | **REPAIR.** Only the critical energy has the \(L^4\)-to-\(L^3\) ledger. |
| P1 preference | **RETAIN only as non-source strategy evidence.** The corpus audit supplies no P1-over-P2 comparison. |
| Exponent quarantine | **PASS.** No internal or global exponent changes. |

The exact \(P_2\) selection is based on a different criterion: its
one-close/one-far geometry fixes the close determinant coordinate
\((g,\Delta_-)\) and exposes a concrete coefficient-retaining
determinant-fibre vector-dispersion seam in \((\Delta_+,h)\).  The claimant's
P1 preference has no source-derived fact that defeats that criterion.
Therefore it **cannot override the P2 selection on source evidence**.  Nor
should the two reports be counted as votes.  A conductor may change the
selection only by an exact interface comparison, a refutation of the P2
seam, or stronger target-ready evidence for P1; none is supplied by this
literature report.

## 6. Dependencies and exact artifacts used

Local artifacts:

- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reports/current_primary_literature_reassessment_after_round193.md`;
- `state/proof_obligations.yml` at the frozen hash in Section 1;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reports/blind_round195_frontier_selection.md`;
- `rounds/codex-managed/full-proof-round191-193-strategy-literature-review/reviews/blind_post_unmask_frontier_selection_review.md`.

Primary records are linked at the exact claims above.  Additional checked
current records were the claimant's linked Mili\'cevi\'c--Qin--Wu, energy,
Guo, Chen--Lin, and Li--Yang records.  No secondary summary was used to
alter a theorem hypothesis.  No shared state or claimant file was edited.

## 7. Recommended state effect

**Retain the report as a repairable dated source no-match; promote no
mathematical claim and make no proof-state change.**

At synthesis:

1. apply the Pascadi, Wright, and TTY source-statement corrections;
2. retain the no-match, literal-coefficient failure, withdrawal ledger,
   dated scope, and exponent quarantine;
3. replace the GAR and BAL hierarchy rows by the exact graph interfaces in
   Section 2.2;
4. classify the P1 recommendation as non-source, inconclusive strategy
   evidence; and
5. do not use it to override the exact P2 geometric recommendation without
   a mathematical interface adjudication.

No analytic owner, parent, endpoint result, bridge, global theorem, or
exponent is promoted by this review.
