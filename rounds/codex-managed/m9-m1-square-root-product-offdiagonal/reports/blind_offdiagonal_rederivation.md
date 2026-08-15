# 1. Result

**Packet-level no-go, together with a sharp elementary shell bound.**  Put

\[
 a_{k,\rho,r}=\epsilon_\rho c_\rho(k,r),\qquad
 D=\sum_{k\asymp Q}\sum_{\rho\in\{1,3\}}\sum_{r\asymp k}
 |a_{k,\rho,r}|^2.
\]

Then the stated diagonal is exactly \(D\asymp Q^2\), and there is no
cross-residue contribution to it.  If \(\mathcal O_\delta\) denotes the
part of the ordered off-diagonal with \(u_1-u_2=\delta\), then, using the
actual coefficient only through its diagonal mass,

\[
 |\mathcal O_\delta|\leq 2D\ll Q^2
 \quad(\delta\in\tfrac12\mathbb Z\setminus\{0\}).
\tag{1.1}
\]

Thus every fixed difference shell, in particular the union of the
\(|\Delta|=1/2,1\) shells, already has the target size.  There are
\(O(Q)\) possible shells, however, and the strongest coefficient-free
consequence is only

\[
 |\mathcal O|\ll QD\ll Q^3.
\tag{1.2}
\]

The desired \(Q^2X^\varepsilon\) bound is false for arbitrary
\((k,r)\)-dependent coefficients having the stated support and diagonal
normalization.  Qualitative smoothness alone does not repair this: a
smooth phase-conjugating coefficient gives \(\mathcal O\asymp Q^3\).
It need not belong to the inherited symbol class, because its derivatives
are large.  Hence this is not a falsification of the *actual* pulled-back
coefficient, whose quantitative formula and symbol seminorms are absent
from the packet.  The actual target remains plausible but unproved.
Perfect-square, fourth-power, and general product-square resonances have
only \(O(Q^{3/2})\) unsigned off-diagonal pairs (and fewer for fourth
powers), so under a bounded-symbol hypothesis they do not by themselves
contradict the target.

# 2. Exact statement and hypotheses

Let \(k,r\) be integers in the fixed smooth interior ranges described in
the packet.  I use only the following consequences of those ranges:

1. \(k\asymp Q\), \(r\asymp k\), and \(u=r-\rho/4\asymp Q>0\);
2. for each \(k\), the number \(N_k\) of active pairs \((\rho,r)\) is
   \(O(Q)\);
3. \(|\epsilon_\rho|=1\), as appropriate for the two signed residue
   factors;
4. the supplied diagonal assertion is \(D\asymp Q^2\).

No pointwise bound, factorization, derivative estimate, or formula for
\(c_\rho(k,r)\) is assumed in (1.1)--(1.2).  For the numerical *counts* of
square-product fibers no coefficient hypothesis is needed.  Turning
those counts into weighted absolute bounds additionally requires, for
example, \(|c_\rho(k,r)|\ll X^\varepsilon\).  That extra bound is stated
only where it is used and is not inferred from the word “smooth.”

Under these hypotheses the exact conclusions are:

\[
 \sum_{k\asymp Q}|P_k|^2=D+\mathcal O,
 \qquad \mathcal O\in\mathbb R,
 \qquad -D\leq\mathcal O\ll QD,
\tag{2.1}
\]

the shell bound (1.1), the exact alias formulae in Section 3, and the
resonant-family counts in Section 5.  In contrast, no uniform estimate
\(\mathcal O\ll D X^\varepsilon\) (for every \(\varepsilon>0\)) follows
for arbitrary moving coefficients from these hypotheses.

# 3. Proof/derivation

For \(i=(\rho_i,r_i)\), expansion gives

\[
 |P_k|^2=\sum_i|a_{k,i}|^2+
 \sum_{i\ne j}a_{k,i}\overline{a_{k,j}}
 e\!\left(2\sqrt{Xk}(\sqrt{u_i}-\sqrt{u_j})\right).
\tag{3.1}
\]

The second sum is precisely the displayed ordered off-diagonal in the
packet.  Reversal of \((i,j)\) conjugates a summand, so \(\mathcal O\) is
real and (2.1) gives \(\mathcal O\geq-D\).

The difference classes are exact.  If \(\rho_1=\rho_2\), then

\[
 \Delta=r_1-r_2\in\mathbb Z,
\]

and \(\Delta=0\) forces the same index.  If
\((\rho_1,\rho_2)=(1,3)\), then

\[
 \Delta=(r_1-r_2)+\tfrac12\in\mathbb Z+\tfrac12,
\]

whereas for \((\rho_1,\rho_2)=(3,1)\),

\[
 \Delta=(r_1-r_2)-\tfrac12\in\mathbb Z+\tfrac12.
\]

Consequently every off-diagonal difference lies in
\(\tfrac12\mathbb Z\setminus\{0\}\), and the cross-residue minimum is
exactly \(1/2\).  Moreover

\[
 d:=\sqrt{u_1}-\sqrt{u_2}
   ={\Delta\over\sqrt{u_1}+\sqrt{u_2}},
 \qquad |d|\asymp {|\Delta|\over\sqrt Q}.
\tag{3.2}
\]

For a fixed \(\delta\), each index \((\rho_1,r_1)\) has at most two
partners \((\rho_2,r_2)\) satisfying \(u_1-u_2=\delta\), one for each
choice of \(\rho_2\); the same is true with incoming and outgoing roles
reversed.  Therefore \(2|zw|\leq |z|^2+|w|^2\) gives

\[
 \begin{aligned}
 |\mathcal O_\delta|
 &\leq \sum_{k}\sum_{u_i-u_j=\delta}|a_{k,i}a_{k,j}|\\
 &\leq {1\over2}\sum_k\sum_{u_i-u_j=\delta}
       (|a_{k,i}|^2+|a_{k,j}|^2)
 \leq 2D.
 \end{aligned}
\tag{3.3}
\]

There are \(O(Q)\) admissible half-integral differences, proving
(1.2).  Equivalently, direct Cauchy gives

\[
 \sum_k|P_k|^2\leq\sum_kN_k\sum_i|a_{k,i}|^2\ll QD,
\tag{3.4}
\]

which is the same elementary barrier.

This barrier is genuine for arbitrary moving coefficients.  Choose a
nonnegative smooth cutoff \(b(k,r)\) supported on a fixed interior
subsector, equal to \(1\) on a smaller subsector, and set

\[
 c_\rho(k,r)=\overline{\epsilon_\rho}\,b(k,r)
 e\!\left(-2\sqrt{Xk(r-\rho/4)}\right).
\tag{3.5}
\]

Then every summand of \(P_k\) equals \(b(k,r)\).  Hence
\(D\asymp Q^2\), \(P_k\asymp Q\) on \(\asymp Q\) values of \(k\), and

\[
 \mathcal O=\sum_k|P_k|^2-D\asymp Q^3.
\tag{3.6}
\]

The function in (3.5) is smooth as an ordinary function on the interior,
but its derivatives contain powers of the large phase parameter.  Thus
it proves that an arbitrary-coefficient large sieve, and also a theorem
based only on qualitative smoothness, is false; it does not assert that
(3.5) has the inherited symbol bounds of the actual coefficient.

For completeness, the exact \(k\)-phase and all its Poisson stationary
aliases can be written without approximation.  Holding \(u_1,u_2\)
fixed, put

\[
 f(t)=2\sqrt X\,d\sqrt t,\qquad
 f'(t)={\sqrt X\,d\over\sqrt t},\qquad
 f''(t)=-{\sqrt X\,d\over2t^{3/2}}.
\tag{3.7}
\]

With the Poisson convention \(e(f(t)-mt)\), a stationary alias exists
exactly for an integer \(m\) having the sign of \(d\) and satisfying

\[
 t_m={Xd^2\over m^2}
\tag{3.8}
\]

inside the \(k\)-support.  At that point,

\[
 f(t_m)-mt_m={Xd^2\over m},\qquad
 |f''(t_m)|={|m|^3\over2Xd^2}.
\tag{3.9}
\]

There are no other stationary aliases; \(m=0\) is nonstationary because
\(d\ne0\).  On \(t,u_i\asymp Q\), the stationary integers have size

\[
 |m|\asymp {\sqrt X\,|\Delta|\over Q},
\tag{3.10}
\]

and a single stationary integral has the natural magnitude

\[
 |f''(t_m)|^{-1/2}\asymp
 {Q\over X^{1/4}|\Delta|^{1/2}}.
\tag{3.11}
\]

There are on the order of
\(1+\sqrt X|\Delta|/Q\) possible aliases across a fixed dyadic
\(k\)-range.  Even optimistically summing (3.11) absolutely produces the
scale \(X^{1/4}|\Delta|^{1/2}\) (plus the possible single-alias term).
At \(Q=X^{1/5}\) this is already larger than the trivial kernel bound
\(Q\) for \(|\Delta|\geq1/2\).  Thus a termwise B-process supplies no
required saving; cancellation among its exact dual phases
\(e(Xd^2/m)\) would itself be a new theorem.

The exact forward \(k\)-difference, for an integer \(h>0\), is

\[
 g_h(t):=f(t+h)-f(t)
 ={2\sqrt X\,d h\over\sqrt{t+h}+\sqrt t},
\tag{3.12}
\]

with

\[
 g_h'(t)=\sqrt X\,d\left({1\over\sqrt{t+h}}-{1\over\sqrt t}\right)
 =-{\sqrt X\,d h\over
 \sqrt t\sqrt{t+h}(\sqrt t+\sqrt{t+h})},
\tag{3.13}
\]

and

\[
 g_h''(t)={\sqrt X\,d\over2}
 \left(t^{-3/2}-(t+h)^{-3/2}\right).
\tag{3.14}
\]

Thus the stationary aliases after differencing are *exactly* the
integers \(m\) in the endpoint range of \(g_h'\); they have sign opposite
to \(d\), and monotonicity from (3.14) gives at most one stationary point
for each such \(m\).  Writing \(a=\sqrt t\), \(b=\sqrt{t+h}\), the
stationary equation and reduced phase are

\[
 m=-{\sqrt X\,d(b-a)\over ab},\qquad
 g_h(t)-mt=-m(a^2+2ab).
\tag{3.15}
\]

Their scale is

\[
 |m|\asymp {\sqrt X\,|\Delta|h\over Q^2}.
\tag{3.16}
\]

These formulae hold when \(r_1,r_2\), hence \(u_1,u_2\), are held fixed
while summing in \(k\).  Any reindexing that moves \(r_i\) with \(k\)
changes \(d\) and requires a fresh derivative calculation; silently
using (3.7) after such a reindexing would be invalid.

# 4. First doubtful or unproved step

The first unsupported step is the needed transition from the separate
shell estimates

\[
 |\mathcal O_\delta|\ll D
\]

to a signed sum over \(O(Q)\) shells of total size \(O(DX^\varepsilon)\).
Triangle inequality loses exactly the factor \(Q\).  No cancellation in
\(\delta\), in the stationary-alias variable \(m\), or between the two
residue classes follows from the packet.  Moreover, because the
coefficient depends on both \(k\) and \(r\), a large-sieve theorem that
treats its entries as arbitrary is ruled out by (3.5).

For the actual coefficient, the first required new input is a
quantitative formula or symbol expansion showing why it cannot track the
phase, followed by a bound that gains a full factor \(Q\) in the signed
sum while retaining all aliases and edges.  The packet gives neither the
needed seminorms nor a factorization to which a standard large sieve can
be applied.  Consequently invoking Robert--Sargos, a double large sieve,
a B-process, or a spectral/Hankel theorem at this point would be an
unsupported hypothesis match, not a proof.

# 5. Required control tests and outcomes

1. **Diagonal and residue control: passed.**  Equation (3.1) gives the
   exact diagonal \(D\asymp Q^2\).  Equality \(u_1=u_2\) is possible only
   for the identical same-residue index; cross residues differ by a
   half-integer.  The exact minimum is \(|\Delta|=1/2\).
2. **Near-diagonal shells: passed at target scale.**  For
   \(|\Delta|=1/2\), the pairs are cross-residue pairs with either equal
   \(r\) or adjacent \(r\), according to orientation.  For
   \(|\Delta|=1\), they are same-residue adjacent-\(r\) pairs.  The four
   directed shells together are \(O(D)=O(Q^2)\) by (3.3), without a
   pointwise coefficient bound.
3. **Poisson/B-process aliases: passed algebraically, no saving
   obtained.**  Equations (3.8)--(3.9) list every original stationary
   alias, and (3.13)--(3.15) list every differenced alias.  Absolute
   treatment of the aliases is no better than the trivial \(k\)-sum at
   the benchmark.  Cancellation in \(e(Xd^2/m)\) remains unproved.
4. **Squares, fourth powers, and product-square fibers: no
   counterexample to the bounded actual-symbol target.**  Write
   \(n=4r-\rho\), so \(u=n/4\) and the individual phase is

   \[
   2\sqrt{Xku}=\sqrt X\sqrt{kn}.
   \tag{5.1}
   \]

   If \(X=L^2\) (hence also if \(X\) is a fourth power) and \(kn=s^2\),
   the phase equals the integer \(Ls\) and its exponential is \(1\).
   Write \(k=da^2\) with \(d\) squarefree.  Since \(n\) is odd,
   \(kn\) is a square exactly when \(d\) is odd and
   \(n=db^2\) with \(b\) odd.  The residue is then forced:
   \(\rho=3\) for \(d\equiv1\pmod4\) and \(\rho=1\) for
   \(d\equiv3\pmod4\).  In dyadic ranges \(k,n\asymp Q\), the number of
   ordered off-diagonal pairs within all such fixed-\(k\) fibers is

   \[
   \ll\sum_{\substack{d\ll Q\\d\ \mathrm{odd\ squarefree}}}
   \left({Q\over d}\right)^{1/2}
   \left({Q\over d}\right)
   \ll Q^{3/2}.
   \tag{5.2}
   \]

   The subfamily \(k=a^2,n=b^2\) has the same \(O(Q^{3/2})\) energy
   count; the fourth-power subfamily \(k=a^4,n=b^4\) has only
   \(O(Q^{3/4})\).  Under \(|c|\ll X^\varepsilon\), their total absolute
   weighted contribution is therefore at most
   \(Q^{3/2}X^{2\varepsilon}\), below \(Q^2X^{2\varepsilon}\).  Without a
   pointwise coefficient bound these are only unsigned counts.
5. **Signed-versus-unsigned control: passed.**  The fiber count (5.2)
   and all spacing counts are unsigned.  They cannot lower-bound or
   upper-bound the signed energy without coefficient information.
   Conversely, the phase-conjugating example aligns the *effective*
   signed coefficients and is why the arbitrary-coefficient statement
   is genuinely false.
6. **Theorem and scope audit: no external theorem was used.**  In
   particular no unverified double-large-sieve, Robert--Sargos,
   Bombieri--Iwaniec/Huxley, Jutila, spectral, or Hankel hypothesis is
   imported.  Every conclusion here is restricted to the supplied
   smooth fixed-interior sector and implies nothing about edges, the full
   cone, a radial interval, M9-M1, M9, or a final exponent.

# 6. Dependencies and exact artifacts used

- `AGENTS.md`, for the report contract and statement-only discipline.
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/derivation_packet.md`, for (68.1)--(68.4), the fixed-interior support, the benchmark \(Q=X^{1/5}\), and the supplied diagonal normalization.
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/briefs/blind_offdiagonal_rederivation.md`, for the isolated assignment and controls.

No graph file, prior synthesis, other brief, Round-68 report, external
source, or numerical computation was read or used.

# 7. Recommended state effect

**No change.**  Do not promote (68.2): the actual-coefficient target is
neither proved nor falsified.  Retain this report as an obstruction: each
fixed near-diagonal shell is harmless, the elementary aggregate stalls
at \(Q^3\), exact square/fourth-power fibers are too sparse to refute a
bounded-symbol theorem, and any successful next step must explicitly
use the quantitative structure of the actual moving coefficient to
control the full stationary-alias sum.  Reject any proposed theorem
whose coefficient class is arbitrary in \((k,r)\), since (3.5)--(3.6)
falsify that formulation.
