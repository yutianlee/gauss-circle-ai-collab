# Round 155 analytic report: exact half-period theta inversion and outer-defect obstruction

- Campaign: `m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate`
- Task: `outer_defect_spectral_dispersion_attack`
- Role: discovery / claimant
- Research round: 155
- Starting graph SHA-256: `84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a`
- Generated: `2026-08-25T11:57:56.2524881+08:00`
- Allocation: 100% analytic and algebraic; 0% numerical
- Status: candidate evidence only

## 1. Result: a masked inverse-Gauss self-return and a route-scoped no-go

The complete half-period theta transform is exactly invertible.  It gives
no cancellation, even before the small-defect mask is restored.  More
precisely, let

$$
 q=4N,\qquad d\mid N,\quad d\text{ odd},\qquad
 c=q_d=\frac qd,\qquad H=\frac c2,
\tag{155.R1}
$$

and use the literal pre-linearization coefficient $B_j$ and finite Fourier
transform

$$
 \widehat B_j(b)=\sum_{x\bmod q}B_j(x)e_q(-bx).
\tag{155.R2}
$$

For every unit $a\bmod c$, put

$$
 \epsilon_a=\begin{cases}1,&a\equiv1\pmod4,\\ i,&a\equiv3\pmod4,
 \end{cases}
 \qquad
 \kappa_c(a)=\epsilon_a\left(\frac ca\right),
\tag{155.R3}
$$

so that the DFI theta Kloosterman sum in the accepted convention is

$$
 K(m,n;c)=\sum_{a\bmod c}^{*}\kappa_c(a)
 e_c(m\bar a+na).
\tag{155.R4}
$$

Then the complete $v\bmod H$ resummation is

$$
 \boxed{
 \begin{aligned}
 &\sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)\\
 &\quad=\frac{1-i}{2}\sqrt c
 \sum_{x\bmod q}B_j(x)
 \sum_{a\bmod c}^{*}\chi_4(a)e_c\!\left(a(x^2-j)\right).
 \end{aligned}}
\tag{155.R5}
$$

After the selector, Fourier, Gauss, and half-Gauss constants are restored,
the exact ambient block becomes

$$
 \boxed{
 \mathcal T_U(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod q}B_j(x)
 {\bf1}_{N\mid x^2-j}\chi_4\!\left(\frac{x^2-j}{N}\right).}
\tag{155.R6}
$$

Thus unrestricted expansion of $K$ followed by complete $v$-summation is
finite Fourier/Gauss inversion back to the same masked, endpoint-sensitive
selector.  There is no residual factor $c^{-1/2}$, $d^{-1/2}$, or
$N^{-1/2}$ that could be called a transform gain.  This is a rigorous
no-go for **complete** $v$-resummation, not for every possible incomplete
or signed joint theorem.

The zero mode is an independent degenerate term.  The literal support and
DFI bound give the explicit estimate

$$
 \mathcal T_{0,U}(V)
 \ll_\varepsilon
 \left(N^{-1/2}M^{-1/4}V+M^{-1/4}\right)X^\varepsilon.
\tag{155.R7}
$$

At $V=K=\sqrt{NM}$ this is $M^{1/4}+M^{-1/4}$, so absolute treatment of
the zero mode is not target-sized at the top.  The accepted nonzero-mode
BV/DFI ledger remains

$$
 \mathcal T_{\ne0,U}(V)
 \ll_\varepsilon M^{-3/4}V X^\varepsilon,
\tag{155.R8}
$$

and hence reproduces the accepted total bound

$$
 \mathcal T_U(V)
 \ll_\varepsilon
 \left(M^{-3/4}V+M^{-1/4}\right)X^\varepsilon.
\tag{155.R9}
$$

No full target and no owner-complete positive-power range follows.  The
new rigorous result is the exact masked inverse-transform obstruction
(155.R5)--(155.R6), together with the zero-mode and sampled-Parseval
ledgers below.  The appropriate round label for this report is
`outer_defect_theta_dispersion_no_go`.

## 2. Exact statement and hypotheses

Fix $A>0$ and

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J_A=M^{3/4}(\log(2X))^A,\qquad K=\sqrt{NM},
\tag{155.R10}
$$

with the inherited range $1\ll M\le R^2$, and take a dyadic block
$J_A<V\le K$.  The selected linearized scalar is

$$
 \mathcal Q_U(V)=
 \sum_{\substack{k\ge1,\ -k\le j\le k-1\\
 V<|j|\le2V,\ N\mid k^2-j\\
 (k^2-j)/N\text{ positive odd}}}
 \chi_4\!\left(\frac{k^2-j}{N}\right)
 w_U\!\left(\frac{k^2-j}{N}\right)e\!\left(-\frac j{2k}\right).
\tag{155.R11}
$$

The literal $B_j(x)$ used in (155.R2) instead retains the exact residual
phase

$$
 e\!\left(\sqrt{x^2-j}-x\right)
 =e\!\left(-\frac{j}{x+\sqrt{x^2-j}}\right),
\tag{155.R12}
$$

the actual zero-extended profile, every support component and transition,
the asymmetric cell $-x\le j\le x-1$, the strict dyadic mask, both signs,
and the hard endpoints.  It has

$$
 |B_j(x)|\ll_\varepsilon M^{-3/4}X^\varepsilon,\qquad
 \#\operatorname{supp}_x B_j\ll KX^\varepsilon,
\tag{155.R13}
$$

and the accepted bounded-variation bound of the same
$M^{-3/4}X^\varepsilon$ scale.  The external factor $B_{1,U}(1)$ remains
outside and is only $O_\varepsilon(X^\varepsilon)$.

The exact ambient expression is

$$
 \mathcal T_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\text{ odd}}}
 \chi_4(d)d\sqrt c
 \sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c),
\tag{155.R14}
$$

where $c=4N/d$ and $H=c/2$.  Formula (155.R5) holds for every integer
$N$, including even and highly imprimitive $N$, every odd $d\mid N$, and
arbitrary $B_j$ on $\mathbb Z/q\mathbb Z$.  It therefore preserves rather
than smooths or separates the literal coefficient.

For later Cauchy or large-sieve placements define the exact folded
coefficient

$$
 C_{j,d}(r)=
 \sum_{\substack{x\bmod q\\x\equiv r\pmod H}}B_j(x),
 \qquad r\bmod H.
\tag{155.R15}
$$

Then sampled Parseval is the identity

$$
 \boxed{
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 =H\sum_{r\bmod H}|C_{j,d}(r)|^2
 =H\!\sum_{\substack{x,y\bmod q\\x\equiv y\pmod H}}
 B_j(x)\overline{B_j(y)}.}
\tag{155.R16}
$$

It is not $q\sum_x|B_j(x)|^2$ in the large-$d$ strata.  If the total
$x$-span is $O(K)$, the collision multiplicity is at most
$O(1+K/H)$, and therefore

$$
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 \ll_\varepsilon
 \left(\frac{NK}{d}+K^2\right)M^{-3/2}X^\varepsilon
 =\left(\frac{N^{3/2}}{dM}+\frac{N}{M^{1/2}}\right)X^\varepsilon.
\tag{155.R17}
$$

This is an upper capacity, not a signed lower bound and not a large-sieve
saving.

## 3. Proof and derivation

### 3.1 The complete half-period Gauss transform

Because $c\equiv0\pmod4$ and $a$ is odd, the summand in

$$
 I_c(a,x)=\sum_{v\bmod H}e_c(-\bar a v^2-2xv)
\tag{155.R18}
$$

really has period $H=c/2$: under $v\mapsto v+H$, the change in the
exponent divided by $c$ is

$$
 -\bar a v-\bar a\frac c4-x\in\mathbb Z.
\tag{155.R19}
$$

Completing the square gives

$$
 -\bar a v^2-2xv
 \equiv-\bar a(v+ax)^2+ax^2\pmod c,
\tag{155.R20}
$$

so translation modulo $H$ yields

$$
 I_c(a,x)=e_c(ax^2)
 \sum_{v\bmod H}e_c(-\bar a v^2).
\tag{155.R21}
$$

The full quadratic Gauss sum is twice this half-period sum.  In the same
normalization used in the accepted completion,

$$
 \sum_{v\bmod c}e_c(Av^2)
 =(1+i)\epsilon_A^{-1}\left(\frac cA\right)\sqrt c
 \qquad(A,c)=1.
\tag{155.R22}
$$

Now $\bar a\equiv a\pmod4$, whence
$\epsilon_{-\bar a}^{-1}=-i\epsilon_a$.  The Kronecker character
$u\mapsto(c/u)$ is a quadratic character on the odd units modulo $c$, so

$$
 \left(\frac c{-\bar a}\right)
 =\left(\frac c{\bar a}\right)
 =\left(\frac ca\right).
\tag{155.R23}
$$

Equations (155.R21)--(155.R23) give the exact inverse kernel

$$
 \boxed{I_c(a,x)=\frac{1-i}{2}\kappa_c(a)\sqrt c\,e_c(ax^2).}
\tag{155.R24}
$$

Since $\kappa_c(a)^2=\epsilon_a^2(c/a)^2=\chi_4(a)$, expanding both
$\widehat B_j$ and $K$ and inserting (155.R24) proves (155.R5):

$$
 \begin{aligned}
 &\sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)\\
 &=\sum_{x\bmod q}B_j(x)
 \sum_{a\bmod c}^{*}\kappa_c(a)e_c(-aj)I_c(a,x)\\
 &=\frac{1-i}{2}\sqrt c
 \sum_{x\bmod q}B_j(x)
 \sum_{a\bmod c}^{*}\chi_4(a)e_c(a(x^2-j)).
 \end{aligned}
\tag{155.R25}
$$

No coprimality, two-adic, or multiplier stratum has been suppressed.

### 3.2 Restoration of every normalization

Insert (155.R25) into (155.R14).  For a fixed $d$, the product of the
finite-Fourier, completed-Gauss, and inverse-half-Gauss powers is

$$
 \frac1q\,(d\sqrt c)\left(\frac{\sqrt c}{2}\right),
 \qquad dc=q.
\tag{155.R26}
$$

The complex constants satisfy $(1+i)(1-i)=2$.  Consequently

$$
 -\frac{i(1+i)}{2Nq}\,d\sqrt c\,\frac{1-i}{2}\sqrt c
 =-\frac{i}{2N}.
\tag{155.R27}
$$

Thus

$$
 \mathcal T_U(V)=
 -\frac{i}{2N}
 \sum_{V<|j|\le2V}\sum_{x\bmod q}B_j(x)
 \sum_{\substack{d\mid N\\d\text{ odd}}}\chi_4(d)
 \sum_{a\bmod(4N/d)}^{*}\chi_4(a)
 e_{4N/d}(a(x^2-j)).
\tag{155.R28}
$$

Odd residues $h\bmod4N$ are partitioned uniquely by

$$
 d=(h,N),\qquad h=da,\qquad
 a\in(\mathbb Z/(4N/d)\mathbb Z)^*.
\tag{155.R29}
$$

Here $d$ is automatically odd, including when $N$ is even.  Moreover
$\chi_4(h)=\chi_4(d)\chi_4(a)$ and
$e_q(h(x^2-j))=e_c(a(x^2-j))$.  Therefore the last two sums in
(155.R28) are precisely the exact quotient selector

$$
 -\frac{i}{2N}\sum_{\substack{h\bmod4N\\h\text{ odd}}}
 \chi_4(h)e_q(h(x^2-j))
 ={\bf1}_{N\mid x^2-j}\chi_4\!\left(\frac{x^2-j}{N}\right).
\tag{155.R30}
$$

This proves (155.R6).  Since the argument is pointwise in $j$ and arbitrary
in $B_j$, it retains the strict outer block, both signs, every support
component, all transitions, the hard endpoints, and the exact residual
phase.  It does not move the accepted selected-graph linearization onto an
off-congruence array.

### 3.3 Zero mode and the complete $N$--$M$--$V$--$d$ ledger

The $v=0$ term of (155.R14) is exactly

$$
 \mathcal T_{0,U}(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\text{ odd}}}
 \chi_4(d)d\sqrt c\,\widehat B_j(0)K(0,-j;c).
\tag{155.R31}
$$

DFI gives

$$
 |K(0,-j;c)|\le(j,c)^{1/2}c^{1/2}\tau(c).
\tag{155.R32}
$$

At this point the exact power cancellation is

$$
 \frac{d\sqrt c\,c^{1/2}}{Nq}=\frac1N,
\tag{155.R33}
$$

not $N^{-1/2}$ and not $d^{-1/2}$.  From (155.R13),

$$
 |\widehat B_j(0)|
 \le\sum_x|B_j(x)|
 \ll_\varepsilon K M^{-3/4}X^\varepsilon.
\tag{155.R34}
$$

For every $c$ and dyadic signed block,

$$
 \sum_{V<|j|\le2V}(j,c)^{1/2}
 \le\sum_{r\mid c}r^{1/2}
 \#\{j:V<|j|\le2V,\ r\mid j\}
 \ll_\varepsilon(V+c^{1/2})c^\varepsilon.
\tag{155.R35}
$$

Since $c=4N/d$ and
$\sum_{d\mid N}d^{-1/2}\ll_\varepsilon N^\varepsilon$, (155.R31)--(155.R35)
give

$$
 \begin{aligned}
 |\mathcal T_{0,U}(V)|
 &\ll_\varepsilon
 \frac{K M^{-3/4}}{N}
 \left(V+N^{1/2}\right)X^\varepsilon\\
 &=\left(N^{-1/2}M^{-1/4}V+M^{-1/4}\right)X^\varepsilon,
 \end{aligned}
\tag{155.R36}
$$

which is (155.R7).  This slightly sharpens the zero-mode portion of the
coarser accepted total estimate but does not close the top: at $V=K$ its
first term is $M^{1/4}$.  It is only an upper bound; it is not evidence that
the zero mode is actually large.

For $v\ne0$, DFI and (155.R33) give the exact pre-BV expression

$$
 |\mathcal T_{\ne0,U}(V)|
 \ll_\varepsilon
 \frac1N\sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\text{ odd}}}
 \sum_{\substack{v\bmod H\\v\ne0}}
 |\widehat B_j(2dv)|(v^2,j,c)^{1/2}X^\varepsilon.
\tag{155.R37}
$$

The accepted literal BV and divisor ledger for (155.R37) is
$M^{-3/4}X^\varepsilon$ per outer $j$, proving (155.R8).  In particular,
all $V$ outer defects have to be restored.  The full power ledger is:

| Placement | Restored size (up to $X^\varepsilon$) | At $V=K=\sqrt{NM}$ |
|---|---:|---:|
| Complete $v$ inversion | $(dc/q)(1/(2N))=1/(2N)$, the exact selector normalization | no gain; identity |
| Zero mode, absolute | $N^{-1/2}M^{-1/4}V+M^{-1/4}$ | $M^{1/4}+M^{-1/4}$ |
| Nonzero modes, termwise DFI/BV | $M^{-3/4}V$ | $N^{1/2}M^{-1/4}$ |
| Total accepted termwise bound | $M^{-3/4}V+M^{-1/4}$ | $N^{1/2}M^{-1/4}+M^{-1/4}$ |
| Selected absolute incidence capacity | $M^{-3/4}V$ | $N^{1/2}M^{-1/4}$ |
| Hypothetical square-root incidence cancellation | $M^{-3/4}V^{1/2}$ | $N^{1/4}M^{-1/2}$ |

The last line would be target-sized only for

$$
 V\le M^{3/2};
\tag{155.R38}
$$

at the top it requires $M\ge N^{1/2}$.  Since the inherited upper range is
$M\le R^2\asymp N^{1/2}$, square-root incidence cancellation alone closes
the top only at that boundary, not uniformly below it.

### 3.4 Truncated transforms do not separate the literal coefficient

Let $\eta$ be any weight on $\mathbb Z/H\mathbb Z$.  Repeating the square
completion without setting $\eta\equiv1$ gives

$$
 \begin{aligned}
 &\sum_{v\bmod H}\eta(v)e_c(-\bar a v^2-2xv)\\
 &\qquad=e_c(ax^2)
 \sum_{u\bmod H}\eta(u-ax)e_c(-\bar a u^2).
 \end{aligned}
\tag{155.R39}
$$

The translated cutoff $\eta(u-ax)$ couples $a$ and $x$.  Thus a proper
frequency truncation does not produce a product of a $j$-coefficient and a
$v$-coefficient, nor a bounded separated surrogate for
$\widehat B_j(2dv)$.  The only cutoff for which the translation disappears
is the complete cutoff $\eta\equiv1$, and that is exactly the self-return
(155.R5).

Taking $\eta={\bf1}_{v\ne0}$ gives the particularly transparent identity

$$
 \mathcal T_{\ne0,U}(V)=\mathcal T_U(V)-\mathcal T_{0,U}(V).
\tag{155.R40}
$$

Hence a theorem for all nonzero modes that is combined only with the
absolute zero-mode bound has not bypassed the original signed scalar; it
has rewritten it minus the explicit degenerate term.

### 3.5 Poisson localization, sampled Parseval, and dispersion diagonals

On the selected linearized graph, for fixed $k\asymp K$ the phase slope in
the defect is

$$
 \frac{\partial}{\partial j}\left(-\frac j{2k}\right)=-\frac1{2k},
 \qquad
 \operatorname{osc}_{|j|\asymp V}\frac j{2k}
 \ll\frac VK\le1.
\tag{155.R41}
$$

In fact, because $2k<N$, divisibility selects at most one $j$ in the whole
nearest cell for a fixed $k$.  Bare archimedean $j$-integration therefore
cannot provide square-root cancellation.

After expanding $K$, the exact residual phase for fixed $x$ has derivative

$$
 \frac{\partial}{\partial j}
 \left(\sqrt{x^2-j}-x-\frac{aj}{c}\right)
 =-\frac1{2\sqrt{x^2-j}}-\frac ac.
\tag{155.R42}
$$

Poisson or first-derivative localization in a block of length $V$ thus
requires

$$
 \left\|\frac ac+\frac1{2x}\right\|_{\mathbb R/\mathbb Z}
 \ll\frac1V.
\tag{155.R43}
$$

For each unit $a\bmod c$, choose its signed lift
$a^\sharp\in(-c/2,c/2]$.  Then (155.R43) is the circular arc

$$
 \left|\frac{a^\sharp}{c}+\frac1{2x}\right|\ll\frac1V,
 \qquad \text{arc centre }a_0^\sharp=-\frac c{2x}\asymp-\frac cK,
\tag{155.R44}
$$

in an interval containing at most $O(1+c/V)$ integers.  For a nonempty
fixed-$x$ defect block one has $V<x$, so its radius $c/V$ exceeds the
centre offset $c/(2x)$ and the circular arc crosses $0$.  In positive
representatives $0\le a<c$, its $a^\sharp>0$ part lies near $a=0$, while
its $a^\sharp<0$ part lies near $a=c-c/(2x)$; both pieces are included in
the single $O(1+c/V)$ capacity.  This is the principal reciprocal
small-frequency arc.  Localization has not supplied a square-root factor;
it has only moved the flat selected phase to the same centered unit arc
that participates in the inverse selector.  At $V=K$ the arc still has
capacity $O(1+c/K)$, with
$c/K\asymp d^{-1}\sqrt{N/M}$.  Its strict-mask and endpoint boundary terms
remain part of $B_j$.

For a Cauchy, spectral-large-sieve, or two-variable dispersion placement,
(155.R16) follows directly from

$$
 \widehat B_j(2dv)
 =\sum_{r\bmod H}C_{j,d}(r)e_H(-vr).
\tag{155.R45}
$$

The collision condition is

$$
 x-y\equiv0\pmod H,\qquad H=\frac{2N}{d}.
\tag{155.R46}
$$

For $d\ll N/K\asymp\sqrt{N/M}$ the literal support span is shorter than
$H$ and only the physical diagonal occurs.  For
$d\gtrsim N/K$, additional folds occur with multiplicity
$O(1+dK/N)$.  This proves (155.R17).  A generic coefficient large sieve
must carry this exact folded norm; it cannot replace it by an independent
$j$-sequence and $v$-sequence.  Conversely, (155.R16)--(155.R17) are only
positive capacities.  They neither lower-bound the signed scalar nor prove
that an off-diagonal estimate is impossible.

No Kuznetsov formula is invoked here.  The family has fixed moduli
$c=4N/d$, not a supplied smooth modulus average, and its coefficient after
any proper $v$ cutoff is the translated chirp (155.R39).  A future spectral
placement must separately restore its zero/degenerate term, continuous and
exceptional spectrum, modulus weights, literal endpoints, and all $d$.
Calling an arbitrary-coefficient spectral right side a signed gain would
not establish the required theorem.

## 4. First doubtful or unproved step

The first unproved step after the exact algebra is a genuinely signed
estimate for a **properly incomplete** transform with kernel (155.R39), or
equivalently a signed selected cross-fibre theorem for (155.R11).  Such an
estimate must simultaneously:

1. control the degenerate zero mode (155.R31), rather than omit it;
2. exploit cancellation across the outer $j$ order, because the phase has
   only $O(V/K)$ archimedean variation and, for odd $N$, the quotient
   character is constant within each fixed-$j$ root fibre;
3. retain the moving, nonseparable $B_j(x)$ coefficient and the folds
   $x-y\equiv0\pmod{2N/d}$;
4. beat $M^{-3/4}V$ by enough to reach at least the square-root scale, with
   a second mechanism above $V=M^{3/2}$ when $M<N^{1/2}$; and
5. include both signs, transitions, hard endpoints, every odd $d\mid N$,
   and the external $B_{1,U}(1)$ seam.

Complete $v$-resummation cannot be that step: (155.R5)--(155.R6) proves it
is the inverse transform.  Poisson localization alone cannot be that step:
(155.R41)--(155.R44) only selects the reciprocal unit arc.  Sampled
Parseval or arbitrary-coefficient Cauchy cannot be that step:
(155.R16) retains the diagonal and large-$d$ folds.  No estimate satisfying
the five requirements above is proved in this report.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_outer_defect_block` | GREEN.  Equations (155.R11)--(155.R14) retain the literal profile, strict block, quotient, cell, and exact residual phase. |
| `selected_ambient_equivalence_and_linearization_scope` | GREEN.  The inverse calculation uses exact ambient $B_j$; the accepted linearization is mentioned only for the selected graph. |
| `exact_Bj_and_nonseparable_coefficient` | GREEN/no separation.  Formula (155.R39) proves every proper $v$ cutoff remains jointly dependent on $a$ and $x$; no surrogate is inserted. |
| `mod4N_selector_and_full_normalization` | GREEN.  The factors $-i/(2N)$, $1/q$, $d\sqrt c$, $\sqrt c/2$, and both eighth-root constants give exactly (155.R27)--(155.R30). |
| `all_gcd_two_adic_and_multiplier_strata` | GREEN.  Every odd $d=(h,N)$ is retained; $c=4N/d\equiv0\pmod4$ for arbitrary even or odd $N$; the exact $\epsilon_a(c/a)$ multiplier is squared to $\chi_4(a)$. |
| `zero_mode_and_exceptional_terms` | GREEN/scoped obstruction.  The exact zero term is (155.R31) and its bound is (155.R36).  No principal, continuous, or exceptional spectral term is silently discarded; no spectral theorem is invoked. |
| `complete_vs_truncated_v_transform` | GREEN.  Complete $\eta=1$ gives exact inversion; a proper cutoff gives the translated chirp (155.R39); $v\ne0$ is exactly total minus zero. |
| `inverse_Gauss_self_return_test` | GREEN/no gain.  Equations (155.R18)--(155.R30) prove exact masked self-return with all constants. |
| `positive_negative_defect_and_cell_endpoints` | GREEN.  The proof is pointwise in $j$ and arbitrary in $B_j$, so both signs and $-x\le j\le x-1$ survive unchanged. |
| `N_M_V_d_power_ledger` | GREEN.  Equations (155.R33)--(155.R38) and the table restore $q,c,d,N,M,V$ before any conclusion. |
| `actual_profile_transitions_and_B11` | GREEN.  Exact inversion is valid for the literal zero-extended coefficient, including transitions and hard endpoints; $B_{1,U}(1)$ remains external and costs only $X^\varepsilon$. |
| `Cauchy_Parseval_diagonal_and_collision_scope` | GREEN/no signed inference.  Equations (155.R15)--(155.R17) give the exact sampled norm and all folds; the capacity is not treated as a lower bound. |
| `square_root_range_V_le_Mthreehalves` | GREEN.  The hypothetical square-root size and its precise limit $V\le M^{3/2}$ are printed; no such cancellation is claimed. |
| `absolute_capacity_vs_signed_sum` | GREEN.  Root counts, the zero-mode majorant, Parseval norms, and theorem right sides are used only as upper capacities; the circular reciprocal-arc count includes both positive-representative pieces. |
| `D_L_generic_tge2_cross_and_downstream_scope` | GREEN.  Nothing is claimed for $D>1$, $L>1$, generic $t=1$, original $t\ge2$, the Round-138 cross owner, other M1 owners, M2, endpoint assembly, M9, the bridge, or either global exponent. |

The control calculation used no numerical experiment.

## 6. Dependencies and exact artifacts used

This report used only the permitted context:

1. `protocol.md`;
2. `state/proof_obligations.yml`, in particular the current Round-154
   root-defect, theta-source, root-dispersion, large-wrap, and global
   lower-radial nodes;
3. `state/active_campaign.yml`;
4. `strategy/round155_d1_outer_defect_theta_dispersion_strategy.md`;
5. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/barrier_packet.md`;
6. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/candidates/conductor_round155_outer_defect_seed.md`;
7. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md`;
8. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reviews/conductor_round154_adjudication.md`; and
9. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/controls/conductor_round154_controls.md`.

The DFI Gauss and Kloosterman conventions are inherited only through those
accepted, source-audited Round-154 artifacts.  No new external theorem,
web source, sibling Round-155 report, computation, or shared-state artifact
was used.

## 7. Recommended state effect

**Promote after independent seam review only as a route-scoped
obstruction:** record (155.R5)--(155.R6) as the exact half-period,
mask-preserving inverse-Gauss self-return and record (155.R16) as the exact
sampled-Parseval collision identity.  Retain (155.R7)--(155.R9) as upper
ledgers, not lower bounds.

Retain the signed outer-defect target beyond every fixed polylogarithmic
collar as open.  Reject any inference that complete $v$-summation,
deletion of $v=0$, bare $j$-Poisson, or an arbitrary-coefficient spectral
large sieve supplies a new gain without the incomplete-kernel and total
norm ledger above.  Make no positive-power owner, $M$-range, downstream
obligation, endpoint, M9, bridge, target, or exponent change.
