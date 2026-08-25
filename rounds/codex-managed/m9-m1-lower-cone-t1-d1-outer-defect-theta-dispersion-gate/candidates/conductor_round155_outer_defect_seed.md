# Round 155 conductor seed: exact signed outer-defect interfaces

- Campaign: `m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate`
- Role: conductor seed, not accepted mathematics beyond the cited Round 154 graph
- Starting graph: `84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a`

## 1. Selected interface

Fix $A>0$ and a dyadic $V$ with

$$
 M^{3/4}(\log(2X))^A<V\le\sqrt{NM}.
\tag{155.CS1}
$$

The exact selected block, after the accepted linearization, is

$$
 \mathcal Q_U(V)=
 \sum_{\substack{k\ge1,\ -k\le j\le k-1\\
 V<|j|\le2V,\ N\mid k^2-j\\
 (k^2-j)/N\ \mathrm{odd}}}
 \chi_4\!\left(\frac{k^2-j}{N}\right)
 w_U\!\left(\frac{k^2-j}{N}\right)e\!\left(-\frac{j}{2k}\right).
\tag{155.CS2}
$$

The target is $|\mathcal Q_U(V)|\ll_{\varepsilon,A}X^\varepsilon$
uniformly in every literal profile component and both defect signs.

## 2. Ambient interface

With $q=4N$, $d\mid N$ odd, and $q_d=q/d$, the exact pre-linearization
block is

$$
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt{q_d}
 \sum_{v\bmod(q_d/2)}
 \widehat B_j(2dv)K(-v^2,-j;q_d).
\tag{155.CS3}
$$

Here $B_j$ contains the literal cell, piecewise-constant profile extension,
zero extension, actual endpoints, strict dyadic mask, and exact residual
phase. The extension is harmless only after the complete selector is
restored.

## 3. Scale test

The accepted termwise estimate is

$$
 \ll_\varepsilon(M^{-3/4}V+M^{-1/4})X^\varepsilon.
\tag{155.CS4}
$$

Square-root cancellation among $O(VX^\varepsilon)$ selected incidences
would be target-sized for $V\le M^{3/2}$. At the top $V\asymp\sqrt{NM}$,
that alone is sufficient only when $M\asymp N^{1/2}$. A full proof below
that endpoint therefore needs stronger joint structure or a second range.

## 4. First new algebraic test

Before invoking a spectral theorem, expand the theta Kloosterman sum and
the finite Fourier coefficient simultaneously. Determine exactly what
happens if the complete $v\bmod(q_d/2)$ sum is restored. Completing the
$v$-square suggests an inverse-Gauss self-return to the original quadratic
selector. This is not yet promoted: the half-period, multiplier, gcd, and
normalizing constants must be proved. If exact, any gain must arise before
complete $v$-resummation, through a frequency split or the literal
coefficient variation.

## 5. Mandatory separations

- zero versus nonzero dual mode;
- selected versus ambient arrays;
- exact versus linearized residual phase;
- complete versus truncated dual resummation;
- arbitrary coefficient large-sieve capacity versus the actual
  $\widehat B_j(2dv)$; and
- fixed-modulus versus modulus-average source input.

## 6. Open analytical question

Can the actual coefficient be decomposed into a controlled number of
separable or spectrally admissible pieces with a total norm small enough to
beat (155.CS4), without losing the cell, mask, principal reciprocal
subfamily, zero mode, or endpoints? Equivalently, can one prove signed
cross-fibre cancellation directly in (155.CS2)?

## 7. State scope

This seed proposes no graph mutation. It freezes the exact interface for
three orthogonal reports and retains every broader M1, M2, endpoint, M9,
bridge, target, and exponent owner unchanged.
