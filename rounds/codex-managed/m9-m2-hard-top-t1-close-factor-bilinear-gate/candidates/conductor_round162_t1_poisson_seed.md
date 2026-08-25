# Round 162 conductor seed: character Poisson and the dual hyperbola

- Campaign: m9-m2-hard-top-t1-close-factor-bilinear-gate
- Status: candidate algebra only; nothing here is accepted mathematics
- Starting graph:
  8d39b06bd12357e337159473da3d4d6ec0c71d0ab3217588e4c6b5b34973b422

## 1. Literal arithmetic simplification

On (t=1), the accepted radical incidence forces (g=u=v=1). Thus the
physical conditions are exactly those in (162.B1). The squarefree and
coprime conditions can be compressed without loss as

\[
 d_1,d_2\ {
m squarefree},\ (d_1,d_2)=1
 \quad\Longleftrightarrow\quad \mu^2(d_1d_2)=1.
\tag{162.C1}
\]

This identity does not make the coefficient separable. Opening
(\mu^2(d_1d_2)=\sum_{a^2\mid d_1d_2}\mu(a)) couples the variables: each
prime square can lie in (d_1), in (d_2), or across both. Every such
allocation and rescaled hard boundary must be charged.

For odd (d_1), retain the exact character identity

\[
 \chi_4(d_1)=\frac{e(d_1/4)-e(-d_1/4)}{2i}.
\tag{162.C2}
\]

## 2. Rank-one phase geometry

For (f(x,z)=J\sqrt{xz}),

\[
 f_x=\frac J2\sqrt{\frac zx},\qquad
 f_z=\frac J2\sqrt{\frac xz},
\tag{162.C3}
\]

and

\[
 \operatorname{Hess}f=\frac J4
 \begin{pmatrix}
 -\sqrt z\,x^{-3/2}&(xz)^{-1/2}\\
 (xz)^{-1/2}&-\sqrt x\,z^{-3/2}
 \end{pmatrix},
 \qquad \det\operatorname{Hess}f=0.
\tag{162.C4}
\]

The radial vector ((x,z)) is null. Therefore no two-dimensional
stationary-phase determinant may be divided out without separately
resolving the radial direction.

## 3. One-variable character Poisson

For the sign (\sigma\in\{+1,-1\}) from (162.C2), the (x)-Poisson
phase at frequency (k\in\mathbb Z) is

\[
 F_{k,\sigma}(x;z)=J\sqrt{xz}+\frac{\sigma x}{4}-kx,
 \qquad r=k-\frac\sigma4.
\tag{162.C5}
\]

An interior saddle requires (r>0) and satisfies

\[
 x_0=\frac{Xz}{4r^2},\qquad
 F_{k,\sigma}(x_0;z)=\frac{Xz}{4r},\qquad
 |F''_{k,\sigma}(x_0;z)|^{-1/2}
 =\left(\frac{Xz}{2r^3}\right)^{1/2}.
\tag{162.C6}
\]

On (x,z\asymp L), the physical saddle range has (r\asymp J), length
(\asymp J), and individual stationary scale (\asymp\sqrt{L/J}).
Termwise positive closure therefore costs (\asymp\sqrt{JL}) per
(z)-row before the outer sum and is not a gain. More importantly, the
dual phase (Xz/(4r)) is the reciprocal hard-TOP carrier. The exact
profiles, stars, quarter shifts, squarefree opening, and endpoints must be
matched before declaring a literal self-return.

## 4. Simultaneous dual equations

After Poisson in both variables, an interior critical point for dual
frequencies ((k,\ell)) would obey

\[
 k-\frac\sigma4=\frac J2\sqrt{\frac zx},\qquad
 \ell=\frac J2\sqrt{\frac xz}.
\tag{162.C7}
\]

Hence the exact dual stationary locus is the hyperbola

\[
 \left(k-\frac\sigma4\right)\ell=\frac X4.
\tag{162.C8}
\]

This is a one-dimensional locus, not an isolated two-dimensional saddle.
Writing (r=k-\sigma/4), the optimized radial mismatch is
(2\sqrt{r\ell}-J). Since (x,z\asymp L), a first integration-by-parts
threshold suggests

\[
 |2\sqrt{r\ell}-J|\lesssim L^{-1}
 \quad\Longleftrightarrow\quad
 |r\ell-X/4|\lesssim J/L.
\tag{162.C9}
\]

Equation (162.C9) is a candidate collar, not yet a proved sharp support
statement at the hard boundaries.

## 5. Candidate power ledger

Because (4r=4k-\sigma) is an odd integer, the collar in (162.C9) is an
integer product window of length (\asymp J/L). Divisor counting alone
suggests at most

\[
 \frac JL X^\varepsilon
\tag{162.C10}
\]

dual pairs in dyadic boxes. Transverse stationary phase with an unresolved
radial interval has candidate size (L^{3/2}J^{-1/2}) per pair. Positive
summation therefore returns

\[
 \frac JL\,L^{3/2}J^{-1/2}X^\varepsilon
 =\sqrt{JL}\,X^\varepsilon.
\tag{162.C11}
\]

The desired comparison (\sqrt{JL}\le L^{3/2}) is equivalent to
(J\le L^2). The physical range has (L\le J^{1/2}), so this ledger is
target-sized only on the boundary and gives no strict range. Hard edges,
Möbius allocations, and coefficient norms can only worsen this positive
ledger unless a signed dual theorem is proved.

## 6. Required falsification

The discovery and source tasks must decide whether (162.C6)--(162.C11)
are literal after all coefficient openings or merely a smooth model. A
valid positive theorem must gain cancellation across the dual product
window for the actual character and Möbius-weighted amplitudes. A valid
no-go may park only the explicitly derived Poisson, positive collar, or
named-source routes. Neither outcome is a physical lower bound.

## 7. Downstream quarantine

Even a proof of the (t=1) target leaves all (L\ll D\ll L^2),
(t\ll\sqrt L) few-point channels and their near collars open. No full
hard-TOP, M9--M2, M9, bridge, quarter-theorem, or exponent statement is
licensed by this seed.
