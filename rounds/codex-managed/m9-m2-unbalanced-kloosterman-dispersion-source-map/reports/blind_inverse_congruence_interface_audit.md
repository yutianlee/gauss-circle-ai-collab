# Blind inverse/congruence interface audit

## 1. Result

The scoped source-level no-go survives post-unmask review, but the original statement-only report required four material repairs.

Write

\[
X=N_0+\xi,\qquad N_0=\lfloor X\rfloor\in\mathbb Z_{>0},\qquad 0\leq\xi<1.
\]

Because \(k/r\asymp K/R=\Delta^{-1}\), the factor \(e(\xi k/r)\) is a uniformly smooth part of the normalized coefficient profile.  It has an exact Fourier--Mellin separation with \(O(1)\) integrated projective norm.  The source phase can therefore use the nonzero integer \(N_0\).  This makes the direct \(m=1\) dictionary, the coprime \(a=m^2\) dictionary, and both completion identities legal for every real \(X\), with no change in their norms or exponents.

The direct Bettin--Chandee bounds are

\[
F^{1/2}\left(R^{11/10}K^{-3/20}+R\right)X^\varepsilon,
\]

and Wright's dominant direct bound is

\[
R^{11/8}F^{1/4}X^\varepsilon.
\]

Every displayed term exceeds the existing absolute capacity \(\Delta X^\varepsilon\) by a fixed power throughout the frozen polytope.  The nonconstant connector

\[
m=k,\qquad a=k^2,\qquad n=r
\]

is exact on coprime rows.  Its sharp diagonal projective norm is \(O(1)\), not the extra \(K^{1/2}\) paid by an all-\(a\) detector, but its repaired Bettin--Chandee and Wright bounds still exceed \(\Delta\) by the same positive margins.

The two completion orders have different complete sums and must not be conflated.

- Smooth-weight-first completion gives a complete inverse-only sum.  Since inversion permutes reduced residues, it is exactly a Ramanujan sum.  After the full gcd decomposition, the coefficient bound
  \[
  R^{-1}\left(1+|h|/\Delta\right)^{-B}
  \]
  and the modulus-gcd sum recover exactly \(\Delta X^\varepsilon\).  This is owner-complete and equals the existing capacity.
- If one ignores that exact evaluation and instead applies a scalar source theorem to the completed primitive blocks, the original
  \[
  \Delta R^{19/20+\varepsilon}
  \]
  bound is legal after the integer-frequency repair, but it is redundant and extremely wasteful.  It is not the completion capacity.
- Inverse-selector-first completion instead gives the genuine Kloosterman sum \(S(N_0,h;n)\).  Parseval and its exact complete-frequency second moment give
  \[
  R\sqrt{\Delta}\,X^\varepsilon,
  \]
  which is worse than \(\Delta\).

The shifted physical residue remains outside Wright's dispersion interface.  Bettin--Chandee Corollary 1 admits an exact fixed-determinant map, but its main terms aggregate only to \(\Delta X^\varepsilon\), while its error is much larger.

Consequently none of the audited source interfaces improves the accepted flat-packet envelope

\[
X^\varepsilon\min\left(\Delta,\sqrt{XL/D}+\sqrt{X/(LD)}\right),
\]

whose exponent is \(\beta(u)=\min(u,(1-u)/2)>1/4\).  The smallest owner-complete quarter-scale survivor is still the entire flat smooth prescribed-centre packet.  This is a scoped method-capacity conclusion, labelled \(\mathsf{source\_level\_no\_go}\); it is not a lower bound for the literal \(\chi_4\)-weighted wave and has no endpoint or downstream scope.

## 2. Exact statement and hypotheses

Let

\[
D=X^\delta,\qquad L=X^\ell,\qquad
R=X^{1-\delta},\qquad K=X^{1+\ell-2\delta},\qquad
\Delta=\frac RK=X^{\delta-\ell},
\]

where

\[
\frac14\leq\delta<\frac12,\qquad
0\leq\ell<\delta-\frac14,\qquad
178\ell+1638\delta>463.
\]

Put

\[
u=\delta-\ell,\qquad F=\frac{XK}{R}=X^{1-u}.
\]

Then

\[
\frac14<u<\frac12,\qquad K<R,\qquad \Delta=X^u,\qquad F\to\infty.
\]

Only the flat smooth packet

\[
\mathscr R_{D,L}(X)=
\sum_{\substack{r\geq1\\r\ \mathrm{odd}}}\chi_4(r)
W\!\left(\frac{X}{rD}\right)
\sum_{k\geq1}\frac{q_L(4Xk/r^2)}{k}e(Xk/r)
\tag{2.1}
\]

and its exact prescribed-centre divisor form are in scope.  The smooth supports imply \(r\asymp R\), \(k\asymp K\), and \(0<k<r\) for sufficiently large \(X\).

The source-safe hypotheses are the following.

1. Bettin--Chandee Theorem 1 has three independent dyadic coefficient sequences, requires the inverse condition \((m,n)=1\), and places one absolute value outside the full trilinear sum.  Although its printed theorem does not type the frequency, its proof uses gcd and coprimality operations with that parameter.  The source-safe form has \(\vartheta\in\mathbb Z\setminus\{0\}\).  Remark 1 permits a smooth real phase perturbation with its stated derivative cost.
2. Wright Theorem 2.1 explicitly inherits a nonzero integral frequency and assumes
   \[
   M\ll N^2,\qquad R_0\ll M^C,\qquad (m,nR_0)=1.
   \]
   Its three coefficient sequences are independent and arbitrary, and its absolute value is outside the total trilinear sum.
3. Wright's dispersion corollaries require a fixed nonzero coprime integer residue, independent convolution coefficients, a principal reduced-residue subtraction, and a modulus sum of individual absolute discrepancies.  Their additional divisor, Siegel--Walfisz, and printed size hypotheses remain in force.
4. Bettin--Chandee Corollary 1 requires a fixed nonzero determinant, four dyadic supports, and the smooth weights and main/error terms appearing in its primary statement.
5. Uniform smoothness of the frozen flat packet is used quantitatively: after a fixed compact extension, the normalized profile has a Fourier--Mellin decomposition whose integrated product-coefficient norm is \(O(1)\).  No coefficient is frozen or deleted.

Under these hypotheses, the following is the exact repaired claim.

> For every real \(X\), the fractional-centre factor can be absorbed into the smooth coefficient profile and \(N_0\) can drive all source phases.  The direct \(m=1\) and coprime \(a=m^2\) dictionaries are legal but have bounds strictly larger than \(\Delta\).  Smooth-weight-first completion is an owner-complete Ramanujan calculation of size \(\Delta X^\varepsilon\); the scalar-source estimate \(\Delta R^{19/20+\varepsilon}\) for those completed blocks is legal but redundant.  Inverse-selector-first completion is a Kloosterman calculation of size \(R\sqrt\Delta\,X^\varepsilon\).  The physical fixed residue does not meet Wright's dispersion hypotheses, and the fixed-determinant map has aggregate main-term capacity \(\Delta X^\varepsilon\) with a much larger error.  Hence these sources prove neither the quarter estimate nor a strict improvement of the accepted flat-packet envelope.

## 3. Proof or derivation

**Integral source frequency and the complete smooth profile.**  Set \(k=Ku\), \(r=Rv\), and \(\widetilde q_L(z)=q_L(Lz)\).  On the fixed buffered support, the normalized amplitude, including the fractional centre, is

\[
G_\xi(u,v)=u^{-1}\widetilde q_L(4u/v^2)W(1/v)
e\!\left(\xi\Delta^{-1}\frac uv\right).
\tag{3.1}
\]

Every normalized derivative is bounded uniformly for \(0\leq\xi<1\), since \(\Delta^{-1}<1\).  Fourier inversion in \((\log u,\log v)\) gives

\[
G_\xi(u,v)=
\iint_{\mathbb R^2}\widehat G_\xi(t_1,t_2)
u^{it_1}v^{it_2}\,dt_1dt_2,
\qquad
\iint_{\mathbb R^2}|\widehat G_\xi(t_1,t_2)|\,dt_1dt_2\ll1.
\tag{3.2}
\]

Thus

\[
e(Xk/r)=e(N_0k/r)e(\xi k/r)
\]

has a nonzero integral source frequency and an exactly separated smooth perturbation.  Each direct fibre has norms

\[
\|\alpha\|_2=1,\qquad
\|\beta\|_2\ll R^{1/2},\qquad
\|\nu\|_2\ll K^{-1/2}.
\tag{3.3}
\]

The character \(\chi_4(r)\) stays inside \(\beta_r\) until a positive norm is taken.  This separation is valid simultaneously for Bettin--Chandee and Wright.  For the direct Bettin--Chandee map alone, Remark 1 with perturbation \(f=\xi a/n\) and scale \(Y\asymp K\) is an alternative repair.

**Direct \(m=1\) dictionary.**  Take

\[
a=k,\qquad m=1,\qquad n=r,\qquad
(A,M,N,R_0,\vartheta)=(K,1,R,1,N_0).
\tag{3.4}
\]

The phase is exact, \((1,r)=1\), and Wright's two size conditions hold.  Bettin--Chandee gives

\[
F^{1/2}\left(R^{11/10}K^{-3/20}+R\right)X^\varepsilon.
\tag{3.5}
\]

The two exponents are

\[
E_{\mathrm{BC},1}
=\frac{29}{20}+\frac{7\ell}{20}-\frac{13\delta}{10},
\qquad
E_{\mathrm{BC},2}
=\frac32+\frac\ell2-\frac{3\delta}{2}.
\tag{3.6}
\]

The first dominates, and the margins over \(u=\delta-\ell\) are

\[
E_{\mathrm{BC},1}-u
=\frac{29}{20}+\frac{27\ell}{20}-\frac{23\delta}{10}
>\frac3{10},
\tag{3.7}
\]

\[
E_{\mathrm{BC},2}-u
=\frac32+\frac{3\ell}{2}-\frac{5\delta}{2}
>\frac14.
\tag{3.8}
\]

Wright's fifth term dominates and gives

\[
R^{11/8}F^{1/4}X^\varepsilon
=X^{E_{\mathrm W,\mathrm{dir}}+\varepsilon},
\qquad
E_{\mathrm W,\mathrm{dir}}
=\frac{13}{8}+\frac\ell4-\frac{13\delta}{8},
\tag{3.9}
\]

with

\[
E_{\mathrm W,\mathrm{dir}}-u
=\frac{13}{8}+\frac{5\ell}{4}-\frac{21\delta}{8}
>\frac5{16}.
\tag{3.10}
\]

A growing fixed factor cannot repair this row: \(M=1\) forces \(R_0=O(1)\), and the owner-complete modulus family has no common growing divisor.

**Sharp nonconstant \(a=m^2\) connector.**  On \((k,r)=1\), use an auxiliary index \(j\) and take

\[
m=k,\qquad a=j^2,\qquad j=m,\qquad n=r,\qquad\vartheta=N_0.
\tag{3.11}
\]

Then

\[
N_0m^2\overline m/r\equiv N_0m/r\pmod1.
\]

The fractional factor is already part of (3.1), so this congruence is legal for every real \(X\).  The exact diagonal decomposition is

\[
\mathbf1_{j=m}=\int_0^1e(t(j-m))\,dt,
\qquad
\alpha_m(t)=m^{-1/2}e(-tm),
\qquad
\nu_{j^2}(t)=j^{-1/2}e(tj).
\tag{3.12}
\]

Both norms are \(O(1)\).  This is sharp: the matrix

\[
C_{j,m}=m^{-1}\mathbf1_{j=m}
\]

has nuclear norm

\[
\|C\|_*=\sum_{m\asymp K}\frac1m\asymp1.
\tag{3.13}
\]

Relative to the direct norm \(\|k^{-1}\|_2\asymp K^{-1/2}\), the unavoidable diagonal cost is exactly \(K^{1/2}\).  An all-\(a\) detector paying another \(K^{1/2}\) is legal but nonminimal.

With

\[
A=K^2,\qquad M=K,\qquad N=R,\qquad
\|\alpha\|_2\|\nu\|_2\|\beta\|_2\ll R^{1/2},
\]

the sharp Bettin--Chandee terms are

\[
F^{1/2}K^{21/20}R^{11/10},
\qquad
F^{1/2}K^{11/8}R.
\tag{3.14}
\]

Their exponents are

\[
E_{\mathrm{BC},\mathrm{sq},1}
=\frac{53}{20}+\frac{31\ell}{20}-\frac{37\delta}{10},
\tag{3.15}
\]

\[
E_{\mathrm{BC},\mathrm{sq},2}
=\frac{23}{8}+\frac{15\ell}{8}-\frac{17\delta}{4}.
\tag{3.16}
\]

They satisfy

\[
E_{\mathrm{BC},\mathrm{sq},1}-u>\frac3{10},
\qquad
E_{\mathrm{BC},\mathrm{sq},2}-u>\frac14.
\tag{3.17}
\]

Wright's fifth term gives

\[
F^{1/4}KR^{11/8}
=X^{\frac{21}{8}+\frac{5\ell}{4}-\frac{29\delta}{8}},
\tag{3.18}
\]

whose exponent exceeds \(u\) by more than \(5/16\).  The sharp connector is therefore algebraically valid but has no useful capacity.

**Smooth-weight-first completion: Ramanujan, not Kloosterman.**  Begin with the full gcd decomposition \(r=gn\), \(k=gj\):

\[
\mathscr R_{D,L}(X)
=\sum_{\substack{g\geq1\\g\ \mathrm{odd}}}\chi_4(g)
\sum_{\substack{n\geq1\\n\ \mathrm{odd}}}\chi_4(n)
W\!\left(\frac{X}{gnD}\right)
\sum_{\substack{j\geq1\\(j,n)=1}}
b_{g,n}(j)e(N_0j/n),
\tag{3.19}
\]

where

\[
b_{g,n}(j)=
\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n).
\tag{3.20}
\]

Here

\[
n\asymp\frac Rg,\qquad j\asymp J=\frac Kg,\qquad \frac nJ=\Delta.
\]

Define

\[
\widehat b_{g,n}(h)=
\frac1n\sum_{j\bmod n}b_{g,n}(j)e(-hj/n).
\tag{3.21}
\]

The support length \(J\), pointwise size \(K^{-1}\), and smoothness give, for every fixed \(B>2\),

\[
|\widehat b_{g,n}(h)|
\ll_B\frac1R
\left(1+\frac{\|h\|_n}{\Delta}\right)^{-B},
\qquad
\sum_{h\bmod n}|\widehat b_{g,n}(h)|\ll\frac1K.
\tag{3.22}
\]

The factor \(e(\xi j/n)\) has normalized derivative scale \(J/n=\Delta^{-1}\) and does not change these estimates.

Fourier inversion gives

\[
\begin{aligned}
\sum_{(j,n)=1}b_{g,n}(j)e(N_0j/n)
&=\sum_{h\bmod n}\widehat b_{g,n}(h)
\sum_{j\bmod n}^{*}e((N_0+h)j/n)\\
&=\sum_{h\bmod n}\widehat b_{g,n}(h)
\sum_{m\bmod n}^{*}e((N_0+h)\overline m/n)\\
&=\sum_{h\bmod n}\widehat b_{g,n}(h)
\mathfrak c_n(N_0+h).
\end{aligned}
\tag{3.23}
\]

The second equality is only the permutation \(j=\overline m\) of the reduced residues.  Hence the complete inverse-only sum is the Ramanujan sum \(\mathfrak c_n\), not a two-variable Kloosterman sum.

Since

\[
|\mathfrak c_n(q)|\leq(n,q),
\qquad
\sum_{n\asymp T}(n,q)\ll_\varepsilon TX^\varepsilon
\quad(q\neq0,\ |q|\asymp X),
\tag{3.24}
\]

and the effective \(h\)-density is \(\Delta\), one obtains

\[
\begin{aligned}
|\mathscr R_{D,L}(X)|
&\ll_\varepsilon
\sum_{g\ll K}\sum_h\frac1R
\left(1+\frac{|h|}{\Delta}\right)^{-B}
\frac Rg X^\varepsilon\\
&\ll_\varepsilon\Delta X^\varepsilon.
\end{aligned}
\tag{3.25}
\]

The \(g\)-sum is harmonic and is absorbed into \(X^\varepsilon\).  This calculation retains every gcd stratum and is owner-complete.  It exactly returns the accepted divisor capacity.

For comparison, on the primitive completed family one may keep \(h\) fixed, dyadically split \(m\asymp M\leq R\), put \(\widehat b_{1,r}(h)\) in the \(r\)-coefficient, and apply the scalar source theorem with the integer frequency \(N_0+h\).  Bettin--Chandee then gives

\[
\left(1+\frac{X}{MR}\right)^{1/2}
\left(M^{17/20}R^{1/10}+M^{7/8}\right)X^\varepsilon,
\tag{3.26}
\]

whose maximum is \(R^{19/20+\varepsilon}\); Wright gives the same maximum.  Summing the \(\Delta\) effective frequencies yields

\[
\Delta R^{19/20+\varepsilon}
=X^{19/20+\delta/20-\ell+\varepsilon}.
\tag{3.27}
\]

Because \(|h|\ll\Delta X^\varepsilon\ll N_0\), the source frequency is a nonzero integer, so (3.27) is legal.  It is nevertheless only a wasteful scalar-source bound for already completed blocks.  The exact complete sum was evaluated in (3.23), and its owner-complete capacity is (3.25), not (3.27).

**Inverse-selector-first completion: genuine Kloosterman.**  Instead define

\[
\gamma_{g,n}(m)=b_{g,n}(\overline m_n)
\]

on reduced residues whose inverse lies in the \(J\)-short support, and set it to zero elsewhere.  Its normalized Fourier transform has the exact Parseval ledger

\[
\sum_{h\bmod n}|\widehat\gamma_{g,n}(h)|^2
=\frac1n\sum_{m\bmod n}|\gamma_{g,n}(m)|^2
\ll\frac1{RK}.
\tag{3.28}
\]

Fourier inversion now gives

\[
\sum_{m\bmod n}^{*}\gamma_{g,n}(m)e(N_0\overline m/n)
=\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n),
\tag{3.29}
\]

where

\[
S(a,h;n)=\sum_{m\bmod n}^{*}e((a\overline m+hm)/n)
\]

is a genuine Kloosterman sum.  Its exact complete-frequency second moment is

\[
\sum_{h\bmod n}|S(N_0,h;n)|^2=n\varphi(n)\leq n^2.
\tag{3.30}
\]

Cauchy--Schwarz gives \(n/\sqrt{RK}\asymp\sqrt\Delta/g\) for one modulus row.  There are \(O(R/g)\) rows at fixed \(g\), so

\[
|\mathscr R_{D,L}(X)|
\ll_\varepsilon R\sqrt\Delta\,X^\varepsilon.
\tag{3.31}
\]

Its exponent is \(1-(\delta+\ell)/2\), and its margin over \(u\) is

\[
1-\frac{\delta+\ell}{2}-u
=1-\frac{3\delta}{2}+\frac\ell2>\frac14.
\tag{3.32}
\]

This completion order is strictly worse than (3.25).  The factor \(e(\xi j/n)\) is already inside \(\gamma\), changes neither its \(L^2\) mass nor the integer Kloosterman phase, and therefore makes (3.31) valid for every real \(X\).

**Physical residue and fixed determinant.**  In the divisor coordinate write \(s=N_0+t\).  Then the exact shifted form is

\[
\sum_t
\sum_{\substack{r\asymp R,\ r\ \mathrm{odd}\\
t\equiv-N_0\ (\mathrm{mod}\ r)}}
\chi_4(r)W\!\left(\frac{X}{rD}\right)
\mathcal Q_L\!\left(\frac{r(\xi-t)}{4X}\right),
\tag{3.33}
\]

effectively for \(|t-\xi|\ll\Delta X^\varepsilon\).  Thus the shifted residue is the fixed integer \(-N_0\), not a nonintegral or modulus-dependent residue.  It is, however, not uniformly coprime to \(r\); the short variable \(t\) is not a product of two independent positive dyadic sequences; its coefficient is joint in \((r,t)\); and its product scale would be \(\Delta\) while the residue size is \(N_0\asymp X\).  Wright's dispersion statements also require a principal reduced-residue subtraction and an absolute discrepancy inside the modulus sum.  Formula (3.33) has neither the required convolution nor the required absolute-value placement.  In the native \(s\)-coordinate the residue is zero.  Hence no literal Wright dispersion application is available.

For each fixed nonzero integer

\[
\tau=N_0-dr,
\]

Bettin--Chandee Corollary 1 has the exact determinant map

\[
(m_1,n_2,m_2,n_1)=(d,r,1,N_0),
\qquad
\Delta_{\mathrm{det}}=-\tau.
\tag{3.34}
\]

The scales and norms are

\[
M_1\asymp D,\qquad M_2\asymp1,\qquad
N_1\asymp X,\qquad N_2\asymp R,
\qquad
\|\alpha\|_2=1,\qquad\|\beta\|_2\ll R^{1/2}.
\]

Since \(DR=X\), the aspect ratio is \(O(1)\).  The Corollary 1 error is

\[
X^{3/5}R^{17/20}X^\varepsilon
=X^{29/20-17\delta/20+\varepsilon},
\tag{3.35}
\]

and

\[
\frac{29}{20}-\frac{17\delta}{20}>\frac{41}{40}.
\tag{3.36}
\]

The main term contributes \(O((N_0,r)/r)\) after its gcd prefactor, so

\[
\sum_{r\asymp R}\frac{(N_0,r)}r\ll_\varepsilon X^\varepsilon.
\tag{3.37}
\]

There are \(O(\Delta X^\varepsilon)\) effective nonzero determinant levels.  Their main terms aggregate to \(\Delta X^\varepsilon\), while their errors acquire another factor \(\Delta\).  The level \(\tau=0\) is a single product level and is divisor-bounded by \(X^\varepsilon\).  The fractional centre remains wholly in the smooth coefficient in (3.33), so this determinant ledger is valid for all real \(X\).

All source exponents above exceed \(u\), while (3.25) and the determinant main terms only reproduce the absolute branch.  The extra inequality \(178\ell+1638\delta>463\) creates no improving chamber.  None of these interfaces reaches the curvature branch when it is smaller, and none reaches \(X^{1/4+\varepsilon}\).

## 4. First doubtful or unproved step

The repaired no-go itself has no remaining source-hypothesis, connector, completion, determinant, or exponent gap.  The first unproved step in any positive continuation is a new estimate for the literal joint signed family

\[
\sum_{k\asymp K}\frac1k
\sum_{r\asymp R}\chi_4(r)
G(k/K,r/R)e(Xk/r),
\tag{4.1}
\]

or for its exact fixed-centre form (3.33), that keeps the \(\chi_4(r)\)-sum before positive row norms and beats

\[
X^{\beta(u)+\varepsilon},
\qquad
\beta(u)=\min(u,(1-u)/2).
\tag{4.2}
\]

The first false step in the tempting nondegenerate source reduction would be to replace

\[
\gamma_{m,r}
=\mathbf1_{\overline m_r\asymp K}
\frac{q_L(4X\overline m_r/r^2)}{\overline m_r}
e(\xi\overline m_r/r)
\tag{4.3}
\]

by a product of independent \(m\)- and \(r\)-coefficients.  The inverse-residue selector changes arithmetically with \(r\).  Smooth separation handles the ordinary normalized profile before inversion; it does not make (4.3) a product.  Completing the smooth weight first avoids that false factorization but gives only the exact Ramanujan capacity \(\Delta\).  Completing the selector first retains the joint matrix and gives the weaker Kloosterman ledger.

Thus a positive proof needs either a new vector-valued theorem accepting the literal modulus-dependent matrix, or a new exact identity exploiting the fixed \(\chi_4\) sequence before triangle inequalities.  Neither audited source supplies such a result.  This gap does not show that the literal sum is large and does not rule out a future \(\chi_4\)-sensitive argument.

## 5. Required control test and outcome

1. **Primary-source frequency control -- passed after repair.**  Bettin--Chandee is used with the source-safe nonzero integral frequency, and Wright is used with its explicit integral-frequency hypothesis.  The split \(X=N_0+\xi\) supplies that frequency for every real \(X\).
2. **Real-centre and moving-profile control -- passed.**  Equations (3.1)--(3.2) retain \(q_L\), \(W\), \(1/k\), and \(e(\xi k/r)\) in a uniformly smooth profile of \(O(1)\) projective mass.  The repair applies simultaneously to \(m=1\), \(a=m^2\), Ramanujan completion, Kloosterman completion, and the determinant ledger.
3. **Weighted-mass control -- passed.**  The literal \(1/k\) coefficient gives \(\|k^{-1}\|_2\asymp K^{-1/2}\).  No raw tuple count or unit \(k\)-coefficient is substituted.
4. **Direct-source capacity control -- failed the target.**  The margins in (3.7), (3.8), and (3.10) are uniformly positive over the full polytope.  A growing Wright factor is unavailable when \(M=1\).
5. **Sharp connector control -- passed algebraically and failed in capacity.**  The diagonal representation (3.12) has the sharp nuclear norm (3.13).  The repaired source bounds (3.14)--(3.18) still exceed \(\Delta\).
6. **Completion-order control -- passed.**  Smooth-first completion gives the Ramanujan identity (3.23) and exact owner capacity (3.25).  The legal scalar bound (3.27) is recorded only as a redundant source diagnostic.  Inverse-first completion gives the distinct Kloosterman identity (3.29) and the weaker bound (3.31).
7. **Gcd-owner control -- passed.**  Equations (3.19)--(3.25) retain every noncoprime stratum.  The harmonic \(g\)-sum is included; no coprime subpacket is promoted as an owner-complete estimate.
8. **Physical-residue and determinant controls -- passed as no-go tests.**  The physical shifted residue is exactly \(-N_0\), but Wright's coprimality, convolution, scale, coefficient, principal-term, and absolute-value interfaces fail.  The determinant dictionary is legal, its main term returns \(\Delta\), and its error is (3.35).
9. **Character and coefficient-adversary control -- passed.**  The true \(\chi_4\) remains in the modulus coefficient through every exact identity.  Each audited bound eventually uses positive norms or rowwise triangle inequalities and therefore also holds for arbitrary phases of the same magnitude.  Failure to save is a method-capacity result, not a lower bound for the true signed array.
10. **Exact-versus-near and scope control -- passed.**  Exact divisibility and determinant identities are not promoted to a near-resonance theorem.  No claim is made for clipped, starred, hard, arithmetic-owner, transition, endpoint, complete-UNBAL, M9-M2, M9, or global packets.

All tests are analytical or algebraic.  No numerical experiment is used.

## 6. Dependencies and exact artifacts used

The original statement-only derivation used:

1. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/briefs/blind_inverse_congruence_interface_audit.md.
2. problems/gauss_circle.md.
3. state/control_models.md.
4. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/blind_statement.md.

The post-unmask owner repair used:

5. protocol.md.
6. state/proof_obligations.yml.
7. state/active_campaign.yml.
8. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/briefs/blind_post_unmask_source_and_capacity_audit.md.
9. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/primary_source_manifest.md.
10. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/wright_bc_exact_source_card.md.
11. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md.
12. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/candidates/conductor_degenerate_source_capacity.md.
13. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/source_post_unmask_discovery_formula_audit.md.
14. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/discovery_post_unmask_blind_completion_audit.md.
15. rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/blind_post_unmask_source_and_capacity_audit.md.
16. This report's pre-repair text, solely to identify and replace its defective claims.

The primary source statements independently checked in the post-unmask review were:

- Bettin--Chandee, arXiv:1502.00769v1, Theorem 1, Remark 1, its proof's integrality uses, and Corollary 1.
- Wright, arXiv:2604.25177v2, the integral-frequency setup, Theorem 2.1, Corollary 2.2, and Theorem 2.3.
- The withdrawal record for arXiv:2601.00292, used only as a negative bibliographic control.

No secondary web source or numerical computation supplies a mathematical claim in this report.

## 7. Recommended state effect

**revise.**  Replace the original real-frequency, nonsharp connector, and conflated-completion claims by the repaired statements above.  Retain the terminal label

\[
\mathsf{source\_level\_no\_go}.
\]

Promote only this scoped conclusion: the audited Bettin--Chandee and Wright interfaces do not improve the accepted flat smooth packet envelope and do not prove the quarter estimate.  Keep the entire flat smooth prescribed-centre packet as the smallest unresolved owner-complete survivor.

Do not infer a lower bound for the literal signed wave, and do not change any clipped, starred, hard, transition, endpoint, complete-UNBAL, M9-M2, M9, quarter-target, or global obligation from this report alone.

