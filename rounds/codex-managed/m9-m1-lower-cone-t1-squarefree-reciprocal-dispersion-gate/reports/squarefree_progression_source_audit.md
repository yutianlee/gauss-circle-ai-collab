# Round 148 primary-source audit of the signed squarefree reciprocal form

## 1. Result: source-hypothesis no-go

**Result (squarefree_reciprocal_dispersion_no_go).** The literal
Round-148 one-sided transform is a signed reciprocal sum, but none of
the audited primary theorems proves its required all-scale bound. This
is a source- and method-specific no-go, not a lower bound for the actual
signed scalar.

On \(d\asymp D\), \(e\asymp E\), \(DE\asymp M\leq R^2\), the smooth
interior stationary term is

$$
\mathcal T_{D,Q}(U)=
\sum_{d\asymp D}\frac Dd\mu^2(d)
\sum_{\substack{u^2\ll E\\u\ {\rm odd}}}\mu(u)
\sum_{v\mid d_o}\mu(v)\frac{\chi_4(\lambda)}{\lambda}
\sum_{\substack{q>0\\q\ {\rm odd}}}
\chi_4(q)\Omega_{d,\lambda,U}(q)
e\!\left(\frac{\lambda Nd}{q}\right),
\quad d_o=\frac d{(d,2)},\quad \lambda=[u^2,v],
\tag{148.1}
$$

where the profile imposes \(q\asymp\lambda Q\) and

$$
Q=D\sqrt{N/M}=\frac{DR^2}{\sqrt M}(1+O(X^{-1})).
\tag{148.2}
$$

The physical contribution is
$$
\frac{e(1/8)}{N^{1/4}D}\mathcal T_{D,Q}(U)
\tag{148.3}
$$
plus retained endpoint, collar, and nonstationary pieces. Hence the
literal transformed target is
$$
|\mathcal T_{D,Q}(U)|\ll_\varepsilon RD X^\varepsilon.
\tag{148.4}
$$

For fixed \((\lambda,q)\), the additive phase in \(d\) has reduced
denominator
$$
q_*=\frac q{(q,\lambda N)}.
\tag{148.5}
$$
The progression theorems below require \(q_*\leq D^\theta\) with
\(\theta<1\) and additionally prime, squarefree, or smooth modulus
hypotheses. Yet the unreduced transformed scale satisfies
$$
\frac{\lambda Q}{D}=\lambda\sqrt{N/M}\geq\lambda R.
\tag{148.6}
$$
Every small-denominator stratum \(q_*\leq Y\leq R\) is already
target-safe by a divisor count, so the pointwise progression ranges
touch only an easy exceptional piece. Choosing the exact reduced
denominator in Schlage-Puchta gives
\(D^{1+\varepsilon}/q_*+q_*D^\varepsilon\), which aggregates in the
favorable coprime case to \(D/\lambda+\lambda Q^2\), not (148.4).
This is only the exact-denominator specialization: exact multiples
already improve it when \(q_*\leq\sqrt D\), and other admissible
approximants for \(q_*>\sqrt D\) are unclassified here. The cited paper
contains no theorem aggregating those choices over the varying outer
\(q\). The Nunes and Mangerel complete sums have a fixed finite-field
modulus and inverse-square phase; Bettin--Chandee has an inverse phase.
None of the quoted theorem interfaces directly matches
\(e(\lambda Nd/q)\) with varying \(q\), and their diagonal terms do not
pay the \(q_1=q_2\) zero phase of dispersion here.

The squarefree analogue of the accepted bare absolute \(Q+D\) estimate
remains open; it is not refuted. An estimate uniform in arbitrary
bounded outer \(q\)-coefficients is false by phase alignment at \(D=1\)
and cannot replace the actual \(\chi_4(q)\)-signed problem.

## 2. Exact statement and hypotheses

The audited face is the dyadic, prefix-uniform form of
$$
S^{(1)}(U)=
\sum_{\substack{d,e\geq1\\M\leq de<U\\
\mu^2(de)=1,\ e\ {\rm odd},\ e>4d}}
(de)^{-3/4}V_{\rm low}\!\left(\frac{R^2de}{N}\right)
\chi_4(e)e(+\sqrt{Nde}),
\tag{148.7}
$$
where \(R=X^{1/4}\), \(N=\lfloor X\rfloor\),
\(M\leq U\leq B_M\leq2M\), \(D\leq\sqrt M\), and \(E\asymp M/D\).
The accepted \(\sqrt D\) cone collar and \(\sqrt M\) radial/prefix
endpoint collars are peeled and retained at physical
\(O(X^\varepsilon)\) cost. Outside them write the complete smooth
weight, including \((de)^{-3/4}\), as \(G_{d,U}(e)\).

Because \(e\) is odd,
$$
\mu^2(de)=\mu^2(d)\mu^2(e){\bf1}_{(d,e)=1},\qquad
\mu^2(e)=\sum_{u^2\mid e}\mu(u),\qquad
{\bf1}_{(d,e)=1}=\sum_{v\mid(d_o,e)}\mu(v).
\tag{148.8}
$$
All Mobius signs remain inside the sum. For
\(\lambda=[u^2,v]\), primitive \(\chi_4\)-Poisson gives the exact
identity
$$
\sum_{\lambda\mid e}\chi_4(e)G_{d,U}(e)e(\sqrt{Nde})
=\frac{i\chi_4(\lambda)}{2\lambda}
\sum_{q\in\mathbb Z}\chi_4(q)
\int_0^\infty G_{d,U}(y)
e\!\left(\sqrt{Ndy}-\frac{qy}{4\lambda}\right)dy.
\tag{148.9}
$$
The positive stationary point is
$$
y_0=\frac{4\lambda^2Nd}{q^2},\qquad
\Phi(y_0)=\frac{\lambda Nd}{q},\qquad
\Phi''(y_0)=-\frac{q^3}{32\lambda^3Nd}.
\tag{148.10}
$$
The actual coupled profile \(\Omega_{d,\lambda,U}(q)\) contains
\(y_0\asymp E\), \(y_0>4d\), \(M\leq dy_0<U\), and
$$
V_{\rm low}\!\left(\frac{4R^2\lambda^2d^2}{q^2}\right).
\tag{148.11}
$$
It is not an arbitrary separable coefficient. The Poisson \(q=0\)
term is killed by \(\chi_4(0)=0\); negative \(q\) is nonstationary.
This does not discard the distinct hard-cone Perron zero mode.

The exact relevant primary theorem cards are as follows.

1. Schlage-Puchta, [The exponential sum over squarefree integers,
   Theorem 3](https://arxiv.org/html/1105.1616v1): if
   \(S_L(\alpha)=\sum_{n\leq L}\mu^2(n)e(\alpha n)\) and
   an integer pair \((a,q)\) satisfies
   \(|\alpha q-a|\leq q^{-1}\), then
$$
   |S_L(\alpha)|\ll L^{1+\varepsilon}q^{-1}+qL^\varepsilon.
   \tag{148.12}
$$
   The approximating pair need not be reduced. The exact reduced
   denominator of a rational frequency is one legal choice, but so are
   its exact multiples and any other pair satisfying the displayed
   inequality. The theorem is pointwise in one additive frequency,
   with no outer \(q\)-average or coupled profile.

2. Nunes, [Squarefree numbers in large arithmetic progressions,
   Theorem 1.1](https://arxiv.org/html/1602.00311v1): for a prime
   modulus \(p\leq L^{13/19-\varepsilon}\), \((a,p)=1\),
$$
   \sum_{\substack{n\leq L\\n\equiv a\ (p)}}\mu^2(n)
   =\frac1{\varphi(p)}\sum_{\substack{n\leq L\\(n,p)=1}}\mu^2(n)
   +O\!\left(\frac{L}{p(\log L)^A}\right).
   \tag{148.13}
$$
   In the same paper,
$$
   S(m,n;p)=\sum_{x\bmod p}^{*}e_p(m\bar x^2+nx),\quad
   K_1(t)=p^{-1/2}S(a,bt;p),\quad K_2(t)=p^{-1/2}S(at,b;p).
   \tag{148.14}
$$
   Theorem 1.2 assumes one fixed prime \(p\), fixed
   \(a,b\in\mathbb F_p^\times\),
   \(1\leq A\leq B^2\), \(B<p\), \(AB^2<p^2\),
   \(|\alpha_m|\leq1\) for \(m\leq A\), and an unweighted interval
   \(\mathcal N\subset[1,p-1]\) of length \(B\), and proves
$$
   \sum_{m\leq A}\sum_{n\in\mathcal N}\alpha_mK_2(mn^2)
   \ll p^\varepsilon\|\alpha\|_1^{1/2}\|\alpha\|_2^{1/2}
   A^{1/4}B\left(\frac{A^3B^6}{p^4}\right)^{-1/16}.
   \tag{148.15}
$$
   Theorem 1.3 assumes the same fixed
   \(a,b\in\mathbb F_p^\times\), \(1\leq A\leq B^2\), \(B<p\),
   \(AB<p^{3/2}\), the same coefficients and interval, and proves
$$
   \sum_{m\leq A}\sum_{n\in\mathcal N}\alpha_mK_1(mn)
   \ll p^\varepsilon\|\alpha\|_1^{1/2}\|\alpha\|_2^{1/2}
   A^{1/4}B\left(\frac{A^2B^5}{p^3}\right)^{-1/12}.
   \tag{148.16}
$$

3. Nunes, [A note on the least squarefree number in an arithmetic
   progression, Theorem 1.1](https://arxiv.org/pdf/1605.03347):
   for squarefree \(q\leq L^{25/36-\varepsilon}\), \((a,q)=1\), the
   analogue of (148.13) has error \(O(L^{1-\delta}/q)\).
   Separately, Lemma 1.3 assumes only an arbitrary positive modulus
   \(q\), a unit residue \(a\in(\mathbb Z/q\mathbb Z)^\times\),
   \(1\leq A\leq q^{3/4}\), and \(1\leq B<q/2\), and bounds
$$
   \#\{m\leq A,n\leq B:m\equiv a\bar n^2\pmod q\}
   \ll A^{2/3}B^{1/4}q^\varepsilon.
   \tag{148.17}
$$
   It is a positive box count at one prescribed general modulus;
   squarefreeness is a hypothesis of Theorem 1.1, not of Lemma 1.3.

4. Nunes, [Squarefree numbers in arithmetic progressions,
   Theorems 1.1--1.2](https://arxiv.org/html/1402.0684v2): with
   \(E(L,p,a)\) the progression error and
   \(\mathcal M_2(L,p)=\sum_{a\bmod p}^{*}|E(L,p,a)|^2\), uniformly
   for \(p\leq L\),
$$
   \mathcal M_2(L,p)=C\prod_{\ell\mid p}(1+2/\ell)^{-1}
   L^{1/2}p^{1/2}
   +O\!\left(d(p)L^{1/3}p^{2/3}
   +L^{23/15}p^{-13/15}(\log L)^{15}\right).
   \tag{148.18}
$$
   Theorem 1.2 correlates \(E(L,p,a)\) with \(E(L,p,ma)\) for fixed
   nonzero \(m\), \((m,p)=1\), with an explicit main term and the same
   error. The average is over residue classes at one fixed modulus and
   contains a genuine diagonal main term.

5. Mangerel, [Squarefree Integers in Arithmetic Progressions to Smooth
   Moduli, Theorem 1.1](https://arxiv.org/html/2008.11163v2): for
   \(0<\eta<1/522\), \(p\leq L^{196/261-\varepsilon}\) both squarefree
   and \(L^\eta\)-smooth, and \((a,p)\leq L^\varepsilon\), the
   progression asymptotic has error \(O_\varepsilon(L^{1-\delta}/p)\).
   The same paper defines
$$
   K_2(A,B;p)=\sum_{x\bmod p}^{*}e_p(A\bar x^2+Bx).
   \tag{148.19}
$$
   Theorem 3.1 fixes a prime \(p\), takes
   \(A\in\mathbb F_p^\times\), a possibly trivial additive character
   \(\psi\), and shifts \(h_i,h'_j\), and proves
$$
   \sum_{B\in\mathbb F_p}\psi(B)
   \prod_{i=1}^{r}K_2(A,B+h_i;p)
   \prod_{j=1}^{s}\overline{K_2(A,B+h'_j;p)}
   \ll(r+s)3^{r+s}p^{(r+s+1)/2},
   \tag{148.20}
$$
   unless \(\psi\) is trivial and the two shift multiplicities are
   congruent modulo \(3\) at every shift. Remark 3.2 notes that equal
   multiplicities give nonnegative summands and no general saving.

6. Bettin--Chandee, [Trilinear forms with Kloosterman fractions,
   Theorem 1](https://arxiv.org/html/1502.00769v1): for arbitrary
   coefficient arrays on \(a\asymp A,m\asymp B,n\asymp C\),
   \((m,n)=1\), and \(\vartheta\ne0\),
$$
   \begin{aligned}
   \sum_{a,m,n}\nu_a\alpha_m\beta_n
   e\!\left(\frac{\vartheta a\bar m}{n}\right)
   \ll{}&\|\nu\|_2\|\alpha\|_2\|\beta\|_2
   \left(1+\frac{|\vartheta|A}{BC}\right)^{1/2}\\
   &\times\left((ABC)^{7/20+\varepsilon}(B+C)^{1/4}
   +(ABC)^{3/8+\varepsilon}(AC+AB)^{1/8}\right).
   \end{aligned}
   \tag{148.21}
$$
   Theorem 2 inserts the Jacobi symbol \((m/n)\), keeps the inverse
   phase and odd coprime support, and gives
   \((BC)^{3/10}(AB+AC)^{7/20+\varepsilon}
   +A^{1/2}(B+C)^{7/8+\varepsilon}\) after the norm and conductor
   factor. Its proof separates the diagonal
   \(\ell_1n_1=\ell_2n_2\).

## 3. Proof and derivation

Since \(\tau(\chi_4)=2i\), residue-class Poisson summation gives
$$
\sum_{n\in\mathbb Z}\chi_4(n)H(n)
=\frac i2\sum_{q\in\mathbb Z}\chi_4(q)\widehat H(q/4).
\tag{148.22}
$$
Taking \(H(x)=G_{d,U}(\lambda x)e(\sqrt{Nd\lambda x})\) and changing
variables proves (148.9). On \(y\asymp E\), (148.10) gives
\(q\asymp\lambda D\sqrt{N/M}=\lambda Q\). Moreover
$$
|\Phi''(y_0)|^{-1/2}
=4\sqrt2\,\lambda^{3/2}(Nd)^{1/2}q^{-3/2},
\quad
(dy_0)^{-3/4}
=2^{-3/2}\lambda^{-3/2}N^{-3/4}d^{-3/2}q^{3/2}.
\tag{148.23}
$$
Multiplication by \(1/(2\lambda)\) leaves
\(N^{-1/4}/(d\lambda)\), with no \(q\)-power. The negative second
derivative contributes \(e(-1/8)\), and
\(ie(-1/8)=e(1/8)\), proving (148.1)--(148.3). The smooth
one-dimensional remainder gains the phase \(\sqrt{NM}\) and is
target-safe after the finite \(u^2\ll E\) and divisor sums. Formula
(148.9) remains exact at every retained boundary.

For fixed \((\lambda,q)\), set
$$
c=\left\lfloor\frac{\lambda N}{q}+\frac12\right\rfloor,\qquad
j=\lambda N-cq,\qquad -q/2\leq j<q/2.
\tag{148.24}
$$
Then
$$
e(\lambda Nd/q)=e(jd/q),\qquad q\mid(\lambda N-j).
\tag{148.25}
$$
A fixed \(j\) has divisor multiplicity at most
\(\tau(|\lambda N-j|)\), with \(\tau(\lambda N)\) at \(j=0\).
In particular \(\lambda=1\) retains \(q\mid N\).

For fixed \(\lambda\), the number of \(q\) with \(q_*\leq Y\) is at
most \(Y\tau(\lambda N)\). Also
$$
\sum_{\substack{u^2\ll E\\u\ {\rm odd}}}\sum_{v\mid d_o}
\frac{|\mu(u)\mu(v)|}{[u^2,v]}\ll X^\varepsilon,
\tag{148.26}
$$
because \([u^2,v]=u^2v/(u,v)\) and both sums factor over primes.
Consequently
$$
\sum_{\substack{d,u,v,q\\u^2\ll E,\ q_*\leq Y}}
\frac Dd\frac1\lambda\ll DY X^\varepsilon.
\tag{148.27}
$$
Thus every \(Y\leq R\), including all three published
\(D^\theta\)-ranges, is already within \(RD X^\varepsilon\).

Applying (148.12) at the exact rational frequency, choosing its exact
reduced denominator \(q_*\), and subtracting two initial sums gives
$$
\sum_{d\asymp D}\mu^2(d)e(\lambda Nd/q)
\ll D^{1+\varepsilon}/q_*+q_*D^\varepsilon.
\tag{148.28}
$$
If \((q,\lambda N)=1\) and \(q\asymp\lambda Q\), summing this
specialization with outer size \(1/\lambda\) gives
\(D/\lambda+\lambda Q^2\). If \(q_*>D\), the pointwise trivial estimate
is better but totals \(QD\). Thus the exact-reduced-denominator
specialization does not reach (148.4).

This is not an exhaustive use of Schlage-Puchta's approximation
condition. If \(q_*\leq\sqrt D\), write the reduced frequency as
\(a_*/q_*\), take
$$
t=\left\lceil\frac{\sqrt D}{q_*}\right\rceil,
\qquad r=tq_*,
\tag{148.28a}
$$
and use the exact pair \((ta_*,r)\). Then
\(\sqrt D\leq r<2\sqrt D\) and
\(|\alpha r-ta_*|=0\), so Theorem 3 gives
$$
\sum_{d\asymp D}\mu^2(d)e(\lambda Nd/q)
\ll D^{1/2+\varepsilon}.
\tag{148.28b}
$$
For \(q_*>\sqrt D\), the other allowable Diophantine approximants have
not been classified in this report. The lawful conclusion is that the
exact-denominator route fails and that the quoted source supplies no
joint theorem for selecting and aggregating the other approximants as
the outer \(q\) varies.

Dispersion of (148.1) produces
$$
e\!\left(\lambda Nd\left(\frac1{q_1}-\frac1{q_2}\right)\right).
\tag{148.29}
$$
The \(q_1=q_2\) diagonal has zero phase; common divisors among
\(q_1,q_2,\lambda N\) create imprimitive strata. Nunes's variance
theorem averages residues at fixed modulus and has its own positive
diagonal. Nunes--Mangerel \(K_2\) correlations require fixed prime
modulus and \(A\bar x^2+Bx\); completion of (148.29) instead produces
geometric or Ramanujan sums. Mangerel Theorem 3.1 explicitly excludes
the balanced diagonal. Bettin--Chandee requires \(\bar m\bmod n\);
replacing \(d\) by \(\bar d\bmod q\) would be a \(q\)-dependent
permutation destroying the dyadic interval and \(\Omega\). These are
phase and averaging mismatches, not weak exponents.

For completeness, fix one sequence \(c_d\) that is independent of
\(q\). In this separable model the elementary large sieve for the
reduced fractions \(\lambda N/q\) gives, using separation
\(\gg(\lambda Q)^{-2}\) and multiplicity
\(\ll\tau(\lambda N)\),
$$
\sum_{q\asymp\lambda Q}
\left|\sum_{d\asymp D}c_de(\lambda Nd/q)\right|^2
\ll X^\varepsilon(D+\lambda^2Q^2)\sum_d|c_d|^2.
\tag{148.30}
$$
For \(|c_d|\leq1\) and
\(\beta_q=\chi_4(q)/\lambda\), Cauchy yields
$$
\left|\sum_q\beta_q\sum_dc_de(\lambda Nd/q)\right|
\ll X^\varepsilon\lambda^{1/2}Q^{3/2}D^{1/2}.
\tag{148.31}
$$
Since \(\lambda Q/D\geq R\), this is worse than trivial \(QD\).
This is only a spacing diagnostic for a fixed, \(q\)-independent inner
coefficient. The literal
\(c_{d,\lambda,q}\) contains
\(\Omega_{d,\lambda,U}(q)\), so (148.30)--(148.31) do not apply to
(148.1) verbatim and spacing alone supplies no coefficient-sensitive
gain.

At \(D=1\), choosing an adversarial outer coefficient conjugate to
\(e(N/q)\) makes the bare sum \(\asymp Q\), whereas the target is
\(R\), and \(Q/R=R/\sqrt M>1\) for \(M<R^2\). Thus the
arbitrary-coefficient analogue is false. This does not test the actual
\(\chi_4(q)\) signs. The squarefree absolute statement
$$
\sum_{q\asymp Q}\left|
\sum_{d\asymp D}\mu^2(d)e(Nd/q)\right|
\stackrel{?}{\ll}(Q+D)X^\varepsilon
\tag{148.32}
$$
remains open: the legal alternatives are (148.28), \(QD\), or the
Mobius-triangle bound \(Q\sqrt D+D\).

The all-scale ledger is:

| Method | Bound | Ratio to \(RD\) |
|---|---:|---:|
| bare absolute average | \(Q+D\) | \(R/\sqrt M+1/R\) |
| expand \(\mu^2(d)\), then triangle | \(Q\sqrt D+D\) | \(R\sqrt D/\sqrt M+1/R\) |
| expand \(\mu^2(e)\), then triangle | \(Q\sqrt E\) | \(R/\sqrt D\) |
| expand both independently | \(Q\sqrt{DE}=DR^2\) | \(R\) |
| pointwise trivial | \(QD\) | \(DR/\sqrt M\) |
| separable \(q\)-independent large-sieve diagnostic (148.31) | \(\lambda^{1/2}Q^{3/2}D^{1/2}\) | \(\lambda^{1/2}DR^2/M^{3/4}\) |

The bare term loses \(R^{1/3}\) at \(M=R^{4/3}\); at
\((M,D,E)=(R^2,R,R)\), the large-sieve ratio is \(R^{3/2}\) for
\(\lambda=1\). These are capacities, not lower bounds.

Finally, Round 147 has \(h_z(k)A_{-z}(kN+j_H)\) with powerful \(k\).
Setting \(k=\lambda\) and \(j_H=-(\lambda N-cq)\) gives
\(kN+j_H=cq\), but not a coefficient identity:
\(\lambda=[u^2,v]\) need not be powerful because \(v\) may contribute
a prime to the first power. Powerful support appears only after exact
Euler recombination. There is also an independent bandwidth mismatch.
The reciprocal nearest-integer coordinate only gives
$$
|j|<q/2\asymp\lambda Q,
\tag{148.32a}
$$
whereas the formal \(H\)-choice \(k=\lambda\) has
$$
|j_H|\lesssim k\sqrt{N/M}
=\frac{\lambda Q}{D}.
\tag{148.32b}
$$
Only a \(D^{-1}\)-thin part of the natural reciprocal \(j\)-range lies
in the \(H\)-band, and no estimate here owns
\(\lambda Q/D\ll|j|<\lambda Q/2\). No audited source identifies the
coefficients or repairs this bandwidth mismatch.

## 4. First doubtful or unproved step

The first unproved arithmetic step is the coefficient-sensitive signed
estimate (148.4) for (148.1), with the \(u,v\) Mobius signs and the
actual \(\chi_4(q)\Omega_{d,\lambda,U}(q)\). No audited theorem has
simultaneously the varying modulus, linear reciprocal phase, fixed
numerator, signed outer coefficient, squarefree/coprime inner
coefficient, dyadic interval, moving prefix, and paid diagonal.

The first exact source obstruction for the pointwise progression
theorems is the reduced-modulus/range mismatch:
\(q_*\leq D^\theta\), \(\theta<1\), with special modulus families,
lies wholly inside the target-safe stratum (148.27). The
exact-denominator specialization of Schlage-Puchta fails by
(148.28), but exact multiples improve it for \(q_*\leq\sqrt D\), and
the other approximants for \(q_*>\sqrt D\) remain unclassified. The
lawful terminal source conclusion is therefore narrower: none of the
quoted theorem interfaces or the direct specializations audited here
supplies the actual varying-\(q\), profile-coupled signed form. This is
not an exhaustive no-go for every possible use of Schlage-Puchta.
The complete-sum theorems still have the wrong phase and averaging
family. The absolute squarefree estimate (148.32) is unproved but not
disproved. Endpoint uniformity is secondary: (148.9) is exact, the
accepted collars produce a smooth interior, and the same direct
interface mismatch already holds when \(\Omega\) is supported strictly
away from all boundaries.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| exact_one_sided_B_process_and_q_amplitude | **Pass.** (148.9), (148.22), and (148.23) give the exact Poisson factor, positive saddle, \(e(1/8)\), and \(N^{-1/4}(d\lambda)^{-1}\) amplitude with no \(q\)-power. |
| Q_length_and_RD_target_normalization | **Pass.** (148.2)--(148.4) give \(q\asymp\lambda Q\), \(Q=D\sqrt{N/M}\), and target \(RD\). |
| squarefree_both_variables_coprime_parity_character_cone | **Pass.** (148.8) retains both squarefree conditions and coprimality; \(d_o\) handles even \(d\); oddness, \(\chi_4\), and \(y_0>4d\) remain literal. |
| Mobius_square_divisor_signed_decomposition | **Pass.** The \(\mu(u)\mu(v)\) signs remain inside (148.1). |
| near_divisor_j_parameter_and_multiplicity | **Pass.** (148.24)--(148.25) retain \(j\), divisibility, and divisor multiplicity. |
| dispersion_diagonal_offdiagonal_common_divisor | **Source fail.** (148.29) exposes the diagonal and imprimitive gcd strata; the cited fixed-modulus correlations do not own them. |
| q_divides_N_small_j_and_zero_frequency | **Pass as retained.** Poisson \(q=0\) is killed, but \(j=0\), \(q\mid\lambda N\), especially \(q\mid N\) at \(\lambda=1\), remains. |
| arbitrary_q_coefficient_phase_alignment_falsifier | **Fail for that analogue, as required.** The \(D=1\) alignment disproves an arbitrary-coefficient all-scale target, without addressing the actual signs. |
| squarefree_absolute_QplusD_feasibility | **Open/source fail.** (148.32) is neither proved nor refuted by the audited sources. |
| source_theorem_phase_modulus_coefficient_match | **No direct match.** The cards (148.12)--(148.21) have unmatched modulus, phase, average, coefficients, ranges, or diagonal. The exact-denominator Schlage-Puchta specialization fails, but other admissible approximants are not exhaustively excluded. |
| H_resonance_interface_translation | **Fail.** The formal substitution does not identify coefficients, \([u^2,v]\) need not be powerful, and (148.32a)--(148.32b) leave the complementary reciprocal \(j\)-range unowned. |
| all_M_D_E_Q_power_ledger | **Pass as a capacity ledger.** The table retains every aspect and the \(R^{4/3}\) transition; the large-sieve row is explicitly only a separable, \(q\)-independent diagnostic. |
| clipped_prefix_profile_collar_polar_boundary | **Pass as reduction, not source estimate.** \(\Omega\) retains the prefix/profile/cone; accepted collars remain separate; (148.9) retains endpoint integrals. |
| D1_prime_even_exact_radical_and_slow_family | **Pass as controls.** \(D=1\), primes (\(u=v=1\)), and even \(d\) via \(d_o\) remain. The exact \(j=0\) reciprocal resonance remains. Inherited \(N=sL^2\) gives \(e(\sqrt{Ns})=1\), while \(N=sL^2+1\) gives \(\sqrt{Ns}=sL+(\sqrt{L^2+1/s}+L)^{-1}\); neither is promoted to a lower bound. |
| individual_positive_direction_and_fixed_centre | **Pass.** Only \(e(+\sqrt{Nde})\), positive stationary \(q\), and fixed \(N=\lfloor X\rfloor\) are used. |
| Round138_cross_tge2_and_downstream_scope | **No effect.** No Round-138 cross, \(t\geq2\) layer, M9 parent, bridge, quarter target, or exponent is claimed. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Repository context used, exactly as assigned:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round148_squarefree_reciprocal_dispersion_strategy.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/barrier_packet.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/candidates/conductor_round147_t1_squarefree_voronoi_and_H_no_go.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/reports/t1_squarefree_voronoi_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/reports/complex_order_voronoi_source_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/reviews/conductor_round147_adjudication.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/synthesis.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reviews/source_applicability_seam_review.md, used for the theorem-hypothesis and applicability repairs.

Primary technical sources used:

- Schlage-Puchta, [The exponential sum over squarefree integers](https://arxiv.org/html/1105.1616v1);
- Nunes, [Squarefree numbers in large arithmetic progressions](https://arxiv.org/html/1602.00311v1);
- Nunes, [A note on the least squarefree number in an arithmetic progression](https://arxiv.org/pdf/1605.03347);
- Nunes, [Squarefree numbers in arithmetic progressions](https://arxiv.org/html/1402.0684v2);
- Mangerel, [Squarefree Integers in Arithmetic Progressions to Smooth Moduli](https://arxiv.org/html/2008.11163v2);
- Bettin and Chandee, [Trilinear forms with Kloosterman fractions](https://arxiv.org/html/1502.00769v1).

No secondary source is used for a technical theorem statement.

## 7. Recommended state effect

**Retain and revise: keep the Round-148 signed squarefree reciprocal
target open. Record this report only as a no-direct-applicability result
for the quoted progression, exact-denominator additive, separable
large-sieve, and fixed-modulus Kloosterman interfaces. It is not an
exhaustive no-go for every Schlage-Puchta approximant or every possible
source-legal reorganization. Make no graph, proof-draft,
validation-matrix, campaign, downstream, or exponent change.**

A lawful next input must be a new coefficient-sensitive theorem for
(148.1), a joint classification and aggregation of admissible
approximants over the varying \(q\), or an exact Euler recombination
followed by a theorem for the resulting \(H\)-interface and its narrower
band. It cannot be an arbitrary-coefficient estimate, an absolute
\(q\)-average inherited from the bare lemma, or a fixed-modulus
Kloosterman correlation with an unmatched phase.
