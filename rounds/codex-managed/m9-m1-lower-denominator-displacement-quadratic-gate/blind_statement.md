# Round 139 statement-only problem: exact denominator-displacement scalar

## 1. Frozen data

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor,\qquad q=N-y^2.
\tag{139.B1}
\]

Then

\[
 0\le q\le2y.
\tag{139.B2}
\]

Let \(\chi_4\) be the primitive real character modulo four and let
\(V_{\rm low}\) be the fixed literal lower profile, with its existing
smooth support and zero-extension conventions.

## 2. Exact scalar and displacement identity

The one-sign integerized lower scalar is

\[
 \mathcal F_N=
 \sum_{d\le y}\chi_4(d)\sum_{h\ge1}\frac1h
 V_{\rm low}(4R^2h^2/d^2)e(hN/d).
\tag{139.B3}
\]

Set

\[
 d=y-v,\qquad 0\le v<y.
\]

The identity

\[
 \frac N{y-v}
 =y+v+\frac{q+v^2}{y-v}
\tag{139.B4}
\]

is exact. Since \(h(y+v)\) is integral,

\[
 \boxed{
 \mathcal F_N=
 \sum_{h\ge1}\frac1h\sum_{0\le v<y}
 \chi_4(y-v)
 V_{\rm low}\!\left(\frac{4R^2h^2}{(y-v)^2}\right)
 e\!\left(h\frac{q+v^2}{y-v}\right).}
\tag{139.B5}
\]

Even \(y-v\) terms vanish. For odd \(y-v\),

\[
 \chi_4(y-v)=e\!\left(\frac{y-v-1}{4}\right),
\]

so the complete physical phase is

\[
 \Psi_{h,q,y}(v)
 =h\frac{q+v^2}{y-v}+\frac{y-v-1}{4}.
\tag{139.B6}
\]

The opposite scalar sign is the complex conjugate.

## 3. Exact quadratic core

There is an exact expansion

\[
 \frac{q+v^2}{y-v}
 =\frac qy+\frac{v^2}{y}
 +\frac{v(q+v^2)}{y(y-v)}.
\tag{139.B7}
\]

Thus a rational quadratic core has phase

\[
 \frac{hq}{y}+\frac{hv^2}{y}-\frac v4+\frac{y-1}{4},
\tag{139.B8}
\]

but its exact correction is

\[
 \mathcal E_{h,q,y}(v)
 =h\frac{v(q+v^2)}{y(y-v)}.
\tag{139.B9}
\]

No task may discard, linearize, freeze, or bound this correction without
a stated displacement range and a complete error ledger.

## 4. Target and capacity

The required estimate is

\[
 \boxed{
 |\mathcal F_N|\ll_\varepsilon RX^\varepsilon}
\tag{139.T}
\]

uniformly for every real \(X\ge2\). The literal scalar has
\(y^{1+o(1)}\) absolute capacity, so the missing gain is a full factor
\(R=y^{1/2}\).

Round 138 already proved a strict scalar-square reduction after deleting
complete denominator rows and both microscopic carrier collars. A claimed
displacement gain must either prove (139.T) for the full scalar or map
exactly to that surviving signed cross-denominator owner.

## 5. Required controls

At minimum test:

- the exact range \(0\le q\le2y\) and both directions of \(d=y-v\);
- odd-denominator parity for both parities of \(y\);
- the literal support relation between \(h\) and \(y-v\), all endpoints,
  zero extension, and both signs;
- the exact correction (139.B9) on every proposed quadratic-completion
  range;
- \(q=0\), \(q=2y\), \(v\) small, \(v\) near \(y\), and fourth-power
  centres;
- half-integer stationary aliases and the known paired-tube capacity;
- every modulus, gcd case, boundary, and completion loss in a Gauss,
  Salié, Weyl, Poisson, or differencing step;
- whether the method is a strict contraction or an invertible return to
  the reciprocal/Farey/Hardy interface;
- the full \(R\)-power ledger and downstream scope.

No displacement-block modulus, arbitrary coefficient theorem, centre
average, positive separated energy, principal-only stationary formula, or
desired Gauss-circle estimate may replace the literal scalar.

## 6. Permitted outcomes

Close under exactly one label:

- target_bound;
- strict_displacement_quadratic_reduction;
- displacement_quadratic_no_go.

A rigorous no-go or a strict owner-complete survivor is useful progress.
Neither licenses lower GAR, a blockwise M1 parent, M9-M1, any M2 parent,
endpoint uniformity, M9, the quarter theorem, or an exponent.

## 7. Report contract

The report must contain exactly seven numbered sections:

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required controls and outcomes.
6. Dependencies and exact artifacts used.
7. Recommended state effect.
