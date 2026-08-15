# Round 52 derivation packet: the Vaaler height floor

This packet freezes the first actual object named but not typed in Round 51.
It asks whether the floor (H_j=lfloor D_jX^{-1/4}\rfloor) is a moving
alpha-contour seam at all, and what its lawful discrete replacement is.

## 1. Exact coefficient family

For an integer (H\geq1), put

\[
 a_H(h)=\mathbf 1_{1\leq h\leq H}\Phi\!\left(\frac h{H+1}\right),
 \qquad
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u.
\]

The positive-frequency Vaaler coefficient is

\[
 \alpha_{h,H}=\frac{i}{2\pi h}a_H(h).
\]

In the actual physical angular coefficient,

\[
 \Omega_X^*(n,h)=\sum_j a_{H_j}(h)
 \left[w_j\!\left(2h\sqrt{X/n}\right)\right]^*,
 \qquad H_j=\lfloor D_jX^{-1/4}\rfloor.
\]

The Mellin antecedent contains the fixed parameter factor

\[
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v.
\]

Here (X,D_j,H_j) are fixed while the contour heights
(\mu,\nu,\alpha,\beta) vary.

## 2. Frozen questions

1. Prove or refute that (H_j) has zero contour velocity and therefore
   produces no moving-face delta in the finite alpha Cauchy--Green ledger.
2. Derive the exact adjacent-height difference

   \[
   \Delta_Ha(h)=a_{H+1}(h)-a_H(h)
   \]

   including (h=H+1), and obtain sharp uniform bounds for its
   (\ell^1_h), weighted (\ell^1_h/h), and relevant power-weighted norms.
3. Decide whether the Vaaler taper makes one unit floor change an
   (O(1)), logarithmic, or (H)-sized perturbation, and whether that fact
   can reduce the alpha lattice jump capacity.
4. Determine the only lawful global parameter along which (H_j) changes
   (for example (X), a continuous scale parameter, or an adjacent
   discrete height), and retain every simultaneous change of (D_j),
   (w_j), support, stars, and external normalization.

## 3. Mandatory controls

- Do not differentiate the integer floor with respect to contour heights.
- Do not replace an actual dyadic-scale change by (H\mapsto H+1) unless
  the denominator profile and scale change are separately accounted for.
- Use the exact endpoint limits (\Phi(0^+)=1), (\Phi(1^-)=0) and the
  identity (\Phi(u)+\Phi(1-u)=1); do not use the false symmetry
  (\Phi(1-u)=\Phi(u)).
- Keep the equality star distinct from the coefficient cutoff.
- A local discrete-variation bound does not by itself prove the projected
  alpha trace or its outside-height limit.

## 4. Completion rule

A successful result either proves a typed discrete-height lemma with all
actual dependencies stated, or gives a rigorous no-go showing that the
floor cannot be the missing alpha seam. No numerical experiment or
external theorem is needed.
