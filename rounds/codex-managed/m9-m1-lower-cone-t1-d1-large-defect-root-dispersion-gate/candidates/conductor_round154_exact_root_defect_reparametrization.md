# Round 154 conductor seed: exact root-defect reparametrization

- Campaign: `m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate`
- Role: conductor-frozen exact algebraic seed
- Starting graph: `6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`
- Status: candidate pending independent review

## 1. Result

The returned direct large-defect wave has an exact sparse quadratic-root
representation. Put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J=M^{3/4},
\tag{154.C1}
$$

and let

$$
 Q_U=\sum_{\substack{n>0\\n\ \mathrm{odd}}}
 {\bf1}_{|k(n)^2-Nn|>J}
 \chi_4(n)n^{-3/4}A_U(n)e(\sqrt{Nn}),
\qquad
 k(n)=\left\lfloor\sqrt{Nn}+\frac12\right\rfloor.
\tag{154.C2}
$$

For $k\ge1$ and $j\in\mathbb Z$, set

$$
 n_{k,j}=\frac{k^2-j}{N}
\tag{154.C3}
$$

when $N\mid k^2-j$. Then

$$
\boxed{
\begin{aligned}
 Q_U={}&\sum_{k\ge1}
 \sum_{\substack{-k\le j\le k-1\\|j|>J\\
 N\mid k^2-j\\n_{k,j}\ \mathrm{odd}}}
 \chi_4(n_{k,j})n_{k,j}^{-3/4}A_U(n_{k,j})\\
 &\hspace{37mm}\times
 e\left(-\frac{j}{k+\sqrt{k^2-j}}\right).
\end{aligned}}
\tag{154.C4}
$$

On literal support, $k\asymp\sqrt{NM}$, its total ambient interval has
length $O(\sqrt{NM})<N$, and $2k<N$ for sufficiently large $X$. Hence a
fixed $k$ has at most one admissible $j$ in its nearest cell. Distinct
supported $n$ have distinct $k$. Formula (154.C4) is a bijective
reparametrization, not an estimate.

## 2. Exact cell and converse

There is no half-integer tie. Indeed, a tie would make $4Nn$ an odd square,
which is impossible modulo four. Thus

$$
 k-\frac12<\sqrt{Nn}<k+\frac12.
\tag{154.C5}
$$

Squaring and using integrality of $j=k^2-Nn$ gives

$$
 -k\le j\le k-1.
\tag{154.C6}
$$

Conversely, if (154.C6) holds, $N\mid k^2-j$, and $n_{k,j}$ is a positive
integer, then

$$
 (k-\tfrac12)^2<k^2-j<(k+\tfrac12)^2,
\tag{154.C7}
$$

so $k$ is the unique nearest integer to $\sqrt{Nn_{k,j}}$. The cell itself
makes $n_{k,j}>0$ for $k\ge1$.

## 3. Support, injectivity, and multiplicity

The zero-extended profile confines $n$ to a fixed dilation of $M$. Hence
$k\asymp\sqrt{NM}$ and the union of its inherited components lies in an
ambient interval of length $O(\sqrt{NM})$. Since $M\le R^2$ and
$N\asymp R^4$,

$$
 \frac{k}{N}\ll\sqrt{\frac MN}\ll R^{-1},
\tag{154.C8}
$$

so $2k<N$ for large $X$. The interval in (154.C6) contains $2k<N$
integers, hence at most one representative of $k^2\pmod N$.

If $n_2>n_1$ are in the fixed support dilation, then

$$
 \sqrt{Nn_2}-\sqrt{Nn_1}
 =\frac{N(n_2-n_1)}{\sqrt{Nn_2}+\sqrt{Nn_1}}
 \gg\sqrt{\frac NM}\gg1.
\tag{154.C9}
$$

For large $X$, their nearest integers are distinct. Thus neither the
reparametrization nor the root coordinate creates a hidden multiplicity.
It also creates no automatic cancellation: the number of retained pairs is
still at most $O(MX^\varepsilon)$ and the actual absolute capacity remains
$M^{1/4}X^\varepsilon$.

## 4. Exact phase and character completion

Because $e(k)=1$,

$$
 e(\sqrt{k^2-j})
 =e\left(\sqrt{k^2-j}-k\right)
 =e\left(-\frac{j}{k+\sqrt{k^2-j}}\right).
\tag{154.C10}
$$

This identity is exact throughout the full cell; no Taylor expansion is
used when $|j|\asymp k$.

Define for every integer $t$

$$
 G_N(t)={\bf1}_{N\mid t}\chi_4(t/N),
\tag{154.C11}
$$

where $\chi_4$ vanishes on even integers. Then

$$
 \boxed{G_N(t)=-\frac{i}{2N}
 \sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}
 \chi_4(h)e\left(\frac{ht}{4N}\right).}
\tag{154.C12}
$$

To prove it, write $h=r+4m$ with $r\in\{1,3\}$ and
$0\le m<N$. The $m$-sum is zero unless $N\mid t$. For $t=Nq$, the remaining
sum is

$$
 N\left(e(q/4)-e(3q/4)\right)=2iN\chi_4(q),
\tag{154.C13}
$$

including zero when $q$ is even. This proves (154.C12) for every parity and
factorization of $N$.

Substituting $t=k^2-j$ exposes the quadratic phase
$e(hk^2/(4N))$ and the linear defect phase $e(-hj/(4N))$. The literal
profile at $(k^2-j)/N$, the nearest cell, and (154.C10) remain coupled and
must be retained in any completion.

## 5. First open analytic step

The exact seed reduces the Round-154 target to proving that the signed sparse
quadratic-root sum (154.C4) is $O_\varepsilon(X^\varepsilon)$ below
$M^{449}\asymp R^{780}$. A lawful proof may use (154.C12), direct root
dispersion in $j$, incomplete quadratic Gauss sums in $k$, or another
coefficient-sensitive mechanism. It must price:

- the complete odd $h\bmod4N$ family and every $(h,4N)$ factor;
- the fact that the $k$-interval is incomplete and shorter than $N$;
- both signs and all dyadic sizes of $j$, including $J<|j|\asymp k$;
- the actual quotient profile, cell, endpoints, and reciprocal-defect phase;
- every Cauchy diagonal, exact collision, near collision, and completion
  remainder; and
- the external $B_{1,U}(1)$ coefficient.

Neither injectivity nor a square-root bound for one complete Gauss sum is by
itself an estimate after the outer variables are restored.

## 6. Required controls

The seed has been checked algebraically for no ties, both cell endpoints,
the converse, positivity, odd quotient, all parities of $N$, support length,
injectivity, uniqueness of the cell residue, exact phase, and the sign and
normalization in the modulo-$4N$ Fourier identity. It uses no numerical
experiment and no external theorem.

Independent work must rederive these seams and either prove a target or
strict range, or isolate the first exact completion, Gauss, root-spacing,
profile, endpoint, diagonal, source, or power obstruction. The known
$|j|\le J$ owner may be removed before Cauchy at scalar level, not inside a
correlation.

## 7. Recommended state effect

No graph mutation is recommended from this seed alone. If independently
verified, (154.C4) and (154.C12) may become an exact reduction. A promoted
analytic conclusion requires a complete estimate or a rigorously scoped
no-go with every outer cost restored. No downstream theorem or exponent
changes at campaign launch.
