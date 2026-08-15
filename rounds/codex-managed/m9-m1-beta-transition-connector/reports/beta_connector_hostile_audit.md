# Hostile audit of the beta-transition connector

## 1. Result: corrected connector lemma and scoped no-go

There are three decisive seams.

First, a mask written only as \(\psi(\beta)\) is not a disjoint
single-transition mask: it also contains the double-bounded box.  A genuine
beta-only partition may be taken as
\[
 \Theta_\beta(\alpha,\beta)=\psi(\beta)\{1-\psi(\alpha)\}.
\]
This creates two, not one, Cauchy--Pompeiu derivative terms.  The frozen
question is well posed only after either this convention is adopted or the
central box is explicitly assigned to the beta branch.

Second, direct stationary phase in the Round-20 amplitude does **not**
produce a \(q^{-1}\) coefficient.  The Hessian factor changes the apparent
power to exactly \(q^0\).  This agrees with the exact sine-kernel inversion.
Consequently a character logarithmic generating function with coefficients
\(\chi_4(q)/q\) is not available from alpha stationary phase alone.

Third, radial integration of the resulting finite \(\chi_4\) Dirichlet
kernels is a plausible replacement, but no target-sized estimate follows
without a new uniform argument retaining the actual top Hilbert profile,
finite-height cutoffs, beta/nu dependence, and all resonance crossings.
The exact connector algebra is promotable only after independent agreement;
the transition estimate is not.

## 2. Exact statement and hypotheses

Fix \(z=u+v\), write \(A=s-z/2=x+iy\), and put
\(B_+=A+z\).  Thus \(y=\beta\) and
\(\alpha=y+\operatorname{Im}z\).  Let
\(R=[-\kappa,a_A]\times[-T,T]\), where
\(a_A=c'-\operatorname{Re}z/2>0\), and extend the real mask to the strip by
the explicit prescription \(\psi(\operatorname{Im}A)\).  Without this
off-line prescription, values on the original vertical line do not define a
unique Cauchy--Pompeiu connector.

For a meromorphic factor \(F(A)\) and
\(\Theta_\beta=\psi(y)(1-\psi(y+\operatorname{Im}z))\), set
\[
 D_\Theta(y)=\psi'(y)(1-\psi(y+\operatorname{Im}z))
 -\psi(y)\psi'(y+\operatorname{Im}z).
\]
Then, with the boundary of \(R\) counterclockwise,
\[
 \oint_{\partial R}\Theta_\beta F\,dA
 =2\pi i\sum_{p\in R}\Theta_\beta(p)\operatorname{Res}_{A=p}F
 -\iint_R D_\Theta(y)F(x+iy)\,dx\,dy.                 \tag{26.1}
\]
If \(T>2B\), uniformly after accounting for the translated finite
\(s\)-box, the two horizontal \(A\)-segments vanish.  To ensure this for
all \(|\operatorname{Im}z|\le U+V\), one needs the corresponding margin
\(S>(U+V)/2+2B\), not merely \(S>(U+V)/2\).  All outside \(u,v\) sides,
top/axial/corner terms, floors, stars, and the factor
\[
 -\frac4\pi X^{1/4}\operatorname{Re}\{e(1/8)\,\cdot\}
\]
remain unchanged.

At \(A=0\), \(\zeta(1-A)=-A^{-1}+O(1)\).  For the disjoint mask,
\[
 \Theta_\beta(0)=1-\psi(\operatorname{Im}z),          \tag{26.2}
\]
so the crossed residue is only an alpha-filtered share of the accepted
\(R_1\) residue, not automatically the full Round-24 term.

## 3. Proof and normalization audit

Since
\[
 \bar\partial_A\Theta_\beta
 =\frac i2D_\Theta(y),
\]
Cauchy--Green gives (26.1); the minus sign is
\(2i(i/2)=-1\).  The right vertical is upward, the left vertical downward,
the top runs right-to-left, and the bottom left-to-right.  For the simpler
overlapping mask \(\psi(\beta)\), replace \(D_\Theta\) by \(\psi'\).

For the alpha stationary phase, Round 20 gives, under \(m=hq\), the
arithmetic part of amplitude (6)
\[
 \left(\frac hq\right)^{\zeta/2}m^{-\sigma}
 =h^{-\sigma+\zeta/2}q^{-\sigma-\zeta/2},             \tag{26.3}
\]
and the large-gamma power
\(|\alpha|^{\sigma+\zeta/2-1/2}\).  The phase satisfies
\[
 \partial_\alpha\Psi
 =\log\frac{\alpha D_j}{\pi q\sqrt{Xx}},\qquad
 \alpha_0=\frac{\pi q\sqrt{Xx}}{D_j},\qquad
 |\Psi''(\alpha_0)|=\alpha_0^{-1}.                   \tag{26.4}
\]
The one-dimensional stationary factor is therefore
\(\asymp\alpha_0^{1/2}\).  Combining it with (26.3) gives
\[
 q^{-\sigma-\zeta/2}
 \alpha_0^{\sigma+\zeta/2-1/2}\alpha_0^{1/2}
 =\left(\frac{\pi\sqrt{Xx}}{D_j}\right)^{\sigma+\zeta/2}, \tag{26.5}
\]
which is exactly \(q^0\).  Dropping the Hessian factor is the source of the
false \(q^{-1}\).

The exact control is
\[
 \frac1{2\pi i}\int X_4(B)Y^{-B}\,dB
 =\sin\frac{\pi Y}{2}.
\]
After expanding the high character factor, its top boundary component is
\[
 K_Q(Y)=\sum_{q\le Q}\chi_4(q)
 \sin\frac{\pi qY}{2},                               \tag{26.6}
\]
again with no \(1/q\).  Although the asymptotic piece \(1/u\) of the top
Mellin transform can look like \(1/\alpha_0\) at an interior saddle, it
cannot replace the exact one-sided top transform: its hard jump contributes
the boundary sine term (26.6).  Hence it does not repair (26.5).

There is also an additional residue seam.  For the split radial remainder
\[
 \rho=\frac14-s-\frac v2
 =\frac14-A-\frac u2-v,
\]
\(R_1\) has an artificial pole at
\(A=1/4-u/2-v\), lying between the indicated right and left lines under the
Round-24 real-part hypotheses.  Its residue cancels only with the opposite
\(E_1\) residue.  Thus one must shift the recombined entire radial factor,
or carry both split terms through (26.1); shifting an isolated \(R_1\)
trace while listing only \(A=0\) is incorrect.

## 4. First doubtful or unproved step

The first open analytic step is a uniform radial estimate for (26.6) with
the actual, q-dependent amplitudes produced by the mask connector and the
finite top Hilbert transform.  For the pure kernel,
\[
 |K_Q(Y)|\ll
 \min\!\left(Q,\frac1{\operatorname{dist}(Y,,2\mathbb Z+1)}\right),
 \qquad K_Q(2k+1)=\pm\#\{q\le Q:q\text{ odd}\}.       \tag{26.7}
\]
Thus pointwise character Abel cancellation is false.  Radial integration
crosses every such resonance and must be performed before taking absolute
values.

On the hard top scale, put
\(Y=2\sqrt{Xx}/D_0\).  Then
\(e(\sqrt{Xx})=e(D_0Y/2)\).  Since \(D_0=\lfloor\sqrt X\rfloor\) is an
integer and \(q\) is odd, expansion of the sine gives frequencies
\(D_0\pm q/2\), so
\[
 |D_0-q/2|\ge\frac12.                                \tag{26.8}
\]
This parity gap removes the exact zero radial frequency \(q=2D_0\), and
suggests a harmonic/logarithmic bound after integration by parts in \(Y\).
It is the only promising actual-character mechanism found here.

However, (26.8) is not yet a proof.  The saddle cutoff depends on
\(qY\); \(\widehat W_0(a+i(\alpha-\beta-\nu))\), the connector, and the
beta/nu integrations cannot be frozen at the saddle; logarithmic mask
convolution has tails; and hard radial endpoints generate boundary terms.
A bound must show uniform bounded variation or an equivalent signed
Hilbert estimate for this full amplitude.  Direct \(L^1\) use of (26.7)
costs \(\log Q\) at each resonance period and accumulates over the whole
radial range, so it does not by itself close the trace.

## 5. Control tests and outcomes

- **Signed versus unsigned:** at odd integral \(Y\), the actual product
  \(\chi_4(q)\sin(\pi qY/2)\) is constant in sign on odd \(q\).  Therefore
  neither signed nor unsigned pointwise summation saves a power.  Outcome:
  radial coupling is indispensable.
- **Coefficient adversary:** arbitrary signs may align with the sine at
  every fixed \(Y\), giving full length \(Q\).  The parity gap (26.8) uses
  both the actual odd support of \(\chi_4\) and integral \(D_0\); it does
  not prove an adversarial analogue.  Outcome: mechanism is correctly
  character-specific.
- **Support and degeneracy:** \(\psi(\beta)\) includes the central box;
  \(\Theta_\beta\) removes it but creates the second derivative connector
  and weights the \(A=0\) residue by (26.2).  Outcome: the original frozen
  mask/residue wording is incomplete.
- **Exact versus near resonance:** exact sine resonances (26.7) occur
  throughout the physical x-range.  The combined top radial phase has no
  exact zero mode by (26.8), but near modes remain at the fixed half-unit
  gap and require an actual amplitude-variation estimate.  Outcome:
  promising but unproved.
- **Normalization:** (26.5) is normalized \(q^0\), and every connector,
  residue share, and radial estimate must still be multiplied by the
  external \(-(4/\pi)X^{1/4}\operatorname{Re}e(1/8)\).  Outcome: no hidden
  \(X^{-1/4}\) or \(q^{-1}\) gain exists.

## 6. Dependencies and exact artifacts used

Used only `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`, the Round-19 vector-Hankel synthesis, the
Round-20 diagonal-transition synthesis and its accepted blind amplitude,
the Round-24 R1-residue synthesis, and the Round-25 partial-functional-
equation synthesis and exact sine-kernel control.  No Round-26 claimant
report, numerical experiment, web source, or external theorem was used.

## 7. Recommended state effect

**Revise** `M9-M1-beta-transition-connector-reduction`; do not promote a
transition estimate.  The conductor may retain as candidate exact algebra
the signed Cauchy--Pompeiu identity (26.1), subject to independent agreement.
The state must record that:

1. a disjoint beta mask has two derivative connectors;
2. its \(A=0\) residue is only an alpha-filtered R1 share and must be
   recombined with the complementary share or bounded anew;
3. the isolated \(R_1\) displacement crosses an artificial pole unless
   \(E_1+R_1\) is kept together; and
4. alpha stationary phase gives \(q^0\), not \(q^{-1}\).

The smallest surviving route is a full physical radial estimate for the
finite character Dirichlet kernel, exploiting the actual top-scale parity
gap (26.8) while retaining the connector, profiles, floors, finite top
Hilbert transform, endpoints, and outside-height limits.
