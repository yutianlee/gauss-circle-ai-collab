## 1. Result

**Zero-mode-safe, but no main-term annihilation; the nonzero aliases remain open.**  For the exact Round-114 double-far survivor, the literal factor

\[
\chi _4(h)\chi _4(h')
\]

does not annihilate the actual symbol.  There are sign-coherent actual-symbol sectors of coefficient mass \(\asymp L^4\), and the translation sector \(h'=h\) alone has mass \(\asymp L^3\).  Thus neither \(\chi _4^2\) nor the slanted smooth weight makes the main term identically zero.  In the increment chart \(h'=h+2s\), the character is exactly \((-1)^s\); Poisson summation therefore shifts the dual lattice by one half but leaves a full nonzero stationary family.  Deleting only the zero dual mode is not a saving argument.

There is nevertheless one rigorous target-sized statement.  If the radial exponential is replaced by \(1\) **before any residue, shift, shell, or divisor-pair absolute value is taken**, the fully assembled phase-free double-far aggregate satisfies

\[
 M_B^{(0)}\ll_{B,\varepsilon}L^3X^\varepsilon .
\]

This is cancellation from the literal character in one divisor variable, with the slanted symbol, the low-gcd cutoff, and both sharp far gates retained.  It is a bound, not a vanishing identity.  Consequently the smallest surviving target exposed by this audit is

\[
 \boxed{\quad
 \mathcal R_B^{\mathrm{osc}}
 :=\sum_{\mathrm{df}}a_B(h,k)\overline{a_B(h',k')}
 \bigl(e(R(\sqrt{hk}-\sqrt{h'k'}))-1\bigr),
 \qquad
 |\mathcal R_B^{\mathrm{osc}}|\ll L^3X^\varepsilon .
 \quad}
\]

No argument in the supplied record, and neither audited external theorem, proves this boxed estimate.  The actual-symbol node therefore remains open.

## 2. Exact statement and hypotheses

Let \(X\ge 4096\), \(R=X^{1/2}\), and let \(B\) be one frozen balanced block from the accepted Round-112 dictionary.  On its support,

\[
 h,k,h',k'\asymp L,\qquad hk,h'k'\asymp N:=L^2,
 \qquad R\asymp L^3,
\]

with \(K/L\in[1,16]\).  The persistent critical case is \(j=1\); the \(j=2\) balanced block exists only in the recorded exact-square endpoint \(K/L=16\).  Put

\[
 a_B(h,k)=\chi _4(h)\,
 \eta\!\left(\frac{(h,k)}{G_0}\right)A_B(h,k),
 \qquad G_0=\frac{\sqrt L}{2},
\]

where \(A_B\) is the literal real continuum amplitude

\[
 A_B(x,z)=W(x/L)\Phi(x/(H+1))
 \left(\frac{M}{xz}\right)^{3/4}
 W\!\left(\sqrt{\frac{xX}{4zD^2}}\right),
\]

extended by zero.  The proof below uses exactly the recorded consequences: compact support of normalized diameter \(O(1)\), \(A_B=O_B(1)\), and total variation \(O_B(1)\) on every horizontal or vertical normalized slice.  It does not replace \(A_B\) by a box, erase the gcd cutoff, or take an envelope over slanted weights.

Write

\[
 r=h'k'-hk,\qquad \rho=hk'-h'k,
\]

and let \(\sum_{\mathrm{df}}\) mean the exact support-restricted sum with

\[
 |r|>L,\qquad |\rho|>L.
\]

The double-far block is

\[
 \mathcal E_B^{\mathrm{df}}
 =\sum_{\mathrm{df}}a_B(h,k)\overline{a_B(h',k')}
 e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right).
\]

Define

\[
 M_B^{(0)}:=\sum_{\mathrm{df}}a_B(h,k)\overline{a_B(h',k')},
 \qquad
 \mathcal R_B^{\mathrm{osc}}:=\mathcal E_B^{\mathrm{df}}-M_B^{(0)}.
\]

The proved statement is

\[
 |M_B^{(0)}|\ll_{B,\varepsilon}L^3X^\varepsilon .
\]

The coherent-sector statements below additionally assume that \(B\) is a nondegenerate interior actual block: its literal amplitude is bounded away from zero and has constant sign on a normalized rectangle of positive area.  This holds for the persistent interior core used by the dictionary.  No lower-bound claim is made for a boundary fragment on which the literal amplitude itself vanishes.  One such admissible actual block is already enough to disprove any block-uniform algebraic-annihilation claim.

The already-owned true diagonal \(r=0\), radial corridor \(|r|\le L\), and determinant corridor \(|\rho|\le L\) are not re-estimated as part of the double-far sum.  They are restored below only in explicitly priced control tests.  No conclusion here changes their owners.

## 3. Proof or derivation

### 3.1 Exact charts and what the determinant gate measures

In the divisor chart \(k=n/h\), \(k'=(n+r)/h'\),

\[
 \rho=\frac{h(n+r)}{h'}-\frac{h'n}{h}
 =\frac{h^2(n+r)-h'^2n}{hh'}.
\]

Thus the determinant deletion is exactly

\[
 \bigl|h^2(n+r)-h'^2n\bigr|>Lhh'.
\]

In logarithmic angular variables

\[
 t=\log\frac h{\sqrt n},\qquad
 t'=\log\frac {h'}{\sqrt{n+r}},
\]

one has the identity

\[
 \rho=2\sqrt{n(n+r)}\sinh(t-t').
\]

Since \(n,n+r\asymp L^2\), determinant-far means angular divisor-ratio separation of order at least \(L^{-1}\).  The phase \(R(\sqrt n-\sqrt{n+r})\), however, is purely radial.  Angular separation by itself supplies no oscillation.

In the increment chart

\[
 h'=h+p,qquad k'=k+q,
\]

the exact identities are

\[
 r=hq+kp+pq,qquad \rho=hq-kp,
\]

and hence

\[
 r+\rho=q(2h+p),\qquad r-\rho=p(2k+q).
\]

The character forces \(h,h'\) odd, so \(p=2s\), and then

\[
 \chi _4(h)\chi _4(h+2s)=(-1)^s=e(s/2).
\]

This identity is independent of \(h\), but it is not zero.

### 3.2 The fully assembled phase-free aggregate is target-safe

Fix \(h,k,k'\).  All factors depending only on \((h,k)\) may be pulled outside the \(h'\)-sum.  Expand the remaining gcd weight exactly by divisor Möbius inversion:

\[
 \eta\!\left(\frac{(h',k')}{{G_0}}\right)
 =\sum_{d\mid h',\ d\mid k'}\gamma_d,
 \qquad
 \gamma_d=\sum_{e\mid d}\mu(e)
 \eta\!\left(\frac{d/e}{G_0}\right).
\]

Because \(\eta\) is bounded, \(|\gamma_d|\ll \tau(d)\).  If \(d\) is even, then \(\chi _4(d\ell)=0\).  For odd \(d\), complete multiplicativity gives

\[
 \chi _4(d\ell)=\chi _4(d)\chi _4(\ell).
\]

After writing \(h'=d\ell\), the two far indicators are

\[
 |d\ell k'-hk|>L,qquad |hk'-d\ell k|>L.
\]

Each is the complement of one interval in \(\ell\); together with the compact support of \(A_B(d\ell,k')\), they split the line into \(O(1)\) intervals.  On every such interval the total variation of \(A_B(d\ell,k')\) is \(O_B(1)\): its derivative in \(\ell\) is \(O_B(d/L)\), while its support length is \(O_B(L/d)\).  The sharp gates contribute only \(O(1)\) endpoint jumps.

The partial sums of \(\chi _4\) are bounded by \(1\).  Abel summation therefore gives, uniformly in \(d,h,k,k'\),

\[
 \sum_{\ell}\chi _4(\ell)A_B(d\ell,k')
 \mathbf 1_{|d\ell k'-hk|>L}
 \mathbf 1_{|hk'-d\ell k|>L}
 \ll_B 1.
\]

Summing the divisor expansion costs

\[
 \sum_{d\mid k'}|\gamma_d|
 \ll\sum_{d\mid k'}\tau(d)\ll_\varepsilon X^\varepsilon.
\]

There are \(O_B(L^3)\) choices of the outer triple \((h,k,k')\), and its remaining literal factors are bounded.  Hence

\[
 \boxed{|M_B^{(0)}|\ll_{B,\varepsilon}L^3X^\varepsilon.}
\]

This proof loses its saving immediately if one first takes absolute values in \(h'\), separates the two residue classes, freezes individual \(p\)-shifts, or replaces the slanted amplitude by an unrelated coefficient array.  Its scope is exactly the assembled phase-free aggregate.

### 3.3 Actual-symbol coherent controls: no algebraic vanishing

First take the translation sector \(p=0\), so \(h'=h\).  Then

\[
 r=\rho=h(k'-k),qquad
 \chi _4(h)\chi _4(h')=\chi _4(h)^2=1
\]

for every contributing odd \(h\).  Choose two separated vertical subintervals inside a constant-sign core of the same literal block.  They give \(|k'-k|\asymp L\), hence \(|r|=|\rho|\asymp L^2\), and all coefficient products have one sign and size \(\gg_B1\).  The low-gcd mask does not destroy the count: the number of pairs \((h,k)\) with \((h,k)>G_0\) is

\[
 \ll \sum_{d>G_0}(L/d)^2\ll L^2/G_0\ll L^{3/2},
\]

so after adjoining the free third variable the discarded triples are \(O(L^{5/2}X^\varepsilon)=o(L^3)\).  Thus this literal \(p=0\) sector has sign-coherent coefficient mass \(\gg_B L^3\).  This is target-sized, not zero.

More strongly, choose two small normalized rectangles \(U,V\) in nonzero constant-sign cores so that their normalized products and slopes are separated.  Every cross-pair then has \(|r|,|\rho|\asymp L^2\).  Restricting to

\[
 h'\equiv h\pmod 4
\]

and to the low-gcd majority leaves \(\gg_B L^4\) cross-pairs with a constant character sign.  The sector \(h'\equiv h+2\pmod4\) has the opposite character sign and the same \(L^4\) capacity.  Therefore the full phase-free bound in Section 3.2 is cancellation between two actual, equal-capacity residue sectors; it is not termwise annihilation.

The tempting translation \(h'\mapsto h'+2\) is not a lawful exact pairing.  It changes the slanted amplitude and gcd mask, moves \(r\) by \(2k'\), moves \(\rho\) by \(-2k\), can cross either sharp gate, and changes the nonlinear phase on the critical scale.  Thus this natural character pairing is broken by the literal symbol and gates; no alternative exact pairing is supplied.

These controls are coefficient-mass statements.  They do not assert a lower bound for the full complex exponential sum, because different radial phases and the two residue sectors may cancel.  They prove precisely the hostile point needed here: literal \(\chi _4\) and the literal symbol permit coherent actual contributions and do not algebraically kill the main term.

### 3.4 Poisson and Hessian audit: the character shifts aliases, not capacity

For fixed \((h,k,q)\), put \(p=2s\).  Restoring either deleted corridor in the \(s\)-sum costs only \(O(1)\) lattice points, since

\[
 \rho=hq-2sk,qquad r=hq+2s(k+q)
\]

have slopes \(\asymp L\).  Over the \(O(L^3)\) triples \((h,k,q)\), this restoration is \(O(L^3X^\varepsilon)\), so it is legitimate at the target scale.

The phase including the exact character is

\[
 \phi(s)=R\!\left(\sqrt{hk}-\sqrt{(h+2s)(k+q)}\right)+\frac{s}{2}.
\]

Poisson summation gives integrals with phase \(\phi(t)-mt\), and the stationary equation is

\[
 \phi'(t)=\frac12-R\sqrt{\frac{k+q}{h+2t}}=m.
\]

The zero dual mode has no critical point on the balanced support, because the second term has size \(R\asymp L^3\).  But

\[
 \phi''(t)=R\sqrt{k+q}(h+2t)^{-3/2}\asymp L^2,
 \qquad \phi'''(t)\asymp L,
\]

and \(\phi'\) traverses an interval of length \(\asymp L^3\) as \(t\) traverses its \(L\)-scale support.  Hence there are \(\asymp L^3\) nonzero stationary integers \(m\); an interior stationary integral has natural size \(L^{-1}\).  Modewise absolute values therefore have size \(L^2\) per fixed \((h,k,q)\), worse than the original \(L\)-term \(s\)-sum.  The half-period character has merely translated the stationary lattice.  Cancellation among nonzero aliases is exactly the missing work.

The two-dimensional real Hessian says the same thing in a different chart.  For fixed \((p,q)\),

\[
 F(x,y)=\sqrt{(x+p)(y+q)}-\sqrt{xy}
\]

satisfies

\[
 \det \nabla^2F
 =-\frac1{16}
 \frac{\sqrt{xy}\sqrt{(x+p)(y+q)}(qx-py)^2}
 {x^2(x+p)^2y^2(y+q)^2}.
\]

Thus \(|\det\nabla^2(RF)|\asymp \rho^2\) at the critical scale.  The zero dual vector can be stationary only when \(qx-py=0\), so it is absent on determinant-far.  This is genuine real nondegeneracy.  It is not a coefficient-uniform lattice estimate: nonzero dual vectors fill the gradient image, and for fixed even \(p\) the character product is the constant \((-1)^{p/2}\).  Taking absolute values of the transformed modes spends rather than gains capacity.  No phase-adapted array is used here; the preceding stationary-family control uses the actual symbol.

The outer one-dimensional B-process is likewise capacity-preserving at \(n\asymp L^2\): for \(R\sqrt n\), \(|f''(n)|\asymp1\), the dual length is \(\asymp L^2\), and the Legendre phase is \(X/(4m)\).  It cannot by itself supply the missing factor \(L\).

### 3.5 Fejer/dispersion capacity seam

Let \(b_n=c_B(n)e(R\sqrt n)\) be supported on an interval of \(N\asymp L^2\) integers and set \(C_r=\sum_n b_{n+r}\overline{b_n}\).  The sliding-block Cauchy argument gives, for every integer \(1\le H\le N\), the exact-range inequality

\[
 \left|\sum_n b_n\right|^2
 \le \frac{N+H-1}{H}
 \left(C_0+2\Re\sum_{1\le r<H}
 \left(1-\frac rH\right)C_r\right).
\]

Coefficient-blind divisor bounds give \(\sum_{|r|<T}|C_r|\ll L^2T X^\varepsilon\).  Consequently, if \(H\le L\), the prefactor \(N/H\) turns the radial-shift mass \(L^2H\) into \(L^4X^\varepsilon\).  If \(L\le H\le N\), restoring just the already-owned width-\(L\) radial corridor costs \(L^3X^\varepsilon\) before the prefactor, hence \(L^5H^{-1}X^\varepsilon\) afterwards.  It is target-safe only at \(H\asymp N\), where the inequality includes the full shift range and is tautological for the present purpose.

The determinant-far deletion is a condition on the two divisor representatives inside \(c_B(n+r)\overline{c_B(n)}\), not a scalar mask in \((n,r)\).  No positive-semidefinite factorization of that pair-dependent mask is supplied.  Inserting it into the Fejer identity is therefore invalid, while paying its complement by absolute values incurs the capacity just computed.  A signed or determinant-masked dispersion argument could help only after proving a new positivity/factorization statement or a signed corridor estimate of target strength; neither is in the record.

### 3.6 Primary-source theorem audit

[Cowan, Theorem 1.1](https://arxiv.org/html/2304.12572v1) assumes a positive **fixed** shift, a rational-prime modulus \(N\), even nontrivial characters \(\chi,\psi\bmod N\) with \(\chi\psi\) nontrivial, and nonzero \(u,v\) with \(|\Re u|+|\Re v|<1/2\); its asymptotic lets \(X\to\infty\) with every other quantity fixed.  The present problem has conductor \(4\), the odd character \(\chi _4\), self-correlation \(\chi _4^2\) principal on odd integers, \(u=v=0\), and shifts \(L<|r|\asymp L^2\) that grow with \(X\).  It also has balanced divisor truncation, a low-gcd mask, determinant deletion, a slanted two-variable symbol, and a coupled nonlinear phase.  Every structural hypothesis that could control its Eisenstein term or uniform error is therefore mismatched.  Cowan cannot be invoked here.

[Chamizo, Theorem 1.1 and Corollary 1.6](https://arxiv.org/html/2009.01667v1) treat the complete correlation

\[
 S(x,m)=\sum_{n\le x}r_2(n)r_2(n+m),
 \qquad r_2(n)=4\sum_{d\mid n}\chi _4(d),
\]

and display the nonzero main term, for \(2^k\Vert m\),

\[
 8|2^{k+1}-3|\,\sigma(m/2^k)\frac{x}{m}.
\]

This primary source is positive evidence against character annihilation: the complete \(\chi _4\)-self-correlation has an Eisenstein main term.  Its shift-uniform asymptotic allows \(m=O(x^\eta)\), \(\eta<64/39\), so the bare scale \(m\asymp x\asymp L^2\) lies in range.  It still does not cover the truncated divisor chart, low-gcd cutoff, determinant deletion, slanted smooth weight, or simultaneous nonlinear sum over shifts.  Even the best displayed error at \(m\asymp x\), \(x^{17/23+\varepsilon}\), costs \(x^{40/23+\varepsilon}>L^3\) after shiftwise absolute summation over \(\asymp x\) shifts.  The theorem is therefore diagnostic, not transferable.

## 4. First doubtful or unproved step

The first unproved step is exactly the boxed estimate

\[
 |\mathcal R_B^{\mathrm{osc}}|\ll L^3X^\varepsilon.
\]

Equivalently, one needs a joint estimate for the nonzero half-shifted Poisson aliases while retaining the literal slanted symbol, gcd mask, and divisor-pair determinant deletion.  There is no justified cancellation after separating \(p\), residue classes, radial shells, or dual modes.  Real Hessian nondegeneracy does not supply the required coefficient-uniform lattice cancellation, the outer B-process preserves capacity, and Fejer dispersion is either \(L^4\)-sized or full-scale/tautological.

The coherent controls in Section 3.3 are not lower bounds for \(\mathcal E_B^{\mathrm{df}}\); proving such a lower bound would require ruling out cancellation between phases and opposite residue sectors.  Conversely, the bound for \(M_B^{(0)}\) does not imply a bound for \(\mathcal R_B^{\mathrm{osc}}\), since \(e(R(\sqrt{hk}-\sqrt{h'k'}))-1\) has full variation and is not small.  Treating either implication as automatic is the first invalid seam.

## 5. Required control tests and outcomes

| Audit axis | Outcome | Exact reason |
|---|---:|---|
| Character | **PASS / no annihilation** | \(p=2s\) and \(\chi _4(h)\chi _4(h+2s)=(-1)^s\); the \(p=0\) sector is positive and target-sized. |
| Main term | **REVISE** | The assembled phase-free term is \(O(L^3X^\varepsilon)\), but not identically zero; actual residue sectors each have \(L^4\) capacity. |
| Capacity | **PASS as an obstruction** | Raw double-pair mass is \(L^4\); the phase-free character sum saves one \(L\), whereas modewise Poisson, B-process, or short Fejer does not. |
| Source | **FAIL for transfer** | Cowan violates conductor, parity, product-character, spectral-parameter, and shift-uniformity hypotheses; Chamizo lacks every truncation/mask/weight and is unsafe after shiftwise \(\ell^1\). |
| Owner | **PASS** | True diagonal and the two width-\(L\) corridors remain with their accepted owners; only the Round-114 double-far survivor is tested. |
| Downstream | **NO PASS-THROUGH** | The open actual-energy node and its parent remain open; no downstream exponent or endpoint claim is promoted. |

| Required control | Outcome | Hostile check |
|---|---:|---|
| Literal full-product to divisor-pair identity | **PASS** | \(r=h'k'-hk\), \(\rho=hk'-h'k\), with no character or symbol deletion. |
| Determinant gate after divisor substitution | **PASS** | It becomes \(|h^2(n+r)-h'^2n|>Lhh'\), not a free radial cutoff. |
| Increment chart and parity character | **PASS** | Exact formulas for \(r,\rho\) and exact half-period \((-1)^s\) were used. |
| Low-gcd cutoff and slanted symbol retention | **PASS** | Möbius expansion keeps \(\eta((h',k')/G_0)\); Abel variation uses the actual \(A_B\). |
| Inner versus outer cancellation | **PASS** | The proved saving is inner \(h'\)-character cancellation only for \(M_B^{(0)}\); it is not charged to the radial exponential. |
| Zero frequency and main term | **PASS / REVISE** | Zero dual stationarity is absent off \(\rho=0\), but nonzero aliases survive; phase-free aggregate is bounded, not zero. |
| Shift range and conductor uniformity | **FAIL for external use** | Neither primary-source theorem has the exact conductor/character/shift family needed. |
| Linear versus energy capacity | **PASS** | No linear bound is inferred from a character-erased energy estimate; the \(L^4\to L^3\) saving is exhibited only in the signed phase-free energy. |
| Actual symbol versus phase-adapted control | **PASS** | Coherent controls use sign-stable cores of the literal amplitude; no adversarial coefficient array is substituted. |
| Double-far owner and corridor scope | **PASS** | Restoring an increment corridor costs \(O(L^3X^\varepsilon)\); Fejer restoration includes its prefactor and is not mispriced. |
| Fixed block and no shellwise \(\ell^1\) | **PASS** | One frozen \(B\) is used throughout; no shellwise or residuewise absolute value is hidden in the proof of \(M_B^{(0)}\). |
| Critical \(j=1\) / exact-square \(j=2\) | **PASS** | The argument is uniform for an existing block; it does not manufacture generic \(j=2\) support away from \(K/L=16\). |
| Fejer prefactor and range | **PASS as no-go** | \((N+H-1)/H\) forces \(L^4\) for \(H\le L\), and a restored width-\(L\) corridor is safe only at \(H\asymp N\). |
| External theorem exact fit | **FAIL** | Both sources are recorded only as mismatch/diagnostic evidence, never as proof of the target. |
| Downstream exponent safety | **PASS** | No new exponent, summability, or endpoint conclusion is asserted. |

## 6. Dependencies and exact artifacts used

The derivation used, completely and only within their stated scope:

- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/briefs/actual_symbol_main_term_hostile.md`;
- `protocol.md`;
- `state/proof_obligations.yml`, especially the accepted dictionary and corridor nodes and the open actual-energy parent;
- `state/active_campaign.yml`;
- `strategy/A1_0821_2.md`;
- `strategy/A2_0821_2.md`;
- `strategy/conductor_0821_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/candidates/conductor_shifted_divisor_fork.md`;
- `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/reports/mean_square_ray_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/reports/balanced_packet_actual_symbol_formalization.md`;
- the exact algebraic Hessian, B-process, character-mode, angular-chart, and Fejer-capacity controls supplied by the conductor for this audit.

The only external results checked were the primary texts [Alex Cowan, *A twisted additive divisor problem*, arXiv:2304.12572](https://arxiv.org/abs/2304.12572) and [Fernando Chamizo, *The additive problem for the number of representations as a sum of two squares*, arXiv:2009.01667](https://arxiv.org/abs/2009.01667), published at [DOI 10.1007/s00009-021-01959-3](https://doi.org/10.1007/s00009-021-01959-3).  No numerical experiment, unlisted empirical fit, or secondary-source theorem was used.

## 7. Recommended state effect

**Retain the main actual-energy obligation as open; revise the next target; reject annihilation and theorem-transfer claims.**

1. Promote only after normal seam review the finite lemma \(|M_B^{(0)}|\ll L^3X^\varepsilon\), explicitly labeled “fully assembled phase-free double-far aggregate.”  Its proof cannot be reused after residuewise, shiftwise, shellwise, or divisor-pair absolute values.
2. Record as a rigorous obstruction that the literal character and slanted symbol do **not** annihilate the main term: the \(p=0\) actual sector survives at \(L^3\), and opposite residue sectors each carry \(L^4\) coefficient mass.
3. Reject any proof step saying “the zero Poisson mode is absent, therefore the block saves \(L\).”  The half-shifted nonzero stationary family has full capacity.
4. Reject Cowan or Chamizo as a direct owner of the present estimate.  Cowan fails exact hypotheses; Chamizo proves a useful nonzero complete main term but does not survive the present truncations, masks, weights, and shift summation.
5. Replace the vague “main-term analysis” target by the smallest surviving estimate \(|\mathcal R_B^{\mathrm{osc}}|\ll L^3X^\varepsilon\), or an equivalent joint nonzero-alias estimate with the actual symbol.  Do not split it by \(p\), residue, or dual mode before cancellation.
6. Make no change to the true-diagonal/corridor owners, the open actual-energy node, its parent balanced estimate, or any downstream exponent claim.
