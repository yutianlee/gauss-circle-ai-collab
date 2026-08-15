# Reflected-mode signed correlation attack

Campaign: m9-m1-reflected-mode-correlation  
Round: 16  
Role: signed-correlation attacker  
Graph SHA-256: 7619a6b552347ce9b522018a104aeaa048304e2913ea1e072e583c0a2ace2c86

## 1. Result

**Sharp no-go result.** Functional-equation reflection cannot algebraically
cancel the hard-top angular cutoff. After placing a mode and its reflection
in common angle coordinates, the principal-value parts have opposite signs,
but their Perron half residues have the same sign because the centered
functional equation has root number \(+1\). With perfectly matched profiles,
their sum is the full angular completion, not zero. With the actual M1
profiles, reflection leaves a centered angular-sign defect.

Thus neither profile complementarity, residue cancellation, nor an abstract
Hilbert-transform \(L^2\) bound proves GAR. The smallest surviving object is
a maximal character-weighted angular-sign radial sum.

## 2. Exact statement and hypotheses

Let
\[
d_{h,q}=2\sqrt X\sqrt{h/q},\qquad A_D(h,q)=D/d_{h,q},
\]
and let \(\Pi(A)=1_{A>1}+\tfrac12 1_{A=1}\). For a finite sum
\(F(u)=\sum_\nu c_\nu A_\nu^u\), symmetric Perron inversion gives
\[
\mathscr P(F):=\sum_\nu c_\nu\Pi(A_\nu)
=\frac12\sum_\nu c_\nu+
\frac1{2\pi}\lim_{T\to\infty}\operatorname{PV}
\int_{-T}^{T}\frac{F(it)}{it}\,dt.
\]
Consequently
\[
\mathscr P(F)+\mathscr P(F(-\,\cdot))=\sum_\nu c_\nu,
\]
while
\[
\mathscr P(F)-\mathscr P(F(-\,\cdot))
=\sum_\nu c_\nu\operatorname{sgn}(\log A_\nu).
\]
The Round-15 incidence factor is exactly
\[
\left(\frac D{2\sqrt X}\right)^u n^{u/2}h^{-u}
=A_D(h,q)^u,\qquad n=hq.
\]
Angle reflection \(h\leftrightarrow q\) sends
\[
d_{h,q}\mapsto d_{q,h}=4X/d_{h,q}.
\]
Therefore \(A_D\mapsto A_D^{-1}\) requires simultaneously
\[
D\mapsto D^\vee=4X/D.
\]
For every actual M1 scale \(D\le\sqrt X\), \(D^\vee\ge4\sqrt X\), outside
the original denominator range. The actual scale measure is not
reflection-invariant.

## 3. Proof or derivation

For \(A>0\),
\[
\frac1{2\pi}\operatorname{PV}\int_{-T}^{T}\frac{A^{it}}{it}\,dt
=\frac1\pi\int_0^T\frac{\sin(t\log A)}t\,dt
\longrightarrow \frac12\operatorname{sgn}(\log A).
\]
Adding the Perron residue \(1/2\) proves the projector formula, including
the endpoint half weight. Replacing \(A\) by \(A^{-1}\) reverses the
principal value but not the residue, proving the two identities.

Hence ideal reflected matching cancels only the odd principal-value part
and leaves the completed coefficient—the Hardy return already identified
in Round 15. Actual matching fails additionally because \(D^\vee\) is
absent, and because \(((H_D+1)/h)^v\), the height floor, and
\(\Phi(h/(H_D+1))\) have no reflected partner. The identity
\(\Phi(t)+\Phi(1-t)=1\) does not help: angle reflection is reciprocal, not
\(t\mapsto1-t\).

A maximal-Hilbert reformulation is equivalent to smooth truncations of the
same angular projector. Plancherel creates correlations among
\(\log(q/h)\); equal ratios collide exactly and near ratios have no uniform
spacing. Thus the necessary \(L^2\) estimate is itself a new angular-ratio
correlation theorem.

## 4. First doubtful or unproved step

The first unproved step is the pointwise maximal bound
\[
\sup_T\left|\sum_{hq\le16\sqrt X}\chi_4(q)(hq)^{-3/4}
e(\sqrt{Xhq})\,\mathcal H_{T,X}(h,q)\right|
\ll_\epsilon X^\epsilon,
\]
where \(\mathcal H_{T,X}\) retains the scale sum, height floors, \(\Phi\),
endpoint stars, and the truncated Perron kernel
\(K_T(\log(D/d_{h,q}))\). No accepted theorem controls this sum.

## 5. Required control test and outcome

Analytically, \(\Pi(A)+\Pi(A^{-1})=1\), not \(0\). Geometrically, at
\(X=y^2,n=7\), \((h,q)=(1,7)\) is active while its reflection \((7,1)\)
is absent. Both exact controls confirm reinforcement/completion rather than
cancellation. No numerical experiment was used.

## 6. Dependencies and exact artifacts used

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- state/best_proof_draft.md
- rounds/codex-managed/m9-m1-angular-mellin-separation/synthesis.md
- rounds/codex-managed/m9-combined-top-cones/synthesis.md
- the assigned Round-16 brief

No other Round-16 report was read.

## 7. Recommended state effect

**Promote** the scoped reflected-Perron no-go: ideal reflection gives full
Hardy completion; the actual profile instead leaves an angular-sign defect.
**Retain open** M9-M1-top-Perron-angular-correlation and GAR, with the
displayed maximal angular-sign sum as the smallest surviving kernel. Make
no change to M9-M1, M9, or the Gauss-circle target.
