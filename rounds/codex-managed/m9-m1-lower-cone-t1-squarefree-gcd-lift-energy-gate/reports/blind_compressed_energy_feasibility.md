# Round 149 statement-only blind report: compressed energy feasibility

- Campaign: m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate
- Task: blind_compressed_energy_feasibility
- Role: statement-only blind rederiver
- Graph hash carried by the brief: 8f1912eeda4843718379213478a839b30fb2694d6b169ac8decbab5ca3561176
- Status: candidate evidence only

## 1. Result: exact compression, safe diagonal, and the first method-specific no-go

Let \(d_{\mathrm o}=d/(d,2)\). The lcm-cell coefficient collapses exactly to

\[
C_d(n)=
\begin{cases}
 \mu(u)\mu(v),&
 n=uv^2,\quad u\mid d_{\mathrm o},\quad
 \mu^2(uv)=1,\quad (v,d_{\mathrm o})=1,\\
 0,&\text{otherwise}.
\end{cases}
\tag{1.1}
\]

In particular, an odd prime \(p\mid d_{\mathrm o}\) occurring to the
second power in \(n\) gives zero. The prime \(2\) contributes no lcm
factor.

After inserting the exact finite nonempty-progression indicator
\(\kappa_{d,U}(n)\), and only then collecting all common gcd lifts
\(\ell=gL,\ q=gq_0\), the exact row is

\[
G_U(d)=
\sum_{\substack{L,q_0\geq1\ {\rm odd}\\(L,q_0)=1}}
 \chi_4(Lq_0)\frac{B_{d,U}(L)}{L}
 W_{d,U}(L/q_0)e(NdL/q_0),
\tag{1.2}
\]

where \(q_0\asymp LQ\) and

\[
B_{d,U}(L)=
\sum_{g\geq1\ {\rm odd}}
\frac{C_d(gL)\kappa_{d,U}(gL)}{g}.
\tag{1.3}
\]

For every finite prefix, without cancellation in that prefix,

\[
\sum_{L\geq1\ {\rm odd}}\frac{|B_{d,U}(L)|^2}{L}
\ll_\varepsilon d^\varepsilon,
\qquad
\sum_{L\geq1\ {\rm odd}}\frac{|B_{d,U}(L)|}{L}
\ll_\varepsilon d^\varepsilon.
\tag{1.4}
\]

Consequently, under the profile normalization
\(\|W_{d,U}\|_\infty\ll X^\varepsilon\) needed for the proposed
diagonal estimate, the literal equal-cell diagonal is

\[
\mathcal E_{\rm diag}
\ll_\varepsilon DQX^\varepsilon
\ll_\varepsilon R^2D X^\varepsilon.
\tag{1.5}
\]

Distinct reduced fractions never belong to this literal diagonal.
Exact \(N\)-dependent alignments can also be priced by a divisor
argument and (1.4): if the finite progression support is polynomial
in \(X\), their total absolute contribution is
\(\ll_\varepsilon DX^\varepsilon\).

The complete joint energy is **not proved by the compression and norm
alone**. The first genuinely open step is an off-diagonal correlation
estimate with the actual coefficient
\(B_{d,U}(L)W_{d,U}(L/q_0)\), which depends on \(d\) through prime
divisibility, the exact prefix, and the profile. A classical large
sieve with one \(d\)-independent coefficient vector therefore does
not apply verbatim.

This obstruction is already decisive at \(D=1\): there are only
\(O(1)\) rows, so joint \(d\)-energy supplies no averaging and asks
directly for square-root cancellation in a \(q_0\)-sum of length as
large as \(Q\asymp R^2\). The lift norm (1.4) does not provide that
cancellation.

This is a method-specific no-go, not a lower bound for the signed
scalar. It does not say that the target energy is false. It says that
the implication

\[
\text{compressed lift norm + literal diagonal}
\Longrightarrow
\sum_d\mu^2(d)|G_U(d)|^2
\ll R^2D X^\varepsilon
\]

has an unfilled premise: a signed variable-coefficient
near-collision/generic correlation theorem using the actual
\(\chi_4\), profile, and prefix.

## 2. Exact statement and hypotheses

Let \(\mathscr A_{d,U}\) be the finite set of integers in the specified
clipped amplitude. The exact progression indicator is

\[
\kappa_{d,U}(n)
=\mathbf 1_{\{n\mathbb N\cap\mathscr A_{d,U}\ne\varnothing\}}.
\tag{2.1}
\]

If the clipped amplitude is the integer interval \(A<e\leq B\), this
is equivalently

\[
\kappa_{d,U}(n)
=\mathbf 1_{\{\lfloor B/n\rfloor-\lfloor A/n\rfloor\geq1\}}.
\tag{2.2}
\]

Formula (2.2), not a continuous surrogate, is the endpoint cutoff.
The derivation uses only that \(\kappa\in\{0,1\}\) and has finite
support. Put

\[
K_{d,U}
=\max\bigl(1,\{n:\kappa_{d,U}(n)=1\}\bigr).
\tag{2.3}
\]

The identities (1.1)--(1.3) and norms (1.4) need no quantitative
bound on \(K_{d,U}\). An \(X^\varepsilon\) divisor price for exact
alignments uses the natural additional condition
\(K_{d,U}\leq X^A\) for some fixed \(A\). The frozen statement says
only that the support is finite, so this must be checked from the
actual clipped amplitude rather than silently assumed.

Likewise, smoothness and support do not by themselves normalize
\(W\): scaling a smooth supported function preserves those
properties. Thus (1.5) and the estimates involving \(W\) use the
explicit necessary normalization
\(\|W_{d,U}\|_\infty\ll X^\varepsilon\). Derivative or variation
bounds needed off the diagonal are not supplied and are not assumed.

For a reduced cell \(x=(L,q_0)\), set

\[
A_d(x)
=\chi_4(Lq_0)\frac{B_{d,U}(L)}{L}W_{d,U}(L/q_0),
\qquad
\theta_x=\frac{NL}{q_0}.
\tag{2.4}
\]

The still-needed estimate is the exact variable-row inequality

\[
\sum_{d\asymp D}\mu^2(d)
\left|\sum_x A_d(x)e(d\theta_x)\right|^2
\ll_\varepsilon R^2D X^\varepsilon.
\tag{2.5}
\]

No arbitrary-sign replacement of \(A_d(x)\) is made below.

## 3. Proof and derivation

### 3.1 Odd-prime cells, \(p\mid d\) cancellation, and \(p=2\)

For an odd prime \(p\), let \(j=v_p(n)\). Since \(\alpha,b\) are
squarefree, \(v_p(\alpha^2)\in\{0,2\}\) and
\(v_p(b)\in\{0,1\}\). The local sums are

| prime case | \(j=0\) | \(j=1\) | \(j=2\) |
|---|---:|---:|---:|
| \(p\nmid d_{\mathrm o}\) | \(1\) | \(0\) | \(-1\) |
| \(p\mid d_{\mathrm o}\) | \(1\) | \(-1\) | \((-1)+(+1)=0\) |

For \(p\mid d_{\mathrm o}\) and \(j=2\), the first term has
\(p\mid\alpha,\ p\nmid b\), while the second has
\(p\mid\alpha,\ p\mid b\). Their signs cancel. Multiplication of the
local factors proves (1.1).

Since \(\alpha,b,n\) are odd, \(p=2\) is absent from every lcm cell.
Whether \(2\mid d\) changes neither \(C_d(n)\) nor the gcd-lift
ledger; it remains present in the outer phase and in any full-\(d\)
dependence of \(\kappa\) and \(W\).

Membership depends only on \(d,n=[\alpha^2,b]\) and the nonempty
progression condition, so grouping equal lcms gives exactly

\[
\sum_{\substack{(\alpha,b)\in\mathcal P(d)\\[\alpha^2,b]=n}}
\mu(\alpha)\mu(b)
=C_d(n)\kappa_{d,U}(n).
\tag{3.1}
\]

### 3.2 Gcd-lift recombination

For every odd \((\ell,q)\), write

\[
g=(\ell,q),\qquad
\ell=gL,\qquad q=gq_0,\qquad (L,q_0)=1.
\]

Then

\[
\chi_4(\ell)\chi_4(q)
=\chi_4(g)^2\chi_4(Lq_0)
=\chi_4(Lq_0),
\tag{3.2}
\]

and

\[
\frac{Nd\ell}{q}=\frac{NdL}{q_0},\qquad
W_{d,U}(\ell/q)=W_{d,U}(L/q_0),\qquad
\frac1\ell=\frac1{gL}.
\tag{3.3}
\]

Also \(q\asymp\ell Q\) is equivalent to \(q_0\asymp LQ\).
Summing all \(g\) proves (1.2)--(1.3). Thus the character, phase, and
ratio profile are constant on a gcd-lift class; \(C_d(gL)\), the exact
prefix, and \(1/g\) are precisely the residual lift dependence.

### 3.3 Closed formula for the truncated lift

If \(B_{d,U}(L)\ne0\), then \(L\) is cube-free. Write uniquely

\[
L=ts^2,\qquad t,s\ \text{squarefree},\qquad (t,s)=1.
\tag{3.4}
\]

For the fixed row \(d\), put

\[
a=(t,d_{\mathrm o}),\qquad r=t/a.
\tag{3.5}
\]

Necessarily \((s,d_{\mathrm o})=1\); otherwise a prime of
\(d_{\mathrm o}\) is squared in every \(gL\), and the local
cancellation makes \(B_{d,U}(L)=0\). When
\((s,d_{\mathrm o})=1\), every nonzero term \(n=gL=uv^2\) is uniquely
of the form

\[
u=au',\quad u'\mid d_{\mathrm o}/a,\qquad
v=rsv',\quad
\mu^2(v')=1,\quad (v',d_{\mathrm o}rs)=1,
\tag{3.6}
\]

and

\[
n=au'(rsv')^2,\qquad g=u'r(v')^2.
\tag{3.7}
\]

Therefore

\[
\boxed{
B_{d,U}(ts^2)
=\frac{\mu(a)\mu(r)\mu(s)}{r}
\sum_{u'\mid d_{\mathrm o}/a}\frac{\mu(u')}{u'}
\sum_{\substack{v'\geq1\ {\rm odd}\\
                  \mu^2(v')=1\\
                  (v',d_{\mathrm o}rs)=1}}
\frac{\mu(v')}{(v')^2}
\kappa_{d,U}\!\left(au'(rsv')^2\right).
}
\tag{3.8}
\]

The prefix in (3.8) couples \(u'\) and \(v'\), so this is generally
not an Euler product. Replacing the finite indicator by an infinite
or continuous cutoff would change the coefficient.

### 3.4 Uniform square norm and auxiliary weighted \(\ell^1\) norm

Taking absolute values only after the exact lift sum has been formed,
(3.8) gives

\[
|B_{d,U}(ts^2)|
\leq
\frac{C}{r}
\prod_{p\mid d_{\mathrm o}}\left(1+\frac1p\right)
\ll_\varepsilon \frac{d^\varepsilon}{r}.
\tag{3.9}
\]

The absolute \(v'\)-sum is bounded by
\(\prod_{p\ {\rm odd}}(1+p^{-2})<\infty\), uniformly in every prefix.
Summing (3.9) over \(L=ars^2\), and dropping coprimality restrictions,
gives

\[
\begin{aligned}
\sum_L\frac{|B_{d,U}(L)|^2}{L}
&\ll_\varepsilon d^\varepsilon
\sum_{a\mid d_{\mathrm o}}\frac1a
\sum_{r\geq1}\frac1{r^3}
\sum_{s\geq1}\frac1{s^2}
\ll_\varepsilon d^\varepsilon,\\
\sum_L\frac{|B_{d,U}(L)|}{L}
&\ll_\varepsilon d^\varepsilon
\sum_{a\mid d_{\mathrm o}}\frac1a
\sum_{r\geq1}\frac1{r^2}
\sum_{s\geq1}\frac1{s^2}
\ll_\varepsilon d^\varepsilon.
\end{aligned}
\tag{3.10}
\]

This proves (1.4), including \(L=1\), \(D=1\), even \(d\), and every
short or irregular prefix. If \(L\leq K\), the same decomposition
also gives the weaker absolute capacity

\[
\sum_{L\leq K}|B_{d,U}(L)|
\ll_\varepsilon d^\varepsilon K^{1/2+\varepsilon}.
\tag{3.11}
\]

### 3.5 Literal diagonal and all-aspect power ledger

For each \(L\), there are \(O(LQ)\) odd \(q_0\asymp LQ\). Hence

\[
\begin{aligned}
\mathcal E_{\rm diag}
&=\sum_{d\asymp D}\mu^2(d)
  \sum_{(L,q_0)=1}|A_d(L,q_0)|^2\\
&\ll_\varepsilon
QX^\varepsilon
\sum_{d\asymp D}\mu^2(d)
\sum_L\frac{|B_{d,U}(L)|^2}{L}
\ll_\varepsilon DQX^\varepsilon.
\end{aligned}
\tag{3.12}
\]

This counts all odd reduced denominators, not squarefree denominators;
no squarefree \(Q+D\) large-sieve bound is used.

Write

\[
M=D^2\lambda^2,\qquad 1\leq\lambda\ll R/D.
\tag{3.13}
\]

Since \(N\asymp X=R^4\) and \(DE\asymp M\),

\[
E\asymp D\lambda^2,\qquad
Q\asymp\frac{R^2}{\lambda},\qquad
RD\ll Q\ll R^2.
\tag{3.14}
\]

Thus

\[
DQ\asymp\frac{R^2D}{\lambda}\leq R^2D.
\tag{3.15}
\]

At \(M\asymp D^2\), the diagonal saturates the target up to constants.
At \(M\asymp R^2\), it has slack factor \(R/D\). This covers every
allowed \(M,D,E,Q\).

After compression, a full absolute-value estimate using (3.11) gives
only

\[
\sum_d|G_U(d)|^2
\ll_\varepsilon DQ^2K^{1+\varepsilon},
\qquad
K=\max_{d\asymp D}K_{d,U}.
\tag{3.16}
\]

Thus the small strict range \(Q^2K\ll R^2\) is settled without
off-diagonal cancellation. In the natural large ranges this fails.
Equation (3.16) is only an adverse upper capacity, not a lower bound
for the signed scalar.

### 3.6 Determinant, exact alignments, common divisors, and near collisions

For two reduced cells \(x_i=(L_i,q_i)\), put

\[
\Delta=L_1q_2-L_2q_1.
\tag{3.17}
\]

Their off-diagonal phase is

\[
e\!\left(Nd\frac{\Delta}{q_1q_2}\right).
\tag{3.18}
\]

Reducedness implies that \(\Delta=0\) only for identical cells.

To retain common divisors and imprimitive difference denominators,
write

\[
H=(q_1,q_2),\qquad
q_1=HA,\qquad q_2=HB,\qquad (A,B)=1,
\tag{3.19}
\]

and

\[
\delta=L_1B-L_2A,\qquad \Delta=H\delta.
\tag{3.20}
\]

Individual reduction gives

\[
(\delta,A)=(\delta,B)=1.
\tag{3.21}
\]

Split a squarefree row as \(d=\eta m\), where
\(\eta\in\{1,2\}\) and \(m\) is odd. The difference phase is

\[
e\!\left(m\frac{\eta N\delta}{HAB}\right).
\tag{3.22}
\]

An exact alignment on either parity subfamily satisfies

\[
HAB\mid\eta N\delta.
\tag{3.23}
\]

Since \(HAB\) is odd, this is equivalent to \(HAB\mid N\delta\).
By (3.21),

\[
AB\mid N,\qquad
H\mid\frac{N}{AB}\delta.
\tag{3.24}
\]

If \(\delta=0\), coprimality gives \(A\mid L_1\) and
\(B\mid L_2\); reducedness then forces \(A=B=1\), so the cells are
identical. For a distinct pair \(\delta\ne0\), the number of exactly
aligned \((q_1,q_2)\) for fixed \(L_1,L_2\) is at most

\[
\sum_{AB\mid N}
\tau\!\left(\left|\frac{N}{AB}\delta\right|\right)
\ll_\varepsilon (N|\delta|)^\varepsilon.
\tag{3.25}
\]

Support only reduces this count. Combining (3.25) with the second
norm in (3.10) gives

\[
\mathcal E_{\rm exact,off}
\ll_\varepsilon D(NKQ)^\varepsilon
\tag{3.26}
\]

when \(L_i\leq K\). Exact alignments are therefore target-safe when
the actual amplitude gives \(K\leq X^{O(1)}\). This permits arbitrary
powers and common factors in \(q_i\); the denominators were not
treated as squarefree.

The special family \(q_0\mid N\) is simpler: its phase is \(1\) for
both odd and even \(d\), and

\[
\left|
\sum_L\frac{B_{d,U}(L)}L
\sum_{\substack{q_0\mid N\\q_0\asymp LQ}}
\chi_4(Lq_0)W_{d,U}(L/q_0)
\right|
\ll_\varepsilon
X^\varepsilon\sum_L\frac{|B_{d,U}(L)|}{L}
\ll_\varepsilon X^\varepsilon.
\tag{3.27}
\]

Thus \(q_0\mid N\), including \(L=1\), is not the unresolved exact
alignment family.

Near collisions on parity-\(\eta\) rows are exactly the solutions of

\[
0<
\left\|\frac{\eta N\delta}{HAB}\right\|
\ll\frac1D,
\tag{3.28}
\]

or, for some integer \(k\),

\[
0<|\eta N\delta-kHAB|
\ll\frac{HAB}{D}.
\tag{3.29}
\]

Unlike (3.23), this does not force \(AB\mid N\) or make \(H\) a
divisor of a fixed nonzero integer. The generic off-diagonal is the
complement

\[
\left\|\frac{\eta N\delta}{HAB}\right\|
\gg\frac1D.
\tag{3.30}
\]

Equations (3.17)--(3.30) retain the determinant, exact and near
congruences, common denominator \(H\), residual coprime denominators
\(A,B\), parity, and imprimitive denominators.

### 3.7 Why the joint energy remains open

Expanding the energy gives the exact off-diagonal

\[
\sum_{x_1\ne x_2}
\sum_{d\asymp D}\mu^2(d)
A_d(x_1)\overline{A_d(x_2)}
e\!\left(Nd\frac{\Delta}{q_1q_2}\right).
\tag{3.31}
\]

The coefficient in the inner \(d\)-sum is not fixed. Formula (3.8)
shows this explicitly. If a prime occurs to the first power in \(L\),
then for \(p\mid d_{\mathrm o}\) it lies in \(a\), with no mandatory
\(1/p\) lift loss, while for \(p\nmid d\) it lies in \(r\), and (3.8)
has the mandatory \(1/p\). Primes of \(d_{\mathrm o}\) not in \(L\)
also enter the \(u'\)-sum. The exact \(\kappa_{d,U}\) couples these
divisors to \(v'\), and \(W_{d,U}\) has further row dependence.

Thus a Dirichlet-kernel or classical large-sieve bound for

\[
\sum_d e\!\left(Nd\frac{\Delta}{q_1q_2}\right)
\]

cannot simply be inserted into (3.31). Even the outer \(\mu^2(d)\)
requires a squarefree-row treatment.

At \(D=1\) there are only \(O(1)\) rows. For \(L=1\),

\[
B_{d,U}(1)
=
\sum_{u'\mid d_{\mathrm o}}\frac{\mu(u')}{u'}
\sum_{\substack{v'\ {\rm odd\ squarefree}\\(v',d_{\mathrm o})=1}}
\frac{\mu(v')}{(v')^2}
\kappa_{d,U}(u'(v')^2),
\tag{3.32}
\]

and the \(L=1\) part of the row is

\[
B_{d,U}(1)
\sum_{q_0\asymp Q}
\chi_4(q_0)W_{d,U}(1/q_0)e(Nd/q_0).
\tag{3.33}
\]

At \(D\asymp M\asymp1\), \(Q\asymp R^2\). The diagonal of (3.33) is
of target size \(R^2\), but (2.5) asks for the signed sum to be
\(O(RX^\varepsilon)\). No \(d\)-average creates this cancellation.
It must come from the actual \(\chi_4(q_0)\), reciprocal phase, and
profile. Neither (1.4) nor reduced-fraction counting supplies it.

Taking moduli in (3.31) would discard precisely that structure and
offer only the adverse capacity (3.16), making no distinction from
an unsigned or adversarial analogue. The first missing lemma must
therefore be a signed estimate for (3.28)--(3.30), valid with the
exact \(d\)-dependent coefficient and every prefix, whose \(D=1\)
case contains a direct bound for (3.33).

If (2.5) were proved, Cauchy--Schwarz and \(d\asymp D\) would give

\[
|\mathcal T|
\ll
D^{1/2}
\left(\sum_d\mu^2(d)|G_U(d)|^2\right)^{1/2}
\ll_\varepsilon RDX^\varepsilon.
\tag{3.34}
\]

Thus the target energy has the correct normalization; its
off-diagonal premise is the unresolved part.

## 4. First doubtful or unproved step

The first genuinely unproved step is the exact correlation bound,
split over \(d=\eta m\), \(\eta\in\{1,2\}\):

\[
\begin{aligned}
&\sum_{\eta=1,2}
\sum_{\substack{m\asymp D/\eta\\m\ {\rm odd\ squarefree}}}
\sum_{x_1\ne x_2}
A_{\eta m}(x_1)\overline{A_{\eta m}(x_2)}
e\!\left(m\frac{\eta N\delta}{HAB}\right)\\
&\hspace{42mm}
\ll_\varepsilon R^2D X^\varepsilon,
\end{aligned}
\tag{4.1}
\]

with both the near range (3.28) and generic range (3.30). The exact
alignment subrange is controlled by (3.26).

Three inputs needed for (4.1) are absent from the frozen statement:

1. quantitative size and derivative/variation bounds for the actual
   radial-cone-prefix profile \(W_{d,U}\);
2. a polynomial support bound and \(d\)-variation rule for the exact
   endpoint indicator \(\kappa_{d,U}\);
3. a variable-coefficient correlation theorem preserving
   \(\chi_4(Lq_0)\) and (3.8), rather than freezing or majorizing them
   by arbitrary signs.

The compulsory endpoint test for any such lemma is (3.33) at \(D=1\).
If it cannot prove that one-row estimate, averaging over \(d\) cannot
repair the gap.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| exact_progression_coefficient_collapse | **Pass.** Equation (1.1), with exact indicator (2.1), is the complete lcm collapse. |
| p_divides_d_square_local_cancellation | **Pass.** The \(p\mid d_{\mathrm o},p^2\mid n\) local cell is \(-1+1=0\). |
| absent \(p=2\) factor and even \(d\) | **Pass.** \(C_d=C_{d_{\mathrm o}}\); parity remains in phase, prefix, and profile. Exact odd-denominator alignments are unchanged, while near conditions retain \(\eta=2\). |
| finite_nonempty_progression_prefix_indicator | **Pass for compression and norms.** Equations (2.1)--(2.2) retain the floor cutoff. Polynomial support and variation needed analytically are not stated. |
| gcd_lift_character_phase_profile_recombination | **Pass.** Equations (3.2)--(3.3) show \(\chi_4(g)^2=1\) and display every remaining \(g\)-dependence in \(B\). |
| truncated_lift_square_norm | **Pass.** Equation (3.10) is uniform in every finite prefix; the auxiliary weighted \(\ell^1\) norm also holds. |
| joint_d_energy_target_normalization | **Pass as a sufficient normalization; open as an estimate.** Equation (3.34) gives the scalar target from (2.5). |
| literal_equal_cell_diagonal | **Pass.** It costs \(DQX^\varepsilon\), not a conjectural squarefree \(Q+D\) term, and is safe since \(Q\ll R^2\). |
| offdiagonal_determinant_and_near_collision | **Classification pass; estimate open.** Equations (3.17), (3.28), and (3.29) retain the determinant and near congruence. |
| N_dependent_exact_alignments | **Pass subject to polynomial progression support.** Equations (3.24)--(3.26) give the divisor price. |
| common_divisor_and_imprimitive_denominator | **Pass.** Equations (3.19)--(3.24) retain \(H,A,B\) and nonsquarefree denominators. |
| d_dependent_arithmetic_coefficient | **Obstruction identified.** Formula (3.8) proves row dependence; no fixed-vector large sieve applies verbatim. |
| all_M_D_E_Q_power_ledger | **Pass for diagonal and absolute strict range.** Equations (3.13)--(3.16) cover balanced and extreme aspects; the near/generic complement remains open. |
| D1_L1_qdividesN_prime_and_prefix_controls | **Pass/obstruction separated.** \(q_0\mid N\) is safe by (3.27); \(D=1,L=1\) isolates (3.33); prime and prefix cases are explicit in (3.8), (3.32). |
| actual-sign control | **Pass.** No arbitrary bounded signs were substituted. Modulus was taken only after exact gcd-lift compression, and adverse capacities were not read as lower bounds. |
| Round138_cross_tge2_and_downstream_scope | **Pass.** This report treats only the displayed compressed \(t=1\) scalar. It makes no claim about the independent cross owner, any \(t\geq2\) layer, or downstream assembly. |

## 6. Dependencies and exact artifacts used

Only the following were read:

1. protocol.md;
2. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/blind_statement.md, including the corrected even-\(d\) statement;
3. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/briefs/blind_compressed_energy_feasibility.md.

No graph file, proof draft, strategy file, Round-138--149 nonblind
artifact, sibling report, web source, or computation was used.

## 7. Recommended state effect

**Retain/revise; do not promote the joint energy.** Retain as candidate
lemmas the odd-prime collapse (1.1), exact gcd-lift compression
(1.2)--(1.3), closed coefficient formula (3.8), uniform norms (1.4),
literal diagonal (1.5), and exact-alignment classification and price
(3.24)--(3.27). Revise the mechanism so that its next owner must prove
the signed variable-\(d\) near/generic correlation (4.1), with the
\(D=1,L=1\) row (3.33) as a compulsory entry test and explicit
profile/prefix hypotheses. Until then, make no state change to the
full joint energy, scalar target, independent cross term, any
\(t\geq2\) layer, or downstream claim.
