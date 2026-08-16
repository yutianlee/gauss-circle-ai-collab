# Round 85 support-edge normalization review

Campaign: `m9-m1-large-dual-difference-joint-dispersion`

Starting graph SHA-256:
`942453c8d45068875932507e8ca84ed87bcb2187ee141029a27eb0c0642bf60f`

## Decision

The smooth-principal outer support-difference collar is target-safe.
The conductor promotes the explicit specialization

\[
 E_*:=\left\lfloor Q^2J^{-1/20}\right\rfloor
 =\lfloor J^{3/4}\rfloor,                              \tag{85.N1}
\]

rather than making graph syntax depend on an arbitrary derivative
order.  Thus, if \(\Delta_b\asymp Q^2\) is the diameter of the exact
stationary support for the fixed class and orientation, every

\[
 |d|\geq\Delta_b-E_*                                   \tag{85.N2}
\]

is target-safe.  The discovery and hostile reports prove the stronger
family \(E_\delta=Q^2J^{-\delta}\) for every fixed \(\delta>0\), with
the required cutoff derivative order depending on \(\delta\).

No whole-offset \(B\)-power or conductor interval is proved.

## Exact stationary split and global errors

For one class and orientation, write

\[
 I_b=P_b+E_b,
\]

where \(P_b\) is the full-Gaussian leading term containing the actual
compactly supported smooth principal cutoff \(V_b(c_{b,n})\), and
\(E_b\) contains entry/exit correction, stationary remainder, wrong
sign, and nonstationary tails.  With

\[
 H={C\sqrt T\over J}=B J^{-1/10},\qquad N=Q^2,
\]

the accepted smooth hierarchy gives

\[
 \|P_b\|_1\ll_\varepsilon X^\varepsilon HN,qquad
 \|E_b\|_1\ll_\varepsilon X^\varepsilon M,qquad M\asymp B.
                                                               \tag{85.N3}
\]

The second inequality is the Round-84 overlap count
\(HN/\sqrt{JQ}\asymp B\), together with fixed-order integration by
parts outside the enlarged stationary band.  Since
\(|A_{M,K,d}(n)|\leq2M^2\), all terms containing at least one \(E_b\),
summed over every integer difference, are

\[
 \ll_\varepsilon X^\varepsilon
 \sum_{b\asymp B}(\|P_b\|_1\|E_b\|_1+\|E_b\|_1^2)
 \ll_\varepsilon X^\varepsilon(B^2HN+B^3).             \tag{85.N4}
\]

At \(C=J^{3/4}\), these powers are \(J^{23/20}\) and
\(J^{9/20}\), both below \(J^{7/5}\).  The hostile report independently
rederives the same conclusion from the pointwise normalized remainder
\(J^{-4/5}\), obtaining \(J\) and \(J^{3/10}\).  Hence (85.N4) does
not reuse the Round-84 small-\(d\) aggregate outside its scope.

## Main-main edge calculation

Let \(\mathscr N_b=[N_b^-,N_b^+]\) be the active stationary support and
\(\Delta_b=N_b^+-N_b^-\).  For \(d>0\), write

\[
 s=\Delta_b-d.
\]

If \(0\leq s\leq E_\delta\) and both main factors are nonzero, their
saddles lie within \(O(Cs/N)\) of opposite endpoints of
\(\operatorname {supp}V_b\).  Compact \(C^\infty\) extension and the
normalized derivative hierarchy imply, for every fixed integer \(R\),

\[
 |P_b(n+d)P_b(n)|
 \ll_{R,\varepsilon}X^\varepsilon H^2
 \left({s+1\over N}\right)^{2R}.                       \tag{85.N5}
\]

The exact residue mass gives, on an interval of \(L\) integers,

\[
 \sum |A_{M,K,d}(n)|\ll ML+M^2.                        \tag{85.N6}
\]

Summing (85.N5)--(85.N6) over both signs, \(b\asymp B\), and
\(0\leq s\leq E_\delta\) gives

\[
 \mathfrak Y_{\mathrm{edge}}^{PP}
 \ll_{R,\varepsilon}X^\varepsilon H^2
 (BE_\delta+E_\delta^2)
 \left({E_\delta\over N}\right)^{2R}.                 \tag{85.N7}
\]

At the upper conductor, the two exponents are at most

\[
 {21\over20}-(2R+1)\delta,qquad
 {17\over10}-(2R+2)\delta.                              \tag{85.N8}
\]

For the promoted choice \(\delta=1/20\), take \(R=3\).  The larger
exponent in (85.N8) is \(13/10<7/5\).  Negative differences follow by
interchange, and the reflected orientation replaces the support by its
negative without changing its diameter.  If \(|d|>\Delta_b\), the
main-main term is zero.  Combining (85.N4) and (85.N7) proves (85.N2)
for the complete smooth-principal Fourier factor.

The derivative-free specialization \(R=0\),
\(E=J^{13/20}\), is independently target-safe by
\(H^2(E^2+BE)\ll J^{7/5}\).  It is a fallback if only the supremum
interface is retained.

## Physical/dual interface and no-go

For the continuously shifted physical rows \(\mathcal R_{b,x}(\theta)\),
the exact identity is

\[
 \mathcal G_b(\theta)
 ={1\over M^2}\sum_{d,n}A_{M,K,d}(n)
 I_b(n+d)\overline{I_b(n)}e(d\theta).                  \tag{85.N9}
\]

The accepted reciprocal estimate remains
\(|\mathcal R_{b,x}(\theta)|\ll X^\varepsilon TQ^{-5/24}\).
For a difference multiplier \(w\), Fourier projection and triangle
inequality therefore give only

\[
 X^\varepsilon\|K_w\|_1{C^3\over TQ^{5/12}},           \tag{85.N10}
\]

and \(\|K_w\|_1\geq1\) for any unit plateau.  Thus this exact
physical/dual identity preserves the earlier row saving but supplies no
\(B\)-power.  Complete projection is the physical-row self-return.

After the edge deletion, a literal \(d\)-A-process has a target-safe
diagonal.  Its first unsupported term is the weighted four-Kloosterman
off-diagonal recorded in the hostile report.  Prime-power nonzero modes,
nonzero modulus multiples, and exact square/fourth-power phases remain
inside it.

## Scope

The resulting exact smooth-principal survivor, with the explicit graph
choice (85.N1), is

\[
 {1\over M^2}\sum_{b\asymp B}
 \sum_{D_0<|d|<\Delta_b-E_*}\sum_n
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}.                 \tag{85.N11}
\]

Raw Round-81 transition error, axes, \(C>J^{3/4}\), cone edges, other
radial sectors, full `M9-M1`, `M9`, endpoint uniformity, and the global
exponent are unchanged.
