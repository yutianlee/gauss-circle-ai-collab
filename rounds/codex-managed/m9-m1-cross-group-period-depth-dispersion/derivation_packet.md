# Round 88 derivation packet: cross-group period-depth dispersion

This packet is the complete mathematical statement for the
statement-only task.  It does not assert the target estimate.

## 1. Frozen scales and prior deletions

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B=C/T,\qquad J^{13/18}<C\le J^{3/4}.
\]

For the three exact classes,

\[
 (g,M,K)\in
 \{(1,4b,k),(2,2b,2[k\bar4]_b),(4,b,[k\bar4]_b)\},
 \qquad b\asymp B,\qquad M\asymp B.
\]

Let

\[
 D_1=\lfloor J^{87/140}\rfloor,\qquad
 E_*=\lfloor Q^2J^{-1/20}\rfloor,\qquad
 D_1<|d|<\Delta_b-E_*,\qquad \Delta_b\asymp Q^2.
\]

The literal dual zero, every \(0<|d|\le D_1\), and the complete outer
support collar are already owned.  Entry/exit, stationary errors,
wrong signs, raw Farey transitions, axes, and exterior tails are
separately owned.

## 2. Normalized physical rows and group decomposition

For a unit \(x\bmod M\), define the normalized physical row

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_n I_b(n)e_M(nx)e(n\theta),
 \qquad
 \sup_{x,\theta}|\mathcal R_{b,x}(\theta)|
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.            \tag{88.1}
\]

For \(P=(x,y)\), \(x\ne y\), put

\[
 F_{b,P}(\theta)=e_M(K(\bar x-\bar y))
 \mathcal R_{b,x}(\theta)\overline{\mathcal R_{b,y}(\theta)}.
                                                               \tag{88.2}
\]

The \(d\)-th Fourier coefficient of (88.2) already contains the exact
external factor \(M^{-2}\).  No further \(M^{-2}\) may be inserted.

Factor \(M=\prod_{q\Vert M}q\) into full prime-power factors.  Every
ordered pair has the unique nonempty active set

\[
 S(P)=\{q:x_q\ne y_q\pmod q\}                                  \tag{88.3}
\]

and active local-pair label \(\alpha(P)\).  Sum inactive diagonal units
into \(H_{b,S,\alpha}=\Pi_{b,D}\sum_zF_{b,P(\alpha,z)}\), where
\(\Pi_{b,D}\) is the exact signed deep Fourier projection and

\[
 \|\Pi_{b,D}f\|_\infty\ll \log(2+J)\|f\|_\infty.                \tag{88.4}
\]

The full projected row is

\[
 G_{b,D}=\sum_{S,\alpha}H_{b,S,\alpha}.                        \tag{88.5}
\]

## 3. Accepted Round-87 deletion and exact survivor

Let \(D_U(\theta)=\sum_{j=0}^{U-1}e(j\theta)\).  Round 87 proves

\[
\begin{aligned}
 \mathcal P_{\rm same}(D,U)
 &=\sum_{b\asymp B}\int_{\mathbb T}|D_U(\theta)|^2
   \sum_{S,\alpha}|H_{b,S,\alpha}(\theta)|^2\,d\theta\\
 &\ll_\varepsilon X^\varepsilon UB^3T^4Q^{-5/6}.              \tag{88.6}
\end{aligned}
\]

With \(U=D\),

\[
 \mathcal P_{\rm same}(D,D)
 \ll_\varepsilon X^\varepsilon {D\over B}J^{14/5},             \tag{88.7}
\]

with \(J^{-2/15}\) slack.  This includes every mixture of the
full-prime-power local-zero and paired branches, all same-group
stride-\(M\) returns, arbitrary prime powers, the full \(2\)-part, all
three classes, and the actual fourfold stationary symbol.

The accepted global \(u=0\) A-process diagonal remains owned once.  The
strict survivor is the cross-group off-diagonal

\[
\boxed{
 \mathcal G_{\rm cross}(D)
 =\sum_{b\asymp B}\int_{\mathbb T}|D_D(\theta)|^2
 \sum_{\substack{(S,\alpha)\ne(S',\alpha')\\u\ne0}}
 H_{b,S,\alpha}(\theta)
 \overline{H_{b,S',\alpha'}(\theta)}\,d\theta .}                \tag{88.8}
\]

The notation \(u\ne0\) means that the zero Fourier shift is excluded
after expanding the Fejer kernel; it is not an extra pointwise
multiplier inside the integral.

The frozen target is

\[
 \mathcal G_{\rm cross}(D)
 \ll_\varepsilon X^\varepsilon {D\over B}J^{14/5},             \tag{88.9}
\]

or an exact further decomposition with a target-safe nonempty part.

## 4. Local completed phase and period depth

The exact completed local phase is

\[
\begin{aligned}
 \mathfrak T_M(u,v;h_1,h_2)
 &=M\!\sum_{\substack{x\bmod M\\
 x,x-h_1,x-v,x-v-h_2\ {\rm units}}}
 e_M\!\left(ux+K\Phi_{h_1,h_2,v}(x)\right),\\
 \Phi_{h_1,h_2,v}(x)
 &=x^{-1}-(x-h_1)^{-1}-(x-v)^{-1}
 +(x-v-h_2)^{-1}.                                      \tag{88.10}
\end{aligned}
\]

Writing \(A=h_1\), \(B_2=h_2\), and \(V=v\), the numerator of the
reciprocal part over its common denominator is

\[
 N_{A,B_2,V}(x)
 =(B_2-A)x^2+2AVx-AV(V+B_2).                           \tag{88.11}
\]

For \(q=p^\nu\Vert M\), the residual may have:

1. a full-period mismatch with an uncancelled local pole;
2. a partial period \(p^{\nu-j}\), \(0<j<\nu\), descending to modulus
   \(p^{\nu-j}\) and supported on shifts \(p^j\mid u\);
3. a bad-prime or nonunit-\(K\) degeneration;
4. an additional \(2\)-adic unit-domain period.

These descriptions are a routing taxonomy, not an accepted estimate.
Any claimed period-depth formula must include the unit-domain indicator
and be proved at the full prime-power level.

## 5. Frozen objective and exit gates

The round has one objective: prove (88.9), prove a target-safe
partial-period or aperiodic subaggregate and isolate a strictly smaller
exact survivor, or give a rigorous actual-symbol no-go.

Every candidate must:

- retain the normalized rows and all powers of \(M,B,Q,T,D\);
- keep \(U=D\), the Fejer weights, and the global \(u=0\) diagonal
  ownership;
- distinguish same-group terms already removed from cross-group terms;
- prove rather than assume the full prime-power period-depth and
  \(2\)-adic classifications;
- use the actual fourfold stationary symbol before absolute values;
- retain Ramanujan centering, both signs, reflected orientations,
  modulus-multiple differences, support endpoints, and perfect powers;
- audit complete-transform self-return and literal current source
  hypotheses;
- make no claim for \(C>J^{3/4}\), transitions, axes, cone edges, other
  radial sectors, full M9-M1, M9-M2, M9, endpoint uniformity, R5-Full,
  or the global exponent.

