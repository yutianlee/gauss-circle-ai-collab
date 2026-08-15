# Round 58 derivation packet: signed hyperbola-floor representation

This packet freezes the exact cross-\(h\) object left by Round 57.  It
asserts no Fourier saving.

## 1. High-shell object and target

Let \(Y=R^2\asymp\sqrt X\), and let
\(J=[A,B]\cap\mathbb Z\subset[cY,CY]\) have \(|J|\le R\).  Retain

\[
 P_J=\sum_{R/4<h\le R/2}\ \sum_{\substack{q\ \mathrm{odd}\\A\le hq\le B}}^{*}
 \chi_4(q)\mathcal A_X(h,q)e(\sqrt{Xhq}),
\tag{58.1}
\]

with the exact actual amplitude \(\mathcal A_X=\Omega_X^*\), all height
floors, profiles, the one-sided hard top, angular stars, and the independent
radial star.  The unweighted target is

\[
 |P_J|\ll_\varepsilon X^\varepsilon\sqrt R.
\tag{58.2}
\]

## 2. Exact endpoint variables

For fixed \(h\), define

\[
 a_h=\left\lceil {A\over h}\right\rceil,
 \qquad b_h=\left\lfloor {B\over h}\right\rfloor.
\tag{58.3}
\]

The exact number of odd denominators is

\[
 \nu_h=\max\left(0,
 \left\lfloor{b_h+1\over2}\right\rfloor-
 \left\lfloor{a_h\over2}\right\rfloor\right).
\tag{58.4}
\]

On the owned shell \(\nu_h\in\{0,1,2\}\).  Formula (58.4) is a count,
not yet the signed weighted row.  The task is to derive a floor-compatible
representation of (58.1), including the parity/character projector and
the dependence of \(\mathcal A_X(h,q)e(\sqrt{Xhq})\) on the selected
integer.

## 3. Candidate sawtooth route

One may write floor and interval indicators using the floor-compatible
sawtooth

\[
 \psi_F(t)=t-\lfloor t\rfloor-\frac12,
 \qquad \psi_F(n)=-\frac12.
\tag{58.5}
\]

A finite Vaaler expansion is allowed only with its explicit Fejer
residual and exact endpoint convention.  Determine:

1. the zero Fourier mode of the odd-character row;
2. the exact nonzero phase after combining a Fourier mode with
   \(e(\sqrt{Xhq})\);
3. whether summation in \(h\), in the endpoint variable, or a bilinear
   reorganization can save \(\sqrt R\);
4. the required truncation height and the total residual;
5. the effect of profile, floor, hard-top, and star jumps.

The exact selector may also be treated by a finite discrete Fourier
transform on each endpoint interval.  Any equivalent representation must
retain all zero/boundary terms.

## 4. Mandatory controls

- A point window has no adjacent pair and becomes a divisor incidence;
  the formula must reproduce it exactly.
- The Round-57 fourth-power family has \(\gg R\) unmatched absolute mass;
  a modewise absolute proof must fail on it.
- At \(X=K^4\), the radial expansion near \(K^2\) has integral or
  half-integral linear term; do not assume a first-derivative gap.
- Artificial window endpoints have full ownership.  Only inherited
  angular or radial equality points carry stars.
- The lower sector \((\log X)^B<h\le R/4\) is not owned.
- This is a physical estimate.  Alpha connectors and height limits remain
  separate even if (58.2) is proved.

No numerical experiment is required.  The round is 100% analytical.
