# Round 74 synthesis: the hard edge is safe, but the signed interior remains

Round 74 does not prove the top \(M2\) affine-cone estimate

\[
 \mathcal T_L^{\mathrm{end}}\ll_\varepsilon
 L^{3/2}X^\varepsilon
\]

for polynomial intermediate \(1\ll L\ll H\).  Bounded \(L\), the
epsilon-trivial range \(L\leq(\log(2+X))^A\), and the inherited terminal
slice \(L\asymp H\) are safe.

The accepted new reduction is elementary but exact.  After Cauchy in the
outer frequency, the diagonal, every fixed-width near-diagonal, and every
correlation touching either moving endpoint have total pre-Cauchy
capacity \(O(L^2)\).  The only survivor of this sufficient route is

\[
 \mathcal C_{\mathrm{core}}
 =2\Re\sum_h\sum_{k>K_0}
 \sum_{b_h<m<h-k}
 a(h,m)\overline{a(h,m+k)}
 e\!\left(\sqrt{Xh}(\sqrt m-\sqrt{m+k})\right),
\]

and

\[
 \mathcal C_{\mathrm{core}}\ll_\varepsilon L^2X^\varepsilon
\]

would imply the target.  This is sufficient, not necessary: Cauchy has
removed the original \(\chi_4(h)\).

The more promising character-preserving candidate is the exact
quarter-shift Poisson normal form.  Its Hessian is rank one.  The formal
stationary image is a fixed-centre near-product wavelet

\[
 \mathcal D_L
 =\sum_{\substack{j\asymp\sqrt X\\j\ \mathrm{odd}}}\chi_4(j)
 \sum_{l\asymp\sqrt X}B_{L,X}(j,l)
 K\!\left(\frac{L(X-jl)}{4l}\right),
\]

effectively supported on
\(|X-jl|\ll\sqrt X\,X^\varepsilon/L\).  The required bound is
\(\mathcal D_L\ll X^{1/4+\varepsilon}\).  Poisson in the uncharactered
leg produces a reciprocal energy with diagonal \(L\sqrt X\), exactly the
target scale; its off-diagonal is open.  Poisson in the character leg
returns coefficient-for-coefficient to the original \(M2\) reciprocal
block.

This candidate was independently supported by the discovery and hostile
reports, but it did not receive the protocol-required statement-only
rederivation.  It is therefore retained for Round 75 rather than promoted
now.

The closest applicable primary bilinear theorem, Kowalski--Robert--Wu
Proposition 5, is dominated by the already accepted two-shift estimate
wherever it is nontrivial.  No source supplies the missing fixed-centre
actual-symbol energy.

The global exponent is unchanged.

