## 1. Result

**No-go for the claimed global limit from the accepted inputs; narrow finite-box distributional certification only.** The fixed-\(w\) complement
\[
 \mathfrak V_{\rm ef}^{\rm fin}
 =\mathfrak V_{\rm pre}^{\rm fin}-\mathfrak M_{\rm fin}                  \tag{37.1}
\]
is an exact and unique finite algebraic object when both terms use the same meromorphic antecedent, rectangles, collision convention, and corner convention. The compact beta mask also removes the radial \(w\)-sides exactly. Neither fact proves convergence of the remaining ordinary \(u,v\) faces and tails.

At fixed \(U,V\), on a collision-separated patch, the hard-top limit is lawfully the signed
\(\pi\delta-i\,\mathrm{PV}\) distribution and its moving faces are locally logarithmic. The authorized evidence supplies no Cauchy estimate as
\(U,V\to\infty\), no uniform Plemelj theorem for faces that move with the saddle, and no declared interchange with the physical profile limit. A bounded smooth counterfunctional below has every finite-box Plemelj limit but no symmetric outside-height limit. It does not falsify the actual profile; it falsifies any inference based only on finite Stokes, local smoothness, and signed Plemelj. The actual-profile remainder limit therefore remains open.

## 2. Exact statement and hypotheses

At fixed positive outside abscissae and finite \(U,V,S\), define (37.1) before any change \(r=w-3/4-v/2\), physical sharp support, or starred Perron limit. Subtract
\[
 \mathfrak M_{\rm fin}
 =\left[\sum_{\xi\in\{1,N_X\}}D_{\xi;U,V,S}
 +\mathfrak R^{\rm ar}_{U,V}[R_1]\right]_{\rm common}                    \tag{37.2}
\]
from the same fixed-\(w\) representative of
\(\mathfrak V_{\rm pre}^{\rm fin}\). Artificial/arithmetic/axial collisions are extracted from the common germ, and the sequential convention includes the joint \(u=v=0\) corner once.

After beta localization, write \(L_j\) for the final \(j\)-vertical,
\(F_j=H_{j,+}-H_{j,-}\) for the outside horizontal difference,
\(R_j\) for the axial residue, and \(C_j\) for the mask-area connector.
After (37.2) and the radial-side support lemma, the complete finite inventory is:

\[
\begin{array}{ll}
\text{pure boundary:}&
L_uL_v,\ F_uL_v,\ L_uF_v,\ F_uF_v,\\
\text{axis/boundary/corner:}&
R_uL_v,\ L_uR_v,\ R_uF_v,\ F_uR_v,\ R_uR_v,\\
\text{connector boundary:}&
C_uL_v,\ L_uC_v,\ C_uF_v,\ F_uC_v,\\
\text{connector axis:}&C_uR_v,\ R_uC_v,\\
\text{mixed area:}&C_uC_v\quad(\psi''(\beta)/4).
\end{array}                                                              \tag{37.3}
\]

No endpoint prefix, \(R_1\)-arithmetic module, radial \(w\)-side, or duplicate artificial residue belongs to (37.3). A global limiting theorem would have to prove that the complete sum (37.3), not each absolute term, is Cauchy under one explicitly stated symmetric/profile exhaustion.

## 3. Proof or derivation

### Finite ownership

Round 36 routes (37.2) only after summing all three masks. Hence subtracting a beta-masked endpoint share or a physical starred formula from
\(\mathfrak V_{\rm pre}^{\rm fin}\) is not equivalent to (37.1). In particular, the off-centred finite Perron path has moving real part and endpoints; any Perron tail left after the common fixed-\(w\) subtraction is a representation mismatch, not a new endpoint-free term.

Compact beta support kills only the radial \(w\)-sides. It does not kill an outside \(u\)-face \(\mu=\pm U\) or \(v\)-face \(\nu=\pm V\): one may still choose
\[
 t=\frac{\mu+\nu}{2}+O(1)
\]
so that \(\beta=t-(\mu+\nu)/2\) lies in the mask support, and the terminal \(t\)-range grows with \(U+V\). Thus every ordinary face in (37.3) remains.

### Narrow Plemelj limit

At fixed \(U,V\), pair in the physical top variable
\(\mu=L-\nu\). For a smooth numerator \(F(\mu,\nu)\),
\[
\begin{aligned}
\mathcal T_{U,V}(F)
={}&\pi\int_{-V}^{V}F(0,\nu)\,d\nu\\
&-i\int_{-V}^{V}\operatorname{PV}
\int_{-U}^{U}\frac{F(\mu,\nu)}{\mu}\,d\mu\,d\nu .                         \tag{37.4}
\end{aligned}
\]
This is the limit of the positive top line
\((a+i\mu)^{-1}\), \(a\downarrow0\). Pointwise at \(L=\pm V\), the same section has a \(\log(1/a)\) edge, but (37.4) is finite against fixed test functions. In the transferred ledger, the negative top line plus the full crossed \(u=0\) residue equals (37.4); one must not add the delta in (37.4) once more to the explicit full residue. The same convention fixes the joint corner.

### Counterfunctional to height exhaustion

Choose \(\chi\in C_c^\infty(\mathbb R)\) with
\(c_\chi=\int\chi\ne0\), and set
\[
\begin{aligned}
g(\mu)&=\frac{\mu}{\sqrt{1+\mu^2}}
\sin\!\left(\frac12\log(1+\mu^2)\right),\\
F(\mu,\nu)&=\chi(\mu+\nu)g(\mu).                                         \tag{37.5}
\end{aligned}
\]
This is a bounded smooth numerator and \(F(0,\nu)=0\). Every finite-box top limit (37.4) exists, but for \(U=V=R\),
\[
\mathcal T_{R,R}(F)
=-i\int\chi(L)
\int_{\substack{|\mu|\le R\\|L-\mu|\le R}}
\frac{\sin(\frac12\log(1+\mu^2))}
{\sqrt{1+\mu^2}}\,d\mu\,dL.                                              \tag{37.6}
\]
For \(L\) in the fixed support of \(\chi\), the endpoint displacement from
\([-R,R]\) contributes \(o(1)\). With \(\mu=\sinh y\),
\[
\int_{-R}^{R}
\frac{\sin(\frac12\log(1+\mu^2))}
{\sqrt{1+\mu^2}}\,d\mu
=2\int_0^{\operatorname{arsinh}R}\sin(\log\cosh y)\,dy.                   \tag{37.7}
\]
Since \(\log\cosh y=y-\log2+O(e^{-2y})\), (37.7) equals a constant minus
\(2\cos(\operatorname{arsinh}R-\log2)+o(1)\). It has distinct subsequential limits. Hence \(\mathcal T_{R,R}(F)\) has no limit.

The counterfunctional is not asserted to equal the project numerator. It proves that finite Plemelj, local logarithmic integrability, bounded smooth numerators, exact side orientations, and symmetric boxes do not imply outside-height convergence. To rule it out for the actual kernel one needs a uniform tail or cancellation theorem in all \(q,h,D_j,x,b\), precisely the datum absent from the authorized evidence.

Moving faces create the same uniformity gap. The finite logarithmic theorem controls a face that meets a saddle only under a scale-normalized BV hypothesis for the complete numerator. That hypothesis and the outside-height tail are explicitly unproved. A fixed compact test in \(L\) does not test the physical situation in which the saddle and the face both escape.

## 4. First doubtful or unproved step

The first unproved step is the Cauchy property of the **complete** outside-height package:
\[
\mathcal E_{U_1,V_1}^{U_2,V_2}
=\mathcal A_{\beta}^{\rm fin}(U_2,V_2,S_2)
 -\mathcal A_{\beta}^{\rm fin}(U_1,V_1,S_1),                             \tag{37.8}
\]
after the fixed-box Plemelj pairing and with \(S_k\) on the accepted nested radial exhaustion. No accepted estimate makes (37.8) tend to zero. Finite Stokes only rewrites (37.8); the \(v\)-horizontals are boundary connectors, not the omitted \(|\nu|>V\) tails, and they reproduce rather than cancel the moving logarithmic edge pointwise.

The exhaustion itself is not sufficiently frozen to repair this: the evidence does not justify interchanging the top Plemelj limit, \(U,V\to\infty\), the \(b\downarrow0\) height-profile limit, character/scale summation, and the nested \(S\)-limit. Local distributional convergence at fixed \(U,V\) gives no uniformity when \(L=\pm V\) tracks an unbounded saddle.

## 5. Control tests and outcomes

- **Fixed-\(w\) complement:** pass only for (37.1)--(37.2) on a common finite antecedent. A frozen moving-\(r\) path fails.
- **Post-module inventory:** pass for the sixteen groups (37.3); ordinary \(u,v\) faces remain.
- **Boundary double count:** pass only if the global module is subtracted once before beta localization. No finite Perron tail or physical endpoint star may be reinserted.
- **Signed Plemelj/moving faces:** fixed-box distribution passes by (37.4); pointwise face uniformity fails, and moving-saddle uniformity is open.
- **Outside-height limit:** fail. The exact counterfunctional (37.5)--(37.7) shows the available hypotheses do not imply existence or uniqueness.
- **Collisions and corner:** conditional pass at finite height under the common combined-residue and one-corner convention. In the limit, delta/full-residue conventions must not be mixed.
- **Profiles and normalization:** all \(W_j,\phi,D_j,H_j+1\), floors, \(\chi_4(q)\), and the factor
\(-4X^{1/4}\Re(e(1/8)\,\cdot)/\pi\) must remain. Multiplying (37.8) by this factor does not create convergence. Stars arise only after a licensed physical inversion.
- **No symbol overreach:** pass. No \(\lambda^{-2}\), \(\lambda^{-3}\), stationary, or target-size estimate is claimed.

## 6. Dependencies and exact artifacts used

Used only protocol.md, state/proof_obligations.yml, state/active_campaign.yml, the permitted Round-29 and Round-30 hostile audits, Round-34 and Round-35 hostile audits, and the Round-36 hostile audit and synthesis. No Round-37 claimant report, numerical experiment, or external source was used.

## 7. Recommended state effect

**Retain the endpoint-free axial remainder limit open.** Promote only the finite fixed-\(w\) complement/inventory and the collision-separated fixed-box Plemelj limit, both already compatible with the accepted graph. Reject any claim that boundary-module removal, radial-side support separation, or local logarithmic integrability automatically yields the \(U,V\) exhaustion.

The smallest next lemma is a complete actual-profile Cauchy tail theorem for (37.8), uniform through moving logarithmic faces and the physical profile net, with the signed vertical/face/axis/connector package kept intact. Alternatively, define a weaker local distribution on a fixed compact \(L\)-test space; such a local object would not yet be the physical endpoint-free axial vector required downstream.
