# Post-unmask source audit of the Round-135 discovery formulas

Campaign: `m9-m2-unbalanced-kloosterman-dispersion-source-map`  
Round: 135  
Role: independent source/formula reviewer  
Starting graph SHA-256: `f9aa6fa43900b9cb73f705405f9a6090e6e84fb5d3c8a9e037ffe3c6911b9ea0`

## 1. Result

**Verdict: pass with repair.**  The discovery report's quantitative
source-capacity conclusion is correct: every literal Bettin--Chandee or
Wright specialization that it prices is larger than the already accepted
flat-row capacity, and Bettin--Chandee Corollary 1 is still much larger even
for one nonzero determinant.  I independently recover all of the displayed
direct and square-connector exponents, the optimal diagonal nuclear norm, the
inverse-first completion cost, and the fixed-determinant main and error terms.
No imported theorem yields a quarter estimate or a smaller owner-complete
survivor.

The report nevertheless needs a substantive, conclusion-preserving repair
at the real centre.  The primary sources support an integral frequency:
Bettin--Chandee's printed Theorem 1 does not type \(\vartheta\), but its proof
uses integer gcd and coprimality operations on it; Wright v2 explicitly calls
\(\vartheta\) a nonzero integer.  Thus the report must not put
\(\vartheta=X\) when \(X\notin\mathbb Z\).  There are two legal repairs.

1. For direct Bettin--Chandee, write \(X=N_0+\xi\),
   \(N_0=\lfloor X\rfloor\), and use Remark 1 with
   \(f_{a,N_0}(m,n)=\xi a/n\).  Its perturbation parameter is \(Y\asymp K\),
   so the oscillation factor remains \(F^{1/2}\).
2. More cleanly, on the frozen flat cell absorb \(e(\xi k/r)\) into the
   uniformly smooth two-variable amplitude before Fourier/Mellin separation.
   Since \(k/r=\Delta^{-1}u/v\), this has uniformly bounded normalized
   derivatives.  All subsequent source phases then have the integral
   frequency \(N_0\).  This repairs not only direct Bettin--Chandee but also
   direct Wright, the \(a=m^2\) connector, and both completion orders for every
   real \(X\), without changing any norm or exponent.

The second repair shows that the discovery report's claims that the
nonconstant connector and classical completion are restricted to integral
centres are false as written.  It also supersedes the source report's
provisional statement that Wright is illegal for nonintegral \(X\): Wright
has no perturbation corollary, but none is needed after the fractional phase
has been put into the arbitrary separated coefficients.

A second repair must distinguish completion orders.  Fourier expansion after
inverse reindexing in the variable \(m\) gives complete Kloosterman sums.
Fourier expansion of the original smooth \(k\)-weight first gives Ramanujan
sums on the coprime part (and an ordinary complete additive delta without the
coprimality restriction).  The latter order recovers the
\(\Delta X^\varepsilon\) absolute capacity, not the larger
\(R\sqrt\Delta\) inverse-first estimate, but gives no strict improvement and
no legal independent Bettin--Chandee/Wright tensor.  These repairs strengthen
the audit while leaving its scoped `source_level_no_go` conclusion intact.

## 2. Exact statement and hypotheses

Let \(X\geq2\) be real and put

\[
 D=X^\delta,\qquad L=X^\ell,\qquad R=X^{1-\delta},\qquad
 K=X^{1+\ell-2\delta},\qquad
 \Delta=R/K=X^{\delta-\ell},\qquad F=XK/R=X^{1+\ell-\delta},
\]

with

\[
 \frac14\leq\delta<\frac12,\qquad
 0\leq\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
\]

Thus \(K,R\to\infty\), \(1<K<R\), and
\(1/4<\delta-\ell<1/2\).  Only one frozen flat smooth component of

\[
 \mathscr R_{D,L}(X)=
 \sum_{r\asymp R,\ r\text{ odd}}\chi_4(r)W(X/(rD))
 \sum_{k\asymp K}\frac{q_L(4Xk/r^2)}{k}e(Xk/r)
\tag{2.1}
\]

is under review.  The component has fixed normalized compact support away
from both coordinate axes and uniform fixed-order seminorms.

The source hypotheses used here are the following.

- Bettin--Chandee, arXiv:1502.00769v1, Theorem 1, has arbitrary complex
  sequences on \([A/2,A]\), \([M/2,M]\), and \([N/2,N]\), the condition
  \((m,n)=1\), phase \(e(\vartheta a\overline m/n)\), product of the three
  \(\ell^2\)-norms, and one absolute value outside the full trilinear sum.
  There is no balance condition on \(A,M,N\).  Source verification restricts
  \(\vartheta\) to a nonzero integer.  Remark 1 permits its stated
  \(C^1\) real perturbation with the corresponding extra parameter in the
  oscillation factor.
- Wright, arXiv:2604.25177v2, Theorem 2.1, has phase
  \(e(\vartheta a\overline m/(nR_0))\), arbitrary independent complex
  sequences, \((m,nR_0)=1\), integral \(\vartheta\ne0\), and one absolute
  value outside the full sum.  It assumes \(M\ll N^2\) and a fixed positive
  integer factor \(R_0\ll M^C\).  The theorem has no printed perturbation
  clause.  Its printed third bracket term contains \(A^{-1/20}\), whereas
  the last bound in the proof contains the stronger \(A^{-3/10}\).  This
  audit uses the weaker printed theorem.  The decisive fifth term is the
  same in the statement and proof, so the discrepancy changes none of the
  direct or square-connector conclusions below.
- Bettin--Chandee Corollary 1 assumes a fixed nonzero integer determinant,
  smooth \(f,g\) with the printed derivative bounds, arbitrary
  \(\alpha,\beta\), and the four dyadic supports in its statement.  Its main
  term and error are exactly those printed in (1.4) of the source.

After the real-centre repair below, the legally audited dictionaries are

\[
 (A,M,N,R_0,\vartheta)=(K,1,R,1,N_0)
\tag{2.2}
\]

for the direct row, and, on \((k,r)=1\),

\[
 a=j^2,\qquad m=j=k,\qquad n=r,\qquad \vartheta=N_0,
 \qquad (A,M,N)=(K^2,K,R)
\tag{2.3}
\]

for the nonconstant connector.  The fixed-determinant dictionary is

\[
 (m_1,n_2,m_2,n_1)=(d,r,1,N_0),\qquad
 \Delta_{\rm det}=-\tau,\qquad \tau=N_0-dr\ne0.
\tag{2.4}
\]

No statement here covers nonflat, sharp, clipped, starred, hard,
arithmetic-owner, transition, remainder, BAL, TOP, complete-UNBAL, endpoint,
M9-M2, M9-M1, M9, or global objects.

## 3. Proof or derivation

### 3.1 Uniform separation, including the fractional centre

Write \(k=Ku\), \(r=Rv\), and \(X=N_0+\xi\), with
\(0\leq\xi<1\).  The discovery report correctly observes that

\[
 \frac{4Xk}{r^2}=4L\frac{u}{v^2},\qquad \frac{X}{rD}=\frac1v.
\]

After the standard scaling of \(q_L\), the complete amplitude, including
\(K/k\), is a uniformly smooth compactly supported function \(G(u,v)\).
The useful strengthened amplitude is

\[
 G_{\xi,\Delta}(u,v)=G(u,v)
 e\!\left(\frac{\xi}{\Delta}\frac{u}{v}\right),
\tag{3.1}
\]

because \(k/r=(K/R)u/v=\Delta^{-1}u/v\).  On the fixed support, for every
fixed multi-index \((a,b)\),

\[
 \sup_{0\leq\xi<1,\ \Delta\geq1}
 \left|\partial_u^a\partial_v^b
 e\!\left(\frac{\xi}{\Delta}\frac{u}{v}\right)\right|\ll_{a,b}1.
\tag{3.2}
\]

After a buffered extension, Fourier inversion in \((\log u,\log v)\)
therefore gives an exact rank-one integral with
\(\iint|\widehat G_{\xi,\Delta}|\ll1\), uniformly in the packet and in the
real centre.  Each fibre has

\[
 \|\alpha\|_2\asymp1,\qquad
 \|\nu\|_2\asymp K^{-1/2},\qquad
 \|\beta\|_2\asymp R^{1/2},
\tag{3.3}
\]

with \(\chi_4(r)\) still inside \(\beta_r\).  Thus the discovery report's
bounded-separation claim passes, and (3.1) supplies the missing uniform
real-centre version at the same cost.

For comparison, direct Bettin--Chandee can also be repaired without (3.1).
In Remark 1 take the integral source frequency \(N_0\) and
\(f_{a,N_0}(m,n)=\xi a/n\).  In the source's correctly interpreted order
\(x=n\asymp R,y=m\asymp1\), the nonzero derivative is
\(O(K/R^2)\); hence the printed condition holds with \(Y\asymp K\).  The
factor becomes

\[
 \left(1+\frac{N_0K+O(K)}R\right)^{1/2}\asymp F^{1/2}.
\tag{3.4}
\]

This verifies the requested Remark 1 seam.  Absorption (3.1) is preferable
because it also works for Wright and the nondegenerate maps.

### 3.2 Direct \(m=1\) substitutions and literal normalization

Use (2.2), with the separated fractional factor in the coefficients.  The
literal product of coefficient norms is

\[
 \|\alpha\|_2\|\beta\|_2\|\nu\|_2
 \asymp (R/K)^{1/2}=\Delta^{1/2}.
\tag{3.5}
\]

Bettin--Chandee gives exactly

\[
 \Delta^{1/2}F^{1/2}
 \left((KR)^{7/20}R^{1/4}+(KR)^{1/2}\right).
\tag{3.6}
\]

The two powers of \(X\) are

\[
 E_{\rm BC,1}=\frac{29}{20}+\frac{7\ell}{20}
                  -\frac{13\delta}{10},\qquad
 E_{\rm BC,2}=\frac32+\frac\ell2-\frac{3\delta}{2}.
\tag{3.7}
\]

They satisfy

\[
 E_{\rm BC,1}-(\delta-\ell)
 =\frac{29}{20}+\frac{27\ell}{20}-\frac{23\delta}{10}>\frac3{10},
\]

\[
 E_{\rm BC,2}-(\delta-\ell)
 =\frac32+\frac{3\ell}{2}-\frac{5\delta}{2}>\frac14.
\tag{3.8}
\]

Also
\(E_{\rm BC,1}-E_{\rm BC,2}=(4\delta-3\ell-1)/20>0\), so the first
term dominates.  These are the discovery report's exponents and they pass.

This calculation must be kept distinct from the source report's deliberately
optimistic generic normalization.  That report defined

\[
 C_2=\|\alpha\|_2\|\beta\|_2\|\nu\|_2(AMN)^{1/2}
\]

and, only as a favourable impossibility screen, replaced \(C_2\) by the
known physical capacity \(\Delta\).  For the literal separated wave,

\[
 C_2=\Delta^{1/2}(KR)^{1/2}=R,
\tag{3.9}
\]

not \(\Delta\).  The source report's \(X^{(1+u)/2}\),
\(u=\delta-\ell\), is therefore not a claimed literal wave bound.  The
discovery report correctly uses (3.9); its literal result is larger than
that optimistic screen by the factor \(R/\Delta=K\).

For Wright, \(R_0=1\) is the only owner-complete fixed factor.  Its two side
conditions hold, (3.9) is again the base Cauchy scale, and the fifth bracket
term dominates the other four because \(R>K>1\).  The result is

\[
 R^{11/8}F^{1/4}=X^{13/8+\ell/4-13\delta/8},
\]

and

\[
 \left(\frac{13}{8}+\frac\ell4-\frac{13\delta}{8}\right)
 -(\delta-\ell)
 =\frac{13}{8}+\frac{5\ell}{4}-\frac{21\delta}{8}>\frac5{16}.
\tag{3.10}
\]

The algebra passes.  Its source-legality statement needs repair: after
(3.1), the source frequency is the nonzero integer \(N_0\), so Wright's
direct estimate is legal for every real project centre even though Wright
does not print a perturbation theorem.

### 3.3 The \(a=j^2,m=k\) connector and its optimal cost

On \((k,r)=1\), integrality of \(N_0\) gives

\[
 k^2\overline k=k+c_{k,r}r,\qquad
 e\!\left(N_0\frac{k^2\overline k}{r}\right)=e(N_0k/r).
\tag{3.11}
\]

The remaining \(e(\xi k/r)\) is already in the uniformly separated
amplitude (3.1).  Thus this connector is legal for all real \(X\), not only
for integral \(X\).

The discovery report's diagonal decomposition is optimal.  With \(a=j^2\),

\[
 \mathbf1_{j=m}=\int_0^1e(t(j-m))\,dt,
\]

and the factor \(1/m\) may be split as
\(m^{-1/2}e(-tm)\cdot j^{-1/2}e(tj)\).  Each norm is \(O(1)\), while the
diagonal matrix

\[
 C_{j,m}=m^{-1}\mathbf1_{j=m}
\]

has

\[
 \|C\|_*=\sum_{m\asymp K}m^{-1}\asymp1.
\tag{3.12}
\]

The square map \(j\mapsto j^2\) is an isometry of the coefficient index set,
and sparse support on squares is allowed because the source coefficients are
arbitrary.  Smooth separated fibre factors merely multiply the diagonal
entries by uniformly bounded one-variable weights.  Hence the projective
norm is \(O(1)\) (and \(\asymp1\) on a nonvanishing flat cell), a sharp
factor \(K^{1/2}\) above the direct \(k^{-1}\) norm.

After a constant number of dyadic subdivisions of the square image, the
source lengths are exactly \((A,M,N)\asymp(K^2,K,R)\); the oscillation ratio
is still \(N_0A/(MN)\asymp F\), and the remaining norm is \(R^{1/2}\).
The two Bettin--Chandee terms before conversion to \(X\)-powers are

\[
 F^{1/2}\left(K^{21/20}R^{11/10}+K^{11/8}R\right).
\tag{3.13}
\]

They give

\[
 E_{\rm BC,sq,1}=\frac{53}{20}+\frac{31\ell}{20}
                         -\frac{37\delta}{10},\qquad
 E_{\rm BC,sq,2}=\frac{23}{8}+\frac{15\ell}{8}
                         -\frac{17\delta}{4},
\tag{3.14}
\]

with excesses

\[
 \frac{53}{20}+\frac{51\ell}{20}-\frac{47\delta}{10}>\frac3{10},
 \qquad
 \frac{23}{8}+\frac{23\ell}{8}-\frac{21\delta}{4}>\frac14.
\tag{3.15}
\]

For Wright, the dominant fifth term is

\[
 KR^{11/8}F^{1/4}
 =X^{21/8+5\ell/4-29\delta/8},
\tag{3.16}
\]

whose exponent exceeds \(\delta-\ell\) by
\(21/8+9\ell/4-37\delta/8>5/16\).  Every exponent in the discovery report
therefore passes.  The conductor candidate's detector
\(\mathbf1_{a=m^2}=\int e(t(a-m^2))dt\) is also legal, but its norm product
has an avoidable extra \(K^{1/2}\); its displayed terms with
\(K^{31/20}\) and \(K^{15/8}\) must not be presented as the optimal square
connector.  Formula (3.13) is the sharp source-capacity version.

### 3.4 The two completion orders

After (3.1), all classical complete sums use the integral parameter \(N_0\).
There are two distinct operations.

**Inverse first, Fourier transform in \(m\).**  Put
\(m=\overline k\pmod r\), let \(g_r(m)\) be the resulting inverse-image
weight (including the separated fractional coefficient), and set

\[
 \widehat g_r(h)=\frac1r\sum_{m\bmod r}g_r(m)e(-hm/r).
\]

Then

\[
 \sum_mg_r(m)e(N_0\overline m/r)
 =\sum_{h\bmod r}\widehat g_r(h)S(N_0,h;r).
\tag{3.17}
\]

This is a complete Kloosterman sum; only the special term \(h=0\) is a
Ramanujan sum.  Since \(g_r\) has \(K\) entries of size \(O(K^{-1})\),

\[
 \sum_h|\widehat g_r(h)|^2\ll\frac1{rK},\qquad
 \sum_h|\widehat g_r(h)|\ll K^{-1/2}.
\]

Under the deliberately favourable condition \((N_0,r)=1\), Weil gives
\(O_\varepsilon(\sqrt{r/K}\,r^\varepsilon)\) per row and hence

\[
 R\sqrt{R/K}=R\sqrt\Delta
 =X^{1-(\delta+\ell)/2},
\]

whose exponent exceeds \(\delta-\ell\) by
\(1-3\delta/2+\ell/2>1/4\).  This verifies the discovery report's
Kloosterman-first completion ledger.  For general real \(X\), its references
to \((X,r)\) and \(S(X,h;r)\) must be replaced by
\((N_0,r)\) and \(S(N_0,h;r)\).

**Smooth \(k\)-weight first.**  On the coprime part, Fourier-expand the
original smooth row weight \(w_r(k)\), including \(e(\xi k/r)\), before
inverse reindexing:

\[
 w_r(k)=\sum_{h\bmod r}\gamma_r(h)e(hk/r),\qquad
 |\gamma_r(h)|\ll_B\frac1r
 \left(1+\frac{\|h\|_r}{\Delta}\right)^{-B}.
\]

Then

\[
 \sum_{k\bmod r}^{*}w_r(k)e(N_0k/r)
 =\sum_{h\bmod r}\gamma_r(h)c_r(N_0+h),
\tag{3.18}
\]

where \(c_r(\cdot)\) is the Ramanujan sum.  Without the star the complete
inner sum is instead \(r\mathbf1_{r\mid N_0+h}\), an ordinary additive
delta.  Using \(|c_r(n)|\ll_\varepsilon r^\varepsilon(r,n)\) and

\[
 \sum_{r\asymp R}\frac{(r,n)}r
 \leq\sum_{d\mid n}\frac{\varphi(d)}d\ll_\varepsilon X^\varepsilon,
\]

the absolute aggregate in (3.18) is

\[
 \ll_\varepsilon \Delta X^\varepsilon.
\tag{3.19}
\]

Thus the other completion order exactly recovers the accepted absolute
capacity but does not improve it.  Its coefficients \(\gamma_r(h)\) still
depend jointly on \((r,h)\), so it is not an independent trilinear source
tensor.  The conductor candidate's blanket word “Ramanujan” is correct only
for this original/inverse-coordinate completion; the discovery report's
word “Kloosterman” is correct only for (3.17).  The blind report's complete
inner sum in its formula (3.3) is likewise a Ramanujan sum after the
integral-frequency repair, so a subsequent scalar Bettin--Chandee/Wright
estimate is unnecessary and weaker than (3.19).

### 3.5 Fixed determinant: dictionary, main term, error, aggregation

Fix \(\tau=N_0-dr\ne0\).  Dictionary (2.4) gives
\(m_1n_2-m_2n_1=dr-N_0=-\tau\) exactly.  Choose constant dyadic parameters
so that the integer \(m_2=1\) lies in the interior of the support of a smooth
\(g\), take \(f\) on \(d\asymp D\), take \(\alpha\) to be the unit mass at
\(N_0\), and set

\[
 \beta_r^{(\tau)}=\chi_4(r)W(X/(rD))
 \mathcal Q_L\!\left(\frac{r(\xi+\tau)}{4X}\right).
\tag{3.20}
\]

Thus

\[
 M_1\asymp D,\quad M_2\asymp1,\quad N_1\asymp X,\quad N_2\asymp R,
 \quad \|\alpha\|_2=1,\quad\|\beta^{(\tau)}\|_2\ll R^{1/2}.
\]

Because \(DR=X\), the corollary's aspect parameter is \(\asymp1\), and the
fixed smoothness parameter is \(O(1)\).  Its error is

\[
 R^{1/2}(XR)^{7/20}X^{1/4}X^\varepsilon
 =X^{3/5+\varepsilon}R^{17/20}.
\tag{3.21}
\]

The exponent is \(29/20-17\delta/20>41/40\), exactly as in the discovery
report.  The effective determinants satisfy
\(|\tau+\xi|\ll\Delta X^\varepsilon\), so they are far inside the source
proof's harmless \(|\Delta_{\rm det}|\ll M_1N_2+M_2N_1\asymp X\) range.

For the main term, the integral has length \(O(X)\).  Multiplication by the
printed factor \((N_0,r)/(N_0r)\) gives
\(O((N_0,r)/r)\), and hence, even before using
\((N_0,r)\mid\tau\),

\[
 \sum_{r\asymp R}\frac{(N_0,r)}r
 \leq\sum_{g\mid N_0}\frac{\varphi(g)}g
 \ll_\varepsilon X^\varepsilon.
\tag{3.22}
\]

Therefore one determinant main term is \(O(X^\varepsilon)\).  Corollary 1
has no average over determinants: triangulating the
\(O(\Delta X^\varepsilon)\) levels gives \(\Delta X^\varepsilon\) for the
main terms and appends a factor \(\Delta\) to (3.21) for the errors.  The
excluded \(\tau=0\) level is one divisor level and is
\(O_\varepsilon(X^\varepsilon)\).  Every determinant formula and capacity
claim in the discovery report passes.

### 3.6 Source scope and endpoints

All capacity comparisons above use only \(\ell\geq0\) and
\(\delta<1/2\); the additional inequality
\(178\ell+1638\delta>463\) cannot open a favourable chamber.  The strict
upper endpoint \(\delta=1/2\) is never inserted.  The lower formal point
\((\delta,\ell)=(1/4,0)\) is infeasible because
\(\ell<\delta-1/4\) is strict.  The fixed-determinant estimate is valid on
its nonzero determinant levels, and the zero level is handled separately.

The source theorems see arbitrary coefficient signs only through positive
\(\ell^2\)-norms; they preserve \(\chi_4\) before the source absolute value
but extract no character-specific cancellation.  The result is accordingly
an upper-bound capacity obstruction to these imports, not a lower bound for
the literal signed wave.  No downstream or endpoint claim is licensed.

## 4. First doubtful or unproved step

After the repairs in Sections 1--3, there is no remaining doubtful source or
algebra step in the scoped no-go.  The first unproved step of any positive
continuation is an estimate for the genuinely coupled, sign-sensitive
coefficient family

\[
 \sum_{k\asymp K}\frac1k\sum_{r\asymp R}
 \chi_4(r)G(k/K,r/R)e(Xk/r),
\]

or for its equivalent fixed-centre divisor form, which gains below the
accepted envelope while keeping the real centre and the one outer absolute
value.  Neither primary source accepts the inverse-selector matrix or the
\((r,h)\)-dependent completion coefficients.  Corollary 1 also supplies no
signed determinant average, so its per-determinant error cannot be aggregated
nontrivially from the printed statement.

The only analytic input used to certify the separation is the frozen flat
cell's uniform normalized seminorm hypothesis.  It does not extend by itself
to sharp, transition, hard, or endpoint owners; those remain the first scope
boundary, not an omitted step in this flat-cell review.

## 5. Required control tests, outcomes, and repair ledger

| Control | Outcome |
|---|---|
| Primary versions and theorem text | Pass. Bettin--Chandee v1 Theorem 1, Remark 1, Corollary 1 and its proof, and Wright v2 Theorem 2.1 were checked in the primary HTML. The withdrawn arXiv:2601.00292 was not used as a theorem. |
| Wright printed/proof discrepancy | Pass with recorded convention. The printed third term is \(A^{-1/20}\), while the proof ends with \(A^{-3/10}\). The weaker printed statement is used; the fifth term dominates and agrees in both locations. |
| Frequency type | Pass with repair. Both audited trilinear uses must have integral frequency; use \(N_0=\lfloor X\rfloor\). |
| Fractional centre | Pass with repair. BC Remark 1 is legal with \(Y\asymp K\). Uniform absorption (3.1) is stronger and makes BC, Wright, the square connector, and both completions legal for all real \(X\). |
| Moving profile | Pass. Log-Fourier/Mellin mass is \(O(1)\) and the literal norms are (3.3). |
| Generic versus literal normalization | Pass after explicit distinction. The source report's \(C_2=\Delta\) was an optimistic screen; the literal wave has \(C_2=R\). |
| Direct exponent algebra | Pass. Equations (3.7)--(3.10) reproduce the discovery report. |
| Square diagonal and lengths | Pass with real-centre repair. The optimal nuclear norm is \(\asymp1\), \(A=K^2,M=K,N=R\), and all exponents (3.14)--(3.16) are correct. |
| Completion order | Pass with clarification. Inverse-first/additive-in-\(m\) gives Kloosterman sums and cost \(R\sqrt\Delta\); smooth-\(k\)-first gives Ramanujan sums and recovers \(\Delta X^\varepsilon\). |
| Corollary 1 | Pass. Supports, nonzero determinant, aspect ratio, coefficient norms, main term, error, and determinant triangle all match the source. |
| Character and absolute values | Pass. \(\chi_4\) remains in the source coefficient until a positive norm is taken; no Wright dispersion absolute value is substituted for the project's outer absolute value. |
| Polytope and owner scope | Pass. Every inequality is uniform on the strict flat-UNBAL region and no endpoint or downstream owner is promoted. |

The exhaustive discovery-report repair list is:

1. In (1.1) and (3.4), replace \(\vartheta=X\) by
   \(\vartheta=N_0\), and include \(e(\xi k/r)\) in the separated amplitude.
   Equations (3.5)--(3.8) are unchanged up to \(N_0\asymp X\).
2. Replace lines 172--176 and the rational/irrational discussion following
   (3.8): there is no real-centre obstruction on the frozen flat cell.
   Bettin--Chandee is also legal via Remark 1, and both direct theorems are
   legal via (3.1).  Rational lifting is unnecessary.
3. In (1.4), write unambiguously
   \(a=j^2,\ j=m=k,\ n=r\).  Remove “at integral centres.”
4. In (3.9), use \(N_0\), insert the missing backslash in `\qquad`, and
   place the fractional factor in (3.1).  Delete the claimed nonintegral
   obstruction following (3.17).
5. In (3.17), replace `X^{,21/8+...}` by
   \(X^{21/8+5\ell/4-29\delta/8}\).
6. In (3.18)--(3.22), replace \(X\) in the classical complete-sum parameter
   by \(N_0\), and replace \((X,r)=1\) by \((N_0,r)=1\).  Add the distinct
   Ramanujan completion (3.18)--(3.19); do not call every completion
   Kloosterman or every completion Ramanujan.
7. Rewrite real-centre control 5 in Section 5: the congruence connectors and
   completions are legal for every real centre after fractional-phase
   separation; their failure is quantitative/coefficient-geometric, not an
   irrational-frequency failure.
8. In (2.2), (2.3), and (3.23), replace the embedded carriage-return
   corruption in `r\ {\rm odd}` by `r\text{ odd}`.  This corruption currently
   splits each displayed formula.
9. In (3.13), insert whitespace before `\tag{3.13}`.  This is presentational,
   not mathematical.

Cross-artifact consistency repairs, which should be observed in the round
synthesis but do not change the audited discovery exponents, are:

- the source report's “coupled profile not certified” is superseded by the
  exact bounded separation in Section 3.1, and its nonintegral-Wright
  illegality is superseded by (3.1); its optimistic \(C_2=\Delta\) screen is
  not to be quoted as the literal bound;
- in the conductor candidate, (135.C3) has two missing backslashes before
  `\qquad`, and the displays (135.C12), (135.C17), and (135.C18) lack closing
  delimiters; (135.C15) is a legal but nonoptimal detector cost, and the word
  “Ramanujan” needs the completion-order qualification above;
- the blind report's real \(\vartheta\) reading is not source-verified.  After
  the \(N_0+\xi\) repair, its complete inner sum in (3.3) is a Ramanujan sum,
  so its later scalar-source completion estimate is only a weaker screen,
  not the sharp completion capacity.

The review allocation was 100% analytical/source work and 0% numerical.

## 6. Dependencies and exact artifacts used

The following local artifacts were read and used:

- `protocol.md`;
- `state/proof_obligations.yml`, with the Round-135 target obligations
  checked;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/briefs/source_post_unmask_discovery_formula_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/primary_source_manifest.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/wright_bc_exact_source_card.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/blind_inverse_congruence_interface_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/candidates/conductor_degenerate_source_capacity.md`.

Primary sources used, and no secondary mathematical sources:

- Bettin and Chandee, *Trilinear forms with Kloosterman fractions*,
  arXiv:1502.00769v1, primary HTML
  <https://arxiv.org/html/1502.00769v1>.  Theorem 1, Remark 1, Corollary 1,
  and the proof of Corollary 1 were checked.
- Wright, *Trilinear Kloosterman fractions I: partially fixed moduli and
  unbalanced convolutions*, arXiv:2604.25177v2, primary HTML
  <https://arxiv.org/html/2604.25177v2>.  The definition preceding and the
  full statement of Theorem 2.1 were checked.
- arXiv:2601.00292 was retained solely as the withdrawn negative
  bibliographic control in the manifest and supplied no theorem.

No numerical experiment was used.

## 7. Recommended state effect

**revise.**  Revise the discovery proposition and its real-centre/completion
language exactly as listed in Section 5, then promote the corrected scoped
method obstruction: the literal direct, optimal-square, inverse-completion,
and fixed-determinant uses of the audited Bettin--Chandee/Wright sources do not
improve the accepted flat-row envelope and do not prove the quarter target.

Do not promote complete UNBAL, M9-M2, M9-M1, endpoint uniformity, M9, the
quarter theorem, or any global exponent improvement.  The corrected result
is a no-go for these source interfaces only; the signed flat packet and a
future coefficient-matrix or fixed-centre dispersion estimate remain open.
