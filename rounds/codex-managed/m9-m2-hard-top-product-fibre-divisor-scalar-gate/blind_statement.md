# Statement-only packet: hard-TOP product-fibre divisor scalar

## Frozen problem

Let \(X\ge2\),

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=\frac{X}{y^2},\qquad H=\lfloor yX^{-1/4}\rfloor.
\tag{137.B1}
\]

Fix one literal polynomial intermediate hard-TOP block
\(1\ll L\ll H\). Let \(\eta_L\) be its half-open dyadic height profile,
\(\Phi\) the actual Vaaler taper, and \(W\) the actual real compact
endpoint profile. For odd positive \(h\), set

\[
 a_{\mathrm{end}}(h,m)
 =\eta_L(h)\Phi\!\left(\frac{h}{H+1}\right)
 \left(\frac{L^2}{hm}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xh}{4m}}\right),
\tag{137.B2}
\]

extended by zero outside

\[
 \lceil h/4\rceil\le m\le h.
\tag{137.B3}
\]

The exact hard-cone scalar is

\[
 \mathcal T_L
 =\sum_{\substack{h\ \mathrm{odd}}}\chi_4(h)
   \sum_{m=\lceil h/4\rceil}^{h}
   a_{\mathrm{end}}(h,m)e(J\sqrt{hm}).
\tag{137.B4}
\]

All half-open support, floors, zero extensions, endpoint values, and the
real-centre quantity \(q_X\) are literal.

## Already controlled square-entry sector

The entry projection \(1_{hm\text{ is a square}}\) is already proved
power-safe in the transposed energy:

\[
 \|A_L^{\square}c\|_2^2
 \ll_\varepsilon L^{3/2}X^\varepsilon
 \qquad(|c_h|\le1).
\tag{137.B5}
\]

Since there are \(O(L)\) active \(m\)-rows, Cauchy gives

\[
 |\mathcal T_L^{\square}|
 \ll_\varepsilon L^{5/4}X^\varepsilon,
\tag{137.B6}
\]

which is smaller than the scalar target. It is removed only through this
proved projection and norm triangle; no orthogonal energy split is assumed.
The frozen target is therefore

\[
 \boxed{
 |\mathcal T_L^{\mathrm{ns}}|
 \ll_\varepsilon L^{3/2}X^\varepsilon,}
\tag{137.B7}
\]

where \(hm\) is restricted to nonsquares.

## Exact product-fibre regrouping

Put \(n=hm\). The hard affine range is equivalent to

\[
 h\mid n,\qquad h\ \mathrm{odd},\qquad
 \sqrt n\le h\le2\sqrt n,qquad m=n/h.
\tag{137.B8}
\]

Define the literal truncated character-divisor coefficient

\[
 \begin{aligned}
 C_L(n):={}&
 \sum_{\substack{h\mid n,\ h\ \mathrm{odd}\\
                  \sqrt n\le h\le2\sqrt n}}
 \chi_4(h)\eta_L(h)
 \Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xh^2}{4n}}\right).
 \end{aligned}
\tag{137.B9}
\]

Then the nonsquare scalar is exactly

\[
 \boxed{
 \mathcal T_L^{\mathrm{ns}}
 =L^{3/2}
 \sum_{\substack{n\asymp L^2\\n\ne\square}}
 n^{-3/4}C_L(n)e(J\sqrt n),}
\tag{137.B10}
\]

with the actual support in (137.B9), not a softened interval. No product
fibre is averaged, completed, or replaced by its absolute value in this
identity.

The raw bounds \(|C_L(n)|\le\tau(n)\) and \(n\asymp L^2\) give
\(L^{2+o(1)}\) capacity, so (137.B7) requires a factor
\(L^{1/2-o(1)}\). The one-dimensional phase has

\[
 f'(n)=\frac{J}{2\sqrt n}\asymp\frac JL,qquad
 f''(n)=-\frac{J}{4n^{3/2}}\asymp-\frac{J}{L^3}.
\tag{137.B11}
\]

These derivatives alone do not authorize treating \(C_L(n)\) as a smooth
or arbitrary bounded coefficient.

## Required analysis and controls

Starting only from (137.B1)--(137.B11), prove (137.B7), reduce it to a
strictly smaller exact signed object, or identify the first exact
arithmetic, curvature, resonance, completion, circularity, or capacity
obstruction.

Any argument must retain the truncated near-square divisor range, the
actual \(\chi_4(h)\), all profiles and hard endpoints, the nonsquare
restriction, and uniformity for every real \(X\) and every polynomial
intermediate \(L\). Test at least:

- primes, prime powers, products with many near-square divisors, and the
  removed square products;
- the full odd-divisor identity
  \(\sum_{d\mid n}\chi_4(d)=r_2(n)/4\), without replacing the truncated
  coefficient by the full one;
- intervals where \(f'(n)\) is near an integer and the corresponding
  stationary dual modes;
- direct first/second derivative estimates, one-dimensional completion,
  Poisson/B-process return, and divisor switching;
- coefficient-uniform phase alignment versus the fixed literal
  coefficient;
- hard-face, support-crossing, floor, and real-centre ownership; and
- whether a proposed estimate is genuinely smaller or merely another form
  of the original hard cone or Gauss-circle discrepancy.

Close under exactly one label: `target_bound`,
`strict_product_fibre_reduction`, or `product_fibre_no_go`. This packet
concerns only the nonsquare polynomial intermediate hard-TOP scalar. It does
not include terminal, BAL, UNBAL, M9-M1, endpoint assembly, M9, or any
global-exponent conclusion.
