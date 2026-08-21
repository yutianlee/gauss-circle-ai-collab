# Round 96 conductor review: capacity, controls, and scope

Starting graph SHA-256:
242a5f0c6cb22d2e9a400bca110a91c08aea3b3cc8c537bc17fd73418df88fd1

## Capacity normalization

The accepted per-ray envelope and ray count give

\[
 M_0\ll_\varepsilon X^\varepsilon\sqrt{GJD},\qquad
 N\asymp AD,
\]

and therefore

\[
 P=NM_0\asymp_{X^\varepsilon}L^2\sqrt\rho,\qquad
 E_0=NM_0^2\asymp_{X^\varepsilon}LJD^2,
\]

with

\[
 \rho=\frac{AJD^3}{L^3}.
\]

For the exact fixed-\(a\) Fejer Gram \(\mathcal G_H^{\rm act}\), Cauchy
and the zero-shift term give the separately estimated contribution

\[
 |\mathfrak Q|^2\ll \frac{P^2}{H},\qquad H\ll D.
\]

Thus a proof which bounds the diagonal separately and takes absolute
values in the other shifts gains at most \(D^{-1/2}\) linearly. It can
match the required \(\rho^{-1/2}\) only when \(\rho\ll D\).

This conclusion is deliberately scoped. The exact Gram is a square,
and signed nonzero correlations can cancel its expanded diagonal.
Consequently the calculation does not prove that every actual-symbol
A-process fails. It proves that character parity, coefficientwise
Cauchy, a separately owned diagonal, or transform unitarity cannot
establish the desired estimate. The still-open theorem is

\[
 \mathcal G_H^{\rm act}
 \ll_\varepsilon X^\varepsilon\frac{H^2}{\rho}E_0
\]

for some lawful \(H\), or an equivalent direct bound for the complete
off-shift correlation.

## Short-fibre control

For every even \(m>2\),

\[
 (a,b)=(m-1,m+1),\qquad q=1,\qquad ab=m^2-1
\]

is primitive, odd, and nonsquare. The Pell subfamily
\(m^2-3n^2=1\) gives \(ab=3n^2\), including \((a,b)=(25,27)\).
Taking \(A\asymp L\ll J^{1/2}\) leaves
\(\rho\asymp J/L^2\to\infty\) while \(D\asymp1\). The hostile
fourth-power recurrence verifies that strict metric support can recur
infinitely often at fixed metric scale. It is only a route control:
no lower bound for the complete physical coefficient, and hence no
counterexample to the canonical theorem, is claimed.

## Curvature and self-return

At fixed physical variable, the \((m,q)\) Hessian is nonsingular, but
the complete three-variable phase is homogeneous of degree one and has
a radial Hessian null vector. After eliminating the physical saddle,

\[
 \nabla^2_{m,q}\Lambda
 =\frac X{(m^2-q^2)^{3/2}}
 \begin{pmatrix}q^2&-mq\\-mq&m^2\end{pmatrix}
\]

has rank one. This does not rule out cone decoupling; it rules out a
determinant-only import that ignores the complete moving symbol.

Fourier transformation of the exact shift Gram gives the squared
modulus of the original half-frequency row. Parity-aware Poisson
retains zero frequency, and the adjoint reciprocal transform returns to
the accepted Round-80 transposed two-character row. Plancherel alone
therefore gives equal capacity.

## Mandatory controls

The three reports pass all frozen controls:

- exact parity, coprimality, and both shift directions;
- independently moving \(k\)-intervals, lift sets, and entry/exit;
- density and discrepancy kept jointly;
- both orientations, one outer \(2\Re\), floors, stars, and owners;
- square rays and exact nonsquare centres not reinserted;
- short-\(q\), Pell, near-square, and fourth-power controls;
- false unsigned and phase-aligned coefficient analogues;
- exact \(\rho\)-power and block-sum nonimplication;
- transform self-return and downstream scope.

The hostile report audits primary sources only negatively. No external
theorem is imported into the internal no-go.

## Review verdict

Promote the coefficientwise/one-step capacity obstruction and exact
self-return. Do not promote the formal wedge \(\rho\ll D\), the Gram
estimate, the canonical M2 cone, M9-M2, M9, or the quarter target.
