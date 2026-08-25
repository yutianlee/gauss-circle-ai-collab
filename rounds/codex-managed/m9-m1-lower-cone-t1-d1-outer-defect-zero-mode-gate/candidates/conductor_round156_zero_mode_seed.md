# Round 156 conductor seed: exact theta zero-frequency arithmetic

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate
- Role: conductor seed; only the cited Round-155 graph is accepted
- Starting graph: f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6

## 1. Frozen row

For $q=4N$, every odd $d\mid N$, and $c=q/d$, retain

$$
 \mathcal Z_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,\widehat B_j(0)K(0,-j;c).
\tag{156.CS1}
$$

The target is $O_{\varepsilon,A}(X^\varepsilon)$ beyond every fixed
polylogarithmic defect collar.

## 2. Exact first decomposition

Put $m=N/d$, so $c=4m$. For every odd unit $a$,

$$
 \epsilon_a=\alpha+\beta\chi_4(a),\qquad
 \alpha=\frac{1+i}{2},\qquad \beta=\frac{1-i}{2},
\tag{156.CS2}
$$

and $(4m/a)=(m/a)$. Hence

$$
 \begin{aligned}
 K(0,-j;4m)
 ={}&\alpha\sum_{a\bmod4m}^{*}
 \left(\frac ma\right)e_{4m}(-aj)\\
 &+\beta\sum_{a\bmod4m}^{*}
 \chi_4(a)\left(\frac ma\right)e_{4m}(-aj).
 \end{aligned}
\tag{156.CS3}
$$

This identity is elementary. It is not yet a bound.

## 3. Required local theorem

For each of the two real characters in (156.CS3), determine:

- its primitive conductor, including the exact two-adic exponent;
- the local Fourier transform at every $p^\nu\Vert4m$;
- the valuation conditions on $j$ for nonvanishing;
- the exact magnitude and phase on the surviving support;
- the principal or imprimitive degeneracies when $m$ is squareful; and
- the effect of summing the nested moduli indexed by $d\mid N$.

The result must remain uniform for arbitrary $N$ and both signs of $j$.

## 4. Weighted seam

Even an exact formula for $K(0,-j;c)$ does not prove (156.CS1) unless it
is summed against the actual

$$
 \widehat B_j(0)=\sum_{x\bmod q}B_j(x).
\tag{156.CS4}
$$

Any partial summation must derive the needed $j$-variation from the
literal cell, residual phase, profile transitions, zero extension, and
hard endpoints. Supremum replacement recovers only the accepted upper
capacity.

## 5. Scale ledger

The accepted absolute zero-row bound is

$$
 \left(N^{-1/2}M^{-1/4}V+M^{-1/4}\right)X^\varepsilon.
\tag{156.CS5}
$$

At $V=\sqrt{NM}$ it contains $M^{1/4}$. A successful local-factor or
character-sum argument must remove this power after all $d$-strata and
profile costs are restored.

## 6. Forbidden inferences

Do not assume squarefree $N$, delete $p=2$, identify an induced character
with a primitive one, use Pólya--Vinogradov without its conductor and
weight norms, omit $d=N$ or any principal local factor, call support
sparsity cancellation, or transfer a zero-row result to the nonzero
matrix.

## 7. State scope

This seed makes no graph mutation. The round closes only after three
orthogonal reports and terminal reviews. Every nonzero, broader-owner,
endpoint-assembly, M9, bridge, target, and exponent conclusion remains
separate.

