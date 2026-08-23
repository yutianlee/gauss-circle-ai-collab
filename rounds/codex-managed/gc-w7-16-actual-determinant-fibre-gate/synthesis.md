# Round 117 synthesis: actual phase savings, determinant target still open

Campaign: `gc-w7-16-actual-determinant-fibre-gate`

Round type: graded actual determinant-correlation gate

Starting recorded graph SHA-256:
`a27a89fd4e688cae719a28fec8f48dd74190bafb64d0345c590f1caadc2805d9`

Resulting graph SHA-256:
`d4e626708a04680cc97b043835466948204c6e123a1dc9fd569b50377349feeb`

## 1. Conductor decision

Promote two genuine but insufficient actual-phase estimates and one scoped
determinant-transform obstruction. Retain the complete
\(Y^{1/2+\varepsilon}\) correlation and the all-block local moment as
open.

Round 117 improves the literal minimax block in two certified senses:

- a complete original-variable numerator/product-window argument lowers
  its bound from \(Y^{43/48}\) to \(Y^{37/48+\varepsilon}\);
- on the bounded-lift reduced-denominator shell \(B\asymp D\), reciprocal
  curvature lowers the bound further to \(Y^{35/48+\varepsilon}\).

These are actual-coefficient savings of \(Y^{1/8}\) and \(Y^{1/6}\),
respectively. Neither reaches \(Y^{1/2}\), no target-safe part of the
Round-95 hard region closes, and no pointwise exponent changes.

The exact two-dimensional half-shift transform returns to the same ratio
phase and has a \(Y^{43/48}\) diagonal after standard norms. The cellwise
product representation is likewise invertible; its clean \(r_2/4\)
coefficient exists only after deleting the literal truncations and
profiles. These results park transform-followed-by-norm and clean
completion as standalone closing mechanisms.

## 2. Complete fixed-block product-window estimate

In one random frequency cell, the original numerator interval has length

\[
 T_0\ll\min(L,D/W).
\]

Sampled BV and geometric summation give the M1 factor
\(L^{-1}\min(T_0,\|c/d\|^{-1})\), and the M2 factors with
\(c/(4d)\pm1/4\). If the norm is below \(\eta\), an integer product
\(rd\) lies in an interval of length \(O(1+\eta D)\) about the arbitrary
real centre \(c\). Divisor bounds and layer cake yield total cell amplitude
\(O_\varepsilon(DL^{-1}Y^\varepsilon)\).

The signed frequency band meets \(O(1+WL/D)\) cells, so

\[
 \boxed{
 \mathcal C_i(c),\ |\mathfrak O_i|
 \ll_\varepsilon
 \left({D^2\over L^2}+{WD\over L}\right)Y^\varepsilon.}
\tag{117.S1}
\]

At minimax this is \(Y^{37/48+\varepsilon}\), compared with the prior
coefficient-blind \(Y^{43/48+\varepsilon}\). The proof precedes ray
grouping and therefore contains every lift.

## 3. Bounded-lift top-shell curvature estimate

On \(b,b'\asymp D\), \(|a|,|a'|\asymp L\), all lift sums are finite
with bounded cardinality. Extend each finite-lift weight to nonprimitive
pairs before Möbius inversion. For

\[
 Q_*=\min\left(D,{D^2\over WL}\right),\qquad
 \lambda={YL\over D^3},
\]

the reciprocal phase on a divisor progression has length
\(Q_*/\rho\) and curvature \(\lambda\rho^2\). Weighted van der Corput,
the divisor sums, and the complete outer-ray/increment triangle prove

\[
 \boxed{
 |\mathfrak O_{i,B\asymp D}|
 \ll_\varepsilon D
 \min\left(Q_*,Q_*\sqrt\lambda+\lambda^{-1/2}\right)Y^\varepsilon.}
\tag{117.S2}
\]

At minimax (117.S2) is \(Y^{35/48+\varepsilon}\), rather than
\(Y^{43/48}\). A phase-conjugated shadow cancels the reciprocal phase and
does not satisfy the finite-lift BV mechanism. Thus the saving is literal,
not coefficient-blind.

The first shell seam is \(B<D\): the lift length \(D/B\) grows, and no
uniform transverse variation theorem for the complete lift transform is
proved.

## 4. Half-shift and transform obstruction

With \(p=a'-a\), \(q=b'-b\),

\[
 n=aq-bp,
 \qquad
 {cn\over\kappa_i b(b+q)}
 ={c\over\kappa_i}\left({a\over b}-{a+p\over b+q}\right).
\]

M1 has \(q=2r\) and character \((-1)^r\); M2 has \(p=2s\) and
character \((-1)^s\), with the fixed sign sector retained. A fixed
determinant gives a step-\(2(a,b)\) progression and only \(O(1)\)
comparable-shell points, so the long increment high-pass is transverse to
the determinant fibres.

For the two-dimensional phase \(f\),

\[
 \det\nabla^2f=-{(c/\kappa_i)^2\over(b+q)^4},
\]

and its Legendre phase is

\[
 {ca\over\kappa_i b}+au+bv+{(c/\kappa_i)v\over u}.
\tag{117.S3}
\]

Thus the dual is another ratio phase; the character only half-shifts one
dual coordinate. At \(B\asymp\sqrt Y\), the stationary amplitude is
constant and standard dual norms contain the original
\(Y^{43/48}\) diagonal. The second transform restores the primal phase and
strip. This is a scoped method obstruction, not a lower bound for the
actual coefficients.

## 5. Product return and sources

Numerator Poisson produces

\[
 B_1(s;y)=\sum_{d\mid s}\chi_4(d)F_1(dy,d),\qquad
 B_2(s;y)=\sum_{rd=s}\chi_4(r)F_2(4dy,d).
\tag{117.S4}
\]

The literal coefficients in (117.S4) differ. They both become
\(r_2(s)/4\) only in the unweighted complete positive-divisor model. The
M1 zero-product mode is separately target-safe, with random-cell square
mass at most \(Y^{1/8}\), but the remaining profile and endpoint atoms
must stay inside the exact transform. Poisson inversion returns the full
cell norm, not a positive one-sided off-diagonal estimate.

No exact separable inverse-modular form matching the cited
Kloosterman-fraction theorems was derived. Their hypotheses do not apply to
the real centre, coupled coefficients, variable triangular top, all
determinants, and hard endpoints. Popov remains an aggregate ceiling, not a
fixed-block estimate.

## 6. Proof-state effect

Create proved nodes for (117.S1), (117.S2), and the scoped half-shift
transform-and-norm obstruction. Update the open determinant correlation
and local moment to record the new bounds and the long-lift/joint-signed
survivors.

Reject fixed-fibre long alternation, fibrewise geometric summation without
an actual symbol norm, multiplying the two one-variable gains, a
two-dimensional B-process followed by a norm, clean literal \(r_2/4\)
completion, product-wave positivity, direct Kloosterman-fraction transfer,
and interpreting \(Y^{37/48}\) as the \(Y^{1/2}\) target.

No status change is made to the complete determinant correlation, the
non-subcoherent local moment, either M9 component, endpoint uniformity,
M9, the conditional quarter bridge, or the Gauss-circle target.

## 7. Full-proof strategy after Round 117

The August 21 strategy remains valid, with one refinement: the graded lane
has produced a real coefficient-sensitive saving, so its surviving
prescribed-centre truncated product wave should be tested together with
the planned unbalanced M2 falsification probe. The next round should decide
whether the actual divisor wave admits any uniform pointwise cancellation
or a structural coherent countermodel. It must not repeat an invertible
Poisson completion.

If that probe gives no viable pointwise mechanism, proceed to the bounded
direct minimization of the two M9-M1 parents. Balanced M2 stays parked
behind its complete signed joint alias kernel; hard TOP, BAL, and UNBAL all
remain necessary for M9-M2.
