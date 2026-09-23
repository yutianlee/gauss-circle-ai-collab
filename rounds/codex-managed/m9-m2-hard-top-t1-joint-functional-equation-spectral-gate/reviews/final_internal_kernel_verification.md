# Final internal verification: Round 169 joint-FE double-Poisson kernel

- Kernel: `proofs/kernels/m9_m2_hard_top_t1_joint_functional_equation_double_poisson_self_return.md`
- Kernel SHA-256: `b4c5e17aab5e586c1234af92f606dad1a8ccf199a108f3afc0ad5fd5977a37dc`
- Role: final accepted-kernel verifier
- Verdict: **PASS**

## 1. Result

**PASS.**  The final kernel is a faithful homogeneous extraction of the
repaired Round-169 conductor candidate.  It retains the complete literal
hard-TOP \(t=1\) scalar, the exact Fourier convention and finite physical
block order, every local coefficient and normalization, the full
completed-function data, the finite-zero/full-residue correction with
the correct sign and strength, the exact stationary product and cone,
the restored smooth-collar power, and the coefficientwise Round-162
self-return.

The kernel proves one exact internal reduction.  It does not turn the
self-return into an estimate, does not replace the literal cardinal
array by a favorable smooth block, does not make a universal source
no-go, and does not promote any owner, bridge, theorem, or exponent.  Its
provenance distinguishes the two accepted upstream kernels from the new
internal deductions.  The dated source-placement sentence is supported
by the assigned source/spectral PASS review and is not represented as an
external theorem used in the internal identities.  No repair is
required.

## 2. Exact statement and hypotheses

The parameter regime

\[
J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
H=\lfloor yX^{-1/4}\rfloor=\sqrt J+O(1),
\qquad 1\ll L\ll H
\tag{169.F1}
\]

matches the candidate.  The exact Round-168 disjoint-cardinal
interpolant \(\mathcal B\) retains every shell, real-centre floor, star,
profile value, cone edge, endpoint transition, parity branch, and zero
extension.  The kernel explicitly fixes

\[
\widetilde{\mathcal B}(\xi,\nu)
=\iint_{\mathbb R^2}\mathcal B(x,z)e(-\xi x-\nu z)\,dx\,dz.
\tag{169.F2}
\]

It also fixes the physical outer sum before Poisson, equivalently by the
rectangle bounded by the positive support suprema.  Extra blocks in that
rectangle have zero complete pre-Poisson lattice sum; their individual
zero and nonzero Poisson modes are not discarded separately.

The arithmetic coefficient is stated both locally and globally.  For
odd \(p\), the six nonzero entries are

\[
\begin{array}{c|rrrrrr}
(v_p(Q),v_p(R))&(0,0)&(2,0)&(0,2)&(1,1)&(2,1)&(1,2)\\ \hline
g_p&1&-1&-1&-\chi_4(p)&1&\chi_4(p),
\end{array}
\tag{169.F3}
\]

while at \(2\) they are \((0,0)\mapsto1\) and
\((0,2)\mapsto-1\).  The collapsed law is

\[
g(Q,R)=\chi_4(Q)
\sum_{\substack{u,v,c\ge1;\ u,c\ \mathrm{odd}\\
                [u^2,c]=Q,\ [v^2,c]=R}}
\mu(u)\mu(v)\mu(c).
\tag{169.F4}
\]

The kernel retains the exact weighted Euler product for
\(\sigma_1,\sigma_2>1/2\), its uniform
\(\eta^{-3}\) specialization at
\(\sigma_1=\sigma_2=1/2+\eta\), and the convergent mass
\(\sum |g(Q,R)|/(QR)\).  These are precisely the coefficient hypotheses
needed for the transform and harmless residue correction; no post-shift
absolute use of the infinite \(G\)-series is asserted.

## 3. Proof and derivation

### 3.1 Coefficients and transform normalization

For odd \(p\), with
\(x=\chi_4(p)p^{-s_1}\) and \(y=p^{-s_2}\),

\[
(1+x+y)(1-x)(1-y)
=1-x^2-y^2-xy+x^2y+xy^2,
\tag{169.F5}
\]

which gives (169.F3).  The eight binary Möbius states give the same six
entries: the two \((2,2)\) contributions cancel.  Since \(u,c\) are odd,
the two-adic branch leaves only \(v_2(v)=0,1\), giving exactly the two
printed coefficients.  Thus (169.K5), (169.K23), and the convolution
(169.K24) preserve every sign and multiplicity, including the even
second leg.

Applying that convolution on the finite lattice support gives

\[
\mathcal S_{L,1}
=\sum_{Q,R}^{\mathrm{phys}}g(Q,R)
 \sum_{m,n\in\mathbb Z}\chi_4(m)\mathcal B(Qm,Rn).
\tag{169.F6}
\]

The Gauss sum \(\tau(\chi_4)=2i\) and conductor four yield

\[
\sum_m\chi_4(m)f(m)
=\frac i2\sum_{\substack{k\in\mathbb Z\\k\ \mathrm{odd}}}
 \chi_4(k)\widehat f(k/4).
\tag{169.F7}
\]

Ordinary Poisson in the second variable and scaling by \(Q,R\) supply
exactly \(1/(QR)\), \(k/(4Q)\), and \(\ell/R\).  Hence (169.K8) has no
missing character, conductor, parity, sign, or Fourier factor.  Pairing
\(k,-k\) and \(\ell,-\ell\) gives the factor \(2\),
\(\sin(\pi kx/(2Q))\), and \(\cos(2\pi\ell z/R)\) in (169.K12).

### 3.2 Finite zero mode and full residue

The kernel correctly distinguishes

\[
Z_{\mathrm{phys}}
=\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}R
 \sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz
\tag{169.F8}
\]

from

\[
R_\zeta
=\sum_{Q\le M_x}\sum_{R\ge1}\frac{g(Q,R)}R
 \sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz.
\tag{169.F9}
\]

The full residue retains the complete \(R\)-sum from \(G(s,1)\), whose
two-adic factor is \(3/4\).  Therefore the exact correction is

\[
E_0=Z_{\mathrm{phys}}-R_\zeta,
\tag{169.F10}
\]

with the sign printed in (169.K9).  Indeed, writing the finite transform
as \(\mathcal S_{L,1}=Z_{\mathrm{phys}}+N_{\mathrm{phys}}\),

\[
\mathcal I_\eta
=\mathcal S_{L,1}-R_\zeta
=E_0+N_{\mathrm{phys}},
\]

which is exactly (169.K11).  Equivalently, blocks added beyond the
physical \(R\)-range have zero complete lattice sum, so their nonzero
modes equal the negative of their zero modes and supply precisely the
same \(E_0\).

At \(x=Qm\), cardinal disjointness leaves one \(x\)-cell.  There are
\(O(L/Q)\) possible \(m\)'s and \(O(L)\) supported \(z\)-cells; on each
cell the \(z\)-phase derivative is \(\asymp J\).  One integration by
parts therefore gives

\[
\left|\sum_m\chi_4(m)\int\mathcal B(Qm,z)\,dz\right|
\ll \frac{L^2}{QJ}.
\tag{169.F11}
\]

Summing against the convergent mass \(\sum |g(Q,R)|/(QR)\) applies both
to (169.F8) and the full \(R\)-sum in (169.F9).  Thus

\[
Z_{\mathrm{phys}},\ R_\zeta,\ E_0\ll L^2/J,
\tag{169.F12}
\]

as stated in (169.K10).  No \(X^\varepsilon\) is needed, and the weaker
accepted headline form would also be target-safe.

### 3.3 Completed functions and contour data

Equations (169.K13)--(169.K14) retain both completed functional
equations.  They encode zeta's even parity, conductor and root number
one, and completed poles at zero and one; and \(\chi_4\)'s odd parity,
conductor four, Gauss sum \(2i\), root number one, and entire completion.
The uncompleted quotients in (169.K15),

\[
X_\zeta(s)=2^s\pi^{s-1}\Gamma(1-s)\sin(\pi s/2),
\qquad
X_4(s)=\left(\frac\pi2\right)^{s-1}
\Gamma(1-s)\cos(\pi s/2),
\tag{169.F13}
\]

are exactly the Mellin kernels of \(2\cos(2\pi u)\) and
\(\sin(\pi u/2)\).  Hence the completed gamma data and the finite
Poisson normalizations agree.

On the intact \(L\zeta G\) contour, only \(s_2=1\) is crossed.  For a
fixed finite physical block the remaining contours may be moved to the
dual convergence region; the apparent singularity at zero cancels in
\(X_\zeta(s)\zeta(1-s)=\zeta(s)\), and reversing \(1-s\) restores
upward orientation without an extra sign.  The kernel expressly forbids
absolute resummation of the infinite \(G\)-series after that left shift.

### 3.4 Phase, collar, and restored power

Only the double-negative positive-frequency branch can be stationary,
with phase

\[
J\sqrt{xz}-\frac{kx}{4Q}-\frac{\ell z}{R}.
\tag{169.F14}
\]

Its two stationary equations give

\[
k\ell=XQR,
\qquad
Q\ell\le Rk\le4Q\ell,
\tag{169.F15}
\]

including the exact image of the literal cone.  With
\(x=rw,z=r/w\), angular stationarity leaves radial phase

\[
r\left(J-\sqrt{\frac{k\ell}{QR}}\right).
\tag{169.F16}
\]

Only for a favorable recombined smooth radial block of length \(L\) does
this broaden to

\[
|k\ell-XQR|\ll QRJ/L.
\tag{169.F17}
\]

The inherited coefficient scale and factor-pair count are

\[
\frac{L^{3/2}}{QR\sqrt J},
\qquad
\left(\frac{QRJ}{L}+1\right)(XQR)^\varepsilon.
\]

Their leading positive product is

\[
\sqrt{JL}\,X^\varepsilon
=L^{3/2}\left(\frac HL+O(L^{-1})\right)X^\varepsilon.
\tag{169.F18}
\]

The kernel therefore restores the unpaid \(H/L\) factor.  It labels this
only as smooth-interior route capacity and expressly refuses to transfer
the length-\(L\) scale to the \(O(L^2)\) unit cardinal cells.

### 3.5 Homogeneity, provenance, and nonpromotion

Every positive clause concerns the same complete literal scalar and the
same double-Poisson reduction.  Substitution of (169.K5) into (169.K8)
restores the accepted Round-162 Möbius signs, character, two-adic branch,
both Fourier variables, and all normalizations coefficientwise.  Thus
the full scalar self-returns exactly, while \(\mathcal I_\eta\)
self-returns with the explicit safe correction \(E_0\).

The provenance is correctly divided.  The intact Mellin/cardinal scalar
and residue come from
`M9-M2-hard-top-t1-mellin-euler-polylog-and-signed-moment-reduction`;
the literal Möbius opening, character-Poisson normalization, rank-one
collar, and positive capacity come from
`M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`.
The \(g\)-law, finite transform, correction, completed-kernel ledger, and
coefficientwise comparison are accurately labelled internal.  The
assigned source/spectral review supplies the evidence for the separate
dated source-placement sentence; no external theorem is used positively.

The final scope paragraph preserves all nonpromotion boundaries.  Its
generic phrases “direct M1 parent,” “bridge,” and “exponent” exclude any
such object; in particular neither direct M1 parent, neither bridge, and
neither exponent ledger changes.

## 4. First doubtful or unproved step

No doubtful step remains inside the asserted kernel.  Since \(E_0\) is
target-safe, the first open theorem is exactly (169.K32):

\[
\frac i2\sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
\sum_{k\ \mathrm{odd}}\chi_4(k)
\sum_{\ell\ne0}
\widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right)
\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{169.F19}
\]

The exact functional equations and double Poisson expose this aggregate;
they supply no cancellation among \((Q,R)\), nearby products, or
cardinal cells.  No audited theorem supplies the required
collar-to-trace-formula placement at target-safe restored power.  This is
a no-go only for bare dualization, the favorable positive placements,
and the dated audited source set.  It is neither a physical lower bound
nor a universal impossibility theorem for a future bespoke signed
spectral or reciprocity estimate.

Even a future proof of (169.F19) would settle only the complete \(t=1\)
face.  The other hard-TOP channels and collars, hard TOP, BAL, UNBAL,
M9--M2, both direct M1 parents, GAR, endpoint uniformity, M9, both
bridges, the quarter theorem, and both exponent ledgers would remain.

## 5. Required controls and outcomes

| Required control | Outcome |
|---|---|
| Literal scalar and support conventions | **PASS.** The exact Round-168 cardinal interpolant, Fourier convention, support suprema, floors, stars, profiles, parity, endpoints, and zero extension are retained. |
| Odd-prime coefficients | **PASS.** The six entries in (169.K4) match direct Euler expansion. |
| Exceptional \(p=2\) | **PASS.** Only \((0,0)\) and \((0,2)\) remain, with weights \(1,-1\); the residue factor is \(3/4\). |
| Collapsed Möbius multiplicity | **PASS.** All eight odd-prime states and both two-adic states give (169.K5) and (169.K24) exactly. |
| Weighted coefficient mass | **PASS.** (169.K6)--(169.K7) retain the exact Euler product, uniform \(\eta^{-3}\) cost, and convergent \((1,1)\)-mass. |
| Character-Poisson normalization | **PASS.** Gauss sum \(2i\), factor \(i/2\), odd \(k\), and scale \(k/(4Q)\) are exact. |
| Ordinary-Poisson normalization | **PASS.** The scale \(\ell/R\), factor \(1/R\), paired cosine, and overall factor \(2\) are exact. |
| Finite zero versus full residue | **PASS.** The finite \(R\)-range and full \(R\ge1\) residue are not identified; \(E_0=Z_{\mathrm{phys}}-R_\zeta\) has the correct sign. |
| Correction bound | **PASS.** The same one-cell integration by parts and convergent Euler mass prove all three bounds in (169.K10). |
| Completed functions and gamma data | **PASS.** Parities, conductors, roots, poles, Gauss sum, completions, quotient kernels, and contour orientation are complete. |
| Exact stationary phase and cone | **PASS.** (169.K16)--(169.K17) give \(k\ell=XQR\) and \(Q\ell\le Rk\le4Q\ell\). |
| Smooth collar qualification | **PASS.** (169.K18)--(169.K20) are explicitly confined to a favorable recombined block and retain the \(H/L\) deficit. |
| Exact Round-162 comparison | **PASS.** Every coefficient, parity branch, Fourier variable, and normalization returns coefficientwise. |
| Source scope | **PASS.** Only dated audited placements are parked; a future bespoke theorem remains open. |
| Provenance | **PASS.** Both accepted mathematical dependencies and every new internal deduction are assigned correctly; the source review supports the negative placement sentence. |
| Homogeneous extraction | **PASS.** All clauses form one exact self-return reduction and its restricted route consequence. |
| Downstream quarantine | **PASS.** No scalar owner, other channel, parent, bridge, theorem, or exponent is promoted. |

No numerical or external theorem is used to certify the internal kernel.

## 6. Dependencies and exact artifacts used

This verification used:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/candidates/conductor_round169_joint_fe_double_poisson_self_return.md`;
3. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/reviews/independent_coefficient_gamma_residue_transform_review.md`;
4. `rounds/codex-managed/m9-m2-hard-top-t1-joint-functional-equation-spectral-gate/reviews/source_spectral_power_self_return_review.md`;
5. `proofs/kernels/m9_m2_hard_top_t1_joint_functional_equation_double_poisson_self_return.md`.

The accepted Round-168 final-kernel verification was consulted only as
a formatting and verification-scope precedent; no mathematical claim was
imported from it.  No graph, active campaign, proof draft, validation
matrix, synthesis, state patch, source paper, sibling report, or other
kernel was read or edited for this task.

The kernel hash was computed directly from the final file.  No numerical
experiment or web lookup was used.

## 7. Recommended state effect

**PASS.**  Accept the final kernel at SHA-256

`b4c5e17aab5e586c1234af92f606dad1a8ccf199a108f3afc0ad5fd5977a37dc`.

It supports one `proved_internal` reduction node for the exact
coefficient law, weighted mass, collapsed Möbius identity, completed
functional-equation kernels, finite double-Poisson formula,
finite-zero/full-residue correction, and coefficientwise joint-FE
self-return.  It should remain only inconclusive evidence below the open
hard-TOP signed-cone owner.

Retain (169.K32) as the first open signed aggregate.  Reject only the
claims that bare joint functional equations, an infinite post-shift
absolute resummation of \(G\), the favorable smooth collar, or the dated
positive/source placements prove it.  Do not promote the polynomial
\(t=1\) scalar or residual, any other hard-TOP channel, hard TOP, BAL,
UNBAL, M9--M2, either direct M1 parent, GAR, endpoint uniformity, M9,
either bridge, the quarter theorem, or either exponent ledger.
