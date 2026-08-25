# Round 153 terminal primary-source review

- Campaign: m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate
- Reviewed candidate: candidates/conductor_round153_mobius_boundary_collapse.md
- Role: independent terminal primary-source and theorem-hypothesis reviewer
- Starting claim-graph SHA-256: 9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1
- Terminal verdict: **GREEN**

## 1. Result

The source-dependent conclusions in the Round-153 candidate and the two
assigned reports are valid at their stated, deliberately limited scope.
The exact Möbius recombination leaves the literal one-variable survivor

\[
 Q_U^*=
 \sum_{\substack{b\ {\rm odd}\\ b\asymp M}}
 \chi _4(b)b^{-3/4}A_U(b)e(\sqrt{Nb})
 \mathbf 1_{\mathcal R_*}(b),
\tag{153.SF1}
\]

with the inherited zero extension, endpoints, profile transitions, and
strict large-defect mask.  The strongest licensed one-variable estimate
in the audited chain is

\[
 |Q_U^*|
 \ll_\varepsilon
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}X^\varepsilon
 +X^\varepsilon .
\tag{153.SF2}
\]

It is target-sized on the already owned side
\(M^{449}\gg R^{780}\), and it has a positive power loss on the frozen
open side \(M^{449}\ll R^{780}\).  None of the primary-source theorems
audited here proves an \(O_\varepsilon(X^\varepsilon)\) estimate for the
literal wave (153.SF1) below \(M^{449}\asymp R^{780}\).

Robert--Sargos Theorem 1 is the closest pointwise monomial theorem.  It
accepts a joint coefficient in two variables and a separate coefficient
in the third, but it does not directly accept the actual factor depending
jointly on \(a^2bs^2\).  Even after replacing that factor by a more
favourable separated model, the exact specialization of its printed
upper bound contains a term at least
\(R^{1/2}M^{-1/4}\gg R^{59/898}\) in the open range.  This proves only
that this direct theorem application does not deliver the target.  It is
not a lower bound for the signed sum.

The other audited sources have earlier literal mismatches: the
Kowalski--Robert--Wu bilinear proposition excludes exponent one;
Matomäki--Teräväinen gives a logarithmic saving for a linear additive
Möbius twist; Heath-Brown averages a varying family of real characters;
Schlage-Puchta treats a linear additive phase on squarefree integers;
Kaczorowski--Perelli treats analytic continuation of twists of fixed
extended-Selberg-class functions rather than the required uniform finite
sum; and Baier's square roots are modular roots inside an \(e_r\)-phase,
not ordinary positive real square roots.

The verdict is GREEN because every material theorem-scope inference and
every power comparison used for the Round-153 decision survives direct
inspection.  Several source-card wording updates are recorded below, but
none changes the no-direct-match conclusion.  In particular, this review
does **not** turn absence of a matching theorem in the audited corpus into
an impossibility theorem for future bilinear, spectral, spacing, or
arithmetic methods.

## 2. Exact source statements and hypotheses

### 2.1 Bourgain and Tao--Trudgian--Yang

Jean Bourgain,
[*Decoupling, exponential sums and the Riemann zeta function*](https://arxiv.org/html/1408.5794v2),
Theorem 6 states that

\[
 \left(\frac{13}{84}+\varepsilon,
       \frac{55}{84}+\varepsilon\right)
\tag{153.SF3}
\]

is an exponent pair.  The shorter window
\(17/42\leq \log M/\log T\leq1/2\) belongs to the direct estimate in
Theorem 4, not to the final scope of Theorem 6.  Section 5 explicitly
handles the cases where the length can exceed \(T^{1/2}\), subject to
\(M\leq T\), and the case of a proper subinterval on which the phase was
initially defined.  Thus importing the Theorem-4 window as an extra
hypothesis on Theorem 6 would be incorrect; the Round-153 report does not
do so.

In Terence Tao, Tim Trudgian, and Andrew Yang,
[*New exponent pairs, zero density estimates, and zero additive energy
estimates: a systematic approach*](https://arxiv.org/html/2501.16779v1),
Definition 11 places \((k,\ell)\) in the standard exponent-pair triangle
and requires

\[
 \sum_{n\in I}e(TF(n/H))
 \ll (T/H)^{k+o(1)}H^{\ell+o(1)}
\tag{153.SF4}
\]

for every interval \(I\subset[H,2H]\), every model phase, and
\(T\geq H\geq1\).  The experimental HTML contains one malformed duplicate
inequality immediately before the correctly quantified line; the latter
and Definition 12 both print the operative condition \(T\geq H\geq1\).
Definition 12 gives the finite-derivative, epsilon-form version uniformly
over every such interval.

Lemma 13 says that the \(A\)-, \(B\)-, and \(C\)-processes preserve
exponent pairs and prints

\[
 B(k,\ell)=(\ell-\tfrac12,k+\tfrac12).
\tag{153.SF5}
\]

Lemma 14 states, for an exponent pair \((k,\ell)\),

\[
 \beta(\alpha)\leq
 \max\!\left\{
 k_1+\alpha(\ell_1-k_1),\,
 \frac1{12}+\frac{2\alpha}{3}
 \right\},\qquad 0\leq\alpha\leq1,
\tag{153.SF6}
\]

where

\[
 (k_1,\ell_1)=D(k,\ell)=
 \left(
 \frac{5k+\ell+2}{8(5k+3\ell+2)},
 \frac{29k+21\ell+10}{8(5k+3\ell+2)}
 \right).
\tag{153.SF7}
\]

Lemma 15 identifies an exponent pair with the corresponding affine upper
bound for \(\beta(\alpha)\) on \(0\leq\alpha\leq1\).  The immediately
following Remark 16 supplies the symmetry reduction to one half of that
interval when the slope is on the stated side of \(1/2\).  Applied to
(153.SF3), these interfaces give, with arbitrary epsilon perturbations
absorbed into \(X^\varepsilon\),

\[
 D\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{18}{199},\frac{593}{796}\right),
\qquad
 BD\!\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{195}{796},\frac{235}{398}\right).
\tag{153.SF8}
\]

### 2.2 Robert--Sargos Theorems 1--2 and Lemma 8

O. Robert and P. Sargos,
[*Three-dimensional exponential sums with monomials*](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf),
define

\[
 S_0=
 \sum_{H<h\leq2H}\sum_{K<n\leq2K}\alpha(h,n)
 \sum_{L<m\leq2L}\beta(m)
 e\!\left(
 \frac{Yh^{\beta_0}n^{\gamma_0}m^{\alpha_0}}
 {H^{\beta_0}K^{\gamma_0}L^{\alpha_0}}
 \right).
\tag{153.SF9}
\]

The exact Theorem-1 hypotheses are that \(H,K,L\) are positive integers,
\(Y>1\), both coefficient families have modulus at most one, the three
exponents are fixed real numbers, and

\[
 \alpha_0(\alpha_0-1)\beta_0\gamma_0\ne0.
\tag{153.SF10}
\]

Its conclusion is

\[
 S_0\ll_\varepsilon(HKL)^{1+\varepsilon}
 \left\{
 \left(\frac{Y}{HKL^2}\right)^{1/4}
 +(HK)^{-1/4}+L^{-1/2}+Y^{-1/2}
 \right\}.
\tag{153.SF11}
\]

Theorem 2 fixes \(\alpha_0\in\mathbb R\setminus\{0,1\}\), takes an integer
\(M_0\geq2\) and a real \(\delta>0\), and counts quadruples
\(m_i\in\{M_0+1,\ldots,2M_0\}\) satisfying

\[
 |m_1^{\alpha_0}+m_2^{\alpha_0}
   -m_3^{\alpha_0}-m_4^{\alpha_0}|
 \leq\delta M_0^{\alpha_0}.
\tag{153.SF12}
\]

It proves

\[
 \mathcal N(M_0,\delta)
 \ll_\varepsilon M_0^{2+\varepsilon}
 +\delta M_0^{4+\varepsilon}.
\tag{153.SF13}
\]

Lemma 8 takes positive integers \(K,L\), coefficients of modulus at most
one, real bounded coordinates \(u(k),v(l)\), and \(Y\geq1\).  If
\(\mathcal B_1,\mathcal B_2\) count ordered coordinate pairs at distance
at most \(Y^{-1}\), then

\[
 \sum_{k\leq K}\sum_{l\leq L}
 a(k)b(l)e(Yu(k)v(l))
 \ll Y^{1/2}\mathcal B_1^{1/2}\mathcal B_2^{1/2}.
\tag{153.SF14}
\]

These statements verify the theorem numbers, coefficient separation, the
exponent-one exclusions, and the spacing threshold used in the source
report.  Neither Theorem 2 nor Lemma 8 supplies a signed lower bound.

### 2.3 Kowalski--Robert--Wu, Matomäki--Teräväinen, and Heath-Brown

E. Kowalski, O. Robert, and J. Wu,
[*Small gaps in coefficients of L-functions and B-free numbers in short
intervals*](https://ems.press/content/serial-article-files/38194?nt=1),
Proposition 5 takes \(X>0\), \(M,N\geq1\), separated coefficient
sequences of modulus at most one, and
\(\alpha,\beta\in\mathbb R\setminus\{0,1\}\).  It proves

\[
 \sum_{m\sim M}\sum_{n\sim N}
 \varphi_m\psi_n
 e\!\left(\frac{Xm^\alpha n^\beta}{M^\alpha N^\beta}\right)
 \ll_\varepsilon
 \left\{
 (XM^6N^6)^{1/8}+M^{1/2}N+MN^{3/4}
 +X^{-1/2}MN
 \right\}(MN)^\varepsilon.
\tag{153.SF15}
\]

The literal pre-collapse phase has exponent one in \(a\) (and also in
\(s\)) and exponent \(1/2\) in \(b\).  Either two-variable ordering that
retains \(a\) hits the proposition's printed exclusion of exponent one.

K. Matomäki and J. Teräväinen,
[*On the Möbius function in all short intervals*](https://arxiv.org/html/1911.09076v2),
Theorem 1.5 fixes \(\theta>3/5\) and \(\varepsilon>0\), takes \(x\)
sufficiently large and \(H\geq x^\theta\), and proves uniformly for every
real \(\alpha\) that

\[
 \sum_{x<n\leq x+H}\mu(n)e(\alpha n)
 =O\!\left(\frac{H}{(\log x)^{1/3-\varepsilon}}\right).
\tag{153.SF16}
\]

This is a linear additive twist with only a logarithmic saving.  It can
inform some genuine Möbius ranges, but it does not cover the compulsory
\(a=1\) survivor, where there is no Möbius variable, and it supplies no
simultaneous \(b\)-cancellation with the fixed \(\chi _4(b)\).

D. R. Heath-Brown,
[*A mean value estimate for real character sums*](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf),
Theorem 1 takes positive integers \(M,N\) and arbitrary complex
coefficients and proves

\[
 \sum_{m\leq M}^{*}
 \left|\sum_{n\leq N}^{*}a_n
 \left(\frac{n}{m}\right)\right|^2
 \ll_\varepsilon
 (MN)^\varepsilon(M+N)
 \sum_{n\leq N}^{*}|a_n|^2,
\tag{153.SF17}
\]

where both stars restrict to positive odd squarefree integers.  This is a
mean square over a varying Jacobi-symbol family.  The Round-153 survivor
instead has one fixed character \(\chi _4\), an ordinary Archimedean
square-root phase, and no modulus average.

### 2.4 Schlage-Puchta

J.-C. Schlage-Puchta,
[*The exponential sum over squarefree integers*](https://arxiv.org/html/1105.1616v1),
defines

\[
 S(\alpha)=\sum_{n\leq N}\mu^2(n)e(\alpha n).
\tag{153.SF18}
\]

The introductory definition of \(\mathfrak m(Q)\) is printed for
\(1\leq Q<N^{1/2}/2\), with major arcs generated by coprime \(a,q\),
\(q\leq Q\), and \(|\alpha q-a|\leq Q/N\).  Theorem 1 itself prints

\[
 S(\alpha)\ll N^{1+\varepsilon}Q^{-1}
\quad(\alpha\in\mathfrak m(Q)),
\qquad Q\leq N^{1/2}.
\tag{153.SF19}
\]

Theorem 3 states that if an integer \(q\) satisfies
\(|\alpha q-a|\leq q^{-1}\), then

\[
 |S(\alpha)|
 \ll N^{1+\varepsilon}q^{-1}+N^\varepsilon q.
\tag{153.SF20}
\]

The preceding Dirichlet-approximation paragraph uses coprime \(a,q\).
The minor-arc result has exceptional major arcs, and both theorems retain
a linear additive phase.  Neither theorem has the ordinary
\(e(\sqrt{Nb})\) phase, its growing parameter, or the actual project
profile.

### 2.5 Kaczorowski--Perelli, including the 2026 multiple twist

J. Kaczorowski and A. Perelli,
[*Twists and resonance of L-functions, I*](https://arxiv.org/html/1304.4734v1),
start with a fixed \(F\in\mathcal S^\sharp\) of degree \(d>0\) and define,
for real \(\alpha\ne0\),

\[
 F(s,\alpha)=
 \sum_{n\geq1}a(n)n^{-s}e(-\alpha n^{1/d}).
\tag{153.SF21}
\]

Their Theorems 1--5 concern analytic continuation, polar structure,
transformation, and growth of infinite nonlinear-twist Dirichlet series.
They do not print a pointwise finite-sum estimate uniform for
\(\alpha=\sqrt N\) growing with the project parameters.  A degree-one
standard twist is linear; an ordinary square-root standard twist requires
degree two.  The required coefficient series

\[
 \sum_{n\geq1}\frac{\mu^2(n)\chi _4(n)}{n^s}
 =\frac{L(s,\chi _4)}{L(2s,\chi _4^2)}
\tag{153.SF22}
\]

is not the required fixed degree-two member of
\(\mathcal S^\sharp\).

Their 2026 paper,
[*Multiple standard twists of L-functions*](https://arxiv.org/html/2603.13885v1),
takes \(N\geq1\), fixed \(F_\nu\in\mathcal S^\sharp\) of degrees
\(d_\nu>0\), \(\alpha>0\), and positive \(\kappa_\nu\) satisfying the
definition

\[
 \sum_{\nu=1}^{N}d_\nu\kappa_\nu=1.
\tag{153.SF23}
\]

It studies

\[
 \sum_{n_1,\ldots,n_N\geq1}
 \frac{\prod_\nu a_\nu(n_\nu)}
      {\prod_\nu n_\nu^{s_\nu}}
 e\!\left(-\alpha\prod_\nu n_\nu^{\kappa_\nu}\right).
\tag{153.SF24}
\]

Theorem 1 is stated for \(N\geq2\) and describes entire or meromorphic
continuation on \(\mathbb C^N\), according to the multiple spectrum.
It is not a finite bilinear estimate.  Moreover, the literal
pre-collapse exponents \(1\) and \(1/2\) do not satisfy (153.SF23) for
two positive-degree extended-Selberg-class factors: such degrees are at
least one, so \(d_1+ d_2/2\geq3/2\).  The coefficient families
\(\mu(a)\) and \(\chi _4(b)\) also do not provide the required pair of
fixed \(L\)-functions in the needed way.  Thus the 2026 paper does not
repair the Round-153 interface.

### 2.6 Baier's modular square roots

Stephan Baier,
[*On certain bilinear sums with modular square roots and
applications*](https://arxiv.org/html/2601.15448v4),
defines \(e_r(x)=e(x/r)\) and explicitly declares that
\(\sqrt{jm}\) denotes the collection of solutions to
\(k^2\equiv jm\pmod r\), not the ordinary positive real square root.
Theorem 2 assumes \(r,j\in\mathbb N\), \((r,j)=1\),
\(1\leq L,M\leq r\), a continuously differentiable \(f\) with
\(|f'|\leq F\leq L^{-1}\), arbitrary finite coefficient sequences, and

\[
 1\leq H\leq\min\{(LF)^{-1},M\}.
\tag{153.SF25}
\]

For its bilinear modular-root sum it proves

\[
 \ll
 \left(
 H^{-1/2}L^{1/2}M+
 H^{1/4}L^{1/4}M+
 H^{-1/4}L^{1/4}M^{3/4}r^{1/4}
 \right)
 \|\boldsymbol\alpha\|_2\|\boldsymbol\beta\|_\infty r^\varepsilon.
\tag{153.SF26}
\]

There is no modulus or modular-root fibre in (153.SF1), so no literal
specialization exists.  The current follow-up
[*Partial progress towards the large sieve for square
moduli*](https://arxiv.org/html/2605.01635v3) continues to distinguish
ordinary square roots in an auxiliary analytic factor from modular roots
inside \(e_r\); it likewise supplies no theorem for (153.SF1).

## 3. Proof or derivation

### 3.1 Exact Möbius collapse

Use the signed identity

\[
 \mu^2(\tau)=\sum_{a^2\mid\tau}\mu(a)
\tag{153.SF27}
\]

and write \(\tau=a^2b\), then \(r=as\).  The coefficient of the resulting
\(r\)-block is

\[
 C_S(r)=
 \sum_{\substack{a\mid r\\r/a<S}}\mu(a).
\tag{153.SF28}
\]

For \(r<S\), every divisor of \(r\) is present, so

\[
 C_S(r)=\sum_{a\mid r}\mu(a)=\mathbf 1_{r=1}.
\tag{153.SF29}
\]

For \(r\geq S\), \(|C_S(r)|\leq d(r)\).  The support
\(r^2b\asymp M\), the weight \((r^2b)^{-3/4}\asymp M^{-3/4}\),
and the accepted \(X^\varepsilon\) profile bound give

\[
 \sum_{r\geq S}|C_S(r)|
 \sum_b |F_U(r^2b)|
 \ll_\varepsilon
 X^\varepsilon\left(M^{-1/4}+\frac{M^{1/4}}{S}\right)
 \ll_\varepsilon X^\varepsilon
\tag{153.SF30}
\]

for \(S=\lceil M^{1/4}\rceil\).  Therefore the only non-absolutely-safe
term is \(r=1\), giving (153.SF1).  In particular, Möbius inversion does
not create independent Type-I/Type-II blocks all the way to the bottom:
complete recombination cancels every \(1<r<S\) exactly.

### 3.2 The one-variable boundary

For \(b\asymp M\), the ordinary phase \(e(\sqrt{Nb})\) has exponent-pair
parameter

\[
 T\asymp\sqrt{NM}=R^2M^{1/2},
\qquad
 \frac{T}{M}\asymp\frac{R^2}{M^{1/2}}\gg R
\tag{153.SF31}
\]

throughout \(M\leq R^2\).  Mod-four residue splitting makes \(\chi _4\)
constant before applying the unweighted interval estimate.  The
square-root phase satisfies the required finite derivative normalization,
and the accepted bounded-variation estimate inserts the literal profile
afterwards by Abel summation.

For an exponent pair \((k,\ell)\), restoring the weight \(M^{-3/4}\)
gives

\[
 |Q_U^*|
 \ll_\varepsilon
 R^{2k}M^{\ell-k/2-3/4}X^\varepsilon+X^\varepsilon .
\tag{153.SF32}
\]

Putting the \(BD\) pair from (153.SF8) into (153.SF32) yields

\[
 2k=\frac{390}{796}=\frac{780}{1592},
\qquad
 \ell-\frac{k}{2}-\frac34=-\frac{449}{1592},
\tag{153.SF33}
\]

which is exactly (153.SF2).  No hidden Theorem-4 window, modulus average,
or endpoint deletion enters this calculation.

For completeness, the auxiliary line in Tao--Trudgian--Yang Lemma 14
does not spoil the \(D\)-step.  On \(0\leq\alpha\leq1/2\), the difference
between the \(D\)-line and
\(1/12+2\alpha/3\) is linear and is positive at both endpoints:

\[
 \frac{18}{199}-\frac1{12}=\frac{17}{2388}>0,
\qquad
 \frac12\left(\frac{18}{199}+\frac{593}{796}\right)
 -\frac5{12}=\frac5{4776}>0.
\tag{153.SF34}
\]

Lemma 15 and Remark 16 give the global \(D\)-pair, after which Lemma 13
legally applies \(B\).

### 3.3 Exact Robert--Sargos translation

Before recombination take

\[
 (H,K,L,Y;\beta_0,\gamma_0,\alpha_0)
 =(A,S,B,\mathcal T;1,1,\tfrac12),
\qquad
 P:=AS,
\tag{153.SF35}
\]

with

\[
 A^2BS^2\asymp M,\qquad
 B\asymp\frac{M}{P^2},\qquad
 PB\asymp\frac{M}{P},\qquad
 \mathcal T=P\sqrt{NB}\asymp R^2M^{1/2}.
\tag{153.SF36}
\]

The choice of \(b\) for the differenced \(m\)-slot is forced if one wants
to meet \(\alpha_0\notin\{0,1\}\); placing \(a\) or \(s\) there gives
\(\alpha_0=1\).  Apply (153.SF11) only to the favourable hypothetical
model in which the coefficient is separated.  Multiplying by the actual
dyadic weight \(M^{-3/4}\), and absorbing \((ASB)^\varepsilon\), gives

\[
 M^{-3/4}|S_0|
 \ll_\varepsilon X^\varepsilon
 \left\{
 R^{1/2}M^{-1/8}P^{-1/4}
 +M^{1/4}P^{-5/4}
 +M^{-1/4}
 +R^{-1}P^{-1}
 \right\}.
\tag{153.SF37}
\]

Indeed, the first source term is exactly

\[
 M^{-3/4}(PB)
 \left(\frac{\mathcal T}{PB^2}\right)^{1/4}
 =R^{1/2}M^{-1/8}P^{-1/4},
\tag{153.SF38}
\]

while the remaining three terms respectively give the remaining three
quantities in (153.SF37).  Since a nonempty dyadic \(b\)-block has
\(B\gg1\), (153.SF36) implies \(P\ll M^{1/2}\).  Hence the first positive
term on the theorem's upper-bound right-hand side satisfies

\[
 R^{1/2}M^{-1/8}P^{-1/4}
 \gg R^{1/2}M^{-1/4}.
\tag{153.SF39}
\]

On \(M^{449}\ll R^{780}\),

\[
 R^{1/2}M^{-1/4}
 \gg R^{1/2-195/449}
 =R^{59/898}.
\tag{153.SF40}
\]

Equations (153.SF37)--(153.SF40) reproduce (153.S45)--(153.S48)
exactly.  They show that the printed Robert--Sargos upper bound is too
large for the target even in the more favourable separated model.  They
do not estimate the actual sum from below and do not rule out additional
arithmetic cancellation.

### 3.4 Direct-match scope

The literal coefficient before recombination contains

\[
 \mu(a)\chi _4(b)
 A_U(a^2bs^2)
 \mathbf 1_{\mathcal R_*}(a^2bs^2;s).
\tag{153.SF41}
\]

The last two factors couple the Robert--Sargos \((a,s)\)-coefficient
block to its separate \(b\)-variable.  Thus (153.SF41) is not a direct
instance of Theorem 1.  After exact recombination, the boundary terms are
absolutely safe and the hard term is \(r=1\), where there is no remaining
Möbius range for a trilinear theorem to exploit.  This establishes a
method-specific source obstruction only.

## 4. First doubtful or unproved step

The first genuinely unproved analytic assertion is

\[
 |Q_U^*|\ll_\varepsilon X^\varepsilon
\quad\text{when}\quad M^{449}\ll R^{780},
\tag{153.SF42}
\]

for the exact wave (153.SF1).  The best licensed bound is (153.SF2), and
its factor \((R^{780}/M^{449})^{1/1592}\) is not harmless on that side of
the boundary.

If a future argument works before exact recombination, its first direct
Robert--Sargos hypothesis gap is the separation of (153.SF41).  Even if
that gap were independently repaired, its next obstacle is the
upper-bound power ledger (153.SF37)--(153.SF40).  Neither observation
proves that a different bilinear or arithmetic method cannot succeed.

The primary-source audit found the following non-blocking wording issues
that should be corrected whenever the source report is reused:

1. Robert--Sargos Theorem 2 also assumes integer \(M_0\geq2\) and
   \(\delta>0\); Lemma 8 also assumes bounded real coordinates,
   coefficient moduli at most one, and sieve parameter at least one.
2. The 2026 Kaczorowski--Perelli paper uses \(N\), not \(J\), for the
   number of functions.  Condition (1.3) imposes
   \(\sum_{\nu=1}^{N}d_\nu\kappa_\nu=1\), and Theorem 1 is stated for
   \(N\geq2\).
3. Heath-Brown's theorem has the full factor \(M+N\) in its upper bound,
   but that entire factor should not be labelled a positive diagonal.
   The direct no-match does not use that label.
4. The Round-153 bibliography gives a stale title for arXiv:2605.01635.
   Its current v3 title is *Partial progress towards the large sieve for
   square moduli*.  ArXiv:2603.00768 is withdrawn and expressly
   superseded by arXiv:2605.01635.  The current paper remains in the
   modular-square-root/square-modulus setting, so the scope conclusion is
   unchanged.

These corrections do not create a theorem-hypothesis gap in any
Round-153 inference and therefore do not lower the terminal verdict.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| Bourgain theorem number and range | **GREEN.** Theorem 6 is the global exponent-pair statement; the \(17/42\)-to-\(1/2\) direct window belongs to Theorem 4 and is not silently imported. |
| TTY Definitions 11--12 | **GREEN.** They give interval-uniform exponent-pair bounds for the model finite-derivative class with \(T\geq H\geq1\). |
| TTY Lemmas 13--15 | **GREEN.** The \(B\)- and \(D\)-formulas, the Lemma-14 maximum, and the Lemma-15 global inference reproduce (153.SF8); the \(D\)-line dominance check is (153.SF34). |
| One-variable power and boundary | **GREEN/open below boundary.** The exact exponent is \((R^{780}/M^{449})^{1/1592}\); no audited source removes it when \(M^{449}\ll R^{780}\). |
| Robert--Sargos Theorem 1 hypotheses | **GREEN.** The source accepts joint \(\alpha(h,n)\), separate \(\beta(m)\), \(Y>1\), and \(\alpha_0(\alpha_0-1)\beta_0\gamma_0\ne0\); the literal mask is not separated. |
| Robert--Sargos Theorem 2 and Lemma 8 | **GREEN.** Their counts, thresholds, and upper bounds match the report after the harmless exact-hypothesis supplements in Section 4.  Neither is used as a signed lower bound. |
| Translation (153.S45)--(153.S48) | **GREEN.** Every \(R,M,A,S,B\) power reproduces in (153.SF37)--(153.SF40).  The \(R^{59/898}\) statement concerns a term on an upper-bound RHS only. |
| Kowalski--Robert--Wu Proposition 5 | **GREEN/no match.** Both printed monomial exponents exclude \(0\) and \(1\); the literal \(a\)-exponent is one. |
| Matomäki--Teräväinen Theorem 1.5 | **GREEN/no match.** It is a uniform linear additive Möbius twist with a logarithmic saving and does not control the \(a=1\) survivor. |
| Heath-Brown real-character large sieve | **GREEN/no match.** It averages varying Jacobi symbols over positive odd squarefree moduli; it is not a theorem for fixed \(\chi _4(b)e(\sqrt{Nb})\). |
| Schlage-Puchta Theorems 1 and 3 | **GREEN/no match.** Both concern \(\mu^2(n)e(\alpha n)\) with linear phase and the printed minor-arc/rational-approximation conditions. |
| Kaczorowski--Perelli 2013 and 2026 | **GREEN/no match.** Both are analytic-continuation theories for fixed extended-Selberg-class coefficient systems; the multiple-twist normalization and theorem scope do not contain the literal finite bilinear sum. |
| Baier 2026 modular-square-root distinction | **GREEN/no match.** The paper explicitly distinguishes its modular-root collection inside \(e_r\) from an ordinary real square root.  Current follow-ups remain in the square-modulus setting. |
| Literal Möbius survivor | **GREEN.** Complete recombination cancels \(1<r<S\), prices \(r\geq S\) absolutely, and keeps \(r=1\) with coefficient one. |
| Absence versus impossibility | **GREEN.** The conclusion is only that no theorem in the audited corpus directly proves (153.SF42); no impossibility theorem is asserted. |
| Downstream scope | **GREEN.** Nothing here promotes \(D>1\), \(L>1\), the generic sector, an original \(t\geq2\) layer, the Round-138 cross owner, M1/M2, endpoint assembly, M9, the bridge, the target, or a global exponent. |

No numerical experiment was used to certify an asymptotic claim.

## 6. Dependencies and exact artifacts used

Repository artifacts read were:

1. protocol.md;
2. state/proof_obligations.yml;
3. state/active_campaign.yml;
4. rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/candidates/conductor_round153_mobius_boundary_collapse.md;
5. rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/reports/squarefree_bilinear_source_audit.md;
6. rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/reports/squarefree_mobius_bilinear_attack.md;
7. rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reviews/source_conductor_round152_final.md;
8. rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reviews/conductor_round152_adjudication.md;
9. sources/tao_trudgian_yang_2025.md; and
10. sources/bourgain_2017_exponent_pair.md.

Primary sources opened and checked directly were:

1. Bourgain, [arXiv:1408.5794v2](https://arxiv.org/html/1408.5794v2), especially Theorems 4 and 6 and Section 5;
2. Tao--Trudgian--Yang, [arXiv:2501.16779v1](https://arxiv.org/html/2501.16779v1), Definitions 11--12, Lemmas 13--15, Remark 16, and Table 1;
3. Robert--Sargos, [primary author PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf), Theorems 1--2 and Lemma 8;
4. Kowalski--Robert--Wu, [primary journal PDF](https://ems.press/content/serial-article-files/38194?nt=1), Proposition 5;
5. Matomäki--Teräväinen, [arXiv:1911.09076v2](https://arxiv.org/html/1911.09076v2), Theorem 1.5;
6. Heath-Brown, [Acta Arithmetica PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf), Theorem 1;
7. Schlage-Puchta, [arXiv:1105.1616v1](https://arxiv.org/html/1105.1616v1), Theorems 1 and 3;
8. Kaczorowski--Perelli, [arXiv:1304.4734v1](https://arxiv.org/html/1304.4734v1), equation (1.1) and Theorems 1--5;
9. Kaczorowski--Perelli, [arXiv:2603.13885v1](https://arxiv.org/html/2603.13885v1), condition (1.3) and Theorem 1;
10. Baier, [arXiv:2601.15448v4](https://arxiv.org/html/2601.15448v4), the modular-root definition and Theorem 2; and
11. Baier, [arXiv:2605.01635v3](https://arxiv.org/html/2605.01635v3), the current superseding follow-up and its explicit ordinary/modular-root distinction.

Every specialization from source variables to
\(R,M,A,S,B\), every Möbius recombination, and every power comparison in
this review is derived above or was a frozen incoming identity.  No
candidate, report, state file, source card, control, synthesis, or proof
draft was edited.

## 7. Recommended state effect

**Promote the exact Round-153 Möbius boundary collapse and retain the
source obstruction, subject to the conductor's mathematical seam reviews;
make no promotion of the open wave estimate.**

The State Patch should record only the following scoped facts:

1. Exact recombination reduces \(P_U^*\) to the literal \(r=1\)
   one-variable wave plus an absolute
   \(O_\varepsilon(X^\varepsilon)\) boundary remainder.
2. The licensed one-variable source bound is (153.SF2), so
   \(M^{449}\gg R^{780}\) is target-safe and the range
   \(M^{449}\ll R^{780}\) remains open.
3. No audited theorem proves the surviving
   \(\chi _4(b)e(\sqrt{Nb})\) actual-profile wave below
   \(M^{449}\asymp R^{780}\).
4. Robert--Sargos has both a literal coefficient-separation mismatch and,
   even in the ideal separated model, the upper-bound power obstruction
   (153.SF40).
5. The wording corrections in Section 4 should accompany any future
   reuse of the source audit.
6. No impossibility theorem, signed lower bound, or downstream M9/M1/M2,
   bridge, target, or exponent conclusion follows from this review.
