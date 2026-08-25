# Round 140 blind statement: exact post-collar height--alias gate

## 1. Frozen scalar

Let

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad0\le q\le2y,
\]

and fix \(0<\rho<1/8\). For \(h\ge1\), put

\[
 L_h=\left\lfloor{\rho y\over\sqrt h}\right\rfloor,
 \qquad D_h=y-L_h-1.
\tag{140.B1}
\]

With literal empty-row and zero-extension conventions, define

\[
 \mathcal S_N^+
 =\sum_{h\ge1}{1\over h}
  \sum_{1\le d\le D_h}\chi_4(d)
  V_{\rm low}\!\left({4R^2h^2\over d^2}\right)
  e\!\left({Nh\over d}\right),
\qquad \mathcal S_N^-=\overline{\mathcal S_N^+}.
\tag{140.B2}
\]

The profile is the fixed real lower profile, with its literal endpoint
samples and zero extension. A nonzero sample forces \(h\ll d/R\), hence
\(h\ll R\). The target is

\[
 \boxed{|\mathcal S_N^\pm|\ll_\varepsilon RX^\varepsilon.}
\tag{140.T}
\]

Round 139 has already shown that this target is equivalent to the
original lower scalar target. No statement about the square of
\(\mathcal S_N\) is supplied or permitted.

## 2. Exact transform coordinates

For the positive sign, use

\[
 \chi_4(d)={e(d/4)-e(-d/4)\over2i}.
\tag{140.B3}
\]

In a complete Poisson formula for the finite interval \(1\le d\le D_h\),
write the branch as \(\tau\in\{+1,-1\}\), the dual integer as \(k\), and

\[
 r=\tau-4k.
\tag{140.B4}
\]

For \(r>0\), the phase

\[
 \phi_{h,r}(x)={Nh\over x}+{rx\over4}
\tag{140.B5}
\]

has

\[
 x_*=2\sqrt{Nh/r},\qquad
 \phi_{h,r}(x_*)=\sqrt{Nhr}.
\tag{140.B6}
\]

The stationary point lies inside the tail interval precisely when

\[
 r\ge {4Nh\over D_h^2}.
\tag{140.B7}
\]

Writing \(r=4h+s\), with \(s\) odd, converts this to the exact threshold

\[
 s\ge {4h(N-D_h^2)\over D_h^2}.
\tag{140.B8}
\]

The right side is heuristically of order \(\sqrt h\), but that comparison
must be proved with every floor and the full range \(0\le q\le2y\).
The possible stationary profile becomes
\(V_{\rm low}(R^2hr/N)\), and the clean interior leading phase becomes

\[
 e\!\left(\sqrt{Nh(4h+s)}\right).
\tag{140.B9}
\]

Equations (140.B6)--(140.B9) describe only stationary coordinates. They
are not authorization to replace the exact finite sum by a principal
family.

## 3. Required owner ledger

Any exact transform must retain:

- the height-dependent integer endpoint \(D_h\), including equality and
  empty rows;
- the hard endpoint half-weight required by the chosen Fourier convention;
- both mod-four branches and the conjugate scalar;
- all nonstationary dual modes;
- stationary entry and exit, profile-boundary crossings, and any
  incomplete-Fresnel transition;
- every stationary remainder and the actual \(h^{-1}\) weight;
- the fixed-centre range \(0\le q\le2y\), including \(q=0\), \(q=2y\),
  and odd fourth-power controls.

The homogeneous phase \(\sqrt{Nhr}\) has a rank-one Hessian in \((h,r)\).
A claimed two-dimensional gain must therefore explain what replaces
nondegenerate curvature and must test coherent rational rays. Product
fibres, the exact phase-one radical channel, near radicals, and their
aggregate must be distinguished. A rowwise or aliaswise modulus, a
positive energy, or a second invertible transform is not a signed gain.

## 4. Decision rule

Prove (140.T), derive a strictly smaller owner-complete signed survivor
with all discarded owners bounded by \(RX^\varepsilon\), or identify the
first rigorous cutoff, endpoint, transition, rank-one, resonance,
product-fibre, self-return, or capacity obstruction.

Return every estimate to the scalar target. Do not infer a tail-square
identity, a deletion from the earlier cross-denominator residual, lower
GAR, a blockwise M1 theorem, M9-M1, any M2 theorem, endpoint uniformity,
M9, the quarter theorem, or an exponent improvement.

The report must have exactly seven numbered sections: result; exact
statement and hypotheses; proof or derivation; first doubtful or unproved
step; control tests and outcomes; dependencies and exact artifacts; and
recommended state effect.
