# Blind rederivation: the two-character stationary map is a self-return

## 1. Result: lemma and smallest no-go

**Lemma (stationary self-return, unique product diagonal, and safe diagonal).**
Use \(e(t)=e^{2\pi i t}\) and the Fourier convention

$$
 \widehat f(\xi)=\int_{\mathbb R}f(x)e(-\xi x)\,dx.
$$

For the complete smooth, zero-extended correlation (B.1)--(B.2), two-character Poisson summation has exactly one stationary sign pair. Its dual coordinates are positive odd integers \(p,q\), its saddles are

$$
 r_{p,k+h}=2\sqrt{\frac{M(k+h)}p},\qquad
 s_{q,k}=2\sqrt{\frac{Mk}q},
\tag{1.1}
$$

and its phase is

$$
 \Psi_{p,q,h}(k)
 =\sqrt{Mp(k+h)}-\sqrt{Mqk}.
\tag{1.2}
$$

The two Gaussian units and the two character-Poisson constants cancel exactly. Thus the principal double transform is another literal Fejer block square, with the same shifts and zero extension, formed from

$$
 \widetilde c_k
 =e(-1/8)M^{1/4}k^{-3/4}
 \sum_{\substack{p>0\\p\ {\rm odd}}}
 \chi_4(p)p^{-3/4}
 W\!\left(\frac{X}{2D}\sqrt{\frac p{Mk}}\right)
 q_L\!\left(\frac{Xp}{M}\right)
 e\!\left(\sqrt{Mkp}\right).
\tag{1.3}
$$

Under the uniform smooth-profile interpretation stated in Section 2,

$$
 \mathcal F_{M,H_0}[c]
 =\mathcal F_{M,H_0}[\widetilde c]+O_{W,q}(1).
\tag{1.4}
$$

The principal one-leg map in (1.3) is microlocally involutive: Poisson summation in \(p\), on its stationary sign, returns the original odd \(r\), the phase \(M k/r\), the literal frozen-\(X\) profiles, the character \(\chi_4(r)\), and unit \(1\). Consequently (1.4) is a transform identity and gives no inequality by itself.

The exact dual product defect is

$$
 N=p(k+h)-qk=(p-q)k+ph,
\qquad
 \Psi=\sqrt M\,\frac{N}{\sqrt{p(k+h)}+\sqrt{qk}}.
\tag{1.5}
$$

On the active ranges \(p,q\asymp L\), \(k,k+h\asymp K\), and
\(|h|<H_0\), one has, for all sufficiently large \(X\),

$$
 N=0\quad\Longleftrightarrow\quad p=q\ \hbox{ and }\ h=0.
\tag{1.6}
$$

The complete principal sector \(p=q,h=0\) is target-safe:

$$
 \mathcal D_0\ll_{W,q}X^{1/2}.
\tag{1.7}
$$

No estimate for the remaining signed stationary lattice follows from this rederivation. Its absolute principal norm has scale \(XL/D=X^{1+\ell-\delta}\), a factor \(LH_0\asymp X^{1/2+\ell-\delta}\) above the target. This is only an obstruction to an absolute-value proof, not a signed lower bound. The smallest rigorous no-go is therefore: **double character Poisson plus stationary phase alone self-returns, and the exclusion \(E\ne0\) does not supply a resolvable \(k\)-frequency gap.** A new signed inequality for the off-diagonal block square, or a separate arithmetic inverse theorem for small nonzero \(E\), is still required for (B.4).

## 2. Exact statement and hypotheses

All hypotheses and notation are those in the blind statement. In particular,

$$
 R=X/D,\quad K=XL/D^2,\quad
 H_0=\left\lceil \sqrt X/D\right\rceil,
 \quad C_0=\frac{J+H_0-1}{H_0^2},
 \quad w_h=H_0-|h|.
\tag{2.1}
$$

The smooth stationary estimates below use the standard quantitative meaning of the packet's phrase "fixed smooth compact profiles": after scaling \(r\) by \(R\), \(k\) by \(K\), and the \(q_L\)-argument by \(L\), finitely many required \(C^A\)-seminorms are bounded independently of \(X\), and the active supports stay in fixed compact subsets of \((0,\infty)\). The exact Poisson signs, saddles, phase identities, defect identities, inverse calculation, and conjugacies do not require this quantitative rider; only the displayed uniform remainder in (1.4) does.

For an active pair \((h,k)\), put \(A=M(k+h)>0\) and \(B=Mk>0\). The exact stationary mode sets are

$$
\begin{aligned}
 \mathcal P_{h,k}&=\left\{p>0\text{ odd}:
 W\!\left(\frac{X}{2D}\sqrt{\frac pA}\right)
 q_L\!\left(\frac{Xp}{M}\right)\ne0\right\},\\
 \mathcal Q_k&=\left\{q>0\text{ odd}:
 W\!\left(\frac{X}{2D}\sqrt{\frac qB}\right)
 q_L\!\left(\frac{Xq}{M}\right)\ne0\right\}.
\end{aligned}
\tag{2.2}
$$

They have \(p,q\asymp L\) and \(O(L)\) elements; the active \(k\)-set has \(O(K)\) elements. No rectangular replacement of these sets is made.

With (1.3) extended by zero on the same \(k\)-line, define

$$
 \widetilde{\mathcal F}_{M,H_0}
 =C_0\sum_{|h|<H_0}w_h\sum_k
 \widetilde c_{k+h}\overline{\widetilde c_k}
 =C_0\sum_n\left|\sum_{a=0}^{H_0-1}\widetilde c_{n+a}\right|^2.
\tag{2.3}
$$

The main assertion is (1.4) for the **complete unmasked** correlation. It is not asserted termwise for (B.3), because the nearest-alias and \(E\)-indicators are discontinuous, coupled functions of \(r,s\). The accepted decomposition can be subtracted after transforming the full correlation, but then proving (B.4) is equivalent, up to the accepted target-sized packages, to bounding (2.3).

## 3. Proof and derivation

### 3.1 Exact character Poisson conventions and all sign branches

For every integer \(n\),

$$
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i}.
$$

Hence, for smooth compactly supported \(f\),

$$
\begin{aligned}
 \sum_{n\in\mathbb Z}\chi_4(n)f(n)
 &=\frac1{2i}\sum_{m\in\mathbb Z}
 \left\{\widehat f(m-1/4)-\widehat f(m+1/4)\right\}\\
 &=\frac i2\sum_{\substack{\nu\in\mathbb Z\\ \nu\ {\rm odd}}}
 \chi_4(\nu)\widehat f(\nu/4).
\end{aligned}
\tag{3.1}
$$

For the \(r,s\) phase \(A/r-B/s\), double Poisson therefore gives the exact oscillatory-integral phase

$$
 \Phi_{\mu,\nu}(x,y)
 =\frac A x-\frac B y-\frac{\mu x}{4}-\frac{\nu y}{4},
 \qquad \mu,\nu\text{ odd},
\tag{3.2}
$$

with coefficient \(-\chi_4(\mu)\chi_4(\nu)/4\). There are four Fourier-sign sectors. The \(x\)-leg is stationary only for \(\mu<0\), and the \(y\)-leg only for \(\nu>0\). Thus:

$$
\begin{array}{c|c}
 (\operatorname{sgn}\mu,\operatorname{sgn}\nu)&\text{stationary legs}\\ \hline
 (-,+)&x\text{ and }y\\
 (-,-)&x\text{ only}\\
 (+,+)&y\text{ only}\\
 (+,-)&\text{none}.
\end{array}
\tag{3.3}
$$

Both congruence classes \(1,3\pmod4\) occur in every relevant sign through \(\chi_4\); no quarter branch has been discarded. Set \(\mu=-p\), \(\nu=q\) in the sole double-stationary branch. Since \(\chi_4(-p)=-\chi_4(p)\), its Poisson coefficient is \(+\chi_4(p)\chi_4(q)/4\).

### 3.2 Saddles, phases, Gaussian units, amplitudes, and profile images

The one-leg phases and their exact data are

$$
\begin{array}{c|c|c|c|c}
 &\text{phase}&\text{saddle}&\text{value}&\text{second derivative}\\ \hline
 r& A/x+px/4&2\sqrt{A/p}&\sqrt{Ap}&p^{3/2}/(4A^{1/2})\\
 s&-B/y-qy/4&2\sqrt{B/q}&-\sqrt{Bq}&-q^{3/2}/(4B^{1/2}).
\end{array}
\tag{3.4}
$$

With the \(e(t)\) convention, their Gaussian factors are respectively \(e(1/8)\) and \(e(-1/8)\), and

$$
 |\phi_r''|^{-1/2}=2A^{1/4}p^{-3/4},\qquad
 |\phi_s''|^{-1/2}=2B^{1/4}q^{-3/4}.
\tag{3.5}
$$

On the \(r\)-leg the Poisson coefficient is

$$
 \frac i2\chi_4(-p)=-\frac i2\chi_4(p),
$$

so coefficient, Gaussian unit, and the factor \(2\) in (3.5) combine to \(\chi_4(p)e(-1/8)\). On the \(s\)-leg they combine to \(\chi_4(q)e(1/8)\). Their product is exactly \(\chi_4(p)\chi_4(q)\), with no residual Gaussian sign.

At (1.1), the profiles become

$$
\begin{aligned}
 W_r&\mapsto W\!\left(\frac{X}{2D}\sqrt{\frac p{M(k+h)}}\right),
 &q_{r,k+h}&\mapsto q_L(Xp/M),\\
 \overline{W_s}&\mapsto
 \overline{W\!\left(\frac{X}{2D}\sqrt{\frac q{Mk}}\right)},
 &\overline{q_{s,k}}&\mapsto\overline{q_L(Xq/M)}.
\end{aligned}
\tag{3.6}
$$

Thus the exact principal term indexed by \((h,k,p,q)\), including the literal denominator and Fejer factors, is

$$
\begin{aligned}
 &C_0w_h\,\chi_4(p)\chi_4(q)
 \frac{M^{1/2}}{\{pq\,k(k+h)\}^{3/4}}
 W\!\left(\frac{X}{2D}\sqrt{\frac p{M(k+h)}}\right)
 \overline{W\!\left(\frac{X}{2D}\sqrt{\frac q{Mk}}\right)}\\
 &\hspace{18mm}\times q_L(Xp/M)\overline{q_L(Xq/M)}
 e\!\left(\Psi_{p,q,h}(k)\right).
\end{aligned}
\tag{3.7}
$$

Expanding (2.3) gives precisely (3.7), proving the principal block-square identity.

### 3.3 Complete dual phase, defect, aliases, sectors, and multiplicities

Besides (1.2), the useful exact derivatives are

$$
\begin{aligned}
 \partial_p\Psi&=r_{p,k+h}/4,&
 \partial_q\Psi&=-s_{q,k}/4,\\
 \partial_k\Psi&=\frac{\sqrt M}{2}
 \left(\frac{\sqrt p}{\sqrt{k+h}}-\frac{\sqrt q}{\sqrt k}\right)
 =M\left(\frac1{r_{p,k+h}}-\frac1{s_{q,k}}\right),&
 \partial_h\Psi&=M/r_{p,k+h},\\
 \partial_k^2\Psi&=-\frac{\sqrt{Mp}}{4(k+h)^{3/2}}
 +\frac{\sqrt{Mq}}{4k^{3/2}}.&
\end{aligned}
\tag{3.8}
$$

For completeness, the other nonzero Hessian entries are

$$
\begin{aligned}
 \Psi_{pp}&=-r/(8p),& \Psi_{qq}&=s/(8q),\\
 \Psi_{pk}=\Psi_{ph}&=r/\{8(k+h)\},&
 \Psi_{qk}&=-s/(8k),\\
 \Psi_{kh}=\Psi_{hh}&=-\sqrt{Mp}/\{4(k+h)^{3/2}\},
\end{aligned}
\tag{3.9}
$$

where \(r=r_{p,k+h}\), \(s=s_{q,k}\).

If Poisson is subsequently applied to the \(k\)-sum with integer mode \(j\), its phase is \(\Psi(k)-jk\). At every point, not merely at a stationary point,

$$
 E_j(r,s):=M(s-r)-jrs
 =rs\{\partial_k\Psi-j\}.
\tag{3.10}
$$

Thus a full \(k\)-saddle is exactly the continuous exact-alias surface \(E_j=0\). This is the precise dual-gradient/primal-alias relation. It does **not** identify the discrete \(E\ne0\) survivor with a uniformly nonstationary integral: at integer \(r,s\asymp R\), the information \(E\ne0\) gives only the frequency spacing

$$
 \left|M(1/r-1/s)-j\right|=|E|/(rs)\geq cR^{-2}.
\tag{3.11}
$$

Across a \(k\)-interval of length \(K\), the resolution of this smallest possible spacing is

$$
 K/R^2=L/X=o(1).
\tag{3.12}
$$

Hence nonexactness alone gives no integration-by-parts saving.

The product defect (1.5) is an integer and satisfies \(N\equiv h\pmod2\). If \(N=0\), then

$$
 |p-q|=\frac{p|h|}{k}\ll\frac{LH_0}{K}\asymp H_0^{-1}.
$$

For sufficiently large \(X\), integrality forces \(p=q\), and then \(ph=0\) forces \(h=0\). This proves (1.6), including negative shifts.

The remaining multiplicities are exact:

- \(p=q,h=0\): \(N=0\) for every active \(k\); this is the sole product diagonal.
- \(p=q,h\ne0\): \(N=ph\ne0\) is independent of \(k\), so the same defect has \(O(K)\) \(k\)-multiplicity and \(\chi_4(p)^2=1\).
- \(p\ne q\): \(N=(p-q)k+ph\) is an arithmetic progression in \(k\); a fixed \(N\) determines at most one \(k\).
- For fixed \(p,q,k,N\), there is at most one shift \(h\), and it exists only under the corresponding divisibility and range conditions.

In the equal-mode shifted sector,

$$
 \Psi_{p,p,h}(k)
 =\frac{\sqrt{Mp}\,h}{\sqrt{k+h}+\sqrt k},\qquad
 \partial_k\Psi_{p,p,h}
 =-\frac{\sqrt{Mp}\,h}
 {2\sqrt k\sqrt{k+h}(\sqrt k+\sqrt{k+h})}.
\tag{3.13}
$$

It has no product collision, but also no character cancellation on \(p=q\). In the unequal-mode sector the signs \(\chi_4(p)\chi_4(q)\) remain, but the progression property of \(N\) is only a multiplicity statement, not a signed bound.

Negative shifts are not discarded. The exact involution

$$
 (h,k,p,q)\longmapsto(-h,k+h,q,p)
\tag{3.14}
$$

sends \(N\) to \(-N\) and the term (3.7) to its complex conjugate. Consequently the full \(h\)-aggregate is real and equals the \(h=0\) term plus twice the real part of the positive shifts. This conjugacy uses the full zero extension and symmetric Fejer weight; it is not an assumption about individual profiles being real.

### 3.4 Exact principal inverse and character persistence

Consider one positive reciprocal leg

$$
 S_A(a)=\sum_{r\ {\rm odd}}\chi_4(r)a(r)e(A/r).
$$

Its principal stationary transform is

$$
 T_Aa(p)=A^{1/4}p^{-3/4}a(2\sqrt{A/p})e(\sqrt{Ap}-1/8),
 \qquad p>0\text{ odd},
\tag{3.15}
$$

with the outer sum carrying \(\chi_4(p)\). Apply (3.1) to that \(p\)-sum. The returning stationary Fourier mode is a positive odd integer \(r\), with phase

$$
 \sqrt{At}-rt/4,
$$

saddle \(t_0=4A/r^2\), phase value \(A/r\), negative second derivative, and Gaussian \(e(-1/8)\). At this saddle,

$$
 |\phi''(t_0)|^{-1/2}=4\sqrt2 A^{1/2}r^{-3/2},
\quad
 A^{1/4}t_0^{-3/4}=2^{-3/2}A^{-1/2}r^{3/2}.
\tag{3.16}
$$

Their product is \(2\). Multiplication by the Poisson coefficient \(i/2\), the original unit \(e(-1/8)\), and the returning Gaussian \(e(-1/8)\) gives

$$
 2\cdot(i/2)\cdot e(-1/8)e(-1/8)=1.
\tag{3.17}
$$

The amplitude returns exactly because

$$
 W\!\left(\frac{X}{2D}\sqrt{\frac{t_0}{A}}\right)
 =W(X/(Dr)),\qquad
 q_L(Xt_0/M)=q_L(4Xk/r^2)
\tag{3.18}
$$

when \(A=Mk\). Formula (3.1) also returns \(\chi_4(r)\). The negative reciprocal leg is its conjugate analogue. Therefore both character signs, both physical profiles with \(X\) frozen, and both shifted values \(k+h,k\) return. The transform has introduced no independent randomness or cancellation.

### 3.5 Safe diagonal and the overstrong absolute norm

The unique product diagonal contributes

$$
\begin{aligned}
 \mathcal D_0={}&C_0H_0M^{1/2}
 \sum_k k^{-3/2}\sum_{\substack{p>0\\p\ {\rm odd}}}p^{-3/2}
 \left|W\!\left(\frac{X}{2D}\sqrt{\frac p{Mk}}\right)\right|^2
 \left|q_L(Xp/M)\right|^2.
\end{aligned}
\tag{3.19}
$$

Using \(O(K)\) active \(k\)'s and \(O(L)\) active \(p\)'s,

$$
 \mathcal D_0
 \ll C_0H_0M^{1/2}\frac{KL}{K^{3/2}L^{3/2}}
 =C_0H_0M^{1/2}(KL)^{-1/2}
 \ll X^{1/2}.
\tag{3.20}
$$

Here the exact normalization check is

$$
 K=L(\sqrt X/D)^2=L H_0^2\{1+O(H_0^{-1})\},
 \qquad C_0\asymp K/H_0^2\asymp L.
\tag{3.21}
$$

By contrast, summing the absolute values of all principal terms gives the capacity

$$
 \mathcal N_1
 \ll C_0H_0^2\,KL^2\,
 \frac{M^{1/2}}{K^{3/2}L^{3/2}}
 \asymp \frac{XL}{D}.
\tag{3.22}
$$

If the fixed profiles are bounded below on any interior active product box, the same restricted box proves the reverse inequality, so the actual \(\ell^1\) norm is \(\asymp XL/D\). Since

$$
 \frac{XL/D}{X^{1/2}}\asymp LH_0,
\tag{3.23}
$$

triangle inequality is genuinely too strong throughout the stated range. No signed lower bound is inferred from (3.22).

### 3.6 Stationary, endpoint, and aggregate error ledger

On scale \(x=Ru\), a relevant one-leg phase has large parameter

$$
 \lambda\asymp A/R\asymp pR\asymp RL.
$$

For each relevant mode, one-term stationary phase has leading size \(R\lambda^{-1/2}=\sqrt{R/L}\) and remainder \(O(R\lambda^{-3/2})\). Summing over \(O(L)\) active modes gives, before the factor \(1/k\),

$$
 \text{principal absolute size }O(\sqrt{RL}),\qquad
 \text{summed remainder }O((RL)^{-1/2}).
\tag{3.24}
$$

Thus the double-product error for fixed \((h,k)\), after the literal denominator, is \(O(K^{-2})\). Since

$$
 \sum_{|h|<H_0}w_h=H_0^2,
$$

its aggregate is

$$
 O\!\left(C_0H_0^2\cdot K\cdot K^{-2}\right)=O(1),
\tag{3.25}
$$

which proves (1.4). Higher stationary terms can be retained if a smaller error is wanted.

The three wrong Fourier-sign sectors in (3.3), and modes separated from the active saddle range, are rapidly small by repeated integration by parts. Smooth compact profiles extended by zero are flat at their support boundary, so a saddle entering or leaving such a support creates no hard half-Gaussian endpoint term; its transition is included uniformly in (3.24). The finite block contributes no approximation error: its entries and exits are exactly represented by zero extension and \(w_h\).

There are two endpoints not covered by this clean ledger. First, a later \(k\)-Poisson step must retain the actual zero-extended \(k\)-support and any endpoint saddles; none may be replaced by a rectangle. Second, inserting the literal \(j,E\) mask of (B.3) before \(r,s\)-Poisson creates nonsmooth internal alias boundaries. Those boundary integrals are not part of (3.24)--(3.25). This is why (1.4) is stated for the complete correlation and not falsely asserted termwise for the survivor.

## 4. First doubtful or unproved step

The first invalid step in a direct proof of (B.4) would be to apply the clean stationary formula (3.7) to the masked sum (B.3) as though its \(j,E\)-indicator were a smooth separable amplitude. It is neither; an interpolation or an exact boundary decomposition is required, and no bound for the resulting alias-boundary terms has been proved here.

If one instead transforms the complete correlation and subtracts the three accepted packages, the first unproved step is the needed signed estimate

$$
 C_0\sum_{|h|<H_0}w_h\sum_k
 \sum_{(p,q,h)\ne(p,p,0)}
 \chi_4(p)\chi_4(q)\,\mathcal A_{p,q,h}(k)
 e(\Psi_{p,q,h}(k))
 \ll_\varepsilon X^{1/2+\varepsilon}.
\tag{4.1}
$$

The defect multiplicities, \(E\ne0\), and character signs established above do not prove (4.1). An assertion of a factor \(LH_0\) of signed cancellation at this point is the first genuinely unproved mathematical claim.

## 5. Control tests and outcomes

| Control | Exact input / expected invariant or failure | Outcome | Implication |
|---|---|---|---|
| literal_Round123_near_alias_survivor | The exact \(j\ne0,E\ne0,|E|\le X^{1+\rho}/L\) mask, shifts, denominators, and Fejer factors | The mask cannot be silently passed through smooth \(r,s\)-stationary phase; the full-minus-packages route remains exact | No claim that (3.7) is a termwise transform of (B.3) |
| H0_K_normalization | \(H_0=\lceil\sqrt X/D\rceil\), \(K=XL/D^2\), exact \(C_0\) | \(K=LH_0^2(1+O(H_0^{-1}))\), \(C_0\asymp L\), and \(\sum_h w_h=H_0^2\) | Gives (3.20), (3.22), and the \(O(1)\) error ledger |
| double_character_Poisson_signs | Both copies of (3.1), including both quarter congruence classes | Only \((\mu,\nu)=(-p,q)\) is double-stationary; coefficient is \(+\chi_4(p)\chi_4(q)/4\) | No missing sign branch and no spurious minus sign |
| stationary_points_and_Gaussian_units | Phases \(A/x+px/4\), \(-B/y-qy/4\) | Saddles and curvatures are (3.4); units \(e(1/8),e(-1/8)\) cancel with Poisson constants as stated | Principal amplitude is exactly (3.7) |
| dual_product_defect | Difference of the two square-root products | Exact identity (1.5), with \(N\in\mathbb Z\) and \(N\equiv h\pmod2\) | Product equality is an arithmetic lattice condition |
| dual_gradient_to_primal_alias | A later \(k\)-Poisson mode \(j\) | Exact identities (3.8) and (3.10) | Full \(k\)-stationarity is the continuous exact-alias surface |
| dual_diagonal_one_count | \(N=0\) on active ranges | Only \(p=q,h=0\); its \(O(LK)\) tuples contribute \(O(\sqrt X)\) | A complete strict sector is target-safe |
| equal_mode_shifted_sector | \(p=q,h\ne0\) | \(N=ph\), formulas (3.13), \(O(K)\) repeated defect, and \(\chi_4(p)^2=1\) | Must not be merged with the safe diagonal; remains unproved |
| unequal_mode_sector | \(p\ne q\) | Fixed-\(N\) multiplicity is at most one \(k\) for fixed \(p,q,h\), but signs remain correlated | Counting alone gives no signed saving |
| mode_shift_alias_multiplicity | All \(p,q,k,h\), including negative \(h\) | Multiplicities are listed after (3.12); conjugacy (3.14) is exact | No hidden one-to-one claim and no double counting of negative shifts |
| character_persistence | Genuine \(\chi_4\) on both primal legs | Dual factor is \(\chi_4(p)\chi_4(q)\), and inverse Poisson returns \(\chi_4(r)\chi_4(s)\) | Transform does not manufacture new randomness |
| stationary_endpoint_and_error_ledger | Flat smooth supports, zero extension, all Fejer entries/exits | Wrong signs are nonstationary, smooth support transitions are uniform, aggregate \(r,s\)-error is \(O(1)\); later \(k\)- and alias-mask boundaries remain open | The claimed error scope is explicit |
| signed_joint_aggregation | Full ordered pairs and true characters, versus absolute mass | Principal terms aggregate to the exact block square (2.3); absolute norm is \(\asymp XL/D\) under nondegeneracy; negative shifts are conjugate | Capacity is not promoted to a signed lower bound or upper saving |
| transform_involution_and_norm_scope | Re-Poissonize the principal \(p\)-sum | Saddles (3.16)--(3.18) return phase, amplitude, character, and unit exactly | An identity or invariant norm is not a proof of (B.4) |
| owner_and_downstream_scope | Flat-smooth strict-UNBAL owner only | No hard, sharp, clipped, starred, arithmetic, transition, or downstream claim is made | Result stays within the assigned owner |

The general signed-vs-unsigned, real-vs-complex-pairing, exact-vs-near-resonance, coefficient-adversary, and support-and-degeneracy controls are also respected: true characters were retained; conjugacy was proved rather than assumed; \(N=0\), \(E=0\), and their nonzero counterparts were separated; no adversarial-coefficient theorem was claimed; and all smooth-support qualifications were stated.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were used:

1. rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/briefs/blind_joint_stationary_lattice_rederivation.md -- frozen task, owner, controls, and report contract.
2. rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/blind_statement.md -- all formulas, scales, accepted decomposition facts, and target.
3. problems/gauss_circle.md -- overall problem statement only.
4. state/control_models.md -- proof-unit-test meanings.

No strategy file, proof graph, prior nonblind round, sibling report, web source, or numerical experiment was consulted.

## 7. Recommended state effect

**Retain.** Retain as candidate evidence the exact character-Poisson signs, stationary lattice (1.1)--(1.5), gradient/alias identity (3.10), unique product-diagonal theorem (1.6), target-safe diagonal estimate (1.7), aggregate smooth error ledger, and principal self-return calculation (3.15)--(3.18).

Do **not** promote (B.4). The complete equal-mode shifted and unequal-mode signed sectors are unresolved, and a direct transform of the literal survivor still lacks the required alias-boundary analysis. Reject any claim that the stationary transform itself supplies cancellation, that \(E\ne0\) is uniformly nonstationary on the \(K\)-scale, or that the absolute capacity (3.22) implies a signed lower bound.
