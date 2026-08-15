# 1. Result

The direct square-root-product bilinear form has a coefficient-preserving
two-dimensional Poisson return to the fixed-center product wavelet. This
uses information hidden by the Round-68 energy expansion, but it does not
yet prove the target.

More precisely, the \(k\)-Poisson transform and the modulo-four
\(q\)-Poisson transform produce dual integers \(m\) and odd \(n\). The
only nonnegligible dual cells satisfy

\[
 m,n\asymp J,\qquad |mn-X|\ll {J\over Q}X^\varepsilon.
\]

The leading scale is \(Q^{3/2}(mn)^{-1/4}\asymp Q^{3/2}J^{-1/2}\).
Consequently the desired \(Q^{3/2}\) direct bound is equivalent to the
same \(J^{1/2}=X^{1/4}\) signed short-product discrepancy isolated in
Rounds 64--65. Two-dimensional Poisson is therefore a lossless return
map, not the missing \(X^{1/20}\) saving at \(Q=X^{1/5}\).

# 2. Exact statement and hypotheses

Let \(J=\sqrt X\), let \(Q=X^{\nu/2}\) with fixed \(0<\nu<1/2\), and
put

\[
 \mathcal T_Q=\sum_{k\in\mathbb Z}\sum_{q\in\mathbb Z}
 \chi_4(q)\,\beta(k/Q)C(k/q)e(J\sqrt{kq}),
\tag{2.1}
\]

where \(\beta,C\) are fixed smooth functions whose combined support is
compactly contained in \(k,q>0\) and in a fixed positive ratio sector.
All square roots below are therefore positive. Define, for \(\theta\) in
the resulting compact dual ratio sector,

\[
 \mathcal K_\theta(\xi)
 =C(\theta/4)\int_0^\infty
 u^{1/2}\beta(u\sqrt\theta/2)e(-\xi u)\,du.
\tag{2.2}
\]

This is a uniformly Schwartz family in \(\xi\). The principal term of
the fixed-sector angular stationary expansion is

\[
 \mathcal T_Q
 =i e(-1/8)Q^{3/2}
 \sum_{\substack{m,n>0\\n\ \mathrm{odd}}}
 \chi_4(n)(mn)^{-1/4}
 \mathcal K_{n/m}\!\left(Q(\sqrt{mn}-J)\right)
 +\mathcal R_{\mathrm{sp}},
\tag{2.3}
\]

Here \(\mathcal R_{\mathrm{sp}}\) contains the lower stationary terms,
nonstationary cells, and transition pieces. Formula (2.3) identifies the
principal kernel and its normalization; it does **not** assert that the
single omitted remainder is \(O_A(Q^{-A})\). Such a conclusion would
require retaining and summing a sufficiently long uniform stationary
expansion. Equation (2.3) is a fixed smooth interior statement only; it
does not include sharp cone edges or the other radial sectors.

# 3. Proof or derivation

With \(\widehat f(\xi)=\int f(x)e(-x\xi)\,dx\), ordinary Poisson in
\(k\) and character Poisson in \(q\) give

\[
 \sum_{q\in\mathbb Z}\chi_4(q)f(q)
 ={i\over2}\sum_{n\in\mathbb Z}\chi_4(n)
 \widehat f(n/4),
\tag{3.1}
\]

because

\[
 \sum_{a\bmod4}\chi_4(a)e(an/4)=2i\chi_4(n).
\]

Hence

\[
 \mathcal T_Q={i\over2}\sum_{m,n}\chi_4(n)I_{m,n},
\tag{3.2}
\]

\[
 I_{m,n}=\iint\beta(x/Q)C(x/y)
 e\!\left(J\sqrt{xy}-mx-{n\over4}y\right)dx\,dy.
\tag{3.3}
\]

Use the exact product-ratio coordinates

\[
 x={Qu\over v},\qquad y=Quv,\qquad
 dx\,dy={2Q^2u\over v}\,du\,dv.
\tag{3.4}
\]

The phase becomes

\[
 Qu\phi_{m,n}(v),\qquad
 \phi_{m,n}(v)=J-{m\over v}-{n v\over4}.
\tag{3.5}
\]

An interior angular saddle exists only for \(m,n>0\), and then

\[
 v_0=2\sqrt{m/n},\qquad
 \phi_{m,n}(v_0)=J-\sqrt{mn},
\tag{3.6}
\]

\[
 \phi_{m,n}''(v_0)=-{n^{3/2}\over4m^{1/2}},qquad
 v_0|\phi_{m,n}''(v_0)|^{1/2}=(mn)^{1/4}.
\tag{3.7}
\]

The fixed ratio support forces \(m,n\asymp J\). One-dimensional
stationary phase in \(v\) contributes \(e(-1/8)\) and

\[
 \begin{aligned}
 I_{m,n}^{\rm stat}
 &=2e(-1/8)Q^{3/2}(mn)^{-1/4}C(n/(4m))\\
 &\quad\times\int_0^\infty u^{1/2}
 \beta(u\sqrt{n/m}/2)
 e\!\left(-Q(\sqrt{mn}-J)u\right)du,
 \end{aligned}
\tag{3.8}
\]

which is exactly the principal summand in (2.3) after multiplication by
the prefactor \(i/2\) in (3.2).

The homogeneous phase has a one-dimensional critical manifold when
\(mn=X\). If \(mn\ne X\), the remaining radial integral is a Schwartz
Fourier transform. Thus

\[
 Q|\sqrt{mn}-J|\ll X^\varepsilon
 \quad\Longleftrightarrow\quad
 |mn-X|\ll {J\over Q}X^\varepsilon
\tag{3.9}
\]

is the complete principal stationary range. Integrating in \(u\) first may appear
to expose additional roots of \(\phi_{m,n}(v)=0\), but those are not
full critical points: since the \(u\)-support stays away from zero, every
polynomial moment of the resulting Fourier kernel vanishes, and
nonstationary integration in \(v\) removes them to arbitrary order.

Let \(T=J/Q\). Removing the harmless factor
\((mn)^{-1/4}\asymp J^{-1/2}\), (2.3) asks for

\[
 \sum_{\substack{m,n\asymp J\\n\ \mathrm{odd}}}
 \chi_4(n)\mathcal W_{m,n}
 \mathcal K_{n/m}\!\left(Q(\sqrt{mn}-J)\right)
 \ll J^{1/2}X^\varepsilon,
\tag{3.10}
\]

where \(\mathcal W_{m,n}\) is a fixed smooth ratio symbol. This is a
signed character-divisor incidence in the window \(|mn-X|\ll T\), the
same fixed-center product-wavelet scale as the accepted Round-64
reduction.

# 4. First doubtful or unproved step

The first arithmetic inequality left unproved is (3.10). Absolute divisor grouping gives
only

\[
 \sum_{|r|\ll T}\tau(X+r)\ll TX^\varepsilon
 ={J\over Q}X^\varepsilon.
\tag{4.1}
\]

Relative to the required \(J^{1/2}\), the exact missing factor is

\[
 {J^{1/2}\over Q}.
\tag{4.2}
\]

At \(Q=X^{1/5}\), this is \(X^{1/20}\), exactly the prior \(H/L\)
deficit. Expanding the divisor incidence in (3.10) reconstructs (2.1),
so neither product grouping nor a second Poisson transform proves the
bound. New signed cancellation across distinct nearby products is still
required. For the literal two-dimensional expansion, uniform summation
of the lower stationary, nonstationary, and transition terms in
\(\mathcal R_{\mathrm{sp}}\) is a separate analytic seam; it is not
needed by the exact accepted inverse-transform plus \(k\)-Poisson return
used in the blind derivation.

# 5. Required control test and outcome

- **Direct normalization:** passed. Equation (69.6) in the packet turns
  the \(Q^{3/2}\) estimate into the required \(J^{1/2}\) bound.
- **Character transform:** passed. The Gauss sum is \(2i\), the dual
  frequency is \(n/4\), and the dual character remains \(\chi_4(n)\).
- **Product/radial coordinates:** passed with Jacobian
  \(2Q^2u/v\).
- **Stationary geometry:** passed. The full stationary condition is
  \(mn=X\); near stationarity has width \(T=J/Q\).
- **Amplitude:** passed. The angular stationary factor and Jacobian give
  exactly \(2Q^{3/2}(mn)^{-1/4}\) before the character-Poisson factor.
- **False interior-root control:** passed. Roots with
  \(\phi=0\), \(\phi'\ne0\) vanish by nonstationary/moment cancellation
  and are not extra main terms.
- **Exact products:** target-safe. The fibre \(mn=X\) has only
  \(O_\varepsilon(X^\varepsilon)\) representations.
- **Absolute capacity:** fails by exactly \(J^{1/2}/Q\); no exponent is
  gained.
- **Remainder scope:** the principal kernel is audited; a one-term
  stationary expansion is not promoted as having an arbitrarily small
  aggregate remainder.
- **Scope:** sharp ratio edges, all Mellin modes, and other radial blocks
  are not promoted here.

No numerical experiment was used.

# 6. Dependencies and exact artifacts used

- `rounds/codex-managed/m9-m1-direct-square-root-product-bilinear/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/actual_symbol_addendum.md`;
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/reviews/conductor_offdiagonal_adjudication.md`;
- accepted graph nodes
  `M9-M1-reciprocal-product-wavelet-reduction` and
  `M9-M1-square-root-product-energy-involution`.

No external theorem is imported. Poisson, the Gauss sum, the coordinate
change, and the stationary constants were rederived locally.

# 7. Recommended state effect

Promote only the principal fixed-interior two-dimensional
Poisson/product-wavelet return geometry and normalization, together with
the exact accepted inverse-transform plus \(k\)-Poisson return after
independent seam review. Retain the aggregate two-dimensional remainder,
the direct \(Q^{3/2}\) estimate, the signed near-product discrepancy,
PSC, GAR, M9-M1, M9, and the exponent open. Future work must act on the
signed short-product coefficient itself; another product grouping,
two-dimensional Poisson transform, or energy Cauchy step is circular.
