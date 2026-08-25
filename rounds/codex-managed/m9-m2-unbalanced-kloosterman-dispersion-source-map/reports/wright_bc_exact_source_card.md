# Round 135 source audit: Bettin--Chandee and Wright

Campaign: m9-m2-unbalanced-kloosterman-dispersion-source-map  
Task: wright_bc_exact_source_card  
Role: source auditor, owner-repaired after post-unmask review  
Starting graph SHA-256: f9aa6fa43900b9cb73f705405f9a6090e6e84fb5d3c8a9e037ffe3c6911b9ea0

## 1. Result

The audited sources do not prove the Round-135 flat prescribed-centre wave
estimate.  The terminal classification remains
\(\mathtt{source\_level\_no\_go}\), but the post-unmask review materially
strengthens the exact dictionaries.

Write

\[
 X=N_0+\xi,\qquad N_0=\lfloor X\rfloor\in\mathbb Z_{>0},
 \qquad 0\leq\xi<1.
\tag{1.1}
\]

On a frozen flat smooth cell, \(e(\xi k/r)\) is part of a uniformly smooth
normalized amplitude because \(k/r=(K/R)u/v=\Delta^{-1}u/v\).  Buffered
Fourier--Mellin separation gives an exact superposition of independent
\(k\)- and \(r\)-coefficients with \(O(1)\) integrated projective mass.
Consequently every source phase below may use the integral frequency
\(N_0\), while the fractional factor remains in the arbitrary separated
coefficients.

This yields four source-level corrections.

1. The direct \(m=1\) specialization is legal for every real \(X\) for both
   Bettin--Chandee and Wright.  Bettin--Chandee Remark 1 gives an alternative
   direct repair, but Wright needs no perturbation theorem after coefficient
   absorption.
2. The coprime \(a=m^2\) connector is likewise legal for every real \(X\);
   its sharp diagonal projective norm is \(\asymp1\), not the extra
   \(K^{1/2}\) paid by the conductor's all-\(a\) detector.
3. Smooth-weight-first completion gives Ramanujan sums (or an ordinary
   additive delta without the coprimality restriction) and returns the
   existing \(\Delta X^\varepsilon\) capacity.  Inverse-selector-first
   completion gives genuine Kloosterman sums and the much worse positive
   cost \(R\sqrt{\Delta}\,X^\varepsilon\).
4. The shifted physical residue is the fixed integer \(-N_0\), not a
   nonintegral or intrinsically modulus-dependent residue.  It still fails
   Wright's convolution, coprimality, range, coefficient, principal-term,
   and absolute-value interfaces.

The literal direct coefficient norms are

\[
 \|\alpha\|_2\asymp1,\qquad
 \|\beta\|_2\asymp R^{1/2},\qquad
 \|\nu\|_2\asymp K^{-1/2}.
\tag{1.2}
\]

With these norms, direct Bettin--Chandee gives exponents

\[
 E_{\rm BC,1}=\frac{29}{20}+\frac{7\ell}{20}
                 -\frac{13\delta}{10},\qquad
 E_{\rm BC,2}=\frac32+\frac\ell2-\frac{3\delta}{2},
\tag{1.3}
\]

and direct Wright gives the dominant exponent

\[
 E_{\rm W,dir}=\frac{13}{8}+\frac\ell4-\frac{13\delta}{8}.
\tag{1.4}
\]

They exceed the known absolute exponent
\(u=\delta-\ell\) by more than \(3/10\), \(1/4\), and \(5/16\),
respectively.  The square connector and Bettin--Chandee Corollary 1 are also
legal but non-saving.  Corollary 1 has per-nonzero-determinant error

\[
 X^{3/5+\varepsilon}R^{17/20},
\tag{1.5}
\]

while its main terms aggregate only to
\(\Delta X^\varepsilon\).  Thus none of these sources improves the accepted
flat envelope, much less proves \(X^{1/4+\varepsilon}\).  This is a scoped
method obstruction, not a lower bound for the literal \(\chi_4\)-signed
wave.

## 2. Exact statement and hypotheses

### Bettin--Chandee, arXiv:1502.00769v1, Theorem 1 and Remark 1

The audited version is Sandro Bettin and Vorrapan Chandee,
*Trilinear forms with Kloosterman fractions*, arXiv:1502.00769v1,
submitted 3 February 2015.  Put

\[
 \mathcal M=[M/2,M],\qquad
 \mathcal N=[N/2,N],\qquad
 \mathcal A=[A/2,A].
\]

For arbitrary complex sequences supported on the integer points of these
intervals, define

\[
 \mathcal B(M,N,A)=
 \sum_{\substack{a\in\mathcal A,\ m\in\mathcal M,\ n\in\mathcal N\\
                  (m,n)=1}}
 \alpha_m\beta_n\nu_a
 e\!\left(\vartheta\frac{a\overline m}{n}\right).
\]

Theorem 1 states

\[
\begin{aligned}
 |\mathcal B(M,N,A)|
 &\ll
 \|\alpha\|_2\|\beta\|_2\|\nu\|_2
 \left(1+\frac{|\vartheta|A}{MN}\right)^{1/2}\\
 &\quad\times
 \left(
 (AMN)^{7/20+\varepsilon}(M+N)^{1/4}
 +(AMN)^{3/8+\varepsilon}(AN+AM)^{1/8}
 \right).
\end{aligned}
\tag{BC1}
\]

There is no printed balance or lower-size condition on \(A,M,N\).
The coefficients are arbitrary; the theorem uses their three
\(\ell^2\)-norms and places one absolute value outside the complete signed
trilinear sum.  No coefficient smoothness, pointwise bound, or
equidistribution hypothesis is assumed.

The printed statement says only \(\vartheta\ne0\), without typing it.  The
proof uses \((n,\vartheta)\), \((\vartheta,b)\), and primes coprime to
\(\vartheta b\).  The source-verified theorem therefore has
\(\vartheta\in\mathbb Z\setminus\{0\}\).  Wright v2 independently describes
the Bettin--Chandee frequency as a nonzero integer.  A real-frequency reading
of the bare theorem is not source-justified.

Remark 1 permits an additional real \(C^1\) phase.  In the source's
\(x,y\) notation, on the two dyadic supports it assumes

\[
 |\partial_x f_{a,\vartheta}(x,y)|
 \ll\frac{Y}{x^2y},\qquad
 |\partial_y f_{a,\vartheta}(x,y)|
 \ll\frac{Y}{xy^2},
\tag{BC-R}
\]

for some \(Y>1\).  The bound (BC1) remains valid with

\[
 \left(1+\frac{|\vartheta|A}{MN}\right)^{1/2}
 \quad\text{replaced by}\quad
 \left(1+\frac{|\vartheta|A+Y}{MN}\right)^{1/2}.
\]

The source switches \(\vartheta\) to \(\theta\) once and orders the
arguments of \(f\) inconsistently with its support labels.  These are
notation defects.  Interpreting \(x\asymp N,y\asymp M\), or swapping both
labels consistently, gives the same derivative audit below.

Bettin--Chandee Theorem 2 inserts
\(\left(\frac mn\right)\) and assumes
\((m,n)=(2,mn)=1\).  At \(m=1\) its Jacobi symbol is \(1\), so it cannot
manufacture \(\chi_4(n)\); the actual character can only remain in the
arbitrary sequence \(\beta_n\).  Its bound is not stronger for the present
degenerate row.

### Wright, arXiv:2604.25177v2, Theorem 2.1

The audited version is Thomas Wright,
*Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced
convolutions*, arXiv:2604.25177v2, revised 7 August 2026.  To avoid a
collision between project and source variables, write \(A_0,M_0,N_0'\) for
the three source lengths and \(R_0\) for the fixed denominator factor.
Wright defines

\[
 \mathcal B(M_0,N_0',A_0;R_0)=
 \sum_{\substack{a\sim A_0,\ m\sim M_0,\ n\sim N_0'\\
                  (m,nR_0)=1}}
 \alpha_m\beta_n\nu_a
 e\!\left(\vartheta\frac{a\overline m}{nR_0}\right),
\tag{W0}
\]

where \(\vartheta\in\mathbb Z\setminus\{0\}\).  The paper temporarily prints
\(\theta\) in the definition but returns to \(\vartheta\) in the bound.  It
inherits arbitrary complex coefficients and \(\ell^2\)-norms from the
preceding Bettin--Chandee setup.

If

\[
 M_0\ll (N_0')^2,\qquad R_0\ll M_0^C
\tag{W-range}
\]

for a fixed large polynomial-growth exponent \(C\), Theorem 2.1 prints

\[
\begin{aligned}
 |\mathcal B(M_0,N_0',A_0;R_0)|
 &\ll M_0^\varepsilon
 \|\alpha\|_2\|\beta\|_2\|\nu\|_2
 (A_0M_0N_0')^{1/2}R_0^{1/4}
 \left(1+\frac{|\vartheta|A_0}{M_0N_0'}\right)^{1/4}\\
 &\quad\times\left(
 (N_0')^{-1/8}
 +\frac{R_0^{1/8}(N_0')^{1/8}}{M_0^{1/4}}
 +\frac{M_0^{1/10}}
 {R_0^{3/20}A_0^{1/20}(N_0')^{3/20}}
 +\frac{(N_0')^{3/20}}{A_0^{3/20}M_0^{1/5}}
 +\frac{(N_0')^{3/8}}{M_0^{1/2}}
 \right).
\end{aligned}
\tag{W1}
\]

The source writes \(R\ll M^A\), reusing \(A\); (W-range) records the
intended polynomial-growth condition without that collision.  The printed
third bracket term has \(A_0^{-1/20}\), while the final line of the proof has
the stronger \(A_0^{-3/10}\).  This report uses the weaker printed theorem.
The fifth term, decisive in every specialization below, agrees in the
statement and proof, so the discrepancy changes no conclusion.

The theorem has one absolute value around the whole signed trilinear sum.
It assumes no Siegel--Walfisz property or coefficient smoothness.  It does
not print a perturbation analogue of Bettin--Chandee Remark 1.  Exact
fractional-phase coefficient separation, proved in Section 3, makes such a
corollary unnecessary for the flat packet.

### Bettin--Chandee, Corollary 1

For a fixed nonzero integer determinant \(\Delta_{\rm det}\), Corollary 1
defines

\[
 \mathcal T=
 \sum_{\substack{m_i\in\mathcal M_i,\ n_i\in\mathcal N_i\\
                  m_1n_2-m_2n_1=\Delta_{\rm det}}}
 f(m_1)g(m_2)\alpha_{n_1}\beta_{n_2},
\tag{BC-C1a}
\]

where
\(\mathcal M_i=[M_i/2,M_i]\),
\(\mathcal N_i=[N_i/2,N_i]\), and

\[
 f^{(j)}\ll\eta^jM_1^{-j},\qquad
 g^{(j)}\ll\eta^jM_2^{-j}
\]

for all \(j\geq0\) and some \(\eta>1\).  It states

\[
\begin{aligned}
 \mathcal T
 &=\sum_{\substack{n_1\in\mathcal N_1,\ n_2\in\mathcal N_2\\
                   (n_1,n_2)\mid\Delta_{\rm det}}}
 \frac{(n_1,n_2)}{n_1n_2}\alpha_{n_1}\beta_{n_2}
 \int_{\mathbb R}
 f\!\left(\frac{x+\Delta_{\rm det}}{n_2}\right)
 g\!\left(\frac{x}{n_1}\right)\,dx\\
 &\quad+
 O\!\left(
 (\eta\mathfrak R)^{3/2}
 \|\alpha\|_2\|\beta\|_2
 (N_1N_2)^{7/20}
 (N_1+N_2)^{1/4+\varepsilon}
 (M_1M_2)^\varepsilon
 \right),
\end{aligned}
\tag{BC-C1b}
\]

where

\[
 \mathfrak R=
 \frac{M_1N_2}{M_2N_1}
 +\frac{M_2N_1}{M_1N_2}.
\]

This is an asymptotic equality, not a modulus-summed discrepancy statement.
The determinant must be nonzero.  The proof notes that if its magnitude is
larger than a constant multiple of
\(M_1N_2+M_2N_1\), both the original sum and main term vanish.  The
fixed-determinant application in Section 3 lies far inside that range.

### Wright dispersion corollaries

Wright Corollary 2.2 bounds a sum over \(q\sim Q\) of the individual
absolute discrepancies for \(mn\equiv a\pmod q\).  It requires a fixed
nonzero integer residue \(a\), \((a,q)=1\), divisor-bounded convolution
coefficients, a Siegel--Walfisz condition on one coefficient, and a
principal reduced-residue subtraction.  With \(MN/2\leq Y\leq4MN\), it
also requires one of

\[
\begin{array}{ll}
\text{(i)}&
 e^{(\log Y)^\varepsilon}\leq N
 \leq Q^{-33/28}Y^{17/28-\varepsilon},
 \quad1\leq|a|\leq Y/12,\\
\text{(ii)}&
 e^{(\log Y)^\varepsilon}\leq N
 \leq Y^{7/90-\varepsilon},\quad
 Q\leq Y^{45/89-\varepsilon},\quad
 1\leq|a|\leq Y/12,\\
\text{(iii)}&
 e^{(\log Y)^\varepsilon}\leq N
 \leq Y^{101/630-\varepsilon},\quad
 Q\leq Y^{45/89-\varepsilon},\quad
 1\leq|a|\leq(Y/4)^{\varepsilon/1000}.
\end{array}
\tag{W-disp}
\]

The project does have a fixed shifted residue, but it does not have the
other required interfaces.  Neither Corollary 2.2 nor Theorem 2.3 is used
as an estimate.

## 3. Proof or derivation

Put

\[
 u=\delta-\ell,\qquad
 R=\frac XD=X^{1-\delta},\qquad
 K=\frac{XL}{D^2}=X^{1+\ell-2\delta},\qquad
 \Delta=\frac RK=X^u,\qquad
 F=\frac{XK}{R}=X^{1-u}.
\tag{3.1}
\]

The strict residual range gives

\[
 \frac14<u<\frac12,\qquad 1<K<R,\qquad F\to\infty.
\tag{3.2}
\]

### Exact flat-profile separation and the real centre

Write \(k=Ku,r=Rv\).  After the standard scaling of \(q_L\), the complete
normalized amplitude, including \(K/k\), can be written

\[
 G_\xi(u,v)=
 u^{-1}\widetilde q_L(4u/v^2)W(1/v)
 e\!\left(\xi\Delta^{-1}\frac uv\right),
\tag{3.3}
\]

on a fixed compact rectangle separated from the axes.  Here
\(\widetilde q_L\) denotes the uniformly normalized flat-cell profile.
For every fixed pair \(a,b\geq0\),

\[
 \sup_{0\leq\xi<1,\ \Delta\geq1}
 \left|\partial_u^a\partial_v^b
 e\!\left(\xi\Delta^{-1}\frac uv\right)\right|
 \ll_{a,b}1.
\tag{3.4}
\]

The supplied flat profile has the same uniform fixed-order bounds.
After a fixed buffered extension, Fourier inversion in
\((\log u,\log v)\) gives

\[
 G_\xi(u,v)=
 \iint_{\mathbb R^2}\widehat G_\xi(t_1,t_2)
 u^{it_1}v^{it_2}\,dt_1dt_2,\qquad
 \iint_{\mathbb R^2}|\widehat G_\xi(t_1,t_2)|
 \,dt_1dt_2\ll1.
\tag{3.5}
\]

This is an exact independent-coefficient decomposition with \(O(1)\)
integrated projective mass.  Since the original amplitude is \(K^{-1}G_\xi\),
each fibre has the norms in (1.2), and \(\chi_4(r)\) remains in
\(\beta_r\) until a positive norm is taken.  All source applications may
therefore use

\[
 e(Xk/r)=e(N_0k/r)\,e(\xi k/r)
\]

with integral source frequency \(N_0\).

For direct Bettin--Chandee alone, Remark 1 gives the same result by taking
\(f_{a,N_0}(m,n)=\xi a/n\).  On
\(m\asymp1,n\asymp R,a\asymp K\), one derivative is zero and the other is
\(O(K/R^2)\), so (BC-R) holds with \(Y\asymp K\).  Its oscillation factor is

\[
 \left(1+\frac{N_0K+O(K)}R\right)^{1/2}\asymp F^{1/2}.
\tag{3.6}
\]

### Direct \(m=1\): literal bounds and the optimistic screen

Take

\[
 a=k,\qquad m=1,\qquad n=r,\qquad
 (A,M,N,R_0,\vartheta)=(K,1,R,1,N_0).
\tag{3.7}
\]

Coprimality is automatic, both Wright side conditions hold, and no growing
fixed factor is available: \(M\asymp1\) forces \(R_0=O(1)\), while the
project moduli have no common growing divisor.

The literal product of coefficient norms is

\[
 \|\alpha\|_2\|\beta\|_2\|\nu\|_2
 \asymp\sqrt{R/K}=\Delta^{1/2}.
\tag{3.8}
\]

Substitution in (BC1) gives

\[
\begin{aligned}
 |\mathscr R_{D,L}(X)|
 &\ll_\varepsilon
 \Delta^{1/2}F^{1/2}
 \left((KR)^{7/20}R^{1/4}+(KR)^{1/2}\right)X^\varepsilon\\
 &=F^{1/2}\left(R^{11/10}K^{-3/20}+R\right)X^\varepsilon.
\end{aligned}
\tag{3.9}
\]

The two exponents are (1.3), and

\[
\begin{aligned}
 E_{\rm BC,1}-u
 &=\frac{29}{20}+\frac{27\ell}{20}
   -\frac{23\delta}{10}>\frac3{10},\\
 E_{\rm BC,2}-u
 &=\frac32+\frac{3\ell}{2}
   -\frac{5\delta}{2}>\frac14.
\end{aligned}
\tag{3.10}
\]

Moreover
\(E_{\rm BC,1}-E_{\rm BC,2}=(4\delta-3\ell-1)/20>0\), so the first
term dominates.

This literal calculation is distinct from the earlier generic optimistic
screen.  If

\[
 C_2=
 \|\alpha\|_2\|\beta\|_2\|\nu\|_2(AMN)^{1/2}
\]

denotes the elementary source Cauchy scale, then the literal wave has

\[
 C_2=\Delta^{1/2}(KR)^{1/2}=R,
\tag{3.11}
\]

not \(\Delta\).  Replacing \(C_2\) by the known physical capacity
\(\Delta=X^u\) was an intentionally favourable impossibility screen only.
Under that artificial normalization, the unavoidable second source term is

\[
 \Delta F^{1/2}=X^{(1+u)/2},
\tag{3.12}
\]

which is already \(>X^{5/8}\).  The literal bound (3.9) is larger than this
screen by \(R/\Delta=K\).  Neither expression is a saving; only (3.9) is the
actual theorem bound for the separated wave.

For Wright, (W1) becomes

\[
\begin{aligned}
 |\mathscr R_{D,L}(X)|
 \ll_\varepsilon RF^{1/4}\big(
 &R^{-1/8}+R^{1/8}+K^{-1/20}R^{-3/20}\\
 &+R^{3/20}K^{-3/20}+R^{3/8}\big)X^\varepsilon.
\end{aligned}
\tag{3.13}
\]

The fifth bracket term dominates for \(1<K<R\), giving

\[
 R^{11/8}F^{1/4}
 =X^{13/8+\ell/4-13\delta/8},
\]

\[
 E_{\rm W,dir}-u
 =\frac{13}{8}+\frac{5\ell}{4}
  -\frac{21\delta}{8}>\frac5{16}.
\tag{3.14}
\]

Because the fractional phase was separated before the theorem call, this is
a legal Wright bound for every real \(X\), despite the absence of a printed
Wright perturbation corollary.

### The \(a=m^2\) connector and its sharp diagonal cost

On \((k,r)=1\), integrality of \(N_0\) gives

\[
 k^2\overline k=k+c_{k,r}r,\qquad
 e\!\left(N_0\frac{k^2\overline k}{r}\right)=e(N_0k/r).
\tag{3.15}
\]

The remaining \(e(\xi k/r)\) is already in (3.3).  Thus, after a constant
number of dyadic subdivisions of the square image, take

\[
 a=j^2,\qquad j=m=k,\qquad n=r,\qquad
 (A,M,N,\vartheta)\asymp(K^2,K,R,N_0).
\tag{3.16}
\]

Detect the diagonal by

\[
 \mathbf1_{j=m}=\int_0^1e(t(j-m))\,dt,\qquad
 \alpha_m(t)=m^{-1/2}e(-tm),\qquad
 \nu_{j^2}(t)=j^{-1/2}e(tj).
\tag{3.17}
\]

Both norms are \(O(1)\).  The matrix
\(C_{j,m}=m^{-1}\mathbf1_{j=m}\) has singular values \(m^{-1}\), hence

\[
 \|C\|_*=\sum_{m\asymp K}m^{-1}\asymp1.
\tag{3.18}
\]

This is the optimal Hilbert-space projective norm for the unit flat
diagonal.  It is a sharp factor \(K^{1/2}\) above the direct
\(\|k^{-1}\|_2\asymp K^{-1/2}\).  The conductor detector
\(\mathbf1_{a=m^2}=\int_0^1e(t(a-m^2))\,dt\), with all
\(a\asymp K^2\) present, is legal but pays one avoidable extra
\(K^{1/2}\).

With the sharp decomposition,
\(\|\alpha\|_2\|\nu\|_2\|\beta\|_2\ll R^{1/2}\), and the two
Bettin--Chandee terms are

\[
 F^{1/2}K^{21/20}R^{11/10},\qquad
 F^{1/2}K^{11/8}R.
\tag{3.19}
\]

Their exponents and margins are

\[
\begin{aligned}
 E_{\rm BC,sq,1}
 &=\frac{53}{20}+\frac{31\ell}{20}
   -\frac{37\delta}{10},&
 E_{\rm BC,sq,1}-u&>\frac3{10},\\
 E_{\rm BC,sq,2}
 &=\frac{23}{8}+\frac{15\ell}{8}
   -\frac{17\delta}{4},&
 E_{\rm BC,sq,2}-u&>\frac14.
\end{aligned}
\tag{3.20}
\]

Wright's fifth term gives

\[
 KR^{11/8}F^{1/4}
 =X^{21/8+5\ell/4-29\delta/8},
\]

whose exponent exceeds \(u\) by
\(21/8+9\ell/4-37\delta/8>5/16\).  The connector is exact for every real
centre after preprocessing, but is quantitatively useless.

### Completion order and coefficient independence

There are two different exact completions.

First complete the original smooth \(k\)-weight, including
\(e(\xi k/r)\).  Its normalized Fourier coefficients satisfy, for fixed
\(B>2\),

\[
 |\widehat w_r(h)|
 \ll_B\frac1r
 \left(1+\frac{\|h\|_r}{\Delta}\right)^{-B},
\qquad
 \sum_h|\widehat w_r(h)|\ll K^{-1}.
\tag{3.21}
\]

On the coprime part,

\[
 \sum_{k\bmod r}^{*}w_r(k)e(N_0k/r)
 =\sum_{h\bmod r}\widehat w_r(h)\,
 \mathfrak c_r(N_0+h),
\tag{3.22}
\]

because inversion permutes the reduced residues and the complete inner sum
is the Ramanujan sum \(\mathfrak c_r\).  Without the star, it is the
ordinary additive delta \(r\mathbf1_{r\mid N_0+h}\).  The divisor identity

\[
 \sum_{r\asymp R}\frac{(r,n)}r
 \ll\sum_{d\mid n}\frac{\varphi(d)}d
 \ll_\varepsilon X^\varepsilon
\tag{3.23}
\]

and the \(O(\Delta)\) effective frequencies return
\(\Delta X^\varepsilon\).  The full gcd decomposition, or equivalently the
unstarred additive calculation, restores every noncoprime row.  This is an
owner-complete self-return to the known absolute capacity, not a source
saving.

If the inverse selector is formed first, define

\[
 g_r(m)=
 \mathbf1_{(m,r)=1}\,
 w_r(\overline m_r),\qquad
 \widehat g_r(h)=\frac1r
 \sum_{m\bmod r}g_r(m)e(-hm/r).
\]

Then

\[
 \sum_mg_r(m)e(N_0\overline m/r)
 =\sum_{h\bmod r}\widehat g_r(h)S(N_0,h;r),
\tag{3.24}
\]

with the genuine Kloosterman sum

\[
 S(a,h;r)=\sum_{m\bmod r}^{*}
 e\!\left(\frac{a\overline m+hm}{r}\right).
\]

The inverse permutation destroys smooth Fourier decay.  Parseval gives only

\[
 \sum_h|\widehat g_r(h)|^2\ll\frac1{rK},\qquad
 \sum_h|\widehat g_r(h)|\ll K^{-1/2}.
\tag{3.25}
\]

The exact complete-frequency identity

\[
 \sum_{h\bmod r}|S(N_0,h;r)|^2=r\varphi(r)
\tag{3.26a}
\]

follows by additive orthogonality and is independent of
\((N_0,r)\).  Cauchy with (3.25) therefore yields
\(O(\sqrt{r/K})\) per row and hence

\[
 R\sqrt{R/K}\,X^\varepsilon
 =R\sqrt{\Delta}\,X^\varepsilon
 =X^{1-(\delta+\ell)/2+\varepsilon}.
\tag{3.26}
\]

Its exponent exceeds \(u\) by
\(1-3\delta/2+\ell/2>1/4\).  The coefficient
\(\widehat g_r(h)\) depends jointly on \((r,h)\), so neither trilinear
source theorem accepts it as independent sequences.  Smooth-first is
Ramanujan/additive and returns \(\Delta\); inverse-first is Kloosterman and
costs \(R\sqrt\Delta\).  The two statements must not be conflated.

### Physical shifted residue and fixed determinant

In the divisor form, write \(s=N_0+t\) with \(t\in\mathbb Z\).  Then

\[
 r\mid s
 \quad\Longleftrightarrow\quad
 t\equiv-N_0\pmod r,
\tag{3.27}
\]

and the flat core is

\[
 \sum_t
 \sum_{\substack{r\asymp R,\ r\text{ odd}\\
                 t\equiv-N_0\ ({\rm mod}\ r)}}
 \chi_4(r)W\!\left(\frac{X}{rD}\right)
 \mathcal Q_L\!\left(\frac{r(\xi-t)}{4X}\right),
\tag{3.28}
\]

effectively for \(|t-\xi|\ll\Delta X^\varepsilon\).

Thus the shifted residue is the fixed nonzero integer \(-N_0\), not a real
or modulus-dependent residue.  This correction does not make Wright's
dispersion results applicable:

1. \((N_0,r)=1\) is not uniform;
2. the short integer \(t\) is not a product of two independent positive
   dyadic sequences;
3. the kernel is joint in \((r,t)\);
4. treating the short scale as the convolution size gives
   \(|N_0|\asymp X\gg\Delta\), outside the printed residue ranges;
5. Wright sums individual absolute discrepancies over moduli after a
   principal reduced-residue subtraction, whereas (3.28) has one absolute
   value after the complete \(\chi_4(r)\)-signed scalar and no matching
   principal subtraction.

There is, however, an exact Bettin--Chandee Corollary 1 route.  Fix
\(\tau=N_0-dr\ne0\) and take

\[
 (m_1,n_2,m_2,n_1)=(d,r,1,N_0),\qquad
 \Delta_{\rm det}=-\tau.
\tag{3.29}
\]

Choose a constant dyadic support with the integer \(m_2=1\) in the interior
of a smooth \(g\), take \(f\) on \(d\asymp D\), let \(\alpha\) be the unit
mass at \(N_0\), and put

\[
 \beta_r^{(\tau)}=
 \chi_4(r)W\!\left(\frac{X}{rD}\right)
 \mathcal Q_L\!\left(\frac{r(\xi+\tau)}{4X}\right).
\tag{3.30}
\]

Then

\[
 M_1\asymp D,\quad M_2\asymp1,\quad
 N_1\asymp X,\quad N_2\asymp R,\quad
 \|\alpha\|_2=1,\quad
 \|\beta^{(\tau)}\|_2\ll R^{1/2}.
\]

Because \(DR=X\), the aspect parameter \(\mathfrak R\asymp1\), and
\(\eta=O(1)\).  The source error (BC-C1b) is

\[
 R^{1/2}(XR)^{7/20}X^{1/4+\varepsilon}
 =X^{3/5+\varepsilon}R^{17/20}.
\tag{3.31}
\]

Its exponent is

\[
 E_{\rm det}=\frac{29}{20}-\frac{17\delta}{20}
 >\frac{41}{40}.
\tag{3.32}
\]

For the main term, the integral in (BC-C1b) has length \(O(X)\).
After its printed gcd prefactor, one \(r\)-contribution is
\(O((N_0,r)/r)\), and

\[
 \sum_{r\asymp R}\frac{(N_0,r)}r
 \ll\sum_{g\mid N_0}\frac{\varphi(g)}g
 \ll_\varepsilon X^\varepsilon.
\tag{3.33}
\]

The condition \((N_0,r)\mid\tau\) only decreases the sum.  There are
\(O(\Delta X^\varepsilon)\) effective nonzero determinants.  Triangulating
their main terms returns \(\Delta X^\varepsilon\), while triangulating their
errors appends another factor \(\Delta\) to (3.31).  The excluded
\(\tau=0\) level is one product level and is
\(O_\varepsilon(X^\varepsilon)\) by the divisor bound.

### Full-polytope capacity

Every direct and square source exponent above exceeds \(u\) by a fixed
positive power using only \(\ell\geq0\) and \(\delta<1/2\).  The completion
(3.22) and determinant main terms merely recover the absolute branch
\(\Delta\); (3.24) and the determinant error are much larger.  The extra
condition \(178\ell+1638\delta>463\) opens no hidden favourable chamber.

The accepted flat-wave envelope has exponent

\[
 \beta(u)=\min\!\left(u,\frac{1-u}{2}\right)>\frac14
\qquad\left(\frac14<u<\frac12\right).
\tag{3.34}
\]

No audited source specialization reaches this envelope when it is smaller
than \(\Delta\), and none reaches \(1/4\).

## 4. First doubtful or unproved step

After this owner repair, the scoped source no-go has no remaining
frequency, separation, normalization, completion-order, determinant, or
exponent gap.  The first unproved positive step is a new theorem for the
literal coupled signed family

\[
 \sum_{k\asymp K}\frac1k
 \sum_{r\asymp R}
 \chi_4(r)G(k/K,r/R)e(Xk/r),
\tag{4.1}
\]

or its exact fixed-centre form (3.28), which keeps the
\(\chi_4(r)\)-sum before positive row norms and beats the accepted exponent
\(\beta(u)\).  Neither Bettin--Chandee nor Wright accepts the
modulus-dependent inverse-selector matrix or supplies a pointwise signed
fixed-centre dispersion estimate.  Corollary 1 has no signed average over
determinants and therefore cannot aggregate its error nontrivially.

The proof of the \(O(1)\) Fourier--Mellin mass uses the frozen flat cell's
uniform normalized seminorms.  It does not extend automatically to sharp,
clipped, starred, hard, transition, arithmetic-owner, or endpoint kernels.
Those owners remain outside the present report rather than being silently
absorbed.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Primary-source versions | Pass. Bettin--Chandee arXiv:1502.00769v1 and Wright arXiv:2604.25177v2 are the audited versions. |
| Printed frequency type | Pass with repair. Bettin--Chandee is source-safe only for integral \(\vartheta\); Wright states this explicitly. Every application uses \(N_0=\lfloor X\rfloor\). |
| Real centre | Pass. The factor \(e(\xi k/r)\) has uniformly bounded normalized derivatives and \(O(1)\) separation mass. Direct Bettin--Chandee and Wright, the square connector, and both completions are legal for every real \(X\). |
| Bettin--Chandee Remark 1 | Pass. The direct perturbation \(f=\xi a/n\) has \(Y\asymp K\) and does not change the \(F^{1/2}\) scale. |
| Wright printed/proof third term | Pass with recorded convention. The statement has \(A_0^{-1/20}\), the proof ends with \(A_0^{-3/10}\), and the weaker printed theorem is used. The common fifth term dominates. |
| Coupled flat profile | Pass. Equation (3.5) certifies exact independent-coefficient separation with \(O(1)\) integrated projective mass. |
| Generic versus literal normalization | Pass with explicit distinction. The optimistic screen set \(C_2=\Delta\); the literal separated wave has \(C_2=R\). |
| Direct \(m=1\) | Legal but non-saving. The literal exponents (1.3)--(1.4) exceed \(u\) by fixed powers. |
| Growing fixed factor | Illegal for the owner-complete direct row. \(M\asymp1\) forces \(R_0=O(1)\). |
| Bettin--Chandee Theorem 2 character | No gain. At \(m=1\), \(\left(\frac1n\right)=1\); \(\chi_4(n)\) remains only in \(\beta_n\). |
| \(a=m^2\) connector | Legal for real \(X\) after coefficient absorption, with sharp diagonal nuclear norm \(\asymp1\), source length \(A\asymp K^2\), and non-saving exponents. |
| Smooth-weight-first completion | Ramanujan/additive, not Kloosterman. It restores all gcd strata and returns \(\Delta X^\varepsilon\). |
| Inverse-selector-first completion | Kloosterman, not Ramanujan. Its coefficient is joint in \((r,h)\); positive closure costs \(R\sqrt\Delta X^\varepsilon\). |
| Physical shifted residue | Repaired. The residue is the fixed integer \(-N_0\), but uniform coprimality, convolution, range, joint-coefficient, principal-term, and absolute-value hypotheses fail. |
| Corollary 1 determinant route | Pass. The exact determinant, supports, smoothness, aspect ratio, coefficient norms, main term, error, nonzero range, and determinant aggregation are audited. |
| Absolute-value placement | Pass for the trilinear theorems and Corollary 1; fail for a proposed direct import of Wright's modulus-summed dispersion discrepancy. |
| Actual \(\chi_4\) placement | Preserved before every source absolute value or positive norm. The generic theorems then extract no character-specific cancellation. |
| Full strict-UNBAL polytope | Pass. Every comparison is uniform for \(1/4<u<1/2\); the additional residual inequality cannot create a target-safe chamber. |
| Endpoint and owner scope | Pass. No sharp, hard, transition, complete-UNBAL, BAL, TOP, endpoint, M9-M2, M9-M1, M9, or global assertion is made. |
| Withdrawn negative control | Pass. arXiv:2601.00292v2 is used only as a withdrawn bibliographic control, never as a theorem. |
| Report hygiene | Pass. The owner-repaired report has seven sections, no control characters, and balanced displayed mathematics. |

No numerical experiment was used.  The allocation was 100% analytical and
source work.

The complete specialization ledger is:

| Proposed interface | Source legality | Exact outcome |
|---|---|---|
| Bettin--Chandee Theorem 1, \(m=1\), real \(X\) | Legal with integral \(N_0\) after (3.5), or via Remark 1. | Literal exponents (1.3), both worse than \(\Delta\). |
| Wright Theorem 2.1, \(m=1\), real \(X\), \(R_0=1\) | Legal after (3.5); no perturbation theorem is needed. | Dominant exponent (1.4), worse than \(\Delta\). |
| Wright with growing \(R_0\) | Illegal for the complete direct row. | \(R_0\ll M^C\) and \(M\asymp1\) force \(R_0=O(1)\). |
| Coprime \(a=m^2,m=k\) | Legal for real \(X\) after (3.3), with constant-many square-scale blocks. | Sharp projective norm \(\asymp1\); all source exponents exceed \(\Delta\). |
| Smooth \(k\)-weight completion | Exact but not a new trilinear specialization. | Ramanujan/additive self-return of size \(\Delta X^\varepsilon\). |
| Inverse-selector completion | Not an independent source tensor. | Kloosterman matrix with positive cost \(R\sqrt\Delta X^\varepsilon\). |
| Shifted physical residue \(-N_0\) | Exact congruence but illegal for Wright dispersion. | Remaining hypotheses and absolute-value placement fail. |
| Bettin--Chandee Corollary 1, fixed \(\tau\ne0\) | Legal with dictionary (3.29). | Main term \(O(X^\varepsilon)\) per level; error (3.31); aggregation is non-saving. |

## 6. Dependencies and exact artifacts used

Local artifacts read and used:

- `protocol.md`;
- `state/proof_obligations.yml`, with the Round-135 target obligations
  checked;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/primary_source_manifest.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/briefs/wright_bc_exact_source_card.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/blind_inverse_congruence_interface_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/candidates/conductor_degenerate_source_capacity.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/source_post_unmask_discovery_formula_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/blind_post_unmask_source_and_capacity_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reviews/discovery_post_unmask_blind_completion_audit.md`.

Primary sources, accessed 23 August 2026:

- Bettin--Chandee, arXiv:1502.00769v1: version record
  <https://arxiv.org/abs/1502.00769>, primary HTML
  <https://arxiv.org/html/1502.00769v1>, and primary PDF
  <https://arxiv.org/pdf/1502.00769v1>.  Audited Theorem 1, Remark 1,
  Theorem 2 as a character control, Corollary 1, and the proof of
  Corollary 1.
- Wright, arXiv:2604.25177v2: version record
  <https://arxiv.org/abs/2604.25177>, primary HTML
  <https://arxiv.org/html/2604.25177v2>, and primary PDF
  <https://arxiv.org/pdf/2604.25177>.  Audited the definition and full
  statement of Theorem 2.1, its final proof line, and Corollary 2.2 solely
  for the failed physical-interface screen.
- Withdrawn bibliographic control only:
  <https://arxiv.org/abs/2601.00292>.  Version v2 records a missing
  \(L^2\) factor that changes \(L^5\) to \(L^7\) and removes the claimed
  improvement.  It supplied no theorem.

No secondary source supplied a mathematical claim.

## 7. Recommended state effect

\(\mathtt{retain}\).

Retain this owner-repaired report as a scoped
\(\mathtt{source\_level\_no\_go}\).  The audited direct, square-connector,
completion, physical-residue, and fixed-determinant interfaces do not improve
the accepted flat-wave envelope and do not prove the quarter target.

Retain the flat smooth prescribed-centre estimate as open.  Do not promote
complete UNBAL, M9-M2, M9-M1, endpoint uniformity, M9, the quarter theorem,
or any global exponent improvement.  A future proof may still exploit a new
coefficient-matrix or sign-preserving fixed-centre dispersion theorem; this
source audit neither proves the literal wave large nor rules out such a
theorem.
