# Round 27: Separated beta radial pushforward

## 1. Result

The positive-alpha stationary part of the post-endpoint radial remainder has one more inverse frequency factor than the unsplit radial transform. After the symmetric physical top-pole split, its local signed convolution has a second inverse frequency factor. Thus the separated interior is locally absolutely summable in the character frequency. This is a scoped local lemma, not a bound for the complete beta transition.

## 2. Exact statement and hypotheses

Use the accepted beta branch, the actual dyadic profile, and

$
R_{1,v}(1-s)=-(pi i sqrt(X)/rho) I_1(rho),
$

where $rho=1/4-s-v/2$. Assume bounded beta, fixed $b=Re(v)>0$, and a positive-alpha saddle separated from saddle entry, saddle exit, and the artificial $rho=0$ seam. Put

$
alpha_0=pi q sqrt(Xx)/D_j.
$

On the saddle support,

$
1/rho=2i/alpha_0+
O((1+|beta+nu|)/alpha_0^2).
$

Consequently the post-endpoint remainder has a $q^{-1}$ factor relative to the unsplit transform. If the hard-top factor is first interpreted by the symmetric distributional limit

$
(a+i mu)^{-1} -> pi delta_0(mu)-i PV(1/mu),
$

then the signed local $nu$ convolution contributes $O_b(alpha_0^{-2})$ in the principal-value part, while the delta part is smaller. After restoring the numerator of the radial remainder, the separated stationary coefficient is therefore of size $D_j/(q alpha_0)$, hence has $q^{-2}$ decay up to fixed-height or logarithmic factors.

## 3. Proof or derivation

The diagonal variables satisfy

$
r=(alpha+beta+nu)/2=-Im(rho), \qquad
mu=alpha-beta-nu, \qquad
alpha=r+mu/2.
$

At the positive-alpha saddle, $alpha=alpha_0$ and the radial denominator gives

$
sqrt(X)/rho = O(D_j/(q sqrt(x))).
$

The $x^{1/2}$ change in $I_1$ cancels the displayed $sqrt(x)$ loss. This proves the extra inverse $q$ factor relative to the unsplit $G=E_1+R_1$ transform.

For the top factor, taking absolute values before the physical split is invalid at the pole. After the PV-plus-delta split, subtract the value at the principal-value singularity. The numerator difference supplies one factor of the displacement, and the fixed-height transform of the compact profile supplies integrable decay. The remaining radial denominator supplies the other inverse $alpha_0$ factor. Thus the PV convolution is $O_b(alpha_0^{-2})$; the point-supported delta term is no larger. Multiplying by the radial numerator yields $D_j/(q alpha_0)$.

## 4. First doubtful or unproved step

Uniform patching is not proved at saddle entry or exit, in the nonstationary zones, or at the artificial $rho=0$ seam. The full scale, height, radial, endpoint, and outside-side sums are also not carried out. Therefore this report does not establish the complete beta trace estimate.

## 5. Required control test and outcome

The normalization control distinguishes the unsplit transform from the post-endpoint remainder: the former is $q^0$ after stationary phase, while the explicit $1/rho$ in the latter restores $q^{-1}$. This control passes.

The hard-top control fails if absolute values are inserted before the symmetric split: an actual top-pole sample grows like $1/a$, and its absolute integral has a logarithmic divergence. The signed PV-plus-delta formulation passes locally and gives the second inverse frequency factor.

## 6. Dependencies and exact artifacts used

- Round 20 vector-Hankel kernel and radial remainder identity.
- Round 24 physical radial residue normalization.
- Round 25 beta/alpha transition assignment.
- Round 26 beta connector identity and accepted profile.
- Round 27 frozen formulas in the campaign plan.

No numerical experiment and no external theorem were used. This report was materialized by the conductor from the task's final analytic verdict after the assigned report write did not complete inside its time box.

## 7. Recommended state effect

Revise the Round 26 stationary-kernel node so that $q^0$ is explicitly restricted to the unsplit transform. Promote the post-endpoint $q^{-1}$ normalization and the separated fixed-height signed-convolution $q^{-2}$ lemma with all exclusions above. Reject uniform pre-split hard-top $q$-bounded-variation as an interface. Retain the complete beta transition, uniform saddle patching, full sums, endpoints, and outside-side limits as open.
