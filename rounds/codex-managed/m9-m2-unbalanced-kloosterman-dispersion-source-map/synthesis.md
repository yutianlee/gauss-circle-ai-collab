# Round 135 synthesis: exact source maps exist, but none improves the flat-wave envelope

Campaign: `m9-m2-unbalanced-kloosterman-dispersion-source-map`

Starting graph SHA-256:
`f9aa6fa43900b9cb73f705405f9a6090e6e84fb5d3c8a9e037ffe3c6911b9ea0`

## Frozen objective and decision

Round 135 asked whether the exact flat-smooth prescribed-centre M2 UNBAL
wave

\[
 \mathscr R_{D,L}(X)=
 \sum_{r\asymp R,\ r\text{ odd}}\chi_4(r)W(X/(rD))
 \sum_{k\asymp K}\frac{q_L(4Xk/r^2)}k e(Xk/r)
\]

can be mapped to the Bettin--Chandee or Wright Kloosterman-fraction and
dispersion machinery while preserving the real centre, moving profiles,
character, absolute-value placement, and owners.

Close the round under `source_level_no_go`. Several exact maps exist, but
all are quantitatively worse than the known capacity or return that capacity
without a saving. No strict owner-complete smaller survivor is obtained.

## Real-centre and profile repair

Write

\[
 X=N_0+\xi,\qquad N_0=\lfloor X\rfloor,\qquad 0\le\xi<1.
\]

On (k=Ku,r=Rv),

\[
 e(\xi k/r)=e\!\left(\xi\Delta^{-1}u/v\right),
 \qquad \Delta=R/K=D/L.
\]

This factor has uniformly bounded normalized derivatives. Buffered
log-Fourier inversion separates it together with (q_L,W,1/k) at (O(1))
integrated projective cost. Every source phase may therefore use the
integer (N_0), while the fractional centre stays in arbitrary separated
coefficients. This makes direct Bettin--Chandee, direct Wright, the
(a=m^2) connector, and both completion orders legal for every real
(X). Claims that the moving profile or an irrational centre is by itself
fatal are rejected.

Each direct fibre has

\[
 \|\alpha\|_2=1,\qquad
 \|\beta\|_2\asymp R^{1/2},\qquad
 \|\nu\|_2\asymp K^{-1/2},
\]

with (\chi_4(r)) retained in (\beta_r).

## Direct and square-connector source capacity

Put

\[
 D=X^\delta,\quad L=X^\ell,\quad
 R=X^{1-\delta},\quad K=X^{1+\ell-2\delta},\quad
 u=\delta-\ell,\quad F=XK/R=X^{1-u}.
\]

The strict region has (1/4<u<1/2). The direct dictionary

\[
 a=k,\qquad m=1,\qquad n=r,\qquad \vartheta=N_0
\]

is exact. Bettin--Chandee gives

\[
 F^{1/2}\left(R^{11/10}K^{-3/20}+R\right)X^\varepsilon.
\]

Its two exponents exceed the absolute-capacity exponent (u) by more than
(3/10) and (1/4). Wright with its only owner-complete fixed factor
(R_0=1) gives

\[
 R^{11/8}F^{1/4}X^\varepsilon,
\]

whose exponent exceeds (u) by more than (5/16). The hypothesis
(R_0\ll M^C), with (M=1), forbids using the growing project modulus as
a helpful fixed factor.

Ordinary and inverse phases are not algebraically disjoint. On coprime
pairs,

\[
 m^2\overline m\equiv m\pmod r.
\]

Taking (a=j^2,j=m=k,n=r) gives an exact connector. The correlated
diagonal has the sharp decomposition

\[
 \mathbf1_{j=m}=\int_0^1e(t(j-m))\,dt,
 \quad \alpha_m=m^{-1/2}e(-tm),
 \quad \nu_{j^2}=j^{-1/2}e(tj),
\]

whose projective norm is (\asymp1), the nuclear norm of
(m^{-1}\mathbf1_{j=m}). The unavoidable inflation over the direct
(k^{-1}) vector is (K^{1/2}), not (K). At source lengths
((A,M,N)=(K^2,K,R)), however, both Bettin--Chandee terms and Wright's
dominant term still exceed (\Delta=X^u) by fixed powers.

## Completion: Ramanujan return versus rough Kloosterman matrix

The two completion orders are inequivalent.

After restoring all gcd strata (r=gn,k=gj), smooth-weight-first
completion has coefficients

\[
 |\widehat b_{g,n}(h)|
 \ll_B R^{-1}\left(1+\|h\|_n/\Delta\right)^{-B}.
\]

Inversion permutes the units, so the complete inverse-only sum is the
Ramanujan sum (\mathfrak c_n(N_0+h)). The exact gcd average gives

\[
 \boxed{|\mathscr R_{D,L}(X)|\ll_\varepsilon
 \Delta X^\varepsilon.}
\]

This is owner-complete, but it exactly returns the known absolute capacity.
A scalar Bettin--Chandee/Wright estimate on the completed blocks gives the
legal but redundant larger bound (\Delta R^{19/20+\varepsilon}).

If the sparse inverse selector is formed first and then Fourier-expanded in
the rough inverse variable, the exact form is

\[
 \sum_h\widehat g_r(h)S(N_0,h;r),\qquad
 \sum_h|\widehat g_r(h)|^2\ll(rK)^{-1}.
\]

The complete-frequency Kloosterman second moment yields the positive cost

\[
 R\sqrt\Delta X^\varepsilon
 =X^{1-(\delta+\ell)/2+\varepsilon},
\]

which is worse than (\Delta). The coefficient depends jointly on modulus
and Fourier frequency and is not an independent trilinear source tensor.

## Physical dispersion and determinant route

With (s=N_0+t), divisibility is exactly

\[
 r\mid s\quad\Longleftrightarrow\quad
 t\equiv-N_0\pmod r,
 \qquad |t-\xi|\ll\Delta X^\varepsilon.
\]

The shifted residue is therefore fixed and integral. Wright's dispersion
corollary still does not apply: coprimality is not uniform; (t) is not an
independent two-sequence convolution; the kernel is joint in ((r,t)); the
residue is too large for the short product scale; and the source sums
modulus-by-modulus absolute discrepancies after a principal subtraction,
whereas the project needs one outer absolute value after the signed
(\chi_4(r))-sum.

Bettin--Chandee Corollary 1 does have an exact dictionary. For
(\tau=N_0-dr\ne0),

\[
 (m_1,n_2,m_2,n_1)=(d,r,1,N_0),\qquad
 m_1n_2-m_2n_1=-\tau.
\]

At scales ((D,1,X,R)), its error per determinant is

\[
 X^{3/5+\varepsilon}R^{17/20}
 =X^{29/20-17\delta/20+\varepsilon},
\]

whose exponent is greater than (41/40). Its main term is
(O(X^\varepsilon)) per determinant and the
(O(\Delta X^\varepsilon)) effective levels merely return
(\Delta X^\varepsilon). The zero determinant is one divisor-bounded
level.

## Smallest survivor and full-proof status

The smallest owner-complete unresolved object remains the full flat-smooth
prescribed-centre signed wave, equivalently its fully gcd-restored
completion. No named published source estimates its joint coefficient
matrix below the accepted envelope

\[
 X^\varepsilon\min\!\left(\Delta,
 \sqrt{XL/D}+\sqrt{X/(LD)}\right),
\]

whose exponent is

\[
 \beta(u)=\min\!\left(u,\frac{1-u}{2}\right)>\frac14
 \quad(1/4<u<1/2).
\]

Round 135 closes the second standard M2 UNBAL surface tested after the
Round-134 positive-energy majorant no-go. A useful continuation must supply
a genuinely new (\chi_4)-signed coefficient-matrix or pointwise
fixed-centre theorem; another direct use of the same trilinear or dispersion
statements is parked.

The flat-smooth UNBAL quarter estimate remains open, as do the other UNBAL
owners, BAL, hard TOP, complete M9-M2, both direct M9-M1 parents, lower GAR,
endpoint uniformity, M9, and the unconditional quarter bridge. The internal
global exponent remains (1/3). The separately audited external Li--Yang
benchmark remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
\]

Round 135 proves no global exponent improvement.
