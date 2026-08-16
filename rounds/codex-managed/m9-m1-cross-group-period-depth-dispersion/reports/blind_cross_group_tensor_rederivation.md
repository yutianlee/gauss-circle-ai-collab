# 1. Result.

**Verdict: rigorous no-go from the supplied statement.**  The packet does determine an exact CRT tensor factorization and an exact full-prime-power Fourier/period-depth decomposition of the completed fourfold symbol.  Those identities separate lower-conductor returns from the primitive local Fourier layer without losing the (2)-part, bad primes, or modulus-multiple shifts.  They do **not** imply

\[
 \mathcal G_{\rm cross}(D)
 \ll_\varepsilon X^\varepsilon {D\over B}J^{14/5}.
\]

There are two independent obstructions.

1. The packet gives no equality expressing the cross-group Fourier correlations in (88.8), with their outer weights and normalizations, as a sum of the completed symbols (88.10).  Consequently the tensor layers cannot be assigned to an exact subaggregate of \(\mathcal G_{\rm cross}\), nor can their coefficients be estimated.
2. Even at the local-symbol level there is no uniform aperiodic estimate to apply.  The actual phase has genuine lower-conductor loci.  For example, if \(A=B_2=V=0\pmod {p^\nu}\), then \(\Phi=0\) and the local completed sum is a Ramanujan sum of size as large as \(p^{2\nu}\) after the prescribed leading factor \(p^\nu\).  More generally, bad-prime and perfect-power congruences can force the same return.  The packet contains neither the cross-group exclusion of these loci nor a bound for the remaining primitive trace.

Thus (88.9) is not proved or disproved as a statement about the underlying M9--M1 problem; it is not derivable from the supplied data.  The only unconditional target-safe local class obtained here is the identically zero class (for example, an empty \(2\)-adic unit domain), but the packet does not identify its preimage in (88.8), so it does not certify a nonempty target-safe component of the actual cross-group aggregate.  No strictly smaller exact survivor of (88.8) can therefore be asserted.

# 2. Exact statement and hypotheses.

Assume exactly the scales, three \((g,M,K)\) classes, normalized rows, deep projection, active-set partition, same-group deletion, and strict cross-group definition stated in the derivation packet.  In particular, no coprimality condition on \(K\), no ranges or congruence restrictions on \((A,B_2,V)\), no formula connecting those shifts to \((S,\alpha),(S',\alpha')\), and no external trace theorem are added.

Write

\[
 H_{b,i}(\theta)=\sum_d h_{b,i}(d)e(d\theta),
 \qquad i=(S,\alpha).
\]

Then the strict cross term has the exact signed coefficient form

\[
 \mathcal G_{\rm cross}(D)
 =\sum_{b\asymp B}\sum_{0<|u|<D}(D-|u|)
   \sum_{i\ne j}\sum_d
   h_{b,i}(d)\overline{h_{b,j}(d+u)}.                 \tag{2.1}
\]

Both signs of \(u\) occur.  The omitted term is the single integer shift \(u=0\), not all shifts congruent to zero modulo \(M\).

For a full factor \(q=p^\nu\Vert M\), put \(m_q=M/q\), let \(c_q\) be the inverse of \(m_q\pmod q\), and define

\[
 \begin{split}
 \mathscr U_q&=\{x\bmod q:x,x-A,x-V,x-V-B_2\in(\mathbb Z/q\mathbb Z)^\times\},\\
 a_q(x)&=1_{\mathscr U_q}(x)
 e_q\!\left(c_qK\Phi_{A,B_2,V}(x)\right),\\
 \mathfrak T_q(w)&=q\sum_{x\bmod q}a_q(x)e_q(wx).
 \end{split}                                                   \tag{2.2}
\]

With \(w_q=c_qu\pmod q\), the exact tensor identity is

\[
 \mathfrak T_M(u,V;A,B_2)
 =\prod_{q\Vert M}\mathfrak T_q(w_q).                         \tag{2.3}
\]

For \(0\le j\le\nu\), define the full-prime-power period projection

\[
 (E_{q,j}a)(x)
 ={1\over p^j}\sum_{t\bmod p^j}
 a\!\left(x+t p^{\nu-j}\right),                              \tag{2.4}
\]

and set

\[
 \Delta_{q,j}=E_{q,j}-E_{q,j+1}\quad(0\le j<\nu),
 \qquad \Delta_{q,\nu}=E_{q,\nu}.                            \tag{2.5}
\]

These operators give the exact depth decomposition

\[
 a_q=\sum_{j=0}^{\nu}\Delta_{q,j}a_q,
 \qquad
 \widehat{\Delta_{q,j}a_q}(w)
 =1_{v_p(w)=j}\widehat a_q(w)                                 \tag{2.6}
\]

for \(j<\nu\), while \(\Delta_{q,\nu}\) is supported at \(w=0\pmod q\).  Here \(v_p(0)\) is truncated to \(\nu\).  Thus \(\Delta_{q,0}=I-E_{q,1}\) is the exact local aperiodic trace operator, and the layers \(j>0\) are the canonical lower-conductor-return layers.  Formula (2.6) is a support identity, not a size estimate.

If \(a_q\) is genuinely periodic modulo \(p^{\nu-j}\), so that it is the lift of a function \(\widetilde a\) modulo \(p^{\nu-j}\), then

\[
 \mathfrak T_q(w)=0\quad(p^j\nmid w),
 \qquad
 \mathfrak T_q(p^jw')=p^{2j}\mathfrak T_{p^{\nu-j}}(w').      \tag{2.7}
\]

The factor \(p^{2j}\) in (2.7), including the leading factor in the definition of \(\mathfrak T\), is essential.

# 3. Proof or derivation.

The normalized row has Fourier coefficient

\[
 \widehat{\mathcal R_{b,x}}(n)=M^{-1}I_b(n)e_M(nx).
\]

Consequently the coefficient of (88.2) at difference \(d\) is

\[
 \widehat F_{b,(x,y)}(d)
 ={1\over M^2}e_M\!\left(K(\bar x-\bar y)\right)
 \sum_m I_b(m+d)\overline{I_b(m)}
 e_M\!\left((m+d)x-my\right).                                \tag{3.1}
\]

This verifies that the external \(M^{-2}\) occurs once, before any group sum or completion.  It must not be inserted again.  Also, (88.1) gives

\[
 |F_{b,(x,y)}(\theta)|
 \ll_\varepsilon X^\varepsilon T^2Q^{-5/12},                 \tag{3.2}
\]

so a product of two physical pair rows carries \(T^4Q^{-5/6}\).  Expanding

\[
 |D_D(\theta)|^2
 =\sum_{|u|<D}(D-|u|)e(u\theta)
\]

and integrating term by term proves (2.1).  This also proves that \(U=D\), all Fejer weights, and both orientations are retained exactly.

For the tensor identity, CRT writes every allowed \(x\bmod M\) as its tuple \((x_q)_{q\Vert M}\).  The four unit conditions factor over the full prime powers.  Moreover

\[
 e_M\!\left(ux+K\Phi(x)\right)
 =\prod_{q\Vert M}
 e_q\!\left(c_qux_q+c_qK\Phi(x_q)\right).
\]

The unrestricted CRT sum therefore factors.  Since \(\prod_{q\Vert M}q=M\), the product of the local leading factors is exactly the one global leading factor in (88.10), proving (2.3).  This is why splitting into prime powers creates no additional power of \(M\).

To prove (2.6), translate the summation variable in the Fourier transform of (2.4):

\[
 \widehat{E_{q,j}a}(w)
 ={1\over p^j}\sum_{t\bmod p^j}e_{p^j}(-wt)\widehat a(w)
 =1_{p^j\mid w}\widehat a(w).                                \tag{3.3}
\]

Taking adjacent differences gives the exact valuation support in (2.6).  If \(a_q(x)=\widetilde a(x\bmod p^{\nu-j})\), write
\(x=y+t p^{\nu-j}\).  The sum over \(t\bmod p^j\) vanishes unless \(p^j\mid w\); in the supported case it equals \(p^j\).  Comparing the leading factors \(p^\nu\) and \(p^{\nu-j}\) gives the second factor \(p^j\), hence (2.7).

The exact test for a claimed phase period must use the denominator as well as the quadratic numerator.  Put

\[
 N(x)=(B_2-A)x^2+2AVx-AV(V+B_2),
 \quad
 P(x)=x(x-A)(x-V)(x-V-B_2).                                  \tag{3.4}
\]

On \(\mathscr U_q\), \(\Phi(x)=N(x)P(x)^{-1}\pmod q\).  For \(0<j<\nu\), translation by \(s=p^{\nu-j}\) preserves every unit indicator because \(p\mid s\).  Hence the full symbol, including its domain, has period \(s\) if and only if

\[
 p^\nu\mid c_qK
 \{N(x+s)P(x)-N(x)P(x+s)\}                                  \tag{3.5}
\]

for every \(x\in\mathscr U_q\).  The denominators in (3.5) are units.  Criterion (3.5), rather than coefficient content of (88.11) alone, is the exact full-prime-power period test.  It remains valid for bad primes and for \(p=2\).  For \(j=\nu\), translation by one need not preserve the unit domain, so constancy of the entire function \(a_q\), not merely the phase, must be checked.

The full \(2\)-part already shows why the domain cannot be suppressed.  If \(q=2^\nu\), then \(\mathscr U_q\ne\varnothing\) forces

\[
 A\equiv B_2\equiv V\equiv0\pmod2.                          \tag{3.6}
\]

If any of these residues is odd, the local symbol and hence the whole tensor term vanish identically.  If all are even, the indicator depends at least on parity and may itself be a lower-conductor function even when the rational phase is constant.

There are genuine degeneracies in the actual fourfold symbol.  If \(A=B_2=V=0\pmod q\), then \(\Phi=0\) and \(a_q=1_{(\mathbb Z/q\mathbb Z)^\times}\).  Therefore

\[
 \mathfrak T_q(w)=q\,c_q(w),                                 \tag{3.7}
\]

where, for \(q=p^\nu\),

\[
 c_{p^\nu}(w)=
 \begin{cases}
  \varphi(p^\nu),&p^\nu\mid w,\\
  -p^{\nu-1},&p^{\nu-1}\mid w,\ p^\nu\nmid w,\\
  0,&p^{\nu-1}\nmid w.
 \end{cases}                                                  \tag{3.8}
\]

Thus a perfect-power return at exact depth \(\nu-1\) can have size
\(p^{2\nu-1}\), and the local-zero residue has size \(p^\nu\varphi(p^\nu)\).  The same phenomenon occurs whenever

\[
 p^\nu\mid K(B_2-A),\qquad
 p^\nu\mid 2KAV,\qquad
 p^\nu\mid KAV(V+B_2),                                      \tag{3.9}
\]

because then the reciprocal phase is trivial on its unit domain.  Conditions (3.9) explicitly include nonunit-\(K\), bad-prime, and \(2\)-adic degenerations.  A local residue \(w=0\pmod q\) in (3.7) is not necessarily the deleted global shift: every nonzero integer \(u=\ell M\), \(|u|<D\), has zero residue at every local factor and remains in (2.1).

Period support alone supplies no target saving.  For a period divisor \(p^j\), the Fejer mass on supported nonzero shifts is

\[
 2\sum_{1\le k<(D/p^j)}(D-kp^j)\asymp {D^2\over p^j}
\]

when \(p^j\ll D\), whereas the exact descent (2.7) carries \(p^{2j}\).  Whether the lower-conductor trace, the outer normalization, and cross-label summation offset this loss cannot be decided without their missing weights.

Nor does Fourier completion create a second saving.  Direct orthogonality gives the self-return and Plancherel identities

\[
 \sum_{w\bmod q}\mathfrak T_q(w)e_q(-wx)=q^2a_q(x),
 \qquad
 \sum_{w\bmod q}|\mathfrak T_q(w)|^2
 =q^3|\mathscr U_q|.                                         \tag{3.10}
\]

The same formulas hold with \(a_q\) replaced by any depth layer.  Hence the operator \(\Delta_{q,0}\) separates the aperiodic spectrum but gives no pointwise or signed cross-group cancellation by itself.

Finally, (88.6) cannot replace the missing cross estimate.  As a control, suppose two allowed deep frequencies \(d_0,d_0+r\) satisfy \(0<r<D\), and let \(L\) distinct group labels have

\[
 h_i(d_0)=h_i(d_0+r)=a,qquad h_i(d)=0\ \text{otherwise}.
\]

Then their same-group Fejer mass is

\[
 L(4D-2r)|a|^2,
\]

but their strict, signed cross-group contribution is positive and equals

\[
 2L(L-1)(D-r)|a|^2.                                          \tag{3.11}
\]

The ratio grows like \(L\).  The amplitude can be scaled to meet any homogeneous row, projection, or same-group upper bound.  This is a Hilbert-space control showing that (88.1), (88.4), and (88.6) do not imply cross-group almost orthogonality.  It is not asserted to be an arithmetic realization of the M9--M1 rows; precisely the missing arithmetic correlation formula and trace estimate would be needed to rule it out.

# 4. First doubtful or unproved step.

The first unproved step is the seam from (2.1) to the proposed local analysis: the packet does not give an exact expansion

\[
 \sum_{i\ne j}\sum_d h_{b,i}(d)\overline{h_{b,j}(d+u)}
 =\sum_{A,B_2,V}W_b(A,B_2,V;u)\,
   \mathfrak T_M(u,V;A,B_2)                                  \tag{4.1}
\]

(or an equivalent formula), including the definition and norm of \(W_b\), the correspondence between distinct group labels and \((A,B_2,V)\), the external \(M^{-2}\) factors from each physical pair row, and all already-owned deletions.  Without (4.1), it is impossible to prove that the degenerate loci (3.6)--(3.9) are absent, same-group-owned, or sparse, and impossible to turn the exact depth layers into an exact component of (88.8).

Even if (4.1) were granted, a second unproved input would remain: a uniform signed estimate for the primitive layers \(\Delta_{q,0}a_q\), together with a lower-conductor estimate that compensates the factor \(p^{2j}\), valid at arbitrary prime powers, bad primes, and the full \(2\)-part.  No theorem with literal hypotheses of that strength is present in the packet.

# 5. Required control tests and outcomes.

| Control | Outcome |
|---|---|
| External normalization | **Pass.** Formula (3.1) retains exactly one \(M^{-2}\) in each physical pair coefficient; no extra copy was introduced. |
| Full-factor ownership | **Pass.** Only \(i\ne j\) is considered.  No same-group local-zero, paired branch, stride-\(M\) return, or other Round-87 package is reassigned.  A degenerate local factor inside a cross term remains cross-group unless an exact seam proves otherwise. |
| Global diagonal one-count | **Pass.** Equation (2.1) deletes only the integer shift \(u=0\).  Nonzero \(u\equiv0\pmod M\) is retained. |
| \(U=D\) and Fejer weights | **Pass.** The exact weights \(D-|u|\), range \(0<|u|<D\), and both signs appear in (2.1). |
| Physical \(Q^{-5/12}\) | **Pass.** One pair row has scale \(T^2Q^{-5/12}\), and a cross product has \(T^4Q^{-5/6}\); see (3.2). |
| Full prime-power period depth | **Pass algebraically / fail analytically.** Equations (2.4)--(2.7) retain every depth \(0,\ldots,\nu\).  No bound for the layers is supplied. |
| Bad primes and full \(2\)-part | **Pass structurally / unresolved for size.** They remain in (3.5), (3.6), and (3.9).  No squarefree reduction or odd-modulus substitution is made. |
| Actual fourfold symbol | **Pass.** The period test uses \(N(x+s)P(x)-N(x)P(x+s)\), not the numerator alone.  The exact zero-phase loci (3.7)--(3.9) were tested. |
| Aperiodic trace operator | **Pass as an identity / fail as an estimate.** \(\Delta_{q,0}=I-E_{q,1}\) isolates \(p\nmid u\), but (3.10) shows that this operation alone gives no saving. |
| Negative and reflected orientations | **Pass.** All integers are reduced only at the local factor, and both \(u\) signs are retained.  No orientation is discarded by taking an early absolute value. |
| Modulus-multiple differences | **Pass.** Nonzero multiples of \(M\) remain and can sample the large local-zero transform in (3.8). |
| Ramanujan terms | **Pass.** They are retained explicitly in (3.7)--(3.8), rather than identified with the single global diagonal. |
| Deep support and owned errors | **Pass as scope.** The literal zero, \(|d|\le D_1\), the outer collar, and separately owned transition/error families are not reopened.  No estimate for them is claimed. |
| Support endpoints | **Pass as scope / unavailable for a new estimate.** The strict deep interval is preserved.  The packet gives no coefficient formula at its endpoints from which a uniform cross bound could be proved. |
| Perfect powers | **Pass.** The depth \(\nu-1\) Ramanujan return in (3.8) is an explicit perfect-power control and prevents a prime-modulus shortcut. |
| Transform self-return | **Pass.** Both inversion and Plancherel are checked in (3.10); completion is not counted as an independent cancellation. |
| Literal source hypotheses | **Fail/unavailable.** No source result or theorem hypotheses are included, and source consultation is excluded, so no Weil, Deligne, or prime-power stationary-phase bound is invoked. |
| Downstream scope | **Pass.** No conclusion is made for \(C>J^{3/4}\), transitions, axes, cone edges, other sectors, M9--M2, full M9--M1, endpoint uniformity, R5-Full, or the global exponent. |

# 6. Dependencies and exact artifacts used.

The only mathematical context used was:

- `rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/derivation_packet.md`.

The task constraints and output contract were read from:

- `rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/briefs/blind_cross_group_tensor_rederivation.md`.

No proof-state file, graph, strategy, earlier report or review, sibling Round-88 artifact, source card, directory listing, web source, or numerical experiment was used.  All computations above are direct finite Fourier and CRT identities.

# 7. Recommended state effect.

**No change** to the accepted proof state.  Retain (2.3)--(2.7), (3.5), and (3.10) only as candidate algebraic evidence for tensorization, exact period-depth routing, and transform self-return.  Reject promotion of (88.9) and reject any claimed nonempty target-safe cross subaggregate from this packet alone.  The sharp survivor is still the whole signed quantity (2.1), because the first necessary cross-correlation-to-symbol seam (4.1) is absent.

## Supplemental post-isolation audit (not blind evidence)

This supplement was performed after statement-only isolation was lifted for the single additional candidate
`rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/candidates/conductor_shallow_quotient_coarse_group_bound.md`.
It does not alter the provenance of the blind analysis above.

**Supplemental verdict.**  The candidate's direct physical-pair coarsening argument is valid, including

\[
 \mathcal P_m(D)
 \ll_\varepsilon X^\varepsilon DB^3R^2T^4Q^{-5/6},
 \qquad R=M/m,                                                \tag{S.1}
\]

the divisor-shell ownership, the centered \(u\ne0\) extraction, and the threshold

\[
 R_{\rm crit}(B)=J^{11/30}B^{-2}.                             \tag{S.2}
\]

This supplies the seam missing from the blind packet at the level actually needed: it works directly with the normalized \(F_{b,P}\) and their fine/coarse group sums, so it does not need an expansion through \(\mathfrak T_M\).  Consequently the earlier blind recommendation against a target-safe component is superseded, for this post-isolation evidence only, by promotion of the exact shells
\(1<R_*\le R_{\rm crit}(B)\) as a candidate target-safe deletion.  Two qualifications are mandatory: the coarse active-set convention must include the empty active set, and the permitted artifacts do not identify a particular completed trace with a particular pair of physical labels.  The claimed \(R_*=3\) shell inclusion is exact; the additional attribution of the value \(M^2/3\) to that physical-label family is only conditional on the missing trace-to-label correspondence.

**Coarse lift count.**  Write

\[
 M=\prod_p p^{\nu_p},\qquad
 m=\prod_p p^{a_p},\quad 0\le a_p\le\nu_p,
 \qquad R=\prod_p p^{\nu_p-a_p}.
\]

A unit residue modulo \(p^{a_p}\) has exactly \(p^{\nu_p-a_p}\) unit lifts if \(a_p>0\).  If \(a_p=0\), the omitted local coordinate has \(\varphi(p^{\nu_p})\le p^{\nu_p}\) choices.  Hence each coarse unit has at most \(R\) physical unit lifts and each coarse ordered pair has at most \(R^2\) physical lifts.  This remains true when \((m,R)>1\), at arbitrary prime-power depth, and at \(p=2\).

For an active set \(S\) of the full prime-power factors of \(m\), let \(m_S\) be their product and \(r_S=m/m_S\).  There are at most

\[
 \prod_{q\in S}\varphi(q)(\varphi(q)-1)\le m_S^2
\]

active labels.  A fixed label has at most
\(\prod_{q\notin S}\varphi(q)\le r_S\) inactive common coarse residues and therefore at most \(r_SR^2\) physical pairs.  Linearity of \(\Pi_{b,D}\) and (88.1), (88.4) give

\[
 \begin{aligned}
 \sum_{\gamma:S(\gamma)=S}|K_{b,m,\gamma}(\theta)|^2
 &\ll_\varepsilon
 X^\varepsilon m_S^2(r_SR^2)^2T^4Q^{-5/6}\\
 &=X^\varepsilon M^2R^2T^4Q^{-5/6}.                          \tag{S.3}
 \end{aligned}
\]

The \(2^{\omega(m)}\) active sets cost \(X^\varepsilon\), and summing \(O(B)\) values of \(b\), with \(M\asymp B\), proves (S.1).  The empty set \(S=\varnothing\) must be included: a physical pair distinct modulo \(M\) may become diagonal modulo \(m\), and for \(m=1\) it is the only coarse group.  With that convention the count covers all physical pairs.  It is independent of \(K\), so bad primes and nonunit \(K\) cause no exception.

The normalization is also exact.  Put \(f_P=\Pi_{b,D}F_{b,P}\).  At the fine modulus,

\[
 K_{b,M,\gamma}=H_{b,\gamma};
\]

at a coarse modulus,

\[
 K_{b,m,\gamma}
 =\sum_{i:\,\Gamma_m(i)=\gamma}H_{b,i}
 =\sum_{P:\,\Gamma_m(P)=\gamma}f_P.                          \tag{S.4}
\]

Thus the candidate uses the \(M^{-2}\) already present in each \(F_{b,P}\), and introduces none.  Coarsening fine labels is exact even when a fine active coordinate becomes coarse diagonal; its common coarse residue is summed inside (S.4), not retained as an active label.

**Divisor-lattice ownership.**  For a local factor \(p^\nu\Vert M\), equality of the two coarse labels at modulus \(p^a\) is monotone as \(a\) decreases.  If the labels are identical and active at \(p^a\), then at \(p^{a-1}\) they remain identical and active or both become diagonal.  If both are diagonal at \(p^a\), they remain diagonal at every lower power.  There is therefore a unique least exponent \(r_p\in\{0,\ldots,\nu\}\) such that the labels agree after quotienting by \(p^{r_p}\).  With

\[
 R_*(P,P')=\prod_{p\mid M}p^{r_p},                            \tag{S.5}
\]

one has, for every divisor \(R\mid M\),

\[
 \Gamma_{M/R}(P)=\Gamma_{M/R}(P')
 \quad\Longleftrightarrow\quad R_*(P,P')\mid R.              \tag{S.6}
\]

Expanding (S.4) pointwise gives the cumulative relation

\[
 A_R(\theta):=
 \sum_\gamma|K_{b,M/R,\gamma}(\theta)|^2
 =\sum_{P,P':\,R_*(P,P')\mid R}f_P(\theta)\overline{f_{P'}(\theta)}.
                                                                    \tag{S.7}
\]

Thus the exact shell is

\[
 C_R(\theta)=\sum_{d\mid R}\mu(R/d)A_d(\theta).              \tag{S.8}
\]

Fine same-group correlations have \(R_*=1\), while fine cross-group correlations have \(R_*>1\).  Formula (S.8) may use the \(R=1\) same-group package as a Möbius basis term, but it does not reassign any \(R_*=1\) correlation to a cross shell.  Summing (S.8) over \(1<R\le R_0\) has total divisor cost at most \(\tau(M)^2=X^\varepsilon\), and every cumulative package that occurs has quotient \(d\le R_0\).  Applying (S.1) with \(R=d\) therefore yields the claimed \(R_0^2\) loss.

**Centered Fejer extraction.**  The centered kernel

\[
 \mathcal K_D^\circ=|D_D|^2-D
 =\sum_{0<|u|<D}(D-|u|)e(u\theta)                              \tag{S.9}
\]

removes exactly the one integer shift \(u=0\), commutes with the pointwise identities (S.7)--(S.8), and retains both signs and every nonzero modulus-multiple shift.  Since

\[
 \|\mathcal K_D^\circ\|_1
 \le \||D_D|^2\|_1+D=2D,                                    \tag{S.10}
\]

the pointwise estimate (S.3) gives the same bound as (S.1), up to an absolute factor, even though the centered package is signed.  Hence

\[
 \left|\mathcal G_{\rm cross}^{\,1<R_*\le R_0}(D)\right|
 \ll_\varepsilon
 X^\varepsilon DB^3R_0^2T^4Q^{-5/6}.                         \tag{S.11}
\]

No Ramanujan term, reflected orientation, support endpoint, or fourfold-symbol degeneration is deleted in this operation; they stay inside the unexpanded physical \(F\)-correlations.

**Threshold check and nonemptiness.**  Dividing (S.11) by the target gives exactly

\[
 R_0^2B^4T^4Q^{-5/6}J^{-14/5}
 =R_0^2B^4J^{-11/15}.                                        \tag{S.12}
\]

Thus (S.11) is target-safe when

\[
 R_0\le J^{11/30}B^{-2}=R_{\rm crit}(B),                     \tag{S.13}
\]

up to harmless fixed \(M\asymp B\) constants and divisor factors absorbed by \(X^\varepsilon\).  From
\(J^{11/90}<B\le J^{3/20}\), the threshold ranges from \(J^{1/15}\) at the upper endpoint to at most \(J^{11/90}\asymp B\) near the lower endpoint.  It tends to infinity uniformly, so integer shells such as \(R_*=2\) are admitted for large \(J\).

Nonemptiness can be checked within the stated classes rather than inferred from the real-valued threshold.  The class \(M=4b\) has a full \(2\)-part \(2^\nu\), \(\nu\ge2\).  At \(\nu=2\), the distinct active labels \((1,3)\) and \((3,1)\pmod4\) both become coarse diagonal modulo \(2\); at \(\nu\ge3\), the distinct active labels \((1,3)\) and \((1+2^{\nu-1},3)\pmod {2^\nu}\) coincide actively modulo \(2^{\nu-1}\).  Holding every odd local label fixed gives \(R_*=2\).  Thus the deletion is genuinely nonempty in the physical group system for sufficiently large \(J\).

For \(M=3^\nu\), two distinct full labels that have the same coarse label modulo \(M/3\) satisfy \(R_*=3\) by (S.6), so every physical correlation between them is genuinely included in (S.11) once \(3\le R_{\rm crit}(B)\).  Explicit examples are \((1,2)\) and \((2,1)\pmod3\) for \(\nu=1\), and \((1,2)\) and \((1+3^{\nu-1},2)\pmod {3^\nu}\) for \(\nu\ge2\).  The value \(M^2/3\) is consistent with the exact depth-\(\nu-1\) Ramanujan return (3.7)--(3.8).  However, the packet and candidate do not provide the map from these physical labels to \((A,B_2,V)\), so they do not independently prove that this particular trace value belongs to these particular examples.  This does not weaken their shell inclusion: the coarse bound covers those correlations for every value of their completed trace.

**Supplemental state recommendation.**  Promote (S.11)--(S.13) as candidate evidence for the exact target-safe shallow coarse-quotient shells, subject to an ownership review confirming the empty coarse group convention and that using the fine \(R=1\) package as a Möbius basis term is permitted.  Retain as the exact survivor the cross shells
\(R_*>R_{\rm crit}(B)\), accidental unit-mask periods not induced by coarse group coincidence, and genuinely aperiodic local traces.  This supplemental recommendation makes no downstream claim beyond the frozen Round-88 scope.
