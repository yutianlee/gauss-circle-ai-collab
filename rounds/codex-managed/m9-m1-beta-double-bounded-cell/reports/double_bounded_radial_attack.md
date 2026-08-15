# Round 42 discovery report: direct estimate of the double-bounded beta cell

Task: `double_bounded_radial_attack`  
Role: discovery  
Allocation: 100% analytical/algebraic; no computation and no external theorem

## 1. Result

The beta-owned double-bounded cell is target-safe.  Compact support in
both

\[
 \beta\quad\hbox{and}\quad \alpha=L+\beta
\]

makes \(L\) compact, keeps both exact gamma quotients in a pole-free
compact set, and removes every need for Stirling or Morse localization.
After the hard top is integrated as its signed Plemelj distribution, the
complete compact archimedean amplitude satisfies the stronger estimate

\[
 \boxed{
  \sup_{1\le x\le N_X}\{|\mathcal A(x)|+x|\mathcal A'(x)|\}
  \ll \log^C(2X). }
 \tag{42.1}
\]

Consequently

\[
 \sup_{1\le x\le N_X}|\mathcal A(x)|
 +\int_1^{N_X}|\mathcal A'(x)|\,dx
 \ll \log^{C+1}(2X)\ll_\varepsilon X^\varepsilon .
 \tag{42.2}
\]

The exact radial integration by parts then gives

\[
 \sqrt X\int_1^{N_X}x^{-3/2-b/2}e(\sqrt{Xx})
 \mathcal A(x)\,dx
 \ll \log^{C+1}(2X).                                  \tag{42.3}
\]

The boundary bracket in this integration by parts is proved directly.
It is not identified with, or estimated by, a beta-masked share of the
previously routed global endpoint module.  Equivalently, at finite
sections one may use the exact identity \(R_1=G-E_1\) with the same
central mask on all three terms: on
\(\Re\rho=-1-b/2\), the central restrictions of both \(G\) and \(E_1\)
are directly bounded.  This resolves the potentially fatal ownership
seam.

The sums over \(h\) and \(q\) converge absolutely on \(c'=5/4\), the
actual dyadic scale sum costs only \(O(\log X)\), and every power of
\(b^{-1}\), every height modulation, and every allowed finite connector
derivative is polylogarithmic.  Restoring the external normalization once
therefore gives

\[
 \boxed{\mathfrak M_{\mathrm{db}}(X)
  =O_\varepsilon(X^{1/4+\varepsilon}).}              \tag{42.4}
\]

This proves only the double-bounded beta cell.  It does not by itself
close the alpha-bounded branch or the full swept operator.

## 2. Exact statement and hypotheses

Use

\[
 \sigma=c'=\frac54,\qquad b=\frac1{\log(2X)},\qquad
 \zeta=a+b,
\]

\[
 r=\frac54-\frac\zeta2,qquad
 p=\frac54+\frac\zeta2,qquad
 D_j=2^{-j}\lfloor\sqrt X\rfloor,qquad
 H_j=\lfloor D_jX^{-1/4}\rfloor,
 \tag{42.5}
\]

on the accepted contour range

\[
 a\ge0,\qquad a+b<\frac12,qquad \frac a2+b<\frac14.
 \tag{42.6}
\]

Let \(0\le j\le J\) denote the actual active scales, so
\(D_j\ge X^{1/4}\), and put

\[
 \Theta_{\rm db}(L,\beta)=\psi(\beta)\chi_0(L+\beta),
 \tag{42.7}
\]

where \(\chi_0\) is the fixed central cutoff from the statement packet.
Thus, on its support,

\[
 |\beta|+|L+\beta|+|L|\le C_0.                       \tag{42.8}
\]

Set the exact gamma-quotient unit phase

\[
 \mathfrak u_\Gamma(\alpha,\beta)
 =\exp\!\left(i\left\{\alpha\log\frac4\pi
                    -\beta\log\pi\right\}\right),
 \tag{42.9a}
\]

and

\[
 \mathcal G(\alpha,\beta)
 =c_{\sigma,\zeta}\mathfrak u_\Gamma(\alpha,\beta)
  R_\alpha(\alpha)R_\beta(\beta),
 \tag{42.9}
\]

with the two exact gamma ratios in the statement packet, and define

\[
 \ell_{j,q,x}=\log\frac{D_j}{2q\sqrt{Xx}},\qquad
 \gamma_{j,x}=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x},
 \tag{42.10}
\]

\[
 g_{j,h,q,x}(L,\beta)
 =\Theta_{\rm db}(L,\beta)\mathcal G(L+\beta,\beta)
   e^{iL\ell_{j,q,x}}e^{-i\beta\log(hqx)},
 \tag{42.11}
\]

\[
 p_{j,x}(\nu)=e^{i\gamma_{j,x}\nu}\widehat\phi(b+i\nu),
 \quad
 A(L,\beta)=-1-\frac b2-i(L+\beta),
 \tag{42.12}
\]

\[
 D(L,\nu;\beta)
 =A(L,\beta)+\frac i2(L-\nu)
 =-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right).
 \tag{42.13}
\]

For an exact numerator \(H_x(L,\nu)=g_x(L,\beta)p_x(\nu)\), define the
complete physical hard-top functional by first taking the signed limit

\[
 \begin{aligned}
 \mathsf P_x[H](L,\beta)
 :={}&\frac12\frac{H_x(L,L)}{A(L,\beta)}\\
 &-\frac{i}{2\pi}\operatorname {PV}
   \int_{\mathbb R}\frac{H_x(L,\nu)}
   {(L-\nu)D(L,\nu;\beta)}\,d\nu .
 \end{aligned}                                           \tag{42.14}
\]

The constant-numerator PV can be evaluated exactly.  Indeed, with
\(y=L-\nu\),

\[
 \operatorname {PV}\int_{\mathbb R}
 \frac{dy}{y\{A+iy/2\}}=\frac{i\pi}{A}.
 \tag{42.15}
\]

Therefore (42.14) is equivalently the cancellation-preserving formula

\[
 \boxed{
 \mathsf P_x[H](L,\beta)
 =\frac{g_x(L,\beta)p_x(L)}{A(L,\beta)}
 -\frac{i g_x(L,\beta)}{2\pi}
  \int_{\mathbb R}
  \frac{p_x(\nu)-p_x(L)}
  {(L-\nu)D(L,\nu;\beta)}\,d\nu .}                 \tag{42.16}
\]

The second integral in (42.16) is absolutely convergent.  Formula
(42.16) is the exact signed diagonal followed by the off-diagonal divided
difference; it is not an absolute interpretation of the hard pole.

Let

\[
 \widehat W_+(u)=\frac1u+\widehat W_{+,r}(u)          \tag{42.17}
\]

be the exact top split.  Put \(\mathscr W_{0,r}(y)=
\widehat W_{+,r}(iy)\), with the accepted limiting real part understood,
and for \(j\ge1\) put
\(\mathscr W_{j,r}(y)=\widehat W(a+iy)\).  The ordinary smooth share is

\[
 \mathsf S_{j,x}(L,\beta)
 =\frac{g_{j,h,q,x}(L,\beta)}{2\pi}
  \int_{\mathbb R}
  \frac{p_{j,x}(\nu)\mathscr W_{j,r}(L-\nu)}
       {D(L,\nu;\beta)}\,d\nu .                    \tag{42.18}
\]

There is no second Plemelj operation in (42.18).  With
\(\mathbf1_{j=0}\mathsf P_x\) denoting the singular top only, define
the compact amplitude

\[
\boxed{
\begin{aligned}
 \mathcal A(x)={}&-\pi i
 \sum_{j=0}^{J}\sum_{h,q\ge1}
 \chi_4(q)h^{-r}q^{-p}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b\\
 &\times\int_{\mathbb R^2}\frac{dL\,d\beta}{(2\pi)^2}
 \left\{
   \mathbf1_{j=0}\mathsf P_{j,h,q,x}(L,\beta)
   +\mathsf S_{j,x}(L,\beta)
 \right\}.
\end{aligned}}                                             \tag{42.19}
\]

For the complete post-routing central cell, (42.19) is summed over the
finite one-count family of ordinary beta-mask and beta-connector product
shares accepted in Round 41.  In each summand, the exact compact
multiplier or its fixed finite derivative replaces the corresponding
factor in \(g\), and \(\mathscr W_{j,r}\) is replaced by its exact
normalized profile derivative.  Formula (42.19), with this finite
one-count sum understood, is the complete compact functional.  All these
replacements obey the same estimates below.  No endpoint, side,
arithmetic, axial, connector-axis, collision, corner, or artificial-pole
module is inserted into (42.19).

The normalized double-bounded terminal contribution before the external
\(X^{1/4}\) factor is exactly

\[
 \mathcal I_{\rm db}(X)
 =\sqrt X\int_1^{N_X}x^{-3/2-b/2}e(\sqrt{Xx})
  \mathcal A(x)\,dx .                                \tag{42.20}
\]

## 3. Proof or derivation

### Compact gamma and profile bounds

The real parts of the four gamma arguments in (42.9) are

\[
 \frac98+\frac\zeta4,\quad
 \frac38-\frac\zeta4,\quad
 \frac58-\frac\zeta4,\quad
 -\frac18+\frac\zeta4.                              \tag{42.21}
\]

Under (42.6), the first three stay positive and the last lies in
\((-1/8,0)\); if it approaches zero, the reciprocal gamma factor tends
to zero rather than developing a pole.  Hence, on (42.8), the exact
quotient, the explicitly retained unit phase (42.9a), and every fixed
derivative required by a connector satisfy

\[
 |\mathcal G|+|\partial_\alpha\mathcal G|
 +|\partial_\beta\mathcal G|\ll \log^C(2X).          \tag{42.22}
\]

No Stirling formula and no passage through \(b=0\) is used.

On the actual ranges,

\[
 |\gamma_{j,x}|\ll\log(2X).                          \tag{42.23}
\]

The accepted cubic height tail and its local positive-line bounds imply,
for a polylogarithmic \(P_X\),

\[
 \|p_{j,x}\|_1+\|p'_{j,x}\|_\infty
 +\|\nu p_{j,x}(\nu)\|_1
 +\sup_\nu(1+|\nu|)^3|p_{j,x}(\nu)|
 \le P_X.                                            \tag{42.24}
\]

This is precisely the first moment needed when \(x\) is differentiated.
The regular top and interior profiles, with every required fixed
derivative, have rapid vertical decay uniformly in \(j\).

### Signed top and its one-x-derivative

Because \(L,\beta\) are compact and \(\Re D=-1-b/2\),

\[
 |A|\asymp1,qquad |D(L,\nu;\beta)|\asymp1+|\nu|.
 \tag{42.25}
\]

For \(|L-\nu|\le1\), the numerator in the integral of (42.16) is
bounded by \(|L-\nu|\|p'_x\|_\infty\).  For
\(|L-\nu|>1\), use the endpoint form and (42.24).  It follows that

\[
 \int_{\mathbb R}
 \frac{|p_x(\nu)-p_x(L)|}
 {|L-\nu|\,|D(L,\nu;\beta)|}\,d\nu\ll P_X.          \tag{42.26}
\]

Thus both the exact diagonal and the off-diagonal term in (42.16) are
\(O(P_X)\).  This proof forms the signed diagonal first; the unintegrated
constant numerator still has a nonintegrable absolute \(1/\nu\) tail.

The unit phase \(\mathfrak u_\Gamma(\alpha,\beta)\) in (42.9a) is
independent of \(x\).  Thus all \(x\)-dependence inside \(g_xp_x\) is
still exactly the scale, height, and beta phase displayed in the
statement packet, and

\[
 x\partial_x\{g_x(L,\beta)p_x(\nu)\}
 =-i\eta\,g_x(L,\beta)p_x(\nu),
 \quad
 \eta=\frac{L+\nu}{2}+\beta,                         \tag{42.27}
\]

and on the diagonal \(\eta=\alpha=L+\beta\).  Differentiating the
off-diagonal numerator in (42.16) gives exactly

\[
 x\partial_x\{g_x[p_x(\nu)-p_x(L)]\}
 =-ig_x\{\eta p_x(\nu)-\alpha p_x(L)\}.             \tag{42.28}
\]

Near \(\nu=L\), the braces in (42.28) are
\(O(P_X|L-\nu|)\).  Away from the diagonal, (42.24), compactness of
\(\alpha\), and (42.25) give

\[
 \int_{\mathbb R}
 \frac{|\eta p_x(\nu)-\alpha p_x(L)|}
 {|L-\nu|\,|D(L,\nu;\beta)|}\,d\nu\ll P_X.          \tag{42.29}
\]

Equations (42.16), (42.28), and (42.29) therefore prove

\[
 |\mathsf P_x[H]|+x|\partial_x\mathsf P_x[H]|
 \ll P_X.                                            \tag{42.30}
\]

For a smooth share, \(|\eta/D|\ll1\).  Absolute integration in
(42.18), rapid spatial decay, and (42.24) immediately give

\[
 |\mathsf S_{j,x}|+x|\partial_x\mathsf S_{j,x}|
 \ll P_X.                                            \tag{42.31}
\]

The cutoff \(\chi_0(\alpha)\), beta mask, normalized Mellin profiles,
and floors do not move with \(x\).  Staying in the Mellin representation
is important: no derivative of a sharp physical support or of a star is
created.

### Absolute coefficient and scale ledger

The coefficient series is already in its absolute chamber.  From
(42.6),

\[
 r-1=\frac14-\frac{a+b}{2}>\frac b2,
 \]

so

\[
 \sum_{h\ge1}h^{-r}\log^k(2h)\ll_k b^{-k-1}
 \ll\log^{k+1}(2X),                                  \tag{42.32}
\]

while

\[
 \sum_{q\ge1}q^{-p}\log^k(2q)\ll_k1.                \tag{42.33}
\]

The fixed logarithmic weights in (42.32)--(42.33) cover every allowed
finite connector derivative.  The character \(\chi_4(q)\) is retained
exactly; only \(|\chi_4(q)|\le1\) is used.  Thus this particular compact
cell is also absolutely safe for unsigned coefficients.  This does not
imply the false unsigned global analogue, because the large transition,
endpoint, and other swept branches are absent.

For every active scale,

\[
 \left(\frac{D_j}{2\sqrt X}\right)^a\le1,
 \qquad
 H_j+1\le2D_jX^{-1/4}\le2X^{1/4},                   \tag{42.34}
\]

with the exact floor retained.  Therefore

\[
 \sum_{j=0}^{J}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b
 \ll J+1\ll\log(2X).                                \tag{42.35}
\]

Equations (42.22), (42.30)--(42.35), fixed compact \((L,\beta)\)
volume, and the exact residual contour factors prove (42.1).  They also
show explicitly that the internal \(\sqrt X\) in the raw coefficient is
the only remaining power of \(X\) before radial oscillation.

### Exact radial integration by parts and endpoint ownership

Put \(N=N_X\), \(y=\sqrt x\), and recall
\(e(t)=\exp(2\pi it)\).  Then

\[
 \mathcal I_{\rm db}
 =2\sqrt X\int_1^{\sqrt N}
  y^{-2-b}e(\sqrt Xy)\mathcal A(y^2)\,dy.
 \tag{42.36}
\]

One integration by parts is the exact identity

\[
\begin{aligned}
 \mathcal I_{\rm db}={}&\frac1{\pi i}
 \left[e(\sqrt Xy)y^{-2-b}\mathcal A(y^2)
 \right]_{1}^{\sqrt N}\\
 &-\frac1{\pi i}\int_1^{\sqrt N}e(\sqrt Xy)
 \frac d{dy}\{y^{-2-b}\mathcal A(y^2)\}\,dy .
\end{aligned}                                           \tag{42.37}
\]

In particular, the boundary bracket has the exact signs

\[
 \frac1{\pi i}\left{
 N^{-1-b/2}e(\sqrt{XN})\mathcal A(N)
 -e(\sqrt X)\mathcal A(1)\right\}.                  \tag{42.38}
\]

The derivative integral is bounded by

\[
 (2+b)\int_1^{\sqrt N}y^{-3-b}|\mathcal A(y^2)|\,dy
 +\int_1^N x^{-1-b/2}|\mathcal A'(x)|\,dx,          \tag{42.39}
\]

which is polylogarithmic by (42.1)--(42.2).  This proves (42.3).

The two traces in (42.38) have the full endpoint coefficients supplied by
continuous radial integration by parts; that operation creates no half
coefficient.  Every half-weight comes only from a pre-existing starred
profile or inversion convention.  In particular, the hard-top
half/delta coefficient in (42.14), the physical top spatial half-star,
and every accepted product equality star remain exactly inside
\(\mathcal A(1)\) and \(\mathcal A(N)\).  The height profile vanishes at
its equality endpoint and creates no new half-star.  Thus every actual
star is retained once.

Most importantly, (42.38) is not imported from the proved unmasked
endpoint theorem.  It is bounded directly by (42.1).  At finite physical
sections this can also be checked before integration by parts from

\[
 \Theta_{\rm db}R_1
 =\Theta_{\rm db}G-\Theta_{\rm db}E_1.              \tag{42.40}
\]

On \(\rho=-1-b/2-i\eta\), direct integration of the defining radial
transform gives

\[
 |G(\rho)|+|\partial_\eta G(\rho)|\ll1,             \tag{42.41}
\]

and its exact endpoint expression gives

\[
 |E_1(\rho)|+|\partial_\eta E_1(\rho)|
 \ll\frac{1+N^{-1-b/2}\log N}{1+|\eta|}.            \tag{42.42}
\]

For the \(E_1\) term, (42.26)--(42.29) apply directly.  For the \(G\)
term there is no \(D^{-1}\) tail: in the hard-top Hilbert integral one
subtracts \(p_x(L)\) only on \(|L-\nu|\le1\), while the far integral is
kept as \(p_x(\nu)/(L-\nu)\).  Its value and logarithmic-height
derivative are bounded by (42.24), (42.41), and the same local Taylor
argument.  Thus both centrally masked terms in (42.40), including their
physical-height limits, are polylogarithmic.  Equation (42.40) is used
only as an internal identity for the already-owned \(R_1\) terminal
remainder.  Neither term is added to the globally routed
endpoint/arithmetic module, and the artificial pole is not crossed
because \(\Re\rho=-1-b/2\).  This proves rather than assumes the required
central masked endpoint control.

Finally, the once-restored physical normalization is

\[
 -\frac4\pi X^{1/4}\Re\{e(1/8)\mathcal I_{\rm db}(X)\}.
 \tag{42.43}
\]

Equations (42.3) and (42.43) prove (42.4).  The powers are: internal
\(\sqrt X\), exactly canceled by radial oscillation; no remaining
\(X,D_j,H_j,h,q\) power after (42.32)--(42.35); and one external
\(X^{1/4}\).

## 4. First doubtful or unproved step

No analytic step remains doubtful in the frozen compact-cell theorem.
The delicate step was (42.37)--(42.42): a radial integration by parts on
the post-routing terminal remainder creates central masked endpoint
traces, and the global endpoint theorem alone would not estimate them.
Here they are explicitly bounded from (42.1), equivalently by the exact
same-mask identity (42.40), so that gap is closed without double counting.

The first unproved step is downstream and operator-level: the conductor
must compose this compact-cell lemma with the Round-41 large-alpha
package under the accepted one-count partition and then close the stated
beta-transition obligation.  The alpha-bounded zeta-high branch remains
a separate contribution to the swept operator.

## 5. Required control test and outcome

1. **Exact double-bounded cutoff:** pass.  Equation (42.8) follows from
   \(\psi(\beta)\chi_0(\alpha)\), so \(L=\alpha-\beta\) is compact.
2. **Compact gamma and pole control:** pass.  The exact argument ledger
   (42.21) has no gamma pole; no Stirling or \(b\downarrow0\) limit is
   used.
3. **Signed top and diagonal:** pass.  The half-delta/PV functional is
   formed first, (42.15) evaluates its diagonal, and only the divided
   difference in (42.16) is absolutely integrated.
4. **One \(x\)-derivative:** pass.  The exact multiplier is \(-i\eta/x\),
   not merely \(-i\nu/(2x)\); (42.24), (42.28), and (42.29) give the
   required first-moment control.
5. **Hard and smooth profiles:** pass.  The singular \(1/u\) occurs once
   in (42.14); (42.18) is ordinary integration and uses rapid spatial
   decay.
6. **Absolute coefficients and character:** pass.  Equations
   (42.32)--(42.33) retain \(\chi_4(q)\) but do not need cancellation.
7. **Dyadic scales, floors, and smallest block:** pass.  Equation (42.35)
   retains \(H_j+1\) exactly, covers \(H_j=1\), and costs one logarithm.
8. **Radial power and endpoint signs:** pass.  Equations (42.36)--(42.39)
   cancel the internal \(\sqrt X\); the upper-minus-lower bracket and all
   genuine stars are explicit.
9. **Aggregate ownership:** pass by direct proof, not by a forbidden
   inference.  Equations (42.40)--(42.42) bound the masked traces within
   the terminal identity and do not repeat the globally removed module.
10. **External normalization:** pass.  Equation (42.43) restores
    \(X^{1/4}\) once and yields (42.4).

## 6. Dependencies and exact artifacts used

The report used exactly:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-beta-double-bounded-cell/statement_packet.md`;
5. `rounds/codex-managed/m9-m1-beta-transition-connector/synthesis.md`;
6. `rounds/codex-managed/m9-m1-beta-physical-module-transfer/synthesis.md`;
7. `rounds/codex-managed/m9-m1-beta-actual-profile-Cauchy-tail/synthesis.md`;
8. `rounds/codex-managed/m9-m1-beta-axial-subtracted-terminal-symbol/synthesis.md`;
9. `rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/synthesis.md`;
10. `proofs/kernels/m9_m1_beta_off_diagonal_product_cell.md`;
11. the Round-42 task brief.

The accepted inputs are the exact beta gamma factorization, including
the unit phase (42.9a), terminal raw
coefficient and phase, hierarchical ownership, singular/smooth top split,
signed physical-height limit, finite one-count product forms, exact
floors and stars, global post-routing ownership, and the common
\(G=E_1+R_1\) identity.  Equations (42.14)--(42.43), including the
compact amplitude, its \(x\)-derivative, absolute coefficient/scale
ledger, direct masked endpoint control, and radial estimate, were derived
here.  No other Round-42 report, numerical experiment, web source, or
external theorem was used.

## 7. Recommended state effect

Promote, after statement-only and hostile validation, the direct
double-bounded beta-cell lemma (42.1)--(42.4), including:

- the exact compact signed-top functional (42.16);
- the complete value and one-\(x\)-derivative bound;
- absolute \(h,q\) convergence and the exact dyadic floor ledger;
- the direct radial integration-by-parts endpoint estimate; and
- the ownership statement that these newly generated traces are bounded
  internally and are not a second copy of the global endpoint module.

Then compose the lemma with the accepted Round-41 large-alpha package to
close the beta branch in its stated scope.  Retain the alpha-bounded
zeta-high branch, M9-M1, M9, and the Gauss-circle target as open.

Reject the shortcuts that (i) take absolute values before Plemelj,
(ii) differentiate only the \(\nu\)-modulation while omitting the
\(L,\beta\) phases, (iii) cite the unmasked endpoint theorem for a masked
central trace, (iv) add a half coefficient to an ordinary radial
integration-by-parts endpoint, or (v) use Stirling in the compact gamma
box.
