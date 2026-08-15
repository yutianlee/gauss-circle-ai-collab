# Round 31 synthesis: use physical height before BV

Campaign: `m9-m1-beta-regular-finite-part-symbol-bv`  
Round type: complete regular beta finite-part symbol BV  
Graph SHA-256 before patch: `fd2cf1bc11f8cba48bce0e3713473d96478500c219cc980b5467312ecc4f992c`

## Conductor decision

Round 31 does not prove the complete regular-symbol BV obligation. It
proves the correct finite-section interface and rejects a tempting but
false derivative strategy.

The divided-difference derivative at fixed \(\mu=L-\nu\) is

\[
 \partial_L\Delta_H(L,\mu)=
 \frac{{\mathsf D}H(L,L-\mu)-{\mathsf D}H(L,L)}\mu,
 \qquad {\mathsf D}=\partial_L+\partial_\nu.          \tag{31.1}
\]

Thus a termwise proof asks for
\(\partial_\nu{\mathsf D}H_{\rm complete}\). But taking absolute values
after differentiating is too strong even for the actual height profile:
the term

\[
 \frac{f_b'(L-\mu)}{\mu\{A(L)+i\mu/2\}}              \tag{31.2}
\]

has mass \(\asymp_b\lambda^{-1}\) over a saddle cell, whereas the target
pre-numerator scale is \(\lambda^{-2}\). After the accepted numerator it
would lose a full \(\lambda\).

This is a coordinate artifact, not a no-go for the actual operator. In
physical height \((L,\nu)\), the translation derivative in (31.2) combines
with the moving endpoint traces. If the complete recombined regular kernel
satisfies

\[
 |K(L,\nu)|\ll X^\varepsilon\lambda^{-2}w_b(\nu),
 \qquad
 |\partial_LK(L,\nu)|\ll X^\varepsilon\lambda^{-3}w_b(\nu),   \tag{31.3}
\]

with \(w_b\in L^1\), then its exact finite-section integral has
supremum plus BV norm \(O(X^\varepsilon\lambda^{-2})\). The accepted
stationary numerator \((D_j/q)\lambda\) then gives
\(D_j/(q\lambda)=D_j/(q^2\theta_j(x))\), preserving local \(q^{-2}\).

The separated fixed-\(b\) \(R_1\) regular kernel satisfies this lemma away
from \(\rho=0\), on either signed saddle. The omega-prime and
omega-double-prime terms cancel exactly under identical ownership. The
complete omega-recombined kernel, axial residue, finite radial sides, and
joint \(U,V,S\) exhaustion are not yet bounded by (31.3).

Round 31 used no numerical experiment and no external theorem.

## Exact finite-section BV lemma

Let

\[
 I_{U,V}(L)=[-V,V]\cap[L-U,L+U],\qquad
 R(L)=\int_{I_{U,V}(L)}K(L,\nu)\,d\nu.              \tag{31.4}
\]

On a saddle cell of length \(O(\lambda)\), assume (31.3), including the
same integrable control on translated endpoint traces. On each affine cell,

\[
 R'(L)=\int_{p(L)}^{q(L)}\partial_LK(L,\nu)d\nu
 +q'(L)K(L,q(L))-p'(L)K(L,p(L)).                    \tag{31.5}
\]

The interior variation is
\(O(\lambda\lambda^{-3}\|w_b\|_1)=O(\lambda^{-2})\).
Fixed faces \(\nu=\pm V\) have zero velocity. Moving faces
\(\nu=L\mp U\) have \(L^1\) traces \(O(\lambda^{-2}\|w_b\|_1)\)
after substitution. Affine switches agree in value and collapsed sections
vanish. Hence

\[
 \boxed{\|R\|_\infty+\operatorname {Var}R
 \ll X^\varepsilon\lambda^{-2}\|w_b\|_1.}          \tag{31.6}
\]

This lemma is coordinate-sensitive: it estimates the signed translation
and endpoints together, rather than demanding target size from each
fixed-\(\mu\) derivative.

## Separated actual R1 kernel

After removing the explicit delta/log face term, the separated kernel is

\[
 K_{R_1}(L,\nu)=
 -\frac{i f_b(L)}{2A\{A+i(L-\nu)/2\}}
 +\frac{f_b(\nu)-f_b(L)}
 {(L-\nu)\{A+i(L-\nu)/2\}},                         \tag{31.7}
\]

where \(|A|\asymp|L|\asymp\lambda\) on a separated saddle patch. The
accepted decay of \(f_b,f_b',f_b''\), with the integral divided difference
at \(\nu=L\), gives (31.3). Therefore (31.6) proves the separated
regular-part BV bound and preserves its local \(q^{-2}\) power for both
saddle signs. The already-promoted face logarithm remains the stronger
local \(q^{-4}\) term.

This statement excludes \(\rho=0\), \(v=0\), saddle entry/exit outside the
declared patch, connector ownership changes, and height exhaustion.

## Artificial-pole derivative ledger

For the exact post-endpoint identity

\[
 R_1=\omega G+(1-\omega)R_1-\omega E_1,             \tag{31.8}
\]

any compatible directional derivative gives

\[
 D\{\text{right side}\}=DR_1,
 \qquad D^2\{\text{right side}\}=D^2R_1,            \tag{31.9}
\]

because the coefficients of \(D\omega,D^2\omega\), and the paired second
derivative terms are derivatives of \(G-E_1-R_1=0\). This remains true
after the linear finite-section regularization only when masks, domains,
endpoint conventions, and the combined diagonal/log subtraction are
identical on all three terms.

Thus cutoff differentiation is not the actual obstruction. The missing
quantity is the ordinary derivative of the complete recombined physical
kernel, including its radial endpoint and axial ledgers.

## Rejected shortcut and exact survivor

The actual term (31.2) proves

\[
 \iint |(31.2)|\,d\mu\,dL\asymp_b\lambda^{-1}       \tag{31.10}
\]

on a legal separated cell. Therefore a proof that bounds every
fixed-\(\mu\) product-rule derivative independently cannot reach the
target. Likewise, the smooth family
\(H_T(L,\nu)=Me^{iTL}\nu\) has target pointwise size but regular-part
variation \(\asymp MT\); pointwise \(q^{-2}\) never implies BV.

The smallest remaining statement is now more precise than the Round-30
obligation: form one complete physical-height kernel after exact omega and
endpoint recombination and prove (31.3), together with an integrable weight
uniform in the axial split and joint height exhaustion. Equivalently, in
the divided-difference language one must prove the bound for

\[
 \partial_\nu(\partial_L+\partial_\nu)H_{\rm complete}          \tag{31.11}
\]

only after translation and endpoint recombination, not term by term.

## Evidence assessment

- The statement-only report derives (31.1), the complete moving-endpoint
  and product-rule ledgers, the cutoff cancellation, and the pointwise/BV
  countermodel.
- The hostile audit supplies the actual-profile countercontrol (31.10),
  independently proves the physical-height lemma (31.3)--(31.6), and
  verifies its q-ledger and endpoint signs.
- The discovery report records the same corrected interface and separated
  application. It was conductor-materialized after the assigned task
  exceeded its timebox; it is not counted as independent validation.
- The conductor independently checked the separated physical-height
  calculation, product-symbol scope, and rho Taylor/cutoff ledger.

Promotion relies on the blind/hostile common algebra and conductor checks,
not on vote or on the materialized discovery report.

## State effect

- promote the physical-height finite-section BV implication (31.3)--(31.6);
- promote its separated fixed-\(b\) \(R_1\) application away from axial and
  artificial seams, preserving local \(q^{-2}\);
- extend the exact omega derivative cancellation through second order;
- reject independent absolute control of every fixed-\(\mu\) product-rule
  derivative and reject pointwise-to-BV inference;
- revise the open complete-symbol obligation to the common recombined
  physical-height kernel bound (31.3), axial/radial sides, and joint height
  exhaustion;
- retain the beta transition, double-bounded share, alpha branch, M9-M1,
  M9-M2, M9, and Gauss-circle target as open.
