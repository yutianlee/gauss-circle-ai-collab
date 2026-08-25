# Round 141 statement-only problem: incomplete divisor fibres with square-root phase

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad0\le q\le2y,
\]

and fix \(0<\rho<1/8\).  For \(h\ge1\), put

\[
 L_h=\left\lfloor{\rho y\over\sqrt h}\right\rfloor,\qquad
 D_h=y-L_h-1,
\]

and, on every nonempty row, let \(r_h\) be the least positive odd
integer satisfying

\[
 r_h\ge {4Nh\over D_h^2}.
\]

Define the exact incomplete divisor coefficient

\[
 A_\rho(m)=
 \sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\
                  r\ge r_h+2}}\chi_4(r).
\tag{B141.1}
\]

The fixed real function \(V_{\rm low}\) is smooth, compactly supported,
flat at its support boundary, and equal to one near zero.  Empty rows
and profile-zero terms contribute zero.  The frozen scalar is

\[
 \mathfrak T_N
 =\sum_{m\ge1}m^{-3/4}V_{\rm low}(R^2m/N)
 A_\rho(m)e(\sqrt{Nm}).
\tag{B141.2}
\]

Its effective range is \(m\ll N/R^2\asymp y\).  The target is

\[
 \boxed{\mathfrak T_N\ll_\varepsilon X^\varepsilon}
\tag{B141.3}
\]

uniformly for every real \(X\), including every interval on which
\(N=\lfloor X\rfloor\), \(y=\lfloor\sqrt X\rfloor\), and the row floors
are constant.

The following distinctions are mandatory.

- The condition in (B141.1) is height-dependent and exact.  It may not
  be replaced by a rounded cone, by half the divisors, or by the
  complete coefficient \(\sum_{r\mid m}\chi_4(r)\).
- The scalar is signed.  Pointwise divisor bounds, fibrewise absolute
  values, positive energies, random-sign heuristics, or centre averages
  do not prove (B141.3).
- Exact radicals and near radicals are different.  If
  \(N=Du^2\), \(D\) squarefree, then \(Nm\) is a square exactly when
  \(m=Dt^2\); no conclusion about \(Nm\) merely close to a square is
  supplied.
- A phase partition must define its resonance variable, widths,
  multiplicities, endpoints, and weighted capacity before calling a
  set sparse or target-safe.
- The phase \(\sqrt{Nhr}\) is homogeneous of degree one in \((h,r)\)
  and has rank-one Hessian.  A generic nondegenerate two-variable
  curvature theorem is unavailable.
- A second canonical stationary transform may return a reciprocal
  phase.  An invertible reparameterization is not a saving.
- Coherent fourth-power rays and same-sign prime-power fibres are
  controls, not by themselves lower bounds for the full scalar.
- The requested conclusion concerns only (B141.2).  It gives no square
  identity, residual deletion, downstream M1 or M2 theorem, endpoint
  theorem, global quarter theorem, or exponent improvement unless each
  separate implication is proved.

Determine whether (B141.3) follows by an exact signed phase-cell,
near-radical, hyperbola, divisor-pairing, or additive-twist argument.
If it does not, prove the first exact obstruction.  A strict reduction
is useful only if the complement is proved target-safe and the surviving
coefficient, phase, support, and target are stated exactly.
