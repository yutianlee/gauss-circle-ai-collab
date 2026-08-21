# Source Card: Popov 2024 local moments

## Bibliographic data

D. A. Popov, “Voronoi's formulae and the Gauss problem,” *Russian
Mathematical Surveys* 79:1 (2024), 53--126,
DOI `10.4213/rm10162e`.

Primary text: https://www.mathnet.ru/eng/rm10162

## Exact theorem used

Popov defines

\[
 E_k(T,H)=\frac1{2H}\int_{T-H}^{T+H}P(x)^k\,dx.
\]

Theorem 10(ii), equation (10.3), states uniformly for
\(H\le T/2\) that

\[
 E_2(T,H)\ll \sqrt T+\frac{T(\log T)^2}{H}.
\]

Equivalently,

\[
 \int_{T-H}^{T+H}|P(x)|^2\,dx
 \ll H\sqrt T+T(\log T)^2.
\]

Theorem 10(iii)--(iv) gives fourth and sixth local moments only for
\(H\ge T^{1/2}\).  Section 11 explicitly records that these available
local moments yield only the trivial pointwise exponent \(1/3+\varepsilon\).

## Exact project map

For a window \(H=T^\alpha\), the total second-moment exponent is
\(q=1\) throughout \(\alpha\le1/2\), because the additive
\(T(\log T)^2\) term dominates.  The exact persistence bridge

\[
 |P(T)|\ll Q^{1/3}+(Q/H)^{1/2}
\]

therefore gives exponent

\[
 \max\left\{\frac13,\frac{1-\alpha}{2}\right\}.
\]

It is exactly \(1/3\) for \(1/3\le\alpha\le1/2\), and worse for
\(\alpha<1/3\).  Thus the theorem is a valid uniform local input but does
not improve the project's accepted pointwise exponent.

## Scope and exclusions

This is a theorem for the fully assembled circle remainder \(P\).  It is
not an actual-coefficient M1/M2 rational-cluster estimate, does not remove
the additive \(T\)-scale error, and does not prove the quarter exponent.

## Audit status

Primary statement and normalization independently checked by the Codex
conductor on 2026-08-17.  Suitable as an external guardrail, not as a new
pointwise dependency.

