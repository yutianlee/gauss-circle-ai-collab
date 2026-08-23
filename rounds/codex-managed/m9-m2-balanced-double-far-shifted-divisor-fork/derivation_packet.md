# Round 115 derivation packet

Campaign: m9-m2-balanced-double-far-shifted-divisor-fork

Starting graph SHA-256:
6eb6eb5941e6d4720294c6b0890356113700db3201cf7c19337b96fb5ed47155

## Accepted input

For one fixed persistent balanced block,

\[
 a_B^{<}(h,k)=\chi_4(h)
 \eta\!\left({(h,k)\over G_0}\right)A_B(h,k),
 \qquad G_0={\sqrt L\over2},
\]

and

\[
 Z_B(R)=2i\sum_{h,k}a_B^{<}(h,k)e(R\sqrt{hk}).
\]

The full-product diagonal and the two corridors

\[
 |h'k'-hk|\le L,\qquad |hk'-h'k|\le L
\]

have already been bounded absolutely within the \(L^3X^\varepsilon\)
energy budget. Hence the only supplied survivor is

\[
 E_{B,\rm df}
 =
 \sum_{|r|>L}\sum_n e\!\left(R(\sqrt n-\sqrt{n+r})\right)
 C_B(n,r),
\]

where

\[
 C_B(n,r)=
 \sum_{\substack{hk=n,\ h'k'=n+r\\|hk'-h'k|>L}}
 a_B^{<}(h,k)\overline{a_B^{<}(h',k')}.
\]

The desired conclusion is

\[
 |E_{B,\rm df}|\ll_\varepsilon L^3X^\varepsilon.
\]

## Exact charts to audit

The divisor chart should be derived, not presumed:

\[
 k={n\over h},\qquad k'={n+r\over h'},
\]

so that

\[
 hk'-h'k
 =
 {h(n+r)\over h'}-{h'n\over h}
 =
 {h^2(n+r)-h'^2n\over hh'}.
\]

The increment chart is

\[
 h'=h+p,\qquad k'=k+q,
\]

with

\[
 r=hq+kp+pq,\qquad
 \rho=hq-kp,
\]

and

\[
 r+\rho=q(2h+p),\qquad r-\rho=p(2k+q).
\]

Because nonzero coefficients require odd \(h,h'\), \(p\) is even and

\[
 \chi_4(h)\chi_4(h+p)=(-1)^{p/2}.
\]

This exact identity is a warning as well as a possible reduction: at
fixed \(p\), the character is a constant sign rather than oscillation in
\(h\).

## Capacity and forbidden substitutions

- The energy target is \(L^3\); the unrestricted pair capacity is \(L^4\).
- The outer phase depends only on \((n,r)\), so determinant separation
  supplies no oscillation within a fixed product fibre.
- A theorem for the complete divisor functions \(1*1\), \(1*\chi_4\), or
  \(\chi_4*\chi_4\) does not automatically apply to the truncated
  two-divisor correlation with a nonseparable slanted symbol and a
  determinant deletion.
- Removing the determinant gate by absolute values is allowed only if its
  cost and the restoration of the already owned corridor are explicit.
- No shellwise absolute value or cancellation between distinct physical
  blocks is permitted.
- Any zero mode or main term must be displayed before a spectral or
  dispersion remainder can be credited.

## Exit condition

Return one of: the full \(L^3\) estimate; a strict target-safe subrange and
smaller survivor; a positive-power actual-symbol saving; an exact
equal-capacity actual-symbol obstruction; or the first failed seam of the
tested noninvertible mechanism.
