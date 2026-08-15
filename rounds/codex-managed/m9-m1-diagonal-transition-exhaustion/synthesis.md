# Round 20 synthesis: diagonal transition formula and exhaustion obstruction

Campaign: `m9-m1-diagonal-transition-exhaustion`  
Round type: diagonal transition and contour-exhaustion attack  
Graph SHA-256 before patch: `8b995fb71c46fb4b38a2ee79c70da79e99a16fa67ebaf84338f736186abd42ef`

## Conductor decision

Promote the exact diagonal gamma factorization and finite single-transition
normal forms. Retain all transition estimates as open. Promote only a scoped
capacity obstruction to deleting radial horizontal sides by nested height:
the hard radial cutoff produces an endpoint expansion beginning at (S^{-1}),
while the left-edge functional-equation factor can grow polynomially.
The terminal single-transition traces also have nonintegrable raw size
against the hard (1/u) measure, so a new signed vector-Hilbert estimate is
required.

The planned hostile task was terminated after failing to deliver within the
round budget. Accordingly, the claimant's stronger two-sided asymptotic
lower bound and exact sharpness assertion are not promoted. They remain
candidate evidence. No target-sized sector is proved.

## Exact diagonal transition algebra

Write

\[
 u=a+i\mu,\quad v=b+i\nu,\quad z=\zeta+i\eta,
 \quad s=\sigma+it,
\]

with (\zeta=a+b), (\eta=\mu+\nu), and set

\[
 \alpha=t+\eta/2,\qquad \beta=t-\eta/2.
\]

On the terminal line, the exact quotient factors as

\[
 K_z(1-s)=C_{\sigma,\zeta}
 e^{i\{\alpha\log(4/\pi)-\beta\log\pi\}}
 R_\alpha R_\beta,
\]

where

\[
 R_\alpha=
 \frac{\Gamma((1+\sigma+\zeta/2)/2+i\alpha/2)}
 {\Gamma((2-\sigma-\zeta/2)/2-i\alpha/2)},
\]

\[
 R_\beta=
 \frac{\Gamma((\sigma-\zeta/2)/2+i\beta/2)}
 {\Gamma((1-\sigma+\zeta/2)/2-i\beta/2)}.
\]

For bounded \(\beta\) and large \(|\alpha|\), \(R_\beta\) remains exact and

\[
 R_\alpha=
 \left|\frac\alpha2\right|^{\sigma+\zeta/2-1/2}
 e^{i\operatorname{sgn}(\alpha)
 (|\alpha|\log(|\alpha|/2)-|\alpha|+\pi/4)}
 (1+O(|\alpha|^{-1})).
\]

The opposite transition interchanges \(\alpha,\beta\); its phase constant is
(-\pi/4). The coordinate map

\[
 t=(\alpha+\beta)/2,\quad
 \eta=\alpha-\beta,\quad
 \mu=\alpha-\beta-\nu
\]

has absolute Jacobian one. The finite box becomes

\[
 |\nu|\le V,quad |\alpha-\beta-\nu|\le U,quad
 |\alpha+\beta|\le2S.
\]

Every scale factor, floor, (widehat\phi), (widehat W_j), top (1/u),
dual incidence, residue, endpoint star, and horizontal side remains present.
The explicit (x)-phase is recorded in the blind report and is accepted as
finite algebra, not an estimate.

## Nested-exhaustion capacity

The concrete choice

\[
 S_X(U,V)=(X+U+V+2)^4
\]

separates each radial horizontal side from both transition planes and makes
the radial (x)-phase nonstationary. Integration by parts in (y=\log x)
then gives an endpoint expansion whose first term is (O(S^{-1})), not
rapid decay, because the radial cutoff has hard endpoints. On the left edge
(\lambda=1-c'<0), the degree-two functional-equation quotient has the
available upper capacity (O(S^{1-2\lambda})). Thus the elementary
pointwise estimate for the side is (O(S^{-2\lambda})), which grows.

This proves a method obstruction: increasing (S) cannot justify side
deletion by absolute pointwise decay. It does not prove that the fully
integrated signed side is large; cancellation between its two endpoint
expansions and the ((\sigma,u,v))-integrals remains possible and is an open
theorem.

## Terminal trace capacity

On (s=c'+it), the trace (|\beta|\lesssim1) has gamma magnitude

\[
 O((1+|\alpha|)^{c'-1/2+\zeta/2}),
\]

and the opposite trace has exponent (c'-1/2-\zeta/2). Since the top
profile contributes only (1/u) and (|\eta|\asymp|\Im u|) on a swept
trace, the raw absolute capacity on the first trace is

\[
 |\Im u|^{c'-3/2+\zeta/2},
\]

which is nonintegrable for the required (c'>1+\zeta/2). This is not a
lower bound for the signed operator; it proves that ordinary absolute
Mellin integration cannot pass the hard-Perron limit.

## Smallest surviving kernel

The exact survivor consists of:

1. the two diagonal single-transition vector traces with the symmetric
   (1/u) measure;
2. the radial horizontal-side functional, including both hard endpoint
   expansions;
3. all arithmetic, axial, corner, and radial endpoint residues.

Neither faster nesting nor fixed-order Hankel asymptotics controls this
object. The next viable move is to renormalize the radial Mellin transform
by subtracting its finite endpoint asymptotic series before shifting the
contour, then test whether the two endpoint functionals cancel against
explicit residues or leave a smaller signed boundary operator.

## State effect

- promote the exact diagonal factorization, Jacobian, transition amplitudes,
  and phases;
- promote the scoped no-go against absolute nested side deletion and
  absolute transition-trace integration;
- retain the stronger side asymptotic/lower-bound claim unaccepted because
  it lacked hostile validation;
- leave the diagonal signed traces, boundary functional, GAR, M9-M1, M9-M2,
  M9, and the target open.
