# Round 154 conductor candidate: logarithmic defect collar and scoped root-completion obstruction

- Campaign: `m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate`
- Round: 154
- Role: conductor-selected proof kernel pending terminal review
- Starting graph SHA-256: `6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`
- Proposed terminal label: `strict_large_defect_root_range`
- Allocation used: 100% analytic, algebraic, and primary-source work; 0% numerical

## 1. Result and exact scope

Put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J=M^{3/4},\qquad K=\sqrt{NM},\qquad 1\ll M\le R^2,
\tag{154.CA1}
$$

and retain the literal zero-extended Round-148 profile

$$
 w_U(n)=n^{-3/4}A_U(n),\qquad
 \|w_U\|_\infty+\operatorname {Var}w_U
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{154.CA2}
$$

The external factor $B_{1,U}(1)$ is not inserted and remains
$O_\varepsilon(X^\varepsilon)$.  The direct large-defect scalar is

$$
 Q_U=\sum_{\substack{n>0,\ n\ \mathrm{odd}\\
 |k(n)^2-Nn|>J}}
 \chi _4(n)w_U(n)e(\sqrt{Nn}),\qquad
 k(n)=\left\lfloor\sqrt{Nn}+\frac12\right\rfloor.
\tag{154.CA3}
$$

Round 154 proves three positive reductions and one route-scoped no-go.

First, with $j=k^2-Nn$, the literal sum has the exact bijective form

$$
 \boxed{
 Q_U=\sum_{\substack{k\ge1,\ -k\le j\le k-1,\ |j|>J\\
 N\mid k^2-j,\ (k^2-j)/N\ \mathrm{odd}}}
 \chi _4\!\left(\frac{k^2-j}{N}\right)
 w_U\!\left(\frac{k^2-j}{N}\right)
 e\!\left(-\frac{j}{k+\sqrt{k^2-j}}\right).}
\tag{154.CA4}
$$

There is no tie, both cell endpoints are literal, the converse holds, and
the inherited support has $k\asymp K$, total $k$-span $O(K)<N$, $2k<N$,
and multiplicity one for sufficiently large $X$.

Second, the residual phase may be linearized uniformly on the **selected
scalar**, not on the off-congruence ambient array:

$$
 -\frac{j}{k+\sqrt{k^2-j}}
 =-\frac{j}{2k}
 -\frac{j^2}{2k(k+\sqrt{k^2-j})^2}.
\tag{154.CA5}
$$

Since $|j|\le k$ in the exact cell, replacing the phase in (154.CA4) by
$e(-j/(2k))$ has total error

$$
 O_\varepsilon\!\left(K^{-1}M^{1/4}X^\varepsilon\right)
 =O_\varepsilon\!\left(N^{-1/2}M^{-1/4}X^\varepsilon\right).
\tag{154.CA6}
$$

Thus, up to a target-safe error, the first open wave is the signed modular
parabola incidence wave with phase $e(-j/(2k))$.  This is an exact
all-scale reduction; it is not yet an estimate for the survivor.

Third, for every fixed $A>0$, put

$$
 L_A(X)=(\log(2X))^A.
\tag{154.CA7}
$$

The complete collar

$$
 J<|j|\le J L_A(X)
\tag{154.CA8}
$$

has contribution $O_{\varepsilon,A}(X^\varepsilon)$, uniformly for every
parity and factorization of $N$, both signs, and all literal support
endpoints.  Consequently

$$
 \boxed{Q_U=Q_{U,A}+O_{\varepsilon,A}(X^\varepsilon),}
\tag{154.CA9}
$$

where $Q_{U,A}$ is (154.CA4) with $|j|>J L_A(X)$.  This is a strict
owner-complete logarithmic enlargement of the Round-152 small-defect owner.
It is not a positive-power defect enlargement and changes no scale or global
exponent.

Finally, the obvious completion architectures do not prove the remaining
wave.  Post-selection Fourier-frequency Cauchy is exactly equality.  The
lawful ambient rows are distinct, but exact finite completion converts them
to theta Kloosterman sums and gives only

$$
 |Q_U(V)|\ll_\varepsilon
 \left(M^{-3/4}V+M^{-1/4}\right)X^\varepsilon
\tag{154.CA10}
$$

on a dyadic block $V<|j|\le2V$.  This independently certifies the first
collar but supplies no positive-power enlargement; at $V\asymp K$ its first
term is $N^{1/2}M^{-1/4}$.  The principal full-cell stationary completion
has phase $e(N/a)$ and exactly reconstructs the accepted reciprocal row.
These are no-go results for the displayed placements, not an impossibility
theorem for a future signed joint $j$-dispersion estimate.

## 2. Exact root cell, parity, and collar proof

A tie would give $4Nn=(2k+1)^2$, impossible modulo four.  Hence

$$
 k-\frac12<\sqrt{Nn}<k+\frac12,
\tag{154.CA11}
$$

and integrality gives exactly

$$
 k^2-k+1\le Nn\le k^2+k,
 \qquad -k\le j\le k-1.
\tag{154.CA12}
$$

Conversely, (154.CA12), $N\mid k^2-j$, and positivity recover the unique
nearest integer.  The cell itself gives positivity.  Quotient oddness and
its sign may be written without inverting $N$:

$$
 \begin{aligned}
 (k^2-j)/N\ \mathrm{odd}
 &\Longleftrightarrow k^2-j\equiv N\pmod {2N},\\
 \chi _4((k^2-j)/N)&=
 \begin{cases}
 1,&k^2-j\equiv N\pmod {4N},\\
 -1,&k^2-j\equiv3N\pmod {4N}.
 \end{cases}
 \end{aligned}
\tag{154.CA13}
$$

Let

$$
 \rho_N(j)=\#\{x\bmod N:x^2\equiv j\pmod N\}.
\tag{154.CA14}
$$

The all-prime-power count, including $p=2$, gives for $j\ne0$

$$
 \rho_N(j)\le4\,2^{\omega(N)}\sqrt{(|j|,N)}.
\tag{154.CA15}
$$

Since the supported $k$-span is shorter than $N$, each root class supplies
at most one supported $k$.  For $1\le H<N$,

$$
 \sum_{0<|j|\le H}\rho_N(j)
 \ll H\,2^{\omega(N)}\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon HX^\varepsilon.
\tag{154.CA16}
$$

Take $H=JL_A(X)$.  This is below $N$ throughout the frozen range.  Multiply
(154.CA16) by the actual supremum $M^{-3/4}X^\varepsilon$ in (154.CA2),
split the requested epsilon among the profile, divisor, and logarithmic
factors, and subtract the already owned $|j|\le J$ sector.  This proves
(154.CA8)--(154.CA9).  The same argument with $H=JM^\delta$ has the
unabsorbed factor $M^\delta$ for every fixed $\delta>0$, so this counting
mechanism proves no positive-power extension.

## 3. Selected rows, ambient rows, and exact completion

For every integer $t$, the exact quotient selector is

$$
 G_N(t)={\bf1}_{N\mid t}\chi _4(t/N)
 =-\frac{i}{2N}\sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}
 \chi _4(h)e\!\left(\frac{ht}{4N}\right).
\tag{154.CA17}
$$

There are two distinct uses of this identity.

On the already selected graph $t=Nn$ with $n$ odd, remove only the quotient
character from the coefficient and let $T_h$ be the resulting unnormalized
row.  Writing $h=r+4m$, $r\in\{1,3\}$, gives

$$
 T_{1+4m}=iQ_U,\qquad T_{3+4m}=-iQ_U,
\tag{154.CA18}
$$

and hence

$$
 \frac1{2N}\sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}|T_h|^2
 =|Q_U|^2.
\tag{154.CA19}
$$

Normalized Cauchy in these post-selection rows is equality and every pair
survives.  This statement is **not** applied to the lawful ambient expansion.

Before the $h$-sum imposes divisibility, set $q=4N$, fix $j$, and extend the
inherited real profile off congruence.  Finite Fourier inversion in $k$ gives

$$
 \sum_kB_j(k)e_q(hk^2)
 =\frac1q\sum_{b\bmod q}\widehat B_j(b)
 \mathcal G(h,b;q).
\tag{154.CA20}
$$

For $d=(h,N)$, $h=da$, and $q'=q/d$, the complete Gauss sum vanishes unless
$b=2dv$ and otherwise equals

$$
 \mathcal G(h,2dv;q)
 =d(1+i)\epsilon_a^{-1}\left(\frac{q'}a\right)
 \sqrt{q'}e_{q'}(-\bar av^2).
\tag{154.CA21}
$$

After the $\chi _4(h)e_q(-hj)$ factor is restored, the complete $a$-sum is

$$
 (1+i)\chi _4(d)K(-v^2,-j;q'),
\tag{154.CA22}
$$

where $K$ is the theta-multiplier Kloosterman sum of
Duke--Friedlander--Iwaniec.  Their Lemma 6.1 applies because $q'\equiv0
\pmod4$ and gives

$$
 |K(m,n;c)|\le(m,n,c)^{1/2}c^{1/2}\tau(c).
\tag{154.CA23}
$$

Here (154.CA22) is only the primitive multiplier sum.  The full normalized
completed expression retains the Gauss prefactor $d\sqrt{q'}$:

$$
 -\frac{i(1+i)}{2Nq}
 \sum_j\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi _4(d)d\sqrt{q'}
 \sum_{v\bmod(q'/2)}
 \widehat B_j(2dv)K(-v^2,-j;q'),
 \qquad q'=q/d.
\tag{154.CA22a}
$$

The BV Fourier bound, all $d$-strata, all nonzero dual modes, the zero mode,
both signs, and every outer $j$ restore to (154.CA10).  In particular,
ambient $h$-cancellation is real; it simply does not overcome the full
defect length or the coupled $j$-dependent Fourier coefficient.

## 4. Principal ambient saddle and exact self-return

The full nearest cells partition the positive integers: for fixed $k$,

$$
 -k\le j\le k-1
 \Longleftrightarrow
 k^2-k+1\le t=k^2-j\le k^2+k,
\tag{154.CA24}
$$

and the next cell begins at $k^2+k+1$.  Restore the already target-safe
exact and small-defect scalars before completing; then

$$
 Q_U=P_U+O_\varepsilon(X^\varepsilon),
\tag{154.CA25}
$$

and the exact full-cell ambient identity is

$$
 P_U=-\frac{i}{2N}
 \sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}\chi _4(h)
 \sum_{t\ge1}w_U(t/N)e\!\left(\sqrt t+\frac{ht}{4N}\right).
\tag{154.CA26}
$$

Center a negative frequency as $h=4N-a$.  The cell phase is

$$
 \Psi_{a,k}(j)=-\frac{a(k^2-j)}{4N}+\sqrt{k^2-j}-k.
\tag{154.CA27}
$$

Its stationary point and phase are

$$
 \sqrt{k^2-j_*}=\frac{2N}{a},\qquad
 n_* =\frac{4N}{a^2},\qquad
 e(\Psi_{a,k}(j_*))=e(N/a).
\tag{154.CA28}
$$

The Fourier coefficient, negative-curvature eighth-root, Hessian size, and
weight give exactly

$$
 e(1/8)N^{-1/4}\chi _4(a)A_U(4N/a^2)e(N/a).
\tag{154.CA29}
$$

With the already accepted nonstationary, transition, endpoint, and hard-top
ledger, (154.CA25)--(154.CA29) reproduce the Round-151 reciprocal row.
The strict mask was restored only at scalar level before this principal
completion; it was not deleted inside a correlation.  A nonprincipal or
directly masked joint completion remains open.

## 5. First doubtful or unproved step

After the exact completion in Section 3, the first missing input is a signed
outer-defect theorem for

$$
 \sum_{V<|j|\le2V}\ \sum_{d\mid N}\ \sum_v
 \widehat B_j(2dv)K(-v^2,-j;4N/d),
 \qquad JL_A(X)\lesssim V\lesssim K,
\tag{154.CA30}
$$

with the literal profile, cell endpoints, both signs, strict mask, all gcd
strata, and stationary reciprocal subfamily retained.  The coefficient is
not separable in $j$ and $v$.  Existing modular-root, sparse-root, parabola,
square-modulus, and modulus-average theorems do not match all of these
hypotheses; termwise DFI gives (154.CA10) but no full-range target.

Equivalently, after (154.CA5)--(154.CA6), the first open selected theorem is
the signed cross-fibre estimate for the linearized phase $e(-j/(2k))$.
For odd $N$, the quotient character is constant along each fixed-$j$ root
fibre, so any cancellation using that character must survive the outer
$j$-ordering.  No capacity, diagonal, or large theorem right side below is
asserted to be a signed lower bound.

## 6. Required controls and source scope

The candidate retains:

1. the literal direct wave, actual profile, external $B_{1,U}(1)$ seam,
   strict scale side, and scalar mask order;
2. no ties, the asymmetric cell endpoints, converse, positivity,
   injectivity, unique residue, quotient parity, and all two-adic cases;
3. raw counts, weighted capacities, and signed sums as different objects;
4. the exact modulo-$4N$ sign and normalization, with post-selection and
   ambient rows explicitly separated;
5. every imprimitive Gauss gcd, even-dual condition, theta multiplier,
   Fourier zero mode, completion tail, defect sign, and outer block;
6. the DFI Lemma 6.1 source match and the first unmatched nonseparable
   $j$-dispersion interface;
7. the principal saddle only after lawful scalar restoration, with its
   reciprocal phase, symbol, endpoints, and accepted error owners; and
8. complete downstream separation from $D>1$, $L>1$, generic $t=1$,
   original $t\ge2$, the Round-138 cross owner, M2, endpoint assembly,
   M9, the bridge, the quarter target, and both global exponents.

The primary-source audit is current through 25 August 2026.  DFI Lemma 6.1
is a genuine match for (154.CA22), not for the remaining sum (154.CA30).
The absence of a matching theorem for (154.CA30) is method evidence, not a
literature-impossibility theorem.

## 7. Recommended state effect

Subject to three independent GREEN terminal reviews:

- promote (154.CA4), the target-safe linearization (154.CA5)--(154.CA6),
  and the strict logarithmic collar (154.CA8)--(154.CA9) as one exact
  root-defect reduction;
- record the selected-row equality (154.CA18)--(154.CA19), the exact
  ambient theta-Kloosterman conversion (154.CA20)--(154.CA23), its complete
  bound (154.CA10), and the principal reciprocal self-return
  (154.CA25)--(154.CA29) as a route-scoped obstruction;
- retain the full large-defect estimate below $M^{449}\asymp R^{780}$ as
  open, with (154.CA30) or the equivalent signed linearized outer-root wave
  as the first missing theorem;
- reject post-selection frequency large-sieve gain, independent $k$- and
  $j$-Gauss gains, primitive-only Gauss replacement, deletion of the small
  mask inside a correlation, absolute outer-$j$ summation advertised as
  character cancellation, and any claim that the principal saddle is a new
  transform gain; and
- make no positive-power scale, downstream theorem, endpoint, or global
  exponent change.
