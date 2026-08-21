# Conductor Round 113 dictionary and normalization review

## Decision

The repaired Round-113 dictionary is a proved coefficientwise connector.
The original candidate is not promoted verbatim: its discrete coefficient
was not yet a typed continuum symbol, its (d=0) notation multiplied a
zero cutoff by an undefined phase, and its low-gcd formula was not the full
physical one-count equation. The repairs below close those seams without
changing any positive-integer coefficient.

## Exact finite profiles

Let (R=\sqrt X), (y=\lfloor R\rfloor),
(D_j=2^{-j}y), and use

\[
 \eta(t)=q(2(t-1)),\qquad W(t)=\eta(t)-\eta(2t),
\]

with (W\in C_c^\infty((0,\infty))),
(\operatorname{supp}W\subset[1/2,3/2]), and (W(1)=1). The denominator
partition telescopes exactly on (1\le d\le y). Only (j=0) meets the
hard upper cutoff; every (j\ge1) is the unrestricted smooth rescaling
(W(d/D_j)) on the integers.

For (H=\lfloor DX^{-1/4}\rfloor) and (L_r=2^{-r}H), the frequency
partition telescopes exactly on (1\le h\le H). Only (r=0) is clipped;
every (r\ge1) is the unrestricted integer profile (W(h/L_r)), and the
bottom is retained separately. For (H=1,2), no full smooth residual
frequency label exists.

The entire (d=0) summand is defined to be zero. Equivalently, the
denominator sum may be written over (d\ge1). This convention is exact
because every positive-support coefficient is unchanged, and it avoids
the meaningless expression (0\,e(hX/0)).

## Physical and stationary normalization

For one full smooth block (B=(X,j,r,+)), set

\[
 D=D_j,\qquad L=L_r,\qquad K=\frac{XL}{D^2},\qquad M=LK.
\]

The exact Vaaler and quarter-shift identities are

\[
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\]

\[
 \alpha_{h,H}C_h
 =-\frac{\Phi(h/(H+1))\chi_4(h)}{\pi h},\qquad
 C_h=e(h/4)-e(3h/4)=2i\chi_4(h).
\]

Thus the positive physical child is

\[
 \mathcal B_B^+
 =-\frac1\pi\sum_{h\ge1}\frac{\chi_4(h)W(h/L)
 \Phi(h/(H+1))}{h}
 \sum_{d\ge1}W(d/D)e(hX/(4d)),
\]

and the two-sided physical block, including the earlier outer factor four,
is (B_{2,B}=8\operatorname{Re}\mathcal B_B^+).

Define the real normalized continuum amplitude on the positive quadrant by

\[
 A_B(x,z)=W(x/L)\Phi(x/(H+1))
 \left(\frac{M}{xz}\right)^{3/4}
 W\!\left(\sqrt{\frac{xX}{4zD^2}}\right),
\tag{113.R1}
\]

and extend it by zero. Since (r\ge1), its rescaled support stays in a
fixed compact subset of the smooth interior of (\Phi). All logarithmic
derivatives are uniformly bounded. Formula (113.R1) agrees with the
literal coefficient at every positive integer pair and makes every smooth
stationary entry and exit part of the symbol.

With

\[
 \mathcal T_B=\sum_{h,k\ge1}\chi_4(h)A_B(h,k)e(R\sqrt{hk}),
 \qquad
 c_B=\frac{e(1/8)}{2\pi}X^{1/4}M^{-3/4},
\]

the accepted smooth transform is exactly

\[
 \mathcal B_B^+=-c_B\mathcal T_B+E_{B,\mathrm{tr}},
 \qquad |E_{B,\mathrm{tr}}|\ll1.
\tag{113.R2}
\]

The minus sign, (e(1/8)), and (1/(2\pi)) are therefore certified.

## Exact balanced labels

The ratio is not merely asymptotic:

\[
 \frac KL=4^j\frac X{\lfloor\sqrt X\rfloor^2}.
\tag{113.R3}
\]

For (X\ge4096), (j=1) is balanced; (j=2) is balanced exactly at
(X=\lfloor\sqrt X\rfloor^2), where (K/L=16); and (j\ge3) is
unbalanced. Equality belongs to the balanced side. The finite earlier-owner
priority is frozen once for the campaign, with equality assigned to the
earlier owner. It is not changed block by block.

This exact classification is useful simplification, but it is not an
estimate: the surviving (j=1) family still contains the full open
balanced signed packet.

## Scope

The review certifies only the finite profiles, continuum symbol,
normalization, exact ratio boundary, and uniformity. It does not certify
the signed quarter-packet bound, any new (D)- or (L)-range, M9-M2,
M9-M1, endpoint uniformity, M9, or a new Gauss-circle exponent.
