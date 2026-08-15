# Hostile audit of the beta radial pushforward and q-BV route

## 1. Result

The hierarchical partition and the recombined contour ledger pass.  The
double-bounded share is independently target-safe on the original right
line after the signed physical top limit.  Two corrections materially
change the proposed positive-alpha attack.

First, Round 26's \(q^0\) normalization applies to the unsplit radial
factor \(G=E_1+R_1\), not to the post-endpoint transition remainder
\(R_1\).  Since
\[
 R_{1,v}(1-s)=-\frac{\pi i\sqrt X}{\rho}
 \int_1^{N_X}x^{\rho-1/2}e(\sqrt{Xx})\,dx,
 \qquad \rho=\frac14-s-\frac v2,
\]
the positive-alpha saddle has a genuine \(q^{-1}\) factor.  Thus the
rejection of every \(q^{-1}\) character-kernel route was too broad.

Second, pointwise complete-profile q-BV is false for the hard top.  After
the correct signed split
\[
 \frac1{0^++i\mu}=\pi\delta_0(\mu)-i\,\mathrm{PV}\frac1\mu,       \tag{27.1}
\]
the \(R_1\) denominator and top Hilbert denominator together are better:
their nu-convolution is \(O(\alpha^{-2})\), while the delta part is
\(O(\alpha^{-4})\).  Restoring the stationary numerator converts this to
an absolutely summable \(q^{-2}\) leading coefficient.  This bypasses,
rather than proves, the proposed q-BV theorem.

This is a scoped positive result, not closure of the beta trace.  Uniform
saddle entry/exit, nonstationary pieces, the exact theta-density scale sum,
radial endpoints, and finite outside-height limits remain open.

## 2. Exact statement and hypotheses

Use
\[
 1=\psi(\beta)+(1-\psi(\beta))\psi(\alpha)
 +(1-\psi(\beta))(1-\psi(\alpha)).                    \tag{27.2}
\]
The first term owns the double-bounded box.  In it, shift the complete
recombined radial factor \(G=E_1+R_1\).  The accepted Cauchy--Green formula
has the single connector \(-\iint\psi'(\beta)\mathcal F\), crosses the full
\(A=0\) residue because \(\psi(0)=1\), and has no artificial radial pole
because those of \(E_1,R_1\) cancel before displacement.  The residue of
\(\zeta(1-A)\) at \(A=0\) is \(-1\).  It is reconciled once with the full
Round-24 \(R_1\) residue; it is not inserted again.

For the positive-alpha interior put
\[
 u=a+i\mu,\quad v=b+i\nu,\quad z=u+v,\quad
 A=s-z/2,\quad B=s+z/2,
\]
\[
 \zeta=a+b,\qquad
 \mu=\alpha-\beta-\nu,qquad
 \rho=\rho_0-i\frac{\alpha+\beta+\nu}{2},\quad
 \rho_0=\frac14-\sigma-\frac b2.                     \tag{27.3}
\]
Assume \(|\beta|\le 2B_0\), an interior saddle separated from its finite
alpha endpoints, and
\[
 f_b(\nu)=\widehat\phi(b+i\nu),\qquad
 \|f_b\|_{W^{1,1}}+\|(1+|\nu|)f_b\|_1\ll_b 1,
 \quad |f_b^{(k)}(\nu)|\ll_{b,k}(1+|\nu|)^{-3-k}.     \tag{27.4}
\]
These hold for the accepted height profile on every fixed line (b>0).
The pole \(\widehat\phi(v)=v^{-1}+O(1)\) makes the constants nonuniform
as (b\downarrow0).  Repeated integration by parts in the defining
Mellin integral shows at most a fixed power of (b^{-1}); the standard
choice (b=1/\log(2X)) therefore costs only a power of \(\log X\).

The exact phase data are
\[
 \alpha_0=\frac{\pi q\sqrt{Xx}}{D_j}=q\theta_j(x),qquad
 \theta_j(x)=\frac{\pi\sqrt{Xx}}{D_j},qquad
 |\Psi''(\alpha_0)|=\alpha_0^{-1}.                   \tag{27.5}
\]
Up to bounded beta factors and fixed constants, the stationary \(R_1\)
amplitude is the stationary unsplit-G amplitude multiplied by
\[
 \frac{\sqrt{Xx}}{\rho}
 =\frac{D_j}{\pi q}\frac{\alpha_0}{\rho}.            \tag{27.6}
\]
Equivalently its exact scale and radial powers before the beta/nu
convolution are
\[
 \begin{aligned}
 &\frac{D_j}{q}\,h^{-\sigma+\zeta/2}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 \left(\frac{\pi\sqrt{Xx}}{D_j}\right)^{\sigma+\zeta/2}
 x^{-\sigma-3/4-b/2}\\
 &\hspace{35mm}\times
 \frac{\alpha_0}{\rho}
 \widehat W_j(a+i\mu)f_b(\nu),                       \tag{27.7}
 \end{aligned}
\]
with the convention that the displayed \(D_j/q\) and
\(\alpha_0/\rho\) together are (27.6).  Formula (27.7), rather than the
unsplit \(q^0\) formula, is the relevant post-endpoint normalization.

## 3. Proof or derivation

### Partition, residue, and central box

Equation (27.2) is exact and assigns every point once.  Applying
Cauchy--Green to \(G\), not isolated \(R_1\), removes the artificial-pole
ambiguity.  The beta mask is one at the arithmetic pole, so the residue is
the full unfiltered Round-24 term.

If both \(\alpha,\beta\) are bounded, then \(t\) and
\(\operatorname{Im}z=\alpha-\beta\) are bounded.  On the original right
line \(\Re B>1\), the q-series is absolutely convergent.  The smooth
height transform controls large opposite \(\mu,\nu\), and (27.1) makes the
top convolution a bounded Hilbert transform plus its half/delta value.
The real scale weights sum geometrically, with at most logarithmic endpoint
loss absorbed by \(X^\varepsilon\).  Hence this compact central share is
\(O_\varepsilon(X^\varepsilon)\) on the normalized scale.  This conclusion
uses signed physical inversion; absolute \(|1/u|\) is not uniform.

### Why R1 restores q inverse

Round-20 stationary phase combines
\[
 \alpha_0^{\sigma+\zeta/2-1/2},\quad
 h^{-\sigma+\zeta/2}q^{-\sigma-\zeta/2},\quad
 \alpha_0^{1/2}
\]
to give q power zero for \(G\).  The \(R_1\) integrand is \(x^{1/2}\)
times the G radial integrand and carries \(\sqrt X/\rho\).  Equation
(27.6) therefore supplies exactly \(D_j/q\) times
\(\alpha_0/\rho\).  For bounded beta and nu,
\(|\alpha_0/\rho|\asymp1\); hence the post-endpoint coefficient is
\(q^{-1}\), not \(q^0\).

The exact sine kernel is consistent with this ledger.  The unsplit G
kernel has q0 boundary capacity; integration by parts in the radial
variable splits it into the full endpoint sine term \(E_1\) and the
\(q^{-1}\)-weighted R1 remainder.  Recovering G by adding E1 restores the
q0 boundary term.  Thus the two normalizations concern different operators
and do not conflict.

### Hard-top signed convolution

Set \(L=\alpha-\beta\), \(K=-\alpha-\beta\).  The hard-top convolution
before multiplying the stationary numerator is
\[
 \mathcal C_a(\alpha,\beta)=
 \int_\mathbb R\frac{f_b(\nu)\,d\nu}
 {\{\rho_0-i(\nu-K)/2\}\{a+i(L-\nu)\}}.              \tag{27.8}
\]
Taking \(a\downarrow0\) by (27.1), its delta component is
\[
 \mathcal C_\delta=
 \frac{\pi f_b(L)}{\rho_0-i\alpha}=O(\alpha^{-4}).    \tag{27.9}
\]
For the PV component, partial fractions give a factor
\((2\alpha+2i\rho_0)^{-1}\) times the difference between the Hilbert
transform of \(f_b\) at \(L\) and its Cauchy transform at
\(K-2i\rho_0\).  Under (27.4), each transform is \(O(\alpha^{-1})\),
uniformly for bounded beta and bounded \(\rho_0\) (with separated PVs if
\(\rho_0=0\)).  Therefore
\[
 \boxed{\mathcal C_{\rm PV}(\alpha,\beta)=O_b(\alpha^{-2}),\qquad
 \mathcal C_\delta(\alpha,\beta)=O_b(\alpha^{-4}).}   \tag{27.10}
\]

Multiplying (27.10) by the numerator in (27.6) yields
\[
 \frac{D_j}{q}\alpha_0\mathcal C_{\rm PV}
 \ll \frac{D_j}{q\alpha_0}
 =\frac{D_j}{q^2\theta_j(x)},                        \tag{27.11}
\]
while the delta part is \(O(D_jq^{-4}\theta_j(x)^{-3})\).
Thus the hard-top stationary interior is absolutely q-summable.  The
smooth remainder of the top profile and every smooth interior
\(\widehat W_j\) are better: convolution of their rapid mu-decay with
(27.4) and the rho denominator is at least \(O(\alpha^{-4})\).

### Artificial-rho seam

Let omega localize \(|\rho|\ll1\) and use
\[
 R_1=\omega G+(1-\omega)R_1-\omega E_1.              \tag{27.12}
\]
On omega support, \(\nu=-\alpha-\beta+O(1)\) and
\(\mu=2\alpha+O(1)\).  Hence
\[
 f_b(\nu)=O(\alpha^{-3}),\qquad
 (0^++i\mu)^{-1}=O(\alpha^{-1}).                     \tag{27.13}
\]
The omega-G term is therefore \(O(\alpha^{-4})\) relative to the q0
stationary normalization.  The pole/PV and residue pieces of
\(-\omega E_1\) receive the same profile separation; after the artificial
residue is reconciled, they are at worst \(O(\alpha^{-2})\), and in the
localized residue itself \(O(\alpha^{-4})\).  Derivatives of omega and
\(\psi'(\beta)\) preserve (27.13).  Thus the artificial seam does not
leave a genuine q-inverse obstruction at large positive alpha.  The masked
E1 share is not automatically covered by the unmasked endpoint theorem,
but (27.13) gives it direct high-alpha summability; its bounded-alpha part
belongs to the already controlled central box.

### Theta pushforward

For any radial monomial \(x^\lambda dx\), the exact pushforward is
\[
 x=\frac{D_j^2\theta^2}{\pi^2X},\qquad
 x^\lambda dx=
 \frac{2D_j^{2\lambda+2}}{\pi^{2\lambda+2}X^{\lambda+1}}
 \theta^{2\lambda+1}d\theta.                         \tag{27.14}
\]
This is the narrow true density lemma.  It does not permit multiplying a
one-period logarithmic kernel norm by one: the theta interval contains
many periods, and the complete amplitude depends on \(q\theta\).
Fortunately (27.11) makes the stationary interior absolutely summable in
q, so a pointwise q-BV theorem is unnecessary there.

## 4. First doubtful or unproved step

The first unproved step is a uniform finite-alpha decomposition joining
the large positive-alpha stationary formula to saddle entry, saddle exit,
mask-transition zones, and the nonstationary negative-alpha piece.  The
estimates (27.10)--(27.13) apply only after the physical top split and only
in the separated positive-alpha interior.  They do not justify exchanging
the finite alpha limit, the PV limit, q summation, radial integration, and
outside u,v limits.

Nor has the full scale/h/radial sum of (27.7) and (27.14) been proved
uniform at both hard radial endpoints.  Endpoint stationary points create
half-Fresnel terms, and finite outside sides remain explicit.  These are
now the smallest surviving beta-branch seams; q-BV is not the principal
obstruction.

## 5. Control tests and outcomes

- **Actual hard-top BV falsifier.**  At fixed beta, nu and theta, the top
  factor sampled at the saddle is
  \[
   \{a+i(q\theta-\beta-\nu)\}^{-1}.
  \]
  Choose an odd actual q-star and vary the continuous physical theta so
  that \(q_*\theta=\beta+\nu\) and
  \(f_b(\nu)\ne0\).  Such choices exist because the nonzero analytic
  transform \(f_b\) cannot vanish on an interval.  The discrete BV norm is
  at least \(c|f_b(\nu)|/a\), hence is not uniform as \(a\downarrow0\).
  Outcome: pointwise complete-profile q-BV before (27.1) is false.
- **Absolute pre-split falsifier.**  For \(L=\alpha-\beta\) with
  \(f_b(L)\ne0\), the absolute integral near \(\nu=L\) is
  \[
   \gg \frac{|f_b(L)|}{\alpha}
   \int_{|y|<c}\frac{dy}{\sqrt{a^2+y^2}}
   \asymp\frac{|f_b(L)|}{\alpha}\log(1/a).
  \]
  There are arbitrarily large such L.  Outcome: taking absolute values
  before the PV/delta split is invalid.
- **Signed versus unsigned/adversarial.**  Exact sine resonance still
  makes the pointwise character sum coherent.  Estimate (27.11), however,
  is absolute and therefore also holds for unsigned coefficients on this
  R1 stationary subpiece.  This does not imply the false unsigned M1
  theorem: E1, the other transition branches, entry/exit zones, and outside
  limits are not included.
- **Exact versus near resonance.**  The top parity gap applies only to
  \(D_0\).  It fails on actual interior scales: if
  \(D_j=\lfloor\sqrt X\rfloor/2^j\) and
  \(2D_j\) is odd, the odd q equal to \(2D_j\) gives exact zero combined
  radial frequency.  Outcome: no all-scale parity-gap proof is valid;
  (27.11) does not use one.
- **Residue and normalization.**  Shifting G crosses A=0 once and no
  artificial pole.  Splitting afterward gives the target-safe full R1
  residue and endpoint ledger.  The stationary R1 factor is (27.6), so its
  q exponent is minus one before top convolution and minus two afterward.
  Every bound remains on the normalized scale and must finally receive
  \(-(4/\pi)X^{1/4}\operatorname{Re}\{e(1/8)\cdot\}\).
- **Support/endpoints/sides.**  Compact beta support deletes only A-horizontal
  sides with adequate margin.  It does not delete outside u,v sides or
  license the symmetric top limit.  Outcome: finite-side closure remains
  open.

## 6. Dependencies and exact artifacts used

Used only the task brief and its permitted context: `protocol.md`, the
authoritative graph and active campaign, the finite character-kernel file,
and the accepted Round-20, Round-21, Round-24, and Round-26 syntheses.  The
exact post-endpoint R1 normalization was rederived from the formula recorded
in the graph/context.  No Round-27 claimant report, numerical experiment,
web source, or external theorem was used.

## 7. Recommended state effect

Promote or retain for conductor synthesis only the following narrow facts:

1. the hierarchical partition, central-box ownership, and recombined-G
   displacement with one full A=0 residue;
2. the correction that the post-endpoint R1 saddle is q-inverse even though
   the unsplit-G saddle is q0;
3. the actual-profile no-go against uniform pre-split hard-top q-BV and
   absolute \(|1/u|\) control;
4. the signed top convolution lemma (27.10), which improves the stationary
   R1 coefficient to q-minus-two; and
5. the exact theta pushforward (27.14) and the high-alpha artificial-seam
   separation (27.13).

Do **not** promote the full beta-transition estimate.  Revise its next
action away from a pointwise complete-profile q-BV theorem.  The smallest
survivor is a uniform stationary/transition patching theorem with the
PV/delta split performed first, followed by the complete scale/h/radial
sum and finite endpoint/outside-side limits.  If that theorem preserves
(27.11) through saddle entry and exit, the positive-alpha R1 branch becomes
absolutely summable and the beta obstruction is substantially reduced.
