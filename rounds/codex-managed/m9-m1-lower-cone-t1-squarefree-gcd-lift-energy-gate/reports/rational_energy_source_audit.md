# Round 149 primary-source audit of the compressed rational energy

## 1. Result: the literal joint energy remains open

**Result (`gcd_lift_energy_no_go`).**  The exact gcd-lift compression has
two useful positive properties:

\[
 \sum_L\frac{|B_{d,U}(L)|^2}{L}\ll (\log X)^3\ll_\varepsilon
 X^\varepsilon
 \tag{149.1}
\]

uniformly in the squarefree integer \(d\asymp D\), including even \(d\),
and its literal equal-cell contribution to the proposed energy is

\[
 \mathcal E_U^{\mathrm{eq}}\ll DQX^\varepsilon
 \le R^2DX^\varepsilon.
 \tag{149.2}
\]

Neither statement, however, controls the non-equal-cell Gram matrix.  None
of the audited primary rational-large-sieve, squarefree-progression,
Kloosterman-fraction, or dispersion theorems applies to that literal
matrix.  The **first exact source seam** is coefficient independence:
Montgomery--Vaughan's large sieve, including its dual form, has one common
coefficient vector, whereas the compressed coefficient

\[
 a_{d;(L,q_0)}=
 \frac{\chi_4(Lq_0)}{L}B_{d,U}(L)
 W_{d,U}(L/q_0)
 \tag{149.3}
\]

depends genuinely and jointly on \(d\) and the rational cell \((L,q_0)\).
The dependence comes from the divisors of the odd part
\(d_o=d/(d,2)\), the exact finite-prefix indicator, and the moving profile.
It is present before any spacing or power estimate is invoked.

Even after making the illegal separable replacement
\(a_{d;(L,q_0)}\rightsquigarrow b_{(L,q_0)}\), raw rational spacing gives
at best

\[
 (D+E^2Q^2)QX^\varepsilon
 \asymp(D+MR^4)QX^\varepsilon,
 \tag{149.4}
\]

whose ratio to \(R^2D\) is

\[
 \frac D{\sqrt M}+R^4\sqrt M.
 \tag{149.5}
\]

Even optimistic determinant-two Farey spacing at \(L\asymp E\) costs
\((D+M)Q\), with ratio \(D/\sqrt M+\sqrt M\), losing a factor as large
as \(R\).  Exact \(N\)-dependent phase alignments and near alignments can
only make a spacing-only argument less favorable.

Thus the audited sources do **not** prove

\[
 \mathcal E_U:=\sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll R^2DX^\varepsilon,
 \tag{149.6}
\]

and hence do not prove 
\(|T|\ll RDX^\varepsilon\) through this gate.  This is a rigorous
source-applicability and direct-specialization no-go, not a lower bound for
the actual signed energy and not an impossibility theorem for a new
coefficient-sensitive method.

## 2. Exact statement and hypotheses

### 2.1 Frozen compressed object and corrected parity

Throughout,

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor\asymp R^4,
 \qquad DE\asymp M\le R^2,\qquad D\le\sqrt M,
 \tag{149.7}
\]

\[
 E=\frac MD,\qquad
 Q=D\sqrt{N/M}\asymp\frac{DR^2}{\sqrt M}.
 \tag{149.8}
\]

Consequently

\[
 D\le E,\qquad R\ll Q\ll R^2,
 \qquad EQ\asymp R^2\sqrt M\le R^3.
 \tag{149.9}
\]

The summation variable \(d\) is squarefree but may be even.  Only
\(\alpha,b,\ell,q,g,L,q_0\) are odd.  Put

\[
 d_o=\frac d{(d,2)}.
 \tag{149.10}
\]

The exact lcm coefficient is

\[
 C_d(n)=
 \sum_{\substack{\alpha,b\ {\rm odd}\\
                   \mu^2(\alpha)=\mu^2(b)=1,\ b\mid d_o\\
                   [\alpha^2,b]=n}}
 \mu(\alpha)\mu(b).
 \tag{149.11}
\]

Its prime-local evaluation is

\[
 C_d(n)=
 \begin{cases}
  \mu(u)\mu(v),&n=uv^2,\quad u\mid d_o,\quad
       \mu^2(uv)=1,\quad (v,d_o)=1,\quad u,v\ {\rm odd},\\
  0,&\text{otherwise}.
 \end{cases}
 \tag{149.12}
\]

Equivalently, for an odd prime \(p\),

| local position | exponent of \(p\) in \(n\) | local coefficient |
|---|---:|---:|
| \(p\nmid d_o\) | \(0\) | \(1\) |
| \(p\nmid d_o\) | \(2\) | \(-1\) |
| \(p\mid d_o\) | \(0\) | \(1\) |
| \(p\mid d_o\) | \(1\) | \(-1\) |
| \(p\mid d_o\) | \(2\) | \((-1)+(+1)=0\) |

All other local exponents vanish.  Since \(v\) is odd, the condition
\((v,d_o)=1\) is equivalent to \((v,d)=1\).  The cancellation in the last row is
compulsory.  The prime \(2\) is absent from this ledger; evenness of \(d\)
does not insert a \(2\)-Euler factor into \(C_d\).

Let \(\kappa_{d,U}(n)\in\{0,1\}\) be the exact indicator that the
underlying finite progression is nonempty.  It may be irregular at a short
prefix and is not replaced by a continuous cutoff.  With

\[
 \ell=gL,\qquad q=gq_0,\qquad (L,q_0)=1,
 \tag{149.13}
\]

all four variables being odd, define

\[
 B_{d,U}(L)=\sum_g\frac{C_d(gL)\kappa_{d,U}(gL)}g.
 \tag{149.14}
\]

The common lift cancels from the character and phase:

\[
 \chi_4(gL)\chi_4(gq_0)
 =\chi_4(g)^2\chi_4(Lq_0)=\chi_4(Lq_0),
 \qquad \frac\ell q=\frac L{q_0}.
 \tag{149.15}
\]

The profile depends on \(d,U,L/q_0\), and every remaining \(g\)-dependence
is inside (149.14).  The exact row is

\[
 G_U(d)=
 \sum_{\substack{(L,q_0)=1\\q_0\asymp LQ}}
 \frac{\chi_4(Lq_0)}L B_{d,U}(L)
 W_{d,U}(L/q_0)e\!\left(\frac{NdL}{q_0}\right),
 \tag{149.16}
\]

where \(L\le e_+\ll E\), \(q_0\ll EQ\ll R^3\), and \(W\) is uniformly
bounded on its actual support.  Finally,

\[
 T=\sum_{d\asymp D}\mu^2(d)\frac DdG_U(d).
 \tag{149.17}
\]

Since \(D/d\asymp1\), Cauchy--Schwarz shows that (149.6) implies

\[
 |T|\ll D^{1/2}\mathcal E_U^{1/2}
 \ll RDX^\varepsilon.
 \tag{149.18}
\]

### 2.2 Primary theorem cards

**Montgomery--Vaughan rational large sieve.**  H. L. Montgomery and
R. C. Vaughan, *The large sieve*, Mathematika **20** (1973), 119--134,
[Theorem 1, equations (1.1)--(1.6), pp. 119--120](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf)
([DOI](https://doi.org/10.1112/S0025579300004708)), take points
\(x_1,\ldots,x_J\) distinct modulo one, put

\[
 \delta=\min_{r\ne s}\|x_r-x_s\|>0,
 \tag{149.19}
\]

and prove, for one common complex sequence \(c_n\) on an interval of
length \(H\),

\[
 \sum_{r=1}^J\left|\sum_n c_ne(nx_r)\right|^2
 \le (H+\delta^{-1})\sum_n|c_n|^2
 \tag{149.20}
\]

with their stated endpoint convention.  Their Lemma 1 is the finite
matrix duality principle; the dual consequence still has one common
vector \(b_r\):

\[
 \sum_n\left|\sum_r b_re(nx_r)\right|^2
 \le (H+\delta^{-1})\sum_r|b_r|^2.
 \tag{149.21}
\]

The theorem does not require coefficient smoothness or arithmetic moduli.
It does require a fixed frequency family and a coefficient vector
independent of the variable on the outside of the square.  Exact duplicate
frequencies must first be grouped; they do not supply a positive
\(\delta\).

**Pointwise squarefree additive sum.**  J.-C. Schlage-Puchta,
*The exponential sum over squarefree integers*, Acta Arith. **115**
(2004), 265--268,
[Theorem 3](https://arxiv.org/html/1105.1616v1), defines
\(S_H(\alpha)=\sum_{n\le H}\mu^2(n)e(\alpha n)\).  If integers \(a,q\)
(not required to be reduced) satisfy

\[
 |\alpha q-a|\le q^{-1},
 \tag{149.22}
\]

then

\[
 |S_H(\alpha)|\ll
 H^{1+\varepsilon}q^{-1}+H^\varepsilon q.
 \tag{149.23}
\]

This is a sharp-prefix, pointwise theorem for the exact coefficient
\(\mu^2(n)\).  It contains no average over the outer rational denominator
and no \(n\)- and cell-dependent multiplier.

**Squarefree progressions and their variance.**  The relevant primary
statements are:

1. R. M. Nunes,
   [*Squarefree numbers in large arithmetic progressions*, Theorem 1.1](https://arxiv.org/html/1602.00311v1),
   treats a fixed reduced residue modulo a prime
   \(p\le H^{13/19-\varepsilon}\), with error
   \(O(H/(p(\log H)^A))\).  Theorems 1.2--1.3 in the same paper fix one
   prime \(p\), fixed nonzero finite-field parameters, and estimate
   inverse-square complete-sum bilinear forms.  In the source notation,
   for \(1\le A\le B^2\), \(B<p\), \(|\alpha_m|\le1\), and an interval
   of length \(B\), Theorem 1.2 also assumes \(AB^2<p^2\) and gives
   \[
   \sum_{m\le A}\sum_{n\in\mathcal N}\alpha_mK_2(mn^2)
   \ll p^\varepsilon\|\alpha\|_1^{1/2}\|\alpha\|_2^{1/2}
   A^{1/4}B\left(\frac{A^3B^6}{p^4}\right)^{-1/16},
   \tag{149.24}
   \]
   while Theorem 1.3 assumes \(AB<p^{3/2}\) and gives
   \[
   \sum_{m\le A}\sum_{n\in\mathcal N}\alpha_mK_1(mn)
   \ll p^\varepsilon\|\alpha\|_1^{1/2}\|\alpha\|_2^{1/2}
   A^{1/4}B\left(\frac{A^2B^5}{p^3}\right)^{-1/12}.
   \tag{149.25}
   \]
2. Nunes,
   [*A note on the least squarefree number in an arithmetic progression*, Theorem 1.1](https://arxiv.org/html/1605.03347v1),
   treats a fixed reduced residue modulo a squarefree
   \(p\le H^{25/36-\varepsilon}\), with error
   \(O(H^{1-\delta}/p)\).  Its Lemma 1.3 instead gives, for an arbitrary
   positive \(p\), a unit \(a\pmod p\), \(1\le A\le p^{3/4}\), and
   \(1\le B<p/2\),
   \[
   \#\{m\le A,n\le B:m\equiv a\bar n^2\pmod p\}
   \ll A^{2/3}B^{1/4}p^\varepsilon.
   \tag{149.26}
   \]
3. Nunes,
   [*Squarefree numbers in arithmetic progressions*, Theorems 1.1--1.2](https://arxiv.org/html/1402.0684v2),
   fixes one modulus \(p\le H\) and averages the progression error over
   reduced residue classes.  In particular,
   \[
   \mathcal M_2(H,p)=C\prod_{\ell\mid p}(1+2/\ell)^{-1}H^{1/2}p^{1/2}
   +O\!\left(d(p)H^{1/3}p^{2/3}
   +H^{23/15}p^{-13/15}(\log H)^{15}\right).
   \tag{149.27}
   \]
   Theorem 1.2 correlates the errors at \(a\) and \(ma\) for fixed
   nonzero \(m\), \((m,p)=1\), and has an explicit main term and the same
   error.  The average is over residues, not over changing moduli or over
   the squarefree summation variable.
4. A. P. Mangerel,
   [*Squarefree Integers in Arithmetic Progressions to Smooth Moduli*, Theorem 1.1](https://arxiv.org/html/2008.11163v2),
   assumes \(0<\eta<1/522\), a squarefree \(H^\eta\)-smooth modulus
   \(p\le H^{196/261-\varepsilon}\), and
   \((a,p)\le H^\varepsilon\), and obtains a progression error
   \(O(H^{1-\delta}/p)\).  Theorem 3.1 instead fixes a prime \(p\),
   \(A\in\mathbb F_p^\times\), an additive character \(\psi\), and
   shifts \(h_i,h'_j\), and gives
   \[
   \sum_{B\in\mathbb F_p}\psi(B)
   \prod_iK_2(A,B+h_i;p)
   \prod_j\overline{K_2(A,B+h'_j;p)}
   \ll(r+s)3^{r+s}p^{(r+s+1)/2},
   \tag{149.28}
   \]
   except when \(\psi\) is trivial and the two shift multiplicities are
   congruent modulo \(3\).  Remark 3.2 records that the exactly balanced
   equal-multiplicity case is nonnegative and has no general saving.

The progression variable would be \(d\), so \(H=D\le R\).  Their printed
modulus ranges translate to

\[
 q_*\le D^{13/19-\varepsilon},\quad
 D^{25/36-\varepsilon},\quad
 D^{196/261-\varepsilon},
 \quad\text{or, in (149.27), }q_*\le D.
 \tag{149.29}
\]

All lie inside \(q_*\le D\le R\), a stratum already controlled
elementarily in Section 3.  Moreover, the progression theorems have the
coefficient \(\mu^2(d)\), not (149.3), and their complete sums have an
inverse-square finite-field phase rather than the linear rational phase in
(149.16).

**Kloosterman fractions.**  S. Bettin and V. Chandee,
[*Trilinear forms with Kloosterman fractions*, Theorem 1](https://arxiv.org/html/1502.00769v1),
for independent sequences on \(a\asymp A\), \(m\asymp B\),
\(n\asymp C\), with \((m,n)=1\) and nonzero source frequency
\(\vartheta\), prove

\[
\begin{aligned}
 \sum_{a,m,n}\nu_a\alpha_m\beta_n
 e\!\left(\frac{\vartheta a\bar m}{n}\right)
 \ll{}&\|\nu\|_2\|\alpha\|_2\|\beta\|_2
 \left(1+\frac{|\vartheta|A}{BC}\right)^{1/2}\\
 &\times\left((ABC)^{7/20+\varepsilon}(B+C)^{1/4}
 +(ABC)^{3/8+\varepsilon}(AC+AB)^{1/8}\right).
\end{aligned}
\tag{149.30}
\]

Theorem 2 adds a Jacobi twist but retains independent sequences, an
inverse phase, and odd coprime support.  In the proof of Theorem 1 the
source diagonal is \(\ell_1n_1=\ell_2n_2\), not either the equal-cell
diagonal or the \(N\)-alignment diagonal below.  Remark 1 permits a smooth
phase perturbation under its derivative bounds; it does not turn a joint,
irregular amplitude into three independent sequences.

There is a formal phase dictionary: with \(a=d\), \(n=q_0\),
\(\vartheta=N\), choose \(m\) so that \(mL\equiv1\pmod{q_0}\), and then
\(\bar m\equiv L\pmod{q_0}\).  But \(m\) is determined jointly by
\((L,q_0)\), its dyadic location is uncontrolled, and the amplitude becomes

\[
 \frac{B_{d,U}(L(m,n))W_{d,U}(L(m,n)/n)}{L(m,n)},
 \tag{149.31}
\]

which is not \(\nu_d\alpha_m\beta_n\).  On an \(L\asymp H\) block, even
the optimistic choice \(B\asymp C\asymp HQ\) gives the source conductor
factor

\[
 \left(1+\frac{ND}{H^2Q^2}\right)^{1/2}
 =\left(1+\frac E{H^2}\right)^{1/2}.
 \tag{149.32}
\]

There is no lawful norm or final \(R,M,D,E,Q\) power to attach to
(149.30), because separability fails before its bound can be invoked.

**Recent partially fixed-modulus dispersion.**  T. Wright,
[*Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*, arXiv:2604.25177v2, revised 7 August 2026](https://arxiv.org/html/2604.25177v2),
Theorem 2.1 retains separate coefficient sequences and an inverse fraction,
while allowing a fixed factor in the denominator.  Its convolution
consequence, Corollary 2.2, assumes divisor-bounded independent
\(\alpha_m,\beta_n\), with \(\beta\) satisfying the paper's exact
Siegel--Walfisz condition, \(M_s,N_s\ge2\), and
\(M_sN_s/2\le Z\le4M_sN_s\).  It estimates

\[
 \sum_{q\asymp Q_s\atop(q,a)=1}
 \left|\sum_{Z<mn\le2Z\atop mn\equiv a\ (q)}\alpha_m\beta_n
 -\frac1{\varphi(q)}
 \sum_{Z<mn\le2Z\atop(mn,q)=1}\alpha_m\beta_n\right|
 \ll_A Z(\log Z)^{-A}
 \tag{149.33}
\]

provided one of the following holds:

\[
\begin{array}{ll}
\text{(i)}&e^{(\log Z)^\varepsilon}\le N_s
 \le Q_s^{-33/28}Z^{17/28-\varepsilon},
 \quad1\le|a|\le Z/12;\\
\text{(ii)}&e^{(\log Z)^\varepsilon}\le N_s
 \le Z^{7/90-\varepsilon},\quad
 Q_s\le Z^{45/89-\varepsilon},\quad1\le|a|\le Z/12;\\
\text{(iii)}&e^{(\log Z)^\varepsilon}\le N_s
 \le Z^{101/630-\varepsilon},\quad
 Q_s\le Z^{45/89-\varepsilon},\quad
 1\le|a|\le(Z/4)^{\varepsilon/1000}.
\end{array}
\tag{149.34}
\]

Theorem 2.3 and Corollary 2.4 retain a fixed residue, a convolution or a
truncated divisor coefficient independent of the modulus, a principal
reduced-residue subtraction, and the sum of individual absolute
discrepancies over moduli; Corollary 2.4 also has its printed large-modulus
and truncation ranges.  The literal Gram matrix has no congruence
\(mn\equiv a\pmod q\), no fixed residue, no independent Siegel--Walfisz
sequence, no principal subtraction, and a different placement of the
absolute square.  Its modulus is a varying reduction of
\(q_{0,1}q_{0,2}\), not the single \(q\) in (149.33).  Hence there is no
legal identification of \(Z,M_s,N_s,Q_s\) with the project variables.
As a deliberately non-lawful size diagnostic, taking \(Z\asymp DE=M\)
would put the upper \(L\asymp E\) modulus at

\[
 q_0\asymp EQ\asymp R^2\sqrt M,
 \tag{149.35}
\]

far beyond \(M^{45/89}\) for every \(M\le R^2\).  More importantly, the
coefficient and congruence mismatches occur before this range test.

## 3. Proof and derivation

### 3.1 Exact coefficient collapse and uniform lift norm

For \(p\nmid d_o\), the local choices are \(p\nmid\alpha\), giving
exponent \(0\) with coefficient \(1\), or \(p\mid\alpha\), giving exponent
\(2\) with coefficient \(-1\).  For \(p\mid d_o\), exponent \(1\) comes
only from \(p\mid b,p\nmid\alpha\) and has coefficient \(-1\).  Exponent
\(2\) has the two contributions

\[
 (p\mid\alpha,p\nmid b): -1,
 \qquad (p\mid\alpha,p\mid b): +1,
 \tag{149.36}
\]

which cancel.  Multiplication over odd primes proves (149.12).  Since
\(p=2\) is absent, this proof is unchanged when \(2\mid d\); only the odd
part \(d_o\) enters.

Nonempty support of \(\kappa_{d,U}(gL)\) implies \(gL\le e_+\ll E\).
Using \(|C_d(n)|\le1\) from (149.12), without smoothing the prefix,

\[
 |B_{d,U}(L)|
 \le\sum_{g\le e_+/L}\frac1g
 \le1+\log(e_+/L).
 \tag{149.37}
\]

Therefore

\[
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 \ll\sum_{L\le e_+}\frac{(1+\log(e_+/L))^2}{L}
 \ll(1+\log e_+)^3,
 \tag{149.38}
\]

proving (149.1) uniformly in \(d,U\), all prefix lengths, and all
\(M\le R^2\).

### 3.2 Literal diagonal and the remaining Gram matrix

Let \(r=(L,q_0)\), \(x_r=NL/q_0\pmod1\), and use (149.3).  Expanding
(149.6) gives

\[
 \mathcal E_U=
 \sum_{r_1,r_2}\sum_{d\asymp D}\mu^2(d)
 a_{d;r_1}\overline{a_{d;r_2}}
 e\!\left(dN\left(\frac{L_1}{q_{0,1}}-
                         \frac{L_2}{q_{0,2}}\right)\right).
 \tag{149.39}
\]

For \(r_1=r_2\), the number of admissible \(q_0\asymp LQ\) is
\(O(LQ)\).  Hence (149.1) gives

\[
 \mathcal E_U^{\mathrm{eq}}
 \ll\sum_{d\asymp D}\sum_L
 (LQ)\frac{|B_{d,U}(L)|^2}{L^2}
 \ll DQX^\varepsilon.
 \tag{149.40}
\]

By (149.8),

\[
 \frac{DQ}{R^2D}=\frac Q{R^2}=\frac D{\sqrt M}\le1,
 \tag{149.41}
\]

which proves (149.2).  This is only the equal-cell diagonal.  Distinct
cells can have equal frequency modulo one and form a separate arithmetic
alignment diagonal.

For the off-diagonal put

\[
 \Delta=L_1q_{0,2}-L_2q_{0,1},\qquad
 \theta_{12}=\frac{N\Delta}{q_{0,1}q_{0,2}}.
 \tag{149.42}
\]

Exact alignment is

\[
 q_{0,1}q_{0,2}\mid N\Delta,
 \tag{149.43}
\]

and the \(d\)-sum is near-stationary whenever

\[
 0<\|\theta_{12}\|\le D^{-1}.
 \tag{149.44}
\]

All \(L_i,q_{0,i}\) are odd, so \(\Delta\) is even.  If
\(q_{0,1}=hr_1,q_{0,2}=hr_2\), \((r_1,r_2)=1\), then

\[
 \Delta=h(L_1r_2-L_2r_1),
 \qquad
 hr_1r_2\mid N(L_1r_2-L_2r_1)
 \tag{149.45}
\]

is the exact-alignment condition.  Thus a common divisor removes only one
copy of \(h\); factors shared with \(N\) and with the determinant create
further imprimitive reductions.  No coprimality simplification used by a
primitive Farey argument may discard (149.45).

### 3.3 The first source seam and the spacing capacities

The primal large sieve (149.20) would require one sequence \(c_d\)
independent of \(r\).  The dual form (149.21), which has the same
orientation as (149.16), would require one \(b_r\) independent of \(d\).
Neither exists in (149.39).  The dependence is not merely notational: for
an odd prime \(p\), the local coefficient at exponent \(1\) is \(-1\) when
\(p\mid d_o\) and \(0\) when \(p\nmid d_o\).  In addition,
\(\kappa_{d,U}\) and \(W_{d,U}\) move with \(d\).  This proves the first
source seam.

A coefficient-blind matrix extension cannot be inferred from the large
sieve: for arbitrary rows one may take
\(a_{d;r}=u_re(-dx_r)\), cancelling every phase and giving
\(G(d)=\sum_ru_r\).  This is a falsifier only for an arbitrary-matrix
extension; it is not a lower bound for the specific arithmetic array
(149.3).

For scale comparison alone, suppose illegally that \(a_{d;r}=b_r\).
By (149.1),

\[
 \sum_r|b_r|^2\ll
 \sum_L(LQ)\frac{|B(L)|^2}{L^2}
 \ll QX^\varepsilon.
 \tag{149.46}
\]

After grouping exact duplicates, two distinct rational frequencies with
\(q_{0,i}\ll EQ\) have the unconditional spacing

\[
 \|x_{r_1}-x_{r_2}\|\ge
 \frac1{q_{0,1}q_{0,2}}\gg(EQ)^{-2},
 \tag{149.47}
\]

so \(\delta^{-1}\ll E^2Q^2\asymp MR^4\).  Equations
(149.21), (149.46) give (149.4)--(149.5).

Even if \(L_i\asymp E\), \(q_{0,i}\asymp EQ\), and one optimistically
uses the smallest permitted nonzero determinant \(|\Delta|=2\), the
unfolded gap is only

\[
 \frac{N|\Delta|}{q_{0,1}q_{0,2}}\asymp\frac1M.
 \tag{149.48}
\]

This gives the still insufficient capacity

\[
 (D+M)QX^\varepsilon,
 \qquad
 \frac{(D+M)Q}{R^2D}
 =\frac D{\sqrt M}+\sqrt M.
 \tag{149.49}
\]

Modulo-one folding and (149.43)--(149.45) are not priced by this optimistic
calculation.  To reach the target with square mass \(Q\), a separable
large sieve would need an effective spacing/cluster constant at most

\[
 K\le\frac{R^2D}{Q}=\sqrt M,
 \tag{149.50}
\]

whereas (149.48) costs \(M\).  At the balanced endpoint
\((M,D,E,Q)=(R^2,R,R,R^2)\), (149.49) loses \(R\).

### 3.4 Small reduced denominators and additive squarefree sources

For one cell, since \((L,q_0)=1\), the reduced denominator of
\(NL/q_0\) is

\[
 q_* =\frac{q_0}{(q_0,N)}.
 \tag{149.51}
\]

For fixed \(L\), if \(q_*\le Y\), write \(h=(q_0,N)\) and
\(q_0=hq_*\).  There are at most \(Y\tau(N)\) possibilities.  By
Cauchy--Schwarz and (149.1),

\[
 \sum_L\frac{|B_{d,U}(L)|}{L}
 \le\left(\sum_L\frac{|B_{d,U}(L)|^2}{L}\right)^{1/2}
     \left(\sum_{L\le e_+}\frac1L\right)^{1/2}
 \ll X^\varepsilon.
 \tag{149.52}
\]

Therefore the scalar contribution to (149.17) from all
\(q_*\le Y\) is

\[
 \ll DY X^\varepsilon.
 \tag{149.53}
\]

It is already within \(RDX^\varepsilon\) for every \(Y\le R\).
Thus all ranges in (149.29), including Nunes's variance range
\(q_*\le D\), lie in an elementary target-safe stratum.  Their special
prime, squarefree, or smooth-modulus hypotheses only reduce that stratum.
They do not address \(q_*>R\), where the project needs cancellation.

Schlage-Puchta is also not literal because the coefficient in \(d\) is
\(\mu^2(d)a_{d;r}\), not \(\mu^2(d)\).  If this dependence is again
discarded and one chooses the exact denominator \(q_*\) in (149.23), then
for fixed \(L\) in a generic coprime-denominator block the aggregation is

\[
 \frac{|B(L)|}{L}
 \sum_{q_0\asymp LQ}\left(\frac D{q_0}+q_0\right)X^\varepsilon
 \ll |B(L)|\left(\frac DL+LQ^2\right)X^\varepsilon.
 \tag{149.54}
\]

Already at \(L=1\) this has capacity \(D+Q^2\), whose ratio to the scalar
target \(RD\) is

\[
 \frac1R+\frac{Q^2}{RD}
 =\frac1R+\frac{R^3}{E}.
 \tag{149.55}
\]

For \(q_*\le\sqrt D\), exact multiples can place the approximating
denominator near \(\sqrt D\) and improve the pointwise estimate to
\(D^{1/2+\varepsilon}\); that entire range is already contained in
(149.53).  For larger \(q_*\), the other legal approximants in (149.22)
are not jointly selected or aggregated by the cited theorem.  Hence
(149.54) is a failed direct specialization, not an exhaustive no-go for
every Diophantine approximant.

The finite-field theorems (149.24)--(149.28) do not repair this gap.
They fix one modulus and use an inverse-square phase, or average residue
classes at one modulus.  Completing the linear \(d\)-phase in (149.39)
instead gives geometric or Ramanujan sums.  Their source diagonals and
averaging axes are therefore different from both (149.40) and
(149.43).

### 3.5 Boundary and interface controls

At \(L=1\), every \(q_0\mid N\) has \(x_r=0\), so

\[
 e(Nd/q_0)=1.
 \tag{149.56}
\]

There are only divisor-many such cells, but they must be retained in the
exact alignment diagonal rather than declared separated.  More generally,
(149.43) retains all \(N\)-dependent equalities and (149.44) all near
equalities.

At \(D=1\), the equal-cell bound is \(QX^\varepsilon\le R^2X^\varepsilon\),
but there is no averaging cancellation in \(d\); this is a sharp control
against silently using a \(d\)-large-sieve gain.  When \(d\) is even,
\(C_d=C_{d_o}\) at the lcm level, but \(\kappa_{d,U}\) and \(W_{d,U}\)
may still distinguish \(d\), and no factor at \(2\) is inserted.

The norm proof (149.37)--(149.38) accepts an arbitrarily short and
irregular exact prefix.  The progression sources accept a sharp initial
interval only for their pure squarefree sequence; Bettin--Chandee accepts
arbitrary *separate* sequences and a controlled smooth phase perturbation.
Neither fact permits smoothing or separating
\(\kappa_{d,U}(gL)W_{d,U}(L/q_0)\).

Finally, the Round-147 \(H\)-correlation is an alternative only after an
exact Euler recombination.  No termwise map from \(L\) or the lcm to a
powerful \(H\)-index is available.  The natural reciprocal band has width
\(LQ\), while the formal \(H\)-band inherited from the earlier interface
has width \(LQ/D\); the complementary band remains unowned.  The Round-138
signed Farey cross-owner and every \(t\ge2\) layer are independent and are
not changed by this report.

The complete power ledger is:

| route | bound or required constant | ratio to the relevant target | status |
|---|---:|---:|---|
| exact compressed lift norm | \((\log X)^3\) | \(X^\varepsilon\) | proved uniformly |
| literal equal-cell energy | \(DQX^\varepsilon\) | \(D/\sqrt M\le1\) versus \(R^2D\) | target-safe |
| small reduced denominators \(q_*\le Y\) | \(DYX^\varepsilon\) | \(Y/R\le1\) versus \(RD\), for \(Y\le R\) | target-safe scalar stratum |
| raw separable rational large sieve | \((D+MR^4)QX^\varepsilon\) | \(D/\sqrt M+R^4\sqrt M\) | illegal coefficient; non-saving power |
| optimistic determinant-two separable sieve | \((D+M)QX^\varepsilon\) | \(D/\sqrt M+\sqrt M\) | illegal coefficient; loses up to \(R\) |
| required separable cluster constant | \(K\le\sqrt M\) | determinant scale gives \(K\asymp M\) | missing \(\sqrt M\) gain |
| Schlage-Puchta exact-denominator diagnostic, \(L=1\) | \(D+Q^2\) | \(R^{-1}+R^3/E\) versus \(RD\) | illegal coefficient; non-saving direct specialization |
| Bettin--Chandee conductor on \(L\asymp H\) | \((1+E/H^2)^{1/2}\) | no lawful coefficient norm | separability fails first |
| Wright upper-lift size diagnostic with \(Z=M\) | \(q_0\asymp R^2\sqrt M\) | far beyond \(M^{45/89}\) | no legal congruence map; range also fails |

No numerical experiment was used.

## 4. First doubtful or unproved step

The first unproved mathematical step after the valid compression is the
off-diagonal estimate in (149.39), with its literal coefficient

\[
 \mu^2(d)B_{d,U}(L_1)\overline{B_{d,U}(L_2)}
 W_{d,U}(L_1/q_{0,1})
 \overline{W_{d,U}(L_2/q_{0,2})}.
 \tag{149.57}
\]

The first exact **source** obstruction occurs even earlier than spacing:
Montgomery--Vaughan Theorem 1 and its duality lemma permit one common
coefficient vector, while (149.57) is a genuine \(d\)-dependent matrix.
No cited theorem authorizes replacing it by a row norm or by a separable
analogue.  If that seam is ignored, the next quantitative obstruction is
the gap between the required effective cluster constant \(\sqrt M\) and
the optimistic Farey cost \(M\), followed by the exact and near
\(N\Delta/(q_{0,1}q_{0,2})\) alignments.

The source-legal conclusion is deliberately narrow: the audited direct
applications do not prove (149.6).  The report does not prove that the
arithmetic \(d\)-dependence is adversarial, does not give a lower bound for
\(\mathcal E_U\), and does not exclude a new matrix-valued rational large
sieve, a successful exact Euler recombination, or a direct count of the
alignment fibers retaining the actual signs.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_progression_coefficient_collapse` | **Pass.** Equations (149.11)--(149.12) give the exact Euler-local coefficient.  The \(p\mid d_o, p^2\mid n\) contributions cancel. |
| `gcd_lift_character_phase_profile_recombination` | **Pass.** Equations (149.13)--(149.16) cancel \(\chi_4(g)^2\) and \(g\) from the fraction while retaining all remaining \(g\)-dependence in \(B_{d,U}\). |
| `truncated_lift_square_norm` | **Pass.** Equations (149.37)--(149.38) prove the uniform \(L^{-1}\ell^2\) norm without smoothing \(\kappa_{d,U}\). |
| `joint_d_energy_target_normalization` | **Pass as normalization; estimate open.** Equations (149.17)--(149.18) show exactly why \(R^2D\) implies \(RD\). |
| `literal_equal_cell_diagonal` | **Pass.** Equations (149.40)--(149.41) give \(DQX^\varepsilon\le R^2DX^\varepsilon\) using the actual \(d\)-dependent coefficient. |
| `offdiagonal_determinant_and_near_collision` | **Retained, unresolved.** Equations (149.42)--(149.44) retain \(\Delta\), exact congruence, and the \(D^{-1}\) near window. |
| `N_dependent_exact_alignments` | **Retained.** Equation (149.43), including \(L=1,q_0\mid N\) in (149.56), is not absorbed into an equal-cell or separated-frequency claim. |
| `common_divisor_and_imprimitive_denominator` | **Pass as exact ledger; estimate open.** Equation (149.45) displays the surviving common factor and all possible reductions through \(N\) and the determinant. |
| `d_dependent_arithmetic_coefficient` | **Source fail at the first seam.** The local \(p\mid d_o\) rule, exact prefix, and profile make (149.3) joint in \(d,r\); neither orientation of Montgomery--Vaughan applies.  Even squarefree \(d\) is handled by \(d_o\), with \(p=2\) absent. |
| `source_theorem_energy_match` | **No match.** Montgomery--Vaughan fails coefficient independence; squarefree progression results have the wrong coefficient/range/average; Nunes--Mangerel complete sums have the wrong phase and diagonal; Bettin--Chandee/Wright require inverse phases or independent convolution coefficients and different absolute-value placement. |
| `all_M_D_E_Q_power_ledger` | **Pass as a capacity audit.** Equations (149.4)--(149.5), (149.49)--(149.50), (149.53)--(149.55), and the final table retain every \(M\le R^2\), \(D\le\sqrt M\), \(E=M/D\), \(Q=DR^2/\sqrt M\). |
| `D1_L1_qdividesN_prime_and_prefix_controls` | **Pass as controls.** \(D=1\) supplies no hidden \(d\)-average; \(L=1,q_0\mid N\) is retained; odd primes dividing \(d_o\), even \(d\), and arbitrary short prefixes are all explicit. |
| `H_interface_and_transform_self_return` | **No transfer.** The \(H\)-route requires exact Euler recombination, powerful support, and its narrower \(LQ/D\) band; no termwise lcm map is used. |
| `Round138_cross_tge2_and_downstream_scope` | **No effect.** The independent Round-138 cross owner, every \(t\ge2\) layer, the M9 parent, bridge, quarter estimate, and exponent remain unchanged. |

## 6. Dependencies and exact artifacts used

Repository context used, exactly as assigned:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round149_gcd_lift_energy_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/squarefree_progression_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reviews/source_conductor_round148_final.md`;
- `rounds/codex-managed/m9-m1-joint-reciprocal-large-sieve/reports/conductor_signed_reciprocal_energy_analysis.md`;
- `rounds/codex-managed/m9-m1-joint-reciprocal-large-sieve/reports/conductor_RSLS_source_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/candidates/conductor_round138_scalar_rows_and_resonance_fibres.md`;
- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/candidates/conductor_round139_curvature_collar_and_quadratic_obstruction.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/briefs/rational_energy_source_audit.md`.

Primary technical sources checked:

- Montgomery and Vaughan, [*The large sieve*](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf), Theorem 1 and Lemma 1;
- Schlage-Puchta, [*The exponential sum over squarefree integers*](https://arxiv.org/html/1105.1616v1), Theorem 3;
- Nunes, [*Squarefree numbers in large arithmetic progressions*](https://arxiv.org/html/1602.00311v1), Theorems 1.1--1.3;
- Nunes, [*A note on the least squarefree number in an arithmetic progression*](https://arxiv.org/html/1605.03347v1), Theorem 1.1 and Lemma 1.3;
- Nunes, [*Squarefree numbers in arithmetic progressions*](https://arxiv.org/html/1402.0684v2), Theorems 1.1--1.2;
- Mangerel, [*Squarefree Integers in Arithmetic Progressions to Smooth Moduli*](https://arxiv.org/html/2008.11163v2), Theorems 1.1 and 3.1 and Remark 3.2;
- Bettin and Chandee, [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/html/1502.00769v1), Theorems 1--2 and Remark 1;
- Wright, [*Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*](https://arxiv.org/html/2604.25177v2), Theorem 2.1, Corollary 2.2, Theorem 2.3, and Corollary 2.4.

No secondary source is used for a technical theorem statement.  No sibling
Round-149 report, synthesis, validation matrix, proof draft, or shared-state
edit was used.

## 7. Recommended state effect

**Retain and revise.**  Record only the source-scoped no-go
`gcd_lift_energy_no_go`: the exact compressed coefficient has the uniform
square norm (149.1), and its equal-cell diagonal is target-safe, but no
audited primary theorem controls the literal \(d\)-dependent off-diagonal
energy.  Keep (149.6) and the signed lower radial estimate open.  Make no
change to the accepted graph, proof draft, validation matrices, campaign,
Round-138 owner, \(t\ge2\) layers, downstream bridge, quarter target, or
exponent.

A promotable continuation must either prove a matrix-valued rational
energy theorem that accepts (149.57) and prices (149.43)--(149.45), or
perform an exact owner-preserving Euler recombination that produces a
source-legal independent coefficient family.  A separable surrogate, an
unpaid Farey spacing claim, a fixed-modulus residue variance, or a smoothed
replacement of the exact prefix is insufficient.
