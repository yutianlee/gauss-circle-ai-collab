# Conductor candidate: uniform sampled-\(k\) rows and the short-shell ceiling

Campaign: `m9-m2-fixed-q-sampled-k-short-shell`

Starting graph SHA-256:
`d2502a33224fbcb1fe3b8ffe0ea1227b953112fa0c98216597e8b0ccfa887372`

## 1. Candidate theorem

For every literal residual row \(b=a+2q\), with

\[
 a\asymp b\asymp A,\qquad q\asymp D,\qquad
 K\asymp {JD\over A},\qquad G\asymp {L\over A},
\]

the complete actual coefficient should satisfy

\[
 \boxed{|F_a(q)|\ll_\varepsilon X^\varepsilon {L^2\over A}.}
 \tag{104.C1}
\]

Consequently

\[
 \sum_{a\asymp A}\sum_{q\asymp D}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon {DL^4\over A}.       \tag{104.C2}
\]

The theorem retains every actual owner and does not insert an arbitrary
coefficient.

## 2. Exact scaling

Rationalization gives

\[
 \delta_q^2
 ={2q^2\over a+q+\sqrt{a(a+2q)}},
 \qquad
 \Lambda_q
 ={Xq^2\over a+q+\sqrt{a(a+2q)}}
 \asymp {J^2D^2\over A}.                            \tag{104.C3}
\]

The exact open reciprocal interval is

\[
 I_{a,q}=\left({J\delta_q\over2\sqrt a},
                 {J\delta_q\over\sqrt{a+2q}}\right).
 \tag{104.C4}
\]

Its saddle \(u_k=(J\delta_q/(2k))^2\) moves monotonically from \(a\)
to \((a+2q)/4\). Empty, singleton and cone-edge intervals are handled by
zero extension.

The exact complete-integral scale is

\[
 V_D={J\delta_q\sqrt G\over K^{3/2}}
 \asymp\sqrt{AL\over JD}.                            \tag{104.C5}
\]

## 3. Complete actual sampled variation

After \(u=y^2\),

\[
 \mathfrak B^\circ_{a,q,k}(g)
 =\int q_{a,q,g}(y)
 e\!\left(gk\left(y-{J\delta_q\over2k}\right)^2\right)dy.
 \tag{104.C6}
\]

The literal amplitude is independent of \(k\), has the accepted
homogeneous profile seminorms, and includes both fixed physical collars.
The collar-to-stationary-width ratio is controlled by

\[
 gk\,(g\sqrt A)^{-2}\asymp {JD\over AL}\ge1.      \tag{104.C7}
\]

The same normalized complete-Fresnel proof as in the singleton case,
now rescaled by \(K\asymp JD/A\), should give

\[
 \sup_k|B_{a,q,g}(k)|+\operatorname {Var}_kB_{a,q,g}(k)
 \ll_\varepsilon X^\varepsilon V_D.                 \tag{104.C8}
\]

The proof uses no stationary leading-term truncation, so entry, exit and
incomplete-Fresnel transitions remain inside (104.C8).

## 4. Reciprocal curvature and metric modes

For every complete metric Fourier mode,

\[
 f_{\nu,g}(k)=\left(\nu-{g\over2}\right){\Lambda_q\over k},
 \qquad n=|2\nu-g|\ge1,                              \tag{104.C9}
\]

and

\[
 |f_{\nu,g}''(k)|\asymp {nA^2\over JD}.             \tag{104.C10}
\]

Weighted van der Corput with (104.C8) gives

\[
 \sum_kB_{a,q,g}(k)e(f_{\nu,g}(k))
 \ll_\varepsilon X^\varepsilon
 \left(\sqrt{ALn}+\sqrt{L/A}\,n^{-1/2}\right).      \tag{104.C11}
\]

The two Fourier moments are \(O(\sqrt G)\) and
\(O(G^{-1/2})\). Hence (104.C11) costs \(O(L+1)\) per lift and
\(O(G(L+1))=O(L^2/A)\) per row, proving (104.C1).

The cancellation of every \(D\)-power in (104.C11) is exact. It is a
rowwise scaling identity, not a saving across \(q\).

## 5. Exact Gram consequence

For \(1\le H\le D\), Cauchy and zero extension give

\[
 \mathcal G_H^{\rm act}
 \le H^2\sum_{a,q}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon {H^2DL^4\over A}.    \tag{104.C12}
\]

The canonical target is

\[
 X^\varepsilon {H^2L^4\over AD}.                    \tag{104.C13}
\]

Thus the coefficientwise sampled-\(k\) route has an exact factor
\(D^2\) gap on polynomial shells. For each fixed \(C\), it proves the
target uniformly on

\[
 D\le(\log X)^C,                                    \tag{104.C14}
\]

because \(D^2\) is absorbed into \(X^\varepsilon\). No polynomial
range follows without a signed \(q\)-correlation or an averaged row
theorem.

## 6. Owners and controls to adjudicate

For fixed \((a,q)\), primitivity, the square-ray owner and the
\(\rho\)-safe owner are independent of \(k\). Exact centers are removed
by the punctured metric window. Actual profiles, floors, stars, both
collars and saddle transitions remain inside the complete integral; the
remaining dyadic multiplier has bounded variation. These assertions must
be checked uniformly as \(b/a\) approaches either cone boundary.

Pell and fourth-power recurrences test coherence but do not make
\(n=|2\nu-g|\) vanish. An arbitrary phase-conjugated \(k\)-sequence can
destroy (104.C8), and absolute summation loses (104.C11). Both are false
analogues rather than covered cases.

## 7. Proposed state effect

If the two independent gates certify (104.C8) and the owner ledger,
promote a narrow uniform fixed-\(q\) row lemma and a fixed/polylogarithmic
ray-gap Gram subrange. Record the exact \(D^2\) ceiling of every purely
rowwise/Cauchy use. Retain the polynomial longer-row complete
mode-resolved Gram, canonical M2 energy, hard cone, smooth packets,
M9-M2, M9-M1, M9, endpoint uniformity, quarter target and global exponent
as open.
