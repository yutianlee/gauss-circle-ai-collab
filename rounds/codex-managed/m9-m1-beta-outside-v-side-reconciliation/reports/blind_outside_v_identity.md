# Round 29 blind report: oriented outside-v identity and logarithmic ledger

Task: blind_outside_v_identity  
Role: statement-only blind rederivation  
Allocation: 100% analytical/algebraic; no computation and no external theorem

## 1. Result: exact identity and sign-sensitive verdict

The exact finite \(v\)-rectangle identity can be derived without taking a
PV limit. Its orientation is
\[
 {\cal V}_b={\cal V}_\ell+{\cal S}_+-{\cal S}_-
             +2\pi i\,\operatorname {Res}_{v=0},               \tag{29.1}
\]
where both horizontal sides are parametrized left-to-right,
\(\ell<0<b\), and the right and left verticals are parametrized upward.
For \(a>0\), the moving \(u=0\) pole lies just to the right of the right
\(v\)-vertical and is not an interior residue.

The logarithmic coefficients match (29.1) exactly. At the upper collision
\(L=V\), the right vertical and the upper side both have coefficient
\(+H_+\log(1/a)\) in the unnormalized \(dv\) integral. At the lower
collision \(L=-V\), the right vertical and the signed term
\(-{\cal S}_-\) both have coefficient
\(-H_-\log(1/a)\). The axial, top, and corner residues have zero
\(\log(1/a)\) coefficient at fixed \(V>0\).

Consequently, the outside sides do not automatically cancel the
finite-height logarithm in the usual shifted representation on the
right-hand side of (29.1); they carry exactly the logarithm needed to make
that representation equal to the original vertical. Cancellation occurs
only in the oppositely signed closed-boundary combination
\[
 {\cal V}_b-{\cal S}_+ +{\cal S}_-
 ={\cal V}_\ell+2\pi i\,\operatorname {Res}_{v=0}.              \tag{29.2}
\]
Thus a project-level cancellation requires proof that the actual operator
contains (29.2), or an additional term with those signs. Merely “retaining
the outside sides” as \(+{\cal S}_+-{\cal S}_-\) transfers the logarithm
to a side; it does not remove it.

At fixed finite heights, (29.2) has ordinary \(C^2\) dependence on \(L\)
under holomorphy and bounded-derivative hypotheses. Nothing in the
permitted statements makes those bounds uniform under nested exhaustion
or supplies the scaled \(C^2\) bounds required by the Fresnel lemma.

## 2. Exact statement and hypotheses

### 2.1 Meromorphic slice and omega recombination

Let
\[
 z=a+b+iL,\qquad a>0,\quad b>0,\quad L\in\mathbb R,
\]
and write \(u=z-v\). Factor the two physical axial poles from the finite
kernel as
\[
 {\cal F}(u,v)={{\cal M}(u,v)\over uv}.                         \tag{29.3}
\]
Here \({\cal M}\) contains every scale, arithmetic, gamma, profile, and
radial factor other than the displayed \(1/u\) and \(1/v\). In particular
its radial factor is the complete expression
\[
 {\cal R}_\omega
 =\omega G+(1-\omega)R_1-\omega E_1,                           \tag{29.4}
\]
not any one summand of (29.4). Assume \({\cal M}\) is holomorphic on a
neighborhood of the finite rectangle used below; any additional known
poles would have to be added explicitly to the residue sum.

On the diagonal slice define
\[
 F_z(v)={ {\cal M}(z-v,v)\over (z-v)v}.                         \tag{29.5}
\]
Choose \(\ell<0<b\), \(V>0\), and set
\[
 \begin{aligned}
 {\cal V}_b&=\int_{b-iV}^{b+iV}F_z(v)\,dv,&
 {\cal V}_\ell&=\int_{\ell-iV}^{\ell+iV}F_z(v)\,dv,\\
 {\cal S}_+&=\int_{\ell}^{b}F_z(\sigma+iV)\,d\sigma,&
 {\cal S}_-&=\int_{\ell}^{b}F_z(\sigma-iV)\,d\sigma .
                                                               \tag{29.6}
 \end{aligned}
\]
Both verticals point upward and both sides in (29.6) point
left-to-right.

Because \(\Re z=a+b>b\), the pole \(v=z\), equivalently \(u=0\), is
outside the rectangle. The only displayed pole inside is \(v=0\), with
\[
 \operatorname {Res}_{v=0}F_z(v)={{\cal M}(z,0)\over z}.        \tag{29.7}
\]
Under these hypotheses (29.1) and (29.2) are exact.

### 2.2 Relation to the truncated moving-pole integral

On \(v=b+i\nu\), put
\[
 H_b^{a,L}(\nu)
 ={ {\cal M}(a+i(L-\nu),\,b+i\nu)\over b+i\nu}.
\]
Then
\[
 {\cal V}_b=iC_{a,V}(L),\qquad
 C_{a,V}(L)=\int_{-V}^{V}
 {H_b^{a,L}(\nu)\over a+i(L-\nu)}\,d\nu .                       \tag{29.8}
\]
Define the shared endpoint numerators
\[
 H_+={{\cal M}(0,b+iV)\over b+iV},\qquad
 H_-={{\cal M}(0,b-iV)\over b-iV}.                              \tag{29.9}
\]
If \({\cal M}\) is \(C^1\) at the two right corners, the complete
logarithmic ledger is
\[
\begin{array}{c|cc}
\text{term} & L=V & L=-V\\ \hline
C_{a,V}(L) & -iH_+\log(1/a) & +iH_-\log(1/a)\\
{\cal V}_b=iC_{a,V} & +H_+\log(1/a) & -H_-\log(1/a)\\
{\cal S}_+ & +H_+\log(1/a) & 0\\
{\cal S}_- & 0 & +H_-\log(1/a)\\
{\cal V}_\ell & 0 & 0\\
\operatorname {Res}_{v=0} & 0 & 0\\
\operatorname {Res}_{u=0} & 0 & 0\\
\operatorname {Res}_{u=v=0} & 0 & 0 .
\end{array}                                                     \tag{29.10}
\]
The side coefficients in (29.10) use the left-to-right convention in
(29.6). Hence the retained side combination
\({\cal S}_+-{\cal S}_-\) has exactly the same edge coefficient as
\({\cal V}_b\), while the closed-boundary correction
\(-{\cal S}_++{\cal S}_-\) has the opposite coefficient.

### 2.3 Complete u/v axial and corner ledger

For clarity, use normalized contour operators. For either variable \(w\),
let \(R_w\) denote its right upward vertical, \(L_w\) its left upward
vertical,
\[
 S_w=H_w^+-H_w^-,
\]
with both \(H_w^\pm\) directed left-to-right, and let \(P_w\) be the
residue operator at \(w=0\). The one-variable formula is
\[
 R_w=L_w+S_w+P_w.                                               \tag{29.11}
\]
Applying it independently in \(u\) and \(v\) gives the exact
two-variable ledger
\[
\begin{split}
 R_uR_v{\cal F}
={}&(L_u+S_u)(L_v+S_v){\cal F}\\
 &+P_u(L_v+S_v){\cal F}
 +(L_u+S_u)P_v{\cal F}
 +P_uP_v{\cal F}.                                               \tag{29.12}
\end{split}
\]
For (29.3),
\[
 P_u{\cal F}={{\cal M}(0,v)\over v},\qquad
 P_v{\cal F}={{\cal M}(u,0)\over u},\qquad
 P_uP_v{\cal F}={\cal M}(0,0).                                 \tag{29.13}
\]
All three signs in (29.13) are positive in (29.12), and the joint corner
appears exactly once.

If the moving pole \(v=z\) is instead crossed as a pole of the
one-dimensional slice (29.5), then
\[
 \operatorname {Res}_{v=z}F_z(v)
 =-{{\cal M}(0,z)\over z}.                                     \tag{29.14}
\]
The minus sign is \(du=-dv\). Formula (29.14) is the slice version of the
\(u=0\) residue and must not be added a second time through \(P_u\).
For the geometry \(a>0\) in (29.1), it is outside and (29.14) is absent.

### 2.4 Finite-height derivative statement

Set
\[
 {\cal B}_{a,V}(L)={\cal V}_b-{\cal S}_++{\cal S}_-.
\]
By (29.2),
\[
 {\cal B}_{a,V}(L)
 ={\cal V}_\ell+2\pi i\,{{\cal M}(z,0)\over z}.                 \tag{29.15}
\]
On the left vertical,
\[
 \Re(z-v)=a+b-\ell\geq b-\ell>0,\qquad \Re z=a+b\geq b.
\]
Therefore, if derivatives of \({\cal M}\) through order two are bounded
on the finite contours, (29.15) is \(C^2\) in \(L\), uniformly for
\(a\geq0\) at fixed \(b,\ell,V\). A direct differentiation gives a bound
of the form
\[
 \max_{0\leq k\leq2}|\partial_L^k{\cal B}_{a,V}(L)|
 \leq C_{b-\ell,b,V}
 \max_{r+s\leq2}\|\partial_u^r\partial_v^s{\cal M}\|_\infty.    \tag{29.16}
\]
This is only a finite-contour bound. Its constant may grow with \(V\),
\(b^{-1}\), the other contour heights, and the derivatives hidden in
\({\cal M}\).

## 3. Proof or derivation

Traverse the rectangle counterclockwise. Its boundary is the lower side
left-to-right, the right vertical upward, the upper side right-to-left,
and the left vertical downward. Cauchy's theorem gives
\[
 {\cal S}_-+{\cal V}_b-{\cal S}_+-{\cal V}_\ell
 =2\pi i\sum\operatorname {Res}.
\]
Rearranging proves (29.1). Equation (29.7) follows immediately from
(29.5). The moving pole is outside because its real part is \(a+b>b\).

At \(L=V\), set \(v=\sigma+iV\) on the upper side and
\(x=b-\sigma\). Near the right corner,
\[
 z-v=a+x,\qquad
 {\cal S}_+
 =H_+\int_0^{b-\ell}{dx\over a+x}+O(1)
 =H_+\log(1/a)+O(1).                                           \tag{29.17}
\]
The same calculation gives
\({\cal S}_-=H_-\log(1/a)+O(1)\) at \(L=-V\).

For the right vertical, (29.8) and the local substitutions
\(y=V-\nu\) at the upper endpoint and \(y=\nu+V\) at the lower endpoint
give
\[
 C_{a,V}(V)=-iH_+\log(1/a)+O(1),
\]
\[
 C_{a,V}(-V)=+iH_-\log(1/a)+O(1).                              \tag{29.18}
\]
Multiplication by \(i\) proves the vertical row of (29.10). Equations
(29.17)-(29.18) show both the matching in (29.1) and the cancellation in
(29.2), including every sign.

Equation (29.12) is the product of the two exact identities (29.11).
It is also an inclusion-exclusion proof that the joint corner occurs once,
not twice. Equation (29.14) follows from
\((z-v)^{-1}=-(v-z)^{-1}\). Finally, differentiating the right side of
(29.15) proves (29.16), since both displayed real-part gaps are positive.

## 4. First doubtful or unproved step

The first project-specific gap is identifying which oriented combination
is actually present after every contour displacement. The standard shift
identity retains \(+{\cal S}_+-{\cal S}_-\) on the same side as the new
left vertical. That combination reproduces the logarithm. The cancelling
combination (29.2) uses the opposite side signs. No permitted artifact
supplies an additional operator with those opposite signs.

Even if the proof architecture does contain (29.2), the next unproved
step is upgrading the finite bound (29.16) to the scaled Fresnel estimate
uniformly in \(q,h,D_j,x,U,V,S\) and \(b\). The omega identity (29.4)
ensures exact artificial-pole bookkeeping, but it supplies no derivative
or exhaustion estimate.

## 5. Control tests and outcomes

### Support-and-degeneracy

**Scoped pass.** The proof assumes \(\ell<0<b\), \(V>0\), \(a>0\), and
that the moving pole \(v=z\) stays to the right until the limit is taken.
The cases \(V=0\), an endpoint coinciding with \(v=0\), or an unlisted pole
inside the rectangle are excluded and require a separate indentation
ledger.

### Residue-and-normalization

**Pass.** The upper-minus-lower orientation is derived from the
counterclockwise boundary. The \(v=0\) and \(u=0\) residues have positive
signs in the independent two-variable shift, the slice \(v=z\) residue
has the required minus sign, and the corner occurs once. All residue
values use the recombined radial factor (29.4).

### Endpoint-uniformity

**Conditional pass for (29.2), fail for the retained-side
representation.** The logarithms cancel coefficient-by-coefficient in
(29.2), yielding finite \(C^2\) dependence at fixed contours. They remain
in \({\cal V}_\ell+{\cal S}_+-{\cal S}_-+\operatorname {Res}\), which is
the usual representation of \({\cal V}_b\). No scaled or exhausted
endpoint bound follows.

### Order of limits

**Open, with an exact warning.** Identity (29.1) must first be used for
\(a>0\). At \(L=\pm V\), neither the right vertical nor the colliding side
has a termwise \(a\downarrow0\) limit. One may take that limit only after
forming (29.2), or after proving a quantitative nested limit such as
\[
 |H_\pm(V)|\log(1/a)\longrightarrow0
\]
together with corresponding derivative bounds. Taking \(V\to\infty\)
first works pointwise for fixed \(L\) only after decay is proved; it is not
uniform in the moving \(L\), because \(L=\pm V\) remains admissible.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read or used:

1. protocol.md;
2. state/active_campaign.yml;
3. rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md;
4. rounds/codex-managed/m9-m1-beta-uniform-stationary-patching/synthesis.md.

No proof graph, proof draft, other Round-29 report, computation, or web
source was read or used.

## 7. Recommended state effect

- **Promote as exact finite algebra:** (29.1), the log coefficient ledger
  (29.10), the two-axis/corner identity (29.12), and the moving-pole sign
  (29.14), all with the stated contour hypotheses.
- **Promote only conditionally:** finite-\(V\) \(C^2\) regularity of the
  closed-boundary combination (29.2), assuming bounded derivatives of the
  complete recombined numerator.
- **Reject as stated:** the assertion that retaining the outside sides
  with their standard \(+{\cal S}_+-{\cal S}_-\) signs cancels the
  moving-edge logarithm. It transfers the same logarithm to the side.
- **Retain open:** whether another accepted ledger term supplies the
  opposite side combination, the nested order of limits, scaled \(C^2\)
  bounds, complete beta summation, M9-M1, M9, and the final target.
