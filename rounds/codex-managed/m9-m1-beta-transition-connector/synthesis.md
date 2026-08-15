# Round 26 synthesis: exact connector algebra and the corrected radial kernel

> Round 27 scope correction (2026-08-13): the q^0 normalization below
> applies to the unsplit radial transform G=E1+R1. The actual
> post-endpoint R1 survivor has an additional 1/rho factor and is q^(-1)
> at a separated positive-alpha saddle; after the signed hard-top PV/delta
> convolution its local coefficient is q^(-2). See the Round 27 synthesis.

Campaign: `m9-m1-beta-transition-connector`  
Round type: beta-transition connector  
Graph SHA-256 before patch: `dce19447a6adb9e776acc944d2b47f22d31eba1f8c2cfecbacac10565d699fdc`

## Conductor decision

Promote three scoped facts and retain the transition estimate open:

1. the exact finite Cauchy--Green displacement, including its sign,
   orientations, finite sides, mask derivative, and crossed residues;
2. the corrected stationary normalization: an interior positive-alpha
   saddle leaves a \(q^0\), not a \(q^{-1}\), character coefficient;
3. the elementary maximal \(L^1\) estimate for the resulting finite
   period-four character Dirichlet kernel, together with the hard-top
   half-integer parity gap.

The round does not prove the connector-completed beta-transition estimate.
It exposes two residue seams that must be resolved before any such claim:
a disjoint mask crosses only a filtered share of the accepted \(R_1\)
residue, and shifting the isolated \(R_1\) term crosses its artificial pole
unless the cancelling \(E_1\) term is carried with it.

All work was analytical/algebraic.  No numerical experiment or external
theorem was used.

## Exact finite connector

Put \(A=s-z/2=x+iy\), let
\(R=[x_1,x_0]\times[-T,T]\), and let \(\mathcal F(A;z)\) be the complete
meromorphic finite integrand. For a \(C^1\) height mask
\(\Theta(y;z)\), define upward verticals \(V_x\) and left-to-right
horizontals \(H_\pm\). Positive rectangle orientation gives

\[
\boxed{
V_{x_0}=V_{x_1}+H_+-H_-
+2\pi i\sum_{p\in R^\circ}\Theta(\Im p;z)
 \operatorname{Res}_{A=p}\mathcal F
-\iint_R \partial_y\Theta(y;z)\mathcal F(x+iy;z)\,dx\,dy.}       \tag{26.1}
\]

The minus sign follows from
\(2i\bar\partial\Theta=2i(i/2)\partial_y\Theta=-\partial_y\Theta\).
If the finite \(A\)-height has the required support margin, \(H_\pm=0\);
the outside \(u,v\) sides and all axial, top, corner, profile, floor, and
endpoint terms remain.

There are two legitimate localization conventions, and they cannot be
silently interchanged:

- If the double-bounded box is assigned to the beta branch, take the
  hierarchical mask \(\Theta_\beta=\psi(\beta)\). It has one connector and
  crosses the full \(A=0\) share.
- If beta and alpha transition strips are made disjoint, take
  \(\Theta_\beta=\psi(\beta)(1-\psi(\alpha))\), where
  \(\alpha=\beta+\Im z\). Then

  \[
  \partial_\beta\Theta_\beta
  =\psi'(\beta)(1-\psi(\alpha))-\psi(\beta)\psi'(\alpha),       \tag{26.2}
  \]

  and at \(A=0\) the residue is weighted by
  \(1-\psi(\Im z)\).

Since \(\zeta(1-A)=-A^{-1}+O(1)\), the zeta residue has negative sign.
For the disjoint mask it is only an alpha-filtered share of \(R_1\); the
full unmasked Round-24 estimate does not bound that share separately.
Moreover, the split \(R_1\) factor has an artificial pole at
\(A=1/4-u/2-v\), whose residue cancels only against \(E_1\). Thus the
actual contour displacement must keep the recombined radial factor or
carry both split terms.  The physical factor

\[
-\frac4\pi X^{1/4}\operatorname{Re}\{e(1/8)(\cdots)\}
\]

is unchanged throughout.

## Stationary normalization correction

In the positive-alpha interior, Round 20 gives

\[
\partial_\alpha\Psi
=\log\frac{\alpha D_j}{\pi q\sqrt{Xx}},\qquad
\alpha_0=\frac{\pi q\sqrt{Xx}}{D_j},\qquad
|\Psi''(\alpha_0)|=\alpha_0^{-1}.                     \tag{26.3}
\]

The large-gamma and arithmetic powers are

\[
|\alpha|^{\sigma+\zeta/2-1/2}
h^{-\sigma+\zeta/2}q^{-\sigma-\zeta/2}.
\]

The one-dimensional stationary factor is \(\alpha_0^{1/2}\), so the total
\(q\)-power is

\[
q^{\sigma+\zeta/2-1/2},q^{1/2},
q^{-\sigma-\zeta/2}=q^0.                              \tag{26.4}
\]

The exact inverse-Mellin sine kernel independently confirms this
normalization. The initially proposed \(q^{-1}\) arctangent series is
therefore rejected.

At the saddle, the leading \(q\)-phase is linear:

\[
e^{-iq\theta_j(x)},\qquad
\theta_j(x)=\frac{\pi\sqrt{Xx}}{D_j}.                 \tag{26.5}
\]

## Finite character kernel

For

\[
D_M^\chi(\theta)=\sum_{q\le M}\chi_4(q)e^{-iq\theta},
\]

the exact geometric series gives

\[
\sup_{M\le Q}|D_M^\chi(\theta)|
\ll\min\{Q,1+|\cos\theta|^{-1}\},
\qquad
\int_0^{2\pi}\sup_{M\le Q}|D_M^\chi(\theta)|d\theta
\ll\log(2Q).                                         \tag{26.6}
\]

The same bound applies to interval sums with a multiplicative discrete-BV
norm. Exact quarter-lattice resonance can have height \(\asymp Q\), but
its radial \(L^1\) cost is logarithmic. On the hard top scale,
\(D_0=\lfloor\sqrt X\rfloor\) is integral and \(q\) is odd, hence

\[
|D_0-q/2|\ge\frac12.                                  \tag{26.7}
\]

This rules out an exact zero radial frequency in the elementary top
boundary phase.  It is not a full near-resonance estimate.

## Why the target remains open

The missing step is an exact physicalization and uniform decomposition of
the shifted line plus connector that simultaneously controls:

- saddle entry and exit and both transition edges;
- the hard top Hilbert pole
  \(\alpha-\beta-\nu=0\);
- theta-dependent actual profiles, floors, stars, and moving supports;
- radial endpoint terms and finite outside-height limits;
- the full or filtered \(A=0\) residue share and the \(E_1/R_1\)
  artificial-pole cancellation.

The logarithmic \(L^1\) lemma becomes useful only after the phase
pushforward has controlled density and the complete \(q\)-amplitude has an
integrable uniform discrete-BV norm.  It also holds for the ordinary
unsigned Dirichlet kernel, so it alone cannot prove the character-sensitive
transition estimate.

## Next target

Use the hierarchical partition

\[
1=\psi(\beta)+(1-\psi(\beta))\psi(\alpha)
 +(1-\psi(\beta))(1-\psi(\alpha)).                    \tag{26.8}
\]

This assigns the double-bounded box to the beta branch, retains the simple
one-edge beta connector, and crosses the full \(A=0\) residue. The next
round should first prove the double-bounded share target-safe and write the
recombined \(E_1+R_1\) displacement. It should then derive the exact radial
phase pushforward and complete-profile \(q\)-BV norm needed to apply
(26.6), with the hard top and smooth interior scales separated.

## State effect

- promote the finite Cauchy--Green identity and mask/residue scope;
- promote the \(q^0\) stationary normalization and finite character-kernel
  lemma;
- reject the \(q^{-1}\) arctangent mechanism and residue shortcuts;
- retain the connector-completed beta estimate, both transition traces,
  M9-M1, M9-M2, M9, and the target as open.
