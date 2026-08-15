## 1. Result

**Narrow abstract certification; no certification of the claimed post-module actual operator.** For a fixed finite product rectangle and a separately meromorphic kernel whose only crossed divisors are simple normal-crossing \(u=0\) and \(v=0\), the complete sixteen-stratum product Cauchy--Green expansion is exact and independent of whether \(u\) or \(v\) is moved first. The one-axis connectors have positive density \(\psi'(\beta)/2\), the mixed density is \(+\psi''(\beta)/4\), all connector faces and connector-axis residues are forced, and the joint corner occurs once.

The stronger actual claim is not presently licensed. The accepted endpoint and \(R_1\)-arithmetic bounds begin only after physical profile limits, while radial-side deletion uses a nested \(S=S(X,U,V)\) limit. Neither accepted statement says that the two-axis transfer commutes with those limits. Thus one may define and shift the **full finite vector complement**, with every finite side and arithmetic stratum retained, but one may not identify it with a finite “endpoint-free, side-removed, physical” operator. The first explicit unaccounted share is the two-axis transfer of the finite renormalized side and any finite arithmetic representative routed only by a physical-limit theorem.

## 2. Exact statement and hypotheses

Write \(u=x+i\mu\), \(v=y+i\nu\), and

\[
 \Theta(\mu,\nu)=\psi(\beta),\qquad
 \beta=t-\frac{\mu+\nu}{2}.
\]

Let \(\mathcal R_u=[a_-,a_+]\times[-U,U]\) and
\(\mathcal R_v=[b_-,b_+]\times[-V,V]\), with \(a_-<0<a_+\) and
\(b_-<0<b_+\). Assume:

1. \(\psi\in C^2\);
2. \(Q(u,v)\) is separately meromorphic near the closed product, has no boundary pole, and its crossed axial divisors are normal crossings;
3. all integrals and residues admit Fubini/order reversal;
4. any non-axial divisor is either outside the product or is included, with all collision residues, in the residue operator;
5. the same actual profiles, floors, stars, characters, finite contours, and regularization are used on every stratum.

For \(j=u,v\), let \(L_j\) denote the final negative-real-part vertical, let
\[
 F_j=H_{j,+}-H_{j,-}
\]
with each \(H_{j,\pm}\) parametrized left-to-right, let
\(R_j=2\pi i\,\operatorname{Res}_{j=0}\), and define

\[
 C_u(W,Q)=-\iint_{\mathcal R_u}\partial_\mu W\,Q,\qquad
 C_v(W,Q)=-\iint_{\mathcal R_v}\partial_\nu W\,Q.                         \tag{34.1}
\]

Then the initial positive vertical in each variable equals
\((L_j+F_j+R_j+C_j)\). The complete product expansion is (34.2).

## 3. Proof or derivation

Positive rectangle orientation in one variable gives
\[
 V_{j,+}[WQ]=L_j[WQ]+F_j[WQ]+R_j[WQ]+C_j(W,Q).                           \tag{34.2a}
\]
Since
\[
 -\partial_\mu\Theta=-\partial_\nu\Theta=\frac12\psi'(\beta),             \tag{34.2b}
\]
both one-axis connectors have the positive one-half sign. Applying (34.2a) successively and retaining every resulting stratum gives

\[
\begin{aligned}
V_{u,+}V_{v,+}[\Theta Q]={}&L_uL_v\\
&+F_uL_v+L_uF_v+F_uF_v\\
&+R_uL_v+L_uR_v+R_uF_v+F_uR_v+R_uR_v\\
&+C_uL_v+L_uC_v\\
&+C_uF_v+F_uC_v\\
&+C_uR_v+R_uC_v\\
&+C_uC_v,                                                               \tag{34.2}
\end{aligned}
\]
all acting on \((\Theta,Q)\). This is the complete sixteen-term product. In particular,
\[
 F_uF_v=(H_{u,+}-H_{u,-})(H_{v,+}-H_{v,-}),                              \tag{34.3}
\]
so its four face corners have signs \(+,-,-,+\). The terms
\(C_uF_v,F_uC_v\) are the connector boundary faces. The connector-axis term, for example, is
\[
 R_uC_v
 =-2\pi i\iint_{\mathcal R_v}
 \partial_\nu\Theta(0,\nu)\operatorname{Res}_{u=0}Q\,dA_v,                \tag{34.4}
\]
and \(C_uR_v\) is analogous. Neither is contained in the pure axial residues.

Finally,
\[
\begin{aligned}
 C_uC_v(\Theta,Q)
 &=\iint_{\mathcal R_u\times\mathcal R_v}
 \partial_\mu\partial_\nu\Theta\,Q\,dA_u\,dA_v\\
 &=\frac14\iint_{\mathcal R_u\times\mathcal R_v}
 \psi''(\beta)Q\,dA_u\,dA_v.                                             \tag{34.5}
\end{aligned}
\]
The sign is positive: the second transfer differentiates the first weight
\(-\partial_\nu\Theta\), adding a second minus. Under the hypotheses,
restrictions commute with restrictions, residues commute at a normal crossing, differentiation commutes with restriction and residue, and
\(\partial_\mu\partial_\nu\Theta=\partial_\nu\partial_\mu\Theta\).
Consequently every term in the \(v\)-then-\(u\) expansion matches the corresponding term in the \(u\)-then-\(v\) expansion.

In the final-negative-contour convention, the corner is
\[
 R_uR_v=(2\pi i)^2\psi(t)
 \operatorname{Res}_{u=0}\operatorname{Res}_{v=0}Q                       \tag{34.6}
\]
and occurs once positively. If instead both “full axes” already include their intersection, their union is
\(R_u^{\rm full}+R_v^{\rm full}-R_{uv}\). One must not combine this inclusion--exclusion convention with the additional positive term (34.6).

Changing variables to \((A,v)\), \(A=s-(u+v)/2\), does not remove any term. The rectangular \((u,v)\) product becomes a sheared domain: the faces
\(\mu=\pm U\) become \(\Im A=t-(\pm U+\nu)/2\), and similarly for
\(\nu=\pm V\). Replacing these slanted faces by an independent rectangular \(A,v\) cutoff changes the operator by exactly the omitted face/connector traces.

For the full finite vector identity, (34.2) acts linearly and separately on the terminal, radial horizontal sides, and arithmetic residue. Hence the exact finite survivor after an attempted premature module deletion is
\[
 \Delta_{\rm mod}
 =\mathsf X_u\mathsf X_v\,\mathfrak B^{\rm rad}_{M;U,V,S}
  +\mathsf X_u\mathsf X_v\,\mathfrak R^{\rm ar,fin}_{1;U,V},              \tag{34.7}
\]
minus only finite representatives actually removed by an exact identity. A theorem about the unshifted physical limit of either summand does not make (34.7) zero.

## 4. First doubtful or unproved step

The first unproved step is the existence of the claimed **actual finite post-module kernel** with the same value under (i) finite two-axis transfer and then physical/nested exhaustion and (ii) physical endpoint/arithmetic and radial-side removal followed by two-axis transfer. The accepted endpoint and \(R_1\)-arithmetic modules are not uniform arbitrary-finite-height statements, and the side theorem controls a declared nested limit of the unshifted renormalized side. No authorized artifact controls every face, residue, and \(\psi'/\psi''\) derivative in (34.7) under that exhaustion.

There is a second conditional seam. The axis-only proof assumes normal crossings. If the artificial rho divisor or an arithmetic divisor enters a shift rectangle, \(R_j\) must include it. At coincidence with an axis or with the arithmetic pole, one must take the single higher/derivative residue of the combined meromorphic kernel. Deleting the cancelling \(E_1\) artificial-pole share before taking these collision residues can make iterated residues order-dependent. The permitted context does not specify an actual post-collapse \(Q\) and pole-separation margin sufficient to exclude every such collision.

## 5. Control tests and outcomes

- **One-axis orientation and area sign:** pass. Each face is upper minus lower; each beta connector is \(+\psi'/2\).
- **Mixed derivative sign:** pass. Two connector minuses give \(+\partial_{\mu\nu}\Theta=+\psi''/4\).
- **Connector axes and boundaries:** pass only for the full sixteen-term formula; omitting any of \(C_uF_v,F_uC_v,C_uR_v,R_uC_v\) changes the operator.
- **Corner convention:** pass under either fixed convention; mixing them double-counts or deletes (34.6).
- **Shift-order commutation:** pass for a fixed finite product with normal crossings and common regularization; not proved across the physical/nested limits.
- **Actual factor/residue ownership:** open. Terminal, side, and arithmetic strata must each receive (34.2); artificial/axial collisions require combined residues.
- **Endpoint-first normalization:** global unmasked endpoint collapse is exact, but the estimates are physical-limit statements. Finite endpoint coefficients have full weight; stars arise only at licensed symmetric inversion. All profiles, floors, \(\chi_4(q)\), and the common factor
\(-4X^{1/4}\Re(e(1/8)\,\cdot)/\pi\) remain unchanged.

## 6. Dependencies and exact artifacts used

Used only protocol.md, state/proof_obligations.yml, state/active_campaign.yml, the permitted Round-19 finite-vector report, Round-22 endpoint synthesis, Round-33 hostile report, conductor connector ledger, and Round-33 synthesis. No Round-34 claimant report, numerical experiment, or external source was used.

## 7. Recommended state effect

**Promote only the abstract finite product-Stokes lemma (34.2)--(34.6); retain the actual obligation open.** Require an explicit common finite post-endpoint integrand and pole-separation/collision ledger. Then prove that every term of (34.7), including connector faces and derivatives, is compatible with the accepted physical profile and nested side limits. Until that is done, the unique vector share removed before local polar subtraction is defined only on the full finite vector ledger, not on a side-removed physical complement. No symbol or size estimate follows.
