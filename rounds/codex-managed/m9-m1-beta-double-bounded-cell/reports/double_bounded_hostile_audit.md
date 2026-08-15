# Round 42 hostile audit: the double-bounded terminal cell

Task: `double_bounded_hostile_audit`  
Role: hostile seam reviewer  
Allocation: 100% analytical/algebraic; no numerics and no web source

## 1. Result

The compact-cell route survives, but two exact corrections are mandatory.

First, a radial integration by parts on the beta-owned central cell does
produce a *masked* endpoint bracket.  That bracket is not the unmasked
three-branch endpoint module proved in Round 36, so citing the global
endpoint theorem for it would be invalid.  This is a real ownership
obstruction to that citation, but not to the estimate.  The bracket is a
new local term with compact alpha and beta, and it is directly
polylogarithmically bounded.  Equivalently, on the already fixed terminal
line one may use the pointwise meromorphic identity

\[
 R_1(\rho)=G(\rho)-E_1(\rho)                         \tag{42H.1}
\]

and estimate both compactly masked summands without moving another contour
or extracting another residue.  This use of (42H.1) does not reintroduce a
globally owned module.

Second, integration by parts in the continuous radial integral has full
endpoint coefficients.  It does not give endpoint halves.  Existing stars
from symmetric Mellin inversion and physical profile equalities remain
where they already occur, but they do not multiply the radial integration-
by-parts bracket by one half.

With those corrections, the actual complete central amplitude satisfies
the stronger estimate

\[
 \sup_{1\le x\le N_X}
 \left\{|\mathcal A(x)|+|x\mathcal A'(x)|\right\}
 \ll P_X,\qquad P_X\ll \log^C(2X),                  \tag{42H.2}
\]

and therefore

\[
 \sup_x|\mathcal A(x)|+
 \int_1^{N_X}|\mathcal A'(x)|\,dx
 \ll \log^{C+1}(2X)\ll_\varepsilon X^\varepsilon. \tag{42H.3}
\]

One exact radial integration by parts then gives

\[
 \sqrt X\int_1^{N_X}x^{-3/2-b/2}e(\sqrt{Xx})
 \mathcal A(x)\,dx\ll P_X.                         \tag{42H.4}
\]

Thus the normalized double-bounded beta terminal cell is
\(O_\varepsilon(X^\varepsilon)\), and restoration of the already fixed
external multiplier makes it
\(O_\varepsilon(X^{1/4+\varepsilon})\).  This proof is absolute in
\(h,q\); it does not use character cancellation and does not claim the
remaining alpha-owned branch or all of M9-M1.

There is one further harmless exact-form correction.  With the displayed
definitions of the two gamma ratios, the full quotient is

\[
 K_z(1-s)=C_{\sigma,\zeta}
 e^{i\{\alpha\log(4/\pi)-\beta\log\pi\}}
 R_\alpha(\alpha)R_\beta(\beta),                   \tag{42H.5}
\]

not merely a fixed \(c_{\sigma,\zeta}R_\alpha R_\beta\).  The omitted
factor has unit modulus, is independent of \(x\), and is smooth on the
central box, so it changes no estimate below; it must nevertheless be
retained in an exact proof.

## 2. Exact statement and hypotheses

Let

\[
 c'=\sigma=\frac54,\qquad b=\frac1{\log(2X)},\qquad
 \zeta=a+b,
\]

\[
 r=\frac54-\frac\zeta2>1,\qquad
 p=\frac54+\frac\zeta2>1,
\]

on the accepted contour, with \(a+b<1/2\) and
\(a/2+b<1/4\).  The chosen contour is fixed with the usual uniform
margin; equivalently any dependence on \((r-1)^{-1}\) is part of the
accepted polylogarithmic contour constant.  Put

\[
 u=a+i(L-\nu),\qquad v=b+i\nu,\qquad
 s=\frac54+i\left(\frac L2+\beta\right),
\]

\[
 \alpha=L+\beta,\qquad
 \eta=\frac{L+\nu}{2}+\beta,\qquad
 \rho=-1-\frac b2-i\eta.                            \tag{42H.6}
\]

Let

\[
 \Theta_c(\alpha,\beta)=\psi(\beta)\chi_0(\alpha)
\]

be the hierarchical beta-owned central cutoff.  Its support gives
\(|\alpha|+|\beta|+|L|\le B_c\), with \(B_c\) fixed independently of
\(X,j,h,q,x\).  It is independent of \(x\).  Use the exact gamma quotient
(42H.5), not a Stirling approximation.  Its gamma arguments have real
parts

\[
 \frac98+\frac\zeta4,\quad
 \frac38-\frac\zeta4,\quad
 \frac58-\frac\zeta4,\quad
 -\frac18+\frac\zeta4.                              \tag{42H.7}
\]

For \(0<\zeta<1/2\), no numerator gamma has a pole, the first denominator
has positive real part, and the possible approach of the last denominator
to the gamma pole at zero produces a zero of its reciprocal rather than a
blow-up.  Hence the quotient and the finitely many derivatives used here
are uniformly bounded on the compact box, up to the accepted contour
constant.  Also

\[
 |\rho|\asymp1+|\eta|,
 \qquad \left|\frac\eta\rho\right|\le1.             \tag{42H.8}
\]

For a frozen \((j,h,q)\), remove only the radial real weight and radial
phase from the terminal \(R_1\) integrand.  The remaining exact unit phase
is

\[
\begin{aligned}
 \Theta_{j,h,q,x}(L,\nu,\beta)
 ={}&L\log\frac{D_j}{2q\sqrt{Xx}}
 +\nu\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}\\
 &-\beta\log(hqx),
\end{aligned}                                      \tag{42H.9}
\]

so that

\[
 x\partial_x\Theta_{j,h,q,x}=-\eta.                \tag{42H.10}
\]

The actual height transform and its needed derivatives have the accepted
cubic tail and first moment,

\[
 \sum_{m\le2}\int_{\mathbb R}(1+|\nu|)
 \left|\partial_\nu^m
 \left(e^{i\gamma_x\nu}\widehat\phi(b+i\nu)\right)
 \right|d\nu\ll P_X,
 \quad P_X\ll b^{-C}\log^C(2X),                    \tag{42H.11}
\]

where

\[
 \gamma_x=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}.
\]

Only this genuine finite moment is used.  Smooth top and interior spatial
profiles have their accepted rapidly decreasing normalized Mellin
profiles.  The singular hard-top term is acted on by the signed Plemelj
distribution before any absolute value; its diagonal logarithmic section
is retained.  Smooth shares retain ordinary \(\mu=L-\nu\) integration.

Define \(\mathcal A(x)\) to be the resulting complete compact alpha-beta,
height, profile, and \((h,q,j)\) amplitude, with the factors

\[
 h^{-r}q^{-p}
 \left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b       \tag{42H.12}
\]

included, and with
\((-\pi i\sqrt X)x^{-3/2-b/2}e(\sqrt{Xx})\) and the
external \(X^{1/4}\) multiplier excluded.  Every globally routed endpoint,
arithmetic, axial, connector-axis, collision, corner, side, and crossed
artificial-residue module remains excluded exactly once.

Under these hypotheses, (42H.2)--(42H.4) hold.  At a continuous radial
endpoint, the integration-by-parts coefficient is full.  Any physical
profile or product equality star already present in \(\mathcal A\) is
retained with its accepted value.

## 3. Proof or derivation

### 3.1 Compact geometry and the gamma factors

The two cutoffs bound \(\alpha\) and \(\beta\); hence
\(L=\alpha-\beta\) is bounded.  This is the essential difference from the
large-alpha cells.  Formula (42H.7) proves compact gamma boundedness
without Stirling and without a pole loss.  The real part of \(\rho\) in
(42H.6) is \(-1-b/2\), so neither \(\rho^{-1}\) nor the diagonal
denominator

\[
 A(L)=-1-\frac b2-i(L+\beta)
\]

has a \(b^{-1}\) singularity.  The only allowed \(b\)-loss is from the
already audited height-profile seminorm, and
\(b^{-C}=\log^C(2X)\).

### 3.2 Signed hard top and ordinary smooth shares

Before the top distribution is applied, a singular local numerator is a
finite sum of terms of the form

\[
 B_x(L,\nu,\beta)
 =\Theta_c(\alpha,\beta)C(\alpha,\beta)
 \frac{e^{i\Theta_{j,h,q,x}(L,\nu,\beta)}
 \widehat\phi(b+i\nu)}{\rho},                       \tag{42H.13}
\]

where \(C\) is a bounded compact gamma/profile coefficient.  From
(42H.8)--(42H.11),

\[
 \int\left(|B_x|+|x\partial_xB_x|
 +|\partial_\nu B_x|\right)d\nu\ll P_X.             \tag{42H.14}
\]

Indeed, the exact phase derivative is especially favorable:

\[
 x\partial_x\left(\frac{e^{i\Theta_{j,h,q,x}}}{\rho}\right)
 =-i\frac\eta\rho e^{i\Theta_{j,h,q,x}},            \tag{42H.15}
\]

which is uniformly bounded.  Estimating the separated phases instead
would still work using the first \(\nu\)-moment in (42H.11), but (42H.15)
shows that no hidden height loss occurs.

Apply

\[
 \frac1{2\pi}\frac1{0^++i(L-\nu)}
 =\frac12\delta_L(\nu)
 -\frac{i}{2\pi}\operatorname {PV}\frac1{L-\nu}.   \tag{42H.16}
\]

On \(|\nu-L|\le1\), subtract \(B_x(L,L,\beta)\) before taking an
absolute value.  The difference is controlled by the last term of
(42H.14).  Its constant-numerator part is exactly the accepted signed
logarithmic Cauchy section; because \(L\) is compact and
\(\Re A<-1\), its logarithm and its \(x\)-derivative are uniformly
bounded on all affine endpoint sections.  On \(|\nu-L|>1\), (42H.14)
allows ordinary absolute integration.  This proves the bound for the
singular top term and its \(x\)-derivative without ever absolutely
integrating the diagonal kernel.  Every smooth spatial share is easier:
its ordinary \(\mu\)-integration has a rapidly decreasing translated
profile and obeys the same estimate.  Fixed hard jumps and existing stars
do not move with \(x\), so differentiating in \(x\) creates no support
measure.

### 3.3 Absolute coefficient and scale ledger

The contour powers give

\[
 \sum_{h\ge1}h^{-r}\ll_{a,b}1,
 \qquad
 \sum_{q\ge1}q^{-p}\ll_{a,b}1.                     \tag{42H.17}
\]

Thus the product restriction, oddness, \(\chi_4(q)\), and endpoint stars
may all be retained and then discarded in the upper bound.  No character
cancellation is needed.  For the actual dyadic scales,

\[
 \left(\frac{D_j}{2\sqrt X}\right)^a\le1,
 \qquad
 (H_j+1)^b\le \exp\{b\log(2+X^{1/4})\}\ll1,         \tag{42H.18}
\]

and there are \(O(\log X)\) scales.  Therefore

\[
 \sum_j\left(\frac{D_j}{2\sqrt X}\right)^a
 (H_j+1)^b\ll\log(2X).                              \tag{42H.19}
\]

Floors, the top scale, and the smallest active height do not change this
bound.  Combining (42H.14), the signed top estimate, and
(42H.17)--(42H.19) proves (42H.2).  It follows that

\[
 \int_1^{N_X}|\mathcal A'(x)|dx
 \le P_X\int_1^{N_X}\frac{dx}{x}
 \ll P_X\log(2X),                                  \tag{42H.20}
\]

which is (42H.3).

### 3.4 Exact radial integration by parts

Let \(E(x)=e(\sqrt{Xx})\).  Then

\[
 E'(x)=\pi i\sqrt X\,x^{-1/2}E(x).
\]

Consequently

\[
\begin{aligned}
 \sqrt X\int_1^{N_X}x^{-3/2-b/2}E(x)\mathcal A(x)dx
 ={}&\frac1{\pi i}
 \left[x^{-1-b/2}E(x)\mathcal A(x)\right]_1^{N_X}\
 &-\frac1{\pi i}\int_1^{N_X}E(x)
 \frac d{dx}\{x^{-1-b/2}\mathcal A(x)\}dx.
\end{aligned}                                      \tag{42H.21}
\]

The lower bracket is \(O(P_X)\), the upper bracket is
\(O(P_XN_X^{-1-b/2})\), and the derivative integral is \(O(P_X)\) by
(42H.2).  This proves (42H.4).  For the raw coefficient
\(-\pi i\sqrt X\), (42H.21) is equivalently the same identity with the
appropriate overall minus sign and no missing contour factor.  Singular
top shares leave the accepted two residual \((2\pi)^{-1}\) measures;
smooth shares retain their three ordinary contour measures.  These are
fixed constants and are not dropped.

The two endpoint terms in (42H.21) have full coefficients.  The star in a
symmetric inverse-Mellin equality changes the value assigned to a physical
profile at its boundary; it does not halve the Lebesgue integration-by-
parts bracket.

### 3.5 Why the masked endpoint is not a blocker

At fixed \(\rho\), put

\[
 G(\rho)=\int_1^{N_X}x^{\rho-1}E(x)dx,
 \qquad
 E_1(\rho)=
 \frac{N_X^\rho E(N_X)-E(1)}{\rho},                 \tag{42H.22}
\]

and \(C=\pi i\sqrt X\).  Exact integration by parts gives

\[
 G(\rho)=E_1(\rho)
 -\frac C\rho\int_1^{N_X}x^{\rho-1/2}E(x)dx
 =E_1(\rho)+R_1(\rho).                              \tag{42H.23}
\]

Thus (42H.1) is exactly the same operation as (42H.21).  On the terminal
line,

\[
 |G(\rho)|+|\partial_\rho G(\rho)|\ll1,
 \qquad
 |E_1(\rho)|+|\partial_\rho E_1(\rho)|
 \ll\frac1{1+|\eta|},                              \tag{42H.24}
\]

because \(\Re\rho=-1-b/2\), while
\(N_X^{\Re\rho}\ll N_X^{-1}\).  Multiplication by the compact gamma
factors and the cubic height profile makes both the hard-top Plemelj
functional and every smooth functional bounded by the same \(P_X\).
The coefficient ledger (42H.17)--(42H.19) then bounds the compactly masked
\(G\) and \(E_1\) terms separately.  In particular the internal
\(C=\pi i\sqrt X\) in the defining \(R_1\) integral has disappeared
exactly in (42H.23); it leaves no residual \(X^{1/2}\) loss.

No contour is shifted in this argument, and \(\rho=0\) is not crossed.
The common package has already been simplified to \(R_1\); (42H.1) is
applied only afterward on its fixed terminal line.  Hence there is no new
arithmetic residue, artificial residue, axial term, connector, collision,
or corner, and no cutoff derivative.  One must not identify the masked
\(E_1\) in (42H.22) with the accepted aggregate endpoint module.  It is
estimated here as one term of a local algebraic equality and is not added
to, subtracted from, or bounded by that global module.

This proves that the ownership seam blocks only the proposed shortcut of
citing Round 36.  It does not block the corrected direct estimate.

## 4. First doubtful or unproved step

The first invalid step in the uncorrected route would be:

> after integrating the central cell by parts in \(x\), identify its
> boundary bracket with the already routed physical endpoint module.

Round 36 proves the endpoint/arithmetic identity only after the three
hierarchical mask shares are summed at finite contour height.  It proves no
separate masked endpoint limit.  The central bracket therefore cannot be
discarded, transferred, or bounded by citation to that theorem.

The first exact replacement is (42H.21), retaining and directly estimating
the full local bracket, or equivalently (42H.23), estimating both local
summands.  Once this is written, the proof above has no remaining analytic
gap.  Before promotion, the conductor should also correct the missing unit
gamma phase in the statement packet and replace any suggestion of half-
weighted radial integration-by-parts endpoints by the full coefficients.

## 5. Required control test and outcome

1. **Exact central geometry:** pass.  Compact alpha and beta imply compact
   \(L\); neither \(\nu\) nor \(\mu\) is incorrectly declared compact.
2. **Gamma poles and \(b\)-loss:** pass with correction (42H.5).  The real
   parts (42H.7) avoid numerator poles; inverse denominators do not blow up.
   Also \(|A|,|\rho|\ge1\), so the only \(b\)-loss is polylogarithmic.
3. **Signed top:** pass.  The diagonal logarithmic section is formed before
   absolute values, and the off-diagonal difference is absolutely
   integrable.  No absolute integral of the \(1/\nu\) diagonal tail is used.
4. **One \(x\)-derivative:** pass.  The exact combined phase gives
   \(x\partial_x\Theta=-\eta\), and \(|\eta/\rho|\le1\).  The genuine
   cubic profile also supplies the required first \(\nu\)-moment.
5. **Moving supports:** pass.  \(\psi(\beta)\), \(\chi_0(\alpha)\), the
   physical height sections, floors, hard jumps, and stars do not move with
   \(x\).  Thus no delta mass is created by \(\partial_x\).
6. **Absolute \(h,q\) convergence:** pass.  Both exponents exceed one;
   replacing \(\chi_4\) by its modulus is harmless for this compact cell.
   This does not prove the false unsigned global analogue because all
   noncompact branches remain outside the lemma.
7. **Dyadic scales:** pass.  The exact factors are bounded as in (42H.18)
   and the actual scale count is \(O(\log X)\).
8. **Radial endpoint signs and stars:** pass after correction.  The upper
   bracket is positive and the lower bracket negative in (42H.21), both at
   full weight.  Existing physical stars are retained elsewhere.
9. **Global ownership:** the attempted aggregate-module citation fails.
   The direct local bracket estimate and the fixed-line identity
   \(R_1=G-E_1\) pass and create no double count.
10. **Contour constants and normalization:** pass.  The raw
    \(-\pi i\sqrt X\), residual \((2\pi)^{-1}\) measures, floors, stars,
    and the external \(X^{1/4}\) factor are all restored exactly once.

No numerical control was used.

## 6. Dependencies and exact artifacts used

- `protocol.md`.
- `state/proof_obligations.yml` and `state/active_campaign.yml`.
- `rounds/codex-managed/m9-m1-beta-double-bounded-cell/statement_packet.md`.
- Round 20 synthesis for the exact diagonal gamma factorization.
- Round 21 synthesis for the full-weight radial endpoint recurrence.
- Round 26 synthesis for hierarchical beta ownership of the central box.
- Round 36 synthesis and its common-module review for aggregate-before-limit
  endpoint/arithmetic routing.
- Round 38 synthesis for the lawful terminal line, positive-b Cauchy limit,
  and actual height tail.
- Round 39 synthesis for contour measures and singular-versus-smooth
  normalization.
- Round 40 synthesis for the signed diagonal Cauchy section.
- Round 41 synthesis and
  `proofs/kernels/m9_m1_beta_off_diagonal_product_cell.md` for the exact
  phase/profile split and common post-routing ownership.

No other Round-42 report was read.  No external theorem, web source, or
computation was used.

## 7. Recommended state effect

**Promote, with exact corrections.**  Promote the beta-owned
double-bounded terminal-cell estimate (42H.2)--(42H.4) and its physical
\(O_\varepsilon(X^{1/4+\varepsilon})\) consequence.  Record explicitly
that the local integration-by-parts endpoint bracket is directly estimated,
not identified with the globally routed endpoint module.  The equivalent
fixed-terminal-line use of \(R_1=G-E_1\) is lawful only without another
contour displacement or separate residue extraction.

Also record two rejected shortcuts: a half-weighted continuous radial
integration-by-parts bracket, and a termwise masked appeal to the Round-36
endpoint theorem.  Correct the exact compact gamma formula by retaining
the unit phase in (42H.5).  Retain the alpha-owned bounded branch, complete
beta-transition assembly until its one-count recombination is checked,
M9-M1, M9-M2, M9, and the Gauss-circle target as open.
