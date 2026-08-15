## 1. Result

**No-go result with an exact kernel reduction.**  The unmasked left-line
part of the alpha-bounded trace has an exact cosine/Poisson return.  After
the common $E_1+R_1$ artificial-pole cancellation, it is

\[
 \begin{aligned}
 \mathcal B_\zeta={}&2\sum_j\sum_{q\geq1}{\chi _4(q)\over q}
 \int_0^{N_X}y^{-3/4}\Delta_X(y)
 V_j^*\!\left({2\sqrt{Xy}\over D_jq}\right)
 \phi\!\left({y\over (H_j+1)q}\right)
 \sum_{h\geq1}\cos {2\pi hy\over q}\,dy,                 \tag{49.1}\\
 \Delta_X(y)={}&e\!\left(\sqrt{X\max(1,y)}\right)
                 -e\!\left(\sqrt{XN_X}\right).
 \end{aligned}
\]

All sums and inversions in (49.1) have the actual floors, stars, interior
profiles, and one-sided top profile; the \(h\)-sum is an Abel/symmetric
distributional limit, not an absolutely convergent series.  Poisson gives

\[
 2\sum_{h\geq1}\cos(2\pi ht)
   =\sum_{n\in\mathbb Z}\delta(t-n)-1.                    \tag{49.2}
\]

The comb part of (49.1) is the original active M1 angular kernel minus its
upper radial endpoint prefix.  The continuous \(-1\) part is exactly
$-\mathfrak R^{\rm ar}[R_1]$, including its sign.  Thus the unmasked
left-line operation returns to an equivalence-hard copy of the original
M1 problem modulo already accepted boundary modules.

This is not yet the complete alpha contribution.  The actual multiplier

\[
 \Theta_\alpha(\alpha,\beta)
   =(1-\psi(\beta))\psi(\alpha),\qquad
 \alpha=\beta+\mu+\nu,                                  \tag{49.3}
\]

is still a joint log-frequency projector, and its Cauchy--Green area
connector and the \(u,v\) face/axis/corner complex do not commute with the
Poisson split.  Consequently the surviving term is a *projected* lattice,
not literally the full M1 block.  The first unavailable object is the sum
of that projected lattice with its connector and outside-\(u,v\) complex.
The unprojected lattice has sharp all-absolute capacity
\(X^{1/8+o(1)}\) on the normalized scale, hence
\(X^{3/8+o(1)}\) after the single external \(X^{1/4}\) factor.  Integer
cosine coherence rules out a coefficientwise improvement.  This is an
absolute-capacity obstruction, not a signed lower bound.

## 2. Exact statement and hypotheses

Let

\[
 z=u+v,\qquad A=s-z/2,\qquad B=A+z,
\]

with $u=a+i\mu$, $v=b+i\nu$, and put

\[
 r=c'-{a+b\over2}>1,\qquad
 \gamma(u,v)={1\over4}-{u\over2}-v,\qquad
 \gamma _0={1\over4}-{a\over2}-b>0.                     \tag{49.4}
\]

Choose a left line

\[
 0<d<\gamma _0.                                         \tag{49.5}
\]

Then automatically $d<1-a-b$, so the nonprincipal series

\[
 L(1-A-u-v,\chi _4)
 =\sum_{q\geq1}\chi _4(q)q^{A+u+v-1}                   \tag{49.6}
\]

converges by Dirichlet's test, locally uniformly on finite boxes on
$\Re A=d$.  Formula (49.6) is used after a finite \(q\)-truncation.  The
unsigned \(h\)-series is first kept finite or Abel-damped on the original
$r>1$ line; its limit on $d<1$ is only distributional.

For fixed \((\mu,\nu)\), write

\[
 \theta_{\mu,\nu}(\beta)
 =\Theta_\alpha(\beta+\mu+\nu,\beta),\qquad
 D_A\Theta_\alpha=(\partial_\alpha+\partial_\beta)
                    \Theta_\alpha.                     \tag{49.7}
\]

If \(I_{\mu,\nu,S}=[-S-(\mu+\nu)/2,S-(\mu+\nu)/2]\), the exact finite
\(A\)-shift is from $r+iI_{\mu,\nu,S}$ to
$d+iI_{\mu,\nu,S}$.  Vertical contours are upward and horizontal
segments are written left-to-right.  With

\[
 \begin{aligned}
 \mathcal Q_j(u,v,A)={}&\mathcal A_j(u,v)R_{1,v}(1-A-z/2)
 X_\zeta(A)\zeta(A)L(1-A-z,\chi _4),                    \tag{49.8}\\
 \mathcal A_j(u,v)={}&\widehat W_j(u)\widehat\phi(v)
 \left({D_j\over2\sqrt X}\right)^u(H_j+1)^v,
 \end{aligned}
\]

Cauchy--Green gives, before any outside limit,

\[
 \boxed{
 I_r[\Theta_\alpha\mathcal Q_j]
 =I_d[\Theta_\alpha\mathcal Q_j]
  +H_A^+[\Theta_\alpha\mathcal Q_j]
  -H_A^-[\Theta_\alpha\mathcal Q_j]
  +P_\rho[\Theta_\alpha\mathcal Q_j]
  -\mathcal A_A[(D_A\Theta_\alpha)\mathcal Q_j].}       \tag{49.9}
\]

Here every \(I,H,P,\mathcal A\) carries its usual \(1/(2\pi i)\)
normalization; $\mathcal A_A$ is real area integration over
$[d,r]\times I_{\mu,\nu,S}$.  The pole $P_\rho$ is the artificial
\(A=\gamma(u,v)\) pole.  Its \(R_1\) residue is

\[
 \operatorname {Res}_{A=\gamma}R_{1,v}(1-A-z/2)
 =\pi i\sqrt X\int_1^{N_X}x^{-1/2}e(\sqrt{Xx})\,dx
 =e(\sqrt{XN_X})-e(\sqrt X),                            \tag{49.10}
\]

and it cancels the $E_1$ residue only under the same mask and finite
antecedent.

If the \(u,v\) contours are also transferred, let $F_u,F_v$ denote final
vertical plus oriented finite faces, $P_u,P_v$ the positive $u=0,v=0$
residues, and $\mathcal A_u,\mathcal A_v$ positive area integration.
The complete two-axis owner is

\[
 \begin{aligned}
 &F_uF_v[\Theta Q]+F_uP_v[\Theta Q]+P_uF_v[\Theta Q]
   +P_uP_v[\Theta Q]\\
 &\quad-F_u\mathcal A_v[(\partial_\nu\Theta)Q]
       -P_u\mathcal A_v[(\partial_\nu\Theta)Q]
       -\mathcal A_uF_v[(\partial_\mu\Theta)Q]
       -\mathcal A_uP_v[(\partial_\mu\Theta)Q]\\
 &\quad+\mathcal A_u\mathcal A_v
             [(\partial_\mu\partial_\nu\Theta)Q],     \tag{49.11}
 \end{aligned}
\]

where

\[
 \partial_\mu\Theta=\partial_\nu\Theta
 ={1\over2}(\partial_\alpha-\partial_\beta)\Theta,
 \qquad
 \partial_\mu\partial_\nu\Theta
 ={1\over4}(\partial_\alpha-\partial_\beta)^2\Theta.  \tag{49.12}
\]

Expanding the \(F\)'s gives every finite face, both axes, both
connector-face families, both connector-axis families, the mixed area,
and the joint corner exactly once.  Equations (49.9)--(49.12), together
with the common $E_1/R_1$ cancellation, are the exact finite
connector-completed alpha operator.

## 3. Proof or derivation

On $\Re A=d$, insert (49.6) and the finite/Abel \(h\)-regularization.  In
the $R_1$ bulk one has

\[
 \rho=\gamma-A
\]

and, after factoring the Mellin powers,

\[
 \begin{aligned}
 &\mathcal A_jq^{A+u+v-1}h^{-A}
 x^{\gamma-A-1/2}\\
 &\quad=q^{-1}x^{-1/4}\widehat W_j(u)\widehat\phi(v)
 \left({D_jq\over2\sqrt{Xx}}\right)^u
 \left({(H_j+1)q\over x}\right)^v
 \left({q\over hx}\right)^A.                          \tag{49.13}
 \end{aligned}
\]

The cosine inversion, with its sign fixed by $d<\Re\gamma$, is

\[
 \boxed{
 {1\over2\pi i}\int_{(d)}
 {X_\zeta(A)Y^{-A}\over\gamma-A}\,dA
 =2\int_0^1 t^{\gamma-1}\cos(2\pi Yt)\,dt.}            \tag{49.14}
\]

Indeed, \(X_\zeta\) has inverse Mellin kernel \(2\cos(2\pi Y)\), and
\((\gamma-A)^{-1}=\int_0^1t^{\gamma-A-1}dt\).  The opposite formula with
$-\int_1^\infty$ belongs to a line right of $\gamma$; using it here
would omit the artificial-pole crossing and produce the wrong radial
bracket.

Apply (49.14), set $y=xt$, and interchange only at finite regularization.
The domain $1\leq x\leq N_X,0<t<1$ becomes
\(0<y<N_X,\max(1,y)\leq x\leq N_X\).  Moreover

\[
 x^{\gamma-1/2}t^{\gamma-1}dt
 =x^{-1/2}y^{-3/4-u/2-v}\,dy.                          \tag{49.15}
\]

The \(u,v\) inversions therefore give the two actual profiles in (49.1),
and

\[
 -2\pi i\sqrt X\int_{\max(1,y)}^{N_X}
 x^{-1/2}e(\sqrt{Xx})\,dx
 =2\Delta_X(y).                                        \tag{49.16}
\]

This proves (49.1) with all constants and its lower-minus-upper sign.

Using (49.2), the positive lattice points give

\[
 \boxed{
 \begin{aligned}
 \mathcal L_X={}&\sum_j\sum_{q\geq1}\sum_{\substack{n\geq1\\nq\leq N_X}}^{*}
 \chi _4(q)(nq)^{-3/4}
 \{e(\sqrt{Xnq})-e(\sqrt{XN_X})\}\\
 &\qquad\times V_j^*\!\left({2\sqrt{Xn/q}\over D_j}\right)
 \phi\!\left({n\over H_j+1}\right).
 \end{aligned}}                                        \tag{49.17}
\]

There is no $n=0$ contribution: actual spatial support forces
$D_j\ll\sqrt{Xy}$, so the test amplitude vanishes in a neighborhood of
$y=0$.  The equality $nq=N_X$ has the inherited product star.  The
first phase in (49.17) and both profiles are exactly the active M1 angular
block (with \(n\) playing the original Vaaler height).  The second phase is
exactly its upper radial endpoint prefix.  Hence

\[
 \mathcal L_X=\mathcal M_{1,\mathrm{angular}}
               -\mathcal U_{N_X}.                      \tag{49.18}
\]

The continuous term in (49.2) is

\[
 -\sum_j\sum_q{\chi _4(q)\over q}\int_0^{N_X}
 y^{-3/4}\Delta_X(y)V_j^*\!\left({2\sqrt{Xy}\over D_jq}\right)
 \phi\!\left({y\over(H_j+1)q}\right)dy
 =-\mathfrak R^{\rm ar}[R_1].                          \tag{49.19}
\]

Consequently the exact unmasked return, in compact owner notation, is

\[
 \boxed{
 \mathcal B_\zeta=\mathcal L_X-\mathfrak R^{\rm ar}[R_1]
 =\mathcal M_{1,\mathrm{angular}}-\mathcal U_{N_X}
  -\mathfrak R^{\rm ar}[R_1].}                          \tag{49.19a}
\]

This sign also follows from

\[
 \operatorname {Res}_{A=0}\{X_\zeta(A)\zeta(A)\}
 =\operatorname {Res}_{A=0}\zeta(1-A)=-1.              \tag{49.20}
\]

Thus the comb is the angular survivor and \(-1\), not the comb, is the
$A=0/R_1$ arithmetic share.

It remains essential not to erase the mask.  Define the exact
log-frequency selector on a triple Mellin antecedent \(M\) by

\[
 \boxed{
 \mathsf P_\alpha[M](L_u,L_v,L_A)
 ={1\over(2\pi)^3}\int_{\mathbb R^3}
 \Theta_\alpha(\beta+\mu+\nu,\beta)
 M(\mu,\nu,\beta)e^{-i(\mu L_u+\nu L_v+\beta L_A)}
 \,d\mu\,d\nu\,d\beta.}                              \tag{49.21}
\]

Finite symmetric cutoffs are understood before the limit.  For fixed
\((\mu,\nu)\), (49.21) is convolution in
\(L_A=\log(hx/q)\) by the inverse Fourier transform of
\(\beta\mapsto\theta_{\mu,\nu}(\beta)\).  It therefore log-dilates the
comb $y/q\in\mathbb Z$; it is not a scalar weight on the lattice points.
The actual alpha bulk is
$\mathsf P_\alpha[\mathcal L_X-\mathfrak R^{\rm ar}[R_1]]$,
interpreted through the common finite antecedent, plus
the connector (49.9) and the complex (49.11).

For the actual hierarchical mask, \(\Theta_\alpha(\alpha,0)=0\) in a
neighborhood of the arithmetic pole.  Hence the alpha branch owns no new
$A=0$ residue.  This does **not** license deleting the projected
continuous term by itself: (49.21) does not commute termwise with a contour
residue decomposition.  The projected \(-1\) mode, the $D_A\Theta$
connector, and the common finite pole ledger must first be recombined; only
that aggregate routes $A=0$ wholly to the accepted unmasked
$\mathfrak R^{\rm ar}[R_1]$ owner.

Explicitly,

\[
 D_A\Theta_\alpha
 =(1-\psi(\beta))\psi'(\alpha)-\psi'(\beta)\psi(\alpha), \tag{49.21a}
\]

so both $\Theta_\alpha$ and its \(A\)-direction derivative vanish in a
neighborhood of $A=0$.  After aggregate pole routing, the genuinely
alpha-owned analytic survivor is only the projected lattice plus its
non-polar connector complex.  In graph terminology it is a projected GAR
return, not the unprojected GAR kernel and not a new scalar kernel with
better capacity.

Finally, if \(\psi(\alpha)\) is supported in \(|\alpha|\leq B_0\), then on
an \(s\)-horizontal side

\[
 |\alpha|\geq S-(U+V)/2.
\]

Thus \(S>(U+V)/2+B_0\) makes the \(A/s\) horizontal sides and all their
mask derivatives identically zero.  No analogous support argument removes
the \(u\)- or \(v\)-faces, because \(t\) can compensate either outside
height.  Their signed joint limit remains part of the survivor.

## 4. First doubtful or unproved step

The first unproved step is the passage from the exact finite identity
(49.9)--(49.12) to a bounded physical operator.  More explicitly, it is
the limit and target estimate for

\[
 \boxed{
 \mathcal S_\alpha=
 \mathsf P_\alpha[\mathcal L_X]
 -\mathsf P_\alpha[\mathfrak R^{\rm ar}[R_1]]
 -\mathcal A_A[(D_A\Theta_\alpha)\mathcal Q]
 +\mathcal X_{u=0}+\mathcal X_{v=0}+\mathcal X_{u=v=0}
 +\mathcal H_{u,v}+\mathcal C_{u,v},}                   \tag{49.22}
\]

where the last five symbols are exactly the face, connector-face,
connector-axis, axis, and corner terms expanded from (49.11), with their
oriented finite sides.  The accepted pole and endpoint modules may be
removed only after their aggregate one-count routing.

There are two precise reasons (49.22) is not yet controlled.

1. The strip connector in (49.9) spans $d\leq\Re A\leq r$.  On its
   right portion there is no simultaneous chamber for both the unsigned
   \(h\)-series and the \(q\)-series (49.6).  Replacing it by (49.17)
   silently drops the Cauchy--Green term.
2. Even after a justified physicalization, (49.18) shows that the lattice
   returns to the original M1 angular sum modulo a proved endpoint.  The
   projector (49.21) and connector complex may contain useful signed
   cancellation, but no accepted estimate extracts it.

For a fixed active scale, write $H_j\asymp D_jX^{-1/4}$ and on profile
support $q\asymp Xn/D_j^2$.  The all-absolute mass of (49.17) is

\[
 \begin{aligned}
 \sum_{n\leq H_j}q\,(nq)^{-3/4}
 &\asymp\sum_{n\leq H_j}
  X^{1/4}D_j^{-1/2}n^{-1/2}\\
 &\asymp X^{1/4}D_j^{-1/2}H_j^{1/2}
  \asymp X^{1/8}.                                       \tag{49.23}
 \end{aligned}
\]

Thus absolute values lose $X^{1/8}$ normalized.  The outside-height
version of the same failure is the known one-large-gamma capacity
$U^{c'-1/2-\Re z/2}$ after the sole hard-top inverse-height factor.
Neither quantity is \(O(X^\varepsilon)\) uniformly.  Equation (49.23) is
the sharp first capacity of the explicit lattice, not a lower bound for
the signed projected operator.

## 5. Control tests and outcomes

1. **Branch orientation — pass.**  $A=s-z/2$ has height $\beta$,
   $B=s+z/2=A+z$ has height $\alpha$.  The alpha-bounded branch leaves
   \(h^{-A}\) unsigned and puts \(\chi _4(q)\) only in
   \(L(1-B,\chi _4)\).
2. **Common antecedent and mask connectors — pass at finite level.**
   Equations (49.9)--(49.12) start from one $E_1+R_1$ antecedent and
   contain $D_A\Theta$, both one-axis derivatives, both
   connector-axis families, the mixed derivative, and the corner.  The
   projected lattice alone fails this control.
3. **Pole and residue ledger — pass.**  $A=1$ is removable;
   $A=\gamma$ has the residue (49.10) and cancels only against $E_1$;
   the \(-1\) term is exactly the residue \(-1\) at $A=0$ and equals
   $-\mathfrak R^{\rm ar}[R_1]$.  The actual alpha mask has zero
   $A=0$ ownership, so this share must be reconciled with, not added to,
   the accepted R1 module.
4. **Signed height order — unresolved, with the first step named.**  The
   \(s\)-faces vanish under the stated nested support separation, but the
   \(u,v\) face/connector/axis complex in (49.22) has no proved signed
   physical limit.  No absolute limit was taken.
5. **Integer cosine resonance — falsifies coefficientwise decay.**  At
   \(y/q\in\mathbb Z\), every \(\cos(2\pi hy/q)=1\).  This is exactly the
   comb in (49.2), so an unsigned high-\(h\) cancellation lemma is false.
6. **Unsigned coefficient control — obstruction quantified.**  Replacing
   the remaining signs by absolute values gives (49.23), namely
   \(X^{1/8+o(1)}\) normalized per scale.  Period-four Abel in \(h\) is
   unavailable because the \(h\)-coefficients are unsigned.
7. **Radial and external normalization — pass.**  The factor
   $-\pi i\sqrt X$ in $R_1$, the cosine factor \(2\), and
   \(d e(\sqrt{Xx})/dx=\pi i\sqrt Xx^{-1/2}e(\sqrt{Xx})\)
   give the positive $2\Delta_X$ in (49.1).  The physical operator is
   exactly

   \[
    -{4\over\pi}X^{1/4}\Re\{e(1/8)\mathcal S_\alpha\},
   \]

   with the external factor applied once.  The absolute lattice capacity
   would therefore be \(X^{3/8+o(1)}\) physically.
8. **Outside height limit — partial pass/no-go.**  Compact alpha support
   kills the radial \(s\)-sides for
   \(S>(U+V)/2+B_0\).  It does not kill the \(u,v\) outside sides; their
   aggregate limit is unproved.
9. **Downstream scope — pass.**  Nothing here estimates the complete alpha
   branch, the swept operator, the post-FE vector kernel, M9-M1, M9, or the
   Gauss-circle error.

No numerical experiment and no external source were used; the work was
100 percent analytical/algebraic.

## 6. Dependencies and exact artifacts used

Files accessed (this report is **non-isolated candidate evidence**):

- `protocol.md`;
- `state/proof_obligations.yml`, specifically the accepted finite vector
  identity, diagonal coordinates, endpoint subtraction, side-removal,
  endpoint/R1 modules, and beta/alpha ownership statements;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-partial-functional-equation-transitions/synthesis.md`;
- `rounds/codex-managed/m9-m1-partial-functional-equation-transitions/reports/blind_partial_FE_factorization.md`;
- `rounds/codex-managed/m9-m1-beta-wrapper-closure-audit/synthesis.md`;
- `rounds/codex-managed/m9-m1-r1-arithmetic-residue/synthesis.md`;
- `rounds/codex-managed/m9-m1-alpha-bounded-zeta-high-transition/derivation_packet.md`
  (accessed as a redundant normalization cross-check);
- `rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md`
  (accessed only to cross-check the finite-kernel normalization already
  present in the permitted proof graph);
- the assigned brief
  `rounds/codex-managed/m9-m1-alpha-bounded-zeta-high-transition/briefs/alpha_physical_kernel_attack.md`.

No beta terminal estimate was imported into the alpha branch.  The only
transform used beyond those artifacts was the elementary tempered
distribution identity (49.2), proved by completing the Fourier series to
$h\in\mathbb Z$.

The two cross-check files just identified were not listed in the discovery
brief's selected-context block.  Their mathematical content was redundant
with the permitted brief/proof-graph statements, but the access is recorded
here so that the conductor can treat this report as non-isolated candidate
evidence rather than silently overstate its context isolation.

## 7. Recommended state effect

**Retain** `M9-M1-alpha-bounded-zeta-high-transition-bound` as open.

**Promote as reductions only**, after independent seam review:

- the finite connector formula (49.9)--(49.12) and exact support removal
  of the \(s\)-horizontal sides;
- the unmasked physical cosine formula (49.1);
- the Poisson split (49.17)--(49.20): lattice equals the active M1 angular
  block minus the upper endpoint prefix, while the continuous term is
  exactly $-\mathfrak R^{\rm ar}[R_1]$;
- the conclusion that the actual survivor is a log-frequency-projected
  equivalence-hard return, not an unprojected new kernel.

**Record as a no-go** the claim that the pure cosine inversion by itself
closes the alpha transition.  It omits the mask connector and returns a
lattice of normalized all-absolute capacity \(X^{1/8+o(1)}\).  The next
campaign, if this report survives review, should freeze (49.22) and seek
one signed theorem for the projector-plus-connector complex; it should not
redo the beta branch or treat (49.17) as a target estimate.
