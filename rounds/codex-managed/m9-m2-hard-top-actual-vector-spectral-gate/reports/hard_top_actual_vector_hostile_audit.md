# Round 126 hostile seam audit: the parity high-pass selects the target mode

Campaign: `m9-m2-hard-top-actual-vector-spectral-gate`
Task: `hard_top_actual_vector_hostile_audit`
Role: hostile seam reviewer
Starting graph SHA-256: `85cf63f0087c6c6adf911bd0f7fdf5d3985a6a49b4e0d6158a7dc28470da10c9`
Evidence status: candidate report only; no shared proof state is changed.

## 1. Result: sharp parity/support no-go and a complete-offset inverse localization

The literal Round-75 vector and all of its energy identities pass. The proposed parity spectral gain does not. The alternating high-pass identity

$$
 2\sum_t(-1)^t v_t=\sum_t(-1)^t(v_t-v_{t+1})
$$

is a normalization of the value of the height Fourier transform at frequency \(\pi\). Its multiplier has modulus \(2\) at that same frequency. It therefore selects and amplifies the target parity mode; it does not remove it. In Gram language, if \(V e_t=v_t\), \(G=V^*V\), \(N=\#\mathscr H_L\), and \(u_\chi=N^{-1/2}(\chi_4(h))_h\), then

$$
 \mathcal E_L^{\rm top}=N\langle Gu_\chi,u_\chi\rangle,
 \qquad
 \mathcal D_L=\operatorname {tr}G.
$$

Thus a theorem genuinely relative to the diagonal would have to prove the actual-symbol anti-concentration

$$
\langle Gu_\chi,u_\chi\rangle
 \ll_\varepsilon {X^\varepsilon\over N}\operatorname {tr}G.       \tag{126.H1}
$$

The stated absolute target asks instead for
\(\langle Gu_\chi,u_\chi\rangle\ll L^2X^\varepsilon/N\).
These coincide on any populated block with \(\mathcal D_L\asymp L^2\);
only the upper bound \(\mathcal D_L\ll L^2\) is needed elsewhere in this
report.

Neither positivity, Bessel's inequality, the parity twist, nor the high-pass identity gives the factor \(N^{-1}\). In fact the optimal coefficient-uniform constant under the literal hard affine supports is \(N\asymp L\): a bounded aligned family on the common hard-cone interior has diagonal capacity \(\asymp L^2\) and parity energy \(\asymp L^3\). This is an exact no-go for every support-only, parity-only, coefficient-blind Bessel/operator claim. It is **not** a lower bound for the actual \(a_{\rm end}(h,m)e(J\sqrt{hm})\) vectors.

There is, however, a rigorous inverse localization. If the actual energy has positive excess \(V=\mathcal E_L^{\rm top}-\mathcal D_L>0\), then one dyadic physical offset family, and equivalently one dyadic primitive-\(q\) family, has positive real part at least \(V/O(\log L)\). The selected family keeps all lifts, coprimality, moving ceilings, reciprocal intervals, collars, entries, exits, floors, stars, metric centres, and one-count slabs jointly. This localization is a signed pigeonhole identity, not a contraction and not a bound. There is no licensed shellwise version of the Round-110 completed-to-physical correction.

Accordingly, no diagonal-scale actual-vector theorem, no strict new polynomial subrange, and no actual-vector lower bound is proved. The maximal safe outcome is the sharp parity/support obstruction plus the complete-offset inverse localization. The hard-TOP lane should be parked at the exact vector, equivalently the one-sided real completed scalar; if a smaller survivor is desired after a fixed-power violation, it is one complete dyadic primitive-offset family with no slabwise separation.

## 2. Exact statement and hypotheses

Let \(X\ge2\) be real, \(J=\sqrt X\), and let \(L\) be one polynomial intermediate hard-TOP height block. Bounded and terminal blocks and all previously accepted target-safe owners are excluded from the new claim. Let \(\mathscr H_L\) be the exact finite odd height support and put

$$
 v_h(m)=1_{\lceil h/4\rceil\le m\le h}
 a_{\rm end}(h,m)e(J\sqrt{hm}),
 \qquad
 R_m=\sum_{\substack{h\in\mathscr H_L\\m\le h\le4m}}
 \chi_4(h)a_{\rm end}(h,m)e(J\sqrt{hm}).                 \tag{126.H2}
$$

All vectors are zero-extended in both the odd-height index and the \(m\)-index. Then

$$
 \mathcal E_L^{\rm top}=\sum_m|R_m|^2
 =\left\|\sum_{h\in\mathscr H_L}\chi_4(h)v_h\right\|_2^2,
 \qquad
 \mathcal D_L=\sum_h\|v_h\|_2^2\ll L^2.                \tag{126.H3}
$$

Write \(h=h_0+2t\), so \(\chi_4(h)=\sigma_0(-1)^t\). The following is the maximal safe theorem.

**Theorem 126.H (parity/support no-go and inverse offset theorem).**

1. For every finite zero-extended Hilbert-space sequence \((z_t)\),
$$
    2\sum_t(-1)^tz_t=\sum_t(-1)^t(z_t-z_{t+1}).          \tag{126.H4}
$$
   This identity has no favorable norm constant.

2. Suppose \(N\) active odd heights have a common nonempty \(m\)-set \(I_*\) inside their literal intervals \([\lceil h/4\rceil,h]\). Among all bounded vector families \(z_h\) supported on those exact intervals, the best constant in
$$
    \left\|\sum_h\chi_4(h)z_h\right\|_2^2
       \le C\sum_h\|z_h\|_2^2                           \tag{126.H5}
$$
   is \(C=N\). For a usual dyadic hard block \(h\in[L,2L]\), one may take
   \(I_*\supset[\lceil L/2\rceil,\lfloor L\rfloor]\), so \(N\asymp L\) and the coherent capacity is \(L^3\) against diagonal capacity \(L^2\).

3. Even after the high-pass replacement, no Bessel gain appears. For \(z_t=(-1)^tw\), \(1\le t\le N\), zero outside,
$$
    {\left\|\sum_t(-1)^t(z_t-z_{t+1})\right\|_2^2
      \over \sum_t\|z_t-z_{t+1}\|_2^2}
      ={4N^2\over4N-2}\asymp N.                          \tag{126.H6}
$$

4. For the actual vectors (126.H2), define the one-orientation physical offset
$$
   \begin{split}
    C_r={}&(-1)^r
    \sum_{\substack{h,h+2r\in\mathscr H_L}}
    \sum_{m=\lceil(h+2r)/4\rceil}^{h}
    a_{\rm end}(h,m)\overline{a_{\rm end}(h+2r,m)}\\
    &\hspace{35mm}\times
    e\!\left(-{2rJ\sqrt m\over\sqrt h+\sqrt{h+2r}}\right).
   \end{split}                                             \tag{126.H7}
$$
   Then
$$
    \mathcal E_L^{\rm top}=\mathcal D_L+2\Re\sum_{r\ge1}C_r. \tag{126.H8}
$$
   Partition the nonempty offsets into \(M\le1+\lceil\log_2(CL)\rceil\) dyadic shells. If \(V=\mathcal E_L^{\rm top}-\mathcal D_L>0\), some complete shell \(\mathcal R\) satisfies
$$
      \Re\sum_{r\in\mathcal R}C_r\ge {V\over2M}.         \tag{126.H9}
$$
   After the unique primitive factorization \(h=ga\), \(h+2r=gb\), \((a,b)=1\), \(b=a+2q\), \(g\) odd, the same conclusion holds for a dyadic \(q\)-shell in
$$
      \mathcal C_L^{\rm off}
        =\sum_{\substack{a>0\\a\text{ odd}}}
         \sum_{q\ge1}(-1)^qF_{L,a}(q), \tag{126.H10}
$$
   with every internal tag of \(F_{L,a}(q)\) retained.

Part 2 is deliberately coefficient-uniform and is only a route obstruction. Parts 1 and 4 apply literally to the actual vectors. No statement here asserts that the actual energy violates its target.

## 3. Proof and hostile derivation

### 3.1 Literal vector, diagonal, sign, and orientation

For integer \(m,h\), the conditions \(\lceil h/4\rceil\le m\le h\) and \(m\le h\le4m\) are equivalent. Hence (126.H2) is exactly the Round-75 transpose, not a softened cone. Expanding (126.H3) gives one diagonal copy of every active \((h,m)\); boundedness of the actual normalized symbol, \(O(L)\) heights, and \(O(L)\) entries per height give \(\mathcal D_L\ll L^2\).

For \(s=h+2r>h\),

$$
 \chi_4(h)\chi_4(s)=(-1)^r,
 \qquad
 J\sqrt m(\sqrt h-\sqrt s)
   =-{2rJ\sqrt m\over\sqrt h+\sqrt s}.
$$

The common \(m\)-range is exactly \(\lceil s/4\rceil\le m\le h\). Taking only \(h<s\) and then one outer \(2\Re\) gives (126.H7)--(126.H8). Including both orientations and another \(2\Re\) would double the cross term. If \(h=ga,s=gb\) is primitive, then \(r=gq\) and \(g\) is odd, so \((-1)^r=(-1)^q\), proving the sign in (126.H10).

The character is inside \(R_m\) before the square. Moving it outside \(|R_m|^2\), taking an outer height Cauchy inequality, or passing to a fixed-\(a\) positive Gram deletes precisely the direction under review.

### 3.2 The spectral proposal has the wrong sign of noninvertibility

Let \(V:\ell^2(\mathscr H_L)\to\ell^2_m\) have columns \(v_h\), and let \(G=V^*V\ge0\). With \(u_\chi=\chi/\sqrt N\),

$$
 \mathcal E_L^{\rm top}=N\langle Gu_\chi,u_\chi\rangle,
 \qquad \mathcal D_L=\operatorname{tr}G.
$$

The generic positive inequality is only

$$
 \langle Gu_\chi,u_\chi\rangle\le\|G\|_{\rm op}
 \le\operatorname{tr}G,
$$

which returns \(\mathcal E_L^{\rm top}\le N\mathcal D_L\), i.e. \(L^3\) capacity. A diagonal-relative target needs the extra \(N^{-1}\) in (126.H1), while the stated absolute target needs the same factor on a populated \(L^2\)-capacity block. A diagonal parity twist \(S_\chi\) is unitary, so

$$
 \|VS_\chi\|_{\rm op}=\|V\|_{\rm op},
 \qquad \|VS_\chi\|_{\rm HS}=\|V\|_{\rm HS}.
$$

Thus a full operator norm or coefficient-blind Bessel theorem cannot see the character. Only the particular direction \(u_\chi\) can see it.

Taking the Fourier transform in \(t\), (126.H4) says that the target is \(\widehat z(\pi)\) and that the difference multiplier is \(1-e^{i\theta}\). At \(\theta=\pi\) its modulus is \(2\), its maximum. The proposed high-pass is therefore an exact selector for the dangerous mode. Formula (126.H6) shows that the finite zero-extension endpoints do not repair the norm: the optimal Bessel constant remains of order \(N\).

### 3.3 The hard-support aligned control is sharp, but not physical evidence

For a dyadic height block \(h\in[L,2L]\), all hard intervals contain a common interval of length \(\asymp L\). Choose a bounded vector \(w\) on this common interval and put

$$
 z_h=\chi_4(h)w.
$$

This obeys the exact affine supports and zero extension. Then

$$
 \sum_h\|z_h\|_2^2=N\|w\|_2^2,
 \qquad
 \left\|\sum_h\chi_4(h)z_h\right\|_2^2=N^2\|w\|_2^2.
$$

Cauchy's inequality supplies the matching upper constant \(N\), proving part 2. With \(|I_*|\asymp L\) and \(N\asymp L\), this is exactly the \(L^2\)-to-\(L^3\) capacity jump.

This control does **not** replace \(z_h\) by the physical vector. In particular it does not prove a lower bound for \(a_{\rm end}(h,m)e(J\sqrt{hm})\). Its sole lawful consequence is that any successful theorem must use a quantified property of the actual phase and amplitude which excludes this alignment. "Parity", "hard support", "bounded entries", "zero extension", "positive Gram", and "noninvertible projection" are not such properties.

### 3.4 Hard faces and one-count slabs supply no hidden small parameter

When \(h\) increases by two, the lower face \(\lceil h/4\rceil\) moves by zero or one and the upper face moves by two. Thus \(v_t-v_{t+1}\) contains upper births, possible lower deaths, and a full common-band phase/amplitude difference. On the common band the phase increment is

$$
 {2J\sqrt m\over\sqrt{h+2}+\sqrt h},                     \tag{126.H11}
$$

which has no uniform distance from the integers. It is not a perturbative \(O(L^{-1})\) increment. The first-failure one-count partition may assign all births, deaths, ceilings, collars, floors, stars, entries, exits, exact centres, terminal members, and zero-extension atoms once, but taking absolute values after that assignment changes an identity into a stronger norm.

On a Round-111 block \(a\asymp A,q\asymp D,g\asymp L/A\), with \(K\asymp JD/A\) and \(\kappa=JD/(AL)\ge D\), the coefficient-blind common-comb capacity is \(DL^2\), while absolute endpoint/slab capacity is \(L^2\sqrt\kappa\). The target is \(L^2\). Hence those norms require respectively a factor \(D\) or \(\sqrt\kappa\) which the high-pass identity does not provide. The scaled-comb total variation is bulk, not boundary-sized. All one-count slabs must therefore remain joint in any actual-vector theorem and in the survivor (126.H10).

### 3.5 Resonance controls rule out a uniform spectral gap, not the theorem

The accepted square-ray owner proves the complete actual square family is \(O_\varepsilon(L^2X^\varepsilon)\), but it does so by retaining the reciprocal \(k\)-phase and obtaining cancellation in \(k\). It does not arise from height parity or a vector Fourier gap. Exact nonsquare centres are also already target-safe in their accepted scope.

The hostile controls remain essential on the residual family:

* near-square/Pell rays show that primitive \(q\)-parity need not alternate along the relevant resonant fibres;
* strict metric incidences persist at the ordinary density \(1/R\), so a density-free "spectral gap" is false;
* for \(X=T^4\), odd \(13\mid T\), \((a,b)=(81,121)\), and \(k=2T^2/13\), the accepted interior control has both actual profile arguments \(9/13,11/13\) equal to one and a half-integral carrier, so the step-two lift ratio is resonant. The offset character supplies no liftwise alternation.

These examples do not lower-bound the complete actual energy because other reciprocal modes and rays can cancel. They do falsify any proof step asserting a uniform phase gap, random-character credit, or automatic parity contraction before that cancellation is proved.

### 3.6 Complete-offset inverse localization

Equation (126.H8) is a finite real identity. Let \(\{\mathcal R_j\}_{j=1}^M\) be the dyadic partition of its nonzero physical offsets. If every shell had real part smaller than \(V/(2M)\), their sum would be smaller than \(V/2\), contradicting

$$
 \sum_j\Re\sum_{r\in\mathcal R_j}C_r
 ={\mathcal E_L^{\rm top}-\mathcal D_L\over2}={V\over2}.
$$

This proves (126.H9). Unique primitive factorization is a bijective reindexing of the same oriented pairs, so the same argument proves the \(q\)-shell version. In particular, a fixed-power violation \(\mathcal E_L^{\rm top}\gg L^2X^\delta\) would force one complete shell of size \(\gg L^2X^{\delta-\varepsilon}\), since \(\log L\ll_\varepsilon X^\varepsilon\).

Round 110 proves only the global real relation

$$
 \Re(\mathfrak C_{L,\mathrm{tag}}^{\mathrm{comp}}-
        \mathcal C_L^{\mathrm{off}})=O_\varepsilon(L^2X^\varepsilon).
$$

It does not identify the correction shell by shell. Therefore a global completed-scalar violation transfers to a physical offset violation above the safe error, but no completed dyadic shell may be declared equivalent without a new tagwise identity. This is the exact limit of the localization theorem.

### 3.7 Capacity ledger

| Object or comparison | Coefficient-blind/coherent capacity | Required scale | Missing gain and audit |
|---|---:|---:|---|
| Diagonal \(\mathcal D_L=\operatorname{tr}G\) | \(L^2\) | \(L^2X^\varepsilon\) | Already safe; one count |
| Actual vector energy \(N\langle Gu_\chi,u_\chi\rangle\) | \(L^3\) | \(L^2X^\varepsilon\) | Full factor \(L\); open for actual vectors |
| Parity high-pass vector | exactly \(4\mathcal E_L^{\rm top}\) | same target | No gain; multiplier is maximal at \(\pi\) |
| Generic positive/Bessel bound | \(N\operatorname{tr}G\asymp L^3\) | \(\operatorname{tr}G\) | Needs the unproved \(N^{-1}\) spectral anti-concentration |
| One-sided \(\Re\mathcal C_L^{\rm off}\) or \(\Re\mathfrak C^{\rm comp}\) | \(L^3\) before sign cancellation | upper bound \(L^2X^\varepsilon\) | Minimal scalar target; lower side follows from energy positivity |
| Complex modulus, blockwise absolute mass, fixed-\(a\) Gram | at least the coherent capacity and strictly stronger | not necessary | Deletes allowed intercancellation; no reverse implication |
| Common-band scaled comb on \((A,D,K,G)\) | \(DL^2\) | \(L^2\) | Missing \(D\); Round-111 bulk obstruction |
| Separated endpoint/one-count slabs | \(L^2\sqrt\kappa\), \(\kappa\ge D\) | \(L^2\) | Missing \(\sqrt\kappa\); must remain joint |
| Adjacent total variation or slabwise \(\ell^1\) | full bulk capacity | \(L^2\) | Strictly stronger and already parked |

## 4. First doubtful or unproved step

The first unproved step is the first inequality after the exact identity (126.H4): any assertion that the single high spectral coefficient

$$
 \left\|\sum_t(-1)^t(v_t-v_{t+1})\right\|_2^2
$$

is \(O_\varepsilon(L^2X^\varepsilon)\) because it is a high-pass, a parity twist, a noninvertible projection, or a vector-valued Bessel quantity. It is exactly \(4\mathcal E_L^{\rm top}\); the difference multiplier is largest at the selected frequency; and the hard-support aligned family forces any coefficient-uniform Bessel constant to be \(\gg L\). No argument in the permitted packet proves the actual Gram anti-concentration (126.H1), and no actual phase/amplitude property is stated that rules out the aligned direction while surviving the square, Pell, fourth-power, hard-face, and endpoint controls.

This failure occurs before reciprocal modes, primitive rays, or one-count slabs are separated. Consequently later slabwise estimates cannot repair the first seam without proving a genuinely new actual-symbol inequality for the complete vector or the complete real off-diagonal.

## 5. Control tests and outcomes

No numerical experiment was used; the audit is entirely algebraic/analytic.

| Required control | Verdict | Exact outcome |
|---|---|---|
| `literal_Round75_hard_top_vector` | **PASS** | (126.H2) uses the literal \(a_{\rm end}\), \(m\le h\le4m\), and exact hard support. |
| `one_orientation_and_outer_2Re` | **PASS** | Only \(h<s\), equivalently \(a<b\), is used, followed by one \(2\Re\). |
| `diagonal_one_count_and_target` | **PASS** | \(\mathcal D_L=\sum_h\|v_h\|^2\ll L^2\); every \((h,m)\) occurs once. |
| `character_inside_vector_before_square` | **PASS** | \(\chi_4(h)\) remains inside \(R_m\); moving it outside is explicitly rejected. |
| `hard_affine_support_and_zero_extension` | **PASS** | Both faces and finite height endpoints are retained. Zero extension is used in (126.H4) and (126.H6), not discarded. |
| `block_energy_vs_offdiagonal_realpart` | **PASS** | (126.H8) and the Round-110 one-sided real equivalence are distinguished from modulus and blockwise absolute norms. |
| `parity_highpass_vector_scope` | **FAIL as a gain** | The identity is correct, but its multiplier has value \(2\) at \(\pi\); the high-pass energy is exactly \(4\mathcal E_L^{\rm top}\). |
| `actual_vs_adversarial_vectors` | **PASS with scope correction** | The affine-support adversary proves only a coefficient-uniform no-go. It is not called an actual lower bound; the actual theorem remains open. |
| `square_Pell_fourth_power_resonances` | **FAIL for a uniform spectral gap** | Square rays are safe only by their accepted \(k\)-cancellation owner; Pell/metric and the explicit fourth-power control defeat automatic parity separation. |
| `one_count_slabs_retained_jointly` | **PASS** | The inverse shell keeps every slab jointly. Any slabwise \(\ell^1\), total variation, or absolute endpoint split is rejected. |
| `capacity_before_and_claimed_gain` | **FAIL for the proposal** | Capacity is \(L^3\), target \(L^2X^\varepsilon\), and the required factor \(L\) is not supplied. Local comb/slab deficits are also displayed. |
| `endpoint_and_prior_owner_scope` | **PASS** | Hard lower and upper faces remain literal; collars, square rays, exact centres, positive-safe blocks, \(q=1\), polylogarithmic, bounded, and terminal owners are not reclaimed. |
| `owner_and_downstream_scope` | **PASS** | The result is only a hard-TOP mechanism obstruction/inverse theorem. It proves nothing about BAL, UNBAL, either M1 route, endpoint uniformity, M9-M2, M9, or an exponent. |

The seam verdict is therefore: all exact vector, sign, orientation, endpoint, and one-count identities pass; the sole proposed analytic gain fails at the first spectral inequality.

## 6. Dependencies and exact artifacts used

The report used only the generated brief and its permitted context:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `strategy/conductor_0821_full_proof_strategy.md`;
5. `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/synthesis.md`;
6. `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/synthesis.md`;
7. `rounds/codex-managed/m9-m2-global-signed-completed-directional/synthesis.md`;
8. `rounds/codex-managed/m9-m2-adjacent-ray-transport-commutator/synthesis.md`;
9. `rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/derivation_packet.md`.

No sibling Round-126 report, excluded blind context, web source, or numerical computation was used. The accepted graph supplies the literal vector, diagonal, offset sign, prior resonance owners, global completed-real self-return, one-count partition, and scaled-comb capacities. The new content is the support-sharp Hilbert-space no-go, its exact finite high-pass control, the Gram anti-concentration correction (126.H1), and the complete dyadic offset inverse theorem.

## 7. Recommended state effect

**Recommendation: promote a narrow obstruction/inverse lemma; retain every analytic target open; park the proposed parity-spectral mechanism.**

The promotable statement is exactly Theorem 126.H:

* parity twisting is unitary at operator-norm level;
* the alternating high-pass selects the \(\pi\)-mode and has no contraction;
* the factor \(L\) loss is sharp for bounded vectors obeying the literal hard affine supports;
* this adversary is not an actual-symbol lower bound;
* every positive actual energy excess localizes, with only a logarithmic loss, to one complete physical or primitive offset shell retaining all one-count data jointly.

Reject any claim that (126.D3), \(U_1-U_3\), a parity-twisted operator norm, a generic positive Gram inequality, or a separated slab norm proves (126.D5). A future positive route must write the literal actual matrix and prove the directional bound \(\langle Gu_\chi,u_\chi\rangle\ll L^2X^\varepsilon/N\) (or the diagonal-relative form (126.H1)), equivalently the one-sided real off-diagonal bound, while explicitly defeating the aligned support model and answering all structured resonance controls.

The parked survivor is

$$
 \boxed{
 \mathcal E_L^{\rm top}
 =\left\|\sum_{h\in\mathscr H_L}\chi_4(h)v_h\right\|_2^2,
 \quad\text{equivalently}\quad
 \Re\mathfrak C_{L,\mathrm{tag}}^{\mathrm{comp}}
 \ll_\varepsilon L^2X^\varepsilon .}
$$

After a hypothesized fixed-power violation, the smallest rigorously localized survivor is one complete dyadic primitive-\(q\) shell in (126.H10), not a fixed-\(a\) Gram, reciprocal mode, lift, collar, endpoint slab, or total-variation piece. Hard TOP remains open. BAL, UNBAL, all M1 owners, endpoint uniformity, M9-M2, M9, the quarter theorem, and every exponent remain unchanged.
