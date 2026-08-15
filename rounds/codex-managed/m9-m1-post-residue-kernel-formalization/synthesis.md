# Round 18 synthesis: the scalar profile is bounded, but the reflected remainder is vector-valued

Campaign: `m9-m1-post-residue-kernel-formalization`  
Round type: post-residue kernel formalization  
Graph SHA-256 before patch: `e581befbc6c1648e50ab0382a0a9478d84629786d37613d0a63f1b1acdad0746`

## Conductor decision

Promote the exact pre-functional-equation scalar profile kernel and its
uniform (O(\log X)) pointwise bound. Reject the Round-16 schematic
post-reflection scalar kernel as presently ill-formed: the non-residue
functional-equation term retains a coupled radial Hankel/gamma operator and
an extra dual index. Consequently the Round-17 high-(2)-adic tail remains
conditional and cannot yet be removed from the full reflected maximal
problem.

The three independent reports agree on this scope. The interrupted analytic
task had already written a complete seven-section report reaching the same
verdict, so it is retained as evidence. No numerical experiment or external
theorem was used.

## Exact direct scalar kernel

Let (D_j=2^{-j}\lfloor\sqrt X\rfloor),
(H_j=\lfloor D_jX^{-1/4}\rfloor),

\[
 d_{h,q}=2\sqrt X\sqrt{h/q},\qquad
 A_j(h,q)=D_j/d_{h,q},
\]

and (phi(t)=\Phi(t)\mathbf1_{0<t<1}). For the top scale truncate the
spatial line symmetrically at height (T); all height and interior spatial
lines are complete. The exact direct profile is

\[
 \begin{aligned}
 \mathcal H^{\rm prof}_{T,X}(h,q)
 ={}&\phi\!\left(\frac h{H_0+1}\right)
 \frac1{2\pi i}\int_{a-iT}^{a+iT}
 \widehat W_+(u)A_0(h,q)^u\,du\\
 &+\sum_{j=1}^J
 \phi\!\left(\frac h{H_j+1}\right)
 W\!\left(\frac{d_{h,q}}{D_j}\right).
 \end{aligned}
\]

Here

\[
 \widehat W_+(u)=\frac1u+R_W(u),\qquad
 R_W(u)=-\frac1u\int_0^1W'(t)t^u\,dt.
\]

The height inversion is absolutely convergent on (Re v=b>0) and returns
the displayed bounded (phi)-factor with the exact floor and no height
half-weight. Interior spatial inversion is ordinary Mellin inversion.

For the top sharp piece,

\[
 Q_{a,T}(A)=\frac1{2\pi i}\int_{a-iT}^{a+iT}\frac{A^u}{u}\,du
\]

is uniformly bounded under symmetric truncation by the sine-integral/
Dirichlet argument. Its limit is (1,1/2,0) for (A>1,A=1,A<1).
The rapid remainder (R_W) has uniform vertical (L^1)-norm. Every scale
therefore contributes (O_W(1)), endpoint stars have magnitude at most one,
and there are (O(\log X)) active scales. Thus

\[
 \boxed{\sup_{T,h,q}|\mathcal H^{\rm prof}_{T,X}(h,q)|
 \ll_W\log(2X).}
\]

This proof never takes (int|du/u|) and is uniform at the hard endpoint.
It also passes through the exact matching profile projection of Round 17.

## Post-reflection obstruction

The finite-height radial functional equation transforms the radial factor
as

\[
 G_v(s)F_{u+v}(s)
 \longmapsto
 G_v(1-s)K_{u+v}(1-s)F_{-(u+v)}(s),
\]

besides the zeta, height, hard-top Perron, and any radial endpoint residues.
After expanding the reflected Dirichlet series, the non-residue term is

\[
 \sum_m a_{-(u+v)}(m)
 \frac1{2\pi i}\int
 G_v(1-s)K_{u+v}(1-s)m^{-s}\,ds,
\]

with finite horizontal sides retained. The quotient (K_{u+v}) couples
the radial height to both outside Mellin heights, while (G_v) contains the
finite radial cutoff and square-root wave. Its inverse is a Hankel kernel in
a new dual radial index (m), not a bounded scalar multiplier of an
original incidence ((h,q)).

No accepted result provides a uniform triple-height (L^1) estimate,
removes the finite horizontal sides, or produces an algebraic
(delta_{m=hq}). Indeed Round 15 explicitly withheld uniform
large-(|\Im z|) Hankel localization. Subtracting residues does not change
this vector structure; the zeta residue itself is global in the radial
variable.

Therefore the schematic post-FE expression

\[
 \sum_{hq}\chi_4(q)(hq)^{-3/4}e(\sqrt{Xhq})
 \mathcal H_{T,X}(h,q)
\]

cannot be treated as a termwise scalar kernel on the current graph. The
correct survivor is a vector kernel
(mathcal K_{T,X}(h,q;m)), or equivalently the original finite
three-contour operator, with all residues outside it.

## Effect on the high-(2)-adic tail

The divisor calculation remains correct: any scalar kernel with pointwise
bound (B_X) gives

\[
 |\text{tail}_{v_2(n)\ge K}|
 \ll B_XN_X^{1/4}2^{-K}\log(2N_X).
\]

For (mathcal H^{\rm prof}), this is an unconditional direct-profile
tail estimate. It does not imply the analogous bound for the full
post-reflection vector remainder. The latter remains conditional on a new
uniform vector-valued Hankel/horizontal-side theorem.

## State effect

- promote the direct scalar profile kernel and its (O(\log X)) bound;
- promote the scalar-separation obstruction for the post-FE remainder;
- replace the schematic post-FE scalar target by a vector-kernel or
  three-contour formulation;
- retain the full high-(2)-adic tail as conditional;
- leave GAR, M9-M1, M9-M2, M9, and the target open.

