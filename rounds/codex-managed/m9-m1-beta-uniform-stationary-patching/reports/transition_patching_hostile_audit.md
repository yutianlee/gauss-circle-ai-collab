# Round 28 hostile audit: beta-transition patching

## 1. Result

The proposed extension of the Round-27 \(q^{-2}\) mechanism to the whole beta-transition trace is **not yet valid**. There is an actual-profile finite-height obstruction: if the spatial top pole is integrated only over \(|\nu|\le V\), then when its moving location \(L=\alpha-\beta\) reaches an endpoint,
\[
C_{a,V}(V)=-iH(V)\log (1/a)+O_{H,V}(1),\qquad a\downarrow0.
\]
For the accepted height profile, \(H(V)\) is generically nonzero. Thus neither an isolated finite-\(V\) principal-value limit nor a uniform passage through saddle/endpoint coalescence exists. The omitted \(|\nu|>V\) contribution or the corresponding finite-contour side may cancel the logarithm, but no accepted identity proves that cancellation uniformly in the moving \(L\).

The narrow survivor is the already local one: on a compact patch separated from the \(\alpha\)-endpoints, the moving top pole, \(\rho=0\), and the \(v=0\) axial residue, with fixed \(b>0\), both the positive- and negative-\(\alpha\) stationary contributions of the post-endpoint \(R_1\) term have the Round-27 \(q^{-2}\) capacity. This does not close the beta-transition sector, the double-bounded box, or the dyadic scale sum.

## 2. Exact statement and hypotheses

Let the finite \(\alpha\)-interval imposed by the old boxes be
\[
A_-(\beta,\nu)=\max\{\beta+\nu-U,-2S-\beta\},\qquad
A_+(\beta,\nu)=\min\{\beta+\nu+U,2S-\beta\}.
\]
Let
\[
\alpha_0=\frac{\pi q\sqrt{Xx}}{D_j},\qquad
\theta_j(x)=\frac{\pi\sqrt{Xx}}{D_j},
\]
and let \(H_b(\nu)\) denote all nonsingular factors multiplying the hard-top kernel
\((a+i(\alpha-\beta-\nu))^{-1}\) after the accepted \(R_1\) endpoint split. On every fixed line \(b>0\),
\[
\widehat\phi(b+i\nu)\ll_b(1+|\nu|)^{-3};
\]
the implied constants can grow polynomially in \(b^{-1}\), hence only polylogarithmically for \(b\asymp1/\log X\). This estimate is not uniform through \(b=0\), where
\(\widehat\phi(v)=v^{-1}+O(1)\) and the axial residue must be kept separately.

The certified local patch requires, for some fixed \(c>0\),
\[
\operatorname{dist}(\pm\alpha_0,\{A_-,A_+\})\ge c\sqrt{\alpha_0},\quad
|\alpha-\beta-\nu|\ge c,\quad |\rho|\ge c,
\]
and excludes finite-\(\nu\) endpoints. There the \(R_1\) factor \(1/\rho\asymp q^{-1}\), followed by signed top convolution \(O_b(\alpha_0^{-2})\), yields the local coefficient
\[
\frac{D_j}{q\alpha_0}
=\frac{D_j}{q^2\theta_j(x)}
=\frac{D_j^2}{\pi q^2\sqrt{Xx}},
\]
up to the other accepted profile, \(h\), radial, and real-part factors.

## 3. Proof or derivation

Put
\[
C_{a,V}(L)=\int_{-V}^{V}\frac{H_b(\nu)}
 {a+i(L-\nu)}\,d\nu .
\]
At \(L=V\), set \(y=V-\nu\). Then
\[
C_{a,V}(V)
=H_b(V)\int_0^{2V}\frac{dy}{a+iy}
+\int_0^{2V}\frac{H_b(V-y)-H_b(V)}{a+iy}\,dy .
\]
If \(H_b\) is \(C^1\) near \(V\), the second integral is uniformly \(O_{H,V}(1)\), while
\[
\int_0^{2V}\frac{dy}{a+iy}
=-i\log(1/a)+O_V(1).
\]
The accepted profile is analytic on \(b>0\) and not identically zero, so one may choose an admissible finite \(V\) with \(H_b(V)\ne0\). This is an actual-profile falsifier of any claim that the truncated segment alone has a uniform \(a\downarrow0\) limit. On the whole real line the opposite side supplies the other half of the principal value, but that is precisely the unproved outside-\(V\)/finite-side reconciliation. Taking \(V\to\infty\) first for fixed \(L\) does not suffice because \(L=\alpha-\beta\) grows with the stationary point and the old side limits also involve \(U,S\).

Stationary phase is likewise nonuniform at the finite \(\alpha\)-edges. With
\[
\tau_\pm=\frac{A_\pm-\alpha_0}{\sqrt{\alpha_0}},
\]
the regime \(\tau_\pm=O(1)\) is governed by an incomplete Fresnel integral, not by the interior Gaussian plus an asserted half-weight. Differentiating this uniform model in \(q,x,\nu\) also differentiates \(\tau_\pm\); those boundary terms have not been bounded. Simultaneous coalescence of an \(\alpha\)-edge with \(L=\pm V\) couples the Fresnel and logarithmic layers, so the two patches cannot be pasted independently.

The negative-\(\alpha\) side is not disposable as nonstationary. For the accepted signed Stirling phase,
\[
\frac{\partial\Psi}{\partial\alpha}
=\log\frac{|\alpha|D_j}{\pi q\sqrt{Xx}},
\]
so there are saddles at \(\alpha=\pm\alpha_0\), with Hessians
\(\Psi''(\pm\alpha_0)=\pm\alpha_0^{-1}\). Their Gaussian factors have the same magnitude \(\asymp\alpha_0^{1/2}\) and opposite Fresnel phase. Away from \(\rho=0\), the negative saddle also has
\(|1/\rho|\asymp\alpha_0^{-1}\asymp q^{-1}\); its reflected signed top convolution has the same \(O_b(\alpha_0^{-2})\) magnitude. Hence it has the same \(q^{-2}\) local capacity as the positive saddle. The beta mask, finite boxes, and one-sided height profile do not give an exact reflection identity, so cancellation between the two saddles cannot be assumed; for an upper bound their contributions must be added, and selected phases can reinforce.

The artificial \(\rho\)-split is harmless only after exact recombination:
\[
R_1=\omega G+(1-\omega)R_1-\omega E_1 .
\]
If endpoint asymptotics, masks, or finite-side limits are applied separately, derivatives of \(\omega\) and boundary assignments need not cancel. No uniform estimate supplied in this round justifies that interchange near \(\rho=0\).

Finally, \(q^{-2}\) is only one summation coordinate. The displayed local factor alone gives
\[
\sum_{D_j\lesssim\sqrt X}\frac{D_j^2}{\sqrt X}\asymp\sqrt X
\]
for dyadic \(D_j\). This is not a lower bound for the trace—the omitted factors may save it—but it falsifies closure based only on absolute \(q\)-summability. The exact \(h,x\), profile, and real-part exponents must be retained before the \(j\)-sum is certified.

## 4. First doubtful or unproved step

The first missing step is a single finite-contour identity that keeps the inside-\(\nu\) integral, the outside-\(\nu\) completion, and every horizontal/vertical side together while \(a\downarrow0\), followed by a justified joint or nested exhaustion in \(U,V,S\). Without it, the logarithm at \(L=\pm V\) can be hidden by writing a formal whole-line PV distribution but is not actually cancelled.

After that, one still needs a two-parameter uniform asymptotic covering \(\tau_\pm=O(1)\) and \(a+i(L\mp V)=O(1)\), on both signs of \(\alpha\), with constants polynomial in \(b^{-1}\). The current packet contains neither result.

## 5. Required control tests and outcomes

1. **Actual-profile endpoint test:** the calculation above gives
   \(-iH_b(V)\log(1/a)\); outcome: the isolated finite-height limit fails.
2. **Outside-side test:** no accepted formula pairs that term with an equal opposite contribution uniformly for moving \(L\); outcome: unresolved.
3. **Endpoint-saddle test:** \(\tau_\pm=O(1)\) produces incomplete Fresnel behavior; outcome: interior stationary phase is insufficient.
4. **Negative-\(\alpha\) test:** the signed phase has saddles at both \(\pm\alpha_0\); outcome: assumed negative-side nonstationarity is false, while its local normalization is again \(q^{-2}\).
5. **Height-line test:** fixed \(b>0\) gives cubic decay with polynomial \(b^{-1}\)-loss, but \(b=0\) has a genuine pole and residue; outcome: fixed-line bounds survive only with the axial term separate.
6. **Scale test:** \(q^{-2}\) sums, whereas the isolated dyadic \(D_j^2/\sqrt X\) factor does not meet the target; outcome: the complete exponent ledger is still required.

## 6. Dependencies and exact artifacts used

This audit used only the Round-28 brief; state/active_campaign.yml; the Round-20 diagonal-transition synthesis; the Round-25 radial-endpoint synthesis; the Round-27 beta-radial-pushforward synthesis; and the two Round-27 reports blind_hierarchical_recombined_identity.md and radial_pushforward_qbv_attack.md. It also used the accepted finite-box constraints, exact hard-top transform, signed Stirling phase, \(R_1=-C\,I_1(\rho)/\rho\), and the accepted fixed-\(b\) height-transform estimate recorded there. No claimant Round-28 report was read.

## 7. Recommended state effect

**Retain, sharply scoped:** keep the Round-27 \(q^{-2}\) stationary capacity only on compact patches separated from all endpoint, pole, and artificial-split seams, for each sign of \(\alpha\) and fixed \(b>0\).

**Promote as a no-go/control obligation:** a finite-\(\nu\) segment cannot be replaced by a whole-line PV before its outside contribution and finite sides are recombined; the actual profile exhibits a logarithmic endpoint obstruction.

**No promotion of the target:** keep M9-M1-BetaTransition open. The double-bounded box remains independently owned and unproved; it cannot be silently absorbed into the beta-transition estimate. The absolute exterior normalization remains unchanged because no new global contribution has been certified.
