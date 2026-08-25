# Round 154 discovery report: exact root-defect dispersion attack

- Campaign: `m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate`
- Task: `large_defect_root_dispersion_attack`
- Role: discovery
- Starting graph SHA-256: `6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`
- Allocation used: 100% analytic/algebraic, 0% numerical
- Proposed terminal label: `large_defect_root_dispersion_no_go`

## 1. Result: an exact Fourier-rank collapse and a scoped all-scale no-go

The conductor's root-defect coordinate and modulo-$4N$ identity are exact.
They do not, however, create a genuine family of $2N$ independent Fourier
rows on the literal wave.  If the odd quotient condition has already been
imposed, the $2N$ odd frequencies modulo $4N$ are $N$ identical copies of
each of two modulo-four rows, and those two rows become negatives of one
another on odd quotients.  Thus the Fourier family has rank at most two on
all quotient residues and rank one on the literal odd-quotient support.
With the normalization in the conductor seed, Cauchy in the Fourier
frequency is an exact equality, not a saving.

More precisely, if the character is removed from the coefficient and the
unnormalized $h$-row is denoted by $T_h$, then

$$
 T_{1+4m}=iQ_U,\qquad T_{3+4m}=-iQ_U
 \qquad(0\le m<N),
\tag{154.D1}
$$

and

$$
 Q_U=-\frac{i}{2N}
 \sum_{\substack{h\bmod 4N\\h\ \mathrm{odd}}}\chi _4(h)T_h,
 \qquad
 \frac1{2N}\sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}|T_h|^2
 =|Q_U|^2.
\tag{154.D2}
$$

The associated pair kernel retains every ordered pair of literal odd
quotients, with its original product of characters; it does not reduce to
the equality diagonal.  This is a rigorous no-go only for
post-selection Fourier-frequency averaging or Cauchy.  It must be
distinguished from the lawful ambient selector expansion: before
$N\mid k^2-j$ is imposed, the rows contain off-congruence values of
$t=k^2-j$ and are not repeated modulo-four rows.  Those ambient rows may be
quadratic-completed, and are tested separately below.

All imprimitive and two-adic complete quadratic Gauss sums can also be
evaluated exactly.  After the incomplete $k$-interval, both defect signs,
all dyadic $j$-blocks, the $h$-average, the actual bounded-variation profile,
and the endpoint remainder are restored, termwise quadratic completion
gives only

$$
 |Q_{U,\sigma,\Delta}|
 \ll_\varepsilon
 \Delta M^{-3/4}\bigl(\sqrt N+\sqrt M\bigr)X^\varepsilon,
 \qquad J\ll\Delta\ll K,
\tag{154.D3}
$$

where $K=\sqrt{NM}$ and $\sigma\in\{+,-\}$.  Already at
$\Delta\asymp J=M^{3/4}$ this ledger has the loss
$\sqrt N+\sqrt M$.  Summing the $h$-rows coherently instead of termwise
merely reconstructs the signed modulo-$4N$ root selector.  Direct
fixed-$j$ Cauchy then reproduces the absolute root capacity; for prime $N$
there is at most one supported root for each nonzero $j$, so there is no
fixed-$j$ root cancellation at all.

There is a second, distinct ambient conclusion.  Restore the Round-152
exact- and small-defect sectors at scalar level, expand the selector on the
full nearest-cell partition, and center a negative frequency as
$h=4N-a$.  The exact combined $j$-phase has stationary point

$$
 \sqrt{k^2-j_*}=\frac{2N}{a},\qquad
 \frac{k^2-j_*}{N}=\frac{4N}{a^2},\qquad
 e(\Psi_a(j_*))=e(N/a).
\tag{154.D3a}
$$

Its stationary symbol, including the Fourier normalization and character
sign, is exactly
$e(1/8)N^{-1/4}\chi _4(a)A_U(4N/a^2)$.  With the already accepted
boundary, transition, and nonstationary ledger this reconstructs the
Round-151 reciprocal row, not a new estimate.  Thus the principal lawful
ambient stationary completion is an exact $B$-process self-return.  This
still does not exclude a new joint treatment of a nonprincipal or masked
correlation not covered by that principal transform.

Accordingly, post-selection frequency Cauchy, termwise absolute
off-congruence Gauss completion, and coefficient-blind fixed-root
dispersion give no target and no new power range anywhere on
$1\ll M\le R^2$, in particular below $M^{449}\asymp R^{780}$.  This is
deliberately route-scoped.  It does not rule out a genuinely joint signed
ambient $h$-$k$-$j$ completion, or a selected signed $k$-$j$ theorem, which
keeps the quotient character, exact reciprocal-defect phase, actual
profile, and all defect blocks together.  No capacity below is used as a
signed lower bound.

## 2. Exact statement and hypotheses

Let

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 1\ll M\le R^2,\qquad J=M^{3/4},\qquad K=\sqrt{NM},
\tag{154.D4}
$$

and work on the open side $M^{449}\ll R^{780}$.  Retain the literal
Round-148 profile, including its zero extension, its finitely many support
components and half-open endpoints, and put

$$
 w_U(x)=x^{-3/4}A_U(x).
\tag{154.D5}
$$

The accepted profile ledger is

$$
 \operatorname {supp}A_U\subset[cM,CM],\qquad
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon M^{-3/4}X^\varepsilon,
\tag{154.D6}
$$

with fixed positive dilation constants $c,C$.  The external row factor
$B_{1,U}(1)$ is not inserted into the scalar and satisfies
$|B_{1,U}(1)|\ll_\varepsilon X^\varepsilon$.

For every retained positive odd $n$, set

$$
 k=k(n)=\left\lfloor\sqrt{Nn}+\frac12\right\rfloor,
 \qquad j=j(n)=k^2-Nn,
\tag{154.D7}
$$

and define

$$
 \phi(k,j)=\sqrt{k^2-j}-k
 =-\frac{j}{k+\sqrt{k^2-j}}.
\tag{154.D8}
$$

The literal returned large-defect scalar is

$$
 Q_U=
 \sum_{\substack{n>0, n\ \mathrm{odd}\\
                   |k(n)^2-Nn|>J}}
 \chi _4(n)w_U(n)e(\sqrt{Nn}).
\tag{154.D9}
$$

Round 152's exact and $0<|j|\le J$ owners have been subtracted at scalar
level before (154.D9) is considered.  No such mask is deleted after a
Cauchy step.

The conclusions proved here are the following.

1. The map $n\mapsto(k,j)$ is a bijection from (154.D9) to the pairs
   $k\ge1$, $-k\le j\le k-1$, $|j|>J$, $N\mid k^2-j$, with positive odd
   quotient $n=(k^2-j)/N$ in the literal support.  Both cell endpoints are
   included, and there is no tie.
2. For every integer $t$ and every parity and prime-power structure of $N$,

   $$
   \begin{aligned}
   G_N(t)&={\bf1}_{N\mid t}\chi _4(t/N)\\
   &={\bf1}_{t\equiv N\ (\mathrm{mod}\ 4N)}
     -{\bf1}_{t\equiv3N\ (\mathrm{mod}\ 4N)}\\
   &=-\frac{i}{2N}
     \sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}
     \chi _4(h)e\!\left(\frac{ht}{4N}\right).
   \end{aligned}
   \tag{154.D10}
   $$

3. On the selected graph $t=Nn$ with $n$ odd, (154.D10) has the exact
   rank collapse (154.D1)--(154.D2).
4. Complete and incomplete quadratic completion obey the all-gcd formula
   and the restored power bound proved in Section 3 below.  Neither it nor
   fixed-$j$ root Cauchy closes any power range.
5. The principal stationary phase of the lawful full-cell ambient expansion
   is exactly the already accepted reciprocal row, after the owned masks are
   restored before expansion.

## 3. Proof and derivation

### 3.1 Nearest cell, converse, support, and injectivity

A half-integer tie would give
$4Nn=(2k+1)^2$, impossible because the left side is divisible by four and
the right side is odd.  Hence

$$
 k-\frac12<\sqrt{Nn}<k+\frac12.
\tag{154.D11}
$$

After squaring, integrality of $k^2-Nn$ gives exactly

$$
 -k\le j\le k-1.
\tag{154.D12}
$$

The upper endpoint $j=k-1$ corresponds to
$k^2-k+1>(k-1/2)^2$, and the lower endpoint $j=-k$ corresponds to
$k^2+k<(k+1/2)^2$.  Conversely, (154.D12) gives

$$
 (k-\tfrac12)^2<k^2-j<(k+\tfrac12)^2.
\tag{154.D13}
$$

Also $k^2-j\ge k^2-k+1>0$, so divisibility by $N$ and positivity of the
quotient recover a unique original $n$.

On (154.D6), $k\asymp K$ and all supported $k$ lie in an ambient interval
of length $O(K)$.  Since $M\le R^2$ and $N\asymp R^4$, fixed-dilate
constants give, for sufficiently large $X$,

$$
 2k<N,\qquad O(K)<N.
\tag{154.D14}
$$

The cell in (154.D12) contains $2k<N$ consecutive integers, so a fixed $k$
has at most one representative of $k^2\pmod N$ in the cell.  If
$n_2>n_1$ are two supported integers, then

$$
 \sqrt{Nn_2}-\sqrt{Nn_1}
 =\frac{N(n_2-n_1)}{\sqrt{Nn_2}+\sqrt{Nn_1}}
 \gg\sqrt{\frac NM}>1,
\tag{154.D15}
$$

again for sufficiently large $X$.  Their nearest integers are therefore
distinct.  The reparametrization creates neither multiplicity nor a second
free summation variable.

The quotient parity conditions can be written without any assumption on
$N$:

$$
 n\ \mathrm{odd}
 \quad\Longleftrightarrow\quad
 k^2-j\equiv N\pmod {2N},
\tag{154.D16}
$$

and, on this class,

$$
 \chi _4(n)=
 \begin{cases}
  +1,&k^2-j\equiv N\pmod {4N},\\
  -1,&k^2-j\equiv3N\pmod {4N}.
 \end{cases}
\tag{154.D17}
$$

In particular $j\equiv k-N\pmod2$: $j$ and $k$ have the same parity when
$N$ is even and opposite parity when $N$ is odd.  Equations
(154.D16)--(154.D17) prove the first two lines of (154.D10), including all
two-adic cases.

### 3.2 Exact quotient-character Fourier identity

Write an odd frequency uniquely as $h=r+4m$, where
$r\in\{1,3\}$ and $0\le m<N$.  Then

$$
 \sum_{m=0}^{N-1}e\!\left(\frac{(r+4m)t}{4N}\right)
 =e\!\left(\frac{rt}{4N}\right)
  \sum_{m=0}^{N-1}e\!\left(\frac{mt}{N}\right).
\tag{154.D18}
$$

This vanishes unless $N\mid t$.  If $t=Nq$, the two $r$-rows give

$$
 N\{e(q/4)-e(3q/4)\}=2iN\chi _4(q),
\tag{154.D19}
$$

also when $q$ is even, when both sides vanish.  Multiplication by
$-i/(2N)$ proves the final line of (154.D10) with its exact sign and
normalization.

### 3.3 The $h$-rows have rank one on the literal support

Let $\mathcal P_U$ denote the literal pair set in the bijection, and remove
only the quotient character from each coefficient:

$$
 c_{k,j}=n_{k,j}^{-3/4}A_U(n_{k,j})e(\phi(k,j)),
 \qquad
 Q_U=\sum_{(k,j)\in\mathcal P_U}\chi _4(n_{k,j})c_{k,j}.
\tag{154.D20}
$$

For each odd $h\bmod4N$, define the unnormalized row

$$
 T_h=\sum_{(k,j)\in\mathcal P_U}
 c_{k,j}e\!\left(\frac{h(k^2-j)}{4N}\right).
\tag{154.D21}
$$

This definition is before the external coefficient $-i/(2N)$ in
(154.D10).  Since $k^2-j=Nn_{k,j}$,

$$
 e\!\left(\frac{(r+4m)(k^2-j)}{4N}\right)
 =e(rn_{k,j}/4)e(mn_{k,j})=e(rn_{k,j}/4).
\tag{154.D22}
$$

For odd $n$, $e(n/4)=i\chi _4(n)$ and
$e(3n/4)=-i\chi _4(n)$.  Equations (154.D20)--(154.D22) prove
(154.D1), with exactly $N$ copies of each row.  Substitution into the
normalized Fourier formula proves the first equality in (154.D2).

Now apply Cauchy with all constants retained:

$$
 \begin{aligned}
 |Q_U|^2
 &\le \frac1{4N^2}(2N)
 \sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}|T_h|^2\\
 &=\frac1{2N}
 \sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}|T_h|^2
 =|Q_U|^2.
 \end{aligned}
\tag{154.D23}
$$

Thus this Cauchy step is equality for the literal wave.

The same fact is visible in the pair kernel.  For every integer $d$,

$$
 \frac1{2N}\sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}
 e\!\left(\frac{hd}{4N}\right)
 =e\!\left(\frac d{4N}\right){\bf1}_{2N\mid d}.
\tag{154.D24}
$$

For two literal pairs, $d=N(n_1-n_2)$ and $n_1-n_2$ is even, so the
indicator in (154.D24) is always one and

$$
 e((n_1-n_2)/4)=\chi _4(n_1)\chi _4(n_2).
\tag{154.D25}
$$

Consequently every ordered pair survives, with precisely its original
character product.  The diagonal is not isolated.  The apparent
oscillation of $e(hk^2/(4N))$ in $k$ is cancelled, on the selected graph,
by the simultaneous factor $e(-hj/(4N))$; separating those two factors and
claiming a post-selection $h$-saving is therefore unlawful.

This does not collapse the ambient rows used to realize the selector.
Before divisibility is imposed, $t=k^2-j$ need not be a multiple of $N$,
so $e((r+4m)t/(4N))$ genuinely depends on $m$.  The post-selection identity
(154.D23) is therefore not cited as a no-go for a joint ambient
$h$-$k$-$j$ analysis.

### 3.4 Signed roots, dyadic defects, and direct root Cauchy

For $0<|j|<N$, put

$$
 \rho_N(j)=\#\{x\bmod N:x^2\equiv j\pmod N\}.
\tag{154.D26}
$$

The all-parity prime-power calculation gives

$$
 \rho_N(j)\le4\,2^{\omega(N)}\sqrt{(|j|,N)}.
\tag{154.D27}
$$

Indeed, at $p^a\Vert N$, if
$v=\min(v_p(j),a)$ is odd and $v<a$, there is no root.  If $v=2b<a$,
there are at most $2p^b$ roots for odd $p$ and at most $4p^b$ roots for
$p=2$; if $v=a$, the zero congruence has
$p^{\lfloor a/2\rfloor}$ roots.  The Chinese remainder theorem proves
(154.D27), including even and nonsquarefree $N$.

Because the supported $k$-span is shorter than $N$, each residue root
contributes at most one supported $k$.  Hence, for either sign and every
dyadic $J\ll\Delta\ll K<N$,

$$
 \begin{aligned}
 T_{\sigma,\Delta}
 &:=\#\{(k,j)\in\mathcal P_U:
          \Delta<\sigma j\le2\Delta\}\\
 &\ll_\varepsilon X^\varepsilon\min\{M,\Delta\}.
 \end{aligned}
\tag{154.D28}
$$

Here the exact positive endpoint $j\le k-1$ and negative endpoint
$j\ge-k$ are imposed by intersection, not replaced asymptotically.  The
$M$ bound in (154.D28) is support injectivity; the $\Delta$ bound follows
by summing (154.D27) and

$$
 \sum_{0<|j|\le H}\sqrt{(|j|,N)}
 \ll H\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon HX^\varepsilon.
\tag{154.D29}
$$

Thus the raw pair count and actual weighted absolute capacity are

$$
 T_{\sigma,\Delta}
 \ll_\varepsilon X^\varepsilon\min\{M,\Delta\},
 \qquad
 \mathcal C_{\sigma,\Delta}
 \ll_\varepsilon
 M^{-3/4}\min\{M,\Delta\}X^\varepsilon.
\tag{154.D30}
$$

The global raw count is $O(M)$ and the global weighted capacity is
$M^{1/4}X^\varepsilon$.  These are upper capacities, not values or signed
lower bounds.  A fixed first collar $J<|j|\le C_0J$, or more generally a
fixed polylogarithmic dilation of $J$, is target-safe by (154.D29); no
positive-power enlargement follows, since the capacity ledger becomes
$HM^{-3/4}$.  This $X^\varepsilon$-equivalent thickening is only
bookkeeping around the accepted small-defect cutoff and is not recommended
as a new terminal strict range.

There is also no coefficient-blind second-moment improvement.  If $r(j)$
is the number of supported roots for $j$, then

$$
 \sum_{\Delta<|j|\le2\Delta}r(j)^2
 \le\sum_{\Delta<|j|\le2\Delta}\rho_N(j)^2
 \ll_\varepsilon\Delta X^\varepsilon.
\tag{154.D31}
$$

To see the last bound, square (154.D27), use
$(j,N)=\sum_{d\mid(j,N)}\varphi(d)$, and sum the multiples of every
$d\mid N$; both the main terms and interval endpoints cost
$O(\Delta\tau(N))$.  Cauchy over the $O(\Delta)$ possible $j$ and then
inside each root fibre gives exactly

$$
 |Q_{U,\sigma,\Delta}|
 \ll_\varepsilon \Delta M^{-3/4}X^\varepsilon,
\tag{154.D32}
$$

the same scale as absolute root counting when $\Delta\le M$.  The
off-diagonal congruence is

$$
 N\mid(k_1-k_2)(k_1+k_2),
\tag{154.D33}
$$

and, because both quotients are odd, its literal pairs in fact satisfy
$2N\mid(k_1-k_2)(k_1+k_2)$.  These imprimitive factor-splitting fibres
cannot be deleted.  If $N$ is prime, (154.D14) makes
$0<k_1+k_2<N$, so (154.D33) forces $k_1=k_2$.  Thus for prime $N$ every
nonzero $j$ has at most one supported root.  Any uniform proof based on
cancellation among several roots of one fixed $j$ already fails on this
allowed modulus class.

The two defect signs cannot be paired formally: their quotients are
$(k^2-|j|)/N$ and $(k^2+|j|)/N$, their modulo-$4N$ classes and profile
samples differ, and their exact phases have opposite signs but unequal
denominators.  A cancellation between them would be a new signed theorem.

### 3.5 Every imprimitive and two-adic quadratic Gauss term

Set $C_N=4N$ and, for odd $h\bmod C_N$, let

$$
 g=(h,C_N)=(h,N),\qquad q=C_N/g,\qquad a=h/g.
\tag{154.D34}
$$

The number $g$ is an odd divisor of the odd part of $N$; the effective
modulus $q$ retains the complete two-adic factor
$2^{v_2(N)+2}$, and $(a,q)=1$.  There are exactly $\varphi(q)$ frequencies
in the $g$-stratum.

For the complete quadratic Gauss sum

$$
 \mathcal G_{C_N}(h,\beta)
 =\sum_{x\bmod C_N}
 e\!\left(\frac{hx^2+\beta x}{C_N}\right),
\tag{154.D35}
$$

period splitting first gives zero unless $g\mid\beta$, and gives
$g\mathcal G_q(a,\beta/g)$ otherwise.  Since $q\equiv0\pmod4$ and $a$ is
odd, pairing $x$ with $x+q/2$ makes this last Gauss sum zero when
$\beta/g$ is odd.  Therefore

$$
 \mathcal G_{C_N}(h,\beta)=0\qquad(2g\nmid\beta).
\tag{154.D36}
$$

If $\beta=2gu$, completing the square modulo $q$ gives the exact formula

$$
 \boxed{
 \mathcal G_{C_N}(h,2gu)
 =g\,e\!\left(-\frac{\bar a u^2}{q}\right)
 (1+i)\epsilon_a^{-1}
 \left(\frac q a\right)\sqrt q,}
\tag{154.D37}
$$

where $a\bar a\equiv1\pmod q$,
$\epsilon_a=1$ for $a\equiv1\pmod4$ and
$\epsilon_a=i$ for $a\equiv3\pmod4$, and $(q/a)$ is the odd-denominator
Jacobi/Kronecker symbol.  In particular

$$
 |\mathcal G_{C_N}(h,2gu)|=\sqrt{2C_Ng}.
\tag{154.D38}
$$

Equations (154.D34)--(154.D38) include primitive and imprimitive $h$, every
valuation of $2$ in $N$, the vanishing dual parity, and the complete phase.

For fixed $j$, the lawful ambient selector expansion evaluates the inherited
real profile at $x=(k^2-j)/N$ before the Fourier sum imposes integrality.
Let

$$
 a_j(k)={\bf1}_{k\ge1}{\bf1}_{-k\le j\le k-1}{\bf1}_{|j|>J}
 w_U\!\left(\frac{k^2-j}{N}\right)e(\phi(k,j)),
\tag{154.D39a}
$$

with the literal real zero extension, support components, transitions, and
half-open endpoints of $A_U$.  No arbitrary off-congruence amplitude is
inserted.  These ambient $h$-rows are not the repeated rows of Section 3.3.
The exact ambient expansion is

$$
 Q_U=-\frac{i}{2N}
 \sum_{\substack{h\bmod C_N\\h\ \mathrm{odd}}}\chi _4(h)
 \sum_j e(-hj/C_N)\sum_k a_j(k)e(hk^2/C_N).
\tag{154.D39b}
$$

All $k,j$ in (154.D39b) are off-congruence ambient variables; the selector
is recovered only after the complete $h$-sum.  On each literal support
component, monotonicity of $(k^2-j)/N$, (154.D6), and

$$
 \left|\frac{\partial}{\partial k}\phi(k,j)\right|
 =\left|\frac{k}{\sqrt{k^2-j}}-1\right|
 \ll\frac{|j|}{K^2}
\tag{154.D39}
$$

give, including all jumps at zero-extension and cell endpoints,

$$
 \|a_j\|_\infty+\operatorname {Var}(a_j)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{154.D40}
$$

Zero extension to a complete residue interval and Fourier inversion give

$$
 \sum_k a_j(k)e(hk^2/C_N)
 =\frac1{C_N}\sum_{\beta\bmod C_N}
 \widehat a_j(\beta)\mathcal G_{C_N}(h,\beta).
\tag{154.D41}
$$

Equivalently, splitting an interval of length $L\ll K$ into complete
periods of length $q=C_N/g$, applying (154.D37) to the complete periods,
and using Abel summation on the terminal incomplete period proves

$$
 \left|\sum_k a_j(k)e(hk^2/C_N)\right|
 \ll_\varepsilon M^{-3/4}X^\varepsilon
 \left\{K\sqrt{\frac g{C_N}}+\sqrt{\frac{C_N}g}\log(2C_N)\right\}.
\tag{154.D42}
$$

The first term is the complete-period contribution and the second is the
incomplete completion remainder.  Neither is omitted.

There are $\varphi(C_N/g)$ odd $h$ in the $g$-stratum.  Using
$\varphi(C_N/g)\le C_N/g$ and summing all odd divisors $g$ gives

$$
 \begin{aligned}
 \frac1{2N}\sum_{\substack{h\bmod C_N\\h\ \mathrm{odd}}}
 K\sqrt{\frac{(h,C_N)}{C_N}}
 &\ll_\varepsilon \sqrt M X^\varepsilon,\\
 \frac1{2N}\sum_{\substack{h\bmod C_N\\h\ \mathrm{odd}}}
 \sqrt{\frac{C_N}{(h,C_N)}}
 &\ll_\varepsilon \sqrt N X^\varepsilon.
 \end{aligned}
\tag{154.D43}
$$

Restoring the $O(\Delta)$ positive or negative $j$ values, the factor
$e(-hj/C_N)$, every $h$-row, and the normalization $1/(2N)$ proves
(154.D3).  Thus a square-root estimate for one complete Gauss sum is not a
complete wave estimate.  The primitive incomplete remainder, all outer
$j$'s, and the coherent $h$ multiplicity are decisive.  This conclusion
prices the ambient rows by absolute values after the individual
completion; it is not an impossibility theorem for cancellation in the
joint completed $h$-$k$-$j$ transform.

Completing the $j$-interval first does not help.  The discrete Fourier
$L^1$ bound for a bounded-variation interval is
$O(C_N\log C_N)$ before the $1/(2N)$ normalization.  Absolute summation
over the $O(K)$ ambient $k$ values therefore gives only

$$
 |Q_U|\ll_\varepsilon
 K M^{-3/4}X^\varepsilon
 =\sqrt N\,M^{-1/4}X^\varepsilon.
\tag{154.D44}
$$

If instead one keeps the $h$-sum coherent, (154.D10) reconstructs the two
signed root congruences (154.D17), and the remaining coefficient-blind
bound is (154.D32).  Thus the two legal orders are respectively too costly
or an exact self-return.

### 3.6 The lawful ambient saddle is the accepted reciprocal self-return

The strict large-defect mask must not be erased inside the ambient
Fourier sum.  Instead restore the already owned exact and small-defect
scalars before any completion.  If $P_U$ is the full literal square-root
wave, Round 152 gives

$$
 Q_U=P_U+O_\varepsilon(X^\varepsilon).
\tag{154.D44a}
$$

This uses only the $j=0$ and $0<|j|\le J$ scalar owners; the direct
large-defect wave still contains every large-square-factor term.

The cells themselves give an exact endpoint partition.  For fixed $k$,
$-k\le j\le k-1$ is equivalent to

$$
 k^2-k+1\le t=k^2-j\le k^2+k,
\tag{154.D44b}
$$

and the next cell starts at $k^2+k+1$.  Hence the full cells partition all
positive integers $t$ once.  Expanding $G_N(t)$ on this full partition is
therefore a lawful off-congruence Fourier expansion of $P_U$.  Since
$e(-k)=1$, gluing the cells gives the exact global form

$$
 P_U=-\frac{i}{2N}
 \sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}\chi _4(h)
 \sum_{t\ge1}w_U(t/N)e\!\left(\sqrt t+\frac{ht}{4N}\right).
\tag{154.D44b1}
$$

Center the negative odd frequency by writing
$h=C_N-a=4N-a$, with $a$ positive and odd.  Since
$\chi _4(4N-a)=-\chi _4(a)$ and $t$ is integral, its exact phase for fixed
$k$ is

$$
 \Psi_{a,k}(j)
 =-\frac{a(k^2-j)}{4N}+\sqrt{k^2-j}-k.
\tag{154.D44c}
$$

Writing $s=\sqrt{k^2-j}$, direct differentiation gives

$$
 \Psi'_{a,k}(j)=\frac{a}{4N}-\frac1{2s},
 \qquad
 \Psi''_{a,k}(j)=-\frac1{4s^3}.
\tag{154.D44d}
$$

Thus a saddle exists on profile support exactly when

$$
 s_*=\frac{2N}{a},\qquad
 n_*=\frac{s_*^2}{N}=\frac{4N}{a^2}\asymp M,
 \qquad a\asymp2\sqrt{\frac NM}.
\tag{154.D44e}
$$

There is no half-integer tie for $s_*=2N/a$: such a tie would make
$4N=a(2m+1)$, impossible because $a$ is odd.  Thus nearby discrete terms
retain their unique literal cell label.  The continuous saddle can meet a
half-cell endpoint buffer, so no claim is made that the real number
$j_*=k^2-s_*^2$ is an integer in the discrete cell.  Gluing first by
(154.D44b1) removes that artificial interface; the accepted transition
ledger owns the endpoint buffer.  At the saddle,

$$
 \Psi_{a,k}(j_*)=\frac Na-k,\qquad e(\Psi_{a,k}(j_*))=e(N/a).
\tag{154.D44f}
$$

The sign and stationary symbol are also exact.  The Fourier coefficient is

$$
 -\frac{i}{2N}\chi _4(4N-a)
 =\frac{i}{2N}\chi _4(a).
\tag{154.D44g}
$$

Because $\Psi''<0$, stationary phase contributes
$e(-1/8)|\Psi''(j_*)|^{-1/2}
=e(-1/8)2s_*^{3/2}$.  Multiplication by

$$
 w_U(n_*)=N^{3/4}s_*^{-3/2}A_U(4N/a^2)
\tag{154.D44h}
$$

and (154.D44g) gives

$$
 e(1/8)N^{-1/4}\chi _4(a)A_U(4N/a^2)e(N/a).
\tag{154.D44i}
$$

Positive centered frequencies have no saddle; negative frequencies outside
(154.D44e), the terminal pieces, support transitions, and hard endpoints
are precisely the nonstationary and boundary terms in the accepted
Round-152 character-Poisson ledger.  Restoring that already proved ledger
gives

$$
 \boxed{
 Q_U=e(1/8)N^{-1/4}
 \sum_{\substack{a>0\\a\ \mathrm{odd}}}
 \chi _4(a)A_U(4N/a^2)e(N/a)
 +O_\varepsilon(X^\varepsilon).}
\tag{154.D44j}
$$

This is the accepted Round-151 reciprocal row, including its actual
profile, zero extension, transitions, endpoints, and external
$B_{1,U}(1)$ seam.  It is a principal stationary self-return, not a new
bound.  Applying the principal transform again returns the square-root
wave.  The outer stationary range has length
$a\asymp2\sqrt{N/M}$, so its absolute principal capacity is

$$
 N^{-1/4}\sqrt{\frac NM}X^\varepsilon
 =R M^{-1/2}X^\varepsilon.
\tag{154.D44k}
$$

This is an upper capacity, not a signed lower bound, and is the accepted
reciprocal capacity rather than a new gain.  A claim about the strict mask
directly inside a correlation, rather than the lawful scalar restoration
(154.D44a), would require a separate masked stationary theorem and is not
made here.

### 3.7 Exact phase, collisions, near collisions, and endpoint error

No phase truncation is needed for the no-go above.  There is, however, a
lawful scalar-level linearization, which shows that the first obstruction is
not an unpriced Taylor endpoint.  From (154.D8), with
$s=\sqrt{k^2-j}$,

$$
 \phi(k,j)=-\frac{j}{2k}
 -\frac{j^2}{2k(k+s)^2}.
\tag{154.D45}
$$

Throughout the exact cell, $|j|\le k$ and $k+s\gg k$, so the second term is
$O(1/k)$.  Applying this replacement only to the already selected scalar,
before any positivity step, costs

$$
 \sum_{(k,j)\in\mathcal P_U}|w_U(n_{k,j})|O(K^{-1})
 \ll_\varepsilon \frac{M^{1/4}}KX^\varepsilon
 =N^{-1/2}M^{-1/4}X^\varepsilon.
\tag{154.D46}
$$

It would not be lawful to price the error over the $NM$ ambient points
created by Fourier expansion; (154.D46) uses the exact selected graph.

The exact phase has no nontrivial exact collision in the large-defect
sector.  Indeed $\phi(k,j)\in(-1/2,1/2)$.  If two literal phases agree
modulo one, then for some integer $m$,

$$
 \sqrt{Nn_1}-\sqrt{Nn_2}=m.
\tag{154.D47}
$$

For distinct positive integers $A,B$, an integral value of
$\sqrt A-\sqrt B$ forces both $A$ and $B$ to be squares: after isolating
$\sqrt B$, its rationality follows.  Hence (154.D47) outside the equality
diagonal lies only on the exact-square rays $j_1=j_2=0$, already owned by
Round 152.

This does not control near collisions sharply.  If neither pair is an
exact square and $m$ is any relevant integer, the algebraic norm identity

$$
 \begin{aligned}
 &\bigl(\sqrt A-\sqrt B-m\bigr)
  \bigl(\sqrt A-\sqrt B+m\bigr)\\
 &\quad\times
  \bigl(\sqrt A+\sqrt B-m\bigr)
  \bigl(\sqrt A+\sqrt B+m\bigr)
  =(A+B-m^2)^2-4AB
 \end{aligned}
\tag{154.D48}
$$

is a nonzero integer.  Since the other three factors are $O(K)$ on the
literal support, it gives only

$$
 \|\phi(k_1,j_1)-\phi(k_2,j_2)\|_{\mathbb R/\mathbb Z}
 \gg K^{-3}.
\tag{154.D49}
$$

This extremely fine spacing does not price the near-collision population
needed by dispersion.  Exact collisions, near collisions, and the positive
Cauchy diagonal are therefore distinct: the first is absent off the owned
square ray, the second remains open, and the third may never be called a
signed lower bound for $Q_U$.

The complete scale and endpoint ledger is:

| Object | Exact size or multiplicity | Restored consequence |
|---|---:|---|
| $N$ | $N\asymp R^4$ | no parity or squarefreeness assumption |
| $J$ | $M^{3/4}$ | strict mask $|j|>J$ retained |
| $k$ | $k\asymp K=R^2M^{1/2}$ | ambient span $O(K)<N$, actual occupancy $O(M)$ |
| cell | $-k\le j\le k-1$ | exactly $2k$ integers; both endpoints retained |
| defect block | $\Delta<\pm j\le2\Delta$, $J\ll\Delta\ll K$ | $O(\log X)$ blocks, signs separate |
| actual pairs in a block | $O_\varepsilon(\min(M,\Delta)X^\varepsilon)$ | weighted capacity (154.D30), not signed mass |
| odd $h\bmod4N$ | $2N$ rows | $N$ repeats of each mod-four row on $t=Nn$ |
| ambient odd $h$ | distinct on off-congruence $t$ | exact expansion (154.D39b); no post-selection rank claim |
| gcd stratum | odd $g\mid N$, count $\varphi(4N/g)$ | no even gcd stratum; full $2^{v_2(N)+2}$ stays in $q$ |
| complete Gauss | zero unless $2g\mid\beta$; otherwise (154.D37) | magnitude $\sqrt{8Ng}$ before outer sums |
| incomplete $k$ interval | length $O(K)$ | complete periods plus $\sqrt{N/g}$ remainder in (154.D42) |
| centered negative frequency | $h=4N-a$, $a\asymp2\sqrt{N/M}$ | saddle $n_*=4N/a^2$ and phase $e(N/a)$ |
| principal stationary symbol | $e(1/8)N^{-1/4}\chi _4(a)A_U(4N/a^2)$ | accepted reciprocal-row self-return (154.D44j), capacity $RM^{-1/2}$ |
| $h$-Cauchy on selected graph | exact identity (154.D23) | all odd-quotient pairs survive |
| fixed-$j$ Cauchy | collision (154.D33), energy (154.D31) | returns $\Delta M^{-3/4}$ capacity |
| exact phase collision | equality only, off owned $j=0$ ray | near collisions still require a theorem |
| profile/endpoints | (154.D6), zero extension and inherited half-open cuts | all completion bounds use full BV norm; no endpoint is discarded |
| $B_{1,U}(1)$ | external, $O_\varepsilon(X^\varepsilon)$ | multiplication changes no displayed power after epsilon renaming |

## 4. First doubtful or unproved step

The first unproved step is not the coordinate, parity, Gauss evaluation, or
Taylor error.  It is a genuinely joint signed estimate across the outer
defect variable after the exact quotient selector has been restored.  One
possible exact formulation is

$$
 \sum_{\sigma\in\{+,-\}}
 \sum_{\substack{\Delta\ \mathrm{dyadic}\\J\ll\Delta\ll K}}
 \sum_{\substack{\Delta<\sigma j\le2\Delta\\
                   -k\le j\le k-1\\
                   k^2-j\equiv N\ \mathrm{or}\ 3N\pmod{4N}}}
 \operatorname {sgn}_{4N}(k^2-j)
 w_U\!\left(\frac{k^2-j}{N}\right)e(\phi(k,j))
 \ll_\varepsilon X^\varepsilon,
\tag{154.D50}
$$

where $\operatorname {sgn}_{4N}$ is $+1$ on the residue $N$ and $-1$ on
$3N$, and every support and endpoint test is literal.  The displayed
dyadic sum is schematic only in its harmless choice of half-open dyadic
boundaries; the cell and actual profile are exact.

Neither the post-selection identity (154.D23), the termwise ambient Gauss
bounds, nor (154.D31) proves (154.D50).  A successful future argument may
exploit the genuinely distinct off-congruence $h$-rows jointly with $k$ and
$j$, or cancellation between different selected $j$'s and gcd strata,
while retaining the quotient character.  It must also prove a
near-collision count stronger than the bare algebraic spacing (154.D49), or
avoid Cauchy altogether.  Nothing here excludes such a theorem.  The
complete principal saddle, however, is already exhausted by the exact
self-return (154.D44j).

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `literal_direct_large_defect_wave` | GREEN. Equation (154.D9) is the direct returned wave, not an artificial Mobius block. |
| `owned_range_and_mask_order` | GREEN. The open side is below $M^{449}\asymp R^{780}$; exact and small defects are removed at scalar level only.  The strict $|j|>J$ mask remains in every masked expression, and is restored to the full scalar only in the lawful identity (154.D44a) before stationary completion. |
| `exact_root_defect_bijection` | GREEN. Equations (154.D11)--(154.D15) prove no tie, bijection, positivity, injectivity, and multiplicity one. |
| `nearest_cell_endpoints_and_converse` | GREEN. Both $j=-k$ and $j=k-1$ are checked exactly in (154.D12)--(154.D13). |
| `support_injectivity_and_unique_residue` | GREEN. Fixed-dilate constants and sufficiently large $X$ give $2k<N$ and a total $k$-span below $N$. |
| `mod4N_quotient_character_completion` | GREEN/scoped no gain. Equations (154.D10), (154.D18)--(154.D25) verify the normalization and prove only the post-selection rank collapse; (154.D39b) separately retains the distinct off-congruence ambient rows. |
| `all_parity_two_adic_imprimitive_Gauss` | GREEN. Equations (154.D16)--(154.D17) and (154.D34)--(154.D38) retain quotient parity, the full two-adic modulus, every odd gcd stratum, dual parity, and the exact Gauss phase. |
| `positive_negative_and_dyadic_defects` | GREEN. Both signs and all $J\ll\Delta\ll K$ are present in (154.D28)--(154.D32); there is no formal sign pairing. |
| `K_J_N_h_power_ledger` | GREEN/no target. The final table, (154.D3), (154.D42)--(154.D44), and the exact saddle ledger (154.D44c)--(154.D44j) restore every outer power and multiplicity. |
| `actual_profile_endpoints_and_B11` | GREEN. The literal BV profile, real zero extension, components, jumps, and half-open endpoints enter (154.D6), (154.D39a)--(154.D40), and the accepted boundary restoration in (154.D44j); $B_{1,U}(1)$ stays external. |
| `Cauchy_diagonal_and_collision_survival` | GREEN/no gain. Selected-$h$ Cauchy is equality; fixed-$j$ collisions obey (154.D33); exact and near phase collisions are separated in (154.D47)--(154.D49). |
| `completion_remainder_and_outer_sums` | GREEN/no target. The complete-period and incomplete-remainder terms are both in (154.D42), followed by all $g,h,j$ sums in (154.D43)--(154.D44).  The coherent principal stationary order is independently checked in (154.D44a)--(154.D44j) and self-returns to the reciprocal row. |
| `absolute_capacity_vs_signed_sum` | GREEN. Equations (154.D30)--(154.D32) are used only as upper capacities.  No diagonal or completion term is asserted as a lower bound for the signed scalar. |
| `D_L_generic_tge2_cross_and_downstream_scope` | GREEN. Nothing is inferred for $D>1$, $L>1$, the growing-$M$ generic $t=1$ sector, any original $t\ge2$ layer, the Round-138 cross owner, M2, endpoint assembly, M9, the bridge, or either global exponent. |

No numerical experiment was performed.  The controls are exact algebraic
or analytic derivations.

## 6. Dependencies and exact artifacts used

This report used only the selected context in the task brief:

1. `protocol.md`;
2. `state/proof_obligations.yml`, in particular the five target nodes named
   by the active campaign and graph
   `6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`;
3. `state/active_campaign.yml`;
4. `strategy/round154_d1_large_defect_root_dispersion_strategy.md`;
5. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/barrier_packet.md`;
6. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_exact_root_defect_reparametrization.md`;
7. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/reviews/conductor_round153_adjudication.md`;
8. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/controls/conductor_round153_controls.md`; and
9. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/candidates/conductor_round152_square_root_wave_reduction.md`.

No external theorem is imported.  The quadratic Gauss evaluation is derived
by period splitting, parity pairing, completion of the square, and the
standard elementary evaluation for a modulus divisible by four; all of its
hypotheses and factors are displayed in (154.D34)--(154.D38).
The global boundary-complete conclusion in (154.D44j) invokes only the
accepted Round-152 character-Poisson formula from artifact 9; its centered
frequency, derivative, saddle, sign, phase, and stationary symbol are
rederived explicitly in (154.D44c)--(154.D44i).

## 7. Recommended state effect

Recommend `revise` the conductor seed into an accepted exact reduction only
after independent review of the cell, modulo-$4N$ normalization, and Gauss
formula.  Recommend recording a new route-scoped obstruction with terminal
label `large_defect_root_dispersion_no_go`:

- after the divisibility selector is imposed, the odd $4N$ Fourier family
  is $N$ repeated copies of two modulo-four rows and rank one on the literal
  odd-quotient graph;
- normalized post-selection $h$-Cauchy is exactly equality and preserves
  every pair with the original character product;
- the distinct ambient off-congruence rows remain eligible for a joint
  analysis, but their termwise incomplete quadratic completion, with all
  gcd, two-adic, remainder, profile, endpoint, $h$, and $j$ costs restored,
  gives (154.D3) and no scale range;
- the full-cell ambient principal saddle, after lawful scalar restoration
  of the owned masks, has the exact sign, symbol, phase, and endpoints of
  the already accepted reciprocal row (154.D44j), so it self-returns; and
- coefficient-blind fixed-$j$ root dispersion returns the absolute root
  capacity and has no inner root sum when $N$ is prime.

Retain the target estimate (154.D50) as open.  Do not interpret this
route-specific no-go as an impossibility theorem for a joint signed ambient
$h$-$k$-$j$ completion or a selected $k$-$j$ method, and make no downstream
theorem, owner, endpoint, or exponent change from this report alone.
