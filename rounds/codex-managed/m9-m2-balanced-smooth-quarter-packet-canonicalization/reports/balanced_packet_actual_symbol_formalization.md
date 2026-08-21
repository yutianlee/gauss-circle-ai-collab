# Round 112 formalization: balanced smooth actual-symbol quarter packet

## 1. Result: normalization lemma and literal-symbol no-go

For one fixed physical smooth residual \((D,L)\)-block, with only a bounded
number of internal fixed-comparability subdivisions, the character algebra,
the two quarter shifts, their order, the factor \(1/(2i)\), the smooth gcd
Poisson identity, the positive/negative-frequency conjugacy, the prior-owner
correction, the norm hierarchy, and the capacity ledger can all be fixed
unambiguously.

The resulting structural identity is

\[
 \mathcal T_{\mathrm{bal,res}}^+
 =\frac1{2i}\sum_{\omega\in\Omega(D,L)}
       \sum_{G\in\mathscr G_{\mathrm{sm}}(L)}G\mathcal Q_{\omega,G}(R)
   -\mathcal E_{\mathrm{sq}}^{<}-\mathcal E_{\mathrm{near}}^{<},
 \qquad R=\sqrt X,                                      \tag{112.F1}
\]

where \(\mathcal Q_{\omega,G}\) is the \(1/4\)-packet minus the
\(3/4\)-packet.  The two correction sums are finite physical sums, are
already target-safe, and are necessary: the smooth packet is the transform
of the **full** small-gcd sum.  Exact-square or near-square indicator masks
must not be inserted into its smooth \(g/G\)-profile.

There is nevertheless a rigorous no-go for the requested *literal
actual-symbol* theorem from the permitted artifacts.  Those artifacts never
define the finite set \(\Omega(D,L)\), its exact denominator and frequency
profiles, the clipped/floored/starred endpoint weights, or the
support-entry/support-exit coefficients.  In particular, they only call
\(q_L\) “the Vaaler/dyadic amplitude,” write \(c_D\asymp1\), and introduce
\(F_{\omega,u,v,G}\) without defining it.  Consequently (112.F1) can be
formalized exactly only as a typed identity conditional on an atom
dictionary; it cannot be certified as the requested standalone literal
actual-symbol formula without inventing missing data.

Thus the result is:

\[
 \boxed{\text{all universal algebraic seams pass, but the literal atom
 dictionary is the first unresolved normalization seam.}}               \tag{112.F2}
\]

Once that dictionary is supplied, the first genuinely unproved analytic
statement is the outside-absolute signed estimate

\[
 \boxed{
 \left|\sum_{\omega\in\Omega(D,L)}
       \sum_{G\in\mathscr G_{\mathrm{sm}}(L)}G\mathcal Q_{\omega,G}(R)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon .}               \tag{112.F3}
\]

No estimate, M9-M2 statement, endpoint-uniformity statement, M9 statement,
or exponent improvement is proved here.

## 2. Exact statement and hypotheses

Write

\[
 e(t)=e^{2\pi i t},\qquad
 \widehat F(\xi)=\int_{\mathbb R}F(x)e(-x\xi)\,dx,
 \qquad R=\sqrt X,qquad X\ge2\text{ real}.             \tag{112.F4}
\]

Fix one physical smooth residual block with denominator scale \(D\), positive
frequency scale \(L\),

\[
 H_D=\lfloor DX^{-1/4}\rfloor,\qquad
 K=\frac{XL}{D^2},\qquad 1\le \frac KL\le16,
 \qquad 1\le L\le R^{1/2}.                             \tag{112.F5}
\]

The boundary \(K/L=16\) belongs to the balanced class.  The label
\(\omega\in\Omega(D,L)\) may index only the bounded internal subdivisions
needed to put this one physical block into fixed compact rectangles.  It may
not range over distinct dyadic physical \((D,L)\)-blocks; those are bounded
separately in the physical one-count assembly.

The audited Vaaler coefficient is

\[
 \alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h},
 \qquad
 \beta_{h,H}
 =-\frac{\Phi(|h|/(H+1))\chi_4(|h|)\mathbf1_{2\nmid h}}
          {\pi |h|}.                                    \tag{112.F6}
\]

In particular \(\beta_{-h,H}=\beta_{h,H}\in\mathbb R\).  A literal atom
dictionary would have to give, for each \(\omega\), a real compactly
supported symbol \(a_{\omega,X}(h,k)\) including every actual Vaaler taper,
denominator profile, frequency subdivision, height floor, star, support
crossing, and real-\(X\) label, with

\[
 \sum_{\omega\in\Omega(D,L)}a_{\omega,X}(h,k)
   =a_{D,L,X}(h,k)                                      \tag{112.F7}
\]

on the one fixed physical block.  The most explicit template justified by
the permitted context is

\[
 a_{\omega,X}(h,k)
 =q_{\omega,X}(h)
   \left(\frac{LK}{hk}\right)^{3/4}
   W_{\omega,X}\!\left(\sqrt{\frac{hX}{4kD^2}}\right),
 \quad
 q_{\omega,X}(h)
 =\Phi\!\left(\frac{h}{H_D+1}\right)\eta_{\omega,X}^{\star}(h),           \tag{112.F8}
\]

for positive \(h,k\).  Here \(\eta_{\omega,X}^{\star}\) must contain the
literal dyadic/clipped/starred frequency weight, while \(W_{\omega,X}\)
must be the literal smooth physical denominator profile.  Formula (112.F8)
is a template, not a completed definition: neither
\(\eta_{\omega,X}^{\star}\) nor \(W_{\omega,X}\), nor their crossing
labels, are supplied in the permitted artifacts.

For the gcd partition, fix once and for all a real
\(\vartheta\in C_c^\infty((1/2,2))\) with

\[
 \sum_{G\in2^{\mathbb Z}}\vartheta(t/G)=1\qquad(t>0).   \tag{112.F9}
\]

Let \(\mathscr G_{\mathrm{sm}}(L)\) consist of the dyadic \(G\) for which the
whole support of \(\vartheta(g/G)\) lies below \(L^{1/2}\).  The at most
boundedly many shells whose support crosses \(L^{1/2}\), together with all
larger shells, belong to the large/boundary-gcd owner.  On a small shell put

\[
 F_{\omega,u,v,G}(x)
 :=\vartheta(x)a_{\omega,X}(Gxu,Gxv),                 \tag{112.F10}
\]

extended by zero off its positive compact support.  No square, near-square,
or other arithmetic owner mask is allowed in (112.F10).

For \((u,v)=1\) and \(u\) odd, define the exact signed packet

\[
\begin{aligned}
 \mathcal Q_{\omega,G}(R)
 :=\sum_{\substack{u,v\ge1\\(u,v)=1\\u\ \mathrm{odd}}}
 \chi_4(u)\sum_{n\in\mathbb Z}\Big[&
 \widehat F_{\omega,u,v,G}
   \big(G(n-R\sqrt{uv}-\tfrac14)\big)\\
 &-\widehat F_{\omega,u,v,G}
   \big(G(n-R\sqrt{uv}-\tfrac34)\big)\Big].          \tag{112.F11}
\end{aligned}
\]

The physical \((u,v)\)-sum is finite; the Poisson \(n\)-sum is an exact
absolutely convergent Schwartz series.  Thus “finite packet” can mean a
finite physical label set, not a finite dual \(n\)-sum.

Define the exact small-shell prior-owner corrections using the same smooth
partition:

\[
\begin{aligned}
 \mathcal E_{\mathrm{sq}}^{<}
 :=\sum_{\omega,G\in\mathscr G_{\mathrm{sm}}}
 \sum_{\substack{g,u,v\ge1\\(u,v)=1\\g,u\ \mathrm{odd}}}
 &\vartheta(g/G)\chi_4(g)\chi_4(u)
 a_{\omega,X}(gu,gv)e(Rg\sqrt{uv})
 \mathbf1_{uv\text{ is a square}},                                  \\
 \mathcal E_{\mathrm{near}}^{<}
 :=\sum_{\omega,G\in\mathscr G_{\mathrm{sm}}}
 \sum_{\substack{g,u,v\ge1\\(u,v)=1\\g,u\ \mathrm{odd}}}
 &\vartheta(g/G)\chi_4(g)\chi_4(u)
 a_{\omega,X}(gu,gv)e(Rg\sqrt{uv})                                  \\
 &\times\mathbf1_{uv\text{ not a square}}
 \mathbf1_{0<\operatorname{dist}(g\sqrt{uv},\mathbb Z)\le R^{-1}}.
                                                               \tag{112.F12}
\end{aligned}
\]

Then (112.F1) is an exact identity for the small-gcd, nonsquare,
non-near-square positive dual child.  The accepted counting bounds give

\[
 |\mathcal E_{\mathrm{sq}}^{<}|+|\mathcal E_{\mathrm{near}}^{<}|
 \ll_\varepsilon L^{1+\varepsilon},                  \tag{112.F13}
\]

and the large/boundary-gcd owner is \(O(L^{3/2})\) absolutely.  Fixed
comparability \(K/L\le16\) changes only fixed constants.

For the full smooth positive-frequency physical block, the accepted
stationary transform has the exact leading normalization

\[
 \mathcal B_{\mathrm{bal,res}}^+
 =-\frac{e(1/8)}{2\pi}X^{1/4}(LK)^{-3/4}
 \left\{
   \frac1{2i}\sum_{\omega,G\in\mathscr G_{\mathrm{sm}}}
       G\mathcal Q_{\omega,G}(R)
   -\mathcal E_{\mathrm{sq}}^{<}-\mathcal E_{\mathrm{near}}^{<}
 \right\}
 +\mathcal E_{\mathrm{tr}},                                  \tag{112.F14}
\]

where the bounded number of smooth transform errors satisfies
\(\mathcal E_{\mathrm{tr}}=O(1)\).  Since the physical profiles and the Vaaler
coefficient are real and even in signed frequency,

\[
 \mathcal B_{\mathrm{bal,res}}^-
 =\overline{\mathcal B_{\mathrm{bal,res}}^+},
 \qquad
 \mathcal B_{\mathrm{bal,res}}
 =2\operatorname{Re}\mathcal B_{\mathrm{bal,res}}^+.   \tag{112.F15}
\]

Consequently (112.F3) is target-equivalent, up to the already bounded
owners and transform error, to the **complex positive-frequency child** and
implies the real physical block bound \(O_\varepsilon(X^{1/4+\varepsilon})\).
The converse from a bound for the real part in (112.F15) to the complex
modulus in (112.F3) is not a norm equivalence and is not asserted.

For later norm hygiene, set

\[
 \mathfrak D:=\left|\sum_{\omega,G}G\mathcal Q_{\omega,G}\right|,
 \qquad
 \mathfrak L_1:=\sum_{\omega,G}G|\mathcal Q_{\omega,G}|.                \tag{112.F16}
\]

Then \(\mathfrak D\le\mathfrak L_1\); the shellwise estimate is strictly
stronger.  A different stronger sufficient route is the character-preserving
row Gram.  If \(A_{\mathrm{res}}\) denotes the exact finite residual coefficient,

\[
 \mathfrak G
 :=\sum_{k\asymp K}
 \left|\sum_{h\asymp L}\chi_4(h)A_{\mathrm{res}}(h,k)
 e(R\sqrt{hk})\right|^2,                               \tag{112.F17}
\]

then Cauchy in \(k\) gives

\[
 |\mathcal T_{\mathrm{bal,res}}^+|^2\ll K\mathfrak G. \tag{112.F18}
\]

Thus \(\mathfrak G\ll_\varepsilon L^2X^\varepsilon\) is sufficient when
\(K\asymp L\).  It retains the character inside the squared row; its
off-diagonal has the exact factor
\(\chi_4(h)\chi_4(h+2r)=(-1)^r\).  The Gram and shellwise \(\ell^1\)
conditions are two different stronger sufficient statements; neither is
identified with the direct linear target.

Finally, the best currently proved balanced envelope is

\[
 |\mathcal T_{L,L}(R)|
 \ll_\varepsilon X^\varepsilon
 \min(L^2,R^{1/2}L^{1/2}),                            \tag{112.F19}
\]

so its exact loss relative to \(L^{3/2}\) is

\[
 \Delta(L)=\min\!\left(L^{1/2},\frac{R^{1/2}}L\right). \tag{112.F20}
\]

The worst point is \(L=R^{1/3}=X^{1/6}\), where
\(\Delta(L)=R^{1/6}=X^{1/12}\).  Fixed comparability
\(1\le K/L\le16\) leaves this power ledger unchanged.

## 3. Proof and derivation

First, for every integer \(g\),

\[
 e(g/4)-e(3g/4)=2i\chi_4(g).                         \tag{112.F21}
\]

It is zero for even \(g\), equals \(2i\) for
\(g\equiv1\pmod4\), and equals \(-2i\) for
\(g\equiv3\pmod4\).  This proves (112.F6) from the audited Vaaler
coefficient and fixes the \(1/(2i)\) normalization.

Second, on a gcd shell write

\[
 h=gu,\qquad k=gv,\qquad (u,v)=1.                    \tag{112.F22}
\]

Every contributing \(h\) is odd, hence both \(g\) and \(u\) are odd and

\[
 \chi_4(h)=\chi_4(g)\chi_4(u),\qquad
 e(R\sqrt{hk})=e(Rg\sqrt{uv}).                       \tag{112.F23}
\]

For a smooth full shell, Poisson summation with convention (112.F4) gives

\[
 \sum_{g\in\mathbb Z}F(g/G)e(\alpha g)
 =G\sum_{n\in\mathbb Z}\widehat F(G(n-\alpha)).      \tag{112.F24}
\]

Insert (112.F21) and take respectively
\(\alpha=R\sqrt{uv}+1/4\) and
\(\alpha=R\sqrt{uv}+3/4\).  The result is

\[
 \sum_g\chi_4(g)F_{\omega,u,v,G}(g/G)e(Rg\sqrt{uv})
 =\frac{G}{2i}\sum_n\left[
   \widehat F\big(G(n-R\sqrt{uv}-\tfrac14)\big)
  -\widehat F\big(G(n-R\sqrt{uv}-\tfrac34)\big)
 \right].                                             \tag{112.F25}
\]

Summing (112.F25) over \(\omega,u,v,G\) proves the full small-gcd packet
identity with the \(1/4\) term first and the \(3/4\) term subtracted.

Third, apply owners by first match.  Exact squares and nonsquare
\(R^{-1}\)-near-squares are finite subsets of the full small-gcd sum, so
subtracting exactly (112.F12) proves (112.F1).  Inserting either arithmetic
indicator into (112.F10) would generally make its \(g/G\)-dependence
nonsmooth and would invalidate (112.F24); this is why the corrections must
remain outside the Fourier profile.  Exact-square counting, the elementary
near-square interval count, and the dyadic gcd count give (112.F13) and the
\(O(L^{3/2})\) large/boundary-shell bound.

Fourth, complementary divisors do not supply an omitted cancellation.  For
odd \(m\), if

\[
 c(m)=\sum_{hk=m}\chi_4(h)a(h,k),
\]

then

\[
 c(m)=\frac12\sum_{hk=m}\chi_4(h)
       \big(a(h,k)+\chi_4(m)a(k,h)\big).              \tag{112.F26}
\]

Thus a symmetric symbol cancels the \(m\equiv3\pmod4\) sector but
reinforces the \(m\equiv1\pmod4\) sector.  If \(m\) is even, every
contributing \(h\) is odd and its complement \(k\) is even, so
\(\chi_4(k)=0\) and there is no character-bearing swapped term.  The actual
one-sided Vaaler and ratio profiles are not symmetric in any event.

Fifth, (112.F15) follows directly from the reality and evenness of
\(\beta_{h,H}\), the reality of the physical profiles, symmetric frequency
stars, and \(e(-t)=\overline{e(t)}\).  Negative frequency is therefore the
conjugate physical orientation; it is not a second independent copy to be
summed and then followed by another outer \(2\operatorname{Re}\).

Sixth, substitute (112.F1) into the accepted smooth stationary transform to
obtain (112.F14).  Since \(K\asymp L\), a bound \(L^{3/2}X^\varepsilon\)
inside braces becomes \(X^{1/4+\varepsilon}\) after multiplication by
\(X^{1/4}(LK)^{-3/4}\).  The owner corrections and the bounded transform
error are target-safe.  This proves the positive-child equivalence and the
physical implication claimed after (112.F15), as well as the norm relations
(112.F16)--(112.F18).

Finally, dividing (112.F19) by \(L^{3/2}\) proves (112.F20).  Equating its
two branches gives \(L=R^{1/3}\), and substitution gives the worst deficit
\(R^{1/6}=X^{1/12}\).  This is a capacity calculation, not an estimate for
(112.F3).

Every step above is exact conditional on the atom identity (112.F7).  The
permitted context does not instantiate that identity, so the derivation
cannot be promoted from a typed formula to a literal actual-symbol theorem.

## 4. First doubtful or unproved step

The first unresolved step is formal, before the analytic estimate: construct
and verify the atom dictionary

\[
 \mathscr A_{D,L}(X)=
 \big\{\omega,\eta_{\omega,X}^{\star},W_{\omega,X},
 K,\text{ floor/star/crossing tags},
 a_{\omega,X},\mathcal E_{\omega,\mathrm{tr}}\big\}_{\omega\in\Omega(D,L)}
                                                               \tag{112.F27}
\]

for each one fixed physical smooth residual block.  The dictionary must
verify all of the following coefficientwise:

- the bounded internal subdivision identity (112.F7), without summing
  distinct physical dyadic blocks;
- the exact \(H_D=\lfloor DX^{-1/4}\rfloor\) dependence and Vaaler taper;
- every half-open endpoint and star weight, including empty, singleton, and
  support-entry/support-exit cases;
- exclusion of the unique hard profile and retention of real-\(X\) labels;
- the exact stationary symbol and the owner of every transform boundary
  term;
- one fixed smooth gcd partition and the complete boundary-shell owner.

None of the permitted artifacts supplies these data.  The phrases “actual
symbol,” “literal decorations,” and “retain floors and stars” are
requirements, not definitions.  In particular, the candidate's
\(F_{\omega,u,v,G}\) is the object that needs to be defined; it cannot serve
as its own definition.

After (112.F27) is supplied and checked, the first analytic unproved step is
exactly (112.F3).  Neither the shellwise \(\ell^1\) estimate, the Gram bound,
an unsigned quarter-resonance count, a product-fibre energy, nor an
arbitrary-coefficient bilinear theorem is equivalent to it.  The latter can
also be false for phase-conjugating coefficients even though the actual
packet may cancel.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `quarter_shift_sign_and_2i_normalization` | **Pass.** Equations (112.F21), (112.F24), and (112.F25) give exactly \((1/4)-(3/4)\) and the prefactor \(G/(2i)\) under the stated Fourier convention. |
| `fixed_smooth_gcd_partition` | **Pass structurally; literal-data gap.** A fixed partition and target-safe crossing-shell owner are given in (112.F9). The repository statement does not identify the actual chosen partition, so literal equality with a pre-existing atom list cannot yet be checked. |
| `odd_h_implies_odd_g_and_u` | **Pass.** It is (112.F23); even \(g\) or \(u\) gives zero character. |
| `even_product_and_complementary_divisor` | **Pass.** Equation (112.F26) handles odd products; for even products the complementary divisor has zero \(\chi_4\)-weight. |
| `positive_negative_frequency_conjugacy` | **Pass conditional on the required real-even star dictionary.** The audited \(\beta\) is real-even and gives (112.F15); no second orientation may be double counted. |
| `exact_square_near_square_and_large_gcd_owners` | **Pass with correction.** The first-match table below is disjoint. The square and near-square sums must be subtracted as (112.F12), not hidden in \(F\). |
| `hard_endpoint_exclusion` | **Pass.** Only a full smooth interior profile enters (112.F8)--(112.F11). The unique band containing \(d=\lfloor\sqrt X\rfloor\) remains with the hard density-discrepancy child. |
| `floors_stars_profiles_and_support_crossings` | **Fail as a literal formalization gate.** Their retention is asserted in the graph, but their coefficient formulas and finite label set are absent from every permitted artifact. This is the first seam (112.F27). |
| `outside_absolute_G_sum_vs_shellwise_l1_and_Gram` | **Pass.** Equations (112.F16)--(112.F18) separate the direct linear target from two stronger sufficient norms. |
| `real_X_and_balanced_comparability` | **Pass.** No integrality of \(R\) is used; \(X\) is real, \(H_D\) retains its floor, and \(1\le K/L\le16\) is fixed throughout. |
| `capacity_and_downstream_scope` | **Pass.** The maximum known deficit is \(X^{1/12}\) at \(L=X^{1/6}\). The smallest surviving signed target is (112.F3), and no downstream theorem is claimed. |

The exact first-match owner table for one physical residual block is:

| Priority | Label condition | Owner | Packet effect |
|---:|---|---|---|
| 1 | inactive bottom, Fejer residual, terminal frequency, full second-derivative region, or TTY wedge | previously proved physical owner | never enters \(\Omega(D,L)\) |
| 2 | the unique profile containing \(d=\lfloor\sqrt X\rfloor\) | hard top density-discrepancy child | excluded from smooth Poisson |
| 3 | smooth residual with \(K/L>16\) | unbalanced three-quarter child | excluded from the balanced packet |
| 4 | balanced smooth and \(hk\) an exact square | `BAL-SQ` | appears in the full small-gcd packet and is subtracted by \(\mathcal E_{\mathrm{sq}}^{<}\); large-shell incidences are owned here first |
| 5 | balanced smooth, nonsquare, and \(0<\operatorname{dist}(\sqrt{hk},\mathbb Z)\le R^{-1}\) | `BAL-NEAR` | appears in the full small-gcd packet and is subtracted by \(\mathcal E_{\mathrm{near}}^{<}\) |
| 6 | remaining balanced term in a gcd shell crossing \(L^{1/2}\), or a larger shell | `BAL-GCD-BDY` | removed before packetization as an entire smooth shell; absolute cost \(O(L^{3/2})\) |
| 7 | remaining balanced term in a full shell below \(L^{1/2}\) | `BAL-Q` | residual governed by (112.F1)--(112.F3) |

This ordering counts every physical incidence once and preserves smoothness
of every \(F_{\omega,u,v,G}\).

## 6. Dependencies and exact artifacts used

The derivation used only the assigned context:

- `protocol.md`;
- `state/proof_obligations.yml`, at graph SHA-256
  `5c49f612b262b1191fe74642ddd8e5d6c70e04b34a59fb1473487d5b5132d747`,
  especially the nodes `M9-M2-beta-algebra`, `M9-M2-character-factor`,
  `M9-M2-dyadic-weight-nondegeneracy`,
  `M9-M2-smooth-dual-three-quarter-equivalence`,
  `M9-M2-smooth-small-gcd-quarter-packet`,
  `M9-M2-smooth-balanced-quarter-packet-estimate`, and
  `M9-M2-physical-one-count-assembly`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/candidates/conductor_balanced_packet_interface.md`;
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/endpoint_dual_signed_attack.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/synthesis.md`;
- `rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/synthesis.md`;
- `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/synthesis.md`.

No Round-112 sibling report, web source, numerical experiment, or
unassigned artifact was used.  The work was entirely algebraic and
analytical.

## 7. Recommended state effect

- **Retain** `M9-M2-smooth-small-gcd-quarter-packet` as a proved structural
  reduction, with the explicit clarification that its smooth packet is the
  full small-gcd packet and that exact-square/near-square prior owners enter
  through the target-safe correction (112.F12).
- **Revise** the Round-112 candidate interface before any promotion: restrict
  \(\omega\) to bounded internal subdivisions of one fixed physical
  \((D,L)\)-block and replace its schematic error by an exact named owner
  correction plus a separately named transform error.
- **Retain open** `M9-M2-smooth-balanced-quarter-packet-estimate`.  Its first
  analytic target is (112.F3), with the absolute value outside the complete
  \((\omega,G)\)-sum for that one block.
- **Record** the literal atom dictionary (112.F27) as the first unresolved
  formalization seam.  Do not promote a standalone actual-symbol theorem
  until the exact profiles, floors, stars, crossings, and finite labels are
  written coefficientwise and checked against (112.F7).
- **Do not replace** (112.F3) by shellwise \(\ell^1\), Gram, product-fibre,
  unsigned, or arbitrary-coefficient statements without a proved bridge.
- **No change** to the statuses of the hard top child, the unbalanced smooth
  child, M9-M2, endpoint uniformity, M9, or the Gauss-circle target.
