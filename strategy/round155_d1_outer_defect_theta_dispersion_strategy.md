# Round 155 strategy: signed outer-defect theta dispersion

## 1. Accepted starting point

Round 154 closes the exact nearest-cell algebra, the selected-graph
linearization, and every fixed-polylogarithmic first defect collar. Fix an
arbitrary constant $A>0$ and put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J_A=M^{3/4}(\log(2X))^A,\qquad K=\sqrt{NM}.
\tag{155.S1}
$$

The remaining $D=d=L=1$ scalar is a sum of dyadic signed blocks
$J_A<V\le K$. Up to the accepted target-safe error, a block is

$$
 \mathcal Q_U(V)=
 \sum_{\substack{k\ge1,\ -k\le j\le k-1\\
 V<|j|\le2V,\ N\mid k^2-j\\
 (k^2-j)/N\ \mathrm{odd}}}
 \chi_4\!\left(\frac{k^2-j}{N}\right)
 w_U\!\left(\frac{k^2-j}{N}\right)e\!\left(-\frac{j}{2k}\right),
\tag{155.S2}
$$

with the literal profile, support, endpoints, and sign branches.

## 2. Equivalent ambient interface

Let $q=4N$. For each literal defect $j$, extend the actual profile
piecewise constantly off congruence, retain the exact cell and zero
extension, and place the exact residual phase into $B_j(k)$. Define

$$
 \widehat B_j(b)=\sum_{x\bmod q}B_j(x)e_q(-bx).
\tag{155.S3}
$$

For $d\mid N$, $d$ odd, and $q_d=q/d$, the exact ambient completion is

$$
 \mathcal T_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt{q_d}
 \sum_{v\bmod(q_d/2)}
 \widehat B_j(2dv)K(-v^2,-j;q_d).
\tag{155.S4}
$$

The exact and linearized selected forms differ only by the accepted Round
154 error. Any use of (155.S4) must retain the factor $d\sqrt{q_d}$, the
selector and Fourier normalizations, the zero mode, every gcd stratum,
both signs, and every outer sum.

## 3. Quantitative target

Termwise DFI gives

$$
 |\mathcal T_U(V)|\ll_\varepsilon
 (M^{-3/4}V+M^{-1/4})X^\varepsilon.
\tag{155.S5}
$$

Thus the target requires genuine signed cancellation once
$V\gg M^{3/4}$. A square-root gain in the $O(VX^\varepsilon)$ selected
incidences would give $M^{-3/4}V^{1/2}$ and therefore close the strict
positive-power range

$$
 V\le M^{3/2}.
\tag{155.S6}
$$

It would not by itself close the top $V\asymp K$ unless $M\asymp N^{1/2}$.
Every claimed gain must print its exact $N,M,V,d$, and dual-frequency
powers after all normalizations and outer variables are restored.

## 4. New mechanisms to test

The primary route is a coefficient-sensitive joint transform, not another
termwise Kloosterman estimate. Expand the theta multiplier only while the
literal $\widehat B_j(2dv)$ remains present; test whether discrete
summation in $j$, a partial $v$-decomposition, Poisson, Kuznetsov, a
spectral large sieve, or a two-variable van der Corput step exposes a
signed transform of the actual coefficient.

Separately test the selected form (155.S2). The phase is now linear in the
defect for fixed $k$, but the congruence selects a sparse modular parabola
and, for odd $N$, $\chi_4((k^2-j)/N)$ is constant in a fixed-$j$ root
fibre. Any character saving must therefore survive the outer $j$ order.

The $v=0$ term must be isolated before a nonzero-mode spectral claim. A
complete expansion and unrestricted resummation of every $v$-mode risks
inverting the Gauss transform and returning the original selector; this
possible self-return must be proved or bypassed, not ignored.

## 5. Required falsification controls

- arbitrary even composite $N$ and every odd $d\mid N$;
- positive and negative defect blocks and the literal asymmetric cell;
- the exact actual coefficient rather than separated surrogate weights;
- zero mode versus nonzero modes;
- complete versus truncated $v$-summation;
- principal reciprocal stationary subfamily and endpoint terms;
- Parseval, Cauchy, diagonal, and complete-sum capacities distinguished
  from signed estimates;
- fixed modulus distinguished from modulus-average source theorems; and
- strict scalar mask restoration distinguished from deletion inside a
  correlation.

## 6. Round decision rule

Promote only one of:

1. the full bound $|\mathcal Q_U(V)|\ll_\varepsilon X^\varepsilon$ for
   every $J_A<V\le K$;
2. a strict owner-complete power range beyond the logarithmic collar, with
   all complementary blocks and endpoints explicitly left open; or
3. a rigorous first obstruction for the exact coefficient-sensitive
   theta-dispersion or selected cross-fibre placement.

No theorem or exponent changes from an upper-capacity calculation, a
source analogy, an averaged-modulus result, or a separated-coefficient
model.

## 7. Downstream scope

Round 155 treats only the returned $D=d=L=1$ outer-defect scalar below the
accepted $M^{449}\asymp R^{780}$ boundary. The $D>1$ recovery fibre,
$L>1$ rows, generic $t=1$ sector, every original $t\ge2$ layer, the
Round-138 cross owner, remaining M1 and all M2 owners, endpoint uniformity,
M9, the bridge, and both global exponents remain outside the round.
