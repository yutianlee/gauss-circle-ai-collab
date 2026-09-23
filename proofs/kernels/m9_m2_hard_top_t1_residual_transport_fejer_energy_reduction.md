# Kernel: residual transport obstruction and Fejer energy reduction

## Statement

Let \(J=\sqrt X\), \(y=\lfloor J\rfloor\),
\(q_X=X/y^2\), \(H=\lfloor yX^{-1/4}\rfloor\), and
\(1\ll L\ll H\leq J^{1/2}\).  For squarefree
\(N=2^{\nu_N}M_N\asymp L^2\), with \(M_N\) odd, retain every literal
profile, support, parity, floor, star, endpoint, and zero-extension
convention of the hard-TOP \(t=1\) scalar.

If the accepted Round-163 selector is absent, set \(\rho_N(d)=1\) for
every \(d\mid M_N\).  If it selects \(p_N,q_N\), set

\[
 \rho_N(d)=1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
 +2\mathbf1_{p_N\mid d}\mathbf1_{q_N\mid d}.
\tag{164.K1}
\]

Thus \(\rho_N\) retains exactly the neither/both incidences.  With

\[
 b_N^{\rm rem}=\sum_{d\mid M_N}\chi_4(d)\rho_N(d)A_N(d),
 \qquad
 c_N^{\rm rem}=\mathbf1_{N\in\mathcal I_L^{\rm lit}}
 \mu^2(N)\left(\frac{L^2}{N}\right)^{3/4}b_N^{\rm rem},
\tag{164.K2}
\]

the complete residual is

\[
 \mathcal S_{L,1}^{\rm rem}
 =\sum_Nc_N^{\rm rem}e(J\sqrt N).
\tag{164.K3}
\]

Four exact conclusions hold.

1. The residual character mass is

   \[
   \sum_{d\mid M_N}\chi_4(d)\rho_N(d)
   =\begin{cases}
   \displaystyle\prod_{r\mid M_N}(1+\chi_4(r)),&
        \text{no pair selected},\\[4pt]
   \displaystyle(1+\chi_4(p_Nq_N))
        \prod_{r\mid M_N,\ r\ne p_N,q_N}(1+\chi_4(r))=0,&
        \text{a pair selected},
   \end{cases}
   \tag{164.K4}
   \]

   where products are over odd prime divisors.  Selection gives ambient
   balance, but no-pair products with all primes \(1\pmod4\) have wholly
   positive mass \(2^{\omega(M_N)}\).

2. If the residual divisors are \(d_1<\cdots<d_r\), with
   \(\sigma_i=\chi_4(d_i)\), \(C_j=\sum_{i\leq j}\sigma_i\),
   \(C_0=0\), \(a_i=A_N(d_i)\), and \(a_0=a_{r+1}=0\), then

   \[
   b_N^{\rm rem}
   =C_ra_r+\sum_{j<r}C_j(a_j-a_{j+1})
   =-\sum_{j=0}^{r}C_j(a_{j+1}-a_j).
   \tag{164.K5}
   \]

   Consequently, for real amplitudes,

   \[
   \boxed{
   |b_N^{\rm rem}|\leq
   \frac12\bigl(\max_jC_j-\min_jC_j\bigr)
   \sum_{j=0}^{r}|a_{j+1}-a_j|.}
   \tag{164.K6}
   \]

   The literal profile has total variation \(O(1)\), including all hard
   faces.  Fixed-box four-prime controls, audited through the
   fixed-modulus theorem in
   `sources/bennett_martin_obryant_rechnitzer_2018.md`, have
   \(L^{2-o(1)}\) coefficient-uniform unit-profile capacity.  For the
   literal profile, direct BV/triangle control asks for the
   weighted sum \(\sum_N\operatorname{osc}(C_N)V_N\).  The unweighted
   sum is only the sharp coefficient-uniform envelope.  The four-prime
   controls show that sign balance, bounded variation, cemetery
   normalization, monotone transport, and the accepted positive product
   collar do not by themselves prove the target uniformly over that
   coefficient class.  This is not literal physical lower mass.

3. Let a consecutive interval of length \(M_L\asymp L^2\) contain the
   literal \(N\)-shell, extend \(c_N^{\rm rem}\) by zero, put
   \(z_N=c_N^{\rm rem}e(J\sqrt N)\), and take \(R=\lceil L\rceil\).
   Define

   \[
   \begin{aligned}
   \mathfrak E_R^{\rm rem}
   &:={1\over R}\sum_{s\in\mathbb Z}
       \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2\\
   &=\sum_N|c_N^{\rm rem}|^2
   +2\Re\sum_{1\leq r<R}\left(1-\frac rR\right)
     \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
     e\!\left(\frac{Jr}{\sqrt{N+r}+\sqrt N}\right).
   \end{aligned}
   \tag{164.K7}
   \]

   Counting the \(R-r\) windows containing a pair at gap \(r\), and then
   applying Cauchy to the exactly \(M_L+R-1\) possibly nonzero windows,
   gives

   \[
   \boxed{
   |\mathcal S_{L,1}^{\rm rem}|^2
   \leq\frac{M_L+R-1}{R}\mathfrak E_R^{\rm rem}.}
   \tag{164.K8}
   \]

4. The accepted coefficient energy, or directly the divisor bound, gives

   \[
   \sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon.
   \tag{164.K9}
   \]

   Therefore the residual target follows from the single one-sided,
   actual-direction theorem

   \[
   \boxed{
   \Re\sum_{1\leq r<R}\left(1-\frac rR\right)
     \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
     e\!\left(\frac{Jr}{\sqrt{N+r}+\sqrt N}\right)
   \leq C_\varepsilon L^2X^\varepsilon.}
   \tag{164.K10}
   \]

   Opening both literal coefficients on supported squarefree rows gives
   exactly \(N=dm\), \(N+r=d'm'\), and

   \[
   \boxed{d'm'-dm=r,\qquad1\leq r<R\asymp L,}
   \tag{164.K11}
   \]

   with both selectors, both parity branches, squarefreeness, profiles,
   and the square-root phase retained.  Equivalently, define every
   coefficient and selector to be zero off its literal row domain.  No
   absolute value may be inserted around an individual shift or divisor
   opening.  The scale \(R\asymp L\) is the first one for which the
   diagonal contribution in (164.K8) reaches the target square
   \(L^3X^\varepsilon\).

## Proof

Equation (164.K1) is the Boolean complement of XOR, so it subtracts the
Round-163 incidence sector exactly once.  Multiplicativity on the odd
divisor cube proves (164.K4).  In the selected case, writing
\(M_N=p_Nq_NR_N\) pairs \(a\mid R_N\) with \(p_Nq_Na\); their signs are
opposite because \(\chi_4(p_Nq_N)=-1\).  Their physical supports are
disjoint since \(p_Nq_N\geq15\), showing why the close XOR displacement
does not survive in the residual.

Telescoping proves (164.K5).  Since
\(\sum_{j=0}^{r}(a_{j+1}-a_j)=0\), subtract the midpoint of the range of
\(C_j\) before applying the triangle inequality; this proves (164.K6).
The fixed smooth profiles have bounded logarithmic derivative on a
fixed log-length interval, and the literal support has only finitely many
bounded hard jumps, so its total variation is \(O(1)\).  Four-prime
unit-profile controls have signs \(\{+,-,-\}\) in the three near-square
partitions.  With no selector their residual sum is \(-1\); with any
selected opposite-character pair, two partitions are XOR and the unique
neither/both partition is negative.  The fixed-modulus prime count gives
\(\gg L^2/(\log L)^4\) such diagnostic products.  This proves the stated
coefficient-uniform positive-route obstruction, with the literal-weight
and outer-phase quarantine.

For (164.K7), expand the sliding-window square.  A pair at positive gap
\(r<R\) occurs in exactly \(R-r\) windows.  Also

\[
 \sum_s\sum_{j=0}^{R-1}z_{s+j}=R\sum_Nz_N.
\]

At most \(M_L+R-1\) windows are nonzero, so Cauchy's inequality proves
(164.K8) without an endpoint error.  Equation (164.K9) follows from
\(|b_N^{\rm rem}|\leq\tau(M_N)\) on \(O(L^2)\) rows, or from the accepted
hard-TOP coefficient energy.  Combining (164.K7)--(164.K9) proves that
(164.K10) is sufficient.  Finally, literal divisor opening is
multiplicity one and turns \(N+r-N=r\) into (164.K11).

For completeness, the full-line regulated version of (164.K5) is

\[
 b_N^{\rm rem}
 =-\int_{\mathbb R}F_N(u)a'_{N,\rm sm}(u)\,du
 -\sum_\beta\left(
 F_N(\beta^-)\Delta^-_\beta a_N
 +F_N(\beta)\Delta^+_\beta a_N\right),
\tag{164.K12}
\]

where the compact zero extension is traversed over the whole line.  There
is no additional terminal term in this convention.  At a divisor lying on
a hard face, the incoming and outgoing increments are weighted by the
left and inclusive cumulative values respectively.

## Status and scope

Equations (164.K1), (164.K4)--(164.K9), and (164.K11)--(164.K12) are
proved internally.  Equation (164.K10) is open.  The terminal label is
`hard_top_t1_residual_transport_no_go`: positive within-product transport
is parked, while the complete residual remains viable through its exact
actual-coefficient short-shift energy.

Nothing here proves the residual target, the complete \(t=1\) face, the
other few-point channels, hard TOP, either smooth M2 packet, M9--M2,
M9--M1, endpoint uniformity, M9, the bridge, the quarter theorem, or a
better global exponent.
