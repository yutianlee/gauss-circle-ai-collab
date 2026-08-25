# Round 153 discovery report: exact Mobius collapse of the squarefree-kernel bilinear family

- Campaign: `m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate`
- Task: `squarefree_mobius_bilinear_attack`
- Role: discovery
- Starting graph SHA-256: `9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1`
- Allocation used: 100% analytic/algebraic; 0% numerical
- Proposed terminal label: `squarefree_kernel_bilinear_no_go`

## 1. Result: exact truncated-divisor collapse and scoped no-go

Let

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 1\ll M\le R^2,\qquad S_\star=\lceil M^{1/4}\rceil,
\tag{153.D1}
$$

and remain in the unowned range $M^{449}\ll R^{780}$.  Define the
literal large-defect weight

$$
 F_U(n):={\bf1}_{n>0\ \operatorname{odd}}\,\chi _4(n)n^{-3/4}A_U(n)
 e(\sqrt{Nn})
 {\bf1}_{\{|k(n)^2-Nn|>M^{3/4}\}},
\tag{153.D2}
$$

where $A_U$ is the inherited zero-extended actual profile, including all
support components and half-open endpoint conventions, and
$k(n)=\lfloor\sqrt{Nn}+1/2\rfloor$.  In particular, the character
$\chi _4(n)$ is part of $F_U(n)$.

The exact Round-152 survivor satisfies

$$
 P_U^*=\sum_{\substack{s<S_\star\\s\ \operatorname{odd}}}
       \sum_{\tau\ \operatorname{odd}}\mu^2(\tau)F_U(\tau s^2).
\tag{153.D3}
$$

For odd $r$, put

$$
 C_{S_\star}(r):=
 \sum_{\substack{a\mid r\\r/a<S_\star}}\mu(a).
\tag{153.D4}
$$

Then finite exact reindexing gives

$$
 \boxed{
 P_U^*=\sum_{r\ \operatorname{odd}}C_{S_\star}(r)
                 \sum_{b\ \operatorname{odd}}F_U(r^2b).}
\tag{153.D5}
$$

For $r<S_\star$ every divisor $a\mid r$ is admitted in (153.D4), so

$$
 C_{S_\star}(r)=\sum_{a\mid r}\mu(a)={\bf1}_{r=1}
 \qquad(r<S_\star).
\tag{153.D6}
$$

Moreover, the complete boundary $r\ge S_\star$ is absolutely target-safe:

$$
 \sum_{\substack{r\ge S_\star\\r\ \operatorname{odd}}}
 |C_{S_\star}(r)|
 \sum_{b\ \operatorname{odd}}|F_U(r^2b)|
 \ll_\varepsilon X^\varepsilon.
\tag{153.D7}
$$

Consequently, if

$$
 P_U^{\rm LD}:=\sum_{b\ \operatorname{odd}}F_U(b),
\tag{153.D8}
$$

then

$$
 \boxed{P_U^*=P_U^{\rm LD}+O_\varepsilon(X^\varepsilon)
       =P_U+O_\varepsilon(X^\varepsilon).}
\tag{153.D9}
$$

The second equality uses only the already accepted exact-square and
nonzero-small-defect owners.  Thus complete squarefree Mobius inversion
does not produce a new bilinear object: after the necessary cancellation
between every $a$, every small product $r=as>1$ vanishes exactly, the
$r=1$ term is the original large-defect character wave, and the remaining
$r\ge S_\star$ boundary is absolutely safe.  In particular the
$a=s=1$ face cannot be removed by a Type-I/Type-II partition.

This is an all-scale **method no-go for treating the artificial Mobius
blocks as independent owners**, not a lower bound for the signed sum and
not an impossibility theorem for a future estimate of $P_U$.  No new
strict $M$-range and no proof of $|P_U^*|\ll_\varepsilon X^\varepsilon$
is obtained below $M^{449}\asymp R^{780}$.

## 2. Exact statement and hypotheses

The result above uses the following literal hypotheses and no others.

1. $N=\lfloor X\rfloor$, $R=X^{1/4}$, $1\ll M\le R^2$, and the
   already owned range $M^{449}\gg R^{780}$ is excluded.
2. $A_U$ is the Round-148/Round-152 actual profile, extended by zero.
   Its support is contained in a fixed dilation of $n\asymp M$, with

   $$
   \|A_U\|_\infty+\operatorname {Var}A_U
   \ll_\varepsilon X^\varepsilon.
   \tag{153.D10}
   $$

   Every actual component, transition, tail, prefix, and half-open
   endpoint remains encoded in the same value $A_U(r^2b)$ after every
   reindexing.
3. Every integer is positive and odd unless explicitly stated.  The
   unique factorization $\ell=\tau s^2$ has $\tau$ squarefree and $s$
   odd, but **does not impose $(\tau,s)=1$**.  For example, an odd prime
   may divide both when its exponent in $\ell$ is at least three.
4. The strict cutoff is exactly $s<S_\star$ with
   $S_\star=\lceil M^{1/4}\rceil$.  The equality $s=S_\star$ is not
   silently included.  Bounded $M$, for which endpoint asymptotics could
   be vacuous, is already target-safe.
5. The nearest integer and strict defect mask are those in (153.D2).
   There is no half-integer tie: for odd $n$, a tie would imply
   $4Nn=(2j+1)^2$, impossible modulo four.
6. The external coefficient $B_{1,U}(1)$ is not part of $F_U$ or of the
   Mobius inversion.  It stays outside the wave with its accepted
   $O_\varepsilon(X^\varepsilon)$ bound.

The fixed-$s$ identity required by the brief is, with no coprimality
inserted,

$$
\boxed{
\begin{aligned}
 P_{U,s}^*
 ={}&\sum_{a,b\ \operatorname{odd}}
 \mu(a)\chi _4(b)(a^2bs^2)^{-3/4}A_U(a^2bs^2) \\
 &\quad\times e(as\sqrt{Nb})
 {\bf1}_{\{|k(a^2bs^2)^2-Na^2bs^2|>M^{3/4}\}} .
\end{aligned}}
\tag{153.D11}
$$

All sums in (153.D3), (153.D5), and (153.D11) are finite because of the
zero-extended support.  Hence their reordering needs no convergence
hypothesis.

## 3. Proof and complete bilinear audit

### 3.1 Exact inversion, character, and the $a=1$ seam

To use Mobius inversion one must first replace the squarefree restriction
by its indicator:

$$
 \sum_{\tau\ \operatorname{odd\ squarefree}}(\cdots)
 =\sum_{\tau\ \operatorname{odd}}\mu^2(\tau)(\cdots),\qquad
 \mu^2(\tau)=\sum_{a^2\mid\tau}\mu(a).
\tag{153.D12}
$$

If the condition ``$\tau$ squarefree'' were retained while (153.D12)
was inserted, only $a=1$ could occur and there would be no bilinear
family.  In the correct unrestricted sum write $\tau=a^2b$.  Since
$a,b,s$ are odd,

$$
 \chi _4(\tau)=\chi _4(a^2b)=\chi _4(b)
 =\chi _4(a^2bs^2),
\tag{153.D13}
$$

and

$$
 (a^2bs^2)^{-3/4}=a^{-3/2}b^{-3/4}s^{-3/2},\qquad
 e(s\sqrt{Na^2b})=e(as\sqrt{Nb}).
\tag{153.D14}
$$

Equations (153.D12)--(153.D14), with the mask and profile evaluated at
the unchanged integer $a^2bs^2$, prove (153.D11).  The term $a=1$ has
coefficient $+1$ and remains literal.  In particular, its $s=1$ face is

$$
 \sum_{b\ \operatorname{odd}}F_U(b)=P_U^{\rm LD},
\tag{153.D15}
$$

the unpruned large-defect character wave.  Bounding this face separately
is exactly the Round-152 problem, not a new Type-I estimate.

### 3.2 Recombination in $r=as$ and the boundary estimate

In the complete sum (153.D3), set $r=as$.  For fixed odd $r$, the
preimages are exactly

$$
 a\mid r,\qquad s=r/a<S_\star,
\tag{153.D16}
$$

with no missing gcd condition.  The common integer, character, phase,
profile, and mask are respectively

$$
 r^2b,\qquad \chi _4(r^2b)=\chi _4(b),\qquad
 e(r\sqrt{Nb})=e(\sqrt{Nr^2b}),\qquad
 A_U(r^2b),\qquad {\bf1}_{\rm LD}(r^2b).
\tag{153.D17}
$$

Thus the signed preimage coefficient is exactly (153.D4), proving
(153.D5).  If $r<S_\star$, then $r/a\le r<S_\star$ for every divisor
$a\mid r$, so (153.D6) follows from the elementary Mobius divisor sum.
Notice what this says about the short-divisor seam: all $a=1,s=r>1$
terms with $r<S_\star$ are canceled by the remaining divisors of the
same $r$; the sole uncanceled short term is $a=s=r=1$.

For $r\ge S_\star$,

$$
 |C_{S_\star}(r)|\le d(r).
\tag{153.D18}
$$

If $F_U(r^2b)\ne0$, then $r\ll\sqrt M$ and, for each of the finitely
many actual support components,

$$
 \#\{b:F_U(r^2b)\ne0\}\ll 1+\frac{M}{r^2}.
\tag{153.D19}
$$

The defect mask, oddness, transitions, and half-open endpoints can only
delete such $b$.  Using (153.D10), $|F_U(r^2b)|\ll
M^{-3/4}X^\varepsilon$, and the divisor bound, one gets (after the usual
renaming of $\varepsilon$)

$$
\begin{aligned}
 \sum_{r\ge S_\star}|C_{S_\star}(r)|
       \sum_b|F_U(r^2b)|
 &\ll_\varepsilon X^\varepsilon M^{-3/4}
 \sum_{S_\star\le r\ll\sqrt M}d(r)
       \left(1+\frac M{r^2}\right)\\
 &\ll_\varepsilon X^\varepsilon
 \left(M^{-1/4}+\frac{M^{1/4}}{S_\star}\right)
 \ll_\varepsilon X^\varepsilon.
\end{aligned}
\tag{153.D20}
$$

This proves (153.D7)--(153.D9).  The ceiling is important: $r=S_\star$
is placed in (153.D20), regardless of the parity of $S_\star$.

### 3.3 Complete $A$--$B$--$s$ power ledger and large-$a$ tails

On a fixed-$s$ block $a\asymp A$, $b\asymp B$, actual support gives

$$
 A^2Bs^2\asymp M,\qquad
 B\asymp\frac{M}{A^2s^2},\qquad
 T:=as\sqrt{NB}\asymp\sqrt{NM}=R^2\sqrt M.
\tag{153.D21}
$$

The last scale is independent of $A$ and $s$.  The complete ledger is

| quantity | fixed $s$ | dyadic $s\asymp S$ |
|---|---:|---:|
| raw number of $(a,b)$ or $(s,a,b)$ terms | $AB\asymp M/(As^2)$ | $ABS\asymp M/(AS)$ |
| pointwise actual weight | $M^{-3/4}X^\varepsilon$ | $M^{-3/4}X^\varepsilon$ |
| absolute weighted capacity | $M^{1/4}/(As^2)$ | $M^{1/4}/(AS)$ |
| unweighted signed target equivalent to weight $O(1)$ | $M^{3/4}$ | $M^{3/4}$ |
| total phase scale | $R^2\sqrt M$ | $R^2\sqrt M$ |

Thus a dyadic $(A,S)$ package is absolutely safe when

$$
 AS\gg M^{1/4}.
\tag{153.D22}
$$

This is exactly the scale of the correction $r=as\ge S_\star$ in
(153.D20); it is not a signed lower bound for any smaller package.

For a literal fixed-$s$ large-$a$ tail, direct counting gives, uniformly
for $A_0\ge1$,

$$
 \sum_{a\ge A_0}\sum_b |W_{a,b;s}|
 \ll_\varepsilon X^\varepsilon
 \left(\frac{M^{1/4}}{A_0s^2}+\frac{M^{-1/4}}s\right),
\tag{153.D23}
$$

where $W_{a,b;s}$ denotes the full amplitude in (153.D11) without its
unit phase and arithmetic signs.  Summing (153.D23) over $s<S_\star$
shows that $a\ge M^{1/4}$ is absolutely safe, while the sharper joint
condition $as\ge S_\star$ is (153.D20).  No estimate of this tail
disposes of $a=s=1$.

The defect mask may be removed only with its accepted owner.  This is
still legal after inversion: a fixed $\ell$ has at most
$X^\varepsilon$ representations $\ell=(as)^2b$, and the accepted exact
plus small-nonzero-defect set has $O_\varepsilon(M^{3/4}X^\varepsilon)$
members.  Its expanded absolute mass is therefore
$O_\varepsilon(X^\varepsilon)$.  After that removal, composition of the
actual BV profile with $a^2bs^2$ permits the same Abel ordering as in
Round 152.  It does not alter the collapse (153.D5), where the mask was
retained exactly.

### 3.4 Legal Type-I placement

Fixing $a$ and $s$ preserves $\chi _4(b)$ and gives a square-root sum in
$b$; summing the resulting bounds over $a$ by absolute values loses the
$\mu(a)$ sign.  If an exponent pair $(\kappa,\lambda)$ is applied after the two
mod-four classes and the legal BV transfer, its main dyadic capacity is

$$
 M^{-3/4}A T^\kappa B^{\lambda-\kappa}
 =R^{2\kappa}M^{\lambda-\kappa/2-3/4}
 A^{1-2\lambda+2\kappa}s^{-2\lambda+2\kappa}.
\tag{153.D24}
$$

The standard $T^{-1}B$ companion contributes only
$O(R^{-2}M^{-1/4}/(As^2))$.  For the accepted
$(\kappa,\lambda)=(195/796,235/398)$, (153.D24) is

$$
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}
 A^{123/398}s^{-275/398}X^\varepsilon.
\tag{153.D25}
$$

At $A=s=1$, this is exactly the Round-152 boundary.  If the fixed-$s$
bounds are summed over a dyadic $s\asymp S$ by absolute values,
(153.D25) becomes

$$
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}
 (AS)^{123/398}X^\varepsilon.
\tag{153.D26}
$$

Below $M^{449}\asymp R^{780}$ its smallest value occurs at $AS=1$ and
already exceeds target scale.  Combining (153.D26) with the decreasing
absolute capacity $M^{1/4}/(AS)$ reaches the target only at the already
safe endpoint $AS\asymp M^{1/4}$.  Hence the legal Type-I split supplies
no owner-complete residual range.  More fundamentally, isolating the
$A=1$ block destroys the exact cancellations (153.D6), while its
$A=s=1$ subblock is (153.D15).

### 3.5 Both Cauchy placements, diagonals, and Type-II capacity

Write a fixed block as

$$
 T_{A,B;s}=\sum_{a\asymp A}\mu(a)
 \sum_{b\asymp B}\chi _4(b)W_{a,b;s}e(a\vartheta_b),
 \qquad \vartheta_b=s\sqrt{Nb}.
\tag{153.D27}
$$

Cauchy in $a$ gives the exact positive energy

$$
\begin{aligned}
 |T_{A,B;s}|^2
 \le{}&\Big(\sum_{a\asymp A}|\mu(a)|^2\Big)
 \sum_{a\asymp A}
 \sum_{b_1,b_2\asymp B}\chi _4(b_1)\chi _4(b_2)\\
 &\quad\times W_{a,b_1;s}\overline{W_{a,b_2;s}}
 e\!\left(as\sqrt N(\sqrt{b_1}-\sqrt{b_2})\right).
\end{aligned}
\tag{153.D28}
$$

The $\mu$ sign is lost; the product $\chi _4(b_1)\chi _4(b_2)$
survives.  The literal $b_1=b_2$ diagonal, after the outer factor $A$
and square root, has capacity

$$
 M^{-3/4}A\sqrt B=\frac{M^{-1/4}}s.
\tag{153.D29}
$$

This diagonal is target-safe.  It does not license taking absolute
values in the off-diagonal character correlation.

Cauchy in $b$ gives

$$
\begin{aligned}
 |T_{A,B;s}|^2
 \le{}&\Big(\sum_{b\asymp B}|\chi _4(b)|^2\Big)
 \sum_{b\asymp B}\sum_{a_1,a_2\asymp A}
 \mu(a_1)\mu(a_2)\\
 &\quad\times W_{a_1,b;s}\overline{W_{a_2,b;s}}
 e\!\left((a_1-a_2)s\sqrt{Nb}\right).
\end{aligned}
\tag{153.D30}
$$

Here $\chi _4$ is lost and $\mu(a_1)\mu(a_2)$ survives.  The
$a_1=a_2$ diagonal has capacity

$$
 M^{-3/4}B\sqrt A
 =\frac{M^{1/4}}{A^{3/2}s^2}.
\tag{153.D31}
$$

After absolute summation over $s\asymp S$, (153.D29) costs
$M^{-1/4}$, whereas (153.D31) costs

$$
 \frac{M^{1/4}}{A^{3/2}S}.
\tag{153.D32}
$$

Thus the second placement, or even hypothetical pointwise square-root
cancellation in the linear $a$-sum, cannot reach target scale in the
short-face region

$$
 A^{3/2}S<M^{1/4}.
\tag{153.D33}
$$

At $A=S=1$, (153.D31) is the full $M^{1/4}$ absolute loss.  This is a
positive-diagonal capacity, not a signed lower bound.

Even an optimistic additive large-sieve model with $B$ frequencies
spaced at scale $1/B$ gives from (153.D28)

$$
 M^{-3/4}\sqrt{AB(A+B)}
 \asymp
 \begin{cases}
 M^{-1/4}s^{-1},&A\ge B,\\
 M^{1/4}A^{-3/2}s^{-2},&B\ge A.
 \end{cases}
\tag{153.D34}
$$

It therefore returns the same short-face loss.  A complete Type-II
argument would have to keep the surviving sign in (153.D28) or
(153.D30) and prove cancellation in the off-diagonal; a positive
spacing energy alone does not do so.

### 3.6 Exact collisions, near collisions, and square-product fibres

The frequency collision in (153.D28) is

$$
 s\sqrt N(\sqrt{b_1}-\sqrt{b_2})\in\mathbb Z.
\tag{153.D35}
$$

If $b_1\ne b_2$, the difference of the two integral square roots is a
nonzero rational.  Its sum is then rational as well, so both
$Nb_1$ and $Nb_2$ are squares.  Conversely, two such squares give an
integer in (153.D35).  Write

$$
 N=c^2n_0,\qquad n_0\ \hbox{squarefree}.
\tag{153.D36}
$$

Then $Nb$ is a square exactly when $b=n_0u^2$.  If $n_0$ is even there
is no odd $b$ on this ray; if $n_0$ is odd then $u$ is odd.  In either
case every present square-ray term has
$Na^2bs^2$ square and is removed by the strict large-defect mask.
Therefore (153.D28) has no literal exact off-diagonal frequency
collision after the accepted exact-square owner is imposed.

There is nevertheless a second exact collision class before any
Cauchy separation:

$$
 a_1\sqrt{b_1}=a_2\sqrt{b_2}
 \quad\Longleftrightarrow\quad
 a_1^2b_1=a_2^2b_2.
\tag{153.D37}
$$

Writing $a_1=gu$, $a_2=gv$, $(u,v)=1$, its complete parametrization is

$$
 b_1=v^2c,\qquad b_2=u^2c.
\tag{153.D38}
$$

These are not generally exact-square phases; they are repeated
factorizations of the same integer.  Their fibre multiplicity is
$O_\varepsilon(X^\varepsilon)$, and their signed coefficient is

$$
 \sum_{a^2\mid n}\mu(a)=\mu^2(n)
\tag{153.D39}
$$

at fixed $s$, or $C_{S_\star}(r)$ after $r=as$ is recombined.  Thus
separating these fibres before taking a positive energy discards the
very Mobius cancellation being sought.  More generally,

$$
 s\sqrt N(a_1\sqrt{b_1}-a_2\sqrt{b_2})\in\mathbb Z
\tag{153.D40}
$$

is either the zero-difference product fibre (153.D37), or, by the same
rational-sum argument, has both $Nb_i$ square and is removed by the
exact-square mask.  This classification is independent of the parity
and prime-power structure of $N$.

For near collisions, put

$$
 Y:=s\sqrt{NB}\asymp\frac{R^2\sqrt M}{A}.
\tag{153.D41}
$$

For distinct $b_1,b_2\asymp B$, let
$\alpha=s\sqrt N(\sqrt{b_1}-\sqrt{b_2})$.  It is a root of the monic
integer polynomial

$$
 P(z)=z^4-2s^2N(b_1+b_2)z^2+s^4N^2(b_1-b_2)^2.
\tag{153.D42}
$$

If $\alpha$ is not an integer and $m$ is its nearest integer, then
$P(m)$ is a nonzero integer.  Factoring $P(m)$ over the four conjugates
$\pm s\sqrt N(\sqrt{b_1}\pm\sqrt{b_2})$ gives

$$
 \|\alpha\|\gg (1+Y)^{-3}.
\tag{153.D43}
$$

When $b_1b_2$ is a square, write $b_i=qu_i^2$ with the same squarefree
$q$.  If $Nq$ is a square, this is the excluded exact collision.  If
not, the quadratic norm

$$
 |\alpha-m|\,|\alpha+m|=|\alpha^2-m^2|\ge1
\tag{153.D44}
$$

improves (153.D43) to $\|\alpha\|\gg(1+Y)^{-1}$.  These exact algebraic
separations are far too weak for the target.  If one optimistically
grants the quadratic spacing $(1+Y)^{-1}$ to every ambient $b$-point
and inserts it as an all-$B$ minimum spacing in (153.D28), or instead
grants the generic quartic spacing to every ambient $b$-point, the two
coefficient-blind controls are, respectively,

$$
 \frac{R}{As}
 \quad\hbox{for the optimistic all-$B$ quadratic control},\qquad
 \frac{R^3M^{1/2}}{A^2s}
 \quad\hbox{for the generic quartic all-$B$ control},
\tag{153.D45}
$$

instead of $O(1)$.  The first quantity is not a bound for a literal
fixed square-product-$q$ fibre: such a fibre has
$b=qu^2\asymp B$ and therefore only
$O(\sqrt{B/q}+1)$ points, which must be priced separately.  Formula
(153.D45) deliberately gives every one of the ambient $B$ points the
stronger quadratic spacing and is thus an optimistic all-$B$ control.
Since $As\ll\sqrt M\le R$, even that optimistic quantity is target-sized
only at the top edge.  The generic quartic all-$B$ minimum-separation
control is still larger.  These coefficient-blind all-$B$ placements do
not close the residual range.

The ambient all-$b$ pigeonhole capacity of the coefficient-blind
Dirichlet-kernel majorant is as follows.  Apart from the $O(\sqrt B)$
possible square-ray points, the remaining $\asymp B$ ambient frequencies
$\vartheta_b\pmod1$ still occupy only $O(A)$ arcs of length $1/(10A)$.
If $B\gg A$, at least

$$
 \gg \frac{B^2}{A}
\tag{153.D46}
$$

ambient ordered pairs lie in a common arc.  The literal active weights
$W_{a,b;s}$ have no lower bound and depend on $a$ through the actual
profile and defect mask.  Thus (153.D46) neither asserts that these
pairs carry nonzero active weight nor gives an unavoidable barrier for
the weighted correlation.  Only after replacing the signed, weighted
correlation in (153.D28) by the coefficient-blind absolute
Dirichlet-kernel majorant does one assign size $\asymp A$ to all these
pairs and recover the capacity (153.D31).  Equation (153.D46) is an
ambient capacity diagnostic for that positive majorant, not a lower
bound for (153.D28); the active weights can vanish and the surviving
$\chi _4(b_1)\chi _4(b_2)$ can cancel.

Finally, the strict defect condition gives only an individual
nonresonance.  For $y=as\sqrt{Nb}\asymp R^2\sqrt M$,

$$
 |k^2-y^2|=(k+y)\|y\|>M^{3/4}
 \quad\Longrightarrow\quad
 \|y\|\gg\frac{M^{1/4}}{R^2}.
\tag{153.D47}
$$

It gives no lower bound for
$\|y_1-y_2\|$.  Treating (153.D47) as a pair-spacing statement would be
an invalid near-collision step.

## 4. First doubtful or unproved step

There is no doubtful step in the finite identity (153.D5), the divisor
collapse (153.D6), or the absolute boundary estimate (153.D20).  Their
first input beyond exact algebra is only the accepted support/BV bound
and the elementary divisor bound.

The first unproved analytic statement is exactly

$$
 \left|P_U^{\rm LD}\right|
 =\left|\sum_{b\ \operatorname{odd}}F_U(b)\right|
 \ll_\varepsilon X^\varepsilon
 \qquad(M^{449}\ll R^{780}),
\tag{153.D48}
$$

equivalently the original Round-152 wave after its target-safe
exact/near-defect pieces are restored.  In bilinear language, the first
missing step would be a coefficient-sensitive signed off-diagonal
estimate for (153.D28) or (153.D30) which:

- does not isolate the $a=s=1$ face;
- recombines the exact product fibres before positivity;
- retains the surviving $\chi _4$ or $\mu$ coefficient;
- controls the near-collision multiplicity beyond (153.D43)--(153.D46);
  and
- remains valid for the literal zero-extended mask and endpoints.

No such theorem is proved here.  Applying Cauchy first and then using an
absolute spacing energy has the quantified short-face loss
(153.D31)--(153.D33); applying minimum algebraic spacing has the still
larger loss (153.D45).  These are scoped upper-capacity no-go results,
not lower bounds for the actual signed correlation.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_Pstar_survivor` | GREEN. Equation (153.D3) is exactly the large-defect, $s<S_\star$ survivor and keeps the compulsory $s=1$ layer. |
| `owned_range_and_owner_exclusion` | GREEN. The report stays below $M^{449}\asymp R^{780}$ and uses the exact-square and small-defect owners only to pass from $P_U^{\rm LD}$ to $P_U$. The already owned upper range is not counted again. |
| `squarefree_kernel_uniqueness` | GREEN. The unique $\ell=\tau s^2$ factorization is used with no false $(\tau,s)=1$ condition. |
| `exact_Mobius_inversion` | GREEN. The squarefree condition is first replaced by $\mu^2(\tau)$ over all odd $\tau$; every $a$, sign, and finite endpoint survives in (153.D11). |
| `a1_short_divisor_seam` | GREEN/no-go. The $a=1,s>1$ terms cancel only after complete $r=as$ recombination. The $a=s=1$ term is exactly $P_U^{\rm LD}$ and remains open. |
| `dyadic_A_B_s_power_ledger` | GREEN. Equations (153.D21)--(153.D26), (153.D29)--(153.D34), and (153.D41)--(153.D45) record every $R,M,A,B,s,S$ power. |
| `actual_profile_mask_and_B11` | GREEN. $A_U$, zero extension, every support component, strict defect mask, nearest integer, transition, and endpoint are evaluated at the unchanged integer. $B_{1,U}(1)$ remains external. |
| `Cauchy_coefficient_survival` | GREEN. Cauchy in $a$ loses $\mu$ but retains $\chi _4(b_1)\chi _4(b_2)$; Cauchy in $b$ loses $\chi _4$ but retains $\mu(a_1)\mu(a_2)$. |
| `diagonal_and_pigeonhole_capacity` | GREEN/no-go. The two literal diagonals are (153.D29) and (153.D31). The ambient all-$b$, coefficient-blind Dirichlet majorant has capacity (153.D31), but the actual $a$-dependent weights have no lower bound; no unavoidable weighted-correlation barrier is claimed. |
| `exact_and_near_frequency_collisions` | GREEN. Exact off-diagonal modulo-one collisions are square rays and are removed; zero-difference product fibres are (153.D37)--(153.D39); generic and square-product near spacings are (153.D43)--(153.D46). All parities of $N$ are covered by (153.D36). |
| `TypeI_TypeII_signed_bilinear_target` | GREEN/no-go. The legal Type-I power is (153.D25); both Type-II Cauchy placements and their required surviving signs are explicit. The $A=S=1$ face prevents an owner-complete range. |
| `absolute_capacity_vs_signed_sum` | GREEN. Every adverse quantity in (153.D22), (153.D31), (153.D34), (153.D45), and (153.D46) is labeled as an absolute or positive-energy capacity, never as a signed lower bound. |
| `N_parity_endpoints_and_transitions` | GREEN. The even-$n_0$ square ray is absent, the odd-$n_0$ ray is excluded by the defect owner, the no-tie argument is retained, and $r=S_\star$ plus every actual half-open endpoint lies in the boundary estimate. |
| `D_L_generic_tge2_cross_and_downstream_scope` | GREEN. No $D>1$, $L>1$, generic growing-$M$, original $t\ge2$, Round-138 cross, full M1/M2, endpoint, M9, bridge, target, or exponent statement is inferred. |

All controls are analytic.  No numerical experiment, random model, or
computational certification was used.

## 6. Dependencies and exact artifacts used

The derivation uses only the following assigned artifacts:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round153_d1_squarefree_kernel_bilinear_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/candidates/conductor_round152_square_root_wave_reduction.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reviews/conductor_round152_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/controls/conductor_round152_controls.md`; and
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`.

The only general arithmetic input added in the derivation is the
elementary identity $\sum_{d\mid n}\mu(d)={\bf1}_{n=1}$ and the accepted
elementary bound $d(n)\ll_\varepsilon n^\varepsilon$.  No external
bilinear or spacing theorem is invoked, so no new source dependency is
created.

## 7. Recommended state effect

Recommend the terminal label

$$
 \boxed{\mathsf{squarefree\_kernel\_bilinear\_no\_go}.}
\tag{153.D49}
$$

Subject to independent review, record (153.D3)--(153.D20) as an exact
scoped obstruction: the complete Mobius-expanded squarefree-kernel
family recombines to the original large-defect $D=d=L=1$ character wave
plus an absolutely target-safe $r\ge\lceil M^{1/4}\rceil$ boundary.
Record (153.D28)--(153.D47) only as method-specific Cauchy, diagonal,
spacing, and collision obstructions.

Do not promote `squarefree_kernel_bilinear_target` or a strict range.
Keep $|P_U^*|\ll_\varepsilon X^\varepsilon$ below
$M^{449}\asymp R^{780}$, `M9-M1-global-lower-radial-signed-estimate`,
the direct M1 parents, M9-M1, M9-M2, endpoint uniformity, M9, the
conditional bridge, and the Gauss-circle target open or unchanged.  A
future round should attack (153.D48) directly or supply a genuinely
signed theorem that survives the exact recombination; it should not
assign independent mathematical ownership to dyadic $a$-blocks whose
cancellation is (153.D6).
