# Round 149 conductor candidate: gcd-lift compression and the variable-row energy boundary

- Campaign: \`m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate\`
- Round: 149
- Role: conductor-selected proof kernel
- Starting graph SHA-256: \`8f1912eeda4843718379213478a839b30fb2694d6b169ac8decbab5ca3561176\`
- Allocation: 100% analytic, algebraic, and source verification; 0% numerical

## 1. Result and exact scope

Retain the Round-148 notation

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq\sqrt M,\qquad
 Q=2\sqrt{ND/E}\ll R^2.
\tag{149.C1}
$$

For squarefree \(d\), put \(d_{\mathrm o}=d/(d,2)\).  The complete
Möbius sum over pairs with the same lcm has the exact coefficient

$$
 C_d(n)=
 \begin{cases}
  \mu(u)\mu(v),&
  n=uv^2,\quad u\mid d_{\mathrm o},\quad
  u,v\ {\rm odd},\quad \mu^2(uv)=1,\quad (v,d)=1,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{149.C2}
$$

Let \(\kappa_{d,U}(n)\) be the literal indicator that the progression
\(e\in n\mathbb N\) meets the inherited clipped amplitude.  It is
finite, may contain floor discontinuities, and is not replaced below
by a continuous cutoff.  After also collecting all common gcd lifts
\(\ell=gL,\ q=gq_0\), the Round-148 scalar is exactly

$$
 \mathcal T_{D,E,U}
 =\sum_{d\asymp D}\mu^2(d)\frac Dd\,G_U(d),
\tag{149.C3}
$$

where

$$
\boxed{
 G_U(d)=
 \sum_{\substack{L,q_0\geq1\ {\rm odd}\\(L,q_0)=1}}
 \chi_4(Lq_0)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q_0)
 e(NdL/q_0),\qquad q_0\asymp LQ,
}
\tag{149.C4}
$$

and

$$
\boxed{
 B_{d,U}(L)=
 \sum_{\substack{g\geq1\\g\ {\rm odd}}}
 \frac{C_d(gL)\kappa_{d,U}(gL)}g .
}
\tag{149.C5}
$$

The exact prefix causes no loss in the two norms

$$
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 +\sum_L\frac{|B_{d,U}(L)|}{L}
 \ll_\varepsilon X^\varepsilon.
\tag{149.C6}
$$

Consequently the literal equal-cell diagonal in
\(\sum_d|G_U(d)|^2\) is \(O_\varepsilon(DQX^\varepsilon)\), hence
target-safe.  Every distinct exact \(N\)-dependent phase alignment is
also target-safe by an imprimitive-denominator divisor classification.
Thus Round 149 removes both the old progression-cell diagonal loss and
the exact-alignment seam.

The complete joint energy

$$
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \stackrel{?}{\ll_\varepsilon}R^2D X^\varepsilon
\tag{149.C7}
$$

is nevertheless not proved.  Its first remaining term is the signed
near/generic determinant correlation with the actual row-dependent
coefficient \(B_{d,U}(L)\mathscr W_{d,U}(L/q_0)\).  A fixed-vector
rational large sieve cannot be inserted at that point, and taking
absolute values discards the compulsory \(\chi_4\) and reciprocal
phase cancellation.  The terminal disposition is therefore a scoped
\(\mathsf{gcd\_lift\_energy\_no\_go}\): the compression and its
positive diagonal do not imply (149.C7) without a new variable-row
signed correlation theorem.  This is not a lower bound for
\(\mathcal T_{D,E,U}\) and not an impossibility result for a different
signed organization.

## 2. Exact lcm coefficient

For an odd prime \(p\), write
\(a=v_p(\alpha)\in\{0,1\}\) and
\(\beta=v_p(b)\in\{0,1\}\), with \(\beta=0\) when
\(p\nmid d_{\mathrm o}\).  The exponent of \(p\) in
\([\alpha^2,b]\) is \(\max(2a,\beta)\).  The local signed ledger is

| prime case | exponent \(0\) | exponent \(1\) | exponent \(2\) |
|---|---:|---:|---:|
| \(p\nmid d_{\mathrm o}\) | \(1\) | \(0\) | \(-1\) |
| \(p\mid d_{\mathrm o}\) | \(1\) | \(-1\) | \(-1+1=0\) |

The last entry is the cancellation between
\((a,\beta)=(1,0)\) and \((1,1)\).  Multiplying the local factors
gives (149.C2): exponent-one primes form \(u\mid d_{\mathrm o}\),
and exponent-two primes form \(v\) coprime to \(d\).  Since
\(\alpha,b\), and \(n\) are odd, \(p=2\) contributes no lcm factor,
even when \(2\mid d\).

Membership in the exact Round-148 pair set depends on
\((\alpha,b)\) only through \(d\), \(n=[\alpha^2,b]\), and whether
the \(n\)-progression meets the amplitude.  Hence

$$
 \sum_{\substack{(\alpha,b)\in\mathcal P(d)\\
                 [\alpha^2,b]=n}}
 \mu(\alpha)\mu(b)
 =C_d(n)\kappa_{d,U}(n).
\tag{149.C8}
$$

For an interval component \(A_d<e\leq B_d\), the cutoff is literally

$$
 {\bf1}_{\{\lfloor B_d/n\rfloor-\lfloor A_d/n\rfloor\geq1\}},
\tag{149.C9}
$$

with the analogous finite union for the actual clipped amplitude.
In the present application its support satisfies
\(n\ll E\ll X^{1/2}\).

## 3. Exact gcd-lift identity

For every odd pair \((\ell,q)\), set

$$
 g=(\ell,q),\qquad \ell=gL,\qquad q=gq_0,\qquad (L,q_0)=1.
\tag{149.C10}
$$

Then

$$
 \chi_4(\ell)\chi_4(q)
 =\chi_4(g)^2\chi_4(Lq_0)=\chi_4(Lq_0),
\tag{149.C11}
$$

while

$$
 \frac{Nd\ell}{q}=\frac{NdL}{q_0},\qquad
 \mathscr W_{d,\ell,U}(q)
 =\mathscr W_{d,U}(L/q_0),\qquad
 \frac1\ell=\frac1{gL}.
\tag{149.C12}
$$

The saddle support \(q\asymp\ell Q\) is equivalent to
\(q_0\asymp LQ\).  Summing the remaining finite \(g\)-dependence in
(149.C12) proves (149.C3)--(149.C5).  No convergence exchange is
needed.

There is also a useful closed description.  If
\(L=ts^2\), with \(t,s\) squarefree and \((t,s)=1\), put

$$
 a=(t,d_{\mathrm o}),\qquad r=t/a.
\tag{149.C13}
$$

When \((s,d_{\mathrm o})>1\), \(B_{d,U}(L)=0\).  Otherwise every
nonzero lift is uniquely

$$
 u=au',\qquad v=rsv',\qquad
 u'\mid d_{\mathrm o}/a,\qquad
 \mu^2(v')=1,\qquad (v',d_{\mathrm o}rs)=1,
\tag{149.C14}
$$

and \(g=u'r(v')^2\).  Therefore

$$
\boxed{
 B_{d,U}(ts^2)
 =\frac{\mu(a)\mu(r)\mu(s)}r
 \sum_{u'\mid d_{\mathrm o}/a}\frac{\mu(u')}{u'}
 \sum_{\substack{v'\geq1\ {\rm odd}\\
                  \mu^2(v')=1\\(v',d_{\mathrm o}rs)=1}}
 \frac{\mu(v')}{(v')^2}
 \kappa_{d,U}\!\left(au'(rsv')^2\right).
}
\tag{149.C15}
$$

The cutoff couples \(u'\) and \(v'\), so (149.C15) is not generally
an Euler product.  This is the first explicit source of row
dependence.

## 4. Prefix-uniform norms and the literal diagonal

Taking absolute values in (149.C15), but not before the exact
compression, gives

$$
 |B_{d,U}(ts^2)|
 \ll_\varepsilon \frac{X^\varepsilon}{r}.
\tag{149.C16}
$$

Indeed, the \(v'\)-sum is bounded by
\(\prod_{p\ {\rm odd}}(1+p^{-2})\), and the \(u'\)-sum is at most
\(\prod_{p\mid d_{\mathrm o}}(1+p^{-1})\ll_\varepsilon X^\varepsilon\).
Since \(L=ars^2\), dropping coprimality restrictions gives

$$
\begin{aligned}
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 &\ll_\varepsilon X^\varepsilon
 \sum_{a\mid d_{\mathrm o}}\frac1a
 \sum_{r\geq1}\frac1{r^3}
 \sum_{s\geq1}\frac1{s^2}
 \ll_\varepsilon X^\varepsilon,\\
 \sum_L\frac{|B_{d,U}(L)|}{L}
 &\ll_\varepsilon X^\varepsilon
 \sum_{a\mid d_{\mathrm o}}\frac1a
 \sum_{r\geq1}\frac1{r^2}
 \sum_{s\geq1}\frac1{s^2}
 \ll_\varepsilon X^\varepsilon.
\end{aligned}
\tag{149.C17}
$$

These bounds are uniform for arbitrary \(0\)-\(1\) finite prefixes.
The additional finite-support estimates

$$
 \sum_L|B_{d,U}(L)|+\sum_L|B_{d,U}(L)|^2
 \ll_\varepsilon \sqrt E\,X^\varepsilon
\tag{149.C18}
$$

follow in the same way from \(L\ll E\).

The accepted profile is uniformly bounded.  Since there are
\(O(LQ)\) admissible \(q_0\) for each \(L\), the literal diagonal is

$$
\begin{aligned}
 \mathscr E_{\rm diag}
 &\ll_\varepsilon
 \sum_{d\asymp D}\sum_L
 \frac{|B_{d,U}(L)|^2}{L^2}(LQ)X^\varepsilon\\
 &\ll_\varepsilon DQX^\varepsilon
 \ll_\varepsilon R^2D X^\varepsilon.
\end{aligned}
\tag{149.C19}
$$

This proves that exact pre-Cauchy compression removes the factor-\(R\)
positive-diagonal loss found in Round 148.

## 5. Exact alignments are target-safe

For two reduced cells \(x_i=(L_i,q_i)\), define

$$
 \Delta=L_1q_2-L_2q_1.
\tag{149.C20}
$$

The difference phase is
\(e(Nd\Delta/(q_1q_2))\).  Literal equality \(\Delta=0\) forces
\((L_1,q_1)=(L_2,q_2)\), already counted in (149.C19).

For a distinct exact \(N\)-alignment, write

$$
 H=(q_1,q_2),\qquad q_1=HA,\qquad q_2=HB,\qquad
 (A,B)=1,
\tag{149.C21}
$$

and put

$$
 \delta=L_1B-L_2A,\qquad \Delta=H\delta.
\tag{149.C22}
$$

Individual reducedness gives
\((\delta,A)=(\delta,B)=1\).  Exact alignment is

$$
 q_1q_2\mid N\Delta
 \quad\Longleftrightarrow\quad
 HAB\mid N\delta.
\tag{149.C23}
$$

It follows that

$$
 AB\mid N,\qquad H\mid\frac{N}{AB}\delta.
\tag{149.C24}
$$

For fixed \(L_1,L_2,A,B\), the nonzero integer \(\delta\) is fixed.
The choices of the coprime pair \(A,B\) with \(AB\mid N\), followed
by the choices of \(H\), have divisor multiplicity
\(O_\varepsilon(X^\varepsilon)\), since
\(L_i,q_i,N\ll X^{O(1)}\).  Thus the number of exactly aligned
\((q_1,q_2)\) for fixed \(L_1,L_2\) is
\(O_\varepsilon(X^\varepsilon)\).  Equations (149.C17) and the
bounded profile then give

$$
 \mathscr E_{\rm exact,off}
 \ll_\varepsilon
 D X^\varepsilon
 \left(\sum_L\frac{|B_{d,U}(L)|}{L}\right)^2
 \ll_\varepsilon D X^\varepsilon.
\tag{149.C25}
$$

The notation in the middle expression suppresses the harmless
row-wise maximum furnished by (149.C17).  The proof permits arbitrary
prime powers and common factors in \(q_1,q_2\), and works for odd and
even squarefree \(d\): writing \(d=\eta m\), \(\eta\in\{1,2\}\),
does not change exact alignment because \(q_1q_2\) is odd.

The special stratum \(q_0\mid N\) is even simpler.  Its entire row is

$$
 O_\varepsilon\!\left(
 \tau(N)\sum_L\frac{|B_{d,U}(L)|}{L}\right)
 =O_\varepsilon(X^\varepsilon).
\tag{149.C26}
$$

Hence neither imprimitive exact alignments nor the zero reduced
frequency is the open seam.

## 6. The first remaining energy seam

With (149.C19) and (149.C25) removed, the exact expansion still
contains

$$
\sum_{x_1\ne x_2}
\sum_{d\asymp D}\mu^2(d)
A_d(x_1)\overline{A_d(x_2)}
e\!\left(Nd\frac{\Delta}{q_1q_2}\right),
\tag{149.C27}
$$

where

$$
 A_d(L,q_0)=
 \chi_4(Lq_0)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q_0).
\tag{149.C28}
$$

After (149.C21)--(149.C22), the near range on
\(d=\eta m\), \(\eta\in\{1,2\}\), is

$$
 0<
 \left\|\frac{\eta N\delta}{HAB}\right\|
 \ll\frac1D,
\qquad\text{equivalently}\qquad
 0<|\eta N\delta-kHAB|
 \ll\frac{HAB}{D}
\tag{149.C29}
$$

for some integer \(k\); the generic range is its complement.
Unlike exact alignment, (149.C29) does not imply \(AB\mid N\) or
make \(H\) divide one fixed nonzero integer.

The coefficient in the inner \(d\)-sum is genuinely row-dependent.
Formula (149.C15) changes when primes enter \(d_{\mathrm o}\), and
the floor cutoff \(\kappa_{d,U}\) and saddle profile carry additional
\(d\)-dependence.  Therefore the classical rational large sieve,
whose quadratic form uses one coefficient vector sampled over its
outer points, does not apply verbatim to (149.C27).  Expanding
squarefreeness and taking absolute values reintroduces a positive
capacity and does not preserve the actual signed cancellation.

The entry test is visible at \(D=1,L=1\):

$$
 B_{d,U}(1)
 \sum_{q_0\asymp Q}
 \chi_4(q_0)\mathscr W_{d,U}(1/q_0)e(Nd/q_0).
\tag{149.C30}
$$

For scale diagnosis only, suppose additionally that the sampled
profile in (149.C30) has total variation \(O_\varepsilon(X^\varepsilon)\)
on each of the two odd residue classes.  The weighted
second-derivative lemma would then give

$$
 \ll_\varepsilon
 (NM)^{1/4}+N^{1/4}M^{-3/4}.
\tag{149.C30a}
$$

This is \(O_\varepsilon(RX^\varepsilon)\) when \(M\asymp1\), but its
first term is \(RM^{1/4}\) in general; the corresponding formal dual
derivative range has length \(\asymp M\) and returns a square-root
phase.  Neither the coefficient norm nor boundedness of the profile
proves the required variation hypothesis, so (149.C30a) is not used
as an unconditional estimate here.  It only shows that the all-scale
\(D=1\) entry test and the transform-self-return persist beyond the
bottom scale.  This is a diagnostic, not a signed lower bound.

Accordingly, the first missing theorem is the literal variable-row
near/generic bound

$$
\begin{aligned}
 \sum_{\eta=1,2}
 \sum_{\substack{m\asymp D/\eta\\m\ {\rm odd\ squarefree}}}
 \sum_{\substack{x_1\ne x_2\\\text{nonexact}}}
 A_{\eta m}(x_1)\overline{A_{\eta m}(x_2)}
 e\!\left(m\frac{\eta N\delta}{HAB}\right)
 \ll_\varepsilon R^2D X^\varepsilon,
\end{aligned}
\tag{149.C31}
$$

uniformly for every \(M,D,E,Q\) and every exact prefix.  No accepted
artifact or audited source currently proves (149.C31).

The control conclusions are:

1. lcm collapse, the \(p\mid d_{\mathrm o}\) square cancellation,
   absent \(p=2\) factor, gcd-lift identity, prefix-uniform norms,
   target normalization, literal diagonal, exact alignments, common
   divisors, imprimitive denominators, \(q_0\mid N\), parity, and all
   \(M,D,E,Q\) diagonal powers pass;
2. near collisions and the generic determinant range are classified
   but not estimated;
3. the actual-sign falsifier passes: no arbitrary outer signs are
   substituted, and an adverse positive capacity is not read as a
   lower bound;
4. the Round-138 cross owner, every \(t\geq2\) layer, lower GAR,
   M9--M1, M9--M2, endpoint uniformity, M9, the conditional bridge,
   the quarter target, and the global exponent remain outside this
   result.

## 7. Dependencies and recommended state effect

The proof kernel uses the accepted Round-148 reciprocal transform and
its exact prefix support, together with the Round-149 blind
rederivation and the source/claimant reports named in the campaign
manifest.  The direct prime-local, divisor, and norm computations in
(149.C2)--(149.C26) are reproduced here.

Subject to seam review, promote:

1. the exact lcm and gcd-lift compression (149.C2)--(149.C15);
2. the prefix-uniform coefficient norms and target-safe literal
   diagonal (149.C16)--(149.C19); and
3. the imprimitive exact-alignment divisor bound
   (149.C20)--(149.C26).

Create or revise an obstruction node stating precisely that those
facts do not imply the variable-row near/generic energy (149.C31), and
that the audited fixed-vector large-sieve and transform-self-return
routes do not fill it.  Retain (149.C7), the signed scalar target,
every downstream obligation, and the exponent as open.
