# Round 149 terminal hostile review: gcd-lift compression and energy boundary

## 1. Result

**Terminal verdict: GREEN. First exact defect: none.**

The discovery report
reports/gcd_lift_euler_compression_attack.md and the conductor candidate
candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md
are compatible and mathematically sound on the claims selected for
promotion. In particular,

\[
 C_d(n)=
 \begin{cases}
  \mu(u)\mu(v),&
  n=uv^2,\quad u\mid d_{\mathrm o},\quad
  \mu^2(uv)=1,\quad (v,d)=1,\quad u,v\ {\rm odd},\\
 0,&\text{otherwise},
 \end{cases}
 \qquad d_{\mathrm o}=\frac d{(d,2)},
\tag{149.R1}
\]

is the exact lcm coefficient for squarefree \(d\), whether \(d\) is
odd or even. The odd-prime exponent-two cancellation is compulsory,
and \(p=2\) is absent from the lcm and gcd-lift ledger. The finite
compression

\[
 B_{d,U}(L)=
 \sum_{\substack{g\geq1\\g\ {\rm odd}}}
 \frac{C_d(gL)\kappa_{d,U}(gL)}g
\tag{149.R2}
\]

retains the literal prefix and gives the exact row

\[
 G_U(d)=
 \sum_{\substack{L,q_0\ {\rm odd}\\(L,q_0)=1\\q_0\asymp LQ}}
 \chi_4(Lq_0)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q_0)e(NdL/q_0).
\tag{149.R3}
\]

The prefix-uniform norms, equal-cell diagonal, complete exact phase
classes, and small individual reduced denominators satisfy

\[
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 +\sum_L\frac{|B_{d,U}(L)|}{L}
 \ll_\varepsilon X^\varepsilon,
\tag{149.R4}
\]

\[
 \mathscr E_{\rm diag}\ll_\varepsilon DQX^\varepsilon,
\qquad
 \mathscr E_{\rm exact,off}\ll_\varepsilon DX^\varepsilon,
\qquad
 \mathscr E_{\rm exact,all}\ll_\varepsilon DQX^\varepsilon,
\tag{149.R5}
\]

\[
 \mathscr E(q_0/(q_0,N)\le Y)
 \ll_\varepsilon DY^2X^\varepsilon
 \quad(Y\le R).
\tag{149.R6}
\]

There is no conflict between the candidate's
\(O(DX^\varepsilon)\) divisor count and the discovery report's
\(O(DQX^\varepsilon)\) phase-class bound. The former is the sharper
bound for **distinct exact off-diagonal pairs**. The latter groups
every cell in each exact phase class and includes the literal
equal-cell squares, whose natural size is \(DQ\). Precisely,

\[
 \mathscr E_{\rm exact,all}
 =\mathscr E_{\rm diag}+\mathscr E_{\rm exact,off}
 \ll_\varepsilon DQX^\varepsilon+DX^\varepsilon
 \ll_\varepsilon DQX^\varepsilon.
\tag{149.R7}
\]

The complete energy

\[
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \stackrel{?}{\ll}_\varepsilon R^2DX^\varepsilon
\tag{149.R8}
\]

remains open exactly where the two artifacts place it: the nonexact
near/generic determinant correlation with the actual \(d\)-dependent
coefficient. The no-go is correctly restricted to the inference from
the proved coefficient norm and positive diagonal through a classical
fixed-vector rational large sieve or a separately positive spacing
argument. It is not a lower bound for the signed row and not an
impossibility theorem for a new coefficient-sensitive organization.

## 2. Exact statement and hypotheses reviewed

The review uses

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\le R^2,\qquad D\le\sqrt M,
\tag{149.R9}
\]

\[
 E\asymp M/D,\qquad
 Q=2\sqrt{ND/E}\asymp\frac{DR^2}{\sqrt M},
\qquad EQ\asymp\sqrt{NM}.
\tag{149.R10}
\]

The hypotheses needed by the promoted kernel are:

1. \(d\asymp D\) is squarefree and may be even; only
   \(\alpha,b,\ell,q,g,L,q_0\) are odd.
2. The original Möbius cells have \(\alpha,b\) individually squarefree;
   they need not be coprime. The common-prime cells produce the
   cancellation at lcm exponent two.
3. The exact prefix
   \(\kappa_{d,U}(n)\in\{0,1\}\) is finite and may be irregular in
   \(d,n,U\). Its support gives \(n\le e_+\ll E\). No continuous
   replacement or monotonicity is assumed.
4. The inherited profile is uniformly bounded and has
   \(q_0\asymp LQ\); after the gcd lift it depends on
   \(d,U,L/q_0\), not separately on \(g\).
5. Every common odd lift is retained. Only
   \((L,q_0)=1\) is imposed; two different denominators may have a
   large common divisor and may be imprimitive relative to \(N\).
6. \(N=\lfloor X\rfloor\) is fixed. There is no center average, no
   arbitrary replacement of \(\chi_4\), and no discarded exact or
   near \(N\)-alignment.

For two cells write

\[
 h=(q_{0,1},q_{0,2}),\qquad
 q_{0,1}=hr_1,\qquad q_{0,2}=hr_2,\qquad(r_1,r_2)=1,
\tag{149.R11}
\]

\[
 \delta=L_1r_2-L_2r_1,\qquad
 \Delta=L_1q_{0,2}-L_2q_{0,1}=h\delta.
\tag{149.R12}
\]

Reducedness gives

\[
 (\delta,r_1r_2)=1,\qquad
 \frac{N\Delta}{q_{0,1}q_{0,2}}
 =\frac{N\delta}{hr_1r_2}.
\tag{149.R13}
\]

If \(k\) is a nearest integer and

\[
 \rho=N\delta-khr_1r_2,\qquad
 |\rho|\le\frac{hr_1r_2}{2},
\tag{149.R14}
\]

then base-frequency exact alignment is \(\rho=0\), while the first
nonzero collar is

\[
 0<|\rho|\le\frac{hr_1r_2}{D}.
\tag{149.R15}
\]

After separating squarefree parity as
\(d=\eta m\), \(\eta\in\{1,2\}\), \(m\) odd squarefree, the literal
centered numerator is instead

\[
 \rho_\eta=\eta N\delta-khr_1r_2,
\qquad
 0<|\rho_\eta|\ll\frac{hr_1r_2}{D}.
\tag{149.R16}
\]

The factor \(\eta\) in the length \(m\asymp D/\eta\) changes only the
absolute constant on the right. Formula (149.R16) also shows that an
\(\eta=2\) exact resonance with nonintegral base frequency is not
silently promoted by the exact-alignment lemma: it remains inside the
unproved nonexact sector of candidate (149.C31).

## 3. Proof and hostile derivation

### 3.1 Lcm coefficient and finite gcd-lift identity

At an odd prime \(p\nmid d_{\mathrm o}\), the local lcm coefficient is
\(1\) at exponent zero and \(-1\) at exponent two. At
\(p\mid d_{\mathrm o}\), it is \(1\) at exponent zero, \(-1\) at
exponent one, and

\[
 (-1)_{\ p\mid\alpha,\ p\nmid b}
 +(1)_{\ p\mid\alpha,\ p\mid b}=0
\tag{149.R17}
\]

at exponent two. Multiplication gives (149.R1). Since all variables
in the lcm are odd, the prime \(2\) contributes only the exponent-zero
factor, even when \(2\mid d\). Thus \(C_d=C_{d_{\mathrm o}}\) at the
lcm level, while the prefix and profile may still depend on the full
\(d\).

Membership in the accepted finite pair set depends on
\((\alpha,b)\) through \(d\), \(n=[\alpha^2,b]\), and whether the
\(n\)-progression meets the clipped amplitude. Also
\(\alpha^2\le n\le e_+\) once the progression is nonempty. Therefore
grouping first by \(n\) is an exact finite identity.

For every remaining \((n,q)\), the bijection

\[
 g=(n,q),\qquad n=gL,\qquad q=gq_0,\qquad(L,q_0)=1
\tag{149.R18}
\]

gives

\[
 \frac1n=\frac1{gL},\quad
 \chi_4(n)\chi_4(q)=\chi_4(g)^2\chi_4(Lq_0)=\chi_4(Lq_0),
\quad
 \frac{Ndn}{q}=\frac{NdL}{q_0}.
\tag{149.R19}
\]

The saddle value and support are unchanged because they depend on
\(n/q=L/q_0\); \(q\asymp nQ\) becomes \(q_0\asymp LQ\). This proves
(149.R2)--(149.R3) without a convergence exchange.

### 3.2 Exact lift parametrization and prefix norms

If \(B_{d,U}(L)\ne0\), write uniquely

\[
 L=ts^2,\qquad \mu^2(ts)=1,\qquad(t,s)=1,
\tag{149.R20}
\]

and put

\[
 a=(t,d_{\mathrm o}),\qquad r=t/a.
\tag{149.R21}
\]

The coefficient vanishes unless \((s,d_{\mathrm o})=1\). In the
nonzero case every lift is uniquely

\[
 u=au',\qquad v=rsv',\qquad
 u'\mid d_{\mathrm o}/a,\qquad
 \mu^2(v')=1,\qquad(v',d_{\mathrm o}rs)=1,
\tag{149.R22}
\]

and

\[
 g=u'r(v')^2.
\tag{149.R23}
\]

Consequently candidate (149.C15) and discovery (149.34) are the same
formula after the substitutions \((a,r,s)=(a_0,a_1,b)\). The
apparently different coprimality conditions are equivalent because
\(v'\) is odd and \(d=\eta d_{\mathrm o}\).

Taking absolute values only after this exact identity gives

\[
 |B_{d,U}(ts^2)|
 \ll_\varepsilon \frac{X^\varepsilon}{r}.
\tag{149.R24}
\]

The arbitrary prefix is harmless because only
\(0\le\kappa_{d,U}\le1\) is used. Since \(L=ars^2\), dropping
coprimality restrictions yields

\[
\begin{aligned}
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 &\ll_\varepsilon X^\varepsilon
 \sum_{a\mid d_{\mathrm o}}\frac1a
 \sum_{r\ge1}\frac1{r^3}
 \sum_{s\ge1}\frac1{s^2},\\
 \sum_L\frac{|B_{d,U}(L)|}{L}
 &\ll_\varepsilon X^\varepsilon
 \sum_{a\mid d_{\mathrm o}}\frac1a
 \sum_{r\ge1}\frac1{r^2}
 \sum_{s\ge1}\frac1{s^2}.
\end{aligned}
\tag{149.R25}
\]

Both converge with
\(\sum_{a\mid d_{\mathrm o}}a^{-1}\ll_\varepsilon X^\varepsilon\),
proving (149.R4). The support \(L\ll E\) similarly gives

\[
 \sum_L|B_{d,U}(L)|
 +\sum_L|B_{d,U}(L)|^2
 \ll_\varepsilon \sqrt E\,X^\varepsilon.
\tag{149.R26}
\]

Thus the candidate's weighted \(\ell^1\) claim, the discovery report's
unweighted \(\ell^1\) claim, and both square norms are consistent.

For each \(L\) there are \(O(LQ)\) denominators. The bounded actual
profile and (149.R25) give

\[
\begin{aligned}
 \mathscr E_{\rm diag}
 &\ll
 \sum_{d\asymp D}\sum_L
 \frac{|B_{d,U}(L)|^2}{L^2}(LQ)X^\varepsilon\\
 &\ll_\varepsilon DQX^\varepsilon.
\end{aligned}
\tag{149.R27}
\]

Since \(Q/R^2\asymp D/\sqrt M\le1\), this is uniformly within the
energy target.

### 3.3 The two exact-alignment proofs and their reconciliation

The discovery proof groups a cell by its reduced phase. Put

\[
 c=(q_0,N),\qquad r=q_0/c,\qquad s_N=N/c.
\tag{149.R28}
\]

Then

\[
 \frac{NL}{q_0}\equiv\frac{s_NL}{r}\pmod1,\qquad(r,s_N)=1,
\tag{149.R29}
\]

and the cells in a fixed reduced phase \(a/r\) satisfy

\[
 q_0=rc,\qquad c\mid N,\qquad
 L\equiv a\overline{s_N}\pmod r,\qquad L\asymp rc/Q.
\tag{149.R30}
\]

For \(c\ge Q\), one phase class has coefficient mass
\(\ll X^\varepsilon/r\). Summing its square over reduced numerators
and \(r\ll EQ\) costs \(X^\varepsilon\). For \(c<Q\), a fixed
\((r,c)\) contributes

\[
 \sum_a\left(\sum_{L\ {\rm in\ class}}\frac{X^\varepsilon}{L}\right)^2
 \ll_\varepsilon\frac{QX^\varepsilon}{rc}.
\tag{149.R31}
\]

The support gives \(Q/c\ll r\ll EQ/c\). Summing first over \(r\)
and then over \(c\mid N\) costs \(QX^\varepsilon\). Cauchy over the
divisor-many eligible \(c\)'s retains every cross-term. Therefore,
for each \(d\),

\[
 \sum_\theta
 \left(\sum_{NL/q_0\equiv\theta}|A_d(L,q_0)|\right)^2
 \ll_\varepsilon QX^\varepsilon.
\tag{149.R32}
\]

This is a complete positive phase-class bound and includes equal cells.

The candidate proves a sharper statement for distinct pairs. In its
notation

\[
 H=(q_1,q_2),\quad q_1=HA,\quad q_2=HB,\quad(A,B)=1,\quad
 \delta=L_1B-L_2A.
\tag{149.R33}
\]

Reducedness gives \((\delta,AB)=1\). For distinct cells
\(\delta\ne0\), and exact alignment is equivalent to

\[
 HAB\mid N\delta
 \quad\Longleftrightarrow\quad
 AB\mid N,\qquad H\mid (N/AB)\delta.
\tag{149.R34}
\]

For fixed \(L_1,L_2\), there are divisor-many choices of the coprime
pair \(A,B\) with \(AB\mid N\), and then divisor-many choices of
\(H\) dividing the fixed nonzero integer \((N/AB)\delta\). All
quantities are \(X^{O(1)}\), so the number of aligned denominator
pairs is \(O_\varepsilon(X^\varepsilon)\). The weighted
\(\ell^1\) norm in (149.R25) therefore gives

\[
 \mathscr E_{\rm exact,off}
 \ll_\varepsilon
 \sum_{d\asymp D}
 \left(\sum_L\frac{|B_{d,U}(L)|}{L}\right)^2X^\varepsilon
 \ll_\varepsilon DX^\varepsilon.
\tag{149.R35}
\]

This proof retains arbitrary prime powers in \(q_1,q_2\), common
factors, the bounded \(d\)-dependent profiles, and even squarefree
\(d\). Combining (149.R27) and (149.R35) proves (149.R7).
The \(r=1\) phase in the discovery proof is precisely
\(q_0\mid N\); the candidate's direct divisor bound for that row is
consistent with both arguments.

### 3.4 Small individual reduced denominators

For

\[
 r=\frac{q_0}{(q_0,N)}\le Y,\qquad q_0=rc,\qquad c\mid N,
\tag{149.R36}
\]

the support again gives \(L\asymp rc/Q\). For each fixed
\((r,c)\),

\[
 \sum_{L\asymp rc/Q}\frac{|B_{d,U}(L)|}{L}
 \ll_\varepsilon X^\varepsilon.
\tag{149.R37}
\]

Summing over \(r\le Y\) and the divisor-many \(c\mid N\) gives row
mass \(O_\varepsilon(YX^\varepsilon)\), and hence (149.R6). At
\(Y=R\) this is exactly \(R^2DX^\varepsilon\). The cross-term with
the complementary row is safely separated by

\[
 |G_{\le Y}+G_{>Y}|^2\le2|G_{\le Y}|^2+2|G_{>Y}|^2.
\tag{149.R38}
\]

The candidate leaves a broader nonexact sector open and therefore does
not depend on silently discarding this stratum. The discovery lemma
legally sharpens the terminal boundary by removing it before the
near/generic problem.

### 3.5 Near collisions, \(D=1\), and all-aspect powers

Equations (149.R11)--(149.R15) are algebraically exact. The literal
kernel is

\[
\begin{aligned}
 \mathcal K_U(1,2)
 ={}&\sum_{d\asymp D}\mu^2(d)
 \frac{B_{d,U}(L_1)\overline{B_{d,U}(L_2)}}{L_1L_2}\\
 &\times
 \mathscr W_{d,U}(L_1/q_{0,1})
 \overline{\mathscr W_{d,U}(L_2/q_{0,2})}
 e\!\left(\frac{d\rho}{hr_1r_2}\right).
\end{aligned}
\tag{149.R39}
\]

It is not the geometric kernel
\(\min(D,hr_1r_2/|\rho|)\), because the squarefree condition,
divisors of \(d_{\mathrm o}\), excluded primes, prefix, and both
profiles move with \(d\). The conductor candidate's parity split
(149.C29)--(149.C31) is the correct refinement of the discovery
formula and does not delete any even-\(d\) resonance.

The all-aspect translations are

\[
 \frac{Q}{R^2}\asymp\frac D{\sqrt M}\le1,\qquad
 EQ\asymp\sqrt{NM},\qquad
 Q\sqrt E\asymp R^2\sqrt D.
\tag{149.R40}
\]

They give the following verified capacities:

| placement | energy size | ratio to \(R^2D\) |
|---|---:|---:|
| equal cells | \(DQ\) | \(D/\sqrt M\le1\) |
| distinct exact off-diagonal | \(D X^\varepsilon\) | \(R^{-2}X^\varepsilon\) |
| full exact phase classes | \(DQX^\varepsilon\) | \(D/\sqrt M\le1\) |
| reduced denominator \(\le Y\) | \(DY^2X^\varepsilon\) | \((Y/R)^2\) |
| full row triangle | \(R^4D^2X^\varepsilon\) | \(R^2D\) |
| frozen coefficient, unwrapped spacing | \(Q(D+M)X^\varepsilon\) | \(D/\sqrt M+\sqrt M\) |
| all wrapped rational spacing | \(Q(D+NM)X^\varepsilon\) | \(D/\sqrt M+N\sqrt M\) |

At \(D=1\),

\[
 E\asymp M,\qquad Q\asymp R^2/\sqrt M,
\tag{149.R41}
\]

so the diagonal, exact alignments, and \(Y\le R\) stratum remain
target-safe, but there is no \(d\)-average. The actual
\(\chi_4(q_0)B_{d,U}(1)\)-weighted reciprocal row must be estimated.
The second-derivative diagnostic has first term
\((NM)^{1/4}=RM^{1/4}\); it reaches the scalar \(R\) target only at
the bottom aspect and returns a square-root phase for general \(M\).
The candidate correctly retains the full all-scale \(D=1\) row as
open.

At \(D\asymp E\asymp\sqrt M\), \(Q\asymp R^2\), so the diagonal can
saturate the target and the optimistic unwrapped placement still loses
\(\sqrt M\). At \(M=R^2\), \(Q\asymp DR\), the diagonal ratio is
\(D/R\le1\), while the same placement loses \(R\). These identities,
together with (149.R40), cover every \(M\le R^2\) and
\(D\le\sqrt M\).

## 4. First doubtful or unproved step

There is no exact defect in either reviewed artifact. The first
unproved step is the variable-row nonexact correlation

\[
\sum_{\eta=1,2}
\sum_{\substack{m\asymp D/\eta\\m\ {\rm odd\ squarefree}}}
\sum_{\substack{x_1\ne x_2\\\text{not base-exact}}}
A_{\eta m}(x_1)\overline{A_{\eta m}(x_2)}
e\!\left(m\frac{\eta N\delta}{HAB}\right)
\stackrel{?}{\ll}_\varepsilon R^2DX^\varepsilon,
\tag{149.R42}
\]

after the proved phase classes and, if desired, the
\(q_0/(q_0,N)\le R\) rows are removed. The first source seam remains
coefficient independence: the Montgomery--Vaughan fixed-vector large
sieve does not accept

\[
 B_{\eta m,U}(L_1)\overline{B_{\eta m,U}(L_2)}
 \mathscr W_{\eta m,U}(L_1/q_{0,1})
 \overline{\mathscr W_{\eta m,U}(L_2/q_{0,2})}.
\tag{149.R43}
\]

The exact and near determinant ledgers classify the obstruction; they
do not estimate (149.R42).

## 5. Control tests and outcomes

| Control | Terminal outcome |
|---|---|
| exact lcm coefficient | **GREEN.** (149.R1), including the common-prime square cancellation, follows from the complete odd-prime table. |
| even squarefree \(d\) and \(p=2\) | **GREEN.** Only \(d_{\mathrm o}\) enters \(C_d\); \(2\) is absent, while the full \(d\) remains in the prefix and profile. |
| finite gcd-lift recombination | **GREEN.** (149.R18)--(149.R19) are a finite bijection; character, phase, saddle, and support are exact. |
| exact-prefix norms | **GREEN.** (149.R24)--(149.R26) use only \(0\le\kappa\le1\), retain the floor cutoff, and prove both reports' stated norms. |
| literal equal-cell diagonal | **GREEN.** (149.R27) is \(DQX^\varepsilon\), target-safe for every aspect. |
| discovery exact phase-class proof | **GREEN.** (149.R28)--(149.R32) includes all \(N\)-dependent phases, cross-divisor terms, and \(q_0\mid N\). |
| candidate exact-pair divisor proof | **GREEN.** (149.R33)--(149.R35) proves the sharper distinct off-diagonal bound \(DX^\varepsilon\). |
| \(D\) versus \(DQ\) reconciliation | **GREEN.** The bounds concern distinct off-diagonal versus full phase classes; (149.R7) is the exact relation. |
| small reduced denominators | **GREEN.** (149.R36)--(149.R38) give \(DY^2X^\varepsilon\), uniformly target-safe for \(Y\le R\). |
| common divisors and imprimitive reductions | **GREEN.** One copy of \(h\) cancels, \((\delta,r_1r_2)=1\), and exact alignment is equivalent to the two divisibility conditions in (149.R34). |
| near-collision formula | **GREEN.** (149.R14)--(149.R16) retain the centered numerator, nearest integer, nonzero collar, parity split, and generic complement. |
| \(D=1\) | **GREEN as a boundary/no-go control.** No \(d\)-gain is claimed; the actual signed reciprocal row remains open at general \(M\). |
| all-aspect powers | **GREEN.** (149.R40)--(149.R41) and the table reproduce every \(R,M,D,E,Q\) power; adverse capacities are not called lower bounds. |
| fixed-vector source applicability | **GREEN as a no-go.** The literal coefficient is \(d\)-dependent before spacing; no classical common-vector theorem is invoked illegally. |
| \(H\)-interface and transform self-return | **GREEN.** No termwise cube-free-to-powerful identification is made; further comparison is deferred until exact Euler recombination. |
| downstream scope | **GREEN.** Round 138, every \(t\ge2\) layer, lower GAR, M9--M1/M2, the bridge, quarter target, and exponent remain unchanged. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The terminal review used:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round149_gcd_lift_energy_strategy.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/barrier_packet.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/reports/gcd_lift_euler_compression_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md;
- the sealed source audit
  rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/reports/rational_energy_source_audit.md,
  used only for the fixed-vector theorem seam.

No unlisted sibling report or later-round artifact was used. No synthesis,
validation matrix, proof draft, or shared-state file was modified.

## 7. Recommended state effect

**GREEN for promotion of the selected Round-149 kernel.** Promote:

1. the parity-correct lcm coefficient and finite gcd-lift identities
   (149.R1)--(149.R3);
2. the exact-prefix norm bounds (149.R4), including the candidate's
   weighted \(\ell^1\) refinement;
3. the literal diagonal \(DQX^\varepsilon\);
4. the distinct exact-alignment bound \(DX^\varepsilon\), with the full
   phase-class statement recorded as \(DQX^\varepsilon\); and
5. the small reduced-denominator energy
   \(DY^2X^\varepsilon\) for \(Y\le R\).

Retain (149.R8), (149.R42), the signed \(RD\) scalar target, and all
downstream obligations as open. Record the terminal label
\(\mathsf{gcd\_lift\_energy\_no\_go}\) only with its stated scope:
the proved compression, norms, diagonal, exact alignments, and small
individual denominators do not by themselves imply the remaining
variable-row energy through a fixed-vector rational large sieve or a
positive spacing ledger. They do not rule out a new signed
coefficient-sensitive theorem or a further exact Euler recombination.
