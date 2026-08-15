# Conductor rho-seam Taylor ledger

Campaign: `m9-m1-beta-regular-finite-part-symbol-bv`  
Role: conductor residue-seam analysis  
Allocation: 100% analytical/algebraic

## 1. Analytic cancellation before finite-section regularization

Put \(C=\pi i\sqrt X\) and

\[
 I_1(\rho)=\int_1^N x^{\rho-1/2}e(\sqrt{Xx})\,dx,
\]

\[
 E_1(\rho)=\frac{N^\rho e(\sqrt{XN})-e(\sqrt X)}\rho,
 \qquad R_1(\rho)=-\frac{CI_1(\rho)}\rho .           \tag{31.R1}
\]

The accepted endpoint identity is

\[
 CI_1(0)=e(\sqrt{XN})-e(\sqrt X).                   \tag{31.R2}
\]

Hence the numerator of \(G=E_1+R_1\) vanishes at \(\rho=0\), and

\[
 G(0)=e(\sqrt{XN})\log N-CI_1'(0),                  \tag{31.R3}
\]

with analogous finite formulas for its first two rho derivatives in terms
of \((\log N)^k\) and \(I_1^{(k)}(0)\). Thus the apparent pole is removed
analytically before any cutoff or height differentiation.

## 2. Exact cutoff derivative cancellation

For

\[
 \mathcal R=\omega G+(1-\omega)R_1-\omega E_1,
\]

the identity \(G=E_1+R_1\) gives \(\mathcal R=R_1\) meromorphically.
For any directional derivative compatible with the shared domains,

\[
 D\mathcal R=DR_1,
 \qquad D^2\mathcal R=D^2R_1,                       \tag{31.R4}
\]

because every omega-prime or omega-double-prime coefficient is a derivative
of \(G-E_1-R_1=0\). This is exact algebra, not an estimate.

The identity remains valid after the finite-section regular-part operator
only if that linear operator is applied to the combined expression with
the same masks, domains, endpoint conventions, and diagonal/log
subtraction. Separate ownership changes before regularization can destroy
the visible cancellation.

## 3. What Taylor expansion does not prove

Equations (31.R2)--(31.R4) remove the artificial-pole singularity and all
cutoff-derivative losses. They do not establish the Round-31 target norm.
The coefficients in (31.R3) contain radial endpoint terms and
\(I_1^{(k)}(0)\), whose uniform bounds under the joint \(U,V,S\) exhaustion
and the external scale sums are not in the accepted packet. Moreover the
post-endpoint survivor intentionally retains the ledgered meromorphic
\(R_1\) residue, so one cannot simply replace it globally by analytic
\(G\).

The exact next estimate remains the physical-height kernel bound for the
combined regular part:

\[
 |K(L,\nu)|\ll X^\varepsilon\lambda^{-2}w(\nu),
 \qquad |\partial_LK(L,\nu)|\ll
 X^\varepsilon\lambda^{-3}w(\nu),                  \tag{31.R5}
\]

with integrable \(w\), uniform through the rho patch and its endpoint
ledger. Taylor analyticity makes (31.R5) plausible locally but does not
supply its parameter-uniform constants.

## 4. State scope

The rho seam itself is not a derivative obstruction: pole and cutoff
singularities cancel exactly. The remaining issue is quantitative control
of the complete Taylor coefficients, radial sides, and height exhaustion.
No target or complete beta-transition promotion follows here.
