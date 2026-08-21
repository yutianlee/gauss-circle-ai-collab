# Round 96 synthesis: primitive-ray q-dispersion

Starting graph SHA-256:
242a5f0c6cb22d2e9a400bca110a91c08aea3b3cc8c537bc17fd73418df88fd1

## 1. Frozen objective

Round 96 tested whether the exact primitive-ray character

\[
 \chi_4(a)\chi_4(b)=(-1)^q,\qquad
 m=(a+b)/2,\quad q=(b-a)/2,
\]

could yield the missing \(\rho^{-1/2}\) gain in the canonical residual
hard top M2 block before metric density and discrepancy were separated.

The reports are:

- blind statement-only rederivation;
- complete analytic attack;
- hostile mathematical and primary-source audit;
- conductor normalization, capacity, and adjudication reviews.

## 2. Exact accepted reduction

Primitive odd rays correspond exactly to

\[
 0<q<3m/5,\qquad m\not\equiv q\pmod2,\qquad (m,q)=1,
\]

and

\[
 \Lambda=X\bigl(m-\sqrt{m^2-q^2}\bigr),\qquad
 \chi_4(a)\chi_4(b)=(-1)^q=(-1)^{m-1}.
\]

At fixed \(m\), legal shifts have the form \(q\mapsto q+2h\), so their
character autocorrelation is \(+1\); odd shifts have empty support.
A sign-changing shift exists at fixed \(a=m-q\):

\[
 (m,q)\mapsto(m+h,q+h),\qquad b\mapsto b+2h.
\]

Its exact expansion is not a scalar alternating sum. It is a
complete-symbol Fejer Gram with two moving reciprocal intervals, two
lift sets, primitive and owner masks, entry/exit samples, and the
product of the full metric coefficients.

Completing the physical phase gives the joint carrier

\[
 \sum_{r\in\mathbb Z}\widehat W_R(r)
 e\!\left((r-g/2)\Lambda/k\right)\widetilde{\mathfrak C}.
\]

The density mode is in the same half-integral family as every
discrepancy mode. Parity-aware Poisson has a half-spaced dual lattice
which includes zero.

## 3. Capacity and self-return

With

\[
 P\asymp_{X^\varepsilon}L^2\sqrt\rho,\qquad
 E_0\asymp_{X^\varepsilon}LJD^2,\qquad
 \rho=\frac{AJD^3}{L^3},
\]

the separately estimated diagonal in a length-\(H\) dispersion costs

\[
 \frac{P^2}{H},\qquad H\ll D.
\]

Thus diagonal separation and coefficientwise bounds gain at most
\(D^{-1/2}\) linearly and can meet \(\rho^{-1/2}\) only when
\(\rho\ll D\). This is not a proved subrange: the complete signed
off-shift Gram remains open.

The hard cone contains primitive nonsquare \(q=1\) and Pell rows with
\(D\asymp1\) and \(\rho\to\infty\). They show that a uniform proof
cannot rely on growing \(q\)-length. The fourth-power recurrence is a
method control only, not a lower bound for the full coefficient.

Fourier transform in the shift gives the squared modulus of the original
half-frequency row. The adjoint reciprocal transform returns to the
accepted Round-80 transposed two-character row. Plancherel therefore
returns equal capacity. The full physical phase is degree-one
homogeneous and has a radial Hessian null direction; after the saddle,
the \((m,q)\) Hessian of \(\Lambda\) has rank one.

## 4. First strict survivor

For the exact residual row \(F_a(q)\), define

\[
 \mathcal G_H^{\rm act}
 =\sum_{a,n}\left|
 \sum_{0\le h<H}(-1)^hF_a(n+h)\right|^2.
\]

The smallest theorem which would change the canonical state is

\[
 \mathcal G_H^{\rm act}
 \ll_\varepsilon X^\varepsilon\frac{H^2}{\rho}E_0
\]

for some lawful \(H\), or an equivalent direct estimate of the complete
nonzero-shift correlation. Its stationary determinant contains

\[
 \frac{g'}{k'(a+2q+2s)^{3/2}}
 -\frac g{k(a+2q)^{3/2}}.
\]

No current source or accepted internal theorem estimates this locus with
the moving actual symbol, metric density, primitive mask, and physical
entry/exit symbols.

## 5. Controls and source audit

Every frozen control passes for the scoped obstruction: parity, gcd,
moving endpoints, density-discrepancy jointness, orientations, stars,
prior owners, short-\(q\), Pell, fourth-power, false unsigned and
phase-aligned coefficients, exact \(\rho\)-ledger, self-return, and
downstream scope.

The hostile audit found no literal primary-source theorem for the open
Gram estimate. In particular, the radial null direction alone does not
invalidate cone decoupling, but the available cone theorem does not map
the fixed-\(X\), nonseparable, moving complete coefficient.

## 6. Conductor decision

Promote a scoped proved obstruction:

- fixed-\(m\) legal shifts erase the character;
- fixed-\(a\) dispersion is an exact complete Gram lift;
- coefficientwise/diagonal-separated bounds are capped at
  \(D^{-1/2}\);
- the shift and reciprocal transforms return at equal capacity.

Create the exact complete fixed-\(a\) Gram estimate as an open candidate.
Reject claims of automatic alternation, full coefficientwise
\(\rho^{-1/2}\), deleted zero frequency, a nonzero complete Hessian
determinant, or a proved \(\rho\ll D\) wedge.

The canonical density-discrepancy theorem, top signed cone, M9-M2,
M9-M1, M9, and the quarter target remain open.

## 7. Global proof status after Round 96

There is no new global exponent. The strongest certified pointwise
theorem remains the separately repaired external Li--Yang exponent

\[
 \theta_{\rm LY}
 =\frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots,
\]

while the strongest theorem proved entirely through the project's
internal architecture remains exponent \(1/3\). Round 96 makes genuine
negative progress by removing a tempting but equal-capacity M2 route
and isolating the exact determinant-weighted shifted Gram that a
successful successor must estimate.
