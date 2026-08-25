# Round 154 strategy: exact root-defect dispersion gate

## Conductor decision

Round 153 closes complete squarefree Mobius inversion plus complete
recombination: it returns the direct large-defect wave and gives no new
range. Round 154 therefore abandons artificial Mobius-block ownership and
moves to a genuinely different arithmetic coordinate attached to the
nearest integer itself.

The single objective is the literal $D=d=L=1$ direct large-defect wave below
$M^{449}\asymp R^{780}$. The new interface is the exact quadratic congruence
between the nearest root $k$ and signed defect $j=k^2-Nn$.

## Frozen exact coordinate

Let

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J=M^{3/4},\qquad 1\ll M\le R^2,
\tag{154.S1}
$$

and let $A_U$ be the inherited literal zero-extended profile. For every
retained positive odd $n$, put

$$
 k=\left\lfloor\sqrt{Nn}+\frac12\right\rfloor,
 \qquad j=k^2-Nn.
\tag{154.S2}
$$

There is no half-integer tie, and the nearest-cell inequalities are exactly

$$
 -k\le j\le k-1.
\tag{154.S3}
$$

Conversely, a positive integer pair $(k,j)$ satisfying (154.S3),
$N\mid k^2-j$, and odd quotient

$$
 n_{k,j}=\frac{k^2-j}{N}
\tag{154.S4}
$$

recovers the original nearest-integer datum. On the fixed-dilate support,
$k\asymp\sqrt{NM}$, the $k$-range has length
$O(\sqrt{NM})<N$, and for large $X$ one has $2k<N$. Thus the congruence
class $j\equiv k^2\pmod N$ contributes at most one $j$ to the nearest cell
for a fixed $k$. Distinct supported integers $n$ have distinct nearest
integers $k$ because their square-root separation is
$\gg\sqrt{N/M}\gg1$.

The Archimedean phase has the exact defect form

$$
 e(\sqrt{Nn_{k,j}})
 =e(\sqrt{k^2-j})
 =e\left(-\frac{j}{k+\sqrt{k^2-j}}\right).
\tag{154.S5}
$$

The character and divisibility may be encoded together, for every integer
$t$, by

$$
 {\bf1}_{N\mid t}\chi_4(t/N)
 =-\frac{i}{2N}
 \sum_{\substack{h\bmod 4N\\h\ \mathrm{odd}}}
 \chi_4(h)e\left(\frac{ht}{4N}\right).
\tag{154.S6}
$$

This identity is exact for every parity and factorization of $N$. It exposes
quadratic phases $e(hk^2/(4N))$ but does not separate the actual quotient
profile, cell, or reciprocal-defect phase.

## Why this is a new interface

The squarefree kernel and its Mobius variables disappear. Cancellation must
now come from the sparse quadratic-residue/root geometry, the exact quotient
character, or a lawful completion/dispersion across $k$, $j$, and the odd
Fourier variable $h$. The phase (154.S5) is bounded after subtracting the
integer $k$, so no derivative gain may be asserted without pricing the
arithmetic sparsity that selected the roots.

The large-defect condition is $|j|>J$. Positive and negative $j$ are kept
separate when needed. The exact and $0<|j|\le J$ sectors remain owned by
Round 152 and may be removed only at scalar level before a positivity step.

## Orthogonal tasks

1. `large_defect_root_dispersion_attack`: derive the exact root-defect sum
   and exhaust quadratic completion, Gauss evaluation, dispersion, Poisson,
   dyadic $j$-ranges, root counts, and signed quotient-character mechanisms.
2. `blind_quadratic_root_wave_feasibility`: from the literal statement only,
   independently derive the coordinate, capacities, diagonals, and first
   feasible or obstructed completion range.
3. `quadratic_root_completion_source_audit`: audit primary incomplete
   quadratic Gauss, Salié/Kloosterman, quadratic-root large-sieve, modular
   parabola, and quotient-character theorems against the literal object.

## Required ledgers

- exact bijection and no-tie proof;
- $k$, $j$, quotient, parity, and support ranges;
- positive and negative defect branches;
- exact modulo-$N$, modulo-$2N$, and modulo-$4N$ character conditions;
- complete and incomplete quadratic Gauss sums, including imprimitive
  $N$, $h$, and every two-adic case;
- actual profile, zero extension, transitions, endpoints, and external
  $B_{1,U}(1)$ seam;
- raw pair count, actual weighted capacity, and signed mass;
- every Cauchy diagonal, exact collision, near collision, and completion
  boundary term;
- the Round-152 owned masks removed only in a lawful order; and
- downstream separation from $D>1$, $L>1$, generic $t=1$, original
  $t\ge2$, the cross owner, M2, endpoint assembly, and global exponents.

## Exit gates

Close under exactly one label:

- `large_defect_root_dispersion_target`;
- `strict_large_defect_root_range`; or
- `large_defect_root_dispersion_no_go`.

A target or strict-range result must include every literal coefficient and
endpoint. A no-go result must identify the first exact completion, Gauss,
root-spacing, quotient-profile, diagonal, source-hypothesis, or power
obstruction. An upper capacity is never a signed lower bound.

Allocation is 100% analytic, algebraic, and primary-source work; no numerical
experiment is planned.
