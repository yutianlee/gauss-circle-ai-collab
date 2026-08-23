# Round 114 derivation packet

Campaign: `m9-m2-balanced-literal-energy-connector-fork`
Starting graph: `411adc0c93d2451dfc1235840f27063b3ef4869d0c67aebfbbc74fe9ef04387c`

This packet freezes the accepted input and the conductor's proposed finite
kernel.  It proves no balanced estimate.

## 1. Accepted literal input

For one Round-113 balanced smooth block `B`,

\[
A_B(x,z)=W(x/L)\Phi(x/(H+1))
\left(\frac{LK}{xz}\right)^{3/4}
W\!\left(\sqrt{\frac{xX}{4zD^2}}\right),
\]

where `A_B` is real, supported on `x asymp L`, `z asymp K`, and has
uniform rescaled seminorms.  For the persistent label `j=1`,

\[
D=\frac{\lfloor R\rfloor}{2},\qquad
\frac KL=4\frac{X}{\lfloor R\rfloor^2},
\]

so `K/L` is bounded above and below by absolute constants.  The isolated
`j=2` balanced label exists only for square `X` at `K/L=16` and is a
separate control.

The exact smooth gcd telescope is

\[
\sum_\sigma\psi_\sigma(g)=\eta(g/G_0),\qquad G_0=\sqrt L/2.
\]

Round 113 proved

\[
Z_B(R):=\sum_\sigma G_\sigma Q_{B,\sigma}^{\rm full}(R)
=2i\mathcal T_B^{\rm low},
\tag{114.D1}
\]

\[
\mathcal T_B^{\rm low}=
\sum_{\substack{g,u,v\ge1\\(u,v)=1}}
\eta(g/G_0)\chi_4(g)\chi_4(u)
A_B(gu,gv)e(Rg\sqrt{uv}).
\tag{114.D2}
\]

The target is `|Z_B(R)| << L^(3/2) X^epsilon`.  The modulus remains
outside the whole sigma sum.  All previous owners remain separate.

## 2. Exact collapse to original lattice coordinates

The map

\[
(h,k)\longleftrightarrow
(g,u,v)=(\gcd(h,k),h/g,k/g)
\]

is a bijection.  Therefore the candidate low-gcd coefficient is

\[
a_B^{<}(h,k)=
\chi_4(h)\eta\!\left(\frac{\gcd(h,k)}{G_0}\right)A_B(h,k),
\tag{114.D3}
\]

and

\[
\mathcal T_B^{\rm low}
=\sum_{h,k}a_B^{<}(h,k)e(R\sqrt{hk}).
\tag{114.D4}
\]

This is not character erasure: (114.D4) is the exact inverse
recombination of both quarter shifts in (114.D1).  It is lawful for a
direct estimate, but a later Cauchy step must still record whether the
character lies inside or outside the squared row.

## 3. Candidate exact energy and product split

Expanding (114.D4) gives

\[
|\mathcal T_B^{\rm low}|^2
=\sum_{h,k,h',k'}a_B^{<}(h,k)\overline{a_B^{<}(h',k')}
e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right).
\tag{114.D5}
\]

In gcd coordinates its phase diagonal is

\[
g^2uv=g'^2u'v',
\tag{114.D6}
\]

not merely `uv=u'v'`.  Define the literal product coefficient

\[
c_B(n)=\sum_{hk=n}a_B^{<}(h,k).
\tag{114.D7}
\]

Then exactly

\[
\mathcal T_B^{\rm low}=\sum_n c_B(n)e(R\sqrt n),
\tag{114.D8}
\]

and the equal-full-product energy is

\[
E_0=\sum_n|c_B(n)|^2.
\tag{114.D9}
\]

Since `|a_B^<|<<1`, `hk asymp LK asymp L^2`, and divisor multiplicities
are `O_epsilon(X^epsilon)`, the proposed elementary bound is

\[
E_0\ll_\varepsilon L^2X^\varepsilon,
\tag{114.D10}
\]

which has a factor `L` of room inside the `L^3` energy budget.  The exact
off-diagonal may be grouped by `r=n-n' != 0` without taking an absolute
value inside the divisor fibres.

## 4. Two stronger sufficient Gram norms

Cauchy in `h` gives

\[
|\mathcal T_B^{\rm low}|^2\ll
L\sum_{h\asymp L}\left|\sum_{k\asymp K}
\eta(\gcd(h,k)/G_0)A_B(h,k)e(R\sqrt{hk})\right|^2.
\tag{114.D11}
\]

The character `chi_4(h)` is outside the inner sum and disappears in its
modulus.  At `K asymp L`, a right side `O(L^2 X^epsilon)` for the displayed
mean square is sufficient but stronger than the direct target.

Cauchy in `k` gives the character-preserving alternative

\[
|\mathcal T_B^{\rm low}|^2\ll
K\sum_{k\asymp K}\left|\sum_{h\asymp L}
\chi_4(h)\eta(\gcd(h,k)/G_0)A_B(h,k)e(R\sqrt{hk})
\right|^2.
\tag{114.D12}
\]

Again `O(L^2 X^epsilon)` is sufficient in the balanced regime.  Neither
Gram is equivalent to the direct scalar target, and the old proposed
mean-square node does not yet have a literal implication to all of M9-M2.

## 5. Literal determinant ray defect

Let

\[
(h',k')=(h+p,k+q),\qquad
\rho=hk'-h'k=hq-kp.
\tag{114.D13}
\]

Put

\[
P=1+\frac12\left(\frac ph+\frac qk\right),\qquad
Q=\left(1+\frac ph\right)\left(1+\frac qk\right).
\]

Because

\[
P^2-Q=\frac14\left(\frac ph-\frac qk\right)^2,
\]

rationalization gives the exact identity

\[
\begin{aligned}
\sqrt{h'k'}-\sqrt{hk}
&-\frac12\sqrt{\frac kh}\,p
-\frac12\sqrt{\frac hk}\,q\\
&=-\frac{\rho^2}
{4(hk)^{3/2}\left(P+\sqrt Q\right)}.
\end{aligned}
\tag{114.D14}
\]

Thus `rho` is the literal transverse determinant for the square-root cone.
The different identity for `u^2/m` is algebraically correct but is not an
independent connector unless its variables are mapped to (114.D5).

## 6. Candidate narrow determinant count

For fixed integer `rho` and fixed `(h,k)`, the equation

\[
hk'-h'k=\rho
\tag{114.D15}
\]

has no solution unless `d=gcd(h,k)` divides `rho`.  When it does, all
solutions differ by

\[
(h',k')\mapsto(h',k')+t(h/d,k/d).
\]

Inside fixed boxes of side `O(L)` there are `O(1+d)` such solutions.  Hence
for nonzero `rho`,

\[
\#\{h,k,h',k': hk'-h'k=\rho\}
\ll L^2\sum_{d\mid\rho}\frac1d
\ll_\varepsilon L^2X^\varepsilon,
\tag{114.D16}
\]

while `rho=0` costs `O(L^2 log L)`.  Consequently

\[
\sum_{|\rho|\le Q}^{\rm absolute}1
\ll_\varepsilon L^2(Q+1)X^\varepsilon.
\tag{114.D17}
\]

The proposed threshold `Q=L` therefore puts the entire determinant-narrow
part of (114.D5) within `L^3X^epsilon`, even for bounded arbitrary
coefficients.  This is a candidate target-safe branch, not the full energy
estimate.  The broad survivor has `|rho|>L` and must still be estimated
with the actual signs and phase.  At the threshold (114.D14) has transverse
phase size comparable to `R/L` at the critical relation `R=L^3`, so no
extra saving is claimed by counting alone.

## 7. Required hostile checks

- Verify the `O(1+d)` line-intersection count uniformly in the slanted
  fixed-comparability support.
- Keep equal full products distinct from equal primitive products.
- Do not infer the direct target from failure of either stronger Gram.
- A phase-conjugating coefficient array falsifies coefficient-uniform Gram
  statements but is not a lower bound for the actual symbol.
- Exact rational rays can contain quarter-shift resonance; periodic
  `chi_4` alone does not automatically cancel them.
- Generic curvature cannot certify a fixed-real-`X` pointwise estimate;
  the broad branch needs a literal arithmetic or sign-sensitive inequality.
- No owner correction or second physical block is available for
  cancellation.

The desired Round-114 theorem-level output is the smallest validated piece
among (114.D5)--(114.D17), together with an exact statement of the broad
survivor or the first failed seam.
