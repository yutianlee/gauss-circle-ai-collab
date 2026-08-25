# Round 150 source audit: the growing-\(M\) large-wrap collar and the bounded-variation derivative edge

- Campaign: `m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate`
- Round: 150
- Task: `variable_row_collar_source_audit`
- Role: source auditor
- Starting graph SHA-256: `b6c5ee5b0d51d347876b389c05c78596c069b190af715d297bd937701ea893b6`
- Allocation: 100% analytic, algebraic, and source verification; 0% numerical
- Proposed terminal label: `strict_moving_coefficient_collar_range`

## 1. Result: a direct-source no-go for the large wraps, and a conditional bounded-\(M\) theorem

Put

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor\asymp R^4,
 \qquad DE\asymp M\le R^2,\qquad D\le\sqrt M,
 \qquad Q=2\sqrt{ND/E}\asymp \frac{DR^2}{\sqrt M}.
\tag{150.S1}
\]

The exact two-row divisor-incidence expansion in the discovery report is
source-useful but does **not** separate the complete row.  It separates the
forced and forbidden prime incidences into

\[
 {\bf1}_{F\mid m}{\bf1}_{(m,P)=1}
 ={\bf1}_{(F,P)=1}\sum_{z\mid P}\mu(z){\bf1}_{Fz\mid m},
\tag{150.S2}
\]

with coefficient projective norm \(O_\varepsilon(X^\varepsilon)\), but leaves
the literal atom

\[
 \begin{aligned}
 &\mu^2(\eta m){\bf1}_{Fz\mid m}
 \kappa_{\eta m,U}(n_1)\kappa_{\eta m,U}(n_2)\\
 &\qquad\times
 \mathscr W_{\eta m,U}(L_1/q_1)
 \overline{\mathscr W_{\eta m,U}(L_2/q_2)}
 \end{aligned}
\tag{150.S3}
\]

joint in the odd squarefree outer row \(m\) and the two cells.  In particular,
neither the two exact floor prefixes nor the two actual sampled profiles has
become a common row vector, a four-fold tensor product, or a bounded-variation
weight merely by (150.S2).

Let the already proposed target-safe wrap packet have size

\[
 \#\mathcal K\ll 1+\frac{R^2}{Q}
 \asymp 1+\frac{\sqrt M}{D}.
\tag{150.S4}
\]

The remaining growing-\(M\) range is

\[
 \frac{R^2}{Q}\ll |k|\ll\frac NQ,
 \qquad 0<|\rho|\le \frac{hr_1r_2}{D}.
\tag{150.S5}
\]

**Source-scoped no-go.**  None of the audited primary results gives a lawful
direct estimate of the literal signed sum in (150.S5):

1. Bombieri--Iwaniec's double large sieve requires a product
   \(a(x)b(y)\).  The residual atom (150.S3) is not such a product.  Even after
   an illegal separation, the entire collar lies in a frequency interval of
   length \(O(D^{-1})\), so the theorem returns a positive local-cluster form
   and erases the retained \(\chi_4\) sign.
2. Duke--Friedlander--Iwaniec's quadratic divisor theorem accepts a fixed
   equation \(am\pm bn=s\), divisor coefficients, and a smooth weight of the
   two *products*.  The shifted-factor identity can be put into that shape,
   but the literal weight depends on the chosen factors, their congruence
   recovery, the exact prefixes, and the two sampled profiles.  Its natural
   source parameters are also far outside the theorem's nontrivial range.
3. Bettin--Chandee's Kloosterman-fraction theorems require three independent
   sequences, while their determinant corollary requires four separated
   weights, two of them smooth, and one fixed determinant.  The profile
   \(\mathscr W_{d,U}(L/(hr))\) already couples \(L\) and \(r\), and the collar
   requires all determinants or all \((k,\rho)\), not one fixed shift.
4. Reuss's additive squarefree correlation has the pure coefficient
   \(\mu^2(n)\mu^2(n+s)\) and a fixed shift with a shift-dependent implied
   constant.  The project has one squarefree outer variable with (150.S3),
   and \(kh\rho\) is a shift between products, not between two outer rows.

This is a direct-specialization and proof-placement no-go only.  It is not a
lower bound for the signed collar, not a proof that the arithmetic coefficient
is adversarial, and not an assertion that no suitable theorem exists.

There is, separately, a standard conditional bottom-scale implication.
If for every supported bounded-\(M\) triple \((d,L,U)\)

\[
 V_{d,L,U}:=
 \|q\mapsto\mathscr W_{d,U}(L/q)\|_\infty+
 \operatorname{Var}_{q\asymp LQ}
       \bigl(q\mapsto\mathscr W_{d,U}(L/q)\bigr)
 \ll_\varepsilon X^\varepsilon,
\tag{150.S6}
\]

then weighted van der Corput and exact treatment of oddness,
\((L,q)=1\), and \(\chi_4(q)\) give

\[
 \sum_{\substack{q\asymp LQ\\q\ {\rm odd},\ (q,L)=1}}
 \chi_4(q)\mathscr W_{d,U}(L/q)e(NdL/q)
 \ll_\varepsilon RX^\varepsilon
\tag{150.S7}
\]

when \(M=O(1)\).  Hence \(|G_U(d)|\ll RX^\varepsilon\) and the
bounded-\(M\) energy is \(O(R^2D X^\varepsilon)\).  The analytic implication
(150.S6) \(\Rightarrow\) (150.S7) is standard and is proved below.  What is
not proved in the discovery report is (150.S6) for the *complete literal*
Round-148 amplitude: the report names the factors and derivative scales but
does not reproduce a factor-by-factor formula, the number of hard boundaries,
or their total variation.  Thus the claimed bounded-\(M\) edge should remain
conditional until that finite profile ledger is supplied.  The exact prefix
\(\kappa_{d,U}\) is constant in \(q\) once \(d,L\) are fixed and therefore is
not itself an obstacle to (150.S7); it remains inside \(B_{d,U}(L)\).

## 2. Exact statement, hypotheses, and source cards

### 2.1 Literal large-wrap object

Write a squarefree row as \(d=\eta m\), where \(\eta\in\{1,2\}\) and
\(m\) is odd squarefree.  For \(L_i=t_is_i^2\), choose \(a_i\mid t_i\),
put \(c_i=t_i/a_i\), and let

\[
 n_i=a_iu_i(c_is_iv_i)^2,\qquad
 \beta_i=
 \frac{\mu(a_i)\mu(c_i)\mu(s_i)\mu(u_i)\mu(v_i)}
      {c_iu_iv_i^2},
\tag{150.S8}
\]

\[
 F=[a_1u_1,a_2u_2],\qquad
 P=\operatorname{rad}(c_1c_2s_1s_2v_1v_2).
\tag{150.S9}
\]

The \(v_i\) are odd squarefree and \((v_i,c_is_i)=1\).  In every cell,

\[
 q_i=hr_i,\quad (r_1,r_2)=1,\quad
 \delta=L_1r_2-L_2r_1,
\tag{150.S10}
\]

and \(k\) is the unique centered integer for which

\[
 \rho=N\delta-khr_1r_2,\qquad
 |\rho|\le \frac{hr_1r_2}{2}.
\tag{150.S11}
\]

All \(L_i,q_i,h,r_i\) are odd,
\((L_i,q_i)=1\), and \(q_i\asymp L_iQ\).  With the harmless outer
coefficient sum in (150.S8)--(150.S9) written explicitly, the unresolved
large-wrap contribution is

\[
\begin{aligned}
 \mathcal C_U^{\rm lw}={}&
 \sum_{\eta=1,2}
 \sum_{\substack{m\ {\rm odd\ squarefree}\\ \eta m\asymp D}}
 \sum_{\substack{L_i,q_i\ {\rm as\ above}\\
        R^2/Q\ll |k|\ll N/Q\\
        0<|\rho|\le hr_1r_2/D}}
 \frac{\chi_4(L_1L_2r_1r_2)}{L_1L_2}
 e\!\left(\frac{\eta m\rho}{hr_1r_2}\right)\\
 &\times
 \sum_{\mathbf a,\mathbf u,\mathbf v,z}
 \beta_1\beta_2\mu(z)
 {\bf1}_{(F,P)=1}{\bf1}_{Fz\mid m}
 \kappa_{\eta m,U}(n_1)\kappa_{\eta m,U}(n_2)\\
 &\times
 \mathscr W_{\eta m,U}(L_1/q_1)
 \overline{\mathscr W_{\eta m,U}(L_2/q_2)}.
\end{aligned}
\tag{150.S12}
\]

The source audit concerns \(|\mathcal C_U^{\rm lw}|\ll
R^2DX^\varepsilon\), not the raw tuple count and not the absolute mass
obtained by deleting the first line's character and phase.  Notice that

\[
 \chi_4(L_1q_1)\overline{\chi_4(L_2q_2)}
 =\chi_4(L_1L_2r_1r_2),
\tag{150.S13}
\]

because \(h^2\equiv1\pmod4\).  This factor is literal.  It is actually
four-fold separable, so it may be absorbed into separated source
coefficients **if** all other source hypotheses hold; no audited placement
gets to that point.

The actual sampled profile is

\[
 \mathscr W_{d,U}(L/q)=
 \mathscr A_{D,E,U}\!\left(d,\frac{4NdL^2}{q^2}\right).
\tag{150.S14}
\]

The prefix is the exact floor-existence indicator

\[
 \kappa_{d,U}(n)=
 {\bf1}_{\{\exists j\ge1:\ \mathscr A_{D,E,U}(d,nj)\ne0\}},
\tag{150.S15}
\]

or, on a component \(A_{d,U}<e\le B_{d,U}\),

\[
 {\bf1}_{\{\lfloor B_{d,U}/n\rfloor-
                 \lfloor A_{d,U}/n\rfloor\ge1\}}.
\tag{150.S16}
\]

Equations (150.S14)--(150.S16), rather than a smooth surrogate, are the
weights checked against every source below.

### 2.2 Power and shift ledger

Put \(\mathcal H=hr_1r_2\).  Uniformly on the support,

\[
\begin{aligned}
 h&\ll\min(L_1,L_2)Q,&
 r_i&\asymp L_iQ/h,\\
 \mathcal H&\asymp L_1L_2Q^2/h,&
 |\delta|&\ll L_1L_2Q/h,\\
 |k|&\ll N/Q,&
 0<|\rho|&\ll L_1L_2Q^2/(hD).
\end{aligned}
\tag{150.S17}
\]

The full centered wrap range has size

\[
 \frac NQ\asymp\frac{R^2\sqrt M}{D},
\qquad
 \frac{R^2}{Q}\asymp\frac{\sqrt M}{D};
\tag{150.S18}
\]

the ratio is \(R^2\).  The fixed-wrap absolute estimate from the discovery
report costs \(DQX^\varepsilon\).  Summed over all centered wraps it would
cost

\[
 DQ\cdot\frac NQ=DN=R^4D,
\tag{150.S19}
\]

which misses the \(R^2D\) target by \(R^2\).  Thus the large-wrap owner needs
a genuine aggregate saving and not another fixed-\(k\) estimate.

For \(k\ne0\), the exact identity is

\[
 (NL_1-khr_1)(NL_2+khr_2)=N^2L_1L_2+kh\rho.
\tag{150.S20}
\]

The two factors are positive on the collar, and

\[
 |kh\rho|\ll \frac{NL_1L_2Q}{D},\qquad
 \frac{|kh\rho|}{N^2L_1L_2}\ll\frac{Q}{DN}\ll1.
\tag{150.S21}
\]

The separate divisor bound at fixed \((L_i,h,k,\rho)\) is
\(O(X^\varepsilon)\), but summing all legal \((h,k,\rho)\) gives

\[
 \frac{NL_1L_2Q}{D}X^\varepsilon,
\tag{150.S22}
\]

whose ratio to the trivial \(L_1L_2Q^2\) denominator-pair capacity is

\[
 \frac{N}{DQ}\asymp\frac{R^2\sqrt M}{D^2}\ge R.
\tag{150.S23}
\]

These are adverse upper capacities for specified placements, never signed
lower bounds.

### 2.3 Primary source cards

**Source card A: Bombieri--Iwaniec double large sieve.**  E. Bombieri and
H. Iwaniec, [*On the order of \(\zeta(1/2+it)\)*, Lemma 2.4](https://www.numdam.org/article/ASNSP_1986_4_13_3_449_0.pdf),
Ann. Scuola Norm. Sup. Pisa **13** (1986), 449--472.  For finite sets
\(\mathcal X,\mathcal Y\subset\mathbb R^K\), separate coefficients
\(a(x),b(y)\), coordinate bounds \(|x_j|\le X_j\), \(|y_j|\le Y_j\), and

\[
 B(a,b)=\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}
 a(x)b(y)e(x\cdot y),
\]

the lemma gives

\[
 |B(a,b)|^2\le (2\pi^2)^K
 \prod_{j=1}^K(1+X_jY_j)\,B(a;Y)B(b;X),
\tag{150.S24}
\]

where \(B(a;Y)\) and \(B(b;X)\) are positive sums of
\(|a(x)a(x')|\), respectively \(|b(y)b(y')|\), over pairs closer than
\((2Y_j)^{-1}\), respectively \((2X_j)^{-1}\), in every coordinate.
There is no smoothness hypothesis, but coefficient separability and control
of both local-cluster forms are essential.  The lemma has no arithmetic
character or diagonal main term of its own; signs disappear inside the two
cluster forms.

For comparison, H. L. Montgomery and R. C. Vaughan,
[*The large sieve*, Theorem 1 and Lemma 1](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf),
Mathematika **20** (1973), 119--134, likewise use one common vector in the
primal and dual orientations.  Matrix duality does not authorize a different
coefficient vector for every outer row.

**Source card B: Duke--Friedlander--Iwaniec quadratic divisor problem.**
W. Duke, J. B. Friedlander, and H. Iwaniec,
[*A quadratic divisor problem*, Theorem 1](https://www.math.ucla.edu/~wdduke/preprints/quadraticdiv.pdf),
Invent. Math. **115** (1994), 209--217.  For \(a,b\ge1\),
\((a,b)=1\), a nonzero fixed shift \(s\), and

\[
 D_f(a,b;s)=\sum_{am\pm bn=s}\tau(m)\tau(n)f(am,bn),
\tag{150.S25}
\]

the source assumes the product-variable derivative bounds

\[
 x^iy^j f^{(i,j)}(x,y)
 \ll_{i,j}(1+x/X)^{-1}(1+y/Y)^{-1}P^{i+j}
\tag{150.S26}
\]

and gives an explicit Ramanujan-series main term plus

\[
 O_\varepsilon\!\left(
 P^{5/4}(X+Y)^{1/4}(XY)^{1/4+\varepsilon}
 \right).
\tag{150.S27}
\]

The error is uniform in the fixed shift, but the theorem does not average
many shifts.  The paper records that the result is nontrivial relative to its
main term only in the corresponding range

\[
 ab\ll P^{-5/4}(X+Y)^{-5/4}(XY)^{3/4-\varepsilon}.
\tag{150.S28}
\]

The source coefficients are exactly divisor coefficients and the weight is
smooth in the two products; factor-dependent congruence weights are not a
printed hypothesis.

**Source card C: Bettin--Chandee Kloosterman fractions and determinant
corollary.**  S. Bettin and V. Chandee,
[*Trilinear forms with Kloosterman fractions*, Theorem 1, Theorem 2,
Remark 1, and Corollary 1](https://arxiv.org/html/1502.00769v1).  Theorem 1
estimates, for \(\vartheta\ne0\), independent sequences on
\(a\asymp A,m\asymp M,n\asymp N\), \((m,n)=1\),

\[
 \sum_{a,m,n}\nu_a\alpha_m\beta_n
 e\!\left(\vartheta\frac{a\bar m}{n}\right)
\tag{150.S29}
\]

by

\[
\begin{aligned}
 \|\nu\|_2\|\alpha\|_2\|\beta\|_2
 \left(1+\frac{|\vartheta|A}{MN}\right)^{1/2}
 \bigl(& (AMN)^{7/20+\varepsilon}(M+N)^{1/4}\\
 &+(AMN)^{3/8+\varepsilon}(AN+AM)^{1/8}\bigr).
\end{aligned}
\tag{150.S30}
\]

Remark 1 permits only a \(C^1\) *phase perturbation* satisfying the printed
derivative bounds; it does not permit a joint amplitude.  Theorem 2 adds a
Jacobi symbol \((m/n)\), which is not the fixed-modulus, four-separable sign
in (150.S13).

Corollary 1 treats one fixed nonzero determinant

\[
 m_1n_2-m_2n_1=\Delta
\tag{150.S31}
\]

with four separated weights \(f(m_1)g(m_2)\alpha_{n_1}\beta_{n_2}\).
The first two are smooth with
\(f^{(j)}\ll\eta^jM_1^{-j}\),
\(g^{(j)}\ll\eta^jM_2^{-j}\).  Besides an explicit density main term,
its error is

\[
 O\!\left((\eta\mathcal R)^{3/2}
 \|\alpha\|_2\|\beta\|_2
 (N_1N_2)^{7/20}(N_1+N_2)^{1/4+\varepsilon}
 (M_1M_2)^\varepsilon\right),
\tag{150.S32}
\]

where

\[
 \mathcal R=\frac{M_1N_2}{M_2N_1}+
             \frac{M_2N_1}{M_1N_2}.
\]

The theorem does not print an average of (150.S32) over all \(\Delta\).

**Source card D: additive squarefree correlation.**  T. Reuss,
[*Pairs of \(k\)-free Numbers, consecutive square-full Numbers*,
Theorem 2](https://arxiv.org/abs/1212.3150v2), proves for fixed
\(k\ge2\) and fixed \(s\ne0\)

\[
 \sum_{n\le x}\mu_k(n)\mu_k(n+s)
 =c_{k,s}x+O_{\varepsilon,k,s}(x^{\omega(k)+\varepsilon}),
\tag{150.S33}
\]

where \(\mu_k\) is the indicator of \(k\)-free integers,

\[
 c_{k,s}=\prod_p\left(1-\frac{\rho_{k,s}(p)}{p^k}\right),
 \quad
 \rho_{k,s}(p)=
 \begin{cases}2,&p^k\nmid s,\\1,&p^k\mid s,\end{cases}
\]

and

\[
 \omega(2)=\frac{26+\sqrt{433}}{81}\approx0.578,
 \qquad \omega(k)=\frac{169}{144k}\quad(k\ge3).
\tag{150.S34}
\]

The coefficient is the pure product of two \(k\)-free indicators; the
implied constant is allowed to depend on the fixed shift.  There is no
cell-dependent multiplier, reciprocal phase, modulus average, or growing
shift average in the theorem.

**Source card E: van der Corput's second-derivative test.**  O. Robert,
[*On van der Corput's \(k\)-th derivative test for exponential sums*,
Theorem 1](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf),
Indag. Math. **27** (2016), 559--589, records the classical statement: if
\(f\in C^2(I)\) on an interval of integer length \(Y\) and

\[
 0<\lambda\le |f''(x)|\le A\lambda\qquad(x\in I),
\tag{150.S35}
\]

then, uniformly on every subinterval,

\[
 \left|\sum_{n\in I\cap\mathbb Z}e(f(n))\right|
 \le C(A)\bigl(Y\lambda^{1/2}+\lambda^{-1/2}\bigr).
\tag{150.S36}
\]

The theorem is unweighted.  The bounded-variation weighted form used below
is an immediate Abel-summation consequence, not an additional imported
regularity theorem.

## 3. Proof and source-hypothesis derivation

### 3.1 The incidence expansion stops before source separability

For fixed \((L_1,L_2)\), (150.S2) is exact: if \((F,P)>1\), no
squarefree \(m\) can contain every prime forced by \(F\) while excluding
every prime in \(P\); if \((F,P)=1\), Möbius inversion of
\({\bf1}_{(m,P)=1}\) gives (150.S2).  The sums of
\(|\beta_1\beta_2\mu(z)|\) are \(O(X^\varepsilon)\) because the
\(u_i^{-1}\) sums are logarithmic, the \(v_i^{-2}\tau(v_i)^C\) sums
converge, and the \(a_i,c_i\) divisor sums are \(X^{o(1)}\).

This exact algebra does not alter (150.S14)--(150.S16).  After the incidence
parameters are fixed, \(n_i\) still changes with the cell, so
\(m\mapsto\kappa_{\eta m,U}(n_i)\) is not a common row coefficient as
the cell changes.  Likewise
\(\mathscr W_{\eta m,U}(L_i/(hr_i))\) changes jointly with the row and
cell.  This is the first literal rank seam.  Calling only the arithmetic
incidence layer "low projective norm" is lawful; calling the full atom
finite rank is not yet justified.

### 3.2 Double-large-sieve placement

Write the collar phase as

\[
 e(m\theta_\gamma),\qquad
 \theta_\gamma=\frac{\eta\rho}{hr_1r_2},\qquad
 |\theta_\gamma|\le \frac{2}{D},
\tag{150.S37}
\]

where \(\gamma\) denotes all cell and incidence variables.  A direct use of
(150.S24) with \(K=1\), \(x=m\), and \(y=\theta_\gamma\) first requires
the coefficient to be \(a(m)b(\gamma)\).  Equation (150.S3) fails this
hypothesis.

Even if (150.S3) is illegally replaced by a product, the natural boxes are
\(X_1\asymp D\), \(Y_1\asymp D^{-1}\), so
\(1+X_1Y_1\asymp1\).  The row cluster form includes pairs
\(|m-m'|\ll D\), and the frequency cluster form includes pairs
\(|\theta_\gamma-\theta_{\gamma'}|\ll D^{-1}\).  The whole collar is
covered by only \(O(1)\) intervals of this latter length.  Thus the source
right side contains essentially the unresolved local positive correlation;
it supplies no automatic version of the factor-\(R^2\) aggregate saving
identified in (150.S19).  Since the cluster form uses absolute products, it
also cannot exploit (150.S13).  Adding formal extra coordinates is not a
legal use of the lemma unless the phase and constraints have first been
linearized in those coordinates.

### 3.3 Shifted-factor identity versus the quadratic divisor theorem

Set

\[
 A=NL_1-khr_1,\qquad B=NL_2+khr_2.
\tag{150.S38}
\]

Then (150.S20) is equivalently

\[
 AB-N^2(L_1L_2)=kh\rho.
\tag{150.S39}
\]

The natural DFI dictionary is therefore

\[
 a=1,\quad b=N^2,\quad m'=AB,\quad n'=L_1L_2,\quad s=kh\rho.
\tag{150.S40}
\]

It respects integrality, \((a,b)=1\), and the nonzero-shift hypothesis.
It does not respect the coefficient.  DFI weights \(m'\) and \(n'\) by
\(\tau(m')\tau(n')\) and a smooth function of \((m',N^2n')\).  The project
instead distinguishes a factorization \(m'=AB\) by

\[
 r_1=\frac{NL_1-A}{kh},\qquad
 r_2=\frac{B-NL_2}{kh},
\tag{150.S41}
\]

then tests divisibility by \(kh\), support, oddness, exact gcd, reducedness,
\((r_1,r_2)=1\), the character \(\chi_4(r_1r_2)\), both sampled profiles,
and (150.S3).  Different factorizations of the same \((m',n')\) carry
different weights.  That is not (150.S25)--(150.S26).  The shifts
\(kh\rho\) also vary over the whole ledger (150.S17); applying the source
error separately would require paying every shift.

There is a decisive formal power mismatch after the earlier coefficient and
smoothness mismatches.  On support,

\[
 X_{\rm DFI}\asymp Y_{\rm DFI}\asymp
 Z:=N^2L_1L_2.
\tag{150.S42}
\]

The error (150.S27) is

\[
 \asymp P^{5/4}Z^{3/4+\varepsilon}
 =P^{5/4}N^{3/2}(L_1L_2)^{3/4+\varepsilon}.
\tag{150.S43}
\]

The nontriviality condition (150.S28) would require

\[
 N^2\ll P^{-5/4}Z^{1/4-\varepsilon}.
\tag{150.S44}
\]

Since \(L_i\le E\le R^2=N^{1/2}\), the right side is at most
\(P^{-5/4}N^{3/4+o(1)}\); (150.S44) fails by a fixed power of \(N\).
Already at \(L_1=L_2=1\), the formal source error is
\(N^{3/2+o(1)}=R^{6+o(1)}\), before any shift sum, whereas the global
collar target is at most \(R^3X^\varepsilon\) because \(D\le R\).
This comparison is a failed direct specialization, not a bound for the
literal signed subfamily.

### 3.4 Bettin--Chandee determinant and inverse-fraction interfaces

The original determinant \(\delta=L_1r_2-L_2r_1\) has exactly the form
(150.S31) with

\[
 (m_1,m_2,n_1,n_2)=(L_1,L_2,r_1,r_2),\qquad \Delta=\delta.
\tag{150.S45}
\]

But for fixed \(d,h\) each row-cell weight is

\[
 \frac{\chi_4(Lr)}{L}B_{d,U}(L)
 \mathscr W_{d,U}(L/(hr)),
\tag{150.S46}
\]

which couples \(L\) and \(r\).  The arithmetic factor \(B_{d,U}(L)\)
is not one of the two smooth source weights, and (150.S14) is not separated
into an \(L\)-weight and an \(r\)-weight.  Interchanging the two sides of the
determinant does not remove this within-cell coupling.  Moreover the collar
does not fix one \(\delta\): it relates every \(\delta\) to a centered \(k\)
and a nonzero \(\rho\).  Corollary 1 has an explicit main term for each
determinant and no printed aggregate estimate over these determinants.

For a unit-coefficient scale diagnostic, on a balanced block
\(r_i\asymp S=LQ/h\), the error (150.S32) alone has size

\[
 \|\alpha\|_2\|\beta\|_2
 (S^2)^{7/20}S^{1/4+\varepsilon}
 \asymp S^{39/20+\varepsilon}
\tag{150.S47}
\]

per determinant.  There is no lawful project coefficient norm to attach to
(150.S47), and separately summing it over
\(|\delta|\ll L_1L_2Q/h\) is not target-sized.  It is therefore only a
source-capacity diagnostic.

Theorem 1's inverse fraction is also not the real reciprocal phase in
(150.S12).  One may formally choose a residue \(m\) satisfying
\(mL\equiv1\pmod q\), so that \(\bar m\equiv L\pmod q\), but then \(m\)
is selected jointly by \((L,q)\), and (150.S46) becomes a graph-supported
amplitude rather than \(\nu_a\alpha_m\beta_n\).  Theorem 2's Jacobi symbol
does not repair this: the literal \(\chi_4\) is already the separate sign
(150.S13), while all residual coupling remains.

### 3.5 Additive squarefree correlation

After (150.S2), the outer variable has the coefficient

\[
 \mu^2(\eta m){\bf1}_{Fz\mid m}
 \kappa_{\eta m,U}(n_1)\kappa_{\eta m,U}(n_2)
 \mathscr W_{\eta m,U}(L_1/q_1)
 \overline{\mathscr W_{\eta m,U}(L_2/q_2)}.
\tag{150.S48}
\]

There is no second outer variable \(m+s\) with a pure squarefree indicator.
The quantity \(kh\rho\) in (150.S39) shifts two products and is unrelated to
the shift in (150.S33).  Even a formal application of (150.S33) would return
a nonzero density main term, a fixed-shift error with a shift-dependent
constant, and no \(\chi_4\)-weighted aggregate over the growing family
\((h,k,\rho)\).  Thus Reuss's theorem neither accepts the coefficient nor
averages the needed shifts.  This mismatch occurs before its exponent can be
used.

### 3.6 Weighted van der Corput with bounded-variation weights

Here is the promised theorem card and derivation.

**Lemma 150.S (weighted second derivative).**  Let \(I=[A,B]\),
\(Y=B-A\ge1\), let \(f\in C^2(I)\) satisfy (150.S35), and let
\((w_n)_{n\in I\cap\mathbb Z}\) be complex weights.  Define the discrete
variation

\[
 \operatorname{Var}_{\mathbb Z}(w;I)
 =\sum_{n,n+1\in I}|w_{n+1}-w_n|.
\]

Then

\[
 \left|\sum_{n\in I\cap\mathbb Z}w_ne(f(n))\right|
 \ll_A
 \bigl(\|w\|_\infty+\operatorname{Var}_{\mathbb Z}(w;I)\bigr)
 \bigl(Y\lambda^{1/2}+\lambda^{-1/2}\bigr).
\tag{150.S49}
\]

To prove it, let \(S(t)=\sum_{A<n\le t}e(f(n))\).  Theorem 1 in source
card E, applied to every initial subinterval, gives

\[
 \sup_t|S(t)|\ll_A Y\lambda^{1/2}+\lambda^{-1/2}.
\]

Discrete Abel summation gives

\[
 \sum_{n=A}^{B}w_ne(f(n))
 =w_BS(B)+\sum_{n=A}^{B-1}(w_n-w_{n+1})S(n),
\]

which is (150.S49).  If \(w\) is the sampling of a complex
bounded-variation function, its discrete variation is at most the continuous
variation.  Hard jumps are therefore allowed and are paid exactly once.

Apply the lemma to

\[
 f(q)=\frac{NdL}{q},\qquad q\asymp LQ.
\tag{150.S50}
\]

Then

\[
 |f''(q)|=\frac{2NdL}{q^3}\asymp
 \lambda:=\frac{Nd}{L^2Q^3},\qquad Y\asymp LQ,
\tag{150.S51}
\]

so (150.S49) gives

\[
 \ll V_{d,L,U}\left(\sqrt{\frac{Nd}{Q}}+
             \frac{LQ^{3/2}}{\sqrt{Nd}}\right).
\tag{150.S52}
\]

The literal arithmetic restrictions cost only \(X^\varepsilon\): split
\(q\) into the two odd residue classes modulo four, on which \(\chi_4(q)\)
is constant, and expand

\[
 {\bf1}_{(q,L)=1}=\sum_{s\mid(q,L)}\mu(s).
\tag{150.S53}
\]

For a fixed odd \(s\mid L\), put \(q=sn\), then split \(n\) modulo four.
The interval length is divided by \(s\), while the second derivative in
\(n\) is multiplied by \(s^2\); hence the first term in (150.S52) is
unchanged and the second only decreases.  The number of divisors is
\(\tau(L)\ll X^\varepsilon\).  The factor \(\chi_4(s)\) has modulus one.
Thus (150.S52) proves the reduced, odd, literal-character version.

Using \(d\asymp D\), (150.S1), and \(L\le E=M/D\), the two terms satisfy

\[
 \sqrt{\frac{Nd}{Q}}\asymp RM^{1/4},
 \qquad
 \frac{LQ^{3/2}}{\sqrt{Nd}}
 \ll \frac{RLD}{M^{3/4}}\le RM^{1/4}.
\tag{150.S54}
\]

This explains both sides of the method boundary.  If \(M=O(1)\), then
\(D,E,d,L=O(1)\), \(Q\asymp R^2\), and (150.S6) gives (150.S7).  The
accepted \(\sum_L|B_{d,U}(L)|/L\ll X^\varepsilon\) then yields

\[
 |G_U(d)|\ll RX^\varepsilon,
 \qquad
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll R^2DX^\varepsilon.
\tag{150.S55}
\]

For growing \(M\), the same standard theorem has the first term
\(RM^{1/4}\).  It does not prove an all-scale \(O(R)\) row bound, even if
(150.S6) were known.  This is an upper-capacity failure of this derivative
placement, not a lower bound for the actual character sum.

Finally, (150.S14) alone does not prove (150.S6).  A complete proof must
write \(\mathscr A_{D,E,U}\) as its actual finite product/sum, show that
every smooth factor composed with \(q\mapsto4NdL^2/q^2\) has total
variation \(O(X^\varepsilon)\), count every half-open product-prefix, cone,
dyadic, radial, and peeled-collar jump, and show that the number and total
jump mass of all pieces is \(O(X^\varepsilon)\), uniformly in \(U\).  The
discovery report asserts these facts for bounded \(M\) but does not display
this ledger.  The external theorem cannot supply it.

## 4. First doubtful or unproved step

For the growing-\(M\) large-wrap collar, the first unproved step after the
valid incidence expansion is a signed aggregate estimate for (150.S12) over

\[
 R^2/Q\ll|k|\ll N/Q,\qquad
 0<|\rho|\le hr_1r_2/D,
\]

with the residual atom (150.S3) and the exact sign (150.S13).  The fixed-wrap
bound leaves the factor-\(R^2\) gap (150.S19); the fixed-shift divisor route
has the adverse capacity (150.S22)--(150.S23); and the audited double-sieve,
shifted-divisor, determinant, inverse-fraction, and squarefree-correlation
theorems fail a coefficient, separability, smoothness, shift-average, main-
term, or power hypothesis before they can close that gap.

At the bounded-\(M\) edge, the standard analytic step is not doubtful:
(150.S49)--(150.S55) prove the claimed conclusion under (150.S6).  The first
unproved internal step is precisely (150.S6) for the complete actual sampled
profile.  Boundedness of \(\mathscr W\) is insufficient.  A finite
factor-by-factor total-variation proof would close this small edge; failure
to have it in the present report is not evidence that such a proof is
impossible.

The endpoint makes the growing-scale scope unavoidable.  At \(D=1\), the
centered collar is the entire nonexact family.  At \(L=1\), there is no row
average and the literal sum is

\[
 B_{1,U}(1)
 \sum_{q\asymp Q\atop q\ {\rm odd}}
 \chi_4(q)\mathscr W_{1,U}(1/q)e(N/q),
\tag{150.S56}
\]

apart from the already owned exact phase classes.  The weighted derivative
bound is

\[
 \ll V_{1,1,U}\bigl(RM^{1/4}+RM^{-3/4}\bigr).
\tag{150.S57}
\]

It is \(O(RX^\varepsilon)\) at bounded \(M\) if (150.S6) holds, but it is
not target-sized by this method for growing \(M\).  None of the audited
sources may manufacture a nonexistent \(d\)-average in (150.S56).

## 5. Control tests and outcomes

1. **`literal_nonzero_collar_expansion` -- pass as an audit.**  Equation
   (150.S12) retains both \(B\)-expansions, both prefixes, both profiles,
   squarefreeness, parity, reducedness, common gcd \(h\), centered \(k\),
   nonzero \(\rho\), and the exact phase.

2. **`two_row_divisor_incidence_linearization` -- pass with a strict
   stopping point.**  Equations (150.S2), (150.S8), and (150.S9) give the
   exact forced/excluded-prime incidence and its \(X^\varepsilon\)
   coefficient norm.  The full residual atom (150.S3) is not declared
   finite rank.

3. **`prefix_profile_d_dependence` -- pass/open split.**  Equations
   (150.S14)--(150.S16) retain the literal floor prefix and sampled profile.
   No growing-\(M\) variation is assumed.  The bounded-\(M\) variation claim
   (150.S6) remains to be proved from the full amplitude formula.

4. **`shifted_factor_identity` -- pass.**  Equations
   (150.S20)--(150.S21) retain signs, integrality, positivity, and the short
   relative shift.  The DFI map (150.S40) is exact algebraically and fails
   only at the subsequent source hypotheses and powers.

5. **`k_zero_and_exceptional_factor` -- pass by scope.**  This report audits
   only the large-wrap range, so \(k\ne0\).  The discovery report's positivity
   and exceptional-factor exclusion are retained; no denominator dividing
   \(N\) is deleted.

6. **`full_shift_and_weight_summation` -- fail for the target, pass as a
   no-go ledger.**  Equations (150.S17)--(150.S23) sum the fixed-shift
   divisor capacity over all \((h,k,\rho)\) and show why it is not a collar
   proof.  No audited source supplies the missing aggregate saving.

7. **`tuple_absolute_signed_separation` -- pass.**  Equations
   (150.S19), (150.S22), and (150.S23) are positive capacities.  Equation
   (150.S12) is the signed target.  No capacity is called a signed lower
   bound.

8. **`mod_four_character_retention` -- pass.**  Equation (150.S13) is kept
   in every literal formula.  Double-large-sieve cluster norms would erase
   it; weighted van der Corput instead treats the two odd residue classes
   exactly.

9. **`source_theorem_collar_match` -- no direct match.**  Source cards A--D
   fail respectively at joint coefficients/local clustering, factor-level
   weights and power, four-fold separation/fixed determinant, and the pure
   two-squarefree fixed-shift coefficient.  This is not an exhaustive
   literature impossibility statement.

10. **`all_M_D_E_Q_L_h_k_rho_power_ledger` -- pass.**  Equations
    (150.S17)--(150.S23), (150.S42)--(150.S44), and
    (150.S51)--(150.S54) retain every requested scale.  The full wrap range
    is \(R^2\) times the proposed packet, and the derivative placement has
    the exact \(RM^{1/4}\) growing-scale term.

11. **`D1_L1_full_frequency_test` -- pass/open split.**  Equations
    (150.S56)--(150.S57) retain the literal one-row reciprocal character sum.
    Its bounded-\(M\) conclusion is conditional on (150.S6); its growing-
    \(M\) large wraps remain open.

12. **`prime_parity_prefix_imprimitive_controls` -- pass.**  The split
    \(d=\eta m\) retains even squarefree rows; \(F,P,z\) retain primes forced
    into or excluded from the odd part; \(h,r_i\) retain common factors and
    imprimitive denominators; no exact prefix is smoothed in a source map.

13. **`exact_and_small_denominator_exclusion` -- pass by ownership.**  The
    audited sum has \(\rho\ne0\) and lies outside the proposed small-wrap
    packet.  Exact phases, \(q_i\mid N\), and small reduced denominators stay
    with their accepted owners and are not reclassified.

14. **`generic_tge2_cross_and_downstream_scope` -- pass.**  Nothing here
    estimates the growing-\(M\) generic complement, a \(t\ge2\) layer, the
    Round-138 cross owner, lower GAR, M9--M1, M9--M2, endpoint uniformity,
    M9, the bridge, the quarter target, or either exponent statement.

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Repository artifacts used:

- `protocol.md`;
- `state/proof_obligations.yml`, limited to the three active obligation
  records named in the campaign;
- `state/active_campaign.yml`;
- `strategy/round150_moving_coefficient_near_collision_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/briefs/variable_row_collar_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reports/moving_coefficient_two_row_expansion_attack.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/reports/rational_energy_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/reviews/discovery_source_conductor_round149_review.md`.

Primary technical sources checked:

- Bombieri and Iwaniec,
  [*On the order of \(\zeta(1/2+it)\)*](https://www.numdam.org/article/ASNSP_1986_4_13_3_449_0.pdf),
  Lemma 2.4;
- Montgomery and Vaughan,
  [*The large sieve*](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf),
  Theorem 1 and Lemma 1;
- Duke, Friedlander, and Iwaniec,
  [*A quadratic divisor problem*](https://www.math.ucla.edu/~wdduke/preprints/quadraticdiv.pdf),
  Theorem 1;
- Bettin and Chandee,
  [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/html/1502.00769v1),
  Theorems 1--2, Remark 1, and Corollary 1;
- Reuss,
  [*Pairs of \(k\)-free Numbers, consecutive square-full Numbers*](https://arxiv.org/abs/1212.3150v2),
  Theorem 2;
- Robert,
  [*On van der Corput's \(k\)-th derivative test for exponential sums*](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf),
  Theorem 1.

No secondary source is used for a technical theorem statement.  No shared
proof state, validation matrix, synthesis, or proof draft was edited.

## 7. Recommended state effect

**Retain and revise under `strict_moving_coefficient_collar_range`.**

1. Retain the discovery report's exact two-row incidence formula and its
   strict fixed-wrap packet as candidate mathematics subject to the other
   Round-150 seams.  This source audit finds no external-source defect in the
   algebraic incidence stopping point.
2. Record only a **source-scoped** large-wrap obstruction: the audited
   double-large-sieve, shifted-divisor, Kloosterman-fraction/determinant, and
   additive-squarefree theorems do not directly prove (150.S12), for the
   exact mismatches and powers above.  Do not turn this into
   `moving_coefficient_collar_no_go` as an impossibility statement.
3. Do not promote the full moving-coefficient collar target.  The growing-
   \(M\) range (150.S5), with literal \(\chi_4\), divisor incidence, prefixes,
   and sampled profiles, remains the first open owner seam.
4. Treat the bounded-\(M\) full-row claim as **conditional on the explicit
   profile variation lemma** (150.S6).  The weighted van der Corput theorem
   and its \(O(RX^\varepsilon)\) translation are complete; the actual
   factor-by-factor BV ledger is not present in the audited report.
5. Make no change to the generic growing-scale complement, any \(t\ge2\)
   layer, the Round-138 cross owner, lower GAR, M9--M1, M9--M2, endpoint
   uniformity, M9, the bridge, the quarter target, or either exponent.
