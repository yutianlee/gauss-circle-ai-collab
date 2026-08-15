# Round 30 synthesis: the logarithmic face is safe; the regular symbol norm remains

Campaign: `m9-m1-beta-log-amplitude-two-saddle`  
Round type: beta logarithmic-amplitude two-saddle estimate  
Graph SHA-256 before patch: `23a3c1929047ab40a0a67d07a4de96a7943ce3b83a8beec35ff433d933038be2`

## Conductor decision

Round 30 proves the singular stationary theorem needed after Round 29 and
shows that the actual logarithmic height face is not the local bottleneck.

For a uniformly nondegenerate one-dimensional saddle, a moving amplitude

\[
 g(t)\Log(a+i(t-t_0))
\]

has oscillatory size

\[
 \boxed{
 O\!\left(\Lambda^{-1/2}\log(2+\Lambda)
 (\|g\|_\infty+\|g'\|_1)\right)}                   \tag{30.1}
\]

in canonical coordinates. It is uniform as the log point, saddle, and
integration endpoint coalesce, and for either Hessian sign. The logarithm
is sharp: at exact saddle coincidence it multiplies the full incomplete
Fresnel coefficient, or its half-Fresnel endpoint version.

In the beta scaling, the ordinary stationary width is
\(\sqrt\lambda\), so (30.1) adds one logarithm but no algebraic power. The
delta trace is a step/BV amplitude and costs only the ordinary Fresnel size.

More importantly, the actual separated \(R_1\) face coefficient is two
inverse powers better than the accepted bulk. If

\[
 A=\rho_0-i\alpha,qquad y=L-\nu,
\]

then

\[
 \frac1{y(A+iy/2)}=\frac1A\frac1y
 -\frac{i}{2A}\frac1{A+iy/2}.                       \tag{30.2}
\]

At a saddle-face collision, \(|L|\asymp|\alpha|\asymp\lambda\), the
actual height transform gives \(f_b(L)=O_b(\lambda^{-3})\) and
\(|A|\asymp\lambda\). Thus the explicit log coefficient is
\(O_b(\lambda^{-4})\). After the accepted stationary numerator
\((D_j/q)\lambda\), the face contribution is

\[
 O_b\!\left(\frac{D_j}{q\lambda^3}\log(2+\lambda)\right)
 =O_b\!\left(
 \frac{D_j\log(2+\lambda)}{q^4\theta_j(x)^3}\right). \tag{30.3}
\]

This is locally \(q^{-4}\), whereas the regular finite part carries the
accepted \(q^{-2}\) capacity.

The full beta transition is not proved. The exact survivor is now a
scale-normalized BV/symbol estimate for the regular finite part of the
complete recombined numerator, including moving endpoint traces, masks,
the \(\rho=0\) package, and height tails. Pointwise value bounds cannot
replace this norm; a phase-cancelling bounded-amplitude adversary proves
that variation control is essential.

Round 30 used no numerical experiment and no external theorem.

## Exact abstract moving-logarithm lemma

Fix a compact interval and let \(\phi\) have one uniformly nondegenerate
critical point, possibly at an endpoint. After the exact Morse coordinate,
it suffices to prove

\[
 \left|\int_p^qG(t)\Log(a+i(t-r))e^{\pm i\Lambda t^2/2}dt\right|
 \ll \Lambda^{-1/2}\log(2+\Lambda)
 (\|G\|_\infty+\|G'\|_1),                           \tag{30.4}
\]

uniformly for moving \(p,q,r\) in a fixed compact set and
\(0\le a\le1\).

Put \(h=\Lambda^{-1/2}\). On the union

\[
 |t|\le2h\quad\text{or}\quad |t-r|\le2h,
\]

take absolute values and use the uniform local mass

\[
 \int_I|\Log(a+i(t-r))|dt\ll h\log(2/h)              \tag{30.5}
\]

for intervals \(I\) of length \(O(h)\). On each complementary component,
integrate by parts with \((\pm i\Lambda t)^{-1}d/dt\). The only new term is

\[
 \frac1\Lambda\int
 \frac{dt}{|t|\,|t-r|}\ll h,                       \tag{30.6}
\]

after the two \(h\)-neighborhoods are removed. Boundary and amplitude
derivative terms cost \(h\log(2/h)\). This proves (30.4), including moving
endpoints and either Hessian sign.

At \(r=0\), \(a=0\), and a saddle at zero, scaling
\(t=y/\sqrt\Lambda\) gives the leading term

\[
 -\frac12\Lambda^{-1/2}\log\Lambda
 \times\{\text{ordinary incomplete Fresnel coefficient}\}.  \tag{30.7}
\]

Thus the log loss is sharp. A saddle at an endpoint yields exactly half the
full Fresnel coefficient.

## Exact finite-section decomposition

Let

\[
 I_{U,V}(L)=[-V,V]\cap[L-U,L+U],
\]

and in \(\mu=L-\nu\) coordinates set

\[
 A(L)=\max(-U,L-V),\qquad B(L)=\min(U,L+V).
\]

For \(h_0(L)=H(L,L)\), the distribution-first kernel is

\[
 {\cal C}_{U,V}H(L)=h_0(L)J_{U,V}(L)+R_{U,V}(L),     \tag{30.8}
\]

where

\[
 J_{U,V}(L)=\pi\mathbf1_{A<0<B}
 -i\log\frac{|B(L)|}{|A(L)|},                       \tag{30.9}
\]

and

\[
 R_{U,V}(L)=-i\int_{A(L)}^{B(L)}
 \frac{H(L,L-\mu)-H(L,L)}\mu\,d\mu.               \tag{30.10}
\]

Equivalently, for

\[
 \Log_-(x)=\log|x|-i\pi\mathbf1_{x<0},
\]

the constant-numerator Plemelj kernel is

\[
 J_{U,V}(L)=-i\{\Log_-(B(L))-\Log_-(A(L))\}.        \tag{30.11}
\]

This fixes the delta/PV sign. Only \(L=\pm V\) gives top-pole face
logarithms. The \(|L-\nu|=U\) faces are affine switches or ordinary
endpoints; the section collapses at \(L=\pm(U+V)\).

On each affine cell, a sufficient BV norm for the regular part is

\[
 \begin{aligned}
 {\mathfrak B}(H)=
 &\sup_L\int_{A(L)}^{B(L)}
 (|\Delta_H(L,\mu)|+|\partial_L\Delta_H(L,\mu)|)d\mu\\
 &+\sum_{\gamma=A,B}\int
 |\Delta_H(L,\gamma(L))|dL,                         \tag{30.12}
 \end{aligned}
\]

where

\[
 \Delta_H(L,\mu)=\frac{H(L,L-\mu)-H(L,L)}\mu.
\]

Then

\[
 \|R_{U,V}\|_\infty+\operatorname {Var}R_{U,V}
 \ll{\mathfrak B}(H).                               \tag{30.13}
\]

For the fixed height profile alone this quotient is benign: one
\(L\)-derivative is controlled by a second derivative of
\(f_b\), and the accepted transform decay makes the endpoint traces
summable. The project-specific issue is that the complete numerator has
many additional \(L\)-dependent factors.

## Actual two-denominator face algebra

For the separated \(R_1\) height model,

\[
 H(L,\nu)=\frac{f_b(\nu)}
 {\rho_0-i(\nu+\alpha+\beta)/2},
 \qquad L=\alpha-\beta.
\]

Putting \(y=L-\nu\) gives \(A+iy/2\) in the second denominator. The exact
identity (30.2) yields

\[
 \begin{aligned}
 \frac{f_b(L-y)}{y(A+iy/2)}={}&
 \frac{f_b(L)}{Ay}
 -\frac{i f_b(L)}{2A(A+iy/2)}\\
 &+\frac{f_b(L-y)-f_b(L)}{y(A+iy/2)}.                \tag{30.14}
 \end{aligned}
\]

The first term, together with the delta trace, contains the entire explicit
face logarithm. The other two terms are regular at \(y=0\). At either
signed saddle-face collision,

\[
 \frac{f_b(L)}A=O_b(\lambda^{-4}),                   \tag{30.15}
\]

proving (30.3). No cancellation between the two saddle signs is used.

The regular finite part should have pre-numerator size
\(O_b(\lambda^{-2})\) away from the artificial seam. If its *scaled BV
norm* has that size uniformly, the abstract Fresnel lemma yields

\[
 \frac{D_j}{q\lambda}\log(2+\lambda)
 =\frac{D_j\log(2+\lambda)}{q^2\theta_j(x)},         \tag{30.16}
\]

which remains absolutely summable in \(q\). This implication is
conditional: Round 27 proves a separated value estimate, not the norm in
(30.12) for the complete recombined amplitude.

## Smallest surviving symbol lemma

After exact Morse scaling on each signed saddle component, let
\({\cal B}_{j,h,q,x}^{\pm}\) denote the complete regular finite-part
amplitude after removing the explicit face logs and delta jumps. The next
smallest statement is

\[
 \boxed{
 \|{\cal B}\|_\infty+\|\partial_y{\cal B}\|_1
 \ll_{b,W,\phi}X^\varepsilon\frac{D_j}{q\lambda}
 \times\{\text{the accepted }h,D_j,x\text{ monomial}\}.}     \tag{30.17}
\]

It must hold uniformly through:

- saddle entry and exit and every affine polytope cell;
- beta connectors and moving endpoint traces;
- the artificial-pole-safe combination
  \(\omega G+(1-\omega)R_1-\omega E_1\);
- the \(v=0\) axial seam and fixed \(b\downarrow0\) losses;
- finite height tails and all actual profiles, floors, and stars.

A pointwise bound cannot imply (30.17): the bounded adversarial amplitude
\(e^{-i\Psi}\) cancels the oscillation and has length-size capacity, while
its variation records exactly the missing cost.

Even after (30.17), the \(U,V,S\) exhaustion, outside sides, and complete
\(h,D_j,x\) sums must still be carried out. The double-bounded share and
the alpha-bounded transition remain separately open.

## Evidence assessment

- The statement-only report independently proves (30.4), both Hessian
  signs, every saddle/log/endpoint coalescence, sharpness, and the
  finite-section logarithm decomposition.
- The discovery report proves (30.8)--(30.15), audits the local q-ledger,
  and isolates (30.17) as the first actual-profile gap.
- The hostile audit independently proves the abstract bound and sharpness,
  verifies the Plemelj signs and (30.2), confirms local \(q^{-4}\) for the
  face log, and supplies the phase-cancelling amplitude falsifier.
- The conductor independently derived the same abstract lemma, actual
  partial fraction, face coefficient, and regular-symbol interface.

The promoted claims are common exact algebra and proofs, not a majority
inference. The actual symbol estimate and complete beta bound remain open.

## State effect

- promote the abstract sharp moving-logarithm Fresnel lemma;
- promote the exact finite-section delta/PV logarithm and regular-part
  decomposition;
- promote the separated actual \(R_1\) face-log estimate (30.3), scoped
  away from the artificial and axial seams;
- revise the beta logarithmic-kernel obligation: singular face control is
  complete, while the regular finite-part symbol norm (30.17), tails, and
  full sums remain;
- reject using a bounded value estimate as a scaled BV estimate;
- create (30.17) as the next open actual-profile symbol obligation;
- retain the beta transition, swept operator, M9-M1, M9-M2, M9, and Gauss
  target as open.

