# Conductor candidate: literal energy and determinant-narrow branch

Campaign: `m9-m2-balanced-literal-energy-connector-fork`
Starting graph: `411adc0c93d2451dfc1235840f27063b3ef4869d0c67aebfbbc74fe9ef04387c`

This is candidate evidence.  It must be independently rederived and
hostilely audited before any state change.

## Candidate A: exact full-product energy connector

For the Round-113 block, let

\[
a_B^{<}(h,k)=\chi_4(h)
\eta\!\left(\frac{\gcd(h,k)}{\sqrt L/2}\right)A_B(h,k).
\]

Then

\[
\sum_\sigma G_\sigma Q_{B,\sigma}^{\rm full}(R)
=2i\sum_{h,k}a_B^{<}(h,k)e(R\sqrt{hk}).
\tag{114.C1}
\]

Consequently its squared energy is exactly the four-variable sum in
(114.D5), and grouping by `n=hk` gives (114.D7)--(114.D9).  The exact
diagonal is `hk=h'k'`, or `g^2uv=g'^2u'v'` in primitive coordinates.
Divisor multiplicity and `|a_B^<|<<1` give

\[
\sum_n\left|\sum_{hk=n}a_B^{<}(h,k)\right|^2
\ll_\varepsilon L^2X^\varepsilon.
\tag{114.C2}
\]

This corrects the strategy-memo shorthand `uv=u'v'`.

## Candidate B: exact determinant curvature identity

For `(h',k')=(h+p,k+q)` define

\[
\rho=hk'-h'k=hq-kp.
\]

Then the exact tangent remainder is (114.D14).  In particular `rho=0`
means that the two lattice points lie on one rational ray, and nonzero
`rho` measures their transverse lattice separation.

## Candidate C: target-safe determinant-narrow branch

Uniformly for `1<=K/L<=16`, bounded coefficients supported on the literal
balanced boxes satisfy

\[
\sum_{\substack{h,k,h',k'\\|hk'-h'k|\le L}}
|b(h,k)b(h',k')|
\ll_\varepsilon L^3X^\varepsilon
\tag{114.C3}
\]

provided `|b|<<1`.  The proof is the lattice-line count (114.D15)--
(114.D17).  Therefore the determinant-narrow portion of the exact packet
energy is target-safe without using a character.  The remaining broad
problem is

\[
\sum_{|hk'-h'k|>L}
a_B^{<}(h,k)\overline{a_B^{<}(h',k')}
e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right)
\ll_\varepsilon L^3X^\varepsilon.
\tag{114.C4}
\]

No estimate for (114.C4) is claimed.  The identity for `u^2/m` is retained
only as a possible coordinate model; (114.D14), not phase analogy, is the
literal connector.

## Candidate D: mean-square disposition

Both row orientations with right side `L^2X^epsilon` imply the direct
balanced target after one Cauchy factor `L`, but both are stronger.  Only
the `k`-outer orientation keeps `chi_4(h)` inside the inner sum.  The old
mean-square node must not be allowed to imply all of `M9-M2` without a
separate literal range-and-owner audit.

## First doubtful step

The first unproved analytic step after Candidates A--C is (114.C4).  The
rank-one identity supplies geometry but not pointwise cancellation at a
fixed real `X`; modulo-one resonances and actual-symbol character placement
remain live.  A continuation is warranted only if a noninvertible broad
estimate produces a strict saving, a target-safe subrange, or an inverse
theorem.
