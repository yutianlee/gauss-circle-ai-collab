# Round 158 primary-source audit: boundary-frozen paired-interior cell trace

## 1. Result

### Cutoff-dated source-audit lemma

Fix the Round 158 hypotheses

\[
q=4N,\qquad c=\frac qd,\qquad H=\frac c2,\qquad
d\mid N,\quad d\ {\rm odd},
\]

\[
W=M^{-3/4},\qquad K=\sqrt{NM},\qquad
M^{3/4}(\log(2X))^A<V\leq K,
\]

with the inherited cone \(1\ll M\leq R^2\), \(R=X^{1/4}\),
\(N=\lfloor X\rfloor\), hence \(M\leq N^{1/2+o(1)}\).  Preserve both
signed blocks, every odd divisor \(d\), the complementary nonzero
frequencies, the literal complex profile, the external
\(B_{1,U}(1)\) seam, and all strict endpoints.

As of 25 August 2026, no audited primary theorem proves the
boundary-frozen strict selected trace target, nor a new
owner-complete positive-power range in the frozen cone.  The exact
conclusion is

> **cutoff-dated SOURCE NO-MATCH, not a mathematical impossibility
> theorem.**

The source audit has three positive outputs.

1. Duke--Friedlander--Iwaniec Lemma 6.1 is an exact theorem for each
   individual theta-multiplier kernel \(K(-v^2,-s;c)\), including
   arbitrary composite \(c\equiv0\pmod4\) and imprimitive gcd strata.
   It is pointwise and does not control the moving Abel trace.
2. Müllner Theorem 5.3 and Lemma 5.4 exactly control unweighted
   complete and incomplete quadratic sums for the even composite
   modulus \(4N\).  Even after granting a coefficient-BV hypothesis
   that is not available for the literal boundary weight, absolute
   restoration of the quotient projector gives raw capacity
   \(N^{1/2}X^\varepsilon\).  The required raw bound is only
   \(M^{3/4}X^\varepsilon\), but this route would still require
   \(M\geq N^{2/3}\), outside \(M\leq N^{1/2}\).
3. Vaaler's interval polynomials and the explicitly stated audited
   pointwise square-root exponent-pair lines apply only to a
   deliberately easier fixed-endpoint, unit-BV model in which the
   residual boundary phases remain in the coefficient but are granted
   lawful BV or joint control.
   The sharp-mask truncation forces Fourier degree \(J\geq M^{1/4}\).
   Bourgain's pair misses the target unless \(M\geq N^{26/45}\); the
   most favorable target threshold among the transformed lines
   explicitly audited in that favorable model is
   \[
      BD\left(\frac{13}{84},\frac{55}{84}\right)
      =\left(\frac{195}{796},\frac{235}{398}\right),
   \]
   and it misses unless
   \[
      M^{703}\geq N^{390},\qquad
      M\geq N^{390/703}>N^{1/2}.
   \]
   Thus the Fourier truncation destroys the source-legal range of the
   corresponding unmasked scalar theorem.  This is an upper-bound
   capacity statement for that method, not a lower bound for the
   trace.

The first exact source-interface mismatch is earlier than either power
loss: the selected root \(k\) simultaneously indexes the literal
coefficient \(F_{k-1}(k)\) or \(F_{-k}(k)\), while the available
fixed-modulus root theorems sum the root with only a fixed additive
mode and keep their outer coefficient independent of that root.  The
project also has modulus \(4N\), a quotient character
\(\chi_4((k^2-s)/N)\), two oppositely oriented strict cell selectors,
moving Fourier endpoints, and \(k\)-dependent residual boundary
phases.  No audited theorem accepts this combination.

The diagonal endpoint \(s=j\), the removed zero-frequency trace, and
the removed Nyquist trace are target-safe.  The strict prefix
\(s<j\) and suffix \(s>j\) survive.  Nothing in this audit controls the
profile-bulk differences or any downstream owner.

## 2. Exact statement and hypotheses

### 2.1 Literal trace and the scalar threshold

Let \(J_+=[a_+,b_+]\) and \(J_-=[a_-,b_-]\).  With

\[
B_j(x)=\mathbf 1_{x\geq\lambda_\sigma(j)}F_j(x),\qquad
\lambda_+(j)=j+1,\qquad\lambda_-(j)=-j,
\]

\[
P^+_{d,v}(j)=\sum_{s=a_+}^{j}K(-v^2,-s;c),\qquad
P^-_{d,v}(j)=\sum_{s=j}^{b_-}K(-v^2,-s;c),
\]

the assigned trace is

\[
\begin{aligned}
\mathcal C_{\rm int,U}(V)
=-\frac{i(1+i)}{2Nq}
\sum_{\substack{d\mid N\\d\ {\rm odd}}}\chi_4(d)d\sqrt c
\bigg[&
\sum_{j=a_+}^{b_+-1}F_j(j+1)
\sum_{\substack{v\bmod H\\v\ne0,H/2}}
 e_c(-2v(j+1))P^+_{d,v}(j)\\
&+\sum_{j=a_-+1}^{b_-}F_j(-j)
\sum_{\substack{v\bmod H\\v\ne0,H/2}}
 e_c(2vj)P^-_{d,v}(j)\bigg].
\end{aligned}
\tag{158.SA1}
\]

Here \(F_j\) retains the actual complex residual phase, zero-extended
profile, transitions, half-open conventions, and hard endpoints.  The
only pointwise input used below is

\[
 |F_j(\lambda_\sigma(j))|\ll W X^\varepsilon.
\tag{158.SA2}
\]

No diagonal bounded-variation assertion in \(j\), \(k\), or \(\ell\)
is part of (158.SA2).

Full-frequency inversion and all-\(d\) recombination give

\[
\begin{aligned}
\mathcal C_+^{\rm full}
 &=\sum_{k=a_++1}^{b_+}F_{k-1}(k)
   \sum_{s=a_+}^{k-1}G_N(k^2-s),\\
\mathcal C_-^{\rm full}
 &=\sum_{k=-b_-}^{-a_--1}F_{-k}(k)
   \sum_{s=-k}^{b_-}G_N(k^2-s),
\end{aligned}
\tag{158.SA3}
\]

where

\[
G_N(t)=\mathbf 1_{N\mid t}\chi_4(t/N).
\tag{158.SA4}
\]

The positive endpoint is \(s=k-1\), and the negative endpoint is
\(s=-k\).  The strict survivor is therefore

\[
\begin{aligned}
\mathcal S_+
 &=\sum_k F_{k-1}(k)
   \sum_{s=a_+}^{k-2}G_N(k^2-s),\\
\mathcal S_-
 &=\sum_k F_{-k}(k)
   \sum_{s=-k+1}^{b_-}G_N(k^2-s),
\end{aligned}
\tag{158.SA5}
\]

with the displayed \(k\)-ranges inherited from (158.SA3).

Put

\[
k(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,\qquad
r_\ell=k(\ell)^2-N\ell.
\tag{158.SA6}
\]

There is no tie, and the asymmetric nearest cell is exactly

\[
-k(\ell)\leq r_\ell\leq k(\ell)-1.
\tag{158.SA7}
\]

The strict positive and negative selectors are respectively

\[
\mathbf 1_{\,+}(\ell)
=\mathbf 1_{\,a_+\leq r_\ell\leq k(\ell)-2}
\mathbf 1_{\{\text{literal positive block/profile tests}\}},
\tag{158.SA8}
\]

\[
\mathbf 1_{\,-}(\ell)
=\mathbf 1_{\,-k(\ell)+1\leq r_\ell\leq b_-}
\mathbf 1_{\{\text{literal negative block/profile tests}\}}.
\tag{158.SA9}
\]

Thus (158.SA5) is the exact restriction of

\[
\sum_{\substack{\ell\asymp M\\ \ell\ {\rm odd}}}
\chi_4(\ell)
\left[
 \mathbf 1_+(\ell)F_{k(\ell)-1}(k(\ell))
 +\mathbf 1_-(\ell)F_{-k(\ell)}(k(\ell))
\right].
\tag{158.SA10}
\]

Its support has cardinality

\[
L_{\rm trace}(V)\ll_\varepsilon\min(M,V)X^\varepsilon,
\tag{158.SA11}
\]

but (158.SA11) is unsigned.  Since one boundary atom has size
\(W=M^{-3/4}\), the scalar target \(O(X^\varepsilon)\) asks only for
the raw signed estimate

\[
\left|\sum_{\ell}\chi_4(\ell)
\bigl[\mathbf 1_+(\ell)A_+(\ell)+
\mathbf 1_-(\ell)A_-(\ell)\bigr]\right|
\ll M^{3/4}X^\varepsilon,
\tag{158.SA12}
\]

where \(A_+=W^{-1}F_{k-1}(k)\) and
\(A_-=W^{-1}F_{-k}(k)\) retain all literal phases and profiles.  A raw
\(M^{1/2}\) theorem would be sufficient but is stronger than needed.

### 2.2 Exact primary-source theorem cards

**Incomplete quadratic sums.**  Clemens Müllner,
[*The Rudin--Shapiro Sequence and Similar Sequences Are Normal Along
Squares*](https://doi.org/10.4153/CJM-2017-053-1), Theorem 5.3, proves
for \(a,b\in\mathbb Z\), \(m\geq1\),

\[
\left|\sum_{x=0}^{m-1}e_m(ax^2+bx)\right|
\leq\sqrt{2m(a,m)}.
\tag{158.SA13}
\]

Lemma 5.4 proves, for integers \(a,b,m,L,n_0\), \(m\geq1\), \(L\geq0\),

\[
\left|\sum_{x=n_0+1}^{n_0+L}e_m(ax^2+bx)\right|
<
\left(\frac Lm+1+\frac2\pi\log\frac{2m}{\pi}\right)
\sqrt{2m(a,m)}.
\tag{158.SA14}
\]

Arbitrary even composite \(m\), arbitrary gcd, and arbitrary interval
endpoints are legal.  An arbitrary coefficient sequence is not.

**Exact theta kernel and spectral formula.**  W. Duke, J. B.
Friedlander, and H. Iwaniec,
[*Weyl Sums for Quadratic Roots*](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf),
define for \(c\equiv0\pmod4\)

\[
K(m,n;c)=\sum_{u\bmod c}^{*}
\epsilon_u\left(\frac cu\right)e_c(m\bar u+nu).
\tag{158.SA15}
\]

Their Lemma 6.1, equation (6.8), states for all integers \(m,n\)

\[
 |K(m,n;c)|\leq(m,n,c)^{1/2}c^{1/2}\tau(c).
\tag{158.SA16}
\]

The erratum does not alter Section 6.  Their Theorem 2.5 instead
assumes \(m,n\geq1\), a singular cusp at infinity, and a smooth
\(g\) satisfying condition (2.8), including

\[
g(0)=g'(0)=0,\qquad
g,g',g''\ll(1+x)^{-2-\varepsilon},
\tag{158.SA17}
\]

together with the transform estimates (2.28)--(2.29).  Its geometric
side is the modulus average

\[
\sum_{c\equiv0\pmod{q_0}}\frac{K(m,n;c)}c
g\!\left(\frac{4\pi\sqrt{mn}}c\right),
\tag{158.SA18}
\]

and its full Maaß/residual, continuous, and holomorphic spectral sides
remain present.

**Moving modular-root cutoff.**  Igor Shparlinski and Yixiu Xiao,
[*Shifted bilinear sums of Salié sums and the distribution of modular
square roots of shifted primes*](https://arxiv.org/html/2601.10113v1),
work with a large prime \(q\) and \((a\lambda,q)=1\).  For

\[
V_{a,b,\lambda}(\boldsymbol\alpha;M,\mathcal N)
=\sum_{m\leq M}\sum_{n\leq N_m}\alpha_m
\sum_{x^2\equiv amn+b\pmod q}e_q(\lambda x),
\tag{158.SA19}
\]

Theorem 2.2 assumes

\[
M\leq q,\qquad MN\leq q^{3/2},\qquad M\leq N^2,
\tag{158.SA20}
\]

and gives

\[
|V_{a,b,\lambda}|
\leq\sqrt{\|\boldsymbol\alpha\|_1
\|\boldsymbol\alpha\|_2}\,
M^{1/12}N^{7/12}q^{1/4+o(1)}.
\tag{158.SA21}
\]

Theorem 2.3 assumes \(MN\ll q\), \(r\geq2\) fixed,
\(|\alpha_m|\ll1\), and smooth \(\varphi_m\) supported on
\([0,N_m]\) with
\(\|\varphi_m^{(j)}\|_\infty\leq C_jN_m^{-j}\); it gives

\[
\left(
M^{3/2-1/(2r)}N^{1/2+1/(2r)}
+M^{1-1/(2r)}N^{1/(2r)}q^{1/2-1/(4r)}
\right)q^{o(1)}.
\tag{158.SA22}
\]

Their separated Type-II Theorem 2.5 gives

\[
\|\boldsymbol\alpha\|_2\|\boldsymbol\beta\|_\infty
\left(M^{1/2}N^{1/2}+M^{1/2}Nq^{-1/4}
+Nq^{1/4}(\log q)^{1/2}\right).
\tag{158.SA23}
\]

**Polynomial-character sums.**  D. R. Heath-Brown,
[*Small Solutions of Quadratic Congruences, and Character Sums with
Binary Quadratic Forms*](https://arxiv.org/html/1411.4816v1),
Theorem 3, assumes \(r\geq3\), odd squarefree \(q\), a primitive
character modulo \(q\), a binary quadratic form \(Q\) with
\((\det Q,q)=1\), and a convex set contained in a radius-\(R\) disc.
For

\[
q^{1/4+1/(2r)}\leq R\leq q^{5/12+1/(2r)}
\tag{158.SA24}
\]

it proves

\[
\sum_{(x,y)\in C}\chi(Q(x,y))
\ll_{\varepsilon,r}
R^{2-1/r}q^{(r+2)/(4r^2)+\varepsilon}.
\tag{158.SA25}
\]

Mei-Chu Chang,
[*Short character sums for composite moduli*](https://arxiv.org/html/1201.0299v2),
Theorem 5, assumes a primitive character modulo \(q\), an interval
\(I\) of length \(L\), and

\[
q>L>\max_{p\mid q}p^{1000},
\tag{158.SA26}
\]

\[
\log L>(\log q)^{1-c}
+C\log\!\left(2\frac{\log q}{\log q'}\right)
\frac{\log q'}{\log\log q},
\qquad q'=\prod_{p\mid q}p,
\tag{158.SA27}
\]

and proves

\[
\left|\sum_{x\in I}\chi(x)\right|
\ll L e^{-\sqrt{\log L}}.
\tag{158.SA28}
\]

**Sharp interval Fourier approximation.**  Jeffrey D. Vaaler,
[*Some extremal functions in Fourier
analysis*](https://doi.org/10.1090/S0273-0979-1985-15349-2),
Theorems 18--19, gives degree-\(J\) periodic majorants and minorants
for an interval.  Their integral excess is \(1/(J+1)\), and the
nonzero Fourier coefficient at \(h\) has the interval coefficient
plus an error \(O((J+1)^{-1})\); in particular its size is

\[
\ll\min\!\left(|I|,\frac1{|h|}\right)+\frac1{J+1}.
\tag{158.SA29}
\]

This is a theorem for a fixed interval.  Applying it when the interval
endpoints and the external complex coefficient move requires a
separate variation argument.

**Pointwise square-root phases.**  Jean Bourgain,
[*Decoupling, exponential sums and the Riemann zeta
function*](https://arxiv.org/abs/1408.5794v2), Theorem 6, supplies the
standard exponent pair

\[
\left(\frac{13}{84},\frac{55}{84}\right).
\tag{158.SA30}
\]

Terence Tao, Tim Trudgian, and Andrew Yang,
[*New exponent pairs, zero density estimates, and zero additive
energy estimates: a systematic
approach*](https://arxiv.org/html/2501.16779v1), Definitions 11--12,
state that an exponent pair \((\kappa,\lambda)\) gives, for a model
phase, \(T\geq L\), and an interval in \([L,2L]\),

\[
\sum_{n\in I}e(TF(n/L))
\ll (T/L)^{\kappa+\varepsilon}L^{\lambda+\varepsilon}.
\tag{158.SA31}
\]

Their Lemma 13 gives

\[
B(\kappa,\lambda)
=\left(\lambda-\frac12,\kappa+\frac12\right),
\tag{158.SA32}
\]

and Lemma 14 gives the Sargos process

\[
D(\kappa,\lambda)=
\left(
\frac{5\kappa+\lambda+2}{8(5\kappa+3\lambda+2)},
\frac{29\kappa+21\lambda+10}{8(5\kappa+3\lambda+2)}
\right).
\tag{158.SA33}
\]

Their Table 1 records

\[
D\left(\frac{13}{84},\frac{55}{84}\right)
=\left(\frac{18}{199},\frac{593}{796}\right),
\tag{158.SA34}
\]

so Lemma 13 yields

\[
BD\left(\frac{13}{84},\frac{55}{84}\right)
=\left(\frac{195}{796},\frac{235}{398}\right).
\tag{158.SA35}
\]

**Square-root moments.**  Yixiu Xiao,
[*Moment Estimates and Discrepancy for Sums of Square Roots Modulo
One*](https://arxiv.org/html/2606.28986v1), defines

\[
S(h,n)=\sum_{a\sim n}e(h\sqrt a).
\tag{158.SA36}
\]

Theorem 1.1 states, for fixed \(\delta,\varepsilon>0\),

\[
\sum_{h\sim H}|S(h,n)|^2
\ll_{\varepsilon,\delta}Hn^{1+\varepsilon},
\qquad H\geq n^{1/2+\delta}.
\tag{158.SA37}
\]

Theorem 1.2 states, for \(0<\delta<1/6\),

\[
\sum_{h\sim H}|S(h,n)|^4
\ll_{\varepsilon,\delta}Hn^{2+\varepsilon},
\qquad n^{1/2+\delta}\leq H\leq n^{2/3}.
\tag{158.SA38}
\]

These are consecutive unweighted radicands and consecutive integer
frequencies.

**Direct floor and fractional-part results.**  Banks and Shparlinski,
[*Multiplicative character sums with twice-differentiable
functions*](https://doi.org/10.1093/qmath/han023), Theorem 6.1, fixes
\(2/3<\kappa<1\) and

\[
0<\varepsilon<
\frac{3\kappa-2}{2\kappa(2-\kappa)},
\tag{158.SA39}
\]

assumes a fixed twice-differentiable \(f\) with

\[
\lim_{x\to\infty}\frac{\log|f''(x)|}{\log x}=-\kappa,
\tag{158.SA40}
\]

a prime \(p\), a nonprincipal character modulo \(p\), and

\[
p^{1/(2\kappa)+\varepsilon}\leq L\leq p^{1/(2-\kappa)}.
\tag{158.SA41}
\]

It proves a power saving for
\(\sum_{n\leq L}\chi(\lfloor f(n)\rfloor)\).
Banks and Shparlinski,
[*Character sums with Beatty sequences on Burgess-type
intervals*](https://arxiv.org/abs/math/0608042), Theorem 4.1, treats
\(\lfloor\alpha n+\beta\rfloor\) for fixed irrational \(\alpha\) and
a nonprincipal character of a growing modulus.  It gives \(o(L)\)
when \(L\geq q^{1/4+\varepsilon}\) for prime \(q\),
\(L\geq q^{1/3+\varepsilon}\) for a prime power, and
\(L\geq q^{3/8+\varepsilon}\) for general \(q\).

Elkies and McMullen,
[*Gaps in \(\sqrt n\bmod1\) and ergodic
theory*](https://doi.org/10.1215/S0012-7094-04-12314-0), prove a
limiting gap law for the unweighted sequence
\(\{\sqrt n\}\).  El-Baz, Marklof, and Vinogradov,
[*The two-point correlation function of the fractional parts of
\(\sqrt n\) is Poisson*](https://arxiv.org/abs/1306.6543), Theorem 1
and its moment results, prove qualitative limiting statistics for the
same undilated unweighted sequence after the stated square
exception.  Neither source states an effective uniform signed
hard-window discrepancy estimate.

## 3. Proof or derivation

### 3.1 Full-frequency inversion, removed modes, and endpoints

Opening (158.SA15), summing \(v\bmod H=c/2\), completing the quadratic
in \(v\), and using the even 2-adic Gauss evaluation gives, for every
physical \(x,s\),

\[
\sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)
=\frac{1-i}{2}\sqrt c
\sum_{u\bmod c}^{*}\chi_4(u)e_c(u(x^2-s)).
\tag{158.SA42}
\]

The exterior odd-divisor recombination is exactly

\[
-\frac{i(1+i)}{2Nq}
\sum_{\substack{d\mid N\\d\ {\rm odd}}}
\chi_4(d)d\sqrt c\,
\sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)
=G_N(x^2-s).
\tag{158.SA43}
\]

Equivalently, the finite quotient projector is

\[
G_N(t)=-\frac{i}{2N}
\sum_{\substack{h\bmod4N\\h\ {\rm odd}}}
\chi_4(h)e_{4N}(ht).
\tag{158.SA44}
\]

Indeed, writing \(h=r+4a\) first forces \(N\mid t\); when
\(t=N\ell\), the remaining mod-four sum is \(2i\chi_4(\ell)\).
Equations (158.SA42)--(158.SA44) prove (158.SA3), with no modulus or
sign dropped.

For \(v=0\), opening the kernel and summing the \(s\)-interval
geometrically gives

\[
\sup_I\left|\sum_{s\in I}K(0,-s;c)\right|
\ll c\log(2c).
\tag{158.SA45}
\]

For \(v=H/2=N/d\), the same opening gives the identical interval
capacity

\[
\sup_I\left|\sum_{s\in I}K(-(N/d)^2,-s;c)\right|
\ll c\log(2c).
\tag{158.SA46}
\]

Restoring the literal atom and every exterior factor, either removed
trace costs

\[
\frac{VW}{Nq}
\sum_{\substack{d\mid N\\d\ {\rm odd}}}dc^{3/2}X^\varepsilon
\ll \frac{VW}{\sqrt N}X^\varepsilon
\leq M^{-1/4}X^\varepsilon.
\tag{158.SA47}
\]

This is trace-level control, not a transfer from the previously closed
total zero or fold row.  If \(c=4\), then \(H=2\), and the only nonzero
mode \(v=1\) is Nyquist; the paired interior frequency set is empty.

The endpoint congruences are

\[
j^2+j+1\equiv0\pmod N,\qquad j(j-1)\equiv0\pmod N.
\tag{158.SA48}
\]

For every prime power \(p^\nu\), \(j(j-1)\) has exactly the roots
\(0,1\pmod{p^\nu}\), hence exactly \(2^{\omega(N)}\) roots modulo
\(N\).  For \(j^2+j+1\), there is no root modulo \(2\); modulo \(3\)
there is the single root \(j=1\), and

\[
(1+3t)^2+(1+3t)+1=3(1+3t+3t^2)
\tag{158.SA49}
\]

shows there is no root modulo \(9\).  For \(p\ne2,3\), the roots exist
exactly when \(p\equiv1\pmod3\); there are two simple roots and each
has a unique lift to \(p^\nu\).  Consequently the first polynomial has
no roots if \(2\mid N\), \(9\mid N\), or a prime
\(p\equiv2\pmod3\) divides \(N\); otherwise it has \(2^r\) roots,
where \(r\) counts the primes \(p\equiv1\pmod3\) dividing \(N\), and a
single factor \(3\) contributes one root.

Because \(V<N\), the endpoint subrow has \(O(N^\varepsilon)\) atoms
and costs \(WN^\varepsilon\), hence is target-safe.  This deletes only
\(s=k-1\) from the positive side and \(s=-k\) from the negative side;
it says nothing about (158.SA5).

### 3.2 What incomplete quadratic completion actually yields

Insert (158.SA44) into (158.SA5).  For odd \(h\bmod q\),

\[
\sum_{s=a_+}^{k-2}e_q(-hs)
=\frac{e_q(-ha_+)-e_q(-h(k-1))}
       {1-e_q(-h)},
\tag{158.SA50}
\]

so the two positive quadratic phases are

\[
h k^2-ha_+,\qquad h(k^2-k+1).
\tag{158.SA51}
\]

Similarly,

\[
\sum_{s=-k+1}^{b_-}e_q(-hs)
=\frac{e_q(h(k-1))-e_q(-h(b_-+1))}
       {1-e_q(-h)},
\tag{158.SA52}
\]

giving

\[
h(k^2+k-1),\qquad hk^2-h(b_-+1).
\tag{158.SA53}
\]

These formulas retain the prefix/suffix orientations and strict
endpoints.

Now make the source-favorable but unproved grant

\[
\sup_k|F_{\pm}(k)|+\operatorname {Var}_k(F_{\pm})
\ll WX^\varepsilon
\tag{158.SA54}
\]

on every relevant \(k\)-interval.  Since its length is \(O(K)<q\),
Müllner's Lemma 5.4 and Abel summation give, for every odd \(h\),

\[
\left|\sum_kF_\pm(k)e_q(hk^2+\alpha hk+\beta h)\right|
\ll W\sqrt{q(h,q)}X^\varepsilon.
\tag{158.SA55}
\]

Using

\[
|1-e_q(h)|^{-1}\ll
\frac q{\min(h,q-h)}
\tag{158.SA56}
\]

and a gcd-divisor split,

\[
\sum_{\substack{h\bmod q\\h\ {\rm odd}}}
\frac{(h,q)^{1/2}}{\min(h,q-h)}
\ll q^\varepsilon,
\tag{158.SA57}
\]

the \(1/(2N)\) projector normalization yields

\[
|\mathcal S_++\mathcal S_-|
\ll W\sqrt N\,X^\varepsilon.
\tag{158.SA58}
\]

Thus this route has raw capacity \(N^{1/2}X^\varepsilon\).  Comparing
with the correct raw target (158.SA12), rather than with the stronger
square-root target, requires

\[
N^{1/2}\leq M^{3/4},\qquad M\geq N^{2/3},
\tag{158.SA59}
\]

which is disjoint from \(M\leq N^{1/2}\).  Equation (158.SA58) is only
an upper bound obtained after the illegal grant (158.SA54); it is not
an obstruction lower bound.  The literal application already stops
at the missing diagonal BV hypothesis.

### 3.3 Exact residual mask and the Fourier-truncation loss

Write

\[
\theta_\ell=\sqrt{N\ell}-k(\ell)\in[-1/2,1/2).
\tag{158.SA60}
\]

Then

\[
r_\ell=-2k(\ell)\theta_\ell-\theta_\ell^2.
\tag{158.SA61}
\]

For \(\eta_k(s)=\sqrt{k^2-s}-k\), the exact interval selectors in
(158.SA8)--(158.SA9) become

\[
\eta_k(k-2)\leq\theta_\ell\leq\eta_k(a_+)
\tag{158.SA62}
\]

on the positive side, and

\[
\eta_k(b_-)\leq\theta_\ell\leq\eta_k(-k+1)
\tag{158.SA63}
\]

on the negative side, together with every literal block/profile test.
Thus the interval endpoints move with \(k=k(\ell)\).

For fixed endpoints, Vaaler's theorem expands a selector into
frequencies \(|h|\leq J\).  Since

\[
e(h\theta_\ell)=e(h\sqrt{N\ell}),
\tag{158.SA64}
\]

splitting \(\chi_4\) into \(\ell=4m+1\) and \(4m+3\) exposes the model
\(\chi_4\)-twisted square-root waves

\[
S_h=\sum_{\ell\asymp M}\chi_4(\ell)
e(h\sqrt{N\ell}),
\tag{158.SA65}
\]

but (158.SA65) is not yet the literal Fourier mode.  The boundary
factors include, with the appropriate sign and endpoint,

\[
e\!\left(\sqrt{k^2-k+1}-k\right),\qquad
e\!\left(\sqrt{k^2+k}-k\right).
\tag{158.SA65a}
\]

They are near fixed phases on the top block, but they are not
algebraically a fixed shift of \(h\) in (158.SA65).  Their remaining
\(k\)-dependence belongs in the Fourier-mode coefficient together with
\(F_{k-1}(k)\) or \(F_{-k}(k)\), and requires its own BV estimate or a
joint coefficient-sensitive theorem.  The favorable benchmark below
therefore additionally grants that this residual boundary factor has
lawful joint variation; it is not discarded from the literal trace.

There are two separate losses.

First, for complex signed weights, the Vaaler excess cannot be
sandwiched through cancellation.  The source leaves a nonnegative
boundary-kernel incidence; it does not by itself bound the discrete
weighted error by its integral.  For the benchmark only, grant the
optimistic equidistributed full-support cost

\[
\frac{M}{J}.
\tag{158.SA66}
\]

Then (158.SA12) already forces \(J\geq M^{1/4}\).  The literal
boundary-kernel incidence may be worse.  If an optimized formal choice
gives \(J<1\), taking \(J=1\) leaves the optimistic raw error \(M\),
still too large.

Second, the Fourier coefficient for a moving interval is

\[
c_h(k)=
\frac{e(-h\alpha_k)-e(-h\beta_k)}{2\pi i h}
+O(J^{-1}).
\tag{158.SA67}
\]

Although \(|c_h(k)|\ll1/|h|+1/J\), variation in \(k\) differentiates
the endpoint phases: the factor \(h\) cancels \(1/h\), giving only
\(\operatorname {Var}_k c_h=O(1)\) in the favorable geometric model,
not \(O(1/h)\).  More fundamentally, no BV theorem is available for
\(F_{k-1}(k)\) or \(F_{-k}(k)\), nor for the combined coefficient
obtained by adjoining (158.SA65a).  Hence the following exponent-pair
ledger deliberately grants fixed endpoints, unit coefficient BV, and
lawful variation of the residual boundary factor.  It is strictly
easier than the literal trace.

### 3.4 Audited pointwise exponent-pair benchmark for the favorable model

For a standard exponent pair \((\kappa,\lambda)\), (158.SA31) applied
after the two mod-four progressions gives, uniformly on subintervals,

\[
|S_h|
\ll h^\kappa N^{\kappa/2}
M^{\lambda-\kappa/2+\varepsilon}.
\tag{158.SA68}
\]

Indeed the phase scale is \(T=h\sqrt{NM}\geq M\), and
\((T/M)^\kappa M^\lambda\) is the right side of (158.SA68).
Under the favorable grants following (158.SA67), Vaaler/Erdős--Turán
therefore gives

\[
E(J)\ll
\frac MJ+
N^{\kappa/2}M^{\lambda-\kappa/2}J^\kappa
X^\varepsilon.
\tag{158.SA69}
\]

Since \(J\geq M^{1/4}\), feasibility of
\(E(J)\ll M^{3/4}X^\varepsilon\) requires

\[
M\geq
N^{\,2\kappa/(\kappa+3-4\lambda)}
\tag{158.SA70}
\]

when the denominator is positive.

For Bourgain's pair (158.SA30),

\[
|S_h|\ll
h^{13/84}N^{13/168}M^{97/168+\varepsilon}.
\tag{158.SA71}
\]

At the mandatory \(J=M^{1/4}\), the oscillatory term is

\[
N^{13/168}M^{69/112+\varepsilon},
\tag{158.SA72}
\]

and (158.SA70) is \(M\geq N^{26/45}\).  Equivalently, optimizing
(158.SA69) gives

\[
J_*=M^{71/194}N^{-13/194},\qquad
E(J_*)\ll N^{13/194}M^{123/194+\varepsilon},
\tag{158.SA73}
\]

which reaches \(M^{3/4}\) only at the same threshold.  At the frozen
edge \(M=N^{1/2}\), (158.SA72) is
\(N^{259/672}\), while the target is \(N^{252/672}\).

For the transformed pair (158.SA35),

\[
|S_h|\ll
h^{195/796}N^{195/1592}M^{745/1592+\varepsilon}.
\tag{158.SA74}
\]

With no mask and \(h=1\), multiplying by \(W\) gives the legitimate
unmasked scalar bound

\[
W|S_1|
\ll
\left(\frac{N^{195}}{M^{449}}\right)^{1/1592}
X^\varepsilon,
\tag{158.SA75}
\]

which is target-sized for \(M^{449}\geq N^{195}\).  With the strict
mask, however, \(J=M^{1/4}\) changes the raw oscillatory term to

\[
N^{195/1592}M^{1685/3184+\varepsilon}.
\tag{158.SA76}
\]

The target condition is exactly

\[
M^{703}\geq N^{390}.
\tag{158.SA77}
\]

Optimizing the full discrepancy ledger instead gives

\[
J_*=M^{847/1982}N^{-195/1982},\qquad
E(J_*)\ll
N^{195/1982}M^{1135/1982+\varepsilon},
\tag{158.SA78}
\]

again equivalent to (158.SA77).  Since
\(390/703>1/2\), this supplies no frozen full-support trace range.

The four new pairs in Tao--Trudgian--Yang Theorem 20 were also checked.
In their printed orientation each has
\(\kappa+3-4\lambda\leq0\).  Applying the legal \(B\)-process, the
closest resulting threshold is obtained from

\[
B\left(\frac{89}{1282},\frac{997}{1282}\right)
=\left(\frac{178}{641},\frac{365}{641}\right),
\tag{158.SA79}
\]

which requires \(M\geq N^{356/641}\), slightly weaker than
(158.SA77).  The other three \(B\)-lines are weaker still.  On the
actual interval \(M\leq N^{1/2}\), Bourgain's original pair has the
smallest of these displayed upper capacities, but it too loses
\(N^{7/672}\) at the endpoint.  Thus (158.SA77) is only the most
favorable extrapolated target threshold among the explicitly stated
audited lines in the fixed-endpoint, unit-BV, residual-phase-BV model.
It is not a universal optimality theorem and is not a bound for the
literal coefficient.

This calculation records the requested Fourier loss: the unmasked
range \(M\geq N^{195/449}\) in (158.SA75) lies inside the frozen cone,
whereas the same pointwise source plus a sharp mask asks for
\(M\geq N^{390/703}\), outside it.

### 3.5 Why moments, root theorems, character theorems, and direct
fractional-part results do not repair the gap

If Xiao's second moment (158.SA37) applied to all needed modes with
the literal weights, dyadic Cauchy would give a square-root-scale
frequency aggregate and would be strong enough.  Its first exact
mismatches are:

1. the theorem starts at \(H\geq M^{1/2+\delta}\), while Vaaler
   requires control of the decisive low modes
   \(1\leq h\leq J\), \(J\asymp M^{1/4}\);
2. it averages consecutive integer \(h\), whereas (158.SA65) has
   frequency \(h\sqrt N\), nonintegral when \(N\) is nonsquare and a
   sparse progression when \(N\) is square;
3. it sums consecutive unweighted radicands \(a\), whereas the project
   has the two mod-four progressions, \(\chi_4\), a prescribed growing
   dilation \(N\), moving endpoints, and the root-indexed literal
   boundary weight.

Padding any of these sparse or weighted sets into (158.SA37) is not a
source-legal inference.

Shparlinski--Xiao Theorem 2.2 is the closest exact moving-cutoff root
card, but in (158.SA19) the outer \(m\) carries \(\alpha_m\) and the
root \(x\) is independently summed with a fixed additive mode.  In
(158.SA10), the selected root is \(k(\ell)\) and the coefficient itself
is \(F_{k-1}(k)\) or \(F_{-k}(k)\).  In addition, their modulus is a
large prime, their right side is \(amn+b\), and
\((a\lambda,q)=1\); the project modulus is the arbitrary even
composite \(4N\), its two affine cell orientations are strict, and its
sign is the character of the quotient after division by \(N\).
Theorem 2.3 smooths the inner cutoff but does not change these root,
modulus, and coefficient mismatches.  Theorem 2.5 additionally
requires separated weights.

Heath-Brown's character is evaluated directly on a nonsingular binary
quadratic form modulo an odd squarefree \(q\), over a two-dimensional
convex region.  The project character has fixed conductor four and is
evaluated on the quotient \((k^2-s)/N\) only after an \(N\)-divisibility
selector; the physical support is a selected one-dimensional moving
cell with a root-dependent coefficient.  Chang's theorem is a full
interval sum of a primitive character of the growing modulus.  Taking
the project character means \(q=4\), contradicting (158.SA26) for a
growing interval; taking \(q=4N\) does not turn \(G_N(k^2-s)\) into a
primitive character modulo \(4N\).  Neither theorem translates.

The direct floor parameterization is no better.  Summing by \(k\), the
cell quotient is governed by

\[
\ell(k)=\left\lfloor\frac{(k+1/2)^2}{N}\right\rfloor
\tag{158.SA80}
\]

away from the retained half-open boundary convention.  The function
\((k+1/2)^2/N\) depends on \(N\) and has constant second derivative
\(2/N\), corresponding to decay exponent \(0\), outside
(158.SA39)--(158.SA40); the source also requires a prime character
modulus.  Summing by \(\ell\), the function
\(\sqrt{N\ell}\) has second-derivative exponent \(3/2\), again outside
\(2/3<\kappa<1\), and \(\chi_4\) is on \(\ell\), not on
\(\lfloor\sqrt{N\ell}\rfloor\).  The Beatty theorem has a fixed
irrational linear slope, while (158.SA61)--(158.SA63) are nonlinear,
depend on the growing \(N\), and have moving endpoints.

Finally, the Elkies--McMullen and El-Baz--Marklof--Vinogradov results
are limiting laws for the unweighted undilated sequence
\(\{\sqrt n\}\).  They do not give a quantitative bound uniform in
the growing dilation \(N\), a prescribed interval of length
\(\asymp M^{-1/4}\) or its moving analogue, the sign \(\chi_4\), or the
literal profile.  A qualitative limiting distribution cannot be
substituted into (158.SA12).

DFI Theorem 2.5 also cannot be delta-localized to
\(c=4N/d\).  A unit-width bump at a growing modulus violates uniform
control of the derivatives and transforms in (158.SA17), and every
Maaß, residual, continuous, and holomorphic piece remains.  The
positive and negative trace blocks also include sign configurations
not simultaneously covered by its printed \(m,n\geq1\) card.  DFI
Lemma 6.1 remains an exact pointwise match only.

## 4. First doubtful or unproved step

After the exact inversion, safe removed-mode estimates, and endpoint
deletion, the first unproved object is the strict selected sum
(158.SA10)--(158.SA12).

The first source insertion already fails at the coefficient interface:
no audited theorem permits the selected root \(k(\ell)\) to carry the
literal coefficient \(F_{k-1}(k)\) or \(F_{-k}(k)\), and the repository
hypotheses do not give the diagonal BV statement (158.SA54).  The
residual boundary factors (158.SA65a) have additional \(k\)-dependence
and are not a fixed Fourier-frequency shift; they require their own BV
or a joint estimate.  Even if these coefficient issues are granted
away, the exact selector has moving Fourier endpoints, so Abel
variation loses the \(1/h\) coefficient decay.  Even if all of those
defects are granted away and one uses the easier fixed-endpoint model,
the most favorable threshold among the explicitly stated audited
favorable-model lines is (158.SA77), incompatible with
\(M\leq N^{1/2}\).

These are three ordered interface failures:

1. literal root-indexed coefficient and profile;
2. \(k\)-dependent residual boundary phase and moving sharp selector,
   including their separate variation/truncation requirements;
3. restored \(N,M,J\) power in the stated favorable model.

They establish a no-go for the audited theorem-insertion routes, not
for a future coefficient-sensitive signed theorem and not for the
truth of the target itself.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| literal_paired_interior_trace | **PASS.** Equation (158.SA1) keeps every odd \(d\mid N\), \(c=4N/d\), both complementary nonzero modes, positive prefix, negative suffix, literal coefficients, and exterior normalization. |
| full_frequency_delta_inversion | **PASS.** Equations (158.SA42)--(158.SA44) give the exact half-period inversion and quotient projector, with signs and \(1/(2N)\) normalization checked. |
| zero_trace_piece | **PASS / TARGET-SAFE.** The trace-level interval estimate (158.SA45), not the total-row theorem, gives (158.SA47). |
| Nyquist_trace_piece | **PASS / TARGET-SAFE.** Equation (158.SA46) gives the same restored bound.  For \(c=4\), zero and Nyquist exhaust the frequency set. |
| endpoint_polynomial_p_adic_roots | **PASS / TARGET-SAFE SUBROW.** Complete \(p=2,3\) and odd-prime tables are in (158.SA48)--(158.SA49); the endpoint has \(N^\varepsilon\) atoms. |
| strict_prefix_suffix_survivor | **PASS / OPEN.** Equations (158.SA5), (158.SA8), and (158.SA9) delete only \(s=k-1\) and \(s=-k\); all strict terms survive. |
| selected_coordinate_boundary_weight | **PASS / SOURCE NO-MATCH.** Equation (158.SA10) retains \(F_{k-1}(k)\), \(F_{-k}(k)\), \(\chi_4(\ell)\), and all profile tests; (158.SA65a) records the \(k\)-dependent residual boundary phases.  No diagonal, residual-phase, or joint BV is invented, and the phases are not called a fixed frequency shift. |
| positive_negative_profiles_and_endpoints | **PASS.** Both signs, opposite orientations, asymmetric cell, half-open conventions, transitions, and external \(B_{1,U}(1)\) seam remain distinct. |
| N_M_V_d_c_power_ledger | **PASS / METHOD OBSTRUCTION.** Removed rows give (158.SA47); quadratic completion gives raw \(N^{1/2}\); masked exponent pairs give exact thresholds (158.SA70), (158.SA77).  The raw target is \(M^{3/4}\), not \(M^{1/2}\). |
| source_theorem_trace_match | **NO MATCH.** DFI Lemma 6.1 matches only one kernel; Müllner matches only unweighted quadratic intervals; root, character, floor, fractional-part, moment, and spectral cards fail explicit hypotheses recorded above. |
| upper_capacity_vs_signed_sum | **PASS.** Equations (158.SA58), (158.SA69), and (158.SA78) are upper capacities.  Their failure to reach the target is not a lower bound.  Equation (158.SA11) is cardinality only. |
| profile_bulk_and_downstream_scope | **PASS.** No trace conclusion is transferred to the profile bulk, full paired matrix, \(D>1\), \(L>1\), generic \(t=1\), \(t\geq2\), cross, M2, endpoint uniformity, M9, bridge, target, or exponent owners. |
| residual_mask_fourier_truncation | **PASS / OBSTRUCTION.** Equations (158.SA60)--(158.SA67) retain the exact residual mask and separate the model wave from the \(k\)-dependent factors (158.SA65a).  Even the optimistic replacement of the unsigned Vaaler boundary-kernel incidence by \(M/J\) forces \(J\geq M^{1/4}\); moving endpoints, residual phases, and literal coefficients make the benchmark easier than the actual problem. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

### Repository evidence

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- strategy/round158_d1_paired_interior_cell_trace_strategy.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/barrier_packet.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/candidates/conductor_round158_cell_trace_seed.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reviews/independent_source_round158.md, Section 3
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reports/nonzero_theta_matrix_source_audit.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reviews/independent_source_round157.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reports/quadratic_root_completion_source_audit.md

The literal trace, selected-coordinate rewrite, support count, and
removed-row identities are internal candidate evidence, not external
theorems.  The source verdict relies only on the primary papers below.

### Primary sources audited

1. Jeffrey D. Vaaler, [*Some extremal functions in Fourier analysis*](https://doi.org/10.1090/S0273-0979-1985-15349-2), Bulletin of the AMS 12 (1985), Theorems 18--19.
2. Clemens Müllner, [*The Rudin--Shapiro Sequence and Similar Sequences Are Normal Along Squares*](https://doi.org/10.4153/CJM-2017-053-1), Canadian Journal of Mathematics 70 (2018), Theorem 5.3 and Lemma 5.4.
3. W. Duke, J. B. Friedlander, and H. Iwaniec, [*Weyl Sums for Quadratic Roots*](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf), IMRN 2012, Theorem 2.5 and Lemma 6.1; [DOI](https://doi.org/10.1093/imrn/rnr112) and [erratum](https://doi.org/10.1093/imrn/rnr240).
4. Igor E. Shparlinski and Yixiu Xiao, [*Shifted bilinear sums of Salié sums and the distribution of modular square roots of shifted primes*](https://arxiv.org/html/2601.10113v1), arXiv:2601.10113v1, Theorems 2.2, 2.3, and 2.5.
5. D. R. Heath-Brown, [*Small Solutions of Quadratic Congruences, and Character Sums with Binary Quadratic Forms*](https://arxiv.org/html/1411.4816v1), arXiv:1411.4816v1, Theorem 3.
6. Mei-Chu Chang, [*Short character sums for composite moduli*](https://arxiv.org/html/1201.0299v2), arXiv:1201.0299v2, Theorem 5.
7. William D. Banks and Igor E. Shparlinski, [*Multiplicative character sums with twice-differentiable functions*](https://doi.org/10.1093/qmath/han023), Quarterly Journal of Mathematics 60 (2009), Theorem 6.1.
8. William D. Banks and Igor E. Shparlinski, [*Character sums with Beatty sequences on Burgess-type intervals*](https://arxiv.org/abs/math/0608042), arXiv:math/0608042, Theorem 4.1.
9. Jean Bourgain, [*Decoupling, exponential sums and the Riemann zeta function*](https://arxiv.org/abs/1408.5794v2), arXiv:1408.5794v2, Theorem 6.
10. Terence Tao, Tim Trudgian, and Andrew Yang, [*New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*](https://arxiv.org/html/2501.16779v1), arXiv:2501.16779v1, Definitions 11--12, Lemmas 13--15, Table 1, and Theorem 20.
11. Yixiu Xiao, [*Moment Estimates and Discrepancy for Sums of Square Roots Modulo One*](https://arxiv.org/html/2606.28986v1), arXiv:2606.28986v1, Theorems 1.1--1.3 and Lemma 2.5.
12. Noam D. Elkies and Curtis T. McMullen, [*Gaps in \(\sqrt n\bmod1\) and ergodic theory*](https://doi.org/10.1215/S0012-7094-04-12314-0), Duke Mathematical Journal 123 (2004), 95--139.
13. Daniel El-Baz, Jens Marklof, and Ilya Vinogradov, [*The two-point correlation function of the fractional parts of \(\sqrt n\) is Poisson*](https://arxiv.org/abs/1306.6543), arXiv:1306.6543, Theorem 1 and the stated moment results.

## 7. Recommended state effect

Recommend **no proof-state promotion from the literature audit**.
Retain the exact endpoint-only target-safe subrow and the separate zero
and Nyquist trace capacities as candidate mathematical evidence, but
do not identify them with the strict trace.

Record the first missing external input as:

> A fixed-\(N\), coefficient-sensitive signed theorem for the
> \(\chi_4\)-twisted nearest-square residual mask which keeps the
> literal root-indexed boundary coefficients \(F_{k-1}(k)\) and
> \(F_{-k}(k)\), both moving strict interval selectors, the actual
> complex phase and profiles, and proves raw
> \(O(M^{3/4}X^\varepsilon)\) uniformly in the frozen cone.

If a terminal route label is required on source evidence, use
**paired_interior_cell_trace_no_go** only in the qualified sense
“no matching primary theorem through 25 August 2026.”  Do not read
this as an impossibility result, a signed lower bound, or evidence
against a future coefficient-sensitive theorem.  Do not transfer it
to the profile bulk, the full paired interior matrix, another owner,
M9, the bridge, the quarter theorem, or a global exponent.
