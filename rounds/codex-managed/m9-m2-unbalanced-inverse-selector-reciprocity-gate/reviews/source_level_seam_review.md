# Round 160 independent source/level seam review

Campaign: `m9-m2-unbalanced-inverse-selector-reciprocity-gate`

Task: round160_source_level_review

Role: independent source and spectral-level reviewer. This is review
evidence only and changes no proof status.

Starting graph SHA-256:
4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d

Generated at: 2026-08-25T19:02:35+08:00

## 1. Result

**Pass with three conclusion-preserving repairs.** The source audit
correctly concludes that none of the cited scalar theorems proves the
Round-160 owner estimate or a strict owner-complete range. In particular:

1. Bettin--Chandee Theorem 1 and Wright Theorem 2.1 accept the bare
   Kloosterman-fraction phase
   \(e(h\overline n_j/j)\), but require independent one-variable
   coefficient sequences. They do not accept the simultaneous joint factor
   \(S(N_0,h;n)\) or the literal moving \((n,j)\)-support as one source
   coefficient. The stated Wright side condition
   \(C_g\ll J_g^2\) is the exact image of \(M\ll N^2\).
2. Blomer--Milićević Theorem 1 has fixed positive Fourier arguments, one
   arithmetic function on \((\mathbb Z/q\mathbb Z)^*\), one smooth scalar
   modulus test, and the Linnik condition \(mn\le C^2\). For
   \(q=4p\), \(p=j\) prime and \(p\nmid h\), the report's calculation
   \(\|\widehat f_{p,h}\|_1\asymp p\) is exact up to the harmless fixed
   mod-\(4\) normalization.
3. Blomer--Milićević's arithmetic-weight identity and Theorem 4 do force
   growing levels when the inverse-residue weight is encoded legally.
   Deshouillers--Iwaniec supply only common-sequence large-sieve
   interfaces, and Assing--Blomer--Li Theorem 2.4 supplies only one
   sequence times a jointly smooth test with the printed derivative
   parameter. None is the required literal vector theorem.

Three phrasings require repair before promotion.

- The exact long-\(h\) self-return shows that a short Linnik estimate does
  **not control** the complement and gives no formal right to delete it. It
  does not prove that the actual signed complement is quantitatively
  non-negligible.
- The prime-level ledger should be stated character by character. The
  principal \(\psi\pmod p\) component has primitive conductor \(4\), odd
  parity, and levels \(4,8,4p,8p\). A nonprincipal \(\psi\) has primitive
  conductor \(4p\) and levels \(4p,8p,4p^2,8p^2\). For \(p\ge5\), both
  parities occur across the nonprincipal \(\psi\)-family, but not at the
  pure levels \(4\) and \(8\).
- The Assing--Blomer--Li mismatch must explicitly retain
  \(\chi_4(c)\). Theorem 2.4 has no such modulus-character input. Encoding
  it by an additive mod-\(4\) test is possible only at archimedean
  frequency \(\asymp C_g\), hence it is another large-\(Z\) cost, not a
  free fixed-level insertion.

With those repairs, the correct conclusion is the narrow one already
required by the post-blind review: the audited **canonical scalar**
Kloosterman-fraction, common-test, fixed-level trace, and common-sequence
large-sieve routes do not yield an owner-saving theorem. This is not a
lower bound for the literal weighted matrix and not an impossibility
theorem for a bespoke vector-valued treatment.

## 2. Exact statement and hypotheses

For fixed \(g\), put

\[
 C_g=R/g,\qquad J_g=K/g,
\]

so \(n\asymp C_g\), \(j\asymp J_g\), and
\(C_g/J_g=\Delta>1\). The source seam concerns

\[
\begin{split}
 \sum_{\substack{n\asymp C_g\\ n\ {\rm odd}}}
 \sum_{1\le h<n}\sum_{\substack{j\in\mathcal J_{g,n}\\ (j,n)=1}}
 &\frac{\chi_4(g)\chi_4(n)}{gnj}
 W\!\left(\frac{X}{gnD}\right)
 q_L\!\left(\frac{4Xj}{gn^2}\right)\\
 &\times e\!\left(\frac{\xi j}{n}
       +\frac{h\overline n_j}{j}-\frac{h}{jn}\right)
 S(N_0,h;n).
\end{split}
\tag{160.SL1}
\]

No coprimality between \(N_0\) and \(n\) is assumed.

**Bettin--Chandee.** Theorem 1 of
[*Trilinear forms with Kloosterman fractions*,
arXiv:1502.00769v1](https://arxiv.org/html/1502.00769v1)
has arbitrary independent sequences on dyadic \(a,m,n\)-ranges,
\((m,n)=1\), one absolute value outside the complete sum, and phase
\(e(\vartheta a\overline m_n/n)\). The legal Round-160 dictionary is

\[
 (a,m,n;\,A,M,N;\,\vartheta)
 =(h,n_{\rm phys},j;\,C_g,C_g,J_g;\,1).
\tag{160.SL2}
\]

The coprimality condition is exact, but
\(S(N_0,h;n_{\rm phys})\) depends jointly on the source \(a\)- and
\(m\)-variables. The moving \(q_L\)-support also couples the source
\(m\)- and \(n\)-variables. Neither is one of the three independent
source sequences.

**Wright.** Theorem 2.1 of
[*Trilinear Kloosterman fractions I: partially fixed moduli and
unbalanced convolutions*, arXiv:2604.25177v2](https://arxiv.org/html/2604.25177v2)
uses the same independent coefficient geometry and phase
\(e(\vartheta a\overline m/(nR_0))\), with

\[
 M\ll N^2,\qquad R_0\ll M^A,\qquad \vartheta\in\mathbb Z\setminus\{0\}.
\tag{160.SL3}
\]

Here \(R_0=1\), \(\vartheta=1\), and (160.SL2) applies. Thus the only
nontrivial side condition is

\[
 C_g\ll J_g^2.
\tag{160.SL4}
\]

At \(g=1\), this is \(3\delta-2\ell\le1\), equivalently
\(\delta+2(\delta-\ell)\le1\). Wright's Corollary 2.2 and Theorem 2.3
have additional divisor-bounded and Siegel--Walfisz/dispersion
hypotheses; they are not invoked here and do not accept (160.SL1).

**Blomer--Milićević.** Theorem 1 of
[*Kloosterman sums in residue classes*, JEMS 17 (2015), 51--69,
DOI 10.4171/JEMS/498](https://ems.press/content/serial-article-files/32008?nt=1)
states, for fixed positive \(m,n,q\),

\[
 \sum_{(c,q)=1}\frac{S(m,n;c)}{\sqrt c}
 f(c)f_\infty(c/C)
 \ll_{f_\infty,\varepsilon}
 C^{1/2+2\theta}\|\widehat f\|_1(mnq)^\varepsilon
\tag{160.SL5}
\]

uniformly for \(mn\le C^2\). For fixed \(g,j,h\), the exact map is

\[
 c=n_{\rm phys},\quad (m,n)_{\rm source}=(N_0,h),\quad
 q=q_j=\operatorname{lcm}(4,j),
\tag{160.SL6}
\]

\[
 f_{j,h}(c)=\chi_4(c)e(h\overline c_j/j),
\tag{160.SL7}
\]

and the remaining factors of (160.SL1), after changing
\(S/c\) into \(S/\sqrt c\), form the scalar \(f_\infty\). A legal
application requires uniform compact support and all source-dependent
seminorms of that scalar test; no theorem constant is uniform merely
because nodal values are prescribed.

Theorem 4 of the same paper is an exact \(H+M+E\) spectral identity. For
each character \(\chi\pmod q\), with primitive conductor \(q_1\), it has
Möbius terms \(d\mid q\), hence nonzero terms only for squarefree \(d\),
at level \(dq_1\). It retains the full holomorphic, Maaß (including
exceptional parameters), and singular-cusp Eisenstein spectra. Its bases
contain the source's newform and oldclass decomposition.

**Deshouillers--Iwaniec.** Theorems 2 and 5 of
[*Kloosterman Sums and Fourier Coefficients of Cusp Forms*,
Invent. Math. 70 (1982), 219--288](https://doi.org/10.1007/BF01390728)
use one fixed cusp and the same coefficient sequence in the spectral
quadratic forms. They do not state a varying-\(j\), varying-level large
sieve for the family (160.SL7), and their printed form is not itself the
odd-nebentypus weight-one theorem required by the growing-level encoding.

**Assing--Blomer--Li.** Theorem 2.4 of
[*Uniform Titchmarsh divisor problems*,
arXiv:2005.13915](https://arxiv.org/html/2005.13915) bounds

\[
 \sum_{(c,r)=1}\frac1c\sum_m\alpha_mF(m,c)
 S(m\overline r,\pm n;sc),
\tag{160.SL8}
\]

where \(n,r,s\) are fixed, \((r,s)=1\), \(\alpha_m\) is one sequence,
\(F\) is supported on \([M,2M]\times[C,2C]\), and

\[
 F^{(\nu_1,\nu_2)}
 \ll_{\nu_1,\nu_2}
 Z^{\nu_1+\nu_2}M^{-\nu_1}C^{-\nu_2},\qquad
 \left(\frac{Mn}{s^2rC^2}\right)^{1/2}\ll Z.
\tag{160.SL9}
\]

Kloosterman symmetry permits the comparison
\((m,c,n,r,s)=(h,n_{\rm phys},N_0,1,1)\), but (160.SL1) is not one
common sequence times a legal small-\(Z\) test, and (160.SL8) has no
\(\chi_4(c)\) modulus twist. One may instead take \(r=2\), \(s=1\),
and source \(m=2h\) to restrict \(c\) to odd integers and recover
\(S(h,N_0;c)\); the remaining sign \(\chi_4(c)\) must then enter the
smooth test and has the large derivative cost recorded below.

## 3. Proof or derivation

### 3.1 Bettin--Chandee and Wright

Under (160.SL2), Bettin--Chandee's theorem is source-legal only after
the joint factors have been replaced by independent sequences. Grant,
favourably, unit projective cost for the moving \((n,j)\)-amplitude and
for the normalized matrix \(S(N_0,h;n)/\sqrt{C_g}\). The product of
source coefficient norms with the physical normalization is then

\[
 \frac{\sqrt{C_gJ_g}}{K}.
\tag{160.SL10}
\]

Substitution in the two printed Bettin--Chandee terms gives

\[
 \frac{C_g^{29/20}J_g^{17/20}}K,\qquad
 \frac{C_g^{3/2}J_g^{7/8}}K.
\tag{160.SL11}
\]

At \(g=1\), division by the accepted divisor capacity \(R/K\) gives

\[
 R^{9/20}K^{17/20}>X^{9/40},\qquad
 R^{1/2}K^{7/8}>X^{1/4}.
\tag{160.SL12}
\]

These inequalities use only \(\delta<1/2\) and \(\ell\ge0\). When
(160.SL4) holds, the first bracket term in Wright's Theorem 2.1 gives the
second quantity in (160.SL11); outside (160.SL4), that theorem is
inapplicable. Thus the report's favourable source-capacity screen is
algebraically and source-theoretically correct. It remains a screen of an
artificial rank-one surrogate, not a bound or lower bound for (160.SL1).

### 3.2 Mellin price and exact induced levels

Take \(j=p\ge5\) prime and \(p\nmid h\). On
\((\mathbb Z/p\mathbb Z)^*\), inversion gives

\[
 \widehat f_h(\psi)
 =\frac1{\sqrt{p-1}}\sum_{b\bmod p}^{*}\psi(b)e(hb/p).
\tag{160.SL13}
\]

The principal coefficient has magnitude \(1/\sqrt{p-1}\), while every
nonprincipal coefficient has magnitude \(\sqrt{p/(p-1)}\). Hence

\[
 \|\widehat f_h\|_1
 =(p-2)\sqrt{\frac p{p-1}}+\frac1{\sqrt{p-1}}
 \asymp p.
\tag{160.SL14}
\]

Tensoring with \(\chi_4\) on the mod-\(4\) unit group changes
(160.SL14) by one fixed factor. Therefore (160.SL5) costs order \(p\)
in its arithmetic Mellin norm for these rows.

For the level ledger, the only characters with nonzero transform are

\[
 \chi=\chi_4\psi\pmod{4p}.
\tag{160.SL15}
\]

If \(\psi\) is principal, \(q_1=4\). Since the nonzero Möbius divisors of
\(4p\) are \(1,2,p,2p\), the levels are

\[
 4,\ 8,\ 4p,\ 8p.
\tag{160.SL16}
\]

This component is odd. If \(\psi\) is nonprincipal, it is primitive
modulo \(p\), so \(q_1=4p\) and the levels are

\[
 4p,\ 8p,\ 4p^2,\ 8p^2.
\tag{160.SL17}
\]

As nonprincipal \(\psi\) ranges over characters modulo \(p\ge5\), both
values of \(\psi(-1)\) occur, and hence both source parities occur in
(160.SL17). Theorem 4 then retains the compatible complete \(H+M+E\)
ledger at each level. This proves the growing-level claim with the parity
qualification in Section 1.

The source Fourier arguments also vary literally with \(j\):

\[
 m_0=\frac{N_0}{(N_0,q_j^\infty)},\qquad
 n_0q_1^2=h(N_0,q_j^\infty)q_1^2.
\tag{160.SL18}
\]

Thus arbitrary gcd strata cannot be replaced by one fixed spectral
sequence.

### 3.3 Additive bandwidth, Linnik range, and long frequencies

The exact additive expansion is

\[
 1_{(c,j)=1}e(h\overline c_j/j)
 =\frac1j\sum_{t\bmod j}S(h,-t;j)e(tc/j).
\tag{160.SL19}
\]

For prime \(p\) and \(h\not\equiv0\pmod p\), Parseval and Weil imply

\[
 \sum_{t\bmod p}\left|\frac{S(h,-t;p)}p\right|^2
 =\frac{p-1}{p},
\tag{160.SL20}
\]

while any \(B=o(p)\) frequencies carry \(o(1)\) of this mass. On
\(c=C_gx\), modes \(|t|\asymp p\) have normalized derivatives of size
\(\asymp C_g\). Therefore any scalar use of (160.SL19) in
(160.SL8) requires \(Z\gg C_g\) on a positive proportion of the
Fourier mass. Even before this inverse-residue price, (160.SL9) forces

\[
 Z\gg\sqrt{X/C_g}=\sqrt{Dg}.
\tag{160.SL21}
\]

The additional factor \(\chi_4(c)\) is absent from (160.SL8). With the
legal choice \(r=2\), \(s=1\), and source \(m=2h\), the condition
\((c,r)=1\) restricts to odd \(c\) and
\(S(2h\overline2,N_0;c)=S(h,N_0;c)\). On those moduli,
\(\chi_4(c)=e((c-1)/4)\), whose normalized frequency is
\(\asymp C_g\). Thus even this legal encoding cannot be inserted at
\(Z=O(1)\).

For (160.SL5), the exact Linnik condition is

\[
 N_0h\le C_g^2,\qquad
 h\ll H_{\rm Lin}(g):=\frac{C_g^2}{X}
 \asymp\frac{K}{Lg^2}.
\tag{160.SL22}
\]

Consequently

\[
 \frac{H_{\rm Lin}(g)}{J_g}\asymp\frac1{Lg},\qquad
 \frac{H_{\rm Lin}(g)}{C_g}\asymp\frac1{Dg}.
\tag{160.SL23}
\]

No cited theorem covers the remaining \(1\le h<n\) with the literal
coefficients. Complete Fourier summation reconstructs the original
reciprocal row, so there is no algebraic deletion of the complement.
This is a coverage failure only: the identity supplies no quantitative
lower bound for the complement.

### 3.4 Common-sequence and vector scope

Deshouillers--Iwaniec can estimate a quadratic form built from one common
sequence at a fixed cusp. It does not accept the family of
\(h\)-dependent arithmetic weights (160.SL7) while \(j\), \(q_j\), and
the levels (160.SL16)--(160.SL17) vary. Assing--Blomer--Li allows
smooth joint \((h,c)\)-dependence, but only after the character and
inverse-residue factors have been represented with the derivative
parameter in (160.SL9). Equations (160.SL19)--(160.SL21) show why that
representation is not a low-bandwidth scalar test.

None of these facts excludes a new theorem acting on the full
\((j,n,h)\)-array, including \(S(N_0,h;n)\), before scalarization or
positive norms.

## 4. First doubtful or unproved step

The first unproved positive step is a coefficient-sensitive vector trace
or large-sieve theorem for the literal weighted matrix

\[
 \chi_4(n)e(h\overline n_j/j-h/(jn))
 S(N_0,h;n)q_L(4Xj/(gn^2)),
\]

with the moving support, complete \(1\le h<n\) range, every induced
level and spectral piece, and an aggregate norm smaller than the required
boundary saving. No cited source states such a theorem.

The source audit also cannot turn the unweighted nuclear-norm calculation
into a lower bound for the literal matrix. As the post-blind review
observes, a literal weighted robustness statement first needs a proved
nonzero profile buffer containing complete residue classes, and even that
would not rule out cancellation created by the Kloosterman array. The
source results audited here are upper-bound interfaces only.

Finally, the exact self-return leaves the long-frequency complement
uncontrolled; it does not certify that complement as large. Any promoted
wording must preserve that distinction.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Bettin--Chandee hypotheses and map | **PASS.** (160.SL2) preserves positivity, dyadic lengths, \((n_{\rm phys},j)=1\), integral frequency \(1\), independent sequences, and the single outside absolute value. The joint Kloosterman coefficient and moving support are not legal source sequences. |
| Wright hypotheses and map | **PASS.** \(R_0=1\) is legal and the exact extra range is (160.SL4). The source-capacity comparison is correct where applicable. Wright's dispersion corollaries are not silently imported. |
| Blomer--Milićević scalar theorem | **PASS with test-norm caveat.** The map (160.SL6)--(160.SL7), fixed positive arguments, unit modulus classes, \(S/\sqrt c\) normalization, and Linnik range are exact. Uniformity still depends on the scalar test seminorms. |
| Mellin \(L^1\) price | **PASS.** (160.SL14) proves the prime price \(\asymp p\) for \(p\nmid h\); the mod-\(4\) factor changes only a constant. |
| Induced levels and parities | **PASS after repair.** The exact character-by-character ledger is (160.SL16)--(160.SL17). Both parities occur across the conductor-\(4p\) family for \(p\ge5\), not at pure levels \(4/8\). |
| Holomorphic/Maaß/exceptional/Eisenstein/new/old ledger | **PASS as an inventory.** Theorem 4 prints \(H+M+E\) and its bases retain new/old components and all singular cusps. No spectral term has been estimated for the owner. |
| Deshouillers--Iwaniec common sequence | **PASS.** The fixed-cusp, one-sequence interface does not accept the varying arithmetic weights and levels. |
| Assing--Blomer--Li | **PASS after character repair.** The theorem and \(Z\)-hypotheses are quoted correctly. The inverse-residue high modes force \(Z\gg C_g\), and \(\chi_4(c)\) is an additional unaccepted modulus factor. |
| Linnik and long-\(h\) complement | **PASS with scope repair.** (160.SL22)--(160.SL23) are exact. The complement is source-uncontrolled, not proved large. |
| Moving support and endpoints | **OPEN for a positive source use.** A scalar application must provide uniform smooth extensions and seminorms. No endpoint is discarded, and no owner-saving estimate follows. |
| Bespoke vector theorem | **OPEN.** No cited theorem rules it out. |
| Owner and downstream scope | **PASS.** No target, strict range, complete M2, M9, bridge, quarter theorem, or exponent improvement follows. |

The review is entirely analytical and source-comparative; no numerical
experiment was used.

## 6. Dependencies and exact artifacts used

The local artifacts read were:

- `protocol.md`;
- `state/proof_obligations.yml`, especially the five Round-160 targets and
  the accepted Round-135 and Round-143 obstruction nodes;
- `state/active_campaign.yml`;
- `strategy/round160_m2_unbalanced_inverse_selector_reciprocity_strategy.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/candidates/conductor_round160_reciprocity_seed.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/reciprocity_projective_source_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/candidates/conductor_round160_reciprocity_projective_obstruction.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/post_blind_reciprocity_projective_seam.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/kuznetsov_source_hypothesis_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/source_post_unmask_spectral_claims_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/source_post_unmask_discovery_formula_audit.md`; and
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/primary_source_manifest.md`.

The primary sources checked were:

1. S. Bettin and V. Chandee,
   [*Trilinear forms with Kloosterman fractions*,
   arXiv:1502.00769v1](https://arxiv.org/html/1502.00769v1),
   Theorem 1 and Remark 1.
2. T. Wright,
   [*Trilinear Kloosterman fractions I: partially fixed moduli and
   unbalanced convolutions*,
   arXiv:2604.25177v2](https://arxiv.org/html/2604.25177v2),
   Theorem 2.1 and the hypotheses of Corollary 2.2 and Theorem 2.3.
3. V. Blomer and D. Milićević,
   [*Kloosterman sums in residue classes*, JEMS 17 (2015), 51--69](https://ems.press/content/serial-article-files/32008?nt=1),
   normalized Mellin transform (1.2), Theorem 1, Corollary 2, encoding
   (2.3)--(2.5), the new/old bases in Section 3, \(H+M+E\) in (4.6),
   singular-cusp criterion (5.1), and Theorem 4.
4. J.-M. Deshouillers and H. Iwaniec,
   [*Kloosterman Sums and Fourier Coefficients of Cusp Forms*,
   Invent. Math. 70 (1982), 219--288](https://doi.org/10.1007/BF01390728),
   Theorems 2 and 5; the
   [official GDZ scan](https://gdz.sub.uni-goettingen.de/id/PPN356556735_0070?tify=%7B%22view%22%3A%22info%22%2C%22pages%22%3A%5B243%5D%7D)
   was used for the printed-page check.
5. E. Assing, V. Blomer, and J. Li,
   [*Uniform Titchmarsh divisor problems*,
   arXiv:2005.13915](https://arxiv.org/html/2005.13915),
   Theorem 2.4.

The withdrawn arXiv:2601.00292 supplied no theorem.

## 7. Recommended state effect

**Revise and then promote only the source-scoped scalar-route
obstruction.** The promotable source content is:

- the exact Bettin--Chandee/Wright dictionary and independent-coefficient
  mismatch;
- the prime Mellin price (160.SL14);
- the exact growing-level ledger (160.SL16)--(160.SL18), with the repaired
  parity wording;
- the additive high-bandwidth and Assing--Blomer--Li \(Z\)-cost;
- the Linnik coverage gap (160.SL22)--(160.SL23), stated as lack of
  control rather than a lower bound; and
- the conclusion that the cited scalar/common-sequence theorems do not
  prove an owner-saving estimate.

Retain `M9-M2-smooth-unbalanced-three-quarter-estimate` as open. Do not
promote the conditional weighted-profile lower bound, a universal
projective obstruction, or an impossibility result for bespoke vector
methods. Do not change M9-M2, M9, the bridge, the quarter target, or any
global exponent.
