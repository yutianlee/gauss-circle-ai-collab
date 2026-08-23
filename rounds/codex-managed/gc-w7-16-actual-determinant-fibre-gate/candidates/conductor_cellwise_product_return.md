# Candidate addendum: cellwise numerator-Poisson product return

Campaign: gc-w7-16-actual-determinant-fibre-gate

Status: conductor diagnostic for audit; no proof-state effect.

## 1. Positive-frequency M1 cell

Fix one random frequency cell

\[
 I=[x,x+W^{-1})
\]

and one literal positive-frequency M1 block. Before reduced-ray grouping,
the cell sum has the form

\[
 S_{1,I}(c)=C_1\sum_{d}\chi_4(d)
 \sum_{h:\ h/d\in I}{F_1(h,d)\over h}e(ch/d),
\tag{117.P1}
\]

where (F_1) contains the fixed height, denominator and frequency
profiles, hard top, floors, and star. Formal finite Poisson in (h),
followed by (h=dy), gives

\[
 S_{1,I}(c)=C_1\sum_{d,m}\chi_4(d)
 \int_I {F_1(dy,d)\over y}e((c-md)y)\,dy
 +\mathcal B_{1,I}.
\tag{117.P2}
\]

The boundary package (mathcal B_{1,I}) must be made literal before
promotion. Regrouping (s=md) suggests the truncated product coefficient

\[
 B_1(s;y)=\sum_{d\mid s}\chi_4(d)F_1(dy,d).
\tag{117.P3}
\]

Without dyadic/profile truncation, (117.P3) is
(sum_{d\mid s}\chi_4(d)=r_2(s)/4), a nonnegative completion.

## 2. Positive-frequency M2 cell

For M2, the cell condition is (h/(4d)\in I), and the literal character
identity is

\[
 \chi_4(h)={e(h/4)-e(-h/4)\over2i}.
\tag{117.P4}
\]

Poisson in (h) and the change (h=4dy) turn the two branches into

\[
 c-(4m-1)d
 \quad\text{and}\quad
 c-(4m+1)d.
\]

The branch signs combine, up to one fixed global constant, into
(chi_4(r)) for odd (r). Thus the formal cell transform is

\[
 S_{2,I}(c)=C_2\sum_{d}\sum_{r\ {\rm odd}}\chi_4(r)
 \int_I {F_2(4dy,d)\over y}e((c-rd)y)\,dy
 +\mathcal B_{2,I},
\tag{117.P5}
\]

with truncated product coefficient

\[
 B_2(s;y)=\sum_{rd=s}\chi_4(r)F_2(4dy,d).
\tag{117.P6}
\]

On complete unweighted divisors, (117.P6) is the same (r_2(s)/4)
coefficient as (117.P3), by divisor symmetry.

## 3. Proposed interpretation

Equations (117.P2) and (117.P5), if made literal with all endpoint and
moving-symbol corrections, show that the M1 denominator character and M2
numerator high-pass are dual orientations of the same prescribed-centre
truncated divisor product wave. A second Poisson transform should return
the original cell sum. This would explain why the isolated character
high-pass need not give cancellation and why the full local-discrepancy
additive term reappears.

This is not yet a no-go theorem. The audit must determine:

1. the exact Poisson convention for hard endpoints and stars;
2. whether all boundary packages are target-safe in the random-cell norm;
3. the effect of dyadic (d,h) profiles and incomplete divisor ranges;
4. both frequency signs and the M1/M2 constants;
5. whether the product regrouping preserves the one-sided determinant
   target or only the full positive cluster form; and
6. whether any noninvertible cancellation survives in the actual truncated
   coefficients.

Only after those seams pass may the product return be recorded as a scoped
obstruction. It does not estimate the product wave.
