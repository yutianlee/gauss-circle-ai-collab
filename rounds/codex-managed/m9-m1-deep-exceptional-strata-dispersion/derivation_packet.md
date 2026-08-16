# Round 87 derivation packet: deep exceptional-strata dispersion

This packet is the complete mathematical statement for the
statement-only task. It does not assert the target estimate.

## 1. Frozen scales and residual object

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B={C\over T},\qquad J^{13/18}<C\leq J^{3/4}.
\]

For the three exact local classes,

\[
 (g,M,K)\in
 \{(1,4b,k),(2,2b,2[k\bar4]_b),(4,b,[k\bar4]_b)\},
 \qquad b\asymp B,
\]

so \(gM=4b\) and \(M\asymp B\). Let

\[
 D_1=\lfloor J^{87/140}\rfloor,
 \qquad E_*=\lfloor Q^2J^{-1/20}\rfloor,
 \qquad \Delta_b\asymp Q^2.
\]

For one fixed compatible smooth nonaxial principal component, define

\[
 A_{M,K,d}(n)=S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)
\]

and the exact deep survivor

\[
 \mathfrak Y_{\rm deep}
 ={1\over M^2}\sum_{b\asymp B}
 \sum_{D_1<|d|<\Delta_b-E_*}\sum_n
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}.             \tag{87.1}
\]

The target is

\[
 \mathfrak Y_{\rm deep}\ll_\varepsilon
 X^\varepsilon {J^2\over T}=X^\varepsilon J^{7/5}. \tag{87.2}
\]

Both signs, reflected orientations, nonzero modulus multiples,
arbitrary composite and prime-power moduli, all Ramanujan terms, and
the exact support intersection are part of (87.1). The prior small and
cubic shells, outer support collar, entry/exit terms, stationary errors,
wrong signs, exterior tails, raw Farey transitions, and axes are
separately owned and must not be reintroduced.

## 2. Accepted stationary and arithmetic interfaces

On one active sign band, \(|n|\asymp Q^2\),

\[
 I_b(n)=P_b(n)e(-\eta\lambda_b\sqrt{|n|}),
 \qquad
 \lambda_b=\sqrt X+{\sqrt{\kappa k}\over b}\asymp J,             \tag{87.3}
\]

with

\[
 \|P_b\|_\infty+\operatorname{Var}P_b
 \ll_\varepsilon X^\varepsilon H,
 \qquad H={C\sqrt T\over J}=BJ^{-1/10}.                           \tag{87.4}
\]

The exact periodic arithmetic identity is

\[
 {1\over M^2}\sum_{r\bmod M}|A_{M,K,d}(r)|\leq2                 \tag{87.5}
\]

for every integer \(d\) and every modulus.

Define the retained difference row

\[
 Z_b(d)={1\over M^2}\sum_n A_{M,K,d}(n)
 I_b(n+d)\overline{I_b(n)},                                      \tag{87.6}
\]

extended by zero outside the deep interval. A sufficient literal
Fejer/A-process off-diagonal input at difference length \(D\) and
shift height \(1\leq U\leq D\) is

\[
 \mathcal E_1(D,U)=
 \sum_{b\asymp B}\sum_{1\leq u<U}(U-u)
 \left|\sum_d Z_b(d+u)\overline{Z_b(d)}\right|                  \tag{87.7}
\]

with

\[
 \mathcal E_1(D,U)
 \ll_\varepsilon X^\varepsilon
 {U^2\over B(D+U)}J^{14/5}.                                     \tag{87.8}
\]

An outside-absolute signed estimate of equal or greater strength is
also admissible. The Fejer prefactor, diagonal, and weights \(U-u\)
are compulsory.

## 3. Exact four-Kloosterman completion

For \(h\not\equiv0\pmod M\), use

\[
 \mathcal C_{M,K}(a,h)=
 \sum_{\substack{y\bmod M\\(y(y+h),M)=1}}
 e_M\!\left(a(y+h)+K((y+h)^{-1}-y^{-1})\right).                 \tag{87.9}
\]

The completed correlation is exactly

\[
\begin{aligned}
 \mathfrak T_M(u,v;h_1,h_2)
 &=\sum_{a\bmod M}\mathcal C(a+u,h_1)
 \overline{\mathcal C(a,h_2)}e_M(-va)\\
 &=M\!\sum_{\substack{x\bmod M\\
 x,x-h_1,x-v,x-v-h_2\ \mathrm{units}}}
 e_M\!\left(ux+K\Phi_{h_1,h_2,v}(x)\right),                   \tag{87.10}\\
 \Phi_{h_1,h_2,v}(x)
 &=x^{-1}-(x-h_1)^{-1}-(x-v)^{-1}+(x-v-h_2)^{-1}.
\end{aligned}
\]

For an odd prime \(p\nmid K\), the reciprocal poles cancel locally
precisely on either of the branches

\[
 h_1\equiv h_2\equiv0\pmod p,
 \quad\hbox{or}\quad
 v\equiv0\pmod p,\ h_1\equiv h_2\pmod p.                       \tag{87.11}
\]

The full local phase is constant only when also \(u\equiv0\pmod p\).
Outside (87.11), a simple pole remains and the prime-field inner trace
has square-root size. This statement does not include a prime-power or
aggregate theorem.

On the paired branch,

\[
 \mathfrak T_M(u,0;h,h)
 =M\sum_{\substack{x\bmod M\\(x(x-h),M)=1}}e_M(ux).             \tag{87.12}
\]

Two exact hostile families are:

\[
 \mathfrak T_{p^\nu}(p^{\nu-1}\alpha,0;
 p^{\nu-1},p^{\nu-1})=-p^{2\nu-1},
 \qquad \nu\geq2,\quad p\nmid\alpha,                            \tag{87.13}
\]

and, for \(M=\ell R\), \((\ell,R)=1\), \(\ell\) a fixed odd prime,

\[
 \mathfrak T_{\ell R}(R,0;R,R)
 =\ell R\varphi(R)(-1-e_\ell(R)).                               \tag{87.14}
\]

For prime \(R\), (87.14) has size \(\asymp_\ell M^2\) even though
\(M\) is squarefree and \(u=M/\ell<M\). These are coefficientwise
no-go examples, not lower bounds for the full weighted aggregate.

## 4. Actual fourfold stationary weight

Opening the A-process off-diagonal produces the exact weight

\[
 \Omega_{b,d,u}(n,m)=
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m),                                      \tag{87.15}
\]

with phase, on a fixed compatible branch,

\[
 -\eta\lambda_b\bigl(
 \sqrt{|n+d+u|}-\sqrt{|n|}
 -\sqrt{|m+d|}+\sqrt{|m|}\bigr).                                \tag{87.16}
\]

The four-Kloosterman main, both Ramanujan cross terms, and the
Ramanujan-square term must be restored exactly once. Replacing
(87.15) by separated arbitrary coefficients or taking absolute values
before exceptional-stratum summation is not an admissible proof of
(87.2).

## 5. Frozen objective and exit gates

The round has one objective: determine whether the divisor-aligned and
prime-power exceptional strata exposed by (87.11)--(87.14) have a
target-safe aggregate against (87.15), or isolate them as a strictly
smaller exact signed survivor while proving a quantitatively sufficient
generic remainder.

A successful result must do at least one of the following:

1. prove (87.2);
2. prove the complete exceptional aggregate target-safe and state the
   exact generic residual correlation;
3. prove a nonempty new conductor/difference subrange;
4. give a rigorous actual-symbol obstruction or counterexample to the
   proposed decomposition, not merely to a coefficientwise surrogate.

Every result must audit all three classes, both signs, reflected
orientations, arbitrary prime powers and the 2-part, gcd strata,
Ramanujan cross/square terms, Fejer normalization, support and error
ownership, integer/perfect-power resonances, complete-transform
self-return, and downstream scope. No global exponent follows unless
the accepted graph is later closed through all remaining M1, M2,
uniformity, and assembly gates.
