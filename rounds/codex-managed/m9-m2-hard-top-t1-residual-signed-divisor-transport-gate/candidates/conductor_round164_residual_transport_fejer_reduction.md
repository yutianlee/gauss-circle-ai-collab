# Conductor candidate: exact residual BV duality and Fejer energy frontier

## 1. Result

Round 164 does not prove the complete residual target.  It proves an exact
residual algebra, a sharp bounded-variation dual formula, a
coefficient-uniform obstruction to closing by positive within-product
transport, and an exact cross-product Fejer reduction which retains the
only remaining oscillation.

The proposed terminal label is

\[
 \boxed{\texttt{hard\_top\_t1\_residual\_transport\_no\_go}.}
\tag{164.C1}
\]

The no-go is route-scoped: it rules out a conclusion based only on positive
monotone transport, unmatched-mass charging, bounded profile variation, and
the accepted positive product collar.  It is not a lower bound for the
literal residual and does not disprove its target.

## 2. Exact residual and sign-mass statement

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad q_X=X/y^2,
 \qquad H=\lfloor yX^{-1/4}\rfloor,
 \qquad 1\ll L\ll H\le J^{1/2}.
\tag{164.C2}
\]

For squarefree \(N\) in the inherited half-open \(N\asymp L^2\) shell,
write

\[
 N=2^{\nu_N}M_N,\qquad \nu_N\in\{0,1\},\qquad M_N\text{ odd}.
\tag{164.C3}
\]

If the Round-163 selector is absent, put \(\rho_N(d)=1\) for every
\(d\mid M_N\).  If it selects \(p_N,q_N\), put

\[
 \rho_N(d)
 =1-\mathbf 1_{p_N\mid d}-\mathbf 1_{q_N\mid d}
   +2\mathbf 1_{p_N\mid d}\mathbf 1_{q_N\mid d}.
\tag{164.C4}
\]

Thus \(\rho_N\) is one exactly on the \(00\) and \(11\) selected-prime
bit patterns.  The complementary Boolean function is the XOR indicator,
so the accepted Round-163 sector and (164.C4) partition every incidence
once and only once.

Let

\[
 \mathscr R_N=\{d\mid M_N:\rho_N(d)=1\}
\tag{164.C5}
\]

and let \(A_N(d)\) be the complete real literal amplitude, including
\(\eta_L\), \(\Phi\), \(W\), the cone and product shells, floors, stars,
half-open endpoint values, parity, and zero extension.  Put

\[
 b_N^{\rm rem}=\sum_{d\in\mathscr R_N}\chi_4(d)A_N(d),
 \qquad
 c_N^{\rm rem}=\mathbf 1_{N\in\mathcal I_L^{\rm lit}}
 \mu^2(N)\left(\frac{L^2}{N}\right)^{3/4}b_N^{\rm rem}.
\tag{164.C6}
\]

The residual owner is exactly

\[
 \mathcal S_{L,1}^{\rm rem}
 =\sum_N c_N^{\rm rem}e(J\sqrt N).
\tag{164.C7}
\]

Its full residual character mass is

\[
 \sum_{d\in\mathscr R_N}\chi_4(d)
 =\begin{cases}
 \displaystyle\prod_{r\mid M_N}(1+\chi_4(r)),
     &\text{no pair is selected},\\[6pt]
 \displaystyle(1+\chi_4(p_Nq_N))
       \prod_{\substack{r\mid M_N\\r\ne p_N,q_N}}
       (1+\chi_4(r))=0,
     &\text{a pair is selected},
 \end{cases}
\tag{164.C8}
\]

where the products are over odd prime divisors.  Hence a selected residual
is exactly balanced.  A no-pair residual is balanced if at least one odd
prime factor is \(3\pmod4\), and is wholly positive, with mass
\(2^{\omega(M_N)}\), if every odd prime factor is \(1\pmod4\).

For a selected pair, writing \(M_N=p_Nq_NR_N\) gives the exact pairing

\[
 \mathscr R_N=\{a:a\mid R_N\}\ \dot\cup\
              \{p_Nq_Na:a\mid R_N\},
\quad
 b_N^{\rm rem}=\sum_{a\mid R_N}\chi_4(a)
       \{A_N(a)-A_N(p_Nq_Na)\}.
\tag{164.C9}
\]

Since \(p_Nq_N\ge15\), the two physical supports in each brace are
disjoint.  The small displacement \(|\log(q_N/p_N)|\ll L^{-1/2}\)
belongs to the deleted XOR pairing \(p_Na\leftrightarrow q_Na\); it does
not transfer to (164.C9).

## 3. Exact Abel identity and sharp BV dual norm

Order the complete residual divisor universe, including zero-amplitude
divisors, as

\[
 d_1<\cdots<d_r,\qquad \sigma_i=\chi_4(d_i),\qquad
 C_j=\sum_{i\le j}\sigma_i,
\tag{164.C10}
\]

and put \(C_0=0\), \(a_i=A_N(d_i)\), \(a_0=a_{r+1}=0\).  Direct
summation by parts gives both exact forms

\[
 \boxed{
 b_N^{\rm rem}=C_ra_r+\sum_{j<r}C_j(a_j-a_{j+1})
 =-\sum_{j=0}^{r}C_j(a_{j+1}-a_j).}
\tag{164.C11}
\]

The largest residual odd divisor is \(M_N\).  It belongs to the no-pair
universe and, after selection, to the both-prime universe.  For \(N>16\),

\[
 M_N>2\sqrt N
\tag{164.C12}
\]

on both the odd and even branches, so \(a_r=0\).  Formula (164.C11),
however, remains valid without deleting the terminal term.

Let

\[
 V_N=\sum_{j=0}^{r}|a_{j+1}-a_j|,
 \qquad
 \operatorname{osc}C_N=max_{0\le j\le r}C_j-min_{0\le j\le r}C_j.
\tag{164.C13}
\]

Because \(\sum_{j=0}^{r}(a_{j+1}-a_j)=0\), subtracting the midpoint of
the range of \(C_j\) in (164.C11) proves the sharp coefficient-uniform
BV dual estimate

\[
 \boxed{
 |b_N^{\rm rem}|\le \frac12\operatorname{osc}C_N\,V_N.}
\tag{164.C14}
\]

This is the correct zero-extended unequal-mass formula.  It automatically
includes unmatched sign mass: no arbitrary cemetery position is needed.
Equivalently, if a cemetery is used to equalize masses, only the variation
and hard jumps crossed by its paths have coefficient meaning; raw distance
through a region where the amplitude is identically zero is not an
intrinsic cost.

For the regulated real extension \(a_N(u)=A_N(e^u)\), define

\[
 F_N(u)=\sum_{\substack{d\in\mathscr R_N\\\log d\le u}}\chi_4(d).
\tag{164.C15}
\]

Splitting each literal boundary \(\beta\) into incoming and outgoing
increments

\[
 \Delta^-_\beta a_N=a_N(\beta)-a_N(\beta^-),\qquad
 \Delta^+_\beta a_N=a_N(\beta^+)-a_N(\beta)
\tag{164.C16}
\]

gives the exact full-line regulated Stieltjes identity

\[
\begin{aligned}
 b_N^{\rm rem}={}&
 -\int_{\mathbb R}F_N(u)a'_{N,{\rm sm}}(u)\,du\\
 &-\sum_\beta\bigl(
 F_N(\beta^-)\Delta^-_\beta a_N
 +F_N(\beta)\Delta^+_\beta a_N\bigr).
\end{aligned}
\tag{164.C17}
\]

Here the compact zero extension is traversed over the whole real line, so
there is no additional terminal term.  The two cumulative values in
(164.C17) are forced when a divisor lies on a hard boundary; they retain
stars, point values, and half-open ties.
The accepted profile seminorms give

\[
 |a'_{N,{\rm sm}}(u)|\ll 1+L/H\ll1,
 \qquad V_N\ll1,
\tag{164.C18}
\]

with every hard face included in \(V_N\).  Applying (164.C14) to the
literal profile and then taking the triangle inequality would be
target-safe from the weighted estimate

\[
 \sum_{N\asymp L^2}\operatorname{osc}C_N\,V_N
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{164.C19}
\]

The unweighted sum \(\sum_N\operatorname{osc}C_N\) is only the sharp
envelope for a theorem uniform over every bounded-variation profile with
\(V_N\ll1\).  The exact algebra controls that envelope only at the
divisor-bound scale \(L^{2+o(1)}\); it does not assert that the fixed
literal variations saturate it.

## 4. Coefficient-uniform transport-capacity obstruction

The hostile audit constructs exact odd and even controls.  The strongest
selector-robust one uses four odd primes in fixed boxes of scale
\(P\asymp\sqrt L\), two in each nonzero residue class modulo four.  The
three physical near-square two-prime partitions have signs

\[
 \{+,-,-\}.
\tag{164.C20}
\]

With no selected pair their unit-profile residual sum is \(-1\).  If an
opposite-character pair is selected, two XOR partitions are deleted and
the unique neither/both partition left behind has sign \(-1\).  Thus the
unit-profile residual is \(-1\) for every selector status.  The even
variant puts the factor \(2\) on the complementary leg and has the same
property.

The audited fixed-modulus prime theorem of Bennett--Martin--O'Bryant--
Rechnitzer, [arXiv:1802.00085](https://arxiv.org/abs/1802.00085),
Theorem 1.2, supplies
\(\gg P/\log P\) primes in each fixed relative-length box and residue
class modulo four.  Unique factorization then gives

\[
 \gg \frac{L^2}{(\log L)^4}=L^{2-o(1)}
\tag{164.C21}
\]

squarefree products satisfying the geometric unit-profile control.
Consequently any coefficient-uniform positive transport/BV theorem based
only on the frozen support, bounded profile, finite variation, and sign
mass has \(L^{2-o(1)}\) capacity.  It cannot supply the unweighted uniform
envelope, and hence cannot prove the target uniformly over that coefficient
class on polynomial \(L\)-blocks.

Equation (164.C21) is not a literal physical lower bound.  No accepted
hypothesis gives a pointwise lower plateau for the product
\(\eta_L\Phi W\) on those prime boxes, and even literal nonzero
coefficients retain the cross-\(N\) phase.  The control rejects only the
coefficient-uniform positive route.

## 5. Exact Fejer/van der Corput frontier

Let an integer interval \(I_L\) of length \(M_L\asymp L^2\) contain the
literal \(N\)-shell, extend \(c_N^{\rm rem}\) by zero outside it, and put

\[
 z_N=c_N^{\rm rem}e(J\sqrt N),\qquad R=\lceil L\rceil.
\tag{164.C22}
\]

Define the sliding Fejer energy by either of the exactly equal formulas

\[
\begin{aligned}
 \mathfrak E_R^{\rm rem}
 &:={1\over R}\sum_{s\in\mathbb Z}
       \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2\\
 &=\sum_N|c_N^{\rm rem}|^2
 +2\Re\sum_{1\le r<R}\left(1-{r\over R}\right)
   \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
   e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
\end{aligned}
\tag{164.C23}
\]

The first identity follows by counting the \(R-r\) windows containing
each ordered pair at gap \(r\).  Also

\[
 \sum_s\sum_{j=0}^{R-1}z_{s+j}
 =R\sum_Nz_N,
\tag{164.C24}
\]

and at most \(M_L+R-1\) windows are nonzero.  Cauchy's inequality gives
the exact endpoint-safe van der Corput bound

\[
 \boxed{
 \left|\mathcal S_{L,1}^{\rm rem}\right|^2
 \le {M_L+R-1\over R}\,\mathfrak E_R^{\rm rem}.}
\tag{164.C25}
\]

The elementary diagonal estimate is

\[
 \sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon,
\tag{164.C26}
\]

because \(|b_N^{\rm rem}|\le\tau(M_N)\) and there are \(O(L^2)\)
rows.  Since \(M_L\asymp L^2\) and \(R\asymp L\), (164.C25) proves the
residual target, after renaming \(\varepsilon\), from the single
actual-direction theorem

\[
 \boxed{
 \Re\sum_{1\le r<R}\left(1-{r\over R}\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left({Jr\over\sqrt{N+r}+\sqrt N}\right)
 \le C_\varepsilon L^2X^\varepsilon.}
\tag{164.C27}
\]

There is no absolute value around an individual shift, divisor pair,
selector branch, or Mobius opening.  The one-sided upper bound in
(164.C27) is sufficient because (164.C23) is nonnegative and its diagonal
is already target-safe.

Expanding the two physical coefficients in (164.C27) produces the exact
near-product additive-shift relation

\[
 N=dm,\qquad N+r=d'm',\qquad
 \boxed{d'm'-dm=r},\qquad 1\le r<R\asymp L,
\tag{164.C28}
\]

where both products are supported squarefree literal rows, \(d,d'\) are
odd, the factors \(2\) are retained in \(m,m'\) when present, and both
residual selectors, both literal amplitudes, and the displayed square-root
phase difference are retained.  Equivalently, every coefficient and
selector is extended by zero off its literal row domain.  This is the first
exact cross-\(N\) theorem, not an arbitrary-coefficient large-sieve
statement.

The scale \(R\asymp L\) is minimal for this diagonal ledger: if
\(R=o(L)\), even \(\mathfrak E_R\ll L^2X^\varepsilon\) inserted in
(164.C25) leaves \(L^4/R\), larger than the target square \(L^3\).

The accepted rank-one character-Poisson route instead has collar
\(|s\ell-XQR|\ll QRJ/L\), individual scale
\(L^{3/2}/(QR\sqrt J)\), and positive collar capacity
\(\sqrt{JL}\).  Taking absolute values in (164.C27) destroys its actual
signed real part and leaves a positive additive-shift form.  The
multiplicative rank-one collar is a separate accepted adverse positive
route with the same missing-power warning, not the same geometry.
Conversely, that collar obstruction does not disprove (164.C27); the latter
is a new actual-coefficient short-shift energy theorem.

## 6. First open step and controls

The first open affirmative step is exactly (164.C27), or any weaker direct
theorem that implies \(\mathfrak E_R^{\rm rem}\ll L^2X^\varepsilon\).
Exact radical-collision sparsity, coarse \(L^2\) coefficient energy, a
common-test large sieve, positive transport, and positive collar counting do
not imply it.  It must exploit the literal residual arithmetic and fail on
phase-aligned arbitrary arrays.

The controls close as follows:

| Control | Outcome |
|---|---|
| one-time residual subtraction | GREEN by (164.C4). |
| odd/even divisor universe | GREEN by (164.C3)--(164.C6); the even factor stays on the complementary leg. |
| sign mass and unmatched branch | GREEN by (164.C8)--(164.C9). |
| ordered Abel and endpoint term | GREEN by (164.C11)--(164.C12). |
| zero extension and hard point values | GREEN by (164.C16)--(164.C18). |
| monotone/BV normalization | GREEN by the exact sharp dual estimate (164.C14); no free cemetery is used. |
| positive transport target | REJECTED at coefficient-uniform level by (164.C20)--(164.C21), not physically disproved. |
| outer phase | GREEN and retained in (164.C23)--(164.C28). |
| diagonal and missing half-power | GREEN: (164.C26) plus length-\(L\) Fejer control has exactly the target ledger. |
| rank-one collar comparison | GREEN as a route comparison, not a universal no-go. |
| updated literature | No later classical pointwise exponent or drop-in theorem for (164.C27) was identified in the dated primary-source scan. |
| downstream scope | QUARANTINED. |

Round 164 used no numerical or symbolic experiment.  Mathematica is
available, but none of the exact finite identities above requires a
computer check.

## 7. Recommended state effect

Promote one proved-internal reduction/obstruction node containing
(164.C4), (164.C8), (164.C11), (164.C14), (164.C21), and
(164.C23)--(164.C28), subject to independent seam review.  Attach it only
as an inconclusive dependency to the two hard-TOP parents.  Keep the full
residual, full \(t=1\) face, remaining few-point channels, hard TOP, both
smooth M2 packets, M9--M2, M9--M1, endpoint uniformity, M9, the bridge,
the quarter theorem, and both global exponents unchanged.

The exact next action is the actual residual short-shift energy (164.C27).
It should be attacked before another within-product matching or another
positive collar count.
