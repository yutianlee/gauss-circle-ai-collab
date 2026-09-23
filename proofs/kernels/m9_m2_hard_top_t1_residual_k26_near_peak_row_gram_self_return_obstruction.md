# M9--M2 hard-TOP residual K26 near-peak row-Gram self-return obstruction

- Campaign: m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate
- Round: 180
- Role: conductor-selected durable proof kernel
- Starting graph: e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4
- Terminal label: row_gram_offdiagonal_capacity_or_self_return_no_go
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Exact setting and result

Put

\[
 e(t)=e^{2\pi i t},\qquad J=\sqrt X,\qquad
 1\ll L\ll H\le J^{1/2},\qquad R_0=\lceil L\rceil,
\]

and let \(M\asymp L^2\) be the exact cardinality of the containing
integer interval. Retain the complete real residual incidence
\(\lambda_N(d)\), including the selected/no-pair field, squarefree and
coprimality projectors, both two-adic branches, all profiles, floors,
stars, hard values, endpoints, transitions, support births and deaths,
and full-line zero extension. On literal support \(N=dm\asymp L^2\) and
\(d,m\asymp L\). The accepted ledgers are

\[
\begin{aligned}
 \Lambda_2
 &:=\sum_{\substack{d\ {\rm odd}\\m\ge1}}
 |\lambda_{dm}(d)|^2
 \ll_\varepsilon L^2X^\varepsilon,\\
 r_d&:=\#\{m:\lambda_{dm}(d)\ne0\}\ll L,\\
 c_N^{\rm rem}
 &:=\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\lambda_N(d),\\
 D_L&:=\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\end{aligned}
\tag{180.K1}
\]

The incidence bound and row length precede divisor recombination; \(D_L\)
is the separate accepted recombined energy. Define

\[
\begin{aligned}
 R_{\epsilon,d}(\theta)
 &=\sum_m(-1)^{\epsilon m}\lambda_{dm}(d)
 e(J\sqrt{dm}+dm\theta),\\
 Z_\epsilon(\theta)
 &=\sum_{d\ {\rm odd}}\chi_4(d)R_{\epsilon,d}(\theta)
 =\sum_N(-1)^{\epsilon N}c_N^{\rm rem}
 e(J\sqrt N+N\theta).
\end{aligned}
\tag{180.K2}
\]

For \(K=\lceil\sqrt L\rceil\) and \(|\nu|\le K\), put

\[
 I_\nu=
 \left[(\nu-1/2)/M,(\nu+1/2)/M\right)\pmod1
\tag{180.K3}
\]

and

\[
\begin{aligned}
 \mathcal G_\nu
 &:=\frac12\sum_{\epsilon=0}^1
 2\Re\sum_{\substack{d<d'\\d,d'\ {\rm odd}}}
 \chi_4(d)\chi_4(d')
 \int_{I_\nu}R_{\epsilon,d}
 \overline{R_{\epsilon,d'}},\\
 \mathcal D_\nu
 &:=\frac12\sum_{\epsilon=0}^1\sum_{d\ {\rm odd}}
 \int_{I_\nu}|R_{\epsilon,d}|^2,\\
 \mathcal E_\nu
 &:=\frac12\sum_{\epsilon=0}^1
 \int_{I_\nu}|Z_\epsilon|^2.
\end{aligned}
\tag{180.K4}
\]

Then exactly

\[
 \boxed{\mathcal E_\nu=\mathcal D_\nu+\mathcal G_\nu},
 \qquad
 0\le\mathcal D_\nu\ll_\varepsilon LX^\varepsilon.
\tag{180.K5}
\]

Consequently the one-sided estimates

\[
 \boxed{
 \mathcal G_\nu\ll_\varepsilon LX^\varepsilon
 \quad\Longleftrightarrow\quad
 \mathcal E_\nu\ll_\varepsilon LX^\varepsilon}
\tag{180.K6}
\]

are equivalent at target strength. The row-Gram split therefore
self-returns to the complete local scalar concentration problem.

The exact cross-row product-collision sector is target-safe:

\[
 \boxed{
 \mathcal P_\nu
 =\frac1M\sum_N
 \left\{(c_N^{\rm rem})^2-
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}\lambda_N(d)^2\right\},
 \qquad
 |\mathcal P_\nu|\ll_\varepsilon X^\varepsilon.}
\tag{180.K7}
\]

Thus the first open theorem is

\[
 \boxed{
 \mathcal U_\nu:=\mathcal G_\nu-\mathcal P_\nu
 \ll_\varepsilon LX^\varepsilon
 \quad\text{uniformly for }|\nu|\le K.}
\tag{180.K8}
\]

No estimate in (180.K8) is proved in this kernel.

## 2. Cell kernel, parity, diagonal, and collision proofs

For every integer \(h\), periodicity permits the real lift
\(\theta=(\nu+u)/M\), \(-1/2\le u<1/2\), and gives

\[
 \int_{I_\nu}e(h\theta)\,d\theta
 =
 \begin{cases}
 e(\nu h/M)\dfrac{\sin(\pi h/M)}{\pi h},&h\ne0,\\[6pt]
 M^{-1},&h=0.
 \end{cases}
\tag{180.K9}
\]

This includes wraparound and introduces no endpoint mass. Also

\[
 \frac12\sum_{\epsilon=0}^1(-1)^{\epsilon(m-m')}
 =\mathbf1_{m\equiv m'\pmod2}.
\tag{180.K10}
\]

Since \(d,d'\) are odd, this retains both odd--odd and squarefree
even--even products and removes only mixed parity.

Expanding \(|Z_\epsilon|^2\) after complete row recombination proves the
identity in (180.K5). Pointwise row Cauchy and the cell length \(1/M\)
give

\[
 \mathcal D_\nu
 \le\frac{\max_dr_d}{M}\Lambda_2
 \ll_\varepsilon LX^\varepsilon,
\tag{180.K11}
\]

which is the complete physical \(d=d'\) block, including unequal products
within a row. It is not a fixed diagonal after a dual transform.
Equation (180.K6) follows because
\(\mathcal G_\nu=\mathcal E_\nu-\mathcal D_\nu\le\mathcal E_\nu\),
while the opposite implication adds (180.K11). Moreover
\(\mathcal G_\nu\ge-\mathcal D_\nu\), so its negative side is already
target-safe.

At \(dm=d'm'=N\), both phases and the parity factor cancel and the kernel
is \(1/M\). Since the literal coefficients are real,

\[
 2\sum_{d<d'}\chi_4(d)\chi_4(d')
 \lambda_N(d)\lambda_N(d')
 =(c_N^{\rm rem})^2-\sum_d\lambda_N(d)^2.
\tag{180.K12}
\]

If \(t_N\) is the number of live odd-divisor incidences over \(N\), then

\[
 \left|(c_N^{\rm rem})^2-\sum_d\lambda_N(d)^2\right|
 \le(t_N-1)\sum_d|\lambda_N(d)|^2.
\tag{180.K13}
\]

The literal scale gives \(t_N\le\tau(N)\ll_\eta X^\eta\). Summing
(180.K13), dividing by \(M\asymp L^2\), and using \(\Lambda_2\) proves
(180.K7) after epsilon rebudgeting.

The retained unequal-product form is

\[
\begin{aligned}
 \mathcal U_\nu
 =2\Re\sum_{\substack{d<d'\\d,d'\ {\rm odd}}}
 \sum_{\substack{m\equiv m'\pmod2\\dm\ne d'm'}}
 &\chi_4(d)\chi_4(d')
 \lambda_{dm}(d)\lambda_{d'm'}(d')\\
 &\times e\!\left(
 J(\sqrt{dm}-\sqrt{d'm'})
 +\frac{\nu(dm-d'm')}{M}\right)\\
 &\times
 \frac{\sin(\pi(dm-d'm')/M)}
 {\pi(dm-d'm')}.
\end{aligned}
\tag{180.K14}
\]

Every surviving difference is even and lies strictly between \(-M\) and
\(M\). No selector, phase, collision complement, endpoint, transition,
hard value, or zero-extension field has been discarded.

## 3. Conditional Fejer and K26 connector

The near cells form the circular interval

\[
 U_K=\left[-(K+1/2)/M,(K+1/2)/M\right)\pmod1,
\tag{180.K15}
\]

and the Fejer kernel satisfies

\[
 F_M(\theta)\ll\frac{M}{1+\nu^2}
 \quad(\theta\in I_\nu),\qquad
 F_M(\theta)\ll\frac ML
 \quad(\theta\in U_K^c).
\tag{180.K16}
\]

If (180.K8) holds, then (180.K5)--(180.K7) give
\(\mathcal E_\nu\ll_\varepsilon LX^\varepsilon\) in every near cell.
Positivity after full recombination therefore gives

\[
 \frac12\sum_\epsilon\int_{U_K}F_M|Z_\epsilon|^2
 \ll_\varepsilon
 \sum_{|\nu|\le K}\frac{M}{1+\nu^2}LX^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
\tag{180.K17}
\]

On the far set, literal Parseval and \(D_L\), not incidence energy alone,
give

\[
 \frac12\sum_\epsilon\int_{U_K^c}F_M|Z_\epsilon|^2
 \ll\frac ML D_L
 \ll_\varepsilon L^3X^\varepsilon.
\tag{180.K18}
\]

Thus the complete physical endpoint energy

\[
 \mathfrak E_M^{(2)}
 :=\frac12\sum_\epsilon\int_0^1F_M|Z_\epsilon|^2
 \ll_\varepsilon L^3X^\varepsilon.
\tag{180.K19}
\]

Write \(Z_\epsilon=Z_{\epsilon,0}+Z_{\epsilon,*}\). The accepted
collective reverse-character bound is

\[
 A_0:=\sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\eta\frac{L^2}{J}X^\eta.
\tag{180.K20}
\]

Since \(F_M\le M\), \(M\asymp L^2\), and \(L^2\le J\), the complete
ordinary-zero-containing sector is

\[
 |\mathcal Z_M|
 \ll M(A_0D_L^{1/2}+A_0^2)
 \ll_\varepsilon L^3X^\varepsilon.
\tag{180.K21}
\]

Consequently (180.K19) implies

\[
 Q_M^*:=\frac12\sum_\epsilon
 \int_0^1F_M|Z_{\epsilon,*}|^2
 \ll_\varepsilon L^3X^\varepsilon.
\tag{180.K22}
\]

Finally, the accepted exact endpoint identity is

\[
 Q_M^*-Q_{R_0}^*
 =2(T_{26}+B_{\rm short})-\mathcal Z_{R_0,M},
\tag{180.K23}
\]

where \(Q_{R_0}^*\ge0\) and both
\(B_{\rm short}\) and \(\mathcal Z_{R_0,M}\) are
\(O_\varepsilon(L^3X^\varepsilon)\). Solving (180.K23) discards only
the favorable term \(-Q_{R_0}^*/2\), pays the short correction once, and
uses the exact terminal \(M\). Hence (180.K8) implies the one-sided K26
endpoint. This is a conditional connector, not a proof of (180.K8).

## 4. Coefficient-uniform capacity and false controls

Let \(S\le M\) be the number of supported product sites. Cauchy after
complete product recombination gives

\[
 \mathcal E_\nu\le\frac{S}{M}D_L
 \ll_\varepsilon L^2X^\varepsilon.
\tag{180.K24}
\]

This local coefficient-uniform scale is attained, up to harmless
\(X^\varepsilon\) factors, on incidence shadows with
\(A\asymp L^2\) atoms, \(O(L)\) atoms per row, and products in one
\(O(M)\)-diameter interval.

The complex dechirped shadow

\[
 \lambda_{dm}^{\rm cx}(d)=\chi_4(d)e(-J\sqrt{dm})
\tag{180.K25}
\]

aligns the rows on a central subarc of length \(c/M\), giving
\(\mathcal E_0\gg L^2\), \(\mathcal D_0\ll L\), and
\(\mathcal G_0\gg L^2\). It is deliberately complex and nonliteral.

For a real shadow, put \(\phi_{dm}=2\pi J\sqrt{dm}\) and

\[
 \lambda_{dm}^{(\alpha)}(d)
 =\chi_4(d)\cos(\phi_{dm}-\alpha).
\tag{180.K26}
\]

Averaging the squared cell norm over the one global phase \(\alpha\)
removes the cross term between an aligned product polynomial and a
twice-chirped polynomial. Some \(\alpha\) therefore has the same
\(L^2\) local order. An arbitrary-real-sign shadow follows by taking

\[
 \lambda_{dm}^{\rm sign}(d)
 =\chi_4(d)\operatorname{sgn}\cos(\phi_{dm}-\alpha)
\tag{180.K27}
\]

and choosing \(\alpha\) so that one real projection has size at least
\((2/\pi)A\).

On a smaller central subarc \(F_M\asymp M\), so all three shadows have
physical Fejer capacity \(L^4\). Replacing \(\chi_4\) by a constant or
erasing the selector leaves these controls after the chosen coefficients
absorb the row sign. An allowed no-pair row whose odd prime factors are
all \(1\bmod4\) has constant character \(+1\), which rules out a formal
rowwise mean-zero identity but supplies no density or lower mass.

Every attaining array in this section is nonliteral. These controls
exclude only coefficient-uniform closure by positivity, realness, parity,
character modulation, an erased selector, row length, hard rectangles,
or the rank-one central product collar. They neither prove nor disprove
(180.K8). A one-row or one-site array has zero off-row form, confirming
that capacity is not a universal lower bound.

## 5. Blind-scope reconciliation and no-repeat boundary

The statement-only finite packet omitted the literal product scale,
total-incidence, divisor-multiplicity, fixed-symbol, and recombined-energy
facts. Its counterexample with arbitrarily many divisor rows above one
arbitrarily large product is valid for that abstract packet but is not a
literal residual counterexample. Equations (180.K12)--(180.K13) show that
literal exact products are target-safe.

The blind proposed fiber-Bessel relation is also automatic after unmasking:

\[
 |c_N^{\rm rem}|^2
 \le t_N\sum_d|\lambda_N(d)|^2,\qquad
 t_N\ll_\eta X^\eta.
\tag{180.K28}
\]

It is not the missing theorem. The blind packet also lacked a full far-arc
bound; the accepted literal \(D_L\) supplies (180.K18). Its complex,
real-cosine, arbitrary-sign, and constant-character arrays remain valid
only as nonliteral false controls against feature-insensitive mechanisms.

Grouping (180.K14) by the nonzero product shift and then taking separate
absolute values returns to the unresolved shifted-correlation capacity.
Positive simultaneous dualization at the central cell returns to the
accepted rank-one product collar. Scalar scale Abel, Haar, martingale, and
positive endpoint closure return to \(L^4\). These are no-repeat controls,
not impossibility theorems for a new complete literal signed argument.

## 6. First open step and exact scope

The first open step remains (180.K8), equivalently (180.K14). It requires
one factor \(L\) of signed anti-concentration across distinct divisor rows
and unequal products, uniformly in every near-peak cell, before any row,
shift, mode, cell, divisor, or opening norm.

A future proof must use a relation absent from all false controls and stable
simultaneously under the selected/no-pair field, squarefree and coprimality
projectors, both two-adic and parity branches, profiles, hard endpoints,
support transitions, zero extension, the character pair, square-root and
cell-centre phases, the sinc kernel, and the single outer real part.

This kernel proves no literal lower mass and no estimate for (180.K8),
\(Q_M^*\), K26, the complete residual scalar, full \(t=1\), another
hard-TOP channel, complete hard TOP, BAL, UNBAL, M9--M2, either M1 route,
GAR, endpoint uniformity, M9, either bridge, the quarter theorem, or an
exponent.

## 7. Evidence and state boundary

The exact identities, product-collision estimate, conditional connector,
capacity controls, and blind-scope repair were independently checked in
the Round-180 reports and the row-identity/Fejer, literal-capacity, and
blind post-unmask reviews. No external theorem or numerical experiment is
used.

The durable state effect is one subordinate proved-internal obstruction:

M9-M2-hard-top-t1-residual-k26-near-peak-row-gram-self-return-obstruction.

It has no implication edge. The literal unequal-product theorem and every
downstream analytic or exponent owner remain open.
