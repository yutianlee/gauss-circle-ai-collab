# Round 169 synthesis: exact double-Poisson self-return

Round 169 closes under
**`t1_joint_FE_spectral_self_return_no_go`**.  It does not prove the
polynomial-range (t=1) estimate or a new strict polynomial sector.  It
does prove the exact coefficientwise joint-functional-equation transform
and identifies it, up to a target-safe residue correction, with the
accepted Round-162 character--Poisson product-collar family.

## Exact progress

For

\[
 G(s_1,s_2)=\sum_{Q,R\geq1}g(Q,R)Q^{-s_1}R^{-s_2},
\]

the odd-prime local coefficients are supported on

\[
 (0,0),(2,0),(0,2),(1,1),(2,1),(1,2)
\]

with weights (1,-1,-1,-\chi_4(p),1,\chi_4(p)).  At (p=2), only
((0,0)) and ((0,2)) occur, with weights (1,-1).  These coefficients
collapse exactly to

\[
 g(Q,R)=\chi_4(Q)
 \sum_{\substack{[u^2,c]=Q,\ [v^2,c]=R\\u,c\ \mathrm{odd}}}
 \mu(u)\mu(v)\mu(c).
\]

Their shifted-line absolute mass is

\[
 \sum_{Q,R}|g(Q,R)|(QR)^{-1/2-\eta}\asymp\eta^{-3},
\]

whereas \(\sum|g(Q,R)|/(QR)\) converges.

With the exact cardinal interpolant and the Fourier convention fixed in
the accepted kernel, finite character Poisson in the first variable and
ordinary Poisson in the second give

\[
 \mathcal S_{L,1}=\frac i2
 \sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)\sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).
\]

The finite physical zero mode is not the complete Mellin residue.  If
(Z_{\mathrm{phys}}) denotes that zero mode, then

\[
 E_0:=Z_{\mathrm{phys}}-R_\zeta,
 \qquad Z_{\mathrm{phys}},R_\zeta,E_0\ll L^2/J.
\]

Consequently the exact open integral is

\[
 \mathcal I_\eta=E_0+\frac i2
 \sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)\sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right).
\]

The completed zeta and (L(s,\chi_4)) equations both have root number
one; their even and odd gamma quotients are respectively the cosine and
sine Mellin kernels in this formula.  The only positive stationary branch
obeys

\[
 k\ell=XQR,\qquad Q\ell\leq Rk\leq4Q\ell.
\]

This is exactly the previously accepted Mobius--Poisson product-collar
geometry after the coefficient collapse.  An infinite (G)-series may
not be absolutely resummed after the left contour shift; finite physical
convolution followed by Poisson is the lawful order.

## First open interface and scoped no-go

On a favorable globally smooth radial model the collar has width
(QRJ/L), but the inherited positive capacity remains
(\sqrt{JL}X^\varepsilon), with unpaid ratio
(H/L+O(L^{-1})\).  The literal cardinal transform has (O(L^2)) cells,
so it cannot inherit this global recombination without another theorem.

The audited primary sources do not directly convert the arbitrary-real
moving product collar, common-prime and two-adic branches, literal
cardinal weight, and signed outer (g(Q,R)/(QR)) aggregate into a
target-safe shifted-convolution, Kloosterman, Kuznetsov, or reciprocity
estimate with every spectral and main term restored.  This is a scoped
interface no-go, not a claim that no future signed spectral theorem can
apply.

The first unproved estimate is therefore the nonzero-frequency aggregate
above at (O_\varepsilon(L^{3/2}X^\varepsilon)).  Bare functional
equations and dualization do not supply the required signed cancellation.

## Proof status after Round 169

The new node is an exact internal reduction below the open hard-TOP
signed-cone owner.  The polynomial (t=1) scalar and residual, K17a,
K26, all other hard-TOP channels and collars, hard TOP, BAL, UNBAL,
M9--M2, both direct M1 parents, GAR, endpoint uniformity, M9, both
bridges, and the quarter theorem remain open.

There is no global exponent improvement.  The internally proved exponent
remains (1/3); the audited external Li--Yang benchmark remains
(0.3144831759740614\ldots); the target remains (1/4).

Round 170 is the mandatory full-proof dependency, frontier, and current-
literature review.  It must compare all open M1 and M2 owners before
selecting another analytic mechanism.

## State effect

The applied State Patch creates
`M9-M2-hard-top-t1-joint-functional-equation-double-poisson-self-return`,
adds it only as an inconclusive dependency of
`M9-M2-top-endpoint-signed-cone`, records seven scoped rejected readings,
and explicitly preserves 22 residual, parent, bridge, theorem, and
exponent nodes.  The resulting graph SHA-256 is
`111809875d911d279ae22bee2ce44f0dba97130eeedcdca0dc65f53f163283ae`.
