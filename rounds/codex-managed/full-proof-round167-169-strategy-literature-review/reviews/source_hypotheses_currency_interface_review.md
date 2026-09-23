# Round 170 source-hypotheses, currency, and interface review

## 1. Result

**Result: revise the source report before relying on its `primary_source_exact_hypotheses` control; after the repairs below, retain its source no-match conclusion and make no proof-graph change.**

The official records confirm the cited versions: Blomer--Pascadi arXiv:2607.24311 has only v1 (27 July 2026), Pascadi arXiv:2511.08445 is currently v2 (21 June 2026, after v1 on 11 November 2025), and Li--Yang arXiv:2308.14859 is currently v2 (14 September 2023). The Blomer--Pascadi formulas (Theorems 1.1, 5.5, 5.7, and 1.6), the displayed delta-specialization powers, the fixed-versus-varying-modulus obstruction, Pascadi Corollary 1.4's placement of the absolute value, and the exceptional-spectrum-only scope are substantively correct.

There are nevertheless mandatory source-interface repairs:

1. The report reverses the official Kloosterman convention and then incorrectly says that symmetry is unnecessary. Both new papers use
   \[
   S_{\rm src}(m,n;c)=\sum_{x\bmod c}^{*}e((mx+n\bar x)/c),
   \]
   whereas the project row is \(\sum_x^*e((N_0\bar x+hx)/n)\). The delta specialization is still exact, but only after the explicit substitution \(x\mapsto\bar x\), equivalently Kloosterman symmetry.
2. With the delta row \(m=1\), the joint source condition is \((1,h,n)=1\), hence automatic. The Blomer--Pascadi Theorems 1.1/5.5 and Pascadi's first Theorem 1.1 bound do **not** restrict the frequency to \((h,n)=1\). Only Pascadi's stronger \(1/276\) alternative retains \((h,n)=1\). The report's “ignoring noncoprime \(h\)” and “coprime-frequency subfamily” wording is false.
3. Pascadi Theorem 1.1 is stated for initial ranges \(1\le m\le M\), \(1\le n\le N\), not arbitrary translated intervals. Therefore the claimed chopping of all \(1\le h<n\) into \(\sqrt n\)-blocks and (170.U6) is not a legal direct application. Its exponent arithmetic is right only under an unstated translated-interval extension. It must be deleted or labelled hypothetical. This only strengthens the no-match verdict.
4. Pascadi Corollary 1.4 also assumes \(C\ge1/2\), \(\mathcal I,\mathcal J\subset\mathbb Z_+\), and \(\max(\mathcal I\cup\mathcal J)\ll C^{O(1)}\). These omitted hypotheses must be restored. Blomer--Pascadi Theorem 5.7, in contrast to Theorem 5.5, does not state \(M,N\le c\); “under the same hypotheses” should be replaced by its literal hypotheses.
5. The Round-169 collar identity must retain the floor error:
   \[
   \sqrt{JL}=L^{3/2}\left(\frac HL+O(L^{-1})\right).
   \]
   Thus the positive capacity exceeds the \(L^{3/2}\) target by \(H/L+O(L^{-1})\), and the required relative saving is \(L/H\). The report's later power direction is right, but (170.L3) is not an exact equality as printed and “misses \(L/H\)” is ambiguous.
6. Formula (170.L1) contains the malformed text `k\ {` followed by `m odd`; it must read \(k\ {\rm odd}\).
7. Li--Yang wording must respect the authoritative state: the repaired specialization is an accepted node with status `proved_external_dependency`, although it is not internally proved, is still a preprint, and proves none of the internal quarter-route owners. “Not an internally accepted graph lemma” and “retain only as a claimed benchmark” can be read as an unauthorized demotion and must be replaced by that exact distinction.

These defects invalidate a clean PASS for exact-source transcription, but none supplies the missing project estimate.

## 2. Exact statements and hypotheses

### 2.1 Versions and Kloosterman convention

The [official Blomer--Pascadi record](https://arxiv.org/abs/2607.24311) lists only arXiv:2607.24311v1, submitted 27 July 2026. The [official v1 manuscript](https://arxiv.org/html/2607.24311v1), Section 2.1 immediately before its Weil bound (2.4), defines

\[
S_{\rm src}(m,n;c)=\sum_{x\in(\mathbb Z/c\mathbb Z)^\times}
e\!\left(\frac{mx+n\bar x}{c}\right).
\tag{R170.1}
\]

The [official Pascadi record](https://arxiv.org/abs/2511.08445) lists v1 on 11 November 2025 and current v2 on 21 June 2026; its comment is “Various revisions and minor corrections following referees' comments.” The [official v2 manuscript](https://arxiv.org/html/2511.08445v2), equation (1.1), uses the same convention (R170.1).

### 2.2 Blomer--Pascadi v1

Theorem 1.1 has \(c\in\mathbb Z_+\), \(N\in\mathbb Z\cap[1,c]\), integer intervals \(|\mathcal I|,|\mathcal J|\le N\), arbitrary complex sequences, and \(a\in(\mathbb Z/c\mathbb Z)^\times\). It states

\[
\left|\sum_{\substack{m\in\mathcal I,n\in\mathcal J\\(m,n,c)=1}}
\alpha_m\beta_nS_{\rm src}(am,n;c)\right|
\ll \|\alpha\|_2\|\beta\|_2c^{1+o(1)}
\left(\frac{N^{1/8}}{c^{3/32}}+
\frac{N^{5/16}}{c^{3/16}}+
\frac{N^{2/3}}{c^{7/18}}\right).
\tag{R170.2}
\]

The source explicitly also grants the bound without the joint gcd condition in the initial-interval case \(\mathcal I=\mathcal J=\{1,\ldots,N\}\). At \(N=\sqrt c\), (R170.2) is \(c^{1-1/32+o(1)}\|\alpha\|_2\|\beta\|_2\).

Theorem 5.5 has \(M,N\in\mathbb Z\cap[1,c]\), arbitrary integer intervals of exact lengths \(M,N\), arbitrary complex sequences, the same joint gcd condition and unit \(a\), and

\[
\left|\sum_{\substack{m\in\mathcal I,n\in\mathcal J\\(m,n,c)=1}}
\alpha_m\beta_nS_{\rm src}(am,n;c)\right|
\ll\|\alpha\|_2\|\beta\|_2c^{1+o(1)}H(M,N,c),
\tag{R170.3}
\]

where the Round-170 transcription of

\[
\begin{aligned}
H(M,N,c)={}&\frac{M^{1/8}((c+MN)(c+N^2))^{1/16}}{c^{1/4}}
\min(c/M,c^{1/2})^{1/16}\\
&+\left(\frac{N^2}{c^2}+\frac{N^{1/2}M(c+N^2)}{c^{5/2}}\right)^{1/16}
+\frac{M^{1/3}+N^{1/3}}{c^{1/5}}\\
&+\frac{M^{1/2}N^{1/6}+M^{1/6}N^{1/2}}{c^{7/18}}
+\frac{M^{1/15}+N^{1/15}}{c^{1/15}}
\end{aligned}
\tag{R170.4}
\]

is exact. The gcd-removal exception requires both initial intervals \(\{1,\ldots,M\}\) and \(\{1,\ldots,N\}\).

Theorem 5.7 instead assumes \(c\in\mathbb Z_+\), integer interval lengths \(M,N\), arbitrary integer intervals and sequences, and unit \(a\); it does not print \(M,N\le c\). Its restriction is \((m,c)=1\), and its exact bound is

\[
\ll\|\alpha\|_2\|\beta\|_2c^{1+o(1)}
\left(\frac{(MN)^{1/2}}{c^{3/4}}+
\frac{N^{1/2}}{c^{1/2}}+
\frac{M^{1/2}}{c^{1/4}}\right).
\tag{R170.5}
\]

Theorem 1.6 takes \(N\ge1/2\) and an arbitrary complex sequence on \(n\sim N\). It is exactly a positive large sieve over the exceptional Maaß cusp forms \(\lambda_j<1/4\) in a complete orthonormal Maaß cusp basis at one fixed level \(q=rs\), one fixed cusp equivalent to \(1/s\), and one scaling matrix. The reported weight

\[
\mathcal X=1+\frac qN+\min\left(\frac{q^{18/11}}{N^{23/11}},
\frac{q^{16/13}}{N^{18/13}},\frac{q^{32/29}}{N^{33/29}}\right)
+\frac{q^2}{N^3}
\tag{R170.6}
\]

and right side \((qN)^{o(1)}(1+N/q)\|\alpha\|_2^2\) are correctly transcribed. The theorem is not a full Kuznetsov identity and states nothing that disposes of regular Maaß, holomorphic, Eisenstein, diagonal, or geometric/main terms in a prospective trace-formula application.

### 2.3 Pascadi v2

Theorem 1.1 uses positive integers \(c,M,N\), initial ranges \(m\le M,n\le N\), \(M,N\ll c^{1/2+o(1)}\), arbitrary complex sequences, and a unit \(a\). Its two exact alternatives are

\[
\sum_{\substack{m\le M,n\le N\\(m,n,c)=1}}
\alpha_m\beta_nS_{\rm src}(am,n;c)
\ll\|\alpha\|_2\|\beta\|_2c^{1-1/700+o(1)},
\tag{R170.7}
\]

and, if \(|\alpha_m|\le1\),

\[
\sum_{\substack{m\le M,n\le N\\(n,c)=1}}
\alpha_m\beta_nS_{\rm src}(am,n;c)
\ll\sqrt M\|\beta\|_2c^{1-1/276+o(1)}.
\tag{R170.8}
\]

Theorem 1.2 and the Round-170 formula

\[
\|\alpha\|_2\|\beta\|_2c^{1+o(1)}
\left(\frac f{\min(c,d^2)}\right)^{1/6},
\qquad c=dd'e, d'\mid d, (d,e)=1, f^2\mid cd\text{ maximal},
\tag{R170.9}
\]

are correct; unlike Theorem 1.1, this theorem permits arbitrary integer intervals of lengths \(\ll c^{1/2+o(1)}\).

Corollary 1.4 has the additional hypotheses omitted in the source report: \(C\ge1/2\), \(\mathcal I,\mathcal J\subset\mathbb Z_+\), lengths \(\ll C^{1/2+o(1)}\), and \(\max(\mathcal I\cup\mathcal J)\ll C^{O(1)}\). Its exact placement is

\[
\sum_{\substack{C<c\le2C\\q\mid c}}
\left|\sum_{\substack{m\in\mathcal I,n\in\mathcal J\\(m,n,q)=1}}
\alpha_m\beta_nS_{\rm src}(m,n;c)\right|,
\tag{R170.10}
\]

and the reported right side

\[
\|\alpha\|_2\|\beta\|_2\frac{C^{2+o(1)}}q
\left(\frac f{\min(C,d^2)+\min(q,d^2C/q)}\right)^{1/6}
\tag{R170.10a}
\]

is correct. Thus the absolute value is taken separately for every varying modulus \(c\), the gcd is with fixed \(q\), and the two sequences are fixed across that modulus sum.

Corollary 1.6 concerns a fixed level \(q\), the cusp at infinity, an orthonormal Maaß cusp basis, \(N\ll q^{1/2+o(1)}\), and a vector supported on \((n,q)=1\). Its sum is only over \(\lambda_j<1/4\), with weight \(q^{(6/5)\theta_j}\). It is therefore an exceptional-Maaß positive square, not an all-spectrum estimate.

### 2.4 Pointwise exponent and normalization

The [official Li--Yang v2](https://arxiv.org/html/2308.14859v2), Theorem 1.2, states the unrestricted pointwise bounds for \(R(X)\) and \(\Delta(X)\) with \(\theta^*=0.314483\ldots\). The repository's repaired narrow specialization gives

\[
\theta_{\rm LY}=\frac{3292+25\sqrt{1717}}{13762}
=0.3144831759740614\ldots
\tag{R170.11}
\]

for real \(X\ge2\), subject to all five literal repairs and the two restricted-range supplements in `sources/li_yang_2023.md`. The official arXiv record remains v2, and the second author's current page still lists it as a preprint. This bibliographic status does not undo the graph's already audited `proved_external_dependency` status.

The [official Gao v1](https://arxiv.org/html/2604.23918v1) is about

\[
\Psi_G(x,y)=\sum_{\substack{n\le x\\P(n)\le y}}r(n)
\]

in a restricted friable range, not the unrestricted discrepancy. Its introduction places \(131/208\) directly in the area-variable formula \(\sum_{n\le x}r(n)-\pi x\); this is a normalization error. [Huxley's official abstract](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024611503014485) states \(131/208\) for the maximum radius-of-curvature variable \(R\), hence \(131/416\) after the circle/area substitution \(R=\sqrt X\). The Round-170 rejection of Gao as an unrestricted exponent update is correct.

## 3. Proof and interface derivation

### 3.1 Correct delta specialization and powers

Let

\[
S_{\rm proj}(N_0,h;n)=\sum_{x\bmod n}^{*}
e((N_0\bar x+hx)/n).
\]

By the bijection \(x\mapsto\bar x\),

\[
S_{\rm proj}(N_0,h;n)=S_{\rm src}(N_0,h;n)
=S_{\rm src}(h,N_0;n).
\tag{R170.12}
\]

On the unit-center subfamily \((N_0,n)=1\), take \(c=n\), \(a=N_0\), \(\mathcal I=\{1\}\), \(\alpha_1=1\), \(\mathcal J=\{1,\ldots,n\}\), \(\beta_h=\widehat\gamma_{g,n}(h)\) for \(h<n\), and \(\beta_n=0\). This gives \(S_{\rm src}(N_0,h;n)\), and (R170.12) gives the project row. The source condition \((m,h,n)=1\) is \((1,h,n)=1\), so it is automatic for every \(h\); the initial-interval gcd-removal clause is not needed. Likewise, Theorem 5.7's \((m,c)=1\) is automatic.

Substitution \((M,N,c)=(1,n,n)\) in (R170.4) gives the five powers

\[
n^{-1/32},\quad 1,\quad n^{2/15},\quad n^{1/9},\quad1.
\]

Thus

\[
H(1,n,n)\asymp n^{2/15},\qquad
\left|\sum_{h<n}\widehat\gamma_{g,n}(h)S_{\rm proj}(N_0,h;n)\right|
\ll n^{17/15+o(1)}\|\widehat\gamma_{g,n}\|_2.
\tag{R170.13}
\]

The common-length Theorem 1.1 with \(N=n\) gives

\[
n^{1+o(1)}(n^{1/32}+n^{1/8}+n^{5/18})
=n^{23/18+o(1)},
\tag{R170.14}
\]

and Theorem 5.7 gives

\[
n^{1+o(1)}(n^{-1/4}+1+n^{-1/4})
\asymp n^{1+o(1)}.
\tag{R170.15}
\]

Theorem 5.7 is therefore the best of these direct full-row fixed-modulus delta applications and has no power saving. Blomer--Pascadi Theorem 1.1 does allow arbitrary translated intervals; chopping into \(n^{1/2}\) blocks gives \(n^{31/32+o(1)}\|\beta_B\|_2\) per block and hence

\[
n^{39/32+o(1)}\|\widehat\gamma_{g,n}\|_2
\tag{R170.16}
\]

after triangle and Cauchy. This arithmetic is correct, and no coprime-frequency deletion is involved.

For Pascadi (R170.7), the formal block arithmetic would indeed be

\[
n^{1-1/700+o(1)}\times n^{1/4}
=n^{5/4-1/700+o(1)},
\tag{R170.17}
\]

but v2 does not state (R170.7) for translated intervals. Only the first initial block is licensed; (R170.17) is not a theorem-backed full-row estimate. Even a hypothetical translated-interval version would be worse than (R170.15). The stronger (R170.8) would retain \((h,n)=1\) and would still not reconstruct the full row.

For arbitrary \((N_0,n)\), the choice \(a=N_0\) violates the unit hypothesis. Choosing \(a=1\) and placing \(N_0\) into an argument replaces that failure by a nonautomatic source gcd condition; it does not license the complete project row. A gcd decomposition would be an additional project reduction.

### 3.2 Fixed modulus, varying vectors, and absolute values

Every bound (R170.2)--(R170.5) is for one fixed modulus \(c\). In the project, \(c=n\) varies and

\[
\beta_h^{(n,g)}=\widehat\gamma_{g,n}(h)
\]

depends on both the modulus and the outer variable \(g\). Applying a fixed-modulus estimate and then summing places absolute values before the outer \(\chi_4(g)\chi_4(n)\) aggregate. Pascadi Corollary 1.4 does vary \(c\), but (R170.10) still takes a separate absolute value at each \(c\) and requires coefficient sequences fixed across \(c\). It therefore cannot accept the project family.

### 3.3 Spectral scope

Blomer--Pascadi Theorem 1.6 and Pascadi Corollary 1.6 bound positive squares only over exceptional Maaß cusp forms. They do not provide the full Kuznetsov transform needed to identify the project kernel, and they do not price regular Maaß, holomorphic, Eisenstein/continuous, diagonal/geometric main, zero-frequency, residue, or endpoint contributions. The Round-170 all-spectrum rejection is correct.

### 3.4 Round-169 collar direction

The authoritative Round-169 node has \(H=\sqrt J+O(1)\). Therefore

\[
\sqrt{JL}=L^{3/2}\frac{\sqrt J}{L}
=L^{3/2}\left(\frac HL+O(L^{-1})\right).
\tag{R170.18}
\]

Since \(1\ll L\ll H\), this capacity is larger than the \(L^{3/2}\) target by \(H/L+O(L^{-1})\). Closing the target needs cancellation by the reciprocal factor \(L/H\). No audited source supplies it. This is the only lawful direction of the power comparison.

### 3.5 Current exponent wording

Li--Yang use the area variable \(m^2+n^2\le X\), so (R170.11) is already the area-variable exponent. Huxley's \(131/208\) is in a radius/curvature variable and becomes \(131/416\) in \(X\). Gao's smooth-number theorem neither removes \(P(n)\le y\) nor gives a uniform limiting passage to the unrestricted problem. The dated exponent ledger is therefore unchanged: internally proved \(1/3\), accepted repaired external dependency \(\theta_{\rm LY}\), target \(1/4\).

## 4. First doubtful or unproved step

The first false transcription in the source report is its redefinition of the official Kloosterman sum in (170.3.2), followed by “Kloosterman symmetry is not needed.” Equation (R170.12) repairs it exactly. The first illegal theorem application is Pascadi Theorem 1.1 on translated \(\sqrt n\)-blocks; the source states initial ranges only.

After those repairs, the first **project** failure for the Round-169 collar remains earlier than any exponent comparison: no exact map from the moving real product collar \(k\ell=XQR\), with the literal cardinal array and outer \(g(Q,R)\), to a source Kloosterman bilinear form or automorphic moment has been proved.

For the UNBAL delta row, the hierarchy is:

1. the complete family does not guarantee \((N_0,n)=1\), while the convenient delta map requires unit \(a=N_0\);
2. on the unit-center subfamily, the delta row, including every frequency \(1\le h<n\), is legal at one fixed modulus after (R170.12);
3. the best direct full-row source bound is the unsaved scale (R170.15);
4. the coefficient vector varies with \((g,n)\), and no cited theorem retains the outer character signs before a positive norm;
5. an attempted spectral replacement still owes the full spectrum, main/residual terms, moving weights, hard endpoints, and real center.

This remains a source-hypothesis and restored-power no-go, not a lower bound and not an impossibility theorem for a new signed vector estimate.

## 5. Required controls and outcomes

| Control | Outcome | Reason |
|---|---|---|
| `source_version_currency` | **GREEN** | BP is v1 dated 2026-07-27; Pascadi is current v2 dated 2026-06-21; Li--Yang remains v2 dated 2023-09-14. |
| `primary_source_exact_hypotheses` | **RED pending repair** | Official Kloosterman convention is reversed in the report; Pascadi translated-block use is illegal; Corollary 1.4 hypotheses and BP 5.7's literal range need restoration. |
| `delta_specialization_powers` | **GREEN algebraically** | \(2/15,1/9,17/15,23/18,1,39/32\) are correct; Pascadi's \(5/4-1/700\) is arithmetic only, not a licensed full-row application. |
| `unit_and_gcd_conditions` | **RED pending repair** | Unit-center obstruction is real, but joint gcd with delta \(m=1\) is automatic; no coprime-frequency restriction occurs in the first BP/Pascadi bounds. |
| `fixed_vs_varying_modulus` | **GREEN as rejection** | BP is fixed modulus; project vectors depend on \((g,n)\); Pascadi's modulus average uses fixed vectors. |
| `absolute_value_placement` | **GREEN as rejection** | Pascadi Corollary 1.4 has \(\sum_c|\text{inner}_c|\), not one absolute value outside a signed modulus sum. |
| `all_spectrum_scope` | **GREEN as rejection** | The two large-sieve statements sum only exceptional Maaß cusp forms and do not settle a full trace-formula ledger. |
| `current_unrestricted_pointwise_exponent` | **GREEN after status wording repair** | Gao is friable-only; Li--Yang remains the accepted repaired external benchmark, not an internally proved theorem. |
| `Gao_Huxley_normalization` | **GREEN** | Gao prints \(131/208\) in the area formula; Huxley's primary abstract makes the radius/curvature normalization and hence \(131/416\) in area explicit. |
| `Round169_H_over_L_direction` | **GREEN after formula repair** | Capacity/target is \(H/L+O(L^{-1})\); required relative saving is \(L/H\). |
| `hard_endpoint_and_signed_aggregate` | **NO SOURCE MATCH** | No cited theorem accepts the literal moving/cardinal weights and outer signed family. |
| `no_status_or_exponent_overpromotion` | **RED pending wording repair** | The report must not describe the accepted Li--Yang external node as absent from the accepted graph. |

Required control test outcome: **the source no-match survives; exact-source PASS does not survive without the listed textual and hypothesis repairs.**

## 6. Dependencies and exact artifacts used

Repository artifacts read completely:

- `protocol.md`;
- `state/active_campaign.yml`;
- the complete authoritative entries `GC-external-Li-Yang-theta-star`, `M9-M2-smooth-unbalanced-three-quarter-estimate`, and `M9-M2-hard-top-t1-joint-functional-equation-double-poisson-self-return` in `state/proof_obligations.yml`;
- `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/reports/current_primary_literature_reassessment.md`;
- `sources/li_yang_2023.md`;
- `proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md`.

Official primary sources checked:

- Blomer--Pascadi record and v1 manuscript: <https://arxiv.org/abs/2607.24311>, <https://arxiv.org/html/2607.24311v1>;
- Pascadi record and v2 manuscript: <https://arxiv.org/abs/2511.08445>, <https://arxiv.org/html/2511.08445v2>;
- Li--Yang record and v2 manuscript: <https://arxiv.org/abs/2308.14859>, <https://arxiv.org/html/2308.14859v2>;
- Xuerui Yang's publication page: <https://sites.google.com/view/xuerui-yang>;
- Gao v1: <https://arxiv.org/html/2604.23918v1>;
- Huxley's official journal abstract: <https://doi.org/10.1112/S0024611503014485>.

No numerical experiment was used as theorem evidence. The displayed exponent substitutions are direct algebraic specializations of the official formulas.

## 7. Recommended state effect

**Recommended report effect: `revise`. Recommended proof-state effect: `no change`.**

Before the Round-170 source report can support a green source seam, it must:

1. restore the official Kloosterman convention and insert the exact symmetry/inversion step (R170.12);
2. remove every suggestion that the first delta bounds require \((h,n)=1\), reserving that condition for Pascadi's \(1/276\) alternative;
3. delete or explicitly quarantine (170.U6) as a hypothetical translated-interval computation, since Pascadi Theorem 1.1 does not state that extension;
4. restore all Corollary 1.4 support hypotheses and state BP Theorem 5.7's literal length hypotheses;
5. repair (170.L1) to \(k\ {\rm odd}\) and (170.L3) to the floor-aware identity (R170.18), saying “unpaid factor \(H/L\), required saving \(L/H\)”;
6. describe Li--Yang as the graph's unchanged `proved_external_dependency` under its repair card, while keeping the internally proved exponent at \(1/3\).

After those repairs, retain the substantive verdict: Blomer--Pascadi v1 and Pascadi v2 are current, relevant fixed-modulus/exceptional-spectrum method leads, but neither proves the Round-169 signed collar, the UNBAL owner, or any downstream parent. Gao does not update the unrestricted exponent. No accepted graph node should be promoted, demoted, or otherwise changed.
