# Round 149 discovery report: Euler-compressed gcd lifts and the moving-coefficient near-collision gate

- Campaign: `m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate`
- Round: 149
- Task: `gcd_lift_euler_compression_attack`
- Role: discovery
- Starting graph SHA-256: `8f1912eeda4843718379213478a839b30fb2694d6b169ac8decbab5ca3561176`
- Allocation: 100% analytic and algebraic; 0% numerical

## 1. Result: exact compression, safe diagonal and exact alignments, but a nonzero near-collision no-go

Put

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq \sqrt M,
\]

and let \(U\) be any inherited half-open prefix retained by the
accepted Round-148 transform.  The variable \(d\) is squarefree but
need not be odd.  Write

\[
 d_{\mathrm o}:=\frac d{(d,2)}.
\tag{149.1}
\]

The first outcome is the exact, parity-correct lcm collapse

\[
 \boxed{
 C_d(n)=
 \begin{cases}
  \mu(u)\mu(v),&n=uv^2,\quad u\mid d_{\mathrm o},\quad
  \mu^2(uv)=1,\quad (v,d)=1,\quad u,v\text{ odd},\\
 0,&\text{otherwise}.
 \end{cases}}
\tag{149.2}
\]

In particular \(C_d(n)=0\) for even \(n\).  If an odd prime
\(p\mid d_{\mathrm o}\), the two cells
\((p\mid\alpha,p\nmid b)\) and
\((p\mid\alpha,p\mid b)\) cancel at lcm exponent two.  The prime
\(2\) never enters the lcm ledger.  Thus (149.2), not the version with
an implicit oddness assumption on \(d\), is the correct formula.

Let \(\kappa_{d,U}(n)\) be the literal indicator that the original
progression \(e=nm\), \(m\geq1\), meets the retained finite amplitude.
Then summing first over every Mobius cell with the same lcm, and next
over every common odd gcd lift, is an exact finite identity.  With
\(\ell=gL\), \(q=gq_0\), and \((L,q_0)=1\), define

\[
 B_{d,U}(L):=
 \sum_{g\geq1}\frac{C_d(gL)\kappa_{d,U}(gL)}g.
\tag{149.3}
\]

The accepted Round-148 scalar becomes

\[
 \boxed{
 \mathcal T_{D,E,U}
 =\sum_{d\asymp D}\mu^2(d)\frac Dd\,G_U(d),}
\tag{149.4}
\]

where

\[
 \boxed{
 G_U(d)=
 \sum_{\substack{L,q_0\geq1\ \mathrm{odd}\\(L,q_0)=1}}
 \frac{\chi_4(Lq_0)B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q_0)
 e\!\left(\frac{NdL}{q_0}\right),
 \qquad q_0\asymp LQ,}
\tag{149.5}
\]

and

\[
 Q=2\sqrt{ND/E}\asymp \frac{DR^2}{\sqrt M}.
\tag{149.6}
\]

Every dependence on the common lift \(g\) is in (149.3).  Indeed,
\(\chi_4(g)^2=1\), while the phase, saddle value, and profile depend
only on \(L/q_0\).

The truncated lift has more than the requested square summability:

\[
 \boxed{
 \sum_{L\geq1}\frac{|B_{d,U}(L)|^2}{L}
 \ll_\varepsilon X^\varepsilon,
 \qquad
 \sum_{L\geq1}|B_{d,U}(L)|
 \ll_\varepsilon \sqrt E\,X^\varepsilon.}
\tag{149.7}
\]

Both bounds are uniform in squarefree even or odd \(d\), in every
actual prefix, and in every aspect.  They use only
\(0\leq\kappa_{d,U}\leq1\), so no regularity of the finite prefix is
silently assumed.

Consequently the literal equal-cell diagonal of the proposed joint
energy is

\[
 \mathscr E_U^{\rm diag}\ll_\varepsilon DQX^\varepsilon
 \leq R^2DX^\varepsilon.
\tag{149.8}
\]

More strongly, after grouping cells with exactly the same additive
phase \(NL/q_0\pmod1\), the complete exact-alignment contribution,
including distinct cells, also satisfies

\[
 \boxed{\mathscr E_U^{\rm exact}\ll_\varepsilon DQX^\varepsilon.}
\tag{149.9}
\]

Thus neither the literal diagonal, \(q_0\mid N\), nor any other exact
\(N\)-dependent phase alignment is the first obstruction.

The target energy

\[
 \mathscr E_U:=\sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \stackrel{?}{\ll}_\varepsilon R^2DX^\varepsilon
\tag{149.10}
\]

is nevertheless not proved.  After (149.9), the first genuinely open
sector is the nonzero centered near-collision family.  For two cells
put \(h=(q_{0,1},q_{0,2})\),
\(q_{0,1}=hr_1\), \(q_{0,2}=hr_2\), \((r_1,r_2)=1\), and

\[
 \delta=L_1r_2-L_2r_1,
 \qquad
 \rho=N\delta-khr_1r_2,
 \qquad
 |\rho|\leq \frac{hr_1r_2}{2},
\tag{149.11}
\]

where \(k\) is a nearest integer.  Exact alignment is \(\rho=0\) and
is covered by (149.9).  The first open collar is

\[
 \boxed{0<|\rho|\leq \frac{hr_1r_2}{D}.}
\tag{149.12}
\]

Its literal \(d\)-kernel contains
\(\mu^2(d)B_{d,U}(L_1)\overline{B_{d,U}(L_2)}\) and two
\(d\)-dependent profiles.  It is therefore not the geometric kernel
to which a classical rational large sieve with a fixed coefficient
vector applies.  Expanding this arithmetic dependence recreates
squarefree divisibility, coprimality, prefix, and imprimitive strata;
no estimate in the permitted context closes (149.12) or its generic
complement.

Even the optimistic diagnostic in which those coefficients are frozen
has unwrapped capacity \(Q(D+M)X^\varepsilon\), whose \(QM\) term
exceeds (149.10) by \(\sqrt M\).  Full rational spacing in the
presence of wrapped near alignments gives the still weaker capacity
\(Q(D+NM)X^\varepsilon\).  These are adverse upper capacities, not
lower bounds for (149.10).  At \(D=1\) there is no \(d\)-average at
all, so the actual \(\chi_4\)- and \(B_{1,U}\)-sensitive reciprocal
sum is mandatory.

Accordingly this report closes under

\[
 \boxed{\mathsf{gcd\_lift\_energy\_no\_go}.}
\tag{149.13}
\]

The no-go is confined to deriving the complete energy from the lift
square norm, exact-diagonal control, and a classical fixed-vector
rational large sieve or positive spacing ledger.  It is not a signed
lower bound and does not rule out a coefficient-sensitive
near-collision theorem, further exact Euler recombination, or a joint
cross-layer mechanism.

## 2. Exact statement and hypotheses

The accepted input is the finite Round-148 reciprocal scalar.  After
its already owned radial and cone collars, its amplitude
\(\mathscr A_{D,E,U}(d,e)\) is compactly supported in
\(0<e\leq e_+\ll E\), is uniformly bounded, and is exact on every
retained lattice point.  Define

\[
 \kappa_{d,U}(n)
 :={\bf1}_{\{\exists m\geq1:\ 
   \mathscr A_{D,E,U}(d,nm)\ne0\}}.
\tag{149.14}
\]

This indicator is allowed to be irregular in both \(d\) and \(n\).
If it is one, then \(n\leq e_+\), so every sum below is finite.

For squarefree \(d\), even or odd, set

\[
 C_d(n):=
 \sum_{\substack{\alpha,b\ \mathrm{odd},\ b\mid d\\
                  \mu^2(\alpha)=\mu^2(b)=1\\
                  [\alpha^2,b]=n}}
 \mu(\alpha)\mu(b).
\tag{149.15}
\]

The precise theorem proved in this report consists of (149.2)--(149.9)
under the following literal conditions:

1. \(N=\lfloor X\rfloor\) is fixed; no center average is introduced.
2. Only the individual positive physical phase, hence the positive
   reciprocal saddle, is used.
3. \(d\asymp D\) is squarefree, but \(2\mid d\) is permitted;
   \(\alpha,b,\ell,q,g,L,q_0\) are odd.
4. \(DE\asymp M\leq R^2\), \(D\leq\sqrt M\), and
   \(Q\) is (149.6), with its literal factor two in the accepted
   transform.
5. The prefix and cone profiles are the actual accepted profiles.
   Only their boundedness and the support
   \(q_0\asymp LQ\), \(L\leq e_+\ll E\), are used in the new norm
   and diagonal arguments.
6. All gcd lifts are included in \(B_{d,U}\).  The reduced condition
   is only \((L,q_0)=1\); denominators from different cells may share
   a large common divisor, and \(q_0\) may be imprimitive relative to
   \(N\).

For the energy expansion define

\[
 A_d(L,q_0):=
 \frac{\chi_4(Lq_0)B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q_0),
\tag{149.16}
\]

so that \(G_U(d)=\sum A_d(L,q_0)e(NdL/q_0)\).  For two cells set

\[
 \Delta=L_1q_{0,2}-L_2q_{0,1}.
\tag{149.17}
\]

Then the literal off-diagonal is

\[
 \boxed{
 \mathscr E_U^{\rm off}
 =\sum_{\substack{(L_1,q_{0,1})\ne(L_2,q_{0,2})}}
 \sum_{d\asymp D}\mu^2(d)
 A_d(L_1,q_{0,1})\overline{A_d(L_2,q_{0,2})}
 e\!\left(\frac{Nd\Delta}{q_{0,1}q_{0,2}}\right).}
\tag{149.18}
\]

No coefficient has been moved outside the \(d\)-sum in (149.18).
With the notation of (149.11),

\[
 \Delta=h\delta,
 \qquad
 \frac{N\Delta}{q_{0,1}q_{0,2}}
 =\frac{N\delta}{hr_1r_2}.
\tag{149.19}
\]

Moreover

\[
 (\delta,r_1r_2)=1.
\tag{149.20}
\]

Hence exact alignment has the sharper necessary and sufficient
conditions

\[
 r_1r_2\mid N,
 \qquad
 h\mid \frac{N}{r_1r_2}\,\delta.
\tag{149.21}
\]

Equations (149.11)--(149.12), (149.19)--(149.21) are the complete
common-divisor, imprimitive-denominator, exact-alignment, and
near-collision bookkeeping used below.

## 3. Proof or derivation

### 3.1 Prime-local lcm collapse, including even \(d\)

Fix an odd prime \(p\).  Let \(a\in\{0,1\}\) be the exponent of
\(p\) in \(\alpha\), let \(b_p\in\{0,1\}\) be its exponent in
\(b\), and let \(\delta_p={\bf1}_{p\mid d_{\mathrm o}}\).  The
local lcm exponent is

\[
 t=\max(2a,b_p),
\]

and the local sign is \((-1)^{a+b_p}\), with
\(b_p\leq\delta_p\).  Direct enumeration gives

| relation to \(d_{\mathrm o}\) | \(t=0\) | \(t=1\) | \(t=2\) | other \(t\) |
|---|---:|---:|---:|---:|
| \(p\nmid d_{\mathrm o}\) | \(1\) | \(0\) | \(-1\) | \(0\) |
| \(p\mid d_{\mathrm o}\) | \(1\) | \(-1\) | \((-1)+(+1)=0\) | \(0\) |

The displayed zero is the compulsory cancellation between
\((a,b_p)=(1,0)\) and \((1,1)\).  At \(p=2\), oddness forces
\(a=b_p=0\); the sole local value is one at exponent zero, whether or
not \(2\mid d\).  Multiplying the local tables proves (149.2): an
exponent-one prime must enter the odd divisor \(u\mid d_{\mathrm o}\),
an exponent-two prime must enter an odd squarefree \(v\) coprime to
\(d\), and the two sets of primes are disjoint.  Their signs are
\(\mu(u)\mu(v)\).

Useful hostile-check specializations are

\[
 C_d(p)=-{\bf1}_{p\mid d_{\mathrm o}},
 \qquad
 C_d(p^2)=-{\bf1}_{p\nmid d_{\mathrm o}}
 \quad(p\text{ odd}).
\tag{149.22}
\]

Thus the coefficient genuinely changes when an odd prime enters
\(d\); for even squarefree \(d=2d_{\mathrm o}\), its arithmetic lcm
coefficient is exactly the same as for \(d_{\mathrm o}\), while its
profile and prefix may still depend on the full \(d\).

### 3.2 Finite lcm recombination and gcd-lift identity

For a fixed \(d\), all pairs \((\alpha,b)\) with the same
\(n=[\alpha^2,b]\) have the same progression and the same
Round-148 saddle profile.  Also, if (149.14) is one, then
\(\alpha^2\leq n\leq e_+\), so the separate condition
\(\alpha^2\leq e_+\) in the finite Round-148 set is automatic after
grouping by \(n\).  Therefore, for every function \(F\),

\[
 \sum_{(\alpha,b)\in\mathcal P(d)}
 \mu(\alpha)\mu(b)F([\alpha^2,b])
 =\sum_{n\geq1}C_d(n)\kappa_{d,U}(n)F(n).
\tag{149.23}
\]

Applying (149.23) to the accepted scalar gives

\[
 \sum_{n\geq1}\frac{C_d(n)\kappa_{d,U}(n)\chi_4(n)}n
 \sum_{\substack{q>0\\q\ \mathrm{odd}}}
 \chi_4(q)\mathscr W_{d,n,U}(q)
 e(Ndn/q),
\tag{149.24}
\]

where

\[
 \mathscr W_{d,n,U}(q)
 =\mathscr A_{D,E,U}\!\left(d,\frac{4Ndn^2}{q^2}\right),
 \qquad q\asymp nQ.
\tag{149.25}
\]

For each finite pair \((n,q)\), take
\(g=(n,q)\), \(n=gL\), and \(q=gq_0\).  This is a bijection with
odd triples \((g,L,q_0)\) satisfying \((L,q_0)=1\).  The four
pieces transform exactly as follows:

\[
 \frac1n=\frac1{gL},\qquad
 \chi_4(n)\chi_4(q)=\chi_4(g)^2\chi_4(Lq_0)=\chi_4(Lq_0),
\tag{149.26}
\]

\[
 e(Ndn/q)=e(NdL/q_0),
\tag{149.27}
\]

and

\[
 \mathscr W_{d,gL,U}(gq_0)
 =\mathscr A_{D,E,U}\!\left(d,\frac{4NdL^2}{q_0^2}\right)
 =:\mathscr W_{d,U}(L/q_0).
\tag{149.28}
\]

Finally \(q\asymp nQ\) is equivalent to
\(q_0\asymp LQ\).  Summing the remaining factor
\(C_d(gL)\kappa_{d,U}(gL)/g\) gives (149.3)--(149.5).
Because \(\kappa_{d,U}(gL)=1\) implies \(gL\leq e_+\), this is a
finite rearrangement, not a conditionally convergent Euler operation.

### 3.3 Exact lift parametrization and the uniform square norm

If \(B_{d,U}(L)\ne0\), then \(L\) divides some
\(uv^2\) from (149.2).  Hence \(L\) is odd and cube-free.  Write it
uniquely as

\[
 L=ab^2,
 \qquad \mu^2(ab)=1,
 \qquad (a,b)=1,
\tag{149.29}
\]

and put

\[
 a_0=(a,d_{\mathrm o}),\qquad a_1=a/a_0.
\tag{149.30}
\]

Necessarily \((b,d)=1\).  Every nonzero multiple \(uv^2\) of
\(L\) occurring in (149.2) is then uniquely

\[
 u=a_0u',\qquad
 v=a_1bv',
\tag{149.31}
\]

where

\[
 u'\mid d_{\mathrm o}/a_0,qquad
 \mu^2(v')=1,qquad
 (v',da_1b)=1.
\tag{149.32}
\]

The corresponding gcd lift is

\[
 g=\frac{uv^2}{L}=u'a_1(v')^2.
\tag{149.33}
\]

Consequently the exact finite lift is

\[
\boxed{
\begin{aligned}
 B_{d,U}(ab^2)
 ={}&\frac{\mu(a_0)\mu(a_1b)}{a_1}
 \sum_{u'\mid d_{\mathrm o}/a_0}\frac{\mu(u')}{u'}\\
 &\quad\times
 \sum_{\substack{v'\geq1\\\mu^2(v')=1\\(v',da_1b)=1}}
 \frac{\mu(v')}{(v')^2}
 \kappa_{d,U}\!\left(a_0u'(a_1bv')^2\right),
\end{aligned}}
\tag{149.34}
\]

provided \((b,d)=1\), and it is zero if (149.29) or that coprimality
condition fails.  This formula displays every lift, every sign, and
every prefix cutoff.

Taking absolute values only for the norm control gives

\[
 |B_{d,U}(ab^2)|
 \leq \frac1{a_1}
 \prod_{p\mid d_{\mathrm o}/a_0}\left(1+\frac1p\right)
 \sum_{v'\geq1}\frac{\mu^2(v')}{(v')^2}
 \ll_\varepsilon \frac{X^\varepsilon}{a_1}.
\tag{149.35}
\]

Therefore

\[
\begin{aligned}
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 &\ll_\varepsilon X^\varepsilon
 \sum_{a_0\mid d_{\mathrm o}}\frac1{a_0}
 \sum_{a_1\geq1}\frac{\mu^2(a_1)}{a_1^3}
 \sum_{b\geq1}\frac{\mu^2(b)}{b^2}\\
 &\ll_\varepsilon X^\varepsilon.
\end{aligned}
\tag{149.36}
\]

All omitted coprimality and finite-support conditions only decrease
the majorant.  Likewise, since \(L\leq e_+\ll E\),

\[
\begin{aligned}
 \sum_L|B_{d,U}(L)|
 &\ll_\varepsilon X^\varepsilon
 \sum_{a_0\mid d_{\mathrm o}}
 \sum_{a_1\geq1}\frac1{a_1}
 \#\left\{b:\ b^2\leq \frac{E}{a_0a_1}\right\}\\
 &\ll_\varepsilon \sqrt E X^\varepsilon
 \left(\sum_{a_0\mid d_{\mathrm o}}a_0^{-1/2}\right)
 \left(\sum_{a_1\geq1}a_1^{-3/2}\right)
 \ll_\varepsilon \sqrt E X^\varepsilon.
\end{aligned}
\tag{149.37}
\]

This proves (149.7).  Notice that the proof did not smooth or
monotonize \(\kappa_{d,U}\).

### 3.4 Joint-energy normalization and the literal diagonal

Since \(d\asymp D\), Cauchy only at the final \(d\)-sum gives

\[
 |\mathcal T_{D,E,U}|^2
 \leq
 \left(\sum_{d\asymp D}\mu^2(d)\frac{D^2}{d^2}\right)
 \mathscr E_U
 \ll D\mathscr E_U.
\tag{149.38}
\]

Thus (149.10) implies
\(|\mathcal T_{D,E,U}|\ll RDX^\varepsilon\), exactly the
Round-148 target.

For a fixed \(L\), the number of odd \(q_0\asymp LQ\) is
\(O(LQ)\), and the actual profile is uniformly bounded.  Hence

\[
\begin{aligned}
 \mathscr E_U^{\rm diag}
 &=\sum_{d\asymp D}\mu^2(d)
 \sum_{\substack{L,q_0\\(L,q_0)=1}}
 \frac{|B_{d,U}(L)|^2}{L^2}
 |\mathscr W_{d,U}(L/q_0)|^2\\
 &\ll Q\sum_{d\asymp D}
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 \ll_\varepsilon DQX^\varepsilon.
\end{aligned}
\tag{149.39}
\]

The parameter relations are

\[
 E\asymp M/D,\qquad
 Q\asymp \frac{DR^2}{\sqrt M},\qquad
 D\leq Q\leq R^2,
\qquad
 EQ\asymp \sqrt{NM}=R^2\sqrt M.
\tag{149.40}
\]

In particular \(Q/R^2\asymp D/\sqrt M\leq1\), proving (149.8).
This calculation retains the actual \(d\)-dependent
\(B_{d,U}\) and profile; it does not replace them by a common vector.

### 3.5 Every exact \(N\)-alignment and every small additive denominator

For a cell \((L,q_0)\), put

\[
 c=(q_0,N),\qquad r=q_0/c,\qquad s=N/c.
\tag{149.41}
\]

Then \(c\mid N\), \((r,s)=1\), and, because \((L,q_0)=1\),

\[
 \frac{NL}{q_0}\equiv\frac{sL}{r}\pmod1
\tag{149.42}
\]

is a reduced fraction of denominator \(r\).  Fix one reduced phase
\(a/r\).  Its cells have

\[
 q_0=rc,qquad c\mid N,qquad (r,N/c)=1,qquad
 L\equiv a\overline{(N/c)}\pmod r,qquad
 L\asymp rc/Q.
\tag{149.43}
\]

By (149.35), the absolute coefficient of a cell is
\(\ll X^\varepsilon/L\).  Split the divisors \(c\mid N\) at
\(c=Q\).

If \(c\geq Q\), a fixed residue class in the interval
\(L\asymp rc/Q\) contains \(O(1+c/Q)\) integers, so its coefficient
mass is

\[
 \ll_\varepsilon X^\varepsilon
 \left(1+\frac cQ\right)\frac Q{rc}
 \ll_\varepsilon \frac{X^\varepsilon}{r}.
\tag{149.44}
\]

There are only \(\tau(N)\) choices of \(c\).  Squaring the total
mass, summing over the \(\varphi(r)\) reduced numerators, and then over
\(r\ll EQ\), gives

\[
 \ll_\varepsilon X^\varepsilon
 \sum_{r\ll EQ}\frac{\varphi(r)}{r^2}
 \ll_\varepsilon X^\varepsilon.
\tag{149.45}
\]

If \(c<Q\), the interval in (149.43) contains \(O(1)\) integers per
residue class.  For a fixed \((r,c)\), summation over all numerators
gives

\[
 \sum_a\left(\sum_{\substack{L\asymp rc/Q\\L\text{ in the }a
 \text{ class}}}\frac{X^\varepsilon}{L}\right)^2
 \ll_\varepsilon \frac{QX^\varepsilon}{rc}.
\tag{149.46}
\]

When contributions from different \(c\)'s fall in the same phase
class, Cauchy over the at most \(\tau(N)\) eligible divisors costs only
an \(X^\varepsilon\) factor.  Thus all short-\(c\) cross-terms are
included.  The support forces \(r\asymp LQ/c\), hence
\(Q/c\ll r\ll EQ/c\).  Summing (149.46) over \(r\), then over
\(c\mid N\), gives

\[
 \ll_\varepsilon QX^\varepsilon
 \sum_{c\mid N}\frac1c
 \ll_\varepsilon QX^\varepsilon.
\tag{149.47}
\]

The long-\(c\)/short-\(c\) cross-term is absorbed phase by phase by
\((x+y)^2\leq2x^2+2y^2\).  Combining (149.45)--(149.47), for every
fixed \(d\),

\[
 \sum_{\theta\in\mathbb Q/\mathbb Z}
 \left(
  \sum_{\substack{(L,q_0):\\NL/q_0\equiv\theta\ ({\rm mod}\ 1)}}
  |A_d(L,q_0)|
 \right)^2
 \ll_\varepsilon QX^\varepsilon.
\tag{149.48}
\]

Summing (149.48) over \(d\asymp D\) proves (149.9).  This argument
includes the \(r=1\) class, namely every \(q_0\mid N\), and it
includes the common-divisor exact alignments (149.21).  It does not
assume that exact equality of phases means equality of cells.

The same parametrization gives a useful separate low-denominator
control.  For \(r=q_0/(q_0,N)\leq Y\), discard the phase and sum
absolutely.  For each \((r,c)\), the interval
\(L\asymp rc/Q\) has coefficient mass \(O_\varepsilon(X^\varepsilon)\);
the divisor multiplicity of \(c\mid N\) is absorbed.  Therefore

\[
 \sum_{\substack{(L,q_0)\\q_0/(q_0,N)\leq Y}}
 |A_d(L,q_0)|\ll_\varepsilon YX^\varepsilon,
\tag{149.49}
\]

and this stratum costs at most

\[
 \mathscr E_U(r\leq Y)\ll_\varepsilon DY^2X^\varepsilon.
\tag{149.50}
\]

It is target-safe for every \(Y\leq R\).  Thus the already known
small reduced-denominator owner survives the exact gcd-lift
compression.  It may be removed at row level before treating the
complement; the cross-term causes no seam because
\(|G_{\leq Y}+G_{>Y}|^2\leq
2|G_{\leq Y}|^2+2|G_{>Y}|^2\).

### 3.6 The complete nonaligned kernel and the power ledger

For two distinct reduced cells, (149.20) follows from

\[
 (L_1,r_1)=1,\quad(L_2,r_2)=1,\quad(r_1,r_2)=1:
\]

indeed \(\delta\equiv L_1r_2\pmod{r_1}\) and
\(\delta\equiv-L_2r_1\pmod{r_2}\).  Equations
(149.19)--(149.21) follow immediately.  Choosing \(k\) as in
(149.11), the phase difference is \(e(d\rho/(hr_1r_2))\).  The
literal nonaligned coefficient kernel is therefore

\[
\boxed{
\begin{aligned}
 \mathcal K_U(1,2):={}&
 \sum_{d\asymp D}\mu^2(d)
 \frac{B_{d,U}(L_1)\overline{B_{d,U}(L_2)}}{L_1L_2}\\
 &\quad\times
 \mathscr W_{d,U}(L_1/q_{0,1})
 \overline{\mathscr W_{d,U}(L_2/q_{0,2})}
 e\!\left(\frac{d\rho}{hr_1r_2}\right).
\end{aligned}}
\tag{149.51}
\]

The two outer mod-four factors are
\(\chi_4(L_1q_{0,1}L_2q_{0,2})\) and remain in the signed sum over
cell pairs.

If the coefficient in (149.51) were independent of \(d\) and the
squarefree restriction were absent, the interval kernel would obey

\[
 \left|\sum_{d\asymp D}e(d\rho/(hr_1r_2))\right|
 \ll \min\left(D,\frac{hr_1r_2}{|\rho|}\right).
\tag{149.52}
\]

This is \(D\) throughout the near collar (149.12).  Formula (149.52)
does not apply verbatim to (149.51).  The obstruction is already
visible in (149.22), and (149.34) makes it complete: divisors of
\(d_{\mathrm o}\), primes excluded from \(d\), the exact prefix, and
the profile all move with \(d\).  Expanding only squarefreeness gives

\[
 \mu^2(d)=\sum_{\gamma^2\mid d}\mu(\gamma),
\tag{149.53}
\]

so even before expanding the two \(B\)'s, (149.52) is replaced by a
sum of geometric kernels at frequencies \(\gamma^2\rho/(hr_1r_2)\).
Expanding (149.34) then adds forced divisors, excluded primes, and two
finite progression indicators.  This is the squarefree-progression
self-return, not a fixed-vector large-sieve hypothesis.

For scale comparison, (149.36)--(149.37) give the exact coefficient
capacities

\[
 \sum_{L,q_0}|A_d(L,q_0)|^2\ll_\varepsilon QX^\varepsilon,
\qquad
 \sum_{L,q_0}|A_d(L,q_0)|
 \ll_\varepsilon Q\sqrt E X^\varepsilon
 \asymp R^2\sqrt D X^\varepsilon.
\tag{149.54}
\]

The complete power ledger is as follows.  Every adverse row is an
upper capacity for the indicated proof placement, not a lower bound
for the actual signed energy.

| Placement | Energy capacity | Ratio to \(R^2D\) | Scalar loss after (149.38) |
|---|---:|---:|---:|
| literal equal cell | \(DQ\) | \(D/\sqrt M\leq1\) | none |
| all exact \(N\)-alignments | \(DQX^\varepsilon\) | \(D/\sqrt M\leq1\) | none |
| reduced additive denominator \(\leq Y\) | \(DY^2X^\varepsilon\) | \((Y/R)^2\) | none for \(Y\leq R\) |
| full row triangle from (149.54) | \(R^4D^2X^\varepsilon\) | \(R^2D\) | \(R\sqrt D\) |
| optimistic fixed-vector, unwrapped determinant spacing | \(Q(D+M)X^\varepsilon\) | \(\leq1+\sqrt M\) | \(M^{1/4}\) |
| classical spacing of all distinct rational phases | \(Q(D+(EQ)^2)X^\varepsilon=Q(D+NM)X^\varepsilon\) | \(\leq1+N\sqrt M\) | \(R^2M^{1/4}\) |

For the fifth row, an unwrapped pair has \(k=0\) and
\(|\Delta|\geq1\), so

\[
 \left|\frac{N\Delta}{q_{0,1}q_{0,2}}\right|
 \gg \frac1M
\tag{149.55}
\]

at the largest allowed \(L_i\asymp E\).  Thus the optimistic spacing
price is \(D+M\).  Its off-diagonal term is

\[
 QM\asymp DR^2\sqrt M,
\tag{149.56}
\]

which is \(\sqrt M\) times the target energy.  Wrapped pairs have
\(k\ne0\) in (149.11); after exact duplicates are grouped, two
distinct rational phases with denominators at most
\(q_0\ll EQ\) can still be only \((EQ)^{-2}\asymp(NM)^{-1}\)
apart.  This gives the sixth, weaker row.  The nonzero collar
(149.12) is exactly where the hoped-for \(d\)-oscillation does not
supply a geometric saving even in the frozen-coefficient diagnostic.

The aspect checks are consistent and exhaustive:

- If \(D\asymp E\asymp\sqrt M\), then \(Q\asymp R^2\); the literal
  diagonal may saturate the target, while (149.56) still loses
  \(\sqrt M\).
- If \(D=1\), then \(E\asymp M\) and
  \(Q\asymp R^2/\sqrt M\).  The diagonal and exact alignments are
  safe, but (149.10) is a one-row assertion and no \(d\)-large-sieve
  cancellation exists.
- At the top \(M=R^2\), \(Q\asymp DR\).  The diagonal ratio is
  \(D/R\leq1\), while the optimistic unwrapped energy loses \(R\)
  and its scalar consequence loses \(R^{1/2}\).
- At the most balanced lower aspect \(M\asymp D^2\), one has
  \(Q\asymp R^2\); the diagonal is again exactly at its largest legal
  ratio, while the unwrapped loss is \(D=\sqrt M\).
- These identities cover every \(M\leq R^2\), not only the crossover
  or top dyadic block.

Thus the exact Euler compression repairs the Round-148 early-diagonal
loss and proves the desired coefficient norm, but it does not by
itself supply the signed nonzero near-collision theorem.

## 4. First doubtful or unproved step

The first unproved step is a coefficient-sensitive estimate for the
sum of (149.51), with the outer
\(\chi_4(L_1q_{0,1}L_2q_{0,2})\) retained, over

\[
 r_i=\frac{q_{0,i}}h,\qquad
 q_{0,i}\asymp L_iQ,\qquad
 (L_i,q_{0,i})=1,
\]

and especially over the exact nonzero collar

\[
 0<|N(L_1r_2-L_2r_1)-khr_1r_2|
 \leq \frac{hr_1r_2}{D}.
\tag{149.57}
\]

The zero value is target-safe by (149.48).  The small individual
additive denominators are target-safe by (149.49)--(149.50).  What
remains has large individual reduced denominators but may have a very
small *difference* denominator through (149.57).  Large
\((q_{0,1},q_{0,2})\), imprimitive factors shared with \(N\), and
wrapped integers \(k\ne0\) are all structural.

There are two lawful ways forward, neither present in the permitted
context:

1. Prove a joint squarefree/coprime additive theorem for (149.51),
   uniform in the actual finite prefix and profile, which gives enough
   cancellation between the near collar and its generic complement
   before either is made positive.
2. Perform a further exact Euler recombination and prove the resulting
   signed correlation.  Only after complete recombination may it be
   compared with the Round-147 powerful \(H\)-correlation.

The square norm (149.7), diagonal (149.8), and exact alignment bound
(149.9) do not imply such a theorem.  A classical large sieve cannot
be quoted with \(A_d(L,q_0)\) as though it were independent of \(d\).
Conversely, the adverse capacities in the last two rows of the table
are not signed lower bounds and do not refute the possibility of the
required cancellation.

## 5. Control tests and outcomes

1. **`exact_progression_coefficient_collapse` -- pass.**
   Equations (149.15), (149.22), and the local table prove (149.2)
   exactly.

2. **`p_divides_d_square_local_cancellation` -- pass, with the even-
   \(d\) correction.**  At every odd \(p\mid d_{\mathrm o}\), the
   exponent-two coefficient is \(-1+1=0\).  The prime \(2\) is absent
   because \(\alpha,b,n,q\) are odd.  Thus \(C_{2d_{\mathrm o}}=C_{d_{\mathrm o}}\)
   on odd \(n\).

3. **`finite_nonempty_progression_prefix_indicator` -- pass.**
   Equation (149.14) is retained literally in (149.23), (149.3), and
   (149.34).  No continuous replacement is made.  The norm uses only
   \(|\kappa|\leq1\).

4. **`gcd_lift_character_phase_profile_recombination` -- pass.**
   Equations (149.26)--(149.28) show the character cancellation,
   reduced phase, invariant saddle profile, support, amplitude, and
   finite lift sum.

5. **`truncated_lift_square_norm` -- pass.**  The exact cube-free
   parametrization (149.29)--(149.34) gives (149.36), uniformly for
   every prefix and even or odd squarefree \(d\).

6. **`joint_d_energy_target_normalization` -- pass as a reduction.**
   Equation (149.38) proves that (149.10) implies the \(RD\) target.
   The energy itself remains open.

7. **`literal_equal_cell_diagonal` -- pass.**  Equation (149.39) gives
   \(DQX^\varepsilon\), and (149.40) gives \(Q\leq R^2\).

8. **`offdiagonal_determinant_and_near_collision` -- exact
   classification pass; nonzero estimate open.**  Equations
   (149.17)--(149.21) and (149.51), (149.57) retain the determinant,
   common divisor, centered integer, near collar, and generic sector.

9. **`N_dependent_exact_alignments` -- pass.**  Equations
   (149.41)--(149.48) bound every exact phase class by
   \(DQX^\varepsilon\), including distinct aligned cells.  No
   assertion is made that only equal fractions align.

10. **`common_divisor_and_imprimitive_denominator` -- pass as exact
    bookkeeping.**  The factor \(h\) cancels only once in (149.19),
    (149.20) forces \(r_1r_2\mid N\) at exact alignment, and the
    remaining condition on \(h\) is (149.21).  Original gcd lifts stay
    in \(B\); additive imprimitive factors stay in (149.41).

11. **`d_dependent_arithmetic_coefficient` -- obstruction.**
    Equations (149.22), (149.34), and (149.51)--(149.53) prove that the
    coefficient vector moves arithmetically with \(d\).  The classical
    fixed-vector large sieve is therefore only the diagnostic in the
    power table.

12. **`all_M_D_E_Q_power_ledger` -- pass as a complete adverse
    ledger.**  Equations (149.40), (149.54)--(149.56) and the table
    distinguish diagonal, exact alignment, low reduced denominator,
    row triangle, unwrapped spacing, and fully wrapped rational
    spacing.  No adverse upper capacity is called a lower bound.

13. **`D1_L1_qdividesN_prime_and_prefix_controls` -- pass/open split.**
    At \(D=1\), (149.34) becomes
    \[
      B_{1,U}(ab^2)=\frac{\mu(ab)}a
      \sum_{\substack{v'\ \mathrm{squarefree}\\(v',ab)=1}}
      \frac{\mu(v')}{(v')^2}
      \kappa_{1,U}((abv')^2),
    \]
    so the actual signed \(q_0\)-sum remains, with no \(d\)-average.
    At \(L=1\),
    \[
      B_{d,U}(1)=
      \sum_{u\mid d_{\mathrm o}}\frac{\mu(u)}u
      \sum_{\substack{v\ \mathrm{squarefree}\\(v,d)=1}}
      \frac{\mu(v)}{v^2}\kappa_{d,U}(uv^2),
    \]
    which is still \(d\)-dependent.  The family \(q_0\mid N\) is the
    \(r=1\) part of (149.48) and is safe.  Odd primes obey (149.22),
    even squarefree \(d\) obey (149.1)--(149.2), and short prefixes are
    covered uniformly by (149.36); a prefix already peeled by the
    Round-148 short-collar owner is not assigned any new lower mass.

14. **`H_interface_and_transform_self_return` -- retained mismatch.**
    The compressed \(L\) in (149.5) is cube-free, not necessarily
    powerful, and \(B_{d,U}(L)\) contains an irregular finite prefix.
    It cannot be identified termwise with the Round-147 powerful
    \(H\)-index.  Expanding (149.53) or applying a second canonical
    transform returns squarefree progressions or the original
    square-root phase; neither operation supplies cancellation by
    itself.

15. **`Round138_cross_tge2_and_downstream_scope` -- retained open.**
    This report treats only the retained \(t=1\) reciprocal scalar.
    Every \(t\geq2\) layer, the independent Round-138 cross owner,
    lower GAR, M9--M1, M9--M2, endpoint uniformity, M9, the bridge, the
    quarter target, and both global exponent statements remain outside
    the result.

No numerical experiment and no external theorem were used.

## 6. Dependencies and exact artifacts used

The derivation used only the selected context authorized in the task:

- `protocol.md`;
- `state/proof_obligations.yml`, in particular the four target nodes
  and their accepted Round-147/Round-148 interfaces;
- `state/active_campaign.yml`, including the corrected
  \(d_{\mathrm o}=d/(d,2)\) convention;
- `strategy/round149_gcd_lift_energy_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/signed_squarefree_reciprocal_attack.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reviews/conductor_round148_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/controls/conductor_round148_controls.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/candidates/conductor_round147_t1_squarefree_voronoi_and_H_no_go.md`.

The Round-148 transform, its unit, support, collars, and \(K=6\)
remainder were treated as accepted input.  The local lcm formula,
finite gcd-lift identity, lift parametrization, square norm, exact
phase-class bound, and all new power translations were derived here.

## 7. Recommended state effect

Subject to independent seam review, promote as candidate mathematics:

1. the parity-correct exact formula (149.2), with
   \(d_{\mathrm o}=d/(d,2)\), the odd-prime square cancellation, and
   absent prime \(2\);
2. the finite identities (149.3)--(149.5) and the exact lift formula
   (149.34), with the literal prefix retained;
3. the uniform square norm and \(\ell^1\) bound (149.7);
4. the joint-energy normalization, literal diagonal, complete exact
   alignment, and low reduced-denominator bounds
   (149.8)--(149.10), (149.48)--(149.50); and
5. the exact nonzero near-collision kernel (149.51), together with the
   scoped fixed-vector/spacing no-go and complete power ledger.

Retain the target energy (149.10), the \(RD\) scalar bound, and every
strict owner-complete range as open.  Record the no-go only for the
placement that tries to pass from the coefficient norm and safe
diagonal to the full energy through a classical \(d\)-independent
large sieve or a separately positive spacing ledger.  Do not record it
as a lower bound or as an impossibility theorem for the actual signed
row.

The next lawful attack is the nonzero moving-coefficient correlation
(149.57), with exact alignments removed and the actual
\(\chi_4\), squarefree, coprime, prefix, common-divisor, and profile
data retained.  The alternative is a complete Euler recombination
followed by a genuinely signed theorem; no termwise map to the
Round-147 powerful \(H\)-index is authorized.
