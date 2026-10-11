# Actual four-point dispersion: paid sectors and an actual Gram-certificate obstruction

Campaign: `gc-complete-four-point-correlation`. Round: 212.
Task: `four_point_oscillatory_attack`. Role: discovery, selected context.
Generated: 2026-09-27T16:23:49Z.
Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Candidate evidence only. Effort: 100 percent analytical; zero experiments.

## 1. Result: complete sector prices and a scoped actual-source no-go

The actual four-point target remains unproved. The following are proved
without a four-point density hypothesis.

1. The complete repeated-shift sector `h=k` and the complete small-product
   sector `Thk/N^(3/2)<=1` together cost at most
   `T^(166/325+epsilon)`, directly under the actual divisor envelope.
2. A dyadic decomposition by the product `hk`, retaining the modulus after
   each full `n`-sum, gives a complete sufficient signed dispersion input.
   On a shell `Lambda~Thk/N^(3/2)>1`, an actual root-mean-square bound
   `N/Lambda+sqrt(N)` would suffice after all shell multiplicities and
   both exceptional sectors are restored. This bound is not proved.
3. A particular proposed way to obtain that input fails on the actual
   coefficients. After removing both paid sectors, the absolute
   four-point mass still averages at least a constant times `N` at every
   fixed interior power scale. A positive radius-Gram certificate that
   takes absolute values of the pairwise Fourier kernel therefore has
   cost at least

   \[
   c\,N T^{-38/325}.
   \tag{1}
   \]

   This exceeds `T^(166/325)` at every fixed scale
   `N=T^alpha` with `204/325<alpha<242/325`. The same obstruction holds
   if this positive certificate is grouped into product shells before
   taking square roots, or capped by the trivial coefficient mass.

Statement 3 is a lower bound on an explicitly defined positive upper
certificate, not on the actual signed dispersion, `D`, or `A4`. It uses
the surviving actual arithmetic mass, rather than an assumed density,
an adversarial coefficient vector, the already paid repeated shifts,
or the already paid small products. It is distinct from the earlier
outer-absolute CRT failure: no divisor progression is estimated in
isolation in its proof.

## 2. Exact statements, hypotheses and quantities

Write `e(x)=exp(2 pi i x)` and take the actual functions and coefficients
from the frozen strategy:

\[
\begin{gathered}
 T\ge2,\qquad I=[T/\sqrt2,\sqrt3T],\qquad b=83/650,\\
 T^{4b}<N<T^{1-2b},\qquad
 g_N(t)=(t/N)^{-3/4}\Psi(\sqrt{t/T})v(t/N),\\
 s_n=r_2(n)g_N(n)e(R\sqrt n),\qquad
 L=\max(2,\lceil N^{1/2}T^{-2b}\rceil),\qquad
 K=\max(2,\lceil NT^{-4b}\rceil).
\end{gathered}
\tag{2}
\]

The fixed real smooth mask `v` is nonzero and supported in `[1,4]`;
the actual real mollifier transform has `Psi(0)=1`. Every sequence is
zero extended. The complete raw correlations and their average are

\[
 D_{h,k}(R)=\sum_n s_{n+h+k}\overline{s_{n+k}}
                      \overline{s_{n+h}}s_n,\qquad
 A_4(R)=\frac1{LK}\sum_{1\le h<L,\,1\le k<K}|D_{h,k}(R)|.
\tag{3}
\]

In particular, there is no extra physical `N^(-3/4)` in `g_N`. Put

\[
\begin{split}
 a_{h,k}(n)&=r_2(n)r_2(n+h)r_2(n+k)r_2(n+h+k),\\
 W_{h,k}(t)&=g_N(t)g_N(t+h)g_N(t+k)g_N(t+h+k),\\
 \psi_{h,k}(t)&=\sqrt{t+h+k}-\sqrt{t+k}-\sqrt{t+h}+\sqrt t,\\
 Q&=N^{3/2}/T,\qquad
 \Lambda_{h,k}=hk/Q,\qquad
 \Lambda_* =LK/Q\asymp T^{1-6b}=T^{76/325}.
\end{split}
\tag{4}
\]

Then `D=sum a W e(R psi)` exactly. Its ambient overlap is
`[ceil(N),floor(4N-h-k)]`, with all mask zeros retained. The original
arithmetic coefficients obey, for every positive `epsilon`,
`a_(h,k)(n)<<N^epsilon` on this overlap.

Let

\[
 \mathcal E=\{(h,k):h=k\}\cup\{(h,k):hk\le Q\},\qquad
 \Omega=\{1\le h<L,1\le k<K\}\setminus\mathcal E.
\tag{5}
\]

The upper bounds below hold uniformly throughout (2), including bounded
cutoffs. The lower-certificate obstruction is asserted at each fixed
interior power scale `N=T^alpha`, `4b<alpha<1-2b`, or uniformly when
`N/T^alpha` stays between fixed positive constants. Thus `L,K` grow by
fixed powers there. It is not asserted uniformly as `alpha` approaches
the lower endpoint with `T`.

For the obstruction, fix any nonnegative smooth `w`, compactly supported
in the interior of `[1/sqrt(2),sqrt(3)]`, with integral one. Define

\[
 \widehat w_+(y)=\int w(t)e(ty)\,dt,\qquad
 u_n=r_2(n)|g_N(n)|,
\]
\[
 B_{h,k}(n)=u_nu_{n+h}u_{n+k}u_{n+h+k}
          =|a_{h,k}(n)W_{h,k}(n)|,\qquad
 M_{h,k}=\sum_n B_{h,k}(n),
\tag{6}
\]

and the **specified positive radius-Gram certificate**

\[
 G_{h,k}=
 \sum_{n,m}B_{h,k}(n)B_{h,k}(m)
 \left|\widehat w_+\bigl(T[\psi_{h,k}(n)-\psi_{h,k}(m)]\bigr)\right|,
\]
\[
 \mathcal P_G=\frac1{LK}\sum_{(h,k)\in\Omega}\sqrt{G_{h,k}}.
\tag{7}
\]

All sums in (7) are complete. No mean is subtracted. In particular this
no-go does not cover a justified centered arithmetic remainder or a
dispersion argument that keeps the Fourier-kernel signs.

## 3. Derivation and complete power accounting

### A. Pay repeated shifts and all small products using the actual envelope

The exact integer lengths satisfy `K>=L`, since the unrounded second
length is the square of the first. Throughout the open band both
unrounded lengths exceed one, and

\[
 L\asymp N^{1/2}T^{-2b},\quad
 K\asymp NT^{-4b},\quad LK\asymp N^{3/2}T^{-6b}.
\tag{8}
\]

For sufficiently large `T` these lengths are at most `delta N`, for
any fixed positive `delta`; bounded `T` is handled by enlarging the
constant in the finite trivial bound. The divisor envelope gives

\[
 |D_{h,k}(R)|\le M_{h,k}\ll_\epsilon N^{1+\epsilon}.
\tag{9}
\]

There are at most `L` repeated pairs. Hence, uniformly in real `R`,

\[
 \frac1{LK}\sum_{h=k}|D_{h,k}|
 \ll N^\epsilon\frac NK\le T^{4b+\epsilon}.
\tag{10}
\]

For `hk<=Q`, the exact count is at most

\[
 \sum_{h<L}\left\lfloor\frac Qh\right\rfloor
 \le Q\sum_{h<L}\frac1h\ll Q\log(2L).
\tag{11}
\]

If `Q<1` the sector is empty; the same upper bound remains valid.
Consequently

\[
 \frac1{LK}\sum_{hk\le Q}|D_{h,k}|
 \ll_\epsilon \frac{N^{1+\epsilon}Q\log(2L)}{LK}
 \ll_\epsilon T^\epsilon NT^{6b-1}
 \le T^{4b+\epsilon}.
\tag{12}
\]

Here the final inequality uses `N<=T^(1-2b)`. Double-counting the
intersection of the two exceptional sectors only enlarges this upper
bound. Formula (10) uses the actual repeated product
`r2(n)r2(n+h)^2r2(n+2h)`. It does not incorrectly regard `h=k>0` as a
zero-phase diagonal. No four-point density is needed in (10)--(12).

### B. A complete product-shell dispersion inequality

Partition the remaining set into the disjoint shells

\[
 \Omega_j=\{(h,k)\in\Omega:2^j<\Lambda_{h,k}\le2^{j+1}\},
 \qquad j=0,1,\ldots,
\]
\[
 m_j=|\Omega_j|,\qquad \delta_j=m_j/(LK),\qquad
 E_j(R)=\frac1{m_j}\sum_{(h,k)\in\Omega_j}|D_{h,k}(R)|^2.
\tag{13}
\]

Empty shells are omitted. The conventions assign every `Lambda>1`
exactly once, including powers of two. There are `O(log(2+Lambda_*))`
nonempty shells, and the product count gives

\[
 \delta_j\ll
 \min\left(1,\frac{2^j\log(2L)}{\Lambda_*}\right),\qquad
 \sum_j\delta_j\le1.
\tag{14}
\]

Cauchy is applied only to the complete correlations inside each shell:

\[
 A_4(R)\ll_\epsilon
 N^\epsilon\left(\frac NK+
          \frac{NQ\log(2L)}{LK}\right)
       +\sum_j\delta_j E_j(R)^{1/2}.
\tag{15}
\]

This is a complete quantitative inequality, not an estimate on a
convenient divisor subfamily. It includes the whole residual `Omega`.
The hypothetical arithmetic input

\[
 \boxed{\quad E_j(R)^{1/2}
       \ll_\epsilon T^\epsilon\left(\frac N{2^j}+\sqrt N\right),
       \quad R\in I,\quad\hbox{every nonempty shell}.\quad}
\tag{16}
\]

would imply, with logarithms absorbed by independently chosen epsilon,

\[
 A_4(R)\ll_\epsilon T^\epsilon
      \left(\frac NK+\frac N{\Lambda_*}+\sqrt N\right)
 \ll_\epsilon T^{166/325+\epsilon}.
\tag{17}
\]

Indeed `sum delta_j/2^j<<log(2L)log(2+Lambda_*)/Lambda_*`,
`N/Lambda_*=N^(5/2)/(TLK)`, and
`sqrt(N)<=T^(121/325)<T^(166/325)`. The smooth-mean-size term `N/2^j`
is therefore paid with the correct product-shell density. A single
unweighted Cauchy over the full shift rectangle would lose this density.

### C. What the genuinely signed arithmetic input contains

The exact squared shell energy is

\[
 E_j(R)=\frac1{m_j}\sum_{(h,k)\in\Omega_j}
 \sum_{n,m}a_{h,k}(n)a_{h,k}(m)W_{h,k}(n)W_{h,k}(m)
 e\bigl(R[\psi_{h,k}(n)-\psi_{h,k}(m)]\bigr).
\tag{18}
\]

The `n=m` diagonal in (18) is `O_epsilon(N^(1+epsilon))`.
The off-diagonal, paired with its conjugate under `n<->m`, is real.
A sufficient input for (16) is therefore the **one-sided signed** bound

\[
 \frac1{m_j}\sum_{(h,k)\in\Omega_j}
 \sum_{n\ne m}a_{h,k}(n)a_{h,k}(m)W_{h,k}(n)W_{h,k}(m)
 e\bigl(R[\psi_{h,k}(n)-\psi_{h,k}(m)]\bigr)
 \ll_\epsilon T^\epsilon\left(N^2 2^{-2j}+N\right).
\tag{19}
\]

Taking absolute values of the individual `n,m` terms is not (19).
No independence assumption about the eight actual arithmetic factors
in this formula is available.

For precision, their divisor representation is the exact finite product

\[
 a_{h,k}(n)=4^4
 \sum_{\substack{d_0\mid n,\ d_1\mid n+h\\
                 d_2\mid n+k,\ d_3\mid n+h+k}}
       \chi_4(d_0)\chi_4(d_1)\chi_4(d_2)\chi_4(d_3).
\tag{20}
\]

All divisors up to the actual four arguments, including their large
divisors, are present. Equivalently it is the exact number of ordered
Gaussian-integer quadruples `(z_0,z_1,z_2,z_3)` whose squared norms
are `n,n+h,n+k,n+h+k`, respectively. Substituting two copies of (20)
into (18) keeps all eight divisor sums inside the complete `n,m` sum
and gives the factor `4^8`. Neither representation supplies (19).

The elementary parity control already prevents an unsupported claim
of independent character averaging: if `h,k` are even and `n` is odd,
the permitted divisor choice `d_eta=n+eta` has

\[
 \chi_4(n)\chi_4(n+h)\chi_4(n+k)\chi_4(n+h+k)=1.
\tag{21}
\]

The same holds for odd `m`; the corresponding eight-character product
is also one. This is only an exact algebraic control, not a positive
lower bound for the full signed divisor expansion. Cancellation in
the phases and across all the other divisor choices remains possible.
No separate absolute CRT progression closure is attempted here.

### D. Actual absolute four-point mass survives both paid sectors

The following proof supplies actual mass for the certificate test, so
the obstruction does not presume a four-point asymptotic.

First,

\[
 \sum_n u_n\asymp N,\qquad
 \max_n u_n\ll_\epsilon N^\epsilon.
\tag{22}
\]

For the lower bound choose a fixed compact interval `[a,b]` in `(1,4)`
on which `|v|` is bounded below. Since `N/T->0` uniformly in the
required band, `Psi(sqrt(t/T))` is bounded away from zero there for
large `T`. The elementary disk-area estimate gives

\[
 \sum_{aN\le n\le bN}r_2(n)
       =\pi(b-a)N+O(\sqrt N+1)\gg N.
\tag{23}
\]

It follows directly by enclosing the unit squares based at lattice
points between disks with radii differing by a fixed constant.
Changing real endpoint conventions costs only the same boundary
order. The upper bound in (22) follows from that disk-area estimate
on the full support and boundedness of `g_N`; the pointwise envelope
is the actual divisor bound. No advanced correlation source is used.

Set `C_h^u=sum_n u_n u_(n+h)`. For a nonnegative sequence supported
in an ambient interval of length `O(N)`, the finite moving-sum identity
and Cauchy give

\[
 \sum_n u_n^2+
 2\sum_{h=1}^{L-1}(1-h/L)C_h^u
 \ge c\frac L N\left(\sum_nu_n\right)^2
 \ge c_1 LN.
\tag{24}
\]

The first diagonal is `O_epsilon(N^(1+epsilon))`. At each fixed
`alpha>4b`, choose epsilon small enough that `N^epsilon=o(L)`.
Positivity and (24) then yield

\[
 \sum_{h=1}^{L-1}C_h^u\ge c_2 LN.
\tag{25}
\]

For each `h`, apply the length-`K` moving-sum inequality to
`t_n=u_nu_(n+h)`. It gives

\[
 \sum_n u_n^2u_{n+h}^2+
 2\sum_{k=1}^{K-1}(1-k/K)M_{h,k}
 \ge c\frac K N(C_h^u)^2.
\tag{26}
\]

Summing in `h`, using Cauchy and (25), and bounding the displayed
diagonals by `O_epsilon(L N^(1+epsilon))` proves

\[
 \sum_{h<L,k<K}M_{h,k}
 \ge c_3 LKN-O_\epsilon(LN^{1+\epsilon})
 \ge c_4 LKN.
\tag{27}
\]

The last step uses `N^epsilon=o(K)`, also valid at each fixed interior
power scale. This proof retains every shift and its zero-extended
support. It uses no individual lower bound for any shifted correlation.

By the complete counts (10)--(11), the mass removed with `mathcal E`
is at most

\[
 O_\epsilon\bigl(N^{1+\epsilon}
                         [L+Q\log(2L)]\bigr).
\tag{28}
\]

Relative to `LKN` this is
`O(N^epsilon/K+N^epsilon log(2L)/Lambda_*)=o(1)` after choosing
epsilon sufficiently small for the fixed alpha. Thus

\[
 \boxed{\qquad
 \sum_{(h,k)\in\Omega}M_{h,k}\ge c_5 LKN.
 \qquad}
\tag{29}
\]

This is an actual averaged **absolute** mass theorem on the residual.
It is not a claim of a smooth density for `a_(h,k)` or a lower bound
for any `D_(h,k)(R)`.

### E. The positive radius-Gram closure cannot exploit that mass

The exact normalized radius energy is

\[
 \frac1T\int w(R/T)|D_{h,k}(R)|^2\,dR
 =\sum_{n,m}a_{h,k}(n)a_{h,k}(m)W_{h,k}(n)W_{h,k}(m)
  \widehat w_+\bigl(T[\psi_{h,k}(n)-\psi_{h,k}(m)]\bigr)
 \le G_{h,k}.
\tag{30}
\]

The equality retains the signs. The inequality is exactly the loss
being tested. It implies an upper certificate for even the weaker
radius-average problem:

\[
 \frac1T\int w(R/T)
       \frac1{LK}\sum_{(h,k)\in\Omega}|D_{h,k}(R)|\,dR
       \le\mathcal P_G.
\tag{31}
\]

The right side of (31) is not asserted to control the pointwise
supremum without additional work. The test grants any such additional
pointwise step free: the exact positive right side already cannot be
bounded at the target scale on the upper part of the band.

Since `hat w_+(0)=1`, continuity supplies a fixed `eta>0` with
`|hat w_+(y)|>=1/2` for `|y|<=eta`. Direct differentiation gives

\[
 \psi_{h,k}'(t)=\frac38\int_0^h\int_0^k
                       (t+u+v)^{-5/2}\,dv\,du,
 \qquad |\psi_{h,k}'(t)|\ll hkN^{-5/2}.
\tag{32}
\]

Partition the full ambient `n` interval into at most
`C(1+Lambda_(h,k))` consecutive intervals, each of length at most
`cN/(1+Lambda_(h,k))`, where `c` is a sufficiently small fixed
constant. For two indices in the same interval, (32) gives
`T|psi(n)-psi(m)|<=eta`. The integer partition can use real bin
boundaries; it covers every integer exactly once. Write `b_i` for
the sum of `B_(h,k)(n)` in bin `i`. Positivity and Cauchy give

\[
 G_{h,k}\ge\frac12\sum_i b_i^2
          \ge c\frac{M_{h,k}^2}{1+\Lambda_{h,k}}.
\tag{33}
\]

Using `Lambda_(h,k)<Lambda_*`, `Lambda_*>>1` and (29) yields

\[
 \mathcal P_G\ge
 \frac{c}{LK\sqrt{1+\Lambda_*}}
       \sum_{(h,k)\in\Omega}M_{h,k}
 \gg\frac N{\sqrt{\Lambda_*}}
 \asymp N T^{-(1-6b)/2}=N T^{-38/325}.
\tag{34}
\]

This argument proves the obstruction on the residual itself; the
paid sectors contribute nothing to (34).

Grouping the terms of (30) into shells before taking a square root
does not help. Concavity of the square root gives

\[
 \sum_j\delta_j
       \left(\frac1{m_j}\sum_{(h,k)\in\Omega_j}G_{h,k}\right)^{1/2}
 \ge\frac1{LK}\sum_{(h,k)\in\Omega}\sqrt{G_{h,k}}
 =\mathcal P_G.
\tag{35}
\]

Also `|hat w_+|<=1`, so `G_(h,k)<=M_(h,k)^2`. Taking the minimum
with the trivial mass bound therefore leaves `sqrt(G_(h,k))`
unchanged. Both common modifications preserve (34).

At a fixed interior scale, the ratio of (34) to the target power is

\[
 T^{\alpha-(1-6b)/2-4b}
       =T^{\alpha-(1/2+b)}
       =T^{\alpha-204/325}.
\tag{36}
\]

Thus this exact positive certificate fails throughout
`204/325<alpha<242/325`. Its supremal upper-edge exponent deficit
is `38/325`; the open endpoint is not claimed attained. Arbitrarily
small epsilon losses do not repair a fixed positive gap.

This is a scoped failure of **absolute radius-Gram transport** for the
actual coefficients. It leaves (18)--(19) untouched when the complex
Fourier-kernel signs, divisor signs and phase correlations are retained.
It also leaves a justified mean-subtracted remainder untouched.

### F. Physical consequence and scope

The inherited, independently reviewed transfer is

\[
 |F_N(R)|^4\ll_\epsilon T^\epsilon
       [N/L^2+N/K+A_4(R)],\qquad
 F_N=N^{-3/4}\sum_ns_n.
\tag{37}
\]

Both displayed diagonals are at most `T^(4b)`. If the genuinely signed
input (16), or (19), were proved uniformly, (17) and the supplied
complete reconstruction would give only
`P(X)<<X^(102/325+epsilon)`. Nothing in this report proves that input.
The full quarter theorem, both independent M1/M2 obligations, all
endpoint quantifiers and the existing two-term moment estimate remain
unchanged. No moment equivalence or quarter consequence is inferred
from this particular fixed-b pointwise sufficient route.

## 4. First doubtful or unproved step

The first unproved arithmetic assertion is the actual shell dispersion
bound (16), equivalently a sufficient one-sided off-diagonal control
such as (19), on the full real `R` window and complete required band.
Its eight arithmetic factors are strongly dependent. The exact divisor
or Gaussian-norm representation does not establish it.

The failed candidate step is replacing the signed radius kernel in
(30) by its absolute value and expecting the resulting Gram certificate
to have the target size. Equations (22)--(36) refute that expectation
on an upper subband using surviving actual mass. Even an optimistic
free passage from radius mean square to a pointwise estimate cannot
remove this positive certificate's excess. A valid passage would in
fact require its own additional cost.

No assertion about an unweighted four-point mean, short-interval
discrepancy or external arithmetic theorem is used. This report does
not repeat the already rejected outer-absolute CRT strategy and does
not claim that any positive certificate lower bound is a lower bound
for a signed arithmetic quantity.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `actual_four_point_coefficients` | Passed for the stated lemmas: (3)--(6), (18), (20) use the exact original r2 product; (22)--(29) prove the surviving mass from actual lattice counts and finite Cauchy. No centered or arbitrary replacement. |
| `complete_shifts_overlap` | Passed: every pair belongs to the paid union or exactly one shell. Exact zero extension is retained in every moving sum. Repeated factors are priced by (10), not deleted. |
| `local_global_discrepancy` | No discrepancy transfer is presumed. The bins in (33) only lower-bound a positive certificate; they do not create a local arithmetic error estimate. |
| `density_hypotheses` | No density is assumed. The elementary one-point total (23) plus two finite inequalities proves an averaged absolute four-point mass, not a four-point asymptotic. |
| `real_endpoints` | Passed: (2), the smooth radius window, integer overlap, real bin boundaries and elementary disk-area estimate allow real parameters. Upper prices hold for bounded cutoffs; the no-go explicitly uses fixed interior power scales. |
| `all_restored_powers` | Passed: both safe-sector costs, shell fractions, the raw size-one four-factor amplitude, the squared-energy diagonal, Lambda_*, the Gram square root and the exponent threshold 204/325 are displayed. The failed method is granted no unsupported free pointwise theorem. |
| `signed_absolute_distinction` | Passed: (18)--(19) remain signed. (34) is solely a lower bound on (7). The exact positive mass (29) does not lower-bound D or A4. |
| `full_quarter_scope` | Passed: no new pointwise exponent, complete moment, M1/M2 closure or quarter theorem. A hypothetical (16) yields only the frozen milestone. |
| `statement_only_control` | Not claimed by this discovery report. No sibling, blind packet or successor file was opened. The surviving-mass lemma and Gram obstruction require the conductor's independent seam review. |

Additional algebraic controls: `h=k` gives the correct squared middle
factor; `Q<1` gives an empty small-product sector; `K>=L` follows from
the exact cutoff definitions; (21) tests actual character dependence;
the signed-mask case is handled by `u=r2|g_N|` only inside the specified
positive certificate. No sign restriction on the original mask was
silently imposed. No mathematical numerical test was run.

## 6. Dependencies and exact artifacts used

Read only the assigned brief and its permitted context. The graph was
read at its authority preamble and relevant nodes `GC-target`, `M9-M1`,
`M9-M2`, and `GC-complete-square-root-large-values-moment-bound`.
No paths mentioned merely as historical dependencies in those files
were opened.

| Artifact | SHA-256 at inspection |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71` |
| `state/active_campaign.yml` | `ce8b5f11dd052674895e2e3b6fa4a0c2ec63486a93d49826b34959531abb82cf` |
| `strategy/round212_complete_four_point_attack.md` | `dc38c727ec4853784081aa35a42facd683a80b6edef39e6e3b7d48f80db3d468` |
| `strategy/gauss_circle_strategy_checkpoint_round211_2026-09-28.md` | `09806113079e70cd5863c315a9595524eac4270de6afa1f0c2b97e02c7f674f8` |
| `rounds/codex-managed/gc-full-source-method-review/controls/conductor_two_stage_strategy.md` | `9bf8f30d240304f88c46a5a93c7d93586b3ade1c674d5a5fdbc61a251fcd176f` |
| `rounds/codex-managed/gc-full-source-method-review/reviews/independent_two_stage_review.md` | `052c3362897ae5185eee0a7afed6242164b3fa0ae6c89edcef90466c5d2adca5` |
| `rounds/codex-managed/gc-signed-near-frequency-cancellation/reports/actual_shifted_correlations.md` | `657fb00457c9ed8fabf4b3d3ffe71b26fdbeff85e767c35a94ff279aec248168` |
| `rounds/codex-managed/gc-signed-near-frequency-cancellation/reviews/independent_shifted_correlations_review.md` | `05960367004f155b22232dbe09bbe74ad11c1834df1196d99aa7f4330d117516` |

The assigned brief is
`rounds/codex-managed/gc-complete-four-point-correlation/briefs/four_point_oscillatory_attack.md`.
The two-stage ledger and review supply (37), its conventions and
conditional reconstruction scope. The round210 files identify the
outer-absolute CRT and one-step Abel closures that were not to be
repeated. The new mass proof and radius-Gram certificate calculation
are elementary derivations given in full here; no external theorem,
web source, computation or unlisted artifact is imported.

The conductor received the safe-sector prices, the shellwise dispersion
criterion and the actual residual-mass/Gram obstruction as they were
derived. The conductor separately described an intended small-product
lower-bound argument; it is not used here. The distinct proof above
establishes absolute mass after removing those small products.

## 7. Recommended state effect

**Retain**, after independent review, the complete safe-sector estimates,
the precisely costed sufficient shell-dispersion interface, and the
actual-coefficient no-go for the positive radius-Gram certificate (7).
**No change** to the accepted arithmetic target, exponent, moment bound,
proof draft or M1/M2 parents. Do not promote (16) or (19), and do not
relabel (34) as a lower bound for A4 or the circle discrepancy.

Only this task's assigned report is written. Shared state, validation
matrices, synthesis, proof drafts, blind and sibling files, immutable
legacy evidence and successor artifacts are untouched. This task stops
after the report and awaits any conductor-directed same-round seam.
