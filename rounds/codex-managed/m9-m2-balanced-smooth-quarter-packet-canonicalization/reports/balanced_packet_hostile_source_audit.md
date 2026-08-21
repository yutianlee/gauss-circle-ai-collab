# Round 112 hostile/source audit: balanced smooth quarter packet

## 1. Result

**No-go result (with a smaller exact survivor).**  The displayed

\[
 \mathcal Q_{\omega,G}(R),\qquad
 \mathcal T_{\mathrm{bal,res}}^+
 ={1\over2i}\sum_{\omega,G}G\mathcal Q_{\omega,G}(R)
 +O_\varepsilon(L^{3/2}X^\varepsilon)
\]

cannot yet be certified as one standalone **literal actual-symbol residual
theorem**.  The obstruction is not the quarter-shift algebra: with
\(e(t)=e^{2\pi i t}\) and
\(\widehat F(\xi)=\int_{\mathbb R}F(x)e(-x\xi)\,dx\), the factor
\(1/(2i)\), the order \(1/4\) minus \(3/4\), and the Poisson arguments in
(112.C1) are correct.  The first failed seam is the missing owner-aware
atom dictionary.

More precisely, smooth Poisson in the actual gcd variable is exact for the
**full** small-gcd shell.  Exact-square and \(R^{-1}\)-near-square estimates
do not silently remove those atoms from its Fourier transform.  If
\(\mathcal T_{\mathrm{bal,res}}^+\) means the complement of those prior
owners, then (112.C2) requires explicit signed square and near-square
corrections (and an explicit last-gcd-shell correction).  Alternatively one
may insert their arithmetic complement into the gcd profile, but that
profile is no longer the uniformly smooth \(F_{\omega,u,v,G}\) displayed in
(112.C1).  The candidate supplies neither construction.

There is a second material scope failure.  An absolute value outside an
\(\omega\)-sum is licensed only after fixing one literal physical
\((D,L,\text{frequency sign})\) block and letting \(\omega\) index finitely
many internal subdivisions whose signed sum reconstructs that same block.
The accepted physical assembly is blockwise.  It supplies no cancellation
theorem across distinct denominator bands \(D\), frequency blocks \(L\), or
hard/smooth owners.  Thus (112.C3), if \(\omega\) ranges over literal
physical blocks, is weaker than the accepted parent and is not an admissible
replacement for it.

The smallest lawful survivor is therefore:

1. fix one real-\(X\), balanced, smooth physical block \(B=(D,L,+)\), with
   \(1\le K/L\le16\);
2. use a fixed smooth gcd partition and apply Poisson to the **full**
   small-gcd contribution of \(B\), with a separately named terminal gcd
   shell;
3. either leave square and near-square atoms inside that packet, or subtract
   them by explicit signed correction sums; and
4. pose the outside-absolute estimate only for the signed recombination of
   the internal labels of this one block.

That exact survivor is a reduction only.  Its signed
\(L^{3/2}X^\varepsilon\) estimate remains open.  No balanced block, M9-M2,
endpoint, M9, or exponent claim is proved here.

## 2. Exact statement and hypotheses

The normalization that can be certified is the following abstract
full-small-gcd identity.  It deliberately does not pretend that the missing
literal physical coefficient has already been supplied.

Let \(X>0\) be real, \(R=\sqrt X\), \(1\le L\le R^{1/2}\), and
\(1\le K/L\le16\).  Fix one positive-frequency, physically smooth block
\(B\).  Suppose its normalized product-phase sum is

\[
 T_B^+(R)=\sum_{h,k\ge1}\chi_4(h)A_B(h,k;X)e(R\sqrt{hk}),                 \tag{2.1}
\]

where \(A_B\) is real, is supported on \(h\asymp L\), \(k\asymp K\), and,
after a finite internal partition \(\Omega_B\), has the uniform continuous
gcd extensions needed below.  All actual constants, the Vaaler taper,
profile factors, floors, stars, and support-entry labels must be included in
the functions \(A_{B,\omega}\), rather than suppressed in an untyped
``admissible symbol''.

Let \(g=(h,k)\), write

\[
 h=gu,\qquad k=gv,\qquad (u,v)=1,                                   \tag{2.2}
\]

and distinguish the integer \(g\) from the dyadic shell scale \(G\).  Fix
once and for all smooth \(\psi_G\) with
\(\sum_G\psi_G(g)=1\) on the intended positive gcd range.  For every
\(B,\omega,u,v,G\), assume

\[
 \psi_G(g)A_{B,\omega}(gu,gv;X)
 =F_{B,\omega,u,v,G}(g/G)                                           \tag{2.3}
\]

on integer \(g\), where the right side has a real
\(C_c^\infty((0,\infty))\) extension with uniform seminorms.  Define

\[
\begin{aligned}
 Q_{B,\omega,G}^{\mathrm{full}}(R)
 =\sum_{\substack{u,v\ge1\;(u,v)=1\;u\ \mathrm{odd}}}\chi_4(u)
 \sum_{n\in\mathbb Z}\Big[&
 \widehat F_{B,\omega,u,v,G}
   \big(G(n-R\sqrt{uv}-\tfrac14)\big)\\
 &-\widehat F_{B,\omega,u,v,G}
   \big(G(n-R\sqrt{uv}-\tfrac34)\big)\Big].                       \tag{2.4}
\end{aligned}
\]

If \(\mathcal G_B^\circ\) consists of shells wholly inside
\(g<L^{1/2}\), then

\[
 T_{B,\mathrm{small}}^{+,\mathrm{full}}
 ={1\over2i}\sum_{\omega\in\Omega_B}
   \sum_{G\in\mathcal G_B^\circ}GQ_{B,\omega,G}^{\mathrm{full}}(R)
 +E_{B,\mathrm{gcd\text{-}bd}},                                    \tag{2.5}
\]

where \(E_{B,\mathrm{gcd\text{-}bd}}\) is the explicitly retained shell
whose smooth support meets \(g=L^{1/2}\).  It may be charged absolutely to
the accepted large-gcd budget, but it may not be erased by writing merely
\(G<L^{1/2}\).

To formulate a residual after prior owners, choose a disjoint priority, for
example

\[
 \mathsf{Sq}=\{hk\text{ is a square}\},\qquad
 \mathsf{Near}=\{hk\notin\square:\
       \operatorname {dist}(\sqrt{hk},\mathbb Z)\le R^{-1}\},         \tag{2.6}
\]

followed by the large-gcd owner on their complement.  Let
\(T_{B,\mathsf{Sq},<}^+\) and \(T_{B,\mathsf{Near},<}^+\) be the literal
signed restrictions of (2.1) to the first two sets and \(g<L^{1/2}\).
Then the exact residual identity is

\[
\begin{aligned}
 T_{B,\mathrm{res}}^+
 ={1\over2i}\sum_{\omega\in\Omega_B}
  \sum_{G\in\mathcal G_B^\circ}GQ_{B,\omega,G}^{\mathrm{full}}(R)
 +E_{B,\mathrm{gcd\text{-}bd}}
 -T_{B,\mathsf{Sq},<}^+-T_{B,\mathsf{Near},<}^+.                    \tag{2.7}
\end{aligned}
\]

The known absolute estimates make the last three terms target-safe after
their overlaps and boundary convention are proved.  Equation (2.7), not a
hidden owner mask in (2.4), is the lawful meaning of ``after the owners.''

The blockwise open theorem would be

\[
 \left|\sum_{\omega\in\Omega_B}
       \sum_{G\in\mathcal G_B^\circ}
       GQ_{B,\omega,G}^{\mathrm{full}}(R)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon,                              \tag{2.8}
\]

uniformly for every literal smooth balanced block \(B\).  Here
\(\Omega_B\) is finite and internal to \(B\); (2.8) does not sum different
\(D\)- or \(L\)-blocks before taking absolute values.  If instead one wants
to remove \(\mathsf{Sq}\) and \(\mathsf{Near}\) inside the packet, a new
Fourier formula for their exact arithmetic projector is required and (2.4)
is no longer the asserted formula.

## 3. Proof or derivation

For odd integers \(r\), and in fact for every integer after both sides are
set to zero on even integers,

\[
 \chi_4(r)={e(r/4)-e(3r/4)\over2i}.                                  \tag{3.1}
\]

On a contributing term in (2.2), \(u\) and \(g\) are odd and
\(\chi_4(gu)=\chi_4(g)\chi_4(u)\).  For fixed \(u,v,G\), Poisson with the
declared Fourier convention gives

\[
 \sum_{g\in\mathbb Z}F(g/G)e(\alpha g)
 =G\sum_{n\in\mathbb Z}\widehat F(G(n-\alpha)).                     \tag{3.2}
\]

Substituting \(\alpha=R\sqrt{uv}+1/4\) and
\(R\sqrt{uv}+3/4\) into (3.2), and then (3.1), proves

\[
 \sum_g\chi_4(g)F(g/G)e(Rg\sqrt{uv})
 ={G\over2i}\sum_n\left[
 \widehat F(G(n-R\sqrt{uv}-\tfrac14))
 -\widehat F(G(n-R\sqrt{uv}-\tfrac34))\right].                     \tag{3.3}
\]

Thus the explicit order in (112.C1), \(1/4\) minus \(3/4\), and the outer
\(1/(2i)\) are correct.  Reversing the packet order changes the sign.  The
shell scale \(G\) is not the integer gcd; writing \(h=Gu,k=Gv\) literally
would lose the Poisson variable and is therefore not an acceptable atom
definition.

There are two independent occurrences of the quarter-shift algebra in the
accepted reduction.  The already audited Vaaler coefficient is

\[
 \alpha_{h,H}=-{\Phi(|h|/(H+1))\over2\pi i h},
\]

and

\[
 \alpha_{h,H}\big(e(h/4)-e(3h/4)\big)
 =-{\Phi(|h|/(H+1))\chi_4(|h|)\mathbf1_{h\ \mathrm{odd}}
       \over\pi|h|}.                                                   \tag{3.4}
\]

This physical coefficient is real and even.  The \(1/(2i)\) in (3.3) is
introduced later when the remaining \(\chi_4(g)\) is Poisson-expanded; it
must not be deleted as though (3.4) had already consumed it.  Conversely,
the overall minus sign, \(1/\pi\), stationary unit, and taper from the
physical block must occur somewhere in the literal \(F\)-dictionary.  Since
the candidate never defines that dictionary, (3.3) certifies only the
relative packet normalization, not every global physical constant in
(112.C2).

If all \(F\)'s are real, then
\(\widehat F(-\xi)=\overline{\widehat F(\xi)}\).  Reindexing \(n\mapsto-n\)
and \(n\mapsto1-n\) in the two shifted sums gives the exact packet relation

\[
 Q_{B,\omega,G}^{\mathrm{full}}(-R)
 =-\overline{Q_{B,\omega,G}^{\mathrm{full}}(R)}.                      \tag{3.5}
\]

The minus sign in (3.5) is compulsory.  Together with
\(\overline{1/(2i)}=-1/(2i)\), it yields

\[
 T_{B,G}^{+}(-R)=\overline{T_{B,G}^{+}(R)},                           \tag{3.6}
\]

which is the required physical positive/negative-frequency conjugacy.  It
does not hold for a generic complex or Fourier-mode symbol, and one must not
sum a conjugate orientation inside the packet and then apply an outer real
part again.

For complementary divisors, let
\(c(m)=\sum_{hk=m}\chi_4(h)A(h,k)\).  When \(m\) is odd,
\(\chi_4(k)=\chi_4(m)\chi_4(h)\), so the exact symmetric/antisymmetric
decomposition is

\[
 c(m)=
 \begin{cases}
 \sum_{hk=m}\chi_4(h)A_{\mathrm{s}}(h,k),&m\equiv1\pmod4,\\
 \sum_{hk=m}\chi_4(h)A_{\mathrm{a}}(h,k),&m\equiv3\pmod4.
 \end{cases}                                                         \tag{3.7}
\]

A symmetric symbol cancels only the \(m\equiv3\pmod4\) sector and
reinforces the \(m\equiv1\pmod4\) sector.  If \(m\) is even, the
character-bearing divisor \(h\) is odd and its complement \(k\) is even;
the swapped term has \(\chi_4(k)=0\).  Hence even products remain in (2.4),
but no complementary-divisor involution is available.

The norm hierarchy is one-way.  With
\(Z_{\omega,G}=GQ_{B,\omega,G}\),

\[
 \left|\sum_{\omega,G}Z_{\omega,G}\right|
 \le\sum_{\omega,G}|Z_{\omega,G}|
 \le |\Omega_B\mathcal G_B|^{1/2}
       \left(\sum_{\omega,G}|Z_{\omega,G}|^2\right)^{1/2}.           \tag{3.8}
\]

Thus the shellwise \(\ell^1\) target and a labelwise Cauchy/Gram target are
sufficient strengthenings, not equivalent reformulations.  Cancellation
such as \(Z_1=-Z_2\) shows that neither converse holds.  More elaborate
Fejer or row-Gram lifts introduce owner cross terms and are not licensed by
a scalar owner bound.  In particular, the modulus in (2.8) must remain
outside the internal signed sum.

The capacity calculation is unchanged by canonicalization.  For
\(K\asymp L\), the raw absolute size is \(L^2\), versus target
\(L^{3/2}\).  The best accepted coefficient-blind/T2S envelope is

\[
 B(R,L)=\min(L^2,R^{1/2}L^{1/2}).                                   \tag{3.9}
\]

Its ratio to the target is

\[
 \min(L^{1/2},R^{1/2}/L),                                           \tag{3.10}
\]

maximal at \(L=R^{1/3}\), where it equals
\(R^{1/6}=X^{1/12}\).  The quarter-packet identity is norm-preserving at
this ledger level and supplies no analytic gain.

The closest primary bilinear result is Proposition 5 of
[Kowalski--Robert--Wu](https://arxiv.org/abs/math/0507001).  For
\(\alpha,\beta\in\mathbb R\setminus\{0,1\}\), \(M,N\ge1\),
\(\mathsf X>0\), and separated coefficients
\(|\varphi_m|,|\psi_n|\le1\), it bounds

\[
 \sum_{m\sim M,n\sim N}\varphi_m\psi_n
 e\!\left({\mathsf X m^\alpha n^\beta\over M^\alpha N^\beta}\right)
\]

by

\[
 \big((\mathsf XM^6N^6)^{1/8}+M^{1/2}N+MN^{3/4}
       +\mathsf X^{-1/2}MN\big)(MN)^\varepsilon.                    \tag{3.11}
\]

For \(\alpha=\beta=1/2\), \(M\asymp N\asymp L\), and
\(\mathsf X\asymp RL\), (3.11) becomes

\[
 R^{1/8}L^{13/8}+L^{3/2}+L^{7/4}+R^{-1/2}L^{3/2},                  \tag{3.12}
\]

up to \(X^\varepsilon\).  A genuinely smooth joint symbol can be separated
by an absolutely summable Fourier expansion, but coprimality, sharp owner
projectors, stars, and the literal packet kernel are not hypotheses of the
theorem.  Even on the smooth precursor, (3.12) is never better than the
accepted envelope in the relevant ranges and does not reach (2.8).

The spacing input used there is Theorem 2 of
[Robert--Sargos](https://doi.org/10.1515/CRELLE.2006.012): for fixed
\(\alpha\ne0,1\), \(M\ge2\), and \(\delta>0\), the number of
\((m_1,m_2,m_3,m_4)\in(M,2M]^4\) satisfying

\[
 |m_1^\alpha+m_2^\alpha-m_3^\alpha-m_4^\alpha|
 \le\delta M^\alpha
\]

is \(\ll_\varepsilon(M^2+\delta M^4)M^\varepsilon\).  At
\(\alpha=1/2\) it is exactly an **unsigned** square-root spacing theorem;
it cannot preserve \(\chi_4(u)\) or the signed difference of the two quarter
packets.  The accepted source audit traces (3.4) to Vaaler's
[1985 extremal-function theorem](https://www.ams.org/journals/bull/1985-12-02/S0273-0979-1985-15349-2/)
for the finite sawtooth coefficient; that source supplies normalization, not
(2.8).
The current Tao--Trudgian--Yang source is a one-variable exponent-pair
theorem; it neither accepts this coprime two-variable packet nor covers the
balanced top-scale wedge.  No audited primary theorem has the hypotheses of
(2.8).

## 4. First doubtful or unproved step

The first unproved step is **not** the \(1/(2i)\) normalization.  It is the
passage from the abstract full-small-gcd identity (3.3) to the asserted
literal residual identity (112.C2).

The candidate does not define:

- the physical block \(B\), the internal versus physical meaning of
  \(\omega\), or the exact domains of \(u,v,G\);
- the actual function \(F_{B,\omega,u,v,G}\), including the physical minus
  sign, \(1/\pi\), taper, floor-dependent height, stars, entry/exit atoms,
  and fixed support-crossing convention;
- the distinction between actual gcd \(g\) and shell scale \(G\);
- the last shell meeting \(g=L^{1/2}\); or
- the explicit corrections required when square and near-square atoms are
  assigned to prior residual owners.

The square/near-square issue is decisive.  Multiplying (2.3) by the exact
owner-complement indicator creates arithmetic jumps depending on
\(gu\,gv=g^2uv\); it cannot be declared a uniformly smooth gcd profile.
Keeping (2.4) smooth instead gives the full small-gcd packet and forces the
explicit correction identity (2.7).  Until one of those two objects is
written and checked atom by atom, the \(O(L^{3/2}X^\varepsilon)\) in
(112.C2) is an unnamed bookkeeping assertion rather than a standalone
theorem.

After this dictionary is repaired, the first genuinely analytic gap is the
blockwise signed estimate (2.8).  Existing unsigned spacing, smooth
coefficient bilinear, Mellin/Voronoi, and coefficient-blind Gram arguments
do not prove it.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `quarter_shift_sign_and_2i_normalization` | **Pass at the full-shell level.** Equations (3.1)--(3.3) give \(1/(2i)\) and \(1/4\) minus \(3/4\). The global physical constant remains conditional on the missing \(F\)-dictionary. |
| `fixed_smooth_gcd_partition` | **Conditional pass / literal fail.** A fixed smooth partition proves (2.5). The actual integer gcd \(g\), dyadic scale \(G\), and the shell crossing \(L^{1/2}\) must be distinct and explicit. |
| prior-owner compatibility | **Fail in (112.C2).** Poisson gives the full small-gcd packet. Residual square/near-square owners require (2.7) or a new nonsmooth-projector transform; neither is present. |
| `even_product_and_complementary_divisor` | **Pass.** Equation (3.7) cancels only symmetric odd \(m\equiv3\pmod4\); odd \(m\equiv1\pmod4\) reinforces, and even products have no swapped character-bearing term. |
| `positive_negative_frequency_conjugacy` | **Conditional pass with a mandatory minus sign.** For real actual profiles, \(Q(-R)=-\overline{Q(R)}\) and \((2i)^{-1}Q(-R)=\overline{(2i)^{-1}Q(R)}\). It fails for generic complex symbols. |
| `hard_endpoint_exclusion` | **Pass only by exclusion.** The unique band containing \(d=\lfloor\sqrt X\rfloor\) has a continuum jump and is not any \(B\) allowed in Section 2. Smooth bands with \(D\asymp\sqrt X\) remain allowed by their physical tag, not their exponent. |
| `floors_stars_profiles_and_support_crossings` | **Fail as a literal theorem.** They are named but absent from the formula for \(F\). A star or sharp crossing cannot be presumed to possess the uniform \(C^\infty\) extension used in Poisson. |
| `outside_absolute_G_sum_vs_shellwise_l1_and_Gram` | **Pass for the hierarchy, fail for candidate scope.** Equation (3.8) shows direct \(<\) shellwise \(\ell^1\) \(<\) Cauchy/Gram as sufficient conditions. The outside-absolute \(\omega\)-sum is lawful only inside one fixed physical block. |
| `false_unsigned_and_phase_conjugating_coefficients` | **Pass as a falsifier only.** The bounded array \(a(h,k)=\chi_4(h)e(-R\sqrt{hk})\) makes the precursor sum have \(\asymp L^2\) mass. It disproves any coefficient-uniform target based only on support and \(\ell^2\) size, but violates the fixed actual-symbol class and is not a lower bound for the actual packet. Unsigned quarter-resonance counts likewise cannot prove the signed difference. |
| `real_X_and_balanced_comparability` | **Conditional pass.** All algebra is uniform for real \(X>0\), without a square-\(X\) assumption, and for \(1\le K/L\le16\). The target \((LK)^{3/4}\asymp L^{3/2}\) is comparable, not an equality when \(K\ne L\). |
| `capacity_and_downstream_scope` | **Pass as a no-go ledger.** Equations (3.9)--(3.10) give the worst \(X^{1/12}\) deficit. A proof of (2.8) for all balanced smooth blocks would close only that parent of the physical M2 assembly; the hard and unbalanced parents would remain open. |
| `primary_source_hypothesis_map` | **Pass, with no import.** KRW Proposition 5 and Robert--Sargos Theorem 2 have the exact hypotheses recorded above and miss or erase the signed packet. Vaaler supplies coefficient normalization only; TTY is one-dimensional and out of range. |

No computation was used.  The phase-conjugating example is a formal
proves-too-much control, not numerical evidence.

## 6. Dependencies and exact artifacts used

The complete selected repository context was:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/briefs/balanced_packet_hostile_source_audit.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/candidates/conductor_balanced_packet_interface.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/hostile_endpoint_scope_review.md`;
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/endpoint_dual_signed_attack.md`;
- `rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/reports/m2_assembly_hostile_hygiene_audit.md`.

The primary sources and source records used for the hypothesis map were:

- J. D. Vaaler, *Some extremal functions in Fourier analysis*, Bull. AMS
  12 (1985), 183--216, DOI
  [10.1090/S0273-0979-1985-15349-2](https://doi.org/10.1090/S0273-0979-1985-15349-2).
  The Round-112 audit relies on the already source-audited graph for its
  exact coefficient rather than claiming a new independent primary-text
  rederivation;
- E. Kowalski, O. Robert, J. Wu, *Small gaps in coefficients of
  \(L\)-functions and B-free numbers in small intervals*,
  [arXiv:math/0507001](https://arxiv.org/abs/math/0507001), Proposition 5;
- O. Robert, P. Sargos, *Three-dimensional exponential sums with
  monomials*, J. reine angew. Math. 591 (2006), 1--20,
  [DOI 10.1515/CRELLE.2006.012](https://doi.org/10.1515/CRELLE.2006.012),
  Theorem 2;
- T. Tao, T. Trudgian, A. Yang, *New exponent pairs, zero density
  estimates, and zero additive energy estimates: a systematic approach*,
  [arXiv:2501.16779](https://arxiv.org/abs/2501.16779), used only for the
  one-variable/out-of-scope check recorded in the accepted source map.

Proposition 5 of Kowalski--Robert--Wu and Theorem 2 of Robert--Sargos were
checked in their primary texts with the hypotheses and all displayed terms
recorded in Section 3.  No new theorem is imported from Vaaler or
Tao--Trudgian--Yang in this report.

No unlisted repository artifact, sibling Round-112 report, numerical file,
or external theorem was used.

## 7. Recommended state effect

- **Retain** `M9-M2-smooth-small-gcd-quarter-packet` only as the abstract
  uniformly smooth **full-small-gcd** reduction with the certified
  \(1/(2i)\), \(1/4-3/4\), and character normalization.  Do not strengthen
  it silently to a literal owner-removed residual theorem.
- **Revise** the Round-112 candidate before promotion.  Replace the
  undefined \(\omega\) by a fixed physical block \(B\) plus an explicitly
  finite internal set \(\Omega_B\); distinguish \(g\) from \(G\); write the
  actual \(F\); name the terminal gcd shell; and use the explicit owner
  correction identity (2.7), or else call the packet full small-gcd and
  leave its square/near-square atoms inside.
- **Revise** `M9-M2-smooth-balanced-quarter-packet-estimate` so its modulus
  is outside the internal signed sum for each literal \((D,L,+)\) block
  separately.  Do not permit cancellation across distinct \(D\)- or
  \(L\)-blocks; the accepted physical assembly sums their already bounded
  magnitudes with logarithmic cost.
- **Record** the exact conjugacy seam
  \(Q(-R)=-\overline{Q(R)}\), the one-way norm hierarchy (3.8), the even
  product/complementary-divisor obstruction, and the \(X^{1/12}\) worst
  capacity deficit as guardrails.
- **Reject** unsigned resonance counts, coefficient-blind or
  phase-conjugating coefficient imports, hard-endpoint insertion, and any
  inference from KRW, Robert--Sargos, Vaaler, TTY, or a Voronoi
  representation to the open signed estimate.
- **No analytic promotion:** keep the balanced estimate, hard child,
  unbalanced child, M9-M2, endpoint uniformity, M9, and the Gauss-circle
  quarter target at their current statuses.  The recommended graph effect
  is `revise` for the canonical interface and `no change` for every
  downstream theorem.
