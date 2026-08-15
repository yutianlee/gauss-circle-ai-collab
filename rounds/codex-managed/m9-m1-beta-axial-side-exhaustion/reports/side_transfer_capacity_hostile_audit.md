## 1. Result

**Scoped exact certification, stronger than an arbitrary-order decay estimate.** If the accepted beta transition cutoff is compactly supported, say
\(\operatorname{supp}\psi\subset[-B,B]\), then on either renormalized radial side every one of the sixteen grouped two-axis transfer strata is identically zero as soon as

\[
 S-\frac{U+V}{2}>B.                                                       \tag{35.1}
\]

This holds before estimating \(R_{M,v}\), gamma quotients, profiles, or integration volumes. Consequently the weakest endpoint-subtraction order is \(M=1\), and one explicit legal nesting is

\[
 S(X,U,V)=(1+X+U+V)^2+B+1.                                               \tag{35.2}
\]

It follows that the beta-masked two-axis transfer commutes with removal of the renormalized radial sides under this support-separated nesting. This result is conditional on compact support being part of the frozen definition of \(\psi\). If \(\psi\) is merely decaying and noncompact, the permitted artifacts do not supply enough derivative/residue uniformity to certify the requested conclusion.

## 2. Exact statement and hypotheses

Let \(w=\sigma\pm iS\) be a radial horizontal side and put \(s=1-w\). Hence
\[
 t=\Im s=\mp S.
\]
Let the finite transfer rectangles satisfy \(|\mu|\le U\), \(|\nu|\le V\), and set
\[
 \Theta_\beta=\psi(\beta),\qquad
 \beta=t-\frac{\mu+\nu}{2}.
\]
Assume:

1. \(\psi\in C_c^2(\mathbb R)\) and
   \(\operatorname{supp}\psi\cup\operatorname{supp}\psi'
   \cup\operatorname{supp}\psi''\subset[-B,B]\);
2. the same finite product rectangles and common combined-residue convention are used on the upper and lower sides;
3. \(G_v=E_{M,v}+R_{M,v}\) is the exact common meromorphic split, with \(M\ge1\);
4. all actual profiles, floors, stars, \(\chi_4\), and external normalization are carried unchanged.

Then the full transfer of the upper-minus-lower \(R_M\) side is zero for every finite \(X,U,V,S\) satisfying (35.1). No physical endpoint or arithmetic limit is asserted.

## 3. Proof or derivation

On both radial sides,
\[
 |\beta|
 =\left|\,\mp S-\frac{\mu+\nu}{2}\right|
 \ge S-\frac{U+V}{2}>B.                                                  \tag{35.3}
\]
Therefore throughout the closed product of the two transfer rectangles,
\[
 \Theta_\beta=\psi'(\beta)=\psi''(\beta)=0.                              \tag{35.4}
\]
The strict inequality supplies an open neighborhood, so (35.4) remains valid when an axial or collision residue is extracted; this is not an indeterminate zero times a pole.

Use the accepted grouped alphabet
\[
 (L_u,F_u,R_u,C_u)(L_v,F_v,R_v,C_v),
\]
where \(L\) is the final vertical, \(F=H_+-H_-\), \(R\) is the axis residue, and \(C\) is the mask-area connector. The complete power table is:

| Strata | Number | Mask coefficient | \(S\)-capacity | \(U,V\)-cost |
|---|---:|---|---|---|
| \(L_uL_v,L_uF_v,F_uL_v,F_uF_v\) | 4 | \(\psi(\beta)\) | \(0\) exactly | \(0\) |
| \(R_uL_v,L_uR_v,R_uF_v,F_uR_v,R_uR_v\) | 5 | restricted \(\psi(\beta)\) | \(0\) exactly | \(0\) |
| \(C_uL_v,L_uC_v,C_uF_v,F_uC_v\) | 4 | \(\psi'(\beta)/2\) | \(0\) exactly | \(0\) |
| \(C_uR_v,R_uC_v\) | 2 | restricted \(\psi'(\beta)/2\) | \(0\) exactly | \(0\) |
| \(C_uC_v\) | 1 | \(\psi''(\beta)/4\) | \(0\) exactly | \(0\) |

Expanding either \(F_j\) into its upper and lower horizontal faces changes no entry. In particular, no factor \(UV\), \(U+V\), or profile norm appears: localization kills the integrand before absolute integration. Upper-minus-lower radial orientation is retained, but both oriented pieces vanish separately.

The possible non-axial collisions are also excluded geometrically. An artificial pole of
\(R_{M,v}(1-s)\) requires
\[
 \Im(1-s-3/4-v/2+r/2)=-t-\nu/2=0,
\]
so \(|\nu|=2S>V\). The moving arithmetic pole requires
\(|\mu+\nu|=2S>U+V\). Thus neither divisor meets the side transfer product under (35.1); the pure \(u=0\), \(v=0\), and joint corner residues remain multiplied by the zero mask in (35.4).

Equation (35.2) is polynomial, satisfies (35.1), and is much larger than \(X+U+V\). It therefore also lies within the accepted nested radial-side regime. Since the transferred side is already zero at every sufficiently large finite stage,
\[
 \lim_{\rm nested}\mathsf X_{uv}\mathfrak S_{\rm rad}^{(M)}=0
 =\mathsf X_{uv}\lim_{\rm nested}\mathfrak S_{\rm rad}^{(M)}.             \tag{35.5}
\]
The common factor
\(-4X^{1/4}\Re(e(1/8)\,\cdot)/\pi\) preserves zero.

## 4. First doubtful or unproved step

The Round-35 brief does not itself state a support radius for \(\psi\). The proof graph describes the transition mask as compact and earlier Cauchy--Green use requires a support margin, but promotion should freeze \(B\) explicitly. If compact support is not intended, (35.4) is unavailable. Then the accepted Round-21 estimate controls only the unshifted side:
\[
 \mathfrak S(R_M)\ll_{X,M}(\log X)\log(2+U)S^{-M-2\lambda}.
\]
It gives no table of uniform \(u,v\) restrictions, connector areas, connector-axis residues, collision derivatives, or constants over shifted real abscissae. In that noncompact variant no explicit \(M\) and nesting law can be certified from the permitted context.

There is also a scope distinction: (35.5) applies only when the beta mask is present on the finite radial-side stratum before transfer. It does not license shifting an unmasked side first and localizing only afterward; Round 33 already shows those operations differ by connectors.

## 5. Control tests and outcomes

- **Arbitrary-\(M\) radial remainder decay:** superseded by exact support separation; \(M=1\) is sufficient and every \(M\ge1\) works.
- **Derivative and residue cost:** zero. The mask and its first two derivatives vanish in an open neighborhood of every allowed restriction/residue.
- **Sixteen-stratum table:** pass; the table above accounts for \(4+5+4+2+1=16\) grouped strata. Raw horizontal-face expansion is also zero termwise.
- **Nested exhaustion uniformity:** pass under (35.1); (35.2) is an explicit common polynomial law.
- **Collision and corner scope:** pass; artificial and arithmetic collision equations require heights outside the product, and the filtered corner is zero.
- **Actual profiles and normalization:** pass vacuously but exactly; no absolute profile estimate, floor simplification, star change, or character cancellation is used.
- **No physical-module overreach:** pass. Nothing here concerns the endpoint or \(R_1\)-arithmetic physical-profile commutator.

## 6. Dependencies and exact artifacts used

Used only protocol.md, state/proof_obligations.yml, state/active_campaign.yml, the permitted Round-21 endpoint-renormalization synthesis, Round-20 exhaustion attack, Round-34 hostile audit, and Round-34 synthesis. No Round-35 claimant report, numerical experiment, or external source was used.

## 7. Recommended state effect

**Promote the support-separated side-transfer lemma, after explicitly freezing compact support of \(\psi\), and close the radial-side commutator in that scope.** Record \(M=1\) and (35.2) as a valid common choice, while noting that arbitrary-order radial decay is not the mechanism. If compact support is not part of the actual mask definition, retain the obligation open and require uniform value, derivative, residue, and collision estimates for all sixteen strata. In either case, do not infer physical endpoint/arithmetic commutation or any terminal-symbol bound.
