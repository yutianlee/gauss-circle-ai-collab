# Round 26 report: beta physical-kernel attack (normalization-corrected)

## 1. Result

**Scoped no-go plus a useful resonance lemma.**  The previous candidate claim that one-dimensional \(\alpha\)-stationary phase itself changes the character coefficient to \(q^{-1}\) is false.  The exact Round-20 amplitude and the stationary factor cancel every power of \(q\), leaving a \(q^0\) character Dirichlet kernel.  Hence the arctangent/logarithmic-series mechanism is retracted as a consequence of stationary phase.  A separate expansion of the hard-top Hilbert factor could create a \(q^{-1}\) subterm, but that expansion is nonuniform at its pole and is not used here.

The corrected positive result is that the actual periodic \(\chi _4\) Dirichlet kernel has only logarithmic \(L^1\) cost after radial \(x\)-integration, despite attaining size \(\asymp Q\) at exact quarter-lattice resonance.  This removes the pure-sine resonance as an \(L^1\) obstruction, but does not yet prove the normalized \(O_\varepsilon(X^\varepsilon)\) transition estimate.

## 2. Exact statement and hypotheses

Let \(\sigma=\Re s\), \(\zeta=\Re z\), and retain the actual beta-transition partition
\[
 \Theta_\beta(\alpha,\beta)=\psi(\beta)(1-\psi(\alpha)),
\]
including both derivative terms in its Cauchy--Pompeiu connector.  For a dual incidence \(m=hq\), the relevant exact finite integrand is Round 20 (6)--(7):
\[
 \chi _4(q)R_\beta |\alpha/2|^{\sigma+\zeta/2-1/2}
 \widehat W_j(a+i(\alpha-\beta-\nu))\widehat\phi(b+i\nu)
 \Big(\frac{D_j}{2\sqrt X}\Big)^a(H_j+1)^b
 \Big(\frac hq\Big)^{\zeta/2}(hq)^{-\sigma}
 x^{-\sigma-3/4-b/2}e^{i\Psi_\alpha(x)}.
\]
The finite polytope, floors, endpoint stars, radial endpoints, shifted line, connector, outside sides, and the once-counted \(A=0\) residue remain part of the formula.  For the hard top,
\[
 \widehat W_0(a+i\mu)=\frac1{a+i\mu}+\widehat W_{+,r}(a+i\mu),
 \qquad \mu=\alpha-\beta-\nu,
\]
and this coupled Hilbert factor is not replaced by its absolute value or by \((i\alpha)^{-1}\).

Define
\[
 D_Q^{\chi}(\theta)=\sum_{1\le q\le Q}\chi _4(q)e^{-iq\theta}.
\]
Then, uniformly for \(Q\ge2\),
\[
 \sup_{M\le Q}|D_M^{\chi}(\theta)|
 \ll \min\{Q,1+|\cos\theta|^{-1}\},\qquad
 \int_0^{2\pi}\sup_{M\le Q}|D_M^{\chi}(\theta)|\,d\theta
 \ll\log(2Q). \tag{26.1}
\]
The same conclusion holds for interval sums and uniformly BV cutoffs by Abel summation.

## 3. Proof or derivation

The phase has
\[
 \partial_\alpha\Psi_\alpha
 =\log\!\frac{\alpha D_j}{\pi q\sqrt{Xx}},\qquad
 \alpha_0=\frac{\pi q\sqrt{Xx}}{D_j}=:C_j(x)q,
 \qquad \Psi_\alpha''(\alpha_0)=\alpha_0^{-1}.
\]
Thus one-dimensional stationary phase contributes \(\alpha_0^{1/2}\).  The total \(q\)-exponent is exactly
\[
 (\sigma+\zeta/2-1/2)+1/2-\zeta/2-\sigma=0. \tag{26.2}
\]
Equivalently,
\[
 \alpha_0^{\sigma+\zeta/2}
 (h/q)^{\zeta/2}(hq)^{-\sigma}
 =C_j(x)^{\sigma+\zeta/2}h^{\zeta/2-\sigma}.
\]
This agrees with the exact inverse-Mellin sine-kernel control, whose character coefficients have size \(q^0\), not \(q^{-1}\).  At the saddle the remaining leading phase is linear,
\[
 e^{-i\theta_j(x)q},\qquad
 \theta_j(x)=\frac{\pi\sqrt{Xx}}{D_j},
\]
up to factors independent of \(q\).

For complete pairs of residue classes,
\[
 \sum_{k=0}^{K}\big(e^{-i(4k+1)\theta}-e^{-i(4k+3)\theta}\big)
 =(e^{-i\theta}-e^{-i3\theta})
 \frac{1-e^{-i4(K+1)\theta}}{1-e^{-i4\theta}}.
\]
This proves (26.1); the only large peaks occur at \(\theta=\pi/2\pmod\pi\), where the bound is \(\min(Q,|\theta-\theta_0|^{-1})\), whose integral is \(O(\log Q)\).

Moreover
\[
 \theta_j'(x)=\frac{\pi\sqrt X}{2D_j\sqrt x}\ne0.
\]
After \(y=\theta_j(x)\), splitting into \(2\pi\)-periods gives, for any transformed radial weight \(w(y)\) of bounded variation,
\[
 \int |w(y)|\sup_{M\le Q}|D_M^\chi(y)|\,dy
 \ll \log(2Q)\big(\|w\|_1+\operatorname{Var}(w)+\|w\|_\infty\big). \tag{26.3}
\]
Thus exact and near quarter-lattice resonances impose only logarithmic radial \(L^1\) cost.

## 4. First doubtful or unproved step

The first unproved step is a uniform stationary-phase decomposition of the **connector-completed** finite operator while retaining \(\widehat W_0(a+i(\alpha-\beta-\nu))\).  It must cover saddle entry/exit, both mask edges, the Hilbert-pole region \(\alpha-\beta-\nu=0\), the \(\psi'(\beta)(1-\psi(\alpha))-\psi(\beta)\psi'(\alpha)\) connector density, and finite outside sides.  Formula (26.3) controls the resulting pure Dirichlet resonance only after these reductions are justified; it does not supply their uniform error or the full \(X,D_j\) bookkeeping.

## 5. Control tests and outcomes

- **Signed versus unsigned:** the unsigned geometric Dirichlet kernel also has logarithmic \(L^1\) norm.  Therefore (26.3) alone is not a character-specific proof of M1.
- **Coefficient adversary:** arbitrary bounded signs can have \(L^1\) size \(\gg Q^{1/2}\); no uniform logarithmic lemma survives.  Period-four structure is essential to (26.1).
- **Support and degeneracy:** \(\Psi''(\alpha_0)=1/\alpha_0\) is nonzero and \(\theta_j'(x)\ne0\), but endpoint saddles and the top Hilbert pole remain untreated.
- **Exact versus near resonance:** exact resonance has height \(\asymp Q\), but width \(\asymp Q^{-1}\); the full neighborhood contributes \(O(\log Q)\), not \(O(Q)\), radially.

## 6. Dependencies and exact artifacts used

`protocol.md`, `state/proof_obligations.yml`, `state/active_campaign.yml`, Round-19 synthesis, Round-20 synthesis and `reports/blind_diagonal_transition_kernel.md` equations (5)--(7), Round-24 synthesis, and Round-25 synthesis.  No numerical experiment or external theorem was used.

## 7. Recommended state effect

**Retain** `M9-M1-beta-transition-connector-reduction` and the transition estimate as open.  **Reject** the claim that stationary phase alone produces a \(q^{-1}\) arctangent kernel.  **Retain as candidate evidence** the exact \(q^0\) normalization (26.2) and the logarithmic radial \(L^1\) resonance lemma (26.1)--(26.3).  The smallest next obligation is the uniform stationary-phase/Hilbert-pole decomposition of the connector-completed actual-top kernel, with all finite sides and the already-closed \(R_1\) residue ledger preserved.
