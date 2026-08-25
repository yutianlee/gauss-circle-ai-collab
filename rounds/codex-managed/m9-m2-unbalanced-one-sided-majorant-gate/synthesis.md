# Round 134 synthesis: the optimal folded majorant exists but pays its entire bandwidth gain

Campaign: `m9-m2-unbalanced-one-sided-majorant-gate`

Starting graph SHA-256:
`40e83c20e83d542e43aa739931f4b89ea76f4541506fb44ef219ce31dca35024`

## Frozen objective

Round 134 tested the sole strategy-authorized untried move on the parked
M2 strict-UNBAL energy surface: a one-sided band-limited majorant applied
directly to the endpoint-complete full-character energy

$$
\mathcal E_\chi
=C_H\sum_n\left|\sum_{p\ {m odd}}\chi_4(p)
\sum_{a=0}^{H-1}b_{p,n+a}\right|^2.
\tag{134.1}
$$

The target remains

$$
\mathcal E_\chi\ll_\varepsilon X^{1/2+\varepsilon}.
\tag{134.2}
$$

## Exact extremal theorem

After forming

$$
A(k)=\sum_{p\ {m odd}}\chi_4(p)b_{p,k},
$$

Parseval writes (134.1) with multiplier

$$
F_H(\alpha)=|D_H(\alpha)|^2,
\qquad D_H(\alpha)=\sum_{a=0}^{H-1}e(a\alpha).
\tag{134.3}
$$

This is already a nonnegative trigonometric polynomial of degree
\(H-1\), integral \(H\), and height \(H^2\) at the origin.

The round proves the sharp finite extremal problem. For \(1\le N\le H\),
write \(H=mN+s\), \(0\le s<N\). Among all real degree-((N-1))
trigonometric polynomials satisfying \(T\ge F_H\), the least possible
zeroth coefficient is

$$
\boxed{
\mu_N(H)=(N-s)m^2+s(m+1)^2
=\frac{H^2}{N}+s\left(1-\frac{s}{N}\right).}
\tag{134.4}
$$

Root-of-unity quadrature gives the lower bound exactly. It is attained by

$$
\boxed{T^*_{H,N}=|mD_N+D_s|^2.}
\tag{134.5}
$$

The pointwise inequality is certified by the exact factorization

$$
|1-z|^2(T^*_{H,N}-F_H)
=|1-z^N|^2\sum_{a=0}^{m-1}(m-a)|1-z^{s+aN}|^2\ge0.
\tag{134.6}
$$

All three reports and all three post-unmask reviews agree on
(134.4)--(134.6), and the conductor reproduces the algebra independently.

## Endpoint-complete folded inequality

Let

$$
n_j=\begin{cases}m+1,&0\le j<s,\\m,&s\le j<N.\end{cases}
$$

For every finite complex sequence zero-extended before translation,

$$
\boxed{
\sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
\le
\sum_n\left|\sum_{j=0}^{N-1}n_jA(n+j)\right|^2.}
\tag{134.7}
$$

This is a genuine strict noninvertible contraction when \(N<H\). It is a
global inequality after summing every translate \(n\), not a pointwise
comparison of individual block squares. Zero extension makes it exact at
all entries and exits.

Its exact least \(L^1\) excess and Fourier coefficient mass are

$$
\mu_N(H)-H=Nm(m-1)+2ms,
\qquad
\sum_{|r|<N}|\widehat T^*_{H,N}(r)|=H^2.
\tag{134.8}
$$

Thus the round found a new finite lemma, not an endpoint estimate.

## Why it does not close \(E_\chi\)

The exact zeroth-mass factor is

$$
\rho(H,N)=\frac{\mu_N(H)}H\ge\frac HN.
\tag{134.9}
$$

The previous separate positive-row deficit is

$$
\Gamma_{\rm before}=\min(H,Q)>1.
$$

If shortening alone is asked to remove it, then
\(N\le H/\Gamma_{\rm before}\), so

$$
\Gamma_{\rm claimed}=1,qquad
\Gamma_{\rm zeroth\ survivor}=\rho(H,N)
\ge\Gamma_{\rm before}.
\tag{134.10}
$$

More generally, a fixed-power contraction \(N\le HX^{-\eta}\) forces a
fixed-power mass loss \(\rho(H,N)\ge X^\eta\). Taking the finite Fourier
lags in moduli uses (134.8) and restores the full factor \(H\).

This capacity result is deliberately scoped. The literal zeroth term is

$$
C_H\mu_N(H)\sum_k
\left|\sum_p\chi_4(p)b_{p,k}\right|^2,
\tag{134.11}
$$

not a positive separate-row diagonal. Cross-\(p\) and cross-lag terms may
cancel. Hence (134.9)--(134.10) obstruct universal diagonal,
positive-row, lag-count-only, and lagwise-absolute closures; they are not
lower bounds for the fixed literal array.

## Order, character, and Poisson seams

Universal quadratic-form domination is exactly pointwise multiplier
domination. Coefficientwise enlargement of a physical window or Fourier
kernel does not order a complex square. A universal rank-one internal
window majorant must be a scalar multiple of the original window and
cannot shorten it. Rowwise modulus or \(E_{\rm eq}\) loses the decisive
actual \(\chi_4\) cross terms.

The lawful folded comparison is applied after the full character sum, so
it retains every \(p,q\) cross term and every moving profile. It does not
itself exploit the character.

Exact character Poisson is also audited. Its factor \(i/2\), saddle,
Gaussian unit, and transported profiles combine to the principal row

$$
\mathcal R(k)=\frac1k\sum_{u>0\atop u\ {m odd}}
\chi_4(u)W\!\left(\frac{X}{Du}\right)
q_L\!\left(\frac{4Xk}{u^2}\right)e(Mk/u).
\tag{134.12}
$$

Substitution returns the reciprocal shifted actual-character Gram with
the same folded weights. It gives no independent power. Only the exact
Poisson integrals, or the principal Gram plus all
principal--remainder/remainder--remainder terms, are endpoint-complete.
No target-safe weighted remainder theorem is proved.

## Decision and full-proof status

Close Round 134 under `majorant_no_go` while promoting the sharp folded
majorant as a finite lemma and the exact bandwidth--mass tradeoff as a
scoped method obstruction. Reject the stronger and false claims that no
strict majorant exists, that coefficientwise majorization orders the
complex square, that the folded zeroth factor is a literal lower bound,
or that Poisson supplies a second saving.

The exact remaining actual-family theorem is the folded signed Gram bound

$$
C_H\sum_{|r|<N}t^*_{-r}
\sum_{p,q\ {m odd}}\chi_4(p)\chi_4(q)
\sum_k b_{p,k+r}\overline{b_{q,k}}
\ll_\varepsilon X^{1/2+\varepsilon},
\tag{134.13}
$$

for a fixed-power \(N\ll H\), with all moving profiles and endpoints.
This is not proved. The positive-energy majorant surface is therefore
parked under the one-round stop rule. The next strategy-authorized M2
UNBAL interface is the physical prescribed-centre truncated-divisor
wavelet with a genuinely modulus-aspect signed dispersion theorem.

The flat-smooth strict-UNBAL estimate and every other UNBAL owner remain
open. BAL, hard TOP, complete M9-M2, both direct M1 parents, the lower GAR
alternative, endpoint uniformity, M9, the bridge, and the quarter target
remain open. The internally proved global exponent remains \(1/3\). The
repaired external Li--Yang benchmark remains

$$
\frac{3292+25\sqrt{1717}}{13762}
=0.3144831759740614\ldots .
$$

Round 134 proves no global exponent improvement.
