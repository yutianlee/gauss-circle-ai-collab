# Round 152 discovery report: the actual-profile square-root character wave

- Campaign: `m9-m1-lower-cone-t1-d1-square-root-wave-gate`
- Research round: 152
- Task: `square_root_character_wave_attack`
- Role: discovery
- Starting graph SHA-256: `d09d0f8c1e7058a1e423e5249d3cf28b08d8478cff55ddd1c85b1d59bb177b2c`
- Allocation used: 100% analytic/algebraic, 0% numerical
- Terminal label recommended: `strict_square_root_character_range`

## 1. Result

The principal positive result is an endpoint-complete, absolute
target-safe pruning of three disjoint arithmetic sectors at every scale
in the Round-152 open range.  It does not close a new full $M$-scale
interval.  More precisely, let

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 1\ll M\leq R^2,\qquad M^{819}\ll R^{1424},
\tag{152.A1}
$$

and retain the exact compact-smooth Round-148 profile.  Then:

1. exact adjacent-odd pairing is a finite difference of the **whole**
   oscillatory summand.  Its phase increment is
   $2\sqrt N/(\sqrt{x+2}+\sqrt x)$ and is not uniformly close to an
   integer or to zero.  Pairing therefore gives no automatic character
   saving;
2. one legal van der Corput $A$-process has only even shifts in the
   original odd variable, and
   $\chi _4(\ell+2h)\chi _4(\ell)=(-1)^h$.  Thus the character becomes a
   constant sign in every shifted correlation.  Termwise use of the
   second-derivative estimate gives

   $$
   |P_U|^2\ll_\varepsilon X^\varepsilon\left{
       \frac{M^{1/2}}H
       +R M^{-3/4}H^{1/2}
       +R^{-1}M^{3/4}H^{-1/2}
   \right}.
   \tag{152.A2}
   $$

   Making the diagonal and first curvature term both target-sized would
   require respectively $H\gg M^{1/2}$ and
   $H\ll M^{3/2}/R^2$, which are compatible only for
   $M\gg R^2$.  Hence this legal character-aware $A$-process gives no
   point in (152.A1);
3. in the unique split $\ell=\tau s^2$, with $\tau$ odd and squarefree
   and $s$ odd, the exact-square family is harmless.  If
   $N=a^2n_0$ with $n_0$ squarefree, exact products occur only for
   $\tau=n_0$, and only when $n_0$ is odd.  Their complete weighted mass is

   $$
   \ll_\varepsilon M^{-1/4}n_0^{-1/2}X^\varepsilon.
   \tag{152.A3}
   $$

   There is nevertheless a new absolute pruning.  If $k(\ell)$ is the
   unique nearest integer to $\sqrt{N\ell}$ and
   $j(\ell)=k(\ell)^2-N\ell$, then the complete sector
   $0<|j|\le M^{3/4}$ has $O_\varepsilon(M^{3/4}X^\varepsilon)$ lattice
   points and hence weighted mass $O_\varepsilon(X^\varepsilon)$ for every
   parity and prime-power structure of $N$.  Independently, the
   squarefree-kernel tail $s\ge M^{1/4}$ has the same absolute bound.
   After assigning overlaps in the order $j=0$, nonzero small $j$, then
   large $s$, the only survivor is

   $$
   |j(\ell)|>M^{3/4},\qquad s<M^{1/4}.
   \tag{152.A3a}
   $$

   A cruder near/far split based only on the inner $s$-oscillation still
   retains the full $M^{1/4}X^\varepsilon$ capacity at
   $\tau\asymp M$; the congruence count above is essential for the small
   $j$ sector but does not estimate the residual (152.A3a);
4. the Mellin spectral parameter is

   $$
   T=\sqrt{NM}\asymp R^2M^{1/2},
   \tag{152.A4}
   $$

   the Mellin transform occupies a $t$-interval of width $\asymp T$, the
   degree-one analytic conductor is $\asymp T$, and an individual
   approximate functional equation has length
   $T^{1/2}\asymp RM^{1/4}$.  Absolute spectral integration loses $R$
   even under a hypothetical Lindelof bound.  Applying the exact
   functional equation instead produces dual length

   $$
   Q\asymp \frac{T}{M}\asymp R^2M^{-1/2}
   \tag{152.A5}
   $$

   (with the exact Poisson normalization $Q=2\sqrt{N/M}$), root number
   $+1$, and reconstructs the accepted reciprocal row $S_U$, including
   the units $e(\pm1/8)$.  It is therefore the already accepted
   principal self-return, not a new estimate; and
5. the verified second- and third-derivative estimates and the audited
   exponent-pair bounds give no new full $M$-range.
   The best source-legal power among the supplied cards is the
   $B$-dual of the Tao--Trudgian--Yang pair,

   $$
   |P_U|\ll_\varepsilon
   \left(\frac{R^{1424}}{M^{819}}\right)^{1/2564}X^\varepsilon,
   \tag{152.A6}
   $$

   which is target-sized exactly at the already owned TTY boundary and
   has a positive loss in (152.A1).

Thus (152.A38l)--(152.A38n) below give a strict square-root-character
sector reduction: the exact squares, every nonzero defect
$|j|\le M^{3/4}$, and the remaining large-square tail
$s\ge M^{1/4}$ are all absolutely target-safe without overlap.  On the
surviving sector, the specified adjacent-pairing, termwise one-$A$-process,
squarefree-kernel inner-linear, pointwise or mean-square Mellin, bare
functional-equation, and current audited derivative/exponent-pair
implementations give no target.  This is not a lower bound for $P_U$ and
not an impossibility theorem for a new coefficient-sensitive signed
estimate.

## 2. Exact statement and hypotheses

Write

$$
 \mathcal A(\ell)=\mathscr A_{1,M,U}(1,\ell),\qquad
 w(\ell)=\ell^{-3/4}\mathcal A(\ell),\qquad
 f(\ell)=\sqrt{N\ell},
\tag{152.A7}
$$

and extend $\mathcal A$ and $w$ by zero before every pairing or
transform.  The literal wave is

$$
 P_U=\sum_{\substack{\ell>0\\ \ell\ {\operatorname{odd}}}}
 \chi _4(\ell)w(\ell)e(f(\ell)).
\tag{152.A8}
$$

The accepted Round-148 ledger supplies finitely many compact support
components with $\ell\asymp M$, all hard radial-prefix and cone collars
already assigned to their prior owners, and

$$
 \|\mathcal A\|_\infty+\operatorname {Var}\mathcal A
 \ll_\varepsilon X^\varepsilon,
 \qquad
 \|w\|_\infty+\operatorname {Var}w
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{152.A9}
$$

This includes the inherited half-open $U$-prefix, stationary buffers,
radial and cone transition widths, tails, and endpoint convention.  No
arbitrary bounded coefficient is substituted for $\mathcal A$.

The literal compressed component is

$$
 \widetilde S_U=B_{1,U}(1)S_U,\qquad
 |B_{1,U}(1)|\ll_\varepsilon X^\varepsilon,
\tag{152.A10}
$$

and the accepted boundary-complete relation is

$$
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon).
\tag{152.A11}
$$

Thus the coefficient (152.A10) is retained and merely costs another
$X^\varepsilon$; it is not absorbed into an arbitrary wave coefficient.

The raw number of possible terms in (152.A8) is $O(M)$ and

$$
 \sum_{\ell\ {\operatorname{odd}}}|w(\ell)|
 \ll_\varepsilon M^{1/4}X^\varepsilon.
\tag{152.A12}
$$

In contrast, with the phase removed, bounded partial sums of $\chi _4$
and (152.A9) give the pure signed character mass

$$
 \left|\sum_{\ell\ {\operatorname{odd}}}\chi _4(\ell)w(\ell)\right|
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{152.A13}
$$

Equations (152.A12)--(152.A13) are deliberately different quantities.
The task is to recover only the factor $M^{1/4}$ needed to replace
(152.A12) by $X^\varepsilon$ in the presence of $e(f(\ell))$.

Bounded $M$ is excluded as already owned.  The boundary
$M^{819}\asymp R^{1424}$ is target-sized in (152.A6), and
$M^{819}\gg R^{1424}$ is excluded as the Round-151 TTY owner.  The
report concerns only (152.A1).  All constants implicit in support
comparisons are fixed profile constants.

## 3. Proof or derivation

### 3.1 Exact adjacent-odd pairing

Put $F(x)=w(x)e(f(x))$, with the zero extension just specified.  The
character identities give the endpoint-complete equality

$$
 P_U=\sum_{n\in\mathbb Z}\{F(4n+1)-F(4n+3)\}.
\tag{152.A14}
$$

For $x=4n+1$ the finite difference is exactly

$$
 F(x)-F(x+2)
 =e(f(x))\left\{w(x)-w(x+2)e(\Delta_2f(x))\right\},
\tag{152.A15}
$$

where

$$
 \Delta_2f(x)=f(x+2)-f(x)
 =\frac{2\sqrt N}{\sqrt{x+2}+\sqrt x}
 \asymp \frac{R^2}{\sqrt M}.
\tag{152.A16}
$$

The exact oscillatory multiplier has size
$|1-e(\Delta_2f(x))|=2|\sin(\pi\Delta_2f(x))|$; no hypothesis controls
it uniformly.  Replacing (152.A15) only by the difference of the smooth
weights would therefore be false.

For comparison, a lawful total-variation bound differentiates the whole
summand:

$$
 F'(x)=e(f(x))\left(w'(x)+2\pi i\frac{\sqrt N}{2\sqrt x}w(x)\right),
\tag{152.A17}
$$

and gives

$$
 \operatorname {Var}F
 \ll_\varepsilon
 \left(M^{-3/4}+R^2M^{-1/4}\right)X^\varepsilon.
\tag{152.A18}
$$

In the whole range $M\le R^2$, (152.A18) is worse than the direct
capacity (152.A12).  Consequently exact adjacent pairing gives at best
$M^{1/4}X^\varepsilon$ after taking the better of the two estimates.  It
does not transfer the small pure character mass (152.A13) through the
square-root phase.

### 3.2 One legal character-aware $A$-process

Index the odd integers by $\ell=2n+1$ and set

$$
 z_n=(-1)^n w(2n+1)e(f(2n+1)).
\tag{152.A19}
$$

The support has length $J\asymp M$.  A shift by an odd number in the
original $\ell$-lattice leaves the odd support and lands on even integers,
so the nonzero correlations have shifts $2h$.  Equivalently,

$$
 \chi _4(\ell+2h)\chi _4(\ell)=(-1)^h
 \quad(\ell\ {\operatorname{odd}}).
\tag{152.A20}
$$

For $1\le H\le cM$, van der Corput differencing gives

$$
 |P_U|^2\ll \frac MH\left{
   C_0+\sum_{1\le h<H}|C_h|
 \right},
\tag{152.A21}
$$

where

$$
 C_0=\sum_{\ell\ {\operatorname{odd}}}|w(\ell)|^2
 \ll_\varepsilon M^{-1/2}X^\varepsilon,
\tag{152.A22}
$$

and, before taking the absolute value,

$$
 C_h=(-1)^h\sum_{\ell\ {\operatorname{odd}}}
 w(\ell+2h)\overline{w(\ell)}
 e(g_h(\ell)),
\qquad
 g_h(x)=\sqrt N(\sqrt{x+2h}-\sqrt x).
\tag{152.A23}
$$

Thus (152.A20) is exact character **loss**, not a residual character sum.
The shifted phase has length $\asymp M$, scaled parameter

$$
 T_h\asymp R^2hM^{-1/2},
\qquad
 g_h^{(r)}(x)\asymp_r R^2hM^{-r-1/2},
\tag{152.A24}
$$

for fixed $r\ge1$ and $h\le cM$.  In particular

$$
 g_h''(x)=\frac{\sqrt N}{4}
 \{x^{-3/2}-(x+2h)^{-3/2}\}
 \asymp R^2hM^{-5/2}.
\tag{152.A25}
$$

The product weight in (152.A23) has supremum plus variation
$\ll M^{-3/2}X^\varepsilon$.  The second-derivative estimate on each odd
progression therefore yields

$$
 |C_h|\ll_\varepsilon X^\varepsilon\left{
   R h^{1/2}M^{-7/4}
   +R^{-1}h^{-1/2}M^{-1/4}
 \right}.
\tag{152.A26}
$$

Summing (152.A26) in (152.A21) proves (152.A2).  Since all three terms in
that displayed majorant are nonnegative, a target-sized output from this
specific procedure would require

$$
 H\gg M^{1/2},\qquad
 H\ll \frac{M^{3/2}}{R^2},\qquad
 H\gg \frac{M^{3/2}}{R^2}.
\tag{152.A27}
$$

The first two conditions force $M\gg R^2$.  At $M\asymp R^2$, choosing
$H\asymp M^{1/2}$ makes all terms target-sized, but that is the already
owned top boundary, not (152.A1).

More generally, an exponent pair $(\kappa,\lambda)$ applied legally to
(152.A23) when $T_h\ge M$ gives

$$
 |C_h|\ll_\varepsilon
 R^{2\kappa}h^\kappa
 M^{\lambda-3/2-3\kappa/2}X^\varepsilon
\tag{152.A28}
$$

and hence

$$
 |P_U|^2\ll_\varepsilon X^\varepsilon\left{
 \frac{M^{1/2}}H+
 R^{2\kappa}M^{\lambda-1/2-3\kappa/2}H^\kappa
 \right}.
\tag{152.A29}
$$

For $T_h<M$ the source convention does not apply and a derivative
fallback such as (152.A26) is compulsory.  Optimizing (152.A29) is just
the ordinary exponent-pair $A$-operation after the character has become
the constant (152.A20).  Any use of cancellation among the outer signs
$(-1)^h$ would be a new two-variable signed theorem, not a gain supplied
by the $A$-process itself.

### 3.3 Squarefree kernel, exact squares, and near squares

Every positive odd $\ell$ has a unique representation
$\ell=\tau s^2$ with $\tau$ odd squarefree and $s$ odd.  Since
$\chi _4(s^2)=1$, the exact identity is

$$
 P_U=
 \sum_{\substack{\tau\ge1\\ \tau\ {\operatorname{odd},\ \operatorname{squarefree}}}}
 \chi _4(\tau)\tau^{-3/4}
 \sum_{\substack{s\ge1\\s\ {\operatorname{odd}}}}
 s^{-3/2}\mathcal A(\tau s^2)e(s\sqrt{N\tau}).
\tag{152.A30}
$$

The zero extension of $\mathcal A$ makes (152.A30) exact at both ends of
every inherited prefix.

Write uniquely

$$
 N=a^2n_0,\qquad n_0\ {\operatorname{squarefree}}.
\tag{152.A31}
$$

Because $n_0$ and $\tau$ are squarefree, $N\tau$ is a square if and only
if $\tau=n_0$.  This value is admissible in (152.A30) if and only if
$n_0$ is odd, equivalently $\nu _2(N)$ is even.  If $\nu _2(N)$ is odd,
the exact family is empty.  When it is present,
$\sqrt{Nn_0}=an_0\in\mathbb Z$, so the phase is one for every $s$ and

$$
 P_{\operatorname{ex}}=\chi _4(n_0)n_0^{-3/4}
 \sum_{s\ {\operatorname{odd}}}s^{-3/2}\mathcal A(n_0s^2).
\tag{152.A32}
$$

There are $O(1+\sqrt{M/n_0})$ raw exact-square terms.  On the actual
support $s\asymp (M/n_0)^{1/2}$, and (152.A32) proves (152.A3).  Thus the
entire exact $N\ell=\square$ channel is target-safe, despite having
constant character and phase along the ray.

For the nonexact family, split $\tau\asymp T$ and put

$$
 Y=(M/T)^{1/2},\qquad
 \Delta_\tau=\|2\sqrt{N\tau}\|.
\tag{152.A33}
$$

The factor 2 is compulsory because $s$ runs through an odd progression:
the ratio of consecutive phases is $e(2\sqrt{N\tau})$.  Abel summation and
the geometric progression bound, with the actual sampled profile, give

$$
 \left|\sum_{s\ {\operatorname{odd}}}s^{-3/2}
 \mathcal A(\tau s^2)e(s\sqrt{N\tau})\right|
 \ll_\varepsilon
 Y^{-3/2}\min\{Y,\Delta_\tau^{-1}\}X^\varepsilon.
\tag{152.A34}
$$

Let $m_\tau$ be a nearest integer to $2\sqrt{N\tau}$ and
$r_\tau=m_\tau^2-4N\tau$.  For $\tau\asymp T$,

$$
 \Delta_\tau
 =\frac{|r_\tau|}{m_\tau+2\sqrt{N\tau}}
 \asymp \frac{|r_\tau|}{R^2\sqrt T}.
\tag{152.A35}
$$

If $m_\tau$ is even, (152.A35) is the ordinary near-square channel for
$N\tau$ and $r_\tau$ is divisible by 4.  If $m_\tau$ is odd, then
$r_\tau\equiv1\pmod4$; this is the nonexact half-integral resonance forced
by the odd $s$-progression.  Exact half-integral resonance is impossible,
because $4N\tau$ cannot be an odd square.  Formula (152.A35) therefore
handles both parities of $N$ and both parities of the nearest frequency.

Define the near family by $\Delta_\tau\le Y^{-1}$.  Equivalently,

$$
 0<|m_\tau^2-4N\tau|
 \ll \frac{R^2T}{\sqrt M}.
\tag{152.A36}
$$

If $K_T$ is the number of such odd squarefree $\tau\asymp T$, then
(152.A34) gives the complete near contribution

$$
 |P_{{\operatorname{near}},T}|
 \ll_\varepsilon
 M^{-1/4}T^{-1/2}K_T X^\varepsilon
 \le M^{-1/4}T^{1/2}X^\varepsilon.
\tag{152.A37}
$$

For the far family, (152.A34) gives exactly

$$
 |P_{{\operatorname{far}},T}|
 \ll_\varepsilon
 M^{-3/4}\sum_{\substack{\tau\asymp T\\
                         \Delta_\tau>Y^{-1}}}
 \Delta_\tau^{-1}X^\varepsilon
 \le M^{-1/4}T^{1/2}X^\varepsilon.
\tag{152.A38}
$$

Summing dyadic $T\le CM$ in (152.A37)--(152.A38) returns
$M^{1/4}X^\varepsilon$.  This is not merely an avoidable weak estimate at
small $T$: at $T\asymp M$ one has $Y\asymp1$ and
$\Delta_\tau\le1/2$, so every $\tau$ is in the no-inner-cancellation
range (up to harmless fixed support constants).  The $s=1$ fibre is the
original squarefree part of (152.A8).  Closing it requires a signed outer
$\chi _4(\tau)$ estimate; taking absolute values in $\tau$ is circular at
capacity $M^{1/4}$.  Equations (152.A37)--(152.A38) are upper capacities,
not lower bounds for the actual wave.

There is a sharper absolute sector which uses the integral square defect,
not merely the geometric estimate (152.A34).  For every retained $\ell$,
let $k(\ell)$ be the nearest integer to $\sqrt{N\ell}$ and put

$$
 j(\ell)=k(\ell)^2-N\ell.
\tag{152.A38a}
$$

The nearest integer is unique for all parities of $N$: a tie would imply
$\sqrt{N\ell}=m+1/2$ and hence
$4N\ell=(2m+1)^2$, impossible because the left side is divisible by 4
and the right side is odd.  Also

$$
 k(\ell)\asymp\sqrt{NM}=R^2\sqrt M,
 \qquad
 |j(\ell)|\ll R^2\sqrt M.
\tag{152.A38b}
$$

For an integer $j$, define the complete root multiplicity

$$
 \rho_N(j)=\#\{x\pmod N:x^2\equiv j\pmod N\}.
\tag{152.A38c}
$$

The following all-parity bound is elementary and uniform:

$$
 \boxed{\rho_N(j)\le 4\,2^{\omega(N)}\sqrt{(|j|,N)}.}
\tag{152.A38d}
$$

To prove it, first take a prime power $p^a\Vert N$ and put
$v=\min\{v_p(j),a\}$.  If $v=a$, the congruence is $x^2\equiv0\pmod {p^a}$
and has $p^{\lfloor a/2\rfloor}\le p^{v/2}$ roots.  If $v<a$ is odd,
there is no root.  If $v=2b<a$, write $x=p^by$; each unit root of

$$
 y^2\equiv j/p^{2b}\pmod {p^{a-2b}}
\tag{152.A38e}
$$

has $p^b$ lifts modulo $p^{a-b}$.  There are at most two unit roots for
odd $p$, and at most four for $p=2$, including the moduli $2$ and $4$.
Thus the local multiplicity is at most $2p^{v/2}$ for odd $p$ and
$4\,2^{v/2}$ at $p=2$.  The Chinese remainder theorem proves
(152.A38d), with no assumption on $\nu _2(N)$ or $(j,N)$.

For $J\ge1$, divisor expansion of the gcd gives

$$
\begin{aligned}
 \sum_{1\le |j|\le J}\rho_N(j)
 &\ll 2^{\omega(N)}
 \sum_{1\le |j|\le J}\sqrt{(|j|,N)}\\
 &\le 2^{\omega(N)}
 \sum_{1\le |j|\le J}
 \sum_{d\mid(|j|,N)}\sqrt d\\
 &\ll J\,2^{\omega(N)}\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon JN^\varepsilon.
\end{aligned}
\tag{152.A38f}
$$

The actual $k$-support in (152.A38b) has total length
$O(\sqrt{NM})$.  Since

$$
 \frac{\sqrt{NM}}N=\sqrt{M/N}\ll R^{-1},
\tag{152.A38g}
$$

it has length less than $N$ for large $X$.  Hence each root class modulo
$N$ supplies at most one $k$ in the full actual support interval (and at
most a fixed number if the finite support components are counted
separately).  Once $j$ and $k$ are fixed,
$\ell=(k^2-j)/N$ is fixed.  Positivity, oddness, nearest-integer status,
the actual support, transition pieces, and both endpoints only delete
these candidates.  Consequently

$$
 \#\{\ell:\mathcal A(\ell)\ne0, \ell\ {\operatorname{odd}},\\
          0<|j(\ell)|\le J\}
 \ll_\varepsilon JX^\varepsilon.
\tag{152.A38h}
$$

Taking $J=M^{3/4}$ and using $|w(\ell)|\ll
M^{-3/4}X^\varepsilon$ proves the endpoint-complete absolute estimate

$$
 \sum_{\substack{\ell\ {\operatorname{retained}}\\
                  0<|j(\ell)|\le M^{3/4}}}|w(\ell)|
 \ll_\varepsilon X^\varepsilon.
\tag{152.A38i}
$$

The excluded value $j=0$ is exactly the square family (152.A32), already
bounded by (152.A3); it is not charged to (152.A38i).

There is a second absolute sector in the unique factorization
$\ell=\tau s^2$.  Put $S=M^{1/4}$.  For each odd $s\ge S$, actual support
$\ell\asymp M$ restricts $\tau$ to an interval containing
$O(1+M/s^2)$ integers.  Therefore, with squarefreeness and oddness only
reducing the count,

$$
 \#\{\ell\ {\operatorname{retained}}:s\ge M^{1/4}\}
 \ll \sum_{M^{1/4}\le s\ll\sqrt M}
       \left(1+\frac M{s^2}\right)
 \ll M^{3/4}.
\tag{152.A38j}
$$

It follows that

$$
 \sum_{\substack{\ell\ {\operatorname{retained}}\\
                  \ell=\tau s^2,\ s\ge M^{1/4}}}|w(\ell)|
 \ll_\varepsilon X^\varepsilon.
\tag{152.A38k}
$$

To combine (152.A3), (152.A38i), and (152.A38k) without overlap, define
the disjoint sets

$$
\begin{aligned}
 \mathcal L_0&=\{\ell:j(\ell)=0\},\\
 \mathcal L_1&=\{\ell:0<|j(\ell)|\le M^{3/4}\},\\
 \mathcal L_2&=\{\ell:|j(\ell)|>M^{3/4},\ s(\ell)\ge M^{1/4}\},\\
 \mathcal L_*&=\{\ell:|j(\ell)|>M^{3/4},\ s(\ell)<M^{1/4}\}.
\end{aligned}
\tag{152.A38l}
$$

They exhaust the actual odd support, including every endpoint.  Thus

$$
 P_U=P_0+P_1+P_2+P_*,\qquad
 |P_0|+|P_1|+|P_2|\ll_\varepsilon X^\varepsilon,
\tag{152.A38m}
$$

and the Round-152 target is reduced, with no overlap, to

$$
 \boxed{
 P_*=
 \sum_{\substack{\ell=\tau s^2\ {\operatorname{retained}}\\
                  |k(\ell)^2-N\ell|>M^{3/4}\\
                  s<M^{1/4}}}
 \chi _4(\ell)w(\ell)e(\sqrt{N\ell})
 \ll_\varepsilon X^\varepsilon.}
\tag{152.A38n}
$$

This is a genuine absolute target-safe pruning, but not a proof of
(152.A38n).  In particular, the top kernel $s=1$, far from integral
square products, is still present as the literal open subwave

$$
 P_{*,s=1}=
 \sum_{\substack{\tau\ \operatorname{odd},\\
                 \tau\ \operatorname{squarefree},\\
                 \mathcal A(\tau)\ne0\\
                 |k(\tau)^2-N\tau|>M^{3/4}}}
 \chi _4(\tau)\tau^{-3/4}\mathcal A(\tau)e(\sqrt{N\tau}).
\tag{152.A38o}
$$

No inner $s$-oscillation remains in (152.A38o), so the pruning does not
silently claim this squarefree-kernel wave.

### 3.4 Mellin conductor, functional equation, and dual length

Set $T=\sqrt{NM}$ and

$$
 \Psi(y)=y^{-3/4}\mathcal A(My)e(T\sqrt y),\qquad
 \widehat\Psi(s)=\int_0^\infty\Psi(y)y^{s-1}\,dy.
\tag{152.A39}
$$

Mellin inversion gives the exact representation

$$
 P_U=M^{-3/4}\frac1{2\pi i}
 \int_{(c)}\widehat\Psi(s)M^sL(s,\chi _4)\,ds,
 \qquad c>1.
\tag{152.A40}
$$

On $s=1/2+it$, the phase of the integral defining
$\widehat\Psi(s)$ is

$$
 2\pi T\sqrt y+t\log y.
\tag{152.A41}
$$

Its stationary relation is $t=-\pi T\sqrt y$.  Hence the transform is
concentrated on $|t|\asymp T$ in an interval of width $\asymp T$, has
stationary size $\ll T^{-1/2}X^\varepsilon$, and decays rapidly away
from that band after the accepted endpoint buffers.  Mellin Plancherel
also gives

$$
 \int_{\mathbb R}|\widehat\Psi(1/2+it)|^2\,dt
 \ll_\varepsilon X^\varepsilon.
\tag{152.A42}
$$

The primitive odd character $\chi _4$ has Gauss sum
$\tau(\chi _4)=2i$ and root number
$\tau(\chi _4)/(i\sqrt4)=+1$.  Its completed function and exact
functional equation are

$$
 \Lambda(s,\chi _4)=
 \left(\frac4\pi\right)^{(s+1)/2}
 \Gamma\!\left(\frac{s+1}{2}\right)L(s,\chi _4),
 \qquad
 \Lambda(s,\chi _4)=\Lambda(1-s,\chi _4),
\tag{152.A43}
$$

or

$$
 L(s,\chi _4)=X_4(s)L(1-s,\chi _4),\qquad
 X_4(s)=\left(\frac4\pi\right)^{1/2-s}
 \frac{\Gamma((2-s)/2)}{\Gamma((s+1)/2)}.
\tag{152.A44}
$$

In particular,

$$
 X_4(1/2+it)=
 \left(\frac4\pi\right)^{-it}
 \frac{\Gamma(3/4-it/2)}{\Gamma(3/4+it/2)},
 \qquad |X_4(1/2+it)|=1.
\tag{152.A45}
$$

Thus the analytic conductor on (152.A41) is
$4(1+|t|)\asymp T$, and the balanced length of an individual approximate
functional equation is $T^{1/2}\asymp RM^{1/4}$.  If one uses any
pointwise bound

$$
 |L(1/2+it,\chi _4)|\ll T^{\theta+\varepsilon}
 \quad(\theta\ge0)
\tag{152.A46}
$$

and takes absolute values in (152.A40), stationary size times transform
width gives

$$
 |P_U|\ll_\varepsilon
 M^{-1/4}T^{1/2+\theta+\varepsilon}
 =R^{1+2\theta}M^{\theta/2}X^\varepsilon.
\tag{152.A47}
$$

Even the hypothetical value $\theta=0$ loses $R$.  Cauchy with
(152.A42) and the standard length-$T$ mean-square scale for $L$ gives the
same $M^{-1/4}T^{1/2}=R$ loss.  Pointwise subconvexity or an approximate
functional equation treated before the $t$-oscillation therefore cannot
prove the target.

Applying (152.A44) without absolute values gives the exact dual kernel

$$
 P_U=M^{-3/4}\sum_{q\ge1}\frac{\chi _4(q)}q
 \mathcal K(Mq),\qquad
 \mathcal K(y)=\frac1{2\pi i}\int
 \widehat\Psi(s)X_4(s)y^s\,ds,
\tag{152.A48}
$$

after the usual residue-free contour move (the primitive nonprincipal
$L$-function is entire).  Stirling in (152.A45), together with
(152.A41), places (152.A48) at $q\asymp T/M$.

The exact constants are most transparently checked through the equivalent
Gauss/Poisson form.  For
$F(x)=x^{-3/4}\mathcal A(x)e(\sqrt{Nx})$, extended by zero,

$$
 \sum_{n\in\mathbb Z}\chi _4(n)F(n)
 =\frac i2\sum_{\substack{q\in\mathbb Z\\q\ {\operatorname{odd}}}}
 \chi _4(q)\widehat F(q/4).
\tag{152.A49}
$$

For $q>0$ the phase $\sqrt{Nx}-qx/4$ has

$$
 x_q=\frac{4N}{q^2},\qquad
 \sqrt{Nx_q}-\frac{qx_q}{4}=\frac Nq,
 \qquad
 \phi_q''(x_q)=-\frac{q^3}{32N},
\tag{152.A50}
$$

and

$$
 x_q^{-3/4}|\phi_q''(x_q)|^{-1/2}=2N^{-1/4}.
\tag{152.A51}
$$

The stationary unit is $e(-1/8)$; multiplication by the Gauss factor
$i/2$ gives $e(1/8)N^{-1/4}$.  Negative $q$ is nonstationary and the
zero frequency is absent.  The accepted actual-profile boundary ledger
therefore gives, with every endpoint and lower symbol included,

$$
 P_U=e(1/8)N^{-1/4}
 \sum_{\substack{q>0\\q\ {\operatorname{odd}}}}
 \chi _4(q)\mathcal A(4N/q^2)e(N/q)
 +O_\varepsilon(X^\varepsilon),
\tag{152.A52}
$$

which is exactly (152.A11).  Its support is
$q\asymp2\sqrt{N/M}=Q$.  Thus the Mellin functional equation, its gamma
factor, and twisted Poisson all reconstruct the accepted reciprocal row;
no main wave can be discarded as an error.

The two elementary capacities for $P_U$ are correspondingly

$$
 |P_U|\ll_\varepsilon
 \min\{M^{1/4},\;R M^{-1/2}\}X^\varepsilon.
\tag{152.A53}
$$

They meet at $M=R^{4/3}$ with loss $R^{1/3}$, and become target-sized
only at bounded $M$ or at $M\asymp R^2$.  They are upper capacities, not
signed lower bounds.

### 3.5 Direct derivatives and exponent-pair powers

On $x\asymp M$,

$$
 f^{(r)}(x)\asymp_r R^2M^{1/2-r},\qquad
 T=R^2M^{1/2},\qquad T/M=R^2M^{-1/2}.
\tag{152.A54}
$$

Resolve the two residue classes modulo 4, apply an unweighted interval
estimate, and then insert the actual weight by Abel summation using
(152.A9).  If an exponent pair $(\kappa,\lambda)$ is legal for the
square-root derivative class, the resulting exact power is

$$
 |P_U|\ll_\varepsilon
 R^{2\kappa}M^{\lambda-\kappa/2-3/4}X^\varepsilon.
\tag{152.A55}
$$

The relevant audited powers are:

| Input | Bound for $P_U$ | Target condition/outcome |
|---|---:|---|
| Bourgain $(13/84,55/84)$ | $R^{13/42}M^{-29/168}=(R^{52}/M^{29})^{1/168}$ | $M^{29}\gg R^{52}$, already inside the owned upper corridor |
| TTY $(89/1282,997/1282)$ used directly | $R^{178/1282}M^{-9/1282}=(R^{178}/M^9)^{1/1282}$ | impossible for $M\le R^2$ |
| $B$(TTY) $=(178/641,365/641)$ | $(R^{1424}/M^{819})^{1/2564}$ | exactly the accepted TTY boundary; positive loss in (152.A1) |

Bourgain's pair is fixed by the $B$-operation.  The $B$(TTY)$ row is
equivalently the accepted application of TTY to the reciprocal phase in
(152.A52).  Both source applications first estimate unweighted intervals
and insert only the actual bounded-variation profile afterwards; neither
source licenses arbitrary weights or supplies an additional character
gain after the mod-four split.

The directly verified classical second- and third-derivative lemmas give,
respectively,

$$
 r=2:\quad |P_U|\ll (RM^{-1/2}+R^{-1})X^\varepsilon,
\tag{152.A57}
$$

$$
 r=3:\quad |P_U|\ll
 (R^{1/3}M^{-1/6}+R^{-1/3}M^{1/6})X^\varepsilon.
\tag{152.A58}
$$

The hypotheses are satisfied because on each fixed dyadic residue
progression $f''$ and $f'''$ have constant sign and fixed-size derivative
ratios given by (152.A54); the actual weight is inserted afterwards by
Abel summation.  The first term in either (152.A57) or (152.A58) is
target-sized only for $M\gg R^2$.

Neither supplied primary-source card states a general $r\ge4$ derivative
theorem with the normalization needed here.  No higher-$r$ formula is
therefore used as certified evidence.  The higher-derivative audit stops
at this exact source-hypothesis obstruction rather than extrapolating an
uncited formula.

### 3.6 Endpoints, parity, and scope

All equalities above use the actual compact profile after zero extension.
Thus (152.A14), (152.A21), (152.A30), (152.A40), and (152.A49) include
the first and last lattice points, a possible short terminal prefix, and
every inherited transition.  The already peeled hard collars are not
reintroduced.  Formula (152.A52), rather than a generic full-Gaussian
formula at a hard endpoint, invokes the accepted Round-148 stationary
buffer, tail, lower-symbol, and endpoint estimate.

No parity of $N$ is discarded.  The only exact-square distinction is
$\nu _2(N)$ even versus odd in (152.A31)--(152.A32); the nonexact defect
formula (152.A35) includes even and odd $m_\tau$.  The floor
$N=\lfloor X\rfloor$ is retained throughout.

The analysis is only for the actual $D=d=L=1$ scalar.  It proves nothing
for the $D>1$ recovery fibre, $L>1$ components, the growing-$M$ generic
sector, the original decomposition's layers $t\ge2$ (distinct from the
temporary squarefree-kernel symbol $\tau$ in (152.A30)), the independent
Round-138 cross owner, full M9--M1, M9--M2, endpoint uniformity, M9, the
conditional bridge, the quarter target, or either global exponent.

## 4. First doubtful or unproved step

The algebraic and power statements (152.A14)--(152.A58), together with
the disjoint pruning (152.A38l)--(152.A38n), are proved under the accepted
actual-profile ledger.  The first unproved mathematical input is the
genuinely signed, coefficient-sensitive residual estimate (152.A38n).
It already contains the explicit open squarefree-kernel subwave
(152.A38o) with $s=1$.

Possible continuations would have to prove joint cancellation among the
correlations (152.A23), including the outer signs $(-1)^h$ rather than
their termwise absolute values; cancellation in $\chi _4(\tau)$ on the
far-defect, small-$s$ residual; or an oscillatory $t$-average of
$L(1/2+it,\chi _4)$ stronger by $R$ than pointwise Lindelof plus mean
square.  Applying the functional equation to the last formulation returns
(152.A52), so it is not an independent input.

Neither audited exponent-pair source supplies (152.A38n) below
$M^{819}\asymp R^{1424}$.  Any claim of a target bound must therefore add
a new theorem at one of these signed interfaces.  The present report does
not assert that such a theorem is impossible.

## 5. Required control test and outcome

| Required control | Outcome |
|---|---|
| `literal_square_root_wave` | GREEN.  Equation (152.A8) retains $\chi _4$, $\ell^{-3/4}$, the exact actual profile, $N=\lfloor X\rfloor$, and positive odd support. |
| `owned_range_exclusion` | GREEN.  Bounded $M$ and $M^{819}\gg R^{1424}$ are excluded; equality is the target-sized TTY endpoint.  No existing owner is recounted. |
| `actual_profile_and_B11_coefficient` | GREEN.  Equations (152.A9)--(152.A11) retain the compact profile, zero extension, transition/boundary ledger, and literal $B_{1,U}(1)$. |
| `adjacent_odd_character_pairing` | GREEN/no-go.  Equations (152.A14)--(152.A18) are exact; the finite phase difference is not replaced by an uncontrolled weight derivative. |
| `A_process_character_survival` | GREEN/no-go.  Even shifts are compulsory, the character product is the constant $(-1)^h$, the diagonal is $M^{-1/2}$, and (152.A2) has no open-range target choice of $H$. |
| `squarefree_kernel_and_exact_square_resonance` | GREEN/strict reduction.  Equation (152.A30) is exact.  The sole possible exact kernel, every nonzero $|j|\le M^{3/4}$ term, and the disjoint $s\ge M^{1/4}$ tail are absolutely target-safe; the residual (152.A38n), including $s=1$, remains open. |
| `Mellin_conductor_and_dual_length` | GREEN/no-go.  $T=R^2M^{1/2}$, width and conductor are $\asymp T$, AFE length is $RM^{1/4}$, root number is $+1$, and the exact dual length is $Q=2\sqrt{N/M}$. |
| `boundary_complete_transform` | GREEN.  Equations (152.A49)--(152.A52) retain the Gauss factor, Fresnel unit, lower symbols, nonstationary terms, stationary buffers, tails, and endpoints through the accepted ledger. |
| `derivative_and_exponent_pair_power` | GREEN/source split.  Equations (152.A55), (152.A57), and (152.A58) and the audited power table reach only owned boundaries.  No uncited general $r\ge4$ derivative formula is retained. |
| `absolute_capacity_vs_signed_sum` | GREEN.  Raw count, absolute mass, pure character mass, exact-square mass, the root-counted $j$-sector, the large-$s$ tail, and the residual signed target are kept distinct; no capacity is called a lower bound. |
| `bounded_intermediate_TTY_endpoint` | GREEN.  Direct/dual capacities cover only bounded/top endpoints, meet with loss $R^{1/3}$ at $M=R^{4/3}$, and (152.A6) is exactly one at $M^{819}=R^{1424}$. |
| `N_parity_and_near_square_controls` | GREEN.  Exact resonance occurs iff the squarefree kernel of $N$ is odd; (152.A35)--(152.A36) retain both near-frequency parities, while the all-prime-power bound (152.A38d) and unique-nearest-integer proof make the small-$j$ owner uniform in every parity of $N$. |
| `D_L_generic_tge2_cross_and_downstream_scope` | GREEN.  Section 3.6 leaves every named complement and downstream owner unchanged. |

No numerical experiment was performed.

## 6. Dependencies and exact artifacts used

Only the context authorized by the task brief was used:

1. `protocol.md`;
2. `state/proof_obligations.yml`, in particular the active Round-151
   character-range, reciprocal-self-return, collar-frontier, and global
   lower-radial nodes and their rejected-inference ledger;
3. `state/active_campaign.yml`;
4. `strategy/round152_d1_square_root_wave_strategy.md`;
5. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/barrier_packet.md`;
6. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/candidates/conductor_round151_character_ranges_and_bprocess_boundary.md`;
7. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/reviews/conductor_round151_adjudication.md`;
8. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/controls/conductor_round151_controls.md`;
9. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`;
10. `sources/tao_trudgian_yang_2025.md`; and
11. `sources/bourgain_2017_exponent_pair.md`.

No sibling Round-152 report, unlisted historical report, web source, or
computational artifact was inspected.

## 7. Recommended state effect

Recommend `promote` the owner-complete arithmetic pruning
(152.A38a)--(152.A38n) under terminal label
`strict_square_root_character_range`.  This label refers to strict
target-safe sectors at every open $M$ scale, not to a newly closed
$M$-interval:

- $j=0$ is the exact square ray and is target-safe by (152.A3);
- $0<|j|\le M^{3/4}$ is absolutely target-safe by the all-parity root
  multiplicity bound (152.A38d)--(152.A38i);
- after those sectors are removed, $s\ge M^{1/4}$ is absolutely
  target-safe by (152.A38j)--(152.A38k); and
- the exact residual is (152.A38n), with the $s=1$ squarefree-kernel wave
  (152.A38o) explicitly open.

Also retain as scoped method obstructions the exact adjacent-pair finite
difference, the legal even-shift $A$-process character loss and
incompatible $H$-conditions (152.A27), the Mellin/functional-equation
self-return, and the verified derivative/exponent-pair ledger ending at
the already owned TTY boundary (152.A6).  Do not create a certified
higher-derivative claim from an uncited formula.

Retain $|P_U|\ll X^\varepsilon$ as open in the range (152.A1).  Make no
change to the $D>1$, $L>1$, generic, original $t\ge2$, Round-138 cross,
M9--M1, M9--M2, endpoint, M9, bridge, target, or exponent obligations.
