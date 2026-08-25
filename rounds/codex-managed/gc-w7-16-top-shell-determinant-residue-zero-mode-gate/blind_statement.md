# Statement-only packet: top-shell determinant-residue resonant mode

Campaign: gc-w7-16-top-shell-determinant-residue-zero-mode-gate

Starting graph SHA-256:
23e7bfacbf6abc5582769fbe8d427cbca2379e1d265b99df21d93a65ec504825

## Frozen scales and scalar

Let

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},
\]

and restrict to one literal top reduced-denominator shell \(B\asymp D\),
one moving-symbol stratum, one orientation, and one M1 or M2 sign sector.
Primitive outer rays \(r=(a,b)\) satisfy \(|a|\asymp L\), \(b\asymp D\).
The actual outer coefficients obey

\[
 \#\{r\}\ll LD,\qquad
 \sum_r |A_i(r)|^2\ll D/L,\qquad
 \sum_r|A_i(r)|\ll D.
\]

Before an outer or numerator triangle, the one-sided scalar is

\[
\begin{aligned}
 \mathfrak O_{i,D}^{+}
 ={}&\sum_{r=(a,b)}^{\rm lit}
 A_i(a,b)e\!\left({ca\over\kappa_i b}\right)
 \sum_p^{\rm lit}\sum_{\rho\mid a+p}
 \sum_{\eta\in\mathcal E_i}\sum_v^{*}
 \zeta_{i,\rho,\eta}(a+p)\,
 T_{i;r,p,\rho,D}(v)\\
 &\quad\times\sum_t c_{i,t}
 \sum_{g\le t/(\rho v)}^{*}
 {\chi_4(g)\over g}P_{i,a+p}(g)
 e\!\left(-{c(a+p)\over\kappa_i\rho v}
          +\vartheta_{i,\eta}\rho v\right).
\end{aligned}
\]

Here \(a'=a+p\), \(b'=\rho v\), \(\kappa_1=1\), \(\kappa_2=4\),
\(\mathcal E_1=\{+,-\}\), and \(\mathcal E_2=\{0\}\). The branch data are

\[
\begin{array}{c|c|c}
(i,\eta)&\vartheta_{i,\eta}&\zeta_{i,\rho,\eta}(a+p)\\ \hline
(1,+)&1/4&\mu(\rho)/(\pi(a+p))\\
(1,-)&-1/4&-\mu(\rho)/(\pi(a+p))\\
(2,0)&0&-4\mu(\rho)\epsilon_{\rm sgn}
\chi_4(|a+p|)/(\pi|a+p|).
\end{array}
\]

The coefficients \(c_{i,t}\) form the exact discrete Stieltjes
difference of the denominator profile and satisfy
\(\sum_t|c_{i,t}|\ll1\). The factors \(P\) and \(T\) retain every
frequency floor, star, determinant taper, threshold equality, support
entry or exit, sign, cell, and half-open owner.

After the Mobius pieces are physically reassembled, put

\[
 a'=a+p,\qquad b'=b+q,\qquad n=ab'-a'b=aq-bp.
\]

For fixed primitive \((a,b)\),

\[
 n\equiv-bp\pmod {|a|},\qquad
 b'={b(a+p)+n\over a}.
\]

On the physical top-shell \(p\)-support, a bounded union of intervals of
total span \(O(|a|)\), fixed \(n\) has \(O(1)\) admissible \(p\)-lifts.
This is a multiplicity statement, not a cancellation theorem.

For each fixed \((r,a')\), the already supplied inner estimate is
\(K_D/L\), where \(K_D=Y^{11/48+o(1)}\). The present outer triangle gives
\(DK_D=Y^{35/48+o(1)}\). The determinant target is \(D=Y^{1/2}\).

## Statement-only task

Without using any historical proof or strategy file:

1. Determine whether the exact induced weight can be separated into a
   factor periodic in \(n\) modulo \(4|a|\) and a bounded-variation
   envelope. State the weakest hypotheses under which that separation is
   legal and price all boundary terms.
2. Compute the physical resonant residue frequency, allowing the M1
   quarter carriers and M2 numerator character to shift the naive zero
   mode.
3. Decide whether the supplied algebra alone forces a complete
   quadratic-character or Salie-class sum. If it does, derive the exact
   modulus and completion cost. If it does not, identify the missing
   identity.
4. Test same-denominator and phase-aligned families. Distinguish a
   per-ray coherent mode from a family-summed outer-ray obstruction.
5. Prove a literal saving, give a support-matched countermodel, or state
   the sharp repaired theorem and first unavailable step.

No positive outer energy, arbitrary operator norm, random-sign model, or
coefficient-blind completion may replace the physical scalar. A
within-ray gain reaching \(Y^{9/16}\) changes no global exponent unless a
strict cross-ray gain is also proved.

The report must use the seven-section project contract and must not edit
shared proof state.
