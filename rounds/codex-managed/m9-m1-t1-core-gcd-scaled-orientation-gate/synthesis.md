# Round 193 synthesis

## Outcome

Round 193 proves a strict gcd-scaled double-close sector inside the exact
Round-192 hard-M1 \(t=1\) core.

On the opposing physical source, put

\[
 g=(d,d'),\qquad D_L=\lceil\sqrt L\rceil,
\qquad
 P_{\rm cl}=
 \mathbf1_{|d-gm|\le D_L}
 \mathbf1_{|d'-gm'|\le D_L}.
\]

The mask is imposed before Fourier expansion and height differencing.  With
every accepted projector rerun on the masked input,

\[
 \boxed{
 |\mathscr R_{{\rm core},Y,H_B}^{\sigma}(P_{\rm cl}W)|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon .}
\]

The result holds on all opposing even-shift atoms.  The cofactor-gcd-one and
\(r\equiv2\pmod4\) hypotheses from the launch target are unnecessary for
this absolute estimate.

## Decisive count and operator seam

In primitive coordinates the two close inequalities give

\[
 S+w\le D_L/g,
 \qquad |\kappa(U-v)|\le3D_L/g.
\]

The hard cone forces \(g=O(1)\).  For fixed
\((\kappa,g,U,v,w)\), the determinant and shift window leave only
\(O(1)\) integers \(S\).  Consequently

\[
 \#\mathcal I_{\rm cl}
 \ll LD_L\log(2L)+LD_L^2\ll L^2,
\]

with no hidden \(Y\), Fourier-mode, or lift multiplicity.

The physical mask does not commute with an already formed height
difference.  Its affine-site commutator, births, and deaths remain in the new
core.  The accepted Round-187--Round-192 safe proofs are deletion-stable
when their operators are rerun on \(P_{\rm cl}W\), so the exact linear core
identity preserves the same target bound, including the literal \(T=0\)
branch.

## Boundary and remaining core

The exact disjoint complement is

\[
 P_1=\mathbf1_{|d-gm|>D_L},
\qquad
 P_2=\mathbf1_{|d-gm|\le D_L}
      \mathbf1_{|d'-gm'|>D_L}.
\]

Only \(P_{\rm cl}\) is proved target-safe.  For a general width
\(1\le D\le L\), the absolute mechanism costs

\[
 O_\varepsilon((LD\log(2L)+LD^2)X^\varepsilon).
\]

Thus square-root width is its power boundary.  This does not lower-bound
either complement.

On the narrower \((m,m')=1\), \(r\equiv2\pmod4\) sub-sector, the map

\[
 \tau_g(d,m,d',m')=(gm,d/g,gm',d'/g)
\]

is an exact character-reversing orientation involution after complete
Fourier recombination.  This finite algebra is retained as a control, not as
the proof of the absolute sector.

## Formalization and proof-state consequence

The durable kernel is

`proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`

at SHA-256

`470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`.

It passed final count/operator, formalization/provenance, and blind/scope
review.  The blind finite rederivation is transparently qualified by prior
through-Round-192 context and is not a premise of the principal theorem.
The finite Wolfram control remains diagnostic only.

The State Patch creates one subordinate proved-internal sector and updates
only the still-open hard-M1 high-radical small-\(t\) owner.  It does not
prove the complete rho-large core, complete original \(t=1\), any original
\(t\ge2\) range, either M1 parent, any M2 parent, endpoint uniformity, M9, a
bridge, the quarter theorem, or a better exponent.

The strongest internal exponent remains \(1/3\), the accepted external
benchmark remains \(0.3144831759740614\ldots\), and the target remains
\(1/4\).

Round 193 closes under exactly
`strict_rho_large_gcd_scaled_orientation_sector`.

Round 194 is the mandatory full-proof strategy and current-primary-literature
checkpoint after analytic Rounds 191--193.  No next analytic round may be
launched before that checkpoint closes.
