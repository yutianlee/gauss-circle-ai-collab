# Round 134 conductor adjudication: sharp folded majorant and capacity no-go

Campaign: `m9-m2-unbalanced-one-sided-majorant-gate`

Starting graph SHA-256:
`40e83c20e83d542e43aa739931f4b89ea76f4541506fb44ef219ce31dca35024`

## Decision

Promote the exact finite folded-majorant theorem and a separately scoped
bandwidth--mass obstruction. Close the proposed standalone one-sided
majorant route under `majorant_no_go`.

The wording matters. Round 134 does **not** show that no strict majorant
exists. It proves the opposite: there is an explicit optimal global
contraction from \(H\) shifts to \(N\) weighted shifts. The no-go is that
the contraction's exact squared weight mass pays at least the same factor
that a lag-count argument hopes to gain. The literal \(E_\chi\) target
remains open because a new signed actual-family theorem could conceivably
cancel that mass.

## Exact full-character multiplier

Form the actual character sum before any modulus,

$$
A(k)=\sum_{p>0\atop p\ {m odd}}\chi_4(p)b_{p,k}.
$$

Zero extension and Parseval give

$$
\mathcal E_\chi
=C_H\sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
=C_H\int_{\mathbb T}F_H(\alpha)|\widehat A(\alpha)|^2\,d\alpha,
\tag{134.R1}
$$

where

$$
F_H=|D_H|^2
=\sum_{|h|<H}(H-|h|)e(h\alpha),qquad
F_H(0)=H^2,qquad \widehat F_H(0)=H.
\tag{134.R2}
$$

Thus the exact Fejer multiplier is already nonnegative and band limited
to degree \(H-1\).

Universal domination of (134.R1) for every finite complex sequence is
equivalent to pointwise multiplier domination. The converse is obtained
by testing the quadratic form with translated normalized Dirichlet
kernels, whose squared moduli are approximate identities. Coefficientwise
order of a window or of Fourier coefficients is not this order.

## Sharp folded-majorant theorem

Let \(1\le N\le H\), write

$$
H=mN+s,qquad 0\le s<N,
$$

and define

$$
n_j=\begin{cases}m+1,&0\le j<s,\\m,&s\le j<N.\end{cases}
$$

Among all real trigonometric polynomials \(T\) of degree at most \(N-1\)
which satisfy \(T\ge F_H\), the exact least zeroth coefficient is

$$
\boxed{
\mu_N(H)=(N-s)m^2+s(m+1)^2
=Nm^2+(2m+1)s
=\frac{H^2}{N}+s\left(1-\frac{s}{N}\right).}
\tag{134.R3}
$$

Indeed exact root-of-unity quadrature and discrete Parseval give

$$
\widehat T(0)
=\frac1N\sum_{\nu=0}^{N-1}T(\nu/N)
\ge\frac1N\sum_{\nu=0}^{N-1}|D_H(\nu/N)|^2
=\sum_{j=0}^{N-1}n_j^2=\mu_N(H).
\tag{134.R4}
$$

The lower bound is attained by

$$
\boxed{T^*_{H,N}=|mD_N+D_s|^2
=\left|\sum_{j=0}^{N-1}n_je(j\alpha)\right|^2.}
\tag{134.R5}
$$

All three independent post-unmask reviews verify the pointwise
factorization. With \(z=e(\alpha)\),

$$
\boxed{
|1-z|^2(T^*_{H,N}-F_H)
=|1-z^N|^2\sum_{a=0}^{m-1}(m-a)|1-z^{s+aN}|^2\ge0.}
\tag{134.R6}
$$

Consequently, for every finite zero-extended complex \(A\),

$$
\boxed{
\sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
\le
\sum_n\left|\sum_{j=0}^{N-1}n_jA(n+j)\right|^2.}
\tag{134.R7}
$$

This is a global inequality after summing all translates \(n\). It is
not a pointwise inequality between individual block squares. It is exact
at every entry and exit because the sequence is zero-extended before
translation.

The exact minimal \(L^1\) excess and Fourier mass are

$$
\int_{\mathbb T}(T^*_{H,N}-F_H)
=\mu_N(H)-H=Nm(m-1)+2ms,
\tag{134.R8}
$$

$$
\sum_{|r|<N}|\widehat T^*_{H,N}(r)|
=T^*_{H,N}(0)=H^2,
\tag{134.R9}
$$

because all folded autocorrelation coefficients are nonnegative. The
endpoint cases are \(N=1\), giving the constant \(H^2\), and \(N=H\),
giving exactly \(F_H\).

## Exact capacity obstruction

Relative to the accepted separate-row diagonal normalization, the folded
zeroth mass has factor

$$
\rho(H,N)=\frac{\mu_N(H)}H\ge\frac HN.
\tag{134.R10}
$$

If shortening alone is chosen to remove

$$
\Gamma_{\rm before}=\min(H,Q),
$$

then one must take \(N\le H/\Gamma_{\rm before}\), and therefore

$$
\Gamma_{\rm claimed}=1,qquad
\Gamma_{\rm zeroth\ survivor}=\rho(H,N)
\ge\Gamma_{\rm before}.
\tag{134.R11}
$$

Likewise \(N\le HX^{-\eta}\) forces \(\rho(H,N)\ge X^\eta\). Taking
the folded lags in moduli uses (134.R9) and restores the full natural
factor \(H\). Hence the optimal majorant cannot yield a fixed-power
target gain through diagonal, positive-row, lag-count-only, or
natural-scale lagwise-absolute bookkeeping.

This is a method obstruction, not a lower bound for the literal array.
At \(r=0\), the actual majorized form contains

$$
C_H\mu_N(H)\sum_k
\left|\sum_p\chi_4(p)b_{p,k}\right|^2,
\tag{134.R12}
$$

not \(\rho(H,N)\mathcal D_0\). Cross-\(p\) and cross-lag cancellation
can change (134.R12). Proving enough cancellation is exactly the new
actual-family theorem still missing.

## Placement and Poisson adjudication

The hostile placement matrix is decisive:

- pointwise multiplier order after forming \(A\) is lawful;
- coefficientwise Fourier or physical-window order is false on complex
  cross terms;
- a universal rank-one internal-window majorant is only a scalar multiple
  of the original window and cannot shorten it;
- rowwise positivity, \(p\)-wise modulus, and \(E_{\rm eq}\) erase the
  actual character and retain \(\min(H,Q)\);
- a majorant of an outer nonnegative selector is lawful but does not
  change the internal Fejer bandwidth; and
- partial-arc or post-Poisson majorants require a prior lawful global
  quadratic-form order and a complete complement ledger.

The discovery Poisson normalization is independently verified. Exact
primitive character Poisson gives the factor \(i/2\). For positive odd
dual mode \(u\), the stationary point and main coefficient are

$$
x_*=\frac{4Mk}{u^2},\qquad
\phi(x_*)=\frac{Mk}{u},\qquad
I_u^{\rm main}(k)=2e(-1/8)(Mk)^{-1/4}
W\!\left(\frac{X}{Du}\right)
q_L\!\left(\frac{4Xk}{u^2}\right)e(Mk/u).
\tag{134.R13}
$$

The outside constants cancel to give the principal reciprocal row

$$
\mathcal R(k)=\frac1k\sum_{u>0\atop u\ {m odd}}
\chi_4(u)W\!\left(\frac{X}{Du}\right)
q_L\!\left(\frac{4Xk}{u^2}\right)e(Mk/u).
\tag{134.R14}
$$

Inserting (134.R14) into the folded form returns the shifted reciprocal
actual-character Gram with the same \(\mu_N(H)\) zeroth price. This is no
second saving. The principal Gram alone is not endpoint-complete: every
principal--remainder and remainder--remainder term, nonstationary sign,
entry, exit, and transition must remain in the exact remainder
\(\mathcal P_{T^*}\). No target-safe weighted remainder theorem is proved.

## Seam decisions

| Seam | Decision |
|---|---|
| Exact block square and Parseval | Green, endpoint-complete after zero extension. |
| Universal order type | Green only as pointwise multiplier / Toeplitz PSD order. |
| Exact extremal mass | Green, independently reproduced by root-of-unity quadrature. |
| Folded pointwise majorant | Green, independently reproduced by the sum-of-squares factorization. |
| Global folded physical inequality | Green; not a per-block pointwise inequality. |
| Fixed-power bandwidth with target-safe mass | Red; exact survivor is at least \(H/N\). |
| Coefficientwise and rowwise placements | Red; either false or character-erasing. |
| Actual \(\chi_4\) retention | Green only when the full \(p\)-sum is formed first. |
| Character Poisson normalization | Green as an exact identity. |
| Reciprocal principal row and Gram | Green as an interior principal module. |
| Weighted endpoint/remainder ledger | Open; principal Gram alone is incomplete. |
| Literal target | Open; no actual-family signed Gram estimate is proved. |
| Downstream scope | Green; flat-smooth strict-UNBAL only. |

## First remaining gap and route decision

For some fixed-power \(N\ll H\), the missing theorem is

$$
C_H\sum_{|r|<N}t^*_{-r}
\sum_{p,q\ {m odd}}\chi_4(p)\chi_4(q)
\sum_k b_{p,k+r}\overline{b_{q,k}}
\ll_\varepsilon X^{1/2+\varepsilon},
\tag{134.R15}
$$

with every literal moving profile and endpoint retained; equivalently one
must estimate the reciprocal principal Gram together with its full
weighted remainder. Equation (134.R15) is a genuinely new signed
actual-family inequality. The optimal majorant does not prove it.

The one-round stop rule therefore fires. Park the positive-energy
majorant surface. A future return requires a theorem that acts jointly on
(134.R15) before modulus and explicitly repays \(\rho(H,N)\), not another
universal majorant, coefficientwise window, or Poisson inversion.

The flat-smooth strict-UNBAL target remains open. All other UNBAL owners,
BAL, hard TOP, complete M9-M2, both direct M1 parents, the lower GAR
alternative, endpoint uniformity, M9, the bridge, and the quarter theorem
remain open. The internal global exponent remains \(1/3\); the repaired
external Li--Yang benchmark remains \(0.3144831759740614\ldots\).
