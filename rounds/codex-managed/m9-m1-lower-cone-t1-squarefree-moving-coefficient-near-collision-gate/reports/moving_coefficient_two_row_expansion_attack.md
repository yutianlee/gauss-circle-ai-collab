# Round 150 discovery report: exact two-row incidence expansion and the target-safe \(k=0\) collar

- Campaign: `m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate`
- Round: 150
- Task: `moving_coefficient_two_row_expansion_attack`
- Role: discovery
- Starting graph SHA-256: `b6c5ee5b0d51d347876b389c05c78596c069b190af715d297bd937701ea893b6`
- Allocation: 100% analytic and algebraic; 0% numerical
- Terminal label: `strict_moving_coefficient_collar_range`

## 1. Result: exact row linearization and an owner-complete \(k=0\) collar

Put

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq \sqrt M,
 \qquad Q=2\sqrt{ND/E}.
\tag{150.1}
\]

The literal product of the two moving gcd-lift coefficients has an
exact divisor-incidence expansion.  If \(d=\eta m\), where
\(\eta\in\{1,2\}\) and \(m=d_{\mathrm o}\) is odd squarefree, and
\(L_i=t_i s_i^2\), then after choosing \(a_i\mid t_i\), putting
\(c_i=t_i/a_i\), and expanding the accepted \(u_i,v_i\) sums, all
purely arithmetic dependence on \(m\) is

\[
 {\bf1}_{F\mid m}{\bf1}_{(m,P)=1}
 ={\bf1}_{(F,P)=1}\sum_{z\mid P}\mu(z){\bf1}_{Fz\mid m},
\tag{150.2}
\]

where

\[
 F=[a_1u_1,a_2u_2],\qquad
 P=\operatorname{rad}(c_1c_2s_1s_2v_1v_2).
\tag{150.3}
\]

The coefficient-side projective norm of this incidence expansion is
\(O_\varepsilon(X^\varepsilon)\) for each fixed \((L_1,L_2)\), on
the literal finite support.  This is a genuine two-row
linearization, not an arbitrary-matrix replacement.  The two exact
prefix values and the two sampled profiles remain joint functions of
\((m,L_i,q_i,u_i,v_i)\); they are displayed below and are not called
smooth, separable, or of bounded variation.

The first new estimate is the following strict, owner-complete range.
For two reduced cells write

\[
 q_i=hr_i,\qquad (r_1,r_2)=1,\qquad
 \delta=L_1r_2-L_2r_1,
\tag{150.4}
\]

and choose the unique centered integer \(k\) such that

\[
 \rho=N\delta-khr_1r_2,\qquad
 |\rho|\leq \frac{hr_1r_2}{2}.
\tag{150.5}
\]

Then the complete coefficient-weighted absolute mass of the nonexact
\(k=0\) collar

\[
 k=0,\qquad 0<|\rho|\leq \frac{hr_1r_2}{D}
\tag{150.6}
\]

satisfies

\[
 \boxed{\mathcal A_{0,U}\ll_\varepsilon DQX^\varepsilon
 \ll_\varepsilon R^2DX^\varepsilon.}
\tag{150.7}
\]

This is stronger than the required estimate for the absolute value of
the signed \(k=0\) contribution.  It is uniform in every clipped
prefix, both profiles, even and odd squarefree \(d\), common factors,
imprimitive denominators, \(q_i\mid N\), small reduced denominators,
and every allowed \(M,D,E,Q\).  It uses neither the mod-four sign nor
oscillation in \(d\).

In fact the same target-safe estimate holds for every *fixed* centered
wrap integer \(k\).  More generally, if \(\mathcal K\) is any set of
wrap integers with

\[
 |\mathcal K|\ll 1+\frac{R^2}{Q}
 \asymp 1+\frac{\sqrt M}{D},
\tag{150.7a}
\]

then the coefficient-weighted absolute mass of all collar pairs whose
centered \(k\) lies in \(\mathcal K\) is

\[
 \boxed{\mathcal A_{\mathcal K,U}
 \ll_\varepsilon R^2DX^\varepsilon.}
\tag{150.7b}
\]

Thus the symmetric small-wrap range \(|k|\leq K_0\) is owned whenever
\(K_0+1\ll1+\sqrt M/D\).  The \(k=0\) result (150.7) remains the
cleanest single-class corollary.

There is a second strict edge range.  If \(M\) is bounded by an
absolute constant, and hence \(D,E\) and the number of supported
\(L\)'s are bounded, the explicit sampled Round-148 cutoff has uniform
\(q\)-total variation.  The weighted second-derivative estimate then
gives

\[
 |G_U(d)|\ll_\varepsilon RX^\varepsilon,
 \qquad
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll_\varepsilon R^2DX^\varepsilon.
\tag{150.7c}
\]

This owns the entire bottom-scale row, hence both its collar and its
generic part.  It does not extend to growing \(M\), where the same
second-derivative placement has the known \(RM^{1/4}\) first term.

The shifted-factor identity is correct:

\[
 \boxed{
 (NL_1-khr_1)(NL_2+khr_2)
 =N^2L_1L_2+kh\rho.}
\tag{150.8}
\]

For \(k\ne0\), its two factors are nonzero and in fact positive on
the collar for sufficiently large \(X\).  For fixed
\((L_1,L_2,h,k,\rho)\), it gives at most \(X^\varepsilon\) candidate
pairs \((r_1,r_2)\).  However, summing this divisor bound separately
over every legal \(h,k,\rho\) gives the adverse raw capacity

\[
 \ll_\varepsilon
 \frac{NL_1L_2Q}{D}X^\varepsilon,
\tag{150.9}
\]

which is worse than the trivial \(O(L_1L_2Q^2)\) pair capacity by

\[
 \frac{N}{DQ}\asymp \frac{R^2\sqrt M}{D^2}\gg R.
\tag{150.10}
\]

Thus a fixed-shift divisor bound, followed by absolute summation of
all shifts, cannot close the growing-\(M\), large-wrap remainder.
Equation (150.9) is an adverse upper capacity for that proof placement,
not a signed lower bound.  The wrap classes outside the target-safe
packet (150.7a) are isolated below as the next exact seam.  The full
collar target is not proved.

## 2. Exact statement and hypotheses

All variables \(L,q,h,r\) below are positive and odd.  The notation
\(q\asymp LQ\) means the fixed two-sided support inherited from the
Round-148 saddle profile; its constants are independent of every
dyadic parameter.  Every cell satisfies

\[
 (L,q)=1,\qquad q\asymp LQ,
\tag{150.11}
\]

and \(B_{d,U}(L)=0\) unless \(L\ll E\) is odd and cube-free.  Define

\[
 A_d(L,q)=
 \chi_4(Lq)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q).
\tag{150.12}
\]

For a pair of cells let \(h=(q_1,q_2)\), put \(q_i=hr_i\), and use
(150.4)--(150.5).  Since all relevant integers are odd, the centered
integer has no tie: an equality
\(2N\delta=(2k+1)hr_1r_2\) would equate an even integer with an odd
integer.

The complete literal nonzero collar contribution is

\[
\begin{aligned}
 \mathcal C_{\mathrm{col},U}
 ={}&\sum_{d\asymp D}\mu^2(d)
 \sum_{\substack{L_i,q_i\ \mathrm{odd}\
                  (L_i,q_i)=1,\ q_i\asymp L_iQ\\
                  0<|\rho|\leq hr_1r_2/D}}
 \chi_4(L_1L_2r_1r_2)
 \frac{B_{d,U}(L_1)\overline{B_{d,U}(L_2)}}{L_1L_2}\\
 &\qquad\qquad\times
 \mathscr W_{d,U}(L_1/q_1)
 \overline{\mathscr W_{d,U}(L_2/q_2)}
 e\!\left(\frac{d\rho}{hr_1r_2}\right).
\end{aligned}
\tag{150.13}
\]

Indeed,

\[
 \chi_4(L_1q_1)\overline{\chi_4(L_2q_2)}
 =\chi_4(L_1L_2h^2r_1r_2)
 =\chi_4(L_1L_2r_1r_2),
\tag{150.14}
\]

and subtracting the integer \(k\) from the difference phase gives the
last factor in (150.13).  Thus the mod-four sign is present literally;
it is not inserted after taking absolute values.

Let \(\mathcal C_{0,U}\) denote the part of (150.13) with \(k=0\),
and define its coefficient-weighted absolute mass by

\[
\begin{aligned}
 \mathcal A_{0,U}:={}&
 \sum_{d\asymp D}\mu^2(d)
 \sum_{\substack{L_i,q_i\ \mathrm{as\ in}\ (150.13)\\
                  k=0}}
 \frac{|B_{d,U}(L_1)B_{d,U}(L_2)|}{L_1L_2}
 \left|\mathscr W_{d,U}(L_1/q_1)
       \mathscr W_{d,U}(L_2/q_2)\right|.
\end{aligned}
\tag{150.15}
\]

The theorem proved here is (150.7), hence
\(|\mathcal C_{0,U}|\leq\mathcal A_{0,U}\).  The only analytic
inputs used for it are the accepted uniform bounds

\[
 \|\mathscr W_{d,U}\|_\infty\ll1,
 \qquad
 \sum_L|B_{d,U}(L)|\ll_\varepsilon \sqrt E\,X^\varepsilon,
\tag{150.16}
\]

and the exact support (150.11).  Consequently no unrecorded
regularity hypothesis enters (150.7).

## 3. Proof and derivation

### 3.1 Literal one-row and two-row coefficient expansion

Write a squarefree \(d\) uniquely as

\[
 d=\eta m,\qquad \eta\in\{1,2\},\qquad
 m=d_{\mathrm o}\ \text{odd and squarefree}.
\tag{150.17}
\]

Let \(L=ts^2\), where \(t,s\) are odd squarefree and
\((t,s)=1\).  Expanding the condition \(a=(t,m)\) in the accepted
closed formula gives the exact identity

\[
\begin{aligned}
 B_{\eta m,U}(ts^2)
 ={}&\sum_{a\mid t}\frac{\mu(a)\mu(c)\mu(s)}c
 \sum_{u\geq1}\frac{\mu(u)}u
 \sum_{\substack{v\geq1\ \mathrm{odd\ squarefree}\\
                  (v,cs)=1}}
 \frac{\mu(v)}{v^2}\\
 &\quad\times
 {\bf1}_{au\mid m}{\bf1}_{(m,csv)=1}
 \kappa_{\eta m,U}\!\left(au(csv)^2\right),
 \qquad c=t/a.
\end{aligned}
\tag{150.18}
\]

If \(L\) has no such cube-free representation, the left side is
zero.  To check (150.18), for a nonzero summand the two masks imply
\(a\mid m\) and \((c,m)=1\).  Since \(t=ac\) is squarefree, this
forces \(a=(t,m)\).  The same masks give \(u\mid m/a\),
\((s,m)=1\), and \((v,mcs)=1\), exactly the accepted closed formula.
Conversely every term in that formula occurs once in (150.18).

Apply (150.18) to both \(L_i=t_is_i^2\).  For chosen
\(a_i\mid t_i\), put

\[
 c_i=t_i/a_i,\qquad
 n_i=a_iu_i(c_is_iv_i)^2,
\tag{150.19}
\]

and retain the fixed restrictions that \(v_i\) is odd squarefree and
\((v_i,c_is_i)=1\).  Define

\[
 \beta_i=
 \frac{\mu(a_i)\mu(c_i)\mu(s_i)\mu(u_i)\mu(v_i)}
      {c_iu_iv_i^2},
\tag{150.20}
\]

and \(F,P\) by (150.3).  The exact product is

\[
\begin{aligned}
 B_{\eta m,U}(L_1)\overline{B_{\eta m,U}(L_2)}
 ={}&\sum_{\substack{a_i\mid t_i,\ u_i\geq1\\
                       v_i\ \mathrm{odd\ squarefree}\\
                       (v_i,c_is_i)=1}}
 \beta_1\beta_2\,
 {\bf1}_{F\mid m}{\bf1}_{(m,P)=1}\\
 &\qquad\times
 \kappa_{\eta m,U}(n_1)\kappa_{\eta m,U}(n_2).
\end{aligned}
\tag{150.21}
\]

All quantities in (150.21) are real, so the bar on the second \(B\)
does not change its expansion.  The compatibility
\((F,P)=1\) is compulsory: if it fails, no \(m\) can satisfy the two
masks.  If it holds, ordinary Mobius inversion gives exactly

\[
 {\bf1}_{F\mid m}{\bf1}_{(m,P)=1}
 ={\bf1}_{(F,P)=1}\sum_{z\mid P}\mu(z){\bf1}_{Fz\mid m},
\tag{150.22}
\]

which proves (150.2).  This retains primes shared between the two
rows: overlaps among \(a_1u_1\) and \(a_2u_2\) enter the lcm \(F\),
while a prime forced into one row and excluded by the other makes
\((F,P)>1\) and kills the term.  No independence between the rows has
been assumed.

There is a quantitative norm.  On a nonzero prefix term,
\(n_i\ll E\).  The sums over \(u_i\), with weights \(1/u_i\), are
logarithmic; the sums over \(v_i\), even after the cost
\(\tau(P)\), converge because

\[
 \sum_{v\geq1}\frac{\mu^2(v)\tau(v)^C}{v^2}<\infty
\tag{150.23}
\]

for every fixed \(C\).  Also

\[
 \sum_{a\mid t}\frac1{t/a}
 =\sum_{c\mid t}\frac1c\ll_\varepsilon X^\varepsilon.
\tag{150.24}
\]

It follows that, for fixed \((L_1,L_2)\), the sum of the absolute
coefficients \(|\beta_1\beta_2\mu(z)|\) in
(150.21)--(150.22), restricted to the literal finite support, is
\(O_\varepsilon(X^\varepsilon)\).  This is the promised low-
projective-norm divisor-incidence layer.  It does not remove the two
following joint factors.

### 3.2 Exact prefix and sampled-profile dependence on \(d\)

Let \(\mathscr A_{D,E,U}(d,e)\) be the accepted compact amplitude.
The prefix is, literally,

\[
 \kappa_{d,U}(n)
 ={\bf1}_{\{\exists j\geq1:\
       \mathscr A_{D,E,U}(d,nj)\ne0\}}.
\tag{150.25}
\]

For a half-open support component \(A_{d,U}<e\leq B_{d,U}\), its
contribution is the exact floor-existence condition

\[
 {\bf1}_{\{\lfloor B_{d,U}/n\rfloor-
                 \lfloor A_{d,U}/n\rfloor\geq1\}},
\tag{150.26}
\]

with the finite union of actual components used in (150.25).  The
endpoints inherit \(M/d\), \(U/d\), the dyadic \(e\)-shell, the cone
boundary \(4d\), and the peeled collars.  Thus (150.26) is a joint
floor function of \((d,n)\), not a continuous cutoff in \(n\).
Even when an endpoint is monotone, its floor can change
\(O(1+E/n)\) times across \(d\asymp D\).  Boundedness of
\(\kappa\) therefore supplies no prefix-uniform \(O(1)\) variation
statement.

The sampled profile is exactly

\[
 \mathscr W_{d,U}(L/q)
 =\mathscr A_{D,E,U}\!\left(
       d,\frac{4NdL^2}{q^2}\right).
\tag{150.27}
\]

Writing \(e_0=4NdL^2/q^2\) exposes the dependence of every named
Round-148 factor:

\[
 de_0=\frac{4Nd^2L^2}{q^2},\qquad
 \frac{e_0}{4d}=\frac{NL^2}{q^2}.
\tag{150.28}
\]

Hence the sampled \(e\)-dyadic factor is a function of \(d\), while
the lower-radial and hard product-prefix factors are functions of
\(d^2\); for example the latter is

\[
 {\bf1}_{\{M\leq4Nd^2L^2/q^2<U\}}.
\tag{150.29}
\]

By contrast, the sampled cone condition \(e_0>4d\) is exactly
\(q^2<NL^2\), independent of \(d\).  These observations identify the
true dependence, but no derivative or variation bound for the full
assembled profile is inferred merely from its accepted boundedness.

After (150.22), the complete remaining row atom is

\[
\begin{aligned}
 &\mu^2(\eta m){\bf1}_{Fz\mid m}
 \kappa_{\eta m,U}(n_1)\kappa_{\eta m,U}(n_2)\\
 &\qquad\times
 \mathscr W_{\eta m,U}(L_1/q_1)
 \overline{\mathscr W_{\eta m,U}(L_2/q_2)}.
\end{aligned}
\tag{150.30}
\]

It is still joint in the outer row and both cells.  Equations
(150.25)--(150.30) are the precise stopping point of the arithmetic
incidence linearization.  The \(k=0\) estimate below is uniform in
this atom and therefore does not require a further rank claim.

### 3.3 Determinant count for the complete \(k=0\) collar

Fix \(d,L_1,L_2,h\), and put

\[
 g_L=(L_1,L_2).
\tag{150.31}
\]

The support \(q_i=hr_i\asymp L_iQ\) places \(r_i\) in intervals of
length \(O(L_iQ/h)\).  When \(k=0\), one has
\(\rho=N\delta\).  Thus the nonzero collar gives

\[
 0<|\delta|leq \frac{hr_1r_2}{ND}
 \ll \frac{L_1L_2Q^2}{hND}
 =\frac{4L_1L_2}{hE}.
\tag{150.32}
\]

Every value of \(\delta=L_1r_2-L_2r_1\) is a multiple of \(g_L\).
Consequently the number of possible nonzero \(\delta\)'s in
(150.32) is

\[
 \ll \frac{L_1L_2}{g_LhE};
\tag{150.33}
\]

when the right side is below the first permitted multiple, the count
is zero.  For a fixed permitted \(\delta\), divide the equation by
\(g_L\).  Since \(L_1/g_L\) and \(L_2/g_L\) are coprime, all integer
solutions are obtained from one solution by

\[
 r_1\longmapsto r_1+(L_1/g_L)t,\qquad
 r_2\longmapsto r_2+(L_2/g_L)t.
\tag{150.34}
\]

Intersecting (150.34) with the two support intervals leaves

\[
 O\!\left(1+\frac{g_LQ}{h}\right)
\tag{150.35}
\]

solutions.  Dropping \((r_1,r_2)=1\), the two reducedness
conditions, oddness, and the requirement that \(h\) be the exact gcd
can only enlarge this count.  Combining (150.33)--(150.35), the raw
number of \(k=0\) collar pairs for fixed \((L_1,L_2,h)\) is

\[
 \mathcal N_0(L_1,L_2;h)
 \ll
 \frac{L_1L_2}{g_LhE}
 +\frac{L_1L_2Q}{h^2E}.
\tag{150.36}
\]

This is a raw tuple count.  It has not yet been confused with either
the coefficient-weighted mass or the signed contribution.  Sum
(150.36) over all positive \(h\) (a harmless enlargement of the odd,
support-limited set).  Using \(\sum_{h\leq X^{O(1)}}h^{-1}ll
X^\varepsilon\) and \(\sum h^{-2}\ll1\), then (150.16), gives for
one row \(d\)

\[
\begin{aligned}
 \mathcal A_{0,U}(d)
 &\ll_\varepsilon
 \sum_{L_1,L_2}
 \frac{|B_{d,U}(L_1)B_{d,U}(L_2)|}{L_1L_2}
 \left(
   \frac{L_1L_2}{g_LE}
  +\frac{L_1L_2Q}{E}
 \right)X^\varepsilon\\
 &\ll_\varepsilon
 \frac{1+Q}{E}
 \left(\sum_L|B_{d,U}(L)|\right)^2X^\varepsilon
 \ll_\varepsilon QX^\varepsilon.
\end{aligned}
\tag{150.37}
\]

The profile bound has been absorbed here.  Summing (150.37) over the
\(O(D)\) squarefree rows, including \(d=2m\), proves

\[
 \mathcal A_{0,U}\ll_\varepsilon DQX^\varepsilon.
\tag{150.38}
\]

Finally,

\[
 \frac{Q}{R^2}\asymp\frac{D}{\sqrt M}\leq1,
\tag{150.39}
\]

so (150.38) proves (150.7).  The proof includes all \(L_i\), all
common divisors \(h\), and every nonzero \(\delta\) in the \(k=0\)
collar.  Exact \(\delta=0\) is excluded and remains with the accepted
exact-phase owner.

### 3.4 Shifted-factor audit for \(k\ne0\)

Expanding the left side of (150.8) gives

\[
\begin{aligned}
 &(NL_1-khr_1)(NL_2+khr_2)\\
 &\quad=N^2L_1L_2+Nkh(L_1r_2-L_2r_1)-k^2h^2r_1r_2\\
 &\quad=N^2L_1L_2+kh(N\delta-khr_1r_2),
\end{aligned}
\tag{150.40}
\]

which is (150.8), with the stated signs.  There are also the useful
exact relations

\[
\begin{aligned}
 r_2(NL_1-khr_1)&=NL_2r_1+\rho,\\
 r_1(NL_2+khr_2)&=NL_1r_2-\rho.
\end{aligned}
\tag{150.41}
\]

They prove all required integrality congruences.  On the collar,

\[
 \frac{|\rho|}{NL_2r_1}
 \leq\frac{q_2}{DNL_2}
 \ll\frac{Q}{DN}\ll1,
\tag{150.42}
\]

and similarly with the indices reversed.  Hence both factors in
(150.8) are positive for sufficiently large \(X\), uniformly in all
allowed aspects.  In particular neither factor, and therefore not
the right side of (150.8), can vanish in the nonzero collar.  This
also covers the potentially exceptional family \(q_i\mid N\): if,
for example, \(NL_1=kq_1\), then (150.41) would force
\(|\rho|=NL_2r_1\), contradicting (150.42).

For \(k\ne0\), fix \((L_1,L_2,h,k,\rho)\) and put

\[
 T=N^2L_1L_2+kh\rho.
\tag{150.43}
\]

Every admissible pair gives a positive factorization \(AB=T\), with

\[
 A=NL_1-khr_1,\qquad B=NL_2+khr_2.
\tag{150.44}
\]

Conversely a factor pair determines at most one candidate through

\[
 r_1=\frac{NL_1-A}{kh},\qquad
 r_2=\frac{B-NL_2}{kh}.
\tag{150.45}
\]

The positivity, divisibility, support, oddness, coprimality, and
reducedness tests only remove candidates.  Since \(T\leq X^{O(1)}\),
the number of candidates for fixed data is therefore

\[
 \ll\tau(T)\ll_\varepsilon X^\varepsilon.
\tag{150.46}
\]

This fixed-shift statement is lawful, but it is not a complete collar
estimate.  The support gives the full parameter ledger

\[
\begin{aligned}
 h&\ll \min(L_1,L_2)Q,\qquad
 r_i\asymp L_iQ/h,\\
 H:=hr_1r_2&\asymp L_1L_2Q^2/h,\\
 |\delta|&\ll L_1L_2Q/h,\\
 |k|&\ll N/Q,\\
 0<|\rho|&\ll L_1L_2Q^2/(hD).
\end{aligned}
\tag{150.47}
\]

Here \(N/Q\gg1\), so the harmless centered \(1/2\) is absorbed in
the fourth line.  Applying (150.46) independently and then summing
all legal shifts yields, for fixed \((L_1,L_2)\),

\[
\begin{aligned}
 \sum_h\sum_{0<|k|\ll N/Q}
 \sum_{0<|\rho|\ll L_1L_2Q^2/(hD)}\tau(T)
 \ll_\varepsilon
 \frac{NL_1L_2Q}{D}X^\varepsilon.
\end{aligned}
\tag{150.48}
\]

By contrast, forgetting the collar leaves only
\(O(L_1L_2Q^2)\) pairs of denominators.  The ratio of the bound in
(150.48) to that trivial capacity is

\[
 \frac{N}{DQ}
 \asymp\frac{R^2\sqrt M}{D^2}
 \geq\frac{R^2}{\sqrt M}\geq R.
\tag{150.49}
\]

Thus separate divisor bounds for fixed \((h,k,\rho)\) lose before
any coefficient weight is used.  If one nevertheless multiplies
(150.48) by the trivial \(D/(L_1L_2)\) row-kernel bound and uses
\(\sum_L|B_d(L)|\ll\sqrt E X^\varepsilon\), the resulting formal
absolute capacity is \(NQEX^\varepsilon\), worse than simply reverting
to the accepted full-row triangle capacity.  No adverse quantity here
is a lower bound for (150.13).  A successful use of (150.8) must
retain cancellation jointly across factors, shifts, the mod-four
sign, and the exact atom (150.30).

For \(k=0\), (150.8) degenerates to
\((NL_1)(NL_2)=N^2L_1L_2\) and contains no \((r_1,r_2)\)
information.  This is why the determinant argument
(150.32)--(150.37), rather than divisor switching, was necessary.

### 3.5 Every fixed wrap and a target-safe small-wrap packet

The determinant argument admits a stronger organization that is
uniform in a fixed \(k\).  Fix \((L_1,L_2,h,k)\) and first fix
\(r_1\).  Put

\[
 S=NL_1-khr_1,\qquad \alpha=hr_1/D.
\tag{150.55}
\]

The collar inequality is exactly

\[
 |Sr_2-NL_2r_1|\leq \alpha r_2.
\tag{150.56}
\]

For every supported solution, (150.41)--(150.42) and
\(r_1/r_2\asymp L_1/L_2\) give

\[
 S\asymp NL_1,
 \qquad
 \frac{\alpha}{S}\ll\frac{Q}{DN}\ll1.
\tag{150.57}
\]

In particular \(S>2\alpha\) for sufficiently large \(X\).  Solving
(150.56) for \(r_2\) confines it to

\[
 \frac{NL_2r_1}{S+\alpha}
 \leq r_2\leq
 \frac{NL_2r_1}{S-\alpha}.
\tag{150.58}
\]

The length of this interval is

\[
 \frac{2NL_2r_1\alpha}{S^2-\alpha^2}
 \ll \frac{L_2Q^2}{hDN}
 =\frac{4L_2}{hE}\ll1,
\tag{150.59}
\]

because \(L_2\ll E\).  Thus each supported \(r_1\) permits
\(O(1)\) values of \(r_2\).  There are
\(O(L_1Q/h)\) supported values of \(r_1\).  Interchanging the two
indices gives the symmetric estimate, and hence the raw fixed-wrap
count

\[
 \mathcal N_k(L_1,L_2;h)
 \ll \frac{Q\min(L_1,L_2)}h.
\tag{150.60}
\]

All oddness, exact-gcd, coprimality, reducedness, and prefix/profile
conditions were again dropped only to enlarge this upper count.

The accepted closed coefficient formula also implies the useful norm

\[
 \boxed{
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}
 \ll_\varepsilon X^\varepsilon.}
\tag{150.61}
\]

Indeed, write \(L=acs^2\), where \(a=(t,d_{\mathrm o})\),
\(c=t/a\), and use \(|B_{d,U}(L)|\ll X^\varepsilon/c\).  Dropping
coprimality conditions and retaining \(L\ll E\) gives

\[
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}
 \ll_\varepsilon X^\varepsilon
 \sum_{a\mid d_{\mathrm o}}a^{-1/2}
 \sum_{c\geq1}c^{-3/2}
 \sum_{s\leq \sqrt E}s^{-1}
 \ll_\varepsilon X^\varepsilon.
\tag{150.62}
\]

The last divisor product is \(X^{o(1)}\), uniformly in squarefree
\(d\).  Since

\[
 \frac1{\max(L_1,L_2)}\leq\frac1{\sqrt{L_1L_2}},
\tag{150.63}
\]

(150.60), the bounded profile, and the harmonic \(h\)-sum give, for
every fixed \(k\) and every fixed row \(d\),

\[
\begin{aligned}
 \mathcal A_{k,U}(d)
 &\ll_\varepsilon QX^\varepsilon
 \sum_{L_1,L_2}
 \frac{|B_{d,U}(L_1)B_{d,U}(L_2)|}
      {\max(L_1,L_2)}\\
 &\ll_\varepsilon QX^\varepsilon
 \left(\sum_L\frac{|B_{d,U}(L)|}{\sqrt L}\right)^2
 \ll_\varepsilon QX^\varepsilon.
\end{aligned}
\tag{150.64}
\]

After summing \(d\), each fixed wrap costs \(DQX^\varepsilon\).
Summing (150.64) over a set \(\mathcal K\) satisfying (150.7a)
costs

\[
 DQ\left(1+\frac{R^2}{Q}\right)X^\varepsilon
 \ll_\varepsilon R^2DX^\varepsilon,
\tag{150.65}
\]

because \(Q\ll R^2\).  This proves (150.7b).  The full centered wrap
range has size \(\asymp N/Q\), which is larger than the owned packet
by a factor of order \(N/R^2\asymp R^2\).  Thus (150.65) is strict
and does not silently cover all \(k\ne0\).

### 3.6 The bounded-\(M\) full-row edge

Assume \(M\leq M_0\) for a fixed absolute constant \(M_0\).  Then
\(D,E\asymp1\), \(L\ll E\) leaves only \(O(1)\) values of \(L\),
and \(Q\asymp R^2\).  Put \(q=LQy\) on the fixed compact saddle
support.  The exact sampled point is

\[
 e_0=\frac{4NdL^2}{q^2}
 =\frac{dE}{D}\,y^{-2}.
\tag{150.66}
\]

Thus every smooth dyadic or radial factor in the accepted profile is
a fixed-scale smooth function of \(y\).  The product prefix is a
single half-open interval condition in \(y^{-2}\), and the sampled
cone is a single threshold by (150.28).  The peeled collar factors
have the bounded derivative scales recorded in the Round-148
remainder ledger; when \(M,D\asymp1\), those scales are \(O(1)\).
Consequently, on each odd residue class, the literal function

\[
 q\longmapsto \mathscr W_{d,U}(L/q)
\tag{150.67}
\]

has total variation \(O_\varepsilon(X^\varepsilon)\), uniformly in
the half-open prefix.  The finitely many hard boundaries contribute
only finitely many jumps.

On a fixed residue class modulo four, set \(f(q)=NdL/q\).  Throughout
\(q\asymp LQ\),

\[
 |f''(q)|\asymp \frac{NdL}{(LQ)^3}
 \asymp R^{-2},
\tag{150.68}
\]

because \(d,L\asymp1\) and \(Q\asymp R^2\).  The standard
second-derivative estimate, uniformly on every subinterval, is

\[
 \sum_{q\in I}e(f(q))
 \ll |I|\,|f''|^{1/2}+|f''|^{-1/2}
 \ll R.
\tag{150.69}
\]

Partial summation using (150.67), separately on the two odd residue
classes where \(\chi_4\) is constant, yields

\[
 \sum_{q\asymp LQ\atop q\ \mathrm{odd}}
 \chi_4(q)\mathscr W_{d,U}(L/q)e(NdL/q)
 \ll_\varepsilon RX^\varepsilon.
\tag{150.70}
\]

Finally the accepted weighted \(\ell^1\) norm gives

\[
 |G_U(d)|
 \ll_\varepsilon RX^\varepsilon
 \sum_L\frac{|B_{d,U}(L)|}{L}
 \ll_\varepsilon RX^\varepsilon.
\tag{150.71}
\]

There are \(O(D)\) rows, proving (150.7c).  For growing \(M\), the
same second-derivative ledger produces the previously recorded
\(RM^{1/4}\) first term and is not target-sized; no such extension is
claimed.

## 4. First doubtful or unproved step

Choose a target-safe wrap packet \(\mathcal K\) satisfying (150.7a)
and containing zero.  After the exact expansion (150.21)--(150.30),
the packet estimate (150.65), and the bounded-\(M\) edge (150.71), the
first unproved step at growing \(M\) is the signed large-wrap collar
sum

\[
\begin{aligned}
 \sum_{\eta=1,2}
 \sum_{\substack{m\ \mathrm{odd\ squarefree}\\
                  \eta m\asymp D}}
 \sum_{\substack{L_i,q_i\ \mathrm{as\ in}\ (150.13)\\
                  k\notin\mathcal K,\ 0<|\rho|\leq H/D}}
 &\chi_4(L_1L_2r_1r_2)e(\eta m\rho/H)\\
 \times\sum_{\mathbf a,\mathbf u,\mathbf v,z}
 &\beta_1\beta_2\mu(z){\bf1}_{(F,P)=1}{\bf1}_{Fz\mid m}\\
 \times{}&\kappa_{\eta m,U}(n_1)\kappa_{\eta m,U}(n_2)
 \mathscr W_{\eta m,U}(L_1/q_1)
 \overline{\mathscr W_{\eta m,U}(L_2/q_2)},
\end{aligned}
\tag{150.50}
\]

with the outer factor \(1/(L_1L_2)\) understood.  In the collar the
phase changes by only \(O(1)\) across a length-\(D\) row, so a bare
geometric sum gives no saving.  The incidence expansion has small
coefficient norm, but its two floor prefixes and two sampled profiles
remain joint row-cell functions.  The shifted identity gives the
fixed-shift divisor count (150.46), but (150.48)--(150.49) prove that
separately summing those counts is not a target-sized route.

What remains necessary is a genuinely joint signed shifted-divisor or
matrix estimate for (150.50), or a further exact recombination that
preserves \(\chi_4(L_1L_2r_1r_2)\) and controls all shifts at once.
No such estimate is derived here.  This is the first doubtful step;
the coefficient expansion and the algebraic factor identity themselves
are proved.

The compulsory endpoint test makes the scope sharp.  At \(D=1\), the
centered condition already implies the collar condition, so the full
nonexact collar contains every nonexact pair.  At \(L_1=L_2=1\),

\[
 B_{1,U}(1)=
 \sum_{\substack{v\ \mathrm{odd\ squarefree}}}
 \frac{\mu(v)}{v^2}\kappa_{1,U}(v^2),
\tag{150.51}
\]

and the complete \(L=1\) nonexact contribution is the square of the
literal character reciprocal sum, less its already owned exact phase
classes:

\[
 |B_{1,U}(1)|^2
 \left|\sum_{q\asymp Q\atop q\ \mathrm{odd}}
 \chi_4(q)\mathscr W_{1,U}(1/q)e(N/q)\right|^2
 -\mathcal E_{\mathrm{exact},L=1}.
\tag{150.52}
\]

The \(k=0\) subfamily of (150.52) is covered by (150.7), and every
bounded-\(M\) instance is covered completely by (150.71).  For
growing \(E\), however, most pairs have \(k\ne0\), outside the packet
(150.7a).  There is no \(d\)-average in (150.52).  Thus the remaining
seam cannot be removed by citing the incidence average alone, and no
arbitrary coefficient or unproved variation analogue is substituted
for the actual sum.

## 5. Control tests and outcomes

1. **`literal_nonzero_collar_expansion` -- pass.**  Equation
   (150.13) retains both \(B\)'s, both profiles, both prefixes through
   the \(B\)'s, squarefreeness, reducedness, common gcd \(h\), the
   centered \(k\), imprimitive denominators, the phase, and the exact
   mod-four factor.

2. **`two_row_divisor_incidence_linearization` -- pass.**  Equations
   (150.18)--(150.22) give the literal two-row expansion.  Forced
   primes form \(F\), excluded primes form \(P\), incompatibility is
   \((F,P)>1\), and coprimality is expanded exactly through \(z\mid P\).
   Equations (150.23)--(150.24) give its
   \(O_\varepsilon(X^\varepsilon)\) coefficient projective norm.

3. **`prefix_profile_d_dependence` -- pass as an exact audit.**
   Equations (150.25)--(150.30) show the floor-existence prefix, the
   two appearances of \(d\) in the sampled amplitude, the linear and
   quadratic \(d\)-dependencies, and the sampled cone's exact
   independence from \(d\).  No unproved global variation bound is
   used.

4. **`shifted_factor_identity` -- pass.**  Equations
   (150.40)--(150.41) verify the signs, integrality, and support
   congruences.  Equation (150.45) proves injective recovery for a
   fixed nonzero shift.

5. **`k_zero_and_exceptional_factor` -- pass.**  The entire nonexact
   \(k=0\) collar is bounded by (150.38), and the larger fixed-wrap
   packet is bounded by (150.65).  For wraps outside that packet,
   (150.41)--(150.42) make both factors positive and exclude zero
   factors and \(T=0\), including when a denominator divides \(N\).

6. **`full_shift_and_weight_summation` -- pass/open split.**  Every
   \(h,L_1,L_2,d\) and every literal coefficient weight is summed for
   each fixed \(k\), and every \(k\) in (150.7a) is summed in the
   promoted packet.  For the remaining large wraps, all
   \(h,k,\rho\) are summed in the method audit (150.48); the resulting
   fixed-shift divisor route is rigorously too costly.  The actual
   signed growing-\(M\), large-wrap sum remains open.

7. **`tuple_absolute_signed_separation` -- pass.**  Equation
   (150.36) is a raw tuple count, (150.15) and (150.37) are
   coefficient-weighted absolute masses, and (150.13) is the signed
   quantity.  Equation (150.48) is an adverse upper capacity and is
   not read as a signed lower bound.

8. **`mod_four_character_retention` -- pass.**  The exact sign is
   \(\chi_4(L_1L_2r_1r_2)\) by (150.14).  The \(k=0\) estimate is
   stronger because it survives absolute values; the unresolved sum
   (150.50) retains the sign.

9. **`all_M_D_E_Q_L_h_k_rho_power_ledger` -- pass.**  The relevant
   sizes are

   \[
   E\asymp M/D,\quad Q\asymp DR^2/\sqrt M,\quad
   H\asymp L_1L_2Q^2/h,\quad
   |k|\ll R^2\sqrt M/D,
   \tag{150.53}
   \]

   together with (150.32), (150.36), and (150.47)--(150.49).  The
   fixed-wrap energy is \(DQ\), whose ratio to \(R^2D\) is
   \(D/\sqrt M\leq1\); hence \(O(1+\sqrt M/D)\) wraps are
   target-safe.  The separately summed full nonzero-shift divisor
   capacity loses at least \(R\) already at raw tuple level.  The
   bounded-\(M\) full row is independently target-safe by (150.71).

10. **`D1_L1_full_frequency_test` -- pass/open split.**  For
    \(D=1\), the collar is the full centered nonexact family.
    Equations (150.51)--(150.52) retain the actual one-row reciprocal
    sum.  Its bounded-\(M\) part passes completely by (150.71), and
    its small-wrap part passes (150.65).  At growing \(M\), the
    remaining wraps are the exact endpoint seam, with no invented
    \(d\)-average.

11. **`prime_parity_prefix_imprimitive_controls` -- pass.**  Writing
    \(d=\eta m\) retains even squarefree rows.  Odd primes forced into
    or excluded from \(m\) are represented by \(F,P\), including
    cross-row incompatibility.  The literal floor prefix is never
    smoothed.  Common factors and imprimitive fractions are retained
    through \(h,r_i\); dropping restrictions occurs only inside an
    upper count.

12. **`exact_and_small_denominator_exclusion` -- pass.**  The promoted
    range has \(\rho\ne0\); \(\rho=0\) stays with the accepted exact
    owner.  The proof of (150.7) includes, rather than assumes away,
    small reduced denominators and \(q_i\mid N\).  It creates no new
    claim about the generic complement.

13. **`generic_tge2_cross_and_downstream_scope` -- pass.**  The
    \(k\ne0\) collar is isolated as the next exact seam.  The generic
    non-collar, every \(t\geq2\) layer, the independent Round-138
    cross owner, lower GAR, M9--M1, M9--M2, endpoint uniformity, M9,
    the bridge, the quarter target, and both exponent statements are
    unchanged.

No numerical experiment and no external theorem were used.

## 6. Dependencies and exact artifacts used

The derivation used exactly the selected context authorized by the
task:

- `protocol.md`;
- `state/proof_obligations.yml`, especially
  `M9-M1-lower-cone-t1-squarefree-gcd-lift-compression-reduction`,
  `M9-M1-lower-cone-t1-squarefree-gcd-lift-energy-obstruction`, and
  `M9-M1-global-lower-radial-signed-estimate`;
- `state/active_campaign.yml`;
- `strategy/round150_moving_coefficient_near_collision_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/reports/gcd_lift_euler_compression_attack.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/reviews/conductor_round149_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/controls/conductor_round149_controls.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`.

The accepted inputs are the exact compressed row, the closed
\(B_{d,U}\) formula, the two prefix-uniform \(B\)-norms, the bounded
profile, exact-phase ownership, and the parameter support.  The
two-row incidence formula, its coefficient norm, the sampled-cutoff
audit, the \(k=0\) determinant estimate, the fixed-wrap packet, the
bounded-\(M\) full-row estimate, the shifted-factor exceptional-case
audit, and the complete fixed-shift power ledger are derived here.

## 7. Recommended state effect

Close this task under

\[
 \boxed{\mathsf{strict\_moving\_coefficient\_collar\_range}.}
\tag{150.54}
\]

Subject to independent seam review, promote as candidate mathematics:

1. the exact two-row divisor-incidence expansion
   (150.18)--(150.24), with both literal prefixes and profiles retained
   as in (150.25)--(150.30);
2. the complete fixed-wrap estimate (150.64), hence the target-safe
   packet (150.7a)--(150.7b), including the nonexact \(k=0\) collar;
3. the bounded-\(M\) full-row estimate (150.66)--(150.71); and
4. the shifted-factor identity, positivity and exceptional-factor
   audit, fixed-shift divisor bound, and scoped all-shift absolute
   summation no-go (150.40)--(150.49).

Retain the full moving-coefficient collar target as open.  Its strict
complement is the growing-\(M\) portion with centered wrap integers
outside a packet of size \(O(1+R^2/Q)\), still under
\(0<|\rho|\leq hr_1r_2/D\), with the literal signed atom (150.50).
That complement is the next isolated owner seam.  The generic
non-collar is controlled here only in the bounded-\(M\) edge; do not
promote it at any growing scale.  Do not promote the full all-scale
joint energy, the \(RD\) scalar target, any \(t\geq2\) layer, the
Round-138 cross term, or any downstream obligation or exponent.
