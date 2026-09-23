# Round 169 conductor adjudication

## 1. Result and terminal decision

Round 169 closes under

\[
 \boxed{\texttt{t1\_joint\_FE\_spectral\_self\_return\_no\_go}.}
\]

The polynomial-range \(t=1\) target and every strict new polynomial
sector remain unproved.  The round does prove one exact homogeneous
reduction: the residual Euler coefficients collapse coefficientwise to
the accepted Round-162 Mobius openings, and the two completed GL(1)
kernels give the exact finite character-Poisson/ordinary-Poisson family.

The delicate zero-mode seam is now exact.  The finite physical zero mode
\(Z_{\mathrm{phys}}\) is not the full Round-168 Mellin residue
\(R_\zeta\), but

\[
 E_0=Z_{\mathrm{phys}}-R_\zeta\ll L^2/J.
\tag{169.A1}
\]

Thus \(\mathcal I_\eta\) is the finite active nonzero-frequency family
plus a target-safe correction.  The active family is exactly the
Round-162 signed product-collar transform in collapsed coordinates.
Bare dualization supplies no estimate for it.

## 2. Accepted internal kernel

For odd primes,

\[
 G_p=1-x_p^2-y_p^2-x_py_p+x_p^2y_p+x_py_p^2,
\]

and \(G_2=1-2^{-2s_2}\).  Hence the six nonzero odd-prime coefficient
pairs are

\[
 (0,0),(2,0),(0,2),(1,1),(2,1),(1,2)
\]

with weights \(1,-1,-1,-\chi_4(p),1,\chi_4(p)\), and

\[
 g(Q,R)=\chi_4(Q)
 \sum_{\substack{[u^2,c]=Q,\ [v^2,c]=R\\u,c\ \mathrm{odd}}}
 \mu(u)\mu(v)\mu(c).
\tag{169.A2}
\]

The exact shifted-line coefficient mass is

\[
 \sum_{Q,R}|g(Q,R)|(QR)^{-1/2-\eta}
 \asymp\eta^{-3},
\]

while the mass with weight \((QR)^{-1}\) converges.

For the exact cardinal interpolant,

\[
 \mathcal S_{L,1}
 =\frac i2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)
 \sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).
\tag{169.A3}
\]

Subtracting the full Mellin residue gives

\[
 \mathcal I_\eta
 =E_0+\frac i2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)
 \sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).
\tag{169.A4}
\]

The zeta and \(\chi_4\) completions have root number one and respectively
even and odd gamma parity.  Their uncompleted gamma quotients are the
Mellin kernels of \(2\cos(2\pi u)\) and \(\sin(\pi u/2)\), giving the
exact constants in (169.A3).  An infinite \(G\)-series cannot be
resummed absolutely after a left contour shift; the finite physical
convolution before Poisson is the lawful order.

The only positive interior stationary branch obeys

\[
 k\ell=XQR,\qquad Q\ell\le Rk\le4Q\ell.
\tag{169.A5}
\]

On a favorable recombined smooth block its width is \(QRJ/L\), and the
inherited positive capacity is \(\sqrt{JL}X^\varepsilon\), with unpaid
ratio \(H/L+O(L^{-1})\).  The exact cardinal array does not inherit that
global radial scale without a new recombination theorem.

## 3. Source and interface adjudication

The hostile audit checks exact primary hypotheses for shifted
convolution, local/global spectral decomposition, Kuznetsov and
Kloosterman sums, regular and exceptional spectral large sieves,
spectral reciprocity, and weighted moments.  None is used in the internal
kernel.

After granting the exact double-Poisson transform, the surviving source
seam is narrow: no audited theorem converts the arbitrary-real moving
product collar, its common-prime and two-adic branches, its literal
cardinal weight, and the signed outer \(g(Q,R)/(QR)\) aggregate into the
required integral additive/Kloosterman data with target-safe norms and
all main, continuous, holomorphic, Maass, and exceptional pieces.

This dated source conclusion is not a universal literature impossibility
theorem.  A bespoke signed theorem for the single aggregate in
(169.A4) remains possible.

## 4. First doubtful or unproved step

The first open theorem is

\[
 \frac i2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)\sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right)
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{169.A6}
\]

The correction \(E_0\) is already safe.  The unresolved step is genuine
signed cancellation among outer coefficient blocks, neighboring products,
and cardinal cells before every positive norm.  Functional equations,
the rank-one phase, and the audited source placements do not prove it.

## 5. Required controls and outcomes

All controls are recorded in
`controls/conductor_round169_controls.md`.  Coefficient algebra,
\(p=2\), the \(\eta\)-mass, completed functions, gamma/Fourier constants,
the finite-zero/full-residue correction, exact endpoint retention,
stationary product and cone, source hypotheses, statement-only
independence, false controls, and downstream scope are green.  The
target-strength signed estimate and a lawful global smooth recombination
remain open.  No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The accepted kernel is
`proofs/kernels/m9_m2_hard_top_t1_joint_functional_equation_double_poisson_self_return.md`.
It depends directly only on the accepted Round-168 Mellin--Euler/cardinal
reduction and the accepted Round-162 character-Poisson/collar obstruction.

The adjudication uses all three Round-169 reports, the conductor
candidate, the independent coefficient/gamma/residue review, the
source/spectral/power review, the downstream graph-scope review, the
final internal-kernel verification, and the conductor control ledger.
The source report supplies negative applicability evidence only.

## 7. Recommended state effect

Create one `proved_internal` reduction node containing the exact local
and collapsed \(g\)-law, completed kernels, finite double-Poisson formula,
finite-zero/full-residue correction, product/cone geometry, and scoped
self-return.  Add it only as an inconclusive dependency of the still-open
`M9-M2-top-endpoint-signed-cone` owner.

Record the stronger false readings as rejected.  Preserve every open
owner, blocker, implication, bridge, theorem, and exponent.  The mandatory
Round-170 full-proof strategy and current-literature review is next.
