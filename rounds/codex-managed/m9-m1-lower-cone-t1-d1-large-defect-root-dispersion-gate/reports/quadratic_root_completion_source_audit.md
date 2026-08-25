# Round 154 primary-source audit: quadratic-root completion

- Campaign: `m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate`
- Role: primary-source auditor
- Literature checked through: 25 August 2026
- Starting graph: `6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`
- Status: candidate evidence only; no shared proof state was edited

## 1. Result

### Source-audited ambient-completion no-go, with one genuine source match

Let

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor\asymp R^4,
 \qquad J=M^{3/4},\qquad
 K\asymp \sqrt{NM}=R^2M^{1/2},
 \qquad 1\ll M\le R^2\asymp N^{1/2}.
\tag{154.SA1}
\]

For the literal direct large-defect wave in the brief, the exact
root-defect reparametrization and the modulo-\(4N\) quotient-character
identity are correct.  The literature audit gives the following more
precise conclusion.

1. After the congruence \(N\mid k^2-j\) has already been imposed, the
   apparent family of odd \(h\pmod {4N}\) consists of \(N\) copies of each
   of two mod-four rows; after the \(\chi _4(h)\) sign and the odd-quotient
   restriction, even those two weighted rows agree.  Hence no theorem
   requiring genuinely distinct \(h\)-frequencies can be applied to the
   already selected root set.
2. This is **not** a global objection to the lawful Fourier-selector
   expansion.  Before the \(h\)-sum is evaluated, off-congruence
   \((k,j)\) points remain and the rows
   \(e_{4N}(h(k^2-j))\) are genuinely quadratic.  Completing this ambient
   \(k\)-sum is legitimate.
3. Termwise incomplete-Gauss estimation, using Clemens Müllner's
   Theorem 5.3 and Lemma 5.4 with every imprimitive gcd restored, gives on
   a dyadic defect block \(V<|j|\le2V\)

   \[
    |Q_U(V)|\ll_\varepsilon
       M^{-3/4}V N^{1/2}X^\varepsilon.
   \tag{154.SA2}
   \]

   Already at \(V=J\), its right side is \(N^{1/2}=R^2\), so this
   direct use proves neither the target nor a range.
4. Full finite Fourier completion in \(k\), followed by the exact
   all-parity Gauss evaluation, is better.  On the stratum
   \(d=(h,N)\), every nonzero dual term is exactly a theta-multiplier
   Kloosterman sum

   \[
      K(-v^2,-j;4N/d)
   \tag{154.SA3}
   \]

   in the normalization of Duke--Friedlander--Iwaniec.  Their Lemma 6.1
   therefore is a genuine, source-legal match, including arbitrary
   composite moduli divisible by four.  The complete gcd, zero-frequency,
   Fourier-tail, endpoint, profile, and divisor ledger yields

   \[
     \boxed{
     |Q_U(V)|\ll_\varepsilon
       \bigl(M^{-3/4}V+M^{-1/4}\bigr)X^\varepsilon}
   \tag{154.SA4}
   \]

   This independently certifies the full first block \(J<|j|\le 2J\)
   and, by the same uniform estimate, every fixed or polylogarithmic
   collar \(J<|j|\le J(\log X)^A\).  It gives no positive-power
   enlargement in the defect variable and is not an all-scale estimate.
   The exact cell contains blocks up to \(V\asymp K\), where (154.SA4)
   becomes

   \[
      N^{1/2}M^{-1/4}X^\varepsilon
      =R^2M^{-1/4}X^\varepsilon
      \ge R^{3/2}X^\varepsilon.
   \tag{154.SA5}
   \]

   Thus the first power obstruction after the lawful Kloosterman gain is
   the outer full defect range, not the complete Gauss sum and not a
   supposed global degeneration of the ambient \(h\)-family.
5. The exact stationary row also survives.  Writing \(h=4N-a\), the
   selector phase combined with the residual phase has

   \[
    \phi_{a,k}(j)
      =-\frac{a(k^2-j)}{4N}+\sqrt{k^2-j}-k.
   \tag{154.SA6}
   \]

   Its zero-frequency stationary point is

   \[
      \sqrt{k^2-j}=\frac{2N}{a},\qquad
      \frac{k^2-j}{N}=\frac{4N}{a^2},\qquad
      e(\phi_{a,k}(j))=e(N/a).
   \tag{154.SA7}
   \]

   This is precisely the earlier reciprocal-row principal phase.  A
   van der Corput transform does not turn (154.SA7) into a free gain:
   Vandehey's Theorem 1.1 produces this main term together with starred
   endpoints and an error of curvature scale \(K^{3/2}\).  With the
   actual \(M^{-3/4}\) weight that error is \(N^{3/4}\) before the outer
   selector and rows are restored.  The actual cell, profile support,
   strict mask, possible endpoint stationary points, and nonstationary
   rows must all be retained.
6. The audited quadratic-root large sieve, fixed-polynomial Weyl sums,
   sparse-root energy, modular-parabola restriction, and square-modulus
   large sieve theorems either fail a literal modulus/coefficient/average/
   weight hypothesis or have a positive power loss even under a more
   favorable prime or squarefree idealization.  None controls the
   \(j\)-dependent Fourier coefficients left in (154.SA3).

Consequently DFI Lemma 6.1 gives a source-legal target on the first
defect collar, but no audited primary-source theorem proves
\(Q_U\ll_\varepsilon X^\varepsilon\) for the complete defect range
throughout the frozen open side \(M^{449}\ll R^{780}\), or even enlarges
that collar by a fixed positive power.  The source-scoped all-scale
terminal label is
`large_defect_root_dispersion_no_go`.  This is a rigorous obstruction to
the audited specializations, not a lower bound for \(Q_U\), not a theorem
that every completion or dispersion method must fail, and not a
literature-impossibility claim.

## 2. Exact statement and hypotheses

### 2.1 Literal project object

The object audited is

\[
 Q_U=\sum_{\substack{n>0\ \mathrm{odd}}\\
              |k(n)^2-Nn|>J}}
 \chi _4(n)n^{-3/4}A_U(n)e(\sqrt{Nn}),
 \qquad
 k(n)=\left\lfloor\sqrt{Nn}+\frac12\right\rfloor .
\tag{154.SA8}
\]

The inherited profile is extended by zero with every actual component,
transition, and endpoint, and satisfies

\[
 \|A_U\|_\infty+\operatorname {Var}A_U
 \ll_\varepsilon X^\varepsilon.
\tag{154.SA9}
\]

It confines \(n\) to a fixed dilation of \(M\).  The scalar
\(B_{1,U}(1)\) remains outside (154.SA8) and has
\(O_\varepsilon(X^\varepsilon)\) size.  The exact-square and
small-defect sectors are restored only when forming the full \(P_U\) for
the principal self-return; they are absent from \(Q_U\) by definition.
The direct \(Q_U\) in (154.SA8) does include the large-square-factor
sector, even though Round 152 separately owns that sector.  Bounded
\(M\) and the already owned range \(M^{449}\gg R^{780}\) remain outside
the frozen open-side audit.

For \(j=k^2-Nn\), the exact formula is

\[
\begin{split}
 Q_U={}&\sum_{k\ge1}
 \sum_{\substack{-k\le j\le k-1,\ |j|>J\\
                  N\mid k^2-j,\ (k^2-j)/N\ \mathrm{odd}}}
 \chi _4\!\left(\frac{k^2-j}{N}\right)
 \left(\frac{k^2-j}{N}\right)^{-3/4}
 A_U\!\left(\frac{k^2-j}{N}\right)  \\
 &\hspace{25mm}\times
 e\!\left(-\frac{j}{k+\sqrt{k^2-j}}\right).
\end{split}
\tag{154.SA10}
\]

On support, \(k\asymp K\), the total inherited \(k\)-interval has length
\(O(K)<N\), and \(2k<N\) for fixed support dilates and sufficiently large
\(X\).

### 2.2 Quotient character and all-parity Gauss card

For every integer \(t\), put

\[
 G_N(t)={\bf1}_{N\mid t}\chi _4(t/N).
\tag{154.SA11}
\]

The exact finite Fourier identity is

\[
 G_N(t)=-\frac{i}{2N}
 \sum_{\substack{h\pmod {4N}\\h\ \mathrm{odd}}}
 \chi _4(h)e_{4N}(ht).
\tag{154.SA12}
\]

This function is not a Dirichlet character modulo \(4N\): it is an
additive quotient pullback supported on the two residue classes
\(N,3N\pmod {4N}\).  Primitive-character large-sieve statements therefore
do not apply merely by calling (154.SA11) a character.

For the complete quadratic sum

\[
 \mathcal G(h,b;4N)=
 \sum_{x\pmod {4N}}e_{4N}(hx^2+bx),
\tag{154.SA13}
\]

let

\[
 d=(h,4N)=(h,N),\quad a=h/d,\quad q'=4N/d.
\tag{154.SA14}
\]

Here \(d\) is odd, \(q'\equiv0\pmod4\), and \((a,q')=1\).  Then

\[
 \mathcal G(h,b;4N)=0
 \quad\text{unless}\quad d\mid b\ \text{and}\ b/d\ \text{is even}.
\tag{154.SA15}
\]

If \(b/d=2v\), then

\[
\begin{split}
 \mathcal G(h,b;4N)
  ={}&d(1+i)\epsilon_a^{-1}
       \left(\frac{q'}a\right)\sqrt{q'}
       e_{q'}(-\bar a v^2),                                      \\
 |\mathcal G(h,b;4N)|={}&\sqrt{8Nd},
\end{split}
\tag{154.SA16}
\]

where \(\epsilon_a=1\) for \(a\equiv1\pmod4\),
\(\epsilon_a=i\) for \(a\equiv3\pmod4\), and
\((q'/a)\) is the Kronecker symbol.  Thus no odd-modulus-only Gauss
formula is enough for this project modulus.

### 2.3 Primary-source theorem cards

#### Incomplete quadratic Gauss sums

In Clemens Müllner,
[*The Rudin--Shapiro Sequence and Similar Sequences Are Normal Along
Squares*](https://doi.org/10.4153/CJM-2017-053-1), Theorem 5.3 states,
for \(a,b\in\mathbb Z\) and \(m\ge1\),

\[
 \left|\sum_{x=0}^{m-1}e_m(ax^2+bx)\right|
 \le \sqrt{2m(a,m)}.
\tag{154.SA17}
\]

Its Lemma 5.4 states, for integers \(a,b,m,L,n_0\), \(m\ge1\),
\(L\ge0\),

\[
 \left|\sum_{x=n_0+1}^{n_0+L}e_m(ax^2+bx)\right|
 \le
 \left(\frac Lm+1+\frac2\pi\log\frac{2m}{\pi}\right)
 \sqrt{2m(a,m)}.
\tag{154.SA18}
\]

There is no parity, primitivity, or endpoint omission in (154.SA18), but
there is no arbitrary coefficient sequence either.  Bounded-variation
partial summation is therefore required for the project profile.

#### Even theta Kloosterman and Salié sums

Duke--Friedlander--Iwaniec,
[*Weyl Sums for Quadratic Roots*](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf),
define, for \(c\equiv0\pmod4\),

\[
 K(m,n;c)=\sum_{x\pmod c}^{*}
 \epsilon_x\left(\frac cx\right)
 e_c(m\bar x+nx).
\tag{154.SA19}
\]

Their Lemma 6.1 is the all-composite estimate

\[
 |K(m,n;c)|\le (m,n,c)^{1/2}c^{1/2}\tau(c).
\tag{154.SA20}
\]

This is the exact source used in (154.SA3).  By contrast, Stephan Baier,
[*Partial progress towards the large sieve for square moduli*](https://arxiv.org/html/2605.01635v3),
Proposition 17 treats

\[
 \mathcal K(a,b,c)=\sum_{x=0}^{c-1}
 \left(\frac xc\right)e_c(a\bar x+bx)
\tag{154.SA21}
\]

only for \(c=p\) or \(p^2\), \(p\) odd, and \((a,p)=1\), proving
\(\mathcal K(a,b,c)\ll c^{1/2}\).  Baier's Hypothesis 18 proposes, rather
than proves, square-root cancellation for a short interval in (154.SA21).
It is an odd-modulus Jacobi-character/unit-inverse statement and cannot
replace (154.SA20) for arbitrary \(4N/d\).

#### Van der Corput transform, main term, and endpoints

Joseph Vandehey,
[*Error term improvements for van der Corput transforms*](https://arxiv.org/html/1205.0090),
Theorem 1.1 assumes that \(f\) is real and \(C^4[a,b]\), that
\(f''(x)\asymp T_0/M_0^2\),
\(f^{(3)}(x)\ll T_0/M_0^3\),
\(f^{(4)}(x)\ll T_0/M_0^4\), with \(M_0\ge b-a\), and that \(g\) is real
of bounded variation \(\mathcal V\).  It gives

\[
 \sum_{a\le n\le b}g(n)e(f(n))
 =\sum_{f'(a)\le r\le f'(b)}
 \frac{g(x_r)e(f(x_r)-rx_r+1/8)}{\sqrt{f''(x_r)}}
 +O\!\left((\mathcal V+|g(a)|)
 \left(\frac{M_0}{\sqrt{T_0}}+\log(f'(b)-f'(a)+2)\right)\right),
\tag{154.SA22}
\]

with \(f'(x_r)=r\).  The source uses starred half weights when a
summation endpoint is integral.  Its Theorem 1.5 (Kusmin--Landau) requires
monotone \(f'\) and a positive lower bound for the distance of \(f'\) to
every integer.  Thus it does not cover the stationary rows in (154.SA7)
without a separate main term.

#### Quadratic-congruence-root large sieves and fixed-polynomial Weyl sums

Fouvry--Iwaniec,
[*Gaussian primes*](https://matwbn.icm.edu.pl/ksiazki/aa/aa79/aa7935.pdf),
Lemma 2 states, for arbitrary complex \(\alpha_n\),

\[
 \sum_{8D<d\le9D}\ \sum_{\nu^2+1\equiv0\ (d)}
 \left|\sum_{n\le T}\alpha_ne(\nu n/d)\right|^2
 \le72(D+T)\sum_{n\le T}|\alpha_n|^2.
\tag{154.SA23}
\]

The polynomial \(X^2+1\) is fixed and the modulus is averaged.  The
project instead fixes the modulus \(N\), varies the right side \(j\) in
\(k^2\equiv j\pmod N\), and selects a short real root interval with a
root-dependent quotient profile.

Theorem 1.1 of Duke--Friedlander--Iwaniec assumes \(h>1\), \(q_0>1\), a
positive odd fundamental discriminant \(D\), and a smooth \(f\) supported
on \([Y,2Y]\) with \(|f|\le1\), \(y^2|f''(y)|\le1\).  For

\[
 W_h(D)=\sum_{c\equiv0\ (q_0)}f(c)
 \sum_{b^2\equiv D\ (c)}e(hb/c)
\tag{154.SA24}
\]

it proves

\[
 W_h(D)\ll h^{1/4}(Y+h\sqrt D)^{3/4}
 D^{1/8-1/1331}.
\tag{154.SA25}
\]

Again the discriminant is fixed and the modulus is smoothly averaged;
the project has both signs of a varying, often nonfundamental or square,
defect at one fixed modulus.

Hieu T. Ngo,
[*On Roots of Quadratic Congruences*](https://arxiv.org/html/2107.13301),
Theorem 1.1 assumes a fixed irreducible integral quadratic \(f\) of
positive discriminant and fixed nonzero \(h\).  With

\[
 \rho_h(n)=\sum_{\nu\pmod n,\ f(\nu)=0}e(h\nu/n),\qquad
 \mathcal W_h(x,N_0)=
 \sum_{x<n<2x,\ n\equiv0\ (N_0)}\rho_h(n),
\tag{154.SA26}
\]

it proves

\[
 \mathcal W_h(x,N_0)
 \ll_\varepsilon
 \left(x^{12/13}N_0^{-11/13}h^{1/13}+h\right)x^\varepsilon.
\tag{154.SA27}
\]

Ngo's Theorem 2.5 is a smooth two-variable spectral Kloosterman estimate:
its weight is supported on \(C<c<2C\), \(K_0<\kappa<2K_0\), has derivative
parameter \(Y_0\ge1\), and its right side contains both

\[
 K_0^{1/2}(K_0^{1/4}q^{-1/4}+1)C^{1/2}Y_0^{3/2}(h,q)^{1/4}
\tag{154.SA28}
\]

and

\[
 K_0^{1/2}q^{1/2}
 (Y_0^{3/4}+K_0^{1/2}q^{-1/2})Y_0^{7/4},
\tag{154.SA29}
\]

up to \((qY_0K_0C)^\varepsilon\).  The second spectral/exceptional-scale
term may not be deleted.  A single fixed modulus, nonsmooth exact cell,
changing first frequency \(-v^2\), and the \(j\)-dependent project weight
do not specialize to this theorem.

#### Current modular-root bilinear theorem

In Baier's arXiv:2605.01635v3, Theorem 6 considers

\[
 \Sigma_f=\sum_{|\ell|\le L}\sum_{1\le m\le M_0}
 \alpha_\ell\beta_m e_r(\ell\sqrt{jm})e(\ell f(m)),
\tag{154.SA30}
\]

where all modular roots are summed, \((r,j)=1\),
\(r^\varepsilon\le L,M_0\le r^{1-\varepsilon}\),
\(|f'|\le F\le L^{-1}\), and

\[
 r^\varepsilon\le H\le\min\{(LF)^{-1},M_0\}.
\tag{154.SA31}
\]

For odd squarefree \(r\), it proves

\[
 \Sigma_f\ll
 (H^{-1/2}L^{1/2}M_0+L^{1/2}M_0^{1/2}r^{1/4}+M_0)
 \|\alpha\|_2\|\beta\|_\infty r^\varepsilon.
\tag{154.SA32}
\]

For \(r=p^2\), an additional
\(H^{-1/2}L^{1/2}M_0^{1/2}r^{3/8}\) occurs.  Corollary 7, with
\(f=0,H=M_0\), gives in the odd-squarefree case

\[
 \Sigma_0\ll
 (L^{1/2}M_0^{1/2}r^{1/4}+M_0)
 \|\alpha\|_2\|\beta\|_\infty r^\varepsilon,
\tag{154.SA33}
\]

and adds \(L^{1/2}r^{3/8}\) for \(p^2\).  Its conditional prime line
under Hypothesis 18 is

\[
 \Sigma_0\ll
 (L^{1/2}M_0^{3/4}+M_0^{1/2}r^{1/4}+M_0)
 \|\alpha\|_2\|\beta\|_\infty r^\varepsilon.
\tag{154.SA34}
\]

The project modulus is arbitrary, while (154.SA32)--(154.SA34) require
odd squarefree, prime, or prime-square modulus.  More importantly,
\(\alpha_\ell\beta_m\) is separated, the archimedean phase depends only
on \(m\), and every modular root is included.  In (154.SA10), the root
representative determines the quotient, actual profile, cell, and exact
reciprocal phase jointly.

#### Sparse modular roots

Kerr--Shkredov--Shparlinski--Zaharescu,
[*Energy bounds for modular roots and their applications*](https://doi.org/10.1017/S1474748023000397),
Theorem 1.1 assumes \(q\) prime, \(j\in\mathbb F_q^*\), and \(V\le q\),
and proves

\[
 \mathsf T_{2,2}(V;j,q)
 \ll (V^{3/2}q^{-1/2}+1)V^{2+o(1)}.
\tag{154.SA35}
\]

For \(a,h\in\mathbb F_q^*\), Corollary 2.1 treats separated bounded
weights on two dyadic intervals \(A,B\le q/2\):

\[
 W_{a,q}=\sum_{m\sim A}\sum_{n\sim B}\alpha_m\beta_n
 \sum_{x^2=amn}e_q(hx)
\tag{154.SA36}
\]

and proves

\[
 |W_{a,q}|\le q^{1/8+o(1)}(AB)^{3/4}
 \left(A^{3/16}q^{-1/16}+1\right)
 \left(B^{3/16}q^{-1/16}+1\right).
\tag{154.SA37}
\]

It has prime modulus, all finite-field roots, product weights, and no
short real root cell or quotient profile.

#### Modular parabola

Kingsbury-Neuschotz,
[*On a Restriction Problem of Hickman and Wright for the Parabola over
\(\mathbb Z/N\mathbb Z\) for Squarefree \(N\)*](https://arxiv.org/html/2509.09885),
Theorem 1.1, for squarefree \(q\),
\(\Sigma=\{(t,t^2):t\in\mathbb Z/q\mathbb Z\}\), and every
\(F:(\mathbb Z/q\mathbb Z)^2\to\mathbb C\), proves

\[
 \left(\frac1{|\Sigma|}\sum_{m\in\Sigma}|\widehat F(m)|^2\right)^{1/2}
 \le2^{\omega(q)/4}q^{-1}
 \left(\sum_x|F(x)|^{4/3}\right)^{3/4},
\tag{154.SA38}
\]

with \(\widehat F(m)=q^{-1}\sum_xF(x)e_q(-x\cdot m)\).  The literal
completion modulus \(4N\) is never squarefree.  Passing to modulus \(N\)
would delete the two-adic quotient character.  Moreover (154.SA38) is a
full two-dimensional restriction norm, not a bound for the scalar
root-dependent coefficient in (154.SA10).

#### Large sieve for square moduli

Baier's Theorem 2 (arXiv:2605.01635v3) states, for \(Q,T\ge1\), real
\(M_1\), arbitrary complex \(a_n\) on \(M_1<n\le M_1+T\), and
\(Z=\sum|a_n|^2\),

\[
 \sum_{q\le Q}\sum_{\substack{1\le a\le q^2\\(a,q)=1}}
 \left|\sum_{M_1<n\le M_1+T}a_ne(na/q^2)\right|^2
 \ll_\varepsilon (QT)^\varepsilon
 \left(Q^3+T+\min\{Q^2T^{1/2},Q^{1/2}T\}\right)Z.
\tag{154.SA39}
\]

The theorem averages square moduli and reduced numerators.  The project
has the single modulus \(4N\), generally nonsquare, and every odd \(h\),
including \((h,N)>1\).

## 3. Proof or derivation

### 3.1 Exact cell, converse, and support multiplicity

A half-integer tie would make \(4Nn\) an odd square, impossible modulo
four.  Therefore

\[
 k-\frac12<\sqrt{Nn}<k+\frac12.
\tag{154.SA40}
\]

Squaring and using \(j=k^2-Nn\in\mathbb Z\) gives
\(-k\le j\le k-1\).  Conversely, this cell, divisibility
\(N\mid k^2-j\), and positivity give

\[
 (k-\tfrac12)^2<k^2-j<(k+\tfrac12)^2,
\tag{154.SA41}
\]

so \(k\) is the unique nearest integer.  The cell contains \(2k<N\)
integers, hence at most one representative of \(k^2\pmod N\).  If
\(n_2>n_1\) lie in the fixed support dilation, then

\[
 \sqrt{Nn_2}-\sqrt{Nn_1}
 =\frac{N(n_2-n_1)}{\sqrt{Nn_2}+\sqrt{Nn_1}}
 \gg\sqrt{N/M}\gg1,
\tag{154.SA42}
\]

so supported \(n\)'s give distinct \(k\)'s.  There are still only
\(O(MX^\varepsilon)\) selected pairs, with absolute weighted capacity
\(M^{1/4}X^\varepsilon\); neither fact is signed cancellation.

### 3.2 The two different meanings of the \(h\)-family

Write \(h=r+4m\), \(r\in\{1,3\}\), \(0\le m<N\).  If
\(t=k^2-j=Nn\) has already been imposed, then

\[
 e_{4N}(ht)=e(hn/4)=e(rn/4),
\tag{154.SA43}
\]

so the \(m\)-dependence disappears.  Also \(\chi _4(h)=\chi _4(r)\).
For odd \(n\), the two weighted rows satisfy

\[
 \chi _4(1)e(n/4)=\chi _4(3)e(3n/4)=i\chi _4(n).
\tag{154.SA44}
\]

Thus post-selection there is one weighted row with multiplicity \(2N\).
This is why an \(h\)-large-sieve gain on the already admissible roots is
false: all selected \(t=Nn\), \(n\) odd, are also congruent to \(N\pmod
{2N}\), so their Cauchy correlations collide.

In the ambient expansion of (154.SA12), however,

\[
 e_{4N}((r+4m)(k^2-j))
 =e_{4N}(r(k^2-j))e_N(m(k^2-j)),
\tag{154.SA45}
\]

and the second factor varies off congruence.  Its sum over \(m\) is exactly
what imposes \(N\mid k^2-j\).  Hence (154.SA43) cannot be used to reject
ambient completion, and (154.SA45) cannot simultaneously be treated as
independent-frequency cancellation after support has been imposed.

### 3.3 Direct incomplete-Gauss ledger

Choose a piecewise-constant extension of the discrete profile to real
arguments.  This does not change (154.SA8), because it is multiplied by
\(G_N(k^2-j)\), which vanishes off congruence.  For fixed \(j\), compose
it with \((k^2-j)/N\), retain the exact cell and zero extension, and put
the exact residual phase into the coefficient.  Monotonicity of
\((k^2-j)/N\), (154.SA9), and

\[
 \frac{d}{dk}\left(\sqrt{k^2-j}-k\right)
 \ll \frac{|j|}{K^2},\qquad |j|\le K,
\tag{154.SA46}
\]

give, uniformly on every proper interval,

\[
 \|B_j\|_\infty+\operatorname {Var}B_j
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{154.SA47}
\]

Müllner's Lemma 5.4 with \(m=4N\), \(a=h\), and interval length
\(O(K)<4N\), followed by Abel summation, gives

\[
 \left|\sum_kB_j(k)e_{4N}(hk^2)\right|
 \ll_\varepsilon M^{-3/4}\sqrt{N(h,N)}X^\varepsilon.
\tag{154.SA48}
\]

For odd \(h\pmod {4N}\), divisor stratification gives

\[
 \sum_{\substack{h\ \mathrm{odd}\\(\bmod\,4N)}}(h,N)^{1/2}
 \ll N\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon NX^\varepsilon.
\tag{154.SA49}
\]

Restoring the \(1/(2N)\) selector and \(O(V)\) positive and negative
defects proves (154.SA2).  The logarithmic incomplete-completion remainder
is included in \(X^\varepsilon\); no outer \(h\) or \(j\) sum was omitted.

### 3.4 Exact ambient completion and the theta-Kloosterman match

For fixed \(j\), zero-extend \(B_j\) to a complete residue system modulo
\(q=4N\), and define

\[
 \widehat B_j(b)=\sum_{x\pmod q}B_j(x)e_q(-bx).
\tag{154.SA50}
\]

Finite Fourier inversion is exact:

\[
 \sum_xB_j(x)e_q(hx^2)
 =\frac1q\sum_{b\pmod q}\widehat B_j(b)\mathcal G(h,b;q).
\tag{154.SA51}
\]

Partition the odd \(h\)'s by \(d=(h,N)\), write \(h=da\),
\(q'=q/d\), and use (154.SA15)--(154.SA16).  Only
\(b=2dv\) survives.  Since

\[
 \chi _4(a)\epsilon_a^{-1}=\epsilon_a,
\tag{154.SA52}
\]

the complete \(a\)-sum is exactly

\[
\begin{split}
 &\sum_{a\pmod {q'}}^*
 \chi _4(da)(1+i)\epsilon_a^{-1}
 \left(\frac{q'}a\right)
 e_{q'}(-aj-\bar av^2)                                      \\
 &\hspace{15mm}=
 (1+i)\chi _4(d)K(-v^2,-j;q').
\end{split}
\tag{154.SA53}
\]

The factor outside (154.SA53) is \(d\sqrt{q'}\).  DFI Lemma 6.1 therefore
gives the complete stratum bound

\[
 \ll q\,(v^2,j,q')^{1/2}\tau(q').
\tag{154.SA54}
\]

This proves that the ambient \(h\)-cancellation is genuine and prices all
two-adic and imprimitive strata.

From (154.SA47), discrete partial summation gives

\[
 |\widehat B_j(0)|\ll KM^{-3/4}X^\varepsilon,
 \qquad
 |\widehat B_j(b)|\ll
 M^{-3/4}X^\varepsilon
 \min\{K,q/|b|_q\}.
\tag{154.SA55}
\]

For a divisor \(c\mid(j,q')\), the condition \(c\mid v^2\) forces
\(s(c)\mid v\), where

\[
 s(c)=\prod_{p^e\parallel c}p^{\lceil e/2\rceil},
 \qquad c^{1/2}/s(c)\le1.
\tag{154.SA56}
\]

Expanding the gcd in (154.SA54) over divisors and summing the nonzero
Fourier modes harmonically therefore gives, for each \(d\mid N\),

\[
 \sum_{v\ne0}|\widehat B_j(2dv)|(v^2,j,q')^{1/2}
 \ll_\varepsilon M^{-3/4}(q/d)X^\varepsilon.
\tag{154.SA57}
\]

After the selector and Fourier factors, the sum of (154.SA57) over \(d\)
is \(O_\varepsilon(M^{-3/4}X^\varepsilon)\) for each \(j\).

The zero mode must be separate.  Uniformly for an interval of \(V\)
integers,

\[
 \sum_{j\in I}(j,Q)^{1/2}
 \ll_\varepsilon (V+Q^{1/2})Q^\varepsilon.
\tag{154.SA58}
\]

Using (154.SA55), its total contribution over a \(j\)-block is

\[
 \ll_\varepsilon
 M^{-3/4}\frac KN(V+N^{1/2})X^\varepsilon.
\tag{154.SA59}
\]

Since \(K/N\le1\) and \((K/N)N^{1/2}=M^{1/2}\), combining
(154.SA57)--(154.SA59) proves (154.SA4).  All dual frequencies, including
zero, all \(d=(h,N)\), and both defect signs are present.

### 3.5 Power translations for the remaining current sources

The following calculations are deliberately favorable to the source
theorems; the literal coefficient mismatches listed in Section 2 make the
actual applications weaker or illegal.

1. **Baier modular roots.**  Pretend \(N\) is odd squarefree, put the
   positive or negative defect into the source \(m\)-interval of length
   \(V\), and pad the \(\ell\)-range with zero coefficients so that only
   one root frequency remains.  Corollary 7 would give

   \[
     M^{-3/4}(N^{1/4}V^{1/2}+V)X^\varepsilon.
   \tag{154.SA60}
   \]

   At \(V=J\), the first term is
   \(N^{1/4}M^{-3/8}\ge N^{1/16}=R^{1/4}\).  The conditional prime
   Salié line retains this same term.  The prime-square line has an
   additional \(N^{3/8}M^{-3/4}\).
2. **Kerr--Shkredov--Shparlinski--Zaharescu.**  Pretend \(N\) is prime,
   set one dyadic factor to size one and the other to \(V\), and ignore
   root-dependent weights.  Corollary 2.1 gives

   \[
    M^{-3/4}
    \left(N^{1/8}V^{3/4}+N^{1/16}V^{15/16}\right)N^{o(1)}.
   \tag{154.SA61}
   \]

   At \(V=J\), these are at least \(N^{1/32}=R^{1/8}\) and
   \(N^{5/128}=R^{5/32}\), respectively.  At \(V=K\), they are
   \(N^{1/2}M^{-3/8}\) and \(N^{17/32}M^{-9/32}\).
3. **Square-modulus large sieve.**  Even in the special case \(N=s^2\),
   so \(4N=(2s)^2\), (154.SA39) covers only the unit \(h\)-stratum.  Encode
   \(k\mapsto k^2\) as a sparse sequence on an interval
   \(T\asymp K^2=NM\), take \(Q\asymp N^{1/2}\), and
   \(Z\ll K\).  Its large-sieve constant is

   \[
    \Delta\ll X^\varepsilon
    (N^{3/2}+NM+N^{5/4}M),
   \tag{154.SA62}
   \]

   where the minimum in (154.SA39) is \(N^{5/4}M\) for
   \(M\le N^{1/2}\).  Cauchy over the unit numerators and then the outer
   \(j\)-sum gives

   \[
    M^{-3/4}V N^{-1/2}(\Delta K)^{1/2}X^\varepsilon.
   \tag{154.SA63}
   \]

   At \(V=J\), the unavoidable \(N^{3/2}\) term in \(\Delta\) leaves
   \(N^{1/2}M^{1/4}\).  Nonunit \(h\)'s and nonsquare \(N\) remain
   untreated.
4. **Modular parabola and fixed-polynomial root sieves.**  Their modulus,
   fixed-discriminant, or modulus-average hypothesis fails before a
   project power can be assigned.  The factor \(2^{\omega(q)/4}\) in
   (154.SA38) is at best \(q^\varepsilon\), not a cancellation power, and
   the needed modulus \(q=4N\) is outside the theorem.

### 3.6 Stationary reciprocal row and why it is not an exact gain

For \(h=4N-a\), integrality of \(k^2-j\) gives (154.SA6).  Direct
differentiation shows

\[
 \phi'_{a,k}(j)=\frac{a}{4N}-\frac1{2\sqrt{k^2-j}},\quad
 \phi''_{a,k}(j)=-\frac1{4(k^2-j)^{3/2}},
\tag{154.SA64}
\]

and \(\phi^{(3)}\asymp K^{-5}\), \(\phi^{(4)}\asymp K^{-7}\) on the
cell.  Equations (154.SA7) follow.  At that point,

\[
 |\phi''_{a,k}(j)|^{-1/2}=2(2N/a)^{3/2}.
\tag{154.SA65}
\]

Multiplying by the literal algebraic weight at
\(n=4N/a^2\) gives the exact cancellation of the \(a\)-power

\[
 2(2N/a)^{3/2}(4N/a^2)^{-3/4}=2N^{3/4}.
\tag{154.SA66}
\]

Thus the stationary main term has phase \(e(N/a)\), profile
\(A_U(4N/a^2)\), and size \(N^{3/4}\), up to the fixed eighth-root factor
in (154.SA22).  It is present only if

\[
 -k\le k^2-4N^2/a^2\le k-1,\qquad
 |k^2-4N^2/a^2|>J,\qquad
 A_U(4N/a^2)\ne0,
\tag{154.SA67}
\]

with the correct sign block.  Unlike (154.SA40), a rational stationary
point may meet a cell or dyadic endpoint, so the source's starred endpoint
terms cannot be suppressed.

Apply Theorem 1.1 to \(-\phi_{a,k}\), whose second derivative is
positive, and then conjugate.  On a \(j\)-interval of length \(V\le K\),
take
\(M_0=V\) and \(T_0\asymp V^2/K^3\) in Vandehey's Theorem 1.1 (or
\(M_0=K,T_0\asymp K^{-1}\)).  Its curvature error is

\[
 \frac{M_0}{\sqrt{T_0}}\asymp K^{3/2}.
\tag{154.SA68}
\]

The actual BV coefficient makes this

\[
 M^{-3/4}K^{3/2}X^\varepsilon
 =N^{3/4}X^\varepsilon,
\tag{154.SA69}
\]

the same scale as (154.SA66), before the selector and all \((a,k)\) rows
are restored.  Away from integers one may use Kusmin--Landau, but the
near-zero stationary band and the near-one endpoint band must be split
off.  Summing the resulting first-derivative bounds over the \(a/(4N)\)
grid and over \(k\asymp K\) reproduces, at best, the scale

\[
 M^{-3/4}KX^\varepsilon
 =N^{1/2}M^{-1/4}X^\varepsilon,
\tag{154.SA70}
\]

which is (154.SA5).  Therefore (154.SA7) identifies the reciprocal
principal row; it is not a source theorem that the whole ambient transform
has gained cancellation.

## 4. First doubtful or unproved step

The first unproved continuation is now sharply localized.  It is **not**
the exact root coordinate, the quotient-character Fourier identity, the
all-parity Gauss evaluation, or the fixed-\(j\) theta-Kloosterman bound.
Those steps are proved in Section 3.

After (154.SA53), a successful argument must sum, without taking absolute
values in \(j\), expressions of the form

\[
 \sum_{V<|j|\le2V}\ \sum_{d\mid N}\ \sum_v
 \widehat B_j(2dv)
 K(-v^2,-j;4N/d),
\tag{154.SA71}
\]

for every \(J\lesssim V\lesssim K\).  The coefficient
\(\widehat B_j(2dv)\) is not a product coefficient: it contains the
literal quotient profile at \((k^2-j)/N\), the exact cell and its two
endpoints, the strict defect mask, and
\(e(-j/(k+\sqrt{k^2-j}))\).  Its stationary subfamily has the principal
phase (154.SA7) and the source-sized endpoint/error terms
(154.SA68)--(154.SA69).

None of the audited theorems has simultaneously:

- the arbitrary even composite moduli \(4N/d\) and every imprimitive
  \(d\)-stratum;
- a fixed modulus rather than a modulus average;
- the varying Kloosterman frequencies \((-v^2,-j)\);
- both signs and the complete interval \(J<|j|\le K\);
- root-dependent, nonseparable coefficients \(\widehat B_j(2dv)\);
- the actual hard cell/profile endpoints and stationary reciprocal main
  term; and
- a bound whose restored right side is \(X^\varepsilon\) below the owned
  threshold.

Replacing \(\widehat B_j(2dv)\) by separated bounded weights is the first
unlicensed step in a proposed use of Baier or Kerr et al.  Replacing the
fixed \(4N/d\) by a smooth modulus average is the first unlicensed step in
a proposed use of Fouvry--Iwaniec, Duke--Friedlander--Iwaniec Theorem 1.1,
or Ngo.  Treating the post-selection \(h\)-rows as distinct is the first
unlicensed step in a proposed \(h\)-large-sieve proof.  Calling
(154.SA7) an exact stationary gain without the terms in (154.SA22) is the
first unlicensed step in a stationary-phase proof.

The absence of a matching theorem in this audit is useful method evidence,
but it is not a proof that no such theorem exists or can be proved.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `literal_direct_large_defect_wave` | **PASS.** Equations (154.SA8)--(154.SA10) retain the actual \(D=d=L=1\) direct wave and the strict mask; no squarefree recombination surrogate is audited. |
| `owned_range_and_mask_order` | **PASS.** Exact-square, small-defect, and other scalar owners are removed before any Cauchy step. The audit concerns the open side below \(M^{449}\asymp R^{780}\), and claims no strict range. |
| `exact_root_defect_bijection` | **PASS.** Equations (154.SA40)--(154.SA42) prove both directions and positivity. |
| `nearest_cell_endpoints_and_converse` | **PASS.** The exact cell is \(-k\le j\le k-1\), with no replacement by \(|j|\le k\). Stationary rational endpoints are separately retained in (154.SA67). |
| `support_injectivity_and_unique_residue` | **PASS.** The supported \(k\)-interval has length \(O(K)<N\), \(2k<N\), one cell residue per \(k\), and distinct supported \(n\)'s give distinct \(k\)'s. |
| `mod4N_quotient_character_completion` | **PASS.** Equation (154.SA12) has the exact sign, \(1/(2N)\), every odd \(h\), and both parities of \(N\). Equations (154.SA43)--(154.SA45) distinguish selected and ambient rows. |
| `all_parity_two_adic_imprimitive_Gauss` | **PASS.** Equations (154.SA14)--(154.SA16) retain \(d=(h,N)\), the even-dual condition, modulus \(4N/d\), Kronecker multiplier, and zero cases. |
| `positive_negative_and_dyadic_defects` | **PASS.** All estimates are stated for both signs and every \(J\lesssim V\lesssim K\); the failing top block is explicitly priced. |
| `K_J_N_h_power_ledger` | **PASS/OBSTRUCTION.** \(J=M^{3/4}\), \(K=N^{1/2}M^{1/2}\), the individual \(h\)-gcd cost, the Kloosterman gain, and the restored top-block loss \(N^{1/2}M^{-1/4}\ge R^{3/2}\) are explicit. |
| `actual_profile_endpoints_and_B11` | **PASS.** Zero extension and BV retain every profile component, transition, and endpoint. \(B_{1,U}(1)\) remains external. Vandehey's starred endpoint convention is not silently identified with the strict project endpoints. |
| `Cauchy_diagonal_and_collision_survival` | **PASS/OBSTRUCTION.** On selected odd quotients, all weighted \(h\)-rows coincide and all \(t=Nn\) lie in one class modulo \(2N\); their correlations survive. Ambient off-congruence rows remain distinct and are treated by exact completion, not deleted. |
| `completion_remainder_and_outer_sums` | **PASS.** Müllner's logarithm, all \(h,j,d,v\) sums, Fourier zero mode, divisor sums, stationary main term, and Vandehey endpoint/error scale are restored. Finite Fourier inversion (154.SA51) itself has no truncation remainder. |
| `source_theorem_quadratic_root_match` | **PASS/PARTIAL MATCH.** DFI Lemma 6.1 exactly matches the ambient fixed-\(j\) theta Kloosterman sum and certifies the first fixed/polylogarithmic defect collar. Every theorem proposed for the remaining all-scale \(j\)-dispersion fails a stated modulus, average, coefficient, root-selection, smoothness, or power hypothesis. |
| `absolute_capacity_vs_signed_sum` | **PASS.** Raw pair count \(O(MX^\varepsilon)\), absolute capacity \(M^{1/4}X^\varepsilon\), signed mass, and theorem-derived upper bounds are kept distinct. No large right side is called a lower bound. |
| `D_L_generic_tge2_cross_and_downstream_scope` | **PASS.** Nothing here proves \(D>1\), \(L>1\), the growing-\(M\) generic \(t=1\) sector, an original \(t\ge2\) layer, the Round-138 cross owner, M2, endpoint assembly, M9, the bridge, the target, or a global exponent. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

### Project context read

The audit used every context artifact named in the brief:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round154_d1_large_defect_root_dispersion_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_exact_root_defect_reparametrization.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/reports/squarefree_bilinear_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/reviews/source_conductor_round153_final.md`; and
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reviews/source_conductor_round152_final.md`.

### Primary sources audited

1. C. Müllner, *The Rudin--Shapiro Sequence and Similar Sequences Are
   Normal Along Squares*, Canadian Journal of Mathematics 70 (2018),
   Theorem 5.3 and Lemma 5.4,
   [DOI/PDF](https://doi.org/10.4153/CJM-2017-053-1).
2. W. Duke, J. B. Friedlander, H. Iwaniec, *Weyl Sums for Quadratic
   Roots*, IMRN (2012), Theorem 1.1 and Lemma 6.1,
   [author PDF](https://www.math.ucla.edu/~wdduke/preprints/weylsums.pdf).
3. J. Vandehey, *Error term improvements for van der Corput transforms*,
   Theorem 1.1, Theorem 1.5, and endpoint conventions,
   [arXiv:1205.0090](https://arxiv.org/html/1205.0090).
4. E. Fouvry, H. Iwaniec, *Gaussian primes*, Acta Arithmetica 79 (1997),
   Lemma 2,
   [journal PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa79/aa7935.pdf).
5. H. T. Ngo, *On Roots of Quadratic Congruences*, Theorems 1.1 and 2.5,
   [arXiv:2107.13301](https://arxiv.org/html/2107.13301).
6. B. Kerr, I. D. Shkredov, I. E. Shparlinski, A. Zaharescu, *Energy
   bounds for modular roots and their applications*, JIMJ 24 (2025),
   Theorem 1.1 and Corollary 2.1,
   [DOI](https://doi.org/10.1017/S1474748023000397).
7. S. Baier, *Partial progress towards the large sieve for square moduli*,
   arXiv:2605.01635v3 (20 July 2026), Theorems 2 and 6, Corollary 7,
   Propositions 12, 13, and 17, and Hypothesis 18,
   [current HTML](https://arxiv.org/html/2605.01635v3).
8. N. Kingsbury-Neuschotz, *On a Restriction Problem of Hickman and
   Wright for the Parabola over \(\mathbb Z/N\mathbb Z\) for Squarefree
   \(N\)*, arXiv:2509.09885v2 (30 June 2026), Theorem 1.1,
   [current HTML](https://arxiv.org/html/2509.09885).

The source search was current to the date above.  The only workspace edit
made by this task is this assigned report.

## 7. Recommended state effect

**Recommendation: retain the target as open; promote only the scoped
source no-go and, after independent mathematical review, the exact
ambient-completion lemma.**

Specifically:

1. retain (154.SA10) and (154.SA12) as the exact proposed reduction;
2. record the selected-versus-ambient \(h\)-row distinction
   (154.SA43)--(154.SA45), so neither a false degeneracy objection nor a
   false post-selection large-sieve gain is carried forward;
3. retain the exact DFI match (154.SA53), the complete dyadic bound
   (154.SA4), and its source-legal target for the first fixed or
   polylogarithmic defect collar;
4. record the first remaining obstruction as the nonseparable full
   \(j\)-dispersion problem (154.SA71), with top-block power
   \(N^{1/2}M^{-1/4}\ge R^{3/2}\);
5. retain the stationary identity (154.SA7) only together with the actual
   support/mask conditions, reciprocal principal row, starred endpoints,
   and error ledger (154.SA68)--(154.SA69); and
6. make no change to the owner boundary \(M^{449}\asymp R^{780}\), any
   downstream obligation, or either global exponent.

The proper terminal classification is
`large_defect_root_dispersion_no_go` for all-scale use of the audited
theorem interfaces beyond that collar.
It must not be paraphrased as a theorem that quadratic-root completion or
future coefficient-sensitive dispersion is impossible.
