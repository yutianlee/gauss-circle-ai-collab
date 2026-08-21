# Conductor working audit: q-curvature and homogeneity

Campaign: `m9-m2-primitive-ray-q-dispersion`

Starting graph SHA-256:
`242a5f0c6cb22d2e9a400bca110a91c08aea3b3cc8c537bc17fd73418df88fd1`

This is conductor working evidence, not accepted mathematics before the
Round-96 seam gates close.

## Exact primitive coordinates

For primitive odd \(a<b\), set

\[
 m=(a+b)/2,qquad q=(b-a)/2.
\]

Then \((a,b)=1\) is equivalent to \((m,q)=1\) together with opposite
parity, and \(a<b<4a\) is equivalent to \(0<q<3m/5\). Moreover

\[
 \chi_4(a)\chi_4(b)=(-1)^q.
 \tag{96.C1}
\]

Writing \(s=\sqrt{m^2-q^2}\), the half-angle quantities simplify to

\[
 u=\frac{q}{m+s}=\frac{m-s}{q},
 \qquad
 \Lambda=Xqu=X(m-s).
 \tag{96.C2}
\]

Hence

\[
 \Lambda_q=\frac{Xq}{s},qquad
 \Lambda_{qq}=\frac{Xm^2}{s^3},qquad
 \Lambda_{qqq}=\frac{3Xm^2q}{s^5}.
 \tag{96.C3}
\]

Large real curvature in (96.C3) is not by itself lattice cancellation;
the fractional derivative is uncontrolled and is coherent on accepted
perfect-power controls.

## Complete integral phase

Before stationary phase, the phase-removed complete coefficient is

\[
 g\int A^\circ_{ga,gb}(gu)
 e\!\left(g[k u-J\delta(m,q)\sqrt u]\right)du,
 \qquad
 \delta(m,q)=\sqrt{m+q}-\sqrt{m-q}.
 \tag{96.C4}
\]

Including the character gives the q-phase

\[
 \phi(q)=q/2-gJ\delta(m,q)\sqrt u.
 \tag{96.C5}
\]

On \(m\asymp A\), \(q\asymp D\), \(u\asymp A\), and
\(g\asymp G=L/A\),

\[
 |\phi''(q)|\asymp \lambda
 :=\frac{LJD}{A^3}.
 \tag{96.C6}
\]

Since

\[
 \rho=\frac{AJD^3}{L^3},
 \qquad G=L/A,
\]

one has the exact scale relation

\[
 \lambda D^2\asymp \rho G^4.
 \tag{96.C7}
\]

The ordinary weighted second-derivative estimate would give, relative
to the trivial q-length \(D\),

\[
 \frac{|S_q|}{D}
 \ll \frac{G^2\sqrt\rho}{D}
     +\frac{1}{G^2\sqrt\rho}.
 \tag{96.C8}
\]

The second term is target-sized, but the first reaches the required
\(\rho^{-1/2}\) only if

\[
 D\ge G^2\rho
 \quad\Longleftrightarrow\quad
 JD^2\le AL.
 \tag{96.C9}
\]

Combining (96.C9) with the hard condition \(AJD^3>L^3\) requires

\[
 A^5>L^3J.
 \tag{96.C10}
\]

But the accepted top support has \(A\le L\le J^{1/2}\), so (96.C10)
has no open polynomial range; equality can occur only at the degenerate
boundary \(A=L=J^{1/2}\), \(D\asymp1\). Thus a bare one-dimensional
second-derivative estimate in q cannot supply the canonical gain.

This is a route-specific capacity calculation, not a proof that every
q-dispersion or joint signed estimate fails.

## Exact shift lattice and the one-step ceiling

At fixed \(m\), admissibility forces \(q\) to have the parity opposite
to \(m\).  Hence every nonempty autocorrelation shift is

\[
 q\longmapsto q+2h,
 \qquad
 (-1)^{q+2h}(-1)^q=1.
 \tag{96.C10a}
\]

Thus the primitive character gives no sign in the fixed-\(m\)
correlation.  Odd shifts have empty support rather than a negative
character correlation.

One may instead fix \(a=m-q\) and move

\[
 (m,q)\longmapsto(m+h,q+h).
 \tag{96.C10b}
\]

This preserves odd \(a,b\) and contributes the correlation sign
\((-1)^h\).  It is a genuine cross-ray direction, but a single Fejer or
van der Corput step along a fibre of length \(D\) still contains its
positive zero-shift energy.  Even if every nonzero shift were disposed
of without loss, the diagonal term permits at most the relative gain

\[
 H^{-1/2}\leq D^{-1/2}.
 \tag{96.C10c}
\]

Consequently a one-step argument can supply the required
\(\rho^{-1/2}\) uniformly only in the subrange \(\rho\leq D\).  The hard
support contains \(D\asymp1\), \(A\asymp L\ll J^{1/2}\), for which
\(\rho\asymp J/L^2\to\infty\); near-square and Pell controls show that
such short fibres are not empty after the previously accepted owners
are removed.  The sign in (96.C10b) therefore does not close the
canonical block.  Removing the diagonal would require a new signed
row-energy identity, not merely ownership language for the original
diagonal.

## Rank and self-return diagnostic

At fixed \(u\), the Hessian of \(\delta\) in \((m,q)\) is

\[
 \begin{pmatrix}
 A_0&B_0\\B_0&A_0
 \end{pmatrix},
 \quad
 A_0=\frac1{4(m-q)^{3/2}}-\frac1{4(m+q)^{3/2}},
 \quad
 B_0=-\frac1{4(m-q)^{3/2}}-\frac1{4(m+q)^{3/2}},
 \tag{96.C11}
\]

and

\[
 \det\nabla^2_{m,q}\delta
 =-\frac1{4(m^2-q^2)^{3/2}}.
 \tag{96.C12}
\]

Thus the two primitive variables have nonzero fixed-u curvature.
However the complete phase

\[
 F(m,q,u)=ku-J\delta(m,q)\sqrt u
 \tag{96.C13}
\]

is homogeneous of degree one under
\((m,q,u)\mapsto t(m,q,u)\). Euler's identity therefore gives a radial
null direction for its full three-variable Hessian. After eliminating
the u-saddle, the reduced phase is proportional to
\(\Lambda/k=X(m-\sqrt{m^2-q^2})/k\), whose \((m,q)\) Hessian has rank
one by degree-one homogeneity.

Any two-dimensional Poisson or stationary argument must therefore show
why it is not merely another representation of this radial/adjoint
self-return. A determinant-only theorem cannot be imported at the
complete-symbol level without resolving this seam.

## First conductor questions

1. Can a q-shift be paired with the lift/radial direction so that the
   homogeneous null direction is removed rather than completed?
2. Can the short-q/Pell blocks be owned separately without reintroducing
   the full positive capacity?
3. Does the actual profile have uniform q-shift BV through its moving
   lift support and two physical collars?
4. Is there a joint character estimate that acts before u-stationary
   reduction and beats the route-specific obstruction (96.C8)?

No canonical estimate or graph change is claimed in this working note.
