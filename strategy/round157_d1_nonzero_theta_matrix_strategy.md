# Round 157 strategy: centered nonzero theta matrix

## 1. Accepted starting point

Round 156 proves the complete mandatory theta zero row. Fix an arbitrary
constant \(A>0\) and put

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J_A=M^{3/4}(\log(2X))^A,\qquad K=\sqrt{NM}.
\tag{157.S1}
\]

For every dyadic signed block \(J_A<V\le K\), set

\[
 q=4N,\qquad d\mid N\ \mathrm{odd},\qquad
 c=\frac qd,\qquad H=\frac c2.
\tag{157.S2}
\]

The first open term is

\[
 \mathcal T_{\ne0,U}(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{\substack{v\bmod H\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;c).
\tag{157.S3}
\]

The literal coefficient, both signs, all odd divisor strata, large-\(d\)
folds, complementary frequencies, the asymmetric cell, profile
transitions, zero extension, strict endpoints, and the external
\(B_{1,U}(1)\) seam remain.

## 2. New exact centered interface

Let

\[
 G_N(t)={\bf1}_{N\mid t}\chi_4(t/N),\qquad
 A_j=\widehat B_j(0),
\tag{157.S4}
\]

and define

\[
 B_j^\circ(x)=B_j(x)-\frac{A_j}{q},\qquad
 \sum_{x\bmod q}B_j^\circ(x)=0.
\tag{157.S5}
\]

The complete theta transform is the original quotient selector, while
Round 156 identifies its \(v=0\) contribution. Their exact difference is

\[
 \boxed{
 \mathcal T_{\ne0,U}(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod q}
 B_j^\circ(x)G_N(x^2-j).}
\tag{157.S6}
\]

Equation (157.S6) is the first control to rederive independently. It
shows that the nonzero theta matrix is precisely a centered
short-physical-window quadratic-root discrepancy, not a second
independent spectral object.

For consecutive residue intervals \(I\) and signed defect intervals
\(J\), define the rectangular discrepancy

\[
 \mathscr D_N(I,J)=
 \sum_{j\in J}\sum_{x\in I}G_N(x^2-j)
 -\frac{|I|}{q}\sum_{j\in J}\mathscr S_N(j),
\tag{157.S7}
\]

where

\[
 \mathscr S_N(j)=\sum_{x\bmod q}G_N(x^2-j).
\tag{157.S8}
\]

The strategy is to derive the exact two-parameter Abel or layer-cake
norm of the literal \(B_j^\circ(x)\) and then either prove the required
signed discrepancy bound or identify its first sharp arithmetic barrier.

## 3. Quantitative target and control capacities

The accepted literal amplitude scale is \(M^{-3/4}X^\varepsilon\).
Consequently a centered root-discrepancy theorem of strength

\[
 \sup_{I,J}|\mathscr D_N(I,J)|
 \ll_\varepsilon M^{3/4}X^\varepsilon
\tag{157.S9}
\]

with the exact moving-profile variation cost would close a block.
Any substitute theorem must print its full \(N,M,V,d\) powers after the
exterior normalization and every profile or endpoint norm are restored.

The following are controls, not gains:

1. complete \(v\)-resummation returns the original selector;
2. the \(v=0\) row is already \(M^{-1/4}X^\varepsilon\);
3. sampled Parseval retains all folds modulo \(2N/d\);
4. fixed-\(v\) Abel plus geometric sums gives at best
   \(\min(V\sqrt c,c)\) before the \(v\)-aggregation;
5. one-dimensional Fourier decay of \(\widehat B_j(2dv)\) has an
   \(H\)-sized \(L^1\) capacity; and
6. completion of a single short quadratic interval has a
   square-root-modulus barrier unless a joint signed average is retained.

The round must compute these capacities exactly and may promote only a
strict improvement for the literal coupled object.

## 4. Mechanisms to test

The primary route is the centered physical identity (157.S6).

- Prove the exact mixed \(j\)- and \(x\)-variation or rectangular
  decomposition of \(B_j^\circ\), including the global constant tail
  created by centering.
- Open \(G_N\) only while the \(j\)-interval, physical \(x\)-window, and
  character remain coupled. Test a two-parameter completion, quadratic
  large sieve, van der Corput differencing, dispersion, or root-pair
  argument on (157.S7).
- In the theta coordinate, combine the fixed-\(v\) interval theorem with
  actual \(v\)-frequency decay and complementary-pair symmetry before
  taking an \(L^1\) or \(L^2\) norm.
- Test whether the nonzero projection removes the principal reciprocal
  arc or merely centers it. Both wrapped branches and every large-\(d\)
  fold must remain.
- Compare the centered theorem with the exact selected scalar

\[
 \sup_{I\subset\{n\asymp M\}}
 \left|
 \sum_{\substack{n\in I,\ n\ \mathrm{odd}\\
 V<|j_n|\le2V}}
 \chi_4(n)e(\sqrt{Nn})
 \right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{157.S10}
\]

An equivalence must restore the profile, both signs, cells, transitions,
and endpoint packages.

## 5. Required falsification controls

- arbitrary even composite \(N\) and every odd \(d\mid N\);
- zero row removed exactly once, with no transfer of its theorem to
  \(v\ne0\);
- the global constant tail in \(B_j^\circ\);
- complete versus nonzero versus truncated frequency families;
- literal two-variable coefficient rather than separated bounded weights;
- all \(2N/d\) folds and complementary \(v\)-representatives;
- both wrapped reciprocal-arc branches and principal stationary pieces;
- positive and negative defect blocks, asymmetric cells, transitions,
  and strict endpoints;
- absolute incidence, Cauchy, Parseval, completion, and theorem-right-side
  capacities distinguished from signed estimates;
- fixed modulus distinguished from averaged-modulus sources; and
- no transfer to another owner or global exponent.

## 6. Round tasks and exit rule

Use three orthogonal tasks:

1. derive and attack the centered physical discrepancy with the literal
   mixed-variation norm;
2. blindly rederive the centered identity and seek a selected
   cross-fibre or root-pair theorem; and
3. audit primary fixed-modulus quadratic-root, incomplete theta,
   Kloosterman-bilinear, and spectral large-sieve sources against the
   exact coupled coefficient.

Close under exactly one label:

- outer_defect_nonzero_matrix_target;
- strict_outer_defect_nonzero_matrix_range; or
- outer_defect_centered_discrepancy_no_go.

No next round begins before adjudication and graph validation.

## 7. Downstream scope

Round 157 treats only the nonzero part of the returned
\(D=d=L=1\) outer-defect scalar below the accepted
\(M^{449}\asymp R^{780}\) boundary. Every \(D>1\), \(L>1\), generic
\(t=1\), original \(t\ge2\), cross, remaining M1, and M2 owner remains
separate. Endpoint uniformity, M9, the bridge, the quarter theorem, the
internal exponent \(1/3\), and the audited external Li--Yang exponent
remain unchanged unless separately proved.
